from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

################################################################################
#### Register Information ####
################################################################################
xdmacRegModule = Register.getRegisterModule("XDMAC")
xdmacRegGroup = xdmacRegModule.getRegisterGroup("XDMAC_CHID")

xdmacReg_CC = xdmacRegGroup.getRegister("XDMAC_CC")
xdmacBitField_CC_TYPE = xdmacReg_CC.getBitfield("TYPE")
xdmacValGrp_CC_TYPE = xdmacRegModule.getValueGroup(xdmacBitField_CC_TYPE.getValueGroupName())
xdmacBitField_CC_DSYNC = xdmacReg_CC.getBitfield("DSYNC")
xdmacValGrp_CC_DSYNC = xdmacRegModule.getValueGroup(xdmacBitField_CC_DSYNC.getValueGroupName())
xdmacBitField_CC_SWREQ = xdmacReg_CC.getBitfield("SWREQ")
xdmacValGrp_CC_SWREQ = xdmacRegModule.getValueGroup(xdmacBitField_CC_SWREQ.getValueGroupName())
xdmacBitField_CC_PERID = xdmacReg_CC.getBitfield("PERID")
xdmacValGrp_CC_PERID = xdmacRegModule.getValueGroup(xdmacBitField_CC_PERID.getValueGroupName())
xdmacBitField_CC_DAM = xdmacReg_CC.getBitfield("DAM")
xdmacValGrp_CC_DAM = xdmacRegModule.getValueGroup(xdmacBitField_CC_DAM.getValueGroupName())
xdmacBitField_CC_SAM = xdmacReg_CC.getBitfield("SAM")
xdmacValGrp_CC_SAM = xdmacRegModule.getValueGroup(xdmacBitField_CC_SAM.getValueGroupName())
xdmacBitField_CC_DIF = xdmacReg_CC.getBitfield("DIF")
xdmacValGrp_CC_DIF = xdmacRegModule.getValueGroup(xdmacBitField_CC_DIF.getValueGroupName())
xdmacBitField_CC_SIF = xdmacReg_CC.getBitfield("SIF")
xdmacValGrp_CC_SIF = xdmacRegModule.getValueGroup(xdmacBitField_CC_SIF.getValueGroupName())
xdmacBitField_CC_DWIDTH = xdmacReg_CC.getBitfield("DWIDTH")
xdmacValGrp_CC_DWIDTH = xdmacRegModule.getValueGroup(xdmacBitField_CC_DWIDTH.getValueGroupName())
xdmacBitField_CC_CSIZE = xdmacReg_CC.getBitfield("CSIZE")
xdmacValGrp_CC_CSIZE = xdmacRegModule.getValueGroup(xdmacBitField_CC_CSIZE.getValueGroupName())
xdmacBitField_CC_MBSIZE = xdmacReg_CC.getBitfield("MBSIZE")
xdmacValGrp_CC_MBSIZE = xdmacRegModule.getValueGroup(xdmacBitField_CC_MBSIZE.getValueGroupName())

################################################################################
#### Global Variables ####
################################################################################
global xdmacHeaderFile
global xdmacSourceFile
global xdmacSystemInitFile
global xdmacSystemIntFile
global xdmacSystemDefFile
global xdmacSystemConfigFile

# Parse atdf xml file to get instance name for the peripheral which has DMA id.
# And construct a list of PERIDs
global peridList
peridList = []
peridList.insert(0, "Software Trigger")

global peridValueList
peridValueList = []
peridValueList.insert(0, 200)

global peridValueListSymbols
peridValueListSymbols = []

global xdmacActiveChannels
xdmacActiveChannels = []

global xdmacChannelIds
xdmacChannelIds = []

atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
try:
    atdfFile = open(atdfFilePath, "r")
except:
    Log.writeInfoMessage("xdmac.py peripheral XDMAC: Error!!! while opening atdf file")
atdfContent = ElementTree.fromstring(atdfFile.read())
for peripheral in atdfContent.iter("module"):
    for instance in peripheral.iter("instance"):
        for param in instance.iter("param"):
            name = param.attrib['name']
            if "DMAC_ID" in name:
                name = name.strip('DMAC_ID_')
                module = str(instance.attrib['name'])
                if "HSMCI" == module:
                    if "HSMCI" not in peridList:
                        peridList.append("HSMCI")
                else:
                    name = name.replace('TX', 'Transmit')
                    name = name.replace('RX', 'Receive')
                    name = name.replace('LEFT', 'Left')
                    name = name.replace('RIGHT', 'Right')
                    peridList.append(module + "_" + name)
                peridValueList.append(param.attrib['value'])

