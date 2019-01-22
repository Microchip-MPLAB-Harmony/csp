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
# SPICON Register
spiValGrp_SPI1CON_MSTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__MSTEN"]')
spiBitField_SPI1CON_MSTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="MSTEN"]')

spiValGrp_SPI1CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__MSSEN"]')
spiBitField_SPI1CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="MSSEN"]')

spiValGrp_SPI1CON_MODE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__MODE32"]')
spiBitField_SPI1CON_MODE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="MODE32"]')

spiValGrp_SPI1CON_CKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__CKE"]')
spiBitField_SPI1CON_CKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="CKE"]')

spiValGrp_SPI1CON_CKP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__CKP"]')
spiBitField_SPI1CON_CKP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="CKP"]')

spiValGrp_SPI1CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__MSSEN"]')
spiBitField_SPI1CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="MSSEN"]')

spiValGrp_SPI1CON_MCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI1CON__MCLKSEL"]')
spiBitField_SPI1CON_MCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI1CON"]/bitfield@[name="MCLKSEL"]')

################################################################################
#### Global Variables ####
################################################################################

global spiInstanceName
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

def InterruptModeDependency(symbol, event):
    fault_enable = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_FAULT_INTERRUPT_ENABLE")
    rx_enable = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_RX_INTERRUPT_ENABLE")
    tx_enable = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_TX_INTERRUPT_ENABLE")
    if(event["id"] == "SPI_FAULT_INTERRUPT_ENABLE"):
        fault_enable = int(event["value"])
    elif(event["id"] == "SPI_RX_INTERRUPT_ENABLE"):
        rx_enable = int(event["value"])
    elif(event["id"] == "SPI_TX_INTERRUPT_ENABLE"):
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

def enableMenu(menu, event):
    menu.setVisible(event["value"])

def _get_enblReg_parms(vectorNumber):
    ##  This takes in vector index for interrupt, and returns the IECx register name as well as
    ##  mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/32)
        bitPosn = int(vectorNumber%32)
        bitMask = hex(1<<bitPosn)
        regName = "IEC"+str(index)
        return regName, str(bitPosn), str(bitMask)

def _get_statReg_parms(vectorNumber):
    ##  This takes in vector index for interrupt, and returns the IFSx register name as well as
    ##  mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/32)
        bitPosn = int(vectorNumber%32)
        bitMask = hex(1<<bitPosn)
        regName = "IFS"+str(index)
        return regName, str(bitPosn), str(bitMask)

def _get_sub_priority_parms(vectorNumber):
    ##  This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift,
    ##  and subpriority bitmask for input vector number
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber/4)
        subPrioBit = 8*(vectorNumber & 0x3)
        subPrioMask = 0x3  ##  always 2 bits
        prioMask = 0x7
        prioBit = subPrioBit + 2
        regName = "IPC"+str(index)
    return regName, str(prioBit), str(prioMask), str(subPrioBit), str(subPrioMask)

def _get_bitfield_names(node, outputList):
    valueNodes = node.getChildren()
    for ii in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):  ##  skip (unused) reserved fields
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')

            ##  Get rid of leading '0x', and convert to int if was hex
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)
            outputList.append(dict)

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

def combineValues(symbol, event):
    spi1conValue = symbol.getValue()
    if(event["id"] == "SPI_MSTR_MODE_EN"):
        mstenValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_MSTEN.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue = spi1conValue | (mstenValue<<5)
    if(event["id"] == "SPI_SPICON_CLK_POL"):
        clkpolValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_CKP.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue = spi1conValue | (clkpolValue<<6)
    if(event["id"] == "SPI_SPICON_CLK_PH"):
        clkphValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_CKE.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue  =  spi1conValue | (clkphValue<<8)
    if(event["id"] == "SPI_SPICON_MODE"):
        modeValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_MODE.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue  = spi1conValue | (modeValue <<10)
    if(event["id"] == "SPI_MASTER_CLOCK"):
        Value = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_MCLKSEL.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue  = spi1conValue | (Value <<23)
    if(event["id"] == "SPI_SPICON_MSSEN"):
        Value = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = spiBitField_SPI1CON_MSSEN.getAttribute("mask")
        spi1conValue = spi1conValue & (~int (maskvalue,0))
        spi1conValue  = spi1conValue | (Value <<28)
    symbol.setValue(spi1conValue, 2)

