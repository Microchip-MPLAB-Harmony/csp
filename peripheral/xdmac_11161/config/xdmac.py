print("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

xdmacMenu = coreComponent.createMenuSymbol(None, None)
xdmacMenu.setLabel("DMA")
xdmacMenu.setDescription("Configuration for DMA Service")

xdmacEnable = coreComponent.createBooleanSymbol("xdmacEnable", xdmacMenu)
xdmacEnable.setLabel("Use DMA Service?")
xdmacEnable.setDefaultValue(True)
xdmacEnable.setVisible(False)

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

def xdmacTransferType(xdmacSym, type):
	print(type.getValue())
	if (type.getValue() == "PER_TRAN"):
		xdmacSym.setVisible(True)
	else :
		xdmacSym.setVisible(False)

xdmacChannelLinkedList = coreComponent.createBooleanSymbol("XDMAC_LL_ENABLE", xdmacMenu)
xdmacChannelLinkedList.setLabel("Use Linked List Mode?")
xdmacChannelLinkedList.setDefaultValue(False)

# Number of channels value is not available as symbol in ATDF. hence hard coded.
for channelID in range(0, 24):
	
	xdmacChannelEnable = coreComponent.createBooleanSymbol("XDMAC_CH"+str(channelID)+"_ENABLE", xdmacMenu)
	xdmacChannelEnable.setLabel("Enable XDMAC Channel "+ str(channelID))
	xdmacChannelEnable.setDefaultValue(False)

	xdmacChannelMenu = coreComponent.createMenuSymbol("XDMAC_CH"+str(channelID)+"CONFIG", xdmacChannelEnable)
	xdmacChannelMenu.setLabel("XDMAC Channel " + str(channelID) + " Settings")
	xdmacChannelMenu.setDescription("Configuration for DMA Channel"+ str(channelID))

	xdmacSym_CC_TYPE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_TYPE", xdmacChannelMenu, xdmacValGrp_CC_TYPE.getValueNames())
	print(xdmacSym_CC_TYPE)
	xdmacSym_CC_TYPE.setLabel(xdmacBitField_CC_TYPE.getDescription())
	# Default value is set later to trigger business logic initially
	
	xdmacSym_CC_PERID = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_PERID", xdmacChannelMenu, xdmacValGrp_CC_PERID.getValueNames())
	print(xdmacSym_CC_PERID)
	xdmacSym_CC_PERID.setLabel(xdmacBitField_CC_PERID.getDescription())
	xdmacSym_CC_PERID.setDefaultValue("HSMCI_TX")
	xdmacSym_CC_PERID.setDependencies(xdmacTransferType, ["XDMAC_CC"+ str(channelID)+"_TYPE"])
	
	xdmacSym_CC_DSYNC = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DSYNC", xdmacChannelMenu, xdmacValGrp_CC_DSYNC.getValueNames())
	print(xdmacSym_CC_DSYNC)
	xdmacSym_CC_DSYNC.setLabel(xdmacBitField_CC_DSYNC.getDescription())
	xdmacSym_CC_DSYNC.setDefaultValue("PER2MEM")
	xdmacSym_CC_DSYNC.setDependencies(xdmacTransferType, ["XDMAC_CC"+ str(channelID)+"_TYPE"])
	
	xdmacSym_CC_SWREQ = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SWREQ", xdmacChannelMenu, xdmacValGrp_CC_SWREQ.getValueNames())
	print(xdmacSym_CC_SWREQ)
	xdmacSym_CC_SWREQ.setLabel(xdmacBitField_CC_SWREQ.getDescription())
	xdmacSym_CC_SWREQ.setDefaultValue("HWR_CONNECTED")
	xdmacSym_CC_SWREQ.setDependencies(xdmacTransferType, ["XDMAC_CC"+ str(channelID)+"_TYPE"])
	xdmacSym_CC_TYPE.setDefaultValue("MEM_TRAN")
	
	xdmacSym_CC_SAM = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SAM", xdmacChannelMenu, xdmacValGrp_CC_SAM.getValueNames())
	print(xdmacSym_CC_SAM)
	xdmacSym_CC_SAM.setLabel(xdmacBitField_CC_SAM.getDescription())
	xdmacSym_CC_SAM.setDefaultValue("INCREMENTED_AM")
	
	xdmacSym_CC_DAM = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DAM", xdmacChannelMenu, xdmacValGrp_CC_DAM.getValueNames())
	print(xdmacSym_CC_DAM)
	xdmacSym_CC_DAM.setLabel(xdmacBitField_CC_DAM.getDescription())
	xdmacSym_CC_DAM.setDefaultValue("INCREMENTED_AM")
	
	xdmacSym_CC_SIF = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_SIF", xdmacChannelMenu, xdmacValGrp_CC_SIF.getValueNames())
	print(xdmacSym_CC_SIF)
	xdmacSym_CC_SIF.setLabel(xdmacBitField_CC_SIF.getDescription())
	xdmacSym_CC_SIF.setDefaultValue("AHB_IF1")
	
	xdmacSym_CC_DIF = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DIF", xdmacChannelMenu, xdmacValGrp_CC_DIF.getValueNames())
	print(xdmacSym_CC_DIF)
	xdmacSym_CC_DIF.setLabel(xdmacBitField_CC_DIF.getDescription())
	xdmacSym_CC_DIF.setDefaultValue("AHB_IF1")
	
	xdmacSym_CC_DWIDTH = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_DWIDTH", xdmacChannelMenu, xdmacValGrp_CC_DWIDTH.getValueNames())
	print(xdmacSym_CC_DWIDTH)
	xdmacSym_CC_DWIDTH.setLabel(xdmacBitField_CC_DWIDTH.getDescription())
	xdmacSym_CC_DWIDTH.setDefaultValue("BYTE")
	
	xdmacSym_CC_CSIZE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_CSIZE", xdmacChannelMenu, xdmacValGrp_CC_CSIZE.getValueNames())
	print(xdmacSym_CC_CSIZE)
	xdmacSym_CC_CSIZE.setLabel(xdmacBitField_CC_CSIZE.getDescription())
	xdmacSym_CC_CSIZE.setDefaultValue("CHK_1")
	
	xdmacSym_CC_MBSIZE = coreComponent.createComboSymbol("XDMAC_CC"+ str(channelID)+"_MBSIZE", xdmacChannelMenu, xdmacValGrp_CC_MBSIZE.getValueNames())
	print(xdmacSym_CC_MBSIZE)
	xdmacSym_CC_MBSIZE.setLabel(xdmacBitField_CC_MBSIZE.getDescription())
	xdmacSym_CC_MBSIZE.setDefaultValue("SINGLE")
	
configName = Variables.get("__CONFIGURATION_NAME")

xdmacHeaderFile = coreComponent.createFileSymbol(None, None)
xdmacHeaderFile.setMarkup(True)
xdmacHeaderFile.setSourcePath("../peripheral/xdmac_11161/templates/plib_xdmac.h.ftl")
xdmacHeaderFile.setOutputName("plib_xdmac.h")
xdmacHeaderFile.setDestPath("system_config/" + configName +"/peripheral/xdmac/")
xdmacHeaderFile.setProjectPath("system_config/" + configName +"/peripheral/xdmac/")
xdmacHeaderFile.setType("HEADER")
xdmacHeaderFile.setOverwrite(True)

xdmacSourceFile = coreComponent.createFileSymbol(None, None)
xdmacSourceFile.setMarkup(True)
xdmacSourceFile.setSourcePath("../peripheral/xdmac_11161/templates/plib_xdmac.c.ftl")
xdmacSourceFile.setOutputName("plib_xdmac.c")
xdmacSourceFile.setDestPath("system_config/" + configName +"/peripheral/xdmac/")
xdmacSourceFile.setProjectPath("system_config/" + configName +"/peripheral/xdmac/")
xdmacSourceFile.setType("SOURCE")
xdmacSourceFile.setOverwrite(True)