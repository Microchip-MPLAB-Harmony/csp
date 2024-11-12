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
    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("irq-name"))
            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):
    vector_index = "-1"
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

def symbolSetValue(symbol, event):
    symbol.setValue(event["value"])

def canCreateFilter(component, menu, filterNumber):
    filterMenu = component.createMenuSymbol(canInstanceName.getValue() + "_FILTER"+ str(filterNumber), menu)
    filterMenu.setLabel("Filter " + str(filterNumber))

    filterEnable = component.createBooleanSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ENABLE", filterMenu)
    filterEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFLTCON0")
    filterEnable.setLabel("Filter Enable")
    filterEnable.setDefaultValue(True if filterNumber < 1 else False)

    id = component.createHexSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ID", filterMenu)
    id.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFLTCON0")
    id.setLabel("ID")
    id.setMin(0)
    id.setMax(0x1FFFFFFF)

    idDecimal = component.createIntegerSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ID_DECIMAL", filterMenu)
    idDecimal.setVisible(False)
    idDecimal.setMin(0)
    idDecimal.setMax(536870911)
    idDecimal.setDependencies(symbolSetValue, [canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_ID"])

    fifoSelect = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_FIFO_SELECT", filterMenu)
    fifoSelect.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOBA")
    fifoSelect.setLabel("Select FIFO")
    fifoSelect_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"C" + canInstanceNum.getValue() + "FLTCON" + str(filterNumber / 4) + "__FSEL" + str(filterNumber) + "\"]")
    fifoSelect_Values = []
    fifoSelect_Values = fifoSelect_Node.getChildren()
    fifoSelect_Values = list(reversed(fifoSelect_Values))
    for index in range(len(fifoSelect_Values)):
        fifoSelect_Key_Value = fifoSelect_Values[index].getAttribute("value")
        fifoSelect_Key_Description = fifoSelect_Values[index].getAttribute("caption")
        fifoSelect.addKey(fifoSelect_Key_Description, fifoSelect_Key_Value, fifoSelect_Key_Description)
    fifoSelect.setDisplayMode("Key")
    fifoSelect.setOutputMode("Value")
    fifoSelect.setDefaultValue(1)

    maskSelect = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FILTER" + str(filterNumber) + "_MASK_SELECT", filterMenu)
    maskSelect.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:C1RXM0")
    maskSelect.setLabel("Select Acceptance Mask")
    maskSelect_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"C" + canInstanceNum.getValue() + "FLTCON" + str(filterNumber / 4) + "__MSEL" + str(filterNumber) + "\"]")
    maskSelect_Values = []
    maskSelect_Values = maskSelect_Node.getChildren()
    maskSelect_Values = list(reversed(maskSelect_Values))
    for index in range(len(maskSelect_Values)):
        maskSelect_Key_Value = maskSelect_Values[index].getAttribute("value")
        maskSelect_Key_Description = maskSelect_Values[index].getAttribute("caption")
        maskSelect.addKey(maskSelect_Key_Description, maskSelect_Key_Value, maskSelect_Key_Description)
    maskSelect.setDisplayMode("Key")
    maskSelect.setOutputMode("Value")
    maskSelect.setDefaultValue(0)

    if (filterNumber >= Database.getSymbolValue(canInstanceName.getValue().lower(), "NUMBER_OF_FILTER")):
        filterMenu.setVisible(False)
        filterMenu.setEnabled(False)
    return filterMenu

def canCreateAcceptanceFilterMask(component, menu, maskNumber):
    acceptanceFilterMaskMenu = component.createMenuSymbol(canInstanceName.getValue() + "_MASK"+ str(maskNumber), menu)
    acceptanceFilterMaskMenu.setLabel("Acceptance Filter Mask " + str(maskNumber))

    maskId = component.createHexSymbol(canInstanceName.getValue() + "_MASK" + str(maskNumber) + "_ID", acceptanceFilterMaskMenu)
    maskId.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:C1RXM0")
    maskId.setLabel("Mask ID")
    maskId.setMin(0)
    maskId.setMax(0x1FFFFFFF)

    maskIdDecimal = component.createIntegerSymbol(canInstanceName.getValue() + "_MASK" + str(maskNumber) + "_ID_DECIMAL", acceptanceFilterMaskMenu)
    maskIdDecimal.setVisible(False)
    maskIdDecimal.setMin(0)
    maskIdDecimal.setMax(536870911)
    maskIdDecimal.setDependencies(symbolSetValue, [canInstanceName.getValue() + "_MASK" + str(maskNumber) + "_ID"])

    if (maskNumber >= Database.getSymbolValue(canInstanceName.getValue().lower(), "NUMBER_OF_ACCEPTANCE_FILTER_MASK")):
        acceptanceFilterMaskMenu.setVisible(False)
        acceptanceFilterMaskMenu.setEnabled(False)
    return acceptanceFilterMaskMenu

