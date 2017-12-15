def instantiateComponent(uartComponent):

	num = uartComponent.getID()[-1:]
	print("Running UART" + str(num))

	uartMenu = uartComponent.createMenuSymbol(None, None)
	uartMenu.setLabel("Hardware Settings ")
	
	uartInterrupt = uartComponent.createBooleanSymbol("interruptMode", uartMenu)
	print(uartInterrupt)
	uartInterrupt.setLabel("Enable Interrupts")
	uartInterrupt.setDefaultValue(True)
	
	uartIndex = uartComponent.createIntegerSymbol("INDEX", uartMenu)
	uartIndex.setVisible(False)
	uartIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")

	uartHeader1File = uartComponent.createFileSymbol(None, None)
	uartHeader1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h.ftl")
	uartHeader1File.setOutputName("plib_uart" + str(num) + ".h")
	uartHeader1File.setDestPath("system_config/" + configName +"/peripheral/uart/")
	uartHeader1File.setProjectPath("system_config/" + configName +"/peripheral/uart/")
	uartHeader1File.setType("HEADER")
	
	uartSource1File = uartComponent.createFileSymbol(None, None)
	uartSource1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.c.ftl")
	uartSource1File.setOutputName("plib_uart" + str(num) + ".c")
	uartSource1File.setDestPath("system_config/" + configName +"/peripheral/uart/")
	uartSource1File.setProjectPath("system_config/" + configName +"/peripheral/uart/")
	uartSource1File.setType("SOURCE")

