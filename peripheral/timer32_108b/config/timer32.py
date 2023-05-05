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

global msecToCount
global sysTimeComponentId
global tmr32TimeMs

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def calcAchievableFreq(inputClk, prescale, dirn, countVal):
    
    tickRateDict = {"tick_rate_hz": 0}
    dummy_dict = dict()

    if sysTimeComponentId.getValue() != "":
        #Input clock frequency
        clk = float(inputClk)/(prescale + 1)
        if dirn == "Up":
            countVal = 0xFFFFFFFF - countVal
        achievableTickRateHz = float(1.0/clk) * countVal
        achievableTickRateHz = (1.0/achievableTickRateHz) * 100000.0
        tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
        dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
        
def handleMessage(messageID, args):
    global sysTimeComponentId
    global tmr32TimeMs

    dummy_dict = dict()
    sysTimePLIBConfig = dict()
    
    print "message = " + messageID

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        print sysTimeComponentId.getValue()
        modeDict = {"plib_mode": "PERIOD_MODE"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            tmr32TimeMs.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        if sysTimeComponentId.getValue() != "":
            #Set the Time Period (millisecond)
            tmr32TimeMs.setValue(args["sys_time_tick_ms"])    

    return dummy_dict
###################################################################################################
########################################## Component  #############################################
###################################################################################################
def setTIMER32InterruptData(timer32_interrupt_name, status):

    print "timer32_interrupt_name = " + timer32_interrupt_name
    print "status = " + str(status)
    
    Database.setSymbolValue("core", timer32_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", timer32_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", timer32_interrupt_name + "_INTERRUPT_HANDLER", timer32_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", timer32_interrupt_name + "_INTERRUPT_HANDLER", timer32_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateTIMER32(interruptEn, interruptType, instanceNum):
    interruptNameDir = "TIMER32_" + instanceNum
    interruptNameAgg = "TIMER32_" + instanceNum + "_GRP"

    if (interruptEn == False):
        setTIMER32InterruptData(interruptNameAgg, False)
        setTIMER32InterruptData(interruptNameDir, False)
    else:
        if interruptType == "AGGREGATE":
            setTIMER32InterruptData(interruptNameDir, False)
            setTIMER32InterruptData(interruptNameAgg, True)
        else:
            setTIMER32InterruptData(interruptNameAgg, False)
            setTIMER32InterruptData(interruptNameDir, True)
        

def nvicInterruptUpdate(symbol, event):
    interruptType = event["source"].getSymbolByID("TMR32_INTERRUPT_TYPE").getSelectedKey()
    interruptEn = event["source"].getSymbolByID("TMR32_INTERRUPT_EN").getValue()
    instanceNum = event["source"].getSymbolByID("TMR32_INSTANCE_NUMBER").getValue()
    
    nvicInterruptUpdateTIMER32(interruptEn, interruptType, instanceNum)

def msecToCount(inputClk, prescale, dirn, timeoutMs):
    global msecToCount
    
    countVal = 0
    
    clk = float(inputClk)/(prescale + 1)
    countVal = (timeoutMs / 1000.0) * clk
    if dirn == "Up":
        countVal = 0xFFFFFFFF - countVal
    
    return countVal
    
def calcTimeoutInMsec(inputClk, prescale, countVal, dirn):
    if dirn == "Up":
        countVal = 0xFFFFFFFF - countVal
    clk = float(inputClk)/(prescale + 1)
    timeoutMs = (float(countVal)/clk) * 1000.0
    return timeoutMs
    
def timeUpdate(symbol, event):
    global msecToCount
    inputClk = event["source"].getSymbolByID("TMR32_CLK_INPUT").getValue()
    prescale = event["source"].getSymbolByID("TMR32_PRESCALE_VALUE").getValue()
    dirn = event["source"].getSymbolByID("TMR32_COUNT_DIR").getValue()
    timeoutMs = event["source"].getSymbolByID("TMR32_TIME_MS").getValue()
    
    countVal = msecToCount(inputClk, prescale, dirn, timeoutMs)
    symbol.setValue(long(countVal))
    calcAchievableFreq(inputClk, prescale, dirn, countVal)

def updateVisibility(symbol, event):
    symbol.setVisible(event["value"] == True)

def irqn_update(symbol, event):
    interruptType = event["source"].getSymbolByID("TMR32_INTERRUPT_TYPE").getSelectedKey()
    instanceNum = event["source"].getSymbolByID("TMR32_INSTANCE_NUMBER").getValue()
    
    if (interruptType == "AGGREGATE"):
        nvic_int_num = {}
        nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "TIMER32_" + instanceNum})
        irqn_name = "GIRQ" + str(nvic_int_num["girqn_reg_num"] + 8) + "_IRQn"
        symbol.setValue(irqn_name)
    else:
        symbol.setValue("TIMER32_" + instanceNum + "_IRQn")

