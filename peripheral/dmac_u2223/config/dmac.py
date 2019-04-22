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

global dmacInstanceName
global dmacHeaderFile
global dmacSourceFile
global dmacSystemInitFile
global dmacSystemDefFile

global dmacEnable

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
def dmacGlobalLogic(symbol, event):

    global dmacActiveChannels

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
            symbol.setValue(int(dmacActiveChannels[0]) + 1, 2)

    if symbol.getID() == "DMA_ENABLE":
        if dmacActiveChannels and symbol.getValue() == False:
            symbol.setValue(True, 2)

        if not dmacActiveChannels:
            symbol.setValue(False, 2)

def onGlobalEnableLogic(symbol, event):
    global dmacInstanceName

    #clock enable
    Database.clearSymbolValue("core", dmacInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", dmacInstanceName.getValue()+"_CLOCK_ENABLE", event["value"], 2)

    InterruptVector = dmacInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = dmacInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = dmacInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, dmacInstanceName.getValue()+"_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "DMAC_Handler", 2)

    # File generation logic
    dmacHeaderFile.setEnabled(event["value"])
    dmacSourceFile.setEnabled(event["value"])
    dmacSystemInitFile.setEnabled(event["value"])
    dmacSystemDefFile.setEnabled(event["value"])

def updateDMACInterruptWarringStatus(symbol, event):

    if dmacEnable.getValue() == True:
        symbol.setVisible(event["value"])

def updateDMACClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def dmacTriggerCalc(symbol, event):

    global per_instance

    symbol.clearValue()
    symbol.setValue(per_instance.get(event["value"]), 2)

def dmacEvsysControl(symbol, event):
    channel = symbol.getID().split("DMAC_EVSYS_DUMMY")[1]

    enable = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + channel)
    input = Database.getSymbolValue("core", "DMAC_ENABLE_EVSYS_IN_" + channel)
    output = Database.getSymbolValue("core", "DMAC_ENABLE_EVSYS_OUT_" + channel)

    Database.setSymbolValue("evsys", "GENERATOR_DMAC_CH_" + channel + "_ACTIVE", (enable & output), 2)
    Database.setSymbolValue("evsys", "USER_DMAC_CH_" + channel + "_READY", (enable & input), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def dmacChannelAllocLogic(symbol, event):
    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
    perID = event["id"].split('DMA_CH_NEEDED_FOR_')[1]
    channelAllocated = False
    for i in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "DMAC_ENABLE_CH_" + str(i))
        dmaChannelPerID = str(Database.getSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_" + str(i)))
        if dmaChannelPerID == perID:
            channelAllocated = True
            break
        # Client requested to allocate channel
        if event["value"]:
            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.setSymbolValue("core", "DMAC_ENABLE_CH_" + str(i), True, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_" + str(i), perID, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_" + str(i) + "_PERID_LOCK", True, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break

        # Client requested to deallocate channel
        else:
            # Reset the previously allocated channel
            if perID == dmaChannelPerID and dmaChannelEnable == True:
                Database.setSymbolValue("core", "DMAC_ENABLE_CH_" + str(i), False, 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_" + str(i), "Software Trigger", 2)
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_" + str(i) + "_PERID_LOCK", False, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -1, 2)

    if event["value"] == True and channelAllocated == False:
        # Couldn't find any free DMA channel, hence set warning.
        Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
        Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -2, 2)

################################################################################
#### Component ####
################################################################################

# DMA_NAME: Needed to map DMA system service APIs to PLIB APIs
dmacSymAPI_Prefix = coreComponent.createStringSymbol("DMA_NAME", None)
dmacSymAPI_Prefix.setDefaultValue("DMAC")
dmacSymAPI_Prefix.setVisible(False)

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]").getChildren()

node = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"LPRAM\"]")
dmacLPRAMPresent = coreComponent.createBooleanSymbol("LPRAM_PRESENT", None)
dmacLPRAMPresent.setVisible(False)
if node != None:
    dmacLPRAMPresent.setDefaultValue(True)

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
dmacInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
dmacInstanceName.setDefaultValue(instances[0].getAttribute("name"))
dmacInstanceName.setVisible(False)

dmacChannelNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMAC\"]/instance@[name=\""+dmacInstanceName.getValue()+"\"]/parameters/param@[name=\"CH_NUM\"]")
dmacChannelCount = int(dmacChannelNode.getAttribute("value"))

dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("dmac_u2223:SAMM0DMAModel")

dmacMenu = coreComponent.createMenuSymbol("DMAC_MENU", None)
dmacMenu.setLabel("DMA (DMAC)")
dmacMenu.setDescription("DMA (DMAC) Configuration")

