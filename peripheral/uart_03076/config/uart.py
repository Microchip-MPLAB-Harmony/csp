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

#ATDF Helper Functions
def getModuleRegisterGroup(moduleName,registerGroup):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]'
    registerGroupNode = ATDF.getNode(atdfPath)
    if(registerGroupNode != None):
        return registerGroupNode.getChildren()
    return None

def getModuleRegisterData(moduleName,registerGroup,register):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
    registerNode = ATDF.getNode(atdfPath)
    if(registerNode != None):
        return registerNode.getChildren()
    return None

def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value

def getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         regDefaultVal = registerNode.getAttribute("initval")
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return getDefaultVal(regDefaultVal,bitMask)
     return 0


def getValueGroupName(moduleName,registerGroup,register,bitfield):
    bitNode = getBitField(moduleName,registerGroup,register,bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

def getValueGroup(moduleName,valueGroupName):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/value-group@[name="'+ valueGroupName + '"]'
    return ATDF.getNode(atdfPath)

def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
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
            optionList.append(dict)
    return optionList

def getKeyValuePairBasedonValue(value,keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find value in dictionary") # should never get here
    return ""

def addKeystoKeyValueSymbol(bitSymbol,bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey( ii['key'],ii['value'], ii['desc'] )

def setClockGeneratorData(valueGroupEntry):
    clkNode = getValueGroup(UART,valueGroupEntry).getChildren()
    for bitfield in clkNode:
        if "Clock Generator" in bitfield.getAttribute("caption"):
            return bitfield.getAttribute("caption")


def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield):
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            symbolKey = valueGroupEntry
            optionList = getBitfieldOptionList(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, None )
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp



################################################################################
#### String Constants ####
################################################################################

#System Component symbol names
CORE_COMPONENT = "core"
SYSTEM_FREQ_SYM = "stdSpeedClkFreq"
SOURCE = "source"

UART = "UART"
#UART ATDF based symbol names
U_CON_STP_KEY = getValueGroupName(UART,"U","CON","STP")
U_CON_CLKSEL_KEY = getValueGroupName(UART,"U","CON","CLKSEL")
U_CON__BRGS_KEY = getValueGroupName(UART,"U","CON","BRGS")
U_CON__CLKMOD_KEY = getValueGroupName(UART,"U","CON","CLKMOD")
U_CON__MODE_KEY = getValueGroupName(UART,"U","CON","MODE")

#UART general symbol names
OPERATING_MODE_KEY = "operatingMode"
RING_BUFFER_MODE_ENABLE_KEY = "ringBufferModeEnable"
INTERRUPT_MODE_KEY ="intEnable"
PARITY_DATA_MODE_KEY = U_CON__MODE_KEY
CLOCK_FREQ_KEY = "clockFreq"
CLOCK_GEN_FREQ_KEY = "clockGenFreq"
RING_BUF_CMNT_KEY = "ringBufComment"
TRANSMIT_BUF_KEY = "txBufferSize"
RECEIVE_BUF_KEY = "rxBufferSize"
BAUD_RATE_KEY = "baudRateVal"
BAUD_ERROR_COMMENT_KEY = "baudErrorCmnt"

BRG_REG_VALUE_KEY = "brgRegValue"
CLK_FREQ_KEY = "uartClkFreq"
CALC_BAUD_KEY = "calcBaudRateVal"

################################################################################
#### Business Logic ####
################################################################################

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

STANDARD_SPEED_PERIPHERAL_CLOCK = "Standard Speed Peripheral Clock"
CLOCK_GENERATOR = setClockGeneratorData(U_CON_CLKSEL_KEY)
CLK_GEN_FREQ_SYM = "clkGen" + CLOCK_GENERATOR[-1] + "OutFrequency"

def clockSourceSystemFreq(symbol, event):
    clockSelSym = event[SOURCE].getSymbolByID(U_CON_CLKSEL_KEY)
    clkEventName = event["id"]
    coreClkSymName =""
    if(clkEventName == U_CON_CLKSEL_KEY) :
        if clockSelSym.getSelectedKey() == STANDARD_SPEED_PERIPHERAL_CLOCK:
            coreClkSymName = SYSTEM_FREQ_SYM
        elif clockSelSym.getSelectedKey() == CLOCK_GENERATOR:
            coreClkSymName = CLK_GEN_FREQ_SYM
    elif clockSelSym.getSelectedKey() == STANDARD_SPEED_PERIPHERAL_CLOCK and clkEventName == SYSTEM_FREQ_SYM:
        coreClkSymName = SYSTEM_FREQ_SYM
    elif clockSelSym.getSelectedKey() == CLOCK_GENERATOR  and clkEventName == CLK_GEN_FREQ_SYM:
        coreClkSymName = CLK_GEN_FREQ_SYM
    symbol.setValue(int(Database.getSymbolValue(CORE_COMPONENT, coreClkSymName)))

def setCoreInterruptSymbols(value):
    for int in interruptEnableList:
        int = int.replace("core.", "")
        Database.setSymbolValue("core", int, value)
    for int in interruptHandlerLockList:
        int = int.replace("core.", "")
        Database.setSymbolValue("core", int, value)

def interruptEnableChange (symbol, event):
    setCoreInterruptSymbols(event["value"])

def updateOperatingMode (symbol, event):
    interruptModeSym = event[SOURCE].getSymbolByID(INTERRUPT_MODE_KEY)
    ringBufferModeSym = event[SOURCE].getSymbolByID(RING_BUFFER_MODE_ENABLE_KEY)
    updateInterruptSettings(symbol,interruptModeSym,ringBufferModeSym)

def updateInterruptSettings(uartModeSym,interruptModeSym,ringBufferModeSym):
    if uartModeSym.getSelectedKey() == "RING_BUFFER":
        interruptModeSym.setValue(True)
        interruptModeSym.setVisible(True)
        ringBufferModeSym.setValue(True)
    elif uartModeSym.getSelectedKey() == "NON_BLOCKING":
        interruptModeSym.setValue(True)
        interruptModeSym.setVisible(True)
        ringBufferModeSym.setValue(False)
    elif uartModeSym.getSelectedKey() == "BLOCKING":
        interruptModeSym.setValue(False)
        interruptModeSym.setVisible(False)
        ringBufferModeSym.setValue(False)

def updateSymbolVisibility(symbol, event):
    # Enable TX and RX ring buffer size option if Ring buffer is enabled.
    symbol.setVisible(event["value"])

def uartFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = event["value"]
    if componentID == "UART_HEADER":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_03076/templates/plib_uart_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/uart_03076/templates/plib_uart.h.ftl"
    elif componentID == "UART_SOURCE":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/uart_03076/templates/plib_uart_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/uart_03076/templates/plib_uart.c.ftl"

    symbol.setSourcePath(filepath)

def handleMessage(messageID, args):
    global uartSym_OperatingMode

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


def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]
    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def baudRateTrigger(symbol, event):
    getBaudSymParams(symbol.getComponent())

def getBaudSymParams(localComponent):
    clkFreq = int(localComponent.getSymbolByID(CLK_FREQ_KEY).getValue())
    reqBaudrate = int(localComponent.getSymbolByID(BAUD_RATE_KEY).getValue())
    baudErrorSym = localComponent.getSymbolByID(BAUD_ERROR_COMMENT_KEY)
    baudParams = getBaudParams(clkFreq,reqBaudrate)
    baudErrorSym.setLabel("Error Rate = " + str(baudParams["baudError"]) +"%")
    localComponent.setSymbolValue(BRG_REG_VALUE_KEY,str(baudParams["brg"]))
    localComponent.setSymbolValue(CALC_BAUD_KEY,str(baudParams["calcBaud"]))
    localComponent.setSymbolValue(U_CON__BRGS_KEY,str(baudParams["brgs"]))
    localComponent.setSymbolValue(U_CON__CLKMOD_KEY,str(baudParams["clkMod"]))


def getBaudParams(clkFreq,reqBaudrate):
    clkMod = 1
    brgs = 0
    brgMax = 0xfffff
    brg = 0
    minFracBrg = 16
    calcBaud = 0
    baudError = 0
    if((clkFreq > 0)  and (reqBaudrate > 0)):
        brg = round(float(clkFreq) / reqBaudrate)
        if(brg < minFracBrg or brg > brgMax):
            brg_4Div = min(round((clkFreq/(4*reqBaudrate))-1),brgMax)
            calcBaud_4DiV = clkFreq/(4*(brg_4Div+1))
            brg_16Div = min(round((clkFreq/(16*reqBaudrate))-1),brgMax)
            calcBaud_16DiV = clkFreq/(16*(brg_16Div+1))
            baudError_4Div = abs(reqBaudrate - calcBaud_4DiV)
            baudError_16Div = abs(reqBaudrate - calcBaud_16DiV)
            if(baudError_4Div <=  baudError_16Div):
                brgs = 1
                calcBaud = calcBaud_4DiV
                baudError = baudError_4Div
                brg= brg_4Div
            else:
                calcBaud = calcBaud_16DiV
                baudError = baudError_16Div
                brg= brg_16Div
            clkMod = 0
        else:
          calcBaud = clkFreq/brg
          baudError = abs(reqBaudrate - calcBaud)

    return {
        "brg" : hex(int(brg)),
        "calcBaud" : round(calcBaud,3),
        "baudError" :  round((baudError*100)/reqBaudrate,2),
        "clkMod" : clkMod,
        "brgs" : brgs
    }

#Interrupt related Helper Function

def getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList):
    intSymbolMap= {}
    intEntryCount = len(interruptList)
    intFlagList = [compPrefix+compInstance+interrupt+"IF" for interrupt in interruptList]
    flagRegisterGroup = getModuleRegisterGroup("intc","IFS")
    isflagDataAdded = False
    if(flagRegisterGroup != None):
        for registerNode in flagRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intFlagList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IF","").lower() + "InterruptFlagBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isflagDataAdded = True
                        break
            if isflagDataAdded:
                break

    intEntryCount = 2*intEntryCount
    isEnableDataAdded = False
    intEnableList = [compPrefix+compInstance+interrupt+"IE" for interrupt in interruptList]
    enableRegisterGroup = getModuleRegisterGroup("intc","IEC")
    if(enableRegisterGroup != None):
        for registerNode in enableRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intEnableList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IE","").lower() + "InterruptEnableBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break

    for interrupt in interruptList:
        intSymbolName = interrupt.lower() + "IsrHandlerName"
        intSymbolMap[intSymbolName] = compPrefix + compInstance +interrupt+"_InterruptHandler"

    return intSymbolMap

