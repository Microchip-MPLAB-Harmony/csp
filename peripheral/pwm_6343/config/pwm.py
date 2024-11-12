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

###################################################################################################
########################### Global variables   #################################
###################################################################################################

global pwmInstanceName
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
pwmSym_PWM_CMPV_CV = []
pwmSym_PWM_CMPV_CVM = []
pwmSym_PWM_CMPM_CTR = []
pwmSym_PWM_CMPM_CPR = []
pwmSym_PWM_CMPM_CUPR = []

pwmFaultIndexMenu = []
pwmSym_PWM_FMR_FPOL = []
pwmSym_PWM_FMR_FMOD = []
pwmSym_PWM_FPV_FPVH = []
pwmSym_PWM_IER1_FCHID = []
pwmSym_PWM_FPV_FPVL = []

global pwminterruptVector
global pwminterruptHandler
global pwminterruptHandlerLock
global pwminterruptVectorUpdate
global interruptDepList
interruptDepList = []

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################
#channel number is extracted as 2nd character in ID. like PWM0_xxx, PWM1_xxx

def pwminterruptControl(symbol, event):
    global pwmSym_PWM_IER1_FCHID
    Database.clearSymbolValue("core", pwminterruptVector)
    Database.clearSymbolValue("core", pwminterruptHandler)
    Database.clearSymbolValue("core", pwminterruptHandlerLock)
    nvicEnable = False
    for channelID in range(0, 4):
        if (pwmSym_PWM_IER1_CHID[channelID].getValue() == True):
            nvicEnable = True
        if (pwmSym_PWM_IER1_FCHID[channelID].getValue() == True):
            nvicEnable = True
    if(nvicEnable == True):
        Database.setSymbolValue("core", pwminterruptVector, True, 2)
        Database.setSymbolValue("core", pwminterruptHandler, pwmInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", pwminterruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", pwminterruptVector, False, 2)
        Database.setSymbolValue("core", pwminterruptHandler, pwmInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", pwminterruptHandlerLock, False, 2)

def pwmClockControl(symbol, event):
    clockEnable = False
    for channelID in range(0, 4):
        if (pwmSym_CH_Enable[channelID].getValue() == True):
            clockEnable = True

    if (clockEnable == True):
        Database.setSymbolValue("core", pwmInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    else :
        Database.setSymbolValue("core", pwmInstanceName.getValue()+"_CLOCK_ENABLE", False, 2)

def pwmClkDependencyStatus(symbol, event):
    clock = bool(Database.getSymbolValue("core", pwmInstanceName.getValue()+"_CLOCK_ENABLE"))
    if ((clock == False) and (pwmSym_CH_Enable[0].getValue() == True or pwmSym_CH_Enable[1].getValue() == True or pwmSym_CH_Enable[2].getValue() == True or pwmSym_CH_Enable[3].getValue() == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmNVICDependencyStatus(symbol, event):
    nvic = bool(Database.getSymbolValue("core", pwminterruptVectorUpdate))
    nvicEnable = False
    for channelID in range(0, 4):
        if (pwmSym_PWM_IER1_CHID[channelID].getValue() == True):
            nvicEnable = True
        if (pwmSym_PWM_IER1_FCHID[channelID].getValue() == True):
            nvicEnable = True

    if(pwmSym_CH_Enable[0].getValue() == True or pwmSym_CH_Enable[1].getValue() == True or pwmSym_CH_Enable[2].getValue() == True or pwmSym_CH_Enable[3].getValue() == True):
        if ((nvic == True) and (nvicEnable == True)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def pwmIER1Calc(symbol, event):
    component = symbol.getComponent()
    f0 = int(component.getSymbolValue("PWM_FAULT_0_IER1_FCHID")) << 16
    f1 = int(component.getSymbolValue("PWM_FAULT_1_IER1_FCHID")) << 17
    f2 = int(component.getSymbolValue("PWM_FAULT_2_IER1_FCHID")) << 18
    f3 = int(component.getSymbolValue("PWM_FAULT_3_IER1_FCHID")) << 19
    c0 = int(component.getSymbolValue("PWM_CH_0_IER1_CHID"))
    c1 = int(component.getSymbolValue("PWM_CH_1_IER1_CHID")) << 1
    c2 = int(component.getSymbolValue("PWM_CH_2_IER1_CHID")) << 2
    c3 = int(component.getSymbolValue("PWM_CH_3_IER1_CHID")) << 3
    val = f0 + f1+ f2+ f3 + c0+ c1+ c2 + c3
    symbol.setValue(val)


def pwmAlignmentVisible(symbol, event):
    if (event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pwmGetMasterClock():
    main_clk_freq = int(Database.getSymbolValue("core", pwmInstanceName.getValue() + "_CLOCK_FREQUENCY"))
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
    if (masterClock_Hz == 0):
        Log.writeErrorMessage("Master clock frequency is zero")
        masterClock_Hz = 1
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
    if (period != 0):
        if (alignment == "LEFT_ALIGNED"):
            frequency = 1.0 / (period / float(clock_Hz))
        else:
            frequency = 1.0 / (2.0 * period / float(clock_Hz))
    else:
        frequency = 0;

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


def pwmFaultFMRUpdate(symbol, event):
    faultIndex = int(event["id"].split("INDEX_")[1])
    currentValue = symbol.getValue()
    if event["value"] == 1:
        symbol.setValue(currentValue | (1 << faultIndex), 1)
    else:
        symbol.setValue(currentValue & ~(1 << faultIndex), 1)

################################################################################
#### Dependency ####
################################################################################
def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    resetChannels()

global lastPwmChU
lastPwmChU = 0
global lastPwmChV
lastPwmChV = 1
global lastPwmChW
lastPwmChW = 2

def resetChannels():
    global lastPwmChU
    global lastPwmChV
    global lastPwmChW
    component = str(pwmInstanceName.getValue()).lower()
    #disable PWM channels
    Database.setSymbolValue(component, "PWM_CH_"+str(lastPwmChU)+"_ENABLE", False)
    Database.setSymbolValue(component, "PWM_CH_"+str(lastPwmChV)+"_ENABLE", False)
    Database.setSymbolValue(component, "PWM_CH_"+str(lastPwmChW)+"_ENABLE", False)
    #disbale interrupt
    Database.setSymbolValue(component, "PWM_FAULT"+str(lastPwmChU)+"_IER1_FCHID", False)

def handleMessage(messageID, args):
    global lastPwmChU
    global lastPwmChV
    global lastPwmChW
    component = str(pwmInstanceName.getValue()).lower()
    dict = {}

    if (messageID == "PMSM_FOC_PWM_CONF"):
        resetChannels()

        dict['PWM_MAX_CH'] = 4

        lastPwmChU = pwmChU = args['PWM_PH_U']
        lastPwmChV = pwmChV = args['PWM_PH_V']
        lastPwmChW = pwmChW = args['PWM_PH_W']

        #synchronous Channels
        if (pwmChU != 0):
            Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_SYNCENABLE", True)
        if (pwmChV != 0):
            Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_SYNCENABLE", True)
        if (pwmChW != 0):
            Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_SYNCENABLE", True)

        #macros for channel numbers
        Database.setSymbolValue(component, "PWM_PH_U", "PWM_CHANNEL_"+str(pwmChU))
        Database.setSymbolValue(component, "PWM_PH_V", "PWM_CHANNEL_"+str(pwmChV))
        Database.setSymbolValue(component, "PWM_PH_W", "PWM_CHANNEL_"+str(pwmChW))
        Database.setSymbolValue(component, "INTR_PWM_FAULT", pwmInstanceName.getValue()+"_IRQn")
        mask = (1 << pwmChU) + (1 << pwmChV) + (1 << pwmChW)
        pwmPhMask.setValue(mask)

        #enable PWM channels
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_ENABLE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_ENABLE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_ENABLE", True)

        #center-aligned symmetric mode
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_CMR_CALG", 1)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_CMR_CALG", 1)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_CMR_CALG", 1)

        freq = args['PWM_FREQ']
        clock = int(Database.getSymbolValue("core", pwmInstanceName.getValue() + "_CLOCK_FREQUENCY"))
        period = int(clock)/int(freq)/2

        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_CPRD", period)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_CPRD", period)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_CPRD", period)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_CDTY", 0)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_CDTY", 0)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_CDTY", 0)

        #dead-Time
        dt = args['PWM_DEAD_TIME']
        deadtime = int((clock) * float(dt)) / 1000000
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_CMR_DTE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_CMR_DTE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_CMR_DTE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_DT_DTL", deadtime)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_DT_DTH", deadtime)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_DT_DTL", deadtime)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_DT_DTH", deadtime)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_DT_DTL", deadtime)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_DT_DTH", deadtime)

        #Trigger
        Database.setSymbolValue(component, "PWM_COMP_0_CMPM_CEN", True)
        Database.setSymbolValue(component, "PWM_COMP_0_ELMR0_CSEL", True)
        Database.setSymbolValue(component, "PWM_COMP_0_CMPV_CV", 10)

        #Fault
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChU)+"_FAULT_ENABLE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChV)+"_FAULT_ENABLE", True)
        Database.setSymbolValue(component, "PWM_CH_"+str(pwmChW)+"_FAULT_ENABLE", True)
        Database.setSymbolValue(component, "PWM_FAULT_"+str(pwmChU)+"_IER1_FCHID", True)
        global pwmSym_PWM_FPE
        fault = args['PWM_FAULT']
        Database.setSymbolValue(component, "PWM_FMR_FMOD_INDEX_" + str(fault)[-1], 0)
        pwmSym_PWM_FPE[pwmChU].setSelectedKey(str(fault))
        pwmSym_PWM_FPE[pwmChV].setSelectedKey(str(fault))
        pwmSym_PWM_FPE[pwmChW].setSelectedKey(str(fault))

    return dict
