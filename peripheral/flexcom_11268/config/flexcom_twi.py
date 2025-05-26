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

################################################################################
#### Business Logic ####
################################################################################
global getFlexcomTwiClockDividerValue
global flexcomSym_Twi_OpMode
global flexcomSym_Twi_Interrupt

def getFlexcomTwiClockDividerValue(flexcomTwiClkSpeed):
    global flexcomSym_TWI_CWGR_BRSRCCLK

    ckdiv = 0
    clockDividerMaxValue = 255
    clockDividerMinValue = 7

    peripheralClockFreq = int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"))

    if flexcomSym_TWI_CWGR_BRSRCCLK.getSelectedKey() == "PERIPH_CLK":
        cldiv = peripheralClockFreq / ( flexcomTwiClkSpeed * 2 ) - 3
    else:
        cldiv = peripheralClockFreq / ( flexcomTwiClkSpeed * 2 )

    if flexcomSym_OperatingMode.getSelectedKey() == "TWI":
        flexcomClockInvalidSym.setVisible((cldiv < 1))

    while int(cldiv) > clockDividerMaxValue and ckdiv < clockDividerMinValue:
        ckdiv += 1
        cldiv /= 2
    chdiv = cldiv

    return int(cldiv), int(chdiv), ckdiv

def setFlexcomTwiClockDividerValue(symbol, event):
    cldiv, chdiv, ckdiv = getFlexcomTwiClockDividerValue(Database.getSymbolValue(deviceNamespace, "I2C_CLOCK_SPEED"))
    # set CLDIV Value
    Database.setSymbolValue(deviceNamespace, "FLEXCOM_TWI_CWGR_CLDIV", cldiv, 1)
    # set CHDIV Value
    Database.setSymbolValue(deviceNamespace, "FLEXCOM_TWI_CWGR_CHDIV", chdiv, 1)
    # set CKDIV Value
    Database.setSymbolValue(deviceNamespace, "FLEXCOM_TWI_CWGR_CKDIV", ckdiv, 1)

def setFlexcomTwiClockSourceFreq(symbol, event):
    symbol.setValue(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"), 1)

def symbolVisible(symbol, event):
    if flexcomSym_OperatingMode.getSelectedKey() == "TWI":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def showTwiDependencies(symbol, event):
    flexcom_mode = event["source"].getSymbolByID("FLEXCOM_MODE").getSelectedKey()
    twi_opmode = event["source"].getSymbolByID("FLEXCOM_TWI_OPMODE").getValue()

    if symbol.getID() == "TWI_INTERRUPT_MODE":
        symbol.setReadOnly(twi_opmode == "MASTER")
        if (twi_opmode == "MASTER"):
            symbol.setValue(True)
        symbol.setVisible(flexcom_mode == "TWI")
    else:
        symbol.setVisible(flexcom_mode == "TWI")

def showMasterDependencies(symbol, event):
    flexcom_mode = event["source"].getSymbolByID("FLEXCOM_MODE").getSelectedKey()
    twi_opmode = event["source"].getSymbolByID("FLEXCOM_TWI_OPMODE").getValue()

    symbol.setVisible(flexcom_mode == "TWI" and twi_opmode == "MASTER")

def showSlaveDependencies(symbol, event):
    flexcom_mode = event["source"].getSymbolByID("FLEXCOM_MODE").getSelectedKey()
    twi_opmode = event["source"].getSymbolByID("FLEXCOM_TWI_OPMODE").getValue()

    symbol.setVisible(flexcom_mode == "TWI" and twi_opmode == "SLAVE")

def twihsMasterModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "MASTER")

def twihsSlaveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "SLAVE")

def updateI2CBaudHz(symbol, event):
    symbol.setValue(event["value"])

def updateTimeoutCount(symbol, event):
    # Counter value obtained by dividing CPU clock frequency with 5000 gives a delay of 200usec (enough to transmit 10 bits of I2C running at 50 kHz).
    # 200usec delay assumes each instruction takes 1 CPU clock to execute. In practice the delay will be ~10 times higher, roughly 2-3 msec.
    symbol.setValue(int(event["value"])/5000)
###################################################################################################
############################################# FLEXCOM TWI #########################################
###################################################################################################

