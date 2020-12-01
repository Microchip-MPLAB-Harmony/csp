# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

################################################################################
#### Business Logic ####
################################################################################

def updateSymbolEnable(symbol, event):
    symbol.setEnabled(event["value"])

################################################################################
#### Data Watchpoint and Trace (DWT) ####
################################################################################
Log.writeInfoMessage("Loading Data Watchpoint and Trace (DWT) for " + Variables.get("__PROCESSOR"))

dwtEnable = coreComponent.createBooleanSymbol("DWT_ENABLE", cortexMenu)
dwtEnable.setLabel("Enable DWT Cycle Counter")
dwtEnable.setDefaultValue(False)

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

dwtHeaderFile = coreComponent.createFileSymbol("DWT_HEADER", None)
dwtHeaderFile.setSourcePath("../peripheral/dwt/templates/plib_dwt.h.ftl")
dwtHeaderFile.setOutputName("plib_dwt.h")
dwtHeaderFile.setDestPath("/peripheral/dwt/")
dwtHeaderFile.setProjectPath("config/" + configName + "/peripheral/dwt/")
dwtHeaderFile.setType("HEADER")
dwtHeaderFile.setOverwrite(True)
dwtHeaderFile.setEnabled(False)
dwtHeaderFile.setMarkup(True)
dwtHeaderFile.setDependencies(updateSymbolEnable, ["DWT_ENABLE"])

dwtSourceFile = coreComponent.createFileSymbol("DWT_SOURCE", None)
dwtSourceFile.setSourcePath("../peripheral/dwt/templates/plib_dwt.c.ftl")
dwtSourceFile.setOutputName("plib_dwt.c")
dwtSourceFile.setDestPath("/peripheral/dwt/")
dwtSourceFile.setProjectPath("config/" + configName + "/peripheral/dwt/")
dwtSourceFile.setType("SOURCE")
dwtSourceFile.setOverwrite(True)
dwtSourceFile.setMarkup(True)
dwtSourceFile.setEnabled(False)
dwtSourceFile.setDependencies(updateSymbolEnable, ["DWT_ENABLE"])

dwtSystemDefFile = coreComponent.createFileSymbol("DWT_DEFINITIONS", None)
dwtSystemDefFile.setType("STRING")
dwtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dwtSystemDefFile.setSourcePath("../peripheral/dwt/templates/system/definitions.h.ftl")
dwtSystemDefFile.setMarkup(True)
dwtSystemDefFile.setEnabled(False)
dwtSystemDefFile.setDependencies(updateSymbolEnable, ["DWT_ENABLE"])

dwtSystemInitFile = coreComponent.createFileSymbol("DWT_INITIALIZATION", None)
dwtSystemInitFile.setType("STRING")
dwtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dwtSystemInitFile.setSourcePath("../peripheral/dwt/templates/system/initialization.c.ftl")
dwtSystemInitFile.setMarkup(True)
dwtSystemInitFile.setEnabled(False)
dwtSystemInitFile.setDependencies(updateSymbolEnable, ["DWT_ENABLE"])
