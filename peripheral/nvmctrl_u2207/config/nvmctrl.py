###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(nvmctrlComponent):

    nvmctrlInstanceIndex = nvmctrlComponent.getID()[-1:]
    Log.writeInfoMessage("Running NVMCTRL" + str(nvmctrlInstanceIndex))

    #main menu
    nvmctrlSym_Menu = nvmctrlComponent.createMenuSymbol("NVMCTRL_MENU", None)
    nvmctrlSym_Menu.setLabel("Hardware Settings ")

    #Flash Address
    nvmctrlFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FLASH\"]")
    if nvmctrlFlashNode != None:
        nvmctrlSym_FLASH_ADDRESS = nvmctrlComponent.createStringSymbol("NVMCTRL_FLASH_ADDRESS", nvmctrlSym_Menu)
        nvmctrlSym_FLASH_ADDRESS.setVisible(False)
        nvmctrlSym_FLASH_ADDRESS.setDefaultValue(str(hex(int(nvmctrlFlashNode.getAttribute("start"),16))))

        #Flash size
        nvmctrlSym_FLASH_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_FLASH_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_FLASH_SIZE.setVisible(False)
        nvmctrlSym_FLASH_SIZE.setDefaultValue(str(hex(int(nvmctrlFlashNode.getAttribute("size"),16))))

        #Flash Page size
        nvmctrlSym_RWW_PAGE_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_PAGE_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWW_PAGE_SIZE.setVisible(False)
        nvmctrlSym_RWW_PAGE_SIZE.setDefaultValue(str(hex(int(nvmctrlFlashNode.getAttribute("pagesize")))))

        #Flash Row size
        nvmctrlSym_ROW_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_ROW_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_ROW_SIZE.setVisible(False)
        nvmctrlSym_ROW_SIZE.setDefaultValue(str(hex(int(nvmctrlFlashNode.getAttribute("rowsize")))))

    #RWWEEPROM Address
    nvmctrlRWWEEPROMNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"RWW\"]")
    if nvmctrlRWWEEPROMNode != None:
        nvmctrlSym_RWWEEPROM_ADDRESS = nvmctrlComponent.createStringSymbol("NVMCTRL_RWWEEPROM_ADDRESS", nvmctrlSym_Menu)
        nvmctrlSym_RWWEEPROM_ADDRESS.setVisible(False)
        nvmctrlSym_RWWEEPROM_ADDRESS.setDefaultValue(str(hex(int(nvmctrlRWWEEPROMNode.getAttribute("start"),16))))

        #RWWEEPROM size
        nvmctrlSym_RWWEEPROM_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_RWWEEPROM_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWWEEPROM_SIZE.setVisible(False)
        nvmctrlSym_RWWEEPROM_SIZE.setDefaultValue(str(hex(int(nvmctrlRWWEEPROMNode.getAttribute("size"),16))))

        #RWWEEPROM Page size
        nvmctrlSym_RWW_PAGE_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_RWWEEPROM_PAGE_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_RWW_PAGE_SIZE.setVisible(False)
        nvmctrlSym_RWW_PAGE_SIZE.setDefaultValue(str(hex(int(nvmctrlRWWEEPROMNode.getAttribute("pagesize")))))

        #RWWEEPROM Row size
        nvmctrlSym_ROW_SIZE = nvmctrlComponent.createStringSymbol("NVMCTRL_RWWEEPROM_ROW_SIZE", nvmctrlSym_Menu)
        nvmctrlSym_ROW_SIZE.setVisible(False)
        nvmctrlSym_ROW_SIZE.setDefaultValue(str(hex(int(nvmctrlRWWEEPROMNode.getAttribute("rowsize")))))


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
    nvmctrlSym_Interrupt.setLabel("Enable Interrupt?")
    nvmctrlSym_Interrupt.setDefaultValue(False)

    #index
    nvmctrlSym_Index = nvmctrlComponent.createIntegerSymbol("NVMCTRL_INDEX", nvmctrlSym_Menu)
    nvmctrlSym_Index.setVisible(False)
    nvmctrlSym_Index.setDefaultValue(int(nvmctrlInstanceIndex))

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmctrlModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]")
    nvmctrlModuleID = nvmctrlModuleNode.getAttribute("id")

    nvmctrlSym_HeaderFile = nvmctrlComponent.createFileSymbol("NVMCTRL_HEADER", None)
    nvmctrlSym_HeaderFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/plib_nvmctrl.h.ftl")
    nvmctrlSym_HeaderFile.setOutputName("plib_nvmctrl"+str(nvmctrlInstanceIndex)+".h")
    nvmctrlSym_HeaderFile.setDestPath("peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setType("HEADER")
    nvmctrlSym_HeaderFile.setMarkup(True)

    nvmctrlSym_SourceFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SOURCE", None)
    nvmctrlSym_SourceFile.setSourcePath("../peripheral/nvmctrl_"+nvmctrlModuleID+"/templates/plib_nvmctrl.c.ftl")
    nvmctrlSym_SourceFile.setOutputName("plib_nvmctrl"+str(nvmctrlInstanceIndex)+".c")
    nvmctrlSym_SourceFile.setDestPath("peripheral/nvmctrl/")
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




