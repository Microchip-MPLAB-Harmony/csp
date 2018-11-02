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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global eicInstanceName

###################################################################################################
######################################### Callbacks ###############################################
###################################################################################################
global DEBOUNCEN_Code

def confMenu(symbol, event):

    if event["id"] == "NMI_CTRL":

        Database.clearSymbolValue("core", NMIInterruptHandler)

        if event["value"] == True:
            Database.setSymbolValue("core", NMIInterruptHandler, "NMI_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", NMIInterruptHandler, "NonMaskableInt_Handler", 2)

    symbol.setVisible(event["value"])

def codeGenerationForEVCCTRL_EXTINTEO(symbol, event):
    global extIntCount
    channel = int(event["id"].split("_")[2])
    if Database.getSymbolValue(event["namespace"], "EIC_CHAN_" + str(channel)):
        if not str(event["id"]).startswith("EIC_CHAN_"):
            if(event["value"] == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
                Database.setSymbolValue("evsys","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", True, 2)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
                Database.setSymbolValue("evsys","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", False, 2)
        else:
            parameter = symbol.getID().split("EIC_")[1]
            if(Database.getSymbolValue(event["namespace"], "EIC_" + str(parameter) + "_" + str(channel)) == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
                Database.setSymbolValue("evsys","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", True, 2)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
                Database.setSymbolValue("evsys","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", False, 2)

    else:
        symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
        Database.setSymbolValue("evsys","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", False, 2)
    

def updateEICInterruptStatus(symbol, event):

    Database.setSymbolValue("core", InterruptVector, bool(event["value"]), 2)
    Database.setSymbolValue("core", InterruptHandlerLock, bool(event["value"]), 2)
    if bool(event["value"]) == True:
        Database.setSymbolValue("core", InterruptHandler, eicInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "EIC_Handler", 2)

def updateEICInterruptWarringStatus(symbol, event):

    if EXTINT_Code.getValue() != 0x0:
        symbol.setVisible(event["value"])

def updateEICClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def filterMenu(symbol, event):
    symbol.setVisible((event["value"] > 0))

###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(eicComponent):
    eicSym_eventsList = []
    eicSym_wakeupList = []
    eicSym_InterruptList = []
    eicSym_Channel = []
    global DEBOUNCEN_Code
    global EXTINT_Code
    global eicInstanceName
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global NMIInterruptHandler

    global extIntCount
    eicInstanceName = eicComponent.createStringSymbol("EIC_INSTANCE_NAME", None)
    eicInstanceName.setVisible(False)
    eicInstanceName.setDefaultValue(eicComponent.getID().upper())

    #clock enable
    Database.clearSymbolValue("core", eicInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", eicInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    extIntNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EIC\"]/instance@[name=\""+eicInstanceName.getValue()+"\"]/parameters/param@[name=\"EXTINT_NUM\"]")
    extIntCount = int(extIntNode.getAttribute("value"))
    eicSym_IntCount = eicComponent.createIntegerSymbol("EIC_INT_COUNT" , None)
    eicSym_IntCount.setDefaultValue(extIntCount)
    eicSym_IntCount.setVisible(False)

    #Non-Maskable Interrupt Control
    eicPLX4 = eicComponent.createBooleanSymbol("NMI_CTRL", None)
    eicPLX4.setLabel("Non Maskable Interrupt Control")

    nmiConfMenu = eicComponent.createMenuSymbol("NMI_MENU", eicPLX4)
    nmiConfMenu.setLabel("NMI Configuration")
    nmiConfMenu.setDependencies(confMenu, ["NMI_CTRL"])
    nmiConfMenu.setVisible(False)

    #NMIFILTEN
    NMI_FILTEN_Selection = eicComponent.createBooleanSymbol("NMI_FILTEN" , nmiConfMenu)
    NMI_FILTEN_Selection.setLabel("Enable filter")

    # NMI - SENSE
    NMI_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("NMI_SENSE" , nmiConfMenu)
    NMI_SENSE_SelectionSymbol.setLabel("NMI Interrupt Edge Selection")

    eicNMISenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_NMICTRL__NMISENSE\"]")

    for index in range(len(eicNMISenseNode.getChildren())):
        eicNMISenseKeyName = eicNMISenseNode.getChildren()[index].getAttribute("name")
        eicNMISenseKeyDescription = eicNMISenseNode.getChildren()[index].getAttribute("caption")
        eicNMISenseKeyValue = eicNMISenseNode.getChildren()[index].getAttribute("value")
        NMI_SENSE_SelectionSymbol.addKey(eicNMISenseKeyName, eicNMISenseKeyValue , eicNMISenseKeyDescription)

    NMI_SENSE_SelectionSymbol.setDefaultValue(0)
    NMI_SENSE_SelectionSymbol.setOutputMode("Key")
    NMI_SENSE_SelectionSymbol.setDisplayMode("Description")

    #Interrupt 0 - EXTINT Settings
    for extIntIndex in range(0 , extIntCount):

        eicPLX1 = eicComponent.createBooleanSymbol("EIC_CHAN_" + str(extIntIndex) , None)
        eicPLX1.setLabel("Enable EIC Channel" + str(extIntIndex))

        eicConfiguration = eicComponent.createMenuSymbol("EIC_MENU" + str(extIntIndex), eicPLX1)
        eicConfiguration.setLabel("EIC Channel" + str(extIntIndex) + " Configuration")
        eicConfiguration.setDependencies(confMenu, ["EIC_CHAN_" + str(extIntIndex)])
        eicConfiguration.setVisible(False)

        # populate a list with IDs for code generation dependency
        eicSym_Channel.append("EIC_CHAN_" + str(extIntIndex))

        eicINT = eicComponent.createBooleanSymbol("EIC_INT_" + str(extIntIndex) , eicConfiguration)
        eicINT.setLabel("Enable Interrupt")
        eicSym_InterruptList.append("EIC_INT_" + str(extIntIndex))

        #EVCTRL - External Interrupt Event Output Enable 0..7 Channel number
        EVCCTRL_EXTINTEO_Selection = eicComponent.createBooleanSymbol("EIC_EXTINTEO_" + str(extIntIndex) , eicConfiguration)
        EVCCTRL_EXTINTEO_Selection.setLabel("Enable Event Output")

        # populate a list with IDs for code generation dependency
        eicSym_eventsList.append("EIC_EXTINTEO_" + str(extIntIndex))

        eicWakeup = eicComponent.createBooleanSymbol("EIC_WAKEUP_" + str(extIntIndex) , eicConfiguration )
        eicWakeup.setLabel("Enable Wakeup on Channel" + str(extIntIndex))

        # populate a list with IDs for code generation dependency
        eicSym_wakeupList.append("EIC_WAKEUP_" + str(extIntIndex))

        #CONFIG - Sense Enable
        CONFIG_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_CONFIG_SENSE_" + str(extIntIndex) , eicConfiguration)
        CONFIG_SENSE_SelectionSymbol.setLabel("External Interrupt" + str(extIntIndex) + " Edge Selection")

        eicConfigSenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_CONFIG__SENSE0\"]")

        for index in range(len(eicConfigSenseNode.getChildren())):
            eicConfigSenseKeyName = eicConfigSenseNode.getChildren()[index].getAttribute("name")
            eicConfigSenseKeyDescription = eicConfigSenseNode.getChildren()[index].getAttribute("caption")
            eicConfigSenseKeyValue = eicConfigSenseNode.getChildren()[index].getAttribute("value")
            CONFIG_SENSE_SelectionSymbol.addKey(eicConfigSenseKeyName, eicConfigSenseKeyValue , eicConfigSenseKeyDescription)

        CONFIG_SENSE_SelectionSymbol.setDefaultValue(0)
        CONFIG_SENSE_SelectionSymbol.setOutputMode("Key")
        CONFIG_SENSE_SelectionSymbol.setDisplayMode("Description")

        #CONFIG - Filter Enable
        CONFIG_FILTER_Selection = eicComponent.createBooleanSymbol("EIC_CONFIG_FILTEN_" + str(extIntIndex) , eicConfiguration)
        CONFIG_FILTER_Selection.setLabel("Enable filter")
        CONFIG_FILTER_Selection.setVisible(False)
        CONFIG_FILTER_Selection.setDependencies(filterMenu, ["EIC_CONFIG_SENSE_" + str(extIntIndex)])


