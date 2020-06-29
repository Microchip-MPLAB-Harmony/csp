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

global sort_alphanumeric

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)


# SPI Components Visible Property
def updateSPISlaveConfigurationVisibleProperty(symbol, event):

    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "SPIS")
    
# SPI Components Visible Property
def updateSPISlaveBusyPinVisibility(symbol, event):

    sercomMode = sercomSym_OperationMode.getSelectedKey()
    busyPinEnabled = event["source"].getSymbolByID("SPIS_USE_BUSY_PIN").getValue() == True
    symbol.setVisible(sercomMode == "SPIS" and busyPinEnabled == True)       

#SPI Transfer Mode Comment
def setSPIClockModeInfo(symbol, event):

    if event["id"] == "SERCOM_MODE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "SPIS")
    else:
        component = symbol.getComponent().getID()

        CPHA = Database.getSymbolValue(component, "SPIS_CLOCK_PHASE")
        CPOL = Database.getSymbolValue(component, "SPIS_CLOCK_POLARITY")

        if CPOL == 0 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 0 is Selected***")
        elif CPOL == 0 and CPHA == 1:
            symbol.setLabel("***SPI Transfer Mode 1 is Selected***")
        elif CPOL == 1 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 2 is Selected***")
        else:
            symbol.setLabel("***SPI Transfer Mode 3 is Selected***")

###################################################################################################
######################################## SPI SLAVE ###############################################
###################################################################################################

global spisSym_Interrupt_Mode

#SPI Interrupt Mode
spisSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("SPIS_INTERRUPT_MODE", sercomSym_OperationMode)
spisSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
spisSym_Interrupt_Mode.setDefaultValue(True)
spisSym_Interrupt_Mode.setVisible(False)
spisSym_Interrupt_Mode.setReadOnly(True)
spisSym_Interrupt_Mode.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Standby Mode
spisSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("SPIS_RUNSTDBY", sercomSym_OperationMode)
spisSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
spisSym_CTRLA_RUNSTDBY.setVisible(False)
spisSym_CTRLA_RUNSTDBY.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI DataOut PinOut
spisSym_CTRLA_DOPO = sercomComponent.createKeyValueSetSymbol("SPIS_DOPO", sercomSym_OperationMode)
spisSym_CTRLA_DOPO.setLabel("SPI Data Out Pad")
spisSym_CTRLA_DOPO.setVisible(False)

spisDOPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DOPO\"]")
spisDOPOValues = spisDOPONode.getChildren()

for index in range(len(spisDOPOValues)):
    spiDOPOKeyName = spisDOPOValues[index].getAttribute("name")
    spiDOPOKeyDescription = spisDOPOValues[index].getAttribute("caption")
    spiDOPOKeyValue = spisDOPOValues[index].getAttribute("value")
    spisSym_CTRLA_DOPO.addKey(spiDOPOKeyName, spiDOPOKeyValue, spiDOPOKeyDescription)

spisSym_CTRLA_DOPO.setDefaultValue(0)
spisSym_CTRLA_DOPO.setOutputMode("Key")
spisSym_CTRLA_DOPO.setDisplayMode("Description")
spisSym_CTRLA_DOPO.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI DataIn pinOut
spisSym_CTRLA_DIPO = sercomComponent.createKeyValueSetSymbol("SPIS_DIPO", sercomSym_OperationMode)
spisSym_CTRLA_DIPO.setLabel("SPI Data In Pad Selection")
spisSym_CTRLA_DIPO.setVisible(False)

spisDIPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DIPO\"]")
spisDIPOValues = spisDIPONode.getChildren()

for index in range(len(spisDIPOValues)):
    spiDIPOKeyName = spisDIPOValues[index].getAttribute("name")
    spiDIPOKeyDescription = spisDIPOValues[index].getAttribute("caption")
    spiDIPOKeyValue = spisDIPOValues[index].getAttribute("value")
    spisSym_CTRLA_DIPO.addKey(spiDIPOKeyName, spiDIPOKeyValue, spiDIPOKeyDescription)

spisSym_CTRLA_DIPO.setDefaultValue(0)
spisSym_CTRLA_DIPO.setOutputMode("Key")
spisSym_CTRLA_DIPO.setDisplayMode("Description")
spisSym_CTRLA_DIPO.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Data Order
spisSym_CTRLA_DORD = sercomComponent.createKeyValueSetSymbol("SPIS_DATA_ORDER", sercomSym_OperationMode)
spisSym_CTRLA_DORD.setLabel("SPI Data Order")
spisSym_CTRLA_DORD.setVisible(False)

spisDORDNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DORD\"]")
spisDORDValues = spisDORDNode.getChildren()

