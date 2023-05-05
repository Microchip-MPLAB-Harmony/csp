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

peripheralFunctionality = ["GPIO", "Alternate", "LED_AH", "LED_AL", "SWITCH_AH", "SWITCH_AL", "VBUS_AH", "VBUS_AL", "R", "S"] # R is for RTC and S is for SUPC

global gpioPeripheralFunc
gpioPeripheralFunc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]

global availablePinDictionary
availablePinDictionary = {}

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

global getAvailablePins
global setPinInterruptData

gpioRegName = coreComponent.createStringSymbol("GPIO_REG_NAME", None)
gpioRegName.setVisible(False)
gpioRegName.setValue("GPIO")

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
            gpioBitPositionNode = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(package.get(pinout["value"])) + "\"]")
            for id in range(0,len(gpioBitPositionNode.getChildren())):
                if "BGA" in pinout["value"] or "WLCSP" in pinout["value"] or "DRQFN" in pinout["value"]:
                    pin_map[gpioBitPositionNode.getChildren()[id].getAttribute("position")] = gpioBitPositionNode.getChildren()[id].getAttribute("pad")
                else:
                    pin_map[int(gpioBitPositionNode.getChildren()[id].getAttribute("position"))] = gpioBitPositionNode.getChildren()[id].getAttribute("pad")

            if "BGA" in pinout["value"] or "WLCSP" in pinout["value"] or "DRQFN" in pinout["value"]:
                ## BGA package ID's are alphanumeric unlike TQFP special sorting required
                pin_position = sort_alphanumeric(pin_map.keys())
            else:
                pin_position = sorted(pin_map.keys())

        prev_package = cur_package

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def setPinInterruptData(pin_interrupt_name, status):

    Database.setSymbolValue("core", pin_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", pin_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", pin_interrupt_name + "_INTERRUPT_HANDLER", pin_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", pin_interrupt_name + "_INTERRUPT_HANDLER", pin_interrupt_name + "_Handler", 1)

def setupGpioPINCFG2(symbol, event):
    cfgValue = 0
    component = event["source"]
    pin_num = str(event["id"].split("_")[1])
    driveStrn = component.getSymbolValue( "PIN_" + pin_num + "_DRVSTR")
    slewRate = component.getSymbolValue( "PIN_" + pin_num + "_SLEW_RATE")

    if driveStrn == "Level1":
        cfgValue |= (1 << 4)
    if driveStrn == "Level2":
        cfgValue |= (2 << 4)
    if driveStrn == "Level3":
        cfgValue |= (3 << 4)
    if slewRate == "Fast":
        cfgValue |= 1

    symbol.setValue(cfgValue)

def setupGpioPINCFG(symbol, event):
    global setPinInterruptData
    component = event["source"]
    pin_num = str(event["id"].split("_")[1])

    peripheralFunc = component.getSymbolValue( "PIN_" + pin_num +"_PERIPHERAL_FUNCTION")
    pullUpDownEnable = component.getSymbolValue( "PIN_" + pin_num + "_PUPD")
    direction = component.getSymbolValue( "PIN_" + pin_num + "_DIR")
    intDetect = component.getSymbolValue( "PIN_" + pin_num + "_INTDET")
    latchValue = component.getSymbolValue( "PIN_" + pin_num + "_LAT")
    polarity = component.getSymbolValue( "PIN_" + pin_num + "_POLARITY")
    inputDisable = component.getSymbolValue( "PIN_" + pin_num + "_INDIS")
    outBufType = component.getSymbolValue( "PIN_" + pin_num + "_OUTBUFTYPE")
    girqNum = component.getSymbolValue( "PIN_" + pin_num + "_GIRQNUM")
    girqBitPos = component.getSymbolValue( "PIN_" + pin_num + "_GIRQBITPOS")


    pin_pad = pin_map.get(pin_position[int(pin_num)-1])

    cfgValue = 0x00008040       # Power on default value

    nvic_int_info = {}
    nvic_int_info = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": pin_pad})
    component.setSymbolValue( "PIN_" + pin_num + "_GIRQNUM", 8 + nvic_int_info["girqn_reg_num"])
    component.setSymbolValue("PIN_" + pin_num + "_GIRQBITPOS", nvic_int_info["girqn_bitpos"])

    if intDetect != "":
        setPinInterruptData(pin_pad +"_GRP", True)
    else:
        setPinInterruptData(pin_pad +"_GRP", False)

    if pullUpDownEnable == "Pull Up":
        cfgValue = (cfgValue & ~ (1 << 15)) | (0x01)
    if pullUpDownEnable == "Pull Down":
        cfgValue = (cfgValue & ~ (1 << 15)) | (0x02)
    if pullUpDownEnable == "Repeater":
        cfgValue = (cfgValue & ~ (1 << 15)) | (0x03)
    if direction == "Out":
        cfgValue = (cfgValue & ~ (1 << 15)) | (0x01 << 9)
    if intDetect == "High Level":
        cfgValue = (cfgValue & ~((1 << 15) | (0x07 << 4))) | (0x01 << 4)
    if intDetect == "Low Level":
        cfgValue = (cfgValue & ~((1 << 15) |(0x07 << 4)))
    if intDetect == "Rising Edge":
        cfgValue = (cfgValue & ~((1 << 15) | (0x07 << 4))) | (0x0D << 4)
    if intDetect == "Falling Edge":
        cfgValue = (cfgValue & ~((1 << 15) | (0x07 << 4))) | (0x0E << 4)
    if intDetect == "Either Edge":
        cfgValue = (cfgValue & ~((1 << 15) | (0x07 << 4))) | (0x0F << 4)
    if latchValue == "High":
        cfgValue = (cfgValue & ~(1 << 15)) | (1 << 16)
    if polarity == "Inverted":
        cfgValue = (cfgValue & ~(1 << 15)) | (1 << 11)
    if outBufType == "Open Drain":
        cfgValue = (cfgValue & ~ (1 << 15)) | (1 << 8)
    # Must enable the input if GPIO function is selcted
    if peripheralFunc == "GPIO":
        cfgValue = (cfgValue & ~ (1 << 15))
    if peripheralFunc not in peripheralFunctionality and peripheralFunc != "":
        cfgValue = (cfgValue & ~(1 << 15)) | (gpioPeripheralFunc.index(peripheralFunc) << 12)
    # The inputDisable check must be the last
    if inputDisable == "True":
        cfgValue |= (1 << 15)

    symbol.setValue(cfgValue)

###################################################################################################
######################################### GPIO Main Menu  #########################################
###################################################################################################

##packagepinout map
global package
global gpioPackage
package = {}
## total number of pins
global pincount
pincount = 0
## Number of unique pinouts
global uniquePinout
uniquePinout = 1
gpioMenu = coreComponent.createMenuSymbol("GPIO_MENU", None)
gpioMenu.setLabel("GPIO")
gpioMenu.setDescription("Configuraiton for GPIO PLIB")

# Needed to map gpio system APIs to PLIB APIs
gpioSymAPI_Prefix = coreComponent.createStringSymbol("GPIO_API_PREFIX", None)
gpioSymAPI_Prefix.setDefaultValue("GPIO")
gpioSymAPI_Prefix.setVisible(False)

gpioEnable = coreComponent.createBooleanSymbol("GPIO_ENABLE", gpioMenu)
gpioEnable.setLabel("Use GPIO PLIB ?")
gpioEnable.setDefaultValue(True)
gpioEnable.setReadOnly(True)

# Build package pinout map
packageNode = ATDF.getNode("/avr-tools-device-file/variants")
for id in range(0,len(packageNode.getChildren())):
    package[packageNode.getChildren()[id].getAttribute("package")] = packageNode.getChildren()[id].getAttribute("pinout")

## Find Number of unique pinouts
uniquePinout = len(set(package.values()))

gpioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", gpioEnable, package.keys())
gpioPackage.setLabel("Pin Package")
gpioPackage.setReadOnly(True)

## get the pin count
pincount = int(re.findall(r'\d+', package.keys()[0])[0])

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################

pinConfiguration = coreComponent.createMenuSymbol("GPIO_PIN_CONFIGURATION", gpioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuraiton for GPIO Pins")

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

pinoutNode = ATDF.getNode('/avr-tools-device-file/pinouts/pinout@[name= "' + str(package.get(gpioPackage.getValue())) + '"]')
for id in range(0,len(pinoutNode.getChildren())):
    if pinoutNode.getChildren()[id].getAttribute("type") == None:
        if "BGA" in gpioPackage.getValue() or "WLCSP" in gpioPackage.getValue() or "DRQFN" in gpioPackage.getValue():
            pin_map[pinoutNode.getChildren()[id].getAttribute("position")] = pinoutNode.getChildren()[id].getAttribute("pad")
        else:
            pin_map[int(pinoutNode.getChildren()[id].getAttribute("position"))] = pinoutNode.getChildren()[id].getAttribute("pad")
    else:
        pin_map_internal[pinoutNode.getChildren()[id].getAttribute("type").split("INTERNAL_")[1]] = pinoutNode.getChildren()[id].getAttribute("pad")

if "BGA" in gpioPackage.getValue() or "WLCSP" in gpioPackage.getValue() or "DRQFN" in gpioPackage.getValue():
    pin_position = sort_alphanumeric(pin_map.keys())
    pin_position_internal = sort_alphanumeric(pin_map_internal.keys())
else:
    pin_position = sorted(pin_map.keys())
    pin_position_internal = sorted(pin_map_internal.keys())

internalPincount = pincount + len(pin_map_internal.keys())

gpioSym_PinMaxIndex = coreComponent.createIntegerSymbol("GPIO_PIN_MAX_INDEX", None)
gpioSym_PinMaxIndex.setVisible(False)
gpioSym_PinMaxIndex.setDefaultValue(internalPincount)

for pinNumber in range(1, internalPincount + 1):

    if pinNumber < pincount + 1:
        pinPad = str(pin_map.get(pin_position[pinNumber-1]))
    else:
        pinPad = str(pin_map_internal.get(pin_position_internal[pinNumber - pincount - 1]))

    if pinNumber < pincount + 1:
        pin = coreComponent.createMenuSymbol("GPIO_PIN" + str(pinNumber), pinConfiguration)
        pin.setLabel("Pin " + str(pin_position[pinNumber-1]))
        pin.setDescription("Configuraiton for Pin " + str(pin_position[pinNumber-1]) )
    else:
        pin = coreComponent.createMenuSymbol("GPIO_PIN" + str(pinNumber), pinConfiguration)
        pin.setLabel("Pin " +  str(pin_position_internal[pinNumber - pincount - 1]))
        pin.setDescription("Configuraiton for Pin " + str(pin_position_internal[pinNumber - pincount - 1]))

    reg_num = 0
    reg_index = 0
    if pinPad.startswith("GPIO"):
        num = int(pinPad[len("GPIO"):], 8)
        reg_num = int(str(oct(int(num/8))))
        reg_index = num%8

    pinCtrlRegNum = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GPIO_CTRL_REG_NUM", pin)
    pinCtrlRegNum.setReadOnly(False)
    pinCtrlRegNum.setDefaultValue(reg_num)
    pinCtrlRegNum.setVisible(False)

    pinCtrlRegIndex = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GPIO_CTRL_REG_INDEX", pin)
    pinCtrlRegIndex.setReadOnly(False)
    pinCtrlRegIndex.setDefaultValue(reg_index)
    pinCtrlRegIndex.setVisible(False)

    pinName = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin)
    pinName.setLabel("Name")
    pinName.setDefaultValue("")
    pinName.setReadOnly(True)

    pinType = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin)
    pinType.setLabel("Type")
    pinType.setReadOnly(True)

    gpioSym_PinPad = coreComponent.createStringSymbol("GPIO_PIN_NAME_" + str(pinNumber), pin)
    gpioSym_PinPad.setVisible(False)
    gpioSym_PinPad.setDefaultValue(pinPad)

    pinPeripheralFunction = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin)
    pinPeripheralFunction.setLabel("Peripheral Selection")
    pinPeripheralFunction.setReadOnly(True)

    pinDirection = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin)
    pinDirection.setLabel("Direction")
    pinDirection.setReadOnly(True)

    pinLatch = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin)
    pinLatch.setLabel("Initial Latch Value")
    pinLatch.setReadOnly(True)

    pin_PU_PD_Enable = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PUPD", pin)
    pin_PU_PD_Enable.setLabel("Pull Up / Pull Down Enable")
    pin_PU_PD_Enable.setReadOnly(True)

    pinInterruptDetection = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_INTDET", pin)
    pinInterruptDetection.setLabel("Interrupt Detection")
    pinInterruptDetection.setReadOnly(True)

    pinGIRQNum = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GIRQNUM", pin)
    pinGIRQNum.setLabel("GIRQ Number")
    pinGIRQNum.setReadOnly(False)
    pinGIRQNum.setDefaultValue(0)
    pinGIRQNum.setVisible(False)

    pinGIRQBitPos = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_GIRQBITPOS", pin)
    pinGIRQBitPos.setLabel("GIRQ Bit Position")
    pinGIRQBitPos.setReadOnly(False)
    pinGIRQBitPos.setDefaultValue(0)
    pinGIRQBitPos.setVisible(False)

    pinPolarity = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_POLARITY", pin)
    pinPolarity.setLabel("Polarity")
    pinPolarity.setReadOnly(True)

    pinInputDisable = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_INDIS", pin)
    pinInputDisable.setLabel("Input Disable")
    pinInputDisable.setVisible(False)
    pinInputDisable.setReadOnly(True)

    pinOutputBufferType = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_OUTBUFTYPE", pin)
    pinOutputBufferType.setLabel("Output Buffer Type")
    pinOutputBufferType.setReadOnly(True)

    pinDriveStrength = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DRVSTR", pin)
    pinDriveStrength.setLabel("Drive Strength")
    pinDriveStrength.setReadOnly(True)

    pinSlewRate = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_SLEW_RATE", pin)
    pinSlewRate.setLabel("Slew Rate")
    pinSlewRate.setReadOnly(True)

    gpioSym_PIN_PINCFG = coreComponent.createHexSymbol("PIN_" + str(pinNumber) + "_CFG", pin)
    gpioSym_PIN_PINCFG.setReadOnly(True)
    gpioSym_PIN_PINCFG.setVisible(False)
    gpioSym_PIN_PINCFG.setDefaultValue(0x00008040)
    gpioSym_PIN_PINCFG.setDependencies(setupGpioPINCFG, ["PIN_" + str(pinNumber) +"_PERIPHERAL_FUNCTION", "PIN_" + str(pinNumber) +"_DIR", "PIN_" + str(pinNumber) +"_LAT", "PIN_" + str(pinNumber) +"_PUPD", "PIN_" + str(pinNumber) + "_INTDET", "PIN_" + str(pinNumber) + "_POLARITY", "PIN_" + str(pinNumber) + "_INDIS", "PIN_" + str(pinNumber) + "_OUTBUFTYPE"])

    gpioSym_PIN_PINCFG2 = coreComponent.createHexSymbol("PIN_" + str(pinNumber) + "_CFG2", pin)
    gpioSym_PIN_PINCFG2.setReadOnly(True)
    gpioSym_PIN_PINCFG2.setVisible(False)
    gpioSym_PIN_PINCFG2.setDefaultValue(0x00)
    gpioSym_PIN_PINCFG2.setDependencies(setupGpioPINCFG2, ["PIN_" + str(pinNumber) +"_DRVSTR", "PIN_" + str(pinNumber) + "_SLEW_RATE"])

