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

################################################################################
#### Register Information ####
################################################################################
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

    return result_dict

##UXMODE
uartValGrp_U1MODE_STSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__STSEL"]')
uartBitField_U1MODE_STSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="STSEL"]')

uartValGrp_U1MODE_PDSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__PDSEL"]')
uartBitField_U1MODE_PDSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="PDSEL"]')

uartValGrp_U1MODE_BRGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__BRGH"]')
uartBitField_U1MODE_BRGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="BRGH"]')

uartValGrp_U1MODE_RXINV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__RXINV"]')
uartBitField_U1MODE_RXINV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="RXINV"]')

uartValGrp_U1MODE_ABAUD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__ABAUD"]')
uartBitField_U1MODE_ABAUD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="ABAUD"]')

uartValGrp_U1MODE_LPBACK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__LPBACK"]')
uartBitField_U1MODE_LPBACK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="LPBACK"]')

uartValGrp_U1MODE_WAKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__WAKE"]')
uartBitField_U1MODE_WAKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="WAKE"]')

uartValGrp_U1MODE_UEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__UEN"]')
uartBitField_U1MODE_UEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="UEN"]')

uartValGrp_U1MODE_RTMSD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__RTSMD"]')
uartBitField_U1MODE_RTMSD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="RTSMD"]')

uartValGrp_U1MODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__IREN"]')
uartBitField_U1MODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="IREN"]')

uartValGrp_U1MODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__SIDL"]')
uartBitField_U1MODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="SIDL"]')

uartValGrp_U1MODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__ON"]')
uartBitField_U1MODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="ON"]')

################################################################################
#### Global Variables ####
################################################################################

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################


def setUARTInterruptData(status):

    for id in InterruptVector:
        Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandlerLock:
        Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandler:
        interruptName = id.split("_INTERRUPT_HANDLER")[0]
        if status == True:
            Database.setSymbolValue("core", id, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", id, interruptName + "_Handler", 1)

def updateUARTInterruptData(symbol, event):

    if event["id"] == "UART_INTERRUPT_MODE_ENABLE":
        setUARTInterruptData(event["value"])

    status = False

    for id in InterruptVectorUpdate:
        id = id.replace("core.", "")
        if Database.getSymbolValue("core", id) == True:
            status = True
            break

    if uartSymInterruptModeEnable.getValue() == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    return regName

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

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
            outputList.append(dict)

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("irq-name"))
            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):

    vector_index = "-1"

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

# Calculates BRG value
def baudRateCalc(clk, baud):

    global uartSym_U1MODE_BRGH
    global uartSym_BaudPerError_Comment
    brgh0 = False
    brgh1 = False

    if clk == 0:
        uartSym_BaudError_Comment.setVisible(True)
        uartSym_U1MODE_BRGH.setValue(1, 2)
        return 0

    UxBRG_BRGH0 = (((clk >> 4) + (baud >> 1)) / baud) - 1
    UxBRG_BRGH1 = (((clk >> 2) + (baud >> 1)) / baud) - 1

    if ((UxBRG_BRGH0 >= 0) and (UxBRG_BRGH0 <= 65535)):
        brgh0 = True
    if ((UxBRG_BRGH1 >= 0) and (UxBRG_BRGH1 <= 65535)):
        brgh1 = True

    # Baud rate is not possible with either BRGH=0 or BRGH=1
    if brgh0 == False and brgh1 == False:
        uartSym_BaudError_Comment.setVisible(True)
        uartSym_U1MODE_BRGH.setValue(1, 2)
        return UxBRG_BRGH0

    # Baud rate is possible with both BRGH = 0 and BRGH = 1. Decide which one to use based on error.
    if brgh0 == True and brgh1 == True:
        actualBaud_BRGH0 = (clk/(16*(UxBRG_BRGH0 + 1)))
        actualBaud_BRGH1 = (clk/(4*(UxBRG_BRGH1 + 1)))

        error_BRGH0 = ((actualBaud_BRGH0 - baud)/float(baud))*100.0
        error_BRGH1 = ((actualBaud_BRGH1 - baud)/float(baud))*100.0

        # If error with BRGH0 is less or same as with BRGH1, use BRGH0
        if (abs(error_BRGH0) <= abs(error_BRGH1)):
            uartSym_U1MODE_BRGH.setValue(1, 2)
            uartSym_BaudPerError_Comment.setLabel("*** Baud Error = " + "{:.4f}".format(error_BRGH0) + " % ***")
            return UxBRG_BRGH0
        # If error with BRGH1 is less, use BRGH1
        else:
            uartSym_U1MODE_BRGH.setValue(0, 2)
            uartSym_BaudPerError_Comment.setLabel("*** Baud Error = " + "{:.4f}".format(error_BRGH1)  + " % ***")
            return UxBRG_BRGH1
    else:
        if brgh0 == True:
            uartSym_U1MODE_BRGH.setValue(1, 2)
            uartSym_BaudPerError_Comment.setLabel("*** Baud Error = " + "{:.4f}".format(error_BRGH0)  + " % ***")
            return UxBRG_BRGH0
        elif brgh1 == True:
            uartSym_U1MODE_BRGH.setValue(0, 2)
            uartSym_BaudPerError_Comment.setLabel("*** Baud Error = " + "{:.4f}".format(error_BRGH1)  + " % ***")
            return UxBRG_BRGH1

