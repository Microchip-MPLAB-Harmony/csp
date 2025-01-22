global INT_MENU, INT_DATA, HANDLER_NAME
INTC_MENU = "INTC_MENU"
INTC_DATA = "INTC_DATA"
HANDLER_NAME = "HANDLER_NAME"

# Symbols list required for callback func
global intEnableSymbolsList, intPrioritySymbolsList, intPolaritySymbolsList
intEnableSymbolsList = []
intPrioritySymbolsList = []
intPolaritySymbolsList = []

# Constants for symbols
global INTC_ENABLE, INTC_ENABLE_CONTEXT, INTC_HANDLER_LOCK, INTC_POLARITY, INTC_HANDLER, INTC_INTERRUPT_HANDLER, INTC_PRIORITY
INTC_ENABLE = "INTC_{}_ENABLE"
INTC_ENABLE_CONTEXT = "INTC_{}_ENABLE_CONTEXT"
INTC_HANDLER_LOCK = "INTC_{}_HANDLER_LOCK"
INTC_POLARITY = "INTC_{}_POLARITY"
INTC_HANDLER = "INTC_{}_HANDLER"
INTC_INTERRUPT_HANDLER = "INTC_{}_INTERRUPT_HANDLER"
INTC_PRIORITY = "INTC_{}_PRIORITY"

global EXTERNAL_EXTERNAL_INTERRUPT_UPDATE
EXTERNAL_EXTERNAL_INTERRUPT_UPDATE = "EXTERNAL_{}_EXTERNAL_INTERRUPT_UPDATE"

global INTC_VECTOR_MIN, INTC_VECTOR_MAX
INTC_VECTOR_MIN = "INTC_VECTOR_MIN"
INTC_VECTOR_MAX = "INTC_VECTOR_MAX"

global MODULE_NAME_UPPER_CASE, MODULE_NAME_LOWER_CASE, FILE_NAME_LOWER_CASE, INT_SOURCE_IRQ_LIST, MAX_EXTERNAL_INT_COUNT, GET_INTERRUPT_PRIORITY_DATA, GET_EXT_INTERRUPT_POSITIVE_EDGE, GIE_STATUS_BIT
MODULE_NAME_UPPER_CASE = "moduleNameUpperCase"
MODULE_NAME_LOWER_CASE = "moduleNameLowerCase"
FILE_NAME_LOWER_CASE = "fileNameLowerCase"
INT_SOURCE_IRQ_LIST = "intSourceIRQList"
MAX_EXTERNAL_INT_COUNT = "MAX_EXTERNAL_INT_COUNT"
GET_INTERRUPT_PRIORITY_DATA = "getInterruptPriorityData"
GET_EXT_INTERRUPT_POSITIVE_EDGE = "getExtInterruptEdgePolarity"
GIE_STATUS_BIT = "GIEStatusbit"

global INTC_SOURCE, INTC_HEADER, DEFINITIONS, INTERRUPTS_SOURCE, INTERRUPTS_HEADER
INTC_SOURCE = "INTC_SOURCE"
INTC_HEADER = "INTC_HEADER"
DEFINITIONS = "DEFINITIONS"
INTERRUPTS_SOURCE = "INTERRUPTS_SOURCE"
INTERRUPTS_HEADER = "INTERRUPTS_HEADER"
TRAPS_SOURCE = "TRAPS_SOURCE"
TRAPS_HEADER = "TRAPS_HEADER"

global EXT_INTERRUPT_INTxEP_REG
EXT_INTERRUPT_INTxEP_REG = "INTCON2"

global EDGE_POLARITY_OPTIONS, PRIORITY_OPTIONS, INTERRUPT_CORE
EDGE_POLARITY_OPTIONS = ["Falling Edge", "Rising Edge"]
PRIORITY_OPTIONS = ["1", "2", "3", "4", "5", "6", "7"]
INTERRUPT_CORE = "intc"

