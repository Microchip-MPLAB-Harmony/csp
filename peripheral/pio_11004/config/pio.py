print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

# Function to enable PORT Channel specific interrupt when any of the pins has interrupt enabled on that particular channel.
def setupInterrupt(portInterruptLocal, pinInterrupt):
    if pinInterrupt.getValue() != "":
        i = []
        # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
        
        # Split the id name by "_" and put all the splitted names in the list "i"
        i = pinInterrupt.getID().split("_")
        
        # 2nd element of the list is suppose to be the pin number which we want, get that in J
        j = pinChannel[int(i[1])].getValue()
        
        # find the index of the string "j" in the list "channel" and save it in k.
        k = channel.index(j)
        
        portInterrupt[k].setValue(portInterruptLocal.getID() + "INT_VALUE", True, 1)

# Function to enable PORT Channel when any of the pins is using the particular channel.
# Once the PORT channel is enabled, option of corresponding channel interrupt also starts showing up.        
def setupPort(usePort, pinChannel):

  #  if ((pinChannel.getValue() == "B" and usePort.getID() == "PIO_INST_IDX1") or (pinChannel.getValue() == "A" and usePort.getID == "PIO_INST_IDX0") or (pinChannel.getValue() == "C" and usePort.getID == "PIO_INST_IDX2") or (pinChannel.getValue() == "D" and usePort.getID == "PIO_INST_IDX3") or (pinChannel.getValue() == "E" and usePort.getID == "PIO_INST_IDX4")):
    # the above "if" statement is not working for some strange reasons, thats why it has been divided in "if-elif" below.
    if(pinChannel.getValue() == "A" and usePort.getID() == "PIO_INST_IDX0"):
        i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[int(i)].setVisible(True)
        
    elif(pinChannel.getValue() == "B" and usePort.getID() == "PIO_INST_IDX1"):
        i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[int(i)].setVisible(True)
        
    elif(pinChannel.getValue() == "C" and usePort.getID() == "PIO_INST_IDX2"):
        i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[int(i)].setVisible(True)
        
    elif(pinChannel.getValue() == "D" and usePort.getID() == "PIO_INST_IDX3"):
        i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[int(i)].setVisible(True)
        
    elif(pinChannel.getValue() == "E" and usePort.getID() == "PIO_INST_IDX4"):
        i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[int(i)].setVisible(True)


###################################################################################################
######################################### PIO Main Menu  ##########################################
###################################################################################################
        
pioMenu = coreComponent.createMenuSymbol(None, None)
pioMenu.setLabel("PIO")
pioMenu.setDescription("Configuraiton for PIO PLIB")

pioEnable = coreComponent.createBooleanSymbol("PIO_ENABLE", pioMenu)
pioEnable.setLabel("Use PIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)

pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, Pin.getPackageNames())
pioPackage.setLabel("Pin Package")
#pioPackage.setDefaultValue("")

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################
    
pinConfiguration = coreComponent.createMenuSymbol(None, pioEnable)
pinConfiguration.setLabel("Pin Configuration")
pinConfiguration.setDescription("Configuraiton for PIO Pins")

pin = []
pinName = []
pinType = []
pinPeripheralFunction = []
pinBitPosition = []
global pinChannel
pinChannel = []
pinMode = []
pinDirection = []
pinLatch = []
pinOpenDrain = []
pinPullUp = []
pinPullDown = []
pinInterrupt = []

pinChannelList = []
pinInterruptList = []

packagePinCount = Pin.getPackagePinCount(pioPackage.getValue())

