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
global createPeripheralTrigger_IDMap
global dmaInterruptUpdate
global setDMAInterruptData

global dmaInstanceName
dmaInstanceName = ""

global per_instance
per_instance = {}

global peridValueListSymbols
peridValueListSymbols = []

global dmaActiveChannels
dmaActiveChannels = []

global dmaChannelIds
dmaChannelIds = []

global dmaTransferSizeValues
global dmaTransferDirValues


################################################################################
#### Business Logic ####
################################################################################

def setDMAInterruptData(dma_interrupt_name, status):

    print "dma_interrupt_name = " + dma_interrupt_name
    print "status = " + str(status)

    Database.setSymbolValue("core", dma_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", dma_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", dma_interrupt_name + "_INTERRUPT_HANDLER", dma_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", dma_interrupt_name + "_INTERRUPT_HANDLER", dma_interrupt_name + "_Handler", 1)

def dmaInterruptUpdate(channel, status, dmaInterruptType):
    global setDMAInterruptData
    interruptNameDir = "DMA_CH0" + str(channel)
    interruptNameAgg = "DMA_CH0" + str(channel) + "_GRP"

    if dmaInterruptType == "AGGREGATE":
        setDMAInterruptData(interruptNameDir, False)
        setDMAInterruptData(interruptNameAgg, status)
    else:
        setDMAInterruptData(interruptNameAgg, False)
        setDMAInterruptData(interruptNameDir, status)

def interruptTypeChange(symbol, event):
    global dmaInterruptUpdate
    channelCount = event["source"].getSymbolByID("DMA_CHANNEL_COUNT").getValue()
    dmaInterruptType = symbol.getSelectedKey()

    for channel in range(0, channelCount):
        isChannelEnabled = event["source"].getSymbolByID("DMA_ENABLE_CH_" + str(channel)).getValue()
        dmaInterruptUpdate(channel, isChannelEnabled, dmaInterruptType)

#-------------------------------------------------------------------------------------------------------------------------#
def onDMAChannelEnable(symbol, event):
    global dmaActiveChannels

    channel = event["id"].strip("DMA_ENABLE_CH_")

    try:
        channel = int(channel)
    except:
        return

    # Update the list of active DMA channels
    if event["value"] == True:
        if channel not in dmaActiveChannels:
            dmaActiveChannels.append(channel)
    else :
        if channel in dmaActiveChannels:
            dmaActiveChannels.remove(channel)

    if symbol.getID() == "DMA_ENABLE":
        # Set DMA_ENABLE to true if atleast one channel is enabled
        symbol.setValue(len(dmaActiveChannels) > 0, 2)
    elif symbol.getID() == "DMA_HIGHEST_CHANNEL":
        dmaActiveChannels.sort()
        dmaActiveChannels.reverse()
        if dmaActiveChannels:
            symbol.setValue(int(dmaActiveChannels[0]) + 1, 2)
        else:
            symbol.setValue(0)

    dmaInterruptType = event["source"].getSymbolByID("DMA_INTERRUPT_TYPE").getSelectedKey()
    dmaInterruptUpdate(channel, event["value"], dmaInterruptType)

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
            hwFlowCtrlDev = localComponent.getSymbolByID("DMA_HW_FLOW_CTRL_DEV_CH_" + str(i)).getSelectedKey()

            if hwFlowCtrlDev == perID:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(i), True, 2)
                localComponent.setSymbolValue("DMA_HW_FLOW_CTRL_DEV_CH_" + str(i) + "_PERID_LOCK", True, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, i, 2)
                channelAllocated = True
                break

            # Reserve the first available free channel
            if dmaChannelEnable == False:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(i), True, 2)
                localComponent.setSymbolValue("DMA_ENABLE_HW_FLOW_CTRL_CH_" + str(i), True)
                localComponent.getSymbolByID("DMA_HW_FLOW_CTRL_DEV_CH_" + str(i)).setSelectedKey(perID)
                localComponent.setSymbolValue("DMA_HW_FLOW_CTRL_DEV_CH_" + str(i) + "_PERID_LOCK", True, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, i, 2)
                localComponent.setSymbolValue("DMA_MEMORY_ADDR_INC_CH_" + str(i), True)
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
            hwFlowCtrlDev = localComponent.getSymbolByID("DMA_HW_FLOW_CTRL_DEV_CH_" + str(channelNumber)).getSelectedKey()
            # Reset the previously allocated channel
            if perID == hwFlowCtrlDev and dmaChannelEnable == True:
                localComponent.setSymbolValue("DMA_ENABLE_CH_" + str(channelNumber), False, 2)
                localComponent.setSymbolValue("DMA_ENABLE_HW_FLOW_CTRL_CH_" + str(i), False)
                hwFlowCtrlDev = localComponent.getSymbolByID("DMA_HW_FLOW_CTRL_DEV_CH_" + str(channelNumber))
                hwFlowCtrlDev.setDefaultValue(hwFlowCtrlDev.getDefaultValue())
                localComponent.setSymbolValue("DMA_HW_FLOW_CTRL_DEV_CH_" + str(channelNumber) + "_PERID_LOCK", False, 2)
                localComponent.setSymbolValue("DMA_CH_FOR_" + perID, -1, 2)
                localComponent.setSymbolValue("DMA_MEMORY_ADDR_INC_CH_" + str(i), False)

