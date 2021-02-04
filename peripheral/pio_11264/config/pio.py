"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))
import re


###############################################Global Variables #############################################
global pinChannel
pinChannel = []
global per_func
per_func = ["GPIO", "A", "B", "C", "D", "E", "F", "G"]
global pinInterrupt
pinInterrupt = []

global port_mskr
port_mskr = {       "A_A" : 0,
                    "A_B" : 0,
                    "A_C" : 0,
                    "A_D" : 0,
                    "A_E" : 0,
                    "A_F" : 0,
                    "A_G" : 0,
                    "A_GPIO" : 0,
                    "B_A" : 0,
                    "B_B" : 0,
                    "B_C" : 0,
                    "B_D" : 0,
                    "B_E" : 0,
                    "B_F" : 0,
                    "B_G" : 0,
                    "B_GPIO" : 0,
                    "C_A" : 0,
                    "C_B" : 0,
                    "C_C" : 0,
                    "C_D" : 0,
                    "C_E" : 0,
                    "C_F" : 0,
                    "C_G" : 0,
                    "C_GPIO" : 0,
                    "D_A" : 0,
                    "D_B" : 0,
                    "D_C" : 0,
                    "D_D" : 0,
                    "D_E" : 0,
                    "D_F" : 0,
                    "D_G" : 0,
                    "D_GPIO" : 0,
                    "E_A" : 0,
                    "E_B" : 0,
                    "E_C" : 0,
                    "E_D" : 0,
                    "E_E" : 0,
                    "E_F" : 0,
                    "E_G" : 0,
                    "E_GPIO" : 0,
                    "F_A" : 0,
                    "F_B" : 0,
                    "F_C" : 0,
                    "F_D" : 0,
                    "F_E" : 0,
                    "F_F" : 0,
                    "F_G" : 0,
                    "F_GPIO" : 0,
                    "G_A" : 0,
                    "G_B" : 0,
                    "G_C" : 0,
                    "G_D" : 0,
                    "G_E" : 0,
                    "G_F" : 0,
                    "G_G" : 0,
                    "G_GPIO" : 0,
                    }
global interruptValues
interruptValues = { "Falling Edge" : 0,
                    "Raising Edge" : 1,
                    "Both Edge"    : 2,
                    "Low Level"    : 3,
                    "High Level"   : 4
}
global latchValues
latchValues = {     "A" : 0,
                    "B" : 0,
                    "C" : 0,
                    "D" : 0,
                    "E" : 0,
                    "F" : 0,
                    "G" : 0
}

global sort_alphanumeric
global prev_package
global cur_package
prev_package = ""
cur_package = ""
global pioSymChannel
pioSymChannel = ["A", "B", "C", "D", "E", "F", "G"]
global pin_map
pin_map = {}
global pin_position
pin_position = []
##packagepinout map
global package
package = {}
## total number of pins
global packagePinCount
packagePinCount = 0
## Number of unique pinouts
global uniquePinout
uniquePinout = 1
global debounceFilterEnabledByDefault
debounceFilterEnabledByDefault = False
global availablePinDictionary
availablePinDictionary = {}

##########################################################################################################################
pinMode = []
pinDirection = []
pinLatch = []
pinOpenDrain = []
pinPullUp = []
pinPullDown = []
pinLatchValue = []
pin = []
pinName = []
pinType = []
pinPeripheralFunction = []
pinBitPosition = []

pincfgrValue = []
drvSTRVal = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PIO"]/value-group@[name="PIO_CFGR0__DRVSTR"]')

node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PIO\"]/instance@[name=\"PIOA\"]/parameters/param@[name=\"DEBOUNCE_GLITCH_ACTIVE\"]")
pioDebounceConf = coreComponent.createBooleanSymbol("PIO_DEBOUNCE_NOT_CONFIGURABLE", None)
pioDebounceConf.setVisible(False)
if node != None:
    debounceFilterEnabledByDefault = True
    pioDebounceConf.setDefaultValue(True)
