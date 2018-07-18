global xc32StackInTCMSym
global xc32DTCMSizeSym
global xc32ITCMSizeSym
global tcmSize
global tcmEnable

def xc32SetTcmSize(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "0KB"):
        xc32DTCMSizeSym.setValue("")
        xc32ITCMSizeSym.setValue("")
    elif (symObj.getSelectedKey() == "32KB"):
        xc32DTCMSizeSym.setValue("0x8000")
        xc32ITCMSizeSym.setValue("0x8000")
    elif (symObj.getSelectedKey() == "64KB"):
        xc32DTCMSizeSym.setValue("0x10000")
        xc32ITCMSizeSym.setValue("0x10000")
    elif (symObj.getSelectedKey() == "128KB"):
        xc32DTCMSizeSym.setValue("0x20000")
        xc32ITCMSizeSym.setValue("0x20000")

def xc32SetStackInTcm(symbol, event):
    if (event["value"] == True):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")

def setTcmSize(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey()  == "0KB"):
        tcmSize.setValue("0 KB",2)
        tcmEnable.setValue(False,2)
    elif (symObj.getSelectedKey()  == "32KB"):
        tcmSize.setValue("32 KB",2)
        tcmEnable.setValue(True,2)
    elif (symObj.getSelectedKey()  == "64KB"):
        tcmSize.setValue("64 KB",2)
        tcmEnable.setValue(True,2)
    elif (symObj.getSelectedKey()  == "128KB"):
        tcmSize.setValue("128 KB",2)
        tcmEnable.setValue(True,2)


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

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(True)
systickExternal.setVisible(False)

deviceBoot = coreComponent.createKeyValueSetSymbol("DEVICE_BOOT", devCfgMenu)
deviceBoot.setLabel("Boot Mode")
deviceBoot.setOutputMode("Key")
deviceBoot.setDisplayMode("Description")
deviceBoot.addKey("CLEAR", "0", "Boot from ROM")
deviceBoot.addKey("SET", "1", "Boot from Flash")
deviceBoot.setSelectedKey("SET",1)

deviceTCMsize = coreComponent.createKeyValueSetSymbol("DEVICE_TCM_SIZE", devCfgMenu)
deviceTCMsize.setLabel("TCM Size")
deviceTCMsize.setOutputMode("Value")
deviceTCMsize.setDisplayMode("Description")
deviceTCMsize.addKey("0KB", "0", "DTCM: 0KB, ITCM: 0KB" )
deviceTCMsize.addKey("32KB", "1", "DTCM: 32KB, ITCM: 32KB")
deviceTCMsize.addKey("64KB", "2", "DTCM: 64 KB, ITCM: 64KB")
deviceTCMsize.addKey("128KB", "3", "DTCM: 128 KB,  ITCM: 128KB")
deviceTCMsize.setSelectedKey("0KB",1)

coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("CORTEX-M7")
coreArch.setReadOnly(True)
coreArch.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_E70_S70_V70_V71")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M7 Configuration")
cortexMenu.setDescription("Configuration for Cortex M7")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_e70/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_e70/plugin/clockmanager.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/SAME70pinmanager.jar")
# Cortex-M7 IP Configuration
tcmMenu = coreComponent.createMenuSymbol("TCM_MENU", cortexMenu)
tcmMenu.setLabel("TCM")
tcmMenu.setDescription("TCM Configuration")

tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", tcmMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(False)
tcmEnable.setVisible(False)

tcmSize = coreComponent.createStringSymbol("TCM_SIZE", tcmMenu)
tcmSize.setLabel("TCM Size Selected through configuration Fuse")
tcmSize.setDefaultValue("0 KB")
tcmSize.setReadOnly(True)
tcmSize.setDependencies(setTcmSize, ["DEVICE_TCM_SIZE"])

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", tcmMenu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(True)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)


# load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic_m7/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic_m7/plugin/ARM_M7_NVICmanager.jar")

#load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/MPUmanager.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load rswdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/rswdt_11110/config/rswdt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

# load device specific adc manager information
coreComponent.addPlugin("../peripheral/afec_11147/plugin/ARM_M7_ADCmanager.jar")


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

# set XC32 ITCM Size
xc32ITCMSizeSym = coreComponent.createSettingSymbol("XC32_ITCM_SIZE", None)
xc32ITCMSizeSym.setCategory("C32Global")
xc32ITCMSizeSym.setKey("mitcm")
xc32ITCMSizeSym.setValue("")
xc32ITCMSizeSym.setDependencies(xc32SetTcmSize, ["DEVICE_TCM_SIZE"])

# set XC32 DTCM Size
xc32DTCMSizeSym = coreComponent.createSettingSymbol("XC32_DTCM_SIZE", None)
xc32DTCMSizeSym.setCategory("C32Global")
xc32DTCMSizeSym.setKey("mdtcm")
xc32DTCMSizeSym.setValue("")
xc32DTCMSizeSym.setDependencies(xc32SetTcmSize, ["DEVICE_TCM_SIZE"])

# set XC32 Stack in TCM: True or False
xc32StackInTCMSym = coreComponent.createSettingSymbol("XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(xc32SetStackInTcm, ["STACK_IN_TCM"])

#devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
#devconSystemInitFile.setType("STRING")
#devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
#devconSystemInitFile.setSourcePath("arm/templates/SAM_E70_S70_V70_V71.c.ftl")
#devconSystemInitFile.setMarkup(True)