# By handler name
global notSupportedInterruptsList
notSupportedInterruptsList = [
    "COMMONInterrupt",
    "CPUFPUInterrupt",
    "XRAMECCInterrupt",
    "YRAMECCInterrupt",
    "PBUEInterrupt",
    "U1EVTInterrupt",
    "U2EVTInterrupt",
    "U3EVTInterrupt",
    "BISS1EInterrupt",
    "BISS1Interrupt",
    "IOIM1Interrupt",
    "IOIM2Interrupt",
    "IOIM3Interrupt",
    "IOIM4Interrupt",
    "IOIM5Interrupt",
    "IOIM6Interrupt",
    "IOIM7Interrupt",
    "IOIM8Interrupt",
    "IOIM9Interrupt",
    "IOIM10Interrupt",
    "IOIM11Interrupt",
    "IOIM12Interrupt",
    "IOIM13Interrupt",
    "IOIM14Interrupt",
    "IOIM15Interrupt",
    "IOIM16Interrupt",
]

BUS_ERROR_TRAP_AVAILABLE = "busErrorTrapAvailable"
ADDRESS_ERROR_TRAP_AVAILABLE = "addressErrorTrapAvailable"
GENERAL_TRAP_AVAILABLE = "generalTrapAvailable"
DMT_TRAP_AVAILABLE = "dmtTrapAvailable"
SOFT_TRAP_AVAILABLE = "softTrapAvailable"
WDT_TRAP_AVAILABLE = "wdtTrapAvailable"
MATH_ERROR_TRAP_AVAILABLE = "mathErrorTrapAvailable"
STACK_ERROR_TRAP_AVAILABLE = "stackErrorTrapAvailable"
ILLEGAL_INSTRUCTION_TRAP_AVAILABLE = "illegalInstructionTrapAvailable"

BUS_ERROR_TRAP_STATUS_BIT = "busErrorTrapStatusBit"
ADDRESS_ERROR_TRAP_STATUS_BIT = "addressErrorTrapStatusBit"
DMT_TRAP_STATUS_BIT = "dmtTrapStatusBit"
SOFT_TRAP_STATUS_BIT = "softTrapStatusBit"
WDT_TRAP_STATUS_BIT = "wdtTrapStatusBit"
MATH_ERROR_TRAP_STATUS_BIT = "mathErrorTrapStatusBit"
STACK_ERROR_TRAP_STATUS_BIT = "stackErrorTrapStatusBit"
ILLEGAL_INSTRUCTION_TRAP_STATUS_BIT = "illegalInstructionTrapStatusBit"
vectorIndexList = []

# Function names
global isExternalInterrupt, generateDefineMacros, generateExternalInterruptEnum, findMinAndMaxVectorNum, generateInterruptHandlerNames, getExtIntEnabledList, getRegisterChildren, getRegisterList, externalInterruptControl, getIPCRegName, getInterruptPriorityData, getInterruptPriorityDataCallback, getExtInterruptPositiveEdge, getExtInterruptPositiveEdgeCallback, delFullStopAddInterrupt, findRegNameByBit, trapsHelperFunc


def trapsHelperFunc(bitfieldName):

    for register in getRegisterList(INTERRUPT_CORE, "INTCON"):
        registerName = register.getAttribute("name")
        for bitfield in getRegisterChildren(INTERRUPT_CORE, "INTCON", registerName):
            if bitfield.getAttribute("name") == bitfieldName:
                return True, "{}bits.{}".format(registerName, bitfieldName)

    return False, None


def createTrapSymbols(
    coreComponent, trapName, isPresentSymbolName, statusBitSymbolName
):

    (doesTrapExist, trapBit) = trapsHelperFunc(trapName)
    # Create boolean symbol
    trap = coreComponent.createBooleanSymbol(isPresentSymbolName, None)
    trap.setDefaultValue(doesTrapExist)
    trap.setVisible(False)

    # Create string symbol if the trap exists
    if doesTrapExist:
        trapValue = coreComponent.createStringSymbol(statusBitSymbolName, None)
        trapValue.setDefaultValue(trapBit)
        trapValue.setVisible(False)


# To check whether an interrupt is external interrupt or not.
def isExternalInterrupt(interruptCaption):

    import re

    pattern = r"^External Interrupt (\d)$"
    match = re.match(pattern, interruptCaption)

    if match:
        return int(match.group(1))
    return None


# To generate the #define interrupts list in ic.h
# Condition check here for non supported
def generateDefineMacros(interruptList):

    res = []
    for interrupt in range(len(interruptList)):
        intName = str(interruptList[interrupt].getAttribute("name"))
        if intName not in notSupportedInterruptsList:
            intIndex = int(interruptList[interrupt].getAttribute("index"))
            removeIntFromName = intName.replace("Interrupt", "")
            template = "#define INT_SOURCE_{:<15}{}U".format(
                removeIntFromName, intIndex
            )
            res.append(template)
    return "\n".join(res)


