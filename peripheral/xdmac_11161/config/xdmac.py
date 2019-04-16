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

# load family specific configuration
Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

###############################################################################
# Register Information ####
###############################################################################


###############################################################################
# Global Variables ####
###############################################################################
global xdmacHeaderFile
global xdmacCommonHeaderFile
global xdmacSourceFile
global xdmacSystemInitFile
global xdmacSystemIntFile
global xdmacSystemDefFile
global xdmacSystemConfigFile
global triggerSettings

global xdmacInstanceName

# Parse atdf xml file to get instance name for the peripheral which has DMA id.
# And construct a list of PERIDs

global per_instance
per_instance = {}

global peridValueListSymbols
peridValueListSymbols = []

global xdmacActiveChannels
xdmacActiveChannels = []

global xdmacChannelIds
xdmacChannelIds = []

# Device specific XDMAC settings
triggerSettings = setXDMACDefaultSettings()

# Create lists for peripheral triggers and the corresponding ID values
node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
modules = node.getChildren()
for module in range(0, len(modules)):
    instances = modules[module].getChildren()
    for instance in range(0, len(instances)):
        options = instances[instance].getChildren()
        for option in range(0, len(options)):
            if "parameters" == options[option].getName():
                parameters = options[option].getChildren()
                for parameter in range(0, len(parameters)):
                    if "name" in parameters[parameter].getAttributeList():
                        name = str(parameters[parameter].getAttribute("name"))
                        if "DMAC_ID" in name:
                            global per_instance
                            if int(parameters[parameter].getAttribute("value")) not in per_instance.values():
                                name = name.replace('DMAC_ID_', '')
                                module = str(
                                    instances[instance].getAttribute("name"))
                                if "HSMCI" == module:
                                    if "HSMCI" not in per_instance.keys():
                                        per_instance["HSMCI"] = int(
                                            parameters[parameter].getAttribute("value"))
                                else:
                                    name = name.replace('TX', 'Transmit')
                                    name = name.replace('RX', 'Receive')
                                    name = name.replace('LEFT', 'Left')
                                    name = name.replace('RIGHT', 'Right')
                                    per_instance[module + "_" + name] = int(
                                        parameters[parameter].getAttribute("value"))

# Needs placed after above parsing as value of DMAC_ID for peripherals may be 0
per_instance["Software Trigger"] = 0

###############################################################################
# Business Logic ####
###############################################################################


def dependencyStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def xdmacTriggerLogic(xdmacSym, event):
    global triggerSettings
    SymID = xdmacSym.getID()

    if event["value"] in triggerSettings:
        trigger = event["value"]
    else:
        if "Transmit" in event["value"]:
            trigger = "Standard_Transmit"
        elif "Receive" in event["value"]:
            trigger = "Standard_Receive"
        else:
            trigger = "Standard_Transmit"

    xdmacSym.clearValue()
    if "TYPE" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][0]), 2)
    if "DSYNC" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][1]), 2)
    if "SWREQ" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][2]), 2)
    if "SAM" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][3]), 2)
    if "DAM" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][4]), 2)
    if "SIF" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][5]), 2)
    if "DIF" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][6]), 2)
    if "DWIDTH" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][7]), 2)
    if "CSIZE" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][8]), 2)
    if "MBSIZE" in str(SymID):
        xdmacSym.setSelectedKey(str(triggerSettings[trigger][9]), 2)

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the
# highest index enabled, also if the list is empty then none of the channel is
# enabled.
# Highest index will be used to create XDMAC objects in source code.
# List empty or non-empty status helps to generate/discard XDMAC code.


