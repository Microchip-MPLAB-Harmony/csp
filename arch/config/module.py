def loadModule():
	print("Core")
	
	coreComponent = Module.CreateSharedComponent("core", "Core", "/", "config/core.py")

	print("create usart component")
	usartComponent = Module.CreateComponent("usart0", "USART 0", "/USART/", "../../peripheral/usart/config/usart.py")
	print(usartComponent)
	print("create tc component")
	tcComponent = Module.CreateComponent("tc0", "TC 0", "/TC/", "../../peripheral/tc/config/tc.py")
	print(tcComponent)

