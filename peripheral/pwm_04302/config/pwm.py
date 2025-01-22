import re
from collections import OrderedDict

CORE_COMPONENT = "core"
STANDARD_SPEED_PERIPHERAL_CLOCK = "Standard Speed Peripheral Clock"
CLOCK_GENERATOR_FIVE = "clkGen5Enable"
PWM_CLK_SRC = "PWM_CLK_SRC"
MODULE_NAME = "PWM"
SYSTEM_FREQ_SYM = "stdSpeedClkFreq"
PWM_CLOCK = "PWM Master Clock"
CLOCK_DIVIDER = "Clock Divider"
CLK_FREQUENCY = "CLK_FREQUENCY"
CLK_DIV_FREQUENCY = "CLK_DIV_FREQUENCY"
MASTER = "MASTER"
ENABLE_INTERRUPT = "intEnabled"
MASTER_CLK_SRC = "MASTER_CLK_SRC"
MASTER_CLK_FREQ = "MASTER_CLK_FREQ"
MASTER_REQ_FREQ = "MASTER_REQ_FREQ"
MASTER_CALC_FREQ = "MASTER_CALC_FREQ"
MASTER_PERIOD = "MASTER_PERIOD"
MASTER_PRIMARY_DC = "MASTER_PRIMARY_DC"
MASTER_PRIMARY_DC_REG_VAL = "MASTER_PRIMARY_DC_REG_VAL"
MASTER_SEC_DC = "MASTER_SEC_DC"
MASTER_SEC_DC_REG_VAL = "MASTER_SEC_DC_REG_VAL"
MASTER_PRIMARY_REQ_PHASE = "MASTER_PRIMARY_REQ_PHASE"
MASTER_PRIMARY_CAL_PHASE = "MASTER_PRIMARY_CAL_PHASE"
MASTER_PHASE_REG_VAL = "MASTER_PHASE_REG_VAL"
MASTER_SEC_REQ_PHASE = "MASTER_SEC_REQ_PHASE"
MASTER_SEC_CAL_PHASE = "MASTER_SEC_CAL_PHASE"
MASTER_SEC_PHASE_REG_VAL = "MASTER_SEC_PHASE_REG_VAL"

ENABLE_INTERRUPT_COMMENT = "ENABLE_INTERRUPT_COMMENT"
CLOCK_COMMENT = "CLOCK_COMMENT"

MICRO_SECONDS = 1e-6

INDEPENDENT_EDGE = "Independent Edge"
INDEPENDENT_EDGE_DUAL_OUTPUT = "Independent Edge, dual output"
VARIABLE_PHASE = "Variable Phase"
COMPLEMENTARY = "Complementary"
PUSH_PULL = "Push-Pull"
INDEPENDENT = "Independent"
CENTER_ALIGNED = "Center-Aligned"
DOUBLE_UPDATE_CENTER_ALIGNED = "Double-Update Center-Aligned"
DUAL_EDGE_CENTER_ALIGNED_TWO_UPDATES_CYCLE = "Dual Edge Center-Aligned;two updates/cycle"
DUAL_EDGE_CENTER_ALIGNED_ONE_UPDATE_CYCLE = "Dual Edge Center-Aligned;one update/cycle"

PG_ENABLE = "{}_ENABLE"
PG_INTERRUPT_ENABLE = "PG{}_intEnabled"
PG_CLOCK_MENU = "{}_CLOCK_MENU"
PG_CLK_SRC = "{}_PG_CON__CLKSEL"
PG_CLK_FREQ = "{}_CLK_FREQ"
PG_OPERATION_MENU = "{}.OPERATION"
PG_USE_MASTER_PERIOD = "{}_USE_MASTER_PERIOD"
PG_USE_MASTER_DC = "{}_USE_MASTER_DC"
PG_USE_MASTER_PHASE = "{}_USE_MASTER_PHASE"
PG_USE_MASTER_PERIOD_COMMENT = "{}_USE_MASTER_PERIOD_COMMENT"
PG_REQ_PWM_FREQ = "{}_REQ_FREQ"
PG_CALC_PWM_FREQ = "{}_CALC_FREQ"
PG_PERIOD = "{}_PERIOD"
PG_PRIMARY_DC = "{}_PRIMARY_DC"
PG_PRIMARY_DC_REG_VAL = "{}_PRIMARY_DC_REG_VAL"
PG_SEC_DC = "{}_SEC_DC"
PG_SEC_DC_REG_VAL = "{}_SEC_DC_REG_VAL"
PG_REQ_PHASE = "{}_PRIMARY_REQ_PHASE"
PG_CAL_PHASE = "{}_PRIMARY_CAL_PHASE"
PG_PHASE_REG_VAL = "{}_PRIMARY_PHASE_REG_VAL"
PG_SEC_REQ_PHASE = "{}_SEC_REQ_PHASE"
PG_SEC_CAL_PHASE = "{}_SEC_CAL_PHASE"
PG_SEC_PHASE_REG_VAL = "{}_SEC_PHASE_REG_VAL"
PG_DEAD_TIME_LOW = "{}_DEAD_TIME_LOW"
PG_CALC_DEAD_TIME_LOW = "{}_CALC_DEAD_TIME_LOW"
PG_DEAD_TIME_HIGH = "{}_DEAD_TIME_HIGH"
PG_DEAD_TIME_REG = "{}_PG_DT"
PG_CALC_DEAD_TIME_HIGH = "{}_CALC_DEAD_TIME_HIGH"
PG_DEAD_TIME_HIGH_REG_VAL = "{}_DEAD_TIME_HIGH_REG_VAL"
PG_DEAD_TIME_LOW_REG_VAL = "{}_DEAD_TIME_LOW_REG_VAL"
PG_DATA_UPDATE_SETTINGS = "{}_DATA_UPDATE_SETTINGS"
PG_MSTEN = "{}_MSTEN"
PG_UPDTRG = "{}_UPDTRG"
PG_OVERRIDE_CONFIGURATIONS = "{}_OVERRIDE_CONFIGURATIONS"
PG_OVRDAT= "{}_PG_IOCON__OVRDAT"
PG_FLTDAT= "{}_PG_IOCON__FLTDAT"
PG_FAULT_CONFIGURATIONS = "{}_FAULT_CONFIGURATIONS"
PG_PSS = "{}_PSS"
PG_PPS = "{}_PPS"
PG_TRIGGER_CONFIGURATIONS = "{}_TRIGGER_CONFIGURATIONS"
PG_SOCS = "{}_SOCS"
PG_PGTRIGSEL = "{}_PGTRIGSEL"
PG_TRIG_A_COMP = "{}_PG_TRIGA"
PG_TRIG_B_COMP = "{}_PG_TRIGB"
PG_TRIG_C_COMP = "{}_PG_TRIGC"
PG_DEAD_TIME_MENU = "{}_DEADTIME_MENU"

interruptVectorData = {}
ifsMap = {}
iecMap = {}
activeGenList = []
# ---------------------------------- Helper functions -------------------------------------------
def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
    # Path to the register node in the ATDF structure
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, register_group, register
    )
    # Retrieve the register node
    register_node = ATDF.getNode(reg_path)
    
    # If the register node is found, fetch and return the initval as hex; otherwise, return "0x0UL"
    if register_node is not None:
        reg_default_val = register_node.getAttribute("initval")
        return "{}UL".format(reg_default_val) if reg_default_val else "0x0UL"
    return "0x0UL"

def getValueGroup(moduleName,valueGroupName):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/value-group@[name="'+ valueGroupName + '"]'
    return ATDF.getNode(atdfPath)

def getBitfieldData(node):
    result = []
    for bitfield in node.getChildren():
        caption = bitfield.getAttribute("caption")
        if caption.lower() != "reserved":
            value = bitfield.getAttribute("value")
            bitfieldInt = int(value, 16) if value.startswith("0x") else int(value)
            result.append({
                "key": bitfield.getAttribute("name") or caption,
                "value": str(bitfieldInt),
                "desc": caption,
            })
    return result

def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value 

def getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         regDefaultVal = registerNode.getAttribute("initval")
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return getDefaultVal(regDefaultVal,bitMask)
     return 0

def findKeyValue(value, dict):
    for index, pair in enumerate(dict):
        if pair["value"] == str(value):
            return index
    print("Could not find value in dictionary")
    return ""

def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

def getDefaultValue(moduleName, registerGroup, register, bitfield):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    
    if valGroup is None:
        return None

    optionList = getBitfieldOptionList(valGroup)
    defaultValue = getSettingBitDefaultValue(moduleName, registerGroup, register, bitfield)
    
    for option in optionList:
        if option["value"] == str(defaultValue):
            return option["key"]
    return None

def getValueGroupName(moduleName,registerGroup,register,bitfield):
    bitNode = getBitField(moduleName,registerGroup,register,bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            optionList.append(dict)
    return optionList 

def getKeyValuePairBasedonValue(value,keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find value in dictionary") # should never get here
    return "" 

def addKeystoKeyValueSymbol(bitSymbol,bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey( ii['key'],ii['value'], ii['desc'] )  

def getParamValue(paramName,dataType="hex"):
    paramVal = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="PWM"]/instance@[name="PWM"]/parameters/param@[name="'+paramName+'"]').getAttribute("value")
    if dataType == "int":
        return int(paramVal)
    elif dataType == "hex":
        return int(paramVal,16)
    return str(paramVal) 

def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield, parentSymbol,genNum,isMasterSym): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            if genNum > 0:
                symbolKey = "PG{}_{}".format(genNum, valueGroupEntry)
            elif isMasterSym == True:
                symbolKey = "MASTER_{}".format(valueGroupEntry)
            else:
                symbolKey = valueGroupEntry

            optionList = getBitfieldOptionList(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, parentSymbol)
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp  

def getTriggerCompareList():
    # fetch Trigger Compare events available from TRIGy registers where y = A,B,C,.. output:[A,B,C]
    trigList = []
    regGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PWM"]/register-group@[name="PG"]')
    if regGroup:
        children = regGroup.getChildren()
        for child in children:
            name = child.getAttribute("name")
            if name and name.startswith("TRIG"):
                trigList.append(name[-1])
    return sorted(trigList)

def getADCTrgList():
    # fetch ADCs from ADTR setting bits output:[1,2] 
    adcList = set()
    regGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PWM"]/register-group@[name="PG"]/register@[name="EVT"]')
    if regGroup:
        children = regGroup.getChildren()
        for child in children:
            name = child.getAttribute("name")
            if name and name.startswith("ADTR"):
                adcList.add(name[4])
    return sorted(adcList)

def getMasterOrPG(symbol,event):
    if MASTER in event["id"]:
        prefix = MASTER
    else:
        prefix = symbol.getID().split("_")[0] # eg: PG1
    return prefix

def populateIntVectorData():
    for interrupt in ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren():
        name = interrupt.getAttribute("name")
        index = int(interrupt.getAttribute("index"))
        if re.match(r"^PWM", name):
            interruptVectorData[name] = index

def createBitSymbol(genName,symbolName, register, bitField,pwmComponent):
    bitSymbol = pwmComponent.createStringSymbol(symbolName, None)
    bitSymbol.setVisible(False)
    bitNode = getBitField("PWM", "PG", register, bitField)
    bitName = ""
    if bitNode is not None:
        bitName = genName + register + "bits." + bitNode.getAttribute("name")
    bitSymbol.setDefaultValue(bitName)

def createRegPorSetString():
    regDefaults = OrderedDict()
    regPorSet = "" 
    pgRegisterList = ["CON", "IOCON", "STAT", "EVT", "DC", "PER", "PHASE", "DT", "FPCI", "TRIGA", "TRIGB", "TRIGC"]
    commonRegList = ["MDC", "MPER", "MPHASE", "PCLKCON"]

    for reg in commonRegList:
        regDefaults[reg] = getRegisterDefaultValue(MODULE_NAME, reg, reg)
        regPorSet += "    {} = {};\n\n".format(reg, regDefaults[reg])

    pgRegDefaults = {}
    for reg in pgRegisterList:
        regName = "{}{}".format("PG", reg)
        pgRegDefaults[regName] = getRegisterDefaultValue(MODULE_NAME, "PG", reg)

    for gen in activeGenList:
        for reg in pgRegisterList:
            regName = "{}{}{}".format("PG", gen, reg)
            regDefaults[regName] = pgRegDefaults["PG" + reg] 
            regPorSet += "    {} = {};\n".format(regName, regDefaults[regName])
        regPorSet += "\n"

    return regPorSet

def updateInterruptSym(symbol,event):
    for i in range(1, NUMBER_OF_GENERATORS + 1):
        if symbol.getComponent().getSymbolValue(PG_INTERRUPT_ENABLE.format(i)) == True :
            symbol.setValue(True)
            return
    symbol.setValue(False)

def getIFSandIECRegMap():
    intFlagList = [interrupt.replace("Interrupt","")+"IF" for interrupt in interruptVectorData.keys()]
    isflagDataAdded = False
    atdfPath = '/avr-tools-device-file/modules/module@[name="intc"]/register-group@[name="IFS"]'
    flagRegisterGroup = ATDF.getNode(atdfPath).getChildren()
    if(flagRegisterGroup != None):
        for registerNode in flagRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith("PWM") and bitName in intFlagList):
                    ifsMap[bitName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(ifsMap) == NUMBER_OF_GENERATORS):
                        isflagDataAdded = True
                        break
            if isflagDataAdded:
                break
    
    isEnableDataAdded = False
    intEnableList = [interrupt.replace("Interrupt","")+"IE" for interrupt in interruptVectorData.keys()]
    atdfIECPath = '/avr-tools-device-file/modules/module@[name="intc"]/register-group@[name="IEC"]'
    enableRegisterGroup = ATDF.getNode(atdfIECPath).getChildren()
    if(enableRegisterGroup != None):
        for registerNode in enableRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith("PWM") and bitName in intEnableList):
                    iecMap[bitName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(iecMap) == NUMBER_OF_GENERATORS):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break                       

