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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def menuVisiblity(symbol, event):
    symbol.setVisible(not bool(event["value"]))

def refreshVisibility(symbol, event):
    symbol.setVisible(not bool(event["value"] > 0))

def updateDACClockWarringStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def manageEvent(event, eventComp, value):
    channel = int(event.split("_")[3][-1])
    if Database.getSymbolValue(eventComp, "DAC_CHANNEL_" + str(channel) + "_ENABLE"):
        if "RESRDYEO" in event:
            status = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_RESRDYEO" + str(channel))
            statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE")
            if statusEvent != status:
                Database.setSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE", status, 2)
        elif "EMPTYEO" in event:
            status = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_EMPTYEO" + str(channel))
            statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE")
            if statusEvent != status:
                Database.setSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE", status, 2)
        else:
            status = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_STARTEI" + str(channel))
            statusEvent = Database.getSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY")
            if statusEvent != status:
                Database.setSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY", status, 2)

def restoreEvents(channel, eventComp):
    resrdyStatus = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_RESRDYEO" + str(channel))
    emptyStatus = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_EMPTYEO" + str(channel))
    startStatus = Database.getSymbolValue(eventComp, "DAC_CHANNEL_EVENT_STARTEI" + str(channel))


    statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE")
    if statusEvent != resrdyStatus:
        Database.setSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE", resrdyStatus, 2)
    statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE")
    if statusEvent != emptyStatus:
        Database.setSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE", emptyStatus, 2)
    statusEvent = Database.getSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY")
    if statusEvent != startStatus:
        Database.setSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY", startStatus, 2)

def disableEvents(channel):
    global evctrlMap
    statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE")
    if statusEvent:
        Database.setSymbolValue("evsys", "GENERATOR_DAC_RESRDY_" + str(channel) + "_ACTIVE", False, 2)
    statusEvent = Database.getSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE")
    if statusEvent:
        Database.setSymbolValue("evsys", "GENERATOR_DAC_EMPTY_" + str(channel) + "_ACTIVE", False, 2)
    statusEvent = Database.getSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY")
    if statusEvent:
        Database.setSymbolValue("evsys", "USER_DAC_START_" + str(channel) + "_READY", False, 2)

def evsysSetup(symbol, event):
    global evctrlMap
    if event["id"] == "DAC_OPERATING_MODE":
        mode = event["value"]
        if mode == 1:
            disableEvents(1)
        else:
            restoreEvents(1, event["namespace"])

    elif "_ENABLE" in event["id"]:
        channel = int(event["id"].split("_")[2])
        if event["value"]:
            restoreEvents(channel, event["namespace"])
        else:
            disableEvents(channel)

    else:
        manageEvent(event["id"], event["namespace"], event["value"])



################################################################################
########                        DAC Data Base Components               #########
################################################################################

