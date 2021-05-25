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
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################
global createDMAChannelVectorList
global getDMAVectorName
global updateDMAInterrupt
global enableAllDMAPriorityInterrupts
global createPeripheralTrigger_IDMap
global updateDMAInterruptWarringStatus

global dmaInstanceName
dmaInstanceName = ""

global dmaVectorNameList
dmaVectorNameList = []

global numGenerators
numGenerators = 0

global numUsers
numUsers = 0

global per_instance
per_instance = {}

global peridValueListSymbols
peridValueListSymbols = []

global dmaActiveChannels
dmaActiveChannels = []

global dmaChannelIds
dmaChannelIds = []

dmaEvsysDepList = []



global triggerSettings

triggerSettings = {
                        #"key"              : ["CASTEN",         "RAS",            "WAS"           ]
                        "Software Trigger"  : ["BLOCK_TRANSFER", "AUTO_ADDR_INCR", "AUTO_ADDR_INCR"],
                        "Standard_Transmit" : ["CELL_TRANSFER", "BYTE_ADDR_INCR", "FIXED_BYTE_ADDR_INCR"],
                        "Standard_Receive"  : ["CELL_TRANSFER", "FIXED_BYTE_ADDR_INCR", "BYTE_ADDR_INCR"]
}

################################################################################
#### Business Logic ####
################################################################################

#-------------------------------------------------------------------------------------------------------------------------#
def getDMAVectorName(priority):
    global dmaVectorNameList

    for n in range(len(dmaVectorNameList)):
        vectorName = dmaVectorNameList[n]
        if vectorName[-1] == priority:
            return vectorName

    return None

def enableAllDMAPriorityInterrupts(isEnable):
    global dmaVectorNameList

    # Enable all the DMA interrupt lines, unlock them and set the default handler
    for n in range(0, len(dmaVectorNameList)):
        vectorName = dmaVectorNameList[n]
        Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", isEnable, 2)
        Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", isEnable, 2)
        if isEnable == True:
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_Handler", 2)

def updateDMAInterrupt(localComponent):
    global dmaVectorNameList
    global getDMAVectorName

    # Get number of DMA channels
    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")

    # First disable all the DMA interrupt lines, unlock them and set the default handler
    for n in range(0, len(dmaVectorNameList)):
        vectorName = dmaVectorNameList[n]
        Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", False, 2)
        Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", False, 2)
        Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_Handler", 2)


    # Now enable DMA channel interrupt lines for which DMA channel is enabled
    for n in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "DMA_ENABLE_CH_" + str(n))
        dmaChannelPriorty = localComponent.getSymbolByID("DMA_CHCTRLB_PRI_CH_" + str(n)).getSelectedValue()
        # Get the vector name to use for the given DMA channel
        vectorName = getDMAVectorName(dmaChannelPriorty)

        if dmaChannelEnable == True:
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_InterruptHandler", 2)


def updateDMAInterruptWarringStatus(symbol, event):
    localComponent = symbol.getComponent()
    dmaEnable = localComponent.getSymbolValue("DMA_ENABLE")

    symbol.setVisible(False)

    # Get number of DMA channels
    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")

    # Get the DMA interrupt priority number corresponding to the Interrupt Vector that got updated
    intPriorityNumber = event["id"].split("_")[1][-1]

    if dmaEnable == True and event["value"] == True:
        for n in range(0, dmaChannelCount):
            dmaChannelEnable = Database.getSymbolValue("core", "DMA_ENABLE_CH_" + str(n))
            dmaChannelPriorty = localComponent.getSymbolByID("DMA_CHCTRLB_PRI_CH_" + str(n)).getSelectedKey()[-1]

            if dmaChannelEnable == True and (dmaChannelPriorty == intPriorityNumber):
                symbol.setVisible(True)

def DMAInterruptConfig(coreComponent,dmaMenu):
    global dmaVectorNameList
    global enableAllDMAPriorityInterrupts
    global updateDMAInterruptWarringStatus
    InterruptVectorUpdate = []

    vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for id in range(0, len(vectorValues)):
        if vectorValues[id].getAttribute("module-instance") == "DMA":
            dmaVectorName = vectorValues[id].getAttribute("name")
            dmaVectorNameList.append(dmaVectorName)

    dmaNumIntPriorities = coreComponent.createIntegerSymbol("DMA_NUM_INT_PRIO", dmaMenu)
    dmaNumIntPriorities.setLabel("Number of interrupt priorities")
    dmaNumIntPriorities.setDefaultValue(len(dmaVectorNameList))
    dmaNumIntPriorities.setVisible(False)

    if len(dmaVectorNameList) > 1:
        nvic_multi_vector = coreComponent.createBooleanSymbol(dmaInstanceName.getValue() + "_MULTI_IRQn", None)
        nvic_multi_vector.setDefaultValue(True)
        nvic_multi_vector.setVisible(False)

    # First disable all the DMA interrupt lines, unlock them and set the default handler
    enableAllDMAPriorityInterrupts(False)

    # Show a warning message if any of the DMA priority interrupt is disabled
    for n in range(0, len(dmaVectorNameList)):
        vectorName = dmaVectorNameList[n]
        InterruptVectorUpdate.append("core." + vectorName + "_INTERRUPT_ENABLE_UPDATE")

    # Interrupt Warning status
    dmaSym_IntEnComment = coreComponent.createCommentSymbol("DMA_INTERRUPT_ENABLE_COMMENT", dmaMenu)
    dmaSym_IntEnComment.setVisible(False)
    dmaSym_IntEnComment.setLabel("Warning!!! DMA Interrupt is Disabled in Interrupt Manager")
    dmaSym_IntEnComment.setDependencies(updateDMAInterruptWarringStatus, InterruptVectorUpdate)

