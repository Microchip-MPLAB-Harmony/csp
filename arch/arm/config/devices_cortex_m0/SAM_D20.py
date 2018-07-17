# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)" )
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)


coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("CORTEX-M0+")
coreArch.setReadOnly(True)
coreArch.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_D20")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M0+ Configuration")
cortexMenu.setDescription("Configuration for Cortex M0+")

# load clock manager information
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_d20/config/clk.py")
#coreComponent.addPlugin("../peripheral/clk_sam_d20_d21/plugin/clockmanager.jar")

# load device specific pin manager information
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
#coreComponent.addPlugin("../peripheral/port_u2210/plugin/SAMC2xpinmanager.jar")

# load NVIC
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic_m7/config/nvic.py")
#coreComponent.addPlugin("../peripheral/nvic_m7/plugin/ARM_M7_NVICmanager.jar")

#load systick
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# load dma manager information
# execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2223/config/dmac.py")
# coreComponent.addPlugin("../peripheral/dmac_u2223/plugin/dmamanager.jar")

# load wdt
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load device specific adc manager information
#coreComponent.addPlugin("../peripheral/afec_11147/plugin/ARM_M7_ADCmanager.jar")

# generate startup_xc32.c file
armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("arm/templates/startup_xc32.c.ftl")
armSysStartSourceFile.setOutputName("startup.c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")


