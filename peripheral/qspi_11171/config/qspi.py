qspiRegModule = Register.getRegisterModule("QSPI")
qspiRegGroup = qspiRegModule.getRegisterGroup("QSPI")

qspiReg_MR = qspiRegGroup.getRegister("QSPI_MR")

qspiBitField_MR_SMM = qspiReg_MR.getBitfield("SMM")
qspiBitField_MR_CSMODE = qspiReg_MR.getBitfield("CSMODE")

qspiValGrp_MR_SMM = qspiRegModule.getValueGroup(qspiBitField_MR_SMM.getValueGroupName())
qspiValGrp_MR_CSMODE = qspiRegModule.getValueGroup(qspiBitField_MR_CSMODE.getValueGroupName())

qspiReg_SCR = qspiRegGroup.getRegister("QSPI_SCR")

qspiBitField_SCR_CPOL = qspiReg_SCR.getBitfield("CPOL")
qspiBitField_SCR_CPHA = qspiReg_SCR.getBitfield("CPHA")
qspiBitField_SCR_SCBR = qspiReg_SCR.getBitfield("SCBR")

def getMasterClkFrequency():
    return int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))

def getQspiClkFrequency():
    global num
    return Database.getSymbolValue("qspi" + str(num), "QSPI_CLK_FREQ")

def getQspiScbrValue():
    global num
    return Database.getSymbolValue("qspi" + str(num), "QSPI_SCBR")

def setQspiClkFrequency(symbol, event):
    master_clk_freq = getMasterClkFrequency()

    if ( symbol.getID() == "QSPI_CLK_FREQ" ):
        qspi_clk_freq = master_clk_freq / (getQspiScbrValue() + 1)

        if ( qspi_clk_freq > symbol.getMax()):
            qspi_clk_freq = symbol.getMax()

        symbol.clearValue()
        symbol.setValue(qspi_clk_freq, 1)

    elif ( symbol.getID() == "QSPI_CLK_COMMENT" ):
        qspi_clk_sym = event["symbol"]
        if ( getQspiClkFrequency() >= qspi_clk_sym.getMax()):
            symbol.setLabel("*** QSPI Clock Frequency Is Set To Maximum " + str(getQspiClkFrequency()) + " for Master Clock Frequency At " + str(master_clk_freq))
        else:
            symbol.setLabel("*** QSPI Clock Frequency Is Set To " + str(getQspiClkFrequency()) + " for Master Clock Frequency At " + str(master_clk_freq))

def setMasterClkDependency(qspiMasterClkComment, masterClkSymbol):
    if (masterClkSymbol["value"] == False):
        qspiMasterClkComment.setVisible(True)
    else:
        qspiMasterClkComment.setVisible(False)