def combinefltIPC_Values(symbol, event):
    global spiFaultVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(spiFaultVectorNum)
    faultipc = symbol.getValue()
    if(event["id"] == "SPI_FLT_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        faultipc = faultipc & ~((int(pm))<< (int(ps)))
        faultipc = faultipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "SPI_FLT_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        faultipc = faultipc & ~((int(spm))<< (int(sps)))
        faultipc = faultipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(faultipc, 2)

def combineRXIPC_Values(symbol, event):
    global spiRxVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(spiRxVectorNum)
    rxipc = symbol.getValue()
    if(event["id"] == "SPI_RX_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        rxipc = rxipc & ~((int(pm))<< (int(ps)))
        rxipc = rxipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "SPI_RX_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        rxipc = rxipc & ~((int(spm))<< (int(sps)))
        rxipc = rxipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(rxipc, 2)

def combineTXIPC_Values(symbol, event):
    global spiTxVectorNum
    pr, ps, pm, sps, spm = _get_sub_priority_parms(spiTxVectorNum)
    txipc = symbol.getValue()
    if(event["id"] == "SPI_TX_IPC_PRI_VALUE"):
        ipcPriValue = int(event["symbol"].getValue())
        txipc = txipc & ~((int(pm))<< (int(ps)))
        txipc = txipc | (ipcPriValue<<(int (ps)))

    if(event["id"] == "SPI_TX_IPC_SUBPRI_VALUE"):
        ipcSPriValue = int(event["symbol"].getValue())
        txipc = txipc & ~((int(spm))<< (int(sps)))
        txipc = txipc | (ipcSPriValue<<(int (sps)))
    symbol.setValue(txipc, 2)

global dummyDataDict
dummyDataDict = {
                    "(AUDEN=1) 24-bit Data, 32-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 32-bit Data" : 0xFFFFFFFF,
                    "(AUDEN=1) 32-bit Data, 32-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 32-bit Data" : 0xFFFFFFFF,
                    "(AUDEN=1) 16-bit Data, 16-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 16-bit Data" : 0xFFFF,
                    "(AUDEN=1) 16-bit Data, 16-bit FIFO, 16-bit Channel/32-bit Frame/(AUDEN=0) 8-bit Data"  : 0xFF,
                }

##  Dependency Function to show or hide the warning message depending on Clock enable/disable status
def ClockStatusWarning(symbol, event):
    if event["value"] == False:
       symbol.setVisible(True)
    else:
       symbol.setVisible(False)

def ClockModeInfo(symbol, event):
    CPHAINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_PH")
    CPOLINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_POL")
    if event["id"] == "SPI_SPICON_CLK_PH":
        CPHA = int(event["symbol"].getKeyValue(event["value"]))
        CPOL = 1 if CPOLINDEX == 0 else 0
    elif event["id"] == "SPI_SPICON_CLK_POL":
        CPOL = int(event["symbol"].getKeyValue(event["value"]))
        CPHA = 1 if CPHAINDEX == 0 else 0
    if (CPOL == 0) and (CPHA == 0):
        symbol.setLabel("                                     ***SPI Mode 0 is Selected***")
    elif (CPOL == 0) and (CPHA == 1):
        symbol.setLabel("                                     ***SPI Mode 1 is Selected***")
    elif (CPOL == 1) and (CPHA == 0):
        symbol.setLabel("                                     ***SPI Mode 2 is Selected***")
    else:
        symbol.setLabel("                                     ***SPI Mode 3 is Selected***")

def getpb2ClockFreq():
    clkSympb2ClockFreq = Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ")
    return int(clkSympb2ClockFreq)

def getref1ClockFreq():
    clkSymrefclk1ClockFreq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))
    return int(clkSymrefclk1ClockFreq)

def showMasterDependencies(spiSym_MR_Dependencies, event):
    if event["symbol"].getKey(event["value"]) == "Master mode":
        spiSym_MR_Dependencies.setVisible(True)
    else:
        spiSym_MR_Dependencies.setVisible(False)

def spiMasterClkFreq(select):
    if(select == 1):
        clkFreq = getpb2ClockFreq()
    else:
        clkFreq = getref1ClockFreq()
    return clkFreq

def calculateBRGValue(clkfreq,baudRate):
    t_brg = ((int(clkfreq/baudRate)/2) - 1)
    baudHigh = int (clkfreq / (2 * (t_brg + 1)))
    baudLow = int (clkfreq / (2 * (t_brg + 2)))
    errorHigh = baudHigh - baudRate
    errorLow = baudRate - baudLow

    if (errorHigh > errorLow):
        t_brg +=1
    ## Baud rate register is a 13 bit register
    if t_brg < 0:
        t_brg = 0
        Log.writeErrorMessage("SPI Clock source Frequency is low for the desired baud rate")
    elif t_brg > 8191:
        t_brg = 8191
        Log.writeErrorMessage("Desired baud rate is low for current SPI Source Clock Frequency")
    return int(t_brg)

