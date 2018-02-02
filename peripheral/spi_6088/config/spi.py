global sysClock_SPI
sysClock_SPI = Database.getSymbolValue("PMC", "SYS_CLK_MASTERCLK_FREQ")
#Above API is not working, so hard coding MCLK value for now
sysClock_SPI = 150000000

def showBaud(spiSym_CSR_SCBR, spiSym_MR_MSTR):
    if spiSym_MR_MSTR.getValue() == "Master":
        spiSym_CSR_SCBR.setVisible(True)
    else:
        spiSym_CSR_SCBR.setVisible(False)
        
def CPOL_ValueUpdate(spiSym_CSR_CPOL_VALUE, spiSym_CSR_CPOL):
    # taking the value fro, ATDF is not working somehow
    #testSym = spiValGrp_CSR_CPOL.getValue(spiSym_CSR_CPOL.getValue())
    #testSymValue = testSym.getValue()
    #print(testSym)
    #print(testSymValue)
    #print("IDLE_HIGH")
    #spiSym_CSR_CPOL_VALUE.setValue(spiSym_CSR_CPOL_VALUE.getID() + "temp", testSymValue, 1)
    if spiSym_CSR_CPOL.getValue() == "IDLE_HIGH":
        spiSym_CSR_CPOL_VALUE.setValue(spiSym_CSR_CPOL_VALUE.getID() + "temp", 0x1, 1)
    else:
        spiSym_CSR_CPOL_VALUE.setValue(spiSym_CSR_CPOL_VALUE.getID() + "temp", 0x0, 1)

def NCPHA_ValueUpdate(spiSym_CSR_NCPHA_VALUE, spiSym_CSR_NCPHA):
    if spiSym_CSR_NCPHA.getValue() == "DATA_CAPTURED_ON_LEADING_EDGE":
        spiSym_CSR_NCPHA_VALUE.setValue(spiSym_CSR_NCPHA_VALUE.getID() + "temp", 0x1, 1)
    else:
        spiSym_CSR_NCPHA_VALUE.setValue(spiSym_CSR_NCPHA_VALUE.getID() + "temp", 0x0, 1)

def SCBR_ValueUpdate(spiSym_CSR_SCBR_VALUE, spiSym_CSR_SCBR):
    SCBR = sysClock_SPI/spiSym_CSR_SCBR.getValue()
    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255
    spiSym_CSR_SCBR_VALUE.setValue(spiSym_CSR_SCBR_VALUE.getID() + "temp", SCBR, 1)

  
spiRegModule = Register.getRegisterModule("SPI")
spiRegGroup = spiRegModule.getRegisterGroup("SPI")

spiReg_MR = spiRegGroup.getRegister("SPI_MR")
spiBitField_MR_MSTR = spiReg_MR.getBitfield("MSTR")
spiValGrp_MR_MSTR = spiRegModule.getValueGroup(spiBitField_MR_MSTR.getValueGroupName())


spiReg_CSR = spiRegGroup.getRegister("SPI_CSR")
spiBitField_CSR_BITS = spiReg_CSR.getBitfield("BITS")
spiValGrp_CSR_BITS = spiRegModule.getValueGroup(spiBitField_CSR_BITS.getValueGroupName())

spiBitField_CSR_CPOL = spiReg_CSR.getBitfield("CPOL")
spiValGrp_CSR_CPOL = spiRegModule.getValueGroup(spiBitField_CSR_CPOL.getValueGroupName())

spiBitField_CSR_NCPHA = spiReg_CSR.getBitfield("NCPHA")
spiValGrp_CSR_NCPHA = spiRegModule.getValueGroup(spiBitField_CSR_NCPHA.getValueGroupName())

