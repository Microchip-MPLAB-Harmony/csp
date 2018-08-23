# Dependency Function to show or hide the warning message depending on Clock enable/disable status
def ClockStatusWarning(symbol, event):
    if event["value"] == False:
       symbol.setVisible(True)
    else:
       symbol.setVisible(False)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):
    global spiInterrupt
    if event["value"] == False and spiInterrupt.getValue() == True:
       symbol.setVisible(True)
    else:
       symbol.setVisible(False)

def ClockModeInfo(symbol, event):
    CPHA = Database.getSymbolValue("spi" + str(spiInstance), "SPI_CLOCK_PHASE")
    CPOL = Database.getSymbolValue("spi" + str(spiInstance), "SPI_CLOCK_POLARITY")
    if (CPOL == 0) and (CPHA == 0):
        symbol.setLabel("                                     ***SPI Mode 0 is Selected***")
    elif (CPOL == 0) and (CPHA == 1):
        symbol.setLabel("                                     ***SPI Mode 1 is Selected***")
    elif (CPOL == 1) and (CPHA == 0):
        symbol.setLabel("                                     ***SPI Mode 2 is Selected***")
    else:
        symbol.setLabel("                                     ***SPI Mode 3 is Selected***")


def setupSpiIntSymbolAndIntHandler(spiInterrupt, event):
    global spiSymNVICVector
    global spiSymNVICHandler
    global spiSymNVICHandlerLock
    global spiSymIntEnComment
    global spiSym_MR_PCS
    global spiDriverControlled
    global spiInterruptDriverModeComment

    if(event["id"] == "SPI_INTERRUPT_MODE"):
        Database.clearSymbolValue("core", spiSymNVICVector)
        Database.clearSymbolValue("core", spiSymNVICHandler)
        Database.clearSymbolValue("core", spiSymNVICHandlerLock)
        if (event["value"] == True):
            Database.setSymbolValue("core", spiSymNVICVector, True, 1)
            Database.setSymbolValue("core", spiSymNVICHandler, "SPI" + str(spiInstance) + "_InterruptHandler", 1)
            Database.setSymbolValue("core", spiSymNVICHandlerLock, True, 1)
        else:
            Database.setSymbolValue("core", spiSymNVICVector, False, 1)
            Database.setSymbolValue("core", spiSymNVICHandler, "SPI" + str(spiInstance) + "_Handler", 1)
            Database.setSymbolValue("core", spiSymNVICHandlerLock, False, 1)

    # control warning message
    if (spiInterrupt.getValue() == True and Database.getSymbolValue("core", spiSymNVICVector) == False):
        spiSymIntEnComment.setVisible(True)
    else:
        spiSymIntEnComment.setVisible(False)

    #control driver dependency
    if(spiInterrupt.getValue() == False and spiDriverControlled.getValue() == True):
        spiInterruptDriverModeComment.setVisible(True)
        spiSym_MR_PCS.setSelectedKey("GPIO",1)
    elif(spiInterrupt.getValue() == True and spiDriverControlled.getValue() == True):
        spiInterruptDriverModeComment.setVisible(False)
        spiInterrupt.setReadOnly(True)
        spiSym_MR_PCS.setSelectedKey("GPIO",1)
    else:
        spiInterruptDriverModeComment.setVisible(False)
        spiInterrupt.setReadOnly(False)

def getMasterClockFreq():
    clkSymMasterClockFreq = Database.getSymbolValue("core","MASTERCLK_FREQ")
    return int(clkSymMasterClockFreq)

def showMasterDependencies(spiSym_MR_Dependencies, event):
    if event["symbol"].getKey(event["value"]) == "MASTER":
        spiSym_MR_Dependencies.setVisible(True)
    else:
        spiSym_MR_Dependencies.setVisible(False)

def SCBR_ValueUpdate(spiSym_CSR_SCBR_VALUE, event):

    if event["id"] == "MASTERCLK_FREQ":
        clk = int(event["value"])
        baud = Database.getSymbolValue("spi" + str(spiInstance), "SPI_BAUD_RATE")
    else:
        #This means there is change in baud rate provided by user in GUI
        baud = event["value"]
        clk = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))

    SCBR = clk/baud
    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255
    spiSym_CSR_SCBR_VALUE.setValue(SCBR, 1)

def calculateCSRIndex(spiSymCSRIndex, event):
    spiSymCSRIndex.setValue(int(event["symbol"].getKeyValue(event["value"])[-1]), 1)