for index in range(len(spisDORDValues)):
    spiDORDKeyName = spisDORDValues[index].getAttribute("name")
    spiDORDKeyDescription = spisDORDValues[index].getAttribute("caption")
    spiDORDKeyValue = spisDORDValues[index].getAttribute("value")
    spisSym_CTRLA_DORD.addKey(spiDORDKeyName, spiDORDKeyValue, spiDORDKeyDescription)

spisSym_CTRLA_DORD.setDefaultValue(0)
spisSym_CTRLA_DORD.setOutputMode("Key")
spisSym_CTRLA_DORD.setDisplayMode("Description")
spisSym_CTRLA_DORD.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Character Size
spisSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("SPIS_CHARSIZE_BITS", sercomSym_OperationMode)
spisSym_CTRLB_CHSIZE.setLabel("SPI Data Character Size")
spisSym_CTRLB_CHSIZE.setVisible(False)

spisCHSIZENode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLB__CHSIZE\"]")
spisCHSIZEValues = spisCHSIZENode.getChildren()

for index in range(len(spisCHSIZEValues)):
    spiCHSIZEKeyName = spisCHSIZEValues[index].getAttribute("name")
    spiCHSIZEKeyDescription = spisCHSIZEValues[index].getAttribute("caption")
    spiCHSIZEKeyValue = spisCHSIZEValues[index].getAttribute("value")
    spisSym_CTRLB_CHSIZE.addKey(spiCHSIZEKeyName, spiCHSIZEKeyValue, spiCHSIZEKeyDescription)

spisSym_CTRLB_CHSIZE.setDefaultValue(0)
spisSym_CTRLB_CHSIZE.setOutputMode("Key")
spisSym_CTRLB_CHSIZE.setDisplayMode("Description")
spisSym_CTRLB_CHSIZE.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Clock Phase
spisSym_CTRLA_ClockPhase = sercomComponent.createKeyValueSetSymbol("SPIS_CLOCK_PHASE", sercomSym_OperationMode)
spisSym_CTRLA_ClockPhase.setLabel("SPI Clock Phase")
spisSym_CTRLA_ClockPhase.setVisible(False)

spsiCLKPHASENode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__CPHA\"]")
spisCLKPHASEValues = spsiCLKPHASENode.getChildren()

for index in range(len(spisCLKPHASEValues)):
    spiCLKPHASEKeyName = spisCLKPHASEValues[index].getAttribute("name")
    spiCLKPHASEKeyDescription = spisCLKPHASEValues[index].getAttribute("caption")
    spiCLKPHASEKeyValue = spisCLKPHASEValues[index].getAttribute("value")
    spisSym_CTRLA_ClockPhase.addKey(spiCLKPHASEKeyName, spiCLKPHASEKeyValue, spiCLKPHASEKeyDescription)

spisSym_CTRLA_ClockPhase.setDefaultValue(0)
spisSym_CTRLA_ClockPhase.setOutputMode("Key")
spisSym_CTRLA_ClockPhase.setDisplayMode("Description")
spisSym_CTRLA_ClockPhase.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Clock Polarity
spisSym_CTRLA_ClockPolarity = sercomComponent.createKeyValueSetSymbol("SPIS_CLOCK_POLARITY", sercomSym_OperationMode)
spisSym_CTRLA_ClockPolarity.setLabel("SPI Clock Polarity")
spisSym_CTRLA_ClockPolarity.setVisible(False)

spisCLKPLORITYNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__CPOL\"]")
spisCLKPLORITYValues = spisCLKPLORITYNode.getChildren()

for index in range(len(spisCLKPLORITYValues)):
    spiCLKPLORITYKeyName = spisCLKPLORITYValues[index].getAttribute("name")
    spiCLKPLORITYKeyDescription = spisCLKPLORITYValues[index].getAttribute("caption")
    spiCLKPLORITYKeyValue = spisCLKPLORITYValues[index].getAttribute("value")
    spisSym_CTRLA_ClockPolarity.addKey(spiCLKPLORITYKeyName, spiCLKPLORITYKeyValue, spiCLKPLORITYKeyDescription)

spisSym_CTRLA_ClockPolarity.setDefaultValue(0)
spisSym_CTRLA_ClockPolarity.setOutputMode("Key")
spisSym_CTRLA_ClockPolarity.setDisplayMode("Description")
spisSym_CTRLA_ClockPolarity.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

ssdeSupported = False

ctrlbNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="SPIS",name="CTRLB"]')
ctrlbValue = ctrlbNode.getChildren()

for index in range(len(ctrlbValue)):
    bitFieldName = str(ctrlbValue[index].getAttribute("name"))
    if bitFieldName == "SSDE":
        ssdeSupported = True
        break

