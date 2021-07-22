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

################################################################################
#### Global Variables ####
################################################################################

global uartInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################

def isKeyPresent(symbol, key):
    for i in range(symbol.getKeyCount()):
        if symbol.getKey(i) == key:
            return True
    return False

def handleMessage(messageID, args):
    global uartSym_OperatingMode

    result_dict = {}

    if (messageID == "UART_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == True:
                uartSym_OperatingMode.setSelectedKey("NON_BLOCKING")
            else:
                uartSym_OperatingMode.setSelectedKey("BLOCKING")

    elif (messageID == "UART_BLOCKING_MODE"):
        if args.get("isReadOnly") != None:
            uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == True:
                uartSym_OperatingMode.setSelectedKey("BLOCKING")

    elif (messageID == "UART_NON_BLOCKING_MODE"):
        if args.get("isReadOnly") != None:
            uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == True:
                uartSym_OperatingMode.setSelectedKey("NON_BLOCKING")

    elif (messageID == "UART_RING_BUFFER_MODE"):
        if args.get("isReadOnly") != None:
            uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == True:
                uartSym_OperatingMode.setSelectedKey("RING_BUFFER")

    elif (messageID == "UART_NON_BLOCKING_DMA_TX_MODE"):
        if isKeyPresent(uartSym_OperatingMode, "NON_BLOCKING_DMA_TX") == True:
            if args.get("isReadOnly") != None:
                uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
            if args.get("isEnabled") != None:
                if args["isEnabled"] == True:
                    uartSym_OperatingMode.setSelectedKey("NON_BLOCKING_DMA_TX")

    elif (messageID == "UART_NON_BLOCKING_DMA_RX_MODE"):
        if isKeyPresent(uartSym_OperatingMode, "NON_BLOCKING_DMA_RX") == True:
            if args.get("isReadOnly") != None:
                uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
            if args.get("isEnabled") != None:
                if args["isEnabled"] == True:
                    uartSym_OperatingMode.setSelectedKey("NON_BLOCKING_DMA_RX")

    elif (messageID == "UART_NON_BLOCKING_DMA_TX_RX_MODE"):
        if isKeyPresent(uartSym_OperatingMode, "NON_BLOCKING_DMA_TX_RX") == True:
            if args.get("isReadOnly") != None:
                uartSym_OperatingMode.setReadOnly(args["isReadOnly"])
            if args.get("isEnabled") != None:
                if args["isEnabled"] == True:
                    uartSym_OperatingMode.setSelectedKey("NON_BLOCKING_DMA_TX_RX")

    return result_dict

def interruptControl(uartNVIC, event):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, uartInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, uartInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyStatus(symbol, event):

    if (Database.getSymbolValue(uartInstanceName.getValue().lower(), "UART_INTERRUPT_MODE_ENABLE") == True):
        symbol.setVisible(event["value"])

def clockWarningVisible(symbol, event):

    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Calculates BRG value
def baudRateCalc(clk, baud):

    if (clk >= (16 * baud)):
        brgVal = (clk / (16 * baud))
    else :
        brgVal = (clk / (8 * baud))

    return brgVal

def baudRateTrigger(symbol, event):

    clk = Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")
    baud = Database.getSymbolValue(uartInstanceName.getValue().lower(), "BAUD_RATE")

    brgVal = baudRateCalc(clk, baud)
    uartClockInvalidSym.setVisible((brgVal < 1) or (brgVal > 65535))
    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):

    symbol.clearValue()
    symbol.setValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def updateSymbolVisibility(symbol, event):

    # Enable TX and RX ring buffer size option if Ring buffer is enabled.
    symbol.setVisible(event["value"])

def UARTFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = event["value"]

    if componentID == "UART_HEADER1":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_6418/templates/plib_uart_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/uart_6418/templates/plib_uart.h.ftl"
    elif componentID == "UART_SOURCE1":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_6418/templates/plib_uart_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/uart_6418/templates/plib_uart.c.ftl"

    symbol.setSourcePath(filepath)