else:
    debounceFilterEnabledByDefault = False
    pioDebounceConf.setDefaultValue(False)

###########################################Local Variables################################################################

############################################Callbacks##############################################

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

    ### No need to process if the device has only one pinout but multiple packages eg: TQFP, LQFP and QFN
    if uniquePinout > 1:
        cur_package = package.get(pinout["value"])

        ### No need to generate Pin map again for same pinout
        if cur_package != prev_package:
            pin_map = {}
            pin_position = []
            portBitPositionNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(package.get(pinout["value"])) + "\"]")
            for id in range(0,len(portBitPositionNode.getChildren())):
                if "BGA" in pinout["value"]:
                    pin_map[portBitPositionNode.getChildren()[id].getAttribute("position")] = portBitPositionNode.getChildren()[id].getAttribute("pad")
                else:
                    pin_map[int(portBitPositionNode.getChildren()[id].getAttribute("position"))] = portBitPositionNode.getChildren()[id].getAttribute("pad")

            if "BGA" in pinout["value"]:
                ## BGA package ID's are alphanumeric unlike TQFP special sorting required
                pin_position = sort_alphanumeric(pin_map.keys())
            else:
                pin_position = sorted(pin_map.keys())

        for index in range(1, len(pin) + 1):
            if index <= len(pin_position):
                if not pin[index - 1].getVisible():
                    pin[index - 1].setVisible(True)
                pin[index - 1].setLabel("Pin " + str(pin_position[index - 1]))
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


def updateInputFilter(symbol, event):
    pin_num = int(str(symbol.getID()).split("PIN_")[1].split("_IFEN")[0])

    if event["value"] == "Debounce Filter":
        ifen = 1
        ifscen = 1
    elif event["value"] == "Glitch Filter":
        ifen = 1
        ifscen = 0
    else:
        ifen = 0
        ifscen = 0

    symbol.setValue(ifen)
    event["source"].setSymbolValue("PIN_" + str(pin_num) + "_IFSCEN", ifscen)


def portFunc(pin, func):
    global port_mskr
    global per_func
    pin_num = int(str(pin.getID()).split("PIN_")[1].split("_PIO_PIN")[0])
    port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")
    bit_pos = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_PIN")
    if port:
        # If a function is assigned to the pin and that function is not something
        # PIO understands,configure the PIN as GPIO. Useful in BSP configured functions.
        # For external functions outside the scope of PIO, these configurations won't matter.
        if func ["value"] and func["value"] not in per_func:
            function = "GPIO"
        else:
            function = func["value"]

        key = port + "_" + function
        if function in per_func:
            for id in per_func:
                if id == function:
                    port_mskr[key] |= (1 << bit_pos)
                else:
                    port_mskr[port + "_" + id] &= ~(1 << bit_pos)
        else:
                        for id in per_func:
                            port_mskr[port + "_" + id] &= ~(1 << bit_pos)

        for id in per_func:
            Database.setSymbolValue("core", "PORT_" + str(port) + "_MSKR_Value" + str(id), str(hex(port_mskr[port + "_" + id])), 2)




def pinCFGR (pin, cfgr_reg):
    cfgr = 0
    global port_mskr
    global per_func
    global interruptValues
    global drvStrengthIsConfigurable
    pin_num = int(str(pin.getID()).split("PIN_")[1].split("_CFGR_Value")[0])
    port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")
    bit_pos = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_PIN")
    pullup = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PU")
    pulldown = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PD")
    opendrain = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_OD")
    interrupt = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_INTERRUPT")
    direction = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_DIR")
    schmitt = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_ST")
    tamper = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_TAMPER")
    if debounceFilterEnabledByDefault == False:
        filterMask = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_IFEN")
        filterclock = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_IFSCEN")
    driver = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_DRV")
    if port:
        if pullup:
            cfgr |= 1 << 9
        if pulldown:
            cfgr |= 1 << 10
        if opendrain:
            cfgr |= 1 << 14
        if direction:
            cfgr |= 1 << 8
        if interrupt:
            cfgr |= interruptValues.get(interrupt) << 24
        if schmitt:
            cfgr |= 1 << 15
        if tamper:
            cfgr |= 1 << 31
        if driver:
            cfgr |= driver << 16
        if debounceFilterEnabledByDefault == False:
            if filterMask:
                cfgr |= 1 << 12
            if filterclock == 1:
                cfgr |= 1 << 13

        Database.setSymbolValue("core", "PORT_" + str(port) + "_CFGR_Value" + str(bit_pos), str(hex(cfgr)), 2)

