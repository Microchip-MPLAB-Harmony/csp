# add TC PLib =============================================================
if (Peripheral.moduleExists("TC")):
	tcModule = Register.getRegisterModule("TC")
	for tcCount in range(0, Peripheral.getModuleInstanceCount("TC")):
		print("create component: Peripheral TC" + str(tcCount) + " (ID = " + tcModule.getID() + ")")
		tcComponent = Module.CreateComponent("tc"+str(tcCount), "TC"+str(tcCount), "/Peripherals/TC/", "../peripheral/tc_"+tcModule.getID()+"/config/tc.py")
		tcComponent.addCapability("TC")
else:
	print("No TC peripheral")
# add USART PLib ==========================================================
if (Peripheral.moduleExists("UART")):
	uartModule = Register.getRegisterModule("UART")
	for uartCount in range(0, Peripheral.getModuleInstanceCount("UART")):
		print("create component: Peripheral UART" + str(uartCount) + " (ID = " + uartModule.getID() + ")")
		uartComponent = Module.CreateComponent("uart"+str(uartCount), "UART"+str(uartCount), "/Peripherals/UART/", "../peripheral/uart_"+uartModule.getID()+"/config/uart.py")
		uartComponent.addCapability("USART")
else:
	print("No UART peripheral")
# add USART PLib ==========================================================
if (Peripheral.moduleExists("USART")):
	usartModule = Register.getRegisterModule("USART")
	for usartCount in range(0, Peripheral.getModuleInstanceCount("USART")):
		print("create component: Peripheral USART" + str(usartCount) + " (ID = " + usartModule.getID() + ")")
		usartComponent = Module.CreateComponent("usart"+str(usartCount), "USART"+str(usartCount), "/Peripherals/USART/", "../peripheral/usart_"+usartModule.getID()+"/config/usart.py")
		usartComponent.addCapability("USART")
else:
	print("No USART peripheral")

# add EEFC PLib ==========================================================
if (Peripheral.moduleExists("EFC")):
	eefcModule = Register.getRegisterModule("EFC")
	print("create component: Peripheral EEFC" + " (ID = " + eefcModule.getID() + ")")
	eefcComponent = Module.CreateComponent("EEFC", "EEFC", "/Peripherals/EEFC/", "../peripheral/eefc_" + eefcModule.getID() + "/config/eefc.py")
	eefcComponent.addCapability("EEFC")
else:
	print("No EEFC peripheral")