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

def updateSupcConfigVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

def updateBOD33PrescalerVisibleProperty(symbol, event):
    if supcSym_BOD33_STDBYCFG.getValue() == 1 or supcSym_BOD33_RUNHIB.getValue() == True or supcSym_BOD33_RUNBKUP.getValue() == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateVrefVisibleProperty(symbol, event):
    if supcSym_VREF_VREFOE.getValue() == True and supcSym_VREF_ONDEMAND.getValue() == False:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def interruptControl(symbol, event):

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_BODDET_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_BODDET_Handler", 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(supcComponent):
    global supcSym_BOD33_STDBYCFG
    global supcSym_BOD33_RUNHIB
    global supcSym_BOD33_RUNBKUP
    global supcSym_VREF_VREFOE
    global supcSym_VREF_ONDEMAND
    global supcInstanceName
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global supcSym_INTENSET

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())

    #BOD33 Menu
    supcSym_BOD33_Menu= supcComponent.createMenuSymbol("BOD33_MENU", None)
    supcSym_BOD33_Menu.setLabel("VDD Brown-Out Detector (BOD33) Configuration")

    #BOD33 interrupt mode
    supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRUPT_ENABLE", supcSym_BOD33_Menu)
    supcSym_INTENSET.setLabel("Enable BOD Interrupt")
    supcSym_INTENSET.setDefaultValue(False)

    # Interrupt Warning status
    supcSym_IntEnComment = supcComponent.createCommentSymbol("SUPC_INTERRUPT_ENABLE_COMMENT", supcSym_BOD33_Menu)
    supcSym_IntEnComment.setVisible(False)
    supcSym_IntEnComment.setLabel("Warning!!! SUPC Interrupt is Disabled in Interrupt Manager")
    supcSym_IntEnComment.setDependencies(interruptControl, ["SUPC_INTERRUPT_ENABLE"])

    #BOD33 RUNHIB
    supcSym_BOD33_RUNHIB = supcComponent.createBooleanSymbol("SUPC_BOD33_RUNHIB", supcSym_BOD33_Menu)
    supcSym_BOD33_RUNHIB.setLabel("Run in Hibernate Mode")
    supcSym_BOD33_RUNHIB.setDescription("Configures BOD33 operation in Hibernate Sleep Mode")
    supcSym_BOD33_RUNHIB.setDefaultValue(False)
    
    #BOD33 RUNBKUP
    supcSym_BOD33_RUNBKUP = supcComponent.createBooleanSymbol("SUPC_BOD33_RUNBKUP", supcSym_BOD33_Menu)
    supcSym_BOD33_RUNBKUP.setLabel("Run in Backup Mode")
    supcSym_BOD33_RUNBKUP.setDescription("Configures BOD33 operation in Backup Sleep Mode")
    supcSym_BOD33_RUNBKUP.setDefaultValue(False)

    #BOD33 RUNSTDBY
    supcSym_BOD33_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_BOD33_RUNSTDBY", supcSym_BOD33_Menu)
    supcSym_BOD33_RUNSTDBY.setLabel("Run in Standby Mode")
    supcSym_BOD33_RUNSTDBY.setDescription("Configures BOD33 operation in Standby Sleep Mode")
    supcSym_BOD33_RUNSTDBY.setDefaultValue(False)

    #BOD33 STDBYCFG mode
    supcSym_BOD33_STDBYCFG = supcComponent.createKeyValueSetSymbol("SUPC_BOD33_STDBYCFG", supcSym_BOD33_Menu)
    supcSym_BOD33_STDBYCFG.setLabel("Select Standby Mode Operation")
    supcSym_BOD33_STDBYCFG.setDescription("Configures whether BOD33 should operate in continuous or sampling mode in Standby Sleep Mode")
    supcSym_BOD33_STDBYCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BOD33_STDBYCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BOD33_STDBYCFG.setDefaultValue(0)
    supcSym_BOD33_STDBYCFG.setOutputMode("Value")
    supcSym_BOD33_STDBYCFG.setDisplayMode("Description")
    supcSym_BOD33_STDBYCFG.setVisible(False)
    supcSym_BOD33_STDBYCFG.setDependencies(updateSupcConfigVisibleProperty, ["SUPC_BOD33_RUNSTDBY"])

    #BOD33 PSEL
    supcSym_BOD33_PSEL = supcComponent.createKeyValueSetSymbol("SUPC_BOD33_PSEL", supcSym_BOD33_Menu)
    supcSym_BOD33_PSEL.setLabel("Select Prescaler for Sampling Clock")
    supcSym_BOD33_PSEL.setDescription("Configures the sampling clock prescaler when BOD33 is operating in sampling Mode")
    supcSym_BOD33_PSEL.setVisible(False)
    supcSym_BOD33_PSEL.setDependencies(updateBOD33PrescalerVisibleProperty, ["SUPC_BOD33_STDBYCFG", "SUPC_BOD33_RUNHIB", "SUPC_BOD33_RUNBKUP"])

    supcBOD33PselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_BOD33__PSEL\"]")
    supcBOD33PselValues = []
    supcBOD33PselValues = supcBOD33PselNode.getChildren()

    #PSEL value 0 is not usable in sampling mode. Thus the loop starts from 1.
    for index in range (1, len(supcBOD33PselValues)):
        supcBOD33PselKeyName = supcBOD33PselValues[index].getAttribute("name")
        supcBOD33PselKeyDescription = supcBOD33PselValues[index].getAttribute("caption")
        supcBOD33PselKeyValue =  supcBOD33PselValues[index].getAttribute("value")
        supcSym_BOD33_PSEL.addKey(supcBOD33PselKeyName, supcBOD33PselKeyValue, supcBOD33PselKeyDescription)

    supcSym_BOD33_PSEL.setDefaultValue(0)
    supcSym_BOD33_PSEL.setOutputMode("Value")
    supcSym_BOD33_PSEL.setDisplayMode("Description")

    #VREG Menu
    supcSym_VREG_Menu= supcComponent.createMenuSymbol("VREG_MENU", None)
    supcSym_VREG_Menu.setLabel("Voltage Regulator (VREG) Configuration")

    #VREG RUNBKUP mode
    supcSym_VREG_RUNBKUP = supcComponent.createKeyValueSetSymbol("SUPC_VREG_RUNBKUP", supcSym_VREG_Menu)
    supcSym_VREG_RUNBKUP.setLabel("Main Voltage Regulator operation in backup sleep")
    supcSym_VREG_RUNBKUP.setDescription("Selects Main Voltage Regulator operation in backup sleep")
    supcSym_VREG_RUNBKUP.addKey("REG_OFF", "0", "Regulator stopped")
    supcSym_VREG_RUNBKUP.addKey("REG_ON", "1", "Regulator not stopped")
    supcSym_VREG_RUNBKUP.setDefaultValue(0)
    supcSym_VREG_RUNBKUP.setOutputMode("Value")
    supcSym_VREG_RUNBKUP.setDisplayMode("Description")

    #VREG VESN
    supcSym_VREG_VSEN = supcComponent.createBooleanSymbol("SUPC_VREG_VSEN", supcSym_VREG_Menu)
    supcSym_VREG_VSEN.setLabel("Enable Voltage Scaling")
    supcSym_VREG_VSEN.setDescription("Enable smooth transition of VDDCORE")
    supcSym_VREG_VSEN.setDefaultValue(False)

    #VREG VSPER
    supcSym_VREG_VSPER = supcComponent.createIntegerSymbol("SUPC_VREG_VSPER", supcSym_VREG_Menu)
    supcSym_VREG_VSPER.setLabel("Voltage Scaling Period")
    supcSym_VREG_VSEN.setDescription("The time is ((2^VSPER) * T), where T is an internal period (typ 250 ns).")
    supcSym_VREG_VSPER.setDefaultValue(0)
    supcSym_VREG_VSPER.setMin(0)
    supcSym_VREG_VSPER.setMax(7)
    supcSym_VREG_VSPER.setVisible(False)
    supcSym_VREG_VSPER.setDependencies(updateSupcConfigVisibleProperty, ["SUPC_VREG_VSEN"])

    #VREF Menu
    supcSym_VREF_Menu= supcComponent.createMenuSymbol("VREF_MENU", None)
    supcSym_VREF_Menu.setLabel("Voltage Reference (VREF) Configuration")

    supcSym_VREF_SEL = supcComponent.createKeyValueSetSymbol("SUPC_VREF_SEL", supcSym_VREF_Menu)
    supcSym_VREF_SEL.setLabel("Voltage Reference value")
    supcSym_VREF_SEL.setDescription("Select the Voltage Reference typical value")

    supcVREFSelNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_VREF__SEL\"]")
    supcVREFSelValues = []
    supcVREFSelValues = supcVREFSelNode.getChildren()

    for index in range (0, len(supcVREFSelValues)):
        supcVREFSelKeyName = supcVREFSelValues[index].getAttribute("name")
        supcVREFSelKeyDescription = supcVREFSelValues[index].getAttribute("caption")
        supcVREFSelKeyValue =  supcVREFSelValues[index].getAttribute("value")
        supcSym_VREF_SEL.addKey(supcVREFSelKeyName, supcVREFSelKeyValue, supcVREFSelKeyDescription)

    supcSym_VREF_SEL.setDefaultValue(0)
    supcSym_VREF_SEL.setOutputMode("Value")
    supcSym_VREF_SEL.setDisplayMode("Description")

    #VREF ONDEMAND mode
    supcSym_VREF_ONDEMAND = supcComponent.createBooleanSymbol("SUPC_VREF_ONDEMAND", supcSym_VREF_Menu)
    supcSym_VREF_ONDEMAND.setLabel("Enable On demand")
    supcSym_VREF_ONDEMAND.setDescription("If this option is enabled, the voltage reference is disabled when no peripheral is requesting it.")
    supcSym_VREF_ONDEMAND.setDefaultValue(False)

    #VREF RUNSTDBY mode
    supcSym_VREF_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_VREF_RUNSTDBY", supcSym_VREF_Menu)
    supcSym_VREF_RUNSTDBY.setLabel("Enable Run in Standby")
    supcSym_VREF_RUNSTDBY.setDescription("Enable VREF operation in Standby Sleep Mode")

    #VREF VREFOE
    supcSym_VREF_VREFOE = supcComponent.createBooleanSymbol("SUPC_VREF_VREFOE", supcSym_VREF_Menu)
    supcSym_VREF_VREFOE.setLabel("Enable VREF output")
    supcSym_VREF_VREFOE.setDescription("Enable VREF connection to ADC. If ONDEMAND is 0 and VREF is enabled, Temperature Sensor cannot be used")
    supcSym_VREF_VREFOE.setDefaultValue(False)

    #VREF TSEN
    supcSym_VREF_TSEN = supcComponent.createBooleanSymbol("SUPC_VREF_TSEN", supcSym_VREF_Menu)
    supcSym_VREF_TSEN.setLabel("Enable Temperature Sensor")
    supcSym_VREF_TSEN.setDescription("Enable Temperature Sensor connection to ADC")
    supcSym_VREF_TSEN.setDefaultValue(False)
    supcSym_VREF_TSEN.setDependencies(updateVrefVisibleProperty, ["SUPC_VREF_ONDEMAND", "SUPC_VREF_VREFOE"])

    #BBPS Menu
    supcSym_BBPS_Menu= supcComponent.createMenuSymbol("SUPC_BBPS", None)
    supcSym_BBPS_Menu.setLabel("Battery Backup Power Switch Configuraiton")

    #BBPS supply switching
    supcSym_BBPS = supcComponent.createBooleanSymbol("SUPC_BBPS_WAKEEN", supcSym_BBPS_Menu)
    supcSym_BBPS.setLabel("Wake Device on BBPS Switching")
    supcSym_BBPS.setDescription("The device can be woken up when switched from battery backup power to Main Power.")

    #SUPC Output pin configuration
    #For pin names, refer 'Supply Controller Pinout' in Datasheet
    supcSym_BKOUT_Menu= supcComponent.createMenuSymbol("SUPC_BKOUT", None)
    supcSym_BKOUT_Menu.setLabel("SUPC Output pin configuraiton")

    #SUPC Output pin 0
    supcSym_BKOUT0 = supcComponent.createBooleanSymbol("SUPC_BKOUT_0", supcSym_BKOUT_Menu)
    supcSym_BKOUT0.setLabel("Enable OUT0")
    supcSym_BKOUT0.setDescription("OUT0 pin can be driven by SUPC. It can be toggled by SUPC, based on RTC Events")
    supcSym_BKOUT0.setDefaultValue(False)

    #RTCTGCL 0
    supcSym_BKOUT_RTCTGL0 = supcComponent.createBooleanSymbol("SUPC_BKOUT_RTCTGCL0", supcSym_BKOUT0)
    supcSym_BKOUT_RTCTGL0.setLabel("Toggle OUT0 on RTC Event")
    supcSym_BKOUT_RTCTGL0.setDescription("OUT0 pin can be toggled by SUPC, based on RTC Events")
    supcSym_BKOUT_RTCTGL0.setDependencies(updateSupcConfigVisibleProperty, ["SUPC_BKOUT_0"])
    supcSym_BKOUT_RTCTGL0.setVisible(False)

    #SUPC Output pin 1
    supcSym_BKOUT1 = supcComponent.createBooleanSymbol("SUPC_BKOUT_1", supcSym_BKOUT_Menu)
    supcSym_BKOUT1.setLabel("Enable OUT1")
    supcSym_BKOUT1.setDescription("OUT1 pin can be driven by SUPC. It can be toggled by SUPC, based on RTC Events")
    supcSym_BKOUT1.setDefaultValue(False)

    #RTCTGCL 1
    supcSym_BKOUT_RTCTGL1 = supcComponent.createBooleanSymbol("SUPC_BKOUT_RTCTGCL1", supcSym_BKOUT1)
    supcSym_BKOUT_RTCTGL1.setLabel("Toggle OUT1 on RTC Event")
    supcSym_BKOUT_RTCTGL1.setDescription("OUT1 pin can be toggled by SUPC, based on RTC Events")
    supcSym_BKOUT_RTCTGL1.setDependencies(updateSupcConfigVisibleProperty, ["SUPC_BKOUT_1"])
    supcSym_BKOUT_RTCTGL1.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = supcInstanceName.getValue() + "_BODDET_INTERRUPT_ENABLE"
    InterruptHandler = supcInstanceName.getValue() + "_BODDET_INTERRUPT_HANDLER"
    InterruptHandlerLock = supcInstanceName.getValue()+ "_BODDET_INTERRUPT_HANDLER_LOCK"

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcSym_HeaderFile = supcComponent.createFileSymbol("SUPC_HEADER", None)
    supcSym_HeaderFile.setSourcePath("../peripheral/supc_u2407/templates/plib_supc.h.ftl")
    supcSym_HeaderFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcSym_HeaderFile.setDestPath("/peripheral/supc/")
    supcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_HeaderFile.setType("HEADER")
    supcSym_HeaderFile.setMarkup(True)

    supcSym_SourceFile = supcComponent.createFileSymbol("SUPC_SOURCE", None)
    supcSym_SourceFile.setSourcePath("../peripheral/supc_u2407/templates/plib_supc.c.ftl")
    supcSym_SourceFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSym_SourceFile.setDestPath("/peripheral/supc/")
    supcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_SourceFile.setType("SOURCE")
    supcSym_SourceFile.setMarkup(True)

    supcSym_SystemInitFile = supcComponent.createFileSymbol("SUPC_SYS_INT", None)
    supcSym_SystemInitFile.setType("STRING")
    supcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSym_SystemInitFile.setSourcePath("../peripheral/supc_u2407/templates/system/initialization.c.ftl")
    supcSym_SystemInitFile.setMarkup(True)

    supcSym_SystemDefFile = supcComponent.createFileSymbol("SUPC_SYS_DEF", None)
    supcSym_SystemDefFile.setType("STRING")
    supcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSym_SystemDefFile.setSourcePath("../peripheral/supc_u2407/templates/system/definitions.h.ftl")
    supcSym_SystemDefFile.setMarkup(True)