# ----------------------------------- Calculation Section ----------------------------------------------

def getFreqCalculationCase(operatingMode, outputMode):
    isEdgeAligned = operatingMode in [INDEPENDENT_EDGE, INDEPENDENT_EDGE_DUAL_OUTPUT, VARIABLE_PHASE]
    isCenterAligned = operatingMode in [
        DUAL_EDGE_CENTER_ALIGNED_ONE_UPDATE_CYCLE,
        DUAL_EDGE_CENTER_ALIGNED_TWO_UPDATES_CYCLE,
        DOUBLE_UPDATE_CENTER_ALIGNED, CENTER_ALIGNED]
    isCompOrIndependentOutputMode = outputMode in [COMPLEMENTARY, INDEPENDENT]

    if isEdgeAligned and isCompOrIndependentOutputMode:
        return "case1"

    elif isCenterAligned and isCompOrIndependentOutputMode:
        return "case2"

    elif isEdgeAligned and outputMode == PUSH_PULL:
        return "case2"

    return "case3"

def getPeriodFromFrequency(inputClockFreq, pwmFreqValue, operatingMode, outputMode, periodMinVal, periodMaxVal):
    if inputClockFreq == 0 or pwmFreqValue == 0:
        return 0

    freqCalcCase = getFreqCalculationCase(operatingMode, outputMode)

    if freqCalcCase == "case1":
        period = round((16 * inputClockFreq) / pwmFreqValue - 16)
    elif freqCalcCase == "case2":
        period = round((8 * inputClockFreq) / pwmFreqValue - 16)
    else:
        period = round((4 * inputClockFreq) / pwmFreqValue - 1)

    if period > periodMaxVal:
        return periodMaxVal
    elif period < periodMinVal:
        return periodMinVal

    return getNearestMultipleOf16WithinRange(period, periodMinVal, periodMaxVal)

def getNearestMultipleOf16WithinRange(value, minLimit, maxLimit):
    nearestMultiple = round(value / 16) * 16
    if nearestMultiple > maxLimit:
        return maxLimit
    elif nearestMultiple < minLimit:
        return minLimit
    return nearestMultiple
 
def getCalculatedFrequency(inputClockFreq, pwmFreqValue, operatingMode, outputMode, periodMinVal, periodMaxVal):
    calcFreq = 0
    freqCalcCase = getFreqCalculationCase(operatingMode,outputMode)
    periodValue = getPeriodFromFrequency(inputClockFreq, pwmFreqValue, operatingMode, outputMode, periodMinVal, periodMaxVal)

    if inputClockFreq == 0 or pwmFreqValue == 0:
        return 0

    if (freqCalcCase == "case2"):
        calcFreq = ((8 * inputClockFreq) / (periodValue + 16))
    elif (freqCalcCase == "case3"):
        calcFreq = ((4 * inputClockFreq) / (periodValue + 16))
    else: #case1
        calcFreq = ((16 * inputClockFreq) / (periodValue + 16))

    return calcFreq

def getMinMaxFrequency(clockFreq, operatingMode, outputMode):
    freqCalcCase = getFreqCalculationCase(operatingMode, outputMode)
    multiplier = 16 if freqCalcCase == "case1" else 8 if freqCalcCase == "case2" else 4
    return {
        "max": int((multiplier * clockFreq) / (MIN_PERIOD_VAL + 16)),
        "min": int((multiplier * clockFreq) / (MAX_PERIOD_VAL + 16)),
    }

def getMinMaxPhase(clkFreq):
    if clkFreq == 0:
        return {"max": 0, "min": 0}
    return {
        "max": int(MAX_PHASE_VAL * 1e6 / (16 * clkFreq)),
        "min": int(MIN_PHASE_VAL * 1e6 / (16 * clkFreq)),
    }

def getMinMaxDeadTime(clkFreq):
    if clkFreq == 0:
        return {"max": 0, "min": 0}
    return {
        "max": int(MAX_DEADTIME_VAL * 1e6 / (16 * clkFreq)),
        "min": int(MIN_DEADTIME_VAL * 1e6 / (16 * clkFreq)),
    }

def getDeadTimeRegVal(deadTime,clkFreq):
    dtRegVal = int(16 * deadTime * clkFreq * MICRO_SECONDS)
    if dtRegVal < 0: 
        return MIN_DEADTIME_VAL
    elif dtRegVal > MAX_DEADTIME_VAL:
        return MAX_DEADTIME_VAL
    return dtRegVal

def getDTCalcVal(reqDeadTime,clkFreq):
    dtRegVal = getDeadTimeRegVal(reqDeadTime,clkFreq)
    deadTimeMinMax = getMinMaxDeadTime(clkFreq)

    dtCalcVal = int(dtRegVal / (16 * clkFreq * MICRO_SECONDS))

    if dtCalcVal < deadTimeMinMax["min"]: 
        return deadTimeMinMax["min"]
    elif dtCalcVal > deadTimeMinMax["max"]:
        return deadTimeMinMax["max"]
    return dtCalcVal

def getPhaseRegVal(reqPhase,clkFreq):
    phaseRegVal = int(16 * reqPhase * clkFreq * MICRO_SECONDS)
    if phaseRegVal < 0: 
        return MIN_PHASE_VAL
    elif phaseRegVal > MAX_PHASE_VAL:
        return MAX_PHASE_VAL
    return phaseRegVal

def getPhaseCalcVal(reqPhase,clkFreq):
    phaseRegVal = getPhaseRegVal(reqPhase,clkFreq)
    phaseMinMax = getMinMaxPhase(clkFreq)
    phaseCalcVal = int(phaseRegVal / (16 * clkFreq * MICRO_SECONDS))
    if phaseCalcVal < phaseMinMax["min"]: 
        return phaseMinMax["min"]
    elif phaseCalcVal > phaseMinMax["max"]:
        return phaseMinMax["max"]
    return phaseCalcVal

def setPhaseSymValues(symbol, event, isSecondary=False, isRegValCalculation=False):
    prefix = MASTER if MASTER in event["id"] else symbol.getID().split("_")[0]

    phaseKey = PG_SEC_REQ_PHASE.format(prefix) if isSecondary else PG_REQ_PHASE.format(prefix)
    reqPhase = symbol.getComponent().getSymbolValue(phaseKey)
    pgClkFreq = symbol.getComponent().getSymbolValue(PG_CLK_FREQ.format(prefix))
    setPhaseMinMax(symbol, prefix)

    if isRegValCalculation:
        symbol.setValue(getPhaseRegVal(reqPhase,pgClkFreq))
    else:
        symbol.setValue(getPhaseCalcVal(reqPhase,pgClkFreq))

def getOVRDATValue(lowValue,highValue):
    combinedValue = "{}_{}".format(lowValue, highValue)
    regValue = 0
    
    if combinedValue == "disabled_disabled":
        regValue = 0
    elif combinedValue == "disabled_enabled":
        regValue = 1
    elif combinedValue == "enabled_disabled":
        regValue = 2
    elif combinedValue == "enabled_enabled":
        regValue = 3
    
    return regValue

def getFLTDATValue(pollVal,polhVal):
    fltdatRegVal = 0
    
    if polhVal == "Active-high" and pollVal == "Active-high":
        fltdatRegVal = 0
    elif polhVal == "Active-high" and pollVal == "Active-low":
        fltdatRegVal = 1
    elif polhVal == "Active-low" and pollVal == "Active-high":
        fltdatRegVal = 2
    elif polhVal == "Active-low" and pollVal == "Active-low":
        fltdatRegVal = 3
    
    return fltdatRegVal

# ----------------------------- Callbacks and others -------------------------------------------------------------------

def setClockGeneratorData(valueGroupEntry):
    clkNode = getValueGroup(MODULE_NAME,valueGroupEntry).getChildren()
    for bitfield in clkNode:
        if "Clock Generator" in bitfield.getAttribute("caption"):
            return bitfield.getAttribute("caption")

def clockSourceSystemFreq(symbol, event):
    clockSelSym = event["source"].getSymbolByID(CONST_MCLKSEL)
    if clockSelSym.getSelectedKey() == STANDARD_SPEED_PERIPHERAL_CLOCK:
        symbol.setValue(int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_FREQ_SYM))) 
    elif clockSelSym.getSelectedKey() == CLOCK_GENERATOR:
        symbol.setValue(int(Database.getSymbolValue(CORE_COMPONENT, CLK_GEN_FREQ_SYM)))   

def clockCommentCb(symbol, event):
    updateClockComment(symbol)            

def updateClockComment(symbol):
    clockSelSym = symbol.getComponent().getSymbolByID(CONST_MCLKSEL)
    clockGenFreq = symbol.getComponent().getSymbolValue(CLK_FREQUENCY)
    if clockSelSym.getSelectedKey() == CLOCK_GENERATOR  and clockGenFreq == 0: 
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)  
    
def updatePGClkFreq(pgClkSrcSym):
    pgName = pgClkSrcSym.getID().split("_")[0]
    pgClkSrc = pgClkSrcSym.getComponent().getSymbolByID(PG_CLK_SRC.format(pgName))
    if pgClkSrc.getSelectedKey() == CLOCK_DIVIDER:
        return int(pgClkSrcSym.getComponent().getSymbolValue(CLK_DIV_FREQUENCY))
    return int(pgClkSrcSym.getComponent().getSymbolValue(CLK_FREQUENCY))

def updateMasterClkFreq(masterClkSrcSym):
    masterClkSrc = masterClkSrcSym.getComponent().getSymbolByID(MASTER_CLK_SRC)
    if masterClkSrc.getSelectedKey() == CLOCK_DIVIDER:
        return int(masterClkSrcSym.getComponent().getSymbolValue(CLK_DIV_FREQUENCY))
    return int(masterClkSrcSym.getComponent().getSymbolValue(CLK_FREQUENCY))

