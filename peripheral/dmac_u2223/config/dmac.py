from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Global Variables ####
################################################################################

# Parse atdf xml file to get instance name for the peripheral which has DMA id.
# And construct a list of PERIDs
global peridList
peridList = []
peridList.insert(0, "Only software/event triggers")

global peridValueList
peridValueList = []
peridValueList.insert(0, 0)

global peridValueListSymbols
peridValueListSymbols = []

global dmacActiveChannels
dmacActiveChannels = []

global dmacChannelIds
dmacChannelIds = []

atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
try:
    atdfFile = open(atdfFilePath, "r")
except:
    Log.writeInfoMessage("dmac.py peripheral DMAC: Error!!! while opening atdf file")
atdfContent = ElementTree.fromstring(atdfFile.read())
for peripheral in atdfContent.iter("module"):
    for instance in peripheral.iter("instance"):
        for param in instance.iter("param"):
            name = param.attrib['name']
            if "DMAC_ID" in name:
                name = name.strip('DMAC_ID_')
                name = name.replace('TX', 'Transmit')
                name = name.replace('RX', 'Receive')
                name = name.replace('LEFT', 'Left')
                name = name.replace('RIGHT', 'Right')
                name = name.replace('0', 'MC0')
                name = name.replace('1', 'MC1')
                name = name.replace('2', 'MC2')
                name = name.replace('3', 'MC3')
                peridList.append(instance.attrib['name'] + "_" + name)
                peridValueList.append(param.attrib['value'])

# This is the dictionary for all trigger sources and corresponding DMAC settings.
# "dmacTriggerLogic" business logic will override the DMAC setting values
# based on the trigger source selected.
global triggerSettings
triggerSettings = {"Only software/event triggers"    : ["TRANSACTION", "SRC", True, True,  "X1", "BYTE", "None"],
                "ADC0_RESRDY"       : ["BEAT", "SRC", False, True, "X1", "BYTE", "ADC0_REGS->ADC_RESULT"],
                "ADC1_RESRDY"       : ["BEAT", "DST", False, True, "X2", "BYTE", "ADC1_REGS->ADC_RESULT"],
                "CAN0_EBUG"         : ["BEAT", "DST", False, True, "X4", "BYTE", "CAN0_REGS->CAN_RXBC.RBSA"],
                "CAN1_EBUG"         : ["BEAT", "DST", False, True, "X4", "BYTE", "CAN1_REGS->CAN_RXBC.RBSA"],
                "DAC_EMPTY"         : ["BEAT", "DST", False, True, "X4", "BYTE", "DAC_REGS->DAC_DATABUF"],
                "PTC_EO"            : ["BEAT", "DST", False, True, "X4", "BYTE", "AC_REGS->SCALER.AC_VALUE"],
                "PTC_SEQ"           : ["BEAT", "DST", False, True, "X4", "BYTE", "AC_REGS->SCALER.AC_VALUE"],
                "PTC_WCOMP"         : ["BEAT", "DST", False, True, "X4", "BYTE", "AC_REGS->SCALER.AC_VALUE"],
                "SDADC_RESRDY"      : ["BEAT", "SRC", False, True, "X1", "BYTE", "SDADC_REGS->SDADC_RESULT"],
                "SERCOM0_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM0_REGS->I2CM.SERCOM_DATA"],
                "SERCOM0_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM0_REGS->I2CM.SERCOM_DATA"],
                "SERCOM1_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM1_REGS->SPI.SERCOM_DATA"],
                "SERCOM1_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM1_REGS->SPI.SERCOM_DATA"],
                "SERCOM2_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM2_REGS->I2CM.SERCOM_DATA"],
                "SERCOM2_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM2_REGS->I2CM.SERCOM_DATA"],
                "SERCOM3_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM3_REGS->I2CM.SERCOM_DATA"],
                "SERCOM3_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM3_REGS->I2CM.SERCOM_DATA"],
                "SERCOM4_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM4_REGS->USART.SERCOM_DATA"],
                "SERCOM4_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM4_REGS->USART.SERCOM_DATA"],
                "SERCOM5_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM5_REGS->I2C.SERCOM_DATA"],
                "SERCOM5_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM5_REGS->I2C.SERCOM_DATA"],
                "SERCOM6_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM6_REGS->I2CM.SERCOM_DATA"],
                "SERCOM6_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM6_REGS->I2CM.SERCOM_DATA"],
                "SERCOM7_Receive"   : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM7_REGS->I2CM.SERCOM_DATA"],
                "SERCOM7_Transmit"  : ["BEAT", "DST", False, True, "X4", "BYTE", "SERCOM7_REGS->I2CM.SERCOM_DATA"],
                "TC0_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC0_REGS->COUNT16.TC_INTFLAG"],
                "TC0_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC0_REGS->COUNT16.TC_INTFLAG"],
                "TC0_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC0_REGS->COUNT16.TC_INTFLAG"],
                "TC1_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC1_REGS->COUNT16.TC_INTFLAG"],
                "TC1_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC1_REGS->COUNT16.TC_INTFLAG"],
                "TC1_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC1_REGS->COUNT16.TC_INTFLAG"],
                "TC2_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC2_REGS->COUNT16.TC_INTFLAG"],
                "TC2_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC2_REGS->COUNT16.TC_INTFLAG"],
                "TC2_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC2_REGS->COUNT16.TC_INTFLAG"],
                "TC3_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC3_REGS->COUNT16.TC_INTFLAG"],
                "TC3_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC3_REGS->COUNT16.TC_INTFLAG"],
                "TC3_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC3_REGS->COUNT16.TC_INTFLAG"],
                "TC4_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC4_REGS->COUNT16.TC_INTFLAG"],
                "TC4_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC4_REGS->COUNT16.TC_INTFLAG"],
                "TC4_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC4_REGS->COUNT16.TC_INTFLAG"],
                "TC5_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC5_REGS->COUNT16.TC_INTFLAG"],
                "TC5_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC5_REGS->COUNT16.TC_INTFLAG"],
                "TC5_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC5_REGS->COUNT16.TC_INTFLAG"],
                "TC6_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC6_REGS->COUNT16.TC_INTFLAG"],
                "TC6_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC6_REGS->COUNT16.TC_INTFLAG"],
                "TC6_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC6_REGS->COUNT16.TC_INTFLAG"],
                "TC7_OVF"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC7_REGS->COUNT16.TC_INTFLAG"],
                "TC7_MC0"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC7_REGS->COUNT16.TC_INTFLAG"],
                "TC7_MC1"           : ["BEAT", "DST", False, True, "X4", "BYTE", "TC7_REGS->COUNT16.TC_INTFLAG"],
                "TCC0_OVF"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC0_REGS->COUNT16.TCC_INTFLAG"],
                "TCC0_MC0"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC0_REGS->COUNT16.TCC_INTFLAG"],
                "TCC0_MC1"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC0_REGS->COUNT16.TCC_INTFLAG"],
                "TCC0_MC2"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC0_REGS->COUNT16.TCC_INTFLAG"],
                "TCC0_MC3"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC0_REGS->COUNT16.TCC_INTFLAG"],
                "TCC1_OVF"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC1_REGS->COUNT16.TCC_INTFLAG"],
                "TCC1_MC0"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC1_REGS->COUNT16.TCC_INTFLAG"],
                "TCC1_MC1"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC1_REGS->COUNT16.TCC_INTFLAG"],
                "TCC2_OVF"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC2_REGS->COUNT16.TCC_INTFLAG"],
                "TCC2_MC0"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC2_REGS->COUNT16.TCC_INTFLAG"],
                "TCC2_MC1"          : ["BEAT", "DST", False, True, "X4", "BYTE", "TCC2_REGS->COUNT16.TCC_INTFLAG"],
                "TSENS_RESRDY"      : ["BEAT", "DST", False, True, "X2", "BYTE", "TSENS_REGS->TSENS_VALUE"]}



                # All triggers are yet to be added.

