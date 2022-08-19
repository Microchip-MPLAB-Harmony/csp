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
modelist = ["Master", "Slave", "Master and Slave"]

global i2cInstanceName
global smbusProtocolEn
global i2cOperatingMode

timeoutScalingReg_RValues_20MHz_100KHz = {
"BUS_CLK_REG": 0x00006565,
"DATA_TIMING_REG": 0x0E54620A,
"RPT_START_HOLD_TIME":0x00000056,
"IDLE_SCALING_REG": 0x0280026C,
"TIMEOUT_SCALING_REG":0x306CF5FB,
}

timeoutScalingReg_RValues_20MHz_400KHz = {
"BUS_CLK_REG": 0x00001320,
"DATA_TIMING_REG": 0x0E151508,
"RPT_START_HOLD_TIME":0x0000000E,
"IDLE_SCALING_REG": 0x00140064,
"TIMEOUT_SCALING_REG":0x0D6CF5FB,
}

timeoutScalingReg_RValues_20MHz_1000KHz = {
"BUS_CLK_REG": 0x0000090A,
"DATA_TIMING_REG": 0x06080801,
"RPT_START_HOLD_TIME":0x00000009,
"IDLE_SCALING_REG": 0x00140064,
"TIMEOUT_SCALING_REG":0x066CF5FB,
}

timeoutScalingReg_RValues_16MHz_100KHz = {
"BUS_CLK_REG": 0x00004F4F,
"DATA_TIMING_REG": 0x0C4D5006,
"RPT_START_HOLD_TIME":0x0000004D,
"IDLE_SCALING_REG": 0x01FC01ED,
"TIMEOUT_SCALING_REG":0x4B9CC2C7,
}

timeoutScalingReg_RValues_16MHz_400KHz = {
"BUS_CLK_REG": 0x00000F17,
"DATA_TIMING_REG": 0x040A0A06,
"RPT_START_HOLD_TIME":0x0000000A,
"IDLE_SCALING_REG": 0x01000050,
"TIMEOUT_SCALING_REG":0x159CC2C7,
}

timeoutScalingReg_RValues_16MHz_1000KHz = {
"BUS_CLK_REG": 0x00000509,
"DATA_TIMING_REG": 0x04060601,
"RPT_START_HOLD_TIME":0x00000006,
"IDLE_SCALING_REG": 0x01000050,
"TIMEOUT_SCALING_REG":0x089CC2C7,
}

timeoutScalingReg_RValues_10MHz_100KHz = {
"BUS_CLK_REG": 0x00003131,
"DATA_TIMING_REG": 0x072A3104,
"RPT_START_HOLD_TIME":0x0000002B,
"IDLE_SCALING_REG": 0x01400136,
"TIMEOUT_SCALING_REG":0x30C6F5FB,
}

timeoutScalingReg_RValues_10MHz_400KHz = {
"BUS_CLK_REG": 0x00000A0D,
"DATA_TIMING_REG": 0x03080804,
"RPT_START_HOLD_TIME":0x00000007,
"IDLE_SCALING_REG": 0x00A00032,
"TIMEOUT_SCALING_REG":0x0DC6F5FB,
}

timeoutScalingReg_RValues_20MHz = {
"100KHZ_BUS_CLK":timeoutScalingReg_RValues_20MHz_100KHz,
"400KHZ_BUS_CLK":timeoutScalingReg_RValues_20MHz_400KHz,
"1000KHZ_BUS_CLK":timeoutScalingReg_RValues_20MHz_1000KHz,
}

timeoutScalingReg_RValues_16MHz = {
"100KHZ_BUS_CLK":timeoutScalingReg_RValues_16MHz_100KHz,
"400KHZ_BUS_CLK":timeoutScalingReg_RValues_16MHz_400KHz,
"1000KHZ_BUS_CLK":timeoutScalingReg_RValues_16MHz_1000KHz,
}

timeoutScalingReg_RValues_10MHz = {
"100KHZ_BUS_CLK":timeoutScalingReg_RValues_10MHz_100KHz,
"400KHZ_BUS_CLK":timeoutScalingReg_RValues_10MHz_400KHz,
"1000KHZ_BUS_CLK":None,
}

timeoutScalingReg_RecommendedValues = {
"20MHZ_BAUD_CLK":timeoutScalingReg_RValues_20MHz,
"16MHZ_BAUD_CLK":timeoutScalingReg_RValues_16MHz,
"10MHZ_BAUD_CLK":timeoutScalingReg_RValues_10MHz,
}

