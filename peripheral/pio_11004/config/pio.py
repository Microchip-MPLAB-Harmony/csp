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
print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

global pioSymChannel
pioSymChannel = ["A", "B", "C", "D", "E"]
global uniquePinout
uniquePinout = 1
##package pinout map
global package
package = {}
global pin_map
pin_map = {}
global pin_position
pin_position = []
global sort_alphanumeric

global availablePinDictionary
availablePinDictionary = {}

registerNodeTemplate = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[name=\"{2}\"]"

global sysioPresent

sysioPresent = coreComponent.createBooleanSymbol("CCFG_SYSIO_PRESENT", None)
sysioPresent.setVisible(False)
sysioPresent.setDefaultValue(ATDF.getNode(registerNodeTemplate.format("MATRIX", "MATRIX", "CCFG_SYSIO"))is not None)

slewRateControlPresent = coreComponent.createBooleanSymbol("PIO_SLEWR_PRESENT", None)
slewRateControlPresent.setVisible(False)
slewRateControlPresent.setDefaultValue(ATDF.getNode(registerNodeTemplate.format("PIO", "PIO", "PIO_SLEWR")) is not None)

driverControlPresent = coreComponent.createBooleanSymbol("PIO_DRIVER_PRESENT", None)
driverControlPresent.setVisible(False)
driverControlPresent.setDefaultValue(ATDF.getNode(registerNodeTemplate.format("PIO", "PIO", "PIO_DRIVER")) is not None)

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
    channelIndex = pioSymChannel.index((symbol.getID()).split("_")[1])
    if portInterrupt[channelIndex].getValue() == True and Database.getSymbolValue("core", pioSymInterruptVectorUpdate[channelIndex]) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Dependency Function to show or hide the warning message depending on Clock
def ClockStatusWarning(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Dependency Function to pass interrupt related info to Interrupt Manager.
# This function will be entered only by internal change happening to PORT channel interrupt, never by manual
# change because channel interrupt is not user configurable directly.
def pioInterruptControl(pioInterrupt, event):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    # Split the id name by "_" and put all the split names in the list "i"
    i = event["id"].split("_")
    k = pioSymChannel.index(i[1])

    if (event["value"] == True):
        Database.setSymbolValue("core", pioSymInterruptVector[k], True, 1)
        Database.setSymbolValue("core", pioSymInterruptHandler[k], "PIO" + i[1] + "_InterruptHandler", 1)
        Database.setSymbolValue("core", pioSymInterruptHandlerLock[k], True, 1)
    else :
        Database.setSymbolValue("core", pioSymInterruptVector[k], False, 1)
        Database.setSymbolValue("core", pioSymInterruptHandler[k], "PIO" + i[1] + "_Handler", 1)
        Database.setSymbolValue("core", pioSymInterruptHandlerLock[k], False, 1)

def pinLatchCal(pin, event):
    global pioSym_PIO_SODR
    global pinDirection
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        SODR_Value = pioSym_PIO_SODR[channelIndex].getValue()

        if event["value"] == "High":
            SODR_Value |= 1 << bit_pos
        else:
            SODR_Value &= ~(1 << bit_pos)

        pioSym_PIO_SODR[channelIndex].setValue(SODR_Value, 2)

def pinDirCal(pin, event):
    global pioSym_PIO_OER
    global pinChannel
    global pinBitPosition
    global pinLatch

    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        OER_Value = pioSym_PIO_OER[channelIndex].getValue()

        if event["value"] == "Out":
            OER_Value |= 1 << bit_pos
        else:
            OER_Value &= ~(1 << bit_pos)

        pioSym_PIO_OER[channelIndex].setValue(OER_Value, 2)


def pinFunctionCal(pType, pFunction):
    global sysioPresent
    global pioSym_PIO_PDR
    global pioSym_PIO_ABCDSR1
    global pioSym_PIO_ABCDSR2
    global pioMatrixSym_CCFG_SYSIO
    global pinChannel
    global pinBitPosition

    pin_num = int((pType.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()

        PDR_Value = pioSym_PIO_PDR[channelIndex].getValue()
        ABCDSR1_Value = pioSym_PIO_ABCDSR1[channelIndex].getValue()
        ABCDSR2_Value = pioSym_PIO_ABCDSR2[channelIndex].getValue()

        if (pFunction["value"] == "A") or (pFunction["value"] == "B") or (pFunction["value"] == "C") or (pFunction["value"] == "D"):
            PDR_Value |= 1 << bit_pos

            if (pFunction["value"] == "A"):
                ABCDSR1_Value &= ~(1 << bit_pos)
                ABCDSR2_Value &= ~(1 << bit_pos)
            elif (pFunction["value"] == "B"):
                ABCDSR1_Value |= (1 << bit_pos)
                ABCDSR2_Value &= ~(1 << bit_pos)
            elif (pFunction["value"] == "C"):
                ABCDSR1_Value &= ~(1 << bit_pos)
                ABCDSR2_Value |= (1 << bit_pos)
            else:
                ABCDSR1_Value |= (1 << bit_pos)
                ABCDSR2_Value |= (1 << bit_pos)

        else:
            ABCDSR1_Value &= ~(1 << bit_pos)
            ABCDSR2_Value &= ~(1 << bit_pos)
            PDR_Value &= ~(1 << bit_pos)

        if sysioPresent.getValue():
            if (portChannel == "B") and ((bit_pos == 4) or (bit_pos == 5) or (bit_pos == 6) or (bit_pos == 7) or (bit_pos == 12)):
                CCFG_SYSIO_Value = pioMatrixSym_CCFG_SYSIO.getValue()
                if (pType.getValue() == "ICE_TDI") or (pType.getValue() == "ICE_TDO/TRACESWO") or (pType.getValue() == "ICE_TMS/SWDIO") or (pType.getValue() == "ICE_TCK/SWDCLK") or (pType.getValue() == "EFC_ERASE") or (pFunction["value"] == ""):
                    CCFG_SYSIO_Value &= ~(1 << bit_pos)
                else:
                    CCFG_SYSIO_Value |= (1 << bit_pos)
                pioMatrixSym_CCFG_SYSIO.setValue(CCFG_SYSIO_Value, 2)

        pioSym_PIO_PDR[channelIndex].setValue(PDR_Value, 2)
        pioSym_PIO_ABCDSR1[channelIndex].setValue(ABCDSR1_Value, 2)
        pioSym_PIO_ABCDSR2[channelIndex].setValue(ABCDSR2_Value, 2)

def pinInterruptCal(pin, event):
    global pioSym_PIO_AIMER
    global pioSym_PIO_LSR
    global pioSym_PIO_REHLSR
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
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
        AIMER_Value = pioSym_PIO_AIMER[channelIndex].getValue()
        LSR_Value = pioSym_PIO_LSR[channelIndex].getValue()
        REHLSR_Value = pioSym_PIO_REHLSR[channelIndex].getValue()

        if (event["value"] == "Falling Edge") or (event["value"] == "Raising Edge") or (event["value"] == "Low Level") or (event["value"] == "High Level"):
            AIMER_Value |= 1 << bit_pos

            if (event["value"] == "Falling Edge"):
                LSR_Value &= ~(1 << bit_pos)
                REHLSR_Value &= ~(1 << bit_pos)
            elif (event["value"] == "Raising Edge"):
                LSR_Value &= ~(1 << bit_pos)
                REHLSR_Value |= (1 << bit_pos)
            elif (event["value"] == "Low Level"):
                LSR_Value |= (1 << bit_pos)
                REHLSR_Value &= ~(1 << bit_pos)
            else:
                LSR_Value |= (1 << bit_pos)
                REHLSR_Value |= (1 << bit_pos)

        else:
            AIMER_Value &= ~(1 << bit_pos)
            LSR_Value &= ~(1 << bit_pos)
            REHLSR_Value &= ~(1 << bit_pos)

        pioSym_PIO_LSR[channelIndex].setValue(LSR_Value, 2)
        pioSym_PIO_REHLSR[channelIndex].setValue(REHLSR_Value, 2)
        pioSym_PIO_AIMER[channelIndex].setValue(AIMER_Value, 2)

def pinOpenDrainCal(pin, event):
    global pioSym_PIO_MDER
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        MDER_Value = pioSym_PIO_MDER[channelIndex].getValue()

        if event["value"] == "True":
            MDER_Value |= 1 << bit_pos
        else:
            MDER_Value &= ~(1 << bit_pos)

        pioSym_PIO_MDER[channelIndex].setValue(MDER_Value, 2)

def pinPullUpCal(pin, event):
    global pioSym_PIO_PUER
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        PUER_Value = pioSym_PIO_PUER[channelIndex].getValue()

        if event["value"] == "True":
            PUER_Value |= 1 << bit_pos
        else:
            PUER_Value &= ~(1 << bit_pos)

        pioSym_PIO_PUER[channelIndex].setValue(PUER_Value, 2)

def pinPullDownCal(pin, event):
    global pioSym_PIO_PPDEN
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bit_pos = pinBitPosition[pin_num-1].getValue()
        PPDEN_Value = pioSym_PIO_PPDEN[channelIndex].getValue()

        if event["value"] == "True":
            PPDEN_Value |= 1 << bit_pos
        else:
            PPDEN_Value &= ~(1 << bit_pos)

        pioSym_PIO_PPDEN[channelIndex].setValue(PPDEN_Value, 2)

def pinFilterCal(pin, event):
    global pioSym_PIO_IFER
    global pioSym_PIO_IFSCER
    global pinChannel
    global pinBitPosition
    pin_num = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pin_num-1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)

        bit_pos = pinBitPosition[pin_num-1].getValue()
        IFER_Value = pioSym_PIO_IFER[channelIndex].getValue()
        IFSCER_Value = pioSym_PIO_IFSCER[channelIndex].getValue()

        if (event["value"] == "Debounce Filter"):
            IFSCER_Value |= 1 << bit_pos
            IFER_Value |= 1 << bit_pos
        elif (event["value"] == "Glitch Filter"):
            IFER_Value |= 1 << bit_pos
            IFSCER_Value &= ~(1 << bit_pos)
        else:
            IFSCER_Value &= ~(1 << bit_pos)
            IFER_Value &= ~(1 << bit_pos)

        pioSym_PIO_IFER[channelIndex].setValue(IFER_Value, 2)
        pioSym_PIO_IFSCER[channelIndex].setValue(IFSCER_Value, 2)


def pinSlewRateControlCal(pin, event):
    pinNumber = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pinNumber - 1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bitPosition = pinBitPosition[pinNumber - 1].getValue()
        slewRateValue = pioSym_PIO_SLEWR[channelIndex].getValue()

        if event["value"] == "True":
            slewRateValue |= 1 << bitPosition
        else:
            slewRateValue &= ~(1 << bitPosition)

        pioSym_PIO_SLEWR[channelIndex].setValue(slewRateValue, 0)


def pinDriverCal(pin, event):
    pinNumber = int((pin.getID()).split("_")[1])
    portChannel = pinChannel[pinNumber - 1].getValue()

    if portChannel != "":
        channelIndex = pioSymChannel.index(portChannel)
        bitPosition = pinBitPosition[pinNumber - 1].getValue()
        driverValue = pioSym_PIO_DRIVER[channelIndex].getValue()

        if event["value"] == "High":
            driverValue |= 1 << bitPosition
        else:
            driverValue &= ~(1 << bitPosition)

        pioSym_PIO_DRIVER[channelIndex].setValue(driverValue, 0)

def packageChange(pinoutSymbol, pinout):
    import re
    global uniquePinout
    global package
    global pin_map
    global pin_position
    global pin
    global pinChannel
    global pinBitPosition

    ### No need to process if the device has only one pinout but multiple packages eg: TQFP, LQFP and QFN
    if uniquePinout > 1:

        pin_map = {}
        pin_position = []
        pinoutNode = ATDF.getNode('/avr-tools-device-file/pinouts/pinout@[name= "' + str(package.get(pinout["value"])) + '"]')
        for id in range(0,len(pinoutNode.getChildren())):
            if "BGA" in pinout["value"]:
                pin_map[pinoutNode.getChildren()[id].getAttribute("position")] = pinoutNode.getChildren()[id].getAttribute("pad")
            else:
                pin_map[int(pinoutNode.getChildren()[id].getAttribute("position"))] = pinoutNode.getChildren()[id].getAttribute("pad")

        if "BGA" in pinout["value"]:
            ## BGA package ID's are alphanumeric unlike TQFP special sorting required
            pin_position = sort_alphanumeric(pin_map.keys())
        else:
            pin_position = sorted(pin_map.keys())

        for pinNumber in range(0, len(pinoutNode.getChildren())):
            pin[pinNumber].setLabel("Pin " + str(pin_position[pinNumber]))
            pinBitPosition[pinNumber].setValue(-1, 2)
            pinChannel[pinNumber].setValue("", 2)
            if pin_map.get(pin_position[pinNumber]).startswith("P"):
                pinBitPosition[pinNumber].setValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber]))[0]), 2)
                pinChannel[pinNumber].setValue(pin_map.get(pin_position[pinNumber])[1], 2)

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