################################################################################
#### Business Logic ####
################################################################################

def setDMACChannelEnableProperty(symbol, event):

    channelId = int(symbol.getID().strip("DMAC_ENABLE_CH_"))

    channelCount = int(event["value"])

    if channelId < channelCount:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def setChCtrlARunStandyProperty(symbol, event):

    symbol.setVisible(event["value"])

def setChCtrlBTrigSrcProperty(symbol, event):

    symbol.setVisible(event["value"])

def setChCtrlBLvlProperty(symbol, event):

    symbol.setVisible(event["value"])

def setBtCtrlBlockActProperty(symbol, event):

    symbol.setVisible(event["value"])

def setCRCEnableProperty(symbol, event):

    symbol.setVisible(event["value"])

def dmacTriggerLogic(symbol, event):
    global triggerSettings

    if "DMAC_ENABLE_CH_" in event["id"]:
        symbol.setVisible(event["value"])
    else:
        SymID = symbol.getID()
        symbol.clearValue()
        if "TRIGACT" in SymID:
            symbol.setSelectedKey(str(triggerSettings[event["value"]][0]), 2)
            if (triggerSettings[event["value"]][0] == "TRANSACTION"):
                symbol.setReadOnly(True)
            else:
                symbol.setReadOnly(False)
        elif "STEPSEL" in SymID:
            symbol.setSelectedKey(str(triggerSettings[event["value"]][1]), 2)
        elif "SRCINC" in SymID:
            symbol.setValue(triggerSettings[event["value"]][2], 2)
        elif "DSTINC" in SymID:
            symbol.setValue(triggerSettings[event["value"]][3], 2)
        elif "STEPSIZE" in SymID:
            symbol.setSelectedKey(str(triggerSettings[event["value"]][4]), 2)
        elif "BEATSIZE" in SymID:
            symbol.setSelectedKey(str(triggerSettings[event["value"]][5]), 2)
        elif "PER_REGISTER" in SymID:
            symbol.setValue(str(triggerSettings[event["value"]][6]), 2)

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the highest
# index enabled, also if the list is empty then none of the channel is enabled.
# Highest index will be used to create DMAC objects in source code.
# List empty or non-empty status helps to generate/discard DMAC code.
def dmacGlobalLogic(dmacGlobalSym, event):
    global dmacActiveChannels

    index = event["id"].strip("DMAC_CH")
    index = index.strip("_ENABLE")
    try:
        index = int(index)
    except:
        return

    if event["value"] is True:
        if index not in dmacActiveChannels:
            dmacActiveChannels.append(index)
    else :
        if index in dmacActiveChannels:
            dmacActiveChannels.remove(index)

    dmacActiveChannels.sort()
    dmacActiveChannels.reverse()

    dmacGlobalSym.clearValue()
    # Check if the list is not empty first since list element is accessed in the code
    if dmacActiveChannels:
        if dmacGlobalSym.getID() == "DMAC_HIGHEST_CHANNEL":
            dmacGlobalSym.setValue(int(dmacActiveChannels[0]) + 1, 2)

    if dmacGlobalSym.getID() == "DMAC_ENABLE":
        if dmacActiveChannels and dmacGlobalSym.getValue() is False:
            dmacGlobalSym.setValue(True, 2)

        if not dmacActiveChannels:
            dmacGlobalSym.setValue(False, 2)

