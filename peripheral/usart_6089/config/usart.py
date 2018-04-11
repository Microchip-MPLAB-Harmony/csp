################################################################################
#### Register Information ####
################################################################################
usartRegModule = Register.getRegisterModule("USART")
usartRegGroup = usartRegModule.getRegisterGroup("USART")

usartReg_MR = usartRegGroup.getRegister("US_MR")
usartBitField_MR_PAR = usartReg_MR.getBitfield("PAR")
usartValGrp_MR_PAR = usartRegModule.getValueGroup(usartBitField_MR_PAR.getValueGroupName())
usartBitField_MR_MODE9 = usartReg_MR.getBitfield("MODE9")
usartValGrp_MR_MODE9 = usartRegModule.getValueGroup(usartBitField_MR_MODE9.getValueGroupName())
usartBitField_MR_NBSTOP = usartReg_MR.getBitfield("NBSTOP")
usartValGrp_MR_NBSTOP = usartRegModule.getValueGroup(usartBitField_MR_NBSTOP.getValueGroupName())
usartBitField_MR_CHRL = usartReg_MR.getBitfield("CHRL")
usartValGrp_MR_CHRL = usartRegModule.getValueGroup(usartBitField_MR_CHRL.getValueGroupName())
usartBitField_MR_SYNC = usartReg_MR.getBitfield("SYNC")
usartValGrp_MR_SYNC = usartRegModule.getValueGroup(usartBitField_MR_NBSTOP.getValueGroupName())

################################################################################
#### Global Variables ####
################################################################################
global usartInstance
global peripId
global NVICVector
global NVICHandler

################################################################################
#### Business Logic ####
################################################################################
def NVICControl(usartNVIC, event):
    Database.clearSymbolValue("core", NVICVector)
    Database.clearSymbolValue("core", NVICHandler)
    if (event["value"] == True):
        Database.setSymbolValue("core", NVICVector, True, 2)
        Database.setSymbolValue("core", NVICHandler, "USART" + str(usartInstance) + "_InterruptHandler", 2)
    else :
        Database.setSymbolValue("core", NVICVector, False, 2)
        Database.setSymbolValue("core", NVICHandler, "USART" + str(usartInstance) + "_Handler", 2)

def dependencyStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

# Calculates BRG value and Oversampling
def baudRateCalc(clk, baud):
    if (clk >= (16 * baud)):
        brgVal = (clk / (16 * baud))
        overSamp = 0
    else :
        brgVal = (clk / (8 * baud))
        overSamp = 1

    return [brgVal, overSamp]


def baudRateTrigger(symbol, event):
    global usartInstance
    clk = Database.getSymbolValue("usart" + str(usartInstance), "USART_CLOCK_FREQ")
    baud = Database.getSymbolValue("usart" + str(usartInstance), "BAUD_RATE")
    if event["id"] == "BAUD_RATE":
        baud = event["value"]
    if event["id"] == "USART_CLOCK_FREQ":
        clk = int(event["value"])

    brgVal, overSamp = baudRateCalc(clk, baud)

    if(brgVal < 1):
        Log.writeErrorMessage("USART Clock source value is low for the desired baud rate")

    symbol.clearValue()
    if symbol.getID() == "BRG_VALUE":
        symbol.setValue(brgVal, 2)
    if symbol.getID() == "USART_MR_OVER":
        symbol.setValue(overSamp, 2)