def baudRateTrigger(symbol, event):

    localComponent = symbol.getComponent()
    clk = int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    baud = int(localComponent.getSymbolByID("BAUD_RATE").getValue())
    brgh = int(localComponent.getSymbolByID("UART_BRGH").getSelectedValue())

    UxBRG_BRGH = 0
    actualBaud = 0

    if brgh == 0:
        UxBRG_BRGH = (((clk >> 4) + (baud >> 1)) / baud) - 1
        if UxBRG_BRGH > 0:
            actualBaud = (clk/(16*(UxBRG_BRGH + 1)))
    else:
        UxBRG_BRGH = (((clk >> 2) + (baud >> 1)) / baud) - 1
        if UxBRG_BRGH > 0:
            actualBaud = (clk/(4*(UxBRG_BRGH + 1)))

    per_error = ((actualBaud - baud)/float(baud))*100.0

    per_error_comment_sym = localComponent.getSymbolByID("UART_BAUD_PER_ERROR_COMMENT")
    per_error_comment_sym.setLabel("*** Baud Error = " + "{:.4f}".format(per_error) + " % ***")

    if ((UxBRG_BRGH >= 0) and (UxBRG_BRGH <= 65535)):
        uartSym_BaudError_Comment.setVisible(False)
    else:
        if UxBRG_BRGH < 0:
            UxBRG_BRGH = 0
        else:
            UxBRG_BRGH = 65535
        uartSym_BaudError_Comment.setVisible(True)

    symbol.setValue(UxBRG_BRGH, 2)

def clockSourceFreq(symbol, event):

    symbol.setValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def u1ModecombineValues(symbol, event):

    uart1modeValue = symbol.getValue()

    if event["id"] == "UART_STOPBIT_SELECT":
        stselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_STSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (stselValue << 0)

    if event["id"] == "UART_PDBIT_SELECT":
        pdselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_PDSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (pdselValue << 1)

    if event["id"] == "UART_BRGH":
        brghValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_BRGH.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (brghValue << 3)

    if event["id"] == "UART_UEN_SELECT":
        uenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_UEN.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (uenValue << 8)


    symbol.setValue(uart1modeValue, 2)

def uartBRGHModeInfo(symbol, event):

    if event["value"] == 1:
        symbol.setLabel("*** Standard Speed mode 16x baud clock enabled (BRGH = 0) ***")
    else:
        symbol.setLabel("*** High Speed mode 4x baud clock enabled (BRGH = 1) ***")

def updateUARTClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def updateSymbolVisibility(symbol, event):

    # Enable TX and RX ring buffer size option if Ring buffer is enabled.
    symbol.setVisible(event["value"])

def UARTFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = event["value"]

    if componentID == "UART_HEADER":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_00734/templates/plib_uart_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/uart_00734/templates/plib_uart.h.ftl"
    elif componentID == "UART_SOURCE":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_00734/templates/plib_uart_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/uart_00734/templates/plib_uart.c.ftl"

    symbol.setSourcePath(filepath)

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def updateAutoAddrSymVisibility(symbol, event):
    pdbit_mode = event["source"].getSymbolByID("UART_PDBIT_SELECT").getSelectedValue()

    if pdbit_mode == "3":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        symbol.setReadOnly(True)
        symbol.setValue(False)
        symbol.setReadOnly(False)

def updateAddrSymVisibility(symbol, event):
    pdbit_mode = event["source"].getSymbolByID("UART_PDBIT_SELECT").getSelectedValue()
    addr_detection_enable = event["source"].getSymbolByID("UART_AUTOMATIC_ADDR_DETECTION_ENABLE").getValue()

    symbol.setVisible(pdbit_mode == "3" and addr_detection_enable == True)

def updateUSARTDataBits (symbol, event):
    symbol.setValue("DRV_USART_DATA_9_BIT" if (event["value"] == 0) else "DRV_USART_DATA_8_BIT")

def updateInterruptMode (symbol, event):
    if symbol.getLabel() != "---":
        usartOperatingModeSym = event["source"].getSymbolByID("UART_OPERATING_MODE")
        if event["value"] == True and usartOperatingModeSym.getSelectedKey() != "RING_BUFFER" :
            usartOperatingModeSym.setSelectedKey("NON_BLOCKING")
        elif event["value"] == False:
            usartOperatingModeSym.setSelectedKey("BLOCKING")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateRingBufferMode (symbol, event):
    if symbol.getLabel() != "---":
        if event["value"] == True:
            event["source"].getSymbolByID("UART_OPERATING_MODE").setSelectedKey("RING_BUFFER")
        symbol.setLabel("---")
        symbol.setVisible(False)