#Device name
dmacSym_DeviceName = coreComponent.createStringSymbol("DMAC_DEVICE_NAME", None)
dmacSym_DeviceName.setVisible(False)
dmacSym_DeviceName.setDefaultValue(Variables.get("__PROCESSOR"))

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
dmacEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", dmacMenu)
dmacEnable.setLabel("Use DMA Service ?")
dmacEnable.setVisible(False)
dmacEnable.setDefaultValue(False)

# DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
dmacChCount = coreComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmacEnable)
dmacChCount.setLabel("DMA (DMAC) Channels Count")
dmacChCount.setDefaultValue(dmacChannelCount)
dmacChCount.setVisible(False)

dmacEventCount = coreComponent.createIntegerSymbol("DMA_EVSYS_CHANNEL_COUNT", dmacEnable)
dmacEventCount.setDefaultValue(4)
dmacEventCount.setVisible(False)

dmacFileGen = coreComponent.createBooleanSymbol("DMAC_FILE_GEN", dmacEnable)
dmacFileGen.setLabel("DMA (DMAC) File Generation")
dmacFileGen.setVisible(False)
dmacFileGen.setDependencies(onGlobalEnableLogic, ["DMA_ENABLE"])

dmacHighestCh = coreComponent.createIntegerSymbol("DMAC_HIGHEST_CHANNEL", dmacEnable)
dmacHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmacHighestCh.setVisible(False)

dmacChannelLinkedList = coreComponent.createBooleanSymbol("DMAC_LL_ENABLE", dmacMenu)
dmacChannelLinkedList.setLabel("Use Linked List Mode ?")

#Priority Control 0 Register
for dmacCount in range(0, 4):

    #Level 0/1/2/3 Round-Robin Arbitration Enable
    PRICTRL0_LVLPRI_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_LVLXPRIO_" + str(dmacCount),dmacMenu)
    PRICTRL0_LVLPRI_SelectionSym.setLabel("Priority Level " + str(dmacCount) + " Arbitration Scheme")

    PRICTRL0_LVLPRI_SelectionSym.addKey("STATIC_LVL", "0", "Static Priority Arbitration")
    PRICTRL0_LVLPRI_SelectionSym.addKey("ROUND_ROBIN_LVL", "1", "Round Robin Priority Arbitration")
    PRICTRL0_LVLPRI_SelectionSym.setDefaultValue(1)
    PRICTRL0_LVLPRI_SelectionSym.setOutputMode("Value")
    PRICTRL0_LVLPRI_SelectionSym.setDisplayMode("Description")

