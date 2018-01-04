#Function for initiating the UI
def instantiateComponent(eefcComponent):

	print("Running EEFC")
	#Create the top menu
	eefcMenu = eefcComponent.createMenuSymbol(None, None)
	eefcMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	eefcInterrupt = eefcComponent.createBooleanSymbol("eefcEnableInterrupt", eefcMenu)
	print(eefcInterrupt)
	eefcInterrupt.setLabel("Enable Interrupts")
	eefcInterrupt.setDefaultValue(True)
	
	#Generate Output Header
	eefcHeaderFile = eefcComponent.createFileSymbol(None, None)
	eefcHeaderFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.h.ftl")
	eefcHeaderFile.setOutputName("plib_eefc.h")
	eefcHeaderFile.setOverwrite(True)
	eefcHeaderFile.setDestPath("peripheral/eefc/")
	eefcHeaderFile.setProjectPath("peripheral/eefc/")
	eefcHeaderFile.setType("HEADER")
	#Generate Output source
	eefcSourceFile = eefcComponent.createFileSymbol(None, None)
	eefcSourceFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.c.ftl")
	eefcSourceFile.setOutputName("plib_eefc.c")
	eefcSourceFile.setOverwrite(True)
	eefcSourceFile.setDestPath("peripheral/eefc/")
	eefcSourceFile.setProjectPath("peripheral/eefc/")
	eefcSourceFile.setType("SOURCE")

