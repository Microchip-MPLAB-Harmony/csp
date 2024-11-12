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
import math
global masterComponentSymbolId
global tcInstanceMasterValue
global isMasterSlaveModeEnable
global tySym_Slave_Mode
global tcSym_OperationMode

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global tcInstanceName

global compareSetApiName_Sym
global periodSetApiName_Sym
global counterApiName_Sym
global timerWidth_Sym
global timerPeriodMax_Sym

global dvrtPlibMode
global dvrtComponentId

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def sysTime8bitCommentVisibility(symbol, event):
    global sysTimePlibMode
    global sysTimeComponentId
    global tcSym_CTRLA_MODE
    messageDict = {"isVisible" : "", "message" : ""}

    #Hide/Un-hide the comment in PLIB and also send a message to the SYS Time module to display similar comment
    if (sysTimeComponentId.getValue() != "") and (sysTimePlibMode.getValue() == "SYS_TIME_PLIB_MODE_COMPARE") and (tcSym_CTRLA_MODE.getSelectedKey() == "COUNT8"):
        symbol.setVisible(True)
        messageDict["isVisible"] = "True"
        messageDict["message"] = symbol.getLabel()
        messageDict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_NOT_SUPPORTED", messageDict)
    else:
        symbol.setVisible(False)
        messageDict["isVisible"] = "False"
        messageDict["message"] = ""
        messageDict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_NOT_SUPPORTED", messageDict)

def calcAchievableFreq():
    global sysTimeComponentId
    global timer_Frequency
    global tcSym_TimerPeriod
    global sysTimePlibMode
    global dvrtComponentId
    tickRateDict = {"tick_rate_hz": 0}
    dummy_dict = dict()

    if ((sysTimeComponentId.getValue() != "") and (sysTimePlibMode.getValue() == "SYS_TIME_PLIB_MODE_PERIOD")):
        timer_Frequency = Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY") / int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        if timer_Frequency != 0:
            achievableTickRateHz = (1.0/float(timer_Frequency)) * (tcSym_TimerPeriod.getValue())
            if achievableTickRateHz != 0:
                achievableTickRateHz = long((1.0/achievableTickRateHz) * 100000.0)
                tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
                dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
            else:
                dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
        else:
            dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

    elif (dvrtComponentId.getValue() != ""):
        timer_Frequency = Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY") / int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        if timer_Frequency != 0:
            achievableTickRateHz = (1.0/float(timer_Frequency)) * (tcSym_TimerPeriod.getValue())
            if achievableTickRateHz != 0:
                achievableTickRateHz = long((1.0/achievableTickRateHz) * 100000.0)
                tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
                dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
            else:
                dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
        else:
            dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

def dvrtPLIBModeConfig(plibMode):
    global tcSym_Timer_TIME_MS
    global tcSym_CTRLA_MODE

    if dvrtComponentId.getValue() != "":
        if plibMode == "DVRT_PLIB_MODE_PERIOD":
            #Enable Period Interrupt
            tcSym_Timer_INTENSET_OVF.setValue(True,2)
            #Disable Compare Interrupt
            tcSym_Timer_INTENSET_MC1.setValue(False,2)
            tcSym_Timer_INTENSET_MC1.setVisible(False)
            #Un-Hide Time Period (ms) menu item
            tcSym_Timer_TIME_MS.setVisible(True)


def sysTimePLIBModeConfig(plibMode):
    global tcSym_Timer_TIME_MS
    global tcSym_CTRLA_MODE

    if sysTimeComponentId.getValue() != "":
        if ((plibMode == "SYS_TIME_PLIB_MODE_COMPARE") and (tcSym_CTRLA_MODE.getSelectedKey() != "COUNT8")):
            #Enable Compare Interrupt
            tcSym_Timer_INTENSET_MC1.setValue(True,2)
            tcSym_Timer_INTENSET_MC1.setVisible(True)
            #Disable Period Interrupt
            tcSym_Timer_INTENSET_OVF.setValue(False,2)
            #Hide Time Period (ms) menu item
            tcSym_Timer_TIME_MS.setVisible(False)

        if (plibMode == "SYS_TIME_PLIB_MODE_PERIOD"):
            #Enable Period Interrupt
            tcSym_Timer_INTENSET_OVF.setValue(True,2)
            #Disable Compare Interrupt
            tcSym_Timer_INTENSET_MC1.setValue(False,2)
            tcSym_Timer_INTENSET_MC1.setVisible(False)
            #Un-Hide Time Period (ms) menu item
            tcSym_Timer_TIME_MS.setVisible(True)

