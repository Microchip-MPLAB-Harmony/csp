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

peripheralFunctionality = ["GPIO", "Alternate", "LED_AH", "LED_AL", "SWITCH_AH", "SWITCH_AL", "VBUS_AH", "VBUS_AL", "RTC", "SUPC", "RTC_IN", "RTC_OUT"]

global portPeripheralFunc
portPeripheralFunc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

global availablePinDictionary
availablePinDictionary = {}

## SHD: Dictionary to store symbols created for each pin
global pinSymbolsDictionary
pinSymbolsDictionary = dict()

global port_evsys_usersNamesList
port_evsys_usersNamesList = []

def portEvsysUserNamesPopulate(instanceName):
    global port_evsys_usersNamesList

    usersNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/users")
    usersValues = usersNode.getChildren()
    for id in range(0, len(usersNode.getChildren())):
        if usersValues[id].getAttribute("module-instance") == instanceName:
            port_evsys_usersNamesList.append(usersValues[id].getAttribute("name"))

global portEvsysUserNameGet
def portEvsysUserNameGet(usrNameMatchList):
    global port_evsys_usersNamesList

    for userName in port_evsys_usersNamesList:
        if all ( x in userName for x in usrNameMatchList):
            return userName

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

global getAvailablePins

global setPinConfigurationValue
global getPinConfigurationValue
global clearPinConfigurationValue

def setPinConfigurationValue(pinNumber, setting, value):
    if setting == "direction":
        if value == "In":
            symbol = pinSymbolsDictionary.get(pinNumber).get("input")
            symbol.setValue("True")
            symbol = pinSymbolsDictionary.get(pinNumber).get("direction")
            symbol.clearValue()
        elif value == "Out":
            symbol = pinSymbolsDictionary.get(pinNumber).get("input")
            symbol.clearValue()
            symbol = pinSymbolsDictionary.get(pinNumber).get("direction")
            symbol.setValue("Out")
        elif value == "In/Out":
            symbol = pinSymbolsDictionary.get(pinNumber).get("input")
            symbol.setValue("True")
            symbol = pinSymbolsDictionary.get(pinNumber).get("direction")
            symbol.setValue("Out")
    elif setting == "trustzone":
        symbol = pinSymbolsDictionary.get(pinNumber).get("trustzone")
        if symbol is not None:
            if value.upper() == "NON-SECURE":
                symbol.setSelectedKey("NON-SECURE")
            else:
                symbol.setSelectedKey("SECURE")
    else:
        symbol = pinSymbolsDictionary.get(pinNumber).get(setting)
        if symbol:
            symbol.clearValue()
            symbol.setValue(value)

        if setting == 'function':
            symbol = pinSymbolsDictionary.get(pinNumber).get('mode')
            if symbol != None:
                if (value.startswith("ADC") or (value.startswith("DAC")) or (value.startswith("PTC"))) and value[-1].isnumeric():
                    symbol.setValue("ANALOG")
                elif value.startswith("SDADC"):
                    symbol.setValue("ANALOG")
                else:
                    symbol.clearValue()
                    
            symbol = pinSymbolsDictionary.get(pinNumber).get('peripheralfunction')
            periphFnValue = value
            if symbol:
                if periphFnValue != "GPIO":
                    instance = value.split("_")[0]
                    module = "".join(filter(lambda x: x.isalpha(), instance))
                    pad = availablePinDictionary[str(pinNumber)]
                    query = '/avr-tools-device-file/devices/device/peripherals/module@[name=\"{}\"]/instance@[name=\"{}\"]/signals/signal@[pad=\"{}\"]'.format(module, instance, pad)
                    node = ATDF.getNode(query)
                    if node is not None:
                        periphFnValue = node.getAttribute("function")

                    if ((periphFnValue not in portPeripheralFunc) and (periphFnValue not in peripheralFunctionality)):
                        periphFnValue = "GPIO"
                    
                symbol.clearValue()
                symbol.setValue(periphFnValue)

        elif setting == 'pull up':
            if value == "True":
                symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
                symbol.setValue("True")
                symbol = pinSymbolsDictionary.get(pinNumber).get('latch')
                symbol.setValue("High")
            else:
                symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
                symbol.clearValue()

        elif setting == 'pull down':
            if value == "True":
                symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
                symbol.setValue("True")
                symbol = pinSymbolsDictionary.get(pinNumber).get('latch')
                symbol.clearValue()
            else:
                symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
                symbol.clearValue()

def getPinConfigurationValue(pinNumber, setting):
    symbol = pinSymbolsDictionary.get(pinNumber).get(setting)
    if symbol:
        return symbol.getValue()

    if setting == 'pull up':
        symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
        pullen = symbol.getValue()
        symbol = pinSymbolsDictionary.get(pinNumber).get('latch')
        pulllatch = symbol.getValue()
        if pullen ==" True" and pulllatch == "High":
            return "True"
        else:
            return "False"

    elif setting == 'pull down':
        symbol = pinSymbolsDictionary.get(pinNumber).get('pullen')
        pullen = symbol.getValue()
        symbol = pinSymbolsDictionary.get(pinNumber).get('latch')
        pulllatch = symbol.getValue()
        if pullen ==" True" and (pulllatch == "Low" or pulllatch == ""):
            return "True"
        else:
            return "False"
        
    elif setting == "direction":
        symbol = pinSymbolsDictionary.get(pinNumber).get("input")
        inputValue = symbol.getValue()
        symbol = pinSymbolsDictionary.get(pinNumber).get("direction")
        dirValue = symbol.getValue()
        if inputValue == "True" and dirValue == "":
            return "In"
        elif dirValue == "Out" and (inputValue == "" or inputValue == "False"):
            return "Out"
        elif inputValue == "True" and dirValue == "Out":
            return "In/Out"
        
    elif setting == "trustzone":
        symbol = pinSymbolsDictionary.get(pinNumber).get("trustzone")
        if symbol is not None:
            return symbol.getSelectedKey()

