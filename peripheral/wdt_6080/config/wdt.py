def instantiateComponent(wdtComponent):

	num = wdtComponent.getID()
	print("Running WDT" )

	wdtMenu = wdtComponent.createMenuSymbol(None, None)
	wdtMenu.setLabel("Hardware Settings ")
	
	wdtReset = wdtComponent.createBooleanSymbol("wdtEnableReset", wdtMenu)
	print(wdtReset)
	wdtReset.setLabel("Enable Reset")
	wdtReset.setDefaultValue(False)
	
	wdtInterrupt = wdtComponent.createBooleanSymbol("wdtinterruptMode", wdtMenu)
	print(wdtInterrupt)
	wdtInterrupt.setLabel("Enable Interrupts")
	wdtInterrupt.setDefaultValue(True)
	wdtInterrupt.setDependencies(wdtResetEnable, ["wdtEnableReset"])
	
	wdtCounterValue = wdtComponent.createIntegerSymbol("wdtWDV", wdtMenu)
	wdtCounterValue.setLabel("Counter value")
	wdtCounterValue.setMax(0x1ff)
	wdtCounterValue.setDefaultValue(0x1ff)
	
	wdtDeltaValue = wdtComponent.createIntegerSymbol("wdtWDD", wdtMenu)
	wdtDeltaValue.setLabel("Delta value")
	wdtDeltaValue.setMax(0x1ff)
	wdtDeltaValue.setDefaultValue(0x1ff)
	
	wdtDebugHalt = wdtComponent.createBooleanSymbol("wdtdebugHalt", wdtMenu)
	print(wdtDebugHalt)
	wdtDebugHalt.setLabel("Enable Debug halt")
	wdtDebugHalt.setDefaultValue(False)

	wdtIdleHalt = wdtComponent.createBooleanSymbol("wdtidleHalt", wdtMenu)
	print(wdtIdleHalt)
	wdtIdleHalt.setLabel("Enable Idle halt")
	wdtIdleHalt.setDefaultValue(False)	
	
	configName = Variables.get("__CONFIGURATION_NAME")

	wdtHeader1File = wdtComponent.createFileSymbol(None, None)
	wdtHeader1File.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.h.ftl")
	wdtHeader1File.setOutputName("plib_wdt.h")
	wdtHeader1File.setDestPath("system_config/" + configName +"/peripheral/wdt/")
	wdtHeader1File.setProjectPath("system_config/" + configName +"/peripheral/wdt/")
	wdtHeader1File.setType("HEADER")
	
	wdtSource1File = wdtComponent.createFileSymbol(None, None)
	wdtSource1File.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.c.ftl")
	wdtSource1File.setOutputName("plib_wdt.c")
	wdtSource1File.setDestPath("system_config/" + configName +"/peripheral/wdt/")
	wdtSource1File.setProjectPath("system_config/" + configName +"/peripheral/wdt/")
	wdtSource1File.setType("SOURCE")

def wdtResetEnable(wdtInterrupt,test):
	if test.getValue() == True:
		wdtInterrupt.setVisible(False)
	else:
		wdtInterrupt.setVisible(True)