global uartCapabilityId
global spiCapabilityId
global i2cCapabilityId

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global sercomInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

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
        if usartSym_Interrupt_Mode.getValue() == False:
            usartSym_Interrupt_Mode.clearValue()
            usartSym_Interrupt_Mode.setValue(True, 2)
        usartSym_Interrupt_Mode.setReadOnly(True)
    elif capability == spiCapabilityId:
        sercomComponent.setCapabilityEnabled(uartCapabilityId, False)
        sercomComponent.setCapabilityEnabled(spiCapabilityId, True)
        sercomComponent.setCapabilityEnabled(i2cCapabilityId, False)
        sercomSym_OperationMode.setSelectedKey("SPIM", 2)
        if spiSym_Interrupt_Mode.getValue() == False:
            spiSym_Interrupt_Mode.clearValue()
            spiSym_Interrupt_Mode.setValue(True, 2)
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
    elif event["value"] == 0x3:
        component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(True)
    elif event["value"] == 0x5:
        component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(True)

def setSERCOMInterruptData(status, sercomMode):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, status, 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if status == True:
        Database.setSymbolValue("core", InterruptHandler, sercomInstanceName.getValue() + "_" + sercomMode + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, sercomInstanceName.getValue() + "_Handler", 2)

def updateSERCOMInterruptStatus(symbol, event):

    global i2cSym_Interrupt_Mode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode
    global sercomSym_OperationMode

    sercomMode = ""

    if event["id"] == "SERCOM_MODE":
        sercomInterruptStatus = False
        sercomUSARTMode = (event["value"] == 0x1) and (usartSym_Interrupt_Mode.getValue() == True)
        sercomSPIMode = (event["value"] == 0x3) and (spiSym_Interrupt_Mode.getValue() == True)
        sercomI2CMode = (event["value"] == 0x5) and (i2cSym_Interrupt_Mode.getValue() == True)

        if sercomUSARTMode == True:
            sercomMode = "USART"
            sercomInterruptStatus = True
        elif sercomSPIMode == True:
            sercomMode = "SPI"
            sercomInterruptStatus = True
        elif sercomI2CMode == True:
            sercomMode = "I2C"
            sercomInterruptStatus = True

        setSERCOMInterruptData(sercomInterruptStatus, sercomMode)
    else:
        if sercomSym_OperationMode.getValue() == 1:
            sercomMode = "USART"
        elif sercomSym_OperationMode.getValue() == 3:
            sercomMode = "SPI"
        elif sercomSym_OperationMode.getValue() == 5:
            sercomMode == "USART"

        setSERCOMInterruptData(event["value"], sercomMode)

def updateSERCOMInterruptWarringStatus(symbol, event):

    global i2cSym_Interrupt_Mode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode
    global sercomSym_OperationMode

    sercomUSARTMode = (sercomSym_OperationMode.getValue() == 0x1) and (usartSym_Interrupt_Mode.getValue() == True)
    sercomSPIMode = (sercomSym_OperationMode.getValue() == 0x3) and (spiSym_Interrupt_Mode.getValue() == True)
    sercomI2CMode = (sercomSym_OperationMode.getValue() == 0x5) and (i2cSym_Interrupt_Mode.getValue() == True)

    if sercomUSARTMode == True or sercomSPIMode == True or sercomI2CMode == True:
        symbol.setVisible(event["value"])

def updateSERCOMClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateSERCOMDMATransferRegister(symbol, event):

    symbol.clearValue()

    if event["value"] == 0x1:
        symbol.setValue("&(" + sercomInstanceName.getValue() + "_REGS->USART.DATA)", 2)
    elif event["value"] == 0x3:
        symbol.setValue("&(" + sercomInstanceName.getValue() + "_REGS->SPI.DATA)", 2)
    else:
        symbol.setValue("", 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(sercomComponent):

    global uartCapabilityId
    global spiCapabilityId
    global i2cCapabilityId
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global sercomInstanceName
    global sercomSym_OperationMode

    sercomInstanceName = sercomComponent.createStringSymbol("SERCOM_INSTANCE_NAME", None)
    sercomInstanceName.setVisible(False)
    sercomInstanceName.setDefaultValue(sercomComponent.getID().upper())

    Log.writeInfoMessage("Running " + sercomInstanceName.getValue())

    uartCapabilityId = sercomInstanceName.getValue() + "_UART"
    spiCapabilityId = sercomInstanceName.getValue() + "_SPI"
    i2cCapabilityId = sercomInstanceName.getValue() + "_I2C"

    #clock enable
    Database.clearSymbolValue("core", sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE")
    Database.setSymbolValue("core", sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE", True, 2)

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

    #SERCOM code generation dependecy based on selected mode
    sercomSym_CodeGeneration = sercomComponent.createBooleanSymbol("SERCOM_CODE_GENERATION", sercomSym_OperationMode)
    sercomSym_CodeGeneration.setVisible(False)
    sercomSym_CodeGeneration.setDependencies(setSERCOMCodeGenerationProperty, ["SERCOM_MODE"])

    #SERCOM Transmit data register
    sercomSym_TxRegister = sercomComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", sercomSym_OperationMode)
    sercomSym_TxRegister.setDefaultValue("&(" + sercomInstanceName.getValue() + "_REGS->USART.DATA)")
    sercomSym_TxRegister.setVisible(False)
    sercomSym_TxRegister.setDependencies(updateSERCOMDMATransferRegister, ["SERCOM_MODE"])

    #SERCOM Receive data register
    sercomSym_RxRegister = sercomComponent.createStringSymbol("RECEIVE_DATA_REGISTER", sercomSym_OperationMode)
    sercomSym_RxRegister.setDefaultValue("&(" + sercomInstanceName.getValue() + "_REGS->USART.DATA)")
    sercomSym_RxRegister.setVisible(False)
    sercomSym_RxRegister.setDependencies(updateSERCOMDMATransferRegister, ["SERCOM_MODE"])

    ###################################################################################################
    ########################################## SERCOM MODE ############################################
    ###################################################################################################

    sercomModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]")
    sercomModuleID = sercomModuleNode.getAttribute("id")

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_i2c.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_spi.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_" + sercomModuleID + "/config/sercom_usart.py")

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = sercomInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = sercomInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = sercomInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = sercomInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for Interrupt
    setSERCOMInterruptData(True, "USART")

    # Interrupt Dynamic settings
    sercomSym_UpdateInterruptStatus = sercomComponent.createBooleanSymbol("SERCOM_INTERRUPT_STATUS", None)
    sercomSym_UpdateInterruptStatus.setDependencies(updateSERCOMInterruptStatus, ["SERCOM_MODE", "USART_INTERRUPT_MODE", "SPI_INTERRUPT_MODE"])
    sercomSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    sercomSym_IntEnComment = sercomComponent.createCommentSymbol("SERCOM_INTERRUPT_ENABLE_COMMENT", None)
    sercomSym_IntEnComment.setVisible(False)
    sercomSym_IntEnComment.setLabel("Warning!!! " + sercomInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    sercomSym_IntEnComment.setDependencies(updateSERCOMInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    sercomSym_ClkEnComment = sercomComponent.createCommentSymbol("SERCOM_CLOCK_ENABLE_COMMENT", None)
    sercomSym_ClkEnComment.setLabel("Warning!!! SERCOM Peripheral Clock is Disabled in Clock Manager")
    sercomSym_ClkEnComment.setVisible(False)
    sercomSym_ClkEnComment.setDependencies(updateSERCOMClockWarringStatus, ["core." + sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    usartHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.h.ftl")
    usartHeaderFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_usart"+".h")
    usartHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setMarkup(True)

    usartCommonHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_COMMON_HEADER", None)
    usartCommonHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart_common.h")
    usartCommonHeaderFile.setOutputName("plib_sercom_usart_common.h")
    usartCommonHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart")
    usartCommonHeaderFile.setType("HEADER")
    usartCommonHeaderFile.setMarkup(True)

    usartSourceFile = sercomComponent.createFileSymbol("SERCOM_USART_SOURCE", None)
    usartSourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.c.ftl")
    usartSourceFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_usart"+".c")
    usartSourceFile.setDestPath("/peripheral/sercom/usart/")
    usartSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartSourceFile.setType("SOURCE")
    usartSourceFile.setMarkup(True)

    spiSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIM_HEADER", None)
    spiSym_HeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi.h.ftl")
    spiSym_HeaderFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_spi.h")
    spiSym_HeaderFile.setDestPath("/peripheral/sercom/spim")
    spiSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_HeaderFile.setType("HEADER")
    spiSym_HeaderFile.setMarkup(True)
    spiSym_HeaderFile.setEnabled(False)

    spiSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIM_COMMON_HEADER", None)
    spiSym_Header1File.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi_common.h")
    spiSym_Header1File.setOutputName("plib_sercom_spi_common.h")
    spiSym_Header1File.setDestPath("/peripheral/sercom/spim")
    spiSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_Header1File.setType("HEADER")
    spiSym_Header1File.setMarkup(True)
    spiSym_Header1File.setEnabled(False)

    spiSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIM_SOURCE", None)
    spiSym_SourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_spi.c.ftl")
    spiSym_SourceFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_spi.c")
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
    i2cmHeaderFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_i2c.h")
    i2cmHeaderFile.setDestPath("/peripheral/sercom/i2cm")
    i2cmHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmHeaderFile.setType("HEADER")
    i2cmHeaderFile.setMarkup(True)
    i2cmHeaderFile.setEnabled(False)

    i2cmSourceFile = sercomComponent.createFileSymbol("SERCOM_I2CM_SOURCE", None)
    i2cmSourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_i2c.c.ftl")
    i2cmSourceFile.setOutputName("plib_"+sercomInstanceName.getValue().lower()+"_i2c.c")
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

