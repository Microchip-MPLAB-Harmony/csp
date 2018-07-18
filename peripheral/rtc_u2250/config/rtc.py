################################################################################
########                        Callback Functions                      ########
################################################################################

#################################### MODE0 #####################################

#Enable Interrupt Property
def setrtcMode0InterruptVisibleProperty(symbol, event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Prescaler Property
def setrtcMode0PrescalerVisibleProperty(symbol, event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Period Notification Property
def setrtcMode0PeriodNotificationVisibleProperty(symbol, event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Configure 32-bit Timer Counter Period
def setrtcMode0TimerPeriodVisibleProperty(symbol,event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Generate Frequency Correction API
def setrtcMode0FrequencyCorrectionVisibleProperty(symbol, event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#################################### MODE1 #####################################

#Enable Interrupt Property
def setrtcMode1InterruptVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Prescaler  Property
def setrtcMode1PrescalerVisibleProperty( symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Period Notification Property
def setrtcMode1PeriodNotificationVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Configure 16-bit Timer Counter Period
def setrtcMode1TimerPeriodVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare 0 Configure Property
def setrtcMode1Compare0ConfigureVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare 0 Match Value Property
def setrtcMode1Compare0MatchValueVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare0 Interrupt Enable Property
def setrtcMode1Compare0GenerateAPIVisisbleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare 1 Configure Property
def setrtcMode1Compare1ConfigureVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare 1 Match Value Property
def setrtcMode1Compare1MatchValueVisibleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Compare 1 Generate API
def setrtcMode1Compare1GenerateAPIVisisbleProperty(symbol,event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Generate Frequency Correction API
def setrtcMode1FrequencyCorrectionVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#################################### MODE2 #####################################

#Enable Interrupt Property
def setrtcMode2InterruptVisibleProperty(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
        symbol.setValue(1,0)
    else:
        symbol.setVisible(False)

#Set Prescaler Property
def setrtcMode2PresaclerVisibleProperty(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Period Notification Property
def setrtcMode2PeriodNotificationVisibleProperty(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Set Clock Representation Property
def setrtcMode2ClkRepVisibleProperty(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Reference Year Property
def setrtcMode2ReferenceYearVisibleProperty(symbol,event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Generate Frequency Correction API
def setrtcMode2FrequencyCorrectionVisibleProperty(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

########################## Code Generation Property ############################

#Update Code Generation Property
def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()
    if(event["value"] == 2):
        component.getSymbolByID("RTC_INSTANCE_HEADER").setEnabled(True)
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(True)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(False)
    else:
        component.getSymbolByID("RTC_INSTANCE_HEADER").setEnabled(True)
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(False)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(True)

################################################################################
########                   RTC DATABASE COMPONENTS                      ########
################################################################################

def instantiateComponent(rtcComponent):
    rtcInstanceIndex = rtcComponent.getID()[-1:]
    Log.writeInfoMessage("Running RTC : " + rtcInstanceIndex)

    #Periodic Interval Notification List
    rtcPERList = ["NO","PER0","PER1","PER2","PER3","PER4","PER5","PER6","PER7"]

    #RTC Main Menu
    rtcSym_Menu = rtcComponent.createMenuSymbol("RTC_OPERATION_MODE",None)
    rtcSym_Menu.setLabel("Hardware Settings")

    #Sub Menu - RTC Modes: RTC_MODE0, RTC_MODE1, RTC_MODE2
    rtcSymSubMenu = rtcComponent.createKeyValueSetSymbol("RTC_MODULE_SELECTION", rtcSym_Menu)
    rtcSymSubMenu.setLabel("RTC Operation Mode")
    rtcSymSubMenu.addKey("MODE0","0","RTC - 32-bit Counter with Single 32-bit Compare")
    rtcSymSubMenu.addKey("MODE1","1","RTC - 16-bit Counter with Two 16-bit Compares")
    rtcSymSubMenu.addKey("MODE2","2","RTC - Clock/Calendar with Alarm")
    rtcSymSubMenu.setDefaultValue(0)
    rtcSymSubMenu.setOutputMode("Key")
    rtcSymSubMenu.setDisplayMode("Description")

    #RTC Instance Index
    rtcSym_INDEX = rtcComponent.createIntegerSymbol("RTC_INDEX", rtcSym_Menu)
    rtcSym_INDEX.setLabel("RTC_INDEX")
    rtcSym_INDEX.setVisible(False)
    rtcSym_INDEX.setDefaultValue(int(rtcInstanceIndex))
    rtcSym_INDEX.setDependencies(updateCodeGenerationProperty, ["RTC_MODULE_SELECTION"])

#################################### MODE0 #####################################

    #Interrupt Enable Set
    rtcSymMode0_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE0_INTERRUPT", rtcSymSubMenu)
    rtcSymMode0_INTENSET.setLabel("Enable Interrupts?")
    rtcSymMode0_INTENSET.setDependencies(setrtcMode0InterruptVisibleProperty,["RTC_MODULE_SELECTION"])

    #Prescaler
    rtcSymMode0_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE0_PRESCALER", rtcSymSubMenu)
    rtcSymMode0_CTRLA_PRESCALER.setLabel("RTC Clock Source Divide-by Prescaler")

    rtcMode0ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE0_CTRLA__PRESCALER\"]")
    rtcMode0ReferenceValues = []
    rtcMode0ReferenceValues = rtcMode0ReferenceNode.getChildren()

    rtcMode0ReferenceDefaultValue = 0

    for index in range(len(rtcMode0ReferenceValues)):
        rtcMode0ReferenceKeyName = rtcMode0ReferenceValues[index].getAttribute("name")

        if (rtcMode0ReferenceKeyName == "DIV1"):
            rtcMode0ReferenceDefaultValue = index

        rtcMode0ReferenceKeyDescription = rtcMode0ReferenceValues[index].getAttribute("caption")
        rtcMode0ReferenceKeyValue = rtcMode0ReferenceValues[index].getAttribute("value")
        rtcSymMode0_CTRLA_PRESCALER.addKey(rtcMode0ReferenceKeyName , rtcMode0ReferenceKeyValue , rtcMode0ReferenceKeyDescription)

    rtcSymMode0_CTRLA_PRESCALER.setDefaultValue(rtcMode0ReferenceDefaultValue)
    rtcSymMode0_CTRLA_PRESCALER.setOutputMode("Value")
    rtcSymMode0_CTRLA_PRESCALER.setDependencies(setrtcMode0PrescalerVisibleProperty,["RTC_MODULE_SELECTION"])

    #Periodic Interval Notification
    rtcSymMode0_PERIN = rtcComponent.createKeyValueSetSymbol("RTC_MODE0_PERIOD", rtcSymSubMenu)
    rtcSymMode0_PERIN.setLabel("Enable Periodic Interval Notification?")
    rtcSymMode0_PERIN.addKey("NO","NO","NO")
    rtcSymMode0_PERIN.addKey("Generate 8 Cycles","PER0","Generate 8 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 16 Cycles","PER1","Generate 16 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 32 Cycles","PER2","Generate 32 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 64 Cycles","PER3","Generate 64 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 128 Cycles","PER4","Generate 128 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 256 Cycles","PER5","Generate 256 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 512 Cycles","PER6","Generate 512 Cycles")
    rtcSymMode0_PERIN.addKey("Generate 1024 Cycles","PER7","Generate 1024 Cycles")
    rtcSymMode0_PERIN.setDefaultValue(0)
    rtcSymMode0_PERIN.setOutputMode("Value")
    rtcSymMode0_PERIN.setDependencies(setrtcMode0PeriodNotificationVisibleProperty,["RTC_MODULE_SELECTION"])

    #Configure 32-Bit Timer Period
    rtcSymMode0_COMP0 = rtcComponent.createHexSymbol("RTC_MODE0_TIMER_COUNTER_PERIOD",rtcSymSubMenu)
    rtcSymMode0_COMP0.setLabel("32-bit Timer Period")
    rtcSymMode0_COMP0.setVisible(True)
    rtcSymMode0_COMP0.setDefaultValue(0x00000000)
    rtcSymMode0_COMP0.setMax(0xFFFFFFFF)
    rtcSymMode0_COMP0.setMin(0x00000000)
    rtcSymMode0_COMP0.setDependencies(setrtcMode0TimerPeriodVisibleProperty,["RTC_MODULE_SELECTION"])

    #Frequency Correction
    rtcSymMode0_FREQCORR = rtcComponent.createBooleanSymbol("RTC_MODE0_FREQCORR",rtcSymSubMenu)
    rtcSymMode0_FREQCORR.setLabel("Generate Frequency Correction API")
    rtcSymMode0_FREQCORR.setDependencies(setrtcMode0FrequencyCorrectionVisibleProperty,["RTC_MODULE_SELECTION"])

#################################### MODE1 #####################################

    #Configure the RTC Interrupts
    rtcSymMode1_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE1_INTERRUPT", rtcSymSubMenu)
    rtcSymMode1_INTENSET.setLabel("Enable Interrupts?")
    rtcSymMode1_INTENSET.setVisible(False)
    rtcSymMode1_INTENSET.setDependencies(setrtcMode1InterruptVisibleProperty,["RTC_MODULE_SELECTION"])

    #Prescaler
    rtcSymMode1_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE1_PRESCALER", rtcSymSubMenu)
    rtcSymMode1_CTRLA_PRESCALER.setLabel("RTC Clock Source Divide-by Prescaler")
    rtcSymMode1_CTRLA_PRESCALER.setVisible(False)

    rtcMode1ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE1_CTRLA__PRESCALER\"]")
    rtcMode1ReferenceValues = []
    rtcMode1ReferenceValues = rtcMode1ReferenceNode.getChildren()

    rtcMode1ReferenceDefaultValue = 0

    for index in range(len(rtcMode1ReferenceValues)):
        rtcMode1ReferenceKeyName = rtcMode1ReferenceValues[index].getAttribute("name")

        if (rtcMode1ReferenceKeyName == "DIV1"):
            rtcMode1ReferenceDefaultValue = index

        rtcMode1ReferenceKeyDescription = rtcMode1ReferenceValues[index].getAttribute("caption")
        rtcMode1ReferenceKeyValue = rtcMode1ReferenceValues[index].getAttribute("value")
        rtcSymMode1_CTRLA_PRESCALER.addKey(rtcMode1ReferenceKeyName , rtcMode1ReferenceKeyValue , rtcMode1ReferenceKeyDescription)

    rtcSymMode1_CTRLA_PRESCALER.setDefaultValue(rtcMode1ReferenceDefaultValue)
    rtcSymMode1_CTRLA_PRESCALER.setOutputMode("Value")
    rtcSymMode1_CTRLA_PRESCALER.setDependencies(setrtcMode1PrescalerVisibleProperty,["RTC_MODULE_SELECTION"])

    #Periodic Interval Notification
    rtcSymMode1_PERIN = rtcComponent.createKeyValueSetSymbol("RTC_MODE1_PERIOD", rtcSymSubMenu)
    rtcSymMode1_PERIN.setLabel("Enable Periodic Interval Notification?")
    rtcSymMode1_PERIN.setVisible(False)
    rtcSymMode1_PERIN.addKey("NO","NO","NO")
    rtcSymMode1_PERIN.addKey("Generate 8 Cycles","PER0","Generate 8 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 16 Cycles","PER1","Generate 16 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 32 Cycles","PER2","Generate 32 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 64 Cycles","PER3","Generate 64 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 128 Cycles","PER4","Generate 128 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 256 Cycles","PER5","Generate 256 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 512 Cycles","PER6","Generate 512 Cycles")
    rtcSymMode1_PERIN.addKey("Generate 1024 Cycles","PER7","Generate 1024 Cycles")
    rtcSymMode1_PERIN.setDefaultValue(0)
    rtcSymMode1_PERIN.setOutputMode("Value")
    rtcSymMode1_PERIN.setDependencies(setrtcMode1PeriodNotificationVisibleProperty,["RTC_MODULE_SELECTION"])

    #Configure 16-Bit Timer Period
    rtcSymMode1_PER = rtcComponent.createHexSymbol("RTC_MODE1_TIMER_COUNTER_PERIOD",rtcSymSubMenu)
    rtcSymMode1_PER.setLabel("16-bit Timer Period")
    rtcSymMode1_PER.setVisible(False)
    rtcSymMode1_PER.setDefaultValue(0x0000)
    rtcSymMode1_PER.setMax(0xFFFF)
    rtcSymMode1_PER.setMin(0x0000)
    rtcSymMode1_PER.setDependencies(setrtcMode1TimerPeriodVisibleProperty,["RTC_MODULE_SELECTION"])

    #Configure Compare 0
    rtcSymMode1Config_CMP0 =  rtcComponent.createMenuSymbol("RTC_MODE1_COMPARE0_CONFIG",rtcSymSubMenu)
    rtcSymMode1Config_CMP0.setVisible(False)
    rtcSymMode1Config_CMP0.setLabel("Compare 0 Configure")
    rtcSymMode1Config_CMP0.setDependencies(setrtcMode1Compare0ConfigureVisibleProperty,["RTC_MODULE_SELECTION"])

    #Generate Compare 0 API
    rtcSymMode1_CMP0_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE1_GENERATE_COMPARE0_API",rtcSymMode1Config_CMP0)
    rtcSymMode1_CMP0_INTENSET.setVisible(False)
    rtcSymMode1_CMP0_INTENSET.setLabel("Generate Compare 0 API")
    rtcSymMode1_CMP0_INTENSET.setDependencies(setrtcMode1Compare0GenerateAPIVisisbleProperty,["RTC_MODULE_SELECTION"])

    #Compare 0 Match Value
    rtcSymMode1_CMP0 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE0_MATCH_VALUE",rtcSymMode1Config_CMP0)
    rtcSymMode1_CMP0.setVisible(False)
    rtcSymMode1_CMP0.setLabel("Compare 0 Value")
    rtcSymMode1_CMP0.setMax(0xFFFF)
    rtcSymMode1_CMP0.setMin(0x0000)
    rtcSymMode1_CMP0.setDefaultValue(0x0000)
    rtcSymMode1_CMP0.setDependencies(setrtcMode1Compare0MatchValueVisibleProperty,["RTC_MODULE_SELECTION"])

    #Ccnfigure Compare 1
    rtcSymMode1Config_CMP1 =  rtcComponent.createMenuSymbol("RTC_MODE1_COMPARE1_CONFIG",rtcSymSubMenu)
    rtcSymMode1Config_CMP1.setVisible(False)
    rtcSymMode1Config_CMP1.setLabel("Copmare 1 Configure")
    rtcSymMode1Config_CMP1.setDependencies(setrtcMode1Compare1ConfigureVisibleProperty,["RTC_MODULE_SELECTION"])

    #Generate Compare 1 API
    rtcSymMode1_CMP1_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE1_GENERATE_COMPARE1_API",rtcSymMode1Config_CMP1)
    rtcSymMode1_CMP1_INTENSET.setVisible(False)
    rtcSymMode1_CMP1_INTENSET.setLabel("Generate Compare 1 API")
    rtcSymMode1_CMP1_INTENSET.setDependencies(setrtcMode1Compare1GenerateAPIVisisbleProperty,["RTC_MODULE_SELECTION"])

    #Compare 1 Match Value
    rtcSymMode1_CMP1 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE1_MATCH_VALUE",rtcSymMode1Config_CMP1)
    rtcSymMode1_CMP1.setVisible(False)
    rtcSymMode1_CMP1.setLabel("Compare 1 Value")
    rtcSymMode1_CMP1.setMax(0xFFFF)
    rtcSymMode1_CMP1.setMin(0x0000)
    rtcSymMode1_CMP1.setDefaultValue(0x0000)
    rtcSymMode1_CMP1.setDependencies(setrtcMode1Compare1MatchValueVisibleProperty,["RTC_MODULE_SELECTION"])

    #Frequency Correction
    rtcSymMode1_FREQCORR = rtcComponent.createBooleanSymbol("RTC_MODE1_FREQCORR",rtcSymSubMenu)
    rtcSymMode1_FREQCORR.setVisible(False)
    rtcSymMode1_FREQCORR.setLabel("Generate Frequency Correction API")
    rtcSymMode1_FREQCORR.setDependencies(setrtcMode1FrequencyCorrectionVisibleProperty,["RTC_MODULE_SELECTION"])

#################################### MODE2 #####################################

    #Interrupt Enable Set
    rtcSymMode2_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE2_INTERRUPT", rtcSymSubMenu)
    rtcSymMode2_INTENSET.setLabel("Enable Interrupts?")
    rtcSymMode2_INTENSET.setVisible(False)
    rtcSymMode2_INTENSET.setDependencies(setrtcMode2InterruptVisibleProperty,["RTC_MODULE_SELECTION"])

    #Prescaler
    rtcSymMode2_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE2_PRESCALER", rtcSymSubMenu)
    rtcSymMode2_CTRLA_PRESCALER.setLabel("RTC Clock Source Divide-by Prescaler")
    rtcSymMode2_CTRLA_PRESCALER.setVisible(False)

    rtcMode2ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE2_CTRLA__PRESCALER\"]")
    rtcMode2ReferenceValues = []
    rtcMode2ReferenceValues = rtcMode2ReferenceNode.getChildren()

    rtcMode2ReferenceDefaultValue = 0

    for index in range(len(rtcMode2ReferenceValues)):
        rtcMode2ReferenceKeyName = rtcMode2ReferenceValues[index].getAttribute("name")

        if (rtcMode2ReferenceKeyName == "DIV1"):
            rtcMode2ReferenceDefaultValue = index

        rtcMode2ReferenceKeyDescription = rtcMode2ReferenceValues[index].getAttribute("caption")
        rtcMode2ReferenceKeyValue = rtcMode2ReferenceValues[index].getAttribute("value")
        rtcSymMode2_CTRLA_PRESCALER.addKey(rtcMode2ReferenceKeyName , rtcMode2ReferenceKeyValue , rtcMode2ReferenceKeyDescription)

    rtcSymMode2_CTRLA_PRESCALER.setDefaultValue(rtcMode2ReferenceDefaultValue)
    rtcSymMode2_CTRLA_PRESCALER.setOutputMode("Value")
    rtcSymMode2_CTRLA_PRESCALER.setDependencies(setrtcMode2PresaclerVisibleProperty,["RTC_MODULE_SELECTION"])

    #Periodic Interval Notification
    rtcSymMode2_PERIN = rtcComponent.createKeyValueSetSymbol("RTC_MODE2_PERIOD", rtcSymSubMenu)
    rtcSymMode2_PERIN.setLabel("Enable Periodic Interval Notification?")
    rtcSymMode2_PERIN.setVisible(False)
    rtcSymMode2_PERIN.addKey("NO","NO","NO")
    rtcSymMode2_PERIN.addKey("Generate 8 Cycles","PER0","Generate 8 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 16 Cycles","PER1","Generate 16 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 32 Cycles","PER2","Generate 32 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 64 Cycles","PER3","Generate 64 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 128 Cycles","PER4","Generate 128 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 256 Cycles","PER5","Generate 256 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 512 Cycles","PER6","Generate 512 Cycles")
    rtcSymMode2_PERIN.addKey("Generate 1024 Cycles","PER7","Generate 1024 Cycles")
    rtcSymMode2_PERIN.setDefaultValue(0)
    rtcSymMode2_PERIN.setOutputMode("Value")
    rtcSymMode2_PERIN.setDependencies(setrtcMode2PeriodNotificationVisibleProperty,["RTC_MODULE_SELECTION"])

    #Clock Representation
    rtcSymMode2_CTRLA_CLKREP = rtcComponent.createBooleanSymbol("RTC_MODE2_CLKREP", rtcSymSubMenu)
    rtcSymMode2_CTRLA_CLKREP.setLabel("12 or 24 Hour Format ?")
    rtcSymMode2_CTRLA_CLKREP.setVisible(False)
    rtcSymMode2_CTRLA_CLKREP.setDependencies(setrtcMode2ClkRepVisibleProperty,["RTC_MODULE_SELECTION"])

    #Reference Year
    rtcSymMode2_REFERENCE_YEAR = rtcComponent.createIntegerSymbol("RTC_MODE2_REFERENCE_YEAR",rtcSymSubMenu)
    rtcSymMode2_REFERENCE_YEAR.setVisible(False)
    rtcSymMode2_REFERENCE_YEAR.setLabel("Reference Year(Leap Year)")
    rtcSymMode2_REFERENCE_YEAR.setDefaultValue(2016)
    rtcSymMode2_REFERENCE_YEAR.setDependencies(setrtcMode2ReferenceYearVisibleProperty,["RTC_MODULE_SELECTION"])

    #Frequency Correction
    rtcSymMode2_FREQCORR = rtcComponent.createBooleanSymbol("RTC_MODE2_FREQCORR",rtcSymSubMenu)
    rtcSymMode2_FREQCORR.setLabel("Generate Frequency Correction API")
    rtcSymMode2_FREQCORR.setVisible(False)
    rtcSymMode2_FREQCORR.setDependencies(setrtcMode2FrequencyCorrectionVisibleProperty,["RTC_MODULE_SELECTION"])

################################ Code Generation ###############################

    configName = Variables.get("__CONFIGURATION_NAME")

    rtcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]")
    rtcModuleID = rtcModuleNode.getAttribute("id")

    # Instance Header File
    rtcHeaderFile = rtcComponent.createFileSymbol("RTC_INSTANCE_HEADER", None)
    rtcHeaderFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc.h.ftl")
    rtcHeaderFile.setOutputName("plib_rtc" + rtcInstanceIndex + ".h")
    rtcHeaderFile.setDestPath("/peripheral/rtc/")
    rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcHeaderFile.setType("HEADER")
    rtcHeaderFile.setMarkup(True)

    # RTC Timer Mode (MODE0 and MODE1) Source File
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc_timer.c.ftl")
    rtcSourceFile.setOutputName("plib_rtc" + rtcInstanceIndex + "_timer.c")
    rtcSourceFile.setDestPath("/peripheral/rtc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSourceFile.setType("SOURCE")
    rtcSourceFile.setMarkup(True)

    # RTC Clock Mode (MODE2) Source File
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_CLOCK_SOURCE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc_clock.c.ftl")
    rtcSourceFile.setOutputName("plib_rtc" + rtcInstanceIndex + "_clock.c")
    rtcSourceFile.setDestPath("/peripheral/rtc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSourceFile.setType("SOURCE")
    rtcSourceFile.setMarkup(True)
    rtcSourceFile.setEnabled(False)

    #System Initialization
    rtcSystemInitFile = rtcComponent.createFileSymbol("RTC_SYS_INIT", None)
    rtcSystemInitFile.setType("STRING")
    rtcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtcSystemInitFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/system/initialization.c.ftl")
    rtcSystemInitFile.setMarkup(True)

    # System Definition
    rtcSystemDefFile = rtcComponent.createFileSymbol("RTC_SYS_DEF", None)
    rtcSystemDefFile.setType("STRING")
    rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtcSystemDefFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/system/definitions.h.ftl")
    rtcSystemDefFile.setMarkup(True)