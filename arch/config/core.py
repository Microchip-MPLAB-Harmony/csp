def instantiateComponent(coreComponent):
	print(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")
	
	# exec part specific script
	execfile(Variables.get("__ARCH_DIR") + "/" + Variables.get("__PROCESSOR") + ".py")