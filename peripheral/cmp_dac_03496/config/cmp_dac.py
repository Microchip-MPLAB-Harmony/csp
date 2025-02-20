CMP_MENU = "CMP_MENU"
DAC_MENU = "DAC_MENU"
DAC_MODE = "DAC_MODE"
DACDATAH = "DAC_DAT__DACDATAH"
DACDATAL = "DAC_DAT__DACDATAL"
DAC_CON__TMCB = "DAC_CON__TMCB"
SLPDAT = "SLPDAT"
CORE = "core"
CLK_SRC = "CLK_SRC"
CLK_FREQ = "cmpDacInputClock"
CLK_GEN7_FREQ = "clkGen7OutFrequency"
REQ_SSTIME = "REQ_SSTIME"
REQ_TMODTIME = "REQ_TMODTIME"
DACCTRL_CTRL2__SSTIME = "DACCTRL_CTRL2__SSTIME"
DACCTRL_CTRL2__TMODTIME = "DACCTRL_CTRL2__TMODTIME"
CMP_DAC_INST_NUM = "instance"
CMP_DAC_INST_NAME = "CMP_DAC_INST_NAME"

DAC_SLPCON__HCFSEL = "DAC_SLPCON__HCFSEL"
DAC_SLPCON__PSE = "DAC_SLPCON__PSE"
DAC_SLPCON__SLPSTRT = "DAC_SLPCON__SLPSTRT"
DAC_SLPCON__SLPSTOPA = "DAC_SLPCON__SLPSTOPA"
DAC_SLPCON__SLPSTOPB = "DAC_SLPCON__SLPSTOPB"
DACCTRL_CTRL1__FCLKDIV = "DACCTRL_CTRL1__FCLKDIV"
DAC_CON__IRQM = "DAC_CON__IRQM"
DAC_SLPCON__HME = "DAC_SLPCON__HME"
DAC_SLPCON__TWME = "DAC_SLPCON__TWME"
DAC_SLPCON__SLOPEN = "DAC_SLPCON__SLOPEN"

MODULE_NAME = "CMP_DAC"
DACCTRL_REG_GRP = "DACCTRL"
DAC_REG_GRP = "DAC"
CON_REG_NAME = "CON"
CMP_INT_REGEX = "CMP{}Interrupt"
CLK_COMMENT = "CLK_COMMENT"
ENABLE_INT_COMMENT = "ENABLE_INT_COMMENT"

# Create a ticket for property creation of the same
DACDATA_MIN_VALUE = 205
DACDATA_MAX_VALUE = 3890


def getValueGroup(moduleName, valueGroupName):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/value-group@[name="'
        + valueGroupName
        + '"]'
    )
    return ATDF.getNode(atdfPath)


def getBitfieldData(node):
    result = []
    for bitfield in node.getChildren():
        caption = bitfield.getAttribute("caption")
        if caption.lower() != "reserved":
            value = bitfield.getAttribute("value")
            bitfieldInt = int(value, 16) if value.startswith("0x") else int(value)
            result.append(
                {
                    "key": bitfield.getAttribute("name") or caption,
                    "value": str(bitfieldInt),
                    "desc": caption,
                }
            )
    return result


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value


def getSettingBitDefaultValue(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        regDefaultVal = registerNode.getAttribute("initval")
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return getDefaultVal(regDefaultVal, bitMask)
    return 0


def findKeyValue(value, dict):
    for index, pair in enumerate(dict):
        if pair["value"] == str(value):
            return index
    print("Could not find value in dictionary")
    return ""


def getBitField(moduleName, registerGroup, register, bitfield):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]/bitfield@[name="'
        + bitfield
        + '"]'
    )
    return ATDF.getNode(atdfPath)


def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if bitNode != None:
        return bitNode.getAttribute("values")
    return ""


def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
    for bitfield in valueNodes:  ##  do this for all <value > entries for this bitfield
        dict = {}
        if (
            bitfield.getAttribute("caption").lower() != "reserved"
        ):  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if value[:2] == "0x":
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            optionList.append(dict)
    return optionList


