def instantiateComponent(timerComponent):
	timerMenu = timerComponent.createMenuSymbol(None, None)
	timerMenu.setLabel("Timer Driver")
	
	usetimer = timerComponent.createBooleanSymbol("TIMER_OPTION_FOO", timerMenu)
	usetimer.setLabel("Use Timer Option Foo?")
	usetimer.setDescription("Enables timer driver option foo")