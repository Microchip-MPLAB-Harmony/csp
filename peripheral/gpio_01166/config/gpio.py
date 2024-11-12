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

import re
import xml.etree.ElementTree as ET
import os.path
import inspect

print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

# "pioSymChannel" list will hold the port channels which are present in particular device.
# it will be dynamically populated based on ATDF pinout info.
global pioSymChannel
pioSymChannel = []

global packageIdMap
packageIdMap = {}
global pin_map
pin_map = {}
global pinModifierMap
pinModifierMap = {}
global pin_position
pin_position = []
global sort_alphanumeric
global createPinMap

global availablePinDictionary
availablePinDictionary = {}

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

global getAvailablePins

# API used by core to return available pins to sender component
def getAvailablePins():
    return availablePinDictionary

# Dependency Function to show or hide the warning message depending on Interrupt
def InterruptStatusWarning(symbol, event):
    if entireInterrupt.getValue() == True and Database.getSymbolValue("core", "CHANGE_NOTICE_INTERRUPT_ENABLE_UPDATE") == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Dependency Function to pass interrupt related info to Interrupt Manager.
# This function will be entered only by internal change happening to PORT channel interrupt, never by manual
# change because channel interrupt is not user configurable directly.
def pioInterruptControl(pioInterrupt, event):
    Database.setSymbolValue("core", "CHANGE_NOTICE_INTERRUPT_ENABLE", event["value"], 1)
    Database.setSymbolValue("core", "CHANGE_NOTICE_INTERRUPT_HANDLER_LOCK", event["value"], 1)

    if event["value"] == True:
        Database.setSymbolValue("core", "CHANGE_NOTICE_INTERRUPT_HANDLER", "CHANGE_NOTICE_InterruptHandler", 1)
    else :
        Database.setSymbolValue("core", "CHANGE_NOTICE_INTERRUPT_HANDLER", "CHANGE_NOTICE_Handler", 1)

def pinLatchCal(pin, event):
    global gpioSym_GPIO_LAT
    global pinDirection
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        LAT_Value = gpioSym_GPIO_LAT[channelIndex].getValue()

        if event["value"] == "High":
            LAT_Value |= 1 << bit_pos
        else:
            LAT_Value &= ~(1 << bit_pos)

        gpioSym_GPIO_LAT[channelIndex].setValue(LAT_Value, 2)

def pinDirCal(pin, event):
    global gpioSym_GPIO_TRIS
    global pinChannel
    global pinBitPosition
    global pinLatch

    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        TRIS_Value = gpioSym_GPIO_TRIS[channelIndex].getValue()

        if event["value"] == "Out":
            TRIS_Value |= 1 << bit_pos
        else:
            TRIS_Value &= ~(1 << bit_pos)
        gpioSym_GPIO_TRIS[channelIndex].setValue(TRIS_Value, 2)

def pinModeCal(pin, event):
    global gpioSym_GPIO_AD1PCFG
    global pinChannel
    global pinBitPosition
    global pinLatch

    pin_num = int((pin.getID()).split("_")[2])

    AD1PCFG_Value = gpioSym_GPIO_AD1PCFG.getValue()

    if event["value"] == "DIGITAL":
        AD1PCFG_Value |= 1 << pin_num
    else:
        AD1PCFG_Value &= ~(1 << pin_num)
    gpioSym_GPIO_AD1PCFG.setValue(AD1PCFG_Value, 2)

def pinInterruptCal(pin, event):
    global gpioSym_GPIO_CNEN
    global CnPinCount

    pin_num = int((event["id"]).split("_")[2])

    atLeastOneInterruptUsed = True

    if event["value"] == "":
        # if interrupt has been disabled for a particular pin, then see if is it disabled for all the pins;
        # if so, then uncheck corresponding port interrupt in GUI.
        atLeastOneInterruptUsed = False
        for pinNumber in range(0, CnPinCount):
            if pinInterrupt[pinNumber].getValue() != "":
                atLeastOneInterruptUsed = True
                break
    entireInterrupt.setValue(atLeastOneInterruptUsed, 1)

    CNEN_Value = gpioSym_GPIO_CNEN.getValue()

    if event["value"] == "True":
        CNEN_Value |= 1 << pin_num
    else:
        CNEN_Value &= ~(1 << pin_num)

    gpioSym_GPIO_CNEN.setValue(CNEN_Value, 2)

