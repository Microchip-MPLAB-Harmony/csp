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
from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################
global createDMAChannelVectorDict
global dmaChannelVectorDict
dmaChannelVectorDict = {}
global dmacInstanceName
global dmacHeaderFile
global dmacSourceFile
global dmacSystemInitFile
global dmacSystemDefFile
global dmacEnable
global numGenerators
global numUsers
numGenerators = 0
numUsers = 0

# Parse atdf xml file to get instance name for the peripheral which has DMA id.
# And construct a list of PERIDs

global per_instance
per_instance = {}

global peridValueListSymbols
peridValueListSymbols = []

global dmacActiveChannels
dmacActiveChannels = []

global dmacChannelIds
dmacChannelIds = []

global dmacChannelInt
dmacChannelInt = []

global has_digits

dmacDep = []
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
                            global per_instance
                            if int(parameters[parameter].getAttribute("value")) not in per_instance.values():
                                name = name.replace('DMAC_ID_', '')
                                name = name.replace('TX', 'Transmit')
                                name = name.replace('RX', 'Receive')
                                name = name.replace('LEFT', 'Left')
                                name = name.replace('RIGHT', 'Right')
                                per_instance[module + "_" + name] = int(parameters[parameter].getAttribute("value"))

# Needs placed after above parsing as value of DMAC_ID for peripherals may be 0
per_instance["Software Trigger"] = 0

generatorValues = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators").getChildren()
for id in range(0, len(generatorValues)):
    if generatorValues[id].getAttribute("module-instance") == "DMAC":
        numGenerators = numGenerators + 1

usersValues = ATDF.getNode("/avr-tools-device-file/devices/device/events/users").getChildren()
for id in range(0, len(usersValues)):
    if usersValues[id].getAttribute("module-instance") == "DMAC":
        numUsers = numUsers + 1

# This is the dictionary for all trigger sources and corresponding DMAC settings.
# "dmacTriggerLogic" business logic will override the DMAC setting values
# based on the trigger source selected.

global triggerSettings

triggerSettings = setDMACDefaultSettings()

################################################################################
#### Business Logic ####
################################################################################

def dmacTriggerLogic(symbol, event):

    global triggerSettings

    symbolID = symbol.getID()

    if event["value"] in triggerSettings:
        trigger = event["value"]
    else:
        if "Receive" in event["value"]:
            trigger = "Standard_Receive"
        else:
            trigger = "Standard_Transmit"

    symbol.clearValue()

    if "TRIGACT" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][0]), 2)
    elif "SRCINC" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][1]), 2)
    elif "DSTINC" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][2]), 2)
    elif "BEATSIZE" in symbolID:
        symbol.setSelectedKey(str(triggerSettings[trigger][3]), 2)

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the highest
# index enabled, also if the list is empty then none of the channel is enabled.
# Highest index will be used to create DMAC objects in source code.
# List empty or non-empty status helps to generate/discard DMAC code.
def onChannelEnable(symbol, event):

    global dmacActiveChannels
    dmaGlobalEnable = False

    index = event["id"].strip("DMAC_ENABLE_CH_")

    try:
        index = int(index)
    except:
        return

    if event["value"] == True:
        if index not in dmacActiveChannels:
            dmacActiveChannels.append(index)
    else :
        if index in dmacActiveChannels:
            dmacActiveChannels.remove(index)

    dmacActiveChannels.sort()
    dmacActiveChannels.reverse()

    symbol.clearValue()

    # Check if the list is not empty first since list element is accessed in the code
    if dmacActiveChannels:
        if symbol.getID() == "DMAC_HIGHEST_CHANNEL":
            symbol.setValue(int(dmacActiveChannels[0]), 2)

    if symbol.getID() == "DMA_ENABLE":
        if dmacActiveChannels:
            dmaGlobalEnable = True

        symbol.setValue(dmaGlobalEnable, 2)

        #clock enable
        Database.setSymbolValue("core", dmacInstanceName.getValue() + "_CLOCK_ENABLE", dmaGlobalEnable, 2)

        # File generation logic
        dmacHeaderFile.setEnabled(dmaGlobalEnable)
        dmacSourceFile.setEnabled(dmaGlobalEnable)
        dmacSystemInitFile.setEnabled(dmaGlobalEnable)
        dmacSystemDefFile.setEnabled(dmaGlobalEnable)

def has_digits(string):
    import re
    res = re.compile('\d').search(string)
    return res is not None

