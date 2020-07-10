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

dbguValGrp_MR_PAR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DBGU"]/value-group@[name="DBGU_MR__PAR"]')

dbguBitField_MR_FILTER = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DBGU"]/register-group@[name="DBGU"]/register@[name="DBGU_MR"]/bitfield@[name="FILTER"]')
dbguCaption_MR_FILTER = dbguBitField_MR_FILTER.getAttribute("caption")

################################################################################
#### Global Variables ####
################################################################################
global dbguInstanceName

################################################################################
#### Business Logic ####
################################################################################
def handleMessage(messageID, args):
    global dbguSym_RingBuffer_Enable
    global dbguInterrupt
    result_dict = {}

    if (messageID == "UART_RING_BUFFER_MODE"):
        if args.get("isReadOnly") != None:
            dbguSym_RingBuffer_Enable.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            dbguSym_RingBuffer_Enable.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            dbguSym_RingBuffer_Enable.setVisible(args["isVisible"])
    elif (messageID == "UART_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            dbguInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            dbguInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            dbguInterrupt.setVisible(args["isVisible"])

    return result_dict

def interruptControl(dbguInt, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, dbguInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, dbguInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyStatus(symbol, event):
    if (Database.getSymbolValue(dbguInstanceName.getValue().lower(), "USART_INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

def clockWarningVisible(symbol, event):
    symbol.setVisible(not event["value"])

# Calculates BRG value
def baudRateCalc(clk, baud):
    global dbguClockInvalidSym
    brgVal = (clk / (16 * baud))
    dbguClockInvalidSym.setVisible((brgVal < 1) or (brgVal > 65535) )
    return brgVal

def baudRateTrigger(symbol, event):
    clk = Database.getSymbolValue("core", dbguInstanceName.getValue() + "_CLOCK_FREQUENCY")
    baud = Database.getSymbolValue(dbguInstanceName.getValue().lower(), "BAUD_RATE")
    brgVal = baudRateCalc(clk, baud)
    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):
    symbol.setValue(int(Database.getSymbolValue("core", dbguInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def updateSymbolVisibility(symbol, event):
    global dbguSym_RingBuffer_Enable
    global dbguInterrupt

    # Enable RX ring buffer size option if Ring buffer is enabled.
    if symbol.getID() == "DBGU_RX_RING_BUFFER_SIZE":
        symbol.setVisible(dbguSym_RingBuffer_Enable.getValue())
    # Enable TX ring buffer size option if Ring buffer is enabled.
    elif symbol.getID() == "DBGU_TX_RING_BUFFER_SIZE":
        symbol.setVisible(dbguSym_RingBuffer_Enable.getValue())
    # If Interrupt is enabled, make ring buffer option visible
    # Further, if Interrupt is disabled, disable the ring buffer mode
    elif symbol.getID() == "DBGU_RING_BUFFER_ENABLE":
        symbol.setVisible(dbguInterrupt.getValue())
        if (dbguInterrupt.getValue() == False):
            readOnlyState = symbol.getReadOnly()
            symbol.setReadOnly(True)
            symbol.setValue(False)
            symbol.setReadOnly(readOnlyState)

def DBGUFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = event["value"]

    if componentID == "DBGU_HEADER":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/dbgu_6059/templates/plib_dbgu_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/dbgu_6059/templates/plib_dbgu.h.ftl"
    elif componentID == "DBGU_SOURCE":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/dbgu_6059/templates/plib_dbgu_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/dbgu_6059/templates/plib_dbgu.c.ftl"

    symbol.setSourcePath(filepath)

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
def instantiateComponent(dbguComponent):
    global dbguInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global dbguClockInvalidSym
    global dbguInterrupt
    global dbguSym_RingBuffer_Enable

    dbguInstanceName = dbguComponent.createStringSymbol("DBGU_INSTANCE_NAME", None)
    dbguInstanceName.setVisible(False)
    dbguInstanceName.setDefaultValue(dbguComponent.getID().upper())

    # The STDIO module looks for USART_INTERRUPT_MODE to disable interrupts so name our
    # variable accordingly to inter-operate correctly
    dbguInterrupt = dbguComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    dbguInterrupt.setLabel("Interrupt Mode")
    dbguInterrupt.setDefaultValue(True)

    #Enable Ring buffer?
    dbguSym_RingBuffer_Enable = dbguComponent.createBooleanSymbol("DBGU_RING_BUFFER_ENABLE", None)
    dbguSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
    dbguSym_RingBuffer_Enable.setDefaultValue(False)
    dbguSym_RingBuffer_Enable.setVisible(Database.getSymbolValue(dbguInstanceName.getValue().lower(), "USART_INTERRUPT_MODE"))
    dbguSym_RingBuffer_Enable.setDependencies(updateSymbolVisibility, ["USART_INTERRUPT_MODE"])

    dbguSym_TXRingBuffer_Size = dbguComponent.createIntegerSymbol("DBGU_TX_RING_BUFFER_SIZE", dbguSym_RingBuffer_Enable)
    dbguSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
    dbguSym_TXRingBuffer_Size.setMin(2)
    dbguSym_TXRingBuffer_Size.setMax(65535)
    dbguSym_TXRingBuffer_Size.setDefaultValue(128)
    dbguSym_TXRingBuffer_Size.setVisible(False)
    dbguSym_TXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["DBGU_RING_BUFFER_ENABLE"])

    dbguSym_RXRingBuffer_Size = dbguComponent.createIntegerSymbol("DBGU_RX_RING_BUFFER_SIZE", dbguSym_RingBuffer_Enable)
    dbguSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
    dbguSym_RXRingBuffer_Size.setMin(2)
    dbguSym_RXRingBuffer_Size.setMax(65535)
    dbguSym_RXRingBuffer_Size.setDefaultValue(128)
    dbguSym_RXRingBuffer_Size.setVisible(False)
    dbguSym_RXRingBuffer_Size.setDependencies(updateSymbolVisibility, ["DBGU_RING_BUFFER_ENABLE"])

    dbguClkSrc = dbguComponent.createKeyValueSetSymbol("DBGU_CLK_SRC", None)
    dbguClkSrc.setLabel("Select Clock Source")
    dbgu_clock = []
    node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DBGU"]/value-group@[name="DBGU_MR__BRSRCCK"]')
    dbgu_clock = node.getChildren()
    for clock in range(0, len(dbgu_clock)):
        dbguClkSrc.addKey(dbgu_clock[clock].getAttribute("name"), dbgu_clock[clock].getAttribute("value"), dbgu_clock[clock].getAttribute("caption"))
    dbguClkSrc.setDisplayMode("Key")
    dbguClkSrc.setOutputMode("Value")
    dbguClkSrc.setDefaultValue(0)

    dbguClkValue = dbguComponent.createIntegerSymbol("DBGU_CLOCK_FREQ", None)
    dbguClkValue.setLabel("Clock Frequency")
    dbguClkValue.setReadOnly(True)
    dbguClkValue.setDependencies(clockSourceFreq, ["DBGU_CLK_SRC", "core." + dbguInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    dbguClkValue.setDefaultValue(int(Database.getSymbolValue("core", dbguInstanceName.getValue() + "_CLOCK_FREQUENCY")))

    dbguClockInvalidSym = dbguComponent.createCommentSymbol("DBGU_CLOCK_INVALID_COMMENT", None)
    dbguClockInvalidSym.setLabel("Warning!!! Configured baud rate cannot be acheived using current source clock frequency !!!")
    dbguClockInvalidSym.setVisible(False)

    dbguBaud = dbguComponent.createIntegerSymbol("BAUD_RATE", None)
    dbguBaud.setLabel("Baud Rate")
    dbguBaud.setDefaultValue(115200)

    brgVal = baudRateCalc(dbguClkValue.getValue(), dbguBaud.getValue())

    dbguBRGValue = dbguComponent.createIntegerSymbol("BRG_VALUE", None)
    dbguBRGValue.setVisible(False)
    dbguBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "core." + dbguInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    dbguBRGValue.setDefaultValue(brgVal)

    dbguDataWidth = dbguComponent.createComboSymbol("DBGU_MR_DATA_WIDTH", None, ["8 BIT"])
    dbguDataWidth.setLabel("Data")
    dbguDataWidth.setDefaultValue("8_BIT")
    dbguDataWidth.setReadOnly(True)

    #DBGU Character Size 8 Bit Mask symbol for USART Driver
    dbguDataWidth_8_Mask = dbguComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    dbguDataWidth_8_Mask.setDefaultValue("0x0")
    dbguDataWidth_8_Mask.setVisible(False)

    parityList = []
    for id in range(0, len(dbguValGrp_MR_PAR.getChildren())):
        parityList.append(id+1)
        parityList[id] = dbguValGrp_MR_PAR.getChildren()[id].getAttribute("name")


    dbguSym_MR_PAR = dbguComponent.createComboSymbol("DBGU_MR_PAR", None, parityList)
    dbguSym_MR_PAR.setLabel("Parity")
    dbguSym_MR_PAR.setDefaultValue("NO")

    #DBGU Transmit data register symbol for USART Driver
    transmitRegister = dbguComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+dbguInstanceName.getValue()+"_REGS->DBGU_THR)")
    transmitRegister.setVisible(False)

    #DBGU Receive data register symbol for USART Driver
    receiveRegister = dbguComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+dbguInstanceName.getValue()+"_REGS->DBGU_RHR)")
    receiveRegister.setVisible(False)

    #DBGU EVEN Parity Mask symbol for USART Driver
    dbguSym_MR_PAR_EVEN_Mask = dbguComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    dbguSym_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
    dbguSym_MR_PAR_EVEN_Mask.setVisible(False)

    #DBGU ODD Parity Mask symbol for USART Driver
    dbguSym_MR_PAR_ODD_Mask = dbguComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    dbguSym_MR_PAR_ODD_Mask.setDefaultValue("0x200")
    dbguSym_MR_PAR_ODD_Mask.setVisible(False)

    #DBGU SPACE Parity Mask symbol for USART Driver
    dbguSym_MR_PAR_SPACE_Mask = dbguComponent.createStringSymbol("USART_PARITY_SPACE_MASK", None)
    dbguSym_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
    dbguSym_MR_PAR_SPACE_Mask.setVisible(False)

    #DBGU MARK Parity Mask symbol for USART Driver
    dbguSym_MR_PAR_MARK_Mask = dbguComponent.createStringSymbol("USART_PARITY_MARK_MASK", None)
    dbguSym_MR_PAR_MARK_Mask.setDefaultValue("0x600")
    dbguSym_MR_PAR_MARK_Mask.setVisible(False)

    #DBGU NO Parity Mask symbol for USART Driver
    dbguSym_MR_PAR_NO_Mask = dbguComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    dbguSym_MR_PAR_NO_Mask.setDefaultValue("0x800")
    dbguSym_MR_PAR_NO_Mask.setVisible(False)

    dbguStopBit = dbguComponent.createComboSymbol("DBGU_MR_STOP_BITS", None, ["1 BIT"])
    dbguStopBit.setLabel("Stop")
    dbguStopBit.setDefaultValue("1_BIT")
    dbguStopBit.setReadOnly(True)

    #DBGU Stop 1-bit Mask symbol for USART Driver
    dbguStopBit_1_Mask = dbguComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    dbguStopBit_1_Mask.setDefaultValue("0x0")
    dbguStopBit_1_Mask.setVisible(False)

    dbguSym_MR_FILTER = dbguComponent.createBooleanSymbol("DBGU_MR_FILTER", None)
    dbguSym_MR_FILTER.setLabel(dbguCaption_MR_FILTER)
    dbguSym_MR_FILTER.setDefaultValue(False)

    #DBGU Overrun error Mask symbol for USART Driver
    dbguSym_SR_OVRE_Mask = dbguComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    dbguSym_SR_OVRE_Mask.setDefaultValue("0x20")
    dbguSym_SR_OVRE_Mask.setVisible(False)

    #DBGU parity error Mask symbol for USART Driver
    dbguSym_SR_PARE_Mask = dbguComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    dbguSym_SR_PARE_Mask.setDefaultValue("0x80")
    dbguSym_SR_PARE_Mask.setVisible(False)

    #DBGU framing error Mask symbol for USART Driver
    dbguSym_SR_FRAME_Mask = dbguComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    dbguSym_SR_FRAME_Mask.setDefaultValue("0x40")
    dbguSym_SR_FRAME_Mask.setVisible(False)

    #DBGU API Prefix symbol for USART Driver
    dbguSym_API_Prefix = dbguComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    dbguSym_API_Prefix.setDefaultValue(dbguInstanceName.getValue())
    dbguSym_API_Prefix.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = dbguInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = dbguInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = dbguInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = dbguInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and Interrupt
    Database.setSymbolValue("core", dbguInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.setSymbolValue("core", interruptHandler, dbguInstanceName.getValue() + "_InterruptHandler", 2)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # Interrupt Dynamic settings
    dbguinterruptControl = dbguComponent.createBooleanSymbol("INTERRUPT_DBGU_ENABLE", None)
    dbguinterruptControl.setDependencies(interruptControl, ["USART_INTERRUPT_MODE"])
    dbguinterruptControl.setVisible(False)

    # Dependency Status
    dbguSymClkEnComment = dbguComponent.createCommentSymbol("DBGU_CLK_ENABLE_COMMENT", None)
    dbguSymClkEnComment.setVisible(False)
    dbguSymClkEnComment.setLabel("Warning!!! DBGU Peripheral Clock is Disabled in Clock Manager")
    dbguSymClkEnComment.setDependencies(clockWarningVisible, ["core." + dbguInstanceName.getValue() + "_CLOCK_ENABLE"])

    dbguSymIntEnComment = dbguComponent.createCommentSymbol("DBGU_INTERRUPT_ENABLE_COMMENT", None)
    dbguSymIntEnComment.setVisible(False)
    dbguSymIntEnComment.setLabel("Warning!!! DBGU Interrupt is Disabled in Interrupt Manager")
    dbguSymIntEnComment.setDependencies(dependencyStatus, ["core." + interruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    dbguHeaderFile = dbguComponent.createFileSymbol("DBGU_COMMON_HEADER", None)
    dbguHeaderFile.setSourcePath("../peripheral/dbgu_6059/templates/plib_dbgu_common.h")
    dbguHeaderFile.setOutputName("plib_dbgu_common.h")
    dbguHeaderFile.setDestPath("/peripheral/dbgu/")
    dbguHeaderFile.setProjectPath("config/" + configName + "/peripheral/dbgu/")
    dbguHeaderFile.setType("HEADER")
    dbguHeaderFile.setOverwrite(True)

    dbguHeader1File = dbguComponent.createFileSymbol("DBGU_HEADER", None)
    dbguHeader1File.setSourcePath("../peripheral/dbgu_6059/templates/plib_dbgu.h.ftl")
    dbguHeader1File.setOutputName("plib_"+dbguInstanceName.getValue().lower()+ ".h")
    dbguHeader1File.setDestPath("/peripheral/dbgu/")
    dbguHeader1File.setProjectPath("config/" + configName + "/peripheral/dbgu/")
    dbguHeader1File.setType("HEADER")
    dbguHeader1File.setOverwrite(True)
    dbguHeader1File.setMarkup(True)
    dbguHeader1File.setDependencies(DBGUFileGeneration, ["DBGU_RING_BUFFER_ENABLE"])

    dbguSource1File = dbguComponent.createFileSymbol("DBGU_SOURCE", None)
    dbguSource1File.setSourcePath("../peripheral/dbgu_6059/templates/plib_dbgu.c.ftl")
    dbguSource1File.setOutputName("plib_"+dbguInstanceName.getValue().lower()+ ".c")
    dbguSource1File.setDestPath("/peripheral/dbgu/")
    dbguSource1File.setProjectPath("config/" + configName + "/peripheral/dbgu/")
    dbguSource1File.setType("SOURCE")
    dbguSource1File.setOverwrite(True)
    dbguSource1File.setMarkup(True)
    dbguSource1File.setDependencies(DBGUFileGeneration, ["DBGU_RING_BUFFER_ENABLE"])

    dbguSystemInitFile = dbguComponent.createFileSymbol("DBGU_INIT", None)
    dbguSystemInitFile.setType("STRING")
    dbguSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    dbguSystemInitFile.setSourcePath("../peripheral/dbgu_6059/templates/system/initialization.c.ftl")
    dbguSystemInitFile.setMarkup(True)

    dbguSystemDefFile = dbguComponent.createFileSymbol("DBGU_DEF", None)
    dbguSystemDefFile.setType("STRING")
    dbguSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dbguSystemDefFile.setSourcePath("../peripheral/dbgu_6059/templates/system/definitions.h.ftl")
    dbguSystemDefFile.setMarkup(True)