gpioSym_PinMaxGPIOPins = coreComponent.createIntegerSymbol("GPIO_PIN_MAX_GPIO_PINS", None)
gpioSym_PinMaxGPIOPins.setVisible(False)
signalIndex = 0

# Code to generate the GPIO_PIN enum in header file
gpioSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"GPIO\"]/instance@[name=\"GPIO\"]/signals").getChildren()

for id in range(0,len(gpioSignalNode)):
    signalPad = gpioSignalNode[id].getAttribute("pad")
    reg_num = 0
    reg_index = 0
    if signalPad.startswith("GPIO"):
        num = int(signalPad[len("GPIO"):], 8)

        gpioSym_PinPad = coreComponent.createStringSymbol("GPIO_PIN_PAD_" + str(signalIndex), None)
        gpioSym_PinPad.setVisible(False)
        gpioSym_PinPad.setDefaultValue(signalPad)

        gpioSym_PinIndex = coreComponent.createIntegerSymbol("GPIO_PIN_INDEX_" + str(signalIndex), None)
        gpioSym_PinIndex.setVisible(False)
        gpioSym_PinIndex.setDefaultValue(num)

        signalIndex = signalIndex + 1

gpioSym_PinMaxGPIOPins.setDefaultValue(signalIndex)

# Code to generate GPIO_GROUP enum in header file
gpioTotalGroupsCnt = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPIO\"]/register-group@[name=\"GPIO\"]/register@[name=\"PARIN\"]").getAttribute("count")
gpioNumGroups = coreComponent.createIntegerSymbol("GPIO_NUM_GROUPS", None)
gpioNumGroups.setVisible(False)
gpioNumGroups.setDefaultValue(int(gpioTotalGroupsCnt))