#-------------------------------------------------------------------------------------------------------------------------#
def onDMAChannelEnable(symbol, event):
    global dmaActiveChannels

    index = event["id"].strip("DMA_ENABLE_CH_")

    try:
        index = int(index)
    except:
        return

    # Update the list of active DMA channels
    if event["value"] == True:
        if index not in dmaActiveChannels:
            dmaActiveChannels.append(index)
    else :
        if index in dmaActiveChannels:
            dmaActiveChannels.remove(index)

    if symbol.getID() == "DMA_ENABLE":
        # Set DMA_ENABLE to true if atleast one channel is enabled
        symbol.setValue(len(dmaActiveChannels) > 0, 2)
        # Enable clock if DMA_ENABLE is true
        Database.setSymbolValue("core", dmaInstanceName.getValue() + "_CLOCK_ENABLE", symbol.getValue(), 2)
    elif symbol.getID() == "DMA_HIGHEST_CHANNEL":
        dmaActiveChannels.sort()
        dmaActiveChannels.reverse()
        if dmaActiveChannels:
            symbol.setValue(int(dmaActiveChannels[0]) + 1, 2)
        else:
            symbol.setValue(0)
    else:
        # Enable all DMA priority interrupts if one or more channel is enabled. Otherwise, disable all interrupts.
        enableAllDMAPriorityInterrupts(len(dmaActiveChannels) > 0)


def onChannelPriorityChange(symbol, event):
    global updateDMAInterrupt
    localComponent = symbol.getComponent()

    priority_level = localComponent.getSymbolByID(event["id"]).getSelectedKey().split("_")[1]
    symbol.setValue(dmaInstanceName.getValue() + "_PRI" + priority_level + "_IRQn")

    # Make sure the DMA interrupt for the new priority level is enabled
    # updateDMAInterrupt(localComponent)


def updateDMAClockWarringStatus(symbol, event):

    symbol.setVisible(not event["value"])

def dmaEvsysControl(symbol, event):
    localComponent = symbol.getComponent()

    channel = symbol.getID().split("DMA_EVSYS_DUMMY")[1]
    enable = localComponent.getSymbolValue("DMA_ENABLE_CH_" + channel)
    input = localComponent.getSymbolValue("DMA_ENABLE_EVSYS_IN_" + channel)
    aux_input = localComponent.getSymbolValue("DMA_ENABLE_EVSYS_AUX_IN_" + channel)

    if localComponent.getSymbolValue("DMA_ENABLE_EVSYS_OUT_" + channel) != None:
        output = localComponent.getSymbolValue("DMA_ENABLE_EVSYS_OUT_" + channel)
        if Database.getSymbolValue("evsys", "GENERATOR_DMA_CH_" + channel + "_ACTIVE") != (enable & output):
            Database.setSymbolValue("evsys", "GENERATOR_DMA_CH_" + channel + "_ACTIVE", (enable & output), 2)

    if Database.getSymbolValue("evsys", "USER_DMA_CHSTRT_" + channel + "_READY") != (enable & input):
        Database.setSymbolValue("evsys", "USER_DMA_CHSTRT_" + channel + "_READY", (enable & input), 2)

    if Database.getSymbolValue("evsys", "USER_DMA_CHAUX_" + channel + "_READY") != (enable & aux_input):
        Database.setSymbolValue("evsys", "USER_DMA_CHAUX_" + channel + "_READY", (enable & aux_input), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def dmaChannelAllocLogic(symbol, event):
    localComponent = symbol.getComponent()
    perID = event["id"].split('DMA_CH_NEEDED_FOR_')[1]

    if event["value"] == True:
        dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
        channelAllocated = False

        for i in range(0, dmaChannelCount):
            dmaChannelEnable = localComponent.getSymbolValue("DMA_ENABLE_CH_" + str(i))
            dmaChannelPerID = localComponent.getSymbolByID("DMA_CHCTRLB_TRIG_CH_" + str(i)).getSelectedKey()

            if dmaChannelPerID == perID:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(i), True, 2)
                localComponent.setSymbolValue("DMA_CHCTRLB_TRIG_CH_" + str(i) + "_VAL_LOCK", True, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break

            # Reserve the first available free channel
            if dmaChannelEnable == False:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(i), True, 2)
                localComponent.getSymbolByID("DMA_CHCTRLB_TRIG_CH_" + str(i)).setSelectedKey(perID)
                localComponent.setSymbolValue("DMA_CHCTRLB_TRIG_CH_" + str(i) + "_VAL_LOCK", True, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break


        if event["value"] == True and channelAllocated == False:
            # Couldn't find any free DMA channel, hence set warning.
            localComponent.clearSymbolValue("DMA_CH_FOR_" + perID)
            localComponent.setSymbolValue("DMA_CH_FOR_" + perID, -2, 2)

    # Client requested to deallocate channel
    else:
        channelNumber = localComponent.getSymbolValue("DMA_CH_FOR_" + perID)
        if channelNumber >= 0:
            dmaChannelEnable = localComponent.getSymbolValue("DMA_ENABLE_CH_" + str(channelNumber))
            dmaChannelPerID = localComponent.getSymbolByID("DMA_CHCTRLB_TRIG_CH_" + str(channelNumber)).getSelectedKey()
            # Reset the previously allocated channel
            if perID == dmaChannelPerID and dmaChannelEnable == True:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(channelNumber), False, 2)
                localComponent.getSymbolByID("DMA_CHCTRLB_TRIG_CH_" + str(channelNumber)).setSelectedKey("Software Trigger")
                localComponent.setSymbolValue("DMA_CHCTRLB_TRIG_CH_" + str(channelNumber) + "_VAL_LOCK", False, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, -1, 2)