def createDMAChannelVectorDict():
    # Returns a list containing dictionary {channel_number : vector_name}, where vector_name is read from ATDF
    # The list index corelates to DMAC channel and contains a dictionary with channel number and the vector name to use for that channel
    # Total size of the list will be equal to DMA_CHANNEL_COUNT (read from ATDF)
    # Example: dmaChannelVectorDict = {"0" : "DMAC_0", "1" : "DMAC_1", "2" : "DMAC_2", "3" : "DMAC_3", "4" : "DMAC_OTHER", "5" : "DMAC_OTHER" ... "31" : "DMAC_OTHER"}
    global dmaChannelVectorDict
    import re
    dmaVectorNameList = []
    highest_ch_num = 0

    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
    vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for id in range(0, len(vectorValues)):
        if vectorValues[id].getAttribute("module-instance") == "DMAC":
            dmaVectorNameList.append(vectorValues[id].getAttribute("name"))

    for n in dmaVectorNameList:
        if "OTHER" not in n:
            name = n.replace("DMAC_", "")
            if has_digits(name) == True:
                name = re.sub("[^0-9, _]", "", name)
            if name.startswith('_') == True:
                name = name[1:]
            channelList = name.split("_")
            if len(channelList) == 1:
                # Enter here where DMA vector names are defined as "DMAC_0" and "DMAC_OTHER"
                dmaChannelVectorDict[channelList[0]] = n
                highest_ch_num = max(highest_ch_num, int(channelList[0]))
            else:
                # Enter here for PIC32CX where NVIC interrupt vector names are defined as "DMAC_0_3" and "DMAC_4_15"
                startCh = channelList[0]
                endCh = channelList[1]
                for x in range(int(startCh), int(endCh) + 1):
                    dmaChannelVectorDict[str(x)] = n
                    highest_ch_num = max(highest_ch_num, x)
    for n in dmaVectorNameList:
        if "OTHER" in n:
            for y in range(highest_ch_num + 1, dmaChannelCount):
                dmaChannelVectorDict[str(y)] = n

    return dmaChannelVectorDict

def updateInterruptLogic(symbol, event):
    global dmaChannelVectorDict

    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
    vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    # First disable all the DMAC channel interrupt lines, unlock them and set the default handler
    for id in range(0, len(vectorValues)):
        if vectorValues[id].getAttribute("module-instance") == "DMAC":
            vectorName = vectorValues[id].getAttribute("name")
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", False, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", False, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_Handler", 2)

    # Now enable DMAC channel interrupt lines for which DMAC channel is enabled
    for n in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + str(n))
        dmaChannelInterrupt = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + str(n) + "_INTERRUPT")
        # Get the vector name to use for the given DMAC channel
        vectorName = dmaChannelVectorDict[str(n)]
        if dmaChannelEnable == True and dmaChannelInterrupt == True:
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_InterruptHandler", 2)

def updateDMACInterruptWarringStatus(symbol, event):

    if dmacEnable.getValue() == True:
        symbol.setVisible(event["value"])

def updateDMACClockWarringStatus(symbol, event):

    symbol.setVisible(not event["value"])

def dmacTriggerCalc(symbol, event):

    global per_instance

    symbol.clearValue()
    symbol.setValue(per_instance.get(event["value"]), 2)

def dmacEvsysControl(symbol, event):

    channel = symbol.getID().split("DMAC_EVSYS_DUMMY")[1]

    enable = Database.getSymbolValue("core","DMAC_ENABLE_CH_" + channel)
    input = Database.getSymbolValue("core","DMAC_ENABLE_EVSYS_IN_" + channel)

    if Database.getSymbolValue("core","DMAC_ENABLE_EVSYS_OUT_" + channel) != None:
        output = Database.getSymbolValue("core","DMAC_ENABLE_EVSYS_OUT_" + channel)
        if Database.getSymbolValue("evsys", "GENERATOR_DMAC_CH_" + channel + "_ACTIVE") != (enable & output):
            Database.setSymbolValue("evsys", "GENERATOR_DMAC_CH_" + channel + "_ACTIVE", (enable & output), 2)
    if Database.getSymbolValue("evsys", "USER_DMAC_CH_" + channel + "_READY") != (enable & input):
        Database.setSymbolValue("evsys", "USER_DMAC_CH_" + channel + "_READY", (enable & input), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def dmacChannelAllocLogic(symbol, event):
    perID = event["id"].split('DMA_CH_NEEDED_FOR_')[1]
    if event["value"] == True:
        dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
        channelAllocated = False

        for i in range(0, dmaChannelCount):
            dmaChannelEnable = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + str(i))
            dmaChannelPerID = str(Database.getSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(i)))

            if dmaChannelPerID == perID:
                Database.setSymbolValue("core", "DMAC_ENABLE_CH_" + str(i), True, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(i), perID, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(i) + "_PERID_LOCK", True, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break

            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.setSymbolValue("core", "DMAC_ENABLE_CH_" + str(i), True, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(i), perID, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(i) + "_PERID_LOCK", True, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break


        if event["value"] == True and channelAllocated == False:
            # Couldn't find any free DMA channel, hence set warning.
            Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
            Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -2, 2)

    # Client requested to deallocate channel
    else:
        channelNumber = Database.getSymbolValue("core", "DMA_CH_FOR_" + perID)
        dmaChannelEnable = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + str(channelNumber))
        dmaChannelPerID = str(Database.getSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelNumber)))
        # Reset the previously allocated channel
        if perID == dmaChannelPerID and dmaChannelEnable == True:
            Database.setSymbolValue("core", "DMAC_ENABLE_CH_" + str(channelNumber), False, 2)
            Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelNumber), "Software Trigger", 2)
            Database.setSymbolValue("core", "DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelNumber) + "_PERID_LOCK", False, 2)
            Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -1, 2)

