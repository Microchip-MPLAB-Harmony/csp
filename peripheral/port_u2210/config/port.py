Log.writeInfoMessage("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

# Function to enable PORT Group when any of the pins is using the particular group.
def setupPort(usePortLocal, event):
    global usePort

    x = portGroup.index(event["value"])

    usePort[x].setValue(True, 1)

###################################################################################################
######################################### PORT Main Menu  ##########################################
###################################################################################################

portMenu = coreComponent.createMenuSymbol("PORT_MENU", None)
portMenu.setLabel("Ports")
portMenu.setDescription("Configuraiton for PORT PLIB")

portEnable = coreComponent.createBooleanSymbol("PORT_ENABLE", portMenu)
portEnable.setLabel("Use PORT PLIB ?")
portEnable.setDefaultValue(True)
portEnable.setReadOnly(True)

portPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", portEnable, Pin.getPackageNames())
portPackage.setLabel("Pin Package")
portPackage.setReadOnly(True)

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################

pinConfiguration = coreComponent.createMenuSymbol("PORT_PIN_CONFIGURATION", portEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuraiton for PORT Pins")

pin = []
pinName = []
pinType = []
pinPeripheralFunction = []
pinBitPosition = []
global pinGroup
pinGroup = []
pinMode = []
pinDirection = []
pinLatch = []
pinPullEnable = []
pinInputEnable = []
pinGroupList = []

packagePinCount = Pin.getPackagePinCount(portPackage.getValue())

for pinNumber in range(1, packagePinCount + 1):

    portSignalNode = ATDF.getNode("/avr-tools-device-file/devices/device@[family=\"PIC32CM\"]/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/signals/signal@[index=\""+ str(pinNumber - 1) +"\"]")

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

    pin.append(pinNumber)
    pin[pinNumber-1] = coreComponent.createMenuSymbol("PORT_PIN" + str(pinNumber), pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pinNumber))
    pin[pinNumber-1].setDescription("Configuraiton for Pin " + str(pinNumber) )

    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    pinName[pinNumber-1].setReadOnly(True)

    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    pinName[pinNumber-1].setReadOnly(True)

    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PORT_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinName[pinNumber-1].setReadOnly(True)

    pinGroup.append(pinNumber)
    pinGroup[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PORT_GROUP", pin[pinNumber-1])
    pinGroup[pinNumber-1].setLabel("Group")
    pinGroup[pinNumber-1].setDefaultValue("")
    pinName[pinNumber-1].setReadOnly(True)

    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setLabel("Mode")
    pinName[pinNumber-1].setReadOnly(True)

    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")
    pinName[pinNumber-1].setReadOnly(True)

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    pinName[pinNumber-1].setReadOnly(True)

    pinPullEnable.append(pinNumber)
    pinPullEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PULLEN", pin[pinNumber-1])
    pinPullEnable[pinNumber-1].setLabel("Pull Enable")
    pinName[pinNumber-1].setReadOnly(True)

    pinInputEnable.append(pinNumber)
    pinInputEnable[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_INEN", pin[pinNumber-1])
    pinInputEnable[pinNumber-1].setLabel("Input Enable")
    pinName[pinNumber-1].setReadOnly(True)

    #list created only for dependecy
    pinGroupList.append(pinNumber)
    pinGroupList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PORT_GROUP"

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

portConfiguration = coreComponent.createMenuSymbol("PORT_CONFIGURATIONS", portEnable)
portConfiguration.setLabel("Port Registers Configuration")

portModuleGC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]/register-group@[name=\"PORT\"]/register-group@[name-in-module=\"GROUP\"]")
portModuleGroupCount = portModuleGC.getAttribute("count")

#port group count
portSym_Count = coreComponent.createIntegerSymbol("PORT_GROUP_COUNT", portConfiguration)
portSym_Count.setVisible(False)
portSym_Count.setDefaultValue(int(portModuleGroupCount))

portSym_PinCount = coreComponent.createIntegerSymbol("PORT_PIN_COUNT", portMenu)
portSym_PinCount.setLabel("No Of Pins")
portSym_PinCount.setVisible(False)
portSym_PinCount.setDefaultValue(int(packagePinCount))

global group
group = [0 for i in range(int(portModuleGroupCount))]

global portGroup
portGroup = []

global usePort
usePort = []

port = []
portSym_PINCFG = [[]]
portSym_PINCFG_PMUXEN = [[]]
portSym_PINCFG_INEN = [[]]
portSym_PINCFG_DRVSTR = [[]]
portSym_PINCFG_PULLEN = [[]]
portSym_PORT_PMUX = [[]]
portSym_PORT_DIR = []
portSym_PORT_CTRL = []

for portNumber in range(0, len(group)):

    port.append(portNumber)
    port[portNumber] = coreComponent.createMenuSymbol("PORT_GROUP_" + str(portNumber) + "_CONFIGURATION", portConfiguration)
    port[portNumber].setLabel("PORT GROUP " + str(portNumber) + " Configuration")

    #creating list for port group
    portGroup.append(str(portNumber))

    usePort.append(portNumber)
    usePort[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber), port[portNumber])
    usePort[portNumber].setLabel("Use PORT GROUP " + str(portNumber))

    portSym_PORT_DIR.append(portNumber)
    portSym_PORT_DIR[portNumber] = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_DIR", port[portNumber])
    portSym_PORT_DIR[portNumber].setLabel("Port Pin Direction")
    portSym_PORT_DIR[portNumber].setDefaultValue("0x00000000")

    portSym_PORT_CTRL.append(portNumber)
    portSym_PORT_CTRL[portNumber] = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_CTRL", port[portNumber])
    portSym_PORT_CTRL[portNumber].setLabel("Enable Input Synchronizer ?")
    portSym_PORT_CTRL[portNumber].setDefaultValue("0x00000000")

    for pinNum in range(0, 32):
        portSym_PINCFG.append(pinNum)
        portSym_PINCFG[portNumber] = coreComponent.createMenuSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum), port[portNumber])
        portSym_PINCFG[portNumber].setLabel("PORT GROUP" + str(portNumber) + " PINCFG" + str(pinNum))

        #Enables the Peripheral Multiplexer on the pin
        portSym_PINCFG_PMUXEN.append(pinNum)
        portSym_PINCFG_PMUXEN[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) + "_PMUXEN", portSym_PINCFG[portNumber])
        portSym_PINCFG_PMUXEN[portNumber].setLabel("Enable Pin Peripheral Multiplexer")

        #Enables or disabled Pin Input Buffer
        portSym_PINCFG_INEN.append(pinNum)
        portSym_PINCFG_INEN[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) + "_INEN", portSym_PINCFG[portNumber])
        portSym_PINCFG_INEN[portNumber].setLabel("Enable Pin Input Buffer")

        #Enables or disabled enhanced Pin Drive Strength
        portSym_PINCFG_DRVSTR.append(pinNum)
        portSym_PINCFG_DRVSTR[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) + "_DRVSTR", portSym_PINCFG[portNumber])
        portSym_PINCFG_DRVSTR[portNumber].setLabel("Enable Pin Strong Drive Strength")

        #Enables or disable the internal pull up resistor
        portSym_PINCFG_PULLEN.append(pinNum)
        portSym_PINCFG_PULLEN[portNumber] = coreComponent.createBooleanSymbol("PORT_GROUP_" + str(portNumber) + "_PINCFG" + str(pinNum) + "_PULLEN", portSym_PINCFG[portNumber])
        portSym_PINCFG_PULLEN[portNumber].setLabel("Enable Internal Pull Up Resistor")

    for pinNum in range(0, 16):
        portSym_PORT_PMUX.append(pinNum)
        portSym_PORT_PMUX[portNumber] = coreComponent.createStringSymbol("PORT_GROUP_" + str(portNumber) + "_PMUX" + str(pinNum) , port[portNumber])
        portSym_PORT_PMUX[portNumber].setLabel("PORT GROUP" + str(portNumber) + " PMUX" + str(pinNum))
        portSym_PORT_PMUX[portNumber].setDefaultValue("0x00")

