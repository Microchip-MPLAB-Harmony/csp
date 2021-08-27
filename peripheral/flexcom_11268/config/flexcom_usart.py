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

global dataBitsDict
global flexcomSym_BaudRatePerErrorComment
global calcBaud

dataBitsDict = {
    "5_BIT": "DRV_USART_DATA_5_BIT",
    "6_BIT": "DRV_USART_DATA_6_BIT",
    "7_BIT": "DRV_USART_DATA_7_BIT",
    "8_BIT": "DRV_USART_DATA_8_BIT",
    "9_BIT": "DRV_USART_DATA_9_BIT"
}

################################################################################
#### Business Logic ####
################################################################################
def updateRingBufferSizeVisibleProperty(symbol, event):
    global flexcomSym_RingBuffer_Mode

    symbol.setVisible(flexcomSym_OperatingMode.getSelectedKey() == "USART" and flexcomSym_RingBuffer_Mode.getValue() == True)

# FLEXCOM USART clock source
clock_source = {"Ext_clk_src_Freq" : 1000000}
global baudRateCalc

def calcBaud(clk, baudrate, over_samp):
    CD = 0,
    FP = 0,
    BaudError = 0

    CD = int((clk / (baudrate * 8 * (2 - over_samp))))

    if CD > 0:
        FP = int(((clk / (baudrate * (2 - over_samp))) - CD * 8))
        ActualBaudRate = (clk / (CD * 8 + FP)) / (2 - over_samp)
        BaudError = ((ActualBaudRate - baudrate)/float(baudrate)) * 100

    return CD, FP, BaudError

# Calculates BRG value and Oversampling
def baudRateCalc(clk, baudrate):

    global calcBaud
    global flexcomSym_BaudRatePerErrorComment

    CD0 = 0
    CD1 = 0
    FP0 = 0
    FP1 = 0
    BaudError0 = 0
    BaudError1 = 0
    OVSAMP = 0

    # Calculate CD and FP for 8x and 16x oversampling:
    CD0, FP0, BaudError0 = calcBaud(clk, baudrate, 0)
    CD1, FP1, BaudError1 = calcBaud(clk, baudrate, 1)

    if ( (not(CD0 > 0 and CD0 <= 65535) ) and (not(CD1 > 0 and CD1 <= 65535)) ):
        # Baudrate cannot be generated either with 8x or 16x oversampling
        return 0, 0, 0

    # If baudrate can be generated with both 8x and 16x oversampling, then choose the one that gives less error:
    if (CD0 > 0 and CD0 <= 65535) and (CD1 > 0 and CD1 <= 65535):
        if BaudError1 < BaudError0:
            CD0 = CD1
            FP0 = FP1
            BaudError0 = BaudError1
            OVSAMP = 1
    else:
        if (CD1 > 0 and CD1 <= 65535):
            CD0 = CD1
            FP0 = FP1
            BaudError0 = BaudError1
            OVSAMP = 1

    if flexcomSym_UsartMode.getSelectedKey() == "IRDA" and BaudError0 > 1.87:
        flexcomSym_BaudRatePerErrorComment.setLabel("Baud rate error is " + "{:.3f}".format(BaudError0) + " %." " Maximum allowable error in IRDA mode is +/- 1.87%.  ")
        flexcomSym_BaudRatePerErrorComment.setVisible(True)
    else:
        flexcomSym_BaudRatePerErrorComment.setVisible(False)

    return int(CD0), int(FP0), OVSAMP

def baudRateTrigger(symbol, event):
    if flexcomSym_OperatingMode.getSelectedKey() == "USART":
        if Database.getSymbolValue(deviceNamespace, "FLEXCOM_USART_MR_USCLKS") == 0x3:
            clk = Database.getSymbolValue(deviceNamespace, "EXTERNAL_CLOCK_FREQ")
        else:
            clk = Database.getSymbolValue(deviceNamespace, "FLEX_USART_CLOCK_FREQ")
        baud = Database.getSymbolValue(deviceNamespace, "BAUD_RATE")

        cd, fp, oversamp = baudRateCalc(clk, baud)

        if symbol.getID() == "BRG_VALUE":
            symbol.setValue(cd, 2)
        if symbol.getID() == "FLEXCOM_USART_MR_OVER":
            symbol.setValue(oversamp, 2)
        if symbol.getID() == "FP_VALUE":
            symbol.setValue(fp, 2)

