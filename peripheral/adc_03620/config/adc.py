# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
import math

###################################################################################################
########################### Component   #################################
###################################################################################################
global adcInstanceName
global nSARCore
global nSARChannel
global SARCoreChannels
global earlyInterruptPresent
global numTriggers

nSARCore = 0
earlyInterruptPresent = False
numTriggers = 0
nSARChannel = []
coreCompartorEnableDepList = []
coreStartConvOnEventInputDepList = []
coreResultReadyEventOutputDepList = []
adcConversionTimeDepList = []
adcClockFreqDepList = []
adcGlobalFIFOIntDepList = []
adcCoreConfigSymbolsList = []
adcCoreIntEnabledDepList = []
adcMaxChannelsDepList = []
adcEvsysGenCHRDYCDepList = []
adcEvsysGenCMPDepList = []
adcEvsysUserDepList = []

ADC_CORCTRL_REG_DepList = []
ADC_CHNCFG1_REG_DepList = []
ADC_CHNCFG2_REG_DepList = []
ADC_CHNCFG3_REG_DepList = []
ADC_CHNCFG4_REG_DepList = []
ADC_CHNCFG5_REG_DepList = []
ADC_EVCTRL_REG_DepList = []
ADC_CMPCTRL_REG_DepList = []
ADC_FLTCTRL_REG_DepList = []
ADC_INTENSET_REG_DepList = []
ADC_PFFCTRL_REG_DepList = []
ADC_CTLINTENSET_REG_DepList = []
ADC_CTRLD_REG_DepList = []
ADC_CTRLC_REG_DepList = []
ADC_CTRLA_REG_DepList = []
ADC_CTRLD__ANLEN_DepList = []

def getChannel(symbol_id):
    return int(symbol_id.split("_")[4])

def getCore(symbol_id):
    return int(symbol_id.split("_")[2])

def getNumCoreChannels(n):
    return nSARChannel[n]

def isChannelEnabled(localComponent, n, k):
    return localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE")

def isChannelComparatorEnabled(localComponent, n, k):
    return localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG1_CHNCMPEN")

def controlClockCalculate(localComponent):
    global adcInstanceName

    TQ = 0
    TQ_USEC = str(0)
    F_CTRL_CLK = 0
    F_CTRL_CLK_MHZ = str(0)


    FSRC_CLK = localComponent.getSymbolValue("ADC_GLOBAL_INPUT_CLK_FREQ")
    CTLCKDIV = localComponent.getSymbolValue("ADC_GLOBAL_CTRLD_CTLCKDIV")

    if FSRC_CLK != 0:
        TSRC_CLK = (1.0/FSRC_CLK)
        TQ = (CTLCKDIV + 1) * TSRC_CLK
        F_CTRL_CLK = FSRC_CLK/(CTLCKDIV + 1)
        TQ_USEC = "{:.4f}".format(TQ*1e6)
        F_CTRL_CLK_MHZ = "{:.4f}".format(F_CTRL_CLK/1e6)

    return (F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC)

def conversionTimeCalculate(localComponent, n):
    global adcInstanceName

    sample_time_usec = str(0)
    conversion_time_usec = str(0)
    conversion_freq_mhz = str(0)

    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(localComponent)

    ADCDIV = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")
    SELRES = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CORCTRL_SELRES").getSelectedKey().split("_")[0])
    SAMC = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_SAMC")

    if TQ != 0:
        TAD = 2 * (ADCDIV * TQ)
        sample_time = (SAMC + 1.5) * TAD
        conversion_time = (sample_time + ((SELRES + 0.5) * TAD))
        conversion_time_usec = "{:.4f}".format(conversion_time*1e6 )
        conversion_freq_mhz = "{:.4f}".format(1.0/(conversion_time*1e6))
        sample_time_usec = "{:.4f}".format(sample_time*1e6 )

    return (sample_time_usec, conversion_time_usec, conversion_freq_mhz)

def adcClockFreqCalculate (localComponent, n):
    adcCoreClockFreqMHz = str(0)
    adcCoreTimePeriodUsec = str(0)

    input_clock_freq = localComponent.getSymbolValue("ADC_GLOBAL_INPUT_CLK_FREQ")
    control_clock_div = localComponent.getSymbolValue("ADC_GLOBAL_CTRLD_CTLCKDIV")
    core_clock_div = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")

    control_clock_freq = input_clock_freq/(control_clock_div + 1)
    core_clock_freq = control_clock_freq / (2 * core_clock_div)

    if core_clock_freq > 0:
        adcCoreClockFreqMHz = core_clock_freq/1e6
        adcCoreTimePeriodUsec = 1/adcCoreClockFreqMHz
        adcCoreClockFreqMHz = "{:.4f}".format(adcCoreClockFreqMHz)
        adcCoreTimePeriodUsec = "{:.4f}".format(adcCoreTimePeriodUsec)

    return (adcCoreClockFreqMHz, adcCoreTimePeriodUsec)

def delayTimeCalculate (localComponent):
    delayTimeUsec = str(0)

    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(localComponent)
    ctrlc_cnt = localComponent.getSymbolValue("ADC_GLOBAL_CTRLC_CNT")

    delayTime = TQ * ctrlc_cnt
    delayTimeUsec =  "{:.4f}".format(delayTime*1e6)

    return delayTimeUsec
#---------------------------------------------------------------------------------

def channelModeChange(symbol, event):
    if "CHNCFG3_DIFF" in event["id"]:
        symbol.setValue(event["value"])
    else:
        symbol.setVisible(event["value"])

def channelVisibility(symbol, event):
    symbol.setVisible(event["value"])

def coreComparatorEnable(symbol, event):
    global nSARChannel
    SARCoreComparatorEnable = False
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    for k in range(0, numChannels):
        channelEnabled = isChannelEnabled(localComponent, n, k)
        comparatorEnabled = isChannelComparatorEnabled(localComponent, n, k)
        if channelEnabled == True and comparatorEnabled == True:
            SARCoreComparatorEnable = True
            break

    symbol.setValue(SARCoreComparatorEnable)

