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

#SPI Mode property
def setspiMODEVisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Standby property
def setspiSTANDBYVisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI DOPO property
def set_SPI_DOPO_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI DIPO property
def set_SPI_DIPO_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Transfer Mode Comment
def setSPIClockModeInfo(symbol, event):

    if event["id"] == "SERCOM_MODE":
        if event["value"] == 0x03:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        component = symbol.getComponent().getID()

        CPHA = Database.getSymbolValue(component, "SPI_CLOCK_PHASE")
        CPOL = Database.getSymbolValue(component, "SPI_CLOCK_POLARITY")

        Database.clearSymbolValue(component, "SPI_TRANSFER_MODE")

        if CPOL == 0 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 0 is Selected***")
            Database.setSymbolValue(component, "SPI_TRANSFER_MODE", "0x0", 2)
        elif CPOL == 0 and CPHA == 1:
            symbol.setLabel("***SPI Transfer Mode 1 is Selected***")
            Database.setSymbolValue(component, "SPI_TRANSFER_MODE", "0x10000000", 2)
        elif CPOL == 1 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 2 is Selected***")
            Database.setSymbolValue(component, "SPI_TRANSFER_MODE", "0x20000000", 2)
        else:
            symbol.setLabel("***SPI Transfer Mode 3 is Selected***")
            Database.setSymbolValue(component, "SPI_TRANSFER_MODE", "0x30000000", 2)

#SPI Clock Phase property
def set_SPI_CPHA_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Clock Polarity property
def set_SPI_CPOL_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Data order property
def set_SPI_DORD_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Character size property
def set_SPI_CHSIZE_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI master slave select Enable Property
def set_SPI_MASTER_SSEN_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Receiver Enable Property
def set_SPI_CTRLB_RXEN_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI baud rate value selection Property
def set_SPI_BAUDRATE_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Master clock Freq selection Property
def set_SPI_MasterClockFreq_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Interrupt mode selection property
def set_SPI_InterruptMode_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#SPI Serial Setup property
def set_SPI_SERIALSETUP_VisibleProperty(symbol, event):
    if event["value"] == 0x3:
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

###################################################################################################
############################################# SPI #################################################
###################################################################################################

global spiSym_Interrupt_Mode

#SPI Interrupt Mode
spiSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", sercomSym_OperationMode)
spiSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
spiSym_Interrupt_Mode.setDefaultValue(True)
spiSym_Interrupt_Mode.setVisible(False)
spiSym_Interrupt_Mode.setDependencies(set_SPI_InterruptMode_VisibleProperty, ["SERCOM_MODE"])

#SPI Standby Mode
spiSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("SPI_RUNSTDBY", sercomSym_OperationMode)
spiSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
spiSym_CTRLA_RUNSTDBY.setVisible(False)
spiSym_CTRLA_RUNSTDBY.setDependencies(setspiSTANDBYVisibleProperty, ["SERCOM_MODE"])

#SPI DataOut PinOut
spiSym_CTRLA_DOPO = sercomComponent.createKeyValueSetSymbol("SPI_DOPO", sercomSym_OperationMode)
spiSym_CTRLA_DOPO.setLabel("SPI Data Out Pad")
spiSym_CTRLA_DOPO.setVisible(False)

spiDOPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DOPO\"]")
spiDOPOValues = []
spiDOPOValues = spiDOPONode.getChildren()

for index in range(len(spiDOPOValues)):
    spiDOPOKeyName = spiDOPOValues[index].getAttribute("name")
    spiDOPOKeyDescription = spiDOPOValues[index].getAttribute("caption")
    spiDOPOKeyValue = spiDOPOValues[index].getAttribute("value")
    spiSym_CTRLA_DOPO.addKey(spiDOPOKeyName, spiDOPOKeyValue, spiDOPOKeyDescription)

spiSym_CTRLA_DOPO.setDefaultValue(0)
spiSym_CTRLA_DOPO.setOutputMode("Value")
spiSym_CTRLA_DOPO.setDisplayMode("Description")
spiSym_CTRLA_DOPO.setDependencies(set_SPI_DOPO_VisibleProperty, ["SERCOM_MODE"])

#SPI DataIn pinOut
spiSym_CTRLA_DIPO = sercomComponent.createKeyValueSetSymbol("SPI_DIPO", sercomSym_OperationMode)
spiSym_CTRLA_DIPO.setLabel("SPI Data In Pad Selection")
spiSym_CTRLA_DIPO.setVisible(False)

spiDIPONode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DIPO\"]")
spiDIPOValues = []
spiDIPOValues = spiDIPONode.getChildren()

for index in range(len(spiDIPOValues)):
    spiDIPOKeyName = spiDIPOValues[index].getAttribute("name")
    spiDIPOKeyDescription = spiDIPOValues[index].getAttribute("caption")
    spiDIPOKeyValue = spiDIPOValues[index].getAttribute("value")
    spiSym_CTRLA_DIPO.addKey(spiDIPOKeyName, spiDIPOKeyValue, spiDIPOKeyDescription)

