import os.path

periphNames = map(str, Register.getRegisterModuleNames())
periphNames.sort()

for periphName in periphNames:
	periphModule =  Register.getRegisterModule(periphName)
	periphInstanceCount = Peripheral.getModuleInstanceCount(periphName)
	periphID = periphModule.getID()
	periphScript = "/peripheral/" + periphName.lower() + "_" + periphID + \
					"/config/" + periphName.lower() + ".py"

	# port/pio is instantiated as part of system service and not part of peripherals
	if (periphName == "PORT" or periphName == "PIO"):
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