def conversionTimeUpdate(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE") == True:
        sample_time_usec, conversion_time_usec, conversion_freq_mhz = conversionTimeCalculate(localComponent, n)
        symbol.setLabel("[ Sampling Time = " + sample_time_usec + " micro sec, " + "Total Conversion Time = " + conversion_time_usec + " micro sec, " + "Max Sampling Freq = " + conversion_freq_mhz + " MHz ]")

def adcClockFreqUpdate(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE") == True:
        adcCoreClockFreqMHz, adcCoreTimePeriodUsec = adcClockFreqCalculate(localComponent, n)
        symbol.setLabel("[ ADC Clock Freq = " + adcCoreClockFreqMHz + " MHz, " + "TAD = " + adcCoreTimePeriodUsec + " micro sec ]")

def updateInputClockFreq(symbol, event):
    symbol.setValue(event["value"])

def updateControlClockFreq(symbol, event):
    localComponent = symbol.getComponent()
    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(localComponent)
    symbol.setValue(F_CTRL_CLK)

def updateCoreReadyIntStatus(symbol, event):
    if event["value"] == False:
        symbol.setReadOnly(True)
        symbol.setValue(False)
    else:
        symbol.setReadOnly(False)

def updateCommonInterruptStatus(symbol, event):
    localComponent = symbol.getComponent()

    core_enabled = False
    core_n_pffcr = False

    for n in range(0, nSARCore):
        core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")
        core_n_pffcr = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR")
        if core_enabled == True and core_n_pffcr == True:
            break

    if core_enabled == True and core_n_pffcr == True:
        symbol.setReadOnly(False)
    else:
        symbol.setReadOnly(True)
        symbol.setValue(False)

def updateControlClockPeriodTQ(symbol, event):
    localComponent = symbol.getComponent()

    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(localComponent)

    symbol.setLabel("[ Control Clock: Freq = " + F_CTRL_CLK_MHZ + " MHz, Period TQ = " + TQ_USEC + "micro sec ]")

def updateDelayTime (symbol, event):
    localComponent = symbol.getComponent()
    delayTimeUsec = delayTimeCalculate(localComponent)

    symbol.setLabel("[ Delay Time = " + delayTimeUsec + " micro sec ]")

def updateTriggerDelayCounter (symbol, event):
    interleaving_enabled = event["symbol"].getSelectedValue()
    if interleaving_enabled == "0x0":       # Interleaving is disabled
        symbol.setReadOnly(True)
        symbol.setValue(0)
    else:
        symbol.setReadOnly(False)

def coreSymVisibilityUpdate (symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    for coreSym in adcCoreConfigSymbolsList[n]:
        localComponent.getSymbolByID(coreSym).setVisible(event["value"])

def updateAdcNVICInterrutps(symbol, event):
    intEnable = False if event["value"] == 0 else True

    if symbol.getID() == "ADC_GLOBAL_NVIC_INT":
        Database.setSymbolValue("core", "ADC_GLOBAL" + "_INTERRUPT_ENABLE", intEnable, 2)
        Database.setSymbolValue("core", "ADC_GLOBAL" + "_INTERRUPT_HANDLER_LOCK", intEnable, 2)
        if intEnable == False:
            Database.setSymbolValue("core", "ADC_GLOBAL" + "_INTERRUPT_HANDLER", "ADC_GLOBAL" + "_Handler", 2)
        else:
            Database.setSymbolValue("core", "ADC_GLOBAL" + "_INTERRUPT_HANDLER", "ADC_GLOBAL" + "_InterruptHandler", 2)
    else:
        n = getCore(symbol.getID()) + 1
        Database.setSymbolValue("core", "ADC_CORE" + str(n) + "_INTERRUPT_ENABLE", intEnable, 2)
        Database.setSymbolValue("core", "ADC_CORE"  + str(n) + "_INTERRUPT_HANDLER_LOCK", intEnable, 2)
        if intEnable == False:
            Database.setSymbolValue("core", "ADC_CORE" + str(n) + "_INTERRUPT_HANDLER", "ADC_CORE" + str(n) + "_Handler", 2)
        else:
            Database.setSymbolValue("core", "ADC_CORE" + str(n) + "_INTERRUPT_HANDLER", "ADC_CORE" + str(n) + "_InterruptHandler", 2)

def updateCoreIntEnabled (symbol, event):
    global nSARCore

    localComponent = symbol.getComponent()

    symbol.setValue(False)

    for n in range(0, nSARCore):
        if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ADC_INTENSET") != 0:
            symbol.setValue(True)
            break

def updateADCMaxChannels (symbol, event):
    global nSARCore
    localComponent = symbol.getComponent()

    max_channels = 0

    for n in range(0, nSARCore):
        if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE") == True:
            max_channels = max(max_channels, nSARChannel[n])

    symbol.setValue(max_channels)

def updateEvctrlCMPEO (symbol, event):
    if event["value"] == True:
        symbol.setReadOnly(False)
    else:
        symbol.setReadOnly(True)
        symbol.setValue(False)

def updateEvctrlSTARTEI (symbol, event):
    global nSARChannel
    isTriggerSrcEventInput = False
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    # Enable (ReadOnly = False) STARTEI, if either the scan trigger source is >= 5 or any core channel trigger source is >=5
    scan_trigger_src = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC").getSelectedValue(), 16)

    if (scan_trigger_src >= 5):
        isTriggerSrcEventInput = True
    else:
        for k in range(0, numChannels):
            if isChannelEnabled(localComponent, n, k) == True:
                ch_trigger_src = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG4_5_TRGSRC").getSelectedValue(), 16)
                if (ch_trigger_src >= 5):
                    isTriggerSrcEventInput = True
                    break

    # Also update the STARTINV
    startInv = localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_EVCTRL_STARTINV")

    if isTriggerSrcEventInput == False:
        symbol.setReadOnly(True)
        symbol.setValue(False)
        startInv.setReadOnly(True)
        startInv.setValue(False)
    else:
        symbol.setReadOnly(False)
        startInv.setReadOnly(False)


def updateEvctrlRESRDYEO (symbol, event):
    global nSARChannel
    channelEnabled = False
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    for k in range(0, numChannels):
        channelEnabled = isChannelEnabled(localComponent, n, k)
        if channelEnabled == True:
            break

    if channelEnabled == False:
        symbol.setReadOnly(True)
        symbol.setValue(False)
    else:
        symbol.setReadOnly(False)

def updateEvsysChrdyGeneratorSymbols (symbol, event):
    global adcInstanceName
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    isADC_CHRDYC_x_Active = False

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")
    evctrl_resrdyeo = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO")

    if core_enabled == True and evctrl_resrdyeo == True:
        isADC_CHRDYC_x_Active = True

    Database.setSymbolValue("evsys", "GENERATOR_" + str(adcInstanceName.getValue()) + "_CHRDYC_" + str(n) + "_ACTIVE", isADC_CHRDYC_x_Active, 2)

def updateEvsysCmpGeneratorSymbols (symbol, event):
    global adcInstanceName
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    isADC_CMP_x_Active = False

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")
    evctrl_cmpeo = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO")

    if core_enabled == True and evctrl_cmpeo == True:
        isADC_CMP_x_Active = True

    Database.setSymbolValue("evsys", "GENERATOR_" + str(adcInstanceName.getValue()) + "_CMP_" + str(n) + "_ACTIVE", isADC_CMP_x_Active, 2)

def updateEvsysUserSymbols (symbol, event):
    global adcInstanceName
    global numTriggers
    global nSARCore

    trigger_src_list = []

    localComponent = symbol.getComponent()

    for n in range(0, nSARCore):
        numChannels = getNumCoreChannels(n)
        core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")
        evctrl_startei = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI")

        if (core_enabled == True) and (evctrl_startei == True):
            # Find the trigger source of SCAN Trigger and add to the list if trigger source is set to ADC Trigger Event User 0 – 10
            trigger_src = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC").getSelectedValue(), 16)
            if (trigger_src >= 5):
                trigger_src_list.append(trigger_src-5)      #Save x in ADC_TRIGGERS_x
            # Find channels that has the trigger source set to ADC Trigger Event User 0 – 10
            for k in range(0, numChannels):
                if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                    trigger_src = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG4_5_TRGSRC").getSelectedValue(), 16)
                    if (trigger_src >= 5):
                        trigger_src_list.append(trigger_src-5)      #Save x in ADC_TRIGGERS_x

    # Find out no. of ADC Event Triggers from the total available trigger sources (Typically numADCEventTriggers = 16-5 = 11)
    numADCEventTriggers = numTriggers - 5

    for n in range(0, numADCEventTriggers):
        if n in trigger_src_list:
            isADC_TRIGGERS_x_Ready = True
        else:
            isADC_TRIGGERS_x_Ready = False
        Database.setSymbolValue("evsys", "USER_" + str(adcInstanceName.getValue()) + "_TRIGGERS_" + str(n) + "_READY", isADC_TRIGGERS_x_Ready, 2)
#---------------------------------------------------------------------------------
def ADC_CORCTRL_REG_Update(symbol, event):
    global earlyInterruptPresent

    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    corctrl_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        adcdiv = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")
        strglvl = 0 if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_STRGLVL") == "Edge" else 1
        strgsrc = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC").getSelectedValue(), 16)
        scnrtds = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_SCNRTDS"))

        if earlyInterruptPresent == True:
            eirqovr = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_EIRQOVR"))
            eis = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_EIS")
        else:
            eirqovr = 0
            eis = 0
        selres = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CORCTRL_SELRES").getSelectedValue(), 16)
        samc = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CORCTRL_SAMC")

        corctrl_val = (adcdiv << 24) | (scnrtds << 22) | (strglvl << 21) | (strgsrc << 16) | (eirqovr << 15) | (eis << 12) | (selres << 10) | (samc)

    symbol.setValue(corctrl_val)

def ADC_CHNCFG1_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    chncfg1_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                chncmpen = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG1_CHNCMPEN"))
                lvl = 0 if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG1_LVL") == "Edge" else 1
                chncfg1_val |= (chncmpen << k) | (lvl << (k+16))

    symbol.setValue(chncfg1_val)

def ADC_CHNCFG2_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    chncfg2_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                fract = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG2_FRACT"))
                css = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG2_CSS"))
                chncfg2_val |= (fract << (k+16)) | (css << k)

    symbol.setValue(chncfg2_val)

def ADC_CHNCFG3_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    chncfg3_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                sign = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG3_SIGN"))
                css = 1 if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG3_DIFF") == "Differential" else 0
                chncfg3_val |= (sign << (k+16)) | (css << k)

    symbol.setValue(chncfg3_val)

def ADC_CHNCFG4_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)
    numChannels = 8 if numChannels > 8 else numChannels

    chncfg4_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                trgsrc = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_CHNCFG4_5_TRGSRC").getSelectedValue(), 16)
                chncfg4_val |= (trgsrc << (k*4))

    symbol.setValue(chncfg4_val)

def ADC_CHNCFG5_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)
    numChannels = numChannels - 8 if numChannels > 8 else 0

    chncfg5_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k+8) + "_ENABLE") == True:
                trgsrc = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_CH_" + str(k+8) + "_CHNCFG4_5_TRGSRC").getSelectedValue(), 16)
                chncfg5_val |= (trgsrc << (k*4))

    symbol.setValue(chncfg5_val)

def ADC_EVCTRL_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    evctrl_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        cmpeo = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO"))
        resrdyeo = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO"))
        startei = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI"))
        startinv = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_EVCTRL_STARTINV"))

        evctrl_val = (cmpeo << 5) | (resrdyeo << 4) | (startinv << 3) | (startei)

    symbol.setValue(evctrl_val)

def ADC_CMPCTRL_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    cmpctrl_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        iehihi = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_IEHIHI"))
        iehilo = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_IEHILO"))
        adcmphi = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPHI")
        iebtwn = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_IEBTWN"))
        ielohi = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_IELOHI"))
        ielolo = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_IELOLO"))
        cmpen = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_CMPEN"))
        adcmplo = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPLO")

        if cmpen == 1:
            cmpctrl_val = (iehihi << 29) | (iehilo << 28) | (adcmphi << 16) | (iebtwn << 15) | (ielohi << 14) | (ielolo << 13) | (cmpen << 12) | (adcmplo)

    symbol.setValue(cmpctrl_val)

def ADC_FLTCTRL_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())

    fltctrl_val = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        fltchnid = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_FLTCTRL_FLTCHNID")
        flten = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_FLTCTRL_FLTEN"))
        fmode = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_FLTCTRL_FMODE").getSelectedValue())
        ovrsam = int(localComponent.getSymbolByID("ADC_CORE_" + str(n) + "_FLTCTRL_OVRSAM").getSelectedValue(), 16)

        if flten == 1:
            fltctrl_val = (fltchnid << 10) | (flten << 8) | (fmode << 3) | (ovrsam)

    symbol.setValue(fltctrl_val)

def ADC_INTENSET_REG_Update(symbol, event):
    localComponent = symbol.getComponent()
    n = getCore(symbol.getID())
    numChannels = getNumCoreChannels(n)

    intenset_val = 0
    chrdy = 0

    core_enabled = localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")

    if core_enabled == True:
        for k in range(0, numChannels):
            if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_ENABLE") == True:
                chrdy |= int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_CH_" + str(k) + "_INTENSET_CHRDY")) << k
        eosrdy = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_INTENSET_EOSRDY"))
        chnerrc = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_INTENSET_CHNERRC"))
        fltrdy = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_INTENSET_FLTRDY"))
        cmphit = int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_INTENSET_CMPHIT"))

        intenset_val = (chrdy << 16) | (eosrdy << 11) | (chnerrc << 10) | (fltrdy << 9) | (cmphit << 4)

    symbol.setValue(intenset_val)

def ADC_PFFCTRL_REG_Update (symbol, event):
    global nSARCore
    localComponent = symbol.getComponent()

    pffctrl_val = 0
    pffcr = 0

    pffrdydma = int(localComponent.getSymbolByID("ADC_GLOBAL_PFFCTRL_PFFRDYDMA").getSelectedValue(), 16)
    for n in range(0, nSARCore):
        if localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE") == True:
            pffcr |= int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR")) << n

    pffen = 1 if pffcr != 0 else 0

    pffctrl_val = (pffrdydma << 16) | (pffcr << 4) | (pffen << 1)

    symbol.setValue(pffctrl_val)

