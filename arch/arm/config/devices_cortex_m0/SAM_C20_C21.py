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
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)")
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)
deviceSecurity.setVisible(False)

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", devCfgMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)

# NVMCTRL fuse configuration
nvmctrlFuseMenu = coreComponent.createMenuSymbol("DEVICE_NVMCTRL_FUSE_CONFIG", fuseSettings)
nvmctrlFuseMenu.setLabel("NVMCTRL Fuse Configuration")

nvmctrlBootloaderSize = coreComponent.createKeyValueSetSymbol("DEVICE_NVMCTRL_BOOTPROT", nvmctrlFuseMenu)
nvmctrlBootloaderSize.setLabel("Bootloader Size")

nvmctrlBootloaderSize_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"USER_FUSES_NVMCTRL__BOOTPROT\"]")
nvmctrlBootloaderSize_Values = []
nvmctrlBootloaderSize_Values = nvmctrlBootloaderSize_Node.getChildren()

for index in range(len(nvmctrlBootloaderSize_Values)):
    nvmctrlBootloaderSize_Key_Name = nvmctrlBootloaderSize_Values[index].getAttribute("name")
    nvmctrlBootloaderSize_Key_Description = nvmctrlBootloaderSize_Values[index].getAttribute("caption")
    nvmctrlBootloaderSize_Key_Value = nvmctrlBootloaderSize_Values[index].getAttribute("value")

    if nvmctrlBootloaderSize_Key_Name[-1:] == "K":
        nvmctrlBootloaderSize_Key_Name = str(int(nvmctrlBootloaderSize_Key_Name[:-1]) * 1024)

    nvmctrlBootloaderSize.addKey(nvmctrlBootloaderSize_Key_Name, nvmctrlBootloaderSize_Key_Value, nvmctrlBootloaderSize_Key_Description)

nvmctrlBootloaderSize.setDefaultValue(0)
nvmctrlBootloaderSize.setOutputMode("Key")
nvmctrlBootloaderSize.setDisplayMode("Description")

nvmctrlEEPROMSize = coreComponent.createKeyValueSetSymbol("DEVICE_NVMCTRL_EEPROM_SIZE", nvmctrlFuseMenu)
nvmctrlEEPROMSize.setLabel("EEPROM Size")

nvmctrlEEPROMSize_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"USER_FUSES_NVMCTRL__EEPROM_SIZE\"]")
nvmctrlEEPROMSize_Values = []
nvmctrlEEPROMSize_Values = nvmctrlEEPROMSize_Node.getChildren()

for index in range(len(nvmctrlEEPROMSize_Values)):
    nvmctrlEEPROMSize_Key_Name = nvmctrlEEPROMSize_Values[index].getAttribute("name")
    nvmctrlEEPROMSize_Key_Description = nvmctrlEEPROMSize_Values[index].getAttribute("caption")
    nvmctrlEEPROMSize_Key_Value = nvmctrlEEPROMSize_Values[index].getAttribute("value")

    if nvmctrlEEPROMSize_Key_Name[-1:] == "K":
        nvmctrlEEPROMSize_Key_Name = str(int(nvmctrlEEPROMSize_Key_Name[:-1]) * 1024)

    nvmctrlEEPROMSize.addKey(nvmctrlEEPROMSize_Key_Name, nvmctrlEEPROMSize_Key_Value, nvmctrlEEPROMSize_Key_Description)

nvmctrlEEPROMSize.setDefaultValue(0)
nvmctrlEEPROMSize.setOutputMode("Key")
nvmctrlEEPROMSize.setDisplayMode("Description")

nvmctrlRegionLock = coreComponent.createHexSymbol("DEVICE_NVMCTRL_REGION_LOCK", nvmctrlFuseMenu)
nvmctrlRegionLock.setLabel("NVM Region Lock Bits")
nvmctrlRegionLock.setDefaultValue(0xFFFF)
nvmctrlRegionLock.setMax(0xFFFF)
nvmctrlRegionLock.setMin(0x0)

# BODVDD fuse configuration
bodvddFuseMenu = coreComponent.createMenuSymbol("DEVICE_BODVDD_FUSE_CONFIG", fuseSettings)
bodvddFuseMenu.setLabel("BODVDD Fuse Configuration")

bodvddEnable = coreComponent.createKeyValueSetSymbol("DEVICE_BODVDD_DISABLE", bodvddFuseMenu)
bodvddEnable.setLabel("BODVDD Disable")
bodvddEnable.setOutputMode("Key")
bodvddEnable.setDisplayMode("Description")
bodvddEnable.addKey("DISABLED", "0", "BODVDD is disabled")
bodvddEnable.addKey("ENABLED", "1", "BODVDD is enabled")
bodvddEnable.setSelectedKey("DISABLED", 1)

