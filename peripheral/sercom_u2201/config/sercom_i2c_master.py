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

global getI2CBaudValue
global getCalculatedI2CClockSpeed

global transferModeBaud

transferModeBaud = {
    # Transfer Mode value : Max baud value
    0:400,
    1:1000,
    2:3400
}

def getCalculatedI2CClockSpeed(f_gclk, trise, baud):
    global desiredI2CBaudRate
    desiredI2CBaudRate = False
    f_scl = int(f_gclk/(10 + baud + float("{0:.15f}".format(float(trise * f_gclk) / 1000000000))))
    return f_scl

def getI2CBaudValue():

    global desiredI2CBaudRate

    baud = 0
    mode = 0
    calculated_f_scl = -1
    f_gclk = int(Database.getSymbolValue("core", sercomClkFrequencyId))
    f_scl = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2C_CLOCK_SPEED")) * 1000
    trise = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CM_TRISE")

    # Standard mode = 100 KHz, Fast mode = upto 400 KHz, Fast mode plus = upto 1 MHz
    # Fast Mode Plus requires SCL High:SCL Low = 1:2
    # Baud.baudlow != 0, SCL Low controlled by Baud.baudlow, SCL High controlled by Baud.baud
    # Baud.baudlow = 0, SCL Low and SCL High are controlled by Baud.baud
    # Mode = 0 covers Standard and Fast mode, Mode = 1 covers Fast Mode Plus

    if speedSupported == True:
        mode = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CM_MODE")

    # Check if baudrate is outside of valid range
    if f_gclk >= (2 * f_scl):
        desiredI2CBaudRate = True
        i2cmSym_BaudError_Comment.setVisible(False)

        if (mode == 2):
            # For HS mode, the master code is transmitted at 400 kHz. After calculating HS mode baud, force f_scl to 400kHz
            # calculate the baud for master code transmission
            hs_baudValue = int(round(((f_gclk / f_scl) - 2)))
            f_scl = 400000

        baudValue = int(round(((f_gclk / f_scl) * (1 - float("{0:.15f}".format(float(trise * f_scl) / 1000000000)))) - 10))

        if (mode == 0):
            if baudValue >= (0xFF * 2):
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, (0xFF * 2))
                baud = 0xFF
            elif baudValue <= 1:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 2)
                baud = 1
            else:
                baud = baudValue/2
        elif (mode == 1):
            if baudValue >= 382:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 382)
                baud = (255 << 8) | 127
            elif baudValue <= 3:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 3)
                baud = (2 << 8) | 1
            else:
                baud = ((baudValue * 2)/3) << 8
                baud |= (baudValue/3)
        else:
            if baudValue >= (0xFF * 2):
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, (0xFF * 2))
                baud = 0xFF
            elif baudValue <= 1:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 2)
                baud = 1
            else:
                baud = baudValue/2

            if hs_baudValue >= 382:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 382)
                baud |= ((255 << 8) | 127) << 16
            elif hs_baudValue <= 3:
                calculated_f_scl = getCalculatedI2CClockSpeed(f_gclk, trise, 3)
                baud |= ((2 << 8) | 1) << 16
            else:
                baud |= ((hs_baudValue * 2)/3) << 24
                baud |= (hs_baudValue/3) << 16

        if desiredI2CBaudRate == False:
            i2cmSym_BaudError_Comment.setLabel("**** Achievable I2C Clock Frequency = " + str(calculated_f_scl) + "Hz")
            i2cmSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
    else:
        desiredI2CBaudRate = False
        i2cmSym_BaudError_Comment.setLabel("**** Reference Clock Frequency too low for generating the desired I2C Clock ")
        i2cmSym_BaudError_Comment.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")

    return baud

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

# I2CM Components Visible Property
def updateI2CMasterConfigurationVisibleProperty(symbol, event):

    global desiredI2CBaudRate

    if symbol.getID() == "I2C_BAUD_ERROR_COMMENT":
        symbol.setVisible(desiredI2CBaudRate == False and sercomSym_OperationMode.getSelectedKey() == "I2CM")
    else:
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")