def portLatch(pin, latch):
    global latchValues
    pin_num = int(str(pin.getID()).split("PIN_")[1].split("_LAT")[0])
    port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")
    bit_pos = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_PIN")
    if port in latchValues:
        if latch["value"]:
            latchValues[port] |= 1 << bit_pos
        else:
            latchValues[port] &= ~(1 << bit_pos)

        Database.setSymbolValue("core", "PORT_" + str(port) + "_LATCH", str(hex(latchValues[port])), 2)

def portInterrupt(pin, interrupt):
    global pinInterrupt
    pin_num = int(str(pin.getID()).split("PIN_")[1].split("_PIO_INTERRUPT")[0])
    port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")

    atLeastOneInterruptOnChannel = True
    if interrupt["value"] == "":
        # if interrupt has been disabled for a particular pin, then see if is it disabled for all the pins of
        # corresponding channel; if so, then uncheck corresponding port interrupt in GUI.
        atLeastOneInterruptOnChannel = False
        for pinNumber in range(1, packagePinCount+1):
            if port == pinChannel[pinNumber-1].getValue():
                if pinInterrupt[pinNumber-1].getValue() != "":
                    atLeastOneInterruptOnChannel = True
                    break

    if atLeastOneInterruptOnChannel == True:
        Database.setSymbolValue("core", "PORT_" + str(port) + "_INTERRUPT_USED", True, 2)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_ENABLE", True, 1)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_HANDLER", "PIO"+str(port)+"_InterruptHandler", 1)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_HANDLER_LOCK", True, 1)
    else:
        Database.setSymbolValue("core", "PORT_" + str(port) + "_INTERRUPT_USED", False, 2)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_ENABLE", False, 1)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_HANDLER", "PIO"+str(port)+"_Handler", 1)
        Database.setSymbolValue("core", "PIO"+str(port)+"_INTERRUPT_HANDLER_LOCK", False, 1)

#####################################################################################################################

##########################################################################################################################
###################################################################################################
######################################### PIO Main Menu  ##########################################
###################################################################################################

pioMenu = coreComponent.createMenuSymbol("PIO_MENU", None)
pioMenu.setLabel("Ports (PIO)")
pioMenu.setDescription("Configuration for PIO PLIB")

pioPortEEnable = coreComponent.createBooleanSymbol("PIO_PORT_E_ENBALE", pioMenu)
pioPortEEnable.setVisible(False)
pioPortEEnable.setDefaultValue(Peripheral.instanceExists("PIO", "PIOE"))

pioPortFEnable = coreComponent.createBooleanSymbol("PIO_PORT_F_ENBALE", pioMenu)
pioPortFEnable.setVisible(False)
pioPortFEnable.setDefaultValue(Peripheral.instanceExists("PIO", "PIOF"))

pioPortGEnable = coreComponent.createBooleanSymbol("PIO_PORT_G_ENBALE", pioMenu)
pioPortGEnable.setVisible(False)
pioPortGEnable.setDefaultValue(Peripheral.instanceExists("PIO", "PIOG"))

