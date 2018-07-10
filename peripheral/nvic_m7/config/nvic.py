from os.path import join
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
global vector

node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__NVIC_PRIO_BITS\"]")
priority_bits = node.getAttribute("value")
nvicPriorityLevels = (2 ** int(priority_bits))

nvicPriorityGroup = list(range(nvicPriorityLevels))
nvicPriorityGroup = [str(item) for item in nvicPriorityGroup]

global vectorSettings
                   #Entry          : [
                                    #Enable value,
                                             #Enable Lock,
                                                      #Enable Generate,
                                                                #Initial Priority value,
                                                                         #Priority Lock,
                                                                                  #Priority Generate,
                                                                                            #Handler Lock]
vectorSettings = {"Reset"         : [True,   True,    False,    "-3",    True,    False,    True],
                "NonMaskableInt"  : [True,   True,    False,    "-2",    True,    False,    True],
                "HardFault"       : [True,   True,    False,    "-1",    True,    False,    True],
                "MemoryManagement": [True,   True,    False,    "0",     False,   True,     True],
                "BusFault"        : [True,   False,   False,    "0",     False,   True,     True],
                "UsageFault"      : [True,   False,   False,    "0",     False,   True,     True],
                "SVCall"          : [False,  True,    False,    "0",     False,   True,     True],
                "DebugMonitor"    : [True,   True,    False,    "0",     False,   True,     True],
                "PendSV"          : [False,  True,    False,    "0",     False,   True,     True],
                "SysTick"         : [False,  True,    False,    "0",     False,   True,     True],
                "Peripheral"      : [False,  False,   True,     "7",     False,   True,     False]}

nvicVectorNumber = []
nvicVectorName = []
nvicVectorEnable = []
nvicVectorEnableLock = []
nvicVectorEnableGenerate = []
nvicVectorPriority = []
nvicVectorPriorityLock = []
nvicVectorPriorityGenerate = []
nvicVectorHandler = []
nvicVectorHandlerLock = []

################################################################################
#### Business Logic ####
################################################################################
def getInterruptName(index):
    node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
    interrupts = node.getChildren()
    for interrupt in range (0 , len(interrupts)):
        if "index" in interrupts[interrupt].getAttributeList():
            if str(index) == interrupts[interrupt].getAttribute("index"):
                if "header:alternate-name" in interrupts[interrupt].getAttributeList():
                    return interrupts[interrupt].getAttribute("header:alternate-name")
                else:
                    return interrupts[interrupt].getAttribute("name")

def getInterruptDescription(index):
    node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
    interrupts = node.getChildren()
    for interrupt in range (0 , len(interrupts)):
        if "index" in interrupts[interrupt].getAttributeList():
            if str(index) == interrupts[interrupt].getAttribute("index"):
                if "header:alternate-caption" in interrupts[interrupt].getAttributeList():
                    return interrupts[interrupt].getAttribute("header:alternate-caption")
                else:
                    return interrupts[interrupt].getAttribute("caption")

def configureVectorSettings(nvicSym, event):
    global vectorSettings
    global vector
    settingsIndex = 0

    symId = nvicSym.getID()
    symId = ''.join([i for i in symId if not i.isdigit()])
    # Following operation is needed for negative vectors
    symId = symId.replace("-", "")

    nvicSym.clearValue()

    if symId == "NVIC__ENABLE":
        settingsIndex = 0
        if (event["value"] == "None"):
            nvicSym.setVisible(False)
    elif symId == "NVIC__ENABLE_LOCK":
        settingsIndex = 1
    elif symId == "NVIC__ENABLE_GENERATE":
        settingsIndex = 2
    elif symId == "NVIC__PRIORITY":
        settingsIndex = 3
    elif symId == "NVIC__PRIORITY_LOCK":
        settingsIndex = 4
    elif symId == "NVIC__PRIORITY_GENERATE":
        settingsIndex = 5
    elif symId == "NVIC__HANDLER_LOCK":
        settingsIndex = 6

    nvicSym.setValue(vectorSettings[vector][settingsIndex], 2)

################################################################################
#### Component ####
################################################################################
nvicMenu = coreComponent.createMenuSymbol("NVIC_MENU", cortexMenu)
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

node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
interrupts = node.getChildren()

global interrupt_index
interrupt_index = {}

for i in range(0,len(interrupts)):
    global interrupt_index
    interrupt_index[int(i)] = interrupts[i].getAttribute("index")

