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
global pinHasAnalogFunctionMap
pinHasAnalogFunctionMap = {}
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
    global portInterrupt
    channelIndex = pioSymChannel.index((symbol.getID()).split("_")[2])
    if portInterrupt[channelIndex].getValue() == True and Database.getSymbolValue("core", pioSymInterruptVectorUpdate[channelIndex]) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def PPSOptionsVisibilityControl(symbol, event):
    symbol.setVisible(event["value"] )

def ppsInputPinValueUpdate(symbol, event):
    import xml.etree.ElementTree as ET

    global ppsXmlPath
    tree = ET.parse(ppsXmlPath)
    root = tree.getroot()

    if "USE_PPS_INPUT_" in event["id"]:
        symbol.setVisible(event["value"] )

    ppsNumber = event["id"].split("_")[-1]

    pinName = symbol.getKey(symbol.getValue())
    functionNameIndex = Database.getSymbolValue("core", "SYS_PORT_PPS_INPUT_FUNCTION_" + ppsNumber)
    functionNameSymbol = event["source"].getSymbolByID("SYS_PORT_PPS_INPUT_FUNCTION_" + ppsNumber)
    functionName = functionNameSymbol.getKey(functionNameIndex)

    for myGroups in root.findall('groups'):
        for myGroup in myGroups.findall('group'):
            for myPin in myGroup.findall('pin'):
                if ("value" in myPin.attrib.keys()) and (pinName == myPin.get("name")): # means its group for input pins and pin name matched
                    pinValue = myPin.get("value") # save the pin value
                    for myFunction in myGroup.findall('function'): # Since pin name is found, now search the function within the same group
                        if functionName == myFunction.get("name"):
                            functionValue = myFunction.get("register-name") # if function is found, save it
                            symbol.setKeyValue(pinName, pinValue) # update the pin value
                            functionNameSymbol.setKeyValue(functionName, functionValue) # update the function value
                            return


def ppsOutputPinValueUpdate(symbol, event):
    import xml.etree.ElementTree as ET

    global ppsXmlPath
    tree = ET.parse(ppsXmlPath)
    root = tree.getroot()

    if "USE_PPS_OUTPUT_" in event["id"]:
        symbol.setVisible(event["value"] )

    ppsNumber = event["id"].split("_")[-1]

    pinName = symbol.getKey(symbol.getValue())
    functionNameIndex = Database.getSymbolValue("core", "SYS_PORT_PPS_OUTPUT_FUNCTION_" + ppsNumber)
    functionNameSymbol = event["source"].getSymbolByID("SYS_PORT_PPS_OUTPUT_FUNCTION_" + ppsNumber)
    functionName = functionNameSymbol.getKey(functionNameIndex)

    for myGroups in root.findall('groups'):
        for myGroup in myGroups.findall('group'):
            for myPin in myGroup.findall('pin'):
                if ("register-name" in myPin.attrib.keys()) and (pinName == myPin.get("name")): # means its group for output pins and pin name matched
                    pinValue = myPin.get("register-name") # save the pin value
                    for myFunction in myGroup.findall('function'): # Since pin name is found, now search the function within the same group
                        if functionName == myFunction.get("name"):
                            functionValue = myFunction.get("value") # if function is found, save it
                            symbol.setKeyValue(pinName, pinValue) # update the function value
                            functionNameSymbol.setKeyValue(functionName, functionValue) # update the pin value
                            return


