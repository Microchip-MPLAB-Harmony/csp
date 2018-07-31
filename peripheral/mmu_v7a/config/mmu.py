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

configName = Variables.get("__CONFIGURATION_NAME")

mmuFile = coreComponent.createFileSymbol("MMU_C", None)
mmuFile.setSourcePath("../peripheral/mmu_v7a/templates/plib_mmu.c.ftl")
mmuFile.setOutputName("plib_mmu.c")
mmuFile.setDestPath("peripheral/mmu/")
mmuFile.setProjectPath("config/" + configName + "/peripheral/mmu/")
mmuFile.setType("SOURCE")
mmuFile.setMarkup(True)

mmuHeader = coreComponent.createFileSymbol("MMU_H", None)
mmuHeader.setSourcePath("../peripheral/mmu_v7a/plib_mmu.h")
mmuHeader.setOutputName("plib_mmu.h")
mmuHeader.setDestPath("peripheral/mmu/")
mmuHeader.setProjectPath("config/" + configName + "/peripheral/mmu/")
mmuHeader.setType("HEADER")
mmuHeader.setMarkup(False)

mmuSystemInitFile = coreComponent.createFileSymbol("mmuSystemInitFile", None)
mmuSystemInitFile.setType("STRING")
mmuSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
mmuSystemInitFile.setSourcePath("../peripheral/mmu_v7a/templates/system/system_initialize.c.ftl")
mmuSystemInitFile.setMarkup(True)

mmuSystemDefFile = coreComponent.createFileSymbol("mmuSystemDefFile", None)
mmuSystemDefFile.setType("STRING")
mmuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
mmuSystemDefFile.setSourcePath("../peripheral/mmu_v7a/templates/system/system_definitions.h.ftl")
mmuSystemDefFile.setMarkup(True)
