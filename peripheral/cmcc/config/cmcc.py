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

global  cmccHeaderFile
global  cmccSourceFile
global  cmccSystemDefFile

def enableFileGen(symbol, event):

    if (Database.getSymbolValue("core", "DATA_CACHE_ENABLE") == True) or (Database.getSymbolValue("core", "INSTRUCTION_CACHE_ENABLE") == True):
        cmccHeaderFile.setEnabled(True)
        cmccSourceFile.setEnabled(True)
        cmccSystemDefFile.setEnabled(True)
    else:
        cmccHeaderFile.setEnabled(False)
        cmccSourceFile.setEnabled(False)
        cmccSystemDefFile.setEnabled(False)

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

cmccHeaderFile = coreComponent.createFileSymbol("CMCC_FILE_0", None)
cmccHeaderFile.setSourcePath("../peripheral/cmcc/templates/plib_cmcc.h.ftl")
cmccHeaderFile.setOutputName("plib_cmcc.h")
cmccHeaderFile.setDestPath("/peripheral/cmcc/")
cmccHeaderFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccHeaderFile.setType("HEADER")
cmccHeaderFile.setOverwrite(True)
cmccHeaderFile.setEnabled(True)
cmccHeaderFile.setMarkup(True)
cmccHeaderFile.setDependencies(enableFileGen, ["DATA_CACHE_ENABLE", "INSTRUCTION_CACHE_ENABLE"])

cmccSourceFile = coreComponent.createFileSymbol("CMCC_FILE_1", None)
cmccSourceFile.setSourcePath("../peripheral/cmcc/templates/plib_cmcc.c.ftl")
cmccSourceFile.setOutputName("plib_cmcc.c")
cmccSourceFile.setDestPath("/peripheral/cmcc/")
cmccSourceFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccSourceFile.setType("SOURCE")
cmccSourceFile.setOverwrite(True)
cmccSourceFile.setMarkup(True)
cmccSourceFile.setEnabled(True)

cmccSystemDefFile = coreComponent.createFileSymbol("CMCC_FILE_2", None)
cmccSystemDefFile.setType("STRING")
cmccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
cmccSystemDefFile.setSourcePath("../peripheral/cmcc/templates/system/definitions.h.ftl")
cmccSystemDefFile.setMarkup(True)
cmccSystemDefFile.setEnabled(True)       