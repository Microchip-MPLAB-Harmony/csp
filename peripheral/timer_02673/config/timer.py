TMR_INSTANCE_NUMBER = "TMR_INSTANCE_NUMBER"
TMR_INTERRUPT_MODE = "TMR_INTERRUPT_MODE"
TCON_PRE_SCALER = "TCON_PRE_SCALER"
TCON_SRC_SEL = "TCON_SRC_SEL"
TCON_TGATE = "TCON_TGATE"
EXT_CLK_FREQ = "EXT_CLK_FREQ"
TCON_TSYNC = "TCON_TSYNC"
TCON_TWDIS = "TCON_TWDIS"
TIMER_CLOCK_FREQ = "TIMER_CLOCK_FREQ"
TIMER_UNIT = "TIMER_UNIT"
TIME_PERIOD_MS = "TIME_PERIOD_MS"
TIMER_PERIOD = "TIMER_PERIOD"
TCON_SIDL = "TCON_SIDL"
TMR_INTERRUPT_HANDLER = "TMR_INTERRUPT_HANDLER"

CORE = "core"
STD_SPEED_CLK_FREQ = "stdSpeedClkFreq"
EXT_CLK_DEFAULT_FREQ = 0
MODULE_NAME = "Timer"
T_REG_GRP = "T"
CON_REG_NAME = "CON"

timeUnitsToSeconds = {
    "millisecond": 1e3,
    "microsecond": 1e6,
    "nanosecond": 1e9,
}


def getBitfieldData(node):

    result = []
    for bitfield in node.getChildren():
        if bitfield.getAttribute("caption").lower() != "reserved":
            bitfieldValue = bitfield.getAttribute("value")
            bitfieldInt = (
                int(bitfieldValue, 16)
                if bitfieldValue.startswith("0x")
                else int(bitfieldValue)
            )

            result.append(
                {
                    "key": bitfield.getAttribute("name")
                    or bitfield.getAttribute("caption"),
                    "value": str(bitfieldInt),
                    "desc": bitfield.getAttribute("caption"),
                }
            )
    return result


def findKeyValue(value, dict):

    for index, pair in enumerate(dict):
        if pair["value"] == str(value):
            return index
    print("Could not find value in dictionary")
    return ""


def isTmrTGATEVisible(symbol, event):

    key = symbol.getComponent().getSymbolByID(event["id"]).getSelectedKey()
    if key == "OPTION_0":
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)


def isTmrTGATECommentVisible(symbol, event):

    component = symbol.getComponent()
    tmrClkSrc = component.getSymbolByID(TCON_SRC_SEL).getSelectedKey()
    tmrGate = component.getSymbolByID(TCON_TGATE).getSelectedKey()
    if tmrClkSrc == "OPTION_1" and tmrGate == "OPTION_0":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def periodRegCommentDependency(symbol, event):

    symbol.setValue(int(event["value"]))


def isTmrExtClkSrcVisible(symbol, event):

    key = symbol.getComponent().getSymbolByID(event["id"]).getSelectedKey()
    if key == "OPTION_0":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def isTmrAsyncSettingVisible(symbol, event):

    component = symbol.getComponent()
    tmrClkSrc = component.getSymbolByID(TCON_SRC_SEL).getSelectedKey()
    tmrExtClkSyncSelection = component.getSymbolByID(TCON_TSYNC).getSelectedKey()
    if tmrClkSrc == "OPTION_0" and tmrExtClkSyncSelection == "OPTION_1":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def timeFreqCalc(symbol, event):

    component = symbol.getComponent()
    tmrClkSrc = component.getSymbolByID(TCON_SRC_SEL).getSelectedKey()
    clkFreq = (
        component.getSymbolValue(EXT_CLK_FREQ)
        if tmrClkSrc == "OPTION_0"
        else Database.getSymbolValue(CORE, STD_SPEED_CLK_FREQ)
    )

    selectPrescaler = component.getSymbolByID(TCON_PRE_SCALER)
    prescalerStr = selectPrescaler.getKeyDescription(selectPrescaler.getValue())
    symbol.setValue(int(clkFreq) / prescalerStrtoInt(prescalerStr))


# "1:256"-> 256
def prescalerStrtoInt(prescalerStr):

    parts = prescalerStr.split(":")
    if len(parts) == 2 and parts[1].isdigit():
        return int(parts[1])
    return None


