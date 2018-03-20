# Dependency Function to show or hide the warning message depending on Clock/Interrupt enable/disable status
def ClockInterruptStatusWarning(symbol, event):
   if event["value"] == False:
       symbol.setVisible(True)
   else:
       symbol.setVisible(False)
    
def setuspiSym_CSRterruptHandler(spiInterrupt, event): 
    global NVICVector
    global NVICHandler
    global NVICHandlerLock
    global spiSymIntEnComment  
        
    if (event["value"] == True):
        Database.setSymbolValue("core", NVICVector, True, 1)
        Database.setSymbolValue("core", NVICHandler, "SPI" + str(spiInstance) + "_InterruptHandler", 1)
        Database.setSymbolValue("core", NVICHandlerLock, True, 1)
    else :
        Database.setSymbolValue("core", NVICVector, False, 1)
        Database.setSymbolValue("core", NVICHandler, "SPI" + str(spiInstance) + "_Handler", 1)
        Database.setSymbolValue("core", NVICHandlerLock, False, 1)
    
    # control warning message
    if (spiInterrupt.getValue() == True and Database.getSymbolValue("core", NVICVector) == False):
        spiSymIntEnComment.setVisible(True)
    else:
        spiSymIntEnComment.setVisible(False)
        
def getMasterClockFreq(): 
    clkSymMasterClockFreq = Database.getSymbolValue("core","MASTERCLK_FREQ") 
    return int(clkSymMasterClockFreq)
        
def showMasterDependencies(spiSym_MR_Dependencies, event):
    if event["value"] == "Master":
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
    spiSymCSRIndex.setValue(int(event["symbol"].getKey(event["value"])[-1]), 1)
    
        
spiRegModule = Register.getRegisterModule("SPI")
spiRegGroup = spiRegModule.getRegisterGroup("SPI")

spiReg_MR = spiRegGroup.getRegister("SPI_MR")
spiBitField_MR_MSTR = spiReg_MR.getBitfield("MSTR")
spiValGrp_MR_MSTR = spiRegModule.getValueGroup(spiBitField_MR_MSTR.getValueGroupName())

spiBitField_MR_PCS = spiReg_MR.getBitfield("PCS")
spiValGrp_MR_PCS = spiRegModule.getValueGroup(spiBitField_MR_PCS.getValueGroupName())


spiReg_CSR = spiRegGroup.getRegister("SPI_CSR")
spiBitField_CSR_BITS = spiReg_CSR.getBitfield("BITS")
spiValGrp_CSR_BITS = spiRegModule.getValueGroup(spiBitField_CSR_BITS.getValueGroupName())

spiBitField_CSR_CPOL = spiReg_CSR.getBitfield("CPOL")
spiValGrp_CSR_CPOL = spiRegModule.getValueGroup(spiBitField_CSR_CPOL.getValueGroupName())

spiBitField_CSR_NCPHA = spiReg_CSR.getBitfield("NCPHA")
spiValGrp_CSR_NCPHA = spiRegModule.getValueGroup(spiBitField_CSR_NCPHA.getValueGroupName())