def dmacTriggerCalc(dmacPERIDVal, event):
    global peridList
    global peridValueList

    perid = event["value"]
    peridIndex = peridList.index(perid)
    dmacPERIDVal.clearValue()
    dmacPERIDVal.setValue(int(peridValueList[peridIndex]), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def dmacChannelAllocLogic(Sym, event):
    dmaChannelCount = Database.getSymbolValue("core", "DMAC_CHANNEL_COUNT")
    perID = event["id"].strip('DMA_CH_NEEDED_FOR_')
    channelAllocated = False

    for i in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "DMAC_CH"+str(i)+"_ENABLE")
        dmaChannelPerID = str(Database.getSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_"+str(i)))

        # Client requested to allocate channel
        if event["value"] == True:
            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.clearSymbolValue("core", "DMAC_CH"+str(i)+"_ENABLE")
                Database.setSymbolValue("core", "DMAC_CH"+str(i)+"_ENABLE", True, 2)

                Database.clearSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_"+str(i))
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_"+str(i), perID, 2)

                Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)

                channelAllocated = True
                i = 0
                break

        # Client requested to deallocate channel
        else:
            # Reset the previously allocated channel
            if perID == dmaChannelPerID and dmaChannelEnable == True:
                Database.clearSymbolValue("core", "DMAC_CH"+str(i)+"_ENABLE")
                Database.setSymbolValue("core", "DMAC_CH"+str(i)+"_ENABLE", False, 2)
                Database.clearSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_"+str(i))
                Database.setSymbolValue("core", "DMAC_CHCTRLB_TRIGSRC_CH_"+str(i), "Software Trigger", 2)
                Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -1, 2)

    if event["value"] == True and channelAllocated == False:
        # Couldn't find any free DMA channel, hence set warning.
        Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
        Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -2, 2)

################################################################################
#### Component ####
################################################################################

dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("SAMM0:SAMM0DMAModel")

dmacMenu = coreComponent.createMenuSymbol("DMAC_MENU", None)
dmacMenu.setLabel("DMA (DMAC)")
dmacMenu.setDescription("DMA (DMAC) Configuration")

dmacIndex = coreComponent.createIntegerSymbol("DMAC_INDEX", dmacMenu)
dmacIndex.setVisible(False)
dmacIndex.setDefaultValue(0)

#DMA Channel Enable Count
DMAC_CHAN_ENAB_CNT_SelectionSym = coreComponent.createIntegerSymbol("DMAC_CHAN_ENABLE_CNT", dmacMenu)
DMAC_CHAN_ENAB_CNT_SelectionSym.setLabel("Number of DMA channels to enable")
DMAC_CHAN_ENAB_CNT_SelectionSym.setDefaultValue(1)
DMAC_CHAN_ENAB_CNT_SelectionSym.setMin(1)
DMAC_CHAN_ENAB_CNT_SelectionSym.setMax(12)

#Enable DMA CRC feature
DMAC_CRC_ENAB_CNT_SelectionSym = coreComponent.createBooleanSymbol("DMAC_CRC_ENABLE", dmacMenu)
DMAC_CRC_ENAB_CNT_SelectionSym.setLabel("Enable DMA CRC feature")
DMAC_CRC_ENAB_CNT_SelectionSym.setVisible(False)

#CRC Source
DMAC_CRC_SRC_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CRC_SRC",dmacMenu)
DMAC_CRC_SRC_SelectionSym.setLabel("Select CRC Source")
DMAC_CRC_SRC_SelectionSym.setVisible(False)
DMAC_CRC_SRC_SelectionSym.setDependencies(setCRCEnableProperty, ["DMAC_CRC_ENABLE"])

dmacCrcSrcNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CRCCTRL__CRCSRC\"]")
dmacCrcSrcValues = []
dmacCrcSrcValues = dmacCrcSrcNode.getChildren()

dmacCrcSrcDefaultValue = 0