if ssdeSupported == True:
    #SPI Hardware Slave Select control
    spisSym_CTRLB_SSDE = sercomComponent.createBooleanSymbol("SPIS_SSDE", sercomSym_OperationMode)
    spisSym_CTRLB_SSDE.setLabel("Slave Select Low Detect Enable")
    spisSym_CTRLB_SSDE.setDefaultValue(True)
    spisSym_CTRLB_SSDE.setVisible(False)
    spisSym_CTRLB_SSDE.setReadOnly(True)
    spisSym_CTRLB_SSDE.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

spisSym_TXBuffer_Size = sercomComponent.createIntegerSymbol("SPIS_TX_BUFFER_SIZE", sercomSym_OperationMode)
spisSym_TXBuffer_Size.setLabel("TX Buffer Size (in bytes)")
spisSym_TXBuffer_Size.setMin(0)
spisSym_TXBuffer_Size.setMax(65535)
spisSym_TXBuffer_Size.setDefaultValue(256)
spisSym_TXBuffer_Size.setVisible(False)
spisSym_TXBuffer_Size.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

spisSym_RXBuffer_Size = sercomComponent.createIntegerSymbol("SPIS_RX_BUFFER_SIZE", sercomSym_OperationMode)
spisSym_RXBuffer_Size.setLabel("RX Buffer Size (in bytes)")
spisSym_RXBuffer_Size.setMin(0)
spisSym_RXBuffer_Size.setMax(65535)
spisSym_RXBuffer_Size.setDefaultValue(256)
spisSym_RXBuffer_Size.setVisible(False)
spisSym_RXBuffer_Size.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

spisSymUseBusyPin = sercomComponent.createBooleanSymbol("SPIS_USE_BUSY_PIN", sercomSym_OperationMode)
spisSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
spisSymUseBusyPin.setDefaultValue(True)
spisSymUseBusyPin.setVisible(False)
spisSymUseBusyPin.setDependencies(updateSPISlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

spisSymBusyPin = sercomComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN", spisSymUseBusyPin)
spisSymBusyPin.setVisible(False)
spisSymBusyPin.setLabel("Slave Busy Pin")
spisSymBusyPin.setOutputMode("Key")
spisSymBusyPin.setDisplayMode("Description")
spisSymBusyPin.setDependencies(updateSPISlaveBusyPinVisibility, ["SERCOM_MODE", "SPIS_USE_BUSY_PIN"])

availablePinDictionary = {}

# Send message to core to get available pins
availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

for pad in sort_alphanumeric(availablePinDictionary.values()):
    key = pad
    value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
    description = pad
    spisSymBusyPin.addKey(key, value, description)    
    
#SPI Character Size
spisSymBusyPinLogicLevel = sercomComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN_LOGIC_LEVEL", spisSymUseBusyPin)
spisSymBusyPinLogicLevel.setLabel("Slave Busy Pin Logic Level")
spisSymBusyPinLogicLevel.setVisible(False)
spisSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
spisSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
spisSymBusyPinLogicLevel.setDefaultValue(1)
spisSymBusyPinLogicLevel.setOutputMode("Key")
spisSymBusyPinLogicLevel.setDisplayMode("Description")
spisSymBusyPinLogicLevel.setDependencies(updateSPISlaveBusyPinVisibility, ["SERCOM_MODE", "SPIS_USE_BUSY_PIN"])
    
spisSymBusyPinConfigComment = sercomComponent.createCommentSymbol("SPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT", spisSymUseBusyPin)
spisSymBusyPinConfigComment.setVisible(False)
spisSymBusyPinConfigComment.setLabel("***Above selected pins must be configured as GPIO Output in Pin Manager***")
spisSymBusyPinConfigComment.setDependencies(updateSPISlaveBusyPinVisibility, ["SERCOM_MODE", "SPIS_USE_BUSY_PIN"])

errorIntSupported = False

intensetNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="SPIS",name="INTENSET"]')
intensetValue = intensetNode.getChildren()

for index in range(len(intensetValue)):
    bitFieldName = str(intensetValue[index].getAttribute("name"))
    if bitFieldName == "ERROR":
        errorIntSupported = True
        break

if errorIntSupported == True:
    #SPI is ERROR present
    spisSym_ERROR = sercomComponent.createBooleanSymbol("SPIS_INTENSET_ERROR", None)
    spisSym_ERROR.setVisible(False)
    spisSym_ERROR.setDefaultValue(True)

# SPI Clock Mode
spisSym_ClockModeComment = sercomComponent.createCommentSymbol("SPIS_CLOCK_MODE_COMMENT", sercomSym_OperationMode)
spisSym_ClockModeComment.setLabel("***SPI Transfer Mode 0 is Selected***")
spisSym_ClockModeComment.setVisible(False)
spisSym_ClockModeComment.setDependencies(setSPIClockModeInfo, ["SERCOM_MODE", "SPIS_CLOCK_PHASE", "SPIS_CLOCK_POLARITY"])


###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

# SPI slave mode is not supported in SPI driver