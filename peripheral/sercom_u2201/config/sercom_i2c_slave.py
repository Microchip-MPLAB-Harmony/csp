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

global updateSDASetupRegisterValue
global updateSDASetupTimeMaxValueInNanoSeconds

def updateSDASetupTimeMaxValueInNanoSeconds():
    sda_setup_reg_max_value = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CS_SDASETUP_MAX_VALUE"))
    cpu_clk_frequency = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    if cpu_clk_frequency > 0:
        cpu_clk_period = 1.0/cpu_clk_frequency
        sda_setup_time_ns = (cpu_clk_period) * (6 + (16*sda_setup_reg_max_value))
        return int(sda_setup_time_ns*1e9)
    else:
        return 0

def updateSDASetupRegisterValue():
    sda_setup_time_ns = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CS_SDASETUP_TIME_NS")) * 1e-9
    cpu_clk_frequency = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    sda_setup_reg_value = ((sda_setup_time_ns * cpu_clk_frequency) - 6 )/16
    if sda_setup_reg_value < 0:
        sda_setup_reg_value = 0
    Database.setSymbolValue(sercomInstanceName.getValue().lower(), "I2CS_SDASETUP_TIME_REG_VALUE", int(sda_setup_reg_value))

# I2CS Components Visible Property
def updateI2CSlaveConfigurationVisibleProperty(symbol, event):

    if event["id"] == "I2CS_TENBITEN_SUPPORT":
        eventSym = event["symbol"]
        if eventSym.getValue() == True:
            symbol.setLabel("I2C Slave Address (10-bit)")
        else:
            symbol.setLabel("I2C Slave Address (7-bit)")
    elif symbol.getID() == "I2CS_SDASETUP_TIME_NS":
        updateSDASetupRegisterValue()
        symbol.setMax(updateSDASetupTimeMaxValueInNanoSeconds())

    symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CS")

def updateI2CClockStretchConfigValue(symbol, event):

    # Enable SCLSM to 1 if High Speed mode is enabled
    if event["symbol"].getValue() == True:
        symbol.setValue(1)
    else:
        symbol.setValue(0)

def updateSmartModeVisibility(symbol, event):

    if event["id"] == "I2CS_MODE":
        if event["symbol"].getValue() == 0x02:
            symbol.setReadOnly(True)
            symbol.setValue(True)
        else:
            symbol.setReadOnly(False)
            symbol.setValue(False)

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

global speedSupported
speedSupported = False

ctrlaNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="CTRLA"]')
ctrlaValue = ctrlaNode.getChildren()

for index in range(len(ctrlaValue)):
    bitFieldName = str(ctrlaValue[index].getAttribute("name"))
    if bitFieldName == "SPEED":
        speedSupported = True
        break

if speedSupported == True:
    # I2C Transfer Speed Mode
    i2csSym_mode = sercomComponent.createKeyValueSetSymbol("I2CS_MODE", sercomSym_OperationMode)
    i2csSym_mode.setLabel("Transfer Speed Mode")
    i2csSym_mode.setVisible(False)

    i2csTransferSpeedNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/value-group@[name="SERCOM_I2CM_CTRLA__SPEED"]')
    i2csTransferSpeedNodeValues = i2csTransferSpeedNode.getChildren()

    for index in range((len(i2cmTransferSpeedNodeValues))):
        i2csTransferSpeedKeyName = i2csTransferSpeedNodeValues[index].getAttribute("name")
        i2csTransferSpeedKeyValue = i2csTransferSpeedNodeValues[index].getAttribute("value")
        i2csTransferSpeedKeyDescription = i2csTransferSpeedNodeValues[index].getAttribute("caption")
        i2csSym_mode.addKey(i2csTransferSpeedKeyName, i2csTransferSpeedKeyValue, i2csTransferSpeedKeyDescription)

    i2csSym_mode.setDefaultValue(0)
    i2csSym_mode.setOutputMode("Key")
    i2csSym_mode.setDisplayMode("Key")
    i2csSym_mode.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["SERCOM_MODE"])

# I2C Smart Mode Enable
i2csSym_CTRLB_SMEN = sercomComponent.createBooleanSymbol("I2CS_SMEN", sercomSym_OperationMode)
i2csSym_CTRLB_SMEN.setLabel("Enable Smart Mode")
i2csSym_CTRLB_SMEN.setDefaultValue(False)
i2csSym_CTRLB_SMEN.setVisible(False)
i2csSym_CTRLB_SMEN.setDependencies(updateSmartModeVisibility, ["SERCOM_MODE", "I2CS_MODE"])

