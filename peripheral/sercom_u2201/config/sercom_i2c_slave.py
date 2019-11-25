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

# I2CS Components Visible Property
def updateI2CSlaveConfigurationVisibleProperty(symbol, event):

    if event["id"] == "I2CS_TENBITEN_SUPPORT":
        eventSym = event["symbol"]
        if eventSym.getValue() == True:
            symbol.setLabel("I2C Slave Address (10-bit)")
        else:
            symbol.setLabel("I2C Slave Address (7-bit)")
    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CS")


###################################################################################################
######################################## I2C MASTER ###############################################
###################################################################################################

global i2csSym_Interrupt_Mode
global i2csSym_CTRLB_SMEN

#I2C Interrupt Mode
i2csSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("I2CS_INTERRUPT_MODE", sercomSym_OperationMode)
i2csSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
i2csSym_Interrupt_Mode.setDefaultValue(True)
i2csSym_Interrupt_Mode.setVisible(False)
i2csSym_Interrupt_Mode.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

# I2C Smart Mode Enable
i2csSym_CTRLB_SMEN = sercomComponent.createBooleanSymbol("I2CS_SMEN", sercomSym_OperationMode)
i2csSym_CTRLB_SMEN.setLabel("Enable Smart Mode")
i2csSym_CTRLB_SMEN.setDefaultValue(False)
i2csSym_CTRLB_SMEN.setVisible(False)
i2csSym_CTRLB_SMEN.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#-----------------------------------------------------------------------------------
# SDA Hold Time
i2csSym_CTRLA_SDAHOLD = sercomComponent.createKeyValueSetSymbol("I2CS_SDAHOLD_TIME", sercomSym_OperationMode)
i2csSym_CTRLA_SDAHOLD.setLabel("SDA Hold Time")
i2csSym_CTRLA_SDAHOLD.setVisible(False)

i2csSDAHoldTimeReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_I2CM_CTRLA__SDAHOLD\"]")
i2csSDAHoldTimeReferenceValues = i2csSDAHoldTimeReferenceNode.getChildren()

for index in range(len(i2csSDAHoldTimeReferenceValues)):
    i2csSDAHoldTimeReferenceKeyName = i2csSDAHoldTimeReferenceValues[index].getAttribute("name")
    i2csSDAHoldTimeReferenceKeyDescription = i2csSDAHoldTimeReferenceValues[index].getAttribute("caption")
    i2csSDAHoldTimeReferenceKeyValue = i2csSDAHoldTimeReferenceValues[index].getAttribute("value")
    i2csSym_CTRLA_SDAHOLD.addKey(i2csSDAHoldTimeReferenceKeyName, i2csSDAHoldTimeReferenceKeyValue, i2csSDAHoldTimeReferenceKeyDescription)

i2csSym_CTRLA_SDAHOLD.setDefaultValue(1)
i2csSym_CTRLA_SDAHOLD.setOutputMode("Key")
i2csSym_CTRLA_SDAHOLD.setDisplayMode("Description")
i2csSym_CTRLA_SDAHOLD.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#-----------------------------------------------------------------------------------
# 10-bit support
TenBitAddrSupported = False
TenBitAddrSupportReferenceNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="ADDR"]')

TenBitSupportValue = TenBitAddrSupportReferenceNode.getChildren()

for index in range(len(TenBitSupportValue)):
    bitFieldName = str(TenBitSupportValue[index].getAttribute("name"))
    if bitFieldName == "TENBITEN":
        TenBitAddrSupported = True
        break

if TenBitAddrSupported == True:
    i2csSym_TENBITEN = sercomComponent.createBooleanSymbol("I2CS_TENBITEN_SUPPORT", sercomSym_OperationMode)
    i2csSym_TENBITEN.setLabel("Enable 10-bit Addressing")
    i2csSym_TENBITEN.setVisible(False)
    i2csSym_TENBITEN.setDefaultValue(False)
    i2csSym_TENBITEN.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