# TO generate the enum list in ic.h
def generateExternalInterruptEnum(interruptList):

    extIntCount = 0
    for interrupt in range(len(interruptList)):
        interruptCaption = str(interruptList[interrupt].getAttribute("caption"))
        if isExternalInterrupt(interruptCaption) != None:
            extIntCount += 1

    res = []
    template = "    EXTERNAL_INT_{:<2} = _IEC1_INT{}IE_MASK,"
    for i in range(extIntCount):
        line = template.format(i, i)
        res.append(line)

    return "\n".join(res)


# To find the min and max vector num in interruptList
def findMinAndMaxVectorNum(interruptList):

    minVectorNum = float("inf")
    maxVectorNum = float("-inf")

    for interrupt in range(len(interruptList)):
        interruptIndex = int(interruptList[interrupt].getAttribute("index"))
        minVectorNum = min(minVectorNum, interruptIndex)
        maxVectorNum = max(maxVectorNum, interruptIndex)

    return minVectorNum, maxVectorNum


# To make the interrupt handler names in the format `_InterruptHandler`
def generateInterruptHandlerNames(interruptList):

    import re

    intHandlerList = []

    for interrupt in range(len(interruptList)):
        interruptName = str(interruptList[interrupt].getAttribute("name"))
        match = re.search(r"([A-Za-z0-9]+)Interrupt", interruptName)
        if match:
            name = match.group(1)
            intHandlerList.append("{}_InterruptHandler".format(name))

    return intHandlerList


# To find the list of enabled external interrupt
def getExtIntEnabledList(symbolComponent, interruptsChildrenList):

    import re

    enabledExtIntList = []
    pattern = r"^INT\d+Interrupt$"

    for interrupt in range(len(interruptsChildrenList)):
        isIntEnabled = symbolComponent.getSymbolValue(INTC_ENABLE.format(interrupt))
        handler = symbolComponent.getSymbolValue(INTC_HANDLER.format(interrupt))
        if isIntEnabled == True and re.match(pattern, handler):
            enabledExtIntList.append(interrupt)
    return enabledExtIntList


# To get the child nodes of a register in ATDF
def getRegisterChildren(moduleName, registerGroup, register):

    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    return ATDF.getNode(atdfPath).getChildren()


# To get the child nodes of a register group in ATDF
def getRegisterList(moduleName, registerGroup):

    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]'
    )
    return ATDF.getNode(atdfPath).getChildren()


# Callback func to set the External Interrupt enable symbol when the corresponding IC gets set
def externalInterruptControl(symbol, event):
    symbol.setValue(event["value"])


# Helper func to get the IPC reg name and mask value in that of a particular vector num.
def getIPCRegName(vectorNumber):

    regName = int(vectorNumber / 8)
    remainder = int(vectorNumber % 8)

    remaindertoMaskMap = {
        0: "0x7",
        1: "0x70",
        2: "0x700",
        3: "0x7000",
        4: "0x70000",
        5: "0x700000",
        6: "0x7000000",
        7: "0x70000000",
    }
    mask = remaindertoMaskMap.get(remainder)

    return "IPC{}".format(regName), mask


# To get the list of priority data of enabled int in ic.c
def getInterruptPriorityData(symbolComponent, interruptsChildrenList):

    result = []
    for interrupt in interruptsChildrenList:
        interruptIndex = int(interrupt.getAttribute("index"))
        isIntEnabled = symbolComponent.getSymbolValue(
            INTC_ENABLE.format(interruptIndex)
        )
        if isIntEnabled == True:
            regName, mask = getIPCRegName(interruptIndex)
            bitfieldData = getRegisterChildren(INTERRUPT_CORE, "IPC", regName)
            for bitfield in bitfieldData:
                if bitfield.getAttribute("mask") == mask:
                    result.append(
                        "{0}bits.{1} = {2};".format(
                            regName,
                            bitfield.getAttribute("name"),
                            symbolComponent.getSymbolValue(
                                INTC_PRIORITY.format(interruptIndex)
                            ),
                        )
                    )

    return "\n".join(line if i == 0 else "    " + line for i, line in enumerate(result))


# Helper Callback for getInterruptPriorityData
def getInterruptPriorityDataCallback(symbol, event):

    interruptsChildrenList = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    symbol.setValue(
        getInterruptPriorityData(symbol.getComponent(), interruptsChildrenList)
    )


