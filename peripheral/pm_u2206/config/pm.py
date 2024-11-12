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

global pmSym_PM_Standby

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updatePMClockWarringStatus(symbol, event):

    symbol.setVisible(not event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pmComponent):
    
    pmSym_RCAUSE = []
    
    pmInstanceName = pmComponent.createStringSymbol("PM_INSTANCE_NAME", None)
    pmInstanceName.setVisible(False)
    pmInstanceName.setDefaultValue(pmComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", pmInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    
    #Idle Sleep configuration
    pmSym_PM_SLEEP_IDLE = pmComponent.createKeyValueSetSymbol("PM_SLEEP_IDLE_OPTION", None)
    pmSym_PM_SLEEP_IDLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2206;register:SLEEP")
    pmSym_PM_SLEEP_IDLE.setLabel("Idle Sleep - Mode Configuration")
    pmSym_PM_SLEEP_IDLE.setOutputMode("Value")
    pmSym_PM_SLEEP_IDLE.setDisplayMode("Description")
    
    #Get different modes for Idle Sleep
    pmIdleSleepOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_SLEEP__IDLE\"]")
    
    pmIdleSleepOptionValues = []
    pmIdleSleepOptionValues = pmIdleSleepOptions.getChildren()
    
    for id in range(0,len(pmIdleSleepOptionValues)):
        pmSym_PM_SLEEP_IDLE_Key_Name = pmIdleSleepOptionValues[id].getAttribute("value")
        pmSym_PM_SLEEP_IDLE.setDefaultValue(0)
        pmSym_PM_SLEEP_IDLE.addKey(pmIdleSleepOptionValues[id].getAttribute("name"), str(id), pmIdleSleepOptionValues[id].getAttribute("caption"))
    
    #Get different options for reset cause
    pmResetCause = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PM"]/register-group@[name="PM"]/register@[name="RCAUSE"]')

    pmSym_RCAUSE_Index = pmComponent.createIntegerSymbol("PM_RCAUSE_OPTIONS", None)
    pmSym_RCAUSE_Index.setDefaultValue(len(pmResetCause.getChildren()))
    pmSym_RCAUSE_Index.setVisible(False)

    Log.writeInfoMessage(str(pmResetCause.getChildren()))
    
    for id in range(0,len(pmResetCause.getChildren())):
        pmSym_RCAUSE.append(id)
        pmSym_RCAUSE[id] = pmComponent.createKeyValueSetSymbol("PM_RCAUSE"+str(id), None)
        pmSym_RCAUSE[id].setLabel(str(pmResetCause.getChildren()[id].getAttribute("caption")))
        pmSym_RCAUSE[id].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2206;register:RCAUSE")
        pmSym_RCAUSE[id].addKey(pmResetCause.getChildren()[id].getAttribute("name"), str(id), pmResetCause.getChildren()[id].getAttribute("caption"))
        pmSym_RCAUSE[id].setOutputMode("Key")
        pmSym_RCAUSE[id].setDisplayMode("Description")
        pmSym_RCAUSE[id].setVisible(False)

    # Clock Warning status
    pmSym_ClkEnComment = pmComponent.createCommentSymbol("PM_CLOCK_ENABLE_COMMENT", None)
    pmSym_ClkEnComment.setLabel("Warning!!! PM Peripheral Clock is Disabled in Clock Manager")
    pmSym_ClkEnComment.setVisible(False)
    pmSym_ClkEnComment.setDependencies(updatePMClockWarringStatus, ["core." + pmInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pmModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]")
    pmModuleID = pmModuleNode.getAttribute("id")

    pmSym_HeaderFile = pmComponent.createFileSymbol("PM_HEADER", None)
    pmSym_HeaderFile.setSourcePath("../peripheral/pm_u2206/templates/plib_pm.h.ftl")
    pmSym_HeaderFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".h")
    pmSym_HeaderFile.setDestPath("/peripheral/pm/")
    pmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_HeaderFile.setType("HEADER")
    pmSym_HeaderFile.setMarkup(True)

    pmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE", None)
    pmSym_SourceFile.setSourcePath("../peripheral/pm_u2206/templates/plib_pm.c.ftl")
    pmSym_SourceFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".c")
    pmSym_SourceFile.setDestPath("/peripheral/pm/")
    pmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_SourceFile.setType("SOURCE")
    pmSym_SourceFile.setMarkup(True)

    pmSymSystemDefFile = pmComponent.createFileSymbol("PM_SYS_DEF", None)
    pmSymSystemDefFile.setType("STRING")
    pmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pmSymSystemDefFile.setSourcePath("../peripheral/pm_u2206/templates/system/definitions.h.ftl")
    pmSymSystemDefFile.setMarkup(True)
