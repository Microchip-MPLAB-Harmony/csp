# Maximum Application Tasks that can be created
appFileMaxCount = 10
appSourceFile = []
appHeaderFile = []
appSrcName    = []
appHeaderName = []

def instantiateComponent(coreComponent):
    global appSourceFile
    global appHeaderFile
    global appSrcName
    global appHeaderName

    devMenu = coreComponent.createMenuSymbol("CoreDevMenu", None)
    devMenu.setLabel("Device Configuration")

    devCfgMenu = coreComponent.createMenuSymbol("CoreCfgMenu", devMenu)
    devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
    devCfgMenu.setDescription("Hardware Configuration Bits")

    genAppFiles = coreComponent.createBooleanSymbol("CoreGenAppFiles", devMenu)
    genAppFiles.setLabel("Generate Harmony Application Files?")
    genAppFiles.setVisible(False)

    stdioEnable = coreComponent.createBooleanSymbol("STDIO_USED", devMenu)
    stdioEnable.setVisible(False)
    stdioEnable.setDefaultValue(False)
    stdioEnable.setDependencies(stdioActivated, ["stdio.STDIO_ENABLE"])

    configName = Variables.get("__CONFIGURATION_NAME")

    #################### Application Files ####################
    # generate main.c file
    mainSourceFile = coreComponent.createFileSymbol("MAIN_C", None)
    mainSourceFile.setSourcePath("templates/main.c.ftl")
    mainSourceFile.setOutputName("main.c")
    mainSourceFile.setMarkup(True)
    mainSourceFile.setOverwrite(False)
    mainSourceFile.setDestPath("../../")
    mainSourceFile.setProjectPath("")
    mainSourceFile.setType("SOURCE")

    bspHeaderInclude = coreComponent.createListSymbol("LIST_BSP_MACRO_INCLUDES", None)
    bspHeaderInclude = coreComponent.createListSymbol("LIST_BSP_INITIALIZATION", None)

    for count in range(0, appFileMaxCount):
        global appSourceFile
        global appSrcName
        global appHeaderFile
        global appHeaderName

        # generate app.c file
        appSrcName.append(count)
        appSrcName[count] = "Harmony.GEN_APP_TASK_NAME_" + str(count)

        appSourceFile.append(count)
        appSourceFile[count] = coreComponent.createFileSymbol("APP" + str(count) + "_C", None)
        appSourceFile[count].setSourcePath("templates/app.c.ftl")
        if (count == 0):
            appSourceFile[count].setOutputName("app.c")
        else:
            appSourceFile[count].setOutputName("app" + str(count) + ".c")
        appSourceFile[count].setMarkup(True)
        appSourceFile[count].setOverwrite(False)
        appSourceFile[count].setDestPath("../../")
        appSourceFile[count].setProjectPath("")
        appSourceFile[count].setType("SOURCE")
        appSourceFile[count].setEnabled(False)
        appSourceFile[count].setDependencies(genAppSourceFile, ["CoreGenAppFiles", "Harmony.GEN_APP_TASK_COUNT", "Harmony.GEN_APP_TASK_NAME_" + str(count)])
        appSourceFile[count].addMarkupVariable("APP_NAME", appSrcName[count])

        # generate app.h file
        appHeaderName.append(count)
        appHeaderName[count] = "Harmony.GEN_APP_TASK_NAME_" + str(count)

        appHeaderFile.append(count)
        appHeaderFile[count] = coreComponent.createFileSymbol("APP" + str(count) + "_H", None)
        appHeaderFile[count].setSourcePath("templates/app.h.ftl")
        if (count == 0):
            appHeaderFile[count].setOutputName("app.h")
        else:
            appHeaderFile[count].setOutputName("app" + str(count) + ".h")
        appHeaderFile[count].setMarkup(True)
        appHeaderFile[count].setOverwrite(False)
        appHeaderFile[count].setDestPath("../../")
        appHeaderFile[count].setProjectPath("")
        appHeaderFile[count].setType("HEADER")
        appHeaderFile[count].setEnabled(False)
        appHeaderFile[count].setDependencies(genAppHeaderFile, ["CoreGenAppFiles", "Harmony.GEN_APP_TASK_COUNT", "Harmony.GEN_APP_TASK_NAME_" + str(count)])
        appHeaderFile[count].addMarkupVariable("APP_NAME", appHeaderName[count])

    #################### Configuration Files ####################
    # generate user.h file
    userHeaderFile = coreComponent.createFileSymbol("USER_H", None)
    userHeaderFile.setSourcePath("templates/user.h.ftl")
    userHeaderFile.setOutputName("user.h")
    userHeaderFile.setMarkup(True)
    userHeaderFile.setOverwrite(False)
    userHeaderFile.setDestPath("")
    userHeaderFile.setProjectPath("config/" + configName + "/")
    userHeaderFile.setType("HEADER")
    userHeaderFile.setEnabled(False)
    userHeaderFile.setDependencies(genUserHeaderFile, ["CoreGenAppFiles"])
    appConfigIncludesList = coreComponent.createListSymbol("LIST_APP_CONFIG_H_GLOBAL_INCLUDES", None)

    # generate configuration.h file
    confHeaderFile = coreComponent.createFileSymbol("CONFIGURATION_H", None)
    confHeaderFile.setSourcePath("templates/configuration.h.ftl")
    confHeaderFile.setOutputName("configuration.h")
    confHeaderFile.setMarkup(True)
    confHeaderFile.setOverwrite(True)
    confHeaderFile.setDestPath("")
    confHeaderFile.setProjectPath("config/" + configName + "/")
    confHeaderFile.setType("HEADER")
    confHeaderFile.setEnabled(False)
    systemConfigIncludesList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES", None)
    systemConfigSysList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION", None)
    systemConfigDrvList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION", None)
    systemConfigMWList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION", None)
    systemConfigAppList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_APPLICATION_CONFIGURATION", None)
    confHeaderFile.setDependencies(genConfHeaderFile, ["CoreGenAppFiles"])

    # generate definitions.h file
    defHeaderFile = coreComponent.createFileSymbol("DEFINITIONS_H", None)
    defHeaderFile.setSourcePath("templates/definitions.h.ftl")
    defHeaderFile.setOutputName("definitions.h")
    defHeaderFile.setMarkup(True)
    defHeaderFile.setOverwrite(True)
    defHeaderFile.setDestPath("")
    defHeaderFile.setProjectPath("config/" + configName + "/")
    defHeaderFile.setType("HEADER")
    systemDefinitionsHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_INCLUDES", None)
    systemDefinitionsObjList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_OBJECTS", None)
    systemDefinitionsExternsList = coreComponent.createListSymbol("LIST_SYSTEM_DEFINITIONS_H_EXTERNS", None)
    systemAppDefinitionsHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_APP_DEFINITIONS_H_INCLUDES", None)

    # generate initialization.c file
    initSourceFile = coreComponent.createFileSymbol("INITIALIZATION_C", None)
    initSourceFile.setSourcePath("templates/initialization.c.ftl")
    initSourceFile.setOutputName("initialization.c")
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
    systemAppInitDataList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_APP_INITIALIZE_DATA", None)

    systemInitCoreList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_MPU", None)
    systemInitCoreList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE", None)
    systemInitPeripheralList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS", None)
    systemInitDriver1List = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS", None)
    systemInitDriver2List = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS", None)
    systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES", None)
    systemInitMWList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE", None)

    # generate tasks.c file
    taskSourceFile = coreComponent.createFileSymbol("TASKS_C", None)
    taskSourceFile.setSourcePath("templates/tasks.c.ftl")
    taskSourceFile.setOutputName("tasks.c")
    taskSourceFile.setMarkup(True)
    taskSourceFile.setOverwrite(True)
    taskSourceFile.setDestPath("")
    taskSourceFile.setProjectPath("config/" + configName + "/")
    taskSourceFile.setType("SOURCE")
    taskSourceFile.setEnabled(False)
    taskSysList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_SYSTEM_TASKS", None)
    taskDrvList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS", None)
    taskLibList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS", None)
    taskGenAppList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_GEN_APP", None)
    taskGenRtosAppList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_GEN_APP", None)
    taskRtosDefList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS", None)
    taskRtosSchedList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_CALL_SCHEDULAR", None)
    taskSourceFile.setDependencies(genTaskSourceFile, ["CoreGenAppFiles"])

    # generate interrupts.c file
    intSourceFile = coreComponent.createFileSymbol("INTERRUPTS_C", None)
    intSourceFile.setSourcePath("templates/interrupts.c.ftl")
    intSourceFile.setOutputName("interrupts.c")
    intSourceFile.setMarkup(True)
    intSourceFile.setOverwrite(True)
    intSourceFile.setDestPath("")
    intSourceFile.setProjectPath("config/" + configName + "/")
    intSourceFile.setType("SOURCE")
    systemIntHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_INCLUDES", None)
    systemIntVectorsList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_VECTORS", None)
    systemIntVectorsWeakHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS", None)
    systemIntVectorsHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_HANDLERS", None)

    # generate exceptions.c file
    intSourceFile = coreComponent.createFileSymbol("EXCEPTIONS_C", None)
    intSourceFile.setSourcePath("templates/exceptions.c.ftl")
    intSourceFile.setOutputName("exceptions.c")
    intSourceFile.setMarkup(True)
    intSourceFile.setOverwrite(True)
    intSourceFile.setDestPath("")
    intSourceFile.setProjectPath("config/" + configName + "/")
    intSourceFile.setType("SOURCE")

    # set XC32 include path
    defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
    defSym.setCategory("C32")
    defSym.setKey("extra-include-directories")
    defSym.setValue("../src;../src/config/"+configName+";../src/packs/"+Variables.get("__PROCESSOR")+"_DFP;../src/packs/CMSIS")
    defSym.setAppend(True, ";")

    # set XC32 option to not use the device startup code
    xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("XC32_NO_DEVICE_STARTUP_CODE", None)
    xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
    xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
    xc32NoDeviceStartupCodeSym.setValue("true")

    # load device specific information, clock and pin manager
    execfile(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")

def genAppSourceFile(symbol, event):
    global appSourceFile
    appName = None

    appFileEnableCount = Database.getSymbolValue("Harmony", "GEN_APP_TASK_COUNT")
    appGenFiles        = Database.getSymbolValue("core", "CoreGenAppFiles")

    for count in range(0, appFileMaxCount):
        appSourceFile[count].setEnabled(False)

    if (appGenFiles == True):
        for count in range(0, appFileEnableCount):
            appName = Database.getSymbolValue("Harmony", "GEN_APP_TASK_NAME_" + str(count))
            appSourceFile[count].setEnabled(True)
            appSourceFile[count].setOutputName(appName.lower() + ".c")

def genAppHeaderFile(symbol, event):
    global appHeaderFile
    appName = None

    appFileEnableCount = Database.getSymbolValue("Harmony", "GEN_APP_TASK_COUNT")
    appGenFiles        = Database.getSymbolValue("core", "CoreGenAppFiles")

    for count in range(0, appFileMaxCount):
        appHeaderFile[count].setEnabled(False)

    if (appGenFiles == True):
        for count in range(0, appFileEnableCount):
            appName = Database.getSymbolValue("Harmony", "GEN_APP_TASK_NAME_" + str(count))
            appHeaderFile[count].setEnabled(True)
            appHeaderFile[count].setOutputName(appName.lower() + ".h")

def genTaskSourceFile(taskSourceFile, event):
    taskSourceFile.setEnabled(event["value"])

def genConfHeaderFile(confHeaderFile, event):
    confHeaderFile.setEnabled(event["value"])

def genUserHeaderFile(userHeaderFile, event):
    userHeaderFile.setEnabled(event["value"])

def stdioActivated(symbol, event):
    symbol.setValue(event["value"], 2)