def instantiateComponent(tmr32Component):

    global msecToCount
    global sysTimeTickRateMs
    global tmr32TimeMs
    global sysTimeComponentId
    #--------------------------------------------------------------------------------------------------------------------------#

    tmr32InstanceName = tmr32Component.createStringSymbol("TMR32_INSTANCE_NAME", None)
    tmr32InstanceName.setVisible(False)
    tmr32InstanceName.setDefaultValue(tmr32Component.getID().upper())
    
    print "tmr32InstanceName = " + tmr32InstanceName.getValue()
    
    tmr32InstanceNum = tmr32Component.createStringSymbol("TMR32_INSTANCE_NUMBER", None)
    tmr32InstanceNum.setVisible(False)
    tmr32InstanceNum.setDefaultValue(tmr32InstanceName.getValue().split("_")[1])

    #-------------------------------------------------------------------------------------------------------------------------#
    
    tmr32InputClk = tmr32Component.createIntegerSymbol("TMR32_CLK_INPUT", None)
    tmr32InputClk.setVisible(False)
    tmr32InputClk.setDefaultValue(48000000)

    tmr32PrescaleVal = tmr32Component.createIntegerSymbol("TMR32_PRESCALE_VALUE", None)
    tmr32PrescaleVal.setLabel("Pre-scale Value")
    tmr32PrescaleVal.setDefaultValue(0)
    tmr32PrescaleVal.setMin(0)
    tmr32PrescaleVal.setMax(65535)
    
    tmr32CountDir = tmr32Component.createComboSymbol("TMR32_COUNT_DIR", None, ["Up", "Down"])
    tmr32CountDir.setLabel("Count Direction")
    tmr32CountDir.setDefaultValue("Down")
    
    max_val = calcTimeoutInMsec(tmr32InputClk.getValue(), tmr32PrescaleVal.getValue(), 4294967295, tmr32CountDir.getValue())
    
    tmr32TimeMs = tmr32Component.createFloatSymbol("TMR32_TIME_MS", None)
    tmr32TimeMs.setLabel("Timeout (ms)")
    tmr32TimeMs.setMin(0.0)
    tmr32TimeMs.setMax(max_val)
    tmr32TimeMs.setDefaultValue(1000)
    
    tmr32CountInitVal = tmr32Component.createLongSymbol("TMR32_COUNT_INIT_VAL", None)
    tmr32CountInitVal.setLabel("Initial Counter Value")
    tmr32CountInitVal.setMin(0)
    tmr32CountInitVal.setMax(4294967295)
    tmr32CountInitVal.setReadOnly(True)
    tmr32CountInitVal.setDefaultValue(long(msecToCount(tmr32InputClk.getValue(), tmr32PrescaleVal.getValue(), tmr32CountDir.getValue(), tmr32TimeMs.getValue())))
    tmr32CountInitVal.setDependencies(timeUpdate, ["TMR32_PRESCALE_VALUE", "TMR32_COUNT_DIR", "TMR32_TIME_MS"])
    
    tmr32AutoRestartEn = tmr32Component.createBooleanSymbol("TMR32_AUTO_RESTART_EN", None)
    tmr32AutoRestartEn.setLabel("Auto-Restart Enable")
    tmr32AutoRestartEn.setDefaultValue(True)
    
    tmr32IntEn = tmr32Component.createBooleanSymbol("TMR32_INTERRUPT_EN", None)
    tmr32IntEn.setLabel("Interrupt Enable")
    tmr32IntEn.setDefaultValue(True)
    
    # Interrupt type selection
    tmr32InterruptType = tmr32Component.createKeyValueSetSymbol("TMR32_INTERRUPT_TYPE", tmr32IntEn)
    tmr32InterruptType.setLabel("Interrupt Type")
    tmr32InterruptType.addKey("DIRECT", "0", "Direct")
    tmr32InterruptType.addKey("AGGREGATE", "1", "Aggregate")
    tmr32InterruptType.setDefaultValue(0)
    tmr32InterruptType.setDisplayMode("Description")
    tmr32InterruptType.setOutputMode("Key")      
    tmr32InterruptType.setDependencies(updateVisibility, ["TMR32_INTERRUPT_EN"])

    # Internal symbol to update NVIC
    tmr32InputerruptUpdate = tmr32Component.createBooleanSymbol("CCT_INTERRUPT_UPDATE", None)
    tmr32InputerruptUpdate.setVisible(False)
    tmr32InputerruptUpdate.setDependencies(nvicInterruptUpdate, ["TMR32_INTERRUPT_EN", "TMR32_INTERRUPT_TYPE"])
    
    # Set NVIC interrupt default value
    nvicInterruptUpdateTIMER32(True, "DIRECT", tmr32InstanceNum.getValue())
    
