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

global sort_alphanumeric
global flexcomSym_SPI_MR_MSTR

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

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
                    "_16_BIT"    :   0xFFFF,
                }

def ClockModeInfo(symbol, event):
    CPHA = Database.getSymbolValue(deviceNamespace, "FLEXCOM_SPI_CSR_NCPHA")
    CPOL = Database.getSymbolValue(deviceNamespace, "FLEXCOM_SPI_CSR_CPOL")
    if (CPOL == 0) and (CPHA == 0):
        symbol.setLabel("***FLEXCOM SPI Mode 1 is Selected***")
    elif (CPOL == 0) and (CPHA == 1):
        symbol.setLabel("***FLEXCOM SPI Mode 0 is Selected***")
    elif (CPOL == 1) and (CPHA == 0):
        symbol.setLabel("***FLEXCOM SPI Mode 3 is Selected***")
    else:
        symbol.setLabel("***FLEXCOM SPI Mode 2 is Selected***")
    # Symbol Visible Property
    if event["id"] == "FLEXCOM_MODE":
        if flexcomSym_OperatingMode.getSelectedKey() == "SPI":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def SCBR_ValueUpdate(spiSym_CSR_SCBR_VALUE, event):
    if event["id"] == flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY":
        clk = int(event["value"])
        baud = Database.getSymbolValue(deviceNamespace, "FLEXCOM_SPI_BAUD_RATE")
    else:
        #This means there is change in baud rate provided by user in GUI
        baud = event["value"]
        clk = int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"))

    SCBR = clk/baud

    if flexcomSym_OperatingMode.getSelectedKey() == "SPI":
        flexcomClockInvalidSym.setVisible((SCBR < 1))

    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255
    spiSym_CSR_SCBR_VALUE.setValue(SCBR, 1)

def calculateCSRIndex(spiSymCSRIndex, event):
    if event["value"] == 0x1:
        spiSymCSRIndex.setValue(1, 2)
    else:
        spiSymCSRIndex.setValue(0, 2)

def DummyData_ValueUpdate(symbol, event):

    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    if event["id"] == "FLEXCOM_SPI_CSR_BITS":
        symbol.setValue(dummyDataDict[event["symbol"].getKey(event["value"])], 1)
        symbol.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])

    if flexcomSym_OperatingMode.getSelectedKey() == "SPI":
        symbol.setVisible(spi_mode == "MASTER")
    else:
        symbol.setVisible(False)

def chipSelectUpdateOnModeChange(symbol, event):

    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    if flexcom_mode == "SPI":
        if spi_mode == "SLAVE":
            symbol.setReadOnly(True)
            symbol.setValue(0)
        else:
            symbol.setReadOnly(False)
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def showSPIDependencies(symbol, event):
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    if flexcom_mode == "SPI":
        if symbol.getID() == "SPI_INTERRUPT_MODE":
            symbol.setReadOnly(spi_mode == "SLAVE")
            symbol.setValue(True)
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def showMasterDependencies(symbol, event):
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    symbol.setVisible(flexcom_mode == "SPI" and spi_mode == "MASTER")

def showSlaveDependencies(symbol, event):
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    symbol.setVisible(flexcom_mode == "SPI" and spi_mode == "SLAVE")

def updateSPISlaveBusyPinVisibility(symbol, event):

    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    busyPinEnabled = event["source"].getSymbolByID("FLEXCOM_SPIS_USE_BUSY_PIN").getValue() == True

    symbol.setVisible(flexcom_mode == "SPI" and spi_mode == "SLAVE" and busyPinEnabled == True)

def updateSPIDMASymbolVisiblity(symbol, event):

    spi_mode = event["source"].getSymbolByID("FLEXCOM_SPI_MR_MSTR").getValue()

    if flexcomSym_OperatingMode.getSelectedKey() == "SPI" and Database.getSymbolValue(deviceNamespace, "SPI_INTERRUPT_MODE") and spi_mode == "MASTER":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def sourceClkUpdate(symbol, event):
    symbol.setValue(event["value"])

