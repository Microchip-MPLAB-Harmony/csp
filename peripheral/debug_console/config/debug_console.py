global debugID

def onDependentComponentAdded(ownerComponent, id, dependencyComponent):
	global debugID
	Name = dependencyComponent.getID()
	dependencyComponent.setSymbolValue("INTERRUPT_MODE", False, 2)
	debugID.setValue(str(Name), 2)

def instantiateComponent(debugComponent):
	global debugID
	
	debugID = debugComponent.createStringSymbol("DEBUG_PERIPHERAL", None)
	debugID.setVisible(False)

	configName = Variables.get("__CONFIGURATION_NAME")
	debugSourceFile = debugComponent.createFileSymbol("DEBUG_CONSOLE_C", None)
	debugSourceFile.setSourcePath("../peripheral/debug_console/templates/debug_console.c.ftl")
	debugSourceFile.setOutputName("debug_console.c")
	debugSourceFile.setMarkup(True)
	debugSourceFile.setOverwrite(True)
	debugSourceFile.setDestPath("/peripheral/debug/")
	debugSourceFile.setProjectPath("config/" + configName + "/peripheral/debug/")
	debugSourceFile.setType("SOURCE")