def getExtInterruptPositiveEdge(symbolComponent, interruptsChildrenList):

    result = []
    for interrupt in interruptsChildrenList:
        interruptIndex = str(interrupt.getAttribute("index"))
        interruptName = str(interrupt.getAttribute("name"))
        interruptCaption = str(interrupt.getAttribute("caption"))
        isIntEnabled = symbolComponent.getSymbolValue(
            INTC_ENABLE.format(interruptIndex)
        )
        # This can be moved up
        if isIntEnabled == True and isExternalInterrupt(interruptCaption) != None:
            result.append(
                "{0}bits.{1}EP = {2};".format(
                    EXT_INTERRUPT_INTxEP_REG,
                    interruptName.replace("Interrupt", ""),
                    (
                        0
                        if symbolComponent.getSymbolValue(
                            INTC_POLARITY.format(interruptIndex)
                        )
                        == "Falling Edge"
                        else 1
                    ),
                )
            )
            # result.append("INTCON2bits.{0}EP = {1};".format(interruptName.replace("Interrupt", ""),
            #                                             0 if symbolComponent.getSymbolValue(IC_POLARITY.format(interruptIndex)) == "Falling Edge" else 1))
    return "\n".join(line if i == 0 else "    " + line for i, line in enumerate(result))


# Helper Callback for getExtInterruptPositiveEdge
def getExtInterruptPositiveEdgeCallback(symbol, event):

    interruptsChildrenList = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    symbol.setValue(
        getExtInterruptPositiveEdge(symbol.getComponent(), interruptsChildrenList)
    )


# Remove fullstop and add `Interrupt` for the label
def delFullStopAddInterrupt(inputStr):

    inputStr = inputStr.rstrip(".")
    words = inputStr.split()

    for i, word in enumerate(words):
        if word.lower() == "interrupt":
            words[i] = "Interrupt"

    if "Interrupt" not in words:
        words.append("Interrupt")

    return " ".join(words)


def findRegNameByBit(regGroupName, regList, bitName):

    for regData in regList:
        bitfieldData = getRegisterChildren(
            INTERRUPT_CORE, regGroupName, regData.getAttribute("name")
        )
        for bitfield in bitfieldData:
            bitfieldName = bitfield.getAttribute("name")
            if bitfieldName == bitName:
                return regData.getAttribute("name")


global deviceSeriesNode, deviceSeries
deviceSeriesNode = ATDF.getNode(
    '/avr-tools-device-file/devices/device@[architecture="33Axxx"]'
)
deviceSeries = deviceSeriesNode.getAttribute("series")

# Can be made ints
icMenu = coreComponent.createMenuSymbol(INTC_MENU, None)
icMenu.setLabel("Interrupts")
icMenu.setDescription("Configuration for " + deviceSeries + " Interrupts")

interruptsChildrenList = ATDF.getNode(
    "/avr-tools-device-file/devices/device/interrupts"
).getChildren()

minVectorNum, maxVectorNum = findMinAndMaxVectorNum(interruptsChildrenList)

icVectorMin = coreComponent.createIntegerSymbol(INTC_VECTOR_MIN, icMenu)
icVectorMin.setDefaultValue(minVectorNum)
icVectorMin.setVisible(False)

icVectorMax = coreComponent.createIntegerSymbol(INTC_VECTOR_MAX, icMenu)
icVectorMax.setDefaultValue(maxVectorNum)
icVectorMax.setVisible(False)

intHandlerList = generateInterruptHandlerNames(interruptsChildrenList)

