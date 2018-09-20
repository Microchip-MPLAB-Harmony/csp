###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

#Receive Enable Visibility Property
def set_usart_RXEN_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Run in StabdBy Enable Visibility Property
def set_usart_RUNSTDBY_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Character Size Visibility Property
def set_usart_CHSIZE_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Stop Bit Mode Visibility Property
def set_usart_SBMODE_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Baud Rate Visibility Property
def set_usart_BAUD_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Baud API Visibility Property
def set_usart_BAUDAPI_EN_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Interrupt mode Visibility Property
def set_usart_MODE_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Parity mode visibility property
def set_usart_PMODE_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Receive Pinout Visibility Property
def set_usart_RXPO_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Transmit Pinout Visibility Property
def set_usart_TXPO_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#Trasmit Enable Visibility Property
def set_usart_TXEN_VisibleProperty(symbol, event):
    if event["value"] == 0x1:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

###################################################################################################
############################################ USART ################################################
###################################################################################################

global usartSym_Interrupt_Mode

#Interrupt/Non-Interrupt Mode
usartSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", sercomSym_OperationMode)
usartSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
usartSym_Interrupt_Mode.setDefaultValue(True)
usartSym_Interrupt_Mode.setDependencies(set_usart_MODE_VisibleProperty, ["SERCOM_MODE"])