for index in range(len(dmacCrcSrcValues)):
    dmacCrcSrcKeyName = dmacCrcSrcValues[index].getAttribute("name")

    if (dmacCrcSrcKeyName == "NOACT"):
        dmacCrcSrcDefaultValue = index

    dmacCrcSrcKeyDescription = dmacCrcSrcValues[index].getAttribute("caption")
    dmacCrcSrcKeyValue = dmacCrcSrcValues[index].getAttribute("value")
    DMAC_CRC_SRC_SelectionSym.addKey(dmacCrcSrcKeyName, dmacCrcSrcKeyValue , dmacCrcSrcKeyDescription)

DMAC_CRC_SRC_SelectionSym.setDefaultValue(dmacCrcSrcDefaultValue)
DMAC_CRC_SRC_SelectionSym.setOutputMode("Key")
DMAC_CRC_SRC_SelectionSym.setDisplayMode("Description")

#CRC Polynomial Type
DMAC_CRC_POLY_TYPE_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CRC_POLY_TYPE",dmacMenu)
DMAC_CRC_POLY_TYPE_SelectionSym.setLabel("Select CRC Polynomial Type")
DMAC_CRC_POLY_TYPE_SelectionSym.setVisible(False)

dmacCrcPolyTypeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CRCCTRL__CRCPOLY\"]")
dmacCrcPolyTypeValues = []
dmacCrcPolyTypeValues = dmacCrcPolyTypeNode.getChildren()

dmacCrcPolyTypeDefaultValue = 0

for index in range(len(dmacCrcPolyTypeValues)):
    dmacCrcPolyTypeKeyName = dmacCrcPolyTypeValues[index].getAttribute("name")

    if (dmacCrcPolyTypeKeyName == "CRC16"):
        dmacCrcPolyTypeDefaultValue = index

    dmacCrcPolyTypeKeyDescription = dmacCrcPolyTypeValues[index].getAttribute("caption")
    dmacCrcPolyTypeKeyValue = dmacCrcPolyTypeValues[index].getAttribute("value")
    DMAC_CRC_POLY_TYPE_SelectionSym.addKey(dmacCrcPolyTypeKeyName, dmacCrcPolyTypeKeyValue , dmacCrcPolyTypeKeyDescription)

DMAC_CRC_POLY_TYPE_SelectionSym.setDefaultValue(dmacCrcPolyTypeDefaultValue)
DMAC_CRC_POLY_TYPE_SelectionSym.setOutputMode("Key")
DMAC_CRC_POLY_TYPE_SelectionSym.setDisplayMode("Description")
DMAC_CRC_POLY_TYPE_SelectionSym.setDependencies(setCRCEnableProperty, ["DMAC_CRC_ENABLE"])

#CRC Beat Size
DMAC_CRC_BEAT_SIZE_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CRC_BEAT_SIZE",dmacMenu)
DMAC_CRC_BEAT_SIZE_SelectionSym.setLabel("Select CRC Beat Size")
DMAC_CRC_BEAT_SIZE_SelectionSym.setVisible(False)
DMAC_CRC_BEAT_SIZE_SelectionSym.setDependencies(setCRCEnableProperty, ["DMAC_CRC_ENABLE"])

dmacCrcBeatSizeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CRCCTRL__CRCBEATSIZE\"]")
dmacCrcBeatSizeValues = []
dmacCrcBeatSizeValues = dmacCrcBeatSizeNode.getChildren()

dmacCrcBeatSizeDefaultValue = 0

for index in range(len(dmacCrcBeatSizeValues)):
    dmacCrcBeatSizeKeyName = dmacCrcBeatSizeValues[index].getAttribute("name")

    if (dmacCrcBeatSizeKeyName == "BYTE"):
        dmacCrcBeatSizeDefaultValue = index

    dmacCrcBeatSizeKeyDescription = dmacCrcBeatSizeValues[index].getAttribute("caption")
    dmacCrcBeatSizeKeyValue = dmacCrcBeatSizeValues[index].getAttribute("value")
    DMAC_CRC_BEAT_SIZE_SelectionSym.addKey(dmacCrcBeatSizeKeyName, dmacCrcBeatSizeKeyValue , dmacCrcBeatSizeKeyDescription)

DMAC_CRC_BEAT_SIZE_SelectionSym.setDefaultValue(dmacCrcBeatSizeDefaultValue)
DMAC_CRC_BEAT_SIZE_SelectionSym.setOutputMode("Key")
DMAC_CRC_BEAT_SIZE_SelectionSym.setDisplayMode("Description")

