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

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    trustZoneSupported = coreComponent.createBooleanSymbol("TRUSTZONE_SUPPORTED", devCfgMenu)
    trustZoneSupported.setVisible(False)

registerGroup = ["USER_FUSES", "BOCOR_FUSES"]

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value

def setDMACDefaultSettings():

    triggerSettings = {
                        "Software Trigger"  : ["BLOCK", "INCREMENTED_AM", "INCREMENTED_AM", "WORD"],
                        "Standard_Transmit" : ["BEAT", "INCREMENTED_AM", "FIXED_AM", "BYTE"],
                        "Standard_Receive"  : ["BEAT", "FIXED_AM", "INCREMENTED_AM", "BYTE"]
                    }

    return triggerSettings

def calculateRAMLength(symbol, event):
    if event["symbol"].getSelectedKey() != None:
        RAMSize = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"HSRAM\"]").getAttribute("size")
        RAMPowerSwitchConfVal = int(event["symbol"].getSelectedKey().replace("KB", "")) * 1024
        if RAMPowerSwitchConfVal < int(RAMSize, 16):
            symbol.setValue("RAM_LENGTH=" + str(hex(RAMPowerSwitchConfVal)))
        else:
            symbol.setValue("")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)" )
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)
deviceSecurity.setVisible(False)

xc32LinkerMacroRAMLength = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RAM_LENGTH", None)
xc32LinkerMacroRAMLength.setCategory("C32-LD")
xc32LinkerMacroRAMLength.setKey("preprocessor-macros")
xc32LinkerMacroRAMLength.setAppend(True, ";=")
xc32LinkerMacroRAMLength.setDependencies(calculateRAMLength, ["pm.PM_PWCFG_RAMPSWC"])

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    secXc32LinkerMacroRAMLength = coreComponent.createSettingSymbol("SECURE_XC32_LINKER_MACRO_RAM_LENGTH", None)
    secXc32LinkerMacroRAMLength.setCategory("C32-LD")
    secXc32LinkerMacroRAMLength.setKey("preprocessor-macros")
    secXc32LinkerMacroRAMLength.setAppend(True, ";=")
    secXc32LinkerMacroRAMLength.setDependencies(calculateRAMLength, ["pm.PM_PWCFG_RAMPSWC"])
    secXc32LinkerMacroRAMLength.setSecurity("SECURE")

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

def getMaxValue(mask):
    if mask == 0 :
        return hex(0)

    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1

    return mask

fuseMenu = coreComponent.createMenuSymbol("FUSE_MENU", devCfgMenu)
fuseMenu.setLabel("Fuse Settings")

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", fuseMenu)
fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)

global fuseMapSymbol
fuseMapSymbol = {}
numfuses = 0

global memoryFuseMaxValue
memoryFuseMaxValue = {}

for group in range(0, len(registerGroup)):
    #registerNames = ["USER_WORD_0", "USER_WORD_1", "USER_WORD_2", "USER_WORD_3", "USER_WORD_4", "USER_WORD_5", "USER_WORD_6"]
        registerNamesnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + registerGroup[group] + "\"]")
        registerNamesvalue = registerNamesnode.getChildren()
        for regNameindex in range(0, len(registerNamesvalue)):
            registerNames = registerNamesvalue[regNameindex].getAttribute("name")
            path = "/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + registerGroup[group] + "\"]/register@[name=\"" + registerNames + "\"]"
            fuseNode = ATDF.getNode(path)
            initVal = fuseNode.getAttribute("initval")

            fuseNodeValues = fuseNode.getChildren()
            for index in range(0, len(fuseNodeValues)):
                key = fuseNodeValues[index].getAttribute("name")
                caption=fuseNodeValues[index].getAttribute("caption")
                valueGroup = fuseNodeValues[index].getAttribute("values")
                stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
                stringSymbol.setDefaultValue(key)
                stringSymbol.setVisible(False)
                fuseMapSymbol[stringSymbol.getValue()] = "FUSE_SYMBOL_VALUE" + str(numfuses)
                if valueGroup == None:
                    mask = fuseNodeValues[index].getAttribute("mask")
                    count = bin((int(mask, 16))).count("1")
                    if count == 1:
                        keyValueSymbol = coreComponent.createKeyValueSetSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                        keyValueSymbol.setLabel(caption)
                        keyValueSymbol.addKey("CLEAR", "0", "CLEAR")
                        keyValueSymbol.addKey("SET", "1", "SET")
                        keyValueSymbol.setDefaultValue(getDefaultVal(initVal, mask))
                        keyValueSymbol.setOutputMode("Key")
                        keyValueSymbol.setDisplayMode("Description")
                        # we will handle memory assignment and peripheral assignment using trustzone manager creating abstraction over fuses
                        if "NONSEC" in key:
                            keyValueSymbol.setVisible(False)
                    else:
                        hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                        hexSymbol.setLabel(caption)
                        hexSymbol.setMin(0)
                        hexSymbol.setMax(getMaxValue(mask))
                        hexSymbol.setDefaultValue(getDefaultVal(initVal, mask))
                        # we will handle memory assignment and peripheral assignment using trustzone manager creating abstraction over fuses
                        if "IDAU_" in key:
                            memoryFuseMaxValue[key] = [int(getMaxValue(mask)), getDefaultVal(initVal, mask), caption]
                            hexSymbol.setVisible(False)
                else:
                    mask = fuseNodeValues[index].getAttribute("mask")
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
                    keyValueSymbol.setDefaultValue(getDefaultVal(initVal, mask))
                    keyValueSymbol.setOutputMode("Value")
                    keyValueSymbol.setDisplayMode("Description")

                numfuses = numfuses + 1

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    systemResourcesList = ["GCLK", "OSC32KCTRL", "OSCCTRL", "MCLK", "IDAU"]
    mixSecurePeripheralList = ["EIC", "EVSYS", "NVMCTRL", "PAC", "PORT"]
    # Setup TrustZone Manager
    execfile(Variables.get("__CORE_DIR") + "/config/trustZone/trustZoneManager.py")

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_L10_L11")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M23 Configuration")
cortexMenu.setDescription("Configuration for Cortex M23")

