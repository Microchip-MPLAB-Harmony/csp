"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

global coretimerFreqComment
global coretimerFrequency
global coretimerCompareMS
global coretimerPeriodMS
global coretimerPeriodUS
global coretimerPeriodValue
global tmrInterruptVector
global tmrInterruptHandlerLock
global tmrInterruptHandler
global tmrInterruptVectorUpdate
global tmrInterruptEnable
global tmrPeriodicInterrupt

global setTimerInterruptData

def handleMessage(messageID, args):
    global coretimerPeriodMS
    
    dummy_dict = {}
    dvrtPLIBConfig = dict()

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        modeDict = {"plib_mode": "COMPARE_MODE"}
        dummy_dict = Database.sendMessage(args["ID"], "SYS_TIME_PLIB_CAPABILITY", modeDict)

        
    elif (messageID == "DVRT_PUBLISH_CAPABILITIES"):
        modeDict = {"plib_mode": "PERIOD_MODE"}
        dvrtPLIBConfig = Database.sendMessage(args["ID"], "DVRT_PLIB_CAPABILITY", modeDict)
        if dvrtPLIBConfig["TIMER_MODE"] == "DVRT_PLIB_MODE_PERIOD":
            coretimerPeriodMS.setValue(dvrtPLIBConfig["dvrt_tick_millisec"])

    elif (messageID == "CORE_TIMER_CONFIG"):
        if "isCoreTmrIntRdOnly" in args:
            Database.getComponentByID("core_timer").getSymbolByID("CORE_TIMER_INTERRUPT_MODE").setReadOnly(args["isCoreTmrIntRdOnly"])
        if "isCoreTmrIntEn" in args:
            Database.setSymbolValue("core_timer", "CORE_TIMER_INTERRUPT_MODE", args["isCoreTmrIntEn"])
        if "isCoreTmrPeriodicIntRdOnly" in args:
            Database.getComponentByID("core_timer").getSymbolByID("CORE_TIMER_PERIODIC_INTERRUPT").setReadOnly(args["isCoreTmrPeriodicIntRdOnly"])
        if "isCoreTmrPeriodicIntEn" in args:
            Database.setSymbolValue("core_timer", "CORE_TIMER_PERIODIC_INTERRUPT", args["isCoreTmrPeriodicIntEn"])
        if "isCoreTmrAutoStart" in args:
            Database.setSymbolValue("core_timer", "CORE_TIMER_AUTOSTART", args["isCoreTmrAutoStart"])

    return dummy_dict

def coreFreqCalc(symbol, event):
    SysClkFreq=Database.getSymbolValue("core", "SYS_CLK_FREQ")

    if (tmrInterruptEnable.getValue() == True):
        periodMS = coretimerPeriodMS.getValue()
    else:
        periodMS = coretimerCompareMS.getValue()

    timerFrequency=int(SysClkFreq)/2
    coretimerFrequency.setValue(timerFrequency,2)
    coretimerFreqComment.setLabel("*** Core Timer Clock Frequency " + str(timerFrequency) + " Hz ***")

    max = ((float(1) / timerFrequency) * (2**32) * 1000)
    coretimerPeriodMS.setMax(float(max))

    defaultPeriod = int(timerFrequency * (periodMS/1000))
    if defaultPeriod > 2**32 - 1:
        defaultPeriod = 2**32 - 1
    coretimerPeriodValue.setValue(str(hex(defaultPeriod)),2)

    coretimerPeriodUS.setValue(int(round(periodMS * 1000)),2)