# Code to generate PIN_FUNCTION enum in header file
gpioMuxFuncEnum_List = coreComponent.createListSymbol("GPIO_MUX_FUNC_ENUM_LIST", None)
gpioMuxFuncEnum_List.setVisible(False)

gpioMuxFuncEnums = coreComponent.createListEntrySymbol("GPIO_MUX_FUNC_ENUM", None)
gpioMuxFuncEnums.setTarget("core.GPIO_MUX_FUNC_ENUM_LIST")
gpioMuxFuncEnums.setVisible(False)

enum_value = ""
gpioMUXFunctions_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPIO\"]/value-group@[name=\"GPIO_CTRL__MUX_CTRL\"]").getChildren()
for id in range(len(gpioMUXFunctions_values)):
    key = gpioMUXFunctions_values[id].getAttribute("name")
    enum_value += "GPIO_FUNCTION_" + key +" = " + "GPIO_CTRL0_MUX_CTRL_" + key + "," + "\n\r\t"

gpioMuxFuncEnums.addValue(enum_value)


# Code to generate PIN_FUNCTION enum in header file
gpioPUPDEnum_List = coreComponent.createListSymbol("GPIO_PU_PD_ENUM_LIST", None)
gpioPUPDEnum_List.setVisible(False)

gpioPUPDEnums = coreComponent.createListEntrySymbol("GPIO_PU_PD_ENUM", None)
gpioPUPDEnums.setTarget("core.GPIO_PU_PD_ENUM_LIST")
gpioPUPDEnums.setVisible(False)

