"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

global fcwInstanceName

def fcwSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])

def setFCWInterruptData(status):

    Database.setSymbolValue("core", fcwInterruptVector, status, 1)
    Database.setSymbolValue("core", fcwInterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", fcwInterruptHandler, fcwInstanceName.getValue() + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", fcwInterruptHandler, "FCW_Handler", 1)

def updateFCWInterruptData(symbol, event):

    if event["id"] == "INTERRUPT_ENABLE":
        setFCWInterruptData(event["value"])

    if fcwInterruptEnable.getValue() == True and Database.getSymbolValue("core", fcwInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(fcwComponent):

    global fcwInstanceName
    global fcwInterruptVector
    global fcwInterruptHandlerLock
    global fcwInterruptHandler
    global fcwInterruptVectorUpdate
    global fcwInterruptEnable

    fcwInstanceName = fcwComponent.createStringSymbol("FCW_INSTANCE_NAME", None)
    fcwInstanceName.setVisible(False)
    fcwInstanceName.setDefaultValue(fcwComponent.getID().upper())
    Log.writeInfoMessage("Running " + fcwInstanceName.getValue())

    fcwFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FCR_PFM\"]")
    if fcwFlashNode == None:
        fcwFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FLASH_PFM\"]")

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    flashStartAddress = fcwFlashNode.getAttribute("start")

    #Flash Address
    fcwSym_FLASH_ADDRESS = fcwComponent.createStringSymbol("FLASH_START_ADDRESS", None)
    fcwSym_FLASH_ADDRESS.setVisible(False)
    fcwSym_FLASH_ADDRESS.setDefaultValue(flashStartAddress)

    #Flash size
    fcwSym_FLASH_SIZE = fcwComponent.createStringSymbol("FLASH_SIZE", None)
    fcwSym_FLASH_SIZE.setVisible(False)
    fcwSym_FLASH_SIZE.setDefaultValue(fcwFlashNode.getAttribute("size"))

    pageSize = "4096"
    rowSize = "1024"
    #Flash Row size
    fcwSym_FLASH_PROGRAM_SIZE = fcwComponent.createStringSymbol("FLASH_PROGRAM_SIZE", None)
    fcwSym_FLASH_PROGRAM_SIZE.setVisible(False)
    fcwSym_FLASH_PROGRAM_SIZE.setDefaultValue(rowSize)

    #Flash Page size
    fcwSym_ERASE_SIZE = fcwComponent.createStringSymbol("FLASH_ERASE_SIZE", None)
    fcwSym_ERASE_SIZE.setVisible(False)
    fcwSym_ERASE_SIZE.setDefaultValue(pageSize)

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    fcwSym_MemoryDriver = fcwComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    fcwSym_MemoryDriver.setLabel("Memory Driver Connected")
    fcwSym_MemoryDriver.setVisible(False)
    fcwSym_MemoryDriver.setDefaultValue(False)

    offsetStart = (int(fcwSym_FLASH_SIZE.getValue(),16) / 2)

    fcwOffset = int(flashStartAddress,16) + offsetStart
    fcwOffset = format(fcwOffset, 'x')

    fcwSym_MemoryStartAddr = fcwComponent.createStringSymbol("START_ADDRESS", None)
    fcwSym_MemoryStartAddr.setLabel("FCW Media Start Address")
    fcwSym_MemoryStartAddr.setVisible(False)
    fcwSym_MemoryStartAddr.setDefaultValue(fcwOffset)
    fcwSym_MemoryStartAddr.setDependencies(fcwSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    fcwSym_MemoryMediaSize = fcwComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", None)
    fcwSym_MemoryMediaSize.setLabel("FCW Media Size (KB)")
    fcwSym_MemoryMediaSize.setVisible(False)
    fcwSym_MemoryMediaSize.setDefaultValue(memMediaSizeKB)
    fcwSym_MemoryMediaSize.setDependencies(fcwSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    fcwSym_MemoryEraseEnable = fcwComponent.createBooleanSymbol("ERASE_ENABLE", None)
    fcwSym_MemoryEraseEnable.setLabel("FCW Erase Enable")
    fcwSym_MemoryEraseEnable.setVisible(False)
    fcwSym_MemoryEraseEnable.setDefaultValue(True)
    fcwSym_MemoryEraseEnable.setReadOnly(True)

    fcwSym_MemoryEraseBufferSize = fcwComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", None)
    fcwSym_MemoryEraseBufferSize.setLabel("FCW Erase Buffer Size")
    fcwSym_MemoryEraseBufferSize.setVisible(False)
    fcwSym_MemoryEraseBufferSize.setDefaultValue(int(fcwSym_ERASE_SIZE.getValue()))
    fcwSym_MemoryEraseBufferSize.setDependencies(fcwSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    fcwSym_MemoryEraseComment = fcwComponent.createCommentSymbol("ERASE_COMMENT", None)
    fcwSym_MemoryEraseComment.setVisible(False)
    fcwSym_MemoryEraseComment.setLabel("*** Should be equal to Page Erase Size ***")
    fcwSym_MemoryEraseComment.setDependencies(fcwSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    ################# Interrupt Settings ###########################

    # Get register names, mask values, bit shifts based on vector number
    fcwInterruptVector = "FCW_INTERRUPT_ENABLE"
    fcwInterruptHandler = "FCW_INTERRUPT_HANDLER"
    fcwInterruptHandlerLock = "FCW_INTERRUPT_HANDLER_LOCK"
    fcwInterruptVectorUpdate = "FCW_INTERRUPT_ENABLE_UPDATE"

    #Configures the library for interrupt mode operations
    fcwInterruptEnable = fcwComponent.createBooleanSymbol("INTERRUPT_ENABLE", None)
    fcwInterruptEnable.setLabel("Enable Interrupt?")
    fcwInterruptEnable.setDefaultValue(False)

    fcwInterruptComment = fcwComponent.createCommentSymbol("FCW_INTRRUPT_ENABLE_COMMENT", None)
    fcwInterruptComment.setLabel("Warning!!! " + fcwInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    fcwInterruptComment.setVisible(False)
    fcwInterruptComment.setDependencies(updateFCWInterruptData, ["INTERRUPT_ENABLE", "core." + fcwInterruptVectorUpdate])

    setFCWInterruptData(False)

    fcwSym_preProgramEnable = fcwComponent.createBooleanSymbol("FCW_PRE_PRGM_ENABLE", None)
    fcwSym_preProgramEnable.setLabel("Enable Pre Program")
    fcwSym_preProgramEnable.setDescription("Enabling Pre-Programing increases endurance of Flash but slows the write/erase operation a little")
    fcwSym_preProgramEnable.setVisible(True)
    fcwSym_preProgramEnable.setDefaultValue(True)

    # Below create family-specific API needed by ftl file
    writeApiName = fcwComponent.getID().upper() + "_RowWrite"
    eraseApiName = fcwComponent.getID().upper() + "_PageErase"

    fcwWriteApiName = fcwComponent.createStringSymbol("WRITE_API_NAME", None)
    fcwWriteApiName.setVisible(False)
    fcwWriteApiName.setReadOnly(True)
    fcwWriteApiName.setDefaultValue(writeApiName)

    fcwEraseApiName = fcwComponent.createStringSymbol("ERASE_API_NAME", None)
    fcwEraseApiName.setVisible(False)
    fcwEraseApiName.setReadOnly(True)
    fcwEraseApiName.setDefaultValue(eraseApiName)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    fcwSym_HeaderFile = fcwComponent.createFileSymbol("FCW_HEADER", None)
    fcwSym_HeaderFile.setSourcePath("../peripheral/fcw_03433/templates/plib_fcw.h.ftl")
    fcwSym_HeaderFile.setOutputName("plib_"+fcwInstanceName.getValue().lower()+".h")
    fcwSym_HeaderFile.setDestPath("/peripheral/fcw/")
    fcwSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/fcw/")
    fcwSym_HeaderFile.setType("HEADER")
    fcwSym_HeaderFile.setMarkup(True)

    fcwSym_SourceFile = fcwComponent.createFileSymbol("FCW_SOURCE", None)
    fcwSym_SourceFile.setSourcePath("../peripheral/fcw_03433/templates/plib_fcw.c.ftl")
    fcwSym_SourceFile.setOutputName("plib_"+fcwInstanceName.getValue().lower()+".c")
    fcwSym_SourceFile.setDestPath("/peripheral/fcw/")
    fcwSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/fcw/")
    fcwSym_SourceFile.setType("SOURCE")
    fcwSym_SourceFile.setMarkup(True)

    fcwSystemDefFile = fcwComponent.createFileSymbol("FCW_SYS_DEF", None)
    fcwSystemDefFile.setSourcePath("../peripheral/fcw_03433/templates/system/definitions.h.ftl")
    fcwSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    fcwSystemDefFile.setType("STRING")
    fcwSystemDefFile.setMarkup(True)

    fcwSystemInitFile = fcwComponent.createFileSymbol("FCW_SYS_INIT", None)
    fcwSystemInitFile.setSourcePath("../peripheral/fcw_03433/templates/system/initialization.c.ftl")
    fcwSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    fcwSystemInitFile.setType("STRING")
    fcwSystemInitFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        fcwSym_HeaderFile.setSecurity("SECURE")
        fcwSym_SourceFile.setSecurity("SECURE")
        fcwSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")
        fcwSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")