###################################################################################################
############################################# FLEXCOM SPI #########################################
###################################################################################################
global flexcomSym_SPI_InterruptMode
flexcomSym_SPI_InterruptMode = flexcomComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", flexcomSym_OperatingMode)
flexcomSym_SPI_InterruptMode.setLabel("Interrupt Mode")
flexcomSym_SPI_InterruptMode.setDefaultValue(True)
flexcomSym_SPI_InterruptMode.setVisible(False)
flexcomSym_SPI_InterruptMode.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

flexcomSPIModeValues = ["MASTER", "SLAVE"]
flexcomSym_SPI_MR_MSTR = flexcomComponent.createComboSymbol("FLEXCOM_SPI_MR_MSTR", flexcomSym_OperatingMode, flexcomSPIModeValues)
flexcomSym_SPI_MR_MSTR.setLabel("Master/Slave Mode")
flexcomSym_SPI_MR_MSTR.setDefaultValue(flexcomSPIModeValues[0])
flexcomSym_SPI_MR_MSTR.setReadOnly(False)
flexcomSym_SPI_MR_MSTR.setVisible(False)
flexcomSym_SPI_MR_MSTR.setDependencies(showSPIDependencies, ["FLEXCOM_MODE"])

#Select clock source
flexcomSym_SPI_MR_BRSRCCLK = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPI_MR_BRSRCCLK", flexcomSym_OperatingMode)
flexcomSym_SPI_MR_BRSRCCLK.setLabel("Select Clock Source")
flexcomSym_SPI_MR_BRSRCCLK_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_SPI_MR__BRSRCCLK\"]")
flexcomSym_SPI_MR_BRSRCCLK_Values = []
flexcomSym_SPI_MR_BRSRCCLK_Values = flexcomSym_SPI_MR_BRSRCCLK_Node.getChildren()
for index in range(len(flexcomSym_SPI_MR_BRSRCCLK_Values)):
    flexcomSym_SPI_MR_BRSRCCLK_Key_Name = flexcomSym_SPI_MR_BRSRCCLK_Values[index].getAttribute("name")
    flexcomSym_SPI_MR_BRSRCCLK_Key_Value = flexcomSym_SPI_MR_BRSRCCLK_Values[index].getAttribute("value")
    flexcomSym_SPI_MR_BRSRCCLK_Key_Description = flexcomSym_SPI_MR_BRSRCCLK_Values[index].getAttribute("caption")
    flexcomSym_SPI_MR_BRSRCCLK.addKey(flexcomSym_SPI_MR_BRSRCCLK_Key_Name, flexcomSym_SPI_MR_BRSRCCLK_Key_Value, flexcomSym_SPI_MR_BRSRCCLK_Key_Description)
flexcomSym_SPI_MR_BRSRCCLK.setDisplayMode("Key")
flexcomSym_SPI_MR_BRSRCCLK.setOutputMode("Key")
flexcomSym_SPI_MR_BRSRCCLK.setDefaultValue(0)
flexcomSym_SPI_MR_BRSRCCLK.setVisible(False)
flexcomSym_SPI_MR_BRSRCCLK.setDependencies(symbolVisible, ["FLEXCOM_MODE"])

