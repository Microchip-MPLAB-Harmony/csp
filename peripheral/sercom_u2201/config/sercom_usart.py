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
###################################### BAUD Calculation ###########################################
###################################################################################################

global getUSARTBaudValue
global getValueGrp

global sort_alphanumeric

global dataBitsDict


dataBitsDict = dict()

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def getUSARTBaudValue():

    global desiredUSARTBaudRate
    global usartSym_CTRLA_FORM

    baudValue = 0
    sampleCount = 0
    sampleRate = 0
    desiredUSARTBaudRate = True

    refClkFreq = int(Database.getSymbolValue("core", sercomClkFrequencyId))
    baudRate = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_BAUD_RATE"))
    frameFormat = usartSym_CTRLA_FORM.getSelectedKey()
    useFractionalBaud = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_USE_FRACTIONAL_BAUD")

    if refClkFreq == 0:
        desiredUSARTBaudRate = False
        usartSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
        return baudValue

    if useFractionalBaud == False:
        if sampleRateSupported == True:
            # find S (Number of samples per bit)
            if refClkFreq >= (16 * baudRate):
                sampleRate = 0
                sampleCount = 16
            elif refClkFreq >= (8 * baudRate):
                sampleRate = 2
                sampleCount = 8
            elif refClkFreq >= (3 * baudRate):
                sampleRate = 4
                sampleCount = 3
            else:
                desiredUSARTBaudRate = False
        else:
            if refClkFreq >= (16 * baudRate):
                sampleCount = 16
            else:
                desiredUSARTBaudRate = False
    else:
        if frameFormat == "USART_FRAME_LIN_MASTER_MODE" or frameFormat == "USART_FRAME_AUTO_BAUD_NO_PARITY" or frameFormat == "USART_FRAME_AUTO_BAUD_WITH_PARITY":
            if refClkFreq >= (16 * baudRate):
                sampleRate = 1
                sampleCount = 16
            else:
                desiredUSARTBaudRate = False
        else:
            if refClkFreq >= (16 * baudRate):
                sampleRate = 1
                sampleCount = 16
            elif refClkFreq >= (8 * baudRate):
                sampleRate = 3
                sampleCount = 8
            else:
                desiredUSARTBaudRate = False

    if desiredUSARTBaudRate == True:
        if useFractionalBaud == True:
            #fractional formula
            baudValue = float(refClkFreq)/(float(sampleCount) * baudRate)
            fp = int((float(baudValue) - int(baudValue)) * 8.0)
            baudValue = int(baudValue)
            if (baudValue == 0) or (baudValue >= 8192):
                desiredUSARTBaudRate = False
                usartSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
            else:
                baudValue |= (fp << 13)
        else:
            #arithmetic formula
            baudValue = int(65536 * (1 - float("{0:.15f}".format(float(sampleCount * baudRate) / refClkFreq))))
        if sampleRateSupported == True:
            usartSym_CTRLA_SAMPR.setValue(sampleRate, 1)
            usartSym_SAMPLE_COUNT.setValue(sampleCount, 1)
    else:
        usartSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

    return baudValue

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateRingBufferSizeVisibleProperty(symbol, event):
    global usartSym_CTRLB_RXEN
    global usartSym_CTRLB_TXEN
    global usartSym_RingBuffer_Mode

    # Enable RX ring buffer size option if Ring buffer is enabled and RX is enabled.
    if symbol.getID() == "USART_RX_RING_BUFFER_SIZE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and usartSym_CTRLB_RXEN.getValue() == True and usartSym_RingBuffer_Mode.getValue() == True)
    # Enable TX ring buffer size option if Ring buffer is enabled and TX is enabled.
    elif symbol.getID() == "USART_TX_RING_BUFFER_SIZE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and usartSym_CTRLB_TXEN.getValue() == True and usartSym_RingBuffer_Mode.getValue() == True)

def updateUSARTConfigurationVisibleProperty(symbol, event):

    global desiredUSARTBaudRate

    if symbol.getID() == "USART_BAUD_ERROR_COMMENT":
        symbol.setVisible(desiredUSARTBaudRate == False and sercomSym_OperationMode.getSelectedKey() == "USART_INT")
    else:
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

    if event["id"] == "USART_7816_CLOCK_OUTPUT":
        event['source'].getSymbolByID("USART_BAUD_RATE").setValue(event['source'].getSymbolByID("USART_7816_CLOCK_OUTPUT").getValue()/372)
    elif event["id"] == "USART_FORM":
        usart_form = event['source'].getSymbolByID("USART_FORM").getSelectedKey()
        if usart_form == "USART_FRAME_ISO_7816" or usart_form == "ISO7816" :
            event['source'].getSymbolByID("USART_BAUD_RATE").setValue(event['source'].getSymbolByID("USART_7816_CLOCK_OUTPUT").getValue()/372)
            event['source'].getSymbolByID("USART_PARITY_MODE").setValue(0)
            event['source'].getSymbolByID("USART_BAUD_ERROR_COMMENT").setVisible(0)
        else:
            event['source'].getSymbolByID("USART_BAUD_RATE").clearValue()
            event['source'].getSymbolByID("USART_PARITY_MODE").clearValue()
            event['source'].getSymbolByID("USART_BAUD_ERROR_COMMENT").setVisible(desiredUSARTBaudRate == False and sercomSym_OperationMode.getSelectedKey() == "USART_INT")

    if event["id"] == "SERCOM_MODE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

def updateUSARTBaudValueProperty(symbol, event):

    symbol.setValue(getUSARTBaudValue(), 1)

def updateUSART7816BaudValueProperty(symbol, event):

    baudRate = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_BAUD_RATE"))
    Refclock = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_7816_CLOCK_OUTPUT"))
    baudvalue = int((Refclock/(2*baudRate)) - 1)
    event['source'].getSymbolByID("USART_7816_BAUD_VALUE").setValue(baudvalue)

def updateUSARTRS485GuardTimeValueProperty(symbol, event):

    usart_frame_format = event['source'].getSymbolByID("USART_FORM").getSelectedKey()

    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and usartSym_CTRLA_TXPO.getSelectedValue() == "0x3" and (usart_frame_format == "USART_FRAME_NO_PARITY" or usart_frame_format == "USART_FRAME_WITH_PARITY"))

