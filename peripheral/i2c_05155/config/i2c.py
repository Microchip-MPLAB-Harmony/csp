import re

HOST = "Host"
CLIENT = "Client"
NANO_SECONDS = 1e-9
SEVEN_BIT_MASK = 127
TEN_BIT_MASK = 1023
MIN_BRG = 4
I2C_INSTANCE_NAME = "moduleName"
OPERATING_MODE = "I2C_OPERATING_MODE"
CLOCK_FREQUENCY = "I2C_CLOCK_FREQUENCY"
BAUD_RATE = "I2C_BAUD_RATE"
REQUESTED_SPEED = "I2C_CLOCK_SPEED"
ENABLE_10BIT_ADDRESS = "ENABLE_10BIT_ADDRESS"
CORE_COMPONENT = "core"
STANDARD_SPEED_CLOCK_FREQ = "stdSpeedClkFreq"
FSCL_SPEEDS = [100000,400000,1000000]
MODULE_NAME = "I2C"

intVectorDataDictionary = {}

def handleMessage(messageID, args):
    global operatingMode

    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            operatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            operatingMode.setValue(HOST)

    elif (messageID == "I2C_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            operatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            operatingMode.setValue(CLIENT)

    return result_dict

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def hostModeVisibility(symbol, event):
    symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == HOST)

def clientModeVisibility(symbol, event):
    symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == CLIENT)

def enableTenBitAddressCallback(symbol, event):
    if event["id"] == ENABLE_10BIT_ADDRESS:
        if symbol.getComponent().getSymbolValue(ENABLE_10BIT_ADDRESS) == True:
            symbol.setLabel("Client Address(10-bit)")
            symbol.setMax(TEN_BIT_MASK)
        else:
            symbol.setLabel("Client Address(7-bit)")
            symbol.setMax(SEVEN_BIT_MASK)
    else:
        symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == CLIENT)

def enableTenBitMaskCallback(symbol, event):
    if event["id"] == ENABLE_10BIT_ADDRESS:
        if symbol.getComponent().getSymbolValue(ENABLE_10BIT_ADDRESS) == True:
            symbol.setLabel("Client Mask(10-bit)")
            symbol.setMax(TEN_BIT_MASK)
        else:
            symbol.setLabel("Client Mask(7-bit)")
            symbol.setMax(SEVEN_BIT_MASK)
    else:
        symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == CLIENT)

def setSysClkFreq(symbol, event):
    if event["id"] == OPERATING_MODE:
        symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == HOST)
    else:
        symbol.setValue(int(Database.getSymbolValue(CORE_COMPONENT, STANDARD_SPEED_CLOCK_FREQ)))

def getBRGValue(clk, baud, i2cInstanceName):
    # BRG = (((1/(2 * baud))-Delay) * clk) - 3
    if baud == 0:
        return MIN_BRG

    delay = int(ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="I2C"]/instance@[name="' + i2cInstanceName+ '"]/parameters/param@[name="pulseGobblerDelay"]').getAttribute("value")) * NANO_SECONDS

    brgValue = (((1.0 / (2.0 * baud)) - delay) * clk) - 3.0
    return max(MIN_BRG,int(brgValue))

def baudRateTrigger(symbol, event):
    i2cInstanceName = symbol.getComponent().getSymbolValue(I2C_INSTANCE_NAME)
    clk = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
    baud = int(symbol.getComponent().getSymbolValue(REQUESTED_SPEED))
    brgVal = getBRGValue(clk, baud, i2cInstanceName)
    symbol.setValue(brgVal)

def getCalcSpeed(clk, brg, i2cInstanceName):
    if clk == 0:
        return 0
    delay = int(ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="I2C"]/instance@[name="' + i2cInstanceName+ '"]/parameters/param@[name="pulseGobblerDelay"]').getAttribute("value")) * NANO_SECONDS
    calcSpeed = round(1 / (2.0 * ((brg + 3.0) / clk + delay)))
    return int(calcSpeed)

def calcSpeedTrigger(symbol, event):
    if event["id"] == OPERATING_MODE:
        symbol.setVisible(symbol.getComponent().getSymbolValue(OPERATING_MODE) == HOST)
    else:
        i2cInstanceName = symbol.getComponent().getSymbolValue(I2C_INSTANCE_NAME)
        clk = symbol.getComponent().getSymbolValue(CLOCK_FREQUENCY)
        reqSpeed = int(symbol.getComponent().getSymbolValue(REQUESTED_SPEED))
        brgVal = getBRGValue(clk, reqSpeed, i2cInstanceName)
        calcSpeed = getCalcSpeed(clk,brgVal, i2cInstanceName)
        symbol.setValue(calcSpeed)

