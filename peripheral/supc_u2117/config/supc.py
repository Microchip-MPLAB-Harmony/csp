# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
global supcSym_BOD33_RUNBKUP
global supcInstanceName
global supcSym_INTENSET

def updateBODVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

def updateBODVDDPrescalerVisibleProperty(symbol, event):

    if supcSym_BODVDD_STDBYCFG.getValue() == 1 or supcSym_BODVDD_ACTCFG.getValue() == 1 or supcSym_BOD33_RUNBKUP.getValue() == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateVrefVisibleProperty(symbol, event):
    if supcSym_VREF_VREFOE.getValue() == True and supcSym_VREF_ONDEMAND.getValue() == False:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

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
    global supcSym_BOD33_RUNBKUP
    global supcSym_VREF_VREFOE
    global supcSym_VREF_ONDEMAND
    global supcInstanceName
    global supcSym_INTENSET
   
    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())
    
    #Parse parameters to show device specific functions (but uses the same IP)
    parameters = [];
    parametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SUPC\"]/instance@[name=\""+supcInstanceName.getValue()+"\"]/parameters")
    for parameter in parametersNode.getChildren():
        if "HAS_" in parameter.getAttribute("name"):
            parameters.append(parameter.getAttribute("name"))
            paramSym = supcComponent.createBooleanSymbol(parameter.getAttribute("name"), None)
            paramSym.setVisible(False)
            paramSym.setDefaultValue(True)

    supcSym_BODVDD_Menu= supcComponent.createMenuSymbol("BOD_MENU", None)
    supcSym_BODVDD_Menu.setLabel("VDD Brown-Out Detector (BOD) Configuration")

    global BODname
    if "HAS_BOD33_REG_NAME" in parameters:
        BODname = "BOD33"
    else:
        BODname = "BODVDD"
        
    supcBODName = supcComponent.createStringSymbol("SUPC_BOD_NAME", None)
    supcBODName.setVisible(False)
    supcBODName.setDefaultValue(BODname)
    
    #Interrupt mode
    supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRUPT_ENABLE", supcSym_BODVDD_Menu)
    supcSym_INTENSET.setLabel("Enable BOD Interrupt")
    supcSym_INTENSET.setDefaultValue(False)

    # Interrupt Warning status
    supcSym_IntEnComment = supcComponent.createCommentSymbol("SUPC_INTERRUPT_ENABLE_COMMENT", supcSym_BODVDD_Menu)
    supcSym_IntEnComment.setVisible(False)
    supcSym_IntEnComment.setLabel("Warning!!! SUPC Interrupt is Disabled in Interrupt Manager")
    supcSym_IntEnComment.setDependencies(interruptControl, [supcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE", "SUPC_INTERRUPT_ENABLE"])

    #BODVDD ACTCFG mode
    supcSym_BODVDD_ACTCFG = supcComponent.createKeyValueSetSymbol("SUPC_"+BODname+"_ACTCFG", supcSym_BODVDD_Menu)
    supcSym_BODVDD_ACTCFG.setLabel("Select Active mode operation")
    supcSym_BODVDD_ACTCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Active mode")
    supcSym_BODVDD_ACTCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_ACTCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_ACTCFG.setDefaultValue(0)
    supcSym_BODVDD_ACTCFG.setOutputMode("Value")
    supcSym_BODVDD_ACTCFG.setDisplayMode("Description")
    
    #BODVDD RUNSTDBY enable
    supcSym_BODVDD_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_"+BODname+"_RUNSTDBY", supcSym_BODVDD_Menu)
    supcSym_BODVDD_RUNSTDBY.setLabel("Run in Standby mode")
    supcSym_BODVDD_RUNSTDBY.setDescription("Configures BODVDD operation in Standby Sleep Mode")

    #BODVDD STDBYCFG mode
    supcSym_BODVDD_STDBYCFG = supcComponent.createKeyValueSetSymbol("SUPC_"+BODname+"_STDBYCFG", supcSym_BODVDD_Menu)
    supcSym_BODVDD_STDBYCFG.setLabel("Select Standby mode operation")
    supcSym_BODVDD_STDBYCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Standby Sleep mode")
    supcSym_BODVDD_STDBYCFG.addKey("CONT_MODE", "0", "Continuous Mode")
    supcSym_BODVDD_STDBYCFG.addKey("SAMP_MODE", "1", "Sampling Mode")
    supcSym_BODVDD_STDBYCFG.setDefaultValue(0)
    supcSym_BODVDD_STDBYCFG.setOutputMode("Value")
    supcSym_BODVDD_STDBYCFG.setDisplayMode("Description")
    supcSym_BODVDD_STDBYCFG.setVisible(False)
    supcSym_BODVDD_STDBYCFG.setDependencies(updateBODVisibleProperty, ["SUPC_"+BODname+"_RUNSTDBY"])

    if "HAS_RUNBKUP_BIT" in parameters:
        #BODVDD RUNBKUP enable
        supcSym_BOD33_RUNBKUP = supcComponent.createBooleanSymbol("SUPC_"+BODname+"_RUNBKUP", supcSym_BODVDD_Menu)
        supcSym_BOD33_RUNBKUP.setLabel("Run in Backup mode")
        supcSym_BOD33_RUNBKUP.setDescription("Configures BODVDD operation in Backup Sleep Mode")
        
    #BODVDD PSEL
    supcSym_BODVDD_PSEL = supcComponent.createKeyValueSetSymbol("SUPC_"+BODname+"_PSEL", supcSym_BODVDD_Menu)
    supcSym_BODVDD_PSEL.setLabel("Select Prescaler for Sampling Clock")
    supcSym_BODVDD_PSEL.setDescription("Configures the sampling clock prescaler when BODVDD is operating in sampling mode")
    supcSym_BODVDD_PSEL.setVisible(False)
    supcSym_BODVDD_PSEL.setDependencies(updateBODVDDPrescalerVisibleProperty, ["SUPC_"+BODname+"_STDBYCFG", "SUPC_"+BODname+"_ACTCFG", "SUPC_"+BODname+"_RUNBKUP"])

    supcBODVDDPselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_"+BODname+"__PSEL\"]")
    supcBODVDDPselValues = []
    supcBODVDDPselValues = supcBODVDDPselNode.getChildren()

    for index in range (0, len(supcBODVDDPselValues)):
        supcBODVDDPselKeyName = supcBODVDDPselValues[index].getAttribute("name")
        supcBODVDDPselKeyDescription = supcBODVDDPselValues[index].getAttribute("caption")
        supcBODVDDPselKeyValue =  supcBODVDDPselValues[index].getAttribute("value")
        supcSym_BODVDD_PSEL.addKey(supcBODVDDPselKeyName, supcBODVDDPselKeyValue, supcBODVDDPselKeyDescription)

    supcSym_BODVDD_PSEL.setDefaultValue(0)
    supcSym_BODVDD_PSEL.setOutputMode("Value")
    supcSym_BODVDD_PSEL.setDisplayMode("Description")

    if "HAS_VMON_BIT" in parameters:
        #BODVDD VMON selection
        supcSym_BOD33_VMON = supcComponent.createBooleanSymbol("SUPC_"+BODname+"_VMON", supcSym_BODVDD_Menu)
        supcSym_BOD33_VMON.setLabel("Monitor VBAT supply?")
        supcSym_BOD33_VMON.setDescription("BOD33 monitors either VDD or VBAT in active and standby mode")

    #VREG Menu
    supcSym_VREG_Menu= supcComponent.createMenuSymbol("VREG_MENU", None)
    supcSym_VREG_Menu.setLabel("Voltage Regulator (VREG) Configuration")

    if "HAS_SEL_BIT" in parameters:    
        #Select LDO or BUCK regulator
        supcSym_VREG_SEL = supcComponent.createBooleanSymbol("SUPC_VREG_SEL", supcSym_VREG_Menu)
        supcSym_VREG_SEL.setLabel("Use Buck regulator instead of LDO")
        supcSym_VREG_SEL.setDefaultValue(0)
        supcSym_VREG_SEL.setDescription("When this option is selected, the voltage regulator used will be the Buck Regulator. Refer schematic checklist for Inductor connection.")

    #VREG RUNSTDBY mode
    supcSym_VREG_RUNSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREG_RUNSTDBY", supcSym_VREG_Menu)
    supcSym_VREG_RUNSTDBY.setLabel("Select Standby mode operation")
    supcSym_VREG_RUNSTDBY.setDescription("Configures VREG operation in Standby Sleep Mode")
    supcSym_VREG_RUNSTDBY.addKey("LP_OP", "0", "Low Power Operation")
    supcSym_VREG_RUNSTDBY.addKey("NORMAL_OP", "1", "Normal Operation")
    supcSym_VREG_RUNSTDBY.setDefaultValue(0)
    supcSym_VREG_RUNSTDBY.setOutputMode("Value")
    supcSym_VREG_RUNSTDBY.setDisplayMode("Description")
    
    
    if "HAS_STDBYPL0_BIT" in parameters:
        #VREG performance level in standby sleep
        supcSym_VREG_STDBYPL0 = supcComponent.createBooleanSymbol("SUPC_VREG_STDBYPL0", supcSym_VREG_Menu)
        supcSym_VREG_STDBYPL0.setLabel("Regulator operation in PL0 in Stanby sleep")
        supcSym_VREG_STDBYPL0.setDefaultValue(1)
        supcSym_VREG_STDBYPL0.setDescription("In Standby sleep mode, the voltage regulator can be configured to set VDDCORE at PL0 voltage level")
    
    if "HAS_LPEFF_BIT" in parameters:    
        #VREG Low power Mode Efficiency
        supcSym_VREG_LPEFF = supcComponent.createBooleanSymbol("SUPC_VREG_LPEFF", supcSym_VREG_Menu)
        supcSym_VREG_LPEFF.setLabel("Increase low power mode efficiency")
        supcSym_VREG_LPEFF.setDefaultValue(0)
        supcSym_VREG_LPEFF.setDescription("When this is set to 1, the voltage regulator in Low power mode has the highest efficiency but it supports a limited VDD range (2.5V to 3.6V).")

    #VREF Menu    
    supcSym_VREF_Menu= supcComponent.createMenuSymbol("VREF_MENU", None)
    supcSym_VREF_Menu.setLabel("Voltage Reference (VREF) Configuration")

    #VREF VREFOE mode
    supcSym_VREF_VREFOE = supcComponent.createBooleanSymbol("SUPC_VREF_VREFOE", supcSym_VREF_Menu)
    supcSym_VREF_VREFOE.setLabel("Enable Voltage Reference Output")
    supcSym_VREF_VREFOE.setDescription("Voltage Reference Output Enable")
    supcSym_VREF_VREFOE.setDefaultValue(False)

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
    supcSym_VREF_SEL.setOutputMode("Value")
    supcSym_VREF_SEL.setDisplayMode("Description")

    #VREF ONDEMAND mode
    supcSym_VREF_ONDEMAND = supcComponent.createBooleanSymbol("SUPC_VREF_ONDEMAND", supcSym_VREF_Menu)
    supcSym_VREF_ONDEMAND.setLabel("Enable On demand")
    supcSym_VREF_ONDEMAND.setDescription("If this option is enabled, the voltage reference is disabled when no peripheral is requesting it.")
    supcSym_VREF_ONDEMAND.setDefaultValue(False)

    if "HAS_NO_TSEN" not in parameters:
        #VREF TSEN
        supcSym_VREF_TSEN = supcComponent.createBooleanSymbol("SUPC_VREF_TSEN", supcSym_VREF_Menu)
        supcSym_VREF_TSEN.setLabel("Enable Temperature Sensor")
        supcSym_VREF_TSEN.setDescription("Enable Temperature Sensor connection to ADC")
        supcSym_VREF_TSEN.setDefaultValue(False)
        supcSym_VREF_TSEN.setDependencies(updateVrefVisibleProperty, ["SUPC_VREF_ONDEMAND", "SUPC_VREF_VREFOE"])
  
    #VREF RUNSTDBY mode
    supcSym_VREF_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_VREF_RUNSTDBY", supcSym_VREF_Menu)
    supcSym_VREF_RUNSTDBY.setLabel("Run in Standby mode")
    supcSym_VREF_RUNSTDBY.setDescription("Enable VREF operation in Standby Sleep Mode")

    if "HAS_BBPS_REG" in parameters:
        #BBPS Menu
        supcSym_BBPS_Menu= supcComponent.createMenuSymbol("SUPC_BBPS", None)
        supcSym_BBPS_Menu.setLabel("Battery Backup Power Switch Configuraiton")

        #BBPS WAKEEN
        supcSym_BBPS = supcComponent.createBooleanSymbol("SUPC_BBPS_WAKEEN", supcSym_BBPS_Menu)
        supcSym_BBPS.setLabel("Wake Device on BBPS Switching")
        supcSym_BBPS.setDescription("The device can be woken up when switched from battery backup power to Main Power.")

        #Battery Backup Power Switch Configuration
        supcSym_BBPS_CONF = supcComponent.createKeyValueSetSymbol("SUPC_BBPS_CONF", supcSym_BBPS_Menu)
        supcSym_BBPS_CONF.setLabel("Select Reference Voltage Level")
        supcSym_BBPS_CONF.setDescription("Configures VREF voltage level")

        supcVREFSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_BBPS__CONF\"]")
        supcBBPSConfValues = []
        supcBBPSConfValues = supcVREFSelectionNode.getChildren()

        for index in range (0, len(supcBBPSConfValues)):
            supcBBPSConfKeyName = supcBBPSConfValues[index].getAttribute("name")
            supcBBPSConfKeyDescription = supcBBPSConfValues[index].getAttribute("caption")
            supcBBPSConfKeyValue =  supcBBPSConfValues[index].getAttribute("value")
            supcSym_BBPS_CONF.addKey(supcBBPSConfKeyName, supcBBPSConfKeyValue, supcBBPSConfKeyDescription)

        supcSym_BBPS_CONF.setDefaultValue(0)
        supcSym_BBPS_CONF.setOutputMode("Key")
        supcSym_BBPS_CONF.setDisplayMode("Description")
        
        #BBPS supply switching
        supcSym_PSOKEN = supcComponent.createBooleanSymbol("SUPC_BBPS_PSOKEN", supcSym_BBPS_Menu)
        supcSym_PSOKEN.setLabel("Use PSOK pin for supply switching?")
        supcSym_PSOKEN.setDefaultValue(0)
        supcSym_PSOKEN.setDescription("If APWS is not used, when the Main Power Supply OK Pin Enable bit in the BBPS register is written to '1' (BBPS.PSOKEN), restoring VDD will form a low-to-high transition on the PSOK pin. This low-to-high transition will switch the Backup Power Supply back to VDD.")
    
    if "HAS_BKOUT_REG" in parameters:    
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
        supcSym_BKOUT_RTCTGL0.setDependencies(updateBODVisibleProperty, ["SUPC_BKOUT_0"])
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
        supcSym_BKOUT_RTCTGL1.setDependencies(updateBODVisibleProperty, ["SUPC_BKOUT_1"])
        supcSym_BKOUT_RTCTGL1.setVisible(False)
    
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]")
    supcModuleID = supcModuleNode.getAttribute("id")

    supcSym_HeaderFile = supcComponent.createFileSymbol("SUPC_HEADER", None)
    supcSym_HeaderFile.setSourcePath("../peripheral/supc_u2117/templates/plib_supc.h.ftl")
    supcSym_HeaderFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcSym_HeaderFile.setDestPath("/peripheral/supc/")
    supcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_HeaderFile.setType("HEADER")
    supcSym_HeaderFile.setMarkup(True)

    supcSym_SourceFile = supcComponent.createFileSymbol("SUPC_SOURCE", None)
    supcSym_SourceFile.setSourcePath("../peripheral/supc_u2117/templates/plib_supc.c.ftl")
    supcSym_SourceFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSym_SourceFile.setDestPath("/peripheral/supc/")
    supcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_SourceFile.setType("SOURCE")
    supcSym_SourceFile.setMarkup(True)

    supcSym_SystemInitFile = supcComponent.createFileSymbol("SUPC_SYS_INT", None)
    supcSym_SystemInitFile.setType("STRING")
    supcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSym_SystemInitFile.setSourcePath("../peripheral/supc_u2117/templates/system/initialization.c.ftl")
    supcSym_SystemInitFile.setMarkup(True)

    supcSym_SystemDefFile = supcComponent.createFileSymbol("SUPC_SYS_DEF", None)
    supcSym_SystemDefFile.setType("STRING")
    supcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSym_SystemDefFile.setSourcePath("../peripheral/supc_u2117/templates/system/definitions.h.ftl")
    supcSym_SystemDefFile.setMarkup(True)
