def instantiateComponent(coreComponent):
	
	devMenu = coreComponent.createMenuSymbol("CoreDevMenu", None)
	devMenu.setLabel("Device & Project Configuration")

	devCfgMenu = coreComponent.createMenuSymbol("CoreCfgMenu", devMenu)
	devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
	devCfgMenu.setDescription("Hardware Configuration Bits")

	prjMenu = coreComponent.createMenuSymbol("CorePrjMenu", devMenu)
	prjMenu.setLabel("Project Configuration")
	prjMenu.setDescription("Project Specific Configuration")

	genAppFiles = coreComponent.createBooleanSymbol("CoreGenAppFiles", prjMenu)
	genAppFiles.setLabel("Generate Harmony Application Files?")

	configName = Variables.get("__CONFIGURATION_NAME")

	#generate main.c file
	mainSourceFile = coreComponent.createFileSymbol(None, None)
	mainSourceFile.setSourcePath("templates/main.c.ftl")
	mainSourceFile.setOutputName("main.c")
	mainSourceFile.setMarkup(True)
	mainSourceFile.setOverwrite(True)
	mainSourceFile.setDestPath("../../")
	mainSourceFile.setProjectPath("")
	mainSourceFile.setType("SOURCE")

	#generate system_init.c file
	initSourceFile = coreComponent.createFileSymbol(None, None)
	initSourceFile.setSourcePath("templates/system_init.c.ftl")
	initSourceFile.setOutputName("system_init.c")
	initSourceFile.setMarkup(True)
	initSourceFile.setOverwrite(True)
	initSourceFile.setDestPath("")
	initSourceFile.setProjectPath("config/" + configName + "/")
	initSourceFile.setType("SOURCE")
	systemInitFuseList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION", None)
	systemInitDrvList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA", None)
	systemInitModuleList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_MODULE_INITIALIZATION_DATA", None)
	systemInitLibList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA", None)
	systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION", None)
	systemInitDataList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DATA", None)
	systemInitCoreList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE", None)
	systemInitDriver1List = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS", None)
	systemInitDriver2List = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS", None)
	systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES", None)
	systemInitMWList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE", None)

	#generate system_config.h file
	confHeaderFile = coreComponent.createFileSymbol(None, None)
	confHeaderFile.setSourcePath("templates/system_config.h.ftl")
	confHeaderFile.setOutputName("system_config.h")
	confHeaderFile.setMarkup(True)
	confHeaderFile.setOverwrite(True)
	confHeaderFile.setDestPath("")
	confHeaderFile.setProjectPath("config/" + configName + "/")
	confHeaderFile.setType("HEADER")
	systemConfigIncludesList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES", None)
	systemConfigSysList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION", None)
	systemConfigDrvList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION", None)
	systemConfigMWList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION", None)
	systemConfigAppList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_APPLICATION_CONFIGURATION", None)

	#generate system_definitions.h file
	defHeaderFile = coreComponent.createFileSymbol(None, None)
	defHeaderFile.setSourcePath("templates/system_definitions.h.ftl")
	defHeaderFile.setOutputName("system_definitions.h")
	defHeaderFile.setMarkup(True)
	defHeaderFile.setOverwrite(True)
	defHeaderFile.setDestPath("")
	defHeaderFile.setProjectPath("config/" + configName + "/")
	defHeaderFile.setType("HEADER")
	systemDefinitionsHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_INCLUDES", None)
	systemDefinitionsObjList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_OBJECTS", None)
	systemDefinitionsExternsList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_EXTERNS", None)


	#generate system_interrupt.c file
	intSourceFile = coreComponent.createFileSymbol(None, None)
	intSourceFile.setSourcePath("templates/system_interrupt.c.ftl")
	intSourceFile.setOutputName("system_interrupt.c")
	intSourceFile.setMarkup(True)
	intSourceFile.setOverwrite(True)
	intSourceFile.setDestPath("")
	intSourceFile.setProjectPath("config/" + configName + "/")
	intSourceFile.setType("SOURCE")
	systemIntHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_INCLUDES", None)
	systemIntVectorsList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_VECTORS", None)

	#generate app.c file
	appSourceFile = coreComponent.createFileSymbol(None, None)
	appSourceFile.setSourcePath("templates/app.c.ftl")
	appSourceFile.setOutputName("app.c")
	appSourceFile.setMarkup(True)
	appSourceFile.setOverwrite(True)
	appSourceFile.setDestPath("../../")
	appSourceFile.setProjectPath("")
	appSourceFile.setType("SOURCE")
	appSourceFile.setEnabled(False)
	appSourceFile.setDependencies(genAppSourceFile, ["CoreGenAppFiles"])

	#generate app.h file
	appHeaderFile = coreComponent.createFileSymbol(None, None)
	appHeaderFile.setSourcePath("templates/app.h.ftl")
	appHeaderFile.setOutputName("app.h")
	appHeaderFile.setMarkup(True)
	appHeaderFile.setOverwrite(True)
	appHeaderFile.setDestPath("../../")
	appHeaderFile.setProjectPath("")
	appHeaderFile.setType("HEADER")
	appHeaderFile.setEnabled(False)
	appHeaderFile.setDependencies(genAppHeaderFile, ["CoreGenAppFiles"])

	# load device specific information, clock and pin manager
	execfile(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")

def genAppSourceFile(appSourceFile, genAppFiles):
	appSourceFile.setEnabled(genAppFiles.getValue())

def genAppHeaderFile(appHeaderFile, genAppFiles):
	appHeaderFile.setEnabled(genAppFiles.getValue())