def getKeyValuePairBasedonValue(value, keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return (
                index  # return occurrence of <bitfield > entry which has matching value
            )
        index += 1

    print("find_key: could not find value in dictionary")  # should never get here
    return ""


def addKeystoKeyValueSymbol(bitSymbol, bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey(ii["key"], ii["value"], ii["desc"])


def createKeyValueSetSymbol(
    component, moduleName, registerGroup, register, bitfield, menuName
):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        symbolKey = valueGroupEntry
        optionList = getBitfieldOptionList(valGroup)
        valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, menuName)
        valueGroupEntryComp.setLabel(symbolKey)
        defaultValue = getSettingBitDefaultValue(
            moduleName, registerGroup, register, bitfield
        )
        valueGroupEntryComp.setDefaultValue(
            getKeyValuePairBasedonValue(defaultValue, optionList)
        )
        valueGroupEntryComp.setOutputMode("Value")
        valueGroupEntryComp.setDisplayMode("Description")
        addKeystoKeyValueSymbol(valueGroupEntryComp, optionList)
        return valueGroupEntryComp


def getBitfieldMask(moduleName, registerGroup, register, bitfield):

    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)

    if registerNode != None:
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return int(bitMask, 16)
    return 0


def dacModeDependencies(symbol, event):

    component = symbol.getComponent()

    modeVisibilityMap = {
        "Hysteretic-Mode": [DACDATAL, DAC_CON__TMCB, DAC_SLPCON__HCFSEL],
        "Triangle-Wave-Mode": [DACDATAL, SLPDAT],
        "Slope-Mode": [
            DACDATAL,
            SLPDAT,
            REQ_SSTIME,
            DACCTRL_CTRL2__SSTIME,
            REQ_TMODTIME,
            DACCTRL_CTRL2__TMODTIME,
            DAC_SLPCON__PSE,
            DAC_SLPCON__SLPSTRT,
            DAC_SLPCON__SLPSTOPA,
            DAC_SLPCON__SLPSTOPB,
        ],
    }

    visibleIds = modeVisibilityMap.get(component.getSymbolValue(DAC_MODE), [])
    symbol.setVisible(symbol.getID() in visibleIds)

    # Set max value for specific symbols
    if symbol.getID() in [REQ_SSTIME, REQ_TMODTIME]:
        clkFreq = component.getSymbolByID(CLK_FREQ).getValue()
        tmodTimeBitMask = getBitfieldMask(
            MODULE_NAME, DACCTRL_REG_GRP, "CTRL2", "TMODTIME"
        )
        maxStateValue = (
            ((tmodTimeBitMask * 2) / float(clkFreq)) * 1e9 if clkFreq != 0 else 0
        )
        symbol.setMax(int(maxStateValue))

    if symbol.getID() in [DACCTRL_CTRL2__SSTIME]:
        clkFreq = component.getSymbolByID(CLK_FREQ).getValue()
        reqSteadyState = component.getSymbolByID(REQ_SSTIME).getValue()
        calcSteadyStateVal = int((reqSteadyState * clkFreq) / (2 * 1e9))

        symbol.setValue(calcSteadyStateVal)

    if symbol.getID() in [DACCTRL_CTRL2__TMODTIME]:
        clkFreq = component.getSymbolByID(CLK_FREQ).getValue()
        reqTransState = component.getSymbolByID(REQ_TMODTIME).getValue()
        calcTransStateVal = int((reqTransState * clkFreq) / (2 * 1e9))

        symbol.setValue(calcTransStateVal)


def extractDividerValue(clkDivStr):

    parts = clkDivStr.split(":")
    clkDivNum = int(parts[1])
    return clkDivNum


def clkFreqDependency(symbol, event):

    component = symbol.getComponent()
    clkDiv = component.getSymbolByID(DACCTRL_CTRL1__FCLKDIV).getSelectedKey()

    symbol.setValue(
        int(Database.getSymbolValue(CORE, CLK_GEN7_FREQ) / extractDividerValue(clkDiv))
    )


def updateClockComment(symbol, event):

    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    vectorIndex = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vectorIndex = str(param.getAttribute("index"))
            break

    return vectorIndex


def interruptControlHelper(symbol, event):

    component = symbol.getComponent()
    instNum = component.getSymbolValue(CMP_DAC_INST_NUM)
    intMode = component.getSymbolByID(DAC_CON__IRQM).getSelectedKey()

    handleInterruptControl(instNum, intMode)


