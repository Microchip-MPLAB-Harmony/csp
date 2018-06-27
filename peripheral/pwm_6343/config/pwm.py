###################################################################################################
########################### Global variables   #################################
###################################################################################################

global pwmNum
pwmChannelMenu = []
pwmSym_CH_Enable = []
pwmSym_CH_SyncEnable = []
pwmSym_CH_Sync_Comment = []
pwmSym_PWM_CMR_CPRE = []
pwmSym_CH_Prescaler_Comment = []
pwmSym_PWM_CMR_CALG = []
pwmSym_PWM_CMR_CPOL = []
pwmSym_PWM_CPRD = []
pwmSym_PWM_FreqComment = []
pwmSym_PWM_CDTY = []
pwmSym_PWM_CMR_DTE = []
pwmSym_PWM_DT_DTL = []
pwmSym_PWM_DT_DTH = []
pwmSym_PWM_Fault_Enable = []
pwmSym_PWM_FPE = []
pwmSym_PWM_CMR_UPDS = []
pwmSym_PWM_CMR_CES = []
pwmSym_PWM_IER1_CHID = []

pwmSym_PWM_CMPM_CEN = []
pwmSym_PWM_ELMR0_CSEL = []
pwmSym_PWM_ELMR1_CSEL = []
pwmSym_PWM_CMPV_CV = []
pwmSym_PWM_CMPV_CVM = []
pwmSym_PWM_CMPM_CTR = []
pwmSym_PWM_CMPM_CPR = []
pwmSym_PWM_CMPM_CUPR = []

pwmFaultIndexMenu = []
pwmSym_PWM_FMR_FPOL = []
pwmSym_PWM_FMR_FMOD = []
pwmSym_PWM_FPV_FPVH = []
pwmSym_PWM_FPV_FPVL = []

global pwmPeriphId
global pwmNVICVector
global pwmNVICHandler
global pwmNVICHandlerLock

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################
#channel number is extracted as 2nd character in ID. like PWM0_xxx, PWM1_xxx

