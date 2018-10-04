# coding: utf-8
"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

# Maximum Application Tasks that can be created
appFileMaxCount = 10
appSourceFile = []
appHeaderFile = []
appHeaderName = []

def instantiateComponent(coreComponent):

    global appSourceFile
    global appHeaderFile
    global appHeaderName

    autoComponentIDTable = ["dfp", "cmsis"]
    res = Database.activateComponents(autoComponentIDTable)

    devMenu = coreComponent.createMenuSymbol("CoreDevMenu", None)
    devMenu.setLabel("Device & Project Configuration")

    devCfgMenu = coreComponent.createMenuSymbol("CoreCfgMenu", devMenu)
    devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
    devCfgMenu.setDescription("Hardware Configuration Bits")


    projMenu = coreComponent.createMenuSymbol("CoreProjMenu", devMenu)
    projMenu.setLabel("Project Configuration")

    exceptionHandling = coreComponent.createBooleanSymbol("ADVANCED_EXCEPTION", projMenu)
    exceptionHandling.setLabel("Use Harmony Exception Handling")
    exceptionHandling.setDefaultValue(False)
    
    toolchainMenu = coreComponent.createMenuSymbol("CoreToolchainMenu", projMenu)
    toolchainMenu.setLabel("Toolchain Selection")

    xc32Sym = coreComponent.createBooleanSymbol("XC32", toolchainMenu)
    xc32Sym.setLabel("XC32 Compiler")
    xc32Sym.setDefaultValue(True)
    xc32Sym.setReadOnly(True)

    xc32Menu = coreComponent.createMenuSymbol("CoreXC32Menu", projMenu)
    xc32Menu.setLabel("XC32 (Global Options)")

    xc32ldMenu = coreComponent.createMenuSymbol("CoreXC32_LD", xc32Menu)
    xc32ldMenu.setLabel("xc32-ld")

    xc32ldGeneralMenu = coreComponent.createMenuSymbol("CoreXC32_LD_General", xc32ldMenu)
    xc32ldGeneralMenu.setLabel("General")

    heapSize = coreComponent.createIntegerSymbol("HEAP_SIZE", xc32ldGeneralMenu)
    heapSize.setLabel("Heap Size (Bytes)")
    heapSize.setDefaultValue(0)
    heapSize.setVisible(True)

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
    systemInitLibList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA", None)
    systemInitSysList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION", None)
    systemAppInitDataList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_APP_INITIALIZE_DATA", None)

    systemInitCoreList = coreComponent.createListSymbol("LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE", None)
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
    systemIntHeadersList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_INCLUDES", None)
    systemIntVectorsList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_C_VECTORS", None)
    systemIntVectorsMultipleHandlesList = coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS", None)
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

    # set XC32 heap size
    xc32HeapSizeSym = coreComponent.createSettingSymbol("XC32_HEAP", None)
    xc32HeapSizeSym.setCategory("C32-LD")
    xc32HeapSizeSym.setKey("heap-size")
    xc32HeapSizeSym.setValue(str(heapSize.getValue()))
    xc32HeapSizeSym.setDependencies(xc32HeapSize, ["HEAP_SIZE"])

    # set XC32 include path
    defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
    defSym.setCategory("C32")
    defSym.setKey("extra-include-directories")
    defSym.setValue("../src;../src/config/"+configName+";../src/packs/"+Variables.get("__PROCESSOR")+"_DFP;../src/packs/CMSIS/CMSIS/Core/Include;../src/packs/CMSIS/")
    defSym.setAppend(True, ";")

    # set XC32 option to not use the device startup code
    xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("XC32_NO_DEVICE_STARTUP_CODE", None)
    xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
    xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
    xc32NoDeviceStartupCodeSym.setValue("true")

    debugSourceFile = coreComponent.createFileSymbol("DEBUG_CONSOLE_C", None)
    debugSourceFile.setSourcePath("../arch/stdio/templates/xc32_monitor.c.ftl")
    debugSourceFile.setOutputName("xc32_monitor.c")
    debugSourceFile.setMarkup(True)
    debugSourceFile.setOverwrite(True)
    debugSourceFile.setDestPath("/stdio/")
    debugSourceFile.setProjectPath("config/" + configName + "/stdio/")
    debugSourceFile.setType("SOURCE")

    # load device specific information, clock and pin manager
    execfile(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")

def xc32HeapSize(symbol, event):
     symbol.setValue(str(event["value"]))
