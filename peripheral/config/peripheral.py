if (Peripheral.moduleExists("USART")):
	usartModule = Register.getRegisterModule("USART")
	for usartCount in range(0, Peripheral.getModuleInstanceCount("USART")):
		print("create component: Peripheral USART" + str(usartCount) + " ID = " + usartModule.getID())
		usartComponent = Module.CreateComponent("usart"+str(usartCount), "USART"+str(usartCount), "/Peripherals/USART/", "../peripheral/usart/config/usart.py")
		usartComponent.addCapability("USART")
else:
	print("No USART peripheral")

if (Peripheral.moduleExists("TC")):
	tcModule = Register.getRegisterModule("TC")
	for tcCount in range(0, Peripheral.getModuleInstanceCount("TC")):
		print("create component: Peripheral TC" + str(tcCount) + " ID = " + tcModule.getID())
		tcComponent = Module.CreateComponent("tc"+str(tcCount), "TC"+str(tcCount), "/Peripherals/TC/", "../peripheral/tc/config/tc.py")
		tcComponent.addCapability("TC")
else:
	print("No TC peripheral")


