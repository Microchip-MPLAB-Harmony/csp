
num=0

canElementSizes = ["8 bytes", "12 bytes", "16 bytes", "20 bytes", "24 bytes", "32 bytes", "48 bytes", "64 bytes"]
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
    config.setOutputMode("Value")
    config.setDisplayMode("Description")
    config.setDefaultValue(1)

def canCreateStdFilter(component, menu, filterNumber):
    stdFilter = component.createMenuSymbol("CAN" + str(num) + "_STD_FILTER"+ str(filterNumber), menu)
    stdFilter.setLabel("Standard Filter " + str(filterNumber))
    stdFilterType = component.createKeyValueSetSymbol("CAN" + str(num) + "_STD_FILTER" + str(filterNumber) + "_TYPE", stdFilter)
    adornFilterType(stdFilterType)
    sfid1 = component.createIntegerSymbol("CAN" + str(num) + "_STD_FILTER" + str(filterNumber) + "_SFID1", stdFilter)
    sfid1.setMin(0)
    sfid1.setMax(2047)
    sfid2 = component.createIntegerSymbol("CAN" + str(num) + "_STD_FILTER" + str(filterNumber) + "_SFID2", stdFilter)
    sfid2.setMin(0)
    sfid2.setMax(2047)

    config = component.createKeyValueSetSymbol("CAN" + str(num) + "_STD_FILTER" + str(filterNumber) + "_CONFIG", stdFilter)
    adornFilterConfig(config)

    stdFilter.setVisible(False)
    stdFilter.setEnabled(False)
    return stdFilter

def canCreateExtFilter(component, menu, filterNumber):
    extFilter = component.createMenuSymbol("CAN" + str(num) + "_EXT_FILTER" + str(filterNumber), menu)
    extFilter.setLabel("Extended Filter " + str(filterNumber))
    extFilterType = component.createKeyValueSetSymbol("CAN" + str(num) + "_EXT_FILTER" + str(filterNumber) + "_TYPE", extFilter)
    adornFilterType(extFilterType)
    efid1 = component.createIntegerSymbol("CAN" + str(num) + "_EXT_FILTER" + str(filterNumber) + "_EFID1", extFilter)
    efid1.setMin(0)
    efid1.setMax(2047)
    efid2 = component.createIntegerSymbol("CAN" + str(num) + "_EXT_FILTER" + str(filterNumber) + "_EFID2", extFilter)
    efid2.setMin(0)
    efid2.setMax(2047)

    config = component.createKeyValueSetSymbol("CAN" + str(num) + "_EXT_FILTER" + str(filterNumber) + "_CONFIG", extFilter)
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