enum_value = ""
gpioPUPDValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPIO\"]/value-group@[name=\"GPIO_CTRL__PU_PD\"]").getChildren()
for id in range(len(gpioPUPDValues)):
    key = gpioPUPDValues[id].getAttribute("name")
    value = gpioPUPDValues[id].getAttribute("value")
    description = gpioPUPDValues[id].getAttribute("caption")
    enum_value += "GPIO_PULL_TYPE_" + key +" = " + value + "U " + "," + "\n\r\t"

gpioPUPDEnums.addValue(enum_value)

packageUpdate = coreComponent.createBooleanSymbol("PACKAGE_UPDATE_DUMMY", None)
packageUpdate.setVisible(False)
packageUpdate.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

# Needed to map port system APIs to PLIB APIs
gpioSymAPI_Prefix = coreComponent.createStringSymbol("PORT_API_PREFIX", None)
gpioSymAPI_Prefix.setDefaultValue("GPIO")
gpioSymAPI_Prefix.setVisible(False)
###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# portModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]")
# portModuleID = portModuleNode.getAttribute("id")

gpioSym_HeaderFile = coreComponent.createFileSymbol("GPIO_HEADER", None)
gpioSym_HeaderFile.setSourcePath("../peripheral/gpio_26/templates/plib_gpio.h.ftl")
gpioSym_HeaderFile.setOutputName("plib_gpio.h")
gpioSym_HeaderFile.setDestPath("/peripheral/gpio/")
gpioSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/gpio/")
gpioSym_HeaderFile.setType("HEADER")
gpioSym_HeaderFile.setMarkup(True)

