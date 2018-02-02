from math import ceil

daccRegModule = Register.getRegisterModule("DACC")
daccValGrp_TRIGR_TRGSEL0 = daccRegModule.getValueGroup("DACC_TRIGR__TRGSEL0")
daccValGrp_TRIGR_OSR0 = daccRegModule.getValueGroup("DACC_TRIGR__OSR0")

dacChannelMenu = []
dacChannelBiasCurrent = []
dacChannelConversionMode = []
dacChannelTriggerSelect = []
dacChannelOSR = []
dacChannelMaxSpeed = []
dacChannelTriggerEnable = []

#-----------------------------------------------------------------------------------------------------------------------

#Function for initiating the UI
def instantiateComponent(daccComponent):
    num = daccComponent.getID()[-1:]
    print("Running DACC" + str(num))

    daccMenu = daccComponent.createMenuSymbol(None, None)
    daccMenu.setLabel("Configurations")

    daccIndex = daccComponent.createIntegerSymbol("INDEX", daccMenu)
    daccIndex.setVisible(False)
    daccIndex.setDefaultValue(int(num))
    
    daccSym_MR_PRESCALER = daccComponent.createIntegerSymbol("DACC_MR_PRESCALER", daccMenu)
    daccSym_MR_PRESCALER.setLabel("Prescaler Value")
    daccSym_MR_PRESCALER.setMin(0)
    daccSym_MR_PRESCALER.setMax(15)
    daccSym_MR_PRESCALER.setDefaultValue(15)

    dacFreq=daccGetMasterClockFrequency()/(daccSym_MR_PRESCALER.getValue()*1000000)
    dacFreq=int(ceil(dacFreq))

    daccPrescalerWarning = daccComponent.createCommentSymbol("PRESCALER_COMMENT", daccMenu)
    daccPrescalerWarning.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz for the selected prescaler value ****")
    daccPrescalerWarning.setVisible(True)
    daccPrescalerWarning.setDependencies(calcDacFrequency, ["DACC_MR_PRESCALER"])


    daccSym_MR_DIFF = daccComponent.createKeyValueSetSymbol("DACC_MR_DIFF", daccMenu)
    daccSym_MR_DIFF.setLabel ("Select DAC Output Mode")
    daccSym_MR_DIFF.addKey("SINGLE_ENDED", "0", "Single-Ended Output")
    daccSym_MR_DIFF.addKey("DIFFERENTIAL", "1", "Differential Output")
    daccSym_MR_DIFF.setOutputMode("Key")
    daccSym_MR_DIFF.setDisplayMode("Description")
    daccSym_MR_DIFF.setDefaultValue(0)

    # ------------------------------------------------------------------------------------------------------------------
    for channelID in range(0, 2):

        dacChannelMenu.append(channelID)
        dacChannelMenu[channelID] = daccComponent.createBooleanSymbol("DACC_CHER_CH"+str(channelID), daccMenu)
        dacChannelMenu[channelID].setLabel("Enable Channel "+str(channelID))
        dacChannelMenu[channelID].setDependencies(channel1Visibility, ["DACC_MR_DIFF"])

        dacChannelConversionMode.append(channelID)
        dacChannelConversionMode[channelID] = daccComponent.createKeyValueSetSymbol("CONVERSION_MODE_CH"+str(channelID), dacChannelMenu[channelID])
        dacChannelConversionMode[channelID].setLabel("Select Conversion Mode")
        dacChannelConversionMode[channelID].addKey("FREE_RUNNING_MODE", "0", "Free-Running Mode")
        dacChannelConversionMode[channelID].addKey("MAX_SPEED_MODE", "1", "Maximum-Speed Mode")
        dacChannelConversionMode[channelID].addKey("TRIGGER_MODE", "2", "External Trigger Mode")
        dacChannelConversionMode[channelID].setOutputMode("Key")
        dacChannelConversionMode[channelID].setDisplayMode("Description")
        dacChannelConversionMode[channelID].setDefaultValue(0)


        dacChannelBiasCurrent.append(channelID)
        dacChannelBiasCurrent[channelID] = daccComponent.createKeyValueSetSymbol("DACC_ACR_IBCTLCH"+str(channelID), dacChannelMenu[channelID])
        dacChannelBiasCurrent[channelID].setLabel("Select Conversion Speed")
        dacChannelBiasCurrent[channelID].addKey("BYPASS", "0", "Bypass mode: Disables output buffer to minimize power")
        dacChannelBiasCurrent[channelID].addKey("500K", "1", "<500 Ksps Conversion speed")
        dacChannelBiasCurrent[channelID].addKey("1M", "3", "Up to 1 Msps Conversion speed")
        dacChannelBiasCurrent[channelID].setOutputMode("Value")
        dacChannelBiasCurrent[channelID].setDisplayMode("Description")
        dacChannelBiasCurrent[channelID].setDefaultValue(0)
        dacChannelBiasCurrent[channelID].setDependencies(setDacSpeed, ["CONVERSION_MODE_CH"+str(channelID)])


        dacChannelMaxSpeed.append(channelID)
        dacChannelMaxSpeed[channelID] = daccComponent.createBooleanSymbol("DACC_MR_MAXS"+str(channelID), dacChannelMenu[channelID])
        dacChannelMaxSpeed[channelID].setLabel("Max Speed Mode")
        dacChannelMaxSpeed[channelID].setVisible(False)

        dacChannelTriggerEnable.append(channelID)
        dacChannelTriggerEnable[channelID] = daccComponent.createBooleanSymbol("DACC_TRIGR_TRGEN"+str(channelID), dacChannelMenu[channelID])
        dacChannelTriggerEnable[channelID].setLabel("Enable Trigger Mode")
        dacChannelTriggerEnable[channelID].setVisible(False)
        dacChannelTriggerEnable[channelID].setDependencies(setupModeBits, ["CONVERSION_MODE_CH"+str(channelID)])

        dacChannelTriggerSelect.append(channelID)
        dacChannelTriggerSelect[channelID] = daccComponent.createKeyValueSetSymbol("DACC_TRIGR_TRGSEL"+str(channelID), dacChannelMenu[channelID])
        dacChannelTriggerSelect[channelID].setLabel("Select Trigger Source")
        dacChannelTriggerSelect[channelID].setDefaultValue(0)
        dacChannelTriggerSelect[channelID].setOutputMode("Key")
        dacChannelTriggerSelect[channelID].setDisplayMode("Description")
        dacChannelTriggerSelect[channelID].setVisible(False)
        dacChannelTriggerSelect[channelID].setDependencies(triggerVisibility, ["CONVERSION_MODE_CH"+str(channelID)])

        count = daccValGrp_TRIGR_TRGSEL0.getValueCount()
        for id in range(0,count):
            valueName = daccValGrp_TRIGR_TRGSEL0.getValueNames()[id]
            dacChannelTriggerSelect[channelID].addKey(valueName, daccValGrp_TRIGR_TRGSEL0.getValue(valueName).getValue(), daccValGrp_TRIGR_TRGSEL0.getValue(valueName).getDescription())

        dacChannelOSR.append(channelID)
        dacChannelOSR[channelID] = daccComponent.createKeyValueSetSymbol("DACC_TRIGR_OSR"+str(channelID), dacChannelMenu[channelID])
        dacChannelOSR[channelID].setLabel("Select Oversampling Ratio for Interpolation Filter")
        dacChannelOSR[channelID].setDefaultValue(0)
        dacChannelOSR[channelID].setOutputMode("Key")
        dacChannelOSR[channelID].setDisplayMode("Description")
        dacChannelOSR[channelID].setVisible(False)
        count = daccValGrp_TRIGR_OSR0.getValueCount()
        for id in range(0,count):
            valueName = daccValGrp_TRIGR_OSR0.getValueNames()[id]
            dacChannelOSR[channelID].addKey(valueName, daccValGrp_TRIGR_OSR0.getValue(valueName).getValue(), daccValGrp_TRIGR_OSR0.getValue(valueName).getDescription())

    # ------------------------------------------------------------------------------------------------------------------

    daccHeader1File = daccComponent.createFileSymbol(None, None)
    daccHeader1File.setSourcePath("../peripheral/dacc_11246/templates/plib_dacc.h.ftl")
    daccHeader1File.setOutputName("plib_dacc" + str(num) + ".h")
    daccHeader1File.setMarkup(True)
    daccHeader1File.setDestPath("peripheral/dacc/")
    daccHeader1File.setProjectPath("peripheral/dacc/")
    daccHeader1File.setType("HEADER")
    daccHeader1File.setOverwrite(True)

    daccSource1File = daccComponent.createFileSymbol(None, None)
    daccSource1File.setSourcePath("../peripheral/dacc_11246/templates/plib_dacc.c.ftl")
    daccSource1File.setOutputName("plib_dacc" + str(num) + ".c")
    daccSource1File.setMarkup(True)
    daccSource1File.setDestPath("peripheral/dacc/")
    daccSource1File.setProjectPath("peripheral/dacc/")
    daccSource1File.setType("SOURCE")
    daccSource1File.setOverwrite(True)