def baudDependencyChanged(symbol, event):
    global transferModeBaud

    if event["id"] == "SERCOM_MODE":
        symbol.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
    else:
        baudMax = transferModeBaud[event["value"]]
        symbol.setMax(baudMax)

# baud rate calc
def updateI2CBaudValueProperty(symbol, event):

    symbol.setValue(getI2CBaudValue(), 1)

def updateI2CClockStretchConfigValue(symbol, event):

    # Enable SCLSM to 1 if High Speed mode is enabled
    if event["symbol"].getValue() == 0x02:
        symbol.setValue(1)
    else:
        symbol.setValue(0)

def updateI2CMasterCodeVisiblity(symbol, event):

    if event["symbol"].getValue() == 0x02:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateI2CBaudHz(symbol, event):
    symbol.setValue(event["value"] * 1000)
###################################################################################################
######################################## I2C MASTER ###############################################
###################################################################################################

global i2cSym_Interrupt_Mode

#I2C Interrupt Mode
i2cSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("I2C_INTERRUPT_MODE", sercomSym_OperationMode)
i2cSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
i2cSym_Interrupt_Mode.setDefaultValue(True)
i2cSym_Interrupt_Mode.setVisible(False)

global speedSupported
speedSupported = False

ctrlaNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CM",name="CTRLA"]')
ctrlaValue = ctrlaNode.getChildren()

for index in range(len(ctrlaValue)):
    bitFieldName = str(ctrlaValue[index].getAttribute("name"))
    if bitFieldName == "SPEED":
        speedSupported = True
        break

if speedSupported == True:
    # I2C Transfer Speed Mode
    i2cmSym_mode = sercomComponent.createKeyValueSetSymbol("I2CM_MODE", sercomSym_OperationMode)
    i2cmSym_mode.setLabel("Transfer Speed Mode")

    i2cmTransferSpeedNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/value-group@[name="SERCOM_I2CM_CTRLA__SPEED"]')
    i2cmTransferSpeedNodeValues = i2cmTransferSpeedNode.getChildren()

    for index in range((len(i2cmTransferSpeedNodeValues))):
        i2cmTransferSpeedKeyName = i2cmTransferSpeedNodeValues[index].getAttribute("name")
        i2cmTransferSpeedKeyValue = i2cmTransferSpeedNodeValues[index].getAttribute("value")
        i2cmTransferSpeedKeyDescription = i2cmTransferSpeedNodeValues[index].getAttribute("caption")
        i2cmSym_mode.addKey(i2cmTransferSpeedKeyName, i2cmTransferSpeedKeyValue, i2cmTransferSpeedKeyDescription)

    i2cmSym_mode.setDefaultValue(0)
    i2cmSym_mode.setOutputMode("Key")
    i2cmSym_mode.setDisplayMode("Key")
    i2cmSym_mode.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
    i2cmSym_mode.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

    i2cmSym_HSMasterCode = sercomComponent.createIntegerSymbol("I2C_MASTER_CODE", sercomSym_OperationMode)
    i2cmSym_HSMasterCode.setLabel("Master Code (0-7)")
    i2cmSym_HSMasterCode.setVisible(False)
    i2cmSym_HSMasterCode.setMin(0)
    i2cmSym_HSMasterCode.setMax(7)
    i2cmSym_HSMasterCode.setDefaultValue(1)
    i2cmSym_HSMasterCode.setDependencies(updateI2CMasterCodeVisiblity, ["I2CM_MODE"])

global sclsmSupported
sclsmSupported = False

# Check if different SCL clock stretching modes are supported
for index in range(len(ctrlaValue)):
    bitFieldName = str(ctrlaValue[index].getAttribute("name"))
    if bitFieldName == "SCLSM":
        sclsmSupported = True
        break

if sclsmSupported == True:
    i2cmSym_CTRLA_SCLSM = sercomComponent.createIntegerSymbol("I2C_SCLSM", sercomSym_OperationMode)
    i2cmSym_CTRLA_SCLSM.setLabel("Clock Stretch Mode")
    i2cmSym_CTRLA_SCLSM.setVisible(False)
    i2cmSym_CTRLA_SCLSM.setDefaultValue(0)
    i2cmSym_CTRLA_SCLSM.setDependencies(updateI2CClockStretchConfigValue, ["I2CM_MODE"])