def timePeriodCalc(symbol, event):

    component = symbol.getComponent()
    clock = component.getSymbolValue(TIMER_CLOCK_FREQ)
    timerUnitName = component.getSymbolValue(TIMER_UNIT)
    unit = timeUnitsToSeconds[timerUnitName]

    resolution = unit / float(clock) if clock else 0

    symbol.setMax(int(((2**32) - 1) * resolution))

    symbol.setLabel("Time in {}".format(timerUnitName))


def periodRegCalc(symbol, event):

    component = symbol.getComponent()
    clkFreq = component.getSymbolValue(TIMER_CLOCK_FREQ)
    unit = timeUnitsToSeconds[component.getSymbolValue(TIMER_UNIT)]

    if clkFreq:
        period = component.getSymbolValue(TIME_PERIOD_MS) * clkFreq / unit
        symbol.setValue(int(period))
    else:
        symbol.setValue(0)

    # Calculation to be done for drivers, DVRT and such
    # calcAchievableFreq()


def mapToEventValueCallback(symbol, event):

    component = symbol.getComponent()
    symbol = component.getSymbolByID(event["id"])
    return int(symbol.getSelectedValue())


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


def handleInterruptControl(instNum, intMode):
    intIndex = getVectorIndex("T{}Interrupt".format(instNum))

    if intMode == True:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), True)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), True)
    else:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), False)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), False)


def defaultInterruptControl(component):

    instNum = component.getSymbolValue(TMR_INSTANCE_NUMBER)
    intMode = component.getSymbolValue(TMR_INTERRUPT_MODE)

    handleInterruptControl(instNum, intMode)


def interruptControlHelper(symbol, event):

    component = symbol.getComponent()
    instNum = component.getSymbolValue(TMR_INSTANCE_NUMBER)
    intMode = event["value"]

    handleInterruptControl(instNum, intMode)


def interruptStatusWarning(symbol, event):

    if symbol.getComponent().getSymbolValue(TMR_INTERRUPT_MODE) == True:
        symbol.setVisible(not event["value"])
    else:
        symbol.setVisible(False)


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value


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


def customSetDefaultValue(symbol, moduleName, registerGroup, register, bitfield):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        optionList = getBitfieldOptionList(valGroup)
        defaultValue = getSettingBitDefaultValue(
            moduleName, registerGroup, register, bitfield
        )
        symbol.setDefaultValue(getKeyValuePairBasedonValue(defaultValue, optionList))


def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if bitNode != None:
        return bitNode.getAttribute("values")
    return ""


def getValueGroup(moduleName, valueGroupName):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/value-group@[name="'
        + valueGroupName
        + '"]'
    )
    return ATDF.getNode(atdfPath)


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


