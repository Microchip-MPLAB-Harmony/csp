# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
vectorSettings = {
                    "Reset"           : [True,   True,    False,    "-3",    True,    False,    True],
                    "NonMaskableInt"  : [True,   True,    False,    "-2",    True,    False,    True],
                    "HardFault"       : [True,   True,    False,    "-1",    True,    False,    True],
                    "MemoryManagement": [False,  True,    False,    "0",     False,   True,     True],
                    "BusFault"        : [False,  False,   False,    "0",     False,   True,     True],
                    "UsageFault"      : [False,  False,   False,    "0",     False,   True,     True],
                    "SVCall"          : [True,   True,    False,    "0",     False,   True,     True],
                    "DebugMonitor"    : [False,  False,   False,    "0",     False,   True,     True],
                    "PendSV"          : [True,   True,    False,    "0",     False,   True,     True],
                    "SysTick"         : [False,  True,    False,    "0",     False,   True,     True],
                    "Peripheral"      : [False,  False,   True,     str(max(nvicPriorityGroup)),     False,   True,     False]
                }
if Database.getSymbolValue("core","CoreArchitecture") in ["CORTEX-M4", "CORTEX-M7"] :
    vectorSettings["MemoryManagement"] = [True,   True,    False,    "-1",    True,    False,    True]
    vectorSettings["BusFault"] = [True,   True,    False,    "-1",    True,    False,    True]
    vectorSettings["UsageFault"] = [True,   True,    False,    "-1",    True,    False,    True]
    vectorSettings["DebugMonitor"] = [True,   True,    False,    "-1",    True,    False,    True]


nvicVectorNumber = []
nvicVectorName = []
nvicVectorNameUI = []
nvicVectorEnable = []
nvicVectorEnableLock = []
nvicVectorEnableGenerate = []
nvicVectorPriority = []
nvicVectorPriorityLock = []
nvicVectorPriorityGenerate = []
nvicVectorHandler = []
nvicVectorHandlerLock = []
nvicVectorGenericHandler = []
nvicVectorCaption = []
nvicVectorNum = []
nvicVectorNumInterrupts = []

global nvicVectorDataStructure
nvicVectorDataStructure = []

################################################################################
#### Business Logic ####
################################################################################
global ecia_module
ecia_module = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ECIA"]"')

def generateNVICVectorDataStructure():

    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for interrupt in range (0, len(interruptsChildrenList)):

        vectorDict = {}
        vCaption = ""
        vIndex = int(interruptsChildrenList[interrupt].getAttribute("index"))
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
        if ecia_module != None:
            arg_list = {"int_source": vName}
            # Send a message to ECIA to get module instance list. ECIA returns a dictionary with vName as the key and list of module-instances as the value
            vectorDict["module-instance"] = Database.sendMessage("core", "NVIC_GET_MODULE_INSTANCE_LIST", arg_list)[vName]
        else:
            vectorDict["module-instance"] = list(vModuleInstance.split(" "))

        nvicVectorDataStructure.append(vectorDict)

def updateNVICVectorPeriEnableValue(symbol, event):

    symbol.setValue(not event["value"], 2)

def updateNVICVectorParametersValue(symbol, event):
    symbol.setValue(event["value"], 2)

def updateSecurity(symbol, event):
    if event["value"]:
        symbol.setValue(1)
    else:
        symbol.setValue(0)

def NVIC_InterruptUpdate(symbol, event):
    vName = ""
    is_enabled = event["value"]
    if "_INTERRUPT_ENABLE" in event["id"]:
        vName = event["id"][:-len("_INTERRUPT_ENABLE")]
    else:
        index = int(event["id"].split("_")[1])
        listIndex = int(event["id"].split("_")[2])
        for vectorDict in nvicVectorDataStructure:
            if vectorDict.get("index") == index:
                handlerList = vectorDict.get("module-instance")
                if len(handlerList) == 1:
                    vName = vectorDict.get("name")
                else:
                    vName = handlerList[listIndex]
                break

    if vName.endswith("_GRP"):
        vName = vName[:-(len("_GRP"))]

    arg_list = {"int_source": vName, "isEnabled": is_enabled}
    Database.sendMessage("core", "NVIC_INT_UPDATE", arg_list)
