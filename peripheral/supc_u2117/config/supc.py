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
global supcSym_BODVDD_STDBYCFG
global supcSym_BODVDD_ACTCFG
global supcInstanceName
global supcSym_INTENSET

def updateBODVDDOperationModeVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

def updateBODVDDPrescalerVisibleProperty(symbol, event):
    global supcSym_BODVDD_STDBYCFG
    global supcSym_BODVDD_ACTCFG

    if supcSym_BODVDD_STDBYCFG.getValue() == 1 or supcSym_BODVDD_ACTCFG.getValue() == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateSUPCInterruptWarringStatus(symbol, event):
    global supcSym_INTENSET

def interruptControl(symbol, event):
    global supcInstanceName
    InterruptVector = supcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = supcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = supcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"

    if (event["value"] == True):
        Database.setSymbolValue("core", InterruptVector, True, 2)
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", InterruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", InterruptVector, False, 2)
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", InterruptHandlerLock, False, 2)

    intEnableState=Database.getSymbolValue("core",supcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE")
    if ((supcSym_INTENSET.getValue() == True) and (intEnableState == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(supcComponent):
    global supcSym_BODVDD_STDBYCFG
    global supcSym_BODVDD_ACTCFG
    global supcInstanceName
    global supcSym_INTENSET

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())

    supcSym_VREG_Menu= supcComponent.createMenuSymbol("VREG_MENU", None)
    supcSym_VREG_Menu.setLabel("Voltage Regulator (VREG) Configuration")

    #VREG RUNSTDBY mode
    supcSym_VREG_RUNSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREG_RUNSTDBY", supcSym_VREG_Menu)
    supcSym_VREG_RUNSTDBY.setLabel("Select Standby mode operation")
    supcSym_VREG_RUNSTDBY.setDescription("Configures VREG operation in Standby Sleep Mode")
    supcSym_VREG_RUNSTDBY.addKey("LP_OP", "0", "Low Power Operation")
    supcSym_VREG_RUNSTDBY.addKey("NORMAL_OP", "1", "Normal Operation")
    supcSym_VREG_RUNSTDBY.setDefaultValue(0)
    supcSym_VREG_RUNSTDBY.setOutputMode("Value")
    supcSym_VREG_RUNSTDBY.setDisplayMode("Description")

    supcSym_BODVDD_Menu= supcComponent.createMenuSymbol("BOD_MENU", None)
    supcSym_BODVDD_Menu.setLabel("VDD Brown-Out Detector (BOD) Configuration")

    #BODVDD RUNSTDBY mode
    #interrupt mode
    supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRRUPT_MODE", supcSym_BODVDD_Menu)
    supcSym_INTENSET.setLabel("Enable BOD Interrupt")
    supcSym_INTENSET.setDefaultValue(False)

    # Interrupt Warning status
    supcSym_IntEnComment = supcComponent.createCommentSymbol("SUPC_INTERRUPT_ENABLE_COMMENT", supcSym_BODVDD_Menu)
    supcSym_IntEnComment.setVisible(False)
    supcSym_IntEnComment.setLabel("Warning!!! SUPC Interrupt is Disabled in Interrupt Manager")
    supcSym_IntEnComment.setDependencies(interruptControl, [supcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE", "SUPC_INTERRRUPT_MODE"])

    supcSym_BODVDD_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_BODVDD_RUNSTDBY", supcSym_BODVDD_Menu)
    supcSym_BODVDD_RUNSTDBY.setLabel("Run in Standby mode")
    supcSym_BODVDD_RUNSTDBY.setDescription("Configures BODVDD operation in Standby Sleep Mode")

    #BODVDD STDBYCFG mode
    supcSym_BODVDD_STDBYCFG = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_STDBYCFG", supcSym_BODVDD_Menu)
    supcSym_BODVDD_STDBYCFG.setLabel("Select Standby mode operation")
    supcSym_BODVDD_STDBYCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Standby Sleep mode")
    supcSym_BODVDD_STDBYCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_STDBYCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_STDBYCFG.setDefaultValue(0)
    supcSym_BODVDD_STDBYCFG.setOutputMode("Value")
    supcSym_BODVDD_STDBYCFG.setDisplayMode("Description")
    supcSym_BODVDD_STDBYCFG.setVisible(False)
    supcSym_BODVDD_STDBYCFG.setDependencies(updateBODVDDOperationModeVisibleProperty, ["SUPC_BODVDD_RUNSTDBY"])

    #BODVDD ACTCFG mode
    supcSym_BODVDD_ACTCFG = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_ACTCFG", supcSym_BODVDD_Menu)
    supcSym_BODVDD_ACTCFG.setLabel("Select Active mode operation")
    supcSym_BODVDD_ACTCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Active mode")
    supcSym_BODVDD_ACTCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_ACTCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_ACTCFG.setDefaultValue(0)
    supcSym_BODVDD_ACTCFG.setOutputMode("Value")
    supcSym_BODVDD_ACTCFG.setDisplayMode("Description")

    #BODVDD PSEL
    supcSym_BODVDD_PSEL = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_PSEL", supcSym_BODVDD_Menu)
    supcSym_BODVDD_PSEL.setLabel("Select Prescaler for Sampling Clock")
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


    supcSym_VREF_Menu= supcComponent.createMenuSymbol("VREF_MENU", None)
    supcSym_VREF_Menu.setLabel("Voltage Reference (VREF) Configuration")

    #VREF VREFOE mode
    supcSym_VREF_VREFOE = supcComponent.createBooleanSymbol("SUPC_VREF_VREFOE", supcSym_VREF_Menu)
    supcSym_VREF_VREFOE.setLabel("Enable Voltage Reference Output")
    supcSym_VREF_VREFOE.setDescription("Voltage Reference Output Enable")

    #VREF selection
    supcSym_VREF_SEL = supcComponent.createKeyValueSetSymbol("SUPC_VREF_SEL", supcSym_VREF_Menu)
    supcSym_VREF_SEL.setLabel("Select Reference Voltage Level")
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
    supcSym_VREF_ONDEMAND = supcComponent.createKeyValueSetSymbol("SUPC_VREF_ONDEMAND", supcSym_VREF_Menu)
    supcSym_VREF_ONDEMAND.setLabel("Select On demand Control")
    supcSym_VREF_ONDEMAND.setDescription("Configures the VREF On Demand behavior")
    supcSym_VREF_ONDEMAND.addKey("ALWAYS_AVA", "0", "Always on")
    supcSym_VREF_ONDEMAND.addKey("ON_PER_REQ", "1", "Enable on Demand")
    supcSym_VREF_ONDEMAND.setDefaultValue(0)
    supcSym_VREF_ONDEMAND.setOutputMode("Value")
    supcSym_VREF_ONDEMAND.setDisplayMode("Description")

    #VREF RUNSTDBY mode
    supcSym_VREF_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_VREF_RUNSTDBY", supcSym_VREF_Menu)
    supcSym_VREF_RUNSTDBY.setLabel("Run in Standby mode")
    supcSym_VREF_RUNSTDBY.setDescription("Enable VREF operation in Standby Sleep Mode")

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
