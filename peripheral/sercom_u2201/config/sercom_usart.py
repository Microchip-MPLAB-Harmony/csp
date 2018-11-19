# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateUSARTConfigurationVisibleProperty(symbol, event):

    if symbol.getID() == "USART_BAUD_ERROR_COMMENT":
        if usartSym_BAUD_VALUE.getValue() == 0 and event["symbol"].getSelectedKey() == "USART_INT":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        if event["symbol"].getSelectedKey() == "USART_INT":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def updateUSARTBaudValueProperty(symbol, event):

    brgVal = 0

    clk = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "SERCOM_CLOCK_FREQUENCY"))
    baud = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_BAUD_RATE"))

    if clk != 0 and baud != 0:
        brgVal = getUSARTBaudValue(clk, baud)

    if brgVal < 1 and sercomSym_OperationMode.getSelectedKey() == "USART_INT":
        usartSym_BaudError_Comment.setVisible(True)
    else:
        usartSym_BaudError_Comment.setVisible(False)

    symbol.setValue(brgVal, 2)

###################################################################################################
############################################ USART ################################################
###################################################################################################

global usartSym_Interrupt_Mode

#Interrupt/Non-Interrupt Mode
usartSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", sercomSym_OperationMode)
usartSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
usartSym_Interrupt_Mode.setDefaultValue(True)
usartSym_Interrupt_Mode.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#Receive Enable
usartSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("USART_RX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_RXEN.setLabel("Receive Enable")
usartSym_CTRLB_RXEN.setDefaultValue(True)
usartSym_CTRLB_RXEN.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#Transmit Enable
usartSym_CTRLB_TXEN = sercomComponent.createBooleanSymbol("USART_TX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_TXEN.setLabel("Transmit Enable")
usartSym_CTRLB_TXEN.setDefaultValue(True)
usartSym_CTRLB_TXEN.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#Run in StandBy
usartSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("USART_RUNSTDBY", sercomSym_OperationMode)
usartSym_CTRLA_RUNSTDBY.setLabel("Enable Run in Standby")
usartSym_CTRLA_RUNSTDBY.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#RXPO - Receive Pin Out
usartSym_CTRLA_RXPO = sercomComponent.createKeyValueSetSymbol("USART_RXPO", sercomSym_OperationMode)
usartSym_CTRLA_RXPO.setLabel("Receive Pinout")

usartSym_CTRLA_RXPO_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLA__RXPO\"]")
usartSym_CTRLA_RXPO_Values = []
usartSym_CTRLA_RXPO_Values = usartSym_CTRLA_RXPO_Node.getChildren()

for index in range(len(usartSym_CTRLA_RXPO_Values)):
    usartSym_CTRLA_RXPO_Key_Name = usartSym_CTRLA_RXPO_Values[index].getAttribute("name")
    usartSym_CTRLA_RXPO_Key_Description = usartSym_CTRLA_RXPO_Values[index].getAttribute("caption")
    usartSym_CTRLA_RXPO_Key_Value = usartSym_CTRLA_RXPO_Values[index].getAttribute("value")
    usartSym_CTRLA_RXPO.addKey(usartSym_CTRLA_RXPO_Key_Name, usartSym_CTRLA_RXPO_Key_Value, usartSym_CTRLA_RXPO_Key_Description)

usartSym_CTRLA_RXPO.setDefaultValue(0)
usartSym_CTRLA_RXPO.setOutputMode("Key")
usartSym_CTRLA_RXPO.setDisplayMode("Description")
usartSym_CTRLA_RXPO.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#TXPO - Transmit Pin Out
usartSym_CTRLA_TXPO = sercomComponent.createKeyValueSetSymbol("USART_TXPO", sercomSym_OperationMode)
usartSym_CTRLA_TXPO.setLabel("Transmit Pinout")

usartSym_CTRLA_TXPO_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_USART_CTRLA__TXPO\"]")
usartSym_CTRLA_TXPO_Values = []
usartSym_CTRLA_TXPO_Values = usartSym_CTRLA_TXPO_Node.getChildren()

for index in range(len(usartSym_CTRLA_TXPO_Values)):
    usartSym_CTRLA_TXPO_Key_Name = usartSym_CTRLA_TXPO_Values[index].getAttribute("name")
    usartSym_CTRLA_TXPO_Key_Description = usartSym_CTRLA_TXPO_Values[index].getAttribute("caption")
    usartSym_CTRLA_TXPO_Key_Value = usartSym_CTRLA_TXPO_Values[index].getAttribute("value")
    usartSym_CTRLA_TXPO.addKey(usartSym_CTRLA_TXPO_Key_Name, usartSym_CTRLA_TXPO_Key_Value, usartSym_CTRLA_TXPO_Key_Description)

usartSym_CTRLA_TXPO.setDefaultValue(0)
usartSym_CTRLA_TXPO.setOutputMode("Key")
usartSym_CTRLA_TXPO.setDisplayMode("Description")
usartSym_CTRLA_TXPO.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#PMODE : USART PARITY MODE
usartSym_CTRLB_PMODE = sercomComponent.createKeyValueSetSymbol("USART_PARITY_MODE", sercomSym_OperationMode)
usartSym_CTRLB_PMODE.setLabel("Parity Mode")
usartSym_CTRLB_PMODE.addKey("EVEN", "0x0", "Even Parity")
usartSym_CTRLB_PMODE.addKey("ODD", "0x1", "Odd Parity")
usartSym_CTRLB_PMODE.addKey("NONE", "0x2", "No Parity")
usartSym_CTRLB_PMODE.setDefaultValue(2)
usartSym_CTRLB_PMODE.setOutputMode("Key")
usartSym_CTRLB_PMODE.setDisplayMode("Description")
usartSym_CTRLB_PMODE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART EVEN Parity Mask
usartSym_CTRLA_PMODE_EVEN_Mask = sercomComponent.createStringSymbol("USART_PARITY_EVEN_MASK", sercomSym_OperationMode)
usartSym_CTRLA_PMODE_EVEN_Mask.setDefaultValue("0x0")
usartSym_CTRLA_PMODE_EVEN_Mask.setVisible(False)

