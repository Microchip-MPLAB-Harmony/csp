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

mcanElementSizes = ["8 bytes", "12 bytes", "16 bytes", "20 bytes", "24 bytes", "32 bytes", "48 bytes", "64 bytes"]
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
    if ((event["id"] == 'MCAN_OPMODE' and event["value"] == 'CAN FD' and Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXBUF_USE") == True)
    or (event["id"] == 'RXBUF_USE' and event["value"] == True and Database.getSymbolValue(mcanInstanceName.getValue().lower(), "MCAN_OPMODE") == 'CAN FD')):
        element.setVisible(True)
    else:
        element.setVisible(False)

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
    if Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                               mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE") == 0:
        id1 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                   mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1")
        id2 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                      mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2")
        if id1 > id2:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def mcanCreateStdFilter(component, menu, filterNumber):
    stdFilter = component.createMenuSymbol(mcanInstanceName.getValue() + "_STD_FILTER"+ str(filterNumber), menu)
    stdFilter.setLabel("Standard Filter " + str(filterNumber))
    stdFilterType = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE", stdFilter)
    stdFilterType.setLabel("Type")
    adornFilterType(stdFilterType)
    sfid1 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setLabel("ID1")
    sfid1.setMin(0)
    sfid1.setMax(2047)
    sfid2 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setLabel("ID2")
    sfid2.setMin(0)
    sfid2.setMax(2047)

    stdFilterRangeInvalidSym = component.createCommentSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_COMMENT", stdFilter)
    stdFilterRangeInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Standard Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    stdFilterRangeInvalidSym.setVisible(False)
    stdFilterRangeInvalidSym.setDependencies(standardFilterRangeCheck, [mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE",
                                                                        mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1",
                                                                        mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2"])

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    config.setLabel("Element Configuration")
    adornFilterConfig(config)

    stdFilter.setVisible(False)
    stdFilter.setEnabled(False)
    return stdFilter

def extendedFilterRangeCheck(symbol, event):
    filterNumber = event["id"].split("_")[2].split("FILTER")[1]
    if Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                               mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE") == 0:
        id1 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                   mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1")
        id2 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                      mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2")
        if id1 > id2:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def mcanCreateExtFilter(component, menu, filterNumber):
    extFilter = component.createMenuSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber), menu)
    extFilter.setLabel("Extended Filter " + str(filterNumber))
    extFilterType = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE", extFilter)
    extFilterType.setLabel("Type")
    adornFilterType(extFilterType)
    efid1 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setLabel("ID1")
    efid1.setMin(0)
    efid1.setMax(536870911)
    efid2 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setLabel("ID2")
    efid2.setMin(0)
    efid2.setMax(536870911)

    extFilterRangeInvalidSym = component.createCommentSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_COMMENT", extFilter)
    extFilterRangeInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Extended Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    extFilterRangeInvalidSym.setVisible(False)
    extFilterRangeInvalidSym.setDependencies(extendedFilterRangeCheck, [mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE",
                                                                        mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1",
                                                                        mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2"])

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
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
        Database.setSymbolValue("core", interruptHandler, mcanInstanceName.getValue() + "_INT0_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, mcanInstanceName.getValue() + "_INT0_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):
    if (Database.getSymbolValue(mcanInstanceName.getValue().lower(), "INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

def mcanCoreClockFreq(symbol, event):
    symbol.setValue(int(Database.getSymbolValue("core", mcanInstanceName.getValue() + "_CLOCK_FREQUENCY")), 2)

def bitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", mcanInstanceName.getValue() + "_CLOCK_FREQUENCY")

    if (bitTiming == "Data"):
        prescaler = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DBRP")
        bitrate = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "DATA_BITRATE")
        samplePoint = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "DATA_SAMPLE_POINT")
    else:
        prescaler = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NBRP")
        bitrate = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "NOMINAL_BITRATE")
        samplePoint = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "NOMINAL_SAMPLE_POINT")

    numOfTimeQuanta = clk / ((bitrate * 1000) * (prescaler + 1))
    if (numOfTimeQuanta < lowTq):
        mcanTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too low for required " + bitTiming + " Bit Timing")
        mcanTimeQuantaInvalidSym.setVisible(True)
        mcanCoreClockInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Clock Frequency is too low for required " + bitTiming + " Bit Timing")
        mcanCoreClockInvalidSym.setVisible(True)
    elif (numOfTimeQuanta > highTq):
        mcanTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too high for required " + bitTiming + " Bit Timing")
        mcanTimeQuantaInvalidSym.setVisible(True)
        mcanCoreClockInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Clock Frequency is too high for required " + bitTiming + " Bit Timing")
        mcanCoreClockInvalidSym.setVisible(True)
    else:
        mcanTimeQuantaInvalidSym.setVisible(False)
        mcanCoreClockInvalidSym.setVisible(False)

    tseg1 = int((numOfTimeQuanta * samplePoint) / 100.0)
    tseg2 = numOfTimeQuanta - tseg1 - 1
    tseg1 -= 2

    return tseg1, tseg2

def dataBitTimingCalculation(symbol, event):
    if (Database.getSymbolValue(mcanInstanceName.getValue().lower(), "MCAN_OPMODE") == "CAN FD"):
        tseg1, tseg2 = bitTimingCalculation("Data", 4, 49)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DTSEG1", tseg1, 2)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DTSEG2", tseg2, 2)

