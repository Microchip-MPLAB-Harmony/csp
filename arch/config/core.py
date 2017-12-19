def instantiateComponent(coreComponent):
	
	# load device specific information, clock and pin manager
	execfile(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")

	
