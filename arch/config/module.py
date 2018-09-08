def loadModule():

	print("Load Module: Device Family Pack (DFP)")
	dfpComponent = Module.CreateComponent("dfp", "Device Family Pack (DFP)", "/Packs/", "config/dfp.py")

	print("Load Module: CMSIS Pack")
	cmsisComponent = Module.CreateComponent("cmsis", "CMSIS Pack", "/Packs/", "config/cmsis.py")

	print("Load Module: CSP System")
	coreComponent = Module.CreateSharedComponent("core", "System", "/", "config/core.py")

	#initiate stdio
	stdioComponent = Module.CreateComponent("stdio", "STDIO", "/Tools/", "../arch/stdio/config/stdio.py")
	stdioComponent.addDependency("UART","UART",False,True)
	
	# load device specific peripherals
	d = dict(locals(), **globals())
	execfile(Module.getPath() + "../../csp/peripheral/config/peripheral.py", d, d)
