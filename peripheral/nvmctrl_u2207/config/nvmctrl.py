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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global nvmctrlInstanceName
global nvmctrlSym_Interrupt
global waitStates
###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def getSelectedEEPSize(eep_size_sym):
    selectedKeyIndex = 0
    coreComponent = Database.getComponentByID("core")
    eepromSizeSym = coreComponent.getSymbolByID(eep_size_sym)
    selectedKey = eepromSizeSym.getSelectedKey()

    for index in range(eepromSizeSym.getKeyCount()):
        if eepromSizeSym.getKey(index) == selectedKey:
            selectedKeyIndex = index
            break

    return int(eepromSizeSym.getKeyDescription(selectedKeyIndex).split()[0])

def updateEmuEEPROMStartAddr(symbol, event):
    localComponent = symbol.getComponent()

    nvmctrlFlashStartAddr = int(localComponent.getSymbolValue("FLASH_START_ADDRESS"), 16)
    nvmctrlFlashSize = int(localComponent.getSymbolValue("FLASH_SIZE"), 16)
    eep_emu_EEPROMSize = getSelectedEEPSize("DEVICE_NVMCTRL_EEPROM_SIZE")

    localComponent.setSymbolValue("NVMCTRL_EMU_EEPROM_SIZE", str(eep_emu_EEPROMSize))
    symbol.setValue(str(hex(nvmctrlFlashStartAddr + nvmctrlFlashSize - eep_emu_EEPROMSize)))

def updateNVMCTRLInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, nvmctrlInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "NVMCTRL_Handler", 2)


def updateNVMCTRLInterruptWarringStatus(symbol, event):

    if nvmctrlSym_Interrupt.getValue() == True:
        symbol.setVisible(event["value"])


def nvmctlrSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])


def waitStateUpdate(symbol, event):
    global waitStates
    cpuFreq = event["value"]
    for key in sorted(waitStates.keys()):
        if int(cpuFreq) <= int(key):
            symbol.setValue(waitStates.get(key), 2)
            break
###################################################################################################
########################################## Component  #############################################
###################################################################################################


