global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global nvmctrlInstanceIndex
global nvmctrlSym_Interrupt

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateNVMCTRLInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, "NVMCTRL" + nvmctrlInstanceIndex + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "NVMCTRL_Handler", 2)

def updateNVMCTRLInterruptWarringStatus(symbol, event):

    if nvmctrlSym_Interrupt.getValue() == True:
        symbol.setVisible(event["value"])

def updateNVMCTRLClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def nvmctlrSetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def instantiateComponent(nvmctrlComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global nvmctrlInstanceIndex
    global nvmctrlSym_Interrupt

    nvmctrlInstanceIndex = nvmctrlComponent.getID()[-1:]
    Log.writeInfoMessage("Running NVMCTRL" + str(nvmctrlInstanceIndex))

    #main menu
    nvmctrlSym_Menu = nvmctrlComponent.createMenuSymbol("NVMCTRL_MENU", None)
    nvmctrlSym_Menu.setLabel("Hardware Settings ")

    #clock enable
    Database.clearSymbolValue("core", "NVMCTRL_CLOCK_ENABLE")
    Database.setSymbolValue("core", "NVMCTRL_CLOCK_ENABLE", True, 2)

    #Flash Address
    nvmctrlFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FLASH\"]")
    if nvmctrlFlashNode != None:
        nvmctrlSym_FLASH_ADDRESS = nvmctrlComponent.createStringSymbol("FLASH_START_ADDRESS", nvmctrlSym_Menu)
        nvmctrlSym_FLASH_ADDRESS.setVisible(False)
        nvmctrlSym_FLASH_ADDRESS.setDefaultValue(nvmctrlFlashNode.getAttribute("start"))

        #Flash size
        nvmctrlSym_FLASH_SIZE = nvmctrlComponent.createStringSymbol("FLASH_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_FLASH_SIZE.setVisible(False)
        nvmctrlSym_FLASH_SIZE.setDefaultValue(nvmctrlFlashNode.getAttribute("size"))

        #Flash Page size
        nvmctrlSym_FLASH_PROGRAM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_PROGRAM_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setDefaultValue(nvmctrlFlashNode.getAttribute("pagesize"))

    #RWWEEPROM Address
    nvmctrlRWWEEPROMNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"RWW\"]")
    if nvmctrlRWWEEPROMNode != None:
        nvmctrlSym_RWWEEPROM_START_ADDRESS = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_START_ADDRESS", nvmctrlSym_Menu)
        nvmctrlSym_RWWEEPROM_START_ADDRESS.setVisible(False)
        nvmctrlSym_RWWEEPROM_START_ADDRESS.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("start"))

        #RWWEEPROM size
        nvmctrlSym_RWWEEPROM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWWEEPROM_SIZE.setVisible(False)
        nvmctrlSym_RWWEEPROM_SIZE.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("size"))

        #RWWEEPROM Page size
        nvmctrlSym_RWW_PROGRAM_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_PROGRAM_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWW_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_RWW_PROGRAM_SIZE.setDefaultValue(nvmctrlRWWEEPROMNode.getAttribute("pagesize"))

    nvmctrlParamNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVMCTRL\"]/instance@[name=\"NVMCTRL\"]/parameters")
    if nvmctrlParamNode != None:
        param_values = []
        param_values = nvmctrlParamNode.getChildren()
        for index in range(0, len(param_values)):
            if "ROW_SIZE" in param_values[index].getAttribute("name"):
                rowSize = param_values[index].getAttribute("value")

            if "RWWEE_ROW_SIZE" in param_values[index].getAttribute("name"):
                eeRowSize = param_values[index].getAttribute("value")

        #Flash Row size
        nvmctrlSym_ERASE_SIZE = nvmctrlComponent.createStringSymbol("FLASH_ERASE_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_ERASE_SIZE.setVisible(False)
        nvmctrlSym_ERASE_SIZE.setDefaultValue(rowSize)

        #RWWEEPROM Row size
        nvmctrlSym_RWW_ERASE_SIZE = nvmctrlComponent.createStringSymbol("FLASH_RWWEEPROM_ERASE_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWW_ERASE_SIZE.setVisible(False)
        nvmctrlSym_RWW_ERASE_SIZE.setDefaultValue(eeRowSize)


    #EEPPROM API Generation Option
    nvmctrlMemSegNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"RWW\"]")

    nvmctrlSym_RWWEE = nvmctrlComponent.createBooleanSymbol("NVMCTRL_RWW_EEPROM", nvmctrlSym_Menu)
    nvmctrlSym_RWWEE.setVisible(False)

    if nvmctrlMemSegNode != None:
        nvmctrlMemSegName = str(nvmctrlMemSegNode.getAttribute("name"))

        nvmctrlSym_RWWEE.setLabel("Generate RWWEEPROM API?")
        nvmctrlSym_RWWEE.setVisible(True)
    else:
            nvmctrlSym_RWWEE.setDefaultValue(False)

    #Region Lock/Unlock API Generation Option
    nvmctrlSym_Region = nvmctrlComponent.createBooleanSymbol("NVMCTRL_REGION_LOCK_UNLOCK", nvmctrlSym_Menu)
    nvmctrlSym_Region.setLabel("Generate Region Lock/Unlock API?")

    #Configures NVM read mode
    nvmctrlSym_CTRLB_READMODE = nvmctrlComponent.createKeyValueSetSymbol("NVMCTRL_CTRLB_READMODE_SELECTION", nvmctrlSym_Menu)
    nvmctrlSym_CTRLB_READMODE.setLabel("NVMCTRL Read Mode")

    nvmctrlReadModeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]/value-group@[name=\"NVMCTRL_CTRLB__READMODE\"]")
    nvmctrlReadModeValues = []
    nvmctrlReadModeValues = nvmctrlReadModeNode.getChildren()

    nvmctrlReadModeDefaultValue = 0

    for index in range (0 , len(nvmctrlReadModeValues)):
        nvmctrlReadModeKeyName = nvmctrlReadModeValues[index].getAttribute("name")

        if (nvmctrlReadModeKeyName == "NO_MISS_PENALTY"):
            nvmctrlReadModeDefaultValue = index

        nvmctrlReadModeKeyDescription = nvmctrlReadModeValues[index].getAttribute("caption")
        nvmctrlReadModeKeyValue =  nvmctrlReadModeValues[index].getAttribute("value")
        nvmctrlSym_CTRLB_READMODE.addKey(nvmctrlReadModeKeyName , nvmctrlReadModeKeyValue , nvmctrlReadModeKeyDescription)

    nvmctrlSym_CTRLB_READMODE.setDefaultValue(nvmctrlReadModeDefaultValue)
    nvmctrlSym_CTRLB_READMODE.setOutputMode("Key")
    nvmctrlSym_CTRLB_READMODE.setDisplayMode("Description")

    #Configures NVM power reduction mode
    nvmctrlSym_CTRLB_SLEEPPRM = nvmctrlComponent.createKeyValueSetSymbol("NVMCTRL_CTRLB_POWER_REDUCTION_MODE", nvmctrlSym_Menu)
    nvmctrlSym_CTRLB_SLEEPPRM.setLabel("Power Reduction Mode During Sleep")

    nvmctrlSleepPrmNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]/value-group@[name=\"NVMCTRL_CTRLB__SLEEPPRM\"]")
    nvmctrlSleepPrmValues = []
    nvmctrlSleepPrmValues = nvmctrlSleepPrmNode.getChildren()

    nvmctrlSleepPrmDefaultValue = 0

    for index in range (0 , len(nvmctrlSleepPrmValues)):
        nvmctrlSleepPrmKeyName = nvmctrlSleepPrmValues[index].getAttribute("name")

        if (nvmctrlSleepPrmKeyName == "WAKEUPACCESS"):
            nvmctrlSleepPrmDefaultValue = index

        nvmctrlSleepPrmKeyDescription = nvmctrlSleepPrmValues[index].getAttribute("caption")
        nvmctrlSleepPrmKeyValue =  nvmctrlSleepPrmValues[index].getAttribute("value")
        nvmctrlSym_CTRLB_SLEEPPRM.addKey(nvmctrlSleepPrmKeyName , nvmctrlSleepPrmKeyValue , nvmctrlSleepPrmKeyDescription)

    nvmctrlSym_CTRLB_SLEEPPRM.setDefaultValue(nvmctrlSleepPrmDefaultValue)
    nvmctrlSym_CTRLB_SLEEPPRM.setOutputMode("Key")
    nvmctrlSym_CTRLB_SLEEPPRM.setDisplayMode("Description")

    #Configures cache operation
    nvmctrlSym_CTRLB_CACHEDIS = nvmctrlComponent.createBooleanSymbol("NVMCTRL_CACHE_ENABLE", nvmctrlSym_Menu)
    nvmctrlSym_CTRLB_CACHEDIS.setLabel("Enable Instruction Cache?")
    nvmctrlSym_CTRLB_CACHEDIS.setDefaultValue(True)

    #Configures the library for interrupt mode operations
    nvmctrlSym_Interrupt = nvmctrlComponent.createBooleanSymbol("NVMCTRL_INTERRUPT_MODE", nvmctrlSym_Menu)
    nvmctrlSym_Interrupt.setLabel("Enable Interrupt ?")
    nvmctrlSym_Interrupt.setDefaultValue(False)

    #Configuration when interfaced with memory driver
    nvmctrlSym_MemoryDriver = nvmctrlComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", nvmctrlSym_Menu)
    nvmctrlSym_MemoryDriver.setLabel("Memory Driver Connected")
    nvmctrlSym_MemoryDriver.setVisible(False)
    nvmctrlSym_MemoryDriver.setDefaultValue(False)

    nvmctrlSym_MemoryStartAddr = nvmctrlComponent.createHexSymbol("START_ADDRESS", nvmctrlSym_Menu)
    nvmctrlSym_MemoryStartAddr.setLabel("NVM Offset for File System")
    nvmctrlSym_MemoryStartAddr.setVisible(False)
    nvmctrlSym_MemoryStartAddr.setDefaultValue(0x20000)
    nvmctrlSym_MemoryStartAddr.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    nvmctrlSym_MemoryEraseEnable = nvmctrlComponent.createBooleanSymbol("ERASE_ENABLE", None)
    nvmctrlSym_MemoryEraseEnable.setLabel("NVM Erase Enable")
    nvmctrlSym_MemoryEraseEnable.setVisible(False)
    nvmctrlSym_MemoryEraseEnable.setDefaultValue(True)
    nvmctrlSym_MemoryEraseEnable.setReadOnly(True)

    nvmctrlSym_MemoryEraseBufferSize = nvmctrlComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", nvmctrlSym_Menu)
    nvmctrlSym_MemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    nvmctrlSym_MemoryEraseBufferSize.setVisible(False)
    nvmctrlSym_MemoryEraseBufferSize.setDefaultValue(256)
    nvmctrlSym_MemoryEraseBufferSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    nvmctrlSym_MemoryEraseComment = nvmctrlComponent.createCommentSymbol("ERASE_COMMENT", nvmctrlSym_Menu)
    nvmctrlSym_MemoryEraseComment.setVisible(False)
    nvmctrlSym_MemoryEraseComment.setLabel("*** Should be equal to Row Erase Size ***")
    nvmctrlSym_MemoryEraseComment.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    nvmctrlSym_MemoryMediaSize = nvmctrlComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", nvmctrlSym_Menu)
    nvmctrlSym_MemoryMediaSize.setLabel("NVM Memory Media Size")
    nvmctrlSym_MemoryMediaSize.setVisible(False)
    nvmctrlSym_MemoryMediaSize.setDefaultValue(1024)
    nvmctrlSym_MemoryMediaSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    #index
    nvmctrlSym_Index = nvmctrlComponent.createIntegerSymbol("NVMCTRL_INDEX", nvmctrlSym_Menu)
    nvmctrlSym_Index.setVisible(False)
    nvmctrlSym_Index.setDefaultValue(int(nvmctrlInstanceIndex))

    writeApiName = nvmctrlComponent.getID().upper() + "_PageWrite"
    eraseApiName = nvmctrlComponent.getID().upper() + "_RowErase"

    efcWriteApiName = nvmctrlComponent.createStringSymbol("WRITE_API_NAME", nvmctrlSym_Menu)
    efcWriteApiName.setVisible(False)
    efcWriteApiName.setReadOnly(True)
    efcWriteApiName.setDefaultValue(writeApiName)

    efcEraseApiName = nvmctrlComponent.createStringSymbol("ERASE_API_NAME", nvmctrlSym_Menu)
    efcEraseApiName.setVisible(False)
    efcEraseApiName.setReadOnly(True)
    efcEraseApiName.setDefaultValue(eraseApiName)

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = "NVMCTRL_INTERRUPT_ENABLE"
    InterruptHandler = "NVMCTRL_INTERRUPT_HANDLER"
    InterruptHandlerLock = "NVMCTRL_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = "NVMCTRL_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    nvmctrlSym_UpdateInterruptStatus = nvmctrlComponent.createBooleanSymbol("NVMCTRL_INTERRUPT_STATUS", None)
    nvmctrlSym_UpdateInterruptStatus.setDependencies(updateNVMCTRLInterruptStatus, ["NVMCTRL_INTERRUPT_MODE"])
    nvmctrlSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    nvmctrlSym_IntEnComment = nvmctrlComponent.createCommentSymbol("NVMCTRL_INTERRUPT_ENABLE_COMMENT", None)
    nvmctrlSym_IntEnComment.setVisible(False)
    nvmctrlSym_IntEnComment.setLabel("Warning!!! NVMCTRL Interrupt is Disabled in Interrupt Manager")
    nvmctrlSym_IntEnComment.setDependencies(updateNVMCTRLInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    nvmctrlSym_ClkEnComment = nvmctrlComponent.createCommentSymbol("NVMCTRL_CLOCK_ENABLE_COMMENT", None)
    nvmctrlSym_ClkEnComment.setLabel("Warning!!! NVMCTRL Peripheral Clock is Disabled in Clock Manager")
    nvmctrlSym_ClkEnComment.setVisible(False)
    nvmctrlSym_ClkEnComment.setDependencies(updateNVMCTRLClockWarringStatus, ["core.NVMCTRL_CLOCK_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmctrlModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]")
    nvmctrlModuleID = nvmctrlModuleNode.getAttribute("id")

    nvmctrlSym_HeaderFile = nvmctrlComponent.createFileSymbol("NVMCTRL_HEADER", None)
    nvmctrlSym_HeaderFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/plib_nvmctrl.h.ftl")
    nvmctrlSym_HeaderFile.setOutputName("plib_nvmctrl"+str(nvmctrlInstanceIndex)+".h")
    nvmctrlSym_HeaderFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setType("HEADER")
    nvmctrlSym_HeaderFile.setMarkup(True)

    nvmctrlSym_SourceFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SOURCE", None)
    nvmctrlSym_SourceFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/plib_nvmctrl.c.ftl")
    nvmctrlSym_SourceFile.setOutputName("plib_nvmctrl"+str(nvmctrlInstanceIndex)+".c")
    nvmctrlSym_SourceFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setType("SOURCE")
    nvmctrlSym_SourceFile.setMarkup(True)

    nvmctrlSym_SystemInitFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_INIT", None)
    nvmctrlSym_SystemInitFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/system/initialization.c.ftl")
    nvmctrlSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    nvmctrlSym_SystemInitFile.setType("STRING")
    nvmctrlSym_SystemInitFile.setMarkup(True)

    nvmctrlSystemDefFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_DEF", None)
    nvmctrlSystemDefFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/system/definitions.h.ftl")
    nvmctrlSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmctrlSystemDefFile.setType("STRING")
    nvmctrlSystemDefFile.setMarkup(True)
