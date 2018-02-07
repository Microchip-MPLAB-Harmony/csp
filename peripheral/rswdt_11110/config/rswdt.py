print("Loading RSWDT for " + Variables.get("__PROCESSOR"))

rswdtMenu = coreComponent.createMenuSymbol(None, None)
rswdtMenu.setLabel("RSWDT")

rswdtEnable = coreComponent.createBooleanSymbol("rswdtENABLE", rswdtMenu)
rswdtEnable.setLabel("Enable Reinforced Safety Watchdog Timer (RSWDT)?")
rswdtEnable.setDefaultValue(True)

def rswdtEnableCfgMenu(rswdtCfgMenu, event):
	rswdtCfgMenu.setVisible(event["value"])
	
	component = rswdtCfgMenu.getComponent()
	component.getSymbolByID("rswdtHeaderFile").setEnabled(event["value"])
	component.getSymbolByID("rswdtSourceFile").setEnabled(event["value"])
	component.getSymbolByID("rswdtSystemIntFile").setEnabled(event["value"])
	component.getSymbolByID("rswdtSystemDefFile").setEnabled(event["value"])

rswdtCfgMenu = coreComponent.createMenuSymbol(None, rswdtMenu)
rswdtCfgMenu.setLabel("RSWDT Configuration")
rswdtCfgMenu.setDependencies(rswdtEnableCfgMenu, ["rswdtENABLE"])

rswdtReset = coreComponent.createBooleanSymbol("rswdtEnableReset", rswdtCfgMenu)
rswdtReset.setLabel("Enable Reset")
rswdtReset.setDefaultValue(False)

def rswdtResetEnable(rswdtInterrupt,event):
	if event["value"] == True:
		rswdtInterrupt.setVisible(False)
		rswdtInterrupt.setValue(False,2)
	else:
		rswdtInterrupt.setVisible(True)

rswdtInterrupt = coreComponent.createBooleanSymbol("rswdtinterruptMode", rswdtCfgMenu)
rswdtInterrupt.setLabel("Enable Interrupts")
rswdtInterrupt.setDefaultValue(False)
rswdtInterrupt.setDependencies(rswdtResetEnable, ["rswdtEnableReset"])

rswdtCounterValue = coreComponent.createIntegerSymbol("rswdtWDV", rswdtCfgMenu)
rswdtCounterValue.setLabel("Counter value")
rswdtCounterValue.setMax(0xfff)
rswdtCounterValue.setDefaultValue(0xfff)

def	rswdtcounter_cal(rswdtCounterValueTime, event):
	data = event["value"] * 3.90625
	rswdtCounterValueTime.setValue(int(round(data)),2)

rswdtCounterValueTime = coreComponent.createIntegerSymbol("rswdtWDVTIME", rswdtCfgMenu)
rswdtCounterValueTime.setLabel("Counter value in ms")
rswdtCounterValueTime.setDependencies(rswdtcounter_cal, ["rswdtWDV"])
rswdtCounterValueTime.setReadOnly(True)

rswdtDebugHalt = coreComponent.createBooleanSymbol("rswdtdebugHalt", rswdtCfgMenu)
rswdtDebugHalt.setLabel("Enable Debug halt")
rswdtDebugHalt.setDefaultValue(False)

rswdtIndex = coreComponent.createIntegerSymbol("rswdtIndex", rswdtCfgMenu)
rswdtIndex.setVisible(False)
rswdtIndex.setDefaultValue(0)

rswdtIdleHalt = coreComponent.createBooleanSymbol("rswdtidleHalt", rswdtCfgMenu)
rswdtIdleHalt.setLabel("Enable Idle halt")
rswdtIdleHalt.setDefaultValue(False)	

configName = Variables.get("__CONFIGURATION_NAME")

rswdtHeaderFile = coreComponent.createFileSymbol("rswdtHeaderFile", None)
rswdtHeaderFile.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.h.ftl")
rswdtHeaderFile.setOutputName("plib_rswdt0.h")
rswdtHeaderFile.setDestPath("peripheral/rswdt/")
rswdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/rswdt/")
rswdtHeaderFile.setType("HEADER")
rswdtHeaderFile.setMarkup(True)
	
rswdtSourceFile = coreComponent.createFileSymbol("rswdtSourceFile", None)
rswdtSourceFile.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.c.ftl")
rswdtSourceFile.setOutputName("plib_rswdt0.c")
rswdtSourceFile.setDestPath("peripheral/rswdt/")
rswdtSourceFile.setProjectPath("config/" + configName + "/peripheral/rswdt/")
rswdtSourceFile.setType("SOURCE")
rswdtSourceFile.setMarkup(True)
		
rswdtSystemInitFile = coreComponent.createFileSymbol("rswdtSystemInitFile", None)
rswdtSystemInitFile.setType("STRING")
rswdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
rswdtSystemInitFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_initialize.c.ftl")
rswdtSystemInitFile.setMarkup(True)

rswdtSystemIntFile = coreComponent.createFileSymbol("rswdtSystemIntFile", None)
rswdtSystemIntFile.setType("STRING")
rswdtSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
rswdtSystemIntFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_interrupt.c.ftl")
rswdtSystemIntFile.setMarkup(True)

rswdtSystemDefFile = coreComponent.createFileSymbol("rswdtSystemDefFile", None)
rswdtSystemDefFile.setType("STRING")
rswdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
rswdtSystemDefFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_definitions.h.ftl")
rswdtSystemDefFile.setMarkup(True)



