from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading Interrupt Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################
global highestID
highestID = Interrupt.getMaxInterruptID()
global lowestID
lowestID = Interrupt.getMinInterruptID()
global nvicPriorityLevels
nvicPriorityLevels = 0
global nvicPriorityGroup
nvicPriorityGroup = []

atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
try:
    atdfFile = open(atdfFilePath, "r")
except:
    Log.writeInfoMessage("nvic.py peripheral NVIC: Error!!! while opening atdf file")
atdfContent = ElementTree.fromstring(atdfFile.read())
for parameters in atdfContent.iter("parameters"):
    for param in atdfContent.iter("param"):
        name = param.attrib['name']
        if "__NVIC_PRIO_BITS" in name:
            nvicPriorityLevels = (2 ** int(param.attrib['value']))
atdfContent = 0

nvicPriorityGroup = list(range(nvicPriorityLevels))
nvicPriorityGroup = [str(item) for item in nvicPriorityGroup]

global coreVectors
coreVectors = ["Reset", "NonMaskableInt", "HardFault", "MemoryManagement", "BusFault", "UsageFault", "SVCall", "DebugMonitor", "PendSV", "SysTick"]

global coreVectorsEnable

nvicVectorCore = []
nvicVectorCoreFixed = []
nvicVectorEnable = []
nvicVectorNumber = []
nvicVectorName = []
nvicVectorPriority = []
nvicVectorHandler = []
nvicVectorHandlerLock = []

################################################################################
#### Business Logic ####
################################################################################
def coreVectorsEnable(nvicSym, event):
    global coreVectors
    for vector in coreVectors:
        if (event["value"] == str(vector)):
            nvicSym.setReadOnly(True)
            nvicSym.clearValue()
            nvicSym.setValue(True, 2)

def coreVectorsFixed(nvicSym, event):
    global coreVectors
    for vectorIndex in range(0,3):
        if (event["value"] == str(coreVectors[vectorIndex])):
            nvicSym.clearValue()
            nvicSym.setValue(True, 2)

def coreVectorsPriority(nvicSym, event):
    global coreVectors

    for vectorIndex in range(0,3):
        if (event["value"] == str(coreVectors[vectorIndex])):
            nvicSym.setVisible(False)

    for vectorIndex in range(3,10):
        if (event["value"] == str(coreVectors[vectorIndex])):
            nvicSym.clearValue()
            nvicSym.setValue("0", 2)

def checkVectorAvailability(nvicSym, event):
    global coreVectorsEnable

    if (event["value"] == "None"):
        nvicSym.setVisible(False)
    else :
        nvicSym.setVisible(True)

    coreVectorsEnable(nvicSym, event)

################################################################################
#### Component ####
################################################################################
nvicMenu = coreComponent.createMenuSymbol(None, None)
nvicMenu.setLabel("Interrupts (NVIC)")
nvicMenu.setDescription("Configuration for NVIC Initialization")

nvicVectorMax= coreComponent.createIntegerSymbol("NVIC_VECTOR_MAX", nvicMenu)
nvicVectorMax.setLabel("Vector Max Value")
nvicVectorMax.setDefaultValue(highestID)
nvicVectorMax.setVisible(False)

nvicVectorMax= coreComponent.createIntegerSymbol("NVIC_VECTOR_MIN", nvicMenu)
nvicVectorMax.setLabel("Vector Min Value")
nvicVectorMax.setDefaultValue(lowestID)
nvicVectorMax.setVisible(False)