def clearPinConfigurationValue(pinNumber, setting):
    pinSymbol = pinSymbolsDictionary.get(pinNumber)
    if pinSymbol is not None:
        if setting == 'function':
            symbol = pinSymbol.get(setting)
            if symbol is not None:
                symbol.clearValue()

            symbol = pinSymbol.get('peripheralfunction')
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()
            
            symbol = pinSymbol.get('mode')
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()

        elif setting == 'pull up' or setting == 'pull down':
            symbol = pinSymbol.get('pullen')
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()
            symbol = pinSymbol.get('latch')
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()

        elif setting == "direction":
            symbol = pinSymbol.get("input")
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()
            symbol = pinSymbol.get("direction")
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()
            
        else:
            symbol = pinSymbol.get(setting)
            if symbol is not None:
                symbol.setReadOnly(True)
                symbol.setReadOnly(False)
                symbol.clearValue()
        
    
portSecAliasRegSpace = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/register-group@[name=\"PORT_SEC\"]")

portRegName = coreComponent.createStringSymbol("PORT_REG_NAME", None)
portRegName.setVisible(False)
if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true" and portSecAliasRegSpace != None:
    portRegName.setValue("PORT_SEC")
else:
    portRegName.setValue("PORT")
# API used by core to return available pins to sender component
def getAvailablePins():

    return availablePinDictionary

def getValueGroupNode__Port(module_name, register_group, register_name, bitfield_name , mode = None):
    bitfield_node_path = ""
    value_group_node = None

    if mode != None:
        bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[modes=\"{2}\",name=\"{3}\"]/bitfield@[name=\"{4}\"]".format(module_name, register_group, mode, register_name, bitfield_name)
    else:
         bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[name=\"{2}\"]/bitfield@[name=\"{3}\"]".format(module_name, register_group, register_name, bitfield_name)

    bitfield_node = ATDF.getNode(bitfield_node_path)

    if bitfield_node != None:
        if bitfield_node.getAttribute("values") == None:
            Log.writeDebugMessage(register_name + "_" + bitfield_name + "does not have value-group attribute")
        else:
            value_group_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"{0}\"]/value-group@[name=\"{1}\"]".format(module_name, bitfield_node.getAttribute("values")))
            if value_group_node == None:
                Log.writeDebugMessage("value-group = " + bitfield_node.getAttribute("values") + " not defined")
    else:
        Log.writeDebugMessage("bitfield_name = " + bitfield_name + " not found" )

    return value_group_node

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
                if "BGA" in pinout["value"] or "WLCSP" in pinout["value"] or "DRQFN" in pinout["value"]:
                    # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
                    pin_map[portBitPositionNode.getChildren()[id].getAttribute("position")] = re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', portBitPositionNode.getChildren()[id].getAttribute("pad"))
                else:
                    # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
                    pin_map[int(portBitPositionNode.getChildren()[id].getAttribute("position"))] = re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', portBitPositionNode.getChildren()[id].getAttribute("pad"))

            if "BGA" in pinout["value"] or "WLCSP" in pinout["value"] or "DRQFN" in pinout["value"]:
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
                pinExportName[index - 1].setValue(str(pin_position[index - 1]) + ":" + str(pin_map[pin_position[index - 1]]))
                if (pin_map.get(pin_position[index-1]).startswith("P")) and (pin_map.get(pin_position[index-1])[-1].isdigit()):
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
    component = event["source"]
    groupName = component.getSymbolValue("PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")
    #This is a port pin (belongs to a port group)
    if groupName:
        bitPosition = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
        pullEnable = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_PULLEN")
        inputEnable = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_INEN")
        if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_ODRAIN")) == True:
            openDrain = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_ODRAIN")
        if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_SLEWRATE")) == True:
            slewRate = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_SLEWRATE")
        if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_DRVSTR")) == True:
            driveStrength = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_DRVSTR")
        peripheralFunc = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) +"_PERIPHERAL_FUNCTION")

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
            if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_ODRAIN")) == True:
                if openDrain:
                    cfgValue |= (1 << 3)
                if openDrain == "False":
                    cfgValue &= ~ (1 << 3)
            if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_SLEWRATE")) == True:
                cfgValue |= (slewRate << 4)
            if (Database.getSymbolValue("core", "PORT_GROUP_PINCFG_DRVSTR")) == True:
                if driveStrength == 0:
                    cfgValue &= ~(1 << 6)
                elif driveStrength == 1:
                    cfgValue |= (1 << 6)
            if peripheralFunc not in peripheralFunctionality and peripheralFunc != "":
                cfgValue |= (1 << 0)
            else :
                cfgValue &= ~ (1 << 0)

            component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PINCFG" + str(bitPosition), str(hex(cfgValue)))

            functionType = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) +"_FUNCTION_TYPE")
            if functionType != "":
                component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PIN_" + str(bitPosition) + "_USED", True)
            else:
                component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PIN_" + str(bitPosition) + "_USED", False)

