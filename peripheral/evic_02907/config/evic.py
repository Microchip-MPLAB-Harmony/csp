from os.path import join

Log.writeInfoMessage("Loading Interrupt Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################

global evicPriorityGroup
evicPriorityGroup = []

global evicSubPriorityGroup
evicSubPriorityGroup = []

node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_PRIO_LEVELS\"]")
if node != None:
    evicPriorityLevels = int(node.getAttribute("value"))
else:
    Log.writeErrorMessage("__INT_PRIO_LEVELS parameter missing in " + + Variables.get("__PROCESSOR") + " ATDF")

node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_SUBPRIO_LEVELS\"]")
if node != None:
    evicSubPriorityLevels = int(node.getAttribute("value"))
else:
    Log.writeErrorMessage("__INT_SUBPRIO_LEVELS parameter missing in " + + Variables.get("__PROCESSOR") + " ATDF")

node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__INT_NUM_SHADOW_SETS\"]")
if node != None:
    evicNumShadowRegSets = int(node.getAttribute("value"))
else:
    Log.writeErrorMessage("__INT_NUM_SHADOW_SETS parameter missing in " + + Variables.get("__PROCESSOR") + " ATDF")

evicPriorityGroup = list(range(evicPriorityLevels + 1))  # 0 to number of levels possible values
evicPriorityGroup = [str(item) for item in evicPriorityGroup]

evicSubPriorityGroup = list(range(evicSubPriorityLevels))
evicSubPriorityGroup = [str(item) for item in evicSubPriorityGroup]

global evicVectorDataStructure
evicVectorDataStructure = []

################################################################################
#### Business Logic ####
################################################################################

def _get_sub_priority_parms(vectorNumber):

    # This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift,
    # and subpriority bitmask for input vector number
    temp = float(vectorNumber) / 4.0
    index = int(temp)
    subPrioBit = 8 * (vectorNumber & 0x3) # bit shift of subpriority field for this interrupt
    subPrioMask = 0x3  # always 2 bits
    prioMask = 0x7     # always 3 bits
    prioBit = subPrioBit + 2            # bit shift of priority field for this interrupt
    regName = "IPC" + str(index)

    return regName, str(prioBit), str(prioMask), str(subPrioBit), str(subPrioMask)

def updateInterruptPriorityAndSubpriorityValue(symbol, event):

    global prioShift
    global subprioShift

    found = False

    # pick off interrupt index number embedded within event ID
    index = event["id"].replace("EVIC_", "")

    if "_PRIORITY" in event["id"]:
        index = index.replace("_PRIORITY", "")
        prioList = [dict for dict in prioShift if index == dict["index"]]
        if len(prioList) != 0:
            shiftval = prioList[0].get("priorityBit")
            symbol.setValue(int(event["value"]) << shiftval, 2)
            found = True
    elif "_SUBPRIORITY" in event["id"]:
        index = index.replace("_SUBPRIORITY", "")
        subPrioList = [dict for dict in subprioShift if index == dict["index"]]
        if len(subPrioList) != 0:
            shiftval = subPrioList[0].get("subPriorityBit")
            symbol.setValue(int(event["value"]) << shiftval, 2)
            found = True

    if found == False:
        Log.writeErrorMessage("***********prioShift: cannot find anything ***************index ", index)

def generateEVICVectorDataStructure():

    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for interrupt in range (0, len(interruptsChildrenList)):

        vectorDict = {}
        vCaption = ""
        vModuleInstance = ""
        vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))

        if "module-instance" in interruptsChildrenList[interrupt].getAttributeList():
            vModuleInstance = str(interruptsChildrenList[interrupt].getAttribute("module-instance"))

        if "header:alternate-name" in interruptsChildrenList[interrupt].getAttributeList():
            vName = str(interruptsChildrenList[interrupt].getAttribute("header:alternate-name"))
        else:
            vName = str(interruptsChildrenList[interrupt].getAttribute("name"))

        if "header:alternate-caption" in interruptsChildrenList[interrupt].getAttributeList():
            if str(interruptsChildrenList[interrupt].getAttribute("header:alternate-caption")) == "None":
                vCaption = vName
            else:
                vCaption = str(interruptsChildrenList[interrupt].getAttribute("header:alternate-caption"))
        else:
            if str(interruptsChildrenList[interrupt].getAttribute("caption")) == "None":
                vCaption = vName
            else:
                vCaption = str(interruptsChildrenList[interrupt].getAttribute("caption"))

        vectorDict["index"] = vIndex
        vectorDict["name"] = vName
        vectorDict["caption"] = vCaption
        vectorDict["module-instance"] = vModuleInstance

        evicVectorDataStructure.append(vectorDict)

def updateEVICVectorEnableUpdateValue(symbol, event):

    symbol.setValue(not event["value"], 2)

def updateEVICVectorParametersValue(symbol, event):

    symbol.setValue(event["value"], 2)

################################################################################
#### Component ####
################################################################################

