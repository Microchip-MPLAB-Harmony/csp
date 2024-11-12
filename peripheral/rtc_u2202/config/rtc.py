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
from collections import defaultdict

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global rtcInstanceName
global eventMap
global eventMapInverse

################################################################################
########                        Callback Functions                      ########
################################################################################

def sysTimeCalendarModeCommentVisibility(symbol, event):
    global sysTimeComponentId
    global rtcModeSelection_Sym
    messageDict = {"isVisible" : "", "message" : ""}

    #Hide/Un-hide the comment in PLIB and also send a message to the SYS Time module to display similar comment
    if ((sysTimeComponentId.getValue() != "") and (rtcModeSelection_Sym.getSelectedKey() == "MODE2")):
        symbol.setVisible(True)
        messageDict["isVisible"] = "True"
        messageDict["message"] = symbol.getLabel()
        messageDict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_NOT_SUPPORTED", messageDict)
    else:
        symbol.setVisible(False)
        messageDict["isVisible"] = "False"
        messageDict["message"] = ""
        messageDict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_NOT_SUPPORTED", messageDict)

def setSysTimeConfiguration(rtcOperationMode, sysTimeOperationMode):
    if sysTimeComponentId.getValue() != "":
        if rtcOperationMode == "MODE0":
            if sysTimeOperationMode == "SYS_TIME_PLIB_MODE_COMPARE":
                Database.setSymbolValue("rtc", "RTC_MODE0_INTENSET_CMP0_ENABLE", True)
                Database.setSymbolValue("rtc", "RTC_MODE0_MATCHCLR", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_TIMER_COMPARE", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_CMP0_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_OVF_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE1_COMPARE0_MATCH_VALUE", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE1_TIMER_COUNTER_PERIOD", long(0))
            elif sysTimeOperationMode == "SYS_TIME_PLIB_MODE_PERIOD":
                Database.setSymbolValue("rtc", "RTC_MODE0_INTENSET_CMP0_ENABLE", True)
                Database.setSymbolValue("rtc", "RTC_MODE0_MATCHCLR", True)
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_CMP0_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_OVF_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE1_COMPARE0_MATCH_VALUE", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE1_TIMER_COUNTER_PERIOD", long(0))
                calcSysTimeCompareVal(rtcOperationMode)
        elif rtcOperationMode == "MODE1":
            if sysTimeOperationMode == "SYS_TIME_PLIB_MODE_COMPARE":
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_CMP0_ENABLE", True)
                Database.setSymbolValue("rtc", "RTC_MODE1_COMPARE0_MATCH_VALUE", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE1_TIMER_COUNTER_PERIOD", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_OVF_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE1_TIMER_COUNTER_PERIOD", long(0))
                Database.setSymbolValue("rtc", "RTC_MODE0_INTENSET_CMP0_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_MATCHCLR", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_TIMER_COMPARE", long(0))
            elif sysTimeOperationMode == "SYS_TIME_PLIB_MODE_PERIOD":
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_OVF_ENABLE", True)
                Database.setSymbolValue("rtc", "RTC_MODE1_INTENSET_CMP0_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_INTENSET_CMP0_ENABLE", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_MATCHCLR", False)
                Database.setSymbolValue("rtc", "RTC_MODE0_TIMER_COMPARE", long(0))
                calcSysTimeCompareVal(rtcOperationMode)


def calcSysTimeCompareVal(rtcOperationMode):
    global sysTimeComponentId
    global sysTimeTickRateMs
    tickRateDict = {"tick_rate_hz": 0}
    dummy_dict = dict()
    periodVal = 0
    if ((sysTimeComponentId.getValue() != "") and (sysTimePlibMode.getValue() == "SYS_TIME_PLIB_MODE_PERIOD")):
        #Get the RTC clock frequency
        rtcClockFrequency = Database.getSymbolValue("core", "RTC_CLOCK_FREQUENCY")
        if rtcOperationMode == "MODE0":
            #Get the RTC prescaler
            rtcPrescaler = Database.getSymbolValue("rtc", "RTC_MODE0_PRESCALER")
            if rtcPrescaler >= 1:
                #Calculate the RTC input clock
                rtcClockFrequency = rtcClockFrequency / (2**(rtcPrescaler))
            newCompareValue = long(rtcClockFrequency * (sysTimeTickRateMs.getValue() / 1000))
            if newCompareValue > 0xFFFFFFFF:
                newCompareValue = 0xFFFFFFFF
            if newCompareValue >=1:
                newCompareValue -= 1
            if newCompareValue == 0:
                newCompareValue = 1
            Database.setSymbolValue("rtc", "RTC_MODE0_TIMER_COMPARE", long(newCompareValue))
            periodVal = newCompareValue + 1
        elif rtcOperationMode == "MODE1":
            #Get the RTC prescaler
            rtcPrescaler = Database.getSymbolValue("rtc", "RTC_MODE1_PRESCALER")
            if rtcPrescaler >= 1:
                #Calculate the RTC input clock
                rtcClockFrequency = rtcClockFrequency / (2**(rtcPrescaler))
            newPeriodValue = long(rtcClockFrequency * (sysTimeTickRateMs.getValue() / 1000))
            if newPeriodValue > 0xFFFF:
                newPeriodValue = 0xFFFF
            if newPeriodValue >=1:
                newPeriodValue -= 1
            if newPeriodValue == 0:
                newPeriodValue = 1
            Database.setSymbolValue("rtc", "RTC_MODE1_TIMER_COUNTER_PERIOD", long(newPeriodValue))
            periodVal = newPeriodValue + 1
        if ((rtcOperationMode == "MODE0") or (rtcOperationMode == "MODE1")):
            achievableTickRateHz = float(1.0/float(rtcClockFrequency)) * long(periodVal)
            achievableTickRateHz = (1.0/achievableTickRateHz) * 100000.0
            tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
            dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

def rtcPrescalerChangeHandler(symbol, event):
    global rtcModeSelection_Sym
    calcSysTimeCompareVal(rtcModeSelection_Sym.getSelectedKey())

def handleMessage(messageID, args):
    global sysTimePlibMode
    global sysTimeComponentId
    global rtcModeSelection_Sym
    global sysTimeTickRateMs
    dummy_dict = dict()
    sysTimePLIBConfig = dict()

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        modeDict = {"plib_mode": "PERIOD_AND_COMPARE_MODES"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        sysTimePlibMode.setValue(sysTimePLIBConfig["plib_mode"])
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            sysTimeTickRateMs.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

        if(rtcModeSelection_Sym.getSelectedKey() == "MODE2"):
            rtcModeSelection_Sym.setReadOnly(True)
            rtcModeSelection_Sym.setSelectedKey("MODE0", 1)
            rtcModeSelection_Sym.setReadOnly(False)

        setSysTimeConfiguration(rtcModeSelection_Sym.getSelectedKey(), sysTimePlibMode.getValue())

    if ((messageID == "SYS_TIME_PLIB_MODE_COMPARE") or (messageID == "SYS_TIME_PLIB_MODE_PERIOD")):
        sysTimePlibMode.setValue(messageID)
        setSysTimeConfiguration(rtcModeSelection_Sym.getSelectedKey(), sysTimePlibMode.getValue())

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        sysTimeTickRateMs.setValue(args["sys_time_tick_ms"])
        calcSysTimeCompareVal(rtcModeSelection_Sym.getSelectedKey())

    return dummy_dict

def evsysSetup(symbol, event):
    global eventMap

    if event["id"] == "RTC_MODULE_SELECTION" :
        selection = Database.getSymbolValue(event["namespace"], "RTC_MODULE_SELECTION")
        selection = "MODE" + str(selection)

        for value in eventMap.keys():
            if locals()['selection'] in value:
                status = Database.getSymbolValue(event["namespace"], value)
                Database.setSymbolValue("evsys", eventMap.get(value), status, 2)
    else:
        Database.setSymbolValue("evsys", eventMap.get(event["id"]), event["value"], 2)

def setRTCInterruptData(status):
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock

    Database.setSymbolValue("core", InterruptVector, status, 2)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 2)

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

def rtcMode0Interrupt(symbol, event):
    global rtcMode0InterruptMap
    mask = rtcMode0InterruptMap.get(event["id"].split("RTC_MODE0_INTENSET_")[1].split("_ENABLE")[0])

    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

def rtcMode0Evctrl(symbol, event):
    global rtcMode0EvctrlMap
    mask = rtcMode0EvctrlMap.get(event["id"].split("RTC_MODE0_EVCTRL_")[1].split("_ENABLE")[0])

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

def rtcMode1Interrupt(symbol, event):
    global rtcMode1InterruptMap
    mask = rtcMode1InterruptMap.get(event["id"].split("RTC_MODE1_INTENSET_")[1].split("_ENABLE")[0])

    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

def rtcMode1Evctrl(symbol, event):
    global rtcMode1EvctrlMap
    mask = rtcMode1EvctrlMap.get(event["id"].split("RTC_MODE1_EVCTRL_")[1].split("_ENABLE")[0])

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

def rtcMode2Interrupt(symbol, event):
    global rtcMode2InterruptMap
    mask = rtcMode2InterruptMap.get(event["id"].split("RTC_MODE2_INTENSET_")[1].split("_ENABLE")[0])

    if event["value"]:
        value = symbol.getValue() | int(mask, 16)
    else:
        value = symbol.getValue() & ~(int(mask, 16))

    symbol.setValue(value, 1)

def rtcMode2Evctrl(symbol, event):
    global rtcMode2EvctrlMap
    mask = rtcMode2EvctrlMap.get(event["id"].split("RTC_MODE2_EVCTRL_")[1].split("_ENABLE")[0])

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

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    localID = localComponent.getID()
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

def onAttachmentDisconnected(source, target):
    global sysTimeComponentId

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

    if remoteID == "sys_time":
        #Reset the remote component ID to NULL
        sysTimeComponentId.setValue("")
        localComponent.getSymbolByID("RTC_MODE0_INTENSET_CMP0_ENABLE").setValue(False)
        localComponent.getSymbolByID("RTC_MODE0_MATCHCLR").setValue(False)
        localComponent.getSymbolByID("RTC_MODE0_TIMER_COMPARE").setValue(long(0))
        localComponent.getSymbolByID("RTC_MODE1_INTENSET_CMP0_ENABLE").setValue(False)
        localComponent.getSymbolByID("RTC_MODE1_INTENSET_OVF_ENABLE").setValue(False)
        localComponent.getSymbolByID("RTC_MODE1_COMPARE0_MATCH_VALUE").setValue(long(0))
        localComponent.getSymbolByID("RTC_MODE1_TIMER_COUNTER_PERIOD").setValue(long(0))
        localComponent.getSymbolByID("SYS_TIME_CALENDAR_MODE_NOT_SUPPORTED_COMMENT").setVisible(False)

def sysTime_updateOnModeChange(rtcMode):
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
    global sysTimePlibMode

    irqEnumName = "RTC_IRQn"

    if rtcMode == "MODE0":
        #32-bit counter
        setSysTimeConfiguration(rtcMode, sysTimePlibMode.getValue())
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
        setSysTimeConfiguration(rtcMode, sysTimePlibMode.getValue())
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

def sysTime_modeSelection(symbol, event):
    symObj = event["symbol"]
    rtcMode = symObj.getSelectedKey()
    sysTime_updateOnModeChange(rtcMode)


################################################################################
########                   RTC DATABASE COMPONENTS                      ########
################################################################################

def instantiateComponent(rtcComponent):
    global eventMap
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
    global rtcMode0InterruptMap
    global rtcMode1InterruptMap
    global rtcMode2InterruptMap
    global rtcModeSelection_Sym
    global rtcMode0EvctrlMap
    global rtcMode1EvctrlMap
    global rtcMode2EvctrlMap
    global rtcModeSelection_Sym
    global rtcSymMode0_INTENSET
    global rtcSymMode1_INTENSET
    global rtcSymMode2_INTENSET
    global evsysDep
    global sysTimeComponentId
    global rtcSymMode0_CTRLA_PRESCALER
    global sysTimePlibMode
    global sysTimeTickRateMs

    rtcMode0InterruptMap = {}
    rtcMode1InterruptMap = {}
    rtcMode2InterruptMap = {}
    rtcMode0EvctrlMap = {}
    rtcMode1EvctrlMap = {}
    rtcMode2EvctrlMap = {}
    rtcMode0InterruptDep = []
    rtcMode1InterruptDep = []
    rtcMode2InterruptDep = []
    rtcMode0EvctrlDep = []
    rtcMode1EvctrlDep = []
    rtcMode2EvctrlDep = []
    evsysDep = []
    eventMap = defaultdict(list)

    generatorsNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators")
    generatorsValue = generatorsNode.getChildren()
    for id in range(0,len(generatorsValue)):
        if generatorsValue[id].getAttribute("module-instance") == "RTC":
            eventMap[generatorsValue[id].getAttribute("name")] = []

    rtcInstanceName = rtcComponent.createStringSymbol("RTC_INSTANCE_NAME", None)
    rtcInstanceName.setVisible(False)
    rtcInstanceName.setDefaultValue(rtcComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtcInstanceName.getValue())

    InterruptVector = rtcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = rtcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    rtcNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]')
    rtcValues = rtcNode.getChildren()

    #RTC Main Menu
    rtcSym_Menu = rtcComponent.createMenuSymbol("RTC_OPERATION_MODE",None)
    rtcSym_Menu.setLabel("Hardware Settings")

    #clock enable
    Database.clearSymbolValue("core", rtcInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", rtcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------

    sysTimeComponentId = rtcComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")

    sysTimePlibMode = rtcComponent.createStringSymbol("SYS_TIME_PLIB_OPERATION_MODE", None)
    sysTimePlibMode.setLabel("SysTime PLIB Operation Mode")
    sysTimePlibMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    sysTimePlibMode.setVisible(False)
    sysTimePlibMode.setDefaultValue("")

    sysTimeTickRateMs = rtcComponent.createFloatSymbol("SYS_TIME_TICK_RATE_MS", None)
    sysTimeTickRateMs.setDefaultValue(1)
    sysTimeTickRateMs.setVisible(False)

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
    rtcSymMode0_FREQCORR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:FREQCORR")
    rtcSymMode0_FREQCORR.setLabel("Generate Frequency Correction API")

    rtcCount_ReadContinuously = rtcComponent.createBooleanSymbol("RTC_COUNT_CLOCK_RCONT",rtcSym_Menu)
    rtcCount_ReadContinuously.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:CLOCK")
    rtcCount_ReadContinuously.setLabel("Continuous Synchronization for RTC Count/Clock Register")

    #Sub Menu - RTC Modes: RTC_MODE0, RTC_MODE1, RTC_MODE2
    rtcModeSelection_Sym = rtcComponent.createKeyValueSetSymbol("RTC_MODULE_SELECTION", rtcSym_Menu)
    rtcModeSelection_Sym.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:CTRL")
    rtcModeSelection_Sym.setLabel("RTC Operation Mode")
    for index in range(0, len(rtcValues)):
        if rtcValues[index].getAttribute("qualifier") != None:
            rtcModeSelection_Sym.addKey(rtcValues[index].getAttribute("name"),rtcValues[index].getAttribute("value"),rtcValues[index].getAttribute("caption"))
    rtcModeSelection_Sym.setDefaultValue(0)
    rtcModeSelection_Sym.setOutputMode("Key")
    rtcModeSelection_Sym.setDisplayMode("Description")

    sysTimeTrigger_Sym = rtcComponent.createBooleanSymbol("SYS_TIME", None)
    sysTimeTrigger_Sym.setVisible(False)
    sysTimeTrigger_Sym.setDependencies(sysTime_modeSelection, ["RTC_MODULE_SELECTION"])

    sysTimeCalendarModeComment = rtcComponent.createCommentSymbol("SYS_TIME_CALENDAR_MODE_NOT_SUPPORTED_COMMENT", rtcModeSelection_Sym)
    sysTimeCalendarModeComment.setLabel("Warning!!! SYS Tick is not supported with RTC in calendar mode")
    sysTimeCalendarModeComment.setVisible(False)
    sysTimeCalendarModeComment.setDependencies(sysTimeCalendarModeCommentVisibility, ["RTC_MODULE_SELECTION"])

#################################### MODE0 #####################################

    rtcSymMode0Menu = rtcComponent.createMenuSymbol("RTC_MODE0_MENU", rtcModeSelection_Sym)
    rtcSymMode0Menu.setLabel("RTC MODE 0 Configuration")
    rtcSymMode0Menu.setDependencies(Mode0Visible,["RTC_MODULE_SELECTION"])

    #Interrupt Enable Set
    rtcSymMode0_INTENSET = rtcComponent.createBooleanSymbol("RTC_MODE0_INTERRUPT", rtcSymMode0Menu)
    rtcSymMode0_INTENSET.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    rtcSymMode0_INTENSET.setLabel("Enable Interrupts ?")
    rtcSymMode0_INTENSET.setDefaultValue(True)

    rtcMode0InterruptNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE0",name="INTENSET"]')
    rtcMode0InterruptValues = rtcMode0InterruptNode.getChildren()

    for i in range(0, len(rtcMode0InterruptValues)):
        rtcSymMode0_Interrupt = rtcComponent.createBooleanSymbol("RTC_MODE0_INTENSET_" + rtcMode0InterruptValues[i].getAttribute("name") + "_ENABLE", rtcSymMode0_INTENSET)
        rtcSymMode0_Interrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:INTENSET")
        rtcSymMode0_Interrupt.setLabel(rtcMode0InterruptValues[i].getAttribute("caption"))
        rtcMode0InterruptMap[rtcMode0InterruptValues[i].getAttribute("name")] = rtcMode0InterruptValues[i].getAttribute("mask")
        rtcMode0InterruptDep.append("RTC_MODE0_INTENSET_" + rtcMode0InterruptValues[i].getAttribute("name") + "_ENABLE")

    #Interrupt Notification
    rtcSymMode0InterruptMask = rtcComponent.createHexSymbol("RTC_MODE0_INTENSET", rtcSymMode0_INTENSET)
    rtcSymMode0InterruptMask.setDefaultValue(0)
    rtcSymMode0InterruptMask.setVisible(False)
    rtcSymMode0InterruptMask.setDependencies(rtcMode0Interrupt, rtcMode0InterruptDep)

    setRTCInterruptData(True)

    #Prescaler
    rtcSymMode0_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE0_PRESCALER", rtcSymMode0Menu)
    rtcSymMode0_CTRLA_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:CTRL")
    rtcSymMode0_CTRLA_PRESCALER.setLabel("RTC Prescaler")

    rtcMode0ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE0_CTRL__PRESCALER\"]")
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
    rtcSymMode0_CTRLA_PRESCALER.setDependencies(rtcPrescalerChangeHandler, ["RTC_MODE0_PRESCALER"])

    #Configure 32-Bit Timer Period
    rtcSymMode0_COMP0 = rtcComponent.createHexSymbol("RTC_MODE0_TIMER_COMPARE",rtcSymMode0Menu)
    rtcSymMode0_COMP0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:COMP")
    rtcSymMode0_COMP0.setLabel("Compare Value")
    rtcSymMode0_COMP0.setDefaultValue(0x00000000)
    rtcSymMode0_COMP0.setMax(0xFFFFFFFF)
    rtcSymMode0_COMP0.setMin(0x00000000)

    #Interrupt Enable Set
    rtcSymMode0_Matcclr = rtcComponent.createBooleanSymbol("RTC_MODE0_MATCHCLR", rtcSymMode0Menu)
    rtcSymMode0_Matcclr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:CTRL")
    rtcSymMode0_Matcclr.setLabel("Clear on compare Match")

    rtcSymMode0Events = rtcComponent.createMenuSymbol("RTC_MODE0_EVCTRL_MENU",rtcSymMode0Menu)
    rtcSymMode0Events.setLabel("RTC EVENTS configuration")

    rtcEventsNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE0",name="EVCTRL"]')
    rtcEventsValues = rtcEventsNode.getChildren()

    for i in range(0,len(rtcEventsValues)):
        rtcSymMode0_Event = rtcComponent.createBooleanSymbol("RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE", rtcSymMode0Events)
        rtcSymMode0_Event.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:EVCTRL")
        rtcSymMode0_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode0EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode0EvctrlDep.append("RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")
        if "PER" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_PER_" + str(rtcEventsValues[i].getAttribute("name")).replace("PEREO", "") + "_ACTIVE"
        if "OVF" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_OVF_ACTIVE"
        if "CMP" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE0_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_CMP_" + str(rtcEventsValues[i].getAttribute("name")).replace("CMPEO", "") + "_ACTIVE"

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
    rtcSymMode1_INTENSET.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    rtcSymMode1_INTENSET.setLabel("Enable Interrupts ?")
    rtcSymMode1_INTENSET.setDefaultValue(True)

    rtcMode1InterruptNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE1",name="INTENSET"]')
    rtcMode1InterruptValues = rtcMode1InterruptNode.getChildren()

    for i in range(0, len(rtcMode1InterruptValues)):
        rtcSymMode1_Interrupt = rtcComponent.createBooleanSymbol("RTC_MODE1_INTENSET_" + rtcMode1InterruptValues[i].getAttribute("name") + "_ENABLE", rtcSymMode1_INTENSET)
        rtcSymMode1_Interrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:INTENSET")
        rtcSymMode1_Interrupt.setLabel(rtcMode1InterruptValues[i].getAttribute("caption"))
        rtcMode1InterruptMap[rtcMode1InterruptValues[i].getAttribute("name")] = rtcMode1InterruptValues[i].getAttribute("mask")
        rtcMode1InterruptDep.append("RTC_MODE1_INTENSET_" + rtcMode1InterruptValues[i].getAttribute("name") + "_ENABLE")

    #Interrupt Notification
    rtcSymMode1InterruptMask = rtcComponent.createHexSymbol("RTC_MODE1_INTENSET", rtcSymMode1_INTENSET)
    rtcSymMode1InterruptMask.setDefaultValue(0)
    rtcSymMode1InterruptMask.setVisible(False)
    rtcSymMode1InterruptMask.setDependencies(rtcMode1Interrupt, rtcMode1InterruptDep)

    #Prescaler
    rtcSymMode1_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE1_PRESCALER", rtcSymMode1Menu)
    rtcSymMode1_CTRLA_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:CTRL")
    rtcSymMode1_CTRLA_PRESCALER.setLabel("RTC Prescaler")

    rtcMode1ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE1_CTRL__PRESCALER\"]")
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
    rtcSymMode1_CTRLA_PRESCALER.setDependencies(rtcPrescalerChangeHandler, ["RTC_MODE1_PRESCALER"])

    #Configure 16-Bit Timer Period
    rtcSymMode1_PER = rtcComponent.createHexSymbol("RTC_MODE1_TIMER_COUNTER_PERIOD",rtcSymMode1Menu)
    rtcSymMode1_PER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:PER")
    rtcSymMode1_PER.setLabel("16-bit Timer Period")
    rtcSymMode1_PER.setDefaultValue(0x0000)
    rtcSymMode1_PER.setMax(0xFFFF)
    rtcSymMode1_PER.setMin(0x0000)

    #Compare 0 Match Value
    rtcSymMode1_CMP0 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE0_MATCH_VALUE",rtcSymMode1Menu)
    rtcSymMode1_CMP0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:COMP")
    rtcSymMode1_CMP0.setLabel("Compare 0 Value")
    rtcSymMode1_CMP0.setMax(0xFFFF)
    rtcSymMode1_CMP0.setMin(0x0000)
    rtcSymMode1_CMP0.setDefaultValue(0x0000)

    #Compare 1 Match Value
    rtcSymMode1_CMP1 = rtcComponent.createHexSymbol("RTC_MODE1_COMPARE1_MATCH_VALUE",rtcSymMode1Menu)
    rtcSymMode1_CMP1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:COMP")
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
        rtcSymMode1_Event.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:EVCTRL")
        rtcSymMode1_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode1EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode1EvctrlDep.append("RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")
        if "PER" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_PER_" + str(rtcEventsValues[i].getAttribute("name")).replace("PEREO", "") + "_ACTIVE"
        if "OVF" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_OVF_ACTIVE"
        if "CMP" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE1_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_CMP_" + str(rtcEventsValues[i].getAttribute("name")).replace("CMPEO", "") + "_ACTIVE"

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
    rtcSymMode2_INTENSET.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    rtcSymMode2_INTENSET.setLabel("Enable Interrupts?")

    #Prescaler
    rtcSymMode2_CTRLA_PRESCALER = rtcComponent.createKeyValueSetSymbol("RTC_MODE2_PRESCALER", rtcSymMode2Menu)
    rtcSymMode2_CTRLA_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    rtcSymMode2_CTRLA_PRESCALER.setLabel("RTC Prescaler")

    rtcMode2ReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]/value-group@[name=\"RTC_MODE2_CTRL__PRESCALER\"]")
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
    rtcSymMode2_REFERENCE_YEAR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:%NOREGISTER%")
    rtcSymMode2_REFERENCE_YEAR.setLabel("Reference Year(Leap Year)")
    rtcSymMode2_REFERENCE_YEAR.setDefaultValue(2016)

    rtcSymMode2Events = rtcComponent.createMenuSymbol("RTC_MODE2_EVCTRL_MENU",rtcSymMode2Menu)
    rtcSymMode2Events.setLabel("RTC EVENTS configuration")

    rtcEventsNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE2",name="EVCTRL"]')
    rtcEventsValues = rtcEventsNode.getChildren()

    for i in range(0,len(rtcEventsValues)):
        rtcSymMode2_Event = rtcComponent.createBooleanSymbol("RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE", rtcSymMode2Events)
        rtcSymMode2_Event.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:EVCTRL")
        rtcSymMode2_Event.setLabel(rtcEventsValues[i].getAttribute("caption"))
        rtcMode2EvctrlMap[rtcEventsValues[i].getAttribute("name")] = rtcEventsValues[i].getAttribute("mask")
        rtcMode2EvctrlDep.append("RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE")
        if "PER" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_PER_" + str(rtcEventsValues[i].getAttribute("name")).replace("PEREO", "") + "_ACTIVE"
        if "OVF" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_OVF_ACTIVE"
        if "ALARM" in rtcEventsValues[i].getAttribute("name"):
            eventMap["RTC_MODE2_EVCTRL_" + rtcEventsValues[i].getAttribute("name") + "_ENABLE"] = "GENERATOR_RTC_CMP_" + str(rtcEventsValues[i].getAttribute("name")).replace("ALARMEO", "") + "_ACTIVE"

    #Periodic Interval Notification
    rtcSymMode2_PERIN = rtcComponent.createHexSymbol("RTC_MODE2_EVCTRL", rtcSymMode2Menu)
    rtcSymMode2_PERIN.setDefaultValue(0)
    rtcSymMode2_PERIN.setVisible(False)
    rtcSymMode2_PERIN.setDependencies(rtcMode2Evctrl, rtcMode2EvctrlDep)

    rtcMode2InterruptNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[modes="MODE2",name="INTENSET"]')
    rtcMode2InterruptValues = rtcMode2InterruptNode.getChildren()

    for i in range(0, len(rtcMode2InterruptValues)):
        rtcSymMode2_Interrupt = rtcComponent.createBooleanSymbol("RTC_MODE2_INTENSET_" + rtcMode2InterruptValues[i].getAttribute("name") + "_ENABLE", rtcSymMode2_INTENSET)
        rtcSymMode2_Interrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtc_u2202;register:INTENSET")
        rtcSymMode2_Interrupt.setLabel(rtcMode2InterruptValues[i].getAttribute("caption"))
        rtcMode2InterruptMap[rtcMode2InterruptValues[i].getAttribute("name")] = rtcMode2InterruptValues[i].getAttribute("mask")
        rtcMode2InterruptDep.append("RTC_MODE2_INTENSET_" + rtcMode2InterruptValues[i].getAttribute("name") + "_ENABLE")

    #Interrupt Notification
    rtcSymMode2InterruptMask = rtcComponent.createHexSymbol("RTC_MODE2_INTENSET", rtcSymMode2_INTENSET)
    rtcSymMode2InterruptMask.setDefaultValue(0)
    rtcSymMode2InterruptMask.setVisible(False)
    rtcSymMode2InterruptMask.setDependencies(rtcMode2Interrupt, rtcMode2InterruptDep)

    ############################################################################
    #### Dependency ####
    ############################################################################

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

    evsysDep = rtcMode0EvctrlDep + rtcMode1EvctrlDep + rtcMode2EvctrlDep
    evsysDep.append("RTC_MODULE_SELECTION")
    evsysTrig = rtcComponent.createBooleanSymbol("EVSYS", None)
    evsysTrig.setVisible(False)
    evsysTrig.setDependencies(evsysSetup, evsysDep)

    sysTime_updateOnModeChange(rtcModeSelection_Sym.getSelectedKey())