def updateSMARTCARDPinProperty(symbol, event):

    if event["id"] == "USART_FORM":
        symbol.setVisible(event['source'].getSymbolByID("USART_FORM").getSelectedKey() == "USART_FRAME_ISO_7816" or event['source'].getSymbolByID("USART_FORM").getSelectedKey() == "ISO7816")

    if event["id"] == "SERCOM_MODE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and (usartSym_CTRLA_FORM.getSelectedKey() == "USART_FRAME_ISO_7816" or usartSym_CTRLA_FORM.getSelectedKey() == "ISO7816"))

def updateUSARTFORMValueProperty(symbol, event):

    if symbol.getID() == "USART_FORM":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

    if event["id"] == "USART_PARITY_MODE":

        if event['source'].getSymbolByID("USART_PARITY_MODE").getSelectedKey() == "NONE":
            if symbol.getValue() == 1:
                symbol.setReadOnly(True)
                symbol.setValue(0)
                symbol.setReadOnly(False)
        else:
            if symbol.getValue() == 0:
                symbol.setReadOnly(True)
                symbol.setValue(1)
                symbol.setReadOnly(False)

    if event["id"] == "USART_FORM":
            usart_form = event['source'].getSymbolByID("USART_FORM").getSelectedKey()
            usartOperatingModeSym = event["source"].getSymbolByID("USART_OPERATING_MODE")

            if usart_form == "USART_FRAME_AUTO_BAUD_NO_PARITY":
                usartOperatingModeSym.setReadOnly(True)
                usartOperatingModeSym.setSelectedKey("RING_BUFFER")
            elif usart_form == "USART_FRAME_ISO_7816" or usart_form == "ISO7816" :
                usartOperatingModeSym.setSelectedKey("BLOCKING")
                usartOperatingModeSym.setReadOnly(True)
                event["source"].getSymbolByID("USART_7816_ENABLE").setValue(True)
                event["source"].getSymbolByID("USART_COMM_MODE").setValue(1)
            else:
                usartOperatingModeSym.setReadOnly(False)
                if event["source"].getSymbolByID("USART_7816_ENABLE").getValue() == True :
                    event["source"].getSymbolByID("USART_7816_ENABLE").setValue(False)
                if(event["source"].getSymbolByID("USART_COMM_MODE").getValue() == 1):
                    event["source"].getSymbolByID("USART_COMM_MODE").setValue(0)

def updateLinMasterModeOptionsVisibility(symbol, event):

    symbol.setVisible(event["symbol"].getSelectedKey() == "USART_FRAME_LIN_MASTER_MODE")

def updateUSARTDataBits (symbol, event):

    dataBits = event["symbol"].getSelectedKey()
    symbol.setValue(dataBitsDict[dataBits])

def update_CTRLB_SFDE_Visibility(symbol, event):
    usartOperatingMode = event["source"].getSymbolByID("USART_OPERATING_MODE").getSelectedKey()
    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and (usartOperatingMode != "BLOCKING"))

def updateInterruptMode (symbol, event):
    if symbol.getLabel() != "---":
        usartOperatingModeSym = event["source"].getSymbolByID("USART_OPERATING_MODE")
        if event["value"] == True and usartOperatingModeSym.getSelectedKey() != "RING_BUFFER" :
            usartOperatingModeSym.setSelectedKey("NON_BLOCKING")
        elif event["value"] == False:
            usartOperatingModeSym.setSelectedKey("BLOCKING")
        symbol.setLabel("---")

def updateRingBufferMode (symbol, event):
    if symbol.getLabel() != "---":
        if event["value"] == True:
            event["source"].getSymbolByID("USART_OPERATING_MODE").setSelectedKey("RING_BUFFER")
        symbol.setLabel("---")

def updateOperatingMode (symbol, event):
    if event["id"] == "USART_OPERATING_MODE":
        interruptModeSym = event["source"].getSymbolByID("USART_INTERRUPT_MODE_ENABLE")
        ringBufferModeSym = event["source"].getSymbolByID("USART_RING_BUFFER_MODE_ENABLE")
        if symbol.getSelectedKey() == "RING_BUFFER":
            interruptModeSym.setValue(True)
            ringBufferModeSym.setValue(True)
        elif symbol.getSelectedKey() == "NON_BLOCKING":
            interruptModeSym.setValue(True)
            ringBufferModeSym.setValue(False)
        elif symbol.getSelectedKey() == "BLOCKING":
            interruptModeSym.setValue(False)
            ringBufferModeSym.setValue(False)
    else:
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

def ringBufferConfigVisibility (symbol, event):
    ringBufferModeEnabled = event["source"].getSymbolByID("USART_RING_BUFFER_MODE_ENABLE").getValue()
    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT" and ringBufferModeEnabled == True)

def usartChszieEnumHelper(chsizeValuesList, bits):
    for index in range(len(chsizeValuesList)):
        if bits in chsizeValuesList[index].getAttribute("name"):
            return chsizeValuesList[index].getAttribute("name")

    return None

def updateFractionalBaudConfig(symbol, event):

    if event["id"] == "USART_FORM":
        usart_frame_format = event['source'].getSymbolByID("USART_FORM").getSelectedKey()
        if (sercomSym_OperationMode.getSelectedKey() == "USART_INT" and (usart_frame_format == "USART_FRAME_LIN_MASTER_MODE" or usart_frame_format == "USART_FRAME_AUTO_BAUD_NO_PARITY" or usart_frame_format == "USART_FRAME_AUTO_BAUD_WITH_PARITY")):
            symbol.setReadOnly(True)
            symbol.setValue(True)
        else:
            symbol.setValue(False)
            symbol.setReadOnly(False)

    elif event["id"] == "SERCOM_MODE":
        symbol.setVisible(sampleRateSupported == True and sercomSym_OperationMode.getSelectedKey() == "USART_INT")

###################################################################################################
############################################ USART ################################################
###################################################################################################

global usartSym_CTRLA_TXPO
global usartSym_CTRLA_SAMPR
global usartSym_SAMPLE_COUNT
global usartSym_BAUD_VALUE
global usartSym_BaudError_Comment
global sampleRateSupported
global usartSym_CTRLB_RXEN
global usartSym_CTRLB_TXEN
global usartSym_CTRLA_FORM
global usartSym_RingBuffer_Mode
global usartSym_Int_Mode
global usartSym_OperatingMode

