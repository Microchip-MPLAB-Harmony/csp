import re

SENT_CON1__TXM                = "SENT_CON1__TXM"
SENT_CON1__PS                 = "SENT_CON1__PS"
SENT_CON1__RCVEN              = "SENT_CON1__RCVEN"
SENT_CON1__SIDL               = "SENT_CON1__SIDL"
SENT_CON1__ON                 = "SENT_CON1__ON"
SENT_CON1__SPCEN              = "SENT_CON1__SPCEN"
SENT_CON1__NIBCNT             = "SENT_CON1__NIBCNT"
SENT_CON1__CRCEN              = "SENT_CON1__CRCEN"
SENT_CON1__TXPOL              = "SENT_CON1__TXPOL"
SENT_CON1__PPP                = "SENT_CON1__PPP"
TRANSMITTER                   = "Transmitter"
RECEIVER                      = "Receiver"
ASYNCHRONOUS                  = "Asynchronous"
SYNCHRONOUS                   = "Synchronous"
INVERTED                      = "Inverted"
NON_INVERTED                  = "Non Inverted"
REQUESTED_TICK_TIME           = "REQUESTED_TICK_TIME"
CLOCK_FREQUENCY               = "CLOCK_FREQUENCY"
CORE_COMPONENT                = "core"
SYSTEM_CLOCK_FREQ             = "sysClockFrequency"
CALCULATED_TICK_TIME          = "CALCULATED_TICK_TIME"
REQUESTED_FRAME_TIME          = "REQUESTED_FRAME_TIME"
CALCULATED_FRAME_TIME         = "CALCULATED_FRAME_TIME"
CLOCK_DIVIDER                 = "CLOCK_DIVIDER"
TICK_TIME                     = "TICK_TIME"
FRAME_TIME                    = "FRAME_TIME"
SENT                          = "SENT"
INTERRUPT_MODE                = "SENT_INTERRUPT_MODE"
SYNCMIN                       = "SYNC_MIN"
SYNCMAX                       = "SYNC_MAX"
CLOCK_SOURCE                  = "CLOCK_SOURCE"
SENT_INSTANCE                 = "SENT_INSTANCE"

####### Numeric Data #######

MICRO_SECONDS = 1000000
MIN_FRAMETIME_FACTOR = 122
MIN_FRAMETIME_MULTIPLICATION_FACTOR = 27
MAX_FRAMETIME_MULTIPLICATION_FACTOR = 12
MAX_FRAMETIME_FACTOR = 848
MIN_TICK_TIME = 3
MAX_TICK_TIME = 90
SYNCMIN_ERROR_FACTOR = 0.8
SYNCMAX_ERROR_FACTOR = 1.2

intVectorDataDictionary = {}

####### Callbacks for ATDF #######

def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

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

def customSetDefaultValue(symbol, moduleName, registerGroup, register, bitfield):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        optionList = getBitfieldOptionList(valGroup)
        defaultValue = getSettingBitDefaultValue(
            moduleName, registerGroup, register, bitfield
        )
        symbol.setDefaultValue(getKeyValuePairBasedonValue(defaultValue, optionList))

def getModuleRegisterGroup(moduleName, registerGroup):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]'
    )
    registerGroupNode = ATDF.getNode(atdfPath)
    if registerGroupNode != None:
        return registerGroupNode.getChildren()
    return None

####### Callbacks for Symbols #######

def transmitModeVisibility(symbol, event):
    symbol.setVisible(symbol.getComponent().getSymbolValue(SENT_CON1__RCVEN) == TRANSMITTER)

def setSysClkFreq(symbol, event):
    
    systemClockFreq = int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_CLOCK_FREQ)) / 2
    sentCon1PsValue = Database.getSymbolValue(symbol.getComponent().getID(), SENT_CON1__PS)

    if sentCon1PsValue == "Divide-by-4":
        clockFreq = systemClockFreq / 4
    else:
        clockFreq = systemClockFreq / 1

    symbol.setValue(clockFreq)
    symbol.setVisible(symbol.getComponent().getSymbolValue(SENT_CON1__RCVEN) == TRANSMITTER)