def updateInterruptMode (symbol, event):
    if symbol.getLabel() != "---":
        uartOperatingModeSym = event["source"].getSymbolByID("UART_OPERATING_MODE")
        if event["value"] == True and uartOperatingModeSym.getSelectedKey() != "RING_BUFFER" and uartOperatingModeSym.getSelectedKey() != "NON_BLOCKING_DMA_TX" and uartOperatingModeSym.getSelectedKey() != "NON_BLOCKING_DMA_RX" and uartOperatingModeSym.getSelectedKey() != "NON_BLOCKING_DMA_TX_RX":
            uartOperatingModeSym.setSelectedKey("NON_BLOCKING")
        elif event["value"] == False:
            uartOperatingModeSym.setSelectedKey("BLOCKING")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateRingBufferMode (symbol, event):
    if symbol.getLabel() != "---":
        if event["value"] == True:
            event["source"].getSymbolByID("UART_OPERATING_MODE").setSelectedKey("RING_BUFFER")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateRxDMAMode(symbol, event):
    if symbol.getLabel() != "---":
        uartOperatingModeSym = event["source"].getSymbolByID("UART_OPERATING_MODE")
        if event["value"] == True:
            if uartOperatingModeSym.getSelectedKey() == "NON_BLOCKING_DMA_TX":
                uartOperatingModeSym.setSelectedKey("NON_BLOCKING_DMA_TX_RX")
            else:
                uartOperatingModeSym.setSelectedKey("NON_BLOCKING_DMA_RX")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateTxDMAMode(symbol, event):
    if symbol.getLabel() != "---":
        uartOperatingModeSym = event["source"].getSymbolByID("UART_OPERATING_MODE")
        if event["value"] == True:
            if uartOperatingModeSym.getSelectedKey() == "NON_BLOCKING_DMA_RX":
                uartOperatingModeSym.setSelectedKey("NON_BLOCKING_DMA_TX_RX")
            else:
                uartOperatingModeSym.setSelectedKey("NON_BLOCKING_DMA_TX")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateOperatingMode (symbol, event):
    txDMASym = None
    rxDMASym = None
    interruptModeSym = event["source"].getSymbolByID("UART_INTERRUPT_MODE_ENABLE")
    ringBufferModeSym = event["source"].getSymbolByID("UART_RING_BUFFER_MODE_ENABLE")
    isPeriheralDMASupported = event["source"].getSymbolByID("UART_PERIPHERAL_DMA_SUPPORT").getValue()

    if isPeriheralDMASupported == True:
        txDMASym = event["source"].getSymbolByID("USE_UART_TRANSMIT_DMA")
        rxDMASym = event["source"].getSymbolByID("USE_UART_RECEIVE_DMA")

    if symbol.getSelectedKey() == "RING_BUFFER":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(True)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(False)
            rxDMASym.setValue(False)
    elif symbol.getSelectedKey() == "NON_BLOCKING":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(False)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(False)
            rxDMASym.setValue(False)
    elif symbol.getSelectedKey() == "BLOCKING":
        interruptModeSym.setValue(False)
        ringBufferModeSym.setValue(False)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(False)
            rxDMASym.setValue(False)
    elif symbol.getSelectedKey() == "NON_BLOCKING_DMA_TX":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(False)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(True)
            rxDMASym.setValue(False)
    elif symbol.getSelectedKey() == "NON_BLOCKING_DMA_RX":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(False)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(False)
            rxDMASym.setValue(True)
    elif symbol.getSelectedKey() == "NON_BLOCKING_DMA_TX_RX":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(False)
        if isPeriheralDMASupported == True:
            txDMASym.setValue(True)
            rxDMASym.setValue(True)

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(uartComponent):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global uartInstanceName
    global uartClockInvalidSym
    global uartSym_OperatingMode

    uartInstanceName = uartComponent.createStringSymbol("UART_INSTANCE_NAME", None)
    uartInstanceName.setVisible(False)
    uartInstanceName.setDefaultValue(uartComponent.getID().upper())

    # Add DMA support if Peripheral DMA Controller (PDC) exist in the UART register group
    uartRegisterDMA = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"UART\"]/register-group@[name=\"UART\"]/register@[name=\"UART_RPR\"]")

    uartIsPeripheralDMASupported = uartComponent.createBooleanSymbol("UART_PERIPHERAL_DMA_SUPPORT", None)
    uartIsPeripheralDMASupported.setDefaultValue(uartRegisterDMA != None)
    uartIsPeripheralDMASupported.setReadOnly(True)
    uartIsPeripheralDMASupported.setVisible(False)