sampleRateSupported = False
isFlowControlSupported = False
isRS485Supported = False
isErrorInterruptSupported = False

sampleRateNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="{0}",name="CTRLA"]'.format(sercomSymUSARTRegName.getValue()))

sampleRateValue = sampleRateNode.getChildren()

for index in range(len(sampleRateValue)):
    bitFieldName = str(sampleRateValue[index].getAttribute("name"))
    if bitFieldName == "SAMPR":
        sampleRateSupported = True
        break

if sampleRateSupported == True:
    #USART Over-Sampling using Baud Rate generation
    usartSym_CTRLA_SAMPR = sercomComponent.createIntegerSymbol("USART_SAMPLE_RATE", sercomSym_OperationMode)
    usartSym_CTRLA_SAMPR.setLabel("Sample Rate")
    usartSym_CTRLA_SAMPR.setDefaultValue(0)
    usartSym_CTRLA_SAMPR.setVisible(False)

# Depricated symbols ---------------------------------------------------------------------------------------------------
#Interrupt/Non-Interrupt Mode
usartSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("USART_INTERRUPT_MODE", sercomSym_OperationMode)
usartSym_Interrupt_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
usartSym_Interrupt_Mode.setDefaultValue(True)
usartSym_Interrupt_Mode.setVisible(False)
usartSym_Interrupt_Mode.setReadOnly(True)
usartSym_Interrupt_Mode.setDependencies(updateInterruptMode, ["USART_INTERRUPT_MODE"])

#Enable Ring buffer?
usartSym_RingBuffer_Enable = sercomComponent.createBooleanSymbol("USART_RING_BUFFER_ENABLE", sercomSym_OperationMode)
usartSym_RingBuffer_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_RingBuffer_Enable.setLabel("Enable Ring Buffer ?")
usartSym_RingBuffer_Enable.setDefaultValue(False)
usartSym_RingBuffer_Enable.setVisible(False)
usartSym_RingBuffer_Enable.setReadOnly(True)
usartSym_RingBuffer_Enable.setDependencies(updateRingBufferMode, ["USART_RING_BUFFER_ENABLE"])

# Depricated symbols ---------------------------------------------------------------------------------------------------

#Interrupt/Non-Interrupt Mode
usartSym_Int_Mode = sercomComponent.createBooleanSymbol("USART_INTERRUPT_MODE_ENABLE", sercomSym_OperationMode)
usartSym_Int_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_Int_Mode.setLabel("Enable Interrupts ?")
usartSym_Int_Mode.setDefaultValue(True)
usartSym_Int_Mode.setVisible(False)
usartSym_Int_Mode.setReadOnly(True)

#Enable Ring buffer?
usartSym_RingBuffer_Mode = sercomComponent.createBooleanSymbol("USART_RING_BUFFER_MODE_ENABLE", sercomSym_OperationMode)
usartSym_RingBuffer_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_RingBuffer_Mode.setLabel("Enable Ring Buffer ?")
usartSym_RingBuffer_Mode.setDefaultValue(False)
usartSym_RingBuffer_Mode.setVisible(False)
usartSym_RingBuffer_Mode.setReadOnly(True)

usartSym_OperatingMode = sercomComponent.createKeyValueSetSymbol("USART_OPERATING_MODE", sercomSym_OperationMode)
usartSym_OperatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_OperatingMode.setLabel("Operating Mode")
usartSym_OperatingMode.addKey("BLOCKING", "0", "Blocking mode")
usartSym_OperatingMode.addKey("NON_BLOCKING", "1", "Non-blocking mode")
usartSym_OperatingMode.addKey("RING_BUFFER", "2", "Ring buffer mode")
usartSym_OperatingMode.setDefaultValue(1)
usartSym_OperatingMode.setDisplayMode("Description")
usartSym_OperatingMode.setOutputMode("Key")
usartSym_OperatingMode.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_OperatingMode.setDependencies(updateOperatingMode, ["SERCOM_MODE",  "USART_OPERATING_MODE"])

usartSym_UsartRingBufferSizeConfig = sercomComponent.createCommentSymbol("SERCOM_USART_RING_BUFFER_SIZE_CONFIG", sercomSym_OperationMode)
usartSym_UsartRingBufferSizeConfig.setLabel("Configure Ring Buffer Size-")
usartSym_UsartRingBufferSizeConfig.setVisible(False)
usartSym_UsartRingBufferSizeConfig.setDependencies(ringBufferConfigVisibility, ["SERCOM_MODE", "USART_RING_BUFFER_MODE_ENABLE"])

usartSym_TXRingBuffer_Size = sercomComponent.createIntegerSymbol("USART_TX_RING_BUFFER_SIZE", usartSym_UsartRingBufferSizeConfig)
usartSym_TXRingBuffer_Size.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_TXRingBuffer_Size.setLabel("TX Ring Buffer Size")
usartSym_TXRingBuffer_Size.setMin(2)
usartSym_TXRingBuffer_Size.setMax(65535)
usartSym_TXRingBuffer_Size.setDefaultValue(128)
usartSym_TXRingBuffer_Size.setVisible(False)
usartSym_TXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["SERCOM_MODE", "USART_RING_BUFFER_MODE_ENABLE", "USART_TX_ENABLE"])

usartSym_RXRingBuffer_Size = sercomComponent.createIntegerSymbol("USART_RX_RING_BUFFER_SIZE", usartSym_UsartRingBufferSizeConfig)
usartSym_RXRingBuffer_Size.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_RXRingBuffer_Size.setLabel("RX Ring Buffer Size")
usartSym_RXRingBuffer_Size.setMin(2)
usartSym_RXRingBuffer_Size.setMax(65535)
usartSym_RXRingBuffer_Size.setDefaultValue(128)
usartSym_RXRingBuffer_Size.setVisible(False)
usartSym_RXRingBuffer_Size.setDependencies(updateRingBufferSizeVisibleProperty, ["SERCOM_MODE", "USART_RING_BUFFER_MODE_ENABLE", "USART_RX_ENABLE"])

