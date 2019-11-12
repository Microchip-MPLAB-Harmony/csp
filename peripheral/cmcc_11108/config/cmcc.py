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
global  cmccHeaderFile
global  cmccSourceFile
global  cmccSystemDefFile

def enableFileGen(symbol, event):
    component = event["source"]
    cmccHeaderFile = component.getSymbolByID("CMCC_HEADER_FILE")
    cmccSourceFile = component.getSymbolByID("CMCC_SOURCE_FILE")
    enableFileGen  = event["value"]
    cmccHeaderFile.setEnabled(enableFileGen)
    cmccSourceFile.setEnabled(enableFileGen)

# CMCC 11008 is also implemented on masks which has multiple cores. In such 
# cases, we only generate cache controller code for the core for which this
# project is created (i.e. the core that is relevant for the current project)
cmccID = Database.getSymbolValue("core", "CMCC_ID")

# Multicore mask, append the core ID to the module name to create instance name
cmccInstanceName  = cmccID if cmccID is not None else "CMCC"

symCMCCInstance = coreComponent.createStringSymbol("CMCC_INSTANCE_NAME", None)
symCMCCInstance.setValue(cmccInstanceName)
symCMCCInstance.setVisible(False)

symCCFGNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CMCC\"]/register-group@[name=\"CMCC\"]/register@[name=\"CMCC_CFG\"]")
symCCFGExists = coreComponent.createBooleanSymbol("CMCC_CCFG_EXISTS", None)
symCCFGExists.setDefaultValue(symCCFGNode is not None)
symCCFGExists.setVisible(False)



############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

cmccHeaderFile = coreComponent.createFileSymbol("CMCC_HEADER_FILE", None)
cmccHeaderFile.setSourcePath("../peripheral/cmcc_11108/templates/plib_cmcc.h.ftl")
cmccHeaderFile.setOutputName("plib_" + cmccInstanceName.lower() + ".h")
cmccHeaderFile.setDestPath("/peripheral/cmcc/")
cmccHeaderFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccHeaderFile.setType("HEADER")
cmccHeaderFile.setOverwrite(True)
cmccHeaderFile.setEnabled(True)
cmccHeaderFile.setMarkup(True)
cmccHeaderFile.setDependencies(enableFileGen, ["INSTRUCTION_CACHE_ENABLE"])

cmccSourceFile = coreComponent.createFileSymbol("CMCC_SOURCE_FILE", None)
cmccSourceFile.setSourcePath("../peripheral/cmcc_11108/templates/plib_cmcc.c.ftl")
cmccSourceFile.setOutputName("plib_" + cmccInstanceName.lower() + ".c")
cmccSourceFile.setDestPath("/peripheral/cmcc/")
cmccSourceFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccSourceFile.setType("SOURCE")
cmccSourceFile.setOverwrite(True)
cmccSourceFile.setMarkup(True)
cmccSourceFile.setEnabled(True)

# System Definition
cmccSystemDefFile = coreComponent.createFileSymbol("CMCC_SYS_DEF_FILE", None)
cmccSystemDefFile.setType("STRING")
cmccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
cmccSystemDefFile.setSourcePath("../peripheral/cmcc_11108/templates/system/definitions.h.ftl")
cmccSystemDefFile.setMarkup(True)