def getClkDividedFreq(pwmClkDivSym):
    clkDivider = int(pwmClkDivSym.getComponent().getSymbolByID(CONST_PWM_CLK_DIVIDER).getSelectedKey()[-1])
    clkFreq = pwmClkDivSym.getComponent().getSymbolValue(CLK_FREQUENCY)
    return clkFreq/clkDivider

def clkDIvFreqCallback(symbol,event):
    symbol.setValue(int(getClkDividedFreq(symbol.getComponent().getSymbolByID(CLK_DIV_FREQUENCY))))

def pgClkFreqCallback(symbol,event):
    symbol.setValue(updatePGClkFreq(symbol))

def masterClkFreqCallback(symbol,event):
    symbol.setValue(updateMasterClkFreq(symbol))

def periodCallback(symbol, prefix):
    component = symbol.getComponent()

    operatingMode = component.getSymbolByID("{}_{}".format(prefix,CONST_MODSEL)).getSelectedKey()
    outputMode = component.getSymbolByID("{}_{}".format(prefix,CONST_PMOD)).getSelectedKey()
    clkFreq = component.getSymbolValue(PG_CLK_FREQ.format(prefix))
    reqFreq = component.getSymbolValue(PG_REQ_PWM_FREQ.format(prefix))
    calcFreqSym = component.getSymbolByID(PG_CALC_PWM_FREQ.format(prefix))
    periodSym = component.getSymbolByID(PG_PERIOD.format(prefix))

    period = getPeriodFromFrequency(clkFreq, reqFreq, operatingMode, outputMode, MIN_PERIOD_VAL, MAX_PERIOD_VAL)
    calcFreq = getCalculatedFrequency(clkFreq, reqFreq, operatingMode, outputMode, MIN_PERIOD_VAL, MAX_PERIOD_VAL)

    periodSym.setValue(int(period))
    calcFreqSym.setValue(int(calcFreq))

def periodCalculationCb(symbol,event):
    pgOrMaster = getMasterOrPG(symbol,event)
    periodCallback(symbol,pgOrMaster)

def setFreqMinMaxValues(symbol,event):
    component = symbol.getComponent()
    masterOrPg = getMasterOrPG(symbol,event)

    operatingMode = component.getSymbolByID("{}_{}".format(masterOrPg,CONST_MODSEL)).getSelectedKey()
    outputMode = component.getSymbolByID("{}_{}".format(masterOrPg,CONST_PMOD)).getSelectedKey()
    clkFreq = component.getSymbolValue(PG_CLK_FREQ.format(masterOrPg)) 
    reqFreqSym = component.getSymbolByID(PG_REQ_PWM_FREQ.format(masterOrPg))

    reqFreqSym.setMin(getMinMaxFrequency(clkFreq,operatingMode,outputMode)["min"])
    reqFreqSym.setMax(getMinMaxFrequency(clkFreq,operatingMode,outputMode)["max"])

def getMasterSettings(symbol):
    component = symbol.getComponent()
    return {
        'operatingMode': component.getSymbolByID(MASTER_OPERATING_MODE).getSelectedKey(),
        'outputMode': component.getSymbolByID(MASTER_OUTPUT_MODE).getSelectedKey(),
        'clkSrc': component.getSymbolByID(MASTER_CLK_SRC).getSelectedKey(),
        'clkFreq': component.getSymbolValue(MASTER_CLK_FREQ),
        'reqFreq': component.getSymbolValue(MASTER_CALC_FREQ),
        'calcFreq': component.getSymbolValue(MASTER_CALC_FREQ),
        'period': component.getSymbolValue(MASTER_PERIOD)
    }

def getDefaultGenSettings(clkFreq):
    minMaxFreq = getMinMaxFrequency(clkFreq,DEF_OPERATING_MODE,DEF_OUTPUT_MODE)
    period = getPeriodFromFrequency(clkFreq, minMaxFreq["min"], DEF_OPERATING_MODE, DEF_OUTPUT_MODE, MIN_PERIOD_VAL, MAX_PERIOD_VAL)
    calcFreq = getCalculatedFrequency(clkFreq, minMaxFreq["min"], DEF_OPERATING_MODE, DEF_OUTPUT_MODE, MIN_PERIOD_VAL, MAX_PERIOD_VAL)

    return {
        "operatingMode": DEF_OPERATING_MODE,
        "outputMode": DEF_OUTPUT_MODE,
        "clkSrc": PWM_CLOCK,
        "clkFreq": clkFreq,
        "reqFreq": minMaxFreq["min"],
        "calcFreq": calcFreq,
        "period": period,
    }

def updateGenSettings(symbol, pgName, settings, readOnly):
    component = symbol.getComponent()
    pgOperatingModeSym = component.getSymbolByID("{}_{}".format(pgName, CONST_MODSEL))
    pgOutputModeSym = component.getSymbolByID("{}_{}".format(pgName, CONST_PMOD))
    pgClkSrcSym = component.getSymbolByID(PG_CLK_SRC.format(pgName))
    pgClkFreqSym = component.getSymbolByID(PG_CLK_FREQ.format(pgName))
    pgReqFreqSym = component.getSymbolByID(PG_REQ_PWM_FREQ.format(pgName))
    pgCalcFreqSym = component.getSymbolByID(PG_CALC_PWM_FREQ.format(pgName))
    pgPeriodSym = component.getSymbolByID(PG_PERIOD.format(pgName))

    pgOperatingModeSym.setSelectedKey(settings['operatingMode'])
    pgOperatingModeSym.setReadOnly(readOnly)

    pgOutputModeSym.setSelectedKey(settings['outputMode'])
    pgOutputModeSym.setReadOnly(readOnly)

    pgClkSrcSym.setSelectedKey(settings['clkSrc'])
    pgClkSrcSym.setReadOnly(readOnly)

    pgClkFreqSym.setValue(settings['clkFreq'])
    pgReqFreqSym.setVisible(not readOnly)
    pgReqFreqSym.setReadOnly(True)
    pgReqFreqSym.setValue(settings['calcFreq'])
    pgReqFreqSym.setReadOnly(False)
    pgCalcFreqSym.setValue(settings['calcFreq'])
    pgPeriodSym.setValue(settings['period'])

def useMasterPeriodCallback(symbol, event):
    masterSettings = getMasterSettings(symbol)
    component = symbol.getComponent()

    if event["id"] in [MASTER_OPERATING_MODE, MASTER_OUTPUT_MODE,MASTER_REQ_FREQ, MASTER_CALC_FREQ]:
        for gen in range(1, NUMBER_OF_GENERATORS + 1):
            if component.getSymbolValue("PG{}_USE_MASTER_PERIOD".format(gen)):
                updateGenSettings(symbol, "PG{}".format(gen), masterSettings, readOnly=True)
    else:
        pgName = symbol.getID().split("_")[0]
        if event["id"] == PG_USE_MASTER_PERIOD.format(pgName):
            useMasterPeriod = event["value"]
            if useMasterPeriod:
                updateGenSettings(symbol, pgName, masterSettings, readOnly=True)
            else:
                clkFreq = component.getSymbolValue(CLK_FREQUENCY)
                updateGenSettings(symbol, pgName, getDefaultGenSettings(clkFreq), readOnly=False)
    operatingModeVisibility(symbol,event)

def useMasterDCCallbck(symbol, event):
    getSymbolValue = symbol.getComponent().getSymbolValue
    getSymbolId = symbol.getComponent().getSymbolByID
    pgName = symbol.getID().split("_")[0]

    if getSymbolValue(PG_USE_MASTER_DC.format(pgName)) == True:
        getSymbolId(PG_PRIMARY_DC.format(pgName)).setReadOnly(True)
        getSymbolId(PG_SEC_DC.format(pgName)).setReadOnly(True)
        getSymbolId(PG_PRIMARY_DC.format(pgName)).setValue(getSymbolValue(MASTER_PRIMARY_DC))
        getSymbolId(PG_SEC_DC.format(pgName)).setValue(getSymbolValue(MASTER_SEC_DC))
    else:
        getSymbolId(PG_PRIMARY_DC.format(pgName)).setReadOnly(False)
        getSymbolId(PG_SEC_DC.format(pgName)).setReadOnly(False)     
        getSymbolId(PG_PRIMARY_DC.format(pgName)).setValue(0)
        getSymbolId(PG_SEC_DC.format(pgName)).setValue(0)

def useMasterPhaseCallbck(symbol,event):
    pgName = symbol.getID().split("_")[0]
    useMasterPhase = symbol.getComponent().getSymbolValue(PG_USE_MASTER_PHASE.format(pgName))
    outputMode = symbol.getComponent().getSymbolByID("{}_{}".format(pgName, CONST_PMOD)).getSelectedKey()

    primaryReqPhase = symbol.getComponent().getSymbolByID(PG_REQ_PHASE.format(pgName)) 
    secReqPhase = symbol.getComponent().getSymbolByID(PG_SEC_REQ_PHASE.format(pgName))
    primaryCalPhase = symbol.getComponent().getSymbolByID(PG_CAL_PHASE.format(pgName))
    secCalPhase = symbol.getComponent().getSymbolByID(PG_SEC_CAL_PHASE.format(pgName))

    primaryReqPhase.setReadOnly(useMasterPhase)
    secReqPhase.setReadOnly(useMasterPhase)
    primaryReqPhase.setVisible(not useMasterPhase)
    secReqPhase.setVisible(useMasterPhase == False and outputMode == INDEPENDENT_EDGE_DUAL_OUTPUT)

    primaryCalPhase.setValue(symbol.getComponent().getSymbolValue(MASTER_PRIMARY_CAL_PHASE) if useMasterPhase else 0)
    secCalPhase.setValue(symbol.getComponent().getSymbolValue(MASTER_SEC_CAL_PHASE) if useMasterPhase else 0)

def useMasterPeriodCmtVisibility(symbol,event):
    # show when useMasterPeriod is false and (useMasterDC or useMasterPhase) is true
    pgName = symbol.getID().split("_")[0]

    useMasterPeriod = symbol.getComponent().getSymbolValue(PG_USE_MASTER_PERIOD.format(pgName)) 
    useMasterDC = symbol.getComponent().getSymbolValue(PG_USE_MASTER_DC.format(pgName))
    useMasterPhase = symbol.getComponent().getSymbolValue(PG_USE_MASTER_PHASE.format(pgName))
    useMasterPeriodComment = symbol.getComponent().getSymbolByID(PG_USE_MASTER_PERIOD_COMMENT.format(pgName))

    if not useMasterPeriod and (useMasterDC or useMasterPhase):
        useMasterPeriodComment.setVisible(True)
    else:
        useMasterPeriodComment.setVisible(False)

def dcRegCallback(symbol,event):
    if MASTER in event["id"]:
        prefix = MASTER
    else:
        prefix = symbol.getID().split("_")[0]
        
    pgPrimaryDC = symbol.getComponent().getSymbolValue(PG_PRIMARY_DC.format(prefix))
    pgSecDC = symbol.getComponent().getSymbolValue(PG_SEC_DC.format(prefix))
    pgPeriod =  symbol.getComponent().getSymbolValue(PG_PERIOD.format(prefix))
                                                      
    symbol.getComponent().getSymbolByID(PG_PRIMARY_DC_REG_VAL.format(prefix)).setValue(int(pgPrimaryDC*0.01*(pgPeriod+16)))
    symbol.getComponent().getSymbolByID(PG_SEC_DC_REG_VAL.format(prefix)).setValue(int(pgSecDC*0.01*(pgPeriod+16)))