# Dependency Function to pass interrupt related info to Interrupt Manager.
# This function will be entered only by internal change happening to PORT channel interrupt, never by manual
# change because channel interrupt is not user configurable directly.
def pioInterruptControl(pioInterrupt, event):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    # Split the id name by "_" and put all the split names in the list "i"
    i = event["id"].split("_")
    k = pioSymChannel.index(i[2])

    Database.setSymbolValue("core", pioSymInterruptVector[k], event["value"], 1)
    Database.setSymbolValue("core", pioSymInterruptHandlerLock[k], event["value"], 1)

    if event["value"] == True:
        Database.setSymbolValue("core", pioSymInterruptHandler[k], "CHANGE_NOTICE_" + i[2] + "_InterruptHandler", 1)
    else :
        Database.setSymbolValue("core", pioSymInterruptHandler[k], "CHANGE_NOTICE_" + i[2] + "_Handler", 1)

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
    global gpioSym_GPIO_ANSEL
    global pinChannel
    global pinBitPosition
    global pinLatch

    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "" and portChannel != "None":
        bit_pos = pinBitPosition[pin_num-1].getValue()
        if pinHasAnalogFunctionMap.get("R" + portChannel + str(bit_pos)) == True:
            channelIndex = pioSymChannel.index(portChannel)
            ANSEL_Value = gpioSym_GPIO_ANSEL[channelIndex].getValue()

            if event["value"] == "DIGITAL":
                ANSEL_Value |= 1 << bit_pos
            else:
                ANSEL_Value &= ~(1 << bit_pos)
            gpioSym_GPIO_ANSEL[channelIndex].setValue(ANSEL_Value, 2)

def pinInterruptCal(pin, event):
    global gpioSym_GPIO_CNEN
    global pinChannel

    pin_num = int((event["id"]).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)

        boolValue = True
        if event["value"] == "":
            # if interrupt has been disabled for a particular pin, then see if is it disabled for all the pins of
            # corresponding channel; if so, then uncheck corresponding port interrupt in GUI.
            boolValue = False
            for pinNumber in range(1, packagePinCount+1):
                if portChannel == pinChannel[pinNumber-1].getValue():
                    if pinInterrupt[pinNumber-1].getValue() != "":
                        boolValue = True
                        break
        portInterrupt[channelIndex].setValue(boolValue, 1)

        bit_pos = pinBitPosition[pin_num-1].getValue()
        CNEN_Value = gpioSym_GPIO_CNEN[channelIndex].getValue()

        if event["value"] == "True":
            CNEN_Value |= 1 << bit_pos
        else:
            CNEN_Value &= ~(1 << bit_pos)

        gpioSym_GPIO_CNEN[channelIndex].setValue(CNEN_Value, 2)

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
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        CNPU_Value = gpioSym_GPIO_CNPU[channelIndex].getValue()

        if event["value"] == "True":
            CNPU_Value |= 1 << bit_pos
        else:
            CNPU_Value &= ~(1 << bit_pos)

        gpioSym_GPIO_CNPU[channelIndex].setValue(CNPU_Value, 2)

def pinPullDownCal(pin, event):
    global gpioSym_GPIO_CNPD
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        CNPD_Value = gpioSym_GPIO_CNPD[channelIndex].getValue()

        if event["value"] == "True":
            CNPD_Value |= 1 << bit_pos
        else:
            CNPD_Value &= ~(1 << bit_pos)

        gpioSym_GPIO_CNPD[channelIndex].setValue(CNPD_Value, 2)


def pinSlewRateCal(pin, event):
    global gpioSym_GPIO_SRCON0
    global gpioSym_GPIO_SRCON1    
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        SRCON0_Value = gpioSym_GPIO_SRCON0[channelIndex].getValue()
        SRCON1_Value = gpioSym_GPIO_SRCON1[channelIndex].getValue()

        if event["value"] == 0: #"Fastest Edge Rate"
            SRCON0_Value &= ~(1 << bit_pos)
            SRCON1_Value &= ~(1 << bit_pos)
        elif event["value"] == 1: #"Medium Edge Rate"
            SRCON1_Value &= ~(1 << bit_pos)
            SRCON0_Value |= 1 << bit_pos 
        elif event["value"] == 2: #"Slow Edge Rate"
            SRCON0_Value &= ~(1 << bit_pos)
            SRCON1_Value |= 1 << bit_pos 
        elif event["value"] == 3: #"Slowest Edge Rate"
            SRCON0_Value |= 1 << bit_pos
            SRCON1_Value |= 1 << bit_pos            
        gpioSym_GPIO_SRCON0[channelIndex].setValue(SRCON0_Value, 2)
        gpioSym_GPIO_SRCON1[channelIndex].setValue(SRCON1_Value, 2)