# Run In Standby
i2cmSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("I2C_RUNSTDBY", sercomSym_OperationMode)
i2cmSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
i2cmSym_CTRLA_RUNSTDBY.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
i2cmSym_CTRLA_RUNSTDBY.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# SDA Hold Time
i2cmSym_CTRLA_SDAHOLD = sercomComponent.createKeyValueSetSymbol("I2C_SDAHOLD_TIME", sercomSym_OperationMode)
i2cmSym_CTRLA_SDAHOLD.setLabel("SDA Hold Time")

i2cmSDAHoldTimeReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_I2CM_CTRLA__SDAHOLD\"]")
i2cmSDAHoldTimeReferenceValues = i2cmSDAHoldTimeReferenceNode.getChildren()

for index in range(len(i2cmSDAHoldTimeReferenceValues)):
    i2cmSDAHoldTimeReferenceKeyName = i2cmSDAHoldTimeReferenceValues[index].getAttribute("name")
    i2cmSDAHoldTimeReferenceKeyDescription = i2cmSDAHoldTimeReferenceValues[index].getAttribute("caption")
    i2cmSDAHoldTimeReferenceKeyValue = i2cmSDAHoldTimeReferenceValues[index].getAttribute("value")
    i2cmSym_CTRLA_SDAHOLD.addKey(i2cmSDAHoldTimeReferenceKeyName, i2cmSDAHoldTimeReferenceKeyValue, i2cmSDAHoldTimeReferenceKeyDescription)

i2cmSym_CTRLA_SDAHOLD.setDefaultValue(1)
i2cmSym_CTRLA_SDAHOLD.setOutputMode("Key")
i2cmSym_CTRLA_SDAHOLD.setDisplayMode("Description")
i2cmSym_CTRLA_SDAHOLD.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
i2cmSym_CTRLA_SDAHOLD.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# Operating speed
i2cmSym_BAUD = sercomComponent.createIntegerSymbol("I2C_CLOCK_SPEED", sercomSym_OperationMode)
i2cmSym_BAUD.setLabel("I2C Speed in KHz")
i2cmSym_BAUD.setMin(1)
i2cmSym_BAUD.setMax(400)
if speedSupported == True:
    maxBaud = transferModeBaud[i2cmSym_mode.getValue()]
    i2cmSym_BAUD.setMax(maxBaud)

i2cmSym_BAUD.setDefaultValue(100)
i2cmSym_BAUD.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
i2cmSym_BAUD.setDependencies(baudDependencyChanged, ["SERCOM_MODE", "I2CM_MODE"])

# Operating speed (Hz)
i2cmSym_BAUD_Hz = sercomComponent.createIntegerSymbol("I2C_CLOCK_SPEED_HZ", sercomSym_OperationMode)
i2cmSym_BAUD_Hz.setLabel("I2C Speed in Hz")
i2cmSym_BAUD_Hz.setDefaultValue(i2cmSym_BAUD.getValue() * 1000)
i2cmSym_BAUD_Hz.setVisible(False)
i2cmSym_BAUD_Hz.setDependencies(updateI2CBaudHz, ["I2C_CLOCK_SPEED"])

# I2C BAUD register value
i2cmSym_TRISEVALUE = sercomComponent.createIntegerSymbol("I2CM_TRISE", sercomSym_OperationMode)
i2cmSym_TRISEVALUE.setLabel("I2C Trise in nano seconds")
i2cmSym_TRISEVALUE.setMin(1)
i2cmSym_TRISEVALUE.setMax(1000)
i2cmSym_TRISEVALUE.setDefaultValue(100)
i2cmSym_TRISEVALUE.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
i2cmSym_TRISEVALUE.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# I2C BAUD register value
i2cmSym_BAUDREGVALUE = sercomComponent.createHexSymbol("I2CM_BAUD", sercomSym_OperationMode)
i2cmSym_BAUDREGVALUE.setLabel("I2C BAUD")
i2cmSym_BAUDREGVALUE.setVisible(False)
i2cmSym_BAUDREGVALUE.setReadOnly(True)
i2cmSym_BAUDREGVALUE.setHexOutputMode(True)
if speedSupported == True:
    i2cmSym_BAUDREGVALUE.setDependencies(updateI2CBaudValueProperty, ["I2CM_MODE", "I2C_CLOCK_SPEED", "I2CM_TRISE", "core." + sercomClkFrequencyId])
