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

def bitTimingCalculation(bitTiming, lowTq, highTq):
    clk = Database.getSymbolValue("core", canInstanceName.getValue() + "_CLOCK_FREQUENCY")

    prescaler = Database.getSymbolValue(canInstanceName.getValue().lower(), "BRP")
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
    # Calculate timing delay as Delay of the bus driver: 50 ns, Delay of the receiver: 30 ns and Delay of the bus line (20 m): 110 ns
    propag = int(((numOfTimeQuanta * bitrate * (2 * (50 + 30 + 110))) / 1000000) - 1)
    phase1 = phase1 - (propag + 1) - 2

    if ((phase1 + 1) > 4):
        sjw = 3
    else:
        sjw = phase1

    return propag, phase1, phase2, sjw

def nominalBitTimingCalculation(symbol, event):
    propag, phase1, phase2, sjw = bitTimingCalculation("Nominal", 8, 25)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PROPAG", propag)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PHASE1", phase1)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "PHASE2", phase2)
    Database.setSymbolValue(canInstanceName.getValue().lower(), "SJW", sjw)

def MsgAcceptanceMsksymbolVisible(symbol, event):
    if event['value'] == 1 or event['value'] == 2 or event['value'] == 4:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def instantiateComponent(canComponent):
    global canInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global canCoreClockInvalidSym
    global canTimeQuantaInvalidSym

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

    brpPrescaler = canComponent.createIntegerSymbol("BRP", canNominalBitTimingMenu)
    brpPrescaler.setLabel("Baudrate Prescaler")
    brpPrescaler.setMin(1)
    brpPrescaler.setMax(127)
    brpPrescaler.setDefaultValue(24)
    brpPrescaler.setDependencies(nominalBitTimingCalculation, ["BRP"])

    propag, phase1, phase2, sjw = bitTimingCalculation("Nominal", 8, 25)

    propagSegment = canComponent.createIntegerSymbol("PROPAG", canNominalBitTimingMenu)
    propagSegment.setLabel("Propagation Segment")
    propagSegment.setMin(0)
    propagSegment.setMax(7)
    propagSegment.setDefaultValue(propag)
    propagSegment.setReadOnly(True)

    phase1Segment = canComponent.createIntegerSymbol("PHASE1", canNominalBitTimingMenu)
    phase1Segment.setLabel("Phase 1 Segment")
    phase1Segment.setMin(0)
    phase1Segment.setMax(7)
    phase1Segment.setDefaultValue(phase1)
    phase1Segment.setReadOnly(True)

    phase2Segment = canComponent.createIntegerSymbol("PHASE2", canNominalBitTimingMenu)
    phase2Segment.setLabel("Phase 2 Segment")
    phase2Segment.setMin(0)
    phase2Segment.setMax(7)
    phase2Segment.setDefaultValue(phase2)
    phase2Segment.setReadOnly(True)

    syncJumpWidth = canComponent.createIntegerSymbol("SJW", canNominalBitTimingMenu)
    syncJumpWidth.setLabel("Synchronization Jump Width")
    syncJumpWidth.setMin(0)
    syncJumpWidth.setMax(3)
    syncJumpWidth.setDefaultValue(sjw)
    syncJumpWidth.setReadOnly(True)

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

        canMailbox_MAM_Identifier = canComponent.createIntegerSymbol("CAN_MAM" + str(MBNum) + "_ID", canMailboxMenu)
        canMailbox_MAM_Identifier.setLabel("Message Acceptance Mask ID")
        canMailbox_MAM_Identifier.setMin(0)
        canMailbox_MAM_Identifier.setMax(536870911)
        canMailbox_MAM_Identifier.setDefaultValue(0)
        canMailbox_MAM_Identifier.setVisible((canMailbox_MMR_MOT.getValue() == 1 or
                                              canMailbox_MMR_MOT.getValue() == 2 or
                                              canMailbox_MMR_MOT.getValue() == 4))
        canMailbox_MAM_Identifier.setDependencies(MsgAcceptanceMsksymbolVisible, ["CAN_MMR" + str(MBNum) + "_MOT"])

    #Timestamp EOF Mode
    canTimestampEofMode = canComponent.createBooleanSymbol("TIMESTAMP_EOF_MODE", None)
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
