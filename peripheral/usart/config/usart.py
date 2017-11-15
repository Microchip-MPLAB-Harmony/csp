def instantiateComponent(usartComponent):
	num = usartComponent.getID()[-1:]

	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("USART " + num)

	useUsart = usartComponent.createBooleanSymbol("USE_USART_" + num, usartMenu)
	useUsart.setLabel("Use USART " + num + "?")
	useUsart.setDescription("Enables usart instance " + num)