numOfExtInt = 0
for interrupt in range(len(interruptsChildrenList)):
    intIndex = str(interruptsChildrenList[interrupt].getAttribute("index"))
    intName = str(interruptsChildrenList[interrupt].getAttribute("name"))
    intCaption = str(interruptsChildrenList[interrupt].getAttribute("caption"))

    if intName not in notSupportedInterruptsList:
        # Check for min and max
        isIntEnabled = coreComponent.createBooleanSymbol(
            INTC_ENABLE.format(intIndex), icMenu
        )
        isIntEnabled.setLabel(delFullStopAddInterrupt("Enable {}".format(intCaption)))
        isIntEnabled.setDescription("Configuration for {}".format(intName))
        isIntEnabled.setDefaultValue(False)

        intEnableSymbolsList.append(INTC_ENABLE.format(intIndex))

        hasContext = coreComponent.createBooleanSymbol(
            INTC_ENABLE_CONTEXT.format(intIndex), isIntEnabled
        )
        hasContext.setLabel("Enable Context")
        hasContext.setDescription("Configuration for {} Context".format(intName))
        hasContext.setDefaultValue(False)
        regName = getIPCRegName(int(intIndex))
        hasContext.setHelp(
            "atmel;device:"
            + Variables.get("__PROCESSOR")
            + ";comp:intc_04436;register:{}".format(regName)
        )

        handlerLock = coreComponent.createBooleanSymbol(
            INTC_HANDLER_LOCK.format(intIndex), isIntEnabled
        )
        handlerLock.setDefaultValue(False)
        handlerLock.setVisible(False)

        extIntNum = isExternalInterrupt(intCaption)
        if extIntNum != None:
            # Rename
            # The below 3 symbols are meant for code generation of exteranl interrupts, they are not shown in the UI
            extIntUpdate = coreComponent.createBooleanSymbol(
                EXTERNAL_EXTERNAL_INTERRUPT_UPDATE.format(extIntNum), isIntEnabled
            )
            extIntUpdate.setDefaultValue(False)
            extIntUpdate.setVisible(False)
            extIntUpdate.setDependencies(
                externalInterruptControl, [INTC_ENABLE.format(intIndex)]
            )

            extIntIECReg = coreComponent.createStringSymbol(
                "extInt{}IECReg".format(extIntNum), isIntEnabled
            )
            extIntIECReg.setDefaultValue(
                findRegNameByBit(
                    "IEC",
                    getRegisterList(INTERRUPT_CORE, "IEC"),
                    "INT{}IE".format(extIntNum),
                )
            )
            extIntIECReg.setVisible(False)

            extIntIFSReg = coreComponent.createStringSymbol(
                "extInt{}IFSReg".format(extIntNum), isIntEnabled
            )
            extIntIFSReg.setDefaultValue(
                findRegNameByBit(
                    "IFS",
                    getRegisterList(INTERRUPT_CORE, "IFS"),
                    "INT{}IF".format(extIntNum),
                )
            )
            extIntIFSReg.setVisible(False)

            edgePolarity = coreComponent.createComboSymbol(
                INTC_POLARITY.format(intIndex), isIntEnabled, EDGE_POLARITY_OPTIONS
            )
            edgePolarity.setLabel("Edge Polarity")
            edgePolarity.setDescription(
                "Configuration for " + intName + " Edge Polarity"
            )
            edgePolarity.setDefaultValue("Falling Edge")

            intPolaritySymbolsList.append(INTC_POLARITY.format(intIndex))

            handlerLock.setDependencies(
                externalInterruptControl, [INTC_ENABLE.format(intIndex)]
            )

            numOfExtInt += 1

        # Property for the priority levels to be created in ATDF
        priority = coreComponent.createComboSymbol(
            INTC_PRIORITY.format(intIndex), isIntEnabled, PRIORITY_OPTIONS
        )
        priority.setLabel("Priority")
        priority.setDescription(
            "Configuration for {} Interrupt Priority".format(intName)
        )
        priority.setDefaultValue("1")

        intPrioritySymbolsList.append(INTC_PRIORITY.format(intIndex))

        handlerName = coreComponent.createStringSymbol(
            INTC_HANDLER.format(intIndex), isIntEnabled
        )
        handlerName.setLabel("Handler")
        handlerName.setDescription("Configuration for {} Handler Name".format(intName))
        handlerName.setDefaultValue(intName)
        handlerName.setReadOnly(True)

        intHandler = coreComponent.createStringSymbol(
            INTC_INTERRUPT_HANDLER.format(intIndex), isIntEnabled
        )
        intHandler.setDefaultValue(intHandlerList[interrupt])
        intHandler.setVisible(False)

        intcName = coreComponent.createStringSymbol(
            "INTC_{}_NAME".format(intIndex), None
        )
        intcName.setDefaultValue(intName)
        intcName.setVisible(False)

        intcCaption = coreComponent.createStringSymbol(
            "INTC_{}_CAPTION_UI".format(intIndex), None
        )
        intcCaption.setDefaultValue(intCaption)
        intcCaption.setVisible(False)

        if intIndex not in vectorIndexList:
            vectorIndexList.append(intIndex)

