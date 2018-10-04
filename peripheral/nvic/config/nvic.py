# coding: utf-8
"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

global nvicPriorityLevels
nvicPriorityLevels = 0

global nvicPriorityGroup
nvicPriorityGroup = []

global nvicCorePriorityGroup
nvicCorePriorityGroup = []

node = ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__NVIC_PRIO_BITS\"]")
priority_bits = node.getAttribute("value")
nvicPriorityLevels = (2 ** int(priority_bits))

nvicPriorityGroup = list(range(nvicPriorityLevels))
nvicPriorityGroup = [str(item) for item in nvicPriorityGroup]

nvicCorePriorityGroup = list(range(-3, nvicPriorityLevels))
nvicCorePriorityGroup = [str(item) for item in nvicCorePriorityGroup]

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
                "MemoryManagement": [False,  True,    False,    "0",     False,   True,     True],
                "BusFault"        : [False,  False,   False,    "0",     False,   True,     True],
                "UsageFault"      : [False,  False,   False,    "0",     False,   True,     True],
                "SVCall"          : [True,   True,    False,    "0",     False,   True,     True],
                "DebugMonitor"    : [False,  False,   False,    "0",     False,   True,     True],
                "PendSV"          : [True,   True,    False,    "0",     False,   True,     True],
                "SysTick"         : [False,  True,    False,    "0",     False,   True,     True],
                "Peripheral"      : [False,  False,   True,     str(max(nvicPriorityGroup)),     False,   True,     False]}

global nvicVectorDataDictionary
nvicVectorDataDictionary = {}

nvicVectorPeriEnableSymbolList = []
nvicVectorPeriHandlerSymbolList = []
nvicVectorPeriHandlerLockSymbolList = []

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
nvicVectorGenericHandler = []
nvicVectorGenericName = []

global interruptsChildrenList

interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

################################################################################
#### Business Logic ####
################################################################################

def generateNVICVectorDataDictionary():

    for interrupt in range (0, len(interruptsChildrenList)):

        vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
        vModuleInstance = str(interruptsChildrenList[interrupt].getAttribute("module-instance"))

        if "header:alternate-name" in interruptsChildrenList[interrupt].getAttributeList():
            vName = str(interruptsChildrenList[interrupt].getAttribute("header:alternate-name"))
        else:
            vName = str(interruptsChildrenList[interrupt].getAttribute("name"))

        if " " in vModuleInstance:
            nvicVectorDataDictionary[vIndex] = list(vModuleInstance.split(" "))
        else:
            nvicVectorDataDictionary[vIndex] = [vName]

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

def getGenericVectorName(vecIndex):

    for interrupt in range (0, len(interruptsChildrenList)):

        vName = str(interruptsChildrenList[interrupt].getAttribute("name"))
        vIndex = str(interruptsChildrenList[interrupt].getAttribute("index"))

        if str(vecIndex) == vIndex:
            if "header:alternate-name" in interruptsChildrenList[interrupt].getAttributeList():
                return str(interruptsChildrenList[interrupt].getAttribute("header:alternate-name"))
            else:
                return vName

def updateNVICVectorPeriEnableValue(symbol, event):

    symbol.clearValue()

    if event["value"] == False:
        symbol.setValue(True, 2)
    else :
        symbol.setValue(False, 2)

def updateNVICVectorParametersValue(symbol, event):

    symbol.clearValue()
    symbol.setValue(event["value"], 2)

def updateNVICHandlerParametersValue(symbol, event):

    symbol.clearValue()
    symbol.setValue(event["value"], 2)

def updateNVICHandlerLockParametersValue(symbol, event):

    symbol.clearValue()
    symbol.setValue(event["value"], 2)

################################################################################
#### Component ####
################################################################################

generateNVICVectorDataDictionary()

highestID = int(max(nvicVectorDataDictionary))
lowestID = int(min(nvicVectorDataDictionary))

