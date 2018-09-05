#Function for initiating the UI
global peripId
global NVICVector
global NVICHandler
global instance 
global NVICHandlerLock

def NVICControl(NVIC, event):
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	Database.clearSymbolValue("core", NVICHandlerLock)
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "TRNG" + str(instance) + "_InterruptHandler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "TRNG_Handler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, False, 2)		
		
def instantiateComponent(trngComponent):
	global NVICVector
	global NVICHandler
	global peripId
	global instance
	global NVICHandlerLock
	peripId = Interrupt.getInterruptIndex("TRNG")
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"
	
	instance = trngComponent.getID()[-1:]
	Log.writeInfoMessage("Running TRNG" + str(instance))

	trngReserved = trngComponent.createBooleanSymbol("TRNG_Reserved", None)
	trngReserved.setLabel("TRNG Reserved")
	trngReserved.setVisible(False)

	trngWarning = trngComponent.createCommentSymbol("TRNG_COMMENT", None)
	trngWarning.setLabel("**** Warning: This module is used and configured by Crypto Library ****")
	trngWarning.setDependencies(showWarning, ["TRNG_Reserved"])
	trngWarning.setVisible(False)
	
	#Create the top menu
	trngMenu = trngComponent.createMenuSymbol("TRNG_MENU_0", None)
	trngMenu.setLabel("Hardware Settings ")
	trngMenu.setDependencies(showMenu, ["TRNG_Reserved"])

	#Create a Checkbox to enable disable interrupts
	trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
	trngInterrupt.setLabel("Enable Interrupts")
	trngInterrupt.setDefaultValue(False)
	
	# Initial settings for CLK and NVIC
	Database.clearSymbolValue("core", "TRNG_CLOCK_ENABLE")
	Database.setSymbolValue("core", "TRNG_CLOCK_ENABLE", True, 2)
	Database.clearSymbolValue("core", NVICVector)
	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.clearSymbolValue("core", NVICHandler)
	Database.setSymbolValue("core", NVICHandler, "TRNG" + str(instance) + "_InterruptHandler", 2)
	Database.clearSymbolValue("core", NVICHandlerLock)
	Database.setSymbolValue("core", NVICHandlerLock, True, 2)

	# NVIC Dynamic settings
	trngNVICControl = trngComponent.createBooleanSymbol("NVIC_TRNG_ENABLE", None)
	trngNVICControl.setDependencies(NVICControl, ["trngEnableInterrupt"])
	trngNVICControl.setVisible(False)
	
	trngIndex = trngComponent.createIntegerSymbol("INDEX", trngMenu)
	trngIndex.setVisible(False)
	trngIndex.setDefaultValue(int(instance))

	configName = Variables.get("__CONFIGURATION_NAME")

	#Generate Output Header
	trngHeaderFile = trngComponent.createFileSymbol("TRNG_FILE_0", None)
	trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
	trngHeaderFile.setMarkup(True)
	trngHeaderFile.setOutputName("plib_trng" + str(instance) + ".h")
	trngHeaderFile.setMarkup(True)
	trngHeaderFile.setOverwrite(True)
	trngHeaderFile.setDestPath("peripheral/trng/")
	trngHeaderFile.setProjectPath("config/" + configName + "/peripheral/trng/")
	trngHeaderFile.setType("HEADER")
	#Generate Output source
	
	trngSourceFile = trngComponent.createFileSymbol("TRNG_FILE_1", None)
	trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
	trngSourceFile.setMarkup(True)
	trngSourceFile.setOutputName("plib_trng" + str(instance) + ".c")
	trngSourceFile.setMarkup(True)
	trngSourceFile.setOverwrite(True)
	trngSourceFile.setDestPath("peripheral/trng/")
	trngSourceFile.setProjectPath("config/" + configName + "/peripheral/trng/")
	trngSourceFile.setType("SOURCE")

	trngSystemDefFile = trngComponent.createFileSymbol("TRNG_FILE_2", None)
	trngSystemDefFile.setType("STRING")
	trngSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	trngSystemDefFile.setSourcePath("../peripheral/trng_6334/templates/system/system_definitions.h.ftl")
	trngSystemDefFile.setMarkup(True)

def showWarning(trngWarning, event):
	trngWarning.setVisible(event["value"])

def showMenu(trngMenu, event):
	trngMenu.setVisible(not event["value"])

def destroyComponent(trngComponent):

	global instance
	global NVICVector
	global NVICHandler
	global NVICHandlerLock

	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.setSymbolValue("core", NVICHandler, "TRNG0_Handler", 2)
	Database.setSymbolValue("core", NVICHandlerLock, False, 2)