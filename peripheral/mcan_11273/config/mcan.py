"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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
opModeValues = ["NORMAL", "CONFIGURATION", "FD", "RESTRICTED", "MONITOR", "EXT LOOPBACK", "INT LOOPBACK"]

stdFilterList = []
extFilterList = []

# if the mode is changed to FD, then show options for more bytes
def showWhenFD(element, event):
    if event["value"] == 'FD':
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
    fifo.setDefaultValue(7)
    fifo.setOutputMode("Value")
    fifo.setDisplayMode("Description")
    fifo.setDependencies(showWhenFD, ["MCAN_OPMODE"])

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
    config.setOutputMode("Value")
    config.setDisplayMode("Description")
    config.setDefaultValue(1)

def mcanCreateStdFilter(component, menu, filterNumber):
    stdFilter = component.createMenuSymbol(mcanInstanceName.getValue() + "_STD_FILTER"+ str(filterNumber), menu)
    stdFilter.setLabel("Standard Filter " + str(filterNumber))
    stdFilterType = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_TYPE", stdFilter)
    adornFilterType(stdFilterType)
    sfid1 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setMin(0)
    sfid1.setMax(2047)
    sfid2 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setMin(0)
    sfid2.setMax(2047)

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    adornFilterConfig(config)

    stdFilter.setVisible(False)
    stdFilter.setEnabled(False)
    return stdFilter

def mcanCreateExtFilter(component, menu, filterNumber):
    extFilter = component.createMenuSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber), menu)
    extFilter.setLabel("Extended Filter " + str(filterNumber))
    extFilterType = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_TYPE", extFilter)
    adornFilterType(extFilterType)
    efid1 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setMin(0)
    efid1.setMax(2047)
    efid2 = component.createIntegerSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setMin(0)
    efid2.setMax(2047)

    config = component.createKeyValueSetSymbol(mcanInstanceName.getValue() + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
    adornFilterConfig(config)

    extFilter.setVisible(False)
    extFilter.setEnabled(False)
    return extFilter

# adjust how many standard filters are shown based on number entered
def adjustStdFilters(filterList, event):
    print event["value"]
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
    print event["value"]
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
        Database.clearSymbolValue("core", interruptVector)
        Database.setSymbolValue("core", interruptVector, True, 2)

        Database.clearSymbolValue("core", interruptHandler)
        Database.setSymbolValue("core", interruptHandler, mcanInstanceName.getValue() + "_INT0_InterruptHandler", 2)

        Database.clearSymbolValue("core", interruptHandlerLock)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        global mcanIntSymbolIds
        intStatus = False

        for symbolId in mcanIntSymbolIds:
            intStatus = intStatus or Database.getSymbolValue(mcanInstanceName.getValue().lower(), symbolId)

        if intStatus == False:
            Database.clearSymbolValue("core", interruptVector)
            Database.setSymbolValue("core", interruptVector, False, 2)

            Database.clearSymbolValue("core", interruptHandler)
            Database.setSymbolValue("core", interruptHandler, mcanInstanceName.getValue() + "_INT0_Handler", 2)

            Database.clearSymbolValue("core", interruptHandlerLock)
            Database.setSymbolValue("core", interruptHandlerLock, False, 2)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):
    global mcanIntSymbolIds
    intStatus = False

    for symbolId in mcanIntSymbolIds:
        intStatus = intStatus or Database.getSymbolValue(mcanInstanceName.getValue().lower(), symbolId)

    if intStatus == True:
        symbol.setVisible(event["value"])

