import os.path

periphlNames = Register.getRegisterModuleNames()

for periphCount in range(0, Register.getRegisterModuleCount()):
	periphName = str(periphlNames[periphCount])
	periphModule =  Register.getRegisterModule(periphName)
	periphInstanceCount = Peripheral.getModuleInstanceCount(periphName)
	periphName = periphName.lower()
	periphID = periphModule.getID()
	periphScript = Variables.get("__CSP_DIR") + "/peripheral/" + periphName + "_" + periphID + "/config/" + periphName + ".py"

	# port/pio is instantiated as part of system service and not part of peripherals
	if (periphName == "port" or periphName == "pio"):
		print("CSP: System Peripheral [" + periphName + " id=" + periphID + "]")
		continue

	# Check if peripheral has implementation
	if (os.path.isfile(periphScript)):
		for periphInstance in range(0, periphInstanceCount):
			print("CSP: create component: Peripheral " + periphName + str(periphInstance) + " (ID = " + periphID + ")")
			periphComponent = Module.CreateComponent(periphName+str(periphInstance), periphName.upper()+str(periphInstance), "/Peripherals/"+periphName.upper()+"/", "../peripheral/"+periphName+"_"+periphID+"/config/"+periphName+".py")

			if (periphName == "uart"):
				periphComponent.addCapability("USART")
			else:
				periphComponent.addCapability(periphName.upper())

	else:
		print("CSP: Peripheral [" + periphName + " id=" + periphID + "] is not supported in MCC")