def updateOperatingMode (symbol, event):
    interruptModeSym = event["source"].getSymbolByID("UART_INTERRUPT_MODE_ENABLE")
    ringBufferModeSym = event["source"].getSymbolByID("UART_RING_BUFFER_MODE_ENABLE")
    if symbol.getSelectedKey() == "RING_BUFFER":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(True)
    elif symbol.getSelectedKey() == "NON_BLOCKING":
        interruptModeSym.setValue(True)
        ringBufferModeSym.setValue(False)
    elif symbol.getSelectedKey() == "BLOCKING":
        interruptModeSym.setValue(False)
        ringBufferModeSym.setValue(False)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(uartComponent):

    global uartInstanceName
    global uartSym_U1MODE_BRGH
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global InterruptVectorUpdate
    global uartSymInterruptModeEnable
    global uartSym_BaudError_Comment
    global uartSym_BaudPerError_Comment
    global uartSym_RingBufferMode_Enable
    global uartSym_OperatingMode

    InterruptVector = []
    InterruptHandler = []
    InterruptHandlerLock = []
    InterruptVectorUpdate = []

    uartInstanceName = uartComponent.createStringSymbol("UART_INSTANCE_NAME", None)
    uartInstanceName.setVisible(False)
    uartInstanceName.setDefaultValue(uartComponent.getID().upper())
    Log.writeInfoMessage("Running " + uartInstanceName.getValue())

    uartInstanceNum = uartComponent.createStringSymbol("UART_INSTANCE_NUM", None)
    uartInstanceNum.setVisible(False)
    componentName = str(uartComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    uartInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

# Depricated symbols ---------------------------------------------------------------------------------------------------
    # Enable Interrupts?
    uartSymInterruptMode = uartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    uartSymInterruptMode.setLabel("Enable Interrrupts ?")
    uartSymInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSymInterruptMode.setDefaultValue(True)
    uartSymInterruptMode.setVisible(False)
    uartSymInterruptMode.setReadOnly(True)
    uartSymInterruptMode.setDependencies(updateInterruptMode, ["USART_INTERRUPT_MODE"])

    #Enable Ring buffer?
    uartSym_RingBuffer_Enable = uartComponent.createBooleanSymbol("UART_RING_BUFFER_ENABLE", None)
    uartSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
    uartSym_RingBuffer_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_RingBuffer_Enable.setDefaultValue(False)
    uartSym_RingBuffer_Enable.setVisible(False)
    uartSym_RingBuffer_Enable.setReadOnly(True)
    uartSym_RingBuffer_Enable.setDependencies(updateRingBufferMode, ["UART_RING_BUFFER_ENABLE"])
# Depricated symbols ---------------------------------------------------------------------------------------------------

    # Enable Interrupts?
    uartSymInterruptModeEnable = uartComponent.createBooleanSymbol("UART_INTERRUPT_MODE_ENABLE", None)
    uartSymInterruptModeEnable.setLabel("Enable Interrrupts ?")
    uartSymInterruptModeEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSymInterruptModeEnable.setDefaultValue(True)
    uartSymInterruptModeEnable.setReadOnly(True)
    uartSymInterruptModeEnable.setVisible(False)

    #Enable Ring buffer?
    uartSym_RingBufferMode_Enable = uartComponent.createBooleanSymbol("UART_RING_BUFFER_MODE_ENABLE", None)
    uartSym_RingBufferMode_Enable.setLabel("Enable Ring Buffer ?")
    uartSym_RingBufferMode_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_RingBufferMode_Enable.setDefaultValue(False)
    uartSym_RingBufferMode_Enable.setReadOnly(True)
    uartSym_RingBufferMode_Enable.setVisible(False)

    uartSym_OperatingMode = uartComponent.createKeyValueSetSymbol("UART_OPERATING_MODE", None)
    uartSym_OperatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_OperatingMode.setLabel("Operating Mode")
    uartSym_OperatingMode.addKey("BLOCKING", "0", "Blocking mode")
    uartSym_OperatingMode.addKey("NON_BLOCKING", "1", "Non-blocking mode")
    uartSym_OperatingMode.addKey("RING_BUFFER", "2", "Ring buffer mode")
    uartSym_OperatingMode.setDefaultValue(1)
    uartSym_OperatingMode.setDisplayMode("Description")
    uartSym_OperatingMode.setOutputMode("Key")
    uartSym_OperatingMode.setVisible(True)
    uartSym_OperatingMode.setDependencies(updateOperatingMode, ["UART_OPERATING_MODE"])

    uartSym_RingBufferSizeConfig = uartComponent.createCommentSymbol("UART_RING_BUFFER_SIZE_CONFIG", None)
    uartSym_RingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
    uartSym_RingBufferSizeConfig.setVisible(False)
    uartSym_RingBufferSizeConfig.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSym_TXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_TX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_TXRingBuffer_Size.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    uartSym_TXRingBuffer_Size.setMin(2)
    uartSym_TXRingBuffer_Size.setMax(65535)
    uartSym_TXRingBuffer_Size.setDefaultValue(128)
    uartSym_TXRingBuffer_Size.setVisible(False)
    uartSym_TXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSym_RXRingBuffer_Size = uartComponent.createIntegerSymbol("UART_RX_RING_BUFFER_SIZE", uartSym_RingBufferSizeConfig)
    uartSym_RXRingBuffer_Size.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    uartSym_RXRingBuffer_Size.setMin(2)
    uartSym_RXRingBuffer_Size.setMax(65535)
    uartSym_RXRingBuffer_Size.setDefaultValue(128)
    uartSym_RXRingBuffer_Size.setVisible(False)
    uartSym_RXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartIrq = "UART_" + uartInstanceNum.getValue()
    uartVectorNum = getVectorIndex(uartIrq)

    if uartVectorNum != "-1":
        InterruptVector.append(uartIrq + "_INTERRUPT_ENABLE")
        InterruptHandler.append(uartIrq + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(uartIrq + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + uartIrq + "_INTERRUPT_ENABLE_UPDATE")

        ## UART Error IRQ
        uartIrqFault = uartInstanceName.getValue() + "_ERR"
        uartFaultVectorNum = int(getIRQIndex(uartIrqFault))

        ## UART RX IRQ
        uartIrqrRx = uartInstanceName.getValue() + "_RX"
        uartRxVectorNum = int(getIRQIndex(uartIrqrRx))

        ## UART TX IRQ
        uartIrqTx = uartInstanceName.getValue() + "_TX"
        uartTxVectorNum = int(getIRQIndex(uartIrqTx))
    else:
        ## UART Fault Interrrupt
        uartIrqFault = uartInstanceName.getValue() + "_FAULT"
        InterruptVector.append(uartIrqFault + "_INTERRUPT_ENABLE")
        InterruptHandler.append(uartIrqFault + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(uartIrqFault + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + uartIrqFault + "_INTERRUPT_ENABLE_UPDATE")
        uartFaultVectorNum = int(getVectorIndex(uartIrqFault))

        ## UART RX Interrupt
        uartIrqrRx = uartInstanceName.getValue() + "_RX"
        InterruptVector.append(uartIrqrRx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(uartIrqrRx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(uartIrqrRx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + uartIrqrRx + "_INTERRUPT_ENABLE_UPDATE")
        uartRxVectorNum = int(getVectorIndex(uartIrqrRx))

        ## UART TX Interrupt
        uartIrqTx = uartInstanceName.getValue() + "_TX"
        InterruptVector.append(uartIrqTx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(uartIrqTx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(uartIrqTx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + uartIrqTx + "_INTERRUPT_ENABLE_UPDATE")
        uartTxVectorNum = int(getVectorIndex(uartIrqTx))

    uartInterruptCount = uartComponent.createIntegerSymbol("UART_INTERRUPT_COUNT", None)
    uartInterruptCount.setDefaultValue(len(InterruptVector))
    uartInterruptCount.setVisible(False)

    urxenblRegName = _get_enblReg_parms(uartRxVectorNum)
    urxstatRegName = _get_statReg_parms(uartRxVectorNum)

    #IEC REG
    uartRXIEC = uartComponent.createStringSymbol("UART_RX_IEC_REG", None)
    uartRXIEC.setDefaultValue(urxenblRegName)
    uartRXIEC.setVisible(False)

    #IFS REG
    uartRXIFS = uartComponent.createStringSymbol("UART_RX_IFS_REG", None)
    uartRXIFS.setDefaultValue(urxstatRegName)
    uartRXIFS.setVisible(False)

    enblRegName = _get_enblReg_parms(uartFaultVectorNum)
    statRegName = _get_statReg_parms(uartFaultVectorNum)

    #IEC REG
    uartFaultIEC = uartComponent.createStringSymbol("UART_FAULT_IEC_REG", None)
    uartFaultIEC.setDefaultValue(enblRegName)
    uartFaultIEC.setVisible(False)

    #IFS REG
    uartFaultIFS = uartComponent.createStringSymbol("UART_FAULT_IFS_REG", None)
    uartFaultIFS.setDefaultValue(statRegName)
    uartFaultIFS.setVisible(False)

    utxenblRegName = _get_enblReg_parms(uartTxVectorNum)
    utxstatRegName = _get_statReg_parms(uartTxVectorNum)

    #IEC REG
    uartTXIEC = uartComponent.createStringSymbol("UART_TX_IEC_REG", None)
    uartTXIEC.setDefaultValue(utxenblRegName)
    uartTXIEC.setVisible(False)

    #IFS REG
    uartTXIFS = uartComponent.createStringSymbol("UART_TX_IFS_REG", None)
    uartTXIFS.setDefaultValue(utxstatRegName)
    uartTXIFS.setVisible(False)

    ##STOP Selection Bit
    stsel_names = []
    _get_bitfield_names(uartValGrp_U1MODE_STSEL, stsel_names)
    uartSym_U1MODE_STSEL = uartComponent.createKeyValueSetSymbol("UART_STOPBIT_SELECT", None)
    uartSym_U1MODE_STSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_U1MODE_STSEL.setLabel(uartBitField_U1MODE_STSEL.getAttribute("caption"))
    uartSym_U1MODE_STSEL.setDefaultValue(1)
    uartSym_U1MODE_STSEL.setOutputMode( "Value" )
    uartSym_U1MODE_STSEL.setDisplayMode( "Description" )
    for ii in stsel_names:
        uartSym_U1MODE_STSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    ##Parity and data Selection Bits
    pdsel_names = []
    _get_bitfield_names(uartValGrp_U1MODE_PDSEL, pdsel_names)
    uartSym_U1MODE_PDSEL = uartComponent.createKeyValueSetSymbol("UART_PDBIT_SELECT", None)
    uartSym_U1MODE_PDSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_U1MODE_PDSEL.setLabel (uartBitField_U1MODE_PDSEL.getAttribute("caption"))
    uartSym_U1MODE_PDSEL.setDefaultValue(3)
    uartSym_U1MODE_PDSEL.setOutputMode( "Value" )
    uartSym_U1MODE_PDSEL.setDisplayMode( "Description" )
    for ii in pdsel_names:
        uartSym_U1MODE_PDSEL.addKey( ii['key'],ii['value'], ii['desc'] )


    ##Automatic Address Detection Enable
    uartSym_AutoAddr_Enable = uartComponent.createBooleanSymbol("UART_AUTOMATIC_ADDR_DETECTION_ENABLE", None)
    uartSym_AutoAddr_Enable.setLabel("Enable Automatic Address Detection?")
    uartSym_AutoAddr_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_AutoAddr_Enable.setDefaultValue(False)
    uartSym_AutoAddr_Enable.setVisible(False)
    uartSym_AutoAddr_Enable.setDependencies(updateAutoAddrSymVisibility, ["UART_PDBIT_SELECT"])

    ##Address value
    uartSym_9BitMode_Addr = uartComponent.createIntegerSymbol("UART_9BIT_MODE_ADDR", None)
    uartSym_9BitMode_Addr.setLabel("Address")
    uartSym_9BitMode_Addr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_9BitMode_Addr.setMin(0)
    uartSym_9BitMode_Addr.setMax(255)
    uartSym_9BitMode_Addr.setDefaultValue(1)
    uartSym_9BitMode_Addr.setVisible(False)
    uartSym_9BitMode_Addr.setDependencies(updateAddrSymVisibility, ["UART_PDBIT_SELECT", "UART_AUTOMATIC_ADDR_DETECTION_ENABLE"])


    ##BRGH Selection Bit
    BRGH_names = []
    _get_bitfield_names(uartValGrp_U1MODE_BRGH, BRGH_names)
    uartSym_U1MODE_BRGH = uartComponent.createKeyValueSetSymbol("UART_BRGH", None)
    uartSym_U1MODE_BRGH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartSym_U1MODE_BRGH.setLabel(uartBitField_U1MODE_BRGH.getAttribute("caption"))
    uartSym_U1MODE_BRGH.setDefaultValue(1)
    uartSym_U1MODE_BRGH.setOutputMode( "Value" )
    uartSym_U1MODE_BRGH.setDisplayMode( "Description" )
    for ii in BRGH_names:
        uartSym_U1MODE_BRGH.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_U1MODE_BRGH.setVisible(True)

    ##UEN Selection Bit
    if uartBitField_U1MODE_UEN != None:
        uensel_caption = {
        "0" : "UxTX and UxRX pins are enabled and used; UxCTS and UxRTS/UxBCLK pins are controlled by corresponding bits in the PORTx register",
        "1" : "UxTX, UxRX and UxRTS pins are enabled and used; UxCTS pin is controlled by corresponding bits in the PORTx register",
        "2" : "UxTX, UxRX, UxCTS and UxRTS pins are enabled and used",
        "3" : "UxTX, UxRX and UxBCLK pins are enabled and used; UxCTS pin is controlled by corresponding bits in the PORTx register"
        }
        uensel_names = []
        _get_bitfield_names(uartValGrp_U1MODE_UEN, uensel_names)
        uartSym_U1MODE_UENEL = uartComponent.createKeyValueSetSymbol("UART_UEN_SELECT", None)
        uartSym_U1MODE_UENEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
        uartSym_U1MODE_UENEL.setLabel(uartBitField_U1MODE_UEN.getAttribute("caption"))
        uartSym_U1MODE_UENEL.setOutputMode( "Value" )
        uartSym_U1MODE_UENEL.setDisplayMode( "Description" )

        # Overwrite the key and description read from ATDF with the one from uensel_caption
        index = 0
        for ii in uensel_names:
            for jj in uensel_caption:
                if ii['value'] == jj:
                    ii['key'] = uensel_caption[jj]
                    ii['desc'] = uensel_caption[jj]
                    if ii['value'] == "0":
                        uartSym_U1MODE_UENEL.setDefaultValue(index)
            index += 1

        for ii in uensel_names:
            uartSym_U1MODE_UENEL.addKey( ii['key'],ii['value'], ii['desc'] )


    uartSym_U1MODE = uartComponent.createHexSymbol("UMODE_VALUE", None)    
    uartSym_U1MODE.setVisible(False)
    uartSym_U1MODE.setDependencies(u1ModecombineValues,["UART_STOPBIT_SELECT", "UART_PDBIT_SELECT", "UART_BRGH", "UART_UEN_SELECT"])

    ## UART Clock Frequency
    uartClkValue = uartComponent.createIntegerSymbol("UART_CLOCK_FREQ", None)
    uartClkValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartClkValue.setLabel("Clock Frequency")
    uartClkValue.setReadOnly(True)
    uartClkValue.setDefaultValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    uartClkValue.setDependencies(clockSourceFreq, ["core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    ## Baud Rate setting
    uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", None)
    uartBaud.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:uart_00734;register:%NOREGISTER%")
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(115200)



    ## Baud Rate Frequency dependency
    uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", None)
    uartBRGValue.setVisible(False)
    uartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "UART_BRGH", "core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    uartSym_BaudPerError_Comment = uartComponent.createCommentSymbol("UART_BAUD_PER_ERROR_COMMENT", None)

    #UART Baud Rate not supported comment
    uartSym_BaudError_Comment = uartComponent.createCommentSymbol("UART_BAUD_ERROR_COMMENT", None)
    uartSym_BaudError_Comment.setLabel("********** UART Clock source value is low for the desired baud rate **********")
    uartSym_BaudError_Comment.setVisible(False)

    brgVal = baudRateCalc(uartClkValue.getValue(), uartBaud.getValue())
    #Use setValue instead of setDefaultValue to store symbol value in default.xml
    uartBRGValue.setValue(brgVal, 1)
    uartSym_U1MODE.setDefaultValue((int(uartSym_U1MODE_BRGH.getSelectedValue()) << 3) | (int(uartSym_U1MODE_PDSEL.getSelectedValue()) << 1) | (int(uartSym_U1MODE_STSEL.getSelectedValue()) << 0))

    ############################################################################
    #### Dependency ####
    ############################################################################

    ## EVIC Interrupt Dynamic settings
    setUARTInterruptData(uartSymInterruptModeEnable.getValue())

    uartSymIntEnComment = uartComponent.createCommentSymbol("UART_INTRRUPT_ENABLE_COMMENT", None)
    uartSymIntEnComment.setLabel("Warning!!! " + uartInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    uartSymIntEnComment.setVisible(False)
    uartSymIntEnComment.setDependencies(updateUARTInterruptData, ["UART_INTERRUPT_MODE_ENABLE"] + InterruptVectorUpdate)

    # Clock Warning status
    uartSym_ClkEnComment = uartComponent.createCommentSymbol("UART_CLOCK_ENABLE_COMMENT", None)
    uartSym_ClkEnComment.setLabel("Warning!!! " + uartInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    uartSym_ClkEnComment.setVisible(False)
    uartSym_ClkEnComment.setDependencies(updateUARTClockWarningStatus, ["core." + uartInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Driver Symbols ############################################
    ###################################################################################################

    #USART API Prefix
    usartSym_API_Prefix = uartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    usartSym_API_Prefix.setDefaultValue(uartInstanceName.getValue())
    usartSym_API_Prefix.setVisible(False)

    #UART Stop 1-bit Mask
    uartStopBit_1_Mask = uartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    uartStopBit_1_Mask.setDefaultValue("0x0")
    uartStopBit_1_Mask.setVisible(False)

    #UART Stop 2-bit Mask
    uartStopBit_2_Mask = uartComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
    uartStopBit_2_Mask.setDefaultValue("0x1")
    uartStopBit_2_Mask.setVisible(False)

    #UART EVEN Parity Mask
    uartSym_MR_PAR_EVEN_Mask = uartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    uartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x2")
    uartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #UART ODD Parity Mask
    uartSym_MR_PAR_ODD_Mask = uartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    uartSym_MR_PAR_ODD_Mask.setDefaultValue("0x4")
    uartSym_MR_PAR_ODD_Mask.setVisible(False)

    #UART NO Parity Mask
    uartSym_MR_PAR_NO_Mask = uartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    uartSym_MR_PAR_NO_Mask.setDefaultValue("0x0")
    uartSym_MR_PAR_NO_Mask.setVisible(False)

    #USART Character Size 8 Mask
    usartSym_CTRLB_CHSIZE_8_Mask = uartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_8_Mask.setDefaultValue("0x0")
    usartSym_CTRLB_CHSIZE_8_Mask.setVisible(False)

    #USART Character Size 9 Mask
    usartSym_CTRLB_CHSIZE_9_Mask = uartComponent.createStringSymbol("USART_DATA_9_BIT_MASK", None)
    usartSym_CTRLB_CHSIZE_9_Mask.setDefaultValue("0x6")
    usartSym_CTRLB_CHSIZE_9_Mask.setVisible(False)

    #USART Overrun error Mask
    usartSym_STATUS_BUFOVF_Mask = uartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    usartSym_STATUS_BUFOVF_Mask.setDefaultValue("0x2")
    usartSym_STATUS_BUFOVF_Mask.setVisible(False)

    #USART parity error Mask
    usartSym_STATUS_PERR_Mask = uartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    usartSym_STATUS_PERR_Mask.setDefaultValue("0x8")
    usartSym_STATUS_PERR_Mask.setVisible(False)

    #USART framing error Mask
    usartSym_STATUS_FERR_Mask = uartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    usartSym_STATUS_FERR_Mask.setDefaultValue("0x4")
    usartSym_STATUS_FERR_Mask.setVisible(False)

    #uart Transmit data register
    uartSym_TxRegister = uartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    uartSym_TxRegister.setDefaultValue("&(U" + uartInstanceNum.getValue() + "TXREG)")
    uartSym_TxRegister.setVisible(False)

    #uart Receive data register
    uartSym_RxRegister = uartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    uartSym_RxRegister.setDefaultValue("&(U" + uartInstanceNum.getValue() + "RXREG)")
    uartSym_RxRegister.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    uartHeaderFile = uartComponent.createFileSymbol("UART_COMMON_HEADER", None)
    uartHeaderFile.setSourcePath("../peripheral/uart_00734/templates/plib_uart_common.h")
    uartHeaderFile.setOutputName("plib_uart_common.h")
    uartHeaderFile.setDestPath("peripheral/uart/")
    uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeaderFile.setType("HEADER")
    uartHeaderFile.setMarkup(False)
    uartHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeader1File.setSourcePath("../peripheral/uart_00734/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)
    uartHeader1File.setDependencies(UARTFileGeneration, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE", None)
    uartSource1File.setSourcePath("../peripheral/uart_00734/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)
    uartSource1File.setDependencies(UARTFileGeneration, ["UART_RING_BUFFER_MODE_ENABLE"])

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_00734/templates/system/initialization.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_00734/templates/system/definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)

    uartSym_DataBits = uartComponent.createStringSymbol("USART_DATA_BITS", None)
    uartSym_DataBits.setDefaultValue("DRV_USART_DATA_9_BIT" if (uartSym_U1MODE_PDSEL.getValue() == 0) else "DRV_USART_DATA_8_BIT")
    uartSym_DataBits.setVisible(False)
    uartSym_DataBits.setDependencies(updateUSARTDataBits, ["UART_PDBIT_SELECT"])