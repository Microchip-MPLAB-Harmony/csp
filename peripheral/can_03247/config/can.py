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
fifoList = []
filterList = []
AcceptanceMaskList = []

################################################################################
#### Business Logic ####
################################################################################
# if operation mode is changed to Normal CAN 2.0 mode then don't show symbol
def showWhenFD(symbol, event):
    if event["value"] == 0x6:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    return regName

def getIRQnumber(string):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

    for param in interruptsChildren:
        name = param.getAttribute("name")
        if string == name:
            irq_index = param.getAttribute("index")
            break
        elif string == name.replace('_',''):
            irq_index = param.getAttribute("irq-index")
            break

    return irq_index

def canCreateFilter(component, menu, filterNumber):
    filterMenu = component.createMenuSymbol(canInstanceName.getValue() + "_FILTER"+ str(filterNumber), menu)
    filterMenu.setLabel("Filter " + str(filterNumber))

    filterEnable = component.createBooleanSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ENABLE", filterMenu)
    filterEnable.setLabel("Filter Enable")
    filterEnable.setDefaultValue(True if filterNumber < 1 else False)

    id = component.createIntegerSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ID", filterMenu)
    id.setLabel("Filter ID")
    id.setMin(0)
    id.setMax(536870911)

    maskId = component.createIntegerSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_MASK_ID", filterMenu)
    maskId.setLabel("Mask ID")
    maskId.setMin(0)
    maskId.setMax(536870911)

    fifoSelect = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_FIFO_SELECT", filterMenu)
    fifoSelect.setLabel("Select FIFO")
    fifoSelect_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "FLTCON" + str(filterNumber / 4) + "__F" + str(filterNumber) + "BP" + "\"]")
    fifoSelect_Values = []
    fifoSelect_Values = fifoSelect_Node.getChildren()
    fifoSelect_Values = list(reversed(fifoSelect_Values))
    for index in range(len(fifoSelect_Values)):
        fifoSelect_Key_Value = fifoSelect_Values[index].getAttribute("value")
        fifoSelect_Key_Description = fifoSelect_Values[index].getAttribute("caption")
        fifoSelect.addKey(fifoSelect_Key_Description, fifoSelect_Key_Value, fifoSelect_Key_Description)
    fifoSelect.setDisplayMode("Key")
    fifoSelect.setOutputMode("Value")
    fifoSelect.setDefaultValue(2)

    if (filterNumber >= Database.getSymbolValue(canInstanceName.getValue().lower(), "NUMBER_OF_FILTER")):
        filterMenu.setVisible(False)
        filterMenu.setEnabled(False)
    return filterMenu

