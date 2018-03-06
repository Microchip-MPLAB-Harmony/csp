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
    clk = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))
    baud = Database.getSymbolValue("usart" + str(usartInstance), "BAUD_RATE")
    if event["id"] == "BAUD_RATE":
        baud = event["value"]
    if event["id"] == "MASTERCLK_FREQ":
        clk = int(event["value"])

    brgVal, overSamp = baudRateCalc(clk, baud)

    symbol.clearValue()
    if symbol.getID() == "BRG_VALUE":
        symbol.setValue(brgVal, 2)
    if symbol.getID() == "USART_MR_OVER":
        symbol.setValue(overSamp, 2)

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

    usartBaud = usartComponent.createIntegerSymbol("BAUD_RATE", None)
    usartBaud.setLabel("Baud Rate")
    usartBaud.setDefaultValue(9600)

    brgVal, overSamp = baudRateCalc(int(Database.getSymbolValue("core", "MASTERCLK_FREQ")), 9600)

    usartSym_MR_OVER = usartComponent.createIntegerSymbol("USART_MR_OVER", None)
    usartSym_MR_OVER.setVisible(False)
    usartSym_MR_OVER.setDependencies(baudRateTrigger, ["BAUD_RATE", "core.MASTERCLK_FREQ"])
    usartSym_MR_OVER.setDefaultValue(overSamp)

    usartBRGValue = usartComponent.createIntegerSymbol("BRG_VALUE", None)
    usartBRGValue.setVisible(False)
    usartBRGValue.setDependencies(baudRateTrigger, ["BAUD_RATE", "core.MASTERCLK_FREQ"])
    usartBRGValue.setDefaultValue(brgVal)

    usartSym_MR_MODE9 = usartComponent.createBooleanSymbol("USART_MR_MODE9", None)
    usartSym_MR_MODE9.setLabel(usartBitField_MR_MODE9.getDescription())
    usartSym_MR_MODE9.setDefaultValue(False)

    usartSym_MR_PAR = usartComponent.createComboSymbol("USART_MR_PAR", None, usartValGrp_MR_PAR.getValueNames())
    usartSym_MR_PAR.setLabel(usartBitField_MR_PAR.getDescription())
    usartSym_MR_PAR.setDefaultValue("NO")

    usartSym_MR_NBSTOP = usartComponent.createComboSymbol("USART_MR_NBSTOP", None, usartValGrp_MR_NBSTOP.getValueNames())
    usartSym_MR_NBSTOP.setLabel(usartBitField_MR_NBSTOP.getDescription())
    usartSym_MR_NBSTOP.setDefaultValue("_1_BIT")

    # Here for the future use, by default only 8 and 9 bit available for now.
    usartSym_MR_CHRL = usartComponent.createComboSymbol("USART_MR_CHRL", None, usartValGrp_MR_CHRL.getValueNames())
    usartSym_MR_CHRL.setVisible(False)
    usartSym_MR_CHRL.setLabel(usartBitField_MR_CHRL.getDescription())
    usartSym_MR_CHRL.setDefaultValue("_8_BIT")

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

    usartHeaderFile = usartComponent.createFileSymbol(None, None)
    usartHeaderFile.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h")
    usartHeaderFile.setOutputName("plib_usart.h")
    usartHeaderFile.setDestPath("peripheral/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setOverwrite(True)

    usartHeader1File = usartComponent.createFileSymbol(None, None)
    usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
    usartHeader1File.setOutputName("plib_usart" + str(usartInstance) + ".h")
    usartHeader1File.setDestPath("peripheral/usart/")
    usartHeader1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartHeader1File.setType("HEADER")
    usartHeader1File.setOverwrite(True)
    usartHeader1File.setMarkup(True)

    usartSource1File = usartComponent.createFileSymbol(None, None)
    usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
    usartSource1File.setOutputName("plib_usart" + str(usartInstance) + ".c")
    usartSource1File.setDestPath("peripheral/usart/")
    usartSource1File.setProjectPath("config/" + configName + "/peripheral/usart/")
    usartSource1File.setType("SOURCE")
    usartSource1File.setOverwrite(True)
    usartSource1File.setMarkup(True)

    usartSystemInitFile = usartComponent.createFileSymbol(None, None)
    usartSystemInitFile.setType("STRING")
    usartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    usartSystemInitFile.setSourcePath("../peripheral/usart_6089/templates/system/system_initialize.c.ftl")
    usartSystemInitFile.setMarkup(True)

    usartSystemDefFile = usartComponent.createFileSymbol(None, None)
    usartSystemDefFile.setType("STRING")
    usartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    usartSystemDefFile.setSourcePath("../peripheral/usart_6089/templates/system/system_definitions.h.ftl")
    usartSystemDefFile.setMarkup(True)
