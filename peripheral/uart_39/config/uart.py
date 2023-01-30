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

uartLCRRegDepList = []
global uartAggInterruptName
uartAggInterruptName = ""
################################################################################
#### Register Information ####
################################################################################
def handleMessage(messageID, args):
    global uartSym_OperatingMode
    
    print "handleMessage"
    print "messageID = " + messageID

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

    return result_dict

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    print ("onCapabilityConnected")

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)
################################################################################
#### Global Variables ####
################################################################################


################################################################################
#### Business Logic ####
################################################################################


def setUARTInterruptData(uart_interrupt_name, status):

    print uart_interrupt_name
    print status

    Database.setSymbolValue("core", uart_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", uart_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", uart_interrupt_name + "_INTERRUPT_HANDLER", uart_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", uart_interrupt_name + "_INTERRUPT_HANDLER", uart_interrupt_name + "_Handler", 1)

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("name")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def updateRingBufferSymVisibility(symbol, event):

    symbol.setVisible(event["symbol"].getSelectedKey() == "RING_BUFFER")

def baudDivisorCalc(clk_src, baud_clk_src, sel_baud_rate):
    baud_clock = 0
    baud_div = 0

    if clk_src == "INTERNAL":
        if baud_clk_src == "48_MHZ":
            baud_clock = 48000000
        else:
            baud_clock = 1843200
        baud_div = (baud_clock/16)/sel_baud_rate

    if baud_div < 1:
        baud_div = 1
    elif baud_div > 32767:
        baud_div = 32767

    return baud_div

def baudDivisorUpdate(symbol, event):
    clk_src = event["source"].getSymbolByID("UART_CFG_SEL_CLK_SRC").getSelectedKey()
    baud_clk_src = event["source"].getSymbolByID("UART_BAUDRT_MSB_BAUD_CLK_SEL").getSelectedKey()
    sel_baud_rate = event["source"].getSymbolByID("UART_BAUDRATE").getValue()

    baud_div = baudDivisorCalc(clk_src, baud_clk_src, sel_baud_rate)

    symbol.setValue(baud_div)

def baudClockSrcUpdate(symbol, event):
    symbol.setVisible(event["symbol"].getSelectedKey() == "INTERNAL")

def nvicInterruptNameUpdate (symbol, event):
    global uartAggInterruptName
    if event["symbol"].getSelectedKey() == "AGGREGATE":
        symbol.setValue(uartAggInterruptName)
    else:
        symbol.setValue("UART" + uartInstanceNum.getValue())

def nvicInterruptUpdate(symbol, event):
    global uartAggInterruptName
    uartInstanceNum = event["source"].getSymbolByID("UART_INSTANCE_NUM").getValue()
    uartOperatingMode = event["source"].getSymbolByID("UART_OPERATING_MODE").getSelectedKey()
    uartInterruptType = event["source"].getSymbolByID("UART_INTERRUPT_TYPE").getSelectedKey()

    interruptName = "UART" + uartInstanceNum
    print "uartAggInterruptName = " + uartAggInterruptName

    if uartOperatingMode != "BLOCKING":
        if uartInterruptType == "AGGREGATE":
            setUARTInterruptData(interruptName, False)
            setUARTInterruptData(uartAggInterruptName, True)
        else:
            setUARTInterruptData(uartAggInterruptName, False)
            setUARTInterruptData(interruptName, True)
    else:
        setUARTInterruptData(interruptName, False)
        setUARTInterruptData(uartAggInterruptName, False)

def interruptTypeUpdate(symbol, event):
    symbol.setVisible(event["symbol"].getSelectedKey() != "BLOCKING")

def regLCRUpdate(symbol, event):
    lcr_reg = 0

    stop_bit = int(event["source"].getSymbolByID("UART_LCR_STOP_BITS_SELECT").getSelectedValue())
    word_len = int(event["source"].getSymbolByID("UART_LCR_WORD_LENGTH_SELECT").getSelectedValue())
    parity_sel = int(event["source"].getSymbolByID("UART_LCR_PARITY_SELECT").getSelectedValue())

    if parity_sel == -1:
        enable_parity = 0
        parity_sel = 0
    else:
        enable_parity = 1

    lcr_reg = (parity_sel << 4 | enable_parity << 3 | stop_bit << 2 | word_len)
    symbol.setValue(lcr_reg)

def getBaudMSB(baud_divisor, cfg_sel_clk_src, baud_clk_sel):
    baud_msb_reg = 0
    
    # Get the MSB part of Baud Divisor
    baud_divisor = ((baud_divisor & 0xFF00) >> 8)

    if cfg_sel_clk_src == "EXTERNAL":
        baud_clk_sel = 0

    baud_msb_reg = (baud_clk_sel << 7 | baud_divisor)
    return baud_msb_reg
    
def regBaudGenMSBUpdate(symbol, event):

    baud_divisor = int(event["source"].getSymbolByID("UART_BAUDRATE_DIVISOR").getValue())
    cfg_sel_clk_src = event["source"].getSymbolByID("UART_CFG_SEL_CLK_SRC").getSelectedKey()
    baud_clk_sel = int(event["source"].getSymbolByID("UART_BAUDRT_MSB_BAUD_CLK_SEL").getSelectedValue())

    symbol.setValue(getBaudMSB(baud_divisor, cfg_sel_clk_src, baud_clk_sel))

def regBaudGenLSBUpdate(symbol, event):

    baud_divisor = int(event["source"].getSymbolByID("UART_BAUDRATE_DIVISOR").getValue())

    # Get the LSB part of Baud Divisor
    symbol.setValue(baud_divisor & 0xFF)

def configSelUpdate(symbol, event):

    cfg_sel_clk_src = int(event["source"].getSymbolByID("UART_CFG_SEL_CLK_SRC").getSelectedValue())
    cfg_sel_polarity = 1 if event["source"].getSymbolByID("UART_CFG_SEL_POLARITY").getValue() == True else 0

    symbol.setValue(cfg_sel_polarity << 2 | cfg_sel_clk_src)

def updateUSARTDataBits (symbol, event):
    word_len = event["source"].getSymbolByID("UART_LCR_WORD_LENGTH_SELECT").getSelectedKey()
    data_bits = "DRV_USART_DATA_" + word_len
    symbol.setValue(data_bits)
    
def UARTFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = True if event["symbol"].getSelectedKey() == "RING_BUFFER" else False

    if componentID == "UART_HEADER":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_39/templates/plib_uart_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/uart_39/templates/plib_uart.h.ftl"
    elif componentID == "UART_SOURCE":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_39/templates/plib_uart_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/uart_39/templates/plib_uart.c.ftl"

    symbol.setSourcePath(filepath)
    
def irqn_update(symbol, event):
    uartInstanceNum = event["source"].getSymbolByID("UART_INSTANCE_NUM").getValue()
    uartInterruptType = event["source"].getSymbolByID("UART_INTERRUPT_TYPE").getSelectedKey()
    
    if (uartInterruptType == "AGGREGATE"):
        nvic_int_num = {}
        nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "UART" + uartInstanceNum})
        irqn_name = "GIRQ" + str(nvic_int_num["girqn_reg_num"] + 8) + "_IRQn"
        symbol.setValue(irqn_name)
    else:
        symbol.setValue("UART" + uartInstanceNum + "_IRQn")    