def clockSourceFreq(symbol, event):
    if (event["id"] == "USART_CLK_SRC"):
        symbol.clearValue()
        if (event["value"] == 0):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTERCLK_FREQ")), 2)
        if (event["value"] == 1):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTERCLK_FREQ")) / 8, 2)
        if (event["value"] == 2):
            symbol.setValue(int(Database.getSymbolValue("core", "PCK4_FREQ")), 2)
    if (event["id"] == "PCK4_FREQ") and (Database.getSymbolValue("usart" + str(usartInstance), "USART_CLK_SRC") == 2):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "PCK4_FREQ")), 2)
    if (event["id"] == "MASTERCLK_FREQ") and (Database.getSymbolValue("usart" + str(usartInstance), "USART_CLK_SRC") == 0):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "MASTERCLK_FREQ")), 2)
    if (event["id"] == "MASTERCLK_FREQ") and (Database.getSymbolValue("usart" + str(usartInstance), "USART_CLK_SRC") == 1):
        symbol.clearValue()
        symbol.setValue(int(Database.getSymbolValue("core", "MASTERCLK_FREQ") / 8), 2)

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
    global NVICVector
    global NVICHandler
    global usartInstance
    global peripId

    usartInstance = usartComponent.getID()[-1:]
    Log.writeInfoMessage("Running USART" + str(usartInstance))

    usartIndex = usartComponent.createIntegerSymbol("INDEX", None)
    usartIndex.setVisible(False)
    usartIndex.setDefaultValue(int(usartInstance))

    usartInterrupt = usartComponent.createBooleanSymbol("INTERRUPT_MODE", None)
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
    usartClkValue.setDependencies(clockSourceFreq, ["USART_CLK_SRC", "core.PCK4_FREQ", "core.MASTERCLK_FREQ"])
    usartClkValue.setDefaultValue(int(Database.getSymbolValue("core", "MASTERCLK_FREQ")))

    usartBaud = usartComponent.createIntegerSymbol("BAUD_RATE", None)
    usartBaud.setLabel("Baud Rate")
    usartBaud.setDefaultValue(9600)

    brgVal, overSamp = baudRateCalc(usartClkValue.getValue(), usartBaud.getValue())

    usartSym_MR_OVER = usartComponent.createIntegerSymbol("USART_MR_OVER", None)
    usartSym_MR_OVER.setVisible(False)
    usartSym_MR_OVER.setDependencies(baudRateTrigger, ["BAUD_RATE", "USART_CLOCK_FREQ"])
    usartSym_MR_OVER.setDefaultValue(overSamp)

    usartBRGValue = usartComponent.createIntegerSymbol("BRG_VALUE", None)
    usartBRGValue.setVisible(False)
    usartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "USART_CLOCK_FREQ"])
    usartBRGValue.setDefaultValue(brgVal)

    usartSym_MR_CHRL = usartComponent.createKeyValueSetSymbol("USART_MR_CHRL", None)
    usartSym_MR_CHRL.setLabel("Data")
    usartSym_MR_CHRL.addKey("5_BIT", "0", "5 BIT")
    usartSym_MR_CHRL.addKey("6_BIT", "1", "6 BIT")
    usartSym_MR_CHRL.addKey("7_BIT", "2", "7 BIT")
    usartSym_MR_CHRL.addKey("8_BIT", "3", "8 BIT")
    # There is no 9 bit available under MR_CHRL, but added here just for menu.
    # usartSym_MR_MODE9 will use this value
    usartSym_MR_CHRL.addKey("8_BIT", "4", "9 BIT")
    usartSym_MR_CHRL.setDisplayMode("Description")
    usartSym_MR_CHRL.setOutputMode("Key")
    usartSym_MR_CHRL.setDefaultValue(3)

    usartSym_MR_MODE9 = usartComponent.createBooleanSymbol("USART_MR_MODE9", None)
    usartSym_MR_MODE9.setVisible(False)
    usartSym_MR_MODE9.setDependencies(dataWidthLogic, ["USART_MR_CHRL"])
    usartSym_MR_MODE9.setLabel("9 Bit Data Width")
    usartSym_MR_MODE9.setDefaultValue(False)

    usartSym_MR_PAR = usartComponent.createComboSymbol("USART_MR_PAR", None, usartValGrp_MR_PAR.getValueNames())
    usartSym_MR_PAR.setLabel("Parity")
    usartSym_MR_PAR.setDefaultValue("NO")

    usartSym_MR_NBSTOP = usartComponent.createKeyValueSetSymbol("USART_MR_NBSTOP", None)
    usartSym_MR_NBSTOP.setLabel("Stop")
    usartSym_MR_NBSTOP.addKey("1_BIT", "0", "1 BIT")
    usartSym_MR_NBSTOP.addKey("1_5_BIT", "2", "1.5 BIT")
    usartSym_MR_NBSTOP.addKey("2_BIT", "1", "2 BIT")
    usartSym_MR_NBSTOP.setDisplayMode("Description")
    usartSym_MR_NBSTOP.setOutputMode("Key")
    usartSym_MR_NBSTOP.setDefaultValue(0)

    usartSym_MR_SYNC = usartComponent.createBooleanSymbol("USART_MR_SYNC", None)
    usartSym_MR_SYNC.setLabel(usartBitField_MR_SYNC.getDescription())
    usartSym_MR_SYNC.setDefaultValue(False)

    ############################################################################
    #### Dependency ####
    ############################################################################
    peripId = Interrupt.getInterruptIndex("USART" + str(usartInstance))
    NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", "PMC_ID_USART" + str(usartInstance))
    Database.setSymbolValue("core", "PMC_ID_USART" + str(usartInstance), True, 2)
    Database.clearSymbolValue("core", NVICVector)
    Database.setSymbolValue("core", NVICVector, True, 2)
    Database.clearSymbolValue("core", NVICHandler)
    Database.setSymbolValue("core", NVICHandler, "USART" + str(usartInstance) + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", NVICHandlerLock)
    Database.setSymbolValue("core", NVICHandlerLock, True, 2)

    # NVIC Dynamic settings
    usartNVICControl = usartComponent.createBooleanSymbol("NVIC_USART_ENABLE", None)
    usartNVICControl.setDependencies(NVICControl, ["INTERRUPT_MODE"])
    usartNVICControl.setVisible(False)

    # Dependency Status
    usartSymClkEnComment = usartComponent.createCommentSymbol("USART_CLK_ENABLE_COMMENT", None)
    usartSymClkEnComment.setVisible(False)
    usartSymClkEnComment.setLabel("Warning!!! USART Peripheral Clock is Disabled in Clock Manager")
    usartSymClkEnComment.setDependencies(dependencyStatus, ["core.PMC_ID_USART" + str(usartInstance)])

    usartSymIntEnComment = usartComponent.createCommentSymbol("USART_NVIC_ENABLE_COMMENT", None)
    usartSymIntEnComment.setVisible(False)
    usartSymIntEnComment.setLabel("Warning!!! USART Interrupt is Disabled in Interrupt Manager")
    usartSymIntEnComment.setDependencies(dependencyStatus, ["core." + NVICVector])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    usartHeaderFile = usartComponent.createFileSymbol("USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h")
    usartHeaderFile.setOutputName("plib_usart.h")
    usartHeaderFile.setDestPath("peripheral/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setOverwrite(True)

    usartHeader1File = usartComponent.createFileSymbol("USART_HEADER1", None)
    usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
    usartHeader1File.setOutputName("plib_usart" + str(usartInstance) + ".h")
    usartHeader1File.setDestPath("peripheral/usart/")
    usartHeader1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeader1File.setType("HEADER")
    usartHeader1File.setOverwrite(True)
    usartHeader1File.setMarkup(True)

    usartSource1File = usartComponent.createFileSymbol("USART_SOURCE1", None)
    usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
    usartSource1File.setOutputName("plib_usart" + str(usartInstance) + ".c")
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