def instantiateComponent(mcanComponent):
    global mcanInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    
    mcanInstanceName = mcanComponent.createStringSymbol("MCAN_INSTANCE_NAME", None)
    mcanInstanceName.setVisible(False)
    mcanInstanceName.setDefaultValue(mcanComponent.getID().upper())
    print("Running " + mcanInstanceName.getValue())

    #main menu
    mcanMenu = mcanComponent.createMenuSymbol("topMenu", None)
    mcanMenu.setLabel("Hardware Settings")

    # PCK5 clock needs to be enabled and have a prescale value
    Database.setSymbolValue("core", "PMC_SCER_PCK5", True, 2)
    Database.setSymbolValue("core", "PMC_PCK5_PRES", 1, 2)

    def hideMenu(menu, event):
        menu.setVisible(event["value"])
        menu.setEnabled(event["value"])

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

    # MCAN operation mode - default to FD
    mcanOpMode = mcanComponent.createComboSymbol("MCAN_OPMODE", mcanMenu, opModeValues)
    mcanOpMode.setLabel("MCAN Operation Mode")
    mcanOpMode.setDefaultValue("FD")

    # MCAN Timing FBTP for FD and BTP for normal operation mode
    mcanTimingMenu = mcanComponent.createMenuSymbol("timingMenu", mcanMenu)
    mcanTimingMenu.setLabel("Timing for Normal operation and FD arbitration")
    mcanTimingMenu.setDescription("This timing must be less or equal to the FD data rate (if used)")
    
    BTPsyncJump = mcanComponent.createIntegerSymbol("BTP_SJW", mcanTimingMenu)
    BTPsyncJump.setLabel("Synchronization Jump Width")
    BTPsyncJump.setMin(0)
    BTPsyncJump.setMax(15)
    BTPsyncJump.setDefaultValue(3)

    BTPBefore = mcanComponent.createIntegerSymbol("BTP_TSEG1", mcanTimingMenu)
    BTPBefore.setLabel("Segment Before duration:")
    BTPBefore.setMin(1)
    BTPBefore.setMax(63)
    BTPBefore.setDefaultValue(10)

    BTPAfter = mcanComponent.createIntegerSymbol("BTP_TSEG2", mcanTimingMenu)
    BTPAfter.setLabel("Segment After duration:")
    BTPAfter.setMin(0)
    BTPAfter.setMax(15)
    BTPAfter.setDefaultValue(3)

    BTPprescale = mcanComponent.createIntegerSymbol("BTP_BRP", mcanTimingMenu)
    BTPprescale.setLabel("BAUD rate prescaler:")
    BTPprescale.setMin(0)
    BTPprescale.setMax(1023)
    BTPprescale.setDefaultValue(0)

    mcanFastTimingMenu = mcanComponent.createMenuSymbol("fastTimingMenu", mcanMenu)
    mcanFastTimingMenu.setLabel("Timing for FD operation")
    mcanFastTimingMenu.setDependencies(showWhenFD, ["MCAN_OPMODE"])

    FBTPsyncJump = mcanComponent.createIntegerSymbol("FBTP_FSJW", mcanFastTimingMenu)
    FBTPsyncJump.setLabel("Fast Synchronization Jump Width")
    FBTPsyncJump.setMin(0)
    FBTPsyncJump.setDefaultValue(3)
    FBTPsyncJump.setMax(3)

    FBTPBefore = mcanComponent.createIntegerSymbol("FBTP_FTSEG1", mcanFastTimingMenu)
    FBTPBefore.setLabel("Segment Before duration:")
    FBTPBefore.setMin(1)
    FBTPBefore.setMax(15)
    FBTPBefore.setDefaultValue(10)

    FBTPAfter = mcanComponent.createIntegerSymbol("FBTP_FTSEG2", mcanFastTimingMenu)
    FBTPAfter.setLabel("Segment After duration:")
    FBTPAfter.setMin(0)
    FBTPAfter.setDefaultValue(3)
    FBTPAfter.setMax(7)

    FBTPprescale = mcanComponent.createIntegerSymbol("FBTP_FBRP", mcanFastTimingMenu)
    FBTPprescale.setLabel("BAUD rate prescaler:")
    FBTPprescale.setMin(0)
    FBTPprescale.setMax(31)
    FBTPprescale.setDefaultValue(0)

    # ----- R X F 0 -----
    mcanRXF0 = mcanComponent.createBooleanSymbol("RXF0_USE", mcanMenu)
    mcanRXF0.setLabel("Use RX0 FIFO")
    mcanRXF0.setDefaultValue(True)

    mcanRXF0Menu = mcanComponent.createMenuSymbol("rxf0Menu", mcanRXF0)
    mcanRXF0Menu.setLabel("RX FIFO 0 Settings")
    mcanRXF0Menu.setDependencies(hideMenu, ["RXF0_USE"])

    # number of RX FIFO 0 elements
    mcanRXF0Elements = mcanComponent.createIntegerSymbol("RXF0_ELEMENTS", mcanRXF0Menu)
    mcanRXF0Elements.setLabel("Number of RX FIFO 0 Elements")
    mcanRXF0Elements.setDefaultValue(1)
    mcanRXF0Elements.setMin(0)
    mcanRXF0Elements.setMax(64)

    mcanRXF0watermarkP = mcanComponent.createIntegerSymbol("RXF0_WP", mcanRXF0Menu)
    mcanRXF0watermarkP.setLabel("RX FIFO 0 Watermark %")
    mcanRXF0watermarkP.setDefaultValue(0)
    mcanRXF0watermarkP.setMin(0)
    mcanRXF0watermarkP.setMax(99)
    
    #This is a computed value
    mcanRXF0watermark = mcanComponent.createIntegerSymbol("RXF0_WATERMARK", mcanRXF0Menu)
    mcanRXF0watermark.setLabel("Watermark at element: ")
    mcanRXF0watermark.setDescription("A value of 0 disables watermark")
    mcanRXF0watermark.setDefaultValue(0)
    mcanRXF0watermark.setReadOnly(True)
    mcanRXF0watermark.setDependencies(RXF0WatermarkUpdate, ["RXF0_ELEMENTS", "RXF0_WP"])
    
    mcanRXF0elementSize = mcanComponent.createKeyValueSetSymbol("RXF0_BYTES_CFG", mcanRXF0Menu)
    mcanRXF0elementSize.setLabel("RX FIFO 0 Element Size:")
    adornElementSize(mcanRXF0elementSize)

    mcanRx0overwrite = mcanComponent.createBooleanSymbol("RXF0_OVERWRITE", mcanRXF0Menu)
    mcanRx0overwrite.setLabel("Use RX FIFO 0 Overwrite Mode")
    mcanRx0overwrite.setDescription("Overwrite RX FIFO 0 entries without blocking")
    mcanRx0overwrite.setDefaultValue(True)

    mcanInterruptRX0NewEntry = mcanComponent.createBooleanSymbol("INT_RXF0_NEW_ENTRY", mcanRXF0Menu)
    mcanInterruptRX0NewEntry.setLabel("Use Interrupt for New Entry in RX0")
    mcanInterruptRX0NewEntry.setDefaultValue(False)

    mcanInterruptRX0Watermark = mcanComponent.createBooleanSymbol("INT_RXF0_WATERMARK", mcanRXF0Menu)
    mcanInterruptRX0Watermark.setLabel("Use Interrupt for RX FIFO 0 Watermark")
    mcanInterruptRX0Watermark.setDefaultValue(False)

    # ----- R X F 1 -----
    mcanRXF1 = mcanComponent.createBooleanSymbol("RXF1_USE", mcanMenu)
    mcanRXF1.setLabel("Use RX1 FIFO")
    mcanRXF1.setDefaultValue(True)

    mcanRXF1Menu = mcanComponent.createMenuSymbol("rxf1menu", mcanRXF1)
    mcanRXF1Menu.setLabel("RX FIFO 1 Settings")
    mcanRXF1Menu.setDependencies(hideMenu, ["RXF1_USE"])

    mcanRXF1Elements = mcanComponent.createIntegerSymbol("RXF1_ELEMENTS", mcanRXF1Menu)
    mcanRXF1Elements.setLabel("Number of RX FIFO 1 Elements")
    mcanRXF1Elements.setDefaultValue(1)
    mcanRXF1Elements.setMin(1)
    mcanRXF1Elements.setMax(64)

    mcanRXF1watermarkP = mcanComponent.createIntegerSymbol("RXF1_WP", mcanRXF1Menu)
    mcanRXF1watermarkP.setLabel("RX FIFO 1 Watermark %")
    mcanRXF1watermarkP.setDefaultValue(0)
    mcanRXF1watermarkP.setMin(0)
    mcanRXF1watermarkP.setMax(99)
    
    #This is a computed value for watermark
    mcanRX1watermark = mcanComponent.createIntegerSymbol("RXF1_WATERMARK", mcanRXF1Menu)
    mcanRX1watermark.setLabel("Watermark at element: ")
    mcanRX1watermark.setDescription("A value of 0 disables watermark")
    mcanRX1watermark.setDefaultValue(0)
    mcanRX1watermark.setReadOnly(True)
    mcanRX1watermark.setDependencies(RXF1WatermarkUpdate, ["RXF1_ELEMENTS", "RXF1_WP"])
    
    mcanRXF1elementSize = mcanComponent.createKeyValueSetSymbol("RXF1_BYTES_CFG", mcanRXF1Menu)
    mcanRXF1elementSize.setLabel("RX FIFO 1 Element Size:")
    adornElementSize(mcanRXF1elementSize)

    mcanRXF1overwrite = mcanComponent.createBooleanSymbol("RXF1_OVERWRITE", mcanRXF1Menu)
    mcanRXF1overwrite.setLabel("Use RX FIFO 1 Overwrite Mode")
    mcanRXF1overwrite.setDescription("Overwrite RX FIFO 1 entries without blocking")
    mcanRXF1overwrite.setDefaultValue(True)

    mcanInterruptRX1NewEntry = mcanComponent.createBooleanSymbol("INT_RXF1_NEW_ENTRY", mcanRXF1Menu)
    mcanInterruptRX1NewEntry.setLabel("Use Interrupt for New Entry in RX1")
    mcanInterruptRX1NewEntry.setDefaultValue(False)

    mcanInterruptRX1Watermark = mcanComponent.createBooleanSymbol("INT_RXF1_WATERMARK", mcanRXF1Menu)
    mcanInterruptRX1Watermark.setLabel("Use Interrupt for RX FIFO 1 Watermark")
    mcanInterruptRX1Watermark.setDefaultValue(False)

    # ------  T X  --------------
    mcanTX = mcanComponent.createBooleanSymbol("TX_USE", mcanMenu)
    mcanTX.setLabel("Use TX FIFO")
    mcanTX.setDefaultValue(True)

    # make a menu separate for TX so it can be turned off and on at one point
    mcanTXmenu = mcanComponent.createMenuSymbol("mcantx", mcanTX)
    mcanTXmenu.setLabel("TX FIFO Settings")
    mcanTXmenu.setDependencies(hideMenu, ["TX_USE"])

    # number of TX FIFO elements
    mcanTXnumElements = mcanComponent.createIntegerSymbol("TX_FIFO_ELEMENTS", mcanTXmenu)
    mcanTXnumElements.setLabel("Number of TX FIFO Elements")
    mcanTXnumElements.setDefaultValue(1)
    mcanTXnumElements.setMin(1)
    mcanTXnumElements.setMax(32)

    mcanTXwatermarkP = mcanComponent.createIntegerSymbol("TX_FIFO_WP", mcanTXmenu)
    mcanTXwatermarkP.setLabel("TX FIFO Watermark %")
    mcanTXwatermarkP.setDefaultValue(0)
    mcanTXwatermarkP.setMin(0)
    mcanTXwatermarkP.setMax(99)
    
    #This is a computed value for watermark
    mcanTXwatermark = mcanComponent.createIntegerSymbol("TX_FIFO_WATERMARK", mcanTXmenu)
    mcanTXwatermark.setLabel("Watermark at element: ")
    mcanTXwatermark.setDescription("A value of 0 disables watermark")
    mcanTXwatermark.setDefaultValue(0)
    mcanTXwatermark.setReadOnly(True)
    mcanTXwatermark.setDependencies(TXWatermarkUpdate, ["TX_FIFO_ELEMENTS", "TX_FIFO_WP"])

    mcanTXElementCfg = mcanComponent.createKeyValueSetSymbol("TX_FIFO_BYTES_CFG", mcanTXmenu)
    mcanTXElementCfg.setLabel("TX Element Size:")
    adornElementSize(mcanTXElementCfg)

    mcanTXpause = mcanComponent.createBooleanSymbol("TX_PAUSE", mcanTXmenu)
    mcanTXpause.setLabel("Enable TX Pause")
    mcanTXpause.setDescription("Pause 2 MCAN bit times between transmissions")
    mcanTXpause.setDefaultValue(False)

    mcanInterruptTXcompleted = mcanComponent.createBooleanSymbol("INT_TX_COMPLETED", mcanTXmenu)
    mcanInterruptTXcompleted.setLabel("Use Interrupt for TX Completed")
    mcanInterruptTXcompleted.setDefaultValue(False)

    mcanInterruptTXEmpty = mcanComponent.createBooleanSymbol("INT_TX_FIFO_EMPTY", mcanTXmenu)
    mcanInterruptTXEmpty.setLabel("Use Interrupt for TX FIFO Empty")
    mcanInterruptTXEmpty.setDefaultValue(False)

    mcanInterruptTXWatermark = mcanComponent.createBooleanSymbol("INT_TX_FIFO_WATERMARK", mcanTXmenu)
    mcanInterruptTXWatermark.setLabel("Use Interrupt for TX FIFO Watermark")
    mcanInterruptTXWatermark.setDefaultValue(False)

    # up to 128 standard filters
    mcanStdFilterMenu = mcanComponent.createMenuSymbol("stdFilterMenu", mcanMenu)
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
    mcanNoMatchStandard = mcanComponent.createKeyValueSetSymbol("FILTERS_STD_NOMATCH", mcanMenu)
    mcanNoMatchStandard.setLabel("Standard message No-Match disposition:")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_0", "0", "Move to RX FIFO 0")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_1", "1", "Move to RX FIFO 1")
    mcanNoMatchStandard.addKey("MCAN_GFC_ANFS(2)",        "2", "Reject")
    mcanNoMatchStandard.setOutputMode("Key")
    mcanNoMatchStandard.setDisplayMode("Description")
    mcanNoMatchStandard.setDefaultValue(2)

    # Reject all standard IDs?
    mcanStdReject = mcanComponent.createBooleanSymbol("FILTERS_STD_REJECT", mcanMenu)
    mcanStdReject.setLabel("Reject all Standard Messages")
    mcanStdReject.setDescription("Reject all remote frames with 11-bit standard IDs")
    mcanStdReject.setDefaultValue(False)

    # 64 extended filters
    mcanExtFilterMenu = mcanComponent.createMenuSymbol("extFilterMenu", mcanMenu)
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

    # Reject all extended IDs?
    mcanExtReject = mcanComponent.createBooleanSymbol("FILTERS_EXT_REJECT", mcanMenu)
    mcanExtReject.setLabel("Reject all Extended Messages")
    mcanExtReject.setDescription("Reject all remote frames with 29-bit extended IDs")
    mcanExtReject.setDefaultValue(False)

    #What to do when a NO-MATCH is detected on an extended message
    mcanNoMatchExtended = mcanComponent.createKeyValueSetSymbol("FILTERS_EXT_NOMATCH", mcanMenu)
    mcanNoMatchExtended.setLabel("Extended message No-Match disposition:")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_0", "0", "Move to RX FIFO 0")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_1", "1", "Move to RX FIFO 1")
    mcanNoMatchExtended.addKey("MCAN_GFC_ANFE(2)",        "2", "Reject")
    mcanNoMatchExtended.setOutputMode("Key")
    mcanNoMatchExtended.setDisplayMode("Description")
    mcanNoMatchExtended.setDefaultValue(2)

    #use timeout?
    mcanUseTimeout = mcanComponent.createBooleanSymbol("MCAN_TIMEOUT", mcanMenu)
    mcanUseTimeout.setLabel("Use Timeout Counter")
    mcanUseTimeout.setDescription("Enables Timeout Counter")
    mcanUseTimeout.setDefaultValue(True)

    #timout count
    mcanTimeoutCount = mcanComponent.createIntegerSymbol("TIMEOUT_COUNT", mcanUseTimeout)
    mcanTimeoutCount.setDependencies(hideMenu, ["MCAN_TIMEOUT"])
    mcanTimeoutCount.setLabel("Timeout Countdown from: ")
    mcanTimeoutCount.setDefaultValue(40000)
    mcanTimeoutCount.setMin(10)
    mcanTimeoutCount.setMax(65535)

    #timeout mode
    mcanTimeoutMode = mcanComponent.createKeyValueSetSymbol("TIMEOUT_SELECT", mcanUseTimeout)
    mcanTimeoutMode.setLabel("Timeout mode:")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_CONTINUOUS", "0", "CONTINUOUS")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_TX_EV_TIMEOUT", "1", "TX EVENT")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_RX0_EV_TIMEOUT", "2", "RX0 EVENT")
    mcanTimeoutMode.addKey("MCAN_TOCC_TOS_RX1_EV_TIMEOUT", "3", "RX1 EVENT")
    mcanTimeoutMode.setOutputMode("Key")
    mcanTimeoutMode.setDisplayMode("Description")
    mcanTimeoutMode.setDependencies(hideMenu, ["MCAN_TIMEOUT"])
    mcanTimeoutMode.setDefaultValue(1)

    #timeout interrupt
    mcanInterruptTimeout = mcanComponent.createBooleanSymbol("INT_TIMEOUT", mcanUseTimeout)
    mcanInterruptTimeout.setLabel("Use Interrupt for Timeout")
    mcanInterruptTimeout.setDependencies(hideMenu, ["MCAN_TIMEOUT"])
    mcanInterruptTimeout.setDefaultValue(False)

    #timestamp Modes
    mcanTimestampMode = mcanComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", mcanMenu)
    mcanTimestampMode.setLabel("Timestamp mode")
    mcanTimestampMode.setDescription("EXT INC: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_ALWAYS_0", "0", "ZERO")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_TCP_INC", "1", "TCP INC")
    mcanTimestampMode.addKey("MCAN_TSCC_TSS_EXT_TIMESTAMP", "2", "EXT INC")
    mcanTimestampMode.setOutputMode("Key")
    mcanTimestampMode.setDisplayMode("Description")
    mcanTimestampMode.setDefaultValue(1)

    #timestamp/timeout Counter Prescaler
    mcanTCP = mcanComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", mcanMenu)
    mcanTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    mcanTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of MCAN bit times.")
    mcanTCP.setDefaultValue(1)
    mcanTCP.setMin(1)
    mcanTCP.setMax(16)

    # Initialize peripheral clock
    Database.clearSymbolValue("core", mcanInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", mcanInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)
    
    # get peripheral id for MCAN
    interruptVector = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE"
    interruptHandler = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER"
    interruptHandlerLock = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = mcanInstanceName.getValue() + "_INT0" + "_INTERRUPT_ENABLE_UPDATE"

    global mcanIntSymbolIds
    mcanIntSymbolIds = ["INT_RXF0_NEW_ENTRY", "INT_RXF0_WATERMARK", "INT_RXF1_NEW_ENTRY", \
                        "INT_RXF1_WATERMARK", "INT_TX_COMPLETED", "INT_TX_FIFO_EMPTY", \
                        "INT_TX_FIFO_WATERMARK", "INT_TIMEOUT"]
    
    # NVIC Dynamic settings
    mcaninterruptControl = mcanComponent.createBooleanSymbol("MCAN_NVIC_ENABLE", None)
    mcaninterruptControl.setVisible(False)
    mcaninterruptControl.setDependencies(interruptControl, mcanIntSymbolIds)

    # Dependency Status for interrupt
    mcanIntEnComment = mcanComponent.createCommentSymbol("MCAN_NVIC_ENABLE_COMMENT", None)
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
    mcanSystemInitFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/system_initialize.c.ftl")
    mcanSystemInitFile.setMarkup(True)

    #MCAN definitions header
    mcanSystemDefFile = mcanComponent.createFileSymbol("defFile", None)
    mcanSystemDefFile.setType("STRING")
    mcanSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mcanSystemDefFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/system_definitions.h.ftl")
    mcanSystemDefFile.setMarkup(True)


def getMasterClockFreq():
    return int(Database.getSymbolValue("core", mcanInstanceName.getValue() + "_CLOCK_FREQUENCY"))

'''********************************End of the file*************************'''
