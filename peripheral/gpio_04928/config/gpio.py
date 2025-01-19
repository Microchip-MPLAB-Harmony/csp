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

global pioSymChannel # ['A','B','C]
pioSymChannel = []

global packageIdMap
packageIdMap = {} #ex: "TQFP":1, "TFBGA":2
global pin_map
pin_map = {} # map to store Pin nmber and pin name ex:1:RE0
global pinHasAnalogFunctionMap
pinHasAnalogFunctionMap = {} # Map to store ANalog support for every pin {'RB1': True, 'RB0': True}
global pin_position
pin_position = []
global createPinMap
global getAnalogFunctions
global getRegisterInitValue
global availablePinDictionary
availablePinDictionary = {}

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

global getAvailablePins

# API used by core to return available pins to sender component
def getAvailablePins():

    return availablePinDictionary

def getRegisterInitValue(regName):
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPIO\"]/register-group")
    registers = node.getChildren()

    for register in registers:
        if register.getAttribute('name') == regName:
            porValue = register.getAttribute('initval')
            return int(porValue, 16)
    return 0

# To get the child nodes of a register in ATDF
def getRegisterChildren(registerGroup,register):
    atdfPath = '/avr-tools-device-file/modules/module@[name=\"GPIO\"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
    return ATDF.getNode(atdfPath).getChildren()

# Dependency Function to show or hide the warning message
def InterruptStatusWarning(symbol, event):
    global portInterrupt
    channel = str(symbol.getID().split("_")[2])
    channelIndex = pioSymChannel.index(channel)
    intIndex = intVectorDataDictionary['CN'+channel+'Interrupt']

    if portInterrupt[channelIndex].getValue() == True and Database.getSymbolValue("core","INTC_{}_ENABLE".format(intIndex)) == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def PPSOptionsVisibilityControl(symbol, event):
    symbol.setVisible(event["value"] )

# Dependency Function to pass interrupt related info to Interrupt Manager.
def pioInterruptControl(symbol, event):
    channel = str(event["id"].split("_")[2])
    intIndex = intVectorDataDictionary['CN'+channel+'Interrupt']

    if event["value"] == True:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), True)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), True)
    else :
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), False)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), False)

def setIFSValue(portNumber):
    if portNumber <=3:
        return "3"
    return "9"

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

    pin_num = int((pin.getID()).split("_")[2])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "" and portChannel != "None":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        TRIS_Value = gpioSym_GPIO_TRIS[channelIndex].getValue()

        if event["value"] == "Out":
            TRIS_Value &= ~(1 << bit_pos)
        else:
            TRIS_Value |= 1 << bit_pos
        gpioSym_GPIO_TRIS[channelIndex].setValue(TRIS_Value, 2)

def pinModeCal(pin, event):
    global gpioSym_GPIO_ANSEL
    global pinChannel
    global pinBitPosition #list with symbols of bitPos

    pin_num = int((pin.getID()).split("_")[2]) # ex :Extract Pin number from Pin symbol name
    portChannel = pinChannel[pin_num-1].getValue() # get the port of this particular pin

    if portChannel != "" and portChannel != "None":
        bit_pos = pinBitPosition[pin_num-1].getValue() #get the bit position for cur pin
        if pinHasAnalogFunctionMap.get("R" + portChannel + str(bit_pos)) == True:
            channelIndex = pioSymChannel.index(portChannel)
            ANSEL_Value = gpioSym_GPIO_ANSEL[channelIndex].getValue()

            if event["value"] == "DIGITAL":
                ANSEL_Value &= ~(1 << bit_pos) # clear the bit value
            else:
                ANSEL_Value |= 1 << bit_pos # set the bit value
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

        pattern = r"^R[A-Z](\d+)?$"  # Matches R followed by one uppercase letter and optional digits
        pin_name = pin_map.get(pin_position[pinNumber])
        if pin_name and re.match(pattern, pin_name):
            pinBitPosition[pinNumber].setValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber]))[0]), 2) #extract bit pos from pin name. ex: 3 in RA3
            pinChannel[pinNumber].setValue(pin_map.get(pin_position[pinNumber])[1], 2) #extract port from pin name. ex: A in RA3