################################################################################
#### Component ####
################################################################################

generateNVICVectorDataStructure()

lowestID = min([vectIndex['index'] for vectIndex in nvicVectorDataStructure])
highestID = max([vectIndex['index'] for vectIndex in nvicVectorDataStructure])

maxPeriAtVector = len(max([vectModuleInstance['module-instance'] for vectModuleInstance in nvicVectorDataStructure], key=len))

nvicMenu = coreComponent.createMenuSymbol("NVIC_MENU", None)
nvicMenu.setLabel("Interrupts (NVIC)")
nvicMenu.setDescription("Configuration for NVIC Initialization")

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MAX", nvicMenu)
nvicVectorMax.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
nvicVectorMax.setLabel("Vector Max Value")
nvicVectorMax.setDefaultValue(highestID)
nvicVectorMax.setVisible(False)

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MIN", nvicMenu)
nvicVectorMax.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
nvicVectorMax.setLabel("Vector Min Value")
nvicVectorMax.setDefaultValue(lowestID)
nvicVectorMax.setVisible(False)

nvicVectorMax = coreComponent.createIntegerSymbol("NVIC_VECTOR_MAX_MULTIPLE_HANDLERS", nvicMenu)
nvicVectorMax.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
nvicVectorMax.setLabel("Vector Max Multiple Hanler For Vector")
nvicVectorMax.setDefaultValue(maxPeriAtVector)
nvicVectorMax.setVisible(False)

nvicTotalVectors = coreComponent.createIntegerSymbol("NVIC_NUM_VECTORS", nvicMenu)
nvicTotalVectors.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
nvicTotalVectors.setLabel("Total NVIC Vector Lines")
nvicTotalVectors.setDefaultValue(len(nvicVectorDataStructure))

global nvicIntUpdateDepList
nvicIntUpdateDepList = []

nvicIntUpdate = coreComponent.createBooleanSymbol("NVIC_INT_UPDATE", nvicMenu)

index = 0
priorityList = []

