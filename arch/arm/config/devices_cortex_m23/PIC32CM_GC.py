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
global ramStart
global maxRamSize

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    trustZoneSupported = coreComponent.createBooleanSymbol("TRUSTZONE_SUPPORTED", devCfgMenu)
    trustZoneSupported.setVisible(False)

registerGroup = ["FUSES_BOOTCFG1", "FUSES_BOOTCFG1A"]

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

ramStart = coreComponent.createStringSymbol("DEVICE_RAM_START", None)
ramStart.setVisible(False)
ramStart.setDefaultValue(ATDF.getNode('/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name="MCRAMC_RET"]').getAttribute("start"))

maxRamSize = coreComponent.createStringSymbol("DEVICE_RAM_SIZE", None)
maxRamSize.setVisible(False)
maxRamSize.setDefaultValue(ATDF.getNode('/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name="MCRAMC_RET"]').getAttribute("size"))

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

mixSecConfig = coreComponent.createBooleanSymbol("CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC", devCfgMenu)
mixSecConfig.setLabel("Configure overall security of a peripheral to Non secure in order for it to be Mixsecure")
mixSecConfig.setDefaultValue(True)
mixSecConfig.setVisible(False)

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

global H2PBX_Dict
H2PBX_Dict = {}

# Create a map of peripheral instance vs bridge id and peripheral id. Example: {"peripheral instance": {"bridge_id": 1, "periph_id": 21}, ...}
# Parse the fuses module and get the peripheral ID corresponding to a given bit in H2PBx from the above created map.
# fuseMapSymbol is used in UI. Whereas "FUSE_SYMBOL_NAMEx" and "FUSE_SYMBOL_VALUEx" pair is used in code generation for fuses.
# Use human readable string in fuseMapSymbol, whereas use the actual fuse name in "FUSE_SYMBOL_NAMEx" symbol.
# Note that symbols are created even for H2PBx bits which are not mapped to any peripheral. This is because, MPLABx requires all fuse bits in a fuse word to be
# defined, irrespecitve of whether it is used or not. For un-mapped fuse bits in H2PBx, the fuseMapSymbol ends with "None" instead of actual peripheral name. Use
# this to discard such un-mapped bits from making it to the peripheralList list which is consumed by the TZ manager UI.

peripherals_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals')
modules_list = peripherals_node.getChildren()
for module_node in modules_list:
    module_name = module_node.getAttribute("name")
    instance_list = module_node.getChildren()
    for instance_node in instance_list:
        instance_name = instance_node.getAttribute("name")
        parameters_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="{0}"]/instance@[name="{1}"]/parameters'.format(module_name, instance_name))
        if parameters_node != None:
            bridge_id_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="{0}"]/instance@[name="{1}"]/parameters/param@[name="BRIDGE_ID"]'.format(module_name, instance_name))
            if bridge_id_node != None:
                bridge_id = bridge_id_node.getAttribute("value")

            periph_id_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="{0}"]/instance@[name="{1}"]/parameters/param@[name="PERIPH_ID"]'.format(module_name, instance_name))
            if periph_id_node != None:
                periph_id = periph_id_node.getAttribute("value")

            if bridge_id_node != None and periph_id_node != None:
                H2PBX_Dict[instance_name] = {"bridge_id":bridge_id, "periph_id":periph_id}

def getH2PBxPeripheral(h2pb_instance_num, bit_mask_str):
    global H2PBX_Dict

    bit_mask_int = int(bit_mask_str, 0)
    bit_pos = bit_mask_int.bit_length() - 1

    for key, val in H2PBX_Dict.items():
        if H2PBX_Dict[key]["bridge_id"] == h2pb_instance_num and H2PBX_Dict[key]["periph_id"] == str(bit_pos):
            return key

    return None

