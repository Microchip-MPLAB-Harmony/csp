print("Loading Pin Manager for " + Variables.get("__PROCESSOR"))

portInterruptList = []
InternalNVICVectorChange = []

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################

# Dependency Function to show or hide the warning message depending on Clock/Interrupt
# enable/disable status from clock/interrupt manager respectively
def ClockInterruptStatusWarning(symbol, event):
   if event["value"] == False:
       symbol.setVisible(True)
   else:
       symbol.setVisible(False)     

# Dependency Function to pass interrupt related info to NVIC Manager.    
# This function will be entered only by internal change happening to PORT Channel interrupt, never by manual
# change because channel interrupt is not user configurable directly.    
def NVICControl(pioNVIC, event):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    # Split the id name by "_" and put all the splitted names in the list "i"
    i = event["id"].split("_")
    k = channel.index(i[1])
    
    global NVICHandlerLock
    global pioSymIntEnComment
    
    if (event["value"] == True):
        Database.setSymbolValue("core", NVICVector[k], True, 1)
        Database.setSymbolValue("core", NVICHandler[k], "PORT" + i[1] + "_InterruptHandler", 1)
        Database.setSymbolValue("core", NVICHandlerLock[k], True, 1)
    else :
        Database.setSymbolValue("core", NVICVector[k], False, 1)
        Database.setSymbolValue("core", NVICHandler[k], "PORT" + i[1] + "_Handler", 1)
        Database.setSymbolValue("core", NVICHandlerLock[k], False, 1)
    
    # show or hide the warning message depending on Interrupt enable/disable status from PIN Manager. 
    if (portInterrupt[k].getValue() == True and Database.getSymbolValue("core", NVICVector[k]) == False):
        pioSymIntEnComment[k].setVisible(True)
    else:
        pioSymIntEnComment[k].setVisible(False)
        
# Function to enable PORT Channel specific interrupt when any of the pins has interrupt enabled on that particular channel.
def setupInterrupt(portInterruptLocal, event):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    # Split the id name by "_" and put all the splitted names in the list "i"
    i = event["id"].split("_")
    
    # 2nd element of the list is suppose to be the pin number which we want, get the channel name of that pin in J
    j = pinChannel[int(i[1])-1].getValue()
    # find the index of the string "j" in the list "channel" and save it in k.
    k = channel.index(j)   
    if event["value"] != "":
        portInterrupt[k].setValue(True, 1)
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
            portInterrupt[k].setValue(False, 1)    
            
# Function to enable PORT Channel and corresponding clock when any of the pins is using the particular channel.
# Once the PORT channel is enabled, option of corresponding channel interrupt also starts showing up.        
def setupPort(usePortLocal, event): 
    global usePort

    # find the index of the string coming from event["value"] in the list "channel" and save it in k.
    k = channel.index(event["value"])
    
    usePort[k].setValue(True, 1)
    portInterrupt[k].setVisible(True)
    #Enable Peripheral clock for respective PORT Channel in Clock Manager
    Database.setSymbolValue("core", "PMC_ID_PORT" + event["value"], True, 1)
        

###################################################################################################
######################################### PIO Main Menu  ##########################################
###################################################################################################
        
pioMenu = coreComponent.createMenuSymbol(PIO_MENU, None)
pioMenu.setLabel("Ports (PIO)")
pioMenu.setDescription("Configuration for PIO PLIB")

pioEnable = coreComponent.createBooleanSymbol("PIO_ENABLE", pioMenu)
pioEnable.setLabel("Use PIO PLIB?")
pioEnable.setDefaultValue(True)
pioEnable.setReadOnly(True)
    
pioPackage = coreComponent.createComboSymbol("COMPONENT_PACKAGE", pioEnable, Pin.getPackageNames())
pioPackage.setLabel("Pin Package")
pioPackage.setReadOnly(True)
#pioPackage.setDefaultValue("")

###################################################################################################
################################# Pin Configuration related code ##################################
###################################################################################################
    