generateEVICVectorDataStructure()

lowestID = min([vectIndex["index"] for vectIndex in evicVectorDataStructure])
highestID = max([vectIndex["index"] for vectIndex in evicVectorDataStructure])

evicMenu = coreComponent.createMenuSymbol("EVIC_MENU", None)
evicMenu.setLabel("PIC32MZ Interrupts")
evicMenu.setDescription("Configuration for PIC32MZ Interrupts")

evicVectorMax = coreComponent.createIntegerSymbol("EVIC_VECTOR_MAX", evicMenu)
evicVectorMax.setDefaultValue(highestID)
evicVectorMax.setVisible(False)

evicVectorMin = coreComponent.createIntegerSymbol("EVIC_VECTOR_MIN", evicMenu)
evicVectorMin.setDefaultValue(lowestID)
evicVectorMin.setVisible(False)

global prioShift
global subprioShift

prioShift = []
subprioShift = []

for vectorDict in evicVectorDataStructure:

    vModuleInstance = vectorDict.get("module-instance")
    vIndex = vectorDict.get("index")
    vName = vectorDict.get("name")
    vDescription = vectorDict.get("caption")

    evicVectorPeriEnable = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE", evicMenu)
    evicVectorPeriEnable.setLabel("Vector Peripheral Enable")
    evicVectorPeriEnable.setVisible(False)

    evicVectorPeriHandler = coreComponent.createStringSymbol(vName + "_INTERRUPT_HANDLER", evicMenu)
    evicVectorPeriHandler.setLabel("Vector Peripheral Handler")
    evicVectorPeriHandler.setVisible(False)
    evicVectorPeriHandler.setDefaultValue(vName + "_Handler")

    evicVectorPeriHandlerLock = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_HANDLER_LOCK", evicMenu)
    evicVectorPeriHandlerLock.setLabel("Vector Peripheral Handler Lock")
    evicVectorPeriHandlerLock.setVisible(False)

    evicVectorEnable = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_ENABLE", evicMenu)
    evicVectorEnable.setLabel("Enable " + vDescription + " Interrupt")
    evicVectorEnable.setDependencies(updateEVICVectorParametersValue, [vName + "_INTERRUPT_ENABLE"])

    #Vector symbol name:  xc32 toolchain expects underscore as leading character for the vector symbol name
    evicInterruptVector = coreComponent.createStringSymbol("EVIC_" + str(vIndex) + "_VECTOR", evicVectorEnable)
    evicInterruptVector.setDefaultValue("_" + vName + "_VECTOR")
    evicInterruptVector.setVisible(False)

    evicInterruptName = coreComponent.createStringSymbol("EVIC_" + str(vIndex) + "_NAME", evicVectorEnable)
    evicInterruptName.setLabel("Vector Name")
    evicInterruptName.setDefaultValue(vName)
    evicInterruptName.setVisible(False)

    evicVectorNumber = coreComponent.createIntegerSymbol("EVIC_" + str(vIndex) + "_NUMBER", evicVectorEnable)
    evicVectorNumber.setLabel("Vector Number")
    evicVectorNumber.setDefaultValue(vIndex)
    evicVectorNumber.setVisible(False)

    evicVectorPriority = coreComponent.createComboSymbol("EVIC_" + str(vIndex) + "_PRIORITY", evicVectorEnable, evicPriorityGroup)
    evicVectorPriority.setLabel("Priority")
    evicVectorPriority.setDefaultValue(min(evicPriorityGroup) + 1)     #Setting default priority to 1

    evicVectorSubPriority = coreComponent.createComboSymbol("EVIC_" + str(vIndex) + "_SUBPRIORITY", evicVectorEnable, evicSubPriorityGroup)
    evicVectorSubPriority.setLabel("Subpriority")
    evicVectorSubPriority.setDefaultValue(min(evicSubPriorityGroup))

    evicVectorHandler = coreComponent.createStringSymbol("EVIC_" + str(vIndex) + "_HANDLER", evicVectorEnable)
    evicVectorHandler.setLabel("Handler")
    evicVectorHandler.setDefaultValue(vName + "_Handler")

    # Used for mapping plib defined handler
    evicInterruptHandler = coreComponent.createStringSymbol("EVIC_" + str(vIndex) + "_INTERRUPT_HANDLER", evicVectorEnable)
    evicInterruptHandler.setDefaultValue(vName + "_Handler")
    evicInterruptHandler.setVisible(False)
    evicInterruptHandler.setDependencies(updateEVICVectorParametersValue, [vName + "_INTERRUPT_HANDLER"])

    evicVectorHandlerLock = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_HANDLER_LOCK", evicVectorEnable)
    evicVectorHandlerLock.setVisible(False)
    evicVectorHandlerLock.setDependencies(updateEVICVectorParametersValue, [vName + "_INTERRUPT_HANDLER_LOCK"])

    evicVectorEnableUpdate = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE_UPDATE", evicVectorEnable)
    evicVectorEnableUpdate.setVisible(False)
    evicVectorEnableUpdate.setDependencies(updateEVICVectorEnableUpdateValue, ["EVIC_" + str(vIndex) + "_ENABLE"])

    regName, prioBit, prioMask, subPrioBit, subPrioMask = _get_sub_priority_parms(vIndex)

    # IPCx register name for this interrupt
    evicVectorRegName = coreComponent.createStringSymbol("EVIC_" + str(vIndex) + "_REGNAME", evicVectorEnable)
    evicVectorRegName.setDefaultValue(regName)
    evicVectorRegName.setVisible(False)

    prioShiftDict = {}
    prioShiftDict["index"] = str(vIndex)
    prioShiftDict["priorityBit"] = int(prioBit)
    prioShift.append(prioShiftDict)

    subPrioShiftDict = {}
    subPrioShiftDict["index"] = str(vIndex)
    subPrioShiftDict["subPriorityBit"] = int(subPrioBit)
    subprioShift.append(subPrioShiftDict)

    # priority value, shifted to correct bit position, for this interrupt
    evicVectorPriorityValue = coreComponent.createHexSymbol("EVIC_" + str(vIndex) + "_PRIVALUE", evicVectorEnable)
    evicVectorPriorityValue.setDefaultValue(int(evicVectorPriority.getValue()) << int(prioBit))
    evicVectorPriorityValue.setVisible(False)
    evicVectorPriorityValue.setDependencies(updateInterruptPriorityAndSubpriorityValue, ["EVIC_" + str(vIndex) + "_PRIORITY"])

    # subpriority, shifted to correct bit position, for this interrupt
    evicVectorSubPriorityValue = coreComponent.createHexSymbol("EVIC_" + str(vIndex) + "_SUBPRIVALUE", evicVectorEnable)
    evicVectorSubPriorityValue.setDefaultValue(int(evicVectorSubPriority.getValue()) << int(subPrioBit))
    evicVectorSubPriorityValue.setVisible(False)
    evicVectorSubPriorityValue.setDependencies(updateInterruptPriorityAndSubpriorityValue, ["EVIC_" + str(vIndex) + "_SUBPRIORITY"])