def handleInterruptControl(instNum, intMode):

    intIndex = getVectorIndex(CMP_INT_REGEX.format(instNum))

    if intMode != "Interrupts are disabled":
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), True)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), True)
    else:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), False)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), False)


def interruptStatusWarning(symbol, event):

    symbolValue = symbol.getComponent().getSymbolByID(DAC_CON__IRQM).getSelectedKey()

    if symbolValue != "Interrupts are disabled":
        symbol.setVisible(not event["value"])
    else:
        symbol.setVisible(False)


def isInterruptEnabled(symbol, event):

    symbolValue = symbol.getComponent().getSymbolByID(DAC_CON__IRQM).getSelectedKey()

    if symbolValue != "Interrupts are disabled":
        symbol.setValue(True)
    else:
        symbol.setValue(False)


def getRegisterDefaultValue(module, registerGroup, register):
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, registerGroup, register
    )
    registerNode = ATDF.getNode(reg_path)

    if registerNode is not None:
        regInitVal = registerNode.getAttribute("initval")
        return "{}UL".format(regInitVal) if regInitVal else "0x0UL"
    return "0x0UL"


def setDacModeDependency(symbol, event):

    symbolID = symbol.getID()
    component = symbol.getComponent()

    component.setSymbolValue(DAC_SLPCON__HME, False)
    component.setSymbolValue(DAC_SLPCON__TWME, False)
    component.setSymbolValue(DAC_SLPCON__SLOPEN, False)

    modeSettings = {
        "Hysteretic-Mode": {DAC_SLPCON__HME: True, DAC_SLPCON__SLOPEN: True},
        "Triangle-Wave-Mode": {DAC_SLPCON__TWME: True, DAC_SLPCON__SLOPEN: True},
        "Slope-Mode": {DAC_SLPCON__SLOPEN: True},
    }

    if event["value"] in modeSettings:
        for key, value in modeSettings[event["value"]].items():
            component.setSymbolValue(key, value)


def handleMessage(messageID, args):
    retDict = {}
    if messageID == "CMPDAC_CONFIG_HW_IO":
        component = cmpInstanceName.getValue().lower()
        setting, enable = args["config"]

        if setting[-1].isalpha():
            if enable == False:
                res = cmpPosInpConfig.setValue(0)
            else:
                res = cmpPosInpConfig.setSelectedKey(setting.upper())

            if res == True:
                retDict = {"Result": "Success"}
            else:
                retDict = {"Result": "Fail"}

    else:
        retDict = {"Result": "CMP_DAC UnImplemented Command"}

    return retDict


