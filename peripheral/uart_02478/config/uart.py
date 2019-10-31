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

    if event["id"] == "USART_INTERRUPT_MODE":
        setUARTInterruptData(event["value"])

    status = False

    for id in InterruptVectorUpdate:
        id = id.replace("core.", "")
        if Database.getSymbolValue("core", id) == True:
            status = True
            break

    if uartSymInterruptMode.getValue() == True and status == True:
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

    global uartSym_UxMODE_BRGH

    brgValLow = ((clk / baud) >> 4) - 1
    brgValHigh = ((clk / baud) >> 2) - 1

    brgh  = int(uartSym_UxMODE_BRGH.getSelectedValue())
    uxmode = int (Database.getSymbolValue(uartInstanceName.getValue().lower(), "UMODE_VALUE"))

    # Check if the baud value can be set with low baud settings
    if((brgValHigh >= 0) and (brgValHigh <= 65535)) :
        brgValue =  (((clk >> 2) + (baud >> 1)) / baud ) - 1
        uartSym_UxMODE_BRGH.setValue(0, 2)
        brghBitL = int(uartSym_UxMODE_BRGH.getSelectedValue())
        return brgValue
    elif((brgValLow >= 0) and (brgValLow <= 65535)) :
        brgValue = (((clk >> 4) + (baud >> 1)) / baud) - 1
        uartSym_UxMODE_BRGH.setValue(1, 2)
        brghBitH = int(uartSym_UxMODE_BRGH.getSelectedValue())
        return brgValue
    elif brgValLow > 65535:
        return brgValLow
    else:
        return brgValLow

def baudRateTrigger(symbol, event):

    clk = int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    baud = int(Database.getSymbolValue(uartInstanceName.getValue().lower(), "BAUD_RATE"))

    brgVal = baudRateCalc(clk, baud)

    uartSym_BaudError_Comment.setVisible(False)

    if brgVal < 1:
        uartSym_BaudError_Comment.setVisible(True)
        return
    elif brgVal > 65535:
        brgVal = 65535
        uartSym_BaudError_Comment.setVisible(True)

    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):

    symbol.setValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def u1ModecombineValues(symbol, event):

    uart1modeValue = symbol.getValue()

    if event["id"] == "UART_STSEL":
        stselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_STSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (stselValue << 0)

    if event["id"] == "UART_PDSEL":
        pdselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_PDSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (pdselValue << 1)

    if event["id"] == "UART_BRGH":
        brghValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_BRGH.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (brghValue << 3)

    if event["id"] == "UART_RXINV":
        rxinvValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_RXINV.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (rxinvValue << 4)

    if event["id"] == "UART_ABAUD":
        abaudValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_ABAUD.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (abaudValue << 5)

    if event["id"] == "UART_LPBACK":
        lpbackValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_LPBACK.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (lpbackValue << 6)

    if event["id"] == "UART_WAKE":
        wakeValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_WAKE.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (wakeValue << 7)

    if event["id"] == "UART_RTSMD":
        rstmdValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_RTSMD.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (rstmdValue << 11)

    if event["id"] == "UART_IREN":
        irenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_IREN.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (irenValue << 12)

    if event["id"] == "UART_SIDL":
        sidlValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_SIDL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (sidlValue << 13)

    if event["id"] == "UART_RUNOVF":
        runovfValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_RUNOVF.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (runovfValue << 16)

    if event["id"] == "UART_CLKSEL":
        clkselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_CLKSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (clkselValue << 17)

    if event["id"] == "UART_SLPEN":
        slpenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_UxMODE_SLPEN.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (slpenValue << 23)

    symbol.setValue(uart1modeValue, 2)