for pinNumber in range(0, packagePinCount):
    pin.append(pinNumber)
    pin[pinNumber]= coreComponent.createMenuSymbol(None, pinConfiguration)
    pin[pinNumber].setLabel("Pin " + str(pinNumber))
    pin[pinNumber].setDescription("Configuraiton for Pin " + str(pinNumber) )
    
    pinName.append(pinNumber)
    pinName[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber])
    pinName[pinNumber].setLabel("Name")
    pinName[pinNumber].setDefaultValue("")
    
    pinType.append(pinNumber)
    pinType[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber])
    pinType[pinNumber].setLabel("Type")
    
    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber])
    pinPeripheralFunction[pinNumber].setLabel("Peripheral Selection")
    
    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PIO_PIN", pin[pinNumber])
    pinBitPosition[pinNumber].setLabel("Bit Position")
    
    pinChannel.append(pinNumber)
    pinChannel[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_CHANNEL", pin[pinNumber])
    pinChannel[pinNumber].setLabel("Channel")
    pinChannel[pinNumber].setDefaultValue("")
    
    pinMode.append(pinNumber)
    pinMode[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_MODE", pin[pinNumber])
    pinMode[pinNumber].setLabel("Mode")
    
    pinDirection.append(pinNumber)
    pinDirection[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber])
    pinDirection[pinNumber].setLabel("Direction")

    pinLatch.append(pinNumber)
    pinLatch[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber])
    pinLatch[pinNumber].setLabel("Initial Latch Value")
    
    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_OD", pin[pinNumber])
    pinOpenDrain[pinNumber].setLabel("Open Drain")
    
    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PU", pin[pinNumber])
    pinPullUp[pinNumber].setLabel("Pull Up")
    
    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PD", pin[pinNumber])
    pinPullDown[pinNumber].setLabel("Pull Down")
    
    pinInterrupt.append(pinNumber)
    # This symbol ID name is split and pin number is extracted and used inside "setupInterrupt" function. so be careful while changing the name of this ID.
    pinInterrupt[pinNumber] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT", pin[pinNumber])
    pinInterrupt[pinNumber].setLabel("PIO Interrupt")

    #list created only for dependecy
    pinChannelList.append(pinNumber)
    pinChannelList[pinNumber] = "PIN_" + str(pinNumber) +"_PIO_CHANNEL"
    
    #list created only for dependecy
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber] = "PIN_" + str(pinNumber) +"_PIO_INTERRUPT"

###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

portConfiguration = coreComponent.createMenuSymbol(None, pioEnable)
portConfiguration.setLabel("Port Registers Configuration")

global channel
channel = ["A", "B", "C", "D", "E"]
port = []
usePort = []  

global portInterrupt
portInterrupt = [] 
   
