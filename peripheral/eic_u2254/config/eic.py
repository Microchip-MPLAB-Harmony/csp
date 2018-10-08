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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global eicInstanceName

###################################################################################################
######################################### Callbacks ###############################################
###################################################################################################
global DEBOUNCEN_Code

def confMenu(symbol, event):

    if event["id"] == "NMI_CTRL":

        Database.clearSymbolValue("core", NMIInterruptHandler)

        if event["value"] == True:
            Database.setSymbolValue("core", NMIInterruptHandler, "NMI_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", NMIInterruptHandler, "NonMaskableInt_Handler", 2)

    symbol.setVisible(event["value"])

def codeGenerationForEVCCTRL_EXTINTEO(symbol, event):
    channel = int(event["id"].split("_")[2])
    if Database.getSymbolValue(event["namespace"], "EIC_CHAN_" + str(channel)):
        if not str(event["id"]).startswith("EIC_CHAN_"):
            if(event["value"] == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)
        else:
            parameter = symbol.getID().split("EIC_")[1]
            if(Database.getSymbolValue(event["namespace"], "EIC_" + str(parameter) + "_" + str(channel)) == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)) , 1)
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)

    else:
        symbol.setValue((symbol.getValue() & (~(0x1 << channel))) , 1)

    #communicate to event system
    Database.setSymbolValue("evsys0","GENERATOR_EIC_EXTINT_" + str(channel) + "_ACTIVE", event["value"], 2)

def updateEICInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, bool(event["value"]), 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, bool(event["value"]), 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if bool(event["value"]) == True:
        Database.setSymbolValue("core", InterruptHandler, eicInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "EIC_Handler", 2)

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

