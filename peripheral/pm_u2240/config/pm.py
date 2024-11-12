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
global PMfilesArray
PMfilesArray = []

def fileUpdate(symbol, event):
    global PMfilesArray
    if event["value"] == False:
        PMfilesArray[0].setSecurity("SECURE")
        PMfilesArray[1].setSecurity("SECURE")
        PMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        PMfilesArray[4].setEnabled(False)
        PMfilesArray[5].setEnabled(False)
        PMfilesArray[6].setEnabled(False)


    else:
        PMfilesArray[0].setSecurity("NON_SECURE")
        PMfilesArray[1].setSecurity("NON_SECURE")
        PMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        PMfilesArray[4].setEnabled(True)
        PMfilesArray[5].setEnabled(True)
        PMfilesArray[6].setEnabled(True)


def updatePMClockWarringStatus(symbol, event):

    symbol.setVisible(not event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pmComponent):

    pmInstanceName = pmComponent.createStringSymbol("PM_INSTANCE_NAME", None)
    pmInstanceName.setVisible(False)
    pmInstanceName.setDefaultValue(pmComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", pmInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    #Parse parameters to show device specific functions (but uses the same IP)
    parameters = [];
    parametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PM\"]/instance@[name=\""+pmInstanceName.getValue()+"\"]/parameters")
    for parameter in parametersNode.getChildren():
        if "HAS_" in parameter.getAttribute("name"):

            parameters.append(parameter.getAttribute("name"))
            paramSym = pmComponent.createBooleanSymbol(parameter.getAttribute("name"), None)
            paramSym.setVisible(False)
            paramSym.setDefaultValue(True)

    if "HAS_PLCFG" in parameters:
        #PM performance level select
        pmSym_PM_PLCFG_PLSEL = pmComponent.createKeyValueSetSymbol("PM_PLCFG_PLSEL", None)
        pmSym_PM_PLCFG_PLSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:PLCFG")
        pmSym_PM_PLCFG_PLSEL.setLabel("Performance Level Select")
        pmSym_PM_PLCFG_PLSEL.setDescription("Selects Performance Level")
        pmSym_PM_PLCFG_PLSEL.addKey("PL0", "0x0", "Performance Level 0")
        pmSym_PM_PLCFG_PLSEL.addKey("PL2", "0x2", "Performance Level 2")
        pmSym_PM_PLCFG_PLSEL.setSelectedKey("PL2")
        pmSym_PM_PLCFG_PLSEL.setOutputMode("Key")
        pmSym_PM_PLCFG_PLSEL.setDisplayMode("Description")

        pmSym_PM_PLCFG_PLDIS = pmComponent.createBooleanSymbol("PLCFG_PLDIS", None)
        pmSym_PM_PLCFG_PLDIS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:PLCFG")
        pmSym_PM_PLCFG_PLDIS.setLabel("Force device to run in PL0")
        pmSym_PM_PLCFG_PLDIS.setDefaultValue(False)


    if "HAS_BBIASHS_FIELD" in parameters:
        #PM standby back biasing for SRAM
        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__BBIASHS\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        pmSym_STDBYCFG_BBIASHS = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_BBIASHS", None)
        pmSym_STDBYCFG_BBIASHS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_BBIASHS.setLabel("Back Bias option for SRAM")
        pmSym_STDBYCFG_BBIASHS.setDescription("Selects low power option for SRAM")

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_STDBYCFG_BBIASHS.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_STDBYCFG_BBIASHS.setDefaultValue(0)
        pmSym_STDBYCFG_BBIASHS.setOutputMode("Value")
        pmSym_STDBYCFG_BBIASHS.setDisplayMode("Description")
    else:
        #PM standby back biasing is a single bit for few devices
        pmSym_STDBYCFG_BBIASHS = pmComponent.createBooleanSymbol("PM_STDBYCFG_BBIASHS", None)
        pmSym_STDBYCFG_BBIASHS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_BBIASHS.setLabel("Put RAM in low power during standby mode")
        pmSym_STDBYCFG_BBIASHS.setDescription("RAM is backbiased in standby mode to reduce power")
        pm_STDBYCFG_initval = int(ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/register-group@[name=\"PM\"]/register@[name=\"STDBYCFG\"]").getAttribute("initval"), 16)
        pm_STDBYCFG_BBIASHS_mask = int(ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/register-group@[name=\"PM\"]/register@[name=\"STDBYCFG\"]/bitfield@[name=\"BBIASHS\"]").getAttribute("mask"), 16)
        pmSym_STDBYCFG_BBIASHS.setDefaultValue(((pm_STDBYCFG_initval & pm_STDBYCFG_BBIASHS_mask) != 0))

    if "HAS_BBIASTR_BIT" in parameters:
        #PM standby back biasing is a single bit for few devices
        pmSym_STDBYCFG_BBIASTR = pmComponent.createBooleanSymbol("PM_STDBYCFG_BBIASTR", None)
        pmSym_STDBYCFG_BBIASTR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_BBIASTR.setLabel("Put TrustRAM in low power during standby mode")
        pmSym_STDBYCFG_BBIASTR.setDescription("RAM is backbiased in standby mode to reduce power")

    if "HAS_BBIASLP_FIELD" in parameters:
        #PM standby back biasing for LP SRAM
        pmSym_STDBYCFG_BBIASLP = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_BBIASLP", None)
        pmSym_STDBYCFG_BBIASLP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_BBIASLP.setLabel("Back Bias option for LP SRAM")
        pmSym_STDBYCFG_BBIASLP.setDescription("Selects low power option for LP SRAM")

        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__BBIASLP\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_STDBYCFG_BBIASLP.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_STDBYCFG_BBIASLP.setDefaultValue(0)
        pmSym_STDBYCFG_BBIASLP.setOutputMode("Value")
        pmSym_STDBYCFG_BBIASLP.setDisplayMode("Description")

    if "HAS_LINKPD_FIELD" in parameters:
        #PM Linked Power Domain
        pmSym_STDBYCFG_LINKPD = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_LINKPD", None)
        pmSym_STDBYCFG_LINKPD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_LINKPD.setLabel("Power Domain Linking")
        pmSym_STDBYCFG_LINKPD.setDescription("Power domains can be linked to each other. When PDn (n=0,1) is active, the linked power domain(s) of higher index PDm (m>n) will be in active state even if there is no activity in PDm.")

        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__LINKPD\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_STDBYCFG_LINKPD.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_STDBYCFG_LINKPD.setDefaultValue(0)
        pmSym_STDBYCFG_LINKPD.setOutputMode("Value")
        pmSym_STDBYCFG_LINKPD.setDisplayMode("Description")

    if "HAS_PDCFG_FIELD" in parameters:
        #PM Power Domain Configuration
        pmSym_STDBYCFG_PDCFG = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_PDCFG", None)
        pmSym_STDBYCFG_PDCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_PDCFG.setLabel("Power Domain Keep Active")
        pmSym_STDBYCFG_PDCFG.setDescription("Power domains can be forced to remain in active state during standby sleep mode, this will accelerate wake-up time")

        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__PDCFG\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_STDBYCFG_PDCFG.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_STDBYCFG_PDCFG.setDefaultValue(0)
        pmSym_STDBYCFG_PDCFG.setOutputMode("Value")
        pmSym_STDBYCFG_PDCFG.setDisplayMode("Description")

    if "HAS_PDCFG_BIT" in parameters:
        #PM Power Domain Configuration
        pmSym_STDBYCFG_PDCFG = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_PDCFG", None)
        pmSym_STDBYCFG_PDCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_PDCFG.setLabel("Power Domain Configuration")
        pmSym_STDBYCFG_PDCFG.setDescription("Power domains can be forced to remain in active state during standby sleep mode, this will accelerate wake-up time")

        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__PDCFG\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_STDBYCFG_PDCFG.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_STDBYCFG_PDCFG.setDefaultValue(0)
        pmSym_STDBYCFG_PDCFG.setOutputMode("Value")
        pmSym_STDBYCFG_PDCFG.setDisplayMode("Description")

    if "HAS_DPGPD0_BIT" in parameters:
        pmSym_STDBYCFG_DPGPD0 = pmComponent.createBooleanSymbol("PM_STDBYCFG_DPGPD0", None)
        pmSym_STDBYCFG_DPGPD0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_DPGPD0.setLabel("PD0 Dynamic Power Gating Enable")
        pmSym_STDBYCFG_DPGPD0.setDefaultValue(0)
        pmSym_STDBYCFG_DPGPD0.setDescription("PD0 and PD1 supports dynamic power gating")

    if "HAS_DPGPD1_BIT" in parameters:
        pmSym_STDBYCFG_DPGPD1 = pmComponent.createBooleanSymbol("PM_STDBYCFG_DPGPD1", None)
        pmSym_STDBYCFG_DPGPD1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_DPGPD1.setLabel("PD1 Dynamic Power Gating Enable")
        pmSym_STDBYCFG_DPGPD1.setDefaultValue(0)
        pmSym_STDBYCFG_DPGPD1.setDescription("PD0 and PD1 supports dynamic power gating")

    if "HAS_DPGPDSW_BIT" in parameters:
        pmSym_STDBYCFG_DPGPD = pmComponent.createBooleanSymbol("PM_STDBYCFG_DPGPD", None)
        pmSym_STDBYCFG_DPGPD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
        pmSym_STDBYCFG_DPGPD.setLabel("Dynamic Power Gating Enable")
        pmSym_STDBYCFG_DPGPD.setDefaultValue(0)
        pmSym_STDBYCFG_DPGPD.setDescription("Dynamic Power Gating for Switchable Power Domain")

    #PM standby VREGMOD configuration
    pmSym_STDBYCFG_VREGSMOD = pmComponent.createKeyValueSetSymbol("PM_STDBYCFG_VREGSMOD", None)
    pmSym_STDBYCFG_VREGSMOD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:STDBYCFG")
    pmSym_STDBYCFG_VREGSMOD.setLabel("Voltage Regulator operation in Standby mode")
    pmSym_STDBYCFG_VREGSMOD.setDescription("Configures the VDDCORE Supply source in Standby Sleep mode.")

    pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_STDBYCFG__VREGSMOD\"]")
    pmStandbyConfigurationValues = []
    pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

    for index in range(len(pmStandbyConfigurationValues)):
        pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
        pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
        pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
        pmSym_STDBYCFG_VREGSMOD.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

    pmSym_STDBYCFG_VREGSMOD.setDefaultValue(0)
    pmSym_STDBYCFG_VREGSMOD.setOutputMode("Value")
    pmSym_STDBYCFG_VREGSMOD.setDisplayMode("Description")

    if "HAS_PWCFG" in parameters:
        pmSym_PWCFG = pmComponent.createKeyValueSetSymbol("PM_PWCFG_RAMPSWC", None)
        pmSym_PWCFG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:PWCFG")
        pmSym_PWCFG.setLabel("RAM Power Switch Configuration")

        pmStandbyConfigurationNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_PWCFG__RAMPSWC\"]")
        pmStandbyConfigurationValues = []
        pmStandbyConfigurationValues = pmStandbyConfigurationNode.getChildren()

        for index in range(len(pmStandbyConfigurationValues)):
            pmStandbyConfigurationKeyName = pmStandbyConfigurationValues[index].getAttribute("name")
            pmStandbyConfigurationKeyDescription = pmStandbyConfigurationValues[index].getAttribute("caption")
            pmStandbyConfigurationKeyValue = pmStandbyConfigurationValues[index].getAttribute("value")
            pmSym_PWCFG.addKey(pmStandbyConfigurationKeyName, pmStandbyConfigurationKeyValue, pmStandbyConfigurationKeyDescription)

        pmSym_PWCFG.setDefaultValue(0)
        pmSym_PWCFG.setOutputMode("Value")
        pmSym_PWCFG.setDisplayMode("Description")

    #Get different modes for Idle Sleep
    pmIdleSleepOptions = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_SLEEPCFG__SLEEPMODE\"]")

    pmIdleSleepOptionValues = []
    pmIdleSleepOptionValues = pmIdleSleepOptions.getChildren()

    IdleModeCount = 0
    for id in range(0,len(pmIdleSleepOptionValues)):
        if "IDLE" in pmIdleSleepOptionValues[id].getAttribute("name"):
            IdleModeCount += 1

    if IdleModeCount > 1:
        #Idle configuration
        pmSym_PM_IDLE = pmComponent.createKeyValueSetSymbol("PM_IDLE_OPTION", None)
        pmSym_PM_IDLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pm_u2240;register:SLEEPCFG")
        pmSym_PM_IDLE.setLabel("Idle Mode Configuration")
        pmSym_PM_IDLE.setOutputMode("Value")
        pmSym_PM_IDLE.setDisplayMode("Description")

        for id in range(0,len(pmIdleSleepOptionValues)):
            pmSym_PM_IDLE_Key_Key = pmIdleSleepOptionValues[id].getAttribute("name")
            if "IDLE" in pmSym_PM_IDLE_Key_Key:
                pmSym_PM_IDLE_Key_Value = pmIdleSleepOptionValues[id].getAttribute("value")
                pmSym_PM_IDLE_Key_Description = pmIdleSleepOptionValues[id].getAttribute("caption")
                pmSym_PM_IDLE.addKey(pmSym_PM_IDLE_Key_Key, pmSym_PM_IDLE_Key_Value, pmSym_PM_IDLE_Key_Description)
        pmSym_PM_IDLE.setDefaultValue(0)

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
    pmSym_HeaderFile.setSourcePath("../peripheral/pm_u2240/templates/plib_pm.h.ftl")
    pmSym_HeaderFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".h")
    pmSym_HeaderFile.setDestPath("/peripheral/pm/")
    pmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_HeaderFile.setType("HEADER")
    pmSym_HeaderFile.setMarkup(True)

    pmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE", None)
    pmSym_SourceFile.setSourcePath("../peripheral/pm_u2240/templates/plib_pm.c.ftl")
    pmSym_SourceFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".c")
    pmSym_SourceFile.setDestPath("/peripheral/pm/")
    pmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pm/")
    pmSym_SourceFile.setType("SOURCE")
    pmSym_SourceFile.setMarkup(True)

    pmSym_SystemInitFile = pmComponent.createFileSymbol("PM_SYS_INIT", None)
    pmSym_SystemInitFile.setType("STRING")
    if any(device in Database.getSymbolValue("core", "CoreSeries") for device in ["PIC32CMLE", "PIC32CMLS"]):
        pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START1")
    else:
        pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    pmSym_SystemInitFile.setSourcePath("../peripheral/pm_u2240/templates/system/initialization.c.ftl")
    pmSym_SystemInitFile.setMarkup(True)

    pmSymSystemDefFile = pmComponent.createFileSymbol("PM_SYS_DEF", None)
    pmSymSystemDefFile.setType("STRING")
    pmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pmSymSystemDefFile.setSourcePath("../peripheral/pm_u2240/templates/system/definitions.h.ftl")
    pmSymSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global PMfilesArray
        pmIsNonSecure = bool(Database.getSymbolValue("core", pmComponent.getID().upper() + "_IS_NON_SECURE"))
        pmSymSystemDefFile.setDependencies(fileUpdate, ["core." + pmComponent.getID().upper() + "_IS_NON_SECURE"])

        secpmSym_HeaderFile = pmComponent.createFileSymbol("PM_HEADER_SECURE", None)
        secpmSym_HeaderFile.setSourcePath("../peripheral/pm_u2240/templates/trustZone/plib_pm_secure.h.ftl")
        secpmSym_HeaderFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".h")
        secpmSym_HeaderFile.setDestPath("/peripheral/pm/")
        secpmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pm/")
        secpmSym_HeaderFile.setType("HEADER")
        secpmSym_HeaderFile.setMarkup(True)
        secpmSym_HeaderFile.setSecurity("SECURE")
        secpmSym_HeaderFile.setEnabled(pmIsNonSecure)

        secpmSym_SourceFile = pmComponent.createFileSymbol("PM_SOURCE_SECURE", None)
        secpmSym_SourceFile.setSourcePath("../peripheral/pm_u2240/templates/trustZone/plib_pm_secure.c.ftl")
        secpmSym_SourceFile.setOutputName("plib_" + pmInstanceName.getValue().lower() + ".c")
        secpmSym_SourceFile.setDestPath("/peripheral/pm/")
        secpmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pm/")
        secpmSym_SourceFile.setType("SOURCE")
        secpmSym_SourceFile.setMarkup(True)
        secpmSym_SourceFile.setSecurity("SECURE")
        secpmSym_SourceFile.setEnabled(pmIsNonSecure)

        secpmSymSystemDefFile = pmComponent.createFileSymbol("PM_SYS_DEF_SECURE", None)
        secpmSymSystemDefFile.setType("STRING")
        secpmSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        secpmSymSystemDefFile.setSourcePath("../peripheral/pm_u2240/templates/system/definitions.h.ftl")
        secpmSymSystemDefFile.setMarkup(True)
        secpmSymSystemDefFile.setEnabled(pmIsNonSecure)

        if any(device in Database.getSymbolValue("core", "CoreSeries") for device in ["PIC32CMLE", "PIC32CMLS"]):
            pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START1")
        else:
            pmSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")

        PMfilesArray.append(pmSym_HeaderFile)
        PMfilesArray.append(pmSym_SourceFile)
        PMfilesArray.append(pmSym_SystemInitFile)
        PMfilesArray.append(pmSymSystemDefFile)
        PMfilesArray.append(secpmSym_HeaderFile)
        PMfilesArray.append(secpmSym_SourceFile)
        PMfilesArray.append(secpmSymSystemDefFile)
        if pmIsNonSecure == False:
            PMfilesArray[0].setSecurity("SECURE")
            PMfilesArray[1].setSecurity("SECURE")
            PMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
