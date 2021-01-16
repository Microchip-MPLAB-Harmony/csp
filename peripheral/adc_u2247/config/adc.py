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
    else:
        if adcSym_INTENSET_RESRDY.getValue() == True or adcSym_INTENSET_WINMON.getValue() == True:
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
    else:
        if adcSym_INTENSET_RESRDY.getValue() == True or adcSym_INTENSET_WINMON.getValue() == True:
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
    if (adcSym_CTRLA_SLAVEEN.getValue() == False):
        prescaler = adcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    else:
        component = int(adcInstanceName.getValue()[-1]) - 1
        prescaler = (Database.getSymbolValue("adc" + str(component), "ADC_CTRLB_PRESCALER"))
        prescaler = math.pow(2, prescaler+1)
    sample_cycles = adcSym_SAMPCTRL_SAMPLEN.getValue()
    data_width = adcSym_CTRLC_RESSEL.getSelectedKey()[:-3]
    conv_time = float((int(sample_cycles) + int(data_width)) * int(prescaler) * 1000000.0) / clock_freq
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
    resolution = component.getSymbolValue("ADC_CTRLC_RESSEL")
    bit = component.getSymbolValue("ADC_RES_BIT")
    if (resolution == 1 and bit == "Accumulation/Averaging"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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
    resolution = component.getSymbolValue("ADC_CTRLC_RESSEL")
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

    if (event["id"] == "ADC_REFCTRL_REFSEL"):
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


def handleMessage(messageID, args):
    dict = {}

    if (messageID == "PMSM_FOC_ADC_CH_CONF"):
        component = str(adcInstanceName.getValue()).lower()
        instanceNum = int(filter(str.isdigit,str(adcInstanceName.getValue())))
        dict['ADC_MAX_CH'] = Database.getSymbolValue(component, "ADC_MAX_CHANNELS")
        dict['ADC_MAX_MODULES'] = Database.getSymbolValue(component, "ADC_NUM_MODULES")
        #Change ADC channels if they are changed in the PMSM_FOC
        resetChannelsForPMSMFOC()
        AdcConfigForPMSMFOC(component, instanceNum, args)

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
    adcPhUCh.setValue("ADC_POSINPUT_AIN2")

    adcPhVCh = adcComponent.createStringSymbol("ADC_CH_PHASE_V", None)
    adcPhVCh.setVisible(False)
    adcPhVCh.setValue("ADC_POSINPUT_AIN5")

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


    # slave mode
    global adcSym_CTRLA_SLAVEEN
    adcSym_CTRLA_SLAVEEN = adcComponent.createBooleanSymbol("ADC_CTRLA_SLAVEEN", None)
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

    for index in range(0, len(param_values)):
        if "LOAD_CALIB" in param_values[index].getAttribute("name"):
            adcSym_CALIB = adcComponent.createBooleanSymbol("ADC_LOAD_CALIB", None)
            adcSym_CALIB.setVisible(False)
            adcSym_CALIB.setDefaultValue(True)

            # NVM register
            adcSym_calib_reg = adcComponent.createStringSymbol("ADC_NVM_CALIB_REG", None)
            adcSym_calib_reg.setVisible(False)
            reg = ""
            node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"OTP5_FUSES\"]")
            if node != None:
                reg = "OTP5_ADDR"
            else:
                node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group@[name=\"SW_CALIB_FUSES\"]")
                if node != None:
                    reg = "SW_CALIB_ADDR"
            adcSym_calib_reg.setDefaultValue(reg)
            

    # prescaler configuration
    global adcSym_CTRLB_PRESCALER
    adcSym_CTRLB_PRESCALER = adcComponent.createKeyValueSetSymbol("ADC_CTRLB_PRESCALER", None)
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
    global adcSym_SAMPCTRL_SAMPLEN
    adcSym_SAMPCTRL_SAMPLEN = adcComponent.createIntegerSymbol("ADC_SAMPCTRL_SAMPLEN", None)
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

    # Sampling time calculation
    adcSym_SAMPCTRL_SAMPLEN_TIME = adcComponent.createCommentSymbol("ADC_SAMPCTRL_SAMPLEN_TIME", None)
    adcSym_SAMPCTRL_SAMPLEN_TIME.setLabel("**** Conversion Time is " + str(conv_time) + " us ****")
    # Dependency registration is done after all dependencies are defined.

    # reference selection
    adcSym_REFCTRL_REFSEL = adcComponent.createKeyValueSetSymbol("ADC_REFCTRL_REFSEL", None)
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
        adcSym_REFCTRL_REFSEL.addKey(adcReferenceValues[index].getAttribute("name"), adcReferenceValues[index].getAttribute("value"),
        adcReferenceValues[index].getAttribute("caption"))
    adcSym_REFCTRL_REFSEL.setDefaultValue(default)

    # trigger
    global adcSym_CONV_TRIGGER
    adcSym_CONV_TRIGGER = adcComponent.createComboSymbol("ADC_CONV_TRIGGER", None, ["Free Run", "SW Trigger", "HW Event Trigger"])
    adcSym_CONV_TRIGGER.setDefaultValue("Free Run")
    adcSym_CONV_TRIGGER.setLabel("Select Conversion Trigger")
    adcSym_CONV_TRIGGER.setDependencies(adcSlaveModeVisibility, ["ADC_CTRLA_SLAVEEN"])

    adcSym_FLUSH_EVENT = adcComponent.createKeyValueSetSymbol("ADC_EVCTRL_FLUSH", adcSym_CONV_TRIGGER)
    adcSym_FLUSH_EVENT.setLabel("Flush Event Input")
    adcSym_FLUSH_EVENT.setVisible(False)
    adcSym_FLUSH_EVENT.setOutputMode("Value")
    adcSym_FLUSH_EVENT.setDisplayMode("Description")
    adcSym_FLUSH_EVENT.addKey("DISABLED", "0", "Disabled")
    adcSym_FLUSH_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    adcSym_FLUSH_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    adcSym_FLUSH_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    adcSym_START_EVENT = adcComponent.createKeyValueSetSymbol("ADC_EVCTRL_START", adcSym_CONV_TRIGGER)
    adcSym_START_EVENT.setLabel("Start Event Input")
    adcSym_START_EVENT.setVisible(False)
    adcSym_START_EVENT.setOutputMode("Value")
    adcSym_START_EVENT.setDisplayMode("Description")
    adcSym_START_EVENT.addKey("DISABLED", "0", "Disabled")
    adcSym_START_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    adcSym_START_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    adcSym_START_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    # Auto sequence menu
    adcSequenceMenu = adcComponent.createMenuSymbol("ADC_SEQUENCE_MENU", None)
    adcSequenceMenu.setLabel("Automatic Sequence Configuration")
    adcSequenceMenu.setVisible(False)
    adcSequenceMenu.setDependencies(adcOptionVisible, ["ADC_CONV_TRIGGER"])

    global adcSym_SEQ_ENABLE
    adcSym_SEQ_ENABLE = adcComponent.createBooleanSymbol("ADC_SEQ_ENABLE", adcSequenceMenu)
    adcSym_SEQ_ENABLE.setLabel("Enable Automatic Sequencing")

    adcPositiveInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXPOS\"]")
    adcPositiveInputValues = []
    adcPositiveInputValues = adcPositiveInputNode.getChildren()
    for index in range(0, len(adcPositiveInputValues)):
        value = int(adcPositiveInputValues[index].getAttribute("value"), 16)
        adcSym_SEQCTRL_SEQ = adcComponent.createBooleanSymbol("ADC_SEQCTRL_SEQ"+str(value), adcSym_SEQ_ENABLE)
        adcSym_SEQCTRL_SEQ.setLabel("Enable "+ str(adcPositiveInputValues[index].getAttribute("caption")))
        if "AIN" in adcPositiveInputValues[index].getAttribute("name"):
            if adcPositiveInputValues[index].getAttribute("name") in channel:
                adcSym_SEQCTRL_SEQ.setVisible(True)
            else:
                adcSym_SEQCTRL_SEQ.setVisible(False)

    adcSym_NUM_CHANNELS = adcComponent.createIntegerSymbol("ADC_NUM_CHANNELS", None)
    adcSym_NUM_CHANNELS.setVisible(False)
    adcSym_NUM_CHANNELS.setDefaultValue(value)

    adcChannelMenu = adcComponent.createMenuSymbol("ADC_CHANNEL_MENU", None)
    adcChannelMenu.setLabel("Channel Configuration")

    adcSym_CTRLC_DIFFMODE = adcComponent.createBooleanSymbol("ADC_CTRLC_DIFFMODE", adcChannelMenu)
    adcSym_CTRLC_DIFFMODE.setLabel("Enable Differential Mode")
    adcSym_CTRLC_DIFFMODE.setDefaultValue(False)

    # positive input
    adcSym_INPUTCTRL_MUXPOS = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXPOS", adcChannelMenu)
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
    adcSym_INPUTCTRL_MUXPOS.setDependencies(adcPosInpVisible, ["ADC_CONV_TRIGGER", "ADC_SEQ_ENABLE"])

    # negative input
    adcSym_INPUTCTRL_MUXNEG = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXNEG", adcChannelMenu)
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
    adcSym_INPUTCTRL_MUXNEG.setDependencies(adcMuxNegVisibility, ["ADC_CTRLC_DIFFMODE"])

    adcResultMenu = adcComponent.createMenuSymbol("ADC_RESULT_MENU", None)
    adcResultMenu.setLabel("Result Configuration")

    # resolution configuration
    global adcSym_CTRLC_RESSEL
    adcSym_CTRLC_RESSEL = adcComponent.createKeyValueSetSymbol("ADC_CTRLC_RESSEL", adcResultMenu)
    adcSym_CTRLC_RESSEL.setLabel("Select Result Resolution")
    adcSym_CTRLC_RESSEL.setDefaultValue(0)
    adcSym_CTRLC_RESSEL.setOutputMode("Key")
    adcSym_CTRLC_RESSEL.setDisplayMode("Description")
    adcResultResolutionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLC__RESSEL\"]")
    adcResultResolutionValues = []
    adcResultResolutionValues = adcResultResolutionNode.getChildren()
    for index in range (0 , len(adcResultResolutionValues)):
        adcSym_CTRLC_RESSEL.addKey(adcResultResolutionValues[index].getAttribute("name"), adcResultResolutionValues[index].getAttribute("value"),
        adcResultResolutionValues[index].getAttribute("caption"))


    adcBits = ["13 Bit", "14 Bit", "15 Bit", "16 Bit", "Accumulation/Averaging"]
    adcSym_RES_BIT = adcComponent.createComboSymbol("ADC_RES_BIT", adcSym_CTRLC_RESSEL, adcBits)
    adcSym_RES_BIT.setLabel("Number of Bits")
    adcSym_RES_BIT.setVisible(False)
    adcSym_RES_BIT.setDependencies(adcResultBitVisibility, ["ADC_CTRLC_RESSEL"])

    # Averaging
    adcSym_AVGCTRL_SAMPLENUM = adcComponent.createKeyValueSetSymbol("ADC_AVGCTRL_SAMPLENUM", adcSym_RES_BIT)
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
    adcSym_AVGCTRL_SAMPLENUM.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT"])

    # division coefficient
    adcSym_AVGCTRL_ADJRES = adcComponent.createIntegerSymbol("ADC_AVGCTRL_ADJRES", adcSym_RES_BIT)
    adcSym_AVGCTRL_ADJRES.setLabel("Number of Right Shifts")
    adcSym_AVGCTRL_ADJRES.setMin(0)
    adcSym_AVGCTRL_ADJRES.setMax(7)
    adcSym_AVGCTRL_ADJRES.setDefaultValue(0)
    adcSym_AVGCTRL_ADJRES.setVisible(False)
    adcSym_AVGCTRL_ADJRES.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT"])

    adcSym_ADJRES = adcComponent.createIntegerSymbol("ADC_ADJRES", adcSym_RES_BIT)
    adcSym_ADJRES.setVisible(False)
    adcSym_ADJRES.setDependencies(adcADJRESCalc, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_ADJRES"])

    adcSym_SAMPLENUM = adcComponent.createIntegerSymbol("ADC_SAMPLENUM", adcSym_RES_BIT)
    adcSym_SAMPLENUM.setVisible(False)
    adcSym_SAMPLENUM.setDependencies(adcSAMPLENUMCalc, ["ADC_CTRLC_RESSEL", "ADC_RES_BIT", "ADC_AVGCTRL_SAMPLENUM"])

    # left adjusted mode
    adcSym_CTRLC_LEFTADJ = adcComponent.createBooleanSymbol("ADC_CTRLC_LEFTADJ", adcResultMenu)
    adcSym_CTRLC_LEFTADJ.setLabel("Left Aligned Result")
    adcSym_CTRLC_LEFTADJ.setVisible(True)

    # interrupt mode
    global adcSym_INTENSET_RESRDY
    adcSym_INTENSET_RESRDY = adcComponent.createBooleanSymbol("ADC_INTENSET_RESRDY", adcResultMenu)
    adcSym_INTENSET_RESRDY.setLabel("Enable Result Ready Interrupt")

    # event out mode
    adcSym_EVCTRL_RSERDYEO = adcComponent.createBooleanSymbol("ADC_EVCTRL_RESRDYEO", adcResultMenu)
    adcSym_EVCTRL_RSERDYEO.setLabel("Enable Result Ready Event Out")

    adcWindowMenu = adcComponent.createMenuSymbol("ADC_WINDOW_CONFIG_MENU", None)
    adcWindowMenu.setLabel("Window Mode Configuration")

    # Configure mode for Window operation
    adcSym_CTRLC_WINMODE = adcComponent.createKeyValueSetSymbol("ADC_CTRLC_WINMODE", adcWindowMenu)
    adcSym_CTRLC_WINMODE.setLabel("Select Window Monitor Mode")
    adcSym_CTRLC_WINMODE.setDefaultValue(0)
    adcSym_CTRLC_WINMODE.setOutputMode("Value")
    adcSym_CTRLC_WINMODE.setDisplayMode("Description")
    adcWindowConfigNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLC__WINMODE\"]")
    adcWindowConfigValues = []
    adcWindowConfigValues = adcWindowConfigNode.getChildren()
    for index in range (0 , len(adcWindowConfigValues)):
        adcSym_CTRLC_WINMODE.addKey(adcWindowConfigValues[index].getAttribute("name"), adcWindowConfigValues[index].getAttribute("value"),
        adcWindowConfigValues[index].getAttribute("caption"))

    # Window upper threshold
    adcSym_WINUT = adcComponent.createIntegerSymbol("ADC_WINUT", adcWindowMenu)
    adcSym_WINUT.setLabel("Window Upper Threshold")
    adcSym_WINUT.setMin(-32768)
    adcSym_WINUT.setMax(32767)
    adcSym_WINUT.setDefaultValue(1024)
    adcSym_WINUT.setVisible(False)
    adcSym_WINUT.setDependencies(adcWindowVisible, ["ADC_CTRLC_WINMODE"])

    # Window lower threshold
    adcSym_WINLT = adcComponent.createIntegerSymbol("ADC_WINLT", adcWindowMenu)
    adcSym_WINLT.setLabel("Window Lower Threshold")
    adcSym_WINLT.setMin(-32768)
    adcSym_WINLT.setMax(32767)
    adcSym_WINLT.setDefaultValue(512)
    adcSym_WINLT.setVisible(False)
    adcSym_WINLT.setDependencies(adcWindowVisible, ["ADC_CTRLC_WINMODE"])

    global adcSym_INTENSET_WINMON
    adcSym_INTENSET_WINMON = adcComponent.createBooleanSymbol("ADC_INTENSET_WINMON", adcWindowMenu)
    adcSym_INTENSET_WINMON.setLabel("Enable Window Monitor Interrupt")
    adcSym_INTENSET_WINMON.setDefaultValue(False)
    adcSym_INTENSET_WINMON.setVisible(False)
    adcSym_INTENSET_WINMON.setDependencies(adcWindowVisible, ["ADC_CTRLC_WINMODE"])

    # Enable Window Monitor Event Out
    adcSym_HW_INP_EVENT = adcComponent.createBooleanSymbol("ADC_WINDOW_OUTPUT_EVENT", adcWindowMenu)
    adcSym_HW_INP_EVENT.setLabel("Enable Window Monitor Event Out")
    adcSym_HW_INP_EVENT.setVisible(False)
    adcSym_HW_INP_EVENT.setDependencies(adcWindowVisible, ["ADC_CTRLC_WINMODE"])

    adcSym_SAMPCTRL_SAMPLEN_TIME.setDependencies(adcCalcSampleTime, ["core."+adcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "adc"+str(component)+".ADC_CTRLB_PRESCALER", "ADC_SAMPCTRL_SAMPLEN", "ADC_CTRLB_PRESCALER", "ADC_CTRLC_RESSEL", "ADC_CTRLA_SLAVEEN"])

    adcSleepMenu = adcComponent.createMenuSymbol("ADC_SLEEP_MENU", None)
    adcSleepMenu.setLabel("Sleep Mode Configuration")

    # run in standby mode
    adcSym_CTRLA_RUNSTDBY = adcComponent.createBooleanSymbol("ADC_CTRLA_RUNSTDBY", adcSleepMenu)
    adcSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")
    adcSym_CTRLA_RUNSTDBY.setVisible(True)

    # run in on demand control mode
    adcSym_CTRLA_ONDEMAND = adcComponent.createBooleanSymbol("ADC_CTRLA_ONDEMAND", adcSleepMenu)
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
        adcSym_UpdateInterruptStatus.setDependencies(updateADCInterruptStatus, ["ADC_INTENSET_RESRDY", "ADC_INTENSET_WINMON"])
        adcSym_UpdateInterruptStatus.setVisible(False)

        InterruptVectorUpdate.append("ADC_INTENSET_RESRDY")
        InterruptVectorUpdate.append("ADC_INTENSET_WINMON")

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
        adcSym_UpdateInterruptStatus.setDependencies(updateADCInterruptStatus, ["ADC_INTENSET_RESRDY", "ADC_INTENSET_WINMON"])
        adcSym_UpdateInterruptStatus.setVisible(False)

        # Interrupt Warning status
        adcSym_IntEnComment = adcComponent.createCommentSymbol("ADC_INTERRUPT_ENABLE_COMMENT", None)
        adcSym_IntEnComment.setVisible(False)
        adcSym_IntEnComment.setLabel("Warning!!! "+adcInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
        adcSym_IntEnComment.setDependencies(updateADCInterruptWarningStatus, ["core." + InterruptVectorUpdate, "ADC_INTENSET_RESRDY", "ADC_INTENSET_WINMON"])

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
    adcSym_CommonHeaderFile.setSourcePath("../peripheral/adc_u2247/templates/plib_adc_common.h.ftl")
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
    adcSym_HeaderFile.setSourcePath("../peripheral/adc_u2247/templates/plib_adc.h.ftl")
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
    adcSym_SourceFile.setSourcePath("../peripheral/adc_u2247/templates/plib_adc.c.ftl")
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
    adcSym_SystemInitFile.setSourcePath("../peripheral/adc_u2247/templates/system/initialization.c.ftl")
    adcSym_SystemInitFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_SystemInitFile)
        if adcIsNonSecure == False:
            adcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")

    adcSym_SystemDefFile = adcComponent.createFileSymbol("ADC_SYS_DEF", None)
    adcSym_SystemDefFile.setType("STRING")
    adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSym_SystemDefFile.setSourcePath("../peripheral/adc_u2247/templates/system/definitions.h.ftl")
    adcSym_SystemDefFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ADCfilesArray.append(adcSym_SystemDefFile)
        adcSym_SystemDefFile.setDependencies(fileUpdate, ["core." + adcComponent.getID().upper() + "_IS_NON_SECURE"])
        if adcIsNonSecure == False:
            adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    # load ADC manager
    adcComponent.addPlugin("../peripheral/adc_u2247/plugin/adc_u2247.jar")
