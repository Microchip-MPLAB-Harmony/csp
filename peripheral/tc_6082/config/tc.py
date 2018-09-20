###################################################################################################
########################### Global Variables   #################################
###################################################################################################
global tcInstanceName
global extClock
channel_periphId = [0, 0, 0]

tcChannelMenu = []
tcSym_CH_Enable = []
tcSym_CH_CMR_TCCLKS = [0, 0, 0, 0]
tcSym_CH_EXT_CLOCK = [0, 0, 0, 0]
tcSym_CH_CLOCK_FREQ = [0, 0, 0, 0]
tcSym_CH_PCK7 = [0, 0, 0, 0]
tcSym_CH_Resolution = [0, 0, 0, 0]
tcSym_CH_OperatingMode = []

tcTimerMenu = []
tcSym_CH_TimerPeriod = []
tcSym_CH_TimerPeriodComment = []
tcSym_CH_TimerPeriodCount = []
tcSym_CH_CMR_CPCSTOP = []
tcSym_CH_IER_CPCS = []
tcSym_CH_IER_CPAS = []

tcCaptureMenu = []
tcSym_CH_CMR_LDRA = []
tcSym_CH_CMR_LDRB = []
tcSym_CH_CAPTURE_EXT_RESET = []
tcSym_CH_CMR_ETRGEDG = []
tcSym_CH_CMR_ETRGEDG_COMMENT = []
tcSym_CH_CMR_ETRGEDG_ALERT = []
tcSym_CH_CAPTURE_IER_LDRAS = []
tcSym_CH_CAPTURE_IER_LDRBS = []
tcSym_CH_CAPTURE_IER_COVFS = []
tcSym_CH_CMR_ABETRG = []
tcSym_CH_CAPTURE_CMR_LDBSTOP = []

tcCompareMenu = []
tcSym_CH_CMR_WAVSEL = []
tcSym_CH_ComparePeriodCount = []
tcSym_CH_ComparePeriod = []
tcEventMenu = []
tcCompareAMenu = []
tcSym_CH_CompareA = []
tcSym_CH_CMR_ACPA = []
tcSym_CH_CMR_ACPC = []
tcSym_CH_CMR_AEEVT = []
tcCompareBMenu = []
tcSym_CH_CompareB = []
tcSym_CH_CMR_BCPB = []
tcSym_CH_CMR_BCPC = []
tcSym_CH_CMR_BEEVT = []
tcSym_CH_CMR_EEVT = []
tcSym_CH_CMP_CMR_ETRGEDG = []
tcSym_CH_COMPARE_IER_CPCS = []
tcSym_CH_COMPARE_CMR_CPCSTOP = []

tcSym_CH_ClockControl = []
tcSym_CH_interruptControl = []
tcSym_CH_IntEnComment = []
tcSym_CH_ClkEnComment = []

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################
#channel number is extracted as 2nd character in ID. like TC0_xxx, TC1_xxx, TC2_xxx

#Enable/Disable peripheral clock
def tcClockControl(symbol, event):
    id = symbol.getID()
    channelID = int(id[2])
    if(tcSym_CH_EnableQEI.getValue() == True):
        Database.clearSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL0_CLOCK_ENABLE")
        Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL0_CLOCK_ENABLE", True, 2)
        Database.clearSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL1_CLOCK_ENABLE")
        if(tcSym_CH_QEI_INDEX_PULSE.getValue() == True):
            Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL1_CLOCK_ENABLE", True, 2)
        else:
            if(tcSym_CH_Enable[1].getValue() == True):
                Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL1_CLOCK_ENABLE", True, 2)
            else:
                Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL1_CLOCK_ENABLE", False, 2)
        if(tcSym_CH_BMR_POSEN.getValue() == "SPEED"):
            Database.clearSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE")
            Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE", True, 2)
        else:
            if(tcSym_CH_Enable[2].getValue() == True):
                Database.clearSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE")
                Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE", True, 2)
            else:
                Database.clearSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE")
                Database.setSymbolValue("core", tcInstanceName.getValue()  + "_CHANNEL2_CLOCK_ENABLE", False, 2)
    else:
        if(tcSym_CH_Enable[channelID].getValue() == True):
            Database.clearSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE")
            Database.setSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE", True, 2)
        else:
            Database.clearSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE")
            Database.setSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE", False, 2)