for nvicNumber in range(lowestID, highestID+1):
    index = nvicNumber - lowestID

    nvicVectorNumber.append(index)
    nvicVectorNumber[index]= coreComponent.createIntegerSymbol("NVIC_" + str(nvicNumber), nvicMenu)
    nvicVectorNumber[index].setLabel("Vector Number")
    nvicVectorNumber[index].setDefaultValue(nvicNumber)
    nvicVectorNumber[index].setVisible(False)

    nvicVectorName.append(index)
    nvicVectorName[index]= coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_VECTOR", nvicMenu)
    nvicVectorName[index].setLabel("Vector Name")
    nvicVectorName[index].setVisible(False)
    # Default value is set later to trigger business logic for the first time

    nvicVectorCoreFixed.append(index)
    nvicVectorCoreFixed[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_CORE_FIXED", nvicMenu)
    nvicVectorCoreFixed[index].setDependencies(coreVectorsFixed, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorCoreFixed[index].setDefaultValue(False)
    nvicVectorCoreFixed[index].setVisible(False)

    nvicVectorCore.append(index)
    nvicVectorCore[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_CORE", nvicMenu)
    nvicVectorCore[index].setDependencies(coreVectorsEnable, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorCore[index].setDefaultValue(False)
    nvicVectorCore[index].setVisible(False)

    nvicVectorEnable.append(index)
    nvicVectorEnable[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_ENABLE", nvicMenu)
    nvicVectorEnable[index].setLabel("Enable " + str(Interrupt.getInterruptDescription(nvicNumber)) + " Interrupt")
    nvicVectorEnable[index].setDependencies(checkVectorAvailability, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorEnable[index].setDefaultValue(False)

    nvicVectorPriority.append(index)
    nvicVectorPriority[index] = coreComponent.createComboSymbol("NVIC_" + str(nvicNumber) + "_PRIORITY", nvicVectorEnable[index], nvicPriorityGroup)
    nvicVectorPriority[index].setLabel("Priority")
    nvicVectorPriority[index].setDependencies(coreVectorsPriority, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorPriority[index].setDefaultValue("7")

    nvicVectorHandler.append(index)
    nvicVectorHandler[index] = coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_HANDLER", nvicVectorEnable[index])
    nvicVectorHandler[index].setLabel("Handler")
    nvicVectorHandler[index].setDefaultValue(str(Interrupt.getInterruptName(nvicNumber)) + "_Handler")

    nvicVectorHandlerLock.append(index)
    nvicVectorHandlerLock[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_HANDLER_LOCK", nvicVectorEnable[index])
    nvicVectorHandlerLock[index].setLabel("Handler Lock")
    nvicVectorHandlerLock[index].setVisible(False)
    nvicVectorHandlerLock[index].setDefaultValue(False)

    nvicVectorName[index].setDefaultValue(str(Interrupt.getInterruptName(nvicNumber)))

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

nvicHeaderFile = coreComponent.createFileSymbol(None, None)
nvicHeaderFile.setMarkup(True)
nvicHeaderFile.setSourcePath("../peripheral/nvic_m7/templates/plib_nvic.h.ftl")
nvicHeaderFile.setOutputName("plib_nvic.h")
nvicHeaderFile.setDestPath("/peripheral/nvic/")
nvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicHeaderFile.setType("HEADER")
nvicHeaderFile.setOverwrite(True)

nvicHeaderFile = coreComponent.createFileSymbol(None, None)
nvicHeaderFile.setMarkup(True)
nvicHeaderFile.setSourcePath("../peripheral/nvic_m7/templates/plib_nvic.c.ftl")
nvicHeaderFile.setOutputName("plib_nvic.c")
nvicHeaderFile.setDestPath("/peripheral/nvic/")
nvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicHeaderFile.setType("SOURCE")
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

nvicSystemIntWeakHandleFile = coreComponent.createFileSymbol(None, None)
nvicSystemIntWeakHandleFile.setType("STRING")
nvicSystemIntWeakHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS")
nvicSystemIntWeakHandleFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_interrupt_weak_handlers.h.ftl")
nvicSystemIntWeakHandleFile.setMarkup(True)

nvicSystemIntTableFile = coreComponent.createFileSymbol(None, None)
nvicSystemIntTableFile.setType("STRING")
nvicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
nvicSystemIntTableFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_interrupt_vector_table.h.ftl")
nvicSystemIntTableFile.setMarkup(True)
