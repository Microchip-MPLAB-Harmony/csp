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

def updateBODVDDOperationModeVisibleProperty(symbol, event):

    symbol.setVisible(event["value"])

    Log.writeInfoMessage("updateBODVDDOperationModeVisibleProperty is : " + str(event["value"]))

def updateBODVDDPrescalerVisibleProperty(symbol, event):

    if supcSym_BODVDD_STDBYCFG.getValue() == 1 or supcSym_BODVDD_ACTCFG.getValue() == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

    Log.writeInfoMessage("updateBODVDDPrescalerVisibleProperty is : " + str(event["value"]))

def updateSUPCInterruptWarringStatus(symbol, event):

    symbol.setVisible(event["value"])

def updateSUPCClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(supcComponent):

    global supcSym_BODVDD_STDBYCFG
    global supcSym_BODVDD_ACTCFG

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())

    #clock enable
    Database.clearSymbolValue("core", supcInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", supcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    #interrupt mode
    supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRRUPT_MODE", None)
    supcSym_INTENSET.setLabel("Interrupt Mode")
    supcSym_INTENSET.setDefaultValue(True)
    supcSym_INTENSET.setReadOnly(True)

    #BODVDD RUNSTDBY mode
    supcSym_BODVDD_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_BODVDD_RUNSTDBY", None)
    supcSym_BODVDD_RUNSTDBY.setLabel("Enable Brown Out Detector in Standby Sleep Mode ?")
    supcSym_BODVDD_RUNSTDBY.setDescription("Configures BODVDD operation in Standby Sleep Mode")

    #BODVDD STDBYCFG mode
    supcSym_BODVDD_STDBYCFG = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_STDBYCFG", supcSym_BODVDD_RUNSTDBY)
    supcSym_BODVDD_STDBYCFG.setLabel("Brown Out Detector Operation Mode in Standby Sleep Mode ?")
    supcSym_BODVDD_STDBYCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Standby Sleep mode")
    supcSym_BODVDD_STDBYCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_STDBYCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_STDBYCFG.setDefaultValue(0)
    supcSym_BODVDD_STDBYCFG.setOutputMode("Value")
    supcSym_BODVDD_STDBYCFG.setDisplayMode("Description")
    supcSym_BODVDD_STDBYCFG.setVisible(False)
    supcSym_BODVDD_STDBYCFG.setDependencies(updateBODVDDOperationModeVisibleProperty, ["SUPC_BODVDD_RUNSTDBY"])

    #BODVDD ACTCFG mode
    supcSym_BODVDD_ACTCFG = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_ACTCFG", None)
    supcSym_BODVDD_ACTCFG.setLabel("Brown Out Detector Operation Mode in Active Mode ?")
    supcSym_BODVDD_ACTCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Active mode")
    supcSym_BODVDD_ACTCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_ACTCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_ACTCFG.setDefaultValue(0)
    supcSym_BODVDD_ACTCFG.setOutputMode("Value")
    supcSym_BODVDD_ACTCFG.setDisplayMode("Description")

    #BODVDD PSEL
    supcSym_BODVDD_PSEL = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_PSEL", None)
    supcSym_BODVDD_PSEL.setLabel("Brown Out Detector Sampling Mode Clock Prescaler")
    supcSym_BODVDD_PSEL.setDescription("Configures the sampling clock prescaler when BODVDD is operating in sampling mode")
    supcSym_BODVDD_PSEL.setVisible(False)
    supcSym_BODVDD_PSEL.setDependencies(updateBODVDDPrescalerVisibleProperty, ["SUPC_BODVDD_STDBYCFG", "SUPC_BODVDD_ACTCFG"])

    supcBODVDDPselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_BODVDD__PSEL\"]")
    supcBODVDDPselValues = []
    supcBODVDDPselValues = supcBODVDDPselNode.getChildren()

    for index in range (0, len(supcBODVDDPselValues)):
        supcBODVDDPselKeyName = supcBODVDDPselValues[index].getAttribute("name")
        supcBODVDDPselKeyDescription = supcBODVDDPselValues[index].getAttribute("caption")
        supcBODVDDPselKeyValue =  supcBODVDDPselValues[index].getAttribute("value")
        supcSym_BODVDD_PSEL.addKey(supcBODVDDPselKeyName, supcBODVDDPselKeyValue, supcBODVDDPselKeyDescription)

    supcSym_BODVDD_PSEL.setDefaultValue(0)
    supcSym_BODVDD_PSEL.setOutputMode("Key")
    supcSym_BODVDD_PSEL.setDisplayMode("Description")

    #VREG RUNSTDBY mode
    supcSym_VREG_RUNSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREG_RUNSTDBY", None)
    supcSym_VREG_RUNSTDBY.setLabel("Voltage Regulator mode in Standby Sleep ?")
    supcSym_VREG_RUNSTDBY.setDescription("Configures VREG operation in Standby Sleep Mode")
    supcSym_VREG_RUNSTDBY.addKey("LP_OP", "0", "Low Power Operation")
    supcSym_VREG_RUNSTDBY.addKey("NORMAL_OP", "1", "Normal Operation")
    supcSym_VREG_RUNSTDBY.setDefaultValue(0)
    supcSym_VREG_RUNSTDBY.setOutputMode("Value")
    supcSym_VREG_RUNSTDBY.setDisplayMode("Description")

    #VREF selection
    supcSym_VREF_SEL = supcComponent.createKeyValueSetSymbol("SUPC_VREF_SEL", None)
    supcSym_VREF_SEL.setLabel("VREF Voltage Level (for ADC, SDADC and DAC) ?")
    supcSym_VREF_SEL.setDescription("Configures VREF voltage level")

    supcVREFSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_VREF__SEL\"]")
    supcVREFSelectionValues = []
    supcVREFSelectionValues = supcVREFSelectionNode.getChildren()

    for index in range (0, len(supcVREFSelectionValues)):
        supcVREFSelectionKeyName = supcVREFSelectionValues[index].getAttribute("name")
        supcVREFSelectionKeyDescription = supcVREFSelectionValues[index].getAttribute("caption")
        supcVREFSelectionKeyValue =  supcVREFSelectionValues[index].getAttribute("value")
        supcSym_VREF_SEL.addKey(supcVREFSelectionKeyName, supcVREFSelectionKeyValue, supcVREFSelectionKeyDescription)

    supcSym_VREF_SEL.setDefaultValue(0)
    supcSym_VREF_SEL.setOutputMode("Key")
    supcSym_VREF_SEL.setDisplayMode("Description")

    #VREF ONDEMAND mode
    supcSym_VREF_ONDEMAND = supcComponent.createKeyValueSetSymbol("SUPC_VREF_ONDEMAND", None)
    supcSym_VREF_ONDEMAND.setLabel("VREF Availability")
    supcSym_VREF_ONDEMAND.setDescription("Configures the VREF On Demand behavior")
    supcSym_VREF_ONDEMAND.addKey("ALWAYS_AVA", "0", "Always Available")
    supcSym_VREF_ONDEMAND.addKey("ON_PER_REQ", "1", "Only on Peripheral Request")
    supcSym_VREF_ONDEMAND.setDefaultValue(0)
    supcSym_VREF_ONDEMAND.setOutputMode("Value")
    supcSym_VREF_ONDEMAND.setDisplayMode("Description")

    #VREF RUNSTDBY mode
    supcSym_VREF_RUNSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREF_RUNSTDBY", None)
    supcSym_VREF_RUNSTDBY.setLabel("Voltage Reference Available in Standby Sleep ?")
    supcSym_VREF_RUNSTDBY.setDescription("Configures VREF operation in Standby Sleep Mode")
    supcSym_VREF_RUNSTDBY.addKey("DISABLE", "0", "Disable in Standby Sleep")
    supcSym_VREF_RUNSTDBY.addKey("AVAILABLE", "1", "Available in Standby Sleep")
    supcSym_VREF_RUNSTDBY.setDefaultValue(0)
    supcSym_VREF_RUNSTDBY.setOutputMode("Value")
    supcSym_VREF_RUNSTDBY.setDisplayMode("Description")

    #VREF VREFOE mode
    supcSym_VREF_VREFOE = supcComponent.createBooleanSymbol("SUPC_VREF_VREFOE", None)
    supcSym_VREF_VREFOE.setLabel("Connect VREF to ADC Channel ?")
    supcSym_VREF_VREFOE.setDescription("Configures VREF availability to ADC input")

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = supcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = supcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = supcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = supcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and Interrupt
    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, True, 2)
    Database.clearSymbolValue("core", InterruptHandler)
    Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, True, 2)

    # Interrupt Warning status
    supcSym_IntEnComment = supcComponent.createCommentSymbol("SUPC_INTERRUPT_ENABLE_COMMENT", None)
    supcSym_IntEnComment.setVisible(False)
    supcSym_IntEnComment.setLabel("Warning!!! SUPC Interrupt is Disabled in Interrupt Manager")
    supcSym_IntEnComment.setDependencies(updateSUPCInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    supcSym_ClkEnComment = supcComponent.createCommentSymbol("SUPC_CLOCK_ENABLE_COMMENT", None)
    supcSym_ClkEnComment.setLabel("Warning!!! SUPC Peripheral Clock is Disabled in Clock Manager")
    supcSym_ClkEnComment.setVisible(False)
    supcSym_ClkEnComment.setDependencies(updateSUPCClockWarringStatus, ["core."+supcInstanceName.getValue()+"_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]")
    supcModuleID = supcModuleNode.getAttribute("id")

    supcSym_HeaderFile = supcComponent.createFileSymbol("SUPC_HEADER", None)
    supcSym_HeaderFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/plib_supc.h.ftl")
    supcSym_HeaderFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcSym_HeaderFile.setDestPath("/peripheral/supc/")
    supcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_HeaderFile.setType("HEADER")
    supcSym_HeaderFile.setMarkup(True)

    supcSym_SourceFile = supcComponent.createFileSymbol("SUPC_SOURCE", None)
    supcSym_SourceFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/plib_supc.c.ftl")
    supcSym_SourceFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSym_SourceFile.setDestPath("/peripheral/supc/")
    supcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_SourceFile.setType("SOURCE")
    supcSym_SourceFile.setMarkup(True)

    supcSym_SystemInitFile = supcComponent.createFileSymbol("SUPC_SYS_INT", None)
    supcSym_SystemInitFile.setType("STRING")
    supcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSym_SystemInitFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/system/initialization.c.ftl")
    supcSym_SystemInitFile.setMarkup(True)

    supcSym_SystemDefFile = supcComponent.createFileSymbol("SUPC_SYS_DEF", None)
    supcSym_SystemDefFile.setType("STRING")
    supcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSym_SystemDefFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/system/definitions.h.ftl")
    supcSym_SystemDefFile.setMarkup(True)