############################################################################
#### Code Generation ####
############################################################################

configName = Variables.get("__CONFIGURATION_NAME")

evicSourceFile = coreComponent.createFileSymbol("EVIC_SOURCE", None)
evicSourceFile.setType("SOURCE")
evicSourceFile.setSourcePath("../peripheral/evic_02907/templates/plib_evic.c.ftl")
evicSourceFile.setOutputName("plib_evic.c")
evicSourceFile.setDestPath("/peripheral/evic/")
evicSourceFile.setProjectPath("config/" + configName + "/peripheral/evic/")
evicSourceFile.setMarkup(True)
evicSourceFile.setOverwrite(True)

evicHeaderFile = coreComponent.createFileSymbol("EVIC_HEADER", None)
evicHeaderFile.setType("HEADER")
evicHeaderFile.setSourcePath("../peripheral/evic_02907/templates/plib_evic.h.ftl")
evicHeaderFile.setOutputName("plib_evic.h")
evicHeaderFile.setDestPath("/peripheral/evic/")
evicHeaderFile.setProjectPath("config/" + configName + "/peripheral/evic/")
evicHeaderFile.setMarkup(True)
evicHeaderFile.setOverwrite(True)

evicSystemDefFile = coreComponent.createFileSymbol("EVIC_DEF", None)
evicSystemDefFile.setType("STRING")
evicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
evicSystemDefFile.setSourcePath("../peripheral/evic_02907/templates/system/definitions.h.ftl")
evicSystemDefFile.setMarkup(True)

evicSystemInitFile = coreComponent.createFileSymbol("EVIC_INIT", None)
evicSystemInitFile.setType("STRING")
evicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
evicSystemInitFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization.c.ftl")
evicSystemInitFile.setMarkup(True)

evicSystemIntInitFile = coreComponent.createFileSymbol("EVIC_INT_ENABLE", None)
evicSystemIntInitFile.setType("STRING")
evicSystemIntInitFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
evicSystemIntInitFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization_interrupts_global_enable.c.ftl")
evicSystemIntInitFile.setMarkup(True)

evicSystemInitStartFile = coreComponent.createFileSymbol("EVIC_INT_DISABLE", None)
evicSystemInitStartFile.setType("STRING")
evicSystemInitStartFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
evicSystemInitStartFile.setSourcePath("../peripheral/evic_02907/templates/system/initialization_interrupts_global_disable.c.ftl")
evicSystemInitStartFile.setMarkup(True)

evicSystemIntTableFile = coreComponent.createFileSymbol("EVIC_INT_TABLE", None)
evicSystemIntTableFile.setType("STRING")
evicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
evicSystemIntTableFile.setSourcePath("../peripheral/evic_02907/templates/system/interrupts_vector_table.h.ftl")
evicSystemIntTableFile.setMarkup(True)