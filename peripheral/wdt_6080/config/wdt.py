Log.writeInfoMessage("Loading WDT for " + Variables.get("__PROCESSOR"))

wdtMenu = coreComponent.createMenuSymbol(None, None)
wdtMenu.setLabel("WDT")

wdtEnable = coreComponent.createBooleanSymbol("wdtENABLE", wdtMenu)
wdtEnable.setLabel("Enable Watchdog Timer?")
wdtEnable.setDefaultValue(False)

def wdtEnableCfgMenu(wdtCfgMenu, event):
	wdtCfgMenu.setVisible(event["value"])

	component = wdtCfgMenu.getComponent()
	component.getSymbolByID("wdtHeaderFile").setEnabled(event["value"])
	component.getSymbolByID("wdtSourceFile").setEnabled(event["value"])
	component.getSymbolByID("wdtSystemDefFile").setEnabled(event["value"])

	if event["value"] == False:
		Database.clearSymbolValue("core", "rswdtENABLE")		
		Database.setSymbolValue("core", "rswdtENABLE", False, 1)

wdtCfgMenu = coreComponent.createMenuSymbol(None, wdtMenu)
wdtCfgMenu.setLabel("WDT Configuration")
wdtCfgMenu.setDependencies(wdtEnableCfgMenu, ["wdtENABLE"])

wdtReset = coreComponent.createBooleanSymbol("wdtEnableReset", wdtCfgMenu)
wdtReset.setLabel("Enable Reset")
wdtReset.setDefaultValue(True)

def wdtResetEnable(wdtInterrupt, event):
	if event["value"] == True:
		wdtInterrupt.setVisible(False)
		wdtInterrupt.setValue(False, 2)
	else:
		wdtInterrupt.setVisible(True)

wdtInterrupt = coreComponent.createBooleanSymbol("wdtinterruptMode", wdtCfgMenu)
wdtInterrupt.setLabel("Enable Interrupts")
wdtInterrupt.setDefaultValue(False)
wdtInterrupt.setDependencies(wdtResetEnable, ["wdtEnableReset"])
wdtInterrupt.setVisible(False)

wdtCounterValue = coreComponent.createIntegerSymbol("wdtWDV", wdtCfgMenu)
wdtCounterValue.setLabel("Counter value")
wdtCounterValue.setMax(0xfff)
wdtCounterValue.setDefaultValue(0xfff)

def	wdtcounter_cal(wdtCounterValueTime, event):
	data = event["value"] * 3.90625
	wdtCounterValueTime.setValue(int(round(data)),2)

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
	wdtDeltaValueTime.setValue(int(round(data)),2)
	
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

global peripId
global NVICVector
global NVICHandler
global NVICHandlerLock

peripId = Interrupt.getInterruptIndex("WDT")
NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

Database.clearSymbolValue("core", NVICVector)
Database.setSymbolValue("core", NVICVector, False, 2)
Database.clearSymbolValue("core", NVICHandler)
Database.setSymbolValue("core", NVICHandler, "WDT0_InterruptHandler", 2)
Database.clearSymbolValue("core", NVICHandlerLock)
Database.setSymbolValue("core", NVICHandlerLock, True, 2)

def NVICControl(NVIC, event):
	global NVICVector
	global NVICHandler
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "WDT0_InterruptHandler", 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "WDT0_Handler", 2)
		
# NVIC Dynamic settings
wdtNVICControl = coreComponent.createBooleanSymbol("NVIC_WDT_ENABLE", None)
wdtNVICControl.setDependencies(NVICControl, ["wdtinterruptMode"])
wdtNVICControl.setVisible(False)


		
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
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_initialize.c.ftl")
wdtSystemInitFile.setMarkup(True)

wdtSystemDefFile = coreComponent.createFileSymbol("wdtSystemDefFile", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