#Data Transfer Quality of Service
#DMAC_DATA_XFER_QOS_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_DATA_XFER_QOS",dmacMenu)
#DMAC_DATA_XFER_QOS_SelectionSym.setLabel("Data Transfer Quality of Service")
#DMAC_DATA_XFER_QOS_SelectionSym.setVisible(False)
#
#dmacDataXferQOSNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_QOSCTRL__DQOS\"]")
#dmacDataXferQOSValues = []
#dmacDataXferQOSValues = dmacDataXferQOSNode.getChildren()
#dmacDataXferQOSDefaultValue = 0
#
#for index in range(len(dmacDataXferQOSValues)):
#    dmacDataXferQOSKeyName = dmacDataXferQOSValues[index].getAttribute("name")
#
#    if (dmacDataXferQOSKeyName == "DISABLE"):
#        dmacDataXferQOSDefaultValue = index
#
#    dmacDataXferQOSKeyDescription = dmacDataXferQOSValues[index].getAttribute("caption")
#    dmacDataXferQOSKeyValue = dmacDataXferQOSValues[index].getAttribute("value")
#    DMAC_DATA_XFER_QOS_SelectionSym.addKey(dmacDataXferQOSKeyName, dmacDataXferQOSKeyValue , dmacDataXferQOSKeyDescription)
#
#DMAC_DATA_XFER_QOS_SelectionSym.setDefaultValue(dmacDataXferQOSDefaultValue)
#DMAC_DATA_XFER_QOS_SelectionSym.setOutputMode("Key")
#DMAC_DATA_XFER_QOS_SelectionSym.setDisplayMode("Description")
#
##Fetch Quality of Service
#DMAC_FETCH_QOS_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_FETCH_QOS",dmacMenu)
#DMAC_FETCH_QOS_SelectionSym.setLabel("Fetch Quality of Service")
#DMAC_FETCH_QOS_SelectionSym.setVisible(False)
#
#dmacFetchQOSNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_QOSCTRL__FQOS\"]")
#dmacFetchQOSValues = []
#dmacFetchQOSValues = dmacFetchQOSNode.getChildren()
#dmacFetchQOSDefaultValue = 0
#
#for index in range(len(dmacFetchQOSValues)):
#    dmacFetchQOSKeyName = dmacFetchQOSValues[index].getAttribute("name")
#
#    if (dmacFetchQOSKeyName == "DISABLE"):
#        dmacFetchQOSDefaultValue = index
#
#    dmacFetchQOSKeyDescription = dmacFetchQOSValues[index].getAttribute("caption")
#    dmacFetchQOSKeyValue = dmacFetchQOSValues[index].getAttribute("value")
#    DMAC_FETCH_QOS_SelectionSym.addKey(dmacFetchQOSKeyName, dmacFetchQOSKeyValue , dmacFetchQOSKeyDescription)
#
#DMAC_FETCH_QOS_SelectionSym.setDefaultValue(dmacFetchQOSDefaultValue)
#DMAC_FETCH_QOS_SelectionSym.setOutputMode("Key")
#DMAC_FETCH_QOS_SelectionSym.setDisplayMode("Description")
#
##Write-back Quality of Service
#DMAC_WR_BACK_QOS_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_WRITE_BACK_QOS",dmacMenu)
#DMAC_WR_BACK_QOS_SelectionSym.setLabel("Write-back Quality of Service")
#DMAC_WR_BACK_QOS_SelectionSym.setVisible(False)
#
#dmacWrBackQOSNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_QOSCTRL__WRBQOS\"]")
#dmacWrBackQOSValues = []
#dmacWrBackQOSValues = dmacWrBackQOSNode.getChildren()
#dmacWrBackQOSDefaultValue = 0
#
#for index in range(len(dmacWrBackQOSValues)):
#    dmacWrBackQOSKeyName = dmacWrBackQOSValues[index].getAttribute("name")
#
#    if (dmacWrBackQOSKeyName == "DISABLE"):
#        dmacWrBackQOSDefaultValue = index
#
#    dmacWrBackQOSKeyDescription = dmacWrBackQOSValues[index].getAttribute("caption")
#    dmacWrBackQOSKeyValue = dmacWrBackQOSValues[index].getAttribute("value")
#    DMAC_WR_BACK_QOS_SelectionSym.addKey(dmacWrBackQOSKeyName, dmacWrBackQOSKeyValue , dmacWrBackQOSKeyDescription)
#
#DMAC_WR_BACK_QOS_SelectionSym.setDefaultValue(dmacWrBackQOSDefaultValue)
#DMAC_WR_BACK_QOS_SelectionSym.setOutputMode("Key")
#DMAC_WR_BACK_QOS_SelectionSym.setDisplayMode("Description")

dmacEnable = coreComponent.createBooleanSymbol("DMAC_ENABLE", dmacMenu)
dmacEnable.setLabel("Use DMA Service?")
dmacEnable.setVisible(False)

dmacHighestCh = coreComponent.createIntegerSymbol("DMAC_HIGHEST_CHANNEL", dmacEnable)
dmacHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmacHighestCh.setVisible(False)

dmacChCount = coreComponent.createIntegerSymbol("DMAC_CHANNEL_COUNT", dmacEnable)
dmacChCount.setLabel("DMA (DMAC) Channels Count")
dmacChCount.setDefaultValue(12)
dmacChCount.setVisible(False)