#Operation Mode
flexcomSym_Twi_OpModeValues = ["MASTER", "SLAVE"]
flexcomSym_Twi_OpMode = flexcomComponent.createComboSymbol("FLEXCOM_TWI_OPMODE", flexcomSym_OperatingMode, flexcomSym_Twi_OpModeValues)
flexcomSym_Twi_OpMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_MR")
flexcomSym_Twi_OpMode.setLabel("FLEXCOM TWI Operation Mode")
flexcomSym_Twi_OpMode.setDefaultValue("MASTER")
flexcomSym_Twi_OpMode.setVisible(False)
flexcomSym_Twi_OpMode.setDependencies(showTwiDependencies, ["FLEXCOM_MODE"])

#Interrupt Mode
flexcomSym_Twi_Interrupt = flexcomComponent.createBooleanSymbol("TWI_INTERRUPT_MODE", flexcomSym_OperatingMode)
flexcomSym_Twi_Interrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_TWI_IER")
flexcomSym_Twi_Interrupt.setLabel("Enable Interrupts ?")
flexcomSym_Twi_Interrupt.setDefaultValue(True)
flexcomSym_Twi_Interrupt.setReadOnly(True)
flexcomSym_Twi_Interrupt.setVisible(False)
flexcomSym_Twi_Interrupt.setDependencies(showTwiDependencies, ["FLEXCOM_TWI_OPMODE", "FLEXCOM_MODE"])

#Select clock source
global flexcomSym_TWI_CWGR_BRSRCCLK
flexcomSym_TWI_CWGR_BRSRCCLK = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_TWI_CWGR_BRSRCCLK", flexcomSym_OperatingMode)
flexcomSym_TWI_CWGR_BRSRCCLK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_TWI_CWGR")
flexcomSym_TWI_CWGR_BRSRCCLK.setLabel("Select Clock Source")
flexcomSym_TWI_CWGR_BRSRCCLK_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_TWI_CWGR__BRSRCCLK\"]")
flexcomSym_TWI_CWGR_BRSRCCLK_Values = []
flexcomSym_TWI_CWGR_BRSRCCLK_Values = flexcomSym_TWI_CWGR_BRSRCCLK_Node.getChildren()
for index in range(len(flexcomSym_TWI_CWGR_BRSRCCLK_Values)):
    flexcomSym_TWI_CWGR_BRSRCCLK_Key_Name = flexcomSym_TWI_CWGR_BRSRCCLK_Values[index].getAttribute("name")
    flexcomSym_TWI_CWGR_BRSRCCLK_Key_Value = flexcomSym_TWI_CWGR_BRSRCCLK_Values[index].getAttribute("value")
    flexcomSym_TWI_CWGR_BRSRCCLK_Key_Description = flexcomSym_TWI_CWGR_BRSRCCLK_Values[index].getAttribute("caption")
    flexcomSym_TWI_CWGR_BRSRCCLK.addKey(flexcomSym_TWI_CWGR_BRSRCCLK_Key_Name, flexcomSym_TWI_CWGR_BRSRCCLK_Key_Value, flexcomSym_TWI_CWGR_BRSRCCLK_Key_Description)
flexcomSym_TWI_CWGR_BRSRCCLK.setDisplayMode("Key")
flexcomSym_TWI_CWGR_BRSRCCLK.setOutputMode("Key")
flexcomSym_TWI_CWGR_BRSRCCLK.setDefaultValue(0)
flexcomSym_TWI_CWGR_BRSRCCLK.setVisible(False)
flexcomSym_TWI_CWGR_BRSRCCLK.setDependencies(showMasterDependencies, ["FLEXCOM_TWI_OPMODE", "FLEXCOM_MODE"])

# Operating speed
flexcomSym_Twi_CLK_SPEED = flexcomComponent.createIntegerSymbol("I2C_CLOCK_SPEED", flexcomSym_OperatingMode)
flexcomSym_Twi_CLK_SPEED.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_TWI_CWGR")
flexcomSym_Twi_CLK_SPEED.setLabel("Clock Speed (Hz)")
flexcomSym_Twi_CLK_SPEED.setMin(100000)
flexcomSym_Twi_CLK_SPEED.setMax(400000)
flexcomSym_Twi_CLK_SPEED.setDefaultValue(400000)
flexcomSym_Twi_CLK_SPEED.setVisible(False)
flexcomSym_Twi_CLK_SPEED.setDependencies(showMasterDependencies, ["FLEXCOM_TWI_OPMODE", "FLEXCOM_MODE"])

