# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

# Function for initiating the UI

global hefcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

def hefcSetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def interruptControl(NVIC, event):
    global hefcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, hefcInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, hefcInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)


def instantiateComponent(hefcComponent):

    global hefcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    hefcInstanceName = hefcComponent.createStringSymbol("HEFC_INSTANCE_NAME", None)
    hefcInstanceName.setVisible(False)
    hefcInstanceName.setDefaultValue(hefcComponent.getID().upper())

    Log.writeInfoMessage("Running HEFC")

    # Create the top menu
    hefcMenu = hefcComponent.createMenuSymbol(None, None)
    hefcMenu.setLabel("Hardware Settings ")

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    # Flash Details
    hefcFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"IFLASH\"]")
    if hefcFlashNode != None:
        hefcFlashStartAddress = hefcComponent.createStringSymbol("FLASH_START_ADDRESS", hefcMenu)
        hefcFlashStartAddress.setVisible(False)
        hefcFlashStartAddress.setDefaultValue(hefcFlashNode.getAttribute("start"))

        # Flash size
        hefcFlashSize = hefcComponent.createStringSymbol("FLASH_SIZE", hefcMenu)
        hefcFlashSize.setVisible(False)
        hefcFlashSize.setDefaultValue(hefcFlashNode.getAttribute("size"))

        # Flash Page size
        hefcFlashProgramSize = hefcComponent.createStringSymbol("FLASH_PROGRAM_SIZE", hefcMenu)
        hefcFlashProgramSize.setVisible(False)
        hefcFlashProgramSize.setDefaultValue(hefcFlashNode.getAttribute("pagesize"))

    #Flash Erase size
    hefcFlashEraseSize = hefcComponent.createStringSymbol("FLASH_ERASE_SIZE", hefcMenu)
    hefcFlashEraseSize.setVisible(False)
    hefcFlashEraseSize.setDefaultValue("4096")

    # Create a Checkbox to enable disable interrupts
    hefcInterrupt = hefcComponent.createBooleanSymbol("INTERRUPT_ENABLE", hefcMenu)
    hefcInterrupt.setLabel("Enable Interrupts")

    hefcMemoryDriver = hefcComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", hefcMenu)
    hefcMemoryDriver.setLabel("Memory Driver Connected")
    hefcMemoryDriver.setVisible(False)
    hefcMemoryDriver.setDefaultValue(False)

    offsetStart = (int(hefcFlashSize.getValue(),16) / 2)

    nvmOffset = str(hex(int(hefcFlashStartAddress.getValue(),16) + offsetStart))

    hefcMemoryStartAddr = hefcComponent.createStringSymbol("START_ADDRESS", hefcMenu)
    hefcMemoryStartAddr.setLabel("NVM Media Start Address")
    hefcMemoryStartAddr.setVisible(False)
    hefcMemoryStartAddr.setDefaultValue(nvmOffset[2:])
    hefcMemoryStartAddr.setDependencies(hefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    hefcMemoryMediaSize = hefcComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", hefcMenu)
    hefcMemoryMediaSize.setLabel("NVM Media Size (KB)")
    hefcMemoryMediaSize.setVisible(False)
    hefcMemoryMediaSize.setDefaultValue(memMediaSizeKB)
    hefcMemoryMediaSize.setDependencies(hefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    hefcMemoryEraseEnable = hefcComponent.createBooleanSymbol("ERASE_ENABLE", None)
    hefcMemoryEraseEnable.setLabel("NVM Erase Enable")
    hefcMemoryEraseEnable.setVisible(False)
    hefcMemoryEraseEnable.setDefaultValue(True)
    hefcMemoryEraseEnable.setReadOnly(True)

    hefcMemoryEraseBufferSize = hefcComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", hefcMenu)
    hefcMemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    hefcMemoryEraseBufferSize.setVisible(False)
    hefcMemoryEraseBufferSize.setDefaultValue(int(hefcFlashEraseSize.getValue()))
    hefcMemoryEraseBufferSize.setDependencies(hefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    hefcMemoryEraseComment = hefcComponent.createCommentSymbol("ERASE_COMMENT", hefcMenu)
    hefcMemoryEraseComment.setVisible(False)
    hefcMemoryEraseComment.setLabel("*** Should be equal to Sector Erase Size ***")
    hefcMemoryEraseComment.setDependencies(hefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    writeApiName = hefcInstanceName.getValue() + "_PageWrite"
    eraseApiName = hefcInstanceName.getValue() + "_SectorErase"

    hefcWriteApiName = hefcComponent.createStringSymbol("WRITE_API_NAME", hefcMenu)
    hefcWriteApiName.setVisible(False)
    hefcWriteApiName.setReadOnly(True)
    hefcWriteApiName.setDefaultValue(writeApiName)

    hefcEraseApiName = hefcComponent.createStringSymbol("ERASE_API_NAME", hefcMenu)
    hefcEraseApiName.setVisible(False)
    hefcEraseApiName.setReadOnly(True)
    hefcEraseApiName.setDefaultValue(eraseApiName)

    interruptVector = hefcInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE"
    interruptHandler = hefcInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER"
    interruptHandlerLock = hefcInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = hefcInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    hefcinterruptControl = hefcComponent.createBooleanSymbol("NVIC_HEFC_ENABLE", None)
    hefcinterruptControl.setDependencies(interruptControl, ["INTERRUPT_ENABLE"])
    hefcinterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")
    # Generate Output Header
    hefcHeaderFile = hefcComponent.createFileSymbol("HEFC_FILE_0", None)
    hefcHeaderFile.setSourcePath("../peripheral/hefc_44123/templates/plib_hefc.h.ftl")
    hefcHeaderFile.setMarkup(True)
    hefcHeaderFile.setOutputName("plib_" + hefcInstanceName.getValue().lower() + ".h")
    hefcHeaderFile.setOverwrite(True)
    hefcHeaderFile.setDestPath("peripheral/hefc/")
    hefcHeaderFile.setProjectPath("config/" + configName + "/peripheral/hefc/")
    hefcHeaderFile.setType("HEADER")
    # Generate Output source
    hefcSourceFile = hefcComponent.createFileSymbol("HEFC_FILE_1", None)
    hefcSourceFile.setSourcePath("../peripheral/hefc_44123/templates/plib_hefc.c.ftl")
    hefcSourceFile.setMarkup(True)
    hefcSourceFile.setOutputName("plib_" + hefcInstanceName.getValue().lower() + ".c")
    hefcSourceFile.setOverwrite(True)
    hefcSourceFile.setDestPath("peripheral/hefc/")
    hefcSourceFile.setProjectPath("config/" + configName + "/peripheral/hefc/")
    hefcSourceFile.setType("SOURCE")

    hefcSystemDefFile = hefcComponent.createFileSymbol("HEFC_FILE_2", None)
    hefcSystemDefFile.setType("STRING")
    hefcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    hefcSystemDefFile.setSourcePath("../peripheral/hefc_44123/templates/system/definitions.h.ftl")
    hefcSystemDefFile.setMarkup(True)

    hefcSystemInitFile = hefcComponent.createFileSymbol("HEFC_FILE_3", None)
    hefcSystemInitFile.setType("STRING")
    hefcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    hefcSystemInitFile.setSourcePath("../peripheral/hefc_44123/templates/system/initialization.c.ftl")
    hefcSystemInitFile.setMarkup(True)