def instantiateComponent(spiComponent):
    global spiInstance
    global NVICVector
    global NVICHandler
    global NVICHandlerLock
    global InternalNVICVectorChange
    
    InternalNVICVectorChange = False
    
    spiInstance = spiComponent.getID()[-1:]
    
    peripId = Interrupt.getInterruptIndex("SPI" + str(spiInstance))
    #IDs used in NVIC Manager
    NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"
    
    # Enable clock for SPI
    Database.setSymbolValue("core", "PMC_ID_SPI" + str(spiInstance), True, 1)
    
    spiIndex = spiComponent.createIntegerSymbol("SPI_INDEX", None)
    spiIndex.setVisible(False)
    spiIndex.setDefaultValue(int(spiInstance))
    
    spiInterrupt = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiInterrupt.setLabel("Interrupt Mode")
    #By Default interrupt mode is enabled and corresponding information is passed to NVIC manager
    spiInterrupt.setDefaultValue(True)
    spiInterrupt.setDependencies(setuspiSym_CSRterruptHandler, ["SPI_INTERRUPT_MODE"])
    Database.setSymbolValue("core", NVICVector, True, 1)
    Database.setSymbolValue("core", NVICHandler, "SPI" + str(spiInstance) + "_InterruptHandler", 1)
    Database.setSymbolValue("core", NVICHandlerLock, True, 1)   
    
    spiSym_MR_MSTR = spiComponent.createKeyValueSetSymbol("SPI_MR_MSTR", None)
    spiSym_MR_MSTR.setLabel(spiBitField_MR_MSTR.getDescription())
    spiSym_MR_MSTR.setOutputMode("Key")
    spiSym_MR_MSTR.setDisplayMode("Description")
    spiSym_MR_MSTR.setDefaultValue(0)
    spiSym_MR_MSTR.setReadOnly(True)

    count = spiValGrp_MR_MSTR.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_MR_MSTR.getValueNames()[id]
        spiSym_MR_MSTR.addKey(valueName, spiValGrp_MR_MSTR.getValue(valueName).getValue(), spiValGrp_MR_MSTR.getValue(valueName).getDescription())
    
    DefaultPCS = 2 
    spiSym_MR_PCS = spiComponent.createKeyValueSetSymbol("SPI_MR_PCS", None)
    spiSym_MR_PCS.setLabel(spiBitField_MR_PCS.getDescription())
    spiSym_MR_PCS.setOutputMode("Key")
    spiSym_MR_PCS.setDisplayMode("Key")
    spiSym_MR_PCS.setDefaultValue(DefaultPCS)
    spiSym_MR_PCS.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    count = spiValGrp_MR_PCS.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_MR_PCS.getValueNames()[id]
        spiSym_MR_PCS.addKey(valueName, spiValGrp_MR_PCS.getValue(valueName).getValue(), spiValGrp_MR_PCS.getValue(valueName).getDescription())       
    
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
    
    spiSym_CSR_BITS = spiComponent.createKeyValueSetSymbol("SPI_CSR_BITS", None)
    spiSym_CSR_BITS.setLabel(spiBitField_CSR_BITS.getDescription())
    spiSym_CSR_BITS.setOutputMode("Key")
    spiSym_CSR_BITS.setDisplayMode("Description")
    spiSym_CSR_BITS.setDefaultValue(8)
    spiSym_CSR_BITS.setVisible(True)
    
    count = spiValGrp_CSR_BITS.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_BITS.getValueNames()[id]
        spiSym_CSR_BITS.addKey(valueName, spiValGrp_CSR_BITS.getValue(valueName).getValue(), spiValGrp_CSR_BITS.getValue(valueName).getDescription())
        
    spiSym_CSR_CPOL = spiComponent.createKeyValueSetSymbol("SPI_CSR_CPOL", None)
    spiSym_CSR_CPOL.setLabel(spiBitField_CSR_CPOL.getDescription())
    spiSym_CSR_CPOL.setOutputMode("Key")
    spiSym_CSR_CPOL.setDisplayMode("Description")
    spiSym_CSR_CPOL.setDefaultValue(1)
    spiSym_CSR_CPOL.setVisible(True)
    
    count = spiValGrp_CSR_CPOL.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_CPOL.getValueNames()[id]
        spiSym_CSR_CPOL.addKey(valueName, spiValGrp_CSR_CPOL.getValue(valueName).getValue(), spiValGrp_CSR_CPOL.getValue(valueName).getDescription())
    
    spiSym_CSR_NCPHA = spiComponent.createKeyValueSetSymbol("SPI_CSR_NCPHA", None)
    spiSym_CSR_NCPHA.setLabel(spiBitField_CSR_NCPHA.getDescription())
    spiSym_CSR_NCPHA.setOutputMode("Key")
    spiSym_CSR_NCPHA.setDisplayMode("Description")
    spiSym_CSR_NCPHA.setDefaultValue(1)
    spiSym_CSR_NCPHA.setVisible(True)
    
    count = spiValGrp_CSR_NCPHA.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_NCPHA.getValueNames()[id]
        spiSym_CSR_NCPHA.addKey(valueName, spiValGrp_CSR_NCPHA.getValue(valueName).getValue(), spiValGrp_CSR_NCPHA.getValue(valueName).getDescription())
     
     
    # Dependency Status for interrupt
    global spiSymIntEnComment
    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_NVIC_ENABLE_COMMENT", None)
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setDependencies(ClockInterruptStatusWarning, ["core." + NVICVector])
    
    # Dependency Status for clock
    spiSymClkEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_CLK_ENABLE_COMMENT", None)
    spiSymClkEnComment.setVisible(False)
    spiSymClkEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Peripheral Clock is Disabled in Clock Manager")
    spiSymClkEnComment.setDependencies(ClockInterruptStatusWarning, ["core.PMC_ID_SPI" + str(spiInstance)])
    
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
    