def setVisibleOnDMAChEnable(symbol, event):
    symbol.setVisible(event["value"])

def updateConfigOnFillEnable(symbol, event):
    isFillEnabled = event["value"]

    dmaEnHwFlowCtrl = event["source"].getSymbolByID("DMA_ENABLE_HW_FLOW_CTRL_CH_1")
    dmaEnHwFlowCtrl.setReadOnly(isFillEnabled == True)
    dmaEnHwFlowCtrl.setValue(False)
    
    dmaDevAddrInc = event["source"].getSymbolByID("DMA_DEVICE_ADDR_INC_CH_1")
    dmaDevAddrInc.setReadOnly(isFillEnabled == True)
    dmaDevAddrInc.setValue(True)
    
    dmaMemAddrInc = event["source"].getSymbolByID("DMA_MEMORY_ADDR_INC_CH_1")
    dmaMemAddrInc.setReadOnly(isFillEnabled == True)
    dmaMemAddrInc.setValue(True)
    
    dmaTransferDir = event["source"].getSymbolByID("DMA_TRANFER_DIR_CH_1")
    dmaTransferDir.setReadOnly(isFillEnabled == True)
    dmaTransferDir.setSelectedKey("DEV_TO_MEM")        
        
        

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
                            if "DMA_ID" in name:
                                if int(parameters[parameter].getAttribute("value")) not in per_instance.values():
                                    name = name.replace('DMA_ID_', '')
                                    name = name.replace('TX', 'Transmit')
                                    name = name.replace('RX', 'Receive')
                                    name = name.replace('LEFT', 'Left')
                                    name = name.replace('RIGHT', 'Right')
                                    per_instance[module + "_" + name] = int(parameters[parameter].getAttribute("value"))

    # Needs placed after above parsing as value of DMA_ID for peripherals may be 0
    per_instance["Software Trigger"] = 0

def DMA_ATDF_Read(coreComponent, dmaEnable):
    dmaChannelCount = 0

    global createPeripheralTrigger_IDMap
    global dmaTransferSizeValues
    global dmaTransferDirValues

    dmaChannelCount = int(ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="DMA_MAIN"]/instance@[name="DMA_MAIN"]/parameters/param@[name="CH_NUM"]').getAttribute("value"))

    # DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
    dmaChCount = coreComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmaEnable)
    dmaChCount.setLabel("DMA (DMAC) Channels Count")
    dmaChCount.setDefaultValue(dmaChannelCount)
    dmaChCount.setVisible(False)

    # DMA transfer size
    dmaTransferSizeValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA_CHAN00\"]/value-group@[name=\"DMA_CHAN00_CTRL__TRANS_SIZE\"]").getChildren()

    # DMA transfer direction
    dmaTransferDirValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMA_CHAN00\"]/value-group@[name=\"DMA_CHAN00_CTRL__TX_DIR\"]").getChildren()


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

#instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMA\"]").getChildren()

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
dmaInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
dmaInstanceName.setDefaultValue("DMA")
dmaInstanceName.setVisible(False)

# dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
# dmaManagerSelect.setVisible(False)
# dmaManagerSelect.setDefaultValue("dma_03639:PIC32CZDMAModel")

dmaMenu = coreComponent.createMenuSymbol("DMA_MENU", None)
dmaMenu.setLabel("DMA (DMAC)")
dmaMenu.setDescription("DMA (DMAC) Configuration")

# DMA_IP: Needed to generate IP specific code in DMA System Service
dmaPLIBIp = coreComponent.createStringSymbol("DMA_IP", dmaMenu)
dmaPLIBIp.setLabel("DMA IP")
dmaPLIBIp.setDefaultValue("dma_85")
dmaPLIBIp.setVisible(False)

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
dmaEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", dmaMenu)
dmaEnable.setLabel("Use DMA Service ?")
dmaEnable.setVisible(True)
dmaEnable.setReadOnly(True)
dmaEnable.setDefaultValue(False)

