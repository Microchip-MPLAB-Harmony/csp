#Function for initiating the UI
def instantiateComponent(trngComponent):

	print("Running TRNG")

	trngReserved = trngComponent.createBooleanSymbol("TRNG_Reserved", None)
	trngReserved.setLabel("TRNG Reserved")

	trngWarning = trngComponent.createCommentSymbol("TRNG_COMMENT", None)
	trngWarning.setLabel("**** Warning: This module is used and configured by Crypto Library ****")
	trngWarning.setDependencies(showWarning, ["TRNG_Reserved"])
	trngWarning.setVisible(True)

	#Create the top menu
	trngMenu = trngComponent.createMenuSymbol(None, None)
	trngMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
	print(trngInterrupt)
	trngInterrupt.setLabel("Enable Interrupts")
	trngInterrupt.setDefaultValue(False)
	
	#Generate Output Header
	trngHeaderFile = trngComponent.createFileSymbol(None, None)
	trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
	trngHeaderFile.setOutputName("plib_trng.h")
	trngHeaderFile.setOverwrite(True)
	trngHeaderFile.setDestPath("peripheral/trng/")
	trngHeaderFile.setProjectPath("peripheral/trng/")
	trngHeaderFile.setType("HEADER")
	#Generate Output source
	trngSourceFile = trngComponent.createFileSymbol(None, None)
	trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
	trngSourceFile.setOutputName("plib_trng.c")
	trngSourceFile.setOverwrite(True)
	trngSourceFile.setDestPath("peripheral/trng/")
	trngSourceFile.setProjectPath("peripheral/trng/")
	trngSourceFile.setType("SOURCE")

def showWarning(trngWarning, trngReserved):
	trngWarning.setVisible(trngReserved.getValue())
