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

Log.writeInfoMessage("Loading MMU for " + Variables.get("__PROCESSOR"))

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(True)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

cacheAlign = coreComponent.createIntegerSymbol("CACHE_ALIGN", cacheMenu)
cacheAlign.setLabel("Cache Alignment Length")
cacheAlign.setVisible(False)
cacheAlign.setDefaultValue(32)

ddrNoCacheStart = int(Database.getSymbolValue("core", "DDRAM_NO_CACHE_START"), 0)
ddrCacheStart = int(Database.getSymbolValue("core", "DDRAM_CACHE_START"), 0)
ddrCacheEnd = int(Database.getSymbolValue("core", "DDRAM_CACHE_END"), 0)

noCacheBegin = coreComponent.createStringSymbol("NO_CACHE_START", cacheMenu)
noCacheBegin.setVisible(False)
noCacheBegin.setDefaultValue("0x%X"% (ddrNoCacheStart >> 20))

cacheBegin = coreComponent.createStringSymbol("CACHE_START", cacheMenu)
cacheBegin.setVisible(False)
cacheBegin.setDefaultValue("0x%X"% (ddrCacheStart >> 20))

cacheEnd = coreComponent.createStringSymbol("CACHE_END", cacheMenu)
cacheEnd.setVisible(False)
cacheEnd.setDefaultValue("0x%X"% ((ddrCacheEnd + 1) >> 20))

configName = Variables.get("__CONFIGURATION_NAME")

mmuFile = coreComponent.createFileSymbol("MMU_C", None)
mmuFile.setSourcePath("../peripheral/mmu_v7a/templates/plib_mmu.c.ftl")
mmuFile.setOutputName("plib_mmu.c")
mmuFile.setDestPath("peripheral/mmu/")
mmuFile.setProjectPath("config/" + configName + "/peripheral/mmu/")
mmuFile.setType("SOURCE")
mmuFile.setMarkup(True)

mmuHeader = coreComponent.createFileSymbol("MMU_H", None)
mmuHeader.setSourcePath("../peripheral/mmu_v7a/templates/plib_mmu.h.ftl")
mmuHeader.setOutputName("plib_mmu.h")
mmuHeader.setDestPath("peripheral/mmu/")
mmuHeader.setProjectPath("config/" + configName + "/peripheral/mmu/")
mmuHeader.setType("HEADER")
mmuHeader.setMarkup(True)

mmuSystemInitFile = coreComponent.createFileSymbol("mmuSystemInitFile", None)
mmuSystemInitFile.setType("STRING")
mmuSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
mmuSystemInitFile.setSourcePath("../peripheral/mmu_v7a/templates/system/initialization.c.ftl")
mmuSystemInitFile.setMarkup(True)

mmuSystemDefFile = coreComponent.createFileSymbol("mmuSystemDefFile", None)
mmuSystemDefFile.setType("STRING")
mmuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
mmuSystemDefFile.setSourcePath("../peripheral/mmu_v7a/templates/system/definitions.h.ftl")
mmuSystemDefFile.setMarkup(True)
