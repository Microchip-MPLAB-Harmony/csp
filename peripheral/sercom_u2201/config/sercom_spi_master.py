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

global getSPIBaudValue
global getValueGrp

def getSPIBaudValue():

    global desiredSPIBaudRate

    baud = 0

    refClkFreq = int(Database.getSymbolValue("core", sercomClkFrequencyId))
    baudRate = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "SPI_BAUD_RATE")

    # Check if baudrate is outside of valid range
    if refClkFreq >= (2 * baudRate):
        desiredSPIBaudRate = True
        spiSym_BaudError_Comment.setVisible(False)
        baud = int(round(float("{0:.15f}".format(float(refClkFreq / (2 * baudRate)))) - 1))
    else:
        desiredSPIBaudRate = False
        spiSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "SPIM")

    return baud

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

# SPI Components Visible Property
def updateSPIMasterConfigurationVisibleProperty(symbol, event):

    global desiredSPIBaudRate

    if symbol.getID() == "SPI_BAUD_ERROR_COMMENT":
        symbol.setVisible(desiredSPIBaudRate == False and sercomSym_OperationMode.getSelectedKey() == "SPIM")
    else:
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "SPIM")

#SPI BAUD Calculation
def updateSPIBaudValueProperty(symbol, event):

    symbol.setValue(getSPIBaudValue(), 1)

#SPI Transfer Mode Comment
def setSPIClockModeInfo(symbol, event):

    if event["id"] == "SERCOM_MODE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "SPIM")
    else:
        component = symbol.getComponent().getID()

        CPHA = Database.getSymbolValue(component, "SPI_CLOCK_PHASE")
        CPOL = Database.getSymbolValue(component, "SPI_CLOCK_POLARITY")

        if CPOL == 0 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 0 is Selected***")
        elif CPOL == 0 and CPHA == 1:
            symbol.setLabel("***SPI Transfer Mode 1 is Selected***")
        elif CPOL == 1 and CPHA == 0:
            symbol.setLabel("***SPI Transfer Mode 2 is Selected***")
        else:
            symbol.setLabel("***SPI Transfer Mode 3 is Selected***")

###################################################################################################
######################################## SPI MASTER ###############################################
###################################################################################################

global spiSym_Interrupt_Mode

#SPI Interrupt Mode
spiSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", sercomSym_OperationMode)
spiSym_Interrupt_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:%NOREGISTER%")
spiSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
spiSym_Interrupt_Mode.setDefaultValue(True)
spiSym_Interrupt_Mode.setVisible(False)
spiSym_Interrupt_Mode.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Standby Mode
spiSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("SPI_RUNSTDBY", sercomSym_OperationMode)
spiSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
spiSym_CTRLA_RUNSTDBY.setVisible(False)
spiSym_CTRLA_RUNSTDBY.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI DataOut PinOut
spiSym_CTRLA_DOPO = sercomComponent.createKeyValueSetSymbol("SPI_DOPO", sercomSym_OperationMode)
spiSym_CTRLA_DOPO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_DOPO.setLabel("SPI Data Out Pad")
spiSym_CTRLA_DOPO.setVisible(False)

spiDOPONode = getValueGrp("SERCOM", "SERCOM", "CTRLA", "DOPO", sercomSymSPIRegName.getValue())

spiDOPOValues = spiDOPONode.getChildren()

for index in range(len(spiDOPOValues)):
    spiDOPOKeyName = spiDOPOValues[index].getAttribute("name")
    spiDOPOKeyDescription = spiDOPOValues[index].getAttribute("caption")
    spiDOPOKeyValue = spiDOPOValues[index].getAttribute("value")
    spiSym_CTRLA_DOPO.addKey(spiDOPOKeyName, spiDOPOKeyValue, spiDOPOKeyDescription)

spiSym_CTRLA_DOPO.setDefaultValue(0)
spiSym_CTRLA_DOPO.setOutputMode("Key")
spiSym_CTRLA_DOPO.setDisplayMode("Description")
spiSym_CTRLA_DOPO.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI DataIn pinOut
spiSym_CTRLA_DIPO = sercomComponent.createKeyValueSetSymbol("SPI_DIPO", sercomSym_OperationMode)
spiSym_CTRLA_DIPO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_DIPO.setLabel("SPI Data In Pad Selection")
spiSym_CTRLA_DIPO.setVisible(False)

