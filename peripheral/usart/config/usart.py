def instantiateComponent(usartComponent):

	num = usartComponent.getID()[-1:]
	print("Running USART" + str(num))

	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("Hardware Settings ")

	usartConfig1 = usartComponent.createBooleanSymbol("Config1", usartMenu)
	print(usartConfig1)
	usartConfig1.setLabel("Config 1")

	usartIndex = usartComponent.createIntegerSymbol("INDEX", usartMenu)
	usartIndex.setVisible(False)
	usartIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")

	usartSource1File = usartComponent.createFileSymbol(None, None)
	usartSource1File.setSourcePath("../peripheral/usart/templates/usart.c.ftl")
	usartSource1File.setOutputName("usart" + str(num) + ".c")
	usartSource1File.setDestPath("system_config/" + configName +"/")
	usartSource1File.setProjectPath("system_config/" + configName +"/")
	usartSource1File.setType("SOURCE")

