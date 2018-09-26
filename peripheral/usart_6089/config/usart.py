################################################################################
#### Register Information ####
################################################################################

usartValGrp_MR_PAR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="USART"]/value-group@[name="US_MR__PAR"]')

################################################################################
#### Global Variables ####
################################################################################
global usartInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################
def interruptControl(usartNVIC, event):
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def dependencyStatus(symbol, event):
    if (Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

# Calculates BRG value
def baudRateCalc(clk, baud, overSamp):
    if (overSamp == 0):
        brgVal = (clk / (16 * baud))
    else :
        brgVal = (clk / (8 * baud))

    return brgVal


def baudRateTrigger(symbol, event):
    global usartInstanceName
    clk = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLOCK_FREQ")
    baud = Database.getSymbolValue(usartInstanceName.getValue().lower(), "BAUD_RATE")
    overSamp = Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_MR_OVER")

    brgVal = baudRateCalc(clk, baud, overSamp)

    if(brgVal < 1):
        Log.writeErrorMessage("USART Clock source value is low for the desired baud rate")

    symbol.clearValue()

    if symbol.getID() == "BRG_VALUE":
        symbol.setValue(brgVal, 2)

def clockSourceFreq(symbol, event):
    if (event["id"] == "USART_CLK_SRC"):
        symbol.clearValue()
        if (event["value"] == 0):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)
        if (event["value"] == 1):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 8, 2)
        if (event["value"] == 2):
            symbol.setValue(int(Database.getSymbolValue("core", "PCK4_CLOCK_FREQUENCY")), 2)
    if (event["id"] == "PCK4_CLOCK_FREQUENCY") and (Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLK_SRC") == 2):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "PCK4_CLOCK_FREQUENCY")), 2)
    if (event["id"] == "MASTER_CLOCK_FREQUENCY") and (Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLK_SRC") == 0):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)
    if (event["id"] == "MASTER_CLOCK_FREQUENCY") and (Database.getSymbolValue(usartInstanceName.getValue().lower(), "USART_CLK_SRC") == 1):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY") / 8), 2)

def dataWidthLogic(symbol, event):
    symbol.clearValue()
    if(event["value"] == 4):
        symbol.setValue(True, 2)
    else:
        symbol.setValue(False, 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(usartComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global usartInstanceName

    usartInstanceName = usartComponent.createStringSymbol("USART_INSTANCE_NAME", None)
    usartInstanceName.setVisible(False)
    usartInstanceName.setDefaultValue(usartComponent.getID().upper())
    Log.writeInfoMessage("Running " + usartInstanceName.getValue())

    usartInterrupt = usartComponent.createBooleanSymbol("USART_INTERRUPT_MODE", None)
    usartInterrupt.setLabel("Interrupt Mode")
    usartInterrupt.setDefaultValue(True)

    usartClkSrc = usartComponent.createKeyValueSetSymbol("USART_CLK_SRC", None)
    usartClkSrc.setLabel("Select Clock Source")
    usartClkSrc.addKey("MCK", "0", "MCK")
    usartClkSrc.addKey("DIV", "1", "MCK/8")
    usartClkSrc.addKey("PCK", "2", "PCK4")
    usartClkSrc.setDisplayMode("Description")
    usartClkSrc.setOutputMode("Key")
    usartClkSrc.setDefaultValue(0)

    usartClkValue = usartComponent.createIntegerSymbol("USART_CLOCK_FREQ", None)
    usartClkValue.setLabel("Clock Source Value")
    usartClkValue.setReadOnly(True)
    usartClkValue.setDependencies(clockSourceFreq, ["USART_CLK_SRC", "core.PCK4_CLOCK_FREQUENCY", "core.MASTER_CLOCK_FREQUENCY"])
    usartClkValue.setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))

    usartBaud = usartComponent.createIntegerSymbol("BAUD_RATE", None)
    usartBaud.setLabel("Baud Rate")
    usartBaud.setDefaultValue(9600)

    usartSym_MR_OVER = usartComponent.createKeyValueSetSymbol("USART_MR_OVER", None)
    usartSym_MR_OVER.setLabel("OverSampling")
    usartSym_MR_OVER.addKey("0", "0", "16 Times")
    usartSym_MR_OVER.addKey("1", "1", "8 Times")
    usartSym_MR_OVER.setDisplayMode("Description")
    usartSym_MR_OVER.setOutputMode("Key")
    usartSym_MR_OVER.setDefaultValue(0)

    brgVal = baudRateCalc(usartClkValue.getValue(), usartBaud.getValue(), usartSym_MR_OVER.getValue())

    usartBRGValue = usartComponent.createIntegerSymbol("BRG_VALUE", None)
    usartBRGValue.setVisible(False)
    usartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "USART_MR_OVER", "USART_CLOCK_FREQ"])
    usartBRGValue.setDefaultValue(brgVal)

    usartSym_MR_CHRL = usartComponent.createKeyValueSetSymbol("USART_MR_CHRL", None)
    usartSym_MR_CHRL.setLabel("Data")
    usartSym_MR_CHRL.addKey("5_BIT", "0", "5 BIT")
    usartSym_MR_CHRL.addKey("6_BIT", "1", "6 BIT")
    usartSym_MR_CHRL.addKey("7_BIT", "2", "7 BIT")
    usartSym_MR_CHRL.addKey("8_BIT", "3", "8 BIT")
    # There is no 9 bit available under MR_CHRL, but added here just for menu.
    # usartSym_MR_MODE9 will use this value
    usartSym_MR_CHRL.addKey("9_BIT", "4", "9 BIT")
    usartSym_MR_CHRL.setDisplayMode("Description")
    usartSym_MR_CHRL.setOutputMode("Key")
    usartSym_MR_CHRL.setDefaultValue(3)

    usartSym_MR_MODE9 = usartComponent.createBooleanSymbol("USART_MR_MODE9", None)
    usartSym_MR_MODE9.setVisible(False)
    usartSym_MR_MODE9.setDependencies(dataWidthLogic, ["USART_MR_CHRL"])
    usartSym_MR_MODE9.setLabel("9 Bit Data Width")
    usartSym_MR_MODE9.setDefaultValue(False)

    #USART Transmit data register
    transmitRegister = usartComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+usartInstanceName.getValue()+"_REGS->US_THR)")
    transmitRegister.setVisible(False)

    #USART Receive data register
    receiveRegister = usartComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+usartInstanceName.getValue()+"_REGS->US_RHR)")
    receiveRegister.setVisible(False)

    #USART Character Size 5 Mask
    usartSym_MR_CHRL_5_Mask = usartComponent.createStringSymbol("USART_DATA_5_BIT_MASK", None)
    usartSym_MR_CHRL_5_Mask.setDefaultValue("0x0")
    usartSym_MR_CHRL_5_Mask.setVisible(False)

    #USART Character Size 6 Mask
    usartSym_MR_CHRL_6_Mask = usartComponent.createStringSymbol("USART_DATA_6_BIT_MASK", None)
    usartSym_MR_CHRL_6_Mask.setDefaultValue("0x40")
    usartSym_MR_CHRL_6_Mask.setVisible(False)

    #USART Character Size 7 Mask
    usartSym_MR_CHRL_7_Mask = usartComponent.createStringSymbol("USART_DATA_7_BIT_MASK", None)
    usartSym_MR_CHRL_7_Mask.setDefaultValue("0x80")
    usartSym_MR_CHRL_7_Mask.setVisible(False)

    #USART Character Size 8 Mask
    usartSym_MR_CHRL_8_Mask = usartComponent.createStringSymbol("USART_DATA_8_BIT_MASK", None)
    usartSym_MR_CHRL_8_Mask.setDefaultValue("0xC0")
    usartSym_MR_CHRL_8_Mask.setVisible(False)

    #USART Character Size 9 Mask
    usartSym_MR_CHRL_9_Mask = usartComponent.createStringSymbol("USART_DATA_9_BIT_MASK", None)
    usartSym_MR_CHRL_9_Mask.setDefaultValue("0x20000")
    usartSym_MR_CHRL_9_Mask.setVisible(False)

    parityList = []
    for id in range(0, len(usartValGrp_MR_PAR.getChildren())):
        parityList.append(id+1)
        parityList[id] = usartValGrp_MR_PAR.getChildren()[id].getAttribute("name")

    usartSym_MR_PAR = usartComponent.createComboSymbol("USART_MR_PAR", None, parityList)
    usartSym_MR_PAR.setLabel("Parity")
    usartSym_MR_PAR.setDefaultValue("NO")

    #USART EVEN Parity Mask
    usartSym_MR_PAR_EVEN_Mask = usartComponent.createStringSymbol("USART_PARITY_EVEN_MASK", None)
    usartSym_MR_PAR_EVEN_Mask.setDefaultValue("0x0")
    usartSym_MR_PAR_EVEN_Mask.setVisible(False)

    #USART ODD Parity Mask
    usartSym_MR_PAR_ODD_Mask = usartComponent.createStringSymbol("USART_PARITY_ODD_MASK", None)
    usartSym_MR_PAR_ODD_Mask.setDefaultValue("0x200")
    usartSym_MR_PAR_ODD_Mask.setVisible(False)

    #USART SPACE Parity Mask
    usartSym_MR_PAR_SPACE_Mask = usartComponent.createStringSymbol("USART_PARITY_SPACE_MASK", None)
    usartSym_MR_PAR_SPACE_Mask.setDefaultValue("0x400")
    usartSym_MR_PAR_SPACE_Mask.setVisible(False)

    #USART MARK Parity Mask
    usartSym_MR_PAR_MARK_Mask = usartComponent.createStringSymbol("USART_PARITY_MARK_MASK", None)
    usartSym_MR_PAR_MARK_Mask.setDefaultValue("0x600")
    usartSym_MR_PAR_MARK_Mask.setVisible(False)

    #USART NO Parity Mask
    usartSym_MR_PAR_NO_Mask = usartComponent.createStringSymbol("USART_PARITY_NONE_MASK", None)
    usartSym_MR_PAR_NO_Mask.setDefaultValue("0x800")
    usartSym_MR_PAR_NO_Mask.setVisible(False)

    #USART MULTIDROP Parity Mask
    usartSym_MR_PAR_MULTIDROP_Mask = usartComponent.createStringSymbol("USART_PARITY_MULTIDROP_MASK", None)
    usartSym_MR_PAR_MULTIDROP_Mask.setDefaultValue("0xC00")
    usartSym_MR_PAR_MULTIDROP_Mask.setVisible(False)

    usartSym_MR_NBSTOP = usartComponent.createKeyValueSetSymbol("USART_MR_NBSTOP", None)
    usartSym_MR_NBSTOP.setLabel("Stop")
    usartSym_MR_NBSTOP.addKey("1_BIT", "0", "1 BIT")
    usartSym_MR_NBSTOP.addKey("1_5_BIT", "2", "1.5 BIT")
    usartSym_MR_NBSTOP.addKey("2_BIT", "1", "2 BIT")
    usartSym_MR_NBSTOP.setDisplayMode("Description")
    usartSym_MR_NBSTOP.setOutputMode("Key")
    usartSym_MR_NBSTOP.setDefaultValue(0)

    #USART Stop 1-bit Mask
    usartSym_MR_NBSTOP_1_Mask = usartComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
    usartSym_MR_NBSTOP_1_Mask.setDefaultValue("0x0")
    usartSym_MR_NBSTOP_1_Mask.setVisible(False)

    #USART Stop 1_5-bit Mask
    usartSym_MR_NBSTOP_1_5_Mask = usartComponent.createStringSymbol("USART_STOP_1_5_BIT_MASK", None)
    usartSym_MR_NBSTOP_1_5_Mask.setDefaultValue("0x1000")
    usartSym_MR_NBSTOP_1_5_Mask.setVisible(False)

    #USART Stop 2-bit Mask
    usartSym_MR_NBSTOP_2_Mask = usartComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
    usartSym_MR_NBSTOP_2_Mask.setDefaultValue("0x2000")
    usartSym_MR_NBSTOP_2_Mask.setVisible(False)

    #USART API Prefix
    usartSym_API_Prefix = usartComponent.createStringSymbol("USART_PLIB_API_PREFIX", None)
    usartSym_API_Prefix.setDefaultValue(usartInstanceName.getValue())
    usartSym_API_Prefix.setVisible(False)

    #USART Overrun error Mask
    usartSym_CSR_OVRE_Mask = usartComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
    usartSym_CSR_OVRE_Mask.setDefaultValue("0x20")
    usartSym_CSR_OVRE_Mask.setVisible(False)

    #USART parity error Mask
    usartSym_CSR_PARE_Mask = usartComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
    usartSym_CSR_PARE_Mask.setDefaultValue("0x80")
    usartSym_CSR_PARE_Mask.setVisible(False)

    #USART framing error Mask
    usartSym_CSR_FRAME_Mask = usartComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
    usartSym_CSR_FRAME_Mask.setDefaultValue("0x40")
    usartSym_CSR_FRAME_Mask.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = usartInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = usartInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = usartInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = usartInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", usartInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", usartInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, usartInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings
    usartinterruptControl = usartComponent.createBooleanSymbol("NVIC_USART_ENABLE", None)
    usartinterruptControl.setDependencies(interruptControl, ["USART_INTERRUPT_MODE"])
    usartinterruptControl.setVisible(False)

    # Dependency Status
    usartSymClkEnComment = usartComponent.createCommentSymbol("USART_CLK_ENABLE_COMMENT", None)
    usartSymClkEnComment.setVisible(False)
    usartSymClkEnComment.setLabel("Warning!!! USART Peripheral Clock is Disabled in Clock Manager")
    usartSymClkEnComment.setDependencies(dependencyStatus, ["core."+usartInstanceName.getValue()+"_CLOCK_ENABLE"])

    usartSymIntEnComment = usartComponent.createCommentSymbol("USART_NVIC_ENABLE_COMMENT", None)
    usartSymIntEnComment.setVisible(False)
    usartSymIntEnComment.setLabel("Warning!!! USART Interrupt is Disabled in Interrupt Manager")
    usartSymIntEnComment.setDependencies(dependencyStatus, ["core." + interruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    usartHeaderFile = usartComponent.createFileSymbol("USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/usart_6089/templates/plib_usart_common.h")
    usartHeaderFile.setOutputName("plib_usart_common.h")
    usartHeaderFile.setDestPath("peripheral/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setOverwrite(True)

    usartHeader1File = usartComponent.createFileSymbol("USART_HEADER1", None)
    usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
    usartHeader1File.setOutputName("plib_"+usartInstanceName.getValue().lower()+".h")
    usartHeader1File.setDestPath("peripheral/usart/")
    usartHeader1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeader1File.setType("HEADER")
    usartHeader1File.setOverwrite(True)
    usartHeader1File.setMarkup(True)

    usartSource1File = usartComponent.createFileSymbol("USART_SOURCE1", None)
    usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
    usartSource1File.setOutputName("plib_"+usartInstanceName.getValue().lower()+".c")
    usartSource1File.setDestPath("peripheral/usart/")
    usartSource1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartSource1File.setType("SOURCE")
    usartSource1File.setOverwrite(True)
    usartSource1File.setMarkup(True)

    usartSystemInitFile = usartComponent.createFileSymbol("USART_INIT", None)
    usartSystemInitFile.setType("STRING")
    usartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    usartSystemInitFile.setSourcePath("../peripheral/usart_6089/templates/system/system_initialize.c.ftl")
    usartSystemInitFile.setMarkup(True)

    usartSystemDefFile = usartComponent.createFileSymbol("USART_DEF", None)
    usartSystemDefFile.setType("STRING")
    usartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    usartSystemDefFile.setSourcePath("../peripheral/usart_6089/templates/system/system_definitions.h.ftl")
    usartSystemDefFile.setMarkup(True)