else:
    i2cmSym_BAUDREGVALUE.setDependencies(updateI2CBaudValueProperty, ["I2C_CLOCK_SPEED", "I2CM_TRISE", "core." + sercomClkFrequencyId])

#I2C Baud Rate not supported comment
global i2cmSym_BaudError_Comment
i2cmSym_BaudError_Comment = sercomComponent.createCommentSymbol("I2C_BAUD_ERROR_COMMENT", sercomSym_OperationMode)
i2cmSym_BaudError_Comment.setLabel("********** value is not suitable for the desired baud rate **********")
i2cmSym_BaudError_Comment.setVisible(False)
i2cmSym_BaudError_Comment.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

slewRateSupported = False

for index in range(len(ctrlaValue)):
    bitFieldName = str(ctrlaValue[index].getAttribute("name"))
    if bitFieldName == "SLEWRATE":
        slewRateSupported = True
        break

# SLEW RATE Control
if slewRateSupported == True:
    i2cmSym_CTRLA_SLEWRATE = sercomComponent.createKeyValueSetSymbol("I2C_SLEWRATE", sercomSym_OperationMode)
    i2cmSym_CTRLA_SLEWRATE.setLabel("I2C Slew Rate Control")

    i2cmSlewRateReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_I2CM_CTRLA__SLEWRATE\"]")
    i2cmSlewRateReferenceValues = i2cmSlewRateReferenceNode.getChildren()

    for index in range(len(i2cmSlewRateReferenceValues)):
        i2cmSlewRateReferenceKeyName = i2cmSlewRateReferenceValues[index].getAttribute("name")
        i2cmSlewRateReferenceKeyDescription = i2cmSlewRateReferenceValues[index].getAttribute("caption")
        i2cmSlewRateReferenceKeyValue = i2cmSlewRateReferenceValues[index].getAttribute("value")
        i2cmSym_CTRLA_SLEWRATE.addKey(i2cmSlewRateReferenceKeyName, i2cmSlewRateReferenceKeyValue, i2cmSlewRateReferenceKeyDescription)

    i2cmSym_CTRLA_SLEWRATE.setDefaultValue(1)
    i2cmSym_CTRLA_SLEWRATE.setOutputMode("Key")
    i2cmSym_CTRLA_SLEWRATE.setDisplayMode("Description")
    i2cmSym_CTRLA_SLEWRATE.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
    i2cmSym_CTRLA_SLEWRATE.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

tenBitAddrSupported = False

addrNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CM",name="ADDR"]')
addrValue = addrNode.getChildren()

for index in range(len(addrValue)):
    bitFieldName = str(addrValue[index].getAttribute("name"))
    if bitFieldName == "TENBITEN":
        tenBitAddrSupported = True
        break

#I2C 10-bit Address support
if tenBitAddrSupported == True:
    i2cSym_TENBITEN = sercomComponent.createBooleanSymbol("I2C_ADDR_TENBITEN", sercomSym_OperationMode)
    i2cSym_TENBITEN.setLabel("Enable 10-bit Addressing")
    i2cSym_TENBITEN.setDefaultValue(False)
    i2cSym_TENBITEN.setVisible(sercomSym_OperationMode.getSelectedKey() == "I2CM")
    i2cSym_TENBITEN.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

#Use setValue instead of setDefaultValue to store symbol value in default.xml
i2cmSym_BAUDREGVALUE.setValue(getI2CBaudValue(), 1)

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#I2C API Prefix
i2cSym_API_Prefix = sercomComponent.createStringSymbol("I2C_PLIB_API_PREFIX", sercomSym_OperationMode)
i2cSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_I2C")
i2cSym_API_Prefix.setVisible(False)