def handleMessage(messageID, args):
    global sysTimeComponentId
    global tcSym_Timer_TIME_MS
    global tcSym_SYS_TIME_CONNECTED
    global sysTimePlibMode
    global tySym_Slave_Mode
    global tcSym_CTRLA_MODE
    global dvrtPlibMode
    global dvrtComponentId

    dummy_dict = dict()
    sysTimePLIBConfig = dict()
    dvrtPLIBConfig = dict()
    dvrt_tick_ms = {"dvrt_tick_ms" : 0.0}

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        modeDict = {"plib_mode": "PERIOD_AND_COMPARE_MODES"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        sysTimePlibMode.setValue(sysTimePLIBConfig["plib_mode"])
        sysTimePLIBModeConfig(sysTimePlibMode.getValue())
        tcSym_SYS_TIME_CONNECTED.setValue(True, 2)
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            tcSym_Timer_TIME_MS.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

    if ((messageID == "SYS_TIME_PLIB_MODE_COMPARE") or (messageID == "SYS_TIME_PLIB_MODE_PERIOD")):
        sysTimePlibMode.setValue(messageID)
        sysTimePLIBModeConfig(sysTimePlibMode.getValue())

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        tcSym_Timer_TIME_MS.setValue(args["sys_time_tick_ms"])

    if (messageID == "TC_MASTER_DESTROYED"):
        #if the message is received by a slave, disable the slave mode and make the mode selection visible
        if tySym_Slave_Mode.getValue() == True:
            tySym_Slave_Mode.setValue(False)
            tySym_Slave_Mode.setVisible(False)
            tcSym_CTRLA_MODE.setValue(tcSym_CTRLA_MODE.getDefaultValue())
            tcSym_CTRLA_MODE.setVisible(True)

    if (messageID == "DVRT_PUBLISH_CAPABILITIES"):
        dvrtComponentId.setValue(args["ID"])
        opemode_Dict = {"plib_mode": "PERIOD_MODE"}
        dvrtPLIBConfig = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_PLIB_CAPABILITY", opemode_Dict)
        dvrtPlibMode.setValue(dvrtPLIBConfig["TIMER_MODE"])
        dvrtPLIBModeConfig(dvrtPlibMode.getValue())
        tcSym_TimerUnit.setValue("millisecond")
        if dvrtPLIBConfig["TIMER_MODE"] == "DVRT_PLIB_MODE_PERIOD":
            tcSym_Timer_TIME_MS.setValue(dvrtPLIBConfig["dvrt_tick_millisec"])

    if (messageID == "DVRT_TICK_RATE_CHANGED"):
        if dvrtComponentId.getValue() != "":
            #Set the Time Period (Milli Sec)
            #Using an intermediate long symbol to pass tick period, as setSymbolValue does not allow passing float values
            dvrt_tick_ms = (long)(args["dvrt_tick_ms"]*1000)
            tcSym_Timer_TIME_MS.setValue(args["dvrt_tick_ms"])

    return dummy_dict

def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()

    component.getSymbolByID("TC_TIMER_HEADER").setEnabled(False)
    component.getSymbolByID("TC_TIMER_SOURCE").setEnabled(False)
    component.getSymbolByID("TC_COMPARE_HEADER").setEnabled(False)
    component.getSymbolByID("TC_COMPARE_SOURCE").setEnabled(False)
    component.getSymbolByID("TC_CAPTURE_HEADER").setEnabled(False)
    component.getSymbolByID("TC_CAPTURE_SOURCE").setEnabled(False)

    if (tySym_Slave_Mode.getValue() == False):
        if tcSym_OperationMode.getValue() == "Timer":
            component.getSymbolByID("TC_TIMER_HEADER").setEnabled(True)
            component.getSymbolByID("TC_TIMER_SOURCE").setEnabled(True)
        elif tcSym_OperationMode.getValue() == "Compare":
            component.getSymbolByID("TC_COMPARE_HEADER").setEnabled(True)
            component.getSymbolByID("TC_COMPARE_SOURCE").setEnabled(True)
        elif tcSym_OperationMode.getValue() == "Capture":
            component.getSymbolByID("TC_CAPTURE_HEADER").setEnabled(True)
            component.getSymbolByID("TC_CAPTURE_SOURCE").setEnabled(True)

def tcResolutionCalc(symbol, event):
    if (event["id"] == "TC_SLAVE_MODE"):
        if event["value"] == True:
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY")
        if clock_freq == 0:
            clock_freq = 1
        prescaler = int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        resolution = (prescaler * 1000000000.0) / clock_freq
        symbol.setLabel("****Timer resolution is " + str(resolution) + " nS****")

def tcFreqCalc(symbol, event):
    symbol.setValue(Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY") / int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]), 2)

def tcSlaveModeVisible(symbol, event):

    if event["value"] == True:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tcSlaveClockEnable(symbol, event):
    component = int(tcInstanceName.getValue()[-1]) + 1
    if event["value"] == 2:   #COUNT32
        if (Database.getSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE") == False):
            #clock enable
            Database.sendMessage("core", "TC"+str(component)+"_CLOCK_ENABLE", {"isEnabled":True})
    else:
        if (Database.getSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE") == True):
            activeComponentList = Database.getActiveComponentIDs()
            if ("tc"+str(component) not in activeComponentList):
                #clock disable
                Database.sendMessage("core", "TC"+str(component)+"_CLOCK_ENABLE", {"isEnabled":False})

def tcSlaveModeCommentVisible(symbol, event):
    if event["value"] == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcSlaveModeSet(symbol, event):
    if event["value"] == 2:
        symbol.setVisible(True)
        symbol.setValue(True, 2)
    else:
        symbol.setVisible(False)
        symbol.setValue(False, 2)

def setTCInterruptData(status, tcMode):
    Database.setSymbolValue("core", InterruptVector, status, 2)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 2)

    if status == True:
        Database.setSymbolValue("core", InterruptHandler, tcInstanceName.getValue() + "_" + tcMode + "InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, tcInstanceName.getValue() + "_Handler", 2)

def updateTCInterruptStatus(symbol, event):

    global tcSym_Timer_INTENSET_OVF
    global tcSym_Timer_INTENSET_MC1
    global tcSym_Compare_InterruptMode
    global tcSym_Capture_InterruptMode
    global tcSym_OperationMode

    if event["id"] == "TC_OPERATION_MODE":
        tcInterruptStatus = False
        tcTimerMode = (event["value"] == "Timer") and (tcSym_Timer_INTENSET_OVF.getValue() == True or tcSym_Timer_INTENSET_MC1.getValue() == True)
        tcCompareMode = (event["value"] == "Compare") and (tcSym_Compare_InterruptMode.getValue() == True)
        tcCaptureMode = (event["value"] == "Capture") and (tcSym_Capture_InterruptMode.getValue() == True)

        if tcTimerMode == True or tcCompareMode == True or tcCaptureMode == True:
            tcInterruptStatus = True

        setTCInterruptData(tcInterruptStatus, event["value"])
    else:
        if(tcSym_OperationMode.getValue() == "Timer"):
            if(tcSym_Timer_INTENSET_OVF.getValue() == True or tcSym_Timer_INTENSET_MC1.getValue() == True):
                setTCInterruptData(True, tcSym_OperationMode.getValue())
            else:
                setTCInterruptData(False, tcSym_OperationMode.getValue())
        else:
            setTCInterruptData(event["value"], tcSym_OperationMode.getValue())

def updateTCInterruptWarringStatus(symbol, event):

    global tcSym_Timer_INTENSET_OVF
    global tcSym_Timer_INTENSET_MC1
    global tcSym_Compare_InterruptMode
    global tcSym_Capture_InterruptMode
    global tcSym_OperationMode

    tcTimerMode = (tcSym_OperationMode.getValue() == "Timer") and (tcSym_Timer_INTENSET_OVF.getValue() == True or tcSym_Timer_INTENSET_MC1.getValue() == True)
    tcCompareMode = (tcSym_OperationMode.getValue() == "Compare") and (tcSym_Compare_InterruptMode.getValue() == True)
    tcCaptureMode = (tcSym_OperationMode.getValue() == "Capture") and (tcSym_Capture_InterruptMode.getValue() == True)

    if tcTimerMode == True or tcCompareMode == True or tcCaptureMode == True:
        symbol.setVisible(event["value"])

def updateTCClockWarringStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]


def onAttachmentDisconnected(source, target):
    global sysTimeComponentId
    global sysTime8bitComment
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if remoteID == "sys_time":
        #Reset the remote component ID to NULL
        sysTimeComponentId.setValue("")
        tcSym_SYS_TIME_CONNECTED.setValue(False, 2)
        tcSym_Timer_INTENSET_MC1.setVisible(False)
        tcSym_Timer_INTENSET_MC1.setValue(False,2)
        tcSym_Timer_INTENSET_OVF.setValue(True,2)
        tcSym_Timer_TIME_MS.setVisible(True)
        tcSym_Timer_TIME_MS.setValue(0)
        sysTime8bitComment.setVisible(False)

    if remoteID == "dvrt":
        dvrtComponentId.setValue("")
        #Show Time Period and clear it
        tcSym_Timer_TIME_MS.clearValue()
        tcSym_Timer_TIME_MS.setVisible(True)


def sysTime_APIUpdate(symbol,event):
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global timerWidth_Sym
    global timerPeriodMax_Sym
    global tcInstanceName

    symobj = event["symbol"]
    key = symobj.getSelectedKey()

    compareSetApiName = tcInstanceName.getValue() + "_Timer" + str(key[5:]) + "bitCompareSet"
    counterGetApiName = tcInstanceName.getValue() + "_Timer" + str(key[5:]) + "bitCounterGet"
    periodSetApiName = tcInstanceName.getValue() + "_Timer" + str(key[5:]) + "bitPeriodSet"

    compareSetApiName_Sym.setValue(compareSetApiName,2)
    counterApiName_Sym.setValue(counterGetApiName,2)
    periodSetApiName_Sym.setValue(periodSetApiName,2)
    timerWidth_Sym.setValue(int(key[5:]), 2)
    timerPeriodMax_Sym.setValue(str(int(math.pow(2, int(key[5:])) - 1)), 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def destroyComponent(tcComponent):
    global tcInstanceName
    global tySym_Slave_Mode
    instance = int(tcInstanceName.getValue()[-1])

    if tySym_Slave_Mode.getValue() == False:
        # Disable the clock only if master is getting destroyed.
        Database.sendMessage("core", "TC"+str(instance)+"_CLOCK_ENABLE", {"isEnabled":False})

    # If master is getting destroyed, then disable slave's clock if the slave tc instance is not active.
    # If the slave tc is active, then send a message to slave indicating that master is destroyed, thereby allowing slave to work as a normal timer (8/16 bit mode)
    if tcComponent.getSymbolByID("TC_CTRLA_MODE").getSelectedKey() == "COUNT32":
        activeComponentList = Database.getActiveComponentIDs()
        slave_instance = instance + 1
        if ("tc"+str(slave_instance) not in activeComponentList):
            Database.sendMessage("core", "TC"+str(slave_instance)+"_CLOCK_ENABLE", {"isEnabled":False})
        else:
            Database.sendMessage("tc"+str(slave_instance), "TC_MASTER_DESTROYED", None)

def instantiateComponent(tcComponent):

    """ Function to instantiate tcComponent to Active Component """

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global tcInstanceName
    global compareSetApiName_Sym
    global periodSetApiName_Sym
    global counterApiName_Sym
    global timerWidth_Sym
    global timerPeriodMax_Sym
    global tcSym_SYS_TIME_CONNECTED
    global masterComponentSymbolId
    global sysTimeComponentId
    global tcSym_Frequency
    global sysTimePlibMode
    global sysTime8bitComment
    global dvrtPlibMode
    global dvrtComponentId

    tcInstanceName = tcComponent.createStringSymbol("TC_INSTANCE_NAME", None)
    tcInstanceName.setVisible(False)
    tcInstanceName.setDefaultValue(tcComponent.getID().upper())

    Log.writeInfoMessage("Running " + tcInstanceName.getValue())

    if Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_ENABLE") == False:
        Database.sendMessage("core", tcInstanceName.getValue()+"_CLOCK_ENABLE", {"isEnabled":True})

    tcInstanceMasterNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\""+tcInstanceName.getValue()+"\"]/parameters/param@[name=\"MASTER\"]")
    tcInstanceMasterValue = int(tcInstanceMasterNode.getAttribute("value"))
    isMasterSlaveModeEnable = False
    masterComponentSymbolId = ""
    if (tcInstanceMasterValue == 0): #slave
        activeComponentList = Database.getActiveComponentIDs()
        temp = int(tcInstanceName.getValue().split("TC")[1])
        masterComponentID = "tc" + str(temp - 1)
        masterComponentSymbolId = masterComponentID + ".TC_CTRLA_MODE"

        if masterComponentID in activeComponentList:
            value = Database.getSymbolValue(masterComponentID, "TC_CTRLA_MODE")
            if value == 2: #count32
                isMasterSlaveModeEnable = True

    global tySym_Slave_Mode
    tySym_Slave_Mode = tcComponent.createBooleanSymbol("TC_SLAVE_MODE", None)
    tySym_Slave_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:%NOREGISTER%")
    tySym_Slave_Mode.setLabel("Slave Mode")
    tySym_Slave_Mode.setDefaultValue(isMasterSlaveModeEnable)
    if isMasterSlaveModeEnable == True:
        tySym_Slave_Mode.setVisible(True)
    else:
        tySym_Slave_Mode.setVisible(False)
    tySym_Slave_Mode.setReadOnly(True)
    if (tcInstanceMasterValue == 0):
        tySym_Slave_Mode.setDependencies(tcSlaveModeSet, [masterComponentSymbolId])

    #counter mode
    global tcSym_CTRLA_MODE
    tcSym_CTRLA_MODE = tcComponent.createKeyValueSetSymbol("TC_CTRLA_MODE", None)
    tcSym_CTRLA_MODE.setLabel("Counter Mode")
    tcSym_CTRLA_MODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:CTRLA")
    tcModeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CTRLA__MODE\"]")
    tcModeValues = []
    tcModeValues = tcModeNode.getChildren()
    tcModeDefaultValue = 0
    for index in range(len(tcModeValues)):
        tcModeKeyName = tcModeValues[index].getAttribute("name")
        if tcModeKeyName == "COUNT16":
            tcModeDefaultValue = index
        if tcModeKeyName == "COUNT32" and tcInstanceMasterValue != 1:
            continue
        tcModeKeyDescription = tcModeValues[index].getAttribute("caption")
        tcModeKeyValue = tcModeValues[index].getAttribute("value")
        tcSym_CTRLA_MODE.addKey(tcModeKeyName, tcModeKeyValue, tcModeKeyDescription)
    tcSym_CTRLA_MODE.setDefaultValue(tcModeDefaultValue)
    tcSym_CTRLA_MODE.setOutputMode("Key")
    tcSym_CTRLA_MODE.setDisplayMode("Description")
    if isMasterSlaveModeEnable == True:
        tcSym_CTRLA_MODE.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_CTRLA_MODE.setDependencies(tcSlaveModeVisible, ["TC_SLAVE_MODE"])

    tcSym_SLAVE_CLOCK_ENABLE = tcComponent.createIntegerSymbol("TC_SLAVE_CLOCK_ENABLE", None)
    tcSym_SLAVE_CLOCK_ENABLE.setVisible(False)
    if (tcInstanceMasterValue == 1):
        tcSym_SLAVE_CLOCK_ENABLE.setDependencies(tcSlaveClockEnable, ["TC_CTRLA_MODE"])
#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------

    sysTimePlibMode = tcComponent.createStringSymbol("SYS_TIME_PLIB_OPERATION_MODE", None)
    sysTimePlibMode.setLabel("SysTime PLIB Operation Mode")
    sysTimePlibMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:%NOREGISTER%")
    sysTimePlibMode.setVisible(False)
    sysTimePlibMode.setDefaultValue("")

    sysTimeComponentId = tcComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:%NOREGISTER%")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")

    dvrtPlibMode = tcComponent.createStringSymbol("DVRT_PLIB_OPERATION_MODE", None)
    dvrtPlibMode.setLabel("dvrt PLIB Operation Mode")
    dvrtPlibMode.setVisible(False)
    dvrtPlibMode.setDefaultValue("")

    dvrtComponentId = tcComponent.createStringSymbol("DVRT_COMPONENT_ID", None)
    dvrtComponentId.setLabel("dvrt Component id")
    dvrtComponentId.setVisible(False)
    dvrtComponentId.setDefaultValue("")

    sysTime8bitComment = tcComponent.createCommentSymbol("SYS_TIME_8BIT_NOT_SUPPORTED_COMMENT", tcSym_CTRLA_MODE)
    sysTime8bitComment.setLabel("Warning!!! Tickless mode of SYS Time is not supported in 8-bit mode")
    sysTime8bitComment.setVisible(False)
    sysTime8bitComment.setDependencies(sysTime8bitCommentVisibility, ["TC_CTRLA_MODE", "SYS_TIME_PLIB_OPERATION_MODE"])

    sysTimeTrigger_Sym = tcComponent.createBooleanSymbol("SYS_TIME", None)
    sysTimeTrigger_Sym.setVisible(False)
    sysTimeTrigger_Sym.setDependencies(sysTime_APIUpdate, ["TC_CTRLA_MODE"])

    tcSym_SYS_TIME_CONNECTED = tcComponent.createBooleanSymbol("TC_SYS_TIME_CONNECTED", None)
    tcSym_SYS_TIME_CONNECTED.setDefaultValue(False)
    tcSym_SYS_TIME_CONNECTED.setVisible(False)

    timerWidth_Sym = tcComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(16)

    timerPeriodMax_Sym = tcComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFF")

    timerStartApiName_Sym = tcComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_TimerStart")

    timeStopApiName_Sym = tcComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_TimerStop")

    compareSetApiName_Sym = tcComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_Timer16bitCompareSet")
    compareSetApiName_Sym.setVisible(False)

    periodSetApiName_Sym = tcComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_Timer16bitPeriodSet")
    periodSetApiName_Sym.setVisible(False)

    counterApiName_Sym = tcComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_Timer16bitCounterGet")
    counterApiName_Sym.setVisible(False)

    frequencyGetApiName_Sym = tcComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_TimerFrequencyGet")

    callbackApiName_Sym = tcComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(tcInstanceName.getValue() + "_TimerCallbackRegister")

    irqEnumName_Sym = tcComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue(tcInstanceName.getValue() + "_IRQn")
#------------------------------------------------------------

    #prescaler
    global tcSym_CTRLA_PRESCALER
    tcSym_CTRLA_PRESCALER = tcComponent.createKeyValueSetSymbol("TC_CTRLA_PRESCALER", None)
    tcSym_CTRLA_PRESCALER.setLabel("Select Prescaler")
    tcSym_CTRLA_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:CTRLA")
    tcPrescalerSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CTRLA__PRESCALER\"]")
    tcPrescalerSelectionValues = []
    tcPrescalerSelectionValues = tcPrescalerSelectionNode.getChildren()
    tcPrescalerSelectionDefaultValue = 0
    for index in range(len(tcPrescalerSelectionValues)):
        tcPrescalerSelectionKeyName = tcPrescalerSelectionValues[index].getAttribute("name")
        if tcPrescalerSelectionKeyName == "DIV1":
            tcPrescalerSelectionDefaultValue = index
        tcPrescalerSelectionKeyDescription = tcPrescalerSelectionValues[index].getAttribute("caption")
        tcPrescalerSelectionKeyValue = tcPrescalerSelectionValues[index].getAttribute("value")
        tcSym_CTRLA_PRESCALER.addKey(tcPrescalerSelectionKeyName, tcPrescalerSelectionKeyValue, tcPrescalerSelectionKeyDescription)
    tcSym_CTRLA_PRESCALER.setDefaultValue(tcPrescalerSelectionDefaultValue)
    tcSym_CTRLA_PRESCALER.setOutputMode("Key")
    tcSym_CTRLA_PRESCALER.setDisplayMode("Description")
    if isMasterSlaveModeEnable == True:
        tcSym_CTRLA_PRESCALER.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_CTRLA_PRESCALER.setDependencies(tcSlaveModeVisible, ["TC_SLAVE_MODE"])

    #clock resolution display
    tcSym_Resolution = tcComponent.createCommentSymbol("TC_Resolution", None)
    clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000000.0) / clock_freq
    tcSym_Resolution.setLabel("****Timer resolution is " + str(resolution) + " nS****")
    if isMasterSlaveModeEnable == True:
        tcSym_Resolution.setVisible(False)
    tcSym_Resolution.setDependencies(tcResolutionCalc, ["TC_SLAVE_MODE", "core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "TC_CTRLA_PRESCALER"])

    #TC clock frequency
    tcSym_Frequency = tcComponent.createIntegerSymbol("TC_FREQUENCY", None)
    tcSym_Frequency.setLabel("Clock Frequency")
    tcSym_Frequency.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:%NOREGISTER%")
    tcSym_Frequency.setVisible(False)
    tcSym_Frequency.setDefaultValue (Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY"))
    tcSym_Frequency.setDependencies(tcFreqCalc, ["core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", "TC_CTRLA_PRESCALER"])

    #tc operation mode
    tcOperationModeList = ["Timer", "Compare", "Capture"]
    global tcSym_OperationMode
    tcSym_OperationMode = tcComponent.createComboSymbol("TC_OPERATION_MODE", None, tcOperationModeList)
    tcSym_OperationMode.setLabel("Operating Mode")
    tcSym_OperationMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:%NOREGISTER%")
    tcSym_OperationMode.setDefaultValue("Timer")
    if isMasterSlaveModeEnable == True:
        tcSym_OperationMode.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_OperationMode.setDependencies(tcSlaveModeVisible, ["TC_SLAVE_MODE"])

    tcSym_SlaveMode_Comment = tcComponent.createCommentSymbol("TC_SLAVE_MODE_COMMENT", None)
    tcSym_SlaveMode_Comment.setVisible(False)
    if isMasterSlaveModeEnable == True:
        tcSym_SlaveMode_Comment.setVisible(True)
    tcSym_SlaveMode_Comment.setLabel("TC is configured in Slave mode to support 32-bit operation")
    if (tcInstanceMasterValue == 0):
        tcSym_SlaveMode_Comment.setDependencies(tcSlaveModeCommentVisible, ["TC_SLAVE_MODE"])

    ###################################################################################################
    #################################### Sleep Configuration  #######################################
    ###################################################################################################

    #sleep configuration
    tcSym_SleepConfiguration = tcComponent.createMenuSymbol("TC_SLEEP_CONFIG", None)
    tcSym_SleepConfiguration.setLabel("Sleep Configurations")
    if isMasterSlaveModeEnable == True:
        tcSym_SleepConfiguration.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_SleepConfiguration.setDependencies(tcSlaveModeVisible, ["TC_SLAVE_MODE"])

    #run standby mode
    tcSym_CTRLA_RUNSTDBY = tcComponent.createBooleanSymbol("TC_CTRLA_RUNSTDBY", tcSym_SleepConfiguration)
    tcSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2212;register:CTRLA")
    tcSym_CTRLA_RUNSTDBY.setLabel("Run during Standby")

    tcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]")
    tcModuleID = tcModuleNode.getAttribute("id")

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2212/config/tc_timer.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2212/config/tc_compare.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2212/config/tc_capture.py")

    tcInstanceName.setDependencies(updateCodeGenerationProperty, ["TC_OPERATION_MODE", "TC_SLAVE_MODE"])
    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = tcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = tcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = tcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = tcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and Interrupt
    Database.setSymbolValue("core", InterruptVector, True, 2)
    Database.setSymbolValue("core", InterruptHandler, tcInstanceName.getValue() + "_TimerInterruptHandler", 2)
    Database.setSymbolValue("core", InterruptHandlerLock, True, 2)

    # Interrupt Dynamic settings
    tcSym_UpdateInterruptStatus = tcComponent.createBooleanSymbol("TC_INTERRUPT_STATUS", None)
    tcSym_UpdateInterruptStatus.setDependencies(updateTCInterruptStatus, ["TC_OPERATION_MODE", "TC_TIMER_INTENSET_OVF", "TC_TIMER_INTENSET_MC1", "TC_COMPARE_INTERRUPT_MODE", "TC_CAPTURE_INTERRUPT"])
    tcSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    tcSym_IntEnComment = tcComponent.createCommentSymbol("TC_INTERRUPT_ENABLE_COMMENT", None)
    tcSym_IntEnComment.setVisible(False)
    tcSym_IntEnComment.setLabel("Warning!!! "+tcInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    tcSym_IntEnComment.setDependencies(updateTCInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    tcSym_ClkEnComment = tcComponent.createCommentSymbol("TC_CLOCK_ENABLE_COMMENT", None)
    tcSym_ClkEnComment.setLabel("Warning!!! TC Peripheral Clock is Disabled in Clock Manager")
    tcSym_ClkEnComment.setVisible(False)
    tcSym_ClkEnComment.setDependencies(updateTCClockWarringStatus, ["core."+tcInstanceName.getValue()+"_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tcSym_CommonHeaderFile = tcComponent.createFileSymbol("TC_COMMON_HEADER", None)
    tcSym_CommonHeaderFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_common.h")
    tcSym_CommonHeaderFile.setOutputName("plib_tc_common.h")
    tcSym_CommonHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CommonHeaderFile.setType("HEADER")
    tcSym_CommonHeaderFile.setMarkup(False)

    tcSym_TimerHeaderFile = tcComponent.createFileSymbol("TC_TIMER_HEADER", None)
    tcSym_TimerHeaderFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_timer.h.ftl")
    tcSym_TimerHeaderFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".h")
    tcSym_TimerHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_TimerHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_TimerHeaderFile.setType("HEADER")
    tcSym_TimerHeaderFile.setMarkup(True)

    tcSym_TimerSourceFile = tcComponent.createFileSymbol("TC_TIMER_SOURCE", None)
    tcSym_TimerSourceFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_timer.c.ftl")
    tcSym_TimerSourceFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".c")
    tcSym_TimerSourceFile.setDestPath("/peripheral/tc/")
    tcSym_TimerSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_TimerSourceFile.setType("SOURCE")
    tcSym_TimerSourceFile.setMarkup(True)

    tcSym_CompareHeaderFile = tcComponent.createFileSymbol("TC_COMPARE_HEADER", None)
    tcSym_CompareHeaderFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_compare.h.ftl")
    tcSym_CompareHeaderFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".h")
    tcSym_CompareHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CompareHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CompareHeaderFile.setType("HEADER")
    tcSym_CompareHeaderFile.setMarkup(True)

    tcSym_CompareSourceFile = tcComponent.createFileSymbol("TC_COMPARE_SOURCE", None)
    tcSym_CompareSourceFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_compare.c.ftl")
    tcSym_CompareSourceFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".c")
    tcSym_CompareSourceFile.setDestPath("/peripheral/tc/")
    tcSym_CompareSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CompareSourceFile.setType("SOURCE")
    tcSym_CompareSourceFile.setMarkup(True)

    tcSym_CaptureHeaderFile = tcComponent.createFileSymbol("TC_CAPTURE_HEADER", None)
    tcSym_CaptureHeaderFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_capture.h.ftl")
    tcSym_CaptureHeaderFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".h")
    tcSym_CaptureHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CaptureHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CaptureHeaderFile.setType("HEADER")
    tcSym_CaptureHeaderFile.setMarkup(True)

    tcSym_CaptureSourceFile = tcComponent.createFileSymbol("TC_CAPTURE_SOURCE", None)
    tcSym_CaptureSourceFile.setSourcePath("../peripheral/tc_u2212/templates/plib_tc_capture.c.ftl")
    tcSym_CaptureSourceFile.setOutputName("plib_"+tcInstanceName.getValue().lower()+".c")
    tcSym_CaptureSourceFile.setDestPath("/peripheral/tc/")
    tcSym_CaptureSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CaptureSourceFile.setType("SOURCE")
    tcSym_CaptureSourceFile.setMarkup(True)

    tcSym_SystemInitFile = tcComponent.createFileSymbol("TC_SYS_INT", None)
    tcSym_SystemInitFile.setType("STRING")
    tcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tcSym_SystemInitFile.setSourcePath("../peripheral/tc_u2212/templates/system/initialization.c.ftl")
    tcSym_SystemInitFile.setMarkup(True)

    tcSym_SystemDefFile = tcComponent.createFileSymbol("TC_SYS_DEF", None)
    tcSym_SystemDefFile.setType("STRING")
    tcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tcSym_SystemDefFile.setSourcePath("../peripheral/tc_u2212/templates/system/definitions.h.ftl")
    tcSym_SystemDefFile.setMarkup(True)
