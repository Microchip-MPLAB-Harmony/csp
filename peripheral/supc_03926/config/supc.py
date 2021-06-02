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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def interruptControl(symbol, event):
    Database.setSymbolValue("core", InterruptVector, event["value"])
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"])
    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_InterruptHandler")
    else:
        Database.setSymbolValue("core", InterruptHandler, supcInstanceName.getValue() + "_Handler")

def interruptEnableComment(symbol, event):
    if (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_INTERRUPT_ENABLE") == True):
        symbol.setVisible(event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(supcComponent):
    global supcInstanceName
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global supcSym_INTENSET

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())

    InterruptVector = supcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = supcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = supcInstanceName.getValue()+ "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = supcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    #BORVDDUSB Interrupt Enable
    supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRUPT_ENABLE", None)
    supcSym_INTENSET.setLabel("Enable BORVDDUSB Interrupt")
    supcSym_INTENSET.setDefaultValue(False)
    supcSym_INTENSET.setDependencies(interruptControl, ["SUPC_INTERRUPT_ENABLE"])

    # Interrupt Warning status
    supcSym_IntEnComment = supcComponent.createCommentSymbol("SUPC_INTERRUPT_ENABLE_COMMENT", None)
    supcSym_IntEnComment.setVisible(False)
    supcSym_IntEnComment.setLabel("Warning!!! SUPC Interrupt is Disabled in Interrupt Manager")
    supcSym_IntEnComment.setDependencies(interruptEnableComment, ["core." + InterruptVectorUpdate])

    #BOR Menu
    supcSym_BOR_Menu= supcComponent.createMenuSymbol("SUPC_BOR_MENU", None)
    supcSym_BOR_Menu.setLabel("Brown-Out Reset (BOR) Configuration")

    #BOR DCBORPSEL
    supcSym_BOR_DCBORPSEL = supcComponent.createKeyValueSetSymbol("SUPC_BOR_DCBORPSEL", supcSym_BOR_Menu)
    supcSym_BOR_DCBORPSEL.setLabel("Select Duty Cycle BOR Prescaler")
    supcBORDcborpselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"BOR__DCBORPSEL\"]")
    supcDcborpselValues = []
    supcDcborpselValues = supcBORDcborpselNode.getChildren()
    for index in range (0, len(supcDcborpselValues)):
        supcDcborpselKeyName = supcDcborpselValues[index].getAttribute("name")
        supcDcborpselKeyDescription = supcDcborpselValues[index].getAttribute("caption")
        supcDcborpselKeyValue =  supcDcborpselValues[index].getAttribute("value")
        supcSym_BOR_DCBORPSEL.addKey(supcDcborpselKeyName, supcDcborpselKeyValue, supcDcborpselKeyDescription)
    supcSym_BOR_DCBORPSEL.setDefaultValue(1)
    supcSym_BOR_DCBORPSEL.setOutputMode("Value")
    supcSym_BOR_DCBORPSEL.setDisplayMode("Description")

    #BOR BORFILT
    supcSym_BOR_BORFILT = supcComponent.createKeyValueSetSymbol("SUPC_BOR_BORFILT", supcSym_BOR_Menu)
    supcSym_BOR_BORFILT.setLabel("BOR Filtering")
    supcBORFiltNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"BOR__BORFILT\"]")
    supcBORFiltValues = []
    supcBORFiltValues = supcBORFiltNode.getChildren()
    for index in range (0, len(supcBORFiltValues)):
        supcBORFiltKeyName = supcBORFiltValues[index].getAttribute("name")
        supcBORFiltKeyDescription = supcBORFiltValues[index].getAttribute("caption")
        supcBORFiltKeyValue =  supcBORFiltValues[index].getAttribute("value")
        supcSym_BOR_BORFILT.addKey(supcBORFiltKeyName, supcBORFiltKeyValue, supcBORFiltKeyDescription)
    supcSym_BOR_BORFILT.setDefaultValue(0)
    supcSym_BOR_BORFILT.setOutputMode("Value")
    supcSym_BOR_BORFILT.setDisplayMode("Description")

    #LVD Menu
    supcSym_LVD_Menu= supcComponent.createMenuSymbol("SUPC_LVD_MENU", None)
    supcSym_LVD_Menu.setLabel("Low Voltage Detect (LVD) Configuration")

    #LVD Enable
    supcSym_LVD_Enable = supcComponent.createBooleanSymbol("SUPC_LVD_ENABLE", supcSym_LVD_Menu)
    supcSym_LVD_Enable.setLabel("Enable")

    #LVD DIR
    supcSym_LVD_DIR = supcComponent.createKeyValueSetSymbol("SUPC_LVD_DIR", supcSym_LVD_Menu)
    supcSym_LVD_DIR.setLabel("Direction")
    supcLvdDirNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"LVD__DIR\"]")
    supcLvdDirValues = []
    supcLvdDirValues = supcLvdDirNode.getChildren()
    for index in range (0, len(supcLvdDirValues)):
        supcLvdDirKeyName = supcLvdDirValues[index].getAttribute("name")
        supcLvdDirKeyDescription = supcLvdDirValues[index].getAttribute("caption")
        supcLvdDirKeyValue =  supcLvdDirValues[index].getAttribute("value")
        supcSym_LVD_DIR.addKey(supcLvdDirKeyName, supcLvdDirKeyValue, supcLvdDirKeyDescription)
    supcSym_LVD_DIR.setDefaultValue(0)
    supcSym_LVD_DIR.setOutputMode("Value")
    supcSym_LVD_DIR.setDisplayMode("Description")

    #LVD OEVEN
    supcSym_LVD_Oeven = supcComponent.createBooleanSymbol("SUPC_LVD_OEVEN", supcSym_LVD_Menu)
    supcSym_LVD_Oeven.setLabel("Output Event Enable")

    #LVD RUNSTDBY
    supcSym_LVD_RunStdby = supcComponent.createBooleanSymbol("SUPC_LVD_RUNSTDBY", supcSym_LVD_Menu)
    supcSym_LVD_RunStdby.setLabel("Run during Standby")

    #VREG Menu
    supcSym_VREGControl_Menu= supcComponent.createMenuSymbol("SUPC_VREG_MENU", None)
    supcSym_VREGControl_Menu.setLabel("Voltage Regulator (VREG) Configuration")

    #VREG Output Control in RUN mode
    supcSym_VREGCTRL_VREGOUT = supcComponent.createKeyValueSetSymbol("SUPC_VREGCTRL_VREGOUT", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_VREGOUT.setLabel("VREG Output Control in RUN mode")
    supcVregOutNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"VREGCTRL__VREGOUT\"]")
    supcVregOutValues = []
    supcVregOutValues = supcVregOutNode.getChildren()
    for index in range (0, len(supcVregOutValues)):
        supcVregOutKeyName = supcVregOutValues[index].getAttribute("name")
        supcVregOutKeyDescription = supcVregOutValues[index].getAttribute("caption")
        supcVregOutKeyValue =  supcVregOutValues[index].getAttribute("value")
        supcSym_VREGCTRL_VREGOUT.addKey(supcVregOutKeyName, supcVregOutKeyValue, supcVregOutKeyDescription)
    supcSym_VREGCTRL_VREGOUT.setDefaultValue(0)
    supcSym_VREGCTRL_VREGOUT.setOutputMode("Value")
    supcSym_VREGCTRL_VREGOUT.setDisplayMode("Description")

    #Off in Standby Control for VREGSW[N-1]
    supcSym_VREGCTRL_OFFSTDBY = supcComponent.createBooleanSymbol("SUPC_VREGCTRL_OFFSTDBY", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_OFFSTDBY.setLabel("Off in Standby Control")

    #Low Voltage Standby Enable
    supcSym_VREGCTRL_LVSTDBY = supcComponent.createBooleanSymbol("SUPC_VREGCTRL_LVSTDBY", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_LVSTDBY.setLabel("Low Voltage Standby Enable")
    supcSym_VREGCTRL_LVSTDBY.setDefaultValue(True)

    #Low Voltage Hibernate Enable
    supcSym_VREGCTRL_LVHIB = supcComponent.createBooleanSymbol("SUPC_VREGCTRL_LVHIB", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_LVHIB.setLabel("Low Voltage Hibernate Enable")
    supcSym_VREGCTRL_LVHIB.setDefaultValue(True)

    #Charge Pump Enable and Auto-enable
    supcSym_VREGCTRL_CPEN = supcComponent.createBooleanSymbol("SUPC_VREGCTRL_CPEN", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_CPEN.setLabel("Charge Pump Enable and Auto-enable")

    #Additional Voltage Regulator Enable
    supcSym_VREGCTRL_AVREGEN = supcComponent.createBooleanSymbol("SUPC_VREGCTRL_AVREGEN", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_AVREGEN.setLabel("Additional Voltage Regulator Enable")
    supcSym_VREGCTRL_AVREGEN.setDefaultValue(True)

    #Additional Voltage Regulator Configuration
    supcSym_VREGCTRL_AVREGSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREGCTRL_AVREGSTDBY", supcSym_VREGControl_Menu)
    supcSym_VREGCTRL_AVREGSTDBY.setLabel("Additional Voltage Regulator Configuration")
    supcAvregStdbyNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"VREGCTRL__AVREGSTDBY\"]")
    supcAvregStdbyValues = []
    supcAvregStdbyValues = supcAvregStdbyNode.getChildren()
    for index in range (0, len(supcAvregStdbyValues)):
        supcAvregStdbyKeyName = supcAvregStdbyValues[index].getAttribute("name")
        supcAvregStdbyKeyDescription = supcAvregStdbyValues[index].getAttribute("caption")
        supcAvregStdbyKeyValue =  supcAvregStdbyValues[index].getAttribute("value")
        supcSym_VREGCTRL_AVREGSTDBY.addKey(supcAvregStdbyKeyName, supcAvregStdbyKeyValue, supcAvregStdbyKeyDescription)
    supcSym_VREGCTRL_AVREGSTDBY.setDefaultValue(1)
    supcSym_VREGCTRL_AVREGSTDBY.setOutputMode("Value")
    supcSym_VREGCTRL_AVREGSTDBY.setDisplayMode("Description")

    #VREF Menu
    supcSym_VREF_Menu= supcComponent.createMenuSymbol("VREF_MENU", None)
    supcSym_VREF_Menu.setLabel("Voltage Reference (VREF) Configuration")

    #Bandgap and Regulators Low Power Standby
    supcSym_VREF_LPSTDBY = supcComponent.createKeyValueSetSymbol("SUPC_VREF_LPSTDBY", supcSym_VREF_Menu)
    supcSym_VREF_LPSTDBY.setLabel("Enable Bandgap and Regulators Low Power Standby")
    supcLPStdbyNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"VREFCTRL__LPSTDBY\"]")
    supcLPStdbyValues = []
    supcLPStdbyValues = supcLPStdbyNode.getChildren()
    for index in range (0, len(supcLPStdbyValues)):
        supcLPStdbyKeyName = supcLPStdbyValues[index].getAttribute("name")
        supcLPStdbyKeyDescription = supcLPStdbyValues[index].getAttribute("caption")
        supcLPStdbyKeyValue =  supcLPStdbyValues[index].getAttribute("value")
        supcSym_VREF_LPSTDBY.addKey(supcLPStdbyKeyName, supcLPStdbyKeyValue, supcLPStdbyKeyDescription)
    supcSym_VREF_LPSTDBY.setDefaultValue(1)
    supcSym_VREF_LPSTDBY.setOutputMode("Value")
    supcSym_VREF_LPSTDBY.setDisplayMode("Description")

    #Bandgap and Regulators Low Power Hibernate
    supcSym_VREF_LPHIB = supcComponent.createKeyValueSetSymbol("SUPC_VREF_LPHIB", supcSym_VREF_Menu)
    supcSym_VREF_LPHIB.setLabel("Enable Bandgap and Regulators Low Power Hibernate")
    supcLPHibNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"VREFCTRL__LPHIB\"]")
    supcLPHibValues = []
    supcLPHibValues = supcLPHibNode.getChildren()
    for index in range (0, len(supcLPHibValues)):
        supcLPHibKeyName = supcLPHibValues[index].getAttribute("name")
        supcLPHibKeyDescription = supcLPHibValues[index].getAttribute("caption")
        supcLPHibKeyValue =  supcLPHibValues[index].getAttribute("value")
        supcSym_VREF_LPHIB.addKey(supcLPHibKeyName, supcLPHibKeyValue, supcLPHibKeyDescription)
    supcSym_VREF_LPHIB.setDefaultValue(1)
    supcSym_VREF_LPHIB.setOutputMode("Value")
    supcSym_VREF_LPHIB.setDisplayMode("Description")

    #VREF TSEN
    supcSym_VREF_TSEN = supcComponent.createBooleanSymbol("SUPC_VREF_TSEN", supcSym_VREF_Menu)
    supcSym_VREF_TSEN.setLabel("Enable Temperature Sensor Output")
    supcSym_VREF_TSEN.setDefaultValue(False)

    #SUPC Output pin configuration
    #For pin names, refer 'Supply Controller Pinout' in Datasheet
    supcSym_BKOUT_Menu= supcComponent.createMenuSymbol("SUPC_BKOUT", None)
    supcSym_BKOUT_Menu.setLabel("SUPC Output pin configuraiton")

    #SUPC Output pin 0
    supcSym_BKOUT0 = supcComponent.createBooleanSymbol("SUPC_BKOUT_0", supcSym_BKOUT_Menu)
    supcSym_BKOUT0.setLabel("Enable OUT0")
    supcSym_BKOUT0.setDescription("OUT0 pin can be driven by SUPC. It can be toggled by SUPC, based on Toggle Output Mode")
    supcSym_BKOUT0.setDefaultValue(False)

    #TGLOM 0
    supcSym_BKOUT_TGLOM0 = supcComponent.createKeyValueSetSymbol("SUPC_BKOUT_TGLOM0", supcSym_BKOUT0)
    supcSym_BKOUT_TGLOM0.setLabel("Toggle Output Mode 0")
    supcTglomNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"BKOUT__TGLOM\"]")
    supcTglomValues = []
    supcTglomValues = supcTglomNode.getChildren()
    for index in range (0, len(supcTglomValues)):
        supcTglom0KeyName = supcTglomValues[index].getAttribute("name")
        supcTglom0KeyDescription = supcTglomValues[index].getAttribute("caption")
        supcTglom0KeyValue =  supcTglomValues[index].getAttribute("value")
        supcSym_BKOUT_TGLOM0.addKey(supcTglom0KeyName, supcTglom0KeyValue, supcTglom0KeyDescription)
    supcSym_BKOUT_TGLOM0.setDefaultValue(0)
    supcSym_BKOUT_TGLOM0.setOutputMode("Value")
    supcSym_BKOUT_TGLOM0.setDisplayMode("Description")

    #SUPC Output pin 1
    supcSym_BKOUT1 = supcComponent.createBooleanSymbol("SUPC_BKOUT_1", supcSym_BKOUT_Menu)
    supcSym_BKOUT1.setLabel("Enable OUT1")
    supcSym_BKOUT1.setDescription("OUT1 pin can be driven by SUPC. It can be toggled by SUPC, based on Toggle Output Mode")
    supcSym_BKOUT1.setDefaultValue(False)

    #TGLOM 1
    supcSym_BKOUT_TGLOM1 = supcComponent.createKeyValueSetSymbol("SUPC_BKOUT_TGLOM1", supcSym_BKOUT1)
    supcSym_BKOUT_TGLOM1.setLabel("Toggle Output Mode 1")
    for index in range (0, len(supcTglomValues)):
        supcTglom1KeyName = supcTglomValues[index].getAttribute("name")
        supcTglom1KeyDescription = supcTglomValues[index].getAttribute("caption")
        supcTglom1KeyValue =  supcTglomValues[index].getAttribute("value")
        supcSym_BKOUT_TGLOM1.addKey(supcTglom1KeyName, supcTglom1KeyValue, supcTglom1KeyDescription)
    supcSym_BKOUT_TGLOM1.setDefaultValue(0)
    supcSym_BKOUT_TGLOM1.setOutputMode("Value")
    supcSym_BKOUT_TGLOM1.setDisplayMode("Description")

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcSym_HeaderFile = supcComponent.createFileSymbol("SUPC_HEADER", None)
    supcSym_HeaderFile.setSourcePath("../peripheral/supc_03926/templates/plib_supc.h.ftl")
    supcSym_HeaderFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcSym_HeaderFile.setDestPath("/peripheral/supc/")
    supcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_HeaderFile.setType("HEADER")
    supcSym_HeaderFile.setMarkup(True)

    supcSym_SourceFile = supcComponent.createFileSymbol("SUPC_SOURCE", None)
    supcSym_SourceFile.setSourcePath("../peripheral/supc_03926/templates/plib_supc.c.ftl")
    supcSym_SourceFile.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSym_SourceFile.setDestPath("/peripheral/supc/")
    supcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSym_SourceFile.setType("SOURCE")
    supcSym_SourceFile.setMarkup(True)

    supcSym_SystemInitFile = supcComponent.createFileSymbol("SUPC_SYS_INT", None)
    supcSym_SystemInitFile.setType("STRING")
    supcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSym_SystemInitFile.setSourcePath("../peripheral/supc_03926/templates/system/initialization.c.ftl")
    supcSym_SystemInitFile.setMarkup(True)

    supcSym_SystemDefFile = supcComponent.createFileSymbol("SUPC_SYS_DEF", None)
    supcSym_SystemDefFile.setType("STRING")
    supcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSym_SystemDefFile.setSourcePath("../peripheral/supc_03926/templates/system/definitions.h.ftl")
    supcSym_SystemDefFile.setMarkup(True)