#Enable/Disable interrupt
def tcinterruptControl(symbol, event):
    id = symbol.getID()
    channelID = int(id[2])
    global channel_periphId

    interruptVector = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_ENABLE"
    interruptHandler = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER"
    interruptHandlerLock = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER_LOCK"

    if(tcSym_CH_EnableQEI.getValue() == True):
        interruptVector = tcInstanceName.getValue() + "_CH0_INTERRUPT_ENABLE"
        interruptHandler = tcInstanceName.getValue() + "_CH0_INTERRUPT_HANDLER"
        interruptHandlerLock = tcInstanceName.getValue() + "_CH0_INTERRUPT_HANDLER_LOCK"
        Database.clearSymbolValue("core", interruptVector)
        Database.clearSymbolValue("core", interruptHandler)
        Database.clearSymbolValue("core", interruptHandlerLock)
        if(tcSym_CH_QIER_IDX.getValue() == True or tcSym_CH_QIER_QERR.getValue() == True or tcSym_CH_QEI_IER_CPCS.getValue() == True):
            Database.setSymbolValue("core", interruptVector, True, 2)
            Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH0_InterruptHandler", 2)
            Database.setSymbolValue("core", interruptHandlerLock, True, 2)
        else:
            Database.setSymbolValue("core", interruptVector, False, 2)
            Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH0_Handler", 2)
            Database.setSymbolValue("core", interruptHandlerLock, False, 2)

        if (tcSym_CH_BMR_POSEN.getValue() == "POSITION" and channelID == 2):
            interruptVector = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_ENABLE"
            interruptHandler = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER"
            interruptHandlerLock = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER_LOCK"
            if (tcSym_CH_Enable[channelID].getValue() == True):
                Database.clearSymbolValue("core", interruptVector)
                Database.clearSymbolValue("core", interruptHandler)
                Database.clearSymbolValue("core", interruptHandlerLock)
                if(tcSym_CH_OperatingMode[channelID].getValue() == "TIMER" and tcSym_CH_IER_CPCS[channelID].getValue() == True):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                elif(tcSym_CH_OperatingMode[channelID].getValue() == "CAPTURE" and \
                    (tcSym_CH_CAPTURE_IER_LDRAS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_LDRBS[channelID].getValue() == True
                     or tcSym_CH_CAPTURE_IER_COVFS[channelID].getValue() == True)):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                elif(tcSym_CH_OperatingMode[channelID].getValue() == "COMPARE" and tcSym_CH_COMPARE_IER_CPCS[channelID].getValue() == True):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                else:
                    Database.setSymbolValue("core", interruptVector, False, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, False, 2)
            else:
                Database.setSymbolValue("core", interruptVector, False, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, False, 2)

        if(tcSym_CH_QEI_INDEX_PULSE.getValue() == False and channelID == 1):
            interruptVector = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_ENABLE"
            interruptHandler = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER"
            interruptHandlerLock = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_HANDLER_LOCK"
            if (tcSym_CH_Enable[channelID].getValue() == True):
                Database.clearSymbolValue("core", interruptVector)
                Database.clearSymbolValue("core", interruptHandler)
                Database.clearSymbolValue("core", interruptHandlerLock)
                if(tcSym_CH_OperatingMode[channelID].getValue() == "TIMER" and tcSym_CH_IER_CPCS[channelID].getValue() == True):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                elif(tcSym_CH_OperatingMode[channelID].getValue() == "CAPTURE" and \
                    (tcSym_CH_CAPTURE_IER_LDRAS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_LDRBS[channelID].getValue() == True or
                     tcSym_CH_CAPTURE_IER_COVFS[channelID].getValue() == True)):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                elif(tcSym_CH_OperatingMode[channelID].getValue() == "COMPARE" and tcSym_CH_COMPARE_IER_CPCS[channelID].getValue() == True):
                    Database.setSymbolValue("core", interruptVector, True, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, True, 2)
                else:
                    Database.setSymbolValue("core", interruptVector, False, 2)
                    Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
                    Database.setSymbolValue("core", interruptHandlerLock, False, 2)
            else:
                Database.setSymbolValue("core", interruptVector, False, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, False, 2)
    else:
        Database.clearSymbolValue("core", interruptVector)
        Database.clearSymbolValue("core", interruptHandler)
        Database.clearSymbolValue("core", interruptHandlerLock)
        if(tcSym_CH_Enable[channelID].getValue() == True):
            if(tcSym_CH_OperatingMode[channelID].getValue() == "TIMER" and (tcSym_CH_IER_CPCS[channelID].getValue() == True or tcSym_CH_IER_CPAS[channelID].getValue() == True)):
                Database.setSymbolValue("core", interruptVector, True, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, True, 2)
            elif(tcSym_CH_OperatingMode[channelID].getValue() == "CAPTURE" and \
                (tcSym_CH_CAPTURE_IER_LDRAS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_LDRBS[channelID].getValue() == True or
                 tcSym_CH_CAPTURE_IER_COVFS[channelID].getValue() == True)):
                Database.setSymbolValue("core", interruptVector, True, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, True, 2)
            elif(tcSym_CH_OperatingMode[channelID].getValue() == "COMPARE" and tcSym_CH_COMPARE_IER_CPCS[channelID].getValue() == True):
                Database.setSymbolValue("core", interruptVector, True, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_InterruptHandler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, True, 2)
            else:
                Database.setSymbolValue("core", interruptVector, False, 2)
                Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
                Database.setSymbolValue("core", interruptHandlerLock, False, 2)
        else:
            Database.setSymbolValue("core", interruptVector, False, 2)
            Database.setSymbolValue("core", interruptHandler, tcInstanceName.getValue() + "_CH"+str(channelID)+"_Handler", 2)
            Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def tcdependencyClockStatus(symbol, event):
    id = symbol.getID()
    channelID = int(id[2])
    clock = bool(Database.getSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE"))
    global tcSym_CH_Enable
    if (clock == False and tcSym_CH_Enable[channelID].getValue() == True):
        tcSym_CH_ClkEnComment[channelID].setVisible(True)
    else:
        tcSym_CH_ClkEnComment[channelID].setVisible(False)

def tcdependencyIntStatus(symbol, event):
    id = symbol.getID()
    channelID = int(id[2])
    global tcSym_CH_Enable
    interruptVectorUpdate = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_ENABLE_UPDATE"
    nvic = bool(Database.getSymbolValue("core", interruptVectorUpdate))
    if(tcSym_CH_Enable[channelID].getValue() == True):
        if(tcSym_CH_OperatingMode[channelID].getValue() == "TIMER" and tcSym_CH_IER_CPCS[channelID].getValue() == True and nvic == True):
            tcSym_CH_IntEnComment[channelID].setVisible(True)
        elif(tcSym_CH_OperatingMode[channelID].getValue() == "CAPTURE" and nvic == True and
             (tcSym_CH_CAPTURE_IER_LDRAS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_LDRBS[channelID].getValue() == True or
              tcSym_CH_CAPTURE_IER_COVFS[channelID].getValue() == True)):
            tcSym_CH_IntEnComment[channelID].setVisible(True)
        elif(tcSym_CH_OperatingMode[channelID].getValue() == "COMPARE" and tcSym_CH_COMPARE_IER_CPCS[channelID].getValue() == True and nvic == True):
            tcSym_CH_IntEnComment[channelID].setVisible(True)
        else:
            tcSym_CH_IntEnComment[channelID].setVisible(False)
    else:
        tcSym_CH_IntEnComment[channelID].setVisible(False)


def tcQEIDependencyClockStatus(symbol, event):
    clock0 = bool(Database.getSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL0_CLOCK_ENABLE"))
    clock1 = bool(Database.getSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL1_CLOCK_ENABLE"))
    clock2 = bool(Database.getSymbolValue("core", tcInstanceName.getValue() + "_CHANNEL2_CLOCK_ENABLE"))
    if(tcSym_CH_EnableQEI.getValue() == True):
        if (clock0 == False):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

        if(tcSym_CH_QEI_INDEX_PULSE.getValue() == True and clock1 == False):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

        if(tcSym_CH_BMR_POSEN.getValue() == "SPEED" and clock2 == False):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def tcQEIDependencyIntStatus(symbol, event):
    interruptVectorUpdate = tcInstanceName.getValue() + "_CH0_INTERRUPT_ENABLE_UPDATE"
    nvic = bool(Database.getSymbolValue("core", interruptVectorUpdate))
    if(tcSym_CH_EnableQEI.getValue() == True):
        if (nvic == True and (tcSym_CH_QIER_IDX.getValue() == True or tcSym_CH_QIER_QERR.getValue() == True or tcSym_CH_QEI_IER_CPCS == True)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def tcGetClockResolution(clockSource, channelID):
    resolution_nS = str(1000000000.0/Database.getSymbolValue("core", "TC"+str(num)+"_CH"+str(channelID)+"_CLOCK_FREQUENCY"))
    global tcSym_CH_EXT_CLOCK
    ext_clock_Hz = tcSym_CH_EXT_CLOCK[channelID].getValue()
    if (ext_clock_Hz == 0):
        Log.writeErrorMessage("External clock frequency is zero")
        ext_clock_Hz = 1
    if (clockSource > 5):
        resolution_nS = str(1000000000.0/ext_clock_Hz)
    return resolution_nS

def tcClockFreq(tcSym_CH_ClockFreqLocal, event):
    id = tcSym_CH_ClockFreqLocal.getID()
    channelID = int(id[2])
    clock_Hz = int(Database.getSymbolValue("core", "TC"+str(num)+"_CH"+str(channelID)+"_CLOCK_FREQUENCY"))
    global tcSym_CH_EXT_CLOCK
    clock = (int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))
    if (clock > 5):
        clock_Hz = (tcSym_CH_EXT_CLOCK[channelID].getValue())
    tcSym_CH_CLOCK_FREQ[channelID].clearValue()
    tcSym_CH_ClockFreqLocal.setValue(int(clock_Hz), 2)

def tcClockResCalc(tcSym_CH_ResolutionLocal, event):
    id = tcSym_CH_ResolutionLocal.getID()
    channelID = int(id[2])
    resolution = None
    clock = Database.getSymbolValue("tc" + str(num), "TC"+str(channelID)+"_CMR_TCCLKS")
    resolution = tcGetClockResolution(clock, channelID)
    tcSym_CH_Resolution[channelID].setLabel("****Clock resolution is " + str(resolution) + " nS****")

def tcExtClockVisible(tcSym_CH_Ext_ClockLocal, event):
    id = tcSym_CH_Ext_ClockLocal.getID()
    channelID = int(id[2])
    source = tcSym_CH_CMR_TCCLKS[channelID].getSelectedKey()
    if(source == "XC0" or source == "XC1" or source == "XC2"):
        tcSym_CH_EXT_CLOCK[channelID].setVisible(True)
    else:
        tcSym_CH_EXT_CLOCK[channelID].setVisible(False)

def tcPCK7Set(tcSym_CH_PCK7Local, event):
    id = tcSym_CH_PCK7Local.getID()
    channelID = int(id[2])
    source = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))
    if (source == "PCK"):
        if (tcSym_CH_PCK_CLKSRC.getValue() == "PCK7"):
            tcSym_CH_PCK7[channelID].clearValue()
            tcSym_CH_PCK7[channelID].setValue(True, 1)
        elif (tcSym_CH_PCK_CLKSRC.getValue() == "PCK6"):
            tcSym_CH_PCK7[channelID].clearValue()
            tcSym_CH_PCK7[channelID].setValue(False, 1)
        else:
            tcSym_CH_PCK7[channelID].clearValue()
            tcSym_CH_PCK7[channelID].setValue(False, 1)

def tcTimerVisible(tcTimerMenuLocal, event):
    id = tcTimerMenuLocal.getID()
    channelID = int(id[2])
    if(event["value"] == "TIMER"):
        tcTimerMenu[channelID].setVisible(True)
    else:
        tcTimerMenu[channelID].setVisible(False)

def tcCaptureVisible(tcCaptureMenuLocal, event):
    id = tcCaptureMenuLocal.getID()
    channelID = int(id[2])
    if(event["value"] == "CAPTURE"):
        tcCaptureMenu[channelID].setVisible(True)
    else:
        tcCaptureMenu[channelID].setVisible(False)

#Business logic to restrict the external reset edge
#if external reset signal is TIOA then load A edge and external reset edge should NOT be same.
def tcCaptureEdgeSelect(tcSym_CH_CMR_ETRGEDGLocal, event):
    global tcSym_CH_CMR_LDRA
    global tcSym_CH_CAPTURE_EXT_RESET
    global tcSym_CH_CMR_ABETRG
    global tcSym_CH_CMR_ETRGEDG
    id = tcSym_CH_CMR_ETRGEDGLocal.getID()
    channelID = int(id[2])
    edgeA = tcSym_CH_CMR_LDRA[channelID].getValue()
    extReset = tcSym_CH_CAPTURE_EXT_RESET[channelID].getValue()
    extResetInput = tcSym_CH_CMR_ABETRG[channelID].getValue()
    extResetEdge = tcSym_CH_CMR_ETRGEDG[channelID].getValue()
    if ((extReset == True) and (extResetInput == "TIOA")):
        if (((edgeA == "RISING") and (extResetEdge == "RISING")) or ((edgeA == "FALLING") and (extResetEdge == "FALLING"))):
            tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(True)
        else:
            tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)
    else:
        tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)

def tcCompareVisible(tcCompareMenuLocal, event):
    id = tcCompareMenuLocal.getID()
    channelID = int(id[2])
    if(event["value"] == "COMPARE"):
        tcCompareMenu[channelID].setVisible(True)
    else:
        tcCompareMenu[channelID].setVisible(False)