def createInterruptSymbols(component,intSymbolMap):
    for key in intSymbolMap:
        interruptSymbol = component.createStringSymbol(key, None)
        interruptSymbol.setDefaultValue(intSymbolMap[key])
        interruptSymbol.setVisible(False)

def updateInterruptLists(instanceNo, interruptList):
    for interrupt in interruptList:
        intIndex = getVectorIndex("U" + instanceNo +interrupt +"Interrupt")
        interruptEnableList.append("core.INTC_"+intIndex+"_ENABLE")
        interruptHandlerLockList.append("core.INTC_"+intIndex+"_HANDLER_LOCK")

def clockCommentCb(symbol, event):
    updateClockComment(symbol)

def updateClockComment(symbol):
    clockSelSym = symbol.getComponent().getSymbolByID(U_CON_CLKSEL_KEY)
    clockGenFreq = symbol.getComponent().getSymbolValue(CLK_FREQ_KEY)
    if clockSelSym.getSelectedKey() == CLOCK_GENERATOR  and clockGenFreq == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def interruptCommentCb(symbol, event):
    updateInterruptComment(symbol)

def updateInterruptComment(symbol):
    interruptState = symbol.getComponent().getSymbolValue(INTERRUPT_MODE_KEY)
    instance = str(symbol.getComponent().getSymbolValue("instanceNumber"))
    status = False
    for int in  interruptEnableList:
        int = int.replace("core.", "")
        if Database.getSymbolValue("core", int) != interruptState:
            status = True
            break
    if status:
        modeSym = symbol.getComponent().getSymbolByID(OPERATING_MODE_KEY)
        modeSymVal = modeSym.getKeyDescription(modeSym.getValue())
        val = "Enable" if interruptState else "Disable"
        symbol.setVisible(True)
        symbol.setLabel("Warning!!!  For "+modeSymVal+", " + val + " UART" + instance +" TX ,RX and Error Interrupts in Interrupts Section of System module")
    else:
        symbol.setVisible(False)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(uartComponent):
    global uartSym_OperatingMode
    global interruptEnableList
    global interruptHandlerLockList

    interruptEnableList = []
    interruptHandlerLockList = []

    # Operating Mode
    uartSym_OperatingMode = uartComponent.createKeyValueSetSymbol(OPERATING_MODE_KEY, None)
    uartSym_OperatingMode.setLabel("Operating Mode")
    uartSym_OperatingMode.addKey("BLOCKING", "0", "Blocking mode")
    uartSym_OperatingMode.addKey("NON_BLOCKING", "1", "Non-blocking mode")
    uartSym_OperatingMode.addKey("RING_BUFFER", "2", "Ring buffer mode")
    uartSym_OperatingMode.setDefaultValue(1)
    uartSym_OperatingMode.setDisplayMode("Description")
    uartSym_OperatingMode.setOutputMode("Key")
    uartSym_OperatingMode.setDependencies(updateOperatingMode, [OPERATING_MODE_KEY])

    # Interrupt Enable
    uartInterruptEnable = uartComponent.createBooleanSymbol(INTERRUPT_MODE_KEY,None)
    uartInterruptEnable.setLabel("Interrupt Enable")
    uartInterruptEnable.setReadOnly(True)
    uartInterruptEnable.setDependencies(interruptEnableChange, [INTERRUPT_MODE_KEY])

    #Enable Ring buffer
    uartSym_RingBufferMode_Enable = uartComponent.createBooleanSymbol(RING_BUFFER_MODE_ENABLE_KEY, None)
    uartSym_RingBufferMode_Enable.setLabel("Enable Ring Buffer ?")
    uartSym_RingBufferMode_Enable.setDefaultValue(False)
    uartSym_RingBufferMode_Enable.setReadOnly(True)
    uartSym_RingBufferMode_Enable.setVisible(False)

    # Tx and Rx Buffer Size
    uartSym_RingBufferSizeConfig = uartComponent.createCommentSymbol(RING_BUF_CMNT_KEY, None)
    uartSym_RingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
    uartSym_RingBufferSizeConfig.setVisible(False)
    uartSym_RingBufferSizeConfig.setDependencies(updateSymbolVisibility, [RING_BUFFER_MODE_ENABLE_KEY])

    uartSym_TXRingBuffer_Size = uartComponent.createIntegerSymbol(TRANSMIT_BUF_KEY, uartSym_RingBufferSizeConfig)
    uartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    uartSym_TXRingBuffer_Size.setMin(2)
    uartSym_TXRingBuffer_Size.setMax(65535)
    uartSym_TXRingBuffer_Size.setDefaultValue(128)
    uartSym_TXRingBuffer_Size.setVisible(False)
    uartSym_TXRingBuffer_Size.setDependencies(updateSymbolVisibility, [RING_BUFFER_MODE_ENABLE_KEY])

    uartSym_RXRingBuffer_Size = uartComponent.createIntegerSymbol(RECEIVE_BUF_KEY, uartSym_RingBufferSizeConfig)
    uartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    uartSym_RXRingBuffer_Size.setMin(2)
    uartSym_RXRingBuffer_Size.setMax(65535)
    uartSym_RXRingBuffer_Size.setDefaultValue(128)
    uartSym_RXRingBuffer_Size.setVisible(False)
    uartSym_RXRingBuffer_Size.setDependencies(updateSymbolVisibility, [RING_BUFFER_MODE_ENABLE_KEY])

    # STOP Selection Bit
    uartSym_UxMODE_STSEL = createKeyValueSetSymbol(uartComponent, UART, "U","CON","STP")
    uartSym_UxMODE_STSEL.setLabel("Stop Selection Bit")

    # Parity and Data Selection
    uartSym_ParityDataMode = uartComponent.createKeyValueSetSymbol(PARITY_DATA_MODE_KEY, None)
    uartSym_ParityDataMode.setLabel("Parity and Data Selection Bits")
    uartSym_ParityDataMode.addKey("8-bit data, no parity", "0", "8-bit data, no parity")
    uartSym_ParityDataMode.addKey("7-bit data, no parity", "1", "7-bit data, no parity")
    uartSym_ParityDataMode.addKey("8-bit data, even parity", "2", "8-bit data, odd parity")
    uartSym_ParityDataMode.addKey("8-bit data, odd parity", "3", "8-bit data, even parity")
    uartSym_ParityDataMode.setDefaultValue(0)
    uartSym_ParityDataMode.setDisplayMode("Description")
    uartSym_ParityDataMode.setOutputMode("Value")


    # Clock Selection
    uartSym_ClockSel = createKeyValueSetSymbol(uartComponent, UART, "U","CON","CLKSEL")
    uartSym_ClockSel.setLabel("Clock Selection")

    # UART Clock Frequency
    uartClkValue = uartComponent.createIntegerSymbol(CLK_FREQ_KEY, None)
    uartClkValue.setLabel("Clock Frequency(In Hz)")
    uartClkValue.setReadOnly(True)
    uartClkValue.setDefaultValue(int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_FREQ_SYM)))
    uartClkValue.setDependencies(clockSourceSystemFreq, [U_CON_CLKSEL_KEY,CORE_COMPONENT+"."+SYSTEM_FREQ_SYM,CORE_COMPONENT+"."+CLK_GEN_FREQ_SYM])

    # Baud Rate
    uartBaud = uartComponent.createIntegerSymbol(BAUD_RATE_KEY, None)
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(115200)
    uartBaud.setDependencies(baudRateTrigger,[BAUD_RATE_KEY,CLK_FREQ_KEY])

    # Error Rate
    uartError = uartComponent.createCommentSymbol(BAUD_ERROR_COMMENT_KEY, None)
    uartError.setLabel("*** Error Rate ***")


    # Code Generation
    moduleName = uartComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue(uartComponent.getID().upper())
    moduleName.setVisible(False)

    instanceNumber = uartComponent.createStringSymbol("instanceNumber", None)
    instanceNumber.setDefaultValue(uartComponent.getID().upper().replace(UART,""))
    instanceNumber.setVisible(False)

    clkSrcGenNumber = uartComponent.createStringSymbol("clkSrcGenNumber", None)
    clkSrcGenNumber.setDefaultValue(CLOCK_GENERATOR[-1])
    clkSrcGenNumber.setVisible(False)

    uconBrgsValue = uartComponent.createStringSymbol(U_CON__BRGS_KEY, None)
    uconBrgsValue.setVisible(False)

    uconClkmodValue = uartComponent.createStringSymbol(U_CON__CLKMOD_KEY, None)
    uconClkmodValue.setVisible(False)

    brgRegValue = uartComponent.createStringSymbol(BRG_REG_VALUE_KEY, None)
    brgRegValue.setVisible(False)

    baudRateVal = uartComponent.createStringSymbol(CALC_BAUD_KEY, None)
    baudRateVal.setVisible(False)

    # Interrupt Symbols from ATDF for Code Generation
    compPrefix = "U"
    compInstance = uartComponent.getID().upper().replace(UART,"")
    interruptList = ["RX" , "TX","E"]
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    intSymbolMap["errorInterruptEnableBit"] = intSymbolMap["eInterruptEnableBit"]
    intSymbolMap["errorIsrHandlerName"] = intSymbolMap["eIsrHandlerName"]
    intSymbolMap["errorInterruptFlagBit"] = intSymbolMap["eInterruptFlagBit"]
    del intSymbolMap["eInterruptEnableBit"]
    del intSymbolMap["eIsrHandlerName"]
    del intSymbolMap["eInterruptFlagBit"]
    createInterruptSymbols(uartComponent,intSymbolMap)

    updateInterruptLists(instanceNumber.getValue(),interruptList)

    intComment = uartComponent.createCommentSymbol("INTERRUPT_COMMENT", None)
    intComment.setVisible(False)
    intComment.setLabel("Warning!!! Peripheral Interrupt is Disabled in Interrupt Manager")
    intComment.setDependencies(interruptCommentCb, [INTERRUPT_MODE_KEY] + interruptEnableList)

    clkComment = uartComponent.createCommentSymbol("CLOCK_COMMENT", None)
    clkComment.setVisible(False)
    clkComment.setLabel("Warning!!! Enable and configure " +  CLOCK_GENERATOR + " in Clock Section of System Module")
    clkComment.setDependencies(clockCommentCb, [CLK_FREQ_KEY , U_CON_CLKSEL_KEY])

    #USART Driver Symbols Start
    #USART API Prefix
    usartSym_API_Prefix = uartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    usartSym_API_Prefix.setDefaultValue(moduleName.getValue())
    usartSym_API_Prefix.setVisible(False)

    #UART Stop 1-bit Mask
    usartSym_CON_STP_1_Mask = uartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    usartSym_CON_STP_1_Mask.setDefaultValue("0x0")
    usartSym_CON_STP_1_Mask.setVisible(False)

    #UART Stop 2-bit Mask
    usartSym_CON_STP_2_Mask = uartComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
    usartSym_CON_STP_2_Mask.setDefaultValue("0x200000")
    usartSym_CON_STP_2_Mask.setVisible(False)

    #UART EVEN Parity Mask
    uartSym_CON_MODE_EVEN_Mask = uartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    uartSym_CON_MODE_EVEN_Mask.setDefaultValue("0x3")
    uartSym_CON_MODE_EVEN_Mask.setVisible(False)

    #UART ODD Parity Mask
    uartSym_CON_MODE_ODD_Mask = uartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    uartSym_CON_MODE_ODD_Mask.setDefaultValue("0x2")
    uartSym_CON_MODE_ODD_Mask.setVisible(False)

    #UART NO Parity Mask
    uartSym_CON_MODE_NO_Mask = uartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    uartSym_CON_MODE_NO_Mask.setDefaultValue("0x0")
    uartSym_CON_MODE_NO_Mask.setVisible(False)

    #UART Character Size 8 Mask
    usartSym_CON_MODE_8_Mask = uartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    usartSym_CON_MODE_8_Mask.setDefaultValue("0x0")
    usartSym_CON_MODE_8_Mask.setVisible(False)

    #UART Overrun error Mask
    usartSym_STAT_RXFOIF_Mask = uartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    usartSym_STAT_RXFOIF_Mask.setDefaultValue("0x2")
    usartSym_STAT_RXFOIF_Mask.setVisible(False)

    #UART parity error Mask
    usartSym_STAT_PERIF_Mask = uartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    usartSym_STAT_PERIF_Mask.setDefaultValue("0x40")
    usartSym_STAT_PERIF_Mask.setVisible(False)

    #UART framing error Mask
    usartSym_STAT_FERIF_Mask = uartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    usartSym_STAT_FERIF_Mask.setDefaultValue("0x8")
    usartSym_STAT_FERIF_Mask.setVisible(False)

    #UART data width
    uartSym_DataBits = uartComponent.createStringSymbol("USART_DATA_BITS", None)
    uartSym_DataBits.setDefaultValue("DRV_USART_DATA_8_BIT")
    uartSym_DataBits.setVisible(False)

    #UART Transmit data register
    uartSym_TxRegister = uartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    uartSym_TxRegister.setDefaultValue("&(U" + instanceNumber.getValue() + "TXB)")
    uartSym_TxRegister.setVisible(False)

    #UART Receive data register
    uartSym_RxRegister = uartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    uartSym_RxRegister.setDefaultValue("&(U" + instanceNumber.getValue() + "RXB)")
    uartSym_RxRegister.setVisible(False)
    #USART Driver Symbols End

    #File Handling
    configName = Variables.get("__CONFIGURATION_NAME")

    uartCommonHeaderFile = uartComponent.createFileSymbol("UART_COMMON_HEADER", None)
    uartCommonHeaderFile.setSourcePath("../peripheral/uart_03076/templates/plib_uart_common.h.ftl")
    uartCommonHeaderFile.setOutputName("plib_uart_common.h")
    uartCommonHeaderFile.setDestPath("peripheral/uart/")
    uartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartCommonHeaderFile.setType("HEADER")
    uartCommonHeaderFile.setMarkup(False)
    uartCommonHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeader1File.setSourcePath("../peripheral/uart_03076/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_" + moduleName.getValue().lower() + ".h")
    uartHeader1File.setDestPath("/peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)
    uartHeader1File.setDependencies(uartFileGeneration, [RING_BUFFER_MODE_ENABLE_KEY])

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE", None)
    uartSource1File.setSourcePath("../peripheral/uart_03076/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_" + moduleName.getValue().lower() + ".c")
    uartSource1File.setDestPath("/peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)
    uartSource1File.setDependencies(uartFileGeneration, [RING_BUFFER_MODE_ENABLE_KEY])

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_03076/templates/system/initialization.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_03076/templates/system/definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)

    #Load Time calculations
    getBaudSymParams(uartBaud.getComponent())
    updateInterruptSettings(uartSym_OperatingMode,uartInterruptEnable,uartSym_RingBufferMode_Enable)
    setCoreInterruptSymbols(uartInterruptEnable.getValue())
    updateInterruptComment(intComment)