# Enable only low-level APIs 
dmaLowLevelAPIOnly = coreComponent.createBooleanSymbol("DMA_LOW_LEVEL_API_ONLY", dmaEnable)
dmaLowLevelAPIOnly.setLabel("Generate low-level APIs only")
dmaLowLevelAPIOnly.setDefaultValue(False)
dmaLowLevelAPIOnly.setVisible(True)

# Interrupt type selection
dmaInterruptType = coreComponent.createKeyValueSetSymbol("DMA_INTERRUPT_TYPE", dmaEnable)
dmaInterruptType.setLabel("Interrupt Type")
dmaInterruptType.addKey("DIRECT", "0", "Direct")
dmaInterruptType.addKey("AGGREGATE", "1", "Aggregate")
dmaInterruptType.setDefaultValue(0)
dmaInterruptType.setDisplayMode("Description")
dmaInterruptType.setOutputMode("Key")
dmaInterruptType.setVisible(True)
dmaInterruptType.setDependencies(interruptTypeChange, ["DMA_INTERRUPT_TYPE"])

# Needed for code generation
dmaHighestCh = coreComponent.createIntegerSymbol("DMA_HIGHEST_CHANNEL", dmaEnable)
dmaHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmaHighestCh.setVisible(False)


DMA_ATDF_Read(coreComponent, dmaEnable)

channelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")

for channelID in range(0, channelCount):

    global per_instance
    global dmaTransferSizeValues
    global dmaTransferDirValues

    # Channel enable
    dmaChannelEnable = coreComponent.createBooleanSymbol("DMA_ENABLE_CH_" + str(channelID), dmaMenu)
    dmaChannelEnable.setLabel("Use DMA Channel " + str(channelID))
    dmaChannelEnable.setDefaultValue(False)
    dmaChannelEnable.setDependencies(onDMAChannelEnable, ["DMA_ENABLE_CH_" + str(channelID)])
    dmaChannelIds.append("DMA_ENABLE_CH_" + str(channelID))

    # Enable hardware flow control?
    dmaHwFlowCtrlEn = coreComponent.createBooleanSymbol("DMA_ENABLE_HW_FLOW_CTRL_CH_" + str(channelID), dmaChannelEnable)
    dmaHwFlowCtrlEn.setLabel("Enable hardware flow control")
    dmaHwFlowCtrlEn.setDefaultValue(True)
    dmaHwFlowCtrlEn.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])

    # Select hardware flow control device
    dmaHwFlowCtrlDevice = coreComponent.createKeyValueSetSymbol("DMA_HW_FLOW_CTRL_DEV_CH_" + str(channelID), dmaHwFlowCtrlEn)
    dmaHwFlowCtrlDevice.setLabel("Hardware flow control device")
    hardwareFlowCtrlDevKeyList = sorted(per_instance.keys())

    for index in range(len(hardwareFlowCtrlDevKeyList)):
        key = hardwareFlowCtrlDevKeyList[index]
        value = per_instance[key]
        description = key
        dmaHwFlowCtrlDevice.addKey(key, str(value), description)
    dmaHwFlowCtrlDevice.setOutputMode("Value")
    dmaHwFlowCtrlDevice.setDisplayMode("Description")
    dmaHwFlowCtrlDevice.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_HW_FLOW_CTRL_CH_" + str(channelID)])
    
    # DMA manager will use LOCK symbol to lock the "DMA_HW_FLOW_CTRL_DEV_CH_ + str(channelID)" symbol
    dmaHwFlowCtrlDevLock = coreComponent.createBooleanSymbol("DMA_HW_FLOW_CTRL_DEV_CH_" + str(channelID) + "_PERID_LOCK", dmaChannelEnable)
    dmaHwFlowCtrlDevLock.setLabel("Lock DMA Request")
    dmaHwFlowCtrlDevLock.setVisible(False)
    dmaHwFlowCtrlDevLock.setUseSingleDynamicValue(True)

    # Select DMA transfer size
    dmaTransferSize = coreComponent.createKeyValueSetSymbol("DMA_TRANS_SIZE_CH_" + str(channelID), dmaChannelEnable)
    dmaTransferSize.setLabel("Transfer Size")

    for index in range(len(dmaTransferSizeValues)):
        key = dmaTransferSizeValues[index].getAttribute("name")
        desc = dmaTransferSizeValues[index].getAttribute("caption")
        val = dmaTransferSizeValues[index].getAttribute("value")
        dmaTransferSize.addKey(key, val, desc)
    dmaTransferSize.setOutputMode("Value")
    dmaTransferSize.setDisplayMode("Description")
    dmaTransferSize.setDefaultValue(0)
    dmaTransferSize.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])

    # Device address increment
    dmaDevAddrInc = coreComponent.createBooleanSymbol("DMA_DEVICE_ADDR_INC_CH_" + str(channelID), dmaChannelEnable)
    dmaDevAddrInc.setLabel("Device address increment")
    dmaDevAddrInc.setDefaultValue(False)
    dmaDevAddrInc.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])

    # Memory address increment
    dmaMemAddrInc = coreComponent.createBooleanSymbol("DMA_MEMORY_ADDR_INC_CH_" + str(channelID), dmaChannelEnable)
    dmaMemAddrInc.setLabel("Memory address increment")
    dmaMemAddrInc.setDefaultValue(False)
    dmaMemAddrInc.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])

    # Transfer Direction
    dmaTransferDir = coreComponent.createKeyValueSetSymbol("DMA_TRANFER_DIR_CH_" + str(channelID), dmaChannelEnable)
    dmaTransferDir.setLabel("Transfer direction")

    for index in range(len(dmaTransferDirValues)):
        key = dmaTransferDirValues[index].getAttribute("name")
        value = dmaTransferDirValues[index].getAttribute("value")
        description = dmaTransferDirValues[index].getAttribute("caption")
        dmaTransferDir.addKey(key, value, description)
    dmaTransferDir.setOutputMode("Value")
    dmaTransferDir.setDisplayMode("Description")
    dmaTransferDir.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])   
    
    if channelID == 0:
        # CRC engine configuration
        dmaCRCEnable = coreComponent.createBooleanSymbol("DMA_CRC_ENABLE_CH_" + str(channelID), dmaChannelEnable)
        dmaCRCEnable.setLabel("CRC Engine Enable")
        dmaCRCEnable.setDefaultValue(False)
        dmaCRCEnable.setDependencies(setVisibleOnDMAChEnable, ["DMA_ENABLE_CH_" + str(channelID)])
    if channelID == 1:
        # Fill engine configuration
        dmaFillEnable = coreComponent.createBooleanSymbol("DMA_FILL_ENABLE_CH_" + str(channelID), dmaChannelEnable)
        dmaFillEnable.setLabel("Fill Engine Enable")
        dmaFillEnable.setDefaultValue(False)
        dmaFillEnable.setDependencies(updateConfigOnFillEnable, ["DMA_FILL_ENABLE_CH_" + str(channelID)])
    