for channelID in range(0, dmacChCount.getValue()):

    global per_instance

    dmacChannelEnable = coreComponent.createBooleanSymbol("DMAC_ENABLE_CH_" + str(channelID), dmacMenu)
    dmacChannelEnable.setLabel("Use DMAC Channel " + str(channelID))
    dmacChannelIds.append("DMAC_ENABLE_CH_" + str(channelID))

    if "SAMD21" not in dmacSym_DeviceName.getValue():
        #Channel Run in Standby
        CH_CHCTRLA_RUNSTDBY_Ctrl = coreComponent.createBooleanSymbol("DMAC_CHCTRLA_RUNSTDBY_CH_" + str(channelID), dmacChannelEnable)
        CH_CHCTRLA_RUNSTDBY_Ctrl.setLabel("Run Channel in Standby mode")

    # CHCTRLB - Trigger Source
    dmacSym_CHCTRLB_TRIGSRC = coreComponent.createComboSymbol("DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID), dmacChannelEnable, sorted(per_instance.keys()))
    dmacSym_CHCTRLB_TRIGSRC.setLabel("Trigger Source")
    dmacSym_CHCTRLB_TRIGSRC.setDefaultValue("Software Trigger")

    dmacSym_PERID_Val = coreComponent.createIntegerSymbol("DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID) + "_PERID_VAL", dmacChannelEnable)
    dmacSym_PERID_Val.setLabel("PERID Value")
    dmacSym_PERID_Val.setDefaultValue(0)
    dmacSym_PERID_Val.setDependencies(dmacTriggerCalc, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID)])
    dmacSym_PERID_Val.setVisible(False)

    # DMA manager will use LOCK symbol to lock the "DMAC_CHCTRLB_TRIGSRC_CH_ + str(channelID)" symbol
    dmacSym_CHCTRLB_TRIGSRC_LOCK = coreComponent.createBooleanSymbol("DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID) + "_PERID_LOCK", dmacChannelEnable)
    dmacSym_CHCTRLB_TRIGSRC_LOCK.setLabel("Lock DMA Request")
    dmacSym_CHCTRLB_TRIGSRC_LOCK.setVisible(False)
    dmacSym_CHCTRLB_TRIGSRC_LOCK.setUseSingleDynamicValue(True)

    # CHCTRLB - Trigger Action
    dmacSym_CHCTRLB_TRIGACT = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLB_TRIGACT_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_CHCTRLB_TRIGACT.setLabel("Trigger Action")
    dmacSym_CHCTRLB_TRIGACT.addKey("BLOCK", "0", "One Block Transfer Per DMA Request")
    dmacSym_CHCTRLB_TRIGACT.addKey("BEAT", "2", "One Beat Transfer per DMA Request")
    dmacSym_CHCTRLB_TRIGACT.setDefaultValue(0)
    dmacSym_CHCTRLB_TRIGACT.setOutputMode("Value")
    dmacSym_CHCTRLB_TRIGACT.setDisplayMode("Description")
    dmacSym_CHCTRLB_TRIGACT.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID)])

    #Channel Priority Level
    CHCTRLB_LVL_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLB_LVL_CH_" + str(channelID), dmacChannelEnable)
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
    dmacSym_BTCTRL_DSTINC_Val.setLabel("Destination Address Mode")
    dmacSym_BTCTRL_DSTINC_Val.addKey("FIXED_AM", "0", "Fixed Address Mode")
    dmacSym_BTCTRL_DSTINC_Val.addKey("INCREMENTED_AM", "1", "Increment Address After Every Transfer")
    dmacSym_BTCTRL_DSTINC_Val.setOutputMode("Key")
    dmacSym_BTCTRL_DSTINC_Val.setDisplayMode("Description")
    dmacSym_BTCTRL_DSTINC_Val.setDefaultValue(1)
    dmacSym_BTCTRL_DSTINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID)])

    # BTCTRL - Source Increment
    dmacSym_BTCTRL_SRCINC_Val = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_SRCINC_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_SRCINC_Val.setLabel("Source Address Mode")
    dmacSym_BTCTRL_SRCINC_Val.addKey("FIXED_AM", "0", "Fixed Address Mode")
    dmacSym_BTCTRL_SRCINC_Val.addKey("INCREMENTED_AM", "1", "Increment Address After Every Transfer")
    dmacSym_BTCTRL_SRCINC_Val.setOutputMode("Key")
    dmacSym_BTCTRL_SRCINC_Val.setDisplayMode("Description")
    dmacSym_BTCTRL_SRCINC_Val.setDefaultValue(1)
    dmacSym_BTCTRL_SRCINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID)])

    # BTCTRL - Beat Size
    dmacSym_BTCTRL_BEATSIZE = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_BEATSIZE_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_BEATSIZE.setLabel("Beat Size")

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
    dmacSym_BTCTRL_BEATSIZE.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_"+ str(channelID)])

    if channelID < 4:
        dmaEVSYSMenu = coreComponent.createMenuSymbol("DMAC_EVSYS_MENU" + str(channelID), dmacChannelEnable)
        dmaEVSYSMenu.setLabel("Event System Configuration")

        dmaEvsysOut = coreComponent.createBooleanSymbol("DMAC_ENABLE_EVSYS_OUT_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysOut.setLabel("Enable Event Output for Channel " + str(channelID))

        dmaEvsysEVOSEL = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_EVSYS_EVOSEL_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysEVOSEL.setLabel("Event Output Selection")

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
        dmaEvsysIn.setLabel("Enable Event Input for Channel " + str(channelID))

        dmaEvsysEVACT = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLB_EVACT_" + str(channelID), dmaEVSYSMenu)
        dmaEvsysEVACT.setLabel("Event Input Action")

        dmaEvsysEVACTNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHCTRLB__EVACT\"]")
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

dmacEnable.setDependencies(dmacGlobalLogic, dmacChannelIds)
dmacHighestCh.setDependencies(dmacGlobalLogic, dmacChannelIds)

#DMA - Source AM Mask
xdmacSym_BTCTRL_SRCINC_MASK = coreComponent.createStringSymbol("DMA_SRC_AM_MASK", dmacChannelEnable)
xdmacSym_BTCTRL_SRCINC_MASK.setDefaultValue("0x400")
xdmacSym_BTCTRL_SRCINC_MASK.setVisible(False)

