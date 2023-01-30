"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

################################################################################
#### Register Information ####
################################################################################


################################################################################
#### Global Variables ####
################################################################################
global rtosTimerInputClock
global sysTimeComponentId
global calcRTOSTimeoutInMsec

rtosTimerInputClock = 32768

################################################################################
#### Business Logic ####
################################################################################
def calcAchievableFreq(inputClk, countVal):
    
    tickRateDict = {"tick_rate_hz": 0}
    dummy_dict = dict()

    if sysTimeComponentId.getValue() != "":        
        achievableTickRateHz = float(1.0/inputClk) * countVal
        achievableTickRateHz = (1.0/achievableTickRateHz) * 100000.0
        tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
        dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
        
def handleMessage(messageID, args):
    global sysTimeComponentId
    global rtosTmrTimeMs

    dummy_dict = dict()
    sysTimePLIBConfig = dict()
    
    print "message = " + messageID

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        modeDict = {"plib_mode": "PERIOD_MODE"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            rtosTmrTimeMs.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        if sysTimeComponentId.getValue() != "":
            #Set the Time Period (millisecond)
            rtosTmrTimeMs.setValue(args["sys_time_tick_ms"])    

    return dummy_dict

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def msecToCount(clk_hz, timeoutMs):
    global msecToCount
    countVal = (timeoutMs / 1000.0) * clk_hz    
    return countVal

def calcRTOSTimeoutInMsec(clk_hz, preload_val):
    global calcRTOSTimeoutInMsec
    timeout_msec = float(preload_val)/(clk_hz)
    timeout_msec = timeout_msec * 1000.0
    return timeout_msec

def setRTOSInterruptData(rtos_interrupt_name, status):

    Database.setSymbolValue("core", rtos_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", rtos_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", rtos_interrupt_name + "_INTERRUPT_HANDLER", rtos_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", rtos_interrupt_name + "_INTERRUPT_HANDLER", rtos_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateRTOS(rtosInterruptType):
    interruptNameDir = "RTMR"
    interruptNameAgg = "RTMR" + "_GRP"

    if rtosInterruptType == "AGGREGATE":
        setRTOSInterruptData(interruptNameDir, False)
        setRTOSInterruptData(interruptNameAgg, True)
    else:
        setRTOSInterruptData(interruptNameAgg, False)
        setRTOSInterruptData(interruptNameDir, True)

def rtosTimeoutUpdate(symbol, event):
    global msecToCount   
    
    countVal = msecToCount(rtosTimerInputClock, event["value"])
    symbol.setValue(long(countVal))
    calcAchievableFreq(rtosTimerInputClock, countVal)

def nvicInterruptUpdate(symbol, event):
    rtosInterruptType = event["source"].getSymbolByID("RTOS_TMR_INTERRUPT_TYPE").getSelectedKey()
    rtosInterruptNameSym = event["source"].getSymbolByID("RTOS_TMR_NVIC_INTERRUPT_NAME")

    nvicInterruptUpdateRTOS(rtosInterruptType)
    if rtosInterruptType == "AGGREGATE":
        rtosInterruptNameSym.setValue("RTMR" + "_GRP")
    else:
        rtosInterruptNameSym.setValue("RTMR")

def irqn_update(symbol, event):
    rtosInterruptType = event["source"].getSymbolByID("RTOS_TMR_INTERRUPT_TYPE").getSelectedKey()
    
    if (rtosInterruptType == "AGGREGATE"):
        nvic_int_num = {}
        nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "RTMR"})
        irqn_name = "GIRQ" + str(nvic_int_num["girqn_reg_num"] + 8) + "_IRQn"
        symbol.setValue(irqn_name)
    else:
        symbol.setValue("RTMR_IRQn")
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(rtosTmrComponent):

    global rtosTmrInstanceName    
    global instanceNum
    global rtosTimerInputClock
    global sysTimeComponentId
    global rtosTmrTimeMs
    global msecToCount
    global calcRTOSTimeoutInMsec
    
    rtosTmrInstanceName = rtosTmrComponent.createStringSymbol("RTOS_TMR_INSTANCE_NAME", None)
    rtosTmrInstanceName.setVisible(False)
    rtosTmrInstanceName.setDefaultValue(rtosTmrComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtosTmrInstanceName.getValue())

    rtosTmrInstanceNum = rtosTmrComponent.createStringSymbol("RTOS_TMR_INSTANCE_NUM", None)
    rtosTmrInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(rtosTmrComponent.getID()))
    rtosTmrInstanceNum.setDefaultValue(instanceNum)   
    
    max_val = calcRTOSTimeoutInMsec(rtosTimerInputClock, 4294967295)
    
    rtosTmrTimeMs = rtosTmrComponent.createFloatSymbol("RTOS_TMR_TIME_MS", None)
    rtosTmrTimeMs.setLabel("Timeout (ms)")
    rtosTmrTimeMs.setMin(0.0)
    rtosTmrTimeMs.setMax(max_val)
    rtosTmrTimeMs.setDefaultValue(1000)
    
    rtosPreloadVal = rtosTmrComponent.createLongSymbol("RTOS_TMR_PRELOAD_VALUE", None)
    rtosPreloadVal.setLabel("Preload Value")
    rtosPreloadVal.setMin(0)
    rtosPreloadVal.setMax(long(4294967295))
    rtosPreloadVal.setDefaultValue(long(msecToCount(rtosTimerInputClock, rtosTmrTimeMs.getValue())))
    rtosPreloadVal.setReadOnly(True)
    rtosPreloadVal.setDependencies(rtosTimeoutUpdate, ["RTOS_TMR_TIME_MS"])
    
    rtosTmrAutoReloadEn = rtosTmrComponent.createBooleanSymbol("RTOS_TMR_AUTO_RELOAD_ENABLE", None)
    rtosTmrAutoReloadEn.setLabel("Auto Reload Enable?")
    rtosTmrAutoReloadEn.setDefaultValue(True)
    
    rtosTmrHwHaltEn = rtosTmrComponent.createBooleanSymbol("RTOS_TMR_HW_HALT_ENABLE", None)
    rtosTmrHwHaltEn.setLabel("Hardware Halt Enable?")
    rtosTmrHwHaltEn.setDefaultValue(False)
    
    ## Interrupt Setup
    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "RTMR"})

    # Interrupt type selection
    rtosTmrInterruptType = rtosTmrComponent.createKeyValueSetSymbol("RTOS_TMR_INTERRUPT_TYPE", None)
    rtosTmrInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        rtosTmrInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        rtosTmrInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    rtosTmrInterruptType.setDefaultValue(0)
    rtosTmrInterruptType.setDisplayMode("Description")
    rtosTmrInterruptType.setOutputMode("Key")
    
    # Trigger dependency when interrupt type changes
    rtosTmrNVICUpdate = rtosTmrComponent.createBooleanSymbol("RTOS_TMR_UPDATE_NVIC_INTERRUPT", None)
    rtosTmrNVICUpdate.setVisible(False)
    rtosTmrNVICUpdate.setDependencies(nvicInterruptUpdate, ["RTOS_TMR_INTERRUPT_TYPE"])

    # Set NVIC interrupt default value
    nvicInterruptUpdateRTOS(rtosTmrInterruptType.getValue())
    
    interruptName = ""
    if rtosTmrInterruptType.getSelectedKey() == "AGGREGATE":
        interruptName = "RTMR" + "_GRP"
    else:
        interruptName = "RTMR"
    rtos_NVIC_InterruptName = rtosTmrComponent.createStringSymbol("RTOS_TMR_NVIC_INTERRUPT_NAME", None)
    rtos_NVIC_InterruptName.setDefaultValue(interruptName)
    rtos_NVIC_InterruptName.setVisible(False)