def getAnalogFunctions():
    import xml.etree.ElementTree as ET

    global familyXmlPath
    tree = ET.parse(familyXmlPath)
    root = tree.getroot()

    # List to store functions with analog functionality
    analogFunctionsList = []

    # Find the modules element
    modules = root.find('modules')

    # Iterate through each module
    for module in modules.findall('module'):
        # Check if the module has the analog attribute set to "true"
        if module.get('analog') == 'true':
            # Iterate through each function in the module
            for function in module.findall('function'):
                # Add the function name to the list
                analogFunctionsList.append(function.get('name'))
        else:
            for function in module.findall('function'):
                if function.get('analog') == 'true':
                    analogFunctionsList.append(function.get('name'))

    return analogFunctionsList

def createPinMap(packageSymbol):
    import xml.etree.ElementTree as ET

    global pinoutXmlPath
    pin_map = {}
    pin_position = []
    global pinHasAnalogFunctionMap
    pinHasAnalogFunctionMap = {}

    tree = ET.parse(pinoutXmlPath)
    root = tree.getroot()

    analogFunctionList = getAnalogFunctions()

    for myPins in root.findall('pins'):  #Iterate in Pins section in Pin.xml
        for myPin in myPins.findall('pin'): #Iterate For all Pin under Pins
            pinHasAnalogFunctionMap[myPin.get("name")] = False  # Add a Pin to map to track if its analog
            for myFunction in myPin.findall('function'): #Iterate in all function names of a pin
                if myFunction.get("name") in analogFunctionList:
                    pinHasAnalogFunctionMap[myPin.get("name")] = True
                    break               

            for myPackageNumber in myPin.findall('number'):
                if packageIdMap.get(packageSymbol.getValue()) == myPackageNumber.get("package"):
                    pin_map[int(myPackageNumber.get("pin"))] = myPin.get("name") # build pin map --> ex: 1:RE0

    pin_position = sorted(pin_map.keys())
    return (pin_map, pin_position)

def checkPortConfiguration(symbol, event):
    # Check if any of the port configuration symbols have changed from their default values
    portChannel = symbol.getID().split("_")[2]

    portSymbols = [
        "SYS_PORT_" + portChannel + "_TRIS",
        "SYS_PORT_" + portChannel + "_LAT",
        "SYS_PORT_" + portChannel + "_ODC",
        "SYS_PORT_" + portChannel + "_ANSEL",
        "SYS_PORT_" + portChannel + "_CNEN",
        "SYS_PORT_" + portChannel + "_CNPU",
        "SYS_PORT_" + portChannel + "_CNPD"
    ]

    for sym in portSymbols:
        if Database.getSymbolValue("core", sym) != getRegisterInitValue(sym.split("_")[-1]+portChannel):
            symbol.setValue(True)
            return

    symbol.setValue(False)

def setOffsetVal(regNameA,regNameB):
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPIO\"]/register-group")
    registers = node.getChildren()

    for register in registers:
        if register.getAttribute('name') == regNameA:
            regAOffsetVal = register.getAttribute('offset')
        elif register.getAttribute('name') == regNameB:
            regBOffsetVal = register.getAttribute('offset')
    return "0x{:X}".format(abs(int(regBOffsetVal, 16) - int(regAOffsetVal, 16)))