def setPhaseMinMax(symbol, prefix):
    pgClkFreq = symbol.getComponent().getSymbolValue(PG_CLK_FREQ.format(prefix))
    phaseMinMax = getMinMaxPhase(pgClkFreq)
    primaryReqPhase = symbol.getComponent().getSymbolByID(PG_REQ_PHASE.format(prefix))
    secReqPhase = symbol.getComponent().getSymbolByID(PG_SEC_REQ_PHASE.format(prefix))
    primaryCalPhase = symbol.getComponent().getSymbolByID(PG_CAL_PHASE.format(prefix))
    secCalPhase = symbol.getComponent().getSymbolByID(PG_SEC_CAL_PHASE.format(prefix))

    for sym in [primaryReqPhase, primaryCalPhase, secReqPhase, secCalPhase]:
        sym.setMin(phaseMinMax["min"])
        sym.setMax(phaseMinMax["max"])

def phaseCalcCallback(symbol, event):
    setPhaseSymValues(symbol, event, isSecondary=False, isRegValCalculation=False)

def phaseRegCallback(symbol, event):
    setPhaseSymValues(symbol, event, isSecondary=False, isRegValCalculation=True)

def secPhaseCalcCallback(symbol, event):
    setPhaseSymValues(symbol, event, isSecondary=True, isRegValCalculation=False)

def secPhaseRegCallback(symbol, event):
    setPhaseSymValues(symbol, event, isSecondary=True, isRegValCalculation=True)

def deadTimeCallback(symbol, event):
    prefix = symbol.getID().split("_")[0]
    outputMode = symbol.getComponent().getSymbolByID("{}_{}".format(prefix, CONST_PMOD)).getSelectedKey()
    setDTSymValues(symbol)
    isVisible = symbol.getComponent().getSymbolValue(PG_ENABLE.format(prefix)) == True and outputMode == DEF_OUTPUT_MODE
    symbol.getComponent().getSymbolByID(PG_DEAD_TIME_MENU.format(prefix)).setVisible(isVisible)

def setDTSymValues(symbol):
    prefix = symbol.getID().split("_")[0]
    component = symbol.getComponent()
    pgClkFreq = component.getSymbolValue(PG_CLK_FREQ.format(prefix))
    deadTimeMinMax = getMinMaxDeadTime(pgClkFreq)

    symbols = {
        "deadTimeHighSym": component.getSymbolByID(PG_DEAD_TIME_HIGH.format(prefix)),
        "deadTimeLowSym": component.getSymbolByID(PG_DEAD_TIME_LOW.format(prefix)),
        "deadTimeHighCalcSym": component.getSymbolByID(PG_CALC_DEAD_TIME_HIGH.format(prefix)),
        "deadTimeLowCalcSym": component.getSymbolByID(PG_CALC_DEAD_TIME_LOW.format(prefix)),
        "deadTimeHighRegSym": component.getSymbolByID(PG_DEAD_TIME_HIGH_REG_VAL.format(prefix)),
        "deadTimeLowRegSym": component.getSymbolByID(PG_DEAD_TIME_LOW_REG_VAL.format(prefix)),
    }

    # Set min and max values for dead time symbols
    for sym in [symbols["deadTimeHighSym"], symbols["deadTimeLowSym"], symbols["deadTimeHighCalcSym"], symbols["deadTimeLowCalcSym"]]:
        sym.setMin(deadTimeMinMax["min"])
        sym.setMax(deadTimeMinMax["max"])

    # Handle the case when DEF_OUTPUT_MODE is False or pgCalcFreq is 0
    if DEF_OUTPUT_MODE and pgClkFreq != 0:
        reqDTHigh = component.getSymbolValue(PG_DEAD_TIME_HIGH.format(prefix))
        reqDTLow = component.getSymbolValue(PG_DEAD_TIME_LOW.format(prefix))

        # Calculate dead time register and calculated values
        deadTimeHighRegVal = getDeadTimeRegVal(reqDTHigh, pgClkFreq)
        deadTimeHighCalcVal = getDTCalcVal(reqDTHigh, pgClkFreq)
        deadTimeLowRegVal = getDeadTimeRegVal(reqDTLow, pgClkFreq)
        deadTimeLowCalcVal = getDTCalcVal(reqDTLow, pgClkFreq)
    else:
        deadTimeHighRegVal = deadTimeHighCalcVal = deadTimeLowRegVal = deadTimeLowCalcVal = 0

    # Set calculated values to their respective symbols
    symbols["deadTimeHighRegSym"].setValue(deadTimeHighRegVal)
    symbols["deadTimeHighCalcSym"].setValue(deadTimeHighCalcVal)
    symbols["deadTimeLowRegSym"].setValue(deadTimeLowRegVal)
    symbols["deadTimeLowCalcSym"].setValue(deadTimeLowCalcVal)

def setVisibility(component, prefix, symbol_ids, visibility):
    for symbol_id in symbol_ids:
        component.getSymbolByID("{}_{}".format(prefix, symbol_id)).setVisible(visibility)

def operatingModeVisibility(symbol, event):
    prefix = MASTER if MASTER in event["id"] else symbol.getID().split("_")[0]
    component = symbol.getComponent()
    operatingMode = component.getSymbolByID("{}_{}".format(prefix, CONST_MODSEL)).getSelectedKey()

    primary_symbols = ["PRIMARY_REQ_PHASE", "PRIMARY_CAL_PHASE"]
    secondary_symbols = ["SEC_REQ_PHASE", "SEC_DC", "SEC_CAL_PHASE"]

    setVisibility(component, prefix, primary_symbols, operatingMode != CENTER_ALIGNED)
    setVisibility(component, prefix, secondary_symbols, INDEPENDENT_EDGE_DUAL_OUTPUT == operatingMode)

def updateOVRDAT(symbol,event):
    prefix = symbol.getID().split("_")[0]
    overrideLow = symbol.getComponent().getSymbolByID("{}_{}".format(prefix, CONST_OVRENL)).getSelectedKey()
    overrideHigh = symbol.getComponent().getSymbolByID("{}_{}".format(prefix, CONST_OVRENH)).getSelectedKey()

    ovrdatValue = getOVRDATValue(overrideLow,overrideHigh)
    symbol.setValue(ovrdatValue)

def updateFLTDAT(symbol,event):
    prefix = symbol.getID().split("_")[0]
    polarityLow = symbol.getComponent().getSymbolByID("{}_{}".format(prefix, CONST_POLL)).getSelectedKey()
    polarityHigh = symbol.getComponent().getSymbolByID("{}_{}".format(prefix, CONST_POLH)).getSelectedKey()

    ovrdatValue = getFLTDATValue(polarityLow,polarityHigh)
    symbol.setValue(ovrdatValue)

def setVisible(symbol,event):
    symbol.setVisible(event["value"])

def pinsCallback(symbol,event):
    pgName = symbol.getID().split("_")[0]
    ppsen = symbol.getComponent().getSymbolByID("{}_{}".format(pgName,CONST_PPSEN)).getSelectedKey()
    penl = symbol.getComponent().getSymbolByID("{}_{}".format(pgName, CONST_PENL)).getSelectedKey()
    penh = symbol.getComponent().getSymbolByID("{}_{}".format(pgName, CONST_PENH)).getSelectedKey()
    commentSym = symbol.getComponent().getSymbolByID("{}_PINS_COMMENT".format(pgName))
    comment = ""
    ppsSuffix= "" if ppsen == "enabled" else "-"
    ppsOrNonpps = "(PPS)" if ppsen == "enabled" else "(NON-PPS)"
    if penl == "enabled" and penh == "enabled":
        comment = "Warning!!!! Go to Pin Configuration and set PWM{}{}L and PWM{}{}H {} pins".format(pgName[-1],ppsSuffix,pgName[-1],ppsSuffix,ppsOrNonpps)
    elif penl == "enabled":
        comment = "Warning!!!! Go to Pin Configuration and set PWM{}{}L {} pin".format(pgName[-1],ppsSuffix,ppsOrNonpps)
    elif penh == "enabled":
        comment = "Warning!!!! Go to Pin Configuration and set PWM{}{}H {} pin".format(pgName[-1],ppsSuffix,ppsOrNonpps)
    else:
        comment = "Warning!!!! Enable the bit here and configure the pins in the Pins Module."

    commentSym.setLabel(comment)

def interruptCallback(symbol, event):
    if "ENABLE" in event["id"]:
        symbol.setVisible(event["value"])
    for i in range(1, NUMBER_OF_GENERATORS + 1):
        interruptName = "PWM{}Interrupt".format(i)
        if interruptName in interruptVectorData:
            interruptIndex = interruptVectorData[interruptName]
            isInterruptEnabled = symbol.getComponent().getSymbolValue(PG_INTERRUPT_ENABLE.format(i)) == True and symbol.getComponent().getSymbolValue(PG_ENABLE.format("PG{}".format(i)))
            Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(interruptIndex), isInterruptEnabled)
            Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_HANDLER_LOCK".format(interruptIndex), isInterruptEnabled)

def interruptStatusWarning(symbol, event):
    showWarning = False
    intList = []
    for i in range(1, NUMBER_OF_GENERATORS + 1):
        interruptName = "PWM{}Interrupt".format(i)
        interruptIndex = interruptVectorData[interruptName]
        if symbol.getComponent().getSymbolValue(PG_INTERRUPT_ENABLE.format(i)) == True and symbol.getComponent().getSymbolValue(PG_ENABLE.format("PG{}".format(i))) == True and Database.getSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(interruptIndex)) == False:
            showWarning = True
            intList.append(interruptName)

    symbol.setVisible(showWarning)
    symbol.setLabel("Warning!!! Enable {} in Interrupts Section of System module".format(', '.join(str(i) for i in intList)))

def updateBoolToKeyValueCb(symbol,event):
    eventVal = "enabled" if event["value"] == True else "disabled"
    symbol.setSelectedKey(eventVal)

def combineDeadTimeRegisters(symbol,event):
    prefix = symbol.getID().split("_")[0]
    deadTimeLow = symbol.getComponent().getSymbolValue(PG_DEAD_TIME_LOW_REG_VAL.format(prefix))
    deadTimeHigh = symbol.getComponent().getSymbolValue(PG_DEAD_TIME_HIGH_REG_VAL.format(prefix))
    if not ( MIN_DEADTIME_VAL <= deadTimeLow <= MAX_DEADTIME_VAL) or not (MIN_DEADTIME_VAL <= deadTimeHigh <= MAX_DEADTIME_VAL):
        return MIN_DEADTIME_VAL
    symbol.setValue((deadTimeHigh << 16) | deadTimeLow)

def updateActiveGenList(symbol,event):
    genNum = int(event["id"].split("_")[0].replace("PG",""))
    if event["value"] == True:
        activeGenList.append(genNum)
    else:
        activeGenList.remove(genNum)
    activeGenList.sort()
    symbol.getComponent().getSymbolByID("regPorSet").setValue(createRegPorSetString())

def updatePSS(symbol,event):
    prefix = event["id"].split("_")[0]
    pssValueGrpName = getValueGroupName(MODULE_NAME, "PG","FPCI","PSS")
    pssValGrp = getValueGroup(MODULE_NAME,CONST_PSS)
    selectedPSS = symbol.getComponent().getSymbolByID("{}_{}".format(prefix,pssValueGrpName)).getSelectedKey()
    
    for option in pssValGrp.getChildren():
        if option.getAttribute("caption") == selectedPSS:
            symbol.setValue(int(option.getAttribute("value"),16))
            break

def updateADTRPSHexSym(symbol,event):
    prefix = event["id"].split("_")[0]
    pssValueGrpName = getValueGroupName(MODULE_NAME, "PG","EVT","ADTR1PS")
    pssValGrp = getValueGroup(MODULE_NAME,CONST_ADTRPS)
    selectedPSS = symbol.getComponent().getSymbolByID("{}_{}".format(prefix,pssValueGrpName)).getSelectedKey()

    for option in pssValGrp.getChildren():
        if option.getAttribute("caption") == selectedPSS:
            symbol.setValue(int(option.getAttribute("value"),16))
            break

