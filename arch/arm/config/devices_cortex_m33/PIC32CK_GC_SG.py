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

global xc32StackInTCMSym
global xc32DTCMSizeSym
global xc32ITCMSizeSym
global tcmSize
global tcmEnable

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    trustZoneSupported = coreComponent.createBooleanSymbol("TRUSTZONE_SUPPORTED", devCfgMenu)
    trustZoneSupported.setVisible(False)

registerGroup = ["FUSES_USERCFG1", "FUSES_BOOTCFG1", "FUSES_DALCFG", "FUSES_USERCFG2", "FUSES_BOOTCFG2"]

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
    if (event["value"]):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")

def udpateSymbolEnableAndVisibility (symbol, event):
    symbol.setVisible(event["symbol"].getSelectedKey() == "XC32")

def setDMADefaultSettings():
    triggerSettings = {"Software Trigger": ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Transmit": ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                       "Standard_Receive": ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    return triggerSettings

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)" )
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)
deviceSecurity.setVisible(compilerChoice.getSelectedKey() == "XC32")
deviceSecurity.setDependencies(udpateSymbolEnableAndVisibility, ['core.COMPILER_CHOICE'])

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
if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    default = [0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0xFFFF, 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF,#FUSES_USERCFG1
            0, 0, 0, 0, 0, 0, 0, 0xFFFFFFFF, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0xF, 0xF, 0x3, 1, 0x0, 1, 0, 0, 0, 0, 0x202, 
            0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
            0x0, 0x0, 0x0, 0xFFFFFFFF, 0xFFFFFFFF,
            0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x1, 0xFFFE, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,                                                      #FUSES_BOOTCFG1
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0x706, 0xFCF04, 0x707F736, 0x3A86, 0x3FF, 0x3F, 0xBF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            #2, 2,              #FUSES_DALCFG
            0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, #FUSES_USERCFG2
            0, 1, 1, 0, 0, 0, 0, 0xFFFFFFFF, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0xF, 0xF, 0x3, 1, 0x0, 1, 0, 0, 0, 0, 0x202, 
            0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 
            0x0, 0x0, 0x0, 0xFFFFFFFF, 0xFFFFFFFF,
            0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x0, 0x0, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,                                                      #FUSES_BOOTCFG2
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0x706, 0xFCF04, 0x707F736, 0x3A86, 0x3FF, 0x3F, 0xBF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,]
else:
    default = [0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0x1, 0xFFFE, 0xFFFF             , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF ,             0xFFFF, 0xFFFF , 0xFFFF,#FUSES_USERCFG1
            0, 0, 0, 0, 0, 0, 0, 0xFFFFFFFF, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0xF, 0xF, 0x3, 1, 0x0, 1, 0, 0, 0, 0, 0x202, 
            0, 0, 0, 0, 1, 1, 0x1, 0xFFFE, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,                                                      #FUSES_BOOTCFG1
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0x706, 0xFCF04, 0x707F736, 0x3A86, 0x3FF, 0x3F, 0xBF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            #2, 2,              #FUSES_DALCFG
            0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0x0, 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, 0xFFFF , 0xFFFF, #FUSES_USERCFG2
            0, 1, 1, 0, 0, 0, 0, 0xFFFFFFFF, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0x3, 1, 0xF, 0xF, 0x3, 1, 0x0, 1, 0, 0, 0, 0, 0x202, 
            0, 0, 0, 0, 1, 1, 0x0, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,                                                      #FUSES_BOOTCFG2
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,
            0xFFFFFFFF, 0x706, 0xFCF04, 0x707F736, 0x3A86, 0x3FF, 0x3F, 0xBF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF,]
numfuses = 0

global memoryFuseMaxValue
memoryFuseMaxValue = {}