def instantiateComponent(dacComponent):

    evctrldep = []

    dacInstanceName = dacComponent.createStringSymbol("DAC_INSTANCE_NAME", None)
    dacInstanceName.setVisible(False)
    dacInstanceName.setDefaultValue(dacComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", dacInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    
    dacMode = dacComponent.createKeyValueSetSymbol("DAC_OPERATING_MODE", None)
    dacMode.setLabel("Select DAC Output Mode")
    dacMode.addKey("SINGLE_ENDED", "0", "Single-Ended Output")
    dacMode.addKey("DIFFERENTIAL", "1", "Differential Output")
    dacMode.setOutputMode("Key")
    dacMode.setDisplayMode("Description")
    dacMode.setDefaultValue(0)
    evctrldep.append("DAC_OPERATING_MODE")

    dacRefSelNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DAC"]/value-group@[name="DAC_CTRLB__REFSEL"]')
    dacRefSelValues = dacRefSelNode.getChildren()

    dacRefSel = dacComponent.createKeyValueSetSymbol("DAC_REFSEL", None)
    dacRefSel.setLabel("Reference Selection for DAC0/1")
    for index in range(0, len(dacRefSelValues)):
        dacRefSelKey = dacRefSelValues[index].getAttribute("name")
        dacRefSelValue = dacRefSelValues[index].getAttribute("value")
        dacRefSelCaption = dacRefSelValues[index].getAttribute("caption")
        dacRefSel.addKey(dacRefSelKey, dacRefSelValue, dacRefSelCaption)
    dacRefSel.setOutputMode("Value")
    dacRefSel.setDisplayMode("Description")
    dacRefSel.setDefaultValue(0)

    numChannels = 0
    numChannelNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DAC"]/register-group/register@[name="INTENSET"]')
    numChannelValues = numChannelNode.getChildren()
    for index in range(0,len(numChannelValues)):
        if "RESRDY" in numChannelValues[index].getAttribute("name"):
            numChannels = numChannels + 1

    for channel in range(0, numChannels):
        channelEnable = dacComponent.createBooleanSymbol("DAC_CHANNEL_" + str(channel) + "_ENABLE", None)
        channelEnable.setLabel("Enable DAC CHANNEL " +  str(channel))
        if channel % 2   == 1:
            channelEnable.setDependencies(menuVisiblity, ["DAC_OPERATING_MODE"])
        evctrldep.append("DAC_CHANNEL_" + str(channel) + "_ENABLE")

        channelMenu = dacComponent.createMenuSymbol("DAC_MENU" + str(channel), channelEnable)
        channelMenu.setLabel("DAC CHANNEL " +  str(channel) + " Configuration")

        channelSpeedNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DAC"]/value-group@[name="DAC_DACCTRL__CCTRL"]')
        channelSpeedValues = channelSpeedNode.getChildren()

        channelSpeed = dacComponent.createKeyValueSetSymbol("DAC_CHANNEL_" + str(channel) + "_SPEED", channelMenu)
        channelSpeed.setLabel("Conversion speed")
        for index in range(0, len(channelSpeedValues)):
            channelSpeedKey = channelSpeedValues[index].getAttribute("name")
            channelSpeedValue = channelSpeedValues[index].getAttribute("value")
            channelSpeedCaption = channelSpeedValues[index].getAttribute("caption")
            channelSpeed.addKey(channelSpeedKey, channelSpeedValue, channelSpeedCaption)
        channelSpeed.setOutputMode("Value")
        channelSpeed.setDisplayMode("Description")
        channelSpeed.setDefaultValue(0)

        channelFilter = dacComponent.createBooleanSymbol("DAC_CHANNEL_" + str(channel) + "_FILTER", channelMenu)
        channelFilter.setLabel("Enable External Filter")

        channelDataAdjustment = dacComponent.createKeyValueSetSymbol("DAC_DATA_ADJUSTMENT" + str(channel) , channelMenu)
        channelDataAdjustment.setLabel("DAC Data register Adjustment")
        channelDataAdjustment.addKey("RIGHT-ADJUSTED", "0", "DATA and DATABUF registers are right-adjusted")
        channelDataAdjustment.addKey("LEFT-ADJUSTED", "1", "DATA and DATABUF registers are left-adjusted")
        channelDataAdjustment.setOutputMode("Key")
        channelDataAdjustment.setDisplayMode("Key")
        channelDataAdjustment.setDefaultValue(0)

        channelRunStdby = dacComponent.createBooleanSymbol("DAC_CHANNEL_" + str(channel) + "_RSTDBY", channelMenu)
        channelRunStdby.setLabel("Run in Standby")

        channelDither = dacComponent.createBooleanSymbol("DAC_CHANNEL_" + str(channel) + "_DITHER", channelMenu)
        channelDither.setLabel("Enable Dithering")

        channelOversampleNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DAC"]/value-group@[name="DAC_DACCTRL__OSR"]')
        channelOversampleValues = channelOversampleNode.getChildren()

        channelOversample = dacComponent.createKeyValueSetSymbol("DAC_CHANNEL_" + str(channel) + "_OVERSAMPLE", channelMenu)
        channelOversample.setLabel("Oversampling Ratio")
        for index in range(0, len(channelOversampleValues)):
            channelOversampleKey = channelOversampleValues[index].getAttribute("name")
            channelOversampleValue = channelOversampleValues[index].getAttribute("value")
            channelOversampleCaption = channelOversampleValues[index].getAttribute("caption")
            channelOversample.addKey(channelOversampleKey, channelOversampleValue, channelOversampleCaption)
        channelOversample.setOutputMode("Value")
        channelOversample.setDisplayMode("Description")
        channelOversample.setDefaultValue(0)

        channelRefreshNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DAC"]/value-group@[name="DAC_DACCTRL__REFRESH"]')
        channelRefreshValues = channelRefreshNode.getChildren()

        channelRefresh = dacComponent.createKeyValueSetSymbol("DAC_CHANNEL_" + str(channel) + "_REFRESH", channelMenu)
        channelRefresh.setLabel("Refresh Rate")
        for index in range(0, len(channelRefreshValues)):
            channelRefreshKey = channelRefreshValues[index].getAttribute("name")
            channelRefreshValue = channelRefreshValues[index].getAttribute("value")
            channelRefreshCaption = channelRefreshValues[index].getAttribute("caption")
            channelRefresh.addKey(channelRefreshKey, channelRefreshValue, channelRefreshCaption)
        channelRefresh.setOutputMode("Value")
        channelRefresh.setDisplayMode("Description")
        channelRefresh.setDefaultValue(0)
        channelRefresh.setDependencies(refreshVisibility,["DAC_CHANNEL_" + str(channel) + "_OVERSAMPLE"])

        channelEvent = dacComponent.createMenuSymbol("DAC_EVENT_MENU" + str(channel), channelMenu)
        channelEvent.setLabel("CHANNEL " + str(channel) + " Event Configuration")

        channelResrdy = dacComponent.createBooleanSymbol("DAC_CHANNEL_EVENT_RESRDYEO" + str(channel), channelEvent)
        channelResrdy.setLabel("Enable Result Ready Event")
        evctrldep.append("DAC_CHANNEL_EVENT_RESRDYEO" + str(channel))

        channelEmpty = dacComponent.createBooleanSymbol("DAC_CHANNEL_EVENT_EMPTYEO" + str(channel), channelEvent)
        channelEmpty.setLabel("Enable Data Buffer Empty Event")
        evctrldep.append("DAC_CHANNEL_EVENT_EMPTYEO" + str(channel))

        channelStart = dacComponent.createBooleanSymbol("DAC_CHANNEL_EVENT_STARTEI" + str(channel), channelEvent)
        channelStart.setLabel("Start Conversion on event detection")
        evctrldep.append("DAC_CHANNEL_EVENT_STARTEI" + str(channel))

        channelInvert = dacComponent.createBooleanSymbol("DAC_CHANNEL_EVENT_INVEI" + str(channel), channelEvent)
        channelInvert.setLabel("Invert Start Conversion Event")

    # Clock Warning status
    dacSym_ClkEnComment = dacComponent.createCommentSymbol("DAC_CLOCK_ENABLE_COMMENT", None)
    dacSym_ClkEnComment.setLabel("Warning!!!" + dacInstanceName.getValue() + " Clock is Disabled in Clock Manager")
    dacSym_ClkEnComment.setVisible(False)
    dacSym_ClkEnComment.setDependencies(updateDACClockWarringStatus, ["core." + dacInstanceName.getValue() + "_CLOCK_ENABLE"])

################################################################################
########                          Code Generation                      #########
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    dacModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DAC\"]")
    dacModuleID = dacModuleNode.getAttribute("id")

    # Instance Header File
    dacHeaderFile = dacComponent.createFileSymbol("DAC_INSTANCE_HEADER", None)
    dacHeaderFile.setSourcePath("../peripheral/dac_u2502/templates/plib_dac.h.ftl")
    dacHeaderFile.setOutputName("plib_"+dacInstanceName.getValue().lower()+".h")
    dacHeaderFile.setDestPath("/peripheral/dac/")
    dacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dac/")
    dacHeaderFile.setType("HEADER")
    dacHeaderFile.setMarkup(True)

    # Source File
    dacSourceFile = dacComponent.createFileSymbol("DAC_SOURCE", None)
    dacSourceFile.setSourcePath("../peripheral/dac_u2502/templates/plib_dac.c.ftl")
    dacSourceFile.setOutputName("plib_" + dacInstanceName.getValue().lower() + ".c")
    dacSourceFile.setDestPath("/peripheral/dac/")
    dacSourceFile.setProjectPath("config/" + configName + "/peripheral/dac/")
    dacSourceFile.setType("SOURCE")
    dacSourceFile.setMarkup(True)

    #System Initialization
    dacSystemInitFile = dacComponent.createFileSymbol("DAC_SYS_INIT", None)
    dacSystemInitFile.setType("STRING")
    dacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    dacSystemInitFile.setSourcePath("../peripheral/dac_u2502/templates/system/initialization.c.ftl")
    dacSystemInitFile.setMarkup(True)

    #System Definition
    dacSystemDefFile = dacComponent.createFileSymbol("DAC_SYS_DEF", None)
    dacSystemDefFile.setType("STRING")
    dacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dacSystemDefFile.setSourcePath("../peripheral/dac_u2502/templates/system/definitions.h.ftl")
    dacSystemDefFile.setMarkup(True)