def canCreateFifoConfig(component, menu, fifoNumber):
    fifoMenu = component.createMenuSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber), menu)
    fifoMenu.setLabel("FIFO " + str(fifoNumber))

    fifoSize = component.createIntegerSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_SIZE", fifoMenu)
    fifoSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCON0")
    fifoSize.setLabel("Number of Message Buffer")
    fifoSize.setMin(1)
    fifoSize.setMax(32)
    fifoSize.setDefaultValue(1)

    fifoTxEnable = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXEN", fifoMenu)
    fifoTxEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCON0")
    fifoTxEnable.setLabel("Select Trasmit/Receive FIFO")
    fifoTxEnable.addKey("RECEIVE_FIFO", "0x0", "FIFO is a Receive FIFO")
    fifoTxEnable.addKey("TRASMIT_FIFO", "0x1", "FIFO is a Transmit FIFO")
    fifoTxEnable.setOutputMode("Value")
    fifoTxEnable.setDisplayMode("Description")
    fifoTxEnable.setDefaultValue(0x1 if fifoNumber < 1 else 0x0)

    fifoTxPriority = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXPR", fifoMenu)
    fifoTxPriority.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCON0")
    fifoTxPriority.setLabel("Transmit Priority")
    fifoTxPriority.addKey("LOWEST_MSG_PRIORITY", "0x0", "Lowest Message Priority")
    fifoTxPriority.addKey("LOW_INT_MSG_PRIORITY", "0x1", "Low Intermediate Message Priority")
    fifoTxPriority.addKey("HIGH_INT_MSG_PRIORITY", "0x2", "High Intermediate Message Priority")
    fifoTxPriority.addKey("HIGHEST_MSG_PRIORITY", "0x3", "Highest Message Priority")
    fifoTxPriority.setOutputMode("Value")
    fifoTxPriority.setDisplayMode("Description")
    fifoTxPriority.setDefaultValue(0)
    fifoTxPriority.setVisible(True if fifoNumber < 1 else False)
    fifoTxPriority.setDependencies(hideMenu, [canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXEN"])

    fifoRTREnable = component.createKeyValueSetSymbol(canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_RTREN", fifoMenu)
    fifoRTREnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCON0")
    fifoRTREnable.setLabel("Auto RTR Enable")
    fifoRTREnable_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"C" + canInstanceNum.getValue() + "FIFOCON" + str(fifoNumber) + "__RTREN\"]")
    fifoRTREnable_Values = []
    fifoRTREnable_Values = fifoRTREnable_Node.getChildren()
    fifoRTREnable_Values = list(reversed(fifoRTREnable_Values))
    for index in range(len(fifoRTREnable_Values)):
        fifoRTREnable_Key_Value = fifoRTREnable_Values[index].getAttribute("value")
        fifoRTREnable_Key_Description = fifoRTREnable_Values[index].getAttribute("caption")
        fifoRTREnable.addKey(fifoRTREnable_Key_Description, fifoRTREnable_Key_Value, fifoRTREnable_Key_Description)
    fifoRTREnable.setDisplayMode("Description")
    fifoRTREnable.setOutputMode("Value")
    fifoRTREnable.setDefaultValue(0)
    fifoRTREnable.setVisible(True if fifoNumber < 1 else False)
    fifoRTREnable.setDependencies(hideMenu, [canInstanceName.getValue() + "_FIFO" + str(fifoNumber) + "_TXEN"])

    if (fifoNumber >= Database.getSymbolValue(canInstanceName.getValue().lower(), "NUMBER_OF_FIFO")):
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

# adjust how many Acceptance filter masks are shown based on number entered
def adjustAcceptanceMask(symbol, event):
    for mask in AcceptanceMaskList[:event["value"]]:
        if mask.getVisible() != True:
            mask.setVisible(True)
            mask.setEnabled(True)
    for mask in AcceptanceMaskList[event["value"]:]:
        if mask.getVisible() != False:
            mask.setVisible(False)
            mask.setEnabled(False)

def canInterruptSet(symbol, event):
    Database.setSymbolValue("core", canInterruptVector, event["value"])
    Database.setSymbolValue("core", canInterruptHandlerLock, event["value"])
    interruptName = canInterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if event["value"] == True:
        Database.setSymbolValue("core", canInterruptHandler, canInstanceName.getValue() + "_InterruptHandler")
    else:
        Database.setSymbolValue("core", canInterruptHandler, interruptName + "_Handler")

def updateCanInterruptData(symbol, event):
    component = symbol.getComponent()
    if canInterruptMode.getValue() == True and Database.getSymbolValue("core", canInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def canCoreClockFreq(symbol, event):
    symbol.setValue(int(Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")))

def autoBitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")
    bitrate = Database.getSymbolValue(canInstanceName.getValue().lower(), "NOMINAL_BITRATE")

    minErrPropag = propagSegment.getMax()
    minErrPhase1 = phase1Segment.getMax()
    minErrPhase2 = phase2Segment.getMax()
    minErrCalculatedNominalBitrate = 0.0
    minErrCalculatedTimeQuanta = lowTq
    minErrTqPeriod = 0.0
    minErrorRate = 100.0
    errorRate = 100.0
    minErrPrescaler = 0
    for propag in range(propagSegment.getMax(), propagSegment.getMin() - 1, -1):
        for phase1 in range(phase1Segment.getMax(), phase1Segment.getMin() - 1, -1):
            for phase2 in range(phase2Segment.getMax(), phase2Segment.getMin() - 1, -1):
                calculatedTimeQuanta = 1 + propag + phase1 + phase2
                if ((propag + phase1) >= phase2):
                    if ((lowTq <= calculatedTimeQuanta) and (calculatedTimeQuanta <= highTq)):
                        prescaler = int(clk /((bitrate * 1000) * (calculatedTimeQuanta * 2))) - 1;
                        if prescaler >= brpPrescaler.getMin():
                            if (prescaler > brpPrescaler.getMax()):
                                prescaler = brpPrescaler.getMax()

                            tqPeriod = float((2.0 * (prescaler + 1) / clk))
                            calculatedNominalBitrate = 1.0 / (float(tqPeriod) * calculatedTimeQuanta)
                            errorRate = ((float(calculatedNominalBitrate) - (bitrate * 1000)) / (bitrate * 1000)) * 100.0
                            if (abs(errorRate) < abs(minErrorRate)):
                                minErrorRate = errorRate
                                minErrPrescaler = prescaler
                                minErrPropag = propag
                                minErrPhase1 = phase1
                                minErrPhase2 = phase2
                                minErrCalculatedNominalBitrate = calculatedNominalBitrate
                                minErrCalculatedTimeQuanta = calculatedTimeQuanta
                                minErrTqPeriod = tqPeriod
                            if errorRate == 0:
                                break
            if errorRate == 0:
                break
        if errorRate == 0:
            break

    if (minErrPhase2 > 4):
        sjw = 4
    else:
        sjw = minErrPhase2

    canNominalSamplePoint.setReadOnly(True)
    canNominalSamplePoint.setValue((float(1 + minErrPropag + minErrPhase1)/minErrCalculatedTimeQuanta) * 100.0)
    brpPrescaler.setReadOnly(True)
    brpPrescaler.setValue(minErrPrescaler)
    propagSegmentTime.setReadOnly(True)
    propagSegmentTime.setValue(int(minErrPropag * (minErrTqPeriod * 1000000000.0)))
    return "{:.3f}".format(minErrorRate), (int(minErrCalculatedNominalBitrate) / 1000), "{:.3f}".format(minErrTqPeriod * 1000000000.0), minErrCalculatedTimeQuanta, minErrPropag, minErrPhase1, minErrPhase2, sjw

def bitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")

    prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "BRP")
    propagationDelayTime = Database.getSymbolValue(canInstanceName.getValue().lower(), "PROPAG_TIME")
    bitrate = Database.getSymbolValue(canInstanceName.getValue().lower(), "NOMINAL_BITRATE")
    samplePoint = Database.getSymbolValue(canInstanceName.getValue().lower(), "NOMINAL_SAMPLE_POINT")

    numOfTimeQuanta = clk / ((bitrate * 1000) * (2 * (prescaler + 1)))
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

    phase1 = int((numOfTimeQuanta * samplePoint) / 100.0)
    phase2 = numOfTimeQuanta - phase1 - 1
    propag = int(((numOfTimeQuanta * bitrate * propagationDelayTime) / 1000000) - 1)
    phase1 = phase1 - (propag + 1) - 2

    if ((phase2 + 1) > 4):
        sjw = 3
    else:
        sjw = phase2

    # Calculated Nominal Bitrate
    if (propag + 1) < propagSegment.getMin():
        calculatedPropag = propagSegment.getMin()
    elif (propag + 1) > propagSegment.getMax():
        calculatedPropag = propagSegment.getMax()
    else:
        calculatedPropag = propag + 1

    if (phase1 + 1) < phase1Segment.getMin():
        calculatedPhase1 = phase1Segment.getMin()
    elif (phase1 + 1) > phase1Segment.getMax():
        calculatedPhase1 = phase1Segment.getMax()
    else:
        calculatedPhase1 = phase1 + 1

    if (phase2 + 1) < phase2Segment.getMin():
        calculatedPhase2 = phase2Segment.getMin()
    elif (phase2 + 1) > phase2Segment.getMax():
        calculatedPhase2 = phase2Segment.getMax()
    else:
        calculatedPhase2 = phase2 + 1

    calculatedTimeQuanta = 1 + calculatedPropag + calculatedPhase1 + calculatedPhase2
    calculatedNominalBitrate = clk / (calculatedTimeQuanta * (2 * (prescaler + 1)))

    tqPeriod = 0.0
    if calculatedNominalBitrate != 0:
        # Calculated Time Quanta (TQ) Period in sec
        tqPeriod = 1.0 / (calculatedNominalBitrate * calculatedTimeQuanta)

    # Calculated Error %
    errorRate = ((float(calculatedNominalBitrate) - (bitrate * 1000)) / (bitrate * 1000)) * 100.0

    return "{:.3f}".format(errorRate), (calculatedNominalBitrate / 1000), "{:.3f}".format(tqPeriod * 1000000000.0), calculatedTimeQuanta, (propag + 1), (phase1 + 1), (phase2 + 1), (sjw + 1)

def nominalBitTimingCalculation(symbol, event):
    if Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True:
        if event["id"] == "BRP" or event["id"] == "NOMINAL_SAMPLE_POINT" or event["id"] == "PROPAG_TIME":
            return
        else:
            errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, propag, phase1, phase2, sjw = autoBitTimingCalculation("Nominal", 8, 25)
    else:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, propag, phase1, phase2, sjw = bitTimingCalculation("Nominal", 8, 25)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "TOTAL_TIME_QUANTA", timeQuanta)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PROPAG", propag)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PHASE1", phase1)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PHASE2", phase2)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "SJW", sjw)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "CALCULATED_NOMINAL_BITRATE", calculatedNominalBitrate)
    symbol.getComponent().getSymbolByID("TIME_QUANTA_PERIOD").setValue(str(tqPeriod))
    symbol.getComponent().getSymbolByID("CALCULATED_ERRORRATE").setValue(str(errorRate))
    if abs(float(errorRate)) > 1:
        canErrorRateCommentSym.setLabel("Warning!!! Error " + str(errorRate) + "%")
        canErrorRateCommentSym.setVisible(True)
    else:
        canErrorRateCommentSym.setVisible(False)

def updateNominalBitTimingSymbols(symbol, event):
    if (event["value"]):
        symbol.getComponent().getSymbolByID("BRP").setReadOnly(True)
        symbol.getComponent().getSymbolByID("NOMINAL_SAMPLE_POINT").setReadOnly(True)
        symbol.getComponent().getSymbolByID("PROPAG_TIME").setReadOnly(True)
        canTimeQuantaInvalidSym.setVisible(False)
        canCoreClockInvalidSym.setVisible(False)
    else:
        symbol.getComponent().getSymbolByID("BRP").setReadOnly(False)
        symbol.getComponent().getSymbolByID("NOMINAL_SAMPLE_POINT").setReadOnly(False)
        symbol.getComponent().getSymbolByID("PROPAG_TIME").setReadOnly(False)

def hideMenu(menu, event):
    menu.setVisible(event["value"])

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
    global canNominalSamplePoint
    global brpPrescaler
    global propagSegmentTime
    global canErrorRateCommentSym
    global propagSegment
    global phase1Segment
    global phase2Segment

    canInstanceName = canComponent.createStringSymbol("CAN_INSTANCE_NAME", None)
    canInstanceName.setVisible(False)
    canInstanceName.setDefaultValue(canComponent.getID().upper())
    Log.writeInfoMessage("Running " + canInstanceName.getValue())

    canInstanceNum = canComponent.createStringSymbol("CAN_INSTANCE_NUM", None)
    canInstanceNum.setVisible(False)
    canInstanceNum.setDefaultValue(filter(str.isdigit,str(canComponent.getID())))

    # Initialize peripheral clock
    Database.setSymbolValue("core", canInstanceName.getValue()+"_CLOCK_ENABLE", True)

    canOpMode = canComponent.createKeyValueSetSymbol("CAN_OPMODE", None)
    canOpMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:C1CON")
    canOpMode.setLabel("CAN Operation Mode")
    canOpMode_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"C" + canInstanceNum.getValue() + "CON__REQOP\"]")
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
    canInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxINT")
    canInterruptMode.setLabel("Interrupt Mode")
    canInterruptMode.setDefaultValue(False)

    canIrq = "CAN_" + canInstanceNum.getValue()
    canVectorNum = getVectorIndex(canIrq)

    if canVectorNum != "-1":
        canInterruptVector = canIrq + "_INTERRUPT_ENABLE"
        canInterruptHandler = canIrq + "_INTERRUPT_HANDLER"
        canInterruptHandlerLock = canIrq + "_INTERRUPT_HANDLER_LOCK"
        canInterruptVectorUpdate = canIrq + "_INTERRUPT_ENABLE_UPDATE"
        canIrq_index = int(getIRQnumber(canInstanceName.getValue()))
        enblRegName = _get_enblReg_parms(canIrq_index)
        statRegName = _get_statReg_parms(canIrq_index)
    else:
        canInterruptVector = canInstanceName.getValue() + "_INTERRUPT_ENABLE"
        canInterruptHandler = canInstanceName.getValue() + "_INTERRUPT_HANDLER"
        canInterruptHandlerLock = canInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
        canInterruptVectorUpdate = canInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
        canIrq_index = int(getVectorIndex(canInstanceName.getValue()))
        enblRegName = _get_enblReg_parms(canIrq_index)
        statRegName = _get_statReg_parms(canIrq_index)

    # CAN Bit Timing Calculation
    canBitTimingCalculationMenu = canComponent.createMenuSymbol("BIT_TIMING_CALCULATION", None)
    canBitTimingCalculationMenu.setLabel("Bit Timing Calculation")
    canBitTimingCalculationMenu.setDescription("CAN Bit Timing Calculation for Normal Operation")

    canCoreClockValue = canComponent.createIntegerSymbol("CAN_CORE_CLOCK_FREQ", canBitTimingCalculationMenu)
    canCoreClockValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:C1CON")
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
    canNominalBitTimingMenu.setDescription("Nominal Bit Timing for CAN Message Frame")

    canAutomaticNominalBitTimingCalculation = canComponent.createBooleanSymbol("AUTO_NOMINAL_BIT_TIMING_CALCULATION", canNominalBitTimingMenu)
    canAutomaticNominalBitTimingCalculation.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canAutomaticNominalBitTimingCalculation.setLabel("Automatic Nominal Bit Timing Calculation")
    canAutomaticNominalBitTimingCalculation.setDefaultValue(False)
    canAutomaticNominalBitTimingCalculation.setDependencies(updateNominalBitTimingSymbols, ["AUTO_NOMINAL_BIT_TIMING_CALCULATION"])

    canNominalBitrate = canComponent.createIntegerSymbol("NOMINAL_BITRATE", canNominalBitTimingMenu)
    canNominalBitrate.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canNominalBitrate.setLabel("Bit Rate (Kbps)")
    canNominalBitrate.setMin(1)
    canNominalBitrate.setMax(1000)
    canNominalBitrate.setDefaultValue(500)
    canNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "AUTO_NOMINAL_BIT_TIMING_CALCULATION", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canNominalSamplePoint = canComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", canNominalBitTimingMenu)
    canNominalSamplePoint.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canNominalSamplePoint.setLabel("Sample Point %")
    canNominalSamplePoint.setMin(50.0)
    canNominalSamplePoint.setMax(100.0)
    canNominalSamplePoint.setDefaultValue(75.0)
    canNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])
    canNominalSamplePoint.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    brpPrescaler = canComponent.createIntegerSymbol("BRP", canNominalBitTimingMenu)
    brpPrescaler.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    brpPrescaler.setLabel("Baudrate Prescaler")
    brpPrescaler.setMin(0)
    brpPrescaler.setMax(63)
    brpPrescaler.setDefaultValue(4)
    brpPrescaler.setDependencies(nominalBitTimingCalculation, ["BRP"])
    brpPrescaler.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    propagSegmentTime = canComponent.createIntegerSymbol("PROPAG_TIME", canNominalBitTimingMenu)
    propagSegmentTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    propagSegmentTime.setLabel("Propagation Segment Time (ns)")
    propagSegmentTime.setMin(1)
    propagSegmentTime.setDefaultValue(300)
    propagSegmentTime.setDependencies(nominalBitTimingCalculation, ["PROPAG_TIME"])
    propagSegmentTime.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    totalTimeQuanta = canComponent.createIntegerSymbol("TOTAL_TIME_QUANTA", canNominalBitTimingMenu)
    totalTimeQuanta.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    totalTimeQuanta.setLabel("Total Time Quanta (TQ)")
    totalTimeQuanta.setReadOnly(True)

    syncSegment = canComponent.createIntegerSymbol("SYNC", totalTimeQuanta)
    syncSegment.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    syncSegment.setLabel("Sync Segment (TQ)")
    syncSegment.setDefaultValue(1)
    syncSegment.setReadOnly(True)

    propagSegment = canComponent.createIntegerSymbol("PROPAG", totalTimeQuanta)
    propagSegment.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    propagSegment.setLabel("Propagation Segment (TQ)")
    propagSegment.setMin(1)
    propagSegment.setMax(8)
    propagSegment.setReadOnly(True)

    phase1Segment = canComponent.createIntegerSymbol("PHASE1", totalTimeQuanta)
    phase1Segment.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    phase1Segment.setLabel("Phase 1 Segment (TQ)")
    phase1Segment.setMin(1)
    phase1Segment.setMax(8)
    phase1Segment.setReadOnly(True)

    phase2Segment = canComponent.createIntegerSymbol("PHASE2", totalTimeQuanta)
    phase2Segment.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    phase2Segment.setLabel("Phase 2 Segment (TQ)")
    phase2Segment.setMin(1)
    phase2Segment.setMax(8)
    phase2Segment.setReadOnly(True)

    if Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, propag, phase1, phase2, sjw = autoBitTimingCalculation("Nominal", 8, 25)
    else:
        errorRate, calculatedNominalBitrate, tqPeriod, timeQuanta, propag, phase1, phase2, sjw = bitTimingCalculation("Nominal", 8, 25)

    totalTimeQuanta.setDefaultValue(timeQuanta)
    propagSegment.setDefaultValue(propag)
    phase1Segment.setDefaultValue(phase1)
    phase2Segment.setDefaultValue(phase2)

    syncJumpWidth = canComponent.createIntegerSymbol("SJW", canNominalBitTimingMenu)
    syncJumpWidth.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    syncJumpWidth.setLabel("Synchronization Jump Width (TQ)")
    syncJumpWidth.setMin(1)
    syncJumpWidth.setMax(4)
    syncJumpWidth.setDefaultValue(sjw)
    syncJumpWidth.setReadOnly(True)

    canTimeQuantaPeriod = canComponent.createStringSymbol("TIME_QUANTA_PERIOD", canNominalBitTimingMenu)
    canTimeQuantaPeriod.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canTimeQuantaPeriod.setLabel("Time Quanta (ns)")
    canTimeQuantaPeriod.setDefaultValue(str(tqPeriod))
    canTimeQuantaPeriod.setReadOnly(True)

    canCalculatedNominalBitrate = canComponent.createIntegerSymbol("CALCULATED_NOMINAL_BITRATE", canNominalBitTimingMenu)
    canCalculatedNominalBitrate.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canCalculatedNominalBitrate.setLabel("Calculated Bit Rate (Kbps)")
    canCalculatedNominalBitrate.setDefaultValue(calculatedNominalBitrate)
    canCalculatedNominalBitrate.setReadOnly(True)

    canCalculatedError = canComponent.createStringSymbol("CALCULATED_ERRORRATE", canNominalBitTimingMenu)
    canCalculatedError.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canCalculatedError.setLabel("Error %")
    canCalculatedError.setDefaultValue(str(errorRate))
    canCalculatedError.setReadOnly(True)

    canErrorRateCommentSym = canComponent.createCommentSymbol("CAN_ERRORRATE_COMMENT", canCalculatedError)
    canErrorRateCommentSym.setLabel("Warning!!! Error " + canCalculatedError.getValue() + "%")
    canErrorRateCommentSym.setVisible(abs(float(errorRate)) > 1)

    canConfigSAM = canComponent.createKeyValueSetSymbol("CAN_CFG_SAM", canNominalBitTimingMenu)
    canConfigSAM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCFG")
    canConfigSAM.setLabel("Sample of the CAN Bus Line bit")
    canConfigSAM.setDescription("3 Time bit sampling is not allowed if BRP is less than 2")
    canConfigSAM_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"C" + canInstanceNum.getValue() + "CFG__SAM\"]")
    canConfigSAM_Values = []
    canConfigSAM_Values = canConfigSAM_Node.getChildren()
    canConfigSAM_Values = list(reversed(canConfigSAM_Values))
    for index in range(len(canConfigSAM_Values)):
        canConfigSAM_Key_Value = canConfigSAM_Values[index].getAttribute("value")
        canConfigSAM_Key_Description = canConfigSAM_Values[index].getAttribute("caption")
        canConfigSAM.addKey(canConfigSAM_Key_Description, canConfigSAM_Key_Value, canConfigSAM_Key_Description)
    canConfigSAM.setDisplayMode("Key")
    canConfigSAM.setOutputMode("Value")
    canConfigSAM.setDefaultValue(0)

    # CAN Message FIFO configuration
    canFifoConfMenu = canComponent.createMenuSymbol("FIFO_CONF_MENU", None)
    canFifoConfMenu.setLabel("FIFO Configuration")
    canFifoConfMenu.setDependencies(adjustFIFOs, ["NUMBER_OF_FIFO"])

    # Number of FIFOs
    canFifoNumber = canComponent.createIntegerSymbol("NUMBER_OF_FIFO", canFifoConfMenu)
    canFifoNumber.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCONn")
    canFifoNumber.setLabel("Number of FIFOs")
    canFifoNumber.setDefaultValue(2)
    canFifoNumber.setMin(1)
    canRegs_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/register-group@[name=\"CAN\"]")
    canRegs_Values = []
    canRegs_Values = canRegs_Node.getChildren()
    maxFifoNum = 0
    canFifoControlReg = "C" + canInstanceNum.getValue() + "FIFOCON"
    for index in range(len(canRegs_Values)):
        if canFifoControlReg in canRegs_Values[index].getAttribute("name"):
            maxFifoNum += 1
    canFifoNumber.setMax(maxFifoNum)

    # Create all FIFOs in a disabled state
    for fifo in range (canFifoNumber.getMax()):
        fifoList.append(canCreateFifoConfig(canComponent, canFifoConfMenu, fifo))

    # CAN Filter Configuration
    canFilterMenu = canComponent.createMenuSymbol("FilterMenu", None)
    canFilterMenu.setLabel("Filter Configuration")
    canFilterMenu.setDependencies(adjustFilters, ["NUMBER_OF_FILTER"])

    # Number of Filters
    canFilterNumber = canComponent.createIntegerSymbol("NUMBER_OF_FILTER", canFilterMenu)
    canFilterNumber.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCONn")
    canFilterNumber.setLabel("Number of Filters")
    canFilterNumber.setDefaultValue(1)
    canFilterNumber.setMin(1)
    maxFilterNum = 0
    canFilterReg = "C" + canInstanceNum.getValue() + "RXF"
    for index in range(len(canRegs_Values)):
        if canFilterReg in canRegs_Values[index].getAttribute("name"):
            maxFilterNum += 1
    canFilterNumber.setMax(maxFilterNum)

    #Create all filters in a disabled state
    for fltr in range (canFilterNumber.getMax()):
        filterList.append(canCreateFilter(canComponent, canFilterMenu, fltr))

    # CAN Acceptance Mask Configuration
    canAcceptanceMaskMenu = canComponent.createMenuSymbol("AcceptanceMaskMenu", None)
    canAcceptanceMaskMenu.setLabel("Acceptance Mask Configuration")
    canAcceptanceMaskMenu.setDependencies(adjustAcceptanceMask, ["NUMBER_OF_ACCEPTANCE_FILTER_MASK"])

    canAcceptanceMaskNumber = canComponent.createIntegerSymbol("NUMBER_OF_ACCEPTANCE_FILTER_MASK", canAcceptanceMaskMenu)
    canAcceptanceMaskNumber.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxFIFOCONn")
    canAcceptanceMaskNumber.setLabel("Number of Acceptance Filter Mask")
    canAcceptanceMaskNumber.setDefaultValue(1)
    canAcceptanceMaskNumber.setMin(1)
    maxAcceptanceMaskNum = 0
    canAcceptanceMaskReg = "C" + canInstanceNum.getValue() + "RXM"
    for index in range(len(canRegs_Values)):
        if canAcceptanceMaskReg in canRegs_Values[index].getAttribute("name"):
            maxAcceptanceMaskNum += 1
    canAcceptanceMaskNumber.setMax(maxAcceptanceMaskNum)

    #Create all filters in a disabled state
    for mask in range (canAcceptanceMaskNumber.getMax()):
        AcceptanceMaskList.append(canCreateAcceptanceFilterMask(canComponent, canAcceptanceMaskMenu, mask))

    canTimestampEnable = canComponent.createBooleanSymbol("CAN_TIMESTAMP_ENABLE", None)
    canTimestampEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:CxCON")
    canTimestampEnable.setLabel("Timestamp Enable")
    canTimestampEnable.setDefaultValue(False)

    canTimestampPrescaler = canComponent.createIntegerSymbol("CAN_TIMESTAMP_PRESCALER", canTimestampEnable)
    canTimestampPrescaler.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:can_01152;register:C1TMR")
    canTimestampPrescaler.setLabel("Timestamp Timer Prescaler")
    canTimestampPrescaler.setDefaultValue(0)
    canTimestampPrescaler.setMin(0)
    canTimestampPrescaler.setMax(65535)
    canTimestampPrescaler.setVisible(False)
    canTimestampPrescaler.setDependencies(hideMenu, ["CAN_TIMESTAMP_ENABLE"])

    # Interrupt Dynamic settings
    caninterruptEnable = canComponent.createBooleanSymbol("CAN_INTERRUPT_ENABLE", None)
    caninterruptEnable.setVisible(False)
    caninterruptEnable.setDependencies(canInterruptSet, ["CAN_INTERRUPT_MODE"])

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
    canMasterHeaderFile.setSourcePath("../peripheral/can_01152/templates/plib_can_common.h")
    canMasterHeaderFile.setOutputName("plib_can_common.h")
    canMasterHeaderFile.setDestPath("/peripheral/can/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = canComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/can_01152/templates/plib_can.c.ftl")
    canMainSourceFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".c")
    canMainSourceFile.setDestPath("/peripheral/can/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)

    #Instance Header File
    canInstHeaderFile = canComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/can_01152/templates/plib_can.h.ftl")
    canInstHeaderFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".h")
    canInstHeaderFile.setDestPath("/peripheral/can/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)

    #CAN Initialize
    canSystemInitFile = canComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    canSystemInitFile.setSourcePath("../peripheral/can_01152/templates/system/initialization.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = canComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/can_01152/templates/system/definitions.h.ftl")
    canSystemDefFile.setMarkup(True)