def instantiateComponent(mcanComponent):
    global num
    
    num = mcanComponent.getID()[-1:]
    print("Running MCAN" + str(num))

    #main menu
    canMenu = mcanComponent.createMenuSymbol("topMenu", None)
    canMenu.setLabel("Hardware Settings")

    # PCK5 clock needs to be enabled and have a prescale value
    Database.setSymbolValue("core", "PMC_SCER_PCK5", True, 2)
    Database.setSymbolValue("core", "PMC_PCK5_PRES", 1, 2)

    #instance index
    canIndex = mcanComponent.createIntegerSymbol("INDEX", canMenu)
    canIndex.setVisible(False)
    canIndex.setDefaultValue(int(num))

    def hideMenu(menu, event):
        menu.setVisible(event["value"])
        menu.setEnabled(event["value"])

    #either the watermark % changed or the number of elements
    def RXF0WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue("mcan" + str(num), "RXF0_WP")
        number_of_elements   = Database.getSymbolValue("mcan" + str(num), "RXF0_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def RXF1WatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue("mcan" + str(num), "RXF1_WP")
        number_of_elements   = Database.getSymbolValue("mcan" + str(num), "RXF1_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    def TXWatermarkUpdate(watermark, event):
        watermark_percentage = Database.getSymbolValue("mcan" + str(num), "TX_FIFO_WP")
        number_of_elements   = Database.getSymbolValue("mcan" + str(num), "TX_FIFO_ELEMENTS")
        watermark.setValue(watermark_percentage * number_of_elements / 100, 0)

    # CAN operation mode - default to FD
    canOpMode = mcanComponent.createComboSymbol("CAN_OPMODE", canMenu, opModeValues)
    canOpMode.setLabel("CAN Operation Mode")
    canOpMode.setDefaultValue("FD")

    # CAN Timing FBTP for FD and BTP for normal operation mode
    canTimingMenu = mcanComponent.createMenuSymbol("timingMenu", canMenu)
    canTimingMenu.setLabel("Timing for Normal operation and FD arbitration")
    canTimingMenu.setDescription("This timing must be less or equal to the FD data rate (if used)")
    
    BTPsyncJump = mcanComponent.createIntegerSymbol("BTP_SJW", canTimingMenu)
    BTPsyncJump.setLabel("Synchronization Jump Width")
    BTPsyncJump.setMin(0)
    BTPsyncJump.setMax(15)
    BTPsyncJump.setDefaultValue(3)

    BTPBefore = mcanComponent.createIntegerSymbol("BTP_TSEG1", canTimingMenu)
    BTPBefore.setLabel("Segment Before duration:")
    BTPBefore.setMin(1)
    BTPBefore.setMax(63)
    BTPBefore.setDefaultValue(10)

    BTPAfter = mcanComponent.createIntegerSymbol("BTP_TSEG2", canTimingMenu)
    BTPAfter.setLabel("Segment After duration:")
    BTPAfter.setMin(0)
    BTPAfter.setMax(15)
    BTPAfter.setDefaultValue(3)

    BTPprescale = mcanComponent.createIntegerSymbol("BTP_BRP", canTimingMenu)
    BTPprescale.setLabel("BAUD rate prescaler:")
    BTPprescale.setMin(0)
    BTPprescale.setMax(1023)
    BTPprescale.setDefaultValue(0)

    canFastTimingMenu = mcanComponent.createMenuSymbol("fastTimingMenu", canMenu)
    canFastTimingMenu.setLabel("Timing for FD operation")
    canFastTimingMenu.setDependencies(showWhenFD, ["CAN_OPMODE"])

    FBTPsyncJump = mcanComponent.createIntegerSymbol("FBTP_FSJW", canFastTimingMenu)
    FBTPsyncJump.setLabel("Fast Synchronization Jump Width")
    FBTPsyncJump.setMin(0)
    FBTPsyncJump.setDefaultValue(3)
    FBTPsyncJump.setMax(3)

    FBTPBefore = mcanComponent.createIntegerSymbol("FBTP_FTSEG1", canFastTimingMenu)
    FBTPBefore.setLabel("Segment Before duration:")
    FBTPBefore.setMin(1)
    FBTPBefore.setMax(15)
    FBTPBefore.setDefaultValue(10)

    FBTPAfter = mcanComponent.createIntegerSymbol("FBTP_FTSEG2", canFastTimingMenu)
    FBTPAfter.setLabel("Segment After duration:")
    FBTPAfter.setMin(0)
    FBTPAfter.setDefaultValue(3)
    FBTPAfter.setMax(7)

    FBTPprescale = mcanComponent.createIntegerSymbol("FBTP_FBRP", canFastTimingMenu)
    FBTPprescale.setLabel("BAUD rate prescaler:")
    FBTPprescale.setMin(0)
    FBTPprescale.setMax(31)
    FBTPprescale.setDefaultValue(0)

    # ----- R X F 0 -----
    canRXF0 = mcanComponent.createBooleanSymbol("RXF0_USE", canMenu)
    canRXF0.setLabel("Use RX0 FIFO")
    canRXF0.setDefaultValue(True)

    canRXF0Menu = mcanComponent.createMenuSymbol("rxf0Menu", canRXF0)
    canRXF0Menu.setLabel("RX FIFO 0 Settings")
    canRXF0Menu.setDependencies(hideMenu, ["RXF0_USE"])

    # number of RX FIFO 0 elements
    canRXF0Elements = mcanComponent.createIntegerSymbol("RXF0_ELEMENTS", canRXF0Menu)
    canRXF0Elements.setLabel("Number of RX FIFO 0 Elements")
    canRXF0Elements.setDefaultValue(1)
    canRXF0Elements.setMin(0)
    canRXF0Elements.setMax(64)

    canRXF0watermarkP = mcanComponent.createIntegerSymbol("RXF0_WP", canRXF0Menu)
    canRXF0watermarkP.setLabel("RX FIFO 0 Watermark %")
    canRXF0watermarkP.setDefaultValue(0)
    canRXF0watermarkP.setMin(0)
    canRXF0watermarkP.setMax(99)
    
    #This is a computed value
    canRXF0watermark = mcanComponent.createIntegerSymbol("RXF0_WATERMARK", canRXF0Menu)
    canRXF0watermark.setLabel("Watermark at element: ")
    canRXF0watermark.setDescription("A value of 0 disables watermark")
    canRXF0watermark.setDefaultValue(0)
    canRXF0watermark.setReadOnly(True)
    canRXF0watermark.setDependencies(RXF0WatermarkUpdate, ["RXF0_ELEMENTS", "RXF0_WP"])
    
    canRXF0elementSize = mcanComponent.createKeyValueSetSymbol("RXF0_BYTES_CFG", canRXF0Menu)
    canRXF0elementSize.setLabel("RX FIFO 0 Element Size:")
    adornElementSize(canRXF0elementSize)

    canRx0overwrite = mcanComponent.createBooleanSymbol("RXF0_OVERWRITE", canRXF0Menu)
    canRx0overwrite.setLabel("Use RX FIFO 0 Overwrite Mode")
    canRx0overwrite.setDescription("Overwrite RX FIFO 0 entries without blocking")
    canRx0overwrite.setDefaultValue(True)

    canInterruptRX0NewEntry = mcanComponent.createBooleanSymbol("INT_RXF0_NEW_ENTRY", canRXF0Menu)
    canInterruptRX0NewEntry.setLabel("Use Interrupt for New Entry in RX0")
    canInterruptRX0NewEntry.setDefaultValue(False)

    canInterruptRX0Watermark = mcanComponent.createBooleanSymbol("INT_RXF0_WATERMARK", canRXF0Menu)
    canInterruptRX0Watermark.setLabel("Use Interrupt for RX FIFO 0 Watermark")
    canInterruptRX0Watermark.setDefaultValue(False)

    # ----- R X F 1 -----
    canRXF1 = mcanComponent.createBooleanSymbol("RXF1_USE", canMenu)
    canRXF1.setLabel("Use RX1 FIFO")
    canRXF1.setDefaultValue(True)

    canRXF1Menu = mcanComponent.createMenuSymbol("rxf1menu", canRXF1)
    canRXF1Menu.setLabel("RX FIFO 1 Settings")
    canRXF1Menu.setDependencies(hideMenu, ["RXF1_USE"])

    canRXF1Elements = mcanComponent.createIntegerSymbol("RXF1_ELEMENTS", canRXF1Menu)
    canRXF1Elements.setLabel("Number of RX FIFO 1 Elements")
    canRXF1Elements.setDefaultValue(1)
    canRXF1Elements.setMin(1)
    canRXF1Elements.setMax(64)

    canRXF1watermarkP = mcanComponent.createIntegerSymbol("RXF1_WP", canRXF1Menu)
    canRXF1watermarkP.setLabel("RX FIFO 1 Watermark %")
    canRXF1watermarkP.setDefaultValue(0)
    canRXF1watermarkP.setMin(0)
    canRXF1watermarkP.setMax(99)
    
    #This is a computed value for watermark
    canRX1watermark = mcanComponent.createIntegerSymbol("RXF1_WATERMARK", canRXF1Menu)
    canRX1watermark.setLabel("Watermark at element: ")
    canRX1watermark.setDescription("A value of 0 disables watermark")
    canRX1watermark.setDefaultValue(0)
    canRX1watermark.setReadOnly(True)
    canRX1watermark.setDependencies(RXF1WatermarkUpdate, ["RXF1_ELEMENTS", "RXF1_WP"])
    
    canRXF1elementSize = mcanComponent.createKeyValueSetSymbol("RXF1_BYTES_CFG", canRXF1Menu)
    canRXF1elementSize.setLabel("RX FIFO 1 Element Size:")
    adornElementSize(canRXF1elementSize)

    canRXF1overwrite = mcanComponent.createBooleanSymbol("RXF1_OVERWRITE", canRXF1Menu)
    canRXF1overwrite.setLabel("Use RX FIFO 1 Overwrite Mode")
    canRXF1overwrite.setDescription("Overwrite RX FIFO 1 entries without blocking")
    canRXF1overwrite.setDefaultValue(True)

    canInterruptRX1NewEntry = mcanComponent.createBooleanSymbol("INT_RXF1_NEW_ENTRY", canRXF1Menu)
    canInterruptRX1NewEntry.setLabel("Use Interrupt for New Entry in RX1")
    canInterruptRX1NewEntry.setDefaultValue(False)

    canInterruptRX1Watermark = mcanComponent.createBooleanSymbol("INT_RXF1_WATERMARK", canRXF1Menu)
    canInterruptRX1Watermark.setLabel("Use Interrupt for RX FIFO 1 Watermark")
    canInterruptRX1Watermark.setDefaultValue(False)

    # ------  T X  --------------
    canTX = mcanComponent.createBooleanSymbol("TX_USE", canMenu)
    canTX.setLabel("Use TX FIFO")
    canTX.setDefaultValue(True)

    # make a menu separate for TX so it can be turned off and on at one point
    canTXmenu = mcanComponent.createMenuSymbol("mcantx", canTX)
    canTXmenu.setLabel("TX FIFO Settings")
    canTXmenu.setDependencies(hideMenu, ["TX_USE"])

    # number of TX FIFO elements
    canTXnumElements = mcanComponent.createIntegerSymbol("TX_FIFO_ELEMENTS", canTXmenu)
    canTXnumElements.setLabel("Number of TX FIFO Elements")
    canTXnumElements.setDefaultValue(1)
    canTXnumElements.setMin(1)
    canTXnumElements.setMax(32)

    canTXwatermarkP = mcanComponent.createIntegerSymbol("TX_FIFO_WP", canTXmenu)
    canTXwatermarkP.setLabel("TX FIFO Watermark %")
    canTXwatermarkP.setDefaultValue(0)
    canTXwatermarkP.setMin(0)
    canTXwatermarkP.setMax(99)
    
    #This is a computed value for watermark
    canTXwatermark = mcanComponent.createIntegerSymbol("TX_FIFO_WATERMARK", canTXmenu)
    canTXwatermark.setLabel("Watermark at element: ")
    canTXwatermark.setDescription("A value of 0 disables watermark")
    canTXwatermark.setDefaultValue(0)
    canTXwatermark.setReadOnly(True)
    canTXwatermark.setDependencies(TXWatermarkUpdate, ["TX_FIFO_ELEMENTS", "TX_FIFO_WP"])

    canTXElementCfg = mcanComponent.createKeyValueSetSymbol("TX_FIFO_BYTES_CFG", canTXmenu)
    canTXElementCfg.setLabel("TX Element Size:")
    adornElementSize(canTXElementCfg)

    canTXpause = mcanComponent.createBooleanSymbol("TX_PAUSE", canTXmenu)
    canTXpause.setLabel("Enable TX Pause")
    canTXpause.setDescription("Pause 2 CAN bit times between transmissions")
    canTXpause.setDefaultValue(False)

    canInterruptTXcompleted = mcanComponent.createBooleanSymbol("INT_TX_COMPLETED", canTXmenu)
    canInterruptTXcompleted.setLabel("Use Interrupt for TX Completed")
    canInterruptTXcompleted.setDefaultValue(False)

    canInterruptTXEmpty = mcanComponent.createBooleanSymbol("INT_TX_FIFO_EMPTY", canTXmenu)
    canInterruptTXEmpty.setLabel("Use Interrupt for TX FIFO Empty")
    canInterruptTXEmpty.setDefaultValue(False)

    canInterruptTXWatermark = mcanComponent.createBooleanSymbol("INT_TX_FIFO_WATERMARK", canTXmenu)
    canInterruptTXWatermark.setLabel("Use Interrupt for TX FIFO Watermark")
    canInterruptTXWatermark.setDefaultValue(False)

    # up to 128 standard filters
    canStdFilterMenu = mcanComponent.createMenuSymbol("stdFilterMenu", canMenu)
    canStdFilterMenu.setLabel("Standard Filters (up to 128)")
    canStdFilterMenu.setDependencies(adjustStdFilters, ["FILTERS_STD"])

    canStdFilterNumber = mcanComponent.createIntegerSymbol("FILTERS_STD", canStdFilterMenu)
    canStdFilterNumber.setLabel("Number of Standard Filters:")
    canStdFilterNumber.setDefaultValue(0)
    canStdFilterNumber.setMin(0)
    canStdFilterNumber.setMax(128)

    #Create all of the standard filters in a disabled state
    for filter in range (128):
        stdFilterList.append(canCreateStdFilter(mcanComponent, canStdFilterMenu, filter + 1))

    #What to do when a NO-MATCH is detected on a standard packet
    canNoMatchStandard = mcanComponent.createKeyValueSetSymbol("FILTERS_STD_NOMATCH", canMenu)
    canNoMatchStandard.setLabel("Standard message No-Match disposition:")
    canNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_0", "0", "Move to RX FIFO 0")
    canNoMatchStandard.addKey("MCAN_GFC_ANFS_RX_FIFO_1", "1", "Move to RX FIFO 1")
    canNoMatchStandard.addKey("MCAN_GFC_ANFS(2)",        "2", "Reject")
    canNoMatchStandard.setOutputMode("Key")
    canNoMatchStandard.setDisplayMode("Description")
    canNoMatchStandard.setDefaultValue(2)

    # Reject all standard IDs?
    canStdReject = mcanComponent.createBooleanSymbol("FILTERS_STD_REJECT", canMenu)
    canStdReject.setLabel("Reject all Standard Messages")
    canStdReject.setDescription("Reject all remote frames with 11-bit standard IDs")
    canStdReject.setDefaultValue(False)

    # 64 extended filters
    canExtFilterMenu = mcanComponent.createMenuSymbol("extFilterMenu", canMenu)
    canExtFilterMenu.setLabel("Extended Filters (up to 64)")
    canExtFilterMenu.setDependencies(adjustExtFilters, ["FILTERS_EXT"])

    #How many extended filters
    canExtFilterNumber = mcanComponent.createIntegerSymbol("FILTERS_EXT", canExtFilterMenu)
    canExtFilterNumber.setLabel("Number of Extended Filters:")
    canExtFilterNumber.setDefaultValue(0)
    canExtFilterNumber.setMin(0)
    canExtFilterNumber.setMax(64)

    #Create all of the 64 extended filters in a disabled state
    for filter in range (64):
        extFilterList.append(canCreateExtFilter(mcanComponent, canExtFilterMenu, filter + 1))

    # Reject all extended IDs?
    canExtReject = mcanComponent.createBooleanSymbol("FILTERS_EXT_REJECT", canMenu)
    canExtReject.setLabel("Reject all Extended Messages")
    canExtReject.setDescription("Reject all remote frames with 29-bit extended IDs")
    canExtReject.setDefaultValue(False)

    #What to do when a NO-MATCH is detected on an extended message
    canNoMatchExtended = mcanComponent.createKeyValueSetSymbol("FILTERS_EXT_NOMATCH", canMenu)
    canNoMatchExtended.setLabel("Extended message No-Match disposition:")
    canNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_0", "0", "Move to RX FIFO 0")
    canNoMatchExtended.addKey("MCAN_GFC_ANFE_RX_FIFO_1", "1", "Move to RX FIFO 1")
    canNoMatchExtended.addKey("MCAN_GFC_ANFE(2)",        "2", "Reject")
    canNoMatchExtended.setOutputMode("Key")
    canNoMatchExtended.setDisplayMode("Description")
    canNoMatchExtended.setDefaultValue(2)

    #use timeout?
    canUseTimeout = mcanComponent.createBooleanSymbol("CAN_TIMEOUT", canMenu)
    canUseTimeout.setLabel("Use Timeout Counter")
    canUseTimeout.setDescription("Enables Timeout Counter")
    canUseTimeout.setDefaultValue(True)

    #timout count
    canTimeoutCount = mcanComponent.createIntegerSymbol("TIMEOUT_COUNT", canUseTimeout)
    canTimeoutCount.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canTimeoutCount.setLabel("Timeout Countdown from: ")
    canTimeoutCount.setDefaultValue(40000)
    canTimeoutCount.setMin(10)
    canTimeoutCount.setMax(65535)

    #timeout mode
    canTimeoutMode = mcanComponent.createKeyValueSetSymbol("TIMEOUT_SELECT", canUseTimeout)
    canTimeoutMode.setLabel("Timeout mode:")
    canTimeoutMode.addKey("MCAN_TOCC_TOS_CONTINUOUS", "0", "CONTINUOUS")
    canTimeoutMode.addKey("MCAN_TOCC_TOS_TX_EV_TIMEOUT", "1", "TX EVENT")
    canTimeoutMode.addKey("MCAN_TOCC_TOS_RX0_EV_TIMEOUT", "2", "RX0 EVENT")
    canTimeoutMode.addKey("MCAN_TOCC_TOS_RX1_EV_TIMEOUT", "3", "RX1 EVENT")
    canTimeoutMode.setOutputMode("Key")
    canTimeoutMode.setDisplayMode("Description")
    canTimeoutMode.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canTimeoutMode.setDefaultValue(1)

    #timeout interrupt
    canInterruptTimeout = mcanComponent.createBooleanSymbol("INT_TIMEOUT", canUseTimeout)
    canInterruptTimeout.setLabel("Use Interrupt for Timeout")
    canInterruptTimeout.setDependencies(hideMenu, ["CAN_TIMEOUT"])
    canInterruptTimeout.setDefaultValue(False)

    #timestamp Modes
    canTimestampMode = mcanComponent.createKeyValueSetSymbol("TIMESTAMP_MODE", canMenu)
    canTimestampMode.setLabel("Timestamp mode")
    canTimestampMode.setDescription("EXT INC: external counter (needed for FD). ZERO: timestamp is always 0x0000. TCP INC: incremented according to TCP.")
    canTimestampMode.addKey("MCAN_TSCC_TSS_ALWAYS_0", "0", "ZERO")
    canTimestampMode.addKey("MCAN_TSCC_TSS_TCP_INC", "1", "TCP INC")
    canTimestampMode.addKey("MCAN_TSCC_TSS_EXT_TIMESTAMP", "2", "EXT INC")
    canTimestampMode.setOutputMode("Key")
    canTimestampMode.setDisplayMode("Description")
    canTimestampMode.setDefaultValue(1)

    #timestamp/timeout Counter Prescaler
    canTCP = mcanComponent.createIntegerSymbol("TIMESTAMP_PRESCALER", canMenu)
    canTCP.setLabel("Timestamp/Timeout Counter Prescaler (TCP):")
    canTCP.setDescription("Configures Timestamp & Timeout counter prescaler in multiples of CAN bit times.")
    canTCP.setDefaultValue(1)
    canTCP.setMin(1)
    canTCP.setMax(16)

    # Initialize peripheral clock
    Database.clearSymbolValue("core", "PMC_ID_MCAN" + str(num))
    Database.setSymbolValue("core", "PMC_ID_MCAN" + str(num), True, 1)
    
    # get peripheral id for MCAN
    peripId = Interrupt.getInterruptIndex("MCAN" + str(num))
    
    # Initialize peripheral Interrupt
    Database.clearSymbolValue("core", "NVIC_" + str(peripId) + "_ENABLE")
    Database.setSymbolValue("core", "NVIC_" + str(peripId) + "_ENABLE", True, 1)
    
    # Set Interrupt Handler Name
    Database.clearSymbolValue("core", "NVIC_" + str(peripId) + "_HANDLER")
    Database.setSymbolValue("core", "NVIC_" + str(peripId) + "_HANDLER", "MCAN" + str(num) + "_InterruptHandler", 1)
    
    REG_MODULE_MCAN = Register.getRegisterModule("MCAN")
    configName = Variables.get("__CONFIGURATION_NAME")
    
    #Master Header
    canMasterHeaderFile = mcanComponent.createFileSymbol("headerFile", None)
    canMasterHeaderFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/drv_can_local.h")
    canMasterHeaderFile.setOutputName("drv_can_local.h")
    canMasterHeaderFile.setDestPath("/peripheral/mcan/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = mcanComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/drv_can.c.ftl")
    canMainSourceFile.setOutputName("drv_can" + str(num) + ".c")
    canMainSourceFile.setDestPath("/peripheral/mcan/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)
    
    #Instance Header File
    canInstHeaderFile = mcanComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/drv_can.h.ftl")
    canInstHeaderFile.setOutputName("drv_can" + str(num) + ".h")
    canInstHeaderFile.setDestPath("/peripheral/mcan/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcan/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)
    
    #CAN Initialize
    canSystemInitFile = mcanComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
    canSystemInitFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/system_initialize.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = mcanComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/mcan_" + REG_MODULE_MCAN.getID() + "/templates/system/system_definitions.h.ftl")
    canSystemDefFile.setMarkup(True)


def getMasterClockFreq():
    return int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))

'''********************************End of the file*************************'''