for vectorDict in nvicVectorDataStructure:

    nvicVectorNumber.append([])
    nvicVectorName.append([])
    nvicVectorNameUI.append([])
    nvicVectorEnableLock.append([])
    nvicVectorEnableGenerate.append([])
    nvicVectorEnable.append([])
    nvicVectorPriority.append([])
    nvicVectorPriorityLock.append([])
    nvicVectorPriorityGenerate.append([])
    nvicVectorHandler.append([])
    nvicVectorHandlerLock.append([])
    nvicVectorGenericHandler.append([])
    nvicVectorCaption.append([])
    nvicVectorNum.append([])
    nvicVectorNumInterrupts.append([])

    handlerList = vectorDict.get("module-instance")
    vIndex = vectorDict.get("index")
    genericName = vectorDict.get("name")

    # Below symbol is only used by NVIC UI to know the NVIC vector number
    nvicVectorNum[index] = coreComponent.createStringSymbol("NVIC_VECTOR_NUM_" + str(index), nvicMenu)
    nvicVectorNum[index].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
    nvicVectorNum[index].setLabel("Vector Number")
    nvicVectorNum[index].setDefaultValue(str(vIndex))

    # Below symbol is only used by NVIC UI to know the number of interrupts on a given NVIC vector number
    nvicVectorNumInterrupts[index] = coreComponent.createIntegerSymbol("NVIC_NUM_INTERRUPTS_" + str(index), nvicMenu)
    nvicVectorNumInterrupts[index].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
    nvicVectorNumInterrupts[index].setLabel("Number of Interrupts on the NVIC vector line")
    nvicVectorNumInterrupts[index].setDefaultValue(len(handlerList))

    for listIndex in range(0, len(handlerList)):

        # check weather sub-vectors or multiple peripherals are present at same interrupt line
        if len(handlerList) == 1:
            vName = vectorDict.get("name")
            vDescription = vectorDict.get("caption")
        else:
            vName = handlerList[listIndex]
            vDescription = vName

        vector = vName

        if vector not in vectorSettings:
            vector = "Peripheral"

        if int(vectorSettings[vector][3]) < 0:
            priorityList = nvicCorePriorityGroup
        else:
            priorityList = nvicPriorityGroup

        nvicVectorPeriEnableList = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE", nvicMenu)
        nvicVectorPeriEnableList.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPeriEnableList.setLabel("Vector Peripheral Enable")
        nvicVectorPeriEnableList.setVisible(False)
        nvicIntUpdateDepList.append(vName + "_INTERRUPT_ENABLE")

        nvicVectorPeriHandlerList = coreComponent.createStringSymbol(vName + "_INTERRUPT_HANDLER", nvicMenu)
        nvicVectorPeriHandlerList.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPeriHandlerList.setLabel("Vector Peripheral Handler")
        nvicVectorPeriHandlerList.setVisible(False)
        nvicVectorPeriHandlerList.setDefaultValue(vName + "_Handler")

        nvicVectorPeriHandlerLockList = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_HANDLER_LOCK", nvicMenu)
        nvicVectorPeriHandlerLockList.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPeriHandlerLockList.setLabel("Vector Peripheral Handler Lock")
        nvicVectorPeriHandlerLockList.setVisible(False)

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            nvicSecureSetup = coreComponent.createBooleanSymbol(vName + "_SET_NON_SECURE", nvicMenu)
            nvicSecureSetup.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
            nvicSecureSetup.setLabel("Peripheral Interrupt Security Setup")
            nvicSecureSetup.setVisible(False)

        nvicVectorCaption[index].append(listIndex)
        nvicVectorCaption[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_CAPTION", nvicMenu)
        nvicVectorCaption[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorCaption[index][listIndex].setLabel("Caption")
        nvicVectorCaption[index][listIndex].setDefaultValue(vectorDict.get("caption"))
        nvicVectorCaption[index][listIndex].setVisible(False)

        nvicVectorEnable[index].append(listIndex)
        nvicVectorEnable[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE", nvicMenu)
        nvicVectorEnable[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorEnable[index][listIndex].setLabel("Enable " + vDescription + " Interrupt")
        nvicVectorEnable[index][listIndex].setDefaultValue(vectorSettings[vector][0])
        nvicVectorEnable[index][listIndex].setDependencies(updateNVICVectorParametersValue, [vName + "_INTERRUPT_ENABLE"])

        nvicIntUpdateDepList.append("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE")

        nvicVectorNumber[index].append(listIndex)
        nvicVectorNumber[index][listIndex] = coreComponent.createIntegerSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_NUMBER", nvicVectorEnable[index][listIndex])
        nvicVectorNumber[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorNumber[index][listIndex].setLabel("Vector Number")
        nvicVectorNumber[index][listIndex].setDefaultValue(int(vIndex))
        nvicVectorNumber[index][listIndex].setVisible(False)

        # Following symbol is used in plib_nvic.c to generate the vector name to be passed into the NVIC APIs
        nvicVectorName[index].append(listIndex)
        nvicVectorName[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_VECTOR", nvicVectorEnable[index][listIndex])
        nvicVectorName[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorName[index][listIndex].setLabel("Vector Name")
        nvicVectorName[index][listIndex].setVisible(False)
        if ecia_module == None:
            nvicVectorName[index][listIndex].setDefaultValue(vName)
        else:
            nvicVectorName[index][listIndex].setDefaultValue(vectorDict.get("name"))

        # Following symbol is used in NVIC UI to populate the vector name column
        nvicVectorNameUI[index].append(listIndex)
        nvicVectorNameUI[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_VECTOR_NAME", nvicVectorEnable[index][listIndex])
        nvicVectorNameUI[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorNameUI[index][listIndex].setLabel("Vector Name UI")
        nvicVectorNameUI[index][listIndex].setVisible(False)
        nvicVectorNameUI[index][listIndex].setDefaultValue(vName)

        nvicVectorEnableLock[index].append(listIndex)
        nvicVectorEnableLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorEnableLock[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorEnableLock[index][listIndex].setLabel("Enable Lock")
        nvicVectorEnableLock[index][listIndex].setVisible(False)
        nvicVectorEnableLock[index][listIndex].setDefaultValue(vectorSettings[vector][1])

        nvicVectorEnableGenerate[index].append(listIndex)
        nvicVectorEnableGenerate[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE_GENERATE", nvicVectorEnable[index][listIndex])
        nvicVectorEnableGenerate[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorEnableGenerate[index][listIndex].setLabel("Enable Generate")
        nvicVectorEnableGenerate[index][listIndex].setVisible(False)
        nvicVectorEnableGenerate[index][listIndex].setDefaultValue(vectorSettings[vector][2])

        nvicVectorPriority[index].append(listIndex)
        nvicVectorPriority[index][listIndex] = coreComponent.createComboSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY", nvicVectorEnable[index][listIndex], priorityList)
        nvicVectorPriority[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPriority[index][listIndex].setLabel("Priority")
        nvicVectorPriority[index][listIndex].setDefaultValue(vectorSettings[vector][3])

        nvicVectorPriorityLock[index].append(index)
        nvicVectorPriorityLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorPriorityLock[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPriorityLock[index][listIndex].setLabel("Priority Lock")
        nvicVectorPriorityLock[index][listIndex].setVisible(False)
        nvicVectorPriorityLock[index][listIndex].setDefaultValue(vectorSettings[vector][4])

        nvicVectorPriorityGenerate[index].append(index)
        nvicVectorPriorityGenerate[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_PRIORITY_GENERATE", nvicVectorEnable[index][listIndex])
        nvicVectorPriorityGenerate[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPriorityGenerate[index][listIndex].setLabel("Priority Generate")
        nvicVectorPriorityGenerate[index][listIndex].setVisible(False)
        nvicVectorPriorityGenerate[index][listIndex].setDefaultValue(vectorSettings[vector][5])

        nvicVectorHandler[index].append(listIndex)
        nvicVectorHandler[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_HANDLER", nvicVectorEnable[index][listIndex])
        nvicVectorHandler[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorHandler[index][listIndex].setLabel("Handler")
        nvicVectorHandler[index][listIndex].setDefaultValue(vName + "_Handler")
        nvicVectorHandler[index][listIndex].setDependencies(updateNVICVectorParametersValue, [vName + "_INTERRUPT_HANDLER"])

        nvicVectorHandlerLock[index].append(listIndex)
        nvicVectorHandlerLock[index][listIndex] = coreComponent.createBooleanSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_HANDLER_LOCK", nvicVectorEnable[index][listIndex])
        nvicVectorHandlerLock[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorHandlerLock[index][listIndex].setLabel("Handler Lock")
        nvicVectorHandlerLock[index][listIndex].setVisible(False)
        nvicVectorHandlerLock[index][listIndex].setDefaultValue(vectorSettings[vector][6])
        nvicVectorHandlerLock[index][listIndex].setDependencies(updateNVICVectorParametersValue, [vName + "_INTERRUPT_HANDLER_LOCK"])
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            nvicSecurity = coreComponent.createKeyValueSetSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_SECURITY_TYPE", nvicVectorEnable[index][listIndex])
            nvicSecurity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
            nvicSecurity.setLabel("Interrupt Security mode")
            nvicSecurity.addKey("SECURE", "0", "False")
            nvicSecurity.addKey("NON-SECURE", "1", "True")
            nvicSecurity.setOutputMode("Key")
            nvicSecurity.setDisplayMode("Key")
            nvicSecurity.setVisible(True)
            nvicSecurity.setDefaultValue(0)
            nvicSecurity.setDependencies(updateSecurity, [vName + "_SET_NON_SECURE"])
        # only if multiple peripherals connected to same interrupt line
        if len(handlerList) > 1:

            nvicVectorGenericHandler[index].append(listIndex)
            nvicVectorGenericHandler[index][listIndex] = coreComponent.createStringSymbol("NVIC_" + str(vIndex) + "_" + str(listIndex) + "_GENERIC_HANDLER", nvicVectorEnable[index][listIndex])
            nvicVectorGenericHandler[index][listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
            nvicVectorGenericHandler[index][listIndex].setLabel("Generic Handler")
            nvicVectorGenericHandler[index][listIndex].setVisible(False)
            nvicVectorGenericHandler[index][listIndex].setDefaultValue(genericName + "_Handler")

        nvicVectorPeriEnableUpdate = coreComponent.createBooleanSymbol(vName + "_INTERRUPT_ENABLE_UPDATE", nvicMenu)
        nvicVectorPeriEnableUpdate.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:nvic;register:%NOREGISTER%")
        nvicVectorPeriEnableUpdate.setLabel("NVIC Peripheral Enable/Disable Update")
        nvicVectorPeriEnableUpdate.setVisible(False)
        nvicVectorPeriEnableUpdate.setDependencies(updateNVICVectorPeriEnableValue, ["NVIC_" + str(vIndex) + "_" + str(listIndex) + "_ENABLE"])

    index += 1

if ecia_module != None:
    nvicIntUpdate.setDependencies(NVIC_InterruptUpdate, nvicIntUpdateDepList)

if Database.getSymbolValue("core", "PERIPHERAL_MULTI_VECTOR") != None:

    # Components which are creating critical section
    corePeripherals = getCorePeripherals()

    modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()

    for module in range (0, len(modules)):
        periphName = str(modules[module].getAttribute("name"))
        if periphName in corePeripherals:
            instances = modules[module].getChildren()
            for instance in range (0, len(instances)):
                isMatched = False
                periphInstanceName = str(instances[instance].getAttribute("name"))
                moduleInstance = [dict for dict in nvicVectorDataStructure if periphInstanceName in dict["module-instance"]]
                if len(moduleInstance) > 1:
                    options = instances[instance].getChildren()
                    for option in range (0, len(options)):
                        parameters = options[option].getChildren()
                        for parameter in range(0, len(parameters)):
                            name = str(parameters[parameter].getAttribute("name"))
                            if "INT_SRC" in name:
                                isMatched = True
                                value = int(parameters[parameter].getAttribute("value"))
                                vectIndexes = [dict for dict in nvicVectorDataStructure if value == dict["index"]]
                                vectName = vectIndexes[0].get("name") + "_IRQn"
                                nvicVectorNumber = coreComponent.createStringSymbol(periphInstanceName + "_" + name, None)
                                nvicVectorNumber.setDefaultValue(vectName)
                                nvicVectorNumber.setVisible(False)

                if isMatched:
                    nvicMultiVector = coreComponent.createBooleanSymbol(periphInstanceName + "_MULTI_IRQn", None)
                    nvicMultiVector.setDefaultValue(True)
                    nvicMultiVector.setVisible(False)

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
nvicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
nvicSystemInitFile.setSourcePath("../peripheral/nvic/templates/system/initialization.c.ftl")
nvicSystemInitFile.setMarkup(True)

nvicSystemDefFile = coreComponent.createFileSymbol("NVIC_DEF", None)
nvicSystemDefFile.setType("STRING")
nvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
nvicSystemDefFile.setSourcePath("../peripheral/nvic/templates/system/definitions.h.ftl")
nvicSystemDefFile.setMarkup(True)

nvicSystemIntHandlerDeclsFile = coreComponent.createFileSymbol("NVIC_HANDLER_DECLS", None)
nvicSystemIntHandlerDeclsFile.setType("STRING")
nvicSystemIntHandlerDeclsFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_HANDLER_DECLS")
nvicSystemIntHandlerDeclsFile.setSourcePath("../peripheral/nvic/templates/system/interrupt_handlers_decls.h.ftl")
nvicSystemIntHandlerDeclsFile.setMarkup(True)

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

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    secnvicSystemIntMultipleHandleFile = coreComponent.createFileSymbol("SEC_NVIC_MULTIPLE_HANDLER", None)
    secnvicSystemIntMultipleHandleFile.setType("STRING")
    secnvicSystemIntMultipleHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_SECURE_MULTIPLE_HANDLERS")
    secnvicSystemIntMultipleHandleFile.setSourcePath("../peripheral/nvic/templates/system/trustZone/interrupts_multiple_handlers_secure.h.ftl")
    secnvicSystemIntMultipleHandleFile.setMarkup(True)

    secnvicSystemIntHandlerDeclsFile = coreComponent.createFileSymbol("SEC_NVIC_HANDLER_DECLS", None)
    secnvicSystemIntHandlerDeclsFile.setType("STRING")
    secnvicSystemIntHandlerDeclsFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_SECURE_HANDLER_DECLS")
    secnvicSystemIntHandlerDeclsFile.setSourcePath("../peripheral/nvic/templates/system/trustZone/interrupt_handlers_decls_secure.h.ftl")
    secnvicSystemIntHandlerDeclsFile.setMarkup(True)

    secnvicSystemIntWeakHandleFile = coreComponent.createFileSymbol("SEC_NVIC_INT_HANDLER", None)
    secnvicSystemIntWeakHandleFile.setType("STRING")
    secnvicSystemIntWeakHandleFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_SECURE_WEAK_HANDLERS")
    secnvicSystemIntWeakHandleFile.setSourcePath("../peripheral/nvic/templates/system/trustZone/interrupts_weak_handlers_secure.h.ftl")
    secnvicSystemIntWeakHandleFile.setMarkup(True)

    secnvicSystemIntTableFile = coreComponent.createFileSymbol("SEC_NVIC_INT_TABLE", None)
    secnvicSystemIntTableFile.setType("STRING")
    secnvicSystemIntTableFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_SECURE_HANDLERS")
    secnvicSystemIntTableFile.setSourcePath("../peripheral/nvic/templates/system/trustZone/interrupts_vector_table_secure.h.ftl")
    secnvicSystemIntTableFile.setMarkup(True)

    nonSecNvicHeaderFile = coreComponent.createFileSymbol("NONSEC_NVIC_HEADER", None)
    nonSecNvicHeaderFile.setType("HEADER")
    nonSecNvicHeaderFile.setSourcePath("../peripheral/nvic/templates/plib_nvic.h.ftl")
    nonSecNvicHeaderFile.setOutputName("plib_nvic.h")
    nonSecNvicHeaderFile.setDestPath("/peripheral/nvic/")
    nonSecNvicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
    nonSecNvicHeaderFile.setMarkup(True)

    nonSecNvicSourceFile = coreComponent.createFileSymbol("NONSEC_NVIC_SOURCE", None)
    nonSecNvicSourceFile.setType("SOURCE")
    nonSecNvicSourceFile.setSourcePath("../peripheral/nvic/templates/trustZone/plib_nvic.c.ftl")
    nonSecNvicSourceFile.setOutputName("plib_nvic.c")
    nonSecNvicSourceFile.setDestPath("/peripheral/nvic/")
    nonSecNvicSourceFile.setProjectPath("config/" + configName + "/peripheral/nvic/")
    nonSecNvicSourceFile.setMarkup(True)

    nonSecNvicSystemInitFile = coreComponent.createFileSymbol("NONSEC_NVIC_INIT", None)
    nonSecNvicSystemInitFile.setType("STRING")
    nonSecNvicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
    nonSecNvicSystemInitFile.setSourcePath("../peripheral/nvic/templates/system/initialization.c.ftl")
    nonSecNvicSystemInitFile.setMarkup(True)

    nonSecNvicSystemDefFile = coreComponent.createFileSymbol("NINSEC_NVIC_DEF", None)
    nonSecNvicSystemDefFile.setType("STRING")
    nonSecNvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nonSecNvicSystemDefFile.setSourcePath("../peripheral/nvic/templates/system/definitions.h.ftl")
    nonSecNvicSystemDefFile.setMarkup(True)

    nvicHeaderFile.setSecurity("SECURE")
    nvicSourceFile.setSecurity("SECURE")
    nvicSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_INTERRUPTS")
    nvicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")