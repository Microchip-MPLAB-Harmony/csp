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

def getI2CBaudValue():

    global desiredI2CBaudRate

    baud = 0
    mode = 0
    refClkFreq = int(Database.getSymbolValue("core", sercomClkFrequencyId))
    clkSpeed = int(Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2C_CLOCK_SPEED")) * 1000
    trise = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CM_TRISE")

    if speedSupported == True:
        mode = Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CM_MODE")

    # Check if baudrate is outside of valid range
    if refClkFreq >= (2 * clkSpeed):
        desiredI2CBaudRate = True
        i2cmSym_BaudError_Comment.setVisible(False)

        baudlow = int(round(((refClkFreq / clkSpeed) * (1 - float("{0:.15f}".format(float(trise * clkSpeed) / 1000000000)))) - 10))

        if baudlow >= (0xFF * 2) or (baudlow <= 1):
            baud = 0
        else:
            if mode == 0:
                baud = ((baudlow / 2) + (((baudlow / 2) + 1) << 8)) if(baudlow & 0x1) \
                else (baudlow / 2)
            else:
                baud = ((baudlow / 3) + ((((2 * baudlow) / 3) + 1) << 8)) if(baudlow & 0x1) \
                else (baudlow / 3)
    else:
        desiredI2CBaudRate = False
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

# baud rate calc
def updateI2CBaudValueProperty(symbol, event):

    symbol.setValue(getI2CBaudValue(), 1)

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
    i2cmSym_mode.setVisible(False)

    i2cmTransferSpeedNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/value-group@[name="SERCOM_I2CM_CTRLA__SPEED"]')
    i2cmTransferSpeedNodeValues = i2cmTransferSpeedNode.getChildren()

    for index in range((len(i2cmTransferSpeedNodeValues) - 1)):
        i2cmTransferSpeedKeyName = i2cmTransferSpeedNodeValues[index].getAttribute("name")
        i2cmTransferSpeedKeyValue = i2cmTransferSpeedNodeValues[index].getAttribute("value")
        i2cmTransferSpeedKeyDescription = i2cmTransferSpeedNodeValues[index].getAttribute("caption")
        i2cmSym_mode.addKey(i2cmTransferSpeedKeyName, i2cmTransferSpeedKeyValue, i2cmTransferSpeedKeyDescription)

    i2cmSym_mode.setDefaultValue(0)
    i2cmSym_mode.setOutputMode("Key")
    i2cmSym_mode.setDisplayMode("Key")
    i2cmSym_mode.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# Run In Standby
i2cmSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("I2C_RUNSTDBY", sercomSym_OperationMode)
i2cmSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
i2cmSym_CTRLA_RUNSTDBY.setVisible(False)
i2cmSym_CTRLA_RUNSTDBY.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# SDA Hold Time
i2cmSym_CTRLA_SDAHOLD = sercomComponent.createKeyValueSetSymbol("I2C_SDAHOLD_TIME", sercomSym_OperationMode)
i2cmSym_CTRLA_SDAHOLD.setLabel("SDA Hold Time")
i2cmSym_CTRLA_SDAHOLD.setVisible(False)

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
i2cmSym_CTRLA_SDAHOLD.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# Operating speed
i2cmSym_BAUD = sercomComponent.createIntegerSymbol("I2C_CLOCK_SPEED", sercomSym_OperationMode)
i2cmSym_BAUD.setLabel("I2C Speed in KHz")
i2cmSym_BAUD.setMin(1)
if speedSupported == True:
    i2cmSym_BAUD.setMax(1000)
else:
    i2cmSym_BAUD.setMax(400)
i2cmSym_BAUD.setDefaultValue(100)
i2cmSym_BAUD.setVisible(False)
i2cmSym_BAUD.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# I2C BAUD register value
i2cmSym_TRISEVALUE = sercomComponent.createIntegerSymbol("I2CM_TRISE", sercomSym_OperationMode)
i2cmSym_TRISEVALUE.setLabel("I2C Trise in nano seconds")
i2cmSym_TRISEVALUE.setMin(1)
i2cmSym_TRISEVALUE.setMax(1000)
i2cmSym_TRISEVALUE.setDefaultValue(100)
i2cmSym_TRISEVALUE.setVisible(False)
i2cmSym_TRISEVALUE.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

# I2C BAUD register value
i2cmSym_BAUDREGVALUE = sercomComponent.createIntegerSymbol("I2CM_BAUD", sercomSym_OperationMode)
i2cmSym_BAUDREGVALUE.setLabel("I2C BAUD")
i2cmSym_BAUDREGVALUE.setVisible(False)
i2cmSym_BAUDREGVALUE.setReadOnly(True)
if speedSupported == True:
    i2cmSym_BAUDREGVALUE.setDependencies(updateI2CBaudValueProperty, ["I2C_CLOCK_SPEED", "I2CM_TRISE", "core." + sercomClkFrequencyId])
else:
    i2cmSym_BAUDREGVALUE.setDependencies(updateI2CBaudValueProperty, ["I2CM_MODE", "I2C_CLOCK_SPEED", "I2CM_TRISE", "core." + sercomClkFrequencyId])

#I2C Baud Rate not supported comment
global i2cmSym_BaudError_Comment
i2cmSym_BaudError_Comment = sercomComponent.createCommentSymbol("I2C_BAUD_ERROR_COMMENT", sercomSym_OperationMode)
i2cmSym_BaudError_Comment.setLabel("********** value is not suitable for the desired baud rate **********")
i2cmSym_BaudError_Comment.setVisible(False)
i2cmSym_BaudError_Comment.setDependencies(updateI2CMasterConfigurationVisibleProperty, ["SERCOM_MODE"])

tenBitAddrSupported = False

addrNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="I2CM",name="ADDR"]')
addrValue = addrNode.getChildren()

for index in range(len(addrValue)):
    bitFieldName = str(addrValue[index].getAttribute("name"))
    if bitFieldName == "TENBITEN":
        tenBitAddrSupported = True
        break

#I2C 10-bit Address support
i2cSym_TENBITEN = sercomComponent.createBooleanSymbol("I2C_ADDR_TENBITEN", sercomSym_OperationMode)
i2cSym_TENBITEN.setDefaultValue(tenBitAddrSupported)
i2cSym_TENBITEN.setVisible(False)

#Use setValue instead of setDefaultValue to store symbol value in default.xml
i2cmSym_BAUDREGVALUE.setValue(getI2CBaudValue(), 1)

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

#I2C API Prefix
i2cSym_API_Prefix = sercomComponent.createStringSymbol("I2C_PLIB_API_PREFIX", sercomSym_OperationMode)
i2cSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_I2C")
i2cSym_API_Prefix.setVisible(False)