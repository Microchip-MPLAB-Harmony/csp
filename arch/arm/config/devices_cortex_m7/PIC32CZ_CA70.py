# load family specific configurations 
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_e70/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_e70/plugin/clockmanager.jar")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")

# load device specific nvic manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic_m7/config/nvic.py")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/SAME70pinmanager.jar")

# load rswdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/rswdt_11110/config/rswdt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

coreUseMPU = coreComponent.createBooleanSymbol("CoreUseMPU", devCfgMenu)
coreUseMPU.setLabel("Enable MPU?")

coreUseTimer = coreComponent.createBooleanSymbol("CoreUseTimer", devCfgMenu)
coreUseTimer.setLabel("Enable Core Timer?")
coreUseTimer.setReadOnly(True)

coreUseCustomVector = coreComponent.createBooleanSymbol("CoreUseCustomVector", devCfgMenu)
coreUseCustomVector.setLabel("Enable Customizable Interrupt Handlers?")

customVectorName = coreComponent.createStringSymbol("CustomVectorName", coreUseCustomVector)
customVectorName.setLabel("Reset Handler Name")

coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("CORTEX-M7")
coreArch.setReadOnly(True)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_E70_S70_V70_V71")
deviceFamily.setReadOnly(True)

#generate arm_cm_mpu.c file
armMPUSourceFile = coreComponent.createFileSymbol(None, None)
armMPUSourceFile.setSourcePath("arm/templates/arm_cm_mpu.c.ftl")
armMPUSourceFile.setOutputName("arm_cm_mpu.c")
armMPUSourceFile.setMarkup(True)
armMPUSourceFile.setOverwrite(True)
armMPUSourceFile.setDestPath("arch/arm/")
armMPUSourceFile.setProjectPath("config/" + configName + "/arch/arm/")
armMPUSourceFile.setType("SOURCE")
armMPUSourceFile.setEnabled(False)

def genMPUSourceFile(armMPUSourceFile, CoreUseMPU):
	armMPUSourceFile.setEnabled(CoreUseMPU.getValue())

armMPUSourceFile.setDependencies(genMPUSourceFile, ["CoreUseMPU"])

#generate arm_cm_mpu.h file
armMPUHeaderFile = coreComponent.createFileSymbol(None, None)
armMPUHeaderFile.setSourcePath("arm/templates/arm_cm_mpu.h.ftl")
armMPUHeaderFile.setOutputName("arm_cm_mpu.h")
armMPUHeaderFile.setMarkup(True)
armMPUHeaderFile.setOverwrite(True)
armMPUHeaderFile.setDestPath("arch/arm/")
armMPUHeaderFile.setProjectPath("config/" + configName + "/arch/arm/")
armMPUHeaderFile.setType("HEADER")
armMPUHeaderFile.setEnabled(False)

def genMPUHeaderFile(armMPUHeaderFile, CoreUseMPU):
	armMPUHeaderFile.setEnabled(CoreUseMPU.getValue())

armMPUHeaderFile.setDependencies(genMPUHeaderFile, ["CoreUseMPU"])

#generate system_core_mpu.c file
armSysMPUSourceFile = coreComponent.createFileSymbol(None, None)
armSysMPUSourceFile.setSourcePath("arm/templates/system_core_mpu.c.ftl")
armSysMPUSourceFile.setOutputName("system_core_mpu.c")
armSysMPUSourceFile.setMarkup(True)
armSysMPUSourceFile.setOverwrite(True)
armSysMPUSourceFile.setDestPath("arch/arm/")
armSysMPUSourceFile.setProjectPath("config/" + configName + "/arch/arm/")
armSysMPUSourceFile.setType("SOURCE")
armSysMPUSourceFile.setEnabled(False)

def genSysMPUSourceFile(armSysMPUSourceFile, CoreUseMPU):
	armSysMPUSourceFile.setEnabled(CoreUseMPU.getValue())

armSysMPUSourceFile.setDependencies(genSysMPUSourceFile, ["CoreUseMPU"])