def tcPeriodCalc(tcSym_CH_ComparePeriodLocal, event):
    global tcSym_CH_CMR_TCCLKS
    global tcSym_CH_TimerPeriodCount
    global tcSym_CH_ComparePeriodCount
    global tcSym_CH_OperatingMode
    count = 1

    id = tcSym_CH_ComparePeriodLocal.getID()
    channelID = int(id[2])
    clock = Database.getSymbolValue("tc" + str(num), "TC"+str(channelID)+"_CMR_TCCLKS")
    mode = tcSym_CH_OperatingMode[channelID].getValue()
    if(mode == "COMPARE"):
        count = tcSym_CH_ComparePeriodCount[channelID].getValue()

    resolution_ns = tcGetClockResolution(clock, channelID)
    time_us = float(resolution_ns) * int(count) / 1000.0;

    if(mode == "COMPARE"):
        tcSym_CH_ComparePeriod[channelID].setLabel("****Waveform period is " + str(time_us) + " uS****")

def tcPeriodCountCalc(symbol, event):
    global tcSym_CH_CMR_TCCLKS
    global tcSym_CH_ComparePeriodCount
    global tcSym_CH_OperatingMode
    global tcSym_CH_TimerPeriod
    global tcSym_CH_TimerPeriodCount
    time = 1.0

    id = symbol.getID()
    channelID = int(id[2])
    clock = Database.getSymbolValue("tc" + str(num), "TC"+str(channelID)+"_CMR_TCCLKS")
    mode = tcSym_CH_OperatingMode[channelID].getValue()

    if (mode == "TIMER"):
        time = tcSym_CH_TimerPeriod[channelID].getValue()

    resolution_ns = tcGetClockResolution(clock, channelID)
    if (float(resolution_ns) == 0.0):
        resolution_ns = 1
    time_period = int((time * 1000000.0 / float(resolution_ns)))

    if (mode == "TIMER"):
        if (time_period > 65535):
            tcSym_CH_TimerPeriodComment[channelID].setLabel("****Period Count is > 65535. Reduce timer period ****")
        else:
            tcSym_CH_TimerPeriodComment[channelID].setLabel("****Period Count is " + str(time_period) + "****")
        tcSym_CH_TimerPeriodCount[channelID].clearValue()
        tcSym_CH_TimerPeriodCount[channelID].setValue(int(time_period), 2)

def tcPeriodMaxVal(symbol, event):
    id = symbol.getID()
    channelID = int(id[2])
    clock = Database.getSymbolValue("tc" + str(num), "TC"+str(channelID)+"_CMR_TCCLKS")
    resolution_ns = tcGetClockResolution(clock, channelID)
    symbol.setMax(float(((float(resolution_ns) * 65535.0)/1000000)))

def tcCompareMaxCalc(tcCompare, event):
    id = tcCompare.getID()
    channelID = int(id[2])
    tcCompare.setMax(event["value"])

def tcWaveformBVisible(tcWaveformB, event):
    id = tcWaveformB.getID()
    channelID = int(id[2])
    symObj = event["symbol"]
    input = symObj.getSelectedKey()
    if (input == "TIOB"):
        tcCompareBMenu[channelID].setVisible(False)
    else:
        tcCompareBMenu[channelID].setVisible(True)

def tcActionExtEvtVisible(actionExtEvt, event):
    id = actionExtEvt.getID()
    channelID = int(id[2])

    if (event["value"] != "NONE"):
        if(actionExtEvt.getID().find("AEEVT") > 0):
            tcSym_CH_CMR_AEEVT[channelID].setVisible(True)
        else:
            tcSym_CH_CMR_BEEVT[channelID].setVisible(True)
    else:
        if(actionExtEvt.getID().find("AEEVT") > 0):
            tcSym_CH_CMR_AEEVT[channelID].setVisible(False)
        else:
            tcSym_CH_CMR_BEEVT[channelID].setVisible(False)

def tcQuadratureVisible(tcQuadratureMenu, event):
    if(event["value"] == True):
        tcQuadratureMenu.setVisible(True)
    else:
        tcQuadratureMenu.setVisible(False)

def tcChannelMenuVisible(tcchannelMenu, event):
    global tcSym_CH_BMR_POSEN
    global tcSym_CH_EnableQEI
    if(tcSym_CH_EnableQEI.getValue() == True):
        tcChannelMenu[0].setVisible(False)
        if (tcSym_CH_QEI_INDEX_PULSE.getValue() == True):
            tcChannelMenu[1].setVisible(False)
        else:
            tcChannelMenu[1].setVisible(True)

        if (tcSym_CH_BMR_POSEN.getValue() == "SPEED"):
            tcChannelMenu[2].setVisible(False)
        else:
            tcChannelMenu[2].setVisible(True)
    else:
        tcChannelMenu[0].setVisible(True)
        tcChannelMenu[1].setVisible(True)
        tcChannelMenu[2].setVisible(True)

def tcQuadratureModeVisible(tcSpeedMenu, event):
    if(event["value"] == "SPEED"):
        tcSpeedMenu.setVisible(True)
    else:
        tcSpeedMenu.setVisible(False)

def tcQuadraturePositionVisible(symbol, event):
    if (tcSym_CH_BMR_POSEN.getValue() == "POSITION" and tcSym_CH_QEI_INDEX_PULSE.getValue() == False):
        tcPositionMenu.setVisible(True)
    else:
        tcPositionMenu.setVisible(False)

def tcQuadratureTimeBaseCalculate(tcSym_CH_QEI_CH2PERIOD_COMMENT, event):
    global tcSym_CH_CMR_TCCLKS
    global tcSym_CH_QEI_CH2PERIOD
    channelID = 3
    clock = Database.getSymbolValue("tc" + str(num), "TC"+str(channelID)+"_CMR_TCCLKS")
    count = tcSym_CH_QEI_CH2PERIOD.getValue()

    resolution_ns = tcGetClockResolution(clock, 3)
    time_us = float(resolution_ns) * int(count) / 1000.0

    tcSym_CH_QEI_CH2PERIOD_COMMENT.setLabel("****Time Base is " + str(time_us) + " uS****")