spiDIPONode = getValueGrp("SERCOM", "SERCOM", "CTRLA", "DIPO", sercomSymSPIRegName.getValue())
spiDIPOValues = spiDIPONode.getChildren()

for index in range(len(spiDIPOValues)):
    spiDIPOKeyName = spiDIPOValues[index].getAttribute("name")
    spiDIPOKeyDescription = spiDIPOValues[index].getAttribute("caption")
    spiDIPOKeyValue = spiDIPOValues[index].getAttribute("value")
    spiSym_CTRLA_DIPO.addKey(spiDIPOKeyName, spiDIPOKeyValue, spiDIPOKeyDescription)

spiSym_CTRLA_DIPO.setDefaultValue(0)
spiSym_CTRLA_DIPO.setOutputMode("Key")
spiSym_CTRLA_DIPO.setDisplayMode("Description")
spiSym_CTRLA_DIPO.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Data Order
spiSym_CTRLA_DORD = sercomComponent.createKeyValueSetSymbol("SPI_DATA_ORDER", sercomSym_OperationMode)
spiSym_CTRLA_DORD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_DORD.setLabel("SPI Data Order")
spiSym_CTRLA_DORD.setVisible(False)

spiDORDNode = getValueGrp("SERCOM", "SERCOM", "CTRLA", "DORD", sercomSymSPIRegName.getValue())
spiDORDValues = spiDORDNode.getChildren()

for index in range(len(spiDORDValues)):
    spiDORDKeyName = spiDORDValues[index].getAttribute("name")
    spiDORDKeyDescription = spiDORDValues[index].getAttribute("caption")
    spiDORDKeyValue = spiDORDValues[index].getAttribute("value")
    spiSym_CTRLA_DORD.addKey(spiDORDKeyName, spiDORDKeyValue, spiDORDKeyDescription)

