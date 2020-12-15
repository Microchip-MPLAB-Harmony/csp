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

global dataBitsDict

dataBitsDict = {
    "5_BIT": "DRV_USART_DATA_5_BIT",
    "6_BIT": "DRV_USART_DATA_6_BIT",
    "7_BIT": "DRV_USART_DATA_7_BIT",
    "8_BIT": "DRV_USART_DATA_8_BIT",
    "9_BIT": "DRV_USART_DATA_9_BIT"
}

################################################################################
#### Global Variables ####
################################################################################

global usartInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################

def handleMessage(messageID, args):
    global usartSym_RingBuffer_Enable
    global usartInterrupt
    global usartSym_Mode
    global usartSPISym_Interrupt
    global usartSPISym_CS
    result_dict = {}

    if (messageID == "UART_RING_BUFFER_MODE"):
        if args.get("isReadOnly") != None:
            usartSym_RingBuffer_Enable.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            usartSym_RingBuffer_Enable.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            usartSym_RingBuffer_Enable.setVisible(args["isVisible"])

    elif (messageID == "UART_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            usartInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            usartInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            usartInterrupt.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None and args["isReadOnly"] == True:
            usartSym_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            usartSym_Mode.setSelectedKey("SPI_MASTER")

    #elif (messageID == "SPI_SLAVE_MODE"):
        # To be implemented

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            usartSPISym_Interrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            usartSPISym_Interrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            usartSPISym_Interrupt.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if args.get("isReadOnly") != None:
            usartSPISym_CS.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == False:
                usartSPISym_CS.setValue(1)
            else:
                usartSPISym_CS.setValue(0)
        if args.get("isVisible") != None:
            usartSPISym_CS.setVisible(args["isVisible"])

    return result_dict

def interruptControl(usartNVIC, event):

    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyStatus(symbol, event):

    if (Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

def clockWarningCb(symbol, event):

    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Calculates BRG value
def baudRateCalc(clk, baud, overSamp):

    if (overSamp == 0):
        brgVal = (clk / (16 * baud))
    else :
        brgVal = (clk / (8 * baud))

    return brgVal

def baudRateTrigger(symbol, event):

    global usartInstanceName

    if Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_MODE") == 0:

        clk = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLOCK_FREQ")
        baud = Database.getSymbolValue(usartInstanceName.getValue().lower(), "BAUD_RATE")
        overSamp = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_MR_OVER")

        brgVal = baudRateCalc(clk, baud, overSamp)

        usartBaudComment = event["source"].getSymbolByID("USART_BAUD_WARNING")
        usartBaudComment.setVisible(brgVal < 1)

        symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):

    symbol.clearValue()
    symbol.setValue(int(Database.getSymbolValue("core", usartInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def dataWidthLogic(symbol, event):

    symbol.clearValue()

    if(event["value"] == 4):
        symbol.setValue(True, 2)
    else:
        symbol.setValue(False, 2)

# Dependency Function for symbol visibility
def updateUSARTDMAConfigurationVisbleProperty(symbol, event):
    global usartInterrupt
    global usartSym_RingBuffer_Enable

    rxDMAVal = event["source"].getSymbolByID("USE_USART_RX_DMA").getValue()
    txDMAVal = event["source"].getSymbolByID("USE_USART_TX_DMA").getValue()

    if event["source"].getSymbolByID("USART_MODE").getValue() == 0:
        symbol.setVisible(usartInterrupt.getValue() == True)
        symbol.setReadOnly(usartSym_RingBuffer_Enable.getValue() == True)
        if symbol.getID() == "USE_USART_RX_DMA" or symbol.getID() == "USE_USART_TX_DMA":
            usartSym_RingBuffer_Enable.setReadOnly(rxDMAVal == True or txDMAVal == True)
    else:
        symbol.setVisible(False)

def updateRingBufferSymbolVisibility(symbol, event):
    global usartInterrupt
    global usartSym_RingBuffer_Enable

    peripheral_rxdma = event["source"].getSymbolByID("USE_USART_RX_DMA")
    peripheral_txdma = event["source"].getSymbolByID("USE_USART_TX_DMA")

    if event["source"].getSymbolByID("USART_MODE").getValue() == 0:
        # Enable RX ring buffer size option if Ring buffer is enabled.
        if symbol.getID() == "USART_RX_RING_BUFFER_SIZE":
            symbol.setVisible(usartSym_RingBuffer_Enable.getValue())
        # Enable TX ring buffer size option if Ring buffer is enabled.
        elif symbol.getID() == "USART_TX_RING_BUFFER_SIZE":
            symbol.setVisible(usartSym_RingBuffer_Enable.getValue())
        elif symbol.getID() == "USART_RING_BUFFER_ENABLE":
            symbol.setVisible(usartInterrupt.getValue() == True)
            if (usartInterrupt.getValue() == False):
                readOnlyState = symbol.getReadOnly()
                symbol.setReadOnly(True)
                symbol.setValue(False)
                symbol.setReadOnly(readOnlyState)
            if (peripheral_rxdma != None and peripheral_txdma != None):
                peripheral_rxdma.setReadOnly(symbol.getValue() == True)
                peripheral_txdma.setReadOnly(symbol.getValue() == True)
    else:
        symbol.setVisible(False)

def updateUSARTSymVisibility(symbol, event):

    symbol.setVisible( event["symbol"].getValue() == 0)

def updateUSART_SPISymVisibility(symbol, event):

    symbol.setVisible( event["symbol"].getValue() == 1)

def updateUSART_SPIDMAConfigurationVisbleProperty(symbol, event):

    if event["id"] == "USART_SPI_INTERRUPT_MODE":
        symbol.setVisible(event["value"])
    else:
        symbol.setVisible(event["value"] == 1)

def usartSPI_BRGRCalculate(symbol, event):
    global usartInstanceName

    baudComment = event["source"].getSymbolByID("USART_SPI_BAUD_WARNING")

    if Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_MODE") == 1:

        clk = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLOCK_FREQ")
        baud = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_SPI_BAUD_RATE")
        brgrVal = clk/baud

        # For USART SPI, BRGR value cannot be less than 6
        if (brgrVal < 6):
            brgrVal = 6
            baudComment.setVisible(True)
        elif (brgrVal > 65535):
            brgrVal = 65535
            baudComment.setVisible(True)
        else:
            baudComment.setVisible(False)

        symbol.setValue(brgrVal)
    else:
        baudComment.setVisible(False)

def USARTFileGeneration(symbol, event):
    global usartInstanceName

    symbolID = symbol.getID()
    filepath = ""
    outputName = ""

    ringBufferModeEnabled = event["source"].getSymbolByID("USART_RING_BUFFER_ENABLE").getValue()
    usartInterruptMode = event["source"].getSymbolByID("USART_INTERRUPT_MODE").getValue()
    usartMode = event["source"].getSymbolByID("USART_MODE").getValue()

    if symbolID == "USART_HEADER":       # Common header file
        if usartMode == 0:
            filepath = "../peripheral/usart_6089/templates/plib_usart_common.h"
            outputName = "plib_usart_common.h"
        else:
            filepath = "../peripheral/usart_6089/templates/plib_usart_spi_common.h"
            outputName = "plib_usart_spi_common.h"
    elif symbolID == "USART_HEADER1":      # Header file
        if usartMode == 0:
            if ringBufferModeEnabled == True and usartInterruptMode == True:
                filepath = "../peripheral/usart_6089/templates/plib_usart_ring_buffer.h.ftl"
            else:
                filepath = "../peripheral/usart_6089/templates/plib_usart.h.ftl"
            outputName = "plib_"+usartInstanceName.getValue().lower()+".h"
        else:
            filepath = "../peripheral/usart_6089/templates/plib_usart_spi.h.ftl"
            outputName = "plib_"+usartInstanceName.getValue().lower()+"_spi.h"
    elif symbolID == "USART_SOURCE1":    # Source file
        if usartMode == 0:
            if ringBufferModeEnabled == True and usartInterruptMode == True:
                filepath = "../peripheral/usart_6089/templates/plib_usart_ring_buffer.c.ftl"
            else:
                filepath = "../peripheral/usart_6089/templates/plib_usart.c.ftl"
            outputName = "plib_"+usartInstanceName.getValue().lower()+".c"
        else:
            filepath = "../peripheral/usart_6089/templates/plib_usart_spi.c.ftl"
            outputName = "plib_"+usartInstanceName.getValue().lower()+"_spi.c"

    symbol.setSourcePath(filepath)
    symbol.setOutputName(outputName)

def updateUSARTDataBits (symbol, event):

    dataBits = event["symbol"].getSelectedKey()
    symbol.setValue(dataBitsDict[dataBits])
################################################################################
#### Component ####
################################################################################

def instantiateComponent(usartComponent):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global usartInstanceName
    global usartSym_RingBuffer_Enable
    global usartInterrupt
    global uartCapabilityId
    global spiCapabilityId
    global usartSPISym_Interrupt
    global usartSPISym_CS
    global usartSym_Mode

    usartInstanceName = usartComponent.createStringSymbol("USART_INSTANCE_NAME", None)
    usartInstanceName.setVisible(False)
    usartInstanceName.setDefaultValue(usartComponent.getID().upper())
    Log.writeInfoMessage("Running " + usartInstanceName.getValue())

    uartCapabilityId = usartInstanceName.getValue() + "_UART"
    spiCapabilityId = usartInstanceName.getValue() + "_SPI"

    usartSym_Mode = usartComponent.createKeyValueSetSymbol("USART_MODE", None)
    usartSym_Mode.setLabel("Mode")
    usartSym_Mode.addKey("USART", "0x0", "USART")
    usartSym_Mode.addKey("SPI_MASTER", "0xE", "SPI MASTER")
    usartSym_Mode.setDisplayMode("Description")
    usartSym_Mode.setOutputMode("Key")
    usartSym_Mode.setDefaultValue(0)

    usart_clock = []
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"USART\"]/instance@[name=\"" + usartInstanceName.getValue() + "\"]/parameters")
    usart_clock = node.getChildren()

    usartClkSrc = usartComponent.createKeyValueSetSymbol("USART_CLK_SRC", None)
    usartClkSrc.setLabel("Select Clock Source")

    for clock in range(0, len(usart_clock)):
        if ("USCLKS" in usart_clock[clock].getAttribute("name")):
            if ("SCK" not in usart_clock[clock].getAttribute("name")):
                name_split = usart_clock[clock].getAttribute("name").split("_")[1:]
                name = "_".join(name_split)
                usartClkSrc.addKey(name, usart_clock[clock].getAttribute("value"), usart_clock[clock].getAttribute("caption"))

    usartClkSrc.setDisplayMode("Description")
    usartClkSrc.setOutputMode("Key")

    usartClkValue = usartComponent.createIntegerSymbol("USART_CLOCK_FREQ", None)
    usartClkValue.setLabel("Source Clock Frequency")
    usartClkValue.setReadOnly(True)
    usartClkValue.setDependencies(clockSourceFreq, ["USART_CLK_SRC", "core." + usartInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    usartClkValue.setDefaultValue(int(Database.getSymbolValue("core", usartInstanceName.getValue() + "_CLOCK_FREQUENCY")))

    usartBaud = usartComponent.createIntegerSymbol("BAUD_RATE", None)
    usartBaud.setLabel("Baud Rate")
    usartBaud.setDefaultValue(115200)
    usartBaud.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    usartBaudComment = usartComponent.createCommentSymbol("USART_BAUD_WARNING", None)
    usartBaudComment.setLabel("USART Clock source value is low for the desired baud rate")
    usartBaudComment.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    usartInterrupt = usartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    usartInterrupt.setLabel("Interrupt Mode")
    usartInterrupt.setDefaultValue(True)
    usartInterrupt.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    # Add DMA support if Peripheral DMA Controller (PDC) exist in the UART register group
    usartRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"USART\"]/register-group@[name=\"USART\"]")
    usartRegisterList = usartRegisterGroup.getChildren()

    #Enable Ring buffer?
    usartSym_RingBuffer_Enable = usartComponent.createBooleanSymbol("USART_RING_BUFFER_ENABLE", None)
    usartSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
    usartSym_RingBuffer_Enable.setDefaultValue(False)
    usartSym_RingBuffer_Enable.setVisible((usartSym_Mode.getValue() == 0) and (usartInterrupt.getValue() == True))
    usartSym_RingBuffer_Enable.setDependencies(updateRingBufferSymbolVisibility, ["USART_INTERRUPT_MODE", "USART_MODE"])

    usartSym_TXRingBuffer_Size = usartComponent.createIntegerSymbol("USART_TX_RING_BUFFER_SIZE", usartSym_RingBuffer_Enable)
    usartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    usartSym_TXRingBuffer_Size.setMin(2)
    usartSym_TXRingBuffer_Size.setMax(65535)
    usartSym_TXRingBuffer_Size.setDefaultValue(128)
    usartSym_TXRingBuffer_Size.setVisible(usartSym_RingBuffer_Enable.getValue() == True)
    usartSym_TXRingBuffer_Size.setDependencies(updateRingBufferSymbolVisibility, ["USART_RING_BUFFER_ENABLE", "USART_MODE"])

    usartSym_RXRingBuffer_Size = usartComponent.createIntegerSymbol("USART_RX_RING_BUFFER_SIZE", usartSym_RingBuffer_Enable)
    usartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    usartSym_RXRingBuffer_Size.setMin(2)
    usartSym_RXRingBuffer_Size.setMax(65535)
    usartSym_RXRingBuffer_Size.setDefaultValue(128)
    usartSym_RXRingBuffer_Size.setVisible(usartSym_RingBuffer_Enable.getValue() == True)
    usartSym_RXRingBuffer_Size.setDependencies(updateRingBufferSymbolVisibility, ["USART_RING_BUFFER_ENABLE", "USART_MODE"])

    for index in range(0, len(usartRegisterList)):
        if (usartRegisterList[index].getAttribute("name") == "US_RPR"):
            usartRxDMAEnable = usartComponent.createBooleanSymbol("USE_USART_RX_DMA", None)
            usartRxDMAEnable.setLabel("Enable DMA for Receive")
            usartRxDMAEnable.setVisible(True)
            usartRxDMAEnable.setDependencies(updateUSARTDMAConfigurationVisbleProperty, ["USART_INTERRUPT_MODE", "USART_MODE", "USART_RING_BUFFER_ENABLE", "USE_USART_RX_DMA"])
            break

    for index in range(0, len(usartRegisterList)):
        if (usartRegisterList[index].getAttribute("name") == "US_TPR"):
            usartTxDMAEnable = usartComponent.createBooleanSymbol("USE_USART_TX_DMA", None)
            usartTxDMAEnable.setLabel("Enable DMA for Transmit")
            usartTxDMAEnable.setVisible(True)
            usartTxDMAEnable.setDependencies(updateUSARTDMAConfigurationVisbleProperty, ["USART_INTERRUPT_MODE", "USART_MODE", "USART_RING_BUFFER_ENABLE", "USE_USART_TX_DMA"])
            break

    usartSym_MR_OVER = usartComponent.createKeyValueSetSymbol("USART_MR_OVER", None)
    usartSym_MR_OVER.setLabel("OverSampling")
    usartSym_MR_OVER.addKey("0", "0", "16 Times")
    usartSym_MR_OVER.addKey("1", "1", "8 Times")
    usartSym_MR_OVER.setDisplayMode("Description")
    usartSym_MR_OVER.setOutputMode("Key")
    usartSym_MR_OVER.setDefaultValue(0)
    usartSym_MR_OVER.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    brgVal = baudRateCalc(usartClkValue.getValue(), usartBaud.getValue(), usartSym_MR_OVER.getValue())

    usartBaudComment.setVisible((brgVal < 1) and (usartSym_Mode.getValue() == 0))

    usartBRGValue = usartComponent.createIntegerSymbol("BRG_VALUE", None)
    usartBRGValue.setVisible(False)
    usartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "USART_MR_OVER", "USART_CLOCK_FREQ", "USART_MODE"])
    usartBRGValue.setDefaultValue(brgVal)

    usartSym_MR_CHRL = usartComponent.createKeyValueSetSymbol("USART_MR_CHRL", None)
    usartSym_MR_CHRL.setLabel("Data")
    usartSym_MR_CHRL.addKey("5_BIT", "0", "5 BIT")
    usartSym_MR_CHRL.addKey("6_BIT", "1", "6 BIT")
    usartSym_MR_CHRL.addKey("7_BIT", "2", "7 BIT")
    usartSym_MR_CHRL.addKey("8_BIT", "3", "8 BIT")
    # There is no 9 bit available under MR_CHRL, but added here just for menu.
    # usartSym_MR_MODE9 will use this value
    usartSym_MR_CHRL.addKey("9_BIT", "4", "9 BIT")
    usartSym_MR_CHRL.setDisplayMode("Description")
    usartSym_MR_CHRL.setOutputMode("Key")
    usartSym_MR_CHRL.setDefaultValue(3)
    usartSym_MR_CHRL.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    usartSym_MR_MODE9 = usartComponent.createBooleanSymbol("USART_MR_MODE9", None)
    usartSym_MR_MODE9.setLabel("9 Bit Data Width")
    usartSym_MR_MODE9.setVisible(False)
    usartSym_MR_MODE9.setDependencies(dataWidthLogic, ["USART_MR_CHRL"])

    #USART Transmit data register
    transmitRegister = usartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+usartInstanceName.getValue()+"_REGS->US_THR)")
    transmitRegister.setVisible(False)

    #USART Receive data register
    receiveRegister = usartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+usartInstanceName.getValue()+"_REGS->US_RHR)")
    receiveRegister.setVisible(False)

    #USART Character Size 5 Mask
    usartSym_MR_CHRL_5_Mask = usartComponent.createStringSymbol("USART_DATA_5_BIT_MASK", None)
    usartSym_MR_CHRL_5_Mask.setDefaultValue("0x0")
    usartSym_MR_CHRL_5_Mask.setVisible(False)

    #USART Character Size 6 Mask
    usartSym_MR_CHRL_6_Mask = usartComponent.createStringSymbol("USART_DATA_6_BIT_MASK", None)
    usartSym_MR_CHRL_6_Mask.setDefaultValue("0x40")
    usartSym_MR_CHRL_6_Mask.setVisible(False)

    #USART Character Size 7 Mask
    usartSym_MR_CHRL_7_Mask = usartComponent.createStringSymbol("USART_DATA_7_BIT_MASK", None)
    usartSym_MR_CHRL_7_Mask.setDefaultValue("0x80")
    usartSym_MR_CHRL_7_Mask.setVisible(False)

    #USART Character Size 8 Mask
    usartSym_MR_CHRL_8_Mask = usartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    usartSym_MR_CHRL_8_Mask.setDefaultValue("0xC0")
    usartSym_MR_CHRL_8_Mask.setVisible(False)

    #USART Character Size 9 Mask
    usartSym_MR_CHRL_9_Mask = usartComponent.createStringSymbol("USART_DATA_9_BIT_MASK", None)
    usartSym_MR_CHRL_9_Mask.setDefaultValue("0x20000")
    usartSym_MR_CHRL_9_Mask.setVisible(False)

    parityList = []
    usartValGrp_MR_PAR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="USART"]/value-group@[name="US_MR__PAR"]')

    for id in range(0, len(usartValGrp_MR_PAR.getChildren())):
        parityList.append(id + 1)
        parityList[id] = usartValGrp_MR_PAR.getChildren()[id].getAttribute("name")

    usartSym_MR_PAR = usartComponent.createComboSymbol("USART_MR_PAR", None, parityList)
    usartSym_MR_PAR.setLabel("Parity")
    usartSym_MR_PAR.setDefaultValue("NO")
    usartSym_MR_PAR.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    #USART EVEN Parity Mask
    usartSym_MR_PAR_EVEN_Mask = usartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    usartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
    usartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #USART ODD Parity Mask
    usartSym_MR_PAR_ODD_Mask = usartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    usartSym_MR_PAR_ODD_Mask.setDefaultValue("0x200")
    usartSym_MR_PAR_ODD_Mask.setVisible(False)

    #USART SPACE Parity Mask
    usartSym_MR_PAR_SPACE_Mask = usartComponent.createStringSymbol("USART_PARITY_SPACE_MASK", None)
    usartSym_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
    usartSym_MR_PAR_SPACE_Mask.setVisible(False)

    #USART MARK Parity Mask
    usartSym_MR_PAR_MARK_Mask = usartComponent.createStringSymbol("USART_PARITY_MARK_MASK", None)
    usartSym_MR_PAR_MARK_Mask.setDefaultValue("0x600")
    usartSym_MR_PAR_MARK_Mask.setVisible(False)

    #USART NO Parity Mask
    usartSym_MR_PAR_NO_Mask = usartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    usartSym_MR_PAR_NO_Mask.setDefaultValue("0x800")
    usartSym_MR_PAR_NO_Mask.setVisible(False)

    #USART MULTIDROP Parity Mask
    usartSym_MR_PAR_MULTIDROP_Mask = usartComponent.createStringSymbol("USART_PARITY_MULTIDROP_MASK", None)
    usartSym_MR_PAR_MULTIDROP_Mask.setDefaultValue("0xC00")
    usartSym_MR_PAR_MULTIDROP_Mask.setVisible(False)

    usartSym_MR_NBSTOP = usartComponent.createKeyValueSetSymbol("USART_MR_NBSTOP", None)
    usartSym_MR_NBSTOP.setLabel("Stop")
    usartSym_MR_NBSTOP.addKey("1_BIT", "0", "1 BIT")
    usartSym_MR_NBSTOP.addKey("1_5_BIT", "2", "1.5 BIT")
    usartSym_MR_NBSTOP.addKey("2_BIT", "1", "2 BIT")
    usartSym_MR_NBSTOP.setDisplayMode("Description")
    usartSym_MR_NBSTOP.setOutputMode("Key")
    usartSym_MR_NBSTOP.setDefaultValue(0)
    usartSym_MR_NBSTOP.setDependencies(updateUSARTSymVisibility, ["USART_MODE"])

    #USART Stop 1-bit Mask
    usartSym_MR_NBSTOP_1_Mask = usartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    usartSym_MR_NBSTOP_1_Mask.setDefaultValue("0x0")
    usartSym_MR_NBSTOP_1_Mask.setVisible(False)

    #USART Stop 1_5-bit Mask
    usartSym_MR_NBSTOP_1_5_Mask = usartComponent.createStringSymbol("USART_STOP_1_5_BIT_MASK", None)
    usartSym_MR_NBSTOP_1_5_Mask.setDefaultValue("0x1000")
    usartSym_MR_NBSTOP_1_5_Mask.setVisible(False)

    #USART Stop 2-bit Mask
    usartSym_MR_NBSTOP_2_Mask = usartComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
    usartSym_MR_NBSTOP_2_Mask.setDefaultValue("0x2000")
    usartSym_MR_NBSTOP_2_Mask.setVisible(False)

    #USART API Prefix
    usartSym_API_Prefix = usartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    usartSym_API_Prefix.setDefaultValue(usartInstanceName.getValue())
    usartSym_API_Prefix.setVisible(False)

    #USART Overrun error Mask
    usartSym_CSR_OVRE_Mask = usartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    usartSym_CSR_OVRE_Mask.setDefaultValue("0x20")
    usartSym_CSR_OVRE_Mask.setVisible(False)

    #USART parity error Mask
    usartSym_CSR_PARE_Mask = usartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    usartSym_CSR_PARE_Mask.setDefaultValue("0x80")
    usartSym_CSR_PARE_Mask.setVisible(False)

    #USART framing error Mask
    usartSym_CSR_FRAME_Mask = usartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    usartSym_CSR_FRAME_Mask.setDefaultValue("0x40")
    usartSym_CSR_FRAME_Mask.setVisible(False)

    ############################################################################
    #### USART SPI Mode ####
    ############################################################################
    defaultbaudRate = 1000000
    defaultBRGR = usartClkValue.getValue()/defaultbaudRate

    usartSPISym_Interrupt = usartComponent.createBooleanSymbol("USART_SPI_INTERRUPT_MODE", None)
    usartSPISym_Interrupt.setLabel("Interrupt Mode")
    usartSPISym_Interrupt.setDefaultValue(True)
    usartSPISym_Interrupt.setVisible(False)
    usartSPISym_Interrupt.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    # Add DMA support if Peripheral DMA Controller (PDC) exist in the UART register group
    for index in range(0, len(usartRegisterList)):
        if (usartRegisterList[index].getAttribute("name") == "US_RPR"):
            usartSPISym_TxRxDMAEnable = usartComponent.createBooleanSymbol("USE_USART_SPI_DMA", usartSPISym_Interrupt)
            usartSPISym_TxRxDMAEnable.setLabel("Enable DMA for Transmit and Receive")
            usartSPISym_TxRxDMAEnable.setVisible(True)
            usartSPISym_TxRxDMAEnable.setDependencies(updateUSART_SPIDMAConfigurationVisbleProperty, ["USART_SPI_INTERRUPT_MODE"])
            break

    usartSPISym_baudRate = usartComponent.createIntegerSymbol("USART_SPI_BAUD_RATE", None)
    usartSPISym_baudRate.setLabel("Baud Rate in Hz")
    usartSPISym_baudRate.setDefaultValue(defaultbaudRate)
    usartSPISym_baudRate.setMin(1)
    usartSPISym_baudRate.setVisible(False)
    usartSPISym_baudRate.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    usartSPISym_BaudComment = usartComponent.createCommentSymbol("USART_SPI_BAUD_WARNING", None)
    usartSPISym_BaudComment.setLabel("USART SPI Clock source value is low for the desired baud rate")
    usartSPISym_BaudComment.setVisible((defaultBRGR < 6) and (usartSym_Mode.getValue() == 1))

    usartSPISym_BRGRValue = usartComponent.createIntegerSymbol("USART_SPI_BRG_VALUE", None)
    usartSPISym_BRGRValue.setVisible(False)
    usartSPISym_BRGRValue.setValue(defaultBRGR)
    usartSPISym_BRGRValue.setDependencies(usartSPI_BRGRCalculate, ["USART_SPI_BAUD_RATE", "USART_CLOCK_FREQ", "USART_MODE"])

    usartSPISym_CS = usartComponent.createKeyValueSetSymbol("USART_SPI_CHIP_SELECT", None)
    usartSPISym_CS.setLabel("Peripheral Chip Select")
    usartSPISym_CS.addKey("NSS", "0", "NSS")
    usartSPISym_CS.addKey("GPIO", "1", "GPIO")
    usartSPISym_CS.setDisplayMode("Description")
    usartSPISym_CS.setOutputMode("Key")
    usartSPISym_CS.setDefaultValue(0)
    usartSPISym_CS.setVisible(False)
    usartSPISym_CS.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    usartSPISym_BitsPerTransfer = usartComponent.createKeyValueSetSymbol("USART_SPI_BITS_PER_TRANSFER", None)
    usartSPISym_BitsPerTransfer.setLabel("Bits Per Transfer")
    usartSPISym_BitsPerTransfer.addKey("8-bits", "3", "8 bits for transfer")
    usartSPISym_BitsPerTransfer.setDisplayMode("Description")
    usartSPISym_BitsPerTransfer.setOutputMode("Key")
    usartSPISym_BitsPerTransfer.setDefaultValue(0)
    usartSPISym_BitsPerTransfer.setVisible(False)
    usartSPISym_BitsPerTransfer.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    usartSPISym_DummyData = usartComponent.createHexSymbol("USART_SPI_DUMMY_DATA", None)
    usartSPISym_DummyData.setLabel("Dummy Data")
    usartSPISym_DummyData.setDescription("Dummy Data to be written during SPI Read")
    usartSPISym_DummyData.setDefaultValue(0xFF)
    usartSPISym_DummyData.setMin(0x0)
    usartSPISym_DummyData.setVisible(False)
    usartSPISym_DummyData.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    usartSPISym_CPOL = usartComponent.createKeyValueSetSymbol("USART_SPI_CLOCK_POLARITY", None)
    usartSPISym_CPOL.setLabel("Clock Polarity")
    usartSPISym_CPOL.addKey("IDLE_LOW", "0x0", "Clock is low when inactive (COPL = 0)")
    usartSPISym_CPOL.addKey("IDLE_HIGH", "0x1", "Clock is high when inactive (COPL = 1)")
    usartSPISym_CPOL.setOutputMode("Value")
    usartSPISym_CPOL.setDisplayMode("Description")
    usartSPISym_CPOL.setDefaultValue(0)
    usartSPISym_CPOL.setVisible(False)
    usartSPISym_CPOL.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    usartSPISym_CPHA = usartComponent.createKeyValueSetSymbol("USART_SPI_CLOCK_PHASE", None)
    usartSPISym_CPHA.setLabel("Clock Phase")
    usartSPISym_CPHA.addKey("VALID_FOLLOWING_EDGE", "0x0", "Data is captured on the following edge of SPCK (CPHA = 0)")
    usartSPISym_CPHA.addKey("VALID_LEADING_EDGE", "0x1", "Data is captured on the leading edge of SPCK (CPHA = 1)")
    usartSPISym_CPHA.setOutputMode("Value")
    usartSPISym_CPHA.setDisplayMode("Description")
    usartSPISym_CPHA.setDefaultValue(0)
    usartSPISym_CPHA.setVisible(False)
    usartSPISym_CPHA.setDependencies(updateUSART_SPISymVisibility, ["USART_MODE"])

    ##### SPI DRIVER SYMBOLS #####

    #SPI API Prefix
    usartSPISym_API_Prefix = usartComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    usartSPISym_API_Prefix.setDefaultValue(usartInstanceName.getValue() + "_SPI")
    usartSPISym_API_Prefix.setVisible(False)

    #SPI Clock Polarity Idle Low Mask
    usartSPISym_CPOL_IL_Mask = usartComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    usartSPISym_CPOL_IL_Mask.setDefaultValue("0x00000000")
    usartSPISym_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    usartSPISym_CPOL_IH_Mask = usartComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    usartSPISym_CPOL_IH_Mask.setDefaultValue("0x00010000")
    usartSPISym_CPOL_IH_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    usartSPISym_CPHA_TE_Mask = usartComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    usartSPISym_CPHA_TE_Mask.setDefaultValue("0x00000000")
    usartSPISym_CPHA_TE_Mask.setVisible(False)

    #SPI Clock Phase Leading Edge Mask
    usartSPISym_CPHA_LE_Mask = usartComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    usartSPISym_CPHA_LE_Mask.setDefaultValue("0x00000100")
    usartSPISym_CPHA_LE_Mask.setVisible(False)

    #SPI 8-bit Character size Mask
    usartSPISym_8BIT = usartComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
    usartSPISym_8BIT.setDefaultValue("0x000000C0")
    usartSPISym_8BIT.setVisible(False)

    usartSym_DataBits = usartComponent.createStringSymbol("USART_DATA_BITS", None)
    usartSym_DataBits.setDefaultValue(dataBitsDict[usartSym_MR_CHRL.getSelectedKey()])
    usartSym_DataBits.setVisible(False)
    usartSym_DataBits.setDependencies(updateUSARTDataBits, ["USART_MR_CHRL"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = usartInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = usartInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = usartInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = usartInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", usartInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", usartInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings
    usartinterruptControl = usartComponent.createBooleanSymbol("NVIC_USART_ENABLE", None)
    usartinterruptControl.setDependencies(interruptControl, ["USART_INTERRUPT_MODE"])
    usartinterruptControl.setVisible(False)

    # Dependency Status
    usartSymClkEnComment = usartComponent.createCommentSymbol("USART_CLK_ENABLE_COMMENT", None)
    usartSymClkEnComment.setVisible(False)
    usartSymClkEnComment.setLabel("Warning!!! USART Peripheral Clock is Disabled in Clock Manager")
    usartSymClkEnComment.setDependencies(clockWarningCb, ["core." + usartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    usartSymIntEnComment = usartComponent.createCommentSymbol("USART_NVIC_ENABLE_COMMENT", None)
    usartSymIntEnComment.setVisible(False)
    usartSymIntEnComment.setLabel("Warning!!! USART Interrupt is Disabled in Interrupt Manager")
    usartSymIntEnComment.setDependencies(dependencyStatus, ["core." + interruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    usartHeaderFile = usartComponent.createFileSymbol("USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/usart_6089/templates/plib_usart_common.h")
    usartHeaderFile.setOutputName("plib_usart_common.h")
    usartHeaderFile.setDestPath("peripheral/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setOverwrite(True)
    usartHeaderFile.setDependencies(USARTFileGeneration, ["USART_MODE"])

    usartHeader1File = usartComponent.createFileSymbol("USART_HEADER1", None)
    usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
    usartHeader1File.setOutputName("plib_"+usartInstanceName.getValue().lower()+".h")
    usartHeader1File.setDestPath("peripheral/usart/")
    usartHeader1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeader1File.setType("HEADER")
    usartHeader1File.setOverwrite(True)
    usartHeader1File.setMarkup(True)
    usartHeader1File.setDependencies(USARTFileGeneration, ["USART_RING_BUFFER_ENABLE", "USART_MODE", "USART_INTERRUPT_MODE"])

    usartSource1File = usartComponent.createFileSymbol("USART_SOURCE1", None)
    usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
    usartSource1File.setOutputName("plib_"+usartInstanceName.getValue().lower()+".c")
    usartSource1File.setDestPath("peripheral/usart/")
    usartSource1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartSource1File.setType("SOURCE")
    usartSource1File.setOverwrite(True)
    usartSource1File.setMarkup(True)
    usartSource1File.setDependencies(USARTFileGeneration, ["USART_RING_BUFFER_ENABLE", "USART_MODE", "USART_INTERRUPT_MODE"])

    usartSystemInitFile = usartComponent.createFileSymbol("USART_INIT", None)
    usartSystemInitFile.setType("STRING")
    usartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    usartSystemInitFile.setSourcePath("../peripheral/usart_6089/templates/system/initialization.c.ftl")
    usartSystemInitFile.setMarkup(True)

    usartSystemDefFile = usartComponent.createFileSymbol("USART_DEF", None)
    usartSystemDefFile.setType("STRING")
    usartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    usartSystemDefFile.setSourcePath("../peripheral/usart_6089/templates/system/definitions.h.ftl")
    usartSystemDefFile.setMarkup(True)

def onAttachmentConnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if connectID == uartCapabilityId:
        localComponent.setCapabilityEnabled(uartCapabilityId, True)
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.getSymbolByID("USART_MODE").setSelectedKey("USART", 2)
    elif connectID == spiCapabilityId:
        localComponent.setCapabilityEnabled(uartCapabilityId, False)
        localComponent.setCapabilityEnabled(spiCapabilityId, True)
        localComponent.getSymbolByID("USART_MODE").setSelectedKey("SPI_MASTER", 2)

    localComponent.getSymbolByID("USART_MODE").setReadOnly(True)

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteID, "REQUEST_CONFIG_PARAMS", argDict)

def onAttachmentDisconnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    localComponent.setCapabilityEnabled(uartCapabilityId, True)
    localComponent.setCapabilityEnabled(spiCapabilityId, True)

    localComponent.getSymbolByID("USART_MODE").setReadOnly(False)