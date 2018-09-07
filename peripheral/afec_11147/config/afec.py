###################################################################################################
########################### Global variables   #################################
###################################################################################################

global num

afecSym_SEQ1R_USCH = []
afecCHMenu = []
afecSym_CH_CHER = []
afecSym_CH_NAME = []
afecSym_CH_PositiveInput = []
afecSym_CH_NegativeInput = []
afecSym_CH_SHMR_DUAL = []
afecSym_CH_DUAL_CHANNEL = []
afecSym_CH_CGR_GAIN = []
afecSym_CH_COCR_AOFF = []
afecSym_CH_IER_EOC = []

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################

def afecClockControl(symbol, event):
    clockSet = False
    Database.clearSymbolValue("core", "AFEC" + str(num)+"_CLOCK_ENABLE")
    for channelID in range(0, 12):
        if (afecSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True):
        Database.setSymbolValue("core", "AFEC" + str(num)+"_CLOCK_ENABLE", True, 2)
    else:
        Database.setSymbolValue("core", "AFEC" + str(num)+"_CLOCK_ENABLE", False, 2)

def afecinterruptControl(symbol, event):
    nvicSet = False
    interruptVector = "AFEC" + str(num) + "_INTERRUPT_ENABLE"
    interruptHandler = "AFEC" + str(num) + "_INTERRUPT_HANDLER"
    interruptHandlerLock = "AFEC" + str(num) + "_INTERRUPT_HANDLER_LOCK"
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    for channelID in range(0, 12):
        if (afecSym_CH_IER_EOC[channelID].getValue() == True):
            nvicSet = True
    if(nvicSet == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, "AFEC"+str(num)+"_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "AFEC"+str(num)+"_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyClockStatus(symbol, event):
    clockSet = False
    clock = bool(Database.getSymbolValue("core", "AFEC" + str(num)+"_CLOCK_ENABLE"))
    for channelID in range(0, 12):
        if (afecSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True and clock == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def dependencyIntStatus(symbol, event):
    nvicSet = False
    interruptVectorUpdate = "AFEC" + str(num) + "_INTERRUPT_ENABLE_UPDATE"
    nvic = bool(Database.getSymbolValue("core", interruptVectorUpdate))
    for channelID in range(0, 12):
        if (afecSym_CH_IER_EOC[channelID].getValue() == True):
            nvicSet = True
    if(nvicSet == True and nvic == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def afecGetMasterClock():
    main_clk_freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))
    return main_clk_freq

def afecPrescalWarning(symbol, event):
    clock = afecGetMasterClock()
    prescaler = afecSym_MR_PRESCAL.getValue() + 1
    afecFreq = clock / prescaler
    if (afecFreq < 4000000):
        symbol.setLabel("AFEC Frequency < 4,000,000 Hz. Decrease prescaler value. ")
        symbol.setVisible(True)
    elif (afecFreq > 40000000):
        symbol.setLabel("AFEC Frequency > 40,000,000 Hz. Increase prescaler value. ")
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def afecFreqCalc(symbol, event):
    clock = afecGetMasterClock()
    prescaler = afecSym_MR_PRESCAL.getValue() + 1
    afecFreq = clock / prescaler
    symbol.clearValue()
    symbol.setValue(afecFreq, 2)

def afecCalcConversionTime(afecSym_CONV_TIME, event):
    clock = afecGetMasterClock()
    if (clock == 0):
        Log.writeErrorMessage("Master clock frequency is zero")
        clock = 1
    prescaler = afecSym_MR_PRESCAL.getValue() + 1
    result_resolution = afecSym_EMR_RES_VALUE.getSelectedKey()
    multiplier = 1
    if (result_resolution == "NO_AVERAGE"):
        multiplier = 1
    if (result_resolution == "OSR4"):
        multiplier = 4
    if (result_resolution == "OSR16"):
        multiplier = 16
    if (result_resolution == "OSR64"):
        multiplier = 64
    if (result_resolution == "OSR256"):
        multiplier = 256
    conv_time = (prescaler * 23.0 * 1000000.0 * multiplier) / clock
    afecSym_CONV_TIME.setLabel("**** Conversion Time is "+str(conv_time)+" us ****")

def afecUserSeqVisible(afecSym_SEQ1R_USCHLocal, event):
    for channelID in range(0, 12):
        if (event["value"] == True):
            afecSym_SEQ1R_USCH[channelID].setVisible(True)
        else:
            afecSym_SEQ1R_USCH[channelID].setVisible(False)

def afecCHNameVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_NAME[channelID].setVisible(True)
    else:
        afecSym_CH_NAME[channelID].setVisible(False)

def afecCHPosInpVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_PositiveInput[channelID].setVisible(True)
    else:
        afecSym_CH_PositiveInput[channelID].setVisible(False)

def afecCHNegInpVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_NegativeInput[channelID].setVisible(True)
    else:
        afecSym_CH_NegativeInput[channelID].setVisible(False)

def afecCHDualVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_SHMR_DUAL[channelID].setVisible(True)
    else:
        afecSym_CH_SHMR_DUAL[channelID].setVisible(False)

def afecCHDualCommentVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_DUAL_CHANNEL[channelID].setVisible(True)
    else:
        afecSym_CH_DUAL_CHANNEL[channelID].setVisible(False)

def afecCHGainVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_CGR_GAIN[channelID].setVisible(True)
    else:
        afecSym_CH_CGR_GAIN[channelID].setVisible(False)

def afecCHOffsetVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_COCR_AOFF[channelID].setVisible(True)
    else:
        afecSym_CH_COCR_AOFF[channelID].setVisible(False)

def afecCHInterruptVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])
    if (event["value"] == True):
        afecSym_CH_IER_EOC[channelID].setVisible(True)
    else:
        afecSym_CH_IER_EOC[channelID].setVisible(False)

