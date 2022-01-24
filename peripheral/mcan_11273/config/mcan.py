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
opModeValues = ["NORMAL", "CAN FD", "Restricted Operation Mode", "Bus Monitoring Mode", "External Loop Back Mode", "Internal Loop Back Mode"]

stdFilterList = []
extFilterList = []

# if the mode is changed to FD, then show options for more bytes
def showWhenFD(element, event):
    if event["value"] != 'NORMAL':
        element.setVisible(True)
    else:
        element.setVisible(False)

# Rx Buffer Element size
def RxBufferElementSize(element, event):
    if ((event["id"] == 'MCAN_OPMODE' and event["value"] != 'NORMAL' and Database.getSymbolValue(mcanInstanceName.getValue().lower(), "RXBUF_USE") == True)
    or (event["id"] == 'RXBUF_USE' and event["value"] == True and Database.getSymbolValue(mcanInstanceName.getValue().lower(), "MCAN_OPMODE") != 'NORMAL')):
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
    if event["value"] != 'NORMAL':
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
    if Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                               mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE") == 0:
        id1 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                   mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1")
        id2 = Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                                      mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2")
        if ((id1 > id2) and (Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                             mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG") != 7)):
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
    sfid1 = component.createHexSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setLabel("ID1")
    sfid1.setMin(0)
    sfid1.setMax(0x7FF)
    sfid2 = component.createHexSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setLabel("ID2")
    sfid2.setMin(0)
    sfid2.setMax(0x7FF)

    stdFilterRangeInvalidSym = component.createCommentSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_COMMENT", stdFilter)
    stdFilterRangeInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Standard Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    stdFilterRangeInvalidSym.setVisible(False)

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    config.setLabel("Element Configuration")
    adornFilterConfig(config)

    stdFilterRangeInvalidSym.setDependencies(standardFilterRangeCheck, [mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE",
                                                                        mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1",
                                                                        mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2",
                                                                        mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG"])
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
        if ((id1 > id2) and (Database.getSymbolValue(mcanInstanceName.getValue().lower(),
                             mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG") != 7)):
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
    efid1 = component.createHexSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setLabel("ID1")
    efid1.setMin(0)
    efid1.setMax(0x1FFFFFFF)
    efid2 = component.createHexSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setLabel("ID2")
    efid2.setMin(0)
    efid2.setMax(0x1FFFFFFF)

    extFilterRangeInvalidSym = component.createCommentSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_COMMENT", extFilter)
    extFilterRangeInvalidSym.setLabel("Warning!!! " + mcanInstanceName.getValue() + " Extended Filter " + str(filterNumber) + " ID2 must be greater or equal to ID1")
    extFilterRangeInvalidSym.setVisible(False)

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
    config.setLabel("Element Configuration")
    adornFilterConfig(config)

    extFilterRangeInvalidSym.setDependencies(extendedFilterRangeCheck, [mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE",
                                                                        mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1",
                                                                        mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2",
                                                                        mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG"])
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

def autoBitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", mcanInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if (bitTiming == "Data"):
        bitrate = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "DATA_BITRATE")
        brpPrescaler = DBTPprescale
        mcanTseg1 = DBTPBeforeSP
        mcanTseg2 = DBTPAfterSP
        mcanSamplePoint = mcanDataSamplePoint
    else:
        bitrate = Database.getSymbolValue(mcanInstanceName.getValue().lower(), "NOMINAL_BITRATE")
        brpPrescaler = NBTPprescale
        mcanTseg1 = NBTPBeforeSP
        mcanTseg2 = NBTPAfterSP
        mcanSamplePoint = mcanNominalSamplePoint

    minErrTseg1 = mcanTseg1.getMax()
    minErrTseg2 = mcanTseg2.getMax()
    minErrCalculatedBitrate = 0.0
    minErrCalculatedTimeQuanta = lowTq
    minErrTqPeriod = 0.0
    minErrorRate = 100.0
    errorRate = 100.0
    minErrPrescaler = 0
    for tseg1 in range(mcanTseg1.getMax(), mcanTseg1.getMin() - 1, -1):
        for tseg2 in range(mcanTseg2.getMax(), mcanTseg2.getMin() - 1, -1):
            calculatedTimeQuanta = 1 + tseg1 + tseg2
            if (tseg1 >= tseg2):
                if ((lowTq <= calculatedTimeQuanta) and (calculatedTimeQuanta <= highTq)):
                    prescaler = int(clk /((bitrate * 1000) * calculatedTimeQuanta)) - 1
                    if prescaler >= brpPrescaler.getMin():
                        if (prescaler > brpPrescaler.getMax()):
                            prescaler = brpPrescaler.getMax()

                        tqPeriod = float(prescaler + 1) / clk
                        calculatedBitrate = 1.0 / (float(tqPeriod) * calculatedTimeQuanta)
                        errorRate = ((float(calculatedBitrate) - (bitrate * 1000)) / (bitrate * 1000)) * 100.0
                        if (abs(errorRate) < abs(minErrorRate)):
                            minErrorRate = errorRate
                            minErrPrescaler = prescaler
                            minErrTseg1 = tseg1
                            minErrTseg2 = tseg2
                            minErrCalculatedBitrate = calculatedBitrate
                            minErrCalculatedTimeQuanta = calculatedTimeQuanta
                            minErrTqPeriod = tqPeriod
                        if errorRate == 0:
                            break
        if errorRate == 0:
            break

    sjw = minErrTseg2
    if (bitTiming == "Data") and (sjw > 8):
        sjw = 8
    mcanSamplePoint.setReadOnly(True)
    mcanSamplePoint.setValue((float(1 + minErrTseg1)/minErrCalculatedTimeQuanta) * 100.0)
    brpPrescaler.setReadOnly(True)
    brpPrescaler.setValue(minErrPrescaler)
    return "{:.3f}".format(minErrorRate), (int(minErrCalculatedBitrate) / 1000), "{:.3f}".format(minErrTqPeriod * 1000000000.0), minErrCalculatedTimeQuanta, minErrTseg1, minErrTseg2, sjw

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
    sjw = tseg2

    if (bitTiming == "Data"):
        mcanTseg1 = DBTPBeforeSP
        mcanTseg2 = DBTPAfterSP
        if (sjw + 1) > 8:
            sjw = 7
    else:
        mcanTseg1 = NBTPBeforeSP
        mcanTseg2 = NBTPAfterSP

    if (tseg1 + 1) < mcanTseg1.getMin():
        calculatedTseg1 = mcanTseg1.getMin()
    elif (tseg1 + 1) > mcanTseg1.getMax():
        calculatedTseg1 = mcanTseg1.getMax()
    else:
        calculatedTseg1 = tseg1 + 1

    if (tseg2 + 1) < mcanTseg2.getMin():
        calculatedTseg2 = mcanTseg2.getMin()
    elif (tseg2 + 1) > mcanTseg2.getMax():
        calculatedTseg2 = mcanTseg2.getMax()
    else:
        calculatedTseg2 = tseg2 + 1

    calculatedTimeQuanta = 1 + calculatedTseg1 + calculatedTseg2
    calculatedBitrate = clk / (calculatedTimeQuanta * (prescaler + 1))

    tqPeriod = 0.0
    if calculatedBitrate != 0:
        # Calculated Time Quanta (TQ) Period in sec
        tqPeriod = 1.0 / (calculatedBitrate * calculatedTimeQuanta)

    # Calculated Error %
    errorRate = ((float(calculatedBitrate) - (bitrate * 1000)) / (bitrate * 1000)) * 100.0

    return "{:.3f}".format(errorRate), (int(calculatedBitrate) / 1000), "{:.3f}".format(tqPeriod * 1000000000.0), calculatedTimeQuanta, (tseg1 + 1), (tseg2 + 1), (sjw + 1)

def dataBitTimingCalculation(symbol, event):
    if (Database.getSymbolValue(mcanInstanceName.getValue().lower(), "MCAN_OPMODE") != "NORMAL"):
        if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_DATA_BIT_TIMING_CALCULATION") == True:
            if event["id"] == "DBTP_DBRP" or event["id"] == "DATA_SAMPLE_POINT":
                return
            else:
                errorRate, calculatedDataBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = autoBitTimingCalculation("Data", 4, 49)
        else:
            errorRate, calculatedDataBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = bitTimingCalculation("Data", 4, 49)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_TOTAL_TIME_QUANTA", timeQuanta)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DTSEG1", tseg1)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DTSEG2", tseg2)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "DBTP_DSJW", sjw)
        Database.setSymbolValue(mcanInstanceName.getValue().lower(), "CALCULATED_DATA_BITRATE", calculatedDataBitrate)
        symbol.getComponent().getSymbolByID("DATA_TIME_QUANTA_PERIOD").setValue(str(tqPeriod))
        symbol.getComponent().getSymbolByID("CALCULATED_DATA_ERRORRATE").setValue(str(errorRate))
        if abs(float(errorRate)) > 1:
            mcanDataErrorRateCommentSym.setLabel("Warning!!! Error " + str(errorRate) + "%")
            mcanDataErrorRateCommentSym.setVisible(True)
        else:
            mcanDataErrorRateCommentSym.setVisible(False)

def nominalBitTimingCalculation(symbol, event):
    if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True:
        if event["id"] == "NBTP_NBRP" or event["id"] == "NOMINAL_SAMPLE_POINT":
            return
        else:
            errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = autoBitTimingCalculation("Nominal", 4, 385)
    else:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = bitTimingCalculation("Nominal", 4, 385)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_TOTAL_TIME_QUANTA", timeQuanta)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NTSEG1", tseg1)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NTSEG2", tseg2)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "NBTP_NSJW", sjw)
    Database.setSymbolValue(mcanInstanceName.getValue().lower(), "CALCULATED_NOMINAL_BITRATE", calculatedNominalBitrate)
    symbol.getComponent().getSymbolByID("NOMINAL_TIME_QUANTA_PERIOD").setValue(str(tqPeriod))
    symbol.getComponent().getSymbolByID("CALCULATED_NOMINAL_ERRORRATE").setValue(str(errorRate))
    if abs(float(errorRate)) > 1:
        mcanNominalErrorRateCommentSym.setLabel("Warning!!! Error " + str(errorRate) + "%")
        mcanNominalErrorRateCommentSym.setVisible(True)
    else:
        mcanNominalErrorRateCommentSym.setVisible(False)

def updateNominalBitTimingSymbols(symbol, event):
    if (event["value"]):
        symbol.getComponent().getSymbolByID("NBTP_NBRP").setReadOnly(True)
        symbol.getComponent().getSymbolByID("NOMINAL_SAMPLE_POINT").setReadOnly(True)
        mcanTimeQuantaInvalidSym.setVisible(False)
        mcanCoreClockInvalidSym.setVisible(False)
    else:
        symbol.getComponent().getSymbolByID("NBTP_NBRP").setReadOnly(False)
        symbol.getComponent().getSymbolByID("NOMINAL_SAMPLE_POINT").setReadOnly(False)

def updateDataBitTimingSymbols(symbol, event):
    if (event["value"]):
        symbol.getComponent().getSymbolByID("DBTP_DBRP").setReadOnly(True)
        symbol.getComponent().getSymbolByID("DATA_SAMPLE_POINT").setReadOnly(True)
        mcanTimeQuantaInvalidSym.setVisible(False)
        mcanCoreClockInvalidSym.setVisible(False)
    else:
        symbol.getComponent().getSymbolByID("DBTP_DBRP").setReadOnly(False)
        symbol.getComponent().getSymbolByID("DATA_SAMPLE_POINT").setReadOnly(False)

def updateSourceFileName(symbol, event):
    id = symbol.getID()

    if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "MCAN_GENERATE_LEGACY_APIS") == True:
        if id == "sourceFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan_legacy.c.ftl")
        elif id == "instHeaderFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan_legacy.h.ftl")
        elif id == "headerFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan_common_legacy.h")
    else:
        mcanInt = ""
        if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "INTERRUPT_MODE") == True:
            mcanInt = "_interrupt"

        if id == "sourceFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan" + mcanInt + ".c.ftl")
        elif id == "instHeaderFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan" + mcanInt + ".h.ftl")
        elif id == "headerFile":
            symbol.setSourcePath("../peripheral/mcan_11273/templates/plib_mcan_common.h")