def ADC_CTLINTENSET_REG_Update(symbol, event):
    global nSARCore
    localComponent = symbol.getComponent()

    ctlintenset_val = 0
    crrdy = 0

    pffhful = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_PFFHFUL")
    pffrdy = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_PFFRDY")
    pffovf = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_PFFOVF")
    pffunf = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_PFFUNF")
    vrefrdy = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_VREFRDY")
    vrefupd = localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_VREFUPD")

    for n in range(0, nSARCore):
        crrdy |= int(localComponent.getSymbolValue("ADC_GLOBAL_CTLINTENSET_CRRDY" + str(n))) << n

    ctlintenset_val = (pffhful << 11) | (pffrdy << 10) | (pffovf << 9) | (pffunf << 8) | (vrefrdy << 7) | (vrefupd << 6) | (crrdy)

    symbol.setValue(ctlintenset_val)

def ADC_CTRLD_REG_Update (symbol, event):
    global nSARCore
    localComponent = symbol.getComponent()

    ctrld_val = 0

    vrefsel = int(localComponent.getSymbolByID("ADC_GLOBAL_CTRLD_VREFSEL").getSelectedValue(), 16)
    wkupexp = localComponent.getSymbolValue("ADC_GLOBAL_CTRLD_WKUPEXP")
    clkdiv = localComponent.getSymbolValue("ADC_GLOBAL_CTRLD_CTLCKDIV")


    ctrld_val = (vrefsel << 28) | (wkupexp << 24)| (clkdiv << 8)

    symbol.setValue(ctrld_val)

def ADC_CTRLC_REG_Update (symbol, event):
    localComponent = symbol.getComponent()

    ctrlc_val = 0

    coreinterleaved = int(localComponent.getSymbolByID("ADC_GLOBAL_CTRLC_COREINTERLEAVED").getSelectedValue(), 16)
    cnt = localComponent.getSymbolValue("ADC_GLOBAL_CTRLC_CNT")

    ctrlc_val = (coreinterleaved << 28) | cnt

    symbol.setValue(ctrlc_val)

def ADC_CTRLA_REG_Update (symbol, event):
    localComponent = symbol.getComponent()

    ctrla_val = 0x00000004

    ondemand = int(localComponent.getSymbolValue("ADC_GLOBAL_CTRLA_ONDEMAND"))
    runstdby = int(localComponent.getSymbolValue("ADC_GLOBAL_CTRLA_RUNSTDBY"))

    ctrla_val |= (ondemand << 7) | (runstdby << 6)

    symbol.setValue(ctrla_val)

def ADC_CTRLD__ANLEN_Update(symbol, event):
    global nSARCore

    localComponent = symbol.getComponent()

    anlen = 0

    for n in range(0, nSARCore):
        anlen |= int(localComponent.getSymbolValue("ADC_CORE_" + str(n) + "_ENABLE")) << n

    if symbol.getID() == "ADC_CTLINTFLAG__CRDY":
        symbol.setValue(anlen)
    elif symbol.getID() == "ADC_CTRLD__CHNEN":
        symbol.setValue(anlen << 16)
    else:
        symbol.setValue(anlen << 20)

#---------------------------------------------------------------------------------
def readATDF(adcInstanceName, adcComponent):
    global nSARCore
    global nSARChannel
    global earlyInterruptPresent
    global numTriggers

    print "adcInstanceName = " + str(adcInstanceName)

    # Read Number of SAR Cores
    adc_param_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName+"\"]/parameters")
    adc_param = adc_param_node.getChildren()

    for index in range(0, len(adc_param)):
        param_name = adc_param[index].getAttribute("name")

        if "SARCORE_NMBR" in param_name:
            nSARCore = adc_param[index].getAttribute("value")
        if "EARLY_INTR_PRESENT" in param_name:
            earlyInterruptPresent = True if adc_param[index].getAttribute("value") == "1" else False
        if "TRGS_NMBR" in param_name:
            numTriggers = int(adc_param[index].getAttribute("value"))

    nSARCore = int(nSARCore)


    # Read channels per SAR Core
    for index in range(0, nSARCore):
        nSARChannelParam = "CHNSAR_NMBR" + str(index+1)
        for index in range(0, len(adc_param)):
            if nSARChannelParam in adc_param[index].getAttribute("name"):
                nSARChannel.append(int(adc_param[index].getAttribute("value")))

    # Number of ADC Cores
    adcNumSARCores = adcComponent.createIntegerSymbol("ADC_NUM_SAR_CORES", None)
    adcNumSARCores.setDefaultValue(nSARCore)
    adcNumSARCores.setVisible(False)

    for n in range(0, nSARCore):
        adcMaxChannelsDepList.append("ADC_CORE_" + str(n) + "_ENABLE")

    adcMaxChannels = adcComponent.createIntegerSymbol("ADC_MAX_CHANNELS", None)
    adcMaxChannels.setDefaultValue(nSARChannel[0])
    adcMaxChannels.setVisible(False)
    adcMaxChannels.setDependencies(updateADCMaxChannels, adcMaxChannelsDepList)