#Receive Enable
usartSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("USART_RX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_RXEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_RXEN.setLabel("Receive Enable")
usartSym_CTRLB_RXEN.setDefaultValue(True)
usartSym_CTRLB_RXEN.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLB_RXEN.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#Transmit Enable
usartSym_CTRLB_TXEN = sercomComponent.createBooleanSymbol("USART_TX_ENABLE", sercomSym_OperationMode)
usartSym_CTRLB_TXEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_TXEN.setLabel("Transmit Enable")
usartSym_CTRLB_TXEN.setDefaultValue(True)
usartSym_CTRLB_TXEN.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLB_TXEN.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART Frame Format
isLINMasterModeSupported = False
usartSym_CTRLA_FORM = sercomComponent.createKeyValueSetSymbol("USART_FORM", sercomSym_OperationMode)
usartSym_CTRLA_FORM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_CTRLA_FORM.setLabel("Frame Format")

usartSym_CTRLA_FORM_Node = getValueGrp("SERCOM", "SERCOM", "CTRLA", "FORM", sercomSymUSARTRegName.getValue())
usartSym_CTRLA_FORM_Values = usartSym_CTRLA_FORM_Node.getChildren()

for index in range(len(usartSym_CTRLA_FORM_Values)):
    form_value = usartSym_CTRLA_FORM_Values[index].getAttribute("value")
    if form_value == "0x2":
        isLINMasterModeSupported = True
    if form_value <= "0x7":
        usartSym_CTRLA_FORM_Key_Name = usartSym_CTRLA_FORM_Values[index].getAttribute("name")
        usartSym_CTRLA_FORM_Key_Description = usartSym_CTRLA_FORM_Values[index].getAttribute("caption")
        usartSym_CTRLA_FORM_Key_Value = usartSym_CTRLA_FORM_Values[index].getAttribute("value")
        usartSym_CTRLA_FORM.addKey(usartSym_CTRLA_FORM_Key_Name, usartSym_CTRLA_FORM_Key_Value, usartSym_CTRLA_FORM_Key_Description)

usartSym_CTRLA_FORM.setDefaultValue(0)
usartSym_CTRLA_FORM.setOutputMode("Value")
usartSym_CTRLA_FORM.setDisplayMode("Description")
usartSym_CTRLA_FORM.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLA_FORM.setDependencies(updateUSARTFORMValueProperty, ["USART_PARITY_MODE", "SERCOM_MODE", "USART_FORM"])

#USART LIN Master Mode Support
usartSym_LIN_MasterSupport = sercomComponent.createBooleanSymbol("USART_LIN_MASTER_SUPPORTED", sercomSym_OperationMode)
usartSym_LIN_MasterSupport.setValue(isLINMasterModeSupported)
usartSym_LIN_MasterSupport.setVisible(False)

# BREAK Length - Applicable when LIN Master mode is selected
usartSym_CTRLC_BRKLEN_Node = getValueGrp("SERCOM", "SERCOM", "CTRLC", "BRKLEN", sercomSymUSARTRegName.getValue())

if usartSym_CTRLC_BRKLEN_Node != None:
    usartSym_CTRLC_BRKLEN = sercomComponent.createKeyValueSetSymbol("USART_LIN_MASTER_BREAK_LEN", sercomSym_OperationMode)
    usartSym_CTRLC_BRKLEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLC")
    usartSym_CTRLC_BRKLEN.setLabel("LIN Master Break Length")
    usartSym_CTRLC_BRKLEN_Values = usartSym_CTRLC_BRKLEN_Node.getChildren()

    for index in range(len(usartSym_CTRLC_BRKLEN_Values)):
        form_value = usartSym_CTRLC_BRKLEN_Values[index].getAttribute("value")
        if form_value <= "0x5":
            usartSym_CTRLC_BRKLEN_Key_Name = usartSym_CTRLC_BRKLEN_Values[index].getAttribute("name")
            usartSym_CTRLC_BRKLEN_Key_Description = usartSym_CTRLC_BRKLEN_Values[index].getAttribute("caption")
            usartSym_CTRLC_BRKLEN_Key_Value = usartSym_CTRLC_BRKLEN_Values[index].getAttribute("value")
            usartSym_CTRLC_BRKLEN.addKey(usartSym_CTRLC_BRKLEN_Key_Name, usartSym_CTRLC_BRKLEN_Key_Value, usartSym_CTRLC_BRKLEN_Key_Description)

    usartSym_CTRLC_BRKLEN.setDefaultValue(0)
    usartSym_CTRLC_BRKLEN.setOutputMode("Value")
    usartSym_CTRLC_BRKLEN.setDisplayMode("Description")
    usartSym_CTRLC_BRKLEN.setVisible(False)
    usartSym_CTRLC_BRKLEN.setDependencies(updateLinMasterModeOptionsVisibility, ["USART_FORM"])

# Hardware Delay - Applicable when LIN Master mode is selected
usartSym_CTRLC_HDRDLY_Node = getValueGrp("SERCOM", "SERCOM", "CTRLC", "HDRDLY", sercomSymUSARTRegName.getValue())

if usartSym_CTRLC_HDRDLY_Node != None:
    usartSym_CTRLC_HDRDLY = sercomComponent.createKeyValueSetSymbol("USART_LIN_MASTER_HDRDLY", sercomSym_OperationMode)
    usartSym_CTRLC_HDRDLY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLC")
    usartSym_CTRLC_HDRDLY.setLabel("LIN Master Hardware Delay")
    usartSym_CTRLC_HDRDLY_Values = usartSym_CTRLC_HDRDLY_Node.getChildren()

    for index in range(len(usartSym_CTRLC_HDRDLY_Values)):
        form_value = usartSym_CTRLC_HDRDLY_Values[index].getAttribute("value")
        if form_value <= "0x5":
            usartSym_CTRLC_HDRDLY_Key_Name = usartSym_CTRLC_HDRDLY_Values[index].getAttribute("name")
            usartSym_CTRLC_HDRDLY_Key_Description = usartSym_CTRLC_HDRDLY_Values[index].getAttribute("caption")
            usartSym_CTRLC_HDRDLY_Key_Value = usartSym_CTRLC_HDRDLY_Values[index].getAttribute("value")
            usartSym_CTRLC_HDRDLY.addKey(usartSym_CTRLC_HDRDLY_Key_Name, usartSym_CTRLC_HDRDLY_Key_Value, usartSym_CTRLC_HDRDLY_Key_Description)

    usartSym_CTRLC_HDRDLY.setDefaultValue(0)
    usartSym_CTRLC_HDRDLY.setOutputMode("Value")
    usartSym_CTRLC_HDRDLY.setDisplayMode("Description")
    usartSym_CTRLC_HDRDLY.setVisible(False)
    usartSym_CTRLC_HDRDLY.setDependencies(updateLinMasterModeOptionsVisibility, ["USART_FORM"])

#USART 7816 SMARTCARD Symbol
usartSym_smartcard = sercomComponent.createBooleanSymbol("USART_7816_ENABLE", sercomSym_OperationMode)
usartSym_smartcard.setDefaultValue(0)
usartSym_smartcard.setVisible(False)
usartSym_smartcard.setDependencies(updateUSARTFORMValueProperty, ["USART_FORM"])

usart7816SourceList = sercomComponent.createListSymbol("LIST_SERCOM_7816_C", None)
usart7816HeaderList = sercomComponent.createListSymbol("LIST_SERCOM_7816_H", None)

#USART Communication Mode
usartSym_COMM_MODE = sercomComponent.createIntegerSymbol("USART_COMM_MODE", sercomSym_OperationMode)
usartSym_COMM_MODE.setLabel("USART Communication Mode")
usartSym_COMM_MODE.setDefaultValue(0)
usartSym_COMM_MODE.setVisible(False)
usartSym_COMM_MODE.setDependencies(updateUSARTFORMValueProperty, ["USART_FORM"])

#USART 7816 Clock input comment
usartSym_7816_clk_input_Comment = sercomComponent.createCommentSymbol("USART_CLOCK_INPUT_COMMENT", sercomSym_OperationMode)
usartSym_7816_clk_input_Comment.setLabel("**** Enter the configured clock source for smartcard ****")
usartSym_7816_clk_input_Comment.setVisible(False)
usartSym_7816_clk_input_Comment.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART 7816 Output Clock
usartSym_CLOCK_OUTPUT = sercomComponent.createIntegerSymbol("USART_7816_CLOCK_OUTPUT", sercomSym_OperationMode)
usartSym_CLOCK_OUTPUT.setLabel("Output clock in Hz")
usartSym_CLOCK_OUTPUT.setDefaultValue(3571200)
usartSym_CLOCK_OUTPUT.setMin(1000000)
usartSym_CLOCK_OUTPUT.setMax(20000000)
usartSym_CLOCK_OUTPUT.setVisible(False)
usartSym_CLOCK_OUTPUT.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART Baud Rate
usartSym_BAUD_RATE = sercomComponent.createIntegerSymbol("USART_BAUD_RATE", sercomSym_OperationMode)
usartSym_BAUD_RATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:BAUD")
usartSym_BAUD_RATE.setLabel("Baud Rate in Hz")
usartSym_BAUD_RATE.setDefaultValue(115200)
usartSym_BAUD_RATE.setMin(1)
usartSym_BAUD_RATE.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_BAUD_RATE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE", "USART_7816_CLOCK_OUTPUT"])

#USART ISO7816 Baud Value
usartSym_7816_BAUD_VALUE = sercomComponent.createIntegerSymbol("USART_7816_BAUD_VALUE", sercomSym_OperationMode)
usartSym_7816_BAUD_VALUE.setLabel("ISO7816 Baud Rate Value")
usartSym_7816_BAUD_VALUE.setDefaultValue(185)
usartSym_7816_BAUD_VALUE.setVisible(False)
usartSym_7816_BAUD_VALUE.setDependencies(updateUSART7816BaudValueProperty, ["USART_7816_CLOCK_OUTPUT", "USART_BAUD_RATE"])

usartSym_UseFractionalBaud = sercomComponent.createBooleanSymbol("USART_USE_FRACTIONAL_BAUD", sercomSym_OperationMode)
usartSym_UseFractionalBaud.setLabel("Use fractional baud?")
usartSym_UseFractionalBaud.setValue(False)
usartSym_UseFractionalBaud.setVisible(sampleRateSupported == True)
usartSym_UseFractionalBaud.setDependencies(updateFractionalBaudConfig, ["USART_FORM", "SERCOM_MODE"])

#USART Baud Value
usartSym_BAUD_VALUE = sercomComponent.createIntegerSymbol("USART_BAUD_VALUE", sercomSym_OperationMode)
usartSym_BAUD_VALUE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:BAUD")
usartSym_BAUD_VALUE.setLabel("Baud Rate Value")
usartSym_BAUD_VALUE.setVisible(False)
usartSym_BAUD_VALUE.setDependencies(updateUSARTBaudValueProperty, ["USART_BAUD_RATE", "core." + sercomClkFrequencyId, "USART_FORM", "USART_USE_FRACTIONAL_BAUD"])

#USART Baud Rate not supported comment
usartSym_BaudError_Comment = sercomComponent.createCommentSymbol("USART_BAUD_ERROR_COMMENT", sercomSym_OperationMode)
usartSym_BaudError_Comment.setLabel("********** USART Clock source value is low for the desired baud rate **********")
usartSym_BaudError_Comment.setVisible(False)
usartSym_BaudError_Comment.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#CARD DETECT Pin Selection
usartSym_CardDetectPin = sercomComponent.createKeyValueSetSymbol("USART_7816_CARD_DETECT", sercomSym_OperationMode)
usartSym_CardDetectPin.setLabel("Card Detect Pin")
usartSym_CardDetectPin.setVisible(False)
usartSym_CardDetectPin.setOutputMode("Key")
usartSym_CardDetectPin.setDisplayMode("Description")
usartSym_CardDetectPin.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])
usartSym_CardDetectPin.addKey("SYS_PORT_PIN_NONE", "-1", "None")