def packageChange(packageSymbol, event):
    import re

    global pin
    global pinChannel
    global pinBitPosition

    pin_map, pin_position  = createPinMap(packageSymbol)

    for pinNumber in range(0, len(pin_map)):
        pin[pinNumber].setLabel("Pin " + str(pin_position[pinNumber]))
        pinBitPosition[pinNumber].setValue(-1, 2)
        pinChannel[pinNumber].setValue("", 2)
        if len(pin_map.get(pin_position[pinNumber])) in [3,4] and pin_map.get(pin_position[pinNumber]).startswith("R") and pin_map.get(pin_position[pinNumber])[2].isnumeric():
            pinBitPosition[pinNumber].setValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber]))[0]), 2)
            pinChannel[pinNumber].setValue(pin_map.get(pin_position[pinNumber])[1], 2)

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
    global pinHasAnalogFunctionMap
    pinHasAnalogFunctionMap = {}

    tree = ET.parse(pinoutXmlPath)
    root = tree.getroot()

    for myPins in root.findall('pins'):
        for myPin in myPins.findall('pin'):
            pinHasAnalogFunctionMap[myPin.get("name")] = False
            for myFunction in myPin.findall('function'):
                if myFunction.get("name").startswith("AN") and myFunction.get("name")[-1].isnumeric():
                    pinHasAnalogFunctionMap[myPin.get("name")] = True
                    break               

            for myPackageNumber in myPin.findall('number'):
                if packageIdMap.get(packageSymbol.getValue()) == myPackageNumber.get("package"):
                    if "BGA" or "VTLA" or "DQFN" in packageSymbol.getValue():
                        pin_map[myPackageNumber.get("pin")] = myPin.get("name")
                    else:
                        pin_map[int(myPackageNumber.get("pin"))] = myPin.get("name")

    if "BGA" or "VTLA" or "DQFN" in packageSymbol.getValue():
        pin_position = sort_alphanumeric(pin_map.keys())
    else:
        pin_position = sorted(pin_map.keys())

    return (pin_map, pin_position)

###################################################################################################
######################################### GPIO Main Menu  ##########################################
###################################################################################################

pioMenu = coreComponent.createMenuSymbol("GPIO_MENU", None)
pioMenu.setLabel("Ports (GPIO)")
pioMenu.setDescription("Configuration for GPIO PLIB")

pioEnable = coreComponent.createBooleanSymbol("GPIO_ENABLE", pioMenu)
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
pinSlewRate = []
global pinInterrupt
pinInterrupt = []
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
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(False)
pioPackage.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

