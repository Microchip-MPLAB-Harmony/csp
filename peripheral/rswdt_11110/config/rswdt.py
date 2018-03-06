Log.writeInfoMessage("Loading RSWDT for " + Variables.get("__PROCESSOR"))

global NVICVector
global NVICHandler

rswdtMenu = coreComponent.createMenuSymbol(None, None)
rswdtMenu.setLabel("RSWDT")

rswdtEnable = coreComponent.createBooleanSymbol("rswdtENABLE", rswdtMenu)
rswdtEnable.setLabel("Enable Reinforced Safety Watchdog Timer (RSWDT)?")
rswdtEnable.setDefaultValue(False)

def rswdtEnableCfgMenu(rswdtCfgMenu, event):
	rswdtCfgMenu.setVisible(event["value"])
	
	component = rswdtCfgMenu.getComponent()
	component.getSymbolByID("rswdtHeaderFile").setEnabled(event["value"])
	component.getSymbolByID("rswdtSourceFile").setEnabled(event["value"])
	component.getSymbolByID("rswdtSystemDefFile").setEnabled(event["value"])

rswdtCfgMenu = coreComponent.createMenuSymbol(None, rswdtMenu)
rswdtCfgMenu.setLabel("RSWDT Configuration")
rswdtCfgMenu.setDependencies(rswdtEnableCfgMenu, ["rswdtENABLE"])

rswdtReset = coreComponent.createBooleanSymbol("rswdtEnableReset", rswdtCfgMenu)
rswdtReset.setLabel("Enable Reset")
rswdtReset.setDefaultValue(True)

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

peripId = Interrupt.getInterruptIndex("RSWDT")
NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

Database.clearSymbolValue("core", NVICVector)
Database.setSymbolValue("core", NVICVector, False, 2)
Database.clearSymbolValue("core", NVICHandler)
Database.setSymbolValue("core", NVICHandler, "RSWDT0_InterruptHandler", 2)
Database.clearSymbolValue("core", NVICHandlerLock)
Database.setSymbolValue("core", NVICHandlerLock, True, 2)

def NVICControl(NVIC, event):
	global NVICVector
	global NVICHandler
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "RSWDT0_InterruptHandler", 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "RSWDT0_Handler", 2)
		
# NVIC Dynamic settings
rswdtNVICControl = coreComponent.createBooleanSymbol("NVIC_RSWDT_ENABLE", None)
rswdtNVICControl.setDependencies(NVICControl, ["rswdtinterruptMode"])
rswdtNVICControl.setVisible(False)

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
rswdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
rswdtSystemInitFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_initialize.c.ftl")
rswdtSystemInitFile.setMarkup(True)

rswdtSystemDefFile = coreComponent.createFileSymbol("rswdtSystemDefFile", None)
rswdtSystemDefFile.setType("STRING")
rswdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
rswdtSystemDefFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_definitions.h.ftl")
rswdtSystemDefFile.setMarkup(True)