#Priority Control 0 Register
for dmacCount in range(0, 4):

    #Level 0/1/2/3 Round-Robin Arbitration Enable
    PRICTRL0_LVLPRI_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_LVLXPRIO_" + str(dmacCount),dmacMenu)
    PRICTRL0_LVLPRI_SelectionSym.setLabel("Scheduling Method for Priority Level " + str(dmacCount) + " Channels")

    dmacLvlPri0Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_PRICTRL0__RRLVLEN0\"]")
    dmacLvlPri0Values = []
    dmacLvlPri0Values = dmacLvlPri0Node.getChildren()

    dmacLvlPri0DefaultValue = 0

    for index in range(len(dmacLvlPri0Values)):
        dmacLvlPri0KeyName = dmacLvlPri0Values[index].getAttribute("name")

        if (dmacLvlPri0KeyName == "STATIC_LVL"):
            dmacLvlPri0DefaultValue = index

        dmacLvlPri0KeyDescription = dmacLvlPri0Values[index].getAttribute("caption")
        dmacLvlPri0KeyValue = dmacLvlPri0Values[index].getAttribute("value")
        PRICTRL0_LVLPRI_SelectionSym.addKey(dmacLvlPri0KeyName, dmacLvlPri0KeyValue , dmacLvlPri0KeyDescription)

    PRICTRL0_LVLPRI_SelectionSym.setDefaultValue(dmacLvlPri0DefaultValue)
    PRICTRL0_LVLPRI_SelectionSym.setOutputMode("Value")
    PRICTRL0_LVLPRI_SelectionSym.setDisplayMode("Description")

#Descriptor Linking
dmacDescLinkingCtrl = coreComponent.createBooleanSymbol("DMAC_DESC_LINKING", dmacMenu)
dmacDescLinkingCtrl.setLabel("Enable Descriptor Linking")

