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
        element.setEnabled(True)
    else:
        element.setVisible(False)
        element.setEnabled(False)

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
    fifo.setDependencies(showWhenFD, ["CAN_OPMODE"])

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

def canCreateStdFilter(component, menu, filterNumber):
    stdFilter = component.createMenuSymbol(canInstanceName.getValue() + "_STD_FILTER"+ str(filterNumber), menu)
    stdFilter.setLabel("Standard Filter " + str(filterNumber))
    stdFilterType = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE", stdFilter)
    adornFilterType(stdFilterType)
    sfid1 = component.createIntegerSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setMin(0)
    sfid1.setMax(2047)
    sfid2 = component.createIntegerSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setMin(0)
    sfid2.setMax(2047)

    config = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    adornFilterConfig(config)

    stdFilter.setVisible(False)
    stdFilter.setEnabled(False)
    return stdFilter

def canCreateExtFilter(component, menu, filterNumber):
    extFilter = component.createMenuSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber), menu)
    extFilter.setLabel("Extended Filter " + str(filterNumber))
    extFilterType = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE", extFilter)
    adornFilterType(extFilterType)
    efid1 = component.createIntegerSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setMin(0)
    efid1.setMax(2047)
    efid2 = component.createIntegerSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setMin(0)
    efid2.setMax(2047)

    config = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
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