#---------------------Symbols needed by SYS Time----------------#    

    # Symbol to save SYS Time ID
    sysTimeComponentId = rtosTmrComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")
    
    timerStartApiName = rtosTmrInstanceName.getValue() +  "Timer_Start"
    timerStopApiName = rtosTmrInstanceName.getValue() + "Timer_Stop "
    counterGetApiName = rtosTmrInstanceName.getValue() +  "Timer_CounterGet"
    frequencyGetApiName = rtosTmrInstanceName.getValue() + "Timer_FrequencyGet"
    callbackApiName = rtosTmrInstanceName.getValue() + "Timer_CallbackRegister"
    periodSetApiName = rtosTmrInstanceName.getValue() + "Timer_PeriodSet"

    timerWidth_Sym = rtosTmrComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = rtosTmrComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = rtosTmrComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = rtosTmrComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timerStopApiName)

    counterApiName_Sym = rtosTmrComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = rtosTmrComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = rtosTmrComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)

    periodSetApiName_Sym = rtosTmrComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)
    periodSetApiName_Sym.setDefaultValue(periodSetApiName);
    
    irqEnumName_Sym = rtosTmrComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue("RTMR_IRQn")
    irqEnumName_Sym.setDependencies(irqn_update, ["RTOS_TMR_INTERRUPT_TYPE"])