for channelID in range(0, dmacChCount.getValue()):

    dmacChannelEnable = coreComponent.createBooleanSymbol("DMAC_ENABLE_CH_" + str(channelID), dmacMenu)
    dmacChannelEnable.setLabel("Use DMAC Channel "+ str(channelID))

    if channelID != 0:
        dmacChannelEnable.setVisible(False)

    dmacChannelIds.append("DMAC_ENABLE_CH_" + str(channelID))
    dmacChannelEnable.setDependencies(setDMACChannelEnableProperty, ["DMAC_CHAN_ENABLE_CNT"])

    #Channel Run in Standby
    CH_CHCTRLA_RUNSTDBY_Ctrl = coreComponent.createBooleanSymbol("DMAC_CHCTRLA_RUNSTDBY_CH_" + str(channelID), dmacChannelEnable)
    CH_CHCTRLA_RUNSTDBY_Ctrl.setLabel("Run Channel in Standby mode")
    CH_CHCTRLA_RUNSTDBY_Ctrl.setVisible(False)
    CH_CHCTRLA_RUNSTDBY_Ctrl.setDependencies(setChCtrlARunStandyProperty, ["DMAC_ENABLE_CH_" + str(channelID)])

    # CHCTRLB - Trigger Source
    dmacSym_CHCTRLB_TRIGSRC = coreComponent.createComboSymbol("DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID), dmacChannelEnable, peridList)
    dmacSym_CHCTRLB_TRIGSRC.setLabel("Trigger Source")
    dmacSym_CHCTRLB_TRIGSRC.setDefaultValue("Only software/event triggers")
    dmacSym_CHCTRLB_TRIGSRC.setVisible(False)
    dmacSym_CHCTRLB_TRIGSRC.setDependencies(setChCtrlBTrigSrcProperty, ["DMAC_ENABLE_CH_" + str(channelID)])

    dmacSym_PERID_Val = coreComponent.createIntegerSymbol("DMAC_CHCTRLB_TRIGSRC_CH_"+ str(channelID)+"_PERID_VAL", dmacChannelEnable)
    dmacSym_PERID_Val.setLabel("PERID Value")
    dmacSym_PERID_Val.setDefaultValue(0)
    dmacSym_PERID_Val.setDependencies(dmacTriggerCalc, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID)])
    dmacSym_PERID_Val.setVisible(False)

    dmacPeripheralRegister = coreComponent.createStringSymbol("DMAC_CH"+ str(channelID)+"_PER_REGISTER", dmacChannelEnable)
    dmacPeripheralRegister.setLabel("Source Address")
    dmacPeripheralRegister.setDefaultValue("None")
    dmacPeripheralRegister.setReadOnly(True)
    dmacPeripheralRegister.setVisible(False)
    dmacPeripheralRegister.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    # CHCTRLB - Trigger Action
    dmacSym_CHCTRLB_TRIGACT = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLB_TRIGACT_CH_" + str(channelID),dmacChannelEnable)
    dmacSym_CHCTRLB_TRIGACT.setLabel("Trigger Action")
    dmacSym_CHCTRLB_TRIGACT.setVisible(False)
    dmacSym_CHCTRLB_TRIGACT.setReadOnly(True)

    dmacTrigActNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHCTRLB__TRIGACT\"]")
    dmacTrigActValues = []
    dmacTrigActValues = dmacTrigActNode.getChildren()

    dmacTrigActDefaultValue = 0

    for index in range(len(dmacTrigActValues)):
       dmacTrigActKeyName = dmacTrigActValues[index].getAttribute("name")

       if (dmacTrigActKeyName == "TRANSACTION"):
          dmacTrigActDefaultValue = index

       dmacTrigActKeyDescription = dmacTrigActValues[index].getAttribute("caption")
       dmacTrigActKeyValue = dmacTrigActValues[index].getAttribute("value")
       dmacSym_CHCTRLB_TRIGACT.addKey(dmacTrigActKeyName, dmacTrigActKeyValue , dmacTrigActKeyDescription)

    dmacSym_CHCTRLB_TRIGACT.setDefaultValue(dmacTrigActDefaultValue)
    dmacSym_CHCTRLB_TRIGACT.setOutputMode("Value")
    dmacSym_CHCTRLB_TRIGACT.setDisplayMode("Key")
    dmacSym_CHCTRLB_TRIGACT.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    #Channel Priority Level
    CHCTRLB_LVL_SelectionSym = coreComponent.createKeyValueSetSymbol("DMAC_CHCTRLB_LVL_CH_" + str(channelID),dmacChannelEnable)
    CHCTRLB_LVL_SelectionSym.setLabel("Channel Priority Level")
    CHCTRLB_LVL_SelectionSym.setVisible(False)

    dmacLvlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_CHCTRLB__LVL\"]")
    dmacLvlValues = []
    dmacLvlValues = dmacLvlNode.getChildren()

    dmacLvlDefaultValue = 0

    for index in range(len(dmacLvlValues)):
        dmacLvlKeyName = dmacLvlValues[index].getAttribute("name")

        if (dmacLvlKeyName == "LVL0"):
            dmacLvlDefaultValue = index

        dmacLvlKeyDescription = dmacLvlValues[index].getAttribute("caption")
        dmacLvlKeyValue = dmacLvlValues[index].getAttribute("value")
        CHCTRLB_LVL_SelectionSym.addKey(dmacLvlKeyName, dmacLvlKeyValue , dmacLvlKeyDescription)

    CHCTRLB_LVL_SelectionSym.setDefaultValue(dmacLvlDefaultValue)
    CHCTRLB_LVL_SelectionSym.setOutputMode("Value")
    CHCTRLB_LVL_SelectionSym.setDisplayMode("Description")
    CHCTRLB_LVL_SelectionSym.setDependencies(setChCtrlBLvlProperty, ["DMAC_ENABLE_CH_" + str(channelID)])

    # CHCTRLB - Step Selection
    dmacSym_BTCTRL_STEPSEL = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_STEPSEL_CH_" + str(channelID),dmacChannelEnable)
    dmacSym_BTCTRL_STEPSEL.setLabel("Step Selection")
    dmacSym_BTCTRL_STEPSEL.setVisible(False)

    dmacStepSelNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_BTCTRL__STEPSEL\"]")
    dmacStepSelValues = []
    dmacStepSelValues = dmacStepSelNode.getChildren()

    dmacStepSelDefaultValue = 0

    for index in range(len(dmacStepSelValues)):
        dmacStepSelKeyName = dmacStepSelValues[index].getAttribute("name")

        if (dmacStepSelKeyName == "DST"):
            dmacStepSelDefaultValue = index

        dmacStepSelKeyDescription = dmacStepSelValues[index].getAttribute("caption")
        dmacStepSelKeyValue = dmacStepSelValues[index].getAttribute("value")
        dmacSym_BTCTRL_STEPSEL.addKey(dmacStepSelKeyName, dmacStepSelKeyValue , dmacStepSelKeyDescription)

    dmacSym_BTCTRL_STEPSEL.setDefaultValue(dmacStepSelDefaultValue)
    dmacSym_BTCTRL_STEPSEL.setOutputMode("Key")
    dmacSym_BTCTRL_STEPSEL.setDisplayMode("Description")
    dmacSym_BTCTRL_STEPSEL.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    # BTCTRL - Address Increment Step Size
    dmacSym_BTCTRL_STEPSIZE = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_STEPSIZE_CH_" + str(channelID),dmacChannelEnable)
    dmacSym_BTCTRL_STEPSIZE.setLabel("Step Size")
    dmacSym_BTCTRL_STEPSIZE.setVisible(False)

    dmacStepSizeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_BTCTRL__STEPSIZE\"]")
    dmacStepSizeValues = []
    dmacStepSizeValues = dmacStepSizeNode.getChildren()

    dmacStepSizeDefaultValue = 0

    for index in range(len(dmacStepSizeValues)):
        dmacStepSizeKeyName = dmacStepSizeValues[index].getAttribute("name")

        if (dmacStepSizeKeyName == "X1"):
            dmacStepSizeDefaultValue = index

        dmacStepSizeKeyDescription = dmacStepSizeValues[index].getAttribute("caption")
        dmacStepSizeKeyValue = dmacStepSizeValues[index].getAttribute("value")
        dmacSym_BTCTRL_STEPSIZE.addKey(dmacStepSizeKeyName, dmacStepSizeKeyValue , dmacStepSizeKeyDescription)

    dmacSym_BTCTRL_STEPSIZE.setDefaultValue(dmacStepSizeDefaultValue)
    dmacSym_BTCTRL_STEPSIZE.setOutputMode("Key")
    dmacSym_BTCTRL_STEPSIZE.setDisplayMode("Description")
    dmacSym_BTCTRL_STEPSIZE.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_" + str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    # BTCTRL - Destination Increment
    dmacSym_BTCTRL_DSTINC_Val = coreComponent.createBooleanSymbol("DMAC_BTCTRL_DSTINC_CH_" + str(channelID), dmacChannelEnable)
    dmacSym_BTCTRL_DSTINC_Val.setLabel("Destination Address Increment Enable")
    dmacSym_BTCTRL_DSTINC_Val.setDefaultValue(True)
    dmacSym_BTCTRL_DSTINC_Val.setVisible(False)
    dmacSym_BTCTRL_DSTINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_"+ str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    # BTCTRL - Source Increment
    dmacSym_BTCTRL_SRCINC_Val = coreComponent.createBooleanSymbol("DMAC_BTCTRL_SRCINC_CH_"+ str(channelID),dmacChannelEnable)
    dmacSym_BTCTRL_SRCINC_Val.setLabel("Source Address Increment Enable")
    dmacSym_BTCTRL_SRCINC_Val.setDefaultValue(True)
    dmacSym_BTCTRL_SRCINC_Val.setVisible(False)
    dmacSym_BTCTRL_SRCINC_Val.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_"+ str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

    # BTCTRL - Beat Size
    dmacSym_BTCTRL_BEATSIZE = coreComponent.createKeyValueSetSymbol("DMAC_BTCTRL_BEATSIZE_CH_"+ str(channelID),dmacChannelEnable)
    dmacSym_BTCTRL_BEATSIZE.setLabel("Beat Size")
    dmacSym_BTCTRL_BEATSIZE.setVisible(False)

    dmacBeatSizeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMAC\"]/value-group@[name=\"DMAC_BTCTRL__BEATSIZE\"]")
    dmacBeatSizeValues = []
    dmacBeatSizeValues = dmacBeatSizeNode.getChildren()

    dmacBeatSizeDefaultValue = 0

    for index in range(len(dmacBeatSizeValues)):
        dmacBeatSizeKeyName = dmacBeatSizeValues[index].getAttribute("name")

        if (dmacBeatSizeKeyName == "BYTE"):
            dmacBeatSizeDefaultValue = index

        dmacBeatSizeKeyDescription = dmacBeatSizeValues[index].getAttribute("caption")
        dmacBeatSizeKeyValue = dmacBeatSizeValues[index].getAttribute("value")
        dmacSym_BTCTRL_BEATSIZE.addKey(dmacBeatSizeKeyName, dmacBeatSizeKeyValue , dmacBeatSizeKeyDescription)

    dmacSym_BTCTRL_BEATSIZE.setDefaultValue(dmacBeatSizeDefaultValue)
    dmacSym_BTCTRL_BEATSIZE.setOutputMode("Key")
    dmacSym_BTCTRL_BEATSIZE.setDisplayMode("Description")
    dmacSym_BTCTRL_BEATSIZE.setDependencies(dmacTriggerLogic, ["DMAC_CHCTRLB_TRIGSRC_CH_"+ str(channelID),"DMAC_ENABLE_CH_" + str(channelID)])

