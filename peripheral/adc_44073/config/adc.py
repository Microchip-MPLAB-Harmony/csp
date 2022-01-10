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
########################### Global variables   #################################
###################################################################################################

adcSym_SEQR1_USCH = []
adcCHMenu = []
adcSym_CH_CHER = []
adcSym_CH_NAME = []
adcSym_CH_PositiveInput = []
adcSym_CH_NegativeInput = []
adcSym_CGR_Gain = []
adcSym_COR_Offset = []
adcSym_CH_IER_EOC = []

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################

def adcClockControl(symbol, event):
    clockSet = False
    Database.clearSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE")
    for channelID in range(0, Database.getSymbolValue(adcInstanceName.getValue().lower(), "ADC_NUM_CHANNELS")):
        if (adcSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True):
        Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    else:
        Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", False, 2)

def adcInterruptEnableDisableCallback(symbol, event):
    global interruptSymbolEnable
    deviceHandlerLastName =         "_InterruptHandler"
    interruptLastNameHandler =      "_INTERRUPT_HANDLER"
    interruptLastNameHandlerLock =  "_INTERRUPT_HANDLER_LOCK"
    interruptNamespace =    "core"
    interruptSymbolHandler =      adcInstanceName.getValue() + interruptLastNameHandler
    interruptSymbolHandlerLock =  adcInstanceName.getValue() + interruptLastNameHandlerLock
    interruptSet = False

    Database.clearSymbolValue("core", interruptSymbolHandlerLock)
    Database.clearSymbolValue("core", interruptSymbolEnable)
    Database.clearSymbolValue("core", interruptSymbolHandler)
    for channelID in range(0, Database.getSymbolValue(adcInstanceName.getValue().lower(), "ADC_NUM_CHANNELS")):
        if (adcSym_CH_IER_EOC[channelID].getValue() == True):
            interruptSet = True
    if (adcSym_IER_COMPE.getValue() == True):
        interruptSet = True
    if(interruptSet == True):
        Database.setSymbolValue( interruptNamespace, interruptSymbolEnable, True, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandler, adcInstanceName.getValue() + deviceHandlerLastName, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandlerLock, True, 2)
    else:
        #Do not try to restore the handler name to the default
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandlerLock, False, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolEnable, False, 2)