################################################################################
#### Component ####
################################################################################

# DMA_NAME: Needed to map DMA system service APIs to PLIB APIs
dmacSymAPI_Prefix = coreComponent.createStringSymbol("DMA_NAME", None)
dmacSymAPI_Prefix.setDefaultValue("DMAC")
dmacSymAPI_Prefix.setVisible(False)

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]").getChildren()

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
dmacInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
dmacInstanceName.setDefaultValue(instances[0].getAttribute("name"))
dmacInstanceName.setVisible(False)

dmacChannelNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]/instance@[name=\""+dmacInstanceName.getValue()+"\"]/parameters/param@[name=\"CH_NUM\"]")
if dmacChannelNode is None:
    dmacChannelNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]/instance@[name=\""+dmacInstanceName.getValue()+"\"]/parameters/param@[name=\"DMA_CH_NUM\"]")
dmacChannelCount = int(dmacChannelNode.getAttribute("value"))

dmacMenu = coreComponent.createMenuSymbol("DMAC_MENU", None)
dmacMenu.setLabel("DMA (DMAC)")
dmacMenu.setDescription("DMA (DMAC) Configuration")

dmacNumIntLines = 0

vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

for id in range(0, len(vectorValues)):
    if vectorValues[id].getAttribute("module-instance") == "DMAC":
        dmacIntName = coreComponent.createStringSymbol("DMA_INT_NAME_" + str(dmacNumIntLines) , dmacMenu)
        dmacIntName.setDefaultValue(vectorValues[id].getAttribute("name").replace("DMAC_", ""))
        dmacIntName.setVisible(False)

        dmacNumIntLines = dmacNumIntLines + 1

dmacIntLines = coreComponent.createIntegerSymbol("DMA_INT_LINES", dmacMenu)
dmacIntLines.setDefaultValue(dmacNumIntLines)
dmacIntLines.setVisible(False)

multi_iqrn_sym_exists = Database.getSymbolValue("core", dmacInstanceName.getValue() + "_MULTI_IRQn")

if dmacNumIntLines > 1 and multi_iqrn_sym_exists == None:
    nvic_multi_vector = coreComponent.createBooleanSymbol(dmacInstanceName.getValue() + "_MULTI_IRQn", None)
    nvic_multi_vector.setDefaultValue(True)
    nvic_multi_vector.setVisible(False)

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
dmacEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", dmacMenu)
dmacEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CTRL")
dmacEnable.setLabel("Use DMA Service ?")
dmacEnable.setVisible(False)

dmacIntEnable = coreComponent.createBooleanSymbol("DMA_INT_ENABLE", dmacMenu)
dmacIntEnable.setVisible(False)

# DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
dmacChCount = coreComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmacEnable)
dmacChCount.setLabel("DMA (DMAC) Channels Count")
dmacChCount.setDefaultValue(dmacChannelCount)
dmacChCount.setVisible(False)

createDMAChannelVectorDict()

dmacEventCount = coreComponent.createIntegerSymbol("DMA_EVSYS_GENERATOR_COUNT", dmacEnable)
dmacEventCount.setDefaultValue(numGenerators)
dmacEventCount.setVisible(False)

dmacEventCount = coreComponent.createIntegerSymbol("DMA_EVSYS_USER_COUNT", dmacEnable)
dmacEventCount.setDefaultValue(numUsers)
dmacEventCount.setVisible(False)

# dmacFileGen = coreComponent.createBooleanSymbol("DMAC_FILE_GEN", dmacEnable)
# dmacFileGen.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:%NOREGISTER%")
# dmacFileGen.setLabel("DMA (DMAC) File Generation")
# dmacFileGen.setVisible(False)
# dmacFileGen.setDependencies(onGlobalEnableLogic, ["DMA_ENABLE"])

dmacHighestCh = coreComponent.createIntegerSymbol("DMAC_HIGHEST_CHANNEL", dmacEnable)
dmacHighestCh.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:PRICTRL0")
dmacHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmacHighestCh.setVisible(False)

dmacChannelLinkedList = coreComponent.createBooleanSymbol("DMAC_LL_ENABLE", dmacMenu)
dmacChannelLinkedList.setLabel("Use Linked List Mode ?")

