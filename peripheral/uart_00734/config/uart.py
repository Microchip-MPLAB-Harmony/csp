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
  
global uartInstanceName

################################################################################
#### Business Logic ####
################################################################################

def dependencyStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        
def dependencyInterrupt(symbol, event):
    if (event["value"] == False):
        symbol.setValue(0,1)
    else:
        symbol.setValue(1,1)
        
def enableMenu(menu, event):
	menu.setVisible(event["value"])

def InterruptModeDependency(symbol, event):
    fault_enable = Database.getSymbolValue(uartInstanceName.getValue().lower(), "UART_FAULT_INTERRUPT_ENABLE")
    rx_enable = Database.getSymbolValue(uartInstanceName.getValue().lower(), "UART_RX_INTERRUPT_ENABLE")
    tx_enable = Database.getSymbolValue(uartInstanceName.getValue().lower(), "UART_TX_INTERRUPT_ENABLE")
    if(event["id"] == "UART_FAULT_INTERRUPT_ENABLE"):
        fault_enable = int(event["value"])
    elif(event["id"] == "UART_RX_INTERRUPT_ENABLE"):
        rx_enable = int(event["value"])
    elif(event["id"] == "UART_TX_INTERRUPT_ENABLE"):
        tx_enable = int(event["value"])

    if(fault_enable and rx_enable and tx_enable ):
        symbol.setValue(1,1)
    else:
        symbol.setValue(0,1)

def InterruptEnDependency(symbol,event):
    if(int(event["value"]) == True):
        symbol.setLabel("                                     ***INTERRUPT MODE Selected***")
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/32)
        bitPosn = int(vectorNumber%32)
        bitMask = hex(1<<bitPosn)
        regName = "IEC"+str(index)
        return regName, str(bitPosn), str(bitMask)
        
def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/32)
        bitPosn = int(vectorNumber%32)
        bitMask = hex(1<<bitPosn)
        regName = "IFS"+str(index)
        return regName, str(bitPosn), str(bitMask)        

def _get_sub_priority_parms(vectorNumber):
    # This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift, 
    # and subpriority bitmask for input vector number
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/4)
        subPrioBit = 8*(vectorNumber & 0x3)
        subPrioMask = 0x3  # always 2 bits
        prioMask = 0x7
        prioBit = subPrioBit + 2
        regName = "IPC"+str(index)
    return regName, str(prioBit), str(prioMask), str(subPrioBit), str(subPrioMask)
    
def _get_bitfield_names(node, outputList):
    valueNodes = node.getChildren()
    for ii in valueNodes:   # do this for all <value > entries for this bitfield
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):  # skip (unused) reserved fields
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')
            
            # Get rid of leading '0x', and convert to int if was hex
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)
            outputList.append(dict)
        
# Calculates BRG value
def baudRateCalc(clk, baud):
    global uartSym_U1MODE_BRGH
    brgValLow = ((clk /baud)>>4)-1
    brgValHigh = ((clk /baud)>>2)-1
    brgh  = int(uartSym_U1MODE_BRGH.getSelectedValue())
    uxmode = int (Database.getSymbolValue(uartInstanceName.getValue().lower(), "UMODE_VALUE"))
    # Check if the baud value can be set with low baud settings 
    if((brgValHigh >= 0) and (brgValHigh <= 65535)) :
       brgValue =  (((clk >> 2) + (baud >> 1)) / baud ) - 1  
       uartSym_U1MODE_BRGH.setValue(0,2)
       brghBitL = int(uartSym_U1MODE_BRGH.getSelectedValue())
       return brgValue
    elif ((brgValLow >= 0) and (brgValLow <= 65535)) :
       brgValue = ( ((clk >> 4) + (baud >> 1)) / baud ) - 1 
       uartSym_U1MODE_BRGH.setValue(1,2)
       brghBitH = int(uartSym_U1MODE_BRGH.getSelectedValue())
       return brgValue  
    elif (brgValLow > 65535):
       return brgValLow    
    else:
       return brgValLow