pioSym_PIO_PER = []
pioSym_PIO_ABCDSR1 = []
pioSym_PIO_ABCDSR2 = []
pioSym_PIO_IER = []
pioSym_PIO_AIMER = []
pioSym_PIO_ESR = []
pioSym_PIO_REHLSR = []
pioSym_PIO_OER = []
pioSym_PIO_PUER = []
pioSym_PIO_PPDEN = []
pioSym_PIO_MDER = []
pioSym_PIO_SODR = []

    
for portNumber in range(0, len(channel)):

    port.append(portNumber)
    port[portNumber]= coreComponent.createMenuSymbol(None, portConfiguration)
    port[portNumber].setLabel("PORT " + channel[portNumber] + " Configuration")

    
    usePort.append(portNumber)
    usePort[portNumber]= coreComponent.createBooleanSymbol("PIO_INST_IDX" + str(portNumber), port[portNumber])
    usePort[portNumber].setLabel("Use PORT " + channel[portNumber])
    usePort[portNumber].setDependencies(setupPort, pinChannelList)
    
    portInterrupt.append(portNumber)
    portInterrupt[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(channel[portNumber]) + "_INTERRUPT_USED", usePort[portNumber])
    portInterrupt[portNumber].setLabel("Use Interrupt for PORT " + channel[portNumber])   
    portInterrupt[portNumber].setDefaultValue(False)
    portInterrupt[portNumber].setVisible(False)
    portInterrupt[portNumber].setDependencies(setupInterrupt, pinInterruptList)
    
    pioSym_PIO_PER.append(portNumber)
    pioSym_PIO_PER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_PER_VALUE", port[portNumber])
    pioSym_PIO_PER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PER")
    pioSym_PIO_PER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_ABCDSR1.append(portNumber)
    pioSym_PIO_ABCDSR1[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR1_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR1[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR1")
    pioSym_PIO_ABCDSR1[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_ABCDSR2.append(portNumber)
    pioSym_PIO_ABCDSR2[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR2_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR2[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR2")
    pioSym_PIO_ABCDSR2[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_IER.append(portNumber)
    pioSym_PIO_IER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_IER_VALUE", port[portNumber])
    pioSym_PIO_IER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_IER")
    pioSym_PIO_IER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_AIMER.append(portNumber)
    pioSym_PIO_AIMER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_AIMER_VALUE", port[portNumber])
    pioSym_PIO_AIMER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_AIMER")
    pioSym_PIO_AIMER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_ESR.append(portNumber)
    pioSym_PIO_ESR[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_ESR_VALUE", port[portNumber])
    pioSym_PIO_ESR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ESR")
    pioSym_PIO_ESR[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_REHLSR.append(portNumber)
    pioSym_PIO_REHLSR[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_REHLSR_VALUE", port[portNumber])
    pioSym_PIO_REHLSR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_REHLSR")
    pioSym_PIO_REHLSR[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_OER.append(portNumber)
    pioSym_PIO_OER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_OER_VALUE", port[portNumber])
    pioSym_PIO_OER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_OER")
    pioSym_PIO_OER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_PUER.append(portNumber)
    pioSym_PIO_PUER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_PUER_VALUE", port[portNumber])
    pioSym_PIO_PUER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PUER")
    pioSym_PIO_PUER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_PPDEN.append(portNumber)
    pioSym_PIO_PPDEN[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_PPDEN_VALUE", port[portNumber])
    pioSym_PIO_PPDEN[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PPDEN")
    pioSym_PIO_PPDEN[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_MDER.append(portNumber)
    pioSym_PIO_MDER[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_MDER_VALUE", port[portNumber])
    pioSym_PIO_MDER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_MDER")
    pioSym_PIO_MDER[portNumber].setDefaultValue(00000000)
    
    pioSym_PIO_SODR.append(portNumber)
    pioSym_PIO_SODR[portNumber] = coreComponent.createHexSymbol("PIO" + str(channel[portNumber]) + "_SODR_VALUE", port[portNumber])
    pioSym_PIO_SODR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_SODR")
    pioSym_PIO_SODR[portNumber].setDefaultValue(00000000)
    
pioSym_AFEC0_CHER = coreComponent.createHexSymbol("PIO_AFEC0_CHER_VALUE", portConfiguration)
pioSym_AFEC0_CHER.setLabel("AFEC0_CHER")
pioSym_AFEC0_CHER.setDefaultValue(00000000)

pioSym_AFEC1_CHER = coreComponent.createHexSymbol("PIO_AFEC1_CHER_VALUE", portConfiguration)
pioSym_AFEC1_CHER.setLabel("AFEC1_CHER")
pioSym_AFEC1_CHER.setDefaultValue(00000000)

pioSym_DACC_CHER = coreComponent.createHexSymbol("PIO_DACC_CHER_VALUE", portConfiguration)
pioSym_DACC_CHER.setLabel("DACC_CHER")
pioSym_DACC_CHER.setDefaultValue(00000000)

###################################################################################################
################################### Pin Type related code  ########################################
###################################################################################################

pinType = coreComponent.createMenuSymbol(None, pioEnable)
pinType.setLabel("Pin Types")
pinType.setDescription("Type of PIO Pins")

type = []
typeName = []
typePinMode = []
typePinDirection = []
typePinLatch = []
typePinOpenDrain = []
typePinCN = []
typePinPullUp = []
typePinPullDown = []
typePinInterrupt = []


for pinTypeNumber in range(0, 20):

    type.append(pinTypeNumber)
    type[pinTypeNumber]= coreComponent.createMenuSymbol(None, pinType)
    type[pinTypeNumber].setLabel("Type " + str(pinTypeNumber))
    
    typeName.append(pinTypeNumber)
    typeName[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_TYPE" + str(pinTypeNumber), type[pinTypeNumber])
    typeName[pinTypeNumber].setLabel("Type Name")
    typeName[pinTypeNumber].setDefaultValue("")
    
    typePinMode.append(pinTypeNumber)
    typePinMode[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_MODE" + str(pinTypeNumber), type[pinTypeNumber])
    typePinMode[pinTypeNumber].setLabel("Mode")
    
    typePinDirection.append(pinTypeNumber)
    typePinDirection[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_DIR" + str(pinTypeNumber), type[pinTypeNumber])
    typePinDirection[pinTypeNumber].setLabel("Direction")

    typePinLatch.append(pinTypeNumber)
    typePinLatch[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_LAT" + str(pinTypeNumber), type[pinTypeNumber])
    typePinLatch[pinTypeNumber].setLabel("Initial Latch Value")
    
    typePinOpenDrain.append(pinTypeNumber)
    typePinOpenDrain[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_OD" + str(pinTypeNumber), type[pinTypeNumber])
    typePinOpenDrain[pinTypeNumber].setLabel("Open Drain")
    
    typePinCN.append(pinTypeNumber)
    typePinCN[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_CN" + str(pinTypeNumber), type[pinTypeNumber])
    typePinCN[pinTypeNumber].setLabel("Change Notice")
    
    typePinPullUp.append(pinTypeNumber)
    typePinPullUp[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_PU" + str(pinTypeNumber), type[pinTypeNumber])
    typePinPullUp[pinTypeNumber].setLabel("Pull Up")
    
    typePinPullDown.append(pinTypeNumber)
    typePinPullDown[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_PD" + str(pinTypeNumber), type[pinTypeNumber])
    typePinPullDown[pinTypeNumber].setLabel("Pull Down")
    
    typePinInterrupt.append(pinTypeNumber)
    typePinInterrupt[pinTypeNumber] = coreComponent.createStringSymbol("BSP_CUSTOM_PIO_INTERRUPT" + str(pinTypeNumber), type[pinTypeNumber])
    typePinInterrupt[pinTypeNumber].setLabel("PIO Interrupt")

#print("==============================================")
#print("Pin Information")
#print("")
#
#print("Package count: " + str(Pin.getPackageCount()))
#portsPackageNames = Pin.getPackageNames()
#print('Package names: [%s]' % ', '.join(map(str, portsPackageNames)))
#print("Pin count for package " + portsPackageNames[0] + ": " + str(Pin.getPackagePinCount(portsPackageNames[0])))
#print("Largest package: " + Pin.getLargestPackageName())
#portsPinNames = Pin.getPinPositions(portsPackageNames[0])
#print('Pin positions for package ' + portsPackageNames[0] + ': [%s]' % ', '.join(map(str, portsPinNames)))
#print(" Pin " + portsPinNames[0] + " is " + Pin.getPinPad(portsPackageNames[0], portsPinNames[0]))
#print(" Pin " + portsPinNames[1] + " is " + Pin.getPinPad(portsPackageNames[0], portsPinNames[1]))
#print(" Pin " + portsPinNames[2] + " is " + Pin.getPinPad(portsPackageNames[0], portsPinNames[2]))
#print(" Pin " + portsPinNames[3] + " is " + Pin.getPinPad(portsPackageNames[0], portsPinNames[3]))
#print("==============================================")

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")
    
pioHeader1File = coreComponent.createFileSymbol(None, None)
pioHeader1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.h.ftl")
pioHeader1File.setOutputName("plib_pio.h")
pioHeader1File.setDestPath("system_config/" + configName +"/peripheral/pio/")
pioHeader1File.setProjectPath("system_config/" + configName +"/peripheral/pio/")
pioHeader1File.setType("HEADER")
pioHeader1File.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol(None, None)
pioSource1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.c.ftl")
pioSource1File.setOutputName("plib_pio.c")
pioSource1File.setDestPath("system_config/" + configName +"/peripheral/pio/")
pioSource1File.setProjectPath("system_config/" + configName +"/peripheral/pio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)

pioInterruptSource1File = coreComponent.createFileSymbol(None, None)
pioInterruptSource1File.setSourcePath("../peripheral/pio_11004/templates/pio_interrupt.c.ftl")
pioInterruptSource1File.setOutputName("pio_interrupt.c")
pioInterruptSource1File.setDestPath("system_config/" + configName +"/peripheral/pio/")
pioInterruptSource1File.setProjectPath("system_config/" + configName +"/peripheral/pio/")
pioInterruptSource1File.setType("SOURCE")
pioInterruptSource1File.setMarkup(True)

#pioSystemConfigFile = coreComponent.createFileSymbol(None, None)
#pioSystemConfigFile.setSourcePath("../peripheral/pio_11004/templates/pio_system_config.h.ftl")
#pioSystemConfigFile.setOutputName("pio_system_config.h")
#pioSystemConfigFile.setDestPath("system_config/" + configName +"/peripheral/pio/")
#pioSystemConfigFile.setProjectPath("system_config/" + configName +"/peripheral/pio/")
#pioSystemConfigFile.setType("HEADER")
#pioSystemConfigFile.setMarkup(True)

pioLocalHeader1File = coreComponent.createFileSymbol(None, None)
pioLocalHeader1File.setSourcePath("../peripheral/pio_11004/plib_pio_local.h")
pioLocalHeader1File.setOutputName("plib_pio_local.h")
pioLocalHeader1File.setDestPath("system_config/" + configName +"/peripheral/pio/")
pioLocalHeader1File.setProjectPath("system_config/" + configName +"/peripheral/pio/")
pioLocalHeader1File.setType("HEADER")
pioLocalHeader1File.setMarkup(False)