for group in range(0, len(registerGroup)):
    key = ""
    caption = ""
    regGroupName = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + "FUSES" + "\"]/instance@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + registerGroup[group] + "\"]")
    if regGroupName == None:
        continue
    regGroupName = regGroupName.getAttribute("name-in-module")
    fuseRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + regGroupName + "\"]")
    registerNames = fuseRegisterGroup.getChildren()
    for i in range(0, len(registerNames)):
        fuseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"" + regGroupName + "\"]/register@[name=\"" + registerNames[i].getAttribute("name") + "\"]")
        fuseNodeValues = fuseNode.getChildren()
        fuseInitVal = fuseNode.getAttribute("initval")

        if len(fuseNodeValues) != 0:
            regIdx = "0"
            if fuseNode.getAttribute("count") == None:
                cnt = 1
                regIdx = ""
            else:
                cnt =  int(fuseNode.getAttribute("count"))
            for idx in range(0, cnt):
                if regIdx != "":
                    regIdx = str(idx)
                for index in range(0, len(fuseNodeValues)):
                    # Skip the children starting with "<mode name="BLOCK" or "<mode name="WATERMARK"
                    if ((fuseNodeValues[index].getAttribute("name") == "BLOCK" or fuseNodeValues[index].getAttribute("name") == "WATERMARK") and fuseNodeValues[index].getAttribute("modes") == None):
                        continue
                    # Skip all bitfields starting with <bitfield modes="BLOCK" as the Block mode is not supported, only watermark mode is supported.
                    if (fuseNodeValues[index].getAttribute("modes") != None and fuseNodeValues[index].getAttribute("modes") == "BLOCK"):
                        continue
                    # If register name is H2PBx, then get the mapped peripheral name by calling the getH2PBxPeripheral function
                    if (registerNames[i].getAttribute("name") in ["H2PB0_NONSECCLRA", "H2PB0_NONSECSETA", "H2PB1_NONSECCLRA", "H2PB1_NONSECSETA", "H2PB2_NONSECCLRA", "H2PB2_NONSECSETA"]):
                        # Pass the H2PB instance and bitfield mask to the getH2PBxPeripheral function and get the corresponding peripheral instance name
                        key = getH2PBxPeripheral(registerNames[i].getAttribute("name")[len("H2PB"):][0], fuseNodeValues[index].getAttribute("mask"))
                        if key != None:
                            caption_text = ""
                            if "NONSECCLRA" in registerNames[i].getAttribute("name"):
                                caption_text = "NONSECCLR bit for " + key
                            else:
                                caption_text = "NONSECSET bit for " + key
                            caption = registerGroup[group].replace("FUSES_", "") + " " + caption_text
                        else:
                            key = "None"    # we still need to create fuse symbol, but we will create it with key set to "None", so that TZ manager does not show this.
                    else:
                        key = fuseNodeValues[index].getAttribute("name")
                        caption = registerGroup[group].replace("FUSES_", "") + " " + fuseNodeValues[index].getAttribute("caption") + regIdx

                    valueGroup = fuseNodeValues[index].getAttribute("values")
                    if key == "Reserved":
                        continue
                    # Skip unsupported DAL Fuses
                    if valueGroup == "DAL__CPU0" or valueGroup == "DAL__CPU1":
                        continue
                    stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
                    stringSymbol.setDefaultValue(registerGroup[group] + "_" + registerNames[i].getAttribute("name") + regIdx + "_" + fuseNodeValues[index].getAttribute("name"))
                    stringSymbol.setVisible(False)
                    fuseMapSymbol[registerGroup[group] + "_" + registerNames[i].getAttribute("name") + regIdx + "_" + key] = "FUSE_SYMBOL_VALUE" + str(numfuses)
                    if valueGroup == None:
                        mask = fuseNodeValues[index].getAttribute("mask")
                        count = bin((int(mask, 16))).count("1")
                        if count == 1:
                            keyValueSymbol = coreComponent.createKeyValueSetSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                            keyValueSymbol.setLabel(caption)
                            keyValueSymbol.addKey("CLEAR", "0", "CLEAR")
                            keyValueSymbol.addKey("SET", "1", "SET")
                            keyValueSymbol.setDefaultValue(getDefaultVal(fuseInitVal, mask))
                            keyValueSymbol.setOutputMode("Key")
                            keyValueSymbol.setDisplayMode("Description")
                            if ("None" in key):
                                keyValueSymbol.setVisible(False)
                        else:
                            hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                            hexSymbol.setLabel(caption)
                            hexSymbol.setMin(0)
                            hexSymbol.setMax(getMaxValue(mask))
                            if fuseNodeValues[index].getAttribute("name") == "SEQ":
                                hexSymbol.setDefaultValue(0x01)
                            elif fuseNodeValues[index].getAttribute("name") == "SEQBAR":
                                hexSymbol.setDefaultValue(0xFFFE)
                            else:
                                hexSymbol.setDefaultValue(getDefaultVal(fuseInitVal, mask))
                            if ("None" in key):
                                hexSymbol.setVisible(False)
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
                        #keyValueSymbol.setDefaultValue(default[numfuses])
                        keyValueSymbol.setDefaultValue(0)
                        if valueGroup == "RPMU_VREGCTRL__VREGOUT" or valueGroup == "RPMU_VREGCTRL__LVSTDBY" or valueGroup == "RPMU_VREGCTRL__LVHIB" or valueGroup == "RPMU_VREGCTRL__ULDOLEVEL":
                            keyValueSymbol.setOutputMode("Value")
                        else:
                            keyValueSymbol.setOutputMode("Key")
                        keyValueSymbol.setDisplayMode("Description")
                    numfuses = numfuses + 1
        else:
            if fuseNode.getAttribute("count") == None:
                stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
                stringSymbol.setDefaultValue(registerGroup[group] + "_" + registerNames[i].getAttribute("name") + "_" + registerNames[i].getAttribute("name"))
                stringSymbol.setVisible(False)
                fuseMapSymbol[stringSymbol.getValue()] = "FUSE_SYMBOL_VALUE" + str(numfuses)
                hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                hexSymbol.setLabel(registerGroup[group].replace("FUSES_", "") + " " + registerNames[i].getAttribute("caption"))
                #hexSymbol.setDefaultValue(default[numfuses])
                hexSymbol.setDefaultValue(0)
                numfuses = numfuses + 1
            else:
                count =  int(fuseNode.getAttribute("count"))
                for index in range(0, count):
                    stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
                    stringSymbol.setDefaultValue(registerGroup[group] + "_" + registerNames[i].getAttribute("name") + str(index) + "_" + registerNames[i].getAttribute("name"))
                    stringSymbol.setVisible(False)
                    fuseMapSymbol[stringSymbol.getValue()] = "FUSE_SYMBOL_VALUE" + str(numfuses)
                    hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                    hexSymbol.setLabel(registerGroup[group].replace("FUSES_", "") + " " + registerNames[i].getAttribute("caption") + str(index))
                    #hexSymbol.setDefaultValue(default[numfuses])
                    hexSymbol.setDefaultValue(0)
                    numfuses = numfuses + 1