def updateSourceCellStriding(symbol, event):
    DMA_CHCTRLB_RAS_Value = event["symbol"].getSelectedKey()
    symbol.setVisible("FIXED" not in DMA_CHCTRLB_RAS_Value)

def updateDestinationCellStriding(symbol, event):
    DMA_CHCTRLB_WAS_Value = event["symbol"].getSelectedKey()
    symbol.setVisible("FIXED" not in DMA_CHCTRLB_WAS_Value)

def updatePatternMatchData(symbol, event):
    localComponent = symbol.getComponent()

    channelNum = symbol.getID().split("_")[-1]

    patternEnable = localComponent.getSymbolValue("DMA_CHCTRLB_PATEN_CH_" + channelNum)
    patternLen = localComponent.getSymbolByID("DMA_CHCTRLB_PATLEN_CH_" + channelNum).getSelectedKey()

    if patternLen == "1_BYTE":
        symbol.setMax(255)
    else:
        symbol.setMax(65535)

    symbol.setVisible(patternEnable == True)

def updateEnablePatternIgnoreByte(symbol, event):
    localComponent = symbol.getComponent()

    channelNum = symbol.getID().split("_")[-1]

    patternEnable = localComponent.getSymbolValue("DMA_CHCTRLB_PATEN_CH_" + channelNum)
    patternLen = localComponent.getSymbolByID("DMA_CHCTRLB_PATLEN_CH_" + channelNum).getSelectedKey()

    # Pattern Ignore function is only available if pattern length is 2 bytes
    if patternEnable == True and patternLen == "2_BYTE":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        symbol.setReadOnly(True)
        symbol.setValue(False)
        symbol.setReadOnly(False)

def updatePatternMatchLength(symbol, event):
    symbol.setVisible(event["value"])

def eventModesVisibility(symbol, event):
    symbol.setVisible(event["value"])

def onTriggerSourceChanged(symbol, event):
    global triggerSettings

    symbolID = symbol.getID()

    triggerSource = event["symbol"].getSelectedKey()

    if triggerSource in triggerSettings.keys():
        trigger = triggerSource
    else:
        if "Receive" in triggerSource:
            trigger = "Standard_Receive"
        else:
            trigger = "Standard_Transmit"

    symbol.clearValue()

    if "CHCTRLB_CASTEN" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][0]), 2)
    elif "CHCTRLB_RAS" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][1]), 2)
    elif "CHCTRLB_WAS" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][2]), 2)

def fileGenerationDep(symbol, event):
    symbol.setEnabled(event["value"])

#-----------------------------------------------------------------------------------------------------#
def createPeripheralTrigger_IDMap():
    global per_instance

    # Create lists for peripheral triggers and the corresponding ID values
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
    modules = node.getChildren()
    for module in range (0, len(modules)):
        instances = modules[module].getChildren()
        for instance in range (0, len(instances)):
            options = instances[instance].getChildren()
            for option in range (0, len(options)):
                if "parameters" == options[option].getName():
                    parameters = options[option].getChildren()
                    for parameter in range(0, len(parameters)):
                        if "name" in parameters[parameter].getAttributeList():
                            name = str(parameters[parameter].getAttribute("name"))
                            module = str(instances[instance].getAttribute("name"))
                            if "DMAC_ID" in name:
                                if int(parameters[parameter].getAttribute("value")) not in per_instance.values():
                                    name = name.replace('DMAC_ID_', '')
                                    name = name.replace('TX', 'Transmit')
                                    name = name.replace('RX', 'Receive')
                                    name = name.replace('LEFT', 'Left')
                                    name = name.replace('RIGHT', 'Right')
                                    per_instance[module + "_" + name] = int(parameters[parameter].getAttribute("value"))

    # Needs placed after above parsing as value of DMAC_ID for peripherals may be 0
    per_instance["Event System Trigger"] = 1
    per_instance["Software Trigger"] = 0