def afecCHEnable(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    #for dual mode, enable corresponding channel pair
    if(event["id"].find("_SHMR_DUAL") > 0):
        if(event["value"] == True):
            afecSym_CH_CHER[channelID].clearValue()
            afecSym_CH_CHER[channelID].setValue(True, 1)
        else:
            afecSym_CH_CHER[channelID].clearValue()
            afecSym_CH_CHER[channelID].setValue(False, 1)

    #for diff mode, hide next odd channel
    if(event["id"].find("_NEG_INP") > 0):
        if(event["value"] == "AN"+str(channelID)):
            afecCHMenu[channelID].setVisible(False)
        else:
            afecCHMenu[channelID].setVisible(True)

def afecTriggerVisible(symbol, event):
    symObj = event["symbol"]
    if(symObj.getSelectedKey() == "HW_TRIGGER"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(afecComponent):
    global num
    num = afecComponent.getID()[-1:]
    Log.writeInfoMessage("Running AFEC" + str(num))

    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = ["False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False"] #array to save available channels
    afecChannelsValues = [] #array used for combo symbol
    afecChannelsValues.append("NONE")

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(packageName)+"\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    afec_signals = []
    afec = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]/instance@[name=\"AFEC"+str(num)+"\"]/signals")
    afec_signals = afec.getChildren()
    for pad in range(0, len(afec_signals)):
        group = afec_signals[pad].getAttribute("group")
        if (("AD" in group) and ("index" in afec_signals[pad].getAttributeList())):
            padSignal = afec_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(afec_signals[pad].getAttribute("index"))] = "True"
                afecChannelsValues.append("CH"+afec_signals[pad].getAttribute("index"))

    afecSym_AvailableChannels = afecComponent.createComboSymbol("AFEC_AVAILABLE_CHANNELS", None, channel)
    afecSym_AvailableChannels.setVisible(False)

    # Clock dynamic settings
    afecSym_ClockControl = afecComponent.createBooleanSymbol("AFEC" + str(num)+"_CLOCK_ENABLE", None)
    afecSym_ClockControl.setDependencies(afecClockControl, ["AFEC_0_CHER", "AFEC_1_CHER", "AFEC_2_CHER", "AFEC_3_CHER", "AFEC_4_CHER", \
    "AFEC_5_CHER", "AFEC_6_CHER", "AFEC_7_CHER", "AFEC_8_CHER", "AFEC_9_CHER", "AFEC_10_CHER", "AFEC_11_CHER"])
    afecSym_ClockControl.setVisible(False)

    # NVIC Dynamic settings
    afecSym_interruptControl = afecComponent.createBooleanSymbol("AFEC_NVIC_ENABLE", None)
    afecSym_interruptControl.setDependencies(afecinterruptControl, ["AFEC_0_IER_EOC", "AFEC_1_IER_EOC", "AFEC_2_IER_EOC", "AFEC_3_IER_EOC", "AFEC_4_IER_EOC",\
    "AFEC_5_IER_EOC", "AFEC_6_IER_EOC", "AFEC_7_IER_EOC", "AFEC_8_IER_EOC", "AFEC_9_IER_EOC", "AFEC_10_IER_EOC", "AFEC_11_IER_EOC"])
    afecSym_interruptControl.setVisible(False)

    # Dependency Status
    afecSym_ClkEnComment = afecComponent.createCommentSymbol("AFEC_CLK_ENABLE_COMMENT", None)
    afecSym_ClkEnComment.setVisible(False)
    afecSym_ClkEnComment.setLabel("Warning!!! AFEC" +str(num)+" Peripheral Clock is Disabled in Clock Manager")
    afecSym_ClkEnComment.setDependencies(dependencyClockStatus, ["core.AFEC" + str(num)+ "_CLOCK_ENABLE", "AFEC_0_CHER", "AFEC_1_CHER", "AFEC_2_CHER", "AFEC_3_CHER", "AFEC_4_CHER", \
    "AFEC_5_CHER", "AFEC_6_CHER", "AFEC_7_CHER", "AFEC_8_CHER", "AFEC_9_CHER", "AFEC_10_CHER", "AFEC_11_CHER"])

    interruptVectorUpdate = "AFEC" + str(num) + "_INTERRUPT_ENABLE_UPDATE"

    afecSym_IntEnComment = afecComponent.createCommentSymbol("AFEC_NVIC_ENABLE_COMMENT", None)
    afecSym_IntEnComment.setVisible(False)
    afecSym_IntEnComment.setLabel("Warning!!! AFEC" +str(num)+" Interrupt is Disabled in Interrupt Manager")
    afecSym_IntEnComment.setDependencies(dependencyIntStatus, ["core." + interruptVectorUpdate, "AFEC_0_IER_EOC", "AFEC_1_IER_EOC", "AFEC_2_IER_EOC", "AFEC_3_IER_EOC", "AFEC_4_IER_EOC",\
    "AFEC_5_IER_EOC", "AFEC_6_IER_EOC", "AFEC_7_IER_EOC", "AFEC_8_IER_EOC", "AFEC_9_IER_EOC", "AFEC_10_IER_EOC", "AFEC_11_IER_EOC"])

    afecMenu = afecComponent.createMenuSymbol("AFEC_MENU", None)
    afecMenu.setLabel("ADC Configuration")

    #max no of channels
    afecSym_NUM_CHANNELS = afecComponent.createIntegerSymbol("AFEC_NUM_CHANNELS", afecMenu)
    afecSym_NUM_CHANNELS.setDefaultValue(12)
    afecSym_NUM_CHANNELS.setVisible(False)

    #Clock prescaler
    global afecSym_MR_PRESCAL
    afecSym_MR_PRESCAL = afecComponent.createIntegerSymbol("AFEC_MR_PRESCAL", afecMenu)
    afecSym_MR_PRESCAL.setLabel("Select Prescaler")
    afecSym_MR_PRESCAL.setDefaultValue(7)
    afecSym_MR_PRESCAL.setMin(1)
    afecSym_MR_PRESCAL.setMax(255)

    #clock selection
    global afecSym_Clock
    afecSym_Clock = afecComponent.createIntegerSymbol("AFEC_CLK", afecMenu)
    afecSym_Clock.setLabel("Clock Frequency (Hz)")
    afecSym_Clock.setDefaultValue(18750000)
    afecSym_Clock.setVisible(True)
    afecSym_Clock.setReadOnly(True)
    afecSym_Clock.setDependencies(afecFreqCalc, ["AFEC_MR_PRESCAL", "core.MASTER_CLOCK_FREQUENCY"])

    afecSym_PRESCAL_WARNING = afecComponent.createCommentSymbol("AFEC_PRESCAL_WARNING", afecMenu)
    afecSym_PRESCAL_WARNING.setLabel("**** AFEC Frequency = 18750000 Hz. ****")
    afecSym_PRESCAL_WARNING.setVisible(False)
    afecSym_PRESCAL_WARNING.setDependencies(afecPrescalWarning, ["AFEC_MR_PRESCAL", "core.MASTER_CLOCK_FREQUENCY"])

    #Result resolution
    #Added keys here as combining two bit-fields EMR_STM and EMR_RES
    global afecSym_EMR_RES_VALUE
    afecSym_EMR_RES_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_RES_VALUE", afecMenu)
    afecSym_EMR_RES_VALUE.setLabel("Result Resolution")
    afecSym_EMR_RES_VALUE.setDefaultValue(0)
    afecSym_EMR_RES_VALUE.setOutputMode("Value")
    afecSym_EMR_RES_VALUE.setDisplayMode("Description")
    afecSym_EMR_RES_VALUE.addKey("NO_AVERAGE", "0", "12-bit")
    afecSym_EMR_RES_VALUE.addKey("OSR4", "1", "13-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR4", "2", "13-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR16", "3", "14-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR16", "4", "14-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR64", "5", "15-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR64", "6", "15-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR256", "7", "16-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR256", "8", "16-bit - multi trigger averaging")

    #Conversion time
    afecSym_CONV_TIME = afecComponent.createCommentSymbol("AFEC_CONV_TIME", afecMenu)
    afecSym_CONV_TIME.setLabel("**** Conversion Time is 1.0733 us ****")
    afecSym_CONV_TIME.setDependencies(afecCalcConversionTime, ["AFEC_MR_PRESCAL", "AFEC_EMR_RES_VALUE", "core.MASTER_CLOCK_FREQUENCY"])

    #Result sign
    afecSym_EMR_SIGNMODE_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_SIGNMODE_VALUE", afecMenu)
    afecSym_EMR_SIGNMODE_VALUE.setLabel("Result Sign")
    afecSym_EMR_SIGNMODE_VALUE.setDefaultValue(0)
    afecSym_EMR_SIGNMODE_VALUE.setOutputMode("Key")
    afecSym_EMR_SIGNMODE_VALUE.setDisplayMode("Description")
    afecSym_EMR_SIGNMODE_VALUE.addKey("SE_UNSG_DF_SIGN", "0", "Single Ended: Unsigned, Differential: Signed")
    afecSym_EMR_SIGNMODE_VALUE.addKey("SE_SIGN_DF_UNSG", "1", "Single Ended: Signed, Differential: Unsigned")
    afecSym_EMR_SIGNMODE_VALUE.addKey("ALL_UNSIGNED", "2", "Single Ended: Unsigned, Differential: Unsigned")
    afecSym_EMR_SIGNMODE_VALUE.addKey("ALL_SIGNED", "3", "Single Ended: Signed, Differential: Signed")

    afecSym_CONV_MODE = afecComponent.createKeyValueSetSymbol("AFEC_CONV_MODE", afecMenu)
    afecSym_CONV_MODE.setLabel("Conversion Mode")
    afecSym_CONV_MODE.setDefaultValue(0)
    afecSym_CONV_MODE.setOutputMode("Value")
    afecSym_CONV_MODE.setDisplayMode("Description")
    afecSym_CONV_MODE.addKey("FREERUN", "0", "Free Run")
    afecSym_CONV_MODE.addKey("SW_TRIGGER", "1", "Software Trigger")
    afecSym_CONV_MODE.addKey("HW_TRIGGER", "2", "Hardware Trigger")

    #Trigger
    afecSym_MR_TRGSEL_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_MR_TRGSEL_VALUE", afecSym_CONV_MODE)
    afecSym_MR_TRGSEL_VALUE.setLabel("Select External Trigger Input")
    afecSym_MR_TRGSEL_VALUE.setVisible(False)
    afecSym_MR_TRGSEL_VALUE.setDefaultValue(1)
    afecSym_MR_TRGSEL_VALUE.setOutputMode("Key")
    afecSym_MR_TRGSEL_VALUE.setDisplayMode("Description")
    trigger_values = []
    afec = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]/instance@[name=\"AFEC"+str(num)+"\"]/parameters")
    trigger_values = afec.getChildren()
    for param in range(0, len(trigger_values)):
        if "TRGSEL" in trigger_values[param].getAttribute("name"):
            afecSym_MR_TRGSEL_VALUE.addKey(trigger_values[param].getAttribute("name"), trigger_values[param].getAttribute("value"), trigger_values[param].getAttribute("caption"))
    afecSym_MR_TRGSEL_VALUE.setDependencies(afecTriggerVisible, ["AFEC_CONV_MODE"])
    #------------------------------------------------------------------------------------
    #user sequence menu
    afecUserSeq = afecComponent.createMenuSymbol("AFEC_USER_SEQ", None)
    afecUserSeq.setLabel("User Channel Sequence Configuration")

    #user sequence comment
    afecSym_USEQ_COMMENT = afecComponent.createCommentSymbol("AFEC_USEQ_COMMENT", afecUserSeq)
    afecSym_USEQ_COMMENT.setLabel("**** Configure selected channels in the Channel Configuration Menu ****")

    #enable user sequence
    afecSym_MR_USEQ = afecComponent.createBooleanSymbol("AFEC_MR_USEQ", afecUserSeq)
    afecSym_MR_USEQ.setLabel("Enable User Sequence Mode")
    afecSym_MR_USEQ.setDefaultValue(False)

    for channelID in range(0, len(channel)):
        #channel selection for user sequence
        afecSym_SEQ1R_USCH.append(channelID)
        afecSym_SEQ1R_USCH[channelID] = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH"+str(channelID), afecSym_MR_USEQ, afecChannelsValues)
        afecSym_SEQ1R_USCH[channelID].setLabel("Select Channel for Sequence Number " + str(channelID))
        afecSym_SEQ1R_USCH[channelID].setDefaultValue(afecChannelsValues[0])
        afecSym_SEQ1R_USCH[channelID].setVisible(False)
        afecSym_SEQ1R_USCH[channelID].setDependencies(afecUserSeqVisible, ["AFEC_MR_USEQ"])
    #--------------------------------------------------------------------------------------

    afecCHConfMenu = afecComponent.createMenuSymbol("AFEC_CH_CONF", None)
    afecCHConfMenu.setLabel("Channel Configuration")

    # Loop runs for 12 channels and visibility of the channel is controlled as per available pins
    for channelID in range(0, len(channel)):
        #Channel menu
        global afecCHMenu
        afecCHMenu.append(channelID)
        afecCHMenu[channelID] = afecComponent.createMenuSymbol("CH"+str(channelID), afecCHConfMenu)
        afecCHMenu[channelID].setLabel("Channel "+str(channelID))
        #Show channels as per available pins in package
        if (channel[channelID] == "False"):
            afecCHMenu[channelID].setVisible(False)

        #Channel enable
        afecSym_CH_CHER.append(channelID)
        afecSym_CH_CHER[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_CHER", afecCHMenu[channelID])
        afecSym_CH_CHER[channelID].setLabel("Enable Channel " + str(channelID))
        afecSym_CH_CHER[channelID].setDefaultValue(False)
        #enable corresponding channel pair of dual mode
        #e.g. for dual mode, CH0 and CH6
        #for diff mode, CH0 and CH1
        if((channelID > ((len(channel) - 1) / 2))):
            if (channelID % 2 == 1):
                afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-6)+"_SHMR_DUAL", "AFEC_"+str(channelID-1)+"_NEG_INP"])
            else:
                afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-6)+"_SHMR_DUAL"])
        elif (channelID % 2 == 1):
            afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-1)+"_NEG_INP"])

        #Channel name
        afecSym_CH_NAME.append(channelID)
        afecSym_CH_NAME[channelID] = afecComponent.createStringSymbol("AFEC_"+str(channelID)+"_NAME", afecSym_CH_CHER[channelID])
        afecSym_CH_NAME[channelID].setLabel("Name")
        afecSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
        afecSym_CH_NAME[channelID].setVisible(False)
        afecSym_CH_NAME[channelID].setDependencies(afecCHNameVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel positive input
        afecSym_CH_PositiveInput.append(channelID)
        afecSym_CH_PositiveInput[channelID] = afecComponent.createStringSymbol("AFEC_"+str(channelID)+"_POS_INP", afecSym_CH_CHER[channelID])
        afecSym_CH_PositiveInput[channelID].setLabel("Positive Input")
        afecSym_CH_PositiveInput[channelID].setDefaultValue("AN"+str(channelID))
        afecSym_CH_PositiveInput[channelID].setReadOnly(True)
        afecSym_CH_PositiveInput[channelID].setVisible(False)
        afecSym_CH_PositiveInput[channelID].setDependencies(afecCHPosInpVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel negative input
        afecSym_CH_NegativeInput.append(channelID)
        afec_EvenChNegInput = ["GND", "AN"+str(channelID+1)]
        afec_OddChNegInput = ["GND"]
        if (channelID % 2 == 1):
            afecSym_CH_NegativeInput[channelID] = afecComponent.createComboSymbol("AFEC_"+str(channelID)+"_NEG_INP", afecSym_CH_CHER[channelID], afec_OddChNegInput)
            afecSym_CH_NegativeInput[channelID].setReadOnly(True)
        else:
            afecSym_CH_NegativeInput[channelID] = afecComponent.createComboSymbol("AFEC_"+str(channelID)+"_NEG_INP", afecSym_CH_CHER[channelID], afec_EvenChNegInput)
            if (channel[channelID + 1] == "False"):
                afecSym_CH_NegativeInput[channelID].setReadOnly(True)
        afecSym_CH_NegativeInput[channelID].setLabel("Negative Input")
        afecSym_CH_NegativeInput[channelID].setDefaultValue("GND")
        afecSym_CH_NegativeInput[channelID].setVisible(False)
        afecSym_CH_NegativeInput[channelID].setDependencies(afecCHNegInpVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Dual mode
        afecSym_CH_SHMR_DUAL.append(channelID)
        if(channelID < len(channel)/2):
            afecSym_CH_SHMR_DUAL[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_SHMR_DUAL", afecSym_CH_CHER[channelID])
            afecSym_CH_SHMR_DUAL[channelID].setLabel("Dual Sample and Hold")
            afecSym_CH_SHMR_DUAL[channelID].setDefaultValue(False)
            afecSym_CH_SHMR_DUAL[channelID].setVisible(False)
            afecSym_CH_SHMR_DUAL[channelID].setDependencies(afecCHDualVisible, ["AFEC_"+str(channelID)+"_CHER"])

        afecSym_CH_DUAL_CHANNEL.append(channelID)
        if(channelID < len(channel)/2):
            afecSym_CH_DUAL_CHANNEL[channelID] = afecComponent.createCommentSymbol("AFEC_"+str(channelID)+"_DUAL_CHANNEL", afecSym_CH_CHER[channelID])
            afecSym_CH_DUAL_CHANNEL[channelID].setLabel("**** Channel "+str(channelID + 6)+" is sampled along with Channel "+str(channelID)+ ". Configure CHANNEL "+str(channelID + 6) + " ****")
            afecSym_CH_DUAL_CHANNEL[channelID].setVisible(False)
            afecSym_CH_DUAL_CHANNEL[channelID].setDependencies(afecCHDualCommentVisible, ["AFEC_"+str(channelID)+"_SHMR_DUAL"])

        #Channel gain
        afecGainValues = ["X1", "X2", "X4"]
        afecSym_CH_CGR_GAIN.append(channelID)
        afecSym_CH_CGR_GAIN[channelID] = afecComponent.createComboSymbol("AFEC_"+str(channelID)+"_CGR_GAIN", afecSym_CH_CHER[channelID], afecGainValues)
        afecSym_CH_CGR_GAIN[channelID].setLabel("Gain")
        afecSym_CH_CGR_GAIN[channelID].setDefaultValue("X1")
        afecSym_CH_CGR_GAIN[channelID].setVisible(False)
        afecSym_CH_CGR_GAIN[channelID].setDependencies(afecCHGainVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel offset
        afecSym_CH_COCR_AOFF.append(channelID)
        afecSym_CH_COCR_AOFF[channelID] = afecComponent.createIntegerSymbol("AFEC_"+str(channelID)+"_COCR_AOFF", afecSym_CH_CHER[channelID])
        afecSym_CH_COCR_AOFF[channelID].setLabel("Offset")
        afecSym_CH_COCR_AOFF[channelID].setDefaultValue(512)
        afecSym_CH_COCR_AOFF[channelID].setVisible(False)
        afecSym_CH_COCR_AOFF[channelID].setMin(0)
        afecSym_CH_COCR_AOFF[channelID].setMax(1024)
        afecSym_CH_COCR_AOFF[channelID].setDependencies(afecCHOffsetVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel interrupt
        afecSym_CH_IER_EOC.append(channelID)
        afecSym_CH_IER_EOC[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_IER_EOC", afecSym_CH_CHER[channelID])
        afecSym_CH_IER_EOC[channelID].setLabel("End of conversion interrupt")
        afecSym_CH_IER_EOC[channelID].setDefaultValue(False)
        afecSym_CH_IER_EOC[channelID].setVisible(False)
        afecSym_CH_IER_EOC[channelID].setDependencies(afecCHInterruptVisible, ["AFEC_"+str(channelID)+"_CHER"])

    #--------------------------------------------------------------------------------------
    afecIndex = afecComponent.createIntegerSymbol("INDEX", afecMenu)
    afecIndex.setVisible(False)
    afecIndex.setDefaultValue(int(num))

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    afec = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AFEC\"]")
    afecID = afec.getAttribute("id")

    afecHeaderFile = afecComponent.createFileSymbol("AFEC_HEADER", None)
    afecHeaderFile.setSourcePath("../peripheral/afec_"+str(afecID)+"/templates/plib_afec.h.ftl")
    afecHeaderFile.setOutputName("plib_afec" + str(num) + ".h")
    afecHeaderFile.setDestPath("peripheral/afec/")
    afecHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecHeaderFile.setType("HEADER")
    afecHeaderFile.setMarkup(True)

    afecGlobalHeaderFile = afecComponent.createFileSymbol("AFEC_GLOBALHEADER", None)
    afecGlobalHeaderFile.setSourcePath("../peripheral/afec_"+str(afecID) + "/plib_afec.h")
    afecGlobalHeaderFile.setOutputName("plib_afec.h")
    afecGlobalHeaderFile.setDestPath("peripheral/afec/")
    afecGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecGlobalHeaderFile.setType("HEADER")

    afecSource1File = afecComponent.createFileSymbol("AFEC_SOURCE", None)
    afecSource1File.setSourcePath("../peripheral/afec_"+str(afecID)+"/templates/plib_afec.c.ftl")
    afecSource1File.setOutputName("plib_afec" + str(num) + ".c")
    afecSource1File.setDestPath("peripheral/afec/")
    afecSource1File.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecSource1File.setType("SOURCE")
    afecSource1File.setMarkup(True)

    afecSystemInitFile = afecComponent.createFileSymbol("AFEC_INIT", None)
    afecSystemInitFile.setType("STRING")
    afecSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    afecSystemInitFile.setSourcePath("../peripheral/afec_"+str(afecID)+"/templates/system/system_initialize.c.ftl")
    afecSystemInitFile.setMarkup(True)

    afecSystemDefFile = afecComponent.createFileSymbol("AFEC_DEF", None)
    afecSystemDefFile.setType("STRING")
    afecSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    afecSystemDefFile.setSourcePath("../peripheral/afec_"+str(afecID)+"/templates/system/system_definitions.h.ftl")
    afecSystemDefFile.setMarkup(True)