def addKeystoKeyValueSymbol(bitSymbol, bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey(ii["key"], ii["value"], ii["desc"])


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


def instantiateComponent(tmrComponent):

    tmrInstNum = tmrComponent.createStringSymbol(TMR_INSTANCE_NUMBER, None)
    tmrInstNum.setDefaultValue(tmrComponent.getID().upper().replace("TIMER", ""))
    tmrInstNum.setVisible(False)

    instNum = tmrInstNum.getValue()

    enableInterrupts = tmrComponent.createBooleanSymbol(TMR_INTERRUPT_MODE, None)
    enableInterrupts.setLabel("Enable Interrrupts")
    enableInterrupts.setDefaultValue(True)
    enableInterrupts.setDependencies(interruptControlHelper, [TMR_INTERRUPT_MODE])
    enableInterrupts.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:intc_04436;register:IEC1"
    )
    defaultInterruptControl(enableInterrupts.getComponent())

    ATDF_T_CON__TCS = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__TCS"]'
    )
    clkSrcData = getBitfieldData(ATDF_T_CON__TCS)

    selectTmrClkSrc = tmrComponent.createKeyValueSetSymbol(TCON_SRC_SEL, None)
    selectTmrClkSrc.setLabel("Timer Clock Source")
    selectTmrClkSrc.setOutputMode("Value")
    selectTmrClkSrc.setDisplayMode("Description")
    selectTmrClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:T1CON"
    )
    for clkSrcItem in clkSrcData:
        selectTmrClkSrc.addKey(
            clkSrcItem["key"], clkSrcItem["value"], clkSrcItem["desc"]
        )
    customSetDefaultValue(selectTmrClkSrc, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "TCS")

    ATDF_T_CON__TCKPS = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__TCKPS"]'
    )
    prescalerData = getBitfieldData(ATDF_T_CON__TCKPS)

    selectPrescaler = tmrComponent.createKeyValueSetSymbol(TCON_PRE_SCALER, None)
    selectPrescaler.setLabel("Prescaler")
    selectPrescaler.setOutputMode("Value")
    selectPrescaler.setDisplayMode("Description")
    selectPrescaler.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:T1CON"
    )
    for prescalerItem in prescalerData:
        selectPrescaler.addKey(
            prescalerItem["key"],
            prescalerItem["value"],
            prescalerItem["desc"],
        )

    customSetDefaultValue(
        selectPrescaler, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "TCKPS"
    )
    selectPrescaler.setVisible(True)

    # These symbols are displayed when `Standard Peripheral clock` is selected
    ATDF_T_CON__TGATE = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__TGATE"]'
    )
    tmrGateData = getBitfieldData(ATDF_T_CON__TGATE)

    tmrGateAccumulation = tmrComponent.createKeyValueSetSymbol(
        TCON_TGATE, selectTmrClkSrc
    )
    tmrGateAccumulation.setLabel("Timer Gated Time Accumulation")
    tmrGateAccumulation.setOutputMode("Value")
    tmrGateAccumulation.setDisplayMode("Description")
    tmrGateAccumulation.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:T1CON"
    )
    for tmrGateItem in tmrGateData:
        tmrGateAccumulation.addKey(
            tmrGateItem["key"], tmrGateItem["value"], tmrGateItem["desc"]
        )
    customSetDefaultValue(
        tmrGateAccumulation, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "TGATE"
    )
    tmrGateAccumulation.setDependencies(isTmrTGATEVisible, [TCON_SRC_SEL])

    tgateComment = tmrComponent.createCommentSymbol("TGATE_COMMENT", selectTmrClkSrc)
    tgateComment.setLabel("Ensure the T1CK pin is properly configured to drive TGATE")
    tgateComment.setVisible(False)
    tgateComment.setDependencies(isTmrTGATECommentVisible, [TCON_SRC_SEL, TCON_TGATE])

    # These symbols are displayed when `External clock` is selected

    extClkFreq = tmrComponent.createIntegerSymbol(EXT_CLK_FREQ, selectTmrClkSrc)
    extClkFreq.setLabel("External Clock Frequency(In Hz)")
    extClkFreq.setDefaultValue(int(EXT_CLK_DEFAULT_FREQ))
    extClkFreq.setVisible(False)
    extClkFreq.setMin(0)
    extClkFreq.setDependencies(isTmrExtClkSrcVisible, [TCON_SRC_SEL])

    ATDF_T_CON__TSYNC = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__TSYNC"]'
    )
    tmrExtClkSyncData = getBitfieldData(ATDF_T_CON__TSYNC)

    tmrExtClkSyncSelection = tmrComponent.createKeyValueSetSymbol(
        TCON_TSYNC, selectTmrClkSrc
    )
    tmrExtClkSyncSelection.setLabel("Timer External Clock Input Synchronization")
    tmrExtClkSyncSelection.setOutputMode("Value")
    tmrExtClkSyncSelection.setDisplayMode("Description")
    tmrExtClkSyncSelection.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:T1CON"
    )
    for tmrExtClkSyncItem in tmrExtClkSyncData:
        tmrExtClkSyncSelection.addKey(
            tmrExtClkSyncItem["key"],
            tmrExtClkSyncItem["value"],
            tmrExtClkSyncItem["desc"],
        )
    customSetDefaultValue(
        tmrExtClkSyncSelection, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "TSYNC"
    )
    tmrExtClkSyncSelection.setVisible(False)
    tmrExtClkSyncSelection.setDependencies(isTmrExtClkSrcVisible, [TCON_SRC_SEL])

    ATDF_T_CON__TMWDIS = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__TMWDIS"]'
    )
    tmrAsyncWriteData = getBitfieldData(ATDF_T_CON__TMWDIS)

    tmrAsyncWriteSelection = tmrComponent.createKeyValueSetSymbol(
        TCON_TWDIS, tmrExtClkSyncSelection
    )
    tmrAsyncWriteSelection.setLabel("Asynchronous Timer Write Disable")
    tmrAsyncWriteSelection.setVisible(False)
    tmrAsyncWriteSelection.setOutputMode("Value")
    tmrAsyncWriteSelection.setDisplayMode("Description")
    tmrAsyncWriteSelection.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:T1CON"
    )
    for tmrAsyncWriteItem in tmrAsyncWriteData:
        tmrAsyncWriteSelection.addKey(
            tmrAsyncWriteItem["key"],
            tmrAsyncWriteItem["value"],
            tmrAsyncWriteItem["desc"],
        )
    customSetDefaultValue(
        tmrAsyncWriteSelection, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "TMWDIS"
    )
    tmrAsyncWriteSelection.setDependencies(
        isTmrAsyncSettingVisible,
        [TCON_SRC_SEL, TCON_TSYNC],
    )

    tmrClkFreq = tmrComponent.createIntegerSymbol(TIMER_CLOCK_FREQ, None)
    tmrClkFreq.setLabel("Timer Clock Frequency(In Hz)")
    tmrClkFreq.setVisible(True)
    tmrClkFreq.setReadOnly(True)
    tmrClkFreq.setDefaultValue(int(Database.getSymbolValue(CORE, STD_SPEED_CLK_FREQ)))
    tmrClkFreq.setDependencies(
        timeFreqCalc,
        [
            TCON_PRE_SCALER,
            TCON_SRC_SEL,
            EXT_CLK_FREQ,
            "core." + STD_SPEED_CLK_FREQ,
        ],
    )

    timeMenu = tmrComponent.createMenuSymbol("TIME_MENU", None)
    timeMenu.setLabel("Requested Timer Period")

    timerUnit = tmrComponent.createComboSymbol(
        TIMER_UNIT, timeMenu, ["millisecond", "microsecond", "nanosecond"]
    )
    timerUnit.setLabel("Timer Period Unit")
    timerUnit.setDefaultValue("millisecond")

    # Create common func
    clkFreq = Database.getSymbolValue(CORE, STD_SPEED_CLK_FREQ)
    prescalerStr = selectPrescaler.getKeyDescription(selectPrescaler.getValue())
    resolution = (
        1e3 * prescalerStrtoInt(prescalerStr) / float(clkFreq) if clkFreq else 0
    )
    maxTmrPeriod = (2**32) * resolution if clkFreq else 0

    timePeriodMs = tmrComponent.createFloatSymbol(TIME_PERIOD_MS, timeMenu)
    timePeriodMs.setLabel("Time in millisecond")
    timePeriodMs.setDefaultValue(1.0)
    timePeriodMs.setMin(0.0)
    timePeriodMs.setMax(int(maxTmrPeriod))
    timePeriodMs.setDependencies(
        timePeriodCalc,
        [
            "core." + STD_SPEED_CLK_FREQ,
            TIMER_CLOCK_FREQ,
            TIMER_UNIT,
        ],
    )

    periodReg = tmrComponent.createHexSymbol(TIMER_PERIOD, timePeriodMs)
    periodReg.setLabel("Period Register")
    periodReg.setDefaultValue(
        int(timePeriodMs.getValue() / resolution - 1) if clkFreq else 0
    )

    periodReg.setReadOnly(True)
    periodReg.setMin(0)
    periodReg.setMax(0xFFFFFFFF)
    periodReg.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:timer_02673;register:PR1"
    )
    periodReg.setDependencies(
        periodRegCalc,
        [
            "core." + STD_SPEED_CLK_FREQ,
            TIME_PERIOD_MS,
            TIMER_CLOCK_FREQ,
            TIMER_UNIT,
        ],
    )

    periodRegComment = tmrComponent.createIntegerSymbol(
        "PERIOD_REG_COMMENT", timePeriodMs
    )
    periodRegComment.setDefaultValue(
        int(timePeriodMs.getValue() / resolution - 1) if clkFreq else 0
    )
    periodRegComment.setDependencies(
        periodRegCommentDependency,
        [TIMER_PERIOD],
    )
    periodRegComment.setVisible(False)

    ATDF_T_CON__SIDL = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="Timer"]/value-group@[name="T_CON__SIDL"]'
    )
    tmrSidlData = getBitfieldData(ATDF_T_CON__SIDL)

    tmrSIDL = tmrComponent.createKeyValueSetSymbol(TCON_SIDL, None)
    tmrSIDL.setLabel("Stop in IDLE Mode Bit")
    tmrSIDL.setOutputMode("Value")
    tmrSIDL.setDisplayMode("Description")
    for tmrSidlItem in tmrSidlData:
        tmrSIDL.addKey(tmrSidlItem["key"], tmrSidlItem["value"], tmrSidlItem["desc"])
    customSetDefaultValue(tmrSIDL, MODULE_NAME, T_REG_GRP, CON_REG_NAME, "SIDL")
    tmrSIDL.setVisible(False)

    intIndex = getVectorIndex("T{}Interrupt".format(instNum))

    tmrComment = tmrComponent.createCommentSymbol("ENABLE_COMMENT", None)
    tmrComment.setVisible(
        not bool(Database.getSymbolValue(CORE, "INTC_{}_ENABLE".format(intIndex)))
    )
    tmrComment.setLabel(
        "Warning!!! Enable Timer {} Interrupt in Interrupts Section of System module".format(
            instNum
        )
    )
    tmrComment.setDependencies(
        interruptStatusWarning, ["core." + "INTC_" + str(intIndex) + "_ENABLE"]
    )

    tmrIntHandler = tmrComponent.createStringSymbol(TMR_INTERRUPT_HANDLER, None)
    tmrIntHandler.setDefaultValue(
        Database.getSymbolValue(CORE, "INTC_{}_INTERRUPT_HANDLER".format(intIndex))
    )
    tmrIntHandler.setVisible(False)

    tconRegPor = tmrComponent.createStringSymbol("TCON_REG_POR", None)
    tconRegPor.setDefaultValue(getRegisterDefaultValue("Timer", "T", "CON"))
    tconRegPor.setVisible(False)

    tmrRegPor = tmrComponent.createStringSymbol("TMR_REG_POR", None)
    tmrRegPor.setDefaultValue(getRegisterDefaultValue("Timer", "TMR", "TMR"))
    tmrRegPor.setVisible(False)

    prRegPor = tmrComponent.createStringSymbol("PR_REG_POR", None)
    prRegPor.setDefaultValue(getRegisterDefaultValue("Timer", "PR", "PR"))
    prRegPor.setVisible(False)

    # Code Generation

    configName = Variables.get("__CONFIGURATION_NAME")

    tmrCommonFile = tmrComponent.createFileSymbol("TMR_COMMON_HEADER", None)
    tmrCommonFile.setSourcePath("../peripheral/timer_02673/templates/plib_tmr_common.h")
    tmrCommonFile.setOutputName("plib_tmr_common.h")
    tmrCommonFile.setDestPath("peripheral/tmr/")
    tmrCommonFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrCommonFile.setType("HEADER")
    tmrCommonFile.setMarkup(False)
    tmrCommonFile.setOverwrite(True)

    # Instance Header File
    tmrHeaderFile = tmrComponent.createFileSymbol("TMR_HEADER", None)
    tmrHeaderFile.setSourcePath("../peripheral/timer_02673/templates/plib_tmr.h.ftl")
    tmrHeaderFile.setOutputName("plib_tmr{}.h".format(instNum))
    tmrHeaderFile.setDestPath("/peripheral/tmr/")
    tmrHeaderFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrHeaderFile.setType("HEADER")
    tmrHeaderFile.setMarkup(True)
    tmrHeaderFile.setOverwrite(True)

    # Instance Source File
    tmrSourceFile = tmrComponent.createFileSymbol("TMR_SOURCE", None)
    tmrSourceFile.setSourcePath("../peripheral/timer_02673/templates/plib_tmr.c.ftl")
    tmrSourceFile.setOutputName("plib_tmr{}.c".format(instNum))
    tmrSourceFile.setDestPath("/peripheral/tmr/")
    tmrSourceFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrSourceFile.setType("SOURCE")
    tmrSourceFile.setMarkup(True)
    tmrSourceFile.setOverwrite(True)

    tmrSystemInitFile = tmrComponent.createFileSymbol("TMR_SYS_INT", None)
    tmrSystemInitFile.setType("STRING")
    tmrSystemInitFile.setOutputName(
        "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS"
    )
    tmrSystemInitFile.setSourcePath(
        "../peripheral/timer_02673/templates/system/initialization.c.ftl"
    )
    tmrSystemInitFile.setMarkup(True)

    tmrSystemDefFile = tmrComponent.createFileSymbol("TMR_SYS_DEF", None)
    tmrSystemDefFile.setType("STRING")
    tmrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tmrSystemDefFile.setSourcePath(
        "../peripheral/timer_02673/templates/system/definitions.h.ftl"
    )
    tmrSystemDefFile.setMarkup(True)