#-----------------------------------------------------------------------------------------------------------------------
#Callback Functions

#TODO Read from clock manager
def daccGetMasterClockFrequency():
    main_clk_sym = Database.getSymbolByID("core", "MASTERCLK_FREQ")
    main_clk_freq = int(main_clk_sym.getValue())
    return main_clk_freq

def calcDacFrequency(symbol,prescaler):
    dacFreq=daccGetMasterClockFrequency()/(prescaler.getValue()*1000000)
    dacFreq=int(ceil(dacFreq))

    print("DAC Frequency = "+str(dacFreq)+" MHz")

    if(dacFreq<=12):
        symbol.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz ****")
    else:
        symbol.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz is greater than 12MHz, Increase the prescaler value ****")

def triggerVisibility(symbol,convMode):
    id = symbol.getID()[-1]
    channelID = int(id)

    if (convMode.getSelectedKey() == "TRIGGER_MODE"):
        dacChannelTriggerSelect[channelID].setVisible(True)
        dacChannelOSR[channelID].setVisible(True)
    else:
        dacChannelTriggerSelect[channelID].setVisible(False)
        dacChannelOSR[channelID].setVisible(False)

def channel1Visibility(symbol,outputMode):
    if (outputMode.getSelectedKey() == "DIFFERENTIAL"):
        dacChannelMenu[1].setVisible(False)
    else:
        dacChannelMenu[1].setVisible(True)

