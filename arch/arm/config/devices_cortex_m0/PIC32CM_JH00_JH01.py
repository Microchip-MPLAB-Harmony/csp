# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

def udpateSymbolEnableAndVisibility (symbol, event):
    symbol.setVisible(event["symbol"].getSelectedKey() == "XC32")

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY_CMD", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)")
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)
deviceSecurity.setVisible(compilerChoice.getSelectedKey() == "XC32")
deviceSecurity.setDependencies(udpateSymbolEnableAndVisibility, ['core.COMPILER_CHOICE'])

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", devCfgMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)

# NVMCTRL fuse configuration
nvmctrlFuseMenu = coreComponent.createMenuSymbol("DEVICE_NVMCTRL_FUSE_CONFIG", fuseSettings)
nvmctrlFuseMenu.setLabel("NVMCTRL Fuse Configuration")

def getMaxValue(mask):
    if mask == 0 :
        return hex(0)

    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1

    return mask

registerGroup = "USER_FUSES"
registerNames = ["USER_WORD_0", "USER_WORD_1"]

#TO:DO Set Default fuse values once device arrives
default = [0x0,
           0x8,
           0x0,
           0x1,
           0x0,
           0x0,
           0xB,
           0xB,
           0xB,
           0x0,
           0x0,
           0xFFFF
           ]
numfuses = 0

for i in range(0, len(registerNames)):
    path = "/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"" + registerGroup + "\"]/register@[name=\"" + registerNames[i] + "\"]"
    fuseNode = ATDF.getNode(path)
    fuseNodeValues = fuseNode.getChildren()
    for index in range(0, len(fuseNodeValues)):
        key = fuseNodeValues[index].getAttribute("name")
        caption=fuseNodeValues[index].getAttribute("caption")
        valueGroup = fuseNodeValues[index].getAttribute("values")
        stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
        stringSymbol.setDefaultValue(key)
        stringSymbol.setVisible(False)
        if valueGroup == None:
            mask = fuseNodeValues[index].getAttribute("mask")
            count = bin((int(mask, 16))).count("1")
            if count == 1:
                keyValueSymbol = coreComponent.createKeyValueSetSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                keyValueSymbol.setLabel(caption)
                keyValueSymbol.addKey("CLEAR", "0", "CLEAR")
                keyValueSymbol.addKey("SET", "1", "SET")
                keyValueSymbol.setDefaultValue(default[numfuses])
                keyValueSymbol.setOutputMode("Key")
                keyValueSymbol.setDisplayMode("Description")
            else:
                hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                hexSymbol.setLabel(caption)
                hexSymbol.setMin(0)
                hexSymbol.setMax(getMaxValue(mask))
                hexSymbol.setDefaultValue(default[numfuses])
        else:
            valueGroupPath = "/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/value-group@[name=\"" + valueGroup + "\"]"
            valueGroupNode = ATDF.getNode(valueGroupPath)
            valueGroupChildren = valueGroupNode.getChildren()
            keyValueSymbol = coreComponent.createKeyValueSetSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
            keyValueSymbol.setLabel(caption)
            for j in range(0, len(valueGroupChildren)):
                name = valueGroupChildren[j].getAttribute("name")
                value = valueGroupChildren[j].getAttribute("value")
                caption = valueGroupChildren[j].getAttribute("caption")
                keyValueSymbol.addKey(name, value, caption)
            keyValueSymbol.setDefaultValue(default[numfuses])
            keyValueSymbol.setOutputMode("Key")
            keyValueSymbol.setDisplayMode("Description")
        numfuses = numfuses + 1

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CM_JH00_JH01")
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

# # load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

ram_start = 0
ram_size = 0

ramInit = coreComponent.createBooleanSymbol("RAM_INIT", xc32Menu)
ramInit.setDefaultValue(True)
ramInit.setVisible(True)

addr_space = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space").getChildren()
for mem_idx in range(0, len(addr_space_children)):
    if addr_space_children[mem_idx].getAttribute("type") == "ram":
        ram_start   = addr_space_children[mem_idx].getAttribute("start")
        ram_size    = addr_space_children[mem_idx].getAttribute("size")

ramStart = coreComponent.createStringSymbol("RAM_START", xc32Menu)
ramStart.setDefaultValue(ram_start)
ramStart.setVisible(False)

ramLength = coreComponent.createStringSymbol("RAM_LENGTH", xc32Menu)
ramLength.setDefaultValue(ram_size)
ramLength.setVisible(False)


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
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/PIC32CM_JH00_JH01.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]
iarUsrStackSize.setDefaultValue(0x400)
iarHeapSize.setDefaultValue(0x0)
