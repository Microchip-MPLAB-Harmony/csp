def instantiateComponent(wdtComponent):

	num = wdtComponent.getID()[-1:]
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
	wdtCounterValue.setMax(0xfff)
	wdtCounterValue.setDefaultValue(0xfff)
	
	wdtCounterValueTime = wdtComponent.createIntegerSymbol("wdtWDVTIME", wdtMenu)
	wdtCounterValueTime.setLabel("Counter value in ms")
	wdtCounterValueTime.setDependencies(wdtcounter_cal, ["wdtWDV"])
	wdtCounterValueTime.setReadOnly(True)
	
	wdtIndex = wdtComponent.createIntegerSymbol("INDEX", wdtMenu)
	wdtIndex.setVisible(False)
	wdtIndex.setDefaultValue(int(num))
	
	wdtDeltaValue = wdtComponent.createIntegerSymbol("wdtWDD", wdtMenu)
	wdtDeltaValue.setLabel("Delta value")
	wdtDeltaValue.setMax(0xfff)
	wdtDeltaValue.setDefaultValue(0xfff)
	
	wdtDeltaValueTime = wdtComponent.createIntegerSymbol("wdtWDDTIME", wdtMenu)
	wdtDeltaValueTime.setLabel("Counter value in ms")
	wdtDeltaValueTime.setDependencies(wdtdelta_cal, ["wdtWDD"])
	wdtDeltaValueTime.setReadOnly(True)
	
	wdtDebugHalt = wdtComponent.createBooleanSymbol("wdtdebugHalt", wdtMenu)
	print(wdtDebugHalt)
	wdtDebugHalt.setLabel("Enable Debug halt")
	wdtDebugHalt.setDefaultValue(False)

	wdtIdleHalt = wdtComponent.createBooleanSymbol("wdtidleHalt", wdtMenu)
	print(wdtIdleHalt)
	wdtIdleHalt.setLabel("Enable Idle halt")
	wdtIdleHalt.setDefaultValue(False)	
	
	wdtDisableValue = Database.getSymbolValue("core", "wdtDISABLE")
	
	if wdtDisableValue == False:
		configName = Variables.get("__CONFIGURATION_NAME")

		wdtHeader1File = wdtComponent.createFileSymbol(None, None)
		wdtHeader1File.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.h.ftl")
		wdtHeader1File.setOutputName("plib_wdt" + str(num) + ".h")
		wdtHeader1File.setDestPath("peripheral/wdt/")
		wdtHeader1File.setProjectPath("config/" + configName + "/peripheral/wdt/")
		wdtHeader1File.setType("HEADER")
		wdtHeader1File.setMarkup(True)
		
		wdtSource1File = wdtComponent.createFileSymbol(None, None)
		wdtSource1File.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.c.ftl")
		wdtSource1File.setOutputName("plib_wdt" + str(num) + ".c")
		wdtSource1File.setDestPath("peripheral/wdt/")
		wdtSource1File.setProjectPath("config/" + configName + "/peripheral/wdt/")
		wdtSource1File.setType("SOURCE")
		wdtSource1File.setMarkup(True)
		
		
		wdtSystemInitFile = wdtComponent.createFileSymbol(None, None)
		wdtSystemInitFile.setType("STRING")
		wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
		wdtSystemInitFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_initialize.h.ftl")
		wdtSystemInitFile.setMarkup(True)

		wdtSystemIntFile = wdtComponent.createFileSymbol(None, None)
		wdtSystemIntFile.setType("STRING")
		wdtSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
		wdtSystemIntFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_interrupt.c.ftl")
		wdtSystemIntFile.setMarkup(True)

		wdtSystemDefFile = wdtComponent.createFileSymbol(None, None)
		wdtSystemDefFile.setType("STRING")
		wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
		wdtSystemDefFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_definitions.h.ftl")
		wdtSystemDefFile.setMarkup(True)

def wdtResetEnable(wdtInterrupt,test):
	if test.getValue() == True:
		wdtInterrupt.setVisible(False)
		wdtInterrupt.setValue("wdtinterruptMode", False, 2)
	else:
		wdtInterrupt.setVisible(True)

def	wdtdelta_cal(wdtDeltaValueTime,test):
	data = test.getValue() * 3.90625
	wdtDeltaValueTime.setValue("wdtWDDTIME",int(round(data)),2)
	
def	wdtcounter_cal(wdtCounterValueTime,test):
	data = test.getValue() * 3.90625
	wdtCounterValueTime.setValue("wdtWDVTIME",int(round(data)),2)
