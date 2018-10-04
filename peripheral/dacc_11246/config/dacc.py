"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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
#### Register Information ####
################################################################################
daccRegModule = Register.getRegisterModule("DACC")
daccValGrp_TRIGR_OSR0 = daccRegModule.getValueGroup("DACC_TRIGR__OSR0")

daccValGrp_TRIGR_TRGSEL = []
dacChannelMenu = []
dacChannelBiasCurrent = []
dacChannelConversionMode = []
dacChannelTriggerSelect = []
dacChannelOSR = []
dacChannelMaxSpeed = []
dacChannelTriggerEnable = []


################################################################################
#### Business Logic ####
################################################################################
def daccGetMasterClockFrequency():
    main_clk_freq = int(Database.getSymbolValue("core", daccInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    return main_clk_freq

def calcDacFrequency(symbol,event):
    dacFreq=daccGetMasterClockFrequency()/((event["value"]+2)*1000000.0)

    Log.writeInfoMessage("************************** DAC Frequency = "+ str(dacFreq) +" MHz*********************")

    if(dacFreq <= 12):
        symbol.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz ****")
    else:
        symbol.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz is greater than 12MHz, Increase the prescaler value ****")

def triggerSelectVisibility(symbol, event):
    symObj=event["symbol"]
    
    if (symObj.getSelectedKey() == "TRIGGER_MODE"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def OSRVisibility(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "TRIGGER_MODE"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(False)
        
def channel1Visibility(symbol,event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey()  == "DIFFERENTIAL"):
        dacChannelMenu[1].setVisible(False)
    else:
        dacChannelMenu[1].setVisible(True)

def enableTriggerMode(symbol, event):  
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "TRIGGER_MODE"):
        symbol.clearValue()
        symbol.setValue(True, 1)
    else:
        symbol.clearValue()
        symbol.setValue(False, 1)

def enableMaxSpeedMode(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "MAX_SPEED_MODE"):
        symbol.clearValue()
        symbol.setValue(True, 1)
    else:
        symbol.clearValue()
        symbol.setValue(False, 1)

def setDacSpeed(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "MAX_SPEED_MODE"):
        symbol.clearValue()
        symbol.setSelectedKey("1M",1)
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)
        

################################################################################
#### Component ####
################################################################################
def instantiateComponent(daccComponent):
    global daccInstanceName
    daccInstanceName = daccComponent.createStringSymbol("DACC_INSTANCE_NAME", None)
    daccInstanceName.setVisible(False)
    daccInstanceName.setDefaultValue(daccComponent.getID().upper())

    Database.clearSymbolValue("core", daccInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", daccInstanceName.getValue()+"_CLOCK_ENABLE", True, 1)


    Log.writeInfoMessage("--------------------------------------------------------------------")
    Log.writeInfoMessage("************************** Running "+ daccInstanceName.getValue()+" *********")
    Log.writeInfoMessage("--------------------------------------------------------------------")
    
    daccSym_MR_PRESCALER = daccComponent.createIntegerSymbol("DACC_MR_PRESCALER", None)
    daccSym_MR_PRESCALER.setLabel("Prescaler Value")
    daccSym_MR_PRESCALER.setMin(0)
    daccSym_MR_PRESCALER.setMax(15)
    daccSym_MR_PRESCALER.setDefaultValue(15)

    dacFreq = daccGetMasterClockFrequency()/((daccSym_MR_PRESCALER.getValue()+2)*1000000.0)

    daccPrescalerWarning = daccComponent.createCommentSymbol("PRESCALER_COMMENT", None)
    daccPrescalerWarning.setLabel("**** DAC Frequency = "+str(dacFreq) + " MHz for the selected prescaler value ****")
    daccPrescalerWarning.setVisible(True)
    daccPrescalerWarning.setDependencies(calcDacFrequency, ["DACC_MR_PRESCALER", "core." + daccInstanceName.getValue() + "_CLOCK_FREQUENCY"])


    daccSym_MR_DIFF = daccComponent.createKeyValueSetSymbol("DACC_MR_DIFF", None)
    daccSym_MR_DIFF.setLabel ("Select DAC Output Mode")
    daccSym_MR_DIFF.addKey("SINGLE_ENDED", "0", "Single-Ended Output")
    daccSym_MR_DIFF.addKey("DIFFERENTIAL", "1", "Differential Output")
    daccSym_MR_DIFF.setOutputMode("Key")
    daccSym_MR_DIFF.setDisplayMode("Description")
    daccSym_MR_DIFF.setSelectedKey("SINGLE_ENDED",1)

    for channelID in range(0, 2):

        dacChannelMenu.append(channelID)
        dacChannelMenu[channelID] = daccComponent.createBooleanSymbol("DACC_CHER_CH"+str(channelID), None)
        dacChannelMenu[channelID].setLabel("Enable Channel "+str(channelID))
        dacChannelMenu[channelID].setDependencies(channel1Visibility, ["DACC_MR_DIFF"])

        dacChannelConversionMode.append(channelID)
        dacChannelConversionMode[channelID] = daccComponent.createKeyValueSetSymbol("CONVERSION_MODE_CH"+str(channelID), dacChannelMenu[channelID])
        dacChannelConversionMode[channelID].setLabel("Select Conversion Mode")
        dacChannelConversionMode[channelID].addKey("FREE_RUNNING_MODE", "0", "Free-Running Mode")
        dacChannelConversionMode[channelID].addKey("MAX_SPEED_MODE", "1", "Maximum-Speed Mode")
        dacChannelConversionMode[channelID].addKey("TRIGGER_MODE", "2", "External Trigger Mode")
        dacChannelConversionMode[channelID].setOutputMode("Key")
        dacChannelConversionMode[channelID].setDisplayMode("Description")
        dacChannelConversionMode[channelID].setSelectedKey("FREE_RUNNING_MODE",1)

        dacChannelBiasCurrent.append(channelID)
        dacChannelBiasCurrent[channelID] = daccComponent.createKeyValueSetSymbol("DACC_ACR_IBCTLCH"+str(channelID), dacChannelMenu[channelID])
        dacChannelBiasCurrent[channelID].setLabel("Select Conversion Speed")
        dacChannelBiasCurrent[channelID].addKey("BYPASS", "0", "Bypass mode: Disables output buffer to minimize power")
        dacChannelBiasCurrent[channelID].addKey("500K", "1", "<500 Ksps Conversion speed")
        dacChannelBiasCurrent[channelID].addKey("1M", "3", "Up to 1 Msps Conversion speed")
        dacChannelBiasCurrent[channelID].setOutputMode("Value")
        dacChannelBiasCurrent[channelID].setDisplayMode("Description")
        dacChannelBiasCurrent[channelID].setSelectedKey("1M",1)
        dacChannelBiasCurrent[channelID].setDependencies(setDacSpeed, ["CONVERSION_MODE_CH"+str(channelID)])


        dacChannelMaxSpeed.append(channelID)
        dacChannelMaxSpeed[channelID] = daccComponent.createBooleanSymbol("DACC_MR_MAXS"+str(channelID), dacChannelMenu[channelID])
        dacChannelMaxSpeed[channelID].setLabel("Max Speed Mode")
        dacChannelMaxSpeed[channelID].setVisible(False)
        dacChannelMaxSpeed[channelID].setDependencies(enableMaxSpeedMode, ["CONVERSION_MODE_CH"+str(channelID)])

        dacChannelTriggerEnable.append(channelID)
        dacChannelTriggerEnable[channelID] = daccComponent.createBooleanSymbol("DACC_TRIGR_TRGEN"+str(channelID), dacChannelMenu[channelID])
        dacChannelTriggerEnable[channelID].setLabel("Enable Trigger Mode")
        dacChannelTriggerEnable[channelID].setVisible(False)
        dacChannelTriggerEnable[channelID].setDependencies(enableTriggerMode, ["CONVERSION_MODE_CH"+str(channelID)])

        dacChannelTriggerSelect.append(channelID)
        dacChannelTriggerSelect[channelID] = daccComponent.createKeyValueSetSymbol("DACC_TRIGR_TRGSEL"+str(channelID), dacChannelMenu[channelID])
        dacChannelTriggerSelect[channelID].setLabel("Select Trigger Source")
        dacChannelTriggerSelect[channelID].setDefaultValue(0)
        dacChannelTriggerSelect[channelID].setOutputMode("Key")
        dacChannelTriggerSelect[channelID].setDisplayMode("Description")
        dacChannelTriggerSelect[channelID].setVisible(False)
        dacChannelTriggerSelect[channelID].setDependencies(triggerSelectVisibility, ["CONVERSION_MODE_CH"+str(channelID)])

        daccValGrp_TRIGR_TRGSEL.append(channelID)
        daccValGrp_TRIGR_TRGSEL[channelID] = daccRegModule.getValueGroup("DACC_TRIGR__TRGSEL" + str(channelID))
        count = daccValGrp_TRIGR_TRGSEL[channelID].getValueCount()
        for id in range(0,count):
            valueName = daccValGrp_TRIGR_TRGSEL[channelID].getValueNames()[id]
            dacChannelTriggerSelect[channelID].addKey(valueName, daccValGrp_TRIGR_TRGSEL[channelID].getValue(valueName).getValue(), daccValGrp_TRIGR_TRGSEL[channelID].getValue(valueName).getDescription())
            
        dacChannelOSR.append(channelID)
        dacChannelOSR[channelID] = daccComponent.createKeyValueSetSymbol("DACC_TRIGR_OSR"+str(channelID), dacChannelMenu[channelID])
        dacChannelOSR[channelID].setLabel("Select Oversampling Ratio for Interpolation Filter")
        dacChannelOSR[channelID].setDefaultValue(0)
        dacChannelOSR[channelID].setOutputMode("Key")
        dacChannelOSR[channelID].setDisplayMode("Description")
        dacChannelOSR[channelID].setVisible(False)
        dacChannelOSR[channelID].setDependencies(OSRVisibility, ["CONVERSION_MODE_CH"+str(channelID)])
        count = daccValGrp_TRIGR_OSR0.getValueCount()
        for id in range(0,count):
            valueName = daccValGrp_TRIGR_OSR0.getValueNames()[id]
            dacChannelOSR[channelID].addKey(valueName, daccValGrp_TRIGR_OSR0.getValue(valueName).getValue(), daccValGrp_TRIGR_OSR0.getValue(valueName).getDescription())

            
############################################################################
#### Dependency ####
############################################################################       
            
            
############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")
    daccHeaderFile = daccComponent.createFileSymbol("DACC_HEADER", None)
    daccHeaderFile.setSourcePath("../peripheral/dacc_11246/templates/plib_dacc_common.h")
    daccHeaderFile.setOutputName("plib_dacc_common.h")
    daccHeaderFile.setDestPath("peripheral/dacc/")
    daccHeaderFile.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccHeaderFile.setType("HEADER")
    daccHeaderFile.setOverwrite(True)
    
    daccHeader1File = daccComponent.createFileSymbol("DACC_HEADER1", None)
    daccHeader1File.setSourcePath("../peripheral/dacc_11246/templates/plib_dacc.h.ftl")
    daccHeader1File.setOutputName("plib_"+daccInstanceName.getValue().lower() + ".h")
    daccHeader1File.setMarkup(True)
    daccHeader1File.setDestPath("peripheral/dacc/")
    daccHeader1File.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccHeader1File.setType("HEADER")
    daccHeader1File.setOverwrite(True)

    daccSource1File = daccComponent.createFileSymbol("DACC_SOURCE", None)
    daccSource1File.setSourcePath("../peripheral/dacc_11246/templates/plib_dacc.c.ftl")
    daccSource1File.setOutputName("plib_"+daccInstanceName.getValue().lower() + ".c")
    daccSource1File.setMarkup(True)
    daccSource1File.setDestPath("peripheral/dacc/")
    daccSource1File.setProjectPath("config/" + configName + "/peripheral/dacc/")
    daccSource1File.setType("SOURCE")
    daccSource1File.setOverwrite(True)

    daccSystemInitFile = daccComponent.createFileSymbol("DACC_INIT", None)
    daccSystemInitFile.setType("STRING")
    daccSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    daccSystemInitFile.setSourcePath("../peripheral/dacc_11246/templates/system/system_initialize.c.ftl")
    daccSystemInitFile.setMarkup(True)

    daccSystemDefFile = daccComponent.createFileSymbol("DACC_DEF", None)
    daccSystemDefFile.setType("STRING")
    daccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    daccSystemDefFile.setSourcePath("../peripheral/dacc_11246/templates/system/system_definitions.h.ftl")
    daccSystemDefFile.setMarkup(True)