def instantiateComponent(canComponent):
    global canInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate

    canInstanceName = canComponent.createStringSymbol("CAN_INSTANCE_NAME", None)
    canInstanceName.setVisible(False)
    canInstanceName.setDefaultValue(canComponent.getID().upper())
    print("Running " + canInstanceName.getValue())

    #main menu
    canMenu = canComponent.createMenuSymbol("topMenu", None)
    canMenu.setLabel("Hardware Settings")

    def hideMenu(menu, event):
        menu.setVisible(event["value"])
        menu.setEnabled(event["value"])

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

    # CAN operation mode - default to FD
    canOpMode = canComponent.createComboSymbol("CAN_OPMODE", canMenu, opModeValues)
    canOpMode.setLabel("CAN Operation Mode")
    canOpMode.setDefaultValue("NORMAL")

    canInterruptMode = canComponent.createBooleanSymbol("INTERRUPT_MODE", canMenu)
    canInterruptMode.setLabel("Interrupt Mode")
    canInterruptMode.setDefaultValue(False)

    interruptVector = canInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = canInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = canInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = canInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # CAN Timing DBTP for FD and NBTP for normal operation mode
    canTimingMenu = canComponent.createMenuSymbol("timingMenu", canMenu)
    canTimingMenu.setLabel("Timing for Normal operation and FD arbitration")
    canTimingMenu.setDescription("This timing must be less or equal to the FD data rate (if used)")

    NBTPsyncJump = canComponent.createIntegerSymbol("NBTP_SJW", canTimingMenu)
    NBTPsyncJump.setLabel("Synchronization Jump Width")
    NBTPsyncJump.setMin(0)
    NBTPsyncJump.setMax(15)
    NBTPsyncJump.setDefaultValue(3)

    NBTPBefore = canComponent.createIntegerSymbol("NBTP_TSEG1", canTimingMenu)
    NBTPBefore.setLabel("Segment Before duration:")
    NBTPBefore.setMin(1)
    NBTPBefore.setMax(63)
    NBTPBefore.setDefaultValue(10)

    NBTPAfter = canComponent.createIntegerSymbol("NBTP_TSEG2", canTimingMenu)
    NBTPAfter.setLabel("Segment After duration:")
    NBTPAfter.setMin(0)
    NBTPAfter.setMax(15)
    NBTPAfter.setDefaultValue(3)

    NBTPprescale = canComponent.createIntegerSymbol("NBTP_BRP", canTimingMenu)
    NBTPprescale.setLabel("BAUD rate prescaler:")
    NBTPprescale.setMin(0)
    NBTPprescale.setMax(1023)
    NBTPprescale.setDefaultValue(0)

    canFastTimingMenu = canComponent.createMenuSymbol("fastTimingMenu", canMenu)
    canFastTimingMenu.setLabel("Timing for FD operation")
    canFastTimingMenu.setVisible(False)
    canFastTimingMenu.setDependencies(showWhenFD, ["CAN_OPMODE"])

    DBTPsyncJump = canComponent.createIntegerSymbol("DBTP_FSJW", canFastTimingMenu)
    DBTPsyncJump.setLabel("Fast Synchronization Jump Width")
    DBTPsyncJump.setMin(0)
    DBTPsyncJump.setDefaultValue(3)
    DBTPsyncJump.setMax(3)

    DBTPBefore = canComponent.createIntegerSymbol("DBTP_FTSEG1", canFastTimingMenu)
    DBTPBefore.setLabel("Segment Before duration:")
    DBTPBefore.setMin(1)
    DBTPBefore.setMax(15)
    DBTPBefore.setDefaultValue(10)

    DBTPAfter = canComponent.createIntegerSymbol("DBTP_FTSEG2", canFastTimingMenu)
    DBTPAfter.setLabel("Segment After duration:")
    DBTPAfter.setMin(0)
    DBTPAfter.setDefaultValue(3)
    DBTPAfter.setMax(7)

    DBTPprescale = canComponent.createIntegerSymbol("DBTP_DBRP", canFastTimingMenu)
    DBTPprescale.setLabel("BAUD rate prescaler:")
    DBTPprescale.setMin(0)
    DBTPprescale.setMax(31)
    DBTPprescale.setDefaultValue(0)

    # ----- Rx FIFO 0 -----
    canRXF0 = canComponent.createBooleanSymbol("RXF0_USE", canMenu)
    canRXF0.setLabel("Use RX0 FIFO")
    canRXF0.setDefaultValue(True)
    canRXF0.setReadOnly(True)

    canRXF0Menu = canComponent.createMenuSymbol("rxf0Menu", canRXF0)
    canRXF0Menu.setLabel("RX FIFO 0 Settings")
    canRXF0Menu.setDependencies(hideMenu, ["RXF0_USE"])

    # number of RX FIFO 0 elements
    canRXF0Elements = canComponent.createIntegerSymbol("RXF0_ELEMENTS", canRXF0Menu)
    canRXF0Elements.setLabel("Number of RX FIFO 0 Elements")
    canRXF0Elements.setDefaultValue(1)
    canRXF0Elements.setMin(0)
    canRXF0Elements.setMax(64)

    canRXF0watermarkP = canComponent.createIntegerSymbol("RXF0_WP", canRXF0Menu)
    canRXF0watermarkP.setLabel("RX FIFO 0 Watermark %")
    canRXF0watermarkP.setDefaultValue(0)
    canRXF0watermarkP.setMin(0)
    canRXF0watermarkP.setMax(99)

    #This is a computed value
    canRXF0watermark = canComponent.createIntegerSymbol("RXF0_WATERMARK", canRXF0Menu)
    canRXF0watermark.setLabel("Watermark at element: ")
    canRXF0watermark.setDescription("A value of 0 disables watermark")
    canRXF0watermark.setDefaultValue(0)
    canRXF0watermark.setReadOnly(True)
    canRXF0watermark.setDependencies(RXF0WatermarkUpdate, ["RXF0_ELEMENTS", "RXF0_WP"])

    canRXF0elementSize = canComponent.createKeyValueSetSymbol("RXF0_BYTES_CFG", canRXF0Menu)
    canRXF0elementSize.setLabel("RX FIFO 0 Element Size:")
    adornElementSize(canRXF0elementSize)

    canRx0overwrite = canComponent.createBooleanSymbol("RXF0_OVERWRITE", canRXF0Menu)
    canRx0overwrite.setLabel("Use RX FIFO 0 Overwrite Mode")
    canRx0overwrite.setDescription("Overwrite RX FIFO 0 entries without blocking")
    canRx0overwrite.setDefaultValue(True)

    # ----- Rx FIFO 1 -----
    canRXF1 = canComponent.createBooleanSymbol("RXF1_USE", canMenu)
    canRXF1.setLabel("Use RX1 FIFO")
    canRXF1.setDefaultValue(True)

    canRXF1Menu = canComponent.createMenuSymbol("rxf1menu", canRXF1)
    canRXF1Menu.setLabel("RX FIFO 1 Settings")
    canRXF1Menu.setDependencies(hideMenu, ["RXF1_USE"])

    canRXF1Elements = canComponent.createIntegerSymbol("RXF1_ELEMENTS", canRXF1Menu)
    canRXF1Elements.setLabel("Number of RX FIFO 1 Elements")
    canRXF1Elements.setDefaultValue(1)
    canRXF1Elements.setMin(1)
    canRXF1Elements.setMax(64)

    canRXF1watermarkP = canComponent.createIntegerSymbol("RXF1_WP", canRXF1Menu)
    canRXF1watermarkP.setLabel("RX FIFO 1 Watermark %")
    canRXF1watermarkP.setDefaultValue(0)
    canRXF1watermarkP.setMin(0)
    canRXF1watermarkP.setMax(99)

    #This is a computed value for watermark
    canRX1watermark = canComponent.createIntegerSymbol("RXF1_WATERMARK", canRXF1Menu)
    canRX1watermark.setLabel("Watermark at element: ")
    canRX1watermark.setDescription("A value of 0 disables watermark")
    canRX1watermark.setDefaultValue(0)
    canRX1watermark.setReadOnly(True)
    canRX1watermark.setDependencies(RXF1WatermarkUpdate, ["RXF1_ELEMENTS", "RXF1_WP"])

    canRXF1elementSize = canComponent.createKeyValueSetSymbol("RXF1_BYTES_CFG", canRXF1Menu)
    canRXF1elementSize.setLabel("RX FIFO 1 Element Size:")
    adornElementSize(canRXF1elementSize)

    canRXF1overwrite = canComponent.createBooleanSymbol("RXF1_OVERWRITE", canRXF1Menu)
    canRXF1overwrite.setLabel("Use RX FIFO 1 Overwrite Mode")
    canRXF1overwrite.setDescription("Overwrite RX FIFO 1 entries without blocking")
    canRXF1overwrite.setDefaultValue(True)

    # ----- Rx Buffer -----
    canRXBuf = canComponent.createBooleanSymbol("RXBUF_USE", canMenu)
    canRXBuf.setLabel("Use Dedicated Rx Buffer")
    canRXBuf.setDefaultValue(False)

    canRXBufElements = canComponent.createIntegerSymbol("RX_BUFFER_ELEMENTS", canRXBuf)
    canRXBufElements.setLabel("Number of Rx Buffer Elements")
    canRXBufElements.setDefaultValue(1)
    canRXBufElements.setMin(1)
    canRXBufElements.setMax(64)

    canRXBufelementSize = canComponent.createKeyValueSetSymbol("RX_BUFFER_BYTES_CFG", canRXBuf)
    canRXBufelementSize.setLabel("Rx Buffer 0 Element Size:")
    adornElementSize(canRXBufelementSize)

    # ------  T X  --------------
    # ----- Tx FIFO -----
    canTX = canComponent.createBooleanSymbol("TX_USE", canMenu)
    canTX.setLabel("Use TX FIFO")
    canTX.setDefaultValue(True)
    canTX.setReadOnly(True)

    # make a menu separate for TX so it can be turned off and on at one point
    canTXmenu = canComponent.createMenuSymbol("cantx", canTX)
    canTXmenu.setLabel("TX FIFO Settings")
    canTXmenu.setDependencies(hideMenu, ["TX_USE"])

    # number of TX FIFO elements
    canTXnumElements = canComponent.createIntegerSymbol("TX_FIFO_ELEMENTS", canTXmenu)
    canTXnumElements.setLabel("Number of TX FIFO Elements")
    canTXnumElements.setDefaultValue(1)
    canTXnumElements.setMin(1)
    canTXnumElements.setMax(32)

    canTXwatermarkP = canComponent.createIntegerSymbol("TX_FIFO_WP", canTXmenu)
    canTXwatermarkP.setLabel("TX FIFO Watermark %")
    canTXwatermarkP.setDefaultValue(0)
    canTXwatermarkP.setMin(0)
    canTXwatermarkP.setMax(99)

    #This is a computed value for watermark
    canTXwatermark = canComponent.createIntegerSymbol("TX_FIFO_WATERMARK", canTXmenu)
    canTXwatermark.setLabel("Watermark at element: ")
    canTXwatermark.setDescription("A value of 0 disables watermark")
    canTXwatermark.setDefaultValue(0)
    canTXwatermark.setReadOnly(True)
    canTXwatermark.setDependencies(TXWatermarkUpdate, ["TX_FIFO_ELEMENTS", "TX_FIFO_WP"])

    canTXElementCfg = canComponent.createKeyValueSetSymbol("TX_FIFO_BYTES_CFG", canTXmenu)
    canTXElementCfg.setLabel("TX Element Size:")
    adornElementSize(canTXElementCfg)

    canTXpause = canComponent.createBooleanSymbol("TX_PAUSE", canTXmenu)
    canTXpause.setLabel("Enable TX Pause")
    canTXpause.setDescription("Pause 2 CAN bit times between transmissions")
    canTXpause.setDefaultValue(False)

    # ----- Tx Buffer -----
    canTXBuf = canComponent.createBooleanSymbol("TXBUF_USE", canMenu)
    canTXBuf.setLabel("Use Dedicated Tx Buffer")
    canTXBuf.setDefaultValue(False)

    # number of TX buffer elements
    canTXBufElements = canComponent.createIntegerSymbol("TX_BUFFER_ELEMENTS", canTXBuf)
    canTXBufElements.setLabel("Number of TX Buffer Elements")
    canTXBufElements.setDefaultValue(0)
    canTXBufElements.setMin(0)
    canTXBufElements.setMax(32)

    # up to 128 standard filters
    canStdFilterMenu = canComponent.createMenuSymbol("stdFilterMenu", canMenu)
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
    canNoMatchStandard = canComponent.createKeyValueSetSymbol("FILTERS_STD_NOMATCH", canMenu)
    canNoMatchStandard.setLabel("Standard message No-Match disposition:")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_RXF0", "0", "Move to RX FIFO 0")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_RXF1", "1", "Move to RX FIFO 1")
    canNoMatchStandard.addKey("CAN_GFC_ANFS_REJECT", "2", "Reject")
    canNoMatchStandard.setOutputMode("Key")
    canNoMatchStandard.setDisplayMode("Description")
    canNoMatchStandard.setDefaultValue(2)

    # Reject all standard IDs?
    canStdReject = canComponent.createBooleanSymbol("FILTERS_STD_REJECT", canMenu)
    canStdReject.setLabel("Reject all Standard Messages")
    canStdReject.setDescription("Reject all remote frames with 11-bit standard IDs")
    canStdReject.setDefaultValue(False)

    # 64 extended filters
    canExtFilterMenu = canComponent.createMenuSymbol("extFilterMenu", canMenu)
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
    canNoMatchExtended = canComponent.createKeyValueSetSymbol("FILTERS_EXT_NOMATCH", canMenu)
    canNoMatchExtended.setLabel("Extended message No-Match disposition:")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_RXF0", "0", "Move to RX FIFO 0")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_RXF1", "1", "Move to RX FIFO 1")
    canNoMatchExtended.addKey("CAN_GFC_ANFE_REJECT", "2", "Reject")
    canNoMatchExtended.setOutputMode("Key")
    canNoMatchExtended.setDisplayMode("Description")
    canNoMatchExtended.setDefaultValue(2)

    # Reject all extended IDs?
    canExtReject = canComponent.createBooleanSymbol("FILTERS_EXT_REJECT", canMenu)
    canExtReject.setLabel("Reject all Extended Messages")
    canExtReject.setDescription("Reject all remote frames with 29-bit extended IDs")
    canExtReject.setDefaultValue(False)

    #use timeout?
    canUseTimeout = canComponent.createBooleanSymbol("CAN_TIMEOUT", canMenu)
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

    #timeout mode
    canTimeoutMode = canComponent.createKeyValueSetSymbol("TIMEOUT_SELECT", canUseTimeout)
    canTimeoutMode.setLabel("Timeout mode:")
    canTimeoutMode.addKey("CAN_TOCC_TOS_CONT", "0", "CONTINUOUS")
    canTimeoutMode.addKey("CAN_TOCC_TOS_TXEF", "1", "TX EVENT")
    canTimeoutMode.addKey("CAN_TOCC_TOS_RXF0", "2", "RX0 EVENT")
    canTimeoutMode.addKey("CAN_TOCC_TOS_RXF1", "3", "RX1 EVENT")
    canTimeoutMode.setOutputMode("Key")
    canTimeoutMode.setDisplayMode("Description")
    canTimeoutMode.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canTimeoutMode.setDefaultValue(1)

    #timestamp Modes
    canTimestampMode = canComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", canMenu)
    canTimestampMode.setLabel("Timestamp mode")
    canTimestampMode.setDescription("EXT INC: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    canTimestampMode.addKey("CAN_TSCC_TSS_ZERO", "0", "ZERO")
    canTimestampMode.addKey("CAN_TSCC_TSS_INC", "1", "TCP INC")
    canTimestampMode.addKey("CAN_TSCC_TSS_EXT", "2", "EXT INC")
    canTimestampMode.setOutputMode("Key")
    canTimestampMode.setDisplayMode("Description")
    canTimestampMode.setDefaultValue(1)

    #timestamp/timeout Counter Prescaler
    canTCP = canComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", canMenu)
    canTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    canTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of CAN bit times.")
    canTCP.setDefaultValue(1)
    canTCP.setMin(1)
    canTCP.setMax(16)

    # Initialize GCLK
    Database.setSymbolValue("core", canInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)

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
    canMasterHeaderFile.setSourcePath("../peripheral/can_" + REG_MODULE_CAN.getID() + "/templates/plib_can_common.h")
    canMasterHeaderFile.setOutputName("plib_can_common.h")
    canMasterHeaderFile.setDestPath("/peripheral/can/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = canComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/can_" + REG_MODULE_CAN.getID() + "/templates/plib_can.c.ftl")
    canMainSourceFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".c")
    canMainSourceFile.setDestPath("/peripheral/can/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)

    #Instance Header File
    canInstHeaderFile = canComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/can_" + REG_MODULE_CAN.getID() + "/templates/plib_can.h.ftl")
    canInstHeaderFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".h")
    canInstHeaderFile.setDestPath("/peripheral/can/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)

    #CAN Initialize
    canSystemInitFile = canComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    canSystemInitFile.setSourcePath("../peripheral/can_" + REG_MODULE_CAN.getID() + "/templates/system/system_initialize.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = canComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/can_" + REG_MODULE_CAN.getID() + "/templates/system/system_definitions.h.ftl")
    canSystemDefFile.setMarkup(True)

'''********************************End of the file*************************'''