bodvddAction = coreComponent.createKeyValueSetSymbol("DEVICE_BODVDD_ACTION", bodvddFuseMenu)
bodvddAction.setLabel("BODVDD Action")

bodvddAction_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"SUPC_BODVDD__ACTION\"]")
bodvddAction_Values = []
bodvddAction_Values = bodvddAction_Node.getChildren()

for index in range(len(bodvddAction_Values)):
    bodvddAction_Key_Name = bodvddAction_Values[index].getAttribute("name")
    bodvddAction_Key_Description = bodvddAction_Values[index].getAttribute("caption")
    bodvddAction_Key_Value = bodvddAction_Values[index].getAttribute("value")
    bodvddAction.addKey(bodvddAction_Key_Name, bodvddAction_Key_Value, bodvddAction_Key_Description)

bodvddAction.setDefaultValue(0)
bodvddAction.setOutputMode("Key")
bodvddAction.setDisplayMode("Description")

bodvddHysterisis = coreComponent.createKeyValueSetSymbol("DEVICE_BODVDD_HYST", bodvddFuseMenu)
bodvddHysterisis.setLabel("BODVDD Hysterisis")
bodvddHysterisis.setOutputMode("Key")
bodvddHysterisis.setDisplayMode("Description")
bodvddHysterisis.addKey("DISABLED", "0", "No hysterisis")
bodvddHysterisis.addKey("ENABLED", "1", "Hysterisis enabled")
bodvddHysterisis.setSelectedKey("DISABLED", 1)

bodvddUserLevel = coreComponent.createHexSymbol("DEVICE_BODVDDUSERLEVEL", bodvddFuseMenu)
bodvddUserLevel.setLabel("BODVDD User Level")
bodvddUserLevel.setDefaultValue(0x8)
bodvddUserLevel.setMax(0x3F)
bodvddUserLevel.setMin(0x0)

# WDT fuse configuration
wdtFuseMenu = coreComponent.createMenuSymbol("DEVICE_WDT_FUSE_CONFIG", fuseSettings)
wdtFuseMenu.setLabel("WDT Fuse Configuration")

wdtEnable = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_ENABLE", wdtFuseMenu)
wdtEnable.setLabel("WDT Enable")
wdtEnable.setOutputMode("Key")
wdtEnable.setDisplayMode("Description")
wdtEnable.addKey("DISABLED", "0", "WDT is disabled")
wdtEnable.addKey("ENABLED", "1", "WDT is enabled")
wdtEnable.setSelectedKey("DISABLED", 1)

wdtAlwaysOn = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_ALWAYSON", wdtFuseMenu)
wdtAlwaysOn.setLabel("WDT Always On")
wdtAlwaysOn.setOutputMode("Key")
wdtAlwaysOn.setDisplayMode("Description")
wdtAlwaysOn.addKey("DISABLED", "0", "WDT is disabled")
wdtAlwaysOn.addKey("ENABLED", "1", "WDT is enabled and disabled through ENABLE bit")
wdtAlwaysOn.setSelectedKey("DISABLED", 1)

wdtPeriod = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_PER", wdtFuseMenu)
wdtPeriod.setLabel("WDT Period")

wdtPeriod_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"WDT_CONFIG__PER\"]")
wdtPeriod_Values = []
wdtPeriod_Values = wdtPeriod_Node.getChildren()

for index in range(len(wdtPeriod_Values)):
    wdtPeriod_Key_Name = wdtPeriod_Values[index].getAttribute("name")
    wdtPeriod_Key_Description = wdtPeriod_Values[index].getAttribute("caption")
    wdtPeriod_Key_Value = wdtPeriod_Values[index].getAttribute("value")
    wdtPeriod.addKey(wdtPeriod_Key_Name, wdtPeriod_Key_Value, wdtPeriod_Key_Description)

wdtPeriod.setDefaultValue(0)
wdtPeriod.setOutputMode("Key")
wdtPeriod.setDisplayMode("Description")

wdtWindowModeEnable = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_WEN", wdtFuseMenu)
wdtWindowModeEnable.setLabel("WDT Window Mode Enable")
wdtWindowModeEnable.setOutputMode("Key")
wdtWindowModeEnable.setDisplayMode("Description")
wdtWindowModeEnable.addKey("DISABLED", "0", "WDT window mode is disabled")
wdtWindowModeEnable.addKey("ENABLED", "1", "WDT window mode is enabled")
wdtWindowModeEnable.setSelectedKey("DISABLED", 1)