def pinOpenDrainCal(pin, event):
    global gpioSym_GPIO_ODC
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        OD_Value = gpioSym_GPIO_ODC[channelIndex].getValue()

        if event["value"] == "True":
            OD_Value |= 1 << bit_pos
        else:
            OD_Value &= ~(1 << bit_pos)

        gpioSym_GPIO_ODC[channelIndex].setValue(OD_Value, 2)

def pinPullUpCal(pin, event):
    global gpioSym_GPIO_CNPU

    pin_num = int((pin.getID()).split("_")[2])

    CNPU_Value = gpioSym_GPIO_CNPU.getValue()

    if event["value"] == "True":
        CNPU_Value |= 1 << pin_num
    else:
        CNPU_Value &= ~(1 << pin_num)

    gpioSym_GPIO_CNPU.setValue(CNPU_Value, 2)

def packageChange(packageSymbol, event):
    import re

    global pin
    global pinChannel
    global pinBitPosition

    pin_map, pin_position  = createPinMap(packageSymbol)

    for pinNumber in range(0, packagePinCount):
        pinBitPosition[pinNumber].setValue(-1, 2)
        pinChannel[pinNumber].setValue("", 2)
        if len(pin_position) > pinNumber: # This if condition is to handle the case when same device has two package options with different pin counts
            pin[pinNumber].setVisible(True)
            pin[pinNumber].setLabel("Pin " + str(pin_position[pinNumber]))

            if pin_map.get(pin_position[pinNumber]).startswith("R"):
                pinBitPosition[pinNumber].setValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber]))[0]), 2)
                pinChannel[pinNumber].setValue(pin_map.get(pin_position[pinNumber])[1], 2)
        else:
            pin[pinNumber].setVisible(False)

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)


def createPinMap(packageSymbol):
    import xml.etree.ElementTree as ET

    global pinoutXmlPath
    pin_map = {}
    pin_position = []
    global pinModifierMap
    pinModifierMap = {}

    tree = ET.parse(pinoutXmlPath)
    root = tree.getroot()

    for myPins in root.findall('pins'):
        for myPin in myPins.findall('pin'):
            if myPin.find('modifiers') != None:
                modeLock = True
            else:
                modeLock = False
            for myPackageNumber in myPin.findall('number'):
                if packageIdMap.get(packageSymbol.getValue()) == myPackageNumber.get("package"):
                    if "BGA" or "VTLA" in packageSymbol.getValue():
                        pin_map[myPackageNumber.get("pin")] = myPin.get("name")
                        pinModifierMap[myPackageNumber.get("pin")] = modeLock
                    else:
                        pin_map[int(myPackageNumber.get("pin"))] = myPin.get("name")
                        pinModifierMap[int(myPackageNumber.get("pin"))] = modeLock

    if "BGA" or "VTLA" in packageSymbol.getValue():
        pin_position = sort_alphanumeric(pin_map.keys())
    else:
        pin_position = sorted(pin_map.keys())

    return (pin_map, pin_position)

def find_cn_pin_name(CnPinNumber):
    import xml.etree.ElementTree as ET

    global pinoutXmlPath
    tree = ET.parse(pinoutXmlPath)
    root = tree.getroot()

    for myPins in root.findall('pins'):
        for myPin in myPins.findall('pin'):
           # if myPin.get("name") != "NC":
            for myFunctions in myPin.findall('function'):
                if myFunctions.get("name") == "CN" + str(CnPinNumber):
                    return myPin.get("name")

###################################################################################################
######################################### GPIO Main Menu  ##########################################
###################################################################################################

