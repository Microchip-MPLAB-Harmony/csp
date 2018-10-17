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


# I2CM Components Visible Property
def sercomi2cComponentVisibleProperty(symbol, event):
    if event["value"] == 0x5:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# baud rate calc
def baudRateCalc(symbol,event):

    gclk_Freq = Database.getSymbolValue("core",sercomInstanceName.getValue() + "_CORE_CLOCK_FREQUENCY")
    clk_Speed = Database.getSymbolValue(sercomInstanceName.getValue().lower() ,"I2C_CLOCK_SPEED")
    i2cm_Trise = Database.getSymbolValue(sercomInstanceName.getValue().lower(),"I2CM_TRISE")
    clk_Genr_Mode = Database.getSymbolValue(sercomInstanceName.getValue().lower(),"I2CM_MODE")

    clk_Speed = (int(clk_Speed) * 1000)
    baudReg = geti2cBaud(gclk_Freq,clk_Speed,i2cm_Trise,int(clk_Genr_Mode))

    if baudReg != None:
        symbol.setValue(baudReg,2)

###################################################################################################
############################################# I2C #################################################
###################################################################################################

global i2cSym_Interrupt_Mode

#I2C Interrupt Mode
i2cSym_Interrupt_Mode = sercomComponent.createBooleanSymbol("I2C_INTERRUPT_MODE", sercomSym_OperationMode)
i2cSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
i2cSym_Interrupt_Mode.setDefaultValue(True)
i2cSym_Interrupt_Mode.setVisible(False)

# I2C Mode
i2cValGrp_I2CM_CTRLA__SPEED = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/value-group@[name="SERCOM_I2CM_CTRLA__SPEED"]')
i2cmSym_mode = sercomComponent.createKeyValueSetSymbol("I2CM_MODE", sercomSym_OperationMode)
i2cmSym_mode.setLabel(i2cValGrp_I2CM_CTRLA__SPEED.getAttribute("caption"))
i2cmSym_mode.setOutputMode("Value")
i2cmSym_mode.setDisplayMode("Key")
i2cmSym_mode.setVisible(False)
i2cmSym_mode.setDefaultValue(0)

for id in range(0, (len(i2cValGrp_I2CM_CTRLA__SPEED.getChildren())-1)):
        valueName = i2cValGrp_I2CM_CTRLA__SPEED.getChildren()[id].getAttribute("name")
        value = i2cValGrp_I2CM_CTRLA__SPEED.getChildren()[id].getAttribute("value")
        description = i2cValGrp_I2CM_CTRLA__SPEED.getChildren()[id].getAttribute("caption")
        i2cmSym_mode.addKey(valueName, value, description)
i2cmSym_mode.setDependencies(sercomi2cComponentVisibleProperty, ["SERCOM_MODE"])

# RunIn Standby
i2cmSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("I2C_RUNSTDBY", sercomSym_OperationMode)
i2cmSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
i2cmSym_CTRLA_RUNSTDBY.setVisible(False)
i2cmSym_CTRLA_RUNSTDBY.setDependencies(sercomi2cComponentVisibleProperty, ["SERCOM_MODE"])

# SDA Hold Time
i2cmSym_CTRLA_SDAHOLD = sercomComponent.createKeyValueSetSymbol("I2C_SDAHOLD_TIME", sercomSym_OperationMode)
i2cmSym_CTRLA_SDAHOLD.setLabel("SDA Hold Time")
i2cmSym_CTRLA_SDAHOLD.setVisible(False)

i2cmSDAHoldTimeReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]/value-group@[name=\"SERCOM_I2CM_CTRLA__SDAHOLD\"]")
i2cmSDAHoldTimeReferenceValues = []
i2cmSDAHoldTimeReferenceValues = i2cmSDAHoldTimeReferenceNode.getChildren()

for index in range(len(i2cmSDAHoldTimeReferenceValues)):
    i2cmSDAHoldTimeReferenceKeyName = i2cmSDAHoldTimeReferenceValues[index].getAttribute("name")
    i2cmSDAHoldTimeReferenceKeyDescription = i2cmSDAHoldTimeReferenceValues[index].getAttribute("caption")
    i2cmSDAHoldTimeReferenceKeyValue = i2cmSDAHoldTimeReferenceValues[index].getAttribute("value")
    i2cmSym_CTRLA_SDAHOLD.addKey(i2cmSDAHoldTimeReferenceKeyName, i2cmSDAHoldTimeReferenceKeyValue, i2cmSDAHoldTimeReferenceKeyDescription)

i2cmSym_CTRLA_SDAHOLD.setDefaultValue(1)
i2cmSym_CTRLA_SDAHOLD.setOutputMode("Value")
i2cmSym_CTRLA_SDAHOLD.setDisplayMode("Description")
i2cmSym_CTRLA_SDAHOLD.setDependencies(sercomi2cComponentVisibleProperty,["SERCOM_MODE"])

# Operating speed
i2cmSym_BAUD = sercomComponent.createIntegerSymbol("I2C_CLOCK_SPEED", sercomSym_OperationMode)
i2cmSym_BAUD.setLabel("I2C Speed in KHz")
i2cmSym_BAUD.setMin(1)
i2cmSym_BAUD.setMax(1000)
i2cmSym_BAUD.setDefaultValue(100)
i2cmSym_BAUD.setVisible(False)
i2cmSym_BAUD.setDependencies(sercomi2cComponentVisibleProperty, ["SERCOM_MODE"])

#I2C API Prefix
i2cSym_API_Prefix = sercomComponent.createStringSymbol("I2C_PLIB_API_PREFIX", sercomSym_OperationMode)
i2cSym_API_Prefix.setDefaultValue(sercomInstanceName.getValue() + "_I2C")
i2cSym_API_Prefix.setVisible(False)


# I2C BAUD register value
i2cmSym_TRISEVALUE = sercomComponent.createIntegerSymbol("I2CM_TRISE", sercomSym_OperationMode)
i2cmSym_TRISEVALUE.setLabel("I2C Trise in nano seconds")
i2cmSym_TRISEVALUE.setMin(1)
i2cmSym_TRISEVALUE.setMax(1000)
i2cmSym_TRISEVALUE.setDefaultValue(100)
i2cmSym_TRISEVALUE.setVisible(False)
i2cmSym_TRISEVALUE.setDependencies(sercomi2cComponentVisibleProperty, ["SERCOM_MODE"])

baudRegValue = geti2cBaud(Database.getSymbolValue("core",sercomInstanceName.getValue() + "_CORE_CLOCK_FREQUENCY"),i2cmSym_BAUD.getValue()*1000,i2cmSym_TRISEVALUE.getValue(),i2cmSym_mode.getValue())

# I2C BAUD register value
i2cmSym_BAUDREGVALUE = sercomComponent.createIntegerSymbol("I2CM_BAUD", sercomSym_OperationMode)
i2cmSym_BAUDREGVALUE.setLabel("I2C BAUD")
i2cmSym_BAUDREGVALUE.setDefaultValue(baudRegValue)
i2cmSym_BAUDREGVALUE.setVisible(False)
i2cmSym_BAUDREGVALUE.setReadOnly(True)
i2cmSym_BAUDREGVALUE.setDependencies(baudRateCalc, ["I2CM_MODE","I2C_CLOCK_SPEED","core." +sercomInstanceName.getValue() + "_CORE_CLOCK_FREQUENCY","I2CM_TRISE"])
