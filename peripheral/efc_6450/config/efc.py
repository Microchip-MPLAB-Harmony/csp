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

#Function for initiating the UI

global efcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock
global waitStates

def waitStateUpdate(symbol, event):
    global waitStates
    cpuFreq = event["value"]
    for key in sorted(waitStates.keys()):
        if int(cpuFreq) <= int(key):
            print cpuFreq
            print key
            symbol.setValue(waitStates.get(key), 2)
            break
            
def efcSetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def interruptControl(NVIC, event):
    global efcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, efcInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, efcInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def instantiateComponent(efcComponent):

    global efcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    efcInstanceName = efcComponent.createStringSymbol("EFC_INSTANCE_NAME", None)
    efcInstanceName.setVisible(False)
    efcInstanceName.setDefaultValue(efcComponent.getID().upper())

    Log.writeInfoMessage("Running EEFC")

    global waitStates
    waitStates = {}
    waitStates = Database.sendMessage("core", "WAIT_STATES", waitStates)

    #Create the top menu
    efcMenu = efcComponent.createMenuSymbol(None, None)
    efcMenu.setLabel("Hardware Settings ")

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    #Flash Details
    efcFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"IFLASH\"]")
    if efcFlashNode != None:
        efcFlashStartAddress = efcComponent.createStringSymbol("FLASH_START_ADDRESS", efcMenu)
        efcFlashStartAddress.setVisible(False)
        efcFlashStartAddress.setDefaultValue(efcFlashNode.getAttribute("start"))

        #Flash size
        efcFlashSize = efcComponent.createStringSymbol("FLASH_SIZE", efcMenu)
        efcFlashSize.setVisible(False)
        efcFlashSize.setDefaultValue(efcFlashNode.getAttribute("size"))

        #Flash Page size
        efcFlashProgramSize = efcComponent.createStringSymbol("FLASH_PROGRAM_SIZE", efcMenu)
        efcFlashProgramSize.setVisible(False)
        efcFlashProgramSize.setDefaultValue(efcFlashNode.getAttribute("pagesize"))

    #Flash Erase size
    efcFlashEraseSize = efcComponent.createStringSymbol("FLASH_ERASE_SIZE", efcMenu)
    efcFlashEraseSize.setVisible(False)
    efcFlashEraseSize.setDefaultValue("8192")

    # Flash Read Wait State (RWS).
    nvm_rws = efcComponent.createIntegerSymbol("NVM_RWS", efcMenu)
    nvm_rws.setDefaultValue(6)
    nvm_rws.setLabel("Wait States")
    nvm_rws.setDependencies(waitStateUpdate, ["core.MASTER_CLOCK_FREQUENCY"])

    #Create a Checkbox to enable disable interrupts
    efcInterrupt = efcComponent.createBooleanSymbol("INTERRUPT_ENABLE", efcMenu)
    efcInterrupt.setLabel("Enable Interrupts")

    efcMemoryDriver = efcComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", efcMenu)
    efcMemoryDriver.setLabel("Memory Driver Connected")
    efcMemoryDriver.setVisible(False)
    efcMemoryDriver.setDefaultValue(False)

    offsetStart = (int(efcFlashSize.getValue(),16) / 2)

    nvmOffset = str(hex(int(efcFlashStartAddress.getValue(),16) + offsetStart))

    efcMemoryStartAddr = efcComponent.createStringSymbol("START_ADDRESS", efcMenu)
    efcMemoryStartAddr.setLabel("NVM Media Start Address")
    efcMemoryStartAddr.setVisible(False)
    efcMemoryStartAddr.setDefaultValue(nvmOffset[2:])
    efcMemoryStartAddr.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    efcMemoryMediaSize = efcComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", efcMenu)
    efcMemoryMediaSize.setLabel("NVM Media Size (KB)")
    efcMemoryMediaSize.setVisible(False)
    efcMemoryMediaSize.setDefaultValue(memMediaSizeKB)
    efcMemoryMediaSize.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    efcMemoryEraseEnable = efcComponent.createBooleanSymbol("ERASE_ENABLE", None)
    efcMemoryEraseEnable.setLabel("NVM Erase Enable")
    efcMemoryEraseEnable.setVisible(False)
    efcMemoryEraseEnable.setDefaultValue(True)
    efcMemoryEraseEnable.setReadOnly(True)

    efcMemoryEraseBufferSize = efcComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", efcMenu)
    efcMemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    efcMemoryEraseBufferSize.setVisible(False)
    efcMemoryEraseBufferSize.setDefaultValue(int(efcFlashEraseSize.getValue()))
    efcMemoryEraseBufferSize.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    efcMemoryEraseComment = efcComponent.createCommentSymbol("ERASE_COMMENT", efcMenu)
    efcMemoryEraseComment.setVisible(False)
    efcMemoryEraseComment.setLabel("*** Should be equal to Sector Erase Size ***")
    efcMemoryEraseComment.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    interruptVector = efcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = efcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = efcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = efcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    writeApiName = efcInstanceName.getValue() + "_PageWrite"
    eraseApiName = efcInstanceName.getValue() + "_SectorErase"

    efcWriteApiName = efcComponent.createStringSymbol("WRITE_API_NAME", efcMenu)
    efcWriteApiName.setVisible(False)
    efcWriteApiName.setReadOnly(True)
    efcWriteApiName.setDefaultValue(writeApiName)

    efcEraseApiName = efcComponent.createStringSymbol("ERASE_API_NAME", efcMenu)
    efcEraseApiName.setVisible(False)
    efcEraseApiName.setReadOnly(True)
    efcEraseApiName.setDefaultValue(eraseApiName)

    # NVIC Dynamic settings
    efcinterruptControl = efcComponent.createBooleanSymbol("NVIC_EFC_ENABLE", None)
    efcinterruptControl.setDependencies(interruptControl, ["INTERRUPT_ENABLE"])
    efcinterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")
    #Generate Output Header
    efcHeaderFile = efcComponent.createFileSymbol("EFC_FILE_0", None)
    efcHeaderFile.setSourcePath("../peripheral/efc_6450/templates/plib_efc.h.ftl")
    efcHeaderFile.setMarkup(True)
    efcHeaderFile.setOutputName("plib_" + efcInstanceName.getValue().lower() + ".h")
    efcHeaderFile.setOverwrite(True)
    efcHeaderFile.setDestPath("peripheral/efc/")
    efcHeaderFile.setProjectPath("config/" + configName + "/peripheral/efc/")
    efcHeaderFile.setType("HEADER")
    #Generate Output source
    efcSourceFile = efcComponent.createFileSymbol("EFC_FILE_1", None)
    efcSourceFile.setSourcePath("../peripheral/efc_6450/templates/plib_efc.c.ftl")
    efcSourceFile.setMarkup(True)
    efcSourceFile.setOutputName("plib_" + efcInstanceName.getValue().lower() + ".c")
    efcSourceFile.setOverwrite(True)
    efcSourceFile.setDestPath("peripheral/efc/")
    efcSourceFile.setProjectPath("config/" + configName + "/peripheral/efc/")
    efcSourceFile.setType("SOURCE")

    efcSystemDefFile = efcComponent.createFileSymbol("EFC_FILE_2", None)
    efcSystemDefFile.setType("STRING")
    efcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    efcSystemDefFile.setSourcePath("../peripheral/efc_6450/templates/system/definitions.h.ftl")
    efcSystemDefFile.setMarkup(True)


    efcSystemInitFile = efcComponent.createFileSymbol("EFC_FILE_3", None)
    efcSystemInitFile.setType("STRING")
    efcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    efcSystemInitFile.setSourcePath("../peripheral/efc_6450/templates/system/initialization.c.ftl")
    efcSystemInitFile.setMarkup(True)
def destroyComponent(efcComponent):

    global efcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    Database.setSymbolValue("core", interruptVector, False, 2)
    Database.setSymbolValue("core", interruptHandler, efcInstanceName.getValue() + "_Handler", 2)
    Database.setSymbolValue("core", interruptHandlerLock, False, 2)
