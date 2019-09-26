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

global rttInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

def sysTimePLIBModeConfig(plibMode):
    global rttPrescaleValue

    if (plibMode == "SYS_TIME_PLIB_MODE_COMPARE"):
        #Enable Alarm Interrupt
        rttAlarm.setValue(True,2)
        #Disable Period Interrupt
        rttPeriodicInterrupt.setValue(False,2)
        #Reset the prescale value for Alarm mode
        rttPrescaleValue.setValue(3)

    if (plibMode == "SYS_TIME_PLIB_MODE_PERIOD"):
        #Enable Period Interrupt
        rttPeriodicInterrupt.setValue(True,2)
        #Disable Alarm Interrupt
        rttAlarm.setValue(False,2)

def calcAchievableFreq(sysTimeRateMs):
    global sysTimeComponentId
    global rttPrescaleValue
    dummy_dict = dict()
    tickRateDict = {"tick_rate_hz": 0}

    #Configure the new prescaler based on the tick rate from sys_time
    newPrescaler = (float(sysTimeRateMs) / 1000) * 32768
    #Set the new prescaler value
    rttPrescaleValue.setValue(int(newPrescaler))
    #Set the achievable tick rate back to the sys_time
    achievableTickRateHz = float(1.0/32768) * float(rttPrescaleValue.getValue())
    achievableTickRateHz = (1.0/achievableTickRateHz) * 100000.0
    tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
    dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

def handleMessage(messageID, args):
    global sysTimeComponentId
    dummy_dict = dict()
    sysTimePLIBConfig = dict()

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        modeDict = {"plib_mode": "PERIOD_AND_COMPARE_MODES"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        sysTimePLIBModeConfig(sysTimePLIBConfig["plib_mode"])
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            calcAchievableFreq(sysTimePLIBConfig["sys_time_tick_ms"])

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        calcAchievableFreq(args["sys_time_tick_ms"])

    if ((messageID == "SYS_TIME_PLIB_MODE_COMPARE") or (messageID == "SYS_TIME_PLIB_MODE_PERIOD")):
        sysTimePLIBModeConfig(messageID)

    return dummy_dict

def interruptControl(rttNVIC, event):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    if event["value"] == True:
        Database.clearSymbolValue("core", interruptVector)
        Database.setSymbolValue("core", interruptVector, True, 2)

        Database.clearSymbolValue("core", interruptHandler)
        Database.setSymbolValue("core", interruptHandler, rttInstanceName.getValue() + "_InterruptHandler", 2)

        Database.clearSymbolValue("core", interruptHandlerLock)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        if rttAlarm.getValue() == False and rttPeriodicInterrupt.getValue() == False:
            Database.clearSymbolValue("core", interruptVector)
            Database.setSymbolValue("core", interruptVector, False, 2)

            Database.clearSymbolValue("core", interruptHandler)
            Database.setSymbolValue("core", interruptHandler, "RTT_Handler", 2)

            Database.clearSymbolValue("core", interruptHandlerLock)
            Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def onAttachmentConnected(source, target):
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

def onAttachmentDisconnected(source, target):
    global sysTimeComponentId
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

    if remoteID == "sys_time":
        #Reset the remote component ID to NULL
        sysTimeComponentId.setValue("")
        rttAlarm.setValue(True,2)
        rttPeriodicInterrupt.setValue(False,2)
        rttPrescaleValue.setValue(3)

def instantiateComponent(rttComponent):

    global rttInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global sysTimeComponentId
    global rttClkSrc
    global rttPrescaleValue

    rttInstanceName = rttComponent.createStringSymbol("RTT_INSTANCE_NAME", None)
    rttInstanceName.setVisible(False)
    rttInstanceName.setDefaultValue(rttComponent.getID().upper())

    rttMenu = rttComponent.createMenuSymbol("RTT_MENU_0", None)
    rttMenu.setLabel("Hardware Settings ")

    rttINC2Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTT\"]/register-group@[name=\"RTT\"]/register@[name=\"RTT_MODR\"]/bitfield@[name=\"SELINC2\"]")

    rttINC2Support = rttComponent.createBooleanSymbol("RTT_INC2_SUPPORTED", None)
    rttINC2Support.setVisible(False)
    rttINC2Support.setDefaultValue(rttINC2Node is not None)

    rttEVANode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTT\"]/register-group@[name=\"RTT\"]/register@[name=\"RTT_MODR\"]/bitfield@[name=\"SELTRGEV\"]")
    rttEVASupport = rttComponent.createBooleanSymbol("RTT_EVA_SUPPORTED", None)
    rttEVASupport.setVisible(False)
    rttEVASupport.setDefaultValue(rttEVANode is not None)