def nominalBitTimingCalculation(symbol, event):
    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NTSEG1", tseg1, 2)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NTSEG2", tseg2, 2)

def instantiateComponent(mcanComponent):
    global mcanInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    global mcanCoreClockInvalidSym
    global mcanTimeQuantaInvalidSym

    mcanInstanceName = mcanComponent.createStringSymbol("MCAN_INSTANCE_NAME", None)
    mcanInstanceName.setVisible(False)
    mcanInstanceName.setDefaultValue(mcanComponent.getID().upper())
    print("Running " + mcanInstanceName.getValue())

    def hideMenu(menu, event):
        menu.setVisible(event["value"])

    #either the watermark % changed or the number of elements
    def RXF0WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXF0_WP")
        number_of_elements   = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXF0_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def RXF1WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXF1_WP")
        number_of_elements   = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXF1_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def TXWatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "TX_FIFO_WP")
        number_of_elements   = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "TX_FIFO_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    # Initialize peripheral clock
    Database.setSymbolValue("core", mcanInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)

    # MCAN operation mode - default to FD
    mcanOpMode = mcanComponent.createComboSymbol("MCAN_OPMODE", None, opModeValues)
    mcanOpMode.setLabel("MCAN Operation Mode")
    mcanOpMode.setDefaultValue("NORMAL")

    mcanInterruptMode = mcanComponent.createBooleanSymbol("INTERRUPT_MODE", None)
    mcanInterruptMode.setLabel("Interrupt Mode")
    mcanInterruptMode.setDefaultValue(False)

    interruptVector = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE"
    interruptHandler = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER"
    interruptHandlerLock = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE_UPDATE"

    mcanSFRRegSym = mcanComponent.createIntegerSymbol("MCAN_SFR_CAN_ENABLE_VALUE", None)
    mcanSFRRegSym.setDefaultValue(0)
    mcanSFRRegSym.setVisible(False)
    modules = ATDF.getNode('/avr-tools-device-file/modules')
    moduleList = modules.getChildren()
    for index in range(0, len(moduleList)):
        if (moduleList[index].getAttribute("name") == "SFR"):
            mcanSFRRegs = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SFR"]/register-group@[name="SFR"]')
            mcanSFRReg = mcanSFRRegs.getChildren()
            for index in range(0, len(mcanSFRReg)):
                if (mcanSFRReg[index].getAttribute("name") == "SFR_CAN"):
                    if (mcanSFRReg[index].getAttribute("count") > 1):
                        mcanSFRRegSym.setValue(2, 2)
                    else:
                        mcanSFRRegSym.setValue(1, 2)
                    break
            break

    mcanMATRIXRegSym = mcanComponent.createBooleanSymbol("MCAN_MATRIX_CAN_ENABLE", None)
    mcanMATRIXRegSym.setDefaultValue(False)
    mcanMATRIXRegSym.setVisible(False)
    for index in range(0, len(moduleList)):
        if (moduleList[index].getAttribute("name") == "MATRIX"):
            mcanMATRIXRegs = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MATRIX"]/register-group@[name="MATRIX"]')
            mcanMATRIXReg = mcanMATRIXRegs.getChildren()
            for index in range(0, len(mcanMATRIXReg)):
                if (mcanMATRIXReg[index].getAttribute("name") == "CCFG_CAN0"):
                    mcanMATRIXRegSym.setValue(True, 2)
                    break
            break

    mcanRevisionASym = mcanComponent.createBooleanSymbol("MCAN_REVISION_A_ENABLE", None)
    mcanRevisionASym.setDefaultValue(False)
    mcanRevisionASym.setVisible(False)
    mcanRegs = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCAN"]/register-group@[name="MCAN"]')
    mcanReg = mcanRegs.getChildren()
    for index in range(0, len(mcanReg)):
        if (mcanReg[index].getAttribute("name") == "MCAN_FBTP"):
            mcanRevisionASym.setValue(True, 2)
            break

    # MCAN Bit Timing Calculation
    mcanBitTimingCalculationMenu = mcanComponent.createMenuSymbol("BIT_TIMING_CALCULATION", None)
    mcanBitTimingCalculationMenu.setLabel("Bit Timing Calculation")
    mcanBitTimingCalculationMenu.setDescription("MCAN Bit Timing Calculation for Normal and CAN-FD Operation")

    mcanCoreClockValue = mcanComponent.createIntegerSymbol("MCAN_CORE_CLOCK_FREQ", mcanBitTimingCalculationMenu)
    mcanCoreClockValue.setLabel("Clock Frequency")
    mcanCoreClockValue.setReadOnly(True)
    mcanCoreClockValue.setDefaultValue(int(Database.getSymbolValue("core", mcanInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    mcanCoreClockValue.setVisible(True)
    mcanCoreClockValue.setDependencies(mcanCoreClockFreq, ["core." + mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    mcanCoreClockInvalidSym = mcanComponent.createCommentSymbol("MCAN_CORE_CLOCK_INVALID_COMMENT", None)
    mcanCoreClockInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Clock Frequency is too low for required Nominal Bit Timing")
    mcanCoreClockInvalidSym.setVisible((mcanCoreClockValue.getValue() == 0))

    mcanTimeQuantaInvalidSym = mcanComponent.createCommentSymbol("MCAN_TIME_QUANTA_INVALID_COMMENT", None)
    mcanTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too low for required Nominal Bit Timing")
    mcanTimeQuantaInvalidSym.setVisible(False)

    # MCAN Nominal Bit Timing Calculation
    mcanNominalBitTimingMenu = mcanComponent.createMenuSymbol("NOMINAL_BIT_TIMING_CALCULATION", mcanBitTimingCalculationMenu)
    mcanNominalBitTimingMenu.setLabel("Nominal Bit Timing")
    mcanNominalBitTimingMenu.setDescription("This timing must be less or equal to the CAN-FD Data Bit Timing if used")

    mcanNominalBitrate = mcanComponent.createIntegerSymbol("NOMINAL_BITRATE", mcanNominalBitTimingMenu)
    mcanNominalBitrate.setLabel("Bit Rate (Kbps)")
    mcanNominalBitrate.setMin(1)
    mcanNominalBitrate.setMax(1000)
    mcanNominalBitrate.setDefaultValue(500)
    mcanNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "core." + mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    mcanNominalSamplePoint = mcanComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", mcanNominalBitTimingMenu)
    mcanNominalSamplePoint.setLabel("Sample Point %")
    mcanNominalSamplePoint.setMin(50.0)
    mcanNominalSamplePoint.setMax(100.0)
    mcanNominalSamplePoint.setDefaultValue(75.0)
    mcanNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])

    NBTPsyncJump = mcanComponent.createIntegerSymbol("NBTP_NSJW", mcanNominalBitTimingMenu)
    NBTPsyncJump.setLabel("Synchronization Jump Width")
    NBTPsyncJump.setMin(0)
    NBTPsyncJump.setMax(127)
    NBTPsyncJump.setDefaultValue(3)

    NBTPprescale = mcanComponent.createIntegerSymbol("NBTP_NBRP", mcanNominalBitTimingMenu)
    NBTPprescale.setLabel("Bit Rate Prescaler")
    NBTPprescale.setMin(0)
    NBTPprescale.setMax(511)
    NBTPprescale.setDefaultValue(0)
    NBTPprescale.setDependencies(nominalBitTimingCalculation, ["NBTP_NBRP"])

    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)

    NBTPBeforeSP = mcanComponent.createIntegerSymbol("NBTP_NTSEG1", mcanNominalBitTimingMenu)
    NBTPBeforeSP.setLabel("Time Segment Before Sample Point")
    NBTPBeforeSP.setMin(1)
    NBTPBeforeSP.setMax(255)
    NBTPBeforeSP.setDefaultValue(tseg1)
    NBTPBeforeSP.setReadOnly(True)

    NBTPAfterSP = mcanComponent.createIntegerSymbol("NBTP_NTSEG2", mcanNominalBitTimingMenu)
    NBTPAfterSP.setLabel("Time Segment After Sample Point")
    NBTPAfterSP.setMin(0)
    NBTPAfterSP.setMax(127)
    NBTPAfterSP.setDefaultValue(tseg2)
    NBTPAfterSP.setReadOnly(True)

    # MCAN Data Bit Timing Calculation
    mcanDataBitTimingMenu = mcanComponent.createMenuSymbol("DATA_BIT_TIMING_CALCULATION", mcanBitTimingCalculationMenu)
    mcanDataBitTimingMenu.setLabel("Data Bit Timing")
    mcanDataBitTimingMenu.setDescription("This timing must be greater or equal to the Nominal Bit Timing")
    mcanDataBitTimingMenu.setVisible(False)
    mcanDataBitTimingMenu.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    mcanDataBitrate = mcanComponent.createIntegerSymbol("DATA_BITRATE", mcanDataBitTimingMenu)
    mcanDataBitrate.setLabel("Bit Rate (Kbps)")
    mcanDataBitrate.setMin(1)
    mcanDataBitrate.setDefaultValue(500)
    mcanDataBitrate.setDependencies(dataBitTimingCalculation, ["DATA_BITRATE", "MCAN_OPMODE", "core." + mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    mcanDataSamplePoint = mcanComponent.createFloatSymbol("DATA_SAMPLE_POINT", mcanDataBitTimingMenu)
    mcanDataSamplePoint.setLabel("Sample Point %")
    mcanDataSamplePoint.setMin(50.0)
    mcanDataSamplePoint.setMax(100.0)
    mcanDataSamplePoint.setDefaultValue(75.0)
    mcanDataSamplePoint.setDependencies(dataBitTimingCalculation, ["DATA_SAMPLE_POINT"])

    DBTPsyncJump = mcanComponent.createIntegerSymbol("DBTP_DSJW", mcanDataBitTimingMenu)
    DBTPsyncJump.setLabel("Synchronization Jump Width")
    DBTPsyncJump.setMin(0)
    DBTPsyncJump.setDefaultValue(3)
    DBTPsyncJump.setMax(7)

    DBTPprescale = mcanComponent.createIntegerSymbol("DBTP_DBRP", mcanDataBitTimingMenu)
    DBTPprescale.setLabel("Bit Rate Prescaler")
    DBTPprescale.setMin(0)
    DBTPprescale.setMax(31)
    DBTPprescale.setDefaultValue(0)
    DBTPprescale.setDependencies(dataBitTimingCalculation, ["DBTP_DBRP"])

    DBTPBeforeSP = mcanComponent.createIntegerSymbol("DBTP_DTSEG1", mcanDataBitTimingMenu)
    DBTPBeforeSP.setLabel("Time Segment Before Sample Point")
    DBTPBeforeSP.setMin(1)
    DBTPBeforeSP.setMax(31)
    DBTPBeforeSP.setDefaultValue(10)
    DBTPBeforeSP.setReadOnly(True)

    DBTPAfterSP = mcanComponent.createIntegerSymbol("DBTP_DTSEG2", mcanDataBitTimingMenu)
    DBTPAfterSP.setLabel("Time Segment After Sample Point")
    DBTPAfterSP.setMin(0)
    DBTPAfterSP.setDefaultValue(3)
    DBTPAfterSP.setMax(15)
    DBTPAfterSP.setReadOnly(True)

    # ----- Rx FIFO 0 -----
    mcanRXF0 = mcanComponent.createBooleanSymbol("RXF0_USE", None)
    mcanRXF0.setLabel("Use RX FIFO 0")
    mcanRXF0.setDefaultValue(True)
    mcanRXF0.setReadOnly(True)

    mcanRXF0Menu = mcanComponent.createMenuSymbol("rxf0Menu", mcanRXF0)
    mcanRXF0Menu.setLabel("RX FIFO 0 Settings")
    mcanRXF0Menu.setDependencies(hideMenu, ["RXF0_USE"])

    # number of RX FIFO 0 elements
    mcanRXF0Elements = mcanComponent.createIntegerSymbol("RXF0_ELEMENTS", mcanRXF0Menu)
    mcanRXF0Elements.setLabel("Number of Elements")
    mcanRXF0Elements.setDefaultValue(1)
    mcanRXF0Elements.setMin(0)
    mcanRXF0Elements.setMax(64)

    mcanRXF0watermarkP = mcanComponent.createIntegerSymbol("RXF0_WP", mcanRXF0Menu)
    mcanRXF0watermarkP.setLabel("Watermark %")
    mcanRXF0watermarkP.setDefaultValue(0)
    mcanRXF0watermarkP.setMin(0)
    mcanRXF0watermarkP.setMax(99)

    #This is a computed value
    mcanRXF0watermark = mcanComponent.createIntegerSymbol("RXF0_WATERMARK", mcanRXF0Menu)
    mcanRXF0watermark.setLabel("Watermark at element")
    mcanRXF0watermark.setDescription("A value of 0 disables watermark")
    mcanRXF0watermark.setDefaultValue(0)
    mcanRXF0watermark.setReadOnly(True)
    mcanRXF0watermark.setDependencies(RXF0WatermarkUpdate, ["RXF0_ELEMENTS", "RXF0_WP"])

    mcanRXF0elementSize = mcanComponent.createKeyValueSetSymbol("RXF0_BYTES_CFG", mcanRXF0Menu)
    mcanRXF0elementSize.setLabel("Element Size")
    mcanRXF0elementSize.setVisible(False)
    adornElementSize(mcanRXF0elementSize)
    mcanRXF0elementSize.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    mcanRx0overwrite = mcanComponent.createBooleanSymbol("RXF0_OVERWRITE", mcanRXF0Menu)
    mcanRx0overwrite.setLabel("Use Overwrite Mode")
    mcanRx0overwrite.setDescription("Overwrite RX FIFO 0 entries without blocking")
    mcanRx0overwrite.setDefaultValue(True)

    # ----- Rx FIFO 1 -----
    mcanRXF1 = mcanComponent.createBooleanSymbol("RXF1_USE", None)
    mcanRXF1.setLabel("Use RX FIFO 1")
    mcanRXF1.setDefaultValue(True)

    mcanRXF1Menu = mcanComponent.createMenuSymbol("rxf1menu", mcanRXF1)
    mcanRXF1Menu.setLabel("RX FIFO 1 Settings")
    mcanRXF1Menu.setDependencies(hideMenu, ["RXF1_USE"])

    mcanRXF1Elements = mcanComponent.createIntegerSymbol("RXF1_ELEMENTS", mcanRXF1Menu)
    mcanRXF1Elements.setLabel("Number of Elements")
    mcanRXF1Elements.setDefaultValue(1)
    mcanRXF1Elements.setMin(1)
    mcanRXF1Elements.setMax(64)

    mcanRXF1watermarkP = mcanComponent.createIntegerSymbol("RXF1_WP", mcanRXF1Menu)
    mcanRXF1watermarkP.setLabel("Watermark %")
    mcanRXF1watermarkP.setDefaultValue(0)
    mcanRXF1watermarkP.setMin(0)
    mcanRXF1watermarkP.setMax(99)

    #This is a computed value for watermark
    mcanRX1watermark = mcanComponent.createIntegerSymbol("RXF1_WATERMARK", mcanRXF1Menu)
    mcanRX1watermark.setLabel("Watermark at element")
    mcanRX1watermark.setDescription("A value of 0 disables watermark")
    mcanRX1watermark.setDefaultValue(0)
    mcanRX1watermark.setReadOnly(True)
    mcanRX1watermark.setDependencies(RXF1WatermarkUpdate, ["RXF1_ELEMENTS", "RXF1_WP"])

    mcanRXF1elementSize = mcanComponent.createKeyValueSetSymbol("RXF1_BYTES_CFG", mcanRXF1Menu)
    mcanRXF1elementSize.setLabel("Element Size")
    mcanRXF1elementSize.setVisible(False)
    adornElementSize(mcanRXF1elementSize)
    mcanRXF1elementSize.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    mcanRXF1overwrite = mcanComponent.createBooleanSymbol("RXF1_OVERWRITE", mcanRXF1Menu)
    mcanRXF1overwrite.setLabel("Use Overwrite Mode")
    mcanRXF1overwrite.setDescription("Overwrite RX FIFO 1 entries without blocking")
    mcanRXF1overwrite.setDefaultValue(True)

    # ----- Rx Buffer -----
    mcanRXBuf = mcanComponent.createBooleanSymbol("RXBUF_USE", None)
    mcanRXBuf.setLabel("Use Dedicated Rx Buffer")
    mcanRXBuf.setDefaultValue(False)

    mcanRXBufElements = mcanComponent.createIntegerSymbol("RX_BUFFER_ELEMENTS", mcanRXBuf)
    mcanRXBufElements.setLabel("Number of Elements")
    mcanRXBufElements.setDefaultValue(1)
    mcanRXBufElements.setMin(1)
    mcanRXBufElements.setMax(64)
    mcanRXBufElements.setVisible(False)
    mcanRXBufElements.setDependencies(hideMenu, ["RXBUF_USE"])

    mcanRXBufelementSize = mcanComponent.createKeyValueSetSymbol("RX_BUFFER_BYTES_CFG", mcanRXBuf)
    mcanRXBufelementSize.setLabel("Element Size")
    mcanRXBufelementSize.setVisible(False)
    adornElementSize(mcanRXBufelementSize)
    mcanRXBufelementSize.setDependencies(RxBufferElementSize, ["MCAN_OPMODE", "RXBUF_USE"])

    # ------  T X  --------------
    # ----- Tx FIFO -----
    mcanTX = mcanComponent.createBooleanSymbol("TX_USE", None)
    mcanTX.setLabel("Use TX FIFO")
    mcanTX.setDefaultValue(True)
    mcanTX.setReadOnly(True)

    # make a menu separate for TX so it can be turned off and on at one point
    mcanTXmenu = mcanComponent.createMenuSymbol("mcantx", mcanTX)
    mcanTXmenu.setLabel("TX FIFO Settings")
    mcanTXmenu.setDependencies(hideMenu, ["TX_USE"])

    # number of TX FIFO elements
    mcanTXnumElements = mcanComponent.createIntegerSymbol("TX_FIFO_ELEMENTS", mcanTXmenu)
    mcanTXnumElements.setLabel("Number of Elements")
    mcanTXnumElements.setDefaultValue(1)
    mcanTXnumElements.setMin(1)
    mcanTXnumElements.setMax(32)

    mcanTXwatermarkP = mcanComponent.createIntegerSymbol("TX_FIFO_WP", mcanTXmenu)
    mcanTXwatermarkP.setLabel("Watermark %")
    mcanTXwatermarkP.setDefaultValue(0)
    mcanTXwatermarkP.setMin(0)
    mcanTXwatermarkP.setMax(99)

    #This is a computed value for watermark
    mcanTXwatermark = mcanComponent.createIntegerSymbol("TX_FIFO_WATERMARK", mcanTXmenu)
    mcanTXwatermark.setLabel("Watermark at element")
    mcanTXwatermark.setDescription("A value of 0 disables watermark")
    mcanTXwatermark.setDefaultValue(0)
    mcanTXwatermark.setReadOnly(True)
    mcanTXwatermark.setDependencies(TXWatermarkUpdate, ["TX_FIFO_ELEMENTS", "TX_FIFO_WP"])

    mcanTXElementCfg = mcanComponent.createKeyValueSetSymbol("TX_FIFO_BYTES_CFG", mcanTXmenu)
    mcanTXElementCfg.setLabel("Element Size")
    adornElementSize(mcanTXElementCfg)
    mcanTXElementCfg.setVisible(False)
    mcanTXElementCfg.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    mcanTXpause = mcanComponent.createBooleanSymbol("TX_PAUSE", None)
    mcanTXpause.setLabel("Enable TX Pause")
    mcanTXpause.setDescription("Pause 2 MCAN bit times between transmissions")
    mcanTXpause.setDefaultValue(False)

    # ----- Tx Buffer -----
    mcanTXBuf = mcanComponent.createBooleanSymbol("TXBUF_USE", None)
    mcanTXBuf.setLabel("Use Dedicated Tx Buffer")
    mcanTXBuf.setDefaultValue(False)

    # number of TX buffer elements
    mcanTXBufElements = mcanComponent.createIntegerSymbol("TX_BUFFER_ELEMENTS", mcanTXBuf)
    mcanTXBufElements.setLabel("Number of TX Buffer Elements")
    mcanTXBufElements.setDefaultValue(1)
    mcanTXBufElements.setMin(1)
    mcanTXBufElements.setMax(32)
    mcanTXBufElements.setVisible(False)
    mcanTXBufElements.setDependencies(hideMenu, ["TXBUF_USE"])

    # up to 128 standard filters
    mcanStdFilterMenu = mcanComponent.createMenuSymbol("stdFilterMenu", None)
    mcanStdFilterMenu.setLabel("Standard Filters (up to 128)")
    mcanStdFilterMenu.setDependencies(adjustStdFilters, ["FILTERS_STD"])

    mcanStdFilterNumber = mcanComponent.createIntegerSymbol("FILTERS_STD", mcanStdFilterMenu)
    mcanStdFilterNumber.setLabel("Number of Standard Filters:")
    mcanStdFilterNumber.setDefaultValue(0)
    mcanStdFilterNumber.setMin(0)
    mcanStdFilterNumber.setMax(128)

    #Create all of the standard filters in a disabled state
    for filter in range (128):
        stdFilterList.append(mcanCreateStdFilter(mcanComponent, mcanStdFilterMenu, filter + 1))

    #What to do when a NO-MATCH is detected on a standard packet
    mcanNoMatchStandard = mcanComponent.createKeyValueSetSymbol("FILTERS_STD_NOMATCH", None)
    mcanNoMatchStandard.setLabel("Standard message No-Match disposition:")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_0", "0", "Move to RX FIFO 0")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_1", "1", "Move to RX FIFO 1")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS(2)",        "2", "Reject")
    mcanNoMatchStandard.setOutputMode("Key")
    mcanNoMatchStandard.setDisplayMode("Description")
    mcanNoMatchStandard.setDefaultValue(2)

    # Reject all standard IDs?
    mcanStdReject = mcanComponent.createBooleanSymbol("FILTERS_STD_REJECT", None)
    mcanStdReject.setLabel("Reject Standard Remote Frames")
    mcanStdReject.setDescription("Reject all remote frames with 11-bit standard IDs")
    mcanStdReject.setDefaultValue(False)

    # 64 extended filters
    mcanExtFilterMenu = mcanComponent.createMenuSymbol("extFilterMenu", None)
    mcanExtFilterMenu.setLabel("Extended Filters (up to 64)")
    mcanExtFilterMenu.setDependencies(adjustExtFilters, ["FILTERS_EXT"])

    #How many extended filters
    mcanExtFilterNumber = mcanComponent.createIntegerSymbol("FILTERS_EXT", mcanExtFilterMenu)
    mcanExtFilterNumber.setLabel("Number of Extended Filters:")
    mcanExtFilterNumber.setDefaultValue(0)
    mcanExtFilterNumber.setMin(0)
    mcanExtFilterNumber.setMax(64)

    #Create all of the 64 extended filters in a disabled state
    for filter in range (64):
        extFilterList.append(mcanCreateExtFilter(mcanComponent, mcanExtFilterMenu, filter + 1))

    #What to do when a NO-MATCH is detected on an extended message
    mcanNoMatchExtended = mcanComponent.createKeyValueSetSymbol("FILTERS_EXT_NOMATCH", None)
    mcanNoMatchExtended.setLabel("Extended message No-Match disposition:")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_0", "0", "Move to RX FIFO 0")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_1", "1", "Move to RX FIFO 1")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE(2)",        "2", "Reject")
    mcanNoMatchExtended.setOutputMode("Key")
    mcanNoMatchExtended.setDisplayMode("Description")
    mcanNoMatchExtended.setDefaultValue(2)

    # Reject all extended IDs?
    mcanExtReject = mcanComponent.createBooleanSymbol("FILTERS_EXT_REJECT", None)
    mcanExtReject.setLabel("Reject Extended Remote Frames")
    mcanExtReject.setDescription("Reject all remote frames with 29-bit extended IDs")
    mcanExtReject.setDefaultValue(False)

    #use timeout?
    mcanUseTimeout = mcanComponent.createBooleanSymbol("MCAN_TIMEOUT", None)
    mcanUseTimeout.setLabel("Use Timeout Counter")
    mcanUseTimeout.setDescription("Enables Timeout Counter")
    mcanUseTimeout.setDefaultValue(False)

    #timout count
    mcanTimeoutCount = mcanComponent.createIntegerSymbol("TIMEOUT_COUNT", mcanUseTimeout)
    mcanTimeoutCount.setDependencies(hideMenu, ["MCAN_TIMEOUT"])
    mcanTimeoutCount.setLabel("Timeout Countdown from: ")
    mcanTimeoutCount.setDefaultValue(40000)
    mcanTimeoutCount.setMin(10)
    mcanTimeoutCount.setMax(65535)
    mcanTimeoutCount.setVisible(False)
    mcanTimeoutCount.setDependencies(hideMenu, ["MCAN_TIMEOUT"])

    #timeout mode
    mcanTimeoutMode = mcanComponent.createKeyValueSetSymbol("TIMEOUT_SELECT", mcanUseTimeout)
    mcanTimeoutMode.setLabel("Timeout mode:")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_CONTINUOUS", "0", "CONTINUOUS")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_TX_EV_TIMEOUT", "1", "TX EVENT")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_RX0_EV_TIMEOUT", "2", "RX0 EVENT")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_RX1_EV_TIMEOUT", "3", "RX1 EVENT")
    mcanTimeoutMode.setOutputMode("Key")
    mcanTimeoutMode.setDisplayMode("Description")
    mcanTimeoutMode.setVisible(False)
    mcanTimeoutMode.setDependencies(hideMenu, ["MCAN_TIMEOUT"])
    mcanTimeoutMode.setDefaultValue(1)

    #timestamp Modes
    mcanTimestampMode = mcanComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", None)
    mcanTimestampMode.setLabel("Timestamp mode")
    mcanTimestampMode.setDescription("EXT TIMESTAMP: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_ALWAYS_0", "0", "ZERO")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_TCP_INC", "1", "TCP INC")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_EXT_TIMESTAMP", "2", "EXT TIMESTAMP")
    mcanTimestampMode.setOutputMode("Key")
    mcanTimestampMode.setDisplayMode("Description")
    mcanTimestampMode.setDefaultValue(1)

    #timestamp/timeout Counter Prescaler
    mcanTCP = mcanComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", None)
    mcanTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    mcanTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of MCAN bit times.")
    mcanTCP.setDefaultValue(0)
    mcanTCP.setMin(0)
    mcanTCP.setMax(15)

    # Interrupt Dynamic settings
    mcaninterruptControl = mcanComponent.createBooleanSymbol("MCAN_INTERRUPT_ENABLE", None)
    mcaninterruptControl.setVisible(False)
    mcaninterruptControl.setDependencies(interruptControl, ["INTERRUPT_MODE"])

    # Dependency Status for interrupt
    mcanIntEnComment = mcanComponent.createCommentSymbol("MCAN_INTERRUPT_ENABLE_COMMENT", None)
    mcanIntEnComment.setVisible(False)
    mcanIntEnComment.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    mcanIntEnComment.setDependencies(InterruptStatusWarning, ["core." + interruptVectorUpdate])

    REG_MODULE_MCAN = Register.getRegisterModule("MCAN")
    configName = Variables.get("__CONFIGURATION_NAME")

    #Master Header
    mcanMasterHeaderFile = mcanComponent.createFileSymbol("headerFile", None)
    mcanMasterHeaderFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/plib_mcan_common.h")
    mcanMasterHeaderFile.setOutputName("plib_mcan_common.h")
    mcanMasterHeaderFile.setDestPath("/peripheral/mcan/")
    mcanMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    mcanMasterHeaderFile.setType("HEADER")

    #Instance Source File
    mcanMainSourceFile = mcanComponent.createFileSymbol("sourceFile", None)
    mcanMainSourceFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/plib_mcan.c.ftl")
    mcanMainSourceFile.setOutputName("plib_"+mcanInstanceName.getValue().lower()+".c")
    mcanMainSourceFile.setDestPath("/peripheral/mcan/")
    mcanMainSourceFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    mcanMainSourceFile.setType("SOURCE")
    mcanMainSourceFile.setMarkup(True)

    #Instance Header File
    mcanInstHeaderFile = mcanComponent.createFileSymbol("instHeaderFile", None)
    mcanInstHeaderFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/plib_mcan.h.ftl")
    mcanInstHeaderFile.setOutputName("plib_"+mcanInstanceName.getValue().lower()+".h")
    mcanInstHeaderFile.setDestPath("/peripheral/mcan/")
    mcanInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    mcanInstHeaderFile.setType("HEADER")
    mcanInstHeaderFile.setMarkup(True)

    #MCAN Initialize
    mcanSystemInitFile = mcanComponent.createFileSymbol("initFile", None)
    mcanSystemInitFile.setType("STRING")
    mcanSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    mcanSystemInitFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/initialization.c.ftl")
    mcanSystemInitFile.setMarkup(True)

    #MCAN definitions header
    mcanSystemDefFile = mcanComponent.createFileSymbol("defFile", None)
    mcanSystemDefFile.setType("STRING")
    mcanSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mcanSystemDefFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/definitions.h.ftl")
    mcanSystemDefFile.setMarkup(True)

'''********************************End of the file*************************'''
