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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

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
    if (event["id"] == "TC_CTRLA_MODE"):
        if event["value"] == 2:
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
    if event["value"] == 2:   #COUNT32
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tcSlaveClockEnable(symbol, event):
    component = int(tcInstanceName.getValue()[-1]) + 1
    if event["value"] == 2:   #COUNT32
        if (Database.getSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE") == False):
            #clock enable
            Database.clearSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE")
            Database.setSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE", True, 2)
    else:
        if (Database.getSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE") == True):
            activeComponentList = Database.getActiveComponentIDs()
            if ("tc"+str(component) not in activeComponentList):
                #clock disable
                Database.clearSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE")
                Database.setSymbolValue("core", "TC"+str(component)+"_CLOCK_ENABLE", False, 2)

def tcSlaveModeCommentVisible(symbol, event):
    if event["value"] == 2:  #COUNT32
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcSlaveModeSet(symbol, event):
    if event["value"] == 2:   #COUNT32
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
    global tcSym_Compare_INTENSET_OVF
    global tcSym_Capture_InterruptMode
    global tcSym_OperationMode

    if event["id"] == "TC_OPERATION_MODE":
        tcInterruptStatus = False
        tcTimerMode = (event["value"] == "Timer") and (tcSym_Timer_INTENSET_OVF.getValue() == True or tcSym_Timer_INTENSET_MC1.getValue() == True)
        tcCompareMode = (event["value"] == "Compare") and (tcSym_Compare_INTENSET_OVF.getValue() == True)
        tcCaptureMode = (event["value"] == "Capture") and (tcSym_Capture_InterruptMode.getValue() == True)

        if tcTimerMode == True or tcCompareMode == True or tcCaptureMode == True:
            tcInterruptStatus = True

        setTCInterruptData(tcInterruptStatus, event["value"])
    else:
        setTCInterruptData(event["value"], tcSym_OperationMode.getValue())

def updateTCInterruptWarringStatus(symbol, event):

    global tcSym_Timer_INTENSET_OVF
    global tcSym_Timer_INTENSET_MC1
    global tcSym_Compare_INTENSET_OVF
    global tcSym_Capture_InterruptMode
    global tcSym_OperationMode

    tcTimerMode = (tcSym_OperationMode.getValue() == "Timer") and (tcSym_Timer_INTENSET_OVF.getValue() == True or tcSym_Timer_INTENSET_MC1.getValue() == True)
    tcCompareMode = (tcSym_OperationMode.getValue() == "Compare") and (tcSym_Compare_INTENSET_OVF.getValue() == True)
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

    if remoteID == "sys_time":
        tcSym_Timer_INTENSET_MC1.setVisible(True)
        tcSym_Timer_INTENSET_MC1.setValue(True,2)
        tcSym_Timer_INTENSET_OVF.setValue(False,2)
        tcSym_SYS_TIME_CONNECTED.setValue(True, 2)
        tcSym_Timer_TIME_MS.setVisible(False)

def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if remoteID == "sys_time":
        tcSym_Timer_INTENSET_MC1.setVisible(False)
        tcSym_Timer_INTENSET_MC1.setValue(False,2)
        tcSym_Timer_INTENSET_OVF.setValue(True,2)
        tcSym_SYS_TIME_CONNECTED.setValue(False, 2)
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
    timerPeriodMax_Sym.setValue(str(int(math.pow(2, int(key[5:])))), 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

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

    tcInstanceName = tcComponent.createStringSymbol("TC_INSTANCE_NAME", None)
    tcInstanceName.setVisible(False)
    tcInstanceName.setDefaultValue(tcComponent.getID().upper())

    Log.writeInfoMessage("Running " + tcInstanceName.getValue())

    if Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_ENABLE") == False:
        Database.clearSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_ENABLE")
        #clock enable
        Database.setSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

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
        tcSym_CTRLA_MODE.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    tcSym_SLAVE_CLOCK_ENABLE = tcComponent.createIntegerSymbol("TC_SLAVE_CLOCK_ENABLE", None)
    tcSym_SLAVE_CLOCK_ENABLE.setVisible(False)
    tcSym_SLAVE_CLOCK_ENABLE.setDependencies(tcSlaveClockEnable, ["TC_CTRLA_MODE"])
#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------
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
        tcSym_CTRLA_PRESCALER.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #clock resolution display
    tcSym_Resolution = tcComponent.createCommentSymbol("TC_Resolution", None)
    clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000000.0) / clock_freq
    tcSym_Resolution.setLabel("****Timer resolution is " + str(resolution) + " nS****")
    if isMasterSlaveModeEnable == True:
        tcSym_Resolution.setVisible(False)
    tcSym_Resolution.setDependencies(tcResolutionCalc, [masterComponentSymbolId, "core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "TC_CTRLA_PRESCALER"])

    #TC clock frequency
    tcSym_Frequency = tcComponent.createIntegerSymbol("TC_FREQUENCY", None)
    tcSym_Frequency.setLabel("Clock Frequency")
    tcSym_Frequency.setVisible(False)
    tcSym_Frequency.setDefaultValue (Database.getSymbolValue("core", tcInstanceName.getValue()+"_CLOCK_FREQUENCY"))
    tcSym_Frequency.setDependencies(tcFreqCalc, ["core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", "TC_CTRLA_PRESCALER"])

    #tc operation mode
    tcOperationModeList = ["Timer", "Compare", "Capture"]
    global tcSym_OperationMode
    tcSym_OperationMode = tcComponent.createComboSymbol("TC_OPERATION_MODE", None, tcOperationModeList)
    tcSym_OperationMode.setLabel("Operating Mode")
    tcSym_OperationMode.setDefaultValue("Timer")
    if isMasterSlaveModeEnable == True:
        tcSym_OperationMode.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_OperationMode.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    tcSym_SlaveMode_Comment = tcComponent.createCommentSymbol("TC_SLAVE_MODE_COMMENT", None)
    tcSym_SlaveMode_Comment.setVisible(False)
    if isMasterSlaveModeEnable == True:
        tcSym_SlaveMode_Comment.setVisible(True)
    tcSym_SlaveMode_Comment.setLabel("TC is configured in Slave mode to support 32-bit operation")
    if (tcInstanceMasterValue == 0):
        tcSym_SlaveMode_Comment.setDependencies(tcSlaveModeCommentVisible, [masterComponentSymbolId])

    ###################################################################################################
    #################################### Sleep Configuration  #######################################
    ###################################################################################################

    #sleep configuration
    tcSym_SleepConfiguration = tcComponent.createMenuSymbol("TC_SLEEP_CONFIG", None)
    tcSym_SleepConfiguration.setLabel("Sleep Configurations")
    if isMasterSlaveModeEnable == True:
        tcSym_SleepConfiguration.setVisible(False)
    if (tcInstanceMasterValue == 0):
        tcSym_SleepConfiguration.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #run standby mode
    tcSym_CTRLA_RUNSTDBY = tcComponent.createBooleanSymbol("TC_CTRLA_RUNSTDBY", tcSym_SleepConfiguration)
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
    tcSym_UpdateInterruptStatus.setDependencies(updateTCInterruptStatus, ["TC_OPERATION_MODE", "TC_TIMER_INTERRUPT_MODE", "TC_COMPARE_INTENSET_OVF", "TC_CAPTURE_INTERRUPT"])
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
