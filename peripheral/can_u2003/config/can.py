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

global interruptVector
global interruptHandler
global interruptHandlerLock

canElementSizes = ["8 bytes", "12 bytes", "16 bytes", "20 bytes", "24 bytes", "32 bytes", "48 bytes", "64 bytes"]
opModeValues = ["NORMAL", "CAN FD"]

stdFilterList = []
extFilterList = []

# if the mode is changed to FD, then show options for more bytes
def showWhenFD(element, event):
    if event["value"] == 'CAN FD':
        element.setVisible(True)
    else:
        element.setVisible(False)

# Rx Buffer Element size
def RxBufferElementSize(element, event):
    if ((event["id"] == 'CAN_OPMODE' and event["value"] == 'CAN FD' and Database.getSymbolValue(canInstanceName.getValue().lower(), "RXBUF_USE") == True)
    or (event["id"] == 'RXBUF_USE' and event["value"] == True and Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_OPMODE") == 'CAN FD')):
        element.setVisible(True)
        element.setReadOnly(False)
    else:
        element.setVisible(False)
        element.setReadOnly(True)

# for FD. Expects keyValue symbol. Use for RX and TX
def adornElementSize(fifo):
    fifo.addKey("8 bytes",  "0", "8 Bytes")
    fifo.addKey("12 bytes", "1", "12 Bytes")
    fifo.addKey("16 bytes", "2", "16 Bytes")
    fifo.addKey("20 bytes", "3", "20 Bytes")
    fifo.addKey("24 bytes", "4", "24 Bytes")
    fifo.addKey("32 bytes", "5", "32 Bytes")
    fifo.addKey("48 bytes", "6", "48 Bytes")
    fifo.addKey("64 bytes", "7", "64 Bytes")
    fifo.setDefaultValue(0)
    fifo.setOutputMode("Value")
    fifo.setDisplayMode("Description")

# if mode is changed to NORMAL then set element size to 8 bytes
def updateElementSize(symbol, event):
    if event["value"] == 'CAN FD':
        symbol.setVisible(True)
        symbol.setReadOnly(False)
    else:
        symbol.setVisible(False)
        symbol.setReadOnly(True)

# for extended and standard filters
def adornFilterType(filterType):
    filterType.addKey("Range",   "0", "Based on Range")
    filterType.addKey("Dual",    "1", "Based on Dual ID")
    filterType.addKey("Classic", "2", "Based on Classic Mask/Value")
    filterType.setOutputMode("Value")
    filterType.setDisplayMode("Key")
    filterType.setDefaultValue(0)

# for extended and standard filter configurations
def adornFilterConfig(config):
    config.addKey("Disabled",   "0", "Filter is Disabled")
    config.addKey("RXF0",       "1", "Store in RX FIFO 0")
    config.addKey("RXF1",       "2", "Store in RX FIFO 1")
    config.addKey("Reject",     "3", "Reject")
    config.addKey("Priority",   "4", "Set priority")
    config.addKey("Priority0",  "5", "Set priority and store in FIFO 0")
    config.addKey("Priority1",  "6", "Set priority and store in FIFO 1")
    config.addKey("RXBUF",      "7", "Store into Rx Buffer")
    config.setOutputMode("Value")
    config.setDisplayMode("Description")
    config.setDefaultValue(1)

def standardFilterRangeCheck(symbol, event):
    filterNumber = event["id"].split("_")[2].split("FILTER")[1]
    if Database.getSymbolValue(canInstanceName.getValue().lower(),
                               canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE") == 0:
        id1 = Database.getSymbolValue(canInstanceName.getValue().lower(),
                                   canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1")
        id2 = Database.getSymbolValue(canInstanceName.getValue().lower(),
                                      canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2")
        if id1 > id2:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def canCreateStdFilter(component, menu, filterNumber):
    stdFilter = component.createMenuSymbol(canInstanceName.getValue() + "_STD_FILTER"+ str(filterNumber), menu)
    stdFilter.setLabel("Standard Filter " + str(filterNumber))
    stdFilterType = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE", stdFilter)
    stdFilterType.setLabel("Type")
    adornFilterType(stdFilterType)
    sfid1 = component.createIntegerSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setLabel("ID1")
    sfid1.setMin(0)
    sfid1.setMax(2047)
    sfid2 = component.createIntegerSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setLabel("ID2")
    sfid2.setMin(0)
    sfid2.setMax(2047)

    stdFilterRangeInvalidSym = component.createCommentSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_COMMENT", stdFilter)
    stdFilterRangeInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Standard Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    stdFilterRangeInvalidSym.setVisible(False)
    stdFilterRangeInvalidSym.setDependencies(standardFilterRangeCheck, [canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE",
                                                                        canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1",
                                                                        canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2"])

    config = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    config.setLabel("Element Configuration")
    adornFilterConfig(config)

    stdFilter.setVisible(False)
    stdFilter.setEnabled(False)
    return stdFilter

def extendedFilterRangeCheck(symbol, event):
    filterNumber = event["id"].split("_")[2].split("FILTER")[1]
    if Database.getSymbolValue(canInstanceName.getValue().lower(),
                               canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE") == 0:
        id1 = Database.getSymbolValue(canInstanceName.getValue().lower(),
                                   canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1")
        id2 = Database.getSymbolValue(canInstanceName.getValue().lower(),
                                      canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2")
        if id1 > id2:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def canCreateExtFilter(component, menu, filterNumber):
    extFilter = component.createMenuSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber), menu)
    extFilter.setLabel("Extended Filter " + str(filterNumber))
    extFilterType = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE", extFilter)
    extFilterType.setLabel("Type")
    adornFilterType(extFilterType)
    efid1 = component.createIntegerSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setLabel("ID1")
    efid1.setMin(0)
    efid1.setMax(536870911)
    efid2 = component.createIntegerSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setLabel("ID2")
    efid2.setMin(0)
    efid2.setMax(536870911)

    extFilterRangeInvalidSym = component.createCommentSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_COMMENT", extFilter)
    extFilterRangeInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Extended Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    extFilterRangeInvalidSym.setVisible(False)
    extFilterRangeInvalidSym.setDependencies(extendedFilterRangeCheck, [canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE",
                                                                        canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1",
                                                                        canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2"])

    config = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
    config.setLabel("Element Configuration")
    adornFilterConfig(config)

    extFilter.setVisible(False)
    extFilter.setEnabled(False)
    return extFilter

# adjust how many standard filters are shown based on number entered
def adjustStdFilters(filterList, event):
    for filter in stdFilterList[:event["value"]]:
        if filter.getVisible() != True:
            filter.setVisible(True)
            filter.setEnabled(True)
    for filter in stdFilterList[event["value"]:]:
        if filter.getVisible() != False:
            filter.setVisible(False)
            filter.setEnabled(False)

# adjust how many extended filters are shown based on number entered
def adjustExtFilters(filterList, event):
    for filter in extFilterList[:event["value"]]:
        if filter.getVisible() != True:
            filter.setVisible(True)
            filter.setEnabled(True)
    for filter in extFilterList[event["value"]:]:
        if filter.getVisible() != False:
            filter.setVisible(False)
            filter.setEnabled(False)

def interruptControl(symbol, event):
    if event["value"] == True:
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, canInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, canInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):
    if (Database.getSymbolValue(canInstanceName.getValue().lower(), "INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

def canCoreClockFreq(symbol, event):
    symbol.setValue(int(Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def bitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")

    if (bitTiming == "Data"):
        prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "DBTP_DBRP")
        bitrate = Database.getSymbolValue(canInstanceName.getValue().lower(), "DATA_BITRATE")
        samplePoint = Database.getSymbolValue(canInstanceName.getValue().lower(), "DATA_SAMPLE_POINT")
    else:
        prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "NBTP_NBRP")
        bitrate = Database.getSymbolValue(canInstanceName.getValue().lower(), "NOMINAL_BITRATE")
        samplePoint = Database.getSymbolValue(canInstanceName.getValue().lower(), "NOMINAL_SAMPLE_POINT")

    numOfTimeQuanta = clk / ((bitrate * 1000) * (prescaler + 1))
    if (numOfTimeQuanta < lowTq):
        canTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too low for required " + bitTiming + " Bit Timing")
        canTimeQuantaInvalidSym.setVisible(True)
        canCoreClockInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Clock Frequency is too low for required " + bitTiming + " Bit Timing")
        canCoreClockInvalidSym.setVisible(True)
    elif (numOfTimeQuanta > highTq):
        canTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too high for required " + bitTiming + " Bit Timing")
        canTimeQuantaInvalidSym.setVisible(True)
        canCoreClockInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Clock Frequency is too high for required " + bitTiming + " Bit Timing")
        canCoreClockInvalidSym.setVisible(True)
    else:
        canTimeQuantaInvalidSym.setVisible(False)
        canCoreClockInvalidSym.setVisible(False)

    tseg1 = int((numOfTimeQuanta * samplePoint) / 100.0)
    tseg2 = numOfTimeQuanta - tseg1 - 1
    tseg1 -= 2

    return tseg1, tseg2

def dataBitTimingCalculation(symbol, event):
    if (Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_OPMODE") == "CAN FD"):
        tseg1, tseg2 = bitTimingCalculation("Data", 4, 49)
        Database.setSymbolValue(canInstanceName.getValue().lower(), "DBTP_DTSEG1", tseg1, 2)
        Database.setSymbolValue(canInstanceName.getValue().lower(), "DBTP_DTSEG2", tseg2, 2)

def nominalBitTimingCalculation(symbol, event):
    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "NBTP_NTSEG1", tseg1, 2)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "NBTP_NTSEG2", tseg2, 2)

def instantiateComponent(canComponent):
    global canInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    global canCoreClockInvalidSym
    global canTimeQuantaInvalidSym

    canInstanceName = canComponent.createStringSymbol("CAN_INSTANCE_NAME", None)
    canInstanceName.setVisible(False)
    canInstanceName.setDefaultValue(canComponent.getID().upper())
    print("Running " + canInstanceName.getValue())

    def hideMenu(menu, event):
        menu.setVisible(event["value"])

    #either the watermark % changed or the number of elements
    def RXF0WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(canInstanceName.getValue().lower(), "RXF0_WP")
        number_of_elements   = Database.getSymbolValue(canInstanceName.getValue().lower(), "RXF0_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def RXF1WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(canInstanceName.getValue().lower(), "RXF1_WP")
        number_of_elements   = Database.getSymbolValue(canInstanceName.getValue().lower(), "RXF1_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def TXWatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(canInstanceName.getValue().lower(), "TX_FIFO_WP")
        number_of_elements   = Database.getSymbolValue(canInstanceName.getValue().lower(), "TX_FIFO_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    # Initialize peripheral clock
    Database.setSymbolValue("core", canInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)

    # CAN operation mode - default to FD
    canOpMode = canComponent.createComboSymbol("CAN_OPMODE", None, opModeValues)
    canOpMode.setLabel("CAN Operation Mode")
    canOpMode.setDefaultValue("NORMAL")

    canInterruptMode = canComponent.createBooleanSymbol("INTERRUPT_MODE", None)
    canInterruptMode.setLabel("Interrupt Mode")
    canInterruptMode.setDefaultValue(False)

    interruptVector = canInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = canInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = canInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = canInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # CAN Bit Timing Calculation
    canBitTimingCalculationMenu = canComponent.createMenuSymbol("BIT_TIMING_CALCULATION", None)
    canBitTimingCalculationMenu.setLabel("Bit Timing Calculation")
    canBitTimingCalculationMenu.setDescription("CAN Bit Timing Calculation for Normal and CAN-FD Operation")

    canCoreClockValue = canComponent.createIntegerSymbol("CAN_CORE_CLOCK_FREQ", canBitTimingCalculationMenu)
    canCoreClockValue.setLabel("Clock Frequency")
    canCoreClockValue.setReadOnly(True)
    canCoreClockValue.setDefaultValue(int(Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    canCoreClockValue.setVisible(True)
    canCoreClockValue.setDependencies(canCoreClockFreq, ["core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canCoreClockInvalidSym = canComponent.createCommentSymbol("CAN_CORE_CLOCK_INVALID_COMMENT", None)
    canCoreClockInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Clock Frequency is too low for required Nominal Bit Timing")
    canCoreClockInvalidSym.setVisible((canCoreClockValue.getValue() == 0))

    canTimeQuantaInvalidSym = canComponent.createCommentSymbol("CAN_TIME_QUANTA_INVALID_COMMENT", None)
    canTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too low for required Nominal Bit Timing")
    canTimeQuantaInvalidSym.setVisible(False)

    # CAN Nominal Bit Timing Calculation
    canNominalBitTimingMenu = canComponent.createMenuSymbol("NOMINAL_BIT_TIMING_CALCULATION", canBitTimingCalculationMenu)
    canNominalBitTimingMenu.setLabel("Nominal Bit Timing")
    canNominalBitTimingMenu.setDescription("This timing must be less or equal to the CAN-FD Data Bit Timing if used")

    canNominalBitrate = canComponent.createIntegerSymbol("NOMINAL_BITRATE", canNominalBitTimingMenu)
    canNominalBitrate.setLabel("Bit Rate (Kbps)")
    canNominalBitrate.setMin(1)
    canNominalBitrate.setMax(1000)
    canNominalBitrate.setDefaultValue(500)
    canNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canNominalSamplePoint = canComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", canNominalBitTimingMenu)
    canNominalSamplePoint.setLabel("Sample Point %")
    canNominalSamplePoint.setMin(50.0)
    canNominalSamplePoint.setMax(100.0)
    canNominalSamplePoint.setDefaultValue(75.0)
    canNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])

    NBTPsyncJump = canComponent.createIntegerSymbol("NBTP_NSJW", canNominalBitTimingMenu)
    NBTPsyncJump.setLabel("Synchronization Jump Width")
    NBTPsyncJump.setMin(0)
    NBTPsyncJump.setMax(127)
    NBTPsyncJump.setDefaultValue(3)

    NBTPprescale = canComponent.createIntegerSymbol("NBTP_NBRP", canNominalBitTimingMenu)
    NBTPprescale.setLabel("Bit Rate Prescaler")
    NBTPprescale.setMin(0)
    NBTPprescale.setMax(511)
    NBTPprescale.setDefaultValue(0)
    NBTPprescale.setDependencies(nominalBitTimingCalculation, ["NBTP_NBRP"])

    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)

    NBTPBeforeSP = canComponent.createIntegerSymbol("NBTP_NTSEG1", canNominalBitTimingMenu)
    NBTPBeforeSP.setLabel("Time Segment Before Sample Point")
    NBTPBeforeSP.setMin(1)
    NBTPBeforeSP.setMax(255)
    NBTPBeforeSP.setDefaultValue(tseg1)
    NBTPBeforeSP.setReadOnly(True)

    NBTPAfterSP = canComponent.createIntegerSymbol("NBTP_NTSEG2", canNominalBitTimingMenu)
    NBTPAfterSP.setLabel("Time Segment After Sample Point")
    NBTPAfterSP.setMin(0)
    NBTPAfterSP.setMax(127)
    NBTPAfterSP.setDefaultValue(tseg2)
    NBTPAfterSP.setReadOnly(True)

    # CAN Data Bit Timing Calculation
    canDataBitTimingMenu = canComponent.createMenuSymbol("DATA_BIT_TIMING_CALCULATION", canBitTimingCalculationMenu)
    canDataBitTimingMenu.setLabel("Data Bit Timing")
    canDataBitTimingMenu.setDescription("This timing must be greater or equal to the Nominal Bit Timing")
    canDataBitTimingMenu.setVisible(False)
    canDataBitTimingMenu.setDependencies(showWhenFD, ["CAN_OPMODE"])

    canDataBitrate = canComponent.createIntegerSymbol("DATA_BITRATE", canDataBitTimingMenu)
    canDataBitrate.setLabel("Bit Rate (Kbps)")
    canDataBitrate.setMin(1)
    canDataBitrate.setDefaultValue(500)
    canDataBitrate.setDependencies(dataBitTimingCalculation, ["DATA_BITRATE", "CAN_OPMODE", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canDataSamplePoint = canComponent.createFloatSymbol("DATA_SAMPLE_POINT", canDataBitTimingMenu)
    canDataSamplePoint.setLabel("Sample Point %")
    canDataSamplePoint.setMin(50.0)
    canDataSamplePoint.setMax(100.0)
    canDataSamplePoint.setDefaultValue(75.0)
    canDataSamplePoint.setDependencies(dataBitTimingCalculation, ["DATA_SAMPLE_POINT"])

    DBTPsyncJump = canComponent.createIntegerSymbol("DBTP_DSJW", canDataBitTimingMenu)
    DBTPsyncJump.setLabel("Synchronization Jump Width")
    DBTPsyncJump.setMin(0)
    DBTPsyncJump.setDefaultValue(3)
    DBTPsyncJump.setMax(7)

    DBTPprescale = canComponent.createIntegerSymbol("DBTP_DBRP", canDataBitTimingMenu)
    DBTPprescale.setLabel("Bit Rate Prescaler")
    DBTPprescale.setMin(0)
    DBTPprescale.setMax(31)
    DBTPprescale.setDefaultValue(0)
    DBTPprescale.setDependencies(dataBitTimingCalculation, ["DBTP_DBRP"])

    DBTPBeforeSP = canComponent.createIntegerSymbol("DBTP_DTSEG1", canDataBitTimingMenu)
    DBTPBeforeSP.setLabel("Time Segment Before Sample Point")
    DBTPBeforeSP.setMin(1)
    DBTPBeforeSP.setMax(31)
    DBTPBeforeSP.setDefaultValue(10)
    DBTPBeforeSP.setReadOnly(True)

    DBTPAfterSP = canComponent.createIntegerSymbol("DBTP_DTSEG2", canDataBitTimingMenu)
    DBTPAfterSP.setLabel("Time Segment After Sample Point")
    DBTPAfterSP.setMin(0)
    DBTPAfterSP.setDefaultValue(3)
    DBTPAfterSP.setMax(15)
    DBTPAfterSP.setReadOnly(True)

    # ----- Rx FIFO 0 -----
    canRXF0 = canComponent.createBooleanSymbol("RXF0_USE", None)
    canRXF0.setLabel("Use RX FIFO 0")
    canRXF0.setDefaultValue(True)
    canRXF0.setReadOnly(True)

    canRXF0Menu = canComponent.createMenuSymbol("rxf0Menu", canRXF0)
    canRXF0Menu.setLabel("RX FIFO 0 Settings")
    canRXF0Menu.setDependencies(hideMenu, ["RXF0_USE"])

    # number of RX FIFO 0 elements
    canRXF0Elements = canComponent.createIntegerSymbol("RXF0_ELEMENTS", canRXF0Menu)
    canRXF0Elements.setLabel("Number of Elements")
    canRXF0Elements.setDefaultValue(1)
    canRXF0Elements.setMin(0)
    canRXF0Elements.setMax(64)

    canRXF0watermarkP = canComponent.createIntegerSymbol("RXF0_WP", canRXF0Menu)
    canRXF0watermarkP.setLabel("Watermark %")
    canRXF0watermarkP.setDefaultValue(0)
    canRXF0watermarkP.setMin(0)
    canRXF0watermarkP.setMax(99)

    #This is a computed value
    canRXF0watermark = canComponent.createIntegerSymbol("RXF0_WATERMARK", canRXF0Menu)
    canRXF0watermark.setLabel("Watermark at element")
    canRXF0watermark.setDescription("A value of 0 disables watermark")
    canRXF0watermark.setDefaultValue(0)
    canRXF0watermark.setReadOnly(True)
    canRXF0watermark.setDependencies(RXF0WatermarkUpdate, ["RXF0_ELEMENTS", "RXF0_WP"])

    canRXF0elementSize = canComponent.createKeyValueSetSymbol("RXF0_BYTES_CFG", canRXF0Menu)
    canRXF0elementSize.setLabel("Element Size")
    canRXF0elementSize.setVisible(False)
    adornElementSize(canRXF0elementSize)
    canRXF0elementSize.setDependencies(updateElementSize, ["CAN_OPMODE"])

    canRx0overwrite = canComponent.createBooleanSymbol("RXF0_OVERWRITE", canRXF0Menu)
    canRx0overwrite.setLabel("Use Overwrite Mode")
    canRx0overwrite.setDescription("Overwrite RX FIFO 0 entries without blocking")
    canRx0overwrite.setDefaultValue(True)

    # ----- Rx FIFO 1 -----
    canRXF1 = canComponent.createBooleanSymbol("RXF1_USE", None)
    canRXF1.setLabel("Use RX FIFO 1")
    canRXF1.setDefaultValue(True)

    canRXF1Menu = canComponent.createMenuSymbol("rxf1menu", canRXF1)
    canRXF1Menu.setLabel("RX FIFO 1 Settings")
    canRXF1Menu.setDependencies(hideMenu, ["RXF1_USE"])

    canRXF1Elements = canComponent.createIntegerSymbol("RXF1_ELEMENTS", canRXF1Menu)
    canRXF1Elements.setLabel("Number of Elements")
    canRXF1Elements.setDefaultValue(1)
    canRXF1Elements.setMin(1)
    canRXF1Elements.setMax(64)

    canRXF1watermarkP = canComponent.createIntegerSymbol("RXF1_WP", canRXF1Menu)
    canRXF1watermarkP.setLabel("Watermark %")
    canRXF1watermarkP.setDefaultValue(0)
    canRXF1watermarkP.setMin(0)
    canRXF1watermarkP.setMax(99)

    #This is a computed value for watermark
    canRX1watermark = canComponent.createIntegerSymbol("RXF1_WATERMARK", canRXF1Menu)
    canRX1watermark.setLabel("Watermark at element")
    canRX1watermark.setDescription("A value of 0 disables watermark")
    canRX1watermark.setDefaultValue(0)
    canRX1watermark.setReadOnly(True)
    canRX1watermark.setDependencies(RXF1WatermarkUpdate, ["RXF1_ELEMENTS", "RXF1_WP"])

    canRXF1elementSize = canComponent.createKeyValueSetSymbol("RXF1_BYTES_CFG", canRXF1Menu)
    canRXF1elementSize.setLabel("Element Size")
    canRXF1elementSize.setVisible(False)
    adornElementSize(canRXF1elementSize)
    canRXF1elementSize.setDependencies(updateElementSize, ["CAN_OPMODE"])

    canRXF1overwrite = canComponent.createBooleanSymbol("RXF1_OVERWRITE", canRXF1Menu)
    canRXF1overwrite.setLabel("Use Overwrite Mode")
    canRXF1overwrite.setDescription("Overwrite RX FIFO 1 entries without blocking")
    canRXF1overwrite.setDefaultValue(True)

    # ----- Rx Buffer -----
    canRXBuf = canComponent.createBooleanSymbol("RXBUF_USE", None)
    canRXBuf.setLabel("Use Dedicated Rx Buffer")
    canRXBuf.setDefaultValue(False)

    canRXBufElements = canComponent.createIntegerSymbol("RX_BUFFER_ELEMENTS", canRXBuf)
    canRXBufElements.setLabel("Number of Elements")
    canRXBufElements.setDefaultValue(1)
    canRXBufElements.setMin(1)
    canRXBufElements.setMax(64)
    canRXBufElements.setVisible(False)
    canRXBufElements.setDependencies(hideMenu, ["RXBUF_USE"])

    canRXBufelementSize = canComponent.createKeyValueSetSymbol("RX_BUFFER_BYTES_CFG", canRXBuf)
    canRXBufelementSize.setLabel("Element Size")
    canRXBufelementSize.setVisible(False)
    adornElementSize(canRXBufelementSize)
    canRXBufelementSize.setDependencies(RxBufferElementSize, ["CAN_OPMODE", "RXBUF_USE"])

    # ------  T X  --------------
    # ----- Tx FIFO -----
    canTX = canComponent.createBooleanSymbol("TX_USE", None)
    canTX.setLabel("Use TX FIFO")
    canTX.setDefaultValue(True)
    canTX.setReadOnly(True)

    # make a menu separate for TX so it can be turned off and on at one point
    canTXmenu = canComponent.createMenuSymbol("cantx", canTX)
    canTXmenu.setLabel("TX FIFO Settings")
    canTXmenu.setDependencies(hideMenu, ["TX_USE"])

    # number of TX FIFO elements
    canTXnumElements = canComponent.createIntegerSymbol("TX_FIFO_ELEMENTS", canTXmenu)
    canTXnumElements.setLabel("Number of Elements")
    canTXnumElements.setDefaultValue(1)
    canTXnumElements.setMin(1)
    canTXnumElements.setMax(32)

    canTXwatermarkP = canComponent.createIntegerSymbol("TX_FIFO_WP", canTXmenu)
    canTXwatermarkP.setLabel("Watermark %")
    canTXwatermarkP.setDefaultValue(0)
    canTXwatermarkP.setMin(0)
    canTXwatermarkP.setMax(99)

    #This is a computed value for watermark
    canTXwatermark = canComponent.createIntegerSymbol("TX_FIFO_WATERMARK", canTXmenu)
    canTXwatermark.setLabel("Watermark at element")
    canTXwatermark.setDescription("A value of 0 disables watermark")
    canTXwatermark.setDefaultValue(0)
    canTXwatermark.setReadOnly(True)
    canTXwatermark.setDependencies(TXWatermarkUpdate, ["TX_FIFO_ELEMENTS", "TX_FIFO_WP"])

    canTXElementCfg = canComponent.createKeyValueSetSymbol("TX_FIFO_BYTES_CFG", canTXmenu)
    canTXElementCfg.setLabel("Element Size")
    adornElementSize(canTXElementCfg)
    canTXElementCfg.setVisible(False)
    canTXElementCfg.setDependencies(updateElementSize, ["CAN_OPMODE"])

    canTXpause = canComponent.createBooleanSymbol("TX_PAUSE", None)
    canTXpause.setLabel("Enable TX Pause")
    canTXpause.setDescription("Pause 2 CAN bit times between transmissions")
    canTXpause.setDefaultValue(False)

    # ----- Tx Buffer -----
    canTXBuf = canComponent.createBooleanSymbol("TXBUF_USE", None)
    canTXBuf.setLabel("Use Dedicated Tx Buffer")
    canTXBuf.setDefaultValue(False)

    # number of TX buffer elements
    canTXBufElements = canComponent.createIntegerSymbol("TX_BUFFER_ELEMENTS", canTXBuf)
    canTXBufElements.setLabel("Number of TX Buffer Elements")
    canTXBufElements.setDefaultValue(1)
    canTXBufElements.setMin(1)
    canTXBufElements.setMax(32)
    canTXBufElements.setVisible(False)
    canTXBufElements.setDependencies(hideMenu, ["TXBUF_USE"])

    # up to 128 standard filters
    canStdFilterMenu = canComponent.createMenuSymbol("stdFilterMenu", None)
    canStdFilterMenu.setLabel("Standard Filters (up to 128)")
    canStdFilterMenu.setDependencies(adjustStdFilters, ["FILTERS_STD"])

    canStdFilterNumber = canComponent.createIntegerSymbol("FILTERS_STD", canStdFilterMenu)
    canStdFilterNumber.setLabel("Number of Standard Filters:")
    canStdFilterNumber.setDefaultValue(0)
    canStdFilterNumber.setMin(0)
    canStdFilterNumber.setMax(128)

    #Create all of the standard filters in a disabled state
    for filter in range (128):
        stdFilterList.append(canCreateStdFilter(canComponent, canStdFilterMenu, filter + 1))

    #What to do when a NO-MATCH is detected on a standard packet
    canNoMatchStandard = canComponent.createKeyValueSetSymbol("FILTERS_STD_NOMATCH", None)
    canNoMatchStandard.setLabel("Standard message No-Match disposition:")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_RXF0", "0", "Move to RX FIFO 0")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_RXF1", "1", "Move to RX FIFO 1")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_REJECT", "2", "Reject")
    canNoMatchStandard.setOutputMode("Key")
    canNoMatchStandard.setDisplayMode("Description")
    canNoMatchStandard.setDefaultValue(2)

    # Reject all standard IDs?
    canStdReject = canComponent.createBooleanSymbol("FILTERS_STD_REJECT", None)
    canStdReject.setLabel("Reject Standard Remote Frames")
    canStdReject.setDescription("Reject all remote frames with 11-bit standard IDs")
    canStdReject.setDefaultValue(False)

    # 64 extended filters
    canExtFilterMenu = canComponent.createMenuSymbol("extFilterMenu", None)
    canExtFilterMenu.setLabel("Extended Filters (up to 64)")
    canExtFilterMenu.setDependencies(adjustExtFilters, ["FILTERS_EXT"])

    #How many extended filters
    canExtFilterNumber = canComponent.createIntegerSymbol("FILTERS_EXT", canExtFilterMenu)
    canExtFilterNumber.setLabel("Number of Extended Filters:")
    canExtFilterNumber.setDefaultValue(0)
    canExtFilterNumber.setMin(0)
    canExtFilterNumber.setMax(64)

    #Create all of the 64 extended filters in a disabled state
    for filter in range (64):
        extFilterList.append(canCreateExtFilter(canComponent, canExtFilterMenu, filter + 1))

    #What to do when a NO-MATCH is detected on an extended message
    canNoMatchExtended = canComponent.createKeyValueSetSymbol("FILTERS_EXT_NOMATCH", None)
    canNoMatchExtended.setLabel("Extended message No-Match disposition:")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_RXF0", "0", "Move to RX FIFO 0")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_RXF1", "1", "Move to RX FIFO 1")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_REJECT", "2", "Reject")
    canNoMatchExtended.setOutputMode("Key")
    canNoMatchExtended.setDisplayMode("Description")
    canNoMatchExtended.setDefaultValue(2)

    # Reject all extended IDs?
    canExtReject = canComponent.createBooleanSymbol("FILTERS_EXT_REJECT", None)
    canExtReject.setLabel("Reject Extended Remote Frames")
    canExtReject.setDescription("Reject all remote frames with 29-bit extended IDs")
    canExtReject.setDefaultValue(False)

    #use timeout?
    canUseTimeout = canComponent.createBooleanSymbol("CAN_TIMEOUT", None)
    canUseTimeout.setLabel("Use Timeout Counter")
    canUseTimeout.setDescription("Enables Timeout Counter")
    canUseTimeout.setDefaultValue(False)

    #timout count
    canTimeoutCount = canComponent.createIntegerSymbol("TIMEOUT_COUNT", canUseTimeout)
    canTimeoutCount.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canTimeoutCount.setLabel("Timeout Countdown from: ")
    canTimeoutCount.setDefaultValue(40000)
    canTimeoutCount.setMin(10)
    canTimeoutCount.setMax(65535)
    canTimeoutCount.setVisible(False)
    canTimeoutCount.setDependencies(hideMenu, ["CAN_TIMEOUT"])

    #timeout mode
    canTimeoutMode = canComponent.createKeyValueSetSymbol("TIMEOUT_SELECT", canUseTimeout)
    canTimeoutMode.setLabel("Timeout mode:")
    canTimeoutMode.addKey("CAN_TOCC_TOS_CONT", "0", "CONTINUOUS")
    canTimeoutMode.addKey("CAN_TOCC_TOS_TXEF", "1", "TX EVENT")
    canTimeoutMode.addKey("CAN_TOCC_TOS_RXF0", "2", "RX0 EVENT")
    canTimeoutMode.addKey("CAN_TOCC_TOS_RXF1", "3", "RX1 EVENT")
    canTimeoutMode.setOutputMode("Key")
    canTimeoutMode.setDisplayMode("Description")
    canTimeoutMode.setVisible(False)
    canTimeoutMode.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canTimeoutMode.setDefaultValue(1)

    #timestamp Modes
    canTimestampMode = canComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", None)
    canTimestampMode.setLabel("Timestamp mode")
    canTimestampMode.setDescription("EXT TIMESTAMP: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    canTimestampMode.addKey("CAN_TSCC_TSS_ZERO", "0", "ZERO")
    canTimestampMode.addKey("CAN_TSCC_TSS_INC", "1", "TCP INC")
    canTimestampMode.addKey("CAN_TSCC_TSS_EXT", "2", "EXT TIMESTAMP")
    canTimestampMode.setOutputMode("Key")
    canTimestampMode.setDisplayMode("Description")
    canTimestampMode.setDefaultValue(1)

    #timestamp/timeout Counter Prescaler
    canTCP = canComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", None)
    canTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    canTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of CAN bit times.")
    canTCP.setDefaultValue(0)
    canTCP.setMin(0)
    canTCP.setMax(15)

    # Interrupt Dynamic settings
    caninterruptControl = canComponent.createBooleanSymbol("CAN_INTERRUPT_ENABLE", None)
    caninterruptControl.setVisible(False)
    caninterruptControl.setDependencies(interruptControl, ["INTERRUPT_MODE"])

    # Dependency Status for interrupt
    canIntEnComment = canComponent.createCommentSymbol("CAN_INTERRUPT_ENABLE_COMMENT", None)
    canIntEnComment.setVisible(False)
    canIntEnComment.setLabel("Warning!!! " + canInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    canIntEnComment.setDependencies(InterruptStatusWarning, ["core." + interruptVectorUpdate])

    REG_MODULE_CAN = Register.getRegisterModule("CAN")
    configName = Variables.get("__CONFIGURATION_NAME")

    #Master Header
    canMasterHeaderFile = canComponent.createFileSymbol("headerFile", None)
    canMasterHeaderFile.setSourcePath("../peripheral/can_u2003/templates/plib_can_common.h")
    canMasterHeaderFile.setOutputName("plib_can_common.h")
    canMasterHeaderFile.setDestPath("/peripheral/can/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = canComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/can_u2003/templates/plib_can.c.ftl")
    canMainSourceFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".c")
    canMainSourceFile.setDestPath("/peripheral/can/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)

    #Instance Header File
    canInstHeaderFile = canComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/can_u2003/templates/plib_can.h.ftl")
    canInstHeaderFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".h")
    canInstHeaderFile.setDestPath("/peripheral/can/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)

    #CAN Initialize
    canSystemInitFile = canComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    canSystemInitFile.setSourcePath("../peripheral/can_u2003/templates/system/initialization.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = canComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/can_u2003/templates/system/definitions.h.ftl")
    canSystemDefFile.setMarkup(True)