################################################################################
################### Business Logic calls for generating code ###################
################################################################################

    eicSym_eventsList.extend(eicSym_Channel)
    eicSym_wakeupList.extend(eicSym_Channel)
    eicSym_InterruptList.extend(eicSym_Channel)

    eicCalculation = eicComponent.createMenuSymbol("REG_MENU", None)
    eicCalculation.setVisible(False)
    eicCalculation.setLabel("Calculated register values")

    WAKEUP_Code = eicComponent.createHexSymbol("EIC_WAKEUP" , eicCalculation)
    WAKEUP_Code.setDefaultValue(0)
    WAKEUP_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_wakeupList)
    
    EVCCTRL_EXTINTEO_Code = eicComponent.createHexSymbol("EIC_EXTINTEO" , eicCalculation)
    EVCCTRL_EXTINTEO_Code.setDefaultValue(0)
    EVCCTRL_EXTINTEO_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_eventsList)

    EXTINT_Code = eicComponent.createHexSymbol("EIC_INT" , eicCalculation)
    EXTINT_Code.setDefaultValue(0)
    EXTINT_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_InterruptList)


    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = eicInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = eicInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = eicInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = eicInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    NMIInterruptHandler = "NonMaskableInt_INTERRUPT_HANDLER"

    # Interrupt Dynamic settings
    eicSym_UpdateInterruptStatus = eicComponent.createBooleanSymbol("EIC_INTERRUPT_STATUS", None)
    eicSym_UpdateInterruptStatus.setDependencies(updateEICInterruptStatus, ["EIC_INT"])
    eicSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    eicSym_IntEnComment = eicComponent.createCommentSymbol("EIC_INTERRUPT_ENABLE_COMMENT", None)
    eicSym_IntEnComment.setVisible(False)
    eicSym_IntEnComment.setLabel("Warning!!! EIC Interrupt is Disabled in Interrupt Manager")
    eicSym_IntEnComment.setDependencies(updateEICInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    eicSym_ClkEnComment = eicComponent.createCommentSymbol("EIC_CLOCK_ENABLE_COMMENT", None)
    eicSym_ClkEnComment.setLabel("Warning!!! EIC Peripheral Clock is Disabled in Clock Manager")
    eicSym_ClkEnComment.setVisible(False)
    eicSym_ClkEnComment.setDependencies(updateEICClockWarringStatus, ["core."+eicInstanceName.getValue()+"_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eicHeader1File = eicComponent.createFileSymbol("EIC_HEADER", None)
    eicHeader1File.setSourcePath("../peripheral/eic_u2217/templates/plib_eic.h.ftl")
    eicHeader1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".h")
    eicHeader1File.setDestPath("/peripheral/eic/")
    eicHeader1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicHeader1File.setType("HEADER")
    eicHeader1File.setMarkup(True)

    eicSource1File = eicComponent.createFileSymbol("EIC_SOURCE", None)
    eicSource1File.setSourcePath("../peripheral/eic_u2217/templates/plib_eic.c.ftl")
    eicSource1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".c")
    eicSource1File.setDestPath("/peripheral/eic/")
    eicSource1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicSource1File.setType("SOURCE")
    eicSource1File.setMarkup(True)

    eicSystemInitFile = eicComponent.createFileSymbol("EIC_SYS_INT", None)
    eicSystemInitFile.setType("STRING")
    eicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eicSystemInitFile.setSourcePath("../peripheral/eic_u2217/templates/system/initialization.c.ftl")
    eicSystemInitFile.setMarkup(True)

    eicSystemDefFile = eicComponent.createFileSymbol("EIC_SYS_DEF", None)
    eicSystemDefFile.setType("STRING")
    eicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eicSystemDefFile.setSourcePath("../peripheral/eic_u2217/templates/system/definitions.h.ftl")
    eicSystemDefFile.setMarkup(True)
