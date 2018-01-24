import os.path

periphNames = map(str, Register.getRegisterModuleNames())
periphNames.sort()

for periphName in periphNames:
	periphModule =  Register.getRegisterModule(periphName)
	periphInstanceCount = Peripheral.getModuleInstanceCount(periphName)
	periphID = periphModule.getID()
	periphScript = "/peripheral/" + periphName.lower() + "_" + periphID + \
					"/config/" + periphName.lower() + ".py"

	# Don't load system services. They will be loaded by family specific script
	if any(x in periphName for x in ["PORT", "PIO", "NVIC", "XDMAC", "OSCILLATOR", "PMC", "WDT"]):
		print("CSP: System Peripheral [" + periphName + " id=" + periphID + "]")
		continue

	# Check if peripheral has implementation
	if (os.path.isfile(Variables.get("__CSP_DIR") + periphScript)):
		for periphInstance in range(0, periphInstanceCount):
			print("CSP: create component: Peripheral " + periphName + 
					str(periphInstance) + " (ID = " + periphID + ")")
			periphComponent = Module.CreateComponent(periphName.lower() +
							str(periphInstance), periphName.upper() +
							str(periphInstance), "/Peripherals/" +
							periphName.upper() + "/", ".." + periphScript)
			periphComponent.addCapability(periphName)
			if (periphName == "UART"):
				periphComponent.addCapability("USART")
	else:
		print("CSP: Peripheral [" + periphName + " id=" + periphID + 
				"] is not supported in MCC")