spiSym_CTRLA_DORD.setDefaultValue(0)
spiSym_CTRLA_DORD.setOutputMode("Key")
spiSym_CTRLA_DORD.setDisplayMode("Description")
spiSym_CTRLA_DORD.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI BaudRate Value
spi_BAUDRATE = sercomComponent.createIntegerSymbol("SPI_BAUD_RATE", sercomSym_OperationMode)
spi_BAUDRATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:BAUD")
spi_BAUDRATE.setLabel("SPI Speed in Hz")
spi_BAUDRATE.setDefaultValue(1000000)
spi_BAUDRATE.setMin(1)
spi_BAUDRATE.setVisible(False)
spi_BAUDRATE.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#SPI Character Size
spiSym_CTRLB_CHSIZE = sercomComponent.createKeyValueSetSymbol("SPI_CHARSIZE_BITS", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
spiSym_CTRLB_CHSIZE.setLabel("SPI Data Character Size")
spiSym_CTRLB_CHSIZE.setVisible(False)

spiCHSIZENode = getValueGrp("SERCOM", "SERCOM", "CTRLB", "CHSIZE", sercomSymSPIRegName.getValue())
spiCHSIZEValues = spiCHSIZENode.getChildren()

for index in range(len(spiCHSIZEValues)):
    spiCHSIZEKeyName = spiCHSIZEValues[index].getAttribute("name")
    spiCHSIZEKeyDescription = spiCHSIZEValues[index].getAttribute("caption")
    spiCHSIZEKeyValue = spiCHSIZEValues[index].getAttribute("value")
    spiSym_CTRLB_CHSIZE.addKey(spiCHSIZEKeyName, spiCHSIZEKeyValue, spiCHSIZEKeyDescription)

spiSym_CTRLB_CHSIZE.setDefaultValue(0)
spiSym_CTRLB_CHSIZE.setOutputMode("Key")
spiSym_CTRLB_CHSIZE.setDisplayMode("Description")
spiSym_CTRLB_CHSIZE.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

spiDataBitsEnumList = sercomComponent.createListSymbol("SERCOM_SPI_DATA_BITS_ENUM_LIST", None)
spiDataBitsEnumList.setVisible(False)

spiDataBitsEnum = sercomComponent.createListEntrySymbol("SERCOM_SPI_DATA_BITS_ENUM", None)
spiDataBitsEnum.setVisible(False)
for i in range (0, 2):
    if int(spiCHSIZEValues[i].getAttribute("value"), 0) == 0:
        spiDataBitsEnumVal = "    SPI_DATA_BITS_8 = "
    else:
        spiDataBitsEnumVal = "    SPI_DATA_BITS_9 = "
    spiDataBitsEnumVal += "SERCOM_" + sercomSymSPIRegName.getValue() + "_CTRLB_CHSIZE_" + spiCHSIZEValues[i].getAttribute("name") + ","
    spiDataBitsEnum.addValue(spiDataBitsEnumVal)
    
spiDataBitsEnum.setTarget(sercomInstanceName.getValue().lower() + ".SERCOM_SPI_DATA_BITS_ENUM_LIST")

#SPI Clock Phase
spiSym_CTRLA_ClockPhase = sercomComponent.createKeyValueSetSymbol("SPI_CLOCK_PHASE", sercomSym_OperationMode)
spiSym_CTRLA_ClockPhase.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_ClockPhase.setLabel("SPI Clock Phase")
spiSym_CTRLA_ClockPhase.setVisible(False)

spiCLKPHASENode = getValueGrp("SERCOM", "SERCOM", "CTRLA", "CPHA", sercomSymSPIRegName.getValue())
spiCLKPHASEValues = spiCLKPHASENode.getChildren()

for index in range(len(spiCLKPHASEValues)):
    spiCLKPHASEKeyName = spiCLKPHASEValues[index].getAttribute("name")
    spiCLKPHASEKeyDescription = spiCLKPHASEValues[index].getAttribute("caption")
    spiCLKPHASEKeyValue = spiCLKPHASEValues[index].getAttribute("value")
    spiSym_CTRLA_ClockPhase.addKey(spiCLKPHASEKeyName, spiCLKPHASEKeyValue, spiCLKPHASEKeyDescription)

spiSym_CTRLA_ClockPhase.setDefaultValue(0)
spiSym_CTRLA_ClockPhase.setOutputMode("Key")
spiSym_CTRLA_ClockPhase.setDisplayMode("Description")
spiSym_CTRLA_ClockPhase.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

spiClkPhaseEnumList = sercomComponent.createListSymbol("SERCOM_SPI_CLOCK_PHASE_ENUM_LIST", None)
spiClkPhaseEnumList.setVisible(False)

spiClkPhaseEnums = sercomComponent.createListEntrySymbol("SERCOM_SPI_CLOCK_PHASE_ENUM", None)
spiClkPhaseEnums.setVisible(False)
for i in range (0, 2):
    if int(spiCLKPHASEValues[i].getAttribute("value"), 0) == 0:
        spiClkPhaseEnumVal = "    SPI_CLOCK_PHASE_LEADING_EDGE = "
    else:
        spiClkPhaseEnumVal = "    SPI_CLOCK_PHASE_TRAILING_EDGE = "
    spiClkPhaseEnumVal += "SERCOM_" + sercomSymSPIRegName.getValue() + "_CTRLA_CPHA_" + spiCLKPHASEValues[i].getAttribute("name") + ","
    spiClkPhaseEnums.addValue(spiClkPhaseEnumVal)
    
spiClkPhaseEnums.setTarget(sercomInstanceName.getValue().lower() + ".SERCOM_SPI_CLOCK_PHASE_ENUM_LIST")

#SPI Clock Polarity
spiSym_CTRLA_ClockPolarity = sercomComponent.createKeyValueSetSymbol("SPI_CLOCK_POLARITY", sercomSym_OperationMode)
spiSym_CTRLA_ClockPolarity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLA")
spiSym_CTRLA_ClockPolarity.setLabel("SPI Clock Polarity")
spiSym_CTRLA_ClockPolarity.setVisible(False)

spiCLKPLORITYNode = getValueGrp("SERCOM", "SERCOM", "CTRLA", "CPOL", sercomSymSPIRegName.getValue())
spiCLKPLORITYValues = spiCLKPLORITYNode.getChildren()

for index in range(len(spiCLKPLORITYValues)):
    spiCLKPLORITYKeyName = spiCLKPLORITYValues[index].getAttribute("name")
    spiCLKPLORITYKeyDescription = spiCLKPLORITYValues[index].getAttribute("caption")
    spiCLKPLORITYKeyValue = spiCLKPLORITYValues[index].getAttribute("value")
    spiSym_CTRLA_ClockPolarity.addKey(spiCLKPLORITYKeyName, spiCLKPLORITYKeyValue, spiCLKPLORITYKeyDescription)

spiSym_CTRLA_ClockPolarity.setDefaultValue(0)
spiSym_CTRLA_ClockPolarity.setOutputMode("Key")
spiSym_CTRLA_ClockPolarity.setDisplayMode("Description")
spiSym_CTRLA_ClockPolarity.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

spiClkPolarityEnumList = sercomComponent.createListSymbol("SERCOM_SPI_CLOCK_POLARITY_ENUM_LIST", None)
spiClkPolarityEnumList.setVisible(False)

spiClkPolarityEnums = sercomComponent.createListEntrySymbol("SERCOM_SPI_CLOCK_POLARITY_ENUM", None)
spiClkPolarityEnums.setVisible(False)
for i in range (0, 2):
    if int(spiCLKPLORITYValues[i].getAttribute("value"), 0) == 0:
        spiClkPolarityEnumVal = "    SPI_CLOCK_POLARITY_IDLE_LOW = "
    else:
        spiClkPolarityEnumVal = "    SPI_CLOCK_POLARITY_IDLE_HIGH = "
    spiClkPolarityEnumVal += "SERCOM_" + sercomSymSPIRegName.getValue() + "_CTRLA_CPOL_" + spiCLKPLORITYValues[i].getAttribute("name") + ","
    spiClkPolarityEnums.addValue(spiClkPolarityEnumVal)
spiClkPolarityEnums.setTarget(sercomInstanceName.getValue().lower() + ".SERCOM_SPI_CLOCK_POLARITY_ENUM_LIST")

global mssenSupported
mssenSupported = False

ctrlbNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="{0}",name="CTRLB"]'.format(sercomSymSPIRegName.getValue()))
ctrlbValue = ctrlbNode.getChildren()