def instantiateComponent(mcanComponent):
    global mcanInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    global mcanCoreClockInvalidSym
    global mcanTimeQuantaInvalidSym
    global NBTPprescale
    global mcanNominalSamplePoint
    global mcanNominalErrorRateCommentSym
    global NBTPBeforeSP
    global NBTPAfterSP
    global mcanDataSamplePoint
    global DBTPprescale
    global mcanDataErrorRateCommentSym
    global DBTPBeforeSP
    global DBTPAfterSP

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
                    mcanSFRRegSym.setValue(1)
                    break
                elif (mcanSFRReg[index].getAttribute("name") == "SFR_" + mcanInstanceName.getValue()[1:]):
                    mcanSFRRegSym.setValue(3)
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

    mcanAutomaticNominalBitTimingCalculation = mcanComponent.createBooleanSymbol("AUTO_NOMINAL_BIT_TIMING_CALCULATION", mcanNominalBitTimingMenu)
    mcanAutomaticNominalBitTimingCalculation.setLabel("Automatic Nominal Bit Timing Calculation")
    mcanAutomaticNominalBitTimingCalculation.setDefaultValue(False)
    mcanAutomaticNominalBitTimingCalculation.setDependencies(updateNominalBitTimingSymbols, ["AUTO_NOMINAL_BIT_TIMING_CALCULATION"])

    mcanNominalBitrate = mcanComponent.createIntegerSymbol("NOMINAL_BITRATE", mcanNominalBitTimingMenu)
    mcanNominalBitrate.setLabel("Bit Rate (Kbps)")
    mcanNominalBitrate.setMin(1)
    mcanNominalBitrate.setMax(1000)
    mcanNominalBitrate.setDefaultValue(500)
    mcanNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "AUTO_NOMINAL_BIT_TIMING_CALCULATION", "core." + mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    mcanNominalSamplePoint = mcanComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", mcanNominalBitTimingMenu)
    mcanNominalSamplePoint.setLabel("Sample Point %")
    mcanNominalSamplePoint.setMin(50.0)
    mcanNominalSamplePoint.setMax(100.0)
    mcanNominalSamplePoint.setDefaultValue(75.0)
    mcanNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])
    mcanNominalSamplePoint.setReadOnly(Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    NBTPprescale = mcanComponent.createIntegerSymbol("NBTP_NBRP", mcanNominalBitTimingMenu)
    NBTPprescale.setLabel("Bit Rate Prescaler")
    NBTPprescale.setMin(0)
    NBTPprescale.setMax(511)
    NBTPprescale.setDefaultValue(0)
    NBTPprescale.setDependencies(nominalBitTimingCalculation, ["NBTP_NBRP"])
    NBTPprescale.setReadOnly(Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    mcanNominalTotalTimeQuanta = mcanComponent.createIntegerSymbol("NBTP_TOTAL_TIME_QUANTA", mcanNominalBitTimingMenu)
    mcanNominalTotalTimeQuanta.setLabel("Total Time Quanta (TQ)")
    mcanNominalTotalTimeQuanta.setReadOnly(True)

    mcanNominalSyncSegment = mcanComponent.createIntegerSymbol("NBTP_SYNC", mcanNominalTotalTimeQuanta)
    mcanNominalSyncSegment.setLabel("Sync Segment (TQ)")
    mcanNominalSyncSegment.setDefaultValue(1)
    mcanNominalSyncSegment.setReadOnly(True)

    NBTPBeforeSP = mcanComponent.createIntegerSymbol("NBTP_NTSEG1", mcanNominalTotalTimeQuanta)
    NBTPBeforeSP.setLabel("Time Segment Before Sample Point (TQ)")
    NBTPBeforeSP.setMin(2)
    NBTPBeforeSP.setMax(256)
    NBTPBeforeSP.setReadOnly(True)

    NBTPAfterSP = mcanComponent.createIntegerSymbol("NBTP_NTSEG2", mcanNominalTotalTimeQuanta)
    NBTPAfterSP.setLabel("Time Segment After Sample Point (TQ)")
    NBTPAfterSP.setMin(1)
    NBTPAfterSP.setMax(128)
    NBTPAfterSP.setReadOnly(True)

    if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = autoBitTimingCalculation("Nominal", 4, 385)
    else:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = bitTimingCalculation("Nominal", 4, 385)

    mcanNominalTotalTimeQuanta.setDefaultValue(timeQuanta)
    NBTPBeforeSP.setDefaultValue(tseg1)
    NBTPAfterSP.setDefaultValue(tseg2)

    NBTPsyncJump = mcanComponent.createIntegerSymbol("NBTP_NSJW", mcanNominalBitTimingMenu)
    NBTPsyncJump.setLabel("Synchronization Jump Width (TQ)")
    NBTPsyncJump.setMin(1)
    NBTPsyncJump.setMax(128)
    NBTPsyncJump.setDefaultValue(sjw)

    mcanNominalTimeQuantaPeriod = mcanComponent.createStringSymbol("NOMINAL_TIME_QUANTA_PERIOD", mcanNominalBitTimingMenu)
    mcanNominalTimeQuantaPeriod.setLabel("Time Quanta (ns)")
    mcanNominalTimeQuantaPeriod.setDefaultValue(str(tqPeriod))
    mcanNominalTimeQuantaPeriod.setReadOnly(True)

    mcanCalculatedNominalBitrate = mcanComponent.createIntegerSymbol("CALCULATED_NOMINAL_BITRATE", mcanNominalBitTimingMenu)
    mcanCalculatedNominalBitrate.setLabel("Calculated Bit Rate (Kbps)")
    mcanCalculatedNominalBitrate.setDefaultValue(calculatedNominalBitrate)
    mcanCalculatedNominalBitrate.setReadOnly(True)

    mcanNominalCalculatedError = mcanComponent.createStringSymbol("CALCULATED_NOMINAL_ERRORRATE", mcanNominalBitTimingMenu)
    mcanNominalCalculatedError.setLabel("Error %")
    mcanNominalCalculatedError.setDefaultValue(str(errorRate))
    mcanNominalCalculatedError.setReadOnly(True)

    mcanNominalErrorRateCommentSym = mcanComponent.createCommentSymbol("MCAN_NOMINAL_ERRORRATE_COMMENT", mcanNominalCalculatedError)
    mcanNominalErrorRateCommentSym.setLabel("Warning!!! Error " + mcanNominalCalculatedError.getValue() + "%")
    mcanNominalErrorRateCommentSym.setVisible(abs(float(errorRate)) > 1)

    # MCAN Data Bit Timing Calculation
    mcanDataBitTimingMenu = mcanComponent.createMenuSymbol("DATA_BIT_TIMING_CALCULATION", mcanBitTimingCalculationMenu)
    mcanDataBitTimingMenu.setLabel("Data Bit Timing")
    mcanDataBitTimingMenu.setDescription("This timing must be greater or equal to the Nominal Bit Timing")
    mcanDataBitTimingMenu.setVisible(False)
    mcanDataBitTimingMenu.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    mcanAutomaticDataBitTimingCalculation = mcanComponent.createBooleanSymbol("AUTO_DATA_BIT_TIMING_CALCULATION", mcanDataBitTimingMenu)
    mcanAutomaticDataBitTimingCalculation.setLabel("Automatic Data Bit Timing Calculation")
    mcanAutomaticDataBitTimingCalculation.setDefaultValue(False)
    mcanAutomaticDataBitTimingCalculation.setDependencies(updateDataBitTimingSymbols, ["AUTO_DATA_BIT_TIMING_CALCULATION"])

    mcanDataBitrate = mcanComponent.createIntegerSymbol("DATA_BITRATE", mcanDataBitTimingMenu)
    mcanDataBitrate.setLabel("Bit Rate (Kbps)")
    mcanDataBitrate.setMin(1)
    mcanDataBitrate.setDefaultValue(500)
    mcanDataBitrate.setDependencies(dataBitTimingCalculation, ["DATA_BITRATE", "AUTO_DATA_BIT_TIMING_CALCULATION", "MCAN_OPMODE", "core." + mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    mcanDataSamplePoint = mcanComponent.createFloatSymbol("DATA_SAMPLE_POINT", mcanDataBitTimingMenu)
    mcanDataSamplePoint.setLabel("Sample Point %")
    mcanDataSamplePoint.setMin(50.0)
    mcanDataSamplePoint.setMax(100.0)
    mcanDataSamplePoint.setDefaultValue(75.0)
    mcanDataSamplePoint.setDependencies(dataBitTimingCalculation, ["DATA_SAMPLE_POINT"])
    mcanDataSamplePoint.setReadOnly(Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_DATA_BIT_TIMING_CALCULATION") == True)

    DBTPprescale = mcanComponent.createIntegerSymbol("DBTP_DBRP", mcanDataBitTimingMenu)
    DBTPprescale.setLabel("Bit Rate Prescaler")
    DBTPprescale.setMin(0)
    DBTPprescale.setMax(31)
    DBTPprescale.setDefaultValue(0)
    DBTPprescale.setDependencies(dataBitTimingCalculation, ["DBTP_DBRP"])
    DBTPprescale.setReadOnly(Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_DATA_BIT_TIMING_CALCULATION") == True)

    mcanDataTotalTimeQuanta = mcanComponent.createIntegerSymbol("DBTP_TOTAL_TIME_QUANTA", mcanDataBitTimingMenu)
    mcanDataTotalTimeQuanta.setLabel("Total Time Quanta (TQ)")
    mcanDataTotalTimeQuanta.setReadOnly(True)

    mcanDataSyncSegment = mcanComponent.createIntegerSymbol("DBTP_SYNC", mcanDataTotalTimeQuanta)
    mcanDataSyncSegment.setLabel("Sync Segment (TQ)")
    mcanDataSyncSegment.setDefaultValue(1)
    mcanDataSyncSegment.setReadOnly(True)

    DBTPBeforeSP = mcanComponent.createIntegerSymbol("DBTP_DTSEG1", mcanDataTotalTimeQuanta)
    DBTPBeforeSP.setLabel("Time Segment Before Sample Point (TQ)")
    DBTPBeforeSP.setMin(2)
    DBTPBeforeSP.setMax(32)
    DBTPBeforeSP.setReadOnly(True)

    DBTPAfterSP = mcanComponent.createIntegerSymbol("DBTP_DTSEG2", mcanDataTotalTimeQuanta)
    DBTPAfterSP.setLabel("Time Segment After Sample Point (TQ)")
    DBTPAfterSP.setMin(1)
    DBTPAfterSP.setMax(16)
    DBTPAfterSP.setReadOnly(True)

    if Database.getSymbolValue(mcanInstanceName.getValue().lower(), "AUTO_DATA_BIT_TIMING_CALCULATION") == True:
        errorRate, calculatedDataBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = autoBitTimingCalculation("Data", 4, 49)
    else:
        errorRate, calculatedDataBitrate, tqPeriod, timeQuanta, tseg1, tseg2, sjw = bitTimingCalculation("Data", 4, 49)

    mcanDataTotalTimeQuanta.setDefaultValue(timeQuanta)
    DBTPBeforeSP.setDefaultValue(tseg1)
    DBTPAfterSP.setDefaultValue(tseg2)

    DBTPsyncJump = mcanComponent.createIntegerSymbol("DBTP_DSJW", mcanDataBitTimingMenu)
    DBTPsyncJump.setLabel("Synchronization Jump Width (TQ)")
    DBTPsyncJump.setMin(1)
    DBTPsyncJump.setDefaultValue(sjw)
    DBTPsyncJump.setMax(8)

    mcanDataTimeQuantaPeriod = mcanComponent.createStringSymbol("DATA_TIME_QUANTA_PERIOD", mcanDataBitTimingMenu)
    mcanDataTimeQuantaPeriod.setLabel("Time Quanta (ns)")
    mcanDataTimeQuantaPeriod.setDefaultValue(str(tqPeriod))
    mcanDataTimeQuantaPeriod.setReadOnly(True)

    mcanCalculatedDataBitrate = mcanComponent.createIntegerSymbol("CALCULATED_DATA_BITRATE", mcanDataBitTimingMenu)
    mcanCalculatedDataBitrate.setLabel("Calculated Bit Rate (Kbps)")
    mcanCalculatedDataBitrate.setDefaultValue(calculatedDataBitrate)
    mcanCalculatedDataBitrate.setReadOnly(True)

    mcanDataCalculatedError = mcanComponent.createStringSymbol("CALCULATED_DATA_ERRORRATE", mcanDataBitTimingMenu)
    mcanDataCalculatedError.setLabel("Error %")
    mcanDataCalculatedError.setDefaultValue(str(errorRate))
    mcanDataCalculatedError.setReadOnly(True)

    mcanDataErrorRateCommentSym = mcanComponent.createCommentSymbol("MCAN_DATA_ERRORRATE_COMMENT", mcanDataCalculatedError)
    mcanDataErrorRateCommentSym.setLabel("Warning!!! Error " + mcanDataCalculatedError.getValue() + "%")
    mcanDataErrorRateCommentSym.setVisible(abs(float(errorRate)) > 1)

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
    mcanRXF0elementSize.setDependencies(updateElementSize, ["MCAN_OPMODE"])

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
    mcanRXF1elementSize.setDependencies(updateElementSize, ["MCAN_OPMODE"])

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
    mcanTXElementCfg.setDependencies(updateElementSize, ["MCAN_OPMODE"])

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

    mcanTimestampEnable = mcanComponent.createBooleanSymbol("TIMESTAMP_ENABLE", None)
    mcanTimestampEnable.setLabel("Timestamp Enable")
    mcanTimestampEnable.setDefaultValue(False)

    #timestamp Modes
    mcanTimestampMode = mcanComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", mcanTimestampEnable)
    mcanTimestampMode.setLabel("Timestamp mode")
    mcanTimestampMode.setDescription("EXT TIMESTAMP: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_ALWAYS_0", "0", "ZERO")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_TCP_INC", "1", "TCP INC")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_EXT_TIMESTAMP", "2", "EXT TIMESTAMP")
    mcanTimestampMode.setOutputMode("Key")
    mcanTimestampMode.setDisplayMode("Description")
    mcanTimestampMode.setDefaultValue(1)
    mcanTimestampMode.setVisible(False)
    mcanTimestampMode.setDependencies(hideMenu, ["TIMESTAMP_ENABLE"])

    #timestamp/timeout Counter Prescaler
    mcanTCP = mcanComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", None)
    mcanTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    mcanTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of MCAN bit times.")
    mcanTCP.setDefaultValue(0)
    mcanTCP.setMin(0)
    mcanTCP.setMax(15)

    mcanGenerateLegacyAPIs = mcanComponent.createBooleanSymbol("MCAN_GENERATE_LEGACY_APIS", None)
    mcanGenerateLegacyAPIs.setLabel("Generate Legacy APIs")
    mcanGenerateLegacyAPIs.setDescription("Generates Legacy APIs for backward compatibility. Legacy APIs will be deprecated in future")
    mcanGenerateLegacyAPIs.setDefaultValue(False)

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
    mcanMasterHeaderFile.setDependencies(updateSourceFileName, ["INTERRUPT_MODE", "MCAN_GENERATE_LEGACY_APIS"])

    #Instance Source File
    mcanMainSourceFile = mcanComponent.createFileSymbol("sourceFile", None)
    mcanMainSourceFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/plib_mcan.c.ftl")
    mcanMainSourceFile.setOutputName("plib_"+mcanInstanceName.getValue().lower()+".c")
    mcanMainSourceFile.setDestPath("/peripheral/mcan/")
    mcanMainSourceFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    mcanMainSourceFile.setType("SOURCE")
    mcanMainSourceFile.setMarkup(True)
    mcanMainSourceFile.setDependencies(updateSourceFileName, ["INTERRUPT_MODE", "MCAN_GENERATE_LEGACY_APIS"])

    #Instance Header File
    mcanInstHeaderFile = mcanComponent.createFileSymbol("instHeaderFile", None)
    mcanInstHeaderFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/plib_mcan.h.ftl")
    mcanInstHeaderFile.setOutputName("plib_"+mcanInstanceName.getValue().lower()+".h")
    mcanInstHeaderFile.setDestPath("/peripheral/mcan/")
    mcanInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    mcanInstHeaderFile.setType("HEADER")
    mcanInstHeaderFile.setMarkup(True)
    mcanInstHeaderFile.setDependencies(updateSourceFileName, ["INTERRUPT_MODE", "MCAN_GENERATE_LEGACY_APIS"])

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
