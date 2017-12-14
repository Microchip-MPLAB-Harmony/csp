if (Peripheral.moduleExists("USART")):
	for usartCount in range(0, Peripheral.getModuleInstanceCount("USART")):
		print("create component: Peripheral USART" + str(usartCount))
		usartComponent = Module.CreateComponent("usart"+str(usartCount), "USART"+str(usartCount), "/Peripherals/USART/", "../peripheral/usart/config/usart.py")
		usartComponent.addCapability("USART")
else:
	print("No USART peripheral")
	
if (Peripheral.moduleExists("UART")):
	for uartCount in range(0, Peripheral.getModuleInstanceCount("UART")):
		print("create component: Peripheral UART" + str(uartCount))
		uartComponent = Module.CreateComponent("uart"+str(uartCount), "UART"+str(uartCount), "/Peripherals/UART/", "../peripheral/uart/config/uart.py")
		uartComponent.addCapability("USART")
else:
	print("No UART peripheral")

if (Peripheral.moduleExists("TC")):
	for tcCount in range(0, Peripheral.getModuleInstanceCount("TC")):
		print("create component: Peripheral TC" + str(tcCount))
		tcComponent = Module.CreateComponent("tc"+str(tcCount), "TC"+str(tcCount), "/Peripherals/TC/", "../peripheral/tc/config/tc.py")
		tcComponent.addCapability("TC")
else:
	print("No TC peripheral")