def globalConfig(adcComponent):
    global nSARCore

    # Global interrupt config depends on ADC Core n symbols. Assume these symbols will be created and them to the dependency list.
    for n in range(0, nSARCore):
        adcGlobalFIFOIntDepList.append("ADC_CORE_" + str(n) + "_ENABLE")
        adcGlobalFIFOIntDepList.append("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR")

    # CTRLA.ONDEMAND
    CTRLA_ONDEMAND_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTRLA_ONDEMAND", None)
    CTRLA_ONDEMAND_Config.setLabel("Enable On-Demand mode")
    CTRLA_ONDEMAND_Config.setDefaultValue(False)
    ADC_CTRLA_REG_DepList.append("ADC_GLOBAL_CTRLA_ONDEMAND")

    # CTRLA.RUNSTDBY
    CTRLA_RUNSTDBY_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTRLA_RUNSTDBY", None)
    CTRLA_RUNSTDBY_Config.setLabel("Enable Standby mode")
    CTRLA_RUNSTDBY_Config.setDefaultValue(False)
    ADC_CTRLA_REG_DepList.append("ADC_GLOBAL_CTRLA_RUNSTDBY")

    clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+ "_CLOCK_FREQUENCY")

    # ADC Input Clock Frequency (TSRC_CLK)
    ADC_INPUT_CLK_FREQ_Config = adcComponent.createIntegerSymbol("ADC_GLOBAL_INPUT_CLK_FREQ", None)
    ADC_INPUT_CLK_FREQ_Config.setLabel("ADC Input Clock Frequency")
    ADC_INPUT_CLK_FREQ_Config.setDefaultValue(clock_freq)
    ADC_INPUT_CLK_FREQ_Config.setReadOnly(True)
    ADC_INPUT_CLK_FREQ_Config.setDependencies(updateInputClockFreq, ["core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    # CTRLD.CTLCKDIV (TQ = (CTRLD.CTLCKDIV + 1)·TSRC_CLK)
    CTRLD_CTLCKDIV_Config = adcComponent.createIntegerSymbol("ADC_GLOBAL_CTRLD_CTLCKDIV", None)
    CTRLD_CTLCKDIV_Config.setLabel("ADC Clock Source to Control Clock Divider")
    CTRLD_CTLCKDIV_Config.setMin(0)
    CTRLD_CTLCKDIV_Config.setMax(65535)
    CTRLD_CTLCKDIV_Config.setDefaultValue(0)
    ADC_CTRLD_REG_DepList.append("ADC_GLOBAL_CTRLD_CTLCKDIV")

    adc_control_clock_freq = adcComponent.createIntegerSymbol("ADC_GLOBAL_CONTROL_CLOCK_FREQ", None)
    adc_control_clock_freq.setVisible(False)
    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(adc_control_clock_freq.getComponent())
    adc_control_clock_freq.setValue(F_CTRL_CLK)
    adc_control_clock_freq.setDependencies(updateControlClockFreq, ["ADC_GLOBAL_INPUT_CLK_FREQ", "ADC_GLOBAL_CTRLD_CTLCKDIV"])

    adc_control_clock_period_tq = adcComponent.createCommentSymbol("ADC_GLOBAL_CONTROL_CLOCK_PERIOD_TQ", None)
    F_CTRL_CLK, TQ, F_CTRL_CLK_MHZ, TQ_USEC = controlClockCalculate(adc_control_clock_period_tq.getComponent())
    adc_control_clock_period_tq.setLabel("[ Control Clock: Freq = " + F_CTRL_CLK_MHZ + " MHz, Period TQ = " + TQ_USEC + "micro sec ]")
    adc_control_clock_period_tq.setDependencies(updateControlClockPeriodTQ, ["ADC_GLOBAL_CONTROL_CLOCK_FREQ"])


    # CTRLD.WKUPEXP (2 Power (WKUPEXP) * TAD)
    CTRLD_WKUPEXP_Config = adcComponent.createIntegerSymbol("ADC_GLOBAL_CTRLD_WKUPEXP", None)
    CTRLD_WKUPEXP_Config.setLabel("Wake Up Delay Exponent (2^WKUPEXP * TAD)")
    CTRLD_WKUPEXP_Config.setMin(4)
    CTRLD_WKUPEXP_Config.setMax(15)
    CTRLD_WKUPEXP_Config.setDefaultValue(4)
    ADC_CTRLD_REG_DepList.append("ADC_GLOBAL_CTRLD_WKUPEXP")


    # CTRLD.VREFSEL
    adc_vref_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"CTRLD__VREFSEL\"]").getChildren()

    CTRLD_VREFSEL_Config = adcComponent.createKeyValueSetSymbol("ADC_GLOBAL_CTRLD_VREFSEL", None)
    CTRLD_VREFSEL_Config.setLabel("VREF Input Selection")

    for id in range(len(adc_vref_values)):
        key = adc_vref_values[id].getAttribute("name")
        value = adc_vref_values[id].getAttribute("value")
        description = adc_vref_values[id].getAttribute("caption")
        CTRLD_VREFSEL_Config.addKey(key, value, description)
    CTRLD_VREFSEL_Config.setDefaultValue(0)
    CTRLD_VREFSEL_Config.setOutputMode("Key")
    CTRLD_VREFSEL_Config.setDisplayMode("Description")
    ADC_CTRLD_REG_DepList.append("ADC_GLOBAL_CTRLD_VREFSEL")

    # CTRLC.COREINTERLEAVED
    adc_core_interleaved_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"CTRLC__COREINTERLEAVED\"]").getChildren()

    CTRLC_COREINTERLEAVED_Config = adcComponent.createKeyValueSetSymbol("ADC_GLOBAL_CTRLC_COREINTERLEAVED", None)
    CTRLC_COREINTERLEAVED_Config.setLabel("ADC Core Interleaving")

    for id in range(len(adc_core_interleaved_values)):
        key = adc_core_interleaved_values[id].getAttribute("name")
        value = adc_core_interleaved_values[id].getAttribute("value")
        description = adc_core_interleaved_values[id].getAttribute("caption")
        CTRLC_COREINTERLEAVED_Config.addKey(key, value, description)
        if value == "0x0":
            CTRLC_COREINTERLEAVED_Config.setDefaultValue(id)
    CTRLC_COREINTERLEAVED_Config.setOutputMode("Key")
    CTRLC_COREINTERLEAVED_Config.setDisplayMode("Description")
    ADC_CTRLC_REG_DepList.append("ADC_GLOBAL_CTRLC_COREINTERLEAVED")

    # CTRLC.CNT
    CTRLC_CNT_Config = adcComponent.createIntegerSymbol("ADC_GLOBAL_CTRLC_CNT", None)
    CTRLC_CNT_Config.setLabel("Delay Counter (TQ based) for STRIG Sync Trigger")
    CTRLC_CNT_Config.setMin(0)
    CTRLC_CNT_Config.setMax(65535)
    CTRLC_CNT_Config.setDefaultValue(0)
    #CTRLC_CNT_Config.setDependencies(updateTriggerDelayCounter, ["ADC_GLOBAL_CTRLC_COREINTERLEAVED"])
    ADC_CTRLC_REG_DepList.append("ADC_GLOBAL_CTRLC_CNT")

    adc_delay_time = adcComponent.createCommentSymbol("ADC_GLOBAL_DELAY_TIME", None)
    delayTimeUsec = delayTimeCalculate(CTRLC_CNT_Config.getComponent())
    adc_delay_time.setLabel("[ Delay Time = " + delayTimeUsec + " micro sec ]")
    adc_delay_time.setDependencies(updateDelayTime, ["ADC_GLOBAL_CONTROL_CLOCK_FREQ", "ADC_GLOBAL_CTRLC_CNT"])

    # PFFCTRL.PFFRDYDMA
    pffrdydma_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"PFFCTRL__PFFRDYDMA\"]").getChildren()

    PFFCTRL_PFFRDYDMA_Config = adcComponent.createKeyValueSetSymbol("ADC_GLOBAL_PFFCTRL_PFFRDYDMA", None)
    PFFCTRL_PFFRDYDMA_Config.setLabel("DMA Trigger Selection")

    for id in range(len(pffrdydma_values)):
        key = pffrdydma_values[id].getAttribute("name")
        value = pffrdydma_values[id].getAttribute("value")
        description = pffrdydma_values[id].getAttribute("caption")
        PFFCTRL_PFFRDYDMA_Config.addKey(key, value, description)
    PFFCTRL_PFFRDYDMA_Config.setDefaultValue(0)
    PFFCTRL_PFFRDYDMA_Config.setOutputMode("Key")
    PFFCTRL_PFFRDYDMA_Config.setDisplayMode("Key")
    ADC_PFFCTRL_REG_DepList.append("ADC_GLOBAL_PFFCTRL_PFFRDYDMA")

    ##Interrupt Configuration Menu:
    global_interrupt_config_menu = adcComponent.createMenuSymbol("ADC_GLOBAL_INTERRUPT_CONFIG", None)
    global_interrupt_config_menu.setLabel("Global Interrupt Configuration")

    # CTLINTENSET.PFFHFUL
    CTLINTENSET_PFFHFUL_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_PFFHFUL", global_interrupt_config_menu)
    CTLINTENSET_PFFHFUL_Config.setLabel("Enable FIFO Half-Full (PFFHFUL) Interrupt")
    CTLINTENSET_PFFHFUL_Config.setDefaultValue(False)
    CTLINTENSET_PFFHFUL_Config.setReadOnly(True)
    CTLINTENSET_PFFHFUL_Config.setDependencies(updateCommonInterruptStatus, adcGlobalFIFOIntDepList)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_PFFHFUL")

    # CTLINTENSET.PFFRDY
    CTLINTENSET_PFFRDY_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_PFFRDY", global_interrupt_config_menu)
    CTLINTENSET_PFFRDY_Config.setLabel("Enable FIFO Data Ready (PFFRDY) Interrupt")
    CTLINTENSET_PFFRDY_Config.setDefaultValue(False)
    CTLINTENSET_PFFRDY_Config.setReadOnly(True)
    CTLINTENSET_PFFRDY_Config.setDependencies(updateCommonInterruptStatus, adcGlobalFIFOIntDepList)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_PFFRDY")

    # CTLINTENSET.PFFOVF
    CTLINTENSET_PFFOVF_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_PFFOVF", global_interrupt_config_menu)
    CTLINTENSET_PFFOVF_Config.setLabel("Enable FIFO Overflow (PFFOVF) Interrupt")
    CTLINTENSET_PFFOVF_Config.setDefaultValue(False)
    CTLINTENSET_PFFOVF_Config.setReadOnly(True)
    CTLINTENSET_PFFOVF_Config.setDependencies(updateCommonInterruptStatus, adcGlobalFIFOIntDepList)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_PFFOVF")

    # CTLINTENSET.PFFUNF
    CTLINTENSET_PFFUNF_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_PFFUNF", global_interrupt_config_menu)
    CTLINTENSET_PFFUNF_Config.setLabel("Enable FIFO Underflow (PFFUNF) Interrupt")
    CTLINTENSET_PFFUNF_Config.setDefaultValue(False)
    CTLINTENSET_PFFUNF_Config.setReadOnly(True)
    CTLINTENSET_PFFUNF_Config.setDependencies(updateCommonInterruptStatus, adcGlobalFIFOIntDepList)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_PFFUNF")

    # CTLINTENSET.VREFRDY
    CTLINTENSET_VREFRDY_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_VREFRDY", global_interrupt_config_menu)
    CTLINTENSET_VREFRDY_Config.setLabel("Enable Voltage Reference Ready (VREFRDY) Interrupt")
    CTLINTENSET_VREFRDY_Config.setDefaultValue(False)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_VREFRDY")

    # CTLINTENSET.VREFUPD
    CTLINTENSET_VREFUPD_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_VREFUPD", global_interrupt_config_menu)
    CTLINTENSET_VREFUPD_Config.setLabel("Enable Voltage Reference Update (VREFUPD) Interrupt")
    CTLINTENSET_VREFUPD_Config.setDefaultValue(False)
    ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_VREFUPD")

    for n in range(0, nSARCore):
        # CTLINTENSET.CRRDYn
        CTLINTENSET_CRRDY_Config = adcComponent.createBooleanSymbol("ADC_GLOBAL_CTLINTENSET_CRRDY" + str(n), global_interrupt_config_menu)
        CTLINTENSET_CRRDY_Config.setLabel("Enable Core " + str(n) + " Ready" + "(CRRDY" + str(n) + ")" " Interrupt")
        CTLINTENSET_CRRDY_Config.setDefaultValue(False)
        CTLINTENSET_CRRDY_Config.setDependencies(updateCoreReadyIntStatus, ["ADC_CORE_" + str(n) + "_ENABLE"])
        ADC_CTLINTENSET_REG_DepList.append("ADC_GLOBAL_CTLINTENSET_CRRDY" + str(n))



