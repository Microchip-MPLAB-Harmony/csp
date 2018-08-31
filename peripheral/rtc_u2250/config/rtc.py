global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global rtcInstanceIndex

################################################################################
########                        Callback Functions                      ########
################################################################################

def setRTCInterruptData(status):
    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, status, 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if status == True:
        Database.setSymbolValue("core", InterruptHandler, "RTC" + rtcInstanceIndex + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "RTC_Handler", 2)

def updateRTCInterruptStatus(symbol, event):
    if event["id"] == "RTC_MODULE_SELECTION":
        rtcInterruptStatus = False
        rtcMode0 = (event["value"] == 0) and (rtcSymMode0_INTENSET.getValue() == True)
        rtcMode1 = (event["value"] == 1) and (rtcSymMode1_INTENSET.getValue() == True)
        rtcMode2 = (event["value"] == 2) and (rtcSymMode2_INTENSET.getValue() == True)

        if rtcMode0 == True or rtcMode1 == True or rtcMode2 == True:
            rtcInterruptStatus = True

        setRTCInterruptData(rtcInterruptStatus)
    else:
        setRTCInterruptData(event["value"])

def updateRTCInterruptWarringStatus(symbol, event):
    rtcMode0 = (rtcSymSubMenu.getValue() == 0) and (rtcSymMode0_INTENSET.getValue() == True)
    rtcMode1 = (rtcSymSubMenu.getValue() == 1) and (rtcSymMode1_INTENSET.getValue() == True)
    rtcMode2 = (rtcSymSubMenu.getValue() == 2) and (rtcSymMode2_INTENSET.getValue() == True)

    if rtcMode0 == True or rtcMode1 == True or rtcMode2 == True:
        symbol.setVisible(event["value"])

def updateRTCClockWarringStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#################################### MODE0 #####################################

global rtcMode0EvctrlMap
global rtcMode1EvctrlMap
global rtcMode2EvctrlMap

