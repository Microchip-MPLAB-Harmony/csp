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

def interruptControl(symbol, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    if event["value"] == True:
        Database.setSymbolValue("core", interruptVector, True)
        Database.setSymbolValue("core", interruptHandler, canInstanceName.getValue() + "_InterruptHandler")
        Database.setSymbolValue("core", interruptHandlerLock, True)
    else:
        Database.setSymbolValue("core", interruptVector, False)
        Database.setSymbolValue("core", interruptHandler, canInstanceName.getValue() + "_Handler")
        Database.setSymbolValue("core", interruptHandlerLock, False)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):
    if (Database.getSymbolValue(canInstanceName.getValue().lower(), "INTERRUPT_MODE") == True):
        symbol.setVisible(event["value"])

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
                        prescaler = int(clk /((bitrate * 1000) * calculatedTimeQuanta)) - 1;
                        if prescaler >= brpPrescaler.getMin():
                            if (prescaler > brpPrescaler.getMax()):
                                prescaler = brpPrescaler.getMax()

                            tqPeriod = float(prescaler + 1) / clk
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

    phase1 = int((numOfTimeQuanta * samplePoint) / 100.0)
    phase2 = numOfTimeQuanta - phase1 - 1
    # The propagation segment time is equal to twice the sum of the signal's propagation time on the bus line, the receiver delay and the output driver delay
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
    calculatedNominalBitrate = clk / (calculatedTimeQuanta * (prescaler + 1))

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

def symbolVisible(symbol, event):
    if event['value'] == 1 or event['value'] == 2 or event['value'] == 4:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def symbolSetValue(symbol, event):
    symbol.setValue(event["value"])

