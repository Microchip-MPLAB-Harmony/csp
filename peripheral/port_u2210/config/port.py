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

Log.writeInfoMessage("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

import re
global sort_alphanumeric
global peripheralFunctionality

peripheralFunctionality = ["GPIO", "Alternate", "LED_AH", "LED_AL", "SWITCH_AH", "SWITCH_AL"]

global availablePinDictionary
availablePinDictionary = {}

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

global getAvailablePins

# API used by core to return available pins to sender component
def getAvailablePins():

    return availablePinDictionary

def packageChange(symbol, pinout):
    global uniquePinout
    global package
    import re
    global prev_package
    global cur_package
    global pin_map
    global pin
    global pin_position
    global portGroupName
    global pinGroupNum
    ### No need to process if the device has only one pinout but multiple packages eg: TQFP, LQFP and QFN
    if uniquePinout > 1:
        cur_package = package.get(pinout["value"])

        ### No need to generate Pin map again for same pinout
        if cur_package != prev_package:
            pin_map = {}
            pin_position = []
            portBitPositionNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(package.get(pinout["value"])) + "\"]")
            for id in range(0,len(portBitPositionNode.getChildren())):
                if "BGA" in pinout["value"] or "WLCSP" in pinout["value"]:
                    pin_map[portBitPositionNode.getChildren()[id].getAttribute("position")] = portBitPositionNode.getChildren()[id].getAttribute("pad")
                else:
                    pin_map[int(portBitPositionNode.getChildren()[id].getAttribute("position"))] = portBitPositionNode.getChildren()[id].getAttribute("pad")

            if "BGA" in pinout["value"] or "WLCSP" in pinout["value"]:
                ## BGA package ID's are alphanumeric unlike TQFP special sorting required
                pin_position = sort_alphanumeric(pin_map.keys())
            else:
                pin_position = sorted(pin_map.keys())

        for index in range(1, len(pin) + 1):
            if index <= len(pin_position):
                if not pin[index - 1].getVisible():
                    pin[index - 1].setVisible(True)
                pin[index - 1].setLabel("Pin " + str(pin_position[index - 1]))
                pinGroupNum[index-1].setValue(portGroupName.index(str(pin_map.get(pin_position[index-1]))[1]), 2)
                if pin_map.get(pin_position[index-1]).startswith("P"):
                    Database.setSymbolValue("core", "PIN_" + str(index) + "_PORT_PIN", int(re.findall('\d+', pin_map.get(pin_position[index - 1]))[0]), 2)
                    Database.setSymbolValue("core", "PIN_" + str(index) + "_PORT_GROUP", pin_map.get(pin_position[index - 1])[1], 2)
                else:
                    Database.setSymbolValue("core", "PIN_" + str(index) + "_PORT_PIN", -1, 2)
                    Database.setSymbolValue("core", "PIN_" + str(index) + "_PORT_GROUP", "", 2)
            else:
                pin[index - 1].setVisible(False)

        prev_package = cur_package

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def setupPortPINCFG(usePortLocalPINCFG, event):

    pullEnable = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PULLEN")
    inputEnable = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_INEN")
    driveStrength = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_DRVSTR")
    peripheralFunc = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) +"_PERIPHERAL_FUNCTION")
    bitPosition = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
    groupName = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")

    if groupName != "None":

        cfgValue = 0

        if pullEnable:
            cfgValue |= (1 << 2)
        if pullEnable == "False":
            cfgValue &= ~ (1 << 2)
        if inputEnable:
            cfgValue |= (1 << 1)
        if inputEnable == "False":
            cfgValue &= ~ (1 << 1)
        if driveStrength == 0:
            cfgValue &= ~(1 << 6)
        elif driveStrength == 1:
            cfgValue |= (1 << 6) 
        if peripheralFunc not in peripheralFunctionality and peripheralFunc != "":
            cfgValue |= (1 << 0)
        else :
            cfgValue &= ~ (1 << 0)

        Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PINCFG" + str(bitPosition), str(hex(cfgValue)), 1)

