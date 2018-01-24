###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pmComponent):

	pmInstanceIndex = pmComponent.getID()[-1:]

	#index
	pmSym_Index = pmComponent.createIntegerSymbol("PM_INDEX", None)
	pmSym_Index.setDefaultValue(int(pmInstanceIndex))
	pmSym_Index.setVisible(False)

	#standby back biasing
	pmSym_STDBYCFG_BBIASHS = pmComponent.createBooleanSymbol("PM_STDBYCFG_BBIASHS", None)
	pmSym_STDBYCFG_BBIASHS.setLabel("Enable RAM DMA Access in Standby Sleep Mode ?")
	pmSym_STDBYCFG_BBIASHS.setDescription("Configures DMA Access in low power modes")

	#standby VREGMOD configuration
	pmSym_STDBYCFG_VREGSMOD = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_VREGSMOD", None)
	pmSym_STDBYCFG_VREGSMOD.setLabel("VDDCORE Voltage Source Selection in Standby Sleep mode")
	pmSym_STDBYCFG_VREGSMOD.setDescription("Configures the VDDCORE Supply source in Standby Sleep mode.")

	pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__VREGSMOD\"]")
	pmStandbyConfigurationValues = []
	pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

	pmStandbyConfigurationDefaultValue = 0

	for index in range(len(pmStandbyConfigurationValues)):
		pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")

		if (pmStandbyConfigurationKeyName == "AUTO"):
			pmStandbyConfigurationDefaultValue = index

		pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
		pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
		pmSym_STDBYCFG_VREGSMOD.addKey(pmStandbyConfigurationKeyName , pmStandbyConfigurationKeyValue , pmStandbyConfigurationKeyDescription)

	pmSym_STDBYCFG_VREGSMOD.setDefaultValue(pmStandbyConfigurationDefaultValue)
	pmSym_STDBYCFG_VREGSMOD.setOutputMode("Key")
	pmSym_STDBYCFG_VREGSMOD.setDisplayMode("Description")

	###################################################################################################
	####################################### Code Generation  ##########################################
	###################################################################################################

	configName = Variables.get("__CONFIGURATION_NAME")

	pmModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]")
	pmModuleID = pmModuleNode.getAttribute("id")

	pmSym_HeaderFile = pmComponent.createFileSymbol("PM_HEADER", None)
	pmSym_HeaderFile.setSourcePath("../peripheral/pm_"+pmModuleID+"/templates/plib_pm.h.ftl")
	pmSym_HeaderFile.setOutputName("plib_pm" + pmInstanceIndex + ".h")
	pmSym_HeaderFile.setDestPath("peripheral/pm/")
	pmSym_HeaderFile.setProjectPath("config/" + configName + "peripheral/pm/")
	pmSym_HeaderFile.setType("HEADER")
	pmSym_HeaderFile.setMarkup(True)

	pmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE", None)
	pmSym_SourceFile.setSourcePath("../peripheral/pm_"+pmModuleID+"/templates/plib_pm.c.ftl")
	pmSym_SourceFile.setOutputName("plib_pm" + pmInstanceIndex + ".c")
	pmSym_SourceFile.setDestPath("peripheral/pm/")
	pmSym_SourceFile.setProjectPath("config/" + configName + "peripheral/pm/")
	pmSym_SourceFile.setType("SOURCE")
	pmSym_SourceFile.setMarkup(True)

	pmSym_SystemInitFile = pmComponent.createFileSymbol("PM_SYS_INIT", None)
	pmSym_SystemInitFile.setType("STRING")
	pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	pmSym_SystemInitFile.setSourcePath("../peripheral/pm_"+pmModuleID+"/templates/system/initialization.c.ftl")
	pmSym_SystemInitFile.setMarkup(True)

	pmSymSystemDefFile = pmComponent.createFileSymbol("PM_SYS_DEF", None)
	pmSymSystemDefFile.setType("STRING")
	pmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	pmSymSystemDefFile.setSourcePath("../peripheral/pm_"+pmModuleID+"/templates/system/definitions.h.ftl")
	pmSymSystemDefFile.setMarkup(True)