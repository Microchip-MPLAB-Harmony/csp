#Function for initiating the UI
def instantiateComponent(trngComponent):

	num = trngComponent.getID()[-1:]
	print("Running TRNG" + str(num))

	trngReserved = trngComponent.createBooleanSymbol("TRNG_Reserved", None)
	trngReserved.setLabel("TRNG Reserved")
	trngReserved.setVisible(False)

	trngWarning = trngComponent.createCommentSymbol("TRNG_COMMENT", None)
	trngWarning.setLabel("**** Warning: This module is used and configured by Crypto Library ****")
	trngWarning.setDependencies(showWarning, ["TRNG_Reserved"])
	trngWarning.setVisible(False)
	
	#Create the top menu
	trngMenu = trngComponent.createMenuSymbol(None, None)
	trngMenu.setLabel("Hardware Settings ")
	trngMenu.setDependencies(showMenu, ["TRNG_Reserved"])

	#Create a Checkbox to enable disable interrupts
	trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
	print(trngInterrupt)
	trngInterrupt.setLabel("Enable Interrupts")
	trngInterrupt.setDefaultValue(False)
	
	trngIndex = trngComponent.createIntegerSymbol("INDEX", trngMenu)
	trngIndex.setVisible(False)
	trngIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")

	#Generate Output Header
	trngHeaderFile = trngComponent.createFileSymbol(None, None)
	trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
	trngHeaderFile.setMarkup(True)
	trngHeaderFile.setOutputName("plib_trng" + str(num) + ".h")
	trngHeaderFile.setMarkup(True)
	trngHeaderFile.setOverwrite(True)
	trngHeaderFile.setDestPath("peripheral/trng/")
	trngHeaderFile.setProjectPath("config/" + configName + "/peripheral/trng/")
	trngHeaderFile.setType("HEADER")
	#Generate Output source
	
	trngSourceFile = trngComponent.createFileSymbol(None, None)
	trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
	trngSourceFile.setMarkup(True)
	trngSourceFile.setOutputName("plib_trng" + str(num) + ".c")
	trngSourceFile.setMarkup(True)
	trngSourceFile.setOverwrite(True)
	trngSourceFile.setDestPath("peripheral/trng/")
	trngSourceFile.setProjectPath("config/" + configName + "/peripheral/trng/")
	trngSourceFile.setType("SOURCE")
	
	trngSystemIntFile = trngComponent.createFileSymbol(None, None)
	trngSystemIntFile.setType("STRING")
	trngSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	trngSystemIntFile.setSourcePath("../peripheral/trng_6334/templates/system/system_interrupt.c.ftl")
	trngSystemIntFile.setMarkup(True)

	trngSystemDefFile = trngComponent.createFileSymbol(None, None)
	trngSystemDefFile.setType("STRING")
	trngSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	trngSystemDefFile.setSourcePath("../peripheral/trng_6334/templates/system/system_definitions.h.ftl")
	trngSystemDefFile.setMarkup(True)

def showWarning(trngWarning, event):
	trngWarning.setVisible(event["value"])

def showMenu(trngMenu, event):
	trngMenu.setVisible(not event["value"])