################################################################################
#### Component ####
################################################################################

def instantiateComponent(uartComponent):

    global uartInstanceName
    global uartInstanceNum
    global uartAggInterruptName
    global uartSym_OperatingMode

    uartInstanceName = uartComponent.createStringSymbol("UART_INSTANCE_NAME", None)
    uartInstanceName.setVisible(False)
    uartInstanceName.setDefaultValue(uartComponent.getID().upper())
    Log.writeInfoMessage("Running " + uartInstanceName.getValue())

    uartInstanceNum = uartComponent.createStringSymbol("UART_INSTANCE_NUM", None)
    uartInstanceNum.setVisible(False)
    componentName = str(uartComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    uartInstanceNum.setDefaultValue(instanceNum)

    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "UART" + uartInstanceNum.getValue()})
    uartAggInterruptName = nvic_int_num["group_nvic_name"]
    
    print "uartAggInterruptName = " + uartAggInterruptName

    # UART_OPERATING_MODE
    uartSym_OperatingMode = uartComponent.createKeyValueSetSymbol("UART_OPERATING_MODE", None)
    uartSym_OperatingMode.setLabel("Operating Mode")
    uartSym_OperatingMode.addKey("BLOCKING", "0", "Blocking mode")
    uartSym_OperatingMode.addKey("NON_BLOCKING", "1", "Non-blocking mode")
    uartSym_OperatingMode.addKey("RING_BUFFER", "2", "Ring buffer mode")
    uartSym_OperatingMode.setDefaultValue(1)
    uartSym_OperatingMode.setDisplayMode("Description")
    uartSym_OperatingMode.setOutputMode("Key")
    uartSym_OperatingMode.setVisible(True)

    # UART Interrupt Type - Aggregate or Direct
    uartInterruptType = uartComponent.createKeyValueSetSymbol("UART_INTERRUPT_TYPE", None)
    uartInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        uartInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        uartInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    uartInterruptType.setDefaultValue(0)
    uartInterruptType.setDisplayMode("Description")
    uartInterruptType.setOutputMode("Key")
    uartInterruptType.setDependencies(interruptTypeUpdate, ["UART_OPERATING_MODE"])

    # UART_RING_BUFFER_SIZE_CONFIG Label
    uartSym_RingBufferSizeConfig = uartComponent.createCommentSymbol("UART_RING_BUFFER_SIZE_CONFIG", None)
    uartSym_RingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
    uartSym_RingBufferSizeConfig.setVisible(False)
    uartSym_RingBufferSizeConfig.setDependencies(updateRingBufferSymVisibility, ["UART_OPERATING_MODE"])

    # UART_TX_RING_BUFFER_SIZE
    uartSym_TXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_TX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    uartSym_TXRingBuffer_Size.setMin(2)
    uartSym_TXRingBuffer_Size.setMax(65535)
    uartSym_TXRingBuffer_Size.setDefaultValue(128)
    uartSym_TXRingBuffer_Size.setVisible(False)
    uartSym_TXRingBuffer_Size.setDependencies(updateRingBufferSymVisibility, ["UART_OPERATING_MODE"])

    # UART_RX_RING_BUFFER_SIZE
    uartSym_RXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_RX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    uartSym_RXRingBuffer_Size.setMin(2)
    uartSym_RXRingBuffer_Size.setMax(65535)
    uartSym_RXRingBuffer_Size.setDefaultValue(128)
    uartSym_RXRingBuffer_Size.setVisible(False)
    uartSym_RXRingBuffer_Size.setDependencies(updateRingBufferSymVisibility, ["UART_OPERATING_MODE"])

    # Clock source
    uartValGrp_UART_CFG_SEL__CLK_SRC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_CFG_SEL__CLK_SRC"]')

    clk_src_bitfields = []
    _get_bitfield_names(uartValGrp_UART_CFG_SEL__CLK_SRC, clk_src_bitfields)

    uart_CFG_SEL_CLK_SRC_SELECT = uartComponent.createKeyValueSetSymbol("UART_CFG_SEL_CLK_SRC", None)
    uart_CFG_SEL_CLK_SRC_SELECT.setLabel("Clock Source")
    uart_CFG_SEL_CLK_SRC_SELECT.setDefaultValue(0)
    uart_CFG_SEL_CLK_SRC_SELECT.setOutputMode( "Value" )
    uart_CFG_SEL_CLK_SRC_SELECT.setDisplayMode( "Key" )
    for ii in clk_src_bitfields:
        uart_CFG_SEL_CLK_SRC_SELECT.addKey( ii['key'],ii['value'], ii['desc'] )

    # Baud clock source select
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_BAUDRT_MSB__BAUD_CLK_SEL"]')

    baud_clk_bitfields = []
    _get_bitfield_names(uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL, baud_clk_bitfields)
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL = uartComponent.createKeyValueSetSymbol("UART_BAUDRT_MSB_BAUD_CLK_SEL", None)
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.setLabel("Baud Clock Select")
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.setOutputMode( "Value" )
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.setDisplayMode( "Key" )
    uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.setDependencies(baudClockSrcUpdate, ["UART_CFG_SEL_CLK_SRC"])
    index = 0
    for ii in baud_clk_bitfields:
        uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.addKey( ii['key'],ii['value'], ii['desc'] )
        if ii['key'] == "1.8432_MHz":
            uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.setDefaultValue(index)
        else:
            index = index + 1

    # Baud Rate
    uartBaudRate = uartComponent.createIntegerSymbol("UART_BAUDRATE", None)
    uartBaudRate.setLabel("Baud Rate")
    uartBaudRate.setDefaultValue(115200)

    # Baud Rate Divisor
    uartBaudRateDiv = uartComponent.createIntegerSymbol("UART_BAUDRATE_DIVISOR", None)
    uartBaudRateDiv.setLabel("Baud Rate Divisor")
    uartBaudRateDiv.setDefaultValue(baudDivisorCalc(uart_CFG_SEL_CLK_SRC_SELECT.getSelectedKey(), uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.getSelectedKey(), uartBaudRate.getValue()))
    uartBaudRateDiv.setVisible(True)
    uartBaudRateDiv.setReadOnly(True)
    uartBaudRateDiv.setDependencies(baudDivisorUpdate, ["UART_BAUDRATE", "UART_BAUDRT_MSB_BAUD_CLK_SEL", "UART_CFG_SEL_CLK_SRC"])


    # Stop bits
    uartValGrp_UART_LCR__STOP_BIT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_LCR__STOP_BITS"]')

    stop_bit_bitfields = []
    _get_bitfield_names(uartValGrp_UART_LCR__STOP_BIT, stop_bit_bitfields)

    uart_LCR_STOP_BITS = uartComponent.createKeyValueSetSymbol("UART_LCR_STOP_BITS_SELECT", None)
    uart_LCR_STOP_BITS.setLabel("Stop Bits")
    uart_LCR_STOP_BITS.setOutputMode( "Value" )
    uart_LCR_STOP_BITS.setDisplayMode( "Description" )
    for ii in stop_bit_bitfields:
        uart_LCR_STOP_BITS.addKey( ii['key'],ii['value'], ii['desc'] )
    uart_LCR_STOP_BITS.setDefaultValue(0)
    uartLCRRegDepList.append("UART_LCR_STOP_BITS_SELECT")

    # Word Length
    uartValGrp_UART_LCR__WORD_LEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_LCR__WORD_LEN"]')

    word_len_bitfields = []
    _get_bitfield_names(uartValGrp_UART_LCR__WORD_LEN, word_len_bitfields)

    uart_LCR_WORD_LEN = uartComponent.createKeyValueSetSymbol("UART_LCR_WORD_LENGTH_SELECT", None)
    uart_LCR_WORD_LEN.setLabel("Word Length")
    uart_LCR_WORD_LEN.setOutputMode( "Value" )
    uart_LCR_WORD_LEN.setDisplayMode( "Description" )
    index = 0
    for ii in word_len_bitfields:
        uart_LCR_WORD_LEN.addKey( ii['key'],ii['value'], ii['desc'] )
        if ii['key'] == "8_BIT":
            uart_LCR_WORD_LEN.setDefaultValue(index)
        else:
            index = index + 1
    uartLCRRegDepList.append("UART_LCR_WORD_LENGTH_SELECT")

    # Parity
    uartValGrp_UART_LCR__PAR_SEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="UART_LCR__PAR_SEL"]')

    parity_bitfields = []
    _get_bitfield_names(uartValGrp_UART_LCR__PAR_SEL, parity_bitfields)

    uart_LCR_PARITY_SELECT = uartComponent.createKeyValueSetSymbol("UART_LCR_PARITY_SELECT", None)
    uart_LCR_PARITY_SELECT.setLabel("Parity")
    uart_LCR_PARITY_SELECT.setOutputMode( "Value" )
    uart_LCR_PARITY_SELECT.setDisplayMode( "Description" )
    for ii in parity_bitfields:
        uart_LCR_PARITY_SELECT.addKey( ii['key'],ii['value'], ii['desc'] )
    uart_LCR_PARITY_SELECT.addKey("None", "-1", "None")         # Adding special key for No parity
    uart_LCR_PARITY_SELECT.setDefaultValue(2)                   # Set None as default
    uartLCRRegDepList.append("UART_LCR_PARITY_SELECT")

    uart_CFG_SEL_POLARITY = uartComponent.createBooleanSymbol("UART_CFG_SEL_POLARITY", None)
    uart_CFG_SEL_POLARITY.setLabel("Invert UART RX and TX pins ?")
    uart_CFG_SEL_POLARITY.setDefaultValue(False)

    interruptName = ""
    if uartInterruptType.getSelectedKey() == "AGGREGATE":
        interruptName = uartAggInterruptName
    else:
        interruptName = "UART" + uartInstanceNum.getValue()
    uart_NVIC_InterruptName = uartComponent.createStringSymbol("UART_NVIC_INTERRUPT_NAME", None)
    uart_NVIC_InterruptName.setDefaultValue(interruptName)
    uart_NVIC_InterruptName.setDependencies(nvicInterruptNameUpdate, ["UART_INTERRUPT_TYPE"])
    uart_NVIC_InterruptName.setVisible(False)

    uart_NVIC_Update = uartComponent.createBooleanSymbol("UART_UPDATE_NVIC_INTERRUPT", None)
    uart_NVIC_Update.setDependencies(nvicInterruptUpdate, ["UART_OPERATING_MODE", "UART_INTERRUPT_TYPE"])
    uart_NVIC_Update.setVisible(False)
    

    ## Enable NVIC interrupt if non-blocking or ring buffer mode is enabled
    setUARTInterruptData(uart_NVIC_InterruptName.getValue(), uartSym_OperatingMode.getSelectedKey() != "BLOCKING")

    ############################################################################
    #### UART Registers ####
    ############################################################################

    uartRegLCR = uartComponent.createHexSymbol("UART_REG_LCR", None)
    uartRegLCR.setLabel("Line Control Register")
    uartRegLCR.setDefaultValue(0x03)                                       # 8-bit mode is default
    uartRegLCR.setVisible(False)
    uartRegLCR.setDependencies(regLCRUpdate, uartLCRRegDepList)

    getBaudMSB(int(uartBaudRateDiv.getValue()), uart_CFG_SEL_CLK_SRC_SELECT.getSelectedValue(), int(uartValGrp_UART_BAUDRT_MSB__BAUD_CLK_SEL.getSelectedValue()))

    uartRegBaudGenMSB = uartComponent.createHexSymbol("UART_REG_BAUD_GEN_MSB", None)
    uartRegBaudGenMSB.setLabel("Baud Generator MSB")
    uartRegBaudGenMSB.setDefaultValue(0x00)
    uartRegBaudGenMSB.setVisible(False)
    uartRegBaudGenMSB.setDependencies(regBaudGenMSBUpdate, ["UART_BAUDRATE_DIVISOR", "UART_CFG_SEL_CLK_SRC", "UART_BAUDRT_MSB_BAUD_CLK_SEL" ])

    
    uartRegBaudGenLSB = uartComponent.createHexSymbol("UART_REG_BAUD_GEN_LSB", None)
    uartRegBaudGenLSB.setLabel("Baud Generator LSB")
    uartRegBaudGenLSB.setDefaultValue(int(uartBaudRateDiv.getValue()) & 0xFF)
    uartRegBaudGenLSB.setVisible(False)
    uartRegBaudGenLSB.setDependencies(regBaudGenLSBUpdate, ["UART_BAUDRATE_DIVISOR"])

    uartRegConfigSel = uartComponent.createHexSymbol("UART_REG_CONFIG_SEL", None)
    uartRegConfigSel.setLabel("Configuration Select")
    uartRegConfigSel.setDefaultValue(0x00)
    uartRegConfigSel.setVisible(False)
    uartRegConfigSel.setDependencies(configSelUpdate, ["UART_CFG_SEL_CLK_SRC", "UART_CFG_SEL_POLARITY"])

    #USART API Prefix
    uartSym_API_Prefix = uartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    uartSym_API_Prefix.setDefaultValue(uartInstanceName.getValue())
    uartSym_API_Prefix.setVisible(False)

    #UART Stop 1-bit Mask
    uartStopBit_1_Mask = uartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    uartStopBit_1_Mask.setDefaultValue("0x0")
    uartStopBit_1_Mask.setVisible(False)
    
    #UART Stop 1-bit Mask
    uartStopBit_1_5_Mask = uartComponent.createStringSymbol("USART_STOP_1_5_BIT_MASK", None)
    uartStopBit_1_5_Mask.setDefaultValue("0x4")
    uartStopBit_1_5_Mask.setVisible(False)

    #UART Stop 2-bit Mask
    uartStopBit_2_Mask = uartComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
    uartStopBit_2_Mask.setDefaultValue("0x4")
    uartStopBit_2_Mask.setVisible(False)

    #UART EVEN Parity Mask
    uartSym_MR_PAR_EVEN_Mask = uartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    uartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x10")
    uartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #UART ODD Parity Mask
    uartSym_MR_PAR_ODD_Mask = uartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    uartSym_MR_PAR_ODD_Mask.setDefaultValue("0x0")
    uartSym_MR_PAR_ODD_Mask.setVisible(False)

    #UART NO Parity Mask
    uartSym_MR_PAR_NO_Mask = uartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    uartSym_MR_PAR_NO_Mask.setDefaultValue("0x0")
    uartSym_MR_PAR_NO_Mask.setVisible(False)
    
    #USART Character Size 5 Mask
    usartSym_CTRLB_CHSIZE_5_Mask = uartComponent.createStringSymbol("USART_DATA_5_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_5_Mask.setDefaultValue("0x0")
    usartSym_CTRLB_CHSIZE_5_Mask.setVisible(False)
    
    #USART Character Size 6 Mask
    usartSym_CTRLB_CHSIZE_6_Mask = uartComponent.createStringSymbol("USART_DATA_6_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_6_Mask.setDefaultValue("0x1")
    usartSym_CTRLB_CHSIZE_6_Mask.setVisible(False)
    
    #USART Character Size 7 Mask
    usartSym_CTRLB_CHSIZE_7_Mask = uartComponent.createStringSymbol("USART_DATA_7_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_7_Mask.setDefaultValue("0x2")
    usartSym_CTRLB_CHSIZE_7_Mask.setVisible(False)

    #USART Character Size 8 Mask
    usartSym_CTRLB_CHSIZE_8_Mask = uartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_8_Mask.setDefaultValue("0x3")
    usartSym_CTRLB_CHSIZE_8_Mask.setVisible(False)

    #USART Overrun error Mask
    usartSym_STATUS_BUFOVF_Mask = uartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    usartSym_STATUS_BUFOVF_Mask.setDefaultValue("0x2")
    usartSym_STATUS_BUFOVF_Mask.setVisible(False)

    #USART parity error Mask
    usartSym_STATUS_PERR_Mask = uartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    usartSym_STATUS_PERR_Mask.setDefaultValue("0x4")
    usartSym_STATUS_PERR_Mask.setVisible(False)

    #USART framing error Mask
    usartSym_STATUS_FERR_Mask = uartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    usartSym_STATUS_FERR_Mask.setDefaultValue("0x8")
    usartSym_STATUS_FERR_Mask.setVisible(False)    
    
    uartSym_DataBits = uartComponent.createStringSymbol("USART_DATA_BITS", None)
    uartSym_DataBits.setDefaultValue("DRV_USART_DATA_8_BIT")
    uartSym_DataBits.setVisible(False)
    uartSym_DataBits.setDependencies(updateUSARTDataBits, ["UART_LCR_WORD_LENGTH_SELECT"])

    uartSymIRQName = uartComponent.createStringSymbol("SINGLE_IRQn", None)
    uartSymIRQName.setDefaultValue("UART" + uartInstanceNum.getValue() + "_IRQn")
    uartSymIRQName.setVisible(False)
    uartSymIRQName.setDependencies(irqn_update, ["UART_INTERRUPT_TYPE"])
    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    uartHeaderFile = uartComponent.createFileSymbol("UART_COMMON_HEADER", None)
    uartHeaderFile.setSourcePath("../peripheral/uart_39/templates/plib_uart_common.h")
    uartHeaderFile.setOutputName("plib_uart_common.h")
    uartHeaderFile.setDestPath("peripheral/uart/")
    uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeaderFile.setType("HEADER")
    uartHeaderFile.setMarkup(False)
    uartHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeader1File.setSourcePath("../peripheral/uart_39/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)
    uartHeader1File.setDependencies(UARTFileGeneration, ["UART_OPERATING_MODE"])

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE", None)
    uartSource1File.setSourcePath("../peripheral/uart_39/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)
    uartSource1File.setDependencies(UARTFileGeneration, ["UART_OPERATING_MODE"])

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_39/templates/system/initialization.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_39/templates/system/definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)