def setupPortDir(usePortLocalDir, event):

    bitPosition = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
    groupName = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")

    preVal = Database.getSymbolValue(event["namespace"], "PORT_GROUP_" + str(portGroupName.index(groupName)) + "_DIR")

    dirValue = 0

    if preVal != None:
        dirValue = int(preVal.split("L")[0],0)

    if event["value"] == "Out":
        dirValue |= 1 << bitPosition
    else:
        dirValue &= ~ (1 << bitPosition)

    Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_DIR", str((hex(dirValue).rstrip("L"))), 1)

def setupPortLat(usePortLocalLatch, event):

    bitPosition = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
    groupName = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")

    preVal = Database.getSymbolValue(event["namespace"], "PORT_GROUP_" + str(portGroupName.index(groupName)) + "_OUT")
    outValue = 0

    if preVal != None:
        outValue = int(preVal.split("L")[0],0)

    if event["value"] == "High":
        outValue |= 1 << bitPosition
    else:
        outValue &= ~(1 << bitPosition)

    Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_OUT", str((hex(outValue).rstrip("L"))), 1)

def evsysControl(symbol, event):
    global group
    for i in range (0, 4):
        status = False
        for j in range(0,len(group)):
            if(Database.getSymbolValue("core", "PORT_"+ str(j) + "_EVACT"+str(i)+"_ENABLE")) == True:
                status = True
                break
        if Database.getSymbolValue("evsys", "USER_PORT_EV_" + str(i) + "_READY") != status:
            Database.setSymbolValue("evsys", "USER_PORT_EV_" + str(i) + "_READY", status, 2)

    evctrl = 0

    channelId = symbol.getID().split("_")[2]

    for i in range (0,len(group)):
        enable = Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_ENABLE")
        action = int(Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_ACTION"))
        pin = int(Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_PIN"))
        if enable == True:
            evctrl |=  1 << (7+(i*8)) | (action << (5+(i*8))) | (pin << (0+(i*8)))

    symbol.setValue(str(hex(evctrl)),2)

def setupPortPinMux(portSym_PORT_PMUX_local, event):
    global intPrePinMuxVal
    global prevID
    global prevVal
    global portPackage
    bitPosition = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
    groupName = Database.getSymbolValue(event["namespace"], "PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")
    peripheralFuncVal = 0
    if event["value"] not in peripheralFunctionality and event["value"] != "":

        prePinMuxVal = Database.getSymbolValue(event["namespace"], "PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2))
        intPrePinMuxVal = int(prePinMuxVal,0)

        if ((bitPosition%2) == 0):
            peripheralFuncVal = portPeripheralFunc.index(event["value"]) | ( int(prePinMuxVal,0) & int("0xf0",0) )
        else :
            peripheralFuncVal = (portPeripheralFunc.index(event["value"]) << 4) | ( int(prePinMuxVal,0) & int("0x0f",0) )

        Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(peripheralFuncVal)), 1)
    else :
        pinMuxVal = Database.getSymbolValue(event["namespace"], "PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2))
        intPinMuxVal = int(pinMuxVal,0)

        if ((bitPosition%2) == 0):
            intPrePinMuxVal &= int("0xf0",0)
        else :
            intPrePinMuxVal &= int("0x0f",0)

        Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(intPrePinMuxVal)), 1)

        if event["id"] != prevID:
            if intPinMuxVal == 0:
                    intPinMuxVal = int("0x00",0)
            else:
                if ((bitPosition%2) == 0):
                    intPinMuxVal &= int("0xf0",0)
                else :
                    intPinMuxVal &= int("0x0f",0)

        Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(intPinMuxVal)), 1)

        if event["id"] == prevID and event["value"] != prevVal:
            Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(intPrePinMuxVal)), 1)

        portPositionNodePin = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(package.get(portPackage.getValue())) + "\"]/pin@[position=\""+ str(event["id"].split("_")[1]) +"\"]")
        position = str(event["id"].split("_")[1])
        bitposition = Database.getSymbolValue("core", "PIN_" + position + "_PORT_PIN")
        if bitPosition < 10:
            bitPositionstr = "0" + str(bitposition)
        else:
            bitPositionstr = str(bitposition)
        padName = "P" + groupName + bitPositionstr
        Database.setSymbolValue( event["namespace"],"PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PAD_" + str(bitPosition) , padName, 1)

    prevID = event["id"]
    prevVal = event["value"]

