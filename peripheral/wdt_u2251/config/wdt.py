#######################################################################################################################################
#####################################       WDT Database Components      ##########################################################
#######################################################################################################################################

#main menu
wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

#WDT Index
wdt_Index = coreComponent.createIntegerSymbol("WDT_INDEX", wdtMenu)
wdt_Index.setVisible(False)
wdt_Index.setDefaultValue(0)

#Enable Early Interrupt
wdtSym_CTRLA_EW = coreComponent.createBooleanSymbol("WDT_EW_ENABLE", wdtMenu)
wdtSym_CTRLA_EW.setLabel("Enable Watchdog Early Interrupt")

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"WDT\"]")
wdtModuleID = wdtModuleNode.getAttribute("id")

	
wdtHeader1File = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeader1File.setSourcePath("../peripheral/wdt_"+wdtModuleID+"/templates/plib_wdt.h.ftl")
wdtHeader1File.setOutputName("plib_wdt0.h")
wdtHeader1File.setDestPath("/peripheral/wdt/")
wdtHeader1File.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeader1File.setType("HEADER")
wdtHeader1File.setMarkup(True)

wdtSource1File = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSource1File.setSourcePath("../peripheral/wdt_"+wdtModuleID+"/templates/plib_wdt.c.ftl")
wdtSource1File.setOutputName("plib_wdt0.c")
wdtSource1File.setDestPath("/peripheral/wdt/")
wdtSource1File.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSource1File.setType("SOURCE")
wdtSource1File.setMarkup(True)

wdtSystemInitFile = coreComponent.createFileSymbol("WDT_SYS_INIT", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_"+wdtModuleID+"/templates/system/initialization.c.ftl")
wdtSystemInitFile.setMarkup(True)

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_"+wdtModuleID+"/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)