for index in interrupt_index:
    nvicNumber = int(interrupt_index.get(index))
    nvicVectorNumber.append(index)
    nvicVectorNumber[index]= coreComponent.createIntegerSymbol("NVIC_" + str(nvicNumber), nvicMenu)
    nvicVectorNumber[index].setLabel("Vector Number")
    nvicVectorNumber[index].setDefaultValue(nvicNumber)
    nvicVectorNumber[index].setVisible(False)

    nvicVectorName.append(index)
    nvicVectorName[index]= coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_VECTOR", nvicMenu)
    nvicVectorName[index].setLabel("Vector Name")
    nvicVectorName[index].setVisible(False)
    vector = str(getInterruptName(nvicNumber))
    # Default value is set later to trigger business logic for the first time

    nvicVectorEnable.append(index)
    nvicVectorEnable[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_ENABLE", nvicMenu)
    nvicVectorEnable[index].setLabel("Enable " + str(getInterruptDescription(nvicNumber)) + " Interrupt")
    nvicVectorEnable[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorEnable[index].setDefaultValue(False)

    nvicVectorEnableLock.append(index)
    nvicVectorEnableLock[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_ENABLE_LOCK", nvicVectorEnable[index])
    nvicVectorEnableLock[index].setLabel("Enable Lock")
    nvicVectorEnableLock[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorEnableLock[index].setDefaultValue(False)
    nvicVectorEnableLock[index].setVisible(False)

    nvicVectorEnableGenerate.append(index)
    nvicVectorEnableGenerate[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_ENABLE_GENERATE", nvicVectorEnable[index])
    nvicVectorEnableGenerate[index].setLabel("Enable Generate")
    nvicVectorEnableGenerate[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorEnableGenerate[index].setDefaultValue(False)
    nvicVectorEnableGenerate[index].setVisible(False)

    nvicVectorPriority.append(index)
    nvicVectorPriority[index] = coreComponent.createComboSymbol("NVIC_" + str(nvicNumber) + "_PRIORITY", nvicVectorEnable[index], nvicPriorityGroup)
    nvicVectorPriority[index].setLabel("Priority")
    nvicVectorPriority[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorPriority[index].setDefaultValue("0")

    nvicVectorPriorityLock.append(index)
    nvicVectorPriorityLock[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_PRIORITY_LOCK", nvicVectorEnable[index])
    nvicVectorPriorityLock[index].setLabel("Priority Lock")
    nvicVectorPriorityLock[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorPriorityLock[index].setDefaultValue(False)
    nvicVectorPriorityLock[index].setVisible(False)

    nvicVectorPriorityGenerate.append(index)
    nvicVectorPriorityGenerate[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_PRIORITY_GENERATE", nvicVectorEnable[index])
    nvicVectorPriorityGenerate[index].setLabel("Priority Generate")
    nvicVectorPriorityGenerate[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorPriorityGenerate[index].setDefaultValue(False)
    nvicVectorPriorityGenerate[index].setVisible(False)

    nvicVectorHandler.append(index)
    nvicVectorHandler[index] = coreComponent.createStringSymbol("NVIC_" + str(nvicNumber) + "_HANDLER", nvicVectorEnable[index])
    nvicVectorHandler[index].setLabel("Handler")
    nvicVectorHandler[index].setDefaultValue(vector + "_Handler")

    nvicVectorHandlerLock.append(index)
    nvicVectorHandlerLock[index] = coreComponent.createBooleanSymbol("NVIC_" + str(nvicNumber) + "_HANDLER_LOCK", nvicVectorEnable[index])
    nvicVectorHandlerLock[index].setLabel("Handler Lock")
    nvicVectorHandlerLock[index].setDependencies(configureVectorSettings, ["NVIC_" + str(nvicNumber) + "_VECTOR"])
    nvicVectorHandlerLock[index].setDefaultValue(False)
    nvicVectorHandlerLock[index].setVisible(False)

    if vector not in vectorSettings:
        vector = "Peripheral"

    nvicVectorName[index].setDefaultValue(str(getInterruptName(nvicNumber)))

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

nvicHeaderFile = coreComponent.createFileSymbol("NVIC_HEADER", None)
nvicHeaderFile.setMarkup(True)
nvicHeaderFile.setSourcePath("../peripheral/nvic_m7/templates/plib_nvic.h.ftl")
nvicHeaderFile.setOutputName("plib_nvic.h")
nvicHeaderFile.setDestPath("/peripheral/nvic/")
nvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicHeaderFile.setType("HEADER")
nvicHeaderFile.setOverwrite(True)

nvicSourceFile = coreComponent.createFileSymbol("NVIC_SOURCE", None)
nvicSourceFile.setMarkup(True)
nvicSourceFile.setSourcePath("../peripheral/nvic_m7/templates/plib_nvic.c.ftl")
nvicSourceFile.setOutputName("plib_nvic.c")
nvicSourceFile.setDestPath("/peripheral/nvic/")
nvicSourceFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicSourceFile.setType("SOURCE")
nvicSourceFile.setOverwrite(True)

nvicSystemInitFile = coreComponent.createFileSymbol("NVIC_INIT", None)
nvicSystemInitFile.setType("STRING")
nvicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
nvicSystemInitFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_initialize.c.ftl")
nvicSystemInitFile.setMarkup(True)

nvicSystemDefFile = coreComponent.createFileSymbol("NVIC_DEF", None)
nvicSystemDefFile.setType("STRING")
nvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
nvicSystemDefFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_definitions.h.ftl")
nvicSystemDefFile.setMarkup(True)

nvicSystemIntWeakHandleFile = coreComponent.createFileSymbol("NVIC_INT_HANDLER", None)
nvicSystemIntWeakHandleFile.setType("STRING")
nvicSystemIntWeakHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS")
nvicSystemIntWeakHandleFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_interrupt_weak_handlers.h.ftl")
nvicSystemIntWeakHandleFile.setMarkup(True)

nvicSystemIntTableFile = coreComponent.createFileSymbol("NVIC_INT_TABLE", None)
nvicSystemIntTableFile.setType("STRING")
nvicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
nvicSystemIntTableFile.setSourcePath("../peripheral/nvic_m7/templates/system/system_interrupt_vector_table.h.ftl")
nvicSystemIntTableFile.setMarkup(True)