# Operating speed (Hz)
flexcomSym_Twi_CLK_SPEED_HZ = flexcomComponent.createIntegerSymbol("I2C_CLOCK_SPEED_HZ", flexcomSym_OperatingMode)
flexcomSym_Twi_CLK_SPEED_HZ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_TWI_CWGR")
flexcomSym_Twi_CLK_SPEED_HZ.setLabel("Clock Speed (Hz)")
flexcomSym_Twi_CLK_SPEED_HZ.setDefaultValue(flexcomSym_Twi_CLK_SPEED.getValue())
flexcomSym_Twi_CLK_SPEED_HZ.setVisible(False)
flexcomSym_Twi_CLK_SPEED_HZ.setDependencies(updateI2CBaudHz, ["I2C_CLOCK_SPEED"])

# Slave Address
flexcomSym_ADDR = flexcomComponent.createHexSymbol("FLEXCOM_TWI_SLAVE_ADDRESS", flexcomSym_OperatingMode)
flexcomSym_ADDR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:flexcom_11268;register:FLEX_TWI_SMR")
flexcomSym_ADDR.setLabel("I2C Slave Address (7-bit)")
flexcomSym_ADDR.setMax(1023)
flexcomSym_ADDR.setVisible(False)
flexcomSym_ADDR.setDefaultValue(0x54)
flexcomSym_ADDR.setDependencies(showSlaveDependencies, ["FLEXCOM_TWI_OPMODE", "FLEXCOM_MODE"])

cldiv, chdiv, ckdiv = getFlexcomTwiClockDividerValue(flexcomSym_Twi_CLK_SPEED.getValue())
#CLDIV
flexcomSym_Twi_CWGR_CLDIV = flexcomComponent.createIntegerSymbol("FLEXCOM_TWI_CWGR_CLDIV", flexcomSym_OperatingMode)
flexcomSym_Twi_CWGR_CLDIV.setVisible(False)
flexcomSym_Twi_CWGR_CLDIV.setValue(cldiv, 1)

#CHDIV
flexcomSym_Twi_CWGR_CHDIV = flexcomComponent.createIntegerSymbol("FLEXCOM_TWI_CWGR_CHDIV", flexcomSym_OperatingMode)
flexcomSym_Twi_CWGR_CHDIV.setVisible(False)
flexcomSym_Twi_CWGR_CHDIV.setValue(chdiv, 1)

#CKDIV
flexcomSym_Twi_CWGR_CKDIV = flexcomComponent.createIntegerSymbol("FLEXCOM_TWI_CWGR_CKDIV", flexcomSym_OperatingMode)
flexcomSym_Twi_CWGR_CKDIV.setVisible(False)
flexcomSym_Twi_CWGR_CKDIV.setValue(ckdiv, 1)

#Clock Divider
flexcomSym_Twi_CLK_DIVIDER = flexcomComponent.createStringSymbol("FLEXCOM_TWI_CLK_DIVIDER", flexcomSym_OperatingMode)
flexcomSym_Twi_CLK_DIVIDER.setVisible(False)
flexcomSym_Twi_CLK_DIVIDER.setDependencies(setFlexcomTwiClockDividerValue, ["I2C_CLOCK_SPEED", "core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

# Peripheral Clock Frequency
flexcomSym_Twi_CLK_SRC_FREQ = flexcomComponent.createIntegerSymbol("FLEXCOM_TWI_CLK_SRC_FREQ", flexcomSym_OperatingMode)
flexcomSym_Twi_CLK_SRC_FREQ.setVisible(False)
flexcomSym_Twi_CLK_SRC_FREQ.setDefaultValue(int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")))
flexcomSym_Twi_CLK_SRC_FREQ.setDependencies(setFlexcomTwiClockSourceFreq, ["core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

flexcomSym_Twi_API_Prefix = flexcomComponent.createStringSymbol("I2C_PLIB_API_PREFIX", flexcomSym_OperatingMode)
flexcomSym_Twi_API_Prefix.setDefaultValue(flexcomInstanceName.getValue()  + "_TWI")
flexcomSym_Twi_API_Prefix.setVisible(False)

cpu_clock = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))

flexcomSym_Twi_TimeoutCountVal = flexcomComponent.createIntegerSymbol("FLEXCOM_TWI_TIMEOUT_COUNT_VAL", None)
flexcomSym_Twi_TimeoutCountVal.setVisible(False)
flexcomSym_Twi_TimeoutCountVal.setDefaultValue(cpu_clock/5000)
flexcomSym_Twi_TimeoutCountVal.setDependencies(updateTimeoutCount, ["core.CPU_CLOCK_FREQUENCY"])