# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

from math import ceil

################################################################################
#### Business Logic ####
################################################################################
def calcDacFrequency(symbol,event):
    dacFreq = int(Database.getSymbolValue("core", daccInstanceName.getValue() + "_CLOCK_FREQUENCY"))/(2 * 1000000.0)
    symbol.setLabel("**** DAC Frequency = " + str(dacFreq) + " MHz ****")

def triggerSelectVisibility(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "TRIGGER_MODE"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def setDacSpeed(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "MAX_SPEED_MODE"):
        symbol.setSelectedKey("1M")
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def symbolVisible(symbol, event):
    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################
def instantiateComponent(daccComponent):
    global daccInstanceName

    daccInstanceName = daccComponent.createStringSymbol("DACC_INSTANCE_NAME", None)
    daccInstanceName.setVisible(False)
    daccInstanceName.setDefaultValue(daccComponent.getID().upper())

    Log.writeInfoMessage("Running " + daccInstanceName.getValue())
    Database.setSymbolValue("core", daccInstanceName.getValue()+"_CLOCK_ENABLE", True)

    dacFreq = int(Database.getSymbolValue("core", daccInstanceName.getValue() + "_CLOCK_FREQUENCY"))/(2 * 1000000.0)
    daccFreqCommnet = daccComponent.createCommentSymbol("DACC_FREQ_COMMENT", None)
    daccFreqCommnet.setLabel("**** DAC Frequency = " + str(dacFreq) + " MHz ****")
    daccFreqCommnet.setDependencies(calcDacFrequency, ["core." + daccInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    dacChannelConversionMode = daccComponent.createKeyValueSetSymbol("CONVERSION_MODE_CH", None)
    dacChannelConversionMode.setLabel("Select Conversion Mode")
    dacChannelConversionMode.addKey("FREE_RUNNING_MODE", "0", "Free-Running Mode")
    dacChannelConversionMode.addKey("MAX_SPEED_MODE", "1", "Maximum Speed Mode")
    dacChannelConversionMode.addKey("TRIGGER_MODE", "2", "External Trigger Mode")
    dacChannelConversionMode.setOutputMode("Key")
    dacChannelConversionMode.setDisplayMode("Description")
    dacChannelConversionMode.setDefaultValue(0)

    daccSym_MR_STARTUP = daccComponent.createKeyValueSetSymbol("DACC_MR_STARTUP", None)
    daccSym_MR_STARTUP.setLabel("Startup Time Selection")
    daccValGrp_STARTUP = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DACC\"]/value-group@[name=\"DACC_MR__STARTUP\"]")
    daccStartupValues = daccValGrp_STARTUP.getChildren()
    for index in range(len(daccStartupValues)):
        daccSym_MR_STARTUP.addKey(daccStartupValues[index].getAttribute("name"), daccStartupValues[index].getAttribute("value"), daccStartupValues[index].getAttribute("caption"))
    daccSym_MR_STARTUP.setOutputMode("Value")
    daccSym_MR_STARTUP.setDisplayMode("Description")
    daccSym_MR_STARTUP.setDefaultValue(8)

    daccChannelEnableReg = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DACC\"]/register-group@[name=\"DACC\"]/register@[name=\"DACC_CHER\"]")
    #Max no of channels
    daccSym_NUM_CHANNELS = daccComponent.createIntegerSymbol("DACC_NUM_CHANNELS", None)
    daccSym_NUM_CHANNELS.setDefaultValue(len(daccChannelEnableReg.getChildren()))
    daccSym_NUM_CHANNELS.setVisible(False)

    for channelID in range(daccSym_NUM_CHANNELS.getValue()):
        daccChannelEnable = daccComponent.createBooleanSymbol("DACC_CHER_CH" + str(channelID), None)
        daccChannelEnable.setLabel("Enable Channel " + str(channelID))

    daccSym_MR_TAG_Enable = daccComponent.createBooleanSymbol("DACC_MR_TAG_ENABLE", None)
    daccSym_MR_TAG_Enable.setLabel("Enable Tag Selection Mode")

    dacChannelTriggerSelect = daccComponent.createKeyValueSetSymbol("DACC_TRIGR_TRGSEL", None)
    dacChannelTriggerSelect.setLabel("Select Trigger Source")
    dacChannelTriggerSelect.setVisible(False)
    dacChannelTriggerSelect.setDependencies(triggerSelectVisibility, ["CONVERSION_MODE_CH"])
    daccValGrp_TRIGR_TRGSEL = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DACC\"]/value-group@[name=\"DACC_MR__TRGSEL\"]")
    daccTrgselValues = daccValGrp_TRIGR_TRGSEL.getChildren()
    for index in range(len(daccTrgselValues)):
        dacChannelTriggerSelect.addKey(daccTrgselValues[index].getAttribute("name"), daccTrgselValues[index].getAttribute("value"), daccTrgselValues[index].getAttribute("caption"))
    dacChannelTriggerSelect.setDefaultValue(0)
    dacChannelTriggerSelect.setOutputMode("Key")
    dacChannelTriggerSelect.setDisplayMode("Description")

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")
    daccHeaderFile = daccComponent.createFileSymbol("DACC_HEADER", None)
    daccHeaderFile.setSourcePath("../peripheral/dacc_6461/templates/plib_dacc_common.h")
    daccHeaderFile.setOutputName("plib_dacc_common.h")
    daccHeaderFile.setDestPath("peripheral/dacc/")
    daccHeaderFile.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccHeaderFile.setType("HEADER")
    daccHeaderFile.setOverwrite(True)
    daccHeaderFile.setMarkup(False)

    daccHeader1File = daccComponent.createFileSymbol("DACC_HEADER1", None)
    daccHeader1File.setSourcePath("../peripheral/dacc_6461/templates/plib_dacc.h.ftl")
    daccHeader1File.setOutputName("plib_"+daccInstanceName.getValue().lower() + ".h")
    daccHeader1File.setMarkup(True)
    daccHeader1File.setDestPath("peripheral/dacc/")
    daccHeader1File.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccHeader1File.setType("HEADER")
    daccHeader1File.setOverwrite(True)

    daccSource1File = daccComponent.createFileSymbol("DACC_SOURCE", None)
    daccSource1File.setSourcePath("../peripheral/dacc_6461/templates/plib_dacc.c.ftl")
    daccSource1File.setOutputName("plib_"+daccInstanceName.getValue().lower() + ".c")
    daccSource1File.setMarkup(True)
    daccSource1File.setDestPath("peripheral/dacc/")
    daccSource1File.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccSource1File.setType("SOURCE")
    daccSource1File.setOverwrite(True)

    daccSystemInitFile = daccComponent.createFileSymbol("DACC_INIT", None)
    daccSystemInitFile.setType("STRING")
    daccSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    daccSystemInitFile.setSourcePath("../peripheral/dacc_6461/templates/system/initialization.c.ftl")
    daccSystemInitFile.setMarkup(True)

    daccSystemDefFile = daccComponent.createFileSymbol("DACC_DEF", None)
    daccSystemDefFile.setType("STRING")
    daccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    daccSystemDefFile.setSourcePath("../peripheral/dacc_6461/templates/system/definitions.h.ftl")
    daccSystemDefFile.setMarkup(True)
