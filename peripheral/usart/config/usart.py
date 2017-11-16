def instantiateComponent(usartComponent):

	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("USART ")

	useUsart = usartComponent.createBooleanSymbol("USE_USART_", usartMenu)
	useUsart.setLabel("Use USART ")

