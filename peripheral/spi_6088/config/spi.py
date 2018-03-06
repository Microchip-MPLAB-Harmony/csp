# Dependency Function to show or hide the warning message depending on Clock/Interrupt enable/disable status
def ClockInterruptStatusWarning(symbol, event):
   if event["value"] == False:
       symbol.setVisible(True)
   else:
       symbol.setVisible(False)
    
def setupInterruptHandler(spiInterrupt, event): 
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
    clk = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))
    baud = Database.getSymbolValue("spi" + str(spiInstance), "SPI_BAUD_RATE")
    
    if event["id"] == "SPI_BAUD_RATE":
        baud = event["value"]
    if event["id"] == "MASTERCLK_FREQ":
        clk = int(event["value"])
    
    SCBR = clk/baud
    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255
    spiSym_CSR_SCBR_VALUE.setValue(SCBR, 1)

        
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

    spiMenu = spiComponent.createMenuSymbol(None, None)
    spiMenu.setLabel("Hardware Settings ")
    
    spiIndex = spiComponent.createIntegerSymbol("SPI_INDEX", spiMenu)
    spiIndex.setVisible(False)
    spiIndex.setDefaultValue(int(spiInstance))
    
    spiInterrupt = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", spiMenu)
    spiInterrupt.setLabel("Interrupt Mode")
    #By Default interrupt mode is enabled and corresponding information is passed to NVIC manager
    spiInterrupt.setDefaultValue(True)
    spiInterrupt.setDependencies(setupInterruptHandler, ["SPI_INTERRUPT_MODE"])
    Database.setSymbolValue("core", NVICVector, True, 1)
    Database.setSymbolValue("core", NVICHandler, "SPI" + str(spiInstance) + "_InterruptHandler", 1)
    Database.setSymbolValue("core", NVICHandlerLock, True, 1)   
    
    spiSym_MR_MSTR = spiComponent.createKeyValueSetSymbol("SPI_MR_MSTR", spiMenu)
    spiSym_MR_MSTR.setLabel(spiBitField_MR_MSTR.getDescription())
    spiSym_MR_MSTR.setOutputMode("Key")
    spiSym_MR_MSTR.setDisplayMode("Description")
    spiSym_MR_MSTR.setDefaultValue(0)
    spiSym_MR_MSTR.setReadOnly(True)

    count = spiValGrp_MR_MSTR.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_MR_MSTR.getValueNames()[id]
        spiSym_MR_MSTR.addKey(valueName, spiValGrp_MR_MSTR.getValue(valueName).getValue(), spiValGrp_MR_MSTR.getValue(valueName).getDescription())
    
    defaultbaudRate = 1000000
    spiSym_CSR_SCBR = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", spiMenu)
    spiSym_CSR_SCBR.setLabel("Baud Rate in Hz")
    spiSym_CSR_SCBR.setDefaultValue(defaultbaudRate)
    spiSym_CSR_SCBR.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])
    
    defaultSCBR = int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))/defaultbaudRate
    #local variable for code generation
    spiSym_CSR_SCBR_VALUE = spiComponent.createIntegerSymbol("SPI_CSR_SCBR_VALUE", spiMenu)
    spiSym_CSR_SCBR_VALUE.setDefaultValue(defaultSCBR)
    spiSym_CSR_SCBR_VALUE.setVisible(False)
    spiSym_CSR_SCBR_VALUE.setDependencies(SCBR_ValueUpdate, ["SPI_BAUD_RATE", "core.MASTERCLK_FREQ"])
        
    spiSym_MR_PCS = spiComponent.createKeyValueSetSymbol("SPI_MR_PCS", spiMenu)
    spiSym_MR_PCS.setLabel(spiBitField_MR_PCS.getDescription())
    spiSym_MR_PCS.setOutputMode("Key")
    spiSym_MR_PCS.setDisplayMode("Description")
    spiSym_MR_PCS.setDefaultValue(0)
    spiSym_MR_PCS.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    count = spiValGrp_MR_PCS.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_MR_PCS.getValueNames()[id]
        spiSym_MR_PCS.addKey(valueName, spiValGrp_MR_PCS.getValue(valueName).getValue(), spiValGrp_MR_PCS.getValue(valueName).getDescription())       
    
    
    spiSym_CSR_BITS = spiComponent.createKeyValueSetSymbol("SPI_CSR_BITS", spiMenu)
    spiSym_CSR_BITS.setLabel(spiBitField_CSR_BITS.getDescription())
    spiSym_CSR_BITS.setOutputMode("Key")
    spiSym_CSR_BITS.setDisplayMode("Description")
    spiSym_CSR_BITS.setDefaultValue(0)
    spiSym_CSR_BITS.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    count = spiValGrp_CSR_BITS.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_BITS.getValueNames()[id]
        spiSym_CSR_BITS.addKey(valueName, spiValGrp_CSR_BITS.getValue(valueName).getValue(), spiValGrp_CSR_BITS.getValue(valueName).getDescription())
 
        
    spiSym_CSR_CPOL = spiComponent.createKeyValueSetSymbol("SPI_CSR_CPOL", spiMenu)
    spiSym_CSR_CPOL.setLabel(spiBitField_CSR_CPOL.getDescription())
    spiSym_CSR_CPOL.setOutputMode("Key")
    spiSym_CSR_CPOL.setDisplayMode("Description")
    spiSym_CSR_CPOL.setDefaultValue(0)
    spiSym_CSR_CPOL.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    count = spiValGrp_CSR_CPOL.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_CPOL.getValueNames()[id]
        spiSym_CSR_CPOL.addKey(valueName, spiValGrp_CSR_CPOL.getValue(valueName).getValue(), spiValGrp_CSR_CPOL.getValue(valueName).getDescription())

    
    spiSym_CSR_NCPHA = spiComponent.createKeyValueSetSymbol("SPI_CSR_NCPHA", spiMenu)
    spiSym_CSR_NCPHA.setLabel(spiBitField_CSR_NCPHA.getDescription())
    spiSym_CSR_NCPHA.setOutputMode("Key")
    spiSym_CSR_NCPHA.setDisplayMode("Description")
    spiSym_CSR_NCPHA.setDefaultValue(0)
    spiSym_CSR_NCPHA.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    count = spiValGrp_CSR_NCPHA.getValueCount()
    for id in range(0,count):
        valueName = spiValGrp_CSR_NCPHA.getValueNames()[id]
        spiSym_CSR_NCPHA.addKey(valueName, spiValGrp_CSR_NCPHA.getValue(valueName).getValue(), spiValGrp_CSR_NCPHA.getValue(valueName).getDescription())
     
     
    # Dependency Status for interrupt
    global spiSymIntEnComment
    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_NVIC_ENABLE_COMMENT", spiMenu)
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setDependencies(ClockInterruptStatusWarning, ["core." + NVICVector])
    
    # Dependency Status for clock
    spiSymClkEnComment = spiComponent.createCommentSymbol("SPI" + str(spiInstance) + "_CLK_ENABLE_COMMENT", spiMenu)
    spiSymClkEnComment.setVisible(False)
    spiSymClkEnComment.setLabel("Warning!!! SPI" + str(spiInstance) + " Peripheral Clock is Disabled in Clock Manager")
    spiSymClkEnComment.setDependencies(ClockInterruptStatusWarning, ["core.PMC_ID_SPI" + str(spiInstance)])
    
    configName = Variables.get("__CONFIGURATION_NAME")
    
    spiHeaderFile = spiComponent.createFileSymbol(None, None)
    spiHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spi.h")
    spiHeaderFile.setOutputName("plib_spi.h")
    spiHeaderFile.setDestPath("peripheral/spi/")
    spiHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/")
    spiHeaderFile.setType("HEADER")
    spiHeaderFile.setOverwrite(True)
    
    spiHeader1File = spiComponent.createFileSymbol(None, None)
    spiHeader1File.setSourcePath("../peripheral/spi_6088/templates/plib_spi.h.ftl")
    spiHeader1File.setOutputName("plib_spi" + str(spiInstance) + ".h")
    spiHeader1File.setDestPath("/peripheral/spi/")
    spiHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiHeader1File.setType("HEADER")
    spiHeader1File.setMarkup(True)
    
    spiSource1File = spiComponent.createFileSymbol(None, None)
    spiSource1File.setSourcePath("../peripheral/spi_6088/templates/plib_spi.c.ftl")
    spiSource1File.setOutputName("plib_spi" + str(spiInstance) + ".c")
    spiSource1File.setDestPath("/peripheral/spi/")
    spiSource1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiSource1File.setType("SOURCE")
    spiSource1File.setMarkup(True)
    
    spiSystemInitFile = spiComponent.createFileSymbol(None, None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_6088/templates/system/system_initialize.c.ftl")
    spiSystemInitFile.setMarkup(True)
    
    spiSystemDefFile = spiComponent.createFileSymbol(None, None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_6088/templates/system/system_definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)
    