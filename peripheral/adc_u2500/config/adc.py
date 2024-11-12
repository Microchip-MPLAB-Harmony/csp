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
import math
global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock = []
global InterruptVectorUpdate
InterruptVectorUpdate = []
global adcInstanceName
adcSym_SEQCTRL_SEQ = []

global adcResult
adcResult = {"13 Bit": 
                {"SAMPLENUM": 2,
                 "ADJRES": 1
                },
            "14 Bit": 
                {"SAMPLENUM": 4,
                 "ADJRES": 2
                },
            "15 Bit": 
                {"SAMPLENUM": 6,
                 "ADJRES": 1
                },
            "16 Bit": 
                {"SAMPLENUM": 8,
                 "ADJRES": 0
                },
            }
###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateADCInterruptStatus(symbol, event):
    if (event["id"] == "ADC_INTENSET_WINMON"):
        Database.setSymbolValue("core", InterruptVector[0], event["value"], 2)
        Database.setSymbolValue("core", InterruptHandlerLock[0], event["value"], 2)
        if event["value"] == True:
            Database.setSymbolValue("core", InterruptHandler[0], adcInstanceName.getValue() + "_OTHER_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptHandler[0], adcInstanceName.getValue() + "_Handler", 2)
    elif (event["id"] == "ADC_INTENSET_RESRDY"):
        Database.setSymbolValue("core", InterruptVector[1], event["value"], 2)
        Database.setSymbolValue("core", InterruptHandlerLock[1], event["value"], 2)
        if event["value"] == True:
            Database.setSymbolValue("core", InterruptHandler[1], adcInstanceName.getValue() + "_RESRDY_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptHandler[1], adcInstanceName.getValue() + "_Handler", 2)

def updateADCInterruptWarningStatus(symbol, event):
    symVisible = False
    if adcSym_INTENSET_WINMON.getValue() == True:
        if (Database.getSymbolValue("core", InterruptVectorUpdate[0].split("core.")[1]) == True):
            symVisible = True
    if adcSym_INTENSET_RESRDY.getValue() == True:
        if (Database.getSymbolValue("core", InterruptVectorUpdate[1].split("core.")[1]) == True):
            symVisible = True
    if symVisible == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateADCClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcCalcSampleTime(symbol, event):
    clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    if (adcSym_CTRLA_SLAVEEN.getValue() == False):
        prescaler = adcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    else:
        component = int(adcInstanceName.getValue()[-1]) - 1
        prescaler = (Database.getSymbolValue("adc" + str(component), "ADC_CTRLA_PRESCALER"))
        prescaler = math.pow(2, prescaler+1)
    sample_cycles = adcSym_SAMPCTRL_SAMPLEN.getValue()
    if (sample_cycles == 1):
        offset_comp = 3
    else:
        offset_comp = 0    
    data_width = adcSym_CTRLC_RESSEL.getSelectedKey()[:-3]
    conv_time = float((int(sample_cycles) + int(data_width) + offset_comp) * int(prescaler) * 1000000.0) / clock_freq
    symbol.setLabel("**** Conversion Time is " + str(conv_time) + " uS ****")

def adcEvesysConfigure(symbol, event):
    if(event["id"] == "ADC_EVCTRL_RESRDYEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(adcInstanceName.getValue())+"_RESRDY_ACTIVE", event["value"], 2)

    if(event["id"] == "ADC_WINDOW_OUTPUT_EVENT"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(adcInstanceName.getValue())+"_WINMON_ACTIVE", event["value"], 2)

    if (adcSym_CONV_TRIGGER.getValue() == "HW Event Trigger"):
        if (event["id"] == "ADC_EVCTRL_FLUSH"):
            if (event["value"] > 0):
                Database.setSymbolValue("evsys", "USER_"+str(adcInstanceName.getValue())+"_SYNC_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(adcInstanceName.getValue())+"_SYNC_READY", False, 2)
        if (event["id"] == "ADC_EVCTRL_START"):
            if (event["value"] > 0):
                Database.setSymbolValue("evsys", "USER_"+str(adcInstanceName.getValue())+"_START_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(adcInstanceName.getValue())+"_START_READY", False, 2)

def adcNegativeInput(symbol, event):
    if (event["value"] == True):
        symbol.setReadOnly(False)
    else:
        symbol.setReadOnly(True)

def adcResultBitVisibility(symbol, event):
    symObj = event["symbol"]
    if(symObj.getSelectedKey() == "16BIT"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcResultConfVisibility(symbol, event):
    component = symbol.getComponent()
    resolution = component.getSymbolValue("ADC_CTRLB_RESSEL")
    bit = component.getSymbolValue("ADC_RES_BIT")
    if (resolution == 1 and bit == "Accumulation/Averaging"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcADJRESCalc(symbol, event):
    component = symbol.getComponent()
    resolution = component.getSymbolValue("ADC_CTRLB_RESSEL")
    bit = component.getSymbolValue("ADC_RES_BIT")
    shift = component.getSymbolValue("ADC_AVGCTRL_ADJRES")
    if resolution == 1 and bit != "Accumulation/Averaging":
        symbol.setValue(adcResult[bit]["ADJRES"])
    else:
        symbol.setValue(shift)   

def adcSAMPLENUMCalc(symbol, event):
    component = symbol.getComponent()
    resolution = component.getSymbolValue("ADC_CTRLB_RESSEL")
    bit = component.getSymbolValue("ADC_RES_BIT")
    samples = component.getSymbolValue("ADC_AVGCTRL_SAMPLENUM")
    if resolution == 1 and bit != "Accumulation/Averaging":
        symbol.setValue(adcResult[bit]["SAMPLENUM"])
    else:
        symbol.setValue(samples)     

def adcSlaveModeVisibility(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def adcEventInputVisibility(symbol, event):
    if (adcSym_CTRLA_SLAVEEN.getValue() == True or adcSym_CONV_TRIGGER.getValue() != "HW Event Trigger"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def adcOptionVisible(symbol, event):
    symbol.setVisible(event["value"])

def adcDmaVisible(symbol, event):
    if(event["value"] == True):
        for index in range(0, len(adcSequenceInputValues)):
            adcSym_SEQCTRL_SEQ[index].setVisible(True)
    else:
        for index in range(0, len(adcSequenceInputValues)):
            adcSym_SEQCTRL_SEQ[index].setVisible(False)

    if(adcSym_CONV_TRIGGER.getValue() != "Free Run"):
        adcSym_SEQCTRL_SEQ[9].setVisible(False)


def adcWindowVisible(symbol, event):
    if (event["value"] > 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcSUPCVisible(symbol, event):
    symbol.setLabel("*********** Enable Vref output in SUPC ***********")
    if (event["id"] == "ADC_INPUTCTRL_MUXPOS"):
        symObj = event["symbol"]
        if (symObj.getSelectedKey() == "BANDGAP"):
            symbol.setVisible(True)
        elif (symObj.getSelectedKey() == "PTAT" or symObj.getSelectedKey() == "CTAT"):
            symbol.setLabel("**** Enable Temperature Sensor and Sensor Channel in SUPC ****")
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

    if (event["id"] == "ADC_REFCTRL_REFSEL"):
        symObj = event["symbol"]
        if (symObj.getSelectedKey() == "INTREF"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

###################################################################################################
########################### Dependency   #################################
###################################################################################################
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
    resetChannelsForPMSMFOC()

# Disable ADC channels and interrupt
def resetChannelsForPMSMFOC():
    component = str(adcInstanceName.getValue()).lower()
    instanceNum = int(filter(str.isdigit,str(adcInstanceName.getValue())))
    #Database.setSymbolValue(component, "ADC_INPUTCTRL_MUXPOS", "0")
    Database.setSymbolValue(component, "ADC_CONV_TRIGGER", "Free Run")
    Database.setSymbolValue(component, "ADC_INTENSET_RESRDY", False)
    #Disable slave for ADC1
    if instanceNum == 1 :
       Database.setSymbolValue(component, "ADC_CTRLA_SLAVEEN", False)

def find_prescale_and_conv_samples(desired_conversion_time_us, resolution, input_clock):
    desired_conversion_frequency = 1e6 / desired_conversion_time_us
    best_error = float('inf')
    best_prescaler = 0
    best_sample_count = 0

    for prescaler in range(7, 0, -1):  # Decreasing order of prescaler values
        prev_error = float('inf')

        for sample_count in range(1, 33):
            actual_conversion_frequency = input_clock / ((2 ** (1 + prescaler)) * (sample_count + resolution))
            error = abs(desired_conversion_frequency - actual_conversion_frequency)
            print(error)

            if error > prev_error:
                break

            if error == 0:
                return prescaler, sample_count

            if error < best_error:
                best_error = error
                best_prescaler = prescaler
                best_sample_count = sample_count

            prev_error = error

    return best_prescaler, best_sample_count

def setAdcConfigParams( args ):
    """The ADC PLIB has following configuration data
                "id" : Unique identifier
                "instance" : Instance of ADC to be configured
                "channel"  : Channel of ADC to be set
                "resolution" : ADC resolution
                "mode": Conversion mode
                "reference": ADC PLIB reference signals
                "conversion_time" : Conversion time in microsecond
                "trigger" : Trigger source
                "result_alignment" : Left or right aligned results
                "enable_eoc_event" : Enable end of conversion event
                "enable_eoc_interrupt" : Enable end of conversion flag
                "enable_slave_mode" : Enable slave mode
                "enable_dma_sequence" : Enable DMA sequencing
    """

    component = args["instance"].lower()
    channel = int(filter(str.isdigit, str(args["channel"])))

    if args["enable"] == True:
        # Calculate prescaler and ADC sample counts based on requested conversion time
        if not(args["conversion_time"] == "default"):
            # Get input clock frequency
            input_clock = Database.getSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_FREQUENCY")

            resolution = int(args["resolution"])

            # Limit the resolution to 12 bits
            if (resolution > 12 ):
                resolution = 12

            prescale, sample_count = find_prescale_and_conv_samples(args["conversion_time"], int(args["resolution"]), input_clock)

            # Set prescaler and sample count values
            adcSym_CTRLB_PRESCALER.setValue(prescale)
            adcSym_SAMPCTRL_SAMPLEN.setValue(sample_count)

        # Calculate prescaler and ADC sample counts based on requested conversion time
        if not(args["reference"] == "default"):
            # ToDO: Placeholder. To be done later
            pass

        # Find the key index of the RESOLUTION
        count = adcSym_CTRLC_RESSEL.getKeyCount()
        resIndex = 0
        for i in range(0, count):
            if ( args["resolution"] in adcSym_CTRLC_RESSEL.getKeyDescription(i) ):
                resIndex = i
                break

        # Enable/ Disable slave for ADC module other than ADC0
        Database.setSymbolValue(component, "ADC_CTRLA_SLAVEEN", args["enable_slave_mode"])

        # Enable channel
        Database.setSymbolValue(component, "ADC_INPUTCTRL_MUXPOS", int(channel))

        # Enable/ Disable end-of-conversion interrupt
        Database.setSymbolValue(component, "ADC_INTENSET_RESRDY", args["enable_eoc_interrupt"])

        # Enable/ Disable end-of-conversion event
        Database.setSymbolValue(component, "ADC_EVCTRL_RESRDYEO", args["enable_eoc_event"])

        # Enable DMA sequencing
        if not args["enable_dma_sequence"] == "default":
            # ToDO: Placeholder for later development
            pass

        if not args["result_alignment"] == "default":
            # ToDO: Placeholder for later development
            pass

        if args["trigger"] != "SOFTWARE_TRIGGER":
            Database.setSymbolValue(component, "ADC_CONV_TRIGGER", "HW Event Trigger")

        Database.setSymbolValue(component, "ADC_EVCTRL_START", 1)
        Database.setSymbolValue(component, "ADC_CTRLB_RESSEL", resIndex)

    else:
        # Enable/ Disable end-of-conversion interrupt
        Database.setSymbolValue(component, "ADC_INTENSET_RESRDY", False)

        # Enable/ Disable end-of-conversion event
        Database.setSymbolValue(component, "ADC_EVCTRL_RESRDYEO", False)

def handleMessage(messageID, args):
    dict = {}
    # print("ADC handleMessage: {} args: {}".format(messageID, args))
    
    if (messageID == "PMSM_FOC_ADC_CH_CONF"):
        component = str(adcInstanceName.getValue()).lower()
        instanceNum = int(filter(str.isdigit,str(adcInstanceName.getValue())))
        dict['ADC_MAX_CH'] = Database.getSymbolValue(component, "ADC_MAX_CHANNELS")
        dict['ADC_MAX_MODULES'] = Database.getSymbolValue(component, "ADC_NUM_MODULES")
        #Change ADC channels if they are changed in the PMSM_FOC
        resetChannelsForPMSMFOC()
        AdcConfigForPMSMFOC(component, instanceNum, args)

    elif ( messageID == "SET_ADC_CONFIG_PARAMS"):
        # Set ADC configuration parameters
        setAdcConfigParams( args )
        
    elif (messageID == "ADC_CONFIG_HW_IO"):
        component = str(adcInstanceName.getValue()).lower()
        channel, muxInput, enable = args['config']

        adcInputCtrlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__{}\"]".format(muxInput))
        adcInputValues = adcInputCtrlNode.getChildren()

        dict = {"Result": "AIN{} is not a permitted value for ADC_INPUTCTRL_{} - adcInputValues: {}".format(channel, muxInput, adcInputValues)}
        
        for adcInputValue in adcInputValues:
            if adcInputValue.getAttribute("name") == "AIN{}".format(channel):
                if enable == False:
                    res = Database.clearSymbolValue(component, "ADC_INPUTCTRL_{}".format(muxInput))
                else:
                    # print("ADC handleMessage setSymbolValue: {} = {}".format("ADC_INPUTCTRL_{}".format(muxInput), int(channel)))
                    res = Database.setSymbolValue(component, "ADC_INPUTCTRL_{}".format(muxInput), int(channel))
                    
                if res == True:
                    dict = {"Result": "Success"}
                else:
                    dict = {"Result": "DB Error in setting ADC_INPUTCTRL_{} value".format(muxInput)}

    return dict

# ADC configurations needed for PMSM_FOC component
def AdcConfigForPMSMFOC(component, instanceNum, args):
    phUModule = args['PHASE_U']
    phUCh = args['PHASE_U_CH']
    phVModule = args['PHASE_V']
    phVCh = args['PHASE_V_CH']
    phDCBusModule = args['VDC']
    phDCBusCh = args['VDC_CH']
    phPotModule = args['POT']
    phPotCh = args['POT_CH']
    resolution = args['RESOLUTION']
    trigger = args['TRIGGER']

    #fine the key index of the RESOLUTION
    count = adcSym_CTRLC_RESSEL.getKeyCount()
    resIndex = 0
    for i in range(0,count):
        if (str(resolution) in adcSym_CTRLC_RESSEL.getKeyDescription(i) ):
            resIndex = i
            break

    #Enable slave for ADC1
    if instanceNum == 1 :
       Database.setSymbolValue(component, "ADC_CTRLA_SLAVEEN", True)

    # Enable ADC modules, Ph U interrupt
    if (int(phUModule) == instanceNum):
        Database.setSymbolValue(component, "ADC_INPUTCTRL_MUXPOS", int(phUCh))
        Database.setSymbolValue(component, "ADC_INTENSET_RESRDY", True)
        Database.setSymbolValue(component, "ADC_CH_PHASE_U", "ADC_POSINPUT_AIN"+str(phUCh))
    if (int(phVModule) == instanceNum):
        Database.setSymbolValue(component, "ADC_INPUTCTRL_MUXPOS", int(phVCh))
        Database.setSymbolValue(component, "ADC_CH_PHASE_V", "ADC_POSINPUT_AIN"+str(phUCh))
    if (int(phPotModule) == instanceNum):
        Database.setSymbolValue(component, "ADC_CH_POT", "ADC_POSINPUT_AIN"+str(phPotCh))
    if (int(phDCBusModule) == instanceNum):
            Database.setSymbolValue(component, "ADC_CH_VDC_BUS", "ADC_POSINPUT_AIN"+str(phDCBusCh))

    if (instanceNum == 0):
        Database.setSymbolValue(component, "ADC_CONV_TRIGGER", "HW Event Trigger") #HW trigger
        Database.setSymbolValue(component, "ADC_EVCTRL_START", 1) #input start event
    Database.setSymbolValue(component, "ADC_CTRLB_RESSEL", resIndex) #resolution

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(adcComponent):
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global adcInstanceName
    global InterruptVectorUpdate

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    Log.writeInfoMessage("Running " + adcInstanceName.getValue())

    #clock enable
    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = []

    pinout = ""
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

    adc_signals = []
    maxChannels = 0
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName.getValue()+"\"]/signals")
    adc_signals = adc.getChildren()
    for pad in range(0, len(adc_signals)):
        group = adc_signals[pad].getAttribute("group")
        if (("AIN" in group) and ("index" in adc_signals[pad].getAttributeList())):
            maxChannels = maxChannels + 1
            padSignal = adc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel.append(adc_signals[pad].getAttribute("group")+adc_signals[pad].getAttribute("index"))

    #number of ADC channels
    adcSym_MAX_CHANNELS = adcComponent.createIntegerSymbol("ADC_MAX_CHANNELS", None)
    adcSym_MAX_CHANNELS.setVisible(False)
    adcSym_MAX_CHANNELS.setDefaultValue(maxChannels)

    #number of ADC modules
    adcSym_NUM_MODULES = adcComponent.createIntegerSymbol("ADC_NUM_MODULES", None)
    adcSym_NUM_MODULES.setVisible(False)
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]")
    adcSym_NUM_MODULES.setDefaultValue(len(adc.getChildren()))

    #----------------- motor control APIs ---------------------------------
    adcConvAPI = adcComponent.createStringSymbol("ADC_START_CONV_API", None)
    adcConvAPI.setVisible(False)
    adcConvAPI.setValue(adcInstanceName.getValue()+"_ConversionStart")

    adcResultAPI = adcComponent.createStringSymbol("ADC_GET_RESULT_API", None)
    adcResultAPI.setVisible(False)
    adcResultAPI.setValue(adcInstanceName.getValue()+"_ConversionResultGet")

    adcResultReadyAPI = adcComponent.createStringSymbol("ADC_IS_RESULT_READY_API", None)
    adcResultReadyAPI.setVisible(False)
    adcResultReadyAPI.setValue(adcInstanceName.getValue()+"_ConversionStatusGet")

    adcCallbackAPI = adcComponent.createStringSymbol("ADC_CALLBACK_API", None)
    adcCallbackAPI.setVisible(False)
    adcCallbackAPI.setValue(adcInstanceName.getValue()+"_CallbackRegister")

    adcStartAPI = adcComponent.createStringSymbol("ADC_START_API", None)
    adcStartAPI.setVisible(False)
    adcStartAPI.setValue(adcInstanceName.getValue()+"_Enable")

    adcStopAPI = adcComponent.createStringSymbol("ADC_STOP_API", None)
    adcStopAPI.setVisible(False)
    adcStopAPI.setValue(adcInstanceName.getValue()+"_Disable")

    adcChannelSelectAPI = adcComponent.createStringSymbol("ADC_CHANNEL_SELECT_API", None)
    adcChannelSelectAPI.setVisible(False)
    adcChannelSelectAPI.setValue(adcInstanceName.getValue() + "_ChannelSelect")

    adcIntDisableAPI = adcComponent.createStringSymbol("ADC_INT_DISABLE_API", None)
    adcIntDisableAPI.setVisible(False)
    adcIntDisableAPI.setValue(adcInstanceName.getValue() + "_InterruptsDisable")

    adcIntEnableAPI = adcComponent.createStringSymbol("ADC_INT_ENABLE_API", None)
    adcIntEnableAPI.setVisible(False)
    adcIntEnableAPI.setValue(adcInstanceName.getValue() + "_InterruptsEnable")

    adcIntClearAPI = adcComponent.createStringSymbol("ADC_INT_CLEAR_API", None)
    adcIntClearAPI.setVisible(False)
    adcIntClearAPI.setValue(adcInstanceName.getValue() + "_InterruptsClear")

    adcPhUCh = adcComponent.createStringSymbol("ADC_CH_PHASE_U", None)
    adcPhUCh.setVisible(False)
    adcPhUCh.setValue("ADC_POSINPUT_AIN0")

    adcPhVCh = adcComponent.createStringSymbol("ADC_CH_PHASE_V", None)
    adcPhVCh.setVisible(False)
    adcPhVCh.setValue("ADC_POSINPUT_AIN0")

    adcVdcCh = adcComponent.createStringSymbol("ADC_CH_VDC_BUS", None)
    adcVdcCh.setVisible(False)
    adcVdcCh.setValue("ADC_POSINPUT_AIN0")

    adcPotCh = adcComponent.createStringSymbol("ADC_CH_POT", None)
    adcPotCh.setVisible(False)
    adcPotCh.setValue("ADC_POSINPUT_AIN0")

    adcGND = adcComponent.createStringSymbol("ADC_GND", None)
    adcGND.setVisible(False)
    adcGND.setValue("ADC_NEGINPUT_GND")

    adcResultInt = adcComponent.createStringSymbol("INTERRUPT_ADC_RESULT", None)
    adcResultInt.setVisible(False)
    adcResultInt.setValue(adcInstanceName.getValue()+"_RESRDY_IRQn")

    #slave mode
    global adcSym_CTRLA_SLAVEEN
    adcSym_CTRLA_SLAVEEN = adcComponent.createBooleanSymbol("ADC_CTRLA_SLAVEEN", None)
    adcSym_CTRLA_SLAVEEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLA")
    adcSym_CTRLA_SLAVEEN.setLabel("Enable Slave")
    adcSym_CTRLA_SLAVEEN.setDefaultValue(False)
    mode = "0"
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName.getValue()+"\"]/parameters")
    param_values = []
    param_values = node.getChildren()
    for index in range(0, len(param_values)):
        if "MASTER_SLAVE_MODE" in param_values[index].getAttribute("name"):
            mode = param_values[index].getAttribute("value")
        if (mode == "2"):
            adcSym_CTRLA_SLAVEEN.setVisible(True)
        else:
            adcSym_CTRLA_SLAVEEN.setVisible(False)

    #prescaler configuration
    global adcSym_CTRLB_PRESCALER
    adcSym_CTRLB_PRESCALER = adcComponent.createKeyValueSetSymbol("ADC_CTRLA_PRESCALER", None)
    adcSym_CTRLB_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLA")
    adcSym_CTRLB_PRESCALER.setLabel("Select Prescaler")
    adcSym_CTRLB_PRESCALER.setDefaultValue(2)
    adcSym_CTRLB_PRESCALER.setOutputMode("Key")
    adcSym_CTRLB_PRESCALER.setDisplayMode("Description")
    adcPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLA__PRESCALER\"]")
    adcPrescalerValues = []
    adcPrescalerValues = adcPrescalerNode.getChildren()
    for index in range(0, len(adcPrescalerValues)):
        adcSym_CTRLB_PRESCALER.addKey(adcPrescalerValues[index].getAttribute("name"), adcPrescalerValues[index].getAttribute("value"), adcPrescalerValues[index].getAttribute("caption"))
    adcSym_CTRLB_PRESCALER.setDependencies(adcSlaveModeVisibility, ["ADC_CTRLA_SLAVEEN"])

    #sampling time
    global adcSym_SAMPCTRL_SAMPLEN
    adcSym_SAMPCTRL_SAMPLEN = adcComponent.createIntegerSymbol("ADC_SAMPCTRL_SAMPLEN", None)
    adcSym_SAMPCTRL_SAMPLEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:SAMPCTRL")
    adcSym_SAMPCTRL_SAMPLEN.setLabel("Select Sample Length (cycles)")
    adcSym_SAMPCTRL_SAMPLEN.setMin(1)
    adcSym_SAMPCTRL_SAMPLEN.setMax(64)
    adcSym_SAMPCTRL_SAMPLEN.setDefaultValue(4)

    clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = adcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    sample_cycles = adcSym_SAMPCTRL_SAMPLEN.getValue()
    data_width = 12
    conv_time = float((int(sample_cycles) + int(data_width)) * int(prescaler) * 1000000.0) / clock_freq

    if adcInstanceName.getValue()[-1].isdigit():
        component = int(adcInstanceName.getValue()[-1]) - 1
    else:
        component = ""

    #Sampling time calculation
    adcSym_SAMPCTRL_SAMPLEN_TIME = adcComponent.createCommentSymbol("ADC_SAMPCTRL_SAMPLEN_TIME", None)
    adcSym_SAMPCTRL_SAMPLEN_TIME.setLabel("**** Conversion Time is " + str(conv_time) + " us ****")
    # Dependency registration is done after all dependencies are defined.

    #reference selection
    adcSym_REFCTRL_REFSEL = adcComponent.createKeyValueSetSymbol("ADC_REFCTRL_REFSEL", None)
    adcSym_REFCTRL_REFSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:REFCTRL")
    adcSym_REFCTRL_REFSEL.setLabel("Select Reference")
    default = 0
    adcSym_REFCTRL_REFSEL.setOutputMode("Key")
    adcSym_REFCTRL_REFSEL.setDisplayMode("Description")
    adcReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_REFCTRL__REFSEL\"]")
    adcReferenceValues = []
    adcReferenceValues = adcReferenceNode.getChildren()
    for index in range(0, len(adcReferenceValues)):
        if adcReferenceValues[index].getAttribute("caption") == "VDDANA":
            default = index
        if "ADC1" in adcReferenceValues[index].getAttribute("caption") and adcInstanceName.getValue() == "ADC0":
            continue
        adcSym_REFCTRL_REFSEL.addKey(adcReferenceValues[index].getAttribute("name"), adcReferenceValues[index].getAttribute("value"),
        adcReferenceValues[index].getAttribute("caption"))
    adcSym_REFCTRL_REFSEL.setDefaultValue(default)

    #trigger
    global adcSym_CONV_TRIGGER
    adcSym_CONV_TRIGGER = adcComponent.createComboSymbol("ADC_CONV_TRIGGER", None, ["Free Run", "SW Trigger", "HW Event Trigger"])
    adcSym_CONV_TRIGGER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:EVCTRL")
    adcSym_CONV_TRIGGER.setDefaultValue("Free Run")
    adcSym_CONV_TRIGGER.setLabel("Select Conversion Trigger")
    adcSym_CONV_TRIGGER.setDependencies(adcSlaveModeVisibility, ["ADC_CTRLA_SLAVEEN"])

    adcSym_FLUSH_EVENT = adcComponent.createKeyValueSetSymbol("ADC_EVCTRL_FLUSH", adcSym_CONV_TRIGGER)
    adcSym_FLUSH_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:EVCTRL")
    adcSym_FLUSH_EVENT.setLabel("Flush Event Input")
    adcSym_FLUSH_EVENT.setVisible(False)
    adcSym_FLUSH_EVENT.setOutputMode("Value")
    adcSym_FLUSH_EVENT.setDisplayMode("Description")
    adcSym_FLUSH_EVENT.addKey("DISABLED", "0", "Disabled")
    adcSym_FLUSH_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    adcSym_FLUSH_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    adcSym_FLUSH_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    adcSym_START_EVENT = adcComponent.createKeyValueSetSymbol("ADC_EVCTRL_START", adcSym_CONV_TRIGGER)
    adcSym_START_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:EVCTRL")
    adcSym_START_EVENT.setLabel("Start Event Input")
    adcSym_START_EVENT.setVisible(False)
    adcSym_START_EVENT.setOutputMode("Value")
    adcSym_START_EVENT.setDisplayMode("Description")
    adcSym_START_EVENT.addKey("DISABLED", "0", "Disabled")
    adcSym_START_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    adcSym_START_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    adcSym_START_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    global adcSym_SEQ_ENABLE
    adcSym_SEQ_ENABLE = adcComponent.createBooleanSymbol("ADC_SEQ_ENABLE", None)
    adcSym_SEQ_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:DSEQCTRL")
    adcSym_SEQ_ENABLE.setLabel("Enable DMA Sequencing")
    adcSym_SEQ_ENABLE.setDependencies(adcDmaVisible, ["ADC_SEQ_ENABLE"])

    global adcSequenceInputValues
    adcSequenceInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/register-group@[name=\"ADC\"]/register@[name=\"DSEQCTRL\"]")
    adcSequenceInputValues = []
    adcSequenceInputValues = adcSequenceInputNode.getChildren()
    for index in range(0, len(adcSequenceInputValues)):
        adcSym_SEQCTRL_SEQ.append(index)
        adcSym_SEQCTRL_SEQ[index] = adcComponent.createBooleanSymbol("ADC_SEQCTRL_SEQ"+str(index), adcSym_SEQ_ENABLE)
        adcSym_SEQCTRL_SEQ[index].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:DSEQCTRL")
        adcSym_SEQCTRL_SEQ[index].setLabel("Enable "+ str(adcSequenceInputValues[index].getAttribute("caption")))
        adcSym_SEQCTRL_SEQ[index].setDependencies(adcOptionVisible, ["ADC_SEQ_ENABLE"])
        adcSym_SEQCTRL_SEQ[index].setVisible(False)
        if(adcSym_CONV_TRIGGER.getValue() == "Free Run" and adcSequenceInputValues[index].getAttribute("name") == "AUTOSTART" and adcSym_SEQ_ENABLE.getValue() == True):
            adcSym_SEQCTRL_SEQ[index].setValue(True , 2)

    adcPositiveInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXPOS\"]")
    adcPositiveInputValues = []
    adcPositiveInputValues = adcPositiveInputNode.getChildren()

    #Used in DMA sequencing
    adcSym_NUM_CHANNELS = adcComponent.createIntegerSymbol("ADC_NUM_CHANNELS", None)
    adcSym_NUM_CHANNELS.setVisible(False)
    adcSym_NUM_CHANNELS.setDefaultValue(len(adcSequenceInputValues))

    adcChannelMenu = adcComponent.createMenuSymbol("ADC_CHANNEL_MENU", None)
    adcChannelMenu.setLabel("Channel Configuration")

    #positive input
    adcSym_INPUTCTRL_MUXPOS = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXPOS", adcChannelMenu)
    adcSym_INPUTCTRL_MUXPOS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:INPUTCTRL")
    adcSym_INPUTCTRL_MUXPOS.setLabel("Select Positive Input")
    adcSym_INPUTCTRL_MUXPOS.setDefaultValue(0)
    adcSym_INPUTCTRL_MUXPOS.setOutputMode("Key")
    adcSym_INPUTCTRL_MUXPOS.setDisplayMode("Description")
    posInput = 0
    for index in range(0, len(adcPositiveInputValues)):
        if "AIN" in adcPositiveInputValues[index].getAttribute("name"):
            if adcPositiveInputValues[index].getAttribute("name") in channel:
                adcSym_MUXPOS_ENUM = adcComponent.createStringSymbol("ADC_MUXPOS_ENUM"+str(posInput), None)
                adcSym_MUXPOS_ENUM.setDefaultValue(adcPositiveInputValues[index].getAttribute("name"))
                adcSym_MUXPOS_ENUM.setVisible(False)
                posInput = posInput + 1
                adcSym_INPUTCTRL_MUXPOS.addKey(adcPositiveInputValues[index].getAttribute("name"), adcPositiveInputValues[index].getAttribute("value"),
                adcPositiveInputValues[index].getAttribute("caption"))
        else:
            adcSym_MUXPOS_ENUM = adcComponent.createStringSymbol("ADC_MUXPOS_ENUM"+str(posInput), None)
            adcSym_MUXPOS_ENUM.setDefaultValue(adcPositiveInputValues[index].getAttribute("name"))
            adcSym_MUXPOS_ENUM.setVisible(False)
            posInput = posInput + 1
            if "ADC0" in adcPositiveInputValues[index].getAttribute("caption") and adcInstanceName.getValue() == "ADC1":
                continue
            adcSym_INPUTCTRL_MUXPOS.addKey(adcPositiveInputValues[index].getAttribute("name"), adcPositiveInputValues[index].getAttribute("value"),
            adcPositiveInputValues[index].getAttribute("caption"))

    #negative input
    adcSym_INPUTCTRL_MUXNEG = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXNEG", adcChannelMenu)
    adcSym_INPUTCTRL_MUXNEG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:INPUTCTRL")
    adcSym_INPUTCTRL_MUXNEG.setLabel("Select Negative Input")
    adcSym_INPUTCTRL_MUXNEG.setOutputMode("Key")
    adcSym_INPUTCTRL_MUXNEG.setDisplayMode("Description")
    defaultIndex = 0
    gndIndex = 0
    posInput = 0
    adcNagativeInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXNEG\"]")
    adcNagativeInputValues = []
    adcNagativeInputValues = adcNagativeInputNode.getChildren()
    for index in range(0, len(adcNagativeInputValues)):
        if adcNagativeInputValues[index].getAttribute("name") == "GND":
            defaultIndex = gndIndex
        if "AIN" in adcNagativeInputValues[index].getAttribute("name"):
            if adcNagativeInputValues[index].getAttribute("name") in channel:
                adcSym_MUXNEG_ENUM = adcComponent.createStringSymbol("ADC_MUXNEG_ENUM"+str(posInput), None)
                adcSym_MUXNEG_ENUM.setDefaultValue(adcNagativeInputValues[index].getAttribute("name"))
                adcSym_MUXNEG_ENUM.setVisible(False)
                posInput = posInput + 1
                adcSym_INPUTCTRL_MUXNEG.addKey(adcNagativeInputValues[index].getAttribute("name"), adcNagativeInputValues[index].getAttribute("value"),
                adcNagativeInputValues[index].getAttribute("caption"))
                gndIndex += 1
        else:
            adcSym_MUXNEG_ENUM = adcComponent.createStringSymbol("ADC_MUXNEG_ENUM"+str(posInput), None)
            adcSym_MUXNEG_ENUM.setDefaultValue(adcNagativeInputValues[index].getAttribute("name"))
            adcSym_MUXNEG_ENUM.setVisible(False)
            posInput = posInput + 1
            adcSym_INPUTCTRL_MUXNEG.addKey(adcNagativeInputValues[index].getAttribute("name"), adcNagativeInputValues[index].getAttribute("value"),
            adcNagativeInputValues[index].getAttribute("caption"))
            gndIndex += 1
    adcSym_INPUTCTRL_MUXNEG.setDefaultValue(defaultIndex)

    adcResultMenu = adcComponent.createMenuSymbol("ADC_RESULT_MENU", None)
    adcResultMenu.setLabel("Result Configuration")

    #resolution configuration
    global adcSym_CTRLC_RESSEL
    adcSym_CTRLC_RESSEL = adcComponent.createKeyValueSetSymbol("ADC_CTRLB_RESSEL", adcResultMenu)
    adcSym_CTRLC_RESSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLB")
    adcSym_CTRLC_RESSEL.setLabel("Select Result Resolution")
    adcSym_CTRLC_RESSEL.setDefaultValue(0)
    adcSym_CTRLC_RESSEL.setOutputMode("Key")
    adcSym_CTRLC_RESSEL.setDisplayMode("Description")
    adcResultResolutionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLB__RESSEL\"]")
    adcResultResolutionValues = []
    adcResultResolutionValues = adcResultResolutionNode.getChildren()
    for index in range (0 , len(adcResultResolutionValues)):
        adcSym_CTRLC_RESSEL.addKey(adcResultResolutionValues[index].getAttribute("name"), adcResultResolutionValues[index].getAttribute("value"),
        adcResultResolutionValues[index].getAttribute("caption"))

    adcBits = ["13 Bit", "14 Bit", "15 Bit", "16 Bit", "Accumulation/Averaging"]
    adcSym_RES_BIT = adcComponent.createComboSymbol("ADC_RES_BIT", adcSym_CTRLC_RESSEL, adcBits)
    adcSym_RES_BIT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLB")
    adcSym_RES_BIT.setLabel("Number of Bits")
    adcSym_RES_BIT.setVisible(False)
    adcSym_RES_BIT.setDependencies(adcResultBitVisibility, ["ADC_CTRLB_RESSEL"])        

    #Averaging
    adcSym_AVGCTRL_SAMPLENUM = adcComponent.createKeyValueSetSymbol("ADC_AVGCTRL_SAMPLENUM", adcSym_RES_BIT)
    adcSym_AVGCTRL_SAMPLENUM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:AVGCTRL")
    adcSym_AVGCTRL_SAMPLENUM.setLabel("Number of Accumulated Samples")
    adcSym_AVGCTRL_SAMPLENUM.setDefaultValue(0)
    adcSym_AVGCTRL_SAMPLENUM.setOutputMode("Key")
    adcSym_AVGCTRL_SAMPLENUM.setDisplayMode("Description")
    adcSym_AVGCTRL_SAMPLENUM.setVisible(False)
    adcResultResolutionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_AVGCTRL__SAMPLENUM\"]")
    adcResultResolutionValues = []
    adcResultResolutionValues = adcResultResolutionNode.getChildren()
    for index in range (0 , len(adcResultResolutionValues)):
        adcSym_AVGCTRL_SAMPLENUM.addKey(adcResultResolutionValues[index].getAttribute("name"), adcResultResolutionValues[index].getAttribute("value"),
        adcResultResolutionValues[index].getAttribute("caption"))
    adcSym_AVGCTRL_SAMPLENUM.setDependencies(adcResultConfVisibility, ["ADC_CTRLB_RESSEL", "ADC_RES_BIT"])

    #division coefficient
    adcSym_AVGCTRL_ADJRES = adcComponent.createIntegerSymbol("ADC_AVGCTRL_ADJRES", adcSym_RES_BIT)
    adcSym_AVGCTRL_ADJRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:AVGCTRL")
    adcSym_AVGCTRL_ADJRES.setLabel("Number of Right Shifts")
    adcSym_AVGCTRL_ADJRES.setMin(0)
    adcSym_AVGCTRL_ADJRES.setMax(7)
    adcSym_AVGCTRL_ADJRES.setDefaultValue(0)
    adcSym_AVGCTRL_ADJRES.setVisible(False)
    adcSym_AVGCTRL_ADJRES.setDependencies(adcResultConfVisibility, ["ADC_CTRLB_RESSEL", "ADC_RES_BIT"])

    adcSym_ADJRES = adcComponent.createIntegerSymbol("ADC_ADJRES", adcSym_RES_BIT)
    adcSym_ADJRES.setVisible(False)
    adcSym_ADJRES.setDependencies(adcADJRESCalc, ["ADC_CTRLB_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_ADJRES"])

    adcSym_SAMPLENUM = adcComponent.createIntegerSymbol("ADC_SAMPLENUM", adcSym_RES_BIT)
    adcSym_SAMPLENUM.setVisible(False)
    adcSym_SAMPLENUM.setDependencies(adcSAMPLENUMCalc, ["ADC_CTRLB_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_SAMPLENUM"])

    #left adjusted mode
    adcSym_CTRLC_LEFTADJ = adcComponent.createBooleanSymbol("ADC_CTRLB_LEFTADJ", adcResultMenu)
    adcSym_CTRLC_LEFTADJ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLB")
    adcSym_CTRLC_LEFTADJ.setLabel("Left Aligned Result")
    adcSym_CTRLC_LEFTADJ.setVisible(True)

    #interrupt mode
    global adcSym_INTENSET_RESRDY
    adcSym_INTENSET_RESRDY = adcComponent.createBooleanSymbol("ADC_INTENSET_RESRDY", adcResultMenu)
    adcSym_INTENSET_RESRDY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:INTENSET")
    adcSym_INTENSET_RESRDY.setLabel("Enable Result Ready Interrupt")

    #event out mode
    adcSym_EVCTRL_RSERDYEO = adcComponent.createBooleanSymbol("ADC_EVCTRL_RESRDYEO", adcResultMenu)
    adcSym_EVCTRL_RSERDYEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:EVCTRL")
    adcSym_EVCTRL_RSERDYEO.setLabel("Enable Result Ready Event Out")

    adcWindowMenu = adcComponent.createMenuSymbol("ADC_WINDOW_CONFIG_MENU", None)
    adcWindowMenu.setLabel("Window Mode Configuration")

    #Configure mode for Window operation
    adcSym_CTRLC_WINMODE = adcComponent.createKeyValueSetSymbol("ADC_CTRLB_WINMODE", adcWindowMenu)
    adcSym_CTRLC_WINMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLB")
    adcSym_CTRLC_WINMODE.setLabel("Select Window Monitor Mode")
    adcSym_CTRLC_WINMODE.setDefaultValue(0)
    adcSym_CTRLC_WINMODE.setOutputMode("Value")
    adcSym_CTRLC_WINMODE.setDisplayMode("Description")
    adcWindowConfigNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLB__WINMODE\"]")
    adcWindowConfigValues = []
    adcWindowConfigValues = adcWindowConfigNode.getChildren()
    for index in range (0 , len(adcWindowConfigValues)):
        adcSym_CTRLC_WINMODE.addKey(adcWindowConfigValues[index].getAttribute("name"), adcWindowConfigValues[index].getAttribute("value"),
        adcWindowConfigValues[index].getAttribute("caption"))

    #Window upper threshold
    adcSym_WINUT = adcComponent.createIntegerSymbol("ADC_WINUT", adcWindowMenu)
    adcSym_WINUT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:WINUT")
    adcSym_WINUT.setLabel("Window Upper Threshold")
    adcSym_WINUT.setMin(-32768)
    adcSym_WINUT.setMax(32767)
    adcSym_WINUT.setDefaultValue(1024)
    adcSym_WINUT.setVisible(False)
    adcSym_WINUT.setDependencies(adcWindowVisible, ["ADC_CTRLB_WINMODE"])

    #Window lower threshold
    adcSym_WINLT = adcComponent.createIntegerSymbol("ADC_WINLT", adcWindowMenu)
    adcSym_WINLT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:WINLT")
    adcSym_WINLT.setLabel("Window Lower Threshold")
    adcSym_WINLT.setMin(-32768)
    adcSym_WINLT.setMax(32767)
    adcSym_WINLT.setDefaultValue(512)
    adcSym_WINLT.setVisible(False)
    adcSym_WINLT.setDependencies(adcWindowVisible, ["ADC_CTRLB_WINMODE"])

    global adcSym_INTENSET_WINMON
    adcSym_INTENSET_WINMON = adcComponent.createBooleanSymbol("ADC_INTENSET_WINMON", adcWindowMenu)
    adcSym_INTENSET_WINMON.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:INTENSET")
    adcSym_INTENSET_WINMON.setLabel("Enable Window Monitor Interrupt")
    adcSym_INTENSET_WINMON.setDefaultValue(False)
    adcSym_INTENSET_WINMON.setVisible(False)
    adcSym_INTENSET_WINMON.setDependencies(adcWindowVisible, ["ADC_CTRLB_WINMODE"])

    #Enable Window Monitor Event Out
    adcSym_HW_INP_EVENT = adcComponent.createBooleanSymbol("ADC_WINDOW_OUTPUT_EVENT", adcWindowMenu)
    adcSym_HW_INP_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:EVCTRL")
    adcSym_HW_INP_EVENT.setLabel("Enable Window Monitor Event Out")
    adcSym_HW_INP_EVENT.setVisible(False)
    adcSym_HW_INP_EVENT.setDependencies(adcWindowVisible, ["ADC_CTRLB_WINMODE"])

    adcSym_SAMPCTRL_SAMPLEN_TIME.setDependencies(adcCalcSampleTime, ["core."+adcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "adc"+str(component)+".ADC_CTRLA_PRESCALER", "ADC_SAMPCTRL_SAMPLEN", "ADC_CTRLA_PRESCALER", "ADC_CTRLB_RESSEL", "ADC_CTRLA_SLAVEEN"])

    adcSleepMenu = adcComponent.createMenuSymbol("ADC_SLEEP_MENU", None)
    adcSleepMenu.setLabel("Sleep Mode Configuration")

    #run in standby mode
    adcSym_CTRLA_RUNSTDBY = adcComponent.createBooleanSymbol("ADC_CTRLA_RUNSTDBY", adcSleepMenu)
    adcSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLA")
    adcSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")
    adcSym_CTRLA_RUNSTDBY.setVisible(True)

    #run in on demand control mode
    adcSym_CTRLA_ONDEMAND = adcComponent.createBooleanSymbol("ADC_CTRLA_ONDEMAND", adcSleepMenu)
    adcSym_CTRLA_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2500;register:CTRLA")
    adcSym_CTRLA_ONDEMAND.setLabel("On Demand Control")
    adcSym_CTRLA_ONDEMAND.setVisible(True)

    adcSym_EVESYS_CONFIGURE = adcComponent.createIntegerSymbol("ADC_EVESYS_CONFIGURE", None)
    adcSym_EVESYS_CONFIGURE.setVisible(False)
    adcSym_EVESYS_CONFIGURE.setDependencies(adcEvesysConfigure, \
        ["ADC_WINDOW_OUTPUT_EVENT", "ADC_EVCTRL_RESRDYEO", "ADC_CONV_TRIGGER", "ADC_EVCTRL_FLUSH", "ADC_EVCTRL_START"])

    adcSym_SUPC_COMMENT = adcComponent.createCommentSymbol("ADC_SUPC_COMMENT", None)
    adcSym_SUPC_COMMENT.setLabel("*********** Enable Vref output in SUPC ***********")
    adcSym_SUPC_COMMENT.setVisible(False)
    adcSym_SUPC_COMMENT.setDependencies(adcSUPCVisible, ["ADC_REFCTRL_REFSEL", "ADC_INPUTCTRL_MUXPOS"])
    ############################################################################
    #### Dependency ####
    ############################################################################
    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues = vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == adcInstanceName.getValue():
            name = vectorValues[id].getAttribute("name")
            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")

    adcSym_IntLines = adcComponent.createIntegerSymbol("ADC_NUM_INT_LINES", None)
    adcSym_IntLines.setVisible(False)
    adcSym_IntLines.setDefaultValue((len(InterruptVector) - 1))

    # Interrupt Dynamic settings
    adcSym_UpdateInterruptStatus = adcComponent.createBooleanSymbol("ADC_INTERRUPT_STATUS", None)
    adcSym_UpdateInterruptStatus.setDependencies(updateADCInterruptStatus, ["ADC_INTENSET_RESRDY", "ADC_INTENSET_WINMON"])
    adcSym_UpdateInterruptStatus.setVisible(False)

    InterruptVectorUpdate.append("ADC_INTENSET_RESRDY")
    InterruptVectorUpdate.append("ADC_INTENSET_WINMON")

    # Interrupt Warning status
    adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_INTERRUPT_ENABLE_COMMENT", None)
    adcSym_IntEnComment.setVisible(False)
    adcSym_IntEnComment.setLabel("Warning!!! "+adcInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    adcSym_IntEnComment.setDependencies(updateADCInterruptWarningStatus, InterruptVectorUpdate)

    # Clock Warning status
    adcSym_ClkEnComment = adcComponent.createCommentSymbol("ADC_CLOCK_ENABLE_COMMENT", None)
    adcSym_ClkEnComment.setVisible(False)
    adcSym_ClkEnComment.setLabel("Warning!!! " +adcInstanceName.getValue()+" Clock is Disabled in Clock Manager")
    adcSym_ClkEnComment.setDependencies(updateADCClockWarningStatus, ["core." + adcInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    adcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]")
    adcModuleID = adcModuleNode.getAttribute("id")

    adcSym_CommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcSym_CommonHeaderFile.setSourcePath("../peripheral/adc_u2500/templates/plib_adc_common.h.ftl")
    adcSym_CommonHeaderFile.setOutputName("plib_adc_common.h")
    adcSym_CommonHeaderFile.setDestPath("/peripheral/adc/")
    adcSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_CommonHeaderFile.setType("HEADER")
    adcSym_CommonHeaderFile.setMarkup(True)

    adcSym_HeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcSym_HeaderFile.setSourcePath("../peripheral/adc_u2500/templates/plib_adc.h.ftl")
    adcSym_HeaderFile.setOutputName("plib_"+adcInstanceName.getValue().lower()+".h")
    adcSym_HeaderFile.setDestPath("/peripheral/adc/")
    adcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_HeaderFile.setType("HEADER")
    adcSym_HeaderFile.setMarkup(True)

    adcSym_SourceFile = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSym_SourceFile.setSourcePath("../peripheral/adc_u2500/templates/plib_adc.c.ftl")
    adcSym_SourceFile.setOutputName("plib_"+adcInstanceName.getValue().lower()+".c")
    adcSym_SourceFile.setDestPath("/peripheral/adc/")
    adcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_SourceFile.setType("SOURCE")
    adcSym_SourceFile.setMarkup(True)

    adcSym_SystemInitFile = adcComponent.createFileSymbol("ADC_SYS_INIT", None)
    adcSym_SystemInitFile.setType("STRING")
    adcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSym_SystemInitFile.setSourcePath("../peripheral/adc_u2500/templates/system/initialization.c.ftl")
    adcSym_SystemInitFile.setMarkup(True)

    adcSym_SystemDefFile = adcComponent.createFileSymbol("ADC_SYS_DEF", None)
    adcSym_SystemDefFile.setType("STRING")
    adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSym_SystemDefFile.setSourcePath("../peripheral/adc_u2500/templates/system/definitions.h.ftl")
    adcSym_SystemDefFile.setMarkup(True)

    # load ADC manager
    adcComponent.addPlugin("../peripheral/adc_u2500/plugin/adc_u2500.jar")