global sclsmSupported
sclsmSupported = False

# Check if different SCL clock stretching modes are supported
for index in range(len(ctrlaValue)):
    bitFieldName = str(ctrlaValue[index].getAttribute("name"))
    if bitFieldName == "SCLSM":
        sclsmSupported = True
        break

if sclsmSupported == True:
    i2csSym_CTRLA_SCLSM = sercomComponent.createIntegerSymbol("I2CS_SCLSM", sercomSym_OperationMode)
    i2csSym_CTRLA_SCLSM.setLabel("Clock Stretch Mode")
    i2csSym_CTRLA_SCLSM.setVisible(False)
    i2csSym_CTRLA_SCLSM.setDefaultValue(0)
    i2csSym_CTRLA_SCLSM.setDependencies(updateI2CClockStretchConfigValue, ["I2CS_HIGH_SPEED_MODE"])
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
# SDA Setup Time
sdaSetupTimeSupported = False
sdaSetupTimeMask = 0
sdaSetupTimeReferenceNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]')

sdaSetupTimeValue = sdaSetupTimeReferenceNode.getChildren()

# Check if CTRLC register exists
for index in range(len(sdaSetupTimeValue)):
    if str(sdaSetupTimeValue[index].getAttribute("modes")) == "I2CS":
        if str(sdaSetupTimeValue[index].getAttribute("name")) == "CTRLC":
            sdaSetupTimeSupported = True
            break

# Check if CTRLC register has the SDASETUP bitfield.
if sdaSetupTimeSupported == True:
    sdaSetupTimeSupported = False
    sdaSetupTimeReferenceNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CS",name="CTRLC"]')
    sdaSetupTimeValue = sdaSetupTimeReferenceNode.getChildren()
    for index in range(len(sdaSetupTimeValue)):
        if str(sdaSetupTimeValue[index].getAttribute("name")) == "SDASETUP":
            sdaSetupTimeMask = int(sdaSetupTimeValue[index].getAttribute("mask"), 16)
            i2csSym_SDASETUP_MaxValue = sercomComponent.createIntegerSymbol("I2CS_SDASETUP_MAX_VALUE", sercomSym_OperationMode)
            i2csSym_SDASETUP_MaxValue.setLabel("SDA Setup Time Max Register Value")
            i2csSym_SDASETUP_MaxValue.setVisible(False)
            i2csSym_SDASETUP_MaxValue.setDefaultValue(sdaSetupTimeMask)
            sdaSetupTimeSupported = True
            break

# CTRLC register exists and has SDASETUP bitfield
if sdaSetupTimeSupported == True:
    i2csSym_SDASETUP = sercomComponent.createBooleanSymbol("I2CS_SDASETUP_TIME_SUPPORT", sercomSym_OperationMode)
    i2csSym_SDASETUP.setVisible(False)
    i2csSym_SDASETUP.setValue(True)

    i2csSym_SDASETUP_Value = sercomComponent.createIntegerSymbol("I2CS_SDASETUP_TIME_NS", sercomSym_OperationMode)
    i2csSym_SDASETUP_Value.setLabel("SDA Setup Time (ns)")
    i2csSym_SDASETUP_Value.setVisible(False)
    i2csSym_SDASETUP_Value.setMin(0)
    i2csSym_SDASETUP_Value.setDefaultValue(250)
    i2csSym_SDASETUP_Value.setDependencies(updateI2CSlaveConfigurationVisibleProperty, ["I2CS_SDASETUP_TIME_NS", "SERCOM_MODE", "core.CPU_CLOCK_FREQUENCY"])

    i2csSym_SDASETUP_RegValue = sercomComponent.createIntegerSymbol("I2CS_SDASETUP_TIME_REG_VALUE", sercomSym_OperationMode)
    i2csSym_SDASETUP_RegValue.setLabel("SDA Setup Time Register Value")
    i2csSym_SDASETUP_RegValue.setVisible(False)
    i2csSym_SDASETUP_RegValue.setDefaultValue(0)
    i2csSym_SDASETUP_RegValue.setMax(sdaSetupTimeMask)
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
i2csSym_ADDR.setMin(0)
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