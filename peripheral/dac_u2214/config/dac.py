# coding: utf-8
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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateDACClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

################################################################################
########                        DAC Data Base Components               #########
################################################################################

def instantiateComponent(dacComponent):

    dacInstanceName = dacComponent.createStringSymbol("DAC_INSTANCE_NAME", None)
    dacInstanceName.setVisible(False)
    dacInstanceName.setDefaultValue(dacComponent.getID().upper())
    Log.writeInfoMessage("Running " + dacInstanceName.getValue())

    #clock enable
    Database.clearSymbolValue("core", dacInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", dacInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    #Run StandBy
    dacSym_CTRLA_RUNSTDBY = dacComponent.createBooleanSymbol("DAC_RUNSTDBY", None)
    dacSym_CTRLA_RUNSTDBY.setLabel("Disable output in Standby Sleep mode?")

    #Reference Selection
    dacSym_CTRLB_REFSEL = dacComponent.createKeyValueSetSymbol("DAC_REFERENCE_SELECTION", None)
    dacSym_CTRLB_REFSEL.setLabel("DAC Reference Voltage Source")

    dacReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DAC\"]/value-group@[name=\"DAC_CTRLB__REFSEL\"]")
    dacReferenceValues = []
    dacReferenceValues = dacReferenceNode.getChildren()

    dacReferenceDefaultValue = 0

    for index in range(len(dacReferenceValues)):
        dacReferenceKeyName = dacReferenceValues[index].getAttribute("name")

        if (dacReferenceKeyName == "INTREF"):
            dacReferenceDefaultValue = index

        dacReferenceKeyDescription = dacReferenceValues[index].getAttribute("caption")
        dacReferenceKeyValue = dacReferenceValues[index].getAttribute("value")
        dacSym_CTRLB_REFSEL.addKey(dacReferenceKeyName , dacReferenceKeyValue , dacReferenceKeyDescription)

    dacSym_CTRLB_REFSEL.setDefaultValue(dacReferenceDefaultValue)
    dacSym_CTRLB_REFSEL.setOutputMode("Value")
    dacSym_CTRLB_REFSEL.setDisplayMode("Description")

    #DAC output as input to Analog Comparator or ADC or as External output 
    dacSym_CTRLB_IOEN_EOEN = dacComponent.createKeyValueSetSymbol("DAC_OUTPUT_MODE", None)
    dacSym_CTRLB_IOEN_EOEN.setLabel ("Select DAC Output Mode")
    dacSym_CTRLB_IOEN_EOEN.addKey("ANALOG_COMPARATOR", "0", "DAC output to Analog Comparator")
    dacSym_CTRLB_IOEN_EOEN.addKey("INTERNAL_AND_EXTERNAL_OUTPUT", "1", "DAC output to AC, ADC and VOUT pin")
    dacSym_CTRLB_IOEN_EOEN.addKey("EXTERNAL_OUTPUT", "2", "DAC output to VOUT pin")
    dacSym_CTRLB_IOEN_EOEN.setOutputMode("Key")
    dacSym_CTRLB_IOEN_EOEN.setDisplayMode("Description")
    dacSym_CTRLB_IOEN_EOEN.setSelectedKey("EXTERNAL_OUTPUT",1)

    #Left-Adjusted Data
    dacSym_CTRLB_LEFTADJ = dacComponent.createBooleanSymbol("DAC_LEFTADJUSTED_DATA", None)
    dacSym_CTRLB_LEFTADJ.setLabel("Input Data Alignment?")
    dacSym_CTRLB_LEFTADJ.setVisible(False)

    #Voltage Pump Disabled
    dacSym_CTRLB_VPD = dacComponent.createBooleanSymbol("DAC_VOLTAGE_PUMP_DISABLED", None)
    dacSym_CTRLB_VPD.setLabel("Disable voltage pump to save power")

    #Dithering Mode
    dacSym_CTRLB_DITHER = dacComponent.createBooleanSymbol("DAC_DITHERING_MODE", None)
    dacSym_CTRLB_DITHER.setLabel("Enable 4-Bit Dithering?")
    dacSym_CTRLB_DITHER.setVisible(True)

    #Enable Inversion Data Buffer Empty Event Output
    dacSym_EVCTRL_INVEI = dacComponent.createBooleanSymbol("DAC_INVERSION_DATA_BUFFER_EMPTY_EVENT_OUTPUT", None)
    dacSym_EVCTRL_INVEI.setLabel("Generate data buffer empty event?")
    dacSym_EVCTRL_INVEI.setVisible(False)

    #Data Buffer Empty Event Output
    dacSym_EVCTRL_EMPTYEO = dacComponent.createBooleanSymbol("DAC_BUFFER_EMPTY_EVENT_OUTPUT", None)
    dacSym_EVCTRL_EMPTYEO.setLabel("Data Buffer Empty Event output")
    dacSym_EVCTRL_EMPTYEO.setVisible(False)

    #Start Conversion Event Input
    dacSym_EVCTRL_STARTEI = dacComponent.createBooleanSymbol("DAC_START_CONVERSION_EVENT_INPUT", None)
    dacSym_EVCTRL_STARTEI.setLabel("Trigger conversion on input event?")
    dacSym_EVCTRL_STARTEI.setVisible(False)
    # Clock Warning status
    dacSym_ClkEnComment = dacComponent.createCommentSymbol("DAC_CLOCK_ENABLE_COMMENT", None)
    dacSym_ClkEnComment.setLabel("Warning!!! DAC Peripheral Clock is Disabled in Clock Manager")
    dacSym_ClkEnComment.setVisible(False)
    dacSym_ClkEnComment.setDependencies(updateDACClockWarringStatus, ["core."+dacInstanceName.getValue()+"_CLOCK_ENABLE"])