################################ Code Generation ###############################

    configName = Variables.get("__CONFIGURATION_NAME")

    rtcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTC\"]")
    rtcModuleID = rtcModuleNode.getAttribute("id")

    # Instance Header File
    rtcHeaderFile = rtcComponent.createFileSymbol("RTC_INSTANCE_HEADER", None)
    rtcHeaderFile.setSourcePath("../peripheral/rtc_u2202/templates/plib_rtc.h.ftl")
    rtcHeaderFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".h")
    rtcHeaderFile.setDestPath("/peripheral/rtc/")
    rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcHeaderFile.setDependencies(updateCodeGenerationProperty, ["RTC_MODULE_SELECTION"])
    rtcHeaderFile.setType("HEADER")
    rtcHeaderFile.setMarkup(True)

    # RTC Timer Mode (MODE0 and MODE1) Source File
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtc_u2202/templates/plib_rtc_timer.c.ftl")
    rtcSourceFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+"_timer.c")
    rtcSourceFile.setDestPath("/peripheral/rtc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSourceFile.setType("SOURCE")
    rtcSourceFile.setMarkup(True)

    # RTC Clock Mode (MODE2) Source File
    rtcSource1File = rtcComponent.createFileSymbol("RTC_CLOCK_SOURCE", None)
    rtcSource1File.setSourcePath("../peripheral/rtc_u2202/templates/plib_rtc_clock.c.ftl")
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
    rtcSystemInitFile.setSourcePath("../peripheral/rtc_u2202/templates/system/initialization.c.ftl")
    rtcSystemInitFile.setMarkup(True)

    # System Definition
    rtcSystemDefFile = rtcComponent.createFileSymbol("RTC_SYS_DEF", None)
    rtcSystemDefFile.setType("STRING")
    rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtcSystemDefFile.setSourcePath("../peripheral/rtc_u2202/templates/system/definitions.h.ftl")
    rtcSystemDefFile.setMarkup(True)