for group in range(0, len(registerGroup)):
    regGroupName = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + "FUSES" + "\"]/instance@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + registerGroup[group] + "\"]").getAttribute("name-in-module")
    fuseRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"" + "FUSES" + "\"]/register-group@[name=\"" + regGroupName + "\"]")
    registerNames = fuseRegisterGroup.getChildren()
    for i in range(0, len(registerNames)):
        fuseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"" + regGroupName + "\"]/register@[name=\"" + registerNames[i].getAttribute("name") + "\"]")
        fuseNodeValues = fuseNode.getChildren()
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
                    key = fuseNodeValues[index].getAttribute("name")
                    caption = registerGroup[group].replace("FUSES_", "") + " " + fuseNodeValues[index].getAttribute("caption") + regIdx
                    valueGroup = fuseNodeValues[index].getAttribute("values")
                    if key == "Reserved":
                        continue
                    # Skip unsupported DAL Fuses
                    if valueGroup == "DAL__CPU0" or valueGroup == "DAL__CPU1":
                        continue
                    stringSymbol = coreComponent.createStringSymbol("FUSE_SYMBOL_NAME" + str(numfuses), fuseSettings)
                    stringSymbol.setDefaultValue(registerGroup[group] + "_" + registerNames[i].getAttribute("name") + regIdx + "_" + key)
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
                            keyValueSymbol.setDefaultValue(default[numfuses])
                            keyValueSymbol.setOutputMode("Key")
                            keyValueSymbol.setDisplayMode("Description")
                            if ("ANSC" in key) :
                                memoryFuseMaxValue[key] = [int(getMaxValue(mask)), getDefaultVal(str(default[numfuses]), mask), caption]
                                hexSymbol.setVisible(False)
                        else:
                            hexSymbol = coreComponent.createHexSymbol("FUSE_SYMBOL_VALUE" + str(numfuses), fuseSettings)
                            hexSymbol.setLabel(caption)
                            hexSymbol.setMin(0)
                            hexSymbol.setMax(getMaxValue(mask))
                            hexSymbol.setDefaultValue(default[numfuses])
                            # we will handle memory assignment and peripheral assignment using trustzone manager creating  abstraction over fuses
                            if ("ANS" in key) or ("RNS" in key):
                                memoryFuseMaxValue[key] = [int(getMaxValue(mask)), getDefaultVal(str(default[numfuses]), mask), caption]
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
                        keyValueSymbol.setDefaultValue(default[numfuses])
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
                hexSymbol.setDefaultValue(default[numfuses])
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
                    hexSymbol.setDefaultValue(default[numfuses])
                    numfuses = numfuses + 1

fuse = coreComponent.createIntegerSymbol("NUMBER_OF_FUSES", fuseSettings)
fuse.setDefaultValue(numfuses)
fuse.setVisible(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    systemResourcesList = ["GCLK", "OSC32KCTRL", "OSCCTRL", "MCLK", "IDAU"]
    mixSecurePeripheralList = ["EIC", "EVSYS", "FCR", "FCW", "PAC", "PORT"]
    # Setup TrustZone Manager
    execfile(Variables.get("__CORE_DIR") + "/config/trustZone/trustZoneManager.py")

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CK_GC_SG")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M33 Configuration")
cortexMenu.setDescription("Configuration for Cortex M33")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CMCC Configuration")
cacheMenu.setDescription("CACHE Configuration")

# TCM exists on PIC32CK GC/SG and cannot be disabled. Only its size can be  configured.
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
    corePeripherals = ["DMA", "I2S", "RTC", "TC", "SERCOM"]

    return corePeripherals

def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"             : ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x00000000",   "2MB"   ],
                   "SRAM"              : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "512KB"],
                   "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x44000000",   "256MB" ],
                   "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ],
                   "QSPI"              : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x10000000",   "256MB"],}
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
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32ck_gc_sg/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32ck_gc_sg/plugin/clk_pic32ck_gc_sg.jar")

# load mpu
#execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
#coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")
if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick_s/config/systick.py")

#load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dma_03639/config/dma.py")
coreComponent.addPlugin("../peripheral/dma_03639/plugin/dmamanager.jar")

#load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

#  load CMCC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/cmcc_u2015/config/cmcc.py")

# load DWT
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dwt/config/dwt.py")

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

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    devconSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_CONFIG_BITS_INITIALIZATION")
else:
    devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/PIC32CK_GC_SG.c.ftl")

devconSystemInitFile.setMarkup(True)