def updateADTROFSHexSym(symbol,event):
    prefix = event["id"].split("_")[0]
    pssValueGrpName = getValueGroupName(MODULE_NAME, "PG","EVT","ADTR1OFS")
    pssValGrp = getValueGroup(MODULE_NAME,CONST_ADTROFS)
    selectedPSS = symbol.getComponent().getSymbolByID("{}_{}".format(prefix,pssValueGrpName)).getSelectedKey()

    for option in pssValGrp.getChildren():
        if option.getAttribute("caption") == selectedPSS:
            symbol.setValue(int(option.getAttribute("value"),16))
            break

def anyGenInUse(symbol,event):
    anyGenInUse = False
    for i in range(1, NUMBER_OF_GENERATORS+1):
        if symbol.getComponent().getSymbolValue(PG_ENABLE.format("PG" + str(i))) == True:
            anyGenInUse = True
            break
    
    symbol.setValue(anyGenInUse)

NUMBER_OF_GENERATORS = getParamValue("num_gen","int")
MIN_PERIOD_VAL = getParamValue("periodMinValue")
MAX_PERIOD_VAL = getParamValue("periodMaxValue")
MIN_DC_VAL = getParamValue("dutyCycleMinLimit")
MIN_PHASE_VAL = getParamValue("phaseMinValue")
MAX_PHASE_VAL = getParamValue("phaseMaxValue")
MIN_DEADTIME_VAL = getParamValue("deadTimeMinLimit")
MAX_DEADTIME_VAL = getParamValue("deadTimeMaxLimit")
MIN_TRG_VAL = getParamValue("trigCompareMinLimit")
MAX_TRG_VAL = getParamValue("trigCompareMaxLimit")

CONST_MCLKSEL = getValueGroupName(MODULE_NAME,"PCLKCON","PCLKCON","MCLKSEL")
CONST_PWM_CLK_DIVIDER = getValueGroupName(MODULE_NAME,"PCLKCON","PCLKCON","DIVSEL")
CONST_MODSEL = getValueGroupName(MODULE_NAME,"PG","CON","MODSEL")
CONST_PMOD = getValueGroupName(MODULE_NAME,"PG","IOCON","PMOD")
CONST_PENL = getValueGroupName(MODULE_NAME, "PG","IOCON","PENL")
CONST_PENH = getValueGroupName(MODULE_NAME, "PG","IOCON","PENH")
CONST_PPSEN = getValueGroupName(MODULE_NAME, "PG","IOCON","PPSEN")
CONST_OVRENL = getValueGroupName(MODULE_NAME, "PG","IOCON","OVRENL")
CONST_OVRENH = getValueGroupName(MODULE_NAME, "PG","IOCON","OVRENH")
CONST_POLL = getValueGroupName(MODULE_NAME, "PG","IOCON","POLL")
CONST_POLH = getValueGroupName(MODULE_NAME, "PG","IOCON","POLH")
CONST_PSS = getValueGroupName(MODULE_NAME, "PG","FPCI","PSS")
CONST_ADTRPS = getValueGroupName(MODULE_NAME, "PG","EVT","ADTR1PS")
CONST_ADTROFS = getValueGroupName(MODULE_NAME, "PG","EVT","ADTR1OFS")
CLOCK_GENERATOR = setClockGeneratorData(CONST_MCLKSEL)
CLK_GEN_FREQ_SYM = "clkGen" + CLOCK_GENERATOR[-1] + "OutFrequency"
MASTER_OPERATING_MODE = "MASTER_{}".format(CONST_MODSEL)
MASTER_OUTPUT_MODE = "MASTER_{}".format(CONST_PMOD)
MASTER_CLK_FREQ = MASTER_CLK_FREQ

DEF_OPERATING_MODE = getDefaultValue(MODULE_NAME,"PG","CON","MODSEL")
DEF_OUTPUT_MODE = getDefaultValue(MODULE_NAME,"PG","IOCON","PMOD")