def channelConfig(n, channel, adcComponent, channel_config_menu):
    ##Channel Configuration Menu:
    channel_k_enable = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE", channel_config_menu)
    channel_k_enable.setLabel("Enable Channel " + str(channel))
    channel_k_enable.setDefaultValue(False)
    channel_k_enable.setVisible(False)
    coreCompartorEnableDepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    coreResultReadyEventOutputDepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    coreStartConvOnEventInputDepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    adcEvsysUserDepList.append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_CHNCFG1_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_CHNCFG2_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_CHNCFG3_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_CHNCFG4_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_CHNCFG5_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE")

    # CHNCFG2n.CSSk
    CHNCFG2_CSS_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG2_CSS", channel_k_enable)
    CHNCFG2_CSS_Config.setLabel("Include Channel in Scan")
    CHNCFG2_CSS_Config.setDefaultValue(False)
    CHNCFG2_CSS_Config.setVisible(False)
    CHNCFG2_CSS_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_CHNCFG2_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG2_CSS")

    # CHNCFG1n.CHNCMPENk
    CHNCFG1_CHNCMPEN_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG1_CHNCMPEN", channel_k_enable)
    CHNCFG1_CHNCMPEN_Config.setLabel("Enable Compare")
    CHNCFG1_CHNCMPEN_Config.setDefaultValue(False)
    CHNCFG1_CHNCMPEN_Config.setVisible(False)
    CHNCFG1_CHNCMPEN_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    coreCompartorEnableDepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG1_CHNCMPEN")
    ADC_CHNCFG1_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG1_CHNCMPEN")

    # CHNCFG3n.DIFF
    CHNCFG3_DIFF_Config = adcComponent.createComboSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG3_DIFF", channel_k_enable, ["Single Ended", "Differential"])
    CHNCFG3_DIFF_Config.setLabel("Mode")
    CHNCFG3_DIFF_Config.setDefaultValue("Single Ended")
    # Differential mode is not supported on Core 0. On other ADC Cores 1,2,3, the only differential channels allowed are {0,1}, {2,3}, {4,5}
    CHNCFG3_DIFF_Config.setReadOnly(n == 0 or not(channel == 0 or channel == 2 or channel == 4))
    CHNCFG3_DIFF_Config.setVisible(False)
    CHNCFG3_DIFF_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_CHNCFG3_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG3_DIFF")

    # CHNCFG4n.TRGSRCk / CHNCFG5n.TRGSRCk
    trgsrc_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"CHNCFG4_CHNCFG5__TRGSRC\"]").getChildren()

    CHNCFG4_5_TRGSRC_Config = adcComponent.createKeyValueSetSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG4_5_TRGSRC", channel_k_enable)
    CHNCFG4_5_TRGSRC_Config.setLabel("Trigger Source")
    for id in range(len(trgsrc_values)):
        key = trgsrc_values[id].getAttribute("name")
        value = trgsrc_values[id].getAttribute("value")
        description = trgsrc_values[id].getAttribute("caption")
        CHNCFG4_5_TRGSRC_Config.addKey(key, value, description)
        if value == "0x0":
            CHNCFG4_5_TRGSRC_Config.setDefaultValue(id)
    CHNCFG4_5_TRGSRC_Config.setOutputMode("Value")
    CHNCFG4_5_TRGSRC_Config.setDisplayMode("Description")
    CHNCFG4_5_TRGSRC_Config.setVisible(False)
    CHNCFG4_5_TRGSRC_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    if channel < 8:
        ADC_CHNCFG4_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG4_5_TRGSRC")
    else:
        ADC_CHNCFG5_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG4_5_TRGSRC")
    coreStartConvOnEventInputDepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG4_5_TRGSRC")
    adcEvsysUserDepList.append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG4_5_TRGSRC")

    # CHNCFG1n.LVL
    CHNCFG3_DIFF_Config = adcComponent.createComboSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG1_LVL", channel_k_enable, ["Edge", "Level (Trigger as long as Trigger Level is High)"])
    CHNCFG3_DIFF_Config.setLabel("Trigger Level")
    CHNCFG3_DIFF_Config.setDefaultValue("Edge")
    CHNCFG3_DIFF_Config.setVisible(False)
    CHNCFG3_DIFF_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_CHNCFG1_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG1_LVL")

    # CHNCFG2n.FRACTk
    CHNCFG2_FRACT_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG2_FRACT", channel_k_enable)
    CHNCFG2_FRACT_Config.setLabel("Enable Fractional Data Output Format")
    CHNCFG2_FRACT_Config.setDefaultValue(False)
    CHNCFG2_FRACT_Config.setVisible(False)
    CHNCFG2_FRACT_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_CHNCFG2_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG2_FRACT")

    # CHNCFG3n.SIGNk
    CHNCFG3_SIGN_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG3_SIGN", channel_k_enable)
    CHNCFG3_SIGN_Config.setLabel("Enable Signed Data Output Format")
    CHNCFG3_SIGN_Config.setDefaultValue(False)
    CHNCFG3_SIGN_Config.setVisible(False)
    CHNCFG3_SIGN_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_CHNCFG3_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_CHNCFG3_SIGN")

    # INTENSETn.CHRDY
    INTENSET_CHRDY_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_INTENSET_CHRDY", channel_k_enable)
    INTENSET_CHRDY_Config.setLabel("Enable Channel Ready Interrupt")
    INTENSET_CHRDY_Config.setDefaultValue(False)
    INTENSET_CHRDY_Config.setVisible(False)
    INTENSET_CHRDY_Config.setDependencies(channelVisibility, ["ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_ENABLE"])
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CH_" + str(channel) + "_INTENSET_CHRDY")