def instantiateComponent(nvmctrlComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global nvmctrlInstanceName
    global nvmctrlSym_Interrupt

    global waitStates
    waitStates = {}
    waitStates = Database.sendMessage("core", "WAIT_STATES", waitStates)

    nvmctrlInstanceName = nvmctrlComponent.createStringSymbol("NVMCTRL_INSTANCE_NAME", None)
    nvmctrlInstanceName.setVisible(False)
    nvmctrlInstanceName.setDefaultValue(nvmctrlComponent.getID().upper())
    Log.writeInfoMessage("Running " + nvmctrlInstanceName.getValue())

    # Flash Address
    nvmctrlFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FLASH\"]")
    if nvmctrlFlashNode != None:
        nvmctrlSym_FLASH_ADDRESS = nvmctrlComponent.createStringSymbol("FLASH_START_ADDRESS", None)
        nvmctrlSym_FLASH_ADDRESS.setVisible(False)
        nvmctrlSym_FLASH_ADDRESS.setDefaultValue(nvmctrlFlashNode.getAttribute("start"))

        # Flash size
        nvmctrlSym_FLASH_SIZE = nvmctrlComponent.createStringSymbol("FLASH_SIZE", None)
        nvmctrlSym_FLASH_SIZE.setVisible(False)
        nvmctrlSym_FLASH_SIZE.setDefaultValue(nvmctrlFlashNode.getAttribute("size"))

        # Flash Page size
        nvmctrlSym_FLASH_PROGRAM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_PROGRAM_SIZE", None)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setDefaultValue(nvmctrlFlashNode.getAttribute("pagesize"))

    # RWWEEPROM Address
    nvmctrlRWWEEPROMNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"RWW\"]")
    if nvmctrlRWWEEPROMNode != None:
        nvmctrlSym_RWWEEPROM_START_ADDRESS = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_START_ADDRESS", None)
        nvmctrlSym_RWWEEPROM_START_ADDRESS.setVisible(False)
        nvmctrlSym_RWWEEPROM_START_ADDRESS.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("start"))

        # RWWEEPROM size
        nvmctrlSym_RWWEEPROM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_SIZE", None)
        nvmctrlSym_RWWEEPROM_SIZE.setVisible(False)
        nvmctrlSym_RWWEEPROM_SIZE.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("size"))

        # RWWEEPROM Page size
        nvmctrlSym_RWW_PROGRAM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_PROGRAM_SIZE", None)
        nvmctrlSym_RWW_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_RWW_PROGRAM_SIZE.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("pagesize"))

    nvmctrlParamNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVMCTRL\"]/instance@[name=\""+nvmctrlInstanceName.getValue()+"\"]/parameters")
    rowSize = "256"
    eeRowSize = "0"
    if nvmctrlParamNode != None:
        param_values = []
        param_values = nvmctrlParamNode.getChildren()
        for index in range(0, len(param_values)):
            if "ROW_SIZE" in param_values[index].getAttribute("name"):
                rowSize = param_values[index].getAttribute("value")

            if "RWWEE_ROW_SIZE" in param_values[index].getAttribute("name"):
                eeRowSize = param_values[index].getAttribute("value")

        # Flash Row size
        nvmctrlSym_ERASE_SIZE = nvmctrlComponent.createStringSymbol("FLASH_ERASE_SIZE", None)
        nvmctrlSym_ERASE_SIZE.setVisible(False)
        nvmctrlSym_ERASE_SIZE.setDefaultValue(rowSize)

        # RWWEEPROM Row size
        nvmctrlSym_RWW_ERASE_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_ERASE_SIZE", None)
        nvmctrlSym_RWW_ERASE_SIZE.setVisible(False)
        nvmctrlSym_RWW_ERASE_SIZE.setDefaultValue(eeRowSize)

    # NVM USER row Address
    nvmctrlUSERPAGENode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"USER_PAGE\"]")
    if nvmctrlUSERPAGENode != None:
        nvmctrlSym_USERROW_START_ADDRESS = nvmctrlComponent.createStringSymbol("FLASH_USERROW_START_ADDRESS", None)
        nvmctrlSym_USERROW_START_ADDRESS.setVisible(False)
        nvmctrlSym_USERROW_START_ADDRESS.setDefaultValue(nvmctrlUSERPAGENode.getAttribute("start"))

        # NVM user row size
        nvmctrlSym_USERROW_SIZE = nvmctrlComponent.createStringSymbol("FLASH_USERROW_SIZE", None)
        nvmctrlSym_USERROW_SIZE.setVisible(False)
        nvmctrlSym_USERROW_SIZE.setDefaultValue(nvmctrlUSERPAGENode.getAttribute("size"))

        # NVM user row Page size
        nvmctrlSym_USERROW_PROGRAM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_USERROW_PROGRAM_SIZE", None)
        nvmctrlSym_USERROW_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_USERROW_PROGRAM_SIZE.setDefaultValue(nvmctrlUSERPAGENode.getAttribute("pagesize"))

    # Configures NVM read mode
    nvmctrlSym_CTRLB_READMODE = nvmctrlComponent.createKeyValueSetSymbol("NVMCTRL_CTRLB_READMODE_SELECTION", None)
    nvmctrlSym_CTRLB_READMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_CTRLB_READMODE.setLabel("NVMCTRL Read Mode")

    nvmctrlReadModeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]/value-group@[name=\"NVMCTRL_CTRLB__READMODE\"]")
    nvmctrlReadModeValues = []
    nvmctrlReadModeValues = nvmctrlReadModeNode.getChildren()

    waitState = 6
    cpuClkFreq = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")

    if cpuClkFreq != None:
        for key in sorted(waitStates.keys()):
            if int(cpuClkFreq) <= int(key):
                waitState = waitStates.get(key)
                break

    # Flash Read Wait State (RWS).
    nvm_rws = nvmctrlComponent.createIntegerSymbol("NVM_RWS", None)
    nvm_rws.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvm_rws.setLabel("Wait States")
    nvm_rws.setDefaultValue(waitState)
    nvm_rws.setDependencies(waitStateUpdate, ["core.CPU_CLOCK_FREQUENCY"])

    nvmctrlReadModeDefaultValue = 0
    nvmctrlReadModeKeyDescription = ""

    for index in range(0, len(nvmctrlReadModeValues)):
        nvmctrlReadModeKeyName = nvmctrlReadModeValues[index].getAttribute("name")

        if (nvmctrlReadModeKeyName == "NO_MISS_PENALTY"):
            nvmctrlReadModeDefaultValue = index
            nvmctrlReadModeKeyDescription = "NO MISS PENALTY"
        elif (nvmctrlReadModeKeyName == "LOW_POWER"):
            nvmctrlReadModeKeyDescription = "LOW POWER"
        elif (nvmctrlReadModeKeyName == "DETERMINISTIC"):
            nvmctrlReadModeKeyDescription = "DETERMINISTIC"

        nvmctrlReadModeKeyValue = nvmctrlReadModeValues[index].getAttribute("value")
        nvmctrlSym_CTRLB_READMODE.addKey(nvmctrlReadModeKeyName, nvmctrlReadModeKeyValue, nvmctrlReadModeKeyDescription)

    nvmctrlSym_CTRLB_READMODE.setDefaultValue(nvmctrlReadModeDefaultValue)
    nvmctrlSym_CTRLB_READMODE.setOutputMode("Key")
    nvmctrlSym_CTRLB_READMODE.setDisplayMode("Description")

    # Configures NVM power reduction mode
    nvmctrlSym_CTRLB_SLEEPPRM = nvmctrlComponent.createKeyValueSetSymbol("NVMCTRL_CTRLB_POWER_REDUCTION_MODE", None)
    nvmctrlSym_CTRLB_SLEEPPRM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_CTRLB_SLEEPPRM.setLabel("Power Reduction Mode During Sleep")

    nvmctrlSleepPrmNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]/value-group@[name=\"NVMCTRL_CTRLB__SLEEPPRM\"]")
    nvmctrlSleepPrmValues = []
    nvmctrlSleepPrmValues = nvmctrlSleepPrmNode.getChildren()

    nvmctrlSleepPrmDefaultValue = 0
    nvmctrlSleepPrmKeyDescription = ""

    for index in range(0, len(nvmctrlSleepPrmValues)):
        nvmctrlSleepPrmKeyName = nvmctrlSleepPrmValues[index].getAttribute("name")

        if (nvmctrlSleepPrmKeyName == "WAKEONACCESS"):
            nvmctrlSleepPrmDefaultValue = index
            nvmctrlSleepPrmKeyDescription = "WAKEUP ON ACCESS"
        elif (nvmctrlSleepPrmKeyName == "WAKEUPINSTANT"):
            nvmctrlSleepPrmKeyDescription = "WAKEUP INSTANT"
        elif (nvmctrlSleepPrmKeyName == "DISABLED"):
            nvmctrlSleepPrmKeyDescription = "DISABLED"

        nvmctrlSleepPrmKeyValue = nvmctrlSleepPrmValues[index].getAttribute("value")
        nvmctrlSym_CTRLB_SLEEPPRM.addKey(nvmctrlSleepPrmKeyName, nvmctrlSleepPrmKeyValue, nvmctrlSleepPrmKeyDescription)

    nvmctrlSym_CTRLB_SLEEPPRM.setDefaultValue(nvmctrlSleepPrmDefaultValue)
    nvmctrlSym_CTRLB_SLEEPPRM.setOutputMode("Key")
    nvmctrlSym_CTRLB_SLEEPPRM.setDisplayMode("Description")

    # Configures Manual Write operation
    nvmctrlSym_CTRLB_WRITEPOLICY = nvmctrlComponent.createComboSymbol("NVMCTRL_WRITE_POLICY", None, ["MANUAL", "AUTOMATIC"])
    nvmctrlSym_CTRLB_WRITEPOLICY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_CTRLB_WRITEPOLICY.setLabel("Write Policy")
    nvmctrlSym_CTRLB_WRITEPOLICY.setDefaultValue("MANUAL")

    # Configures cache operation
    nvmctrlSym_CTRLB_CACHEENABLE = nvmctrlComponent.createBooleanSymbol("NVMCTRL_CACHE_ENABLE", None)
    nvmctrlSym_CTRLB_CACHEENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_CTRLB_CACHEENABLE.setLabel("Enable Instruction Cache?")
    nvmctrlSym_CTRLB_CACHEENABLE.setDefaultValue(True)

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    # Configures the library for interrupt mode operations
    nvmctrlSym_Interrupt = nvmctrlComponent.createBooleanSymbol("INTERRUPT_ENABLE", None)
    nvmctrlSym_Interrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:INTENSET")
    nvmctrlSym_Interrupt.setLabel("Enable Interrupt?")
    nvmctrlSym_Interrupt.setDefaultValue(False)

    # Configuration when interfaced with memory driver
    nvmctrlSym_MemoryDriver = nvmctrlComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    nvmctrlSym_MemoryDriver.setLabel("Memory Driver Connected")
    nvmctrlSym_MemoryDriver.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:%NOREGISTER%")
    nvmctrlSym_MemoryDriver.setVisible(False)
    nvmctrlSym_MemoryDriver.setDefaultValue(False)

    offsetStart = (int(nvmctrlSym_FLASH_SIZE.getValue(), 16) / 2)

    nvmOffset = str(hex(int(nvmctrlSym_FLASH_ADDRESS.getValue(), 16) + offsetStart))

    nvmctrlSym_MemoryStartAddr = nvmctrlComponent.createStringSymbol("START_ADDRESS", None)
    nvmctrlSym_MemoryStartAddr.setLabel("NVM Media Start Address")
    nvmctrlSym_MemoryStartAddr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:ADDR")
    nvmctrlSym_MemoryStartAddr.setVisible(False)
    nvmctrlSym_MemoryStartAddr.setDefaultValue(nvmOffset[2:])
    nvmctrlSym_MemoryStartAddr.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    nvmctrlSym_MemoryMediaSize = nvmctrlComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", None)
    nvmctrlSym_MemoryMediaSize.setLabel("NVM Media Size (KB)")
    nvmctrlSym_MemoryMediaSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_MemoryMediaSize.setVisible(False)
    nvmctrlSym_MemoryMediaSize.setDefaultValue(memMediaSizeKB)
    nvmctrlSym_MemoryMediaSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    nvmctrlSym_MemoryEraseEnable = nvmctrlComponent.createBooleanSymbol("ERASE_ENABLE", None)
    nvmctrlSym_MemoryEraseEnable.setLabel("NVM Erase Enable")
    nvmctrlSym_MemoryEraseEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:CTRLB")
    nvmctrlSym_MemoryEraseEnable.setVisible(False)
    nvmctrlSym_MemoryEraseEnable.setDefaultValue(True)
    nvmctrlSym_MemoryEraseEnable.setReadOnly(True)

    nvmctrlSym_MemoryEraseBufferSize = nvmctrlComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", None)
    nvmctrlSym_MemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    nvmctrlSym_MemoryEraseBufferSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvmctrl_u2207;register:%NOREGISTER%")
    nvmctrlSym_MemoryEraseBufferSize.setVisible(False)
    nvmctrlSym_MemoryEraseBufferSize.setDefaultValue(int(nvmctrlSym_ERASE_SIZE.getValue()))
    nvmctrlSym_MemoryEraseBufferSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    nvmctrlSym_MemoryEraseComment = nvmctrlComponent.createCommentSymbol("ERASE_COMMENT", None)
    nvmctrlSym_MemoryEraseComment.setVisible(False)
    nvmctrlSym_MemoryEraseComment.setLabel("*** Should be equal to Row Erase Size ***")
    nvmctrlSym_MemoryEraseComment.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    writeApiName = nvmctrlComponent.getID().upper() + "_PageWrite"
    eraseApiName = nvmctrlComponent.getID().upper() + "_RowErase"
    userRowEraseApiName = nvmctrlComponent.getID().upper() + "_USER_ROW_RowErase"
    userRowWriteApiName = nvmctrlComponent.getID().upper() + "_USER_ROW_PageWrite"
    unlockApiName = nvmctrlComponent.getID().upper() + "_RegionUnlock"

    nvmctrlWriteApiName = nvmctrlComponent.createStringSymbol("WRITE_API_NAME", None)
    nvmctrlWriteApiName.setVisible(False)
    nvmctrlWriteApiName.setReadOnly(True)
    nvmctrlWriteApiName.setDefaultValue(writeApiName)

    nvmctrlEraseApiName = nvmctrlComponent.createStringSymbol("ERASE_API_NAME", None)
    nvmctrlEraseApiName.setVisible(False)
    nvmctrlEraseApiName.setReadOnly(True)
    nvmctrlEraseApiName.setDefaultValue(eraseApiName)

    nvmctrlUserRowEraseApiName = nvmctrlComponent.createStringSymbol("USER_ROW_ERASE_API_NAME", None)
    nvmctrlUserRowEraseApiName.setVisible(False)
    nvmctrlUserRowEraseApiName.setReadOnly(True)
    nvmctrlUserRowEraseApiName.setDefaultValue(userRowEraseApiName)

    nvmctrlUserRowWriteApiName = nvmctrlComponent.createStringSymbol("USER_ROW_WRITE_API_NAME", None)
    nvmctrlUserRowWriteApiName.setVisible(False)
    nvmctrlUserRowWriteApiName.setReadOnly(True)
    nvmctrlUserRowWriteApiName.setDefaultValue(userRowWriteApiName)

    nvmctrlUnlockApiName = nvmctrlComponent.createStringSymbol("UNLOCK_API_NAME", None)
    nvmctrlUnlockApiName.setVisible(False)
    nvmctrlUnlockApiName.setReadOnly(True)
    nvmctrlUnlockApiName.setDefaultValue(unlockApiName)

    eep_size_sym =  Database.getComponentByID("core").getSymbolValue("DEVICE_NVMCTRL_EEPROM_SIZE")

    if eep_size_sym != None:
        eep_emu_EEPROMSize = getSelectedEEPSize("DEVICE_NVMCTRL_EEPROM_SIZE")

        nvmctrlEmuEEPROMSize = nvmctrlComponent.createStringSymbol("NVMCTRL_EMU_EEPROM_SIZE", None)
        nvmctrlEmuEEPROMSize.setDefaultValue(str(eep_emu_EEPROMSize))
        nvmctrlEmuEEPROMSize.setVisible(False)

        nvmctrlFlashStartAddr = int(nvmctrlSym_FLASH_ADDRESS.getValue(), 16)
        nvmctrlFlashSize = int(nvmctrlSym_FLASH_SIZE.getValue(), 16)

        nvmctrlEmuEEPROMStartAddr = nvmctrlComponent.createStringSymbol("NVMCTRL_EMU_EEPROM_START_ADDR", None)
        nvmctrlEmuEEPROMStartAddr.setVisible(False)
        nvmctrlEmuEEPROMStartAddr.setDefaultValue(str(hex(nvmctrlFlashStartAddr + nvmctrlFlashSize - eep_emu_EEPROMSize)))
        nvmctrlEmuEEPROMStartAddr.setDependencies(updateEmuEEPROMStartAddr, ["core.DEVICE_NVMCTRL_EEPROM_SIZE"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = nvmctrlInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = nvmctrlInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = nvmctrlInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = nvmctrlInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    nvmctrlSym_UpdateInterruptStatus = nvmctrlComponent.createBooleanSymbol("NVMCTRL_INTERRUPT_STATUS", None)
    nvmctrlSym_UpdateInterruptStatus.setDependencies(updateNVMCTRLInterruptStatus, ["INTERRUPT_ENABLE"])
    nvmctrlSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    nvmctrlSym_IntEnComment = nvmctrlComponent.createCommentSymbol("NVMCTRL_INTERRUPT_ENABLE_COMMENT", None)
    nvmctrlSym_IntEnComment.setVisible(False)
    nvmctrlSym_IntEnComment.setLabel("Warning!!! NVMCTRL Interrupt is Disabled in Interrupt Manager")
    nvmctrlSym_IntEnComment.setDependencies(updateNVMCTRLInterruptWarringStatus, ["core." + InterruptVectorUpdate])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmctrlModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]")
    nvmctrlModuleID = nvmctrlModuleNode.getAttribute("id")

    nvmctrlSym_HeaderFile = nvmctrlComponent.createFileSymbol("NVMCTRL_HEADER", None)
    nvmctrlSym_HeaderFile.setSourcePath("../peripheral/nvmctrl_u2207/templates/plib_nvmctrl.h.ftl")
    nvmctrlSym_HeaderFile.setOutputName("plib_"+nvmctrlInstanceName.getValue().lower()+".h")
    nvmctrlSym_HeaderFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setType("HEADER")
    nvmctrlSym_HeaderFile.setMarkup(True)

    nvmctrlSym_SourceFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SOURCE", None)
    nvmctrlSym_SourceFile.setSourcePath("../peripheral/nvmctrl_u2207/templates/plib_nvmctrl.c.ftl")
    nvmctrlSym_SourceFile.setOutputName("plib_"+nvmctrlInstanceName.getValue().lower()+".c")
    nvmctrlSym_SourceFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setType("SOURCE")
    nvmctrlSym_SourceFile.setMarkup(True)

    nvmctrlSym_SystemInitFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_INIT_0", None)
    nvmctrlSym_SystemInitFile.setSourcePath("../peripheral/nvmctrl_u2207/templates/system/nvm_waitstate.h.ftl")
    nvmctrlSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    nvmctrlSym_SystemInitFile.setType("STRING")
    nvmctrlSym_SystemInitFile.setMarkup(True)

    nvmctrlSym_SystemInitFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_INIT", None)
    nvmctrlSym_SystemInitFile.setSourcePath("../peripheral/nvmctrl_u2207/templates/system/initialization.c.ftl")
    nvmctrlSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    nvmctrlSym_SystemInitFile.setType("STRING")
    nvmctrlSym_SystemInitFile.setMarkup(True)

    nvmctrlSystemDefFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_DEF", None)
    nvmctrlSystemDefFile.setSourcePath("../peripheral/nvmctrl_u2207/templates/system/definitions.h.ftl")
    nvmctrlSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmctrlSystemDefFile.setType("STRING")
    nvmctrlSystemDefFile.setMarkup(True)