def canCreateFifoConfig(component, menu, fifoNumber):
    fifoMenu = component.createMenuSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber), menu)
    fifoMenu.setLabel("FIFO " + str(fifoNumber))

    fifoSize = component.createIntegerSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_SIZE", fifoMenu)
    fifoSize.setLabel("Number of Message Buffer")
    fifoSize.setDescription("Total number of message buffers in FIFO " + str(fifoNumber))
    fifoSize.setDefaultValue(1)
    fifoSize.setMin(1)
    fifoSize.setMax(32)

    fifoTxEnable = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXEN", fifoMenu)
    fifoTxEnable.setLabel("Select Trasmit/Receive FIFO")
    fifoTxEnable.addKey("RECEIVE_FIFO", "0x0", "FIFO is a Receive FIFO")
    fifoTxEnable.addKey("TRASMIT_FIFO", "0x1", "FIFO is a Transmit FIFO")
    fifoTxEnable.setOutputMode("Value")
    fifoTxEnable.setDisplayMode("Description")
    fifoTxEnable.setDefaultValue(0x1 if fifoNumber < 2 else 0x0)

    fifoPayloadSize = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_PAYLOAD_SIZE", fifoMenu)
    fifoPayloadSize.setLabel("Payload Size")
    fifoPayloadSize_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "FIFOCON" + str(fifoNumber) + "__PLSIZE" + "\"]")
    fifoPayloadSize_Values = []
    fifoPayloadSize_Values = fifoPayloadSize_Node.getChildren()
    for index in range(len(fifoPayloadSize_Values)):
        fifoPayloadSize_Key_Value = fifoPayloadSize_Values[index].getAttribute("value")
        fifoPayloadSize_Key_Description = fifoPayloadSize_Values[index].getAttribute("caption")
        fifoPayloadSize.addKey(fifoPayloadSize_Key_Description, fifoPayloadSize_Key_Value, fifoPayloadSize_Key_Description)
    fifoPayloadSize.setDisplayMode("Description")
    fifoPayloadSize.setOutputMode("Value")
    fifoPayloadSize.setDefaultValue(0)

    fifoMsgPriority = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_MESSAGE_PRIORITY", fifoMenu)
    fifoMsgPriority.setLabel("Transmit Message Priority")
    fifoMsgPriority_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "FIFOCON" + str(fifoNumber) + "__TXPRI" + "\"]")
    fifoMsgPriority_Values = []
    fifoMsgPriority_Values = fifoMsgPriority_Node.getChildren()
    fifoMsgPriority_Values = list(reversed(fifoMsgPriority_Values))
    for index in range(len(fifoMsgPriority_Values)):
        fifoMsgPriority_Key_Value = fifoMsgPriority_Values[index].getAttribute("value")
        fifoMsgPriority_Key_Description = fifoMsgPriority_Values[index].getAttribute("caption")
        fifoMsgPriority.addKey(fifoMsgPriority_Key_Description, fifoMsgPriority_Key_Value, fifoMsgPriority_Key_Description)
    fifoMsgPriority.setDisplayMode("Description")
    fifoMsgPriority.setOutputMode("Value")
    fifoMsgPriority.setDefaultValue(0)
    fifoMsgPriority.setVisible(True if fifoNumber < 2 else False)
    fifoMsgPriority.setDependencies(hideMenu, [canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXEN"])

    if (fifoNumber > Database.getSymbolValue(canInstanceName.getValue().lower(), "NUMBER_OF_FIFO")):
        fifoMenu.setVisible(False)
        fifoMenu.setEnabled(False)
    return fifoMenu

# adjust how many FIFOs are shown based on number entered
def adjustFIFOs(symbol, event):
    for fifo in fifoList[:event["value"]]:
        if fifo.getVisible() != True:
            fifo.setVisible(True)
            fifo.setEnabled(True)
    for fifo in fifoList[event["value"]:]:
        if fifo.getVisible() != False:
            fifo.setVisible(False)
            fifo.setEnabled(False)

# adjust how many filters are shown based on number entered
def adjustFilters(symbol, event):
    for fltr in filterList[:event["value"]]:
        if fltr.getVisible() != True:
            fltr.setVisible(True)
            fltr.setEnabled(True)
    for fltr in filterList[event["value"]:]:
        if fltr.getVisible() != False:
            fltr.setVisible(False)
            fltr.setEnabled(False)

def canInterruptSet(symbol, event):
    Database.setSymbolValue("core", canInterruptVector, event["value"])
    Database.setSymbolValue("core", canInterruptHandlerLock, event["value"])
    interruptName = canInterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if event["value"] == True:
        Database.setSymbolValue("core", canInterruptHandler, interruptName + "_InterruptHandler")
    else:
        Database.setSymbolValue("core", canInterruptHandler, interruptName + "_Handler")

def updateCanInterruptData(symbol, event):
    component = symbol.getComponent()
    canInterruptVectorUpdate = canInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    if canInterruptMode.getValue() == True and Database.getSymbolValue("core", canInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def canCoreClockFreq(symbol, event):
    symbol.setValue(int(Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")))

def bitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")

    if (bitTiming == "Data"):
        prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "DBT_BRP")
        bitrate = Database.getSymbolValue(canInstanceName.getValue().lower(), "DATA_BITRATE")
        samplePoint = Database.getSymbolValue(canInstanceName.getValue().lower(), "DATA_SAMPLE_POINT")
    else:
        prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "NBT_BRP")
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
    if (Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_OPMODE") == 0x0):
        tseg1, tseg2 = bitTimingCalculation("Data", 3, 49)
        Database.setSymbolValue(canInstanceName.getValue().lower(), "DBT_TSEG1", tseg1)
        Database.setSymbolValue(canInstanceName.getValue().lower(), "DBT_TSEG2", tseg2)
        component = symbol.getComponent()
        if (tseg2 > component.getSymbolByID("DBT_SJW").getMax()):
            sjw = component.getSymbolByID("DBT_SJW").getMax()
        else:
            sjw = tseg2
        Database.setSymbolValue(canInstanceName.getValue().lower(), "DBT_SJW", sjw)

def nominalBitTimingCalculation(symbol, event):
    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "NBT_TSEG1", tseg1)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "NBT_TSEG2", tseg2)
    component = symbol.getComponent()
    if (tseg2 > component.getSymbolByID("NBT_SJW").getMax()):
        sjw = component.getSymbolByID("NBT_SJW").getMax()
    else:
        sjw = tseg2
    Database.setSymbolValue(canInstanceName.getValue().lower(), "NBT_SJW", sjw)

def hideMenu(menu, event):
    menu.setVisible(event["value"])

def UpdateTimestampTSRESVisibility(symbol, event):
    canOpmode = Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_OPMODE")
    canTimestampEnable = Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_TIMESTAMP_ENABLE")
    canTimestampEOF = Database.getSymbolValue(canInstanceName.getValue().lower(), "CAN_TIMESTAMP_EOF")
    if (canOpmode != 0x6) and (canTimestampEnable == True) and (canTimestampEOF == 0x0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def instantiateComponent(canComponent):
    global canInstanceName
    global canInstanceNum
    global canInterruptVector
    global canInterruptHandler
    global canInterruptHandlerLock
    global canInterruptVectorUpdate
    global canCoreClockInvalidSym
    global canTimeQuantaInvalidSym
    global canInterruptMode

    canInstanceName = canComponent.createStringSymbol("CAN_INSTANCE_NAME", None)
    canInstanceName.setVisible(False)
    canInstanceName.setDefaultValue(canComponent.getID().upper())
    print("Running " + canInstanceName.getValue())

    canInstanceNum = canComponent.createStringSymbol("CAN_INSTANCE_NUM", None)
    canInstanceNum.setVisible(False)
    canInstanceNum.setDefaultValue(filter(str.isdigit,str(canComponent.getID())))

    # Initialize peripheral clock
    Database.setSymbolValue("core", canInstanceName.getValue()+"_CLOCK_ENABLE", True)

    canOpMode = canComponent.createKeyValueSetSymbol("CAN_OPMODE", None)
    canOpMode.setLabel("CAN Operation Mode")
    canOpMode_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "CON__REQOP\"]")
    canOpMode_Values = []
    canOpMode_Values = canOpMode_Node.getChildren()
    canOpMode_Values = list(reversed(canOpMode_Values))
    for index in range(len(canOpMode_Values)):
        canOpMode_Key_Value = canOpMode_Values[index].getAttribute("value")
        canOpMode_Key_Description = canOpMode_Values[index].getAttribute("caption")
        if "Reserved" in canOpMode_Key_Description:
            continue
        canOpMode.addKey(canOpMode_Key_Description, canOpMode_Key_Value, canOpMode_Key_Description)
    canOpMode.setOutputMode("Value")
    canOpMode.setDisplayMode("Description")
    canOpMode.setDefaultValue(0)

    canInterruptMode = canComponent.createBooleanSymbol("CAN_INTERRUPT_MODE", None)
    canInterruptMode.setLabel("Interrupt Mode")
    canInterruptMode.setDefaultValue(False)

    canInterruptVector = canInstanceName.getValue() + "_INTERRUPT_ENABLE"
    canInterruptHandler = canInstanceName.getValue() + "_INTERRUPT_HANDLER"
    canInterruptHandlerLock = canInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    canInterruptVectorUpdate = canInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # CAN Bit Timing Calculation
    canBitTimingCalculationMenu = canComponent.createMenuSymbol("BIT_TIMING_CALCULATION", None)
    canBitTimingCalculationMenu.setLabel("Bit Timing Calculation")
    canBitTimingCalculationMenu.setDescription("CAN Bit Timing Calculation for Normal Operation")

    canSelectClockSource = canComponent.createKeyValueSetSymbol("CAN_CORE_SELECT_CLOCK_SOURCE", canBitTimingCalculationMenu)
    canSelectClockSource.setLabel("Select Clock Source")
    canSelectClockSource_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "CON__CLKSEL0" + "\"]")
    canSelectClockSource_Values = []
    canSelectClockSource_Values = canSelectClockSource_Node.getChildren()
    canSelectClockSource_Values = list(reversed(canSelectClockSource_Values))
    for index in range(len(canSelectClockSource_Values)):
        canSelectClockSource_Key_Value = canSelectClockSource_Values[index].getAttribute("value")
        canSelectClockSource_Key_Description = canSelectClockSource_Values[index].getAttribute("caption")
        canSelectClockSource.addKey(canSelectClockSource_Key_Description, canSelectClockSource_Key_Value, canSelectClockSource_Key_Description)
    canSelectClockSource.setDisplayMode("Description")
    canSelectClockSource.setOutputMode("Value")
    canSelectClockSource.setDefaultValue(0)

    canCoreClockValue = canComponent.createIntegerSymbol("CAN_CORE_CLOCK_FREQ", canBitTimingCalculationMenu)
    canCoreClockValue.setLabel("Clock Frequency")
    canCoreClockValue.setReadOnly(True)
    canCoreClockValue.setDefaultValue(int(Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    canCoreClockValue.setVisible(True)
    canCoreClockValue.setDependencies(canCoreClockFreq, ["CAN_CORE_SELECT_CLOCK_SOURCE", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canCoreClockInvalidSym = canComponent.createCommentSymbol("CAN_CORE_CLOCK_INVALID_COMMENT", None)
    canCoreClockInvalidSym.setLabel("Warning!!! " + canInstanceName.getValue() + " Clock Frequency is too low for required Nominal Bit Timing")
    canCoreClockInvalidSym.setVisible((canCoreClockValue.getValue() == 0))

    canTimeQuantaInvalidSym = canComponent.createCommentSymbol("CAN_TIME_QUANTA_INVALID_COMMENT", None)
    canTimeQuantaInvalidSym.setLabel("Warning!!! Number of Time Quanta is too low for required Nominal Bit Timing")
    canTimeQuantaInvalidSym.setVisible(False)

    # CAN Nominal Bit Timing Calculation
    canNominalBitTimingMenu = canComponent.createMenuSymbol("NOMINAL_BIT_TIMING_CALCULATION", canBitTimingCalculationMenu)
    canNominalBitTimingMenu.setLabel("Nominal Bit Timing")
    canNominalBitTimingMenu.setDescription("Nominal Bit Timing for CAN Message Frame")

    canNominalBitrate = canComponent.createIntegerSymbol("NOMINAL_BITRATE", canNominalBitTimingMenu)
    canNominalBitrate.setLabel("Bit Rate (Kbps)")
    canNominalBitrate.setMin(1)
    canNominalBitrate.setMax(1000)
    canNominalBitrate.setDefaultValue(500)
    canNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "CAN_CORE_CLOCK_FREQ", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canNominalSamplePoint = canComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", canNominalBitTimingMenu)
    canNominalSamplePoint.setLabel("Sample Point %")
    canNominalSamplePoint.setMin(50.0)
    canNominalSamplePoint.setMax(100.0)
    canNominalSamplePoint.setDefaultValue(75.0)
    canNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])

    canNominalBrp = canComponent.createIntegerSymbol("NBT_BRP", canNominalBitTimingMenu)
    canNominalBrp.setLabel("Baudrate Prescaler")
    canNominalBrp.setMin(0)
    canNominalBrp.setMax(255)
    canNominalBrp.setDefaultValue(14)
    canNominalBrp.setDependencies(nominalBitTimingCalculation, ["NBT_BRP"])

    tseg1, tseg2 = bitTimingCalculation("Nominal", 4, 385)

    canNominalTseg1 = canComponent.createIntegerSymbol("NBT_TSEG1", canNominalBitTimingMenu)
    canNominalTseg1.setLabel("Phase 1 Segment")
    canNominalTseg1.setMin(1)
    canNominalTseg1.setMax(255)
    canNominalTseg1.setDefaultValue(tseg1)
    canNominalTseg1.setReadOnly(True)

    canNominalTseg2 = canComponent.createIntegerSymbol("NBT_TSEG2", canNominalBitTimingMenu)
    canNominalTseg2.setLabel("Phase 2 Segment")
    canNominalTseg2.setMin(0)
    canNominalTseg2.setMax(127)
    canNominalTseg2.setDefaultValue(tseg2)
    canNominalTseg2.setReadOnly(True)

    canNominalSyncJumpWidth = canComponent.createIntegerSymbol("NBT_SJW", canNominalBitTimingMenu)
    canNominalSyncJumpWidth.setLabel("Synchronization Jump Width")
    canNominalSyncJumpWidth.setMin(0)
    canNominalSyncJumpWidth.setMax(127)
    canNominalSyncJumpWidth.setDefaultValue(canNominalTseg2.getValue())

    # CAN Data Bit Timing Calculation
    canDataBitTimingMenu = canComponent.createMenuSymbol("DATA_BIT_TIMING_CALCULATION", canBitTimingCalculationMenu)
    canDataBitTimingMenu.setLabel("Data Bit Timing")
    canDataBitTimingMenu.setDescription("This timing must be greater or equal to the Nominal Bit Timing")
    canDataBitTimingMenu.setDependencies(showWhenFD, ["CAN_OPMODE"])

    canDataBitrate = canComponent.createIntegerSymbol("DATA_BITRATE", canDataBitTimingMenu)
    canDataBitrate.setLabel("Bit Rate (Kbps)")
    canDataBitrate.setMin(1)
    canDataBitrate.setMax(8000)
    canDataBitrate.setDefaultValue(500)
    canDataBitrate.setDependencies(dataBitTimingCalculation, ["DATA_BITRATE", "CAN_OPMODE", "CAN_CORE_CLOCK_FREQ", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canDataSamplePoint = canComponent.createFloatSymbol("DATA_SAMPLE_POINT", canDataBitTimingMenu)
    canDataSamplePoint.setLabel("Sample Point %")
    canDataSamplePoint.setMin(50.0)
    canDataSamplePoint.setMax(100.0)
    canDataSamplePoint.setDefaultValue(75.0)
    canDataSamplePoint.setDependencies(dataBitTimingCalculation, ["DATA_SAMPLE_POINT"])

    canDataBrp = canComponent.createIntegerSymbol("DBT_BRP", canDataBitTimingMenu)
    canDataBrp.setLabel("Baudrate Prescaler")
    canDataBrp.setMin(0)
    canDataBrp.setMax(255)
    canDataBrp.setDefaultValue(14)
    canDataBrp.setDependencies(dataBitTimingCalculation, ["DBT_BRP"])

    tseg1, tseg2 = bitTimingCalculation("Data", 3, 49)

    canDataTseg1 = canComponent.createIntegerSymbol("DBT_TSEG1", canDataBitTimingMenu)
    canDataTseg1.setLabel("Time Segment Before Sample Point")
    canDataTseg1.setMin(0)
    canDataTseg1.setMax(31)
    canDataTseg1.setDefaultValue(tseg1)
    canDataTseg1.setReadOnly(True)

    canDataTseg2 = canComponent.createIntegerSymbol("DBT_TSEG2", canDataBitTimingMenu)
    canDataTseg2.setLabel("Time Segment After Sample Point")
    canDataTseg2.setMin(0)
    canDataTseg2.setDefaultValue(tseg2)
    canDataTseg2.setMax(15)
    canDataTseg2.setReadOnly(True)

    canDataSyncJumpWidth = canComponent.createIntegerSymbol("DBT_SJW", canDataBitTimingMenu)
    canDataSyncJumpWidth.setLabel("Synchronization Jump Width")
    canDataSyncJumpWidth.setMin(0)
    canDataSyncJumpWidth.setDefaultValue(canDataTseg2.getValue())
    canDataSyncJumpWidth.setMax(15)

    # CAN Tx Event FIFO configuration
    canTxEventFIFO = canComponent.createBooleanSymbol("TX_EVENT_FIFO_USE", None)
    canTxEventFIFO.setLabel("Use Tx Event FIFO")
    canTxEventFIFO.setDefaultValue(True)

    canTxEventFIFOMsgBuffer = canComponent.createIntegerSymbol("TX_EVENT_FIFO_MESSAGE_BUFFER", canTxEventFIFO)
    canTxEventFIFOMsgBuffer.setLabel("Number of Message Buffer")
    canTxEventFIFOMsgBuffer.setDescription("Total number of message buffers in Tx Event FIFO")
    canTxEventFIFOMsgBuffer.setDefaultValue(1)
    canTxEventFIFOMsgBuffer.setMin(1)
    canTxEventFIFOMsgBuffer.setMax(32)
    canTxEventFIFOMsgBuffer.setDependencies(hideMenu, ["TX_EVENT_FIFO_USE"])

    # CAN Message Tx Queue configuration
    canTxQueue = canComponent.createBooleanSymbol("TX_QUEUE_USE", None)
    canTxQueue.setLabel("Use Tx Queue")
    canTxQueue.setDefaultValue(True)

    canTxQueueMsgBuffer = canComponent.createIntegerSymbol("TX_QUEUE_MESSAGE_BUFFER", canTxQueue)
    canTxQueueMsgBuffer.setLabel("Number of Message Buffer")
    canTxQueueMsgBuffer.setDescription("Total number of message buffers in Tx Queue")
    canTxQueueMsgBuffer.setDefaultValue(1)
    canTxQueueMsgBuffer.setMin(1)
    canTxQueueMsgBuffer.setMax(32)
    canTxQueueMsgBuffer.setDependencies(hideMenu, ["TX_QUEUE_USE"])

    canTxQueuePayloadSize = canComponent.createKeyValueSetSymbol("TX_QUEUE_PAYLOAD_SIZE", canTxQueue)
    canTxQueuePayloadSize.setLabel("Payload Size")
    canTxQueuePayloadSize_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "TXQCON__PLSIZE" + "\"]")
    canTxQueuePayloadSize_Values = []
    canTxQueuePayloadSize_Values = canTxQueuePayloadSize_Node.getChildren()
    for index in range(len(canTxQueuePayloadSize_Values)):
        canTxQueuePayloadSize_Key_Value = canTxQueuePayloadSize_Values[index].getAttribute("value")
        canTxQueuePayloadSize_Key_Description = canTxQueuePayloadSize_Values[index].getAttribute("caption")
        canTxQueuePayloadSize.addKey(canTxQueuePayloadSize_Key_Description, canTxQueuePayloadSize_Key_Value, canTxQueuePayloadSize_Key_Description)
    canTxQueuePayloadSize.setDisplayMode("Description")
    canTxQueuePayloadSize.setOutputMode("Value")
    canTxQueuePayloadSize.setDefaultValue(0)
    canTxQueuePayloadSize.setDependencies(hideMenu, ["TX_QUEUE_USE"])

    canTxQueueMsgPriority = canComponent.createKeyValueSetSymbol("TX_QUEUE_MESSAGE_PRIORITY", canTxQueue)
    canTxQueueMsgPriority.setLabel("Tx Queue Message Priority")
    canTxQueueMsgPriority_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "TXQCON__TXPRI" + "\"]")
    canTxQueueMsgPriority_Values = []
    canTxQueueMsgPriority_Values = canTxQueueMsgPriority_Node.getChildren()
    canTxQueueMsgPriority_Values = list(reversed(canTxQueueMsgPriority_Values))
    for index in range(len(canTxQueueMsgPriority_Values)):
        canTxQueueMsgPriority_Key_Value = canTxQueueMsgPriority_Values[index].getAttribute("value")
        canTxQueueMsgPriority_Key_Description = canTxQueueMsgPriority_Values[index].getAttribute("caption")
        canTxQueueMsgPriority.addKey(canTxQueueMsgPriority_Key_Description, canTxQueueMsgPriority_Key_Value, canTxQueueMsgPriority_Key_Description)
    canTxQueueMsgPriority.setDisplayMode("Description")
    canTxQueueMsgPriority.setOutputMode("Value")
    canTxQueueMsgPriority.setDefaultValue(0)
    canTxQueueMsgPriority.setDependencies(hideMenu, ["TX_QUEUE_USE"])

    # CAN Message FIFO configuration
    canFifoConfMenu = canComponent.createMenuSymbol("FIFO_CONF_MENU", None)
    canFifoConfMenu.setLabel("FIFO Configuration")
    canFifoConfMenu.setDependencies(adjustFIFOs, ["NUMBER_OF_FIFO"])

    # Number of FIFOs
    canFifoNumber = canComponent.createIntegerSymbol("NUMBER_OF_FIFO", canFifoConfMenu)
    canFifoNumber.setLabel("Number of FIFOs")
    canFifoNumber.setDefaultValue(2)
    canFifoNumber.setMin(1)
    canRegs_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/register-group@[name=\"CAN\"]")
    canRegs_Values = []
    canRegs_Values = canRegs_Node.getChildren()
    maxFifoNum = 0
    canFifoControlReg = "CFD" + canInstanceNum.getValue() + "FIFOCON"
    for index in range(len(canRegs_Values)):
        if canFifoControlReg in canRegs_Values[index].getAttribute("name"):
            maxFifoNum += 1
    canFifoNumber.setMax(maxFifoNum)

    # Create all FIFOs in a disabled state
    for fifo in range (canFifoNumber.getMax()):
        fifoList.append(canCreateFifoConfig(canComponent, canFifoConfMenu, (fifo + 1)))

    # CAN Filter Configuration
    canFilterMenu = canComponent.createMenuSymbol("FilterMenu", None)
    canFilterMenu.setLabel("Filter Configuration")
    canFilterMenu.setDependencies(adjustFilters, ["NUMBER_OF_FILTER"])

    # Number of Filters
    canFilterNumber = canComponent.createIntegerSymbol("NUMBER_OF_FILTER", canFilterMenu)
    canFilterNumber.setLabel("Number of Filters")
    canFilterNumber.setDefaultValue(1)
    canFilterNumber.setMin(1)
    maxFilterNum = 0
    canFilterReg = "CFD" + canInstanceNum.getValue() + "FLTOBJ"
    for index in range(len(canRegs_Values)):
        if canFilterReg in canRegs_Values[index].getAttribute("name"):
            maxFilterNum += 1
    canFilterNumber.setMax(maxFilterNum)

    #Create all filters in a disabled state
    for fltr in range (canFilterNumber.getMax()):
        filterList.append(canCreateFilter(canComponent, canFilterMenu, fltr))

    canTimestampEnable = canComponent.createBooleanSymbol("CAN_TIMESTAMP_ENABLE", None)
    canTimestampEnable.setLabel("Timestamp Enable")
    canTimestampEnable.setDefaultValue(False)

    canTimestampPrescaler = canComponent.createIntegerSymbol("CAN_TIMESTAMP_PRESCALER", canTimestampEnable)
    canTimestampPrescaler.setLabel("Time Base Counter Prescaler")
    canTimestampPrescaler.setDefaultValue(0)
    canTimestampPrescaler.setMin(0)
    canTimestampPrescaler.setMax(1023)
    canTimestampPrescaler.setVisible(False)
    canTimestampPrescaler.setDependencies(hideMenu, ["CAN_TIMESTAMP_ENABLE"])

    canTimestampEOF = canComponent.createKeyValueSetSymbol("CAN_TIMESTAMP_EOF", canTimestampEnable)
    canTimestampEOF.setLabel("Timestamp SOF/EOF")
    canTimestampEOF.setDescription("Time Stamp at Start of Frame or End of Frame")
    canTimestampEOF_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "TSCON__TSEOF" + "\"]")
    canTimestampEOF_Values = []
    canTimestampEOF_Values = canTimestampEOF_Node.getChildren()
    canTimestampEOF_Values = list(reversed(canTimestampEOF_Values))
    for index in range(len(canTimestampEOF_Values)):
        canTimestampEOF_Key_Value = canTimestampEOF_Values[index].getAttribute("value")
        canTimestampEOF_Key_Description = canTimestampEOF_Values[index].getAttribute("caption")
        canTimestampEOF.addKey(canTimestampEOF_Key_Description, canTimestampEOF_Key_Value, canTimestampEOF_Key_Description)
    canTimestampEOF.setDisplayMode("Description")
    canTimestampEOF.setOutputMode("Value")
    canTimestampEOF.setDefaultValue(0)
    canTimestampEOF.setVisible(False)
    canTimestampEOF.setDependencies(hideMenu, ["CAN_TIMESTAMP_ENABLE"])

    canTimestampTSRES = canComponent.createKeyValueSetSymbol("CAN_TIMESTAMP_TSRES", canTimestampEOF)
    canTimestampTSRES.setLabel("Time Stamp Resolution(TSRES)")
    canTimestampTSRES.setDescription("Time Stamp Resolution bit for FD Frame only")
    canTimestampTSRES_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CFD" + canInstanceNum.getValue() + "TSCON__TSRES" + "\"]")
    canTimestampTSRES_Values = []
    canTimestampTSRES_Values = canTimestampTSRES_Node.getChildren()
    canTimestampTSRES_Values = list(reversed(canTimestampTSRES_Values))
    for index in range(len(canTimestampTSRES_Values)):
        canTimestampTSRES_Key_Value = canTimestampTSRES_Values[index].getAttribute("value")
        canTimestampTSRES_Key_Description = canTimestampTSRES_Values[index].getAttribute("caption")
        canTimestampTSRES.addKey(canTimestampTSRES_Key_Description, canTimestampTSRES_Key_Value, canTimestampTSRES_Key_Description)
    canTimestampTSRES.setDisplayMode("Description")
    canTimestampTSRES.setOutputMode("Value")
    canTimestampTSRES.setDefaultValue(0)
    canTimestampTSRES.setVisible(False)
    canTimestampTSRES.setDependencies(UpdateTimestampTSRESVisibility, ["CAN_TIMESTAMP_ENABLE", "CAN_TIMESTAMP_EOF", "CAN_OPMODE"])

    # Interrupt Dynamic settings
    caninterruptEnable = canComponent.createBooleanSymbol("CAN_INTERRUPT_ENABLE", None)
    caninterruptEnable.setVisible(False)
    caninterruptEnable.setDependencies(canInterruptSet, ["CAN_INTERRUPT_MODE"])

    canIrq_index = int(getIRQnumber(canInstanceName.getValue()))
    enblRegName = _get_enblReg_parms(canIrq_index)
    statRegName = _get_statReg_parms(canIrq_index)

    #IEC REG
    canIEC = canComponent.createStringSymbol("CAN_IEC_REG", None)
    canIEC.setDefaultValue(enblRegName)
    canIEC.setVisible(False)

    #IFS REG
    canIFS = canComponent.createStringSymbol("CAN_IFS_REG", None)
    canIFS.setDefaultValue(statRegName)
    canIFS.setVisible(False)

    # Dependency Status for interrupt
    canIntEnComment = canComponent.createCommentSymbol("CAN_INTERRUPT_ENABLE_COMMENT", None)
    canIntEnComment.setVisible(False)
    canIntEnComment.setLabel("Warning!!! " + canInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    canIntEnComment.setDependencies(updateCanInterruptData, ["core." + canInterruptVectorUpdate])

    REG_MODULE_CAN = Register.getRegisterModule("CAN")
    configName = Variables.get("__CONFIGURATION_NAME")

    #Master Header
    canMasterHeaderFile = canComponent.createFileSymbol("headerFile", None)
    canMasterHeaderFile.setSourcePath("../peripheral/can_03247/templates/plib_can_common.h")
    canMasterHeaderFile.setOutputName("plib_can_common.h")
    canMasterHeaderFile.setDestPath("/peripheral/can/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = canComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/can_03247/templates/plib_can.c.ftl")
    canMainSourceFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".c")
    canMainSourceFile.setDestPath("/peripheral/can/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)

    #Instance Header File
    canInstHeaderFile = canComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/can_03247/templates/plib_can.h.ftl")
    canInstHeaderFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".h")
    canInstHeaderFile.setDestPath("/peripheral/can/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)

    #CAN Initialize
    canSystemInitFile = canComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    canSystemInitFile.setSourcePath("../peripheral/can_03247/templates/system/initialization.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = canComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/can_03247/templates/system/definitions.h.ftl")
    canSystemDefFile.setMarkup(True)