memoryFuseMaxValue["IDAU_ANSC"] =  [int(getMaxValue("0xFFFFFF")),   0, u'USERCFG2 Non-secure callable Flash application size']
memoryFuseMaxValue["IDAU_RNS"] =  [int(getMaxValue("0xFFFFFF")), 0, u'USERCFG2 Non-secure RAM size']
memoryFuseMaxValue["IDAU_ANS"] =   [int(getMaxValue("0xFFFFFF")), 0, u'USERCFG2 Non-secure Flash application size']

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    systemResourcesList = ["GCLK", "OSC32KCTRL", "OSCCTRL", "MCLK", "IDAU"]
    mixSecurePeripheralList = ["EIC", "PORT"]
    # alwaysSecurePeripheralsList = ["FCR", "FCW", "FREQM", "WDT", "HMATRIX2", "IDAU", "PAC", "WFT", "ATW", "MBISTINTF", "TDM", "MCRAMC", "H2PB0", "BROMC", "EVSYS", "PUF", "SCANCTRL", "H2PB1", "PM", "SUPC", "RSTC", "RTC", "TRAM", "AT", "H2PB2"]
    # alwaysNonSecurePeripheralsList = ["DSU"]
    # Setup TrustZone Manager
    execfile(Variables.get("__CORE_DIR") + "/config/trustZone/trustZoneManager.py")

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CM_GC_SG")
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
    corePeripherals = ["I2S", "RTC", "TC", "TCC", "SERCOM"]

    return corePeripherals

def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"             : ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xC000000",   "512KB"   ],
                   "SRAM"              : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "128KB"],
                   "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x44000000",   "256MB" ],
                   "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ]
                   }
    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM"]

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

global swdPin
swdPin = {"PA30": "0x06"}

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
coreComponent.addPlugin("../peripheral/port_u2210/plugin/port_u2210.jar")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32cm_gc_sg/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32cm_gc_sg/plugin/clk_pic32cm_gc_sg.jar")

#load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "MPU_CONFIGURATOR", {"plugin_name": "MPU Configurator", "main_html_path": "csp/plugins/configurators/mpu-configurators/mpu-configurator/build/index.html"})

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "NVIC_MANAGER", {"plugin_name": "NVIC Configuration", "main_html_path": "csp/plugins/configurators/interrupt_configurators/nvic_interrupt_configuration/build/index.html"})

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")
if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick_s/config/systick.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2223/config/dmac.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar",
                        "DMA_UI_MANAGER_ID_SAM_L21",
                        {
                            "plugin_name": "DMA Configuration",
                            "main_html_path": "csp/plugins/configurators/dma-configurators/dma-configurator-1/build/index.html",
                            "symbol_config": "csp/peripheral/dmac_u2223/plugin/symbol-config.json"
                        }
                        )

#load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_04298/config/pac.py")

ramInit = coreComponent.createBooleanSymbol("RAM_INIT", xc32Menu)
ramInit.setDefaultValue(True)
ramInit.setVisible(True)

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
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/SAM_LE00_LS00_LS60.c.ftl")

devconSystemInitFile.setMarkup(True)
