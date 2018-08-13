###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def adcNegativeInput(symbol, event):
    if (event["value"] == True):
        symbol.setReadOnly(False)
    else:
        symbol.setReadOnly(True)

def adcResultConfVisibility(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "16BIT"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(adcComponent):

    adcInstanceIndex = adcComponent.getID()[-1:]
    Log.writeInfoMessage("Running ADC" + str(adcInstanceIndex))

    #index
    adcSym_Index = adcComponent.createIntegerSymbol("ADC_INDEX", None)
    adcSym_Index.setDefaultValue(int(adcInstanceIndex))
    adcSym_Index.setVisible(False)

    #------------------------- ATDF Read -------------------------------------
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
    adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC"+str(adcInstanceIndex)+"\"]/signals")
    adc_signals = adc.getChildren()
    for pad in range(0, len(adc_signals)):
        group = adc_signals[pad].getAttribute("group")
        if (("AIN" in group) and ("index" in adc_signals[pad].getAttributeList())):
            padSignal = adc_signals[pad].getAttribute("pad")
            if padSignal in availablePins:
                channel.append(adc_signals[pad].getAttribute("group")+adc_signals[pad].getAttribute("index"))

    #slave mode
    global adcSym_CTRLA_SLAVEEN
    adcSym_CTRLA_SLAVEEN = adcComponent.createBooleanSymbol("ADC_CTRLA_SLAVEEN", None)
    adcSym_CTRLA_SLAVEEN.setLabel("Enable Slave")
    adcSym_CTRLA_SLAVEEN.setDefaultValue(False)
    mode = "0"
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADC\"]/instance@[name=\"ADC"+str(adcInstanceIndex)+"\"]/parameters")
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
    adcSym_CTRLB_PRESCALER = adcComponent.createKeyValueSetSymbol("ADC_CTRLB_PRESCALER", None)
    adcSym_CTRLB_PRESCALER.setLabel("Select Prescaler")
    adcSym_CTRLB_PRESCALER.setDefaultValue(0)
    adcSym_CTRLB_PRESCALER.setOutputMode("Key")
    adcSym_CTRLB_PRESCALER.setDisplayMode("Description")
    adcPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_CTRLB__PRESCALER\"]")
    adcPrescalerValues = []
    adcPrescalerValues = adcPrescalerNode.getChildren()
    for index in range(0, len(adcPrescalerValues)):
        adcSym_CTRLB_PRESCALER.addKey(adcPrescalerValues[index].getAttribute("name"), adcPrescalerValues[index].getAttribute("value"), adcPrescalerValues[index].getAttribute("caption"))
    adcSym_CTRLB_PRESCALER.setDependencies(adcSlaveModeVisibility, ["ADC_CTRLA_SLAVEEN"])

    #sampling time
    adcSym_SAMPCTRL_SAMPLEN = adcComponent.createIntegerSymbol("ADC_SAMPCTRL_SAMPLEN", None)
    adcSym_SAMPCTRL_SAMPLEN.setLabel("Select Sample Length (cycles)")
    adcSym_SAMPCTRL_SAMPLEN.setMin(0)
    adcSym_SAMPCTRL_SAMPLEN.setMax(63)
    adcSym_SAMPCTRL_SAMPLEN.setDefaultValue(0)

    #Sampling time calculation
    adcSym_SAMPCTRL_SAMPLEN_TIME = adcComponent.createCommentSymbol("ADC_SAMPCTRL_SAMPLEN_TIME", None)
    adcSym_SAMPCTRL_SAMPLEN_TIME.setLabel("**** Sampling Time is 0.04166 us ****")
    #adcSym_SAMPCTRL_SAMPLEN_TIME.setDependencies(adcCalcSampleTime, ["ADC_SAMPCTRL_SAMPLEN", "ADC_CTRLB_PRESCALER"])

    #reference selection
    adcSym_REFCTRL_REFSEL = adcComponent.createKeyValueSetSymbol("ADC_REFCTRL_REFSEL", None)
    adcSym_REFCTRL_REFSEL.setLabel("Select Reference")
    adcSym_REFCTRL_REFSEL.setDefaultValue(0)
    adcSym_REFCTRL_REFSEL.setOutputMode("Key")
    adcSym_REFCTRL_REFSEL.setDisplayMode("Description")
    adcReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_REFCTRL__REFSEL\"]")
    adcReferenceValues = []
    adcReferenceValues = adcReferenceNode.getChildren()
    for index in range(0, len(adcReferenceValues)):
        adcSym_REFCTRL_REFSEL.addKey(adcReferenceValues[index].getAttribute("name"), adcReferenceValues[index].getAttribute("value"),
        adcReferenceValues[index].getAttribute("caption"))

    #trigger
    global adcSym_CONV_TRIGGER
    adcSym_CONV_TRIGGER = adcComponent.createComboSymbol("ADC_CONV_TRIGGER", None, ["SW Trigger", "HW Event Trigger", "Free Run"])
    adcSym_CONV_TRIGGER.setDefaultValue("SW Trigger")
    adcSym_CONV_TRIGGER.setLabel("Select Conversion Trigger")

    #input event
    adcSym_HW_INP_EVENT = adcComponent.createCommentSymbol("ADC_HW_INP_EVENT", adcSym_CONV_TRIGGER)
    adcSym_HW_INP_EVENT.setLabel("**** Flush Input Event is Enabled ****")
    adcSym_HW_INP_EVENT.setVisible(False)
    adcSym_HW_INP_EVENT.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    #Invert Sync input event
    adcSym_EVCTRL_FLUSHINV = adcComponent.createBooleanSymbol("ADC_EVCTRL_FLUSHINV", adcSym_CONV_TRIGGER)
    adcSym_EVCTRL_FLUSHINV.setLabel("Invert Flush Event")
    adcSym_EVCTRL_FLUSHINV.setDefaultValue(False)
    adcSym_EVCTRL_FLUSHINV.setVisible(False)
    adcSym_EVCTRL_FLUSHINV.setDependencies(adcEventInputVisibility, ["ADC_CONV_TRIGGER", "ADC_CTRLA_SLAVEEN"])

    adcChannelMenu = adcComponent.createMenuSymbol("ADC_CHANNEL_MENU", None)
    adcChannelMenu.setLabel("Channel Configuration")

    #positive input
    adcSym_INPUTCTRL_MUXPOS = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXPOS", adcChannelMenu)
    adcSym_INPUTCTRL_MUXPOS.setLabel("Select Positive Input")
    adcSym_INPUTCTRL_MUXPOS.setDefaultValue(0)
    adcSym_INPUTCTRL_MUXPOS.setOutputMode("Key")
    adcSym_INPUTCTRL_MUXPOS.setDisplayMode("Description")
    adcPositiveInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXPOS\"]")
    adcPositiveInputValues = []
    adcPositiveInputValues = adcPositiveInputNode.getChildren()
    for index in range(0, len(adcPositiveInputValues)):
        if "AIN" in adcPositiveInputValues[index].getAttribute("name"):
            if adcPositiveInputValues[index].getAttribute("name") in channel:
                adcSym_INPUTCTRL_MUXPOS.addKey(adcPositiveInputValues[index].getAttribute("name"), adcPositiveInputValues[index].getAttribute("value"),
                adcPositiveInputValues[index].getAttribute("caption"))
        else:
            adcSym_INPUTCTRL_MUXPOS.addKey(adcPositiveInputValues[index].getAttribute("name"), adcPositiveInputValues[index].getAttribute("value"),
            adcPositiveInputValues[index].getAttribute("caption"))

    #differential mode
    adcSym_CTRLC_DIFFMODE = adcComponent.createBooleanSymbol("ADC_CTRLC_DIFFMODE", adcChannelMenu)
    adcSym_CTRLC_DIFFMODE.setLabel("Differential Mode")
    adcSym_CTRLC_DIFFMODE.setDefaultValue(False)

    #negative input
    adcSym_INPUTCTRL_MUXNEG = adcComponent.createKeyValueSetSymbol("ADC_INPUTCTRL_MUXNEG", adcChannelMenu)
    adcSym_INPUTCTRL_MUXNEG.setLabel("Select Negative Input")
    adcSym_INPUTCTRL_MUXNEG.setOutputMode("Key")
    adcSym_INPUTCTRL_MUXNEG.setDisplayMode("Description")
    adcSym_INPUTCTRL_MUXNEG.setReadOnly(True)
    defaultIndex = 0
    gndIndex = 0
    adcNagativeInputNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]/value-group@[name=\"ADC_INPUTCTRL__MUXNEG\"]")
    adcNagativeInputValues = []
    adcNagativeInputValues = adcNagativeInputNode.getChildren()
    for index in range(0, len(adcNagativeInputValues)):
        if adcNagativeInputValues[index].getAttribute("name") == "GND":
            defaultIndex = gndIndex
        if "AIN" in adcNagativeInputValues[index].getAttribute("name"):
            if adcNagativeInputValues[index].getAttribute("name") in channel:
                adcSym_INPUTCTRL_MUXNEG.addKey(adcNagativeInputValues[index].getAttribute("name"), adcNagativeInputValues[index].getAttribute("value"),
                adcNagativeInputValues[index].getAttribute("caption"))
                gndIndex += 1
        else:
            adcSym_INPUTCTRL_MUXNEG.addKey(adcNagativeInputValues[index].getAttribute("name"), adcNagativeInputValues[index].getAttribute("value"),
            adcNagativeInputValues[index].getAttribute("caption"))
            gndIndex += 1
    adcSym_INPUTCTRL_MUXNEG.setDefaultValue(defaultIndex)
    adcSym_INPUTCTRL_MUXNEG.setDependencies(adcNegativeInput, ["ADC_CTRLC_DIFFMODE"])

    adcResultMenu = adcComponent.createMenuSymbol("ADC_RESULT_MENU", None)
    adcResultMenu.setLabel("Result Configuration")

    #resolution configuration
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

    #Averaging
    adcSym_AVGCTRL_SAMPLENUM = adcComponent.createKeyValueSetSymbol("ADC_AVGCTRL_SAMPLENUM", adcSym_CTRLC_RESSEL)
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
    adcSym_AVGCTRL_SAMPLENUM.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL"])

    #division coefficient
    adcSym_AVGCTRL_ADJRES = adcComponent.createIntegerSymbol("ADC_AVGCTRL_ADJRES", adcSym_CTRLC_RESSEL)
    adcSym_AVGCTRL_ADJRES.setLabel("Number of Right Shifts")
    adcSym_AVGCTRL_ADJRES.setMin(0)
    adcSym_AVGCTRL_ADJRES.setMax(7)
    adcSym_AVGCTRL_ADJRES.setDefaultValue(0)
    adcSym_AVGCTRL_ADJRES.setVisible(False)
    adcSym_AVGCTRL_ADJRES.setDependencies(adcResultConfVisibility, ["ADC_CTRLC_RESSEL"])

    #left adjusted mode
    adcSym_CTRLC_LEFTADJ = adcComponent.createBooleanSymbol("ADC_CTRLC_LEFTADJ", adcResultMenu)
    adcSym_CTRLC_LEFTADJ.setLabel("Left Aligned Result")
    adcSym_CTRLC_LEFTADJ.setVisible(True)

    #interrupt mode
    adcSym_INTENSET_RESRDY = adcComponent.createBooleanSymbol("ADC_INTENSET_RESRDY", adcResultMenu)
    adcSym_INTENSET_RESRDY.setLabel("Enable Result Ready Interrupt")

    #event out mode
    adcSym_EVCTRL_RSERDYEO = adcComponent.createBooleanSymbol("ADC_EVCTRL_RSERDYEO", adcResultMenu)
    adcSym_EVCTRL_RSERDYEO.setLabel("Enable Result Ready Event Out")

    adcSleepMenu = adcComponent.createMenuSymbol("ADC_SLEEP_MENU", None)
    adcSleepMenu.setLabel("Sleep Mode Configuration")

    #run in standby mode
    adcSym_CTRLA_RUNSTDBY = adcComponent.createBooleanSymbol("ADC_CTRLA_RUNSTDBY", adcSleepMenu)
    adcSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")
    adcSym_CTRLA_RUNSTDBY.setVisible(True)

    #run in on demand control mode
    adcSym_CTRLA_ONDEMAND = adcComponent.createBooleanSymbol("ADC_CTRLA_ONDEMAND", adcSleepMenu)
    adcSym_CTRLA_ONDEMAND.setLabel("On Demand Control")
    adcSym_CTRLA_ONDEMAND.setVisible(True)


    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    adcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]")
    adcModuleID = adcModuleNode.getAttribute("id")

    adcSym_CommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcSym_CommonHeaderFile.setSourcePath("../peripheral/adc_"+adcModuleID+"/plib_adc.h")
    adcSym_CommonHeaderFile.setOutputName("plib_adc.h")
    adcSym_CommonHeaderFile.setDestPath("/peripheral/adc/")
    adcSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_CommonHeaderFile.setType("HEADER")
    adcSym_CommonHeaderFile.setMarkup(True)

    adcSym_HeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcSym_HeaderFile.setSourcePath("../peripheral/adc_"+adcModuleID+"/templates/plib_adc.h.ftl")
    adcSym_HeaderFile.setOutputName("plib_adc"+adcInstanceIndex+".h")
    adcSym_HeaderFile.setDestPath("/peripheral/adc/")
    adcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_HeaderFile.setType("HEADER")
    adcSym_HeaderFile.setMarkup(True)

    adcSym_SourceFile = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSym_SourceFile.setSourcePath("../peripheral/adc_"+adcModuleID+"/templates/plib_adc.c.ftl")
    adcSym_SourceFile.setOutputName("plib_adc"+adcInstanceIndex+".c")
    adcSym_SourceFile.setDestPath("/peripheral/adc/")
    adcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/adc/")
    adcSym_SourceFile.setType("SOURCE")
    adcSym_SourceFile.setMarkup(True)

    adcSym_SystemInitFile = adcComponent.createFileSymbol("ADC_SYS_INIT", None)
    adcSym_SystemInitFile.setType("STRING")
    adcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSym_SystemInitFile.setSourcePath("../peripheral/adc_"+adcModuleID+"/templates/system/initialization.c.ftl")
    adcSym_SystemInitFile.setMarkup(True)

    adcSym_SystemDefFile = adcComponent.createFileSymbol("ADC_SYS_DEF", None)
    adcSym_SystemDefFile.setType("STRING")
    adcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSym_SystemDefFile.setSourcePath("../peripheral/adc_"+adcModuleID+"/templates/system/definitions.h.ftl")
    adcSym_SystemDefFile.setMarkup(True)