###################################################################################################
######################################### PIO Main Menu  ##########################################
###################################################################################################

pioMenu = coreComponent.createMenuSymbol("PIO_MENU", None)
pioMenu.setLabel("Ports (PIO)")
pioMenu.setDescription("Configuration for PIO PLIB")

pioEnable = coreComponent.createBooleanSymbol("PIO_ENABLE", pioMenu)
pioEnable.setLabel("Use PIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)


# Needed to map port system APIs to PLIB APIs
pioSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
pioSymAPI_Prefix.setDefaultValue("PIO")
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
pinSlewRateList =[]
pinDriverList = []

# Build package-pinout map
packageNode = ATDF.getNode("/avr-tools-device-file/variants")
for id in range(0,len(packageNode.getChildren())):
    package[packageNode.getChildren()[id].getAttribute("package")] = packageNode.getChildren()[id].getAttribute("pinout")

pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, package.keys())
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(True)
pioPackage.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

## Find Number of unique pinouts
uniquePinout = len(set(package.values()))

global packagePinCount
packagePinCount = int(re.findall(r'\d+', package.keys()[0])[0])

pinConfiguration = coreComponent.createMenuSymbol("PIO_PIN_CONFIGURATION", pioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuration for PIO Pins")

pinTotalPins = coreComponent.createIntegerSymbol("PIO_PIN_TOTAL" , pinConfiguration)
pinTotalPins.setVisible(False)
pinTotalPins.setDefaultValue(packagePinCount)

# Build pins position-pad map
pinoutNode = ATDF.getNode('/avr-tools-device-file/pinouts/pinout@[name= "' + str(package.get(pioPackage.getValue())) + '"]')
for id in range(0,len(pinoutNode.getChildren())):
    if "BGA" in pioPackage.getValue():
        pin_map[pinoutNode.getChildren()[id].getAttribute("position")] = pinoutNode.getChildren()[id].getAttribute("pad")
    else:
        pin_map[int(pinoutNode.getChildren()[id].getAttribute("position"))] = pinoutNode.getChildren()[id].getAttribute("pad")

if "BGA" in pioPackage.getValue():
    pin_position = sort_alphanumeric(pin_map.keys())
else:
    pin_position = sorted(pin_map.keys())




# Note that all the lists below starts from 0th index and goes till "packagePinCount-1"
# But actual pin numbers on the device starts from 1 (not from 0) and goes till "packagePinCount"
# that is why "pinNumber-1" is used to index the lists wherever applicable.
for pinNumber in range(1, packagePinCount + 1):
    pin.append(pinNumber)
    pin[pinNumber-1]= coreComponent.createMenuSymbol("PIO_PIN_CONFIGURATION" + str(pinNumber - 1), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pin_position[pinNumber-1]))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pin_position[pinNumber-1]))

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    pinPeripheralFunction[pinNumber-1].setReadOnly(True)

    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    pinType[pinNumber-1].setReadOnly(True)
    pinType[pinNumber-1].setDependencies(pinFunctionCal, ["PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION"])

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PIO_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)

    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
    pinChannel[pinNumber-1].setReadOnly(True)

    if pin_map.get(pin_position[pinNumber-1]).startswith("P"):
        pinBitPosition[pinNumber-1].setDefaultValue(int(re.findall('\d+', pin_map.get(pin_position[pinNumber-1]))[0]))
        pinChannel[pinNumber-1].setDefaultValue(pin_map.get(pin_position[pinNumber-1])[1])

        availablePinDictionary[str(pinNumber)] = "P" + str(pinChannel[pinNumber-1].getValue()) + str(pinBitPosition[pinNumber-1].getValue())

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")
    pinDirection[pinNumber-1].setReadOnly(True)
    pinDirection[pinNumber-1].setDependencies(pinDirCal, ["PIN_" + str(pinNumber) + "_DIR" ])

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinLatch[pinNumber-1].setReadOnly(True)
    pinLatch[pinNumber-1].setDefaultValue("")
    pinLatch[pinNumber-1].setDependencies(pinLatchCal, ["PIN_" + str(pinNumber) + "_LAT"])

    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    pinOpenDrain[pinNumber-1].setReadOnly(True)
    pinOpenDrain[pinNumber-1].setDependencies(pinOpenDrainCal, ["PIN_" + str(pinNumber) + "_OD"])

    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PU", pin[pinNumber-1])
    pinPullUp[pinNumber-1].setLabel("Pull Up")
    pinPullUp[pinNumber-1].setReadOnly(True)
    pinPullUp[pinNumber-1].setDependencies(pinPullUpCal, ["PIN_" + str(pinNumber) + "_PU"])

    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PD", pin[pinNumber-1])
    pinPullDown[pinNumber-1].setLabel("Pull Down")
    pinPullDown[pinNumber-1].setReadOnly(True)
    pinPullDown[pinNumber-1].setDependencies(pinPullDownCal, ["PIN_" + str(pinNumber) + "_PD"])

    pinInterrupt.append(pinNumber)
    # This symbol ID name is split and pin number is extracted and used inside "pinInterruptCal" function. so be careful while changing the name of this ID.
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("PIO Interrupt")
    pinInterrupt[pinNumber-1].setReadOnly(True)
    pinInterrupt[pinNumber-1].setDependencies(pinInterruptCal, ["PIN_" + str(pinNumber) + "_PIO_INTERRUPT"])

    pinGlitchFilter.append(pinNumber)
    pinGlitchFilter[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_FILTER", pin[pinNumber-1])
    pinGlitchFilter[pinNumber-1].setLabel("PIO Filter")
    pinGlitchFilter[pinNumber-1].setReadOnly(True)
    pinGlitchFilter[pinNumber-1].setDependencies(pinFilterCal, ["PIN_" + str(pinNumber) + "_PIO_FILTER"])

    if slewRateControlPresent.getValue():
        pinSlewRateList.append(pinNumber)
        pinSlewRateList[pinNumber - 1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_SLEW_RATE", pin[pinNumber - 1])
        pinSlewRateList[pinNumber - 1].setLabel("PIO Slew Rate Control")
        pinSlewRateList[pinNumber - 1].setReadOnly(True)
        pinSlewRateList[pinNumber - 1].setDependencies(pinSlewRateControlCal, ["PIN_" + str(pinNumber) + "_SLEW_RATE"])

    if driverControlPresent.getValue():
        pinDriverList.append(pinNumber)
        pinDriverList[pinNumber - 1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DRIVER", pin[pinNumber - 1])
        pinDriverList[pinNumber - 1].setLabel("PIO Drive")
        pinDriverList[pinNumber - 1].setReadOnly(True)
        pinDriverList[pinNumber - 1].setDependencies(pinDriverCal, ["PIN_" + str(pinNumber) + "_DRIVER"])

    #list created only for dependency
    pinFunctionTypelList.append(pinNumber)
    pinFunctionTypelList[pinNumber-1] = "PIN_" + str(pinNumber) +"_FUNCTION_TYPE"

    #list created only for dependency
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PIO_INTERRUPT"

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

def activateInterrupt(symbol, event):
    global interruptDependncy
    active = False
    for i in range(0, len(interruptDependncy)):
        if Database.getSymbolValue("core", interruptDependncy[i]):
            active = True
            break
    if active != symbol.getValue():
        symbol.setValue(active, 2)

portConfiguration = coreComponent.createMenuSymbol("PIO_CONFIGURATION", pioEnable)
portConfiguration.setLabel("PIO Registers Configuration")

port = []

portInterruptList = []

global portInterrupt
portInterrupt = []
global pioSym_PIO_PDR
pioSym_PIO_PDR = []
global pioSym_PIO_ABCDSR1
pioSym_PIO_ABCDSR1 = []
global pioSym_PIO_ABCDSR2
pioSym_PIO_ABCDSR2 = []
global pioSym_PIO_AIMER
pioSym_PIO_AIMER = []
global pioSym_PIO_LSR
pioSym_PIO_LSR = []
global pioSym_PIO_REHLSR
pioSym_PIO_REHLSR = []
global pioSym_PIO_OER
pioSym_PIO_OER = []
global pioSym_PIO_PUER
pioSym_PIO_PUER = []
global pioSym_PIO_PPDEN
pioSym_PIO_PPDEN = []
global pioSym_PIO_MDER
pioSym_PIO_MDER = []
global pioSym_PIO_SODR
pioSym_PIO_SODR = []
global pioMatrixSym_CCFG_SYSIO
global pioSym_PIO_IFSCER
pioSym_PIO_IFSCER = []
global pioSym_PIO_IFER
pioSym_PIO_IFER = []
pioSym_PIO_SCDR = []
global pioSym_PIO_SLEWR
pioSym_PIO_SLEWR = []
global pioSym_PIO_DRIVER
pioSym_PIO_DRIVER = []

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
global interruptDependncy
node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PIO\"]")
values = node.getChildren()
interruptDependncy = []

for portNumber in range(0, len(values)):

    #Enable Peripheral clock for all the PORT Channels in Clock Manager
    Database.setSymbolValue("core", "PIO" + str(pioSymChannel[portNumber]) + "_CLOCK_ENABLE", True, 1)

    port.append(portNumber)
    port[portNumber]= coreComponent.createMenuSymbol("PIO_CONFIGURATION" + str(portNumber), portConfiguration)
    port[portNumber].setLabel("PIO " + pioSymChannel[portNumber] + " Configuration")

    pioSym_PIO_SCDR.append(portNumber)
    pioSym_PIO_SCDR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_SCDR_VALUE", port[portNumber])
    pioSym_PIO_SCDR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_SCDR")
    pioSym_PIO_SCDR[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_SCDR[portNumber].setMin(0x0)
    pioSym_PIO_SCDR[portNumber].setMax(0x00003FFF)

    portInterrupt.append(portNumber)
    portInterrupt[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_USED", port[portNumber])
    portInterrupt[portNumber].setLabel("Use Interrupt for PIO " + pioSymChannel[portNumber])
    portInterrupt[portNumber].setDefaultValue(False)
    portInterrupt[portNumber].setVisible(True)
    portInterrupt[portNumber].setReadOnly(True)
    interruptDependncy.append("PIO_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_USED")

    #list created only for dependency
    portInterruptList.append(portNumber)
    portInterruptList[portNumber] = "PIO_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_USED"

    pioSym_PIO_PDR.append(portNumber)
    pioSym_PIO_PDR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_PDR_VALUE", port[portNumber])
    pioSym_PIO_PDR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_PDR")
    pioSym_PIO_PDR[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_PDR[portNumber].setReadOnly(True)

    pioSym_PIO_ABCDSR1.append(portNumber)
    pioSym_PIO_ABCDSR1[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_ABCDSR1_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR1[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_ABCDSR1")
    pioSym_PIO_ABCDSR1[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_ABCDSR1[portNumber].setReadOnly(True)

    pioSym_PIO_ABCDSR2.append(portNumber)
    pioSym_PIO_ABCDSR2[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_ABCDSR2_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR2[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_ABCDSR2")
    pioSym_PIO_ABCDSR2[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_ABCDSR2[portNumber].setReadOnly(True)

    pioSym_PIO_OER.append(portNumber)
    pioSym_PIO_OER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_OER_VALUE", port[portNumber])
    pioSym_PIO_OER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_OER")
    pioSym_PIO_OER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_OER[portNumber].setReadOnly(True)

    pioSym_PIO_SODR.append(portNumber)
    pioSym_PIO_SODR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_SODR_VALUE", port[portNumber])
    pioSym_PIO_SODR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_SODR")
    pioSym_PIO_SODR[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_SODR[portNumber].setReadOnly(True)

    pioSym_PIO_AIMER.append(portNumber)
    pioSym_PIO_AIMER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_AIMER_VALUE", port[portNumber])
    pioSym_PIO_AIMER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_AIMER")
    pioSym_PIO_AIMER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_AIMER[portNumber].setReadOnly(True)

    pioSym_PIO_LSR.append(portNumber)
    pioSym_PIO_LSR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_LSR_VALUE", port[portNumber])
    pioSym_PIO_LSR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_LSR")
    pioSym_PIO_LSR[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_LSR[portNumber].setReadOnly(True)

    pioSym_PIO_REHLSR.append(portNumber)
    pioSym_PIO_REHLSR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_REHLSR_VALUE", port[portNumber])
    pioSym_PIO_REHLSR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_REHLSR")
    pioSym_PIO_REHLSR[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_REHLSR[portNumber].setReadOnly(True)

    pioSym_PIO_PUER.append(portNumber)
    pioSym_PIO_PUER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_PUER_VALUE", port[portNumber])
    pioSym_PIO_PUER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_PUER")
    pioSym_PIO_PUER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_PUER[portNumber].setReadOnly(True)

    pioSym_PIO_PPDEN.append(portNumber)
    pioSym_PIO_PPDEN[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_PPDEN_VALUE", port[portNumber])
    pioSym_PIO_PPDEN[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_PPDEN")
    pioSym_PIO_PPDEN[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_PPDEN[portNumber].setReadOnly(True)

    pioSym_PIO_MDER.append(portNumber)
    pioSym_PIO_MDER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_MDER_VALUE", port[portNumber])
    pioSym_PIO_MDER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_MDER")
    pioSym_PIO_MDER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_MDER[portNumber].setReadOnly(True)

    pioSym_PIO_IFER.append(portNumber)
    pioSym_PIO_IFER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_IFER_VALUE", port[portNumber])
    pioSym_PIO_IFER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_IFER")
    pioSym_PIO_IFER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_IFER[portNumber].setReadOnly(True)

    pioSym_PIO_IFSCER.append(portNumber)
    pioSym_PIO_IFSCER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_IFSCER_VALUE", port[portNumber])
    pioSym_PIO_IFSCER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_IFSCER")
    pioSym_PIO_IFSCER[portNumber].setDefaultValue(0x00000000)
    pioSym_PIO_IFSCER[portNumber].setReadOnly(True)

    if slewRateControlPresent.getValue():
        pioSym_PIO_SLEWR.append(portNumber)
        pioSym_PIO_SLEWR[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_SLEWR_VALUE", port[portNumber])
        pioSym_PIO_SLEWR[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_SLEWR")
        pioSym_PIO_SLEWR[portNumber].setDefaultValue(0x00000000)
        pioSym_PIO_SLEWR[portNumber].setReadOnly(True)

    if driverControlPresent.getValue():
        pioSym_PIO_DRIVER.append(portNumber)
        pioSym_PIO_DRIVER[portNumber] = coreComponent.createHexSymbol("PIO" + str(pioSymChannel[portNumber]) + "_DRIVER_VALUE", port[portNumber])
        pioSym_PIO_DRIVER[portNumber].setLabel("PIO" + str(pioSymChannel[portNumber]) + "_DRIVER")
        pioSym_PIO_DRIVER[portNumber].setDefaultValue(0x00000000)
        pioSym_PIO_DRIVER[portNumber].setReadOnly(True)

    #symbols and variables for interrupt handling
    pioSymInterruptVector.append(portNumber)
    pioSymInterruptVector[portNumber] = "PIO" + str(pioSymChannel[portNumber]) + "_INTERRUPT_ENABLE"
    pioSymInterruptHandler.append(portNumber)
    pioSymInterruptHandler[portNumber] = "PIO" + str(pioSymChannel[portNumber]) + "_INTERRUPT_HANDLER"
    pioSymInterruptHandlerLock.append(portNumber)
    pioSymInterruptHandlerLock[portNumber] = "PIO" + str(pioSymChannel[portNumber]) + "_INTERRUPT_HANDLER_LOCK"
    pioSymInterruptVectorUpdate.append(portNumber)
    pioSymInterruptVectorUpdate[portNumber] = "PIO" + str(pioSymChannel[portNumber]) + "_INTERRUPT_ENABLE_UPDATE"

    # Dependency Status for interrupt
    pioSymIntEnComment.append(portNumber)
    pioSymIntEnComment[portNumber] = coreComponent.createCommentSymbol("PIO_" + str(pioSymChannel[portNumber]) + "_NVIC_ENABLE_COMMENT", pioMenu)
    pioSymIntEnComment[portNumber].setVisible(False)
    pioSymIntEnComment[portNumber].setLabel("Warning!!! PIO" + str(pioSymChannel[portNumber]) + " Interrupt is Disabled in Interrupt Manager")
    pioSymIntEnComment[portNumber].setDependencies(InterruptStatusWarning, ["core." + pioSymInterruptVectorUpdate[portNumber], "PIO_" + str(pioSymChannel[portNumber]) + "_INTERRUPT_USED"])

    # Dependency Status for clock
    pioSymClkEnComment.append(portNumber)
    pioSymClkEnComment[portNumber] = coreComponent.createCommentSymbol("PIO_" + str(pioSymChannel[portNumber]) + "_CLK_ENABLE_COMMENT", pioMenu)
    pioSymClkEnComment[portNumber].setVisible(False)
    pioSymClkEnComment[portNumber].setLabel("Warning!!! PIO" + str(pioSymChannel[portNumber]) + " Peripheral Clock is Disabled in Clock Manager")
    pioSymClkEnComment[portNumber].setDependencies(ClockStatusWarning, ["core.PIO" + str(pioSymChannel[portNumber]) + "_CLOCK_ENABLE"])
 
interruptActive = coreComponent.createBooleanSymbol("INTERRUPT_ACTIVE", portConfiguration)
interruptActive.setDefaultValue(False)
interruptActive.setVisible(False)
interruptActive.setDependencies(activateInterrupt, interruptDependncy)
# Interrupt Dynamic settings
pioSymInterruptControl = coreComponent.createBooleanSymbol("NVIC_PIO_ENABLE", None)
pioSymInterruptControl.setDependencies(pioInterruptControl, portInterruptList)
pioSymInterruptControl.setVisible(False)

pioMatrixSym_CCFG_SYSIO = coreComponent.createHexSymbol("PIO_CCFG_SYSIO_VALUE", portConfiguration)
pioMatrixSym_CCFG_SYSIO.setLabel("CCFG_SYSIO")
pioMatrixSym_CCFG_SYSIO.setDescription("System Pins as GPIO")
pioMatrixSym_CCFG_SYSIO.setDefaultValue(0x00000000)
pioMatrixSym_CCFG_SYSIO.setVisible(False)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pioHeaderFile = coreComponent.createFileSymbol("PIO_HEADER", None)
pioHeaderFile.setSourcePath("../peripheral/pio_11004/templates/plib_pio.h.ftl")
pioHeaderFile.setOutputName("plib_pio.h")
pioHeaderFile.setDestPath("/peripheral/pio/")
pioHeaderFile.setProjectPath("config/" + configName +"/peripheral/pio/")
pioHeaderFile.setType("HEADER")
pioHeaderFile.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol("PIO_SOURCE", None)
pioSource1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.c.ftl")
pioSource1File.setOutputName("plib_pio.c")
pioSource1File.setDestPath("/peripheral/pio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)

pioSystemInitFile = coreComponent.createFileSymbol("PIO_INIT", None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
pioSystemInitFile.setSourcePath("../peripheral/pio_11004/templates/system/initialization.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol("PIO_DEF", None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/pio_11004/templates/system/definitions.h.ftl")
pioSystemDefFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PIO_BSP_H", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/pio_11004/templates/plib_pio_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("PIO_BSP_C", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspIncludeFile.setSourcePath("../peripheral/pio_11004/templates/plib_pio_bsp.c.ftl")
bspIncludeFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("PIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/pio_11004/templates/plib_pio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)
