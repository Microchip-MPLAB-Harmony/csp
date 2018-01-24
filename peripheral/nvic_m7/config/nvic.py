print("Loading Interrupt Manager for " + Variables.get("__PROCESSOR"))

global lowestID
lowestID = Interrupt.getMinInterruptID()
global highestID
highestID = Interrupt.getMaxInterruptID()

nvicPriorityGroup = ["0", "1", "2", "3", "4", "5", "6", "7"]

nvicVectorEnable = []
nvicVectorNumber = []
nvicVectorName = []
nvicVectorPriority = []
nvicVectorHandler = []

def checkVectorAvailability(nvicSym, vector):
	if (vector.getValue() == "None"):
		nvicSym.setVisible(False)
	else :
		nvicSym.setVisible(True)

nvicMenu = coreComponent.createMenuSymbol(None, None)
nvicMenu.setLabel("Interrupts (NVIC)")
nvicMenu.setDescription("Configuration for NVIC Initialization")

nvicEnable = coreComponent.createBooleanSymbol("nvicEnable", nvicMenu)
nvicEnable.setLabel("Use NVIC?")
nvicEnable.setDefaultValue(True)
nvicEnable.setReadOnly(True)

for nvicNumber in range(0, highestID+1):

	nvicVectorNumber.append(nvicNumber)
	nvicVectorNumber[nvicNumber]= coreComponent.createIntegerSymbol("NVIC_" + str(nvicNumber), nvicEnable)
	nvicVectorNumber[nvicNumber].setLabel("Vector Number")
	nvicVectorNumber[nvicNumber].setDefaultValue(nvicNumber)
	nvicVectorNumber[nvicNumber].setVisible(False)

	nvicVectorName.append(nvicNumber)
	nvicVectorName[nvicNumber]= coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_VECTOR", nvicEnable)
	nvicVectorName[nvicNumber].setLabel("Vector Name")
	nvicVectorName[nvicNumber].setVisible(False)

	nvicVectorEnable.append(nvicNumber)
	nvicVectorEnable[nvicNumber] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_ENABLE", nvicEnable)
	nvicVectorEnable[nvicNumber].setLabel("Enable " + str(Interrupt.getInterruptName(nvicNumber)) + " Interrupt")
	nvicVectorEnable[nvicNumber].setDependencies(checkVectorAvailability, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
	nvicVectorEnable[nvicNumber].setDefaultValue(False)
	nvicVectorName[nvicNumber].setDefaultValue(str(Interrupt.getInterruptName(nvicNumber)))

	nvicVectorPriority.append(nvicNumber)
	nvicVectorPriority[nvicNumber] = coreComponent.createComboSymbol("NVIC_" + str(nvicNumber) + "_PRIORITY", nvicVectorEnable[nvicNumber], nvicPriorityGroup)
	nvicVectorPriority[nvicNumber].setLabel("Priority")
	nvicVectorPriority[nvicNumber].setDefaultValue("7")

	nvicVectorHandler.append(nvicNumber)
	nvicVectorHandler[nvicNumber] = coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_HANDLER", nvicVectorEnable[nvicNumber])
	nvicVectorHandler[nvicNumber].setLabel("Handler")
	nvicVectorHandler[nvicNumber].setDefaultValue(str(Interrupt.getInterruptName(nvicNumber)) + "_Handler")

configName = Variables.get("__CONFIGURATION_NAME")

nvicHeaderFile = coreComponent.createFileSymbol(None, None)
nvicHeaderFile.setMarkup(True)
nvicHeaderFile.setSourcePath("../peripheral/nvic_m7/templates/plib_nvic.h.ftl")
nvicHeaderFile.setOutputName("plib_nvic.h")
nvicHeaderFile.setDestPath("/peripheral/nvic/")
nvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicHeaderFile.setType("HEADER")
nvicHeaderFile.setOverwrite(True)

nvicSystemInitFile = coreComponent.createFileSymbol(None, None)
nvicSystemInitFile.setType("STRING")
nvicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
nvicSystemInitFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_initialize.h.ftl")
nvicSystemInitFile.setMarkup(True)

nvicSystemDefFile = coreComponent.createFileSymbol(None, None)
nvicSystemDefFile.setType("STRING")
nvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
nvicSystemDefFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_definitions.h.ftl")
nvicSystemDefFile.setMarkup(True)