def clockSourceFreq(symbol, event):
    if (event["id"] == "FLEXCOM_USART_MR_USCLKS" or (event["id"] == flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")):
        symbol.setValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)
    if (event["id"] == "FLEXCOM_MODE"):
        if flexcomSym_OperatingMode.getSelectedKey() == "USART":
            symbol.setVisible(True)
        else :
            symbol.setVisible(False)
    elif event["id"] == "FLEXCOM_USART_MR_USCLKS":
        if event["value"] == 0x3:
            symbol.setVisible(False)
        else :
            symbol.setVisible(True)

def irdaFilterVal(symbol, event):
    peripheralClkFreq = int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    # t_peripheralClock * (IRDA_FILTER + 3) < 1.41 1us
    # Subtracting 4 instead of 3, as filterVal must be less than 1.41 us
    filterVal = (int)((1.41e-6)*(peripheralClkFreq) - 4)
    symbol.setValue(filterVal)

def irdaBaudErrorCalculate(symbol, event):
    if flexcomSym_OperatingMode.getSelectedKey() == "USART" and flexcomSym_UsartMode.getSelectedKey() == "IRDA":
        if Database.getSymbolValue(deviceNamespace, "FLEXCOM_USART_MR_USCLKS") == 0x3:
            clk = Database.getSymbolValue(deviceNamespace, "EXTERNAL_CLOCK_FREQ")
        else:
            clk = Database.getSymbolValue(deviceNamespace, "FLEX_USART_CLOCK_FREQ")
        baud = Database.getSymbolValue(deviceNamespace, "BAUD_RATE")

        baudRateCalc(clk, baud)
    else:
        symbol.setVisible(False)

def dataWidthLogic(symbol, event):
    if(event["value"] == 4):
        symbol.setValue(True, 2)
    else:
        symbol.setValue(False, 2)

def ExternalClkSymbolVisible(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def symbolVisible(symbol, event):
    if flexcomSym_OperatingMode.getSelectedKey() == "USART":
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def fifoOptionsVisible(symbol, event):
   fifoEnable = event["source"].getSymbolByID("FLEXCOM_USART_FIFO_ENABLE").getValue()
   symbol.setVisible(flexcomSym_OperatingMode.getSelectedKey() == "USART" and fifoEnable == True)

def rxFifo2OptionVisible(symbol, event):
    uartMode = event["source"].getSymbolByID("FLEXCOM_USART_MR_USART_MODE").getSelectedKey()

    symbol.setVisible(flexcomSym_OperatingMode.getSelectedKey() == "USART" and uartMode == "HW_HANDSHAKING")

def updateUSARTDataBits (symbol, event):

    dataBits = event["symbol"].getSelectedKey()
    symbol.setValue(dataBitsDict[dataBits])

def updateInterruptMode (symbol, event):
    print "updateInterruptMode - " + str(event["value"])
    if symbol.getLabel() != "---":
        print "entered"
        if event["value"] == True and event["source"].getSymbolByID("FLEXCOM_USART_OPERATING_MODE").getSelectedKey() != "RING_BUFFER" :
            event["source"].getSymbolByID("FLEXCOM_USART_OPERATING_MODE").setSelectedKey("NON_BLOCKING")
        elif event["value"] == False:
            event["source"].getSymbolByID("FLEXCOM_USART_OPERATING_MODE").setSelectedKey("BLOCKING")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateRingBufferMode (symbol, event):
    print "updateRingBufferMode - " + str(event["value"])
    if symbol.getLabel() != "---":
        print "entered"
        if event["value"] == True:
            event["source"].getSymbolByID("FLEXCOM_USART_OPERATING_MODE").setSelectedKey("RING_BUFFER")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateOperatingMode (symbol, event):
    if event["id"] == "FLEXCOM_USART_OPERATING_MODE":

        interruptModeSym = event["source"].getSymbolByID("FLEXCOM_USART_INTERRUPT_MODE_ENABLE")
        ringBufferModeSym = event["source"].getSymbolByID("FLEXCOM_USART_RING_BUFFER_MODE_ENABLE")
        fifoModeSym = event["source"].getSymbolByID("FLEXCOM_USART_FIFO_ENABLE")

        if symbol.getSelectedKey() == "BLOCKING" or symbol.getSelectedKey() == "BLOCKING_FIFO":
            interruptModeSym.setValue(False)
            ringBufferModeSym.setValue(False)
            fifoModeSym.setValue(symbol.getSelectedKey() == "BLOCKING_FIFO")
        elif symbol.getSelectedKey() == "NON_BLOCKING" or symbol.getSelectedKey() == "NON_BLOCKING_FIFO":
            interruptModeSym.setValue(True)
            ringBufferModeSym.setValue(False)
            fifoModeSym.setValue(symbol.getSelectedKey() == "NON_BLOCKING_FIFO")
        elif symbol.getSelectedKey() == "RING_BUFFER" or symbol.getSelectedKey() == "RING_BUFFER_FIFO":
            interruptModeSym.setValue(True)
            ringBufferModeSym.setValue(True)
            fifoModeSym.setValue(symbol.getSelectedKey() == "RING_BUFFER_FIFO")
    else:
        symbol.setVisible(flexcomSym_OperatingMode.getSelectedKey() == "USART")

def updateHWHandshakingComment (symbol, event):
    nonFifoOperatingMode = False
    flexcomMode = flexcomSym_OperatingMode.getSelectedKey()
    mode = flexcomSym_UsartMode.getSelectedKey()
    if "FIFO" not in flexcomSym_UsartOperatingMode.getSelectedKey():
        nonFifoOperatingMode = True
    symbol.setVisible(flexcomMode == "USART" and mode == "HW_HANDSHAKING" and nonFifoOperatingMode == True)
###################################################################################################
############################################ FLEXCOM USART ########################################
###################################################################################################
global flexcomSym_BaudRatePerErrorComment
global flexcomSym_UsartMode
global flexcomSym_UsartOperatingMode
global flexcomSym_RingBuffer_Mode

# Depricated symbols ---------------------------------------------------------------------------------------------------

#Interrupt/Non-Interrupt Mode
flexcomSym_UsartInterrupt = flexcomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", flexcomSym_OperatingMode)
flexcomSym_UsartInterrupt.setLabel("Interrupt Mode")
flexcomSym_UsartInterrupt.setDefaultValue(True)
flexcomSym_UsartInterrupt.setVisible(False)
flexcomSym_UsartInterrupt.setReadOnly(True)
flexcomSym_UsartInterrupt.setDependencies(updateInterruptMode, ["USART_INTERRUPT_MODE"])

#Enable Ring buffer?
flexcomSym_RingBuffer_Enable = flexcomComponent.createBooleanSymbol("USART_RING_BUFFER_ENABLE", flexcomSym_OperatingMode)
flexcomSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
flexcomSym_RingBuffer_Enable.setDefaultValue(False)
flexcomSym_RingBuffer_Enable.setVisible(False)
flexcomSym_RingBuffer_Enable.setReadOnly(True)
flexcomSym_RingBuffer_Enable.setDependencies(updateRingBufferMode, ["USART_RING_BUFFER_ENABLE"])

# Depricated symbols ---------------------------------------------------------------------------------------------------

flexcomUSARTFIFONode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"FLEXCOM\"]/instance@[name=\"FLEXCOM0\"]/parameters/param@[name=\"USART_FIFO_SIZE\"]")
flexcomUSARTFIFOSize = int(flexcomUSARTFIFONode.getAttribute('value'),10)

flexcomSym_UsartFIFOSize = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_FIFO_SIZE", flexcomSym_OperatingMode)
flexcomSym_UsartFIFOSize.setDefaultValue(flexcomUSARTFIFOSize)
flexcomSym_UsartFIFOSize.setVisible(False)

#Interrupt/Non-Interrupt Mode
flexcomSym_UsartIntMode = flexcomComponent.createBooleanSymbol("FLEXCOM_USART_INTERRUPT_MODE_ENABLE", flexcomSym_OperatingMode)
flexcomSym_UsartIntMode.setLabel("Enable Interrupts ?")
flexcomSym_UsartIntMode.setDefaultValue(True)
flexcomSym_UsartIntMode.setVisible(False)
flexcomSym_UsartIntMode.setReadOnly(True)

#Enable Ring buffer?
flexcomSym_RingBuffer_Mode = flexcomComponent.createBooleanSymbol("FLEXCOM_USART_RING_BUFFER_MODE_ENABLE", flexcomSym_OperatingMode)
flexcomSym_RingBuffer_Mode.setLabel("Enable Ring Buffer ?")
flexcomSym_RingBuffer_Mode.setDefaultValue(False)
flexcomSym_RingBuffer_Mode.setVisible(False)
flexcomSym_RingBuffer_Mode.setReadOnly(True)

flexcomSym_UsartMode = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_USART_MR_USART_MODE", flexcomSym_OperatingMode)
flexcomSym_UsartMode.setLabel("Mode")
flexcomSym_USART_MODE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_US_MR__USART_MODE\"]")
flexcomSym_UsartMode_Values = []
flexcomSym_UsartMode_Values = flexcomSym_USART_MODE_Node.getChildren()
for index in range(len(flexcomSym_UsartMode_Values)):
    flexcomSym_UsartMode_Key_Name = flexcomSym_UsartMode_Values[index].getAttribute("name")
    flexcomSym_UsartMode_Key_Value = flexcomSym_UsartMode_Values[index].getAttribute("value")
    flexcomSym_UsartMode_Key_Description = flexcomSym_UsartMode_Values[index].getAttribute("caption")
    if flexcomSym_UsartMode_Key_Name == "NORMAL" or flexcomSym_UsartMode_Key_Name == "RS485" or flexcomSym_UsartMode_Key_Name == "HW_HANDSHAKING" or flexcomSym_UsartMode_Key_Name == "IRDA":
        flexcomSym_UsartMode.addKey(flexcomSym_UsartMode_Key_Name, flexcomSym_UsartMode_Key_Value, flexcomSym_UsartMode_Key_Description)