def tcQuadratureIndexPulse(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcQuadratureCommentChange(tcQuadratureComment, event):
    if (tcSym_CH_BMR_POSEN.getValue() == "POSITION"):
        if (tcSym_CH_QEI_INDEX_PULSE.getValue() == True):
            tcQuadratureComment.setLabel("**** Quadrature mode uses two channels. Channel 0 to capture number of edges and Channel 1 to capture number of revolutions ****")
        else:
            tcQuadratureComment.setLabel("**** Quadrature mode uses one channel. Channel 0 to capture number of edges ****")
    else:
        if (tcSym_CH_QEI_INDEX_PULSE.getValue() == True):
            tcQuadratureComment.setLabel("**** Quadrature mode uses three channels. Channel 0 and Channel 2 to capture speed and Channel 1 to capture number of revolutions ****")
        else:
            tcQuadratureComment.setLabel("**** Quadrature mode uses two channels. Channel 0 and Channel 2 to capture speed ****")

def tcPCKVisible(symbol, event):
    clock0 = tcSym_CH_CMR_TCCLKS[0].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[0].getSelectedValue()))
    clock1 = tcSym_CH_CMR_TCCLKS[1].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[1].getSelectedValue()))
    clock2 = tcSym_CH_CMR_TCCLKS[2].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[2].getSelectedValue()))
    if (clock0 == "PCK" or clock1 == "PCK" or clock2 == "PCK"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcClockSymbols(tcComponent, channelID, menu):
    #clock selection
    #Added keys here as this symbol combines two bit-fields CMR_TCCLKS and EMR_NODIVCLK
    global tcSym_CH_CMR_TCCLKS
    i = 0 #value of the key. As keys are added conditionally, incrementing value with variable i
    tcSym_CH_CMR_TCCLKS[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_TCCLKS", menu)
    tcSym_CH_CMR_TCCLKS[channelID].setLabel("Select Clock Source")
    tcSym_CH_CMR_TCCLKS[channelID].addKey("", str(i), "MCK")

    childrenNodes = []
    tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__TCCLKS\"]")
    childrenNodes = tc.getChildren()

    if (int(tcInstanceName.getValue().split("TC")[1]) == 0):
        tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK1", str(i + 1), "PCK")
    else:
        tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK1", str(i + 1), "PCK6")
    i = i + 1
    for param in range(1, len(childrenNodes)):
        if (childrenNodes[param].getAttribute("name") == "XC0"):
            if (extClock[0] == True):
                tcSym_CH_CMR_TCCLKS[channelID].addKey(childrenNodes[param].getAttribute("name"), str(i + param), \
                    childrenNodes[param].getAttribute("caption"))
        elif (childrenNodes[param].getAttribute("name") == "XC1"):
            if (extClock[1] == True):
                tcSym_CH_CMR_TCCLKS[channelID].addKey(childrenNodes[param].getAttribute("name"), str(i + param), \
                    childrenNodes[param].getAttribute("caption"))
        elif (childrenNodes[param].getAttribute("name") == "XC2"):
            if (extClock[2] == True):
                tcSym_CH_CMR_TCCLKS[channelID].addKey(childrenNodes[param].getAttribute("name"), str(i + param), \
                    childrenNodes[param].getAttribute("caption"))
        else:
            tcSym_CH_CMR_TCCLKS[channelID].addKey(childrenNodes[param].getAttribute("name"), str(i + param), \
                childrenNodes[param].getAttribute("caption"))
    tcSym_CH_CMR_TCCLKS[channelID].setDefaultValue(0)
    tcSym_CH_CMR_TCCLKS[channelID].setOutputMode("Key")
    tcSym_CH_CMR_TCCLKS[channelID].setDisplayMode("Description")

    #PCK7 and also enable clock PCK6 or PCK7
    tcSym_CH_PCK7[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_PCK7", menu)
    tcSym_CH_PCK7[channelID].setLabel("PCK7")
    tcSym_CH_PCK7[channelID].setVisible(False)
    tcSym_CH_PCK7[channelID].setDefaultValue(False)
    tcSym_CH_PCK7[channelID].setDependencies(tcPCK7Set, ["TC"+str(channelID)+"_CMR_TCCLKS", "TC_PCK_CLKSRC"])

    #external clock frequency
    global tcSym_CH_EXT_CLOCK
    tcSym_CH_EXT_CLOCK[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_EXT_CLOCK", menu)
    tcSym_CH_EXT_CLOCK[channelID].setLabel("External Clock Frequency (Hz)")
    tcSym_CH_EXT_CLOCK[channelID].setVisible(False)
    tcSym_CH_EXT_CLOCK[channelID].setDefaultValue(50000000)
    tcSym_CH_EXT_CLOCK[channelID].setMin (1)
    tcSym_CH_EXT_CLOCK[channelID].setDependencies(tcExtClockVisible, ["TC"+str(channelID)+"_CMR_TCCLKS"])

    #Save clock frequency
    tcSym_CH_CLOCK_FREQ[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_CLOCK_FREQ", menu)
    tcSym_CH_CLOCK_FREQ[channelID].setLabel("Clock Frequency (Hz)")
    tcSym_CH_CLOCK_FREQ[channelID].setVisible(False)
    tcSym_CH_CLOCK_FREQ[channelID].setDefaultValue(150000000)
    tcSym_CH_CLOCK_FREQ[channelID].setDependencies(tcClockFreq, ["TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
        "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC"])

    #clock resolution display
    tcSym_CH_Resolution[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_Resolution", menu)
    tcSym_CH_Resolution[channelID].setLabel("****Timer resolution is " + str(6.66) + " nS****")
    tcSym_CH_Resolution[channelID].setDependencies(tcClockResCalc, ["TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
        "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC"])

def onCapabilityConnected(connectionInfo):
    global sysTimeChannel_Sym

    remoteComponent = connectionInfo["remoteComponent"]
    if (remoteComponent.getID() == "sys_time"):
        sysTimeChannel_Sym.setSelectedKey("_CH0",1)
        sysTimeChannel_Sym.setVisible(True)

def onCapabilityDisconnected(connectionInfo):
    global sysTimeChannel_Sym

    tcSym_CH_TimerPeriod[0].setVisible(True)
    tcSym_CH_TimerPeriod[1].setVisible(True)
    tcSym_CH_TimerPeriod[2].setVisible(True)

    remoteComponent = connectionInfo["remoteComponent"]
    if (remoteComponent.getID() == "sys_time"):
        sysTimeChannel_Sym.setVisible(False)


def sysTime_ChannelSelection(symbol,event):
    global timerStartApiName_Sym
    global timeStopApiName_Sym
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global frequencyGetApiName_Sym
    global callbackApiName_Sym
    global irqEnumName_Sym
    global tcInstanceName


    symObj=event["symbol"]
    tc_channel = symObj.getSelectedKey()

    channelID = int(tc_channel[3])

    tcSym_CH_Enable[channelID].setValue(True,2)
    tcSym_CH_IER_CPAS[channelID].setValue(True,2)
    tcSym_CH_IER_CPCS[channelID].setValue(False,2)

    tcSym_CH_TimerPeriod[channelID].setVisible(False)

    if(channelID==0):
        tcSym_CH_TimerPeriod[1].setVisible(True)
        tcSym_CH_TimerPeriod[2].setVisible(True)
        tcSym_CH_Enable[1].setValue(False,2)
        tcSym_CH_Enable[2].setValue(False,2)
    elif(channelID==1):
        tcSym_CH_TimerPeriod[0].setVisible(True)
        tcSym_CH_TimerPeriod[2].setVisible(True)
        tcSym_CH_Enable[0].setValue(False,2)
        tcSym_CH_Enable[2].setValue(False,2)
    elif(channelID==2):
        tcSym_CH_TimerPeriod[0].setVisible(True)
        tcSym_CH_TimerPeriod[1].setVisible(True)
        tcSym_CH_Enable[0].setValue(False,2)
        tcSym_CH_Enable[1].setValue(False,2)

    timerStartApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerStart"
    timeStopApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerStop "
    compareSetApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerCompareSet"
    counterGetApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerCounterGet"
    frequencyGetApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerFrequencyGet"
    callbackApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerCallbackRegister"
    irqEnumName = tcInstanceName.getValue() + str(tc_channel) + "_IRQn"
    periodSetApiName = tcInstanceName.getValue() + str(tc_channel) + "_TimerPeriodSet"

    timerStartApiName_Sym.setValue(timerStartApiName,2)
    timeStopApiName_Sym.setValue(timeStopApiName,2)
    compareSetApiName_Sym.setValue(compareSetApiName,2)
    counterApiName_Sym.setValue(counterGetApiName,2)
    frequencyGetApiName_Sym.setValue(frequencyGetApiName,2)
    callbackApiName_Sym.setValue(callbackApiName,2)
    irqEnumName_Sym.setValue(irqEnumName,2)
    periodSetApiName_Sym.setValue(periodSetApiName,2)


###################################################################################################
########################### Instantiation   #################################
###################################################################################################
def instantiateComponent(tcComponent):
    global timerStartApiName_Sym
    global timeStopApiName_Sym
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global frequencyGetApiName_Sym
    global callbackApiName_Sym
    global irqEnumName_Sym
    global sysTimeChannel_Sym
    global tcInstanceName

    tcInstanceName = tcComponent.createStringSymbol("TC_INSTANCE_NAME", None)
    tcInstanceName.setVisible(False)
    tcInstanceName.setDefaultValue(tcComponent.getID().upper())
    print("Running " + tcInstanceName.getValue())

    tcSym_MAX_CHANNELS = tcComponent.createIntegerSymbol("TC_MAX_CHANNELS", None)
    tcSym_MAX_CHANNELS.setDefaultValue(3)
    tcSym_MAX_CHANNELS.setVisible(False)
    
    tcSym_MCU_SERIES = tcComponent.createStringSymbol("TC_MCU_SERIES", None)
    tcSym_MCU_SERIES.setVisible(False)
    node = ATDF.getNode("/avr-tools-device-file/devices")
    series = node.getChildren()[0].getAttribute("series")
    tcSym_MCU_SERIES.setDefaultValue(node.getChildren()[0].getAttribute("series"))

    #*********** Restrict the channel mode as per ATDF file **************************
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []        # array to save available pins
    channel = [False, False, False] #array to save available channels
    global extClock
    extClock = [False, False, False] #array to save if ext clock pin is available

    # Save pins in availablePins array as per selected package
    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(packageName)+"\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    #Find available channels and available external clock pins
    tc_signals = []
    tc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+tcInstanceName.getValue()+"\"]/signals")
    tc_signals = tc.getChildren()
    for pad in range(0, len(tc_signals)):
        if "TIOA" in tc_signals[pad].getAttribute("group"):
            padSignal = tc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(tc_signals[pad].getAttribute("index"))%3] = True
            else:
                channel[int(tc_signals[pad].getAttribute("index"))%3] = False
        if "TCLK" in tc_signals[pad].getAttribute("group"):
            padSignal = tc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                extClock[int(tc_signals[pad].getAttribute("index"))%3] = True
            else:
                extClock[int(tc_signals[pad].getAttribute("index"))%3] = False


    sysTimeTrigger_Sym = tcComponent.createBooleanSymbol("SYS_TIME", None)
    sysTimeTrigger_Sym.setVisible(False)
    sysTimeTrigger_Sym.setDependencies(sysTime_ChannelSelection, ["SYS_TIME_TC_CHANNEL"])

    sysTimeChannel_Sym = tcComponent.createKeyValueSetSymbol("SYS_TIME_TC_CHANNEL", None)
    sysTimeChannel_Sym.setLabel("Select TC Channel for Time System Service")
    sysTimeChannel_Sym.addKey("_CH0", "0", "Channel 0")
    sysTimeChannel_Sym.addKey("_CH1", "1", "Channel 1")
    sysTimeChannel_Sym.addKey("_CH2", "2", "Channel 2")
    sysTimeChannel_Sym.setOutputMode("Key")
    sysTimeChannel_Sym.setDisplayMode("Description")
    sysTimeChannel_Sym.setDefaultValue(0)
    sysTimeChannel_Sym.setVisible(False)

#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------
    timerWidth_Sym = tcComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(16)

    timerPeriodMax_Sym = tcComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFF")

    timerStartApiName_Sym = tcComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)

    timeStopApiName_Sym = tcComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)

    compareSetApiName_Sym = tcComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiName_Sym.setVisible(False)

    periodSetApiName_Sym = tcComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)

    counterApiName_Sym = tcComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)

    frequencyGetApiName_Sym = tcComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)

    callbackApiName_Sym = tcComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)

    irqEnumName_Sym = tcComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
