def instantiateComponent(rxlpComponent):
    instanceName = rxlpComponent.createStringSymbol("RXLP_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(rxlpComponent.getID().upper());

    filterSym = rxlpComponent.createBooleanSymbol("FILTER", None)
    filterSym.setLabel("Filter")
    filterSym.setDescription("Enable Rx Digital Filter")
    filterSym.setVisible(True)
    filterSym.setDefaultValue(False)

    mrRegParity = Register.getRegisterModule("RXLP").getRegisterGroup("RXLP").getRegister("RXLP_MR").getBitfield("PAR")
    mrRegParityValues = Register.getRegisterModule("RXLP").getValueGroup(mrRegParity.getValueGroupName())
    parity = rxlpComponent.createKeyValueSetSymbol("PARITY", None)
    parity.setLabel("Parity")
    parity.setVisible(True)
    parity.setOutputMode("Value")
    parity.setDisplayMode("Key")
    for name in mrRegParityValues.getValueNames():
        value = mrRegParityValues.getValue(name)
        parity.addKey(value.getName(), value.getValue(), value.getDescription())


    cd = rxlpComponent.createIntegerSymbol("CD", None)
    cd.setVisible(True)
    cd.setLabel("CD")
    cd.setDescription("Baud rate is 32.768Khz / (16 * CD)")
    cd.setMin(1)
    cd.setMax(3)

    cdComment = rxlpComponent.createCommentSymbol(None, None)
    cdComment.setVisible(True)
    cdComment.setLabel("Baud Rate: " + str(32768/(16 * int(cd.getValue()))))
    cdComment.setDependencies(lambda symbol, event: symbol.setLabel("Baud Rate: " + str(32768/(16*int(cd.getValue())))), ["CD"])

    val1 = rxlpComponent.createIntegerSymbol("VAL1", None)
    val1.setLabel("VAL1")
    val1.setMin(0)
    val1.setMax(255)

    val2 = rxlpComponent.createIntegerSymbol("VAL2", None)
    val2.setLabel("VAL2")
    val2.setMin(0)
    val2.setMax(255)

    configName = Variables.get("__CONFIGURATION_NAME")

    srcFile = rxlpComponent.createFileSymbol(None, None)
    srcFile.setSourcePath("../peripheral/rxlp_11285/templates/plib_rxlp.c.ftl")
    srcFile.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    srcFile.setDestPath("/peripheral/rxlp/")
    srcFile.setProjectPath("config/"+configName+"/peripheral/rxlp/")
    srcFile.setType("SOURCE")
    srcFile.setOverwrite(True)
    srcFile.setMarkup(True)

    hdrFile = rxlpComponent.createFileSymbol(None, None)
    hdrFile.setSourcePath("../peripheral/rxlp_11285/templates/plib_rxlp.h.ftl")
    hdrFile.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    hdrFile.setDestPath("/peripheral/rxlp/")
    hdrFile.setProjectPath("config/"+configName+"/peripheral/rxlp/")
    hdrFile.setType("HEADER")
    hdrFile.setOverwrite(True)
    hdrFile.setMarkup(True)

    rxlpSystemInitFile = rxlpComponent.createFileSymbol(None, None)
    rxlpSystemInitFile.setType("STRING")
    rxlpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rxlpSystemInitFile.setSourcePath("../peripheral/rxlp_11285/templates/system/initialization.c.ftl")
    rxlpSystemInitFile.setMarkup(True)

    rxlpSystemDefFile = rxlpComponent.createFileSymbol(None, None)
    rxlpSystemDefFile.setType("STRING")
    rxlpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rxlpSystemDefFile.setSourcePath("../peripheral/rxlp_11285/templates/system/definitions.h.ftl")
    rxlpSystemDefFile.setMarkup(True)