flexcomSym_UsartMode.setDisplayMode("Key")
flexcomSym_UsartMode.setOutputMode("Key")
flexcomSym_UsartMode.setDefaultValue(0)
flexcomSym_UsartMode.setVisible(False)
flexcomSym_UsartMode.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_UsartOperatingMode = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_USART_OPERATING_MODE", flexcomSym_OperatingMode)
flexcomSym_UsartOperatingMode.setLabel("Operating Mode")
flexcomSym_UsartOperatingMode.addKey("BLOCKING", "0", "Blocking mode")
flexcomSym_UsartOperatingMode.addKey("BLOCKING_FIFO", "1", "Blocking mode with FIFO")
flexcomSym_UsartOperatingMode.addKey("NON_BLOCKING", "2", "Non-blocking mode")
flexcomSym_UsartOperatingMode.addKey("NON_BLOCKING_FIFO", "3", "Non-blocking mode with FIFO")
flexcomSym_UsartOperatingMode.addKey("RING_BUFFER", "4", "Ring buffer mode")
flexcomSym_UsartOperatingMode.addKey("RING_BUFFER_FIFO", "5", "Ring buffer mode with FIFO")
flexcomSym_UsartOperatingMode.setDefaultValue(2)
flexcomSym_UsartOperatingMode.setDisplayMode("Description")
flexcomSym_UsartOperatingMode.setOutputMode("Key")
flexcomSym_UsartOperatingMode.setVisible(flexcomSym_OperatingMode.getSelectedKey() == "USART")
flexcomSym_UsartOperatingMode.setDependencies(updateOperatingMode, ["FLEXCOM_MODE",  "FLEXCOM_USART_OPERATING_MODE"])

