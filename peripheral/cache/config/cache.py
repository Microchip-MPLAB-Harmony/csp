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
Log.writeInfoMessage("Loading Cache for " + Variables.get("__PROCESSOR"))

def cacheEnable(symbol, event):
    symbol.setValue(event["value"], 1)

def cacheFilesEnable(symbol, event):
    symbol.setEnabled(event["value"])

dcacheEnable = coreComponent.createBooleanSymbol("USE_CACHE_MAINTENANCE", cacheMenu)
dcacheEnable.setLabel("Use Cache Maintenance")
dcacheEnable.setDefaultValue(False)

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(False)
dcacheEnable.setVisible(False)
dcacheEnable.setReadOnly(True)
dcacheEnable.setDependencies(cacheEnable, ["USE_CACHE_MAINTENANCE"])

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(False)
icacheEnable.setVisible(False)
icacheEnable.setReadOnly(True)
icacheEnable.setDependencies(cacheEnable, ["USE_CACHE_MAINTENANCE"])

############################################################################
#### Code Generation ####
############################################################################

configName = Variables.get("__CONFIGURATION_NAME")

cacheSourceFile = coreComponent.createFileSymbol("CACHE_LOCAL_H", None)
cacheSourceFile.setSourcePath("../peripheral/cache/templates/plib_cache_local.h")
cacheSourceFile.setOutputName("plib_cache_local.h")
cacheSourceFile.setDestPath("peripheral/cache/")
cacheSourceFile.setProjectPath("config/" + configName + "/peripheral/cache/")
cacheSourceFile.setType("SOURCE")
cacheSourceFile.setEnabled(False)
cacheSourceFile.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])

cacheHeaderFile = coreComponent.createFileSymbol("CACHE_HEADER_H", None)
cacheHeaderFile.setSourcePath("../peripheral/cache/templates/plib_cache.h")
cacheHeaderFile.setOutputName("plib_cache.h")
cacheHeaderFile.setDestPath("peripheral/cache/")
cacheHeaderFile.setProjectPath("config/" + configName + "/peripheral/cache/")
cacheHeaderFile.setType("HEADER")
cacheHeaderFile.setEnabled(False)
cacheHeaderFile.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])

cacheSourcePic32MzFile = coreComponent.createFileSymbol("CACHE_SOURCE_PIC32MZ_C", None)
cacheSourcePic32MzFile.setSourcePath("../peripheral/cache/templates/plib_cache_pic32mz.c")
cacheSourcePic32MzFile.setOutputName("plib_cache.c")
cacheSourcePic32MzFile.setDestPath("peripheral/cache/")
cacheSourcePic32MzFile.setProjectPath("config/" + configName + "/peripheral/cache/")
cacheSourcePic32MzFile.setType("SOURCE")
cacheSourcePic32MzFile.setEnabled(False)
cacheSourcePic32MzFile.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])

cacheHeaderPic32MzFile = coreComponent.createFileSymbol("CACHE_PIC32MZ_H", None)
cacheHeaderPic32MzFile.setSourcePath("../peripheral/cache/templates/plib_cache_pic32mz.h")
cacheHeaderPic32MzFile.setOutputName("plib_cache_pic32mz.h")
cacheHeaderPic32MzFile.setDestPath("peripheral/cache/")
cacheHeaderPic32MzFile.setProjectPath("config/" + configName + "/peripheral/cache/")
cacheHeaderPic32MzFile.setType("HEADER")
cacheHeaderPic32MzFile.setEnabled(False)
cacheHeaderPic32MzFile.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])

cacheSourcePic32MzAsm = coreComponent.createFileSymbol("CACHE_SOURCE_PIC32MZ_S", None)
cacheSourcePic32MzAsm.setSourcePath("../peripheral/cache/templates/plib_cache_pic32mz.S")
cacheSourcePic32MzAsm.setOutputName("plib_cache_pic32mz.S")
cacheSourcePic32MzAsm.setDestPath("peripheral/cache/")
cacheSourcePic32MzAsm.setProjectPath("config/" + configName + "/peripheral/cache/")
cacheSourcePic32MzAsm.setType("SOURCE")
cacheSourcePic32MzAsm.setEnabled(False)
cacheSourcePic32MzAsm.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])

cacheSystemDefFile = coreComponent.createFileSymbol("CACHE_SYSTEM_DEF_H", None)
cacheSystemDefFile.setType("STRING")
cacheSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
cacheSystemDefFile.setSourcePath("../peripheral/cache/templates/system/definitions.h.ftl")
cacheSystemDefFile.setMarkup(True)
cacheSystemDefFile.setEnabled(False)
cacheSystemDefFile.setDependencies(cacheFilesEnable, ["USE_CACHE_MAINTENANCE"])