# This is the dictionary for all trigger sources and corresponding XDMAC settings.
# "xdmacTriggerLogic" business logic will override the XDMAC setting values
# based on the trigger source selected.
global triggerSettings
triggerSettings = {"Software Trigger"    : ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "None"],
                "USART0_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART0_REGS->US_THR"],
                "USART0_Receive"        : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART0_REGS->US_RHR"],
                "USART1_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART1_REGS->US_THR"],
                "USART1_Receive"        : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART1_REGS->US_RHR"],
                "USART2_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART2_REGS->US_THR"],
                "USART2_Receive"        : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "USART2_REGS->US_RHR"],
                "UART0_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART0_REGS->UART_THR"],
                "UART0_Receive"            : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART0_REGS->UART_RHR"],
                "UART1_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART1_REGS->UART_THR"],
                "UART1_Receive"            : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART1_REGS->UART_RHR"],
                "UART2_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART2_REGS->UART_THR"],
                "UART2_Receive"            : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART2_REGS->UART_RHR"],
                "UART3_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART3_REGS->UART_THR"],
                "UART3_Receive"            : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART3_REGS->UART_RHR"],
                "UART4_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART4_REGS->UART_THR"],
                "UART4_Receive"            : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "UART4_REGS->UART_RHR"],
                "SPI0_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "SPI0_REGS->SPI_TDR"],
                "SPI0_Receive"        : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "SPI0_REGS->SPI_RDR"],
                "SPI1_Transmit"        : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "SPI1_REGS->SPI_TDR"],
                "SPI1_Receive"        : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE", "SPI1_REGS->SPI_RDR"]}
                
                # All triggers are yet to be added.

################################################################################
#### Business Logic ####
################################################################################
def dependencyStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def xdmacTriggerLogic(xdmacSym, event):
    global triggerSettings
    SymID = xdmacSym.getID()
    xdmacSym.clearValue()
    if "TYPE" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][0]), 2)
    if "DSYNC" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][1]), 2)
    if "SWREQ" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][2]), 2)
    if "SAM" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][3]), 2)
    if "DAM" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][4]), 2)
    if "SIF" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][5]), 2)
    if "DIF" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][6]), 2)
    if "DWIDTH" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][7]), 2)
    if "CSIZE" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][8]), 2)
    if "MBSIZE" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][9]), 2)
    if "PER_REGISTER" in str(SymID):
        xdmacSym.setValue(str(triggerSettings[event["value"]][10]), 2)

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the highest
# index enabled, also if the list is empty then none of the channel is enabled.
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
    else :
        if index in xdmacActiveChannels:
            xdmacActiveChannels.remove(index)

    xdmacActiveChannels.sort()
    xdmacActiveChannels.reverse()

    xdmacGlobalSym.clearValue()
    # Check if the list is not empty first since list element is accessed in the code
    if xdmacActiveChannels:
        if xdmacGlobalSym.getID() == "XDMAC_HIGHEST_CHANNEL":
            xdmacGlobalSym.setValue(int(xdmacActiveChannels[0]) + 1, 2)

    if xdmacGlobalSym.getID() == "XDMAC_ENABLE":
        if xdmacActiveChannels and xdmacGlobalSym.getValue() is False:
            xdmacGlobalSym.setValue(True, 2)

        if not xdmacActiveChannels:
            xdmacGlobalSym.setValue(False, 2)

def onGlobalEnableLogic(xdmacFileGen, event):
    peripId = Interrupt.getInterruptIndex("XDMAC")
    NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", "PMC_ID_XDMAC")
    Database.setSymbolValue("core", "PMC_ID_XDMAC", event["value"], 2)
    Database.clearSymbolValue("core", NVICVector)
    Database.setSymbolValue("core", NVICVector, event["value"], 2)
    Database.clearSymbolValue("core", NVICHandlerLock)
    Database.setSymbolValue("core", NVICHandlerLock, event["value"], 2)
    Database.clearSymbolValue("core", NVICHandler)
    if (event["value"] == True) :
        Database.setSymbolValue("core", NVICHandler, "XDMAC_InterruptHandler", 2)
    else :
        Database.setSymbolValue("core", NVICHandler, "XDMAC_Handler", 2)

    # File generation logic
    xdmacHeaderFile.setEnabled(event["value"])
    xdmacSourceFile.setEnabled(event["value"])
    xdmacSystemInitFile.setEnabled(event["value"])
    xdmacSystemDefFile.setEnabled(event["value"])
    xdmacSystemConfigFile.setEnabled(event["value"])