def instantiateComponent(pwmComponent):
    pwmInterrupts = pwmComponent.createBooleanSymbol(ENABLE_INTERRUPT,None)
    pwmInterrupts.setLabel("Enable Interrupts")
    pgList = [PG_ENABLE.format("PG" + str(i)) for i in range(1, NUMBER_OF_GENERATORS+1)]
    pgIntList = [PG_INTERRUPT_ENABLE.format(str(i)) for i in range(1, NUMBER_OF_GENERATORS+1)]
    pwmInterrupts.setDependencies(updateInterruptSym, pgList + pgIntList)
    pwmInterrupts.setVisible(False)

    interruptWarning = pwmComponent.createCommentSymbol(ENABLE_INTERRUPT_COMMENT, None)
    interruptWarning.setVisible(False)
    populateIntVectorData()
    interruptWarning.setDependencies(interruptStatusWarning,["{}.INTC_{}_ENABLE".format(CORE_COMPONENT,i) for i in interruptVectorData.values()])

    pwmClockMenu = pwmComponent.createMenuSymbol("PWM_CLOCK_MENU", None)
    pwmClockMenu.setLabel("Clock Configuration")

    pwmClkSrc = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PCLKCON","PCLKCON","MCLKSEL",pwmClockMenu,0,False)  
    pwmClkSrc.setLabel("PWM Master Clock Selection")
    pwmClkSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PCLKCON")

    clkComment = pwmComponent.createCommentSymbol(CLOCK_COMMENT, pwmClockMenu)
    clkComment.setVisible(False)
    clkComment.setLabel("Warning!!! Enable and configure PWM Clock Generator in Clock Section of System Module")
    clkComment.setDependencies(clockCommentCb, [CONST_MCLKSEL,CLK_FREQUENCY])

    pwmClkFreq = pwmComponent.createIntegerSymbol(CLK_FREQUENCY,pwmClockMenu)
    pwmClkFreq.setLabel("PWM Master Clock Frequency(Hz)")
    pwmClkFreq.setReadOnly(True)
    pwmClkFreq.setDefaultValue(int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_FREQ_SYM) or 0))
    pwmClkFreq.setDependencies(clockSourceSystemFreq, [CONST_MCLKSEL,CORE_COMPONENT+"."+SYSTEM_FREQ_SYM,CORE_COMPONENT+"."+CLK_GEN_FREQ_SYM])

    pwmClkDiv = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PCLKCON","PCLKCON","DIVSEL",pwmClockMenu,0,False)  
    pwmClkDiv.setLabel("Clock Divider")
    pwmClkDiv.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PCLKCON")

    pwmClkDivFreq = pwmComponent.createIntegerSymbol(CLK_DIV_FREQUENCY,pwmClockMenu)
    pwmClkDivFreq.setLabel("Clock Divided Frequency(Hz)")
    pwmClkDivFreq.setReadOnly(True)
    pwmClkDivFreq.setDefaultValue(getClkDividedFreq(pwmClkDivFreq))
    pwmClkDivFreq.setDependencies(clkDIvFreqCallback, [CLK_FREQUENCY,CONST_PWM_CLK_DIVIDER,CONST_MCLKSEL,CORE_COMPONENT+"."+SYSTEM_FREQ_SYM,CORE_COMPONENT+"."+CLK_GEN_FREQ_SYM])

    # Master Settings
    masterSettingsMenu = pwmComponent.createMenuSymbol("MASTER_SETTINGS", None)
    masterSettingsMenu.setLabel("Master Settings")

    masterClkSrc = pwmComponent.createKeyValueSetSymbol(MASTER_CLK_SRC,masterSettingsMenu)
    masterClkSrc.addKey("PWM Master Clock","1","PWM Master Clock")
    masterClkSrc.addKey("Clock Divider","2","Clock Divider")
    masterClkSrc.setLabel("Master Settings Clock Selection")
    masterClkSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

    masterClkFreq = pwmComponent.createIntegerSymbol(MASTER_CLK_FREQ,masterSettingsMenu)
    masterClkFreq.setLabel("Master Settings Clock Frequency(Hz)")
    masterClkFreq.setReadOnly(True)
    masterClkFreq.setDefaultValue(updateMasterClkFreq(masterClkSrc))
    masterClkFreq.setDependencies(masterClkFreqCallback,[MASTER_CLK_SRC,CLK_FREQUENCY,CLK_DIV_FREQUENCY])

    masterOperatingMode = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","CON","MODSEL",masterSettingsMenu,0,True)  
    masterOperatingMode.setLabel("Operating Mode")
    masterOperatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

    masterOutputMode = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","PMOD",masterSettingsMenu,0,True)  
    masterOutputMode.setLabel("Output Mode")
    masterOutputMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

    masterReqPWMFreq = pwmComponent.createIntegerSymbol(MASTER_REQ_FREQ,masterSettingsMenu)
    masterReqPWMFreq.setLabel("Requested PWM Frequency(Hz)")
    pwmMinMaxFreq = getMinMaxFrequency(masterClkFreq.getValue(), DEF_OPERATING_MODE,DEF_OUTPUT_MODE)
    masterReqPWMFreq.setMin(pwmMinMaxFreq["min"])
    masterReqPWMFreq.setMax(pwmMinMaxFreq["max"])
    masterReqPWMFreq.setDependencies(setFreqMinMaxValues,[MASTER_OPERATING_MODE,MASTER_OUTPUT_MODE,MASTER_CLK_FREQ])

    masterCalPWMFreq = pwmComponent.createIntegerSymbol(MASTER_CALC_FREQ,masterSettingsMenu)
    masterCalPWMFreq.setLabel("Calculated PWM Frequency(Hz)")
    masterCalPWMFreq.setReadOnly(True)
    
    masterPeriod = pwmComponent.createHexSymbol(MASTER_PERIOD,masterSettingsMenu)
    masterPeriod.setLabel("Period (MPER)")
    masterPeriod.setReadOnly(True)
    masterPeriod.setDependencies(periodCalculationCb,[MASTER_REQ_FREQ,MASTER_CLK_FREQ,MASTER_OPERATING_MODE,MASTER_OUTPUT_MODE])
    periodCallback(masterPeriod,MASTER)
    masterPeriod.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:MPER")

    masterPrimaryDC = pwmComponent.createFloatSymbol(MASTER_PRIMARY_DC,masterSettingsMenu)
    masterPrimaryDC.setLabel("Duty Cycle(%)")
    masterPrimaryDC.setMin(0)
    masterPrimaryDC.setMax(100)
    masterPrimaryDC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:MDC")

    masterDCReg = pwmComponent.createHexSymbol(MASTER_PRIMARY_DC_REG_VAL,masterSettingsMenu)
    masterDCReg.setLabel("Duty Cycle Register Value")  
    masterDCReg.setVisible(False)
    masterDCReg.setDependencies(dcRegCallback,[MASTER_PRIMARY_DC,MASTER_CLK_FREQ,MASTER_CALC_FREQ])

    masterSecDC = pwmComponent.createFloatSymbol(MASTER_SEC_DC,masterSettingsMenu)
    masterSecDC.setLabel("Secondary Duty Cycle(%)")
    masterSecDC.setVisible(False)
    masterSecDC.setMin(0)
    masterSecDC.setMax(100)
    masterSecDC.setDependencies(operatingModeVisibility,[MASTER_SEC_DC,MASTER_CALC_FREQ]) 
    masterSecDC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGB")

    masterSecDCReg = pwmComponent.createHexSymbol(MASTER_SEC_DC_REG_VAL,masterSettingsMenu)
    masterSecDCReg.setLabel("Secondary Duty Cycle Register Value")  
    masterSecDCReg.setVisible(False)
    masterSecDCReg.setDependencies(dcRegCallback,[MASTER_SEC_DC,MASTER_CALC_FREQ])

    masterReqPhase = pwmComponent.createFloatSymbol(MASTER_PRIMARY_REQ_PHASE,masterSettingsMenu)
    masterReqPhase.setLabel("Requested Phase(us)")
    masterReqPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:MPHASE")

    masterCalPhase = pwmComponent.createFloatSymbol(MASTER_PRIMARY_CAL_PHASE,masterSettingsMenu)
    masterCalPhase.setLabel("Calculated Phase(us)")
    masterCalPhase.setReadOnly(True)
    masterCalPhase.setDependencies(phaseCalcCallback,[MASTER_PRIMARY_REQ_PHASE,MASTER_CALC_FREQ])

    masterPhaseReg = pwmComponent.createHexSymbol(MASTER_PHASE_REG_VAL,masterSettingsMenu)
    masterPhaseReg.setLabel("Phase Register Value")    
    masterPhaseReg.setReadOnly(True)
    masterPhaseReg.setVisible(False)
    masterPhaseReg.setDependencies(phaseRegCallback,[MASTER_PRIMARY_REQ_PHASE,MASTER_CALC_FREQ])

    masterSecReqPhase = pwmComponent.createFloatSymbol(MASTER_SEC_REQ_PHASE,masterSettingsMenu)
    masterSecReqPhase.setLabel("Requested Secondary Phase(us)")
    masterSecReqPhase.setVisible(False)
    masterSecReqPhase.setDependencies(operatingModeVisibility,[MASTER_OPERATING_MODE])
    masterSecReqPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGA")

    masterSecCalPhase = pwmComponent.createFloatSymbol(MASTER_SEC_CAL_PHASE,masterSettingsMenu)
    masterSecCalPhase.setLabel("Calculated Secondary Phase(us)")
    masterSecCalPhase.setReadOnly(True)
    masterSecCalPhase.setVisible(False)
    masterSecCalPhase.setDependencies(secPhaseCalcCallback,[MASTER_SEC_REQ_PHASE,MASTER_CALC_FREQ])

    masterSecPhaseReg = pwmComponent.createHexSymbol(MASTER_SEC_PHASE_REG_VAL,masterSettingsMenu)
    masterSecPhaseReg.setLabel("Secondary Phase Register Value")    
    masterSecPhaseReg.setReadOnly(True)
    masterSecPhaseReg.setVisible(False)
    masterSecPhaseReg.setDependencies(secPhaseRegCallback,[MASTER_SEC_REQ_PHASE,MASTER_CALC_FREQ])
    setPhaseMinMax(masterReqPhase,MASTER)

    #Channel Configurations
    pgConfigMenu = pwmComponent.createMenuSymbol("GENERATOR_CONFIGURATIONS", None)
    pgConfigMenu.setLabel("PWM Generator Configuration")

    for gen in range (1,NUMBER_OF_GENERATORS+1):
        pgName = "PG{}".format(gen)

        pgMenu = pwmComponent.createBooleanSymbol(PG_ENABLE.format(pgName), pgConfigMenu)
        pgMenu.setLabel("Use PWM Generator {}".format(gen))
        pgMenu.setDependencies(updateActiveGenList,[PG_ENABLE.format(pgName)])

        pgInterrupt = pwmComponent.createBooleanSymbol(PG_INTERRUPT_ENABLE.format(gen),pgMenu)
        pgInterrupt.setLabel("Enable Interrupt")
        pgInterrupt.setVisible(False)
        pgInterrupt.setDependencies(interruptCallback, [PG_ENABLE.format(pgName),PG_INTERRUPT_ENABLE.format(gen)])
        pgInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:intc_04436;register:IFS1")

        pgON = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","ON",pgMenu,gen,False)
        pgON.setLabel("Enable During Initialization")
        pgON.setVisible(False)
        pgON.setDependencies(setVisible,[PG_ENABLE.format(pgName)])
        pgON.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgClockMenu = pwmComponent.createMenuSymbol(PG_CLOCK_MENU.format(pgName), pgMenu)
        pgClockMenu.setLabel("Clock Configuration")
        pgClockMenu.setVisible(False)
        pgClockMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgClkSrc = pwmComponent.createKeyValueSetSymbol(PG_CLK_SRC.format(pgName),pgClockMenu)
        pgClkSrc.addKey("PWM Master Clock","1","PWM Master Clock")
        pgClkSrc.addKey("Clock Divider","2","Clock Divider")
        pgClkSrc.setLabel("PG Clock Selection")
        pgClkSrc.setOutputMode("Value")
        pgClkSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgClkFreq = pwmComponent.createIntegerSymbol(PG_CLK_FREQ.format(pgName),pgClockMenu)
        pgClkFreq.setLabel("PG{} Clock Frequency(Hz)".format(gen))
        pgClkFreq.setReadOnly(True)
        pgClkFreq.setDefaultValue(updatePGClkFreq(pgClkSrc))
        pgClkFreq.setDependencies(pgClkFreqCallback,[PG_CLK_SRC.format(pgName),CLK_FREQUENCY,CLK_DIV_FREQUENCY])

        pgOperationMenu = pwmComponent.createMenuSymbol(PG_OPERATION_MENU.format(pgName),pgMenu)
        pgOperationMenu.setLabel("PWM Modes")
        pgOperationMenu.setVisible(False)
        pgOperationMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgUseMasterPeriod = pwmComponent.createBooleanSymbol(PG_USE_MASTER_PERIOD.format(pgName), pgOperationMenu)
        pgUseMasterPeriod.setLabel("Use Master Period")
        pgUseMasterPeriod.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")
        
        pgUseMasterDC = pwmComponent.createBooleanSymbol(PG_USE_MASTER_DC.format(pgName), pgOperationMenu)
        pgUseMasterDC.setLabel("Use Master Duty Cycle")
        pgUseMasterDC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgUseMasterPhase = pwmComponent.createBooleanSymbol(PG_USE_MASTER_PHASE.format(pgName), pgOperationMenu)
        pgUseMasterPhase.setLabel("Use Master Phase")
        pgUseMasterPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgMPERSEL = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","MPERSEL",pgOperationMenu,gen,False)
        pgMPERSEL.setVisible(False)
        pgMPERSEL.setDependencies(updateBoolToKeyValueCb,[PG_USE_MASTER_PERIOD.format(pgName)])

        pgMDCSEL = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","MDCSEL",pgOperationMenu,gen,False)
        pgMDCSEL.setDependencies(updateBoolToKeyValueCb,[PG_USE_MASTER_DC.format(pgName)])
        pgMDCSEL.setVisible(False)

        pgMPHSEL = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","MPHSEL",pgOperationMenu,gen,False)
        pgMPHSEL.setDependencies(updateBoolToKeyValueCb,[PG_USE_MASTER_PHASE.format(pgName)])
        pgMPHSEL.setVisible(False)

        pgUseMasterPerCmt = pwmComponent.createCommentSymbol(PG_USE_MASTER_PERIOD_COMMENT.format(pgName), pgOperationMenu)
        pgUseMasterPerCmt.setVisible(False)
        pgUseMasterPerCmt.setLabel("******** Warning!!! Enable Use Master Period ********")
        pgUseMasterPerCmt.setDependencies(useMasterPeriodCmtVisibility, [PG_USE_MASTER_PERIOD.format(pgName),PG_USE_MASTER_DC.format(pgName),PG_USE_MASTER_PHASE.format(pgName),])

        pgOperatingMode = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","CON","MODSEL",pgOperationMenu,gen,False)  
        pgOperatingMode.setLabel("Operating Mode")
        pgOperatingMode.setOutputMode("Value")
        pgOperatingMode.setDependencies(useMasterPeriodCallback,[PG_USE_MASTER_PERIOD.format(pgName),MASTER_OPERATING_MODE,MASTER_OUTPUT_MODE,MASTER_CALC_FREQ])
        pgOperatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgOutputMode = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","PMOD",pgOperationMenu,gen,False)  
        pgOutputMode.setLabel("Output Mode")
        pgOutputMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgReqPWMFreq = pwmComponent.createIntegerSymbol(PG_REQ_PWM_FREQ.format(pgName),pgOperationMenu)
        pgReqPWMFreq.setLabel("Requested Frequency(Hz)")
        pgReqPWMFreq.setMin(pwmMinMaxFreq["min"])
        pgReqPWMFreq.setMax(pwmMinMaxFreq["max"])
        pgReqPWMFreq.setDependencies(setFreqMinMaxValues,[PG_CLK_FREQ.format(pgName),"{}_{}".format(pgName,CONST_MODSEL),"{}_{}".format(pgName,CONST_PMOD)])

        pgCalPWMFreq = pwmComponent.createIntegerSymbol(PG_CALC_PWM_FREQ.format(pgName),pgOperationMenu)
        pgCalPWMFreq.setLabel("Calculated Frequency(Hz)")
        pgCalPWMFreq.setReadOnly(True)

        pgPeriod = pwmComponent.createHexSymbol(PG_PERIOD.format(pgName),pgOperationMenu)
        pgPeriod.setLabel("PG Period")
        pgPeriod.setReadOnly(True)
        pgPeriod.setMin(MIN_PERIOD_VAL)
        pgPeriod.setMax(MAX_PERIOD_VAL)
        pgPeriod.setDependencies(periodCalculationCb,[PG_REQ_PWM_FREQ.format(pgName),PG_CLK_FREQ.format(pgName),"{}_{}".format(pgName,CONST_MODSEL),"{}_{}".format(pgName,CONST_PMOD)])
        periodCallback(pgPeriod,pgName)
        pgPeriod.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxPER")
        
        pgPrimaryDC = pwmComponent.createFloatSymbol(PG_PRIMARY_DC.format(pgName),pgOperationMenu)
        pgPrimaryDC.setLabel("Duty Cycle(%)")
        pgPrimaryDC.setMin(0)
        pgPrimaryDC.setMax(100)
        pgPrimaryDC.setDependencies(useMasterDCCallbck,[PG_USE_MASTER_PERIOD.format(pgName),PG_USE_MASTER_DC.format(pgName),MASTER_OPERATING_MODE,MASTER_OUTPUT_MODE,MASTER_PRIMARY_DC])
        pgPrimaryDC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxDC")

        pgPrimaryDCRegVal = pwmComponent.createHexSymbol(PG_PRIMARY_DC_REG_VAL.format(pgName),pgOperationMenu)
        pgPrimaryDCRegVal.setLabel("Duty Cycle Register Value")
        pgPrimaryDCRegVal.setReadOnly(True)
        pgPrimaryDCRegVal.setVisible(False)
        pgPrimaryDCRegVal.setDefaultValue(int(pgPrimaryDC.getValue()*(pgPeriod.getValue()+16)))
        pgPrimaryDCRegVal.setDependencies(dcRegCallback,[PG_PRIMARY_DC.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])

        pgSecDC = pwmComponent.createFloatSymbol(PG_SEC_DC.format(pgName),pgOperationMenu)
        pgSecDC.setLabel("Secondary Duty Cycle(%)")
        pgSecDC.setVisible(False)
        pgSecDC.setMin(0)
        pgSecDC.setMax(100)
        pgSecDC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGB")
        
        pgSecDCRegVal = pwmComponent.createHexSymbol(PG_SEC_DC_REG_VAL.format(pgName),pgOperationMenu)
        pgSecDCRegVal.setLabel("Secondary Duty Cycle Register Value")
        pgSecDCRegVal.setReadOnly(True)
        pgSecDCRegVal.setVisible(False)
        pgSecDCRegVal.setDefaultValue(int(pgSecDC.getValue()*(pgPeriod.getValue()+16)))
        pgSecDCRegVal.setDependencies(dcRegCallback,[PG_SEC_DC.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])

        pgReqPhase = pwmComponent.createFloatSymbol(PG_REQ_PHASE.format(pgName),pgOperationMenu)
        pgReqPhase.setLabel("Requested Phase(us)")
        pgReqPhase.setDependencies(useMasterPhaseCallbck,[PG_USE_MASTER_PERIOD.format(pgName),PG_USE_MASTER_PHASE.format(pgName),MASTER_OPERATING_MODE,MASTER_OUTPUT_MODE,MASTER_PRIMARY_CAL_PHASE,MASTER_SEC_CAL_PHASE])
        pgReqPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxPHASE")

        pgCalPhase = pwmComponent.createFloatSymbol(PG_CAL_PHASE.format(pgName),pgOperationMenu)
        pgCalPhase.setLabel("Calculated Phase(us)")
        pgCalPhase.setReadOnly(True)
        pgCalPhase.setDependencies(phaseCalcCallback,[PG_REQ_PHASE.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])
        
        pgPhaseRegVal = pwmComponent.createHexSymbol(PG_PHASE_REG_VAL.format(pgName),pgOperationMenu)
        pgPhaseRegVal.setLabel("Phase Register Value")
        pgPhaseRegVal.setReadOnly(True)
        pgPhaseRegVal.setVisible(False)
        pgPhaseRegVal.setDependencies(phaseRegCallback,[PG_REQ_PHASE.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])

        pgSecReqPhase = pwmComponent.createFloatSymbol(PG_SEC_REQ_PHASE.format(pgName),pgOperationMenu)
        pgSecReqPhase.setLabel("Secondary Requested Phase(us)")
        pgSecReqPhase.setVisible(False)
        pgSecReqPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGA")
        
        pgSecCalPhase = pwmComponent.createFloatSymbol(PG_SEC_CAL_PHASE.format(pgName),pgOperationMenu)
        pgSecCalPhase.setLabel("Secondary Calculated Phase(us)")
        pgSecCalPhase.setReadOnly(True)
        pgSecCalPhase.setVisible(False)
        pgSecCalPhase.setDependencies(secPhaseCalcCallback,[PG_SEC_REQ_PHASE.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])

        pgSecPhaseRegVal = pwmComponent.createHexSymbol(PG_SEC_PHASE_REG_VAL.format(pgName),pgOperationMenu)
        pgSecPhaseRegVal.setLabel("Secondary Phase Register Value")
        pgSecPhaseRegVal.setReadOnly(True)
        pgSecPhaseRegVal.setVisible(False)
        pgSecPhaseRegVal.setDependencies(secPhaseRegCallback,[PG_SEC_REQ_PHASE.format(pgName),PG_CALC_PWM_FREQ.format(pgName)])
        setPhaseMinMax(pgReqPhase,pgName)

        pgPinConfiguration = pwmComponent.createMenuSymbol("{}_PINS_MENU".format(pgName),pgMenu)
        pgPinConfiguration.setLabel("Pin Configuration")
        pgPinConfiguration.setVisible(False)
        pgPinConfiguration.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgPPSEN = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","PPSEN",pgPinConfiguration,gen,False)  
        pgPPSEN.setLabel("Enable PPS Pins (PPSEN)")
        pgPPSEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGIOxIOCON")

        pgPENL = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","PENL",pgPinConfiguration,gen,False)  
        pgPENL.setLabel("Enable Low Pin (PENL)")
        pgPENL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgPENH = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","PENH",pgPinConfiguration,gen,False)  
        pgPENH.setLabel("Enable High Pin (PENH)")
        pgPENH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgPinSwap = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","SWAP",pgPinConfiguration,gen,False)  
        pgPinSwap.setLabel("Swap PWM Pins (SWAP)")
        pgPinSwap.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgPinsComment = pwmComponent.createCommentSymbol("{}_PINS_COMMENT".format(pgName),pgPinConfiguration)
        pgPinsComment.setLabel("Warning!!!! Enable the bit here and configure the pins in the Pin Configuration Module.")
        pgPinsComment.setDependencies(pinsCallback,["{}_{}".format(pgName,CONST_PPSEN),"{}_{}".format(pgName,CONST_PENL),"{}_{}".format(pgName,CONST_PENH)])

        pgDeadTimeMenu = pwmComponent.createMenuSymbol(PG_DEAD_TIME_MENU.format(pgName),pgMenu)
        pgDeadTimeMenu.setLabel("Dead Time Configuration")
        pgDeadTimeMenu.setVisible(False)
        pgDeadTimeMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgDeadTimeLow = pwmComponent.createFloatSymbol(PG_DEAD_TIME_LOW.format(pgName),pgDeadTimeMenu)
        pgDeadTimeLow.setLabel("Dead Time Low(us)")
        pgDeadTimeLow.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxDT")

        pgCalcDeadTimeLow = pwmComponent.createFloatSymbol(PG_CALC_DEAD_TIME_LOW.format(pgName),pgDeadTimeMenu)
        pgCalcDeadTimeLow.setLabel("Calculated Dead Time Low(us)")
        pgCalcDeadTimeLow.setReadOnly(True)
        pgCalcDeadTimeLow.setDependencies(deadTimeCallback,[PG_DEAD_TIME_LOW.format(pgName),pgName+"_"+CONST_PMOD,PG_CALC_PWM_FREQ.format(pgName),"{}_{}".format(pgName,CONST_PMOD)])

        pgDeadTimeLowReg = pwmComponent.createHexSymbol(PG_DEAD_TIME_LOW_REG_VAL.format(pgName),pgDeadTimeMenu)
        pgDeadTimeLowReg.setLabel("Dead Time Low Reg value")
        pgDeadTimeLowReg.setReadOnly(True)
        pgDeadTimeLowReg.setVisible(False)

        pgDeadTimeHigh = pwmComponent.createFloatSymbol(PG_DEAD_TIME_HIGH.format(pgName),pgDeadTimeMenu)
        pgDeadTimeHigh.setLabel("Dead Time High(us)")
        pgDeadTimeHigh.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxDT")

        pgCalcDeadTimeHigh = pwmComponent.createFloatSymbol(PG_CALC_DEAD_TIME_HIGH.format(pgName),pgDeadTimeMenu)
        pgCalcDeadTimeHigh.setLabel("Calculated Dead Time High(us)")
        pgCalcDeadTimeHigh.setReadOnly(True)
        pgCalcDeadTimeHigh.setDependencies(deadTimeCallback,[PG_DEAD_TIME_HIGH.format(pgName),pgName+"_"+CONST_PMOD,PG_CALC_PWM_FREQ.format(pgName),"{}_{}".format(pgName,CONST_PMOD)])

        pgDeadTimeHighReg = pwmComponent.createHexSymbol(PG_DEAD_TIME_HIGH_REG_VAL.format(pgName),pgDeadTimeMenu)
        pgDeadTimeHighReg.setLabel("Dead Time High Reg value")
        pgDeadTimeHighReg.setReadOnly(True)
        pgDeadTimeHighReg.setVisible(False)
        setDTSymValues(pgDeadTimeHigh)

        pgDeadTimeReg = pwmComponent.createHexSymbol(PG_DEAD_TIME_REG.format(pgName),pgDeadTimeMenu)
        pgDeadTimeReg.setVisible(False)
        pgDeadTimeReg.setDependencies(combineDeadTimeRegisters,[PG_DEAD_TIME_HIGH_REG_VAL.format(pgName),PG_DEAD_TIME_LOW_REG_VAL.format(pgName)])

        dataUpdMenu = pwmComponent.createMenuSymbol(PG_DATA_UPDATE_SETTINGS.format(pgName), pgMenu)
        dataUpdMenu.setLabel("Data Update Settings".format(gen))
        dataUpdMenu.setVisible(False)
        dataUpdMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgUPDMODE = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","UPDMOD",dataUpdMenu,gen,False)
        pgUPDMODE.setLabel("Data Register Update Modes(UPDMOD)")
        pgUPDMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgMSTEN = createKeyValueSetSymbol(pwmComponent,MODULE_NAME,"PG","CON","MSTEN",dataUpdMenu,gen,False)
        pgMSTEN.setLabel("Master Update Enable(MSTEN)")
        pgMSTEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgUPDTRG = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","UPDTRG",dataUpdMenu,gen,False)
        pgUPDTRG.setLabel("Update Trigger Selection(UPDTRG)")
        pgUPDTRG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxEVT")

        overrideMenu = pwmComponent.createMenuSymbol(PG_OVERRIDE_CONFIGURATIONS.format(pgName), pgMenu)
        overrideMenu.setLabel("Override Configuration".format(gen))
        overrideMenu.setVisible(False)
        overrideMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgOVRENL = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","OVRENL",overrideMenu,gen,False)
        pgOVRENL.setLabel("Override Low")
        pgOVRENL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgOVRENH = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","OVRENH",overrideMenu,gen,False)
        pgOVRENH.setLabel("Override High")
        pgOVRENH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgOVRDAT = pwmComponent.createIntegerSymbol(PG_OVRDAT.format(pgName),overrideMenu)
        pgOVRDAT.setReadOnly(True)
        pgOVRDAT.setLabel("OVRDAT")
        pgOVRDAT.setDependencies(updateOVRDAT,["{}_{}".format(pgName,CONST_OVRENL),"{}_{}".format(pgName,CONST_OVRENH)])
        pgOVRDAT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgOSYNC = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","OSYNC",overrideMenu,gen,False)
        pgOSYNC.setLabel("Overide Synchronization Control (OSYNC)")
        pgOSYNC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        faultMenu = pwmComponent.createMenuSymbol(PG_FAULT_CONFIGURATIONS.format(pgName), pgMenu)
        faultMenu.setLabel("Polarity and Fault Configuration".format(gen))
        faultMenu.setVisible(False)
        faultMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgPOLL = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","POLL",faultMenu,gen,False)
        pgPOLL.setLabel("PWM-L Output Polarity")
        pgPOLL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgPOLH = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","IOCON","POLH",faultMenu,gen,False)
        pgPOLH.setLabel("PWM-H Output Polarity")
        pgPOLH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgFLTDAT = pwmComponent.createIntegerSymbol(PG_FLTDAT.format(pgName),faultMenu)
        pgFLTDAT.setReadOnly(True)
        pgFLTDAT.setLabel("FLTDAT")
        pgFLTDAT.setDependencies(updateFLTDAT,["{}_{}".format(pgName,CONST_POLL),"{}_{}".format(pgName,CONST_POLH)])
        pgFLTDAT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxIOCON")

        pgPSS = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","FPCI","PSS",faultMenu,gen,False)
        pgPSS.setLabel("Fault Input Source")
        pgPSS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxFPCI")

        pgPSSHex = pwmComponent.createHexSymbol("{}_{}_HEX".format(pgName,CONST_PSS),faultMenu)
        pgPSSHex.setVisible(False)
        pgPSSHex.setDependencies(updatePSS,["{}_{}".format(pgName,CONST_PSS)])

        pgPPS = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","FPCI","PPS",faultMenu,gen,False)
        pgPPS.setLabel("Fault Input Polarity")
        pgPPS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxFPCI")

        triggerMenu = pwmComponent.createMenuSymbol(PG_TRIGGER_CONFIGURATIONS.format(pgName), pgMenu) 
        triggerMenu.setLabel("Trigger Configuration".format(gen))
        triggerMenu.setVisible(False)
        triggerMenu.setDependencies(setVisible,[PG_ENABLE.format(pgName)])

        pgSOCS = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","CON","SOCS",triggerMenu,gen,False)
        pgSOCS.setLabel("Start of cycle Trigger(SOCS)")
        pgSOCS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgTRGMOD = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","CON","TRGMOD",triggerMenu,gen,False)
        pgTRGMOD.setLabel("Trigger Mode Selection(TRGMOD)")
        pgTRGMOD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxCON")

        pgPGTRIGSEL = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","PGTRGSEL",triggerMenu,gen,False)
        pgPGTRIGSEL.setLabel("Trigger Output Selection(PGTRIGSEL)")
        pgPGTRIGSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxEVT")

        pgTrigACmp = pwmComponent.createHexSymbol(PG_TRIG_A_COMP.format(pgName),triggerMenu)
        pgTrigACmp.setLabel("Trigger A Compare")
        pgTrigACmp.setMin(MIN_TRG_VAL)
        pgTrigACmp.setMax(MAX_TRG_VAL)
        pgTrigACmp.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGA")

        pgTrigBCmp = pwmComponent.createHexSymbol(PG_TRIG_B_COMP.format(pgName),triggerMenu)
        pgTrigBCmp.setLabel("Trigger B Compare")
        pgTrigBCmp.setMin(MIN_TRG_VAL)
        pgTrigBCmp.setMax(MAX_TRG_VAL)
        pgTrigBCmp.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGB")

        pgTrigCCmp = pwmComponent.createHexSymbol(PG_TRIG_C_COMP.format(pgName),triggerMenu)
        pgTrigCCmp.setLabel("Trigger C Compare")
        pgTrigCCmp.setMin(MIN_TRG_VAL)
        pgTrigCCmp.setMax(MAX_TRG_VAL)
        pgTrigCCmp.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxTRIGC")

        pgADTRPS = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","ADTR1PS",triggerMenu,gen,False) 
        pgADTRPS.setLabel("ADC Trigger 1 Postscaler Selection(ADTR1PS)")
        pgADTRPS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxEVT")

        pgADTRPSInHex = pwmComponent.createHexSymbol("{}_ADTR1PS".format(pgName),triggerMenu)
        pgADTRPSInHex.setDependencies(updateADTRPSHexSym,["{}_{}".format(pgName,CONST_ADTRPS)])
        pgADTRPSInHex.setVisible(False)

        pgADTROFS = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","ADTR1OFS",triggerMenu,gen,False)
        pgADTROFS.setLabel("ADC Trigger 1 Offset Selection(ADTR1OFS)")
        pgADTROFS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxEVT")

        pgADTROFSInHex = pwmComponent.createHexSymbol("{}_ADTR1OFS".format(pgName),triggerMenu)
        pgADTROFSInHex.setDependencies(updateADTROFSHexSym,["{}_{}".format(pgName,CONST_ADTROFS)])
        pgADTROFSInHex.setVisible(False)

        for adcTrgNum in getADCTrgList():
            for trigger in getTriggerCompareList():
                pgAdcTrg = pwmComponent.createBooleanSymbol("{}_ADC{}_TRIG{}".format(pgName, adcTrgNum, trigger), triggerMenu)
                pgAdcTrg.setLabel("Use TRIG{} as ADC {} Trigger Source".format(trigger, adcTrgNum))

                cmpEventNum = ord(trigger)-ord("A")+1

                pgADTREN = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","ADTR{}EN{}".format(adcTrgNum,cmpEventNum),triggerMenu,gen,False) 
                pgADTREN.setVisible(False)
                pgADTREN.setDefaultValue(1)
                pgADTREN.setDependencies(updateBoolToKeyValueCb,["{}_ADC{}_TRIG{}".format(pgName, adcTrgNum,trigger)])
                pgADTREN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pwm_04302;register:PGxEVT")

        pgHREN = pwmComponent.createBooleanSymbol("{}_HighResolutionEnable".format(pgName),pgOperationMenu)
        pgHREN.setVisible(getBitField("PWM", "PG", "CON", "HREN")!=None)
        pgHREN.setDefaultValue(False)

        pgPCI = createKeyValueSetSymbol(pwmComponent, MODULE_NAME, "PG","EVT","PWMPCI",triggerMenu,gen,False)
        pgPCI.setVisible(False)

        getIFSandIECRegMap()
        pgIntFlagBit = pwmComponent.createStringSymbol("pg{}intFlagBit".format(gen),None)
        pgIntFlagBit.setDefaultValue(ifsMap["PWM{}IF".format(gen)])
        pgIntFlagBit.setVisible(False)

        pgIntEnableBit = pwmComponent.createStringSymbol("pg{}intEnableBit".format(gen),None)
        pgIntEnableBit.setDefaultValue(iecMap["PWM{}IE".format(gen)])
        pgIntEnableBit.setVisible(False)

        createBitSymbol(pgName,"pg{}intFaultEnableBit".format(gen), "EVT", "FLTIEN",pwmComponent)
        createBitSymbol(pgName,"pg{}intCurrentLimitEnableBit".format(gen), "EVT", "CLIEN",pwmComponent)
        createBitSymbol(pgName,"pg{}intFeedForwardEnableBit".format(gen), "EVT", "FFIEN",pwmComponent)
        createBitSymbol(pgName,"pg{}intSyncEnableBit".format(gen), "EVT", "SIEN",pwmComponent)
        createBitSymbol(pgName,"pg{}intFaultStatusBit".format(gen), "STAT", "FLTEVT",pwmComponent)
        createBitSymbol(pgName,"pg{}intCurrentLimitStatusBit".format(gen), "STAT", "CLEVT",pwmComponent)
        createBitSymbol(pgName,"pg{}intFeedForwardStatusBit".format(gen), "STAT", "FFEVT",pwmComponent)
        createBitSymbol(pgName,"pg{}intSyncStatusBit".format(gen), "STAT", "SEVT",pwmComponent)

        createBitSymbol(pgName,"pg{}softwareUpdateRequestBit".format(gen), "STAT", "UPDREQ",pwmComponent)
        createBitSymbol(pgName,"pg{}softwareUpdateReqStatusBit".format(gen), "STAT", "UPDREQ",pwmComponent)

        createBitSymbol(pgName,"pg{}trig1EnableBitForCmpA".format(gen), "EVT", "ADTR1EN1",pwmComponent)
        createBitSymbol(pgName,"pg{}trig1EnableBitForCmpB".format(gen), "EVT", "ADTR1EN2",pwmComponent)
        createBitSymbol(pgName,"pg{}trig1EnableBitForCmpC".format(gen), "EVT", "ADTR1EN3",pwmComponent)
        createBitSymbol(pgName,"pg{}trig2EnableBitForCmpA".format(gen), "EVT", "ADTR2EN1",pwmComponent)
        createBitSymbol(pgName,"pg{}trig2EnableBitForCmpB".format(gen), "EVT", "ADTR2EN2",pwmComponent)
        createBitSymbol(pgName,"pg{}trig2EnableBitForCmpC".format(gen), "EVT", "ADTR2EN3",pwmComponent)

        createBitSymbol(pgName,"pg{}dacTriggerEnableForCmpD".format(gen), "EVT1", "DACTREN1",pwmComponent)
        createBitSymbol(pgName,"pg{}dacTriggerEnableForCmpE".format(gen), "EVT1", "DACTREN2",pwmComponent)
        createBitSymbol(pgName,"pg{}faultModeLatchClearBit".format(gen), "FPCI", "SWTERM",pwmComponent)