#---------------------Symbols needed by SYS Time----------------#    

    # Symbol to save SYS Time ID
    sysTimeComponentId = tmr32Component.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")
    
    timerStartApiName = tmr32InstanceName.getValue() +  "_Start"
    timerStopApiName = tmr32InstanceName.getValue() + "_Stop "
    counterGetApiName = tmr32InstanceName.getValue() +  "_CounterGet"
    frequencyGetApiName = tmr32InstanceName.getValue() + "_FrequencyGet"
    callbackApiName = tmr32InstanceName.getValue() + "_CallbackRegister"
    periodSetApiName = tmr32InstanceName.getValue() + "_PreLoadCountSet"

    timerWidth_Sym = tmr32Component.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = tmr32Component.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = tmr32Component.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = tmr32Component.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timerStopApiName)

    counterApiName_Sym = tmr32Component.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = tmr32Component.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = tmr32Component.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)

    periodSetApiName_Sym = tmr32Component.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)
    periodSetApiName_Sym.setDefaultValue(periodSetApiName);
    
    irqEnumName_Sym = tmr32Component.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue("TIMER32_" + tmr32InstanceNum.getValue() + "_IRQn")
    irqEnumName_Sym.setDependencies(irqn_update, ["TMR32_INTERRUPT_TYPE"])
#----------------------------------------------------------------------------------------------------------------------------#

    configName = Variables.get("__CONFIGURATION_NAME")

    tmr32SourceFile = tmr32Component.createFileSymbol("TMR32_SOURCE", None)
    tmr32SourceFile.setSourcePath("../peripheral/timer32_108b/templates/plib_timer32.c.ftl")
    tmr32SourceFile.setOutputName("plib_"+ tmr32InstanceName.getValue().lower() + ".c")
    tmr32SourceFile.setDestPath("/peripheral/timer32/")
    tmr32SourceFile.setProjectPath("config/" + configName + "/peripheral/timer32/")
    tmr32SourceFile.setType("SOURCE")
    tmr32SourceFile.setMarkup(True)
    tmr32SourceFile.setOverwrite(True)

    tmr32HeaderFile = tmr32Component.createFileSymbol("TMR32_HEADER", None)
    tmr32HeaderFile.setSourcePath("../peripheral/timer32_108b/templates/plib_timer32.h.ftl")
    tmr32HeaderFile.setOutputName("plib_"+ tmr32InstanceName.getValue().lower() + ".h")
    tmr32HeaderFile.setDestPath("/peripheral/timer32/")
    tmr32HeaderFile.setProjectPath("config/" + configName + "/peripheral/timer32/")
    tmr32HeaderFile.setType("HEADER")
    tmr32HeaderFile.setMarkup(True)
    tmr32HeaderFile.setOverwrite(True)

    tmr32CommonHeaderFile = tmr32Component.createFileSymbol("TMR32_COMMON_HEADER", None)
    tmr32CommonHeaderFile.setSourcePath("../peripheral/timer32_108b/templates/plib_timer32_common.h")
    tmr32CommonHeaderFile.setOutputName("plib_timer32_common.h")
    tmr32CommonHeaderFile.setDestPath("/peripheral/timer32/")
    tmr32CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/timer32/")
    tmr32CommonHeaderFile.setType("HEADER")
    tmr32CommonHeaderFile.setMarkup(False)
    tmr32CommonHeaderFile.setOverwrite(True)

    tmr32SystemInitFile = tmr32Component.createFileSymbol("TMR32_SYS_INT", None)
    tmr32SystemInitFile.setType("STRING")
    tmr32SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tmr32SystemInitFile.setSourcePath("../peripheral/timer32_108b/templates/system/initialization.c.ftl")
    tmr32SystemInitFile.setMarkup(True)
    tmr32SystemInitFile.setOverwrite(True)

    tmr32SystemDefFile = tmr32Component.createFileSymbol("TMR32_SYS_DEF", None)
    tmr32SystemDefFile.setType("STRING")
    tmr32SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tmr32SystemDefFile.setSourcePath("../peripheral/timer32_108b/templates/system/definitions.h.ftl")
    tmr32SystemDefFile.setMarkup(True)
    tmr32SystemDefFile.setOverwrite(True)
