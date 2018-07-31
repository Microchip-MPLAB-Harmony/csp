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