def handleMessage(messageID, args):
    global i2cOperatingMode

    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            i2cOperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            i2cOperatingMode.setValue(modelist[0])

    elif (messageID == "I2C_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            i2cOperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            i2cOperatingMode.setValue(modelist[1])

    return result_dict

def setI2CInterruptData(i2c_interrupt_name, status):

    Database.setSymbolValue("core", i2c_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", i2c_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", i2c_interrupt_name + "_INTERRUPT_HANDLER", i2c_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", i2c_interrupt_name + "_INTERRUPT_HANDLER", i2c_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateI2C(i2cInstanceNum, i2cInterruptType):
    interruptNameDir = "I2CSMB" + i2cInstanceNum
    interruptNameAgg = "I2CSMB" + i2cInstanceNum + "_GRP"

    if i2cInterruptType == "AGGREGATE":
        setI2CInterruptData(interruptNameDir, False)
        setI2CInterruptData(interruptNameAgg, True)
    else:
        setI2CInterruptData(interruptNameAgg, False)
        setI2CInterruptData(interruptNameDir, True)

def nvicInterruptUpdate(symbol, event):
    i2cInstanceNum = event["source"].getSymbolByID("I2C_INSTANCE_NUM").getValue()
    i2cInterruptType = event["source"].getSymbolByID("I2C_INTERRUPT_TYPE").getSelectedKey()
    i2cInterruptNameSym = event["source"].getSymbolByID("I2C_NVIC_INTERRUPT_NAME")

    nvicInterruptUpdateI2C(i2cInstanceNum, i2cInterruptType)
    if i2cInterruptType == "AGGREGATE":
        i2cInterruptNameSym.setValue("I2CSMB" + i2cInstanceNum + "_GRP")
    else:
        i2cInterruptNameSym.setValue("I2CSMB" + i2cInstanceNum)

# Calculates BRG value
def baudRateCalc(clk, baud):
    global i2cMaxBRG
    global i2cBaudErrorComment

    high_low_period = ((float(clk)/baud)/2.0) - 1
    max_baud_val = i2cMaxBRG.getValue()

    i2cBaudErrorComment.setVisible(False)

    if high_low_period > max_baud_val:
        high_low_period = max_baud_val
        i2cBaudErrorComment.setVisible(True)

    return int(high_low_period)

def baudRateTrigger(symbol, event):
    clk = event["source"].getSymbolByID("I2C_INPUT_CLOCK_FREQ").getValue()
    baud = event["source"].getSymbolByID("I2C_CLOCK_SPEED_HZ").getValue()
    busFreqValIndex = event["source"].getSymbolByID("BUS_FREQ_VAL_INDEX")

    brgVal = baudRateCalc(clk, baud)
    symbol.setValue(brgVal, 2)

    if baud < 250000:
        busFreqValIndex.setValue(0)
    elif baud < 750000:
        busFreqValIndex.setValue(1)
    else:
        busFreqValIndex.setValue(2)

def masterModeVisibility(symbol, event):
    opMode = event["value"]

    if opMode == "Master" or opMode == "Master and Slave":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def slaveModeVisibility(symbol, event):
    opMode = event["value"]

    if event["value"] == "Slave" or opMode == "Master and Slave":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def smbusProtocolUpdate (symbol, event):
    opMode = event["value"]
    if opMode == "Master and Slave":
        symbol.setReadOnly(True)
        symbol.setValue(True)
    else:
        symbol.setReadOnly(False)

def smbusLowLevelAPIGenUpdate (symbol, event):
    opMode = event["value"]
    symbol.setVisible(opMode == "Master and Slave")

def smbusPECUpdate (symbol, event):
    symbol.setVisible(event["value"])

def smbusTimingCheckEnUpdate (symbol, event):
    symbol.setVisible(event["value"])

def requestAndAssignDMAChannel(symbol, event):
    global i2cInstanceName

    dmaDev = ""
    dummyDict = {}
    assignDMAChannel = False
    symId = symbol.getID()
    opMode = event["source"].getSymbolByID("I2C_OPERATING_MODE").getValue()
    smbusEn = event["source"].getSymbolByID("I2C_SMBUS_PROTOCOL_EN").getValue()

    if event["id"] == "I2C_OPERATING_MODE":
        if symId == "I2C_SMBUS_MASTER_DMA_CHANNEL":
            if symbol.getValue() != -1:     #SMBUS master is currently assigned a DMA channel
                if opMode == "Slave":       #Let go the DMA host channel if new mode is "Slave"
                    dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "HOST"
                    Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})
                    symbol.setValue(-1)
                    symbol.setVisible(False)
            else:#SMBUS master is currently not assigned any DMA channel
                if smbusEn == True and (opMode == "Master" or opMode == "Master and Slave"):
                    dmaDev = "HOST"
                    assignDMAChannel = True
        else:
            if symbol.getValue() != -1:     #SMBUS slave is currently assigned a DMA channel
                if opMode == "Master":       #Let go the DMA Target channel if new mode is "Master"
                    dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "TARGET"
                    Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})
                    symbol.setValue(-1)
                    symbol.setVisible(False)
            else:#SMBUS slave is currently not assigned any DMA channel
                if smbusEn == True and (opMode == "Slave" or opMode == "Master and Slave"):
                    dmaDev = "TARGET"
                    assignDMAChannel = True
    else:
        if symId == "I2C_SMBUS_MASTER_DMA_CHANNEL":
            if symbol.getValue() == -1:#SMBUS master is currently not assigned any DMA channel
                if smbusEn == True:
                    if opMode == "Master" or opMode == "Master and Slave":
                        dmaDev = "HOST"
                        assignDMAChannel = True
            else:#SMBUS master is currently assigned a channel
                if smbusEn == False: #Let go the DMA host channel if SMBUS mode is disabled
                    dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "HOST"
                    Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})
                    symbol.setValue(-1)
                    symbol.setVisible(False)
        else:
            if symbol.getValue() == -1:#SMBUS slave is currently not assigned any DMA channel
                if smbusEn == True:
                    if opMode == "Slave" or opMode == "Master and Slave":
                        dmaDev = "TARGET"
                        assignDMAChannel = True
            else:#SMBUS slave is currently assigned a channel
                if smbusEn == False: #Let go the DMA Target channel if SMBUS mode is disabled
                    dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "TARGET"
                    Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})
                    symbol.setValue(-1)
                    symbol.setVisible(False)


    if assignDMAChannel == True:
        dmaChannelID = "DMA_CH_FOR_" + i2cInstanceName.getValue() + "_" + dmaDev
        dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + dmaDev
        symbol.setVisible(True)
        dummyDict = Database.sendMessage("core", "DMA_CHANNEL_ENABLE", {"dma_channel":dmaRequestID})
        channel = Database.getSymbolValue("core", dmaChannelID)
        symbol.setValue(channel)
        symbol.setVisible(True)