def DMA_ATDF_Read(coreComponent, dmaEnable):
    dmaChannelCount = 0
    global numGenerators
    global numUsers
    global createPeripheralTrigger_IDMap

    dmaChannelNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/register-group@[name=\"DMA\"]").getChildren()
    for id in range(0, len(dmaChannelNode)):
        if dmaChannelNode[id].getAttribute("name") == "CHANNEL":
            dmaChannelCount = int(dmaChannelNode[id].getAttribute("count"))

    generatorValues = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators").getChildren()
    for id in range(0, len(generatorValues)):
        if generatorValues[id].getAttribute("module-instance") == "DMA":
            numGenerators = numGenerators + 1

    usersValues = ATDF.getNode("/avr-tools-device-file/devices/device/events/users").getChildren()
    for id in range(0, len(usersValues)):
        if usersValues[id].getAttribute("module-instance") == "DMA":
            numUsers = numUsers + 1

    #Two types of actions DMA can take upon receiving an event. Either start transfer or take action defined in EVAUXACT. Hence divide by 2.
    numUsers = numUsers/2

    # DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
    dmaChCount = coreComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmaEnable)
    dmaChCount.setLabel("DMA (DMAC) Channels Count")
    dmaChCount.setDefaultValue(dmaChannelCount)
    dmaChCount.setVisible(False)

    dmaEventGeneratorCount = coreComponent.createIntegerSymbol("DMA_EVSYS_GENERATOR_COUNT", dmaEnable)
    dmaEventGeneratorCount.setDefaultValue(numGenerators)
    dmaEventGeneratorCount.setVisible(False)

    dmaEventUserCount = coreComponent.createIntegerSymbol("DMA_EVSYS_USER_COUNT", dmaEnable)
    dmaEventUserCount.setDefaultValue(numUsers)
    dmaEventUserCount.setVisible(False)

    createPeripheralTrigger_IDMap()