flexcomSym_UsartHwHandshakingComment = flexcomComponent.createCommentSymbol("FLEXCOM_USART_HW_HANDSHAKING_COMMENT", flexcomSym_OperatingMode)
flexcomSym_UsartHwHandshakingComment.setLabel("!!! Note: For hardware handshaking, select hardware FIFO based Operating Mode !!!")
flexcomSym_UsartHwHandshakingComment.setVisible(False)
flexcomSym_UsartHwHandshakingComment.setDependencies(updateHWHandshakingComment, ["FLEXCOM_MODE", "FLEXCOM_USART_MR_USART_MODE", "FLEXCOM_USART_OPERATING_MODE"])

flexcomSym_UsartRingBufferSizeConfig = flexcomComponent.createCommentSymbol("FLEXCOM_USART_RING_BUFFER_SIZE_CONFIG", flexcomSym_OperatingMode)
flexcomSym_UsartRingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
flexcomSym_UsartRingBufferSizeConfig.setVisible(False)
flexcomSym_UsartRingBufferSizeConfig.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "FLEXCOM_USART_RING_BUFFER_MODE_ENABLE"])

flexcomSym_TXRingBuffer_Size = flexcomComponent.createIntegerSymbol("USART_TX_RING_BUFFER_SIZE", flexcomSym_UsartRingBufferSizeConfig)
flexcomSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
flexcomSym_TXRingBuffer_Size.setMin(2)
flexcomSym_TXRingBuffer_Size.setMax(65535)
flexcomSym_TXRingBuffer_Size.setDefaultValue(128)
flexcomSym_TXRingBuffer_Size.setVisible(False)
flexcomSym_TXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "FLEXCOM_USART_RING_BUFFER_MODE_ENABLE"])

flexcomSym_RXRingBuffer_Size = flexcomComponent.createIntegerSymbol("USART_RX_RING_BUFFER_SIZE", flexcomSym_UsartRingBufferSizeConfig)
flexcomSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
flexcomSym_RXRingBuffer_Size.setMin(2)
flexcomSym_RXRingBuffer_Size.setMax(65535)
flexcomSym_RXRingBuffer_Size.setDefaultValue(128)
flexcomSym_RXRingBuffer_Size.setVisible(False)
flexcomSym_RXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["FLEXCOM_MODE", "FLEXCOM_USART_RING_BUFFER_MODE_ENABLE"])

flexcomSym_UsartFIFOEnable = flexcomComponent.createBooleanSymbol("FLEXCOM_USART_FIFO_ENABLE", flexcomSym_OperatingMode)
flexcomSym_UsartFIFOEnable.setLabel("Enable FIFO")
flexcomSym_UsartFIFOEnable.setDefaultValue(False)
flexcomSym_UsartFIFOEnable.setVisible(False)

flexcomSym_UsartFIFOThresholdsConfig = flexcomComponent.createCommentSymbol("FLEXCOM_USART_FIFO_THRESHOLD_CONFIG", flexcomSym_OperatingMode)
flexcomSym_UsartFIFOThresholdsConfig.setLabel("Config FIFO Thresholds-")
flexcomSym_UsartFIFOThresholdsConfig.setVisible(False)
flexcomSym_UsartFIFOThresholdsConfig.setDependencies(fifoOptionsVisible, ["FLEXCOM_MODE", "FLEXCOM_USART_FIFO_ENABLE"])

