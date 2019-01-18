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
    
    #Menu - Standby Sleep Config
    pmSym_Standby_Menu= pmComponent.createMenuSymbol("STANDBY_CONFIG", None)
    pmSym_Standby_Menu.setLabel("Standby Sleep Configuration")
    
    #System RAM Retention in Stanby Sleep
    pmSym_PM_STDBYCFG_RAMCFG = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_RAMCFG", pmSym_Standby_Menu)
    pmSym_PM_STDBYCFG_RAMCFG.setLabel("System RAM Retention")
    pmSym_PM_STDBYCFG_RAMCFG.setOutputMode("Value")
    pmSym_PM_STDBYCFG_RAMCFG.setDisplayMode("Description")
    
    #Get options for System RAM Retention
    pmStandbySysRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__RAMCFG\"]")
    
    pmStandbySysRamValues = []
    pmStandbySysRamValues = pmStandbySysRamOptions.getChildren()
    
    for id in range(0,len(pmStandbySysRamValues)):
        pmSym_PM_STDBYCFG_RAMCFG.setDefaultValue(0)
        pmSym_PM_STDBYCFG_RAMCFG.addKey(pmStandbySysRamValues[id].getAttribute("name"), str(id), pmStandbySysRamValues[id].getAttribute("caption"))

    #Fast Wakeup
    pmSym_PM_STDBYCFG_FASTWKUP = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_FASTWKUP", pmSym_Standby_Menu)
    pmSym_PM_STDBYCFG_FASTWKUP.setLabel("Fast Wakeup for NVM and Main Regulator")
    pmSym_PM_STDBYCFG_FASTWKUP.setOutputMode("Value")
    pmSym_PM_STDBYCFG_FASTWKUP.setDisplayMode("Description")
    
    #Get options for Fast Wakeup
    pmStandbySleepFastWakeupOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__FASTWKUP\"]")
    
    pmStandbyFastWakeupOptionValues = []
    pmStandbyFastWakeupOptionValues = pmStandbySleepFastWakeupOptions.getChildren()
    
    for id in range(0,len(pmStandbyFastWakeupOptionValues)):
        pmSym_PM_STDBYCFG_FASTWKUP.setDefaultValue(0)
        pmSym_PM_STDBYCFG_FASTWKUP.addKey(pmStandbyFastWakeupOptionValues[id].getAttribute("name"), str(id), pmStandbyFastWakeupOptionValues[id].getAttribute("caption"))

    #Menu - Hibernate Sleep Config
    pmSym_Hibernate_Menu= pmComponent.createMenuSymbol("HIBERNATE_CONFIG", None)
    pmSym_Hibernate_Menu.setLabel("Hibernate Sleep Configuration")

    #System RAM Retention in Hibernate Sleep
    pmSym_PM_HIBCFG_RAMCFG = pmComponent.createKeyValueSetSymbol("PM_HIBCFG_RAMCFG", pmSym_Hibernate_Menu)
    pmSym_PM_HIBCFG_RAMCFG.setLabel("System RAM Retention")
    pmSym_PM_HIBCFG_RAMCFG.setOutputMode("Value")
    pmSym_PM_HIBCFG_RAMCFG.setDisplayMode("Description")
    
    #Get options for System RAM Retention
    pmHibernateSysRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_HIBCFG__RAMCFG\"]")
    
    pmHibernateSysRamValues = []
    pmHibernateSysRamValues = pmHibernateSysRamOptions.getChildren()
    
    for id in range(0,len(pmHibernateSysRamValues)):
        pmSym_PM_HIBCFG_RAMCFG.setDefaultValue(0)
        pmSym_PM_HIBCFG_RAMCFG.addKey(pmHibernateSysRamValues[id].getAttribute("name"), str(id), pmHibernateSysRamValues[id].getAttribute("caption"))
    
    #Backup RAM Retention in Hibernate Sleep
    pmSym_PM_HIBCFG_BRAMCFG = pmComponent.createKeyValueSetSymbol("PM_HIBCFG_BRAMCFG", pmSym_Hibernate_Menu)
    pmSym_PM_HIBCFG_BRAMCFG.setLabel("Backup RAM Retention")
    pmSym_PM_HIBCFG_BRAMCFG.setOutputMode("Value")
    pmSym_PM_HIBCFG_BRAMCFG.setDisplayMode("Description")
    
    #Get options for Backup RAM Retention
    pmHibernateBackupRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_HIBCFG__BRAMCFG\"]")
    
    pmHibernateBackupRamValues = []
    pmHibernateBackupRamValues = pmHibernateBackupRamOptions.getChildren()
    
    for id in range(0,len(pmHibernateBackupRamValues)):
        pmSym_PM_HIBCFG_BRAMCFG.setDefaultValue(0)
        pmSym_PM_HIBCFG_BRAMCFG.addKey(pmHibernateBackupRamValues[id].getAttribute("name"), str(id), pmHibernateBackupRamValues[id].getAttribute("caption"))
        
    #Menu - Backup Sleep Config
    pmSym_Backup_Menu= pmComponent.createMenuSymbol("BACKUP_CONFIG", None)
    pmSym_Backup_Menu.setLabel("Backup Sleep Configuration")
    
    #Backup RAM Retention in Backup Sleep
    pmSym_PM_BKUPCFG_BRAMCFG = pmComponent.createKeyValueSetSymbol("PM_BKUPCFG_BRAMCFG", pmSym_Backup_Menu)
    pmSym_PM_BKUPCFG_BRAMCFG.setLabel("Backup RAM Retention")
    pmSym_PM_BKUPCFG_BRAMCFG.setOutputMode("Value")
    pmSym_PM_BKUPCFG_BRAMCFG.setDisplayMode("Description")
    
    #Get options for Backup RAM Retention
    pmBackupSleepBackupRamOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_BKUPCFG__BRAMCFG\"]")
    
    pmBackupSleepBackupRamValues = []
    pmBackupSleepBackupRamValues = pmBackupSleepBackupRamOptions.getChildren()
    
    for id in range(0,len(pmBackupSleepBackupRamValues)):
        pmSym_PM_BKUPCFG_BRAMCFG.setDefaultValue(0)
        pmSym_PM_BKUPCFG_BRAMCFG.addKey(pmBackupSleepBackupRamValues[id].getAttribute("name"), str(id), pmBackupSleepBackupRamValues[id].getAttribute("caption"))
    
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
    pmSym_HeaderFile.setSourcePath("../peripheral/pm_u2406/templates/plib_pm.h.ftl")
    pmSym_HeaderFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".h")
    pmSym_HeaderFile.setDestPath("/peripheral/pm/")
    pmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_HeaderFile.setType("HEADER")
    pmSym_HeaderFile.setMarkup(True)

    pmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE", None)
    pmSym_SourceFile.setSourcePath("../peripheral/pm_u2406/templates/plib_pm.c.ftl")
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
    pmSymSystemDefFile.setSourcePath("../peripheral/pm_u2406/templates/system/definitions.h.ftl")
    pmSymSystemDefFile.setMarkup(True)