def getTickTime(tickTime, clkFreq):

    if clkFreq == 0:
        return '0x0'

    calTickTime = ((tickTime * clkFreq) / MICRO_SECONDS) - 1
    return hex(int(calTickTime))

def updateTickTime(symbol, event):

    requestedTickTime = symbol.getComponent().getSymbolValue(REQUESTED_TICK_TIME)
    clkFreq  = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
    calculatedTickTime = getTickTime(requestedTickTime, clkFreq)
    symbol.setValue(int(calculatedTickTime, 16)) 
    
def getTickPeriodCalculation(tickTime, clkFreq):

    if clkFreq == 0:
        return 0
    
    freq = clkFreq / MICRO_SECONDS
    calTickPeriod = (tickTime+1) / freq
    return calTickPeriod

def updateTickPeriodCalculated(symbol, event):

    clkFreq = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
    tickTime = symbol.getComponent().getSymbolValue(TICK_TIME)
    calculatedTickTimePeriod = getTickPeriodCalculation(tickTime, clkFreq)
    symbol.setValue(calculatedTickTimePeriod)

def getMinFrameTimeInUs(datalength, requestedticktime):
    return ((MIN_FRAMETIME_FACTOR + MIN_FRAMETIME_MULTIPLICATION_FACTOR * int(datalength)) * int(requestedticktime))

def getMaxFrameTimeInUs(datalength, requestedticktime):
    return ((MAX_FRAMETIME_FACTOR + MAX_FRAMETIME_MULTIPLICATION_FACTOR * int(datalength)) * int(requestedticktime))

def updateRequestedFrameTime(symbol, event):
    if event["id"] == SENT_CON1__PPP:
        symbol.setVisible(event["value"])

    requestedTickTime = symbol.getComponent().getSymbolValue(REQUESTED_TICK_TIME)
    dataLength = symbol.getComponent().getSymbolValue(SENT_CON1__NIBCNT )
    minFrameTime = getMinFrameTimeInUs(dataLength, requestedTickTime)
    maxFrameTime = getMaxFrameTimeInUs(dataLength, requestedTickTime)
    symbol.setMin(minFrameTime)
    symbol.setMax(maxFrameTime)
    symbol.setValue(minFrameTime)

def getFrameTime(requestedFrameTime, requestedTickTime):

    calFrameTime = (requestedFrameTime / requestedTickTime)
    return hex(int(calFrameTime))
    
def updateFrameTime(symbol, event):
    if event["id"] == SENT_CON1__PPP :
        symbol.setVisible(False)
    else:
        requestedframeTime = symbol.getComponent().getSymbolValue(REQUESTED_FRAME_TIME)
        requestedTickTime = symbol.getComponent().getSymbolValue(REQUESTED_TICK_TIME)
        calculatedFrameTime = getFrameTime(requestedframeTime, requestedTickTime)
        symbol.setValue(int(calculatedFrameTime, 16))

def getCalculatedFrameTime(frametime, requestedticktime):
    return (frametime * requestedticktime)

def updateCalculatedFrameTime(symbol, event):
    if event["id"] == SENT_CON1__PPP :
        symbol.setVisible(event["value"])
    else:
        requestedTickTime = symbol.getComponent().getSymbolValue(REQUESTED_TICK_TIME)
        frameTime = symbol.getComponent().getSymbolValue(FRAME_TIME)
        calculatedFrameTime = getCalculatedFrameTime(requestedTickTime, frameTime)
        symbol.setValue(calculatedFrameTime)

valueGroupNode_NibbleCount = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SENT"]/value-group@[name="SENT_CON1__NIBCNT"]')
dataLength = valueGroupNode_NibbleCount.getChildren()
nibbleCountCaptions = []