def DummyData_ValueUpdate(spiSymDummyData, event):
    if event["symbol"].getKey(event["value"]) == "_8_BIT":
        spiSymDummyData.setValue(0xFF, 1)
    elif event["symbol"].getKey(event["value"]) == "_9_BIT":
        spiSymDummyData.setValue(0x1FF, 1)
    elif event["symbol"].getKey(event["value"]) == "_10_BIT":
        spiSymDummyData.setValue(0x3FF, 1)
    elif event["symbol"].getKey(event["value"]) == "_11_BIT":
        spiSymDummyData.setValue(0x7FF, 1)
    elif event["symbol"].getKey(event["value"]) == "_12_BIT":
        spiSymDummyData.setValue(0xFFF, 1)
    elif event["symbol"].getKey(event["value"]) == "_13_BIT":
        spiSymDummyData.setValue(0x1FFF, 1)
    elif event["symbol"].getKey(event["value"]) == "_14_BIT":
        spiSymDummyData.setValue(0x3FFF, 1)
    elif event["symbol"].getKey(event["value"]) == "_15_BIT":
        spiSymDummyData.setValue(0x7FFF, 1)
    elif event["symbol"].getKey(event["value"]) == "_16_BIT":
        spiSymDummyData.setValue(0xFFFF, 1)

spiBitField_MR_MSTR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_MR"]/bitfield@[name="MSTR"]')
spiValGrp_MR_MSTR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_MR__MSTR"]')

spiBitField_MR_PCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_MR"]/bitfield@[name="PCS"]')
spiValGrp_MR_PCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_MR__PCS"]')

spiBitField_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="BITS"]')
spiValGrp_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__BITS"]')

spiBitField_CSR_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="CPOL"]')
spiValGrp_CSR_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__CPOL"]')

spiBitField_CSR_NCPHA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="NCPHA"]')
spiValGrp_CSR_NCPHA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__NCPHA"]')