def setTimerInterruptData(status):
    Database.setSymbolValue("core", tmrInterruptVector, status, 1)
    Database.setSymbolValue("core", tmrInterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", tmrInterruptHandler, "CORE_TIMER_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", tmrInterruptHandler, "CORE_TIMER_Handler", 1)

def updateTimerInterruptData(symbol, event):

    if event["id"] == "CORE_TIMER_INTERRUPT_MODE":
        setTimerInterruptData(event["value"])

    if tmrInterruptEnable.getValue() == True and Database.getSymbolValue("core", tmrInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def getIRQnumber(string):

    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

    for param in interruptsChildren:
        modInst = param.getAttribute("name")
        if string == modInst:
            irq_index = param.getAttribute("index")

    return irq_index


def onAttachmentConnected(source, target):
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

    if remoteID == "sys_time":
        tmrInterruptEnable.setValue(True,1)
        tmrPeriodicInterrupt.setValue(False,1)
        
    if remoteID == "dvrt":
        tmrInterruptEnable.setValue(True,1)
        tmrPeriodicInterrupt.setValue(True,1)

def onAttachmentDisconnected(source, target):
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    
    if ((remoteID == "sys_time") or (remoteID == "dvrt")):
        tmrInterruptEnable.setValue(False,1)
        tmrPeriodicInterrupt.setValue(False,1)

def setVisibility(symbol,event):
    symbol.setVisible(event["value"])

def setCompareVisibility(symbol,event):
    symbol.setVisible((event["value"] == False))

################################################################################
#### Menu ####
################################################################################
def instantiateComponent(tmrComponent):
    global coretimerFreqComment
    global coretimerFrequency
    global coretimerCompareMS
    global coretimerPeriodMS
    global coretimerPeriodUS
    global coretimerPeriodValue
    global tmrInterruptVector
    global tmrInterruptHandlerLock
    global tmrInterruptHandler
    global tmrInterruptVectorUpdate
    global tmrInterruptEnable
    global tmrPeriodicInterrupt

    tmrInterruptEnable = tmrComponent.createBooleanSymbol("CORE_TIMER_INTERRUPT_MODE", None)
    tmrInterruptEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    tmrInterruptEnable.setLabel("Enable Interrupt mode")
    tmrInterruptEnable.setDefaultValue(False)

    tmrPeriodicInterrupt = tmrComponent.createBooleanSymbol("CORE_TIMER_PERIODIC_INTERRUPT", tmrInterruptEnable)
    tmrPeriodicInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    tmrPeriodicInterrupt.setLabel("Generate Periodic interrupt")
    tmrPeriodicInterrupt.setDefaultValue(False)
    tmrPeriodicInterrupt.setVisible(False)
    tmrPeriodicInterrupt.setDependencies(setVisibility, ["CORE_TIMER_INTERRUPT_MODE"])

    coretimerStopInDebug = tmrComponent.createBooleanSymbol("CORE_TIMER_STOP_IN_DEBUG", None)
    coretimerStopInDebug.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    coretimerStopInDebug.setLabel("Stop Timer in Debug mode")

    SysClkFreq=Database.getSymbolValue("core", "SYS_CLK_FREQ")
    timerFrequency=int(SysClkFreq)/2

    max = ((float(1) / timerFrequency) * (2**32) * 1000)

    coretimerCompareMS = tmrComponent.createFloatSymbol("CORE_TIMER_COMPARE_MS", None)
    coretimerCompareMS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    coretimerCompareMS.setLabel("Compare period (milliseconds)")
    coretimerCompareMS.setDefaultValue(float(1.0))
    coretimerCompareMS.setMin(0)
    coretimerCompareMS.setMax(float(max))
    coretimerCompareMS.setVisible((tmrInterruptEnable.getValue() == False))
    coretimerCompareMS.setDependencies(setCompareVisibility, ["CORE_TIMER_INTERRUPT_MODE"])

    coretimerPeriodMS = tmrComponent.createFloatSymbol("CORE_TIMER_PERIOD_MS", tmrPeriodicInterrupt)
    coretimerPeriodMS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    coretimerPeriodMS.setLabel("Timer interrupt period (milliseconds)")
    coretimerPeriodMS.setDefaultValue(float(1.0))
    coretimerPeriodMS.setMin(0)
    coretimerPeriodMS.setMax(float(max))
    coretimerPeriodMS.setVisible(False)
    coretimerPeriodMS.setDependencies(setVisibility, ["CORE_TIMER_PERIODIC_INTERRUPT"])

    coretimerPeriodUS = tmrComponent.createIntegerSymbol("CORE_TIMER_PERIOD_US", None)
    coretimerPeriodUS.setVisible(False)
    coretimerPeriodUS.setDefaultValue(1000)
    coretimerPeriodUS.setMin(0)

    defaultPeriod = int(timerFrequency / 1000)
    coretimerPeriodValue = tmrComponent.createStringSymbol("CORE_TIMER_PERIOD_VALUE", None)
    coretimerPeriodValue.setLabel("Timer Interrupt Period")
    coretimerPeriodValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:coretimer;register:%NOREGISTER%")
    coretimerPeriodValue.setVisible(False)
    coretimerPeriodValue.setDefaultValue(str(hex(defaultPeriod)))

    coretimerFrequency = tmrComponent.createIntegerSymbol("CORE_TIMER_FREQUENCY", None)
    coretimerFrequency.setVisible(False)
    coretimerFrequency.setDefaultValue(timerFrequency)
    coretimerFrequency.setDependencies(coreFreqCalc, ["core.SYS_CLK_FREQ", "CORE_TIMER_PERIOD_MS", "CORE_TIMER_COMPARE_MS"])

    coretimerFreqComment = tmrComponent.createCommentSymbol("CORE_TIMER_FREQUENCY_COMMENT", None)
    coretimerFreqComment.setLabel("*** Core Timer Clock Frequency " + str(timerFrequency) + " Hz ***")

    coretimerAutoStart = tmrComponent.createBooleanSymbol("CORE_TIMER_AUTOSTART", None)
    coretimerAutoStart.setLabel("Auto start timer after initialization")
    coretimerAutoStart.setDefaultValue(False)
    coretimerAutoStart.setVisible(False)

    ################# Interrupt Settings ###########################

    # Get register names, mask values, bit shifts based on vector number
    tmrInterruptVector = "CORE_TIMER_INTERRUPT_ENABLE"
    tmrInterruptHandler = "CORE_TIMER_INTERRUPT_HANDLER"
    tmrInterruptHandlerLock = "CORE_TIMER_INTERRUPT_HANDLER_LOCK"
    tmrInterruptVectorUpdate = "CORE_TIMER_INTERRUPT_ENABLE_UPDATE"
    tmrIrq_index = int(getIRQnumber("CORE_TIMER"))


    tmrInterruptComment = tmrComponent.createCommentSymbol("CORE_TIMER_INTRRUPT_ENABLE_COMMENT", None)
    tmrInterruptComment.setLabel("Warning!!! Core Timer Interrupt is Disabled in Interrupt Manager")
    tmrInterruptComment.setVisible(False)
    tmrInterruptComment.setDependencies(updateTimerInterruptData, ["CORE_TIMER_INTERRUPT_MODE", "core." + tmrInterruptVectorUpdate])

    setTimerInterruptData(False)

    enblRegName, enblBitPosn = _get_enblReg_parms(tmrIrq_index)
    statRegName, statBitPosn = _get_statReg_parms(tmrIrq_index)

    # Below create family-specific register names / masking needed by ftl file
    tmrEnblRegWrt = tmrComponent.createStringSymbol("CORE_TIMER_IEC_REG", None)
    tmrEnblRegWrt.setDefaultValue(enblRegName)
    tmrEnblRegWrt.setVisible(False)

    tmrEnblRegVal = tmrComponent.createStringSymbol("CORE_TIMER_IEC_REG_VALUE", None)
    tmrEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
    tmrEnblRegVal.setVisible(False)

    tmrStatRegRd = tmrComponent.createStringSymbol("CORE_TIMER_IFS_REG", None)
    tmrStatRegRd.setDefaultValue(statRegName)
    tmrStatRegRd.setVisible(False)

    tmrStatRegShiftVal = tmrComponent.createStringSymbol("CORE_TIMER_IFS_REG_VALUE", None)
    tmrStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
    tmrStatRegShiftVal.setVisible(False)

    tmrVectorNum = tmrComponent.createIntegerSymbol("CORE_TIMER_VECTOR_NUMBER", None)
    tmrVectorNum.setDefaultValue(tmrIrq_index)
    tmrVectorNum.setVisible(False)

    ################# Common Symbols needed for SYS_TIME usage ###########################

    timerWidth_Sym = tmrComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerMaxValue = pow(2, int(32)) - 1

    timerPeriodMax_Sym = tmrComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue(str(timerMaxValue))

    timerStartApiName_Sym = tmrComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)

    timeStopApiName_Sym = tmrComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)

    periodSetApiName_Sym = tmrComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)
    
    
    compareSetApiName_Sym = tmrComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiName_Sym.setVisible(False)

    counterApiName_Sym = tmrComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)

    frequencyGetApiName_Sym = tmrComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)

    callbackApiName_Sym = tmrComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)

    irqEnumName_Sym = tmrComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)

    timerStartApiName = "CORETIMER_Start"
    timeStopApiName = "CORETIMER_Stop "
    
    compareSetApiName = "CORETIMER_CompareSet"
    counterGetApiName = "CORETIMER_CounterGet"
    frequencyGetApiName = "CORETIMER_FrequencyGet"
    callbackApiName = "CORETIMER_CallbackSet"

    timerStartApiName_Sym.setDefaultValue(timerStartApiName)
    timeStopApiName_Sym.setDefaultValue(timeStopApiName)
    
    compareSetApiName_Sym.setDefaultValue(compareSetApiName)
    counterApiName_Sym.setDefaultValue(counterGetApiName)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)
    callbackApiName_Sym.setDefaultValue(callbackApiName)
    irqEnumName_Sym.setDefaultValue(str(tmrIrq_index))