# Depricated symbols ---------------------------------------------------------------------------------------------------
    uartInterrupt = uartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    uartInterrupt.setLabel("Interrupt Mode")
    uartInterrupt.setDefaultValue(True)
    uartInterrupt.setReadOnly(True)
    uartInterrupt.setVisible(False)
    uartInterrupt.setDependencies(updateInterruptMode, ["USART_INTERRUPT_MODE"])

    #Enable Ring buffer?
    uartSym_RingBuffer_Enable = uartComponent.createBooleanSymbol("UART_RING_BUFFER_ENABLE", None)
    uartSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
    uartSym_RingBuffer_Enable.setDefaultValue(False)
    uartSym_RingBuffer_Enable.setVisible(False)
    uartSym_RingBuffer_Enable.setReadOnly(True)
    uartSym_RingBuffer_Enable.setDependencies(updateRingBufferMode, ["UART_RING_BUFFER_ENABLE"])

    if uartIsPeripheralDMASupported.getValue() == True:
        uartRxDMAEnable = uartComponent.createBooleanSymbol("USE_UART_RX_DMA", None)
        uartRxDMAEnable.setLabel("Enable DMA for Receive")
        uartRxDMAEnable.setVisible(False)
        uartRxDMAEnable.setReadOnly(True)
        uartRxDMAEnable.setDependencies(updateRxDMAMode, ["USE_UART_RX_DMA"])

        uartTxDMAEnable = uartComponent.createBooleanSymbol("USE_UART_TX_DMA", None)
        uartTxDMAEnable.setLabel("Enable DMA for Transmit")
        uartTxDMAEnable.setVisible(False)
        uartTxDMAEnable.setReadOnly(True)
        uartTxDMAEnable.setDependencies(updateTxDMAMode, ["USE_UART_TX_DMA"])
