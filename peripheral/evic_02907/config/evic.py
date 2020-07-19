"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

from os.path import join

Log.writeInfoMessage("Loading Interrupt Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################

global evicSystemIntASMFile

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

evicPriorityGroup = list(range(1, evicPriorityLevels + 1))  # 1 to number of levels possible values
evicPriorityGroup = [str(item) for item in evicPriorityGroup]

evicSubPriorityGroup = list(range(evicSubPriorityLevels))
evicSubPriorityGroup = [str(item) for item in evicSubPriorityGroup]

global evicVectorDataStructure
evicVectorDataStructure = []

global evicVectorSettings

#Default configuration for vector with RTOS support
evicVectorSettings = {

    #Entry : [ #Enable value,
               #Enable Lock,
               #Enable Generate,
               #Initial Priority value,
               #Priority Lock,
               #Priority Generate,
               #Initial subPriority value,
               #SubPriority Lock,
               #SubPriority Generate,
               #Handler Lock ]
    "CORE_SOFTWARE_0" : [False, True, False, str(min(evicPriorityGroup)), True, False, str(min(evicSubPriorityGroup)), True, False, True],  # Specific to FreeRTOS
    "TIMER_1"         : [False, True, False, str(min(evicPriorityGroup)), True, False, str(min(evicSubPriorityGroup)), True, False, True],  # With RTOS
    "Peripheral"      : [False, False, True,  str(min(evicPriorityGroup)), False, True,  str(min(evicSubPriorityGroup)), False, True, False]  # With Baremetal
}

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

    # pick off interrupt index number embedded within event ID
    index = event["id"].replace("EVIC_", "")

    if "_PRIORITY" in event["id"]:
        index = index.replace("_PRIORITY", "")
        prioList = [dict for dict in prioShift if index == dict["index"]]
        if len(prioList) != 0:
            shiftval = prioList[0].get("priorityBit")
            symbol.setValue(int(event["value"]) << shiftval, 2)
    elif "_SUBPRIORITY" in event["id"]:
        index = index.replace("_SUBPRIORITY", "")
        subPrioList = [dict for dict in subprioShift if index == dict["index"]]
        if len(subPrioList) != 0:
            shiftval = subPrioList[0].get("subPriorityBit")
            symbol.setValue(int(event["value"]) << shiftval, 2)

def generateEVICVectorDataStructure():

    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for interrupt in range (len(interruptsChildrenList)):

        vectorDict = {}
        irqCaption = ""
        irqIndex = -1
        irqName = ""

        vecIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
        vecName = str(interruptsChildrenList[interrupt].getAttribute("name"))
        vecCaption = str(interruptsChildrenList[interrupt].getAttribute("caption"))

        if "irq-index" in interruptsChildrenList[interrupt].getAttributeList():
            irqIndex = int(interruptsChildrenList[interrupt].getAttribute("irq-index"))

        if "irq-name" in interruptsChildrenList[interrupt].getAttributeList():
            irqName = str(interruptsChildrenList[interrupt].getAttribute("irq-name"))
        else:
            irqName = vecName

        if "irq-caption" in interruptsChildrenList[interrupt].getAttributeList():
            irqCaption = str(interruptsChildrenList[interrupt].getAttribute("irq-caption"))
        else:
            irqCaption = vecCaption

        vectorDict["index"] = vecIndex
        vectorDict["name"] = vecName
        vectorDict["caption"] = vecCaption
        vectorDict["irq-index"] = irqIndex
        vectorDict["irq-name"] = irqName
        vectorDict["irq-caption"] = irqCaption

        evicVectorDataStructure.append(vectorDict)

def updateEVICVectorEnableUpdateValue(symbol, event):

    symbol.setValue(not event["value"], 2)

def updateEVICVectorParametersValue(symbol, event):
    symbol.setValue(event["value"])

def updateEVICVectorParametersValue1(symbol, event):
    if "SELECT_RTOS" in event["id"]:
        symbolId = symbol.getID()
        vectorIndex=symbolId.split("_")[1]
        if not ((event["value"] == "ThreadX") and (vectorIndex == "1")): # Software Interrupt 0 is not used by ThreadX
            symbol.setValue((event["value"] != "BareMetal"))
    else:
        symbol.setValue(event["value"])

def updateEVICVectorSettings(symbol, event):

    symbolId = symbol.getID()
    vectorIndex=symbolId.split("_")[1]

    if not ((event["value"] == "ThreadX") and (vectorIndex == "1")): # Software Interrupt 0 is not used by ThreadX
        if "_ENABLE_LOCK" in symbolId:
            symbol.setValue((event["value"] != "BareMetal"))
        elif "_ENABLE_GENERATE" in symbolId:
            symbol.setValue((event["value"] == "BareMetal"))
        elif "_PRIORITY_LOCK" in symbolId:
            symbol.setValue((event["value"] != "BareMetal"))
        elif "_PRIORITY_GENERATE" in symbolId:
            symbol.setValue((event["value"] == "BareMetal"))
        elif "_SUBPRIORITY_LOCK" in symbolId:
            symbol.setValue((event["value"] != "BareMetal"))
        elif "_SUBPRIORITY_GENERATE" in symbolId:
            symbol.setValue((event["value"] == "BareMetal"))
        else:
            symbol.setValue((event["value"] != "BareMetal"))         # For CORE_TIMER_0 with FreeRtos


    evicSystemIntASMFile.setEnabled((event["value"] == "FreeRTOS"))

def externalInterruptControl(symbol, event):
    i = []
    # splitting of ID below is dependent on ID name, if ID name is changed, below code may need a change as well
    # Split the id name by "_" and put all the split names in the list "i"
    i = symbol.getID().split("_")
    j = event["id"].split("_")

    symbol.setValue(event["value"])

    Database.setSymbolValue("core", "EVIC_" + j[1] + "_HANDLER_LOCK", event["value"], 1)

    if event["value"] == True:
        Database.setSymbolValue("core", "EVIC_" + j[1] + "_INTERRUPT_HANDLER", "EXTERNAL_" + i[1] + "_InterruptHandler", 1)
    else :
        Database.setSymbolValue("core","EVIC_" + j[1] + "_INTERRUPT_HANDLER", "EXTERNAL_" + i[1] + "_Handler", 1)

def updateInterruptPriorityforSRS(symbol, event):
    symbol.setValue(int(event["value"][-1]))

def updateInterruptAttribute(symbol, event):
    for i in range(1,8):
        Database.setSymbolValue("core", "EVIC_PRIORITY_" + str(i) + "ATTRIBUTE", "SOFT", 1)

    if event["value"] != 0:
        Database.setSymbolValue("core", "EVIC_PRIORITY_" + str(event["value"]) + "ATTRIBUTE", "SRS", 1)

def updatePRISS(symbol, event):
    symbol.setValue(1 << (event["value"] * 4))

################################################################################
#### Component ####
################################################################################

generateEVICVectorDataStructure()

vecLowestID = min([vectIndex["index"] for vectIndex in evicVectorDataStructure])
vecHighestID = max([vectIndex["index"] for vectIndex in evicVectorDataStructure])

irqLowestID = min([vectIndex["irq-index"] for vectIndex in evicVectorDataStructure])
irqHighestID = max([vectIndex["irq-index"] for vectIndex in evicVectorDataStructure])

deviceSeriesNode = ATDF.getNode("/avr-tools-device-file/devices/device@[architecture=\"MIPS\"]")
deviceSeries = deviceSeriesNode.getAttribute("series")

evicMenu = coreComponent.createMenuSymbol("EVIC_MENU", None)
evicMenu.setLabel(deviceSeries + " Interrupts")
evicMenu.setDescription("Configuration for " + deviceSeries + " Interrupts")

############################################# Shadow Register Setting Start ############################################## 
node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__INT_NUM_SHADOW_SETS"]')
numOfShadowSet = int(node.getAttribute("value"))

evicShadowRegMenu = coreComponent.createMenuSymbol("EVIC_SHADOW_REG_MENU", evicMenu)
evicShadowRegMenu.setLabel("Shadow Register Set Configuration")
if numOfShadowSet == 0:
    evicShadowRegMenu.setVisible(False)

SRS_MENU_COMMENT = coreComponent.createCommentSymbol("EVIC_SRS_COMMENT", evicShadowRegMenu)
SRS_MENU_COMMENT.setLabel("**** Configure Shadow Register Set in DEVCFG3 Fuse Settings ****")
SRS_MENU_COMMENT.setVisible(False)

if numOfShadowSet == 1: # For PIC32MX3XX/4XX and PIC32MKGPE series
    evicNumOfShadowSet = coreComponent.createIntegerSymbol("EVIC_PRIORITY_FOR_SHADOW_SET", evicShadowRegMenu)
    evicNumOfShadowSet.setLabel("Shadow Set used by Interrupt with a priority level of")
    evicNumOfShadowSet.setDefaultValue(7)
    if deviceSeries == "PIC32MX":
        evicNumOfShadowSet.setReadOnly(True)
        SRS_MENU_COMMENT.setVisible(True)
        evicNumOfShadowSet.setDependencies(updateInterruptPriorityforSRS, ["CONFIG_FSRSSEL"])
    else: #for PIC32MK
        evicNumOfShadowSet.setMin(1)
        evicNumOfShadowSet.setMax(7)

for i in range (1,8):
    if numOfShadowSet == 7:
        evicPriorityShadowSetMap = coreComponent.createIntegerSymbol("EVIC_PRIORITY_" + str(i) + "_SHADOW_SET", evicShadowRegMenu)
        evicPriorityShadowSetMap.setLabel("Interrupt with a priority level of " + str(i) + " uses Shadow Set")
        evicPriorityShadowSetMap.setReadOnly(True)
        evicPriorityShadowSetMap.setDefaultValue(i)
        evicPriorityShadowSetMap.setVisible(True)

    evicPriorityISR_Attribute = coreComponent.createComboSymbol("EVIC_PRIORITY_" + str(i) + "ATTRIBUTE", evicShadowRegMenu, ["SOFT", "SRS", "AUTO"])
    evicPriorityISR_Attribute.setLabel("Interrupt with a priority level of " + str(i) + " uses ISR Attribute")
    evicPriorityISR_Attribute.setVisible(False)
    if numOfShadowSet == 7:
        evicPriorityISR_Attribute.setDefaultValue("SRS")
    else:
        if i == 7 and numOfShadowSet == 1:
            evicPriorityISR_Attribute.setDefaultValue("SRS")
        else:
            evicPriorityISR_Attribute.setDefaultValue("SOFT")

if numOfShadowSet == 1:
    evicPriorityISR_Attribute.setDependencies(updateInterruptAttribute, ["EVIC_PRIORITY_FOR_SHADOW_SET"])

if ATDF.getNode('/avr-tools-device-file/modules/module@[name="INT"]/register-group@[name="INT"]/register@[name="PRISS"]') is not None:
    evicPRISSValue = coreComponent.createHexSymbol("EVIC_PRISS_VALUE", evicShadowRegMenu)
    evicPRISSValue.setVisible(False)
    if numOfShadowSet == 7:
        evicPRISSValue.setDefaultValue(0x76543210)
    else:
        evicPRISSValue.setDefaultValue(0x10000000)
        evicPRISSValue.setDependencies(updatePRISS, ["EVIC_PRIORITY_FOR_SHADOW_SET"])
############################################# Shadow Register Setting End ############################################## 

evicVectorMax = coreComponent.createIntegerSymbol("EVIC_VECTOR_MAX", evicMenu)
evicVectorMax.setDefaultValue(vecHighestID)
evicVectorMax.setVisible(False)

evicVectorMin = coreComponent.createIntegerSymbol("EVIC_VECTOR_MIN", evicMenu)
evicVectorMin.setDefaultValue(vecLowestID)
evicVectorMin.setVisible(False)

evicIRQMax = coreComponent.createIntegerSymbol("EVIC_IRQ_MAX", evicMenu)
evicIRQMax.setDefaultValue(irqHighestID)
evicIRQMax.setVisible(False)

evicIRQMin = coreComponent.createIntegerSymbol("EVIC_IRQ_MIN", evicMenu)
evicIRQMin.setDefaultValue(irqLowestID)
evicIRQMin.setVisible(False)

global prioShift
global subprioShift

prioShift = []
subprioShift = []

vectorIndexList = []

for vectorDict in evicVectorDataStructure:

    vIndex = vectorDict.get("index")
    vName = vectorDict.get("name")
    vDescription = vectorDict.get("caption")

    irqIndex = vectorDict.get("irq-index")
    irqName = vectorDict.get("irq-name")
    irqDescription = vectorDict.get("irq-caption")

    # Check weather IRQ support is there or not
    if irqIndex != -1:

        #IRQ symbol name:  xc32 toolchain expects underscore as leading character for the IRQ symbol name
        evicIRQ = coreComponent.createStringSymbol("EVIC_" + str(irqIndex) + "_IRQ", None)
        evicIRQ.setDefaultValue("_" + irqName + "_IRQ")
        evicIRQ.setVisible(False)

        evicIRQName = coreComponent.createStringSymbol("EVIC_" + str(irqIndex) + "_IRQ_NAME", None)
        evicIRQName.setDefaultValue(irqName)
        evicIRQName.setVisible(False)

        evicIRQNumber = coreComponent.createIntegerSymbol("EVIC_" + str(irqIndex) + "_IRQ_NUMBER", None)
        evicIRQNumber.setDefaultValue(irqIndex)
        evicIRQNumber.setVisible(False)

    if vIndex not in vectorIndexList:            #Skip duplicate vector entry
        vectorIndexList.append(vIndex)

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

        if "EXTERNAL_" == vName[:-1]:
            evicExtIntPolarity = coreComponent.createComboSymbol("EVIC_" + str(vIndex) + "_EXT_INT_EDGE_POLARITY", evicVectorEnable, ["Rising Edge", "Falling Edge"])
            evicExtIntPolarity.setLabel("Edge Polarity")
            evicExtIntPolarity.setDefaultValue("Falling Edge") 

        evicVectorPriority = coreComponent.createComboSymbol("EVIC_" + str(vIndex) + "_PRIORITY", evicVectorEnable, evicPriorityGroup)
        evicVectorPriority.setLabel("Priority")
        evicVectorPriority.setDefaultValue(min(evicPriorityGroup))     #Setting default priority to 1

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
        evicVectorHandlerLock.setDependencies(updateEVICVectorParametersValue1, [vName + "_INTERRUPT_HANDLER_LOCK"])

        evicVectorEnableUpdate = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE_UPDATE", evicVectorEnable)
        evicVectorEnableUpdate.setVisible(False)
        evicVectorEnableUpdate.setDependencies(updateEVICVectorEnableUpdateValue, ["EVIC_" + str(vIndex) + "_ENABLE"])

        if "EXTERNAL_" == vName[:-1]:
            externalIntUpdate = coreComponent.createBooleanSymbol(vName + "_EXTERNAL_INTERRUPT_UPDATE", evicVectorEnable)
            externalIntUpdate.setVisible(False)
            externalIntUpdate.setDependencies(externalInterruptControl, ["EVIC_" + str(vIndex) + "_ENABLE"])

        #Only created for vector used by RTOS
        if vName in evicVectorSettings:

            if evicVectorSettings[vName][0] == True:
                evicVectorEnable.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            vector = "Peripheral"

            evicVectorHandlerLock.setDefaultValue(evicVectorSettings[vector][9])
            # override the dependency to add "SELECT_RTOS" symbol
            evicVectorHandlerLock.setDependencies(updateEVICVectorParametersValue1, [vName + "_INTERRUPT_HANDLER_LOCK", "HarmonyCore.SELECT_RTOS"])

            evicVectorEnableLock = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_ENABLE_LOCK", evicVectorEnable)
            evicVectorEnableLock.setVisible(False)
            evicVectorEnableLock.setDefaultValue(evicVectorSettings[vector][1])
            evicVectorEnableLock.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            evicVectorEnableGenerate = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_ENABLE_GENERATE", evicVectorEnable)
            evicVectorEnableGenerate.setVisible(False)
            evicVectorEnableGenerate.setDefaultValue(evicVectorSettings[vector][2])
            evicVectorEnableGenerate.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            evicVectorPriorityLock = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_PRIORITY_LOCK", evicVectorEnable)
            evicVectorPriorityLock.setVisible(False)
            evicVectorPriorityLock.setDefaultValue(evicVectorSettings[vector][4])
            evicVectorPriorityLock.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            evicVectorPriorityGenerate = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_PRIORITY_GENERATE", evicVectorEnable)
            evicVectorPriorityGenerate.setVisible(False)
            evicVectorPriorityGenerate.setDefaultValue(evicVectorSettings[vector][5])
            evicVectorPriorityGenerate.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            evicVectorSubPriorityLock = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_SUBPRIORITY_LOCK", evicVectorEnable)
            evicVectorSubPriorityLock.setVisible(False)
            evicVectorSubPriorityLock.setDefaultValue(evicVectorSettings[vector][7])
            evicVectorSubPriorityLock.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

            evicVectorSubPriorityGenerate = coreComponent.createBooleanSymbol("EVIC_" + str(vIndex) + "_SUBPRIORITY_GENERATE", evicVectorEnable)
            evicVectorSubPriorityGenerate.setVisible(False)
            evicVectorSubPriorityGenerate.setDefaultValue(evicVectorSettings[vector][8])
            evicVectorSubPriorityGenerate.setDependencies(updateEVICVectorSettings, ["HarmonyCore.SELECT_RTOS"])

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

###################################################################################################
####################################### Driver Symbols ############################################
###################################################################################################

corePeripherals = {}

# Components which are creating critical section
corePeripherals = getCorePeripheralsInterruptDataStructure()

for moduleInstance in corePeripherals:

    dict = {}
    dict = corePeripherals.get(moduleInstance)
    vectName = dict.get("name")
    vectIntSrc = dict.get("INT_SRC")

    if len(vectName) > 1:
        # Symbol to check peripheral contains multi vector
        evicMultiVector = coreComponent.createBooleanSymbol(moduleInstance + "_MULTI_IRQn", None)
        evicMultiVector.setDefaultValue(True)
        evicMultiVector.setVisible(False)

        for intSrc in range(len(vectIntSrc)):

            # Check weather IRQ support is there or not
            if irqLowestID != -1 and irqHighestID != -1:
                name = "_" + vectName[intSrc] + "_IRQ"
            else:
                name = "_" + vectName[intSrc] + "_VECTOR"

            # Symbol to get individual interrupt vector of peripheral containing multi vector
            evicVectorNumber = coreComponent.createStringSymbol(moduleInstance + "_" + vectIntSrc[intSrc] + "_INT_SRC", None)
            evicVectorNumber.setDefaultValue(name)
            evicVectorNumber.setVisible(False)
    else:
        if len(vectName) != 0:
            name = "_" + vectName[0] + "_VECTOR"

            # Symbol to get interrupt vector of peripheral containing single vector
            evicVectorName = coreComponent.createStringSymbol(moduleInstance + "_SINGLE_IRQn", None)
            evicVectorName.setDefaultValue(name)
            evicVectorName.setVisible(False)

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

evicSystemIntWeakHandleFile = coreComponent.createFileSymbol("EVIC_INT_HANDLER", None)
evicSystemIntWeakHandleFile.setType("STRING")
evicSystemIntWeakHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS")
evicSystemIntWeakHandleFile.setSourcePath("../peripheral/evic_02907/templates/system/interrupts_weak_handlers.h.ftl")
evicSystemIntWeakHandleFile.setMarkup(True)

evicSystemIntTableFile = coreComponent.createFileSymbol("EVIC_INT_TABLE", None)
evicSystemIntTableFile.setType("STRING")
evicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
evicSystemIntTableFile.setSourcePath("../peripheral/evic_02907/templates/system/interrupts_vector_table.h.ftl")
evicSystemIntTableFile.setMarkup(True)

evicSystemIntASMFile = coreComponent.createFileSymbol("EVIC_INT_ASM", None)
evicSystemIntASMFile.setType("STRING")
evicSystemIntASMFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_ASM")
evicSystemIntASMFile.setSourcePath("../peripheral/evic_02907/templates/system/interrupts_vector_asm.h.ftl")
evicSystemIntASMFile.setMarkup(True)
evicSystemIntASMFile.setEnabled(False)