availablePinDictionary = {}

# Send message to core to get available pins
availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

for pad in sort_alphanumeric(availablePinDictionary.values()):
    key = pad
    value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
    description = pad
    usartSym_CardDetectPin.addKey(key, value, description)

#VCC Enable Pin Selection
usartSym_VCCEnablePin = sercomComponent.createKeyValueSetSymbol("USART_7816_VCC_ENABLE", sercomSym_OperationMode)
usartSym_VCCEnablePin.setLabel("VCC Enable Pin")
usartSym_VCCEnablePin.setVisible(False)
usartSym_VCCEnablePin.setOutputMode("Key")
usartSym_VCCEnablePin.setDisplayMode("Description")
usartSym_VCCEnablePin.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])
usartSym_VCCEnablePin.addKey("SYS_PORT_PIN_NONE", "-1", "None")

availablePinDictionary = {}

# Send message to core to get available pins
availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

for pad in sort_alphanumeric(availablePinDictionary.values()):
    key = pad
    value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
    description = pad
    usartSym_VCCEnablePin.addKey(key, value, description)

#RESET Pin Selection
usartSym_ResetPin = sercomComponent.createKeyValueSetSymbol("USART_7816_RESET", sercomSym_OperationMode)
usartSym_ResetPin.setLabel("RESET Pin")
usartSym_ResetPin.setVisible(False)
usartSym_ResetPin.setOutputMode("Key")
usartSym_ResetPin.setDisplayMode("Description")
usartSym_ResetPin.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])
usartSym_ResetPin.addKey("SYS_PORT_PIN_NONE", "-1", "None")