usePort[0].setDependencies(setupPort, pinGroupList)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################
configName = Variables.get("__CONFIGURATION_NAME")

portModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PORT\"]")
portModuleID = portModuleNode.getAttribute("id")

portSym_HeaderFile = coreComponent.createFileSymbol("PORT_HEADER", None)
portSym_HeaderFile.setSourcePath("../peripheral/port_"+portModuleID+"/templates/plib_port.h.ftl")
portSym_HeaderFile.setOutputName("plib_port.h")
portSym_HeaderFile.setDestPath("config/" + configName + "/peripheral/port/")
portSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/port/")
portSym_HeaderFile.setType("HEADER")
portSym_HeaderFile.setMarkup(True)

portSym_SourceFile = coreComponent.createFileSymbol("PORT_SOURCE", None)
portSym_SourceFile.setSourcePath("../peripheral/port_"+portModuleID+"/templates/plib_port.c.ftl")
portSym_SourceFile.setOutputName("plib_port.c")
portSym_SourceFile.setDestPath("config/" + configName + "/peripheral/port/")
portSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/port/")
portSym_SourceFile.setType("SOURCE")
portSym_SourceFile.setMarkup(True)

portSym_SystemInitFile = coreComponent.createFileSymbol("PORT_SYS_INIT", None)
portSym_SystemInitFile.setSourcePath("../peripheral/port_"+portModuleID+"/templates/system/initialization.c.ftl")
portSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
portSym_SystemInitFile.setType("STRING")
portSym_SystemInitFile.setMarkup(True)

portSym_SystemDefFile = coreComponent.createFileSymbol("PORT_SYS_DEF", None)
portSym_SystemDefFile.setSourcePath("../peripheral/port_"+portModuleID+"/templates/system/definitions.h.ftl")
portSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
portSym_SystemDefFile.setType("STRING")
portSym_SystemDefFile.setMarkup(True)
