from os.path import join

Log.writeInfoMessage("Loading Interrupt Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################

global maxPriority
global minPriority
global maxSubPriority
global minSubPriority
global intPriorityLevels
intPriorityLevels = 0

global intPriorityGroup
intPriorityGroup = []

if( "PIC32M" in Variables.get("__PROCESSOR")):
    node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_PRIO_LEVELS\"]")
    intPriorityLevels = int(node.getAttribute("value"))
    node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_SUBPRIO_LEVELS\"]")
    intSubPriorityLevels = int(node.getAttribute("value"))
    node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_NUM_SHADOW_SETS\"]")
    intNumShadowRegSets = int(node.getAttribute("value"))

intPriorityGroup = list(range(intPriorityLevels+1))  # 0 to number of levels possible values
maxPriority = max(intPriorityGroup)
minPriority = min(intPriorityGroup)
intPriorityGroup = [str(item) for item in intPriorityGroup]

intSubPriorityGroup = list(range(intSubPriorityLevels))
maxSubPriority = max(intSubPriorityGroup)
minSubPriority = min(intSubPriorityGroup)
intSubPriorityGroup = [str(item) for item in intSubPriorityGroup]


global vectorSettings

global intVectorDataDictionary
intVectorDataDictionary = {}

global interruptsChildrenList
interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

################################################################################
#### Business Logic ####
################################################################################

def generateIntVectorDataDictionary():

    for interrupt in range (0, len(interruptsChildrenList)):

        vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
        
        # Not all entries have a module-instance field
        vModuleInstance = ''
        if "module-instance" in interruptsChildrenList[interrupt].getAttributeList():
            vModuleInstance = str(interruptsChildrenList[interrupt].getAttribute("module-instance"))

        if "header:alternate-name" in interruptsChildrenList[interrupt].getAttributeList():
            vName = str(interruptsChildrenList[interrupt].getAttribute("header:alternate-name"))
        else:
            vName = str(interruptsChildrenList[interrupt].getAttribute("name"))

        if " " in vModuleInstance:
            intVectorDataDictionary[vIndex] = list(vModuleInstance.split(" "))
        else:
            intVectorDataDictionary[vIndex] = [vName]

def getInterruptDescription(vIndex, periName):
    for interrupt in range (0, len(interruptsChildrenList)):
        if vIndex == int(interruptsChildrenList[interrupt].getAttribute("index")):
            if "header:alternate-caption" in interruptsChildrenList[interrupt].getAttributeList():
                if str(interruptsChildrenList[interrupt].getAttribute("header:alternate-caption")) == "None":
                    return periName
                else:
                    return str(interruptsChildrenList[interrupt].getAttribute("header:alternate-caption"))
            else:
                if str(interruptsChildrenList[interrupt].getAttribute("caption")) == "None":
                    return periName
                else:
                    return str(interruptsChildrenList[interrupt].getAttribute("caption"))
    return periName

def updateIntVectorPrioValue(symbol, event):
    symbol.clearValue()
    if event["value"] == False:
        symbol.setValue(str(minPriority), 1)
    else:
        symbol.setValue(str(maxPriority), 1)

def updateIntVectorSubPrioValue(symbol, event):
    #symObj=event["symbol"]
    symbol.clearValue()
    if event["value"] == False:
        symbol.setValue(str(minSubPriority), 1)
    else:
        symbol.setValue(str(maxSubPriority), 1)


def updateIntVectorParametersValue(symbol, event):
    symbol.clearValue()
    symbol.setValue(event["value"], 2)

def updateIntHandlerParametersValue(symbol, event):
    symbol.clearValue()
    symbol.setValue(event["value"], 2)
    
################################################################################
#### Component ####
################################################################################

generateIntVectorDataDictionary()

highestID = int(max(intVectorDataDictionary))
lowestID = int(min(intVectorDataDictionary))

max_key, max_value = max(intVectorDataDictionary.items(), key = lambda x: len(set(x[1])))

intMenu = coreComponent.createMenuSymbol("INT_MENU", None)
intMenu.setLabel("PIC32MZ Interrupts")
intMenu.setDescription("Configuration for PIC32MZ Initialization")

intVectorMax = coreComponent.createIntegerSymbol("INT_VECTOR_MAX", intMenu)
intVectorMax.setDefaultValue(highestID)
intVectorMax.setVisible(False)

intVectorMin = coreComponent.createIntegerSymbol("INT_VECTOR_MIN", intMenu)
intVectorMin.setDefaultValue(lowestID)
intVectorMin.setVisible(False)

index = 0
priorityList = intPriorityGroup
subPriorityList = intSubPriorityGroup
handlerList = []