max_key, max_value = max(nvicVectorDataDictionary.items(), key = lambda x: len(set(x[1])))

nvicMenu = coreComponent.createMenuSymbol("NVIC_MENU", None)
nvicMenu.setLabel("Interrupts (NVIC)")
nvicMenu.setDescription("Configuration for NVIC Initialization")

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MAX", nvicMenu)
nvicVectorMax.setLabel("Vector Max Value")
nvicVectorMax.setDefaultValue(highestID)
nvicVectorMax.setVisible(False)

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MIN", nvicMenu)
nvicVectorMax.setLabel("Vector Min Value")
nvicVectorMax.setDefaultValue(lowestID)
nvicVectorMax.setVisible(False)

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MAX_MULTIPLE_HANDLERS", nvicMenu)
nvicVectorMax.setLabel("Vector Max Multiple Hanler For Vector")
nvicVectorMax.setDefaultValue(len(max_value))
nvicVectorMax.setVisible(False)

index = 0
priorityList = []

for vIndex in sorted(nvicVectorDataDictionary):

    nvicVectorNumber.append([])
    nvicVectorName.append([])
    nvicVectorEnableLock.append([])
    nvicVectorEnableGenerate.append([])
    nvicVectorEnable.append([])
    nvicVectorPriority.append([])
    nvicVectorPriorityLock.append([])
    nvicVectorPriorityGenerate.append([])
    nvicVectorHandler.append([])
    nvicVectorHandlerLock.append([])
    nvicVectorGenericHandler.append([])
    nvicVectorGenericName.append([])

    handlerList = nvicVectorDataDictionary.get(vIndex)

    for listIndex in range(0, len(handlerList)):

        vName = handlerList[listIndex]
        vDescription = str(getInterruptDescription(vIndex, vName))
        vector = vName

        if vector not in vectorSettings:
            vector = "Peripheral"

        if int(vectorSettings[vector][3]) < 0:
            priorityList = nvicCorePriorityGroup
        else:
            priorityList = nvicPriorityGroup

        nvicVectorPeriEnableList = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE", nvicMenu)
        nvicVectorPeriEnableList.setLabel("Vector Peripheral Enable")
        nvicVectorPeriEnableList.setVisible(False)
        nvicVectorPeriEnableSymbolList.append(vName + "_INTERRUPT_ENABLE")

        nvicVectorPeriHandlerList = coreComponent.createStringSymbol(vName + "_INTERRUPT_HANDLER", nvicMenu)
        nvicVectorPeriHandlerList.setLabel("Vector Peripheral Handler")
        nvicVectorPeriHandlerList.setVisible(False)
        nvicVectorPeriHandlerList.setDefaultValue(vName + "_Handler")
        nvicVectorPeriHandlerSymbolList.append(vName + "_INTERRUPT_HANDLER")

        nvicVectorPeriHandlerLockList = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_HANDLER_LOCK", nvicMenu)
        nvicVectorPeriHandlerLockList.setLabel("Vector Peripheral Handler Lock")
        nvicVectorPeriHandlerLockList.setVisible(False)
        nvicVectorPeriHandlerLockSymbolList.append(vName + "_INTERRUPT_HANDLER_LOCK")

        nvicVectorEnable[index].append(listIndex)
        nvicVectorEnable[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE", nvicMenu)
        nvicVectorEnable[index][listIndex].setLabel("Enable " + vDescription + " Interrupt")
        nvicVectorEnable[index][listIndex].setDefaultValue(vectorSettings[vector][0])
        nvicVectorEnable[index][listIndex].setDependencies(updateNVICVectorParametersValue, [vName + "_INTERRUPT_ENABLE"])

        nvicVectorNumber[index].append(listIndex)
        nvicVectorNumber[index][listIndex] = coreComponent.createIntegerSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_NUMBER", nvicVectorEnable[index][listIndex])
        nvicVectorNumber[index][listIndex].setLabel("Vector Number")
        nvicVectorNumber[index][listIndex].setDefaultValue(int(vIndex))
        nvicVectorNumber[index][listIndex].setVisible(False)

        nvicVectorName[index].append(listIndex)
        nvicVectorName[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_VECTOR", nvicVectorEnable[index][listIndex])
        nvicVectorName[index][listIndex].setLabel("Vector Name")
        nvicVectorName[index][listIndex].setVisible(False)
        nvicVectorName[index][listIndex].setDefaultValue(vName)

        nvicVectorEnableLock[index].append(listIndex)
        nvicVectorEnableLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorEnableLock[index][listIndex].setLabel("Enable Lock")
        nvicVectorEnableLock[index][listIndex].setVisible(False)
        nvicVectorEnableLock[index][listIndex].setDefaultValue(vectorSettings[vector][1])

        nvicVectorEnableGenerate[index].append(listIndex)
        nvicVectorEnableGenerate[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE_GENERATE", nvicVectorEnable[index][listIndex])
        nvicVectorEnableGenerate[index][listIndex].setLabel("Enable Generate")
        nvicVectorEnableGenerate[index][listIndex].setVisible(False)
        nvicVectorEnableGenerate[index][listIndex].setDefaultValue(vectorSettings[vector][2])

        nvicVectorPriority[index].append(listIndex)
        nvicVectorPriority[index][listIndex] = coreComponent.createComboSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY", nvicVectorEnable[index][listIndex], priorityList)
        nvicVectorPriority[index][listIndex].setLabel("Priority")
        nvicVectorPriority[index][listIndex].setDefaultValue(vectorSettings[vector][3])

        nvicVectorPriorityLock[index].append(index)
        nvicVectorPriorityLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorPriorityLock[index][listIndex].setLabel("Priority Lock")
        nvicVectorPriorityLock[index][listIndex].setVisible(False)
        nvicVectorPriorityLock[index][listIndex].setDefaultValue(vectorSettings[vector][4])

        nvicVectorPriorityGenerate[index].append(index)
        nvicVectorPriorityGenerate[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY_GENERATE", nvicVectorEnable[index][listIndex])
        nvicVectorPriorityGenerate[index][listIndex].setLabel("Priority Generate")
        nvicVectorPriorityGenerate[index][listIndex].setVisible(False)
        nvicVectorPriorityGenerate[index][listIndex].setDefaultValue(vectorSettings[vector][5])

        nvicVectorHandler[index].append(listIndex)
        nvicVectorHandler[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_HANDLER", nvicVectorEnable[index][listIndex])
        nvicVectorHandler[index][listIndex].setLabel("Handler")
        nvicVectorHandler[index][listIndex].setDefaultValue(vName + "_Handler")
        nvicVectorHandler[index][listIndex].setDependencies(updateNVICHandlerParametersValue, [vName + "_INTERRUPT_HANDLER"])

        nvicVectorHandlerLock[index].append(listIndex)
        nvicVectorHandlerLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_HANDLER_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorHandlerLock[index][listIndex].setLabel("Handler Lock")
        nvicVectorHandlerLock[index][listIndex].setVisible(False)
        nvicVectorHandlerLock[index][listIndex].setDefaultValue(vectorSettings[vector][6])
        nvicVectorHandlerLock[index][listIndex].setDependencies(updateNVICHandlerParametersValue, [vName + "_INTERRUPT_HANDLER_LOCK"])

        nvicVectorGenericName[index].append(listIndex)
        nvicVectorGenericName[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_GENERIC_NAME", nvicVectorEnable[index][listIndex])
        nvicVectorGenericName[index][listIndex].setLabel("Generic Vector Name")
        nvicVectorGenericName[index][listIndex].setVisible(False)
        nvicVectorGenericName[index][listIndex].setDefaultValue(str(getGenericVectorName(vIndex)))

        if len(handlerList) > 1:

            nvicVectorGenericHandler[index].append(listIndex)
            nvicVectorGenericHandler[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_GENERIC_HANDLER", nvicVectorEnable[index][listIndex])
            nvicVectorGenericHandler[index][listIndex].setLabel("Generic Handler")
            nvicVectorGenericHandler[index][listIndex].setVisible(False)
            nvicVectorGenericHandler[index][listIndex].setDefaultValue(str(getGenericVectorName(vIndex) + "_Handler"))

        nvicVectorPeriEnableUpdate = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE_UPDATE", nvicMenu)
        nvicVectorPeriEnableUpdate.setLabel("NVIC Peripheral Enable/Disable Update")
        nvicVectorPeriEnableUpdate.setVisible(False)
        nvicVectorPeriEnableUpdate.setDependencies(updateNVICVectorPeriEnableValue, ["NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE"])

    index += 1

############################################################################
#### Code Generation ####
############################################################################

configName = Variables.get("__CONFIGURATION_NAME")

nvicHeaderFile = coreComponent.createFileSymbol("NVIC_HEADER", None)
nvicHeaderFile.setType("HEADER")
nvicHeaderFile.setSourcePath("../peripheral/nvic/templates/plib_nvic.h.ftl")
nvicHeaderFile.setOutputName("plib_nvic.h")
nvicHeaderFile.setDestPath("/peripheral/nvic/")
nvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicHeaderFile.setMarkup(True)
nvicHeaderFile.setOverwrite(True)

nvicSourceFile = coreComponent.createFileSymbol("NVIC_SOURCE", None)
nvicSourceFile.setType("SOURCE")
nvicSourceFile.setSourcePath("../peripheral/nvic/templates/plib_nvic.c.ftl")
nvicSourceFile.setOutputName("plib_nvic.c")
nvicSourceFile.setDestPath("/peripheral/nvic/")
nvicSourceFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
nvicSourceFile.setMarkup(True)
nvicSourceFile.setOverwrite(True)

nvicSystemInitFile = coreComponent.createFileSymbol("NVIC_INIT", None)
nvicSystemInitFile.setType("STRING")
nvicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
nvicSystemInitFile.setSourcePath("../peripheral/nvic/templates/system/initialization.c.ftl")
nvicSystemInitFile.setMarkup(True)

nvicSystemDefFile = coreComponent.createFileSymbol("NVIC_DEF", None)
nvicSystemDefFile.setType("STRING")
nvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
nvicSystemDefFile.setSourcePath("../peripheral/nvic/templates/system/definitions.h.ftl")
nvicSystemDefFile.setMarkup(True)

nvicSystemIntMultipleHandleFile = coreComponent.createFileSymbol("NVIC_MULTIPLE_HANDLER", None)
nvicSystemIntMultipleHandleFile.setType("STRING")
nvicSystemIntMultipleHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS")
nvicSystemIntMultipleHandleFile.setSourcePath("../peripheral/nvic/templates/system/interrupts_multiple_handlers.h.ftl")
nvicSystemIntMultipleHandleFile.setMarkup(True)

nvicSystemIntWeakHandleFile = coreComponent.createFileSymbol("NVIC_INT_HANDLER", None)
nvicSystemIntWeakHandleFile.setType("STRING")
nvicSystemIntWeakHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS")
nvicSystemIntWeakHandleFile.setSourcePath("../peripheral/nvic/templates/system/interrupts_weak_handlers.h.ftl")
nvicSystemIntWeakHandleFile.setMarkup(True)

nvicSystemIntTableFile = coreComponent.createFileSymbol("NVIC_INT_TABLE", None)
nvicSystemIntTableFile.setType("STRING")
nvicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLERS")
nvicSystemIntTableFile.setSourcePath("../peripheral/nvic/templates/system/interrupts_vector_table.h.ftl")
nvicSystemIntTableFile.setMarkup(True)