pioMenu = coreComponent.createMenuSymbol("GPIO_MENU", None)
pioMenu.setLabel("Ports (GPIO)")
pioMenu.setDescription("Configuration for GPIO PLIB")

pioEnable = coreComponent.createBooleanSymbol("GPIO_ENABLE", pioMenu)
pioEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
pioEnable.setLabel("Use GPIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)

pinConfiguration = coreComponent.createMenuSymbol("GPIO_PIN_CONFIGURATION", pioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuration for GPIO Pins")

# Needed to map port system APIs to PLIB APIs
pioSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
pioSymAPI_Prefix.setDefaultValue("GPIO")
pioSymAPI_Prefix.setVisible(False)

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################
global pin
pin = []
pinName = []
pinType = []
pinPeripheralFunction = []
global pinBitPosition
pinBitPosition = []
global pinChannel
pinChannel = []
global pinDirection
pinDirection = []
global pinLatch
pinLatch = []
pinOpenDrain = []
pinPullUp = []
pinPullDown = []
global pinInterrupt
pinInterrupt = []
CnPin = []
pinGlitchFilter = []
pinFunctionTypelList = []
pinInterruptList = []

pinMode = []

# parse XML
global pinoutXmlPath
currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
deviceXmlPath = os.path.join(currentPath, "../plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
deviceXmlTree = ET.parse(deviceXmlPath)
deviceXmlRoot = deviceXmlTree.getroot()
pinoutXmlName = deviceXmlRoot.get("pins")
pinoutXmlPath = os.path.join(currentPath, "../plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
pinoutXmlPath = os.path.normpath(pinoutXmlPath)
tree = ET.parse(pinoutXmlPath)
root = tree.getroot()

# Build package-id map
for myPackages in root.findall('packages'):
    for myPackage in myPackages.findall('package'):
        packageIdMap[myPackage.get("name")] = myPackage.get("id")

pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, packageIdMap.keys())
pioPackage.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(False)
pioPackage.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

global packagePinCount
packagePinCount = int(re.findall(r'\d+', pinoutXmlName)[0])

pinTotalPins = coreComponent.createIntegerSymbol("GPIO_PIN_TOTAL" , pinConfiguration)
pinTotalPins.setVisible(False)
pinTotalPins.setDefaultValue(packagePinCount)

#build pins position-pad map (pin_map)
pin_map, pin_position = createPinMap(pioPackage)

# Note that all the lists below starts from 0th index and goes till "packagePinCount-1"
# But actual pin numbers on the device starts from 1 (not from 0) and goes till "packagePinCount"
# that is why "pinNumber-1" is used to index the lists wherever applicable.

for pinNumber in range(1, packagePinCount + 1):
    pin.append(pinNumber)
    pin[pinNumber-1]= coreComponent.createMenuSymbol("GPIO_PIN_CONFIGURATION" + str(pinNumber - 1), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pinNumber))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pinNumber-1))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(False)


    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(False)
    #pinType[pinNumber-1].setDependencies(pinFunctionCal, ["PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION"])

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(False)

    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
    pinChannel[pinNumber-1].setReadOnly(False)
    if len(pin_position) > pinNumber-1:# This if condition is to handle the case when same device has two package options with different pin counts
        if pin_map.get(pin_position[pinNumber-1]).startswith("R"):
            # populate pioSymChannel list
            if  pin_map.get(pin_position[pinNumber-1])[1] in pioSymChannel:
                pass
            else:
                pioSymChannel.append(pin_map.get(pin_position[pinNumber-1])[1])
            # Assign channel and bit position value for each pin
            pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]))
            pinChannel[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])

            availablePinDictionary[str(pinNumber)] = "R" + str(pinChannel[pinNumber-1].getValue()) + str(pinBitPosition[pinNumber-1].getValue())
    else:
        pin[pinNumber-1].setVisible(False)

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(False)
    pinDirection[pinNumber-1].setDependencies(pinDirCal, ["BSP_PIN_" + str(pinNumber) + "_DIR" ])

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(False)
    pinLatch[pinNumber-1].setDefaultValue("")
    pinLatch[pinNumber-1].setDependencies(pinLatchCal, ["BSP_PIN_" + str(pinNumber) + "_LAT"])

    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    pinOpenDrain[pinNumber-1].setReadOnly(False)
    pinOpenDrain[pinNumber-1].setDependencies(pinOpenDrainCal, ["BSP_PIN_" + str(pinNumber) + "_OD"])

    #list created only for dependency
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "BSP_PIN_" + str(pinNumber) + "_CN"

