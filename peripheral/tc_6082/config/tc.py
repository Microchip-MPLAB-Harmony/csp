def instantiateComponent(tcComponent):
	tcMenu = tcComponent.createMenuSymbol(None, None)
	tcMenu.setLabel("Hardware Settings")
	
	tcConfig1 = tcComponent.createBooleanSymbol("Config1", tcMenu)
	tcConfig1.setLabel("Config 1")
	tcConfig1.setDescription("Set value for Config 1")
