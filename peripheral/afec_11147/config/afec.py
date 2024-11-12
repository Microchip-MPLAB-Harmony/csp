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

global afecInstanceName

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
    Database.clearSymbolValue("core", afecInstanceName.getValue()+"_CLOCK_ENABLE")
    for channelID in range(0, 12):
        if (afecSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True):
        Database.setSymbolValue("core", afecInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    else:
        Database.setSymbolValue("core", afecInstanceName.getValue()+"_CLOCK_ENABLE", False, 2)

def afecinterruptControl(symbol, event):
    nvicSet = False
    interruptVector = afecInstanceName.getValue()+"_INTERRUPT_ENABLE"
    interruptHandler = afecInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = afecInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    for channelID in range(0, 12):
        if (afecSym_CH_IER_EOC[channelID].getValue() == True):
            nvicSet = True

    localComponent = symbol.getComponent()
    if localComponent.getSymbolValue("AFEC_IER_COMPE") == True:
        nvicSet = True

    if(nvicSet == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, afecInstanceName.getValue()+"_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, afecInstanceName.getValue()+"_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyClockStatus(symbol, event):
    clockSet = False
    clock = bool(Database.getSymbolValue("core", afecInstanceName.getValue()+"_CLOCK_ENABLE"))
    for channelID in range(0, 12):
        if (afecSym_CH_CHER[channelID].getValue() == True):
            clockSet = True
    if(clockSet == True and clock == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def dependencyIntStatus(symbol, event):
    nvicSet = False
    interruptVectorUpdate = afecInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"
    nvic = bool(Database.getSymbolValue("core", interruptVectorUpdate))
    for channelID in range(0, 12):
        if (afecSym_CH_IER_EOC[channelID].getValue() == True):
            nvicSet = True
    if(nvicSet == True and nvic == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def afecGetMasterClock():
    main_clk_freq = int(Database.getSymbolValue("core", afecInstanceName.getValue() + "_CLOCK_FREQUENCY"))
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

def afec_EMR_CMPSEL_Update(symbol, event):
    symbol.setVisible(event["value"] == False)

def afecTempModeVisibility(symbol, event):
    symbol.setVisible(event["value"])
###################################################################################################
########################### Dependency   #################################
###################################################################################################
global lastAdcModuleU, lastAdcChU
lastAdcChU = 0
global lastAdcModuleV, lastAdcChV
lastAdcChV = 6
global lastAdcModulePot, lastADCChPot
lastADCChPot = 10
global lastAdcModuleVdc, lastADCChVdc
lastADCChVdc = 7
lastAdcModuleU = lastAdcModuleV = lastAdcModulePot = lastAdcModuleVdc = 0

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
    global lastAdcModuleU,lastAdcChU
    global lastAdcModuleV, lastAdcChV
    global lastAdcModulePot, lastADCChPot
    global lastAdcModuleVdc, lastADCChVdc

    component = str(afecInstanceName.getValue()).lower()
    instanceNum = int(filter(str.isdigit,str(afecInstanceName.getValue())))
    if (int(lastAdcModuleU) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(lastAdcChU)+"_CHER", False)
        Database.setSymbolValue(component, "AFEC"+str((lastAdcChU))+"_IER_EOC", False)
    if (int(lastAdcModuleV) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(lastAdcChV)+"_CHER", False)
    if (int(lastAdcModulePot) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(lastADCChPot)+"_CHER", False)
    if (int(lastAdcModuleVdc) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(lastADCChVdc)+"_CHER", False)
    Database.setSymbolValue(component, "AFEC_CONV_MODE", 0)

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

    if args["enable"] == True:
        # Calculate prescaler and ADC sample counts based on requested conversion time
        if not(args["conversion_time"] == "default"):
            # ToDO: Place Holder. Add the code later
            pass

        # Calculate prescaler and ADC sample counts based on requested conversion time
        if not(args["reference"] == "default"):
            # ToDO: Placeholder. To be done later
            pass

        # Find the key index of the RESOLUTION
        count = afecSym_EMR_RES_VALUE.getKeyCount()
        resIndex = 0
        for i in range(0,count):
            if (str(args["resolution"]) in afecSym_EMR_RES_VALUE.getKeyDescription(i) ):
                resIndex = i
                break

        # Set resolution value
        Database.setSymbolValue(component, "AFEC_EMR_RES_VALUE", resIndex)

        if args["trigger"] != "SOFTWARE_TRIGGER":
            # Find the key index of the trigger as a PWM channel as per TRIGGER argument
            count = afecSym_MR_TRGSEL_VALUE.getKeyCount()
            triggerIndex = 0
            for i in range(0,count):
                if ("PWM" + str(args["trigger"]) in afecSym_MR_TRGSEL_VALUE.getKeyDescription(i) ):
                    triggerIndex = i
                    break

            Database.setSymbolValue(component, "AFEC_MR_TRGSEL_VALUE", triggerIndex)
            Database.setSymbolValue(component, "AFEC_CONV_MODE", 2)

        # Enable/ Disable end-of-conversion interrupt
        Database.setSymbolValue(component, "AFEC_"+ args["channel"] +"_IER_EOC", args["enable_eoc_interrupt"])

        # Enable/ Disable channel
        Database.setSymbolValue(component, "AFEC_"+ args["channel"] +"_CHER", True)

        # Enable DMA sequencing
        if not args["enable_dma_sequence"] == "default":
            # ToDO: Placeholder for later development
            pass

        if not args["result_alignment"] == "default":
            # ToDO: Placeholder for later development
            pass

    else:
        # Enable/ Disable end-of-conversion interrupt
        Database.setSymbolValue(component, "AFEC_"+ args["channel"] +"_IER_EOC", False)

        # Enable/ Disable channel
        Database.setSymbolValue(component, "AFEC_"+ args["channel"] +"_CHER", False)

def handleMessage(messageID, args):
    dict = {}

    if (messageID == "PMSM_FOC_ADC_CH_CONF"):
        component = str(afecInstanceName.getValue()).lower()
        instanceNum = int(filter(str.isdigit,str(afecInstanceName.getValue())))
        dict['ADC_MAX_CH'] = Database.getSymbolValue(component, "AFEC_NUM_CHANNELS")
        dict['ADC_MAX_MODULES'] = Database.getSymbolValue(component, "AFEC_NUM_MODULES")
        #Change ADC channels if they are changed in the PMSM_FOC
        resetChannelsForPMSMFOC()
        AdcConfigForPMSMFOC(component, instanceNum, args)

    elif ( messageID == "SET_ADC_CONFIG_PARAMS"):
        # Set ADC configuration parameters
        setAdcConfigParams( args )
    
    elif (messageID == "ADC_CONFIG_HW_IO"):
        # print("AFEC handleMessage: {} args: {}".format(messageID, args))
        component = str(afecInstanceName.getValue()).lower()
        channel, isNegInput, enable = args['config']

        res = Database.setSymbolValue(component, "AFEC_{}_CHER".format(channel), enable)
        if channel % 2 == 1 and isNegInput == True:
            res = Database.setSymbolValue(component, "AFEC_{}_NEG_INP".format(channel - 1), "AN{}".format(channel))
        
        if res == True:
            dict = {"Result": "Success"}
        else:
            dict = {"Result": "Fail"}


    return dict

# ADC configurations needed for PMSM_FOC component
def AdcConfigForPMSMFOC(component, instanceNum, args):
    global afecSym_MR_TRGSEL_VALUE

    global lastAdcModuleU, lastAdcChU
    global lastAdcModuleV, lastAdcChV
    global lastAdcModulePot, lastADCChPot
    global lastAdcModuleVdc, lastADCChVdc

    lastAdcModuleU = phUModule = args['PHASE_U']
    lastAdcChU = phUCh = args['PHASE_U_CH']
    lastAdcModuleV = phVModule = args['PHASE_V']
    lastAdcChV = phVCh = args['PHASE_V_CH']
    lastAdcModuleVdc = phDCBusModule = args['VDC']
    lastADCChVdc = phDCBusCh = args['VDC_CH']
    lastAdcModulePot = phPotModule = args['POT']
    lastADCChPot = phPotCh = args['POT_CH']
    resolution = args['RESOLUTION']
    trigger = args['TRIGGER']

    # Find the key index of the trigger as a PWM channel as per TRIGGER argument
    count = afecSym_MR_TRGSEL_VALUE.getKeyCount()
    triggerIndex = 0
    for i in range(0,count):
        if ("PWM"+str(trigger) in afecSym_MR_TRGSEL_VALUE.getKeyDescription(i) ):
            triggerIndex = i
            break

    #fine the key index of the RESOLUTION
    count = afecSym_EMR_RES_VALUE.getKeyCount()
    resIndex = 0
    for i in range(0,count):
        if (str(resolution) in afecSym_EMR_RES_VALUE.getKeyDescription(i) ):
            resIndex = i
            break

    # Enable ADC modules, Ph U interrupt
    if (int(phUModule) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(phUCh)+"_CHER", True)
        Database.setSymbolValue(component, "AFEC_"+str((phUCh))+"_IER_EOC", True)
        #dual sample and hold for ph U
        if (phUCh < (len(channel)/2)):
            Database.setSymbolValue(component, "AFEC_"+str(phUCh)+"_SHMR_DUAL", True)
        Database.setSymbolValue(component, "ADC_CH_PHASE_U", "AFEC_CH"+str(phUCh))
    if (int(phVModule) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(phVCh)+"_CHER", True)
        Database.setSymbolValue(component, "ADC_CH_PHASE_V", "AFEC_CH"+str(phVCh))
    if (int(phPotModule) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(phPotCh)+"_CHER", True)
        Database.setSymbolValue(component, "ADC_CH_POT", "AFEC_CH"+str(phPotCh))
    if (int(phDCBusModule) == instanceNum):
        Database.setSymbolValue(component, "AFEC_"+str(phDCBusCh)+"_CHER", True)
        Database.setSymbolValue(component, "ADC_CH_VDC_BUS", "AFEC_CH"+str(phDCBusCh))

    if (int(phUModule) == instanceNum):
        Database.setSymbolValue(component, "AFEC_CONV_MODE", 2) #HW trigger
        Database.setSymbolValue(component, "AFEC_MR_TRGSEL_VALUE", triggerIndex) #trigger as PWM Phase U
    Database.setSymbolValue(component, "AFEC_EMR_RES_VALUE", resIndex) #resolution

###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(afecComponent):
    global afecInstanceName
    global channel
    afecInstanceName = afecComponent.createStringSymbol("AFEC_INSTANCE_NAME", None)
    afecInstanceName.setVisible(False)
    afecInstanceName.setDefaultValue(afecComponent.getID().upper())

    Log.writeInfoMessage("Running " + afecInstanceName.getValue())


    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []      # array to save available pins
    channel = ["False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False", "False"] #array to save available channels
    afecChannelsValues = [] #array used for combo symbol
    afecChannelsValues.append("NONE")

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

    afec_signals = []
    afec = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]/instance@[name=\""+afecInstanceName.getValue()+"\"]/signals")
    afec_temperature_sensor_ch_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]/instance@[name=\"'+afecInstanceName.getValue()+'\"]/parameters/param@[name=\"TEMP_SENSOR_CH_NUM\"]')
    if afec_temperature_sensor_ch_node != None:
        afec_temp_sensor_ch = int(afec_temperature_sensor_ch_node.getAttribute("value"))
    else:
        afec_temp_sensor_ch = -1


    afec_signals = afec.getChildren()
    for pad in range(0, len(afec_signals)):
        group = afec_signals[pad].getAttribute("group")
        if (("AD" in group) and ("index" in afec_signals[pad].getAttributeList())):
            padSignal = afec_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel[int(afec_signals[pad].getAttribute("index"))] = "True"
                afecChannelsValues.append("CH"+afec_signals[pad].getAttribute("index"))

    if afec_temperature_sensor_ch_node != None:
        channel[afec_temp_sensor_ch] = "True"
        afecChannelsValues.append("CH"+afec_temperature_sensor_ch_node.getAttribute("value"))

    afecSym_AvailableChannels = afecComponent.createComboSymbol("AFEC_AVAILABLE_CHANNELS", None, channel)
    afecSym_AvailableChannels.setVisible(False)

    #----------------- motor control APIs ---------------------------------
    afecConvAPI = afecComponent.createStringSymbol("ADC_START_CONV_API", None)
    afecConvAPI.setVisible(False)
    afecConvAPI.setValue(afecInstanceName.getValue()+"_ConversionStart")

    afecResultAPI = afecComponent.createStringSymbol("ADC_GET_RESULT_API", None)
    afecResultAPI.setVisible(False)
    afecResultAPI.setValue(afecInstanceName.getValue()+"_ChannelResultGet")

    afecResultReadyAPI = afecComponent.createStringSymbol("ADC_IS_RESULT_READY_API", None)
    afecResultReadyAPI.setVisible(False)
    afecResultReadyAPI.setValue(afecInstanceName.getValue()+"_ChannelResultIsReady")

    afecCallbackAPI = afecComponent.createStringSymbol("ADC_CALLBACK_API", None)
    afecCallbackAPI.setVisible(False)
    afecCallbackAPI.setValue(afecInstanceName.getValue()+"_CallbackRegister")

    afecPhUCh = afecComponent.createStringSymbol("ADC_CH_PHASE_U", None)
    afecPhUCh.setVisible(False)
    afecPhUCh.setValue("AFEC_CH0")

    afecPhVCh = afecComponent.createStringSymbol("ADC_CH_PHASE_V", None)
    afecPhVCh.setVisible(False)
    afecPhVCh.setValue("AFEC_CH6")

    afecVdcCh = afecComponent.createStringSymbol("ADC_CH_VDC_BUS", None)
    afecVdcCh.setVisible(False)
    afecVdcCh.setValue("AFEC_CH7")

    afecPotCh = afecComponent.createStringSymbol("ADC_CH_POT", None)
    afecPotCh.setVisible(False)
    afecPotCh.setValue("AFEC_CH10")

    afecResultInt = afecComponent.createStringSymbol("INTERRUPT_ADC_RESULT", None)
    afecResultInt.setVisible(False)
    afecResultInt.setValue(afecInstanceName.getValue()+"_IRQn")

    afecMenu = afecComponent.createMenuSymbol("AFEC_MENU", None)
    afecMenu.setLabel("ADC Configuration")

    #max no of channels
    afecSym_NUM_CHANNELS = afecComponent.createIntegerSymbol("AFEC_NUM_CHANNELS", afecMenu)
    afecSym_NUM_CHANNELS.setDefaultValue(12)
    afecSym_NUM_CHANNELS.setVisible(False)

    #number of AFEC modules
    afecSym_NUM_MODULES = afecComponent.createIntegerSymbol("AFEC_NUM_MODULES", afecMenu)
    afecSym_NUM_MODULES.setVisible(False)
    afec = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]")
    afecSym_NUM_MODULES.setDefaultValue(len(afec.getChildren()))

    #Clock prescaler
    global afecSym_MR_PRESCAL
    afecSym_MR_PRESCAL = afecComponent.createIntegerSymbol("AFEC_MR_PRESCAL", afecMenu)
    afecSym_MR_PRESCAL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_MR")
    afecSym_MR_PRESCAL.setLabel("Select Prescaler")
    afecSym_MR_PRESCAL.setDefaultValue(7)
    afecSym_MR_PRESCAL.setMin(1)
    afecSym_MR_PRESCAL.setMax(255)

    #clock selection
    global afecSym_Clock
    afecSym_Clock = afecComponent.createIntegerSymbol("AFEC_CLK", afecMenu)
    afecSym_Clock.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
    afecSym_Clock.setLabel("Clock Frequency (Hz)")
    afecSym_Clock.setDefaultValue(18750000)
    afecSym_Clock.setVisible(True)
    afecSym_Clock.setReadOnly(True)
    afecSym_Clock.setDependencies(afecFreqCalc, ["AFEC_MR_PRESCAL", "core." + afecInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    afecSym_PRESCAL_WARNING = afecComponent.createCommentSymbol("AFEC_PRESCAL_WARNING", afecMenu)
    afecSym_PRESCAL_WARNING.setLabel("**** AFEC Frequency = 18750000 Hz. ****")
    afecSym_PRESCAL_WARNING.setVisible(False)
    afecSym_PRESCAL_WARNING.setDependencies(afecPrescalWarning, ["AFEC_MR_PRESCAL", "core." + afecInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Result resolution
    #Added keys here as combining two bit-fields EMR_STM and EMR_RES
    global afecSym_EMR_RES_VALUE
    afecSym_EMR_RES_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_RES_VALUE", afecMenu)
    afecSym_EMR_RES_VALUE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
    afecSym_EMR_RES_VALUE.setLabel("Result Resolution")
    afecSym_EMR_RES_VALUE.setDefaultValue(0)
    afecSym_EMR_RES_VALUE.setOutputMode("Value")
    afecSym_EMR_RES_VALUE.setDisplayMode("Description")
    afecSym_EMR_RES_VALUE.addKey("NO_AVERAGE", "0", "12-bit")
    afecSym_EMR_RES_VALUE.addKey("OSR4", "1", "13-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR4_", "2", "13-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR16", "3", "14-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR16_", "4", "14-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR64", "5", "15-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR64_", "6", "15-bit - multi trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR256", "7", "16-bit - single trigger averaging")
    afecSym_EMR_RES_VALUE.addKey("OSR256_", "8", "16-bit - multi trigger averaging")

    #Conversion time
    afecSym_CONV_TIME = afecComponent.createCommentSymbol("AFEC_CONV_TIME", afecMenu)
    afecSym_CONV_TIME.setLabel("**** Conversion Time is 1.0733 us ****")
    afecSym_CONV_TIME.setDependencies(afecCalcConversionTime, ["AFEC_MR_PRESCAL", "AFEC_EMR_RES_VALUE", "core." + afecInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Result sign
    afecSym_EMR_SIGNMODE_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_SIGNMODE_VALUE", afecMenu)
    afecSym_EMR_SIGNMODE_VALUE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_EMR")
    afecSym_EMR_SIGNMODE_VALUE.setLabel("Result Sign")
    afecSym_EMR_SIGNMODE_VALUE.setDefaultValue(0)
    afecSym_EMR_SIGNMODE_VALUE.setOutputMode("Key")
    afecSym_EMR_SIGNMODE_VALUE.setDisplayMode("Description")
    afecSym_EMR_SIGNMODE_VALUE.addKey("SE_UNSG_DF_SIGN", "0", "Single Ended: Unsigned, Differential: Signed")
    afecSym_EMR_SIGNMODE_VALUE.addKey("SE_SIGN_DF_UNSG", "1", "Single Ended: Signed, Differential: Unsigned")
    afecSym_EMR_SIGNMODE_VALUE.addKey("ALL_UNSIGNED", "2", "Single Ended: Unsigned, Differential: Unsigned")
    afecSym_EMR_SIGNMODE_VALUE.addKey("ALL_SIGNED", "3", "Single Ended: Signed, Differential: Signed")

    afecSym_CONV_MODE = afecComponent.createKeyValueSetSymbol("AFEC_CONV_MODE", afecMenu)
    afecSym_CONV_MODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_MR")
    afecSym_CONV_MODE.setLabel("Conversion Mode")
    afecSym_CONV_MODE.setDefaultValue(0)
    afecSym_CONV_MODE.setOutputMode("Value")
    afecSym_CONV_MODE.setDisplayMode("Description")
    afecSym_CONV_MODE.addKey("FREERUN", "0", "Free Run")
    afecSym_CONV_MODE.addKey("SW_TRIGGER", "1", "Software Trigger")
    afecSym_CONV_MODE.addKey("HW_TRIGGER", "2", "Hardware Trigger")

    #Trigger
    global afecSym_MR_TRGSEL_VALUE
    afecSym_MR_TRGSEL_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_MR_TRGSEL_VALUE", afecSym_CONV_MODE)
    afecSym_MR_TRGSEL_VALUE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_MR")
    afecSym_MR_TRGSEL_VALUE.setLabel("Select External Trigger Input")
    afecSym_MR_TRGSEL_VALUE.setVisible(False)
    afecSym_MR_TRGSEL_VALUE.setDefaultValue(1)
    afecSym_MR_TRGSEL_VALUE.setOutputMode("Key")
    afecSym_MR_TRGSEL_VALUE.setDisplayMode("Description")
    trigger_values = []
    afec = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AFEC\"]/instance@[name=\""+afecInstanceName.getValue()+"\"]/parameters")
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
    afecSym_MR_USEQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_MR")
    afecSym_MR_USEQ.setLabel("Enable User Sequence Mode")
    afecSym_MR_USEQ.setDefaultValue(False)

    for channelID in range(0, len(channel)):
        #channel selection for user sequence
        afecSym_SEQ1R_USCH.append(channelID)
        afecSym_SEQ1R_USCH[channelID] = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH"+str(channelID), afecSym_MR_USEQ, afecChannelsValues)
        afecSym_SEQ1R_USCH[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_SEQ1R")
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
        afecSym_CH_CHER[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
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
        afecSym_CH_NAME[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
        afecSym_CH_NAME[channelID].setLabel("Name")
        afecSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
        afecSym_CH_NAME[channelID].setVisible(False)
        afecSym_CH_NAME[channelID].setDependencies(afecCHNameVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel positive input
        afecSym_CH_PositiveInput.append(channelID)
        afecSym_CH_PositiveInput[channelID] = afecComponent.createStringSymbol("AFEC_"+str(channelID)+"_POS_INP", afecSym_CH_CHER[channelID])
        afecSym_CH_PositiveInput[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
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
            afecSym_CH_NegativeInput[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
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
            afecSym_CH_SHMR_DUAL[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
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
        afecSym_CH_CGR_GAIN[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
        afecSym_CH_CGR_GAIN[channelID].setLabel("Gain")
        afecSym_CH_CGR_GAIN[channelID].setDefaultValue("X1")
        afecSym_CH_CGR_GAIN[channelID].setVisible(False)
        afecSym_CH_CGR_GAIN[channelID].setDependencies(afecCHGainVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel offset
        afecSym_CH_COCR_AOFF.append(channelID)
        afecSym_CH_COCR_AOFF[channelID] = afecComponent.createIntegerSymbol("AFEC_"+str(channelID)+"_COCR_AOFF", afecSym_CH_CHER[channelID])
        afecSym_CH_COCR_AOFF[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_COCR")
        afecSym_CH_COCR_AOFF[channelID].setLabel("Offset")
        afecSym_CH_COCR_AOFF[channelID].setDefaultValue(512)
        afecSym_CH_COCR_AOFF[channelID].setVisible(False)
        afecSym_CH_COCR_AOFF[channelID].setMin(0)
        afecSym_CH_COCR_AOFF[channelID].setMax(1024)
        afecSym_CH_COCR_AOFF[channelID].setDependencies(afecCHOffsetVisible, ["AFEC_"+str(channelID)+"_CHER"])

        #Channel interrupt
        afecSym_CH_IER_EOC.append(channelID)
        afecSym_CH_IER_EOC[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_IER_EOC", afecSym_CH_CHER[channelID])
        afecSym_CH_IER_EOC[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
        afecSym_CH_IER_EOC[channelID].setLabel("End of conversion interrupt")
        afecSym_CH_IER_EOC[channelID].setDefaultValue(False)
        afecSym_CH_IER_EOC[channelID].setVisible(False)
        afecSym_CH_IER_EOC[channelID].setDependencies(afecCHInterruptVisible, ["AFEC_"+str(channelID)+"_CHER"])

        if afec_temp_sensor_ch == channelID:
            afecSym_CH_TEMPMR_RTCT = afecComponent.createBooleanSymbol("AFEC_TEMPMR_RTCT", afecSym_CH_CHER[channelID])
            afecSym_CH_TEMPMR_RTCT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_TEMPMR")
            afecSym_CH_TEMPMR_RTCT.setLabel("Enable Temperature Sensor Trigger by RTC event")
            afecSym_CH_TEMPMR_RTCT.setDefaultValue(False)
            afecSym_CH_TEMPMR_RTCT.setVisible(False)
            afecSym_CH_TEMPMR_RTCT.setDependencies(afecTempModeVisibility, ["AFEC_"+str(channelID)+"_CHER"])

            afecSym_CH_TEMP_CMP_MODE_EN = afecComponent.createBooleanSymbol("AFEC_TEMP_CMP_MODE_EN", afecSym_CH_CHER[channelID])
            afecSym_CH_TEMP_CMP_MODE_EN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:%NOREGISTER%")
            afecSym_CH_TEMP_CMP_MODE_EN.setLabel("Enable Temperature Comparision")
            afecSym_CH_TEMP_CMP_MODE_EN.setDefaultValue(False)
            afecSym_CH_TEMP_CMP_MODE_EN.setVisible(False)
            afecSym_CH_TEMP_CMP_MODE_EN.setDependencies(afecTempModeVisibility, ["AFEC_"+str(channelID)+"_CHER"])

            afec_tempmr_tempcmpmod_val = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AFEC\"]/value-group@[name=\"AFEC_TEMPMR__TEMPCMPMOD\"]")
            afec_tempmr_tempcmpmod_values = afec_tempmr_tempcmpmod_val.getChildren()

            afecSym_CH_TEMPMR_TEMPCMPMOD = afecComponent.createKeyValueSetSymbol("AFEC_TEMPMR_TEMPCMPMOD", afecSym_CH_TEMP_CMP_MODE_EN)
            afecSym_CH_TEMPMR_TEMPCMPMOD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_TEMPMR")
            afecSym_CH_TEMPMR_TEMPCMPMOD.setLabel("Temperature Comparision Mode")
            afecSym_CH_TEMPMR_TEMPCMPMOD.setOutputMode("Key")
            afecSym_CH_TEMPMR_TEMPCMPMOD.setDisplayMode("Description")
            afecSym_CH_TEMPMR_TEMPCMPMOD.setVisible(False)
            for j in range(0, len(afec_tempmr_tempcmpmod_values)):
                name = afec_tempmr_tempcmpmod_values[j].getAttribute("name")
                value = afec_tempmr_tempcmpmod_values[j].getAttribute("value")
                caption = afec_tempmr_tempcmpmod_values[j].getAttribute("caption")
                afecSym_CH_TEMPMR_TEMPCMPMOD.addKey(name, value, caption)
            afecSym_CH_TEMPMR_TEMPCMPMOD.setDependencies(afecTempModeVisibility, ["AFEC_TEMP_CMP_MODE_EN"])

            afecSym_CH_TEMPCWR_THIGHTHRES = afecComponent.createIntegerSymbol("AFEC_TEMPCWR_THIGHTHRES", afecSym_CH_TEMP_CMP_MODE_EN)
            afecSym_CH_TEMPCWR_THIGHTHRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_TEMPCWR")
            afecSym_CH_TEMPCWR_THIGHTHRES.setLabel("Temperature High Threshold")
            afecSym_CH_TEMPCWR_THIGHTHRES.setMin(0)
            afecSym_CH_TEMPCWR_THIGHTHRES.setMax(65535)
            afecSym_CH_TEMPCWR_THIGHTHRES.setDefaultValue(0)
            afecSym_CH_TEMPCWR_THIGHTHRES.setVisible(False)
            afecSym_CH_TEMPCWR_THIGHTHRES.setDependencies(afecTempModeVisibility, ["AFEC_TEMP_CMP_MODE_EN"])

            afecSym_CH_TEMPCWR_TLOWTHRES = afecComponent.createIntegerSymbol("AFEC_TEMPCWR_TLOWTHRES", afecSym_CH_TEMP_CMP_MODE_EN)
            afecSym_CH_TEMPCWR_TLOWTHRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_TEMPCWR")
            afecSym_CH_TEMPCWR_TLOWTHRES.setLabel("Temperature Low Threshold")
            afecSym_CH_TEMPCWR_TLOWTHRES.setMin(0)
            afecSym_CH_TEMPCWR_TLOWTHRES.setMax(65535)
            afecSym_CH_TEMPCWR_TLOWTHRES.setDefaultValue(0)
            afecSym_CH_TEMPCWR_TLOWTHRES.setVisible(False)
            afecSym_CH_TEMPCWR_TLOWTHRES.setDependencies(afecTempModeVisibility, ["AFEC_TEMP_CMP_MODE_EN"])

            afecSym_CH_IER_TEMPCHG = afecComponent.createBooleanSymbol("AFEC_IER_TEMPCHG", afecSym_CH_TEMP_CMP_MODE_EN)
            afecSym_CH_IER_TEMPCHG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_IER")
            afecSym_CH_IER_TEMPCHG.setLabel("Temperature Change Interrupt")
            afecSym_CH_IER_TEMPCHG.setDefaultValue(False)
            afecSym_CH_IER_TEMPCHG.setVisible(False)
            afecSym_CH_IER_TEMPCHG.setDependencies(afecTempModeVisibility, ["AFEC_TEMP_CMP_MODE_EN"])

    afecComparatorMenu = afecComponent.createMenuSymbol("AFEC_COMPARE_MENU", None)
    afecComparatorMenu.setLabel("Comparator Configuration")

    afecSym_EMR_CMPALL = afecComponent.createBooleanSymbol("AFEC_EMR_CMPALL", afecComparatorMenu)
    afecSym_EMR_CMPALL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_EMR")
    afecSym_EMR_CMPALL.setLabel("Compare all channels")
    afecSym_EMR_CMPALL.setDefaultValue(False)

    afecSym_EMR_CMPSEL = afecComponent.createKeyValueSetSymbol("AFEC_EMR_CMPSEL", afecComparatorMenu)
    afecSym_EMR_CMPSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_EMR")
    afecSym_EMR_CMPSEL.setLabel("Compare Channel")
    afecSym_EMR_CMPSEL.setOutputMode("Value")
    afecSym_EMR_CMPSEL.setDisplayMode("Description")
    for channelID in range(0, len(channel)):
        #Show channels as per available pins in package
        if (channel[channelID] == "True"):
            afecSym_EMR_CMPSEL.addKey("CHANNEL_" + str(channelID), str(channelID), "Channel " + str(channelID))

    afecSym_EMR_CMPSEL.setDependencies(afec_EMR_CMPSEL_Update, ["AFEC_EMR_CMPALL"])

    afecSym_CWR_HIGHTHRES = afecComponent.createIntegerSymbol("AFEC_CWR_HIGHTHRES", afecComparatorMenu)
    afecSym_CWR_HIGHTHRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_CWR")
    afecSym_CWR_HIGHTHRES.setLabel("High Threshold")
    afecSym_CWR_HIGHTHRES.setMin(0)
    afecSym_CWR_HIGHTHRES.setMax(65535)
    afecSym_CWR_HIGHTHRES.setDefaultValue(0)

    afecSym_CWR_LOWTHRES = afecComponent.createIntegerSymbol("AFEC_CWR_LOWTHRES", afecComparatorMenu)
    afecSym_CWR_LOWTHRES.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_CWR")
    afecSym_CWR_LOWTHRES.setLabel("Low Threshold")
    afecSym_CWR_LOWTHRES.setMin(0)
    afecSym_CWR_LOWTHRES.setMax(65535)
    afecSym_CWR_LOWTHRES.setDefaultValue(0)

    afecSym_EMR_CMPFILTER = afecComponent.createIntegerSymbol("AFEC_EMR_CMPFILTER", afecComparatorMenu)
    afecSym_EMR_CMPFILTER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_EMR")
    afecSym_EMR_CMPFILTER.setLabel("Compare Event Filter")
    afecSym_EMR_CMPFILTER.setDefaultValue(0)
    afecSym_EMR_CMPFILTER.setMin(0)
    afecSym_EMR_CMPFILTER.setMax(3)

    afecSym_EMR_CMPMODE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_CMPMODE", afecComparatorMenu)
    afecSym_EMR_CMPMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_EMR")
    afecSym_EMR_CMPMODE.setLabel("Compare Mode")
    afecSym_EMR_CMPMODE.setDefaultValue(0)
    afecSym_EMR_CMPMODE.setOutputMode("Key")
    afecSym_EMR_CMPMODE.setDisplayMode("Description")
    afecSym_EMR_CMPMODE.addKey("LOW", "0", "Generates an event when the converted data is lower than the low threshold of the window")
    afecSym_EMR_CMPMODE.addKey("HIGH", "1", "Generates an event when the converted data is higher than the high threshold of the window")
    afecSym_EMR_CMPMODE.addKey("IN", "2", "Generates an event when the converted data is in the comparison window")
    afecSym_EMR_CMPMODE.addKey("OUT", "3", "Generates an event when the converted data is out of the comparison window")

    afecSym_EMR_COMPE = afecComponent.createBooleanSymbol("AFEC_IER_COMPE", afecComparatorMenu)
    afecSym_EMR_COMPE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:afec_11147;register:AFEC_IER")
    afecSym_EMR_COMPE.setLabel("Enable Compare Interrupt")
    afecSym_EMR_COMPE.setDefaultValue(False)




    #--------------------------------------------------------------------------------------
    # Clock dynamic settings
    afecSym_ClockControl = afecComponent.createBooleanSymbol(afecInstanceName.getValue()+"_CLOCK_ENABLE", None)
    afecSym_ClockControl.setDependencies(afecClockControl, ["AFEC_0_CHER", "AFEC_1_CHER", "AFEC_2_CHER", "AFEC_3_CHER", "AFEC_4_CHER", \
        "AFEC_5_CHER", "AFEC_6_CHER", "AFEC_7_CHER", "AFEC_8_CHER", "AFEC_9_CHER", "AFEC_10_CHER", "AFEC_11_CHER"])
    afecSym_ClockControl.setVisible(False)

    # NVIC Dynamic settings
    afecSym_interruptControl = afecComponent.createBooleanSymbol("AFEC_NVIC_ENABLE", None)
    afecSym_interruptControl.setDependencies(afecinterruptControl, ["AFEC_0_IER_EOC", "AFEC_1_IER_EOC", "AFEC_2_IER_EOC", "AFEC_3_IER_EOC", "AFEC_4_IER_EOC",\
        "AFEC_5_IER_EOC", "AFEC_6_IER_EOC", "AFEC_7_IER_EOC", "AFEC_8_IER_EOC", "AFEC_9_IER_EOC", "AFEC_10_IER_EOC", "AFEC_11_IER_EOC", "AFEC_IER_COMPE"])
    afecSym_interruptControl.setVisible(False)

    # Dependency Status
    afecSym_ClkEnComment = afecComponent.createCommentSymbol("AFEC_CLK_ENABLE_COMMENT", None)
    afecSym_ClkEnComment.setVisible(False)
    afecSym_ClkEnComment.setLabel("Warning!!! "+afecInstanceName.getValue()+" Peripheral Clock is Disabled in Clock Manager")
    afecSym_ClkEnComment.setDependencies(dependencyClockStatus, ["core."+afecInstanceName.getValue()+"_CLOCK_ENABLE", "AFEC_0_CHER", "AFEC_1_CHER", "AFEC_2_CHER", "AFEC_3_CHER", "AFEC_4_CHER", \
        "AFEC_5_CHER", "AFEC_6_CHER", "AFEC_7_CHER", "AFEC_8_CHER", "AFEC_9_CHER", "AFEC_10_CHER", "AFEC_11_CHER"])
    interruptVectorUpdate = afecInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    afecSym_IntEnComment = afecComponent.createCommentSymbol("AFEC_NVIC_ENABLE_COMMENT", None)
    afecSym_IntEnComment.setVisible(False)
    afecSym_IntEnComment.setLabel("Warning!!! "+afecInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    afecSym_IntEnComment.setDependencies(dependencyIntStatus, ["core." + interruptVectorUpdate, "AFEC_0_IER_EOC", "AFEC_1_IER_EOC", "AFEC_2_IER_EOC", "AFEC_3_IER_EOC", "AFEC_4_IER_EOC",\
        "AFEC_5_IER_EOC", "AFEC_6_IER_EOC", "AFEC_7_IER_EOC", "AFEC_8_IER_EOC", "AFEC_9_IER_EOC", "AFEC_10_IER_EOC", "AFEC_11_IER_EOC", "AFEC_IER_COMPE"])

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    afec = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AFEC\"]")
    afecID = afec.getAttribute("id")

    afecHeaderFile = afecComponent.createFileSymbol("AFEC_HEADER", None)
    afecHeaderFile.setSourcePath("../peripheral/afec_11147/templates/plib_afec.h.ftl")
    afecHeaderFile.setOutputName("plib_"+afecInstanceName.getValue().lower() + ".h")
    afecHeaderFile.setDestPath("peripheral/afec/")
    afecHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecHeaderFile.setType("HEADER")
    afecHeaderFile.setMarkup(True)

    afecGlobalHeaderFile = afecComponent.createFileSymbol("AFEC_GLOBALHEADER", None)
    afecGlobalHeaderFile.setSourcePath("../peripheral/afec_11147/templates/plib_afec_common.h")
    afecGlobalHeaderFile.setOutputName("plib_afec_common.h")
    afecGlobalHeaderFile.setDestPath("peripheral/afec/")
    afecGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecGlobalHeaderFile.setType("HEADER")

    afecSource1File = afecComponent.createFileSymbol("AFEC_SOURCE", None)
    afecSource1File.setSourcePath("../peripheral/afec_11147/templates/plib_afec.c.ftl")
    afecSource1File.setOutputName("plib_"+afecInstanceName.getValue().lower()+".c")
    afecSource1File.setDestPath("peripheral/afec/")
    afecSource1File.setProjectPath("config/" + configName +"/peripheral/afec/")
    afecSource1File.setType("SOURCE")
    afecSource1File.setMarkup(True)

    afecSystemInitFile = afecComponent.createFileSymbol("AFEC_INIT", None)
    afecSystemInitFile.setType("STRING")
    afecSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    afecSystemInitFile.setSourcePath("../peripheral/afec_11147/templates/system/initialization.c.ftl")
    afecSystemInitFile.setMarkup(True)

    afecSystemDefFile = afecComponent.createFileSymbol("AFEC_DEF", None)
    afecSystemDefFile.setType("STRING")
    afecSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    afecSystemDefFile.setSourcePath("../peripheral/afec_11147/templates/system/definitions.h.ftl")
    afecSystemDefFile.setMarkup(True)

    afecComponent.addPlugin("../peripheral/afec_11147/plugin/afec_11147.jar")