pinModeConfiguration = coreComponent.createMenuSymbol("PIN_MODE_CONFIGURATION", pioEnable)
pinModeConfiguration.setLabel("Pin Mode Configuration")

node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/parameters/param@[name=\"AN_PIN_COUNT\"]")
AnPinCount = int(node.getAttribute("value"))

for AnPinNumber in range(0, AnPinCount):
    pinMode.append(AnPinNumber)
    pinMode[AnPinNumber] = coreComponent.createStringSymbol("BSP_PIN_" + str(AnPinNumber) + "_MODE", pinModeConfiguration)
    pinMode[AnPinNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinMode[AnPinNumber].setLabel("Pin AN"+ str(AnPinNumber) + " Mode")
    pinMode[AnPinNumber].setDefaultValue("ANALOG")
    pinMode[AnPinNumber].setReadOnly(False)
    pinMode[AnPinNumber].setDependencies(pinModeCal, ["BSP_PIN_" + str(AnPinNumber) + "_MODE" ])

CnPinConfiguration = coreComponent.createMenuSymbol("CN_PIN_CONFIGURATION", pioEnable)
CnPinConfiguration.setLabel("Change Notice Pin Configuration")

global CnPinCount
node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/parameters/param@[name=\"CN_PIN_COUNT\"]")
CnPinCount = int(node.getAttribute("value"))

CnPinTotal = coreComponent.createIntegerSymbol("CN_PIN_TOTAL" , CnPinConfiguration)
CnPinTotal.setVisible(False)
CnPinTotal.setDefaultValue(CnPinCount)

for CnPinNumber in range(0, CnPinCount):
    CnPin.append(CnPinNumber)
    CnPin[CnPinNumber] = coreComponent.createMenuSymbol("CN" + str(CnPinNumber) + "_PIN_CONFIGURATION", CnPinConfiguration)
    CnPin[CnPinNumber].setLabel("CN" + str(CnPinNumber) + " Pin")

    pinInterrupt.append(CnPinNumber)
    pinInterrupt[CnPinNumber] = coreComponent.createStringSymbol("BSP_PIN_" + str(CnPinNumber) + "_CN", CnPin[CnPinNumber])
    pinInterrupt[CnPinNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinInterrupt[CnPinNumber].setLabel("Change Notice Interrupt")
    pinInterrupt[CnPinNumber].setReadOnly(False)
    pinInterrupt[CnPinNumber].setDependencies(pinInterruptCal, ["BSP_PIN_" + str(CnPinNumber) + "_CN"])

    pinName.append(CnPinNumber)
    pinName[CnPinNumber] = coreComponent.createStringSymbol("CN_PIN_" + str(CnPinNumber) + "_NAME", CnPin[CnPinNumber])
    pinName[CnPinNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinName[CnPinNumber].setLabel("CN Pin Name")
    pinName[CnPinNumber].setDefaultValue("GPIO_PIN_" + find_cn_pin_name(CnPinNumber))
    pinName[CnPinNumber].setReadOnly(True)
    pinName[CnPinNumber].setVisible(True)

    pinPullUp.append(CnPinNumber)
    pinPullUp[CnPinNumber] = coreComponent.createStringSymbol("BSP_PIN_" + str(CnPinNumber) + "_PU", CnPin[CnPinNumber])
    pinPullUp[CnPinNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    pinPullUp[CnPinNumber].setLabel("Pull Up")
    pinPullUp[CnPinNumber].setReadOnly(False)
    pinPullUp[CnPinNumber].setDependencies(pinPullUpCal, ["BSP_PIN_" + str(CnPinNumber) + "_PU"])

pioSymChannel.sort()

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

channelConfiguration = coreComponent.createMenuSymbol("CHANNEL_CONFIGURATION", pioEnable)
channelConfiguration.setLabel("Channel Configuration")

gpioChannelName = []

port = []

global portInterrupt
portInterrupt = []
global gpioSym_GPIO_CNPU

global gpioSym_GPIO_CNPD
gpioSym_GPIO_CNPD = []
global gpioSym_GPIO_TRIS
gpioSym_GPIO_TRIS =[]
global gpioSym_GPIO_LAT
gpioSym_GPIO_LAT =[]
global gpioSym_GPIO_ODC
gpioSym_GPIO_ODC=[]
global gpioSym_GPIO_AD1PCFG

global gpioSym_GPIO_CNEN


gpioTotalChannels = coreComponent.createIntegerSymbol("GPIO_CHANNEL_TOTAL" , channelConfiguration)
gpioTotalChannels.setVisible(False)
gpioTotalChannels.setDefaultValue(len(pioSymChannel))

interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
for interrupt in range (0, len(interruptsChildrenList)):
    vName = str(interruptsChildrenList[interrupt].getAttribute("name"))
    if "CHANGE_NOTICE" in vName:
        irqNumber = int(interruptsChildrenList[interrupt].getAttribute("irq-index"))

# This symbol gives which IFS/IEC register should be used for CN interrupt handling.
# it is assumed (true for all the existing MIPS mask) that all the CN interrupts belong to same IFS/IEC register.
gpioSym_IFS_RegIndex = coreComponent.createStringSymbol("SYS_PORT_IFS_REG_INDEX", pioEnable)
gpioSym_IFS_RegIndex.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
gpioSym_IFS_RegIndex.setLabel("IFS Register Index")
gpioSym_IFS_RegIndex.setDefaultValue(str((int(irqNumber))/32))
gpioSym_IFS_RegIndex.setReadOnly(True)
gpioSym_IFS_RegIndex.setVisible(False)

for portNumber in range(0, len(pioSymChannel)):

    gpioChannelName.append(portNumber)
    gpioChannelName[portNumber] = coreComponent.createStringSymbol("GPIO_CHANNEL_" + str(portNumber) + "_NAME" , channelConfiguration)
    gpioChannelName[portNumber].setVisible(False)
    gpioChannelName[portNumber].setDefaultValue(pioSymChannel[portNumber])

    port.append(portNumber)
    port[portNumber] = coreComponent.createMenuSymbol("PORT_CONFIGURATION" + str(portNumber), channelConfiguration)
    port[portNumber].setLabel("PORT " + pioSymChannel[portNumber] + " Configuration")

    gpioSym_GPIO_TRIS.append(portNumber)
    gpioSym_GPIO_TRIS[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_TRIS", port[portNumber])
    gpioSym_GPIO_TRIS[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    gpioSym_GPIO_TRIS[portNumber].setLabel("TRIS" + str(pioSymChannel[portNumber]) + "CLR" + " Value")
    gpioSym_GPIO_TRIS[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_TRIS[portNumber].setReadOnly(False)

    gpioSym_GPIO_LAT.append(portNumber)
    gpioSym_GPIO_LAT[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_LAT", port[portNumber])
    gpioSym_GPIO_LAT[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    gpioSym_GPIO_LAT[portNumber].setLabel("LAT" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_LAT[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_LAT[portNumber].setReadOnly(False)

    gpioSym_GPIO_ODC.append(portNumber)
    gpioSym_GPIO_ODC[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ODC", port[portNumber])
    gpioSym_GPIO_ODC[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
    gpioSym_GPIO_ODC[portNumber].setLabel("ODC" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_ODC[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_ODC[portNumber].setReadOnly(False)

gpioSym_GPIO_AD1PCFG = coreComponent.createHexSymbol("SYS_PORT_AD1PCFG", channelConfiguration)
gpioSym_GPIO_AD1PCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
gpioSym_GPIO_AD1PCFG.setLabel("AD1PCFG Value")
gpioSym_GPIO_AD1PCFG.setDefaultValue(0x00000000)
gpioSym_GPIO_AD1PCFG.setReadOnly(False)

gpioSym_GPIO_CNEN = coreComponent.createHexSymbol("SYS_PORT_CNEN", channelConfiguration)
gpioSym_GPIO_CNEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
gpioSym_GPIO_CNEN.setLabel("CNEN Value")
gpioSym_GPIO_CNEN.setDefaultValue(0x00000000)
gpioSym_GPIO_CNEN.setReadOnly(False)

gpioSym_GPIO_CNPU = coreComponent.createHexSymbol("SYS_PORT_CNPUE", channelConfiguration)
gpioSym_GPIO_CNPU.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
gpioSym_GPIO_CNPU.setLabel("CNPUE Value")
gpioSym_GPIO_CNPU.setDefaultValue(0x00000000)
gpioSym_GPIO_CNPU.setReadOnly(False)

global entireInterrupt
entireInterrupt = coreComponent.createBooleanSymbol("SYS_PORT_ATLEAST_ONE_CN_USED", CnPinConfiguration)
entireInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_01166;register:%NOREGISTER%")
entireInterrupt.setDefaultValue(False)
entireInterrupt.setLabel("At Least One CN Interrupt is Used")
entireInterrupt.setVisible(True)
entireInterrupt.setReadOnly(True)

# Dependency Status for interrupt
pioSymIntEnComment = coreComponent.createCommentSymbol("SYS_PORT_NVIC_ENABLE_COMMENT", pioMenu)
pioSymIntEnComment.setVisible(False)
pioSymIntEnComment.setLabel("Warning!!! GPIO (Change Notice) Interrupt is Disabled in Interrupt Manager")
pioSymIntEnComment.setDependencies(InterruptStatusWarning, ["core.CHANGE_NOTICE_INTERRUPT_ENABLE_UPDATE", "SYS_PORT_ATLEAST_ONE_CN_USED"])

# Interrupt Dynamic settings
pioSymInterruptControl = coreComponent.createBooleanSymbol("EVIC_GPIO_ENABLE", pioMenu)
pioSymInterruptControl.setDependencies(pioInterruptControl, ["SYS_PORT_ATLEAST_ONE_CN_USED"])
pioSymInterruptControl.setVisible(False)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pioHeaderFile = coreComponent.createFileSymbol("GPIO_HEADER", None)
pioHeaderFile.setSourcePath("../peripheral/gpio_01166/templates/plib_gpio.h.ftl")
pioHeaderFile.setOutputName("plib_gpio.h")
pioHeaderFile.setDestPath("/peripheral/gpio/")
pioHeaderFile.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioHeaderFile.setType("HEADER")
pioHeaderFile.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol("GPIO_SOURCE", None)
pioSource1File.setSourcePath("../peripheral/gpio_01166/templates/plib_gpio.c.ftl")
pioSource1File.setOutputName("plib_gpio.c")
pioSource1File.setDestPath("/peripheral/gpio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)


pioSystemInitFile = coreComponent.createFileSymbol("GPIO_INIT", None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE1")
pioSystemInitFile.setSourcePath("../peripheral/gpio_01166/templates/system/initialization.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol("GPIO_DEF", None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/gpio_01166/templates/system/definitions.h.ftl")
pioSystemDefFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("GPIO_BSP_H", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/gpio_01166/templates/plib_gpio_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("GPIO_BSP_C", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspIncludeFile.setSourcePath("../peripheral/gpio_01166/templates/plib_gpio_bsp.c.ftl")
bspIncludeFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("GPIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/gpio_01166/templates/plib_gpio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)
