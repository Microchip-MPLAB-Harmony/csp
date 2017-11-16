def instantiateComponent(tcComponent):
	tcMenu = tcComponent.createMenuSymbol(None, None)
	tcMenu.setLabel("TC Driver")
	
	usetimer = tcComponent.createBooleanSymbol("TIMER_OPTION_FOO", tcMenu)
	usetimer.setLabel("Use Timer Option Foo?")
	usetimer.setDescription("Enables timer driver option foo")