for index in range(len(ctrlbValue)):
    bitFieldName = str(ctrlbValue[index].getAttribute("name"))
    if bitFieldName == "MSSEN":
        mssenSupported = True
        break

if mssenSupported == True:
    global spiSym_CTRLB_MSSEN
    #SPI Hardware Slave Select control
    spiSym_CTRLB_MSSEN = sercomComponent.createBooleanSymbol("SPI_MSSEN", sercomSym_OperationMode)
    spiSym_CTRLB_MSSEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
    spiSym_CTRLB_MSSEN.setLabel("Enable SPI Master Hardware Slave Select")
    spiSym_CTRLB_MSSEN.setVisible(False)
    spiSym_CTRLB_MSSEN.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

errorIntSupported = False

intensetNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="{0}",name="INTENSET"]'.format(sercomSymSPIRegName.getValue()))
intensetValue = intensetNode.getChildren()

for index in range(len(intensetValue)):
    bitFieldName = str(intensetValue[index].getAttribute("name"))
    if bitFieldName == "ERROR":
        errorIntSupported = True
        break

#SPI is ERROR present
spiSym_ERROR = sercomComponent.createBooleanSymbol("SPI_INTENSET_ERROR", None)
spiSym_ERROR.setVisible(False)
spiSym_ERROR.setDefaultValue(errorIntSupported)