for cap in dataLength:
    nibbleCount = cap.getAttribute("caption")
    nibbleCountCaptions.append(nibbleCount)

nibbleCountCaptionsArray = nibbleCountCaptions

valueGroupNode_preScaler = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SENT"]/value-group@[name="SENT_CON1__PS"]')
preScaler = valueGroupNode_preScaler.getChildren()
preScalerList = []

for cap in preScaler:
    preScalerValue = cap.getAttribute("caption")
    preScalerList.append(preScalerValue)

def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
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

def sentTransmitModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID(SENT_CON1__RCVEN).getValue() == TRANSMITTER)

def sentRecieveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID(SENT_CON1__RCVEN).getValue() == RECEIVER)

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break
    return vector_index

def getMinSyncTime(calculatedTickTime, clkFreq):

    syncMin = round((SYNCMIN_ERROR_FACTOR * (8 * calculatedTickTime * (clkFreq / MICRO_SECONDS))))
    return hex(int(syncMin))

def updateSyncMinTime(symbol, event):

    calculatedTickTime = symbol.getComponent().getSymbolValue(CALCULATED_TICK_TIME)
    clkFreq = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
    calculatedSyncMinTime = getMinSyncTime(calculatedTickTime, clkFreq)
    symbol.setValue(int(calculatedSyncMinTime, 16))

def getMaxSyncTime(calculatedTickTime, clkFreq):

    syncMax = round((SYNCMAX_ERROR_FACTOR * (8 * calculatedTickTime * (clkFreq / MICRO_SECONDS))))
    return hex(int(syncMax))

def updateSyncMaxTime(symbol, event):

    calculatedTickTime = symbol.getComponent().getSymbolValue(CALCULATED_TICK_TIME)
    clkFreq = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
    calculatedSyncMaxTime = getMaxSyncTime(calculatedTickTime, clkFreq)
    symbol.setValue(int(calculatedSyncMaxTime, 16))

def interruptStatusWarning(symbol, event):

    sentOperatingValue = symbol.getComponent().getSymbolValue(SENT_CON1__RCVEN)
    sentInstanceName = symbol.getComponent().getSymbolValue("SENT_INSTANCE_NAME")
    interruptMode = symbol.getComponent().getSymbolValue(INTERRUPT_MODE)

    if sentOperatingValue == TRANSMITTER and interruptMode:
        transmitterInterrupt = next((intIndex for key, intIndex in intVectorDataDictionary.items() if key == sentInstanceName + "Interrupt"), None)
        symbol.setVisible(not bool(Database.getSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(transmitterInterrupt))))
    elif sentOperatingValue == RECEIVER and interruptMode:
        recieveInterrupt = next((intIndex for key, intIndex in intVectorDataDictionary.items() if key == sentInstanceName + "Interrupt" or key == sentInstanceName + "EInterrupt"), None)
        symbol.setVisible(not bool(Database.getSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(recieveInterrupt))))
        
def updatePattern(symbol, event):
    sentInstanceName = symbol.getComponent().getSymbolValue("SENT_INSTANCE_NAME")
    sentOperatingValue = symbol.getComponent().getSymbolValue(SENT_CON1__RCVEN)
    interruptMode = symbol.getComponent().getSymbolValue(INTERRUPT_MODE)

    pattern = r"^" + sentInstanceName + r"(EInterrupt|Interrupt)"
    symbol.setValue(pattern)

    for interrupt in interruptsChildrenList:
        vIndex = int(interrupt.getAttribute("index"))
        vName = str(interrupt.getAttribute("name"))
        currentPattern = symbol.getValue()

        if re.search(currentPattern, vName):
            intVectorDataDictionary[vName] = vIndex

    for intIndex in intVectorDataDictionary.values():
        Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex), False)
        Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_HANDLER_LOCK".format(intIndex), False)

    for key, intIndex in intVectorDataDictionary.items():
        if interruptMode:
            if (sentOperatingValue == RECEIVER and (key == sentInstanceName + "Interrupt" or key == sentInstanceName + "EInterrupt")) or \
            (sentOperatingValue == TRANSMITTER and key == sentInstanceName + "Interrupt"):
                Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex), True)
                Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_HANDLER_LOCK".format(intIndex), True)

  