def setupModeBits(symbol, convMode):
    id = symbol.getID()[-1]
    channelID = int(id)

    if (convMode.getSelectedKey() == "MAX_SPEED_MODE"):
        dacChannelMaxSpeed[channelID].clearValue("DACC_MR_MAXS"+str(channelID))
        dacChannelMaxSpeed[channelID].setValue("DACC_MR_MAXS"+str(channelID), True, 1)
    else:
        dacChannelMaxSpeed[channelID].clearValue("DACC_MR_MAXS"+str(channelID))
        dacChannelMaxSpeed[channelID].setValue("DACC_MR_MAXS"+str(channelID), False, 1)

    if (convMode.getSelectedKey() == "TRIGGER_MODE"):
        dacChannelTriggerEnable[channelID].clearValue("DACC_TRIGR_TRGEN"+str(channelID))
        dacChannelTriggerEnable[channelID].setValue("DACC_TRIGR_TRGEN"+str(channelID), True, 1)
    else:
        dacChannelTriggerEnable[channelID].clearValue("DACC_TRIGR_TRGEN"+str(channelID))
        dacChannelTriggerEnable[channelID].setValue("DACC_TRIGR_TRGEN"+str(channelID), False, 1)

def setDacSpeed(symbol, convMode):
    id = symbol.getID()[-1]
    channelID = int(id)

    if (convMode.getSelectedKey() == "MAX_SPEED_MODE"):
		dacChannelBiasCurrent[channelID].clearValue("DACC_ACR_IBCTLCH"+str(channelID))
		dacChannelBiasCurrent[channelID].setSelectedKey("DACC_ACR_IBCTLCH"+str(channelID),"1M",1)
		dacChannelBiasCurrent[channelID].setVisible(False)
    else:
		dacChannelBiasCurrent[channelID].setVisible(True)