###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(pwmComponent):
    global pwmInstanceName
    pwmInstanceName = pwmComponent.createStringSymbol("PWM_INSTANCE_NAME", None)
    pwmInstanceName.setVisible(False)
    pwmInstanceName.setDefaultValue(pwmComponent.getID().upper())
    Log.writeInfoMessage("Running " + pwmInstanceName.getValue())

    #-----------------------------------------------------------------------------------------------------------
    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = [False, False, False, False] #array t0 save available channels
    i = 0

    pinout = "LQFP144"
    val = ATDF.getNode("/avr-tools-device-file/variants")
    children = val.getChildren()
    for index in range(0, len(children)):
        if packageName in children[index].getAttribute("package"):
            pinout = children[index].getAttribute("pinout")

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(pinout)+"\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    #Find available channels and available external clock pins
    pwm_signals = []
    pwm = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PWM\"]/instance@[name=\""+pwmInstanceName.getValue()+"\"]/signals")
    pwm_signals = pwm.getChildren()
    for pad in range(0, len(pwm_signals)):
        if "PWMH" in pwm_signals[pad].getAttribute("group"):
            padSignal = pwm_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(pwm_signals[pad].getAttribute("index"))] = True
    #-----------------------------------------------------------------------------------------------------------

    pwmStartApi = pwmComponent.createStringSymbol("PWM_START_API", None)
    pwmStartApi.setVisible(False)
    pwmStartApi.setValue(pwmInstanceName.getValue()+"_ChannelsStart")

    pwmStopApi = pwmComponent.createStringSymbol("PWM_STOP_API", None)
    pwmStopApi.setVisible(False)
    pwmStopApi.setValue(pwmInstanceName.getValue()+"_ChannelsStop")

    pwmPeriodApi = pwmComponent.createStringSymbol("PWM_GET_PERIOD_API", None)
    pwmPeriodApi.setVisible(False)
    pwmPeriodApi.setValue(pwmInstanceName.getValue()+"_ChannelPeriodGet")

    pwmDutyApi = pwmComponent.createStringSymbol("PWM_SET_DUTY_API", None)
    pwmDutyApi.setVisible(False)
    pwmDutyApi.setValue(pwmInstanceName.getValue() + "_ChannelDutySet")

    pwmOpDisableApi = pwmComponent.createStringSymbol("PWM_OUTPUT_DISABLE_API", None)
    pwmOpDisableApi.setVisible(False)
    pwmOpDisableApi.setValue(pwmInstanceName.getValue() + "_ChannelOverrideDisable")

    pwmOpEnableApi = pwmComponent.createStringSymbol("PWM_OUTPUT_ENABLE_API", None)
    pwmOpEnableApi.setVisible(False)
    pwmOpEnableApi.setValue(pwmInstanceName.getValue() + "_ChannelOverrideEnable")

    pwmCallbackApi = pwmComponent.createStringSymbol("PWM_CALLBACK_API", None)
    pwmCallbackApi.setVisible(False)
    pwmCallbackApi.setValue(pwmInstanceName.getValue() + "_CallbackRegister")

    pwmPhU = pwmComponent.createStringSymbol("PWM_PH_U", None)
    pwmPhU.setVisible(False)
    pwmPhU.setValue("PWM_CHANNEL_0")

    pwmPhV = pwmComponent.createStringSymbol("PWM_PH_V", None)
    pwmPhV.setVisible(False)
    pwmPhV.setValue("PWM_CHANNEL_1")

    pwmPhW = pwmComponent.createStringSymbol("PWM_PH_W", None)
    pwmPhW.setVisible(False)
    pwmPhW.setValue("PWM_CHANNEL_2")

    global pwmPhMask
    pwmPhMask = pwmComponent.createHexSymbol("PWM_PH_MASK", None)
    pwmPhMask.setVisible(False)
    pwmPhMask.setValue(0x7)

    pwmFaultInt = pwmComponent.createStringSymbol("INTR_PWM_FAULT", None)
    pwmFaultInt.setVisible(False)
    pwmFaultInt.setValue(pwmInstanceName.getValue()+"_IRQn")