global packagePinCount
packagePinCount = int((re.findall(r'_\d+', pinoutXmlName)[0])[1:])

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
    pin[pinNumber-1]= coreComponent.createMenuSymbol("GPIO_PIN_CONFIGURATION" + str(pinNumber), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pin_position[pinNumber-1]))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pinNumber-1))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(False)


    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(False)
    #pinType[pinNumber-1].setDependencies(pinFunctionCal, ["PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION"])

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(False)

    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
    pinChannel[pinNumber-1].setReadOnly(False)
    if len(pin_map.get(pin_position[pinNumber-1])) in [3,4] and pin_map.get(pin_position[pinNumber-1]).startswith("R") and pin_map.get(pin_position[pinNumber-1])[2].isnumeric():
        # populate pioSymChannel list
        if  pin_map.get(pin_position[pinNumber-1])[1] in pioSymChannel:
            pass
        else:
            pioSymChannel.append(pin_map.get(pin_position[pinNumber-1])[1])
        # Assign channel and bit position value for each pin
        pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]))
        pinChannel[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])

        availablePinDictionary[str(pinNumber)] = "R" + str(pinChannel[pinNumber-1].getValue()) + str(pinBitPosition[pinNumber-1].getValue())

    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setLabel("Mode")
    pinMode[pinNumber-1].setDefaultValue("")
    pinMode[pinNumber-1].setReadOnly(False)
    pinMode[pinNumber-1].setDependencies(pinModeCal, ["BSP_PIN_" + str(pinNumber) + "_MODE" ])

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(False)
    pinDirection[pinNumber-1].setDependencies(pinDirCal, ["BSP_PIN_" + str(pinNumber) + "_DIR" ])

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(False)
    pinLatch[pinNumber-1].setDefaultValue("")
    pinLatch[pinNumber-1].setDependencies(pinLatchCal, ["BSP_PIN_" + str(pinNumber) + "_LAT"])

    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    pinOpenDrain[pinNumber-1].setReadOnly(False)
    pinOpenDrain[pinNumber-1].setDependencies(pinOpenDrainCal, ["BSP_PIN_" + str(pinNumber) + "_OD"])

    pinInterrupt.append(pinNumber)
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_CN", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("Change Notice")
    pinInterrupt[pinNumber-1].setReadOnly(False)
    pinInterrupt[pinNumber-1].setDependencies(pinInterruptCal, ["BSP_PIN_" + str(pinNumber) + "_CN"])

    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PU", pin[pinNumber-1])
    pinPullUp[pinNumber-1].setLabel("Pull Up")
    pinPullUp[pinNumber-1].setReadOnly(False)
    pinPullUp[pinNumber-1].setDependencies(pinPullUpCal, ["BSP_PIN_" + str(pinNumber) + "_PU"])

    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PD", pin[pinNumber-1])
    pinPullDown[pinNumber-1].setLabel("Pull Down")
    pinPullDown[pinNumber-1].setReadOnly(False)
    pinPullDown[pinNumber-1].setDependencies(pinPullDownCal, ["BSP_PIN_" + str(pinNumber) + "_PD"])

    pinSlewRate.append(pinNumber)
    pinSlewRate[pinNumber-1] = coreComponent.createKeyValueSetSymbol("BSP_PIN_" + str(pinNumber) + "_SR", pin[pinNumber-1])
    pinSlewRate[pinNumber-1].setLabel("Slew Rate")
    pinSlewRate[pinNumber-1].setReadOnly(False)
    pinSlewRate[pinNumber-1].setOutputMode("Value")
    pinSlewRate[pinNumber-1].setDisplayMode("Key")
    pinSlewRate[pinNumber-1].setDefaultValue(0)
    pinSlewRate[pinNumber-1].setVisible(True)
    pinSlewRate[pinNumber-1].addKey("Fastest Edge Rate", "0x0", "Fastest Edge Rate (Slew Rate Control Disabled)")
    pinSlewRate[pinNumber-1].addKey("Medium Edge Rate", "0x1", "Medium Edge Rate")
    pinSlewRate[pinNumber-1].addKey("Slow Edge Rate", "0x2", "Slow Edge Rate")
    pinSlewRate[pinNumber-1].addKey("Slowest Edge Rate", "0x3", "Slowest Edge Rate")
    pinSlewRate[pinNumber-1].setDependencies(pinSlewRateCal, ["BSP_PIN_" + str(pinNumber) + "_SR"])

    #list created only for dependency
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "BSP_PIN_" + str(pinNumber) + "_CN"

###################################################################################################
################################# PPS Pins Configuration related code #################################
###################################################################################################
pioSymChannel.sort()

PPSPinCount = 60

ppsPinInputConfiguration= coreComponent.createMenuSymbol("GPIO_PPS_PIN_INPUT_CONFIGURATION", pioEnable)
ppsPinInputConfiguration.setLabel("PPS Input Pin Configuration")

ppsPinOutputConfiguration= coreComponent.createMenuSymbol("GPIO_PPS_PIN_OUTPUT_CONFIGURATION", pioEnable)
ppsPinOutputConfiguration.setLabel("PPS Output Pin Configuration")

#Number of PPS input/output pins
gpioSymPPSPinCount = coreComponent.createIntegerSymbol("PPS_PIN_COUNT", pioEnable)
gpioSymPPSPinCount.setLabel("PPS Pin Count")
gpioSymPPSPinCount.setDefaultValue(PPSPinCount)
gpioSymPPSPinCount.setReadOnly(False)
gpioSymPPSPinCount.setVisible(False)

