global debugID

def onDependentComponentAdded(ownerComponent, id, dependencyComponent):
	global debugID
	Name = dependencyComponent.getID()
	dependencyComponent.setSymbolValue("INTERRUPT_MODE", False, 2)
	debugID.setValue(str(Name), 2)

def instantiateComponent(debugComponent):
	global debugID
	
	stdioEnable = debugComponent.createBooleanSymbol("STDIO_ENABLE", None)
	stdioEnable.setVisible(False)
	stdioEnable.setDefaultValue(True)
	
	debugID = debugComponent.createStringSymbol("DEBUG_PERIPHERAL", None)
	debugID.setVisible(False)

	configName = Variables.get("__CONFIGURATION_NAME")
	debugSourceFile = debugComponent.createFileSymbol("DEBUG_CONSOLE_C", None)
	debugSourceFile.setSourcePath("../arch/stdio/templates/xc32_monitor.c.ftl")
	debugSourceFile.setOutputName("xc32_monitor.c")
	debugSourceFile.setMarkup(True)
	debugSourceFile.setOverwrite(True)
	debugSourceFile.setDestPath("/stdio/")
	debugSourceFile.setProjectPath("config/" + configName + "/stdio/")
	debugSourceFile.setType("SOURCE")