spiSym_CTRLA_DIPO.setDefaultValue(0)
spiSym_CTRLA_DIPO.setOutputMode("Value")
spiSym_CTRLA_DIPO.setDisplayMode("Description")
spiSym_CTRLA_DIPO.setDependencies(set_SPI_DIPO_VisibleProperty, ["SERCOM_MODE"])

#SPI Data Order
spiSym_CTRLA_DORD = sercomComponent.createKeyValueSetSymbol("SPI_DATA_ORDER", sercomSym_OperationMode)
spiSym_CTRLA_DORD.setLabel("SPI Data Order")
spiSym_CTRLA_DORD.setVisible(False)

spiDORDNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_SPIM_CTRLA__DORD\"]")
spiDORDValues = []
spiDORDValues = spiDORDNode.getChildren()

for index in range(len(spiDORDValues)):
    spiDORDKeyName = spiDORDValues[index].getAttribute("name")
    spiDORDKeyDescription = spiDORDValues[index].getAttribute("caption")
    spiDORDKeyValue = spiDORDValues[index].getAttribute("value")
    spiSym_CTRLA_DORD.addKey(spiDORDKeyName, spiDORDKeyValue, spiDORDKeyDescription)

spiSym_CTRLA_DORD.setDefaultValue(0)
spiSym_CTRLA_DORD.setOutputMode("Key")
spiSym_CTRLA_DORD.setDisplayMode("Description")
spiSym_CTRLA_DORD.setDependencies(set_SPI_DORD_VisibleProperty, ["SERCOM_MODE"])

#SPI BaudRate Value
spi_BAUDRATE = sercomComponent.createIntegerSymbol("SPI_BAUD_RATE", sercomSym_OperationMode)
spi_BAUDRATE.setLabel("SPI Speed in Hz")
spi_BAUDRATE.setDefaultValue(1000000)
spi_BAUDRATE.setVisible(False)
spi_BAUDRATE.setDependencies(set_SPI_BAUDRATE_VisibleProperty, ["SERCOM_MODE"])

