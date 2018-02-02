print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

# Function to enable PORT Channel specific interrupt when any of the pins has interrupt enabled on that particular channel.
def setupInterrupt(portInterruptLocal, pinInterruptLocal):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    
    # Split the id name by "_" and put all the splitted names in the list "i"
    i = pinInterruptLocal.getID().split("_")
    
    # 2nd element of the list is suppose to be the pin number which we want, get the channel name of that pin in J
    j = pinChannel[int(i[1])-1].getValue()
    # find the index of the string "j" in the list "channel" and save it in k.
    k = channel.index(j)
        
    if pinInterruptLocal.getValue() != "":
        portInterrupt[k].setValue(portInterruptLocal.getID() + "INT_VALUE", True, 1)
    else:
        # if interrupt has been disabled for a particular pin, then see if is it disabled for all the pins of
        # corresponding channel; if so, then uncheck corresponding port interrupt in GUI.
        boolValue = False
        for pinNumber in range(1, packagePinCount+1):
            if j == pinChannel[pinNumber-1].getValue():
                if pinInterrupt[pinNumber-1].getValue() != "":
                    boolValue = True
                    break
        if boolValue == False:
            portInterrupt[k].setValue(portInterruptLocal.getID() + "INT_VALUE_1", False, 1)    
            
# Function to enable PORT Channel when any of the pins is using the particular channel.
# Once the PORT channel is enabled, option of corresponding channel interrupt also starts showing up.        
def setupPort(usePort, pinChannelLocal):
    
    # Split the id name by "_" and put all the splitted names in the list "i"
    # 2nd element in the list will be the port name
    i = usePort.getID().split("_")
    # find the index of the string i[1] in the list "channel" and save it in k.
    k = channel.index(i[1])
    
  #  if ((pinChannelLocal.getValue() == "B" and usePort.getID() == "PIO_B_USED") or (pinChannelLocal.getValue() == "A" and usePort.getID == "PIO_A_USED") or (pinChannelLocal.getValue() == "C" and usePort.getID == "PIO_C_USED") or (pinChannelLocal.getValue() == "D" and usePort.getID == "PIO_D_USED") or (pinChannelLocal.getValue() == "E" and usePort.getID == "PIO_E_USED")):
    # the above "if" statement is not working for some strange reasons, thats why it has been divided in "if-elif" below.
    if(pinChannelLocal.getValue() == "A" and usePort.getID() == "PIO_A_USED"):
            
     #   i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[k].setVisible(True)
        
    elif(pinChannelLocal.getValue() == "B" and usePort.getID() == "PIO_B_USED"):
     #   i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[k].setVisible(True)
        
    elif(pinChannelLocal.getValue() == "C" and usePort.getID() == "PIO_C_USED"):
      #  i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[k].setVisible(True)
        
    elif(pinChannelLocal.getValue() == "D" and usePort.getID() == "PIO_D_USED"):
     #   i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[k].setVisible(True)
        
    elif(pinChannelLocal.getValue() == "E" and usePort.getID() == "PIO_E_USED"):
      #  i = usePort.getID()[-1]
        usePort.setValue(usePort.getID() + "DYN_VALUE", True, 1)
        portInterrupt[k].setVisible(True)


###################################################################################################
######################################### PIO Main Menu  ##########################################
###################################################################################################
        
pioMenu = coreComponent.createMenuSymbol(None, None)
pioMenu.setLabel("Ports (PIO)")
pioMenu.setDescription("Configuration for PIO PLIB")

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
pinConfiguration.setDescription("Configuration for PIO Pins")

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
global pinInterrupt
pinInterrupt = []

pinChannelList = []
pinInterruptList = []

global packagePinCount
packagePinCount = Pin.getPackagePinCount(pioPackage.getValue())