def instantiateComponent(sentComponent):

    global sentInstance, intVectorDataDictionary, interruptsChildrenList
    intVectorDataDictionary = {}

    sentInstance = sentComponent.createStringSymbol(SENT_INSTANCE, None)
    sentInstance.setVisible(False)
    sentInstance.setDefaultValue(sentComponent.getID().upper().replace("SENT",""))

    sentInstanceName = sentComponent.createStringSymbol("SENT_INSTANCE_NAME", None)
    sentInstanceName.setVisible(False)
    sentInstanceName.setDefaultValue(sentComponent.getID().upper())

    # Transmission Type
    transmissionType = sentComponent.createComboSymbol(SENT_CON1__RCVEN, None, [TRANSMITTER, RECEIVER])
    transmissionType.setLabel("Operation Mode")
    transmissionType.setDefaultValue(TRANSMITTER)
    transmissionType.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    #Menu 
    messageSettings = sentComponent.createMenuSymbol("MESSAGE_SETTINGS", None)
    messageSettings.setLabel("Message Settings")

    # Operating Mode
    operatingMode = sentComponent.createComboSymbol(SENT_CON1__TXM, messageSettings, [ASYNCHRONOUS, SYNCHRONOUS])
    operatingMode.setLabel("Operating Mode")
    operatingMode.setDefaultValue(ASYNCHRONOUS)
    operatingMode.setDependencies(transmitModeVisibility, [SENT_CON1__RCVEN])
    operatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    # Pre Scaler
    preScaler = sentComponent.createComboSymbol(SENT_CON1__PS, messageSettings, preScalerList)
    preScaler.setLabel("Prescaler")
    preScaler.setDefaultValue(preScalerList[-1])
    preScaler.setDependencies(transmitModeVisibility, [SENT_CON1__RCVEN])
    preScaler.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    # Clock Source
    clockSource = sentComponent.createStringSymbol(CLOCK_SOURCE, messageSettings)
    clockSource.setLabel("Clock Source")
    clockSource.setDefaultValue("Standard Speed Peripheral Clock")
    clockSource.setReadOnly(True)

    # Clock Frequency
    clockFrequency = sentComponent.createIntegerSymbol(CLOCK_FREQUENCY, messageSettings)
    clockFrequency.setLabel("Clock Frequency (Hz)")
    clockFrequency.setDefaultValue(int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_CLOCK_FREQ)/2 or 0))
    clockFrequency.setReadOnly(True)
    clockFrequency.setDependencies(setSysClkFreq, [CORE_COMPONENT+"."+SYSTEM_CLOCK_FREQ, SENT_CON1__PS])
 
    # Requested Nominal Tick Time
    requestedTickTime = sentComponent.createIntegerSymbol(REQUESTED_TICK_TIME, messageSettings)
    requestedTickTime.setLabel("Requested Nominal Tick Time (us)")
    requestedTickTime.setMin(MIN_TICK_TIME)
    requestedTickTime.setMax(MAX_TICK_TIME)
    requestedTickTime.setDefaultValue(MIN_TICK_TIME)
    requestedTickTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON2")
 
    # TICKTIME  for register (SENTxCON2)
    tickTime = sentComponent.createHexSymbol(TICK_TIME, messageSettings)
    tickTime.setLabel("Tick Time in (us)")
    tickTimeValue = getTickTime(requestedTickTime.getValue(), clockFrequency.getValue())
    tickTime.setDefaultValue(int(tickTimeValue, 16))
    tickTime.setVisible(False)
    tickTime.setDependencies(updateTickTime, [CLOCK_FREQUENCY, REQUESTED_TICK_TIME])
    tickTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON2")

    # Tick Period Calculation
    tickPeriodCalculation = sentComponent.createIntegerSymbol(CALCULATED_TICK_TIME, messageSettings)
    tickPeriodCalculation.setLabel("Calculated Nominal Tick Time (us)")
    tickPeriod = int(getTickPeriodCalculation(tickTime.getValue(), clockFrequency.getValue()))
    tickPeriodCalculation.setReadOnly(True)
    tickPeriodCalculation.setDefaultValue(tickPeriod)
    tickPeriodCalculation.setDependencies(updateTickPeriodCalculated, [TICK_TIME, CLOCK_FREQUENCY])

    #Enable Hardware CRC
    enableHardwareCRC = sentComponent.createBooleanSymbol(SENT_CON1__CRCEN , messageSettings)
    enableHardwareCRC.setLabel("Enable Hardware CRC")
    enableHardwareCRC.setDefaultValue(True)
    enableHardwareCRC.setReadOnly(True)
    enableHardwareCRC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    #Data Length
    dataLength = sentComponent.createComboSymbol(SENT_CON1__NIBCNT, messageSettings, nibbleCountCaptionsArray)
    dataLength.setLabel("Data Length (Nibbles)")
    defaultValue = nibbleCountCaptionsArray[0]
    dataLength.setDefaultValue(defaultValue)
    dataLength.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    #Polarity
    polarity = sentComponent.createComboSymbol(SENT_CON1__TXPOL, messageSettings, [INVERTED, NON_INVERTED])
    polarity.setLabel("Polarity")
    polarity.setDefaultValue(NON_INVERTED)
    polarity.setDependencies(transmitModeVisibility, [SENT_CON1__RCVEN])
    polarity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    # Enable Pause Pulse
    enablePausePulse = sentComponent.createBooleanSymbol(SENT_CON1__PPP, None)
    enablePausePulse.setLabel("Enable Pause Pulse")
    enablePausePulse.setDefaultValue(False)
    enablePausePulse.setDependencies(transmitModeVisibility, [SENT_CON1__RCVEN])
    enablePausePulse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON1")

    # Requested Nominal Frame Time
    requestedFrameTime = sentComponent.createIntegerSymbol(REQUESTED_FRAME_TIME, enablePausePulse)
    requestedFrameTime.setLabel("Requested Nominal Frame Time (us)")
    requestedFrameTime.setVisible(enablePausePulse.getValue())
    requestedFrameTime.setMin(int(getMinFrameTimeInUs(dataLength.getValue(), requestedTickTime.getValue())))
    requestedFrameTime.setMax(int(getMaxFrameTimeInUs(dataLength.getValue(), requestedTickTime.getValue())))
    requestedFrameTime.setDefaultValue(int(getMinFrameTimeInUs(dataLength.getValue(), requestedTickTime.getValue())))
    requestedFrameTime.setDependencies(updateRequestedFrameTime, [SENT_CON1__PPP , SENT_CON1__NIBCNT , REQUESTED_TICK_TIME])

    # Frame Time (SENTxCON3)
    frameTime = sentComponent.createHexSymbol(FRAME_TIME, None)
    frameTime.setLabel("Frame Time (us)")
    frameTimeValue = getFrameTime(requestedFrameTime.getValue(), requestedTickTime.getValue())
    frameTime.setDefaultValue(int(frameTimeValue, 16))
    frameTime.setVisible(False)
    frameTime.setDependencies(updateFrameTime, [REQUESTED_FRAME_TIME, REQUESTED_TICK_TIME, SENT_CON1__PPP ])
    frameTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sent_02359;register:SENTxCON3")

    # Calculated Frame Time
    calculatedFrameTime = sentComponent.createIntegerSymbol(CALCULATED_FRAME_TIME, enablePausePulse)
    calculatedFrameTime.setLabel("Calculated Nominal Frame Time (us)")
    frameTimeCalculated = int(getCalculatedFrameTime(frameTime.getValue(), requestedTickTime.getValue()))
    calculatedFrameTime.setDefaultValue(frameTimeCalculated)
    calculatedFrameTime.setVisible(False)
    calculatedFrameTime.setReadOnly(True)
    calculatedFrameTime.setDependencies(updateCalculatedFrameTime, [FRAME_TIME, REQUESTED_TICK_TIME, SENT_CON1__PPP])

    #Interrupt handling
    interruptEnable = sentComponent.createBooleanSymbol(INTERRUPT_MODE, messageSettings)
    interruptEnable.setLabel("Enable Interrupts")
    interruptEnable.setDefaultValue(True)

    pattern = r"^" + sentInstanceName.getValue() + r"(Interrupt)"
    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for interrupt in interruptsChildrenList:
        vIndex = int(interrupt.getAttribute("index"))
        vName = str(interrupt.getAttribute("name"))
        if re.search(pattern, vName):
            intVectorDataDictionary[vName] = vIndex

    for intIndex in intVectorDataDictionary.values():
            Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex), True)
            Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_HANDLER_LOCK".format(intIndex), True)

    patternSymbol = sentComponent.createStringSymbol("PATTERN_SYMBOL", None)
    patternSymbol.setLabel("Patterns for Interrupts")
    patternSymbol.setVisible(False)
    patternSymbol.setDependencies(updatePattern, [SENT_CON1__RCVEN, INTERRUPT_MODE])

    sentComment = sentComponent.createCommentSymbol("ENABLE_COMMENT", messageSettings)
    sentComment.setVisible(any(not bool(Database.getSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex))) for intIndex in intVectorDataDictionary.values()))
    sentComment.setLabel("Warning!!! Enable " + sentInstanceName.getValue() + " General and Error Interrupt in Interrupts Section of System module")
    sentComment.setDependencies(interruptStatusWarning, ["core.INTC_{}_ENABLE".format(intIndex) for intIndex in intVectorDataDictionary.values()])

    ######### Code Generation Symbols ###########

    moduleName = sentComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue(sentComponent.getID().upper())
    moduleName.setVisible(False)

    con1regPor = sentComponent.createStringSymbol("CON1_REG_POR", None)
    con1regPor.setDefaultValue(getRegisterDefaultValue(SENT, SENT, "CON1"))
    con1regPor.setVisible(False)

    con2regPor = sentComponent.createStringSymbol("CON2_REG_POR", None)
    con2regPor.setDefaultValue(getRegisterDefaultValue(SENT, SENT, "CON2"))
    con2regPor.setVisible(False)

    con3regPor = sentComponent.createStringSymbol("CON3_REG_POR", None)
    con3regPor.setDefaultValue(getRegisterDefaultValue(SENT, SENT, "CON3"))
    con3regPor.setVisible(False)

    ATDF_SENT_CON1__SPCEN = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="SENT"]/value-group@[name="SENT_CON1__SPCEN"]'
    )
    sentPWMData = getBitfieldData(ATDF_SENT_CON1__SPCEN)

    shortPWMCode = sentComponent.createKeyValueSetSymbol(SENT_CON1__SPCEN, None)
    shortPWMCode.setVisible(False)
    shortPWMCode.setLabel("Short PWM Code Bit")
    shortPWMCode.setOutputMode("Value")
    shortPWMCode.setDisplayMode("Description")
    for pwmItem in sentPWMData :
        shortPWMCode.addKey(pwmItem["key"], pwmItem["value"], pwmItem["desc"])
    customSetDefaultValue(shortPWMCode, SENT, SENT, "CON1", "SPCEN")

    ATDF_SENT_CON1__SIDL = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="SENT"]/value-group@[name="SENT_CON1__SIDL"]'
    )
    sentSidlData = getBitfieldData(ATDF_SENT_CON1__SIDL)

    sleepInIdle = sentComponent.createKeyValueSetSymbol(SENT_CON1__SIDL, None)
    sleepInIdle.setLabel("Stop in IDLE Mode Bit")
    sleepInIdle.setOutputMode("Value")
    sleepInIdle.setDisplayMode("Description")
    for sidlItem in sentSidlData:
        sleepInIdle.addKey(sidlItem["key"], sidlItem["value"], sidlItem["desc"])
    customSetDefaultValue(sleepInIdle, SENT, SENT, "CON1", "SIDL")
    sleepInIdle.setVisible(False)

    ATDF_SENT_CON1__ON = ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="SENT"]/value-group@[name="SENT_CON1__ON"]'
    )
    sentOnBitData = getBitfieldData(ATDF_SENT_CON1__ON)

    sentEnable = sentComponent.createKeyValueSetSymbol(SENT_CON1__ON, None)
    sentEnable.setVisible(False)
    sentEnable.setLabel("Enable Bit")
    sentEnable.setOutputMode("Value")
    sentEnable.setDisplayMode("Description")
    for onItem in sentOnBitData:
        sentEnable.addKey(onItem["key"], onItem["value"], onItem["desc"])
    customSetDefaultValue(sentEnable, SENT, SENT, "CON1", "ON")

    syncMin = sentComponent.createHexSymbol(SYNCMIN, None)
    syncMin.setLabel("Sync Minimum")
    syncMinValue = getMinSyncTime(tickPeriodCalculation.getValue(), clockFrequency.getValue())
    syncMin.setDefaultValue(int(syncMinValue, 16)) 
    syncMin.setVisible(False)
    syncMin.setDependencies(updateSyncMinTime, [CLOCK_FREQUENCY, CALCULATED_TICK_TIME])

    syncMax = sentComponent.createHexSymbol(SYNCMAX, None)
    syncMax.setLabel("Sync Maximum")
    syncMaxValue = getMaxSyncTime(tickPeriodCalculation.getValue(), clockFrequency.getValue())
    syncMax.setDefaultValue(int(syncMaxValue, 16))
    syncMax.setVisible(False)
    syncMax.setDependencies(updateSyncMaxTime, [CLOCK_FREQUENCY, CALCULATED_TICK_TIME])

    # File Handling  
      
    configName = Variables.get("__CONFIGURATION_NAME")
    
    transmitCommonHeaderFile = sentComponent.createFileSymbol("TRANSMIT_COMMON_HEADER", None)
    transmitCommonHeaderFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_tx_common.h")
    transmitCommonHeaderFile.setOutputName("plib_sent_tx_common.h")
    transmitCommonHeaderFile.setDestPath("peripheral/sent/sent_tx")
    transmitCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_tx")
    transmitCommonHeaderFile.setType("HEADER")
    transmitCommonHeaderFile.setMarkup(True)
    transmitCommonHeaderFile.setOverwrite(True)
    transmitCommonHeaderFile.setEnabled(transmissionType.getValue() == TRANSMITTER)
    transmitCommonHeaderFile.setDependencies(sentTransmitModeFileGeneration, [SENT_CON1__RCVEN])

    transmitHeaderFile = sentComponent.createFileSymbol("TRANSMIT_HEADER", None)
    transmitHeaderFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_tx.h.ftl")
    transmitHeaderFile.setOutputName("plib_sent"+sentInstance.getValue()+"_tx.h")
    transmitHeaderFile.setDestPath("/peripheral/sent/sent_tx")
    transmitHeaderFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_tx")
    transmitHeaderFile.setType("HEADER")
    transmitHeaderFile.setOverwrite(True)
    transmitHeaderFile.setMarkup(True)
    transmitHeaderFile.setEnabled(transmissionType.getValue() == TRANSMITTER)
    transmitHeaderFile.setDependencies(sentTransmitModeFileGeneration, [SENT_CON1__RCVEN])

    transmitSourceFile = sentComponent.createFileSymbol("TRANSMIT_SOURCE", None)
    transmitSourceFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_tx.c.ftl")
    transmitSourceFile.setOutputName("plib_sent"+sentInstance.getValue()+"_tx.c")
    transmitSourceFile.setDestPath("/peripheral/sent/sent_tx")
    transmitSourceFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_tx")
    transmitSourceFile.setType("SOURCE")
    transmitSourceFile.setOverwrite(True)
    transmitSourceFile.setMarkup(True)
    transmitSourceFile.setEnabled(transmissionType.getValue() == TRANSMITTER)
    transmitSourceFile.setDependencies(sentTransmitModeFileGeneration, [SENT_CON1__RCVEN])

    recieveCommonHeaderFile = sentComponent.createFileSymbol("RECIEVE_COMMON_HEADER", None)
    recieveCommonHeaderFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_rx_common.h")
    recieveCommonHeaderFile.setOutputName("plib_sent_rx_common.h")
    recieveCommonHeaderFile.setDestPath("peripheral/sent/sent_rx")
    recieveCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_rx")
    recieveCommonHeaderFile.setType("HEADER")
    recieveCommonHeaderFile.setMarkup(True)
    recieveCommonHeaderFile.setOverwrite(True)
    recieveCommonHeaderFile.setEnabled(transmissionType.getValue() == RECEIVER)
    recieveCommonHeaderFile.setDependencies(sentRecieveModeFileGeneration, [SENT_CON1__RCVEN])
   
    recieveHeaderFile = sentComponent.createFileSymbol("RECIEVE_HEADER", None)
    recieveHeaderFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_rx.h.ftl")
    recieveHeaderFile.setOutputName("plib_sent"+sentInstance.getValue()+"_rx.h")
    recieveHeaderFile.setDestPath("/peripheral/sent/sent_rx")
    recieveHeaderFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_rx")
    recieveHeaderFile.setType("HEADER")
    recieveHeaderFile.setOverwrite(True)
    recieveHeaderFile.setMarkup(True)
    recieveHeaderFile.setEnabled(transmissionType.getValue() == RECEIVER)
    recieveHeaderFile.setDependencies(sentRecieveModeFileGeneration, [SENT_CON1__RCVEN])

    recieveSourceFile = sentComponent.createFileSymbol("RECIEVE_SOURCE", None)
    recieveSourceFile.setSourcePath("../peripheral/sent_02359/templates/plib_sent_rx.c.ftl")
    recieveSourceFile.setOutputName("plib_sent"+sentInstance.getValue()+"_rx.c")
    recieveSourceFile.setDestPath("/peripheral/sent/sent_rx")
    recieveSourceFile.setProjectPath("config/" + configName + "/peripheral/sent/sent_rx")
    recieveSourceFile.setType("SOURCE")
    recieveSourceFile.setOverwrite(True)
    recieveSourceFile.setMarkup(True)
    recieveSourceFile.setEnabled(transmissionType.getValue() == RECEIVER)
    recieveSourceFile.setDependencies(sentRecieveModeFileGeneration, [SENT_CON1__RCVEN])
    
    sentSystemInitFile = sentComponent.createFileSymbol("SENT_INIT", None)
    sentSystemInitFile.setType("STRING")
    sentSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sentSystemInitFile.setSourcePath("../peripheral/sent_02359/templates/system/initialization.c.ftl")
    sentSystemInitFile.setMarkup(True)

    sentSystemDefFile = sentComponent.createFileSymbol("SENT_DEF", None)
    sentSystemDefFile.setType("STRING")
    sentSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sentSystemDefFile.setSourcePath("../peripheral/sent_02359/templates/system/definitions.h.ftl")
    sentSystemDefFile.setMarkup(True)