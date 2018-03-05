#Function for initiating the UI

global instance
global peripId
global NVICVector
global NVICHandler

def NVICControl(NVIC, event):
	global NVICVector
	global NVICHandler
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_InterruptHandler", 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_Handler", 2)
		
def instantiateComponent(efcComponent):

	global instance
	global peripId
	global NVICVector
	global NVICHandler
	instance = efcComponent.getID()[-1:]
	Log.writeInfoMessage("Running EEFC")
	#Create the top menu
	eefcMenu = efcComponent.createMenuSymbol(None, None)
	eefcMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	eefcInterrupt = efcComponent.createBooleanSymbol("eefcEnableInterrupt", eefcMenu)
	eefcInterrupt.setLabel("Enable Interrupts")
	eefcInterrupt.setDefaultValue(True)
	
	#instance index
	eefcIndex = efcComponent.createIntegerSymbol("INDEX", eefcMenu)
	eefcIndex.setVisible(False)
	eefcIndex.setDefaultValue(int(instance))

	peripId = Interrupt.getInterruptIndex("EFC")
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

	Database.clearSymbolValue("core", NVICVector)
	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.clearSymbolValue("core", NVICHandler)
	Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_InterruptHandler", 2)
	Database.clearSymbolValue("core", NVICHandlerLock)
	Database.setSymbolValue("core", NVICHandlerLock, True, 2)

	# NVIC Dynamic settings
	efcNVICControl = efcComponent.createBooleanSymbol("NVIC_EFC_ENABLE", None)
	efcNVICControl.setDependencies(NVICControl, ["eefcEnableInterrupt"])
	efcNVICControl.setVisible(False)
	
	configName = Variables.get("__CONFIGURATION_NAME")
	#Generate Output Header
	eefcHeaderFile = efcComponent.createFileSymbol(None, None)
	eefcHeaderFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.h.ftl")
	eefcHeaderFile.setMarkup(True)
	eefcHeaderFile.setOutputName("plib_eefc" + str(instance) + ".h")
	eefcHeaderFile.setOverwrite(True)
	eefcHeaderFile.setDestPath("peripheral/eefc/")
	eefcHeaderFile.setProjectPath("config/" + configName + "/peripheral/eefc/")
	eefcHeaderFile.setType("HEADER")
	#Generate Output source
	eefcSourceFile = efcComponent.createFileSymbol(None, None)
	eefcSourceFile.setSourcePath("../peripheral/efc_6450/templates/plib_eefc.c.ftl")
	eefcSourceFile.setMarkup(True)
	eefcSourceFile.setOutputName("plib_eefc" + str(instance) + ".c")
	eefcSourceFile.setOverwrite(True)
	eefcSourceFile.setDestPath("peripheral/eefc/")
	eefcSourceFile.setProjectPath("config/" + configName + "/peripheral/eefc/")
	eefcSourceFile.setType("SOURCE")

	eefcSystemDefFile = efcComponent.createFileSymbol(None, None)
	eefcSystemDefFile.setType("STRING")
	eefcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	eefcSystemDefFile.setSourcePath("../peripheral/efc_6450/templates/system/system_definitions.h.ftl")
	eefcSystemDefFile.setMarkup(True)