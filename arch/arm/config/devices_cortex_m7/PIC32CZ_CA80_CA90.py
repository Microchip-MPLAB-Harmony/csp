# coding: utf-8
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
global tcmEnable

def xc32SetStackInTcm(symbol, event):
    if (event["value"]):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")

def setDMADefaultSettings():
    triggerSettings = {"Software Trigger": ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Transmit": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Receive": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    return triggerSettings

def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"ITCM": ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00000000",   "128KB"],
                   "FCR_BFM": ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x8000000",   "1MB"],
                   "FCR_PFM": ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0xC000000",   "8MB"],
                   "DTCM": ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "128KB"],
                   "SRAM": ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20020000",   "1MB"],
                   "PERIPHERALS": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB"],
                   "EBI_SMC": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x60000000",   "256MB"],
                   "HSM": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x4F018000",   "1MB"],
                   "SQI": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x80000000",   "256MB"],
                   "USBHS_RAM": ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x4F010000",   "1MB"],
                   "PPB": ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "512MB"]}
    mpuSetUpLogicList = ['ITCM', 'DTCM',
                         'SRAM', 'EBI_SMC', 'HSM', 'SQI']

    return mpuRegions, mpuSettings, mpuSetUpLogicList

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", devCfgMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(False)

default = [0x1, 0xFFFE, 0xFFFF , 0xFFFF, 0, 1 , 1, 0, 0, 0, 0, 0xFF, 0xFF, 0xFF, 0xFF, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0xF, 0xF, 0xF, 0xF, 0x3, 1, 1, 0, 0, 0, 0, 1, 1, 0xFFFFFFFF, 0xFFFFFFFF]
numfuses = 0
fuseRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + "FUSES_USERCFG1" + "\"]")
registerNames = fuseRegisterGroup.getChildren()
for i in range(0, len(registerNames)):
    fuseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"FUSES_USERCFG1\"]/register@[name=\"" + registerNames[i].getAttribute("name") + "\"]")
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
                keyValueSymbol.addKey(name, str(value), caption)
            keyValueSymbol.setDefaultValue(default[numfuses])
            keyValueSymbol.setOutputMode("Key")
            keyValueSymbol.setDisplayMode("Description")
        numfuses = numfuses + 1

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol(
    "SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

deviceTCMsize = coreComponent.createIntegerSymbol("DEVICE_TCM_SIZE", devCfgMenu)
deviceTCMsize.setLabel("TCM Size")
deviceTCMsize.setDefaultValue(0)
deviceTCMsize.setReadOnly(True)
deviceTCMsize.setVisible(False)

tcmFixedSize = coreComponent.createBooleanSymbol("TCM_FIXED_SIZE", devCfgMenu)
tcmFixedSize.setLabel("TCM size is not configurable")
tcmFixedSize.setDefaultValue(True)
tcmFixedSize.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CZ_CA80_CA90")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M7 Configuration")
cortexMenu.setDescription("Configuration for Cortex M7")

global nvmWaitStates
nvmWaitStates = { #VDD > 2.7
                    23000000 : 0,
                    46000000 : 1,
                    69000000 : 2,
                    92000000 : 3,
                    115000000 : 4,
                    138000000 : 5,
                    150000000 : 6,
                    300000000 : 7
                }

#periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"FCR\"]")
#modules = periphNode.getChildren()
#components = []
#for nvmctrl_instance in range (0, len(modules)):
#    components.append(str(modules[nvmctrl_instance].getAttribute("name")).lower())
#Database.activateComponents(components)

#periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"FCW\"]")
#modules = periphNode.getChildren()
#components = []
#for nvmctrl_instance in range (0, len(modules)):
#    components.append(str(modules[nvmctrl_instance].getAttribute("name")).lower())
#Database.activateComponents(components)

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
coreComponent.addPlugin("../peripheral/port_u2210/plugin/port_u2210.jar")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32cz_ca/config/clk.py")
#coreComponent.addPlugin("../peripheral/clk_pic32cz_ca/plugin/clockmanager.jar")

# Cortex-M7 IP Configuration
tcmMenu = coreComponent.createMenuSymbol("TCM_MENU", cortexMenu)
tcmMenu.setLabel("TCM")
tcmMenu.setDescription("TCM Configuration")

tcmComment = coreComponent.createCommentSymbol("TCM_COMMENT", tcmMenu)
tcmComment.setLabel("Configure the TCM using the Device Configuration Fuse Setting")

tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", tcmMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(True)
tcmEnable.setVisible(False)

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", xc32Menu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)

ramInit = coreComponent.createBooleanSymbol("RAM_INIT", xc32Menu)
ramInit.setDefaultValue(True)
ramInit.setVisible(False)

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

# #load DWT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwt/config/dwt.py")

# load dma manager information
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/dma_03639/config/dma.py")
#coreComponent.addPlugin("../peripheral/dma_03639/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

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

# set XC32 Stack in TCM: True or False
xc32StackInTCMSym = coreComponent.createSettingSymbol(
    "XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(xc32SetStackInTcm, ["STACK_IN_TCM"])

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/PIC32CZ_CA.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]

#Override default sizes for IAR stack and heap
iarUsrStackSize.setDefaultValue(0x0400)
iarHeapSize.setDefaultValue(0x0200)