for vIndex in sorted(intVectorDataDictionary):
    name = (intVectorDataDictionary.get(vIndex))
    vName = name[0] # 1-element list converted to string to avoid errors below
    
    vDescription = str(getInterruptDescription(vIndex, vName))
    vector = vName
    #Vector symbol name:  xc32 toolchain expects underscore as leading character for the vector symbol name
    interruptName = coreComponent.createStringSymbol(vName + "_VECTOR", intMenu)
    interruptName.setDefaultValue("_" + vName + "_VECTOR")
    interruptName.setVisible(False)

    intVectorEnable = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_0_ENABLE", intMenu)
    intVectorEnable.setLabel("Enable " + vDescription + " Interrupt")
    intVectorEnable.setDefaultValue(False)
    intVectorEnable.setDependencies(updateIntVectorParametersValue, ["NVIC_" + str(vIndex) + "_0_ENABLE"])
    
    intVectorPriority = coreComponent.createComboSymbol("NVIC_" + str(vIndex) + "_0_PRIORITY", intVectorEnable, priorityList)
    intVectorPriority.setLabel("Priority")
    intVectorPriority.setDefaultValue("0")
    intVectorPriority.setDependencies(updateIntVectorPrioValue,["NVIC_" + str(vIndex) + "_0_ENABLE"])
    
    intVectorSubPriority = coreComponent.createComboSymbol(vName + "_SUBPRIORITY", intVectorEnable, subPriorityList)
    intVectorSubPriority.setLabel("Subpriority")
    intVectorSubPriority.setDefaultValue("0")
    intVectorSubPriority.setDependencies(updateIntVectorSubPrioValue,["NVIC_" + str(vIndex) + "_0_ENABLE"])    
    
    intVectorHandler = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_0_HANDLER", intVectorEnable)
    intVectorHandler.setLabel("Handler")
    intVectorHandler.setDefaultValue(vName + "_Handler")
    intVectorHandler.setDependencies(updateIntHandlerParametersValue, ["NVIC_" + str(vIndex) + "_0_HANDLER"])

    # Handler locks - not needed for MIPS.
    
    # Enable locks - not needed for MIPS.
    
    # only for use by the interrupt ftl code
    symbol = coreComponent.createStringSymbol("INT_FIRST_NAME_KEY_" + str(vIndex), intVectorEnable )
    symbol.setDefaultValue( str(vIndex) )
    symbol.setVisible( False )
    
    # only for use by the interrupt ftl code - cross-reference name with index number
    symbol = coreComponent.createStringSymbol("INT_FIRST_NAME_STRING_" + str(vIndex), intVectorEnable )
    symbol.setDefaultValue( vName )
    symbol.setVisible( False )
    
    # Below is for interrupt manager support only
    symbol = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_0_HANDLER_LOCK", intVectorEnable)
    symbol.setDefaultValue(False)
    symbol.setVisible(False)

    symbol = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_0_ENABLE_LOCK", intVectorEnable)
    symbol.setDefaultValue(False)
    symbol.setVisible(False)
    
    symbol = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_0_PRIORITY_LOCK", intVectorEnable)
    symbol.setDefaultValue(False)
    symbol.setVisible(False)
    
    symbol = coreComponent.createIntegerSymbol("NVIC_" + str(vIndex) + "_0_NUMBER", intVectorEnable)
    symbol.setDefaultValue(vIndex)
    symbol.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################


configName = Variables.get("__CONFIGURATION_NAME")

intSystemDefFile = coreComponent.createFileSymbol("INT_DEF", None)
intSystemDefFile.setType("STRING")
intSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
intSystemDefFile.setSourcePath("../peripheral/evic_02907/templates/system/definitions.h.ftl")
intSystemDefFile.setMarkup(True)

intSystemInitFile = coreComponent.createFileSymbol("INT_INIT", None)
intSystemInitFile.setType("STRING")
intSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
intSystemInitFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization.c.ftl")
intSystemInitFile.setMarkup(True)

intSystemInitStartFile = coreComponent.createFileSymbol("INT_INIT_START", None)
intSystemInitStartFile.setType("STRING")
intSystemInitStartFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
intSystemInitStartFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization_mips_start.c.ftl")
intSystemInitStartFile.setMarkup(True)

intSystemInitEndFile = coreComponent.createFileSymbol("INT_INIT_END", None)
intSystemInitEndFile.setType("STRING")
intSystemInitEndFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_END")
intSystemInitEndFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization_mips_end.c.ftl")
intSystemInitEndFile.setMarkup(True)

intSourceFile = coreComponent.createFileSymbol("INT_SOURCE", None)
intSourceFile.setType("SOURCE")
intSourceFile.setSourcePath("../peripheral/evic_02907/templates/plib_int.c.ftl")
intSourceFile.setOutputName("plib_int.c")
intSourceFile.setDestPath("/peripheral/evic_02907/")
intSourceFile.setProjectPath("config/" + configName + "/peripheral/evic_02907/")
intSourceFile.setMarkup(True)
intSourceFile.setOverwrite(True)

intHeaderFile = coreComponent.createFileSymbol("INT_HEADER", None)
intHeaderFile.setType("HEADER")
intHeaderFile.setSourcePath("../peripheral/evic_02907/templates/plib_int.h.ftl")
intHeaderFile.setOutputName("plib_int.h")
intHeaderFile.setDestPath("/peripheral/evic_02907/")
intHeaderFile.setProjectPath("config/" + configName + "/peripheral/evic_02907/")
intHeaderFile.setMarkup(True)
intHeaderFile.setOverwrite(True)

intSystemIntTableFile = coreComponent.createFileSymbol("NVIC_INT_TABLE", None)
intSystemIntTableFile.setType("STRING")
intSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
intSystemIntTableFile.setDestPath("/peripheral/evic_02907/")
intSystemIntTableFile.setProjectPath("config/" + configName + "/peripheral/evic_02907/")
intSystemIntTableFile.setSourcePath("../peripheral/evic_02907/templates/system/interrupts_vector_table.h.ftl")
intSystemIntTableFile.setMarkup(True)