availablePinDictionary = {}

# Send message to core to get available pins
availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

for pad in sort_alphanumeric(availablePinDictionary.values()):
    key = pad
    value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
    description = pad
    usartSym_ResetPin.addKey(key, value, description)

#PMODE : USART PARITY MODE
usartSym_CTRLB_PMODE = sercomComponent.createKeyValueSetSymbol("USART_PARITY_MODE", sercomSym_OperationMode)
usartSym_CTRLB_PMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_PMODE.setLabel("Parity Mode")
usartSym_CTRLB_PMODE.addKey("EVEN", "0x0", "Even Parity")
usartSym_CTRLB_PMODE.addKey("ODD", "0x1", "Odd Parity")
usartSym_CTRLB_PMODE.addKey("NONE", "0x2", "No Parity")
usartSym_CTRLB_PMODE.setDefaultValue(2)
usartSym_CTRLB_PMODE.setOutputMode("Key")
usartSym_CTRLB_PMODE.setDisplayMode("Description")
usartSym_CTRLB_PMODE.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLB_PMODE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE", "USART_FORM"])

#USART 7816 GTIME
usartSym_GTIME = sercomComponent.createIntegerSymbol("USART_7816_GTIME", sercomSym_OperationMode)
usartSym_GTIME.setLabel("Guard Time")
usartSym_GTIME.setDefaultValue(0)
usartSym_GTIME.setMin(0)
usartSym_GTIME.setMax(7)
usartSym_GTIME.setVisible(False)
usartSym_GTIME.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART 7816 MAXITER
usartSym_MAXITER = sercomComponent.createIntegerSymbol("USART_7816_MAXITER", sercomSym_OperationMode)
usartSym_MAXITER.setLabel("Maximum Iterations")
usartSym_MAXITER.setDefaultValue(0)
usartSym_MAXITER.setMin(0)
usartSym_MAXITER.setMax(7)
usartSym_MAXITER.setVisible(False)
usartSym_MAXITER.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART 7816 INACK
usartSym_INACK = sercomComponent.createBooleanSymbol("USART_7816_INACK", sercomSym_OperationMode)
usartSym_INACK.setLabel("Disable NACK when parity error received")
usartSym_INACK.setDefaultValue(False)
usartSym_INACK.setVisible(False)
usartSym_INACK.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART 7816 DSNACK
usartSym_DSNACK = sercomComponent.createBooleanSymbol("USART_7816_DSNACK", sercomSym_OperationMode)
usartSym_DSNACK.setLabel("Disable Successive Not Acknowledge")
usartSym_DSNACK.setDefaultValue(False)
usartSym_DSNACK.setVisible(False)
usartSym_DSNACK.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#Character Size
usartSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("USART_CHARSIZE_BITS", sercomSym_OperationMode)
usartSym_CTRLB_CHSIZE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_CHSIZE.setLabel("Character Size")

usartSym_CTRLA_CHSIZE_Node = getValueGrp("SERCOM", "SERCOM", "CTRLB", "CHSIZE", sercomSymUSARTRegName.getValue())
usartSym_CTRLA_CHSIZE_Values = usartSym_CTRLA_CHSIZE_Node.getChildren()

for index in range(len(usartSym_CTRLA_CHSIZE_Values)):
    usartSym_CTRLB_CHSIZE_Key_Name = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("name")
    usartSym_CTRLB_CHSIZE_Key_Description = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("caption")
    usartSym_CTRLB_CHSIZE_Key_Value = usartSym_CTRLA_CHSIZE_Values[index].getAttribute("value")
    usartSym_CTRLB_CHSIZE.addKey(usartSym_CTRLB_CHSIZE_Key_Name, usartSym_CTRLB_CHSIZE_Key_Value, usartSym_CTRLB_CHSIZE_Key_Description)

usartSym_CTRLB_CHSIZE.setDefaultValue(0)
usartSym_CTRLB_CHSIZE.setOutputMode("Key")
usartSym_CTRLB_CHSIZE.setDisplayMode("Description")
usartSym_CTRLB_CHSIZE.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLB_CHSIZE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

usartChsizeEnumList = sercomComponent.createListSymbol("SERCOM_CHSIZE_ENUM_LIST", None)
usartChsizeEnumList.setVisible(False)

usartChsizeEnums = sercomComponent.createListEntrySymbol("SERCOM_CHSIZE_ENUM", None)
usartChsizeEnums.setVisible(False)
for i in range (5,10):
    chsizeEnumVal = usartChszieEnumHelper(usartSym_CTRLA_CHSIZE_Values, str(i))
    if chsizeEnumVal != None:
        dataBitsDict[chsizeEnumVal] = "DRV_USART_DATA_" + str(i) + "_BIT"
        chsizeEnumVal = "    USART_DATA_" + str(i) + "_BIT = SERCOM_" + sercomSymUSARTRegName.getValue() + "_CTRLB_CHSIZE_" + chsizeEnumVal + ","
        usartChsizeEnums.addValue(chsizeEnumVal)

usartChsizeEnums.setTarget(sercomInstanceName.getValue().lower() + ".SERCOM_CHSIZE_ENUM_LIST")

#Stop Bit
usartSym_CTRLB_SBMODE = sercomComponent.createKeyValueSetSymbol("USART_STOP_BIT", sercomSym_OperationMode)
usartSym_CTRLB_SBMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_SBMODE.setLabel("Stop Bit Mode")

