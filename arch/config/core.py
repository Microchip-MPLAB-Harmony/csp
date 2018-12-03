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

def genExceptionAsmSourceFile(symbol, event):
    coreSysFileEnabled = Database.getSymbolValue("core", "CoreSysFiles")
    coreSysExceptionFileEnabled = Database.getSymbolValue("core", "CoreSysExceptionFile")
    coreSysAdvancedExceptionFileEnabled = Database.getSymbolValue("core", "ADVANCED_EXCEPTION")

    if ((coreSysExceptionFileEnabled == True) and
        (coreSysAdvancedExceptionFileEnabled == True) and
        (coreSysFileEnabled == True)):
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def setFileVisibility (symbol, event):
    symbol.setVisible(event["value"])

def setSysFileVisibility (symbol, event):
    symbol.setVisible(event["value"])
    symbol.setValue(event["value"], 1)

def genMainSourceFile(symbol, event):
    mainName    = Database.getSymbolValue("core", "CoreMainFileName")
    genMainSrc  = Database.getSymbolValue("core", "CoreMainFile")

    if (genMainSrc == True):
        symbol.setOutputName(mainName.lower() + ".c")
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def genSysSourceFile(symbol, event):
    coreSysFileEnabled = Database.getSymbolValue("core", "CoreSysFiles")
    coreSysSourceFileEnabled = False

    if(event["id"] == "CoreSysDefFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysDefFile")
    elif(event["id"] == "CoreSysInitFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysInitFile")
    elif(event["id"] == "CoreSysIntFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysIntFile")
    elif(event["id"] == "CoreSysExceptionFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysExceptionFile")
    elif(event["id"] == "CoreSysStartupFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysStartupFile")
    elif(event["id"] == "CoreSysCallsFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysCallsFile")
    elif(event["id"] == "CoreSysStdioSyscallsFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysStdioSyscallsFile")

    if ((coreSysFileEnabled == True) and (coreSysSourceFileEnabled == True)):
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def instantiateComponent(coreComponent):
    autoComponentIDTable = ["dfp", "cmsis"]
    res = Database.activateComponents(autoComponentIDTable)

    coreArch = coreComponent.createStringSymbol("CoreArchitecture", None)
    coreArch.setDefaultValue(ATDF.getNode("/avr-tools-device-file/devices/device").getAttribute("architecture"))
    coreArch.setReadOnly(True)
    coreArch.setVisible(False)

    devMenu = coreComponent.createMenuSymbol("CoreDevMenu", None)
    devMenu.setLabel("Device & Project Configuration")

    devCfgMenu = coreComponent.createMenuSymbol("CoreCfgMenu", devMenu)
    devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
    devCfgMenu.setDescription("Hardware Configuration Bits")

    projMenu = coreComponent.createMenuSymbol("CoreProjMenu", devMenu)
    projMenu.setLabel("Project Configuration")

    genMainFile = coreComponent.createBooleanSymbol("CoreMainFile", projMenu)
    genMainFile.setLabel("Generate Main Source File")
    genMainFile.setDefaultValue(True)

    genMainFileName = coreComponent.createStringSymbol("CoreMainFileName", genMainFile)
    genMainFileName.setLabel("Main File Name")
    genMainFileName.setDescription("Main File Name")
    genMainFileName.setDefaultValue("main")
    genMainFileName.setDependencies(setFileVisibility, ["CoreMainFile"])

    genSysFiles = coreComponent.createBooleanSymbol("CoreSysFiles", projMenu)
    genSysFiles.setDefaultValue(True)
    genSysFiles.setLabel("Generate System Source Files")

    genSysDefFile = coreComponent.createBooleanSymbol("CoreSysDefFile", genSysFiles)
    genSysDefFile.setLabel("Generate System Definition")
    genSysDefFile.setDefaultValue(True)
    genSysDefFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysInitFile = coreComponent.createBooleanSymbol("CoreSysInitFile", genSysFiles)
    genSysInitFile.setLabel("Generate System Initialization")
    genSysInitFile.setDefaultValue(True)
    genSysInitFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysIntFile = coreComponent.createBooleanSymbol("CoreSysIntFile", genSysFiles)
    genSysIntFile.setLabel("Generate System Interrupts")
    genSysIntFile.setDefaultValue(True)
    genSysIntFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysCallsFile = coreComponent.createBooleanSymbol("CoreSysCallsFile", genSysFiles)
    genSysCallsFile.setLabel("Generate LIBC Syscalls")
    genSysCallsFile.setDefaultValue(True)
    genSysCallsFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysStartupFile = coreComponent.createBooleanSymbol("CoreSysStartupFile", genSysFiles)
    genSysStartupFile.setLabel("Generate System Startup")
    genSysStartupFile.setDefaultValue(True)
    genSysStartupFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysDebugConsoleFile = coreComponent.createBooleanSymbol("CoreSysStdioSyscallsFile", genSysFiles)
    genSysDebugConsoleFile.setLabel("Generate STDIO Syscalls")
    genSysDebugConsoleFile.setDefaultValue(True)
    genSysDebugConsoleFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysExceptionFile = coreComponent.createBooleanSymbol("CoreSysExceptionFile", genSysFiles)
    genSysExceptionFile.setLabel("Generate System Exception")
    genSysExceptionFile.setDefaultValue(True)
    genSysExceptionFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    exceptionHandling = coreComponent.createBooleanSymbol("ADVANCED_EXCEPTION", genSysExceptionFile)
    exceptionHandling.setLabel("Use Advanced Exception Handling")
    exceptionHandling.setDefaultValue(False)
    exceptionHandling.setDependencies(setFileVisibility, ["CoreSysExceptionFile"])

    arch = ""
    if "CORTEX" in coreArch.getValue():
        arch="arm"
    else:
        arch="mips"
    toolChainSpecifics = coreComponent.createFileSymbol(None, None)
    toolChainSpecifics.setSourcePath(arch+"/toolchain_specifics.h")
    toolChainSpecifics.setOutputName("toolchain_specifics.h");
    toolChainSpecifics.setMarkup(False)
    toolChainSpecifics.setOverwrite(True)
    toolChainSpecifics.setDestPath("../../"+arch)
    toolChainSpecifics.setProjectPath(arch)
    toolChainSpecifics.setType("HEADER")

    toolChainMenu = coreComponent.createMenuSymbol("CoreToolChainMenu", projMenu)
    toolChainMenu.setLabel("Tool Chain Selections")

    compilerSymbolName = "COMPILER_CHOICE"
    compilerChoice = coreComponent.createKeyValueSetSymbol( compilerSymbolName, toolChainMenu )
    compilerChoice.setLabel( "Compiler" )
    compilerChoice.setOutputMode( "Key" )
    compilerChoice.setDisplayMode( "Description" )
    compilerChoice.setVisible( True )
    compilerChoices =       [( "XC32_COMPILER",  "0", "XC32" ), 
                             ( "IAR_COMPILER",   "1", "IAR" ), 
                             ]
    for tupleElem in compilerChoices:
        compilerChoice.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    ## xc32 Tool Config
    xc32Menu = coreComponent.createMenuSymbol("CoreXC32Menu", toolChainMenu)
    xc32Menu.setLabel("XC32 Global Options")

    xc32LdMenu = coreComponent.createMenuSymbol("CoreXC32_LD", xc32Menu)
    xc32LdMenu.setLabel("Linker")

    xc32LdGeneralMenu = coreComponent.createMenuSymbol("CoreXC32_LD_General", xc32LdMenu)
    xc32LdGeneralMenu.setLabel("General")

    xc32HeapSize = coreComponent.createIntegerSymbol("XC32_HEAP_SIZE", xc32LdGeneralMenu)
    xc32HeapSize.setLabel("Heap Size (bytes)")
    xc32HeapSize.setDefaultValue(0)
    xc32HeapSize.setVisible(True)

    ## iar Tool Config
    iarMenu = coreComponent.createMenuSymbol("CoreIARMenu", toolChainMenu)
    iarMenu.setLabel("IAR Global Options")

    iarLdMenu = coreComponent.createMenuSymbol("CoreIAR_LD", iarMenu)
    iarLdMenu.setLabel("Linker")

    iarLdGeneralMenu = coreComponent.createMenuSymbol("CoreIAR_LD_General", iarLdMenu)
    iarLdGeneralMenu.setLabel("General")

    iarHeapSize = coreComponent.createIntegerSymbol("IAR_HEAP_SIZE", iarLdGeneralMenu)
    iarHeapSize.setLabel("Heap Size (bytes)")
    iarHeapSize.setDefaultValue(512)
    iarHeapSize.setVisible(True)

    iarUsrStackSize = coreComponent.createIntegerSymbol("IAR_USR_STACK_SIZE", iarLdGeneralMenu)
    iarUsrStackSize.setLabel("User Stack Size (bytes)")
    iarUsrStackSize.setDefaultValue(4096)
    iarUsrStackSize.setVisible(True)

    iarFiqStackSize = coreComponent.createIntegerSymbol("IAR_FIQ_STACK_SIZE", iarLdGeneralMenu)
    iarFiqStackSize.setLabel("FIQ Stack Size (bytes)")
    iarFiqStackSize.setDefaultValue(96)
    iarFiqStackSize.setVisible(True)

    iarIrqStackSize = coreComponent.createIntegerSymbol("IAR_IRQ_STACK_SIZE", iarLdGeneralMenu)
    iarIrqStackSize.setLabel("IRQ Stack Size (bytes)")
    iarIrqStackSize.setDefaultValue(96)
    iarIrqStackSize.setVisible(True)

    iarSvcStackSize = coreComponent.createIntegerSymbol("IAR_SVC_STACK_SIZE", iarLdGeneralMenu)
    iarSvcStackSize.setLabel("Superviser Stack Size (bytes)")
    iarSvcStackSize.setDefaultValue(96)
    iarSvcStackSize.setVisible(True)

    iarAbtStackSize = coreComponent.createIntegerSymbol("IAR_ABT_STACK_SIZE", iarLdGeneralMenu)
    iarAbtStackSize.setLabel("Abort Stack Size (bytes)")
    iarAbtStackSize.setDefaultValue(64)
    iarAbtStackSize.setVisible(True)

    iarSysStackSize = coreComponent.createIntegerSymbol("IAR_SYS_STACK_SIZE", iarLdGeneralMenu)
    iarSysStackSize.setLabel("System Stack Size (bytes)")
    iarSysStackSize.setDefaultValue(64)
    iarSysStackSize.setVisible(True)

    iarUndStackSize = coreComponent.createIntegerSymbol("IAR_UND_STACK_SIZE", iarLdGeneralMenu)
    iarUndStackSize.setLabel("Undefined Stack Size (bytes)")
    iarUndStackSize.setDefaultValue(64)
    iarUndStackSize.setVisible(True)

    configName = Variables.get("__CONFIGURATION_NAME")

    #################### Main File ####################
    # generate main.c file
    mainSourceFile = coreComponent.createFileSymbol("MAIN_C", None)
    mainSourceFile.setSourcePath("templates/main.c.ftl")
    mainSourceFile.setOutputName("main.c")
    mainSourceFile.setMarkup(True)
    mainSourceFile.setOverwrite(False)
    mainSourceFile.setDestPath("../../")
    mainSourceFile.setProjectPath("")
    mainSourceFile.setType("SOURCE")
    mainSourceFile.setDependencies(genMainSourceFile, ["CoreMainFile", "CoreMainFileName"])

    bspHeaderInclude = coreComponent.createListSymbol("LIST_BSP_MACRO_INCLUDES", None)
    bspHeaderInclude = coreComponent.createListSymbol("LIST_BSP_INITIALIZATION", None)

    # list of SYS_PORTS
    systemPortIncludesList = coreComponent.createListSymbol("LIST_SYS_PORT_INCLUDES", None)

    # list for configuration.h
    systemConfigIncludesList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES", None)
    systemConfigSysList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION", None)
    systemConfigDrvList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION", None)
    systemConfigMWList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION", None)
    systemConfigAppList = coreComponent.createListSymbol("LIST_SYSTEM_CONFIG_H_APPLICATION_CONFIGURATION", None)

    # list for task.c file
    taskSysList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_SYSTEM_TASKS", None)
    taskDrvList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS", None)
    taskLibList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS", None)
    taskGenAppList = coreComponent.createListSymbol("LIST_SYSTEM_TASKS_C_GEN_APP", None)
    taskGenRtosAppList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_GEN_APP", None)
    taskRtosDefList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS", None)
    taskRtosSchedList = coreComponent.createListSymbol("LIST_SYSTEM_RTOS_TASKS_C_CALL_SCHEDULAR", None)

    #################### System Files ####################
    # generate definitions.h file
    defHeaderFile = coreComponent.createFileSymbol("DEFINITIONS_H", None)
    defHeaderFile.setSourcePath("templates/definitions.h.ftl")
    defHeaderFile.setOutputName("definitions.h")
    defHeaderFile.setMarkup(True)
    defHeaderFile.setOverwrite(True)
    defHeaderFile.setDestPath("")
    defHeaderFile.setProjectPath("config/" + configName + "/")
    defHeaderFile.setType("HEADER")
    defHeaderFile.setDependencies(genSysSourceFile, ["CoreSysDefFile", "CoreSysFiles"])
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
    initSourceFile.setDependencies(genSysSourceFile, ["CoreSysInitFile", "CoreSysFiles"])
    systemInitFuseList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION", None)
    systemInitDrvList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA", None)
    systemInitLibList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA", None)
    systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION", None)
    systemAppInitDataList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_APP_INITIALIZE_DATA", None)

    systemInitCoreList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE", None)
    systemInitInterruptList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_INTERRUPTS", None)
    systemInitBootloaderList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_BOOTLOADER_TRIGGER", None)
    systemInitPeripheralList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS", None)
    systemInitDriver2List = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS", None)
    systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES", None)
    systemInitMWList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE", None)

    # generate interrupts.c file
    intSourceFile = coreComponent.createFileSymbol("INTERRUPTS_C", None)
    intSourceFile.setSourcePath("templates/interrupts.c.ftl")
    intSourceFile.setOutputName("interrupts.c")
    intSourceFile.setMarkup(True)
    intSourceFile.setOverwrite(True)
    intSourceFile.setDestPath("")
    intSourceFile.setProjectPath("config/" + configName + "/")
    intSourceFile.setType("SOURCE")
    intSourceFile.setDependencies(genSysSourceFile, ["CoreSysIntFile", "CoreSysFiles"])
    systemIntHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_INCLUDES", None)
    systemIntVectorsList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_VECTORS", None)
    systemIntVectorsMultipleHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS", None)
    systemIntVectorsWeakHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS", None)
    systemIntVectorsSharedHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS", None)
    systemIntVectorsHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_HANDLERS", None)

    debugSourceFile = coreComponent.createFileSymbol("DEBUG_CONSOLE_C", None)
    debugSourceFile.setSourcePath("../arch/stdio/templates/xc32_monitor.c.ftl")
    debugSourceFile.setOutputName("xc32_monitor.c")
    debugSourceFile.setMarkup(True)
    debugSourceFile.setOverwrite(True)
    debugSourceFile.setDestPath("/stdio/")
    debugSourceFile.setProjectPath("config/" + configName + "/stdio/")
    debugSourceFile.setType("SOURCE")
    debugSourceFile.setDependencies(genSysSourceFile, ["CoreSysStdioSyscallsFile", "CoreSysFiles"])

    # generate exceptions.c file
    exceptSourceFile = coreComponent.createFileSymbol("EXCEPTIONS_C", None)
    exceptSourceFile.setSourcePath("templates/exceptions.c.ftl")
    exceptSourceFile.setOutputName("exceptions.c")
    exceptSourceFile.setMarkup(True)
    exceptSourceFile.setOverwrite(True)
    exceptSourceFile.setDestPath("")
    exceptSourceFile.setProjectPath("config/" + configName + "/")
    exceptSourceFile.setType("SOURCE")
    exceptSourceFile.setDependencies(genSysSourceFile, ["CoreSysExceptionFile", "CoreSysFiles"])

    # generate exceptionsHandler.s file
    exceptionAsmSourceFile = coreComponent.createFileSymbol("EXCEPTIONS_ASM", None)
    exceptionAsmSourceFile.setSourcePath("templates/exceptionsHandler.s.ftl")
    exceptionAsmSourceFile.setOutputName("exceptionsHandler.s")
    exceptionAsmSourceFile.setMarkup(True)
    exceptionAsmSourceFile.setOverwrite(True)
    exceptionAsmSourceFile.setDestPath("")
    exceptionAsmSourceFile.setProjectPath("config/" + configName + "/")
    exceptionAsmSourceFile.setType("SOURCE")
    exceptionAsmSourceFile.setEnabled(False)
    exceptionAsmSourceFile.setDependencies(genExceptionAsmSourceFile, ["CoreSysFiles", "CoreSysExceptionFile", "ADVANCED_EXCEPTION"])

    # set XC32 heap size
    xc32HeapSizeSym = coreComponent.createSettingSymbol("XC32_HEAP", None)
    xc32HeapSizeSym.setCategory("C32-LD")
    xc32HeapSizeSym.setKey("heap-size")
    xc32HeapSizeSym.setValue(str(xc32HeapSize.getValue()))
    xc32HeapSizeSym.setDependencies(heapSizeCallBack, ["XC32_HEAP_SIZE"])

    # set include path and monitor file
    processor = Variables.get("__PROCESSOR")
    corePath = ""
    if "SAMA5" in processor:
        corePath = "../src/packs/CMSIS/CMSIS/Core_A/Include"
    else:
        corePath = "../src/packs/CMSIS/CMSIS/Core/Include"

    defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
    defSym.setCategory("C32")
    defSym.setKey("extra-include-directories")
    defSym.setValue("../src;../src/config/" + configName + ";../src/packs/" + processor + "_DFP;"+corePath+";../src/packs/CMSIS/;../src/"+arch)
    defSym.setAppend(True, ";")

    # set XC32 option to not use the device startup code
    xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("XC32_NO_DEVICE_STARTUP_CODE", None)
    xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
    xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
    xc32NoDeviceStartupCodeSym.setValue("true")

    debugSourceFile.setType("SOURCE")
    debugSourceFile.setSourcePath("../arch/stdio/templates/xc32_monitor.c.ftl")
    debugSourceFile.setOutputName("xc32_monitor.c")
    debugSourceFile.setDependencies( debugSourceCallBack, [ compilerSymbolName ] )
    monitorFile ="xc32_monitor.c"
    if "IAR_COMPILER" == compilerChoice.getValue():
        monitorFile ="iar_monitor.c"

    debugSourceFile.setProjectPath("config/" + configName + "/stdio/")
    debugSourceFile.setType("SOURCE")
    # load device specific information, clock and pin manager
    execfile(Variables.get("__ARCH_DIR") + "/" + processor + ".py")


def heapSizeCallBack(symbol, event):
    symbol.setValue(str(event["value"]))


def debugSourceCallBack( debugSourceFile, event ):
    compilerChoiceSymbol = event[ "symbol" ]
    monitorFile ="xc32_monitor.c"
    if "IAR_COMPILER" == compilerChoiceSymbol.getSelectedKey():
        monitorFile ="iar_monitor.c"
    debugSourceFile.setSourcePath("../arch/stdio/templates/" + monitorFile + ".ftl")
    debugSourceFile.setOutputName( monitorFile )
    print "monitorFile:" + monitorFile 

