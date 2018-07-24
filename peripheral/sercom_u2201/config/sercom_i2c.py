###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

# I2CM Run StandBy Visible Property
def seti2cmRunStandByVisibleProperty(symbol, event):
    if event["value"] == 0x5:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# I2CM SDAHOLD Time Visible Property
def seti2cmSDAHoldTimeVisibleProperty(symbol, event):
    if event["value"] == 0x5:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# I2CM Speed Visible Property
def seti2cmSpeedVisibleProperty(symbol, event):
    if event["value"] == 0x5:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

# Set Number of Transaction Request Block Visible Property
def seti2cmNumberTRBsVisibleProperty(symbol, event):
    if event["value"] == 0x5:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
############################################# I2C #################################################
###################################################################################################

# Number of Transaction request blocks
i2cmSym_NumTRBs = sercomComponent.createIntegerSymbol("I2CM_NUM_TRBS", sercomSym_OperationMode)
i2cmSym_NumTRBs.setLabel("Number of Transfer Request Blocks (TRBs)")
i2cmSym_NumTRBs.setMin(2)
i2cmSym_NumTRBs.setMax(255)
i2cmSym_NumTRBs.setDefaultValue(2)
i2cmSym_NumTRBs.setVisible(False)
i2cmSym_NumTRBs.setDependencies(seti2cmNumberTRBsVisibleProperty, ["SERCOM_MODE"])

# RunIn Standby
i2cmSym_CTRLA_RUNSTDBY = sercomComponent.createBooleanSymbol("I2C_RUNSTDBY", sercomSym_OperationMode)
i2cmSym_CTRLA_RUNSTDBY.setLabel("Enable operation in Standby mode")
i2cmSym_CTRLA_RUNSTDBY.setVisible(False)
i2cmSym_CTRLA_RUNSTDBY.setDependencies(seti2cmRunStandByVisibleProperty, ["SERCOM_MODE"])

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

i2cmSym_CTRLA_SDAHOLD.setDefaultValue(0)
i2cmSym_CTRLA_SDAHOLD.setOutputMode("Value")
i2cmSym_CTRLA_SDAHOLD.setDisplayMode("Description")
i2cmSym_CTRLA_SDAHOLD.setDependencies(seti2cmSDAHoldTimeVisibleProperty,["SERCOM_MODE"])

# Operating speed
i2cmSym_BAUD = sercomComponent.createIntegerSymbol("I2C_CLOCK_SPEED", sercomSym_OperationMode)
i2cmSym_BAUD.setLabel("I2C Speed in KHz")
i2cmSym_BAUD.setMin(100)
i2cmSym_BAUD.setMax(400)
i2cmSym_BAUD.setDefaultValue(100)
i2cmSym_BAUD.setVisible(False)
i2cmSym_BAUD.setDependencies(seti2cmSpeedVisibleProperty, ["SERCOM_MODE"])