#DMA - Source FIXED_AM Value
dmacSym_BTCTRL_SRCINC_FIXED = coreComponent.createStringSymbol("DMA_SRC_FIXED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_SRCINC_FIXED.setDefaultValue("0x0")
dmacSym_BTCTRL_SRCINC_FIXED.setVisible(False)

#DMA - Source INCREMENTED_AM Value
dmacSym_BTCTRL_SRCINC_INCREMENTED = coreComponent.createStringSymbol("DMA_SRC_INCREMENTED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_SRCINC_INCREMENTED.setDefaultValue("0x400")
dmacSym_BTCTRL_SRCINC_INCREMENTED.setVisible(False)

#DMA - Destination AM Mask
xdmacSym_BTCTRL_DSTIN_MASK = coreComponent.createStringSymbol("DMA_DST_AM_MASK", dmacChannelEnable)
xdmacSym_BTCTRL_DSTIN_MASK.setDefaultValue("0x800")
xdmacSym_BTCTRL_DSTIN_MASK.setVisible(False)

#DMA - Destination FIXED_AM Value
dmacSym_BTCTRL_DSTINC_FIXED = coreComponent.createStringSymbol("DMA_DST_FIXED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_DSTINC_FIXED.setDefaultValue("0x0")
dmacSym_BTCTRL_DSTINC_FIXED.setVisible(False)

#DMA - Destination INCREMENTED_AM Value
dmacSym_BTCTRL_DSTINC_INCREMENTED = coreComponent.createStringSymbol("DMA_DST_INCREMENTED_AM_VALUE", dmacChannelEnable)
dmacSym_BTCTRL_DSTINC_INCREMENTED.setDefaultValue("0x800")
dmacSym_BTCTRL_DSTINC_INCREMENTED.setVisible(False)

#DMA - Data Width Mask
xdmacSym_BTCTRL_BEATSIZE_MASK = coreComponent.createStringSymbol("DMA_DATA_WIDTH_MASK", dmacChannelEnable)
xdmacSym_BTCTRL_BEATSIZE_MASK.setDefaultValue("0x300")
xdmacSym_BTCTRL_BEATSIZE_MASK.setVisible(False)

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
    dmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    dmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    dmacChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(per), dmacMenu)
    dmacChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    dmacChannel.setDefaultValue(-1)
    dmacChannel.setVisible(False)

dmacPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", dmacChannelEnable)
dmacPERIDChannelUpdate.setLabel("Local dmacChannelAllocLogic")
dmacPERIDChannelUpdate.setVisible(False)
dmacPERIDChannelUpdate.setDependencies(dmacChannelAllocLogic, peridValueListSymbols)

dmacInterruptVectorUpdate = "DMAC_INTERRUPT_ENABLE_UPDATE"

# Interrupt Warning status
dmacSym_IntEnComment = coreComponent.createCommentSymbol("DMAC_INTERRUPT_ENABLE_COMMENT", dmacMenu)
dmacSym_IntEnComment.setVisible(False)
dmacSym_IntEnComment.setLabel("Warning!!! DMAC Interrupt is Disabled in Interrupt Manager")
dmacSym_IntEnComment.setDependencies(updateDMACInterruptWarringStatus, ["core." + dmacInterruptVectorUpdate])

# Clock Warning status
dmacSym_ClkEnComment = coreComponent.createCommentSymbol("DMAC_CLOCK_ENABLE_COMMENT", dmacMenu)
dmacSym_ClkEnComment.setLabel("Warning!!! DMAC Peripheral Clock is Disabled in Clock Manager")
dmacSym_ClkEnComment.setVisible(False)
dmacSym_ClkEnComment.setDependencies(updateDMACClockWarringStatus, ["core." + dmacInstanceName.getValue() + "_CLOCK_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmacHeaderFile = coreComponent.createFileSymbol("DMAC_HEADER", None)
dmacHeaderFile.setSourcePath("../peripheral/dmac_u2223/templates/plib_dmac.h.ftl")
dmacHeaderFile.setOutputName("plib_" + dmacInstanceName.getValue().lower() + ".h")
dmacHeaderFile.setDestPath("/peripheral/dmac/")
dmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacHeaderFile.setType("HEADER")
dmacHeaderFile.setMarkup(True)
dmacHeaderFile.setEnabled(False)

# Source File
dmacSourceFile = coreComponent.createFileSymbol("DMAC_SOURCE", None)
dmacSourceFile.setSourcePath("../peripheral/dmac_u2223/templates/plib_dmac.c.ftl")
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
dmacSystemInitFile.setSourcePath("../peripheral/dmac_u2223/templates/system/initialization.c.ftl")
dmacSystemInitFile.setMarkup(True)
dmacSystemInitFile.setEnabled(False)

#System Definition
dmacSystemDefFile = coreComponent.createFileSymbol("DMAC_SYS_DEF", None)
dmacSystemDefFile.setType("STRING")
dmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmacSystemDefFile.setSourcePath("../peripheral/dmac_u2223/templates/system/definitions.h.ftl")
dmacSystemDefFile.setMarkup(True)
dmacSystemDefFile.setEnabled(False)