flexcomSym_UsartFIFORXThreshold = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_RX_FIFO_THRESHOLD", flexcomSym_UsartFIFOThresholdsConfig)
flexcomSym_UsartFIFORXThreshold.setLabel("RX FIFO Threshold")
flexcomSym_UsartFIFORXThreshold.setMin(1)
flexcomSym_UsartFIFORXThreshold.setMax(flexcomUSARTFIFOSize)
flexcomSym_UsartFIFORXThreshold.setDefaultValue(flexcomUSARTFIFOSize/2)
flexcomSym_UsartFIFORXThreshold.setVisible(False)
flexcomSym_UsartFIFORXThreshold.setDependencies(fifoOptionsVisible, ["FLEXCOM_MODE", "FLEXCOM_USART_FIFO_ENABLE"])

flexcomSym_UsartFIFOTXThreshold = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_TX_FIFO_THRESHOLD", flexcomSym_UsartFIFOThresholdsConfig)
flexcomSym_UsartFIFOTXThreshold.setLabel("TX FIFO Threshold")
flexcomSym_UsartFIFOTXThreshold.setMin(0)
flexcomSym_UsartFIFOTXThreshold.setMax(flexcomUSARTFIFOSize-1)
flexcomSym_UsartFIFOTXThreshold.setDefaultValue(flexcomUSARTFIFOSize/2)
flexcomSym_UsartFIFOTXThreshold.setVisible(False)
flexcomSym_UsartFIFOTXThreshold.setDependencies(fifoOptionsVisible, ["FLEXCOM_MODE", "FLEXCOM_USART_FIFO_ENABLE"])

flexcomSym_UsartFIFORX2Threshold = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_RX_FIFO_THRESHOLD_2", flexcomSym_UsartFIFOThresholdsConfig)
flexcomSym_UsartFIFORX2Threshold.setLabel("RX FIFO Threshold 2")
flexcomSym_UsartFIFORX2Threshold.setMin(1)
flexcomSym_UsartFIFORX2Threshold.setMax(flexcomUSARTFIFOSize)
flexcomSym_UsartFIFORX2Threshold.setDefaultValue(flexcomUSARTFIFOSize/2)
flexcomSym_UsartFIFORX2Threshold.setVisible(False)
flexcomSym_UsartFIFORX2Threshold.setDependencies(rxFifo2OptionVisible, ["FLEXCOM_MODE", "FLEXCOM_USART_MR_USART_MODE"])

flexcomSym_TimeGuardValue = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_TTGR", flexcomSym_OperatingMode)
flexcomSym_TimeGuardValue.setLabel("Time Guard Value")
flexcomSym_TimeGuardValue.setDefaultValue(0)
flexcomSym_TimeGuardValue.setMin(0)
flexcomSym_TimeGuardValue.setMax(255)
flexcomSym_TimeGuardValue.setVisible(False)
flexcomSym_TimeGuardValue.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_UsartClkSrc = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_USART_MR_USCLKS", flexcomSym_OperatingMode)
flexcomSym_UsartClkSrc.setLabel("Select Clock Source")
flexcomSym_UsartClkSrc_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_US_MR__USCLKS\"]")
flexcomSym_UsartClkSrc_Values = []
flexcomSym_UsartClkSrc_Values = flexcomSym_UsartClkSrc_Node.getChildren()
for index in range(len(flexcomSym_UsartClkSrc_Values)):
    flexcomSym_UsartClkSrc_Key_Name = flexcomSym_UsartClkSrc_Values[index].getAttribute("name")
    flexcomSym_UsartClkSrc_Key_Value = flexcomSym_UsartClkSrc_Values[index].getAttribute("value")
    flexcomSym_UsartClkSrc_Key_Description = flexcomSym_UsartClkSrc_Values[index].getAttribute("caption")
    flexcomSym_UsartClkSrc.addKey(flexcomSym_UsartClkSrc_Key_Name, flexcomSym_UsartClkSrc_Key_Value, flexcomSym_UsartClkSrc_Key_Description)
