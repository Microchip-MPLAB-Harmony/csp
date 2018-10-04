# coding: utf-8
"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global rtcInstanceName

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
        Database.setSymbolValue("core", InterruptHandler, rtcInstanceName.getValue() + "_InterruptHandler", 2)
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
    rtcMode0 = (rtcModeSelection_Sym.getValue() == 0) and (rtcSymMode0_INTENSET.getValue() == True)
    rtcMode1 = (rtcModeSelection_Sym.getValue() == 1) and (rtcSymMode1_INTENSET.getValue() == True)
    rtcMode2 = (rtcModeSelection_Sym.getValue() == 2) and (rtcSymMode2_INTENSET.getValue() == True)

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
    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode0Evctrl(symbol, event):
    global rtcMode0EvctrlMap
    mask = rtcMode0EvctrlMap.get(event["id"].split("RTC_MODE0_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

#################################### MODE1 #####################################

def Mode1Visible(symbol, event):
    if event["value"] == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode1Evctrl(symbol, event):
    global rtcMode1EvctrlMap
    mask = rtcMode1EvctrlMap.get(event["id"].split("RTC_MODE1_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

#################################### MODE2 #####################################

def Mode2Visible(symbol, event):
    if event["value"] == 2:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def rtcMode2Evctrl(symbol, event):
    global rtcMode2EvctrlMap
    mask = rtcMode1EvctrlMap.get(event["id"].split("RTC_MODE2_EVCTRL_")[1].split("_ENABLE")[0])
    print mask
    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

########################## Code Generation Property ############################

#Update Code Generation Property
def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()
    if event["value"] == 2:
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(True)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(False)
    else:
        component.getSymbolByID("RTC_CLOCK_SOURCE").setEnabled(False)
        component.getSymbolByID("RTC_TIMER_SOURCE").setEnabled(True)

def onCapabilityConnected(connectionInfo):
    global rtcModeSelection_Sym

    remoteComponent = connectionInfo["remoteComponent"]
    if (remoteComponent.getID() == "sys_time"):
        rtcModeSelection_Sym.setSelectedKey("MODE0",1)

def sysTime_modeSelection(symbol,event):
    global timerStartApiName_Sym
    global timeStopApiName_Sym
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global frequencyGetApiName_Sym
    global callbackApiName_Sym
    global irqEnumName_Sym
    global timerWidth_Sym
    global timerPeriodMax_Sym
    global rtcInstanceName

    symObj = event["symbol"]
    rtcMode = symObj.getSelectedKey()

    irqEnumName = "RTC_IRQn"

    if rtcMode == "MODE0":
        #32-bit counter
        periodSetApiName = ""
        periodSetApiName_Sym.setValue(periodSetApiName,2)
        timerWidth_Sym.setValue(32,2)
        timerPeriodMax_Sym.setValue("0xFFFFFFFF",2)
        timerStartApiName = rtcInstanceName.getValue() + "_Timer32Start"
        timeStopApiName = rtcInstanceName.getValue() + "_Timer32Stop"
        compareSetApiName = rtcInstanceName.getValue() + "_Timer32CompareSet"
        counterGetApiName = rtcInstanceName.getValue() + "_Timer32CounterGet"
        frequencyGetApiName = rtcInstanceName.getValue() + "_Timer32FrequencyGet"
        callbackApiName = rtcInstanceName.getValue() + "_Timer32CallbackRegister"
    elif rtcMode == "MODE1":
        #16-bit counter
        periodSetApiName = rtcInstanceName.getValue() + "_Timer16PeriodSet"
        periodSetApiName_Sym.setValue(periodSetApiName,2)
        timerWidth_Sym.setValue(16,2)
        timerPeriodMax_Sym.setValue("0xFFFF",2)
        timerStartApiName = rtcInstanceName.getValue() + "_Timer16Start"
        timeStopApiName = rtcInstanceName.getValue() + "_Timer16Stop"
        compareSetApiName = rtcInstanceName.getValue() + "_Timer16Compare0Set"
        counterGetApiName = rtcInstanceName.getValue() + "_Timer16CounterGet"
        frequencyGetApiName = rtcInstanceName.getValue() + "_Timer16FrequencyGet"
        callbackApiName = rtcInstanceName.getValue() + "_Timer16CallbackRegister"

    if rtcMode != "MODE2":
        timerStartApiName_Sym.setValue(timerStartApiName,2)
        timeStopApiName_Sym.setValue(timeStopApiName,2)
        compareSetApiName_Sym.setValue(compareSetApiName,2)
        counterApiName_Sym.setValue(counterGetApiName,2)
        frequencyGetApiName_Sym.setValue(frequencyGetApiName,2)
        callbackApiName_Sym.setValue(callbackApiName,2)
        irqEnumName_Sym.setValue(irqEnumName,2)

################################################################################
########                   RTC DATABASE COMPONENTS                      ########
################################################################################

def instantiateComponent(rtcComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global rtcInstanceName
    global timerStartApiName_Sym
    global timeStopApiName_Sym
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global frequencyGetApiName_Sym
    global callbackApiName_Sym
    global irqEnumName_Sym
    global timerWidth_Sym
    global timerPeriodMax_Sym
    global rtcModeSelection_Sym
    global rtcMode0EvctrlMap
    global rtcMode1EvctrlMap
    global rtcMode2EvctrlMap
    global rtcModeSelection_Sym
    global rtcSymMode0_INTENSET
    global rtcSymMode1_INTENSET
    global rtcSymMode2_INTENSET

    rtcMode0EvctrlMap = {}
    rtcMode1EvctrlMap = {}
    rtcMode2EvctrlMap = {}
    rtcMode0EvctrlDep = []
    rtcMode1EvctrlDep = []
    rtcMode2EvctrlDep = []

    rtcInstanceName = rtcComponent.createStringSymbol("RTC_INSTANCE_NAME", None)
    rtcInstanceName.setVisible(False)
    rtcInstanceName.setDefaultValue(rtcComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtcInstanceName.getValue())

    rtcNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]')
    rtcValues = rtcNode.getChildren()

    #RTC Main Menu
    rtcSym_Menu = rtcComponent.createMenuSymbol("RTC_OPERATION_MODE",None)
    rtcSym_Menu.setLabel("Hardware Settings")

    #clock enable
    Database.clearSymbolValue("core", rtcInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", rtcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    #Frequency Correction
    sysTimeTrigger_Sym = rtcComponent.createBooleanSymbol("SYS_TIME", None)
    sysTimeTrigger_Sym.setVisible(False)
    sysTimeTrigger_Sym.setDependencies(sysTime_modeSelection, ["RTC_MODULE_SELECTION"])

#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------
    timerWidth_Sym = rtcComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)

    timerPeriodMax_Sym = rtcComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)

    timerStartApiName_Sym = rtcComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)

    timeStopApiName_Sym = rtcComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)

    compareSetApiName_Sym = rtcComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiName_Sym.setVisible(False)

    periodSetApiName_Sym = rtcComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)

    counterApiName_Sym = rtcComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)

    frequencyGetApiName_Sym = rtcComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)

    callbackApiName_Sym = rtcComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)

    irqEnumName_Sym = rtcComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
