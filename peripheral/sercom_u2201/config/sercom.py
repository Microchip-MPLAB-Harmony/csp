###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

global uartCapabilityId
global spiCapabilityId
global i2cCapabilityId

def onCapabilityConnected(event):

    global sercomSym_OperationMode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode

    capability = event["capabilityID"]
    sercomComponent = event["localComponent"]

    if capability == uartCapabilityId:
        sercomComponent.setCapabilityEnabled(uartCapabilityId, True)
        sercomComponent.setCapabilityEnabled(spiCapabilityId, False)
        sercomComponent.setCapabilityEnabled(i2cCapabilityId, False)
        sercomSym_OperationMode.setSelectedKey("USART_INT", 2)
        usartSym_Interrupt_Mode.setReadOnly(True)
    elif capability == spiCapabilityId:
        sercomComponent.setCapabilityEnabled(uartCapabilityId, False)
        sercomComponent.setCapabilityEnabled(spiCapabilityId, True)
        sercomComponent.setCapabilityEnabled(i2cCapabilityId, False)
        sercomSym_OperationMode.setSelectedKey("SPIM", 2)
        spiSym_Interrupt_Mode.setReadOnly(True)
    elif capability == i2cCapabilityId:
        sercomComponent.setCapabilityEnabled(uartCapabilityId, False)
        sercomComponent.setCapabilityEnabled(spiCapabilityId, False)
        sercomComponent.setCapabilityEnabled(i2cCapabilityId, True)
        sercomSym_OperationMode.setSelectedKey("I2CM", 2)

    sercomSym_OperationMode.setReadOnly(True)

def onCapabilityDisconnected(event):

    global sercomSym_OperationMode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode

    capability = event["capabilityID"]
    sercomComponent = event["localComponent"]

    sercomComponent.setCapabilityEnabled(uartCapabilityId, True)
    sercomComponent.setCapabilityEnabled(spiCapabilityId, True)
    sercomComponent.setCapabilityEnabled(i2cCapabilityId, True)

    sercomSym_OperationMode.setReadOnly(False)
    spiSym_Interrupt_Mode.setReadOnly(False)
    usartSym_Interrupt_Mode.setReadOnly(False)