flexcomSym_UsartClkSrc.setDisplayMode("Key")
flexcomSym_UsartClkSrc.setOutputMode("Key")
flexcomSym_UsartClkSrc.setDefaultValue(0)
flexcomSym_UsartClkSrc.setVisible(False)
flexcomSym_UsartClkSrc.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_UsartExternalClkValue = flexcomComponent.createIntegerSymbol("EXTERNAL_CLOCK_FREQ", flexcomSym_UsartClkSrc)
flexcomSym_UsartExternalClkValue.setLabel("External Clock Source")
flexcomSym_UsartExternalClkValue.setDefaultValue(clock_source.get("Ext_clk_src_Freq"))
flexcomSym_UsartExternalClkValue.setMin(1)
flexcomSym_UsartExternalClkValue.setMax(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY") / 3))
flexcomSym_UsartExternalClkValue.setVisible(False)
flexcomSym_UsartExternalClkValue.setDependencies(ExternalClkSymbolVisible, ["FLEXCOM_USART_MR_USCLKS"])

flexcomSym_UsartClkValue = flexcomComponent.createIntegerSymbol("FLEX_USART_CLOCK_FREQ", flexcomSym_OperatingMode)
flexcomSym_UsartClkValue.setLabel("Clock Source Value")
flexcomSym_UsartClkValue.setReadOnly(True)
flexcomSym_UsartClkValue.setDefaultValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")))
flexcomSym_UsartClkValue.setVisible(False)
flexcomSym_UsartClkValue.setDependencies(clockSourceFreq, ["FLEXCOM_MODE", "FLEXCOM_USART_MR_USCLKS", "core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

flexcomSym_UsartIRDAFilterValue = flexcomComponent.createIntegerSymbol("FLEX_USART_IRDA_FILTER_VAL", flexcomSym_OperatingMode)
flexcomSym_UsartIRDAFilterValue.setLabel("Clock Source Value")
flexcomSym_UsartIRDAFilterValue.setReadOnly(True)
flexcomSym_UsartIRDAFilterValue.setDefaultValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")))
flexcomSym_UsartIRDAFilterValue.setVisible(False)
flexcomSym_UsartIRDAFilterValue.setDependencies(irdaFilterVal, ["core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

flexcomSym_UsartBaud = flexcomComponent.createIntegerSymbol("BAUD_RATE", flexcomSym_OperatingMode)
flexcomSym_UsartBaud.setLabel("Baud Rate")
flexcomSym_UsartBaud.setDefaultValue(115200)
flexcomSym_UsartBaud.setMin(1)
flexcomSym_UsartBaud.setVisible(False)
flexcomSym_UsartBaud.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_BaudRatePerErrorComment = flexcomComponent.createCommentSymbol("FLEXCOM_BAUD_PER_ERROR_COMMENT", flexcomSym_OperatingMode)
flexcomSym_BaudRatePerErrorComment.setVisible(False)
flexcomSym_BaudRatePerErrorComment.setLabel("Baud rate error is" + "" + "Maximum baud rate error must be within +/- 1.87%.  ")
flexcomSym_BaudRatePerErrorComment.setDependencies(irdaBaudErrorCalculate, ["FLEXCOM_MODE", "FLEXCOM_USART_MR_USART_MODE"])

cd, fp, overSamp = baudRateCalc(flexcomSym_UsartClkValue.getValue(), flexcomSym_UsartBaud.getValue())
flexcomSym_MR_OVER = flexcomComponent.createIntegerSymbol("FLEXCOM_USART_MR_OVER", flexcomSym_OperatingMode)
flexcomSym_MR_OVER.setVisible(False)
flexcomSym_MR_OVER.setDefaultValue(overSamp)
flexcomSym_MR_OVER.setDependencies(baudRateTrigger, ["BAUD_RATE", "FLEX_USART_CLOCK_FREQ", "EXTERNAL_CLOCK_FREQ"])

flexcomSym_UsartBRGValue = flexcomComponent.createIntegerSymbol("BRG_VALUE", flexcomSym_OperatingMode)
flexcomSym_UsartBRGValue.setVisible(False)
flexcomSym_UsartBRGValue.setDefaultValue(cd)
flexcomSym_UsartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "FLEX_USART_CLOCK_FREQ", "EXTERNAL_CLOCK_FREQ"])

flexcomSym_UsartFPValue = flexcomComponent.createIntegerSymbol("FP_VALUE", flexcomSym_OperatingMode)
flexcomSym_UsartFPValue.setVisible(False)
flexcomSym_UsartFPValue.setDefaultValue(fp)
flexcomSym_UsartFPValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "FLEX_USART_CLOCK_FREQ", "EXTERNAL_CLOCK_FREQ"])

flexcomSym_Usart_MR_CHRL = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_CHRL", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL.setLabel("Data")
flexcomSym_Usart_MR_CHRL_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_US_MR__CHRL\"]")
flexcomSym_Usart_MR_CHRL_Values = []
flexcomSym_Usart_MR_CHRL_Values = flexcomSym_Usart_MR_CHRL_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_CHRL_Values)):
    flexcomSym_Usart_MR_CHRL_Key_Name = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_CHRL_Key_Value = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_CHRL_Key_Description = flexcomSym_Usart_MR_CHRL_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_CHRL.addKey(flexcomSym_Usart_MR_CHRL_Key_Name, flexcomSym_Usart_MR_CHRL_Key_Value, flexcomSym_Usart_MR_CHRL_Key_Description)
