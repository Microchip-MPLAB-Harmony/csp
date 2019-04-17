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

global xc32StackInTCMSym
global xc32DTCMSizeSym
global xc32ITCMSizeSym
global tcmSize
global tcmEnable


def xc32SetTcmSize(symbol, event):
    symObj = event["symbol"]
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
    if (event["value"]):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")


def setTcmSize(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "0KB"):
        tcmSize.setValue("0 KB", 2)
        tcmEnable.setValue(False, 2)
    elif (symObj.getSelectedKey() == "32KB"):
        tcmSize.setValue("32 KB", 2)
        tcmEnable.setValue(True, 2)
    elif (symObj.getSelectedKey() == "64KB"):
        tcmSize.setValue("64 KB", 2)
        tcmEnable.setValue(True, 2)
    elif (symObj.getSelectedKey() == "128KB"):
        tcmSize.setValue("128 KB", 2)
        tcmEnable.setValue(True, 2)


def setXDMACDefaultSettings():
    triggerSettings = {"Software Trigger": ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Transmit": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Receive": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"],
                       "SSC_Transmit": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "HALFWORD", "CHK_1", "SINGLE"],
                       "SSC_Receive": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC0_Transmit_Left": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC0_Receive_Left": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC1_Transmit_Left": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC1_Receive_Left": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC0_Transmit_Right": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC0_Receive_Right": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC1_Transmit_Right": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "HALFWORD", "CHK_1", "SINGLE"],
                       "I2SC1_Receive_Right": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "HALFWORD", "CHK_1", "SINGLE"]}

    return triggerSettings


def setMPUDefaultSettings():
    mpuRegions = 16
    mpuSettings = {"ITCM": ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00000000",   "4MB"],
                   "FLASH": ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00400000",   "4MB"],
                   "DTCM": ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "4MB"],
                   "SRAM": ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20400000",   "8MB"],
                   "PERIPHERALS": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB"],
                   "EBI_SMC": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x60000000",   "256MB"],
                   "EBI_SDRAM": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x70000000",   "256MB"],
                   "QSPI": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x80000000",   "256MB"],
                   "USBHS_RAM": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xA0100000",   "1MB"],
                   "SYSTEM": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"]}
    mpuSetUpLogicList = ['ITCM', 'DTCM',
                         'SRAM', 'EBI_SMC', 'EBI_SDRAM', 'QSPI']

    return mpuRegions, mpuSettings, mpuSetUpLogicList


# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific configurations (fuses), temporary, to be removed once
# XC32 updated
devCfgComment = coreComponent.createCommentSymbol(
    "CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel(
    "Note: Set Device Configuration Bits via Programming Tool")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol(
    "DEVICE_SECURITY", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)")
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR", 1)

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol(
    "SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(True)
systickExternal.setVisible(False)

deviceBoot = coreComponent.createKeyValueSetSymbol("DEVICE_BOOT", devCfgMenu)
deviceBoot.setLabel("Boot Mode")
deviceBoot.setOutputMode("Key")
deviceBoot.setDisplayMode("Description")
deviceBoot.addKey("CLEAR", "0", "Boot from ROM")
deviceBoot.addKey("SET", "1", "Boot from Flash")
deviceBoot.setSelectedKey("SET", 1)

deviceTCMsize = coreComponent.createKeyValueSetSymbol(
    "DEVICE_TCM_SIZE", devCfgMenu)
deviceTCMsize.setLabel("TCM Size")
deviceTCMsize.setOutputMode("Value")
deviceTCMsize.setDisplayMode("Description")
deviceTCMsize.addKey("0KB", "0", "DTCM: 0KB, ITCM: 0KB")
deviceTCMsize.addKey("32KB", "1", "DTCM: 32KB, ITCM: 32KB")
deviceTCMsize.addKey("64KB", "2", "DTCM: 64 KB, ITCM: 64KB")
deviceTCMsize.addKey("128KB", "3", "DTCM: 128 KB,  ITCM: 128KB")
deviceTCMsize.setSelectedKey("0KB", 1)

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
execfile(Variables.get("__CORE_DIR")
         + "/../peripheral/clk_sam_e70/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_e70/plugin/clockmanager.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR")
         + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/pio_11004.jar")
# Cortex-M7 IP Configuration
tcmMenu = coreComponent.createMenuSymbol("TCM_MENU", cortexMenu)
tcmMenu.setLabel("TCM")
tcmMenu.setDescription("TCM Configuration")

tcmComment = coreComponent.createCommentSymbol("TCM_COMMENT", tcmMenu)
tcmComment.setLabel("Configure the TCM using the Device Configuration Fuse Setting")


tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", tcmMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(False)
tcmEnable.setVisible(False)

tcmSize = coreComponent.createStringSymbol("TCM_SIZE", tcmMenu)
tcmSize.setLabel("TCM Size Selected through configuration Fuse")
tcmSize.setDefaultValue("0 KB")
tcmSize.setVisible(False)
tcmSize.setDependencies(setTcmSize, ["DEVICE_TCM_SIZE"])

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", xc32Menu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

dcacheEnable = coreComponent.createBooleanSymbol(
    "DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(True)

icacheEnable = coreComponent.createBooleanSymbol(
    "INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

cacheAlign = coreComponent.createIntegerSymbol("CACHE_ALIGN", cacheMenu)
cacheAlign.setLabel("Cache Alignment Length")
cacheAlign.setVisible(False)
cacheAlign.setDefaultValue(32)

execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# load systick
execfile(Variables.get("__CORE_DIR")
         + "/../peripheral/systick/config/systick.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR")
         + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load rswdt
execfile(Variables.get("__CORE_DIR")
         + "/../peripheral/rswdt_11110/config/rswdt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

global armLibCSourceFile
global devconSystemInitFile
global compilerSpecifics

compilerSelected = compilerChoice.getSelectedKey().lower()

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("../arch/arm/templates/" + compilerSelected + "/cortex_m/startup/startup_" + compilerSelected + ".c.ftl")
armSysStartSourceFile.setOutputName("startup_" + compilerSelected + ".c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setDependencies(
    genSysSourceFile, ["CoreSysStartupFile", "CoreSysFiles"])

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")
armLibCSourceFile.setDependencies(
    genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])

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
xc32StackInTCMSym = coreComponent.createSettingSymbol(
    "XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(xc32SetStackInTcm, ["STACK_IN_TCM"])

devconSystemInitFile = coreComponent.createFileSymbol(
    "DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName(
    "core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_E70_S70_V70_V71.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]