#Receive Enable
usartSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("USART_RX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_RXEN.setLabel("Receive Enable")
usartSym_CTRLB_RXEN.setDefaultValue(True)
usartSym_CTRLB_RXEN.setDependencies(set_usart_RXEN_VisibleProperty, ["SERCOM_MODE"])

#Transmit Enable
usartSym_CTRLB_TXEN = sercomComponent.createBooleanSymbol("USART_TX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_TXEN.setLabel("Transmit Enable")
usartSym_CTRLB_TXEN.setDefaultValue(True)
usartSym_CTRLB_TXEN.setDependencies(set_usart_TXEN_VisibleProperty, ["SERCOM_MODE"])

#Run in StandBy
usartSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("USART_RUNSTDBY", sercomSym_OperationMode)
usartSym_CTRLA_RUNSTDBY.setLabel("Enable Run in Standby")
usartSym_CTRLA_RUNSTDBY.setDependencies(set_usart_RUNSTDBY_VisibleProperty, ["SERCOM_MODE"])

#RXPO - Receive Pin Out
usartSym_CTRLA_RXPO = sercomComponent.createKeyValueSetSymbol("USART_RXPO", sercomSym_OperationMode)
usartSym_CTRLA_RXPO.setLabel("Receive Pinout")

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
    usartSym_CTRLA_RXPO.addKey(usartSym_CTRLA_RXPO_Key_Name, usartSym_CTRLA_RXPO_Key_Value, usartSym_CTRLA_RXPO_Key_Description)

usartSym_CTRLA_RXPO.setDefaultValue(usartSym_CTRLA_RXPO_Default_Val)
usartSym_CTRLA_RXPO.setOutputMode("Key")
usartSym_CTRLA_RXPO.setDisplayMode("Description")
usartSym_CTRLA_RXPO.setDependencies(set_usart_RXPO_VisibleProperty, ["SERCOM_MODE"])

#TXPO - Transmit Pin Out
usartSym_CTRLA_TXPO = sercomComponent.createKeyValueSetSymbol("USART_TXPO", sercomSym_OperationMode)
usartSym_CTRLA_TXPO.setLabel("Transmit Pinout")

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
    usartSym_CTRLA_TXPO.addKey(usartSym_CTRLA_TXPO_Key_Name, usartSym_CTRLA_TXPO_Key_Value, usartSym_CTRLA_TXPO_Key_Description)

usartSym_CTRLA_TXPO.setDefaultValue(usartSym_CTRLA_TXPO_Default_Val)
usartSym_CTRLA_TXPO.setOutputMode("Key")
usartSym_CTRLA_TXPO.setDisplayMode("Description")
usartSym_CTRLA_TXPO.setDependencies(set_usart_TXPO_VisibleProperty, ["SERCOM_MODE"])

#PMODE : USART PARITY MODE
usartSym_CTRLB_PMODE = sercomComponent.createKeyValueSetSymbol("USART_PARITY_MODE", sercomSym_OperationMode)
usartSym_CTRLB_PMODE.setLabel("Parity Mode")

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
    usartSym_CTRLB_PMODE.addKey(usartSym_CTRLB_PMODE_Key_Name, usartSym_CTRLB_PMODE_Key_Value, usartSym_CTRLB_PMODE_Key_Description)

usartSym_CTRLB_PMODE.setDefaultValue(usartSym_CTRLB_PMODE_Default_Val)
usartSym_CTRLB_PMODE.setOutputMode("Key")
usartSym_CTRLB_PMODE.setDisplayMode("Description")
usartSym_CTRLB_PMODE.setDependencies(set_usart_PMODE_VisibleProperty, ["SERCOM_MODE"])

#USART EVEN Parity Mask
usartSym_CTRLA_PMODE_EVEN_Mask = sercomComponent.createStringSymbol("USART_PARITY_EVEN_MASK", sercomSym_OperationMode)
usartSym_CTRLA_PMODE_EVEN_Mask.setDefaultValue("0x0")
usartSym_CTRLA_PMODE_EVEN_Mask.setVisible(False)

#USART ODD Parity Mask
usartSym_CTRLA_PMODE_ODD_Mask = sercomComponent.createStringSymbol("USART_PARITY_ODD_MASK", sercomSym_OperationMode)
usartSym_CTRLA_PMODE_ODD_Mask.setDefaultValue("0x80000")
usartSym_CTRLA_PMODE_ODD_Mask.setVisible(False)

#Character Size
usartSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("USART_CHARSIZE_BITS", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE.setLabel("Character Size")

usartSym_CTRLA_CHSIZE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLB__CHSIZE\"]")
usartSym_CTRLA_CHSIZE_Values = []
usartSym_CTRLA_CHSIZE_Values = usartSym_CTRLA_CHSIZE_Node.getChildren()

for index in range(len(usartSym_CTRLA_CHSIZE_Values)):
    usartSym_CTRLB_CHSIZE_Key_Name = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("name")
    usartSym_CTRLB_CHSIZE_Key_Description = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("caption")
    usartSym_CTRLB_CHSIZE_Key_Value = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("value")
    usartSym_CTRLB_CHSIZE.addKey(usartSym_CTRLB_CHSIZE_Key_Name, usartSym_CTRLB_CHSIZE_Key_Value, usartSym_CTRLB_CHSIZE_Key_Description)

usartSym_CTRLB_CHSIZE.setDefaultValue(0)
usartSym_CTRLB_CHSIZE.setOutputMode("Key")
usartSym_CTRLB_CHSIZE.setDisplayMode("Description")
usartSym_CTRLB_CHSIZE.setDependencies(set_usart_CHSIZE_VisibleProperty, ["SERCOM_MODE"])

#USART Character Size 5 Mask
usartSym_CTRLB_CHSIZE_5_Mask = sercomComponent.createStringSymbol("USART_DATA_5_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE_5_Mask.setDefaultValue("0x5")
usartSym_CTRLB_CHSIZE_5_Mask.setVisible(False)

#USART Character Size 6 Mask
usartSym_CTRLB_CHSIZE_6_Mask = sercomComponent.createStringSymbol("USART_DATA_6_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE_6_Mask.setDefaultValue("0x6")
usartSym_CTRLB_CHSIZE_6_Mask.setVisible(False)

#USART Character Size 7 Mask
usartSym_CTRLB_CHSIZE_7_Mask = sercomComponent.createStringSymbol("USART_DATA_7_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE_7_Mask.setDefaultValue("0x7")
usartSym_CTRLB_CHSIZE_7_Mask.setVisible(False)

#USART Character Size 8 Mask
usartSym_CTRLB_CHSIZE_8_Mask = sercomComponent.createStringSymbol("USART_DATA_8_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE_8_Mask.setDefaultValue("0x0")
usartSym_CTRLB_CHSIZE_8_Mask.setVisible(False)

#USART Character Size 9 Mask
usartSym_CTRLB_CHSIZE_9_Mask = sercomComponent.createStringSymbol("USART_DATA_9_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE_9_Mask.setDefaultValue("0x1")
usartSym_CTRLB_CHSIZE_9_Mask.setVisible(False)

#Stop Bit
usartSym_CTRLB_SBMODE = sercomComponent.createKeyValueSetSymbol("USART_STOP_BIT", sercomSym_OperationMode)
usartSym_CTRLB_SBMODE.setLabel("Stop Bit Mode")

usartSym_CTRLA_SBMODE_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLB__SBMODE\"]")
usartSym_CTRLA_SBMODE_Values = []
usartSym_CTRLA_SBMODE_Values = usartSym_CTRLA_SBMODE_Node.getChildren()

for index in range(len(usartSym_CTRLA_SBMODE_Values)):
    usartSym_CTRLB_SBMODE_Key_Name = usartSym_CTRLA_SBMODE_Values[index].getAttribute("name")
    usartSym_CTRLB_SBMODE_Key_Description = usartSym_CTRLA_SBMODE_Values[index].getAttribute("caption")
    usartSym_CTRLB_SBMODE_Key_Value = usartSym_CTRLA_SBMODE_Values[index].getAttribute("value")
    usartSym_CTRLB_SBMODE.addKey(usartSym_CTRLB_SBMODE_Key_Name, usartSym_CTRLB_SBMODE_Key_Value, usartSym_CTRLB_SBMODE_Key_Description)

usartSym_CTRLB_SBMODE.setDefaultValue(0)
usartSym_CTRLB_SBMODE.setOutputMode("Key")
usartSym_CTRLB_SBMODE.setDisplayMode("Description")
usartSym_CTRLB_SBMODE.setDependencies(set_usart_SBMODE_VisibleProperty, ["SERCOM_MODE"])

#USART Stop 1-bit Mask
usartSym_CTRLB_SBMODE_1_Mask = sercomComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
usartSym_CTRLB_SBMODE_1_Mask.setDefaultValue("0x0")
usartSym_CTRLB_SBMODE_1_Mask.setVisible(False)

#USART Stop 2-bit Mask
usartSym_CTRLB_SBMODE_2_Mask = sercomComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
usartSym_CTRLB_SBMODE_2_Mask.setDefaultValue("0x40")
usartSym_CTRLB_SBMODE_2_Mask.setVisible(False)

#Baud Rate
usartSym_BAUD_RATE = sercomComponent.createIntegerSymbol("USART_BAUD_RATE", sercomSym_OperationMode)
usartSym_BAUD_RATE.setDefaultValue(9600)
usartSym_BAUD_RATE.setLabel("Baud Rate")
usartSym_BAUD_RATE.setDependencies(set_usart_BAUD_VisibleProperty, ["SERCOM_MODE"])

#Serial Setup API Enable
usartSym_SerialSetup_EN = sercomComponent.createBooleanSymbol("USART_SERIAL_SETUP_ENABLE", sercomSym_OperationMode)
usartSym_SerialSetup_EN.setLabel("Generate Serial Configuration API")
usartSym_SerialSetup_EN.setDefaultValue(True)
usartSym_SerialSetup_EN.setDependencies(set_usart_BAUDAPI_EN_VisibleProperty, ["SERCOM_MODE"])

#USART API Prefix
usartSym_API_Prefix = sercomComponent.createStringSymbol("USART_PLIB_API_PREFIX", sercomSym_OperationMode)
usartSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_USART")
usartSym_API_Prefix.setVisible(False)