#-----------------------------------------------------------------------------------
# Slave Address
i2csSym_ADDR = sercomComponent.createHexSymbol("I2CS_SLAVE_ADDDRESS", sercomSym_OperationMode)
i2csSym_ADDR.setLabel("I2C Slave Address (7-bit)")
i2csSym_ADDR.setMax(1023)
i2csSym_ADDR.setVisible(False)
i2csSym_ADDR.setDefaultValue(0x54)
i2csSym_ADDR.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE", "I2CS_TENBITEN_SUPPORT"])

#-----------------------------------------------------------------------------------
# Error Interrupt Support
errorInterruptSupported = False

intensetNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="INTENSET"]')
intensetValue = intensetNode.getChildren()

for index in range(len(intensetValue)):
    bitFieldName = str(intensetValue[index].getAttribute("name"))
    if bitFieldName == "ERROR":
        errorInterruptSupported = True
        break

#I2CS is ERROR present
i2csSym_ERROR = sercomComponent.createBooleanSymbol("I2CS_INTENSET_ERROR", None)
i2csSym_ERROR.setVisible(False)
i2csSym_ERROR.setDefaultValue(errorInterruptSupported)

#-----------------------------------------------------------------------------------
# LOWTOUT Support
lowToutSupported = False
lowToutReferenceNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="CTRLA"]')

lowToutValue = lowToutReferenceNode.getChildren()

for index in range(len(lowToutValue)):
    bitFieldName = str(lowToutValue[index].getAttribute("name"))
    if bitFieldName == "LOWTOUTEN":
        lowToutSupported = True
        break

if lowToutSupported == True:
    i2csSym_LOWTOUT = sercomComponent.createBooleanSymbol("I2CS_LOWTOUT_SUPPORT", sercomSym_OperationMode)
    i2csSym_LOWTOUT.setLabel("Enable SCL Low Time-Out")
    i2csSym_LOWTOUT.setVisible(False)
    i2csSym_LOWTOUT.setDefaultValue(False)
    i2csSym_LOWTOUT.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])
#-----------------------------------------------------------------------------------
# SEXTTOEN Support
lowExtendToutSupported = False
lowExtendToutReferenceNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="CTRLA"]')

lowExtendToutValue = lowExtendToutReferenceNode.getChildren()

for index in range(len(lowExtendToutValue)):
    bitFieldName = str(lowExtendToutValue[index].getAttribute("name"))
    if bitFieldName == "SEXTTOEN":
        lowExtendToutSupported = True
        break

if lowExtendToutSupported == True:
    i2csSym_SEXTTOEN = sercomComponent.createBooleanSymbol("I2CS_SEXTTOEN_SUPPORT", sercomSym_OperationMode)
    i2csSym_SEXTTOEN.setLabel("Enable SCL Low Extend Time-Out")
    i2csSym_SEXTTOEN.setVisible(False)
    i2csSym_SEXTTOEN.setDefaultValue(False)
    i2csSym_SEXTTOEN.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])
#-----------------------------------------------------------------------------------
# LOWTOUT Error Status Support
i2csSym_LOWTOUTErrorStatus = sercomComponent.createBooleanSymbol("I2CS_LOWTOUT_ERROR_SUPPORT", None)
i2csSym_LOWTOUTErrorStatus.setVisible(False)
i2csSym_LOWTOUTErrorStatus.setDefaultValue(lowToutSupported)

#-----------------------------------------------------------------------------------
# SEXTTOUT Error Status Support
i2csSym_SEXTTOUTErrorStatus = sercomComponent.createBooleanSymbol("I2CS_SEXTTOOUT_ERROR_SUPPORT", None)
i2csSym_SEXTTOUTErrorStatus.setVisible(False)
i2csSym_SEXTTOUTErrorStatus.setDefaultValue(lowExtendToutSupported)

#-----------------------------------------------------------------------------------
# Run In Standby
i2csSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("I2CS_RUNSTDBY", sercomSym_OperationMode)
i2csSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
i2csSym_CTRLA_RUNSTDBY.setVisible(False)
i2csSym_CTRLA_RUNSTDBY.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])
#-----------------------------------------------------------------------------------

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#I2C API Prefix
i2cSym_API_Prefix = sercomComponent.createStringSymbol("I2CS_PLIB_API_PREFIX", sercomSym_OperationMode)
i2cSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_I2C")
i2cSym_API_Prefix.setVisible(False)