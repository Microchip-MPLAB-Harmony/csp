# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

def update_cache(symbol, event):
    if event["value"] == 0:
        symbol.setReadOnly(True)
        symbol.setValue(False)
    else:
        symbol.setReadOnly(False)
        symbol.clearValue()


def set_startup_file(symbol,event):
    compilerSelected = event["symbol"].getSelectedKey().lower()
    symbol.setSourcePath("../arch/arm/templates/{0}/cortex_m/startup/"
                         "startup_{0}.c.ftl".format(compilerSelected))
    symbol.setOutputName("startup_" + compilerSelected + ".c")


# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# productFamily (ID = "PRODUCT_FAMILY") symbol should be used everywhere to
# identify the product family.This symbol is created inside core.py with the
# default value obtained from ATDF. Since some of the ATDF doesn't give
# uniquely identifiable family name, same is updated in family python like this

global productFamily
productFamily.setDefaultValue("PIC32CX_MT")

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK",
                                                                    devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(True)
systickExternal.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CX_MT")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M4 Configuration")
cortexMenu.setDescription("Configuration for Cortex M4")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", None)
cacheMenu.setLabel("CMCC Configuration")
cacheMenu.setDescription("CACHE Configuration")

deviceITCMsize = coreComponent.createKeyValueSetSymbol("DEVICE_ITCM_SIZE", cacheMenu)
deviceITCMsize.setLabel("ITCM and ICache Size")
deviceITCMsize.setOutputMode("Value")
deviceITCMsize.setDisplayMode("Description")
deviceITCMsize.addKey("16KB", "0", "TCM: 16 KB, Cache: 0 KB")
deviceITCMsize.addKey("14KB", "1", "TCM: 14 KB, Cache: 2 KB")
deviceITCMsize.addKey("12KB", "2", "TCM: 12 KB, Cache: 4 KB")
deviceITCMsize.addKey("8KB", "3", "TCM: 8 KB, Cache: 8 KB")
deviceITCMsize.addKey("0KB", "4", "TCM: 0 KB, Cache: 16 KB")
deviceITCMsize.setDefaultValue(4)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDependencies(update_cache, ["DEVICE_ITCM_SIZE"])
icacheEnable.setDefaultValue(True)

deviceDTCMsize = coreComponent.createKeyValueSetSymbol("DEVICE_DTCM_SIZE", cacheMenu)
deviceDTCMsize.setLabel("DTCM and DCache Size")
deviceDTCMsize.setOutputMode("Value")
deviceDTCMsize.setDisplayMode("Description")
deviceDTCMsize.addKey("8KB", "0", "TCM: 8 KB, Cache: 0 KB")
deviceDTCMsize.addKey("14KB", "1", "TCM: 6 KB, Cache: 2 KB")
deviceDTCMsize.addKey("12KB", "2", "TCM: 4 KB, Cache: 4 KB")
deviceDTCMsize.addKey("0KB", "3", "TCM: 0 KB, Cache: 8 KB")

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setReadOnly(True)
dcacheEnable.setDependencies(update_cache, ["DEVICE_DTCM_SIZE"])

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", cacheMenu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)
stackTCM.setVisible(False)

def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"         : ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x01000000",   "2MB"   ],
                    "SRAM"         : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "512KB"],
                    "PERIPHERALS"  : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                    "SYSTEM"       : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ],
                    "QSPI"         : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x04000000",   "256MB"],}
    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM", "QSPI"]
    return mpuRegions, mpuSettings, mpuSetUpLogicList

#Load DWDT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwdt_04686/config/dwdt.py")

# Load Clock
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32cx_mt/config/clk.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "CLOCK_UI_MANAGER_ID_PIC32CX_MT", {"plugin_name": "Clock Manager", "main_html_path": "../csp/peripheral/clk_pic32cx_mt/plugins/pic32cxmt_clock_manager/build/index.html"})

#Load RSTC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/rstc_04678/config/rstc.py")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# #load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# #  load CMCC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/cmcc_11108/config/cmcc.py")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11264/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11264/plugin/pio_11264.jar")

periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SEFC\"]")
modules = periphNode.getChildren()
components = []
for sefc_instance in range (0, len(modules)):
    components.append(str(modules[sefc_instance].getAttribute("name")).lower())
Database.activateComponents(components)

compilerSelected = compilerChoice.getSelectedKey().lower()

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath(("../arch/arm/templates/{0}/cortex_m/" +
        "startup/startup_{0}.c.ftl").format(compilerSelected))
armSysStartSourceFile.setOutputName("startup_" + compilerSelected + ".c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setDependencies(set_startup_file, [compilerChoice.getID()])

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")
armLibCSourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(
        event["symbol"].getSelectedKey()=="XC32"), [compilerChoice.getID()])
armLibCSourceFile.setEnabled(compilerSelected == "xc32")

# set XC32 Stack in TCM: True or False
xc32StackInTCMSym = coreComponent.createSettingSymbol(
    "XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(lambda symbol, event: symbol.setValue(
                                        event["value"]), ["STACK_IN_TCM"])
