# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
global qspiSym_BAUD_CPOL_IL_Mask
global qspiSym_BAUD_CPOL_IH_Mask

global dummyDataDict
dummyDataDict = {
                    "_8_BIT"     :   0xFF,
                    "_9_BIT"     :   0x1FF,
                    "_10_BIT"    :   0x3FF,
                    "_11_BIT"    :   0x7FF,
                    "_12_BIT"    :   0xFFF,
                    "_13_BIT"    :   0x1FFF,
                    "_14_BIT"    :   0x3FFF,
                    "_15_BIT"    :   0x7FFF,
                    "_16_BIT"    :   0xFFFF
                }


def setClockPolarity(symbol, event):
    # callback for setting clock polarity symbols needed, based on user selection
    symObj=event["symbol"]
    if(symObj.getSelectedKey() == "LOW"):
        qspiSym_BAUD_CPOL_IL_Mask.setValue("0x0", 1)
        qspiSym_BAUD_CPOL_IH_Mask.setValue("0x1", 1)
    else:
        qspiSym_BAUD_CPOL_IL_Mask.setValue("0x1", 1)
        qspiSym_BAUD_CPOL_IH_Mask.setValue("0x0", 1)


def DummyData_ValueUpdate(spiSymDummyData, event):
    spiSymDummyData.setValue(dummyDataDict[event["symbol"].getKey(event["value"])], 1)
    spiSymDummyData.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])

###################################################################################################
######################################## QSPI IN SPI MODE #########################################
###################################################################################################
qspiRegModule = Register.getRegisterModule("QSPI")
qspiRegGroup = qspiRegModule.getRegisterGroup("QSPI")
qspiReg_CTRLB = qspiRegGroup.getRegister("CTRLB")
qspiBitField_CTRLB_DATALEN = qspiReg_CTRLB.getBitfield("DATALEN")
qspiValGrp_CTRLB_DATALEN = qspiRegModule.getValueGroup(qspiBitField_CTRLB_DATALEN.getValueGroupName())
qspiBitField_CTRLB_LOOPEN = qspiReg_CTRLB.getBitfield("LOOPEN")
qspiValGrp_CTRLB_LOOPEN = qspiRegModule.getValueGroup(qspiBitField_CTRLB_LOOPEN.getValueGroupName())

# number of bits per transfer
count = qspiValGrp_CTRLB_DATALEN.getValueCount()
qspiDATALEN = qspiComponent.createKeyValueSetSymbol("QSPI_DATALEN", qspiMenu)
qspiDATALEN.setLabel(qspiBitField_CTRLB_DATALEN.getDescription())
qspiDATALEN.setVisible(True)
qspiDATALEN.setOutputMode("Value")
qspiDATALEN.setDisplayMode("Description")
qspiDATALEN.setSelectedKey("16BITS",1)
qspiDATALEN.setReadOnly(False)
for id in range(0,count):
    valueName = qspiValGrp_CTRLB_DATALEN.getValueNames()[id]
    qspiDATALEN.addKey(valueName, qspiValGrp_CTRLB_DATALEN.getValue(valueName).getValue(), qspiValGrp_CTRLB_DATALEN.getValue(valueName).getDescription())

# loopback mode
count = qspiValGrp_CTRLB_LOOPEN.getValueCount()
qspiLOOPEN = qspiComponent.createKeyValueSetSymbol("QSPI_LOOPEN", qspiMenu)
qspiLOOPEN.setLabel(qspiBitField_CTRLB_LOOPEN.getDescription())
qspiLOOPEN.setVisible(True)
qspiLOOPEN.setOutputMode("Value")
qspiLOOPEN.setDisplayMode("Description")
qspiLOOPEN.setSelectedKey("DISABLED",1)
qspiLOOPEN.setReadOnly(False)
for id in range(0,count):
    valueName = qspiValGrp_CTRLB_LOOPEN.getValueNames()[id]
    qspiLOOPEN.addKey(valueName, qspiValGrp_CTRLB_LOOPEN.getValue(valueName).getValue(), qspiValGrp_CTRLB_LOOPEN.getValue(valueName).getDescription())

#SPI Transmit data register
transmitRegister = qspiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
transmitRegister.setDefaultValue("&("+qspiInstanceName.getValue()+"_REGS->TXDATA)")
transmitRegister.setVisible(False)

#SPI Receive data register
receiveRegister = qspiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
receiveRegister.setDefaultValue("&("+qspiInstanceName.getValue()+"_REGS->RXDATA)")
receiveRegister.setVisible(False)

#SPI 8-bit Character size Mask
qspiSym_CSR_BITS_8BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
qspiSym_CSR_BITS_8BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_8BIT.setVisible(False)

#SPI 9-bit Character size Mask
qspiSym_CSR_BITS_9BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_9_BIT_MASK", None)
qspiSym_CSR_BITS_9BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_9BIT.setVisible(False)

#SPI 10-bit Character size Mask
qspiSym_CSR_BITS_10BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_10_BIT_MASK", None)
qspiSym_CSR_BITS_10BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_10BIT.setVisible(False)

#SPI 11-bit Character size Mask
qspiSym_CSR_BITS_11BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_11_BIT_MASK", None)
qspiSym_CSR_BITS_11BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_11BIT.setVisible(False)

#SPI 12-bit Character size Mask
qspiSym_CSR_BITS_12BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_12_BIT_MASK", None)
qspiSym_CSR_BITS_12BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_12BIT.setVisible(False)

#SPI 13-bit Character size Mask
qspiSym_CSR_BITS_13BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_13_BIT_MASK", None)
qspiSym_CSR_BITS_13BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_13BIT.setVisible(False)

#SPI 14-bit Character size Mask
qspiSym_CSR_BITS_14BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_14_BIT_MASK", None)
qspiSym_CSR_BITS_14BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_14BIT.setVisible(False)

#SPI 15-bit Character size Mask
qspiSym_CSR_BITS_15BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_15_BIT_MASK", None)
qspiSym_CSR_BITS_15BIT.setDefaultValue("0x0")
qspiSym_CSR_BITS_15BIT.setVisible(False)

#SPI 16-bit Character size Mask
qspiSym_CSR_BITS_16BIT = qspiComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", None)
qspiSym_CSR_BITS_16BIT.setDefaultValue("0x80")
qspiSym_CSR_BITS_16BIT.setVisible(False)

#SPI Clock Polarity Idle Low Mask
qspiSym_BAUD_CPOL_IL_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
qspiSym_BAUD_CPOL_IL_Mask.setDefaultValue("0x0")
qspiSym_BAUD_CPOL_IL_Mask.setVisible(False)

#SPI Clock Polarity Idle High Mask
qspiSym_BAUD_CPOL_IH_Mask = qspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
qspiSym_BAUD_CPOL_IH_Mask.setDefaultValue("0x1")
qspiSym_BAUD_CPOL_IH_Mask.setVisible(False)

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