def instantiateComponent(qspiComponent):

    global num

    num = qspiComponent.getID()[-1:]
    print("Running QSPI" + str(num))

    #Enable Clock for QSPI instance 
    Database.clearSymbolValue("core", "PMC_ID_QSPI")
    Database.setSymbolValue("core", "PMC_ID_QSPI", True, 1)

    qspiMenu = qspiComponent.createMenuSymbol("QSPI", None)
    qspiMenu.setLabel("Hardware Settings ")

    qspiSMM = qspiComponent.createKeyValueSetSymbol("QSPI_SMM", qspiMenu)
    qspiSMM.setLabel(qspiBitField_MR_SMM.getDescription())
    qspiSMM.setVisible(True)
    qspiSMM.setOutputMode("Key")
    qspiSMM.setDisplayMode("Description")
    qspiSMM.setSelectedKey("MEMORY",1)
    qspiSMM.setReadOnly(True)

    count = qspiValGrp_MR_SMM.getValueCount()
    for id in range(0,count):
        valueName = qspiValGrp_MR_SMM.getValueNames()[id]
        qspiSMM.addKey(valueName, qspiValGrp_MR_SMM.getValue(valueName).getValue(), qspiValGrp_MR_SMM.getValue(valueName).getDescription())

    qspiCSMODE = qspiComponent.createComboSymbol("QSPI_CSMODE", qspiMenu, qspiValGrp_MR_CSMODE.getValueNames())
    qspiCSMODE.setVisible(False)
    qspiCSMODE.setLabel(qspiBitField_MR_CSMODE.getDescription())
    qspiCSMODE.setDefaultValue("LASTXFER")

    qspiCPOL = qspiComponent.createKeyValueSetSymbol("QSPI_CPOL", qspiMenu)
    qspiCPOL.setLabel(qspiBitField_SCR_CPOL.getDescription())
    qspiCPOL.setVisible(True)
    qspiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    qspiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    qspiCPOL.setOutputMode("Key")
    qspiCPOL.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LOW",1)

    qspiCPHA = qspiComponent.createKeyValueSetSymbol("QSPI_CPHA", qspiMenu)
    qspiCPHA.setLabel(qspiBitField_SCR_CPHA.getDescription())
    qspiCPHA.setVisible(True)
    qspiCPHA.addKey("RISING", "1", "Data is Valid on Clock Rising Edge (CPHA=0)")
    qspiCPHA.addKey("FALLING", "1", "Data is Valid on Clock Falling Edge (CPHA=1)")
    qspiCPHA.setOutputMode("Key")
    qspiCPHA.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("RISING",1)

    qspiSCBR = qspiComponent.createIntegerSymbol("QSPI_SCBR", qspiMenu)
    qspiSCBR.setLabel(qspiBitField_SCR_SCBR.getDescription())
    qspiSCBR.setVisible(True)
    qspiSCBR.setMin(1)
    qspiSCBR.setMax(255)
    qspiSCBR.setDefaultValue(2)

    default_qspi_clk_freq = getMasterClkFrequency() / (qspiSCBR.getValue() + 1)

    qspiClkFreq = qspiComponent.createIntegerSymbol("QSPI_CLK_FREQ", qspiMenu)
    qspiClkFreq.setLabel("QSPI Clock Frequency")
    qspiClkFreq.setVisible(False)
    qspiClkFreq.setMax(66000000)
    qspiClkFreq.setDefaultValue(default_qspi_clk_freq)
    qspiClkFreq.setDependencies(setQspiClkFrequency, ["QSPI_SCBR", "core.MASTERCLK_FREQ"])

    qspiClkComment = qspiComponent.createCommentSymbol("QSPI_CLK_COMMENT", qspiMenu)
    qspiClkComment.setVisible(True)
    qspiClkComment.setLabel("*** QSPI Clock Frequency Is Set To " + str(qspiClkFreq.getValue()) +  " for Master Clock Frequency At " + str(getMasterClkFrequency()))
    qspiClkComment.setDependencies(setQspiClkFrequency, ["QSPI_CLK_FREQ"])

    qspiMasterClkComment = qspiComponent.createCommentSymbol("QSPI_MASTER_CLK_COMMENT", qspiMenu)
    qspiMasterClkComment.setVisible(False)
    qspiMasterClkComment.setLabel("WARNING!!! QSPI Peripheral Clock Is Disabled In Clock Manager")
    qspiMasterClkComment.setDependencies(setMasterClkDependency, ["core.PMC_ID_QSPI"])

    qspiIndex = qspiComponent.createIntegerSymbol("INDEX", qspiMenu)
    qspiIndex.setVisible(False)
    qspiIndex.setDefaultValue(int(num))

    configName = Variables.get("__CONFIGURATION_NAME")

    qspiHeader1File = qspiComponent.createFileSymbol(None, None)
    qspiHeader1File.setSourcePath("../peripheral/qspi_" + qspiRegModule.getID() + "/templates/plib_qspi.h")
    qspiHeader1File.setOutputName("plib_qspi.h")
    qspiHeader1File.setDestPath("/peripheral/qspi/")
    qspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader1File.setType("HEADER")

    qspiHeader1File = qspiComponent.createFileSymbol(None, None)
    qspiHeader1File.setSourcePath("../peripheral/qspi_" + qspiRegModule.getID() + "/templates/plib_qspi.h.ftl")
    qspiHeader1File.setOutputName("plib_qspi" + str(num) + ".h")
    qspiHeader1File.setDestPath("/peripheral/qspi/")
    qspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader1File.setType("HEADER")
    qspiHeader1File.setMarkup(True)
    qspiHeader1File.setOverwrite(True)

    qspiSource1File = qspiComponent.createFileSymbol(None, None)
    qspiSource1File.setSourcePath("../peripheral/qspi_" + qspiRegModule.getID() + "/templates/plib_qspi.c.ftl")
    qspiSource1File.setOutputName("plib_qspi" + str(num) + ".c")
    qspiSource1File.setDestPath("/peripheral/qspi/")
    qspiSource1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiSource1File.setType("SOURCE")
    qspiSource1File.setMarkup(True)
    qspiSource1File.setOverwrite(True)

    #QSPI Initialize 
    qspiSystemInitFile = qspiComponent.createFileSymbol(None, None)
    qspiSystemInitFile.setType("STRING")
    qspiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    qspiSystemInitFile.setSourcePath("../peripheral/qspi_" + qspiRegModule.getID() + "/templates/system/system_initialize.c.ftl")
    qspiSystemInitFile.setMarkup(True)

    #QSPI definitions header
    qspiSystemDefFile = qspiComponent.createFileSymbol(None, None)
    qspiSystemDefFile.setType("STRING")
    qspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qspiSystemDefFile.setSourcePath("../peripheral/qspi_" + qspiRegModule.getID() + "/templates/system/system_definitions.h.ftl")
    qspiSystemDefFile.setMarkup(True)
