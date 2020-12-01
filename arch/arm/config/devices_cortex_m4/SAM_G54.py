# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", devCfgMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)

# load device specific configurations (fuses), temporary, to be removed once
# XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", fuseSettings)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY", fuseSettings)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)")
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR", 1)

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(True)
systickExternal.setVisible(False)

deviceBoot = coreComponent.createKeyValueSetSymbol("DEVICE_BOOT", fuseSettings)
deviceBoot.setLabel("Boot Mode")
deviceBoot.setOutputMode("Key")
deviceBoot.setDisplayMode("Description")
deviceBoot.addKey("CLEAR", "0", "Boot from ROM")
deviceBoot.addKey("SET", "1", "Boot from Flash")
deviceBoot.setSelectedKey("SET", 1)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_G54")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M4 Configuration")
cortexMenu.setDescription("Configuration for Cortex M4")

def setMPUDefaultSettings():

    mpuRegions = 8

    mpuSettings = {
                    "FLASH": ["MPU_ATTR_NORMAL_WT",         "MPU_RASR_AP_READWRITE_Val",    "",     "",   "0x00400000",  "2MB"],
                    "SRAM": ["MPU_ATTR_NORMAL_WB_WA",       "MPU_RASR_AP_READWRITE_Val",    "True", "",   "0x20000000",  "2MB"],
                    "PERIPHERALS": ["MPU_ATTR_DEVICE",      "MPU_RASR_AP_READWRITE_Val",    "",     "",   "0x40000000",  "256MB"],
                    "SYSTEM": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",     "",   "0xE0000000",  "1MB"],
                    "UHP_DPRAM": ["MPU_ATTR_DEVICE",        "MPU_RASR_AP_READWRITE_Val",    "",     "",   "0x20400000",  "1MB"],
                   }

    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM", "UHP_DPRAM"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList

global nvmWaitStates

nvmWaitStates = {

    # VDD > 1.6
    12500000: 0,
    25000000: 1,
    38000000: 2,
    51000000: 3,
    64000000: 4,
    76000000: 5,
    88000000: 6,
    96000000: 7
}

# SYSIO Pin configuration information (Required by PIO 11104)
global getArchSYSIOInformation

def getArchSYSIOInformation():

    matrixName = "MATRIX"
    sysioRegName = "CCFG_SYSIO"
    sysioInfoDict = {}

    #SYSIO information Dictionary is of the format {"SIGNAL_PAD":["FUNCTION_NAME":"SYSIO_MASK"]}
    sysioInfoDict["PA21"] = ["UHP_DM", 0x00000400]
    sysioInfoDict["PA22"] = ["UHP_DP", 0x00000800]
    sysioInfoDict["PB4"] = ["ICE_TDI", 0x00000010]
    sysioInfoDict["PB5"] = ["ICE_TDO/TRACESWO", 0x00000020]
    sysioInfoDict["PB6"] = ["ICE_TMS/SWDIO", 0x00000040]
    sysioInfoDict["PB7"] = ["ICE_TCK/SWDCLK", 0x00000080]
    sysioInfoDict["PB12"] = ["EFC_ERASE", 0x00001000]

    return matrixName, sysioRegName, sysioInfoDict

periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EFC\"]")
modules = periphNode.getChildren()
components = []
for nvmctrl_instance in range(0, len(modules)):
    components.append(str(modules[nvmctrl_instance].getAttribute("name")).lower())
Database.activateComponents(components)

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/pio_11004.jar")

# # load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_g51_g53_g54/config/clock.py")
coreComponent.addPlugin("../peripheral/clk_sam_g51_g53_g54/plugin/clockmanager.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# #load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# #load DWT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwt/config/dwt.py")

# # load wdt
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

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_G55.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]

#Override default sizes for IAR stack and heap
iarUsrStackSize.setDefaultValue(0x1000)
iarHeapSize.setDefaultValue(0x2000)