global flexcomSym_SPI_MR_PCS
flexcomSym_SPI_MR_PCS = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPI_MR_PCS", flexcomSym_OperatingMode)
flexcomSym_SPI_MR_PCS.setLabel("Peripheral Chip Select")
flexcomSym_SPI_MR_PCS.setOutputMode("Key")
flexcomSym_SPI_MR_PCS.setDisplayMode("Key")
flexcomSym_SPI_MR_PCS.setDefaultValue(0)
flexcomSym_SPI_MR_PCS.addKey("NPCS0", "0", "NPCS0 as Chip Select")
flexcomSym_SPI_MR_PCS.addKey("NPCS1", "1", "NPCS1 as Chip Select")
# When User wants to control his chip select himself (through some GPIO pin),
# then all the NPCSx lines are free to be used as PIO pins. But in MR_PCS
# field, one of the NPCS lines still has to be selected in order to decide
# which SPI_CSRx register will be active. Here we have used NPCS0 selection
# for such case, it can be changed to any other NPCSx line without affecting
# the user.
flexcomSym_SPI_MR_PCS.addKey("GPIO", "0", "User Controlled Chip Select Through GPIO Pin")
flexcomSym_SPI_MR_PCS.setVisible(False)
flexcomSym_SPI_MR_PCS.setDependencies(chipSelectUpdateOnModeChange, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

flexcomSym_SPI_CSRIndex = flexcomComponent.createIntegerSymbol("FLEXCOM_SPI_CSR_INDEX", flexcomSym_OperatingMode)
flexcomSym_SPI_CSRIndex.setDefaultValue(0)
flexcomSym_SPI_CSRIndex.setVisible(False)
flexcomSym_SPI_CSRIndex.setDependencies(calculateCSRIndex, ["FLEXCOM_SPI_MR_PCS"])

flexcomSym_SPI_MasterClock = flexcomComponent.createIntegerSymbol("FLEXCOM_SPI_PERIPHERAL_CLOCK", flexcomSym_OperatingMode)
flexcomSym_SPI_MasterClock.setDefaultValue(int(Database.getSymbolValue("core",flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY")))
flexcomSym_SPI_MasterClock.setDependencies(sourceClkUpdate, ["core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])
flexcomSym_SPI_MasterClock.setVisible(False)

defaultbaudRate = 1000000
flexcomSym_SPI_Baudrate = flexcomComponent.createIntegerSymbol("FLEXCOM_SPI_BAUD_RATE", flexcomSym_OperatingMode)
flexcomSym_SPI_Baudrate.setLabel("Baud Rate (Hz)")
flexcomSym_SPI_Baudrate.setDefaultValue(defaultbaudRate)
flexcomSym_SPI_Baudrate.setVisible(False)
flexcomSym_SPI_Baudrate.setDependencies(showMasterDependencies, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

defaultSCBR = int(Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"))/defaultbaudRate
flexcomSym_SPI_CSR_SCBR_VALUE = flexcomComponent.createIntegerSymbol("FLEXCOM_SPI_CSR_SCBR_VALUE", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_SCBR_VALUE.setDefaultValue(defaultSCBR)
flexcomSym_SPI_CSR_SCBR_VALUE.setVisible(False)
flexcomSym_SPI_CSR_SCBR_VALUE.setDependencies(SCBR_ValueUpdate, ["FLEXCOM_SPI_BAUD_RATE", "core." + flexcomInstanceName.getValue() + "_CLOCK_FREQUENCY"])

flexcomSym_SPI_CSR_BITS = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPI_CSR_BITS", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS.setLabel("Bits Per Transfer")
flexcomSym_SPI_CSR_BITS.setOutputMode("Key")
flexcomSym_SPI_CSR_BITS.setDisplayMode("Description")
flexcomSym_SPI_CSR_BITS.setDefaultValue(0)
flexcomSym_SPI_CSR_BITS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEX_SPI_CSR__BITS\"]")
flexcomSym_SPI_CSR_BITS_Values = []
flexcomSym_SPI_CSR_BITS_Values = flexcomSym_SPI_CSR_BITS_Node.getChildren()
for index in range(len(flexcomSym_SPI_CSR_BITS_Values)):
    flexcomSym_SPI_CSR_BITS_Key_Name = flexcomSym_SPI_CSR_BITS_Values[index].getAttribute("name")
    flexcomSym_SPI_CSR_BITS_Key_Value = flexcomSym_SPI_CSR_BITS_Values[index].getAttribute("value")
    flexcomSym_SPI_CSR_BITS_Key_Description = flexcomSym_SPI_CSR_BITS_Values[index].getAttribute("caption")
    flexcomSym_SPI_CSR_BITS.addKey(flexcomSym_SPI_CSR_BITS_Key_Name, flexcomSym_SPI_CSR_BITS_Key_Value, flexcomSym_SPI_CSR_BITS_Key_Description)
flexcomSym_SPI_CSR_BITS.setVisible(False)
flexcomSym_SPI_CSR_BITS.setDependencies(showSPIDependencies, ["FLEXCOM_MODE"])

flexcomSym_SPI_DummyData = flexcomComponent.createHexSymbol("FLEXCOM_SPI_DUMMY_DATA", flexcomSym_OperatingMode)
flexcomSym_SPI_DummyData.setVisible(False)
flexcomSym_SPI_DummyData.setLabel("Dummy Data")
flexcomSym_SPI_DummyData.setDescription("Dummy Data to be written during SPI Read")
flexcomSym_SPI_DummyData.setDefaultValue(0xFF)
flexcomSym_SPI_DummyData.setMin(0x0)
flexcomSym_SPI_DummyData.setDependencies(DummyData_ValueUpdate, ["FLEXCOM_SPI_CSR_BITS", "FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

flexcomSym_SPI_CSR_CPOL = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPI_CSR_CPOL", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_CPOL.setLabel("Clock Polarity")
flexcomSym_SPI_CSR_CPOL.setOutputMode("Value")
flexcomSym_SPI_CSR_CPOL.setDisplayMode("Description")
flexcomSym_SPI_CSR_CPOL.setDefaultValue(0)
flexcomSym_SPI_CSR_CPOL.addKey("CPOL0", "0", "The inactive state value of SPCK is logic level zero (CPOL=0)")
flexcomSym_SPI_CSR_CPOL.addKey("CPOL1", "1", "The inactive state value of SPCK is logic level one (CPOL=1)")
flexcomSym_SPI_CSR_CPOL.setVisible(False)
flexcomSym_SPI_CSR_CPOL.setDependencies(showSPIDependencies, ["FLEXCOM_MODE"])

flexcomSym_SPI_CSR_NCPHA = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPI_CSR_NCPHA", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_NCPHA.setLabel("Clock Phase")
flexcomSym_SPI_CSR_NCPHA.setOutputMode("Value")
flexcomSym_SPI_CSR_NCPHA.setDisplayMode("Description")
flexcomSym_SPI_CSR_NCPHA.setDefaultValue(1)
flexcomSym_SPI_CSR_NCPHA.addKey("NCPHA0", "0", "Data are changed on the leading edge of SPCK and captured on the following edge of SPCK (NCPHA=0)")
flexcomSym_SPI_CSR_NCPHA.addKey("NCPHA1", "1", "Data are captured on the leading edge of SPCK and changed on the following edge of SPCK (NCPHA=1)")
flexcomSym_SPI_CSR_NCPHA.setVisible(False)
flexcomSym_SPI_CSR_NCPHA.setDependencies(showSPIDependencies, ["FLEXCOM_MODE"])

flexcomSym_TXBuffer_Size = flexcomComponent.createIntegerSymbol("FLEXCOM_SPIS_TX_BUFFER_SIZE", None)
flexcomSym_TXBuffer_Size.setLabel("TX Buffer Size (in bytes)")
flexcomSym_TXBuffer_Size.setMin(0)
flexcomSym_TXBuffer_Size.setMax(65535)
flexcomSym_TXBuffer_Size.setDefaultValue(256)
flexcomSym_TXBuffer_Size.setVisible(False)
flexcomSym_TXBuffer_Size.setDependencies(showSlaveDependencies, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

flexcomSym_RXBuffer_Size = flexcomComponent.createIntegerSymbol("FLEXCOM_SPIS_RX_BUFFER_SIZE", None)
flexcomSym_RXBuffer_Size.setLabel("RX Buffer Size (in bytes)")
flexcomSym_RXBuffer_Size.setMin(0)
flexcomSym_RXBuffer_Size.setMax(65535)
flexcomSym_RXBuffer_Size.setDefaultValue(256)
flexcomSym_RXBuffer_Size.setVisible(False)
flexcomSym_RXBuffer_Size.setDependencies(showSlaveDependencies, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

flexcomSymUseBusyPin = flexcomComponent.createBooleanSymbol("FLEXCOM_SPIS_USE_BUSY_PIN", None)
flexcomSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
flexcomSymUseBusyPin.setDefaultValue(True)
flexcomSymUseBusyPin.setVisible(False)
flexcomSymUseBusyPin.setDependencies(showSlaveDependencies, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR"])

flexcomSymBusyPin = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPIS_BUSY_PIN", flexcomSymUseBusyPin)
flexcomSymBusyPin.setVisible(False)
flexcomSymBusyPin.setLabel("Slave Busy Pin")
flexcomSymBusyPin.setOutputMode("Key")
flexcomSymBusyPin.setDisplayMode("Description")
flexcomSymBusyPin.setDependencies(updateSPISlaveBusyPinVisibility, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR", "FLEXCOM_SPIS_USE_BUSY_PIN"])

availablePinDictionary = {}

# Send message to core to get available pins
availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

for pad in sort_alphanumeric(availablePinDictionary.values()):
    key = pad
    value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
    description = pad
    flexcomSymBusyPin.addKey(key, value, description)

#SPI Character Size
flexcomSymBusyPinLogicLevel = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_SPIS_BUSY_PIN_LOGIC_LEVEL", flexcomSymUseBusyPin)
flexcomSymBusyPinLogicLevel.setLabel("Slave Busy Pin Logic Level")
flexcomSymBusyPinLogicLevel.setVisible(False)
flexcomSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
flexcomSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
flexcomSymBusyPinLogicLevel.setDefaultValue(1)
flexcomSymBusyPinLogicLevel.setOutputMode("Key")
flexcomSymBusyPinLogicLevel.setDisplayMode("Description")
flexcomSymBusyPinLogicLevel.setDependencies(updateSPISlaveBusyPinVisibility, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR", "FLEXCOM_SPIS_USE_BUSY_PIN"])

flexcomSymBusyPinConfigComment = flexcomComponent.createCommentSymbol("FLEXCOM_SPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT", flexcomSymUseBusyPin)
flexcomSymBusyPinConfigComment.setVisible(False)
flexcomSymBusyPinConfigComment.setLabel("***Above selected Busy pin must be configured as GPIO Output in Pin Manager***")
flexcomSymBusyPinConfigComment.setDependencies(updateSPISlaveBusyPinVisibility, ["FLEXCOM_MODE", "FLEXCOM_SPI_MR_MSTR", "FLEXCOM_SPIS_USE_BUSY_PIN"])

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################
#FLEXCOM SPI 8-bit Character size Mask
flexcomSym_SPI_CSR_BITS_8BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_8BIT.setDefaultValue("0x0")
flexcomSym_SPI_CSR_BITS_8BIT.setVisible(False)

#FLEXCOM SPI 9-bit Character size Mask
flexcomSym_SPI_CSR_BITS_9BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_9_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_9BIT.setDefaultValue("0x10")
flexcomSym_SPI_CSR_BITS_9BIT.setVisible(False)

#FLEXCOM SPI 10-bit Character size Mask
flexcomSym_SPI_CSR_BITS_10BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_10_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_10BIT.setDefaultValue("0x20")
flexcomSym_SPI_CSR_BITS_10BIT.setVisible(False)

#FLEXCOM SPI 11-bit Character size Mask
flexcomSym_SPI_CSR_BITS_11BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_11_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_11BIT.setDefaultValue("0x30")
flexcomSym_SPI_CSR_BITS_11BIT.setVisible(False)

#FLEXCOM SPI 12-bit Character size Mask
flexcomSym_SPI_CSR_BITS_12BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_12_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_12BIT.setDefaultValue("0x40")
flexcomSym_SPI_CSR_BITS_12BIT.setVisible(False)

#FLEXCOM SPI 13-bit Character size Mask
flexcomSym_SPI_CSR_BITS_13BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_13_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_13BIT.setDefaultValue("0x50")
flexcomSym_SPI_CSR_BITS_13BIT.setVisible(False)

#FLEXCOM SPI 14-bit Character size Mask
flexcomSym_SPI_CSR_BITS_14BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_14_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_14BIT.setDefaultValue("0x60")
flexcomSym_SPI_CSR_BITS_14BIT.setVisible(False)

#FLEXCOM SPI 15-bit Character size Mask
flexcomSym_SPI_CSR_BITS_15BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_15_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_15BIT.setDefaultValue("0x70")
flexcomSym_SPI_CSR_BITS_15BIT.setVisible(False)

#FLEXCOM SPI 16-bit Character size Mask
flexcomSym_SPI_CSR_BITS_16BIT = flexcomComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_BITS_16BIT.setDefaultValue("0x80")
flexcomSym_SPI_CSR_BITS_16BIT.setVisible(False)

#SPI Clock Polarity Idle Low Mask
flexcomSym_SPI_CSR_CPOL_IL_Mask = flexcomComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_CPOL_IL_Mask.setDefaultValue("0x0")
flexcomSym_SPI_CSR_CPOL_IL_Mask.setVisible(False)

#SPI Clock Polarity Idle High Mask
flexcomSym_SPI_CSR_CPOL_IH_Mask = flexcomComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_CPOL_IH_Mask.setDefaultValue("0x1")
flexcomSym_SPI_CSR_CPOL_IH_Mask.setVisible(False)

#SPI Clock Phase Leading Edge Mask
flexcomSym_SPI_CSR_NCPHA_TE_Mask = flexcomComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_NCPHA_TE_Mask.setDefaultValue("0x0")
flexcomSym_SPI_CSR_NCPHA_TE_Mask.setVisible(False)

#SPI Clock Phase Trailing Edge Mask
flexcomSym_SPI_CSR_NCPHA_LE_Mask = flexcomComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", flexcomSym_OperatingMode)
flexcomSym_SPI_CSR_NCPHA_LE_Mask.setDefaultValue("0x2")
flexcomSym_SPI_CSR_NCPHA_LE_Mask.setVisible(False)

flexcomSym_SPI_API_Prefix = flexcomComponent.createStringSymbol("SPI_PLIB_API_PREFIX", flexcomSym_OperatingMode)
flexcomSym_SPI_API_Prefix.setDefaultValue(flexcomInstanceName.getValue()  + "_SPI")
flexcomSym_SPI_API_Prefix.setVisible(False)

flexcomSym_SPI_ClockModeComment = flexcomComponent.createCommentSymbol("FLEXCOM_SPI_CLOCK_MODE_COMMENT", flexcomSym_OperatingMode)
flexcomSym_SPI_ClockModeComment.setLabel("***FLEXCOM SPI Mode 0 is Selected***")
flexcomSym_SPI_ClockModeComment.setVisible(False)
flexcomSym_SPI_ClockModeComment.setDependencies(ClockModeInfo, ["FLEXCOM_MODE", "FLEXCOM_SPI_CSR_CPOL", "FLEXCOM_SPI_CSR_NCPHA"])

#FLEXCOM SPI Driver Controlled Symbol
global flexcomSym_SPI_DriverControlled
flexcomSym_SPI_DriverControlled = flexcomComponent.createBooleanSymbol("SPI_DRIVER_CONTROLLED", flexcomSym_OperatingMode)
flexcomSym_SPI_DriverControlled.setVisible(False)
flexcomSym_SPI_DriverControlled.setDefaultValue(False)

# Warning message when PLIB is configured in non-interrupt mode but used with driver.
global flexcomSym_SPI_InterruptDriverModeComment
flexcomSym_SPI_InterruptDriverModeComment = flexcomComponent.createCommentSymbol("SPI_INT_DRIVER_COMMENT", flexcomSym_OperatingMode)
flexcomSym_SPI_InterruptDriverModeComment.setVisible(False)
flexcomSym_SPI_InterruptDriverModeComment.setLabel("Warning!!! " + flexcomInstanceName.getValue() + "SPI PLIB to be used with driver, must be configured in interrupt mode")