usartSym_CTRLA_SBMODE_Node = getValueGrp("SERCOM", "SERCOM", "CTRLB", "SBMODE", sercomSymUSARTRegName.getValue())
usartSym_CTRLA_SBMODE_Values = usartSym_CTRLA_SBMODE_Node.getChildren()

for index in range(len(usartSym_CTRLA_SBMODE_Values)):
    usartSym_CTRLB_SBMODE_Key_Name = usartSym_CTRLA_SBMODE_Values[index].getAttribute("name")
    usartSym_CTRLB_SBMODE_Key_Description = usartSym_CTRLA_SBMODE_Values[index].getAttribute("caption")
    usartSym_CTRLB_SBMODE_Key_Value = usartSym_CTRLA_SBMODE_Values[index].getAttribute("value")
    usartSym_CTRLB_SBMODE.addKey(usartSym_CTRLB_SBMODE_Key_Name, usartSym_CTRLB_SBMODE_Key_Value, usartSym_CTRLB_SBMODE_Key_Description)

usartSym_CTRLB_SBMODE.setDefaultValue(0)
usartSym_CTRLB_SBMODE.setOutputMode("Key")
usartSym_CTRLB_SBMODE.setDisplayMode("Description")
usartSym_CTRLB_SBMODE.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLB_SBMODE.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

usartSbmodeEnumList = sercomComponent.createListSymbol("SERCOM_SBMODE_ENUM_LIST", None)
usartSbmodeEnumList.setVisible(False)
usartSbmodeEnums = sercomComponent.createListEntrySymbol("SERCOM_SBMODE_ENUM", None)
usartSbmodeEnums.setVisible(False)
for i in range (0, 2):
    if int(usartSym_CTRLA_SBMODE_Values[i].getAttribute("value"), 0) == i:
        sbmodeEnumVal = "    USART_STOP_" + str(i) + "_BIT = " + "SERCOM_" + sercomSymUSARTRegName.getValue() + "_CTRLB_SBMODE_" + usartSym_CTRLA_SBMODE_Values[i].getAttribute("name") + ","
        usartSbmodeEnums.addValue(sbmodeEnumVal)
usartSbmodeEnums.setTarget(sercomInstanceName.getValue().lower() + ".SERCOM_SBMODE_ENUM_LIST")

usartSym_CTRLB_SFDE = sercomComponent.createBooleanSymbol("USART_SFDE", sercomSym_OperationMode)
usartSym_CTRLB_SFDE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
usartSym_CTRLB_SFDE.setLabel("Start-of-Frame Detection Enable")
usartSym_CTRLB_SFDE.setDefaultValue(False)
usartSym_CTRLB_SFDE.setDependencies(update_CTRLB_SFDE_Visibility, ["SERCOM_MODE", "USART_OPERATING_MODE"])

#RXPO - Receive Pin Out
usartSym_CTRLA_RXPO = sercomComponent.createKeyValueSetSymbol("USART_RXPO", sercomSym_OperationMode)
usartSym_CTRLA_RXPO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_CTRLA_RXPO.setLabel("Receive Pinout")

usartSym_CTRLA_RXPO_Node = getValueGrp("SERCOM", "SERCOM", "CTRLA", "RXPO", sercomSymUSARTRegName.getValue())
usartSym_CTRLA_RXPO_Values = usartSym_CTRLA_RXPO_Node.getChildren()

for index in range(len(usartSym_CTRLA_RXPO_Values)):
    usartSym_CTRLA_RXPO_Key_Name = usartSym_CTRLA_RXPO_Values[index].getAttribute("name")
    usartSym_CTRLA_RXPO_Key_Description = usartSym_CTRLA_RXPO_Values[index].getAttribute("caption")
    usartSym_CTRLA_RXPO_Key_Value = usartSym_CTRLA_RXPO_Values[index].getAttribute("value")
    usartSym_CTRLA_RXPO.addKey(usartSym_CTRLA_RXPO_Key_Name, usartSym_CTRLA_RXPO_Key_Value, usartSym_CTRLA_RXPO_Key_Description)

usartSym_CTRLA_RXPO.setDefaultValue(0)
usartSym_CTRLA_RXPO.setOutputMode("Value")
usartSym_CTRLA_RXPO.setDisplayMode("Description")
usartSym_CTRLA_RXPO.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLA_RXPO.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#TXPO - Transmit Pin Out
usartSym_CTRLA_TXPO = sercomComponent.createKeyValueSetSymbol("USART_TXPO", sercomSym_OperationMode)
usartSym_CTRLA_TXPO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_CTRLA_TXPO.setLabel("Transmit Pinout")

usartSym_CTRLA_TXPO_Node = getValueGrp("SERCOM", "SERCOM", "CTRLA", "TXPO", sercomSymUSARTRegName.getValue())
usartSym_CTRLA_TXPO_Values = usartSym_CTRLA_TXPO_Node.getChildren()

for index in range(len(usartSym_CTRLA_TXPO_Values)):
    usartSym_CTRLA_TXPO_Key_Name = usartSym_CTRLA_TXPO_Values[index].getAttribute("name")
    usartSym_CTRLA_TXPO_Key_Description = usartSym_CTRLA_TXPO_Values[index].getAttribute("caption")
    usartSym_CTRLA_TXPO_Key_Value = usartSym_CTRLA_TXPO_Values[index].getAttribute("value")
    usartSym_CTRLA_TXPO.addKey(usartSym_CTRLA_TXPO_Key_Name, usartSym_CTRLA_TXPO_Key_Value, usartSym_CTRLA_TXPO_Key_Description)

    if int(usartSym_CTRLA_TXPO_Key_Value, 0) == 2:
        isFlowControlSupported = True
    if int(usartSym_CTRLA_TXPO_Key_Value, 0) == 3:
        isRS485Supported = True

usartSym_CTRLA_TXPO.setDefaultValue(0)
usartSym_CTRLA_TXPO.setOutputMode("Value")
usartSym_CTRLA_TXPO.setDisplayMode("Description")
usartSym_CTRLA_TXPO.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLA_TXPO.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