###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(eicComponent):
    eicSym_eventsList = []
    eicSym_asynchList = []
    eicSym_debounceList =[]
    eicSym_InterruptList = []
    eicSym_Channel = []
    global DEBOUNCEN_Code
    global EXTINT_Code
    global eicInstanceName
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global NMIInterruptHandler

    eicInstanceName = eicComponent.createStringSymbol("EIC_INSTANCE_NAME", None)
    eicInstanceName.setVisible(False)
    eicInstanceName.setDefaultValue(eicComponent.getID().upper())

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
    CTRLA_CKSEL_SelectionSymbol.setLabel("EIC Clock Source Selection")

    eicClkselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_CTRLA__CKSEL\"]")

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
    eicPLX4.setLabel("Non Maskable Interrupt Control")

    nmiConfMenu = eicComponent.createMenuSymbol("NMI_MENU", eicPLX4)
    nmiConfMenu.setLabel("NMI Configuration")
    nmiConfMenu.setDependencies(confMenu, ["NMI_CTRL"])
    nmiConfMenu.setVisible(False)

    #NMIASYNCH
    NMI_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("NMI_ASYNCH" , nmiConfMenu)
    NMI_ASYNCH_Selection.setLabel("NMI Detection Clock")

    eicNMIAsyncNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_NMICTRL__NMIASYNCH\"]")
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
    NMI_FILTEN_Selection.setLabel("Enable filter")

    # NMI - SENSE
    NMI_SENSE_SelectionSymbol = eicComponent.createKeyValueSetSymbol("NMI_SENSE" , nmiConfMenu)
    NMI_SENSE_SelectionSymbol.setLabel("NMI Interrupt Edge Selection")

    eicNMISenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_NMICTRL__NMISENSE\"]")

    for index in range(len(eicNMISenseNode.getChildren())):
        eicNMISenseKeyName = eicNMISenseNode.getChildren()[index].getAttribute("name")
        eicNMISenseKeyDescription = eicNMISenseNode.getChildren()[index].getAttribute("caption")
        eicNMISenseKeyValue = eicNMISenseNode.getChildren()[index].getAttribute("value")
        NMI_SENSE_SelectionSymbol.addKey(eicNMISenseKeyName, eicNMISenseKeyValue , eicNMISenseKeyDescription)

    NMI_SENSE_SelectionSymbol.setDefaultValue(0)
    NMI_SENSE_SelectionSymbol.setOutputMode("Key")
    NMI_SENSE_SelectionSymbol.setDisplayMode("Description")

    #Interrupt 0 - EXTINT Settings
    for extIntIndex in range(0 , extIntCount):

        eicPLX1 = eicComponent.createBooleanSymbol("EIC_CHAN_" + str(extIntIndex) , None)
        eicPLX1.setLabel("Enable EIC Channel" + str(extIntIndex))

        eicConfiguration = eicComponent.createMenuSymbol("EIC_MENU" + str(extIntIndex), eicPLX1)
        eicConfiguration.setLabel("EIC Channel" + str(extIntIndex) + " Configuration")
        eicConfiguration.setDependencies(confMenu, ["EIC_CHAN_" + str(extIntIndex)])
        eicConfiguration.setVisible(False)

        # populate a list with IDs for code generation dependency
        eicSym_Channel.append("EIC_CHAN_" + str(extIntIndex))

        eicINT = eicComponent.createBooleanSymbol("EIC_INT_" + str(extIntIndex) , eicConfiguration)
        eicINT.setLabel("Enable Interrupt")
        eicSym_InterruptList.append("EIC_INT_" + str(extIntIndex))

        #EVCTRL - External Interrupt Event Output Enable 0..7 Channel number
        EVCCTRL_EXTINTEO_Selection = eicComponent.createBooleanSymbol("EIC_EXTINTEO_" + str(extIntIndex) , eicConfiguration)
        EVCCTRL_EXTINTEO_Selection.setLabel("Enable Event Output")

        # populate a list with IDs for code generation dependency
        eicSym_eventsList.append("EIC_EXTINTEO_" + str(extIntIndex))

        #ASYNCH
        ASYNCH_ASYNCH_Selection = eicComponent.createKeyValueSetSymbol("EIC_ASYNCH_" + str(extIntIndex) , eicConfiguration)
        ASYNCH_ASYNCH_Selection.setLabel("External Interrupt" + str(extIntIndex) + " Detection Clock")

        eicAsynchNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_ASYNCH__ASYNCH\"]")

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
        CONFIG_SENSE_SelectionSymbol.setLabel("External Interrupt" + str(extIntIndex) + " Edge Selection")

        eicConfigSenseNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_CONFIG__SENSE0\"]")

        for index in range(len(eicConfigSenseNode.getChildren())):
            eicConfigSenseKeyName = eicConfigSenseNode.getChildren()[index].getAttribute("name")
            eicConfigSenseKeyDescription = eicConfigSenseNode.getChildren()[index].getAttribute("caption")
            eicConfigSenseKeyValue = eicConfigSenseNode.getChildren()[index].getAttribute("value")
            CONFIG_SENSE_SelectionSymbol.addKey(eicConfigSenseKeyName, eicConfigSenseKeyValue , eicConfigSenseKeyDescription)

        CONFIG_SENSE_SelectionSymbol.setDefaultValue(0)
        CONFIG_SENSE_SelectionSymbol.setOutputMode("Key")
        CONFIG_SENSE_SelectionSymbol.setDisplayMode("Description")

        #DEBOUNCEN
        DEBOUNCEN_Selection = eicComponent.createBooleanSymbol("EIC_DEBOUNCEN_" + str(extIntIndex) , eicConfiguration)
        DEBOUNCEN_Selection.setLabel("Enable Debounce")
        DEBOUNCEN_Selection.setVisible(False)
        DEBOUNCEN_Selection.setDependencies(debounceEnable,["EIC_CONFIG_SENSE_" + str(extIntIndex)])

        #CONFIG - Filter Enable
        CONFIG_FILTER_Selection = eicComponent.createBooleanSymbol("EIC_CONFIG_FILTEN_" + str(extIntIndex) , eicConfiguration)
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

    eicCalculation = eicComponent.createMenuSymbol("REG_MENU", None)
    eicCalculation.setVisible(False)
    eicCalculation.setLabel("Calculated register values")

    EVCCTRL_EXTINTEO_Code = eicComponent.createHexSymbol("EIC_EXTINTEO" , eicCalculation)
    EVCCTRL_EXTINTEO_Code.setDefaultValue(0)
    EVCCTRL_EXTINTEO_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_eventsList)

    ASYNCH_Code = eicComponent.createHexSymbol("EIC_ASYNCH" , eicCalculation)
    ASYNCH_Code.setDefaultValue(0)
    ASYNCH_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_asynchList)

    DEBOUNCEN_Code = eicComponent.createHexSymbol("EIC_DEBOUNCEN" , eicCalculation)
    DEBOUNCEN_Code.setDefaultValue(0)
    DEBOUNCEN_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_debounceList)

    EXTINT_Code = eicComponent.createHexSymbol("EIC_INT" , eicCalculation)
    EXTINT_Code.setDefaultValue(0)
    EXTINT_Code.setDependencies(codeGenerationForEVCCTRL_EXTINTEO, eicSym_InterruptList)

    eicDebounceMenu = eicComponent.createMenuSymbol("DEBOUNCE_MENU", None)
    eicDebounceMenu.setLabel("Debouncer ConfiGuration")
    eicDebounceMenu.setVisible(False)
    eicDebounceMenu.setDependencies(debounceMenu, ["EIC_DEBOUNCEN"])

    #DEBOUNCER - TICKON
    PRESCALER_TICKON_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_PRESCALER_TICKON" , eicDebounceMenu)
    PRESCALER_TICKON_SelectionSymbol.setLabel("Debouncer Sampler Clock Source")

    eicTickOnNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__TICKON\"]")

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
    DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States for EXTINT[7:0]")

    eicStatesxNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__STATES0\"]")

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
    DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[7:0]")

    eicPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__PRESCALER0\"]")

    for index in range(len(eicPrescalerNode.getChildren())):
        eicPrescalerKeyName = eicPrescalerNode.getChildren()[index].getAttribute("name")
        eicPrescalerKeyDescription = eicPrescalerNode.getChildren()[index].getAttribute("caption")
        eicPrescalerKeyValue = eicPrescalerNode.getChildren()[index].getAttribute("value")
        DEBOUNCER_PRESCALER_SelectionSymbol.addKey(eicPrescalerKeyName, eicPrescalerKeyValue , eicPrescalerKeyDescription)

    DEBOUNCER_PRESCALER_SelectionSymbol.setDefaultValue(0)
    DEBOUNCER_PRESCALER_SelectionSymbol.setOutputMode("Value")
    DEBOUNCER_PRESCALER_SelectionSymbol.setDisplayMode("Description")

    #DEBOUNCER - Number of States x (8:15)
    DEBOUNCER_NO_STATES_SelectionSymbol = eicComponent.createKeyValueSetSymbol("EIC_DEBOUNCER_NO_STATES_1" , eicDebounceMenu)
    DEBOUNCER_NO_STATES_SelectionSymbol.setLabel("Valid Pin States Duration for EXTINT[15:8]")

    eicStatesxNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__STATES1\"]")
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
    DEBOUNCER_PRESCALER_SelectionSymbol.setLabel("Debouncer Prescaler for EXTINT[15:8]")

    eicPrescalerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/value-group@[name=\"EIC_DPRESCALER__PRESCALER1\"]")

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

    InterruptVector = eicInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = eicInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = eicInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = eicInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    NMIInterruptHandler = "NonMaskableInt_INTERRUPT_HANDLER"

    # Interrupt Dynamic settings
    eicSym_UpdateInterruptStatus = eicComponent.createBooleanSymbol("EIC_INTERRUPT_STATUS", None)
    eicSym_UpdateInterruptStatus.setDependencies(updateEICInterruptStatus, ["EIC_INT"])
    eicSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    eicSym_IntEnComment = eicComponent.createCommentSymbol("EIC_INTERRUPT_ENABLE_COMMENT", None)
    eicSym_IntEnComment.setVisible(False)
    eicSym_IntEnComment.setLabel("Warning!!! EIC Interrupt is Disabled in Interrupt Manager")
    eicSym_IntEnComment.setDependencies(updateEICInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    eicSym_ClkEnComment = eicComponent.createCommentSymbol("EIC_CLOCK_ENABLE_COMMENT", None)
    eicSym_ClkEnComment.setLabel("Warning!!! EIC Peripheral Clock is Disabled in Clock Manager")
    eicSym_ClkEnComment.setVisible(False)
    eicSym_ClkEnComment.setDependencies(updateEICClockWarringStatus, ["core."+eicInstanceName.getValue()+"_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eicHeader1File = eicComponent.createFileSymbol("EIC_HEADER", None)
    eicHeader1File.setSourcePath("../peripheral/eic_u2254/templates/plib_eic.h.ftl")
    eicHeader1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".h")
    eicHeader1File.setDestPath("/peripheral/eic/")
    eicHeader1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicHeader1File.setType("HEADER")
    eicHeader1File.setMarkup(True)

    eicSource1File = eicComponent.createFileSymbol("EIC_SOURCE", None)
    eicSource1File.setSourcePath("../peripheral/eic_u2254/templates/plib_eic.c.ftl")
    eicSource1File.setOutputName("plib_"+eicInstanceName.getValue().lower()+".c")
    eicSource1File.setDestPath("/peripheral/eic/")
    eicSource1File.setProjectPath("config/" + configName + "/peripheral/eic/")
    eicSource1File.setType("SOURCE")
    eicSource1File.setMarkup(True)

    eicSystemInitFile = eicComponent.createFileSymbol("EIC_SYS_INT", None)
    eicSystemInitFile.setType("STRING")
    eicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eicSystemInitFile.setSourcePath("../peripheral/eic_u2254/templates/system/initialization.c.ftl")
    eicSystemInitFile.setMarkup(True)

    eicSystemDefFile = eicComponent.createFileSymbol("EIC_SYS_DEF", None)
    eicSystemDefFile.setType("STRING")
    eicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eicSystemDefFile.setSourcePath("../peripheral/eic_u2254/templates/system/definitions.h.ftl")
    eicSystemDefFile.setMarkup(True)
