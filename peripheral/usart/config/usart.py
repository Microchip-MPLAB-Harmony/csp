def instantiateComponent(usartComponent):

	num = usartComponent.getID()[-1:]
	print("Running USART" + str(num))

	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("Hardware Settings ")

	UsartConfig1 = usartComponent.createBooleanSymbol("Config1", usartMenu)
	print(UsartConfig1)
	UsartConfig1.setLabel("Config 1")

