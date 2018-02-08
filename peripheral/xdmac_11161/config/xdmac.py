from os.path import join
from xml.etree import ElementTree

print("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

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

# Parse atdf xml file to get instance name for the peripheral which has DMA id.
# And construct a list of PERIDs
global peridList
peridList = []
peridList.insert(0, "Software Trigger")

global peridValueList
peridValueList = []
peridValueList.insert(0, 200)

atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
try:
	atdfFile = open(atdfFilePath, "r")
except:
	print("xdmac.py peripheral XDMAC: Error!!! while opening atdf file")
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
				peridList.append(instance.attrib['name'] + "_" + name)
				peridValueList.append(param.attrib['value'])

# This is the dictionary for all trigger sources and corresponding XDMAC settings.
# "xdmacTriggerLogic" business logic will override the XDMAC setting values
# based on the trigger source selected.
global triggerSettings
triggerSettings = {"Software Trigger"	: ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART0_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART0_Receive"		: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART1_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART1_Receive"		: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART2_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"USART2_Receive"		: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART0_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART0_Receive"			: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART1_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART1_Receive"			: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART2_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART2_Receive"			: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART3_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART3_Receive"			: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART4_Transmit"		: ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
				"UART4_Receive"			: ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"]}
				# All triggers are yet to be added.

def xdmacTriggerLogic(xdmacSym, event):
	global triggerSettings
	SymID = xdmacSym.getID()
	xdmacSym.clearValue(SymID)
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

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the highest
# index enabled, also if the list is empty then none of the channel is enabled.
# Highest index will be used to create XDMAC objects in source code.
# List empty or non-empty status helps to generate/discard XDMAC code.  

global xdmacActiveChannels
xdmacActiveChannels = []

def xdmacGlobalLogic(xdmacGlobalSym, event):
	global xdmacActiveChannels

	index = event["id"].strip("XDMAC_CH")
	index = index.strip("_ENABLE")
	try:
		index = int(index)
	except:
		return

	globalSymID = xdmacGlobalSym.getID()
	xdmacGlobalSym.clearValue(globalSymID)

	if event["value"] is True:
		if index not in xdmacActiveChannels:
			xdmacActiveChannels.append(index)
	else :
		if index in xdmacActiveChannels:
			xdmacActiveChannels.remove(index)

	xdmacActiveChannels.sort()
	xdmacActiveChannels.reverse()

	# Check if the list is not empty first since list element is accessed in the code
	if xdmacActiveChannels:
		if str(globalSymID) == "XDMAC_HIGHEST_CHANNEL":
			xdmacGlobalSym.setValue(int(xdmacActiveChannels[0]) + 1, 2)

	if str(globalSymID) == "XDMAC_ENABLE":
		if xdmacActiveChannels and xdmacGlobalSym.getValue() is False:
			xdmacGlobalSym.setValue(True, 2)

		if not xdmacActiveChannels:
			xdmacGlobalSym.setValue(False, 2)

def xdmacFileGenLogic(xdmacFileGen, event):

	xdmacHeaderFile = Database.getSymbolByID("core","xdmacHeaderFile")
	xdmacHeaderFile.setEnabled(event["value"])

	xdmacSourceFile = Database.getSymbolByID("core","xdmacSourceFile")
	xdmacSourceFile.setEnabled(event["value"])

	xdmacSystemInitFile = Database.getSymbolByID("core","xdmacSystemInitFile")
	xdmacSystemInitFile.setEnabled(event["value"])

	xdmacSystemIntFile = Database.getSymbolByID("core","xdmacSystemIntFile")
	xdmacSystemIntFile.setEnabled(event["value"])

	xdmacSystemDefFile = Database.getSymbolByID("core","xdmacSystemDefFile")
	xdmacSystemDefFile.setEnabled(event["value"])

def xdmacTriggerCalc(xdmacPERIDVal, event):
	global peridList
	global peridValueList

	perid = event["value"]
	peridIndex = peridList.index(perid)
	peridValueID = xdmacPERIDVal.getID()
	xdmacPERIDVal.clearValue(peridValueID)
	xdmacPERIDVal.setValue(int(peridValueList[peridIndex]), 2)


dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("SAME70:SAME70DMAModel")	

xdmacMenu = coreComponent.createMenuSymbol(None, None)
xdmacMenu.setLabel("DMA (XDMAC)")
xdmacMenu.setDescription("DMA (XDMAC) Configuration")

xdmacEnable = coreComponent.createBooleanSymbol("XDMAC_ENABLE", xdmacMenu)
xdmacEnable.setLabel("Use DMA Service?")
xdmacEnable.setVisible(False)
xdmacEnable.setDefaultValue(False)

xdmacFileGen = coreComponent.createBooleanSymbol(None, xdmacEnable)
xdmacFileGen.setLabel("DMA (XDMAC) File Generation")
xdmacFileGen.setDependencies(xdmacFileGenLogic, ["XDMAC_ENABLE"])
xdmacFileGen.setVisible(False)

xdmacHighestCh = coreComponent.createIntegerSymbol("XDMAC_HIGHEST_CHANNEL", xdmacEnable)
xdmacHighestCh.setLabel("DMA (XDMAC) Highest Active Channel")
xdmacHighestCh.setDependencies(xdmacFileGenLogic, ["XDMAC_ENABLE"])
xdmacHighestCh.setVisible(False)

xdmacChannelLinkedList = coreComponent.createBooleanSymbol("XDMAC_LL_ENABLE", xdmacMenu)
xdmacChannelLinkedList.setLabel("Use Linked List Mode?")
xdmacChannelLinkedList.setDefaultValue(False)

# Create channel enable list to trigger business logic when any of the channel
# is enabled/disabled
xdmacChannelIds = []

# Number of channels value is not available as symbol in ATDF, hence hard coded.
for channelID in range(0, 24):

	xdmacChannelEnable = coreComponent.createBooleanSymbol("XDMAC_CH"+str(channelID)+"_ENABLE", xdmacMenu)
	xdmacChannelEnable.setLabel("Enable XDMAC Channel "+ str(channelID))
	xdmacChannelEnable.setDefaultValue(False)
	xdmacChannelIds.append("XDMAC_CH"+str(channelID)+"_ENABLE")

	xdmacChannelMenu = coreComponent.createMenuSymbol("XDMAC_CH"+str(channelID)+"CONFIG", xdmacChannelEnable)
	xdmacChannelMenu.setLabel("XDMAC Channel " + str(channelID) + " Settings")
	xdmacChannelMenu.setDescription("Configuration for DMA Channel"+ str(channelID))

	xdmacSym_CC_PERID = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_PERID", xdmacChannelMenu, peridList)
	xdmacSym_CC_PERID.setLabel(xdmacBitField_CC_PERID.getDescription())
	xdmacSym_CC_PERID.setDefaultValue("Software Trigger")
	
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
xdmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
xdmacSystemInitFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_initialize.h.ftl")
xdmacSystemInitFile.setMarkup(True)
xdmacSystemInitFile.setEnabled(False)

xdmacSystemIntFile = coreComponent.createFileSymbol("xdmacSystemIntFile", None)
xdmacSystemIntFile.setType("STRING")
xdmacSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
xdmacSystemIntFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_interrupt.c.ftl")
xdmacSystemIntFile.setMarkup(True)
xdmacSystemIntFile.setEnabled(False)

xdmacSystemDefFile = coreComponent.createFileSymbol("xdmacSystemDefFile", None)
xdmacSystemDefFile.setType("STRING")
xdmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
xdmacSystemDefFile.setSourcePath("../peripheral/xdmac_11161/templates/system/system_definitions.h.ftl")
xdmacSystemDefFile.setMarkup(True)
xdmacSystemDefFile.setEnabled(False)