################################################################################
########                          Code Generation                      #########
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    dacModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DAC\"]")
    dacModuleID = dacModuleNode.getAttribute("id")

    # Instance Header File
    dacHeaderFile = dacComponent.createFileSymbol("DAC_INSTANCE_HEADER", None)
    dacHeaderFile.setSourcePath("../peripheral/dac_"+ dacModuleID+"/templates/plib_dac.h.ftl")
    dacHeaderFile.setOutputName("plib_"+dacInstanceName.getValue().lower()+".h")
    dacHeaderFile.setDestPath("/peripheral/dac/")
    dacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dac/")
    dacHeaderFile.setType("HEADER")
    dacHeaderFile.setMarkup(True)

    # Source File
    dacSourceFile = dacComponent.createFileSymbol("DAC_SOURCE", None)
    dacSourceFile.setSourcePath("../peripheral/dac_"+dacModuleID+"/templates/plib_dac.c.ftl")
    dacSourceFile.setOutputName("plib_" + dacInstanceName.getValue().lower() + ".c")
    dacSourceFile.setDestPath("/peripheral/dac/")
    dacSourceFile.setProjectPath("config/" + configName + "/peripheral/dac/")
    dacSourceFile.setType("SOURCE")
    dacSourceFile.setMarkup(True)

    #System Initialization
    dacSystemInitFile = dacComponent.createFileSymbol("DAC_SYS_INIT", None)
    dacSystemInitFile.setType("STRING")
    dacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    dacSystemInitFile.setSourcePath("../peripheral/dac_"+dacModuleID+"/templates/system/initialization.c.ftl")
    dacSystemInitFile.setMarkup(True)

    #System Definition
    dacSystemDefFile = dacComponent.createFileSymbol("DAC_SYS_DEF", None)
    dacSystemDefFile.setType("STRING")
    dacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dacSystemDefFile.setSourcePath("../peripheral/dac_"+dacModuleID+"/templates/system/definitions.h.ftl")
    dacSystemDefFile.setMarkup(True)