def smbMasterFilesGeneration(symbol, event):
    global smbusProtocolEn
    global i2cOperatingMode
    symbol.setEnabled((i2cOperatingMode.getValue() == "Master" or i2cOperatingMode.getValue() == "Master and Slave") and smbusProtocolEn.getValue() == True)

def smbSlaveFilesGeneration(symbol, event):
    global smbusProtocolEn
    global i2cOperatingMode
    symbol.setEnabled((i2cOperatingMode.getValue() == "Slave"  or i2cOperatingMode.getValue() == "Master and Slave") and smbusProtocolEn.getValue() == True)

def smbMasterSlaveFilesGeneration(symbol, event):
    global smbusProtocolEn
    global i2cOperatingMode
    symbol.setEnabled(i2cOperatingMode.getValue() == "Master and Slave" and smbusProtocolEn.getValue() == True)

def masterFilesGeneration(symbol, event):
    global smbusProtocolEn
    global i2cOperatingMode
    symbol.setEnabled(i2cOperatingMode.getValue() == "Master" and smbusProtocolEn.getValue() == False)

def slaveFilesGeneration(symbol, event):
    global smbusProtocolEn
    global i2cOperatingMode

    if symbol.getID() == "I2C_SLAVE_COMMON_HEADER":
        symbol.setEnabled(i2cOperatingMode.getValue() == "Slave" and smbusProtocolEn.getValue() == False)
    else:
        symbol.setEnabled(i2cOperatingMode.getValue() == "Slave" and smbusProtocolEn.getValue() == False)

def lowlevelFilesGeneration (symbol, event):
    global i2cOperatingMode
    symbol.setEnabled(i2cOperatingMode.getValue() == "Master and Slave" and event["value"] == True)

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

###################################################################################################
########################################## Component  #############################################
###################################################################################################
def destroyComponent(i2cComponent):
    global i2cInstanceName
    dummyDict = {}

    # Give up the DMA channel if allocated
    if i2cComponent.getSymbolValue("I2C_SMBUS_MASTER_DMA_CHANNEL") != -1:
        dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "HOST"
        dummyDict = Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})
    if i2cComponent.getSymbolValue("I2C_SMBUS_SLAVE_DMA_CHANNEL") != -1:
        dmaRequestID = "DMA_CH_NEEDED_FOR_" + i2cInstanceName.getValue() + "_" + "TARGET"
        dummyDict = Database.sendMessage("core", "DMA_CHANNEL_DISABLE", {"dma_channel":dmaRequestID})