pinConfiguration = coreComponent.createMenuSymbol(PIO_PIN_CONFIGURATION, pioEnable)
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
    pin[pinNumber-1]= coreComponent.createMenuSymbol("PIO_PIN_CONFIGURATION" + pinNumber - 1, pinConfiguration)
    pin[pinNumber-1].setLabel("Pin " + str(pinNumber))
    pin[pinNumber-1].setDescription("Configuration for Pin " + str(pinNumber) )
    
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
    
    pinBitPosition.append(pinNumber)
    pinBitPosition[pinNumber-1] = coreComponent.createIntegerSymbol("PIN_" + str(pinNumber) + "_PIO_PIN", pin[pinNumber-1])
    pinBitPosition[pinNumber-1].setLabel("Bit Position")
    pinBitPosition[pinNumber-1].setReadOnly(True)
    
    pinChannel.append(pinNumber)
    pinChannel[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_CHANNEL", pin[pinNumber-1])
    pinChannel[pinNumber-1].setLabel("Channel")
    pinChannel[pinNumber-1].setDefaultValue("")
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
    
    pinInterrupt.append(pinNumber)
    # This symbol ID name is split and pin number is extracted and used inside "setupInterrupt" function. so be careful while changing the name of this ID.
    pinInterrupt[pinNumber-1] = coreComponent.createStringSymbol("PIN_" + str(pinNumber) + "_PIO_INTERRUPT", pin[pinNumber-1])
    pinInterrupt[pinNumber-1].setLabel("PIO Interrupt")
    pinInterrupt[pinNumber-1].setReadOnly(True)

    #list created only for dependency
    pinChannelList.append(pinNumber)
    pinChannelList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PIO_CHANNEL"
    
    #list created only for dependency
    pinInterruptList.append(pinNumber)
    pinInterruptList[pinNumber-1] = "PIN_" + str(pinNumber) +"_PIO_INTERRUPT"
    

    
    
###################################################################################################
################################# PORT Configuration related code #################################
###################################################################################################

portConfiguration = coreComponent.createMenuSymbol(PORT_CONFIGURATION, pioEnable)
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
pioSym_PIO_LSR = []
pioSym_PIO_REHLSR = []
pioSym_PIO_FELLSR = []
pioSym_PIO_OER = []
pioSym_PIO_PUER = []
pioSym_PIO_PPDEN = []
pioSym_PIO_MDER = []
pioSym_PIO_SODR = []

peripId = []
global NVICVector
NVICVector = []
global NVICHandler
NVICHandler = []
global NVICHandlerLock
NVICHandlerLock = []
pioSymClkEnComment = []
global pioSymIntEnComment
pioSymIntEnComment = []

 
for portNumber in range(0, len(channel)):

    port.append(portNumber)
    port[portNumber]= coreComponent.createMenuSymbol("PORT_CONFIGURATION" + portNumber, portConfiguration)
    port[portNumber].setLabel("PORT " + channel[portNumber] + " Configuration")

    global usePort
    usePort.append(portNumber)
    usePort[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(channel[portNumber]) + "_USED", port[portNumber])
    usePort[portNumber].setLabel("Use PORT " + channel[portNumber])
    usePort[portNumber].setReadOnly(True)
    
    portInterrupt.append(portNumber)
    portInterrupt[portNumber]= coreComponent.createBooleanSymbol("PIO_" + str(channel[portNumber]) + "_INTERRUPT_USED", usePort[portNumber])
    portInterrupt[portNumber].setLabel("Use Interrupt for PORT " + channel[portNumber])   
    portInterrupt[portNumber].setDefaultValue(False)
    portInterrupt[portNumber].setVisible(False)
    portInterrupt[portNumber].setReadOnly(True)
    
    #list created only for dependency
    portInterruptList.append(portNumber)
    portInterruptList[portNumber] = "PIO_" + str(channel[portNumber]) + "_INTERRUPT_USED"
    
    pioSym_PIO_PER.append(portNumber)
    pioSym_PIO_PER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PER_VALUE", port[portNumber])
    pioSym_PIO_PER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PER")
    pioSym_PIO_PER[portNumber].setDefaultValue("0xFFFFFFFF")
    pioSym_PIO_PER[portNumber].setReadOnly(True)
    
    pioSym_PIO_ABCDSR1.append(portNumber)
    pioSym_PIO_ABCDSR1[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR1_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR1[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR1")
    pioSym_PIO_ABCDSR1[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_ABCDSR1[portNumber].setReadOnly(True)
    
    pioSym_PIO_ABCDSR2.append(portNumber)
    pioSym_PIO_ABCDSR2[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ABCDSR2_VALUE", port[portNumber])
    pioSym_PIO_ABCDSR2[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ABCDSR2")
    pioSym_PIO_ABCDSR2[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_ABCDSR2[portNumber].setReadOnly(True)
    
    pioSym_PIO_OER.append(portNumber)
    pioSym_PIO_OER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_OER_VALUE", port[portNumber])
    pioSym_PIO_OER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_OER")
    pioSym_PIO_OER[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_OER[portNumber].setReadOnly(True)
    
    pioSym_PIO_SODR.append(portNumber)
    pioSym_PIO_SODR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_SODR_VALUE", port[portNumber])
    pioSym_PIO_SODR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_SODR")
    pioSym_PIO_SODR[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_SODR[portNumber].setReadOnly(True)
   
   # IER register is not needed to be configured in PIO_Initialize
   #pioSym_PIO_IER.append(portNumber)
   #pioSym_PIO_IER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_IER_VALUE", port[portNumber])
   #pioSym_PIO_IER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_IER")
   #pioSym_PIO_IER[portNumber].setDefaultValue("0x00000000")
   #pioSym_PIO_IER[portNumber].setReadOnly(True)
    
    pioSym_PIO_AIMER.append(portNumber)
    pioSym_PIO_AIMER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_AIMER_VALUE", port[portNumber])
    pioSym_PIO_AIMER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_AIMER")
    pioSym_PIO_AIMER[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_AIMER[portNumber].setReadOnly(True)
    
    pioSym_PIO_ESR.append(portNumber)
    pioSym_PIO_ESR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_ESR_VALUE", port[portNumber])
    pioSym_PIO_ESR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_ESR")
    pioSym_PIO_ESR[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_ESR[portNumber].setReadOnly(True)
    
    pioSym_PIO_LSR.append(portNumber)
    pioSym_PIO_LSR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_LSR_VALUE", port[portNumber])
    pioSym_PIO_LSR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_LSR")
    pioSym_PIO_LSR[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_LSR[portNumber].setReadOnly(True)
    
    pioSym_PIO_REHLSR.append(portNumber)
    pioSym_PIO_REHLSR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_REHLSR_VALUE", port[portNumber])
    pioSym_PIO_REHLSR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_REHLSR")
    pioSym_PIO_REHLSR[portNumber].setDefaultValue("0x00000000")  
    pioSym_PIO_REHLSR[portNumber].setReadOnly(True)
    
    pioSym_PIO_FELLSR.append(portNumber)
    pioSym_PIO_FELLSR[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_FELLSR_VALUE", port[portNumber])
    pioSym_PIO_FELLSR[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_FELLSR")
    pioSym_PIO_FELLSR[portNumber].setDefaultValue("0x00000000")  
    pioSym_PIO_FELLSR[portNumber].setReadOnly(True)
    
    pioSym_PIO_PUER.append(portNumber)
    pioSym_PIO_PUER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PUER_VALUE", port[portNumber])
    pioSym_PIO_PUER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PUER")
    pioSym_PIO_PUER[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_PUER[portNumber].setReadOnly(True)
    
    pioSym_PIO_PPDEN.append(portNumber)
    pioSym_PIO_PPDEN[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_PPDEN_VALUE", port[portNumber])
    pioSym_PIO_PPDEN[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_PPDEN")
    pioSym_PIO_PPDEN[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_PPDEN[portNumber].setReadOnly(True)
    
    pioSym_PIO_MDER.append(portNumber)
    pioSym_PIO_MDER[portNumber] = coreComponent.createStringSymbol("PIO" + str(channel[portNumber]) + "_MDER_VALUE", port[portNumber])
    pioSym_PIO_MDER[portNumber].setLabel("PIO" + str(channel[portNumber]) + "_MDER")
    pioSym_PIO_MDER[portNumber].setDefaultValue("0x00000000")
    pioSym_PIO_MDER[portNumber].setReadOnly(True)
    
    ##TBD. these are needed to count number of particular channel interrupt. Right now this logic is there in FTL, it can be shifted here.
    ##Symbols created only for internal calculations
    ##number of pins enabled for particular interrupt channel
    #pioSym_NumOfInterrupts.append(portNumber)
    #pioSym_NumOfInterrupts[portNumber] = coreComponent.createIntegerSymbol("NUMBER_OF_CHANNEL" + str(pinNumber) + "INTERRUPTS", portConfiguration)
    #pioSym_NumOfInterrupts[portNumber].setDefaultValue(0)
    #pioSym_NumOfInterrupts[portNumber].setVisible(False)
    
    #symbols and variables for interrupt handling
    peripId.append(portNumber)
    peripId[portNumber] = Interrupt.getInterruptIndex("PORT" + str(channel[portNumber]))
    NVICVector.append(portNumber)
    NVICVector[portNumber] = "NVIC_" + str(peripId[portNumber]) + "_ENABLE"
    NVICHandler.append(portNumber)
    NVICHandler[portNumber] = "NVIC_" + str(peripId[portNumber]) + "_HANDLER"
    NVICHandlerLock.append(portNumber)
    NVICHandlerLock[portNumber] = "NVIC_" + str(peripId[portNumber]) + "_HANDLER_LOCK"
    global InternalNVICVectorChange
    InternalNVICVectorChange.append(portNumber)
    InternalNVICVectorChange[portNumber] = False
    
    # Dependency Status for interrupt   
    pioSymIntEnComment.append(portNumber)
    pioSymIntEnComment[portNumber] = coreComponent.createCommentSymbol("PIO_" + str(channel[portNumber]) + "_NVIC_ENABLE_COMMENT", pioMenu)
    pioSymIntEnComment[portNumber].setVisible(False)
    pioSymIntEnComment[portNumber].setLabel("Warning!!! PORT" + str(channel[portNumber]) + " Interrupt is Disabled in Interrupt Manager")
    pioSymIntEnComment[portNumber].setDependencies(ClockInterruptStatusWarning, ["core." + NVICVector[portNumber]])
    
    # Dependency Status for clock
    pioSymClkEnComment.append(portNumber)
    pioSymClkEnComment[portNumber] = coreComponent.createCommentSymbol("PIO_" + str(channel[portNumber]) + "_CLK_ENABLE_COMMENT", pioMenu)
    pioSymClkEnComment[portNumber].setVisible(False)
    pioSymClkEnComment[portNumber].setLabel("Warning!!! PORT" + str(channel[portNumber]) + " Peripheral Clock is Disabled in Clock Manager")
    pioSymClkEnComment[portNumber].setDependencies(ClockInterruptStatusWarning, ["core.PMC_ID_PORT" + str(channel[portNumber])])
    
  
# NVIC Dynamic settings
pioNVICControl = coreComponent.createBooleanSymbol("NVIC_PIO_ENABLE", None)
pioNVICControl.setDependencies(NVICControl, portInterruptList)
pioNVICControl.setVisible(False)

# Call "setupPort" function to update status of port channel and its clock whenever there is any change in any of the pin status
# index for "usePort[]" is used as 0 because it is irrelevent here. either of the values 0,1,2,3.. can be used here.    
usePort[0].setDependencies(setupPort, pinChannelList)
    

# Call "setupInterrupt" function to update status of port channel interrupt whenever there is any change in any of the pin interrupt enable/disable status
# index for "portInterrupt[]" is used as 0 because it is irrelevent here. either of the values 0,1,2,3.. can be used here. 
portInterrupt[0].setDependencies(setupInterrupt, pinInterruptList)
    
pioSym_AFEC0_CHER = coreComponent.createStringSymbol("PIO_AFEC0_CHER_VALUE", portConfiguration)
pioSym_AFEC0_CHER.setLabel("AFEC0_CHER")
pioSym_AFEC0_CHER.setDefaultValue("0x00000000")
pioSym_AFEC0_CHER.setReadOnly(True)

pioSym_AFEC1_CHER = coreComponent.createStringSymbol("PIO_AFEC1_CHER_VALUE", portConfiguration)
pioSym_AFEC1_CHER.setLabel("AFEC1_CHER")
pioSym_AFEC1_CHER.setDefaultValue("0x00000000")
pioSym_AFEC1_CHER.setReadOnly(True)

pioSym_DACC_CHER = coreComponent.createStringSymbol("PIO_DACC_CHER_VALUE", portConfiguration)
pioSym_DACC_CHER.setLabel("DACC_CHER")
pioSym_DACC_CHER.setDefaultValue("0x00000000")
pioSym_DACC_CHER.setReadOnly(True)

pioMatrixSym_CCFG_SYSIO = coreComponent.createStringSymbol("PIO_CCFG_SYSIO_VALUE", portConfiguration)
pioMatrixSym_CCFG_SYSIO.setLabel("CCFG_SYSIO")
pioMatrixSym_CCFG_SYSIO.setDescription("System Pins as GPIO")
pioMatrixSym_CCFG_SYSIO.setDefaultValue("0x00000000")
pioMatrixSym_CCFG_SYSIO.setReadOnly(True)


###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")
    
pioHeader1File = coreComponent.createFileSymbol(PIO_HEADER, None)
pioHeader1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.h.ftl")
pioHeader1File.setOutputName("plib_pio.h")
pioHeader1File.setDestPath("/peripheral/pio/")
pioHeader1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioHeader1File.setType("HEADER")
pioHeader1File.setMarkup(True)

pioSource1File = coreComponent.createFileSymbol(PIO_SOURCE, None)
pioSource1File.setSourcePath("../peripheral/pio_11004/templates/plib_pio.c.ftl")
pioSource1File.setOutputName("plib_pio.c")
pioSource1File.setDestPath("/peripheral/pio/")
pioSource1File.setProjectPath("config/" + configName +"/peripheral/pio/")
pioSource1File.setType("SOURCE")
pioSource1File.setMarkup(True)


pioSystemInitFile = coreComponent.createFileSymbol(PIO_INIT, None)
pioSystemInitFile.setType("STRING")
pioSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
pioSystemInitFile.setSourcePath("../peripheral/pio_11004/templates/system/system_initialize.c.ftl")
pioSystemInitFile.setMarkup(True)

pioSystemDefFile = coreComponent.createFileSymbol(PIO_DEF, None)
pioSystemDefFile.setType("STRING")
pioSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pioSystemDefFile.setSourcePath("../peripheral/pio_11004/templates/system/system_definitions.h.ftl")
pioSystemDefFile.setMarkup(True)

