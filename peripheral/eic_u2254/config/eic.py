###################################################################################################
######################################### Callbacks ###############################################
###################################################################################################

def setNMIAsynchProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setNMIFiltenProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setNMISenseProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setConfigFilterProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setDebouncenProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setEvcCtrlExtInteo1Property(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setConfigSenseProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setAsynchProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setDebouncerPrescalerProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def setDebouncerStatesXProperty(symbol, event):

    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(eicComponent):

    eicInstanceIndex = eicComponent.getID()[-1:]

    eicMenu = eicComponent.createMenuSymbol("EIC_MENU" , None)
    eicMenu.setLabel("Hardware Settings ")

    eicIndex = eicComponent.createIntegerSymbol("EIC_INDEX" , eicMenu)
    eicIndex.setVisible(False)
    eicIndex.setDefaultValue(int(eicInstanceIndex))

    extIntNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EIC\"]/instance@[name=\"EIC\"]/parameters/param@[name=\"EXTINT_NUM\"]")

    extIntCount = int(extIntNode.getAttribute("value"))

    eicSym_IntCount = eicComponent.createIntegerSymbol("EIC_INT_COUNT" , eicMenu)
    eicSym_IntCount.setDefaultValue(extIntCount)
    eicSym_IntCount.setVisible(False)

    # CTRLA - Clock Selection
    CTRLA_CKSEL_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_CLKSEL" , eicMenu)
    CTRLA_CKSEL_SelectionSymbol.setLabel("EIC Clock Source Selection")

    eicClkselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_CTRLA__CKSEL\"]")
    eicClkselValues = []
    eicClkselValues = eicClkselNode.getChildren()

    eicClkselDefaultValue = 0

    for index in range(len(eicClkselValues)):
        eicClkselKeyName = eicClkselValues[index].getAttribute("name")

        if (eicClkselKeyName == "CLK_GCLK"):
            eicClkselDefaultValue = index

        eicClkselKeyDescription = eicClkselValues[index].getAttribute("caption")
        eicClkselKeyValue = eicClkselValues[index].getAttribute("value")
        CTRLA_CKSEL_SelectionSymbol.addKey(eicClkselKeyName, eicClkselKeyValue , eicClkselKeyDescription)

    CTRLA_CKSEL_SelectionSymbol.setDefaultValue(eicClkselDefaultValue)
    CTRLA_CKSEL_SelectionSymbol.setOutputMode("Value")
    CTRLA_CKSEL_SelectionSymbol.setDisplayMode("Description")

    #Non-Maskable Interrupt Control
    eicPLX4 = eicComponent.createBooleanSymbol("NMI_CTRL", eicMenu)
    eicPLX4.setLabel("Non Maskable Interrupt Control")
    
    #NMIASYNCH
    NMI_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("NMI_ASYNCH" , eicPLX4)
    NMI_ASYNCH_Selection.setLabel("NMI Edge Detection Clock Synchronization")
    NMI_ASYNCH_Selection.setVisible(False)

    eicNMIAsyncNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_NMICTRL__NMIASYNCH\"]")
    eicNMIAsyncValues = []
    eicNMIAsyncValues = eicNMIAsyncNode.getChildren()

    eicNMIAsyncDefaultValue = 0

    for index in range(len(eicNMIAsyncValues)):
        eicNMIAsyncKeyName = eicNMIAsyncValues[index].getAttribute("name")

        if (eicNMIAsyncKeyName == "SYNC"):
            eicNMIAsyncDefaultValue = index

        eicNMIAsyncKeyDescription = eicNMIAsyncValues[index].getAttribute("caption")
        eicNMIAsyncKeyValue = eicNMIAsyncValues[index].getAttribute("value")
        NMI_ASYNCH_Selection.addKey(eicNMIAsyncKeyName, eicNMIAsyncKeyValue , eicNMIAsyncKeyDescription)

    NMI_ASYNCH_Selection.setDefaultValue(eicNMIAsyncDefaultValue)
    NMI_ASYNCH_Selection.setOutputMode("Value")
    NMI_ASYNCH_Selection.setDisplayMode("Description")
    NMI_ASYNCH_Selection.setDependencies(setNMIAsynchProperty, ["NMI_CTRL"])

    #NMIFILTEN
    NMI_FILTEN_Selection = eicComponent.createBooleanSymbol("NMI_FILTEN" , eicPLX4)
    NMI_FILTEN_Selection.setLabel("Enabled filter on NMI Pin ?")
    NMI_FILTEN_Selection.setVisible(False)
    NMI_FILTEN_Selection.setDependencies(setNMIFiltenProperty, ["NMI_CTRL"])

    # NMI - SENSE
    NMI_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("NMI_SENSE" , eicPLX4)
    NMI_SENSE_SelectionSymbol.setLabel("NMI Interrupt Detection Configuration")
    NMI_SENSE_SelectionSymbol.setVisible(False)

    eicNMISenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_NMICTRL__NMISENSE\"]")
    eicNMISenseValues = []
    eicNMISenseValues = eicNMISenseNode.getChildren()

    eicNMISenseDefaultValue = 0

    for index in range(len(eicNMISenseValues)):
        eicNMISenseKeyName = eicNMISenseValues[index].getAttribute("name")

        if (eicNMISenseKeyName == "NONE"):
            eicNMISenseDefaultValue = index

        eicNMISenseKeyDescription = eicNMISenseValues[index].getAttribute("caption")
        eicNMISenseKeyValue = eicNMISenseValues[index].getAttribute("value")
        NMI_SENSE_SelectionSymbol.addKey(eicNMISenseKeyName, eicNMISenseKeyValue , eicNMISenseKeyDescription)

    NMI_SENSE_SelectionSymbol.setDefaultValue(eicNMISenseDefaultValue)
    NMI_SENSE_SelectionSymbol.setOutputMode("Key")
    NMI_SENSE_SelectionSymbol.setDisplayMode("Description")
    NMI_SENSE_SelectionSymbol.setDependencies(setNMISenseProperty, ["NMI_CTRL"])
    
    #Interrupt 0 - EXTINT Settings
    for extIntIndex in range(0 , extIntCount):

        eicPLX1 = eicComponent.createBooleanSymbol("EIC_INT_CHAN_" + str(extIntIndex) , eicMenu)
        eicPLX1.setLabel("Enable EXTINT " + str(extIntIndex))

        #EVCTRL - External Interrupt Event Output Enable 0..7 Channel number
        EVCCTRL_EXTINTEO_Selection = eicComponent.createBooleanSymbol("EIC_EVCTRL_EXTINTEO_" + str(extIntIndex) , eicPLX1)
        EVCCTRL_EXTINTEO_Selection.setLabel("Enable Event Output Enable on Interrupt " + str(extIntIndex) + "?")
        EVCCTRL_EXTINTEO_Selection.setVisible(False)
        
        #ASYNCH
        ASYNCH_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("EIC_ASYNCH_" + str(extIntIndex) , eicPLX1)
        ASYNCH_ASYNCH_Selection.setLabel("External Interrupt " + str(extIntIndex) + " Edge Detection Clock Synchronization")
        ASYNCH_ASYNCH_Selection.setVisible(False)

        eicAsynchNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_ASYNCH__ASYNCH\"]")
        eicAsynchValues = []
        eicAsynchValues = eicAsynchNode.getChildren()

        eicAsynchDefaultValue = 0

        for index in range(len(eicAsynchValues)):
            eicAsynchKeyName = eicAsynchValues[index].getAttribute("name")

            if (eicAsynchKeyName == "SYNC"):
                eicAsynchDefaultValue = index

            eicAsynchKeyDescription = eicAsynchValues[index].getAttribute("caption")
            eicAsynchKeyValue = eicAsynchValues[index].getAttribute("value")
            ASYNCH_ASYNCH_Selection.addKey(eicAsynchKeyName, eicAsynchKeyValue , eicAsynchKeyDescription)

        ASYNCH_ASYNCH_Selection.setDefaultValue(eicAsynchDefaultValue)
        ASYNCH_ASYNCH_Selection.setOutputMode("Value")
        ASYNCH_ASYNCH_Selection.setDisplayMode("Description")
        ASYNCH_ASYNCH_Selection.setDependencies(setAsynchProperty, ["EIC_INT_CHAN_" + str(extIntIndex)])

        #CONFIG - Sense Enable
        CONFIG_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_CONFIG_SENSE_" + str(extIntIndex) , eicPLX1)
        CONFIG_SENSE_SelectionSymbol.setLabel("External Interrupt " + str(extIntIndex) + " Detection Configuration")
        CONFIG_SENSE_SelectionSymbol.setVisible(False)

        eicConfigSenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_CONFIG__SENSE0\"]")
        eicConfigSenseValues = []
        eicConfigSenseValues = eicConfigSenseNode.getChildren()

        eicConfigSenseDefaultValue = 0

        for index in range(len(eicConfigSenseValues)):
            eicConfigSenseKeyName = eicConfigSenseValues[index].getAttribute("name")

            if (eicConfigSenseKeyName == "NONE"):
                eicConfigSenseDefaultValue = index

            eicConfigSenseKeyDescription = eicConfigSenseValues[index].getAttribute("caption")
            eicConfigSenseKeyValue = eicConfigSenseValues[index].getAttribute("value")
            CONFIG_SENSE_SelectionSymbol.addKey(eicConfigSenseKeyName, eicConfigSenseKeyValue , eicConfigSenseKeyDescription)

        CONFIG_SENSE_SelectionSymbol.setDefaultValue(eicConfigSenseDefaultValue)
        CONFIG_SENSE_SelectionSymbol.setOutputMode("Key")
        CONFIG_SENSE_SelectionSymbol.setDisplayMode("Description")
        CONFIG_SENSE_SelectionSymbol.setDependencies(setConfigSenseProperty, ["EIC_INT_CHAN_" + str(extIntIndex)])

        #CONFIG - Filter Enable
        CONFIG_FILTER_Selection = eicComponent.createBooleanSymbol("EIC_CONFIG_FILTEN_" + str(extIntIndex) , eicPLX1)
        CONFIG_FILTER_Selection.setLabel("Enable filter on External Interrupt Pin " + str(extIntIndex) + "?")
        CONFIG_FILTER_Selection.setVisible(False)
        CONFIG_FILTER_Selection.setDependencies(setConfigFilterProperty, ["EIC_INT_CHAN_" + str(extIntIndex)])

        #DEBOUNCEN
        DEBOUNCEN_Selection = eicComponent.createBooleanSymbol("EIC_DEBOUNCEN_" + str(extIntIndex) , eicPLX1)
        DEBOUNCEN_Selection.setLabel("Enable debounce on External Interrupt Pin " + str(extIntIndex) + "?")
        DEBOUNCEN_Selection.setVisible(False)
        DEBOUNCEN_Selection.setDependencies(setDebouncenProperty, ["EIC_INT_CHAN_" + str(extIntIndex)])

    #DEBOUNCER - TICKON
    PRESCALER_TICKON_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_PRESCALER_TICKON" , eicMenu)
    PRESCALER_TICKON_SelectionSymbol.setLabel("Debouncer Sampler Clock Source")

    eicTickOnNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__TICKON\"]")
    eicTickOnValues = []
    eicTickOnValues = eicTickOnNode.getChildren()

    eicTickOnDefaultValue = 0

    for index in range(len(eicTickOnValues)):
        eicTickOnKeyName = eicTickOnValues[index].getAttribute("name")

        if (eicTickOnKeyName == "BOUNCE_SAMP_CLK_GCLK_EIC"):
            eicTickOnDefaultValue = index

        eicTickOnKeyDescription = eicTickOnValues[index].getAttribute("caption")
        eicTickOnKeyValue = eicTickOnValues[index].getAttribute("value")
        PRESCALER_TICKON_SelectionSymbol.addKey(eicTickOnKeyName, eicTickOnKeyValue , eicTickOnKeyDescription)

    PRESCALER_TICKON_SelectionSymbol.setDefaultValue(eicTickOnDefaultValue)
    PRESCALER_TICKON_SelectionSymbol.setOutputMode("Value")
    PRESCALER_TICKON_SelectionSymbol.setDisplayMode("Description")

    #DEBOUNCER - Number of States x (7:0)
    DEBOUNCER_NO_STATES_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_NO_STATES_0" , eicMenu)
    DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States Duration for EXTINT[7:0]")

    eicStatesxNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__STATES0\"]")
    eicStatesxValues = []
    eicStatesxValues = eicStatesxNode.getChildren()

    eicStatesxDefaultValue = 0

    for index in range(len(eicStatesxValues)):
        eicStatesxKeyName = eicStatesxValues[index].getAttribute("name")

        if (eicStatesxKeyName == "LFREQ3"):
            eicStatesxDefaultValue = index

        eicStatesxKeyDescription = eicStatesxValues[index].getAttribute("caption")
        eicStatesxKeyValue = eicStatesxValues[index].getAttribute("value")
        DEBOUNCER_NO_STATES_SelectionSymbol.addKey(eicStatesxKeyName, eicStatesxKeyValue , eicStatesxKeyDescription)

    DEBOUNCER_NO_STATES_SelectionSymbol.setDefaultValue(eicStatesxDefaultValue)
    DEBOUNCER_NO_STATES_SelectionSymbol.setOutputMode("Value")
    DEBOUNCER_NO_STATES_SelectionSymbol.setDisplayMode("Description")

    #BOUNCER - Prescaler x (7:0)
    DEBOUNCER_PRESCALER_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_PRESCALER_0" , eicMenu)
    DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[7:0]")

    eicPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__PRESCALER0\"]")
    eicPrescalerValues = []
    eicPrescalerValues = eicPrescalerNode.getChildren()

    eicPrescalerDefaultValue = 0

    for index in range(len(eicPrescalerValues)):
        eicPrescalerKeyName = eicPrescalerValues[index].getAttribute("name")

        if (eicPrescalerKeyName == "DIV2"):
            eicPrescalerDefaultValue = index

        eicPrescalerKeyDescription = eicPrescalerValues[index].getAttribute("caption")
        eicPrescalerKeyValue = eicPrescalerValues[index].getAttribute("value")
        DEBOUNCER_PRESCALER_SelectionSymbol.addKey(eicPrescalerKeyName, eicPrescalerKeyValue , eicPrescalerKeyDescription)

    DEBOUNCER_PRESCALER_SelectionSymbol.setDefaultValue(eicPrescalerDefaultValue)
    DEBOUNCER_PRESCALER_SelectionSymbol.setOutputMode("Value")
    DEBOUNCER_PRESCALER_SelectionSymbol.setDisplayMode("Description")

    #DEBOUNCER - Number of States x (8:15)
    DEBOUNCER_NO_STATES_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_NO_STATES_1" , eicMenu)
    DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States Duration for EXTINT[15:8]")

    eicStatesxNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__STATES1\"]")
    eicStatesxValues = []
    eicStatesxValues = eicStatesxNode.getChildren()

    eicStatesxDefaultValue = 0

    for index in range(len(eicStatesxValues)):
        eicStatesxKeyName = eicStatesxValues[index].getAttribute("name")

        if (eicStatesxKeyName == "LFREQ3"):
            eicStatesxDefaultValue = index

        eicStatesxKeyDescription = eicStatesxValues[index].getAttribute("caption")
        eicStatesxKeyValue = eicStatesxValues[index].getAttribute("value")
        DEBOUNCER_NO_STATES_SelectionSymbol.addKey(eicStatesxKeyName, eicStatesxKeyValue , eicStatesxKeyDescription)

    DEBOUNCER_NO_STATES_SelectionSymbol.setDefaultValue(eicStatesxDefaultValue)
    DEBOUNCER_NO_STATES_SelectionSymbol.setOutputMode("Value")
    DEBOUNCER_NO_STATES_SelectionSymbol.setDisplayMode("Description")

    #BOUNCER - Prescaler x (8:15)
    DEBOUNCER_PRESCALER_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_PRESCALER_1" , eicMenu)
    DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[15:8]")

    eicPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__PRESCALER1\"]")
    eicPrescalerValues = []
    eicPrescalerValues = eicPrescalerNode.getChildren()

    eicPrescalerDefaultValue = 0

    for index in range(len(eicPrescalerValues)):
        eicPrescalerKeyName = eicPrescalerValues[index].getAttribute("name")

        if (eicPrescalerKeyName == "DIV2"):
            eicPrescalerDefaultValue = index

        eicPrescalerKeyDescription = eicPrescalerValues[index].getAttribute("caption")
        eicPrescalerKeyValue = eicPrescalerValues[index].getAttribute("value")
        DEBOUNCER_PRESCALER_SelectionSymbol.addKey(eicPrescalerKeyName, eicPrescalerKeyValue , eicPrescalerKeyDescription)

    DEBOUNCER_PRESCALER_SelectionSymbol.setDefaultValue(eicPrescalerDefaultValue)
    DEBOUNCER_PRESCALER_SelectionSymbol.setOutputMode("Value")
    DEBOUNCER_PRESCALER_SelectionSymbol.setDisplayMode("Description")

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eicHeader1File = eicComponent.createFileSymbol("EIC_HEADER", None)
    eicHeader1File.setSourcePath("../peripheral/eic_u2254/templates/plib_eic.h.ftl")
    eicHeader1File.setOutputName("plib_eic" + str(eicInstanceIndex) + ".h")
    eicHeader1File.setDestPath("/peripheral/eic/")
    eicHeader1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicHeader1File.setType("HEADER")
    eicHeader1File.setMarkup(True)

    eicSource1File = eicComponent.createFileSymbol("EIC_SOURCE", None)
    eicSource1File.setSourcePath("../peripheral/eic_u2254/templates/plib_eic.c.ftl")
    eicSource1File.setOutputName("plib_eic" + str(eicInstanceIndex) + ".c")
    eicSource1File.setDestPath("/peripheral/eic/")
    eicSource1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicSource1File.setType("SOURCE")
    eicSource1File.setMarkup(True)

    eicSystemInitFile = eicComponent.createFileSymbol("EIC_SYS_INT", None)
    eicSystemInitFile.setType("STRING")
    eicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eicSystemInitFile.setSourcePath("../peripheral/eic_u2254/templates/system/initialization.c.ftl")
    eicSystemInitFile.setMarkup(True)

    eicSystemDefFile = eicComponent.createFileSymbol("EIC_SYS_DEF", None)
    eicSystemDefFile.setType("STRING")
    eicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eicSystemDefFile.setSourcePath("../peripheral/eic_u2254/templates/system/definitions.h.ftl")
    eicSystemDefFile.setMarkup(True)
