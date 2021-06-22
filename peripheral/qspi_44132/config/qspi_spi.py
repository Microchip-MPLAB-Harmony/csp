# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
global qspiMenu
global qspiSMM
global qspiSym_CSR_CPOL_IL_Mask
global qspiSym_CSR_CPOL_IH_Mask

global dummyDataDict
dummyDataDict = {
                    "8_BIT"     :   0xFF,
                    "16_BIT"    :   0xFFFF
                }

def setClockPolarity(symbol, event):
    # callback for setting clock polarity symbols needed, based on user selection
    symObj=event["symbol"]
    if(symObj.getSelectedKey() == "LOW"):
        qspiSym_CSR_CPOL_IL_Mask.setValue("0x0")
        qspiSym_CSR_CPOL_IH_Mask.setValue("0x1")
    else:
        qspiSym_CSR_CPOL_IL_Mask.setValue("0x1")
        qspiSym_CSR_CPOL_IH_Mask.setValue("0x0")

def DummyData_ValueUpdate(spiSymDummyData, event):
    spiSymDummyData.setValue(dummyDataDict[event["symbol"].getKey(event["value"])])
    spiSymDummyData.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])

def symbolVisible(symbol, event):
    if event["symbol"].getSelectedKey() == "SPI":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
######################################## QSPI IN SPI MODE #########################################
###################################################################################################

qspiBitField_MR_NBBITS = qspiReg_MR.getBitfield("NBBITS")
qspiValGrp_MR_NBBITS = qspiRegModule.getValueGroup(qspiBitField_MR_NBBITS.getValueGroupName())

# number of bits per transfer
count = qspiValGrp_MR_NBBITS.getValueCount()
qspiNBBITS = qspiComponent.createKeyValueSetSymbol("QSPI_NBBITS", qspiMenu)
qspiNBBITS.setLabel(qspiBitField_MR_NBBITS.getDescription())
qspiNBBITS.setVisible(False)
qspiNBBITS.setOutputMode("Value")
qspiNBBITS.setDisplayMode("Description")
qspiNBBITS.setSelectedKey("16_BIT")
qspiNBBITS.setReadOnly(False)
for id in range(0,count):
    valueName = qspiValGrp_MR_NBBITS.getValueNames()[id]
    qspiNBBITS.addKey(valueName, qspiValGrp_MR_NBBITS.getValue(valueName).getValue(), qspiValGrp_MR_NBBITS.getValue(valueName).getDescription())
qspiNBBITS.setDependencies(symbolVisible, ["QSPI_SMM"])

#SPI Transmit data register
transmitRegister = qspiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
transmitRegister.setDefaultValue("&("+qspiInstanceName.getValue()+"_REGS->QSPI_TDR)")
transmitRegister.setVisible(False)

#SPI Receive data register
receiveRegister = qspiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
receiveRegister.setDefaultValue("&("+qspiInstanceName.getValue()+"_REGS->QSPI_RDR)")
receiveRegister.setVisible(False)

#SPI 8-bit Character size Mask
qspiSym_CSR_BITS_8BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
qspiSym_CSR_BITS_8BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_8BIT.setVisible(False)

#SPI 16-bit Character size Mask
qspiSym_CSR_BITS_16BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", None)
qspiSym_CSR_BITS_16BIT.setDefaultValue("0x80")
qspiSym_CSR_BITS_16BIT.setVisible(False)

#SPI Clock Polarity Idle Low Mask
qspiSym_CSR_CPOL_IL_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
qspiSym_CSR_CPOL_IL_Mask.setDefaultValue("0x0")
qspiSym_CSR_CPOL_IL_Mask.setVisible(False)

#SPI Clock Polarity Idle High Mask
qspiSym_CSR_CPOL_IH_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
qspiSym_CSR_CPOL_IH_Mask.setDefaultValue("0x1")
qspiSym_CSR_CPOL_IH_Mask.setVisible(False)

#SPI Clock Phase Leading Edge Mask
qspiSym_CSR_NCPHA_TE_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
qspiSym_CSR_NCPHA_TE_Mask.setDefaultValue("0x0")
qspiSym_CSR_NCPHA_TE_Mask.setVisible(False)

#SPI Clock Phase Trailing Edge Mask
qspiSym_CSR_NCPHA_LE_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
qspiSym_CSR_NCPHA_LE_Mask.setDefaultValue("0x2")
qspiSym_CSR_NCPHA_LE_Mask.setVisible(False)

qspiSymDummyData = qspiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
qspiSymDummyData.setVisible(False)
qspiSymDummyData.setLabel("Dummy Data")
qspiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
qspiSymDummyData.setDefaultValue(0xFFFF)
qspiSymDummyData.setMin(0x0)
qspiSymDummyData.setDependencies(DummyData_ValueUpdate, ["QSPI_NBBITS"])

#SPI API Prefix
qspiSym_API_Prefix = qspiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
qspiSym_API_Prefix.setDefaultValue(qspiInstanceName.getValue())
qspiSym_API_Prefix.setVisible(False)