def SPIBRG_ValueUpdate(spiSym_SPIBRG_VALUE, event):
    clksectect = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_MASTER_CLOCK")
    BaudRate = int (Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_BAUD_RATE"))
    if event["id"] == "SPI_MASTER_CLOCK":
        if (int(event["value"]) == 0):
            clkFreq = int(getref1ClockFreq())
        elif (int(event["value"]) == 1):
            clkFreq = int(getpb2ClockFreq())
    elif event["id"] == "SPI_BAUD_RATE":
        ## This means there is change in baud rate provided by user in GUI
        BaudRate = int (event["value"])
        clkFreq = spiMasterClkFreq(clksectect)
    else:
        clkFreq = spiMasterClkFreq(clksectect)
    t_brg = calculateBRGValue(clkFreq,BaudRate)
    spiSym_SPIBRG_VALUE.setValue(t_brg, 1)

def SPI_MasterFreqValueUpdate(symbol,event):
    clksectect = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_MASTER_CLOCK")
    if event["id"] == "SPI_MASTER_CLOCK":
        if (int(event["value"]) == 0):
            clkFreq = int(getref1ClockFreq())
        elif (int(event["value"]) == 1):
            clkFreq = int(getpb2ClockFreq())
    else:
        clkFreq = spiMasterClkFreq(clksectect)
    symbol.setValue(clkFreq,1)

def DummyData_ValueUpdate(spiSymDummyData, event):
    spiSymDummyData.setValue(dummyDataDict[event["symbol"].getKey(event["value"])],1)
    spiSymDummyData.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])