#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------
    timerStartApiName = rttInstanceName.getValue() + "_Enable"
    timeStopApiName = rttInstanceName.getValue() + "_Disable"
    compareSetApiName = rttInstanceName.getValue() + "_AlarmValueSet"
    counterGetApiName = rttInstanceName.getValue() + "_TimerValueGet"
    frequencyGetApiName = rttInstanceName.getValue() + "_FrequencyGet"
    callbackApiName = rttInstanceName.getValue() + "_CallbackRegister"
    irqEnumName = "RTT_IRQn"

    sysTimeComponentId = rttComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")

    timerWidth_Sym = rttComponent.createIntegerSymbol("TIMER_WIDTH", rttMenu)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = rttComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = rttComponent.createStringSymbol("TIMER_START_API_NAME", rttMenu)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = rttComponent.createStringSymbol("TIMER_STOP_API_NAME", rttMenu)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timeStopApiName)

    compareSetApiName_Sym = rttComponent.createStringSymbol("COMPARE_SET_API_NAME", rttMenu)
    compareSetApiName_Sym.setVisible(False)
    compareSetApiName_Sym.setDefaultValue(compareSetApiName)

    counterApiName_Sym = rttComponent.createStringSymbol("COUNTER_GET_API_NAME", rttMenu)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = rttComponent.createStringSymbol("FREQUENCY_GET_API_NAME", rttMenu)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = rttComponent.createStringSymbol("CALLBACK_API_NAME", rttMenu)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)

    irqEnumName_Sym = rttComponent.createStringSymbol("IRQ_ENUM_NAME", rttMenu)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue(irqEnumName)
