def loadModule():
	coreComponent = Module.CreateSharedComponent("core", "System", "/", "config/core.py")

	# load device specific peripherals
	Module.execfile("../../csp/peripheral/config/peripheral.py")