def instantiateComponent(spiComponent):
    global spiInstanceName
    global spiInstanceNum
    global spiFaultVectorNum
    global spiRxVectorNum
    global spiTxVectorNum

    spiInstanceName = spiComponent.createStringSymbol("SPI_INSTANCE_NAME", None)
    spiInstanceName.setVisible(False)
    spiInstanceName.setDefaultValue(spiComponent.getID().upper())
    Log.writeInfoMessage("Running " + spiInstanceName.getValue())

    spiInstanceNum = spiComponent.createStringSymbol("SPI_INSTANCE_NUM", None)
    spiInstanceNum.setVisible(False)
    componentName = str(spiComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    spiInstanceNum.setDefaultValue(instanceNum)

    ## Interrrupt Setup Fault
    spiIrqFault = spiInstanceName.getValue()+ "_FAULT"
    spiFaultVectorNum = int(getIRQnumber(spiIrqFault))

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiFaultVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiFaultVectorNum)
    prioRegName, prioShift, prioMask, subprioShift, subprioMask = _get_sub_priority_parms(spiFaultVectorNum)

    ## IEC REG
    spiIEC = spiComponent.createStringSymbol("SPI_FLT_IEC_REG", None)
    spiIEC.setDefaultValue(enblRegName)
    spiIEC.setVisible(False)

    ## IFS REG
    spiIFS = spiComponent.createStringSymbol("SPI_FLT_IFS_REG", None)
    spiIFS.setDefaultValue(statRegName)
    spiIFS.setVisible(False)


    ## PRIORITY VALUE
    spiFaultVectorPriSym = "NVIC_" + str(spiFaultVectorNum) + "_0_PRIORITY"
    spiFltpriValue = Database.getSymbolValue("core",spiFaultVectorPriSym)
    spiIPC_PriValue = spiComponent.createHexSymbol("SPI_FLT_IPC_PRI_VALUE", None)
    spiIPC_PriValue.setDefaultValue(int(spiFltpriValue))
    spiIPC_PriValue.setVisible(False)
    spiIPC_PriValue.setDependencies(updateIRQValues, ["core." + spiFaultVectorPriSym])

    ## SUBPRIORITY VALUE
    spiFaultVectorSubPriSym = "NVIC_" + str(spiFaultVectorNum) + "_0_SUBPRIORITY"
    spiFltSubPriValue = Database.getSymbolValue("core",spiFaultVectorSubPriSym)
    spiIPC_SubpriValue = spiComponent.createHexSymbol("SPI_FLT_IPC_SUBPRI_VALUE", None)
    spiIPC_SubpriValue.setDefaultValue(int(spiFltSubPriValue))
    spiIPC_SubpriValue.setVisible(False)
    spiIPC_SubpriValue.setDependencies(updateIRQValues, ["core." + spiFaultVectorSubPriSym])

    ## IPC VALUE
    spiIPC_Val = spiComponent.createHexSymbol("SPI_FLT_IPC_VALUE", None)
    spiIPC_Val.setDefaultValue((int (spiIPC_PriValue.getDefaultValue()) << int(prioShift)) | (int (spiIPC_SubpriValue.getDefaultValue()) << int(subprioShift)))
    spiIPC_Val.setVisible(False)
    spiIPC_Val.setDependencies(combinefltIPC_Values, ["SPI_FLT_IPC_PRI_VALUE"])
    spiIPC_Val.setDependencies(combinefltIPC_Values, ["SPI_FLT_IPC_SUBPRI_VALUE"])

    ## HANDLER NAME
    spifaultVectorSym = "NVIC_" + str(spiFaultVectorNum) + "_0_HANDLER"
    faulthandlerValue = Database.getSymbolValue("core",spifaultVectorSym)
    spiIPC_handlerStr = spiComponent.createStringSymbol("SPI_ISR_FAULT_HANDLER_NAME", None)
    spiIPC_handlerStr.setDefaultValue(faulthandlerValue)
    spiIPC_handlerStr.setVisible(False)
    spiIPC_handlerStr.setDependencies(updateHandlerName, ["core." + spifaultVectorSym])

    ## SPI RX Interrupt
    spiIrqrx = spiInstanceName.getValue()+ "_RX"
    spiRxVectorNum = int(getIRQnumber(spiIrqrx))

    spirxenblRegName, spirxenblBitPosn, spirxenblMask = _get_enblReg_parms(spiRxVectorNum)
    spirxstatRegName, spirxstatBitPosn, spirxstatMask = _get_statReg_parms(spiRxVectorNum)
    spirxprioRegName, spirxprioShift, spirxprioMask, spirxsubprioShift, spirxsubprioMask = _get_sub_priority_parms(spiRxVectorNum)

    ## IEC REG
    spiRXIEC = spiComponent.createStringSymbol("SPI_RX_IEC_REG", None)
    spiRXIEC.setDefaultValue(spirxenblRegName)
    spiRXIEC.setVisible(False)

    ## IFS REG
    spiRXIFS = spiComponent.createStringSymbol("SPI_RX_IFS_REG", None)
    spiRXIFS.setDefaultValue(spirxstatRegName)
    spiRXIFS.setVisible(False)


    ## PRIORITY VALUE
    spiRxVectorPriSym = "NVIC_" + str(spiRxVectorNum) + "_0_PRIORITY"
    spiRxpriValue = Database.getSymbolValue("core",spiRxVectorPriSym)
    spiRXIPC_PriValue = spiComponent.createHexSymbol("SPI_RX_IPC_PRI_VALUE", None)
    spiRXIPC_PriValue.setDefaultValue(int(spiRxpriValue))
    spiRXIPC_PriValue.setVisible(False)
    spiRXIPC_PriValue.setDependencies(updateIRQValues, ["core."+ spiRxVectorPriSym])

    ## SUBPRIORITY VALUE
    spiRxVectorSubPriSym =  "NVIC_" + str(spiRxVectorNum) + "_0_SUBPRIORITY"
    spiRxSubPriValue = Database.getSymbolValue("core",spiRxVectorSubPriSym)
    spiRXIPC_SubpriValue = spiComponent.createHexSymbol("SPI_RX_IPC_SUBPRI_VALUE", None)
    spiRXIPC_SubpriValue.setDefaultValue(int(spiRxSubPriValue))
    spiRXIPC_SubpriValue.setVisible(False)
    spiRXIPC_SubpriValue.setDependencies(updateIRQValues, ["core."+ spiRxVectorSubPriSym])

    ## IPC VALUE
    spiRXIPC_Val = spiComponent.createHexSymbol("SPI_RX_IPC_VALUE", None)
    spiRXIPC_Val.setDefaultValue((int(spiRXIPC_PriValue.getDefaultValue()) << int(spirxprioShift)) | (int (spiRXIPC_SubpriValue.getDefaultValue()) << int(spirxsubprioShift)))
    spiRXIPC_Val.setVisible(False)
    spiRXIPC_Val.setDependencies(combineRXIPC_Values, ["SPI_RX_IPC_PRI_VALUE"])
    spiRXIPC_Val.setDependencies(combineRXIPC_Values, ["SPI_RX_IPC_SUBPRI_VALUE"])

    ## HANDLER NAME
    spiRxVectorSym = "NVIC_" + str(spiRxVectorNum) + "_0_HANDLER"
    spiRXIPC_handlerStr = spiComponent.createStringSymbol("SPI_ISR_RX_HANDLER_NAME", None)
    rxhandlerValue = Database.getSymbolValue("core",spiRxVectorSym)
    spiRXIPC_handlerStr.setDefaultValue(rxhandlerValue)
    spiRXIPC_handlerStr.setVisible(False)
    spiRXIPC_handlerStr.setDependencies(updateHandlerName, ["core." + spiRxVectorSym])

    ## SPI TX Interrupt
    spiIrqtx = spiInstanceName.getValue()+ "_TX"
    spiTxVectorNum = int(getIRQnumber(spiIrqtx))
    spitxenblRegName, spitxenblBitPosn, spitxenblMask = _get_enblReg_parms(spiTxVectorNum)
    spitxstatRegName, spitxstatBitPosn, spitxstatMask = _get_statReg_parms(spiTxVectorNum)
    spitxprioRegName, spitxprioShift, spitxprioMask, spitxsubprioShift, spitxsubprioMask = _get_sub_priority_parms(spiTxVectorNum)

    ## IEC REG
    spiTXIEC = spiComponent.createStringSymbol("SPI_TX_IEC_REG", None)
    spiTXIEC.setDefaultValue(spitxenblRegName)
    spiTXIEC.setVisible(False)

    ## IFS REG
    spiTXIFS = spiComponent.createStringSymbol("SPI_TX_IFS_REG", None)
    spiTXIFS.setDefaultValue(spitxstatRegName)
    spiTXIFS.setVisible(False)


    ## PRIORITY VALUE
    spiTxVectorPriSym = "NVIC_" + str(spiTxVectorNum) + "_0_PRIORITY"
    spiTxpriValue = Database.getSymbolValue("core",spiTxVectorPriSym)
    spiTXIPC_PriValue = spiComponent.createHexSymbol("SPI_TX_IPC_PRI_VALUE", None)
    spiTXIPC_PriValue.setDefaultValue(int(spiTxpriValue))
    spiTXIPC_PriValue.setVisible(False)
    spiTXIPC_PriValue.setDependencies(updateIRQValues, ["core." + spiTxVectorPriSym])

    ## SUBPRIORITY VALUE
    spiTxVectorSubPriSym = "NVIC_" + str(spiTxVectorNum) + "_0_SUBPRIORITY"
    spiTxSubPriValue = Database.getSymbolValue("core",spiTxVectorSubPriSym)
    spiTXIPC_SubpriValue = spiComponent.createHexSymbol("SPI_TX_IPC_SUBPRI_VALUE", None)
    spiTXIPC_SubpriValue.setDefaultValue(int(spiTxSubPriValue))
    spiTXIPC_SubpriValue.setVisible(False)
    spiTXIPC_SubpriValue.setDependencies(updateIRQValues, ["core." + spiTxVectorSubPriSym])

    ## IPC VALUE
    spiTXIPC_Val = spiComponent.createHexSymbol("SPI_TX_IPC_VALUE", None)
    spiTXIPC_Val.setDefaultValue((int(spiTXIPC_PriValue.getDefaultValue()) << int(spitxprioShift)) | (int (spiTXIPC_SubpriValue.getDefaultValue()) << int(spitxsubprioShift)))
    spiTXIPC_Val.setVisible(False)
    spiTXIPC_Val.setDependencies(combineTXIPC_Values, ["SPI_TX_IPC_PRI_VALUE"])
    spiTXIPC_Val.setDependencies(combineTXIPC_Values, ["SPI_TX_IPC_SUBPRI_VALUE"])

    ## TX HANDLER NAME
    spitxVectorSym = "NVIC_" + str(spiTxVectorNum) + "_0_HANDLER"
    spiTXIPC_handlerStr = spiComponent.createStringSymbol("SPI_ISR_TX_HANDLER_NAME", None)
    txhandlerValue = Database.getSymbolValue("core", spitxVectorSym)
    spiTXIPC_handlerStr.setDefaultValue(txhandlerValue)
    spiTXIPC_handlerStr.setVisible(False)
    spiTXIPC_handlerStr.setDependencies(updateHandlerName, ["core." + spitxVectorSym])

    ## MSTEN Selection Bit
    msten_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_MSTEN, msten_names)
    spiSym_SPICON_MSTEN = spiComponent.createKeyValueSetSymbol( "SPI_MSTR_MODE_EN",None)
    spiSym_SPICON_MSTEN.setLabel(spiBitField_SPI1CON_MSTEN.getAttribute("caption"))
    spiSym_SPICON_MSTEN.setDefaultValue(0)
    spiSym_SPICON_MSTEN.setReadOnly(True)
    spiSym_SPICON_MSTEN.setOutputMode( "Value" )
    spiSym_SPICON_MSTEN.setDisplayMode( "Description" )
    for ii in msten_names:
        spiSym_SPICON_MSTEN.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_MSTEN.setVisible(True)

    ## CLock Polarity
    clkpol_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_CKP, clkpol_names)
    spiSym_SPICON_CLKPOL = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_CLK_POL",None)
    spiSym_SPICON_CLKPOL.setLabel(spiBitField_SPI1CON_CKP.getAttribute("caption"))
    spiSym_SPICON_CLKPOL.setDefaultValue(1)
    spiSym_SPICON_CLKPOL.setOutputMode( "Value" )
    spiSym_SPICON_CLKPOL.setDisplayMode( "Description" )
    for ii in clkpol_names:
        spiSym_SPICON_CLKPOL.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_CLKPOL.setVisible(True)

    ## Clock Phase Bit
    clkph_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_CKE, clkph_names)
    spiSym_SPICON_CLKPH = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_CLK_PH",None)
    spiSym_SPICON_CLKPH.setLabel(spiBitField_SPI1CON_CKE.getAttribute("caption"))
    spiSym_SPICON_CLKPH.setDefaultValue(1)
    spiSym_SPICON_CLKPH.setOutputMode( "Value" )
    spiSym_SPICON_CLKPH.setDisplayMode( "Description" )
    for ii in clkph_names:
        spiSym_SPICON_CLKPH.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_CLKPH.setVisible(True)

    ## Slave slect pin enable bit
    ssen_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_MSSEN, ssen_names)
    spiSym_SPICON_MSSEN = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_MSSEN",None)
    spiSym_SPICON_MSSEN.setLabel(spiBitField_SPI1CON_MSSEN.getAttribute("caption"))
    spiSym_SPICON_MSSEN.setDefaultValue(0)
    spiSym_SPICON_MSSEN.setOutputMode( "Value" )
    spiSym_SPICON_MSSEN.setDisplayMode( "Description" )
    for ii in ssen_names:
        spiSym_SPICON_MSSEN.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_MSSEN.setVisible(True)

    ## SPI data width(Mode)
    mode_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_MODE, mode_names)
    spiSym_SPICON_MODE = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_MODE",None)
    spiSym_SPICON_MODE.setLabel(spiBitField_SPI1CON_MODE.getAttribute("caption"))
    spiSym_SPICON_MODE.setDefaultValue(3)
    spiSym_SPICON_MODE.setOutputMode( "Value" )
    spiSym_SPICON_MODE.setDisplayMode( "Description" )
    for ii in mode_names:
        spiSym_SPICON_MODE.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_MODE.setVisible(True)

    ## SPI Master clock
    msclk_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_MCLKSEL, msclk_names)
    spiSym_SPI1CON_MCLKSEL = spiComponent.createKeyValueSetSymbol( "SPI_MASTER_CLOCK",None)
    spiSym_SPI1CON_MCLKSEL.setLabel(spiBitField_SPI1CON_MCLKSEL.getAttribute("caption"))
    spiSym_SPI1CON_MCLKSEL.setDefaultValue(1)
    spiSym_SPI1CON_MCLKSEL.setOutputMode( "Value" )
    spiSym_SPI1CON_MCLKSEL.setReadOnly(False)
    spiSym_SPI1CON_MCLKSEL.setDisplayMode( "Description" )
    for ii in msclk_names:
        spiSym_SPI1CON_MCLKSEL.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPI1CON_MCLKSEL.setVisible(True)

    spiSym_SPI1CON_Value = spiComponent.createHexSymbol("SPICON_REG_VALUE",None)
    spiSym_SPI1CON_Value.setDefaultValue((int(spiSym_SPICON_MSTEN.getSelectedValue())<<5) | (int (spiSym_SPICON_CLKPOL.getSelectedValue())<<6) \
    | (int(spiSym_SPICON_CLKPH.getSelectedValue())<<8) | (int(spiSym_SPICON_MODE.getSelectedValue())<<10) | (int(spiSym_SPI1CON_MCLKSEL.getSelectedValue())<<23)\
    | (int(spiSym_SPICON_MSSEN.getSelectedValue())<<28))
    spiSym_SPI1CON_Value.setVisible(False)
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_MSTR_MODE_EN"])
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_SPICON_CLK_POL"])
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_SPICON_CLK_PH"])
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_SPICON_MODE"])
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_MASTER_CLOCK"])
    spiSym_SPI1CON_Value.setDependencies(combineValues,["SPI_SPICON_MSSEN"])


    defaultbaudRate = 1000000
    spiSym_Baud_Rate = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", None)
    spiSym_Baud_Rate.setLabel("Baud Rate in Hz")
    spiSym_Baud_Rate.setDefaultValue(defaultbaudRate)
    spiSym_Baud_Rate.setVisible(True)
    spiSym_Baud_Rate.setMin(1)
    spiSym_Baud_Rate.setDependencies(showMasterDependencies, ["SPI_MSTR_MODE_EN"])

    ## Baud Rate generation

    spimclk_Index = int(spiSym_SPI1CON_MCLKSEL.getValue())
    spiMasterFreq= spiMasterClkFreq(spimclk_Index)
    defaultSPIBR = calculateBRGValue(spiMasterFreq , defaultbaudRate)

    spiSym_SPIBRG_VALUE = spiComponent.createIntegerSymbol("SPI_BRG_VALUE", None)
    spiSym_SPIBRG_VALUE.setDefaultValue(defaultSPIBR)
    spiSym_SPIBRG_VALUE.setVisible(False)
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["SPI_BAUD_RATE"])
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["SPI_MASTER_CLOCK"])
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["CONFIG_SYS_CLK_PBCLK2_FREQ"])
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["CONFIG_SYS_CLK_REFCLK1_FREQ"])

    spiSym_MasterFreq_VALUE = spiComponent.createIntegerSymbol("SPI_MASTER_FREQ_VALUE", None)
    spiSym_MasterFreq_VALUE.setDefaultValue(spiMasterFreq)
    spiSym_MasterFreq_VALUE.setVisible(False)
    spiSym_MasterFreq_VALUE.setDependencies(SPI_MasterFreqValueUpdate, ["SPI_MASTER_CLOCK"])
    spiSym_MasterFreq_VALUE.setDependencies(SPI_MasterFreqValueUpdate, ["CONFIG_SYS_CLK_PBCLK2_FREQ"])
    spiSym_MasterFreq_VALUE.setDependencies(SPI_MasterFreqValueUpdate, ["CONFIG_SYS_CLK_REFCLK1_FREQ"])

    spiSymDummyData = spiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
    spiSymDummyData.setVisible(True)
    spiSymDummyData.setLabel("Dummy Data")
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setMin(0x0)
    spiSymDummyData.setDependencies(DummyData_ValueUpdate, ["SPI_SPICON_MODE"])

    spiSymClockModeComment = spiComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", None)
    spiSymClockModeComment.setVisible(True)
    spiSymClockModeComment.setLabel("                                     ***SPI Mode 0 Selected***")
    spiSymClockModeComment.setDependencies(ClockModeInfo, ["SPI_SPICON_CLK_POL","SPI_SPICON_CLK_PH"])
 

    ############################################################################
    #### Interrupt Dependency ####
    ############################################################################
    ## MIPS Interrupt Dynamic settings
    faultinterruptEnable = spiComponent.createBooleanSymbol("SPI_FAULT_INTERRUPT_ENABLE", None)
    faultinterruptEnable.setVisible(False)
    rxinterruptEnable = spiComponent.createBooleanSymbol("SPI_RX_INTERRUPT_ENABLE", None)
    rxinterruptEnable.setVisible(False)
    txinterruptEnable = spiComponent.createBooleanSymbol("SPI_TX_INTERRUPT_ENABLE", None)
    txinterruptEnable.setVisible(False)

    ## Fault Default Values
    faultVectorEnableSym = "NVIC_" + str(spiFaultVectorNum) + "_0_ENABLE"
    spifltSymIntEnComment = spiComponent.createCommentSymbol("SPI_FAULTINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", faultVectorEnableSym) == False):
        spifltSymIntEnComment.setVisible(True)
        faultinterruptEnable.setDefaultValue(False)
    else:
        spifltSymIntEnComment.setVisible(False)
        faultinterruptEnable.setDefaultValue(True)

    ## Fault Dependency
    spifltSymIntEnComment.setLabel("Warning!!! SPI" + str(instanceNum) + " Fault Interrupt is Disabled in Interrupt Manager")
    faultinterruptEnable.setDependencies(dependencyInterrupt, ["core." + faultVectorEnableSym])
    spifltSymIntEnComment.setDependencies(dependencyStatus, ["core." + faultVectorEnableSym])

    ## rx Default Values
    rxVectorEnableSym = "NVIC_" + str(spiRxVectorNum) + "_0_ENABLE"
    spirxSymIntEnComment = spiComponent.createCommentSymbol("SPI_RXINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", rxVectorEnableSym) == False):
        spirxSymIntEnComment.setVisible(True)
        rxinterruptEnable.setDefaultValue(False)
    else:
        spirxSymIntEnComment.setVisible(False)
        rxinterruptEnable.setDefaultValue(True)
     ## rx Dependency
    spirxSymIntEnComment.setLabel("Warning!!! SPI" + str(instanceNum) + " RX Interrupt is Disabled in Interrupt Manager")
    spirxSymIntEnComment.setDependencies(dependencyStatus, ["core." + rxVectorEnableSym])
    rxinterruptEnable.setDependencies(dependencyInterrupt, ["core." + rxVectorEnableSym])

    ## tx Default Values
    txVectorEnableSym = "NVIC_" + str(spiTxVectorNum) + "_0_ENABLE"
    spitxSymIntEnComment = spiComponent.createCommentSymbol("SPI_TXINTR_ENABLE_COMMENT", None)
    if(Database.getSymbolValue("core", txVectorEnableSym) == False):
        spitxSymIntEnComment.setVisible(True)
        txinterruptEnable.setDefaultValue(False)
    else:
        spitxSymIntEnComment.setVisible(False)
        txinterruptEnable.setDefaultValue(True)
     ## TX Dependency
    spitxSymIntEnComment.setLabel("Warning!!! SPI" + str(instanceNum) + " TX Interrupt is Disabled in Interrupt Manager")
    spitxSymIntEnComment.setDependencies(dependencyStatus, ["core." + txVectorEnableSym])
    txinterruptEnable.setDependencies(dependencyInterrupt, ["core." + txVectorEnableSym])

    spiSymInterruptMode = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiSymInterruptMode.setVisible(False)
    combineInterruptValue = faultinterruptEnable.getValue() & rxinterruptEnable.getValue() & txinterruptEnable.getValue()
    spiSymInterruptMode.setDefaultValue(combineInterruptValue)
    spiSymInterruptMode.setDependencies(InterruptModeDependency, ["SPI_FAULT_INTERRUPT_ENABLE"])
    spiSymInterruptMode.setDependencies(InterruptModeDependency, ["SPI_RX_INTERRUPT_ENABLE"])
    spiSymInterruptMode.setDependencies(InterruptModeDependency, ["SPI_TX_INTERRUPT_ENABLE"])

    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI_INTRRUPT_ENABLE_COMMENT", None)
    if(combineInterruptValue == 1):
        spiSymIntEnComment.setVisible(True)
        spiSymIntEnComment.setLabel("                                     ***INTERRUPT MODE Selected***")
    else:
        spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setDependencies(InterruptEnDependency,["SPI_INTERRUPT_MODE"])  