# Depricated symbols ---------------------------------------------------------------------------------------------------

        # Operating Mode
    uartSym_OperatingMode = uartComponent.createKeyValueSetSymbol("UART_OPERATING_MODE", None)
    uartSym_OperatingMode.setLabel("Operating Mode")
    uartSym_OperatingMode.addKey("BLOCKING", "0", "Blocking mode")
    uartSym_OperatingMode.addKey("NON_BLOCKING", "1", "Non-blocking mode")
    if uartIsPeripheralDMASupported.getValue() == True:
        uartSym_OperatingMode.addKey("NON_BLOCKING_DMA_TX", "2", "Non-blocking mode with DMA for transmit")
        uartSym_OperatingMode.addKey("NON_BLOCKING_DMA_RX", "3", "Non-blocking mode with DMA for receive")
        uartSym_OperatingMode.addKey("NON_BLOCKING_DMA_TX_RX", "4", "Non-blocking mode with DMA for transmit and receive")
    uartSym_OperatingMode.addKey("RING_BUFFER", "5", "Ring buffer mode")
    uartSym_OperatingMode.setDefaultValue(1)
    uartSym_OperatingMode.setDisplayMode("Description")
    uartSym_OperatingMode.setOutputMode("Key")
    uartSym_OperatingMode.setVisible(True)
    uartSym_OperatingMode.setDependencies(updateOperatingMode, ["UART_OPERATING_MODE"])

    # Enable Interrupts?
    uartSymInterruptModeEnable = uartComponent.createBooleanSymbol("UART_INTERRUPT_MODE_ENABLE", None)
    uartSymInterruptModeEnable.setLabel("Enable Interrrupts ?")
    uartSymInterruptModeEnable.setDefaultValue(True)
    uartSymInterruptModeEnable.setReadOnly(True)
    uartSymInterruptModeEnable.setVisible(False)

    #Enable Ring buffer?
    uartSym_RingBufferMode_Enable = uartComponent.createBooleanSymbol("UART_RING_BUFFER_MODE_ENABLE", None)
    uartSym_RingBufferMode_Enable.setLabel("Enable Ring Buffer ?")
    uartSym_RingBufferMode_Enable.setDefaultValue(False)
    uartSym_RingBufferMode_Enable.setReadOnly(True)
    uartSym_RingBufferMode_Enable.setVisible(False)

    # DMA RX/TX
    if uartIsPeripheralDMASupported.getValue() == True:
        uartReceiveDMAEnable = uartComponent.createBooleanSymbol("USE_UART_RECEIVE_DMA", None)
        uartReceiveDMAEnable.setLabel("Enable DMA for Receive")
        uartReceiveDMAEnable.setVisible(False)
        uartReceiveDMAEnable.setReadOnly(True)

        uartTransmitDMAEnable = uartComponent.createBooleanSymbol("USE_UART_TRANSMIT_DMA", None)
        uartTransmitDMAEnable.setLabel("Enable DMA for Transmit")
        uartTransmitDMAEnable.setVisible(False)
        uartTransmitDMAEnable.setReadOnly(True)

    uartSym_RingBufferSizeConfig = uartComponent.createCommentSymbol("UART_RING_BUFFER_SIZE_CONFIG", None)
    uartSym_RingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
    uartSym_RingBufferSizeConfig.setVisible(False)
    uartSym_RingBufferSizeConfig.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSym_TXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_TX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    uartSym_TXRingBuffer_Size.setMin(2)
    uartSym_TXRingBuffer_Size.setMax(65535)
    uartSym_TXRingBuffer_Size.setDefaultValue(128)
    uartSym_TXRingBuffer_Size.setVisible(False)
    uartSym_TXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSym_RXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_RX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    uartSym_RXRingBuffer_Size.setMin(2)
    uartSym_RXRingBuffer_Size.setMax(65535)
    uartSym_RXRingBuffer_Size.setDefaultValue(128)
    uartSym_RXRingBuffer_Size.setVisible(False)
    uartSym_RXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    # Clock
    uart_clock = []
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"UART\"]/instance@[name=\"" + uartInstanceName.getValue() + "\"]/parameters")
    uart_clock = node.getChildren()

    uartClkSrc = uartComponent.createKeyValueSetSymbol("UART_CLK_SRC", None)
    uartClkSrc.setLabel("Select Clock Source")

    for clock in range(0, len(uart_clock)):
        if ("BRSRCCK" in uart_clock[clock].getAttribute("name")):
            name_split = uart_clock[clock].getAttribute("name").split("_")[1:]
            name = "_".join(name_split)
            uartClkSrc.addKey(name, uart_clock[clock].getAttribute("value"), uart_clock[clock].getAttribute("caption"))

    uartClkSrc.setDisplayMode("Description")
    uartClkSrc.setOutputMode("Key")
    uartClkSrc.setDefaultValue(0)
    uartClkSrc.setVisible(uartClkSrc.getKeyCount() > 0)

    uartClkValue = uartComponent.createIntegerSymbol("UART_CLOCK_FREQ", None)
    uartClkValue.setLabel("Clock Frequency")
    uartClkValue.setReadOnly(True)
    uartClkValue.setDependencies(clockSourceFreq, ["UART_CLK_SRC", "core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    uartClkValue.setDefaultValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")))

    uartSymClkEnComment = uartComponent.createCommentSymbol("UART_CLK_ENABLE_COMMENT", None)
    uartSymClkEnComment.setVisible(False)
    uartSymClkEnComment.setLabel("Warning!!! UART Peripheral Clock is Disabled in Clock Manager")
    uartSymClkEnComment.setDependencies(clockWarningVisible, ["core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    # Baud
    uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", None)
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(115200)

    uartClockInvalidSym = uartComponent.createCommentSymbol("UART_CLOCK_INVALID", None)
    uartClockInvalidSym.setLabel("Warning!!! Configured baud rate cannot be acheived using current source clock frequency !!!")
    uartClockInvalidSym.setVisible(False)

    brgVal = baudRateCalc(uartClkValue.getValue(), uartBaud.getValue())

    uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", None)
    uartBRGValue.setVisible(False)
    uartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    uartBRGValue.setDefaultValue(brgVal)

    uartDataWidth = uartComponent.createComboSymbol("UART_MR_DATA_WIDTH", None, ["8 BIT"])
    uartDataWidth.setLabel("Data")
    uartDataWidth.setDefaultValue("8_BIT")
    uartDataWidth.setReadOnly(True)

    #UART Character Size 8 Mask
    uartDataWidth_8_Mask = uartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    uartDataWidth_8_Mask.setDefaultValue("0x0")
    uartDataWidth_8_Mask.setVisible(False)

    uartValGrp_MR_PAR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_MR__PAR"]')
    parityList = []
    for id in range(0, len(uartValGrp_MR_PAR.getChildren())):
        parityList.append(id + 1)
        parityList[id] = uartValGrp_MR_PAR.getChildren()[id].getAttribute("name")

    uartSym_MR_PAR = uartComponent.createComboSymbol("UART_MR_PAR", None, parityList)
    uartSym_MR_PAR.setLabel("Parity")
    uartSym_MR_PAR.setDefaultValue("NO")

    #UART Transmit data register
    transmitRegister = uartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+uartInstanceName.getValue()+"_REGS->UART_THR)")
    transmitRegister.setVisible(False)

    #UART Receive data register
    receiveRegister = uartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+uartInstanceName.getValue()+"_REGS->UART_RHR)")
    receiveRegister.setVisible(False)

    #UART EVEN Parity Mask
    uartSym_MR_PAR_EVEN_Mask = uartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    uartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
    uartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #UART ODD Parity Mask
    uartSym_MR_PAR_ODD_Mask = uartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    uartSym_MR_PAR_ODD_Mask.setDefaultValue("0x200")
    uartSym_MR_PAR_ODD_Mask.setVisible(False)

    #UART SPACE Parity Mask
    uartSym_MR_PAR_SPACE_Mask = uartComponent.createStringSymbol("USART_PARITY_SPACE_MASK", None)
    uartSym_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
    uartSym_MR_PAR_SPACE_Mask.setVisible(False)

    #UART MARK Parity Mask
    uartSym_MR_PAR_MARK_Mask = uartComponent.createStringSymbol("USART_PARITY_MARK_MASK", None)
    uartSym_MR_PAR_MARK_Mask.setDefaultValue("0x600")
    uartSym_MR_PAR_MARK_Mask.setVisible(False)

    #UART NO Parity Mask
    uartSym_MR_PAR_NO_Mask = uartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    uartSym_MR_PAR_NO_Mask.setDefaultValue("0x800")
    uartSym_MR_PAR_NO_Mask.setVisible(False)

    uartStopBit = uartComponent.createComboSymbol("UART_MR_STOP_BITS", None, ["1 BIT"])
    uartStopBit.setLabel("Stop")
    uartStopBit.setDefaultValue("1_BIT")
    uartStopBit.setReadOnly(True)

    #UART Stop 1-bit Mask
    uartStopBit_1_Mask = uartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    uartStopBit_1_Mask.setDefaultValue("0x0")
    uartStopBit_1_Mask.setVisible(False)

    uartSym_MR_FILTER = uartComponent.createBooleanSymbol("UART_MR_FILTER", None)
    uartSym_MR_FILTER.setLabel("Receiver Digital Filter")
    uartSym_MR_FILTER.setDefaultValue(False)

    #USART Overrun error Mask
    uartSym_SR_OVRE_Mask = uartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    uartSym_SR_OVRE_Mask.setDefaultValue("0x20")
    uartSym_SR_OVRE_Mask.setVisible(False)

    #USART parity error Mask
    uartSym_SR_PARE_Mask = uartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    uartSym_SR_PARE_Mask.setDefaultValue("0x80")
    uartSym_SR_PARE_Mask.setVisible(False)

    #USART framing error Mask
    uartSym_SR_FRAME_Mask = uartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    uartSym_SR_FRAME_Mask.setDefaultValue("0x40")
    uartSym_SR_FRAME_Mask.setVisible(False)

    #UART API Prefix
    uartSym_API_Prefix = uartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    uartSym_API_Prefix.setDefaultValue(uartInstanceName.getValue())
    uartSym_API_Prefix.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = uartInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = uartInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = uartInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = uartInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, uartInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings
    uartinterruptControl = uartComponent.createBooleanSymbol("NVIC_UART_ENABLE", None)
    uartinterruptControl.setDependencies(interruptControl, ["UART_INTERRUPT_MODE_ENABLE"])
    uartinterruptControl.setVisible(False)

    # Dependency Status
    uartSymIntEnComment = uartComponent.createCommentSymbol("UART_NVIC_ENABLE_COMMENT", None)
    uartSymIntEnComment.setVisible(False)
    uartSymIntEnComment.setLabel("Warning!!! UART Interrupt is Disabled in Interrupt Manager")
    uartSymIntEnComment.setDependencies(dependencyStatus, ["core." + interruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    uartHeaderFile = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeaderFile.setSourcePath("../peripheral/uart_6418/templates/plib_uart_common.h")
    uartHeaderFile.setOutputName("plib_uart_common.h")
    uartHeaderFile.setDestPath("/peripheral/uart/")
    uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeaderFile.setType("HEADER")
    uartHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER1", None)
    uartHeader1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_"+uartInstanceName.getValue().lower()+ ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)
    uartHeader1File.setDependencies(UARTFileGeneration, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE1", None)
    uartSource1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_"+uartInstanceName.getValue().lower()+ ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)
    uartSource1File.setDependencies(UARTFileGeneration, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_6418/templates/system/initialization.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_6418/templates/system/definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)

    uartSym_DataBits = uartComponent.createStringSymbol("USART_DATA_BITS", None)
    uartSym_DataBits.setDefaultValue("DRV_USART_DATA_8_BIT")
    uartSym_DataBits.setVisible(False)