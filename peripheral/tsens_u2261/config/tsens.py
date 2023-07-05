# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2023 Microchip Technology Inc. and its subsidiaries.
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
import math
global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global InterruptVectorUpdate
global tsensInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateTSENSInterruptStatus(symbol, event):
    if tsensSym_INTENSET_RESRDY.getValue() == True or tsensSym_INTENSET_WINMON.getValue() == True:
        Database.setSymbolValue("core", InterruptVector, True, 2)
        Database.setSymbolValue("core", InterruptHandlerLock, True, 2)
        Database.setSymbolValue("core", InterruptHandler, tsensInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptVector, False, 2)
        Database.setSymbolValue("core", InterruptHandlerLock, False, 2)
        Database.setSymbolValue("core", InterruptHandler, tsensInstanceName.getValue() + "_Handler", 2)


def updateTSENSInterruptWarningStatus(symbol, event):
    if tsensSym_INTENSET_RESRDY.getValue() == True or tsensSym_INTENSET_WINMON.getValue() == True:
        if (Database.getSymbolValue("core", InterruptVectorUpdate) == True):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def updateTSENSClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tsensEvesysConfigure(symbol, event):
    if(event["id"] == "TSENS_WINDOW_OUTPUT_EVENT"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(tsensInstanceName.getValue())+"_WINMON_ACTIVE", event["value"], 2)

    if (tsensSym_CONV_TRIGGER.getValue() == "HW Event Trigger"):
        if (event["id"] == "TSENS_EVCTRL_START"):
            if (event["value"] > 0):
                Database.setSymbolValue("evsys", "USER_"+str(tsensInstanceName.getValue())+"_START_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(tsensInstanceName.getValue())+"_START_READY", False, 2)


def tsensEventInputVisibility(symbol, event):
    if (tsensSym_CONV_TRIGGER.getValue() != "HW Event Trigger"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tsensWindowVisible(symbol, event):
    if (event["value"] > 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tsensComponent):
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorUpdate
    global tsensInstanceName
    global InterruptVectorSecurity

    tsensInstanceName = tsensComponent.createStringSymbol("TSENS_INSTANCE_NAME", None)
    tsensInstanceName.setVisible(False)
    tsensInstanceName.setDefaultValue(tsensComponent.getID().upper())
    Log.writeInfoMessage("Running " + tsensInstanceName.getValue())

    # clock enable
    Database.setSymbolValue("core", tsensInstanceName.getValue() + "_CLOCK_ENABLE", True, 2) 

    # trigger
    global tsensSym_CONV_TRIGGER
    tsensSym_CONV_TRIGGER = tsensComponent.createComboSymbol("TSENS_CONV_TRIGGER", None, ["Free Run", "SW Trigger", "HW Event Trigger"])
    tsensSym_CONV_TRIGGER.setDefaultValue("Free Run")
    tsensSym_CONV_TRIGGER.setLabel("Select Conversion Trigger")

    tsensSym_START_EVENT = tsensComponent.createKeyValueSetSymbol("TSENS_EVCTRL_START", tsensSym_CONV_TRIGGER)
    tsensSym_START_EVENT.setLabel("Start Event Input")
    tsensSym_START_EVENT.setVisible(False)
    tsensSym_START_EVENT.setOutputMode("Value")
    tsensSym_START_EVENT.setDisplayMode("Description")
    tsensSym_START_EVENT.addKey("DISABLED", "0", "Disabled")
    tsensSym_START_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    tsensSym_START_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    tsensSym_START_EVENT.setDependencies(tsensEventInputVisibility, ["TSENS_CONV_TRIGGER"])

    global tsensSym_INTENSET_RESRDY
    tsensSym_INTENSET_RESRDY = tsensComponent.createBooleanSymbol("TSENS_INTENSET_RESRDY", None)
    tsensSym_INTENSET_RESRDY.setLabel("Enable Result Interrupt")
    
    tsensWindowMenu = tsensComponent.createMenuSymbol("TSENS_WINDOW_CONFIG_MENU", None)
    tsensWindowMenu.setLabel("Window Mode Configuration")

    # Configure mode for Window operation
    tsensSym_CTRLC_WINMODE = tsensComponent.createKeyValueSetSymbol("TSENS_CTRLC_WINMODE", tsensWindowMenu)
    tsensSym_CTRLC_WINMODE.setLabel("Select Window Monitor Mode")
    tsensSym_CTRLC_WINMODE.setDefaultValue(0)
    tsensSym_CTRLC_WINMODE.setOutputMode("Value")
    tsensSym_CTRLC_WINMODE.setDisplayMode("Description")
    tsensWindowConfigNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TSENS\"]/value-group@[name=\"TSENS_CTRLC__WINMODE\"]")
    tsensWindowConfigValues = []
    tsensWindowConfigValues = tsensWindowConfigNode.getChildren()
    for index in range (0 , len(tsensWindowConfigValues)):
        tsensSym_CTRLC_WINMODE.addKey(tsensWindowConfigValues[index].getAttribute("name"), tsensWindowConfigValues[index].getAttribute("value"),
        tsensWindowConfigValues[index].getAttribute("caption"))

    # Window upper threshold
    tsensSym_WINUT = tsensComponent.createIntegerSymbol("TSENS_WINUT", tsensWindowMenu)
    tsensSym_WINUT.setLabel("Window Upper Threshold")
    tsensSym_WINUT.setMin(0)
    tsensSym_WINUT.setMax(pow(2, 24))
    tsensSym_WINUT.setDefaultValue(1024)
    tsensSym_WINUT.setVisible(False)
    tsensSym_WINUT.setDependencies(tsensWindowVisible, ["TSENS_CTRLC_WINMODE"])

    # Window lower threshold
    tsensSym_WINLT = tsensComponent.createIntegerSymbol("TSENS_WINLT", tsensWindowMenu)
    tsensSym_WINLT.setLabel("Window Lower Threshold")
    tsensSym_WINLT.setMin(0)
    tsensSym_WINLT.setMax(pow(2, 24))
    tsensSym_WINLT.setDefaultValue(512)
    tsensSym_WINLT.setVisible(False)
    tsensSym_WINLT.setDependencies(tsensWindowVisible, ["TSENS_CTRLC_WINMODE"])

    global tsensSym_INTENSET_WINMON
    tsensSym_INTENSET_WINMON = tsensComponent.createBooleanSymbol("TSENS_INTENSET_WINMON", tsensWindowMenu)
    tsensSym_INTENSET_WINMON.setLabel("Enable Window Monitor Interrupt")
    tsensSym_INTENSET_WINMON.setDefaultValue(False)
    tsensSym_INTENSET_WINMON.setVisible(False)
    tsensSym_INTENSET_WINMON.setDependencies(tsensWindowVisible, ["TSENS_CTRLC_WINMODE"])

    # Enable Window Monitor Event Out
    tsensSym_HW_INP_EVENT = tsensComponent.createBooleanSymbol("TSENS_WINDOW_OUTPUT_EVENT", tsensWindowMenu)
    tsensSym_HW_INP_EVENT.setLabel("Enable Window Monitor Event Out")
    tsensSym_HW_INP_EVENT.setVisible(False)
    tsensSym_HW_INP_EVENT.setDependencies(tsensWindowVisible, ["TSENS_CTRLC_WINMODE"])

    tsensSleepMenu = tsensComponent.createMenuSymbol("TSENS_SLEEP_MENU", None)
    tsensSleepMenu.setLabel("Sleep Mode Configuration")

    # run in standby mode
    tsensSym_CTRLA_RUNSTDBY = tsensComponent.createBooleanSymbol("TSENS_CTRLA_RUNSTDBY", tsensSleepMenu)
    tsensSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")
    tsensSym_CTRLA_RUNSTDBY.setVisible(True)

    tsensSym_EVESYS_CONFIGURE = tsensComponent.createIntegerSymbol("TSENS_EVESYS_CONFIGURE", None)
    tsensSym_EVESYS_CONFIGURE.setVisible(False)
    tsensSym_EVESYS_CONFIGURE.setDependencies(tsensEvesysConfigure, \
        ["TSENS_WINDOW_OUTPUT_EVENT", "TSENS_CONV_TRIGGER", "TSENS_EVCTRL_START"])

    ############################################################################
    #### Dependency ####
    ############################################################################
    InterruptVector = tsensInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = tsensInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = tsensInstanceName.getValue()+ "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = tsensInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    tsensSym_UpdateInterruptStatus = tsensComponent.createBooleanSymbol("TSENS_INTERRUPT_STATUS", None)
    tsensSym_UpdateInterruptStatus.setDependencies(updateTSENSInterruptStatus, ["TSENS_INTENSET_RESRDY", "TSENS_INTENSET_WINMON"])
    tsensSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    tsensSym_IntEnComment = tsensComponent.createCommentSymbol("TSENS_INTERRUPT_ENABLE_COMMENT", None)
    tsensSym_IntEnComment.setVisible(False)
    tsensSym_IntEnComment.setLabel("Warning!!! "+tsensInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    tsensSym_IntEnComment.setDependencies(updateTSENSInterruptWarningStatus, ["core." + InterruptVectorUpdate, "TSENS_INTENSET_RESRDY", "TSENS_INTENSET_WINMON"])

    # Clock Warning status
    tsensSym_ClkEnComment = tsensComponent.createCommentSymbol("TSENS_CLOCK_ENABLE_COMMENT", None)
    tsensSym_ClkEnComment.setVisible(False)
    tsensSym_ClkEnComment.setLabel("Warning!!! " +tsensInstanceName.getValue()+" Clock is Disabled in Clock Manager")
    tsensSym_ClkEnComment.setDependencies(updateTSENSClockWarningStatus, ["core." + tsensInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tsensModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TSENS\"]")
    tsensModuleID = tsensModuleNode.getAttribute("id")

 
    tsensSym_CommonHeaderFile = tsensComponent.createFileSymbol("TSENS_COMMON_HEADER", None)
    tsensSym_CommonHeaderFile.setSourcePath("../peripheral/tsens_u2261/templates/plib_tsens_common.h.ftl")
    tsensSym_CommonHeaderFile.setOutputName("plib_tsens_common.h")
    tsensSym_CommonHeaderFile.setDestPath("/peripheral/tsens/")
    tsensSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/tsens/")
    tsensSym_CommonHeaderFile.setType("HEADER")
    tsensSym_CommonHeaderFile.setMarkup(True)


    tsensSym_HeaderFile = tsensComponent.createFileSymbol("TSENS_HEADER", None)
    tsensSym_HeaderFile.setSourcePath("../peripheral/tsens_u2261/templates/plib_tsens.h.ftl")
    tsensSym_HeaderFile.setOutputName("plib_"+tsensInstanceName.getValue().lower()+".h")
    tsensSym_HeaderFile.setDestPath("/peripheral/tsens/")
    tsensSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/tsens/")
    tsensSym_HeaderFile.setType("HEADER")
    tsensSym_HeaderFile.setMarkup(True)

    tsensSym_SourceFile = tsensComponent.createFileSymbol("TSENS_SOURCE", None)
    tsensSym_SourceFile.setSourcePath("../peripheral/tsens_u2261/templates/plib_tsens.c.ftl")
    tsensSym_SourceFile.setOutputName("plib_"+tsensInstanceName.getValue().lower()+".c")
    tsensSym_SourceFile.setDestPath("/peripheral/tsens/")
    tsensSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/tsens/")
    tsensSym_SourceFile.setType("SOURCE")
    tsensSym_SourceFile.setMarkup(True)

    tsensSym_SystemInitFile = tsensComponent.createFileSymbol("TSENS_SYS_INIT", None)
    tsensSym_SystemInitFile.setType("STRING")
    tsensSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tsensSym_SystemInitFile.setSourcePath("../peripheral/tsens_u2261/templates/system/initialization.c.ftl")
    tsensSym_SystemInitFile.setMarkup(True)

    tsensSym_SystemDefFile = tsensComponent.createFileSymbol("TSENS_SYS_DEF", None)
    tsensSym_SystemDefFile.setType("STRING")
    tsensSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tsensSym_SystemDefFile.setSourcePath("../peripheral/tsens_u2261/templates/system/definitions.h.ftl")
    tsensSym_SystemDefFile.setMarkup(True)