periInstanceMultiVectorSupport = coreComponent.createBooleanSymbol("PERIPHERAL_MULTI_VECTOR", None)
periInstanceMultiVectorSupport.setDefaultValue(True)
periInstanceMultiVectorSupport.setVisible(False)

def getCorePeripherals():

    # Components which are creating critical section
    corePeripherals = ["DMAC", "I2S", "RTC", "TC", "SERCOM"]

    return corePeripherals

global nvmWaitStates
nvmWaitStates = { #VDD > 2.7
                    14000000 : 0,
                    32000000 : 1,
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
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_l10_l11/config/clock.py")
coreComponent.addPlugin("../peripheral/clk_sam_l10_l11/plugin/clk_sam_l10_l11.jar")

#load mpu
# execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
# coreComponent.addPlugin("../peripheral/mpu/plugin/MPUmanager.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick_s/config/systick.py")
#load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2223/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_u2223/plugin/dmamanager.jar")

#load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

# load device specific adc manager information
#coreComponent.addPlugin("../peripheral/afec_11147/plugin/ARM_M7_ADCmanager.jar")

# Activate PM
periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PM\"]")
modules = periphNode.getChildren()
components = []
for pm_instance in range (0, len(modules)):
    components.append(str(modules[pm_instance].getAttribute("name")).lower())
Database.activateComponents(components)

# Activate Event System
periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EVSYS\"]")
modules = periphNode.getChildren()
components = []
for evsys_instance in range (0, len(modules)):
    components.append(str(modules[evsys_instance].getAttribute("name")).lower())
Database.activateComponents(components)

global armLibCSourceFile
global secarmLibCSourceFile
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

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    secarmSysStartSourceFile = coreComponent.createFileSymbol("SEC_STARTUP_C", None)
    secarmSysStartSourceFile.setSourcePath("../arch/arm/templates/" + compilerSelected + "/cortex_m/startup/startup_" + compilerSelected + ".c.ftl")
    secarmSysStartSourceFile.setOutputName("startup_" + compilerSelected + ".c")
    secarmSysStartSourceFile.setMarkup(True)
    secarmSysStartSourceFile.setOverwrite(True)
    secarmSysStartSourceFile.setDestPath("")
    secarmSysStartSourceFile.setProjectPath("config/" + configName + "/")
    secarmSysStartSourceFile.setType("SOURCE")
    secarmSysStartSourceFile.setSecurity("SECURE")
    secarmSysStartSourceFile.setDependencies(
        genSysSourceFile, ["CoreSysStartupFile", "CoreSysFiles"])

    # generate libc_syscalls.c file
    secarmLibCSourceFile = coreComponent.createFileSymbol("SEC_LIBC_SYSCALLS_C", None)
    secarmLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
    secarmLibCSourceFile.setOutputName("libc_syscalls.c")
    secarmLibCSourceFile.setMarkup(True)
    secarmLibCSourceFile.setOverwrite(True)
    secarmLibCSourceFile.setDestPath("")
    secarmLibCSourceFile.setProjectPath("config/" + configName + "/")
    secarmLibCSourceFile.setType("SOURCE")
    secarmLibCSourceFile.setSecurity("SECURE")
    secarmLibCSourceFile.setDependencies(genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])
    compilerSpecifics = [armSysStartSourceFile, secarmSysStartSourceFile]

else:
    compilerSpecifics = [armSysStartSourceFile]

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    devconSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_CONFIG_BITS_INITIALIZATION")
else:
    devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_L10_L11.c.ftl")

devconSystemInitFile.setMarkup(True)

