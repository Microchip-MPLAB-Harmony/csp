print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))
import re


###############################################Global Variables #############################################
global pinChannel
pinChannel = []
global per_func
per_func = ["A", "B", "C", "D", "E", "F", "G"]
global pinInterrupt
pinInterrupt = []

global port_mskr
port_mskr = {		"A_A" : 0,
					"A_B" : 0,
					"A_C" : 0,
					"A_D" : 0,
					"A_E" : 0,
					"A_F" : 0,
					"A_G" : 0,
					"B_A" : 0,
					"B_B" : 0,
					"B_C" : 0,
					"B_D" : 0,
					"B_E" : 0,
					"B_F" : 0,
					"B_G" : 0,
					"C_A" : 0,
					"C_B" : 0,
					"C_C" : 0,
					"C_D" : 0,
					"C_E" : 0,
					"C_F" : 0,
					"C_G" : 0,
					"D_A" : 0,
					"D_B" : 0,
					"D_C" : 0,
					"D_D" : 0,
					"D_E" : 0,
					"D_F" : 0,
					"D_G" : 0,
					"E_A" : 0,
					"E_B" : 0,
					"E_C" : 0,
					"E_D" : 0,
					"E_E" : 0,
					"E_F" : 0,
					"E_G" : 0
					}
global interruptValues
interruptValues = {	"Falling Edge" : 0,
					"Raising Edge" : 1,
					"Both Edge"	   : 2,
					"Low Level"	   : 3,
					"High Level"   : 4
}
global latchValues
latchValues = {	    "A" : 0,
					"B" : 0,
					"C"	: 0,
					"D"	: 0,
					"E" : 0
}
global port_interrupt
port_interrupt = {	    "A" : 0,
					"B" : 0,
					"C"	: 0,
					"D"	: 0,
					"E" : 0
}
global sort_alphanumeric
global prev_package
global cur_package
prev_package = ""
cur_package = ""
global pioSymChannel
pioSymChannel = ["A", "B", "C", "D", "E"]
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


###########################################Local Variables################################################################

############################################Callbacks##############################################

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


def portFunc(pin, func):
    global port_mskr
    global per_func
    pin_num = int(str(pin.getID()).split("PIN_")[1].split("_PIO_PIN")[0])
    port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")
    bit_pos = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_PIN")
    if port:
        key = port + "_" + func["value"]
        if func["value"] in per_func:
            for id in per_func:
                if id == func["value"]:
                    port_mskr[key] |= (1 << bit_pos)
                else:
                    port_mskr[port + "_" + id] &= ~(1 << bit_pos)
        else:
                        for id in per_func:
                            port_mskr[port + "_" + id] &= ~(1 << bit_pos)
                            print port_mskr[port + "_" + id]

        for id in per_func:
            Database.setSymbolValue("core", "PORT_" + str(port) + "_MSKR_Value" + str(id), str(hex(port_mskr[port + "_" + id])), 2)


def pinCFGR (pin, cfgr_reg):
	cfgr = 0
	global port_mskr
	global per_func
	global interruptValues
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
	filter = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_FILTER")
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
			cfgr |= 1 << 16
		if filter:
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
	global port_interrupt
	pin_num = int(str(pin.getID()).split("PIN_")[1].split("_PIO_INTERRUPT")[0])
	port = Database.getSymbolValue("core", "PIN_" + str(pin_num) + "_PIO_CHANNEL")
	if port in port_interrupt:
		if interrupt["value"]:
			port_interrupt[port] += 1
		else:
			port_interrupt[port] -= 1

		Database.setSymbolValue("core", "PORT_" + str(port) + "_NUM_INT_PINS", int(port_interrupt[port]), 2)

		if port_interrupt[port] > 0:
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