vectorIndexGUIList = [str(r) for r in vectorIndexList]
intc = coreComponent.createComboSymbol(
    "INTC_GUI_COLUMN_VECTOR_ID", icMenu, vectorIndexGUIList
)
intc.setVisible(False)

# Code Generation

moduleNameUpperCase = coreComponent.createStringSymbol(MODULE_NAME_UPPER_CASE, icMenu)
moduleNameUpperCase.setDefaultValue("INTC")
moduleNameUpperCase.setVisible(False)

moduleNameLowerCase = coreComponent.createStringSymbol(MODULE_NAME_LOWER_CASE, icMenu)
moduleNameLowerCase.setDefaultValue("intc")
moduleNameLowerCase.setVisible(False)

fileNameLowerCase = coreComponent.createStringSymbol(FILE_NAME_LOWER_CASE, icMenu)
fileNameLowerCase.setDefaultValue("plib_intc")
fileNameLowerCase.setVisible(False)

intSourceIRQList = coreComponent.createStringSymbol(INT_SOURCE_IRQ_LIST, icMenu)
intSourceIRQList.setDefaultValue(generateDefineMacros(interruptsChildrenList))
intSourceIRQList.setVisible(False)

maxExtIntCount = coreComponent.createIntegerSymbol(MAX_EXTERNAL_INT_COUNT, icMenu)
maxExtIntCount.setDefaultValue(numOfExtInt)
maxExtIntCount.setVisible(False)

gieStatusBit = coreComponent.createStringSymbol(GIE_STATUS_BIT, icMenu)
gieStatusBit.setDefaultValue(
    "{}bits.GIE".format(
        findRegNameByBit("INTCON", getRegisterList(INTERRUPT_CORE, "INTCON"), "GIE")
    )
)
gieStatusBit.setVisible(False)

getInterruptPriorityDataSymbol = coreComponent.createStringSymbol(
    GET_INTERRUPT_PRIORITY_DATA, icMenu
)
getInterruptPriorityDataSymbol.setDefaultValue("")
getInterruptPriorityDataSymbol.setVisible(False)
getInterruptPriorityDataSymbol.setDependencies(
    getInterruptPriorityDataCallback, intEnableSymbolsList + intPrioritySymbolsList
)

getExtInterruptPositiveEdgeSymbol = coreComponent.createStringSymbol(
    GET_EXT_INTERRUPT_POSITIVE_EDGE, icMenu
)
getExtInterruptPositiveEdgeSymbol.setDefaultValue("")
getExtInterruptPositiveEdgeSymbol.setVisible(False)
getExtInterruptPositiveEdgeSymbol.setDependencies(
    getExtInterruptPositiveEdgeCallback, intEnableSymbolsList + intPolaritySymbolsList
)

cspVersion = coreComponent.createStringSymbol("CSPVersion", icMenu)
cspVersion.setDefaultValue("1.0.0")
cspVersion.setVisible(False)

selectedDev = coreComponent.createStringSymbol("selectedDevice", icMenu)
selectedDev.setDefaultValue("dsPIC33AK512MPS512")
selectedDev.setVisible(False)

disc = coreComponent.createStringSymbol("disclaimer", icMenu)
disc.setDefaultValue(" ")
disc.setVisible(False)

# Traps Generated Code

trapsFileUpperCase = coreComponent.createStringSymbol("trapsFileUpperCase", icMenu)
trapsFileUpperCase.setDefaultValue("TRAPS")
trapsFileUpperCase.setVisible(False)

trapsFileLowerCase = coreComponent.createStringSymbol("trapsFileLowerCase", icMenu)
trapsFileLowerCase.setDefaultValue("traps")
trapsFileLowerCase.setVisible(False)

supressMisraWarning = coreComponent.createBooleanSymbol("supressMisraWarning", icMenu)
supressMisraWarning.setDefaultValue(False)
supressMisraWarning.setVisible(False)

traps = ["CPUBET", "ADDRERR", "DMTE", "SOFT", "WDTE", "DIV0ERR", "STKERR", "BADOPERR"]

trapAvailableSymbols = [
    BUS_ERROR_TRAP_AVAILABLE,
    ADDRESS_ERROR_TRAP_AVAILABLE,
    DMT_TRAP_AVAILABLE,
    SOFT_TRAP_AVAILABLE,
    WDT_TRAP_AVAILABLE,
    MATH_ERROR_TRAP_AVAILABLE,
    STACK_ERROR_TRAP_AVAILABLE,
    ILLEGAL_INSTRUCTION_TRAP_AVAILABLE,
]