def coreConfig(n, nChannels, adcComponent):
    global earlyInterruptPresent

    coreCompartorEnableDepList.append([])
    adcConversionTimeDepList.append([])
    adcClockFreqDepList.append([])
    ADC_CORCTRL_REG_DepList.append([])
    ADC_CHNCFG1_REG_DepList.append([])
    ADC_CHNCFG2_REG_DepList.append([])
    ADC_CHNCFG3_REG_DepList.append([])
    ADC_CHNCFG4_REG_DepList.append([])
    ADC_CHNCFG5_REG_DepList.append([])
    ADC_EVCTRL_REG_DepList.append([])
    ADC_CMPCTRL_REG_DepList.append([])
    ADC_FLTCTRL_REG_DepList.append([])
    ADC_INTENSET_REG_DepList.append([])
    coreStartConvOnEventInputDepList.append([])
    coreResultReadyEventOutputDepList.append([])
    adcCoreConfigSymbolsList.append([])
    adcEvsysGenCHRDYCDepList.append([])
    adcEvsysGenCMPDepList.append([])

    adcConversionTimeDepList[n].append("core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY")
    adcConversionTimeDepList[n].append("ADC_GLOBAL_CTRLD_CTLCKDIV")

    # Core enable -
    adcCoreEnable = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_ENABLE", None)
    adcCoreEnable.setLabel("Enable ADC Core " + str(n))
    adcCoreEnable.setDefaultValue(False)

    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CHNCFG1_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CHNCFG2_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CHNCFG3_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CHNCFG4_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CHNCFG5_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_EVCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_FLTCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CTRLD_REG_DepList.append("ADC_CORE_" + str(n) + "_ENABLE")
    ADC_CTRLD__ANLEN_DepList.append("ADC_CORE_" + str(n) + "_ENABLE")
    adcConversionTimeDepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    adcClockFreqDepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    adcEvsysUserDepList.append("ADC_CORE_" + str(n) + "_ENABLE")
    adcEvsysGenCHRDYCDepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")
    adcEvsysGenCMPDepList[n].append("ADC_CORE_" + str(n) + "_ENABLE")

    # CORCTRL_SELRES
    adc_resolution_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"CORCTRL__SELRES\"]").getChildren()

    CORCTRL_SELRES_Config = adcComponent.createKeyValueSetSymbol("ADC_CORE_" + str(n) + "_CORCTRL_SELRES", adcCoreEnable)
    CORCTRL_SELRES_Config.setLabel("Select Resolution")

    for id in range(len(adc_resolution_values)):
        key = adc_resolution_values[id].getAttribute("name")
        value = adc_resolution_values[id].getAttribute("value")
        description = adc_resolution_values[id].getAttribute("caption")
        CORCTRL_SELRES_Config.addKey(key, value, description)
        if value == "0x3":
            CORCTRL_SELRES_Config.setDefaultValue(id)
    CORCTRL_SELRES_Config.setOutputMode("Key")
    CORCTRL_SELRES_Config.setDisplayMode("Description")
    CORCTRL_SELRES_Config.setVisible(False)
    adcConversionTimeDepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SELRES")
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SELRES")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SELRES")

    # CORCTRL_ADCDIV (TAD = 2*(CORCTRL_ADCDIV)*TQ)
    CORCTRL_ADCDIV_Config = adcComponent.createIntegerSymbol("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV", adcCoreEnable)
    CORCTRL_ADCDIV_Config.setLabel("Division Ratio for ADC Core Clock")
    CORCTRL_ADCDIV_Config.setMin(1)
    CORCTRL_ADCDIV_Config.setMax(127)
    CORCTRL_ADCDIV_Config.setDefaultValue(1)
    CORCTRL_ADCDIV_Config.setVisible(False)
    adcConversionTimeDepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV")

    # Comment: ADC Clock Frequency and TAD
    adc_clock_freq = adcComponent.createCommentSymbol("ADC_CORE_" + str(n) + "_ADC_CLOCK_FREQ", adcCoreEnable)

    adcCoreClockFreqMHz, adcCoreTimePeriodUsec = adcClockFreqCalculate(adc_clock_freq.getComponent(), n)

    adc_clock_freq.setVisible(False)
    adc_clock_freq.setLabel("[ ADC Clock Freq = " + adcCoreClockFreqMHz + " MHz, " + "TAD = " + adcCoreTimePeriodUsec + " micro sec ]")
    adcClockFreqDepList[n].extend(["ADC_GLOBAL_INPUT_CLK_FREQ", "ADC_GLOBAL_CTRLD_CTLCKDIV", "ADC_CORE_" + str(n) + "_CORCTRL_ADCDIV"])
    adc_clock_freq.setDependencies(adcClockFreqUpdate, adcClockFreqDepList[n])
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_ADC_CLOCK_FREQ")

    # CORCTRL_SAMC
    CORCTRL_SAMC_Config = adcComponent.createIntegerSymbol("ADC_CORE_" + str(n) + "_CORCTRL_SAMC", adcCoreEnable)
    CORCTRL_SAMC_Config.setLabel("Sample Count")
    CORCTRL_SAMC_Config.setMax(1023)
    CORCTRL_SAMC_Config.setVisible(False)
    if n == 0:
        CORCTRL_SAMC_Config.setMin(4)
        CORCTRL_SAMC_Config.setDefaultValue(4)
    else:
        CORCTRL_SAMC_Config.setMin(1)
        CORCTRL_SAMC_Config.setDefaultValue(1)
    adcConversionTimeDepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SAMC")
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SAMC")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SAMC")

    adc_conversion_time = adcComponent.createCommentSymbol("ADC_CORE_" + str(n) + "_ADC_CONVERSION_TIME", adcCoreEnable)

    sample_time_usec, conversion_time_usec, conversion_freq_mhz = conversionTimeCalculate(adc_conversion_time.getComponent(), n)

    adc_conversion_time.setVisible(False)
    adc_conversion_time.setLabel("[ Sampling Time = " + sample_time_usec + " micro sec, " + "Total Conversion Time = " + conversion_time_usec + " micro sec, " + "Max Sampling Freq = " + conversion_freq_mhz + " MHz ]")
    adc_conversion_time.setDependencies(conversionTimeUpdate, adcConversionTimeDepList[n])
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_ADC_CONVERSION_TIME")

    # CORCTRL_STRGSRC
    scan_trigger_src_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"CORCTRL__STRGSRC\"]").getChildren()

    CORCTRL_STRGSRC_Config = adcComponent.createKeyValueSetSymbol("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC", adcCoreEnable)
    CORCTRL_STRGSRC_Config.setLabel("Scan Trigger Source")

    for id in range(len(scan_trigger_src_values)):
        key = scan_trigger_src_values[id].getAttribute("name")
        value = scan_trigger_src_values[id].getAttribute("value")
        description = scan_trigger_src_values[id].getAttribute("caption")
        CORCTRL_STRGSRC_Config.addKey(key, value, description)
    CORCTRL_STRGSRC_Config.setDefaultValue(0)
    CORCTRL_STRGSRC_Config.setOutputMode("Key")
    CORCTRL_STRGSRC_Config.setDisplayMode("Description")
    CORCTRL_STRGSRC_Config.setVisible(False)
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC")
    coreStartConvOnEventInputDepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_STRGSRC")

    # CORCTRL_STRGLVL
    CORCTRL_STRGLVL_Config = adcComponent.createComboSymbol("ADC_CORE_" + str(n) + "_CORCTRL_STRGLVL", adcCoreEnable, ["Edge", "Level (SCAN will re-trigger as long as Trigger Level is High)"])
    CORCTRL_STRGLVL_Config.setLabel("Scan Trigger Level")
    CORCTRL_STRGLVL_Config.setDefaultValue("Edge")
    CORCTRL_STRGLVL_Config.setVisible(False)
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_STRGLVL")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_STRGLVL")


    # CORCTRL_SCNRTDS
    CORCTRL_SCNRTDS_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CORCTRL_SCNRTDS", adcCoreEnable)
    CORCTRL_SCNRTDS_Config.setLabel("Scan Re-trigger Disable")
    CORCTRL_SCNRTDS_Config.setDefaultValue(False)
    CORCTRL_SCNRTDS_Config.setVisible(False)
    ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SCNRTDS")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_SCNRTDS")

    # PFFCTRL.PFFCR
    PFFCTRL_PFFCR_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR", adcCoreEnable)
    PFFCTRL_PFFCR_Config.setLabel("Store ADC Results to FIFO")
    PFFCTRL_PFFCR_Config.setDefaultValue(False)
    PFFCTRL_PFFCR_Config.setVisible(False)
    ADC_PFFCTRL_REG_DepList.append("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_PFFCTRL_PFFCR")

    if earlyInterruptPresent == True:
        # CORCTRL.EIRQOVR
        CORCTRL_EIRQOVR_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CORCTRL_EIRQOVR", adcCoreEnable)
        CORCTRL_EIRQOVR_Config.setLabel("Enable Early Interrupts")
        CORCTRL_EIRQOVR_Config.setDefaultValue(False)
        CORCTRL_EIRQOVR_Config.setVisible(False)
        ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_EIRQOVR")
        adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_EIRQOVR")

        # CORCTRL.EIS
        CORCTRL_EIS_Config = adcComponent.createIntegerSymbol("ADC_CORE_" + str(n) + "_CORCTRL_EIS", adcCoreEnable)
        CORCTRL_EIS_Config.setLabel("TAD Clocks Prior to EOC At Which Early Interrupt Is Generated")
        CORCTRL_EIS_Config.setMin(0)
        CORCTRL_EIS_Config.setMax(7)
        CORCTRL_EIS_Config.setDefaultValue(0)
        CORCTRL_EIS_Config.setVisible(False)
        ADC_CORCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_EIS")
        adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CORCTRL_EIS")


    ##Digital Comparator Configuration Menu:
    dig_comparator_config_menu = adcComponent.createMenuSymbol("ADC_CORE_" + str(n) + "_COMPARATOR_CONFIG", adcCoreEnable)
    dig_comparator_config_menu.setLabel("Digital Comparator Configuration")
    dig_comparator_config_menu.setVisible(False)
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_COMPARATOR_CONFIG")

    # CMPCTRL.CMPEN
    CMPCTRL_CMPEN_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_CMPEN", dig_comparator_config_menu)
    CMPCTRL_CMPEN_Config.setLabel("Enable Comparator")
    CMPCTRL_CMPEN_Config.setDefaultValue(False)
    CMPCTRL_CMPEN_Config.setVisible(False)
    CMPCTRL_CMPEN_Config.setReadOnly(True)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_CMPEN")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_CMPEN")

    # CMPCTRL.ADCMPHI
    CMPCTRL_ADCMPHI_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPHI", dig_comparator_config_menu)
    CMPCTRL_ADCMPHI_Config.setLabel("Comparator High Limit")
    CMPCTRL_ADCMPHI_Config.setMin(0x00)
    CMPCTRL_ADCMPHI_Config.setMax(0xFFF)
    CMPCTRL_ADCMPHI_Config.setDefaultValue(0)
    CMPCTRL_ADCMPHI_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPHI")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPHI")

    # CMPCTRL.ADCMPLO
    CMPCTRL_ADCMPLO_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPLO", dig_comparator_config_menu)
    CMPCTRL_ADCMPLO_Config.setLabel("Comparator Low Limit")
    CMPCTRL_ADCMPLO_Config.setMin(0x00)
    CMPCTRL_ADCMPLO_Config.setMax(0xFFF)
    CMPCTRL_ADCMPLO_Config.setDefaultValue(0)
    CMPCTRL_ADCMPLO_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPLO")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_ADCMPLO")

    # CMPCTRL.IEHIHI
    CMPCTRL_IEHIHI_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_IEHIHI", dig_comparator_config_menu)
    CMPCTRL_IEHIHI_Config.setLabel("Enable Comparision Event - ADC value >= ADCMPHI")
    CMPCTRL_IEHIHI_Config.setDefaultValue(False)
    CMPCTRL_IEHIHI_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEHIHI")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEHIHI")

    # CMPCTRL.IEHILO
    CMPCTRL_IEHILO_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_IEHILO", dig_comparator_config_menu)
    CMPCTRL_IEHILO_Config.setLabel("Enable Comparision Event - ADC value < ADCMPHI")
    CMPCTRL_IEHILO_Config.setDefaultValue(False)
    CMPCTRL_IEHILO_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEHILO")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEHILO")

    # CMPCTRL.IELOHI
    CMPCTRL_IELOHI_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_IELOHI", dig_comparator_config_menu)
    CMPCTRL_IELOHI_Config.setLabel("Enable Comparision Event - ADC value >= ADCMPLO")
    CMPCTRL_IELOHI_Config.setDefaultValue(False)
    CMPCTRL_IELOHI_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IELOHI")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IELOHI")

    # CMPCTRL.IELOLO
    CMPCTRL_IELOLO_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_IELOLO", dig_comparator_config_menu)
    CMPCTRL_IELOLO_Config.setLabel("Enable Comparision Event - ADC value < ADCMPLO")
    CMPCTRL_IELOLO_Config.setDefaultValue(False)
    CMPCTRL_IELOLO_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IELOLO")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IELOLO")

    # CMPCTRL.IEBTWN
    CMPCTRL_IEBTWN_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_CMPCTRL_IEBTWN", dig_comparator_config_menu)
    CMPCTRL_IEBTWN_Config.setLabel("Enable Comparision Event - ADCMPLO <= ADC Value < ADCMPHI")
    CMPCTRL_IEBTWN_Config.setDefaultValue(False)
    CMPCTRL_IEBTWN_Config.setVisible(False)
    ADC_CMPCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEBTWN")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CMPCTRL_IEBTWN")

    ##Digital Filter Configuration Menu:
    dig_filter_config_menu = adcComponent.createMenuSymbol("ADC_CORE_" + str(n) + "_FILTER_CONFIG", adcCoreEnable)
    dig_filter_config_menu.setLabel("Digital Filter Configuration")
    dig_filter_config_menu.setVisible(False)
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_FILTER_CONFIG")

    # FLTCTRL.FLTEN
    FLTCTRL_FLTEN_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_FLTCTRL_FLTEN", dig_filter_config_menu)
    FLTCTRL_FLTEN_Config.setLabel("Enable Digital Filter")
    FLTCTRL_FLTEN_Config.setDefaultValue(False)
    FLTCTRL_FLTEN_Config.setVisible(False)
    ADC_FLTCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FLTEN")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FLTEN")

    # FLTCTRL.FLTCHNID
    FLTCTRL_FLTCHNID_Config = adcComponent.createIntegerSymbol("ADC_CORE_" + str(n) + "_FLTCTRL_FLTCHNID", dig_filter_config_menu)
    FLTCTRL_FLTCHNID_Config.setLabel("Channel ID to Filter")
    FLTCTRL_FLTCHNID_Config.setMin(0)
    FLTCTRL_FLTCHNID_Config.setMax(nChannels-1)
    FLTCTRL_FLTCHNID_Config.setDefaultValue(0)
    FLTCTRL_FLTCHNID_Config.setVisible(False)
    ADC_FLTCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FLTCHNID")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FLTCHNID")

    # FLTCTRL.FMODE
    FLTCTRL_FMODE_Config = adcComponent.createKeyValueSetSymbol("ADC_CORE_" + str(n) + "_FLTCTRL_FMODE", dig_filter_config_menu)
    FLTCTRL_FMODE_Config.setLabel("Mode")
    FLTCTRL_FMODE_Config.addKey("0", "0", "Oversampling Mode")
    FLTCTRL_FMODE_Config.addKey("1", "1", "Averaging Mode")
    FLTCTRL_FMODE_Config.setDefaultValue(0)
    FLTCTRL_FMODE_Config.setOutputMode("Key")
    FLTCTRL_FMODE_Config.setDisplayMode("Description")
    FLTCTRL_FMODE_Config.setVisible(False)
    ADC_FLTCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FMODE")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_FMODE")

    # FLTCTRL.OVRSAM
    oversampling_ratio_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"FLTCTRL__OVRSAM\"]").getChildren()

    FLTCTRL_OVRSAM_Config = adcComponent.createKeyValueSetSymbol("ADC_CORE_" + str(n) + "_FLTCTRL_OVRSAM", dig_filter_config_menu)
    FLTCTRL_OVRSAM_Config.setLabel("Oversampling Ratio")
    for id in range(len(oversampling_ratio_values)):
        key = oversampling_ratio_values[id].getAttribute("name")
        value = oversampling_ratio_values[id].getAttribute("value")
        description = oversampling_ratio_values[id].getAttribute("caption")
        FLTCTRL_OVRSAM_Config.addKey(key, value, description)
    FLTCTRL_OVRSAM_Config.setDefaultValue(0)
    FLTCTRL_OVRSAM_Config.setOutputMode("Value")
    FLTCTRL_OVRSAM_Config.setDisplayMode("Description")
    FLTCTRL_OVRSAM_Config.setVisible(False)
    ADC_FLTCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_OVRSAM")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_FLTCTRL_OVRSAM")

    ##Event Configuration Menu:
    event_config_menu = adcComponent.createMenuSymbol("ADC_CORE_" + str(n) + "_EVENT_CONFIG", adcCoreEnable)
    event_config_menu.setLabel("Event Configuration")
    event_config_menu.setVisible(False)
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_EVENT_CONFIG")

    # EVCTRLn.RESRDYEO
    EVCTRL_RESRDYEO_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO", event_config_menu)
    EVCTRL_RESRDYEO_Config.setLabel("Enable Result Ready Event Out")
    EVCTRL_RESRDYEO_Config.setDefaultValue(False)
    EVCTRL_RESRDYEO_Config.setVisible(False)
    EVCTRL_RESRDYEO_Config.setReadOnly(True)
    ADC_EVCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO")
    adcEvsysGenCHRDYCDepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_RESRDYEO")

    # EVCTRLn.CMPEO
    EVCTRL_CMPEO_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO", event_config_menu)
    EVCTRL_CMPEO_Config.setLabel("Enable Digital Comparator Event Out")
    EVCTRL_CMPEO_Config.setDefaultValue(False)
    EVCTRL_CMPEO_Config.setVisible(False)
    EVCTRL_CMPEO_Config.setReadOnly(True)
    EVCTRL_CMPEO_Config.setDependencies(updateEvctrlCMPEO, ["ADC_CORE_" + str(n) + "_CMPCTRL_CMPEN"])
    ADC_EVCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO")
    adcEvsysGenCMPDepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_CMPEO")

    # EVCTRLn.STARTEI
    EVCTRL_STARTEI_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI", event_config_menu)
    EVCTRL_STARTEI_Config.setLabel("Start Conversion on Event Input")
    EVCTRL_STARTEI_Config.setDefaultValue(False)
    EVCTRL_STARTEI_Config.setVisible(False)
    EVCTRL_STARTEI_Config.setReadOnly(True)
    ADC_EVCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI")
    adcEvsysUserDepList.append("ADC_CORE_" + str(n) + "_EVCTRL_STARTEI")

    # EVCTRLn.STARTINV
    EVCTRL_STARTINV_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVCTRL_STARTINV", event_config_menu)
    EVCTRL_STARTINV_Config.setLabel("Start Conversion Event Invert Enable")
    EVCTRL_STARTINV_Config.setDefaultValue(False)
    EVCTRL_STARTINV_Config.setVisible(False)
    EVCTRL_STARTINV_Config.setReadOnly(True)
    ADC_EVCTRL_REG_DepList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_STARTINV")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_EVCTRL_STARTINV")

    ##Channel Configuration Menu:
    channel_config_menu = adcComponent.createMenuSymbol("ADC_CORE_" + str(n) + "_CHANNEL_CONFIG", adcCoreEnable)
    channel_config_menu.setLabel("Channel Configuration")
    channel_config_menu.setVisible(False)
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_CHANNEL_CONFIG")

    for channel in range(0, nChannels):
        channelConfig(n, channel, adcComponent, channel_config_menu)

    # Update ADC core symbols that are dependent on core channels
    CMPCTRL_CMPEN_Config.setDependencies(coreComparatorEnable, coreCompartorEnableDepList[n])
    EVCTRL_RESRDYEO_Config.setDependencies(updateEvctrlRESRDYEO, coreResultReadyEventOutputDepList[n])
    EVCTRL_STARTEI_Config.setDependencies(updateEvctrlSTARTEI, coreStartConvOnEventInputDepList[n])

    ##Interrupt Configuration Menu:
    interrupt_config_menu = adcComponent.createMenuSymbol("ADC_CORE_" + str(n) + "_INTERRUPT_CONFIG", adcCoreEnable)
    interrupt_config_menu.setLabel("Core Interrupt Configuration")
    interrupt_config_menu.setVisible(False)
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_INTERRUPT_CONFIG")

    # INTENSETn.EOSRDY
    INTENSET_EOSRDY_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_INTENSET_EOSRDY", interrupt_config_menu)
    INTENSET_EOSRDY_Config.setLabel("Enable End of Scan (EOS) interrupt")
    INTENSET_EOSRDY_Config.setDefaultValue(False)
    INTENSET_EOSRDY_Config.setVisible(False)
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_INTENSET_EOSRDY")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_INTENSET_EOSRDY")

    # INTENSETn.CMPHIT
    INTENSET_CMPHIT_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_INTENSET_CMPHIT", interrupt_config_menu)
    INTENSET_CMPHIT_Config.setLabel("Enable Comparator Hit (CMPHIT) interrupt")
    INTENSET_CMPHIT_Config.setDefaultValue(False)
    INTENSET_CMPHIT_Config.setVisible(False)
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_INTENSET_CMPHIT")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_INTENSET_CMPHIT")

    # INTENSETn.FLTRDY
    INTENSET_FLTRDY_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_INTENSET_FLTRDY", interrupt_config_menu)
    INTENSET_FLTRDY_Config.setLabel("Enable Filter Ready (FLTRDY) interrupt")
    INTENSET_FLTRDY_Config.setDefaultValue(False)
    INTENSET_FLTRDY_Config.setVisible(False)
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_INTENSET_FLTRDY")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_INTENSET_FLTRDY")

    # INTENSETn.CHNERRC
    INTENSET_CHNERRC_Config = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_INTENSET_CHNERRC", interrupt_config_menu)
    INTENSET_CHNERRC_Config.setLabel("Enable Channel Overwritten Error (CHNERRC) interrupt")
    INTENSET_CHNERRC_Config.setDefaultValue(False)
    INTENSET_CHNERRC_Config.setVisible(False)
    ADC_INTENSET_REG_DepList[n].append("ADC_CORE_" + str(n) + "_INTENSET_CHNERRC")
    adcCoreConfigSymbolsList[n].append("ADC_CORE_" + str(n) + "_INTENSET_CHNERRC")

    # Dummy symbol to trigger Core Symbols visibility:
    CoreSymbolsVisibility_Update = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_VISIBILITY_UPDATE", None)
    CoreSymbolsVisibility_Update.setVisible(False)
    CoreSymbolsVisibility_Update.setDependencies(coreSymVisibilityUpdate, ["ADC_CORE_" + str(n) + "_ENABLE"])