def sckPinCallback(symbol,event):
    import re
    flag = False
    if re.search("SCK[0-9]", event["value"]) is not None:
        for pinNumber in range(0, packagePinCount):
            if symbol.getComponent().getSymbolValue("USE_PPS_INPUT_" + str(pinNumber)) == True:
                selectedFunction = symbol.getComponent().getSymbolByID("SYS_PORT_PPS_INPUT_FUNCTION_" + str(pinNumber)).getSelectedKey()
                if event["value"] == selectedFunction:
                    selectedPin = symbol.getComponent().getSymbolByID("SYS_PORT_PPS_INPUT_PIN_" + str(pinNumber)).getSelectedKey()
                    flag = True
            if flag == True:
                for pinNumber in range(0, packagePinCount):
                    if symbol.getComponent().getSymbolValue("USE_PPS_OUTPUT_" + str(pinNumber)) == False:
                        symbol.getComponent().getSymbolByID("USE_PPS_OUTPUT_" + str(pinNumber)).setValue(True)
                        symbol.getComponent().getSymbolByID("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber)).setSelectedKey(selectedFunction)
                        symbol.getComponent().getSymbolByID("SYS_PORT_PPS_OUTPUT_PIN_" + str(pinNumber)).setSelectedKey(selectedPin)
                        break
                    else:
                        if event["value"] == symbol.getComponent().getSymbolByID("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber)).getSelectedKey():
                            break 
                break

    sckList = []

    for pinNumber in range(0, packagePinCount):
        if symbol.getComponent().getSymbolValue("USE_PPS_INPUT_" + str(pinNumber)) == True:
            selectedKey = symbol.getComponent().getSymbolByID("SYS_PORT_PPS_INPUT_FUNCTION_" + str(pinNumber)).getSelectedKey()
            if re.search("SCK[0-9]", selectedKey) is not None:
                sckList.append(selectedKey)

    for pinNumber in range(0, packagePinCount):
        if symbol.getComponent().getSymbolValue("USE_PPS_OUTPUT_" + str(pinNumber)) == True:
            selectedKey = symbol.getComponent().getSymbolByID("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber)).getSelectedKey()
            if selectedKey not in sckList:
                symbol.getComponent().getSymbolByID("USE_PPS_OUTPUT_" + str(pinNumber)).setValue(False)
                break 

###################################################################################################
######################################### GPIO Main Menu  ##########################################
###################################################################################################

pioMenu = coreComponent.createMenuSymbol("GPIO_MENU", None)
pioMenu.setLabel("Ports (GPIO)")
pioMenu.setDescription("Configuration for GPIO PLIB")

pioUsePluginHelp = coreComponent.createCommentSymbol("GPIO_USE_PLUGIN_INLINE_COMMENT",pioMenu)
pioUsePluginHelp.setLabel("Info: Please use the Pin Configuration Plugin to configure the pins.")

pioEnable = coreComponent.createBooleanSymbol("GPIO_ENABLE", pioMenu)
pioEnable.setLabel("Use GPIO PLIB")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)

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
pinGlitchFilter = []
pinFunctionTypelList = []
pinInterruptList = []
global pinNameList
pinNameList = []

pinMode = []

# parse XML
global pinoutXmlPath
currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1])) # get the path of gpio.py file
deviceXmlPath = os.path.join(currentPath, "../plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")  # path to get component.xml ex: dsPIC33AK512MPS512.xml

deviceXmlTree = ET.parse(deviceXmlPath)
deviceXmlRoot = deviceXmlTree.getroot()
pinoutXmlName = deviceXmlRoot.get("pins")
pinoutXmlPath = os.path.join(currentPath, "../plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
pinoutXmlPath = os.path.normpath(pinoutXmlPath)
tree = ET.parse(pinoutXmlPath)
root = tree.getroot()

# Family.xml path
global familyXmlPath
familyXmlName = deviceXmlRoot.get("families")
familyXmlPath = os.path.join(currentPath, "../plugin/pin_xml/families/" + familyXmlName + ".xml")
familyXmlPath = os.path.normpath(familyXmlPath)

# Build package-id map
for myPackages in root.findall('packages'):
    for myPackage in myPackages.findall('package'):
        packageIdMap[myPackage.get("name")] = myPackage.get("id") #ex: {"TQFP":1, "TFBGA":2}
pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, packageIdMap.keys())
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(True)
pioPackage.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