#----------------------------------------------------------------------------------------------------------------------------#
    
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rtosTmrHeaderFile = rtosTmrComponent.createFileSymbol("RTOS_TMR_COMMON_HEADER", None)
    rtosTmrHeaderFile.setSourcePath("../peripheral/rtos_140/templates/plib_rtos_tmr_common.h")
    rtosTmrHeaderFile.setOutputName("plib_rtos_tmr_common.h")
    rtosTmrHeaderFile.setDestPath("peripheral/rtos_tmr/")
    rtosTmrHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtos_tmr/")
    rtosTmrHeaderFile.setType("HEADER")
    rtosTmrHeaderFile.setMarkup(False)
    rtosTmrHeaderFile.setOverwrite(True)

    # Instance Header File
    rtosTmrCmnHeaderFile = rtosTmrComponent.createFileSymbol("RTOS_TMR_HEADER1", None)
    rtosTmrCmnHeaderFile.setSourcePath("../peripheral/rtos_140/templates/plib_rtos_tmr.h.ftl")
    rtosTmrCmnHeaderFile.setOutputName("plib_rtos_tmr.h")
    rtosTmrCmnHeaderFile.setDestPath("/peripheral/rtos_tmr/")
    rtosTmrCmnHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtos_tmr/")
    rtosTmrCmnHeaderFile.setType("HEADER")
    rtosTmrCmnHeaderFile.setMarkup(True)
    rtosTmrCmnHeaderFile.setOverwrite(True)

    # Instance Source File
    rtosTmrSourceFile = rtosTmrComponent.createFileSymbol("RTOS_TMR_SOURCE", None)
    rtosTmrSourceFile.setSourcePath("../peripheral/rtos_140/templates/plib_rtos_tmr.c.ftl")
    rtosTmrSourceFile.setOutputName("plib_" + rtosTmrInstanceName.getValue().lower() + "_tmr.c")
    rtosTmrSourceFile.setDestPath("/peripheral/rtos_tmr/")
    rtosTmrSourceFile.setProjectPath("config/" + configName + "/peripheral/rtos_tmr/")
    rtosTmrSourceFile.setType("SOURCE")
    rtosTmrSourceFile.setMarkup(True)
    rtosTmrSourceFile.setOverwrite(True)

    rtosTmrSystemInitFile = rtosTmrComponent.createFileSymbol("RTOS_TMR_SYS_INT", None)
    rtosTmrSystemInitFile.setType("STRING")
    rtosTmrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtosTmrSystemInitFile.setSourcePath("../peripheral/rtos_140/templates/system/initialization.c.ftl")
    rtosTmrSystemInitFile.setMarkup(True)

    rtosTmrSystemDefFile = rtosTmrComponent.createFileSymbol("RTOS_TMR_SYS_DEF", None)
    rtosTmrSystemDefFile.setType("STRING")
    rtosTmrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtosTmrSystemDefFile.setSourcePath("../peripheral/rtos_140/templates/system/definitions.h.ftl")
    rtosTmrSystemDefFile.setMarkup(True)
