"""*****************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

uartValGrp_U1MODE_RTSMD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__RTSMD"]')
uartBitField_U1MODE_RTSMD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="RTSMD"]')

uartValGrp_U1MODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__IREN"]')
uartBitField_U1MODE_IREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="IREN"]')

uartValGrp_U1MODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__SIDL"]')
uartBitField_U1MODE_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="SIDL"]')

uartValGrp_U1MODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__ON"]')
uartBitField_U1MODE_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="ON"]')

uartValGrp_U1MODE_RUNOVF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__RUNOVF"]')
uartBitField_U1MODE_RUNOVF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="RUNOVF"]')

uartValGrp_U1MODE_CLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__CLKSEL"]')
uartBitField_U1MODE_CLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="CLKSEL"]')

uartValGrp_U1MODE_SLPEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/value-group@[name="U1MODE__SLPEN"]')
uartBitField_U1MODE_SLPEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="UART"]/register-group@[name="UART"]/register@[name="U1MODE"]/bitfield@[name="SLPEN"]')

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

def getIRQnumber(string):

    for param in interruptsChildren:
        name = param.getAttribute("name")
        if string == name:
            irq_index = param.getAttribute("index")
            break

    return irq_index

# Calculates BRG value
def baudRateCalc(clk, baud):

    global uartSym_U1MODE_BRGH

    brgValLow = ((clk / baud) >> 4) - 1
    brgValHigh = ((clk / baud) >> 2) - 1

    brgh  = int(uartSym_U1MODE_BRGH.getSelectedValue())
    uxmode = int (Database.getSymbolValue(uartInstanceName.getValue().lower(), "UMODE_VALUE"))

    # Check if the baud value can be set with low baud settings
    if((brgValHigh >= 0) and (brgValHigh <= 65535)) :
        brgValue =  (((clk >> 2) + (baud >> 1)) / baud ) - 1
        uartSym_U1MODE_BRGH.setValue(0, 2)
        brghBitL = int(uartSym_U1MODE_BRGH.getSelectedValue())
        return brgValue
    elif((brgValLow >= 0) and (brgValLow <= 65535)) :
        brgValue = (((clk >> 4) + (baud >> 1)) / baud) - 1
        uartSym_U1MODE_BRGH.setValue(1, 2)
        brghBitH = int(uartSym_U1MODE_BRGH.getSelectedValue())
        return brgValue
    elif brgValLow > 65535:
        return brgValLow
    else:
        return brgValLow

def baudRateTrigger(symbol, event):

    global uartInstanceName

    clk = int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    baud = int(Database.getSymbolValue(uartInstanceName.getValue().lower(), "BAUD_RATE"))

    brgVal = baudRateCalc(clk, baud)

    if brgVal < 1:
        Log.writeErrorMessage("UART Clock source Frequency is low for the desired baud rate")
        return
    elif brgVal > 65535:
        brgVal = 65535
        Log.writeErrorMessage("Desired baud rate is low for current UART Source Clock Frequency")

    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):
    global uartInstanceName
    symbol.setValue(int(Database.getSymbolValue("core", uartInstanceName.getValue() + "_CLOCK_FREQUENCY")),2)

def u1ModecombineValues(symbol, event):

    uart1modeValue = symbol.getValue()

    if event["id"] == "UART_STSEL":
        stselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_STSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (stselValue << 0)

    if event["id"] == "UART_PDSEL":
        pdselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_PDSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (pdselValue << 1)

    if event["id"] == "UART_BRGH":
        brghValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_BRGH.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (brghValue << 3)

    if event["id"] == "UART_RXINV":
        rxinvValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_RXINV.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (rxinvValue << 4)

    if event["id"] == "UART_ABAUD":
        abaudValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_ABAUD.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (abaudValue << 5)

    if event["id"] == "UART_LPBACK":
        lpbackValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_LPBACK.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (lpbackValue << 6)

    if event["id"] == "UART_WAKE":
        wakeValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_WAKE.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (wakeValue << 7)

    if event["id"] == "UART_RTSMD":
        rstmdValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_RTSMD.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (rstmdValue << 11)

    if event["id"] == "UART_IREN":
        irenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_IREN.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (irenValue << 12)

    if event["id"] == "UART_SIDL":
        sidlValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_SIDL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (sidlValue << 13)

    if event["id"] == "UART_RUNOVF":
        runovfValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_RUNOVF.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (runovfValue << 16)

    if event["id"] == "UART_CLKSEL":
        clkselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_CLKSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int(maskvalue, 0))
        uart1modeValue = uart1modeValue | (clkselValue << 17)

    if event["id"] == "UART_SLPEN":
        slpenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_SLPEN.getAttribute("mask")
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
        if(ii["value"] == str(value)):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find value in dictionary") # should never get here
    return ""

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
    global uartSymInterruptMode

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

    uartSymInterruptMode = uartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    uartSymInterruptMode.setLabel("Enable Interrrupts ?")
    uartSymInterruptMode.setDefaultValue(True)

    ## Fault Interrrupt Setup
    uartIrqFault = uartInstanceName.getValue() + "_FAULT"
    InterruptVector.append(uartIrqFault + "_INTERRUPT_ENABLE")
    InterruptHandler.append(uartIrqFault + "_INTERRUPT_HANDLER")
    InterruptHandlerLock.append(uartIrqFault + "_INTERRUPT_HANDLER_LOCK")
    InterruptVectorUpdate.append("core." + uartIrqFault + "_INTERRUPT_ENABLE_UPDATE")
    uartFaultVectorNum = int(getIRQnumber(uartIrqFault))

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

    ## UART RX Interrupt
    uartIrqrRx = uartInstanceName.getValue() + "_RX"
    InterruptVector.append(uartIrqrRx + "_INTERRUPT_ENABLE")
    InterruptHandler.append(uartIrqrRx + "_INTERRUPT_HANDLER")
    InterruptHandlerLock.append(uartIrqrRx + "_INTERRUPT_HANDLER_LOCK")
    InterruptVectorUpdate.append("core." + uartIrqrRx + "_INTERRUPT_ENABLE_UPDATE")
    uartRxVectorNum = int(getIRQnumber(uartIrqrRx))
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

    ##UART TX Interrupt
    uartIrqTx = uartInstanceName.getValue() + "_TX"
    InterruptVector.append(uartIrqTx + "_INTERRUPT_ENABLE")
    InterruptHandler.append(uartIrqTx + "_INTERRUPT_HANDLER")
    InterruptHandlerLock.append(uartIrqTx + "_INTERRUPT_HANDLER_LOCK")
    InterruptVectorUpdate.append("core." + uartIrqTx + "_INTERRUPT_ENABLE_UPDATE")
    uartTxVectorNum = int(getIRQnumber(uartIrqTx))
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
    _get_bitfield_names(uartValGrp_U1MODE_STSEL, stsel_names)
    uartSym_U1MODE_STSEL = uartComponent.createKeyValueSetSymbol("UART_STSEL", None)
    uartSym_U1MODE_STSEL.setLabel(uartBitField_U1MODE_STSEL.getAttribute("caption"))
    uartSym_U1MODE_STSEL.setDefaultValue(find_key_value(0,stsel_names)) # 1 stop bit
    uartSym_U1MODE_STSEL.setOutputMode( "Value" )
    uartSym_U1MODE_STSEL.setDisplayMode( "Description" )
    for ii in stsel_names:
        uartSym_U1MODE_STSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    #PDSEL, Parity and data Selection Bits
    pdsel_names = []
    _get_bitfield_names(uartValGrp_U1MODE_PDSEL, pdsel_names)
    uartSym_U1MODE_PDSEL = uartComponent.createKeyValueSetSymbol("UART_PDSEL", None)
    uartSym_U1MODE_PDSEL.setLabel (uartBitField_U1MODE_PDSEL.getAttribute("caption"))
    uartSym_U1MODE_PDSEL.setDefaultValue(find_key_value(0,pdsel_names)) # 8-bit data, no parity
    uartSym_U1MODE_PDSEL.setOutputMode( "Value" )
    uartSym_U1MODE_PDSEL.setDisplayMode( "Description" )
    for ii in pdsel_names:
        uartSym_U1MODE_PDSEL.addKey( ii['key'],ii['value'], ii['desc'] )

    #BRGH, BRGH Selection Bit
    BRGH_names = []
    _get_bitfield_names(uartValGrp_U1MODE_BRGH, BRGH_names)
    uartSym_U1MODE_BRGH = uartComponent.createKeyValueSetSymbol("UART_BRGH", None)
    uartSym_U1MODE_BRGH.setLabel(uartBitField_U1MODE_BRGH.getAttribute("caption"))
    uartSym_U1MODE_BRGH.setDefaultValue(find_key_value(0,BRGH_names)) # standard speed mode
    uartSym_U1MODE_BRGH.setOutputMode( "Value" )
    uartSym_U1MODE_BRGH.setDisplayMode( "Description" )
    for ii in BRGH_names:
        uartSym_U1MODE_BRGH.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_U1MODE_BRGH.setReadOnly(True)

    #RXINV, Rx polarity inversion bit
    RXINV_names = []
    _get_bitfield_names(uartValGrp_U1MODE_RXINV, RXINV_names)
    uartSym_U1MODE_RXINV = uartComponent.createKeyValueSetSymbol("UART_RXINV", None)
    uartSym_U1MODE_RXINV.setLabel(uartBitField_U1MODE_RXINV.getAttribute("caption"))
    uartSym_U1MODE_RXINV.setDefaultValue(find_key_value(0,RXINV_names)) # standard speed mode
    uartSym_U1MODE_RXINV.setOutputMode( "Value" )
    uartSym_U1MODE_RXINV.setDisplayMode( "Description" )
    uartSym_U1MODE_RXINV.setVisible(False)
    for ii in RXINV_names:
        uartSym_U1MODE_RXINV.addKey( ii['key'],ii['value'], ii['desc'] )

    #ABAUD, Auto-baud enable bit
    ABAUD_names = []
    _get_bitfield_names(uartValGrp_U1MODE_ABAUD, ABAUD_names)
    uartSym_U1MODE_ABAUD = uartComponent.createKeyValueSetSymbol("UART_ABAUD", None)
    uartSym_U1MODE_ABAUD.setLabel(uartBitField_U1MODE_ABAUD.getAttribute("caption"))
    uartSym_U1MODE_ABAUD.setDefaultValue(find_key_value(0,ABAUD_names)) # baud rate measurement disabled
    uartSym_U1MODE_ABAUD.setOutputMode( "Value" )
    uartSym_U1MODE_ABAUD.setDisplayMode( "Description" )
    uartSym_U1MODE_ABAUD.setVisible(False)
    for ii in ABAUD_names:
        uartSym_U1MODE_ABAUD.addKey( ii['key'],ii['value'], ii['desc'] )


    #LPBACK, Loopback Mode Select bit
    LPBACK_names = []
    _get_bitfield_names(uartValGrp_U1MODE_LPBACK, LPBACK_names)
    uartSym_U1MODE_LPBACK = uartComponent.createKeyValueSetSymbol("UART_LPBACK", None)
    uartSym_U1MODE_LPBACK.setLabel(uartBitField_U1MODE_LPBACK.getAttribute("caption"))
    uartSym_U1MODE_LPBACK.setDefaultValue(find_key_value(0,LPBACK_names)) # loopback mode disabled
    uartSym_U1MODE_LPBACK.setOutputMode( "Value" )
    uartSym_U1MODE_LPBACK.setDisplayMode( "Description" )
    uartSym_U1MODE_LPBACK.setVisible(False)
    for ii in LPBACK_names:
        uartSym_U1MODE_LPBACK.addKey( ii['key'],ii['value'], ii['desc'] )

    #WAKE, Enable Wake-up on Start bit Detect During Sleep Mode bit
    WAKE_names = []
    _get_bitfield_names(uartValGrp_U1MODE_WAKE, WAKE_names)
    uartSym_U1MODE_WAKE = uartComponent.createKeyValueSetSymbol("UART_WAKE", None)
    uartSym_U1MODE_WAKE.setLabel(uartBitField_U1MODE_WAKE.getAttribute("caption"))
    uartSym_U1MODE_WAKE.setDefaultValue(find_key_value(0,WAKE_names)) # wake-up disabled
    uartSym_U1MODE_WAKE.setOutputMode( "Value" )
    uartSym_U1MODE_WAKE.setDisplayMode( "Description" )
    uartSym_U1MODE_WAKE.setVisible(False)
    for ii in WAKE_names:
        uartSym_U1MODE_WAKE.addKey( ii['key'],ii['value'], ii['desc'] )

    #RTSMD, Mode Selection for UxRTS Pin bit
    RTSMD_names = []
    _get_bitfield_names(uartValGrp_U1MODE_RTSMD, RTSMD_names)
    uartSym_U1MODE_RTSMD = uartComponent.createKeyValueSetSymbol("UART_RTSMD", None)
    uartSym_U1MODE_RTSMD.setLabel(uartBitField_U1MODE_RTSMD.getAttribute("caption"))
    uartSym_U1MODE_RTSMD.setDefaultValue(find_key_value(0,RTSMD_names)) # /UxRTS pin is in Flow Control mode
    uartSym_U1MODE_RTSMD.setOutputMode( "Value" )
    uartSym_U1MODE_RTSMD.setDisplayMode( "Description" )
    uartSym_U1MODE_RTSMD.setVisible(False)
    for ii in RTSMD_names:
        uartSym_U1MODE_RTSMD.addKey( ii['key'],ii['value'], ii['desc'] )

    #IREN, IrDA Encoder and Decoder Enable bit
    IREN_names = []
    _get_bitfield_names(uartValGrp_U1MODE_IREN, IREN_names)
    uartSym_U1MODE_IREN = uartComponent.createKeyValueSetSymbol("UART_IREN", None)
    uartSym_U1MODE_IREN.setLabel(uartBitField_U1MODE_IREN.getAttribute("caption"))
    uartSym_U1MODE_IREN.setDefaultValue(find_key_value(0,IREN_names)) # IrDA is disabled
    uartSym_U1MODE_IREN.setOutputMode( "Value" )
    uartSym_U1MODE_IREN.setDisplayMode( "Description" )
    uartSym_U1MODE_IREN.setVisible(False)
    for ii in IREN_names:
        uartSym_U1MODE_IREN.addKey( ii['key'],ii['value'], ii['desc'] )

    #SIDL, Stop in Idle Mode bit
    SIDL_names = []
    _get_bitfield_names(uartValGrp_U1MODE_SIDL, SIDL_names)
    uartSym_U1MODE_SIDL = uartComponent.createKeyValueSetSymbol("UART_SIDL", None)
    uartSym_U1MODE_SIDL.setLabel(uartBitField_U1MODE_SIDL.getAttribute("caption"))
    uartSym_U1MODE_SIDL.setDefaultValue(find_key_value(0,SIDL_names)) # continue operation in idle mode
    uartSym_U1MODE_SIDL.setOutputMode( "Value" )
    uartSym_U1MODE_SIDL.setDisplayMode( "Description" )
    uartSym_U1MODE_SIDL.setVisible(False)
    for ii in SIDL_names:
        uartSym_U1MODE_SIDL.addKey( ii['key'],ii['value'], ii['desc'] )

    #RUNOVF, Run During Overflow Condition Mode bit
    RUNOVF_names = []
    _get_bitfield_names(uartValGrp_U1MODE_RUNOVF, RUNOVF_names)
    uartSym_U1MODE_RUNOVF = uartComponent.createKeyValueSetSymbol("UART_RUNOVF", None)
    uartSym_U1MODE_RUNOVF.setLabel(uartBitField_U1MODE_RUNOVF.getAttribute("caption"))
    uartSym_U1MODE_RUNOVF.setDefaultValue(find_key_value(0,RUNOVF_names)) # shift register stops during overflow
    uartSym_U1MODE_RUNOVF.setOutputMode( "Value" )
    uartSym_U1MODE_RUNOVF.setDisplayMode( "Description" )
    uartSym_U1MODE_RUNOVF.setVisible(False)
    for ii in RUNOVF_names:
        uartSym_U1MODE_RUNOVF.addKey( ii['key'],ii['value'], ii['desc'] )

    #CLKSEL, UARTx Module Clock Selection bits
    CLKSEL_names = []
    _get_bitfield_names(uartValGrp_U1MODE_CLKSEL, CLKSEL_names)
    uartSym_U1MODE_CLKSEL = uartComponent.createKeyValueSetSymbol("UART_CLKSEL", None)
    uartSym_U1MODE_CLKSEL.setLabel(uartBitField_U1MODE_CLKSEL.getAttribute("caption"))
    uartSym_U1MODE_CLKSEL.setDefaultValue(find_key_value(0,CLKSEL_names)) # BRG clock is PBCLK2
    uartSym_U1MODE_CLKSEL.setOutputMode( "Value" )
    uartSym_U1MODE_CLKSEL.setDisplayMode( "Description" )
    uartSym_U1MODE_CLKSEL.setVisible(False)
    for ii in CLKSEL_names:
        uartSym_U1MODE_CLKSEL.addKey( ii['key'],ii['value'], ii['desc'] )


    #SLPEN, Run During Sleep Enable bit
    SLPEN_names = []
    _get_bitfield_names(uartValGrp_U1MODE_SLPEN, SLPEN_names)
    uartSym_U1MODE_SLPEN = uartComponent.createKeyValueSetSymbol("UART_SLPEN", None)
    uartSym_U1MODE_SLPEN.setLabel(uartBitField_U1MODE_SLPEN.getAttribute("caption"))
    uartSym_U1MODE_SLPEN.setDefaultValue(find_key_value(0,SLPEN_names)) # BRG clock off during sleep mode
    uartSym_U1MODE_SLPEN.setOutputMode( "Value" )
    uartSym_U1MODE_SLPEN.setDisplayMode( "Description" )
    uartSym_U1MODE_SLPEN.setVisible(False)
    for ii in SLPEN_names:
        uartSym_U1MODE_SLPEN.addKey( ii['key'],ii['value'], ii['desc'] )

    uartSym_U1MODE = uartComponent.createHexSymbol("UMODE_VALUE", None)
    uartSym_U1MODE.setDefaultValue((int(uartSym_U1MODE_BRGH.getSelectedValue()) << 3) | (int(uartSym_U1MODE_PDSEL.getSelectedValue()) << 1) | (int(uartSym_U1MODE_STSEL.getSelectedValue()) << 0))
    uartSym_U1MODE.setVisible(False)
    uartSym_U1MODE.setDependencies(u1ModecombineValues,["UART_STSEL", "UART_PDSEL", "UART_BRGH", "UART_RXINV", "UART_ABAUD", "UART_LPBACK", "UART_WAKE", "UART_RTSMD", "UART_IREN", "UART_SIDL", "UART_RUNOVF", "UART_CLKSEL", "UART_SLPEN"])

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
