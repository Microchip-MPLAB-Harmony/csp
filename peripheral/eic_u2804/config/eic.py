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
import re

global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock =[]
global EICfilesArray
global InterruptVectorSecurity
InterruptVectorSecurity = []
global interruptSecurityState
interruptSecurityState = []
EICfilesArray = []
global eicInstanceName
global intPrev
intPrev = 0
global secPrev
secPrev = 0
global evsys_generatorsNamesList
evsys_generatorsNamesList = []
global has_digits
###################################################################################################
######################################### Callbacks ###############################################
###################################################################################################

global DEBOUNCEN_Code

def eicEvsysGeneratorNamesPopulate(instanceName):
    global evsys_generatorsNamesList

    generatorNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators")
    generatorValues = generatorNode.getChildren()
    for id in range(0, len(generatorNode.getChildren())):
        if generatorValues[id].getAttribute("module-instance") == instanceName:
            evsys_generatorsNamesList.append(generatorValues[id].getAttribute("name"))

def eicEvsysGenNameGet(genNameMatchList):
    global evsys_generatorsNamesList

    for genName in evsys_generatorsNamesList:
        if all ( x in genName for x in genNameMatchList):
            return genName

def getValueGroupNode__EIC(module_name, register_group, register_name, bitfield_name , mode = None):
    bitfield_node_path = ""
    value_group_node = None

    if mode != None:
        bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[modes=\"{2}\",name=\"{3}\"]/bitfield@[name=\"{4}\"]".format(module_name, register_group, mode, register_name, bitfield_name)
    else:
         bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[name=\"{2}\"]/bitfield@[name=\"{3}\"]".format(module_name, register_group, register_name, bitfield_name)

    print (bitfield_node_path)
    bitfield_node = ATDF.getNode(bitfield_node_path)

    if bitfield_node != None:
        if bitfield_node.getAttribute("values") == None:
            print (register_name + "_" + bitfield_name + "does not have value-group attribute")
        else:
            value_group_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"{0}\"]/value-group@[name=\"{1}\"]".format(module_name, bitfield_node.getAttribute("values")))
            if value_group_node == None:
                print ("value-group = " + bitfield_node.getAttribute("values") + " not defined")
    else:
        print ("bitfield_name = " + bitfield_name + " not found" )

    return value_group_node

def confMenu(symbol, event):

    if event["id"] == "NMI_CTRL":

        Database.clearSymbolValue("core", NMIInterruptHandler)

        if event["value"] == True:
            Database.setSymbolValue("core", NMIInterruptHandler, "NMI_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", NMIInterruptHandler, "NonMaskableInt_Handler", 2)

    symbol.setVisible(event["value"])

def codeGenerationForEVCCTRL_EXTINTEO(symbol, event):
    global extIntCount
    isEVCTL = False
    if symbol.getID() == "EIC_EXTINTEO":
        isEVCTL = True
    channel = int(event["id"].split("_")[2])
    evsysGenName = eicEvsysGenNameGet(["EXTINT", str(channel)])
    if Database.getSymbolValue(event["namespace"], "EIC_CHAN_" + str(channel)):
        if not str(event["id"]).startswith("EIC_CHAN_"):
            if(event["value"] == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
                if isEVCTL:
                    Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", True, 2)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
                if isEVCTL:
                    Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", False, 2)
        else:
            parameter = symbol.getID().split("EIC_")[1]
            if(Database.getSymbolValue(event["namespace"], "EIC_" + str(parameter) + "_" + str(channel)) == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
                if isEVCTL:
                    Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", True, 2)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
                if isEVCTL:
                    Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", False, 2)

    else:
        symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
        if isEVCTL:
            Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", False, 2)

def fileGenLogic(symbol, event):
    global EICfilesArray
    global eicInstanceName

    overallSecurity = "NON_SECURE"

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
            if Database.getSymbolValue(event["namespace"], "IS_EIC_NONSEC") == True:
                overallSecurity = "NON_SECURE"
            else:
                overallSecurity = "SECURE"


    print (overallSecurity)

    if (int(Database.getSymbolValue(event["namespace"], "EIC_NONSEC")) > 0 or int(Database.getSymbolValue(event["namespace"], "NMI_IS_NON_SECURE")) == 1) and (overallSecurity == "NON_SECURE"):
        EICfilesArray[0].setEnabled(True)
        EICfilesArray[1].setEnabled(True)
        EICfilesArray[2].setEnabled(True)
        EICfilesArray[3].setEnabled(True)
    else:
        EICfilesArray[0].setEnabled(False)
        EICfilesArray[1].setEnabled(False)
        EICfilesArray[2].setEnabled(False)
        EICfilesArray[3].setEnabled(False)

    print ("Enable status = " + str(EICfilesArray[0].getEnabled()))

def updateEicInterruptSecurity(symbol, event):
    global InterruptVectorSecurity
    global interruptSecurityState
    import math
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global secPrev
    global extIntCount
    if "EIC_NONSEC" in event["id"]:
        Database.setSymbolValue(event["namespace"], "EIC_NUM_NONSEC_CHANNEL", (bin(event["value"])[2:]).count('1'))
        value = event["value"] ^ secPrev
        if value > 0:
            bitPos = int(math.log(value, 2))
            if sharedVector:
                if bitPos < len(InterruptVector) - 1:
                    #for TrustZone
                    if Database.getSymbolValue(event["namespace"], "EIC_NONSEC_" + str(bitPos)) != None:
                        if Database.getSymbolValue(event["namespace"], "EIC_NONSEC_" + str(bitPos)) == 0:
                            Database.setSymbolValue("core", InterruptVectorSecurity[bitPos], False)
                            interruptSecurityState[bitPos] = False
                        else:
                            Database.setSymbolValue("core", InterruptVectorSecurity[bitPos], True)
                            interruptSecurityState[bitPos] = True

                else:
                    nonsecureInterrupt = False
                    for i in range(extIntCount - len(InterruptVector) - 2, extIntCount):
                        if Database.getSymbolValue(event["namespace"], "EIC_CHAN_" + str(i)):
                            if Database.getSymbolValue(event["namespace"], "EIC_NONSEC_" + str(i)) == 0:
                                nonsecureInterrupt = False
                                break
                            else:
                                nonsecureInterrupt = True
                    interruptSecurityState[(len(InterruptVector) - 1)] = nonsecureInterrupt
                    Database.setSymbolValue("core", InterruptVectorSecurity[(len(InterruptVector) - 1)], nonsecureInterrupt)
                    Database.setSymbolValue(event["namespace"], "EIC_OTHER_HANDLER_IS_NON_SEC", nonsecureInterrupt)
            else:
                result = bool(event["value"] & (1<<bitPos))
                Database.setSymbolValue("core", InterruptVectorSecurity[bitPos], result)
                interruptSecurityState[bitPos] = result
        secPrev = event["value"]
    else:
        bitPos = int (event["id"].split("EIC_CHAN_")[1])
        if sharedVector:
            if bitPos >= len(InterruptVector) - 1:
                nonsecureInterrupt = False
                for i in range(extIntCount - len(InterruptVector) - 2, extIntCount):
                    if Database.getSymbolValue(event["namespace"], "EIC_CHAN_" + str(i)):
                        if Database.getSymbolValue(event["namespace"], "EIC_NONSEC_" + str(i)) == 0:
                            nonsecureInterrupt = False
                            break
                        else:
                            nonsecureInterrupt = True
                interruptSecurityState[(len(InterruptVector) - 1)] = nonsecureInterrupt
                Database.setSymbolValue("core", InterruptVectorSecurity[(len(InterruptVector) - 1)], nonsecureInterrupt)
                Database.setSymbolValue(event["namespace"], "EIC_OTHER_HANDLER_IS_NON_SEC", nonsecureInterrupt)

def updateEICInterruptStatus(symbol, event):
    import math
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global intPrev
    global extIntCount
    if len(InterruptVector) == 1:
        Database.setSymbolValue("core", InterruptVector[0], bool(event["value"]), 2)
        Database.setSymbolValue("core", InterruptHandlerLock[0], bool(event["value"]), 2)
        if bool(event["value"]) == True:
            Database.setSymbolValue("core", InterruptHandler[0], InterruptHandler[0].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptHandler[0], InterruptHandler[0].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)
    else:
        value = event["value"] ^ intPrev
        if value > 0:
            bitPos = int(math.log(value, 2))
            if sharedVector:
                if bitPos < len(InterruptVector) - 1:
                    result = bool(event["value"] & (1<<bitPos))
                    Database.setSymbolValue("core", InterruptVector[bitPos], result, 2)
                    Database.setSymbolValue("core", InterruptHandlerLock[bitPos], result, 2)
                    if result:
                        Database.setSymbolValue("core", InterruptHandler[bitPos], InterruptHandler[bitPos].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)
                    else:
                        Database.setSymbolValue("core", InterruptHandler[bitPos], InterruptHandler[bitPos].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)
                else:
                    result = event["value"] > (1 << (len(InterruptVector) - 2))
                    Database.setSymbolValue("core", InterruptVector[(len(InterruptVector) - 1)], result, 2)
                    Database.setSymbolValue("core", InterruptHandlerLock[(len(InterruptVector) - 1)], result, 2)
                    Database.setSymbolValue(event["namespace"], "EIC_OTHER_HANDLER_ACTIVE", result, 2)
                    if result:
                        Database.setSymbolValue("core", InterruptHandler[(len(InterruptVector) - 1)], "EIC_OTHER_InterruptHandler", 2)
                    else:
                        Database.setSymbolValue("core", InterruptHandler[(len(InterruptVector) - 1)], "EIC_OTHER_Handler", 2)
            else:
                result = bool(event["value"] & (1<<bitPos))
                Database.setSymbolValue("core", InterruptVector[bitPos], result, 2)
                Database.setSymbolValue("core", InterruptHandlerLock[bitPos], result, 2)
                if result:
                    Database.setSymbolValue("core", InterruptHandler[bitPos], InterruptHandler[bitPos].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)
                else:
                    Database.setSymbolValue("core", InterruptHandler[bitPos], InterruptHandler[bitPos].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)
        intPrev = event["value"]
def updateEICInterruptWarringStatus(symbol, event):

    if EXTINT_Code.getValue() != 0x0:
        symbol.setVisible(event["value"])

def updateEICClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def debounceEnable(symbol, event):
    global DEBOUNCEN_Code
    channel = int(event["id"].split("_")[3])
    if event["value"] == 1 or  event["value"] == 2 or event["value"] == 3:
        symbol.setVisible(True)
        if(Database.getSymbolValue(event["namespace"], "EIC_DEBOUNCEN_" + str(channel)) == True):
            DEBOUNCEN_Code.setValue((DEBOUNCEN_Code.getValue()) | (0x1 << channel), 1)
        else:
            DEBOUNCEN_Code.setValue((DEBOUNCEN_Code.getValue()) & (~(0x1 << channel)), 1)
    else:
        symbol.setVisible(False)
        DEBOUNCEN_Code.setValue((DEBOUNCEN_Code.getValue()) & (~(0x1 << channel)), 1)

def debounceMenu(symbol, event):
    if int(event["value"] > 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def filterMenu(symbol, event):
    symbol.setVisible((event["value"] > 0))

def eicIsNonsecUpdate(symbol, event):
    symbol.setValue(event["value"])

def eicSecurityModeVisibility(symbol, event):
    #If the EIC is configured as Non Secure in TZ manager, then show the inidividual EIC pin Security configuration for mixed secure behavior
    if event["value"] == True:
        symbol.setReadOnly(False)
    else:
        symbol.setReadOnly(True)
        symbol.setSelectedKey("SECURE")

def has_digits(string):
    res = re.compile('\d').search(string)
    return res is not None
###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(eicComponent):
    eicSym_eventsList = []
    eicSym_asynchList = []
    eicSym_debounceList =[]
    eicSym_InterruptList = []
    eicSym_Channel = []
    eicSym_nonSecList = []
    global DEBOUNCEN_Code
    global EXTINT_Code
    global eicInstanceName
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global NMIInterruptHandler
    global numInt
    global extIntCount
    global sharedVector
    InterruptVectorUpdate = []

    eicTickOnNode = getValueGroupNode__EIC("EIC", "EIC", "DPRESCALER", "TICKON")

    debounceSupported = eicComponent.createBooleanSymbol("DEBOUNCE_SUPPORT", None)
    if eicTickOnNode != None:
        debounceSupported.setDefaultValue(True)
    debounceSupported.setVisible(False)

    eicInstanceName = eicComponent.createStringSymbol("EIC_INSTANCE_NAME", None)
    eicInstanceName.setVisible(False)
    eicInstanceName.setDefaultValue(eicComponent.getID().upper())

    eicEvsysGeneratorNamesPopulate(eicInstanceName.getValue())

    #clock enable
    Database.clearSymbolValue("core", eicInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", eicInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    extIntNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EIC\"]/instance@[name=\""+eicInstanceName.getValue()+"\"]/parameters/param@[name=\"EXTINT_NUM\"]")
    extIntCount = int(extIntNode.getAttribute("value"))
    eicSym_IntCount = eicComponent.createIntegerSymbol("EIC_INT_COUNT" , None)
    eicSym_IntCount.setDefaultValue(extIntCount)
    eicSym_IntCount.setVisible(False)

    # CTRLA - Clock Selection
    CTRLA_CKSEL_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_CLKSEL" , None)
    CTRLA_CKSEL_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:%NOREGISTER%")
    CTRLA_CKSEL_SelectionSymbol.setLabel("EIC Clock Source Selection")

    eicClkselNode = getValueGroupNode__EIC("EIC", "EIC", "CTRLA", "CKSEL")

    for index in range(len(eicClkselNode.getChildren())):
        eicClkselKeyName = eicClkselNode.getChildren()[index].getAttribute("name")
        eicClkselKeyDescription = eicClkselNode.getChildren()[index].getAttribute("caption")
        eicClkselKeyValue = eicClkselNode.getChildren()[index].getAttribute("value")
        CTRLA_CKSEL_SelectionSymbol.addKey(eicClkselKeyName, eicClkselKeyValue , eicClkselKeyDescription)

    CTRLA_CKSEL_SelectionSymbol.setDefaultValue(0)
    CTRLA_CKSEL_SelectionSymbol.setOutputMode("Value")
    CTRLA_CKSEL_SelectionSymbol.setDisplayMode("Description")

    #Non-Maskable Interrupt Control

    eicPLX4 = eicComponent.createBooleanSymbol("NMI_CTRL", None)
    eicPLX4.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:CTRL")
    eicPLX4.setLabel("Non Maskable Interrupt Control")

    nmiConfMenu = eicComponent.createMenuSymbol("NMI_MENU", eicPLX4)
    nmiConfMenu.setLabel("NMI Configuration")
    nmiConfMenu.setDependencies(confMenu, ["NMI_CTRL"])
    nmiConfMenu.setVisible(False)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
            eicIsNonsec = eicComponent.createBooleanSymbol("IS_EIC_NONSEC", None)
            eicIsNonsec.setVisible(False)
            eicIsNonsec.setDefaultValue(Database.getSymbolValue("core", eicInstanceName.getValue() + "_IS_NON_SECURE"))
            eicIsNonsec.setDependencies(eicIsNonsecUpdate, ["core." + eicInstanceName.getValue() + "_IS_NON_SECURE"])

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        nmiSecurity = eicComponent.createKeyValueSetSymbol("NMI_IS_NON_SECURE", nmiConfMenu)
        nmiSecurity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:NONSEC")
        nmiSecurity.setLabel("Security mode")
        nmiSecurity.addKey("SECURE", "0", "False")
        nmiSecurity.addKey("NON-SECURE", "1", "True")
        nmiSecurity.setOutputMode("Key")
        nmiSecurity.setDisplayMode("Key")
        nmiSecurity.setDefaultValue(0)
        if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
            nmiSecurity.setDependencies(eicSecurityModeVisibility, ["IS_EIC_NONSEC"])
            nmiSecurity.setReadOnly(eicIsNonsec.getValue() == False)

    #NMIASYNCH
    NMI_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("NMI_ASYNCH" , nmiConfMenu)
    NMI_ASYNCH_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:NMICTRL")
    NMI_ASYNCH_Selection.setLabel("NMI Detection Clock")

    eicNMIAsyncNode = getValueGroupNode__EIC("EIC", "EIC", "NMICTRL", "NMIASYNCH")
    eicNMIAsyncValues = []
    eicNMIAsyncValues = eicNMIAsyncNode.getChildren()

    for index in range(len(eicNMIAsyncNode.getChildren())):
        eicNMIAsyncKeyName = eicNMIAsyncNode.getChildren()[index].getAttribute("name")
        eicNMIAsyncKeyDescription = eicNMIAsyncNode.getChildren()[index].getAttribute("caption")
        eicNMIAsyncKeyValue = eicNMIAsyncNode.getChildren()[index].getAttribute("value")
        NMI_ASYNCH_Selection.addKey(eicNMIAsyncKeyName, eicNMIAsyncKeyValue , eicNMIAsyncKeyDescription)

    NMI_ASYNCH_Selection.setDefaultValue(0)
    NMI_ASYNCH_Selection.setOutputMode("Value")
    NMI_ASYNCH_Selection.setDisplayMode("Description")

    #NMIFILTEN
    NMI_FILTEN_Selection = eicComponent.createBooleanSymbol("NMI_FILTEN" , nmiConfMenu)
    NMI_FILTEN_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:NMICTRL")
    NMI_FILTEN_Selection.setLabel("Enable filter")

    # NMI - SENSE
    NMI_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("NMI_SENSE" , nmiConfMenu)
    NMI_SENSE_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:NMICTRL")
    NMI_SENSE_SelectionSymbol.setLabel("NMI Interrupt Edge Selection")

    eicNMISenseNode = getValueGroupNode__EIC("EIC", "EIC", "NMICTRL", "NMISENSE")

    for index in range(len(eicNMISenseNode.getChildren())):
        eicNMISenseKeyName = eicNMISenseNode.getChildren()[index].getAttribute("name")
        eicNMISenseKeyDescription = eicNMISenseNode.getChildren()[index].getAttribute("caption")
        eicNMISenseKeyValue = eicNMISenseNode.getChildren()[index].getAttribute("value")
        NMI_SENSE_SelectionSymbol.addKey(eicNMISenseKeyName, eicNMISenseKeyValue , eicNMISenseKeyDescription)

    NMI_SENSE_SelectionSymbol.setDefaultValue(0)
    NMI_SENSE_SelectionSymbol.setOutputMode("Key")
    NMI_SENSE_SelectionSymbol.setDisplayMode("Description")

    configRegArrBased = eicComponent.createBooleanSymbol("EIC_CONFIG_REG_ARR_BASED" , None)
    configRegArrBased.setVisible(False)

    config_reg_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/register-group@[name=\"EIC\"]/register@[name=\"CONFIG\"]")
    if config_reg_node != None and config_reg_node.getAttribute("count") != None and int(config_reg_node.getAttribute("count")) > 1:
        configRegArrBased.setDefaultValue(True)
    else:
        configRegArrBased.setDefaultValue(False)

    #Interrupt 0 - EXTINT Settings
    for extIntIndex in range(0 , extIntCount):

        eicPLX1 = eicComponent.createBooleanSymbol("EIC_CHAN_" + str(extIntIndex) , None)
        eicPLX1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:%NOREGISTER%")
        eicPLX1.setLabel("Enable EIC Channel" + str(extIntIndex))

        eicConfiguration = eicComponent.createMenuSymbol("EIC_MENU" + str(extIntIndex), eicPLX1)
        eicConfiguration.setLabel("EIC Channel" + str(extIntIndex) + " Configuration")
        eicConfiguration.setDependencies(confMenu, ["EIC_CHAN_" + str(extIntIndex)])
        eicConfiguration.setVisible(False)

        # populate a list with IDs for code generation dependency
        eicSym_Channel.append("EIC_CHAN_" + str(extIntIndex))

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            eicSecurity = eicComponent.createKeyValueSetSymbol("EIC_NONSEC_" + str(extIntIndex), eicConfiguration)
            eicSecurity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:NONSEC")
            eicSecurity.setLabel("Security mode")
            eicSecurity.addKey("SECURE", "0", "False")
            eicSecurity.addKey("NON-SECURE", "1", "True")
            eicSecurity.setOutputMode("Key")
            eicSecurity.setDisplayMode("Key")
            eicSecurity.setDefaultValue(0)
            eicSym_nonSecList.append("EIC_NONSEC_" + str(extIntIndex))
            if Database.getSymbolValue("core", "CONFIG_OVERALL_SEC_TO_NONSEC_FOR_MIXSEC") != None:
                eicSecurity.setDependencies(eicSecurityModeVisibility, ["IS_EIC_NONSEC"])
                eicSecurity.setReadOnly(eicIsNonsec.getValue() == False)

        eicINT = eicComponent.createBooleanSymbol("EIC_INT_" + str(extIntIndex) , eicConfiguration)
        eicINT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:CTRLA")
        eicINT.setLabel("Enable Interrupt")
        eicSym_InterruptList.append("EIC_INT_" + str(extIntIndex))

        #EVCTRL - External Interrupt Event Output Enable 0..7/15 Channel number
        EVCCTRL_EXTINTEO_Selection = eicComponent.createBooleanSymbol("EIC_EXTINTEO_" + str(extIntIndex) , eicConfiguration)
        EVCCTRL_EXTINTEO_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:%NOREGISTER%")
        EVCCTRL_EXTINTEO_Selection.setLabel("Enable Event Output")

        # populate a list with IDs for code generation dependency
        eicSym_eventsList.append("EIC_EXTINTEO_" + str(extIntIndex))

        #ASYNCH
        ASYNCH_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("EIC_ASYNCH_" + str(extIntIndex) , eicConfiguration)
        ASYNCH_ASYNCH_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:ASYNCH")
        ASYNCH_ASYNCH_Selection.setLabel("External Interrupt" + str(extIntIndex) + " Detection Clock")

        eicAsynchNode = getValueGroupNode__EIC("EIC", "EIC", "ASYNCH", "ASYNCH")
        if eicAsynchNode == None:
            eicAsynchNode = getValueGroupNode__EIC("EIC", "EIC", "ASYNCH", "ASYNCH0")

        for index in range(len(eicAsynchNode.getChildren())):
            eicAsynchKeyName = eicAsynchNode.getChildren()[index].getAttribute("name")
            eicAsynchKeyDescription = eicAsynchNode.getChildren()[index].getAttribute("caption")
            eicAsynchKeyValue = eicAsynchNode.getChildren()[index].getAttribute("value")
            ASYNCH_ASYNCH_Selection.addKey(eicAsynchKeyName, eicAsynchKeyValue , eicAsynchKeyDescription)

        ASYNCH_ASYNCH_Selection.setDefaultValue(0)
        ASYNCH_ASYNCH_Selection.setOutputMode("Value")
        ASYNCH_ASYNCH_Selection.setDisplayMode("Description")

        # populate a list with IDs for code generation dependency
        eicSym_asynchList.append("EIC_ASYNCH_" + str(extIntIndex))

        #CONFIG - Sense Enable
        CONFIG_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_CONFIG_SENSE_" + str(extIntIndex) , eicConfiguration)
        CONFIG_SENSE_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:CONFIG")
        CONFIG_SENSE_SelectionSymbol.setLabel("External Interrupt" + str(extIntIndex) + " Edge Selection")

        if configRegArrBased.getValue() == True or extIntCount < 9:
            eicConfigSenseNode = getValueGroupNode__EIC("EIC", "EIC", "CONFIG", "SENSE0")
        else:
            eicConfigSenseNode = getValueGroupNode__EIC("EIC", "EIC", "CONFIG0", "SENSE0")

        for index in range(len(eicConfigSenseNode.getChildren())):
            eicConfigSenseKeyName = eicConfigSenseNode.getChildren()[index].getAttribute("name")
            eicConfigSenseKeyDescription = eicConfigSenseNode.getChildren()[index].getAttribute("caption")
            eicConfigSenseKeyValue = eicConfigSenseNode.getChildren()[index].getAttribute("value")
            CONFIG_SENSE_SelectionSymbol.addKey(eicConfigSenseKeyName, eicConfigSenseKeyValue , eicConfigSenseKeyDescription)

        CONFIG_SENSE_SelectionSymbol.setDefaultValue(0)
        CONFIG_SENSE_SelectionSymbol.setOutputMode("Key")
        CONFIG_SENSE_SelectionSymbol.setDisplayMode("Description")

        if debounceSupported.getValue():
            #DEBOUNCEN
            DEBOUNCEN_Selection = eicComponent.createBooleanSymbol("EIC_DEBOUNCEN_" + str(extIntIndex) , eicConfiguration)
            DEBOUNCEN_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DEBOUNCEN")
            DEBOUNCEN_Selection.setLabel("Enable Debounce")
            DEBOUNCEN_Selection.setVisible(False)
            DEBOUNCEN_Selection.setDependencies(debounceEnable,["EIC_CONFIG_SENSE_" + str(extIntIndex)])

        #CONFIG - Filter Enable
        CONFIG_FILTER_Selection = eicComponent.createBooleanSymbol("EIC_CONFIG_FILTEN_" + str(extIntIndex) , eicConfiguration)
        CONFIG_FILTER_Selection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:CONFIG")
        CONFIG_FILTER_Selection.setLabel("Enable filter")
        CONFIG_FILTER_Selection.setVisible(False)
        CONFIG_FILTER_Selection.setDependencies(filterMenu, ["EIC_CONFIG_SENSE_" + str(extIntIndex)])
        # populate a list with IDs for code generation dependency
        eicSym_debounceList.append("EIC_DEBOUNCEN_" + str(extIntIndex))



################################################################################
################### Business Logic calls for generating code ###################
################################################################################

    eicSym_debounceList.extend(eicSym_Channel)
    eicSym_eventsList.extend(eicSym_Channel)
    eicSym_asynchList.extend(eicSym_Channel)
    eicSym_InterruptList.extend(eicSym_Channel)
    eicSym_nonSecList.extend(eicSym_Channel)

    eicCalculation = eicComponent.createMenuSymbol("REG_MENU", None)
    eicCalculation.setVisible(False)
    eicCalculation.setLabel("Calculated register values")

    EVCCTRL_EXTINTEO_Code = eicComponent.createHexSymbol("EIC_EXTINTEO" , eicCalculation)
    EVCCTRL_EXTINTEO_Code.setDefaultValue(0)
    EVCCTRL_EXTINTEO_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_eventsList)

    ASYNCH_Code = eicComponent.createHexSymbol("EIC_ASYNCH" , eicCalculation)
    ASYNCH_Code.setDefaultValue(0)
    ASYNCH_Code.setVisible(False)
    ASYNCH_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_asynchList)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        nonSecReg = eicComponent.createHexSymbol("EIC_NONSEC" , eicCalculation)
        nonSecReg.setDefaultValue(0)
        nonSecReg.setVisible(True)
        nonSecReg.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_nonSecList)

        nonSecChannel = eicComponent.createIntegerSymbol("EIC_NUM_NONSEC_CHANNEL" , eicCalculation)
        nonSecChannel.setDefaultValue(0)
        nonSecChannel.setVisible(True)

    if debounceSupported.getValue():
        DEBOUNCEN_Code = eicComponent.createHexSymbol("EIC_DEBOUNCEN" , eicCalculation)
        DEBOUNCEN_Code.setDefaultValue(0)
        DEBOUNCEN_Code.setVisible(False)
        DEBOUNCEN_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_debounceList)

    EXTINT_Code = eicComponent.createHexSymbol("EIC_INT" , eicCalculation)
    EXTINT_Code.setDefaultValue(0)
    EXTINT_Code.setVisible(False)
    EXTINT_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_InterruptList)

    eicDebounceMenu = eicComponent.createMenuSymbol("DEBOUNCE_MENU", None)
    eicDebounceMenu.setLabel("Debouncer Configuration")
    eicDebounceMenu.setVisible(False)
    if debounceSupported.getValue():
        eicDebounceMenu.setDependencies(debounceMenu, ["EIC_DEBOUNCEN"])

        #DEBOUNCER - TICKON
        PRESCALER_TICKON_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_PRESCALER_TICKON" , eicDebounceMenu)
        PRESCALER_TICKON_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DPRESCALER")
        PRESCALER_TICKON_SelectionSymbol.setLabel("Debouncer Sampler Clock Source")

        for index in range(len(eicTickOnNode.getChildren())):
            eicTickOnKeyName = eicTickOnNode.getChildren()[index].getAttribute("name")
            eicTickOnKeyDescription = eicTickOnNode.getChildren()[index].getAttribute("caption")
            eicTickOnKeyValue = eicTickOnNode.getChildren()[index].getAttribute("value")
            PRESCALER_TICKON_SelectionSymbol.addKey(eicTickOnKeyName, eicTickOnKeyValue , eicTickOnKeyDescription)

        PRESCALER_TICKON_SelectionSymbol.setDefaultValue(0)
        PRESCALER_TICKON_SelectionSymbol.setOutputMode("Value")
        PRESCALER_TICKON_SelectionSymbol.setDisplayMode("Description")

        #DEBOUNCER - Number of States x (7:0)
        DEBOUNCER_NO_STATES_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_NO_STATES_0" , eicDebounceMenu)
        DEBOUNCER_NO_STATES_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DPRESCALER")
        DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States for EXTINT[7:0]")

        eicStatesxNode = getValueGroupNode__EIC("EIC", "EIC", "DPRESCALER", "STATES0")

        for index in range(len(eicStatesxNode.getChildren())):
            eicStatesxKeyName = eicStatesxNode.getChildren()[index].getAttribute("name")
            eicStatesxKeyDescription = eicStatesxNode.getChildren()[index].getAttribute("caption")
            eicStatesxKeyValue = eicStatesxNode.getChildren()[index].getAttribute("value")
            DEBOUNCER_NO_STATES_SelectionSymbol.addKey(eicStatesxKeyName, eicStatesxKeyValue , eicStatesxKeyDescription)

        DEBOUNCER_NO_STATES_SelectionSymbol.setDefaultValue(0)
        DEBOUNCER_NO_STATES_SelectionSymbol.setOutputMode("Value")
        DEBOUNCER_NO_STATES_SelectionSymbol.setDisplayMode("Description")

        #BOUNCER - Prescaler x (7:0)
        DEBOUNCER_PRESCALER_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_PRESCALER_0" , eicDebounceMenu)
        DEBOUNCER_PRESCALER_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DPRESCALER")
        DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[7:0]")

        eicPrescalerNode = getValueGroupNode__EIC("EIC", "EIC", "DPRESCALER", "PRESCALER0")

        for index in range(len(eicPrescalerNode.getChildren())):
            eicPrescalerKeyName = eicPrescalerNode.getChildren()[index].getAttribute("name")
            eicPrescalerKeyDescription = eicPrescalerNode.getChildren()[index].getAttribute("caption")
            eicPrescalerKeyValue = eicPrescalerNode.getChildren()[index].getAttribute("value")
            DEBOUNCER_PRESCALER_SelectionSymbol.addKey(eicPrescalerKeyName, eicPrescalerKeyValue , eicPrescalerKeyDescription)

        DEBOUNCER_PRESCALER_SelectionSymbol.setDefaultValue(0)
        DEBOUNCER_PRESCALER_SelectionSymbol.setOutputMode("Value")
        DEBOUNCER_PRESCALER_SelectionSymbol.setDisplayMode("Description")

        eicStatesxNode = getValueGroupNode__EIC("EIC", "EIC", "DPRESCALER", "STATES1")

        if eicStatesxNode != None:
            #DEBOUNCER - Number of States x (8:15)
            DEBOUNCER_NO_STATES_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_NO_STATES_1" , eicDebounceMenu)
            DEBOUNCER_NO_STATES_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DPRESCALER")
            DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States Duration for EXTINT[15:8]")

            for index in range(len(eicStatesxNode.getChildren())):
                eicStatesxKeyName = eicStatesxNode.getChildren()[index].getAttribute("name")
                eicStatesxKeyDescription = eicStatesxNode.getChildren()[index].getAttribute("caption")
                eicStatesxKeyValue = eicStatesxNode.getChildren()[index].getAttribute("value")
                DEBOUNCER_NO_STATES_SelectionSymbol.addKey(eicStatesxKeyName, eicStatesxKeyValue , eicStatesxKeyDescription)

            DEBOUNCER_NO_STATES_SelectionSymbol.setDefaultValue(0)
            DEBOUNCER_NO_STATES_SelectionSymbol.setOutputMode("Value")
            DEBOUNCER_NO_STATES_SelectionSymbol.setDisplayMode("Description")

            #BOUNCER - Prescaler x (8:15)
            DEBOUNCER_PRESCALER_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_PRESCALER_1" , eicDebounceMenu)
            DEBOUNCER_PRESCALER_SelectionSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:eic_u2804;register:DPRESCALER")
            DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[15:8]")

            eicPrescalerNode = getValueGroupNode__EIC("EIC", "EIC", "DPRESCALER", "PRESCALER1")

            for index in range(len(eicPrescalerNode.getChildren())):
                eicPrescalerKeyName = eicPrescalerNode.getChildren()[index].getAttribute("name")
                eicPrescalerKeyDescription = eicPrescalerNode.getChildren()[index].getAttribute("caption")
                eicPrescalerKeyValue = eicPrescalerNode.getChildren()[index].getAttribute("value")
                DEBOUNCER_PRESCALER_SelectionSymbol.addKey(eicPrescalerKeyName, eicPrescalerKeyValue , eicPrescalerKeyDescription)

            DEBOUNCER_PRESCALER_SelectionSymbol.setDefaultValue(0)
            DEBOUNCER_PRESCALER_SelectionSymbol.setOutputMode("Value")
            DEBOUNCER_PRESCALER_SelectionSymbol.setDisplayMode("Description")

    ############################################################################
    #### Dependency ####
    ############################################################################
    eicDedicatedVectors = 0
    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues=vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == "EIC":
            name=vectorValues[id].getAttribute("name")

            if has_digits(name) == True:
                eicChannel = re.sub("[^0-9]", "", name)        #Extract the EIC channel number from the vector name
                eicDedicatedVectors += 1
            else:
                eicChannel = name                               # When vector name is OTHER or NSCHK or just EIC in case of single vector line
            eicIntHandlerName = eicComponent.createStringSymbol("EIC_INT_HANDLER_NAME_" + str(eicChannel) , None)
            eicIntHandlerName.setDefaultValue(name)
            eicIntHandlerName.setVisible(False)

            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")
            InterruptVectorSecurity.append(name + "_SET_NON_SECURE")
            interruptSecurityState.append(False)

    eicIntLines = eicComponent.createIntegerSymbol("NUM_INT_LINES", None)
    eicIntLines.setVisible(False)
    eicIntLines.setDefaultValue(eicDedicatedVectors)

    sharedVector = False
    if (len(InterruptVector) < extIntCount):
        sharedVector = True
        eicOtherHandler = eicComponent.createBooleanSymbol("EIC_OTHER_HANDLER_ACTIVE", None)
        eicOtherHandler.setVisible(False)
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            eicOtherHandlerNonSec = eicComponent.createBooleanSymbol("EIC_OTHER_HANDLER_IS_NON_SEC", None)
            eicOtherHandlerNonSec.setVisible(False)

    NMIInterruptHandler = "NonMaskableInt_INTERRUPT_HANDLER"

    # Interrupt Dynamic settings
    eicSym_UpdateInterruptStatus = eicComponent.createBooleanSymbol("EIC_INTERRUPT_STATUS", None)
    eicSym_UpdateInterruptStatus.setDependencies(updateEICInterruptStatus, ["EIC_INT"])
    eicSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    eicSym_IntEnComment = eicComponent.createCommentSymbol("EIC_INTERRUPT_ENABLE_COMMENT", None)
    eicSym_IntEnComment.setVisible(False)
    eicSym_IntEnComment.setLabel("Warning!!! EIC Interrupt is Disabled in Interrupt Manager")
    eicSym_IntEnComment.setDependencies(updateEICInterruptWarringStatus, InterruptVectorUpdate)

    # Clock Warning status
    eicSym_ClkEnComment = eicComponent.createCommentSymbol("EIC_CLOCK_ENABLE_COMMENT", None)
    eicSym_ClkEnComment.setLabel("Warning!!! EIC Peripheral Clock is Disabled in Clock Manager")
    eicSym_ClkEnComment.setVisible(False)
    eicSym_ClkEnComment.setDependencies(updateEICClockWarringStatus, ["core."+eicInstanceName.getValue()+"_CLOCK_ENABLE"])

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        eicnonSecDepList = []
        eicnonSecDepList.append("EIC_NONSEC")
        eicnonSecDepList.extend(eicSym_Channel)
        eicSym_UpdateInterruptSecurity = eicComponent.createBooleanSymbol("EIC_SECURITY_STATUS", None)
        eicSym_UpdateInterruptSecurity.setDependencies(updateEicInterruptSecurity, eicnonSecDepList)
        eicSym_UpdateInterruptSecurity.setVisible(False)
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eicHeader1File = eicComponent.createFileSymbol("EIC_HEADER", None)
    eicHeader1File.setSourcePath("../peripheral/eic_u2804/templates/plib_eic.h.ftl")
    eicHeader1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".h")
    eicHeader1File.setDestPath("/peripheral/eic/")
    eicHeader1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicHeader1File.setType("HEADER")
    eicHeader1File.setMarkup(True)

    eicSource1File = eicComponent.createFileSymbol("EIC_SOURCE", None)
    eicSource1File.setSourcePath("../peripheral/eic_u2804/templates/plib_eic.c.ftl")
    eicSource1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".c")
    eicSource1File.setDestPath("/peripheral/eic/")
    eicSource1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicSource1File.setType("SOURCE")
    eicSource1File.setMarkup(True)

    eicSystemInitFile = eicComponent.createFileSymbol("EIC_SYS_INT", None)
    eicSystemInitFile.setType("STRING")
    eicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eicSystemInitFile.setSourcePath("../peripheral/eic_u2804/templates/system/initialization.c.ftl")
    eicSystemInitFile.setMarkup(True)

    eicSystemDefFile = eicComponent.createFileSymbol("EIC_SYS_DEF", None)
    eicSystemDefFile.setType("STRING")
    eicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eicSystemDefFile.setSourcePath("../peripheral/eic_u2804/templates/system/definitions.h.ftl")
    eicSystemDefFile.setMarkup(True)


    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":

        if ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EIC\"]/instance@[name=\"EIC\"]/register-group@[name=\"EIC_SEC\"]") != None:
            eicSecureAlias = eicComponent.createBooleanSymbol("EIC_SECURE_ALIAS", None)
            eicSecureAlias.setValue(True)
            eicSecureAlias.setVisible(False)

        nonseceicHeader1File = eicComponent.createFileSymbol("EIC_HEADER_NONSEC", None)
        nonseceicHeader1File.setSourcePath("../peripheral/eic_u2804/templates/trustZone/plib_eic.h.ftl")
        nonseceicHeader1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".h")
        nonseceicHeader1File.setDestPath("/peripheral/eic/")
        nonseceicHeader1File.setProjectPath("config/" + configName + "/peripheral/eic/")
        nonseceicHeader1File.setType("HEADER")
        nonseceicHeader1File.setMarkup(True)
        nonseceicHeader1File.setEnabled(False)

        nonseceicSource1File = eicComponent.createFileSymbol("EIC_SOURCE_NONSEC", None)
        nonseceicSource1File.setSourcePath("../peripheral/eic_u2804/templates/trustZone/plib_eic.c.ftl")
        nonseceicSource1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".c")
        nonseceicSource1File.setDestPath("/peripheral/eic/")
        nonseceicSource1File.setProjectPath("config/" + configName + "/peripheral/eic/")
        nonseceicSource1File.setType("SOURCE")
        nonseceicSource1File.setMarkup(True)
        nonseceicSource1File.setEnabled(False)

        nonseceicSystemInitFile = eicComponent.createFileSymbol("EIC_SYS_INT_NONSEC", None)
        nonseceicSystemInitFile.setType("STRING")
        nonseceicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        nonseceicSystemInitFile.setSourcePath("../peripheral/eic_u2804/templates/system/initialization.c.ftl")
        nonseceicSystemInitFile.setMarkup(True)
        nonseceicSystemInitFile.setEnabled(False)

        nonseceicSystemDefFile = eicComponent.createFileSymbol("EIC_SYS_DEF_NONSEC", None)
        nonseceicSystemDefFile.setType("STRING")
        nonseceicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        nonseceicSystemDefFile.setSourcePath("../peripheral/eic_u2804/templates/system/definitions.h.ftl")
        nonseceicSystemDefFile.setMarkup(True)
        nonseceicSystemDefFile.setEnabled(False)
        nonseceicSystemDefFile.setDependencies(fileGenLogic, ["EIC_NONSEC", "NMI_IS_NON_SECURE", "IS_EIC_NONSEC"])

        EICfilesArray.append(nonseceicHeader1File)
        EICfilesArray.append(nonseceicSource1File)
        EICfilesArray.append(nonseceicSystemDefFile)
        EICfilesArray.append(nonseceicSystemInitFile)

        eicHeader1File.setSecurity("SECURE")
        eicSource1File.setSecurity("SECURE")
        eicSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        eicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")