trapStatusSymbols = [
    BUS_ERROR_TRAP_STATUS_BIT,
    ADDRESS_ERROR_TRAP_STATUS_BIT,
    DMT_TRAP_STATUS_BIT,
    SOFT_TRAP_STATUS_BIT,
    WDT_TRAP_STATUS_BIT,
    MATH_ERROR_TRAP_STATUS_BIT,
    STACK_ERROR_TRAP_STATUS_BIT,
    ILLEGAL_INSTRUCTION_TRAP_STATUS_BIT,
]

for trap, trapAvailable, trapStatus in zip(
    traps, trapAvailableSymbols, trapStatusSymbols
):
    createTrapSymbols(coreComponent, trap, trapAvailable, trapStatus)

generalTrapAvailable = coreComponent.createBooleanSymbol(GENERAL_TRAP_AVAILABLE, icMenu)
generalTrapAvailable.setDefaultValue(True)
generalTrapAvailable.setVisible(False)

configName = Variables.get("__CONFIGURATION_NAME")

icSourceFile = coreComponent.createFileSymbol(INTC_SOURCE, None)
icSourceFile.setType("SOURCE")
icSourceFile.setSourcePath("../peripheral/intc_04436/templates/plib_intc.c.ftl")
icSourceFile.setOutputName("plib_intc.c")
icSourceFile.setDestPath("/peripheral/intc/")
icSourceFile.setProjectPath("config/{}/peripheral/intc/".format(configName))
icSourceFile.setMarkup(True)
icSourceFile.setOverwrite(True)

icHeaderFile = coreComponent.createFileSymbol(INTC_HEADER, None)
icHeaderFile.setType("HEADER")
icHeaderFile.setSourcePath("../peripheral/intc_04436/templates/plib_intc.h.ftl")
icHeaderFile.setOutputName("plib_intc.h")
icHeaderFile.setDestPath("/peripheral/intc/")
icHeaderFile.setProjectPath("config/{}/peripheral/intc/".format(configName))
icHeaderFile.setMarkup(True)
icHeaderFile.setOverwrite(True)

defFile = coreComponent.createFileSymbol(DEFINITIONS, None)
defFile.setType("STRING")
defFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
defFile.setSourcePath("../peripheral/intc_04436/templates/system/definitions.h.ftl")
defFile.setMarkup(True)

intSourceFile = coreComponent.createFileSymbol(INTERRUPTS_SOURCE, None)
intSourceFile.setType("STRING")
intSourceFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
intSourceFile.setSourcePath(
    "../peripheral/intc_04436/templates/system/interrupts_vector_table.h.ftl"
)
intSourceFile.setMarkup(True)

intHeaderFile = coreComponent.createFileSymbol(INTERRUPTS_HEADER, None)
intHeaderFile.setType("STRING")
intHeaderFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLER_DECLS")
intHeaderFile.setSourcePath(
    "../peripheral/intc_04436/templates/system/interrupts_handlers_decls.h.ftl"
)
intHeaderFile.setMarkup(True)

initFile = coreComponent.createFileSymbol("INITIALIZATION_FILE", None)
initFile.setType("STRING")
initFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
initFile.setSourcePath("../peripheral/intc_04436/templates/system/initialization.c.ftl")
initFile.setMarkup(True)

initIntGlobalEnableFile = coreComponent.createFileSymbol("INIT_INT_GLOBAL_ENABLE", None)
initIntGlobalEnableFile.setType("STRING")
initIntGlobalEnableFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
initIntGlobalEnableFile.setSourcePath(
    "../peripheral/intc_04436/templates/system/initialization_interrupts_global_enable.c.ftl"
)
initIntGlobalEnableFile.setMarkup(True)

initIntGlobalDisableFile = coreComponent.createFileSymbol(
    "INIT_INT_GLOBAL_DISABLE", None
)
initIntGlobalDisableFile.setType("STRING")
initIntGlobalDisableFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
initIntGlobalDisableFile.setSourcePath(
    "../peripheral/intc_04436/templates/system/initialization_interrupts_global_disable.c.ftl"
)
initIntGlobalDisableFile.setMarkup(True)
