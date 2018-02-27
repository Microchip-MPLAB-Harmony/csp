# load family specific configurations 
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_e70/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_e70/plugin/clockmanager.jar")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load device specific nvic manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic_m7/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic_m7/plugin/ARM_M7_NVICmanager.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/SAME70pinmanager.jar")

# load rswdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/rswdt_11110/config/rswdt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

#load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/MPUmanager.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("CORTEX-M7")
coreArch.setReadOnly(True)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_E70_S70_V70_V71")
deviceFamily.setReadOnly(True)


#generate system_startup_xc32.c file
armSysStartSourceFile = coreComponent.createFileSymbol(None, None)
armSysStartSourceFile.setSourcePath("arm/templates/system_startup_xc32.c.ftl")
armSysStartSourceFile.setOutputName("system_startup.c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

#generate newlib_syscalls_xc32.c file
armSysCallSourceFile = coreComponent.createFileSymbol(None, None)
armSysCallSourceFile.setSourcePath("arm/templates/newlib_syscalls_xc32.c.ftl")
armSysCallSourceFile.setOutputName("newlib_syscalls_xc32.c")
armSysCallSourceFile.setMarkup(True)
armSysCallSourceFile.setOverwrite(True)
armSysCallSourceFile.setDestPath("")
armSysCallSourceFile.setProjectPath("config/" + configName + "/")
armSysCallSourceFile.setType("SOURCE")