def instantiateComponent(spiComponent):

    num = spiComponent.getID()[-1:]
    print("Running SPI" + str(num))
    
    spiMenu = spiComponent.createMenuSymbol(None, None)
    spiMenu.setLabel("Hardware Settings ")
    
    spiIndex = spiComponent.createIntegerSymbol("SPI_INDEX", spiMenu)
    spiIndex.setVisible(False)
    spiIndex.setDefaultValue(int(num))
    
    spiInterrupt = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", spiMenu)
    print(spiInterrupt)
    spiInterrupt.setLabel("Interrupt Mode")
    spiInterrupt.setDefaultValue(True)
    

    spiSym_MR_MSTR = spiComponent.createComboSymbol("SPI_MR_MSTR", spiMenu, spiValGrp_MR_MSTR.getValueNames())
    spiSym_MR_MSTR.setLabel(spiBitField_MR_MSTR.getDescription())
    spiSym_MR_MSTR.setDefaultValue("Master")
    
    spiSym_CSR_SCBR = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", spiMenu)
    spiSym_CSR_SCBR.setLabel("Baud Rate in Hz")
    spiSym_CSR_SCBR.setDefaultValue(1000000)
    spiSym_CSR_SCBR.setDependencies(showBaud, ["SPI_MR_MSTR"])
    
    #local variable for code generation
    spiSym_CSR_SCBR_VALUE = spiComponent.createHexSymbol("SPI_CSR_SCBR_VALUE", spiMenu)
    spiSym_CSR_SCBR_VALUE.setDefaultValue(0x96)
    spiSym_CSR_SCBR_VALUE.setVisible(False)
    spiSym_CSR_SCBR_VALUE.setDependencies(SCBR_ValueUpdate, ["SPI_BAUD_RATE"])
    
    
    spiSym_CSR_BITS = spiComponent.createComboSymbol("SPI_CSR_BITS", spiMenu, spiValGrp_CSR_BITS.getValueNames())
    spiSym_CSR_BITS.setLabel(spiBitField_CSR_BITS.getDescription())
    spiSym_CSR_BITS.setDefaultValue("_8_BIT")
    spiSym_CSR_BITS.setReadOnly(True)

    spiSym_CSR_CPOL = spiComponent.createComboSymbol("SPI_CSR_CPOL", spiMenu, spiValGrp_CSR_CPOL.getValueNames())
    spiSym_CSR_CPOL.setLabel(spiBitField_CSR_CPOL.getDescription())
    spiSym_CSR_CPOL.setDefaultValue("IDLE_LOW")
    
    #local variable for code generation
    spiSym_CSR_CPOL_VALUE = spiComponent.createHexSymbol("SPI_CSR_CPOL_VALUE", spiMenu)
    spiSym_CSR_CPOL_VALUE.setDefaultValue(0x0)
    spiSym_CSR_CPOL_VALUE.setVisible(False)
    spiSym_CSR_CPOL_VALUE.setDependencies(CPOL_ValueUpdate, ["SPI_CSR_CPOL"])

    
    spiSym_CSR_NCPHA = spiComponent.createComboSymbol("SPI_CSR_NCPHA", spiMenu, spiValGrp_CSR_NCPHA.getValueNames())
    spiSym_CSR_NCPHA.setLabel(spiBitField_CSR_NCPHA.getDescription())
    spiSym_CSR_NCPHA.setDefaultValue("DATA_CHANGED_ON_LEADING_EDGE")
    
    #local variable for code generation
    spiSym_CSR_NCPHA_VALUE = spiComponent.createHexSymbol("SPI_CSR_NCPHA_VALUE", spiMenu)
    spiSym_CSR_NCPHA_VALUE.setDefaultValue(0x0)
    spiSym_CSR_NCPHA_VALUE.setVisible(False)
    spiSym_CSR_NCPHA_VALUE.setDependencies(NCPHA_ValueUpdate, ["SPI_CSR_NCPHA"])
    
    
    configName = Variables.get("__CONFIGURATION_NAME")
    
    spiHeader1File = spiComponent.createFileSymbol(None, None)
    spiHeader1File.setSourcePath("../peripheral/spi_6088/templates/plib_spi.h.ftl")
    spiHeader1File.setOutputName("plib_spi" + str(num) + ".h")
    spiHeader1File.setDestPath("/peripheral/spi/")
    spiHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiHeader1File.setType("HEADER")
    spiHeader1File.setMarkup(True)
    
    spiCommonHeader1File = spiComponent.createFileSymbol(None, None)
    spiCommonHeader1File.setSourcePath("../peripheral/spi_6088/templates/plib_spi.h")
    spiCommonHeader1File.setOutputName("plib_spi.h")
    spiCommonHeader1File.setDestPath("/peripheral/spi/")
    spiCommonHeader1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiCommonHeader1File.setType("HEADER")
    spiCommonHeader1File.setMarkup(False)
    
    spiSource1File = spiComponent.createFileSymbol(None, None)
    spiSource1File.setSourcePath("../peripheral/spi_6088/templates/plib_spi.c.ftl")
    spiSource1File.setOutputName("plib_spi" + str(num) + ".c")
    spiSource1File.setDestPath("/peripheral/spi/")
    spiSource1File.setProjectPath("config/" + configName +"/peripheral/spi/")
    spiSource1File.setType("SOURCE")
    spiSource1File.setMarkup(True)
    
    spiSystemInitFile = spiComponent.createFileSymbol(None, None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_6088/templates/system/system_initialize.c.ftl")
    spiSystemInitFile.setMarkup(True)
    
    spiSystemIntFile = spiComponent.createFileSymbol(None, None)
    spiSystemIntFile.setType("STRING")
    spiSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
    spiSystemIntFile.setSourcePath("../peripheral/spi_6088/templates/system/system_interrupt.c.ftl")
    spiSystemIntFile.setMarkup(True)
    
    spiSystemDefFile = spiComponent.createFileSymbol(None, None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_6088/templates/system/system_definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)