################################################################################
#### Register Information ####
################################################################################
uartRegModule = Register.getRegisterModule("UART")
uartRegGroup = uartRegModule.getRegisterGroup("UART")

uartReg_MR = uartRegGroup.getRegister("UART_MR")
uartBitField_MR_PAR = uartReg_MR.getBitfield("PAR")
uartValGrp_MR_PAR = uartRegModule.getValueGroup(uartBitField_MR_PAR.getValueGroupName())
uartBitField_MR_FILTER = uartReg_MR.getBitfield("FILTER")

################################################################################
#### Global Variables ####
################################################################################
global uartInstance
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################
def interruptControl(uartNVIC, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, "UART" + str(uartInstance) + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "UART" + str(uartInstance) + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyStatus(symbol, event):
    if (Database.getSymbolValue("uart" + str(uartInstance), "USART_INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])


# Calculates BRG value
def baudRateCalc(clk, baud):
    if (clk >= (16 * baud)):
        brgVal = (clk / (16 * baud))
    else :
        brgVal = (clk / (8 * baud))

    return brgVal


def baudRateTrigger(symbol, event):
    global uartInstance
    clk = Database.getSymbolValue("core", "UART"+str(uartInstance)+"_CLOCK_FREQUENCY")
    baud = Database.getSymbolValue("uart" + str(uartInstance), "BAUD_RATE")
    brgVal = baudRateCalc(clk, baud)
    if(brgVal < 1):
        Log.writeErrorMessage("UART Clock source value is low for the desired baud rate")
    symbol.clearValue()
    symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):
    symbol.clearValue()
    symbol.setValue(int(Database.getSymbolValue("core", "UART"+str(uartInstance)+"_CLOCK_FREQUENCY")), 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(uartComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global uartInstance

    uartInstance = uartComponent.getID()[-1:]
    Log.writeInfoMessage("Running UART" + str(uartInstance))

    uartIndex = uartComponent.createIntegerSymbol("INDEX", None)
    uartIndex.setVisible(False)
    uartIndex.setDefaultValue(int(uartInstance))

    uartInterrupt = uartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    uartInterrupt.setLabel("Interrupt Mode")
    uartInterrupt.setDefaultValue(True)

    uartClkSrc = uartComponent.createKeyValueSetSymbol("UART_CLK_SRC", None)
    uartClkSrc.setLabel("Select Clock Source")
    childrenNodes = []
    uart = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"UART\"]/value-group@[name=\"UART_MR__BRSRCCK\"]")
    childrenNodes = uart.getChildren()
    for param in range(0, len(childrenNodes)):
        uartClkSrc.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))
    uartClkSrc.setDisplayMode("Description")
    uartClkSrc.setOutputMode("Key")
    uartClkSrc.setDefaultValue(0)

    uartClkValue = uartComponent.createIntegerSymbol("UART_CLOCK_FREQ", None)
    uartClkValue.setLabel("Clock Source Value")
    uartClkValue.setReadOnly(True)
    uartClkValue.setDependencies(clockSourceFreq, ["UART_CLK_SRC", "core.UART"+str(uartInstance)+"_CLOCK_FREQUENCY"])
    uartClkValue.setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))

    uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", None)
    uartBaud.setLabel("Baud Rate")
    uartBaud.setDefaultValue(9600)

    brgVal = baudRateCalc(uartClkValue.getValue(), uartBaud.getValue())

    uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", None)
    uartBRGValue.setVisible(False)
    uartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "core.UART"+str(uartInstance)+"_CLOCK_FREQUENCY"])
    uartBRGValue.setDefaultValue(brgVal)

    uartDataWidth = uartComponent.createComboSymbol("UART_MR_DATA_WIDTH", None, ["8 BIT"])
    uartDataWidth.setLabel("Data")
    uartDataWidth.setDefaultValue("8_BIT")
    uartDataWidth.setReadOnly(True)

    #UART Character Size 8 Mask
    uartDataWidth_8_Mask = uartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    uartDataWidth_8_Mask.setDefaultValue("0x0")
    uartDataWidth_8_Mask.setVisible(False)

    uartSym_MR_PAR = uartComponent.createComboSymbol("UART_MR_PAR", None, uartValGrp_MR_PAR.getValueNames())
    uartSym_MR_PAR.setLabel("Parity")
    uartSym_MR_PAR.setDefaultValue("NO")

    #UART Transmit data register
    transmitRegister = uartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&(UART"+str(uartInstance)+"_REGS->UART_THR)")
    transmitRegister.setVisible(False)

    #UART Receive data register
    receiveRegister = uartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&(UART"+str(uartInstance)+"_REGS->UART_RHR)")
    receiveRegister.setVisible(False)

    #UART EVEN Parity Mask
    uartSym_MR_PAR_EVEN_Mask = uartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    uartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
    uartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #UART ODD Parity Mask
    uartSym_MR_PAR_ODD_Mask = uartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    uartSym_MR_PAR_ODD_Mask.setDefaultValue("0x200")
    uartSym_MR_PAR_ODD_Mask.setVisible(False)

    #UART SPACE Parity Mask
    uartSym_MR_PAR_SPACE_Mask = uartComponent.createStringSymbol("USART_PARITY_SPACE_MASK", None)
    uartSym_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
    uartSym_MR_PAR_SPACE_Mask.setVisible(False)

    #UART MARK Parity Mask
    uartSym_MR_PAR_MARK_Mask = uartComponent.createStringSymbol("USART_PARITY_MARK_MASK", None)
    uartSym_MR_PAR_MARK_Mask.setDefaultValue("0x600")
    uartSym_MR_PAR_MARK_Mask.setVisible(False)

    #UART NO Parity Mask
    uartSym_MR_PAR_NO_Mask = uartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    uartSym_MR_PAR_NO_Mask.setDefaultValue("0x800")
    uartSym_MR_PAR_NO_Mask.setVisible(False)

    uartStopBit = uartComponent.createComboSymbol("UART_MR_STOP_BITS", None, ["1 BIT"])
    uartStopBit.setLabel("Stop")
    uartStopBit.setDefaultValue("1_BIT")
    uartStopBit.setReadOnly(True)

    #UART Stop 1-bit Mask
    uartStopBit_1_Mask = uartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    uartStopBit_1_Mask.setDefaultValue("0x0")
    uartStopBit_1_Mask.setVisible(False)

    uartSym_MR_FILTER = uartComponent.createBooleanSymbol("UART_MR_FILTER", None)
    uartSym_MR_FILTER.setLabel(uartBitField_MR_FILTER.getDescription())
    uartSym_MR_FILTER.setDefaultValue(False)

    #UART API Prefix
    uartSym_API_Prefix = uartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    uartSym_API_Prefix.setDefaultValue("UART" + str(uartInstance))
    uartSym_API_Prefix.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = "UART" + str(uartInstance) + "_INTERRUPT_ENABLE"
    interruptHandler = "UART" + str(uartInstance) + "_INTERRUPT_HANDLER"
    interruptHandlerLock = "UART" + str(uartInstance) + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = "UART" + str(uartInstance) + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", "UART"+ str(uartInstance)+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", "UART"+ str(uartInstance)+"_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, "UART" + str(uartInstance) + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings
    uartinterruptControl = uartComponent.createBooleanSymbol("NVIC_UART_ENABLE", None)
    uartinterruptControl.setDependencies(interruptControl, ["USART_INTERRUPT_MODE"])
    uartinterruptControl.setVisible(False)

    # Dependency Status
    uartSymClkEnComment = uartComponent.createCommentSymbol("UART_CLK_ENABLE_COMMENT", None)
    uartSymClkEnComment.setVisible(False)
    uartSymClkEnComment.setLabel("Warning!!! UART Peripheral Clock is Disabled in Clock Manager")
    uartSymClkEnComment.setDependencies(dependencyStatus, ["core.UART"+ str(uartInstance)+"_CLOCK_ENABLE"])

    uartSymIntEnComment = uartComponent.createCommentSymbol("UART_NVIC_ENABLE_COMMENT", None)
    uartSymIntEnComment.setVisible(False)
    uartSymIntEnComment.setLabel("Warning!!! UART Interrupt is Disabled in Interrupt Manager")
    uartSymIntEnComment.setDependencies(dependencyStatus, ["core." + interruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    uartHeaderFile = uartComponent.createFileSymbol("UART_HEADER", None)
    uartHeaderFile.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h")
    uartHeaderFile.setOutputName("plib_uart.h")
    uartHeaderFile.setDestPath("peripheral/uart/")
    uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeaderFile.setType("HEADER")
    uartHeaderFile.setOverwrite(True)

    uartHeader1File = uartComponent.createFileSymbol("UART_HEADER1", None)
    uartHeader1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h.ftl")
    uartHeader1File.setOutputName("plib_uart" + str(uartInstance) + ".h")
    uartHeader1File.setDestPath("peripheral/uart/")
    uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartHeader1File.setType("HEADER")
    uartHeader1File.setOverwrite(True)
    uartHeader1File.setMarkup(True)

    uartSource1File = uartComponent.createFileSymbol("UART_SOURCE1", None)
    uartSource1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.c.ftl")
    uartSource1File.setOutputName("plib_uart" + str(uartInstance) + ".c")
    uartSource1File.setDestPath("peripheral/uart/")
    uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
    uartSource1File.setType("SOURCE")
    uartSource1File.setOverwrite(True)
    uartSource1File.setMarkup(True)

    uartSystemInitFile = uartComponent.createFileSymbol("UART_INIT", None)
    uartSystemInitFile.setType("STRING")
    uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    uartSystemInitFile.setSourcePath("../peripheral/uart_6418/templates/system/system_initialize.c.ftl")
    uartSystemInitFile.setMarkup(True)

    uartSystemDefFile = uartComponent.createFileSymbol("UART_DEF", None)
    uartSystemDefFile.setType("STRING")
    uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    uartSystemDefFile.setSourcePath("../peripheral/uart_6418/templates/system/system_definitions.h.ftl")
    uartSystemDefFile.setMarkup(True)
