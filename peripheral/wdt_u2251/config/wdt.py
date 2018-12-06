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

global wdtInstanceName
global wdtInterruptVector
global wdtInterruptHandler
global wdtInterruptHandlerLock
global wdtSym_Use
global wdtSym_CTRLA_EW

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateWDTInterruptStatus(symbol, event):

    Database.setSymbolValue("core", wdtInterruptVector, event["value"], 2)
    Database.setSymbolValue("core", wdtInterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", wdtInterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_Handler", 2)

def updateWDTInterruptWarningStatus(symbol, event):

    if wdtSym_CTRLA_EW.getValue() == True and wdtSym_Use.getValue() == True:
        symbol.setVisible(event["value"])

def updateWDTConfigCommentVisibleProperty(symbol, event):

    symbol.setVisible(event["value"])

def updateWDTEnarlyInterruptVisibleProperty(symbol, event):

    component = symbol.getComponent()
    component.getSymbolByID("WDT_HEADER").setEnabled(event["value"])
    component.getSymbolByID("WDT_SOURCE").setEnabled(event["value"])
    component.getSymbolByID("WDT_SYS_DEF").setEnabled(event["value"])

    symbol.setVisible(event["value"])

    if wdtSym_CTRLA_EW.getValue() == True:
        Database.setSymbolValue("core", wdtInterruptVector, event["value"], 2)
        Database.setSymbolValue("core", wdtInterruptHandlerLock, event["value"], 2)

        if event["value"] == True:
            Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_Handler", 2)

###################################################################################################
#############################################  WDT  ###############################################
###################################################################################################

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]").getChildren()

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
wdtInstanceName.setDefaultValue(instances[0].getAttribute("name"))

#WDT menu
wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

#WDT Use
wdtSym_Use = coreComponent.createBooleanSymbol("WDT_USE", wdtMenu)
wdtSym_Use.setLabel("Use WDT ?")

#Enable Early Interrupt
wdtSym_CTRLA_EW = coreComponent.createBooleanSymbol("WDT_EW_ENABLE", wdtSym_Use)
wdtSym_CTRLA_EW.setLabel("Enable Watchdog Early Interrupt")
wdtSym_CTRLA_EW.setVisible(False)
wdtSym_CTRLA_EW.setDependencies(updateWDTEnarlyInterruptVisibleProperty, ["WDT_USE"])

#WDT Configuration comment
wdtSym_ConfigComment = coreComponent.createCommentSymbol("WDT_CONFIG_COMMENT", wdtSym_Use)
wdtSym_ConfigComment.setLabel("************** Configure WDT via Fuse ***************")
wdtSym_ConfigComment.setVisible(False)
wdtSym_ConfigComment.setDependencies(updateWDTConfigCommentVisibleProperty, ["WDT_USE"])

############################################################################
#### Dependency ####
############################################################################

wdtInterruptVector = wdtInstanceName.getValue() + "_INTERRUPT_ENABLE"
wdtInterruptHandler = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER"
wdtInterruptHandlerLock = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
wdtInterruptVectorUpdate = wdtInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

# Interrupt Dynamic settings
wdtSym_UpdateInterruptStatus = coreComponent.createBooleanSymbol("WDT_INTERRUPT_STATUS", wdtSym_Use)
wdtSym_UpdateInterruptStatus.setDependencies(updateWDTInterruptStatus, ["WDT_EW_ENABLE"])
wdtSym_UpdateInterruptStatus.setVisible(False)

# Interrupt Warning status
wdtSym_IntEnComment = coreComponent.createCommentSymbol("WDT_INTERRUPT_ENABLE_COMMENT", wdtSym_Use)
wdtSym_IntEnComment.setVisible(False)
wdtSym_IntEnComment.setLabel("Warning!!! WDT Interrupt is Disabled in Interrupt Manager")
wdtSym_IntEnComment.setDependencies(updateWDTInterruptWarningStatus, ["core." + wdtInterruptVectorUpdate])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"WDT\"]")
wdtModuleID = wdtModuleNode.getAttribute("id")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_u2251/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("/peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(False)

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_u2251/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("/peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(False)

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_u2251/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(False)