def pwmNVICControl(symbol, event):
    Database.clearSymbolValue("core", pwmNVICVector)
    Database.clearSymbolValue("core", pwmNVICHandler)
    Database.clearSymbolValue("core", pwmNVICHandlerLock)
    nvicEnable = False
    for channelID in range(0, 4):
        if (pwmSym_PWM_IER1_CHID[channelID].getValue() == True):
            nvicEnable = True

    if(nvicEnable == True):
        Database.setSymbolValue("core", pwmNVICVector, True, 2)
        Database.setSymbolValue("core", pwmNVICHandler, "PWM" + str(pwmNum) + "_InterruptHandler", 2)
        Database.setSymbolValue("core", pwmNVICHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", pwmNVICVector, False, 2)
        Database.setSymbolValue("core", pwmNVICHandler, "PWM" + str(pwmNum) + "_Handler", 2)
        Database.setSymbolValue("core", pwmNVICHandlerLock, False, 2)

def pwmClockControl(symbol, event):
    clockEnable = False
    for channelID in range(0, 4):
        if (pwmSym_CH_Enable[channelID].getValue() == True):
            clockEnable = True

    if (clockEnable == True):
        Database.setSymbolValue("core", "PMC_ID_PWM" + str(pwmNum), True, 2)
    else :
        Database.setSymbolValue("core", "PMC_ID_PWM" + str(pwmNum), False, 2)

def pwmClkDependencyStatus(symbol, event):
    clock = bool(Database.getSymbolValue("core", "PMC_ID_PWM" + str(pwmNum)))
    if ((clock == False) and (pwmSym_CH_Enable[0].getValue() == True or pwmSym_CH_Enable[1].getValue() == True or pwmSym_CH_Enable[2].getValue() == True or pwmSym_CH_Enable[3].getValue() == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmNVICDependencyStatus(symbol, event):
    nvic = bool(Database.getSymbolValue("core", pwmNVICVector))

    if(pwmSym_CH_Enable[0].getValue() == True or pwmSym_CH_Enable[1].getValue() == True or pwmSym_CH_Enable[2].getValue() == True or pwmSym_CH_Enable[3].getValue() == True):
        if ((nvic == False) and (pwmSym_PWM_IER1_CHID[0].getValue() == True or pwmSym_PWM_IER1_CHID[1].getValue() == True or pwmSym_PWM_IER1_CHID[2].getValue() == True or pwmSym_PWM_IER1_CHID[3].getValue() == True)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def pwmAlignmentVisible(symbol, event):
    if (event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmGetMasterClock():
    main_clk_freq = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))
    return main_clk_freq

def pwmGetInternalClk(channelClock, divider):
    clock_Hz = 0.0
    masterClock_Hz = pwmGetMasterClock()
    if (channelClock == "CLK"):
        clock_Hz = masterClock_Hz/float(divider)
    if (channelClock == "CLK_DIV2"):
        clock_Hz = masterClock_Hz/2.0/float(divider)
    if (channelClock == "CLK_DIV4"):
        clock_Hz = masterClock_Hz/4.0/float(divider)
    if (channelClock == "CLK_DIV8"):
        clock_Hz = masterClock_Hz/8.0/float(divider)
    if (channelClock == "CLK_DIV16"):
        clock_Hz = masterClock_Hz/16.0/float(divider)
    if (channelClock == "CLK_DIV32"):
        clock_Hz = masterClock_Hz/32.0/float(divider)
    if (channelClock == "CLK_DIV64"):
        clock_Hz = masterClock_Hz/64.0/float(divider)
    if (channelClock == "CLK_DIV128"):
        clock_Hz = masterClock_Hz/128.0/float(divider)
    if (channelClock == "CLK_DIV256"):
        clock_Hz = masterClock_Hz/256.0/float(divider)
    if (channelClock == "CLK_DIV512"):
        clock_Hz = masterClock_Hz/512.0/float(divider)
    if (channelClock == "CLK_DIV1024"):
        clock_Hz = masterClock_Hz/1024.0/float(divider)
    return clock_Hz

def pwmCalcFreq(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[2])
    global pwmSym_PWM_CLK_PREA
    global pwmSym_PWM_CLK_PREB
    global pwmSym_PWM_CLK_DIVA
    global pwmSym_PWM_CLK_DIVB
    clock_Hz = 0.0
    frequency = None
    masterClock_Hz = pwmGetMasterClock()
    channelClock_Hz = pwmSym_PWM_CMR_CPRE[channelID].getSelectedKey()
    if (channelClock_Hz == "MCK"):
        clock_Hz = masterClock_Hz
    if (channelClock_Hz == "MCK_DIV_2"):
        clock_Hz = masterClock_Hz/2
    if (channelClock_Hz == "MCK_DIV_4"):
        clock_Hz = masterClock_Hz/4
    if (channelClock_Hz == "MCK_DIV_8"):
        clock_Hz = masterClock_Hz/8
    if (channelClock_Hz == "MCK_DIV_16"):
        clock_Hz = masterClock_Hz/16
    if (channelClock_Hz == "MCK_DIV_32"):
        clock_Hz = masterClock_Hz/32
    if (channelClock_Hz == "MCK_DIV_64"):
        clock_Hz = masterClock_Hz/64
    if (channelClock_Hz == "MCK_DIV_128"):
        clock_Hz = masterClock_Hz/128
    if (channelClock_Hz == "MCK_DIV_256"):
        clock_Hz = masterClock_Hz/256
    if (channelClock_Hz == "MCK_DIV_512"):
        clock_Hz = masterClock_Hz/512
    if (channelClock_Hz == "MCK_DIV_1024"):
        clock_Hz = masterClock_Hz/1024
    if (channelClock_Hz == "CLKA"):
        clock_Hz = pwmGetInternalClk(pwmSym_PWM_CLK_PREA.getSelectedKey(), pwmSym_PWM_CLK_DIVA.getValue())
    if (channelClock_Hz == "CLKB"):
        clock_Hz = pwmGetInternalClk(pwmSym_PWM_CLK_PREB.getSelectedKey(), pwmSym_PWM_CLK_DIVB.getValue())

    alignment = pwmSym_PWM_CMR_CALG[channelID].getSelectedKey()
    period = pwmSym_PWM_CPRD[channelID].getValue()
    if (alignment == "LEFT_ALIGNED"):
        frequency = 1.0 / (period / float(clock_Hz))
    else:
        frequency = 1.0 / (2.0 * period / float(clock_Hz))

    symbol.setLabel("**** PWM Frequency is " +str(frequency) +" Hz ****")

    if (pwmSym_CH_Enable[channelID].getValue() == True):
        if (pwmSym_CH_SyncEnable[channelID].getValue() == True):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmChannelConfVisible(symbol, event):
    if (event["value"] == True):
        if(symbol.getID() == "PWM_CH_0_SYNCENABLE"):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmDutyMaxValue(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[2])
    symbol.setMax(pwmSym_PWM_CPRD[channelID].getValue())

    if (pwmSym_CH_Enable[channelID].getValue() == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmFaultMenuVisible(symbol, event):
    if (pwmSym_PWM_Fault_Enable[0].getValue() == True or pwmSym_PWM_Fault_Enable[1].getValue() == True or \
    pwmSym_PWM_Fault_Enable[2].getValue() == True or pwmSym_PWM_Fault_Enable[3].getValue() == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmSyncChannelConfVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[2])

    if (pwmSym_CH_Enable[channelID].getValue() == True):
        if (pwmSym_CH_SyncEnable[channelID].getValue() == True):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmSyncChannelCommentVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[2])

    if (pwmSym_CH_Enable[channelID].getValue() == True):
        if (pwmSym_CH_SyncEnable[channelID].getValue() == True):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def pwmPrescalerCommentVisible(symbol, event):
    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[2])

    if (pwmSym_CH_Enable[channelID].getValue() == True):
        if (pwmSym_PWM_CMR_CPRE[channelID].getSelectedKey() == "CLKA" or pwmSym_PWM_CMR_CPRE[channelID].getSelectedKey() == "CLKB"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def pwmSyncMenuVisible(symbol, event):
    if (pwmSym_CH_SyncEnable[1].getValue() == True or pwmSym_CH_SyncEnable[2].getValue() == True or pwmSym_CH_SyncEnable[3].getValue() == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmSyncPeriodVisible(symbol, event):
    if (event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmCompMaxValue(symbol, event):
    symbol.setMax(event["value"])

def pwmCompMenuVisible(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(pwmComponent):
    global pwmNum
    pwmNum = pwmComponent.getID()[-1:]
    Log.writeInfoMessage("Running PWM" + str(pwmNum))

    #--------------------- Dependency ----------------------------------------
    global pwmPeriphId
    global pwmNVICVector
    global pwmNVICHandler
    global pwmNVICHandlerLock

    pwmPeriphId = Interrupt.getInterruptIndex("PWM" + str(pwmNum))
    pwmNVICVector = "NVIC_" + str(pwmPeriphId) + "_ENABLE"
    pwmNVICHandler = "NVIC_" + str(pwmPeriphId) + "_HANDLER"
    pwmNVICHandlerLock = "NVIC_" + str(pwmPeriphId) + "_HANDLER_LOCK"

    # NVIC Dynamic settings
    pwmSym_NVICControl = pwmComponent.createBooleanSymbol("PWM_NVIC_ENABLE", None)
    pwmSym_NVICControl.setDependencies(pwmNVICControl, ["PWM_CH_0_IER1_CHID", "PWM_CH_1_IER1_CHID", "PWM_CH_2_IER1_CHID", "PWM_CH_3_IER1_CHID"])
    pwmSym_NVICControl.setVisible(False)

    # Clock Dynamic settings
    pwmSym_ClockControl = pwmComponent.createBooleanSymbol("PWM_CLOCK_ENABLE", None)
    pwmSym_ClockControl.setDependencies(pwmClockControl, ["PWM_CH_0_ENABLE", "PWM_CH_1_ENABLE", "PWM_CH_2_ENABLE", "PWM_CH_3_ENABLE"])
    pwmSym_ClockControl.setVisible(False)

    # Dependency Status
    pwmSymClkEnComment = pwmComponent.createCommentSymbol("PWM_CLK_ENABLE_COMMENT", None)
    pwmSymClkEnComment.setVisible(False)
    pwmSymClkEnComment.setLabel("Warning!!! PWM Peripheral Clock is Disabled in Clock Manager")
    pwmSymClkEnComment.setDependencies(pwmClkDependencyStatus, ["core.PMC_ID_PWM" + str(pwmNum), "PWM_CH_0_ENABLE", "PWM_CH_1_ENABLE", "PWM_CH_2_ENABLE", "PWM_CH_3_ENABLE"])

    pwmSymIntEnComment = pwmComponent.createCommentSymbol("PWM_NVIC_ENABLE_COMMENT", None)
    pwmSymIntEnComment.setVisible(False)
    pwmSymIntEnComment.setLabel("Warning!!! PWM Interrupt is Disabled in Interrupt Manager")
    pwmSymIntEnComment.setDependencies(pwmNVICDependencyStatus, ["core." + pwmNVICVector, "PWM_CH_0_IER1_CHID", "PWM_CH_1_IER1_CHID", "PWM_CH_2_IER1_CHID", "PWM_CH_3_IER1_CHID", \
        "PWM_CH_0_ENABLE", "PWM_CH_1_ENABLE", "PWM_CH_2_ENABLE", "PWM_CH_3_ENABLE"])

    #-----------------------------------------------------------------------------------------------------------
    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = [False, False, False, False] #array t0 save available channels
    i = 0

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(packageName)+"\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    #Find available channels and available external clock pins
    pwm_signals = []
    pwm = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PWM\"]/instance@[name=\"PWM"+str(pwmNum)+"\"]/signals")
    pwm_signals = pwm.getChildren()
    for pad in range(0, len(pwm_signals)):
        if "PWMH" in pwm_signals[pad].getAttribute("group"):
            padSignal = pwm_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(pwm_signals[pad].getAttribute("index"))] = True
            else:
                channel[int(pwm_signals[pad].getAttribute("index"))] = False
    #-----------------------------------------------------------------------------------------------------------

    #Clock menu
    pwmClockMenu = pwmComponent.createMenuSymbol("PWM_CLOCK", None)
    pwmClockMenu.setLabel("Clock Configurations")

    #enable clock A
    pwmSym_PWM_CLKA_ENABLE = pwmComponent.createBooleanSymbol("PWM_CLK_A_ENABLE", pwmClockMenu)
    pwmSym_PWM_CLKA_ENABLE.setLabel("Enable Clock A")
    pwmSym_PWM_CLKA_ENABLE.setDefaultValue(False)

    #clock A source selection
    global pwmSym_PWM_CLK_PREA
    pwmSym_PWM_CLK_PREA = pwmComponent.createKeyValueSetSymbol("PWM_CLK_PREA", pwmSym_PWM_CLKA_ENABLE)
    pwmSym_PWM_CLK_PREA.setLabel("Select Clock A Source")
    childrenNodes = []
    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CLK__PREA\"]")
    childrenNodes = pwm.getChildren()
    for param in range(0, len(childrenNodes)):
        pwmSym_PWM_CLK_PREA.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
    pwmSym_PWM_CLK_PREA.setDefaultValue(0)
    pwmSym_PWM_CLK_PREA.setDisplayMode("Description")
    pwmSym_PWM_CLK_PREA.setOutputMode("Key")
    pwmSym_PWM_CLK_PREA.setVisible(False)
    pwmSym_PWM_CLK_PREA.setDependencies(pwmChannelConfVisible, ["PWM_CLK_A_ENABLE"])

    global pwmSym_PWM_CLK_DIVA
    pwmSym_PWM_CLK_DIVA = pwmComponent.createIntegerSymbol("PWM_CLK_DIVA", pwmSym_PWM_CLKA_ENABLE)
    pwmSym_PWM_CLK_DIVA.setLabel("Select Clock A Divider")
    pwmSym_PWM_CLK_DIVA.setDefaultValue(1)
    pwmSym_PWM_CLK_DIVA.setMin(1)
    pwmSym_PWM_CLK_DIVA.setMax(255)
    pwmSym_PWM_CLK_DIVA.setVisible(False)
    pwmSym_PWM_CLK_DIVA.setDependencies(pwmChannelConfVisible, ["PWM_CLK_A_ENABLE"])

    #enable clock A
    pwmSym_PWM_CLKB_ENABLE = pwmComponent.createBooleanSymbol("PWM_CLK_B_ENABLE", pwmClockMenu)
    pwmSym_PWM_CLKB_ENABLE.setLabel("Enable Clock B")
    pwmSym_PWM_CLKB_ENABLE.setDefaultValue(False)

    #clock B source selection
    global pwmSym_PWM_CLK_PREB
    pwmSym_PWM_CLK_PREB = pwmComponent.createKeyValueSetSymbol("PWM_CLK_PREB", pwmSym_PWM_CLKB_ENABLE)
    pwmSym_PWM_CLK_PREB.setLabel("Select Clock B Source")
    childrenNodes = []
    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CLK__PREB\"]")
    childrenNodes = pwm.getChildren()
    for param in range(0, len(childrenNodes)):
        pwmSym_PWM_CLK_PREB.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
    pwmSym_PWM_CLK_PREB.setDefaultValue(0)
    pwmSym_PWM_CLK_PREB.setDisplayMode("Description")
    pwmSym_PWM_CLK_PREB.setOutputMode("Key")
    pwmSym_PWM_CLK_PREB.setVisible(False)
    pwmSym_PWM_CLK_PREB.setDependencies(pwmChannelConfVisible, ["PWM_CLK_B_ENABLE"])

    global pwmSym_PWM_CLK_DIVB
    pwmSym_PWM_CLK_DIVB = pwmComponent.createIntegerSymbol("PWM_CLK_DIVB", pwmSym_PWM_CLKB_ENABLE)
    pwmSym_PWM_CLK_DIVB.setLabel("Select Clock B Divider")
    pwmSym_PWM_CLK_DIVB.setDefaultValue(1)
    pwmSym_PWM_CLK_DIVB.setMin(1)
    pwmSym_PWM_CLK_DIVB.setMax(255)
    pwmSym_PWM_CLK_DIVB.setVisible(False)
    pwmSym_PWM_CLK_DIVB.setDependencies(pwmChannelConfVisible, ["PWM_CLK_B_ENABLE"])
    #-----------------------------------------------------------------------------------------------------------
    #channel menu
    pwmChannelConfMenu = pwmComponent.createMenuSymbol("PWM_CHANNEL", None)
    pwmChannelConfMenu.setLabel("Channel Configurations")

    for channelID in range(0, 4):
        #channel menu
        pwmChannelMenu.append(channelID)
        pwmChannelMenu[channelID] = pwmComponent.createMenuSymbol("Channel "+str(channelID), pwmChannelConfMenu)
        pwmChannelMenu[channelID].setLabel("Channel "+str(channelID))
        if (channel[channelID] == True):
            pwmChannelMenu[channelID].setVisible(True)
        else:
            pwmChannelMenu[channelID].setVisible(False)

        #channel enable
        pwmSym_CH_Enable.append(channelID)
        pwmSym_CH_Enable[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_ENABLE", pwmChannelMenu[channelID])
        pwmSym_CH_Enable[channelID].setLabel("Enable")
        pwmSym_CH_Enable[channelID].setDefaultValue(False)

        #sync enable
        pwmSym_CH_SyncEnable.append(channelID)
        pwmSym_CH_SyncEnable[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_SYNCENABLE", pwmSym_CH_Enable[channelID])
        pwmSym_CH_SyncEnable[channelID].setLabel("Enable Sync Mode")
        pwmSym_CH_SyncEnable[channelID].setDefaultValue(False)
        pwmSym_CH_SyncEnable[channelID].setVisible(False)
        pwmSym_CH_SyncEnable[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

        #sync comment
        pwmSym_CH_Sync_Comment.append(channelID)
        pwmSym_CH_Sync_Comment[channelID] = pwmComponent.createCommentSymbol("PWM_CH_"+str(channelID)+"_SYNC_COMMENT", pwmSym_CH_Enable[channelID])
        pwmSym_CH_Sync_Comment[channelID].setLabel("**** Channel "+str(channelID) + " is synchronized with channel 0. Enable and configure channel 0 ****")
        pwmSym_CH_Sync_Comment[channelID].setVisible(False)
        pwmSym_CH_Sync_Comment[channelID].setDependencies(pwmSyncChannelCommentVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])

        #prescaler
        pwmSym_PWM_CMR_CPRE.append(channelID)
        pwmSym_PWM_CMR_CPRE[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CPRE", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_CPRE[channelID].setLabel("Select Channel Clock")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMR0__CPRE\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_CPRE[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_CPRE[channelID].setDefaultValue(0)
        pwmSym_PWM_CMR_CPRE[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_CPRE[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_CPRE[channelID].setVisible(False)
        pwmSym_PWM_CMR_CPRE[channelID].setDependencies(pwmSyncChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])

        #prescaler comment
        pwmSym_CH_Prescaler_Comment.append(channelID)
        pwmSym_CH_Prescaler_Comment[channelID] = pwmComponent.createCommentSymbol("PWM_CH_"+str(channelID)+"_PRESCALER_COMMENT", pwmSym_CH_Enable[channelID])
        pwmSym_CH_Prescaler_Comment[channelID].setLabel("**** Make sure that clock is enabled in Clock Configurations ****")
        pwmSym_CH_Prescaler_Comment[channelID].setVisible(False)
        pwmSym_CH_Prescaler_Comment[channelID].setDependencies(pwmPrescalerCommentVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_CMR_CPRE"])

        #alignment
        pwmSym_PWM_CMR_CALG.append(channelID)
        pwmSym_PWM_CMR_CALG[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CALG", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_CALG[channelID].setLabel("Select Alignment")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMR0__CALG\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_CALG[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_CALG[channelID].setDefaultValue(1)
        pwmSym_PWM_CMR_CALG[channelID].setVisible(False)
        pwmSym_PWM_CMR_CALG[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_CALG[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_CALG[channelID].setDependencies(pwmSyncChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])

        #update selection
        pwmSym_PWM_CMR_UPDS.append(channelID)
        pwmSym_PWM_CMR_UPDS[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_UPDS", pwmSym_PWM_CMR_CALG[channelID])
        pwmSym_PWM_CMR_UPDS[channelID].setLabel("Select Duty-Cycle Update Trigger")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMR0__UPDS\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_UPDS[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_UPDS[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_UPDS[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_UPDS[channelID].setDependencies(pwmAlignmentVisible, ["PWM_CH_"+str(channelID)+"_CMR_CALG"])

        #counter event selection
        pwmSym_PWM_CMR_CES.append(channelID)
        pwmSym_PWM_CMR_CES[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CES", pwmSym_PWM_CMR_CALG[channelID])
        pwmSym_PWM_CMR_CES[channelID].setLabel("Select Counter Event Occurrence")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMR0__CES\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_CES[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_CES[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_CES[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_CES[channelID].setDependencies(pwmAlignmentVisible, ["PWM_CH_"+str(channelID)+"_CMR_CALG"])

        #polarity
        pwmSym_PWM_CMR_CPOL.append(channelID)
        pwmSym_PWM_CMR_CPOL[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CPOL", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_CPOL[channelID].setLabel("Output Polarity")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMR0__CPOL\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_CPOL[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_CPOL[channelID].setVisible(False)
        pwmSym_PWM_CMR_CPOL[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_CPOL[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_CPOL[channelID].setDependencies(pwmSyncChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])

        #period
        pwmSym_PWM_CPRD.append(channelID)
        pwmSym_PWM_CPRD[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_CPRD", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CPRD[channelID].setLabel("Period Value")
        pwmSym_PWM_CPRD[channelID].setDefaultValue(7500)
        pwmSym_PWM_CPRD[channelID].setMin(0)
        pwmSym_PWM_CPRD[channelID].setMax(65535)
        pwmSym_PWM_CPRD[channelID].setVisible(False)
        pwmSym_PWM_CPRD[channelID].setDependencies(pwmSyncChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])

        #PWM frequency comment
        pwmSym_PWM_FreqComment.append(channelID)
        pwmSym_PWM_FreqComment[channelID] = pwmComponent.createCommentSymbol("PWM_CH_"+str(channelID)+"_FREQ_COMMENT", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_FreqComment[channelID].setLabel("**** PWM Frequency is 10000 Hz ****")
        pwmSym_PWM_FreqComment[channelID].setDependencies(pwmCalcFreq, ["core.MASTERCLK_FREQ", "PWM_CH_"+str(channelID)+"_CMR_CPRE",\
        "PWM_CLK_PREA", "PWM_CLK_PREB", "PWM_CLK_DIVA", "PWM_CLK_DIVB", "PWM_CH_"+str(channelID)+"_CPRD", "PWM_CH_"+str(channelID)+"_CMR_CALG", "PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])
        pwmSym_PWM_FreqComment[channelID].setVisible(False)

        #duty
        pwmSym_PWM_CDTY.append(channelID)
        pwmSym_PWM_CDTY[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_CDTY", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CDTY[channelID].setLabel("Duty Value")
        pwmSym_PWM_CDTY[channelID].setDefaultValue(3750)
        pwmSym_PWM_CDTY[channelID].setMin(0)
        pwmSym_PWM_CDTY[channelID].setMax(pwmSym_PWM_CPRD[channelID].getValue())
        pwmSym_PWM_CDTY[channelID].setVisible(False)
        pwmSym_PWM_CDTY[channelID].setDependencies(pwmDutyMaxValue, ["PWM_CH_"+str(channelID)+"_CPRD", "PWM_CH_"+str(channelID)+"_ENABLE"])

        #dead time enable
        pwmSym_PWM_CMR_DTE.append(channelID)
        pwmSym_PWM_CMR_DTE[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_CMR_DTE", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_DTE[channelID].setLabel("Enable Dead Time")
        pwmSym_PWM_CMR_DTE[channelID].setDefaultValue(True)
        pwmSym_PWM_CMR_DTE[channelID].setVisible(False)
        pwmSym_PWM_CMR_DTE[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

        #duty for low side output
        pwmSym_PWM_DT_DTL.append(channelID)
        pwmSym_PWM_DT_DTL[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_DT_DTL", pwmSym_PWM_CMR_DTE[channelID])
        pwmSym_PWM_DT_DTL[channelID].setLabel("Dead Time for low-Side Output")
        pwmSym_PWM_DT_DTL[channelID].setDefaultValue(100)
        pwmSym_PWM_DT_DTL[channelID].setMin(0)
        pwmSym_PWM_DT_DTL[channelID].setMax(4095)

        #duty for high side output
        pwmSym_PWM_DT_DTH.append(channelID)
        pwmSym_PWM_DT_DTH[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_DT_DTH", pwmSym_PWM_CMR_DTE[channelID])
        pwmSym_PWM_DT_DTH[channelID].setLabel("Dead Time for high-Side Output")
        pwmSym_PWM_DT_DTH[channelID].setDefaultValue(100)
        pwmSym_PWM_DT_DTH[channelID].setMin(0)
        pwmSym_PWM_DT_DTH[channelID].setMax(4095)

        #fault enable
        pwmSym_PWM_Fault_Enable.append(channelID)
        pwmSym_PWM_Fault_Enable[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_FAULT_ENABLE", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_Fault_Enable[channelID].setLabel("Enable Fault")
        pwmSym_PWM_Fault_Enable[channelID].setDefaultValue(False)
        pwmSym_PWM_Fault_Enable[channelID].setVisible(False)
        pwmSym_PWM_Fault_Enable[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

        #fault source
        pwmSym_PWM_FPE.append(channelID)
        pwmSym_PWM_FPE[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_FPE", pwmSym_PWM_Fault_Enable[channelID])
        pwmSym_PWM_FPE[channelID].setLabel("Select Fault Source")
        pwmSym_PWM_FPE[channelID].setDefaultValue(0)
        pwmSym_PWM_FPE[channelID].setVisible(False)
        fault_id = []
        pwm = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PWM\"]/instance@[name=\"PWM"+str(pwmNum)+"\"]/parameters")
        fault_id = pwm.getChildren()
        for param in range(0, len(fault_id)):
            if "FAULT" in fault_id[param].getAttribute("name"):
                pwmSym_PWM_FPE[channelID].addKey(fault_id[param].getAttribute("name"), fault_id[param].getAttribute("value"), fault_id[param].getAttribute("caption"))
        pwmSym_PWM_FPE[channelID].setDisplayMode("Description")
        pwmSym_PWM_FPE[channelID].setOutputMode("Value")
        pwmSym_PWM_FPE[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_FAULT_ENABLE"])

        #output polarity after fault
        pwmSym_PWM_FPV_FPVL.append(channelID)
        pwmSym_PWM_FPV_FPVL[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_FAULT_"+str(channelID)+"_FPV_FPVL", pwmSym_PWM_Fault_Enable[channelID])
        pwmSym_PWM_FPV_FPVL[channelID].setLabel("Select low-side Output Polarity after Fault")
        pwmSym_PWM_FPV_FPVL[channelID].addKey("LOW", "0", "Low")
        pwmSym_PWM_FPV_FPVL[channelID].addKey("HIGH", "1", "High")
        pwmSym_PWM_FPV_FPVL[channelID].addKey("HIGH_IMPEDANCE", "2", "High-Impedance")
        pwmSym_PWM_FPV_FPVL[channelID].setDisplayMode("Description")
        pwmSym_PWM_FPV_FPVL[channelID].setOutputMode("Value")
        pwmSym_PWM_FPV_FPVL[channelID].setDefaultValue(1)
        pwmSym_PWM_FPV_FPVL[channelID].setVisible(False)
        pwmSym_PWM_FPV_FPVL[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_FAULT_ENABLE"])

        pwmSym_PWM_FPV_FPVH.append(channelID)
        pwmSym_PWM_FPV_FPVH[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_FAULT_"+str(channelID)+"_FPV_FPVH", pwmSym_PWM_Fault_Enable[channelID])
        pwmSym_PWM_FPV_FPVH[channelID].setLabel("Select high-side Output Polarity after Fault")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("LOW", "0", "Low")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("HIGH", "1", "High")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("HIGH_IMPEDANCE", "2", "High-Impedance")
        pwmSym_PWM_FPV_FPVH[channelID].setDisplayMode("Description")
        pwmSym_PWM_FPV_FPVH[channelID].setOutputMode("Value")
        pwmSym_PWM_FPV_FPVH[channelID].setVisible(False)
        pwmSym_PWM_FPV_FPVH[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_FAULT_ENABLE"])

        #interrupt enable
        pwmSym_PWM_IER1_CHID.append(channelID)
        pwmSym_PWM_IER1_CHID[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_IER1_CHID", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_IER1_CHID[channelID].setLabel("Enable Counter Event")
        pwmSym_PWM_IER1_CHID[channelID].setDefaultValue(False)
        pwmSym_PWM_IER1_CHID[channelID].setVisible(False)
        pwmSym_PWM_IER1_CHID[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

    #-----------------------------------------------------------------------------------------------------------

    #fault menu
    pwmFaultMenu = pwmComponent.createMenuSymbol("PWM_FAULT", None)
    pwmFaultMenu.setLabel("Fault Configurations")
    pwmFaultMenu.setVisible(False)
    pwmFaultMenu.setDependencies(pwmFaultMenuVisible, ["PWM_CH_0_FAULT_ENABLE", "PWM_CH_1_FAULT_ENABLE", "PWM_CH_2_FAULT_ENABLE", "PWM_CH_3_FAULT_ENABLE"])

    for faultID in range(0, 8):
        pwmFaultIndexMenu.append(faultID)
        pwmFaultIndexMenu[faultID] = pwmComponent.createMenuSymbol("PWM_FAULT_"+str(faultID)+"_INDEX", pwmFaultMenu)
        pwmFaultIndexMenu[faultID].setLabel("Fault "+str(faultID))

        #fault polarity
        pwmSym_PWM_FMR_FPOL.append(faultID)
        pwmSym_PWM_FMR_FPOL[faultID] = pwmComponent.createKeyValueSetSymbol("PWM_FAULT_"+str(faultID)+"_FMR_FPOL", pwmFaultIndexMenu[faultID])
        pwmSym_PWM_FMR_FPOL[faultID].setLabel("Select Fault Polarity")
        pwmSym_PWM_FMR_FPOL[faultID].addKey("LOW", "0", "Active when fault input is low")
        pwmSym_PWM_FMR_FPOL[faultID].addKey("HIGH", "1", "Active when fault input is high")
        pwmSym_PWM_FMR_FPOL[faultID].setDisplayMode("Description")
        pwmSym_PWM_FMR_FPOL[faultID].setOutputMode("Value")
        if (faultID > 2):
            pwmSym_PWM_FMR_FPOL[faultID].setDefaultValue(1)
            pwmSym_PWM_FMR_FPOL[faultID].setReadOnly(True)

        #fault mode
        pwmSym_PWM_FMR_FMOD.append(faultID)
        pwmSym_PWM_FMR_FMOD[faultID] = pwmComponent.createKeyValueSetSymbol("PWM_FAULT_"+str(faultID)+"_FMR_FMOD", pwmFaultIndexMenu[faultID])
        pwmSym_PWM_FMR_FMOD[faultID].setLabel("Select Fault Mode")
        pwmSym_PWM_FMR_FMOD[faultID].addKey("CLEAR_AT_PERIPHERAL", "0", "Fault is active until cleared at peripheral level")
        pwmSym_PWM_FMR_FMOD[faultID].addKey("CLEAR_AT_PERIPHERAL_AND_REGISTER", "1", "Fault is active until cleared at peripheral level AND cleared in PWM_FCR register")
        pwmSym_PWM_FMR_FMOD[faultID].setDisplayMode("Description")
        pwmSym_PWM_FMR_FMOD[faultID].setOutputMode("Value")
        pwmSym_PWM_FMR_FMOD[faultID].setDefaultValue(1)

    #-----------------------------------------------------------------------------------------------------------

    #Synchronous channels menu
    pwmSyncChMenu = pwmComponent.createMenuSymbol("PWM_SYNC_CHANNELS", None)
    pwmSyncChMenu.setLabel("Synchronous Channels Configurations")
    pwmSyncChMenu.setVisible(False)
    pwmSyncChMenu.setDependencies(pwmSyncMenuVisible, ["PWM_CH_0_SYNCENABLE", "PWM_CH_1_SYNCENABLE", "PWM_CH_2_SYNCENABLE"])

    #sync update mode
    pwmSym_PWM_SCM_UPDM = pwmComponent.createKeyValueSetSymbol("PWM_SCM_UPDM", pwmSyncChMenu)
    pwmSym_PWM_SCM_UPDM.setLabel("Select Synchronous Channel Update Mode")
    childrenNodes = []
    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_SCM__UPDM\"]")
    childrenNodes = pwm.getChildren()
    for param in range(0, (len(childrenNodes) - 1)):
        pwmSym_PWM_SCM_UPDM.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
    pwmSym_PWM_SCM_UPDM.setDefaultValue(1)
    pwmSym_PWM_SCM_UPDM.setDisplayMode("Description")
    pwmSym_PWM_SCM_UPDM.setOutputMode("Key")

    #Sync update period
    pwmSym_PWM_SCUP_UPR = pwmComponent.createIntegerSymbol("PWM_SCUP_UPR", pwmSyncChMenu)
    pwmSym_PWM_SCUP_UPR.setLabel("Synchronous Update Period")
    pwmSym_PWM_SCUP_UPR.setMin(0)
    pwmSym_PWM_SCUP_UPR.setMax(15)
    pwmSym_PWM_SCUP_UPR.setDefaultValue(0)
    pwmSym_PWM_SCUP_UPR.setDependencies(pwmSyncPeriodVisible, ["PWM_SCM_UPDM"])

    #-----------------------------------------------------------------------------------------------------------
    #compare unit menu
    pwmCompareMenu = pwmComponent.createMenuSymbol("PWM_COMPARE", None)
    pwmCompareMenu.setLabel("Compare Unit Configurations")
    pwmCompareMenu.setDependencies(pwmCompMenuVisible, ["PWM_CH_0_ENABLE"])

    for compareID in range(0, 8):

        #compare unit enable
        pwmSym_PWM_CMPM_CEN.append(compareID)
        pwmSym_PWM_CMPM_CEN[compareID] = pwmComponent.createBooleanSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CEN", pwmCompareMenu)
        pwmSym_PWM_CMPM_CEN[compareID].setLabel("Compare Unit " + str(compareID) +" Enable")
        pwmSym_PWM_CMPM_CEN[compareID].setDefaultValue(False)

        pwmSym_PWM_ELMR0_CSEL.append(compareID)
        pwmSym_PWM_ELMR0_CSEL[compareID] = pwmComponent.createBooleanSymbol("PWM_COMP_"+str(compareID)+"_ELMR0_CSEL", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_ELMR0_CSEL[compareID].setLabel("Generate Pulse on Event Line 0")
        pwmSym_PWM_ELMR0_CSEL[compareID].setDefaultValue(False)

        pwmSym_PWM_ELMR1_CSEL.append(compareID)
        pwmSym_PWM_ELMR1_CSEL[compareID] = pwmComponent.createBooleanSymbol("PWM_COMP_"+str(compareID)+"_ELMR1_CSEL", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_ELMR1_CSEL[compareID].setLabel("Generate Pulse on Event Line 1")
        pwmSym_PWM_ELMR1_CSEL[compareID].setDefaultValue(False)

        #compare Value
        pwmSym_PWM_CMPV_CV.append(compareID)
        pwmSym_PWM_CMPV_CV[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPV_CV", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPV_CV[compareID].setLabel("Comparison Value")
        pwmSym_PWM_CMPV_CV[compareID].setDefaultValue(100)
        pwmSym_PWM_CMPV_CV[compareID].setMin(0)
        pwmSym_PWM_CMPV_CV[compareID].setMax(pwmSym_PWM_CPRD[0].getValue())
        pwmSym_PWM_CMPV_CV[compareID].setDependencies(pwmCompMaxValue, ["PWM_CH_0_CPRD"])

        #compare mode
        pwmSym_PWM_CMPV_CVM.append(compareID)
        pwmSym_PWM_CMPV_CVM[compareID] = pwmComponent.createKeyValueSetSymbol("PWM_COMP_"+str(compareID)+"_CMPV_CVM", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPV_CVM[compareID].setLabel("Comparison Mode")
        childrenNodes = []
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"PWM_CMPV0__CVM\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMPV_CVM[compareID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMPV_CVM[compareID].setDisplayMode("Description")
        pwmSym_PWM_CMPV_CVM[compareID].setOutputMode("Key")
        pwmSym_PWM_CMPV_CVM[compareID].setDependencies(pwmAlignmentVisible, ["PWM_CH_0_CMR_CALG"])

        #CTR, CPR, CUPR
        pwmSym_PWM_CMPM_CPR.append(compareID)
        pwmSym_PWM_CMPM_CPR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CPR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CPR[compareID].setLabel("Comparison Period")
        pwmSym_PWM_CMPM_CPR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CPR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CPR[compareID].setMax(15)

        pwmSym_PWM_CMPM_CTR.append(compareID)
        pwmSym_PWM_CMPM_CTR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CTR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CTR[compareID].setLabel("Comparison Trigger")
        pwmSym_PWM_CMPM_CTR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CTR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CTR[compareID].setMax(pwmSym_PWM_CMPM_CPR[compareID].getValue())
        pwmSym_PWM_CMPM_CTR[compareID].setDependencies(pwmCompMaxValue, ["PWM_COMP_"+str(compareID)+"_CMPM_CPR"])

        pwmSym_PWM_CMPM_CUPR.append(compareID)
        pwmSym_PWM_CMPM_CUPR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CUPR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CUPR[compareID].setLabel("Comparison Update Period")
        pwmSym_PWM_CMPM_CUPR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CUPR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CUPR[compareID].setMax(pwmSym_PWM_CMPM_CPR[compareID].getValue())
        pwmSym_PWM_CMPM_CUPR[compareID].setDependencies(pwmCompMaxValue, ["PWM_COMP_"+str(compareID)+"_CMPM_CPR"])

    #-----------------------------------------------------------------------------------------------------------
    pwmIndex = pwmComponent.createIntegerSymbol("INDEX", pwmChannelMenu[channelID])
    pwmIndex.setVisible(False)
    pwmIndex.setDefaultValue(int(pwmNum))

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################

    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]")
    pwmID = pwm.getAttribute("id")

    pwmHeaderFile = pwmComponent.createFileSymbol(None, None)
    pwmHeaderFile.setSourcePath("../peripheral/pwm_"+str(pwmID)+"/templates/plib_pwm.h.ftl")
    pwmHeaderFile.setOutputName("plib_pwm" + str(pwmNum) + ".h")
    pwmHeaderFile.setDestPath("/peripheral/pwm/")
    pwmHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmHeaderFile.setType("HEADER")
    pwmHeaderFile.setOverwrite(True)
    pwmHeaderFile.setMarkup(True)

    pwmSource1File = pwmComponent.createFileSymbol(None, None)
    pwmSource1File.setSourcePath("../peripheral/pwm_"+str(pwmID)+"/templates/plib_pwm.c.ftl")
    pwmSource1File.setOutputName("plib_pwm" + str(pwmNum) + ".c")
    pwmSource1File.setDestPath("/peripheral/pwm/")
    pwmSource1File.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmSource1File.setType("SOURCE")
    pwmSource1File.setOverwrite(True)
    pwmSource1File.setMarkup(True)

    pwmGlobalHeaderFile = pwmComponent.createFileSymbol(None, None)
    pwmGlobalHeaderFile.setSourcePath("../peripheral/pwm_"+str(pwmID)+"/plib_pwm.h")
    pwmGlobalHeaderFile.setOutputName("plib_pwm" + ".h")
    pwmGlobalHeaderFile.setDestPath("/peripheral/pwm/")
    pwmGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmGlobalHeaderFile.setType("HEADER")
    pwmGlobalHeaderFile.setMarkup(False)

    pwmSystemInitFile = pwmComponent.createFileSymbol(None, None)
    pwmSystemInitFile.setType("STRING")
    pwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pwmSystemInitFile.setSourcePath("../peripheral/pwm_"+str(pwmID)+"/templates/system/system_initialize.c.ftl")
    pwmSystemInitFile.setMarkup(True)

    pwmSystemDefinitionFile = pwmComponent.createFileSymbol(None, None)
    pwmSystemDefinitionFile.setType("STRING")
    pwmSystemDefinitionFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pwmSystemDefinitionFile.setSourcePath("../peripheral/pwm_"+str(pwmID)+"/templates/system/system_definitions.h.ftl")
    pwmSystemDefinitionFile.setMarkup(True)