############################################################################
#### Code Generation ####
############################################################################
    generatorsInUse = pwmComponent.createBooleanSymbol("generatorsInUse", None)
    generatorsInUse.setVisible(False)
    genList = [PG_ENABLE.format("PG" + str(i)) for i in range(1, NUMBER_OF_GENERATORS+1)]
    generatorsInUse.setDependencies(anyGenInUse,genList)

    moduleNameUpperCase = pwmComponent.createStringSymbol("moduleNameUpperCase", None)
    moduleNameUpperCase.setVisible(False)
    moduleNameUpperCase.setDefaultValue(pwmComponent.getID().upper())   

    moduleNameLowerCase = pwmComponent.createStringSymbol("moduleNameLowerCase", None)
    moduleNameLowerCase.setVisible(False)
    moduleNameLowerCase.setDefaultValue(pwmComponent.getID().lower())  

    fileNameLowerCase = pwmComponent.createStringSymbol("fileNameLowerCase", None)
    fileNameLowerCase.setVisible(False)
    fileNameLowerCase.setDefaultValue(pwmComponent.getID().lower())  

    maxGeneratorCount = pwmComponent.createIntegerSymbol("MAX_GENERATOR_COUNT", None)
    maxGeneratorCount.setVisible(False)
    maxGeneratorCount.setDefaultValue(NUMBER_OF_GENERATORS)

    trigCmpCount = pwmComponent.createIntegerSymbol("MAX_TRIGGER_COMPARE_OPTIONS", None)
    trigCmpCount.setVisible(False)
    trigCmpCount.setDefaultValue(len(getTriggerCompareList()))

    dacTrgAvailable = pwmComponent.createBooleanSymbol("dacTriggerCompareRegisterAvailable", None)
    dacTrgAvailable.setVisible(False)
    dacTrgAvailable.setDefaultValue(False)

    masterDutyCycleReg = pwmComponent.createStringSymbol("masterDutyCycleReg", None)
    masterDutyCycleReg.setVisible(False)
    masterDutyCycleReg.setDefaultValue("MDC")

    masterPeriodReg = pwmComponent.createStringSymbol("masterPeriodReg", None)
    masterPeriodReg.setVisible(False)
    masterPeriodReg.setDefaultValue("MPER")

    masterPhaseReg = pwmComponent.createStringSymbol("masterPhaseReg", None)
    masterPhaseReg.setVisible(False)
    masterPhaseReg.setDefaultValue("MPHASE")


    trgCmpList = getTriggerCompareList()
    for trgCmp in range(ord('A'), ord('G')):
        trgCmpAvailable = pwmComponent.createBooleanSymbol("trig{}CompareOptionAvailable".format(chr(trgCmp)),None)
        trgCmpAvailable.setVisible(False)
        trgCmpAvailable.setDefaultValue(chr(trgCmp) in trgCmpList)

    masterHREN = pwmComponent.createBooleanSymbol("masterHighResolutionModeEnabled",None)
    masterHREN.setVisible(getBitField("PWM", "PG", "CON", "HREN")!=None)
    masterHREN.setDefaultValue(False)    

    CoreSysIntFile = pwmComponent.createBooleanSymbol("CoreSysIntFile",None)
    CoreSysIntFile.setVisible(False)
    CoreSysIntFile.setDefaultValue(False)    

    clkGenNum = pwmComponent.createIntegerSymbol("clkSrcGenNumber",None)
    clkGenNum.setVisible(False)
    clkGenNum.setDefaultValue(5)    

    # String symbol for the POR (Power-On Reset) values of registers
    regPorSet = pwmComponent.createStringSymbol("regPorSet", None)
    regPorSet.setDefaultValue(createRegPorSetString())
    regPorSet.setVisible(False)