def setupPortDir(usePortLocalDir, event):
    component = event["source"]
    groupName = component.getSymbolValue("PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")
    #This is a port pin (belongs to a port group)
    if groupName:
        bitPosition = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
        preVal = component.getSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_DIR")
        dirValue = 0

        if preVal != None:
            dirValue = int(preVal.split("L")[0],0)

        if event["value"] == "Out":
            dirValue |= 1 << bitPosition
        else:
            dirValue &= ~ (1 << bitPosition)

        component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_DIR", str((hex(dirValue).rstrip("L"))))

def setupPortLat(usePortLocalLatch, event):
    component = event["source"]
    groupName = component.getSymbolValue("PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")
    #This is a port pin (belongs to a port group)
    if groupName:
        bitPosition = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
        preVal = component.getSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_OUT")
        outValue = 0

        if preVal != None:
            outValue = int(preVal.split("L")[0],0)

        if event["value"] == "High":
            outValue |= 1 << bitPosition
        else:
            outValue &= ~(1 << bitPosition)

        component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_OUT", str((hex(outValue).rstrip("L"))))

def evsysControl(symbol, event):
    global group
    for i in range (0, 4):
        status = False
        for j in range(0,len(group)):
            if(Database.getSymbolValue("core", "PORT_"+ str(j) + "_EVACT"+str(i)+"_ENABLE")) == True:
                status = True
                break
        evsysUserName = portEvsysUserNameGet(["EV", str(i)])
        if Database.getSymbolValue("evsys", "USER_" + evsysUserName + "_READY") != status:
            Database.setSymbolValue("evsys", "USER_" + evsysUserName + "_READY", status, 2)

    evctrl = 0

    channelId = symbol.getID().split("_")[2]

    for i in range (0,4):
        enable = Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_ENABLE")
        action = int(Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_ACTION"))
        pin = int(Database.getSymbolValue("core", "PORT_"+ channelId + "_EVACT"+str(i)+"_PIN"))
        if enable == True:
            evctrl |=  1 << (7+(i*8)) | (action << (5+(i*8))) | (pin << (0+(i*8)))

    symbol.setValue(str(hex(evctrl)),2)

def setupPortPinMux(portSym_PORT_PMUX_local, event):

    global prevID
    global prevVal
    global portPackage

    component = event["source"]
    groupName = component.getSymbolValue("PIN_" + str(event["id"].split("_")[1]) + "_PORT_GROUP")
    #This is a port pin (belongs to a port group)
    if groupName:
        bitPosition = component.getSymbolValue( "PIN_" + str(event["id"].split("_")[1]) + "_PORT_PIN")
        peripheralFuncVal = 0
        if event["value"] not in peripheralFunctionality and event["value"] != "":
            prePinMuxVal = component.getSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2))
            intPrePinMuxVal = int(prePinMuxVal,0)

            if event["value"] in portPeripheralFunc:
                if ((bitPosition%2) == 0):
                    peripheralFuncVal = portPeripheralFunc.index(event["value"]) | ( intPrePinMuxVal & 0xf0 )
                else :
                    peripheralFuncVal = (portPeripheralFunc.index(event["value"]) << 4) | ( intPrePinMuxVal & 0x0f )
            else:
                Log.writeWarningMessage("{0} is not a peripheral function for pin P{1}{2}".format(event["value"], groupName, bitPosition))

            component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(peripheralFuncVal)), 1)
        else :
            pinMuxVal = component.getSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2))
            initVal = int(component.getSymbolByID("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2)).getDefaultValue(),0)
            intPrePinMuxVal = int(pinMuxVal,0)

            if ((bitPosition%2) == 0):
                intPrePinMuxVal &= 0xf0
                intPrePinMuxVal |= (initVal & 0x0f)
            else :
                intPrePinMuxVal &= 0x0f
                intPrePinMuxVal |= (initVal & 0xf0)

            component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PMUX" + str(bitPosition/2), str(hex(intPrePinMuxVal)))

        if bitPosition < 10:
            bitPositionstr = "0" + str(bitPosition)
        else:
            bitPositionstr = str(bitPosition)
        padName = "P" + groupName + bitPositionstr
        component.setSymbolValue("PORT_GROUP_" + str(portGroupName.index(groupName)) + "_PAD_" + str(bitPosition) , padName)


def update_port_nonsec_mask(symbol, event):
    pinNum = event["id"].split("_IS_NON_SECURE")[0].split("PIN_")[1]
    groupName = Database.getSymbolValue("core", "PIN_" + str(pinNum) + "_PORT_GROUP")
    if groupName:
        portGroup = ord(groupName) - 65
        pinPos = int(Database.getSymbolValue("core", "PIN_" + str(pinNum) + "_PORT_PIN"))
        if Database.getSymbolValue("core", "PORT_GROUP_" + str(portGroup) + "_NONSEC") != None:
            portNonSecRegValue = int(Database.getSymbolValue("core", "PORT_GROUP_" + str(portGroup) + "_NONSEC"))

            if event["value"] == 1:
                portNonSecRegValue = portNonSecRegValue | 1<<pinPos
            else:
                portNonSecRegValue = portNonSecRegValue & ~(1<<pinPos)

            Database.setSymbolValue("core", "PORT_GROUP_" + str(portGroup) + "_NONSEC", long(portNonSecRegValue))
        

def updateSecurityAttributeVisibility(symbol, event):
    component = event["source"]
    portPinCount = component.getSymbolValue("PORT_PIN_COUNT")
    for pinNumber in range(1, portPinCount + 1):
        pinSecuritySym = component.getSymbolByID("PIN_" + str(pinNumber) + "_IS_NON_SECURE")
        if event["value"] == True:
            pinSecuritySym.setReadOnly(False)
        else:
            pinSecuritySym.setReadOnly(True)
            pinSecuritySym.setSelectedKey("SECURE")

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
global swdPin

portEvsysUserNamesPopulate("PORT")

uniquePinout = 1
portMenu = coreComponent.createMenuSymbol("PORT_MENU", None)
portMenu.setLabel("Ports")
portMenu.setDescription("Configuraiton for PORT PLIB")

# Needed to map port system APIs to PLIB APIs
portSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
portSymAPI_Prefix.setDefaultValue("PORT")
portSymAPI_Prefix.setVisible(False)

portEnable = coreComponent.createBooleanSymbol("PORT_ENABLE", portMenu)
portEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:CTRL")
portEnable.setLabel("Use PORT PLIB ?")
portEnable.setDefaultValue(True)
portEnable.setReadOnly(True)

portExport = coreComponent.createBooleanSymbol("PORT_EXPORT", portEnable)
portExport.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:PINCFG")
portExport.setLabel("Export PORT configuration")
portExport.setDefaultValue(True)
portExport.setVisible(False)

portExportAs = coreComponent.createComboSymbol("PORT_EXPORT_AS", portExport, ["CSV File"])
portExportAs.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:PINCFG")
portExportAs.setLabel("Export PORT configuration as ")
portExportAs.setVisible(False)

# Build package pinout map
packageNode = ATDF.getNode("/avr-tools-device-file/variants")
for id in range(0,len(packageNode.getChildren())):
    package[packageNode.getChildren()[id].getAttribute("package")] = packageNode.getChildren()[id].getAttribute("pinout")

## Find Number of unique pinouts
uniquePinout = len(set(package.values()))

portPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", portEnable, package.keys())
portPackage.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:CTRL")
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
global pin_map_internal
global pin_position
global pin_position_internal
pin_map = {}
pin_map_internal = {}
pin_position = []
pin_position_internal = []
global pin
pin = []
global pinExportName
pinExportName = []
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
pinSlewRate = []
pinOpenDrain = []
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
    if pinoutNode.getChildren()[id].getAttribute("type") == None:
        if "BGA" in portPackage.getValue() or "WLCSP" in portPackage.getValue() or "DRQFN" in portPackage.getValue():
            # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
            pin_map[pinoutNode.getChildren()[id].getAttribute("position")] = re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', pinoutNode.getChildren()[id].getAttribute("pad"))
        else:
            # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
            pin_map[int(pinoutNode.getChildren()[id].getAttribute("position"))] = re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', pinoutNode.getChildren()[id].getAttribute("pad"))
    else:
        # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
        pin_map_internal[pinoutNode.getChildren()[id].getAttribute("type").split("INTERNAL_")[1]] = re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', pinoutNode.getChildren()[id].getAttribute("pad"))

if "BGA" in portPackage.getValue() or "WLCSP" in portPackage.getValue() or "DRQFN" in portPackage.getValue():
    pin_position = sort_alphanumeric(pin_map.keys())
    pin_position_internal = sort_alphanumeric(pin_map_internal.keys())
else:
    pin_position = sorted(pin_map.keys())
    pin_position_internal = sorted(pin_map_internal.keys())

internalPincount = pincount + len(pin_map_internal.keys())

pinTotalPins = coreComponent.createIntegerSymbol("PIO_PIN_TOTAL" , pinConfiguration)
pinTotalPins.setVisible(False)
pinTotalPins.setDefaultValue(internalPincount)

portSym_PinMaxIndex = coreComponent.createIntegerSymbol("PORT_PIN_MAX_INDEX", None)
portSym_PinMaxIndex.setVisible(False)
max_index = 0

portPINCFGOpenDrain = coreComponent.createBooleanSymbol("PORT_GROUP_PINCFG_ODRAIN", None)
portPINCFGOpenDrain.setDefaultValue((ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/register-group@[name=\"GROUP\"]/register@[name=\"PINCFG\"]/bitfield@[name=\"ODRAIN\"]") != None))
portPINCFGOpenDrain.setVisible(False)

portPINCFGSlewRate = coreComponent.createBooleanSymbol("PORT_GROUP_PINCFG_SLEWRATE", None)
portPINCFGSlewRate.setDefaultValue((ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/register-group@[name=\"GROUP\"]/register@[name=\"PINCFG\"]/bitfield@[name=\"SLEWLIM\"]") != None))
portPINCFGSlewRate.setVisible(False)

portPINCFGDriverStrength = coreComponent.createBooleanSymbol("PORT_GROUP_PINCFG_DRVSTR", None)
portPINCFGDriverStrength.setDefaultValue((ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/register-group@[name=\"GROUP\"]/register@[name=\"PINCFG\"]/bitfield@[name=\"DRVSTR\"]") != None))
portPINCFGDriverStrength.setVisible(False)

for pinNumber in range(1, internalPincount + 1):

    symbolsDict = dict()

    if pinNumber < pincount + 1:
        pinPad = str(pin_map.get(pin_position[pinNumber-1]))
    else:
        pinPad = str(pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1]))

    portSym_PinIndexTz = coreComponent.createIntegerSymbol("PORT_PIN_INDEX_TZ_" + str(pinNumber), None)
    portSym_PinIndexTz.setVisible(False)

    portSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/signals/signal@[pad=\""+ pinPad +"\"]")

    if portSignalNode != None:

        signalIndex = int(portSignalNode.getAttribute("index"))
        # Convert single digit [0-9] string to the two digit [00-09] string, For example "PA9" to "PA09"
        signalPad = str(re.sub(r'(?<!\d)(\d)(?!\d)', r'0\1', portSignalNode.getAttribute("pad")))

        if signalIndex != None and signalPad != None:
            portSym_PinPad = coreComponent.createStringSymbol("PORT_PIN_PAD_" + str(signalIndex), None)
            portSym_PinPad.setVisible(False)
            portSym_PinPad.setDefaultValue(signalPad)

            portSym_PinIndex = coreComponent.createIntegerSymbol("PORT_PIN_INDEX_" + str(signalIndex), None)
            portSym_PinIndex.setVisible(False)
            portSym_PinIndex.setDefaultValue(signalIndex)

            portSym_PinIndexTz.setDefaultValue(signalIndex)

            if signalIndex > max_index:
                max_index = signalIndex

    if pinNumber < pincount + 1:
        pin.append(pinNumber)
        pin[pinNumber-1] = coreComponent.createMenuSymbol("PORT_PIN" + str(pinNumber), pinConfiguration)
        pin[pinNumber-1].setLabel("Pin " + str(pin_position[pinNumber-1]))
        pin[pinNumber-1].setDescription("Configuraiton for Pin " + str(pin_position[pinNumber-1]) )

        pinExportName.append(pinNumber)
        pinExportName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_EXPORT_NAME", pin[pinNumber-1])
        pinExportName[pinNumber-1].setDefaultValue(str(pin_position[pinNumber - 1]) + ":" + str(pin_map[pin_position[pinNumber - 1]]))
        pinExportName[pinNumber-1].setReadOnly(True)
    else:
        pin.append(pinNumber)
        pin[pinNumber-1] = coreComponent.createMenuSymbol("PORT_PIN" + str(pinNumber), pinConfiguration)
        pin[pinNumber-1].setLabel("Pin " +  str(pin_position_internal[pinNumber - pincount - 1]))
        pin[pinNumber-1].setDescription("Configuraiton for Pin " + str(pin_position_internal[pinNumber - pincount - 1]))

        pinExportName.append(pinNumber)
        pinExportName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_EXPORT_NAME", pin[pinNumber-1])
        pinExportName[pinNumber-1].setDefaultValue(str(pin_position_internal[pinNumber - pincount - 1]) + ":" + str(pin_map_internal[pin_position_internal[pinNumber - pincount - 1]]))
        pinExportName[pinNumber-1].setReadOnly(True)

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)

    pinGroup.append(pinNumber)
    pinGroup[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PORT_GROUP", pin[pinNumber-1])
    pinGroup[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinGroup[pinNumber-1].setLabel("Group")
    pinGroup[pinNumber-1].setReadOnly(True)

    pinGroupNum.append(pinNumber)
    pinGroupNum[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GROUP", pin[pinNumber-1])
    pinGroupNum[pinNumber-1].setVisible(False)

    if pinNumber < pincount + 1:
        if (pin_map.get(pin_position[pinNumber-1]).startswith("P")) and (pin_map.get(pin_position[pinNumber-1])[-1].isdigit()):
            pin_pos = re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]
            pinGroup[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])
            pinGroupNum[pinNumber-1].setDefaultValue(portGroupName.index(str(pin_map.get(pin_position[pinNumber-1]))[1]))
            availablePinDictionary[str(pinNumber)] = "P" + str(pinGroup[pinNumber-1].getValue()) + pin_pos
            pinBitPosition[pinNumber-1].setDefaultValue(int(pin_pos))
    else:
        if (pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1]).startswith("P")) and (pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1])[-1].isdigit()):
            pin_pos = re.findall('\d+', pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1]))[0]
            pinGroup[pinNumber-1].setDefaultValue(pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1])[1])
            pinGroupNum[pinNumber-1].setDefaultValue(portGroupName.index(str(pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1]))[1]))
            availablePinDictionary[str(pinNumber)] = "P" + str(pinGroup[pinNumber-1].getValue()) + pin_pos
            pinBitPosition[pinNumber-1].setDefaultValue(int(pin_pos))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('name', pinName[pinNumber-1])


    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('function', pinType[pinNumber-1])

    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    pinPeripheralFunction[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('peripheralfunction', pinPeripheralFunction[pinNumber-1])

    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinMode[pinNumber-1].setLabel("Mode")
    pinMode[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('mode', pinMode[pinNumber-1])

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:DIR")
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('direction', pinDirection[pinNumber-1])

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('latch', pinLatch[pinNumber-1])

    pinPullEnable.append(pinNumber)
    pinPullEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PULLEN", pin[pinNumber-1])
    pinPullEnable[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinPullEnable[pinNumber-1].setLabel("Pull Enable")
    pinPullEnable[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('pullen', pinPullEnable[pinNumber-1])

    pinInputEnable.append(pinNumber)
    pinInputEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_INEN", pin[pinNumber-1])
    pinInputEnable[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
    pinInputEnable[pinNumber-1].setLabel("Input Enable")
    pinInputEnable[pinNumber-1].setReadOnly(True)
    symbolsDict.setdefault('input', pinInputEnable[pinNumber-1])

    if portPINCFGOpenDrain.getValue() == True:
        pinOpenDrain.append(pinNumber)
        pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_ODRAIN", pin[pinNumber-1])
        pinOpenDrain[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
        pinOpenDrain[pinNumber-1].setLabel("Open Drain")
        pinOpenDrain[pinNumber-1].setReadOnly(True)
        symbolsDict.setdefault('open drain', pinOpenDrain[pinNumber-1])

    if portPINCFGSlewRate.getValue() == True:
        portSLEWLIMValueGroupNode = getValueGroupNode__Port("PORT", "GROUP", "PINCFG", "SLEWLIM")
        if portSLEWLIMValueGroupNode != None:
            pinSlewRate.append(pinNumber)
            pinSlewRate[pinNumber-1] = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_SLEWRATE", pin[pinNumber-1])
            pinSlewRate[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
            pinSlewRate[pinNumber-1].setLabel("Slew Rate")
            pinSlewRate[pinNumber-1].setDisplayMode("Key")
            for index in range(0, len(portSLEWLIMValueGroupNode.getChildren())):
                portSLEWLIMKeyName = portSLEWLIMValueGroupNode.getChildren()[index].getAttribute("name")
                portSLEWLIMValue = portSLEWLIMValueGroupNode.getChildren()[index].getAttribute("value")
                portSLEWLIMDescription = portSLEWLIMValueGroupNode.getChildren()[index].getAttribute("caption")
                pinSlewRate[pinNumber-1].addKey(portSLEWLIMKeyName, portSLEWLIMValue, portSLEWLIMDescription)
            pinSlewRate[pinNumber-1].setReadOnly(True)
            symbolsDict.setdefault('slewrate', pinSlewRate[pinNumber-1])

    if portPINCFGDriverStrength.getValue() == True:
        pinDrvStr.append(pinNumber)
        pinDrvStr[pinNumber-1] = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_DRVSTR", pin[pinNumber-1])
        pinDrvStr[pinNumber-1].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
        pinDrvStr[pinNumber-1].setLabel("Drive Strength")
        pinDrvStr[pinNumber-1].setDisplayMode("Key")
        pinDrvStr[pinNumber-1].addKey("NORMAL", "0", "Normal")
        pinDrvStr[pinNumber-1].addKey("STRONG", "1", "Strong")
        pinDrvStr[pinNumber-1].setReadOnly(True)
        symbolsDict.setdefault('drv', pinDrvStr[pinNumber-1])

    ## Add symbol to global dictionary
    pinSymbolsDictionary.setdefault(pinNumber, symbolsDict)
    
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
    portSym_PIN_PINCFG[pinNumber-1].setDependencies(setupPortPINCFG, ["PIN_" + str(pinNumber) +"_INEN", "PIN_" + str(pinNumber) +"_PULLEN", "PIN_" + str(pinNumber) +"_PERIPHERAL_FUNCTION", "PIN_" + str(pinNumber) + "_DRVSTR", "PIN_" + str(pinNumber) + "_ODRAIN", "PIN_" + str(pinNumber) + "_SLEWRATE"])

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        pinSecurity = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_IS_NON_SECURE", pin[pinNumber-1])
        pinSecurity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:WRCONFIG")
        pinSecurity.setLabel("Security mode")
        pinSecurity.addKey("SECURE", "0", "False")
        pinSecurity.addKey("NON-SECURE", "1", "True")
        pinSecurity.setOutputMode("Key")
        pinSecurity.setDisplayMode("Key")
        pinSecurity.setVisible(True)
        pinSecurity.setDefaultValue(0)
        if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
            pinSecurity.setReadOnly(Database.getSymbolValue("core", "PORT_IS_NON_SECURE") == False)
        pinSecurity.setDependencies(update_port_nonsec_mask, ["PIN_" + str(pinNumber) + "_IS_NON_SECURE"])
        symbolsDict.setdefault('trustzone', pinSecurity)

portSym_PinMaxIndex.setDefaultValue(max_index)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
        pinSecurityVisibility = coreComponent.createBooleanSymbol("PIN_SECURITY_VISIBILITY", None)
        pinSecurityVisibility.setVisible(False)
        pinSecurityVisibility.setDependencies(updateSecurityAttributeVisibility, ["core.PORT_IS_NON_SECURE"])



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
portSym_PinCount.setDefaultValue(internalPincount)

global group
group = [0 for i in range(int(portModuleGC.getAttribute("count")))]

global portPin
portPin = []

global usePort
usePort = []
evsysDep = []
port = []
visibility = False
portSym_GroupName = []

portEvsysActionNode = getValueGroupNode__Port("PORT", "GROUP", "EVCTRL", "EVACT0")
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
    usePort[portNumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:PMUX")
    usePort[portNumber].setLabel("Use PORT GROUP " + str(portGroupName[portNumber]))
    usePort[portNumber].setValue(True, 1)
    usePort[portNumber].setVisible(visibility)

    portSym_PORT_DIR = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_DIR", port[portNumber])
    portSym_PORT_DIR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:DIR")
    portSym_PORT_DIR.setLabel("Port Pin Direction")
    portSym_PORT_DIR.setVisible(visibility)
    portSym_PORT_DIR.setDefaultValue(str(hex(0)))
    portSym_PORT_DIR.setDependencies(setupPortDir, pinDirList)

    portSym_PORT_LATCH = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_OUT", port[portNumber])
    portSym_PORT_LATCH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:OUT")
    portSym_PORT_LATCH.setLabel("Port Pin Output Value")
    portSym_PORT_LATCH.setDefaultValue(str(hex(0)))
    portSym_PORT_LATCH.setDependencies(setupPortLat, pinLatchList)
    portSym_PORT_LATCH.setVisible(visibility)

    portSym_PORT_CTRL = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_CTRL", port[portNumber])
    portSym_PORT_CTRL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:CTRL")
    portSym_PORT_CTRL.setLabel("Enable Input Synchronizer")
    portSym_PORT_CTRL.setDefaultValue(str(hex(0)))
    portSym_PORT_CTRL.setVisible(visibility)

    for pinNum in range(0, 32):
        #creating list for port pin
        portPin.append(str(pinNum))

        portSym_PORT_PINCFG = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) , port[portNumber])
        portSym_PORT_PINCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:PINCFG")
        portSym_PORT_PINCFG.setLabel("PORT GROUP " + str(portGroupName[portNumber]) + " PINCFG" + str(pinNum))
        portSym_PORT_PINCFG.setDefaultValue(str(hex(0)))
        portSym_PORT_PINCFG.setVisible(visibility)

        portPad = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PAD_" + str(pinNum), port[portNumber])
        portPad.setVisible(False)
        portPad.setDefaultValue("0")

        portPinUsed = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber) + "_PIN_" + str(pinNum) + "_USED", port[portNumber])
        portPinUsed.setVisible(False)
        portPinUsed.setDefaultValue(False)

    for pinNum in range(0, 16):
        portSym_PORT_PMUX = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PMUX" + str(pinNum) , port[portNumber])
        portSym_PORT_PMUX.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:PMUX")
        portSym_PORT_PMUX.setLabel("PORT GROUP " + str(portGroupName[portNumber]) + " PMUX" + str(pinNum))

        defaultVal = str(hex(0))
        portPinEven = "P" + chr(ord("A") + portNumber) + str(pinNum * 2)
        portPinOdd = "P" + chr(ord("A") + portNumber) + str((pinNum * 2) + 1)

        # Overwrite default value of 0 for pins whose init value is not zero at POR
        if portPinEven in swdPin.keys():
            defaultVal = swdPin[portPinEven]
        if portPinOdd in swdPin.keys():
            defaultVal = str((hex(int(defaultVal, 16) | (int(swdPin[portPinOdd], 16) << 4))))

        portSym_PORT_PMUX.setDefaultValue(defaultVal)
        portSym_PORT_PMUX.setVisible(visibility)
        portSym_PORT_PMUX.setDependencies(setupPortPinMux, pinPinMuxList)

    if portEvsysActionNode != None:
        portEVSYS = coreComponent.createMenuSymbol("PORT_MENU_EVSYS" + str(portNumber), port[portNumber])
        portEVSYS.setLabel("EVENT System Configuraiton")

        for i in range(0, 4):
            portEVSYSEnable = coreComponent.createBooleanSymbol("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ENABLE", portEVSYS)
            portEVSYSEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:EVCTRL")
            portEVSYSEnable.setLabel("Enable Event" + str(i) + " Input")
            evsysDep.append("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ENABLE")

            portEvsysAction = coreComponent.createKeyValueSetSymbol("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_ACTION",portEVSYSEnable)
            portEvsysAction.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:EVCTRL")
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
            portEvsysPin.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:EVCTRL")
            portEvsysPin.setLabel("Event" + str(i) + " Pin")
            for index in range(0, 32):
                portEvsysPin.addKey("P" + str(index), str(index) , "Pin " + str(index))

            portEvsysAction.setDefaultValue(0)
            portEvsysAction.setOutputMode("Value")
            portEvsysAction.setDisplayMode("Description")
            evsysDep.append("PORT_" + str(portNumber) + "_EVACT" + str(i) + "_PIN")

        portSym_PORT_EVCTRL = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_EVCTRL", port[portNumber])
        portSym_PORT_EVCTRL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:port_u2210;register:EVCTRL")
        portSym_PORT_EVCTRL.setLabel("Port Event Control")
        portSym_PORT_EVCTRL.setVisible(True)
        #portSym_PORT_EVCTRL.setVisible(visibility)
        portSym_PORT_EVCTRL.setDefaultValue(str(hex(0)))
        portSym_PORT_EVCTRL.setDependencies(evsysControl, evsysDep)

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            pin_nonsec_mask = coreComponent.createHexSymbol("PORT_GROUP_" + str(portNumber) + "_NONSEC", port[portNumber])
            pin_nonsec_mask.setVisible(False)
            pin_nonsec_mask.setDefaultValue(0)

portSymPMUX_FUNCTIONS_List = coreComponent.createListSymbol("PERIPHERAL_PMUX_FUNCTIONS_LIST", None)
portSymPMUX_FUNCTIONS_List.setVisible(False)

portSymPMUX_FUNCTIONS = coreComponent.createListEntrySymbol("PERIPHERAL_PMUX_FUNCTIONS", None)
portSymPMUX_FUNCTIONS.setTarget("core.PERIPHERAL_PMUX_FUNCTIONS_LIST")
portSymPMUX_FUNCTIONS.setVisible(False)

portPMUXValueGroupValues = 0
portPMUXValueGroupNode = getValueGroupNode__Port("PORT", "GROUP", "PMUX", "PMUXE")

if portPMUXValueGroupNode != None:
    portPMUXValueGroupValues = portPMUXValueGroupNode.getChildren()

portSymPMUXMap = coreComponent.createKeyValueSetSymbol("PIN_PERIPHERAL_FUNCTION_MAP", None)
portSymPMUXMap.setVisible(False)
for index in range(0, len(portPMUXValueGroupValues)):
    portPMUXKeyName = portPMUXValueGroupValues[index].getAttribute("name")
    portPMUXValue = portPMUXValueGroupValues[index].getAttribute("value")
    portPMUXDescription = portPMUXValueGroupValues[index].getAttribute("caption")
    portSymPMUXMap.addKey(portPMUXKeyName, portPMUXValue , portPMUXDescription)

for i in range(portSymPMUXMap.getKeyCount()):
    enum_value = "PERIPHERAL_FUNCTION_" + portSymPMUXMap.getKey(i) + " = " + portSymPMUXMap.getKeyValue(i) + ','
    portSymPMUX_FUNCTIONS.addValue(enum_value)
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

portExportFile = coreComponent.createFileSymbol("PORT_EXPORT_FILE", None)
portExportFile.setSourcePath("../peripheral/port_u2210/templates/export/plib_port_export.ftl")
portExportFile.setOutputName("pin_configurations.csv")
portExportFile.setType("IMPORTANT")
portExportFile.setMarkup(True)
portExportFile.setEnabled(portExport.getValue())
portExportFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["value"]), ["PORT_EXPORT"])

bspIncludeFile = coreComponent.createFileSymbol("PORT_BSP_HEADER", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/port_u2210/templates/plib_port_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspSourceFile = coreComponent.createFileSymbol("PORT_BSP_SOURCE", None)
bspSourceFile.setType("STRING")
bspSourceFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspSourceFile.setSourcePath("../peripheral/port_u2210/templates/plib_port_bsp.c.ftl")
bspSourceFile.setMarkup(True)

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

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":

    nonSecportSym_HeaderFile = coreComponent.createFileSymbol("PORT_HEADER_NONSEC", None)
    nonSecportSym_HeaderFile.setSourcePath("../peripheral/port_u2210/templates/trustZone/plib_port_nonsecure.h.ftl")
    nonSecportSym_HeaderFile.setOutputName("plib_port.h")
    nonSecportSym_HeaderFile.setDestPath("/peripheral/port/")
    nonSecportSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/port/")
    nonSecportSym_HeaderFile.setType("HEADER")
    nonSecportSym_HeaderFile.setMarkup(True)

    nonportSym_SourceFile = coreComponent.createFileSymbol("PORT_SOURCE_NONSEC", None)
    nonportSym_SourceFile.setSourcePath("../peripheral/port_u2210/templates/trustZone/plib_port_nonsecure.c.ftl")
    nonportSym_SourceFile.setOutputName("plib_port.c")
    nonportSym_SourceFile.setDestPath("/peripheral/port/")
    nonportSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/port/")
    nonportSym_SourceFile.setType("SOURCE")
    nonportSym_SourceFile.setMarkup(True)

    nonSecportSym_SystemDefFile = coreComponent.createFileSymbol("PORT_SYS_DEF_NONSEC", None)
    nonSecportSym_SystemDefFile.setSourcePath("../peripheral/port_u2210/templates/system/definitions.h.ftl")
    nonSecportSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nonSecportSym_SystemDefFile.setType("STRING")
    nonSecportSym_SystemDefFile.setMarkup(True)

    bspSecureIncludeFile = coreComponent.createFileSymbol("PORT_BSP_SECURE_HEADER", None)
    bspSecureIncludeFile.setType("STRING")
    bspSecureIncludeFile.setOutputName("core.LIST_BSP_MACRO_SECURE_INCLUDES")
    bspSecureIncludeFile.setSourcePath("../peripheral/port_u2210/templates/trustZone/plib_port_bsp_secure.h.ftl")
    bspSecureIncludeFile.setMarkup(True)
    bspSecureIncludeFile.setSecurity("SECURE")

    bspSecureSourceFile = coreComponent.createFileSymbol("PORT_BSP_SECURE_SOURCE", None)
    bspSecureSourceFile.setType("STRING")
    bspSecureSourceFile.setOutputName("core.LIST_BSP_SECURE_INITIALIZATION")
    bspSecureSourceFile.setSourcePath("../peripheral/port_u2210/templates/trustZone/plib_port_bsp_secure.c.ftl")
    bspSecureSourceFile.setMarkup(True)
    bspSecureSourceFile.setSecurity("SECURE")

    portSym_HeaderFile.setSecurity("SECURE")
    portSym_SourceFile.setSecurity("SECURE")
    portSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE")
    portSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

