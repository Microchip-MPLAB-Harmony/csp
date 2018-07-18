################################################################################
#############        Callback Functions   ######################################
################################################################################

def setSERCOMCodeGenerationProperty(symbol, event):

    component = symbol.getComponent()

    Log.writeInfoMessage("setSERCOMCodeGenerationProperty" + str(event["value"]))

    component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(False)

    if(event["value"] == 0x00 or event["value"] == 0x01):
        component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(True)
    if(event["value"] == 0x03):
        component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(True)
    elif(event["value"] == 0x05):
        component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(True)

#SPI Mode property
def setspiMODEVisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Standby property
def setspiSTANDBYVisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI DOPO property
def set_SPI_DOPO_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI DIPO property
def set_SPI_DIPO_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI clock Phase property
def set_SPI_CPHA_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Clock Polarity property
def set_SPI_CPOL_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Transfer Mode property
def set_SPI_Transfer_Mode_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Data order property
def set_SPI_DORD_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Character size property
def set_SPI_CHSIZE_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI master slave select Enable Property
def set_SPI_MASTER_SSEN_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI baud rate value selection Property
def set_SPI_BAUDRATE_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Master clock Freq selection Property
def set_SPI_MasterClockFreq_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Interrupt mode selection property
def set_SPI_INTERRUPTMODE_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Interrupt mode selection property
def set_SPI_SERIALSETUP_VisibleProperty(symbol, event):
    if(event["value"] == 0x03):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

# I2CM Run StandBy Visible Property
def seti2cmRunStandByVisibleProperty(symbol,event):
    if(event["value"] == 0x05):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# I2CM SDAHOLD Time Visible Property
def seti2cmSDAHoldTimeVisibleProperty(symbol,event):
    if(event["value"] == 0x05):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# I2CM Speed Visible Property
def seti2cmSpeedVisibleProperty(symbol,event):
    if(event["value"] == 0x05):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Set Number of Transaction Request Block Visible Property
def seti2cmNumberTRBsVisibleProperty(symbol,event):
    if(event["value"] == 0x05):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#Receive Enable Visibility Property
def set_usart_RXEN_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Run in StabdBy Enable Visibility Property
def set_usart_RUNSTDBY_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Character Size Visibility Property
def set_usart_CHSIZE_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Stop Bit Mode Visibility Property
def set_usart_SBMODE_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Baud Rate Visibility Property
def set_usart_BAUD_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Baud API Visibility Property
def set_usart_BAUDAPI_EN_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Interrupt mode Visibility Property
def set_usart_MODE_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Parity mode visibility property
def set_usart_PMODE_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Receive Pinout Visibility Property
def set_usart_RXPO_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        print("RXPO True")
        symbol.setVisible(False)

#Transmit Pinout Visibility Property
def set_usart_TXPO_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Trasmit Enable Visibility Property
def set_usart_TXEN_VisibleProperty(symbol, event):
    if((event["value"] == 0x0) or (event["value"] == 0x1)):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#######################################################################################################################################
#####################################       Sercom Database Components      ##########################################################
#######################################################################################################################################