#generate arch.h file
def genArchHeaderFile(archHeaderFile, CoreUseMPU):
	coreUseMPU = archHeaderFile.getComponent().getSymbolValue("CoreUseMPU")
	coreUseTimer = archHeaderFile.getComponent().getSymbolValue("CoreUseTimer")

	if(coreUseMPU or coreUseTimer):
		archHeaderFile.setEnabled(True)
	else:
		archHeaderFile.setEnabled(False)

archHeaderFile = coreComponent.createFileSymbol(None, None)
archHeaderFile.setSourcePath("arm/templates/arch.h.ftl")
archHeaderFile.setOutputName("arch.h")
archHeaderFile.setMarkup(True)
archHeaderFile.setOverwrite(True)
archHeaderFile.setDestPath("arch/")
archHeaderFile.setProjectPath("config/" + configName + "/arch/")
archHeaderFile.setType("HEADER")
archHeaderFile.setEnabled(False)
archHeaderFile.setDependencies(genArchHeaderFile, ["CoreUseMPU", "CoreUseTimer"])

def genArchHeaderFileList(archHeaderFileListEntry, CoreUseMPU):
	coreUseMPU = archHeaderFileListEntry.getComponent().getSymbolValue("CoreUseMPU")
	coreUseTimer = archHeaderFileListEntry.getComponent().getSymbolValue("CoreUseTimer")

	if(coreUseMPU or coreUseTimer):
		archHeaderFileListEntry.setEnabled(True)
	else:
		archHeaderFileListEntry.setEnabled(False)

archHeaderFileListEntry = coreComponent.createListEntrySymbol(None, None)
archHeaderFileListEntry.setTarget("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
archHeaderFileListEntry.addValue("#include \"arch/arch.h\"")
archHeaderFileListEntry.setEnabled(False)
archHeaderFileListEntry.setDependencies(genArchHeaderFileList, ["CoreUseMPU", "CoreUseTimer"])

#Add code to initialize Core Timer
archInitFile = coreComponent.createFileSymbol(None, None)
archInitFile.setType("STRING")
archInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
archInitFile.setSourcePath("arm/templates/arch_system_init.c.ftl")
archInitFile.setMarkup(True)

#generate system_startup_xc32.c file
armSysStartSourceFile = coreComponent.createFileSymbol(None, None)
armSysStartSourceFile.setSourcePath("arm/templates/system_startup_xc32.c.ftl")
armSysStartSourceFile.setOutputName("system_startup.c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartHandlersList = coreComponent.createListSymbol("LIST_SYSTEM_STARTUP_INTERRUPT_HANDLERS", None)

#generate newlib_syscalls_xc32.c file
armSysCallSourceFile = coreComponent.createFileSymbol(None, None)
armSysCallSourceFile.setSourcePath("arm/templates/newlib_syscalls_xc32.c.ftl")
armSysCallSourceFile.setOutputName("newlib_syscalls_xc32.c")
armSysCallSourceFile.setMarkup(True)
armSysCallSourceFile.setOverwrite(True)
armSysCallSourceFile.setDestPath("")
armSysCallSourceFile.setProjectPath("config/" + configName + "/")
armSysCallSourceFile.setType("SOURCE")

#generate device specific header file
armDeviceHeaderFile = coreComponent.createFileSymbol(None, None)
armDeviceHeaderFile.setSourcePath("arm/templates/devices_cortex_m7.h.ftl")
armDeviceHeaderFile.setOutputName("device_" + Variables.get("__PROCESSOR") + ".h")
armDeviceHeaderFile.setMarkup(True)
armDeviceHeaderFile.setOverwrite(True)
armDeviceHeaderFile.setDestPath("arch/arm/")
armDeviceHeaderFile.setProjectPath("config/" + configName + "/arch/arm/")
armDeviceHeaderFile.setType("HEADER")

armDeviceHeaderFileListEntry = coreComponent.createListEntrySymbol(None, None)
armDeviceHeaderFileListEntry.setTarget("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
armDeviceHeaderFileListEntry.addValue("#include \"arch/arm/device_" + Variables.get("__PROCESSOR") + ".h\"")