dmacEnable.setDependencies(dmacGlobalLogic, dmacChannelIds)
dmacHighestCh.setDependencies(dmacGlobalLogic, dmacChannelIds)

# Interface for Peripheral clients
for per in peridList:
    dmacChannelNeeded = coreComponent.createBooleanSymbol("DMA_CH_NEEDED_FOR_" + str(per), dmacChannelEnable)
    dmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    dmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    dmacChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(per), dmacChannelEnable)
    dmacChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    dmacChannel.setDefaultValue(-1)
    dmacChannel.setVisible(False)

dmacPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", dmacChannelEnable)
dmacPERIDChannelUpdate.setLabel("Local dmacChannelAllocLogic")
dmacPERIDChannelUpdate.setVisible(False)
dmacPERIDChannelUpdate.setDependencies(dmacChannelAllocLogic, peridValueListSymbols)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmacHeaderFile = coreComponent.createFileSymbol("DMAC_HEADER", None)
dmacHeaderFile.setSourcePath("../peripheral/dmac_u2223/templates/plib_dmac.h.ftl")
dmacHeaderFile.setOutputName("plib_dmac0.h")
dmacHeaderFile.setDestPath("/peripheral/dmac/")
dmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacHeaderFile.setType("HEADER")
dmacHeaderFile.setMarkup(True)

# Source File
dmacSourceFile = coreComponent.createFileSymbol("DMAC_SOURCE", None)
dmacSourceFile.setSourcePath("../peripheral/dmac_u2223/templates/plib_dmac.c.ftl")
dmacSourceFile.setOutputName("plib_dmac0.c")
dmacSourceFile.setDestPath("/peripheral/dmac/")
dmacSourceFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacSourceFile.setType("SOURCE")
dmacSourceFile.setMarkup(True)

#System Initialization
dmacSystemInitFile = coreComponent.createFileSymbol("DMAC_SYS_INIT", None)
dmacSystemInitFile.setType("STRING")
dmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmacSystemInitFile.setSourcePath("../peripheral/dmac_u2223/templates/system/initialization.c.ftl")
dmacSystemInitFile.setMarkup(True)

#System Definition
dmacSystemDefFile = coreComponent.createFileSymbol("DMAC_SYS_DEF", None)
dmacSystemDefFile.setType("STRING")
dmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmacSystemDefFile.setSourcePath("../peripheral/dmac_u2223/templates/system/definitions.h.ftl")
dmacSystemDefFile.setMarkup(True)