ppsInputEnable = []
ppsInputFunction = []
ppsInputPin = []
ppsOutputEnable = []
ppsOutputFunction = []
ppsOutputPin = []
ppsInputPinMap = {}
ppsOutputFunctionMap = {}
global PORTS_REMAP_OUTPUT_PIN
PORTS_REMAP_OUTPUT_PIN = {}
PORTS_REMAP_INPUT_FUNCTION= {}

# parse XML and populate PPS lists and dictionaries
global ppsXmlPath
ppsXmlName = deviceXmlRoot.get("families")
ppsXmlPath = os.path.join(currentPath, "../plugin/pin_xml/families/" + ppsXmlName + ".xml")
ppsXmlPath = os.path.normpath(ppsXmlPath)

tree = ET.parse(ppsXmlPath)
root = tree.getroot()

for myGroups in root.findall('groups'):
    for myGroup in myGroups.findall('group'):
        for myPin in myGroup.findall('pin'):
            if "value" in myPin.attrib.keys(): # means its group for input pins
                ppsInputPinMap[myPin.get("name")] = myPin.get("value")
            elif "register-name" in myPin.attrib.keys(): # means its group for output pins
                PORTS_REMAP_OUTPUT_PIN[myPin.get("name")] = myPin.get("register-name")
        for myFunction in myGroup.findall('function'):
            if "value" in myFunction.attrib.keys():  # means its group for output functions
                ppsOutputFunctionMap[myFunction.get("name")] = myFunction.get("value")
            elif "register-name" in myFunction.attrib.keys():  # means its group for input functions
                PORTS_REMAP_INPUT_FUNCTION[myFunction.get("name")] = myFunction.get("register-name")

