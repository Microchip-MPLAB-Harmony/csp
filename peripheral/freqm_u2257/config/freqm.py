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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global freqmInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateFREQMInterruptStatus(symbol, event):

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, freqmInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, freqmInstanceName.getValue() + "_Handler", 2)

def updateFREQMInterruptWarningStatus(symbol, event):
    if freqmSym_INTERRUPTMODE.getValue() == True:
        symbol.setVisible(event["value"])

def updateFREQMClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

def updateMeasurementTime(symbol, event):
    component = symbol.getComponent()
    refClockFrequency = float(Database.getSymbolValue("core", freqmInstanceName.getValue() + "_REF_CLOCK_FREQUENCY"))
    refClockDivider = component.getSymbolByID("FREQM_REF_CLK_DIV").getValue()
    refClockCycles = float(component.getSymbolByID("FREQM_REF_CLK_CYCLES").getSelectedValue())

    if refClockDivider == True:
        refClockFrequency= refClockFrequency/8

    if refClockFrequency != 0:
        measurementTime = (1000 * refClockCycles) / refClockFrequency
        measurementTime = format(measurementTime, '.3f')
        component.getSymbolByID("FREQM_REF_CLOCK_FREQUENCY_COMMENT").setLabel("*** Reference Clock Frequency " + str(refClockFrequency) + " Hz ***")
    else:
        measurementTime = 0
        component.getSymbolByID("FREQM_REF_CLOCK_FREQUENCY_COMMENT").setLabel("Warning!!! Reference Clock Frequency 0 Hz ***")

    component.getSymbolByID("FREQ_MEASUREMENT_TIME_COMMENT").setLabel("*** Measurement Time " + str(measurementTime) + " mS ***")
    component.getSymbolByID("FREQM_REF_CLOCK_FREQUENCY").setValue(int(refClockFrequency),2)

    for resultRightShift in range(8):
        if refClockCycles % (2 << resultRightShift) != 0:
            break

    component.getSymbolByID("FREQM_RESULT_RIGHT_SHIFT").setValue(resultRightShift, 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(freqmComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global freqmInstanceName
    global freqmSym_INTERRUPTMODE

    freqmInstanceName = freqmComponent.createStringSymbol("FREQM_INSTANCE_NAME", None)
    freqmInstanceName.setVisible(False)
    freqmInstanceName.setDefaultValue(freqmComponent.getID().upper())

    Log.writeInfoMessage("Running " + freqmInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", freqmInstanceName.getValue() + "_REF_CLOCK_ENABLE", True, 2)
    Database.setSymbolValue("core", freqmInstanceName.getValue() + "_MSR_CLOCK_ENABLE", True, 2)

    #FREQM Interrupt Mode
    freqmSym_INTERRUPTMODE = freqmComponent.createBooleanSymbol("FREQM_INTERRUPT_MODE", None)
    freqmSym_INTERRUPTMODE.setLabel("Enable Interrupt ?")
    freqmSym_INTERRUPTMODE.setDescription("Selection of polled or Interrupt Mode")

    #FREQM Selection of the division for the Reference Clock
    freqmSym_CFGA_DIVREF = freqmComponent.createBooleanSymbol("FREQM_REF_CLK_DIV", None)
    freqmSym_CFGA_DIVREF.setLabel("Divide reference clock by 8")
    freqmSym_CFGA_DIVREF.setDescription("selection of either refclk1 or refclk8")
    freqmSym_CFGA_DIVREF.setVisible(False)

    freqmRef8 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FREQM"]/register-group@[name="FREQM"]/register@[name="CFGA"]')
    for id in range(0,len(freqmRef8.getChildren())):
        if freqmRef8.getChildren()[id].getAttribute("name") == "DIVREF":
            freqmSym_CFGA_DIVREF.setVisible(True)

    #FREQM Reference Clock Frequency
    refClockFrequency = int(Database.getSymbolValue("core", freqmInstanceName.getValue() + "_REF_CLOCK_FREQUENCY"))
    freqmSym_RefClkFrequency = freqmComponent.createIntegerSymbol("FREQM_REF_CLOCK_FREQUENCY", None)
    freqmSym_RefClkFrequency.setDefaultValue(refClockFrequency)
    freqmSym_RefClkFrequency.setVisible(False)

    freqmSym_RefClkFrequency_Comment = freqmComponent.createCommentSymbol("FREQM_REF_CLOCK_FREQUENCY_COMMENT", None)
    if refClockFrequency != 0:
        freqmSym_RefClkFrequency_Comment.setLabel("*** Reference Clock Frequency " + str(refClockFrequency) + " Hz ***")
    else:
        freqmSym_RefClkFrequency_Comment.setLabel("Warning!!! Reference Clock Frequency 0 Hz ***")

    #FREQM Selection of the Reference Clock Cycles
    freqmSym_CFGA_REFNUM = freqmComponent.createKeyValueSetSymbol("FREQM_REF_CLK_CYCLES", None)
    freqmSym_CFGA_REFNUM.setLabel("Measurement Time (Ref Cycles)")
    freqmSym_CFGA_REFNUM.setDescription(" Measurement Time specified in terms of reference clock cycles")
    freqmSym_CFGA_REFNUM.addKey("1_CLOCK", "1", "1 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("2_CLOCK", "2", "2 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("4_CLOCK", "4", "4 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("8_CLOCK", "8", "8 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("16_CLOCK", "16", "16 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("32_CLOCK", "32", "32 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("64_CLOCK", "64", "64 Clock Cycles")
    freqmSym_CFGA_REFNUM.addKey("128_CLOCK", "128", "128 Clock Cycles")
    freqmSym_CFGA_REFNUM.setOutputMode("Value")
    freqmSym_CFGA_REFNUM.setDisplayMode("Description")
    freqmSym_CFGA_REFNUM.setDefaultValue(0)

    freqmSym_RightshiftResult = freqmComponent.createIntegerSymbol("FREQM_RESULT_RIGHT_SHIFT", None)
    freqmSym_RightshiftResult.setVisible(False)
    freqmSym_RightshiftResult.setDefaultValue(0)

    if refClockFrequency != 0:
        measurementTime = 1000/ float(refClockFrequency)
        measurementTime = format(measurementTime, '.3f')
    else:
        measurementTime = 0

    freqmSym_MeasurementTime_Comment = freqmComponent.createCommentSymbol("FREQ_MEASUREMENT_TIME_COMMENT", None)
    freqmSym_MeasurementTime_Comment.setLabel("*** Measurement Time " + str(measurementTime) + " mS ***")
    freqmSym_MeasurementTime_Comment.setDependencies(updateMeasurementTime, ["core." + freqmInstanceName.getValue() + "_REF_CLOCK_FREQUENCY","FREQM_REF_CLK_CYCLES", "FREQM_REF_CLK_DIV"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = freqmInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = freqmInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = freqmInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = freqmInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    freqmSym_UpdateInterruptStatus = freqmComponent.createBooleanSymbol("FREQM_INTERRUPT_STATUS", None)
    freqmSym_UpdateInterruptStatus.setVisible(False)
    freqmSym_UpdateInterruptStatus.setDependencies(updateFREQMInterruptStatus, ["FREQM_INTERRUPT_MODE"])

    # Interrupt Warning status
    freqmSym_IntEnComment = freqmComponent.createCommentSymbol("FREQM_INTERRUPT_ENABLE_COMMENT", None)
    freqmSym_IntEnComment.setVisible(False)
    freqmSym_IntEnComment.setLabel("Warning!!! FREQM Interrupt is Disabled in Interrupt Manager")
    freqmSym_IntEnComment.setDependencies(updateFREQMInterruptWarningStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    freqmSym_REFClkEnComment = freqmComponent.createCommentSymbol("FREQM_REF_CLOCK_ENABLE_COMMENT", None)
    freqmSym_REFClkEnComment.setLabel("Warning!!! FREQM Peripheral Reference Clock is Disabled in Clock Manager")
    freqmSym_REFClkEnComment.setVisible(False)
    freqmSym_REFClkEnComment.setDependencies(updateFREQMClockWarningStatus, ["core." + freqmInstanceName.getValue() + "_REF_CLOCK_ENABLE"])

    freqmSym_MSRClkEnComment = freqmComponent.createCommentSymbol("FREQM_MSR_CLOCK_ENABLE_COMMENT", None)
    freqmSym_MSRClkEnComment.setLabel("Warning!!! FREQM Peripheral Measurement Clock is Disabled in Clock Manager")
    freqmSym_MSRClkEnComment.setVisible(False)
    freqmSym_MSRClkEnComment.setDependencies(updateFREQMClockWarningStatus, ["core." + freqmInstanceName.getValue() + "_MSR_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    freqmModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FREQM\"]")
    freqmModuleID = freqmModuleNode.getAttribute("id")

    freqmSym_HeaderFile = freqmComponent.createFileSymbol("FREQM_HEADER", None)
    freqmSym_HeaderFile.setSourcePath("../peripheral/freqm_u2257/templates/plib_freqm.h.ftl")
    freqmSym_HeaderFile.setOutputName("plib_" + freqmInstanceName.getValue().lower() + ".h")
    freqmSym_HeaderFile.setDestPath("/peripheral/freqm/")
    freqmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/freqm/")
    freqmSym_HeaderFile.setType("HEADER")
    freqmSym_HeaderFile.setMarkup(True)

    freqmSym_SourceFile = freqmComponent.createFileSymbol("FREQM_SOURCE", None)
    freqmSym_SourceFile.setSourcePath("../peripheral/freqm_u2257/templates/plib_freqm.c.ftl")
    freqmSym_SourceFile.setOutputName("plib_" + freqmInstanceName.getValue().lower() + ".c")
    freqmSym_SourceFile.setDestPath("/peripheral/freqm/")
    freqmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/freqm/")
    freqmSym_SourceFile.setType("SOURCE")
    freqmSym_SourceFile.setMarkup(True)

    freqmSystemInitFile = freqmComponent.createFileSymbol("FREQM_SYS_INIT", None)
    freqmSystemInitFile.setType("STRING")
    freqmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    freqmSystemInitFile.setSourcePath("../peripheral/freqm_u2257/templates/system/initialization.c.ftl")
    freqmSystemInitFile.setMarkup(True)

    freqmSystemDefFile = freqmComponent.createFileSymbol("FREQM_SYS_DEF", None)
    freqmSystemDefFile.setType("STRING")
    freqmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    freqmSystemDefFile.setSourcePath("../peripheral/freqm_u2257/templates/system/definitions.h.ftl")
    freqmSystemDefFile.setMarkup(True)