#Priority Control 0 Register
for dmacCount in range(0, 4):

    #Level 0/1/2/3 Round-Robin Arbitration Enable
    PRICTRL0_LVLPRI_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_LVLXPRIO_" + str(dmacCount),dmacMenu)
    PRICTRL0_LVLPRI_SelectionSym.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CTRL")
    PRICTRL0_LVLPRI_SelectionSym.setLabel("Priority Level " + str(dmacCount) + " Arbitration Scheme")

    PRICTRL0_LVLPRI_SelectionSym.addKey("STATIC_LVL", "0", "Static Priority Arbitration")
    PRICTRL0_LVLPRI_SelectionSym.addKey("ROUND_ROBIN_LVL", "1", "Round Robin Priority Arbitration")
    PRICTRL0_LVLPRI_SelectionSym.setDefaultValue(1)
    PRICTRL0_LVLPRI_SelectionSym.setOutputMode("Value")
    PRICTRL0_LVLPRI_SelectionSym.setDisplayMode("Description")

for channelID in range(0, dmacChCount.getValue()):

    global per_instance
    global numUsers
    global numGenerators

    dmacChannelEnable = coreComponent.createBooleanSymbol("DMAC_ENABLE_CH_" + str(channelID), dmacMenu)
    dmacChannelEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacChannelEnable.setLabel("Use DMAC Channel " + str(channelID))
    dmacChannelIds.append("DMAC_ENABLE_CH_" + str(channelID))

    #Channel Run in Standby
    CH_CHCTRLA_RUNSTDBY_Ctrl = coreComponent.createBooleanSymbol("DMAC_CHCTRLA_RUNSTDBY_CH_" + str(channelID), dmacChannelEnable)
    CH_CHCTRLA_RUNSTDBY_Ctrl.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    CH_CHCTRLA_RUNSTDBY_Ctrl.setLabel("Run Channel in Standby mode")

    # Enable interrupt
    dmacChannelEnableInt = coreComponent.createBooleanSymbol("DMAC_ENABLE_CH_" + str(channelID) + "_INTERRUPT", dmacChannelEnable)
    dmacChannelEnableInt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:INTSTATUS")
    dmacChannelEnableInt.setLabel("Enable Interrupt")
    dmacChannelEnableInt.setDefaultValue(True)
    dmacChannelInt.append("DMAC_ENABLE_CH_" + str(channelID) + "_INTERRUPT")

    # CHCTRLA - Trigger Source
    dmacSym_CHCTRLA_TRIGSRC = coreComponent.createComboSymbol("DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID), dmacChannelEnable, sorted(per_instance.keys()))
    dmacSym_CHCTRLA_TRIGSRC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacSym_CHCTRLA_TRIGSRC.setLabel("Trigger Source")
    dmacSym_CHCTRLA_TRIGSRC.setDefaultValue("Software Trigger")

    dmacSym_PERID_Val = coreComponent.createIntegerSymbol("DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID) + "_PERID_VAL", dmacChannelEnable)
    dmacSym_PERID_Val.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacSym_PERID_Val.setLabel("PERID Value")
    dmacSym_PERID_Val.setDefaultValue(0)
    dmacSym_PERID_Val.setDependencies(dmacTriggerCalc, ["DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID)])
    dmacSym_PERID_Val.setVisible(False)

    # DMA manager will use LOCK symbol to lock the "DMAC_CHCTRLA_TRIGSRC_CH_ + str(channelID)" symbol
    dmacSym_CHCTRLA_TRIGSRC_LOCK = coreComponent.createBooleanSymbol("DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID) + "_PERID_LOCK", dmacChannelEnable)
    dmacSym_CHCTRLA_TRIGSRC_LOCK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacSym_CHCTRLA_TRIGSRC_LOCK.setLabel("Lock DMA Request")
    dmacSym_CHCTRLA_TRIGSRC_LOCK.setVisible(False)
    dmacSym_CHCTRLA_TRIGSRC_LOCK.setUseSingleDynamicValue(True)

    # CHCTRLA - Trigger Action
    dmacSym_CHCTRLA_TRIGACT = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLA_TRIGACT_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_CHCTRLA_TRIGACT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacSym_CHCTRLA_TRIGACT.setLabel("Trigger Action")
    dmacSym_CHCTRLA_TRIGACT.addKey("BLOCK", "0", "One Block Transfer Per DMA Request")
    dmacSym_CHCTRLA_TRIGACT.addKey("BEAT", "2", "One Beat Transfer per DMA Request")
    dmacSym_CHCTRLA_TRIGACT.addKey("TRANSACTION", "3", "One Transaction per DMA Request")
    dmacSym_CHCTRLA_TRIGACT.setDefaultValue(0)
    dmacSym_CHCTRLA_TRIGACT.setOutputMode("Value")
    dmacSym_CHCTRLA_TRIGACT.setDisplayMode("Description")
    dmacSym_CHCTRLA_TRIGACT.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID)])

    #Channel Priority Level
    CHCTRLB_LVL_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLA_LVL_CH_" + str(channelID), dmacChannelEnable)
    CHCTRLB_LVL_SelectionSym.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHPRILVL")
    CHCTRLB_LVL_SelectionSym.setLabel("Channel Priority Level")
    CHCTRLB_LVL_SelectionSym.addKey("LVL0", "0", "Priority Level 0")
    CHCTRLB_LVL_SelectionSym.addKey("LVL1", "1", "Priority Level 1")
    CHCTRLB_LVL_SelectionSym.addKey("LVL2", "2", "Priority Level 2")
    CHCTRLB_LVL_SelectionSym.addKey("LVL3", "3", "Priority Level 3")
    CHCTRLB_LVL_SelectionSym.setDefaultValue(0)
    CHCTRLB_LVL_SelectionSym.setOutputMode("Value")
    CHCTRLB_LVL_SelectionSym.setDisplayMode("Description")

    # BTCTRL - Destination Increment
    dmacSym_BTCTRL_DSTINC_Val = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_DSTINC_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_DSTINC_Val.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:BTCTRL")
    dmacSym_BTCTRL_DSTINC_Val.setLabel("Destination Address Mode")
    dmacSym_BTCTRL_DSTINC_Val.addKey("FIXED_AM", "0", "Fixed Address Mode")
    dmacSym_BTCTRL_DSTINC_Val.addKey("INCREMENTED_AM", "1", "Increment Address After Every Transfer")
    dmacSym_BTCTRL_DSTINC_Val.setOutputMode("Key")
    dmacSym_BTCTRL_DSTINC_Val.setDisplayMode("Description")
    dmacSym_BTCTRL_DSTINC_Val.setDefaultValue(1)
    dmacSym_BTCTRL_DSTINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID)])

    # BTCTRL - Source Increment
    dmacSym_BTCTRL_SRCINC_Val = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_SRCINC_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_SRCINC_Val.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:BTCTRL")
    dmacSym_BTCTRL_SRCINC_Val.setLabel("Source Address Mode")
    dmacSym_BTCTRL_SRCINC_Val.addKey("FIXED_AM", "0", "Fixed Address Mode")
    dmacSym_BTCTRL_SRCINC_Val.addKey("INCREMENTED_AM", "1", "Increment Address After Every Transfer")
    dmacSym_BTCTRL_SRCINC_Val.setOutputMode("Key")
    dmacSym_BTCTRL_SRCINC_Val.setDisplayMode("Description")
    dmacSym_BTCTRL_SRCINC_Val.setDefaultValue(1)
    dmacSym_BTCTRL_SRCINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLA_TRIGSRC_CH_" + str(channelID)])

    # BTCTRL - Beat Size
    dmacSym_BTCTRL_BEATSIZE = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_BEATSIZE_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_BEATSIZE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:BTCNT")
    dmacSym_BTCTRL_BEATSIZE.setLabel("Beat Size")

    # Burst
    dmacBurst = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLA_BURSTLEN_CH_" + str(channelID), dmacChannelEnable)
    dmacBurst.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacBurst.setLabel("Burst Length")
    dmacBurstNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHCTRLA__BURSTLEN\"]")
    dmacBurstValues = dmacBurstNode.getChildren()
    for index in range(len(dmacBurstValues)):
        dmacBurstKeyName = dmacBurstValues[index].getAttribute("name")
        dmacBurstKeyDescription = dmacBurstValues[index].getAttribute("caption")
        dmacBurstKeyValue = dmacBurstValues[index].getAttribute("value")
        dmacBurst.addKey(dmacBurstKeyName, dmacBurstKeyValue, dmacBurstKeyDescription)

    dmacBurst.setOutputMode("Value")
    dmacBurst.setDisplayMode("Key")

    #Threshold
    dmacThreshold = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLA_THRESH_CH_" + str(channelID), dmacChannelEnable)
    dmacThreshold.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHCTRLA")
    dmacThreshold.setLabel("FIFO Threshold")
    dmacThresholdNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHCTRLA__THRESHOLD\"]")
    dmacThresholdValues = dmacThresholdNode.getChildren()
    for index in range(len(dmacThresholdValues)):
        dmacThresholdKeyName = dmacThresholdValues[index].getAttribute("name")
        dmacThresholdKeyDescription = dmacThresholdValues[index].getAttribute("caption")
        dmacThresholdKeyValue = dmacThresholdValues[index].getAttribute("value")
        dmacThreshold.addKey(dmacThresholdKeyName, dmacThresholdKeyValue, dmacThresholdKeyDescription)

    dmacThreshold.setOutputMode("Value")
    dmacThreshold.setDisplayMode("Key")

    dmacBeatSizeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_BTCTRL__BEATSIZE\"]")
    dmacBeatSizeValues = []
    dmacBeatSizeValues = dmacBeatSizeNode.getChildren()

    dmacBeatSizeDefaultValue = 0

    for index in range(len(dmacBeatSizeValues)):
        dmacBeatSizeKeyName = dmacBeatSizeValues[index].getAttribute("name")

        if dmacBeatSizeKeyName == "WORD":
            dmacBeatSizeDefaultValue = index

        dmacBeatSizeKeyDescription = dmacBeatSizeValues[index].getAttribute("caption")
        dmacBeatSizeKeyValue = dmacBeatSizeValues[index].getAttribute("value")
        dmacSym_BTCTRL_BEATSIZE.addKey(dmacBeatSizeKeyName, dmacBeatSizeKeyValue, dmacBeatSizeKeyDescription)

    dmacSym_BTCTRL_BEATSIZE.setDefaultValue(dmacBeatSizeDefaultValue)
    dmacSym_BTCTRL_BEATSIZE.setOutputMode("Key")
    dmacSym_BTCTRL_BEATSIZE.setDisplayMode("Description")
    dmacSym_BTCTRL_BEATSIZE.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLA_TRIGSRC_CH_"+ str(channelID)])

    if dmacNumIntLines > 1 and multi_iqrn_sym_exists == None:
        # DMA channel interrupt number - needed by core drivers to disable during critical section
        DMAC_ChannelX_VectorEnum = coreComponent.createStringSymbol(dmacInstanceName.getValue() + "_CHANNEL" + str(channelID) + "_INT_SRC", dmacChannelEnable)
        DMAC_ChannelX_VectorEnum.setLabel("DMAC Channel X interrupt Vector Number Enum")
        DMAC_ChannelX_VectorEnum.setDefaultValue(dmaChannelVectorDict[str(channelID)] + "_IRQn")
        DMAC_ChannelX_VectorEnum.setVisible(False)

    if channelID < numUsers:
        dmaEVSYSMenu = coreComponent.createMenuSymbol("DMAC_EVSYS_MENU"+str(channelID), dmacChannelEnable)
        dmaEVSYSMenu.setLabel("Event System Configuration")

        if channelID < numGenerators:
            dmaEvsysOut = coreComponent.createBooleanSymbol("DMAC_ENABLE_EVSYS_OUT_" + str(channelID), dmaEVSYSMenu)
            dmaEvsysOut.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHEVCTRL")
            dmaEvsysOut.setLabel("Enable Event Output for Channel " + str(channelID))

            dmaEvsysEVOSEL = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_EVSYS_EVOSEL_" + str(channelID), dmaEVSYSMenu)
            dmaEvsysEVOSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:BTCTRL")
            dmaEvsysEVOSEL.setLabel("Event Output Selection")

            dmaEvsysEVOMODE = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_EVSYS_EVOMODE_" + str(channelID), dmaEVSYSMenu)
            dmaEvsysEVOMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHEVCTRL")
            dmaEvsysEVOMODE.setLabel("Event Output Mode")

            dmaEvsysEVOMODENode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHEVCTRL__EVOMODE\"]")
            dmaEvsysEVOMODEValues = dmaEvsysEVOMODENode.getChildren()

            for index in range(len(dmaEvsysEVOMODEValues)):
                dmaEvsysEVOMODEKeyName = dmaEvsysEVOMODEValues[index].getAttribute("name")
                dmaEvsysEVOMODEKeyDescription = dmaEvsysEVOMODEValues[index].getAttribute("caption")
                dmaEvsysEVOMODEKeyValue = dmaEvsysEVOMODEValues[index].getAttribute("value")
                dmaEvsysEVOMODE.addKey(dmaEvsysEVOMODEKeyName, dmaEvsysEVOMODEKeyValue, dmaEvsysEVOMODEKeyDescription)

            dmaEvsysEVOMODE.setOutputMode("Value")
            dmaEvsysEVOMODE.setDisplayMode("Key")

            dmaEvsysEVOSELNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_BTCTRL__EVOSEL\"]")
            dmaEvsysEVOSELValues = dmaEvsysEVOSELNode.getChildren()

            for index in range(len(dmaEvsysEVOSELValues)):
                dmaEvsysEVOSELKeyName = dmaEvsysEVOSELValues[index].getAttribute("name")
                dmaEvsysEVOSELKeyDescription = dmaEvsysEVOSELValues[index].getAttribute("caption")
                dmaEvsysEVOSELKeyValue = dmaEvsysEVOSELValues[index].getAttribute("value")
                dmaEvsysEVOSEL.addKey(dmaEvsysEVOSELKeyName, dmaEvsysEVOSELKeyValue, dmaEvsysEVOSELKeyDescription)

            dmaEvsysEVOSEL.setOutputMode("Value")
            dmaEvsysEVOSEL.setDisplayMode("Description")

        dmaEvsysIn = coreComponent.createBooleanSymbol("DMAC_ENABLE_EVSYS_IN_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysIn.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHEVCTRL")
        dmaEvsysIn.setLabel("Enable Event Input for Channel " + str(channelID))

        dmaEvsysEVACT = coreComponent.createKeyValueSetSymbol("DMAC_CHEVCTRL_EVACT_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysEVACT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CHEVCTRL")
        dmaEvsysEVACT.setLabel("Event Input Action")

        dmaEvsysEVACTNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHEVCTRL__EVACT\"]")
        dmaEvsysEVACTValues = dmaEvsysEVACTNode.getChildren()

        for index in range(len(dmaEvsysEVACTValues)):
            dmaEvsysEVACTKeyName = dmaEvsysEVACTValues[index].getAttribute("name")
            dmaEvsysEVACTKeyDescription = dmaEvsysEVACTValues[index].getAttribute("caption")
            dmaEvsysEVACTKeyValue = dmaEvsysEVACTValues[index].getAttribute("value")
            dmaEvsysEVACT.addKey(dmaEvsysEVACTKeyName, dmaEvsysEVACTKeyValue, dmaEvsysEVACTKeyDescription)

        dmaEvsysEVACT.setOutputMode("Value")
        dmaEvsysEVACT.setDisplayMode("Description")
        dmacDep.append("DMAC_ENABLE_CH_" + str(channelID))
        dmacDep.append("DMAC_ENABLE_EVSYS_OUT_" + str(channelID))
        dmacDep.append("DMAC_ENABLE_EVSYS_IN_" + str(channelID))

        dmacEvsys = coreComponent.createBooleanSymbol("DMAC_EVSYS_DUMMY" + str(channelID) , dmacMenu)
        dmacEvsys.setVisible(False)
        dmacEvsys.setDependencies(dmacEvsysControl, ["DMAC_ENABLE_CH_" + str(channelID), "DMAC_ENABLE_EVSYS_OUT_" + str(channelID), "DMAC_ENABLE_EVSYS_IN_" + str(channelID)])

