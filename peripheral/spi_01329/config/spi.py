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

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

global dummyDataDict
dummyDataDict = {
                    "(AUDEN=1) 24-bit Data, 32-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 32-bit Data" : 0xFFFFFFFF,
                    "(AUDEN=1) 32-bit Data, 32-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 32-bit Data" : 0xFFFFFFFF,
                    "(AUDEN=1) 16-bit Data, 16-bit FIFO, 32-bit Channel/64-bit Frame/(AUDEN=0) 16-bit Data" : 0xFFFF,
                    "(AUDEN=1) 16-bit Data, 16-bit FIFO, 16-bit Channel/32-bit Frame/(AUDEN=0) 8-bit Data"  : 0xFF,
                }

################################################################################
#### Business Logic ####
################################################################################

def setSPIInterruptData(status):

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

def updateSPIInterruptData(symbol, event):

    if event["id"] == "SPI_INTERRUPT_MODE":
        setSPIInterruptData(event["value"])

    status = False

    for id in InterruptVectorUpdate:
        id = id.replace("core.", "")
        if Database.getSymbolValue("core", id) == True:
            status = True
            break

    if spiSymInterruptMode.getValue() == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

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

def ClockModeInfo(symbol, event):

    CKEINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_PH")
    CPOLINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_POL")

    if event["id"] == "SPI_SPICON_CLK_PH":
        CKE = int(event["symbol"].getKeyValue(event["value"]))
        CPOL = 1 if CPOLINDEX == 0 else 0
    elif event["id"] == "SPI_SPICON_CLK_POL":
        CPOL = int(event["symbol"].getKeyValue(event["value"]))
        CKE = 1 if CKEINDEX == 0 else 0

    if (CPOL == 0) and (CKE == 1):
        symbol.setLabel("***SPI Mode 0 is Selected***")
    elif (CPOL == 0) and (CKE == 0):
        symbol.setLabel("***SPI Mode 1 is Selected***")
    elif (CPOL == 1) and (CKE == 1):
        symbol.setLabel("***SPI Mode 2 is Selected***")
    else:
        symbol.setLabel("***SPI Mode 3 is Selected***")

def showMasterDependencies(symbol, event):

    if event["symbol"].getKey(event["value"]) == "Master mode":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def calculateBRGValue(clkfreq, baudRate):

    t_brg = 0

    if clkfreq != 0 and baudRate != 0:
        t_brg = ((int(clkfreq/baudRate) / 2) - 1)
        baudHigh = int (clkfreq / (2 * (t_brg + 1)))
        baudLow = int (clkfreq / (2 * (t_brg + 2)))
        errorHigh = baudHigh - baudRate
        errorLow = baudRate - baudLow

        if errorHigh > errorLow:
            t_brg +=1

    spiSym_BaudError_Comment.setVisible(False)

    ## Baud rate register is a 9/13 bit register
    if t_brg < 0:
        t_brg = 0
        spiSym_BaudError_Comment.setVisible(True)
    elif t_brg > spiSymMaxBRG.getValue():
        t_brg = spiSymMaxBRG.getValue()
        spiSym_BaudError_Comment.setVisible(True)

    return int(t_brg)

def SPIBRG_ValueUpdate(symbol, event):
    clkFreq = int(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    BaudRate = int (Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_BAUD_RATE"))

    if event["id"] == "SPI_BAUD_RATE":
        BaudRate = int(event["value"])
    elif "_CLOCK_FREQUENCY" in event["id"]:
        clkFreq = int(event["value"])

    t_brg = calculateBRGValue(clkFreq, BaudRate)
    symbol.setValue(t_brg, 1)

def DummyData_ValueUpdate(symbol, event):

    symbol.setValue(dummyDataDict[event["symbol"].getKey(event["value"])], 1)

    symbol.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])

def updateSPIClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def instantiateComponent(spiComponent):

    global spiSym_BaudError_Comment
    global spiInstanceName
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global InterruptVectorUpdate
    global spiSymInterruptMode
    global spiSymMaxBRG

    InterruptVector = []
    InterruptHandler = []
    InterruptHandlerLock = []
    InterruptVectorUpdate = []

    spiInstanceName = spiComponent.createStringSymbol("SPI_INSTANCE_NAME", None)
    spiInstanceName.setVisible(False)
    spiInstanceName.setDefaultValue(spiComponent.getID().upper())
    Log.writeInfoMessage("Running " + spiInstanceName.getValue())

    spiInstanceNum = spiComponent.createStringSymbol("SPI_INSTANCE_NUM", None)
    spiInstanceNum.setVisible(False)
    componentName = str(spiComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    spiInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    spiSymInterruptMode = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiSymInterruptMode.setLabel("Enable Interrrupts ?")
    spiSymInterruptMode.setDefaultValue(True)

    spiIrq = "SPI_" + spiInstanceNum.getValue()
    spiVectorNum = getVectorIndex(spiIrq)

    if spiVectorNum != "-1":
        InterruptVector.append(spiIrq + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrq + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrq + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrq + "_INTERRUPT_ENABLE_UPDATE")

        ## SPI Error IRQ
        spiIrqFault = spiInstanceName.getValue() + "_ERR"
        spiFaultVectorNum = int(getIRQIndex(spiIrqFault))

        ## SPI RX IRQ
        spiIrqrRx = spiInstanceName.getValue() + "_RX"
        spiRxVectorNum = int(getIRQIndex(spiIrqrRx))

        ## SPI TX IRQ
        spiIrqTx = spiInstanceName.getValue() + "_TX"
        spiTxVectorNum = int(getIRQIndex(spiIrqTx))
    else:
        ## SPI Fault Interrrupt
        spiIrqFault = spiInstanceName.getValue() + "_FAULT"
        spiFaultVectorNum = int(getVectorIndex(spiIrqFault))

        ## SPI RX Interrupt
        spiIrqrRx = spiInstanceName.getValue() + "_RX"
        InterruptVector.append(spiIrqrRx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrqrRx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrqrRx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrqrRx + "_INTERRUPT_ENABLE_UPDATE")
        spiRxVectorNum = int(getVectorIndex(spiIrqrRx))

        ## SPI TX Interrupt
        spiIrqTx = spiInstanceName.getValue() + "_TX"
        InterruptVector.append(spiIrqTx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrqTx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrqTx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrqTx + "_INTERRUPT_ENABLE_UPDATE")
        spiTxVectorNum = int(getVectorIndex(spiIrqTx))

    spiInterruptCount = spiComponent.createIntegerSymbol("SPI_INTERRUPT_COUNT", None)
    spiInterruptCount.setDefaultValue(len(InterruptVector))
    spiInterruptCount.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiFaultVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiFaultVectorNum)

    ## IEC REG
    spiIEC = spiComponent.createStringSymbol("SPI_FLT_IEC_REG", None)
    spiIEC.setDefaultValue(enblRegName)
    spiIEC.setVisible(False)

    ## IEC REG MASK
    spiIECMask = spiComponent.createStringSymbol("SPI_FLT_IEC_REG_MASK", None)
    spiIECMask.setDefaultValue(enblMask)
    spiIECMask.setVisible(False)

    ## IFS REG
    spiIFS = spiComponent.createStringSymbol("SPI_FLT_IFS_REG", None)
    spiIFS.setDefaultValue(statRegName)
    spiIFS.setVisible(False)

    ## IFS REG MASK
    spiIFSMask = spiComponent.createStringSymbol("SPI_FLT_IFS_REG_MASK", None)
    spiIFSMask.setDefaultValue(statMask)
    spiIFSMask.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiRxVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiRxVectorNum)

    ## IEC REG
    spiRXIEC = spiComponent.createStringSymbol("SPI_RX_IEC_REG", None)
    spiRXIEC.setDefaultValue(enblRegName)
    spiRXIEC.setVisible(False)

    ## IEC REG MASK
    spiRXIECMask = spiComponent.createStringSymbol("SPI_RX_IEC_REG_MASK", None)
    spiRXIECMask.setDefaultValue(enblMask)
    spiRXIECMask.setVisible(False)

    ## IFS REG
    spiRXIFS = spiComponent.createStringSymbol("SPI_RX_IFS_REG", None)
    spiRXIFS.setDefaultValue(statRegName)
    spiRXIFS.setVisible(False)

    ## IFS REG MASK
    spiRXIFSMask = spiComponent.createStringSymbol("SPI_RX_IFS_REG_MASK", None)
    spiRXIFSMask.setDefaultValue(statMask)
    spiRXIFSMask.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiTxVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiTxVectorNum)

    ## IEC REG
    spiTXIEC = spiComponent.createStringSymbol("SPI_TX_IEC_REG", None)
    spiTXIEC.setDefaultValue(enblRegName)
    spiTXIEC.setVisible(False)

    ## IEC REG MASK
    spiTXIECMask = spiComponent.createStringSymbol("SPI_TX_IEC_REG_MASK", None)
    spiTXIECMask.setDefaultValue(enblMask)
    spiTXIECMask.setVisible(False)

    ## IFS REG
    spiTXIFS = spiComponent.createStringSymbol("SPI_TX_IFS_REG", None)
    spiTXIFS.setDefaultValue(statRegName)
    spiTXIFS.setVisible(False)

    ## IFS REG MASK
    spiTXIFSMask = spiComponent.createStringSymbol("SPI_TX_IFS_REG_MASK", None)
    spiTXIFSMask.setDefaultValue(statMask)
    spiTXIFSMask.setVisible(False)

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

    ## Clock Phase Bit
    clkph_names = []
    _get_bitfield_names(spiValGrp_SPI1CON_CKE, clkph_names)
    spiSym_SPICON_CLKPH = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_CLK_PH",None)
    spiSym_SPICON_CLKPH.setLabel(spiBitField_SPI1CON_CKE.getAttribute("caption"))
    spiSym_SPICON_CLKPH.setDefaultValue(0)
    spiSym_SPICON_CLKPH.setOutputMode( "Value" )
    spiSym_SPICON_CLKPH.setDisplayMode( "Description" )
    for ii in clkph_names:
        spiSym_SPICON_CLKPH.addKey( ii['key'],ii['value'], ii['desc'] )

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

    spiSym_Baud_Rate = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", None)
    spiSym_Baud_Rate.setLabel("Baud Rate in Hz")
    spiSym_Baud_Rate.setDefaultValue(1000000)
    spiSym_Baud_Rate.setMin(1)
    spiSym_Baud_Rate.setMax(50000000)
    spiSym_Baud_Rate.setDependencies(showMasterDependencies, ["SPI_MSTR_MODE_EN"])

    #SPI Baud Rate not supported comment
    spiSym_BaudError_Comment = spiComponent.createCommentSymbol("SPI_BAUD_ERROR_COMMENT", None)
    spiSym_BaudError_Comment.setLabel("********** WARNING!: Baud Rate is out of range **********")
    spiSym_BaudError_Comment.setVisible(False)

    spixBRG = spiInstanceName.getValue() + "BRG"
    spixBRG_Bitfield = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="' + spixBRG + '"]/bitfield@[name="' + spixBRG + '"]')
    spiMaxBRG = int(str(spixBRG_Bitfield.getAttribute("mask")), 0)

    spiSymMaxBRG = spiComponent.createIntegerSymbol("SPI_MAX_BRG", None)
    spiSymMaxBRG.setDefaultValue(spiMaxBRG)
    spiSymMaxBRG.setVisible(False)

    ## Baud Rate generation
    spiDefaultMasterFreq = int(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    defaultSPIBR = calculateBRGValue(spiDefaultMasterFreq, spiSym_Baud_Rate.getValue())

    spiSym_SPIBRG_VALUE = spiComponent.createIntegerSymbol("SPI_BRG_VALUE", None)
    spiSym_SPIBRG_VALUE.setVisible(False)
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["SPI_BAUD_RATE", "core." + spiInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Use setValue instead of setDefaultValue to store symbol value in default.xml
    spiSym_SPIBRG_VALUE.setValue(defaultSPIBR, 1)

    spiSymDummyData = spiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
    spiSymDummyData.setLabel("Dummy Data")
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setMin(0x0)
    spiSymDummyData.setDependencies(DummyData_ValueUpdate, ["SPI_SPICON_MODE"])

    spiSymClockModeComment = spiComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", None)
    spiSymClockModeComment.setLabel("***SPI Mode 0 Selected***")
    spiSymClockModeComment.setDependencies(ClockModeInfo, ["SPI_SPICON_CLK_POL", "SPI_SPICON_CLK_PH"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    setSPIInterruptData(spiSymInterruptMode.getValue())

    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI_INTRRUPT_ENABLE_COMMENT", None)
    spiSymIntEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setDependencies(updateSPIInterruptData, ["SPI_INTERRUPT_MODE"] + InterruptVectorUpdate)

    # Clock Warning status
    spiSym_ClkEnComment = spiComponent.createCommentSymbol("SPI_CLOCK_ENABLE_COMMENT", None)
    spiSym_ClkEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    spiSym_ClkEnComment.setVisible(False)
    spiSym_ClkEnComment.setDependencies(updateSPIClockWarningStatus, ["core." + spiInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Driver Symbols ############################################
    ###################################################################################################

    #SPI 8-bit Character size Mask
    spiSym_CHSIZE_8BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
    spiSym_CHSIZE_8BIT.setDefaultValue("0x00000000")
    spiSym_CHSIZE_8BIT.setVisible(False)

    #SPI 16-bit Character size Mask
    spiSym_CHSIZE_16BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", None)
    spiSym_CHSIZE_16BIT.setDefaultValue("0x00000400")
    spiSym_CHSIZE_16BIT.setVisible(False)

    #SPI 32-bit Character size Mask
    spiSym_CHSIZE_32BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_32_BIT_MASK", None)
    spiSym_CHSIZE_32BIT.setDefaultValue("0x00000800")
    spiSym_CHSIZE_32BIT.setVisible(False)

    #SPI Clock Phase Leading Edge Mask
    spiSym_CPHA_LE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CPHA_LE_Mask.setDefaultValue("0x00000100")
    spiSym_CPHA_LE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CPHA_TE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CPHA_TE_Mask.setDefaultValue("0x00000000")
    spiSym_CPHA_TE_Mask.setVisible(False)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CPOL_IL_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CPOL_IL_Mask.setDefaultValue("0x00000000")
    spiSym_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CPOL_IH_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CPOL_IH_Mask.setDefaultValue("0x00000040")
    spiSym_CPOL_IH_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = spiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue(spiInstanceName.getValue())
    spiSym_API_Prefix.setVisible(False)

    #SPI Transmit data register
    transmitRegister = spiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+spiInstanceName.getValue()+"BUF)")
    transmitRegister.setVisible(False)

    #SPI Receive data register
    receiveRegister = spiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+spiInstanceName.getValue()+"BUF)")
    receiveRegister.setVisible(False)

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
    spiHeader1File.setOutputName("plib_" + spiInstanceName.getValue().lower() + ".h")
    spiHeader1File.setDestPath("/peripheral/spi/")
    spiHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiHeader1File.setType("HEADER")
    spiHeader1File.setMarkup(True)

    spiSource1File = spiComponent.createFileSymbol("SPI_SOURCE", None)
    spiSource1File.setSourcePath("../peripheral/spi_01329/templates/plib_spi.c.ftl")
    spiSource1File.setOutputName("plib_" + spiInstanceName.getValue().lower() + ".c")
    spiSource1File.setDestPath("/peripheral/spi/")
    spiSource1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiSource1File.setType("SOURCE")
    spiSource1File.setMarkup(True)

    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_01329/templates/system/initialization.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_01329/templates/system/definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)