gpioSym_SourceFile = coreComponent.createFileSymbol("GPIO_SOURCE", None)
gpioSym_SourceFile.setSourcePath("../peripheral/gpio_26/templates/plib_gpio.c.ftl")
gpioSym_SourceFile.setOutputName("plib_gpio.c")
gpioSym_SourceFile.setDestPath("/peripheral/gpio/")
gpioSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/gpio/")
gpioSym_SourceFile.setType("SOURCE")
gpioSym_SourceFile.setMarkup(True)

bspIncludeFile = coreComponent.createFileSymbol("GPIO_BSP_HEADER", None)
bspIncludeFile.setType("STRING")
bspIncludeFile.setOutputName("core.LIST_BSP_MACRO_INCLUDES")
bspIncludeFile.setSourcePath("../peripheral/gpio_26/templates/plib_gpio_bsp.h.ftl")
bspIncludeFile.setMarkup(True)

bspSourceFile = coreComponent.createFileSymbol("GPIO_BSP_SOURCE", None)
bspSourceFile.setType("STRING")
bspSourceFile.setOutputName("core.LIST_BSP_INITIALIZATION")
bspSourceFile.setSourcePath("../peripheral/gpio_26/templates/plib_gpio_bsp.c.ftl")
bspSourceFile.setMarkup(True)

sysPortIncludeFile = coreComponent.createFileSymbol("GPIO_SYSPORT_H", None)
sysPortIncludeFile.setType("STRING")
sysPortIncludeFile.setOutputName("core.LIST_SYS_PORT_INCLUDES")
sysPortIncludeFile.setSourcePath("../peripheral/gpio_26/templates/plib_gpio_sysport.h.ftl")
sysPortIncludeFile.setMarkup(True)

gpioSym_SystemInitFile = coreComponent.createFileSymbol("GPIO_SYS_INIT", None)
gpioSym_SystemInitFile.setSourcePath("../peripheral/gpio_26/templates/system/initialization.c.ftl")
gpioSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
gpioSym_SystemInitFile.setType("STRING")
gpioSym_SystemInitFile.setMarkup(True)

gpioSym_SystemDefFile = coreComponent.createFileSymbol("GPIO_SYS_DEF", None)
gpioSym_SystemDefFile.setSourcePath("../peripheral/gpio_26/templates/system/definitions.h.ftl")
gpioSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
gpioSym_SystemDefFile.setType("STRING")
gpioSym_SystemDefFile.setMarkup(True)