#########################################################################################################################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pwmHeaderFile = pwmComponent.createFileSymbol("PWM_HEADER", None)
    pwmHeaderFile.setMarkup(True)
    pwmHeaderFile.setSourcePath("../peripheral/pwm_04302/templates/pwm.h.ftl")
    pwmHeaderFile.setOutputName("plib_pwm.h")
    pwmHeaderFile.setDestPath("peripheral/pwm/")
    pwmHeaderFile.setProjectPath("config/" + configName + "/peripheral/pwm/")
    pwmHeaderFile.setType("HEADER")
    pwmHeaderFile.setOverwrite(True)

    pwmSourceFile = pwmComponent.createFileSymbol("PWM_SOURCE1", None)
    pwmSourceFile.setMarkup(True)
    pwmSourceFile.setSourcePath("../peripheral/pwm_04302/templates/pwm.c.ftl")
    pwmSourceFile.setOutputName("plib_pwm.c")
    pwmSourceFile.setDestPath("peripheral/pwm/")
    pwmSourceFile.setProjectPath("config/" + configName + "/peripheral/pwm/")
    pwmSourceFile.setType("SOURCE")
    pwmSourceFile.setOverwrite(True)

    pwmSystemInitFile = pwmComponent.createFileSymbol("PWM_INIT", None)
    pwmSystemInitFile.setType("STRING")
    pwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pwmSystemInitFile.setSourcePath("../peripheral/pwm_04302/templates/system/initialization.c.ftl")
    pwmSystemInitFile.setMarkup(True)

    pwmSystemDefFile = pwmComponent.createFileSymbol("PWM_DEF", None)
    pwmSystemDefFile.setType("STRING")
    pwmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pwmSystemDefFile.setSourcePath("../peripheral/pwm_04302/templates/system/definitions.h.ftl")
    pwmSystemDefFile.setMarkup(True)