###################################################################################################
######################################### PORT Main Menu  #########################################
###################################################################################################

##packagepinout map
global package
global portPackage
package = {}
## total number of pins
global pincount
pincount = 0
## Number of unique pinouts
global uniquePinout
uniquePinout = 1
portMenu = coreComponent.createMenuSymbol("PORT_MENU", None)
portMenu.setLabel("Ports")
portMenu.setDescription("Configuraiton for PORT PLIB")

# Needed to map port system APIs to PLIB APIs
portSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
portSymAPI_Prefix.setDefaultValue("PORT")
portSymAPI_Prefix.setVisible(False)

portEnable = coreComponent.createBooleanSymbol("PORT_ENABLE", portMenu)
portEnable.setLabel("Use PORT PLIB ?")
portEnable.setDefaultValue(True)
portEnable.setReadOnly(True)

# Build package pinout map
packageNode = ATDF.getNode("/avr-tools-device-file/variants")
for id in range(0,len(packageNode.getChildren())):
    package[packageNode.getChildren()[id].getAttribute("package")] = packageNode.getChildren()[id].getAttribute("pinout")

## Find Number of unique pinouts
uniquePinout = len(set(package.values()))

portPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", portEnable, package.keys())
portPackage.setLabel("Pin Package")
portPackage.setReadOnly(True)

## get the pin count
pincount = int(re.findall(r'\d+', package.keys()[0])[0])

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################