if isRS485Supported == True:
    #USART RS485 mode Guard Time
    usartSym_CTRLC_GTIME = sercomComponent.createIntegerSymbol("USART_CTRLC_GTIME", sercomSym_OperationMode)
    usartSym_CTRLC_GTIME.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLC")
    usartSym_CTRLC_GTIME.setLabel("RS485 Guard Time")
    usartSym_CTRLC_GTIME.setDefaultValue(0)
    usartSym_CTRLC_GTIME.setMin(0)
    usartSym_CTRLC_GTIME.setMax(7)
    usartSym_CTRLC_GTIME.setVisible(False)
    usartSym_CTRLC_GTIME.setDependencies(updateUSARTRS485GuardTimeValueProperty, ["SERCOM_MODE", "USART_TXPO" , "USART_FORM"])

#Run in StandBy
usartSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("USART_RUNSTDBY", sercomSym_OperationMode)
usartSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
usartSym_CTRLA_RUNSTDBY.setLabel("Enable Run in Standby")
usartSym_CTRLA_RUNSTDBY.setVisible(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
usartSym_CTRLA_RUNSTDBY.setDependencies(updateUSARTConfigurationVisibleProperty, ["SERCOM_MODE"])

#USART 7816 Clock configuration comment
usartSym_7816_clkcfg_Comment = sercomComponent.createCommentSymbol("USART_CLOCK_CFG_COMMENT", sercomSym_OperationMode)
usartSym_7816_clkcfg_Comment.setLabel("********** Configure GCLK I/O pin as clock output to smartcard **********")
usartSym_7816_clkcfg_Comment.setVisible(False)
usartSym_7816_clkcfg_Comment.setDependencies(updateSMARTCARDPinProperty, ["SERCOM_MODE","USART_FORM"])

#USART No Of Samples
usartSym_SAMPLE_COUNT = sercomComponent.createIntegerSymbol("USART_SAMPLE_COUNT", sercomSym_OperationMode)
usartSym_SAMPLE_COUNT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:%NOREGISTER%")
usartSym_SAMPLE_COUNT.setLabel("No Of Samples")
usartSym_SAMPLE_COUNT.setDefaultValue(16)
usartSym_SAMPLE_COUNT.setVisible(False)

intensetNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="{0}",name="INTENSET"]'.format(sercomSymUSARTRegName.getValue()))
intensetValue = intensetNode.getChildren()

for index in range(len(intensetValue)):
    bitFieldName = str(intensetValue[index].getAttribute("name"))
    if bitFieldName == "ERROR":
        isErrorInterruptSupported = True
        break

#USART is ERROR present
usartSym_ErrorInterrupt = sercomComponent.createBooleanSymbol("USART_INTENSET_ERROR", None)
usartSym_ErrorInterrupt.setVisible(False)
usartSym_ErrorInterrupt.setDefaultValue(isErrorInterruptSupported)

#USART Flow Control supported
usartSym_FlowControl = sercomComponent.createBooleanSymbol("USART_FLOW_CONTROL", None)
usartSym_FlowControl.setVisible(False)
usartSym_FlowControl.setDefaultValue(isFlowControlSupported)

#USART RS485 mode supported
usartSym_RS485 = sercomComponent.createBooleanSymbol("USART_RS485", None)
usartSym_RS485.setVisible(False)
usartSym_RS485.setDefaultValue(isRS485Supported)

#Use setValue instead of setDefaultValue to store symbol value in default.xml
usartSym_BAUD_VALUE.setValue(getUSARTBaudValue(), 1)

usartSym_CTRLA_MODE_Values = getValueGrp("SERCOM", "SERCOM", "CTRLA", "MODE", sercomSymUSARTRegName.getValue()).getChildren()

usartSymMode = sercomComponent.createStringSymbol("USART_MODE", sercomSym_OperationMode)
usartSymMode.setVisible(False)
for index in range(len(usartSym_CTRLA_MODE_Values)):
    if int(usartSym_CTRLA_MODE_Values[index].getAttribute("value"), 0) == 1:
        usartSymMode.setDefaultValue(usartSym_CTRLA_MODE_Values[index].getAttribute("name"))
        break



###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#USART API Prefix
usartSym_API_Prefix = sercomComponent.createStringSymbol("USART_PLIB_API_PREFIX", sercomSym_OperationMode)
usartSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_USART")
usartSym_API_Prefix.setVisible(False)

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

#USART Stop 1-bit Mask
usartSym_CTRLB_SBMODE_1_Mask = sercomComponent.createStringSymbol("USART_STOP_1_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_SBMODE_1_Mask.setDefaultValue("0x0")
usartSym_CTRLB_SBMODE_1_Mask.setVisible(False)

#USART Stop 2-bit Mask
usartSym_CTRLB_SBMODE_2_Mask = sercomComponent.createStringSymbol("USART_STOP_2_BIT_MASK", sercomSym_OperationMode)
usartSym_CTRLB_SBMODE_2_Mask.setDefaultValue("0x40")
usartSym_CTRLB_SBMODE_2_Mask.setVisible(False)

#USART Overrun error Mask
sercomSym_STATUS_BUFOVF_Mask = sercomComponent.createStringSymbol("USART_OVERRUN_ERROR_VALUE", sercomSym_OperationMode)
sercomSym_STATUS_BUFOVF_Mask.setDefaultValue("0x4")
sercomSym_STATUS_BUFOVF_Mask.setVisible(False)

#USART parity error Mask
sercomSym_STATUS_PERR_Mask = sercomComponent.createStringSymbol("USART_PARITY_ERROR_VALUE", sercomSym_OperationMode)
sercomSym_STATUS_PERR_Mask.setDefaultValue("0x0")
sercomSym_STATUS_PERR_Mask.setVisible(False)

#USART framing error Mask
sercomSym_STATUS_FERR_Mask = sercomComponent.createStringSymbol("USART_FRAMING_ERROR_VALUE", sercomSym_OperationMode)
sercomSym_STATUS_FERR_Mask.setDefaultValue("0x2")
sercomSym_STATUS_FERR_Mask.setVisible(False)

usartSym_DataBits = sercomComponent.createStringSymbol("USART_DATA_BITS", sercomSym_OperationMode)
usartSym_DataBits.setDefaultValue(dataBitsDict[usartSym_CTRLB_CHSIZE.getSelectedKey()])
usartSym_DataBits.setVisible(False)
usartSym_DataBits.setDependencies(updateUSARTDataBits, ["USART_CHARSIZE_BITS"])