pioEnable = coreComponent.createBooleanSymbol("PIO_ENABLE", pioMenu)
pioEnable.setLabel("Use PIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)

Database.setSymbolValue("core",  "PIO_CLOCK_ENABLE", True)

# Build package pinout map
packageNode = ATDF.getNode("/avr-tools-device-file/variants")
for id in range(0,len(packageNode.getChildren())):
    package[packageNode.getChildren()[id].getAttribute("package")] = packageNode.getChildren()[id].getAttribute("pinout")

## Find Number of unique pinouts
uniquePinout = len(set(package.values()))

## get the pin count
packagePinCount = int(re.findall(r'\d+', package.keys()[0])[0])

pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, package.values())
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(True)

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################

pinConfiguration = coreComponent.createMenuSymbol("PIO_PIN_CONFIGURATION", pioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuration for PIO Pins")

pinTotalPins = coreComponent.createIntegerSymbol("PIO_PIN_TOTAL" , pinConfiguration)
pinTotalPins.setVisible(False)
pinTotalPins.setDefaultValue(packagePinCount)

# Needed to map port system APIs to PLIB APIs
pioSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
pioSymAPI_Prefix.setDefaultValue("PIO")
pioSymAPI_Prefix.setVisible(False)

portBitPositionNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(pioPackage.getValue()) + "\"]")
for id in range(0,len(portBitPositionNode.getChildren())):
    if "BGA" in pioPackage.getValue():
        pin_map[portBitPositionNode.getChildren()[id].getAttribute("position")] = portBitPositionNode.getChildren()[id].getAttribute("pad")
    else:
        pin_map[int(portBitPositionNode.getChildren()[id].getAttribute("position"))] = portBitPositionNode.getChildren()[id].getAttribute("pad")

if "BGA" in pioPackage.getValue():
    pin_position = sort_alphanumeric(pin_map.keys())
else:
    pin_position = sorted(pin_map.keys())