def find_key_value(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.  This function is used with bitfield values for a given
    <value-group>, to set up default values for key value symbols.
    Arguments:
          value - the value to be looked for in the dictionary, a particular bitfield value to be found in 'keypairs'
          keypairs - the dictionary to be searched over, represents all bitfield values in a <value-group > to scanned over

    Without this helper function, setDefaultValue(<some_integer_value>) would not be very helpful for key/value symbols.
    Just inputting an integer value would require the user to see what order the bitfields are populated in the atdf file,
    to know what integer to use for setting a menu entry to a desired value.  This function removes the user requirement
    for figuring out what integer value should be used in order to get a particular bitfield value set by default.

    The (integer) value returned by this function call corresponds to the particular entry of the
    list that has the user-input key value.  The returned index value is dependent on the order
    of accumulation of bitfield entries from the atdf file.  This function removes that dependence by
    scanning the list (i.e., scans keypairs) for the particular key 'value' that matches what is being
    looked for, returning the element number for that (in the order it was scanned from the atdf file).

    The *.setDefaultValue( ) method that called this function will use that value to correctly populate
    the menu item.
    '''
    index = 0
    for ii in keypairs:
        if ii["value"] == str(value):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find value in dictionary") # should never get here
    return ""

def updateUARTClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################

def instantiateComponent(uartComponent):

    global uartInstanceName
    global uartSym_UxMODE_BRGH
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global InterruptVectorUpdate
    global uartSymInterruptMode
    global uartBitField_UxMODE_STSEL
    global uartBitField_UxMODE_PDSEL
    global uartBitField_UxMODE_BRGH
    global uartBitField_UxMODE_RXINV
    global uartBitField_UxMODE_ABAUD
    global uartBitField_UxMODE_LPBACK
    global uartBitField_UxMODE_WAKE
    global uartBitField_UxMODE_UEN
    global uartBitField_UxMODE_RTSMD
    global uartBitField_UxMODE_IREN
    global uartBitField_UxMODE_SIDL
    global uartBitField_UxMODE_ON
    global uartBitField_UxMODE_RUNOVF
    global uartBitField_UxMODE_CLKSEL
    global uartBitField_UxMODE_SLPEN
    global uartSym_BaudError_Comment

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

    ################################################################################
    #### Register Information ####
    ################################################################################

    # UxMODE Register
    uartValGrp_UxMODE_STSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__STSEL"]')
    uartBitField_UxMODE_STSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="STSEL"]')

    uartValGrp_UxMODE_PDSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__PDSEL"]')
    uartBitField_UxMODE_PDSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="PDSEL"]')

    uartValGrp_UxMODE_BRGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__BRGH"]')
    uartBitField_UxMODE_BRGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="BRGH"]')

    uartValGrp_UxMODE_RXINV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__RXINV"]')
    uartBitField_UxMODE_RXINV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="RXINV"]')

    uartValGrp_UxMODE_ABAUD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__ABAUD"]')
    uartBitField_UxMODE_ABAUD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="ABAUD"]')

    uartValGrp_UxMODE_LPBACK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__LPBACK"]')
    uartBitField_UxMODE_LPBACK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="LPBACK"]')

    uartValGrp_UxMODE_WAKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__WAKE"]')
    uartBitField_UxMODE_WAKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="WAKE"]')

    uartValGrp_UxMODE_UEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__UEN"]')
    uartBitField_UxMODE_UEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="UEN"]')

    uartValGrp_UxMODE_RTSMD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__RTSMD"]')
    uartBitField_UxMODE_RTSMD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="RTSMD"]')

    uartValGrp_UxMODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__IREN"]')
    uartBitField_UxMODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="IREN"]')

    uartValGrp_UxMODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__SIDL"]')
    uartBitField_UxMODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="SIDL"]')

    uartValGrp_UxMODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__ON"]')
    uartBitField_UxMODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="ON"]')

    uartValGrp_UxMODE_RUNOVF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__RUNOVF"]')
    uartBitField_UxMODE_RUNOVF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="RUNOVF"]')

    uartValGrp_UxMODE_CLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__CLKSEL"]')
    uartBitField_UxMODE_CLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="CLKSEL"]')

    uartValGrp_UxMODE_SLPEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U' + uartInstanceNum.getValue() + 'MODE__SLPEN"]')
    uartBitField_UxMODE_SLPEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U' + uartInstanceNum.getValue() + 'MODE"]/bitfield@[name="SLPEN"]')

    #Clock enable
    Database.setSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    uartSymInterruptMode = uartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    uartSymInterruptMode.setLabel("Enable Interrrupts ?")
    uartSymInterruptMode.setDefaultValue(True)

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

    #STSEL, STOP Selection Bit
    stsel_names = []
    _get_bitfield_names(uartValGrp_UxMODE_STSEL, stsel_names)
    uartSym_UxMODE_STSEL = uartComponent.createKeyValueSetSymbol("UART_STSEL", None)
    uartSym_UxMODE_STSEL.setLabel(uartBitField_UxMODE_STSEL.getAttribute("caption"))
    uartSym_UxMODE_STSEL.setDefaultValue(find_key_value(0, stsel_names)) # 1 stop bit
    uartSym_UxMODE_STSEL.setOutputMode( "Value" )
    uartSym_UxMODE_STSEL.setDisplayMode( "Description" )
    for ii in stsel_names:
        uartSym_UxMODE_STSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    #PDSEL, Parity and data Selection Bits
    pdsel_names = []
    _get_bitfield_names(uartValGrp_UxMODE_PDSEL, pdsel_names)
    uartSym_UxMODE_PDSEL = uartComponent.createKeyValueSetSymbol("UART_PDSEL", None)
    uartSym_UxMODE_PDSEL.setLabel (uartBitField_UxMODE_PDSEL.getAttribute("caption"))
    uartSym_UxMODE_PDSEL.setDefaultValue(find_key_value(0, pdsel_names)) # 8-bit data, no parity
    uartSym_UxMODE_PDSEL.setOutputMode( "Value" )
    uartSym_UxMODE_PDSEL.setDisplayMode( "Description" )
    for ii in pdsel_names:
        uartSym_UxMODE_PDSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    #BRGH, BRGH Selection Bit
    BRGH_names = []
    _get_bitfield_names(uartValGrp_UxMODE_BRGH, BRGH_names)
    uartSym_UxMODE_BRGH = uartComponent.createKeyValueSetSymbol("UART_BRGH", None)
    uartSym_UxMODE_BRGH.setLabel(uartBitField_UxMODE_BRGH.getAttribute("caption"))
    uartSym_UxMODE_BRGH.setDefaultValue(find_key_value(0, BRGH_names)) # standard speed mode
    uartSym_UxMODE_BRGH.setOutputMode( "Value" )
    uartSym_UxMODE_BRGH.setDisplayMode( "Description" )
    for ii in BRGH_names:
        uartSym_UxMODE_BRGH.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_UxMODE_BRGH.setReadOnly(True)

    #RXINV, Rx polarity inversion bit
    RXINV_names = []
    _get_bitfield_names(uartValGrp_UxMODE_RXINV, RXINV_names)
    uartSym_UxMODE_RXINV = uartComponent.createKeyValueSetSymbol("UART_RXINV", None)
    uartSym_UxMODE_RXINV.setLabel(uartBitField_UxMODE_RXINV.getAttribute("caption"))
    uartSym_UxMODE_RXINV.setDefaultValue(find_key_value(0, RXINV_names)) # standard speed mode
    uartSym_UxMODE_RXINV.setOutputMode( "Value" )
    uartSym_UxMODE_RXINV.setDisplayMode( "Description" )
    uartSym_UxMODE_RXINV.setVisible(False)
    for ii in RXINV_names:
        uartSym_UxMODE_RXINV.addKey( ii['key'],ii['value'], ii['desc'] )

    #ABAUD, Auto-baud enable bit
    ABAUD_names = []
    _get_bitfield_names(uartValGrp_UxMODE_ABAUD, ABAUD_names)
    uartSym_UxMODE_ABAUD = uartComponent.createKeyValueSetSymbol("UART_ABAUD", None)
    uartSym_UxMODE_ABAUD.setLabel(uartBitField_UxMODE_ABAUD.getAttribute("caption"))
    uartSym_UxMODE_ABAUD.setDefaultValue(find_key_value(0, ABAUD_names)) # baud rate measurement disabled
    uartSym_UxMODE_ABAUD.setOutputMode( "Value" )
    uartSym_UxMODE_ABAUD.setDisplayMode( "Description" )
    uartSym_UxMODE_ABAUD.setVisible(False)
    for ii in ABAUD_names:
        uartSym_UxMODE_ABAUD.addKey( ii['key'],ii['value'], ii['desc'] )

    #LPBACK, Loopback Mode Select bit
    LPBACK_names = []
    _get_bitfield_names(uartValGrp_UxMODE_LPBACK, LPBACK_names)
    uartSym_UxMODE_LPBACK = uartComponent.createKeyValueSetSymbol("UART_LPBACK", None)
    uartSym_UxMODE_LPBACK.setLabel(uartBitField_UxMODE_LPBACK.getAttribute("caption"))
    uartSym_UxMODE_LPBACK.setDefaultValue(find_key_value(0, LPBACK_names)) # loopback mode disabled
    uartSym_UxMODE_LPBACK.setOutputMode( "Value" )
    uartSym_UxMODE_LPBACK.setDisplayMode( "Description" )
    uartSym_UxMODE_LPBACK.setVisible(False)
    for ii in LPBACK_names:
        uartSym_UxMODE_LPBACK.addKey( ii['key'],ii['value'], ii['desc'] )

    #WAKE, Enable Wake-up on Start bit Detect During Sleep Mode bit
    WAKE_names = []
    _get_bitfield_names(uartValGrp_UxMODE_WAKE, WAKE_names)
    uartSym_UxMODE_WAKE = uartComponent.createKeyValueSetSymbol("UART_WAKE", None)
    uartSym_UxMODE_WAKE.setLabel(uartBitField_UxMODE_WAKE.getAttribute("caption"))
    uartSym_UxMODE_WAKE.setDefaultValue(find_key_value(0, WAKE_names)) # wake-up disabled
    uartSym_UxMODE_WAKE.setOutputMode( "Value" )
    uartSym_UxMODE_WAKE.setDisplayMode( "Description" )
    uartSym_UxMODE_WAKE.setVisible(False)
    for ii in WAKE_names:
        uartSym_UxMODE_WAKE.addKey( ii['key'],ii['value'], ii['desc'] )

    #RTSMD, Mode Selection for UxRTS Pin bit
    RTSMD_names = []
    _get_bitfield_names(uartValGrp_UxMODE_RTSMD, RTSMD_names)
    uartSym_UxMODE_RTSMD = uartComponent.createKeyValueSetSymbol("UART_RTSMD", None)
    uartSym_UxMODE_RTSMD.setLabel(uartBitField_UxMODE_RTSMD.getAttribute("caption"))
    uartSym_UxMODE_RTSMD.setDefaultValue(find_key_value(0, RTSMD_names)) # /UxRTS pin is in Flow Control mode
    uartSym_UxMODE_RTSMD.setOutputMode( "Value" )
    uartSym_UxMODE_RTSMD.setDisplayMode( "Description" )
    uartSym_UxMODE_RTSMD.setVisible(False)
    for ii in RTSMD_names:
        uartSym_UxMODE_RTSMD.addKey( ii['key'],ii['value'], ii['desc'] )

    #IREN, IrDA Encoder and Decoder Enable bit
    IREN_names = []
    _get_bitfield_names(uartValGrp_UxMODE_IREN, IREN_names)
    uartSym_UxMODE_IREN = uartComponent.createKeyValueSetSymbol("UART_IREN", None)
    uartSym_UxMODE_IREN.setLabel(uartBitField_UxMODE_IREN.getAttribute("caption"))
    uartSym_UxMODE_IREN.setDefaultValue(find_key_value(0, IREN_names)) # IrDA is disabled
    uartSym_UxMODE_IREN.setOutputMode( "Value" )
    uartSym_UxMODE_IREN.setDisplayMode( "Description" )
    uartSym_UxMODE_IREN.setVisible(False)
    for ii in IREN_names:
        uartSym_UxMODE_IREN.addKey( ii['key'],ii['value'], ii['desc'] )

    #SIDL, Stop in Idle Mode bit
    SIDL_names = []
    _get_bitfield_names(uartValGrp_UxMODE_SIDL, SIDL_names)
    uartSym_UxMODE_SIDL = uartComponent.createKeyValueSetSymbol("UART_SIDL", None)
    uartSym_UxMODE_SIDL.setLabel(uartBitField_UxMODE_SIDL.getAttribute("caption"))
    uartSym_UxMODE_SIDL.setDefaultValue(find_key_value(0, SIDL_names)) # continue operation in idle mode
    uartSym_UxMODE_SIDL.setOutputMode( "Value" )
    uartSym_UxMODE_SIDL.setDisplayMode( "Description" )
    uartSym_UxMODE_SIDL.setVisible(False)
    for ii in SIDL_names:
        uartSym_UxMODE_SIDL.addKey( ii['key'],ii['value'], ii['desc'] )

    #RUNOVF, Run During Overflow Condition Mode bit
    RUNOVF_names = []
    _get_bitfield_names(uartValGrp_UxMODE_RUNOVF, RUNOVF_names)
    uartSym_UxMODE_RUNOVF = uartComponent.createKeyValueSetSymbol("UART_RUNOVF", None)
    uartSym_UxMODE_RUNOVF.setLabel(uartBitField_UxMODE_RUNOVF.getAttribute("caption"))
    uartSym_UxMODE_RUNOVF.setDefaultValue(find_key_value(0, RUNOVF_names)) # shift register stops during overflow
    uartSym_UxMODE_RUNOVF.setOutputMode( "Value" )
    uartSym_UxMODE_RUNOVF.setDisplayMode( "Description" )
    uartSym_UxMODE_RUNOVF.setVisible(False)
    for ii in RUNOVF_names:
        uartSym_UxMODE_RUNOVF.addKey( ii['key'],ii['value'], ii['desc'] )

    #CLKSEL, UARTx Module Clock Selection bits
    CLKSEL_names = []
    _get_bitfield_names(uartValGrp_UxMODE_CLKSEL, CLKSEL_names)
    uartSym_UxMODE_CLKSEL = uartComponent.createKeyValueSetSymbol("UART_CLKSEL", None)
    uartSym_UxMODE_CLKSEL.setLabel(uartBitField_UxMODE_CLKSEL.getAttribute("caption"))
    uartSym_UxMODE_CLKSEL.setDefaultValue(find_key_value(0, CLKSEL_names)) # BRG clock is PBCLK2
    uartSym_UxMODE_CLKSEL.setOutputMode( "Value" )
    uartSym_UxMODE_CLKSEL.setDisplayMode( "Description" )
    for ii in CLKSEL_names:
        uartSym_UxMODE_CLKSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    #SLPEN, Run During Sleep Enable bit
    SLPEN_names = []
    _get_bitfield_names(uartValGrp_UxMODE_SLPEN, SLPEN_names)
    uartSym_UxMODE_SLPEN = uartComponent.createKeyValueSetSymbol("UART_SLPEN", None)
    uartSym_UxMODE_SLPEN.setLabel(uartBitField_UxMODE_SLPEN.getAttribute("caption"))
    uartSym_UxMODE_SLPEN.setDefaultValue(find_key_value(0, SLPEN_names)) # BRG clock off during sleep mode
    uartSym_UxMODE_SLPEN.setOutputMode( "Value" )
    uartSym_UxMODE_SLPEN.setDisplayMode( "Description" )
    uartSym_UxMODE_SLPEN.setVisible(False)
    for ii in SLPEN_names:
        uartSym_UxMODE_SLPEN.addKey( ii['key'],ii['value'], ii['desc'] )

    uartSym_UxMODE = uartComponent.createHexSymbol("UMODE_VALUE", None)
    uartSym_UxMODE.setDefaultValue((int(uartSym_UxMODE_BRGH.getSelectedValue()) << 3) | (int(uartSym_UxMODE_PDSEL.getSelectedValue()) << 1) | (int(uartSym_UxMODE_STSEL.getSelectedValue()) << 0))
    uartSym_UxMODE.setVisible(False)
    uartSym_UxMODE.setDependencies(u1ModecombineValues,["UART_STSEL", "UART_PDSEL", "UART_BRGH", "UART_RXINV", "UART_ABAUD", "UART_LPBACK", "UART_WAKE", "UART_RTSMD", "UART_IREN", "UART_SIDL", "UART_RUNOVF", "UART_CLKSEL", "UART_SLPEN"])

    ## UART Clock Frequency
    uartClkValue = uartComponent.createIntegerSymbol("UART_CLOCK_FREQ", None)
    uartClkValue.setLabel("Clock Frequency")
    uartClkValue.setReadOnly(True)
    uartClkValue.setDefaultValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    uartClkValue.setDependencies(clockSourceFreq, ["core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    ## Baud Rate setting
    uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", None)
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(115200)

    brgVal = baudRateCalc(uartClkValue.getValue(), uartBaud.getValue())

    ## Baud Rate Frequency dependency
    uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", None)
    uartBRGValue.setVisible(False)
    uartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "core." + uartInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #UART Baud Rate not supported comment
    uartSym_BaudError_Comment = uartComponent.createCommentSymbol("UART_BAUD_ERROR_COMMENT", None)
    uartSym_BaudError_Comment.setLabel("********** UART Clock source value is low for the desired baud rate **********")
    uartSym_BaudError_Comment.setVisible(False)

    #Use setValue instead of setDefaultValue to store symbol value in default.xml
    uartBRGValue.setValue(brgVal, 1)

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

    #USART Character Size 9 Mask - 9-bit, no parity is below ORed with the none parity mask above
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
    #### Dependency ####
    ############################################################################

    ## EVIC Interrupt Dynamic settings
    setUARTInterruptData(uartSymInterruptMode.getValue())

    uartSymIntEnComment = uartComponent.createCommentSymbol("UART_INTRRUPT_ENABLE_COMMENT", None)
    uartSymIntEnComment.setLabel("Warning!!! " + uartInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    uartSymIntEnComment.setVisible(False)
    uartSymIntEnComment.setDependencies(updateUARTInterruptData, ["USART_INTERRUPT_MODE"] + InterruptVectorUpdate)

    # Clock Warning status
    uartSym_ClkEnComment = uartComponent.createCommentSymbol("UART_CLOCK_ENABLE_COMMENT", None)
    uartSym_ClkEnComment.setLabel("Warning!!! " + uartInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    uartSym_ClkEnComment.setVisible(False)
    uartSym_ClkEnComment.setDependencies(updateUARTClockWarningStatus, ["core." + uartInstanceName.getValue() + "_CLOCK_ENABLE"])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    uartHeaderFile = uartComponent.createFileSymbol("UART_COMMON_HEADER", None)
    uartHeaderFile.setSourcePath("../peripheral/uart_02478/templates/plib_uart_common.h")
    uartHeaderFile.setOutputName("plib_uart_common.h")
    uartHeaderFile.setDestPath("peripheral/uart/")
    uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeaderFile.setType("HEADER")
    uartHeaderFile.setMarkup(False)
    uartHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeader1File.setSourcePath("../peripheral/uart_02478/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE", None)
    uartSource1File.setSourcePath("../peripheral/uart_02478/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_" + uartInstanceName.getValue().lower() + ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_02478/templates/system/initialization.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_02478/templates/system/definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)
