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


def createBooleanSymbol(
    component, moduleName, registerGroup, register, bitfield, menuName
):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        symbolKey = valueGroupEntry
        valueGroupEntryComp = component.createBooleanSymbol(symbolKey, menuName)
        valueGroupEntryComp.setLabel(symbolKey)
        return valueGroupEntryComp


def showOnEnableDependency(symbol, event):

    symbol.setVisible(event["value"])


def extractDividerValue(clkDivStr):

    parts = clkDivStr.split(":")
    clkDivNum = int(parts[1])
    return clkDivNum


def clkFreqDependency(symbol, event):

    component = symbol.getComponent()
    clkDiv = component.getSymbolByID("QEI_CON__INTDIV").getSelectedKey()

    symbol.setValue(
        int(
            Database.getSymbolValue("core", "stdSpeedClkFreq")
            / extractDividerValue(clkDiv)
        )
    )


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


def create_reg_por_set_string(module, registers_by_group, instNum):
    import re

    """
    Generates a formatted string of default register values for a given module and a dictionary of register groups and registers,
    incorporating the provided instance number.
    """
    reg_defaults = {}  # Dictionary to store default values for each register
    reg_por_set = ""  # Initialize the regPorSet output string

    # Iterate through the dictionary of register groups and their registers
    for register_group, registers in registers_by_group.items():
        for reg in registers:
            # Form key as register_group + instNum + reg
            reg_name = "{}{}{}".format(register_group, instNum, reg)
            reg_defaults[reg_name] = getRegisterDefaultValue(
                module, register_group, reg
            )

    # Format the output string with 4-space indentation per register
    for reg_name, default_val in reg_defaults.items():
        reg_por_set += "    {} = {};\n".format(reg_name, default_val)

    return reg_por_set


