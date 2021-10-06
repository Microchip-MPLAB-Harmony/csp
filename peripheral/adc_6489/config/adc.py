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

###################################################################################################
######################################## Global variables #########################################
###################################################################################################

global adcInstanceName
global adcSym_NUM_CHANNELS
global seq

adcSym_SEQ1R_USCH = []
adcCHMenu = []
adcSym_CH_CHER = []
adcSym_CH_NAME = []
adcSym_CH_PositiveInput = []
adcSym_CH_NegativeInput = []
adcSym_CH_SHMR_DUAL = []
adcSym_CH_DUAL_CHANNEL = []
adcSym_CH_CGR_GAIN = []
adcSym_CH_COCR_AOFF = []
adcSym_CH_IER_EOC = []

###################################################################################################
############################################ Callbacks ############################################
###################################################################################################

def adcClockControl(symbol, event):

    clockSet = False
    Database.clearSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE")

    for channelID in range(0, adcSym_NUM_CHANNELS.getValue()):
        if adcSym_CH_CHER[channelID].getValue() == True:
            clockSet = True

    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", clockSet, 2)

def adcinterruptControl(symbol, event):

    nvicSet = False
    interruptVector = adcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = adcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = adcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    for channelID in range(0, adcSym_NUM_CHANNELS.getValue()):
        if (adcSym_CH_IER_EOC[channelID].getValue() == True):
            nvicSet = True

    localComponent = symbol.getComponent()
    if localComponent.getSymbolValue("ADC_IER_COMPE") == True:
        nvicSet = True

    if nvicSet == True:
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, adcInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, adcInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyClockStatus(symbol, event):

    clockSet = False
    clock = bool(Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE"))

    for channelID in range(0, adcSym_NUM_CHANNELS.getValue()):
        if adcSym_CH_CHER[channelID].getValue() == True:
            clockSet = True

    if clockSet == True and clock == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def dependencyIntStatus(symbol, event):

    nvicSet = False
    interruptVectorUpdate = adcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    nvic = bool(Database.getSymbolValue("core", interruptVectorUpdate))

    for channelID in range(0, adcSym_NUM_CHANNELS.getValue()):
        if adcSym_CH_IER_EOC[channelID].getValue() == True:
            nvicSet = True

    if nvicSet == True and nvic == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcGetMasterClock():

    main_clk_freq = int(Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY"))

    return main_clk_freq

def adcPrescalWarning(symbol, event):

    clock = adcGetMasterClock()
    prescaler = (adcSym_MR_PRESCAL.getValue() + 1) * 2
    adcFreq = clock / prescaler

    if adcFreq < 100000:
        symbol.setLabel("ADC Frequency < 100,000 Hz. Decrease prescaler value. ")
        symbol.setVisible(True)
    elif adcFreq > 10000000:
        symbol.setLabel("ADC Frequency > 10,000,000 Hz. Increase prescaler value. ")
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcFreqCalc(symbol, event):

    clock = adcGetMasterClock()
    prescaler = (adcSym_MR_PRESCAL.getValue() + 1) * 2
    adcFreq = clock / prescaler

    symbol.clearValue()
    symbol.setValue(adcFreq, 2)

def adcCalcConversionTime(adcSym_CONV_TIME, event):

    clock = adcGetMasterClock()
    if (clock == 0):
        clock = 1
    prescaler = (adcSym_MR_PRESCAL.getValue() + 1) * 2
    result_resolution = adcSym_EMR_RES_VALUE.getSelectedKey()
    multiplier = 1

    if result_resolution == "NO_AVERAGE":
        multiplier = 1
    if result_resolution == "OSR4":
        multiplier = 4
    if result_resolution == "OSR16":
        multiplier = 16
    if result_resolution == "OSR64":
        multiplier = 64
    if result_resolution == "OSR256":
        multiplier = 256

    conv_time = (prescaler * 20.0 * 1000000.0 * multiplier) / clock
    adcSym_CONV_TIME.setLabel("**** Conversion Time is " + str(conv_time) + " us ****")

def adcUserSeqVisible(symbol, event):

    for channelID in range(0, len(seq)):
        adcSym_SEQ1R_USCH[channelID].setVisible(event["value"])

def adcCHNameVisible(symbol, event):

    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    adcSym_CH_NAME[channelID].setVisible(event["value"])

def adcCHPosInpVisible(symbol, event):

    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    adcSym_CH_PositiveInput[channelID].setVisible(event["value"])

def adcCHNegInpVisible(symbol, event):

    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    component = symbol.getComponent()
    if component.getSymbolValue("ADC_MR_ANACH") == False:
        if component.getSymbolValue("ADC_" + str(channelID) + "_CHER") == True:
            adcSym_CH_NegativeInput[channelID].setVisible(True)
        else:
            adcSym_CH_NegativeInput[channelID].setVisible(False)
    else:
        if channelID != 0:
            adcSym_CH_NegativeInput[channelID].setVisible(False)

def adcCHInterruptVisible(symbol, event):

    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    adcSym_CH_IER_EOC[channelID].setVisible(event["value"])

def adcCHEnable(symbol, event):

    id = []
    #split as per "_" to get the channel number
    id = symbol.getID().split("_")
    channelID = int(id[1])

    #for diff mode, hide next odd channel
    if event["id"].find("_NEG_INP") > 0:
        if event["value"] == "AN" + str(channelID):
            adcCHMenu[channelID].setVisible(False)
        else:
            adcCHMenu[channelID].setVisible(True)

def adcTriggerVisible(symbol, event):

    symbol.setVisible(event["symbol"].getSelectedKey() == "HW_TRIGGER")


def adc_EMR_CMPSEL_Update(symbol, event):
    symbol.setVisible(event["value"] == False)
###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(adcComponent):

    global adcInstanceName

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())

    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = ["False", "False", "False", "False", "False", "False", "False", "False"] #array to save available channels
    adcChannelsValues = [] #array used for combo symbol
    adcChannelsValues.append("NONE")

    pinout = ""
    val = ATDF.getNode("/avr-tools-device-file/variants")
    children = val.getChildren()
    for index in range(0, len(children)):
        if packageName in children[index].getAttribute("package"):
            pinout = children[index].getAttribute("pinout")

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(pinout) + "\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    adc_signals = []
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"" + adcInstanceName.getValue() + "\"]/signals")
    adc_signals = adc.getChildren()
    for pad in range(0, len(adc_signals)):
        group = adc_signals[pad].getAttribute("group")
        if (("AD" in group) and ("index" in adc_signals[pad].getAttributeList())):
            padSignal = adc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(adc_signals[pad].getAttribute("index"))] = "True"
                adcChannelsValues.append("CH"+adc_signals[pad].getAttribute("index"))

    adcSym_AvailableChannels = adcComponent.createComboSymbol("ADC_AVAILABLE_CHANNELS", None, channel)
    adcSym_AvailableChannels.setVisible(False)

    adcMenu = adcComponent.createMenuSymbol("ADC_MENU", None)
    adcMenu.setLabel("ADC Configuration")

    # Fine number of channels from number of result registers
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group/register@[name=\"ADC_CDR\"]")
    adcChannels = node.getAttribute("count")

    #max no of channels
    global adcSym_NUM_CHANNELS
    adcSym_NUM_CHANNELS = adcComponent.createIntegerSymbol("ADC_NUM_CHANNELS", adcMenu)
    adcSym_NUM_CHANNELS.setDefaultValue(int(adcChannels))
    adcSym_NUM_CHANNELS.setVisible(False)

    adcSym_EMR_SRCCLK = adcComponent.createKeyValueSetSymbol("ADC_CLK_SRC", adcMenu)
    adcSym_EMR_SRCCLK.setLabel("Select Clock Source")

    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"" + adcInstanceName.getValue() + "\"]/parameters")
    clkSource = []
    clkSource = node.getChildren()
    for clock in range (0, len(clkSource)):
        if "SRCCLK" in clkSource[clock].getAttribute("name"):
            adcSym_EMR_SRCCLK.addKey(clkSource[clock].getAttribute("name"), clkSource[clock].getAttribute("value"), clkSource[clock].getAttribute("caption"))

    adcSym_EMR_SRCCLK.setOutputMode("Key")
    adcSym_EMR_SRCCLK.setDisplayMode("Description")
    adcSym_EMR_SRCCLK.setVisible(adcSym_EMR_SRCCLK.getKeyCount() > 0)

    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    #Clock prescaler
    global adcSym_MR_PRESCAL
    adcSym_MR_PRESCAL = adcComponent.createIntegerSymbol("ADC_MR_PRESCAL", adcMenu)
    adcSym_MR_PRESCAL.setLabel("Select Prescaler")
    adcSym_MR_PRESCAL.setDefaultValue(7)
    adcSym_MR_PRESCAL.setMin(0)
    adcSym_MR_PRESCAL.setMax(255)

    #clock selection
    global adcSym_Clock
    adcSym_Clock = adcComponent.createIntegerSymbol("ADC_CLK", adcMenu)
    adcSym_Clock.setLabel("Clock Frequency (Hz)")
    adcSym_Clock.setDefaultValue(Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY") / ((adcSym_MR_PRESCAL.getValue() + 1 ) * 2))
    adcSym_Clock.setReadOnly(True)
    adcSym_Clock.setDependencies(adcFreqCalc, ["ADC_CLK_SRC", "ADC_MR_PRESCAL", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    adcSym_PRESCAL_WARNING = adcComponent.createCommentSymbol("ADC_PRESCAL_WARNING", adcMenu)
    adcSym_PRESCAL_WARNING.setLabel("**** ADC Frequency = 18750000 Hz. ****")
    adcSym_PRESCAL_WARNING.setVisible(False)
    adcSym_PRESCAL_WARNING.setDependencies(adcPrescalWarning, ["ADC_CLK_SRC", "ADC_MR_PRESCAL", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Result resolution
    #Added keys here as combining two bit-fields EMR_STM and EMR_RES
    global adcSym_EMR_RES_VALUE
    adcSym_EMR_RES_VALUE = adcComponent.createKeyValueSetSymbol("ADC_EMR_RES_VALUE", adcMenu)
    adcSym_EMR_RES_VALUE.setLabel("Result Resolution")
    adcSym_EMR_RES_VALUE.setDefaultValue(0)
    adcSym_EMR_RES_VALUE.setOutputMode("Value")
    adcSym_EMR_RES_VALUE.setDisplayMode("Description")
    adcSym_EMR_RES_VALUE.addKey("NO_AVERAGE", "0", "12-bit")
    adcSym_EMR_RES_VALUE.addKey("OSR4_S", "1", "13-bit - single trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR4_M", "2", "13-bit - multi trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR16_S", "3", "14-bit - single trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR16_M", "4", "14-bit - multi trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR64_S", "5", "15-bit - single trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR64_M", "6", "15-bit - multi trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR256_S", "7", "16-bit - single trigger averaging")
    adcSym_EMR_RES_VALUE.addKey("OSR256_M", "8", "16-bit - multi trigger averaging")

    clock = Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY")

    if (clock != 0):
        time = (adcSym_MR_PRESCAL.getValue() + 1) * 2 * 20.0 * 1000000.0 / Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY")
    else:
        time = 0

    #Conversion time
    adcSym_CONV_TIME = adcComponent.createCommentSymbol("ADC_CONV_TIME", adcMenu)
    adcSym_CONV_TIME.setLabel("**** Conversion Time is " + str(time) + " us ****")
    adcSym_CONV_TIME.setDependencies(adcCalcConversionTime, ["ADC_CLK_SRC", "ADC_MR_PRESCAL", "ADC_EMR_RES_VALUE", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    adcSym_CONV_MODE = adcComponent.createKeyValueSetSymbol("ADC_CONV_MODE", adcMenu)
    adcSym_CONV_MODE.setLabel("Conversion Mode")
    adcSym_CONV_MODE.setDefaultValue(0)
    adcSym_CONV_MODE.setOutputMode("Value")
    adcSym_CONV_MODE.setDisplayMode("Description")
    adcSym_CONV_MODE.addKey("FREERUN", "0", "Free Run")
    adcSym_CONV_MODE.addKey("SW_TRIGGER", "1", "Software Trigger")
    adcSym_CONV_MODE.addKey("HW_TRIGGER", "2", "Hardware Trigger")

    #Trigger
    adcSym_MR_TRGSEL_VALUE = adcComponent.createKeyValueSetSymbol("ADC_MR_TRGSEL_VALUE", adcSym_CONV_MODE)
    adcSym_MR_TRGSEL_VALUE.setLabel("Select External Trigger Input")
    adcSym_MR_TRGSEL_VALUE.setVisible(False)
    adcSym_MR_TRGSEL_VALUE.setDefaultValue(1)
    adcSym_MR_TRGSEL_VALUE.setOutputMode("Key")
    adcSym_MR_TRGSEL_VALUE.setDisplayMode("Description")

    trigger_values = []
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName.getValue()+"\"]/parameters")
    trigger_values = adc.getChildren()
    for param in range(0, len(trigger_values)):
        if "TRGSEL" in trigger_values[param].getAttribute("name"):
            adcSym_MR_TRGSEL_VALUE.addKey(trigger_values[param].getAttribute("name"), trigger_values[param].getAttribute("value"), trigger_values[param].getAttribute("caption"))
    adcSym_MR_TRGSEL_VALUE.setDependencies(adcTriggerVisible, ["ADC_CONV_MODE"])

    #------------------------------------------------------------------------------------
    #user sequence menu
    adcUserSeq = adcComponent.createMenuSymbol("ADC_USER_SEQ", None)
    adcUserSeq.setLabel("User Channel Sequence Configuration")

    #user sequence comment
    adcSym_USEQ_COMMENT = adcComponent.createCommentSymbol("ADC_USEQ_COMMENT", adcUserSeq)
    adcSym_USEQ_COMMENT.setLabel("**** Configure selected channels in the Channel Configuration Menu ****")

    #enable user sequence
    adcSym_MR_USEQ = adcComponent.createBooleanSymbol("ADC_MR_USEQ", adcUserSeq)
    adcSym_MR_USEQ.setLabel("Enable User Sequence Mode")

    global seq
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group/register@[name=\"ADC_SEQR1\"]")
    seq = node.getChildren()

    for channelID in range(0, len(seq)):
        #channel selection for user sequence
        adcSym_SEQ1R_USCH.append(channelID)
        adcSym_SEQ1R_USCH[channelID] = adcComponent.createComboSymbol("ADC_SEQ1R_USCH" + str(channelID), adcSym_MR_USEQ, adcChannelsValues)
        adcSym_SEQ1R_USCH[channelID].setLabel("Select Channel for Sequence Number " + str(channelID + 1))
        adcSym_SEQ1R_USCH[channelID].setDefaultValue(adcChannelsValues[0])
        adcSym_SEQ1R_USCH[channelID].setVisible(False)
        adcSym_SEQ1R_USCH[channelID].setDependencies(adcUserSeqVisible, ["ADC_MR_USEQ"])
    #--------------------------------------------------------------------------------------

    adcCHConfMenu = adcComponent.createMenuSymbol("ADC_CH_CONF", None)
    adcCHConfMenu.setLabel("Channel Configuration")

    adcBitField_MR_ANACH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ADC"]/register-group@[name="ADC"]/register@[name="ADC_MR"]/bitfield@[name="ANACH"]')

    if adcBitField_MR_ANACH != None:
        adcSym_MR_ANACH = adcComponent.createBooleanSymbol("ADC_MR_ANACH", adcCHConfMenu)
        adcSym_MR_ANACH.setLabel("Use Channel0 DIFF setting for all the analog channels")

    # Loop runs for 8 channels and visibility of the channel is controlled as per available pins
    for channelID in range(0, len(channel)):
        #Channel menu
        global adcCHMenu
        adcCHMenu.append(channelID)
        adcCHMenu[channelID] = adcComponent.createMenuSymbol("CH" + str(channelID), adcCHConfMenu)
        adcCHMenu[channelID].setLabel("Channel " + str(channelID))
        #Show channels as per available pins in package
        if channel[channelID] == "False":
            adcCHMenu[channelID].setVisible(False)

        #Channel enable
        adcSym_CH_CHER.append(channelID)
        adcSym_CH_CHER[channelID] = adcComponent.createBooleanSymbol("ADC_" + str(channelID) + "_CHER", adcCHMenu[channelID])
        adcSym_CH_CHER[channelID].setLabel("Enable Channel " + str(channelID))

        #for diff mode, CH0 and CH1
        if channelID % 2 == 1:
            adcSym_CH_CHER[channelID].setDependencies(adcCHEnable, ["ADC_" + str(channelID - 1) + "_NEG_INP"])

        #Channel name
        adcSym_CH_NAME.append(channelID)
        adcSym_CH_NAME[channelID] = adcComponent.createStringSymbol("ADC_" + str(channelID) + "_NAME", adcSym_CH_CHER[channelID])
        adcSym_CH_NAME[channelID].setLabel("Name")
        adcSym_CH_NAME[channelID].setDefaultValue("CHANNEL_" + str(channelID))
        adcSym_CH_NAME[channelID].setVisible(False)
        adcSym_CH_NAME[channelID].setDependencies(adcCHNameVisible, ["ADC_" + str(channelID) + "_CHER"])

        #Channel positive input
        adcSym_CH_PositiveInput.append(channelID)
        adcSym_CH_PositiveInput[channelID] = adcComponent.createStringSymbol("ADC_" + str(channelID) + "_POS_INP", adcSym_CH_CHER[channelID])
        adcSym_CH_PositiveInput[channelID].setLabel("Positive Input")
        adcSym_CH_PositiveInput[channelID].setDefaultValue("AN" + str(channelID))
        adcSym_CH_PositiveInput[channelID].setReadOnly(True)
        adcSym_CH_PositiveInput[channelID].setVisible(False)
        adcSym_CH_PositiveInput[channelID].setDependencies(adcCHPosInpVisible, ["ADC_" + str(channelID) + "_CHER"])

        #Channel negative input
        adcSym_CH_NegativeInput.append(channelID)
        adc_EvenChNegInput = ["GND", "AN" + str(channelID + 1)]
        adc_OddChNegInput = ["GND"]

        if channelID % 2 == 1:
            adcSym_CH_NegativeInput[channelID] = adcComponent.createComboSymbol("ADC_" + str(channelID) + "_NEG_INP", adcSym_CH_CHER[channelID], adc_OddChNegInput)
            adcSym_CH_NegativeInput[channelID].setReadOnly(True)
        else:
            adcSym_CH_NegativeInput[channelID] = adcComponent.createComboSymbol("ADC_" + str(channelID) + "_NEG_INP", adcSym_CH_CHER[channelID], adc_EvenChNegInput)
            if channel[channelID + 1] == "False":
                adcSym_CH_NegativeInput[channelID].setReadOnly(True)

        adcSym_CH_NegativeInput[channelID].setLabel("Negative Input")
        adcSym_CH_NegativeInput[channelID].setDefaultValue("GND")
        adcSym_CH_NegativeInput[channelID].setVisible(False)
        adcSym_CH_NegativeInput[channelID].setDependencies(adcCHNegInpVisible, ["ADC_" + str(channelID) + "_CHER", "ADC_MR_ANACH"])

        #Channel interrupt
        adcSym_CH_IER_EOC.append(channelID)
        adcSym_CH_IER_EOC[channelID] = adcComponent.createBooleanSymbol("ADC_" + str(channelID) + "_IER_EOC", adcSym_CH_CHER[channelID])
        adcSym_CH_IER_EOC[channelID].setLabel("End of conversion interrupt")
        adcSym_CH_IER_EOC[channelID].setVisible(False)
        adcSym_CH_IER_EOC[channelID].setDependencies(adcCHInterruptVisible, ["ADC_" + str(channelID) + "_CHER"])

    adcComparatorMenu = adcComponent.createMenuSymbol("ADC_COMPARE_MENU", None)
    adcComparatorMenu.setLabel("Comparator Configuration")

    adcSym_EMR_CMPALL = adcComponent.createBooleanSymbol("ADC_EMR_CMPALL", adcComparatorMenu)
    adcSym_EMR_CMPALL.setLabel("Compare all channels")
    adcSym_EMR_CMPALL.setDefaultValue(False)

    adcSym_EMR_CMPSEL = adcComponent.createKeyValueSetSymbol("ADC_EMR_CMPSEL", adcComparatorMenu)
    adcSym_EMR_CMPSEL.setLabel("Compare Channel")
    adcSym_EMR_CMPSEL.setOutputMode("Value")
    adcSym_EMR_CMPSEL.setDisplayMode("Description")
    for channelID in range(0, len(channel)):
        #Show channels as per available pins in package
        if (channel[channelID] == "True"):
            adcSym_EMR_CMPSEL.addKey("CHANNEL_" + str(channelID), str(channelID), "Channel " + str(channelID))

    adcSym_EMR_CMPSEL.setDependencies(adc_EMR_CMPSEL_Update, ["ADC_EMR_CMPALL"])

    adcSym_CWR_HIGHTHRES = adcComponent.createIntegerSymbol("ADC_CWR_HIGHTHRES", adcComparatorMenu)
    adcSym_CWR_HIGHTHRES.setLabel("High Threshold")
    adcSym_CWR_HIGHTHRES.setMin(0)
    adcSym_CWR_HIGHTHRES.setMax(65535)
    adcSym_CWR_HIGHTHRES.setDefaultValue(0)

    adcSym_CWR_LOWTHRES = adcComponent.createIntegerSymbol("ADC_CWR_LOWTHRES", adcComparatorMenu)
    adcSym_CWR_LOWTHRES.setLabel("Low Threshold")
    adcSym_CWR_LOWTHRES.setMin(0)
    adcSym_CWR_LOWTHRES.setMax(65535)
    adcSym_CWR_LOWTHRES.setDefaultValue(0)

    adcSym_EMR_CMPMODE = adcComponent.createKeyValueSetSymbol("ADC_EMR_CMPMODE", adcComparatorMenu)
    adcSym_EMR_CMPMODE.setLabel("Compare Mode")
    adcSym_EMR_CMPMODE.setDefaultValue(0)
    adcSym_EMR_CMPMODE.setOutputMode("Key")
    adcSym_EMR_CMPMODE.setDisplayMode("Description")
    adcSym_EMR_CMPMODE.addKey("LOW", "0", "Generates an event when the converted data is lower than the low threshold of the window")
    adcSym_EMR_CMPMODE.addKey("HIGH", "1", "Generates an event when the converted data is higher than the high threshold of the window")
    adcSym_EMR_CMPMODE.addKey("IN", "2", "Generates an event when the converted data is in the comparison window")
    adcSym_EMR_CMPMODE.addKey("OUT", "3", "Generates an event when the converted data is out of the comparison window")

    adcSym_EMR_CMPFILTER = adcComponent.createIntegerSymbol("ADC_EMR_CMPFILTER", adcComparatorMenu)
    adcSym_EMR_CMPFILTER.setLabel("Compare Event Filter")
    adcSym_EMR_CMPFILTER.setDefaultValue(0)
    adcSym_EMR_CMPFILTER.setMin(0)
    adcSym_EMR_CMPFILTER.setMax(3)

    adcSym_EMR_CMPTYPE = adcComponent.createKeyValueSetSymbol("ADC_EMR_CMPTYPE", adcComparatorMenu)
    adcSym_EMR_CMPTYPE.setLabel("Comparision Type")
    adcSym_EMR_CMPTYPE.addKey("ADC_EMR_CMPTYPE_FLAG_ONLY", "0" , "Flag Only")
    adcSym_EMR_CMPTYPE.addKey("ADC_EMR_CMPTYPE_START_CONDITION", "1" , "Start Condition")
    adcSym_EMR_CMPTYPE.setOutputMode("Key")
    adcSym_EMR_CMPTYPE.setDisplayMode("Description")
    adcSym_EMR_CMPTYPE.setDefaultValue(0)

    adcSym_EMR_COMPE = adcComponent.createBooleanSymbol("ADC_IER_COMPE", adcComparatorMenu)
    adcSym_EMR_COMPE.setLabel("Enable Compare Interrupt")
    adcSym_EMR_COMPE.setDefaultValue(False)

    #--------------------------------------------------------------------------------------
    # Clock dynamic settings
    adcSym_ClockControl = adcComponent.createBooleanSymbol(adcInstanceName.getValue() + "_CLOCK_ENABLE", None)
    adcSym_ClockControl.setDependencies(adcClockControl, ["ADC_0_CHER", "ADC_1_CHER", "ADC_2_CHER", "ADC_3_CHER", "ADC_4_CHER", \
        "ADC_5_CHER", "ADC_6_CHER", "ADC_7_CHER"])
    adcSym_ClockControl.setVisible(False)

    # NVIC Dynamic settings
    adcSym_interruptControl = adcComponent.createBooleanSymbol("ADC_NVIC_ENABLE", None)
    adcSym_interruptControl.setDependencies(adcinterruptControl, ["ADC_0_IER_EOC", "ADC_1_IER_EOC", "ADC_2_IER_EOC", "ADC_3_IER_EOC", "ADC_4_IER_EOC",\
        "ADC_5_IER_EOC", "ADC_6_IER_EOC", "ADC_7_IER_EOC", "ADC_IER_COMPE"])
    adcSym_interruptControl.setVisible(False)

    # Dependency Status
    adcSym_ClkEnComment = adcComponent.createCommentSymbol("ADC_CLK_ENABLE_COMMENT", None)
    adcSym_ClkEnComment.setVisible(False)
    adcSym_ClkEnComment.setLabel("Warning!!! " + adcInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    adcSym_ClkEnComment.setDependencies(dependencyClockStatus, ["core." + adcInstanceName.getValue() + "_CLOCK_ENABLE", "ADC_0_CHER", "ADC_1_CHER", "ADC_2_CHER", "ADC_3_CHER", "ADC_4_CHER", \
        "ADC_5_CHER", "ADC_6_CHER", "ADC_7_CHER"])
    interruptVectorUpdate = adcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_NVIC_ENABLE_COMMENT", None)
    adcSym_IntEnComment.setVisible(False)
    adcSym_IntEnComment.setLabel("Warning!!! " + adcInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    adcSym_IntEnComment.setDependencies(dependencyIntStatus, ["core." + interruptVectorUpdate, "ADC_0_IER_EOC", "ADC_1_IER_EOC", "ADC_2_IER_EOC", "ADC_3_IER_EOC", "ADC_4_IER_EOC",\
        "ADC_5_IER_EOC", "ADC_6_IER_EOC", "ADC_7_IER_EOC", "ADC_IER_COMPE"])

    ###################################################################################################
    ######################################### Code Generation #########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    adcHeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcHeaderFile.setSourcePath("../peripheral/adc_6489/templates/plib_adc.h.ftl")
    adcHeaderFile.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".h")
    adcHeaderFile.setDestPath("peripheral/adc/")
    adcHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcHeaderFile.setType("HEADER")
    adcHeaderFile.setMarkup(True)

    adcGlobalHeaderFile = adcComponent.createFileSymbol("ADC_GLOBALHEADER", None)
    adcGlobalHeaderFile.setSourcePath("../peripheral/adc_6489/templates/plib_adc_common.h")
    adcGlobalHeaderFile.setOutputName("plib_adc_common.h")
    adcGlobalHeaderFile.setDestPath("peripheral/adc/")
    adcGlobalHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcGlobalHeaderFile.setType("HEADER")

    adcSource1File = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSource1File.setSourcePath("../peripheral/adc_6489/templates/plib_adc.c.ftl")
    adcSource1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".c")
    adcSource1File.setDestPath("peripheral/adc/")
    adcSource1File.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSource1File.setType("SOURCE")
    adcSource1File.setMarkup(True)

    adcSystemInitFile = adcComponent.createFileSymbol("ADC_INIT", None)
    adcSystemInitFile.setType("STRING")
    adcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSystemInitFile.setSourcePath("../peripheral/adc_6489/templates/system/initialization.c.ftl")
    adcSystemInitFile.setMarkup(True)

    adcSystemDefFile = adcComponent.createFileSymbol("ADC_DEF", None)
    adcSystemDefFile.setType("STRING")
    adcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSystemDefFile.setSourcePath("../peripheral/adc_6489/templates/system/definitions.h.ftl")
    adcSystemDefFile.setMarkup(True)

    adcComponent.addPlugin("../peripheral/adc_6489/plugin/adc_6489.jar")