def Mode0Visible(symbol, event):
    if(event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode0Evctrl(symbol, event):
    global rtcMode0EvctrlMap
    mask = rtcMode0EvctrlMap.get(event["id"].split("RTC_MODE0_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else :
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

#################################### MODE1 #####################################

def Mode1Visible(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode1Evctrl(symbol, event):
    global rtcMode1EvctrlMap
    mask = rtcMode1EvctrlMap.get(event["id"].split("RTC_MODE1_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else :
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

#################################### MODE2 #####################################

def Mode2Visible(symbol, event):
    if(event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode2Evctrl(symbol, event):
    global rtcMode2EvctrlMap
    mask = rtcMode1EvctrlMap.get(event["id"].split("RTC_MODE2_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else :
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

########################## Code Generation Property ############################

#Update Code Generation Property
def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()
    if(event["value"] == 2):
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(True)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(False)
    else:
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(False)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(True)

################################################################################
########                   RTC DATABASE COMPONENTS                      ########
################################################################################

def instantiateComponent(rtcComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global rtcInstanceIndex
    global rtcMode0EvctrlMap
    global rtcMode1EvctrlMap
    global rtcMode2EvctrlMap
    global rtcSymSubMenu
    global rtcSymMode0_INTENSET
    global rtcSymMode1_INTENSET
    global rtcSymMode2_INTENSET

    rtcMode0EvctrlMap = {}
    rtcMode1EvctrlMap = {}
    rtcMode2EvctrlMap = {}
    rtcMode0EvctrlDep = []
    rtcMode1EvctrlDep = []
    rtcMode2EvctrlDep = []

    rtcInstanceIndex = rtcComponent.getID()[-1:]
    Log.writeInfoMessage("Running RTC : " + rtcInstanceIndex)

    rtcNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]')
    rtcValues = rtcNode.getChildren()

    #RTC Main Menu
    rtcSym_Menu = rtcComponent.createMenuSymbol("RTC_OPERATION_MODE",None)
    rtcSym_Menu.setLabel("Hardware Settings")

    #clock enable
    Database.clearSymbolValue("core", "RTC_CLOCK_ENABLE")
    Database.setSymbolValue("core", "RTC_CLOCK_ENABLE", True, 2)

    #Frequency Correction
    rtcSymMode0_FREQCORR = rtcComponent.createBooleanSymbol("RTC_FREQCORR",rtcSym_Menu)
    rtcSymMode0_FREQCORR.setLabel("Generate Frequency Correction API")

    #Sub Menu - RTC Modes: RTC_MODE0, RTC_MODE1, RTC_MODE2
    rtcSymSubMenu = rtcComponent.createKeyValueSetSymbol("RTC_MODULE_SELECTION", rtcSym_Menu)
    rtcSymSubMenu.setLabel("RTC Operation Mode")
    for index in range(0, len(rtcValues)):
        if rtcValues[index].getAttribute("qualifier") != None:
            rtcSymSubMenu.addKey(rtcValues[index].getAttribute("name"),rtcValues[index].getAttribute("value"),rtcValues[index].getAttribute("caption"))
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

    rtcSymMode0Menu = rtcComponent.createMenuSymbol("RTC_MODE0_MENU", rtcSymSubMenu)
    rtcSymMode0Menu.setLabel("RTC MODE 0 Configuration")
    rtcSymMode0Menu.setDependencies(Mode0Visible,["RTC_MODULE_SELECTION"])

    #Interrupt Enable Set
    rtcSymMode0_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE0_INTERRUPT", rtcSymMode0Menu)
    rtcSymMode0_INTENSET.setLabel("Enable Interrupts?")

    #Prescaler
    rtcSymMode0_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE0_PRESCALER", rtcSymMode0Menu)
    rtcSymMode0_CTRLA_PRESCALER.setLabel("RTC Prescaler")

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

    #Configure 32-Bit Timer Period
    rtcSymMode0_COMP0 = rtcComponent.createHexSymbol("RTC_MODE0_TIMER_COMPARE",rtcSymMode0Menu)
    rtcSymMode0_COMP0.setLabel("Compare Value")
    rtcSymMode0_COMP0.setDefaultValue(0x00000000)
    rtcSymMode0_COMP0.setMax(0xFFFFFFFF)
    rtcSymMode0_COMP0.setMin(0x00000000)

    #Interrupt Enable Set
    rtcSymMode0_Matcclr = rtcComponent.createBooleanSymbol("RTC_MODE0_MATCHCLR", rtcSymMode0Menu)
    rtcSymMode0_Matcclr.setLabel("Clear on compare Match")

    rtcSymMode0Events = rtcComponent.createMenuSymbol("RTC_MODE0_EVCTRL_MENU",rtcSymMode0Menu)
    rtcSymMode0Events.setLabel("RTC EVENTS configuration")

    rtcEventsNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE0",name="EVCTRL"]')
    rtcEventsValues = rtcEventsNode.getChildren()

    for i in range(0,len(rtcEventsValues)):
        rtcSymMode0_Event = rtcComponent.createBooleanSymbol("RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE", rtcSymMode0Events)
        rtcSymMode0_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode0EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode0EvctrlDep.append("RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")

    #Periodic Interval Notification
    rtcSymMode0_PERIN = rtcComponent.createHexSymbol("RTC_MODE0_EVCTRL", rtcSymMode0Menu)
    rtcSymMode0_PERIN.setDefaultValue(0)
    rtcSymMode0_PERIN.setVisible(False)
    rtcSymMode0_PERIN.setDependencies(rtcMode0Evctrl, rtcMode0EvctrlDep)

#################################### MODE1 #####################################

    rtcSymMode1Menu = rtcComponent.createMenuSymbol("RTC_MODE1_MENU", rtcSymSubMenu)
    rtcSymMode1Menu.setLabel("RTC MODE 1 Configuration")
    rtcSymMode1Menu.setVisible(False)
    rtcSymMode1Menu.setDependencies(Mode1Visible,["RTC_MODULE_SELECTION"])

    #Configure the RTC Interrupts
    rtcSymMode1_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE1_INTERRUPT", rtcSymMode1Menu)
    rtcSymMode1_INTENSET.setLabel("Enable Interrupts?")

    #Prescaler
    rtcSymMode1_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE1_PRESCALER", rtcSymMode1Menu)
    rtcSymMode1_CTRLA_PRESCALER.setLabel("RTC Prescaler")

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

    #Configure 16-Bit Timer Period
    rtcSymMode1_PER = rtcComponent.createHexSymbol("RTC_MODE1_TIMER_COUNTER_PERIOD",rtcSymMode1Menu)
    rtcSymMode1_PER.setLabel("16-bit Timer Period")
    rtcSymMode1_PER.setDefaultValue(0x0000)
    rtcSymMode1_PER.setMax(0xFFFF)
    rtcSymMode1_PER.setMin(0x0000)

    #Compare 0 Match Value
    rtcSymMode1_CMP0 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE0_MATCH_VALUE",rtcSymMode1Menu)
    rtcSymMode1_CMP0.setLabel("Compare 0 Value")
    rtcSymMode1_CMP0.setMax(0xFFFF)
    rtcSymMode1_CMP0.setMin(0x0000)
    rtcSymMode1_CMP0.setDefaultValue(0x0000)

    #Compare 1 Match Value
    rtcSymMode1_CMP1 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE1_MATCH_VALUE",rtcSymMode1Menu)
    rtcSymMode1_CMP1.setLabel("Compare 1 Value")
    rtcSymMode1_CMP1.setMax(0xFFFF)
    rtcSymMode1_CMP1.setMin(0x0000)
    rtcSymMode1_CMP1.setDefaultValue(0x0000)

    rtcSymMode1Events = rtcComponent.createMenuSymbol("RTC_MODE1_EVCTRL_MENU",rtcSymMode1Menu)
    rtcSymMode1Events.setLabel("RTC EVENTS configuration")

    rtcEventsNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE1",name="EVCTRL"]')
    rtcEventsValues = rtcEventsNode.getChildren()

    for i in range(0,len(rtcEventsValues)):
        rtcSymMode1_Event = rtcComponent.createBooleanSymbol("RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE", rtcSymMode1Events)
        rtcSymMode1_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode1EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode1EvctrlDep.append("RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")

    #Periodic Interval Notification
    rtcSymMode1_PERIN = rtcComponent.createHexSymbol("RTC_MODE1_EVCTRL", rtcSymMode1Menu)
    rtcSymMode1_PERIN.setDefaultValue(0)
    rtcSymMode1_PERIN.setVisible(False)
    rtcSymMode1_PERIN.setDependencies(rtcMode1Evctrl, rtcMode1EvctrlDep)

#################################### MODE2 #####################################

    rtcSymMode2Menu = rtcComponent.createMenuSymbol("RTC_MODE2_MENU", rtcSymSubMenu)
    rtcSymMode2Menu.setLabel("RTC MODE 2 Configuration")
    rtcSymMode2Menu.setVisible(False)
    rtcSymMode2Menu.setDependencies(Mode2Visible,["RTC_MODULE_SELECTION"])

    #Interrupt Enable Set
    rtcSymMode2_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE2_INTERRUPT", rtcSymMode2Menu)
    rtcSymMode2_INTENSET.setLabel("Enable Interrupts?")

    #Prescaler
    rtcSymMode2_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE2_PRESCALER", rtcSymMode2Menu)
    rtcSymMode2_CTRLA_PRESCALER.setLabel("RTC Prescaler")

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

    #Reference Year
    rtcSymMode2_REFERENCE_YEAR = rtcComponent.createIntegerSymbol("RTC_MODE2_REFERENCE_YEAR",rtcSymMode2Menu)
    rtcSymMode2_REFERENCE_YEAR.setLabel("Reference Year(Leap Year)")
    rtcSymMode2_REFERENCE_YEAR.setDefaultValue(2016)

    rtcSymMode2Events = rtcComponent.createMenuSymbol("RTC_MODE2_EVCTRL_MENU",rtcSymMode2Menu)
    rtcSymMode2Events.setLabel("RTC EVENTS configuration")

    rtcEventsNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE2",name="EVCTRL"]')
    rtcEventsValues = rtcEventsNode.getChildren()

    for i in range(0,len(rtcEventsValues)):
        rtcSymMode2_Event = rtcComponent.createBooleanSymbol("RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE", rtcSymMode2Events)
        rtcSymMode2_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode2EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode2EvctrlDep.append("RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")

    #Periodic Interval Notification
    rtcSymMode2_PERIN = rtcComponent.createHexSymbol("RTC_MODE2_EVCTRL", rtcSymMode2Menu)
    rtcSymMode2_PERIN.setDefaultValue(0)
    rtcSymMode2_PERIN.setVisible(False)
    rtcSymMode2_PERIN.setDependencies(rtcMode2Evctrl, rtcMode2EvctrlDep)

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = "RTC_INTERRUPT_ENABLE"
    InterruptHandler = "RTC_INTERRUPT_HANDLER"
    InterruptHandlerLock = "RTC_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = "RTC_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    rtcSym_UpdateInterruptStatus = rtcComponent.createBooleanSymbol("RTC_INTERRUPT_STATUS", None)
    rtcSym_UpdateInterruptStatus.setDependencies(updateRTCInterruptStatus, ["RTC_MODULE_SELECTION", "RTC_MODE0_INTERRUPT", "RTC_MODE1_INTERRUPT", "RTC_MODE2_INTERRUPT"])
    rtcSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    rtcSym_IntEnComment = rtcComponent.createCommentSymbol("RTC_INTERRUPT_ENABLE_COMMENT", None)
    rtcSym_IntEnComment.setVisible(False)
    rtcSym_IntEnComment.setLabel("Warning!!! RTC" + rtcInstanceIndex + " Interrupt is Disabled in Interrupt Manager")
    rtcSym_IntEnComment.setDependencies(updateRTCInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    rtcSym_ClkEnComment = rtcComponent.createCommentSymbol("RTC_CLOCK_ENABLE_COMMENT", None)
    rtcSym_ClkEnComment.setLabel("Warning!!! RTC Peripheral Clock is Disabled in Clock Manager")
    rtcSym_ClkEnComment.setVisible(False)
    rtcSym_ClkEnComment.setDependencies(updateRTCClockWarringStatus, ["core.RTC_CLOCK_ENABLE"])

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
    rtcSource1File = rtcComponent.createFileSymbol("RTC_CLOCK_SOURCE", None)
    rtcSource1File.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc_clock.c.ftl")
    rtcSource1File.setOutputName("plib_rtc" + rtcInstanceIndex + "_clock.c")
    rtcSource1File.setDestPath("/peripheral/rtc/")
    rtcSource1File.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSource1File.setType("SOURCE")
    rtcSource1File.setMarkup(True)
    rtcSource1File.setEnabled(False)

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
