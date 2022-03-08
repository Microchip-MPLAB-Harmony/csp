"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

global sefcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock
global system_tacc_flash

def div_ceil(a, b):
    return (((a) + (b) - 1) / (b))

def waitStateUpdate(symbol, event):
    global system_tacc_flash

    if (event["value"] != ""):
        cpuClkFreq_MHz = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / 1000000
        waitState = div_ceil((system_tacc_flash * cpuClkFreq_MHz), 1000)
        symbol.setValue(waitState)

def sefcSetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def interruptControl(NVIC, event):
    global sefcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True)
        Database.setSymbolValue("core", interruptHandler, sefcInstanceName.getValue() + "_InterruptHandler")
        Database.setSymbolValue("core", interruptHandlerLock, True)
    else :
        Database.setSymbolValue("core", interruptVector, False)
        Database.setSymbolValue("core", interruptHandler, sefcInstanceName.getValue() + "_Handler")
        Database.setSymbolValue("core", interruptHandlerLock, False)

def instantiateComponent(sefcComponent):

    global sefcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global system_tacc_flash

    sefcInstanceName = sefcComponent.createStringSymbol("SEFC_INSTANCE_NAME", None)
    sefcInstanceName.setVisible(False)
    sefcInstanceName.setDefaultValue(sefcComponent.getID().upper())

    Log.writeInfoMessage("Running " + sefcInstanceName.getValue())

    #Create the top menu
    sefcMenu = sefcComponent.createMenuSymbol(None, None)
    sefcMenu.setLabel("Hardware Settings ")

    #SEFC memory segment name
    sefcMemSegName = sefcComponent.createStringSymbol("MEM_SEGMENT_NAME", None)
    sefcMemSegName.setVisible(False)
    sefcMemSegName.setReadOnly(True)
    sefcMemSegName.setDefaultValue("IFLASH" + sefcInstanceName.getValue().split("SEFC")[1])

    ##### Do not modify below symbol names as they are used by Memory Driver #####
    #Flash Details
    sefcFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"" + sefcMemSegName.getValue() + "\"]")
    if sefcFlashNode is not None:
        sefcFlashStartAddress = sefcComponent.createStringSymbol("FLASH_START_ADDRESS", sefcMenu)
        sefcFlashStartAddress.setVisible(False)
        sefcFlashStartAddress.setDefaultValue(sefcFlashNode.getAttribute("start"))

        #Flash size
        sefcFlashSize = sefcComponent.createStringSymbol("FLASH_SIZE", sefcMenu)
        sefcFlashSize.setVisible(False)
        sefcFlashSize.setDefaultValue(sefcFlashNode.getAttribute("size"))

        #Flash Page size
        sefcFlashProgramSize = sefcComponent.createStringSymbol("FLASH_PROGRAM_SIZE", sefcMenu)
        sefcFlashProgramSize.setVisible(False)
        sefcFlashProgramSize.setDefaultValue(sefcFlashNode.getAttribute("pagesize"))

    #Flash Erase size
    sefcFlashEraseSize = sefcComponent.createStringSymbol("FLASH_ERASE_SIZE", sefcMenu)
    sefcFlashEraseSize.setVisible(False)
    sefcFlashEraseSize.setDefaultValue("8192")

    #tACC(max) = 30 ns + 2 ns (Routing Flash + AHB), Read access time of Flash in ns
    system_tacc_flash = 32
    cpuClkFreq_MHz = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / 1000000
    waitState = div_ceil((system_tacc_flash * cpuClkFreq_MHz), 1000)

    # Flash Read Wait State (RWS).
    nvm_rws = sefcComponent.createIntegerSymbol("NVM_RWS", sefcMenu)
    nvm_rws.setLabel("Wait States")
    nvm_rws.setMin(0)
    nvm_rws.setMax(15)
    nvm_rws.setDefaultValue(waitState)
    nvm_rws.setDependencies(waitStateUpdate, ["core.CPU_CLOCK_FREQUENCY"])

    #Create a Checkbox to enable disable interrupts
    sefcInterrupt = sefcComponent.createBooleanSymbol("INTERRUPT_ENABLE", sefcMenu)
    sefcInterrupt.setLabel("Enable Interrupts")

    sefcMemoryDriver = sefcComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", sefcMenu)
    sefcMemoryDriver.setLabel("Memory Driver Connected")
    sefcMemoryDriver.setVisible(False)
    sefcMemoryDriver.setDefaultValue(False)

    offsetStart = (int(sefcFlashSize.getValue(),16) / 2)

    nvmOffset = str(hex(int(sefcFlashStartAddress.getValue(),16) + offsetStart))

    sefcMemoryStartAddr = sefcComponent.createStringSymbol("START_ADDRESS", sefcMenu)
    sefcMemoryStartAddr.setLabel("NVM Media Start Address")
    sefcMemoryStartAddr.setVisible(False)
    sefcMemoryStartAddr.setDefaultValue(nvmOffset[2:])
    sefcMemoryStartAddr.setDependencies(sefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    sefcMemoryMediaSize = sefcComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", sefcMenu)
    sefcMemoryMediaSize.setLabel("NVM Media Size (KB)")
    sefcMemoryMediaSize.setVisible(False)
    sefcMemoryMediaSize.setDefaultValue(memMediaSizeKB)
    sefcMemoryMediaSize.setDependencies(sefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    sefcMemoryEraseEnable = sefcComponent.createBooleanSymbol("ERASE_ENABLE", None)
    sefcMemoryEraseEnable.setLabel("NVM Erase Enable")
    sefcMemoryEraseEnable.setVisible(False)
    sefcMemoryEraseEnable.setDefaultValue(True)
    sefcMemoryEraseEnable.setReadOnly(True)

    sefcMemoryEraseBufferSize = sefcComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", sefcMenu)
    sefcMemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    sefcMemoryEraseBufferSize.setVisible(False)
    sefcMemoryEraseBufferSize.setDefaultValue(int(sefcFlashEraseSize.getValue()))
    sefcMemoryEraseBufferSize.setDependencies(sefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    sefcMemoryEraseComment = sefcComponent.createCommentSymbol("ERASE_COMMENT", sefcMenu)
    sefcMemoryEraseComment.setVisible(False)
    sefcMemoryEraseComment.setLabel("*** Should be equal to Sector Erase Size ***")
    sefcMemoryEraseComment.setDependencies(sefcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    interruptVector = sefcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = sefcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = sefcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = sefcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    writeApiName = sefcInstanceName.getValue() + "_PageWrite"
    eraseApiName = sefcInstanceName.getValue() + "_SectorErase"

    sefcWriteApiName = sefcComponent.createStringSymbol("WRITE_API_NAME", sefcMenu)
    sefcWriteApiName.setVisible(False)
    sefcWriteApiName.setReadOnly(True)
    sefcWriteApiName.setDefaultValue(writeApiName)

    sefcEraseApiName = sefcComponent.createStringSymbol("ERASE_API_NAME", sefcMenu)
    sefcEraseApiName.setVisible(False)
    sefcEraseApiName.setReadOnly(True)
    sefcEraseApiName.setDefaultValue(eraseApiName)

    # NVIC Dynamic settings
    sefcinterruptControl = sefcComponent.createBooleanSymbol("NVIC_SEFC_ENABLE", None)
    sefcinterruptControl.setDependencies(interruptControl, ["INTERRUPT_ENABLE"])
    sefcinterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    #Generate Output Header
    sefcHeaderFile = sefcComponent.createFileSymbol("SEFC_FILE_H", None)
    sefcHeaderFile.setSourcePath("../peripheral/sefc_04463/templates/plib_sefc.h.ftl")
    sefcHeaderFile.setMarkup(True)
    sefcHeaderFile.setOutputName("plib_" + sefcInstanceName.getValue().lower() + ".h")
    sefcHeaderFile.setOverwrite(True)
    sefcHeaderFile.setDestPath("peripheral/sefc/")
    sefcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sefc/")
    sefcHeaderFile.setType("HEADER")

    #Generate Output common Header
    sefcCommonHeaderFile = sefcComponent.createFileSymbol("SEFC_FILE_COMMON_H", None)
    sefcCommonHeaderFile.setSourcePath("../peripheral/sefc_04463/templates/plib_sefc_common.h")
    sefcCommonHeaderFile.setMarkup(False)
    sefcCommonHeaderFile.setOutputName("plib_sefc_common.h")
    sefcCommonHeaderFile.setOverwrite(True)
    sefcCommonHeaderFile.setDestPath("peripheral/sefc/")
    sefcCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sefc/")
    sefcCommonHeaderFile.setType("HEADER")

    #Generate Output source
    sefcSourceFile = sefcComponent.createFileSymbol("SEFC_FILE_C", None)
    sefcSourceFile.setSourcePath("../peripheral/sefc_04463/templates/plib_sefc.c.ftl")
    sefcSourceFile.setMarkup(True)
    sefcSourceFile.setOutputName("plib_" + sefcInstanceName.getValue().lower() + ".c")
    sefcSourceFile.setOverwrite(True)
    sefcSourceFile.setDestPath("peripheral/sefc/")
    sefcSourceFile.setProjectPath("config/" + configName + "/peripheral/sefc/")
    sefcSourceFile.setType("SOURCE")

    sefcSystemDefFile = sefcComponent.createFileSymbol("SEFC_FILE_DEF_H", None)
    sefcSystemDefFile.setType("STRING")
    sefcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sefcSystemDefFile.setSourcePath("../peripheral/sefc_04463/templates/system/definitions.h.ftl")
    sefcSystemDefFile.setMarkup(True)

    sefcSystemInitFile = sefcComponent.createFileSymbol("SEFC_FILE_INIT_C", None)
    sefcSystemInitFile.setType("STRING")
    sefcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    sefcSystemInitFile.setSourcePath("../peripheral/sefc_04463/templates/system/initialization.c.ftl")
    sefcSystemInitFile.setMarkup(True)

def destroyComponent(sefcComponent):

    global sefcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    Database.setSymbolValue("core", interruptVector, False)
    Database.setSymbolValue("core", interruptHandler, sefcInstanceName.getValue() + "_Handler")
    Database.setSymbolValue("core", interruptHandlerLock, False)