# Note that all the lists below starts from 0th index and goes till "packagePinCount-1"
# But actual pin numbers on the device starts from 1 (not from 0) and goes till "packagePinCount"
# that is why "pinNumber-1" is used to index the lists wherever applicable.
for pinNumber in range(1, packagePinCount + 1):
    pin.append(pinNumber)
    pin[pinNumber-1]= coreComponent.createMenuSymbol("PIO_PIN_CONFIGURATION" + str(pinNumber), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pin_position[pinNumber-1]))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pin_position[pinNumber-1]))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    #pinType[pinNumber-1].setReadOnly(True)

    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    pinPeripheralFunction[pinNumber-1].setReadOnly(True)

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PIO_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)
    pinBitPosition[pinNumber-1].setDependencies(portFunc, ["PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION"])

    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")

    if pin_map.get(pin_position[pinNumber-1]).startswith("P"):
        pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]))
        pinChannel[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])

        availablePinDictionary[str(pinNumber)] = "P" + str(pinChannel[pinNumber-1].getValue()) + str(pinBitPosition[pinNumber-1].getValue())
    pinChannel[pinNumber-1].setReadOnly(True)

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

    pinLatchValue.append(pinNumber)
    pinLatchValue[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT_Value", pin[pinNumber-1])
    pinLatchValue[pinNumber-1].setReadOnly(True)
    pinLatchValue[pinNumber-1].setVisible(False)
    pinLatchValue[pinNumber-1].setDependencies(portLatch, ["PIN_" + str(pinNumber) + "_LAT"])

    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    pinOpenDrain[pinNumber-1].setReadOnly(True)

    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PU", pin[pinNumber-1])
    pinPullUp[pinNumber-1].setLabel("Pull Up")
    pinPullUp[pinNumber-1].setReadOnly(True)

    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PD", pin[pinNumber-1])
    pinPullDown[pinNumber-1].setLabel("Pull Down")
    pinPullDown[pinNumber-1].setReadOnly(True)

    pinSchmitt = coreComponent.createBooleanSymbol("PIN_" + str(pinNumber) + "_ST", pin[pinNumber-1])
    pinSchmitt.setLabel("Schmitt Trigger")

    pinTrigger = coreComponent.createBooleanSymbol("PIN_" + str(pinNumber) + "_TAMPER", pin[pinNumber-1])
    pinTrigger.setLabel("Tamper Enable")

    pinDRV = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_DRV", pin[pinNumber-1])
    pinDRV.setLabel("Driver Strength")
    pinDRV.setOutputMode("Value")
    pinDRV.setDisplayMode("Description")
    for id in range(0,len(drvSTRVal.getChildren())):
        pinDRV.addKey(drvSTRVal.getChildren()[id].getAttribute("name"), str(drvSTRVal.getChildren()[id].getAttribute("value")) , drvSTRVal.getChildren()[id].getAttribute("caption") )

    # This symbol is used to map the UI manager selection to the corresponding symbol in the tree view. Will not be
    # displayed in the tree view
    pinFilterTypeString = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_FILTER", pin[pinNumber-1])
    pinFilterTypeString.setVisible(False)
    pinFilterTypeString.setReadOnly(True)

    pinFilter = coreComponent.createBooleanSymbol("PIN_" + str(pinNumber) + "_IFEN", pin[pinNumber-1])
    pinFilter.setLabel("Glitch Filter Enable")
    pinFilter.setDependencies(updateInputFilter, ["PIN_" + str(pinNumber) + "_PIO_FILTER"])
    if debounceFilterEnabledByDefault:
        pinFilter.setVisible(False)

    pinFilterClock = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_IFSCEN", pin[pinNumber-1])
    pinFilterClock.setLabel("Glitch filter Clock Source ")
    pinFilterClock.addKey("MCK", str(0) , "The glitch filter is able to filter glitches with a duration < tmck/2" )
    pinFilterClock.addKey("SLCK", str(1) , "The debouncing filter is able to filter pulses with a duration < tdiv_slck/2" )
    if debounceFilterEnabledByDefault:
        pinFilterClock.setVisible(False)

    # This symbol ID name is split and pin number is extracted and used inside "setupInterrupt" function. so be careful while changing the name of this ID.
    pinInterrupt.append(pinNumber)
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("PIO Interrupt")
    pinInterrupt[pinNumber-1].setReadOnly(True)

    # This symbol ID name is split and pin number is extracted and used inside "setupInterrupt" function. so be careful while changing the name of this ID.
    pinInterruptValue = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT_VAL", pin[pinNumber-1])
    pinInterruptValue.setReadOnly(True)
    pinInterruptValue.setVisible(False)
    pinInterruptValue.setDependencies(portInterrupt, ["PIN_" + str(pinNumber) + "_PIO_INTERRUPT"])

    pincfgrValue.append(pinNumber)
    pincfgrValue[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_CFGR_Value", pin[pinNumber-1])
    pincfgrValue[pinNumber-1].setReadOnly(True)
    pincfgrValue[pinNumber-1].setVisible(False)
    pincfgrValue[pinNumber-1].setDependencies(pinCFGR, ["PIN_" + str(pinNumber) + "_PD", "PIN_" + str(pinNumber) + "_PU", "PIN_" + str(pinNumber) + "_OD", "PIN_" + str(pinNumber) + "_DIR", "PIN_" + str(pinNumber) + "_PIO_INTERRUPT", "PIN_" + str(pinNumber) + "_IFSCEN", "PIN_" + str(pinNumber) + "_IFEN", "PIN_" + str(pinNumber) + "_DRV", "PIN_" + str(pinNumber) + "_TAMPER", "PIN_" + str(pinNumber) + "_ST" ])

packageUpdate = coreComponent.createBooleanSymbol("PACKAGE_UPDATE_DUMMY", None)
packageUpdate.setVisible(False)
packageUpdate.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

portTotalChannels = coreComponent.createIntegerSymbol("PORT_CHANNEL_TOTAL" , None)
portTotalChannels.setVisible(False)
portTotalChannels.setDefaultValue(len(pioSymChannel))

for port in pioSymChannel:
    mskr = 0
    portLATCH = coreComponent.createStringSymbol("PORT_" + str(port) + "_LATCH", None)
    portLATCH.setReadOnly(True)
    portLATCH.setVisible(False)
    portLATCH.setDefaultValue(str(hex(0)))

    for pin in range(0,32):
        mskr = 1 << pin
        pincfgr = coreComponent.createStringSymbol("PORT_" + str(port) + "_CFGR_Value" + str(pin), None)
        pincfgr.setReadOnly(True)
        pincfgr.setVisible(False)
        pincfgr.setDefaultValue(str(hex(0)))

        pinmskr = coreComponent.createStringSymbol("PORT_" + str(port) + "_MSKR_Value" + str(pin), None)
        pinmskr.setReadOnly(True)
        pinmskr.setVisible(False)
        pinmskr.setDefaultValue(str(hex(mskr)))

for port in pioSymChannel:

    portChannelName = coreComponent.createStringSymbol("PORT_CHANNEL_" + str(pioSymChannel.index(port)) + "_NAME" , None)
    portChannelName.setVisible(False)
    portChannelName.setDefaultValue(str(port))

    portIntEnable = coreComponent.createBooleanSymbol("PORT_" + str(port) + "_INTERRUPT_USED", None)
    portIntEnable.setReadOnly(True)
    portIntEnable.setVisible(False)
    portIntEnable.setDefaultValue(False)

    for per in per_func:
        portperMSKR = coreComponent.createStringSymbol("PORT_" + str(port) + "_MSKR_Value" + str(per), None)
        portperMSKR.setReadOnly(True)
        portperMSKR.setVisible(False)
        portperMSKR.setDefaultValue(str(hex(0)))

count = 0
for func in per_func:
    portperMSKR = coreComponent.createStringSymbol("FUNC_" + str(func) + "_CFGR_Value", None)
    portperMSKR.setReadOnly(True)
    portperMSKR.setVisible(False)
    portperMSKR.setDefaultValue(str(hex(count)))
    count += 1

portConfiguration = coreComponent.createMenuSymbol("PIO_CONFIGURATION", pioEnable)
portConfiguration.setLabel("PIO Registers Configuration")
scdrNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PIO\"]/register-group@[name=\"PIO\"]/register@[name=\"PIO_SCDR\"]")
if scdrNode:
    pioSCLKDIV = coreComponent.createIntegerSymbol("PORT_SCLK_DIV", portConfiguration)
    pioSCLKDIV.setLabel("Slow Clock Divider Selection for Debouncing")
    pioSCLKDIV.setMax(16383)
    pioSCLKDIV.setMin(0)
    pioSCLKDIV.setDefaultValue(0)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pioHeaderFile = coreComponent.createFileSymbol("PIO_HEADER", None)
pioHeaderFile.setSourcePath("../peripheral/pio_11264/templates/plib_pio.h.ftl")
pioHeaderFile.setOutputName("plib_pio.h")
pioHeaderFile.setDestPath("/peripheral/pio/")
pioHeaderFile.setProjectPath("config/" + configName +"/peripheral/pio/")
pioHeaderFile.setType("HEADER")
pioHeaderFile.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol("PIO_SOURCE", None)
pioSource1File.setSourcePath("../peripheral/pio_11264/templates/plib_pio.c.ftl")
pioSource1File.setOutputName("plib_pio.c")
pioSource1File.setDestPath("/peripheral/pio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)

pioSystemInitFile = coreComponent.createFileSymbol("PIO_INIT", None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
pioSystemInitFile.setSourcePath("../peripheral/pio_11264/templates/system/initialization.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol("PIO_DEF", None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/pio_11264/templates/system/definitions.h.ftl")
pioSystemDefFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("PIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/pio_11264/templates/plib_pio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PIO_BSP_H", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/pio_11264/templates/plib_pio_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PIO_BSP_C", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspIncludeFile.setSourcePath("../peripheral/pio_11264/templates/plib_pio_bsp.c.ftl")
bspIncludeFile.setMarkup(True)