dmacEnable.setDependencies(onChannelEnable, dmacChannelIds)
dmacHighestCh.setDependencies(onChannelEnable, dmacChannelIds)
dmacIntEnable.setDependencies(updateInterruptLogic, dmacChannelIds + dmacChannelInt)

#DMA - Source AM Mask
dmacSym_BTCTRL_SRCINC_MASK = coreComponent.createStringSymbol("DMA_SRC_AM_MASK", dmacChannelEnable)
dmacSym_BTCTRL_SRCINC_MASK.setDefaultValue("0x400")
dmacSym_BTCTRL_SRCINC_MASK.setVisible(False)

#DMA - Source FIXED_AM Value
dmacSym_BTCTRL_SRCINC_FIXED = coreComponent.createStringSymbol("DMA_SRC_FIXED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_SRCINC_FIXED.setDefaultValue("0x0")
dmacSym_BTCTRL_SRCINC_FIXED.setVisible(False)

#DMA - Source INCREMENTED_AM Value
dmacSym_BTCTRL_SRCINC_INCREMENTED = coreComponent.createStringSymbol("DMA_SRC_INCREMENTED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_SRCINC_INCREMENTED.setDefaultValue("0x400")
dmacSym_BTCTRL_SRCINC_INCREMENTED.setVisible(False)

#DMA - Destination AM Mask
dmacSym_BTCTRL_DSTIN_MASK = coreComponent.createStringSymbol("DMA_DST_AM_MASK", dmacChannelEnable)
dmacSym_BTCTRL_DSTIN_MASK.setDefaultValue("0x800")
dmacSym_BTCTRL_DSTIN_MASK.setVisible(False)

#DMA - Destination FIXED_AM Value
dmacSym_BTCTRL_DSTINC_FIXED = coreComponent.createStringSymbol("DMA_DST_FIXED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_DSTINC_FIXED.setDefaultValue("0x0")
dmacSym_BTCTRL_DSTINC_FIXED.setVisible(False)

#DMA - Destination INCREMENTED_AM Value
dmacSym_BTCTRL_DSTINC_INCREMENTED = coreComponent.createStringSymbol("DMA_DST_INCREMENTED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_DSTINC_INCREMENTED.setDefaultValue("0x800")
dmacSym_BTCTRL_DSTINC_INCREMENTED.setVisible(False)

#DMA - Data Width Mask
dmacSym_BTCTRL_BEATSIZE_MASK = coreComponent.createStringSymbol("DMA_DATA_WIDTH_MASK", dmacChannelEnable)
dmacSym_BTCTRL_BEATSIZE_MASK.setDefaultValue("0x300")
dmacSym_BTCTRL_BEATSIZE_MASK.setVisible(False)

#DMA - Beat Size BYTE Value
dmacSym_BTCTRL_BEATSIZE_BYTE = coreComponent.createStringSymbol("DMA_DATA_WIDTH_BYTE_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_BEATSIZE_BYTE.setDefaultValue("0x0")
dmacSym_BTCTRL_BEATSIZE_BYTE.setVisible(False)

#DMA - Beat Size HWORD Value
dmacSym_BTCTRL_BEATSIZE_HWORD = coreComponent.createStringSymbol("DMA_DATA_WIDTH_HALFWORD_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_BEATSIZE_HWORD.setDefaultValue("0x100")
dmacSym_BTCTRL_BEATSIZE_HWORD.setVisible(False)

#DMA - Beat Size WORD Value
dmacSym_BTCTRL_BEATSIZE_WORD = coreComponent.createStringSymbol("DMA_DATA_WIDTH_WORD_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_BEATSIZE_WORD.setDefaultValue("0x200")
dmacSym_BTCTRL_BEATSIZE_WORD.setVisible(False)

# Interface for Peripheral clients
for per in per_instance.keys():
    dmacChannelNeeded = coreComponent.createBooleanSymbol("DMA_CH_NEEDED_FOR_" + str(per), dmacMenu)
    dmacChannelNeeded.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CRCCTRL")
    dmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    dmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    dmacChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(per), dmacMenu)
    dmacChannel.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CRCCTRL")
    dmacChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    dmacChannel.setDefaultValue(-1)
    dmacChannel.setVisible(False)

dmacPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", dmacChannelEnable)
dmacPERIDChannelUpdate.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmac_u2503;register:CRCSTATUS")
dmacPERIDChannelUpdate.setLabel("Local dmacChannelAllocLogic")
dmacPERIDChannelUpdate.setVisible(False)
dmacPERIDChannelUpdate.setDependencies(dmacChannelAllocLogic, peridValueListSymbols)

InterruptVectorUpdate = []
InterruptVectorUpdate.append("core." + name + "_INTERRUPT_ENABLE_UPDATE")

# Interrupt Warning status
dmacSym_IntEnComment = coreComponent.createCommentSymbol("DMAC_INTERRUPT_ENABLE_COMMENT", dmacMenu)
dmacSym_IntEnComment.setVisible(False)
dmacSym_IntEnComment.setLabel("Warning!!! DMAC Interrupt is Disabled in Interrupt Manager")
dmacSym_IntEnComment.setDependencies(updateDMACInterruptWarringStatus, InterruptVectorUpdate)

# Clock Warning status
dmacSym_ClkEnComment = coreComponent.createCommentSymbol("DMAC_CLOCK_ENABLE_COMMENT", dmacMenu)
dmacSym_ClkEnComment.setLabel("Warning!!! DMAC Peripheral Clock is Disabled in Clock Manager")
dmacSym_ClkEnComment.setVisible(False)
dmacSym_ClkEnComment.setDependencies(updateDMACClockWarringStatus, ["core."+dmacInstanceName.getValue()+"_CLOCK_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmacHeaderFile = coreComponent.createFileSymbol("DMAC_HEADER", None)
dmacHeaderFile.setSourcePath("../peripheral/dmac_u2503/templates/plib_dmac.h.ftl")
dmacHeaderFile.setOutputName("plib_" + dmacInstanceName.getValue().lower() + ".h")
dmacHeaderFile.setDestPath("/peripheral/dmac/")
dmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacHeaderFile.setType("HEADER")
dmacHeaderFile.setMarkup(True)
dmacHeaderFile.setEnabled(False)

# Source File
dmacSourceFile = coreComponent.createFileSymbol("DMAC_SOURCE", None)
dmacSourceFile.setSourcePath("../peripheral/dmac_u2503/templates/plib_dmac.c.ftl")
dmacSourceFile.setOutputName("plib_" + dmacInstanceName.getValue().lower() + ".c")
dmacSourceFile.setDestPath("/peripheral/dmac/")
dmacSourceFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacSourceFile.setType("SOURCE")
dmacSourceFile.setMarkup(True)
dmacSourceFile.setEnabled(False)

#System Initialization
dmacSystemInitFile = coreComponent.createFileSymbol("DMAC_SYS_INIT", None)
dmacSystemInitFile.setType("STRING")
dmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmacSystemInitFile.setSourcePath("../peripheral/dmac_u2503/templates/system/initialization.c.ftl")
dmacSystemInitFile.setMarkup(True)
dmacSystemInitFile.setEnabled(False)

#System Definition
dmacSystemDefFile = coreComponent.createFileSymbol("DMAC_SYS_DEF", None)
dmacSystemDefFile.setType("STRING")
dmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmacSystemDefFile.setSourcePath("../peripheral/dmac_u2503/templates/system/definitions.h.ftl")
dmacSystemDefFile.setMarkup(True)
dmacSystemDefFile.setEnabled(False)