# Note that all the lists below starts from 0th index and goes till "packagePinCount-1"
# But actual pin numbers on the device starts from 1 (not from 0) and goes till "packagePinCount"
# that is why "pinNumber-1" is used to index the lists wherever applicable.
for pinNumber in range(1, packagePinCount + 1):
    pin.append(pinNumber)
    pin[pinNumber-1]= coreComponent.createMenuSymbol(None, pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pinNumber))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pinNumber) )
    
    pinName.append(pinNumber)
    pinName[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_NAME", pin[pinNumber-1])
    pinName[pinNumber-1].setLabel("Name")
    pinName[pinNumber-1].setDefaultValue("")
    
    pinType.append(pinNumber)
    pinType[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_FUNCTION_TYPE", pin[pinNumber-1])
    pinType[pinNumber-1].setLabel("Type")
    
    pinPeripheralFunction.append(pinNumber)
    pinPeripheralFunction[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PERIPHERAL_FUNCTION", pin[pinNumber-1])
    pinPeripheralFunction[pinNumber-1].setLabel("Peripheral Selection")
    
    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PIO_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    
    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
    
    pinMode.append(pinNumber)
    pinMode[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_MODE", pin[pinNumber-1])
    pinMode[pinNumber-1].setLabel("Mode")
    
    pinDirection.append(pinNumber)
    pinDirection[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_DIR", pin[pinNumber-1])
    pinDirection[pinNumber-1].setLabel("Direction")

    pinLatch.append(pinNumber)
    pinLatch[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_LAT", pin[pinNumber-1])
    pinLatch[pinNumber-1].setLabel("Initial Latch Value")
    
    pinOpenDrain.append(pinNumber)
    pinOpenDrain[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_OD", pin[pinNumber-1])
    pinOpenDrain[pinNumber-1].setLabel("Open Drain")
    
    pinPullUp.append(pinNumber)
    pinPullUp[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PU", pin[pinNumber-1])
    pinPullUp[pinNumber-1].setLabel("Pull Up")
    
    pinPullDown.append(pinNumber)
    pinPullDown[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PD", pin[pinNumber-1])
    pinPullDown[pinNumber-1].setLabel("Pull Down")
    
    pinInterrupt.append(pinNumber)
    # This symbol ID name is split and pin number is extracted and used inside "setupInterrupt" function. so be careful while changing the name of this ID.
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("PIO Interrupt")

    #list created only for dependecy
    pinChannelList.append(pinNumber)
    pinChannelList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PIO_CHANNEL"
    
    #list created only for dependecy
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PIO_INTERRUPT"

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
global pioSym_PIO_ABCDSR1
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
    usePort[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(channel[portNumber]) + "_USED", port[portNumber])
    usePort[portNumber].setLabel("Use PORT " + channel[portNumber])
    usePort[portNumber].setDependencies(setupPort, pinChannelList)
    
    portInterrupt.append(portNumber)
    portInterrupt[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(channel[portNumber]) + "_INTERRUPT_USED", usePort[portNumber])
    portInterrupt[portNumber].setLabel("Use Interrupt for PORT " + channel[portNumber])   
    portInterrupt[portNumber].setDefaultValue(False)
    portInterrupt[portNumber].setVisible(False)
    portInterrupt[portNumber].setDependencies(setupInterrupt, pinInterruptList)
    
    pioSym_PIO_PER.append(portNumber)
    pioSym_PIO_PER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PER_VALUE", port[portNumber])
    pioSym_PIO_PER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PER")
    pioSym_PIO_PER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_ABCDSR1.append(portNumber)
    pioSym_PIO_ABCDSR1[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR1_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR1[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR1")
    pioSym_PIO_ABCDSR1[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_ABCDSR2.append(portNumber)
    pioSym_PIO_ABCDSR2[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR2_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR2[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR2")
    pioSym_PIO_ABCDSR2[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_IER.append(portNumber)
    pioSym_PIO_IER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_IER_VALUE", port[portNumber])
    pioSym_PIO_IER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_IER")
    pioSym_PIO_IER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_AIMER.append(portNumber)
    pioSym_PIO_AIMER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_AIMER_VALUE", port[portNumber])
    pioSym_PIO_AIMER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_AIMER")
    pioSym_PIO_AIMER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_ESR.append(portNumber)
    pioSym_PIO_ESR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ESR_VALUE", port[portNumber])
    pioSym_PIO_ESR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ESR")
    pioSym_PIO_ESR[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_REHLSR.append(portNumber)
    pioSym_PIO_REHLSR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_REHLSR_VALUE", port[portNumber])
    pioSym_PIO_REHLSR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_REHLSR")
    pioSym_PIO_REHLSR[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_OER.append(portNumber)
    pioSym_PIO_OER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_OER_VALUE", port[portNumber])
    pioSym_PIO_OER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_OER")
    pioSym_PIO_OER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_PUER.append(portNumber)
    pioSym_PIO_PUER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PUER_VALUE", port[portNumber])
    pioSym_PIO_PUER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PUER")
    pioSym_PIO_PUER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_PPDEN.append(portNumber)
    pioSym_PIO_PPDEN[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PPDEN_VALUE", port[portNumber])
    pioSym_PIO_PPDEN[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PPDEN")
    pioSym_PIO_PPDEN[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_MDER.append(portNumber)
    pioSym_PIO_MDER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_MDER_VALUE", port[portNumber])
    pioSym_PIO_MDER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_MDER")
    pioSym_PIO_MDER[portNumber].setDefaultValue("0x00000000")
    
    pioSym_PIO_SODR.append(portNumber)
    pioSym_PIO_SODR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_SODR_VALUE", port[portNumber])
    pioSym_PIO_SODR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_SODR")
    pioSym_PIO_SODR[portNumber].setDefaultValue("0x00000000")
    
pioSym_AFEC0_CHER = coreComponent.createStringSymbol("PIO_AFEC0_CHER_VALUE", portConfiguration)
pioSym_AFEC0_CHER.setLabel("AFEC0_CHER")
pioSym_AFEC0_CHER.setDefaultValue("0x00000000")

pioSym_AFEC1_CHER = coreComponent.createStringSymbol("PIO_AFEC1_CHER_VALUE", portConfiguration)
pioSym_AFEC1_CHER.setLabel("AFEC1_CHER")
pioSym_AFEC1_CHER.setDefaultValue("0x00000000")

pioSym_DACC_CHER = coreComponent.createStringSymbol("PIO_DACC_CHER_VALUE", portConfiguration)
pioSym_DACC_CHER.setLabel("DACC_CHER")
pioSym_DACC_CHER.setDefaultValue("0x00000000")

pioMatrixSym_CCFG_SYSIO = coreComponent.createStringSymbol("PIO_CCFG_SYSIO_VALUE", portConfiguration)
pioMatrixSym_CCFG_SYSIO.setLabel("CCFG_SYSIO")
pioMatrixSym_CCFG_SYSIO.setDescription("System Pins as GPIO")
pioMatrixSym_CCFG_SYSIO.setDefaultValue("0x00000000")



###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")
    
pioHeader1File = coreComponent.createFileSymbol(None, None)
pioHeader1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.h.ftl")
pioHeader1File.setOutputName("plib_pio.h")
pioHeader1File.setDestPath("/peripheral/pio/")
pioHeader1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioHeader1File.setType("HEADER")
pioHeader1File.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol(None, None)
pioSource1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.c.ftl")
pioSource1File.setOutputName("plib_pio.c")
pioSource1File.setDestPath("/peripheral/pio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)


pioSystemInitFile = coreComponent.createFileSymbol(None, None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
pioSystemInitFile.setSourcePath("../peripheral/pio_11004/templates/system/system_initialize.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemIntFile = coreComponent.createFileSymbol(None, None)
pioSystemIntFile.setType("STRING")
pioSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
pioSystemIntFile.setSourcePath("../peripheral/pio_11004/templates/system/system_interrupt.c.ftl")
pioSystemIntFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol(None, None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/pio_11004/templates/system/system_definitions.h.ftl")
pioSystemDefFile.setMarkup(True)