############################################################################
    #### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    spiHeaderFile = spiComponent.createFileSymbol("SPI_COMMON_HEADER", None)
    spiHeaderFile.setSourcePath("../peripheral/spi_01329/templates/plib_spi_common.h")
    spiHeaderFile.setOutputName("plib_spi_common.h")
    spiHeaderFile.setDestPath("peripheral/spi/")
    spiHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/")
    spiHeaderFile.setType("HEADER")
    spiHeaderFile.setMarkup(False)
    spiHeaderFile.setOverwrite(True)

    spiHeader1File = spiComponent.createFileSymbol("SPI_HEADER", None)
    spiHeader1File.setSourcePath("../peripheral/spi_01329/templates/plib_spi.h.ftl")
    spiHeader1File.setOutputName("plib_"+spiInstanceName.getValue().lower()+".h")
    spiHeader1File.setDestPath("/peripheral/spi/")
    spiHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiHeader1File.setType("HEADER")
    spiHeader1File.setMarkup(True)

    spiSource1File = spiComponent.createFileSymbol("SPI_SOURCE", None)
    spiSource1File.setSourcePath("../peripheral/spi_01329/templates/plib_spi.c.ftl")
    spiSource1File.setOutputName("plib_"+spiInstanceName.getValue().lower()+".c")
    spiSource1File.setDestPath("/peripheral/spi/")
    spiSource1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiSource1File.setType("SOURCE")
    spiSource1File.setMarkup(True)

    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_01329/templates/system/system_initialize.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_01329/templates/system/system_definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)