#USART ODD Parity Mask
usartSym_CTRLA_PMODE_ODD_Mask = sercomComponent.createStringSymbol("USART_PARITY_ODD_MASK", sercomSym_OperationMode)
usartSym_CTRLA_PMODE_ODD_Mask.setDefaultValue("0x80000")
usartSym_CTRLA_PMODE_ODD_Mask.setVisible(False)

#USART NONE Parity Mask
usartSym_Parity_NONE_Mask = sercomComponent.createStringSymbol("USART_PARITY_NONE_MASK", sercomSym_OperationMode)
usartSym_Parity_NONE_Mask.setDefaultValue("0x2")
usartSym_Parity_NONE_Mask.setVisible(False)

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
usartSym_CTRLB_CHSIZE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

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
usartSym_CTRLB_SBMODE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART Stop 1-bit Mask
usartSym_CTRLB_SBMODE_1_Mask = sercomComponent.createStringSymbol("USART_STOP_1_BIT_MASK", None)
usartSym_CTRLB_SBMODE_1_Mask.setDefaultValue("0x0")
usartSym_CTRLB_SBMODE_1_Mask.setVisible(False)

#USART Stop 2-bit Mask
usartSym_CTRLB_SBMODE_2_Mask = sercomComponent.createStringSymbol("USART_STOP_2_BIT_MASK", None)
usartSym_CTRLB_SBMODE_2_Mask.setDefaultValue("0x40")
usartSym_CTRLB_SBMODE_2_Mask.setVisible(False)

#USART Over-Sampling using Baud Rate generation
global usartSym_CTRLA_SAMPR
usartSym_CTRLA_SAMPR = sercomComponent.createIntegerSymbol("USART_SAMPLE_RATE", sercomSym_OperationMode)
usartSym_CTRLA_SAMPR.setLabel("Sample Rate")
usartSym_CTRLA_SAMPR.setDefaultValue(0)
usartSym_CTRLA_SAMPR.setVisible(False)

#USART No Of Samples
global usartSym_SAMPLE_COUNT
usartSym_SAMPLE_COUNT = sercomComponent.createIntegerSymbol("USART_SAMPLE_COUNT", sercomSym_OperationMode)
usartSym_SAMPLE_COUNT.setLabel("No Of Samples")
usartSym_SAMPLE_COUNT.setDefaultValue(16)
usartSym_SAMPLE_COUNT.setVisible(False)

#USART Baud Rate
usartSym_BAUD_RATE = sercomComponent.createIntegerSymbol("USART_BAUD_RATE", sercomSym_OperationMode)
usartSym_BAUD_RATE.setLabel("Baud Rate in Hz")
usartSym_BAUD_RATE.setDefaultValue(115200)
usartSym_BAUD_RATE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART Baud Value
global usartSym_BAUD_VALUE
usartSym_BAUD_VALUE = sercomComponent.createIntegerSymbol("USART_BAUD_VALUE", sercomSym_OperationMode)
usartSym_BAUD_VALUE.setDefaultValue(getUSARTBaudValue(sercomSym_ClockFrequency.getValue(), usartSym_BAUD_RATE.getValue()))
usartSym_BAUD_VALUE.setLabel("Baud Rate Value")
usartSym_BAUD_VALUE.setVisible(False)
usartSym_BAUD_VALUE.setDependencies(updateUSARTBaudValueProperty, ["USART_BAUD_RATE", "SERCOM_CLOCK_FREQUENCY"])

#USART Baud Rate not supported comment
global usartSym_BaudError_Comment
usartSym_BaudError_Comment = sercomComponent.createCommentSymbol("USART_BAUD_ERROR_COMMENT", sercomSym_OperationMode)
usartSym_BaudError_Comment.setLabel("********** USART Clock source value is low for the desired baud rate **********")
usartSym_BaudError_Comment.setVisible(False)
usartSym_BaudError_Comment.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART API Prefix
usartSym_API_Prefix = sercomComponent.createStringSymbol("USART_PLIB_API_PREFIX", sercomSym_OperationMode)
usartSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_USART")
usartSym_API_Prefix.setVisible(False)

#USART Overrun error Mask
sercomSym_STATUS_BUFOVF_Mask = sercomComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", None)
sercomSym_STATUS_BUFOVF_Mask.setDefaultValue("0x4")
sercomSym_STATUS_BUFOVF_Mask.setVisible(False)

#USART parity error Mask
sercomSym_STATUS_PERR_Mask = sercomComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", None)
sercomSym_STATUS_PERR_Mask.setDefaultValue("0x0")
sercomSym_STATUS_PERR_Mask.setVisible(False)

#USART framing error Mask
sercomSym_STATUS_FERR_Mask = sercomComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", None)
sercomSym_STATUS_FERR_Mask.setDefaultValue("0x2")
sercomSym_STATUS_FERR_Mask.setVisible(False)