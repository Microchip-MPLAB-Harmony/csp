def loadModule():
	coreComponent = Module.CreateSharedComponent("core", "Core", "/", "config/core.py")
	execfile("../../csp/peripheral/config/peripheral.py")