pioEnable = coreComponent.createBooleanSymbol("PIO_ENABLE", pioMenu)
pioEnable.setLabel("Use PIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)

Database.setSymbolValue("core", "PIOA_CLOCK_ENABLE", True, 1)

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

	pinFilter = coreComponent.createBooleanSymbol("PIN_" + str(pinNumber) + "_PIO_FILTER", pin[pinNumber-1])
	pinFilter.setLabel("Glitch Filter Enable")

	pinFilterClock = coreComponent.createKeyValueSetSymbol("PIN_" + str(pinNumber) + "_IFSCEN", pin[pinNumber-1])
	pinFilterClock.setLabel("Glitch filter Clock Source ")
	pinFilterClock.addKey("MCK", str(0) , "The glitch filter is able to filter glitches with a duration < tmck/2" )
	pinFilterClock.addKey("SLCK", str(1) , "The debouncing filter is able to filter pulses with a duration < tdiv_slck/2" )

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
	pincfgrValue[pinNumber-1].setDependencies(pinCFGR, ["PIN_" + str(pinNumber) + "_PD", "PIN_" + str(pinNumber) + "_PU", "PIN_" + str(pinNumber) + "_OD", "PIN_" + str(pinNumber) + "_DIR", "PIN_" + str(pinNumber) + "_PIO_INTERRUPT", "PIN_" + str(pinNumber) + "_IFSCEN", "PIN_" + str(pinNumber) + "_PIO_FILTER", "PIN_" + str(pinNumber) + "_DRV", "PIN_" + str(pinNumber) + "_TAMPER", "PIN_" + str(pinNumber) + "_ST" ])



packageUpdate = coreComponent.createBooleanSymbol("PACKAGE_UPDATE_DUMMY", None)
packageUpdate.setVisible(False)
packageUpdate.setDependencies(packageChange, ["COMPONENT_PACKAGE"])

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
	portIntEnable = coreComponent.createBooleanSymbol("PORT_" + str(port) + "_INTERRUPT_USED", None)
	portIntEnable.setReadOnly(True)
	portIntEnable.setVisible(False)
	portIntEnable.setDefaultValue(False)

	portINT = coreComponent.createIntegerSymbol("PORT_" + str(port) + "_NUM_INT_PINS", None)
	portINT.setReadOnly(True)
	portINT.setVisible(False)
	portINT.setDefaultValue(0)

	for per in per_func:
		portperMSKR = coreComponent.createStringSymbol("PORT_" + str(port) + "_MSKR_Value" + str(per), None)
		portperMSKR.setReadOnly(True)
		portperMSKR.setVisible(False)
		portperMSKR.setDefaultValue(str(hex(0)))

count = 1
for func in per_func:
	portperMSKR = coreComponent.createStringSymbol("FUNC_" + str(func) + "_CFGR_Value", None)
	portperMSKR.setReadOnly(True)
	portperMSKR.setVisible(False)
	portperMSKR.setDefaultValue(str(hex(count)))
	count += 1

portConfiguration = coreComponent.createMenuSymbol("PIO_CONFIGURATION", pioEnable)
portConfiguration.setLabel("PIO Registers Configuration")
for port in pioSymChannel:
	pioSCLKDIV = coreComponent.createIntegerSymbol("PORT_" + str(port) + "_SCLK_DIV", portConfiguration)
	pioSCLKDIV.setLabel("PORT" + str(port) + " Slow Clock Divider")
	pioSCLKDIV.setMax(8192)
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

pioMappingHeaderFile = coreComponent.createFileSymbol("PIO_MAPPING_HEADER", None)
pioMappingHeaderFile.setSourcePath("../peripheral/pio_11264/plib_pio_pin.h")
pioMappingHeaderFile.setOutputName("plib_pio_pin.h")
pioMappingHeaderFile.setDestPath("/peripheral/pio/")
pioMappingHeaderFile.setProjectPath("config/" + configName +"/peripheral/pio/")
pioMappingHeaderFile.setType("HEADER")
pioMappingHeaderFile.setMarkup(False)

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
pioSystemInitFile.setSourcePath("../peripheral/pio_11264/templates/system/system_initialize.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol("PIO_DEF", None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/pio_11264/templates/system/system_definitions.h.ftl")
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
