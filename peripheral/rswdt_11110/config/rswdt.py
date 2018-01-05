def instantiateComponent(rswdtComponent):

	num = rswdtComponent.getID()
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
	rswdtCounterValue.setMax(0x1ff)
	rswdtCounterValue.setDefaultValue(0x1ff)
	
	rswdtCounterValueTime = rswdtComponent.createIntegerSymbol("rswdtWDVTIME", rswdtMenu)
	rswdtCounterValueTime.setLabel("Counter value in ms")
	rswdtCounterValueTime.setDependencies(rswdtcounter_cal, ["rswdtWDV"])
	rswdtCounterValueTime.setReadOnly(True)
	
	rswdtDebugHalt = rswdtComponent.createBooleanSymbol("rswdtdebugHalt", rswdtMenu)
	print(rswdtDebugHalt)
	rswdtDebugHalt.setLabel("Enable Debug halt")
	rswdtDebugHalt.setDefaultValue(False)

	rswdtIdleHalt = rswdtComponent.createBooleanSymbol("rswdtidleHalt", rswdtMenu)
	print(rswdtIdleHalt)
	rswdtIdleHalt.setLabel("Enable Idle halt")
	rswdtIdleHalt.setDefaultValue(False)	
	
	rswdtHeader1File = rswdtComponent.createFileSymbol(None, None)
	rswdtHeader1File.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.h.ftl")
	rswdtHeader1File.setOutputName("plib_rswdt.h")
	rswdtHeader1File.setDestPath("peripheral/rswdt/")
	rswdtHeader1File.setProjectPath("peripheral/rswdt/")
	rswdtHeader1File.setType("HEADER")
	
	rswdtSource1File = rswdtComponent.createFileSymbol(None, None)
	rswdtSource1File.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.c.ftl")
	rswdtSource1File.setOutputName("plib_rswdt.c")
	rswdtSource1File.setDestPath("peripheral/rswdt/")
	rswdtSource1File.setProjectPath("peripheral/rswdt/")
	rswdtSource1File.setType("SOURCE")

def rswdtResetEnable(rswdtInterrupt,test):
	if test.getValue() == True:
		rswdtInterrupt.setVisible(False)
		rswdtInterrupt.setValue("rswdtinterruptMode",False,300)
	else:
		rswdtInterrupt.setVisible(True)

def	rswdtcounter_cal(rswdtCounterValueTime,test):
	data = test.getValue() * 3.90625
	rswdtCounterValueTime.setValue("rswdtWDVTIME",data,300)