wdtWindowTimeOutPeriod = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_WINDOW", wdtFuseMenu)
wdtWindowTimeOutPeriod.setLabel("WDT Window Time-Out Period")

wdtWindowTimeOutPeriod_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"WDT_CONFIG__WINDOW\"]")
wdtWindowTimeOutPeriod_Values = []
wdtWindowTimeOutPeriod_Values = wdtWindowTimeOutPeriod_Node.getChildren()

for index in range(len(wdtWindowTimeOutPeriod_Values)):
    wdtWindowTimeOutPeriod_Key_Name = wdtWindowTimeOutPeriod_Values[index].getAttribute("name")
    wdtWindowTimeOutPeriod_Key_Description = wdtWindowTimeOutPeriod_Values[index].getAttribute("caption")
    wdtWindowTimeOutPeriod_Key_Value = wdtWindowTimeOutPeriod_Values[index].getAttribute("value")
    wdtWindowTimeOutPeriod.addKey(wdtWindowTimeOutPeriod_Key_Name, wdtWindowTimeOutPeriod_Key_Value, wdtWindowTimeOutPeriod_Key_Description)

wdtWindowTimeOutPeriod.setDefaultValue(0)
wdtWindowTimeOutPeriod.setOutputMode("Key")
wdtWindowTimeOutPeriod.setDisplayMode("Description")

wdtEarlyWarningOffset = coreComponent.createKeyValueSetSymbol("DEVICE_WDT_EWOFFSET", wdtFuseMenu)
wdtEarlyWarningOffset.setLabel("WDT Early Warning Offset")

wdtEarlyWarningOffset_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/value-group@[name=\"WDT_EWCTRL__EWOFFSET\"]")
wdtEarlyWarningOffset_Values = []
wdtEarlyWarningOffset_Values = wdtEarlyWarningOffset_Node.getChildren()

for index in range(len(wdtEarlyWarningOffset_Values)):
    wdtEarlyWarningOffset_Key_Name = wdtEarlyWarningOffset_Values[index].getAttribute("name")
    wdtEarlyWarningOffset_Key_Description = wdtEarlyWarningOffset_Values[index].getAttribute("caption")
    wdtEarlyWarningOffset_Key_Value = wdtEarlyWarningOffset_Values[index].getAttribute("value")
    wdtEarlyWarningOffset.addKey(wdtEarlyWarningOffset_Key_Name, wdtEarlyWarningOffset_Key_Value, wdtEarlyWarningOffset_Key_Description)

wdtEarlyWarningOffset.setDefaultValue(0)
wdtEarlyWarningOffset.setOutputMode("Key")
wdtEarlyWarningOffset.setDisplayMode("Description")

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_C20_C21")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M0+ Configuration")
cortexMenu.setDescription("Configuration for Cortex M0+")

def setDMACDefaultSettings():

    triggerSettings = {
                        "Software Trigger"  : ["BLOCK", "INCREMENTED_AM", "INCREMENTED_AM", "WORD"],
                        "Standard_Transmit" : ["BEAT", "INCREMENTED_AM", "FIXED_AM", "BYTE"],
                        "Standard_Receive"  : ["BEAT", "FIXED_AM", "INCREMENTED_AM", "BYTE"]
                    }

    return triggerSettings


def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"              : ["MPU_ATTR_NORMAL_WT",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00000000",   "4MB"   ],
                    "RWW"               : ["MPU_ATTR_NORMAL_WT",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00400000",   "4MB"   ],
                    "SRAM"              : ["MPU_ATTR_NORMAL_WT",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x20000000",   "4MB"   ],
                    "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                    "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ]}
    mpuSetUpLogicList = ["FLASH", "RWW", "SRAM", "PERIPHERALS", "SYSTEM"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

global nvmWaitStates
nvmWaitStates = { #VDD > 2.7
                    19000000 : 0,
                    38000000 : 1,
                    48000000 : 2
                }
                
periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVMCTRL\"]")
modules = periphNode.getChildren()
components = []
for nvmctrl_instance in range (0, len(modules)):
    components.append(str(modules[nvmctrl_instance].getAttribute("name")).lower())
Database.activateComponents(components)

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
coreComponent.addPlugin("../peripheral/port_u2210/plugin/port_u2210.jar")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_c20_c21/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_c20_c21/plugin/clk_sam_c20_c21.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2223/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_u2223/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

# Activate Event System
periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EVSYS\"]")
modules = periphNode.getChildren()
components = []
for evsys_instance in range (0, len(modules)):
    components.append(str(modules[evsys_instance].getAttribute("name")).lower())
Database.activateComponents(components)

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
armLibCSourceFile.setDependencies(genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_C20_C21.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]