def xdmacTriggerCalc(xdmacPERIDVal, event):
    global peridList
    global peridValueList

    perid = event["value"]
    peridIndex = peridList.index(perid)
    xdmacPERIDVal.clearValue()
    xdmacPERIDVal.setValue(int(peridValueList[peridIndex]), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def xdmacChannelAllocLogic(Sym, event):
    dmaChannelCount = Database.getSymbolValue("core", "XDMAC_CHANNEL_COUNT")
    perID = event["id"].strip('DMA_CH_NEEDED_FOR_')
    channelAllocated = False

    for i in range(0, dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "XDMAC_CH"+str(i)+"_ENABLE")
        dmaChannelPerID = str(Database.getSymbolValue("core", "XDMAC_CC"+str(i)+"_PERID"))

        # Client requested to allocate channel
        if event["value"] == True:
            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.clearSymbolValue("core", "XDMAC_CH"+str(i)+"_ENABLE")
                Database.setSymbolValue("core", "XDMAC_CH"+str(i)+"_ENABLE", True, 2)

                Database.clearSymbolValue("core", "XDMAC_CC"+str(i)+"_PERID")
                Database.setSymbolValue("core", "XDMAC_CC"+str(i)+"_PERID", perID, 2)

                Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, i, 2)

                channelAllocated = True
                i = 0
                break

        # Client requested to deallocate channel
        else:
            # Reset the previously allocated channel
            if perID == dmaChannelPerID and dmaChannelEnable == True:
                Database.clearSymbolValue("core", "XDMAC_CH"+str(i)+"_ENABLE")
                Database.setSymbolValue("core", "XDMAC_CH"+str(i)+"_ENABLE", False, 2)
                Database.clearSymbolValue("core", "XDMAC_CC"+str(i)+"_PERID")
                Database.setSymbolValue("core", "XDMAC_CC"+str(i)+"_PERID", "Software Trigger", 2)
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
dmaManagerSelect.setDefaultValue("SAME70:SAME70DMAModel")

xdmacMenu = coreComponent.createMenuSymbol("XDMAC_MENU", None)
xdmacMenu.setLabel("DMA (XDMAC)")
xdmacMenu.setDescription("DMA (XDMAC) Configuration")

xdmacEnable = coreComponent.createBooleanSymbol("XDMAC_ENABLE", xdmacMenu)
xdmacEnable.setLabel("Use DMA Service?")
xdmacEnable.setVisible(False)
xdmacEnable.setDefaultValue(False)

xdmacFileGen = coreComponent.createBooleanSymbol("XDMAC_FILE_GEN", xdmacEnable)
xdmacFileGen.setLabel("DMA (XDMAC) File Generation")
xdmacFileGen.setDependencies(onGlobalEnableLogic, ["XDMAC_ENABLE"])
xdmacFileGen.setVisible(False)

xdmacHighestCh = coreComponent.createIntegerSymbol("XDMAC_HIGHEST_CHANNEL", xdmacEnable)
xdmacHighestCh.setLabel("DMA (XDMAC) Highest Active Channel")
xdmacHighestCh.setVisible(False)

xdmacChCount = coreComponent.createIntegerSymbol("XDMAC_CHANNEL_COUNT", xdmacEnable)
xdmacChCount.setLabel("DMA (XDMAC) Channels Count")
xdmacChCount.setDefaultValue(24)
xdmacChCount.setVisible(False)

xdmacChannelLinkedList = coreComponent.createBooleanSymbol("XDMAC_LL_ENABLE", xdmacMenu)
xdmacChannelLinkedList.setLabel("Use Linked List Mode?")
xdmacChannelLinkedList.setDefaultValue(False)