# There is no 9 bit available under MR_CHRL, but added here just for menu.
# FLEX_USART_MR_MODE9 will use this value
flexcomSym_Usart_MR_CHRL.addKey("_9_BIT", "4", "Character length is 9 bits")
flexcomSym_Usart_MR_CHRL.setDisplayMode("Description")
flexcomSym_Usart_MR_CHRL.setOutputMode("Key")
flexcomSym_Usart_MR_CHRL.setDefaultValue(3)
flexcomSym_Usart_MR_CHRL.setVisible(False)
flexcomSym_Usart_MR_CHRL.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSym_Usart_MR_MODE9 = flexcomComponent.createBooleanSymbol("FLEX_USART_MR_MODE9", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_MODE9.setVisible(False)
flexcomSym_Usart_MR_MODE9.setDependencies(dataWidthLogic, ["FLEX_USART_MR_CHRL"])
flexcomSym_Usart_MR_MODE9.setLabel("9 Bit Data Width")
flexcomSym_Usart_MR_MODE9.setDefaultValue(False)

#FLEXCOM USART Character Size 5 Mask
flexcomSym_Usart_MR_CHRL_5_Mask = flexcomComponent.createStringSymbol("USART_DATA_5_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_5_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_CHRL_5_Mask.setVisible(False)

#FLEXCOM USART Character Size 6 Mask
flexcomSym_Usart_MR_CHRL_6_Mask = flexcomComponent.createStringSymbol("USART_DATA_6_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_6_Mask.setDefaultValue("0x40")
flexcomSym_Usart_MR_CHRL_6_Mask.setVisible(False)

#FLEXCOM USART Character Size 7 Mask
flexcomSym_Usart_MR_CHRL_7_Mask = flexcomComponent.createStringSymbol("USART_DATA_7_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_7_Mask.setDefaultValue("0x80")
flexcomSym_Usart_MR_CHRL_7_Mask.setVisible(False)

#FLEXCOM USART Character Size 8 Mask
flexcomSym_Usart_MR_CHRL_8_Mask = flexcomComponent.createStringSymbol("USART_DATA_8_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_8_Mask.setDefaultValue("0xC0")
flexcomSym_Usart_MR_CHRL_8_Mask.setVisible(False)

#FLEXCOM USART Character Size 9 Mask
flexcomSym_Usart_MR_CHRL_9_Mask = flexcomComponent.createStringSymbol("USART_DATA_9_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_CHRL_9_Mask.setDefaultValue("0x20000")
flexcomSym_Usart_MR_CHRL_9_Mask.setVisible(False)

flexcomSym_Usart_MR_PAR = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_PAR", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR.setLabel("Parity")
flexcomSym_Usart_MR_PAR_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_US_MR__PAR\"]")
flexcomSym_Usart_MR_PAR_Values = []
flexcomSym_Usart_MR_PAR_Values = flexcomSym_Usart_MR_PAR_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_PAR_Values)):
    flexcomSym_Usart_MR_PAR_Key_Name = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_PAR_Key_Value = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_PAR_Key_Description = flexcomSym_Usart_MR_PAR_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_PAR.addKey(flexcomSym_Usart_MR_PAR_Key_Name, flexcomSym_Usart_MR_PAR_Key_Value, flexcomSym_Usart_MR_PAR_Key_Description)
flexcomSym_Usart_MR_PAR.setDefaultValue(4)
flexcomSym_Usart_MR_PAR.setDisplayMode("Key")
flexcomSym_Usart_MR_PAR.setOutputMode("Key")
flexcomSym_Usart_MR_PAR.setVisible(False)
flexcomSym_Usart_MR_PAR.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

#FLEXCOM USART EVEN Parity Mask
flexcomSym_Usart_MR_PAR_EVEN_Mask = flexcomComponent.createStringSymbol("USART_PARITY_EVEN_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_PAR_EVEN_Mask.setVisible(False)

#FLEXCOM USART ODD Parity Mask
flexcomSym_Usart_MR_PAR_ODD_Mask = flexcomComponent.createStringSymbol("USART_PARITY_ODD_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_ODD_Mask.setDefaultValue("0x200")
flexcomSym_Usart_MR_PAR_ODD_Mask.setVisible(False)

#FLEXCOM USART SPACE Parity Mask
flexcomSym_Usart_MR_PAR_SPACE_Mask = flexcomComponent.createStringSymbol("USART_PARITY_SPACE_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
flexcomSym_Usart_MR_PAR_SPACE_Mask.setVisible(False)

#FLEXCOM USART MARK Parity Mask
flexcomSym_Usart_MR_PAR_MARK_Mask = flexcomComponent.createStringSymbol("USART_PARITY_MARK_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_MARK_Mask.setDefaultValue("0x600")
flexcomSym_Usart_MR_PAR_MARK_Mask.setVisible(False)

#FLEXCOM USART NO Parity Mask
flexcomSym_Usart_MR_PAR_NO_Mask = flexcomComponent.createStringSymbol("USART_PARITY_NONE_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_NO_Mask.setDefaultValue("0x800")
flexcomSym_Usart_MR_PAR_NO_Mask.setVisible(False)

#FLEXCOM USART MULTIDROP Parity Mask
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask = flexcomComponent.createStringSymbol("USART_PARITY_MULTIDROP_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask.setDefaultValue("0xC00")
flexcomSym_Usart_MR_PAR_MULTIDROP_Mask.setVisible(False)

flexcomSym_Usart_MR_NBSTOP = flexcomComponent.createKeyValueSetSymbol("FLEX_USART_MR_NBSTOP", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP.setLabel("Stop")
flexcomSym_Usart_MR_NBSTOP_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_US_MR__NBSTOP\"]")
flexcomSym_Usart_MR_NBSTOP_Values = []
flexcomSym_Usart_MR_NBSTOP_Values = flexcomSym_Usart_MR_NBSTOP_Node.getChildren()
for index in range(len(flexcomSym_Usart_MR_NBSTOP_Values)):
    flexcomSym_Usart_MR_NBSTOP_Key_Name = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("name")
    flexcomSym_Usart_MR_NBSTOP_Key_Value = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("value")
    flexcomSym_Usart_MR_NBSTOP_Key_Description = flexcomSym_Usart_MR_NBSTOP_Values[index].getAttribute("caption")
    flexcomSym_Usart_MR_NBSTOP.addKey(flexcomSym_Usart_MR_NBSTOP_Key_Name, flexcomSym_Usart_MR_NBSTOP_Key_Value, flexcomSym_Usart_MR_NBSTOP_Key_Description)
flexcomSym_Usart_MR_NBSTOP.setDisplayMode("Description")
flexcomSym_Usart_MR_NBSTOP.setOutputMode("Key")
flexcomSym_Usart_MR_NBSTOP.setDefaultValue(0)
flexcomSym_Usart_MR_NBSTOP.setVisible(False)
flexcomSym_Usart_MR_NBSTOP.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

#FLEXCOM USART Stop 1-bit Mask
flexcomSym_Usart_MR_NBSTOP_1_Mask = flexcomComponent.createStringSymbol("USART_STOP_1_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_1_Mask.setDefaultValue("0x0")
flexcomSym_Usart_MR_NBSTOP_1_Mask.setVisible(False)

#FLEXCOM USART Stop 1_5-bit Mask
flexcomSym_Usart_MR_NBSTOP_1_5_Mask = flexcomComponent.createStringSymbol("USART_STOP_1_5_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_1_5_Mask.setDefaultValue("0x1000")
flexcomSym_Usart_MR_NBSTOP_1_5_Mask.setVisible(False)

#FLEXCOM USART Stop 2-bit Mask
flexcomSym_Usart_MR_NBSTOP_2_Mask = flexcomComponent.createStringSymbol("USART_STOP_2_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_Usart_MR_NBSTOP_2_Mask.setDefaultValue("0x2000")
flexcomSym_Usart_MR_NBSTOP_2_Mask.setVisible(False)

#FLEXCOM USART Overrun error Mask
flexcomSym_Usart_CSR_OVRE_Mask = flexcomComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_OVRE_Mask.setDefaultValue("0x20")
flexcomSym_Usart_CSR_OVRE_Mask.setVisible(False)

#FLEXCOM USART parity error Mask
flexcomSym_Usart_CSR_PARE_Mask = flexcomComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_PARE_Mask.setDefaultValue("0x80")
flexcomSym_Usart_CSR_PARE_Mask.setVisible(False)

#FLEXCOM USART framing error Mask
flexcomSym_Usart_CSR_FRAME_Mask = flexcomComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", flexcomSym_OperatingMode)
flexcomSym_Usart_CSR_FRAME_Mask.setDefaultValue("0x40")
flexcomSym_Usart_CSR_FRAME_Mask.setVisible(False)

#FLEXCOM USART API Prefix
flexcomSym_Usart_API_Prefix = flexcomComponent.createStringSymbol("USART_PLIB_API_PREFIX", flexcomSym_OperatingMode)
flexcomSym_Usart_API_Prefix.setDefaultValue(flexcomInstanceName.getValue() + "_USART")
flexcomSym_Usart_API_Prefix.setVisible(False)

flexcomSym_Usart_DataBits = flexcomComponent.createStringSymbol("USART_DATA_BITS", flexcomSym_OperatingMode)
flexcomSym_Usart_DataBits.setDefaultValue(dataBitsDict[flexcomSym_Usart_MR_CHRL.getSelectedKey()])
flexcomSym_Usart_DataBits.setVisible(False)
flexcomSym_Usart_DataBits.setDependencies(updateUSARTDataBits, ["FLEX_USART_MR_CHRL"])