def dmaSymbolsForDMASysService(coreComponent, dmaChannelEnable):

    #DMA - Source FIXED_AM Value
    dmaSym_BTCTRL_SRCINC_FIXED = coreComponent.createStringSymbol("DMA_SRC_FIXED_AM_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_SRCINC_FIXED.setDefaultValue("0")
    dmaSym_BTCTRL_SRCINC_FIXED.setVisible(False)

    #DMA - Source INCREMENTED_AM Value
    dmaSym_BTCTRL_SRCINC_INCREMENTED = coreComponent.createStringSymbol("DMA_SRC_INCREMENTED_AM_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_SRCINC_INCREMENTED.setDefaultValue("1")
    dmaSym_BTCTRL_SRCINC_INCREMENTED.setVisible(False)

    #DMA - Destination FIXED_AM Value
    dmaSym_BTCTRL_DSTINC_FIXED = coreComponent.createStringSymbol("DMA_DST_FIXED_AM_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_DSTINC_FIXED.setDefaultValue("0")
    dmaSym_BTCTRL_DSTINC_FIXED.setVisible(False)

    #DMA - Destination INCREMENTED_AM Value
    dmaSym_BTCTRL_DSTINC_INCREMENTED = coreComponent.createStringSymbol("DMA_DST_INCREMENTED_AM_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_DSTINC_INCREMENTED.setDefaultValue("1")
    dmaSym_BTCTRL_DSTINC_INCREMENTED.setVisible(False)

    #DMA - Beat Size BYTE Value
    dmaSym_BTCTRL_BEATSIZE_BYTE = coreComponent.createStringSymbol("DMA_DATA_WIDTH_BYTE_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_BEATSIZE_BYTE.setDefaultValue("0")
    dmaSym_BTCTRL_BEATSIZE_BYTE.setVisible(False)

    #DMA - Beat Size HWORD Value
    dmaSym_BTCTRL_BEATSIZE_HWORD = coreComponent.createStringSymbol("DMA_DATA_WIDTH_HALFWORD_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_BEATSIZE_HWORD.setDefaultValue("1")
    dmaSym_BTCTRL_BEATSIZE_HWORD.setVisible(False)

    #DMA - Beat Size WORD Value
    dmaSym_BTCTRL_BEATSIZE_WORD = coreComponent.createStringSymbol("DMA_DATA_WIDTH_WORD_VALUE", dmaChannelEnable)
    dmaSym_BTCTRL_BEATSIZE_WORD.setDefaultValue("2")
    dmaSym_BTCTRL_BEATSIZE_WORD.setVisible(False)
#-----------------------------------------------------------------------------------------------------#

################################################################################
#### Component ####
################################################################################

# DMA_NAME: Needed to map DMA system service APIs to PLIB APIs
dmaSymAPI_Prefix = coreComponent.createStringSymbol("DMA_NAME", None)
dmaSymAPI_Prefix.setDefaultValue("DMA")
dmaSymAPI_Prefix.setVisible(False)

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMA\"]").getChildren()

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
dmaInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
dmaInstanceName.setDefaultValue(instances[0].getAttribute("name"))
dmaInstanceName.setVisible(False)

dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("dma_u2503:SAME5XDMAModel")

dmaMenu = coreComponent.createMenuSymbol("DMA_MENU", None)
dmaMenu.setLabel("DMA (DMAC)")
dmaMenu.setDescription("DMA (DMAC) Configuration")

# DMA_IP: Needed to generate IP specific code in DMA System Service
dmaPLIBIp = coreComponent.createStringSymbol("DMA_IP", dmaMenu)
dmaPLIBIp.setLabel("DMA IP")
dmaPLIBIp.setValue("dma_03639")
dmaPLIBIp.setVisible(False)

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
dmaEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", dmaMenu)
dmaEnable.setLabel("Use DMA Service ?")
dmaEnable.setVisible(True)

# Needed to generate Linked list APIs
dmaChannelLinkedList = coreComponent.createBooleanSymbol("DMA_LL_ENABLE", dmaMenu)
dmaChannelLinkedList.setLabel("Use Linked List Mode ?")

# Needed for code generation
dmaHighestCh = coreComponent.createIntegerSymbol("DMA_HIGHEST_CHANNEL", dmaEnable)
dmaHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmaHighestCh.setVisible(False)

DMA_ATDF_Read(coreComponent, dmaEnable)

DMAInterruptConfig(coreComponent, dmaMenu)

channelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")

for channelID in range(0, channelCount):

    global per_instance
    global numUsers
    global numGenerators

    # Channel enable - CHCTRLAk.ENABLE
    dmaChannelEnable = coreComponent.createBooleanSymbol("DMA_ENABLE_CH_" + str(channelID), dmaMenu)
    dmaChannelEnable.setLabel("Use DMA Channel " + str(channelID))
    dmaChannelEnable.setDefaultValue(False)
    dmaChannelEnable.setDependencies(onDMAChannelEnable, ["DMA_ENABLE_CH_" + str(channelID)])
    dmaChannelIds.append("DMA_ENABLE_CH_" + str(channelID))

    #Channel Run in Standby - CHCTRLAk.RUNSTANDBY
    CHCTRLA_RUNSTDBY_Enable = coreComponent.createBooleanSymbol("DMA_CHCTRLA_RUNSTDBY_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLA_RUNSTDBY_Enable.setLabel("Run Channel in Standby mode")
    CHCTRLA_RUNSTDBY_Enable.setDefaultValue(False)

    # Channel Trigger Source - CHCTRLBk.TRIG[7:0]
    CHCTRLB_TRIG_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_TRIG_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_TRIG_Config.setLabel("Trigger Source")

    sortedTriggerSourcesKeyList = sorted(per_instance.keys())

    for id in range(len(sortedTriggerSourcesKeyList)):
        key = sortedTriggerSourcesKeyList[id]
        value = per_instance[key]
        description = key
        CHCTRLB_TRIG_Config.addKey(key, str(value), description)
        if key == "Software Trigger":
            CHCTRLB_TRIG_Config.setDefaultValue(id)
    CHCTRLB_TRIG_Config.setOutputMode("Value")
    CHCTRLB_TRIG_Config.setDisplayMode("Description")

    # DMA manager will use LOCK symbol to lock the "DMA_CHCTRLB_TRIG_CH_ + str(channelID)" symbol
    dmaSym_CHCTRLA_TRIGSRC_LOCK = coreComponent.createBooleanSymbol("DMA_CHCTRLB_TRIG_CH_" + str(channelID) + "_VAL_LOCK", dmaChannelEnable)
    dmaSym_CHCTRLA_TRIGSRC_LOCK.setLabel("Lock DMA Request")
    dmaSym_CHCTRLA_TRIGSRC_LOCK.setVisible(False)
    dmaSym_CHCTRLA_TRIGSRC_LOCK.setUseSingleDynamicValue(True)

    #Channel Priority Level - CHCTRLbk.PRI
    priority_level_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/value-group@[name=\"CHCTRLB__PRI\"]").getChildren()

    CHCTRLB_PRI_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_PRI_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_PRI_Config.setLabel("Channel Priority Level")

    for id in range(len(priority_level_values)):
        CHCTRLB_PRI_Config.addKey("PRI_" + str(id+1), str(id), "Priority Level " + str(id+1))
    CHCTRLB_PRI_Config.setDefaultValue(0)
    CHCTRLB_PRI_Config.setOutputMode("Key")
    CHCTRLB_PRI_Config.setDisplayMode("Description")
    #CHCTRLB_PRI_Config.setDependencies(onChannelPriorityChange, ["DMA_CHCTRLB_PRI_CH_" + str(channelID)])

    #Channel Read address sequence - CHCTRLbk.RAS[2:0]
    ras_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/value-group@[name=\"CHCTRLB__RAS\"]").getChildren()

    CHCTRLB_RAS_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_RAS_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_RAS_Config.setLabel("Read Address Sequence")

    for id in range(len(ras_values)):
        key = ras_values[id].getAttribute("name")
        value = ras_values[id].getAttribute("value")
        description = ras_values[id].getAttribute("caption")
        CHCTRLB_RAS_Config.addKey(key, value, description)
    CHCTRLB_RAS_Config.setDefaultValue(0)
    CHCTRLB_RAS_Config.setOutputMode("Key")
    CHCTRLB_RAS_Config.setDisplayMode("Description")
    CHCTRLB_RAS_Config.setDependencies(onTriggerSourceChanged, ["DMA_CHCTRLB_TRIG_CH_" + str(channelID)])

    #Channel Write address sequence - CHCTRLbk.WAS[2:0]
    was_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/value-group@[name=\"CHCTRLB__WAS\"]").getChildren()

    CHCTRLB_WAS_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_WAS_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_WAS_Config.setLabel("Write Address Sequence")

    for id in range(len(was_values)):
        key = was_values[id].getAttribute("name")
        value = was_values[id].getAttribute("value")
        description = was_values[id].getAttribute("caption")
        CHCTRLB_WAS_Config.addKey(key, value, description)
    CHCTRLB_WAS_Config.setDefaultValue(0)
    CHCTRLB_WAS_Config.setOutputMode("Key")
    CHCTRLB_WAS_Config.setDisplayMode("Description")
    CHCTRLB_WAS_Config.setDependencies(onTriggerSourceChanged, ["DMA_CHCTRLB_TRIG_CH_" + str(channelID)])

    #Channel Cell transfer size - CHXSIZk.CSZ
    CHXSIZ_Register = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/register-group@[name=\"CHANNEL\"]/register@[name=\"CHXSIZ\"]").getChildren()

    for bitfields in range(len(CHXSIZ_Register)):
        if CHXSIZ_Register[bitfields].getAttribute("name") == "CSZ":
            max_cell_size_value = CHXSIZ_Register[bitfields].getAttribute("mask")
            break

    CHXSIZ_CSZ_Config = coreComponent.createIntegerSymbol("DMA_CHXSIZ_CSZ_CH_" + str(channelID), dmaChannelEnable)
    CHXSIZ_CSZ_Config.setLabel("Cell Transfer Size")
    CHXSIZ_CSZ_Config.setMin(0)
    CHXSIZ_CSZ_Config.setMax(int(max_cell_size_value, 16))
    CHXSIZ_CSZ_Config.setDefaultValue(1)

    #Channel Trigger Action (Cell Auto Start Enable of Ensuing Transfers) - CHCTRLB.CASTEN
    CHCTRLB_CASTEN_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_CASTEN_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_CASTEN_Config.setLabel("Trigger Action (Cell Auto Start Enable)")
    CHCTRLB_CASTEN_Config.addKey("CELL_TRANSFER", "0", "One Cell Transfer Per DMA Start Trigger")
    CHCTRLB_CASTEN_Config.addKey("BLOCK_TRANSFER", "1", "Transfer all cells (complete block) on a single DMA Start Trigger")
    CHCTRLB_CASTEN_Config.setDefaultValue(0)
    CHCTRLB_CASTEN_Config.setOutputMode("Value")
    CHCTRLB_CASTEN_Config.setDisplayMode("Description")

    #Channel Source Cell Striding Size - CHSSTRDk.SSTRD
    CHSSTRD_Register = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/register-group@[name=\"CHANNEL\"]/register@[name=\"CHSSTRD\"]").getChildren()
    for bitfields in range(len(CHSSTRD_Register)):
        if CHSSTRD_Register[bitfields].getAttribute("name") == "SSTRD":
            max_cell_striding_size_value = CHSSTRD_Register[bitfields].getAttribute("mask")
            break

    CHSSTRD_SSTRD_Config = coreComponent.createIntegerSymbol("DMA_CHSSTRD_SSTRD_CH_" + str(channelID), dmaChannelEnable)
    CHSSTRD_SSTRD_Config.setLabel("Source Cell Striding Size")
    CHSSTRD_SSTRD_Config.setMin(0)
    CHSSTRD_SSTRD_Config.setMax(int(max_cell_striding_size_value, 16))
    CHSSTRD_SSTRD_Config.setDefaultValue(0)
    #Cell striding is not used for fixed addressing mode
    CHSSTRD_SSTRD_Config.setDependencies(updateSourceCellStriding, ["DMA_CHCTRLB_RAS_CH_" + str(channelID)])

    #Channel Destination Cell Striding Size - CHDSTRDk.DSTRD
    CHDSTRD_DSTRD_Config = coreComponent.createIntegerSymbol("DMA_CHDSTRD_DSTRD_CH_" + str(channelID), dmaChannelEnable)
    CHDSTRD_DSTRD_Config.setLabel("Destination Cell Striding Size")
    CHDSTRD_DSTRD_Config.setMin(0)
    CHDSTRD_DSTRD_Config.setMax(int(max_cell_striding_size_value, 16))
    CHDSTRD_DSTRD_Config.setDefaultValue(0)
    #Cell striding is not used for fixed addressing mode
    CHDSTRD_DSTRD_Config.setDependencies(updateDestinationCellStriding, ["DMA_CHCTRLB_WAS_CH_" + str(channelID)])

    #Channel Enable Abort on Pattern Match - CHCTRLB.PATEN
    CHCTRLB_PATEN_Enable = coreComponent.createBooleanSymbol("DMA_CHCTRLB_PATEN_CH_" + str(channelID), dmaChannelEnable)
    CHCTRLB_PATEN_Enable.setLabel("Enable Abort on Pattern Match?")
    CHCTRLB_PATEN_Enable.setDefaultValue(False)

    #Channel Enable Abort on Pattern Match - CHCTRLB.PATLEN
    CHCTRLB_PATLEN_Config = coreComponent.createKeyValueSetSymbol("DMA_CHCTRLB_PATLEN_CH_" + str(channelID), CHCTRLB_PATEN_Enable)
    CHCTRLB_PATLEN_Config.setLabel("Pattern Match Length")
    CHCTRLB_PATLEN_Config.addKey("1_BYTE", "0", "1 Byte")
    CHCTRLB_PATLEN_Config.addKey("2_BYTE", "1", "2 Bytes")
    CHCTRLB_PATLEN_Config.setDefaultValue(0)
    CHCTRLB_PATLEN_Config.setOutputMode("Value")
    CHCTRLB_PATLEN_Config.setDisplayMode("Description")
    CHCTRLB_PATLEN_Config.setVisible(False)
    CHCTRLB_PATLEN_Config.setDependencies(updatePatternMatchLength, ["DMA_CHCTRLB_PATEN_CH_" + str(channelID)])

    #Channel Pattern Match Data - CHPDAT.PDAT
    CHPDAT_PDAT_Config = coreComponent.createHexSymbol("DMA_CHPDAT_PDAT_CH_" + str(channelID), CHCTRLB_PATEN_Enable)
    CHPDAT_PDAT_Config.setLabel("Pattern Match Data")
    CHPDAT_PDAT_Config.setMin(0)
    CHPDAT_PDAT_Config.setMax(65535)
    CHPDAT_PDAT_Config.setDefaultValue(0)
    CHPDAT_PDAT_Config.setVisible(False)
    CHPDAT_PDAT_Config.setDependencies(updatePatternMatchData, ["DMA_CHCTRLB_PATEN_CH_" + str(channelID), "DMA_CHCTRLB_PATLEN_CH_" + str(channelID)])

    #Channel Pattern Ignore Byte Enable - CHCTRLB.PIGNEN
    CHCTRLB_PIGNEN_Enable = coreComponent.createBooleanSymbol("DMA_CHCTRLB_PIGNEN_CH_" + str(channelID), CHCTRLB_PATEN_Enable)
    CHCTRLB_PIGNEN_Enable.setLabel("Enable Pattern Ignore Byte")
    CHCTRLB_PIGNEN_Enable.setDefaultValue(False)
    CHCTRLB_PIGNEN_Enable.setVisible(False)
    CHCTRLB_PIGNEN_Enable.setDependencies(updateEnablePatternIgnoreByte, ["DMA_CHCTRLB_PATEN_CH_" + str(channelID), "DMA_CHCTRLB_PATLEN_CH_" + str(channelID)])

    #Channel Pattern Ignore Byte Value - CHPDAT.PIGN[7:0]
    CHPDAT_PIGN_Config = coreComponent.createHexSymbol("DMA_CHPDAT_PIGN_CH_" + str(channelID), CHCTRLB_PIGNEN_Enable)
    CHPDAT_PIGN_Config.setLabel("Pattern Ignore Value")
    CHPDAT_PIGN_Config.setMin(0)
    CHPDAT_PIGN_Config.setMax(255)
    CHPDAT_PIGN_Config.setDefaultValue(0)
    CHPDAT_PIGN_Config.setVisible(False)
    CHPDAT_PIGN_Config.setDependencies(updatePatternMatchLength, ["DMA_CHCTRLB_PIGNEN_CH_" + str(channelID)])

    # DMA channel interrupt number - needed by core drivers to disable during critical section
    DMA_ChannelX_VectorEnum = coreComponent.createStringSymbol(dmaInstanceName.getValue() + "_CHANNEL" + str(channelID) + "_INT_SRC", dmaChannelEnable)
    DMA_ChannelX_VectorEnum.setLabel("DMA Channel X interrupt Vector Number Enum")
    DMA_ChannelX_VectorEnum.setDefaultValue(dmaInstanceName.getValue() + "_PRI" + CHCTRLB_PRI_Config.getSelectedKey().split("_")[1] + "_IRQn")
    DMA_ChannelX_VectorEnum.setDependencies(onChannelPriorityChange, ["DMA_CHCTRLB_PRI_CH_" + str(channelID)])
    DMA_ChannelX_VectorEnum.setVisible(False)

####################################################################################################

    if channelID < numUsers:
        dmaEVSYSMenu = coreComponent.createMenuSymbol("DMA_EVSYS_MENU"+str(channelID), dmaChannelEnable)
        dmaEVSYSMenu.setLabel("Event System Configuration")

        if channelID < numGenerators:
            dmaEvsysOut = coreComponent.createBooleanSymbol("DMA_ENABLE_EVSYS_OUT_" + str(channelID), dmaEVSYSMenu)
            dmaEvsysOut.setLabel("Enable Event Output for Channel " + str(channelID))

            dmaEvsysEVOMODE = coreComponent.createKeyValueSetSymbol("DMA_BTCTRL_EVSYS_EVOMODE_" + str(channelID), dmaEvsysOut)
            dmaEvsysEVOMODE.setLabel("Event Output Mode")

            dmaEvsysEVOMODEValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/value-group@[name=\"CHEVCTRL__EVOMODE\"]").getChildren()

            for index in range(len(dmaEvsysEVOMODEValues)):
                dmaEvsysEVOMODEKeyName = dmaEvsysEVOMODEValues[index].getAttribute("name")
                dmaEvsysEVOMODEKeyDescription = dmaEvsysEVOMODEValues[index].getAttribute("caption")
                dmaEvsysEVOMODEKeyValue = dmaEvsysEVOMODEValues[index].getAttribute("value")
                dmaEvsysEVOMODE.addKey(dmaEvsysEVOMODEKeyName, dmaEvsysEVOMODEKeyValue, dmaEvsysEVOMODEKeyDescription)

            dmaEvsysEVOMODE.setOutputMode("Key")
            dmaEvsysEVOMODE.setDisplayMode("Description")
            dmaEvsysEVOMODE.setVisible(False)
            dmaEvsysEVOMODE.setDependencies(eventModesVisibility, ["DMA_ENABLE_EVSYS_OUT_" + str(channelID)])

        dmaEvsysIn = coreComponent.createBooleanSymbol("DMA_ENABLE_EVSYS_IN_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysIn.setLabel("Enable Start Event Input for Channel " + str(channelID))

        dmaEvsysAuxIn = coreComponent.createBooleanSymbol("DMA_ENABLE_EVSYS_AUX_IN_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysAuxIn.setLabel("Enable Auxillary Event for Channel " + str(channelID))

        dmaEvsysAuxACT = coreComponent.createKeyValueSetSymbol("DMA_CHEVCTRL_EVACT_" + str(channelID), dmaEvsysAuxIn)
        dmaEvsysAuxACT.setLabel("Event Input Action")

        dmaEvsysAuxActValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA\"]/value-group@[name=\"CHEVCTRL__EVAUXACT\"]").getChildren()

        for index in range(len(dmaEvsysAuxActValues)):
            dmaEvsysAuxACTKeyName = dmaEvsysAuxActValues[index].getAttribute("name")
            dmaEvsysAuxACTKeyDescription = dmaEvsysAuxActValues[index].getAttribute("caption")
            dmaEvsysAuxACTKeyValue = dmaEvsysAuxActValues[index].getAttribute("value")
            dmaEvsysAuxACT.addKey(dmaEvsysAuxACTKeyName, dmaEvsysAuxACTKeyValue, dmaEvsysAuxACTKeyDescription)

        dmaEvsysAuxACT.setOutputMode("Key")
        dmaEvsysAuxACT.setDisplayMode("Description")
        dmaEvsysAuxACT.setVisible(False)
        dmaEvsysAuxACT.setDependencies(eventModesVisibility, ["DMA_ENABLE_EVSYS_AUX_IN_" + str(channelID)])

        dmaEvsysDepList.append("DMA_ENABLE_CH_" + str(channelID))
        dmaEvsysDepList.append("DMA_ENABLE_EVSYS_OUT_" + str(channelID))
        dmaEvsysDepList.append("DMA_ENABLE_EVSYS_IN_" + str(channelID))
        dmaEvsysDepList.append("DMA_ENABLE_EVSYS_AUX_IN_" + str(channelID))

        dmaEvsys = coreComponent.createBooleanSymbol("DMA_EVSYS_DUMMY" + str(channelID) , dmaMenu)
        dmaEvsys.setVisible(False)
        dmaEvsys.setDependencies(dmaEvsysControl, dmaEvsysDepList)

dmaEnable.setDependencies(onDMAChannelEnable, dmaChannelIds)
dmaHighestCh.setDependencies(onDMAChannelEnable, dmaChannelIds)

dmaSymbolsForDMASysService(coreComponent, dmaChannelEnable)

# Interface for Peripheral clients
for per in per_instance.keys():
    dmaChannelNeeded = coreComponent.createBooleanSymbol("DMA_CH_NEEDED_FOR_" + str(per), dmaMenu)
    dmaChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    dmaChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    dmaChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(per), dmaMenu)
    dmaChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    dmaChannel.setDefaultValue(-1)
    dmaChannel.setVisible(False)

dmaPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", dmaChannelEnable)
dmaPERIDChannelUpdate.setLabel("Local dmaChannelAllocLogic")
dmaPERIDChannelUpdate.setVisible(False)
dmaPERIDChannelUpdate.setDependencies(dmaChannelAllocLogic, peridValueListSymbols)

# Clock Warning status
dmaSym_ClkEnComment = coreComponent.createCommentSymbol("DMA_CLOCK_ENABLE_COMMENT", dmaMenu)
dmaSym_ClkEnComment.setLabel("Warning!!! DMA Peripheral Clock is Disabled in Clock Manager")
dmaSym_ClkEnComment.setVisible(False)
dmaSym_ClkEnComment.setDependencies(updateDMAClockWarringStatus, ["core."+dmaInstanceName.getValue()+"_CLOCK_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmaHeaderFile = coreComponent.createFileSymbol("DMA_HEADER", None)
dmaHeaderFile.setSourcePath("../peripheral/dma_03639/templates/plib_dma.h.ftl")
dmaHeaderFile.setOutputName("plib_" + dmaInstanceName.getValue().lower() + ".h")
dmaHeaderFile.setDestPath("/peripheral/dma/")
dmaHeaderFile.setProjectPath("config/" + configName + "/peripheral/dma/")
dmaHeaderFile.setType("HEADER")
dmaHeaderFile.setMarkup(True)
dmaHeaderFile.setEnabled(False)
dmaHeaderFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])

# Source File
dmaSourceFile = coreComponent.createFileSymbol("DMA_SOURCE", None)
dmaSourceFile.setSourcePath("../peripheral/dma_03639/templates/plib_dma.c.ftl")
dmaSourceFile.setOutputName("plib_" + dmaInstanceName.getValue().lower() + ".c")
dmaSourceFile.setDestPath("/peripheral/dma/")
dmaSourceFile.setProjectPath("config/" + configName + "/peripheral/dma/")
dmaSourceFile.setType("SOURCE")
dmaSourceFile.setMarkup(True)
dmaSourceFile.setEnabled(False)
dmaSourceFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])

#System Initialization
dmaSystemInitFile = coreComponent.createFileSymbol("DMA_SYS_INIT", None)
dmaSystemInitFile.setType("STRING")
dmaSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmaSystemInitFile.setSourcePath("../peripheral/dma_03639/templates/system/initialization.c.ftl")
dmaSystemInitFile.setMarkup(True)
dmaSystemInitFile.setEnabled(False)
dmaSystemInitFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])

#System Definition
dmaSystemDefFile = coreComponent.createFileSymbol("DMA_SYS_DEF", None)
dmaSystemDefFile.setType("STRING")
dmaSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmaSystemDefFile.setSourcePath("../peripheral/dma_03639/templates/system/definitions.h.ftl")
dmaSystemDefFile.setMarkup(True)
dmaSystemDefFile.setEnabled(False)
dmaSystemDefFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])
