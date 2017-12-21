#Function for initiating the UI
def instantiateComponent(trngComponent):

	print("Running TRNG")
	#Create the top menu
	trngMenu = trngComponent.createMenuSymbol(None, None)
	trngMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
	print(trngInterrupt)
	trngInterrupt.setLabel("Enable Interrupts")
	trngInterrupt.setDefaultValue(False)
	
	configName = Variables.get("__CONFIGURATION_NAME")
	#Generate Output Header
	trngHeaderFile = trngComponent.createFileSymbol(None, None)
	trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
	trngHeaderFile.setOutputName("plib_trng.h")
	trngHeaderFile.setOverwrite(True)
	trngHeaderFile.setDestPath("system_config/" + configName +"/peripheral/trng/")
	trngHeaderFile.setProjectPath("system_config/" + configName +"/peripheral/trng/")
	trngHeaderFile.setType("HEADER")
	#Generate Output source
	trngSourceFile = trngComponent.createFileSymbol(None, None)
	trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
	trngSourceFile.setOutputName("plib_trng.c")
	trngSourceFile.setOverwrite(True)
	trngSourceFile.setDestPath("system_config/" + configName +"/peripheral/trng/")
	trngSourceFile.setProjectPath("system_config/" + configName +"/peripheral/trng/")
	trngSourceFile.setType("SOURCE")