def instantiateComponent(spiComponent):
    global spiInstance
    global spiSymNVICVector
    global spiSymNVICHandler
    global spiSymNVICHandlerLock
    global InternalNVICVectorChange

    InternalNVICVectorChange = False

    spiInstance = spiComponent.getID()[-1:]

    peripId = Interrupt.getInterruptIndex("SPI" + str(spiInstance))
    #IDs used in NVIC Manager
    spiSymNVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    spiSymNVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    spiSymNVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

    # Enable clock for SPI
    Database.setSymbolValue("core", "PMC_ID_SPI" + str(spiInstance), True, 1)

    spiIndex = spiComponent.createIntegerSymbol("SPI_INDEX", None)
    spiIndex.setVisible(False)
    spiIndex.setDefaultValue(int(spiInstance))

    global spiDriverControlled
    spiDriverControlled = spiComponent.createBooleanSymbol("SPI_DRIVER_CONTROLLED", None)
    spiDriverControlled.setVisible(False)
    spiDriverControlled.setDefaultValue(False)

    global spiInterrupt
    spiInterrupt = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiInterrupt.setLabel("Interrupt Mode")
    spiInterrupt.setDefaultValue(True)
    #By Default interrupt mode is enabled and corresponding information is passed to NVIC manager
    Database.setSymbolValue("core", spiSymNVICVector, True, 1)
    Database.setSymbolValue("core", spiSymNVICHandler, "SPI" + str(spiInstance) + "_InterruptHandler", 1)
    Database.setSymbolValue("core", spiSymNVICHandlerLock, True, 1)
    spiInterrupt.setDependencies(setupSpiIntSymbolAndIntHandler, ["SPI_INTERRUPT_MODE", "SPI_DRIVER_CONTROLLED"])

    spiSym_MR_MSTR = spiComponent.createKeyValueSetSymbol("SPI_MR_MSTR", None)
    spiSym_MR_MSTR.setLabel(spiBitField_MR_MSTR.getAttribute("caption"))
    spiSym_MR_MSTR.setOutputMode("Key")
    spiSym_MR_MSTR.setDisplayMode("Description")
    spiSym_MR_MSTR.setDefaultValue(0)
    spiSym_MR_MSTR.setReadOnly(True)

    for id in range(0, len(spiValGrp_MR_MSTR.getChildren())):
        valueName = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("name")
        value = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("value")
        description = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("caption")
        spiSym_MR_MSTR.addKey(valueName, value, description)

    DefaultPCS = 0
    global spiSym_MR_PCS
    spiSym_MR_PCS = spiComponent.createKeyValueSetSymbol("SPI_MR_PCS", None)
    spiSym_MR_PCS.setLabel(spiBitField_MR_PCS.getAttribute("caption"))
    spiSym_MR_PCS.setOutputMode("Value")
    spiSym_MR_PCS.setDisplayMode("Key")
    spiSym_MR_PCS.setDefaultValue(DefaultPCS)
    spiSym_MR_PCS.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    spiSym_MR_PCS.addKey("NPCS0", "NPCS0", "NPCS0 as Chip Select")
    spiSym_MR_PCS.addKey("NPCS1", "NPCS1", "NPCS1 as Chip Select")
    spiSym_MR_PCS.addKey("NPCS2", "NPCS2", "NPCS2 as Chip Select")
    spiSym_MR_PCS.addKey("NPCS3", "NPCS3", "NPCS3 as Chip Select")
    # When User wants to control his chip select himself (through some GPIO pin),
    # then all the NPCSx lines are free to be used as PIO pins. But in MR_PCS
    # field, one of the NPCS lines still has to be selected in order to decide
    # which SPI_CSRx register will be active. Here we have used NPCS0 selection
    # for such case, it can be changed to any other NPCSx line without affecting
    # the user.
    spiSym_MR_PCS.addKey("GPIO", "NPCS0", "User Controlled Chip Select Through GPIO Pin")

    defaultIndex = int(spiSym_MR_PCS.getKey(DefaultPCS)[-1])
    # internal symbol, used to pass CSR register index to SPI FTL
    spiSymCSRIndex = spiComponent.createIntegerSymbol("SPI_CSR_INDEX", None)
    spiSymCSRIndex.setDefaultValue(defaultIndex)
    spiSymCSRIndex.setVisible(False)
    spiSymCSRIndex.setDependencies(calculateCSRIndex, ["SPI_MR_PCS"])

    defaultbaudRate = 1000000
    defaultSCBR = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))/defaultbaudRate

    # Used to pass master clock frequency to SPI FTL
    spiSymMasterClock = spiComponent.createIntegerSymbol("SPI_MASTER_CLOCK", None)
    spiSymMasterClock.setDefaultValue(getMasterClockFreq())
    spiSymMasterClock.setVisible(False)

    spiSym_CSR_SCBR = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", None)
    spiSym_CSR_SCBR.setLabel("Baud Rate in Hz")
    spiSym_CSR_SCBR.setDefaultValue(defaultbaudRate)
    spiSym_CSR_SCBR.setVisible(True)
    spiSym_CSR_SCBR.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    #local variable for code generation
    spiSym_CSR_SCBR_VALUE = spiComponent.createIntegerSymbol("SPI_CSR_SCBR_VALUE", None)
    spiSym_CSR_SCBR_VALUE.setDefaultValue(defaultSCBR)
    spiSym_CSR_SCBR_VALUE.setVisible(False)
    spiSym_CSR_SCBR_VALUE.setDependencies(SCBR_ValueUpdate, ["SPI_BAUD_RATE", "core.MASTERCLK_FREQ"])

    spiSym_CSR_BITS = spiComponent.createKeyValueSetSymbol("SPI_CHARSIZE_BITS", None)
    spiSym_CSR_BITS.setLabel(spiBitField_CSR_BITS.getAttribute("caption"))
    spiSym_CSR_BITS.setOutputMode("Key")
    spiSym_CSR_BITS.setDisplayMode("Description")
    spiSym_CSR_BITS.setDefaultValue(0)
    spiSym_CSR_BITS.setVisible(True)

    for id in range(0,len(spiValGrp_CSR_BITS.getChildren())):
        valueName = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("caption")
        spiSym_CSR_BITS.addKey(valueName, value, description)

        index = ''.join([i for i in valueName if i.isdigit()])

        #SPI CHARSIZE BIT Mask
        spiSym_CSR_BITS_Mask = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_" + str(index) + "_BIT_MASK", None)
        spiSym_CSR_BITS_Mask.setDefaultValue(value)
        spiSym_CSR_BITS_Mask.setVisible(False)

    spiSymDummyData = spiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
    spiSymDummyData.setVisible(True)
    spiSymDummyData.setLabel("Dummy Data")
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setDependencies(DummyData_ValueUpdate, ["SPI_CHARSIZE_BITS"])

    spiSym_CSR_CPOL = spiComponent.createKeyValueSetSymbol("SPI_CLOCK_POLARITY", None)
    spiSym_CSR_CPOL.setLabel(spiBitField_CSR_CPOL.getAttribute("caption"))
    spiSym_CSR_CPOL.setOutputMode("Key")
    spiSym_CSR_CPOL.setDisplayMode("Description")
    spiSym_CSR_CPOL.setDefaultValue(0)
    spiSym_CSR_CPOL.setVisible(True)

    for id in range(0, len(spiValGrp_CSR_CPOL.getChildren())):
        valueName = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("caption")
        spiSym_CSR_CPOL.addKey(valueName, value, description)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CSR_CPOL_IL_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CSR_CPOL_IL_Mask.setDefaultValue("0x0")
    spiSym_CSR_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CSR_CPOL_IH_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CSR_CPOL_IH_Mask.setDefaultValue("0x1")
    spiSym_CSR_CPOL_IH_Mask.setVisible(False)

    spiSym_CSR_NCPHA = spiComponent.createKeyValueSetSymbol("SPI_CLOCK_PHASE", None)
    spiSym_CSR_NCPHA.setLabel(spiBitField_CSR_NCPHA.getAttribute("caption"))
    spiSym_CSR_NCPHA.setOutputMode("Key")
    spiSym_CSR_NCPHA.setDisplayMode("Description")
    spiSym_CSR_NCPHA.setDefaultValue(0)
    spiSym_CSR_NCPHA.setVisible(True)

    for id in range(0, len(spiValGrp_CSR_NCPHA.getChildren())):
        valueName = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("caption")
        spiSym_CSR_NCPHA.addKey(valueName, value, description)

    #SPI Clock Phase Leading Edge Mask
    spiSym_CTRLA_CPHA_TE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CTRLA_CPHA_TE_Mask.setDefaultValue("0x1")
    spiSym_CTRLA_CPHA_TE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CTRLA_CPHA_LE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CTRLA_CPHA_LE_Mask.setDefaultValue("0x0")
    spiSym_CTRLA_CPHA_LE_Mask.setVisible(False)

    #SPI Status OVERRUN Mask
    spiSym_STATUS_OVERRUN_Mask = spiComponent.createStringSymbol("SPI_STATUS_OVERRUN_MASK", None)
    spiSym_STATUS_OVERRUN_Mask.setDefaultValue("0x8")
    spiSym_STATUS_OVERRUN_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = spiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue("SPI" + spiInstance)
    spiSym_API_Prefix.setVisible(False)

    spiSymClockModeComment = spiComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", None)
    spiSymClockModeComment.setVisible(True)
    spiSymClockModeComment.setLabel("                                     ***SPI Mode 0 is Selected***")
    spiSymClockModeComment.setDependencies(ClockModeInfo, ["SPI_CLOCK_POLARITY","SPI_CLOCK_PHASE"])

    # Dependency Status for interrupt
    global spiSymIntEnComment
    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_NVIC_ENABLE_COMMENT", None)
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setDependencies(InterruptStatusWarning, ["core." + spiSymNVICVector])

    # Dependency Status for clock
    spiSymClkEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_CLK_ENABLE_COMMENT", None)
    spiSymClkEnComment.setVisible(False)
    spiSymClkEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Peripheral Clock is Disabled in Clock Manager")
    spiSymClkEnComment.setDependencies(ClockStatusWarning, ["core.PMC_ID_SPI" + str(spiInstance)])

    # Warning message when PLIB is configured in non-interrupt mode but used with driver.
    global spiInterruptDriverModeComment
    spiInterruptDriverModeComment = spiComponent.createCommentSymbol("SPI_INT_DRIVER_COMMENT", None)
    spiInterruptDriverModeComment.setVisible(False)
    spiInterruptDriverModeComment.setLabel("Warning!!! SPI PLIB to be used with driver, must be configured in interrupt mode")

    configName = Variables.get("__CONFIGURATION_NAME")

    spiHeaderFile = spiComponent.createFileSymbol("SPI_COMMON_HEADER", None)
    spiHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spi.h")
    spiHeaderFile.setOutputName("plib_spi.h")
    spiHeaderFile.setDestPath("peripheral/spi/")
    spiHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/")
    spiHeaderFile.setType("HEADER")
    spiHeaderFile.setMarkup(False)
    spiHeaderFile.setOverwrite(True)

    spiHeader1File = spiComponent.createFileSymbol("SPI_HEADER", None)
    spiHeader1File.setSourcePath("../peripheral/spi_6088/templates/plib_spix.h.ftl")
    spiHeader1File.setOutputName("plib_spi" + str(spiInstance) + ".h")
    spiHeader1File.setDestPath("/peripheral/spi/")
    spiHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiHeader1File.setType("HEADER")
    spiHeader1File.setMarkup(True)

    spiSource1File = spiComponent.createFileSymbol("SPI_SOURCE", None)
    spiSource1File.setSourcePath("../peripheral/spi_6088/templates/plib_spix.c.ftl")
    spiSource1File.setOutputName("plib_spi" + str(spiInstance) + ".c")
    spiSource1File.setDestPath("/peripheral/spi/")
    spiSource1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiSource1File.setType("SOURCE")
    spiSource1File.setMarkup(True)

    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_6088/templates/system/system_initialize.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_6088/templates/system/system_definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)