def baudRateTrigger(symbol, event):
    global uartInstanceName
    clk = int (Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ"))
    baud = int (Database.getSymbolValue(uartInstanceName.getValue().lower(), "BAUD_RATE"))

    brgVal = baudRateCalc(clk, baud)
     
    if(brgVal < 1):
        Log.writeErrorMessage("UART Clock source Frequency is low for the desired baud rate")
        return
    elif (brgVal>65535):
        brgVal= 65535
        Log.writeErrorMessage("Desired baud rate is low for current UART Source Clock Frequency")
    symbol.clearValue()
    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):
    symbol.clearValue()
    symbol.setValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ")),2)

def getIRQnumber(string):
    interrupts = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts')
    interruptsChildren = interrupts.getChildren()
    for param in interruptsChildren:  
        modInst = param.getAttribute('module-instance')
        if(string == modInst):
            irq_index = param.getAttribute('index')
            break
    return irq_index
    
def updateIRQValues(symbol, event):
    irqvalue = int(event["value"])
    symbol.setValue(irqvalue, 2)

def updateHandlerName(symbol, event):
    handlername = str(event["value"])
    symbol.setValue(handlername, 2)

def u1ModecombineValues(symbol, event):
    uart1modeValue = symbol.getValue()
    if(event["id"] == "UART_STOPBIT_SELECT"):
        stselValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = uartBitField_U1MODE_STSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int (maskvalue,0))
        uart1modeValue = uart1modeValue | (stselValue<<0)
    if(event["id"] == "UART_PDBIT_SELECT"):
        pdselValue = int(event["symbol"].getKeyValue(event["value"])) 
        maskvalue = uartBitField_U1MODE_PDSEL.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int (maskvalue,0))
        uart1modeValue = uart1modeValue | (pdselValue<<1) 
    if(event["id"] == "UART_BRGH"):
        brghValue = int(event["symbol"].getKeyValue(event["value"])) 
        maskvalue = uartBitField_U1MODE_BRGH.getAttribute("mask")
        uart1modeValue = uart1modeValue & (~int (maskvalue,0)) 
        uart1modeValue  =  uart1modeValue | (brghValue<<3)  
    symbol.setValue(uart1modeValue, 2)