def xdmacGlobalLogic(xdmacGlobalSym, event):
    global xdmacActiveChannels

    index = event["id"].strip("XDMAC_CH")
    index = index.strip("_ENABLE")
    try:
        index = int(index)
    except:
        return

    if event["value"] is True:
        if index not in xdmacActiveChannels:
            xdmacActiveChannels.append(index)
    else:
        if index in xdmacActiveChannels:
            xdmacActiveChannels.remove(index)

    xdmacActiveChannels.sort()
    xdmacActiveChannels.reverse()

    xdmacGlobalSym.clearValue()
    # Check if the list is not empty first since list element is accessed in
    # the code
    if xdmacActiveChannels:
        if xdmacGlobalSym.getID() == "XDMAC_HIGHEST_CHANNEL":
            xdmacGlobalSym.setValue(int(xdmacActiveChannels[0]) + 1, 2)

    if xdmacGlobalSym.getID() == "DMA_ENABLE":
        if xdmacActiveChannels and xdmacGlobalSym.getValue() is False:
            xdmacGlobalSym.setValue(True, 2)

        if not xdmacActiveChannels:
            xdmacGlobalSym.setValue(False, 2)


def onGlobalEnableLogic(xdmacFileGen, event):

    interruptVector = xdmacInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = xdmacInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = xdmacInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue(
        "core", xdmacInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue(
        "core", xdmacInstanceName.getValue() + "_CLOCK_ENABLE", event["value"], 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, event["value"], 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, event["value"], 2)
    Database.clearSymbolValue("core", interruptHandler)

    if event["value"] == True:
        Database.setSymbolValue(
            "core", interruptHandler, xdmacInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", interruptHandler,
                                xdmacInstanceName.getValue() + "_Handler", 2)

    # File generation logic
    xdmacHeaderFile.setEnabled(event["value"])
    xdmacCommonHeaderFile.setEnabled(event["value"])
    xdmacSourceFile.setEnabled(event["value"])
    xdmacSystemInitFile.setEnabled(event["value"])
    xdmacSystemDefFile.setEnabled(event["value"])


def xdmacTriggerCalc(xdmacPERIDVal, event):
    global per_instance
    xdmacPERIDVal.clearValue()
    xdmacPERIDVal.setValue(per_instance.get(event["value"]), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"


def xdmacChannelAllocLogic(Sym, event):
    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
    perID = event["id"].split('DMA_CH_NEEDED_FOR_')[1]
    channelAllocated = False

    for i in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue(
            "core", "XDMAC_CH" + str(i) + "_ENABLE")
        dmaChannelPerID = str(Database.getSymbolValue(
            "core", "XDMAC_CC" + str(i) + "_PERID"))

        if dmaChannelPerID == perID:
            channelAllocated = True
            break
        # Client requested to allocate channel
        if event["value"] == True:
            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.setSymbolValue(
                    "core", "XDMAC_CH" + str(i) + "_ENABLE", True, 2)
                Database.setSymbolValue(
                    "core", "XDMAC_CC" + str(i) + "_PERID", perID, 2)
                Database.setSymbolValue(
                    "core", "XDMAC_CC" + str(i) + "_PERID_LOCK", True, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break

        # Client requested to deallocate channel
        else:
            # Reset the previously allocated channel
            if perID == dmaChannelPerID and dmaChannelEnable == True:
                Database.setSymbolValue(
                    "core", "XDMAC_CH" + str(i) + "_ENABLE", False, 2)
                Database.setSymbolValue(
                    "core", "XDMAC_CC" + str(i) + "_PERID", "Software Trigger", 2)
                Database.setSymbolValue(
                    "core", "XDMAC_CC" + str(i) + "_PERID_LOCK", False, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -1, 2)
                channelAllocated = True
                break

    if event["value"] == True and channelAllocated == False:
        Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -2, 2)
        Log.writeWarningMessage(
            "Warning!!! Couldn't Allocate any DMA Channel. Check DMA manager.")


###############################################################################
# Component ####
###############################################################################
dmaManagerSelect = coreComponent.createStringSymbol(
    "DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("xdmac_11161:SAME70DMAModel")

xdmacMenu = coreComponent.createMenuSymbol("XDMAC_MENU", None)
xdmacMenu.setLabel("DMA (XDMAC)")
xdmacMenu.setDescription("DMA (XDMAC) Configuration")

# DMA_NAME: Needed to map DMA system service APIs to PLIB APIs
xdmacSymAPI_Prefix = coreComponent.createStringSymbol("DMA_NAME", None)
xdmacSymAPI_Prefix.setDefaultValue("XDMAC")
xdmacSymAPI_Prefix.setVisible(False)

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
xdmacInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
instances = ATDF.getNode(
    "/avr-tools-device-file/devices/device/peripherals/module@[name=\"XDMAC\"]").getChildren()
xdmacInstanceName.setDefaultValue(instances[0].getAttribute("name"))
xdmacInstanceName.setVisible(False)

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
xdmacEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", xdmacMenu)
xdmacEnable.setLabel("Use DMA Service?")
xdmacEnable.setVisible(False)
xdmacEnable.setDefaultValue(False)

# DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
countNode = ATDF.getNode(
    '/avr-tools-device-file/modules/module@[name="XDMAC"]/register-group@[name="XDMAC"]/register-group@[name="XDMAC_CHID"]')
xdmacChCount = coreComponent.createIntegerSymbol(
    "DMA_CHANNEL_COUNT", xdmacEnable)
xdmacChCount.setLabel("DMA (XDMAC) Channels Count")
xdmacChCount.setDefaultValue(int(countNode.getAttribute("count")))
# xdmacChCount.setVisible(False)

xdmacFileGen = coreComponent.createBooleanSymbol("XDMAC_FILE_GEN", xdmacEnable)
xdmacFileGen.setLabel("DMA (XDMAC) File Generation")
xdmacFileGen.setDependencies(onGlobalEnableLogic, ["DMA_ENABLE"])
xdmacFileGen.setVisible(False)

xdmacHighestCh = coreComponent.createIntegerSymbol(
    "XDMAC_HIGHEST_CHANNEL", xdmacEnable)
xdmacHighestCh.setLabel("DMA (XDMAC) Highest Active Channel")
xdmacHighestCh.setVisible(False)

xdmacChannelLinkedList = coreComponent.createBooleanSymbol(
    "XDMAC_LL_ENABLE", xdmacMenu)
xdmacChannelLinkedList.setLabel("Use Linked List Mode?")
xdmacChannelLinkedList.setDefaultValue(False)


for channelID in range(0, xdmacChCount.getValue()):
    global per_instance
    xdmacChannelEnable = coreComponent.createBooleanSymbol(
        "XDMAC_CH" + str(channelID) + "_ENABLE", xdmacMenu)
    xdmacChannelEnable.setLabel("Use XDMAC Channel " + str(channelID))
    xdmacChannelEnable.setDefaultValue(False)
    xdmacChannelEnable.setUseSingleDynamicValue(True)
    xdmacChannelIds.append("XDMAC_CH" + str(channelID) + "_ENABLE")

    xdmacChannelMenu = coreComponent.createMenuSymbol(
        "XDMAC_CH" + str(channelID) + "CONFIG", xdmacChannelEnable)
    xdmacChannelMenu.setLabel("XDMAC Channel " + str(channelID) + " Settings")
    xdmacChannelMenu.setDescription(
        "Configuration for DMA Channel" + str(channelID))

    xdmacSym_CC_PERID = coreComponent.createComboSymbol(
        "XDMAC_CC" + str(channelID) + "_PERID", xdmacChannelMenu, sorted(per_instance.keys()))
    xdmacSym_CC_PERID.setLabel("DMA Request")
    xdmacSym_CC_PERID.setDefaultValue("Software Trigger")
    xdmacSym_CC_PERID.setUseSingleDynamicValue(True)

    # DMA manager will use LOCK symbol to lock the "XDMAC_CC"+ str(channelID)+"_PERID" symbol
    xdmacSym_CC_PERID_LOCK = coreComponent.createBooleanSymbol(
        "XDMAC_CC" + str(channelID) + "_PERID_LOCK", xdmacChannelMenu)
    xdmacSym_CC_PERID_LOCK.setLabel("Lock DMA Request")
    xdmacSym_CC_PERID_LOCK.setVisible(False)
    xdmacSym_CC_PERID_LOCK.setDefaultValue(False)
    xdmacSym_CC_PERID_LOCK.setUseSingleDynamicValue(True)

    xdmacSym_CC_PERID_Val = coreComponent.createIntegerSymbol(
        "XDMAC_CC" + str(channelID) + "_PERID_VAL", xdmacChannelMenu)
    xdmacSym_CC_PERID_Val.setLabel("PERID Value")
    xdmacSym_CC_PERID_Val.setDefaultValue(200)
    xdmacSym_CC_PERID_Val.setDependencies(
        xdmacTriggerCalc, ["XDMAC_CC" + str(channelID) + "_PERID"])
    xdmacSym_CC_PERID_Val.setVisible(False)

    xdmacSym_CC_TYPE = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_TYPE", xdmacChannelMenu)
    xdmacSym_CC_TYPE.setLabel("DMA Transfer Type")
    xdmacSym_CC_TYPE.addKey("MEM_TRAN", "0", "Transfer From Memory To Memory")
    xdmacSym_CC_TYPE.addKey(
        "PER_TRAN", "1", "Transfer Between Peripheral And Memory")
    xdmacSym_CC_TYPE.setOutputMode("Key")
    xdmacSym_CC_TYPE.setDisplayMode("Description")
    xdmacSym_CC_TYPE.setDefaultValue(0)
    xdmacSym_CC_TYPE.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_DSYNC = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_DSYNC", xdmacChannelMenu)
    xdmacSym_CC_DSYNC.setLabel("DMA Transfer Direction")
    xdmacSym_CC_DSYNC.addKey("PER2MEM", "0", "Peripheral To Memory Transfer")
    xdmacSym_CC_DSYNC.addKey("MEM2PER", "1", "Memory To Peripheral Transfer")
    xdmacSym_CC_DSYNC.setOutputMode("Key")
    xdmacSym_CC_DSYNC.setDisplayMode("Description")
    xdmacSym_CC_DSYNC.setDefaultValue(0)
    xdmacSym_CC_DSYNC.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_SWREQ = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_SWREQ", xdmacChannelMenu)
    xdmacSym_CC_SWREQ.setLabel("DMA Request Type")
    xdmacSym_CC_SWREQ.addKey("HWR_CONNECTED", "0",
                             "Peripheral Generates DMA Request")
    xdmacSym_CC_SWREQ.addKey("SWR_CONNECTED", "1",
                             "Software Initiates DMA Request")
    xdmacSym_CC_SWREQ.setOutputMode("Key")
    xdmacSym_CC_SWREQ.setDisplayMode("Description")
    xdmacSym_CC_SWREQ.setDefaultValue(1)
    xdmacSym_CC_SWREQ.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_SAM = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_SAM", xdmacChannelMenu)
    xdmacSym_CC_SAM.setLabel("Source Addressing Mode")
    xdmacSym_CC_SAM.addKey("FIXED_AM", "0", "Fixed Address Mode")
    xdmacSym_CC_SAM.addKey("INCREMENTED_AM", "1",
                           "Increment Address After Every Transfer")
    xdmacSym_CC_SAM.setOutputMode("Key")
    xdmacSym_CC_SAM.setDisplayMode("Description")
    xdmacSym_CC_SAM.setDefaultValue(1)
    xdmacSym_CC_SAM.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_DAM = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_DAM", xdmacChannelMenu)
    xdmacSym_CC_DAM.setLabel("Destination Addressing Mode")
    xdmacSym_CC_DAM.addKey("FIXED_AM", "0", "Fixed Address Mode")
    xdmacSym_CC_DAM.addKey("INCREMENTED_AM", "1",
                           "Increment Address After Every Transfer")
    xdmacSym_CC_DAM.setOutputMode("Key")
    xdmacSym_CC_DAM.setDisplayMode("Description")
    xdmacSym_CC_DAM.setDefaultValue(1)
    xdmacSym_CC_DAM.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_SIF = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_SIF", xdmacChannelMenu)
    xdmacSym_CC_SIF.setLabel("DMA Interface Bus To Read Source Data")
    xdmacSym_CC_SIF.addKey("AHB_IF0", "0", "DMA Interface Bus 0")
    xdmacSym_CC_SIF.addKey("AHB_IF1", "1", "DMA Interface Bus 1")
    xdmacSym_CC_SIF.setOutputMode("Key")
    xdmacSym_CC_SIF.setDisplayMode("Description")
    xdmacSym_CC_SIF.setDefaultValue(1)
    xdmacSym_CC_SIF.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_DIF = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_DIF", xdmacChannelMenu)
    xdmacSym_CC_DIF.setLabel("DMA Interface Bus To Write Destination Data")
    xdmacSym_CC_DIF.addKey("AHB_IF0", "0", "DMA Interface Bus 0")
    xdmacSym_CC_DIF.addKey("AHB_IF1", "1", "DMA Interface Bus 1")
    xdmacSym_CC_DIF.setOutputMode("Key")
    xdmacSym_CC_DIF.setDisplayMode("Description")
    xdmacSym_CC_DIF.setDefaultValue(1)
    xdmacSym_CC_DIF.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_DWIDTH = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_DWIDTH", xdmacChannelMenu)
    xdmacSym_CC_DWIDTH.setLabel("Data Width")
    xdmacSym_CC_DWIDTH.addKey("BYTE", "0", "8-Bits")
    xdmacSym_CC_DWIDTH.addKey("HALFWORD", "1", "16-Bits")
    xdmacSym_CC_DWIDTH.addKey("WORD", "2", "32-Bits")
    xdmacSym_CC_DWIDTH.setOutputMode("Key")
    xdmacSym_CC_DWIDTH.setDisplayMode("Description")
    xdmacSym_CC_DWIDTH.setDefaultValue(0)
    xdmacSym_CC_DWIDTH.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_CSIZE = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_CSIZE", xdmacChannelMenu)
    xdmacSym_CC_CSIZE.setLabel("Data Transfers Per DMA Request")
    xdmacSym_CC_CSIZE.addKey("CHK_1", "0", "1 Transfer Per Request")
    xdmacSym_CC_CSIZE.addKey("CHK_2", "1", "2 Transfers Per Request")
    xdmacSym_CC_CSIZE.addKey("CHK_4", "2", "4 Transfers Per Request")
    xdmacSym_CC_CSIZE.addKey("CHK_8", "3", "8 Transfers Per Request")
    xdmacSym_CC_CSIZE.addKey("CHK_16", "4", "16 Transfers Per Request")
    xdmacSym_CC_CSIZE.setOutputMode("Key")
    xdmacSym_CC_CSIZE.setDisplayMode("Description")
    xdmacSym_CC_CSIZE.setDefaultValue(0)
    xdmacSym_CC_CSIZE.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

    xdmacSym_CC_MBSIZE = coreComponent.createKeyValueSetSymbol(
        "XDMAC_CC" + str(channelID) + "_MBSIZE", xdmacChannelMenu)
    xdmacSym_CC_MBSIZE.setLabel("Burst Size For Memory To Memory Transfer")
    xdmacSym_CC_MBSIZE.addKey("SINGLE", "0", "1 Transfer Per Burst")
    xdmacSym_CC_MBSIZE.addKey("FOUR", "1", "4 Transfers Per Burst")
    xdmacSym_CC_MBSIZE.addKey("EIGHT", "2", "8 Transfers Per Burst")
    xdmacSym_CC_MBSIZE.addKey("SIXTEEN", "3", "16 Transfers Per Burst")
    xdmacSym_CC_MBSIZE.setOutputMode("Key")
    xdmacSym_CC_MBSIZE.setDisplayMode("Description")
    xdmacSym_CC_MBSIZE.setDefaultValue(0)
    xdmacSym_CC_MBSIZE.setDependencies(
        xdmacTriggerLogic, ["XDMAC_CC" + str(channelID) + "_PERID"])

xdmacEnable.setDependencies(xdmacGlobalLogic, xdmacChannelIds)
xdmacHighestCh.setDependencies(xdmacGlobalLogic, xdmacChannelIds)

# DMA - Source AM Mask
xdmacSym_CC_SAM_MASK = coreComponent.createStringSymbol(
    "DMA_SRC_AM_MASK", xdmacChannelMenu)
xdmacSym_CC_SAM_MASK.setDefaultValue("0x30000")
xdmacSym_CC_SAM_MASK.setVisible(False)

# DMA - Source FIXED_AM Value
xdmacSym_CC_SAM_FIXED = coreComponent.createStringSymbol(
    "DMA_SRC_FIXED_AM_VALUE", xdmacChannelMenu)
xdmacSym_CC_SAM_FIXED.setDefaultValue("0x0")
xdmacSym_CC_SAM_FIXED.setVisible(False)

# DMA - Source INCREMENTED_AM Value
xdmacSym_CC_SAM_INCREMENTED = coreComponent.createStringSymbol(
    "DMA_SRC_INCREMENTED_AM_VALUE", xdmacChannelMenu)
xdmacSym_CC_SAM_INCREMENTED.setDefaultValue("0x10000")
xdmacSym_CC_SAM_INCREMENTED.setVisible(False)

# DMA - Destination AM Mask
xdmacSym_CC_DAM_MASK = coreComponent.createStringSymbol(
    "DMA_DST_AM_MASK", xdmacChannelMenu)
xdmacSym_CC_DAM_MASK.setDefaultValue("0xC0000")
xdmacSym_CC_DAM_MASK.setVisible(False)

# DMA - Destination FIXED_AM Value
xdmacSym_CC_DAM_FIXED = coreComponent.createStringSymbol(
    "DMA_DST_FIXED_AM_VALUE", xdmacChannelMenu)
xdmacSym_CC_DAM_FIXED.setDefaultValue("0x0")
xdmacSym_CC_DAM_FIXED.setVisible(False)

# DMA - Destination INCREMENTED_AM Value
xdmacSym_CC_DAM_INCREMENTED = coreComponent.createStringSymbol(
    "DMA_DST_INCREMENTED_AM_VALUE", xdmacChannelMenu)
xdmacSym_CC_DAM_INCREMENTED.setDefaultValue("0x40000")
xdmacSym_CC_DAM_INCREMENTED.setVisible(False)

# DMA - Data Width Mask
xdmacSym_CC_DWIDTH_MASK = coreComponent.createStringSymbol(
    "DMA_DATA_WIDTH_MASK", xdmacChannelMenu)
xdmacSym_CC_DWIDTH_MASK.setDefaultValue("0x1800")
xdmacSym_CC_DWIDTH_MASK.setVisible(False)

# DMA - Data Width BYTE Value
xdmacSym_CC_DWIDTH_BYTE = coreComponent.createStringSymbol(
    "DMA_DATA_WIDTH_BYTE_VALUE", xdmacChannelMenu)
xdmacSym_CC_DWIDTH_BYTE.setDefaultValue("0x0")
xdmacSym_CC_DWIDTH_BYTE.setVisible(False)

# DMA - Data Width HALFWORD Value
xdmacSym_CC_DWIDTH_HALFWORD = coreComponent.createStringSymbol(
    "DMA_DATA_WIDTH_HALFWORD_VALUE", xdmacChannelMenu)
xdmacSym_CC_DWIDTH_HALFWORD.setDefaultValue("0x800")
xdmacSym_CC_DWIDTH_HALFWORD.setVisible(False)

# DMA - Data Width WORD Value
xdmacSym_CC_DWIDTH_WORD = coreComponent.createStringSymbol(
    "DMA_DATA_WIDTH_WORD_VALUE", xdmacChannelMenu)
xdmacSym_CC_DWIDTH_WORD.setDefaultValue("0x1000")
xdmacSym_CC_DWIDTH_WORD.setVisible(False)

# Interface for Peripheral clients
for per in per_instance.keys():
    xdmacChannelNeeded = coreComponent.createBooleanSymbol(
        "DMA_CH_NEEDED_FOR_" + str(per), xdmacChannelMenu)
    xdmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    xdmacChannelNeeded.setDefaultValue(False)
    xdmacChannelNeeded.setUseSingleDynamicValue(True)
    xdmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    xdmacChannel = coreComponent.createIntegerSymbol(
        "DMA_CH_FOR_" + str(per), xdmacChannelMenu)
    xdmacChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    xdmacChannel.setDefaultValue(-1)
    xdmacChannel.setUseSingleDynamicValue(True)
    xdmacChannel.setVisible(False)

xdmacPERIDChannelUpdate = coreComponent.createBooleanSymbol(
    "DMA_CHANNEL_ALLOC", xdmacChannelMenu)
xdmacPERIDChannelUpdate.setLabel("Local xdmacChannelAllocLogic")
xdmacPERIDChannelUpdate.setDefaultValue(False)
xdmacPERIDChannelUpdate.setVisible(False)
xdmacPERIDChannelUpdate.setDependencies(
    xdmacChannelAllocLogic, peridValueListSymbols)

################################################################################
#### Dependency ####
################################################################################


################################################################################
#### Code Generation ####
################################################################################
configName = Variables.get("__CONFIGURATION_NAME")

xdmacCommonHeaderFile = coreComponent.createFileSymbol(
    "xdmacCommonHeaderFile", None)
xdmacCommonHeaderFile.setMarkup(False)
xdmacCommonHeaderFile.setSourcePath(
    "../peripheral/xdmac_11161/templates/plib_xdmac_common.h")
xdmacCommonHeaderFile.setOutputName("plib_xdmac_common.h")
xdmacCommonHeaderFile.setDestPath("/peripheral/xdmac/")
xdmacCommonHeaderFile.setProjectPath(
    "config/" + configName + "/peripheral/xdmac/")
xdmacCommonHeaderFile.setType("HEADER")
xdmacCommonHeaderFile.setOverwrite(True)
xdmacCommonHeaderFile.setEnabled(False)

xdmacHeaderFile = coreComponent.createFileSymbol("xdmacHeaderFile", None)
xdmacHeaderFile.setMarkup(True)
xdmacHeaderFile.setSourcePath(
    "../peripheral/xdmac_11161/templates/plib_xdmac.h.ftl")
xdmacHeaderFile.setOutputName(
    "plib_" + xdmacInstanceName.getValue().lower() + ".h")
xdmacHeaderFile.setDestPath("/peripheral/xdmac/")
xdmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/xdmac/")
xdmacHeaderFile.setType("HEADER")
xdmacHeaderFile.setOverwrite(True)
xdmacHeaderFile.setEnabled(False)

xdmacSourceFile = coreComponent.createFileSymbol("xdmacSourceFile", None)
xdmacSourceFile.setMarkup(True)
xdmacSourceFile.setSourcePath(
    "../peripheral/xdmac_11161/templates/plib_xdmac.c.ftl")
xdmacSourceFile.setOutputName(
    "plib_" + xdmacInstanceName.getValue().lower() + ".c")
xdmacSourceFile.setDestPath("/peripheral/xdmac/")
xdmacSourceFile.setProjectPath("config/" + configName + "/peripheral/xdmac/")
xdmacSourceFile.setType("SOURCE")
xdmacSourceFile.setOverwrite(True)
xdmacSourceFile.setEnabled(False)

xdmacSystemInitFile = coreComponent.createFileSymbol(
    "xdmacSystemInitFile", None)
xdmacSystemInitFile.setType("STRING")
xdmacSystemInitFile.setOutputName(
    "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
xdmacSystemInitFile.setSourcePath(
    "../peripheral/xdmac_11161/templates/system/initialization.c.ftl")
xdmacSystemInitFile.setMarkup(True)
xdmacSystemInitFile.setEnabled(False)

xdmacSystemDefFile = coreComponent.createFileSymbol("xdmacSystemDefFile", None)
xdmacSystemDefFile.setType("STRING")
xdmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
xdmacSystemDefFile.setSourcePath(
    "../peripheral/xdmac_11161/templates/system/definitions.h.ftl")
xdmacSystemDefFile.setMarkup(True)
xdmacSystemDefFile.setEnabled(False)