#------------------------------------------------------------
    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    coretimerHeaderFile = tmrComponent.createFileSymbol("CORETIMER_FILE_0", None)
    coretimerHeaderFile.setSourcePath("../peripheral/coretimer/templates/plib_coretimer.h.ftl")
    coretimerHeaderFile.setOutputName("plib_coretimer.h")
    coretimerHeaderFile.setDestPath("/peripheral/coretimer/")
    coretimerHeaderFile.setProjectPath("config/" + configName + "/peripheral/coretimer/")
    coretimerHeaderFile.setType("HEADER")
    coretimerHeaderFile.setOverwrite(True)
    coretimerHeaderFile.setEnabled(True)
    coretimerHeaderFile.setMarkup(True)

    coretimerSourceFile = tmrComponent.createFileSymbol("CORETIMER_FILE_1", None)
    coretimerSourceFile.setSourcePath("../peripheral/coretimer/templates/plib_coretimer.c.ftl")
    coretimerSourceFile.setOutputName("plib_coretimer.c")
    coretimerSourceFile.setDestPath("/peripheral/coretimer/")
    coretimerSourceFile.setProjectPath("config/" + configName + "/peripheral/coretimer/")
    coretimerSourceFile.setType("SOURCE")
    coretimerSourceFile.setOverwrite(True)
    coretimerSourceFile.setMarkup(True)
    coretimerSourceFile.setEnabled(True)

    coretimerSystemDefFile = tmrComponent.createFileSymbol("CORETIMER_FILE_2", None)
    coretimerSystemDefFile.setType("STRING")
    coretimerSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    coretimerSystemDefFile.setSourcePath("../peripheral/coretimer/templates/system/definitions.h.ftl")
    coretimerSystemDefFile.setMarkup(True)
    coretimerSystemDefFile.setEnabled(True)


    coretimerSystemInitFile = tmrComponent.createFileSymbol("CORETIMER_FILE_3", None)
    coretimerSystemInitFile.setType("STRING")
    coretimerSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    coretimerSystemInitFile.setSourcePath("../peripheral/coretimer/templates/system/initialization.c.ftl")
    coretimerSystemInitFile.setMarkup(True)
    coretimerSystemInitFile.setEnabled(True)