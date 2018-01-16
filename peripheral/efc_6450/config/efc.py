#Function for initiating the UI
def instantiateComponent(eefcComponent):

	num = eefcComponent.getID()[-1:]
	print("Running EEFC")
	#Create the top menu
	eefcMenu = eefcComponent.createMenuSymbol(None, None)
	eefcMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	eefcInterrupt = eefcComponent.createBooleanSymbol("eefcEnableInterrupt", eefcMenu)
	print(eefcInterrupt)
	eefcInterrupt.setLabel("Enable Interrupts")
	eefcInterrupt.setDefaultValue(True)
	
	#instance index
	eefcIndex = eefcComponent.createIntegerSymbol("INDEX", eefcMenu)
	eefcIndex.setVisible(False)
	eefcIndex.setDefaultValue(int(num))
	
	configName = Variables.get("__CONFIGURATION_NAME")
	#Generate Output Header
	eefcHeaderFile = eefcComponent.createFileSymbol(None, None)
	eefcHeaderFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.h.ftl")
	eefcHeaderFile.setMarkup(True)
	eefcHeaderFile.setOutputName("plib_eefc" + str(num) + ".h")
	eefcHeaderFile.setOverwrite(True)
	eefcHeaderFile.setDestPath("peripheral/eefc/")
	eefcHeaderFile.setProjectPath("config/" + configName + "/peripheral/eefc/")
	eefcHeaderFile.setType("HEADER")
	#Generate Output source
	eefcSourceFile = eefcComponent.createFileSymbol(None, None)
	eefcSourceFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.c.ftl")
	eefcSourceFile.setMarkup(True)
	eefcSourceFile.setOutputName("plib_eefc" + str(num) + ".c")
	eefcSourceFile.setOverwrite(True)
	eefcSourceFile.setDestPath("peripheral/eefc/")
	eefcSourceFile.setProjectPath("config/" + configName + "/peripheral/eefc/")
	eefcSourceFile.setType("SOURCE")
	
	eefcSystemIntFile = eefcComponent.createFileSymbol(None, None)
	eefcSystemIntFile.setType("STRING")
	eefcSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	eefcSystemIntFile.setSourcePath("../peripheral/efc_6450/templates/system/system_interrupt.c.ftl")
	eefcSystemIntFile.setMarkup(True)

	eefcSystemDefFile = eefcComponent.createFileSymbol(None, None)
	eefcSystemDefFile.setType("STRING")
	eefcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	eefcSystemDefFile.setSourcePath("../peripheral/efc_6450/templates/system/system_definitions.h.ftl")
	eefcSystemDefFile.setMarkup(True)