#------------------------------------------------------------

    global rttPeriodicInterrupt
    rttPeriodicInterrupt = rttComponent.createBooleanSymbol("rttINCIEN", rttMenu)
    rttPeriodicInterrupt.setLabel("Enable Prescale Rollover Interrupt")
    rttPeriodicInterrupt.setDefaultValue(False)

    global rttAlarm
    rttAlarm = rttComponent.createBooleanSymbol("rttALMIEN", rttMenu)
    rttAlarm.setLabel("Enable Alarm Interrupt")
    rttAlarm.setDefaultValue(True)

    if rttINC2Support.getValue():
        rttInc2Enable = rttComponent.createBooleanSymbol("rttINC2EN", rttMenu)
        rttInc2Enable.setLabel("Enable RTTINC2 Interrupt")
        rttInc2Enable.setDefaultValue(False)

        rttInc2Node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTT"]/value-group@[name="RTT_MODR__SELINC2"]')
        rttInc2Values = rttInc2Node.getChildren()

        rttSelinc2 = rttComponent.createKeyValueSetSymbol("RTT_SELINC2", rttMenu)
        rttSelinc2.setLabel("Periodicity of RTTINC2 Interrupt")
        for index in range(0, len(rttInc2Values)):
            key =  rttInc2Values[index].getAttribute("name")
            value =  rttInc2Values[index].getAttribute("value")
            description =  rttInc2Values[index].getAttribute("caption")
            rttSelinc2.addKey(key, value, description)
        rttSelinc2.setDefaultValue(0)
        rttSelinc2.setOutputMode("Value")
        rttSelinc2.setDisplayMode("Description")

    if rttEVASupport.getValue():
        rttEventEnable = rttComponent.createBooleanSymbol("rttEVAEN", rttMenu)
        rttEventEnable.setLabel("Generate Alarm Interrupt on RTT event")
        rttEventEnable.setDefaultValue(False)

        rttInc2Node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTT"]/value-group@[name="RTT_MODR__SELTRGEV"]')
        rttInc2Values = rttInc2Node.getChildren()

        rttSeltrgev = rttComponent.createKeyValueSetSymbol("RTT_SELTRGEV", rttMenu)
        rttSeltrgev.setLabel("Periodicity of RTT Event")
        for index in range(0, len(rttInc2Values)):
            key =  rttInc2Values[index].getAttribute("name")
            value =  rttInc2Values[index].getAttribute("value")
            description =  rttInc2Values[index].getAttribute("caption")
            rttSeltrgev.addKey(key, value, description)
        rttSeltrgev.setDefaultValue(0)
        rttSeltrgev.setOutputMode("Value")
        rttSeltrgev.setDisplayMode("Description")

    rttClkSrc = rttComponent.createBooleanSymbol("rttRTC1HZ", rttMenu)
    rttClkSrc.setLabel("Use RTC 1Hz as clock Source")
    rttClkSrc.setDefaultValue(False)

    rttPrescaleValue = rttComponent.createIntegerSymbol("rttRTPRES", rttMenu)
    rttPrescaleValue.setLabel("Prescalar Value ")
    rttPrescaleValue.setMax(65535)
    rttPrescaleValue.setMin(0)
    rttPrescaleValue.setDefaultValue(3)
    rttPrescaleValue.setDependencies(rttPrescaleHide, ["rttRTC1HZ"])

    rttResolutionComment = rttComponent.createCommentSymbol("rttResolution", rttMenu)
    rttResolutionComment.setLabel("RTT Counter Clock Resolution: 0.092 ms")
    rttResolutionComment.setDependencies(rttResolutionUpdate, ["rttRTC1HZ", "rttRTPRES"])

    interruptVector = rttInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = rttInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = rttInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    # Interrupt Dynamic settings
    rttinterruptControl = rttComponent.createBooleanSymbol("INTERRUPT_RTT_ENABLE", None)
    rttinterruptControl.setDependencies(interruptControl, ["rttALMIEN", "rttINCIEN"])
    rttinterruptControl.setVisible(False)

    if ((rttAlarm.getValue() == True) or (rttPeriodicInterrupt.getValue() == True)):
        Database.clearSymbolValue("core", interruptVector)
        Database.setSymbolValue("core", interruptVector, True, 2)

        Database.clearSymbolValue("core", interruptHandler)
        Database.setSymbolValue("core", interruptHandler, rttInstanceName.getValue() + "_InterruptHandler", 2)

        Database.clearSymbolValue("core", interruptHandlerLock)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    configName = Variables.get("__CONFIGURATION_NAME")

    rttCommonHeader1File = rttComponent.createFileSymbol("RTT_FILE", None)
    rttCommonHeader1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt_common.h")
    rttCommonHeader1File.setMarkup(False)
    rttCommonHeader1File.setOutputName("plib_rtt_common.h")
    rttCommonHeader1File.setDestPath("/peripheral/rtt/")
    rttCommonHeader1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
    rttCommonHeader1File.setType("HEADER")

    rttHeader1File = rttComponent.createFileSymbol("RTT_FILE_0", None)
    rttHeader1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.h.ftl")
    rttHeader1File.setMarkup(True)
    rttHeader1File.setOutputName("plib_" + rttInstanceName.getValue().lower() + ".h")
    rttHeader1File.setDestPath("/peripheral/rtt/")
    rttHeader1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
    rttHeader1File.setType("HEADER")

    rttSource1File = rttComponent.createFileSymbol("RTT_FILE_1", None)
    rttSource1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.c.ftl")
    rttSource1File.setMarkup(True)
    rttSource1File.setOutputName("plib_" + rttInstanceName.getValue().lower() + ".c")
    rttSource1File.setDestPath("/peripheral/rtt/")
    rttSource1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
    rttSource1File.setType("SOURCE")

    rttSystemInitFile = rttComponent.createFileSymbol("RTT_FILE_2", None)
    rttSystemInitFile.setType("STRING")
    rttSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rttSystemInitFile.setSourcePath("../peripheral/rtt_6081/templates/system/initialization.c.ftl")
    rttSystemInitFile.setMarkup(True)

    rttSystemDefFile = rttComponent.createFileSymbol("RTT_FILE_3", None)
    rttSystemDefFile.setType("STRING")
    rttSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rttSystemDefFile.setSourcePath("../peripheral/rtt_6081/templates/system/definitions.h.ftl")
    rttSystemDefFile.setMarkup(True)

def rttPrescaleHide(rttPrescaleValue, event):
    if event["value"] == True:
        rttPrescaleValue.setReadOnly(True)
        rttPrescaleValue.setValue(0)
        rttPrescaleValue.setVisible(False)
    else:
        rttPrescaleValue.clearValue()
        rttPrescaleValue.setReadOnly(False)
        rttPrescaleValue.setVisible(True)


def rttResolutionUpdate(comment, event):
    data = comment.getComponent()
    rtt1Hz = data.getSymbolValue("rttRTC1HZ")
    rttPres = data.getSymbolValue("rttRTPRES")

    timeResolutionMs = str(0)

    if rtt1Hz == True:
        timeResolutionMs=str(1000)
    else:
        if rttPres == 0:
            timeResolutionMs = "%10.3f"% ((float(65536) / 32768)*1000)

        elif rttPres > 2:
            timeResolutionMs =  "%10.3f"% ((float(rttPres) / 32768)*1000)

    if rttPres == 1 or rttPres == 2:
        comment.setLabel("******* RTT Prescale value of 1 or 2 is invalid")
    else :
        comment.setLabel("RTT Counter Clock Resolution: "+ timeResolutionMs + " ms")
