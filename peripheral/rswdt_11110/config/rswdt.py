def instantiateComponent(rswdtComponent):

	num = rswdtComponent.getID()[-1:]
	print("Running WDT" )

	rswdtMenu = rswdtComponent.createMenuSymbol(None, None)
	rswdtMenu.setLabel("Hardware Settings ")
	
	rswdtReset = rswdtComponent.createBooleanSymbol("rswdtEnableReset", rswdtMenu)
	print(rswdtReset)
	rswdtReset.setLabel("Enable Reset")
	rswdtReset.setDefaultValue(False)
	
	rswdtInterrupt = rswdtComponent.createBooleanSymbol("rswdtinterruptMode", rswdtMenu)
	print(rswdtInterrupt)
	rswdtInterrupt.setLabel("Enable Interrupts")
	rswdtInterrupt.setDefaultValue(False)
	rswdtInterrupt.setDependencies(rswdtResetEnable, ["rswdtEnableReset"])
	
	rswdtCounterValue = rswdtComponent.createIntegerSymbol("rswdtWDV", rswdtMenu)
	rswdtCounterValue.setLabel("Counter value")
	rswdtCounterValue.setMax(0xfff)
	rswdtCounterValue.setDefaultValue(0xfff)
	
	rswdtCounterValueTime = rswdtComponent.createIntegerSymbol("rswdtWDVTIME", rswdtMenu)
	rswdtCounterValueTime.setLabel("Counter value in ms")
	rswdtCounterValueTime.setDependencies(rswdtcounter_cal, ["rswdtWDV"])
	rswdtCounterValueTime.setReadOnly(True)
	
	rswdtDebugHalt = rswdtComponent.createBooleanSymbol("rswdtdebugHalt", rswdtMenu)
	print(rswdtDebugHalt)
	rswdtDebugHalt.setLabel("Enable Debug halt")
	rswdtDebugHalt.setDefaultValue(False)
	
	rswdtIndex = rswdtComponent.createIntegerSymbol("INDEX", rswdtMenu)
	rswdtIndex.setVisible(False)
	rswdtIndex.setDefaultValue(int(num))

	rswdtIdleHalt = rswdtComponent.createBooleanSymbol("rswdtidleHalt", rswdtMenu)
	print(rswdtIdleHalt)
	rswdtIdleHalt.setLabel("Enable Idle halt")
	rswdtIdleHalt.setDefaultValue(False)	
	
	configName = Variables.get("__CONFIGURATION_NAME")

	rswdtHeader1File = rswdtComponent.createFileSymbol(None, None)
	rswdtHeader1File.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.h.ftl")
	rswdtHeader1File.setOutputName("plib_rswdt" + str(num) + ".h")
	rswdtHeader1File.setDestPath("peripheral/rswdt/")
	rswdtHeader1File.setProjectPath("config/" + configName + "/peripheral/rswdt/")
	rswdtHeader1File.setType("HEADER")
	rswdtHeader1File.setMarkup(True)
	
	rswdtSource1File = rswdtComponent.createFileSymbol(None, None)
	rswdtSource1File.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.c.ftl")
	rswdtSource1File.setOutputName("plib_rswdt" + str(num) + ".c")
	rswdtSource1File.setDestPath("peripheral/rswdt/")
	rswdtSource1File.setProjectPath("config/" + configName + "/peripheral/rswdt/")
	rswdtSource1File.setType("SOURCE")
	rswdtSource1File.setMarkup(True)
	
	rswdtSystemInitFile = rswdtComponent.createFileSymbol(None, None)
	rswdtSystemInitFile.setType("STRING")
	rswdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
	rswdtSystemInitFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_initialize.h.ftl")
	rswdtSystemInitFile.setMarkup(True)

	rswdtSystemIntFile = rswdtComponent.createFileSymbol(None, None)
	rswdtSystemIntFile.setType("STRING")
	rswdtSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	rswdtSystemIntFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_interrupt.c.ftl")
	rswdtSystemIntFile.setMarkup(True)

	rswdtSystemDefFile = rswdtComponent.createFileSymbol(None, None)
	rswdtSystemDefFile.setType("STRING")
	rswdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rswdtSystemDefFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_definitions.h.ftl")
	rswdtSystemDefFile.setMarkup(True)

def rswdtResetEnable(rswdtInterrupt,test):
	if test.getValue() == True:
		rswdtInterrupt.setVisible(False)
		rswdtInterrupt.setValue("rswdtinterruptMode",False,2)
	else:
		rswdtInterrupt.setVisible(True)

def	rswdtcounter_cal(rswdtCounterValueTime,test):
	data = test.getValue() * 3.90625
	rswdtCounterValueTime.setValue("rswdtWDVTIME",int(round(data)),2)
