"""*****************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

import re
import xml.etree.ElementTree as ET
import os.path
import inspect
from collections import OrderedDict

# Dummy Data Dictionary
# Dictionary mapping key names to corresponding dummy data values based on ATDF file specifications.
# These values are fixed, while their captions may vary across different families using this SPI PLIB.
dummyDataDict = {
    "8 bit": 0xFF,  # 8-bit
    "16 bit": 0xFFFF,  # 16-bit
    "24 bit": 0xFFFFFF,  # 24-bit
    "32 bit": 0xFFFFFFFF,  # 32-bit
}

# SPI Data Widths
# List of supported data widths for SPI communication, specified in bits.
SPI_DATA_WIDTHS = ["8 bit", "16 bit", "32 bit"]

# Interrupt List
# List of possible interrupt types for the SPI module.
interruptList = ["RX", "TX", "E"]

# Interrupt Vector Data Dictionary
# Dictionary to hold vector data for interrupt handling.
intVectorDataDictionary = {}

# SPI Configuration Constants
# Constants representing key identifiers used in SPI configuration and operations.
SPI = "SPI"
CON1 = "CON1"
MSTEN = "MSTEN"
CKP = "CKP"
CKE = "CKE"
SMP = "SMP"
MCLKEN = "MCLKEN"
HOST = "Host"
CLIENT = "Client"
CORE = "core"
SOURCE = "source"
BRG = "BRG"
SPI1BRG = "SPI1BRG"
ENABLE = "Enable"
DISABLE = "Disable"
INTERRUPT = "Interrupt"
IC_PREFIX = "INTC"
ID = "id"

# Symbol Key Constants
# Constants for symbol keys used in SPI configuration.
SPI_CON1__MSTEN = "SPI_CON1__MSTEN"
SPI_SPICON_DATA_WIDTH = "SPI_SPICON_DATA_WIDTH"
INTERRUPT_MODE = "SPI_INTERRUPT_MODE"
SPI_MODE = "SPI_MODE"
REQUESTED_SPEED = "REQUESTED_SPEED"
CALCULATED_SPEED = "CALCULATED_SPEED"
INTERRUPT_COMMENT = "INTERRUPT_COMMENT"
SPI_DUMMY_DATA = "SPI_DUMMY_DATA"
TX_BUFFER_SIZE = "SPIS_TX_BUFFER_SIZE"
RX_BUFFER_SIZE = "SPIS_RX_BUFFER_SIZE"
CLIENT_SELECT = "CLIENT_SELECT"
SPI_INSTANCE_NAME = "SPI_INSTANCE_NAME"
SPI_INSTANCE_NUM = "instanceNumber"
SPI_CLOCK_MODE_COMMENT = "SPI_CLOCK_MODE_COMMENT"
SPI_MAX_BRG = "SPI_MAX_BRG"
SPI_BRG_VALUE = "SPI_BRG_VALUE"
SPI_CON1__CKP = "SPI_CON1__CKP"
SPI_CON1__CKE = "SPI_CON1__CKE"
SPI_CON1__MCLKEN = "SPI_CON1__MCLKEN"
SPIS_CS_PIN = "SPIS_CS_PIN"
SPIS_CS_PIN_LOGIC_LEVEL = "SPIS_CS_PIN_LOGIC_LEVEL"
SPIS_CS_PIN_CONFIG_COMMENT = "SPIS_CS_PIN_CONFIG_COMMENT"
SPIS_USE_BUSY_PIN = "SPIS_USE_BUSY_PIN"
SPIS_BUSY_PIN = "SPIS_BUSY_PIN"
SPIS_BUSY_PIN_LOGIC_LEVEL = "SPIS_BUSY_PIN_LOGIC_LEVEL"
SPIS_Client_BUSY_PIN_CONFIG_COMMENT = "SPIS_Client_BUSY_PIN_CONFIG_COMMENT"

# Core Component Clock Constants
# Constants related to the core component clock settings for SPI.
CLOCK_FREQ_KEY = "SPI_Clock_Frequency"
CLOCK_GENERATOR_9 = "Clock Generator 9"
NINE = "9"
CLOCK_GENERATOR9_FREQ = "clkGen9OutFrequency"
STANDARD_SPEED_PERIPHERAL_CLOCK = "Standard Speed Peripheral Clock"
STANDARD_SPEED_CLOCK_FREQ = "stdSpeedClkFreq"
CLOCK_FREQUENCY = "Clock Source Frequency (Hz)"

# Constants for SPI Modes
# Constants defining the various operational modes of SPI communication.
IDLE_TO_ACTIVE = "Idle to Active"
ACTIVE_TO_IDLE = "Active to Idle"
IDLE_LOW_ACTIVE_HIGH = "Idle:Low, Active:High"
IDLE_HIGH_ACTIVE_LOW = "Idle:High, Active:Low"

# Label Constants
# Constants for labels used in the configuration UI for SPI settings.
SPI_INTERRUPT_MODE_LABEL = "Enable Interrupts"
SPI_SPICON_MSTEN_LABEL = "Operating Mode"
SPI_SPICON_CLKPOL_LABEL = "Clock Polarity"
SPI_SPICON_CLKPH_LABEL = "Clock Edge"
SPI_SPICON_SMP_LABEL = "Data Input Sample Phase"
SPI_SPICON_DATA_WIDTH_LABEL = "Data Width"
CLOCK_SOURCE_LABEL = "Clock Source"
SPI_REQUESTED_SPEED_LABEL = "Requested Bus Speed (Hz)"
SPI_CALCULATED_SPEED_LABEL = "Calculated Bus Speed (Hz)"
WARNING_INTERRUPT_DISABLED_LABEL = (
    "Warning!!! Peripheral Interrupt is Disabled in Interrupt Manager"
)

# Mode Labels
# Constants for displaying current SPI modes.
MODE_LABEL = "Mode"
SPI_MODE_0_LABEL = "***SPI Mode 0 is Set***"
SPI_MODE_1_LABEL = "***SPI Mode 1 is Set***"
SPI_MODE_2_LABEL = "***SPI Mode 2 is Set***"
SPI_MODE_3_LABEL = "***SPI Mode 3 is Set***"

# Dummy Data Labels
# Constants for dummy data labels used in SPI operations.
SPI_DUMMY_DATA_LABEL = "Dummy Data"
SPI_DUMMY_DATA_DESC = "Dummy Data to be written during SPI Read"
SPIS_TX_BUFFER_SIZE_LABEL = "TX Buffer Size (in bytes)"
SPIS_RX_BUFFER_SIZE_LABEL = "RX Buffer Size (in bytes)"
SPIS_CLIENT_SELECT_ENABLE_LABEL = "Enable Client Select"
SPI2_PIN_CONFIGURATION_MESSAGE = "Note: To use non-PPS pins for SPI2, enable SPI2PIN in System/Device_Configuration/FDEVOPT and configure it accordingly."
SPI_CON1__MODE_32_MODE_16 = "SPI_CON1__MODE_32_MODE_16"

# ATDF Helper Functions start


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value


def getSettingBitDefaultValue(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        regDefaultVal = registerNode.getAttribute("initval")
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return getDefaultVal(regDefaultVal, bitMask)
    return 0


def maxThreshold(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return int(bitMask, 0)
    return 0


def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if bitNode != None:
        return bitNode.getAttribute("values")
    return ""


def getModuleRegisterGroup(moduleName, registerGroup):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]'
    )
    registerGroupNode = ATDF.getNode(atdfPath)
    if registerGroupNode != None:
        return registerGroupNode.getChildren()
    return None


def getModuleRegisterData(moduleName, registerGroup, register):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(atdfPath)
    if registerNode != None:
        return registerNode.getChildren()
    return None


def getValueGroup(moduleName, valueGroupName):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/value-group@[name="'
        + valueGroupName
        + '"]'
    )
    return ATDF.getNode(atdfPath)


def getBitField(moduleName, registerGroup, register, bitfield):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]/bitfield@[name="'
        + bitfield
        + '"]'
    )
    return ATDF.getNode(atdfPath)


def processBitfield(bitfield, remove_prefix=False):
    dict = {}
    caption = bitfield.getAttribute("caption")
    if caption.lower() != "reserved":  # skip (unused) reserved fields
        if remove_prefix and caption.startswith("AD1"):
            caption = caption[3:]
        dict["desc"] = caption
        dict["key"] = caption

        # Get rid of leading '0x', and convert to int if was hex
        value = bitfield.getAttribute("value")
        if value[:2] == "0x":
            temp = value[2:]
            tempint = int(temp, 16)
        else:
            tempint = int(value)

        dict["value"] = str(tempint)
        return dict
    return None


def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
    for bitfield in valueNodes:
        processed_bitfield = processBitfield(bitfield)
        if processed_bitfield:
            optionList.append(processed_bitfield)
    return optionList


def addKeystoKeyValueSymbol(bitSymbol, bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey(ii["key"], ii["value"], ii["desc"])


def getKeyValuePairBasedonValue(value, keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return (
                index  # return occurrence of <bitfield > entry which has matching value
            )
        index += 1
    print("find_key: could not find value in dictionary")  # should never get here
    return ""


def createKeyValueSetSymbol(
    component, moduleName, registerGroup, register, bitfield, parentNode=None
):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        symbolKey = valueGroupEntry
        optionList = getBitfieldOptionList(valGroup)
        valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, parentNode)
        valueGroupEntryComp.setLabel(symbolKey)
        defaultValue = getSettingBitDefaultValue(
            moduleName, registerGroup, register, bitfield
        )
        valueGroupEntryComp.setDefaultValue(
            getKeyValuePairBasedonValue(defaultValue, optionList)
        )
        valueGroupEntryComp.setOutputMode("Value")
        valueGroupEntryComp.setDisplayMode("Description")
        addKeystoKeyValueSymbol(valueGroupEntryComp, optionList)
        return valueGroupEntryComp


# ATDF Helper Functions end

def handleMessage(messageID, args):
    global operatingMode
    global spisSym_RXBuffer_Size
    global spisSym_TXBuffer_Size
    global spiInterruptMode
    result_dict = {}

    if (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None and args["isReadOnly"] == True:
            operatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            operatingMode.setSelectedKey(HOST)

    elif (messageID == "SPI_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            operatingMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            operatingMode.setSelectedKey(CLIENT)

    elif (messageID == "SPI_SLAVE_RX_BUFFER_SIZE"):
        if args.get("isReadOnly") != None:
            spisSym_RXBuffer_Size.setReadOnly(args["isReadOnly"])
        if args.get("size") != None:
            spisSym_RXBuffer_Size.setValue(args["size"], 2)

    elif (messageID == "SPI_SLAVE_TX_BUFFER_SIZE"):
        if args.get("isReadOnly") != None:
            spisSym_TXBuffer_Size.setReadOnly(args["isReadOnly"])
        if args.get("size") != None:
            spisSym_TXBuffer_Size.setValue(args["size"], 2)

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            spiInterruptMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            spiInterruptMode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            spiInterruptMode.setVisible(args["isVisible"])

    return result_dict

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

# CallBack functions start

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def updateSPIClientBusyPinVisibility(symbol, event):

    spiMode = event["source"].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey()
    busyPinEnabled = event["source"].getSymbolByID("SPIS_USE_BUSY_PIN").getValue()
    symbol.setVisible(spiMode == CLIENT and busyPinEnabled == True)

def showModeDependencies(symbol, event):
    # Fetch the symbols based on their IDs
    fetched_clkPolarity_symbol = event["source"].getSymbolByID(SPI_CON1__CKP)
    fetched_clkEdge_symbol = event["source"].getSymbolByID(SPI_CON1__CKE)
    fetched_modeComment_symbol = event["source"].getSymbolByID(SPI_CLOCK_MODE_COMMENT)

    # Set visibility based on the event value
    is_visible = event["value"]
    fetched_clkPolarity_symbol.setVisible(is_visible)
    fetched_clkEdge_symbol.setVisible(is_visible)
    fetched_modeComment_symbol.setVisible(is_visible)


def clockModeInfo(symbol, event):
    clock_edge = event[SOURCE].getSymbolByID(SPI_CON1__CKE).getSelectedKey()
    clock_polarity = event[SOURCE].getSymbolByID(SPI_CON1__CKP).getSelectedKey()

    # Mapping of (clock_edge, clock_polarity) to mode labels
    mode_map = {
        (IDLE_TO_ACTIVE, IDLE_LOW_ACTIVE_HIGH): SPI_MODE_1_LABEL,
        (IDLE_TO_ACTIVE, IDLE_HIGH_ACTIVE_LOW): SPI_MODE_3_LABEL,
        (ACTIVE_TO_IDLE, IDLE_LOW_ACTIVE_HIGH): SPI_MODE_0_LABEL,
        (ACTIVE_TO_IDLE, IDLE_HIGH_ACTIVE_LOW): SPI_MODE_2_LABEL,
    }

    # Retrieve the mode label based on the clock edge and polarity
    mode_str = mode_map.get((clock_edge, clock_polarity), "")

    symbol.setLabel(mode_str)


def showHostDependencies(symbol, event):
    if event["source"].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey() == HOST:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def showClientDependencies(symbol, event):
    if event[SOURCE].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey() == CLIENT:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateClkFreq(symbol, event):
    mclkEnabled = event[SOURCE].getSymbolByID(SPI_CON1__MCLKEN).getSelectedKey()
    reqSpeed = event[SOURCE].getSymbolByID(REQUESTED_SPEED)

    # Create a mapping of clock types to their corresponding frequency symbols
    clock_map = {
        CLOCK_GENERATOR_9: CLOCK_GENERATOR9_FREQ,
        STANDARD_SPEED_PERIPHERAL_CLOCK: STANDARD_SPEED_CLOCK_FREQ,
    }
    # Get the frequency symbol for the selected clock type
    frequency_symbol = clock_map.get(mclkEnabled)
    if frequency_symbol is not None:
        clkFreq = int(Database.getSymbolValue(CORE, frequency_symbol))
        symbol.setValue(clkFreq)

        # update min and max for requested speed
        baud_rates = calculateMinMaxBaudRates(clkFreq)
        reqSpeed.setMin(int(baud_rates["min_baud_rate"]))
        reqSpeed.setMax(int(baud_rates["max_baud_rate"]))


def updateIntReadOnlyAttr(symbol, event):
    symbol.setReadOnly(
        event[SOURCE].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey() == CLIENT
    )


def get_brg_value(clock_source_freq, spi_req_freq, max_brg_value):
    if clock_source_freq <= 0 or spi_req_freq <= 0:
         return 0
    brg_val = round(clock_source_freq / (2 * spi_req_freq) - 1)
    # Ensure BRG value does not exceed the maximum allowed value
    return min(max(brg_val, 0), max_brg_value)


def get_calculated_frequency(clock_source_freq, spi_req_freq, max_brg_value):
    # If either clock source frequency or desired SPI request frequency is invalid, return 0
    if clock_source_freq <= 0 or spi_req_freq <= 0:
        return 0
    # Calculate the Baud Rate Generator value
    brg_val = get_brg_value(clock_source_freq, spi_req_freq, max_brg_value)
    # Round and return the actual frequency
    calcSpeed = round(get_actual_freq(clock_source_freq, brg_val))
    return int(calcSpeed)


def get_actual_freq(clock_source_freq, brg_val):
    return clock_source_freq / (2 * (brg_val + 1))


def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break
    return vector_index


def updateInterruptLists(instanceNo, interruptList):
    for interrupt in interruptList:
        intIndex = getVectorIndex(SPI + instanceNo + interrupt + INTERRUPT)
        interruptEnableList.append("{}.{}_{}_ENABLE".format(CORE, IC_PREFIX, intIndex))
        interruptHandlerLockList.append(
            "{}.{}_{}_HANDLER_LOCK".format(CORE, IC_PREFIX, intIndex)
        )


def setCoreInterruptSymbols(value):
    for int in interruptEnableList:
        int = int.replace(CORE + ".", "")
        Database.setSymbolValue(CORE, int, value)

    for int in interruptHandlerLockList:
        int = int.replace(CORE + ".", "")
        Database.setSymbolValue(CORE, int, value)


def interruptEnableChange(symbol, event):
    if event["id"] == INTERRUPT_MODE:
        setCoreInterruptSymbols(bool(event["value"]))

    updateIntReadOnlyAttr(symbol, event)


def interruptCommentCb(symbol, event):
    updateInterruptComment(symbol)


def updateInterruptComment(symbol):
    interruptState = symbol.getComponent().getSymbolValue(INTERRUPT_MODE)
    instance = str(symbol.getComponent().getSymbolValue(SPI_INSTANCE_NUM))
    status = False
    for int in interruptEnableList:
        int = int.replace(CORE + ".", "")
        if bool(Database.getSymbolValue(CORE, int)) != interruptState:
            status = True
            break
    if status:
        modeSym = symbol.getComponent().getSymbolByID(SPI_CON1__MSTEN)
        modeSymVal = modeSym.getKeyDescription(modeSym.getValue())
        val = ENABLE if interruptState else DISABLE
        symbol.setVisible(True)
        symbol.setLabel(
            "Warning!!!  For "
            + modeSymVal
            + ", "
            + val
            + " SPI"
            + instance
            + " TX ,RX and Error Interrupts in Interrupts Section of System module"
        )
    else:
        symbol.setVisible(False)


def updateOperatingMode(symbol, event):
    interruptModeSym = event[SOURCE].getSymbolByID(INTERRUPT_MODE)
    if symbol.getSelectedKey() == HOST :
        interruptModeSym.setValue(True)
    else:
        interruptModeSym.setValue(True)


def baudRateTrigger(symbol, event):
    clock_source_freq = symbol.getComponent().getSymbolValue(CLOCK_FREQ_KEY)
    reqSpeed = int(symbol.getComponent().getSymbolValue(REQUESTED_SPEED))
    maxBrgVal = symbol.getComponent().getSymbolValue(SPI_MAX_BRG)
    brgVal = get_brg_value(clock_source_freq, reqSpeed, maxBrgVal)
    symbol.setValue(int(brgVal))


def calcSpeedTrigger(symbol, event):
    if event["id"] == SPI_CON1__MSTEN:
        showHostDependencies(symbol, event)
    else:
        clk = symbol.getComponent().getSymbolValue(CLOCK_FREQ_KEY)
        reqSpeed = int(symbol.getComponent().getSymbolValue(REQUESTED_SPEED))
        maxBrgVal = symbol.getComponent().getSymbolValue(SPI_MAX_BRG)
        calcSpeed = get_calculated_frequency(clk, reqSpeed, maxBrgVal)
        symbol.setValue(calcSpeed)


def calculateMinMaxBaudRates(fpb):
    # Maximum baud rate occurs when SPIxBRG = 0
    max_baud_rate = fpb / 2
    # Minimum baud rate occurs when SPIxBRG = 16383 (or 2^14 - 1)
    min_baud_rate = fpb / 32768  # Equivalent to F_PB / (2 * (16383 + 1))
    return {"max_baud_rate": max_baud_rate, "min_baud_rate": min_baud_rate}


def DummyData_ValueUpdate(symbol, event):
    spiMode = event[SOURCE].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey()
    if event["id"] == SPI_CON1__MSTEN:
        symbol.setVisible(spiMode == HOST)
    elif spiMode == HOST and event["id"] == SPI_SPICON_DATA_WIDTH:
        # Use a default value if the key does not exist in dummyDataDict
        dummy_value = dummyDataDict.get(str(event["value"]), 0x0)
        symbol.setValue(dummy_value, 1)
        symbol.setMax(dummy_value)

def setClockGeneratorData(valueGroupEntry):
    clkNode = getValueGroup(SPI,valueGroupEntry).getChildren()
    for bitfield in clkNode:
        if "Clock Generator" in bitfield.getAttribute("caption"):
            return bitfield.getAttribute("caption")

SPI_CON1_MCLKEN_KEY = getValueGroupName(SPI,SPI,CON1,MCLKEN)
CLOCK_GENERATOR = setClockGeneratorData(SPI_CON1_MCLKEN_KEY)

def clockCommentCb(symbol, event):
    updateClockComment(symbol)

def updateClockComment(symbol):
    clockSelSym = symbol.getComponent().getSymbolByID(SPI_CON1_MCLKEN_KEY)
    clockGenFreq = symbol.getComponent().getSymbolValue(CLOCK_FREQ_KEY)
    if clockSelSym.getSelectedKey() == CLOCK_GENERATOR  and clockGenFreq == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


# Define the mapping of channels to IFS registers dynamically
def getIFSRegister(instance):
   if instance == 1:  # SPI instance 1
    return "IFS1"
   elif instance == 2 or instance == 3 :  # SPI instance 2
    return "IFS2"
   return None

def instantiateComponent(spiComponent):

    global interruptEnableList,spiInstanceName
    global interruptHandlerLockList
    interruptEnableList = []
    interruptHandlerLockList = []

    spiInstanceName = spiComponent.createStringSymbol(SPI_INSTANCE_NAME, None)
    spiInstanceName.setVisible(False)
    spiInstanceName.setDefaultValue(spiComponent.getID().upper())
    Log.writeInfoMessage("Running " + spiInstanceName.getValue())

    instanceNumber = spiComponent.createStringSymbol(SPI_INSTANCE_NUM, None)
    instanceNumber.setDefaultValue(spiComponent.getID().upper().replace(SPI, ""))
    instanceNumber.setVisible(False)

    # OperatingMode
    global operatingMode
    operatingMode = createKeyValueSetSymbol(spiComponent, SPI, SPI, CON1, MSTEN)
    operatingMode.setLabel(SPI_SPICON_MSTEN_LABEL)
    operatingMode.setSelectedKey(HOST)
    operatingMode.setReadOnly(False)
    operatingMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")


    # Interrupt Mode
    global spiInterruptMode
    spiInterruptMode = spiComponent.createBooleanSymbol(INTERRUPT_MODE, None)
    spiInterruptMode.setLabel(SPI_INTERRUPT_MODE_LABEL)
    spiInterruptMode.setDefaultValue(True)
    spiInterruptMode.setDependencies(interruptEnableChange, [SPI_CON1__MSTEN,INTERRUPT_MODE])
    spiInstanceNumber = int(spiComponent.getID().upper().replace(SPI, ""))
     # Determine the IFS register for the channel
    ifsRegister = getIFSRegister(spiInstanceNumber)
    if ifsRegister is None:
        Log.writeInfoMessage("No IFS register mapping found for instance {}, channel {}. Skipping.".format(spiInstanceNumber))
        return
    # Add setHelp to the symbol
    spiInterruptMode.setHelp("atmel;device:{};comp:spi_01482;register:{}".format(Variables.get("__PROCESSOR"), ifsRegister))



    ## Clock Source
    clockSource = createKeyValueSetSymbol(spiComponent, SPI, SPI, CON1, MCLKEN)
    clockSource.setLabel(CLOCK_SOURCE_LABEL)
    clockSource.setReadOnly(False)
    clockSource.setDependencies(showHostDependencies, [SPI_CON1__MSTEN])
    clockSource.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")


    # Clock Frequency
    clockFrequency = spiComponent.createIntegerSymbol(CLOCK_FREQ_KEY, None)
    clockFrequency.setLabel(CLOCK_FREQUENCY)
    clockFrequency.setMin(0)
    clockFrequency.setReadOnly(True)
    clockFrequency.setDefaultValue(
        int(Database.getSymbolValue(CORE, STANDARD_SPEED_CLOCK_FREQ))
    )
    clockFrequency.setDependencies(updateClkFreq, [CORE+"."+STANDARD_SPEED_CLOCK_FREQ,CORE+"."+CLOCK_GENERATOR9_FREQ,SPI_CON1__MCLKEN])

    ## Mode
    spiUseSymMode = spiComponent.createMenuSymbol(
        SPI_MODE, None
    )  # No need boolean symbol
    spiUseSymMode.setLabel(MODE_LABEL)
    spiUseSymMode.setDependencies(showModeDependencies, [SPI_MODE])

    ## CLock Polarity
    spiSym_SPICON_CLKPOL = createKeyValueSetSymbol( spiComponent, SPI, SPI, CON1, CKP, spiUseSymMode)
    spiSym_SPICON_CLKPOL.setLabel(SPI_SPICON_CLKPOL_LABEL)
    spiSym_SPICON_CLKPOL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")


    ## Clock Phase Bit
    spiSym_SPICON_CLKPH = createKeyValueSetSymbol( spiComponent, SPI, SPI, CON1, CKE, spiUseSymMode)
    spiSym_SPICON_CLKPH.setLabel(SPI_SPICON_CLKPH_LABEL)
    spiSym_SPICON_CLKPH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")


    ## Mode Comment
    spiSymClockModeComment = spiComponent.createCommentSymbol(
        SPI_CLOCK_MODE_COMMENT, spiUseSymMode
    )
    spiSymClockModeComment.setLabel(SPI_MODE_1_LABEL)
    spiSymClockModeComment.setDependencies(
        clockModeInfo, [SPI_CON1__CKP, SPI_CON1__CKE]
    )

    ## Data Input Sample Phase bit
    spiSym_SPICON_SMP = createKeyValueSetSymbol(spiComponent, SPI, SPI, CON1, SMP)
    spiSym_SPICON_SMP.setLabel(SPI_SPICON_SMP_LABEL)
    spiSym_SPICON_SMP.setDependencies(showHostDependencies, [SPI_CON1__MSTEN])
    spiSym_SPICON_SMP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")




    ####  Maximum Baud Rate:
    #
    # The maximum possible SPI clock frequency occurs when SPIxBRG = 0.
    # Substituting SPIxBRG = 0 into the formula:
    # F_SCK = F_PB / (2 * (0 + 1)) = F_PB / 2
    #
    # Therefore, the maximum baud rate is F_PB / 2.
    #
    ####  Minimum Baud Rate:
    #
    # The minimum baud rate occurs when SPIxBRG = 16383.
    # Substituting SPIxBRG = 16383 into the formula:
    # F_SCK = F_PB / (2 * (16383 + 1)) = F_PB / 32768
    #
    # Therefore, the minimum baud rate is F_PB / 32768

    ## Requested Speed
    reqSpeed = spiComponent.createIntegerSymbol(REQUESTED_SPEED, None)
    reqSpeed.setLabel(SPI_REQUESTED_SPEED_LABEL)
    fbp = clockFrequency.getComponent().getSymbolValue(CLOCK_FREQ_KEY)
    baud_rates = calculateMinMaxBaudRates(fbp)
    reqSpeed.setDefaultValue(1000000)  # discuss default , min and max value
    reqSpeed.setMin(int(baud_rates["min_baud_rate"]))
    reqSpeed.setMax(int(baud_rates["max_baud_rate"]))
    reqSpeed.setDependencies(showHostDependencies, [SPI_CON1__MSTEN])
    reqSpeed.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxBRG")

    ## Calculated Speed
    calcSpeed = spiComponent.createIntegerSymbol(CALCULATED_SPEED, None)
    calcSpeed.setLabel(SPI_CALCULATED_SPEED_LABEL)
    calcSpeed.setReadOnly(True)
    spiMaxBRG = maxThreshold(SPI, SPI, BRG, SPI1BRG)
    calculateFreq = get_calculated_frequency(
        clockFrequency.getValue(), reqSpeed.getValue(), spiMaxBRG
    )
    calcSpeed.setValue(calculateFreq)
    calcSpeed.setDependencies(calcSpeedTrigger, [SPI_BRG_VALUE, SPI_CON1__MSTEN])

    # Max BRG Value
    spiMaxBRGValue = spiComponent.createHexSymbol(SPI_MAX_BRG, None)
    spiMaxBRGValue.setDefaultValue(spiMaxBRG)
    spiMaxBRGValue.setVisible(False)

    # BRG Value
    calculatedBRGValue = spiComponent.createHexSymbol(SPI_BRG_VALUE, None)
    calculatedBRGValue.setVisible(False)
    brg_val = get_brg_value(clockFrequency.getValue(), reqSpeed.getValue(), spiMaxBRGValue.getValue())
    calculatedBRGValue.setDefaultValue(int(brg_val))
    calculatedBRGValue.setDependencies(
        baudRateTrigger, [REQUESTED_SPEED, CLOCK_FREQ_KEY]
    )

    # SPI data width(Mode)
    spiSym_SPICON_MODE = spiComponent.createComboSymbol(SPI_SPICON_DATA_WIDTH, None, SPI_DATA_WIDTHS)
    spiSym_SPICON_MODE.setLabel(SPI_SPICON_DATA_WIDTH_LABEL)
    spiSym_SPICON_MODE.setDefaultValue(SPI_DATA_WIDTHS[0])
    spiSym_SPICON_MODE.setReadOnly(True)
    spiSym_SPICON_SMP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:spi_01482;register:SPIxCON1")


    # Dummy Data
    spiSymDummyData = spiComponent.createHexSymbol(SPI_DUMMY_DATA, None)
    spiSymDummyData.setLabel(SPI_DUMMY_DATA_LABEL)
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setMin(0x0)
    spiSymDummyData.setDependencies(
        DummyData_ValueUpdate, [SPI_SPICON_DATA_WIDTH, SPI_CON1__MSTEN]
    )

    ### CLIENT ####

    # TX_BUFFER_SIZE
    global spisSym_TXBuffer_Size
    spisSym_TXBuffer_Size = spiComponent.createIntegerSymbol(TX_BUFFER_SIZE, None)
    spisSym_TXBuffer_Size.setLabel(SPIS_TX_BUFFER_SIZE_LABEL)
    spisSym_TXBuffer_Size.setMin(1)
    spisSym_TXBuffer_Size.setMax(256)
    spisSym_TXBuffer_Size.setDefaultValue(256)
    spisSym_TXBuffer_Size.setVisible(False)
    spisSym_TXBuffer_Size.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # RX_BUFFER_SIZE
    global spisSym_RXBuffer_Size
    spisSym_RXBuffer_Size = spiComponent.createIntegerSymbol(RX_BUFFER_SIZE, None)
    spisSym_RXBuffer_Size.setLabel(SPIS_RX_BUFFER_SIZE_LABEL)
    spisSym_RXBuffer_Size.setMin(1)
    spisSym_RXBuffer_Size.setMax(256)
    spisSym_RXBuffer_Size.setDefaultValue(256)
    spisSym_RXBuffer_Size.setVisible(False)
    spisSym_RXBuffer_Size.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # CLIENT_SELECT
    spisSym_ClientSelect_Enable = spiComponent.createBooleanSymbol(CLIENT_SELECT, None)
    spisSym_ClientSelect_Enable.setLabel(SPIS_CLIENT_SELECT_ENABLE_LABEL)
    spisSym_ClientSelect_Enable.setValue(True)
    spisSym_ClientSelect_Enable.setReadOnly(True)
    spisSym_ClientSelect_Enable.setVisible(False)
    spisSym_ClientSelect_Enable.setDependencies(
        showClientDependencies, [SPI_CON1__MSTEN]
    )

    # SPIS_CS_PIN
    clientSelectPinList = getChipSelectPinList("SS" + instanceNumber.getValue())

    spisSymCSPin = spiComponent.createKeyValueSetSymbol(SPIS_CS_PIN, None)
    spisSymCSPin.setVisible(False)
    spisSymCSPin.setLabel("Chip Select Pin")
    spisSymCSPin.setOutputMode("Value")
    spisSymCSPin.setDisplayMode("Description")
    for pin in clientSelectPinList:
        spisSymCSPin.addKey(pin, pin, pin)
    spisSymCSPin.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # SPIS_CS_PIN_LOGIC_LEVEL
    spisSymCSPinLogicLevel = spiComponent.createKeyValueSetSymbol(SPIS_CS_PIN_LOGIC_LEVEL, spisSymCSPin)
    spisSymCSPinLogicLevel.setLabel("Chip Select Pin Logic Level")
    spisSymCSPinLogicLevel.setVisible(False)
    spisSymCSPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    spisSymCSPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    spisSymCSPinLogicLevel.setDefaultValue(0)
    spisSymCSPinLogicLevel.setOutputMode("Key")
    spisSymCSPinLogicLevel.setDisplayMode("Description")
    spisSymCSPinLogicLevel.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # SPIS_CS_PIN_CONFIG_COMMENT
    spisSymBusyPinConfigComment = spiComponent.createCommentSymbol(SPIS_CS_PIN_CONFIG_COMMENT, spisSymCSPin)
    spisSymBusyPinConfigComment.setVisible(False)
    spisSymBusyPinConfigComment.setLabel("***Enable Change Notification on the Chip Select pin in Pin Manager***")
    spisSymBusyPinConfigComment.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # SPIS_USE_BUSY_PIN
    spisSymUseBusyPin = spiComponent.createBooleanSymbol(SPIS_USE_BUSY_PIN, None)
    spisSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
    spisSymUseBusyPin.setDefaultValue(True)
    spisSymUseBusyPin.setVisible(False)
    spisSymUseBusyPin.setDependencies(showClientDependencies, [SPI_CON1__MSTEN])

    # SPIS_BUSY_PIN
    spisSymBusyPin = spiComponent.createKeyValueSetSymbol(SPIS_BUSY_PIN, spisSymUseBusyPin)
    spisSymBusyPin.setVisible(False)
    spisSymBusyPin.setLabel("Client Busy Pin")
    spisSymBusyPin.setOutputMode("Value")
    spisSymBusyPin.setDisplayMode("Description")
    spisSymBusyPin.setDependencies(updateSPIClientBusyPinVisibility, [SPI_CON1__MSTEN, SPIS_USE_BUSY_PIN])

    availablePinDictionary = {}

    # Send message to core to get available pins
    availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

    for pad in sort_alphanumeric(availablePinDictionary.values()):
        # key = pad
        # value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)] This is in efficient way
        key, value = next((key, value) for key, value in availablePinDictionary.items() if value == pad)
        description = pad
        spisSymBusyPin.addKey(key, value, description)

    # SPIS_BUSY_PIN_LOGIC_LEVEL
    spisSymBusyPinLogicLevel = spiComponent.createKeyValueSetSymbol(SPIS_BUSY_PIN_LOGIC_LEVEL, spisSymUseBusyPin)
    spisSymBusyPinLogicLevel.setLabel("Client Busy Pin Logic Level")
    spisSymBusyPinLogicLevel.setVisible(False)
    spisSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    spisSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    spisSymBusyPinLogicLevel.setDefaultValue(1)
    spisSymBusyPinLogicLevel.setOutputMode("Key")
    spisSymBusyPinLogicLevel.setDisplayMode("Description")
    spisSymBusyPinLogicLevel.setDependencies(updateSPIClientBusyPinVisibility, [SPI_CON1__MSTEN, SPIS_USE_BUSY_PIN])

    # SPIS_Client_BUSY_PIN_CONFIG_COMMENT
    spisSymBusyPinConfigComment = spiComponent.createCommentSymbol(SPIS_Client_BUSY_PIN_CONFIG_COMMENT, spisSymUseBusyPin)
    spisSymBusyPinConfigComment.setVisible(False)
    spisSymBusyPinConfigComment.setLabel("***Configure Busy pin as GPIO Output in Pin Manager***")
    spisSymBusyPinConfigComment.setDependencies(updateSPIClientBusyPinVisibility, [SPI_CON1__MSTEN, SPIS_USE_BUSY_PIN])

    ##Interrupt Handling
    compPrefix = "SPI"
    compInstance = spiComponent.getID().upper().replace(SPI,"")
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    intSymbolMap["errorInterruptEnableBit"] = intSymbolMap["eInterruptEnableBit"]
    intSymbolMap["errorIsrHandlerName"] = intSymbolMap["eIsrHandlerName"]
    intSymbolMap["errorInterruptFlagBit"] = intSymbolMap["eInterruptFlagBit"]
    del intSymbolMap["eInterruptEnableBit"]
    del intSymbolMap["eIsrHandlerName"]
    del intSymbolMap["eInterruptFlagBit"]
    createInterruptSymbols(spiComponent,intSymbolMap)

    updateInterruptLists(instanceNumber.getValue(), interruptList)

    # Non-pps pin notification
    if(spiInstanceName.getValue() == "SPI2"):
     spi2NonPpsPinsComment = spiComponent.createCommentSymbol("spi2NonPpsPinsComment",None)
     spi2NonPpsPinsComment.setLabel(SPI2_PIN_CONFIGURATION_MESSAGE)

    intComment = spiComponent.createCommentSymbol(INTERRUPT_COMMENT, None)
    intComment.setVisible(False)
    intComment.setLabel(WARNING_INTERRUPT_DISABLED_LABEL)
    intComment.setDependencies(
        interruptCommentCb, [INTERRUPT_MODE] + interruptEnableList
    )

    # Load Time Calculations
    setCoreInterruptSymbols(spiInterruptMode.getValue())
    updateInterruptComment(intComment)

    # Code Generation synbols

    # SPI_CON1__MODE_32_MODE_16
    # Note: For the current dsPIC33A device, we are supporting only 8-bit data width.
    # The `updateDataWidth` callback is intended to handle future cases where 16-bit and 32-bit
    # data widths may be supported. Since these widths are not currently relevant, we are
    # commenting out the dependency for now.
    con1_mode32_mode16 = spiComponent.createStringSymbol(SPI_CON1__MODE_32_MODE_16,None)
    con1_mode32_mode16.setVisible(False)
    con1_mode32_mode16.setDefaultValue("0")

    # Commented out as only 8-bit data width is currently supported:
    # con1_mode32_mode16.setDependencies(updateDataWidth, [SPI_SPICON_DATA_WIDTH])

    # SPI_CON1__ENHBUF
    con1_mode32_mode16 = spiComponent.createStringSymbol("SPI_CON1__ENHBUF",None)
    con1_mode32_mode16.setVisible(False)
    con1_mode32_mode16.setDefaultValue("1")

    # SPI_SPICON_MODE
    spi_con_mode = spiComponent.createStringSymbol("SPI_SPICON_MODE",None)
    spi_con_mode.setVisible(False)
    spi_con_mode.setDefaultValue("0")

    # clkSrcGenNumber
    clkSrcGenNumber = spiComponent.createStringSymbol("clkSrcGenNumber", None)
    clkSrcGenNumber.setDefaultValue(NINE)
    clkSrcGenNumber.setVisible(False)

    # String symbol for the POR (Power-On Reset) values of registers
    registers_spi = ["CON1","CON2","BRG","IMSK","STAT"]
    reg_por_set  = create_reg_por_set_string(SPI, SPI, registers_spi )
    regPorSet = spiComponent.createStringSymbol("regPorSet", None)
    regPorSet.setDefaultValue(reg_por_set)
    regPorSet.setVisible(False)

    # Clock warning message
    clkComment = spiComponent.createCommentSymbol("CLOCK_COMMENT", None)
    clkComment.setVisible(False)
    clkComment.setLabel("Warning!!! Enable and configure " +  CLOCK_GENERATOR + " in Clock Section of System Module")
    clkComment.setDependencies(clockCommentCb, [CLOCK_FREQ_KEY , SPI_CON1_MCLKEN_KEY])

    # Driver Symbols Start
    #SPI 8-bit Character size Mask
    spiSym_CON1_8BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
    spiSym_CON1_8BIT.setDefaultValue("0x00000000")
    spiSym_CON1_8BIT.setVisible(False)

    #SPI Clock Phase Leading Edge Mask
    spiSym_CON1_LE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CON1_LE_Mask.setDefaultValue("0x00000100")
    spiSym_CON1_LE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CON1_TE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CON1_TE_Mask.setDefaultValue("0x00000000")
    spiSym_CON1_TE_Mask.setVisible(False)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CON1_IL_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CON1_IL_Mask.setDefaultValue("0x00000000")
    spiSym_CON1_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CON1_IH_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CON1_IH_Mask.setDefaultValue("0x00000040")
    spiSym_CON1_IH_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = spiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue(spiInstanceName.getValue())
    spiSym_API_Prefix.setVisible(False)

    #SPI Transmit data register
    transmitRegister = spiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&(" + spiInstanceName.getValue() + "BUF)")
    transmitRegister.setVisible(False)

    #SPI Receive data register
    receiveRegister = spiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&(" + spiInstanceName.getValue() + "BUF)")
    receiveRegister.setVisible(False)
    # Driver Symbols End

    ###### Code Generation File Handling #########

    configName = Variables.get("__CONFIGURATION_NAME")

    # SPI HOST files
    spimCommonHeaderFile = spiComponent.createFileSymbol("SPI_COMMON_HEADER", None)
    spimCommonHeaderFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_host_common.h")
    spimCommonHeaderFile.setOutputName("plib_spi_host_common.h")
    spimCommonHeaderFile.setDestPath("peripheral/spi/spi_host")
    spimCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_host")
    spimCommonHeaderFile.setType("HEADER")
    spimCommonHeaderFile.setMarkup(False)
    spimCommonHeaderFile.setOverwrite(True)
    spimCommonHeaderFile.setEnabled(operatingMode.getSelectedKey() == HOST)
    spimCommonHeaderFile.setDependencies(spiHostModeFileGeneration, [SPI_CON1__MSTEN])

    spimHeaderFile = spiComponent.createFileSymbol("SPI_HEADER", None)
    spimHeaderFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_host.h.ftl")
    spimHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_host.h")
    spimHeaderFile.setDestPath("/peripheral/spi/spi_host")
    spimHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_host")
    spimHeaderFile.setType("HEADER")
    spimHeaderFile.setMarkup(True)
    spimHeaderFile.setEnabled(operatingMode.getSelectedKey() == HOST)
    spimHeaderFile.setDependencies(spiHostModeFileGeneration, [SPI_CON1__MSTEN])

    spimSourceFile = spiComponent.createFileSymbol("SPI_SOURCE", None)
    spimSourceFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_host.c.ftl")
    spimSourceFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_host.c")
    spimSourceFile.setDestPath("/peripheral/spi/spi_host")
    spimSourceFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_host")
    spimSourceFile.setType("SOURCE")
    spimSourceFile.setMarkup(True)
    spimSourceFile.setEnabled(operatingMode.getSelectedKey() == HOST)
    spimSourceFile.setDependencies(spiHostModeFileGeneration, [SPI_CON1__MSTEN])

    # SPI CLIENT files
    spisCommonHeaderFile = spiComponent.createFileSymbol("SPIS_COMMON_HEADER", None)
    spisCommonHeaderFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_client_common.h")
    spisCommonHeaderFile.setOutputName("plib_spi_client_common.h")
    spisCommonHeaderFile.setDestPath("peripheral/spi/spi_client")
    spisCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_client")
    spisCommonHeaderFile.setType("HEADER")
    spisCommonHeaderFile.setMarkup(False)
    spisCommonHeaderFile.setOverwrite(True)
    spisCommonHeaderFile.setEnabled(operatingMode.getSelectedKey() == CLIENT)
    spisCommonHeaderFile.setDependencies(spiClientModeFileGeneration, [SPI_CON1__MSTEN])

    spisHeaderFile = spiComponent.createFileSymbol("SPIS_HEADER", None)
    spisHeaderFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_client.h.ftl")
    spisHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_client.h")
    spisHeaderFile.setDestPath("/peripheral/spi/spi_client")
    spisHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_client")
    spisHeaderFile.setType("HEADER")
    spisHeaderFile.setMarkup(True)
    spisHeaderFile.setEnabled(operatingMode.getSelectedKey() == CLIENT)
    spisHeaderFile.setDependencies(spiClientModeFileGeneration, [SPI_CON1__MSTEN])

    spisSourceFile = spiComponent.createFileSymbol("SPIS_SOURCE", None)
    spisSourceFile.setSourcePath("../peripheral/spi_01482/templates/plib_spi_client.c.ftl")
    spisSourceFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_client.c")
    spisSourceFile.setDestPath("/peripheral/spi/spi_client")
    spisSourceFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_client")
    spisSourceFile.setType("SOURCE")
    spisSourceFile.setMarkup(True)
    spisSourceFile.setEnabled(operatingMode.getSelectedKey() == CLIENT)
    spisSourceFile.setDependencies(spiClientModeFileGeneration, [SPI_CON1__MSTEN])

    # Common files
    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_01482/templates/system/initialization.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_01482/templates/system/definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)

def getChipSelectPinList(ss_pin):
    # parse XML
    gpioIP = "gpio_04928"
    currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    gpioPlibPath = os.path.split(currentPath)[0]
    gpioPlibPath = os.path.split(gpioPlibPath)[0]
    gpioPlibPath = os.path.join(gpioPlibPath, gpioIP)
    deviceXmlPath = os.path.join(gpioPlibPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
    deviceXmlTree = ET.parse(deviceXmlPath)
    deviceXmlRoot = deviceXmlTree.getroot()

    familiesXmlName = deviceXmlRoot.get("families")
    familiesXmlPath = os.path.join(gpioPlibPath, "plugin/pin_xml/families/" + familiesXmlName + ".xml")
    familiesXmlPath = os.path.normpath(familiesXmlPath)
    familiesXmlTree = ET.parse(familiesXmlPath)
    familiesXmlRoot = familiesXmlTree.getroot()

    pinoutXmlName = deviceXmlRoot.get("pins")
    pinoutXmlPath = os.path.join(gpioPlibPath, "plugin/pin_xml/pins/" + pinoutXmlName + ".xml")
    pinoutXmlPath = os.path.normpath(pinoutXmlPath)
    pinoutXmlTree = ET.parse(pinoutXmlPath)
    pinoutXmlRoot = pinoutXmlTree.getroot()

    # Get all elements with tag = "group" and having attribute "id"
    group_elements = familiesXmlRoot.findall(".//group/[@id]")
    # Get a list of all group elements. Each element of list is a dictionary.
    # key is tag and value is attribute which is another dictionary.
    group_elements_list = [{t.tag : t.attrib} for t in group_elements]
    final_pin_list = []
    for group_elem in group_elements_list:
        target_elements = familiesXmlRoot.findall(".//group/[@id='" + group_elem["group"]["id"] + "']/*")
        # Create a list containing a dictionary of "tag":"attrib"
        # Each element of list is a dictionary. t.attrib is another dictionary.
        result = [{t.tag : t.attrib} for t in target_elements]
        for dic in result:
            if "function" in dic:
                if ss_pin in dic["function"]["name"] and dic["function"]["direction"] == "in":
                    # Found the group containing the SSx function
                    for dic in result:
                        if "pin" in dic:
                            pin = dic["pin"]["name"]
                            # Discard any pin that does not start with character 'R'. Example: "PTG30"
                            if pin.startswith('R'):
                                pinFromFamilyXml = pin.replace('P', '')
                                # make the pin part of list only if it is present in pin xml
                                for pin in pinoutXmlRoot.iter("pin"):
                                    if pinFromFamilyXml == pin.get('name'):
                                        final_pin_list.append(pinFromFamilyXml)
                                        break
                    break
    # for some of the devices like PIC32MM, few SPI instances have fixed SSx pins, get their pin name from pin xml
    # for some of the devices like PIC32MZW1, few spi instances have fixed SSx pins as well as mappable SSx pins
    # so its needed to run through pin xml file as well and find such instances
    for pin in pinoutXmlRoot.iter("pin"):
        for function in pin.iter("function"):
            if ss_pin == function.get('name'):
                final_pin_list.append(pin.get('name'))
                break

    final_pin_list.sort()
    return final_pin_list

# Code Generation Helper Functions

# Updates 'SPI_CON1__MODE_32_MODE_16' and 'SPI_CLIENT_MODE' symbols based on the selected 'SPI_SPICON_DATA_WIDTH' value.
def updateDataWidth(symbol, event):

    dataWidthSym = symbol.getComponent().getSymbolValue(SPI_SPICON_DATA_WIDTH)
    mode32_mode16_Sym = symbol.getComponent().getSymbolByID(SPI_CON1__MODE_32_MODE_16)
    spi_con_mode = symbol.getComponent().getSymbolByID("SPI_SPICON_MODE")
    # Define mappings
    mode_mapping = {
        "8 bit": {"mode_value": "0", "client_data_width_mode": "0"},
        "16 bit": {"mode_value": "1", "client_data_width_mode": "1"},
        "32 bit": {"mode_value": "2", "client_data_width_mode": ""}
    }

    # Update based on data width, ensuring keys exist
    if dataWidthSym in mode_mapping:
        mode32_mode16_Sym.setValue(mode_mapping[dataWidthSym]["mode_value"])
        spi_con_mode.setValue(mode_mapping[dataWidthSym]["client_data_width_mode"])
        Log.writeInfoMessage("SPI_SPICON_DATA_WIDTH updated: '{}', SPI_CON1__MODE_32_MODE_16 set to '{}' , SPI_SPICON_MODE:'{}'."
                            .format(dataWidthSym, mode_mapping[dataWidthSym]["mode_value"], mode_mapping[dataWidthSym]["client_data_width_mode"]))

    else:
        Log.writeWarningMessage("Invalid SPI_SPICON_DATA_WIDTH: '{}'.".format(dataWidthSym))




def spiHostModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey() == HOST)

def spiClientModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID(SPI_CON1__MSTEN).getSelectedKey() == CLIENT)

#Interrupt related Helper Function

def getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList):
    intSymbolMap= {}
    intEntryCount = len(interruptList)
    intFlagList = [compPrefix+compInstance+interrupt+"IF" for interrupt in interruptList]
    flagRegisterGroup = getModuleRegisterGroup("intc","IFS")
    isflagDataAdded = False
    if(flagRegisterGroup != None):
        for registerNode in flagRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intFlagList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IF","").lower() + "InterruptFlagBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isflagDataAdded = True
                        break
            if isflagDataAdded:
                break

    intEntryCount = 2*intEntryCount
    isEnableDataAdded = False
    intEnableList = [compPrefix+compInstance+interrupt+"IE" for interrupt in interruptList]
    enableRegisterGroup = getModuleRegisterGroup("intc","IEC")
    if(enableRegisterGroup != None):
        for registerNode in enableRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intEnableList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IE","").lower() + "InterruptEnableBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break

    for interrupt in interruptList:
        intSymbolName = interrupt.lower() + "IsrHandlerName"
        intSymbolMap[intSymbolName] = compPrefix + compInstance +interrupt+"_InterruptHandler"

    return intSymbolMap

def createInterruptSymbols(component,intSymbolMap):
    for key in intSymbolMap:
        interruptSymbol = component.createStringSymbol(key, None)
        interruptSymbol.setDefaultValue(intSymbolMap[key])
        interruptSymbol.setVisible(False)


def create_reg_por_set_string(module, register_group, registers):
    """
    Generates a formatted string of default register values for a given module, register group, and list of registers.
    """
    reg_defaults = OrderedDict()  # Use OrderedDict to maintain the insertion order
    reg_por_set = ""  # Initialize the regPorSet output string

    module_name = spiInstanceName.getValue()
    match = re.search(r"\d+$", module_name)
    instance_number = match.group(0) if match else ""  # Extract instance number

    for reg in registers:
        reg_name = "{}{}{}".format( register_group, instance_number, reg)  # Form key as register_group + instanceNumber + reg
        reg_defaults[reg_name] = getRegisterDefaultValue(module, register_group, reg)

    # Format the output string with 4-space indentation per register
    for reg_name, default_val in reg_defaults.items():
        reg_por_set += "    {} = {};\n".format(reg_name, default_val)

    return reg_por_set


def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
    # Path to the register node in the ATDF structure
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, register_group, register
    )
    # Retrieve the register node
    register_node = ATDF.getNode(reg_path)

    # If the register node is found, fetch and return the initval as hex; otherwise, return "0x0UL"
    if register_node is not None:
        reg_default_val = register_node.getAttribute("initval")
        return "{}UL".format(reg_default_val) if reg_default_val else "0x0UL"
    return "0x0UL"
