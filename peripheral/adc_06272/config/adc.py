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
global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global InterruptVectorUpdate
global adcInstanceName
global multiVectorSupport
multiVectorSupport = False
global ADCfilesArray
global InterruptVectorSecurity
ADCfilesArray = []

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

def fileUpdate(symbol, event):
    global ADCfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        ADCfilesArray[0].setSecurity("SECURE")
        ADCfilesArray[1].setSecurity("SECURE")
        ADCfilesArray[2].setSecurity("SECURE")
        ADCfilesArray[3].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        ADCfilesArray[4].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, False)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        ADCfilesArray[0].setSecurity("NON_SECURE")
        ADCfilesArray[1].setSecurity("NON_SECURE")
        ADCfilesArray[2].setSecurity("NON_SECURE")
        ADCfilesArray[3].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        ADCfilesArray[4].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, True)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, True)

def updateADCInterruptStatus(symbol, event):
    global multiVectorSupport
    if multiVectorSupport:
        if (event["id"] == "ADC_INTENSET_WCMP"):
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
        elif (event["id"] == "ADC_INTENSET_SAMPRDY"):
            Database.setSymbolValue("core", InterruptVector[2], event["value"], 2)
            Database.setSymbolValue("core", InterruptHandlerLock[2], event["value"], 2)
            if event["value"] == True:
                Database.setSymbolValue("core", InterruptHandler[2], adcInstanceName.getValue() + "_SAMPRDY_InterruptHandler", 2)
            else:
                Database.setSymbolValue("core", InterruptHandler[2], adcInstanceName.getValue() + "_Handler", 2)
        elif (event["id"] == "ADC_INTENSET_RESOVR"):
            Database.setSymbolValue("core", InterruptVector[3], event["value"], 2)
            Database.setSymbolValue("core", InterruptHandlerLock[3], event["value"], 2)
            if event["value"] == True:
                Database.setSymbolValue("core", InterruptHandler[3], adcInstanceName.getValue() + "_RRESOVR_InterruptHandler", 2)
            else:
                Database.setSymbolValue("core", InterruptHandler[4], adcInstanceName.getValue() + "_Handler", 2)    
        elif (event["id"] == "ADC_INTENSET_SAMPOVR"):
            Database.setSymbolValue("core", InterruptVector[4], event["value"], 2)
            Database.setSymbolValue("core", InterruptHandlerLock[4], event["value"], 2)
            if event["value"] == True:
                Database.setSymbolValue("core", InterruptHandler[4], adcInstanceName.getValue() + "_SAMPOVR_InterruptHandler", 2)
            else:
                Database.setSymbolValue("core", InterruptHandler[4], adcInstanceName.getValue() + "_Handler", 2)
    else:
        if adcSym_INTENSET_RESRDY.getValue() == True or adcSym_INTENSET_RESOVR.getValue() == True or adcSym_INTENSET_WCMP.getValue() == True or adcSym_INTENSET_SAMPRDY.getValue() == True or adcSym_INTENSET_SAMPOVR.getValue() == True:
            Database.setSymbolValue("core", InterruptVector, True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock, True, 2)
            Database.setSymbolValue("core", InterruptHandler, adcInstanceName.getValue() + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptVector, False, 2)
            Database.setSymbolValue("core", InterruptHandlerLock, False, 2)
            Database.setSymbolValue("core", InterruptHandler, adcInstanceName.getValue() + "_Handler", 2)


def updateADCInterruptWarningStatus(symbol, event):
    global multiVectorSupport
    symVisible = False
    if multiVectorSupport:
        if adcSym_INTENSET_WCMP.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate[0].split("core.")[1]) == True):
                symVisible = True
        if adcSym_INTENSET_RESRDY.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate[1].split("core.")[1]) == True):
                symVisible = True
        if adcSym_INTENSET_SAMPRDY.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate[2].split("core.")[1]) == True):
                symVisible = True
        if adcSym_INTENSET_RESOVR.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate[3].split("core.")[1]) == True):
                symVisible = True
        if adcSym_INTENSET_SAMPOVR.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate[4].split("core.")[1]) == True):
                symVisible = True
        if symVisible == True:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        if adcSym_INTENSET_RESRDY.getValue() == True or adcSym_INTENSET_RESOVR.getValue() == True or adcSym_INTENSET_WCMP.getValue() == True or adcSym_INTENSET_SAMPRDY.getValue() == True or adcSym_INTENSET_SAMPOVR.getValue() == True:
            if (Database.getSymbolValue("core", InterruptVectorUpdate) == True):
                symbol.setVisible(True)
            else:
                symbol.setVisible(False)
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
    prescaler = adcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    sample_cycles = adcSym_CTRLE_SAMPLEN.getValue()
    data_width = adcSym_CTRLD_RESOLUTION.getSelectedKey()[:-3]
    conv_time = float(((((int(sample_cycles) + 1) + int(data_width)) * int(prescaler)) + 6) * 1000000.0) / clock_freq
    symbol.setLabel("**** Conversion Time is " + str(conv_time) + " uS ****")

def adcCalcTimeBaseValue(symbole, event):
    clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    timebase_time = adcSym_CTRLB_TIMEBASE.getValue()
    timebase_value = math.ceil(clock_freq * (timebase_time / 1000000.0))
    adcSym_TIMEBASE_VALUE.setValue(timebase_value)