pinConfiguration = coreComponent.createMenuSymbol("PORT_PIN_CONFIGURATION", portEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuraiton for PORT Pins")

global prev_package
global cur_package
prev_package = ""
cur_package = ""
global pin_map
global pin_position
pin_map = {}
pin_position = []
global pin
pin = []
pinName = []
pinType = []
pinPeripheralFunction = []
pinBitPosition = []
global pinGroup
global prevID
global prevVal
prevID = ""
prevVal = ""
prevID = ""
pinGroup = []
pinMode = []
pinDirection = []
pinLatch = []
pinPullEnable = []
pinInputEnable = []
pinDrvStr = []
pinDirList = []
pinLatchList = []
pinPinMuxList = []
global pinGroupNum
pinGroupNum = []
portSym_PIN_PINCFG = []

# Create portGroupName list of uppercase letters
global portGroupName
portGroupName = []
for letter in range(65,91):
    portGroupName.append(chr(letter))

pinoutNode = ATDF.getNode('/avr-tools-device-file/pinouts/pinout@[name= "' + str(package.get(portPackage.getValue())) + '"]')
for id in range(0,len(pinoutNode.getChildren())):
    if "BGA" in portPackage.getValue() or "WLCSP" in portPackage.getValue():
        pin_map[pinoutNode.getChildren()[id].getAttribute("position")] = pinoutNode.getChildren()[id].getAttribute("pad")
    else:
        pin_map[int(pinoutNode.getChildren()[id].getAttribute("position"))] = pinoutNode.getChildren()[id].getAttribute("pad")

if "BGA" in portPackage.getValue() or "WLCSP" in portPackage.getValue():
    pin_position = sort_alphanumeric(pin_map.keys())
else:
    pin_position = sorted(pin_map.keys())

for pinNumber in range(1, pincount + 1):

    portSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/signals/signal@[index=\""+ str(pinNumber - 1) +"\"]")

    if portSignalNode != None:

        signalIndex = int(portSignalNode.getAttribute("index"))
        siganlPad = str(portSignalNode.getAttribute("pad"))

        if signalIndex != None and siganlPad != None:
            portSym_PinPad = coreComponent.createStringSymbol("PORT_PIN_PAD_" + str(signalIndex), None)
            portSym_PinPad.setVisible(False)
            portSym_PinPad.setDefaultValue(siganlPad)

            portSym_PinIndex = coreComponent.createIntegerSymbol("PORT_PIN_INDEX_" + str(signalIndex), None)
            portSym_PinIndex.setVisible(False)
            portSym_PinIndex.setDefaultValue(signalIndex)

            availablePinDictionary[str(signalIndex)] = siganlPad

    pin.append(pinNumber)
    pin[pinNumber-1] = coreComponent.createMenuSymbol("PORT_PIN" + str(pinNumber), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pin_position[pinNumber-1]))
    pin[pinNumber-1].setDescription("Configuraiton for Pin " + str(pin_position[pinNumber-1]) )

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)

    pinGroup.append(pinNumber)
    pinGroup[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PORT_GROUP", pin[pinNumber-1])
    pinGroup[pinNumber-1].setLabel("Group")
    pinGroup[pinNumber-1].setReadOnly(True)

    pinGroupNum.append(pinNumber)
    pinGroupNum[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GROUP", pin[pinNumber-1])
    pinGroupNum[pinNumber-1].setVisible(False)

    if pin_map.get(pin_position[pinNumber-1]).startswith("P"):
        pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]))
        pinGroup[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])
        pinGroupNum[pinNumber-1].setDefaultValue(portGroupName.index(str(pin_map.get(pin_position[pinNumber-1]))[1]))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(True)

    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    pinPeripheralFunction[pinNumber-1].setReadOnly(True)

    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setLabel("Mode")
    pinMode[pinNumber-1].setReadOnly(True)

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(True)

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(True)

    pinPullEnable.append(pinNumber)
    pinPullEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PULLEN", pin[pinNumber-1])
    pinPullEnable[pinNumber-1].setLabel("Pull Enable")
    pinPullEnable[pinNumber-1].setReadOnly(True)

    pinInputEnable.append(pinNumber)
    pinInputEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_INEN", pin[pinNumber-1])
    pinInputEnable[pinNumber-1].setLabel("Input Enable")
    pinInputEnable[pinNumber-1].setReadOnly(True)

    pinDrvStr.append(pinNumber)
    pinDrvStr[pinNumber-1] = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_DRVSTR", pin[pinNumber-1])
    pinDrvStr[pinNumber-1].setLabel("Drive Strength")
    pinDrvStr[pinNumber-1].setDisplayMode("Key")
    pinDrvStr[pinNumber-1].addKey("NORMAL", "0", "Normal")
    pinDrvStr[pinNumber-1].addKey("STRONG", "1", "Strong")
    pinDrvStr[pinNumber-1].setReadOnly(True)

    #creating list for direction dependency
    pinDirList.append(pinNumber)
    pinDirList[pinNumber-1] = "PIN_" + str(pinNumber) +"_DIR"

    #creating list for direction dependency
    pinLatchList.append(pinNumber)
    pinLatchList[pinNumber-1] = "PIN_" + str(pinNumber) +"_LAT"

    #creating list for peripheral function dependency
    pinPinMuxList.append(pinNumber)
    pinPinMuxList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PERIPHERAL_FUNCTION"

    portSym_PIN_PINCFG.append(pinNumber)
    portSym_PIN_PINCFG[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_CFG", pin[pinNumber-1])
    portSym_PIN_PINCFG[pinNumber-1].setReadOnly(True)
    portSym_PIN_PINCFG[pinNumber-1].setVisible(False)
    portSym_PIN_PINCFG[pinNumber-1].setDependencies(setupPortPINCFG, ["PIN_" + str(pinNumber) +"_INEN", "PIN_" + str(pinNumber) +"_PULLEN", "PIN_" + str(pinNumber) +"_PERIPHERAL_FUNCTION", "PIN_" + str(pinNumber) + "_DRVSTR"])

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

packageUpdate = coreComponent.createBooleanSymbol("PACKAGE_UPDATE_DUMMY", None)
packageUpdate.setVisible(False)
packageUpdate.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

portConfiguration = coreComponent.createMenuSymbol("PORT_CONFIGURATIONS", portEnable)
portConfiguration.setLabel("Port Registers Configuration")

portModuleGC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/register-group@[name=\"PORT\"]/register-group@[name-in-module=\"GROUP\"]")

#port group count
portSym_Count = coreComponent.createIntegerSymbol("PORT_GROUP_COUNT", portConfiguration)
portSym_Count.setVisible(False)
portSym_Count.setDefaultValue(int(portModuleGC.getAttribute("count")))

portSym_PinCount = coreComponent.createIntegerSymbol("PORT_PIN_COUNT", portMenu)
portSym_PinCount.setVisible(False)
portSym_PinCount.setDefaultValue(pincount)

global portPeripheralFunc
portPeripheralFunc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

global group
group = [0 for i in range(int(portModuleGC.getAttribute("count")))]

global intPrePinMuxVal
intPrePinMuxVal = 0x00

global portPin
portPin = []

global usePort
usePort = []
evsysDep = []
port = []
visibility = False
portSym_GroupName = []

portEvsysActionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/value-group@[name=\"PORT_EVCTRL__EVACT0\"]")
if portEvsysActionNode != None:
    portEvsysActionValues = portEvsysActionNode.getChildren()

for portNumber in range(0, len(group)):

    port.append(portNumber)
    port[portNumber] = coreComponent.createMenuSymbol("PORT_GROUP_" + str(portNumber) + "_CONFIGURATION", portConfiguration)
    port[portNumber].setLabel("PORT" + str(portGroupName[portNumber]) + " Configuration")

    #port group name
    portSym_GroupName.append(portNumber)
    portSym_GroupName[portNumber] = coreComponent.createStringSymbol("PORT_GROUP_NAME_" + str(portNumber), portConfiguration)
    portSym_GroupName[portNumber].setVisible(False)
    portSym_GroupName[portNumber].setDefaultValue(str(portNumber))

    usePort.append(portNumber)
    usePort[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber), port[portNumber])
    usePort[portNumber].setLabel("Use PORT GROUP " + str(portGroupName[portNumber]))
    usePort[portNumber].setValue(True, 1)
    usePort[portNumber].setVisible(visibility)

    portSym_PORT_DIR = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_DIR", port[portNumber])
    portSym_PORT_DIR.setLabel("Port Pin Direction")
    portSym_PORT_DIR.setVisible(visibility)
    portSym_PORT_DIR.setDefaultValue(str(hex(0)))
    portSym_PORT_DIR.setDependencies(setupPortDir, pinDirList)

    portSym_PORT_LATCH = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_OUT", port[portNumber])
    portSym_PORT_LATCH.setLabel("Port Pin Output Value")
    portSym_PORT_LATCH.setDefaultValue(str(hex(0)))
    portSym_PORT_LATCH.setDependencies(setupPortLat, pinLatchList)
    portSym_PORT_LATCH.setVisible(visibility)

    portSym_PORT_CTRL = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_CTRL", port[portNumber])
    portSym_PORT_CTRL.setLabel("Enable Input Synchronizer")
    portSym_PORT_CTRL.setDefaultValue(str(hex(0)))
    portSym_PORT_CTRL.setVisible(visibility)

    for pinNum in range(0, 32):
        #creating list for port pin
        portPin.append(str(pinNum))

        portSym_PORT_PINCFG = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) , port[portNumber])
        portSym_PORT_PINCFG.setLabel("PORT GROUP " + str(portGroupName[portNumber]) + " PINCFG" + str(pinNum))
        portSym_PORT_PINCFG.setDefaultValue(str(hex(0)))
        portSym_PORT_PINCFG.setVisible(visibility)

        portPad = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PAD_" + str(pinNum), port[portNumber])
        portPad.setVisible(False)
        portPad.setDefaultValue("0")

    for pinNum in range(0, 16):
        portSym_PORT_PMUX = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PMUX" + str(pinNum) , port[portNumber])
        portSym_PORT_PMUX.setLabel("PORT GROUP " + str(portGroupName[portNumber]) + " PMUX" + str(pinNum))
        portSym_PORT_PMUX.setDefaultValue(str(hex(0)))
        portSym_PORT_PMUX.setVisible(visibility)
        portSym_PORT_PMUX.setDependencies(setupPortPinMux, pinPinMuxList)

    if portEvsysActionNode != None:
        portEVSYS = coreComponent.createMenuSymbol("PORT_MENU_EVSYS" + str(portNumber), port[portNumber])
        portEVSYS.setLabel("EVENT System Configuraiton")

        for i in range(0, 4):
            portEVSYSEnable = coreComponent.createBooleanSymbol("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ENABLE", portEVSYS)
            portEVSYSEnable.setLabel("Enable Event" + str(i) + " Input")
            evsysDep.append("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ENABLE")

            portEvsysAction = coreComponent.createKeyValueSetSymbol("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ACTION",portEVSYSEnable)
            portEvsysAction.setLabel("Event" + str(i) + " Action")
            for index in range(0, len(portEvsysActionValues)):
                portEvsysActionKeyName = portEvsysActionValues[index].getAttribute("name")
                portEvsysActionDescription = portEvsysActionValues[index].getAttribute("caption")
                portEvsysActionValue = portEvsysActionValues[index].getAttribute("value")
                portEvsysAction.addKey(portEvsysActionKeyName, portEvsysActionValue , portEvsysActionDescription)

            portEvsysAction.setDefaultValue(0)
            portEvsysAction.setOutputMode("Value")
            portEvsysAction.setDisplayMode("Description")
            evsysDep.append("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ACTION")

            portEvsysPin = coreComponent.createKeyValueSetSymbol("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_PIN",portEVSYSEnable)
            portEvsysPin.setLabel("Event" + str(i) + " Pin")
            for index in range(0, 32):
                portEvsysPin.addKey("P" + str(index), str(index) , "Pin " + str(index))

            portEvsysAction.setDefaultValue(0)
            portEvsysAction.setOutputMode("Value")
            portEvsysAction.setDisplayMode("Description")
            evsysDep.append("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_PIN")

        portSym_PORT_EVCTRL = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_EVCTRL", port[portNumber])
        portSym_PORT_EVCTRL.setLabel("Port Event Control")
        portSym_PORT_EVCTRL.setVisible(visibility)
        portSym_PORT_EVCTRL.setDefaultValue(str(hex(0)))
        portSym_PORT_EVCTRL.setDependencies(evsysControl, evsysDep)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

portModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]")
portModuleID = portModuleNode.getAttribute("id")

portSym_HeaderFile = coreComponent.createFileSymbol("PORT_HEADER", None)
portSym_HeaderFile.setSourcePath("../peripheral/port_u2210/templates/plib_port.h.ftl")
portSym_HeaderFile.setOutputName("plib_port.h")
portSym_HeaderFile.setDestPath("/peripheral/port/")
portSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/port/")
portSym_HeaderFile.setType("HEADER")
portSym_HeaderFile.setMarkup(True)

portSym_SourceFile = coreComponent.createFileSymbol("PORT_SOURCE", None)
portSym_SourceFile.setSourcePath("../peripheral/port_u2210/templates/plib_port.c.ftl")
portSym_SourceFile.setOutputName("plib_port.c")
portSym_SourceFile.setDestPath("/peripheral/port/")
portSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/port/")
portSym_SourceFile.setType("SOURCE")
portSym_SourceFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PORT_BSP_HEADER", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/port_u2210/templates/plib_port_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PORT_BSP_SOURCE", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspIncludeFile.setSourcePath("../peripheral/port_u2210/templates/plib_port_bsp.c.ftl")
bspIncludeFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("PIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/port_u2210/templates/plib_port_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)

portSym_SystemInitFile = coreComponent.createFileSymbol("PORT_SYS_INIT", None)
portSym_SystemInitFile.setSourcePath("../peripheral/port_u2210/templates/system/initialization.c.ftl")
portSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
portSym_SystemInitFile.setType("STRING")
portSym_SystemInitFile.setMarkup(True)

portSym_SystemDefFile = coreComponent.createFileSymbol("PORT_SYS_DEF", None)
portSym_SystemDefFile.setSourcePath("../peripheral/port_u2210/templates/system/definitions.h.ftl")
portSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
portSym_SystemDefFile.setType("STRING")
portSym_SystemDefFile.setMarkup(True)