#------------------------------------------------------------


    #*****************************QUADRATURE******************************
    #channel enable
    global tcSym_CH_EnableQEI
    tcSym_CH_EnableQEI = tcComponent.createBooleanSymbol("TC_ENABLE_QEI", None)
    tcSym_CH_EnableQEI.setLabel("Enable Quadrature Encoder Mode")
    tcSym_CH_EnableQEI.setDefaultValue(False)
    #Quadrature interface is not available if channel 0 and channel 1 pins are not available
    if (channel[0] == True and channel[1] == True):
        tcSym_CH_EnableQEI.setVisible(True)
    else:
        tcSym_CH_EnableQEI.setVisible(False)

    # Dependency Status
    tcSym_QEI_ClkEnComment = tcComponent.createCommentSymbol("TC_CLK_ENABLE_COMMENT", tcSym_CH_EnableQEI)
    tcSym_QEI_ClkEnComment.setVisible(False)
    tcSym_QEI_ClkEnComment.setLabel("Warning!!! " + tcInstanceName.getValue() + " Channel Peripheral Clock is Disabled in Clock Manager")
    tcSym_QEI_ClkEnComment.setDependencies(tcQEIDependencyClockStatus, ["core." +  tcInstanceName.getValue()  + "_CHANNEL0_CLOCK_ENABLE", \
        "core." + tcInstanceName.getValue() + "_CHANNEL1_CLOCK_ENABLE", "core." + tcInstanceName.getValue() + "_CHANNEL2_CLOCK_ENABLE", "TC_ENABLE_QEI", "TC_BMR_POSEN", "TC_INDEX_PULSE"])

    interruptVectorUpdate = tcInstanceName.getValue() + "_CH0_INTERRUPT_ENABLE_UPDATE"
    tcSym_QEI_IntEnComment = tcComponent.createCommentSymbol("TC_NVIC_ENABLE_COMMENT", tcSym_CH_EnableQEI)
    tcSym_QEI_IntEnComment.setVisible(False)
    tcSym_QEI_IntEnComment.setLabel("Warning!!! " +tcInstanceName.getValue()+"_CH0 Interrupt is Disabled in Interrupt Manager")
    tcSym_QEI_IntEnComment.setDependencies(tcQEIDependencyIntStatus, ["core." + interruptVectorUpdate, "TC_ENABLE_QEI", "TC_QIER_IDX", "TC_QIER_QERR", "TC_QEI_IER_CPCS"])

    #quadrature menu
    tcQuadratureMenu = tcComponent.createMenuSymbol("TC_QUADRATURE", tcSym_CH_EnableQEI)
    tcQuadratureMenu.setLabel("Quadrature")
    tcQuadratureMenu.setVisible(False)
    tcQuadratureMenu.setDependencies(tcQuadratureVisible, ["TC_ENABLE_QEI"])

    tcQuadratureComment = tcComponent.createCommentSymbol("TC_QUADRATURE_COMMENT", tcQuadratureMenu)
    tcQuadratureComment.setLabel("**** Quadrature mode uses two channels. Channel 0 to capture number of edges and Channel 1 to capture number of revolutions ****")
    tcQuadratureComment.setDependencies(tcQuadratureCommentChange, ["TC_BMR_POSEN", "TC_INDEX_PULSE"])

    # Swap PhA and PhB
    tcSym_CH_QEI_BMR_SWAP = tcComponent.createBooleanSymbol("TC_BMR_SWAP", tcQuadratureMenu)
    tcSym_CH_QEI_BMR_SWAP.setLabel("Swap Phase A and Phase B Signals")
    tcSym_CH_QEI_BMR_SWAP.setDefaultValue(False)

    # Filter value
    tcSym_CH_BMR_MAXFILT = tcComponent.createIntegerSymbol("TC_BMR_MAXFILT", tcQuadratureMenu)
    tcSym_CH_BMR_MAXFILT.setLabel("Select Input Signal Filter Count")
    tcSym_CH_BMR_MAXFILT.setDefaultValue(2)
    tcSym_CH_BMR_MAXFILT.setMin(0)
    tcSym_CH_BMR_MAXFILT.setMax(63)

    # Index pulse
    global tcSym_CH_QEI_INDEX_PULSE
    tcSym_CH_QEI_INDEX_PULSE = tcComponent.createBooleanSymbol("TC_INDEX_PULSE", tcQuadratureMenu)
    tcSym_CH_QEI_INDEX_PULSE.setLabel("Is Index Pulse Available?")
    tcSym_CH_QEI_INDEX_PULSE.setDefaultValue(True)

    #Mode
    global tcSym_CH_BMR_POSEN
    tcSym_CH_BMR_POSEN = tcComponent.createComboSymbol("TC_BMR_POSEN", tcQuadratureMenu, ["POSITION", "SPEED"])
    tcSym_CH_BMR_POSEN.setLabel("Select Mode")
    tcSym_CH_BMR_POSEN.setDefaultValue("POSITION")

    #position menu
    global tcPositionMenu
    tcPositionMenu = tcComponent.createMenuSymbol("TC_QUADRATURE_POSITION", tcSym_CH_BMR_POSEN)
    tcPositionMenu.setLabel("Position Measurement")
    tcPositionMenu.setVisible(False)
    tcPositionMenu.setDependencies(tcQuadraturePositionVisible, ["TC_BMR_POSEN", "TC_INDEX_PULSE"])

    #Num pulses
    tcSym_CH_QEI_NUM_PULSES = tcComponent.createIntegerSymbol("TC_QEI_NUM_PULSES", tcPositionMenu)
    tcSym_CH_QEI_NUM_PULSES.setLabel("Number of Quadrature Pulses per Revolution")
    tcSym_CH_QEI_NUM_PULSES.setDefaultValue(1024)
    tcSym_CH_QEI_NUM_PULSES.setMin(0)
    tcSym_CH_QEI_NUM_PULSES.setMax(65535)

    #Position reset interrupt
    global tcSym_CH_QEI_IER_CPCS
    tcSym_CH_QEI_IER_CPCS = tcComponent.createBooleanSymbol("TC_QEI_IER_CPCS", tcPositionMenu)
    tcSym_CH_QEI_IER_CPCS.setLabel("Enable Period Interrupt")
    tcSym_CH_QEI_IER_CPCS.setDefaultValue(False)

    #speed menu
    tcSpeedMenu = tcComponent.createMenuSymbol("TC_QUADRATURE_SPEED", tcSym_CH_BMR_POSEN)
    tcSpeedMenu.setLabel("Speed Measurement")
    tcSpeedMenu.setVisible(False)
    tcSpeedMenu.setDependencies(tcQuadratureModeVisible, ["TC_BMR_POSEN"])

    # clock selection for channel 2. For quadrature mode, channel ID 3 is used to distinguish between channel numbers and quadrature mode
    tcClockSymbols(tcComponent, 3, tcSpeedMenu)

    # CH2 time period
    global tcSym_CH_QEI_CH2PERIOD
    tcSym_CH_QEI_CH2PERIOD = tcComponent.createIntegerSymbol("TC_QEI_PERIOD", tcSpeedMenu)
    tcSym_CH_QEI_CH2PERIOD.setLabel("Select Speed Time Base")
    tcSym_CH_QEI_CH2PERIOD.setDefaultValue(15015)

    # CH2 time in us comment
    tcSym_CH_QEI_CH2PERIOD_COMMENT = tcComponent.createCommentSymbol("TC_QEI_PERIOD_COMMENT", tcSpeedMenu)
    tcSym_CH_QEI_CH2PERIOD_COMMENT.setLabel("**** Time Base is 100 uS  ****")
    tcSym_CH_QEI_CH2PERIOD_COMMENT.setDependencies(tcQuadratureTimeBaseCalculate, ["TC_QEI_PERIOD", "TC3_CMR_TCCLKS", \
        "core."+tcInstanceName.getValue()+"_CH3_CLOCK_FREQUENCY"])

    # enable index interrupt
    global tcSym_CH_QIER_IDX
    tcSym_CH_QIER_IDX = tcComponent.createBooleanSymbol("TC_QIER_IDX", tcQuadratureMenu)
    tcSym_CH_QIER_IDX.setLabel("Enable Index Interrupt")
    tcSym_CH_QIER_IDX.setDefaultValue(False)
    tcSym_CH_QIER_IDX.setDependencies(tcQuadratureIndexPulse, ["TC_INDEX_PULSE"])

    # enable quadrature error interrupt
    global tcSym_CH_QIER_QERR
    tcSym_CH_QIER_QERR = tcComponent.createBooleanSymbol("TC_QIER_QERR", tcQuadratureMenu)
    tcSym_CH_QIER_QERR.setLabel("Enable Quadrature Error Interrupt")
    tcSym_CH_QIER_QERR.setDefaultValue(False)

    #combo box to select PCK source only visible for TC0
    global tcSym_CH_PCK_CLKSRC
    tcSym_CH_PCK_CLKSRC = tcComponent.createComboSymbol("TC_PCK_CLKSRC", None, ["PCK6", "PCK7"])
    tcSym_CH_PCK_CLKSRC.setLabel("Select PCK Clock Source")
    tcSym_CH_PCK_CLKSRC.setDefaultValue("PCK6")
    tcSym_CH_PCK_CLKSRC.setVisible(False)
    tcSym_CH_PCK_CLKSRC.setDependencies(tcPCKVisible, ["TC0_CMR_TCCLKS", "TC1_CMR_TCCLKS", "TC2_CMR_TCCLKS"])

    #*************************CHANNEL CONFIGURATIONS ******************************
    for channelID in range(0, len(channel)):
        #channel menu
        tcChannelMenu.append(channelID)
        tcChannelMenu[channelID] = tcComponent.createMenuSymbol("Channel "+str(channelID), None)
        tcChannelMenu[channelID].setLabel("Channel "+str(channelID))
        tcChannelMenu[channelID].setDependencies(tcChannelMenuVisible, ["TC_ENABLE_QEI", "TC_BMR_POSEN", "TC_INDEX_PULSE"])

        #channel enable
        tcSym_CH_Enable.append(channelID)
        tcSym_CH_Enable[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_ENABLE", tcChannelMenu[channelID])
        tcSym_CH_Enable[channelID].setLabel("Enable")
        tcSym_CH_Enable[channelID].setDefaultValue(False)

        ############################################################################
        #### Dependency ####
        ############################################################################
        # Clock dynamic settings
        tcSym_CH_ClockControl.append(channelID)
        tcSym_CH_ClockControl[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CLOCK_ENABLE", None)
        tcSym_CH_ClockControl[channelID].setDependencies(tcClockControl, ["TC"+str(channelID)+"_ENABLE", "TC_ENABLE_QEI", "TC_BMR_POSEN", "TC_INDEX_PULSE"])
        tcSym_CH_ClockControl[channelID].setVisible(False)

        # NVIC Dynamic settings
        tcSym_CH_interruptControl.append(channelID)
        tcSym_CH_interruptControl[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_NVIC_ENABLE", None)
        tcSym_CH_interruptControl[channelID].setDependencies(tcinterruptControl, ["TC"+str(channelID)+"_ENABLE", "TC_ENABLE_QEI", "TC"+str(channelID)+"_OPERATING_MODE", \
            "TC"+str(channelID)+"_CAPTURE_IER_LDRAS", "TC"+str(channelID)+"_CAPTURE_IER_LDRBS", "TC"+str(channelID)+"_CAPTURE_IER_COVFS", \
            "TC"+str(channelID)+"_COMPARE_IER_CPCS", "TC"+str(channelID)+"_IER_CPCS", "TC"+str(channelID)+"_IER_CPAS", "TC_QIER_IDX", "TC_QIER_QERR", "TC_INDEX_PULSE", "TC_QEI_IER_CPCS"])
        tcSym_CH_interruptControl[channelID].setVisible(False)

        # Dependency Status
        tcSym_CH_ClkEnComment.append(channelID)
        tcSym_CH_ClkEnComment[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CLK_ENABLE_COMMENT", tcChannelMenu[channelID])
        tcSym_CH_ClkEnComment[channelID].setVisible(False)
        tcSym_CH_ClkEnComment[channelID].setLabel("Warning!!! " +tcInstanceName.getValue()+"_CH"+str(channelID)+" Peripheral Clock is Disabled in Clock Manager")
        tcSym_CH_ClkEnComment[channelID].setDependencies(tcdependencyClockStatus, ["core." + tcInstanceName.getValue() + "_CHANNEL"+str(channelID) + "_CLOCK_ENABLE", "TC"+str(channelID)+"_ENABLE"])

        node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
        interrupts = node.getChildren()
        for interrupt in range(0, len(interrupts)):
            if "header:alternate-name" in interrupts[interrupt].getAttributeList():
                alternate_name = interrupts[interrupt].getAttribute("header:alternate-name")
                if ((tcInstanceName.getValue() + "_CH" + str(channelID)) == alternate_name):
                    channel_periphId[channelID] = interrupts[interrupt].getAttribute("index")

        interruptVectorUpdate = tcInstanceName.getValue() + "_CH" + str(channelID) + "_INTERRUPT_ENABLE_UPDATE"
        tcSym_CH_IntEnComment.append(channelID)
        tcSym_CH_IntEnComment[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_NVIC_ENABLE_COMMENT", tcChannelMenu[channelID])
        tcSym_CH_IntEnComment[channelID].setVisible(False)
        tcSym_CH_IntEnComment[channelID].setLabel("Warning!!! " +tcInstanceName.getValue()+"_CH"+str(channelID)+" Interrupt is Disabled in Interrupt Manager")
        tcSym_CH_IntEnComment[channelID].setDependencies(tcdependencyIntStatus, ["core." + interruptVectorUpdate, "TC"+str(channelID)+"_ENABLE", "TC"+str(channelID)+"_OPERATING_MODE", \
            "TC"+str(channelID)+"_CAPTURE_IER_LDRAS", "TC"+str(channelID)+"_CAPTURE_IER_LDRBS", "TC"+str(channelID)+"_CAPTURE_IER_COVFS", \
            "TC"+str(channelID)+"_COMPARE_IER_CPCS", "TC"+str(channelID)+"_IER_CPCS"])

        ############################################################################
        #### Dependency END ####
        ############################################################################

        #Clock symbols
        tcClockSymbols(tcComponent, channelID, tcSym_CH_Enable[channelID])

        if(channel[channelID] == True):
            tcModeValues = ["TIMER", "CAPTURE", "COMPARE"]
        else:
            tcModeValues = ["TIMER"]
        #operating mode
        tcSym_CH_OperatingMode.append(channelID)
        tcSym_CH_OperatingMode[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_OPERATING_MODE", tcSym_CH_Enable[channelID], tcModeValues)
        tcSym_CH_OperatingMode[channelID].setLabel("Operating Mode")
        tcSym_CH_OperatingMode[channelID].setDefaultValue("TIMER")

        #*****************************TIMER******************************
        #timer menu
        tcTimerMenu.append(channelID)
        tcTimerMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_TIMER", tcSym_CH_OperatingMode[channelID])
        tcTimerMenu[channelID].setLabel("Timer")
        tcTimerMenu[channelID].setDependencies(tcTimerVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])

        global tcSym_CH_TimerPeriod
        tcSym_CH_TimerPeriod.append(channelID)
        tcSym_CH_TimerPeriod[channelID] = tcComponent.createFloatSymbol("TC"+str(channelID)+"_TIMER_PERIOD_MS", tcTimerMenu[channelID])
        tcSym_CH_TimerPeriod[channelID].setLabel("Timer Period (Milli Sec)")
        tcSym_CH_TimerPeriod[channelID].setDefaultValue(0.4)
        tcSym_CH_TimerPeriod[channelID].setMin(0.0)
        #tcSym_CH_TimerPeriod[channelID].setMax(0.436)
        tcSym_CH_TimerPeriod[channelID].setDependencies(tcPeriodMaxVal, \
        ["TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
            "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC"])

        tcSym_CH_TimerPeriodComment.append(channelID)
        tcSym_CH_TimerPeriodComment[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_TIMER_PERIOD_CMT", tcTimerMenu[channelID])
        tcSym_CH_TimerPeriodComment[channelID].setLabel("**** Period Count is 60060 ****")
        tcSym_CH_TimerPeriodComment[channelID].setVisible(False)
        tcSym_CH_TimerPeriodComment[channelID].setDependencies(tcPeriodCountCalc, \
        ["TC"+str(channelID)+"_TIMER_PERIOD_MS", "TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
            "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC"])

        tcSym_CH_TimerPeriodCount.append(channelID)
        tcSym_CH_TimerPeriodCount[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_TIMER_PERIOD_COUNT", tcTimerMenu[channelID])
        tcSym_CH_TimerPeriodCount[channelID].setVisible(False)
        tcSym_CH_TimerPeriodCount[channelID].setDefaultValue(60000)
        tcSym_CH_TimerPeriodCount[channelID].setDependencies(tcPeriodCountCalc, \
        ["TC"+str(channelID)+"_TIMER_PERIOD_MS", "TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
            "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC", "TC"+str(channelID)+"_ENABLE"])

        #one-shot timer
        tcSym_CH_CMR_CPCSTOP.append(channelID)
        tcSym_CH_CMR_CPCSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CMR_CPCSTOP", tcTimerMenu[channelID])
        tcSym_CH_CMR_CPCSTOP[channelID].setLabel("Enable One Shot Mode")
        tcSym_CH_CMR_CPCSTOP[channelID].setDefaultValue(False)

        #period interrupt
        tcSym_CH_IER_CPCS.append(channelID)
        tcSym_CH_IER_CPCS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_IER_CPCS", tcTimerMenu[channelID])
        tcSym_CH_IER_CPCS[channelID].setLabel("Enable Period Interrupt")
        tcSym_CH_IER_CPCS[channelID].setDefaultValue(True)

        #compare interrupt
        tcSym_CH_IER_CPAS.append(channelID)
        tcSym_CH_IER_CPAS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_IER_CPAS", tcTimerMenu[channelID])
        tcSym_CH_IER_CPAS[channelID].setLabel("Enable Compare Interrupt")
        tcSym_CH_IER_CPAS[channelID].setDefaultValue(False)

        #****************************CAPTURE*****************************
        #capture menu
        tcCaptureMenu.append(channelID)
        tcCaptureMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_CAPTURE", tcSym_CH_OperatingMode[channelID])
        tcCaptureMenu[channelID].setLabel("Capture")
        tcCaptureMenu[channelID].setDependencies(tcCaptureVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])
        tcCaptureMenu[channelID].setVisible(False)

        #one-shot timer
        tcSym_CH_CAPTURE_CMR_LDBSTOP.append(channelID)
        tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_CMR_LDBSTOP", tcCaptureMenu[channelID])
        tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID].setLabel("Enable One Shot Mode")
        tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID].setDefaultValue(False)

        #edge for capture A
        global tcSym_CH_CMR_LDRA
        childrenNodes = []
        loadEdgeA = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__LDRA\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            loadEdgeA.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_LDRA.append(channelID)
        tcSym_CH_CMR_LDRA[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_LDRA", tcCaptureMenu[channelID], loadEdgeA)
        tcSym_CH_CMR_LDRA[channelID].setLabel("Select TIOA Input Edge for Capture A")
        tcSym_CH_CMR_LDRA[channelID].setDefaultValue(loadEdgeA[1])

        #edge for capture B
        childrenNodes = []
        loadEdgeB = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__LDRB\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            loadEdgeB.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_LDRB.append(channelID)
        tcSym_CH_CMR_LDRB[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_LDRB", tcCaptureMenu[channelID], loadEdgeB)
        tcSym_CH_CMR_LDRB[channelID].setLabel("Select TIOA Input Edge for Capture B")
        tcSym_CH_CMR_LDRB[channelID].setDefaultValue(loadEdgeB[2])

        #Capture external reset
        global tcSym_CH_CAPTURE_EXT_RESET
        tcSym_CH_CAPTURE_EXT_RESET.append(channelID)
        tcSym_CH_CAPTURE_EXT_RESET[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_EXT_RESET", tcCaptureMenu[channelID])
        tcSym_CH_CAPTURE_EXT_RESET[channelID].setLabel("Reset Timer on External Event")
        tcSym_CH_CAPTURE_EXT_RESET[channelID].setDefaultValue(True)

        #external event signal
        global tcSym_CH_CMR_ABETRG
        tcValGroup_ABETRG = ["TIOA", "TIOB"]
        tcSym_CH_CMR_ABETRG.append(channelID)
        tcSym_CH_CMR_ABETRG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ABETRG", tcSym_CH_CAPTURE_EXT_RESET[channelID], tcValGroup_ABETRG)
        tcSym_CH_CMR_ABETRG[channelID].setLabel("Select External Event Input")
        tcSym_CH_CMR_ABETRG[channelID].setDefaultValue("TIOA")

        #external event edge
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ETRGEDG\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_ETRGEDG.append(channelID)
        tcSym_CH_CMR_ETRGEDG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ETRGEDG", tcSym_CH_CAPTURE_EXT_RESET[channelID], comboOptions)
        tcSym_CH_CMR_ETRGEDG[channelID].setLabel("Select External Event Edge")
        tcSym_CH_CMR_ETRGEDG[channelID].setDefaultValue(comboOptions[2])

        #external event edge comment
        tcSym_CH_CMR_ETRGEDG_COMMENT.append(channelID)
        tcSym_CH_CMR_ETRGEDG_COMMENT[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CMR_ETRGEDG_COMMENT", tcSym_CH_CAPTURE_EXT_RESET[channelID])
        tcSym_CH_CMR_ETRGEDG_COMMENT[channelID].setLabel("** When 'external event input' is TIOA, 'external event edge' should NOT be same as 'capture A edge' **")

        #external event edge alert
        tcSym_CH_CMR_ETRGEDG_ALERT.append(channelID)
        tcSym_CH_CMR_ETRGEDG_ALERT[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CMR_ETRGEDG_ALERT", tcSym_CH_CAPTURE_EXT_RESET[channelID])
        tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setLabel("**** EXTRNAL EVENT EDGE IS SAME AS CAPTURE A EDGE ****")
        tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)
        tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setDependencies(tcCaptureEdgeSelect, ["TC"+str(channelID)+"_CMR_ETRGEDG", "TC"+str(channelID)+"_CAPTURE_EXT_RESET", "TC"+str(channelID)+"_CMR_ABETRG", "TC"+str(channelID)+"_CMR_LDRA"])

        #capture A interrupt
        tcSym_CH_CAPTURE_IER_LDRAS.append(channelID)
        tcSym_CH_CAPTURE_IER_LDRAS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_LDRAS", tcCaptureMenu[channelID])
        tcSym_CH_CAPTURE_IER_LDRAS[channelID].setLabel("Enable Capture A Interrupt")
        tcSym_CH_CAPTURE_IER_LDRAS[channelID].setDefaultValue(True)

        #capture B interrupt
        tcSym_CH_CAPTURE_IER_LDRBS.append(channelID)
        tcSym_CH_CAPTURE_IER_LDRBS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_LDRBS", tcCaptureMenu[channelID])
        tcSym_CH_CAPTURE_IER_LDRBS[channelID].setLabel("Enable Capture B Interrupt")
        tcSym_CH_CAPTURE_IER_LDRBS[channelID].setDefaultValue(False)

        #counter overflow interrupt
        tcSym_CH_CAPTURE_IER_COVFS.append(channelID)
        tcSym_CH_CAPTURE_IER_COVFS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_COVFS", tcCaptureMenu[channelID])
        tcSym_CH_CAPTURE_IER_COVFS[channelID].setLabel("Enable Counter Overflow Interrupt")
        tcSym_CH_CAPTURE_IER_COVFS[channelID].setDefaultValue(False)

        #***************************COMPARE*******************************
        #compare menu
        tcCompareMenu.append(channelID)
        tcCompareMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPARE", tcSym_CH_OperatingMode[channelID])
        tcCompareMenu[channelID].setLabel("Compare")
        tcCompareMenu[channelID].setDependencies(tcCompareVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])
        tcCompareMenu[channelID].setVisible(False)

        #waveform type
        tcSym_CH_CMR_WAVSEL.append(channelID)
        tcSym_CH_CMR_WAVSEL[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_WAVSEL", tcCompareMenu[channelID])
        tcSym_CH_CMR_WAVSEL[channelID].setLabel("Select Waveform Mode")
        tcSym_CH_CMR_WAVSEL[channelID].addKey("UP_RC", "0", "UP Count Mode")
        tcSym_CH_CMR_WAVSEL[channelID].addKey("UPDOWN_RC", "0", "UP and DOWN Count Mode")
        tcSym_CH_CMR_WAVSEL[channelID].setDefaultValue(0)
        tcSym_CH_CMR_WAVSEL[channelID].setDisplayMode("Description")
        tcSym_CH_CMR_WAVSEL[channelID].setOutputMode("Key")

        #one-shot timer
        tcSym_CH_COMPARE_CMR_CPCSTOP.append(channelID)
        tcSym_CH_COMPARE_CMR_CPCSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_COMPARE_CMR_CPCSTOP", tcCompareMenu[channelID])
        tcSym_CH_COMPARE_CMR_CPCSTOP[channelID].setLabel("Enable One Shot Mode")
        tcSym_CH_COMPARE_CMR_CPCSTOP[channelID].setDefaultValue(False)

        #period count
        global tcSym_CH_ComparePeriodCount
        tcSym_CH_ComparePeriodCount.append(channelID)
        tcSym_CH_ComparePeriodCount[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_PERIOD_COUNT", tcCompareMenu[channelID])
        tcSym_CH_ComparePeriodCount[channelID].setLabel("Period Value")
        tcSym_CH_ComparePeriodCount[channelID].setDefaultValue(10000)
        tcSym_CH_ComparePeriodCount[channelID].setMin(0)
        tcSym_CH_ComparePeriodCount[channelID].setMax(65535)

        #period time in uS
        tcSym_CH_ComparePeriod.append(channelID)
        tcSym_CH_ComparePeriod[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_COMPARE_PERIOD", tcCompareMenu[channelID])
        tcSym_CH_ComparePeriod[channelID].setLabel("****Timer Period is 66.6 uS****")
        tcSym_CH_ComparePeriod[channelID].setDependencies(tcPeriodCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT", "TC"+str(channelID)+"_CMR_TCCLKS", \
            "core."+tcInstanceName.getValue()+"_CH"+str(channelID)+"_CLOCK_FREQUENCY", "TC_PCK_CLKSRC"])

        #External Event Menu
        tcEventMenu.append(channelID)
        tcEventMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_EXT_EVENT", tcCompareMenu[channelID])
        tcEventMenu[channelID].setLabel("External Event Input Configuration")

        #external reset signal
        tcSym_CH_CMR_EEVT.append(channelID)
        tcSym_CH_CMR_EEVT[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_EEVT", tcEventMenu[channelID])
        tcSym_CH_CMR_EEVT[channelID].setLabel("Select External Event Input")
        childrenNodes = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__EEVT\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            tcSym_CH_CMR_EEVT[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        tcSym_CH_CMR_EEVT[channelID].setDefaultValue(1)
        tcSym_CH_CMR_EEVT[channelID].setDisplayMode("Description")
        tcSym_CH_CMR_EEVT[channelID].setOutputMode("Key")

        #External reset edge
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__EEVTEDG\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMP_CMR_ETRGEDG.append(channelID)
        tcSym_CH_CMP_CMR_ETRGEDG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMP_CMR_ETRGEDG", tcEventMenu[channelID], comboOptions)
        tcSym_CH_CMP_CMR_ETRGEDG[channelID].setLabel("Select External Event Edge")
        tcSym_CH_CMP_CMR_ETRGEDG[channelID].setDefaultValue(comboOptions[0])

        #Waveform A menu
        tcCompareAMenu.append(channelID)
        tcCompareAMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPAREA", tcCompareMenu[channelID])
        tcCompareAMenu[channelID].setLabel("Compare A Output (TIOA) Configuration")

        #compare A
        global tcSym_CH_CompareA
        tcSym_CH_CompareA.append(channelID)
        tcSym_CH_CompareA[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_A", tcCompareAMenu[channelID])
        tcSym_CH_CompareA[channelID].setLabel("Compare Value")
        tcSym_CH_CompareA[channelID].setDefaultValue(5000)
        tcSym_CH_CompareA[channelID].setMin(0)
        tcSym_CH_CompareA[channelID].setMax(tcSym_CH_ComparePeriodCount[channelID].getValue())
        tcSym_CH_CompareA[channelID].setDependencies(tcCompareMaxCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT"])

        #action on compare A
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ACPA\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_ACPA.append(channelID)
        tcSym_CH_CMR_ACPA[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ACPA", tcCompareAMenu[channelID], comboOptions)
        tcSym_CH_CMR_ACPA[channelID].setLabel("Action on Compare Match A")
        tcSym_CH_CMR_ACPA[channelID].setDefaultValue(comboOptions[1])

        #action on compare C
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ACPC\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_ACPC.append(channelID)
        tcSym_CH_CMR_ACPC[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ACPC", tcCompareAMenu[channelID], comboOptions)
        tcSym_CH_CMR_ACPC[channelID].setLabel("Action on Compare Match C")
        tcSym_CH_CMR_ACPC[channelID].setDefaultValue(comboOptions[2])

        #action on external event
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__AEEVT\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_AEEVT.append(channelID)
        tcSym_CH_CMR_AEEVT[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_AEEVT", tcCompareAMenu[channelID], comboOptions)
        tcSym_CH_CMR_AEEVT[channelID].setLabel("Action on External Event")
        tcSym_CH_CMR_AEEVT[channelID].setDefaultValue(comboOptions[2])
        tcSym_CH_CMR_AEEVT[channelID].setDependencies(tcActionExtEvtVisible, ["TC"+str(channelID)+"_CMP_CMR_ETRGEDG"])
        tcSym_CH_CMR_AEEVT[channelID].setVisible(False)

        #waveform B menu
        tcCompareBMenu.append(channelID)
        tcCompareBMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPAREB", tcCompareMenu[channelID])
        tcCompareBMenu[channelID].setLabel("Compare B Output (TIOB) Configuration")
        tcCompareBMenu[channelID].setDependencies(tcWaveformBVisible, ["TC"+str(channelID)+"_CMR_EEVT"])

        #Compare B
        global tcSym_CH_CompareB
        tcSym_CH_CompareB.append(channelID)
        tcSym_CH_CompareB[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_B", tcCompareBMenu[channelID])
        tcSym_CH_CompareB[channelID].setLabel("Compare Value")
        tcSym_CH_CompareB[channelID].setDefaultValue(3000)
        tcSym_CH_CompareB[channelID].setMin(0)
        tcSym_CH_CompareB[channelID].setMax(tcSym_CH_ComparePeriodCount[channelID].getValue())
        tcSym_CH_CompareB[channelID].setDependencies(tcCompareMaxCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT"])

        #Action on compare B
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BCPB\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_BCPB.append(channelID)
        tcSym_CH_CMR_BCPB[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BCPB", tcCompareBMenu[channelID], comboOptions)
        tcSym_CH_CMR_BCPB[channelID].setLabel("Action on Compare Match B")
        tcSym_CH_CMR_BCPB[channelID].setDefaultValue(comboOptions[1])

        #Action on compare C
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BCPC\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_BCPC.append(channelID)
        tcSym_CH_CMR_BCPC[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BCPC", tcCompareBMenu[channelID], comboOptions)
        tcSym_CH_CMR_BCPC[channelID].setLabel("Action on Compare Match C")
        tcSym_CH_CMR_BCPC[channelID].setDefaultValue(comboOptions[2])

        #Action on external event
        childrenNodes = []
        comboOptions = []
        tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BEEVT\"]")
        childrenNodes = tc.getChildren()
        for param in range(0, len(childrenNodes)):
            comboOptions.append(childrenNodes[param].getAttribute("name"))
        tcSym_CH_CMR_BEEVT.append(channelID)
        tcSym_CH_CMR_BEEVT[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BEEVT", tcCompareBMenu[channelID], comboOptions)
        tcSym_CH_CMR_BEEVT[channelID].setLabel("Action on External Event")
        tcSym_CH_CMR_BEEVT[channelID].setDefaultValue(comboOptions[2])
        tcSym_CH_CMR_BEEVT[channelID].setDependencies(tcActionExtEvtVisible, ["TC"+str(channelID)+"_CMP_CMR_ETRGEDG"])
        tcSym_CH_CMR_BEEVT[channelID].setVisible(False)

        #period interrupt
        tcSym_CH_COMPARE_IER_CPCS.append(channelID)
        tcSym_CH_COMPARE_IER_CPCS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_COMPARE_IER_CPCS", tcCompareMenu[channelID])
        tcSym_CH_COMPARE_IER_CPCS[channelID].setLabel("Enable Period Interrupt")
        tcSym_CH_COMPARE_IER_CPCS[channelID].setDefaultValue(True)

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]")
    tcID = tc.getAttribute("id")

    tcHeaderFile = tcComponent.createFileSymbol("TC_HEADER", None)
    tcHeaderFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/plib_tc.h.ftl")
    tcHeaderFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".h")
    tcHeaderFile.setDestPath("/peripheral/tc/")
    tcHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcHeaderFile.setType("HEADER")
    tcHeaderFile.setOverwrite(True)
    tcHeaderFile.setMarkup(True)

    tcSource1File = tcComponent.createFileSymbol("TC_SOURCE", None)
    tcSource1File.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/plib_tc.c.ftl")
    tcSource1File.setOutputName("plib_"+tcInstanceName.getValue().lower()+".c")
    tcSource1File.setDestPath("/peripheral/tc/")
    tcSource1File.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSource1File.setType("SOURCE")
    tcSource1File.setOverwrite(True)
    tcSource1File.setMarkup(True)

    tcGlobalHeaderFile = tcComponent.createFileSymbol("TC_GLOBALHEADER", None)
    tcGlobalHeaderFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/plib_tc_common.h")
    tcGlobalHeaderFile.setOutputName("plib_tc_common.h")
    tcGlobalHeaderFile.setDestPath("/peripheral/tc/")
    tcGlobalHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcGlobalHeaderFile.setType("HEADER")
    tcGlobalHeaderFile.setMarkup(False)

    tcSystemInitFile = tcComponent.createFileSymbol("TC_INIT", None)
    tcSystemInitFile.setType("STRING")
    tcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tcSystemInitFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/system/system_initialize.c.ftl")
    tcSystemInitFile.setMarkup(True)

    tcSystemDefinitionFile = tcComponent.createFileSymbol("TC_DEF", None)
    tcSystemDefinitionFile.setType("STRING")
    tcSystemDefinitionFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tcSystemDefinitionFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/system/system_definitions.h.ftl")
    tcSystemDefinitionFile.setMarkup(True)