def setSERCOMCodeGenerationProperty(symbol, event):

    component = symbol.getComponent()

    component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(False)

    if event["value"] == 0x1:
        component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(True)
        component.setCapabilityEnabled(uartCapabilityId, True)
        component.setCapabilityEnabled(spiCapabilityId, False)
        component.setCapabilityEnabled(i2cCapabilityId, False)
    elif event["value"] == 0x3:
        component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(True)
        component.setCapabilityEnabled(uartCapabilityId, False)
        component.setCapabilityEnabled(spiCapabilityId, True)
        component.setCapabilityEnabled(i2cCapabilityId, False)
    elif event["value"] == 0x05:
        component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(True)
        component.setCapabilityEnabled(uartCapabilityId, False)
        component.setCapabilityEnabled(spiCapabilityId, False)
        component.setCapabilityEnabled(i2cCapabilityId, True)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(sercomComponent):

    global uartCapabilityId
    global spiCapabilityId
    global i2cCapabilityId
    global sercomSym_OperationMode

    sercomInstanceIndex = sercomComponent.getID()[-1:]

    Log.writeInfoMessage("Running SERCOM" + str(sercomInstanceIndex))

    uartCapabilityId = "SERCOM_" + sercomInstanceIndex + "_UART"
    spiCapabilityId = "SERCOM_" + sercomInstanceIndex + "_SPI"
    i2cCapabilityId = "SERCOM_" + sercomInstanceIndex + "_I2C"

    #sercom mode Menu - Serial Communication Interfaces
    sercomSym_OperationMode = sercomComponent.createKeyValueSetSymbol("SERCOM_MODE", None)
    sercomSym_OperationMode.setLabel("Select SERCOM Operation Mode")

    sercomSym_OperationMode_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_CTRLA__MODE\"]")
    sercomSym_OperationMode_Values = []
    sercomSym_OperationMode_Values = sercomSym_OperationMode_Node.getChildren()

    sercomSym_OperationMode_Default_Val = 0

    for index in range(len(sercomSym_OperationMode_Values)):
        sercomSym_OperationMode_Key_Name = sercomSym_OperationMode_Values[index].getAttribute("name")

        if sercomSym_OperationMode_Key_Name == "USART_INT":
            sercomSym_OperationMode_Default_Val = index

        sercomSym_OperationMode_Key_Description = sercomSym_OperationMode_Values[index].getAttribute("caption")
        sercomSym_OperationMode_Key_Value = sercomSym_OperationMode_Values[index].getAttribute("value")
        sercomSym_OperationMode.addKey(sercomSym_OperationMode_Key_Name, sercomSym_OperationMode_Key_Value, sercomSym_OperationMode_Key_Description)

    sercomSym_OperationMode.setDefaultValue(sercomSym_OperationMode_Default_Val)
    sercomSym_OperationMode.setOutputMode("Key")
    sercomSym_OperationMode.setDisplayMode("Key")

    #SERCOM Instance Index
    sercomSym_INDEX = sercomComponent.createIntegerSymbol("SERCOM_INDEX", None)
    sercomSym_INDEX.setDefaultValue(int(sercomInstanceIndex))
    sercomSym_INDEX.setVisible(False)
    sercomSym_INDEX.setDependencies(setSERCOMCodeGenerationProperty, ["SERCOM_MODE"])

    sercomInstanceParametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]/instance@[name=\"SERCOM" + sercomInstanceIndex + "\"]/parameters/param@[name=\"GCLK_ID_CORE\"]")
    sercomInstanceGCLKId = int(sercomInstanceParametersNode.getAttribute("value"))

    #Peripheral Channel Index
    sercomSym_PHCTRL_INDEX = sercomComponent.createIntegerSymbol("SERCOM_PHCTRL_INDEX", None)
    sercomSym_PHCTRL_INDEX.setVisible(False)
    sercomSym_PHCTRL_INDEX.setDefaultValue(sercomInstanceGCLKId)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sercomModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]")
    sercomModuleID = sercomModuleNode.getAttribute("id")

    usartHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.h.ftl")
    usartHeaderFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_usart" + ".h")
    usartHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setMarkup(True)

    usartCommonHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_COMMON_HEADER", None)
    usartCommonHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.h")
    usartCommonHeaderFile.setOutputName("plib_sercom_usart.h")
    usartCommonHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart")
    usartCommonHeaderFile.setType("HEADER")
    usartCommonHeaderFile.setMarkup(True)

    usartSourceFile = sercomComponent.createFileSymbol("SERCOM_USART_SOURCE", None)
    usartSourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.c.ftl")
    usartSourceFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_usart" + ".c")
    usartSourceFile.setDestPath("/peripheral/sercom/usart/")
    usartSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartSourceFile.setType("SOURCE")
    usartSourceFile.setMarkup(True)

    spiSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIM_HEADER", None)
    spiSym_HeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi.h.ftl")
    spiSym_HeaderFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_spi.h")
    spiSym_HeaderFile.setDestPath("/peripheral/sercom/spim")
    spiSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_HeaderFile.setType("HEADER")
    spiSym_HeaderFile.setMarkup(True)
    spiSym_HeaderFile.setEnabled(False)

    spiSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIM_COMMON_HEADER", None)
    spiSym_Header1File.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi.h")
    spiSym_Header1File.setOutputName("plib_sercom_spi.h")
    spiSym_Header1File.setDestPath("/peripheral/sercom/spim")
    spiSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_Header1File.setType("HEADER")
    spiSym_Header1File.setMarkup(True)
    spiSym_Header1File.setEnabled(False)

    spiSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIM_SOURCE", None)
    spiSym_SourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi.c.ftl")
    spiSym_SourceFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_spi.c")
    spiSym_SourceFile.setDestPath("/peripheral/sercom/spim")
    spiSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_SourceFile.setType("SOURCE")
    spiSym_SourceFile.setMarkup(True)
    spiSym_SourceFile.setEnabled(False)

    i2cmMasterHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_MASTER_HEADER", None)
    i2cmMasterHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setOutputName("plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setDestPath("/peripheral/sercom/i2cm")
    i2cmMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmMasterHeaderFile.setType("HEADER")
    i2cmMasterHeaderFile.setMarkup(True)
    i2cmMasterHeaderFile.setEnabled(False)

    i2cmHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_HEADER", None)
    i2cmHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_i2c.h.ftl")
    i2cmHeaderFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_i2c.h")
    i2cmHeaderFile.setDestPath("/peripheral/sercom/i2cm")
    i2cmHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmHeaderFile.setType("HEADER")
    i2cmHeaderFile.setMarkup(True)
    i2cmHeaderFile.setEnabled(False)

    i2cmSourceFile = sercomComponent.createFileSymbol("SERCOM_I2CM_SOURCE", None)
    i2cmSourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_i2c.c.ftl")
    i2cmSourceFile.setOutputName("plib_sercom" + sercomInstanceIndex + "_i2c.c")
    i2cmSourceFile.setDestPath("/peripheral/sercom/i2cm")
    i2cmSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmSourceFile.setType("SOURCE")
    i2cmSourceFile.setMarkup(True)
    i2cmSourceFile.setEnabled(False)

    sercomSystemInitFile = sercomComponent.createFileSymbol("SERCOM_SYS_INIT", None)
    sercomSystemInitFile.setType("STRING")
    sercomSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sercomSystemInitFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/system/initialization.c.ftl")
    sercomSystemInitFile.setMarkup(True)

    sercomSystemDefFile = sercomComponent.createFileSymbol("SERCOM_SYS_DEF", None)
    sercomSystemDefFile.setType("STRING")
    sercomSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sercomSystemDefFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/system/definitions.h.ftl")
    sercomSystemDefFile.setMarkup(True)

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_i2c.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_spi.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_usart.py")