####################################################################################################

dmaEnable.setDependencies(onDMAChannelEnable, dmaChannelIds)
dmaHighestCh.setDependencies(onDMAChannelEnable, dmaChannelIds)

#dmaSymbolsForDMASysService(coreComponent, dmaChannelEnable)

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

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmaHeaderFile = coreComponent.createFileSymbol("DMA_HEADER", None)
dmaHeaderFile.setSourcePath("../peripheral/dma_85/templates/plib_dma.h.ftl")
dmaHeaderFile.setOutputName("plib_" + dmaInstanceName.getValue().lower() + ".h")
dmaHeaderFile.setDestPath("/peripheral/dma/")
dmaHeaderFile.setProjectPath("config/" + configName + "/peripheral/dma/")
dmaHeaderFile.setType("HEADER")
dmaHeaderFile.setMarkup(True)
dmaHeaderFile.setEnabled(False)
dmaHeaderFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])

# Source File
dmaSourceFile = coreComponent.createFileSymbol("DMA_SOURCE", None)
dmaSourceFile.setSourcePath("../peripheral/dma_85/templates/plib_dma.c.ftl")
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
dmaSystemInitFile.setSourcePath("../peripheral/dma_85/templates/system/initialization.c.ftl")
dmaSystemInitFile.setMarkup(True)
dmaSystemInitFile.setEnabled(False)
dmaSystemInitFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])

#System Definition
dmaSystemDefFile = coreComponent.createFileSymbol("DMA_SYS_DEF", None)
dmaSystemDefFile.setType("STRING")
dmaSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmaSystemDefFile.setSourcePath("../peripheral/dma_85/templates/system/definitions.h.ftl")
dmaSystemDefFile.setMarkup(True)
dmaSystemDefFile.setEnabled(False)
dmaSystemDefFile.setDependencies(fileGenerationDep, ["DMA_ENABLE"])
