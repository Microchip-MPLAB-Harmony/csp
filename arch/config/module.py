def loadModule():
	coreComponent = Module.CreateSharedComponent("core", "System", "/", "config/core.py")

	print("Load Module: Device Family Pack (DFP)")

	# supportedProcessors = []
	selectedProcessor = Variables.get("__PROCESSOR")

	#    if selectedProcessor.lower() in supportedProcessors:
	dfpComponent = Module.CreateComponent("dfp", "Device Family Pack (DFP)", "/Packs/", "config/dfp.py")
	#    else:
	#        print("Can't Load PIC32CZ-CA70 DFP: " + selectedProcessor + " is not supported.")

	print("Load Module: CMSIS Pack")
	cmsisComponent = Module.CreateComponent("cmsis", "CMSIS Pack", "/Packs/", "config/cmsis.py")

	#initiate stdio
	stdioComponent = Module.CreateComponent("stdio", "STDIO", "/Tools/", "../arch/stdio/config/stdio.py")
	stdioComponent.addDependency("UART","UART")
	stdioComponent.addDependency("USART","USART")
	
	# load device specific peripherals
	d = dict(locals(), **globals())
	execfile(Module.getPath() + "../../csp/peripheral/config/peripheral.py", d, d)