#------------------------------------------------------------
    #Frequency Correction
    rtcSymMode0_FREQCORR = rtcComponent.createBooleanSymbol("RTC_FREQCORR",rtcSym_Menu)
    rtcSymMode0_FREQCORR.setLabel("Generate Frequency Correction API")

    #Sub Menu - RTC Modes: RTC_MODE0, RTC_MODE1, RTC_MODE2
    rtcModeSelection_Sym = rtcComponent.createKeyValueSetSymbol("RTC_MODULE_SELECTION", rtcSym_Menu)
    rtcModeSelection_Sym.setLabel("RTC Operation Mode")
    for index in range(0, len(rtcValues)):
        if rtcValues[index].getAttribute("qualifier") != None:
            rtcModeSelection_Sym.addKey(rtcValues[index].getAttribute("name"),rtcValues[index].getAttribute("value"),rtcValues[index].getAttribute("caption"))
    rtcModeSelection_Sym.setDefaultValue(0)
    rtcModeSelection_Sym.setOutputMode("Key")
    rtcModeSelection_Sym.setDisplayMode("Description")


#################################### MODE0 #####################################

    rtcSymMode0Menu = rtcComponent.createMenuSymbol("RTC_MODE0_MENU", rtcModeSelection_Sym)
    rtcSymMode0Menu.setLabel("RTC MODE 0 Configuration")
    rtcSymMode0Menu.setDependencies(Mode0Visible,["RTC_MODULE_SELECTION"])

    #Interrupt Enable Set
    rtcSymMode0_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE0_INTERRUPT", rtcSymMode0Menu)
    rtcSymMode0_INTENSET.setLabel("Enable Interrupts?")
    rtcSymMode0_INTENSET.setDefaultValue(True)
    setRTCInterruptData(True)

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
    rtcSymMode1Menu = rtcComponent.createMenuSymbol("RTC_MODE1_MENU", rtcModeSelection_Sym)
    rtcSymMode1Menu.setLabel("RTC MODE 1 Configuration")
    rtcSymMode1Menu.setVisible(False)
    rtcSymMode1Menu.setDependencies(Mode1Visible,["RTC_MODULE_SELECTION"])

    #Configure the RTC Interrupts
    rtcSymMode1_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE1_INTERRUPT", rtcSymMode1Menu)
    rtcSymMode1_INTENSET.setLabel("Enable Interrupts?")
    rtcSymMode1_INTENSET.setDefaultValue(True)

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
    rtcSymMode2Menu = rtcComponent.createMenuSymbol("RTC_MODE2_MENU", rtcModeSelection_Sym)
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

    InterruptVector = rtcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = rtcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    rtcSym_UpdateInterruptStatus = rtcComponent.createBooleanSymbol("RTC_INTERRUPT_STATUS", None)
    rtcSym_UpdateInterruptStatus.setDependencies(updateRTCInterruptStatus, ["RTC_MODULE_SELECTION", "RTC_MODE0_INTERRUPT", "RTC_MODE1_INTERRUPT", "RTC_MODE2_INTERRUPT"])
    rtcSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    rtcSym_IntEnComment = rtcComponent.createCommentSymbol("RTC_INTERRUPT_ENABLE_COMMENT", None)
    rtcSym_IntEnComment.setVisible(False)
    rtcSym_IntEnComment.setLabel("Warning!!! " + rtcInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    rtcSym_IntEnComment.setDependencies(updateRTCInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    rtcSym_ClkEnComment = rtcComponent.createCommentSymbol("RTC_CLOCK_ENABLE_COMMENT", None)
    rtcSym_ClkEnComment.setLabel("Warning!!! RTC Peripheral Clock is Disabled in Clock Manager")
    rtcSym_ClkEnComment.setVisible(False)
    rtcSym_ClkEnComment.setDependencies(updateRTCClockWarringStatus, ["core."+rtcInstanceName.getValue()+"_CLOCK_ENABLE"])

################################ Code Generation ###############################

    configName = Variables.get("__CONFIGURATION_NAME")

    rtcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]")
    rtcModuleID = rtcModuleNode.getAttribute("id")

    # Instance Header File
    rtcHeaderFile = rtcComponent.createFileSymbol("RTC_INSTANCE_HEADER", None)
    rtcHeaderFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc.h.ftl")
    rtcHeaderFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".h")
    rtcHeaderFile.setDestPath("/peripheral/rtc/")
    rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcHeaderFile.setType("HEADER")
    rtcHeaderFile.setMarkup(True)

    # RTC Timer Mode (MODE0 and MODE1) Source File
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc_timer.c.ftl")
    rtcSourceFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+"_timer.c")
    rtcSourceFile.setDestPath("/peripheral/rtc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSourceFile.setType("SOURCE")
    rtcSourceFile.setMarkup(True)

    # RTC Clock Mode (MODE2) Source File
    rtcSource1File = rtcComponent.createFileSymbol("RTC_CLOCK_SOURCE", None)
    rtcSource1File.setSourcePath("../peripheral/rtc_"+ rtcModuleID +"/templates/plib_rtc_clock.c.ftl")
    rtcSource1File.setOutputName("plib_"+rtcInstanceName.getValue().lower()+"_clock.c")
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
