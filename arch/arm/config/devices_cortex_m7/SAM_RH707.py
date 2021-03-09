"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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


def xc32SetStackInTcm(symbol, event):
    if (event["value"]):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")


# Channel x Configuration Register[0..31] defaults
#"TYPE" "DSYNC" "SWREQ" "SAM" "DAM" "SIF" "DIF" "DWIDTH" "CSIZE" "MBSIZE"
def setXDMACDefaultSettings():
    triggerSettings = {"Software Trigger":  ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Transmit": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM",       "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Receive":  ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM",       "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    return triggerSettings


def setMPUDefaultSettings():
    mpuRegions = 16
    mpuSettings = {"ITCM":        ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00000000",   "4MB"],
                   "FLASH":       ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x10000000",   "1MB"],
                   "DTCM":        ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "1MB"],
                   "SRAM":        ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x21000000",   "1MB"],
                   "PERIPHERALS": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB"],
                   "HEMC":     ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x60000000",   "256MB"],
                   "QSPI":        ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x18000000",   "256MB"],
                   "USBHS_RAM":   ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xA0100000",   "1MB"],
                   "SYSTEM":      ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"]}
    mpuSetUpLogicList = ['ITCM', 'FLASH', 'DTCM', 'SRAM', 'HEMC', 'QSPI']

    return mpuRegions, mpuSettings, mpuSetUpLogicList


print ("Loading System Services for " + Variables.get("__PROCESSOR"))

# DEVICE & PROJECT CONFIGURATION MENU
deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAMRH")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(True)
systickExternal.setVisible(False)

tcmFixedSize = coreComponent.createBooleanSymbol("TCM_FIXED_SIZE", devCfgMenu)
tcmFixedSize.setLabel("TCM size is not configurable")
tcmFixedSize.setDefaultValue(True)
tcmFixedSize.setVisible(False)

deviceTCMsize = coreComponent.createIntegerSymbol("DEVICE_TCM_SIZE", devCfgMenu)
deviceTCMsize.setLabel("TCM Size")
deviceTCMsize.setDefaultValue(0)
deviceTCMsize.setReadOnly(True)
deviceTCMsize.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

# CORTEX-M7 CONFIGURATION MENU
cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M7 Configuration")
cortexMenu.setDescription("Configuration for Cortex M7")

# TCM MENU
tcmMenu = coreComponent.createMenuSymbol("TCM_MENU", cortexMenu)
tcmMenu.setLabel("TCM")
tcmMenu.setDescription("TCM Configuration")

tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", tcmMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(True)
tcmEnable.setVisible(True)

tcmEccEnable = coreComponent.createBooleanSymbol("TCM_ECC_ENABLE", tcmMenu)
tcmEccEnable.setLabel("Enable ECC for TCM")
tcmEccEnable.setDefaultValue(True)
tcmEccEnable.setVisible(True)

flexRamEccEnable = coreComponent.createBooleanSymbol("ECC_SUPPORTED", tcmMenu)
flexRamEccEnable.setDefaultValue(True)
flexRamEccEnable.setVisible(False)

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", xc32Menu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)

# CACHE MENU
cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(True)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

cacheAlign = coreComponent.createIntegerSymbol("CACHE_ALIGN", cacheMenu)
cacheAlign.setLabel("Cache Alignment Length")
cacheAlign.setVisible(False)
cacheAlign.setDefaultValue(32)

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_rh707/config/clk.py")
#coreComponent.addPlugin("../peripheral/clk_sam_rh707/plugin/clk_sam_rh707.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11264/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11264/plugin/pio_11264.jar")

# load matrix
execfile(Variables.get("__CORE_DIR") + "/../peripheral/matrix_44138/config/matrix.py")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# #load DWT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwt/config/dwt.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

# load ADC manager information
coreComponent.addPlugin("../peripheral/adc_44073/plugin/adc_44073.jar")

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
armSysStartSourceFile.setDependencies(genSysSourceFile, ["CoreSysStartupFile", "CoreSysFiles"])

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")
armLibCSourceFile.setDependencies(genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])

# set XC32 ITCM Size
xc32ITCMSizeSym = coreComponent.createSettingSymbol("XC32_ITCM_SIZE", None)
xc32ITCMSizeSym.setCategory("C32Global")
xc32ITCMSizeSym.setKey("mitcm")
xc32ITCMSizeSym.setValue("0x20000")

# set XC32 DTCM Size
xc32DTCMSizeSym = coreComponent.createSettingSymbol("XC32_DTCM_SIZE", None)
xc32DTCMSizeSym.setCategory("C32Global")
xc32DTCMSizeSym.setKey("mdtcm")
xc32DTCMSizeSym.setValue("0x40000")

# set XC32 Stack in TCM: True or False
xc32StackInTCMSym = coreComponent.createSettingSymbol("XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(xc32SetStackInTcm, ["STACK_IN_TCM"])

compilerSpecifics = [armSysStartSourceFile]

#Override default sizes for IAR stack and heap
iarUsrStackSize.setDefaultValue( 0x0400 )
iarHeapSize.setDefaultValue(0x0200)
