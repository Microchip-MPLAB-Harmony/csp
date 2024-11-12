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

sdadcSym_SEQCTRL_SEQ = []

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global InterruptVectorUpdate
global sdadcInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateSDADCInterruptStatus(symbol, event):
    component = symbol.getComponent()
    if (component.getSymbolValue("SDADC_INTENSET_RESRDY") or component.getSymbolValue("SDADC_INTENSET_WINMON")):
        Database.setSymbolValue("core", InterruptVector, True, 2)
        Database.setSymbolValue("core", InterruptHandlerLock, True, 2)
        Database.setSymbolValue("core", InterruptHandler, sdadcInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptVector, False, 2)
        Database.setSymbolValue("core", InterruptHandlerLock, False, 2)
        Database.setSymbolValue("core", InterruptHandler, sdadcInstanceName.getValue() + "_Handler", 2)

def updateSDADCInterruptWarningStatus(symbol, event):
    component = symbol.getComponent()
    if (component.getSymbolValue("SDADC_INTENSET_RESRDY") or component.getSymbolValue("SDADC_INTENSET_WINMON")):
        if(Database.getSymbolValue("core", InterruptVectorUpdate) == False):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateSDADCClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def sdadcEvesysConfigure(symbol, event):
    if(event["id"] == "SDADC_EVCTRL_RESRDYEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+sdadcInstanceName.getValue()+"_RESRDY_ACTIVE", event["value"], 2)

    if(event["id"] == "SDADC_EVCTRL_WINMONEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+sdadcInstanceName.getValue()+"_WINMON_ACTIVE", event["value"], 2)

    if(sdadcSym_TRIGGER.getValue() == 2):
        if (event["id"] == "SDADC_EVCTRL_FLUSH"):
            if (event["value"] > 0):
                Database.setSymbolValue("evsys", "USER_"+str(sdadcInstanceName.getValue())+"_FLUSH_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(sdadcInstanceName.getValue())+"_FLUSH_READY", False, 2)
        if (event["id"] == "SDADC_EVCTRL_START"):
            if (event["value"] > 0):
                Database.setSymbolValue("evsys", "USER_"+str(sdadcInstanceName.getValue())+"_START_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(sdadcInstanceName.getValue())+"_START_READY", False, 2)


def sdadcCalcConvTime(symbol, event):
    clock_freq = Database.getSymbolValue("core", sdadcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = sdadcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    osr = sdadcSym_CTRLB_OSR.getSelectedKey()[3:]

    conv_time = float(((int(osr) * int(prescaler) * 4 * 1000000) / clock_freq))
    symbol.setLabel("**** Conversion Time is " + str(conv_time) + " uS ****")

def sdadcChannelVisible(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def sdadcMuxVisible(symbol, event):
    if(event["value"] == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def sdadcOptionVisible(symbol, event):
    if(event["value"] > 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def sdadcHWEventVisible(symbol, event):
    if (event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
###########################################################################################
####                                   SDADC Database Components
###########################################################################################

def instantiateComponent(sdadcComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorUpdate
    global sdadcInstanceName

    sdadcInstanceName = sdadcComponent.createStringSymbol("SDADC_INSTANCE_NAME", None)
    sdadcInstanceName.setVisible(False)
    sdadcInstanceName.setDefaultValue(sdadcComponent.getID().upper())
    Log.writeInfoMessage("Running " + sdadcInstanceName.getValue())

    #clock enable
    Database.setSymbolValue("core", sdadcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    #Prescaler Configuration
    global sdadcSym_CTRLB_PRESCALER
    sdadcSym_CTRLB_PRESCALER = sdadcComponent.createKeyValueSetSymbol("SDADC_CTRLB_PRESCALER", None)
    sdadcSym_CTRLB_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:CTRLB")
    sdadcSym_CTRLB_PRESCALER.setLabel("Select Prescaler")
    sdadcPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SDADC\"]/value-group@[name=\"SDADC_CTRLB__PRESCALER\"]")
    sdadcPrescalerValues = []
    sdadcPrescalerValues = sdadcPrescalerNode.getChildren()
    sdadcPrescalerDefaultValue = 0
    for index in range(len(sdadcPrescalerValues)):
        if (sdadcPrescalerValues[index].getAttribute("name") == "DIV2"):
            sdadcPrescalerDefaultValue = index
        sdadcSym_CTRLB_PRESCALER.addKey(sdadcPrescalerValues[index].getAttribute("name"), sdadcPrescalerValues[index].getAttribute("value"), \
            sdadcPrescalerValues[index].getAttribute("caption"))
    sdadcSym_CTRLB_PRESCALER.setDefaultValue(sdadcPrescalerDefaultValue)
    sdadcSym_CTRLB_PRESCALER.setOutputMode("Key")
    sdadcSym_CTRLB_PRESCALER.setDisplayMode("Description")

    #Over Sampling Ratio
    global sdadcSym_CTRLB_OSR
    sdadcSym_CTRLB_OSR = sdadcComponent.createKeyValueSetSymbol("SDADC_CTRLB_OSR", None)
    sdadcSym_CTRLB_OSR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:CTRLB")
    sdadcSym_CTRLB_OSR.setLabel("Over Sampling Ratio")
    sdadcSymOSRSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SDADC\"]/value-group@[name=\"SDADC_CTRLB__OSR\"]")
    sdadcSymOSRSelectionValues = []
    sdadcSymOSRSelectionValues = sdadcSymOSRSelectionNode.getChildren()
    sdadcOSRSelectionDefaultValue = 0
    for index in range(len(sdadcSymOSRSelectionValues)):
        if (sdadcSymOSRSelectionValues[index].getAttribute("name") == "OSR64"):
            sdadcOSRSelectionDefaultValue = index
        sdadcSym_CTRLB_OSR.addKey(sdadcSymOSRSelectionValues[index].getAttribute("name"), sdadcSymOSRSelectionValues[index].getAttribute("value"),\
            sdadcSymOSRSelectionValues[index].getAttribute("caption"))
    sdadcSym_CTRLB_OSR.setDefaultValue(sdadcOSRSelectionDefaultValue)
    sdadcSym_CTRLB_OSR.setOutputMode("Key")
    sdadcSym_CTRLB_OSR.setDisplayMode("Description")

    clock_freq = Database.getSymbolValue("core", sdadcInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = sdadcSym_CTRLB_PRESCALER.getSelectedKey()[3:]
    osr = sdadcSym_CTRLB_OSR.getSelectedKey()[3:]
    conv_time = float(((int(osr) * int(prescaler) * 4 * 1000000) / clock_freq))

    sdadcSym_CONV_TIME = sdadcComponent.createCommentSymbol("SDADC_CONV_TIME", None)
    sdadcSym_CONV_TIME.setLabel("**** Conversion Time is " + str(conv_time) +" uS ****")
    sdadcSym_CONV_TIME.setDependencies(sdadcCalcConvTime, \
        ["core."+sdadcInstanceName.getValue()+"_CLOCK_FREQUENCY", "SDADC_CTRLB_OSR", "SDADC_CTRLB_PRESCALER"])

    #Reference Selection
    sdadcSym_REFCTRL_REFSEL = sdadcComponent.createKeyValueSetSymbol("SDADC_REFCTRL_REFSEL", None)
    sdadcSym_REFCTRL_REFSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:REFCTRL")
    sdadcSym_REFCTRL_REFSEL.setLabel("Select Reference")
    sdadcReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SDADC\"]/value-group@[name=\"SDADC_REFCTRL__REFSEL\"]")
    sdadcReferenceValues = []
    sdadcReferenceValues = sdadcReferenceNode.getChildren()
    sdadcReferenceDefaultValue = 0
    for index in range(len(sdadcReferenceValues)):
        if (sdadcReferenceValues[index].getAttribute("name") == "INTREF"):
            sdadcReferenceDefaultValue = index
        sdadcSym_REFCTRL_REFSEL.addKey(sdadcReferenceValues[index].getAttribute("name"), sdadcReferenceValues[index].getAttribute("value"), \
            sdadcReferenceValues[index].getAttribute("caption"))
    sdadcSym_REFCTRL_REFSEL.setDefaultValue(sdadcReferenceDefaultValue)
    sdadcSym_REFCTRL_REFSEL.setOutputMode("Key")
    sdadcSym_REFCTRL_REFSEL.setDisplayMode("Description")

    #Trigger selection
    global sdadcSym_TRIGGER
    sdadcSym_TRIGGER = sdadcComponent.createKeyValueSetSymbol("SDADC_TRIGGER", None)
    sdadcSym_TRIGGER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:%NOREGISTER%")
    sdadcSym_TRIGGER.setLabel("Select Conversion Trigger")
    sdadcSym_TRIGGER.addKey("FREE_RUN", "0", "Free Run")
    sdadcSym_TRIGGER.addKey("SW_TRIGGER", "1", "Software Trigger")
    sdadcSym_TRIGGER.addKey("HW_TRIGGER", "2", "Hardware Event Trigger")
    sdadcSym_TRIGGER.setDefaultValue(0)
    sdadcSym_TRIGGER.setOutputMode("Value")
    sdadcSym_TRIGGER.setDisplayMode("Description")

    sdadcSym_FLUSH_EVENT = sdadcComponent.createKeyValueSetSymbol("SDADC_EVCTRL_FLUSH", sdadcSym_TRIGGER)
    sdadcSym_FLUSH_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:EVCTRL")
    sdadcSym_FLUSH_EVENT.setLabel("Flush Event Input")
    sdadcSym_FLUSH_EVENT.setVisible(False)
    sdadcSym_FLUSH_EVENT.setOutputMode("Value")
    sdadcSym_FLUSH_EVENT.setDisplayMode("Description")
    sdadcSym_FLUSH_EVENT.addKey("DISABLED", "0", "Disabled")
    sdadcSym_FLUSH_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    sdadcSym_FLUSH_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    sdadcSym_FLUSH_EVENT.setDependencies(sdadcHWEventVisible, ["SDADC_TRIGGER"])

    sdadcSym_START_EVENT = sdadcComponent.createKeyValueSetSymbol("SDADC_EVCTRL_START", sdadcSym_TRIGGER)
    sdadcSym_START_EVENT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:EVCTRL")
    sdadcSym_START_EVENT.setLabel("Start Event Input")
    sdadcSym_START_EVENT.setVisible(False)
    sdadcSym_START_EVENT.setOutputMode("Value")
    sdadcSym_START_EVENT.setDisplayMode("Description")
    sdadcSym_START_EVENT.addKey("DISABLED", "0", "Disabled")
    sdadcSym_START_EVENT.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
    sdadcSym_START_EVENT.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
    sdadcSym_START_EVENT.setDependencies(sdadcHWEventVisible, ["SDADC_TRIGGER"])

    # Auto sequencer
    sdadcSym_AUTO_SEQUENCE = sdadcComponent.createBooleanSymbol("SDADC_AUTO_SEQUENCE", None)
    sdadcSym_AUTO_SEQUENCE.setLabel("Enable Automatic Sequencing")
    sdadcSym_AUTO_SEQUENCE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:%NOREGISTER%")
    sdadcSym_AUTO_SEQUENCE.setVisible(False)
    sdadcSym_AUTO_SEQUENCE.setDependencies(sdadcOptionVisible, ["SDADC_TRIGGER"])

    for channelID in range(0, 3):
        #Enable channel in sequencer
        sdadcSym_SEQCTRL_SEQ.append(channelID)
        sdadcSym_SEQCTRL_SEQ[channelID] = sdadcComponent.createBooleanSymbol("SDADC_SEQCTRL_SEQ"+str(channelID), sdadcSym_AUTO_SEQUENCE)
        sdadcSym_SEQCTRL_SEQ[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:SEQCTRL")
        sdadcSym_SEQCTRL_SEQ[channelID].setLabel("Enable Channel " + str(channelID))
        sdadcSym_SEQCTRL_SEQ[channelID].setVisible(False)
        sdadcSym_SEQCTRL_SEQ[channelID].setDependencies(sdadcChannelVisible, ["SDADC_AUTO_SEQUENCE"])

    #MUX Selection
    sdadcSym_INPUTCTRL_MUXSEL = sdadcComponent.createKeyValueSetSymbol("SDADC_INPUTCTRL_MUXSEL", None)
    sdadcSym_INPUTCTRL_MUXSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:INPUTCTRL")
    sdadcSym_INPUTCTRL_MUXSEL.setLabel("MUX Selection")
    sdadcMuxSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SDADC\"]/value-group@[name=\"SDADC_INPUTCTRL__MUXSEL\"]")
    sdadcMuxSelectionValues = []
    sdadcMuxSelectionValues = sdadcMuxSelectionNode.getChildren()
    sdadcMuxSelectionDefaultValue = 0
    for index in range(len(sdadcMuxSelectionValues)):
        if (sdadcMuxSelectionValues[index].getAttribute("name") == "AIN0"):
            sdadcMuxSelectionDefaultValue = index
        sdadcSym_INPUTCTRL_MUXSEL.addKey(sdadcMuxSelectionValues[index].getAttribute("name"), sdadcMuxSelectionValues[index].getAttribute("value"), \
            sdadcMuxSelectionValues[index].getAttribute("caption"))
    sdadcSym_INPUTCTRL_MUXSEL.setDefaultValue(sdadcMuxSelectionDefaultValue)
    sdadcSym_INPUTCTRL_MUXSEL.setOutputMode("Key")
    sdadcSym_INPUTCTRL_MUXSEL.setDisplayMode("Description")
    sdadcSym_INPUTCTRL_MUXSEL.setDependencies(sdadcMuxVisible, ["SDADC_AUTO_SEQUENCE"])

    #result ready interrupt
    global sdadcSym_INTENSET_RESRDY
    sdadcSym_INTENSET_RESRDY = sdadcComponent.createBooleanSymbol("SDADC_INTENSET_RESRDY", None)
    sdadcSym_INTENSET_RESRDY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:INTENSET")
    sdadcSym_INTENSET_RESRDY.setLabel("Enable Result Ready Interrupt")

    #result ready event out
    sdadcSym_EVCTRL_RESRDYEO = sdadcComponent.createBooleanSymbol("SDADC_EVCTRL_RESRDYEO", None)
    sdadcSym_EVCTRL_RESRDYEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:EVCTRL")
    sdadcSym_EVCTRL_RESRDYEO.setLabel("Enable Result Ready Event Out")

    sdadcSym_WINMODE_MENU = sdadcComponent.createMenuSymbol("SDADC_WINMODE_MENU", None)
    sdadcSym_WINMODE_MENU.setLabel("Window Monitor Configurations")

    #Window monitor mode
    sdadcSym_WINCTRL_WINMODE = sdadcComponent.createKeyValueSetSymbol("SDADC_WINCTRL_WINMODE", sdadcSym_WINMODE_MENU)
    sdadcSym_WINCTRL_WINMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:WINCTRL")
    sdadcSym_WINCTRL_WINMODE.setLabel("Select Window Monitor Mode")
    sdadcSym_WINCTRL_WINMODE.addKey("DISABLED", "0", "Disabled")
    sdadcSym_WINCTRL_WINMODE.addKey("ABOVE", "1", "Result is greater than lower threshold")
    sdadcSym_WINCTRL_WINMODE.addKey("BELOW", "2", "Result is lower than upper threshold")
    sdadcSym_WINCTRL_WINMODE.addKey("INSIDE", "3", "Result is between lower and upper threshold")
    sdadcSym_WINCTRL_WINMODE.addKey("OUTSIDE", "4", "Result is outside lower and upper threshold")
    sdadcSym_WINCTRL_WINMODE.setOutputMode("Value")
    sdadcSym_WINCTRL_WINMODE.setDisplayMode("Description")

    #Upper threshold value
    sdadcSym_WINUT = sdadcComponent.createIntegerSymbol("SDADC_WINUT", sdadcSym_WINCTRL_WINMODE)
    sdadcSym_WINUT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:WINUT")
    sdadcSym_WINUT.setLabel("Window Upper Threshold")
    sdadcSym_WINUT.setDefaultValue(10000)
    sdadcSym_WINUT.setMin(-32768)
    sdadcSym_WINUT.setMax(32767)
    sdadcSym_WINUT.setVisible(False)
    sdadcSym_WINUT.setDependencies(sdadcOptionVisible, ["SDADC_WINCTRL_WINMODE"])

    #Lower threshold value
    sdadcSym_WINLT = sdadcComponent.createIntegerSymbol("SDADC_WINLT", sdadcSym_WINCTRL_WINMODE)
    sdadcSym_WINLT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:WINLT")
    sdadcSym_WINLT.setLabel("Window Lower Threshold")
    sdadcSym_WINLT.setDefaultValue(5000)
    sdadcSym_WINLT.setMin(-32768)
    sdadcSym_WINLT.setMax(32767)
    sdadcSym_WINLT.setVisible(False)
    sdadcSym_WINLT.setDependencies(sdadcOptionVisible, ["SDADC_WINCTRL_WINMODE"])

    #window monitor event
    sdadcSym_INTENSET_WINMON = sdadcComponent.createBooleanSymbol("SDADC_INTENSET_WINMON", sdadcSym_WINCTRL_WINMODE)
    sdadcSym_INTENSET_WINMON.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:INTENSET")
    sdadcSym_INTENSET_WINMON.setLabel("Enable Window Monitor Interrupt")
    sdadcSym_INTENSET_WINMON.setVisible(False)
    sdadcSym_INTENSET_WINMON.setDependencies(sdadcOptionVisible, ["SDADC_WINCTRL_WINMODE"])

    #window monitor event out
    sdadcSym_EVCTRL_WINMONEO = sdadcComponent.createBooleanSymbol("SDADC_EVCTRL_WINMONEO", sdadcSym_WINCTRL_WINMODE)
    sdadcSym_EVCTRL_WINMONEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:EVCTRL")
    sdadcSym_EVCTRL_WINMONEO.setLabel("Enable Window Monitor Event Out")
    sdadcSym_EVCTRL_WINMONEO.setVisible(False)
    sdadcSym_EVCTRL_WINMONEO.setDependencies(sdadcOptionVisible, ["SDADC_WINCTRL_WINMODE"])

    sdadcSym_EVESYS_CONFIGURE = sdadcComponent.createIntegerSymbol("SDADC_EVESYS_CONFIGURE", None)
    sdadcSym_EVESYS_CONFIGURE.setVisible(False)
    sdadcSym_EVESYS_CONFIGURE.setDependencies(sdadcEvesysConfigure, \
        ["SDADC_EVCTRL_WINMONEO", "SDADC_EVCTRL_RESRDYEO", "SDADC_EVCTRL_FLUSH", "SDADC_EVCTRL_START"])

    #Sleep configurations
    sdadcSym_Sleep_Menu = sdadcComponent.createMenuSymbol("SDADC_SLEEP", None)
    sdadcSym_Sleep_Menu.setLabel("Sleep Configurations")

    #Run StandBy
    sdadcSym_CTRLA_RUNSTDBY = sdadcComponent.createBooleanSymbol("SDADC_RUNSTDBY", sdadcSym_Sleep_Menu)
    sdadcSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:%NOREGISTER%")
    sdadcSym_CTRLA_RUNSTDBY.setLabel("Run During Standby")

    #On Demand
    sdadcSym_CTRLA_ONDEMAND = sdadcComponent.createBooleanSymbol("SDADC_ONDEMAND", sdadcSym_Sleep_Menu)
    sdadcSym_CTRLA_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdadc_u2260;register:%NOREGISTER%")
    sdadcSym_CTRLA_ONDEMAND.setLabel("On Demand Control")

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = sdadcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = sdadcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = sdadcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = sdadcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    sdadcSym_UpdateInterruptStatus = sdadcComponent.createBooleanSymbol("SDADC_INTERRUPT_STATUS", None)
    sdadcSym_UpdateInterruptStatus.setDependencies(updateSDADCInterruptStatus, ["SDADC_INTENSET_RESRDY", "SDADC_INTENSET_WINMON"])
    sdadcSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    sdadcSym_IntEnComment = sdadcComponent.createCommentSymbol("SDADC_INTERRUPT_ENABLE_COMMENT", None)
    sdadcSym_IntEnComment.setVisible(False)
    sdadcSym_IntEnComment.setLabel("Warning!!! SDADC Interrupt is Disabled in Interrupt Manager")
    sdadcSym_IntEnComment.setDependencies(updateSDADCInterruptWarningStatus, ["core." + InterruptVectorUpdate, "SDADC_INTENSET_RESRDY", "SDADC_INTENSET_WINMON"])

    # Clock Warning status
    sdadcSym_ClkEnComment = sdadcComponent.createCommentSymbol("SDADC_CLOCK_ENABLE_COMMENT", None)
    sdadcSym_ClkEnComment.setLabel("Warning!!! SDADC Peripheral Clock is Disabled in Clock Manager")
    sdadcSym_ClkEnComment.setVisible(False)
    sdadcSym_ClkEnComment.setDependencies(updateSDADCClockWarningStatus, ["core."+sdadcInstanceName.getValue()+"_CLOCK_ENABLE"])

###########################################################################################################################################
########################                                         Code Generation                                   ########################
###########################################################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sdadcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SDADC\"]")
    sdadcModuleID = sdadcModuleNode.getAttribute("id")

    # Global Header File
    sdadcGlobalHeaderFile = sdadcComponent.createFileSymbol("SDADC_GLOBAL_HEADER", None)
    sdadcGlobalHeaderFile.setSourcePath("../peripheral/sdadc_u2260/templates/plib_sdadc_common.h")
    sdadcGlobalHeaderFile.setOutputName("plib_sdadc_common.h")
    sdadcGlobalHeaderFile.setDestPath("/peripheral/sdadc/")
    sdadcGlobalHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdadc/")
    sdadcGlobalHeaderFile.setType("HEADER")
    sdadcGlobalHeaderFile.setMarkup(False)

    # Instance Header File
    sdadcHeaderFile = sdadcComponent.createFileSymbol("SDADC_HEADER", None)
    sdadcHeaderFile.setSourcePath("../peripheral/sdadc_u2260/templates/plib_sdadc.h.ftl")
    sdadcHeaderFile.setOutputName("plib_"+sdadcInstanceName.getValue().lower()+".h")
    sdadcHeaderFile.setDestPath("/peripheral/sdadc/")
    sdadcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdadc/")
    sdadcHeaderFile.setType("HEADER")
    sdadcHeaderFile.setMarkup(True)

    # Source File
    sdadcSourceFile = sdadcComponent.createFileSymbol("SDADC_SOURCE", None)
    sdadcSourceFile.setSourcePath("../peripheral/sdadc_u2260/templates/plib_sdadc.c.ftl")
    sdadcSourceFile.setOutputName("plib_"+sdadcInstanceName.getValue().lower()+".c")
    sdadcSourceFile.setDestPath("/peripheral/sdadc/")
    sdadcSourceFile.setProjectPath("config/" + configName + "/peripheral/sdadc/")
    sdadcSourceFile.setType("SOURCE")
    sdadcSourceFile.setMarkup(True)

    #System Initialization
    sdadcSystemInitFile = sdadcComponent.createFileSymbol("SDADC_SYS_INIT", None)
    sdadcSystemInitFile.setType("STRING")
    sdadcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sdadcSystemInitFile.setSourcePath("../peripheral/sdadc_u2260/templates/system/initialization.c.ftl")
    sdadcSystemInitFile.setMarkup(True)

    #System Definition
    sdadcSystemDefFile = sdadcComponent.createFileSymbol("SDADC_SYS_DEF", None)
    sdadcSystemDefFile.setType("STRING")
    sdadcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sdadcSystemDefFile.setSourcePath("../peripheral/sdadc_u2260/templates/system/definitions.h.ftl")
    sdadcSystemDefFile.setMarkup(True)