#-----------------------------------------------------------------------------------------------------------

    #Clock menu
    pwmClockMenu = pwmComponent.createMenuSymbol("PWM_CLOCK", None)
    pwmClockMenu.setLabel("Clock Configurations")

    #enable clock A
    pwmSym_PWM_CLKA_ENABLE = pwmComponent.createBooleanSymbol("PWM_CLK_A_ENABLE", pwmClockMenu)
    pwmSym_PWM_CLKA_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
    pwmSym_PWM_CLKA_ENABLE.setLabel("Enable Clock A")
    pwmSym_PWM_CLKA_ENABLE.setDefaultValue(False)

    #clock A source selection
    global pwmSym_PWM_CLK_PREA
    pwmSym_PWM_CLK_PREA = pwmComponent.createKeyValueSetSymbol("PWM_CLK_PREA", pwmSym_PWM_CLKA_ENABLE)
    pwmSym_PWM_CLK_PREA.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CLK")
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
    pwmSym_PWM_CLK_DIVA.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CLK")
    pwmSym_PWM_CLK_DIVA.setLabel("Select Clock A Divider")
    pwmSym_PWM_CLK_DIVA.setDefaultValue(1)
    pwmSym_PWM_CLK_DIVA.setMin(1)
    pwmSym_PWM_CLK_DIVA.setMax(255)
    pwmSym_PWM_CLK_DIVA.setVisible(False)
    pwmSym_PWM_CLK_DIVA.setDependencies(pwmChannelConfVisible, ["PWM_CLK_A_ENABLE"])

    #enable clock A
    pwmSym_PWM_CLKB_ENABLE = pwmComponent.createBooleanSymbol("PWM_CLK_B_ENABLE", pwmClockMenu)
    pwmSym_PWM_CLKB_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
    pwmSym_PWM_CLKB_ENABLE.setLabel("Enable Clock B")
    pwmSym_PWM_CLKB_ENABLE.setDefaultValue(False)

    #clock B source selection
    global pwmSym_PWM_CLK_PREB
    pwmSym_PWM_CLK_PREB = pwmComponent.createKeyValueSetSymbol("PWM_CLK_PREB", pwmSym_PWM_CLKB_ENABLE)
    pwmSym_PWM_CLK_PREB.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CLK")
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
    pwmSym_PWM_CLK_DIVB.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CLK")
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
        pwmSym_CH_Enable[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_CH_Enable[channelID].setLabel("Enable")
        pwmSym_CH_Enable[channelID].setDefaultValue(False)

        #sync enable
        pwmSym_CH_SyncEnable.append(channelID)
        pwmSym_CH_SyncEnable[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_SYNCENABLE", pwmSym_CH_Enable[channelID])
        pwmSym_CH_SyncEnable[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
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
        pwmSym_PWM_CMR_CPRE[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMR")
        pwmSym_PWM_CMR_CPRE[channelID].setLabel("Select Channel Clock")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CH_NUM\"]/register@[name=\"PWM_CMR\"]/bitfield@[name=\"CPRE\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
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
        pwmSym_PWM_CMR_CALG[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMR")
        pwmSym_PWM_CMR_CALG[channelID].setLabel("Select Alignment")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CH_NUM\"]/register@[name=\"PWM_CMR\"]/bitfield@[name=\"CALG\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
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
        pwmSym_PWM_CMR_UPDS[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_CMR_UPDS[channelID].setLabel("Select Duty-Cycle Update Trigger")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CH_NUM\"]/register@[name=\"PWM_CMR\"]/bitfield@[name=\"UPDS\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_UPDS[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_UPDS[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_UPDS[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_UPDS[channelID].setDependencies(pwmAlignmentVisible, ["PWM_CH_"+str(channelID)+"_CMR_CALG"])

        #counter event selection
        pwmSym_PWM_CMR_CES.append(channelID)
        pwmSym_PWM_CMR_CES[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CES", pwmSym_PWM_CMR_CALG[channelID])
        pwmSym_PWM_CMR_CES[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_CMR_CES[channelID].setLabel("Select Counter Event Occurrence")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CH_NUM\"]/register@[name=\"PWM_CMR\"]/bitfield@[name=\"CES\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMR_CES[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMR_CES[channelID].setDisplayMode("Description")
        pwmSym_PWM_CMR_CES[channelID].setOutputMode("Key")
        pwmSym_PWM_CMR_CES[channelID].setDependencies(pwmAlignmentVisible, ["PWM_CH_"+str(channelID)+"_CMR_CALG"])

        #polarity
        pwmSym_PWM_CMR_CPOL.append(channelID)
        pwmSym_PWM_CMR_CPOL[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_CMR_CPOL", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_CPOL[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMR")
        pwmSym_PWM_CMR_CPOL[channelID].setLabel("Output Polarity")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CH_NUM\"]/register@[name=\"PWM_CMR\"]/bitfield@[name=\"CPOL\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
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
        pwmSym_PWM_CPRD[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CPRD")
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
        pwmSym_PWM_FreqComment[channelID].setDependencies(pwmCalcFreq, ["core." + pwmInstanceName.getValue() + "_CLOCK_FREQUENCY", "PWM_CH_"+str(channelID)+"_CMR_CPRE",\
        "PWM_CLK_PREA", "PWM_CLK_PREB", "PWM_CLK_DIVA", "PWM_CLK_DIVB", "PWM_CH_"+str(channelID)+"_CPRD", "PWM_CH_"+str(channelID)+"_CMR_CALG", "PWM_CH_"+str(channelID)+"_ENABLE", "PWM_CH_"+str(channelID)+"_SYNCENABLE"])
        pwmSym_PWM_FreqComment[channelID].setVisible(False)

        #duty
        pwmSym_PWM_CDTY.append(channelID)
        pwmSym_PWM_CDTY[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_CDTY", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CDTY[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CDTY")
        pwmSym_PWM_CDTY[channelID].setLabel("Duty Value")
        pwmSym_PWM_CDTY[channelID].setDefaultValue(3750)
        pwmSym_PWM_CDTY[channelID].setMin(0)
        pwmSym_PWM_CDTY[channelID].setMax(pwmSym_PWM_CPRD[channelID].getValue())
        pwmSym_PWM_CDTY[channelID].setVisible(False)
        pwmSym_PWM_CDTY[channelID].setDependencies(pwmDutyMaxValue, ["PWM_CH_"+str(channelID)+"_CPRD", "PWM_CH_"+str(channelID)+"_ENABLE"])

        #dead time enable
        pwmSym_PWM_CMR_DTE.append(channelID)
        pwmSym_PWM_CMR_DTE[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_CMR_DTE", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_CMR_DTE[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMR")
        pwmSym_PWM_CMR_DTE[channelID].setLabel("Enable Dead Time")
        pwmSym_PWM_CMR_DTE[channelID].setDefaultValue(True)
        pwmSym_PWM_CMR_DTE[channelID].setVisible(False)
        pwmSym_PWM_CMR_DTE[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

        #duty for low side output
        pwmSym_PWM_DT_DTL.append(channelID)
        pwmSym_PWM_DT_DTL[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_DT_DTL", pwmSym_PWM_CMR_DTE[channelID])
        pwmSym_PWM_DT_DTL[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_DT")
        pwmSym_PWM_DT_DTL[channelID].setLabel("Dead Time for low-Side Output")
        pwmSym_PWM_DT_DTL[channelID].setDefaultValue(100)
        pwmSym_PWM_DT_DTL[channelID].setMin(0)
        pwmSym_PWM_DT_DTL[channelID].setMax(4095)

        #duty for high side output
        pwmSym_PWM_DT_DTH.append(channelID)
        pwmSym_PWM_DT_DTH[channelID] = pwmComponent.createIntegerSymbol("PWM_CH_"+str(channelID)+"_DT_DTH", pwmSym_PWM_CMR_DTE[channelID])
        pwmSym_PWM_DT_DTH[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_DT")
        pwmSym_PWM_DT_DTH[channelID].setLabel("Dead Time for high-Side Output")
        pwmSym_PWM_DT_DTH[channelID].setDefaultValue(100)
        pwmSym_PWM_DT_DTH[channelID].setMin(0)
        pwmSym_PWM_DT_DTH[channelID].setMax(4095)

        #fault enable
        pwmSym_PWM_Fault_Enable.append(channelID)
        pwmSym_PWM_Fault_Enable[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_FAULT_ENABLE", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_Fault_Enable[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_Fault_Enable[channelID].setLabel("Enable Fault")
        pwmSym_PWM_Fault_Enable[channelID].setDefaultValue(False)
        pwmSym_PWM_Fault_Enable[channelID].setVisible(False)
        pwmSym_PWM_Fault_Enable[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])

        #fault source
        global pwmSym_PWM_FPE
        pwmSym_PWM_FPE.append(channelID)
        pwmSym_PWM_FPE[channelID] = pwmComponent.createKeyValueSetSymbol("PWM_CH_"+str(channelID)+"_FPE", pwmSym_PWM_Fault_Enable[channelID])
        pwmSym_PWM_FPE[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_FPE")
        pwmSym_PWM_FPE[channelID].setLabel("Select Fault Source")
        pwmSym_PWM_FPE[channelID].setDefaultValue(0)
        pwmSym_PWM_FPE[channelID].setVisible(False)
        fault_id = []
        pwm = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PWM\"]/instance@[name=\""+pwmInstanceName.getValue()+"\"]/parameters")
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
        pwmSym_PWM_FPV_FPVL[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
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
        pwmSym_PWM_FPV_FPVH[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_FPV_FPVH[channelID].setLabel("Select high-side Output Polarity after Fault")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("LOW", "0", "Low")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("HIGH", "1", "High")
        pwmSym_PWM_FPV_FPVH[channelID].addKey("HIGH_IMPEDANCE", "2", "High-Impedance")
        pwmSym_PWM_FPV_FPVH[channelID].setDisplayMode("Description")
        pwmSym_PWM_FPV_FPVH[channelID].setOutputMode("Value")
        pwmSym_PWM_FPV_FPVH[channelID].setVisible(False)
        pwmSym_PWM_FPV_FPVH[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_FAULT_ENABLE"])

        global pwmSym_PWM_IER1_FCHID
        pwmSym_PWM_IER1_FCHID.append(channelID)
        pwmSym_PWM_IER1_FCHID[channelID] = pwmComponent.createBooleanSymbol("PWM_FAULT_"+str(channelID)+"_IER1_FCHID", pwmSym_PWM_Fault_Enable[channelID])
        pwmSym_PWM_IER1_FCHID[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_IER1_FCHID[channelID].setLabel("Enable Fault Interrupt")
        pwmSym_PWM_IER1_FCHID[channelID].setVisible(False)
        pwmSym_PWM_IER1_FCHID[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_FAULT_ENABLE"])
        interruptDepList.append("PWM_FAULT_"+str(channelID)+"_IER1_FCHID")

        #interrupt enable
        pwmSym_PWM_IER1_CHID.append(channelID)
        pwmSym_PWM_IER1_CHID[channelID] = pwmComponent.createBooleanSymbol("PWM_CH_"+str(channelID)+"_IER1_CHID", pwmSym_CH_Enable[channelID])
        pwmSym_PWM_IER1_CHID[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
        pwmSym_PWM_IER1_CHID[channelID].setLabel("Enable Counter Period Interrupt")
        pwmSym_PWM_IER1_CHID[channelID].setDefaultValue(False)
        pwmSym_PWM_IER1_CHID[channelID].setVisible(False)
        pwmSym_PWM_IER1_CHID[channelID].setDependencies(pwmChannelConfVisible, ["PWM_CH_"+str(channelID)+"_ENABLE"])
        interruptDepList.append("PWM_CH_"+str(channelID)+"_IER1_CHID")

    pwmSym_PWM_IER1_REG = pwmComponent.createHexSymbol("PWM_IER1_REG", None)
    pwmSym_PWM_IER1_REG.setVisible(False)
    pwmSym_PWM_IER1_REG.setDependencies(pwmIER1Calc, interruptDepList)

    #-----------------------------------------------------------------------------------------------------------

    #fault menu
    pwmFaultMenu = pwmComponent.createMenuSymbol("PWM_FAULT", None)
    pwmFaultMenu.setLabel("Fault Configurations")
    pwmFaultMenu.setVisible(False)
    pwmFaultMenu.setDependencies(pwmFaultMenuVisible, ["PWM_CH_0_FAULT_ENABLE", "PWM_CH_1_FAULT_ENABLE", "PWM_CH_2_FAULT_ENABLE", "PWM_CH_3_FAULT_ENABLE"])

    pwmSym_PWM_FMR_FPOL_Val = pwmComponent.createHexSymbol("PWM_FMR_FPOL_VAL", pwmFaultMenu)
    pwmSym_PWM_FMR_FPOL_Val.setVisible(False)
    pwmFaultFPOLSymNameList = []
    pwmFPOLDefaultVal = 0

    pwmSym_PWM_FMR_FMOD_Val = pwmComponent.createHexSymbol("PWM_FMR_FMOD_VAL", pwmFaultMenu)
    pwmSym_PWM_FMR_FMOD_Val.setVisible(False)
    pwmFaultFMODSymNameList = []
    pwmFMODDefaultVal = 0

    pwmSym_PWM_FMR_FFIL_Val = pwmComponent.createHexSymbol("PWM_FMR_FFIL_VAL", pwmFaultMenu)
    pwmSym_PWM_FMR_FFIL_Val.setVisible(False)
    pwmFaultFILSymNameList = []
    pwmFFILDefaultVal = 0

    parametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PWM\"]/instance@[name=\"" + pwmInstanceName.getValue() + "\"]/parameters")
    for parameter in parametersNode.getChildren():
        if parameter.getAttribute("name").startswith("FAULT"):
            # ID number of the fault
            faultID = parameter.getAttribute("name").split("_ID")[1]

            # Fault Menu
            pwmFaultIndexMenu = pwmComponent.createMenuSymbol("PWM_FAULT_" + faultID, pwmFaultMenu)
            pwmFaultIndexMenu.setLabel(parameter.getAttribute("caption"))

            # Fault polarity
            pwmFPOLSymName = "PWM_FMR_FPOL_INDEX_" + faultID
            pwmSym_PWM_FMR_FPOL = pwmComponent.createKeyValueSetSymbol(pwmFPOLSymName, pwmFaultIndexMenu)
            pwmSym_PWM_FMR_FPOL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
            pwmSym_PWM_FMR_FPOL.setLabel("Select Fault Polarity")
            pwmSym_PWM_FMR_FPOL.addKey("LOW", "0", "Active when fault input is low")
            pwmSym_PWM_FMR_FPOL.addKey("HIGH", "1", "Active when fault input is high")
            pwmSym_PWM_FMR_FPOL.setDisplayMode("Description")
            pwmSym_PWM_FMR_FPOL.setOutputMode("Value")
            if not parameter.getAttribute("caption").endswith("Input pin"):
                pwmSym_PWM_FMR_FPOL.setDefaultValue(1)
                pwmSym_PWM_FMR_FPOL.setReadOnly(True)
                pwmFPOLDefaultVal |= (1 << int(faultID))
            pwmFaultFPOLSymNameList.append(pwmFPOLSymName)

            # Fault mode
            global pwmSym_PWM_FMR_FMOD
            pwmFMODSymName = "PWM_FMR_FMOD_INDEX_" + faultID
            pwmSym_PWM_FMR_FMOD = pwmComponent.createKeyValueSetSymbol(pwmFMODSymName, pwmFaultIndexMenu)
            pwmSym_PWM_FMR_FMOD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
            pwmSym_PWM_FMR_FMOD.setLabel("Select Fault Mode")
            pwmSym_PWM_FMR_FMOD.addKey("CLEAR_AT_PERIPHERAL", "0", "Fault is active until cleared at peripheral level")
            pwmSym_PWM_FMR_FMOD.addKey("CLEAR_AT_PERIPHERAL_AND_REGISTER", "1", "Fault is active until cleared at peripheral level AND cleared in PWM_FCR register")
            pwmSym_PWM_FMR_FMOD.setDisplayMode("Description")
            pwmSym_PWM_FMR_FMOD.setOutputMode("Value")
            pwmSym_PWM_FMR_FMOD.setDefaultValue(1)
            pwmFMODDefaultVal |= (1 << int(faultID))
            pwmFaultFMODSymNameList.append(pwmFMODSymName)

            #Fault Filter
            pwmFFILSymName = "PWM_FMR_FFIL_INDEX_" + faultID
            pwmSym_PWM_FMR_FFIL = pwmComponent.createKeyValueSetSymbol(pwmFFILSymName, pwmFaultIndexMenu)
            pwmSym_PWM_FMR_FFIL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
            pwmSym_PWM_FMR_FFIL.setLabel("Select Fault Filter")
            pwmSym_PWM_FMR_FFIL.addKey("DISABLE_FILTER", "0", "Fault input is not filtered")
            pwmSym_PWM_FMR_FFIL.addKey("ENABLE_FILTER", "1", "Fault input is filtered")
            pwmSym_PWM_FMR_FFIL.setDisplayMode("Description")
            pwmSym_PWM_FMR_FFIL.setOutputMode("Value")
            pwmFaultFILSymNameList.append(pwmFFILSymName)

    # Set the dependency update function for FPOL, FMOD and FFIL
    pwmSym_PWM_FMR_FPOL_Val.setDefaultValue(pwmFPOLDefaultVal)
    pwmSym_PWM_FMR_FPOL_Val.setDependencies(pwmFaultFMRUpdate, pwmFaultFPOLSymNameList)

    pwmSym_PWM_FMR_FMOD_Val.setDefaultValue(pwmFMODDefaultVal)
    pwmSym_PWM_FMR_FMOD_Val.setDependencies(pwmFaultFMRUpdate, pwmFaultFMODSymNameList)

    pwmSym_PWM_FMR_FFIL_Val.setDefaultValue(pwmFFILDefaultVal)
    pwmSym_PWM_FMR_FFIL_Val.setDependencies(pwmFaultFMRUpdate, pwmFaultFILSymNameList)

    #-----------------------------------------------------------------------------------------------------------

    #Synchronous channels menu
    pwmSyncChMenu = pwmComponent.createMenuSymbol("PWM_SYNC_CHANNELS", None)
    pwmSyncChMenu.setLabel("Synchronous Channels Configurations")
    pwmSyncChMenu.setVisible(False)
    pwmSyncChMenu.setDependencies(pwmSyncMenuVisible, ["PWM_CH_0_SYNCENABLE", "PWM_CH_1_SYNCENABLE", "PWM_CH_2_SYNCENABLE"])

    #sync update mode
    pwmSym_PWM_SCM_UPDM = pwmComponent.createKeyValueSetSymbol("PWM_SCM_UPDM", pwmSyncChMenu)
    pwmSym_PWM_SCM_UPDM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_SCM")
    pwmSym_PWM_SCM_UPDM.setLabel("Select Synchronous Channel Update Mode")
    childrenNodes = []
    bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM\"]/register@[name=\"PWM_SCM\"]/bitfield@[name=\"UPDM\"]")
    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
    childrenNodes = pwm.getChildren()
    for param in range(0, (len(childrenNodes) - 1)):
        pwmSym_PWM_SCM_UPDM.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
    pwmSym_PWM_SCM_UPDM.setDefaultValue(1)
    pwmSym_PWM_SCM_UPDM.setDisplayMode("Description")
    pwmSym_PWM_SCM_UPDM.setOutputMode("Key")

    #Sync update period
    pwmSym_PWM_SCUP_UPR = pwmComponent.createIntegerSymbol("PWM_SCUP_UPR", pwmSyncChMenu)
    pwmSym_PWM_SCUP_UPR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_SCUP")
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
    pwmCompareMenu.setVisible(pwmSym_CH_Enable[0].getValue())

    registerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM\"]/register@[name=\"PWM_ELMR\"]")
    elmTotal =  int(registerNode.getAttribute("count"), 0)

    for compareID in range(0, 8):

        #compare unit enable
        pwmSym_PWM_CMPM_CEN.append(compareID)
        pwmSym_PWM_CMPM_CEN[compareID] = pwmComponent.createBooleanSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CEN", pwmCompareMenu)
        pwmSym_PWM_CMPM_CEN[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPM")
        pwmSym_PWM_CMPM_CEN[compareID].setLabel("Compare Unit " + str(compareID) +" Enable")
        pwmSym_PWM_CMPM_CEN[compareID].setDefaultValue(False)

        #Event line mode
        for elmID in range(elmTotal):
            elmSym = pwmComponent.createBooleanSymbol("PWM_COMP_{0}_ELMR{1}_CSEL".format(compareID, elmID), pwmSym_PWM_CMPM_CEN[compareID])
            elmSym.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:%NOREGISTER%")
            elmSym.setLabel("Generate Pulse on Event Line " + str(elmID))
            elmSym.setDefaultValue(False)

        #compare Value
        pwmSym_PWM_CMPV_CV.append(compareID)
        pwmSym_PWM_CMPV_CV[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPV_CV", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPV_CV[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPV")
        pwmSym_PWM_CMPV_CV[compareID].setLabel("Comparison Value")
        pwmSym_PWM_CMPV_CV[compareID].setDefaultValue(100)
        pwmSym_PWM_CMPV_CV[compareID].setMin(0)
        pwmSym_PWM_CMPV_CV[compareID].setMax(pwmSym_PWM_CPRD[0].getValue())
        pwmSym_PWM_CMPV_CV[compareID].setDependencies(pwmCompMaxValue, ["PWM_CH_0_CPRD"])

        #compare mode
        pwmSym_PWM_CMPV_CVM.append(compareID)
        pwmSym_PWM_CMPV_CVM[compareID] = pwmComponent.createKeyValueSetSymbol("PWM_COMP_"+str(compareID)+"_CMPV_CVM", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPV_CVM[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPV")
        pwmSym_PWM_CMPV_CVM[compareID].setLabel("Comparison Mode")
        childrenNodes = []
        bitfieldNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/register-group@[name=\"PWM_CMP\"]/register@[name=\"PWM_CMPV\"]/bitfield@[name=\"CVM\"]")
        pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]/value-group@[name=\"" + bitfieldNode.getAttribute("values") + "\"]")
        childrenNodes = pwm.getChildren()
        for param in range(0, len(childrenNodes)):
            pwmSym_PWM_CMPV_CVM[compareID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
        pwmSym_PWM_CMPV_CVM[compareID].setDisplayMode("Description")
        pwmSym_PWM_CMPV_CVM[compareID].setOutputMode("Key")
        pwmSym_PWM_CMPV_CVM[compareID].setDependencies(pwmAlignmentVisible, ["PWM_CH_0_CMR_CALG"])

        #CTR, CPR, CUPR
        pwmSym_PWM_CMPM_CPR.append(compareID)
        pwmSym_PWM_CMPM_CPR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CPR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CPR[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPM")
        pwmSym_PWM_CMPM_CPR[compareID].setLabel("Comparison Period")
        pwmSym_PWM_CMPM_CPR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CPR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CPR[compareID].setMax(15)

        pwmSym_PWM_CMPM_CTR.append(compareID)
        pwmSym_PWM_CMPM_CTR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CTR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CTR[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPM")
        pwmSym_PWM_CMPM_CTR[compareID].setLabel("Comparison Trigger")
        pwmSym_PWM_CMPM_CTR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CTR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CTR[compareID].setMax(pwmSym_PWM_CMPM_CPR[compareID].getValue())
        pwmSym_PWM_CMPM_CTR[compareID].setDependencies(pwmCompMaxValue, ["PWM_COMP_"+str(compareID)+"_CMPM_CPR"])

        pwmSym_PWM_CMPM_CUPR.append(compareID)
        pwmSym_PWM_CMPM_CUPR[compareID] = pwmComponent.createIntegerSymbol("PWM_COMP_"+str(compareID)+"_CMPM_CUPR", pwmSym_PWM_CMPM_CEN[compareID])
        pwmSym_PWM_CMPM_CUPR[compareID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_6343;register:PWM_CMPM")
        pwmSym_PWM_CMPM_CUPR[compareID].setLabel("Comparison Update Period")
        pwmSym_PWM_CMPM_CUPR[compareID].setDefaultValue(0)
        pwmSym_PWM_CMPM_CUPR[compareID].setMin(0)
        pwmSym_PWM_CMPM_CUPR[compareID].setMax(pwmSym_PWM_CMPM_CPR[compareID].getValue())
        pwmSym_PWM_CMPM_CUPR[compareID].setDependencies(pwmCompMaxValue, ["PWM_COMP_"+str(compareID)+"_CMPM_CPR"])

    #-----------------------------------------------------------------------------------------------------------
    #--------------------- Dependency ----------------------------------------
    global pwminterruptVector
    global pwminterruptHandler
    global pwminterruptHandlerLock
    global pwminterruptVectorUpdate

    pwminterruptVector = pwmInstanceName.getValue() + "_INTERRUPT_ENABLE"
    pwminterruptHandler = pwmInstanceName.getValue() + "_INTERRUPT_HANDLER"
    pwminterruptHandlerLock = pwmInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    pwminterruptVectorUpdate = pwmInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    pwmSym_interruptControl = pwmComponent.createBooleanSymbol("PWM_NVIC_ENABLE", None)
    pwmSym_interruptControl.setDependencies(pwminterruptControl, interruptDepList)
    pwmSym_interruptControl.setVisible(False)

    # Clock Dynamic settings
    pwmSym_ClockControl = pwmComponent.createBooleanSymbol("PWM_CLOCK_ENABLE", None)
    pwmSym_ClockControl.setDependencies(pwmClockControl, ["PWM_CH_0_ENABLE", "PWM_CH_1_ENABLE", "PWM_CH_2_ENABLE", "PWM_CH_3_ENABLE"])
    pwmSym_ClockControl.setVisible(False)

    # Dependency Status
    pwmSymClkEnComment = pwmComponent.createCommentSymbol("PWM_CLK_ENABLE_COMMENT", None)
    pwmSymClkEnComment.setVisible(False)
    pwmSymClkEnComment.setLabel("Warning!!! PWM Peripheral Clock is Disabled in Clock Manager")

    pwmSymClkEnComment.setDependencies(pwmClkDependencyStatus, ["core."+pwmInstanceName.getValue()+"_CLOCK_ENABLE", "PWM_CH_0_ENABLE", "PWM_CH_1_ENABLE", "PWM_CH_2_ENABLE", "PWM_CH_3_ENABLE"])

    interruptCommentDepList = interruptDepList[:]
    interruptCommentDepList.append("core." + pwminterruptVectorUpdate)
    interruptCommentDepList.append("PWM_CH_0_ENABLE")
    interruptCommentDepList.append( "PWM_CH_1_ENABLE")
    interruptCommentDepList.append( "PWM_CH_2_ENABLE")
    interruptCommentDepList.append("PWM_CH_3_ENABLE")

    pwmSymIntEnComment = pwmComponent.createCommentSymbol("PWM_NVIC_ENABLE_COMMENT", None)
    pwmSymIntEnComment.setVisible(False)
    pwmSymIntEnComment.setLabel("Warning!!! PWM Interrupt is Disabled in Interrupt Manager")
    pwmSymIntEnComment.setDependencies(pwmNVICDependencyStatus, interruptCommentDepList)



    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################

    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]")
    pwmID = pwm.getAttribute("id")

    pwmHeaderFile = pwmComponent.createFileSymbol("PWM_HEADER", None)
    pwmHeaderFile.setSourcePath("../peripheral/pwm_6343/templates/plib_pwm.h.ftl")
    pwmHeaderFile.setOutputName("plib_"+pwmInstanceName.getValue().lower()+ ".h")
    pwmHeaderFile.setDestPath("/peripheral/pwm/")
    pwmHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmHeaderFile.setType("HEADER")
    pwmHeaderFile.setOverwrite(True)
    pwmHeaderFile.setMarkup(True)

    pwmSource1File = pwmComponent.createFileSymbol("PWM_SOURCE", None)
    pwmSource1File.setSourcePath("../peripheral/pwm_6343/templates/plib_pwm.c.ftl")
    pwmSource1File.setOutputName("plib_"+pwmInstanceName.getValue().lower()+".c")
    pwmSource1File.setDestPath("/peripheral/pwm/")
    pwmSource1File.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmSource1File.setType("SOURCE")
    pwmSource1File.setOverwrite(True)
    pwmSource1File.setMarkup(True)

    pwmGlobalHeaderFile = pwmComponent.createFileSymbol("PWM_COMMON_HEADER", None)
    pwmGlobalHeaderFile.setSourcePath("../peripheral/pwm_6343/templates/plib_pwm_common.h")
    pwmGlobalHeaderFile.setOutputName("plib_pwm_common.h")
    pwmGlobalHeaderFile.setDestPath("/peripheral/pwm/")
    pwmGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmGlobalHeaderFile.setType("HEADER")
    pwmGlobalHeaderFile.setMarkup(False)

    pwmSystemInitFile = pwmComponent.createFileSymbol("PWM_INIT", None)
    pwmSystemInitFile.setType("STRING")
    pwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pwmSystemInitFile.setSourcePath("../peripheral/pwm_6343/templates/system/initialization.c.ftl")
    pwmSystemInitFile.setMarkup(True)

    pwmSystemDefinitionFile = pwmComponent.createFileSymbol("PWM_DEF", None)
    pwmSystemDefinitionFile.setType("STRING")
    pwmSystemDefinitionFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pwmSystemDefinitionFile.setSourcePath("../peripheral/pwm_6343/templates/system/definitions.h.ftl")
    pwmSystemDefinitionFile.setMarkup(True)