def instantiateComponent(cmpdacComponent):
    global cmpInstanceName
    cmpInstanceName = cmpdacComponent.createStringSymbol(CMP_DAC_INST_NAME, None)
    cmpInstanceName.setVisible(False)
    cmpInstanceName.setDefaultValue(cmpdacComponent.getID().upper())
    Log.writeInfoMessage("Running " + cmpInstanceName.getValue())

    cmpDacInstNum = cmpdacComponent.createStringSymbol(CMP_DAC_INST_NUM, None)
    cmpDacInstNum.setDefaultValue(
        cmpdacComponent.getID().upper().replace("CMP_DAC", "")
    )
    cmpDacInstNum.setVisible(False)

    cmpDacInstNum = cmpDacInstNum.getValue()

    cmpMenu = cmpdacComponent.createMenuSymbol(CMP_MENU, None)
    cmpMenu.setLabel("Comparator")

    global cmpPosInpConfig
    cmpPosInpConfig = cmpdacComponent.createKeyValueSetSymbol("DAC_CON__INSEL", cmpMenu)
    cmpPosInpConfig.setLabel("Comparator Positive Input Configuration")
    cmpPosInpConfig.addKey(
        "CMP{}A".format(cmpDacInstNum), "0", "CMP{}A".format(cmpDacInstNum)
    )
    cmpPosInpConfig.addKey(
        "CMP{}B".format(cmpDacInstNum), "1", "CMP{}B".format(cmpDacInstNum)
    )
    cmpPosInpConfig.addKey(
        "CMP{}C".format(cmpDacInstNum), "2", "CMP{}C".format(cmpDacInstNum)
    )
    cmpPosInpConfig.addKey(
        "CMP{}D".format(cmpDacInstNum), "3", "CMP{}D".format(cmpDacInstNum)
    )
    cmpPosInpConfig.setOutputMode("Value")
    cmpPosInpConfig.setDisplayMode("Description")
    cmpPosInpConfig.setDefaultValue(0)
    cmpPosInpConfig.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    intEventPol = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, CON_REG_NAME, "IRQM", cmpMenu
    )
    intEventPol.setLabel("Interrupt Event Polarity")
    intEventPol.setDependencies(interruptControlHelper, [DAC_CON__IRQM])
    intEventPol.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpOutInv = cmpdacComponent.createBooleanSymbol(
        "{}_{}__CMPPOL".format(DAC_REG_GRP, CON_REG_NAME), cmpMenu
    )
    cmpOutInv.setLabel("Comparator Output Inversion")
    cmpOutInv.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpHysSelect = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, CON_REG_NAME, "HYSSEL", cmpMenu
    )
    cmpHysSelect.setLabel("Comparator Hysteresis")
    cmpHysSelect.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpHysPol = cmpdacComponent.createBooleanSymbol(
        "{}_{}__HYSPOL".format(DAC_REG_GRP, CON_REG_NAME), cmpMenu
    )
    cmpHysPol.setLabel("Comparator Hysteresis Polarity Enable")
    cmpHysPol.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpBlankEn = cmpdacComponent.createBooleanSymbol(
        "{}_{}__CBE".format(DAC_REG_GRP, CON_REG_NAME), cmpMenu
    )
    cmpBlankEn.setLabel("Comparator Blank Enable")
    cmpBlankEn.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpFilterEn = cmpdacComponent.createBooleanSymbol(
        "{}_{}__FLTREN".format(DAC_REG_GRP, CON_REG_NAME), cmpMenu
    )
    cmpFilterEn.setLabel("Comparator Digital Filter Enable")
    cmpFilterEn.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    dacMenu = cmpdacComponent.createMenuSymbol(DAC_MENU, None)
    dacMenu.setLabel(DAC_REG_GRP)

    dacMode = cmpdacComponent.createComboSymbol(
        DAC_MODE,
        dacMenu,
        ["DC-Mode", "Hysteretic-Mode", "Triangle-Wave-Mode", "Slope-Mode"],
    )
    dacMode.setLabel("DAC Mode")
    dacMode.setDefaultValue("DC-Mode")

    clkSrc = cmpdacComponent.createStringSymbol(CLK_SRC, dacMenu)
    clkSrc.setLabel("Clock Source")
    clkSrc.setDefaultValue("Clock Generator 7")
    clkSrc.setReadOnly(True)

    clkDiv = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DACCTRL_REG_GRP, "CTRL1", "FCLKDIV", dacMenu
    )
    clkDiv.setLabel("Clock Divider")
    clkDiv.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACCTRL1"
    )

    clkFreq = cmpdacComponent.createIntegerSymbol(CLK_FREQ, dacMenu)
    clkFreq.setLabel("Clock Calculated Frequency (Hz)")
    clkFreq.setReadOnly(True)
    clkFreq.setDefaultValue(Database.getSymbolValue(CORE, CLK_GEN7_FREQ))
    clkFreq.setDependencies(
        clkFreqDependency,
        [
            CORE + "." + CLK_GEN7_FREQ,
            DACCTRL_CTRL1__FCLKDIV,
        ],
    )

    dacOutEn = cmpdacComponent.createBooleanSymbol(
        "{}_{}__DACOEN".format(DAC_REG_GRP, CON_REG_NAME), dacMenu
    )
    dacOutEn.setLabel("DAC Output Enable")
    dacOutEn.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    dacdatahReg = cmpdacComponent.createHexSymbol(DACDATAH, dacMenu)
    dacdatahReg.setLabel(DACDATAH)
    dacdatahReg.setDefaultValue(DACDATA_MAX_VALUE)
    dacdatahReg.setMin(DACDATA_MIN_VALUE)
    dacdatahReg.setMax(DACDATA_MAX_VALUE)
    dacdatahReg.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxDAT"
    )

    dacdatalReg = cmpdacComponent.createHexSymbol(DACDATAL, dacMenu)
    dacdatalReg.setLabel(DACDATAL)
    dacdatalReg.setDefaultValue(DACDATA_MIN_VALUE)
    dacdatalReg.setMin(DACDATA_MIN_VALUE)
    dacdatalReg.setMax(DACDATA_MAX_VALUE)
    dacdatalReg.setVisible(False)
    dacdatalReg.setDependencies(dacModeDependencies, [DAC_MODE])
    dacdatalReg.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxDAT"
    )

    # Hysteresis Mode symbols
    blankPeriod = cmpdacComponent.createHexSymbol(DAC_CON__TMCB, dacMenu)
    blankPeriod.setLabel("Blank Period")
    blankPeriod.setDefaultValue(0)
    blankPeriod.setMin(0)
    blankPeriod.setMax(getBitfieldMask(MODULE_NAME, DAC_REG_GRP, CON_REG_NAME, "TMCB"))
    blankPeriod.setVisible(False)
    blankPeriod.setDependencies(dacModeDependencies, [DAC_MODE])
    blankPeriod.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxCON"
    )

    cmpFuncInput = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, "SLPCON", "HCFSEL", dacMenu
    )
    cmpFuncInput.setLabel("Comparator Function Input")
    cmpFuncInput.setVisible(False)
    cmpFuncInput.setDependencies(dacModeDependencies, [DAC_MODE])
    cmpFuncInput.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPCON"
    )

    slpdat = cmpdacComponent.createHexSymbol(SLPDAT, dacMenu)
    slpdat.setLabel("SLPDAT")
    slpdat.setDefaultValue(0)
    slpdat.setMin(0)
    slpdat.setMax(getBitfieldMask(MODULE_NAME, DAC_REG_GRP, SLPDAT, SLPDAT))
    slpdat.setVisible(False)
    slpdat.setDependencies(dacModeDependencies, [DAC_MODE])
    slpdat.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPDAT"
    )

    clkFreq = clkFreq.getValue()
    tmodTimeBitMask = getBitfieldMask(MODULE_NAME, DACCTRL_REG_GRP, "CTRL2", "TMODTIME")

    maxStateValue = (
        ((tmodTimeBitMask * 2) / float(clkFreq)) * 1e9 if clkFreq != 0 else 0
    )

    reqSteadyState = cmpdacComponent.createIntegerSymbol(REQ_SSTIME, dacMenu)
    reqSteadyState.setLabel("Requested Steady State Time(ns)")
    reqSteadyState.setDefaultValue(0)
    reqSteadyState.setMin(0)
    reqSteadyState.setMax(int(maxStateValue))
    reqSteadyState.setVisible(False)
    reqSteadyState.setDependencies(
        dacModeDependencies, [DAC_MODE, CLK_FREQ, DACCTRL_CTRL1__FCLKDIV]
    )

    calcSteadyState = cmpdacComponent.createHexSymbol(DACCTRL_CTRL2__SSTIME, dacMenu)
    calcSteadyState.setLabel("Calculated Steady State Time")
    calcSteadyState.setDefaultValue(0)
    calcSteadyState.setMin(0)
    calcSteadyState.setMax(tmodTimeBitMask)
    calcSteadyState.setVisible(False)
    calcSteadyState.setReadOnly(True)
    calcSteadyState.setDependencies(
        dacModeDependencies, [DAC_MODE, CLK_FREQ, REQ_SSTIME]
    )
    calcSteadyState.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACCTRL2"
    )

    reqSteadyStateCmt = cmpdacComponent.createCommentSymbol(
        "REQ_STEADY_STATE_COMMENT", reqSteadyState
    )
    reqSteadyStateCmt.setLabel(
        "***Ensure same Steady State Time is configured across all CMP-DAC instances***"
    )

    reqTransMode = cmpdacComponent.createIntegerSymbol(REQ_TMODTIME, dacMenu)
    reqTransMode.setLabel("Requested Transition Mode Time(ns)")
    reqTransMode.setDefaultValue(0)
    reqTransMode.setMin(0)
    reqTransMode.setMax(int(maxStateValue))
    reqTransMode.setVisible(False)
    reqTransMode.setDependencies(
        dacModeDependencies, [DAC_MODE, CLK_FREQ, DACCTRL_CTRL1__FCLKDIV]
    )

    calcTransState = cmpdacComponent.createHexSymbol(DACCTRL_CTRL2__TMODTIME, dacMenu)
    calcTransState.setLabel("Calculated Transition State")
    calcTransState.setDefaultValue(0)
    calcTransState.setMin(0)
    calcTransState.setMax(tmodTimeBitMask)
    calcTransState.setVisible(False)
    calcTransState.setReadOnly(True)
    calcTransState.setDependencies(
        dacModeDependencies, [DAC_MODE, CLK_FREQ, REQ_TMODTIME]
    )
    calcTransState.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACCTRL2"
    )

    reqTransModeCmt = cmpdacComponent.createCommentSymbol(
        "REQ_TRANS_TIME_COMMENT", reqTransMode
    )
    reqTransModeCmt.setLabel(
        "***Ensure same Transition Mode Time is configured across all CMP-DAC instances***"
    )

    slopeDir = cmpdacComponent.createBooleanSymbol(
        "{}_{}__PSE".format(DAC_REG_GRP, "SLPCON"), dacMenu
    )
    slopeDir.setLabel("Slope Direction Enable")
    slopeDir.setVisible(False)
    slopeDir.setDependencies(dacModeDependencies, [DAC_MODE])
    slopeDir.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPCON"
    )

    startSignal = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, "SLPCON", "SLPSTRT", dacMenu
    )
    startSignal.setLabel("Start Signal")
    startSignal.setVisible(False)
    startSignal.setDependencies(dacModeDependencies, [DAC_MODE])
    startSignal.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPCON"
    )

    stopSignalA = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, "SLPCON", "SLPSTOPA", dacMenu
    )
    stopSignalA.setLabel("Stop Signal A")
    stopSignalA.setVisible(False)
    stopSignalA.setDependencies(dacModeDependencies, [DAC_MODE])
    stopSignalA.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPCON"
    )

    stopSignalB = createKeyValueSetSymbol(
        cmpdacComponent, MODULE_NAME, DAC_REG_GRP, "SLPCON", "SLPSTOPB", dacMenu
    )
    stopSignalB.setLabel("Stop Signal B")
    stopSignalB.setVisible(False)
    stopSignalB.setDependencies(dacModeDependencies, [DAC_MODE])
    stopSignalB.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:cmp_dac_03496;register:DACxSLPCON"
    )

    clkComment = cmpdacComponent.createCommentSymbol(CLK_COMMENT, dacMenu)
    clkComment.setLabel(
        "Warning!!! Enable and configure Clock Generator 7 in Clock Section of System Module"
    )
    clkComment.setDependencies(updateClockComment, [CLK_FREQ])

    intIndex = getVectorIndex(CMP_INT_REGEX.format(cmpDacInstNum))

    intComment = cmpdacComponent.createCommentSymbol(ENABLE_INT_COMMENT, cmpMenu)
    intComment.setVisible(False)
    intComment.setLabel(
        "Warning!!! Enable Comparator {} Interrupt in Interrupts Section of System module".format(
            cmpDacInstNum
        )
    )
    intComment.setDependencies(
        interruptStatusWarning, [CORE + "." + "INTC_" + str(intIndex) + "_ENABLE"]
    )

    # Code Generation

    moduleName = cmpdacComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue("CMP{}".format(cmpDacInstNum))
    moduleName.setVisible(False)

    cmpIntEnable = cmpdacComponent.createBooleanSymbol("cmpIntEnable", None)
    cmpIntEnable.setVisible(False)
    cmpIntEnable.setDependencies(isInterruptEnabled, [DAC_CON__IRQM])

    porDacctrl1 = cmpdacComponent.createStringSymbol("porDacctrl1", None)
    porDacctrl1.setDefaultValue(
        getRegisterDefaultValue(MODULE_NAME, "DACCTRL", "CTRL1")
    )
    porDacctrl1.setVisible(False)

    porDacctrl2 = cmpdacComponent.createStringSymbol("porDacctrl2", None)
    porDacctrl2.setDefaultValue(
        getRegisterDefaultValue(MODULE_NAME, "DACCTRL", "CTRL2")
    )
    porDacctrl2.setVisible(False)

    cmpIsrHandlerName = cmpdacComponent.createStringSymbol("cmpIsrHandlerName", None)
    cmpIsrHandlerName.setDefaultValue(
        Database.getSymbolValue(CORE, "INTC_{}_INTERRUPT_HANDLER".format(intIndex))
    )
    cmpIsrHandlerName.setVisible(False)

    slopen = cmpdacComponent.createBooleanSymbol(DAC_SLPCON__SLOPEN, None)
    slopen.setVisible(False)
    slopen.setDependencies(setDacModeDependency, [DAC_MODE])

    hme = cmpdacComponent.createBooleanSymbol(DAC_SLPCON__HME, None)
    hme.setVisible(False)
    hme.setDependencies(setDacModeDependency, [DAC_MODE])

    twme = cmpdacComponent.createBooleanSymbol(DAC_SLPCON__TWME, None)
    twme.setVisible(False)
    twme.setDependencies(setDacModeDependency, [DAC_MODE])

    paramNode = ATDF.getNode(
        (
            '/avr-tools-device-file/devices/device/peripherals/module@[name="{}"]/instance@[name="{}"]/parameters/param@[name="{}"]'
        ).format(MODULE_NAME, "CMP_DAC1", "calibrationFlashAddress")
    )

    calibrationFlashAddress = cmpdacComponent.createStringSymbol(
        "calibrationFlashAddress", None
    )
    calibrationFlashAddress.setDefaultValue(paramNode.getAttribute("value"))
    calibrationFlashAddress.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    cmpCommonFile = cmpdacComponent.createFileSymbol("CMP_COMMON_HEADER", None)
    cmpCommonFile.setSourcePath(
        "../peripheral/cmp_dac_03496/templates/plib_cmp_common.h.ftl"
    )
    cmpCommonFile.setOutputName("plib_cmp_common.h")
    cmpCommonFile.setDestPath("peripheral/cmp_dac/")
    cmpCommonFile.setProjectPath("config/" + configName + "/peripheral/cmp_dac/")
    cmpCommonFile.setType("HEADER")
    cmpCommonFile.setMarkup(False)
    cmpCommonFile.setOverwrite(True)

    # Instance Header File
    cmpHeaderFile = cmpdacComponent.createFileSymbol("CMP_HEADER", None)
    cmpHeaderFile.setSourcePath("../peripheral/cmp_dac_03496/templates/plib_cmp.h.ftl")
    cmpHeaderFile.setOutputName("plib_cmp{}.h".format(cmpDacInstNum))
    cmpHeaderFile.setDestPath("/peripheral/cmp_dac/")
    cmpHeaderFile.setProjectPath("config/" + configName + "/peripheral/cmp_dac/")
    cmpHeaderFile.setType("HEADER")
    cmpHeaderFile.setMarkup(True)
    cmpHeaderFile.setOverwrite(True)

    # Instance Source File
    cmpSourceFile = cmpdacComponent.createFileSymbol("CMP_SOURCE", None)
    cmpSourceFile.setSourcePath("../peripheral/cmp_dac_03496/templates/plib_cmp.c.ftl")
    cmpSourceFile.setOutputName("plib_cmp{}.c".format(cmpDacInstNum))
    cmpSourceFile.setDestPath("/peripheral/cmp_dac/")
    cmpSourceFile.setProjectPath("config/" + configName + "/peripheral/cmp_dac/")
    cmpSourceFile.setType("SOURCE")
    cmpSourceFile.setMarkup(True)
    cmpSourceFile.setOverwrite(True)

    cmpSystemInitFile = cmpdacComponent.createFileSymbol("CMP_SYS_INT", None)
    cmpSystemInitFile.setType("STRING")
    cmpSystemInitFile.setOutputName(
        "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS"
    )
    cmpSystemInitFile.setSourcePath(
        "../peripheral/cmp_dac_03496/templates/system/initialization.c.ftl"
    )
    cmpSystemInitFile.setMarkup(True)

    cmpSystemDefFile = cmpdacComponent.createFileSymbol("CMP_SYS_DEF", None)
    cmpSystemDefFile.setType("STRING")
    cmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cmpSystemDefFile.setSourcePath(
        "../peripheral/cmp_dac_03496/templates/system/definitions.h.ftl"
    )
    cmpSystemDefFile.setMarkup(True)
