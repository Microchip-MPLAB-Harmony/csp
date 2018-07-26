print ("Loading System Services for " + Variables.get("__PROCESSOR"))

coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("ARM-926")
coreArch.setReadOnly(True)
coreArch.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM9X6")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("ARM 926 Configuration")
cortexMenu.setDescription("Configuration for ARM 926")

# load clock manager information

# load device specific pin manager information

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(True)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

# load AIC

# load PIT

# load dma manager information
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
#coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load wdt

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("arm/templates/9x_cstartup.s.ftl")
armSysStartSourceFile.setOutputName("cstartup.s")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

#default exception handlers.
faultSourceFile = coreComponent.createFileSymbol("DFLT_FAULT_HANDLER_C", None)
faultSourceFile.setSourcePath("arm/templates/a5_vectortrap.s.ftl")
faultSourceFile.setOutputName("vectortrap.s")
faultSourceFile.setMarkup(True)
faultSourceFile.setOverwrite(True)
faultSourceFile.setDestPath("")
faultSourceFile.setProjectPath("config/" + configName + "/")
faultSourceFile.setType("SOURCE")