#SPI Receiver Enable
spiSym_CTRLB_RXEN = sercomComponent.createBooleanSymbol("SPI_RECIEVER_ENABLE", sercomSym_OperationMode)
spiSym_CTRLB_RXEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:CTRLB")
spiSym_CTRLB_RXEN.setLabel("SPI Receiver Enable")
spiSym_CTRLB_RXEN.setDefaultValue(True)
spiSym_CTRLB_RXEN.setVisible(False)
spiSym_CTRLB_RXEN.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# SPI Clock Mode
spiSym_ClockModeComment = sercomComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", sercomSym_OperationMode)
spiSym_ClockModeComment.setLabel("***SPI Transfer Mode 0 is Selected***")
spiSym_ClockModeComment.setVisible(False)
spiSym_ClockModeComment.setDependencies(setSPIClockModeInfo, ["SERCOM_MODE", "SPI_CLOCK_PHASE", "SPI_CLOCK_POLARITY"])

#SPI Baud Rate not supported comment
global spiSym_BaudError_Comment
spiSym_BaudError_Comment = sercomComponent.createCommentSymbol("SPI_BAUD_ERROR_COMMENT", sercomSym_OperationMode)
spiSym_BaudError_Comment.setLabel("********** SPI Clock source is not suitable for the desired baud rate **********")
spiSym_BaudError_Comment.setVisible(False)
spiSym_BaudError_Comment.setDependencies(updateSPIMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# SPI BAUD REG Value
spi_BAUDREG = sercomComponent.createIntegerSymbol("SPI_BAUD_REG_VALUE", sercomSym_OperationMode)
spi_BAUDREG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sercom_u2201;register:BAUD")
spi_BAUDREG.setLabel("SPI Baud")
spi_BAUDREG.setVisible(False)
spi_BAUDREG.setDependencies(updateSPIBaudValueProperty, ["core." + sercomClkFrequencyId, "SPI_BAUD_RATE"])

#Use setValue instead of setDefaultValue to store symbol value in default.xml
spi_BAUDREG.setValue(getSPIBaudValue(), 1)

spiSym_CTRLA_MODE_Values = getValueGrp("SERCOM", "SERCOM", "CTRLA", "MODE", sercomSymSPIRegName.getValue()).getChildren()

spiSymMasterMode = sercomComponent.createStringSymbol("SPIM_MODE", sercomSym_OperationMode)
spiSymMasterMode.setVisible(False)
for index in range(len(spiSym_CTRLA_MODE_Values)):
    if int(spiSym_CTRLA_MODE_Values[index].getAttribute("value"), 0) == 3:
        spiSymMasterMode.setDefaultValue(spiSym_CTRLA_MODE_Values[index].getAttribute("name"))
        break

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#SPI API Prefix
spiSym_API_Prefix = sercomComponent.createStringSymbol("SPI_PLIB_API_PREFIX", sercomSym_OperationMode)
spiSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_SPI")
spiSym_API_Prefix.setVisible(False)

#SPI 8-bit Character size Mask
spiSym_CTRLB_CHSIZE_8BIT = sercomComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE_8BIT.setDefaultValue("0x0")
spiSym_CTRLB_CHSIZE_8BIT.setVisible(False)

#SPI 9-bit Character size Mask
spiSym_CTRLB_CHSIZE_9BIT = sercomComponent.createStringSymbol("SPI_CHARSIZE_BITS_9_BIT_MASK", sercomSym_OperationMode)
spiSym_CTRLB_CHSIZE_9BIT.setDefaultValue("0x1")
spiSym_CTRLB_CHSIZE_9BIT.setVisible(False)

#SPI Clock Phase Trailing Edge Mask
spiSym_CTRLA_CPHA_LE_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPHA_LE_Mask.setDefaultValue("0x0")
spiSym_CTRLA_CPHA_LE_Mask.setVisible(False)

#SPI Clock Phase Leading Edge Mask
spiSym_CTRLA_CPHA_TE_Mask = sercomComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", sercomSym_OperationMode)
spiSym_CTRLA_CPHA_TE_Mask.setDefaultValue("0x10000000")
spiSym_CTRLA_CPHA_TE_Mask.setVisible(False)

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