def coreRegisterConfig(n, adcComponent):
    # ADC_CORCTRL
    ADC_CORCTRL_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CORCTRL", None)
    if n == 0:
        ADC_CORCTRL_REG_Config.setDefaultValue(0x01000C04)
    else:
        ADC_CORCTRL_REG_Config.setDefaultValue(0x01000C01)
    ADC_CORCTRL_REG_Config.setVisible(False)
    ADC_CORCTRL_REG_Config.setDependencies(ADC_CORCTRL_REG_Update, ADC_CORCTRL_REG_DepList[n])

    # ADC_CHNCFG1
    ADC_CHNCFG1_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CHNCFG1", None)
    ADC_CHNCFG1_REG_Config.setDefaultValue(0x00000000)
    ADC_CHNCFG1_REG_Config.setVisible(False)
    ADC_CHNCFG1_REG_Config.setDependencies(ADC_CHNCFG1_REG_Update, ADC_CHNCFG1_REG_DepList[n])

    # ADC_CHNCFG2
    ADC_CHNCFG2_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CHNCFG2", None)
    ADC_CHNCFG2_REG_Config.setDefaultValue(0x00000000)
    ADC_CHNCFG2_REG_Config.setVisible(False)
    ADC_CHNCFG2_REG_Config.setDependencies(ADC_CHNCFG2_REG_Update, ADC_CHNCFG2_REG_DepList[n])

    # ADC_CHNCFG3
    ADC_CHNCFG3_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CHNCFG3", None)
    ADC_CHNCFG3_REG_Config.setDefaultValue(0x00000000)
    ADC_CHNCFG3_REG_Config.setVisible(False)
    ADC_CHNCFG3_REG_Config.setDependencies(ADC_CHNCFG3_REG_Update, ADC_CHNCFG3_REG_DepList[n])

    # ADC_CHNCFG4
    ADC_CHNCFG4_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CHNCFG4", None)
    ADC_CHNCFG4_REG_Config.setDefaultValue(0x00000000)
    ADC_CHNCFG4_REG_Config.setVisible(False)
    ADC_CHNCFG4_REG_Config.setDependencies(ADC_CHNCFG4_REG_Update, ADC_CHNCFG4_REG_DepList[n])

    # ADC_CHNCFG5
    ADC_CHNCFG5_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CHNCFG5", None)
    ADC_CHNCFG5_REG_Config.setDefaultValue(0x00000000)
    ADC_CHNCFG5_REG_Config.setVisible(False)
    ADC_CHNCFG5_REG_Config.setDependencies(ADC_CHNCFG5_REG_Update, ADC_CHNCFG5_REG_DepList[n])

    # ADC_EVCTRL
    ADC_EVCTRL_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_EVCTRL", None)
    ADC_EVCTRL_REG_Config.setDefaultValue(0x00000000)
    ADC_EVCTRL_REG_Config.setVisible(False)
    ADC_EVCTRL_REG_Config.setDependencies(ADC_EVCTRL_REG_Update, ADC_EVCTRL_REG_DepList[n])

    # ADC_CMPCTRL
    ADC_CMPCTRL_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_CMPCTRL", None)
    ADC_CMPCTRL_REG_Config.setDefaultValue(0x00000000)
    ADC_CMPCTRL_REG_Config.setVisible(False)
    ADC_CMPCTRL_REG_Config.setDependencies(ADC_CMPCTRL_REG_Update, ADC_CMPCTRL_REG_DepList[n])

    # ADC_FLTCTRL
    ADC_FLTCTRL_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_FLTCTRL", None)
    ADC_FLTCTRL_REG_Config.setDefaultValue(0x00000000)
    ADC_FLTCTRL_REG_Config.setVisible(False)
    ADC_FLTCTRL_REG_Config.setDependencies(ADC_FLTCTRL_REG_Update, ADC_FLTCTRL_REG_DepList[n])

    # ADC_INTENSET
    ADC_INTENSET_REG_Config = adcComponent.createHexSymbol("ADC_CORE_" + str(n) + "_ADC_INTENSET", None)
    ADC_INTENSET_REG_Config.setDefaultValue(0x00000000)
    ADC_INTENSET_REG_Config.setVisible(False)
    ADC_INTENSET_REG_Config.setDependencies(ADC_INTENSET_REG_Update, ADC_INTENSET_REG_DepList[n])
    adcCoreIntEnabledDepList.append("ADC_CORE_" + str(n) + "_ADC_INTENSET")