def instantiateComponent(sercomComponent):

    sercomInstanceIndex = sercomComponent.getID()[-1:]

    Log.writeInfoMessage("Running SERCOM" + str(sercomInstanceIndex))

    #SERCOM Main Menu
    sercomSym_Menu = sercomComponent.createMenuSymbol("SERCOM_MENU", None)
    sercomSym_Menu.setLabel("SERCOM MODULE SETTINGS ")

    #Sub Menu - Serial Communication Interfaces
    sercomSym_SubMenu = sercomComponent.createKeyValueSetSymbol("SERCOM_MODE", sercomSym_Menu)
    sercomSym_SubMenu.setLabel("SERCOM Modes")
    sercomSym_SubMenu_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_CTRLA__MODE\"]")
    sercomSym_SubMenu_Values = []
    sercomSym_SubMenu_Values = sercomSym_SubMenu_Node.getChildren()

    sercomSym_SubMenu_Default_Val = 0

    for index in range(len(sercomSym_SubMenu_Values)):
        sercomSym_SubMenu_Key_Name = sercomSym_SubMenu_Values[index].getAttribute("name")

        if(sercomSym_SubMenu_Key_Name == "SPIM"):
            sercomSym_SubMenu_Default_Val = index

        sercomSym_SubMenu_Key_Description = sercomSym_SubMenu_Values[index].getAttribute("caption")
        sercomSym_SubMenu_Key_Value = sercomSym_SubMenu_Values[index].getAttribute("value")
        sercomSym_SubMenu.addKey(sercomSym_SubMenu_Key_Name, sercomSym_SubMenu_Key_Value , sercomSym_SubMenu_Key_Description)

    sercomSym_SubMenu.setDefaultValue(sercomSym_SubMenu_Default_Val)
    sercomSym_SubMenu.setOutputMode("Key")
    sercomSym_SubMenu.setDisplayMode("Key")

    #SPI Interrupt Mode
    spiSym_INTERRUPTMODE = sercomComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", sercomSym_SubMenu)
    spiSym_INTERRUPTMODE.setLabel("Enable Interrupts? ")
    spiSym_INTERRUPTMODE.setDefaultValue(False)
    spiSym_INTERRUPTMODE.setDependencies(set_SPI_INTERRUPTMODE_VisibleProperty, ["SERCOM_MODE"])

    #SPI Standby Mode
    spiSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("SPI_STANDBY", sercomSym_SubMenu)
    spiSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
    spiSym_CTRLA_RUNSTDBY.setDependencies(setspiSTANDBYVisibleProperty, ["SERCOM_MODE"])

    #SPI DataOut PinOut
    spiSym_CTRLA_DOPO = sercomComponent.createKeyValueSetSymbol("SPI_DOPO", sercomSym_SubMenu)
    spiSym_CTRLA_DOPO.setLabel("SPI Data Out Pad ")
    #spiSym_CTRLA_DOPO.setVisible(False)

    spiDOPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DOPO\"]")
    spiDOPOValues = []
    spiDOPOValues = spiDOPONode.getChildren()
    spiDOPODefaultValue = 0
    for index in range(len(spiDOPOValues)):
        spiDOPOKeyName = spiDOPOValues[index].getAttribute("name")

        if (spiDOPOKeyName == "SERCOM_PAD0"):
            spiDOPODefaultValue = index

        spiDOPOKeyDescription = spiDOPOValues[index].getAttribute("caption")
        spiDOPOKeyValue = spiDOPOValues[index].getAttribute("value")
        spiSym_CTRLA_DOPO.addKey(spiDOPOKeyName, spiDOPOKeyValue , spiDOPOKeyDescription)

    spiSym_CTRLA_DOPO.setDefaultValue(spiDOPODefaultValue)
    spiSym_CTRLA_DOPO.setOutputMode("Value")
    spiSym_CTRLA_DOPO.setDisplayMode("Description")
    spiSym_CTRLA_DOPO.setDependencies(set_SPI_DOPO_VisibleProperty, ["SERCOM_MODE"])

    #SPI DataIn pinOut
    spiSym_CTRLA_DIPO = sercomComponent.createKeyValueSetSymbol("SPI_DIPO", sercomSym_SubMenu)
    spiSym_CTRLA_DIPO.setLabel("SPI Data In Pad Selection")
    spiDIPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DIPO\"]")
    spiDIPOValues = []
    spiDIPOValues = spiDIPONode.getChildren()
    spiDIPODefaultValue = 0
    for index in range(len(spiDIPOValues)):
        spiDIPOKeyName = spiDIPOValues[index].getAttribute("name")

        if (spiDIPOKeyName == "SERCOM_PAD0"):
            spiDIPODefaultValue = index

        spiDIPOKeyDescription = spiDIPOValues[index].getAttribute("caption")
        spiDIPOKeyValue = spiDIPOValues[index].getAttribute("value")
        spiSym_CTRLA_DIPO.addKey(spiDIPOKeyName, spiDIPOKeyValue , spiDIPOKeyDescription)

    spiSym_CTRLA_DIPO.setDefaultValue(spiDIPODefaultValue)
    spiSym_CTRLA_DIPO.setOutputMode("Value")
    spiSym_CTRLA_DIPO.setDisplayMode("Description")
    spiSym_CTRLA_DIPO.setDependencies(set_SPI_DIPO_VisibleProperty, ["SERCOM_MODE"])

    #SPI Transfer Mode
    spiSym_CTRLA_TRANSFER_MODE = sercomComponent.createKeyValueSetSymbol("SPI_TRANSFER_MODE", sercomSym_SubMenu)
    spiSym_CTRLA_TRANSFER_MODE.setLabel("SPI Transfer Mode")
    spiSym_CTRLA_TRANSFER_MODE.addKey("TRANSFER_MODE_1","0x00" ,"Data sampled on leading rising clock edge, changes on trailing falling clock edge")
    spiSym_CTRLA_TRANSFER_MODE.addKey("TRANSFER_MODE_2","0x10000000" ,"Data changes on leading leading clock edge, sampled on trailing falling clock edge")
    spiSym_CTRLA_TRANSFER_MODE.addKey("TRANSFER_MODE_3","0x20000000" ,"Data sampled on leading falling clock edge, changes on trailing rising clock edge")
    spiSym_CTRLA_TRANSFER_MODE.addKey("TRANSFER_MODE_4","0x30000000" ,"Data change on leading falling clock edge, sampled on trailing rising clock edge")

    spiSym_CTRLA_TRANSFER_MODE.setDefaultValue(0)
    spiSym_CTRLA_TRANSFER_MODE.setOutputMode("Value")
    spiSym_CTRLA_TRANSFER_MODE.setDisplayMode("Description")
    spiSym_CTRLA_TRANSFER_MODE.setDependencies(set_SPI_Transfer_Mode_VisibleProperty, ["SERCOM_MODE"])

    #SPI Data Order
    spiSym_CTRLA_DORD = sercomComponent.createKeyValueSetSymbol("SPI_DATA_ORDER", sercomSym_SubMenu)
    spiSym_CTRLA_DORD.setLabel("SPI Data Order")

    spiDORDNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DORD\"]")
    spiDORDValues = []
    spiDORDValues = spiDORDNode.getChildren()
    spiDORDDefaultValue = 0
    for index in range(len(spiDORDValues)):
        spiDORDKeyName = spiDORDValues[index].getAttribute("name")

        if (spiDORDKeyName == "MSB"):
            spiDORDDefaultValue = index

        spiDORDKeyDescription = spiDORDValues[index].getAttribute("caption")
        spiDORDKeyValue = spiDORDValues[index].getAttribute("value")
        spiSym_CTRLA_DORD.addKey(spiDORDKeyName, spiDORDKeyValue , spiDORDKeyDescription)

    spiSym_CTRLA_DORD.setDefaultValue(spiDORDDefaultValue)
    spiSym_CTRLA_DORD.setOutputMode("Key")
    spiSym_CTRLA_DORD.setDisplayMode("Description")
    spiSym_CTRLA_DORD.setDependencies(set_SPI_DORD_VisibleProperty, ["SERCOM_MODE"])

    #SPI Character Size
    spiSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("SPI_CHAR_SIZE", sercomSym_SubMenu)
    spiSym_CTRLB_CHSIZE.setLabel("SPI Data Character Size")
    spiCHSIZENode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLB__CHSIZE\"]")
    spiCHSIZEValues = []
    spiCHSIZEValues = spiCHSIZENode.getChildren()
    spiCHSIZEDefaultValue = 0
    for index in range(len(spiCHSIZEValues)):
        spiCHSIZEKeyName = spiCHSIZEValues[index].getAttribute("name")

        if (spiCHSIZEKeyName == "8BIT"):
            spiCHSIZEDefaultValue = index

        spiCHSIZEKeyDescription = spiCHSIZEValues[index].getAttribute("caption")
        spiCHSIZEKeyValue = spiCHSIZEValues[index].getAttribute("value")
        spiSym_CTRLB_CHSIZE.addKey(spiCHSIZEKeyName, spiCHSIZEKeyValue , spiCHSIZEKeyDescription)

    spiSym_CTRLB_CHSIZE.setDefaultValue(spiCHSIZEDefaultValue)
    spiSym_CTRLB_CHSIZE.setOutputMode("Value")
    spiSym_CTRLB_CHSIZE.setDisplayMode("Description")
    spiSym_CTRLB_CHSIZE.setDependencies(set_SPI_CHSIZE_VisibleProperty, ["SERCOM_MODE"])

    #SPI Hardware Slave Select control
    spiSym_CTRLB_MSSEN = sercomComponent.createBooleanSymbol("SPI_MSSEN", sercomSym_SubMenu)
    spiSym_CTRLB_MSSEN.setLabel("Enable SPI Master Hardware Slave Select")
    spiSym_CTRLB_MSSEN.setDefaultValue(False)
    spiSym_CTRLB_MSSEN.setDependencies(set_SPI_MASTER_SSEN_VisibleProperty, ["SERCOM_MODE"])

    #SPI Receiver Enable
    spiSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("SPI_RECIEVER_ENABLE", sercomSym_SubMenu)
    spiSym_CTRLB_RXEN.setLabel("SPI Receiver Enable")
    spiSym_CTRLB_RXEN.setDefaultValue(1)
    spiSym_CTRLB_RXEN.setVisible(False)

    #SPI BaudRate Value
    spi_BAUDRATE = sercomComponent.createIntegerSymbol("SPI_BAUDRATE", sercomSym_SubMenu)
    spi_BAUDRATE.setLabel("SPI Speed in Hz")
    spi_BAUDRATE.setDependencies(set_SPI_BAUDRATE_VisibleProperty, ["SERCOM_MODE"])

    #SPI Serial Setup API Enable
    spiSym_TRANSFERSETUP = sercomComponent.createBooleanSymbol("SPI_TRANSFERSETUP", sercomSym_SubMenu)
    spiSym_TRANSFERSETUP.setLabel("Generate Transfer Setup API ")

    spiSym_TRANSFERSETUP.setDefaultValue(True)
    spiSym_TRANSFERSETUP.setDependencies(set_SPI_SERIALSETUP_VisibleProperty, ["SERCOM_MODE"])

    # Number of Transaction request blocks
    i2cmSym_NumTRBs = sercomComponent.createIntegerSymbol("I2CM_NUM_TRBS", sercomSym_SubMenu)
    i2cmSym_NumTRBs.setLabel("Number of Transfer Request Blocks (TRBs)")
    i2cmSym_NumTRBs.setMax(255)
    i2cmSym_NumTRBs.setMin(2)
    i2cmSym_NumTRBs.setDefaultValue(2)
    i2cmSym_NumTRBs.setVisible(False)
    i2cmSym_NumTRBs.setDependencies(seti2cmNumberTRBsVisibleProperty,["SERCOM_MODE"])

    # RunIn Standby
    i2cmSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("RUN_IN_STANDBY", sercomSym_SubMenu)
    i2cmSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
    i2cmSym_CTRLA_RUNSTDBY.setVisible(False)
    i2cmSym_CTRLA_RUNSTDBY.setDependencies(seti2cmRunStandByVisibleProperty,["SERCOM_MODE"])

    # SDA Hold Time
    i2cmSym_CTRLA_SDAHOLD = sercomComponent.createKeyValueSetSymbol("SDAHOLD_TIME", sercomSym_SubMenu)
    i2cmSym_CTRLA_SDAHOLD.setLabel("SDA Hold Time")
    i2cmSym_CTRLA_SDAHOLD.setVisible(False)

    i2cmSDAHoldTimeReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_I2CM_CTRLA__SDAHOLD\"]")
    i2cmSDAHoldTimeReferenceValues = []
    i2cmSDAHoldTimeReferenceValues = i2cmSDAHoldTimeReferenceNode.getChildren()

    i2cmSDAHoldTimeReferenceDefaultValue = 0

    for index in range(len(i2cmSDAHoldTimeReferenceValues)):
        i2cmSDAHoldTimeReferenceKeyName = i2cmSDAHoldTimeReferenceValues[index].getAttribute("name")

        if (i2cmSDAHoldTimeReferenceKeyName == "DIS"):
            i2cmSDAHoldTimeReferenceDefaultValue = index

        i2cmSDAHoldTimeReferenceKeyDescription = i2cmSDAHoldTimeReferenceValues[index].getAttribute("caption")
        i2cmSDAHoldTimeReferenceKeyValue = i2cmSDAHoldTimeReferenceValues[index].getAttribute("value")
        i2cmSym_CTRLA_SDAHOLD.addKey(i2cmSDAHoldTimeReferenceKeyName , i2cmSDAHoldTimeReferenceKeyValue , i2cmSDAHoldTimeReferenceKeyDescription)

    i2cmSym_CTRLA_SDAHOLD.setDefaultValue(i2cmSDAHoldTimeReferenceDefaultValue)
    i2cmSym_CTRLA_SDAHOLD.setOutputMode("Value")
    i2cmSym_CTRLA_SDAHOLD.setDisplayMode("Description")
    i2cmSym_CTRLA_SDAHOLD.setDependencies(seti2cmSDAHoldTimeVisibleProperty,["SERCOM_MODE"])

    # Operating speed
    i2cmSym_BAUD = sercomComponent.createIntegerSymbol("I2C_SPEED", sercomSym_SubMenu)
    i2cmSym_BAUD.setLabel("I2C Speed in KHz")
    i2cmSym_BAUD.setMax(400)
    i2cmSym_BAUD.setMin(100)
    i2cmSym_BAUD.setDefaultValue(100)
    i2cmSym_BAUD.setVisible(False)
    i2cmSym_BAUD.setDependencies(seti2cmSpeedVisibleProperty,["SERCOM_MODE"])

    #Interrupt/Non-Interrupt Mode
    usart_Sym_MODE = sercomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", sercomSym_SubMenu)
    usart_Sym_MODE.setLabel("Interrupt Mode")
    usart_Sym_MODE.setVisible(False)
    usart_Sym_MODE.setDependencies(set_usart_MODE_VisibleProperty, ["SERCOM_MODE"])

    #Receive Enable
    usartSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("USART_RX_ENABLE", sercomSym_SubMenu)
    usartSym_CTRLB_RXEN.setLabel("Receive Enable")
    usartSym_CTRLB_RXEN.setVisible(False)
    usartSym_CTRLB_RXEN.setDependencies(set_usart_RXEN_VisibleProperty, ["SERCOM_MODE"])

    #Transmit Enable
    usartSym_CTRLB_TXEN = sercomComponent.createBooleanSymbol("USART_TX_ENABLE", sercomSym_SubMenu)
    usartSym_CTRLB_TXEN.setLabel("Transmit Enable")
    usartSym_CTRLB_TXEN.setVisible(False)
    usartSym_CTRLB_TXEN.setDependencies(set_usart_TXEN_VisibleProperty, ["SERCOM_MODE"])

    #Run in StandBy
    usartSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("USART_RUNSTDBY", sercomSym_SubMenu)
    usartSym_CTRLA_RUNSTDBY.setLabel("Enable Run in Standby")
    usartSym_CTRLA_RUNSTDBY.setVisible(False)
    usartSym_CTRLA_RUNSTDBY.setDependencies(set_usart_RUNSTDBY_VisibleProperty, ["SERCOM_MODE"])

    #RXPO - Receive Pin Out
    usart_Sym_CTRLA_RXPO = sercomComponent.createKeyValueSetSymbol("USART_RXPO", sercomSym_SubMenu)
    usart_Sym_CTRLA_RXPO.setLabel("Receive Pinout")

    usartSym_CTRLA_RXPO_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLA__RXPO\"]")
    usartSym_CTRLA_RXPO_Values = []
    usartSym_CTRLA_RXPO_Values = usartSym_CTRLA_RXPO_Node.getChildren()

    usartSym_CTRLA_RXPO_Default_Val = 0

    for index in range(len(usartSym_CTRLA_RXPO_Values)):
        usartSym_CTRLA_RXPO_Key_Name = usartSym_CTRLA_RXPO_Values[index].getAttribute("name")

        if(usartSym_CTRLA_RXPO_Key_Name == "SERCOM_PAD3"):
            usartSym_CTRLA_RXPO_Default_Val = index

        usartSym_CTRLA_RXPO_Key_Description = usartSym_CTRLA_RXPO_Values[index].getAttribute("caption")
        usartSym_CTRLA_RXPO_Key_Value = usartSym_CTRLA_RXPO_Values[index].getAttribute("value")
        usart_Sym_CTRLA_RXPO.addKey(usartSym_CTRLA_RXPO_Key_Name, usartSym_CTRLA_RXPO_Key_Value , usartSym_CTRLA_RXPO_Key_Description)

    usart_Sym_CTRLA_RXPO.setDefaultValue(usartSym_CTRLA_RXPO_Default_Val)
    usart_Sym_CTRLA_RXPO.setOutputMode("Key")
    usart_Sym_CTRLA_RXPO.setDisplayMode("Description")
    usart_Sym_CTRLA_RXPO.setVisible(False)
    usart_Sym_CTRLA_RXPO.setDependencies(set_usart_RXPO_VisibleProperty, ["SERCOM_MODE"])

    #TXPO - Transmit Pin Out
    usart_Sym_CTRLA_TXPO = sercomComponent.createKeyValueSetSymbol("USART_TXPO", sercomSym_SubMenu)
    usart_Sym_CTRLA_TXPO.setLabel("Transmit Pinout")

    usartSym_CTRLA_TXPO_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLA__TXPO\"]")
    usartSym_CTRLA_TXPO_Values = []
    usartSym_CTRLA_TXPO_Values = usartSym_CTRLA_TXPO_Node.getChildren()

    usartSym_CTRLA_TXPO_Default_Val = 0

    for index in range(len(usartSym_CTRLA_TXPO_Values)):
        usartSym_CTRLA_TXPO_Key_Name = usartSym_CTRLA_TXPO_Values[index].getAttribute("name")

        if (usartSym_CTRLA_TXPO_Key_Name == "SERCOM_PAD2"):
            usartSym_CTRLA_TXPO_Default_Val = index

        usartSym_CTRLA_TXPO_Key_Description = usartSym_CTRLA_TXPO_Values[index].getAttribute("caption")
        usartSym_CTRLA_TXPO_Key_Value = usartSym_CTRLA_TXPO_Values[index].getAttribute("value")
        usart_Sym_CTRLA_TXPO.addKey(usartSym_CTRLA_TXPO_Key_Name, usartSym_CTRLA_TXPO_Key_Value , usartSym_CTRLA_TXPO_Key_Description)

    usart_Sym_CTRLA_TXPO.setDefaultValue(usartSym_CTRLA_TXPO_Default_Val)
    usart_Sym_CTRLA_TXPO.setOutputMode("Key")
    usart_Sym_CTRLA_TXPO.setDisplayMode("Description")
    usart_Sym_CTRLA_TXPO.setVisible(False)
    usart_Sym_CTRLA_TXPO.setDependencies(set_usart_TXPO_VisibleProperty, ["SERCOM_MODE"])

    #PMODE : USART PARITY MODE
    usart_Sym_CTRLB_PMODE = sercomComponent.createKeyValueSetSymbol("USART_PMODE", sercomSym_SubMenu)
    usart_Sym_CTRLB_PMODE.setLabel("Parity Mode")

    usartSym_CTRLA_PMODE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLB__PMODE\"]")
    usartSym_CTRLA_PMODE_Values = []
    usartSym_CTRLA_PMODE_Values = usartSym_CTRLA_PMODE_Node.getChildren()

    usartSym_CTRLB_PMODE_Default_Val = 0

    for index in range(len(usartSym_CTRLA_PMODE_Values)):
        usartSym_CTRLB_PMODE_Key_Name = usartSym_CTRLA_PMODE_Values[index].getAttribute("name")

        if (usartSym_CTRLB_PMODE_Key_Name == "NONE"):
            usartSym_CTRLB_PMODE_Default_Val = index

        usartSym_CTRLB_PMODE_Key_Description = usartSym_CTRLA_PMODE_Values[index].getAttribute("caption")
        usartSym_CTRLB_PMODE_Key_Value = usartSym_CTRLA_PMODE_Values[index].getAttribute("value")
        usart_Sym_CTRLB_PMODE.addKey(usartSym_CTRLB_PMODE_Key_Name, usartSym_CTRLB_PMODE_Key_Value , usartSym_CTRLB_PMODE_Key_Description)

    usart_Sym_CTRLB_PMODE.setDefaultValue(usartSym_CTRLB_PMODE_Default_Val)
    usart_Sym_CTRLB_PMODE.setOutputMode("Key")
    usart_Sym_CTRLB_PMODE.setDisplayMode("Description")
    usart_Sym_CTRLB_PMODE.setVisible(False)
    usart_Sym_CTRLB_PMODE.setDependencies(set_usart_PMODE_VisibleProperty, ["SERCOM_MODE"])

    #Character Size
    usartSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("USART_CH_SIZE", sercomSym_SubMenu)
    usartSym_CTRLB_CHSIZE.setLabel("Character Size")

    usartSym_CTRLA_CHSIZE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLB__CHSIZE\"]")
    usartSym_CTRLA_CHSIZE_Values = []
    usartSym_CTRLA_CHSIZE_Values = usartSym_CTRLA_CHSIZE_Node.getChildren()

    usartSym_CTRLB_CHSIZE_Default_Val = 0

    for index in range(len(usartSym_CTRLA_CHSIZE_Values)):
        usartSym_CTRLB_CHSIZE_Key_Name = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("name")

        if (usartSym_CTRLB_CHSIZE_Key_Name == "8BITS"):
            usartSym_CTRLB_CHSIZE_Default_Val = index

        usartSym_CTRLB_CHSIZE_Key_Description = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("caption")
        usartSym_CTRLB_CHSIZE_Key_Value = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("value")
        usartSym_CTRLB_CHSIZE.addKey(usartSym_CTRLB_CHSIZE_Key_Name, usartSym_CTRLB_CHSIZE_Key_Value , usartSym_CTRLB_CHSIZE_Key_Description)

    usartSym_CTRLB_CHSIZE.setDefaultValue(usartSym_CTRLB_CHSIZE_Default_Val)
    usartSym_CTRLB_CHSIZE.setOutputMode("Key")
    usartSym_CTRLB_CHSIZE.setDisplayMode("Description")
    usartSym_CTRLB_CHSIZE.setVisible(False)
    usartSym_CTRLB_CHSIZE.setDependencies(set_usart_CHSIZE_VisibleProperty, ["SERCOM_MODE"])

    #Stop Bit
    usartSym_CTRLB_SBMODE = sercomComponent.createKeyValueSetSymbol("USART_SB", sercomSym_SubMenu)
    usartSym_CTRLB_SBMODE.setLabel("Stop Bit Mode")

    usartSym_CTRLB_SBMODE_Default_Val = 0

    usartSym_CTRLA_SBMODE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLB__SBMODE\"]")
    usartSym_CTRLA_SBMODE_Values = []
    usartSym_CTRLA_SBMODE_Values = usartSym_CTRLA_SBMODE_Node.getChildren()

    for index in range(len(usartSym_CTRLA_SBMODE_Values)):
        usartSym_CTRLB_SBMODE_Key_Name = usartSym_CTRLA_SBMODE_Values[index].getAttribute("name")

        if (usartSym_CTRLB_SBMODE_Key_Name == "1BIT"):
            usartSym_CTRLB_SBMODE_Default_Val = index

        usartSym_CTRLB_SBMODE_Key_Description = usartSym_CTRLA_SBMODE_Values[index].getAttribute("caption")
        usartSym_CTRLB_SBMODE_Key_Value = usartSym_CTRLA_SBMODE_Values[index].getAttribute("value")
        usartSym_CTRLB_SBMODE.addKey(usartSym_CTRLB_SBMODE_Key_Name, usartSym_CTRLB_SBMODE_Key_Value , usartSym_CTRLB_SBMODE_Key_Description)

    usartSym_CTRLB_SBMODE.setDefaultValue(usartSym_CTRLB_SBMODE_Default_Val)
    usartSym_CTRLB_SBMODE.setOutputMode("Key")
    usartSym_CTRLB_SBMODE.setDisplayMode("Description")
    usartSym_CTRLB_SBMODE.setVisible(False)
    usartSym_CTRLB_SBMODE.setDependencies(set_usart_SBMODE_VisibleProperty, ["SERCOM_MODE"])

    #Baud Rate API Enable
    usart_Sym_BAUDAPI_EN = sercomComponent.createBooleanSymbol("USART_BAUDAPI_EN", sercomSym_SubMenu)
    usart_Sym_BAUDAPI_EN.setDefaultValue(False)
    usart_Sym_BAUDAPI_EN.setLabel("Generate Serial Configuration API")
    usart_Sym_BAUDAPI_EN.setVisible(False)
    usart_Sym_BAUDAPI_EN.setDependencies(set_usart_BAUDAPI_EN_VisibleProperty, ["SERCOM_MODE"])

    #Baud Rate
    usart_Sym_BAUD = sercomComponent.createIntegerSymbol("USART_BAUD", sercomSym_SubMenu)
    usart_Sym_BAUD.setDefaultValue(int(9600))
    usart_Sym_BAUD.setLabel("Baud Rate")
    usart_Sym_BAUD.setVisible(False)
    usart_Sym_BAUD.setDependencies(set_usart_BAUD_VisibleProperty, ["SERCOM_MODE"])

    #SERCOM Instance Index
    sercomSym_INDEX = sercomComponent.createIntegerSymbol("SERCOM_INDEX", sercomSym_Menu)
    sercomSym_INDEX.setLabel("SERCOM_INDEX")
    sercomSym_INDEX.setVisible(False)
    sercomSym_INDEX.setDependencies(setSERCOMCodeGenerationProperty, ["SERCOM_MODE"])
    sercomSym_INDEX.setDefaultValue(int(sercomInstanceIndex))
    sercomSym_INDEXVal = (int(sercomInstanceIndex))

    #Peripheral Channel Index
    sercomSym_PHCTRL_INDEX = sercomComponent.createIntegerSymbol("SERCOM_PHCTRL_INDEX", sercomSym_Menu)
    sercomSym_PHCTRL_INDEX.setVisible(False)
    if(sercomSym_INDEXVal == 0):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(19))
    elif(sercomSym_INDEXVal == 1):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(20))
    elif(sercomSym_INDEXVal == 2):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(21))
    elif(sercomSym_INDEXVal == 3):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(22))
    elif(sercomSym_INDEXVal == 4):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(23))
    elif(sercomSym_INDEXVal == 5):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(25))
    elif(sercomSym_INDEXVal == 6):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(41))
    elif(sercomSym_INDEXVal == 7):
        sercomSym_PHCTRL_INDEX.setDefaultValue(int(42))

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sercomModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]")
    sercomModuleID = sercomModuleNode.getAttribute("id")

    spiSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIM_HEADER", None)
    spiSym_HeaderFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID + "/templates/plib_sercom_spi.h.ftl")
    spiSym_HeaderFile.setOutputName("plib_sercom"+ str(sercomInstanceIndex)+"_spi.h")
    spiSym_HeaderFile.setDestPath("peripheral/sercom/spim")
    spiSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_HeaderFile.setType("HEADER")
    spiSym_HeaderFile.setMarkup(True)

    spiSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIM_COMMON_HEADER", None)
    spiSym_Header1File.setSourcePath("../peripheral/sercom_" +  sercomModuleID + "/templates/plib_sercom_spi.h")
    spiSym_Header1File.setOutputName("plib_sercom_spi.h")
    spiSym_Header1File.setDestPath("peripheral/sercom/spim")
    spiSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_Header1File.setType("HEADER")
    spiSym_Header1File.setMarkup(True)

    spiSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIM_SOURCE", None)
    spiSym_SourceFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID + "/templates/plib_sercom_spi.c.ftl")
    spiSym_SourceFile.setOutputName("plib_sercom"+ str(sercomInstanceIndex)+"_spi.c")
    spiSym_SourceFile.setDestPath("peripheral/sercom/spim")
    spiSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi/")
    spiSym_SourceFile.setType("SOURCE")
    spiSym_SourceFile.setMarkup(True)

    i2cmMasterHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_MASTER_HEADER", None)
    i2cmMasterHeaderFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID + "/templates/plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setOutputName("plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setDestPath("/peripheral/sercom/i2cm")
    i2cmMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmMasterHeaderFile.setType("HEADER")
    i2cmMasterHeaderFile.setMarkup(True)
    i2cmMasterHeaderFile.setEnabled(False)

    i2cmHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_HEADER", None)
    i2cmHeaderFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID + "/templates/plib_sercom_i2c.h.ftl")
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

    usartHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.h.ftl")
    usartHeaderFile.setOutputName("plib_sercom"+ sercomInstanceIndex + "_usart" + ".h")
    usartHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setMarkup(True)
    usartHeaderFile.setEnabled(False)

    usartCommonHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_COMMON_HEADER", None)
    usartCommonHeaderFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.h")
    usartCommonHeaderFile.setOutputName("plib_sercom_usart.h")
    usartCommonHeaderFile.setDestPath("peripheral/sercom/usart/")
    usartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart")
    usartCommonHeaderFile.setType("HEADER")
    usartCommonHeaderFile.setMarkup(True)
    usartCommonHeaderFile.setEnabled(False)

    usartSourceFile = sercomComponent.createFileSymbol("SERCOM_USART_SOURCE", None)
    usartSourceFile.setSourcePath("../peripheral/sercom_" + sercomModuleID + "/templates/plib_sercom_usart.c.ftl")
    usartSourceFile.setOutputName("plib_sercom"+ sercomInstanceIndex + "_usart" + ".c")
    usartSourceFile.setDestPath("/peripheral/sercom/usart/")
    usartSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartSourceFile.setType("SOURCE")
    usartSourceFile.setMarkup(True)
    usartSourceFile.setEnabled(False)

    sercomSystemInitFile = sercomComponent.createFileSymbol("SERCOM_SYS_INIT", None)
    sercomSystemInitFile.setType("STRING")
    sercomSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sercomSystemInitFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID +  "/templates/system/initialization.c.ftl")
    sercomSystemInitFile.setMarkup(True)

    sercomSystemDefFile = sercomComponent.createFileSymbol("SERCOM_SYS_DEF", None)
    sercomSystemDefFile.setType("STRING")
    sercomSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sercomSystemDefFile.setSourcePath("../peripheral/sercom_" +  sercomModuleID +  "/templates/system/definitions.h.ftl")
    sercomSystemDefFile.setMarkup(True)