pinConfiguration = coreComponent.createMenuSymbol("GPIO_PIN_CONFIGURATION", pioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuration for GPIO Pins")

global packagePinCount  # store the Pincount of device
packagePinCount = int((re.findall(r'_\d+', pinoutXmlName)[0])[1:])  # ex: fetch the pin count from "AK_MPS_124_pin.xml"

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
    pinName[pinNumber-1].setLabel("Custom Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(True)
    pinType[pinNumber-1].setDependencies(sckPinCallback,["BSP_PIN_" + str(pinNumber) + "_FUNCTION_TYPE"])

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)
    pinBitPosition[pinNumber-1].setVisible(False)

    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PORT_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
    pinChannel[pinNumber-1].setVisible(False)
    pinChannel[pinNumber-1].setReadOnly(True)

    # Define the regex pattern for pin names
    pattern = r"^R[A-Z](\d+)?$"  # Matches R followed by one uppercase letter and optional digits

    # Check if the pin name matches the pattern
    pin_name = pin_map.get(pin_position[pinNumber-1])
    if pin_name and re.match(pattern, pin_name):
        # Populate pioSymChannel list
        if pin_name[1] not in pioSymChannel:  # Port E from RE0 not in list, add it
            pioSymChannel.append(pin_name[1])

        # Assign channel and bit position value for each pin
        pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall(r'\d+', pin_name)[0]))  # 0 in RE0
        pinChannel[pinNumber-1].setDefaultValue(pin_name[1])  # E in RE0
        availablePinDictionary[str(pinNumber)] = "R" + str(pinChannel[pinNumber-1].getValue()) + str(pinBitPosition[pinNumber-1].getValue())

    
    pinNameList.append(pinNumber)
    pinNameList[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PIN_NAME", pin[pinNumber-1])
    pinNameList[pinNumber-1].setLabel("Pin Name")
    pinNameList[pinNumber-1].setDefaultValue(pin_name)
    pinNameList[pinNumber-1].setReadOnly(True)

    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setLabel("Mode")
    pinMode[pinNumber-1].setDefaultValue("")
    pinMode[pinNumber-1].setReadOnly(True)
    pinMode[pinNumber-1].setDependencies(pinModeCal, ["BSP_PIN_" + str(pinNumber) + "_MODE" ])

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(True)
    pinDirection[pinNumber-1].setDependencies(pinDirCal, ["BSP_PIN_" + str(pinNumber) + "_DIR" ])
    pinDirection[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:TRISx")

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(True)
    pinLatch[pinNumber-1].setDefaultValue("")
    pinLatch[pinNumber-1].setDependencies(pinLatchCal, ["BSP_PIN_" + str(pinNumber) + "_LAT"])
    pinDirection[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:LATx")

    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    pinOpenDrain[pinNumber-1].setReadOnly(True)
    pinOpenDrain[pinNumber-1].setDependencies(pinOpenDrainCal, ["BSP_PIN_" + str(pinNumber) + "_OD"])
    pinOpenDrain[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:ODCx")

    pinInterrupt.append(pinNumber)
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_CN", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("Change Notice")
    pinInterrupt[pinNumber-1].setReadOnly(True)
    pinInterrupt[pinNumber-1].setDependencies(pinInterruptCal, ["BSP_PIN_" + str(pinNumber) + "_CN"])
    pinInterrupt[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNEN0x")

    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PU", pin[pinNumber-1])
    pinPullUp[pinNumber-1].setLabel("Pull Up")
    pinPullUp[pinNumber-1].setReadOnly(True)
    pinPullUp[pinNumber-1].setDependencies(pinPullUpCal, ["BSP_PIN_" + str(pinNumber) + "_PU"])
    pinPullUp[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNPUx")

    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber-1] = coreComponent.createStringSymbol("BSP_PIN_" + str(pinNumber) + "_PD", pin[pinNumber-1])
    pinPullDown[pinNumber-1].setLabel("Pull Down")
    pinPullDown[pinNumber-1].setReadOnly(True)
    pinPullDown[pinNumber-1].setDependencies(pinPullDownCal, ["BSP_PIN_" + str(pinNumber) + "_PD"])
    pinPullDown[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNPDx")

    #list created only for dependency
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "BSP_PIN_" + str(pinNumber) + "_CN"

###################################################################################################
################################# PPS Pins Configuration related code #################################
###################################################################################################
pioSymChannel.sort()

PPSPinCount = packagePinCount

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
                ppsInputPinMap[myPin.get("name")] = myPin.get("value") # {"RP1":1}
            elif "register-name" in myPin.attrib.keys(): # means its group for output pins
                PORTS_REMAP_OUTPUT_PIN[myPin.get("name")] = myPin.get("register-name") # {"RP1":"RP1R"}
        for myFunction in myGroup.findall('function'):
            if myFunction.get("direction") == "out" and myFunction.get("value") is not None:
                ppsOutputFunctionMap[myFunction.get("name")] = myFunction.get("value") # output Pin Function map {"CLC10OUT":"78"}
            elif  myFunction.get("direction") == "in" and myFunction.get("register-name") is not None:
                PORTS_REMAP_INPUT_FUNCTION[myFunction.get("name")] = myFunction.get("register-name") + "bits." + myFunction.get("name") # Input Pin function map {"CLC10OUT":"78"}

for pinNumber in range(0,packagePinCount):

    #PPS input pin Configuration
    ppsInputEnable.append(pinNumber)
    ppsInputEnable[pinNumber] = coreComponent.createBooleanSymbol("USE_PPS_INPUT_" + str(pinNumber), ppsPinInputConfiguration)
    ppsInputEnable[pinNumber].setLabel("USE PPS Input" + str(pinNumber))
    ppsInputEnable[pinNumber].setDefaultValue(False)
    ppsInputEnable[pinNumber].setReadOnly(True)
    ppsInputEnable[pinNumber].setVisible(False)
    ppsInputEnable[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_INPUT_" + str(pinNumber)])

    ppsInputFunction.append(pinNumber)
    ppsInputFunction[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_INPUT_FUNCTION_" + str(pinNumber), ppsInputEnable[pinNumber])
    ppsInputFunction[pinNumber].setLabel("Function")
    ppsInputFunction[pinNumber].setOutputMode("Value")
    ppsInputFunction[pinNumber].setDisplayMode("Key")
    ppsInputFunction[pinNumber].setDefaultValue(0)    
    ppsInputFunction[pinNumber].setReadOnly(True)
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
    ppsInputPin[pinNumber].setReadOnly(True)
    ppsInputPin[pinNumber].setVisible(False)

    for key, value in ppsInputPinMap.items():
        ppsInputPin[pinNumber].addKey(key, value, key)
    ppsInputPin[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_INPUT_" + str(pinNumber)])

for pinNumber in range(0, packagePinCount):
    #PPS Output pin Configuration
    ppsOutputEnable.append(pinNumber)
    ppsOutputEnable[pinNumber] = coreComponent.createBooleanSymbol("USE_PPS_OUTPUT_" + str(pinNumber), ppsPinOutputConfiguration)
    ppsOutputEnable[pinNumber].setLabel("USE PPS Output" + str(pinNumber))
    ppsOutputEnable[pinNumber].setDefaultValue(False)
    ppsOutputEnable[pinNumber].setReadOnly(True)
    ppsOutputEnable[pinNumber].setVisible(False)
    ppsOutputEnable[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_OUTPUT_" + str(pinNumber)])

    ppsOutputFunction.append(pinNumber)
    ppsOutputFunction[pinNumber] = coreComponent.createKeyValueSetSymbol("SYS_PORT_PPS_OUTPUT_FUNCTION_" + str(pinNumber), ppsOutputEnable[pinNumber])
    ppsOutputFunction[pinNumber].setLabel("Function")
    ppsOutputFunction[pinNumber].setOutputMode("Value")
    ppsOutputFunction[pinNumber].setDisplayMode("Key")
    ppsOutputFunction[pinNumber].setDefaultValue(0)
    ppsOutputFunction[pinNumber].setReadOnly(True)
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
    ppsOutputPin[pinNumber].setReadOnly(True)
    ppsOutputPin[pinNumber].setVisible(False)
    for key, value in PORTS_REMAP_OUTPUT_PIN.items():
        ppsOutputPin[pinNumber].addKey(key, value, value)
    ppsOutputPin[pinNumber].setDependencies(PPSOptionsVisibilityControl, ["USE_PPS_OUTPUT_" + str(pinNumber)])

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

channelConfiguration = coreComponent.createMenuSymbol("CHANNEL_CONFIGURATION", pioEnable)
channelConfiguration.setLabel("Channel Configuration")

gpioChannelName = []
gpioChannelIFS = []

port = []

portInterruptList = []

global portInterrupt
portInterrupt = []
global portInterruptStyle
portInterruptStyle = []
global gpioSym_GPIO_CNPU
gpioSym_GPIO_CNPU = []
global gpioSym_GPIO_CNPU_INIT_VAL
gpioSym_GPIO_CNPU_INIT_VAL =[]
global gpioSym_GPIO_CNPD
gpioSym_GPIO_CNPD = []
global gpioSym_GPIO_CNPD_INIT_VAL
gpioSym_GPIO_CNPD_INIT_VAL =[]
global gpioSym_GPIO_TRIS
gpioSym_GPIO_TRIS =[]
global gpioSym_GPIO_TRIS_INIT_VAL
gpioSym_GPIO_TRIS_INIT_VAL =[]
global gpioSym_GPIO_LAT
gpioSym_GPIO_LAT =[]
global gpioSym_GPIO_LAT_INIT_VAL
gpioSym_GPIO_LAT_INIT_VAL =[]
global gpioSym_GPIO_ODC
gpioSym_GPIO_ODC=[]
global gpioSym_GPIO_ODC_INIT_VAL
gpioSym_GPIO_ODC_INIT_VAL =[]
global gpioSym_GPIO_ANSEL
gpioSym_GPIO_ANSEL =[]
global gpioSym_GPIO_ANSEL_INIT_VAL
gpioSym_GPIO_ANSEL_INIT_VAL =[]
global gpioSym_GPIO_CNEN
gpioSym_GPIO_CNEN =[]
global gpioSym_PORT_CONFIG
gpioSym_PORT_CONFIG =[]

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
    pattern = r"CN[A-Z]Interrupt"
    if re.search(pattern, vName):
        intVectorDataDictionary[vName] = vIndex

# This symbol gives which IFS/IEC register should be used for CN interrupt handling.
gpioSym_IFS_RegIndex = coreComponent.createStringSymbol("SYS_PORT_IFS_REG_INDEX", pioEnable)
gpioSym_IFS_RegIndex.setLabel("IFS Register Index")
gpioSym_IFS_RegIndex.setReadOnly(True)
gpioSym_IFS_RegIndex.setVisible(False)

for portNumber in range(0, len(pioSymChannel)):

    gpioChannelName.append(portNumber)
    gpioChannelName[portNumber] = coreComponent.createStringSymbol("GPIO_CHANNEL_" + str(portNumber) + "_NAME" , channelConfiguration)
    gpioChannelName[portNumber].setVisible(False)
    gpioChannelName[portNumber].setDefaultValue(pioSymChannel[portNumber])

    gpioChannelIFS.append(portNumber)
    gpioChannelIFS[portNumber] = coreComponent.createStringSymbol("GPIO_CHANNEL_" + str(portNumber) + "_IFS" , channelConfiguration)
    gpioChannelIFS[portNumber].setVisible(False)
    gpioChannelIFS[portNumber].setDefaultValue(setIFSValue(portNumber))

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

    gpioSym_GPIO_TRIS.append(portNumber)
    gpioSym_GPIO_TRIS[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_TRIS", port[portNumber])
    gpioSym_GPIO_TRIS[portNumber].setLabel("TRIS" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_TRIS[portNumber].setDefaultValue(getRegisterInitValue("TRIS"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_TRIS[portNumber].setReadOnly(True)
    gpioSym_GPIO_TRIS[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:TRISx")

    gpioSym_GPIO_TRIS_INIT_VAL.append(portNumber)
    gpioSym_GPIO_TRIS_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_TRIS_INIT_VAL", port[portNumber])
    gpioSym_GPIO_TRIS_INIT_VAL[portNumber].setLabel("TRIS" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_TRIS_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_TRIS_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("TRIS"+str(pioSymChannel[portNumber])))

    gpioSym_GPIO_LAT.append(portNumber)
    gpioSym_GPIO_LAT[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_LAT", port[portNumber])
    gpioSym_GPIO_LAT[portNumber].setLabel("LAT" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_LAT[portNumber].setDefaultValue(getRegisterInitValue("LAT"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_LAT[portNumber].setReadOnly(True)
    gpioSym_GPIO_LAT[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:LATx")

    gpioSym_GPIO_LAT_INIT_VAL.append(portNumber)
    gpioSym_GPIO_LAT_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_LAT_INIT_VAL", port[portNumber])
    gpioSym_GPIO_LAT_INIT_VAL[portNumber].setLabel("LAT" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_LAT_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_LAT_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("LAT"+str(pioSymChannel[portNumber])))

    gpioSym_GPIO_ODC.append(portNumber)
    gpioSym_GPIO_ODC[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ODC", port[portNumber])
    gpioSym_GPIO_ODC[portNumber].setLabel("ODC" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_ODC[portNumber].setDefaultValue(getRegisterInitValue("ODC"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_ODC[portNumber].setReadOnly(True)
    gpioSym_GPIO_ODC[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:ODCx")

    gpioSym_GPIO_ODC_INIT_VAL.append(portNumber)
    gpioSym_GPIO_ODC_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ODC_INIT_VAL", port[portNumber])
    gpioSym_GPIO_ODC_INIT_VAL[portNumber].setLabel("ODC" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_ODC_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_ODC_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("ODC"+str(pioSymChannel[portNumber])))

    gpioSym_GPIO_ANSEL.append(portNumber)
    gpioSym_GPIO_ANSEL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ANSEL", port[portNumber])
    gpioSym_GPIO_ANSEL[portNumber].setLabel("ANSEL" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_ANSEL[portNumber].setDefaultValue(getRegisterInitValue("ANSEL"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_ANSEL[portNumber].setReadOnly(True)
    gpioSym_GPIO_ANSEL[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:ANSELx")

    gpioSym_GPIO_ANSEL_INIT_VAL.append(portNumber)
    gpioSym_GPIO_ANSEL_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ANSEL_INIT_VAL", port[portNumber])
    gpioSym_GPIO_ANSEL_INIT_VAL[portNumber].setLabel("ANSEL" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_ANSEL_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_ANSEL_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("ANSEL"+str(pioSymChannel[portNumber])))

    gpioSym_GPIO_CNEN.append(portNumber)
    gpioSym_GPIO_CNEN[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNEN", port[portNumber])
    gpioSym_GPIO_CNEN[portNumber].setLabel("CNEN" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNEN[portNumber].setDefaultValue(getRegisterInitValue("CNEN0"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_CNEN[portNumber].setReadOnly(True)
    gpioSym_GPIO_CNEN[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNEN0x")

    gpioSym_GPIO_CNPU.append(portNumber)
    gpioSym_GPIO_CNPU[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPU", port[portNumber])
    gpioSym_GPIO_CNPU[portNumber].setLabel("CNPU" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNPU[portNumber].setDefaultValue(getRegisterInitValue("CNPU"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_CNPU[portNumber].setReadOnly(True)
    gpioSym_GPIO_CNPU[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNPUx")

    gpioSym_GPIO_CNPU_INIT_VAL.append(portNumber)
    gpioSym_GPIO_CNPU_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPU_INIT_VAL", port[portNumber])
    gpioSym_GPIO_CNPU_INIT_VAL[portNumber].setLabel("CNPU" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_CNPU_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_CNPU_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("CNPU"+str(pioSymChannel[portNumber])))

    gpioSym_GPIO_CNPD.append(portNumber)
    gpioSym_GPIO_CNPD[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPD", port[portNumber])
    gpioSym_GPIO_CNPD[portNumber].setLabel("CNPD" + str(pioSymChannel[portNumber]) + " Value")
    gpioSym_GPIO_CNPD[portNumber].setDefaultValue(getRegisterInitValue("CNPD"+str(pioSymChannel[portNumber])))
    gpioSym_GPIO_CNPD[portNumber].setReadOnly(True)
    gpioSym_GPIO_CNPD[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:gpio_04928;register:CNPDx")

    gpioSym_GPIO_CNPD_INIT_VAL.append(portNumber)
    gpioSym_GPIO_CNPD_INIT_VAL[portNumber] = coreComponent.createHexSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPD_INIT_VAL", port[portNumber])
    gpioSym_GPIO_CNPD_INIT_VAL[portNumber].setLabel("CNPD" + str(pioSymChannel[portNumber]) + " Init Value")
    gpioSym_GPIO_CNPD_INIT_VAL[portNumber].setVisible(False)
    gpioSym_GPIO_CNPD_INIT_VAL[portNumber].setDefaultValue(getRegisterInitValue("CNPD"+str(pioSymChannel[portNumber])))

    #symbols and variables for interrupt handling
    intIndex = intVectorDataDictionary['CN'+str(pioSymChannel[portNumber]) +'Interrupt']

    pioSymIntEnComment.append(portNumber)
    pioSymIntEnComment[portNumber] = coreComponent.createCommentSymbol("SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ENABLE_COMMENT", pioMenu)
    pioSymIntEnComment[portNumber].setVisible(False)
    pioSymIntEnComment[portNumber].setLabel("Warning!!! Change Notice " + str(pioSymChannel[portNumber]) + " Interrupt is Disabled in Interrupt Manager")
    pioSymIntEnComment[portNumber].setDependencies(InterruptStatusWarning, [
        "core." + "INTC_" + str(intIndex) + "_ENABLE", 
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CN_USED"
    ])

    #Symbol to indicate there is changes in the port
    gpioSym_PORT_CONFIG.append(portNumber)
    gpioSym_PORT_CONFIG[portNumber] = coreComponent.createBooleanSymbol("GPIO_CHANNEL_" + str(pioSymChannel[portNumber]) + "_CONFIG", port[portNumber])
    gpioSym_PORT_CONFIG[portNumber].setLabel("Port " + str(pioSymChannel[portNumber]) +" Configured")
    gpioSym_PORT_CONFIG[portNumber].setDefaultValue(False)
    gpioSym_PORT_CONFIG[portNumber].setVisible(False)
    gpioSym_PORT_CONFIG[portNumber].setDependencies(checkPortConfiguration, [
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_TRIS",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_LAT",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ODC",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_ANSEL",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNEN",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPU",
        "SYS_PORT_" + str(pioSymChannel[portNumber]) + "_CNPD"
    ])

# Interrupt Dynamic settings
pioSymInterruptControl = coreComponent.createBooleanSymbol("IC_GPIO_ENABLE", pioMenu)
pioSymInterruptControl.setDependencies(pioInterruptControl, portInterruptList)
pioSymInterruptControl.setVisible(False)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

REGISTER_OFFSET = coreComponent.createStringSymbol("REGISTER_OFFSET",None)
REGISTER_OFFSET.setLabel("Register Offset 1")
REGISTER_OFFSET.setDefaultValue(setOffsetVal("TRISA","TRISB")) 
REGISTER_OFFSET.setVisible(False)

INTERRUPT_OFFSET = coreComponent.createStringSymbol("CN_INTERRUPT_OFFSET",None)
INTERRUPT_OFFSET.setLabel("INTERRUPT_OFFSET")
INTERRUPT_OFFSET.setDefaultValue(setOffsetVal("CNEN0A","CNEN0B"))
INTERRUPT_OFFSET.setVisible(False)

defFile = coreComponent.createFileSymbol("DEFINITIONS_FILE", None)
defFile.setType("STRING")
defFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
defFile.setSourcePath("../peripheral/gpio_04928/templates/system/definitions.h.ftl")
defFile.setMarkup(True)
 
initFile = coreComponent.createFileSymbol("INITIALIZATION_FILES", None)
initFile.setType("STRING")
initFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE1")
initFile.setSourcePath("../peripheral/gpio_04928/templates/system/initialization.c.ftl")
initFile.setMarkup(True)

pioHeaderFile = coreComponent.createFileSymbol("GPIO_HEADER", None)
pioHeaderFile.setSourcePath("../peripheral/gpio_04928/templates/plib_gpio.h.ftl")
pioHeaderFile.setOutputName("plib_gpio.h")
pioHeaderFile.setDestPath("/peripheral/gpio/")
pioHeaderFile.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioHeaderFile.setType("HEADER")
pioHeaderFile.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol("GPIO_SOURCE", None)
pioSource1File.setSourcePath("../peripheral/gpio_04928/templates/plib_gpio.c.ftl")
pioSource1File.setOutputName("plib_gpio.c")
pioSource1File.setDestPath("/peripheral/gpio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/gpio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)

ppsPinsLockBit = coreComponent.createStringSymbol("PPSPinsLockBit",None) 
ppsPinsLockBit.setLabel("PPS Pin Lock Bit")
ppsPinsLockBit.setVisible(False)

bitfieldData = getRegisterChildren("GPIO", "RPCON")
for bitfield in bitfieldData:
    if bitfield.getAttribute("name") == "IOLOCK":
        ppsPinsLockBit.setDefaultValue("RPCONbits.IOLOCK")
        break

sysPortIncludeFile = coreComponent.createFileSymbol("GPIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/gpio_04928/templates/plib_gpio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)