for channelID in range(0, xdmacChCount.getValue()):

    xdmacChannelEnable = coreComponent.createBooleanSymbol("XDMAC_CH"+str(channelID)+"_ENABLE", xdmacMenu)
    xdmacChannelEnable.setLabel("Use XDMAC Channel "+ str(channelID))
    xdmacChannelEnable.setDefaultValue(False)
    xdmacChannelIds.append("XDMAC_CH"+str(channelID)+"_ENABLE")

    xdmacChannelMenu = coreComponent.createMenuSymbol("XDMAC_CH"+str(channelID)+"CONFIG", xdmacChannelEnable)
    xdmacChannelMenu.setLabel("XDMAC Channel " + str(channelID) + " Settings")
    xdmacChannelMenu.setDescription("Configuration for DMA Channel"+ str(channelID))

    xdmacSym_CC_PERID = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_PERID", xdmacChannelMenu, peridList)
    xdmacSym_CC_PERID.setLabel(xdmacBitField_CC_PERID.getDescription())
    xdmacSym_CC_PERID.setDefaultValue("Software Trigger")

    xdmacPeripheralRegister = coreComponent.createStringSymbol("XDMAC_CH"+ str(channelID)+"_PER_REGISTER", xdmacChannelMenu)
    xdmacPeripheralRegister.setLabel("Peripheral Register associated with the DMA Channel")
    xdmacPeripheralRegister.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacPeripheralRegister.setDefaultValue("None")
    xdmacPeripheralRegister.setReadOnly(True)

    xdmacSym_CC_PERID_Val = coreComponent.createIntegerSymbol("XDMAC_CC"+ str(channelID)+"_PERID_VAL", xdmacChannelMenu)
    xdmacSym_CC_PERID_Val.setLabel("PERID Value")
    xdmacSym_CC_PERID_Val.setDefaultValue(200)
    xdmacSym_CC_PERID_Val.setDependencies(xdmacTriggerCalc, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_PERID_Val.setVisible(True)

    xdmacSym_CC_TYPE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_TYPE", xdmacChannelMenu, xdmacValGrp_CC_TYPE.getValueNames())
    xdmacSym_CC_TYPE.setLabel(xdmacBitField_CC_TYPE.getDescription())
    xdmacSym_CC_TYPE.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_TYPE.setDefaultValue("MEM_TRAN")

    xdmacSym_CC_DSYNC = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DSYNC", xdmacChannelMenu, xdmacValGrp_CC_DSYNC.getValueNames())
    xdmacSym_CC_DSYNC.setLabel(xdmacBitField_CC_DSYNC.getDescription())
    xdmacSym_CC_DSYNC.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_DSYNC.setDefaultValue("PER2MEM")

    xdmacSym_CC_SWREQ = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SWREQ", xdmacChannelMenu, xdmacValGrp_CC_SWREQ.getValueNames())
    xdmacSym_CC_SWREQ.setLabel(xdmacBitField_CC_SWREQ.getDescription())
    xdmacSym_CC_SWREQ.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_SWREQ.setDefaultValue("HWR_CONNECTED")

    xdmacSym_CC_SAM = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SAM", xdmacChannelMenu, xdmacValGrp_CC_SAM.getValueNames())
    xdmacSym_CC_SAM.setLabel(xdmacBitField_CC_SAM.getDescription())
    xdmacSym_CC_SAM.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_SAM.setDefaultValue("INCREMENTED_AM")

    xdmacSym_CC_DAM = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DAM", xdmacChannelMenu, xdmacValGrp_CC_DAM.getValueNames())
    xdmacSym_CC_DAM.setLabel(xdmacBitField_CC_DAM.getDescription())
    xdmacSym_CC_DAM.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_DAM.setDefaultValue("INCREMENTED_AM")

    xdmacSym_CC_SIF = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SIF", xdmacChannelMenu, xdmacValGrp_CC_SIF.getValueNames())
    xdmacSym_CC_SIF.setLabel(xdmacBitField_CC_SIF.getDescription())
    xdmacSym_CC_SIF.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_SIF.setDefaultValue("AHB_IF1")

    xdmacSym_CC_DIF = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DIF", xdmacChannelMenu, xdmacValGrp_CC_DIF.getValueNames())
    xdmacSym_CC_DIF.setLabel(xdmacBitField_CC_DIF.getDescription())
    xdmacSym_CC_DIF.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_DIF.setDefaultValue("AHB_IF1")

    xdmacSym_CC_DWIDTH = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DWIDTH", xdmacChannelMenu, xdmacValGrp_CC_DWIDTH.getValueNames())
    xdmacSym_CC_DWIDTH.setLabel(xdmacBitField_CC_DWIDTH.getDescription())
    xdmacSym_CC_DWIDTH.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_DWIDTH.setDefaultValue("BYTE")

    xdmacSym_CC_CSIZE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_CSIZE", xdmacChannelMenu, xdmacValGrp_CC_CSIZE.getValueNames())
    xdmacSym_CC_CSIZE.setLabel(xdmacBitField_CC_CSIZE.getDescription())
    xdmacSym_CC_CSIZE.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_CSIZE.setDefaultValue("CHK_1")

    xdmacSym_CC_MBSIZE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_MBSIZE", xdmacChannelMenu, xdmacValGrp_CC_MBSIZE.getValueNames())
    xdmacSym_CC_MBSIZE.setLabel(xdmacBitField_CC_MBSIZE.getDescription())
    xdmacSym_CC_MBSIZE.setDependencies(xdmacTriggerLogic, ["XDMAC_CC"+ str(channelID)+"_PERID"])
    xdmacSym_CC_MBSIZE.setDefaultValue("SINGLE")

xdmacEnable.setDependencies(xdmacGlobalLogic, xdmacChannelIds)
xdmacHighestCh.setDependencies(xdmacGlobalLogic, xdmacChannelIds)

# Interface for Peripheral clients
for per in peridList:
    xdmacChannelNeeded = coreComponent.createBooleanSymbol("DMA_CH_NEEDED_FOR_" + str(per), xdmacChannelMenu)
    xdmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(per))
    xdmacChannelNeeded.setDefaultValue(False)
    xdmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(per))

    xdmacChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(per), xdmacChannelMenu)
    xdmacChannel.setLabel("Local DMA_CH_FOR_" + str(per))
    xdmacChannel.setDefaultValue(-1)
    xdmacChannel.setVisible(False)

xdmacPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", xdmacChannelMenu)
xdmacPERIDChannelUpdate.setLabel("Local xdmacChannelAllocLogic")
xdmacPERIDChannelUpdate.setDefaultValue(False)
xdmacPERIDChannelUpdate.setVisible(False)
xdmacPERIDChannelUpdate.setDependencies(xdmacChannelAllocLogic, peridValueListSymbols)
################################################################################
#### Dependency ####
################################################################################


################################################################################
#### Code Generation ####
################################################################################
configName = Variables.get("__CONFIGURATION_NAME")

xdmacHeaderFile = coreComponent.createFileSymbol("xdmacHeaderFile", None)
xdmacHeaderFile.setMarkup(True)
xdmacHeaderFile.setSourcePath("../peripheral/xdmac_11161/templates/plib_xdmac.h.ftl")
xdmacHeaderFile.setOutputName("plib_xdmac.h")
xdmacHeaderFile.setDestPath("/peripheral/xdmac/")
xdmacHeaderFile.setProjectPath("config/" + configName +"/peripheral/xdmac/")
xdmacHeaderFile.setType("HEADER")
xdmacHeaderFile.setOverwrite(True)
xdmacHeaderFile.setEnabled(False)

xdmacSourceFile = coreComponent.createFileSymbol("xdmacSourceFile", None)
xdmacSourceFile.setMarkup(True)
xdmacSourceFile.setSourcePath("../peripheral/xdmac_11161/templates/plib_xdmac.c.ftl")
xdmacSourceFile.setOutputName("plib_xdmac.c")
xdmacSourceFile.setDestPath("/peripheral/xdmac/")
xdmacSourceFile.setProjectPath("config/" + configName +"/peripheral/xdmac/")
xdmacSourceFile.setType("SOURCE")
xdmacSourceFile.setOverwrite(True)
xdmacSourceFile.setEnabled(False)

xdmacSystemInitFile = coreComponent.createFileSymbol("xdmacSystemInitFile", None)
xdmacSystemInitFile.setType("STRING")
xdmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
xdmacSystemInitFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_initialize.c.ftl")
xdmacSystemInitFile.setMarkup(True)
xdmacSystemInitFile.setEnabled(False)

xdmacSystemDefFile = coreComponent.createFileSymbol("xdmacSystemDefFile", None)
xdmacSystemDefFile.setType("STRING")
xdmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
xdmacSystemDefFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_definitions.h.ftl")
xdmacSystemDefFile.setMarkup(True)
xdmacSystemDefFile.setEnabled(False)

xdmacSystemConfigFile = coreComponent.createFileSymbol("xdmacSystemConfigFile", None)
xdmacSystemConfigFile.setType("STRING")
xdmacSystemConfigFile.setOutputName("core.LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION")
xdmacSystemConfigFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_config.h.ftl")
xdmacSystemConfigFile.setMarkup(True)
xdmacSystemConfigFile.setEnabled(False)