def combineFaultIPC_Values(symbol, event):
    global uartFaultVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(uartFaultVectorNum)
    faultipc = symbol.getValue()
    if(event["id"] == "UART_FLT_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        faultipc = faultipc & ~((int(pm))<< (int(ps)))
        faultipc = faultipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "UART_FLT_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        faultipc = faultipc & ~((int(spm))<< (int(sps)))
        faultipc = faultipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(faultipc, 2)

def combineRXIPC_Values(symbol, event):
    global uartRxVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(uartRxVectorNum)
    rxipc = symbol.getValue()
    if(event["id"] == "UART_RX_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        rxipc = rxipc & ~((int(pm))<< (int(ps)))
        rxipc = rxipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "UART_RX_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        rxipc = rxipc & ~((int(spm))<< (int(sps)))
        rxipc = rxipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(rxipc, 2)

def combineTXIPC_Values(symbol, event):
    global uartTxVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(uartTxVectorNum)
    txipc = symbol.getValue()
    if(event["id"] == "UART_TX_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        txipc = txipc & ~((int(pm))<< (int(ps)))
        txipc = txipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "UART_TX_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        txipc = txipc & ~((int(spm))<< (int(sps)))
        txipc = txipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(txipc, 2)
    
################################################################################
#### Component ####
################################################################################
def instantiateComponent(uartComponent):
 
    global uartInstanceName
    global uartInstanceNum
    global uartFaultVectorNum
    global uartRxVectorNum
    global uartTxVectorNum
    global uartSym_U1MODE_BRGH

    uartInstanceName = uartComponent.createStringSymbol("UART_INSTANCE_NAME", None)
    uartInstanceName.setVisible(False)
    uartInstanceName.setDefaultValue(uartComponent.getID().upper())
    Log.writeInfoMessage("Running " + uartInstanceName.getValue())
    
    uartInstanceNum = uartComponent.createStringSymbol("UART_INSTANCE_NUM", None)
    uartInstanceNum.setVisible(False)
    componentName = str(uartComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    uartInstanceNum.setDefaultValue(instanceNum)
      
    ## Interrrupt Setup Fault
    uartIrqFault = uartInstanceName.getValue()+ "_FAULT"
    uartFaultVectorNum = int(getIRQnumber(uartIrqFault))
      
    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(uartFaultVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(uartFaultVectorNum)
    prioRegName, prioShift, prioMask, subprioShift, subprioMask = _get_sub_priority_parms(uartFaultVectorNum)
    
    #IEC REG
    uartFaultIEC = uartComponent.createStringSymbol("UART_FAULT_IEC_REG", None)
    uartFaultIEC.setDefaultValue(enblRegName)
    uartFaultIEC.setVisible(False)

    #IFS REG
    uartFaultIFS = uartComponent.createStringSymbol("UART_FAULT_IFS_REG", None)
    uartFaultIFS.setDefaultValue(statRegName)
    uartFaultIFS.setVisible(False)

    #PRIORITY VALUE
    uartVectorPriSym = "NVIC_" + str(uartFaultVectorNum) + "_0_PRIORITY"
    uartFltpriValue = Database.getSymbolValue("core",uartVectorPriSym)
    uartFaultIPC_PriValue = uartComponent.createHexSymbol("UART_FLT_IPC_PRI_VALUE", None)
    uartFaultIPC_PriValue.setDefaultValue(int(uartFltpriValue))
    uartFaultIPC_PriValue.setVisible(False)
    uartFaultIPC_PriValue.setDependencies(updateIRQValues, ["core." + uartVectorPriSym])

    #SUBPRIORITY VALUE
    uartVectorSubPriSym = "NVIC_" + str(uartFaultVectorNum) + "_0_SUBPRIORITY"
    uartFaultSubPriValue = Database.getSymbolValue("core",uartVectorSubPriSym)
    uartFaultIPC_SubpriValue = uartComponent.createHexSymbol("UART_FLT_IPC_SUBPRI_VALUE", None)
    uartFaultIPC_SubpriValue.setDefaultValue(int(uartFaultSubPriValue))
    uartFaultIPC_SubpriValue.setVisible(False)
    uartFaultIPC_SubpriValue.setDependencies(updateIRQValues, ["core." + uartVectorSubPriSym])

    #IPC VALUE
    uartFaultIPC_Val = uartComponent.createHexSymbol("UART_FAULT_IPC_VALUE", None)
    uartFaultIPC_Val.setDefaultValue((int (uartFaultIPC_PriValue.getDefaultValue()) << int(prioShift)) | (int (uartFaultIPC_SubpriValue.getDefaultValue()) << int(subprioShift)))
    uartFaultIPC_Val.setVisible(False)    
    uartFaultIPC_Val.setDependencies(combineFaultIPC_Values, ["UART_FLT_IPC_PRI_VALUE"])
    uartFaultIPC_Val.setDependencies(combineFaultIPC_Values, ["UART_FLT_IPC_SUBPRI_VALUE"])

    #HANDLER NAME
    uartFaultVectorSym = "NVIC_" + str(uartFaultVectorNum) + "_0_HANDLER"
    faulthandlerValue = Database.getSymbolValue("core",uartFaultVectorSym)
    uartFaultIPC_handlerStr = uartComponent.createStringSymbol("UART_ISR_FAULT_HANDLER_NAME", None)
    uartFaultIPC_handlerStr.setDefaultValue(faulthandlerValue)
    uartFaultIPC_handlerStr.setVisible(False)
    uartFaultIPC_handlerStr.setDependencies(updateHandlerName, (["core." + uartFaultVectorSym]))
    
    ## UART RX Interrupt
    uartIrqrx = uartInstanceName.getValue()+ "_RX"
    uartRxVectorNum = int(getIRQnumber(uartIrqrx))
    urxenblRegName, urxenblBitPosn, urxenblMask = _get_enblReg_parms(uartRxVectorNum)
    urxstatRegName, urxstatBitPosn, urxstatMask = _get_statReg_parms(uartRxVectorNum)
    urxprioRegName, urxprioShift, urxprioMask, urxsubprioShift, urxsubprioMask = _get_sub_priority_parms(uartRxVectorNum)
    
    #IEC REG
    uartRXIEC = uartComponent.createStringSymbol("UART_RX_IEC_REG", None)
    uartRXIEC.setDefaultValue(urxenblRegName)
    uartRXIEC.setVisible(False)

    #IFS REG
    uartRXIFS = uartComponent.createStringSymbol("UART_RX_IFS_REG", None)
    uartRXIFS.setDefaultValue(urxstatRegName)
    uartRXIFS.setVisible(False)

   #PRIORITY VALUE
    uartRxVectorPriSym = "NVIC_" + str(uartRxVectorNum) + "_0_PRIORITY"
    uartRxpriValue = Database.getSymbolValue("core",uartRxVectorPriSym)
    uartRXIPC_PriValue = uartComponent.createHexSymbol("UART_RX_IPC_PRI_VALUE", None)
    uartRXIPC_PriValue.setDefaultValue(int(uartRxpriValue))
    uartRXIPC_PriValue.setVisible(False)
    uartRXIPC_PriValue.setDependencies(updateIRQValues, ["core."+ uartRxVectorPriSym])

    #SUBPRIORITY VALUE
    uartRxVectorSubPriSym = "NVIC_" + str(uartRxVectorNum) + "_0_SUBPRIORITY"
    uartRxSubPriValue = Database.getSymbolValue("core",uartRxVectorSubPriSym)
    uartRXIPC_SubpriValue = uartComponent.createHexSymbol("UART_RX_IPC_SUBPRI_VALUE", None)
    uartRXIPC_SubpriValue.setDefaultValue(int(uartRxSubPriValue))
    uartRXIPC_SubpriValue.setVisible(False)
    uartRXIPC_SubpriValue.setDependencies(updateIRQValues, ["core."+ uartRxVectorSubPriSym])

    #IPC VALUE
    uartRXIPC_Val = uartComponent.createHexSymbol("UART_RX_IPC_VALUE", None)
    uartRXIPC_Val.setDefaultValue((int(uartRXIPC_PriValue.getDefaultValue()) << int(urxprioShift)) | (int (uartRXIPC_SubpriValue.getDefaultValue()) << int(urxsubprioShift)))
    uartRXIPC_Val.setVisible(False)    
    uartRXIPC_Val.setDependencies(combineRXIPC_Values, ["UART_RX_IPC_PRI_VALUE"])
    uartRXIPC_Val.setDependencies(combineRXIPC_Values, ["UART_RX_IPC_SUBPRI_VALUE"])

    #HANDLER NAME  
    uartVectorSym = "NVIC_" + str(uartRxVectorNum) + "_0_HANDLER"
    uartRXIPC_handlerStr = uartComponent.createStringSymbol("UART_ISR_RX_HANDLER_NAME", None)
    rxhandlerValue = Database.getSymbolValue("core",uartVectorSym)
    uartRXIPC_handlerStr.setDefaultValue(rxhandlerValue)
    uartRXIPC_handlerStr.setVisible(False)
    uartRXIPC_handlerStr.setDependencies(updateHandlerName, (["core." + uartVectorSym]))
    
    ##UART TX Interrupt
    uartIrqtx = uartInstanceName.getValue()+ "_TX"
    uartTxVectorNum = int(getIRQnumber(uartIrqtx))
    utxenblRegName, utxenblBitPosn, utxenblMask = _get_enblReg_parms(uartTxVectorNum)
    utxstatRegName, utxstatBitPosn, utxstatMask = _get_statReg_parms(uartTxVectorNum)
    utxprioRegName, utxprioShift, utxprioMask, utxsubprioShift, utxsubprioMask = _get_sub_priority_parms(uartTxVectorNum)
    
    #IEC REG
    uartTXIEC = uartComponent.createStringSymbol("UART_TX_IEC_REG", None)
    uartTXIEC.setDefaultValue(utxenblRegName)
    uartTXIEC.setVisible(False)

    #IFS REG
    uartTXIFS = uartComponent.createStringSymbol("UART_TX_IFS_REG", None)
    uartTXIFS.setDefaultValue(utxstatRegName)
    uartTXIFS.setVisible(False)

    #PRIORITY VALUE
    uartTxVectorPriSym = "NVIC_" + str(uartTxVectorNum) + "_0_PRIORITY"
    uartTxpriValue = Database.getSymbolValue("core",uartTxVectorPriSym)
    uartTXIPC_PriValue = uartComponent.createHexSymbol("UART_TX_IPC_PRI_VALUE", None)
    uartTXIPC_PriValue.setDefaultValue(int(uartTxpriValue))
    uartTXIPC_PriValue.setVisible(False)
    uartTXIPC_PriValue.setDependencies(updateIRQValues, ["core." + uartTxVectorPriSym])

    #SUBPRIORITY VALUE
    uartTxVectorSubPriSym = "NVIC_" + str(uartTxVectorNum) + "_0_SUBPRIORITY"
    uartTxSubPriValue = Database.getSymbolValue("core",uartTxVectorSubPriSym)
    uartTXIPC_SubpriValue = uartComponent.createHexSymbol("UART_TX_IPC_SUBPRI_VALUE", None)
    uartTXIPC_SubpriValue.setDefaultValue(int(uartTxSubPriValue))
    uartTXIPC_SubpriValue.setVisible(False)
    uartTXIPC_SubpriValue.setDependencies(updateIRQValues, ["core." + uartTxVectorSubPriSym])

    #IPC VALUE
    uartTXIPC_Val = uartComponent.createHexSymbol("UART_TX_IPC_VALUE", None)
    uartTXIPC_Val.setDefaultValue((int(uartTXIPC_PriValue.getDefaultValue()) << int(utxprioShift)) | (int (uartTXIPC_SubpriValue.getDefaultValue()) << int(utxsubprioShift)))
    uartTXIPC_Val.setVisible(False)    
    uartTXIPC_Val.setDependencies(combineTXIPC_Values, ["UART_TX_IPC_PRI_VALUE"])
    uartTXIPC_Val.setDependencies(combineTXIPC_Values, ["UART_TX_IPC_SUBPRI_VALUE"])

    #TX HANDLER NAME
    uarttxVectorSym = "NVIC_" + str(uartTxVectorNum) + "_0_HANDLER"
    uartTXIPC_handlerStr = uartComponent.createStringSymbol("UART_ISR_TX_HANDLER_NAME", None)
    txhandlerValue = Database.getSymbolValue("core", uarttxVectorSym)
    uartTXIPC_handlerStr.setDefaultValue(txhandlerValue)
    uartTXIPC_handlerStr.setVisible(False)
    uartTXIPC_handlerStr.setDependencies(updateHandlerName, ["core." + uarttxVectorSym])
   
    ##STOP Selection Bit
    stsel_names = []
    _get_bitfield_names(uartValGrp_U1MODE_STSEL, stsel_names)
    uartSym_U1MODE_STSEL = uartComponent.createKeyValueSetSymbol( "UART_STOPBIT_SELECT",None)  
    uartSym_U1MODE_STSEL.setLabel(uartBitField_U1MODE_STSEL.getAttribute("caption"))
    uartSym_U1MODE_STSEL.setDefaultValue(1)
    uartSym_U1MODE_STSEL.setOutputMode( "Value" )
    uartSym_U1MODE_STSEL.setDisplayMode( "Description" )
    for ii in stsel_names:
        uartSym_U1MODE_STSEL.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_U1MODE_STSEL.setVisible(True)
   
   ##Parity and data Selection Bits
    pdsel_names = []
    _get_bitfield_names(uartValGrp_U1MODE_PDSEL, pdsel_names)
    uartSym_U1MODE_PDSEL = uartComponent.createKeyValueSetSymbol( "UART_PDBIT_SELECT",None)  
    uartSym_U1MODE_PDSEL.setLabel (uartBitField_U1MODE_PDSEL.getAttribute("caption"))
    uartSym_U1MODE_PDSEL.setDefaultValue(3)
    uartSym_U1MODE_PDSEL.setOutputMode( "Value" )
    uartSym_U1MODE_PDSEL.setDisplayMode( "Description" )
    for ii in pdsel_names:
        uartSym_U1MODE_PDSEL.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_U1MODE_PDSEL.setVisible(True)

    ##BRGH Selection Bit
    BRGH_names = []
    _get_bitfield_names(uartValGrp_U1MODE_BRGH, BRGH_names)
    uartSym_U1MODE_BRGH = uartComponent.createKeyValueSetSymbol( "UART_BRGH",None)  
    uartSym_U1MODE_BRGH.setLabel(uartBitField_U1MODE_BRGH.getAttribute("caption"))
    uartSym_U1MODE_BRGH.setDefaultValue(1)
    uartSym_U1MODE_BRGH.setOutputMode( "Value" )
    uartSym_U1MODE_BRGH.setDisplayMode( "Description" )
    for ii in BRGH_names:
        uartSym_U1MODE_BRGH.addKey( ii['key'],ii['value'], ii['desc'] )
    uartSym_U1MODE_BRGH.setVisible(True)
    uartSym_U1MODE_BRGH.setReadOnly(True)
    
    uartSym_U1MODE = uartComponent.createHexSymbol("UMODE_VALUE",None)
    uartSym_U1MODE.setDefaultValue((int(uartSym_U1MODE_BRGH.getSelectedValue())<<3) | (int (uartSym_U1MODE_PDSEL.getSelectedValue())<<1) | (int(uartSym_U1MODE_STSEL.getSelectedValue())<<0))
    uartSym_U1MODE.setVisible(False)
    uartSym_U1MODE.setDependencies(u1ModecombineValues,["UART_STOPBIT_SELECT"])
    uartSym_U1MODE.setDependencies(u1ModecombineValues,["UART_PDBIT_SELECT"])
    uartSym_U1MODE.setDependencies(u1ModecombineValues,["UART_BRGH"])
   
    ## UART Clock Frequency
    uartClkValue = uartComponent.createIntegerSymbol("UART_CLOCK_FREQ", None)
    uartClkValue.setLabel("Clock Frequency")
    uartClkValue.setReadOnly(True)
    uartClkValue.setVisible(True)
    uartClkValue.setDependencies(clockSourceFreq, ["core." + "CONFIG_SYS_CLK_PBCLK2_FREQ"])
    uartClkValue.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ")))
    
    ## Baud Rate setting
    uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", None)
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(9600)
    uartBaud.setVisible(True)
    brgVal = baudRateCalc(uartClkValue.getValue(), uartBaud.getValue())
    
    ## Baud Rate Frequency dependency
    uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", None)
    uartBRGValue.setVisible(False)
    uartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE"])
    uartBRGValue.setDependencies(baudRateTrigger, ["core." + "CONFIG_SYS_CLK_PBCLK2_FREQ"])
    uartBRGValue.setDefaultValue(brgVal)


    ############################################################################
    #### Dependency ####
    ############################################################################
    ## MIPS Interrupt Dynamic settings
    faultinterruptEnable = uartComponent.createBooleanSymbol("UART_FAULT_INTERRUPT_ENABLE", None)
    faultinterruptEnable.setVisible(False)
    rxinterruptEnable = uartComponent.createBooleanSymbol("UART_RX_INTERRUPT_ENABLE", None)
    rxinterruptEnable.setVisible(False)
    txinterruptEnable = uartComponent.createBooleanSymbol("UART_TX_INTERRUPT_ENABLE", None) 
    txinterruptEnable.setVisible(False)
  
    ## Fault Default Values
    faultVectorEnableSym = "NVIC_" + str(uartFaultVectorNum) + "_0_ENABLE"
    uartfltSymIntEnComment = uartComponent.createCommentSymbol("UART_FAULTINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", faultVectorEnableSym) == False):
        uartfltSymIntEnComment.setVisible(True)
        faultinterruptEnable.setDefaultValue(0)
    else:
        uartfltSymIntEnComment.setVisible(False)
        faultinterruptEnable.setDefaultValue(1)
    

    ## Fault Dependency
    uartfltSymIntEnComment.setLabel("Warning!!! UART" + str(instanceNum) + " Fault Interrupt is Disabled in Interrupt Manager")
    faultinterruptEnable.setDependencies(dependencyInterrupt, ["core." + faultVectorEnableSym])
    uartfltSymIntEnComment.setDependencies(dependencyStatus, ["core." + faultVectorEnableSym])

    ## rx Default Values
    rxVectorEnableSym = "NVIC_" + str(uartRxVectorNum) + "_0_ENABLE"
    uartrxSymIntEnComment = uartComponent.createCommentSymbol("UART_RXINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", rxVectorEnableSym) == False):
        uartrxSymIntEnComment.setVisible(True)
        rxinterruptEnable.setDefaultValue(0)
    else:
        uartrxSymIntEnComment.setVisible(False)
        rxinterruptEnable.setDefaultValue(1)
     ## rx Dependency
    uartrxSymIntEnComment.setLabel("Warning!!! UART" + str(instanceNum) + " RX Interrupt is Disabled in Interrupt Manager")
    uartrxSymIntEnComment.setDependencies(dependencyStatus, ["core." + rxVectorEnableSym])
    rxinterruptEnable.setDependencies(dependencyInterrupt, ["core." + rxVectorEnableSym])

    ## tx Default Values
    txVectorEnableSym = "NVIC_" + str(uartTxVectorNum) + "_0_ENABLE"
    uarttxSymIntEnComment = uartComponent.createCommentSymbol("UART_TXINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", txVectorEnableSym) == False):
        uarttxSymIntEnComment.setVisible(True)
        txinterruptEnable.setDefaultValue(0)
    else:
        uarttxSymIntEnComment.setVisible(False)
        txinterruptEnable.setDefaultValue(1)
     ## TX Dependency
    uarttxSymIntEnComment.setLabel("Warning!!! UART" + str(instanceNum) + " TX Interrupt is Disabled in Interrupt Manager")
    uarttxSymIntEnComment.setDependencies(dependencyStatus, ["core." + txVectorEnableSym])
    txinterruptEnable.setDependencies(dependencyInterrupt, ["core." + txVectorEnableSym])
    
    uartSymInterruptMode = uartComponent.createBooleanSymbol("UART_INTERRUPT_MODE", None)
    uartSymInterruptMode.setVisible(False)
    combineInterruptValue = faultinterruptEnable.getValue() & rxinterruptEnable.getValue() & txinterruptEnable.getValue()
    uartSymInterruptMode.setDefaultValue(combineInterruptValue)
    uartSymInterruptMode.setDependencies(InterruptModeDependency, ["UART_FAULT_INTERRUPT_ENABLE"])
    uartSymInterruptMode.setDependencies(InterruptModeDependency, ["UART_RX_INTERRUPT_ENABLE"])
    uartSymInterruptMode.setDependencies(InterruptModeDependency, ["UART_TX_INTERRUPT_ENABLE"])

    uartSymIntEnComment = uartComponent.createCommentSymbol("UART_INTRRUPT_ENABLE_COMMENT", None)
    if(combineInterruptValue == 1):
        uartSymIntEnComment.setVisible(True)
    else:
        uartSymIntEnComment.setVisible(False)
    uartSymIntEnComment.setDependencies(InterruptEnDependency,["UART_INTERRUPT_MODE"])   

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
    uartHeader1File.setOutputName("plib_"+uartInstanceName.getValue().lower()+ ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE", None)
    uartSource1File.setSourcePath("../peripheral/uart_00734/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_"+uartInstanceName.getValue().lower()+ ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_00734/templates/system/system_initialize.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_00734/templates/system/system_definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)