def instantiateComponent(qeiComponent):

    qeiInstNum = qeiComponent.createStringSymbol("QEI_INSTANCE_NUMBER", None)
    qeiInstNum.setDefaultValue(qeiComponent.getID().upper().replace("QEI", ""))
    qeiInstNum.setVisible(False)

    inpClkPrescaler = createKeyValueSetSymbol(
        qeiComponent, "QEI", "QEI", "CON", "INTDIV", None
    )
    inpClkPrescaler.setLabel("Input Clock Prescaler")
    inpClkPrescaler.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1CON"
    )

    clkSrcFreq = qeiComponent.createIntegerSymbol("CLK_SRC_FREQ", None)
    clkSrcFreq.setLabel("Clock Calculated Frequency(Hz)")
    clkSrcFreq.setDefaultValue(Database.getSymbolValue("core", "stdSpeedClkFreq"))
    clkSrcFreq.setReadOnly(True)
    clkSrcFreq.setDependencies(
        clkFreqDependency, ["QEI_CON__INTDIV", "core." + "stdSpeedClkFreq"]
    )

    posCountInit = qeiComponent.createKeyValueSetSymbol("QEI_CON__PIMOD", None)
    posCountInit.setLabel("Operation Mode")
    posCountInit.addKey("Free running mode", "0", "Free running mode")
    posCountInit.addKey("Reset on index mode", "1", "Reset on index mode")
    posCountInit.addKey("Modulo Count mode", "6", "Modulo Count mode")
    posCountInit.setOutputMode("Value")
    posCountInit.setDisplayMode("Description")
    posCountInit.setDefaultValue(0)
    posCountInit.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1CON"
    )

    digitalFilter = createBooleanSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "FLTREN", None
    )
    digitalFilter.setLabel("Digital Filter")
    digitalFilter.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    digitalFilterClkDivide = createKeyValueSetSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "QFDIV", digitalFilter
    )
    digitalFilterClkDivide.setLabel("Digital Input Filter Clock Divide")
    digitalFilterClkDivide.setVisible(False)
    digitalFilterClkDivide.setDependencies(showOnEnableDependency, ["QEI_IOC__FLTREN"])
    digitalFilterClkDivide.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    isIndPulseEnabled = qeiComponent.createBooleanSymbol("IS_INDEX_PULSE_ENABLED", None)
    isIndPulseEnabled.setLabel("Enable Index Pulse settings")

    indxxInpPol = createBooleanSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "IDXPOL", isIndPulseEnabled
    )
    indxxInpPol.setLabel("Index Input Polarity")
    indxxInpPol.setVisible(False)
    indxxInpPol.setDependencies(showOnEnableDependency, ["IS_INDEX_PULSE_ENABLED"])
    indxxInpPol.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    indPulseCapture = createBooleanSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "QCAPEN", isIndPulseEnabled
    )
    indPulseCapture.setLabel("Index Pulse Capture")
    indPulseCapture.setVisible(False)
    indPulseCapture.setDependencies(showOnEnableDependency, ["IS_INDEX_PULSE_ENABLED"])
    indPulseCapture.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    isHomeSignEnabled = qeiComponent.createBooleanSymbol("IS_HOME_SIGNAL_ENABLED", None)
    isHomeSignEnabled.setLabel("Enable Home Signal settings")

    homexInpPol = createBooleanSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "HOMPOL", isHomeSignEnabled
    )
    homexInpPol.setLabel("Home Input Polarity")
    homexInpPol.setVisible(False)
    homexInpPol.setDependencies(showOnEnableDependency, ["IS_HOME_SIGNAL_ENABLED"])
    homexInpPol.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    homePulseCapture = createBooleanSymbol(
        qeiComponent, "QEI", "QEI", "IOC", "HCAPEN", isHomeSignEnabled
    )
    homePulseCapture.setLabel("Home Pulse Capture")
    homePulseCapture.setVisible(False)
    homePulseCapture.setDependencies(showOnEnableDependency, ["IS_HOME_SIGNAL_ENABLED"])
    homePulseCapture.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1IOC"
    )

    posComp = qeiComponent.createMenuSymbol("POSITION_COMPARATOR", None)
    posComp.setLabel("Position Comparator")

    qeixLec = qeiComponent.createHexSymbol("QEIxLEC", posComp)
    qeixLec.setLabel("QEI{}LEC".format(qeiInstNum.getValue()))
    qeixLec.setMin(0)
    qeixLec.setMax(0xFFFFFFFF)
    qeixLec.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1LEC"
    )

    qeixGec = qeiComponent.createHexSymbol("QEIxGEC", posComp)
    qeixGec.setLabel("QEI{}GEC".format(qeiInstNum.getValue()))
    qeixGec.setMin(0)
    qeixGec.setMax(0xFFFFFFFF)
    qeixGec.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:qei_05177;register:QEI1GEC"
    )

    # Code generation

    moduleName = qeiComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue("QEI{}".format(qeiInstNum.getValue()))
    moduleName.setVisible(False)

    regPorSet = qeiComponent.createStringSymbol("regPorSet", None)
    regPorDict = {
        "QEI": ["CON", "IOC", "STAT", "GEC", "LEC"],
        "POS": ["CNT", "HLD"],
        "VEL": ["CNT", "HLD"],
        "INT": ["TMR", "HLD", "HLD"],
        "INDX": ["CNT", "HLD"],
    }
    regPorSet.setDefaultValue(
        create_reg_por_set_string("QEI", regPorDict, qeiInstNum.getValue())
    )
    regPorSet.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    qeiHeaderFile = qeiComponent.createFileSymbol("QEI_HEADER", None)
    qeiHeaderFile.setSourcePath("../peripheral/qei_05177/templates/plib_qei1.h.ftl")
    qeiHeaderFile.setOutputName("plib_qei{}.h".format(qeiInstNum.getValue()))
    qeiHeaderFile.setDestPath("/peripheral/qei/")
    qeiHeaderFile.setProjectPath("config/" + configName + "/peripheral/qei/")
    qeiHeaderFile.setType("HEADER")
    qeiHeaderFile.setMarkup(True)
    qeiHeaderFile.setOverwrite(True)

    # Instance Source File
    qeiSourceFile = qeiComponent.createFileSymbol("QEI_SOURCE", None)
    qeiSourceFile.setSourcePath("../peripheral/qei_05177/templates/plib_qei1.c.ftl")
    qeiSourceFile.setOutputName("plib_qei{}.c".format(qeiInstNum.getValue()))
    qeiSourceFile.setDestPath("/peripheral/qei/")
    qeiSourceFile.setProjectPath("config/" + configName + "/peripheral/qei/")
    qeiSourceFile.setType("SOURCE")
    qeiSourceFile.setMarkup(True)
    qeiSourceFile.setOverwrite(True)

    qeiSystemInitFile = qeiComponent.createFileSymbol("QEI_SYS_INT", None)
    qeiSystemInitFile.setType("STRING")
    qeiSystemInitFile.setOutputName(
        "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS"
    )
    qeiSystemInitFile.setSourcePath(
        "../peripheral/qei_05177/templates/system/initialization.c.ftl"
    )
    qeiSystemInitFile.setMarkup(True)

    qeiSystemDefFile = qeiComponent.createFileSymbol("QEI_SYS_DEF", None)
    qeiSystemDefFile.setType("STRING")
    qeiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qeiSystemDefFile.setSourcePath(
        "../peripheral/qei_05177/templates/system/definitions.h.ftl"
    )
    qeiSystemDefFile.setMarkup(True)