#SPI Character Size
spiSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("SPI_CHARSIZE_BITS", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE.setLabel("SPI Data Character Size")
spiSym_CTRLB_CHSIZE.setVisible(False)
spiSym_CTRLB_CHSIZE.addKey("_8_BIT", "0x0", "8 bits for transfer")
spiSym_CTRLB_CHSIZE.addKey("_9_BIT", "0x1", "9 bits for transfer")
spiSym_CTRLB_CHSIZE.setDefaultValue(0)
spiSym_CTRLB_CHSIZE.setOutputMode("Key")
spiSym_CTRLB_CHSIZE.setDisplayMode("Description")
spiSym_CTRLB_CHSIZE.setDependencies(set_SPI_CHSIZE_VisibleProperty, ["SERCOM_MODE"])

#SPI 8-bit Character size Mask
spiSym_CTRLB_CHSIZE_8BIT = sercomComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE_8BIT.setDefaultValue("0x0")
spiSym_CTRLB_CHSIZE_8BIT.setVisible(False)

#SPI 9-bit Character size Mask
spiSym_CTRLB_CHSIZE_9BIT = sercomComponent.createStringSymbol("SPI_CHARSIZE_BITS_9_BIT_MASK", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE_9BIT.setDefaultValue("0x1")
spiSym_CTRLB_CHSIZE_9BIT.setVisible(False)

#SPI Clock Phase
spiSym_CTRLA_ClockPhase = sercomComponent.createKeyValueSetSymbol("SPI_CLOCK_PHASE", sercomSym_OperationMode)
spiSym_CTRLA_ClockPhase.setLabel("SPI Clock Phase")
spiSym_CTRLA_ClockPhase.setVisible(False)
spiSym_CTRLA_ClockPhase.addKey("VALID_LEADING_EDGE", "0x0", "The data is sampled on a leading SCK edge and changed on a trailing SCK edge")
spiSym_CTRLA_ClockPhase.addKey("VALID_TRAILING_EDGE", "0x1", "The data is sampled on a trailing SCK edge and changed on a leading SCK edge")
spiSym_CTRLA_ClockPhase.setDefaultValue(0)
spiSym_CTRLA_ClockPhase.setOutputMode("Key")
spiSym_CTRLA_ClockPhase.setDisplayMode("Description")
spiSym_CTRLA_ClockPhase.setDependencies(set_SPI_CPHA_VisibleProperty, ["SERCOM_MODE"])

#SPI Clock Phase Trailing Edge Mask
spiSym_CTRLA_CPHA_LE_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPHA_LE_Mask.setDefaultValue("0x0")
spiSym_CTRLA_CPHA_LE_Mask.setVisible(False)

#SPI Clock Phase Leading Edge Mask
spiSym_CTRLA_CPHA_TE_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPHA_TE_Mask.setDefaultValue("0x10000000")
spiSym_CTRLA_CPHA_TE_Mask.setVisible(False)

#SPI Clock Polarity
spiSym_CTRLA_ClockPolarity = sercomComponent.createKeyValueSetSymbol("SPI_CLOCK_POLARITY", sercomSym_OperationMode)
spiSym_CTRLA_ClockPolarity.setLabel("SPI Clock Polarity")
spiSym_CTRLA_ClockPolarity.setVisible(False)
spiSym_CTRLA_ClockPolarity.addKey("IDLE_LOW", "0x0", "SCK is low when idle")
spiSym_CTRLA_ClockPolarity.addKey("IDLE_HIGH", "0x1", "SCK is high when idle")
spiSym_CTRLA_ClockPolarity.setDefaultValue(0)
spiSym_CTRLA_ClockPolarity.setOutputMode("Key")
spiSym_CTRLA_ClockPolarity.setDisplayMode("Description")
spiSym_CTRLA_ClockPolarity.setDependencies(set_SPI_CPOL_VisibleProperty, ["SERCOM_MODE"])

#SPI Clock Polarity Idle Low Mask
spiSym_CTRLA_CPOL_IL_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPOL_IL_Mask.setDefaultValue("0x0")
spiSym_CTRLA_CPOL_IL_Mask.setVisible(False)

#SPI Clock Polarity Idle High Mask
spiSym_CTRLA_CPOL_IH_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPOL_IH_Mask.setDefaultValue("0x20000000")
spiSym_CTRLA_CPOL_IH_Mask.setVisible(False)

#SPI Status OVERRUN Mask
spiSym_STATUS_BUFOVF_Mask = sercomComponent.createStringSymbol("SPI_STATUS_OVERRUN_MASK", sercomSym_OperationMode)
spiSym_STATUS_BUFOVF_Mask.setDefaultValue("0x4")
spiSym_STATUS_BUFOVF_Mask.setVisible(False)

#SPI Transfer Mode
spiSym_CTRLA_TRANSFER_MODE = sercomComponent.createStringSymbol("SPI_TRANSFER_MODE", sercomSym_OperationMode)
spiSym_CTRLA_TRANSFER_MODE.setLabel("SPI Transfer Mode")
spiSym_CTRLA_TRANSFER_MODE.setDefaultValue("0x0")
spiSym_CTRLA_TRANSFER_MODE.setVisible(False)

#SPI Hardware Slave Select control
spiSym_CTRLB_MSSEN = sercomComponent.createBooleanSymbol("SPI_MSSEN", sercomSym_OperationMode)
spiSym_CTRLB_MSSEN.setLabel("Enable SPI Master Hardware Slave Select")
spiSym_CTRLB_MSSEN.setVisible(False)
spiSym_CTRLB_MSSEN.setDependencies(set_SPI_MASTER_SSEN_VisibleProperty, ["SERCOM_MODE"])

#SPI Receiver Enable
spiSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("SPI_RECIEVER_ENABLE", sercomSym_OperationMode)
spiSym_CTRLB_RXEN.setLabel("SPI Receiver Enable")
spiSym_CTRLB_RXEN.setDefaultValue(True)
spiSym_CTRLB_RXEN.setVisible(False)
spiSym_CTRLB_RXEN.setDependencies(set_SPI_CTRLB_RXEN_VisibleProperty, ["SERCOM_MODE"])

#SPI Serial Setup API Enable
spiSym_TRANSFERSETUP = sercomComponent.createBooleanSymbol("SPI_TRANSFER_SETUP_ENABLE", sercomSym_OperationMode)
spiSym_TRANSFERSETUP.setLabel("Generate Transfer Setup API")
spiSym_TRANSFERSETUP.setDefaultValue(True)
spiSym_TRANSFERSETUP.setVisible(False)
spiSym_TRANSFERSETUP.setDependencies(set_SPI_SERIALSETUP_VisibleProperty, ["SERCOM_MODE"])

#SPI API Prefix
spiSym_API_Prefix = sercomComponent.createStringSymbol("SPI_PLIB_API_PREFIX", sercomSym_OperationMode)
spiSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_SPI")
spiSym_API_Prefix.setVisible(False)

# SPI Clock Mode
spiSym_ClockModeComment = sercomComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", sercomSym_OperationMode)
spiSym_ClockModeComment.setLabel("***SPI Transfer Mode 0 is Selected***")
spiSym_ClockModeComment.setVisible(False)
spiSym_ClockModeComment.setDependencies(setSPIClockModeInfo, ["SERCOM_MODE", "SPI_CLOCK_PHASE", "SPI_CLOCK_POLARITY"])