for pinNumber in range(0, PPSPinCount):

    #PPS input pin Configuration
    ppsInputEnable.append(pinNumber)
    ppsInputEnable[pinNumber] = coreComponent.createBooleanSymbol("USE_PPS_INPUT_" + str(pinNumber), ppsPinInputConfiguration)
    ppsInputEnable[pinNumber].setLabel("USE PPS Input" + str(pinNumber))
    ppsInputEnable[pinNumber].setDefaultValue(False)
    ppsInputEnable[pinNumber].setReadOnly(False)

    ppsInputFunction.append(pinNumber)
    ppsInputFunction[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_INPUT_FUNCTION_" + str(pinNumber), ppsInputEnable[pinNumber])
    ppsInputFunction[pinNumber].setLabel("Function")
    ppsInputFunction[pinNumber].setOutputMode("Value")
    ppsInputFunction[pinNumber].setDisplayMode("Key")
    ppsInputFunction[pinNumber].setDefaultValue(0)    
    ppsInputFunction[pinNumber].setReadOnly(False)
    ppsInputFunction[pinNumber].setVisible(False)
    for key, value in PORTS_REMAP_INPUT_FUNCTION.items():
        ppsInputFunction[pinNumber].addKey(key, value, value)
    ppsInputFunction[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_INPUT_" + str(pinNumber)])

    
    ppsInputPin.append(pinNumber)
    ppsInputPin[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_INPUT_PIN_" + str(pinNumber), ppsInputEnable[pinNumber])
    ppsInputPin[pinNumber].setLabel("Pin")
    ppsInputPin[pinNumber].setOutputMode("Value")
    ppsInputPin[pinNumber].setDisplayMode("Key")
    ppsInputPin[pinNumber].setDefaultValue(0)
    ppsInputPin[pinNumber].setReadOnly(False)
    ppsInputPin[pinNumber].setVisible(False)
    for key, value in ppsInputPinMap.items():
        ppsInputPin[pinNumber].addKey(key, value, key)
    ppsInputPin[pinNumber].setDependencies(ppsInputPinValueUpdate, ["SYS_PORT_PPS_INPUT_FUNCTION_" + str(pinNumber), "USE_PPS_INPUT_" + str(pinNumber), "SYS_PORT_PPS_INPUT_PIN_" + str(pinNumber)])
    

    #PPS Output pin Configuration
    ppsOutputEnable.append(pinNumber)
    ppsOutputEnable[pinNumber] = coreComponent.createBooleanSymbol("USE_PPS_OUTPUT_" + str(pinNumber), ppsPinOutputConfiguration)
    ppsOutputEnable[pinNumber].setLabel("USE PPS Output" + str(pinNumber))
    ppsOutputEnable[pinNumber].setDefaultValue(False)
    ppsOutputEnable[pinNumber].setReadOnly(False)

    
    ppsOutputFunction.append(pinNumber)
    ppsOutputFunction[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber), ppsOutputEnable[pinNumber])
    ppsOutputFunction[pinNumber].setLabel("Function")
    ppsOutputFunction[pinNumber].setOutputMode("Value")
    ppsOutputFunction[pinNumber].setDisplayMode("Key")
    ppsOutputFunction[pinNumber].setDefaultValue(0)
    ppsOutputFunction[pinNumber].setReadOnly(False)
    ppsOutputFunction[pinNumber].setVisible(False)
    for key, value in ppsOutputFunctionMap.items():
        ppsOutputFunction[pinNumber].addKey(key, value, key)
    ppsOutputFunction[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_OUTPUT_" + str(pinNumber)])
    
    ppsOutputPin.append(pinNumber)
    ppsOutputPin[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_OUTPUT_PIN_" + str(pinNumber), ppsOutputEnable[pinNumber])
    ppsOutputPin[pinNumber].setLabel("Pin")
    ppsOutputPin[pinNumber].setOutputMode("Value")
    ppsOutputPin[pinNumber].setDisplayMode("Key")
    ppsOutputPin[pinNumber].setDefaultValue(0)    
    ppsOutputPin[pinNumber].setReadOnly(False)
    ppsOutputPin[pinNumber].setVisible(False)
    for key, value in PORTS_REMAP_OUTPUT_PIN.items():
        ppsOutputPin[pinNumber].addKey(key, value, value)
    ppsOutputPin[pinNumber].setDependencies(ppsOutputPinValueUpdate, ["SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber),"USE_PPS_OUTPUT_" + str(pinNumber), "SYS_PORT_PPS_OUTPUT_PIN_" + str(pinNumber)])

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

channelConfiguration = coreComponent.createMenuSymbol("CHANNEL_CONFIGURATION", pioEnable)
channelConfiguration.setLabel("Channel Configuration")

gpioChannelName = []

port = []

portInterruptList = []

global portInterrupt
portInterrupt = []
global portInterruptStyle
portInterruptStyle = []
global gpioSym_GPIO_CNPU
gpioSym_GPIO_CNPU = []
global gpioSym_GPIO_CNPD
gpioSym_GPIO_CNPD = []
global gpioSym_GPIO_TRIS
gpioSym_GPIO_TRIS =[]
global gpioSym_GPIO_LAT
gpioSym_GPIO_LAT =[]
global gpioSym_GPIO_ODC
gpioSym_GPIO_ODC=[]
global gpioSym_GPIO_ANSEL
gpioSym_GPIO_ANSEL =[]
global gpioSym_GPIO_CNEN
gpioSym_GPIO_CNEN =[]

global gpioSym_GPIO_SRCON0
gpioSym_GPIO_SRCON0 =[]
global gpioSym_GPIO_SRCON1
gpioSym_GPIO_SRCON1 =[]

global pioSymInterruptVector
pioSymInterruptVector = []
global pioSymInterruptHandler
pioSymInterruptHandler = []
global pioSymInterruptHandlerLock
pioSymInterruptHandlerLock = []
global pioSymInterruptVectorUpdate
pioSymInterruptVectorUpdate = []
pioSymClkEnComment = []
global pioSymIntEnComment
pioSymIntEnComment = []

gpioTotalChannels = coreComponent.createIntegerSymbol("GPIO_CHANNEL_TOTAL" , channelConfiguration)
gpioTotalChannels.setVisible(False)
gpioTotalChannels.setDefaultValue(len(pioSymChannel))

global intVectorDataDictionary
intVectorDataDictionary = {}

interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
for interrupt in range (0, len(interruptsChildrenList)):
    vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
    vName = str(interruptsChildrenList[interrupt].getAttribute("name"))
    if "CHANGE_NOTICE_" in vName:
        intVectorDataDictionary[vName] = vIndex

for portNumber in range(0, len(pioSymChannel)):

    gpioChannelName.append(portNumber)
    gpioChannelName[portNumber] = coreComponent.createStringSymbol("GPIO_CHANNEL_" + str(portNumber) + "_NAME" , channelConfiguration)
    gpioChannelName[portNumber].setVisible(False)
    gpioChannelName[portNumber].setDefaultValue(pioSymChannel[portNumber])

    port.append(portNumber)
    port[portNumber] = coreComponent.createMenuSymbol("PORT_CONFIGURATION" + str(portNumber), channelConfiguration)
    port[portNumber].setLabel("PORT " + pioSymChannel[portNumber] + " Configuration")

    portInterrupt.append(portNumber)
    portInterrupt[portNumber] = coreComponent.createBooleanSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CN_USED", port[portNumber])
    portInterrupt[portNumber].setLabel("Use Change Notice On PORT " + pioSymChannel[portNumber])
    portInterrupt[portNumber].setDefaultValue(False)
    portInterrupt[portNumber].setVisible(True)
    portInterrupt[portNumber].setReadOnly(True)
    portInterruptStyle.append(portNumber)
    portInterruptStyle[portNumber] = coreComponent.createBooleanSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CN_STYLE", port[portNumber])
    portInterruptStyle[portNumber].setLabel("Use Edge Type Interrupt On PORT " + pioSymChannel[portNumber])
    portInterruptStyle[portNumber].setDescription("if False, mismatch type interrupt will be used; check the box for edge style interrupt")
    portInterruptStyle[portNumber].setDefaultValue(False)
    portInterruptStyle[portNumber].setVisible(True)
    portInterruptStyle[portNumber].setReadOnly(False)

    #list created only for dependency
    portInterruptList.append(portNumber)
    portInterruptList[portNumber] = "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CN_USED"

    gpioSym_GPIO_CNPU.append(portNumber)
    gpioSym_GPIO_CNPU[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPU", port[portNumber])
    gpioSym_GPIO_CNPU[portNumber].setLabel("CNPU" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNPU[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_CNPU[portNumber].setReadOnly(False)

    gpioSym_GPIO_CNPD.append(portNumber)
    gpioSym_GPIO_CNPD[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPD", port[portNumber])
    gpioSym_GPIO_CNPD[portNumber].setLabel("CNPD" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNPD[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_CNPD[portNumber].setReadOnly(False)

    gpioSym_GPIO_TRIS.append(portNumber)
    gpioSym_GPIO_TRIS[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_TRIS", port[portNumber])
    gpioSym_GPIO_TRIS[portNumber].setLabel("TRIS" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_TRIS[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_TRIS[portNumber].setReadOnly(False)

    gpioSym_GPIO_LAT.append(portNumber)
    gpioSym_GPIO_LAT[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_LAT", port[portNumber])
    gpioSym_GPIO_LAT[portNumber].setLabel("LAT" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_LAT[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_LAT[portNumber].setReadOnly(False)

    gpioSym_GPIO_ODC.append(portNumber)
    gpioSym_GPIO_ODC[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ODC", port[portNumber])
    gpioSym_GPIO_ODC[portNumber].setLabel("ODC" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_ODC[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_ODC[portNumber].setReadOnly(False)

    gpioSym_GPIO_ANSEL.append(portNumber)
    gpioSym_GPIO_ANSEL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ANSEL", port[portNumber])
    gpioSym_GPIO_ANSEL[portNumber].setLabel("ANSEL" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_ANSEL[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_ANSEL[portNumber].setReadOnly(False)

    gpioSym_GPIO_CNEN.append(portNumber)
    gpioSym_GPIO_CNEN[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNEN", port[portNumber])
    gpioSym_GPIO_CNEN[portNumber].setLabel("CNEN" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNEN[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_CNEN[portNumber].setReadOnly(False)

    gpioSym_GPIO_SRCON0.append(portNumber)
    gpioSym_GPIO_SRCON0[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_SRCON0", port[portNumber])
    gpioSym_GPIO_SRCON0[portNumber].setLabel("SRCON0" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_SRCON0[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_SRCON0[portNumber].setReadOnly(False)

    gpioSym_GPIO_SRCON1.append(portNumber)
    gpioSym_GPIO_SRCON1[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_SRCON1", port[portNumber])
    gpioSym_GPIO_SRCON1[portNumber].setLabel("SRCON1" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_SRCON1[portNumber].setDefaultValue(0x00000000)
    gpioSym_GPIO_SRCON1[portNumber].setReadOnly(False)

    #symbols and variables for interrupt handling
    pioSymInterruptVector.append(portNumber)
    pioSymInterruptVector[portNumber] = "CHANGE_NOTICE_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_ENABLE"
    pioSymInterruptHandler.append(portNumber)
    pioSymInterruptHandler[portNumber] = "CHANGE_NOTICE_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_HANDLER"
    pioSymInterruptHandlerLock.append(portNumber)
    pioSymInterruptHandlerLock[portNumber] = "CHANGE_NOTICE_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_HANDLER_LOCK"
    pioSymInterruptVectorUpdate.append(portNumber)
    pioSymInterruptVectorUpdate[portNumber] = "CHANGE_NOTICE_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_ENABLE_UPDATE"

    # Dependency Status for interrupt
    pioSymIntEnComment.append(portNumber)
    pioSymIntEnComment[portNumber] = coreComponent.createCommentSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_NVIC_ENABLE_COMMENT", pioMenu)
    pioSymIntEnComment[portNumber].setVisible(False)
    pioSymIntEnComment[portNumber].setLabel("Warning!!! GPIO" + str(pioSymChannel[portNumber]) + " Interrupt is Disabled in Interrupt Manager")
    pioSymIntEnComment[portNumber].setDependencies(InterruptStatusWarning, ["core." + pioSymInterruptVectorUpdate[portNumber], "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CN_USED"])

# Interrupt Dynamic settings
pioSymInterruptControl = coreComponent.createBooleanSymbol("EVIC_GPIO_ENABLE", pioMenu)
pioSymInterruptControl.setDependencies(pioInterruptControl, portInterruptList)
pioSymInterruptControl.setVisible(False)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pioHeaderFile = coreComponent.createFileSymbol("GPIO_HEADER", None)
pioHeaderFile.setSourcePath("../peripheral/gpio_02467/templates/plib_gpio_pic32c.h.ftl")    
pioHeaderFile.setOutputName("plib_gpio.h")
pioHeaderFile.setDestPath("/peripheral/gpio/")
pioHeaderFile.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioHeaderFile.setType("HEADER")
pioHeaderFile.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol("GPIO_SOURCE", None)
pioSource1File.setSourcePath("../peripheral/gpio_02467/templates/plib_gpio_pic32c.c.ftl")
pioSource1File.setOutputName("plib_gpio.c")
pioSource1File.setDestPath("/peripheral/gpio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)


pioSystemInitFile = coreComponent.createFileSymbol("GPIO_INIT", None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE1")
pioSystemInitFile.setSourcePath("../peripheral/gpio_02467/templates/system/initialization.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol("GPIO_DEF", None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/gpio_02467/templates/system/definitions.h.ftl")
pioSystemDefFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("GPIO_BSP_H", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/gpio_02467/templates/plib_gpio_bsp_pic32c.h.ftl")
bspIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("GPIO_BSP_C", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspIncludeFile.setSourcePath("../peripheral/gpio_02467/templates/plib_gpio_bsp.c.ftl")
bspIncludeFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("GPIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/gpio_02467/templates/plib_gpio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)
