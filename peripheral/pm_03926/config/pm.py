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
global PMfilesArray
PMfilesArray = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updatePMClockWarringStatus(symbol, event):

    symbol.setVisible(not event["value"])

def fileUpdate(symbol, event):
    global PMfilesArray

    if event["value"] == False:
        PMfilesArray[0].setSecurity("SECURE")
        PMfilesArray[1].setSecurity("SECURE")
        PMfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        PMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    else:
        PMfilesArray[0].setSecurity("NON_SECURE")
        PMfilesArray[1].setSecurity("NON_SECURE")            
        PMfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        PMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
  

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pmComponent):
    pmInstanceName = pmComponent.createStringSymbol("PM_INSTANCE_NAME", None)
    pmInstanceName.setVisible(False)
    pmInstanceName.setDefaultValue(pmComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", pmInstanceName.getValue() + "_CLOCK_ENABLE", True)

    #Menu - Standby Sleep Config
    pmSym_Standby_Menu= pmComponent.createMenuSymbol("STANDBY_CONFIG", None)
    pmSym_Standby_Menu.setLabel("Standby Sleep Configuration")

    #System RAM Retention in Stanby Sleep
    pmSym_PM_STDBYCFG_RAMCFG = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_RAMCFG", pmSym_Standby_Menu)
    pmSym_PM_STDBYCFG_RAMCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_03926;register:STDBYCFG")
    pmSym_PM_STDBYCFG_RAMCFG.setLabel("System RAM Retention")
    pmSym_PM_STDBYCFG_RAMCFG.setOutputMode("Value")
    pmSym_PM_STDBYCFG_RAMCFG.setDisplayMode("Description")
    pmStandbySysRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"STDBYCFG__RAMCFG\"]")
    pmStandbySysRamValues = []
    pmStandbySysRamValues = pmStandbySysRamOptions.getChildren()
    for id in range(0,len(pmStandbySysRamValues)):
        pmSym_PM_STDBYCFG_RAMCFG.setDefaultValue(0)
        pmSym_PM_STDBYCFG_RAMCFG.addKey(pmStandbySysRamValues[id].getAttribute("name"), str(id), pmStandbySysRamValues[id].getAttribute("caption"))

    #Low Power RAM Enable in Stanby Sleep
    pmSym_PM_STDBYCFG_LPRAM = pmComponent.createBooleanSymbol("PM_STDBYCFG_LPRAM", pmSym_Standby_Menu)
    pmSym_PM_STDBYCFG_LPRAM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_03926;register:STDBYCFG")
    pmSym_PM_STDBYCFG_LPRAM.setLabel("Low Power RAM Enable")
    pmSym_PM_STDBYCFG_LPRAM.setDefaultValue(True)

    #Menu - Hibernate Sleep Config
    pmSym_Hibernate_Menu= pmComponent.createMenuSymbol("HIBERNATE_CONFIG", None)
    pmSym_Hibernate_Menu.setLabel("Hibernate Sleep Configuration")

    #System RAM Retention in Hibernate Sleep
    pmSym_PM_HIBCFG_RAMCFG = pmComponent.createKeyValueSetSymbol("PM_HIBCFG_RAMCFG", pmSym_Hibernate_Menu)
    pmSym_PM_HIBCFG_RAMCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_03926;register:HIBCFG")
    pmSym_PM_HIBCFG_RAMCFG.setLabel("System RAM Retention")
    pmSym_PM_HIBCFG_RAMCFG.setOutputMode("Value")
    pmSym_PM_HIBCFG_RAMCFG.setDisplayMode("Description")
    pmHibernateSysRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"HIBCFG__RAMCFG\"]")
    pmHibernateSysRamValues = []
    pmHibernateSysRamValues = pmHibernateSysRamOptions.getChildren()
    for id in range(0,len(pmHibernateSysRamValues)):
        pmSym_PM_HIBCFG_RAMCFG.setDefaultValue(0)
        pmSym_PM_HIBCFG_RAMCFG.addKey(pmHibernateSysRamValues[id].getAttribute("name"), str(id), pmHibernateSysRamValues[id].getAttribute("caption"))

    #Low Power RAM Enable in Hibernate Sleep
    pmSym_PM_HIBCFG_LPRAM = pmComponent.createBooleanSymbol("PM_HIBCFG_LPRAM", pmSym_Hibernate_Menu)
    pmSym_PM_HIBCFG_LPRAM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_03926;register:HIBCFG")
    pmSym_PM_HIBCFG_LPRAM.setLabel("Low Power RAM Enable")
    pmSym_PM_HIBCFG_LPRAM.setDefaultValue(True)

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
    pmSym_HeaderFile.setSourcePath("../peripheral/pm_03926/templates/plib_pm.h.ftl")
    pmSym_HeaderFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".h")
    pmSym_HeaderFile.setDestPath("/peripheral/pm/")
    pmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_HeaderFile.setType("HEADER")
    pmSym_HeaderFile.setMarkup(True)

    pmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE", None)
    pmSym_SourceFile.setSourcePath("../peripheral/pm_03926/templates/plib_pm.c.ftl")
    pmSym_SourceFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".c")
    pmSym_SourceFile.setDestPath("/peripheral/pm/")
    pmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_SourceFile.setType("SOURCE")
    pmSym_SourceFile.setMarkup(True)

    pmSym_SystemInitFile = pmComponent.createFileSymbol("PM_SYS_INIT", None)
    pmSym_SystemInitFile.setType("STRING")
    pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pmSym_SystemInitFile.setSourcePath("../peripheral/pm_u2240/templates/system/initialization.c.ftl")
    pmSym_SystemInitFile.setMarkup(True)

    pmSymSystemDefFile = pmComponent.createFileSymbol("PM_SYS_DEF", None)
    pmSymSystemDefFile.setType("STRING")
    pmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pmSymSystemDefFile.setSourcePath("../peripheral/pm_03926/templates/system/definitions.h.ftl")
    pmSymSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global PMfilesArray
        pmIsNonSecure = Database.getSymbolValue("core", pmComponent.getID().upper() + "_IS_NON_SECURE")
        PMfilesArray.append(pmSym_HeaderFile)
        PMfilesArray.append(pmSym_SourceFile)
        PMfilesArray.append(pmSym_SystemInitFile)
        PMfilesArray.append(pmSymSystemDefFile)        

        if pmIsNonSecure == False:
            pmSym_HeaderFile.setSecurity("SECURE")
            pmSym_SourceFile.setSecurity("SECURE")
            pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            pmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

        pmSymSystemDefFile.setDependencies(fileUpdate, ["core." + pmComponent.getID().upper() + "_IS_NON_SECURE"])    
