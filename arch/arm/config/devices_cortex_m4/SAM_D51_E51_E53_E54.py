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
global fuseMenu

# ///////////////////////Symbol Creation for Fuses ////////////////////////// #
def getMaxValue(mask):
    if mask == 0 :
        return hex(0)

    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1

    return mask

def xc32SetTcmSize(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "0KB"):
        xc32DTCMSizeSym.setValue("")
        xc32ITCMSizeSym.setValue("")
    elif (symObj.getSelectedKey() == "2KB"):
        xc32DTCMSizeSym.setValue("0x800")
        xc32ITCMSizeSym.setValue("0x800")
    elif (symObj.getSelectedKey() == "3KB"):
        xc32DTCMSizeSym.setValue("0xC00")
        xc32ITCMSizeSym.setValue("0xC00")
    elif (symObj.getSelectedKey() == "4KB"):
        xc32DTCMSizeSym.setValue("0x1000")
        xc32ITCMSizeSym.setValue("0x1000")

def xc32SetStackInTcm(symbol, event):
    if (event["value"] == True):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")

def udpateSymbolEnableAndVisibility (symbol, event):
    symbol.setVisible(event["symbol"].getSelectedKey() == "XC32")

def calculateRAMLength(symbol, event):
    if event["value"] == 0:
        RAMSize = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"HSRAM\"]").getAttribute("size")
        symbol.setValue("RAM_LENGTH=" + str(hex(int(RAMSize, 16) / 2)))
    else:
        symbol.setValue("")

# load family specific configurations
Log.writeInfoMessage("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

fuseMenu = coreComponent.createMenuSymbol("FUSE_MENU", devCfgMenu)
fuseMenu.setLabel("Fuse Settings")


fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", fuseMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY_CMD", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)" )
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)
deviceSecurity.setVisible(compilerChoice.getSelectedKey() == "XC32")
deviceSecurity.setDependencies(udpateSymbolEnableAndVisibility, ['core.COMPILER_CHOICE'])

xc32LinkerMacroRAMLength = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RAM_LENGTH", None)
xc32LinkerMacroRAMLength.setCategory("C32-LD")
xc32LinkerMacroRAMLength.setKey("preprocessor-macros")
xc32LinkerMacroRAMLength.setAppend(True, ";=")

registerGroup = "USER_FUSES"
registerNames = ["USER_WORD_0", "USER_WORD_1", "USER_WORD_2"]

default = [1, 0x1C, 1 , 0x2, 0, 0 , 0, 1, 0, 0, 10, 10, 10, 0, 0xFFFFFFFF ]
numfuses = 0

for i in range(0, len(registerNames)):
    path = "/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + registerGroup + "\"]/register@[name=\"" + registerNames[i] + "\"]"
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
                keyValueSymbol.addKey(name, str(value), caption)
            keyValueSymbol.setDefaultValue(default[numfuses])
            keyValueSymbol.setOutputMode("Key")
            keyValueSymbol.setDisplayMode("Description")

        if key == "RAMECC_ECCDIS":
            xc32LinkerMacroRAMLength.setDependencies(calculateRAMLength, ["FUSE_SYMBOL_VALUE" + str(numfuses)])

        numfuses = numfuses + 1

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_D51_E51_E53_E54")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M4 Configuration")
cortexMenu.setDescription("Configuration for Cortex M4")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CMCC Configuration")
cacheMenu.setDescription("CACHE Configuration")

# TCM exists on D5x/E5x and cannot be disabled. Only its size can be  configured.
# We need this symbol defined so that the FTL will emit the code associated
# with TCM configuration.
tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", cacheMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(True)
tcmEnable.setReadOnly(True)
tcmEnable.setVisible(False)

deviceTCMsize = coreComponent.createKeyValueSetSymbol("DEVICE_TCM_SIZE", cacheMenu)
deviceTCMsize.setLabel("TCM and cache Size")
deviceTCMsize.setOutputMode("Value")
deviceTCMsize.setDisplayMode("Description")
deviceTCMsize.addKey("0KB", "2", "TCM: 0 KB, Cache: 4 KB" )
deviceTCMsize.addKey("2KB", "1", "TCM: 2 KB, Cache: 2 KB")
deviceTCMsize.addKey("3KB", "0", "TCM: 3 KB, Cache: 1 KB")
deviceTCMsize.addKey("4KB", "3", "TCM: 4 KB,  Cache: 0 KB")
deviceTCMsize.setSelectedKey("0KB")


dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(False)
dcacheEnable.setDependencies(updateDataCacheVisibility, ["DEVICE_TCM_SIZE"])

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", cacheMenu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)
stackTCM.setVisible(False)

cacheAlign = coreComponent.createIntegerSymbol("CACHE_ALIGN", cacheMenu)
cacheAlign.setLabel("Cache Alignment Length")
cacheAlign.setVisible(False)
cacheAlign.setDefaultValue(16)

periInstanceMultiVectorSupport = coreComponent.createBooleanSymbol("PERIPHERAL_MULTI_VECTOR", None)
periInstanceMultiVectorSupport.setDefaultValue(True)
periInstanceMultiVectorSupport.setVisible(False)

def getCorePeripherals():

    # Components which are creating critical section
    corePeripherals = ["DMAC", "I2S", "RTC", "TC", "SERCOM"]

    return corePeripherals

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
                    "SRAM"              : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "8MB"],
                    "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                    "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ],
                    "QSPI"              : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x04000000",   "256MB"],}
    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM", "QSPI"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList

global nvmWaitStates
nvmWaitStates = { #VDD > 2.7
                    24000000 : 0,
                    51000000 : 1,
                    77000000 : 2,
                    101000000 : 3,
                    119000000 : 4,
                    120000000 : 5
                }

periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVMCTRL\"]")
modules = periphNode.getChildren()
components = []
for nvmctrl_instance in range (0, len(modules)):
    components.append(str(modules[nvmctrl_instance].getAttribute("name")).lower())
Database.activateComponents(components)

global swdPin
swdPin = {"PA30": "0x07"}

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
coreComponent.addPlugin("../peripheral/port_u2210/plugin/port_u2210.jar")

# # load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_d51_e51_e53_e54/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_d51_e51_e53_e54/plugin/clk_sam_e5x.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "NVIC_MANAGER", {"plugin_name": "NVIC Configuration", "main_html_path": "csp/plugins/configurators/interrupt_configurators/nvic_interrupt_configuration/build/index.html"})

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "MPU_CONFIGURATOR", {"plugin_name": "MPU Configurator", "main_html_path": "csp/plugins/configurators/mpu-configurators/mpu-configurator/build/index.html"})

# #load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# #load DWT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwt/config/dwt.py")

# # load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2503/config/dmac.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar",
                        "DMA_UI_MANAGER_ID_SAM_D51_E51_E53_E54",
                        {
                            "plugin_name": "DMA Configuration",
                            "main_html_path": "csp/plugins/configurators/dma-configurators/dma-configurator-1/build/index.html",
                            "symbol_config": "csp/peripheral/dmac_u2503/plugin/symbol-config.json"
                        }
                        )

# # load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

#  load CMCC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/cmcc_u2015/config/cmcc.py")

# # load device specific adc manager information
# coreComponent.addPlugin("../peripheral/afec_11147/plugin/ARM_M7_ADCmanager.jar")

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

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_D51_E51_E53_E54.c.ftl")
devconSystemInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]

#Override default sizes for IAR stack and heap
iarUsrStackSize.setDefaultValue(0xC000)
iarHeapSize.setDefaultValue(0x0)