def commonRegisterConfig(adcComponent):

    # ADC_PFFCTRL
    ADC_PFFCTRL_REG_Config = adcComponent.createHexSymbol("ADC_PFFCTRL", None)
    ADC_PFFCTRL_REG_Config.setDefaultValue(0x00000000)
    ADC_PFFCTRL_REG_Config.setVisible(False)
    ADC_PFFCTRL_REG_Config.setDependencies(ADC_PFFCTRL_REG_Update, ADC_PFFCTRL_REG_DepList)

    # ADC_CTLINTENSET
    ADC_CTLINTENSET_REG_Config = adcComponent.createHexSymbol("ADC_CTLINTENSET", None)
    ADC_CTLINTENSET_REG_Config.setDefaultValue(0x00000000)
    ADC_CTLINTENSET_REG_Config.setVisible(False)
    ADC_CTLINTENSET_REG_Config.setDependencies(ADC_CTLINTENSET_REG_Update, ADC_CTLINTENSET_REG_DepList)

    # ADC_CTRLD
    ADC_CTRLD_REG_Config = adcComponent.createHexSymbol("ADC_CTRLD", None)
    ADC_CTRLD_REG_Config.setDefaultValue(0x04000000)        # Default value of WKUPEXP is 4
    ADC_CTRLD_REG_Config.setVisible(False)
    ADC_CTRLD_REG_Config.setDependencies(ADC_CTRLD_REG_Update, ADC_CTRLD_REG_DepList)

    # ADC_CTRLC
    ADC_CTRLC_REG_Config = adcComponent.createHexSymbol("ADC_CTRLC", None)
    ADC_CTRLC_REG_Config.setDefaultValue(0x00000000)
    ADC_CTRLC_REG_Config.setVisible(False)
    ADC_CTRLC_REG_Config.setDependencies(ADC_CTRLC_REG_Update, ADC_CTRLC_REG_DepList)

    # ADC_CTRLA
    ADC_CTRLA_REG_Config = adcComponent.createHexSymbol("ADC_CTRLA", None)
    ADC_CTRLA_REG_Config.setDefaultValue(0x00000004)        # Default, ANAEN is enabled
    ADC_CTRLA_REG_Config.setVisible(False)
    ADC_CTRLA_REG_Config.setDependencies(ADC_CTRLA_REG_Update, ADC_CTRLA_REG_DepList)

    # ADC_CTRLD__ANLEN
    ADC_CTRLD__ANLEN_BITS_Config = adcComponent.createHexSymbol("ADC_CTRLD__ANLEN", None)
    ADC_CTRLD__ANLEN_BITS_Config.setDefaultValue(0x00000000)
    ADC_CTRLD__ANLEN_BITS_Config.setVisible(False)
    ADC_CTRLD__ANLEN_BITS_Config.setDependencies(ADC_CTRLD__ANLEN_Update, ADC_CTRLD__ANLEN_DepList)

    # ADC_CTRLD__CHNEN
    ADC_CTRLD__CHNEN_BITS_Config = adcComponent.createHexSymbol("ADC_CTRLD__CHNEN", None)
    ADC_CTRLD__CHNEN_BITS_Config.setDefaultValue(0x00000000)
    ADC_CTRLD__CHNEN_BITS_Config.setVisible(False)
    ADC_CTRLD__CHNEN_BITS_Config.setDependencies(ADC_CTRLD__ANLEN_Update, ADC_CTRLD__ANLEN_DepList)

    # ADC_CTLINTFLAG__CRDY
    ADC_CTLINTFLAG__CRDY_BITS_Config = adcComponent.createHexSymbol("ADC_CTLINTFLAG__CRDY", None)
    ADC_CTLINTFLAG__CRDY_BITS_Config.setDefaultValue(0x00000000)
    ADC_CTLINTFLAG__CRDY_BITS_Config.setVisible(False)
    ADC_CTLINTFLAG__CRDY_BITS_Config.setDependencies(ADC_CTRLD__ANLEN_Update, ADC_CTRLD__ANLEN_DepList)

def adcInterruptHandlerConfig(adcComponent):
    global nSARCore

    # Dummy symbol to update ADC GLOBAL NVIC Interrupt
    adcGlobalNVICInt = adcComponent.createBooleanSymbol("ADC_GLOBAL_NVIC_INT", None)
    adcGlobalNVICInt.setVisible(False)
    adcGlobalNVICInt.setDependencies(updateAdcNVICInterrutps, ["ADC_CTLINTENSET"])

    for n in range(0, nSARCore):
        # Dummy symbols to update ADC CORE NVIC Interrupts
        adcCoreNVICInt = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_NVIC_INT", None)
        adcCoreNVICInt.setVisible(False)
        adcCoreNVICInt.setDependencies(updateAdcNVICInterrutps, ["ADC_CORE_" + str(n) + "_ADC_INTENSET"])

    # Dummy symbol to decide if any core interrupt is enabled and then used to conditionally generate core callback related APIs
    adcCoreIntEnabled = adcComponent.createBooleanSymbol("ADC_CORE_CORE_INT_ENABLED", None)
    adcCoreIntEnabled.setVisible(False)
    adcCoreIntEnabled.setDependencies(updateCoreIntEnabled, adcCoreIntEnabledDepList)

def adcEvsysConfig(adcComponent):
    global nSARCore

    # Dummy symbol to update EVSYS User symbols (ADC_TRIGGERS_x)
    adcCoreEVSYSUserUpdate = adcComponent.createBooleanSymbol("ADC_CORE_EVSYS_USER_UPDATE", None)
    adcCoreEVSYSUserUpdate.setVisible(False)
    adcCoreEVSYSUserUpdate.setDependencies(updateEvsysUserSymbols, adcEvsysUserDepList)

    for n in range(0, nSARCore):
        # Dummy symbol to update EVSYS CHRDY Generator symbols (ADC_CHRDYC_x)
        adcCoreEVSYSGenChrdyUpdate = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVSYS_GEN_CHRDY_UPDATE", None)
        adcCoreEVSYSGenChrdyUpdate.setVisible(False)
        adcCoreEVSYSGenChrdyUpdate.setDependencies(updateEvsysChrdyGeneratorSymbols, adcEvsysGenCHRDYCDepList[n])

        # Dummy symbol to update EVSYS CMP Generator symbols (ADC_CMP_x)
        adcCoreEVSYSGenCmpUpdate = adcComponent.createBooleanSymbol("ADC_CORE_" + str(n) + "_EVSYS_GEN_CMP_UPDATE", None)
        adcCoreEVSYSGenCmpUpdate.setVisible(False)
        adcCoreEVSYSGenCmpUpdate.setDependencies(updateEvsysCmpGeneratorSymbols, adcEvsysGenCMPDepList[n])



def codeGenerationConfig (adcComponent, Module):

    configName = Variables.get("__CONFIGURATION_NAME")

    adcHeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcHeaderFile.setSourcePath("../peripheral/adc_03620/templates/plib_adc.h.ftl")
    adcHeaderFile.setOutputName("plib_" + Module.lower() + ".h")
    adcHeaderFile.setDestPath("peripheral/adc/")
    adcHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcHeaderFile.setType("HEADER")
    adcHeaderFile.setMarkup(True)

    adcGlobalHeaderFile = adcComponent.createFileSymbol("ADC_GLOBALHEADER", None)
    adcGlobalHeaderFile.setSourcePath("../peripheral/adc_03620/templates/plib_adc_common.h.ftl")
    adcGlobalHeaderFile.setOutputName("plib_adc_common.h")
    adcGlobalHeaderFile.setDestPath("peripheral/adc/")
    adcGlobalHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcGlobalHeaderFile.setType("HEADER")
    adcGlobalHeaderFile.setMarkup(True)

    adcSourceFile = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSourceFile.setSourcePath("../peripheral/adc_03620/templates/plib_adc.c.ftl")
    adcSourceFile.setOutputName("plib_" + Module.lower() +".c")
    adcSourceFile.setDestPath("peripheral/adc/")
    adcSourceFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSourceFile.setType("SOURCE")
    adcSourceFile.setMarkup(True)

    adcSystemInitFile = adcComponent.createFileSymbol("ADC_INIT", None)
    adcSystemInitFile.setType("STRING")
    adcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSystemInitFile.setSourcePath("../peripheral/adc_03620/templates/system/initialization.c.ftl")
    adcSystemInitFile.setMarkup(True)

    adcSystemDefFile = adcComponent.createFileSymbol("ADC_DEF", None)
    adcSystemDefFile.setType("STRING")
    adcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSystemDefFile.setSourcePath("../peripheral/adc_03620/templates/system/definitions.h.ftl")
    adcSystemDefFile.setMarkup(True)

    # adcComponent.addPlugin("../peripheral/adc_03620/plugin/adc_03620.jar")


def instantiateComponent(adcComponent):
    global nSARCore
    global nSARChannel
    global adcInstanceName

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    Module = adcInstanceName.getValue()
    Log.writeInfoMessage("Running " + Module)

    # clock enable
    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    readATDF(adcInstanceName.getValue(), adcComponent)

    # Global config
    globalConfig(adcComponent)

    # ADC Core n and Channel k config
    for n in range(0, nSARCore):
        coreConfig(n, nSARChannel[n], adcComponent)

    # ADC Core registers
    for n in range(0, nSARCore):
        coreRegisterConfig(n, adcComponent)

    # ADC Common registers
    commonRegisterConfig(adcComponent)

    adcInterruptHandlerConfig(adcComponent)

    adcEvsysConfig(adcComponent)

    codeGenerationConfig(adcComponent, Module)