def instantiateComponent(canComponent):
    global canInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global canCoreClockInvalidSym
    global canTimeQuantaInvalidSym
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
    print("Running " + canInstanceName.getValue())

    # Initialize peripheral clock
    Database.setSymbolValue("core", canInstanceName.getValue()+"_CLOCK_ENABLE", True)

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
    canBitTimingCalculationMenu.setDescription("CAN Bit Timing Calculation for Normal Operation")

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
    canNominalBitTimingMenu.setDescription("Nominal Bit Timing for CAN Message Frame")

    canAutomaticNominalBitTimingCalculation = canComponent.createBooleanSymbol("AUTO_NOMINAL_BIT_TIMING_CALCULATION", canNominalBitTimingMenu)
    canAutomaticNominalBitTimingCalculation.setLabel("Automatic Nominal Bit Timing Calculation")
    canAutomaticNominalBitTimingCalculation.setDefaultValue(False)
    canAutomaticNominalBitTimingCalculation.setDependencies(updateNominalBitTimingSymbols, ["AUTO_NOMINAL_BIT_TIMING_CALCULATION"])

    canNominalBitrate = canComponent.createIntegerSymbol("NOMINAL_BITRATE", canNominalBitTimingMenu)
    canNominalBitrate.setLabel("Bit Rate (Kbps)")
    canNominalBitrate.setMin(1)
    canNominalBitrate.setMax(1000)
    canNominalBitrate.setDefaultValue(500)
    canNominalBitrate.setDependencies(nominalBitTimingCalculation, ["NOMINAL_BITRATE", "AUTO_NOMINAL_BIT_TIMING_CALCULATION", "core." + canInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    canNominalSamplePoint = canComponent.createFloatSymbol("NOMINAL_SAMPLE_POINT", canNominalBitTimingMenu)
    canNominalSamplePoint.setLabel("Sample Point %")
    canNominalSamplePoint.setMin(50.0)
    canNominalSamplePoint.setMax(100.0)
    canNominalSamplePoint.setDefaultValue(75.0)
    canNominalSamplePoint.setDependencies(nominalBitTimingCalculation, ["NOMINAL_SAMPLE_POINT"])
    canNominalSamplePoint.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    brpPrescaler = canComponent.createIntegerSymbol("BRP", canNominalBitTimingMenu)
    brpPrescaler.setLabel("Baudrate Prescaler")
    brpPrescaler.setMin(1)
    brpPrescaler.setMax(127)
    brpPrescaler.setDefaultValue(24)
    brpPrescaler.setDependencies(nominalBitTimingCalculation, ["BRP"])
    brpPrescaler.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    propagSegmentTime = canComponent.createIntegerSymbol("PROPAG_TIME", canNominalBitTimingMenu)
    propagSegmentTime.setLabel("Propagation Segment Time (ns)")
    propagSegmentTime.setMin(1)
    propagSegmentTime.setDefaultValue(380)
    propagSegmentTime.setDependencies(nominalBitTimingCalculation, ["PROPAG_TIME"])
    propagSegmentTime.setReadOnly(Database.getSymbolValue(canInstanceName.getValue().lower(), "AUTO_NOMINAL_BIT_TIMING_CALCULATION") == True)

    totalTimeQuanta = canComponent.createIntegerSymbol("TOTAL_TIME_QUANTA", canNominalBitTimingMenu)
    totalTimeQuanta.setLabel("Total Time Quanta (TQ)")
    totalTimeQuanta.setReadOnly(True)

    syncSegment = canComponent.createIntegerSymbol("SYNC", totalTimeQuanta)
    syncSegment.setLabel("Sync Segment (TQ)")
    syncSegment.setDefaultValue(1)
    syncSegment.setReadOnly(True)

    propagSegment = canComponent.createIntegerSymbol("PROPAG", totalTimeQuanta)
    propagSegment.setLabel("Propagation Segment (TQ)")
    propagSegment.setMin(1)
    propagSegment.setMax(8)
    propagSegment.setReadOnly(True)

    phase1Segment = canComponent.createIntegerSymbol("PHASE1", totalTimeQuanta)
    phase1Segment.setLabel("Phase 1 Segment (TQ)")
    phase1Segment.setMin(1)
    phase1Segment.setMax(8)
    phase1Segment.setReadOnly(True)

    phase2Segment = canComponent.createIntegerSymbol("PHASE2", totalTimeQuanta)
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
    syncJumpWidth.setLabel("Synchronization Jump Width (TQ)")
    syncJumpWidth.setMin(1)
    syncJumpWidth.setMax(4)
    syncJumpWidth.setDefaultValue(sjw)
    syncJumpWidth.setReadOnly(True)

    canTimeQuantaPeriod = canComponent.createStringSymbol("TIME_QUANTA_PERIOD", canNominalBitTimingMenu)
    canTimeQuantaPeriod.setLabel("Time Quanta (ns)")
    canTimeQuantaPeriod.setDefaultValue(str(tqPeriod))
    canTimeQuantaPeriod.setReadOnly(True)

    canCalculatedNominalBitrate = canComponent.createIntegerSymbol("CALCULATED_NOMINAL_BITRATE", canNominalBitTimingMenu)
    canCalculatedNominalBitrate.setLabel("Calculated Bit Rate (Kbps)")
    canCalculatedNominalBitrate.setDefaultValue(calculatedNominalBitrate)
    canCalculatedNominalBitrate.setReadOnly(True)

    canCalculatedError = canComponent.createStringSymbol("CALCULATED_ERRORRATE", canNominalBitTimingMenu)
    canCalculatedError.setLabel("Error %")
    canCalculatedError.setDefaultValue(str(errorRate))
    canCalculatedError.setReadOnly(True)

    canErrorRateCommentSym = canComponent.createCommentSymbol("CAN_ERRORRATE_COMMENT", canCalculatedError)
    canErrorRateCommentSym.setLabel("Warning!!! Error " + canCalculatedError.getValue() + "%")
    canErrorRateCommentSym.setVisible(abs(float(errorRate)) > 1)

    canConfigSMP = canComponent.createKeyValueSetSymbol("CAN_CFG_SMP", canNominalBitTimingMenu)
    canConfigSMP.setLabel("Sampling Mode")
    canConfigSMP.setDescription("SMP Sampling Mode is automatically disabled if BRP is 0")
    canConfigSMP_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CAN_BR__SMP\"]")
    canConfigSMP_Values = []
    canConfigSMP_Values = canConfigSMP_Node.getChildren()
    for index in range(len(canConfigSMP_Values)):
        canConfigSMP_Key_Value = canConfigSMP_Values[index].getAttribute("value")
        canConfigSMP_Key_Name = canConfigSMP_Values[index].getAttribute("name")
        canConfigSMP_Key_Description = canConfigSMP_Values[index].getAttribute("caption")
        canConfigSMP.addKey(canConfigSMP_Key_Name, canConfigSMP_Key_Value, canConfigSMP_Key_Description)
    canConfigSMP.setDisplayMode("Key")
    canConfigSMP.setOutputMode("Value")
    canConfigSMP.setDefaultValue(0)

    # Mailbox configuration
    canMailboxConfigurationMenu = canComponent.createMenuSymbol("MAILBOX_CONFIGURATION", None)
    canMailboxConfigurationMenu.setLabel("Mailbox Configuration")
    canMailboxConfigurationMenu.setDescription("Mailbox configuration for mailbox object type and message acceptance")

    canNumberOfMailbox = canComponent.createIntegerSymbol("NUMBER_OF_MAILBOX", canMailboxConfigurationMenu)
    canNumberOfMailbox.setLabel("Number of mailbox")
    canNumberOfMailbox_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/register-group@[name=\"CAN\"]/register@[name=\"CAN_TCR\"]")
    canNumberOfMailbox_Values = canNumberOfMailbox_Node.getChildren()
    NumOfMB = 0
    for index in range(len(canNumberOfMailbox_Values)):
        if canNumberOfMailbox_Values[index].getAttribute("name")[:2] == "MB":
            NumOfMB += 1
    canNumberOfMailbox.setDefaultValue(NumOfMB)
    canNumberOfMailbox.setVisible(False)

    for MBNum in range(0, canNumberOfMailbox.getValue(), 1):
        canMailboxMenu = canComponent.createMenuSymbol("MAILBOX" + str(MBNum) + "_CONFIGURATION", canMailboxConfigurationMenu)
        canMailboxMenu.setLabel("Mailbox " + str(MBNum) + " Configuration")
        canMailboxMenu.setDescription("Mailbox " + str(MBNum) + " configuration for mailbox object type and message acceptance")
        # Each Mailbox configuration
        canMailbox_MMR_MOT = canComponent.createKeyValueSetSymbol("CAN_MMR" + str(MBNum) + "_MOT", canMailboxMenu)
        canMailbox_MMR_MOT.setLabel("Mailbox Object Type")
        canMailbox_MMR_MOT_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CAN\"]/value-group@[name=\"CAN_MMR0__MOT\"]")
        canMailbox_MMR_MOT_Values = canMailbox_MMR_MOT_Node.getChildren()
        for index in range(len(canMailbox_MMR_MOT_Values)):
            canMailbox_MMR_MOT_Name = canMailbox_MMR_MOT_Values[index].getAttribute("name")
            canMailbox_MMR_MOT_Value = canMailbox_MMR_MOT_Values[index].getAttribute("value")
            canMailbox_MMR_MOT_Description = canMailbox_MMR_MOT_Values[index].getAttribute("caption")
            canMailbox_MMR_MOT.addKey(canMailbox_MMR_MOT_Name, canMailbox_MMR_MOT_Value, canMailbox_MMR_MOT_Description)
        canMailbox_MMR_MOT.setDefaultValue((3-MBNum) if MBNum < 2 else 0)
        canMailbox_MMR_MOT.setDisplayMode("Key")
        canMailbox_MMR_MOT.setOutputMode("Key")
        canMailbox_MMR_MOT.setVisible(True)

        canMailbox_MID_Identifier = canComponent.createHexSymbol("CAN_MID" + str(MBNum) + "_ID", canMailboxMenu)
        canMailbox_MID_Identifier.setLabel("Message ID")
        canMailbox_MID_Identifier.setMin(0)
        canMailbox_MID_Identifier.setMax(0x1FFFFFFF)
        canMailbox_MID_Identifier.setDefaultValue(0)
        canMailbox_MID_Identifier.setVisible((canMailbox_MMR_MOT.getValue() == 1 or
                                              canMailbox_MMR_MOT.getValue() == 2 or
                                              canMailbox_MMR_MOT.getValue() == 4))
        canMailbox_MID_Identifier.setDependencies(symbolVisible, ["CAN_MMR" + str(MBNum) + "_MOT"])

        canMailbox_MID_IdentifierDecimal = canComponent.createIntegerSymbol("CAN_MID" + str(MBNum) + "_ID_DECIMAL", canMailboxMenu)
        canMailbox_MID_IdentifierDecimal.setVisible(False)
        canMailbox_MID_IdentifierDecimal.setMin(0)
        canMailbox_MID_IdentifierDecimal.setMax(536870911)
        canMailbox_MID_IdentifierDecimal.setDefaultValue(0)
        canMailbox_MID_IdentifierDecimal.setDependencies(symbolSetValue, ["CAN_MID" + str(MBNum) + "_ID"])

        canMailbox_MAM_Identifier = canComponent.createHexSymbol("CAN_MAM" + str(MBNum) + "_ID", canMailboxMenu)
        canMailbox_MAM_Identifier.setLabel("Message Acceptance Mask ID")
        canMailbox_MAM_Identifier.setMin(0)
        canMailbox_MAM_Identifier.setMax(0x1FFFFFFF)
        canMailbox_MAM_Identifier.setDefaultValue(0)
        canMailbox_MAM_Identifier.setVisible((canMailbox_MMR_MOT.getValue() == 1 or
                                              canMailbox_MMR_MOT.getValue() == 2 or
                                              canMailbox_MMR_MOT.getValue() == 4))
        canMailbox_MAM_Identifier.setDependencies(symbolVisible, ["CAN_MMR" + str(MBNum) + "_MOT"])

        canMailbox_MAM_IdentifierDecimal = canComponent.createIntegerSymbol("CAN_MAM" + str(MBNum) + "_ID_DECIMAL", canMailboxMenu)
        canMailbox_MAM_IdentifierDecimal.setVisible(False)
        canMailbox_MAM_IdentifierDecimal.setMin(0)
        canMailbox_MAM_IdentifierDecimal.setMax(536870911)
        canMailbox_MAM_IdentifierDecimal.setDefaultValue(0)
        canMailbox_MAM_IdentifierDecimal.setDependencies(symbolSetValue, ["CAN_MAM" + str(MBNum) + "_ID"])

    canTimestampEnable = canComponent.createBooleanSymbol("TIMESTAMP_ENABLE", None)
    canTimestampEnable.setLabel("Timestamp Enable")
    canTimestampEnable.setDefaultValue(True)
    canTimestampEnable.setReadOnly(True)

    #Timestamp EOF Mode
    canTimestampEofMode = canComponent.createBooleanSymbol("TIMESTAMP_EOF_MODE", canTimestampEnable)
    canTimestampEofMode.setLabel("Timestamp at end of message frame")
    canTimestampEofMode.setDescription("Timestamp at end of message frame : True, Timestamp at start of message frame : False")
    canTimestampEofMode.setDefaultValue(False)

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
    canMasterHeaderFile.setSourcePath("../peripheral/can_6019/templates/plib_can_common.h")
    canMasterHeaderFile.setOutputName("plib_can_common.h")
    canMasterHeaderFile.setDestPath("/peripheral/can/")
    canMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMasterHeaderFile.setType("HEADER")

    #Instance Source File
    canMainSourceFile = canComponent.createFileSymbol("sourceFile", None)
    canMainSourceFile.setSourcePath("../peripheral/can_6019/templates/plib_can.c.ftl")
    canMainSourceFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".c")
    canMainSourceFile.setDestPath("/peripheral/can/")
    canMainSourceFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canMainSourceFile.setType("SOURCE")
    canMainSourceFile.setMarkup(True)

    #Instance Header File
    canInstHeaderFile = canComponent.createFileSymbol("instHeaderFile", None)
    canInstHeaderFile.setSourcePath("../peripheral/can_6019/templates/plib_can.h.ftl")
    canInstHeaderFile.setOutputName("plib_"+canInstanceName.getValue().lower()+".h")
    canInstHeaderFile.setDestPath("/peripheral/can/")
    canInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/can/")
    canInstHeaderFile.setType("HEADER")
    canInstHeaderFile.setMarkup(True)

    #CAN Initialize
    canSystemInitFile = canComponent.createFileSymbol("initFile", None)
    canSystemInitFile.setType("STRING")
    canSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    canSystemInitFile.setSourcePath("../peripheral/can_6019/templates/system/initialization.c.ftl")
    canSystemInitFile.setMarkup(True)

    #CAN definitions header
    canSystemDefFile = canComponent.createFileSymbol("defFile", None)
    canSystemDefFile.setType("STRING")
    canSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    canSystemDefFile.setSourcePath("../peripheral/can_6019/templates/system/definitions.h.ftl")
    canSystemDefFile.setMarkup(True)