def adcEvesysConfigure(symbol, event):
    if(event["id"] == "ADC_EVCTRL_RESRDYEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(adcInstanceName.getValue())+"_RESRDY_ACTIVE", event["value"], 2)

    if(event["id"] == "ADC_WINDOW_OUTPUT_EVENT"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(adcInstanceName.getValue())+"_WINMON_ACTIVE", event["value"], 2)

    if(event["id"] == "ADC_EVCTRL_SAMPRDYEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(adcInstanceName.getValue())+"_SAMPRDY_ACTIVE", event["value"], 2)

    if (adcSym_CONV_TRIGGER.getValue() == "HW Event Trigger"):
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

# def adcResultConfVisibility(symbol, event):
#     component = symbol.getComponent()
#     resolution = component.getSymbolValue("ADC_CTRLC_RESSEL")
#     bit = component.getSymbolValue("ADC_RES_BIT")
#     if (resolution == 1 and bit == "Accumulation/Averaging"):
#         symbol.setVisible(True)
#     else:
#         symbol.setVisible(False)

def adcADJRESCalc(symbol, event):
    component = symbol.getComponent()
    resolution = component.getSymbolValue("ADC_CTRLC_RESSEL")
    bit = component.getSymbolValue("ADC_RES_BIT")
    shift = component.getSymbolValue("ADC_AVGCTRL_ADJRES")
    if resolution == 1 and bit != "Accumulation/Averaging":
        symbol.setValue(adcResult[bit]["ADJRES"])
    else:
        symbol.setValue(shift)   

def adcSAMPLENUMCalc(symbol, event):
    component = symbol.getComponent()
    resolution = component.getSymbolValue("ADC_CTRLD_RESOLUTION")
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
    if (adcSym_CONV_TRIGGER.getValue() != "HW Event Trigger"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def adcOptionVisible(symbol, event):
    if(event["value"] != "Free Run"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcWindowVisible(symbol, event):
    if (event["value"] > 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcPosInpVisible(symbol, event):
    if (adcSym_CONV_TRIGGER.getValue() != "Free Run"):
        if (adcSym_SEQ_ENABLE.getValue() == True):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setVisible(True)

def adcSUPCVisible(symbol, event):
    if (event["id"] == "ADC_INPUTCTRL_MUXPOS"):
        symObj = event["symbol"]
        if (symObj.getSelectedKey() == "BANDGAP"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

    if (event["id"] == "ADC_CTRLC_REFSEL"):
        symObj = event["symbol"]
        if (symObj.getSelectedKey() == "INTREF"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def adcMuxNegVisibility(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcFilterVisibility(symbol, event):
    symObj = event["symbol"]
    if ((symObj.getSelectedKey() == "SERIES") or (symObj.getSelectedKey() == "BURST")):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcChopVisibility(symbol, event):
    symObj = event["symbol"]
    if ((symObj.getSelectedKey() == "SERIES") or (symObj.getSelectedKey() == "BURST")):
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
    dict = {}
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
            adcSym_CTRLE_SAMPLEN.setValue(sample_count)

        # Calculate prescaler and ADC sample counts based on requested conversion time
        if not(args["reference"] == "default"):
            # ToDO: Placeholder. To be done later
            pass

        # Find the key index of the RESOLUTION
        count = adcSym_CTRLD_RESOLUTION.getKeyCount()
        resIndex = 0
        for i in range(0, count):
            if ( args["resolution"] in adcSym_CTRLD_RESOLUTION.getKeyDescription(i) ):
                resIndex = i
                break

        # Enable/ Disable slave for ADC module
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

    if (messageID == "PMSM_FOC_ADC_CH_CONF"):
        component = str(adcInstanceName.getValue()).lower()
        instanceNum = int(filter(str.isdigit,str(adcInstanceName.getValue())))
        dict['ADC_MAX_CH'] = Database.getSymbolValue(component, "ADC_NUM_CHANNELS")
        dict['ADC_MAX_MODULES'] = Database.getSymbolValue(component, "ADC_NUM_MODULES")
        #Change ADC channels if they are changed in the PMSM_FOC
        resetChannelsForPMSMFOC()
        AdcConfigForPMSMFOC(component, instanceNum, args)

    elif ( messageID == "SET_ADC_CONFIG_PARAMS"):
        # Set ADC configuration parameters
        setAdcConfigParams( args )

    elif (messageID == "ADC_CONFIG_HW_IO"):
        component = str(adcInstanceName.getValue()).lower()
        setting, muxInput, enable = args['config']

        if "VREF" in setting.upper():
            extRefNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_REFCTRL__REFSEL\"]/value@[caption=\"External Reference\"]")
            symbolName = "ADC_CTRLC_REFSEL"
            symbolValue = int(extRefNode.getAttribute("value"), 0)
            res = Database.setSymbolValue(component, symbolName, symbolValue)
            if res == True:
                dict = {"Result": "Success"}
            else:
                dict = {"Result": "DB Error in setting ADC_CTRLC_REFSEL value".format(symbolValue)}
        else:
            channel = "".join(filter(lambda x: x.isdigit(), setting))

            adcInputCtrlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__{}\"]".format(muxInput))
            adcInputValues = adcInputCtrlNode.getChildren()

            dict = {"Result": "AIN{} is not a permitted value for ADC_INPUTCTRL_{}".format(channel, muxInput)}

            if enable == False:
                Database.clearSymbolValue(component, "ADC_INPUTCTRL_{}".format(muxInput))
                if muxInput == 'MUXNEG':
                    Database.clearSymbolValue(component, "ADC_COMMAND_DIFFMODE")
                    
                dict = {"Result": "Success"}
            else:
                for adcInputValue in adcInputValues:
                    if adcInputValue.getAttribute("name") == "AIN{}".format(channel):
                        if muxInput == 'MUXNEG':
                            res = Database.setSymbolValue(component, "ADC_COMMAND_DIFFMODE", enable)
                            adcSym_INPUTCTRL_MUXNEG.setSelectedKey("AIN{}".format(channel))
                        else:
                            res = True
                            adcSym_INPUTCTRL_MUXPOS.setSelectedKey("AIN{}".format(channel))
                        
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
    count = adcSym_CTRLD_RESOLUTION.getKeyCount()
    resIndex = 0
    for i in range(0,count):
        if (str(resolution) in adcSym_CTRLD_RESOLUTION.getKeyDescription(i) ):
            resIndex = i
            break

    #Enable slave for ADC1
    if instanceNum == 1 :
       Database.setSymbolValue(component, "ADC_CTRLA_SLAVEEN", True)

    # Enable ADC modules, Ph U interrupt
    if (int(phUModule) == instanceNum):
        adcSym_INPUTCTRL_MUXPOS.setSelectedKey("AIN"+str(phUCh))
        Database.setSymbolValue(component, "ADC_INTENSET_RESRDY", True)
        Database.setSymbolValue(component, "ADC_CH_PHASE_U", "ADC_POSINPUT_AIN"+str(phUCh))
    if (int(phVModule) == instanceNum):
        adcSym_INPUTCTRL_MUXPOS.setSelectedKey("AIN"+str(phVCh))
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
    global InterruptVectorUpdate
    global adcInstanceName
    global multiVectorSupport
    global InterruptVectorSecurity

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    Log.writeInfoMessage("Running " + adcInstanceName.getValue())

    # clock enable
    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    count = 0
    vectorNode=ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
    vectorValues = vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == adcInstanceName.getValue():
            count = count + 1

    if count > 1:
        multiVectorSupport = True

    # ------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = []

    pinout = "SAMC21N"
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

    #timebase value
    adc_clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    timebase_value = adc_clock_freq * 0.000001

    global adcSym_TIMEBASE_VALUE
    adcSym_TIMEBASE_VALUE = adcComponent.createFloatSymbol("ADC_TIMEBASE_VALUE", None)
    adcSym_TIMEBASE_VALUE.setVisible(False)
    adcSym_TIMEBASE_VALUE.setDefaultValue(timebase_value)

    #number of ADC modules
    adcSym_NUM_MODULES = adcComponent.createIntegerSymbol("ADC_NUM_MODULES", None)
    adcSym_NUM_MODULES.setVisible(False)
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]")
    adcSym_NUM_MODULES.setDefaultValue(len(adc.getChildren()))    

#----------------- motor control APIs ---------------------------------
    # adcConvAPI = adcComponent.createStringSymbol("ADC_START_CONV_API", None)
    # adcConvAPI.setVisible(False)
    # adcConvAPI.setValue(adcInstanceName.getValue()+"_ConversionStart")

    # adcResultAPI = adcComponent.createStringSymbol("ADC_GET_RESULT_API", None)
    # adcResultAPI.setVisible(False)
    # adcResultAPI.setValue(adcInstanceName.getValue()+"_ConversionResultGet")

    # adcResultReadyAPI = adcComponent.createStringSymbol("ADC_IS_RESULT_READY_API", None)
    # adcResultReadyAPI.setVisible(False)
    # adcResultReadyAPI.setValue(adcInstanceName.getValue()+"_ConversionStatusGet")

    # adcCallbackAPI = adcComponent.createStringSymbol("ADC_CALLBACK_API", None)
    # adcCallbackAPI.setVisible(False)
    # adcCallbackAPI.setValue(adcInstanceName.getValue()+"_CallbackRegister")

    # adcStartAPI = adcComponent.createStringSymbol("ADC_START_API", None)
    # adcStartAPI.setVisible(False)
    # adcStartAPI.setValue(adcInstanceName.getValue()+"_Enable")

    # adcStopAPI = adcComponent.createStringSymbol("ADC_STOP_API", None)
    # adcStopAPI.setVisible(False)
    # adcStopAPI.setValue(adcInstanceName.getValue()+"_Disable")

    # adcChannelSelectAPI = adcComponent.createStringSymbol("ADC_CHANNEL_SELECT_API", None)
    # adcChannelSelectAPI.setVisible(False)
    # adcChannelSelectAPI.setValue(adcInstanceName.getValue() + "_ChannelSelect")

    # adcIntDisableAPI = adcComponent.createStringSymbol("ADC_INT_DISABLE_API", None)
    # adcIntDisableAPI.setVisible(False)
    # adcIntDisableAPI.setValue(adcInstanceName.getValue() + "_InterruptsDisable")

    # adcIntEnableAPI = adcComponent.createStringSymbol("ADC_INT_ENABLE_API", None)
    # adcIntEnableAPI.setVisible(False)
    # adcIntEnableAPI.setValue(adcInstanceName.getValue() + "_InterruptsEnable")

    # adcIntClearAPI = adcComponent.createStringSymbol("ADC_INT_CLEAR_API", None)
    # adcIntClearAPI.setVisible(False)
    # adcIntClearAPI.setValue(adcInstanceName.getValue() + "_InterruptsClear")

    # adcPhUCh = adcComponent.createStringSymbol("ADC_CH_PHASE_U", None)
    # adcPhUCh.setVisible(False)
    # adcPhUCh.setValue("ADC_POSINPUT_AIN2")

    # adcPhVCh = adcComponent.createStringSymbol("ADC_CH_PHASE_V", None)
    # adcPhVCh.setVisible(False)
    # adcPhVCh.setValue("ADC_POSINPUT_AIN5")

    # adcVdcCh = adcComponent.createStringSymbol("ADC_CH_VDC_BUS", None)
    # adcVdcCh.setVisible(False)
    # adcVdcCh.setValue("ADC_POSINPUT_AIN0")

    # adcPotCh = adcComponent.createStringSymbol("ADC_CH_POT", None)
    # adcPotCh.setVisible(False)
    # adcPotCh.setValue("ADC_POSINPUT_AIN0")

    # adcGND = adcComponent.createStringSymbol("ADC_GND", None)
    # adcGND.setVisible(False)
    # adcGND.setValue("ADC_NEGINPUT_GND")

    # adcResultInt = adcComponent.createStringSymbol("INTERRUPT_ADC_RESULT", None)
    # adcResultInt.setVisible(False)
    # adcResultInt.setValue(adcInstanceName.getValue()+"_RESRDY_IRQn")


    # slave mode
    # global adcSym_CTRLA_SLAVEEN
    # adcSym_CTRLA_SLAVEEN = adcComponent.createBooleanSymbol("ADC_CTRLA_SLAVEEN", None)
    # adcSym_CTRLA_SLAVEEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2247;register:CTRLA")
    # adcSym_CTRLA_SLAVEEN.setLabel("Enable Slave")
    # adcSym_CTRLA_SLAVEEN.setDefaultValue(False)
    # mode = "0"
    # node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\""+adcInstanceName.getValue()+"\"]/parameters")
    # param_values = []
    # param_values = node.getChildren()
    # for index in range(0, len(param_values)):
    #     if "MASTER_SLAVE_MODE" in param_values[index].getAttribute("name"):
    #         mode = param_values[index].getAttribute("value")
    #     if (mode == "2"):
    #         adcSym_CTRLA_SLAVEEN.setVisible(True)
    #     else:
    #         adcSym_CTRLA_SLAVEEN.setVisible(False)

    # for index in range(0, len(param_values)):
    #     if "LOAD_CALIB" in param_values[index].getAttribute("name"):
    #         adcSym_CALIB = adcComponent.createBooleanSymbol("ADC_LOAD_CALIB", None)
    #         adcSym_CALIB.setVisible(False)
    #         adcSym_CALIB.setDefaultValue(True)

    #         # NVM register
    #         adcSym_calib_reg = adcComponent.createStringSymbol("ADC_NVM_CALIB_REG", None)
    #         adcSym_calib_reg.setVisible(False)
    #         reg = ""
    #         node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"OTP5_FUSES\"]")
    #         if node != None:
    #             reg = "OTP5_ADDR"
    #         else:
    #             node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"SW_CALIB_FUSES\"]")
    #             if node != None:
    #                 reg = "SW_CALIB_ADDR"
    #         adcSym_calib_reg.setDefaultValue(reg)

    # # start conversion type configuration
    # global adcSym_COMMAND_STARTCONVERSIONTYPE
    # adcSym_COMMAND_STARTCONVERSIONTYPE = adcComponent.createKeyValueSetSymbol("ADC_COMMAND_STARTCONVERSIONTYPE", None)
    # adcSym_COMMAND_STARTCONVERSIONTYPE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:COMMAND")
    # adcSym_COMMAND_STARTCONVERSIONTYPE.setLabel("Select Start Convrsion Mode")
    # adcSym_COMMAND_STARTCONVERSIONTYPE.setDefaultValue(0)
    # adcSym_COMMAND_STARTCONVERSIONTYPE.setOutputMode("Key")
    # adcSym_COMMAND_STARTCONVERSIONTYPE.setDisplayMode("Description")
    # adcStartNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_COMMAND__START\"]")
    # adcStartValues = []
    # adcStartValues = adcStartNode.getChildren()
    # for index in range(0, len(adcStartValues)):
    #     adcSym_COMMAND_STARTCONVERSIONTYPE.addKey(adcStartValues[index].getAttribute("name"), adcStartValues[index].getAttribute("value"), adcStartValues[index].getAttribute("caption"))

    # voltage pump disable configuration
    adcSym_CTRLD_VPD = adcComponent.createBooleanSymbol("ADC_CTRLD_VPD", None)
    adcSym_CTRLD_VPD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_VPD.setLabel("Disable Voltage Pump")
    adcSym_CTRLD_VPD.setVisible(True)

    # timbase configuration
    global adcSym_CTRLB_TIMEBASE
    adcSym_CTRLB_TIMEBASE = adcComponent.createIntegerSymbol("ADC_CTRLB_TIMEBASE", None)
    adcSym_CTRLB_TIMEBASE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLB")
    adcSym_CTRLB_TIMEBASE.setLabel("Select Timebase Time (in microseconds)")
    adcSym_CTRLB_TIMEBASE.setMin(1)
    adcSym_CTRLB_TIMEBASE.setMax(32)
    adcSym_CTRLB_TIMEBASE.setDefaultValue(1) 
    adcSym_CTRLB_TIMEBASE.setDependencies(adcCalcTimeBaseValue, ["ADC_CTRLB_TIMEBASE"])

    # operation mode configuration
    global adcSym_COMMAND_OPMODE
    adcSym_COMMAND_OPMODE = adcComponent.createKeyValueSetSymbol("ADC_COMMAND_OPMODE", None)
    adcSym_COMMAND_OPMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:COMMAND")
    adcSym_COMMAND_OPMODE.setLabel("Select Operation Mode")
    adcSym_COMMAND_OPMODE.setDefaultValue(0)
    adcSym_COMMAND_OPMODE.setOutputMode("Value")
    adcSym_COMMAND_OPMODE.setDisplayMode("Description")
    adcOperationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_COMMAND__MODE\"]")
    adcOperationValues = []
    adcOperationValues = adcOperationNode.getChildren()
    for index in range(0, len(adcOperationValues)):
        adcSym_COMMAND_OPMODE.addKey(adcOperationValues[index].getAttribute("name"), adcOperationValues[index].getAttribute("value"), adcOperationValues[index].getAttribute("caption"))

    # filter configuration
    adcSym_CTRLD_FILTER = adcComponent.createBooleanSymbol("ADC_CTRLD_FILTER", adcSym_COMMAND_OPMODE)
    adcSym_CTRLD_FILTER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_FILTER.setLabel("Enable Filter")
    adcSym_CTRLD_FILTER.setVisible(False)
    adcSym_CTRLD_FILTER.setDependencies(adcFilterVisibility, ["ADC_COMMAND_OPMODE"])

    # chop configuration
    adcSym_CTRLD_CHOPPING = adcComponent.createBooleanSymbol("ADC_CTRLD_CHOPPING", adcSym_COMMAND_OPMODE)
    adcSym_CTRLD_CHOPPING.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_CHOPPING.setLabel("Enable Chopping")
    adcSym_CTRLD_CHOPPING.setVisible(False)
    adcSym_CTRLD_CHOPPING.setDependencies(adcChopVisibility, ["ADC_COMMAND_OPMODE"])

    # prescaler configuration
    global adcSym_CTRLB_PRESCALER
    adcSym_CTRLB_PRESCALER = adcComponent.createKeyValueSetSymbol("ADC_CTRLB_PRESCALER", None)
    adcSym_CTRLB_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLB")
    adcSym_CTRLB_PRESCALER.setLabel("Select Prescaler")
    adcSym_CTRLB_PRESCALER.setDefaultValue(2)
    adcSym_CTRLB_PRESCALER.setOutputMode("Key")
    adcSym_CTRLB_PRESCALER.setDisplayMode("Description")
    adcPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLB__PRESCALER\"]")
    adcPrescalerValues = []
    adcPrescalerValues = adcPrescalerNode.getChildren()
    for index in range(0, len(adcPrescalerValues)):
        adcSym_CTRLB_PRESCALER.addKey(adcPrescalerValues[index].getAttribute("name"), adcPrescalerValues[index].getAttribute("value"), adcPrescalerValues[index].getAttribute("caption"))
    adcSym_CTRLB_PRESCALER.setDependencies(adcSlaveModeVisibility, ["ADC_CTRLA_SLAVEEN"])

    # sampling time
    global adcSym_CTRLE_SAMPLEN
    adcSym_CTRLE_SAMPLEN = adcComponent.createIntegerSymbol("ADC_CTRLE_SAMPLEN", None)
    adcSym_CTRLE_SAMPLEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:SAMPCTRL")
    adcSym_CTRLE_SAMPLEN.setLabel("Select Sample Length (cycles)")
    adcSym_CTRLE_SAMPLEN.setMin(1)
    adcSym_CTRLE_SAMPLEN.setMax(256)
    adcSym_CTRLE_SAMPLEN.setDefaultValue(4)

    clock_freq = Database.getSymbolValue("core", adcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = adcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    sample_cycles = adcSym_CTRLE_SAMPLEN.getValue()
    data_width = 12
    conv_time = float((int(sample_cycles) + int(data_width)) * int(prescaler) * 1000000.0) / clock_freq
    if adcInstanceName.getValue()[-1].isdigit():
        component = int(adcInstanceName.getValue()[-1]) - 1
    else:
        component = ""

    # Sampling time calculation
    adcSym_CTRLE_SAMPLEN_TIME = adcComponent.createCommentSymbol("ADC_CTRLE_SAMPLEN_TIME", None)
    adcSym_CTRLE_SAMPLEN_TIME.setLabel("**** Conversion Time is " + str(conv_time) + " us ****")
    # Dependency registration is done after all dependencies are defined.

    # reference selection
    adcSym_CTRLC_REFSEL = adcComponent.createKeyValueSetSymbol("ADC_CTRLC_REFSEL", None)
    adcSym_CTRLC_REFSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLC")
    adcSym_CTRLC_REFSEL.setLabel("Select Reference")
    default = 0
    adcSym_CTRLC_REFSEL.setOutputMode("Key")
    adcSym_CTRLC_REFSEL.setDisplayMode("Description")
    adcReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLC__REFSEL\"]")
    adcReferenceValues = []
    adcReferenceValues = adcReferenceNode.getChildren()
    for index in range(0, len(adcReferenceValues)):
        if adcReferenceValues[index].getAttribute("caption") == "VDDANA":
            default = index
        if adcReferenceValues[index].getAttribute("caption").lower() == "external reference":
            adcSym_CTRLC_REFSEL.addKey(adcReferenceValues[index].getAttribute("name"), adcReferenceValues[index].getAttribute("value"),
            adcReferenceValues[index].getAttribute("caption") + " (" + adcReferenceValues[index].getAttribute("name") + ")")
        else:
            adcSym_CTRLC_REFSEL.addKey(adcReferenceValues[index].getAttribute("name"), adcReferenceValues[index].getAttribute("value"),
            adcReferenceValues[index].getAttribute("caption"))
    adcSym_CTRLC_REFSEL.setDefaultValue(default)

    # # trigger
    global adcSym_CONV_TRIGGER
    adcSym_CONV_TRIGGER = adcComponent.createComboSymbol("ADC_CONV_TRIGGER", None, ["Free Run", "SW Trigger", "HW Event Trigger"])
    adcSym_CONV_TRIGGER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CONV_TRIGGER.setDefaultValue("Free Run")
    adcSym_CONV_TRIGGER.setLabel("Select Conversion Trigger")

    adcSym_START_EVENT = adcComponent.createKeyValueSetSymbol("ADC_EVCTRL_START", adcSym_CONV_TRIGGER)
    adcSym_START_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:EVCTRL")
    adcSym_START_EVENT.setLabel("Start Event Input")
    adcSym_START_EVENT.setVisible(False)
    adcSym_START_EVENT.setOutputMode("Value")
    adcSym_START_EVENT.setDisplayMode("Description")
    adcSym_START_EVENT.addKey("DISABLED", "0", "Disabled")
    adcSym_START_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    adcSym_START_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    adcSym_START_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER"])

    adcPositiveInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXPOS\"]")
    adcPositiveInputValues = []
    adcPositiveInputValues = adcPositiveInputNode.getChildren()
    for index in range(0, len(adcPositiveInputValues)):
        value = int(adcPositiveInputValues[index].getAttribute("value"), 16)

    # start conversion configuration
    global adcSym_COMMAND_CTRLCONV
    adcSym_COMMAND_CTRLCONV = adcComponent.createKeyValueSetSymbol("ADC_COMMAND_CTRLCONV", None)
    adcSym_COMMAND_CTRLCONV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:COMMAND")
    adcSym_COMMAND_CTRLCONV.setLabel("Select Conversion Start Type")
    adcSym_COMMAND_CTRLCONV.setDefaultValue(0)
    adcSym_COMMAND_CTRLCONV.setOutputMode("Value")
    adcSym_COMMAND_CTRLCONV.setDisplayMode("Description")
    adcOperationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_COMMAND__START\"]")
    adcOperationValues = []
    adcOperationValues = adcOperationNode.getChildren()
    for index in range(0, len(adcOperationValues)):
        adcSym_COMMAND_CTRLCONV.addKey(adcOperationValues[index].getAttribute("name"), adcOperationValues[index].getAttribute("value"), adcOperationValues[index].getAttribute("caption"))

    adcSym_NUM_CHANNELS = adcComponent.createIntegerSymbol("ADC_NUM_CHANNELS", None)
    adcSym_NUM_CHANNELS.setVisible(False)
    adcSym_NUM_CHANNELS.setDefaultValue(value)

    adcChannelMenu = adcComponent.createMenuSymbol("ADC_CHANNEL_MENU", None)
    adcChannelMenu.setLabel("Channel Configuration")

    adcSym_COMMAND_DIFFMODE = adcComponent.createBooleanSymbol("ADC_COMMAND_DIFFMODE", adcChannelMenu)
    adcSym_COMMAND_DIFFMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:COMMAND")
    adcSym_COMMAND_DIFFMODE.setLabel("Enable Differential Mode")
    adcSym_COMMAND_DIFFMODE.setDefaultValue(False)

    # positive input
    global adcSym_INPUTCTRL_MUXPOS
    adcSym_INPUTCTRL_MUXPOS = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXPOS", adcChannelMenu)
    adcSym_INPUTCTRL_MUXPOS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INPUTCTRL")
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
            adcSym_INPUTCTRL_MUXPOS.addKey(adcPositiveInputValues[index].getAttribute("name"), adcPositiveInputValues[index].getAttribute("value"),
            adcPositiveInputValues[index].getAttribute("caption"))
    adcSym_INPUTCTRL_MUXPOS.setVisible(True)
    #adcSym_INPUTCTRL_MUXPOS.setDependencies(adcPosInpVisible, ["ADC_CONV_TRIGGER"])

    # negative input
    global adcSym_INPUTCTRL_MUXNEG
    adcSym_INPUTCTRL_MUXNEG = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXNEG", adcChannelMenu)
    adcSym_INPUTCTRL_MUXNEG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INPUTCTRL")
    adcSym_INPUTCTRL_MUXNEG.setLabel("Select Negative Input")
    adcSym_INPUTCTRL_MUXNEG.setOutputMode("Key")
    adcSym_INPUTCTRL_MUXNEG.setDisplayMode("Description")
    adcSym_INPUTCTRL_MUXNEG.setVisible(False)
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
    adcSym_INPUTCTRL_MUXNEG.setDependencies(adcMuxNegVisibility, ["ADC_COMMAND_DIFFMODE"])

    adcResultMenu = adcComponent.createMenuSymbol("ADC_RESULT_MENU", None)
    adcResultMenu.setLabel("Result Configuration")

    # resolution configuration
    global adcSym_CTRLD_RESOLUTION
    adcSym_CTRLD_RESOLUTION = adcComponent.createKeyValueSetSymbol("ADC_CTRLD_RESOLUTION", adcResultMenu)
    adcSym_CTRLD_RESOLUTION.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_RESOLUTION.setLabel("Select Result Resolution")
    adcSym_CTRLD_RESOLUTION.setDefaultValue(0)
    adcSym_CTRLD_RESOLUTION.setOutputMode("Key")
    adcSym_CTRLD_RESOLUTION.setDisplayMode("Description")
    adcResultResolutionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLD__RESOLUTION\"]")
    adcResultResolutionValues = []
    adcResultResolutionValues = adcResultResolutionNode.getChildren()
    for index in range (0 , len(adcResultResolutionValues)):
        adcSym_CTRLD_RESOLUTION.addKey(adcResultResolutionValues[index].getAttribute("name"), adcResultResolutionValues[index].getAttribute("value"),
        adcResultResolutionValues[index].getAttribute("caption"))

    #adcSym_CTRLD_SAMPNUM.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT"])

    # # division coefficient
    # adcSym_AVGCTRL_ADJRES = adcComponent.createIntegerSymbol("ADC_AVGCTRL_ADJRES", adcSym_RES_BIT)
    # adcSym_AVGCTRL_ADJRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_u2247;register:AVGCTRL")
    # adcSym_AVGCTRL_ADJRES.setLabel("Number of Right Shifts")
    # adcSym_AVGCTRL_ADJRES.setMin(0)
    # adcSym_AVGCTRL_ADJRES.setMax(7)
    # adcSym_AVGCTRL_ADJRES.setDefaultValue(0)
    # adcSym_AVGCTRL_ADJRES.setVisible(False)
    # adcSym_AVGCTRL_ADJRES.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT"])

    # adcSym_ADJRES = adcComponent.createIntegerSymbol("ADC_ADJRES", adcSym_RES_BIT)
    # adcSym_ADJRES.setVisible(False)
    # adcSym_ADJRES.setDependencies(adcADJRESCalc, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_ADJRES"])

    # adcSym_SAMPLENUM = adcComponent.createIntegerSymbol("ADC_SAMPLENUM", adcSym_RES_BIT)
    # adcSym_SAMPLENUM.setVisible(False)
    # adcSym_SAMPLENUM.setDependencies(adcSAMPLENUMCalc, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_SAMPLENUM"])

    # # left adjusted mode
    # adcSym_CTRLC_LEFTADJ = adcComponent.createBooleanSymbol("ADC_CTRLC_LEFTADJ", adcResultMenu)
    # adcSym_CTRLC_LEFTADJ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLC")
    # adcSym_CTRLC_LEFTADJ.setLabel("Left Aligned Result")
    # adcSym_CTRLC_LEFTADJ.setVisible(True)

    # interrupt mode
    global adcSym_INTENSET_RESRDY
    adcSym_INTENSET_RESRDY = adcComponent.createBooleanSymbol("ADC_INTENSET_RESRDY", adcResultMenu)
    adcSym_INTENSET_RESRDY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INTENSET")
    adcSym_INTENSET_RESRDY.setLabel("Enable Result Ready Interrupt")

    global adcSym_INTENSET_RESOVR
    adcSym_INTENSET_RESOVR = adcComponent.createBooleanSymbol("ADC_INTENSET_RESOVR", adcResultMenu)
    adcSym_INTENSET_RESOVR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INTENSET")
    adcSym_INTENSET_RESOVR.setLabel("Enable Result Overwrite Interrupt")

    # event out mode
    adcSym_EVCTRL_RSERDYEO = adcComponent.createBooleanSymbol("ADC_EVCTRL_RESRDYEO", adcResultMenu)
    adcSym_EVCTRL_RSERDYEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:EVCTRL")
    adcSym_EVCTRL_RSERDYEO.setLabel("Enable Result Ready Event Out")

    # scaling configuration
    adcSym_CTRLD_SCALING = adcComponent.createKeyValueSetSymbol("ADC_CTRLD_SCALING", adcResultMenu)
    adcSym_CTRLD_SCALING.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_SCALING.setLabel("Select Result Scaling")
    adcSym_CTRLD_SCALING.setDefaultValue(0)
    adcSym_CTRLD_SCALING.setOutputMode("Value")
    adcSym_CTRLD_SCALING.setDisplayMode("Description")
    adcResultScalingNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLD__SCALING\"]")
    adcResultScalingValues = []
    adcResultScalingValues = adcResultScalingNode.getChildren()
    for index in range (0 , len(adcResultScalingValues)):
        adcSym_CTRLD_SCALING.addKey(adcResultScalingValues[index].getAttribute("name"), adcResultScalingValues[index].getAttribute("value"),
        adcResultScalingValues[index].getAttribute("caption"))
    

    #Sample menu
    adcSampleMenu = adcComponent.createMenuSymbol("ADC_SAMPLE_MENU", None)
    adcSampleMenu.setLabel("Sample Configuration")
    
    # Sample Accumulation Number Select
    adcSym_CTRLD_SAMPNUM = adcComponent.createKeyValueSetSymbol("ADC_CTRLD_SAMPNUM", adcSampleMenu)
    adcSym_CTRLD_SAMPNUM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLD")
    adcSym_CTRLD_SAMPNUM.setLabel("Number of Accumulated Samples")
    adcSym_CTRLD_SAMPNUM.setDefaultValue(0)
    adcSym_CTRLD_SAMPNUM.setOutputMode("Value")
    adcSym_CTRLD_SAMPNUM.setDisplayMode("Description")
    adcSym_CTRLD_SAMPNUM.setVisible(True)
    adcSampleNumNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLD__SAMPNUM\"]")
    adcSampleNumValues = []
    adcSampleNumValues = adcSampleNumNode.getChildren()
    for index in range (0 , len(adcSampleNumValues)):
        adcSym_CTRLD_SAMPNUM.addKey(adcSampleNumValues[index].getAttribute("name"), adcSampleNumValues[index].getAttribute("value"),
        adcSampleNumValues[index].getAttribute("caption"))

    # interrupt mode
    global adcSym_INTENSET_SAMPRDY
    adcSym_INTENSET_SAMPRDY = adcComponent.createBooleanSymbol("ADC_INTENSET_SAMPRDY", adcSampleMenu)
    adcSym_INTENSET_SAMPRDY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INTENSET")
    adcSym_INTENSET_SAMPRDY.setLabel("Enable Sample Ready Interrupt")

    global adcSym_INTENSET_SAMPOVR
    adcSym_INTENSET_SAMPOVR = adcComponent.createBooleanSymbol("ADC_INTENSET_SAMPOVR", adcSampleMenu)
    adcSym_INTENSET_SAMPOVR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INTENSET")
    adcSym_INTENSET_SAMPOVR.setLabel("Enable Sample Overwrite Interrupt")

    # event out mode
    adcSym_EVCTRL_SAMPRDYEO = adcComponent.createBooleanSymbol("ADC_EVCTRL_SAMPRDYEO", adcSampleMenu)
    adcSym_EVCTRL_SAMPRDYEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:EVCTRL")
    adcSym_EVCTRL_SAMPRDYEO.setLabel("Enable Sample Ready Event Out")

    adcWindowMenu = adcComponent.createMenuSymbol("ADC_WINDOW_CONFIG_MENU", None)
    adcWindowMenu.setLabel("Window Mode Configuration")

    # Configure mode for Window operation
    adcSym_WINCTRL_WINMODE = adcComponent.createKeyValueSetSymbol("ADC_WINCTRL_WINMODE", adcWindowMenu)
    adcSym_WINCTRL_WINMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:WINCTRL")
    adcSym_WINCTRL_WINMODE.setLabel("Select Window Monitor Mode")
    adcSym_WINCTRL_WINMODE.setDefaultValue(0)
    adcSym_WINCTRL_WINMODE.setOutputMode("Value")
    adcSym_WINCTRL_WINMODE.setDisplayMode("Description")
    adcWindowConfigNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_WINCTRL__WINMODE\"]")
    adcWindowConfigValues = []
    adcWindowConfigValues = adcWindowConfigNode.getChildren()
    for index in range (0 , len(adcWindowConfigValues)):
        adcSym_WINCTRL_WINMODE.addKey(adcWindowConfigValues[index].getAttribute("name"), adcWindowConfigValues[index].getAttribute("value"),
        adcWindowConfigValues[index].getAttribute("caption"))

    # Configure Source for Window operation
    adcSym_WINCTRL_WINSRC = adcComponent.createKeyValueSetSymbol("ADC_WINCTRL_WINSRC", adcWindowMenu)
    adcSym_WINCTRL_WINSRC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:WINCTRL")
    adcSym_WINCTRL_WINSRC.setLabel("Select Window Monitor Source")
    adcSym_WINCTRL_WINSRC.setDefaultValue(0)
    adcSym_WINCTRL_WINSRC.setOutputMode("Value")
    adcSym_WINCTRL_WINSRC.setDisplayMode("Description")
    adcWindowConfigNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_WINCTRL__WINSRC\"]")
    adcWindowConfigValues = []
    adcWindowConfigValues = adcWindowConfigNode.getChildren()
    for index in range (0 , len(adcWindowConfigValues)):
        adcSym_WINCTRL_WINSRC.addKey(adcWindowConfigValues[index].getAttribute("name"), adcWindowConfigValues[index].getAttribute("value"),
        adcWindowConfigValues[index].getAttribute("caption"))
    adcSym_WINCTRL_WINSRC.setVisible(False)
    adcSym_WINCTRL_WINSRC.setDependencies(adcWindowVisible, ["ADC_WINCTRL_WINMODE"])

    # Window upper threshold
    adcSym_WINHT = adcComponent.createIntegerSymbol("ADC_WINHT", adcWindowMenu)
    adcSym_WINHT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:WINHT")
    adcSym_WINHT.setLabel("Window Upper Threshold")
    adcSym_WINHT.setMin(-32768)
    adcSym_WINHT.setMax(32767)
    adcSym_WINHT.setDefaultValue(1024)
    adcSym_WINHT.setVisible(False)
    adcSym_WINHT.setDependencies(adcWindowVisible, ["ADC_WINCTRL_WINMODE"])

    # Window lower threshold
    adcSym_WINLT = adcComponent.createIntegerSymbol("ADC_WINLT", adcWindowMenu)
    adcSym_WINLT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:WINLT")
    adcSym_WINLT.setLabel("Window Lower Threshold")
    adcSym_WINLT.setMin(-32768)
    adcSym_WINLT.setMax(32767)
    adcSym_WINLT.setDefaultValue(512)
    adcSym_WINLT.setVisible(False)
    adcSym_WINLT.setDependencies(adcWindowVisible, ["ADC_WINCTRL_WINMODE"])

    global adcSym_INTENSET_WCMP
    adcSym_INTENSET_WCMP = adcComponent.createBooleanSymbol("ADC_INTENSET_WCMP", adcWindowMenu)
    adcSym_INTENSET_WCMP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:INTENSET")
    adcSym_INTENSET_WCMP.setLabel("Enable Window Comparator Interrupt")
    adcSym_INTENSET_WCMP.setDefaultValue(False)
    adcSym_INTENSET_WCMP.setVisible(False)
    adcSym_INTENSET_WCMP.setDependencies(adcWindowVisible, ["ADC_WINCTRL_WINMODE"])

    # Enable Window Monitor Event Out
    adcSym_HW_OUT_EVENT = adcComponent.createBooleanSymbol("ADC_WINDOW_OUTPUT_EVENT", adcWindowMenu)
    adcSym_HW_OUT_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:EVCTRL")
    adcSym_HW_OUT_EVENT.setLabel("Enable Window Monitor Event Out")
    adcSym_HW_OUT_EVENT.setVisible(False)
    adcSym_HW_OUT_EVENT.setDependencies(adcWindowVisible, ["ADC_WINCTRL_WINMODE"])

    adcSym_CTRLE_SAMPLEN_TIME.setDependencies(adcCalcSampleTime, ["core."+adcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "adc"+str(component)+".ADC_CTRLB_PRESCALER", "ADC_CTRLE_SAMPLEN", "ADC_CTRLB_PRESCALER", "ADC_CTRLD_RESOLUTION"])

    adcSleepMenu = adcComponent.createMenuSymbol("ADC_SLEEP_MENU", None)
    adcSleepMenu.setLabel("Sleep Mode Configuration")

    # run in standby mode
    adcSym_CTRLA_RUNSTDBY = adcComponent.createBooleanSymbol("ADC_CTRLA_RUNSTDBY", adcSleepMenu)
    adcSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLA")
    adcSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")
    adcSym_CTRLA_RUNSTDBY.setVisible(True)

    # run in on demand control mode
    adcSym_CTRLA_ONDEMAND = adcComponent.createBooleanSymbol("ADC_CTRLA_ONDEMAND", adcSleepMenu)
    adcSym_CTRLA_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_06272;register:CTRLA")
    adcSym_CTRLA_ONDEMAND.setLabel("On Demand Control")
    adcSym_CTRLA_ONDEMAND.setVisible(True)

    adcSym_EVESYS_CONFIGURE = adcComponent.createIntegerSymbol("ADC_EVESYS_CONFIGURE", None)
    adcSym_EVESYS_CONFIGURE.setVisible(False)
    adcSym_EVESYS_CONFIGURE.setDependencies(adcEvesysConfigure, \
        ["ADC_WINDOW_OUTPUT_EVENT", "ADC_EVCTRL_RESRDYEO", "ADC_CONV_TRIGGER", "ADC_EVCTRL_START", "ADC_EVCTRL_SAMPRDYEO"])

    # adcSym_SUPC_COMMENT = adcComponent.createCommentSymbol("ADC_SUPC_COMMENT", None)
    # adcSym_SUPC_COMMENT.setLabel("*********** Enable Vref output in SUPC ***********")
    # adcSym_SUPC_COMMENT.setVisible(False)
    # adcSym_SUPC_COMMENT.setDependencies(adcSUPCVisible, ["ADC_CTRLC_REFSEL", "ADC_INPUTCTRL_MUXPOS"])
    ############################################################################
    #### Dependency ####
    ############################################################################
    if multiVectorSupport:
        InterruptVector = []
        InterruptHandler = []
        InterruptHandlerLock = []
        InterruptVectorUpdate = []
        InterruptVectorSecurity = []
        multiVectorSupport = adcComponent.createBooleanSymbol("MULTI_VECTOR_SUPPORT", None)
        multiVectorSupport.setVisible(False)

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
                InterruptVectorSecurity.append(name + "_SET_NON_SECURE")
        adcSym_IntLines = adcComponent.createIntegerSymbol("ADC_NUM_INT_LINES", None)
        adcSym_IntLines.setVisible(False)
        adcSym_IntLines.setDefaultValue((len(InterruptVector) - 1))

        # Interrupt Dynamic settings
        adcSym_UpdateInterruptStatus = adcComponent.createBooleanSymbol("ADC_INTERRUPT_STATUS", None)
        adcSym_UpdateInterruptStatus.setDependencies(updateADCInterruptStatus, ["ADC_INTENSET_RESRDY", "ADC_INTENSET_RESOVR", "ADC_INTENSET_WCMP", "ADC_INTENSET_SAMPRDY", "ADC_INTENSET_SAMPOVR"])
        adcSym_UpdateInterruptStatus.setVisible(False)

        InterruptVectorUpdate.append("ADC_INTENSET_RESRDY")
        InterruptVectorUpdate.append("ADC_INTENSET_WCMP")
        InterruptVectorUpdate.append("ADC_INTENSET_SAMPRDY")
        InterruptVectorUpdate.append("ADC_INTENSET_RESOVR")
        InterruptVectorUpdate.append("ADC_INTENSET_SAMPOVR")

        # Interrupt Warning status
        adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_INTERRUPT_ENABLE_COMMENT", None)
        adcSym_IntEnComment.setVisible(False)
        adcSym_IntEnComment.setLabel("Warning!!! "+adcInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
        adcSym_IntEnComment.setDependencies(updateADCInterruptWarningStatus, InterruptVectorUpdate)

    else:
        InterruptVector = adcInstanceName.getValue() + "_INTERRUPT_ENABLE"
        InterruptHandler = adcInstanceName.getValue() + "_INTERRUPT_HANDLER"
        InterruptHandlerLock = adcInstanceName.getValue()+ "_INTERRUPT_HANDLER_LOCK"
        InterruptVectorUpdate = adcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
        InterruptVectorSecurity = adcInstanceName.getValue() + "_SET_NON_SECURE"
        # Interrupt Dynamic settings
        adcSym_UpdateInterruptStatus = adcComponent.createBooleanSymbol("ADC_INTERRUPT_STATUS", None)
        adcSym_UpdateInterruptStatus.setDependencies(updateADCInterruptStatus, ["ADC_INTENSET_RESRDY","ADC_INTENSET_RESOVR","ADC_INTENSET_WCMP","ADC_INTENSET_SAMPRDY","ADC_INTENSET_SAMPOVR"])
        adcSym_UpdateInterruptStatus.setVisible(False)

        # Interrupt Warning status
        adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_INTERRUPT_ENABLE_COMMENT", None)
        adcSym_IntEnComment.setVisible(False)
        adcSym_IntEnComment.setLabel("Warning!!! "+adcInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
        adcSym_IntEnComment.setDependencies(updateADCInterruptWarningStatus, ["core." + InterruptVectorUpdate, "ADC_INTENSET_RESRDY", "ADC_INTENSET_RESOVR", "ADC_INTENSET_WCMP", "ADC_INTENSET_SAMPRDY", "ADC_INTENSET_SAMPOVR"])

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

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global ADCfilesArray
        adcIsNonSecure = Database.getSymbolValue("core", adcComponent.getID().upper() + "_IS_NON_SECURE")
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, adcIsNonSecure)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, adcIsNonSecure)

    adcSym_CommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcSym_CommonHeaderFile.setSourcePath("../peripheral/adc_06272/templates/plib_adc_common.h.ftl")
    adcSym_CommonHeaderFile.setOutputName("plib_adc_common.h")
    adcSym_CommonHeaderFile.setDestPath("/peripheral/adc/")
    adcSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_CommonHeaderFile.setType("HEADER")
    adcSym_CommonHeaderFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_CommonHeaderFile)
        if adcIsNonSecure == False:
            adcSym_CommonHeaderFile.setSecurity("SECURE")

    adcSym_HeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcSym_HeaderFile.setSourcePath("../peripheral/adc_06272/templates/plib_adc.h.ftl")
    adcSym_HeaderFile.setOutputName("plib_"+adcInstanceName.getValue().lower()+".h")
    adcSym_HeaderFile.setDestPath("/peripheral/adc/")
    adcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_HeaderFile.setType("HEADER")
    adcSym_HeaderFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_HeaderFile)
        if adcIsNonSecure == False:
            adcSym_HeaderFile.setSecurity("SECURE")

    adcSym_SourceFile = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSym_SourceFile.setSourcePath("../peripheral/adc_06272/templates/plib_adc.c.ftl")
    adcSym_SourceFile.setOutputName("plib_"+adcInstanceName.getValue().lower()+".c")
    adcSym_SourceFile.setDestPath("/peripheral/adc/")
    adcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_SourceFile.setType("SOURCE")
    adcSym_SourceFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_SourceFile)
        if adcIsNonSecure == False:
            adcSym_SourceFile.setSecurity("SECURE")

    adcSym_SystemInitFile = adcComponent.createFileSymbol("ADC_SYS_INIT", None)
    adcSym_SystemInitFile.setType("STRING")
    adcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSym_SystemInitFile.setSourcePath("../peripheral/adc_06272/templates/system/initialization.c.ftl")
    adcSym_SystemInitFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_SystemInitFile)
        if adcIsNonSecure == False:
            adcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")

    adcSym_SystemDefFile = adcComponent.createFileSymbol("ADC_SYS_DEF", None)
    adcSym_SystemDefFile.setType("STRING")
    adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSym_SystemDefFile.setSourcePath("../peripheral/adc_06272/templates/system/definitions.h.ftl")
    adcSym_SystemDefFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_SystemDefFile)
        adcSym_SystemDefFile.setDependencies(fileUpdate, ["core." + adcComponent.getID().upper() + "_IS_NON_SECURE"])
        if adcIsNonSecure == False:
            adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    adcComponent.addPlugin(
        "../../harmony-services/plugins/generic_plugin.jar",
        "ADC_UI_MANAGER_ID_adc_06272",
        {
            "plugin_name": "ADC Configuration",
            "main_html_path": "csp/plugins/configurators/adc-configurators/adc_06272/build/index.html",
            "componentId": adcComponent.getID()
        }
    )