def interruptStatusWarning(symbol, event):
    i2cInstanceName = symbol.getComponent().getSymbolValue(I2C_INSTANCE_NAME)
    intIndex = intVectorDataDictionary[i2cInstanceName+'Interrupt']
    intEIndex = intVectorDataDictionary.get(i2cInstanceName + 'EInterrupt')
    if Database.getSymbolValue(CORE_COMPONENT,"INTC_{}_ENABLE".format(intIndex)) == False or Database.getSymbolValue(CORE_COMPONENT,"INTC_{}_ENABLE".format(intEIndex)) == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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

def getMaskValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return int(bitMask,16)
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

def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield):
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            symbolKey = valueGroupEntry
            optionList = getBitfieldOptionList(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, None )
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp

def hostFilesGeneration(symbol, event):
    symbol.setEnabled(symbol.getComponent().getSymbolValue(OPERATING_MODE) == HOST)

def clientFilesGeneration(symbol, event):
    symbol.setEnabled(symbol.getComponent().getSymbolValue(OPERATING_MODE) == CLIENT)

def instantiateComponent(i2cComponent):

    i2cInstanceName = i2cComponent.createStringSymbol(I2C_INSTANCE_NAME, None)
    i2cInstanceName.setVisible(False)
    i2cInstanceName.setDefaultValue(i2cComponent.getID().upper())

    i2cInstanceNum = i2cComponent.createStringSymbol("instance", None)
    i2cInstanceNum.setVisible(False)
    i2cInstanceNum.setDefaultValue(str(i2cComponent.getID()[-1]))

    i2cAlternatePinsComment = i2cComponent.createCommentSymbol("alternatePinsComment",None)
    i2cAlternatePinsComment.setLabel("Note: To use alternate pins, enable ALTI2C config bits in System/Device_Configuration/FDEVOPT and set the ALTI2C pins.")

    i2cInterruptMode = i2cComponent.createBooleanSymbol("I2CInterruptMode",None)
    i2cInterruptMode.setLabel("Interrupt Mode")
    i2cInterruptMode.setReadOnly(True)
    i2cInterruptMode.setDefaultValue(True)
    i2cInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:intc_04436;register:IFS2")

    # Operating Mode
    global operatingMode
    operatingMode = i2cComponent.createComboSymbol(OPERATING_MODE, None, [HOST,CLIENT])
    operatingMode.setLabel("Operating Mode")
    operatingMode.setDefaultValue(HOST)

    # Clock Source
    clockSource = i2cComponent.createStringSymbol("CLOCK_SOURCE", None)
    clockSource.setLabel("Clock Source")
    clockSource.setDefaultValue("Standard Speed Peripheral Clock")
    clockSource.setReadOnly(True)
    clockSource.setDependencies(hostModeVisibility, [OPERATING_MODE])

    # Clock Frequency
    clockFrequency = i2cComponent.createIntegerSymbol(CLOCK_FREQUENCY, None)
    clockFrequency.setLabel("Clock Frequency(Hz)")
    clockFrequency.setDefaultValue(int(Database.getSymbolValue(CORE_COMPONENT, STANDARD_SPEED_CLOCK_FREQ) or 0))
    clockFrequency.setReadOnly(True)
    clockFrequency.setDependencies(setSysClkFreq,[CORE_COMPONENT+"."+STANDARD_SPEED_CLOCK_FREQ,OPERATING_MODE])

    # Baud Rate
    reqSpeed = i2cComponent.createIntegerSymbol(REQUESTED_SPEED, None)
    reqSpeed.setLabel("Requested Speed(Hz)")
    reqSpeed.setDefaultValue(FSCL_SPEEDS[0])
    reqSpeed.setMax(getMaskValue(MODULE_NAME, "I2C","HBRG","I2CHBRG"))
    reqSpeed.setMin(0)
    reqSpeed.setDependencies(hostModeVisibility, [OPERATING_MODE])
    reqSpeed.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxHBRG")

    # Calculated Speed
    calcSpeed = i2cComponent.createLongSymbol("CALCULATED_SPEED", None)
    calcSpeed.setLabel("Calculated Speed(Hz)")
    calcSpeed.setReadOnly(True)
    brgVal = getBRGValue(clockFrequency.getValue(), int(reqSpeed.getValue()), i2cInstanceName.getValue())
    calcSpeed.setDefaultValue(getCalcSpeed(clockFrequency.getValue(), brgVal, i2cInstanceName.getValue()))
    calcSpeed.setDependencies(calcSpeedTrigger,[CLOCK_FREQUENCY, REQUESTED_SPEED, OPERATING_MODE])
    calcSpeed.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxHBRG")

    # Calculated BRG Value
    calculatedBRGValue = i2cComponent.createHexSymbol("brgValueInHex", None)
    calculatedBRGValue.setLabel("Calculated BRG Value")
    calculatedBRGValue.setDefaultValue(brgVal)
    calculatedBRGValue.setVisible(False)
    calculatedBRGValue.setDependencies(baudRateTrigger,[CLOCK_FREQUENCY,REQUESTED_SPEED])

    # clock stretching
    enableClockStretching = i2cComponent.createBooleanSymbol("ENABLE_CLOCK_STRETCHING", None)
    enableClockStretching.setLabel("Enable Clock Stretching")
    enableClockStretching.setDefaultValue(False)
    enableClockStretching.setVisible(False)
    enableClockStretching.setDependencies(clientModeVisibility,[OPERATING_MODE])
    enableClockStretching.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # 10-bit addressing
    enableTenBitAddress = i2cComponent.createBooleanSymbol("ENABLE_10BIT_ADDRESS", None)
    enableTenBitAddress.setLabel("Enable 10-bit Addressing")
    enableTenBitAddress.setDefaultValue(False)
    enableTenBitAddress.setVisible(False)
    enableTenBitAddress.setDependencies(clientModeVisibility,[OPERATING_MODE])
    enableTenBitAddress.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # Client Address
    clientAddress = i2cComponent.createHexSymbol("CLIENT_ADDDRESS", None)
    clientAddress.setLabel("Client Address(7-bit)")
    clientAddress.setMin(0)
    clientAddress.setMax(SEVEN_BIT_MASK)
    clientAddress.setVisible(False)
    clientAddress.setDefaultValue(0x0)
    clientAddress.setDependencies(enableTenBitAddressCallback,[OPERATING_MODE,"ENABLE_10BIT_ADDRESS"])
    clientAddress.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxADD")

    # Client Mask
    clientMask = i2cComponent.createHexSymbol("CLIENT_MASK", None)
    clientMask.setLabel("Client Mask(7-bit)")
    clientMask.setMin(0)
    clientMask.setMax(SEVEN_BIT_MASK)
    clientMask.setVisible(False)
    clientMask.setDefaultValue(0x0)
    clientMask.setDependencies(enableTenBitMaskCallback,[OPERATING_MODE,"ENABLE_10BIT_ADDRESS"])
    clientMask.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxMSK")

    # Slew Rate Control
    slewRateControl = createKeyValueSetSymbol(i2cComponent, MODULE_NAME, "I2C","CON1","DISSLW")
    slewRateControl.setLabel("Disable Slew Rate Control")
    slewRateControl.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # SMBus Input Levels bit
    smBusInputLevels = createKeyValueSetSymbol(i2cComponent, MODULE_NAME, "I2C","CON1","SMBEN")
    smBusInputLevels.setLabel("SMBus Input Levels")
    smBusInputLevels.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # Stop in Idle Mode bit
    sdaHoldTime = createKeyValueSetSymbol(i2cComponent, MODULE_NAME, "I2C","CON1","SDAHT")
    sdaHoldTime.setLabel("SDA Hold Time")
    sdaHoldTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    forceWriteComment = i2cComponent.createCommentSymbol("FORCE_WRITE_COMMENT", None)
    forceWriteComment.setLabel("Force Write I2C Function (Ignore NACK from Client)")
    forceWriteComment.setDependencies(hostModeVisibility, [OPERATING_MODE])

    # Force Write
    forceWrite = i2cComponent.createBooleanSymbol("I2C_INCLUDE_FORCED_WRITE", None)
    forceWrite.setLabel("Include Force Write")
    forceWrite.setDefaultValue(False)
    forceWrite.setVisible(True)
    forceWrite.setDependencies(hostModeVisibility, [OPERATING_MODE])

    # AHEN (Address Hold Enable Bit)
    settingBitAHEN = getBitField(MODULE_NAME,"I2C","CON1","AHEN")
    if settingBitAHEN != None:
        enableAddHold = i2cComponent.createBooleanSymbol("I2CS_AHEN_SUPPORT", None)
        enableAddHold.setLabel("Enable Address Hold")
        enableAddHold.setVisible(False)
        enableAddHold.setDefaultValue(False)
        enableAddHold.setDependencies(clientModeVisibility,[OPERATING_MODE])
        enableAddHold.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # DHEN (Data Hold Enable Bit)
    settingBitDHEN = getBitField(MODULE_NAME,"I2C","CON1","DHEN")
    if settingBitDHEN != None:
        enableDataHold = i2cComponent.createBooleanSymbol("I2CS_DHEN_SUPPORT", None)
        enableDataHold.setLabel("Enable Data Hold")
        enableDataHold.setVisible(False)
        enableDataHold.setDefaultValue(False)
        enableDataHold.setDependencies(clientModeVisibility,[OPERATING_MODE])
        enableDataHold.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:i2c_05155;register:I2CxCON1")

    # Setup and Rise Time
    setupAndRiseTime = i2cComponent.createKeyValueSetSymbol("SETUP_RISE_TIME", None)
    setupAndRiseTime.setLabel("Setup and Rise Time")
    setupAndRiseTime.addKey("0", "0" , "100 kHz - Setup time 250ns, Rise time 1000ns")
    setupAndRiseTime.addKey("1", "1" , "400 kHz - Setup time 100ns, Rise time 300ns")
    setupAndRiseTime.addKey("2", "2" , "1000 kHz - Setup time 50ns, Rise time 120ns")
    setupAndRiseTime.setDisplayMode("Description")
    setupAndRiseTime.setDefaultValue(0)
    setupAndRiseTime.setVisible(False)
    setupAndRiseTime.setDependencies(clientModeVisibility,[OPERATING_MODE])

    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
    for interrupt in range (0, len(interruptsChildrenList)):
        vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
        vName = str(interruptsChildrenList[interrupt].getAttribute("name"))
        pattern = r"^" + i2cInstanceName.getValue() + r"(EInterrupt|Interrupt)"
        if re.search(pattern, vName):
            intVectorDataDictionary[vName] = vIndex

    for intIndex in intVectorDataDictionary.values():
        Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex), True)
        Database.setSymbolValue(CORE_COMPONENT, "INTC_{}_HANDLER_LOCK".format(intIndex), True)

    intComment = i2cComponent.createCommentSymbol("ENABLE_COMMENT", None)
    intComment.setVisible(all(not bool(Database.getSymbolValue(CORE_COMPONENT, "INTC_{}_ENABLE".format(intIndex))) for intIndex in intVectorDataDictionary.values()))
    intComment.setLabel("Warning!!! Enable " + i2cInstanceName.getValue() + " General and Error Interrupt in Interrupts Section of System module")
    intComment.setDependencies(interruptStatusWarning, ["core." + "INTC_" + str(intIndex) + "_ENABLE" for intIndex in intVectorDataDictionary.values()])

    #Driver Symbol Start
    #I2C API Prefix
    i2cSym_API_Prefix = i2cComponent.createStringSymbol("I2C_PLIB_API_PREFIX", None)
    i2cSym_API_Prefix.setDefaultValue(i2cInstanceName.getValue())
    i2cSym_API_Prefix.setVisible(False)
    #Driver Symbol End

    ######################## Code Generation ##################################

    configName = Variables.get("__CONFIGURATION_NAME")

    i2cHostHeaderFile = i2cComponent.createFileSymbol("I2C_HOST_HEADER", None)
    i2cHostHeaderFile.setSourcePath("../peripheral/i2c_05155/templates/host/plib_i2c_host.h.ftl")
    i2cHostHeaderFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_host.h")
    i2cHostHeaderFile.setDestPath("peripheral/i2c/host")
    i2cHostHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/host")
    i2cHostHeaderFile.setType("HEADER")
    i2cHostHeaderFile.setMarkup(True)
    i2cHostHeaderFile.setEnabled(True)
    i2cHostHeaderFile.setDependencies(hostFilesGeneration, [OPERATING_MODE])

    i2cHostCommonHeaderFile = i2cComponent.createFileSymbol("I2C_HOST_COMMON_HEADER", None)
    i2cHostCommonHeaderFile.setSourcePath("../peripheral/i2c_05155/templates/host/plib_i2c_host_common.h.ftl")
    i2cHostCommonHeaderFile.setOutputName("plib_i2c_host_common.h")
    i2cHostCommonHeaderFile.setDestPath("peripheral/i2c/host")
    i2cHostCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/host")
    i2cHostCommonHeaderFile.setType("HEADER")
    i2cHostCommonHeaderFile.setEnabled(True)
    i2cHostCommonHeaderFile.setDependencies(hostFilesGeneration, [OPERATING_MODE])

    i2cHostSourceFile = i2cComponent.createFileSymbol("I2C_HOST_SOURCE", None)
    i2cHostSourceFile.setSourcePath("../peripheral/i2c_05155/templates/host/plib_i2c_host.c.ftl")
    i2cHostSourceFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_host.c")
    i2cHostSourceFile.setDestPath("peripheral/i2c/host")
    i2cHostSourceFile.setProjectPath("config/" + configName + "/peripheral/i2c/host")
    i2cHostSourceFile.setType("SOURCE")
    i2cHostSourceFile.setMarkup(True)
    i2cHostSourceFile.setEnabled(True)
    i2cHostSourceFile.setDependencies(hostFilesGeneration, [OPERATING_MODE])

    i2cClientHeaderFile = i2cComponent.createFileSymbol("I2C_CLIENT_HEADER", None)
    i2cClientHeaderFile.setSourcePath("../peripheral/i2c_05155/templates/client/plib_i2c_client.h.ftl")
    i2cClientHeaderFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_client.h")
    i2cClientHeaderFile.setDestPath("peripheral/i2c/client")
    i2cClientHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/client")
    i2cClientHeaderFile.setType("HEADER")
    i2cClientHeaderFile.setMarkup(True)
    i2cClientHeaderFile.setEnabled(False)
    i2cClientHeaderFile.setDependencies(clientFilesGeneration, [OPERATING_MODE])

    i2cClientCommonHeaderFile = i2cComponent.createFileSymbol("I2C_CLIENT_COMMON_HEADER", None)
    i2cClientCommonHeaderFile.setSourcePath("../peripheral/i2c_05155/templates/client/plib_i2c_client_common.h.ftl")
    i2cClientCommonHeaderFile.setOutputName("plib_i2c_client_common.h")
    i2cClientCommonHeaderFile.setDestPath("peripheral/i2c/client")
    i2cClientCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/client")
    i2cClientCommonHeaderFile.setType("HEADER")
    i2cClientCommonHeaderFile.setEnabled(False)
    i2cClientCommonHeaderFile.setDependencies(clientFilesGeneration, [OPERATING_MODE])

    i2cClientSourceFile = i2cComponent.createFileSymbol("I2C_CLIENT_SOURCE", None)
    i2cClientSourceFile.setSourcePath("../peripheral/i2c_05155/templates/client/plib_i2c_client.c.ftl")
    i2cClientSourceFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_client.c")
    i2cClientSourceFile.setDestPath("peripheral/i2c/client")
    i2cClientSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c/client")
    i2cClientSourceFile.setType("SOURCE")
    i2cClientSourceFile.setMarkup(True)
    i2cClientSourceFile.setEnabled(False)
    i2cClientSourceFile.setDependencies(clientFilesGeneration, [OPERATING_MODE])

    i2cSystemInitFile = i2cComponent.createFileSymbol("I2C_INIT", None)
    i2cSystemInitFile.setType("STRING")
    i2cSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    i2cSystemInitFile.setSourcePath("../peripheral/i2c_05155/templates/system/initialization.c.ftl")
    i2cSystemInitFile.setMarkup(True)

    i2cSystemDefFile = i2cComponent.createFileSymbol("I2C_DEF", None)
    i2cSystemDefFile.setType("STRING")
    i2cSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    i2cSystemDefFile.setSourcePath("../peripheral/i2c_05155/templates/system/definitions.h.ftl")
    i2cSystemDefFile.setMarkup(True)

    errorInterruptSymbol = i2cComponent.createStringSymbol("i2cErrorInterruptHandler", None)
    errorInterruptSymbol.setDefaultValue(MODULE_NAME+i2cInstanceNum.getValue()+"E_InterruptHandler")
    errorInterruptSymbol.setVisible(False)

    commonInterruptSymbol = i2cComponent.createStringSymbol("i2cCommonInterruptHandler", None)
    commonInterruptSymbol.setDefaultValue(MODULE_NAME+i2cInstanceNum.getValue()+"_InterruptHandler")
    commonInterruptSymbol.setVisible(False)