def instantiateComponent(i2cComponent):

    global i2cInstanceName
    global i2cMaxBRG
    global i2cBaudErrorComment
    global i2cOperatingMode
    global smbusProtocolEn

    i2cInstanceName = i2cComponent.createStringSymbol("I2C_INSTANCE_NAME", None)
    i2cInstanceName.setVisible(False)
    i2cInstanceName.setDefaultValue(i2cComponent.getID().upper())

    i2cInstanceNum = i2cComponent.createStringSymbol("I2C_INSTANCE_NUM", None)
    i2cInstanceNum.setVisible(False)
    componentName = str(i2cComponent.getID())
    instanceNum = componentName[3]
    i2cInstanceNum.setDefaultValue(instanceNum)

    #Total SMBUS instances
    numSMBUSInstances = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="SMB"]').getChildren()
    i2cNumSMBUSInstances = i2cComponent.createIntegerSymbol("I2C_NUM_SMBUS_INSTANCES", None)
    i2cNumSMBUSInstances.setVisible(False)
    i2cNumSMBUSInstances.setDefaultValue(len(numSMBUSInstances))

    i2cOperatingMode = i2cComponent.createComboSymbol("I2C_OPERATING_MODE", None, modelist)
    i2cOperatingMode.setLabel("Operating Mode")
    i2cOperatingMode.setDefaultValue("Master")

    #SMBUS protocol enable
    smbusProtocolEn = i2cComponent.createBooleanSymbol("I2C_SMBUS_PROTOCOL_EN", None)
    smbusProtocolEn.setLabel("SMBUS Protocol Enable")
    smbusProtocolEn.setDefaultValue(False)
    smbusProtocolEn.setDependencies(smbusProtocolUpdate, ["I2C_OPERATING_MODE"])

    #Low level APIs only enable
    smbusLowLevelAPIGen = i2cComponent.createBooleanSymbol("I2C_SMBUS_LOW_LEVEL_API_ONLY", None)
    smbusLowLevelAPIGen.setLabel("Generate low-level APIs only")
    smbusLowLevelAPIGen.setVisible(False)
    smbusLowLevelAPIGen.setDefaultValue(False)
    smbusLowLevelAPIGen.setDependencies(smbusLowLevelAPIGenUpdate, ["I2C_OPERATING_MODE"])

    #SMBUS Error Check enable
    smbusPECEn = i2cComponent.createBooleanSymbol("I2C_SMBUS_PEC_ENABLE", None)
    smbusPECEn.setLabel("PEC Enable")
    smbusPECEn.setDefaultValue(False)
    smbusPECEn.setVisible(False)
    smbusPECEn.setDependencies(smbusPECUpdate, ["I2C_SMBUS_PROTOCOL_EN"])

    #SMBUS Timing Check enable
    smbusTimingCheckEn = i2cComponent.createBooleanSymbol("I2C_SMBUS_TIMING_CHK_ENABLE", None)
    smbusTimingCheckEn.setLabel("Timing Check Enable")
    smbusTimingCheckEn.setDefaultValue(False)
    smbusTimingCheckEn.setVisible(False)
    smbusTimingCheckEn.setDependencies(smbusTimingCheckEnUpdate, ["I2C_SMBUS_PROTOCOL_EN"])

    #Slave Address 1
    i2cSlaveADDR1 = i2cComponent.createHexSymbol("I2C_SLAVE_ADDDRESS_1", None)
    i2cSlaveADDR1.setLabel("I2C Slave Address 1 (7-bit)")
    i2cSlaveADDR1.setMax(128)
    i2cSlaveADDR1.setVisible(False)
    i2cSlaveADDR1.setDefaultValue(0x54)
    i2cSlaveADDR1.setDependencies(slaveModeVisibility, ["I2C_OPERATING_MODE"])

    #Slave Address 2
    i2cSlaveADDR2 = i2cComponent.createHexSymbol("I2C_SLAVE_ADDDRESS_2", None)
    i2cSlaveADDR2.setLabel("I2C Slave Address 2 (7-bit)")
    i2cSlaveADDR2.setMax(128)
    i2cSlaveADDR2.setVisible(False)
    i2cSlaveADDR2.setDefaultValue(0x55)
    i2cSlaveADDR2.setDependencies(slaveModeVisibility, ["I2C_OPERATING_MODE"])

    ##I2C Input Clock Frequency
    i2cInputClkFreq = i2cComponent.createIntegerSymbol("I2C_INPUT_CLOCK_FREQ", None)
    i2cInputClkFreq.setLabel("I2C Clock Frequency")
    i2cInputClkFreq.setReadOnly(True)
    i2cInputClkFreq.setDefaultValue(16000000)

    # Master DMA channel for SMBUS protocol
    smbusMasterDMAChannel = i2cComponent.createIntegerSymbol("I2C_SMBUS_MASTER_DMA_CHANNEL", None)
    smbusMasterDMAChannel.setLabel("DMA Channel For SMBUS Master")
    smbusMasterDMAChannel.setDefaultValue(-1)
    smbusMasterDMAChannel.setVisible(False)
    smbusMasterDMAChannel.setReadOnly(True)
    smbusMasterDMAChannel.setDependencies(requestAndAssignDMAChannel, ["I2C_SMBUS_PROTOCOL_EN", "I2C_OPERATING_MODE"])

    # Slave DMA channel for SMBUS protocol
    smbusSlaveDMAChannel = i2cComponent.createIntegerSymbol("I2C_SMBUS_SLAVE_DMA_CHANNEL", None)
    smbusSlaveDMAChannel.setLabel("DMA Channel For SMBUS Slave")
    smbusSlaveDMAChannel.setDefaultValue(-1)
    smbusSlaveDMAChannel.setVisible(False)
    smbusSlaveDMAChannel.setReadOnly(True)
    smbusSlaveDMAChannel.setDependencies(requestAndAssignDMAChannel, ["I2C_SMBUS_PROTOCOL_EN", "I2C_OPERATING_MODE"])

    #Baud Rate (Hz)
    i2cBAUD_HZ = i2cComponent.createIntegerSymbol("I2C_CLOCK_SPEED_HZ", None)
    i2cBAUD_HZ.setLabel("I2C Baud Rate (Hz)")
    i2cBAUD_HZ.setMin(1)
    i2cBAUD_HZ.setMax(1000000)
    i2cBAUD_HZ.setDefaultValue(400000)
    i2cBAUD_HZ.setDependencies(masterModeVisibility, ["I2C_OPERATING_MODE"])

    #I2C Baud Rate not supported comment
    i2cBaudErrorComment = i2cComponent.createCommentSymbol("I2C_BAUD_ERROR_COMMENT", None)
    i2cBaudErrorComment.setLabel("********** WARNING!: Baud Rate is out of range **********")
    i2cBaudErrorComment.setVisible(False)

    #Read Max Baud from ATDF
    i2cxBRG_Bitfield = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMB"]/register-group@[name="SMB"]/register@[name="' + "BUSCLK" + '"]/bitfield@[name="LOW_PER"]')

    i2cMaxBRG = i2cComponent.createIntegerSymbol("I2C_MAX_BRG", None)
    i2cMaxBRG.setDefaultValue(int(str(i2cxBRG_Bitfield.getAttribute("mask")), 0))
    i2cMaxBRG.setVisible(False)

    ## Baud Rate
    i2cBRGValue = i2cComponent.createIntegerSymbol("BRG_VALUE", None)
    i2cBRGValue.setVisible(False)
    i2cBRGValue.setDefaultValue(baudRateCalc(i2cInputClkFreq.getValue(), i2cBAUD_HZ.getValue()))
    i2cBRGValue.setDependencies(baudRateTrigger, ["I2C_CLOCK_SPEED_HZ"])

    # Index into the array of recommended values to use for timing related registers
    i2cBusFreqIndex = i2cComponent.createIntegerSymbol("BUS_FREQ_VAL_INDEX", None)
    i2cBusFreqIndex.setDefaultValue(1)
    i2cBusFreqIndex.setVisible(False)

    ## Interrupt Setup
    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "I2CSMB" + i2cInstanceNum.getValue()})

    # Interrupt type selection
    i2cInterruptType = i2cComponent.createKeyValueSetSymbol("I2C_INTERRUPT_TYPE", None)
    i2cInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        i2cInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        i2cInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    i2cInterruptType.setDefaultValue(0)
    i2cInterruptType.setDisplayMode("Description")
    i2cInterruptType.setOutputMode("Key")

    # Trigger dependency when interrupt type changes
    i2cNVICUpdate = i2cComponent.createBooleanSymbol("I2C_UPDATE_NVIC_INTERRUPT", None)
    i2cNVICUpdate.setVisible(False)
    i2cNVICUpdate.setDependencies(nvicInterruptUpdate, ["I2C_INTERRUPT_TYPE"])

    # Set NVIC interrupt default value
    nvicInterruptUpdateI2C(i2cInstanceNum.getValue(), i2cInterruptType.getValue())

    i2cPortSel = i2cComponent.createKeyValueSetSymbol("I2C_PORT_SEL", None)
    i2cPortSel.setLabel("Port Select")

    i2cSignalNodeValues = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="SMB"]/instance@[name="' + i2cInstanceName.getValue()+'"]/signals').getChildren()
    if i2cSignalNodeValues != None:
        for index in range(len(i2cSignalNodeValues)):
            if i2cSignalNodeValues[index].getAttribute("group") == "SCL":
                port_index = i2cSignalNodeValues[index].getAttribute("index")
                key = "I2C" + port_index
                i2cPortSel.addKey(key, port_index, key)
    i2cPortSel.setOutputMode("Value")
    i2cPortSel.setDisplayMode("Description")

    interruptName = ""
    if i2cInterruptType.getSelectedKey() == "AGGREGATE":
        interruptName = "I2CSMB" + i2cInstanceNum.getValue() + "_GRP"
    else:
        interruptName = "I2CSMB" + i2cInstanceNum.getValue()
    i2c_NVIC_InterruptName = i2cComponent.createStringSymbol("I2C_NVIC_INTERRUPT_NAME", None)
    i2c_NVIC_InterruptName.setDefaultValue(interruptName)
    i2c_NVIC_InterruptName.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    ###################################################################################################
    ####################################### Driver Symbols ############################################
    ###################################################################################################

    #I2C API Prefix
    i2cAPIPrefix = i2cComponent.createStringSymbol("I2C_PLIB_API_PREFIX", None)
    i2cAPIPrefix.setDefaultValue(i2cInstanceName.getValue())
    i2cAPIPrefix.setVisible(False)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    i2cSMBMasterHeaderFile = i2cComponent.createFileSymbol("I2C_SMB_MASTER_HEADER", None)
    i2cSMBMasterHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_master.h.ftl")
    i2cSMBMasterHeaderFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_master.h")
    i2cSMBMasterHeaderFile.setDestPath("peripheral/i2c/master")
    i2cSMBMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/master")
    i2cSMBMasterHeaderFile.setType("HEADER")
    i2cSMBMasterHeaderFile.setMarkup(True)
    i2cSMBMasterHeaderFile.setEnabled(False)
    i2cSMBMasterHeaderFile.setDependencies(smbMasterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBMasterCommonHeaderFile = i2cComponent.createFileSymbol("I2C_SMB_MASTER_COMMON_HEADER", None)
    i2cSMBMasterCommonHeaderFile.setSourcePath("../peripheral/smb_31/plib_i2c_smbus_master_common.h")
    i2cSMBMasterCommonHeaderFile.setOutputName("plib_smb_master_common.h")
    i2cSMBMasterCommonHeaderFile.setDestPath("peripheral/i2c/master")
    i2cSMBMasterCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/master")
    i2cSMBMasterCommonHeaderFile.setType("HEADER")
    i2cSMBMasterCommonHeaderFile.setEnabled(False)
    i2cSMBMasterCommonHeaderFile.setDependencies(smbMasterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBMasterSourceFile = i2cComponent.createFileSymbol("I2C_SMB_MASTER_SOURCE", None)
    i2cSMBMasterSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_master.c.ftl")
    i2cSMBMasterSourceFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_master.c")
    i2cSMBMasterSourceFile.setDestPath("peripheral/i2c/master")
    i2cSMBMasterSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c/master")
    i2cSMBMasterSourceFile.setType("SOURCE")
    i2cSMBMasterSourceFile.setMarkup(True)
    i2cSMBMasterSourceFile.setEnabled(False)
    i2cSMBMasterSourceFile.setDependencies(smbMasterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBSlaveHeaderFile = i2cComponent.createFileSymbol("I2C_SMB_SLAVE_HEADER", None)
    i2cSMBSlaveHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_slave.h.ftl")
    i2cSMBSlaveHeaderFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_slave.h")
    i2cSMBSlaveHeaderFile.setDestPath("peripheral/i2c/slave")
    i2cSMBSlaveHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/slave")
    i2cSMBSlaveHeaderFile.setType("HEADER")
    i2cSMBSlaveHeaderFile.setMarkup(True)
    i2cSMBSlaveHeaderFile.setEnabled(False)
    i2cSMBSlaveHeaderFile.setDependencies(smbSlaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBSlaveCommonHeaderFile = i2cComponent.createFileSymbol("I2C_SMB_SLAVE_COMMON_HEADER", None)
    i2cSMBSlaveCommonHeaderFile.setSourcePath("../peripheral/smb_31/plib_i2c_smbus_slave_common.h")
    i2cSMBSlaveCommonHeaderFile.setOutputName("plib_smb_slave_common.h")
    i2cSMBSlaveCommonHeaderFile.setDestPath("peripheral/i2c/slave")
    i2cSMBSlaveCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/slave")
    i2cSMBSlaveCommonHeaderFile.setType("HEADER")
    i2cSMBSlaveCommonHeaderFile.setEnabled(False)
    i2cSMBSlaveCommonHeaderFile.setDependencies(smbSlaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBSlaveSourceFile = i2cComponent.createFileSymbol("I2C_SMB_SLAVE_SOURCE", None)
    i2cSMBSlaveSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_slave.c.ftl")
    i2cSMBSlaveSourceFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_slave.c")
    i2cSMBSlaveSourceFile.setDestPath("peripheral/i2c/slave")
    i2cSMBSlaveSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c/slave")
    i2cSMBSlaveSourceFile.setType("SOURCE")
    i2cSMBSlaveSourceFile.setMarkup(True)
    i2cSMBSlaveSourceFile.setEnabled(False)
    i2cSMBSlaveSourceFile.setDependencies(smbSlaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBMasterSlaveCommonSourceFile = i2cComponent.createFileSymbol("I2C_SMB_MASTER_SLAVE_COMMON_SOURCE", None)
    i2cSMBMasterSlaveCommonSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_master_slave_common.c.ftl")
    i2cSMBMasterSlaveCommonSourceFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_master_slave_common.c")
    i2cSMBMasterSlaveCommonSourceFile.setDestPath("peripheral/i2c")
    i2cSMBMasterSlaveCommonSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c")
    i2cSMBMasterSlaveCommonSourceFile.setType("SOURCE")
    i2cSMBMasterSlaveCommonSourceFile.setMarkup(True)
    i2cSMBMasterSlaveCommonSourceFile.setEnabled(False)
    i2cSMBMasterSlaveCommonSourceFile.setDependencies(smbMasterSlaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSMBMasterSlaveCommonHeaderFile = i2cComponent.createFileSymbol("I2C_SMB_MASTER_SLAVE_COMMON_HEADER", None)
    i2cSMBMasterSlaveCommonHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_master_slave_common.h.ftl")
    i2cSMBMasterSlaveCommonHeaderFile.setOutputName("plib_" + i2cInstanceName.getValue().lower() + "_master_slave_common.h")
    i2cSMBMasterSlaveCommonHeaderFile.setDestPath("peripheral/i2c")
    i2cSMBMasterSlaveCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c")
    i2cSMBMasterSlaveCommonHeaderFile.setType("HEADER")
    i2cSMBMasterSlaveCommonHeaderFile.setMarkup(True)
    i2cSMBMasterSlaveCommonHeaderFile.setEnabled(False)
    i2cSMBMasterSlaveCommonHeaderFile.setDependencies(smbMasterSlaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    ######

    i2cMasterHeaderFile = i2cComponent.createFileSymbol("I2C_MASTER_HEADER", None)
    i2cMasterHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_master.h.ftl")
    i2cMasterHeaderFile.setOutputName("plib_i2c" + i2cInstanceNum.getValue() + "_master.h")
    i2cMasterHeaderFile.setDestPath("peripheral/i2c/master")
    i2cMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/master")
    i2cMasterHeaderFile.setType("HEADER")
    i2cMasterHeaderFile.setMarkup(True)
    i2cMasterHeaderFile.setEnabled(True)
    i2cMasterHeaderFile.setDependencies(masterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cMasterCommonHeaderFile = i2cComponent.createFileSymbol("I2C_MASTER_COMMON_HEADER", None)
    i2cMasterCommonHeaderFile.setSourcePath("../peripheral/smb_31/plib_i2c_master_common.h")
    i2cMasterCommonHeaderFile.setOutputName("plib_i2c_master_common.h")
    i2cMasterCommonHeaderFile.setDestPath("peripheral/i2c/master")
    i2cMasterCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/master")
    i2cMasterCommonHeaderFile.setType("HEADER")
    i2cMasterCommonHeaderFile.setEnabled(True)
    i2cMasterCommonHeaderFile.setDependencies(masterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cMasterSourceFile = i2cComponent.createFileSymbol("I2C_MASTER_SOURCE", None)
    i2cMasterSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_master.c.ftl")
    i2cMasterSourceFile.setOutputName("plib_i2c" + i2cInstanceNum.getValue() + "_master.c")
    i2cMasterSourceFile.setDestPath("peripheral/i2c/master")
    i2cMasterSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c/master")
    i2cMasterSourceFile.setType("SOURCE")
    i2cMasterSourceFile.setMarkup(True)
    i2cMasterSourceFile.setEnabled(True)
    i2cMasterSourceFile.setDependencies(masterFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSlaveHeaderFile = i2cComponent.createFileSymbol("I2C_SLAVE_HEADER", None)
    i2cSlaveHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_slave.h.ftl")
    i2cSlaveHeaderFile.setOutputName("plib_i2c" + i2cInstanceNum.getValue() + "_slave.h")
    i2cSlaveHeaderFile.setDestPath("peripheral/i2c/slave")
    i2cSlaveHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/slave")
    i2cSlaveHeaderFile.setType("HEADER")
    i2cSlaveHeaderFile.setMarkup(True)
    i2cSlaveHeaderFile.setEnabled(False)
    i2cSlaveHeaderFile.setDependencies(slaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSlaveCommonHeaderFile = i2cComponent.createFileSymbol("I2C_SLAVE_COMMON_HEADER", None)
    i2cSlaveCommonHeaderFile.setSourcePath("../peripheral/smb_31/plib_i2c_slave_common.h")
    i2cSlaveCommonHeaderFile.setOutputName("plib_i2c_slave_common.h")
    i2cSlaveCommonHeaderFile.setDestPath("peripheral/i2c/slave")
    i2cSlaveCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c/slave")
    i2cSlaveCommonHeaderFile.setType("HEADER")
    i2cSlaveCommonHeaderFile.setEnabled(False)
    i2cSlaveCommonHeaderFile.setDependencies(slaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    i2cSlaveSourceFile = i2cComponent.createFileSymbol("I2C_SLAVE_SOURCE", None)
    i2cSlaveSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_slave.c.ftl")
    i2cSlaveSourceFile.setOutputName("plib_i2c" + i2cInstanceNum.getValue() + "_slave.c")
    i2cSlaveSourceFile.setDestPath("peripheral/i2c/slave")
    i2cSlaveSourceFile.setProjectPath("config/" + configName +"/peripheral/i2c/slave")
    i2cSlaveSourceFile.setType("SOURCE")
    i2cSlaveSourceFile.setMarkup(True)
    i2cSlaveSourceFile.setEnabled(False)
    i2cSlaveSourceFile.setDependencies(slaveFilesGeneration, ["I2C_OPERATING_MODE", "I2C_SMBUS_PROTOCOL_EN"])

    ####

    i2cLowLevelSourceFile = i2cComponent.createFileSymbol("I2C_SLAVE_LOWLEVEL_SOURCE", None)
    i2cLowLevelSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_lowlevel_intf.c")
    i2cLowLevelSourceFile.setOutputName("plib_i2c_smbus_lowlevel_intf.c")
    i2cLowLevelSourceFile.setDestPath("peripheral/i2c")
    i2cLowLevelSourceFile.setProjectPath("config/" + configName + "/peripheral/i2c")
    i2cLowLevelSourceFile.setType("SOURCE")
    i2cLowLevelSourceFile.setEnabled(False)
    i2cLowLevelSourceFile.setDependencies(lowlevelFilesGeneration, ["I2C_SMBUS_LOW_LEVEL_API_ONLY"])

    i2cLowLevelHeaderFile = i2cComponent.createFileSymbol("I2C_SLAVE_LOWLEVEL_HEADER", None)
    i2cLowLevelHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_lowlevel_intf.h.ftl")
    i2cLowLevelHeaderFile.setOutputName("plib_i2c_smbus_lowlevel_intf.h")
    i2cLowLevelHeaderFile.setDestPath("peripheral/i2c")
    i2cLowLevelHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c")
    i2cLowLevelHeaderFile.setType("HEADER")
    i2cLowLevelHeaderFile.setMarkup(True)
    i2cLowLevelHeaderFile.setEnabled(False)
    i2cLowLevelHeaderFile.setDependencies(lowlevelFilesGeneration, ["I2C_SMBUS_LOW_LEVEL_API_ONLY"])

    i2cCommonSourceFile = i2cComponent.createFileSymbol("I2C_COMMON_SOURCE", None)
    i2cCommonSourceFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_common.c.ftl")
    i2cCommonSourceFile.setOutputName("plib_i2c_smb_common.c")
    i2cCommonSourceFile.setDestPath("peripheral/i2c")
    i2cCommonSourceFile.setProjectPath("config/" + configName + "/peripheral/i2c")
    i2cCommonSourceFile.setType("SOURCE")
    i2cCommonSourceFile.setMarkup(True)
    i2cCommonSourceFile.setEnabled(True)

    i2cCommonHeaderFile = i2cComponent.createFileSymbol("I2C_COMMON_HEADER", None)
    i2cCommonHeaderFile.setSourcePath("../peripheral/smb_31/templates/plib_i2c_smbus_common.h")
    i2cCommonHeaderFile.setOutputName("plib_i2c_smb_common.h")
    i2cCommonHeaderFile.setDestPath("peripheral/i2c")
    i2cCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/i2c")
    i2cCommonHeaderFile.setType("HEADER")
    i2cCommonHeaderFile.setEnabled(True)

    ####

    i2cSystemInitFile = i2cComponent.createFileSymbol("I2C_INIT", None)
    i2cSystemInitFile.setType("STRING")
    i2cSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    i2cSystemInitFile.setSourcePath("../peripheral/smb_31/templates/system/initialization.c.ftl")
    i2cSystemInitFile.setMarkup(True)

    i2cSystemDefFile = i2cComponent.createFileSymbol("I2C_DEF", None)
    i2cSystemDefFile.setType("STRING")
    i2cSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    i2cSystemDefFile.setSourcePath("../peripheral/smb_31/templates/system/definitions.h.ftl")
    i2cSystemDefFile.setMarkup(True)
