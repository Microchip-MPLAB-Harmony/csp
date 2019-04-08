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

global pacInterruptVector
global pacInterruptHandler
global pacInterruptHandlerLock
global pacInstanceName
global pacSym_Use
global pacSym_INTENSET

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updatePACInterruptStatus(symbol, event):

    Database.setSymbolValue("core", pacInterruptVector, event["value"], 2)
    Database.setSymbolValue("core", pacInterruptHandlerLock, event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", pacInterruptHandler, pacInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", pacInterruptHandler, pacInstanceName.getValue() + "_Handler", 2)

def updatePACInterruptWarringStatus(symbol, event):

    if pacSym_INTENSET.getValue() == True and pacSym_Use.getValue() == True:
        symbol.setVisible(event["value"])

def updatePACInterruptVisibleProperty(symbol, event):

    symbol.setVisible(event["value"])

    if pacSym_INTENSET.getValue() == True:
        Database.setSymbolValue("core", pacInterruptVector, event["value"], 2)
        Database.setSymbolValue("core", pacInterruptHandlerLock, event["value"], 2)

        if event["value"] == True:
            Database.setSymbolValue("core", pacInterruptHandler, pacInstanceName.getValue() + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", pacInterruptHandler, pacInstanceName.getValue() + "_Handler", 2)

def updatePACErrorEventVisibleProperty(symbol, event):

    component = symbol.getComponent()

    component.getSymbolByID("PAC_HEADER").setEnabled(event["value"])
    component.getSymbolByID("PAC_SOURCE").setEnabled(event["value"])
    component.getSymbolByID("PAC_SYS_DEF").setEnabled(event["value"])
    component.getSymbolByID("PAC_SYS_INIT").setEnabled(event["value"])

    symbol.setVisible(event["value"])

    if event["value"] == False:
        component.getSymbolByID("PAC_INTERRUPT_ENABLE_COMMENT").setVisible(False)

def evsysSetup(symbol, event):

    pacActive = Database.getSymbolValue(event["namespace"], "PAC_USE")
    eventActive = Database.getSymbolValue(event["namespace"], "PAC_ERROR_EVENT")
    prevStatus = Database.getSymbolValue("evsys", "GENERATOR_PAC_ACCERR_ACTIVE")

    if (prevStatus != (pacActive & eventActive)):
        Database.setSymbolValue("evsys", "GENERATOR_PAC_ACCERR_ACTIVE", (pacActive & eventActive), 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

#PAC menu
pacSym_Menu = coreComponent.createMenuSymbol("PAC_MENU", None)
pacSym_Menu.setLabel("PAC")

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PAC\"]").getChildren()

pacInstanceName = coreComponent.createStringSymbol("PAC_INSTANCE_NAME", pacSym_Menu)
pacInstanceName.setVisible(False)
pacInstanceName.setDefaultValue(instances[0].getAttribute("name"))

#PAC Use
pacSym_Use = coreComponent.createBooleanSymbol("PAC_USE", pacSym_Menu)
pacSym_Use.setLabel("Use PAC ?")

#interrupt mode
pacSym_INTENSET = coreComponent.createBooleanSymbol("PAC_INTERRRUPT_MODE", pacSym_Use)
pacSym_INTENSET.setLabel("Enable PAC Interrupt ?")
pacSym_INTENSET.setVisible(False)
pacSym_INTENSET.setDefaultValue(True)
pacSym_INTENSET.setDependencies(updatePACInterruptVisibleProperty, ["PAC_USE"])

#Error Event
pacSym_ErrEventSET = coreComponent.createBooleanSymbol("PAC_ERROR_EVENT", pacSym_Use)
pacSym_ErrEventSET.setLabel("Generate Peripheral Access Error Event Output")
pacSym_ErrEventSET.setVisible(False)
pacSym_ErrEventSET.setDependencies(updatePACErrorEventVisibleProperty, ["PAC_USE"])

#Error Event
pacSym_ErrEventSET = coreComponent.createBooleanSymbol("PAC_EVSYS_TRIGGER_DUMMY", pacSym_Use)
pacSym_ErrEventSET.setVisible(False)
pacSym_ErrEventSET.setDependencies(evsysSetup, ["PAC_ERROR_EVENT", "PAC_USE"])

pacIndex = 0

modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()
for module in range (0, len(modules)):
    instances = modules[module].getChildren()
    for instance in range (0, len(instances)):
        options = instances[instance].getChildren()
        for option in range (0, len(options)):
            parameters = options[option].getChildren()
            for parameter in range(0, len(parameters)):
                name = str(parameters[parameter].getAttribute("name"))
                if "INSTANCE_ID" in name:
                    periName = str(instances[instance].getAttribute("name"))

                    pacSym_PeripheralName = coreComponent.createStringSymbol("PAC_" + str(pacIndex) + "_PERI_NAME", pacSym_Use)
                    pacSym_PeripheralName.setDefaultValue(periName)
                    pacSym_PeripheralName.setVisible(False)

                    pacIndex += 1

pacSym_PeriCount = coreComponent.createIntegerSymbol("PAC_PERI_COUNT", pacSym_Use)
pacSym_PeriCount.setDefaultValue(pacIndex)
pacSym_PeriCount.setVisible(False)

############################################################################
#### Dependency ####
############################################################################

pacInterruptVector = pacInstanceName.getValue() + "_INTERRUPT_ENABLE"
pacInterruptHandler = pacInstanceName.getValue() + "_INTERRUPT_HANDLER"
pacInterruptHandlerLock = pacInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
pacInterruptVectorUpdate = pacInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

# Interrupt Dynamic settings
pacSym_UpdateInterruptStatus = coreComponent.createBooleanSymbol("PAC_INTERRUPT_STATUS", pacSym_Use)
pacSym_UpdateInterruptStatus.setDependencies(updatePACInterruptStatus, ["PAC_INTERRRUPT_MODE"])
pacSym_UpdateInterruptStatus.setVisible(False)

# Interrupt Warning status
pacSym_IntEnComment = coreComponent.createCommentSymbol("PAC_INTERRUPT_ENABLE_COMMENT", pacSym_Use)
pacSym_IntEnComment.setVisible(False)
pacSym_IntEnComment.setLabel("Warning!!! PAC Interrupt is Disabled in Interrupt Manager")
pacSym_IntEnComment.setDependencies(updatePACInterruptWarringStatus, ["core." + pacInterruptVectorUpdate])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pacSym_HeaderFile = coreComponent.createFileSymbol("PAC_HEADER", None)
pacSym_HeaderFile.setSourcePath("../peripheral/pac_u2120/templates/plib_pac.h.ftl")
pacSym_HeaderFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".h")
pacSym_HeaderFile.setDestPath("/peripheral/pac/")
pacSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_HeaderFile.setType("HEADER")
pacSym_HeaderFile.setMarkup(True)
pacSym_HeaderFile.setEnabled(False)

pacSym_SourceFile = coreComponent.createFileSymbol("PAC_SOURCE", None)
pacSym_SourceFile.setSourcePath("../peripheral/pac_u2120/templates/plib_pac.c.ftl")
pacSym_SourceFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".c")
pacSym_SourceFile.setDestPath("/peripheral/pac/")
pacSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_SourceFile.setType("SOURCE")
pacSym_SourceFile.setMarkup(True)
pacSym_SourceFile.setEnabled(False)

pacSystemDefFile = coreComponent.createFileSymbol("PAC_SYS_DEF", None)
pacSystemDefFile.setType("STRING")
pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pacSystemDefFile.setSourcePath("../peripheral/pac_u2120/templates/system/definitions.h.ftl")
pacSystemDefFile.setMarkup(True)
pacSystemDefFile.setEnabled(False)

pacSystemInitFile = coreComponent.createFileSymbol("PAC_SYS_INIT", None)
pacSystemInitFile.setType("STRING")
pacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
pacSystemInitFile.setSourcePath("../peripheral/pac_u2120/templates/system/initialization.c.ftl")
pacSystemInitFile.setMarkup(True)
pacSystemInitFile.setEnabled(False)
