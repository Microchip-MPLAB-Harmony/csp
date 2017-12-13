def loadModule():
	coreComponent = Module.CreateSharedComponent("core", "System", "/", "config/core.py")
	execfile("../../csp/peripheral/config/peripheral.py")
