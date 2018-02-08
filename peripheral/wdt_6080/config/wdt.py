print("Loading WDT for " + Variables.get("__PROCESSOR"))

wdtMenu = coreComponent.createMenuSymbol(None, None)
wdtMenu.setLabel("WDT")

wdtEnable = coreComponent.createBooleanSymbol("wdtENABLE", wdtMenu)
wdtEnable.setLabel("Enable Watchdog Timer?")
wdtEnable.setDefaultValue(True)

def wdtEnableCfgMenu(wdtCfgMenu, wdtEnable):
	wdtCfgMenu.setVisible(event["value"])

	component = wdtCfgMenu.getComponent()
	component.getSymbolByID("wdtHeaderFile").setEnabled(event["value"])
	component.getSymbolByID("wdtSourceFile").setEnabled(event["value"])
	component.getSymbolByID("wdtSystemIntFile").setEnabled(event["value"])
	component.getSymbolByID("wdtSystemDefFile").setEnabled(event["value"])

	if event["value"] == False:
		component.getSymbolByID("wdtRswdtEnable").setValue(False, 1)

wdtCfgMenu = coreComponent.createMenuSymbol(None, wdtMenu)
wdtCfgMenu.setLabel("WDT Configuration")
wdtCfgMenu.setDependencies(wdtEnableCfgMenu, ["wdtENABLE"])

wdtReset = coreComponent.createBooleanSymbol("wdtEnableReset", wdtCfgMenu)
wdtReset.setLabel("Enable Reset")
wdtReset.setDefaultValue(False)

def wdtResetEnable(wdtInterrupt, event):
	if event["value"] == True:
		wdtInterrupt.setVisible(False)
		wdtInterrupt.setValue("wdtinterruptMode", False, 2)
	else:
		wdtInterrupt.setVisible(True)

wdtInterrupt = coreComponent.createBooleanSymbol("wdtinterruptMode", wdtCfgMenu)
wdtInterrupt.setLabel("Enable Interrupts")
wdtInterrupt.setDefaultValue(True)
wdtInterrupt.setDependencies(wdtResetEnable, ["wdtEnableReset"])

wdtCounterValue = coreComponent.createIntegerSymbol("wdtWDV", wdtCfgMenu)
wdtCounterValue.setLabel("Counter value")
wdtCounterValue.setMax(0xfff)
wdtCounterValue.setDefaultValue(0xfff)

def	wdtcounter_cal(wdtCounterValueTime, event):
	data = event["value"] * 3.90625
	wdtCounterValueTime.setValue("wdtWDVTIME",int(round(data)),2)

wdtCounterValueTime = coreComponent.createIntegerSymbol("wdtWDVTIME", wdtCfgMenu)
wdtCounterValueTime.setLabel("Counter value in ms")
wdtCounterValueTime.setDependencies(wdtcounter_cal, ["wdtWDV"])
wdtCounterValueTime.setReadOnly(True)

wdtIndex = coreComponent.createIntegerSymbol("wdtIndex", wdtCfgMenu)
wdtIndex.setVisible(False)
wdtIndex.setDefaultValue(0)

wdtDeltaValue = coreComponent.createIntegerSymbol("wdtWDD", wdtCfgMenu)
wdtDeltaValue.setLabel("Delta value")
wdtDeltaValue.setMax(0xfff)
wdtDeltaValue.setDefaultValue(0xfff)

def	wdtdelta_cal(wdtDeltaValueTime, event):
	data = event["value"] * 3.90625
	wdtDeltaValueTime.setValue("wdtWDDTIME",int(round(data)),2)
	
wdtDeltaValueTime = coreComponent.createIntegerSymbol("wdtWDDTIME", wdtCfgMenu)
wdtDeltaValueTime.setLabel("Counter value in ms")
wdtDeltaValueTime.setDependencies(wdtdelta_cal, ["wdtWDD"])
wdtDeltaValueTime.setReadOnly(True)
	
wdtDebugHalt = coreComponent.createBooleanSymbol("wdtdebugHalt", wdtCfgMenu)
wdtDebugHalt.setLabel("Enable Debug halt")
wdtDebugHalt.setDefaultValue(False)

wdtIdleHalt = coreComponent.createBooleanSymbol("wdtidleHalt", wdtCfgMenu)
wdtIdleHalt.setLabel("Enable Idle halt")
wdtIdleHalt.setDefaultValue(False)	

configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("wdtHeaderFile", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_wdt0.h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)

wdtSourceFile = coreComponent.createFileSymbol("wdtSourceFile", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_wdt0.c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)

wdtSystemInitFile = coreComponent.createFileSymbol("wdtSystemInitFile", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_initialize.c.ftl")
wdtSystemInitFile.setMarkup(True)

wdtSystemIntFile = coreComponent.createFileSymbol("wdtSystemIntFile", None)
wdtSystemIntFile.setType("STRING")
wdtSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
wdtSystemIntFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_interrupt.c.ftl")
wdtSystemIntFile.setMarkup(True)

wdtSystemDefFile = coreComponent.createFileSymbol("wdtSystemDefFile", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