def dependencyClockStatus(symbol, event):
    clockSet = False
    clock = bool(Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE"))
    for channelID in range(0, Database.getSymbolValue(adcInstanceName.getValue().lower(), "ADC_NUM_CHANNELS")):
        if (adcSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True and clock == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def dependencyIntStatus(symbol, event):
    global interruptSymbolEnable
    interruptSet = False
    interrupt = bool(Database.getSymbolValue("core", interruptSymbolEnable))
    for channelID in range(0, Database.getSymbolValue(adcInstanceName.getValue().lower(), "ADC_NUM_CHANNELS")):
        if (adcSym_CH_IER_EOC[channelID].getValue() == True):
            interruptSet = True
    if (adcSym_IER_COMPE.getValue() == True):
        interruptSet = True
    if(interruptSet == True and interrupt == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcGetPeripheralClock():
    peripheral_clk_freq = int(Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    return peripheral_clk_freq

def adcPrescalWarning(symbol, event):
    clock = adcGetPeripheralClock()
    prescaler = adcSym_MR_PRESCAL.getValue() + 1
    adcFreq = clock / (2 * prescaler)
    if (adcFreq < 200000):
        symbol.setLabel("ADC Frequency < 200,000 Hz. Decrease prescaler value. ")
        symbol.setVisible(True)
    elif (adcFreq > 20000000):
        symbol.setLabel("ADC Frequency > 20,000,000 Hz. Increase prescaler value. ")
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcFreqCalc(symbol, event):
    clock = adcGetPeripheralClock()
    prescaler = adcSym_MR_PRESCAL.getValue() + 1
    adcFreq = clock / (2 * prescaler)
    symbol.clearValue()
    symbol.setValue(adcFreq, 2)

def adcCalcConversionTime(adcSym_CONV_TIME, event):
    clock = adcGetPeripheralClock()
    adcClockSourceInvalidSym.setVisible((clock == 0))
    if (clock == 0):
        clock = 1
    prescaler = adcSym_MR_PRESCAL.getValue() + 1
    over_sampling_rate = adcSym_EMR_OSR_VALUE.getSelectedKey()
    multiplier = 1
    if (over_sampling_rate == "NO_AVERAGE"):
        multiplier = 1
    elif (over_sampling_rate == "OSR4_SIN") or (over_sampling_rate == "OSR4_MUL"):
        multiplier = 4
    elif (over_sampling_rate == "OSR16_SIN") or (over_sampling_rate == "OSR16_MUL"):
        multiplier = 16
    elif (over_sampling_rate == "OSR64_SIN") or (over_sampling_rate == "OSR64_MUL"):
        multiplier = 64
    elif (over_sampling_rate == "OSR256_SIN") or (over_sampling_rate == "OSR256_MUL"):
        multiplier = 256
    if adcSym_MR_TRACKING_TIME_VALUE.getValue() != 15:
        adcClkMul = 20.0
    else:
        adcClkMul = 21.0
    conv_time = ((2 * prescaler) * adcClkMul * 1000000.0 * multiplier) / clock
    adcSym_CONV_TIME.setLabel("**** Conversion Time is "+str(conv_time)+" us ****")

def adcUserSeqVisible(adcSym_SEQR1_USCHLocal, event):
    for channelID in range(0, Database.getSymbolValue(adcInstanceName.getValue().lower(), "ADC_CHANNEL_SEQ_NUM")):
        adcSym_SEQR1_USCH[channelID].setVisible(event["value"])

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
    adcSym_CH_NegativeInput[channelID].setVisible(event["value"])

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
    if(event["id"].find("_NEG_INP") > 0):
        if(event["value"] == "AN"+str(channelID)):
            adcCHMenu[channelID].setVisible(False)
        else:
            adcCHMenu[channelID].setVisible(True)

def adcTriggerVisible(symbol, event):
    symObj = event["symbol"]
    if(symObj.getSelectedKey() == "EXT_TRIG_RISE" or
       symObj.getSelectedKey() == "EXT_TRIG_FALL" or
       symObj.getSelectedKey() == "EXT_TRIG_ANY" or
       symObj.getSelectedKey() == "HW_TRIGGER"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcTriggerTimeVisible(symbol, event):
    if(event["id"] == "ADC_TRGR_MODE" and event["value"] == 4):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcCalcTriggerPeriod(symbol, event):
    trgper = int((adcSym_TRIGGER_TIME.getValue() * adcSym_Clock.getValue() / 1000.0) - 1) #Trigger time is in millisecond
    if(event["id"] == "ADC_TRIGGER_TIME" or (event["id"] == "ADC_TRGR_MODE" and event["value"] == 4)):
        symbol.setValue(trgper, 2)
    else:
        symbol.clearValue()

def adcSymbolVisible(symbol, event):
    symbol.setVisible(event["value"])

###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(adcComponent):
    global adcInstanceName
    global interruptSymbolEnable
    global adcClockSourceInvalidSym

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())

    Log.writeInfoMessage("Running " + adcInstanceName.getValue())
    interruptLastNameEnable = "_INTERRUPT_ENABLE"
    interruptSymbolEnable = adcInstanceName.getValue() + interruptLastNameEnable

    #------------------------- ATDF Read -------------------------------------
    availablePins = []      # array to save available pins
    channel = [] #array to save available channels
    adcChannelsValues = [] #array used for combo symbol
    adcChannelsValues.append("NONE")

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + Database.getSymbolValue("core", "COMPONENT_PACKAGE") + "\"]")
    children = val.getChildren()
    for pad in range(0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    adc_signals = []
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName.getValue()+"\"]/signals")
    adc_signals = adc.getChildren()
    for pad in range(0, len(adc_signals)):
        group = adc_signals[pad].getAttribute("group")
        if (("AD" in group) and ("index" in adc_signals[pad].getAttributeList())):
            channel.append("False")
            padSignal = adc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(adc_signals[pad].getAttribute("index"))] = "True"
                adcChannelsValues.append("CH"+adc_signals[pad].getAttribute("index"))

    adcMenu = adcComponent.createMenuSymbol("ADC_MENU", None)
    adcMenu.setLabel("ADC Configuration")

    #max no of channels
    adcSym_NUM_CHANNELS = adcComponent.createIntegerSymbol("ADC_NUM_CHANNELS", adcMenu)
    adcSym_NUM_CHANNELS.setDefaultValue(len(channel))
    adcSym_NUM_CHANNELS.setVisible(False)

    # Provide a source clock selection symbol for masks that supports it
    valueGroupPath = "/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_EMR__SRCCLK\"]"
    valueGroup = ATDF.getNode(valueGroupPath)
    if valueGroup is not None:
        adcSym_EMR_SRCCLK = adcComponent.createKeyValueSetSymbol("ADC_CLK_SRC", adcMenu)
        adcSym_EMR_SRCCLK.setLabel(valueGroup.getAttribute("caption"))
        values = valueGroup.getChildren()
        for index in range(len(values)):
            adcSym_EMR_SRCCLK.addKey(values[index].getAttribute("name"),
                                    values[index].getAttribute("value"),
                                    values[index].getAttribute("caption"))
            adcSym_EMR_SRCCLK.setOutputMode("Key")
            adcSym_EMR_SRCCLK.setDisplayMode("Key")

    adcClockSourceInvalidSym = adcComponent.createCommentSymbol("ADC_CLK_SRC_INVALID_COMMENT", adcMenu)
    adcClockSourceInvalidSym.setLabel("Warning!!! " + adcInstanceName.getValue() + " clock frequency is zero")
    adcClockSourceInvalidSym.setVisible(False)

    #Clock prescaler
    global adcSym_MR_PRESCAL
    adcSym_MR_PRESCAL = adcComponent.createIntegerSymbol("ADC_MR_PRESCAL", adcMenu)
    adcSym_MR_PRESCAL.setLabel("Select Prescaler")
    adcSym_MR_PRESCAL.setDefaultValue(9)
    adcSym_MR_PRESCAL.setMin(0)
    adcSym_MR_PRESCAL.setMax(255)

    #clock selection
    global adcSym_Clock
    adcSym_Clock = adcComponent.createIntegerSymbol("ADC_CLK", adcMenu)
    adcSym_Clock.setLabel("Clock Frequency (Hz)")
    defaultAdcFreq = int(adcGetPeripheralClock() / (2 * (adcSym_MR_PRESCAL.getValue() + 1)))
    adcSym_Clock.setDefaultValue(defaultAdcFreq)
    adcSym_Clock.setVisible(True)
    adcSym_Clock.setReadOnly(True)
    adcSym_Clock.setDependencies(adcFreqCalc, ["ADC_MR_PRESCAL", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Startup time
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_MR__STARTUP\"]")
    if valueGroup is not None:
        adcSym_MR_STARTUP_TIME_VALUE = adcComponent.createKeyValueSetSymbol("ADC_MR_STARTUP_VALUE", adcMenu)
        adcSym_MR_STARTUP_TIME_VALUE.setLabel("Startup Time")
        adcSym_MR_STARTUP_TIME_VALUE.setDefaultValue(8)
        adcSym_MR_STARTUP_TIME_VALUE.setOutputMode("Key")
        adcSym_MR_STARTUP_TIME_VALUE.setDisplayMode("Description")
        startupTimeValues = valueGroup.getChildren()
        for index in range(len(startupTimeValues)):
            adcSym_MR_STARTUP_TIME_VALUE.addKey(startupTimeValues[index].getAttribute("name"), startupTimeValues[index].getAttribute("value"), startupTimeValues[index].getAttribute("caption"))

    #Tracking time
    global adcSym_MR_TRACKING_TIME_VALUE
    adcSym_MR_TRACKING_TIME_VALUE = adcComponent.createIntegerSymbol("ADC_MR_TRACKTIM_VALUE", adcMenu)
    adcSym_MR_TRACKING_TIME_VALUE.setLabel("Tracking Time")
    adcSym_MR_TRACKING_TIME_VALUE.setDefaultValue(15)
    adcSym_MR_TRACKING_TIME_VALUE.setMin(0)
    adcSym_MR_TRACKING_TIME_VALUE.setMax(15)

    adcSym_PRESCAL_WARNING = adcComponent.createCommentSymbol("ADC_PRESCAL_WARNING", adcMenu)
    adcSym_PRESCAL_WARNING.setLabel("**** ADC Frequency = " + str(defaultAdcFreq) + " Hz. ****")
    adcSym_PRESCAL_WARNING.setVisible(False)
    adcSym_PRESCAL_WARNING.setDependencies(adcPrescalWarning, ["ADC_MR_PRESCAL", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Result resolution
    #Added keys here as combining two bit-fields EMR_ASTE and EMR_OSR
    global adcSym_EMR_OSR_VALUE
    adcSym_EMR_OSR_VALUE = adcComponent.createKeyValueSetSymbol("ADC_EMR_OSR_VALUE", adcMenu)
    adcSym_EMR_OSR_VALUE.setLabel("Result Resolution")
    adcSym_EMR_OSR_VALUE.setDefaultValue(0)
    adcSym_EMR_OSR_VALUE.setOutputMode("Value")
    adcSym_EMR_OSR_VALUE.setDisplayMode("Description")
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_EMR__OSR\"]")
    if valueGroup is not None:
        osrValues = valueGroup.getChildren()
        for index in range(len(osrValues)):
            if osrValues[index].getAttribute("name") == "NO_AVERAGE":
                adcSym_EMR_OSR_VALUE.addKey("NO_AVERAGE", "0", "12-bit")
            elif osrValues[index].getAttribute("name") == "OSR4":
                adcSym_EMR_OSR_VALUE.addKey("OSR4_SIN", "1", "13-bit - single trigger averaging")
                adcSym_EMR_OSR_VALUE.addKey("OSR4_MUL", "2", "13-bit - multi trigger averaging")
            elif osrValues[index].getAttribute("name") == "OSR16":
                adcSym_EMR_OSR_VALUE.addKey("OSR16_SIN", "3", "14-bit - single trigger averaging")
                adcSym_EMR_OSR_VALUE.addKey("OSR16_MUL", "4", "14-bit - multi trigger averaging")
            elif osrValues[index].getAttribute("name") == "OSR64":
                adcSym_EMR_OSR_VALUE.addKey("OSR64_SIN", "5", "15-bit - single trigger averaging")
                adcSym_EMR_OSR_VALUE.addKey("OSR64_MUL", "6", "15-bit - multi trigger averaging")
            elif osrValues[index].getAttribute("name") == "OSR256":
                adcSym_EMR_OSR_VALUE.addKey("OSR256_SIN", "7", "16-bit - single trigger averaging")
                adcSym_EMR_OSR_VALUE.addKey("OSR256_MUL", "8", "16-bit - multi trigger averaging")

    #Conversion time
    adcSym_CONV_TIME = adcComponent.createCommentSymbol("ADC_CONV_TIME", adcMenu)
    adcSym_CONV_TIME.setLabel("**** Conversion Time is 0 us ****")
    adcSym_CONV_TIME.setDependencies(adcCalcConversionTime, ["ADC_MR_PRESCAL", "ADC_EMR_OSR_VALUE", "ADC_MR_TRACKTIM_VALUE", "core." + adcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Result sign
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_EMR__SIGNMODE\"]")
    if valueGroup is not None:
        adcSym_EMR_SIGNMODE_VALUE = adcComponent.createKeyValueSetSymbol("ADC_EMR_SIGNMODE_VALUE", adcMenu)
        adcSym_EMR_SIGNMODE_VALUE.setLabel("Result Sign")
        adcSym_EMR_SIGNMODE_VALUE.setDefaultValue(0)
        adcSym_EMR_SIGNMODE_VALUE.setOutputMode("Key")
        adcSym_EMR_SIGNMODE_VALUE.setDisplayMode("Description")
        signmodeValues = valueGroup.getChildren()
        for index in range(len(signmodeValues)):
            adcSym_EMR_SIGNMODE_VALUE.addKey(signmodeValues[index].getAttribute("name"), signmodeValues[index].getAttribute("value"), signmodeValues[index].getAttribute("caption"))

    #Trigger Mode
    adcSym_TRGR_MODE = adcComponent.createKeyValueSetSymbol("ADC_TRGR_MODE", adcMenu)
    adcSym_TRGR_MODE.setLabel("Trigger Mode")
    adcSym_TRGR_MODE.setOutputMode("Key")
    adcSym_TRGR_MODE.setDisplayMode("Description")
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_TRGR__TRGMOD\"]")
    if valueGroup is not None:
        trgmodeValues = valueGroup.getChildren()
        for index in range(len(trgmodeValues)):
            if trgmodeValues[index].getAttribute("name") != "PEN_TRIG": #Touchscreen mode is not supported
                adcSym_TRGR_MODE.addKey(trgmodeValues[index].getAttribute("name"), trgmodeValues[index].getAttribute("value"), trgmodeValues[index].getAttribute("caption"))
        adcSym_TRGR_MODE.setDefaultValue(5)
    else:
        adcSym_TRGR_MODE.addKey("FREERUN", "0", "Free Run")
        adcSym_TRGR_MODE.addKey("SW_TRIGGER", "1", "Software Trigger")
        adcSym_TRGR_MODE.addKey("HW_TRIGGER", "2", "Hardware Trigger")
        adcSym_TRGR_MODE.setDefaultValue(0)

    #External Trigger Mode
    adcSym_MR_TRGSEL_VALUE = adcComponent.createKeyValueSetSymbol("ADC_MR_TRGSEL_VALUE", adcSym_TRGR_MODE)
    adcSym_MR_TRGSEL_VALUE.setLabel("Select External Trigger Input")
    adcSym_MR_TRGSEL_VALUE.setVisible(False)
    adcSym_MR_TRGSEL_VALUE.setDefaultValue(1)
    adcSym_MR_TRGSEL_VALUE.setOutputMode("Key")
    adcSym_MR_TRGSEL_VALUE.setDisplayMode("Description")
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_MR__TRGSEL\"]")
    if valueGroup is not None:
        trgselValues = valueGroup.getChildren()
        for index in range(len(trgselValues)):
            adcSym_MR_TRGSEL_VALUE.addKey(trgselValues[index].getAttribute("name"), trgselValues[index].getAttribute("value"), trgselValues[index].getAttribute("caption"))
    adcSym_MR_TRGSEL_VALUE.setDependencies(adcTriggerVisible, ["ADC_TRGR_MODE"])

    trgmodevalueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_TRGR__TRGMOD\"]")
    if trgmodevalueGroup is not None:
        #ADC Internal Periodic Trigger
        global adcSym_TRIGGER_TIME
        adcSym_TRIGGER_TIME = adcComponent.createIntegerSymbol("ADC_TRIGGER_TIME", adcSym_TRGR_MODE)
        adcSym_TRIGGER_TIME.setLabel("Trigger Period (ms)")
        adcSym_TRIGGER_TIME.setDefaultValue(2)
        adcSym_TRIGGER_TIME.setMin(1)
        adcSym_TRIGGER_TIME.setMax(int((65536 * 1000.0)))
        adcSym_TRIGGER_TIME.setVisible(False)
        adcSym_TRIGGER_TIME.setDependencies(adcTriggerTimeVisible, ["ADC_TRGR_MODE"])

        adcSym_TRGR_TRGPER = adcComponent.createIntegerSymbol("ADC_TRGR_TRIGGER_PERIOD", adcSym_TRIGGER_TIME)
        adcSym_TRGR_TRGPER.setVisible(False)
        adcSym_TRGR_TRGPER.setDependencies(adcCalcTriggerPeriod, ["ADC_TRIGGER_TIME", "ADC_TRGR_MODE"])

    #Sleep Mode
    adcSym_MR_SLEEP = adcComponent.createBooleanSymbol("ADC_MR_SLEEP", adcMenu)
    adcSym_MR_SLEEP.setLabel("Sleep Mode")
    adcSym_MR_SLEEP.setDefaultValue(False)

    adcFastWakeupValues = ["OFF", "ON"]
    adcSym_MR_FWUP = adcComponent.createComboSymbol("ADC_MR_FWUP", adcSym_MR_SLEEP, adcFastWakeupValues)
    adcSym_MR_FWUP.setLabel("Fast Wakeup")
    adcSym_MR_FWUP.setDefaultValue(adcFastWakeupValues[0])
    adcSym_MR_FWUP.setVisible(False)
    adcSym_MR_FWUP.setDependencies(adcSymbolVisible, ["ADC_MR_SLEEP"])

    #Automatic Window Comparison
    adcSym_COMP_WINDOW = adcComponent.createBooleanSymbol("ADC_COMP_WINDOW", adcMenu)
    adcSym_COMP_WINDOW.setLabel("Automatic Window Comparison")
    adcSym_COMP_WINDOW.setDefaultValue(False)

    adcSym_EMR_CMPMODE = adcComponent.createKeyValueSetSymbol("ADC_EMR_CMPMODE", adcSym_COMP_WINDOW)
    adcSym_EMR_CMPMODE.setLabel("Comparison Mode")
    adcSym_EMR_CMPMODE.setDefaultValue(0)
    adcSym_EMR_CMPMODE.setOutputMode("Key")
    adcSym_EMR_CMPMODE.setDisplayMode("Description")
    adcSym_EMR_CMPMODE.addKey("CMPMODE_LOW", "0", "Vin < VLo")
    adcSym_EMR_CMPMODE.addKey("CMPMODE_HIGH", "1", "Vin < VHi")
    adcSym_EMR_CMPMODE.addKey("CMPMODE_IN", "2", "VLo < Vin < VHi")
    adcSym_EMR_CMPMODE.addKey("CMPMODE_OUT", "3", "VHi < Vin < VLo")
    adcSym_EMR_CMPMODE.setVisible(False)
    adcSym_EMR_CMPMODE.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])

    adcSym_EMR_CMPTYPE = adcComponent.createKeyValueSetSymbol("ADC_EMR_CMPTYPE", adcSym_COMP_WINDOW)
    adcSym_EMR_CMPTYPE.setLabel("Comparison Type")
    adcSym_EMR_CMPTYPE.setDefaultValue(0)
    adcSym_EMR_CMPTYPE.setOutputMode("Key")
    adcSym_EMR_CMPTYPE.setDisplayMode("Description")
    adcSym_EMR_CMPTYPE.addKey("CMPTYPE_FLAG_ONLY", "0", "0-No Comparison")
    adcSym_EMR_CMPTYPE.addKey("CMPTYPE_START_CONDITION", "1", "1-Comparison match")
    adcSym_EMR_CMPTYPE.setVisible(False)
    adcSym_EMR_CMPTYPE.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])

    adcCompSelectedChannelValues = adcChannelsValues[1:]
    adcCompSelectedChannelValues.append("All");
    adcSym_EMR_CMPSEL = adcComponent.createComboSymbol("ADC_EMR_CMPSEL", adcSym_COMP_WINDOW, adcCompSelectedChannelValues)
    adcSym_EMR_CMPSEL.setLabel("Comparison Selected Channel")
    adcSym_EMR_CMPSEL.setDefaultValue(adcCompSelectedChannelValues[0])
    adcSym_EMR_CMPSEL.setVisible(False)
    adcSym_EMR_CMPSEL.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])

    adcSym_CWR_LOWTHRES = adcComponent.createIntegerSymbol("ADC_CWR_LOWTHRES_VALUE", adcSym_COMP_WINDOW)
    adcSym_CWR_LOWTHRES.setLabel("Low Threshold")
    adcSym_CWR_LOWTHRES.setDefaultValue(0)
    adcSym_CWR_LOWTHRES.setVisible(False)
    adcSym_CWR_LOWTHRES.setMin(0)
    maxThreshold = int(ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group@[name=\"ADC\"]/register@[name=\"ADC_CWR\"]/bitfield@[name=\"LOWTHRES\"]").getAttribute("mask"), 16)
    adcSym_CWR_LOWTHRES.setMax(maxThreshold)
    adcSym_CWR_LOWTHRES.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])

    adcSym_CWR_HIGHTHRES = adcComponent.createIntegerSymbol("ADC_CWR_HIGHTHRES_VALUE", adcSym_COMP_WINDOW)
    adcSym_CWR_HIGHTHRES.setLabel("High Threshold")
    adcSym_CWR_HIGHTHRES.setDefaultValue(0)
    adcSym_CWR_HIGHTHRES.setVisible(False)
    adcSym_CWR_HIGHTHRES.setMin(0)
    adcSym_CWR_HIGHTHRES.setMax(maxThreshold)
    adcSym_CWR_HIGHTHRES.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])

    global adcSym_IER_COMPE
    adcSym_IER_COMPE = adcComponent.createBooleanSymbol("ADC_IER_COMPE", adcSym_COMP_WINDOW)
    adcSym_IER_COMPE.setLabel("Comparison Event Interrupt")
    adcSym_IER_COMPE.setDefaultValue(False)
    adcSym_IER_COMPE.setVisible(False)
    adcSym_IER_COMPE.setDependencies(adcSymbolVisible, ["ADC_COMP_WINDOW"])
    #------------------------------------------------------------------------------------
    #user sequence menu
    adcUserSeq = adcComponent.createMenuSymbol("ADC_USER_SEQ", None)
    adcUserSeq.setLabel("User Channel Sequence Configuration")

    adcSym_ChannelSeqNum = adcComponent.createIntegerSymbol("ADC_CHANNEL_SEQ_NUM", adcUserSeq)
    adcSym_ChannelSeqNum.setLabel("Total number of User Channel Sequence")
    adcSym_ChannelSeqNum.setDefaultValue(len(ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group@[name=\"ADC\"]/register@[name=\"ADC_SEQR2\"]").getChildren()) + 8)
    adcSym_ChannelSeqNum.setVisible(False)

    #user sequence comment
    adcSym_USEQ_COMMENT = adcComponent.createCommentSymbol("ADC_USEQ_COMMENT", adcUserSeq)
    adcSym_USEQ_COMMENT.setLabel("**** Configure selected channels in the Channel Configuration Menu ****")

    #enable user sequence
    adcSym_MR_USEQ = adcComponent.createBooleanSymbol("ADC_MR_USEQ", adcUserSeq)
    adcSym_MR_USEQ.setLabel("Enable User Sequence Mode")
    adcSym_MR_USEQ.setDefaultValue(False)

    for channelID in range(0, adcSym_ChannelSeqNum.getValue()):
        #channel selection for user sequence
        adcSym_SEQR1_USCH.append(channelID)
        adcSym_SEQR1_USCH[channelID] = adcComponent.createComboSymbol("ADC_SEQR1_USCH" + str(channelID + 1), adcSym_MR_USEQ, adcChannelsValues)
        adcSym_SEQR1_USCH[channelID].setLabel("Select Channel for Sequence Number " + str(channelID + 1))
        adcSym_SEQR1_USCH[channelID].setDefaultValue(adcChannelsValues[0])
        adcSym_SEQR1_USCH[channelID].setVisible(False)
        adcSym_SEQR1_USCH[channelID].setDependencies(adcUserSeqVisible, ["ADC_MR_USEQ"])
    #--------------------------------------------------------------------------------------

    adcCHConfMenu = adcComponent.createMenuSymbol("ADC_CH_CONF", None)
    adcCHConfMenu.setLabel("Channel Configuration")

    # Loop runs for ADC channels and visibility of the channel is controlled as per available pins
    for channelID in range(0, len(channel)):
        #Channel menu
        global adcCHMenu
        adcCHMenu.append(channelID)
        adcCHMenu[channelID] = adcComponent.createMenuSymbol("CH"+str(channelID), adcCHConfMenu)
        adcCHMenu[channelID].setLabel("Channel "+str(channelID))
        #Show channels as per available pins in package
        if (channel[channelID] == "False"):
            adcCHMenu[channelID].setVisible(False)

        #Channel enable
        adcSym_CH_CHER.append(channelID)
        adcSym_CH_CHER[channelID] = adcComponent.createBooleanSymbol("ADC_"+str(channelID)+"_CHER", adcCHMenu[channelID])
        adcSym_CH_CHER[channelID].setLabel("Enable Channel " + str(channelID))
        adcSym_CH_CHER[channelID].setDefaultValue(False)
        #enable corresponding channel pair for diff mode, e.g. CH0 and CH1
        if (channelID % 2 == 1):
            adcSym_CH_CHER[channelID].setDependencies(adcCHEnable, ["ADC_"+str(channelID-1)+"_NEG_INP"])

        #Channel name
        adcSym_CH_NAME.append(channelID)
        adcSym_CH_NAME[channelID] = adcComponent.createStringSymbol("ADC_"+str(channelID)+"_NAME", adcSym_CH_CHER[channelID])
        adcSym_CH_NAME[channelID].setLabel("Name")
        adcSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
        adcSym_CH_NAME[channelID].setVisible(False)
        adcSym_CH_NAME[channelID].setDependencies(adcCHNameVisible, ["ADC_"+str(channelID)+"_CHER"])

        #Channel positive input
        adcSym_CH_PositiveInput.append(channelID)
        adcSym_CH_PositiveInput[channelID] = adcComponent.createStringSymbol("ADC_"+str(channelID)+"_POS_INP", adcSym_CH_CHER[channelID])
        adcSym_CH_PositiveInput[channelID].setLabel("Positive Input")
        adcSym_CH_PositiveInput[channelID].setDefaultValue("AN"+str(channelID))
        adcSym_CH_PositiveInput[channelID].setReadOnly(True)
        adcSym_CH_PositiveInput[channelID].setVisible(False)
        adcSym_CH_PositiveInput[channelID].setDependencies(adcCHPosInpVisible, ["ADC_"+str(channelID)+"_CHER"])

        #Channel negative input
        adcSym_CH_NegativeInput.append(channelID)
        adc_EvenChNegInput = ["GND", "AN"+str(channelID+1)]
        adc_OddChNegInput = ["GND"]
        if (channelID % 2 == 1):
            adcSym_CH_NegativeInput[channelID] = adcComponent.createComboSymbol("ADC_"+str(channelID)+"_NEG_INP", adcSym_CH_CHER[channelID], adc_OddChNegInput)
            adcSym_CH_NegativeInput[channelID].setReadOnly(True)
        else:
            adcSym_CH_NegativeInput[channelID] = adcComponent.createComboSymbol("ADC_"+str(channelID)+"_NEG_INP", adcSym_CH_CHER[channelID], adc_EvenChNegInput)
            if (channel[channelID + 1] == "False"):
                adcSym_CH_NegativeInput[channelID].setReadOnly(True)
        adcSym_CH_NegativeInput[channelID].setLabel("Negative Input")
        adcSym_CH_NegativeInput[channelID].setDefaultValue("GND")
        adcSym_CH_NegativeInput[channelID].setVisible(False)
        adcSym_CH_NegativeInput[channelID].setDependencies(adcCHNegInpVisible, ["ADC_"+str(channelID)+"_CHER"])

        #Channel Gain
        channelGainValueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CGR__GAIN" + str(channelID) + "\"]")
        if channelGainValueGroup is not None:
            adcSym_CGR_Gain.append(channelID)
            adcSym_CGR_Gain[channelID] = adcComponent.createKeyValueSetSymbol("ADC_" + str(channelID) + "_CGR_GAIN", adcSym_CH_CHER[channelID])
            adcSym_CGR_Gain[channelID].setLabel("Gain")
            adcSym_CGR_Gain[channelID].setOutputMode("Key")
            adcSym_CGR_Gain[channelID].setDisplayMode("Description")
            adcSym_CGR_Gain[channelID].setVisible(False)
            cgrGainValues = channelGainValueGroup.getChildren()
            for index in range(len(cgrGainValues)):
                adcSym_CGR_Gain[channelID].addKey(cgrGainValues[index].getAttribute("name"), cgrGainValues[index].getAttribute("value"), cgrGainValues[index].getAttribute("caption"))
            adcSym_CGR_Gain[channelID].setDependencies(adcSymbolVisible, ["ADC_" + str(channelID) + "_CHER"])

        #Channel Offset
        channelOffsetReg = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group@[name=\"ADC\"]/register@[name=\"ADC_COR\"]/bitfield@[name=\"OFFSET" + str(channelID) + "\"]")
        if channelOffsetReg is not None:
            adcSym_COR_Offset.append(channelID)
            adcSym_COR_Offset[channelID] = adcComponent.createBooleanSymbol("ADC_" + str(channelID) + "_COR_OFFSET", adcSym_CH_CHER[channelID])
            adcSym_COR_Offset[channelID].setLabel("Offset")
            adcSym_COR_Offset[channelID].setDescription("Centers the analog signal on VADVREF/2 before the gain scaling. The offset applied is (G-1)VADVREF/2 where G is the gain applied.")
            adcSym_COR_Offset[channelID].setVisible(False)
            adcSym_COR_Offset[channelID].setDependencies(adcSymbolVisible, ["ADC_" + str(channelID) + "_CHER"])

        #Channel interrupt
        adcSym_CH_IER_EOC.append(channelID)
        adcSym_CH_IER_EOC[channelID] = adcComponent.createBooleanSymbol("ADC_"+str(channelID)+"_IER_EOC", adcSym_CH_CHER[channelID])
        adcSym_CH_IER_EOC[channelID].setLabel("End of conversion interrupt")
        adcSym_CH_IER_EOC[channelID].setDefaultValue(False)
        adcSym_CH_IER_EOC[channelID].setVisible(False)
        adcSym_CH_IER_EOC[channelID].setDependencies(adcCHInterruptVisible, ["ADC_"+str(channelID)+"_CHER"])

    # Clock dynamic settings
    adcSym_ClockControl = adcComponent.createBooleanSymbol("ADC_CLOCK_ENABLE", None)
    adcSym_ClockControl.setDependencies(adcClockControl, [str("ADC_" + str(channelID) + "_CHER") for channelID in range(adcSym_NUM_CHANNELS.getValue())])
    adcSym_ClockControl.setVisible(False)

    adcInterruptList = [str("ADC_" + str(channelID) + "_IER_EOC") for channelID in range(adcSym_NUM_CHANNELS.getValue())]
    adcInterruptList.append("ADC_IER_COMPE")

    # Interrupt Dynamic settings
    adcSym_InterruptControl = adcComponent.createBooleanSymbol("ADC_INTERRUPT_ENABLE", None)
    adcSym_InterruptControl.setDependencies(adcInterruptEnableDisableCallback, adcInterruptList)
    adcSym_InterruptControl.setVisible(False)

    adcClkEnCommentList = [str("ADC_" + str(channelID) + "_CHER") for channelID in range(adcSym_NUM_CHANNELS.getValue())]
    adcClkEnCommentList.append("core." + adcInstanceName.getValue() + "_CLOCK_ENABLE")

    # Dependency Status
    adcSym_ClkEnComment = adcComponent.createCommentSymbol("ADC_CLK_ENABLE_COMMENT", None)
    adcSym_ClkEnComment.setVisible(False)
    adcSym_ClkEnComment.setLabel("Warning!!! " + adcInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    adcSym_ClkEnComment.setDependencies(dependencyClockStatus, adcClkEnCommentList)

    adcInterruptEnCommentList = adcInterruptList
    adcInterruptEnCommentList.append("core." + interruptSymbolEnable)

    adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_INTERRUPT_ENABLE_COMMENT", None)
    adcSym_IntEnComment.setVisible(False)
    adcSym_IntEnComment.setLabel("Warning!!! " + adcInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    adcSym_IntEnComment.setDependencies(dependencyIntStatus, adcInterruptEnCommentList)

    #--------------------------------------------------------------------------------------
    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    adc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]")
    adcID = adc.getAttribute("id")

    adcHeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcHeaderFile.setSourcePath("../peripheral/adc_" + str(adcID) + "/templates/plib_adc.h.ftl")
    adcHeaderFile.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".h")
    adcHeaderFile.setDestPath("peripheral/adc/")
    adcHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcHeaderFile.setType("HEADER")
    adcHeaderFile.setMarkup(True)

    adcCommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcCommonHeaderFile.setSourcePath("../peripheral/adc_" + str(adcID) + "/templates/plib_adc_common.h.ftl")
    adcCommonHeaderFile.setOutputName("plib_adc_common.h")
    adcCommonHeaderFile.setDestPath("peripheral/adc/")
    adcCommonHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcCommonHeaderFile.setType("HEADER")
    adcCommonHeaderFile.setMarkup(True)

    adcSource1File = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSource1File.setSourcePath("../peripheral/adc_" + str(adcID) + "/templates/plib_adc.c.ftl")
    adcSource1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".c")
    adcSource1File.setDestPath("peripheral/adc/")
    adcSource1File.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcSource1File.setType("SOURCE")
    adcSource1File.setMarkup(True)

    adcSystemInitFile = adcComponent.createFileSymbol("ADC_INIT", None)
    adcSystemInitFile.setType("STRING")
    adcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSystemInitFile.setSourcePath("../peripheral/adc_"+str(adcID)+"/templates/system/initialization.c.ftl")
    adcSystemInitFile.setMarkup(True)

    adcSystemDefFile = adcComponent.createFileSymbol("ADC_DEF", None)
    adcSystemDefFile.setType("STRING")
    adcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSystemDefFile.setSourcePath("../peripheral/adc_"+str(adcID)+"/templates/system/definitions.h.ftl")
    adcSystemDefFile.setMarkup(True)
