from math import ceil
from os.path import join
from xml.etree import ElementTree

###################################################################################################
########################### Register Interface   #################################
###################################################################################################	

afecRegModule = Register.getRegisterModule("AFEC")
afecRegGroup = afecRegModule.getRegisterGroup("AFEC")

#Result resolution
afecReg_EMR = afecRegGroup.getRegister("AFEC_EMR")
afecBitField_EMR_RES = afecReg_EMR.getBitfield("RES")
adcValGroup_EMR_RES = afecRegModule.getValueGroup("AFEC_EMR__RES")
adcValGroup_EMR_RESDefault = adcValGroup_EMR_RES.getValue("NO_AVERAGE")

#Result sign
afecBitField_SIGNMODE = afecReg_EMR.getBitfield("SIGNMODE")
adcValGroup_EMR_SIGNMODE = afecRegModule.getValueGroup("AFEC_EMR__SIGNMODE")
adcValGroup_EMR_SIGNMODEDefault = adcValGroup_EMR_SIGNMODE.getValue("SE_UNSG_DF_SIGN")

###################################################################################################
########################### Global variables   #################################
###################################################################################################	

global num

afecSym_SEQ1R_USCH = []
afecCHMenu = []
afecSym_CH_CHER = []
afecSym_CH_NAME = []
afecSym_CH_PositiveInput = []
afecSym_CH_NegativeInput = []
afecSym_CH_SHMR_DUAL = []
afecSym_CH_DUAL_CHANNEL = []
afecSym_CH_CGR_GAIN = []
afecSym_CH_COCR_AOFF = []
afecSym_CH_IER_EOC = []

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################	

def afecClockControl(symbol, event):
	clockSet = False
	Database.clearSymbolValue("core", "PMC_ID_AFEC" + str(num))
	for channelID in range(0, 12):
		if (afecSym_CH_CHER[channelID].getValue() == True):
			clockSet = True
	if(clockSet == True):
		Database.setSymbolValue("core", "PMC_ID_AFEC" + str(num), True, 2)
	else:
		Database.setSymbolValue("core", "PMC_ID_AFEC" + str(num), False, 2)	
		
def afecNVICControl(symbol, event):
	nvicSet = False
	peripId = Interrupt.getInterruptIndex("AFEC" + str(num))
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"	
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	Database.clearSymbolValue("core", NVICHandlerLock)
	for channelID in range(0, 12):
		if (afecSym_CH_IER_EOC[channelID].getValue() == True):
			nvicSet = True
	if(nvicSet == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "AFEC"+str(num)+"_InterruptHandler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	else:
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "AFEC"+str(num)+"_Handler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, False, 2)

def dependencyClockStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

def dependencyIntStatus(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)		
		
def afecGetMasterClock():
	main_clk_freq = int(Database.getSymbolValue("core","MASTERCLK_FREQ"))
	return main_clk_freq
	
def afecCalcPrescal(afecSym_MR_PRESCAL, event ):
	clock = afecGetMasterClock()
	afecSym_MR_PRESCAL.setValue(int(ceil(clock/afecSym_Clock.getValue())), 1)
	
def afecCalcConversionTime(afecSym_CONV_TIME, event):
	global afecSym_MR_PRESCAL
	prescaler = afecSym_MR_PRESCAL.getValue()
	result_resolution = afecSym_EMR_RES_VALUE.getSelectedKey()
	multiplier = 1
	if (result_resolution == "NO_AVERAGE"):
		multiplier = 1
	if (result_resolution == "OSR4"):
		multiplier = 4
	if (result_resolution == "OSR16"):
		multiplier = 16
	if (result_resolution == "OSR64"):
		multiplier = 64
	if (result_resolution == "OSR256"):
		multiplier = 256
	conv_time = (prescaler * 23.0 * 1000000.0 * multiplier) / afecGetMasterClock()
	afecSym_CONV_TIME.setLabel("**** Conversion Time is "+str(conv_time)+" us ****")

def afecUserSeqVisible(afecSym_SEQ1R_USCHLocal, event):
	for channelID in range(0, 12):
		if (event["value"] == True):
			afecSym_SEQ1R_USCH[channelID].setVisible(True)
		else:
			afecSym_SEQ1R_USCH[channelID].setVisible(False)

def afecCHNameVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_NAME[channelID].setVisible(True)
	else:
		afecSym_CH_NAME[channelID].setVisible(False)
		
def afecCHPosInpVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_PositiveInput[channelID].setVisible(True)
	else:
		afecSym_CH_PositiveInput[channelID].setVisible(False)
		
def afecCHNegInpVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_NegativeInput[channelID].setVisible(True)
	else:
		afecSym_CH_NegativeInput[channelID].setVisible(False)
		
def afecCHDualVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_SHMR_DUAL[channelID].setVisible(True)
	else:
		afecSym_CH_SHMR_DUAL[channelID].setVisible(False)

def afecCHDualCommentVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_DUAL_CHANNEL[channelID].setVisible(True)
	else:
		afecSym_CH_DUAL_CHANNEL[channelID].setVisible(False)
		
def afecCHGainVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_CGR_GAIN[channelID].setVisible(True)
	else:
		afecSym_CH_CGR_GAIN[channelID].setVisible(False)

def afecCHOffsetVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_COCR_AOFF[channelID].setVisible(True)
	else:
		afecSym_CH_COCR_AOFF[channelID].setVisible(False)

def afecCHInterruptVisible(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	if (event["value"] == True):
		afecSym_CH_IER_EOC[channelID].setVisible(True)
	else:
		afecSym_CH_IER_EOC[channelID].setVisible(False)

def afecCHEnable(symbol, event):
	id = []
	#split as per "_" to get the channel number
	id = symbol.getID().split("_")
	channelID = int(id[1])
	
	#for dual mode, enable corresponding channel pair
	if(event["id"].find("_SHMR_DUAL") > 0):
		if(event["value"] == True):
			afecSym_CH_CHER[channelID].clearValue()
			afecSym_CH_CHER[channelID].setValue(True, 1)
		else:
			afecSym_CH_CHER[channelID].clearValue()
			afecSym_CH_CHER[channelID].setValue(False, 1)	

	#for diff mode, hide next odd channel 
	if(event["id"].find("_NEG_INP") > 0):
		if(event["value"] == "AN"+str(channelID)):
			afecCHMenu[channelID].setVisible(False)
		else:
			afecCHMenu[channelID].setVisible(True)

###################################################################################################
########################### Component   #################################
###################################################################################################				
def instantiateComponent(afecComponent):
	global num
	num = afecComponent.getID()[-1:]
	Log.writeInfoMessage("Running AFEC" + str(num))
	
	#------------------------- ATDF Read -------------------------------------
	packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
	availablePins = []		# array to save available pins
	channel = [False, False, False, False, False, False, False, False, False, False, False, False] #array t0 save available channels
	afecChannelsValues = [] #array used for combo symbol
	afecChannelsValues.append("NONE")
	i = 0
	
	#Read atdf file
	atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
	
	try:
		atdfFile = open(atdfFilePath, "r")
	except:
		Log.writeInfoMessage("afec.py peripheral AFEC: Error!!! while opening atdf file")
		
	atdfContent = ElementTree.fromstring(atdfFile.read())
	
	# Save pins in availablePins array as per selected package 
	for package in atdfContent.iter("pinout"):
		if packageName in package.attrib["name"]:
			for pad in package.iter("pin"):
				availablePins.append(pad.attrib["pad"])
	
	#Find available channels
	for peripheral in atdfContent.iter("module"):
		if "AFEC" in peripheral.attrib["name"]:
			for instance in peripheral.iter("instance"):
				if "AFEC"+str(num) in instance.attrib["name"]:
					for signal in instance.iter("signals"):
						for pad in signal.iter("signal"):
							if "index" in pad.attrib:
								pin = pad.attrib["pad"]
								if pin in availablePins:
									channel[i] = (True)
									afecChannelsValues.append("CH"+str(pad.attrib["index"]))
								else:
									channel[i] = (False)
								i = i + 1

	# Clock dynamic settings
	afecSym_ClockControl = afecComponent.createBooleanSymbol("AFEC_CLOCK_ENABLE", None)
	afecSym_ClockControl.setDependencies(afecClockControl, ["AFEC_0_CHER", "AFEC_1_CHER", "AFEC_2_CHER", "AFEC_3_CHER", "AFEC_4_CHER", \
	"AFEC_5_CHER", "AFEC_6_CHER", "AFEC_7_CHER", "AFEC_8_CHER", "AFEC_9_CHER", "AFEC_10_CHER", "AFEC_11_CHER"])
	afecSym_ClockControl.setVisible(False)		
	
	# NVIC Dynamic settings
	afecSym_NVICControl = afecComponent.createBooleanSymbol("AFEC_NVIC_ENABLE", None)
	afecSym_NVICControl.setDependencies(afecNVICControl, ["AFEC_0_IER_EOC", "AFEC_1_IER_EOC", "AFEC_2_IER_EOC", "AFEC_3_IER_EOC", "AFEC_4_IER_EOC",\
	"AFEC_5_IER_EOC","AFEC_6_IER_EOC","AFEC_7_IER_EOC","AFEC_8_IER_EOC","AFEC_9_IER_EOC","AFEC_10_IER_EOC","AFEC_11_IER_EOC"])
	afecSym_NVICControl.setVisible(False)
	
	# Dependency Status
	afecSym_ClkEnComment = afecComponent.createCommentSymbol("AFEC_CLK_ENABLE_COMMENT", None)
	afecSym_ClkEnComment.setVisible(False)
	afecSym_ClkEnComment.setLabel("Warning!!! AFEC" +str(num)+" Peripheral Clock is Disabled in Clock Manager")
	afecSym_ClkEnComment.setDependencies(dependencyClockStatus, ["core.PMC_ID_AFEC" + str(num)])
	
	periphId = Interrupt.getInterruptIndex("AFEC" + str(num))
	NVICVector = "NVIC_" + str(periphId) + "_ENABLE"

	afecSym_IntEnComment = afecComponent.createCommentSymbol("AFEC_NVIC_ENABLE_COMMENT", None)
	afecSym_IntEnComment.setVisible(False)
	afecSym_IntEnComment.setLabel("Warning!!! AFEC" +str(num)+" Interrupt is Disabled in Interrupt Manager")
	afecSym_IntEnComment.setDependencies(dependencyIntStatus, ["core." + NVICVector])
		
	afecMenu = afecComponent.createMenuSymbol(None, None)
	afecMenu.setLabel("ADC Configuration")
	
	#clock selection
	afecSym_Clock = afecComponent.createIntegerSymbol("AFEC_CLK", afecMenu)
	afecSym_Clock.setLabel("Clock Frequency (Hz)")
	afecSym_Clock.setMin(4000000)
	afecSym_Clock.setMax(40000000)
	afecSym_Clock.setDefaultValue(20000000)

	#Result resolution
	global afecSym_EMR_RES_VALUE
	afecSym_EMR_RES_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_RES_VALUE", afecMenu)
	afecSym_EMR_RES_VALUE.setLabel ("Result Resolution")
	afecSym_EMR_RES_VALUE.setDefaultValue(3)
	afecSym_EMR_RES_VALUE.setOutputMode("Key")
	afecSym_EMR_RES_VALUE.setDisplayMode("Description")
	count = adcValGroup_EMR_RES.getValueCount()
	for id in range(0,count):
		valueName = adcValGroup_EMR_RES.getValueNames()[id]
		afecSym_EMR_RES_VALUE.addKey(valueName, adcValGroup_EMR_RES.getValue(valueName).getValue(), adcValGroup_EMR_RES.getValue(valueName).getDescription())

	#Single trigger mode
	afecSym_EMR_STM = afecComponent.createBooleanSymbol("AFEC_EMR_STM", afecMenu)
	afecSym_EMR_STM.setLabel("Averaging Single Trigger Mode")
	afecSym_EMR_STM.setDefaultValue(False)
		
	#Clock prescaler
	global afecSym_MR_PRESCAL
	afecSym_MR_PRESCAL = afecComponent.createIntegerSymbol("AFEC_MR_PRESCAL", afecMenu)
	afecSym_MR_PRESCAL.setVisible(False)
	afecSym_MR_PRESCAL.setDefaultValue(5)
	afecSym_MR_PRESCAL.setDependencies(afecCalcPrescal, ["AFEC_CLK", "core.MASTERCLK_FREQ"])
	
	#Conversion time
	afecSym_CONV_TIME = afecComponent.createCommentSymbol("AFEC_CONV_TIME", afecMenu)
	afecSym_CONV_TIME.setLabel("**** Conversion Time is 1.15 us ****")
	afecSym_CONV_TIME.setDependencies(afecCalcConversionTime, ["AFEC_CLK", "AFEC_EMR_RES_VALUE", "core.MASTERCLK_FREQ"])
	
	#Result sign
	afecSym_EMR_SIGNMODE_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_EMR_SIGNMODE_VALUE", afecMenu)
	afecSym_EMR_SIGNMODE_VALUE.setLabel ("Result Sign")
	afecSym_EMR_SIGNMODE_VALUE.setDefaultValue(3)
	afecSym_EMR_SIGNMODE_VALUE.setOutputMode("Key")
	afecSym_EMR_SIGNMODE_VALUE.setDisplayMode("Description")
	count = adcValGroup_EMR_SIGNMODE.getValueCount()
	for id in range(0,count):
		valueName = adcValGroup_EMR_SIGNMODE.getValueNames()[id]
		afecSym_EMR_SIGNMODE_VALUE.addKey(valueName, adcValGroup_EMR_SIGNMODE.getValue(valueName).getValue(), adcValGroup_EMR_SIGNMODE.getValue(valueName).getDescription())
	
	#Free run mode
	afecSym_MR_FREERUN = afecComponent.createBooleanSymbol("AFEC_MR_FREERUN", afecMenu)
	afecSym_MR_FREERUN.setLabel("Enable Free Running Mode")
	afecSym_MR_FREERUN.setDefaultValue(False)
	
	#Conversion trigger
	afecSym_MR_TRGEN = afecComponent.createBooleanSymbol("AFEC_MR_TRGEN", afecMenu)
	afecSym_MR_TRGEN.setLabel("Enable External Trigger Mode")
	afecSym_MR_TRGEN.setDefaultValue(False)
	
	#Trigger
	afecSym_MR_TRGSEL_VALUE = afecComponent.createKeyValueSetSymbol("AFEC_MR_TRGSEL_VALUE", afecSym_MR_TRGEN)
	afecSym_MR_TRGSEL_VALUE.setLabel ("Select External Trigger Input")
	afecSym_MR_TRGSEL_VALUE.setDefaultValue(1)
	afecSym_MR_TRGSEL_VALUE.setOutputMode("Key")
	afecSym_MR_TRGSEL_VALUE.setDisplayMode("Description")
	for peripheral in atdfContent.iter("module"):
		if "AFEC" in peripheral.attrib["name"]:
			for instance in peripheral.iter("instance"):
				if "AFEC"+str(num) in instance.attrib["name"]:
					for param in instance.iter("parameters"):
						for trigger in param.iter("param"):
							if "TRGSEL" in trigger.attrib["name"]:
								afecSym_MR_TRGSEL_VALUE.addKey(trigger.attrib["name"], trigger.attrib["value"], trigger.attrib["caption"])
	
	#------------------------------------------------------------------------------------
	#user sequence menu
	afecUserSeq = afecComponent.createMenuSymbol("AFEC_USER_SEQ", None)
	afecUserSeq.setLabel("User Channel Sequence Configuration")
	
	#user sequence comment
	afecSym_USEQ_COMMENT = afecComponent.createCommentSymbol("AFEC_USEQ_COMMENT", afecUserSeq)
	afecSym_USEQ_COMMENT.setLabel("**** Configure selected channels in the Channel Configuration Menu ****")
	
	#enable user sequence
	afecSym_MR_USEQ = afecComponent.createBooleanSymbol("AFEC_MR_USEQ", afecUserSeq)
	afecSym_MR_USEQ.setLabel("Enable User Sequence Mode")
	afecSym_MR_USEQ.setDefaultValue(False)
	
	for channelID in range(0, 12):
		#channel selection for user sequence
		afecSym_SEQ1R_USCH.append(channelID)
		afecSym_SEQ1R_USCH[channelID] = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH"+str(channelID), afecSym_MR_USEQ, afecChannelsValues)
		afecSym_SEQ1R_USCH[channelID].setLabel ("Select Channel for Sequence Number "+str(channelID))
		afecSym_SEQ1R_USCH[channelID].setDefaultValue(afecChannelsValues[0])
		afecSym_SEQ1R_USCH[channelID].setVisible(False)
		afecSym_SEQ1R_USCH[channelID].setDependencies(afecUserSeqVisible, ["AFEC_MR_USEQ"])
	#--------------------------------------------------------------------------------------

	afecCHConfMenu = afecComponent.createMenuSymbol("AFEC_CH_CONF", None)
	afecCHConfMenu.setLabel("Channel Configuration")
	
	# Loop runs for 12 channels and visibility of the channel is controlled as per available pins
	for channelID in range(0, 12):
		#Channel menu
		global afecCHMenu
		afecCHMenu.append(channelID)
		afecCHMenu[channelID] = afecComponent.createMenuSymbol("CH"+str(channelID), afecCHConfMenu)
		afecCHMenu[channelID].setLabel("Channel "+str(channelID))
		#Show channels as per available pins in package
		if (channel[channelID] == False):
			afecCHMenu[channelID].setVisible(False)
		
		#Channel enable
		afecSym_CH_CHER.append(channelID)
		afecSym_CH_CHER[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_CHER", afecCHMenu[channelID])
		afecSym_CH_CHER[channelID].setLabel("Enable Channel " + str(channelID))
		afecSym_CH_CHER[channelID].setDefaultValue(False)
		#enable corresponding channel pair of dual mode
		#e.g. for dual mode, CH0 and CH6
		#for diff mode, CH0 and CH1
		if((channelID > 5)):
			if (channelID % 2 == 1):
				afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-6)+"_SHMR_DUAL", "AFEC_"+str(channelID-1)+"_NEG_INP"])
			else:
				afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-6)+"_SHMR_DUAL"])
		elif (channelID % 2 == 1):
			afecSym_CH_CHER[channelID].setDependencies(afecCHEnable, ["AFEC_"+str(channelID-1)+"_NEG_INP"])
		
		#Channel name
		afecSym_CH_NAME.append(channelID)
		afecSym_CH_NAME[channelID] = afecComponent.createStringSymbol("AFEC_"+str(channelID)+"_NAME", afecSym_CH_CHER[channelID])
		afecSym_CH_NAME[channelID].setLabel ("Name")
		afecSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
		afecSym_CH_NAME[channelID].setVisible(False)
		afecSym_CH_NAME[channelID].setDependencies(afecCHNameVisible, ["AFEC_"+str(channelID)+"_CHER"])
		
		#Channel positive input
		afecSym_CH_PositiveInput.append(channelID)
		afecSym_CH_PositiveInput[channelID] = afecComponent.createStringSymbol("AFEC_"+str(channelID)+"_POS_INP", afecSym_CH_CHER[channelID])
		afecSym_CH_PositiveInput[channelID].setLabel ("Positive Input")
		afecSym_CH_PositiveInput[channelID].setDefaultValue("AN"+str(channelID))
		afecSym_CH_PositiveInput[channelID].setReadOnly(True)
		afecSym_CH_PositiveInput[channelID].setVisible(False)
		afecSym_CH_PositiveInput[channelID].setDependencies(afecCHPosInpVisible, ["AFEC_"+str(channelID)+"_CHER"])
		
		#Channel negative input
		afecSym_CH_NegativeInput.append(channelID)
		afecSym_CH0_NEG_INPValues = ["GND", "AN"+str(channelID+1)]
		afecSym_CH_NegativeInput[channelID] = afecComponent.createComboSymbol("AFEC_"+str(channelID)+"_NEG_INP", afecSym_CH_CHER[channelID], afecSym_CH0_NEG_INPValues)
		afecSym_CH_NegativeInput[channelID].setLabel ("Negative Input")
		afecSym_CH_NegativeInput[channelID].setDefaultValue("GND")
		afecSym_CH_NegativeInput[channelID].setVisible(False)
		afecSym_CH_NegativeInput[channelID].setDependencies(afecCHNegInpVisible, ["AFEC_"+str(channelID)+"_CHER"])

		#Dual mode
		afecSym_CH_SHMR_DUAL.append(channelID)
		if(channelID < 6 ):
			afecSym_CH_SHMR_DUAL[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_SHMR_DUAL", afecSym_CH_CHER[channelID])
			afecSym_CH_SHMR_DUAL[channelID].setLabel("Dual Sample and Hold")
			afecSym_CH_SHMR_DUAL[channelID].setDefaultValue(False)
			afecSym_CH_SHMR_DUAL[channelID].setVisible(False)
			afecSym_CH_SHMR_DUAL[channelID].setDependencies(afecCHDualVisible, ["AFEC_"+str(channelID)+"_CHER"])
			
		afecSym_CH_DUAL_CHANNEL.append(channelID)
		if(channelID < 6 ):
			afecSym_CH_DUAL_CHANNEL[channelID] = afecComponent.createCommentSymbol("AFEC_"+str(channelID)+"_DUAL_CHANNEL", afecSym_CH_CHER[channelID])
			afecSym_CH_DUAL_CHANNEL[channelID].setLabel("**** Channel "+str(channelID + 6)+" is converted along with Channel "+str(channelID)+ ". Configure CHANNEL "+str(channelID + 6) + " ****")
			afecSym_CH_DUAL_CHANNEL[channelID].setVisible(False)
			afecSym_CH_DUAL_CHANNEL[channelID].setDependencies(afecCHDualCommentVisible, ["AFEC_"+str(channelID)+"_SHMR_DUAL"])
			
		#Channel gain
		afecGainValues = ["X1", "X2", "X4"]
		afecSym_CH_CGR_GAIN.append(channelID)
		afecSym_CH_CGR_GAIN[channelID] = afecComponent.createComboSymbol("AFEC_"+str(channelID)+"_CGR_GAIN", afecSym_CH_CHER[channelID], afecGainValues)
		afecSym_CH_CGR_GAIN[channelID].setLabel("Gain")
		afecSym_CH_CGR_GAIN[channelID].setDefaultValue("X1")
		afecSym_CH_CGR_GAIN[channelID].setVisible(False)
		afecSym_CH_CGR_GAIN[channelID].setDependencies(afecCHGainVisible, ["AFEC_"+str(channelID)+"_CHER"])
		
		#Channel offset
		afecSym_CH_COCR_AOFF.append(channelID)
		afecSym_CH_COCR_AOFF[channelID] = afecComponent.createIntegerSymbol("AFEC_"+str(channelID)+"_COCR_AOFF", afecSym_CH_CHER[channelID])
		afecSym_CH_COCR_AOFF[channelID].setLabel("Offset")
		afecSym_CH_COCR_AOFF[channelID].setDefaultValue(512)
		afecSym_CH_COCR_AOFF[channelID].setVisible(False)
		afecSym_CH_COCR_AOFF[channelID].setDependencies(afecCHOffsetVisible, ["AFEC_"+str(channelID)+"_CHER"])
		
		#Channel interrupt
		afecSym_CH_IER_EOC.append(channelID)
		afecSym_CH_IER_EOC[channelID] = afecComponent.createBooleanSymbol("AFEC_"+str(channelID)+"_IER_EOC", afecSym_CH_CHER[channelID])
		afecSym_CH_IER_EOC[channelID].setLabel("End of conversion interrupt")
		afecSym_CH_IER_EOC[channelID].setDefaultValue(False)
		afecSym_CH_IER_EOC[channelID].setVisible(False)
		afecSym_CH_IER_EOC[channelID].setDependencies(afecCHInterruptVisible, ["AFEC_"+str(channelID)+"_CHER"])
	
	#--------------------------------------------------------------------------------------
	afecIndex = afecComponent.createIntegerSymbol("INDEX", afecMenu)
	afecIndex.setVisible(False)
	afecIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")
	
###################################################################################################
########################### Code Generation   #################################
###################################################################################################		

	afecHeaderFile = afecComponent.createFileSymbol(None, None)
	afecHeaderFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/plib_afec.h.ftl")
	afecHeaderFile.setOutputName("plib_afec" + str(num) + ".h")
	afecHeaderFile.setDestPath("peripheral/afec/")
	afecHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
	afecHeaderFile.setType("HEADER")
	afecHeaderFile.setMarkup(True)
	
	afecGlobalHeaderFile = afecComponent.createFileSymbol(None, None)
	afecGlobalHeaderFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID() + "/plib_afec.h")
	afecGlobalHeaderFile.setOutputName("plib_afec.h")
	afecGlobalHeaderFile.setDestPath("peripheral/afec/")
	afecGlobalHeaderFile.setProjectPath("/peripheral/afec/")
	afecGlobalHeaderFile.setType("HEADER")
	
	afecSource1File = afecComponent.createFileSymbol(None, None)
	afecSource1File.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/plib_afec.c.ftl")
	afecSource1File.setOutputName("plib_afec" + str(num) + ".c")
	afecSource1File.setDestPath("peripheral/afec/")
	afecSource1File.setProjectPath("/peripheral/afec/")
	afecSource1File.setType("SOURCE")
	afecSource1File.setMarkup(True)

	afecSystemInitFile = afecComponent.createFileSymbol(None, None)
	afecSystemInitFile.setType("STRING")
	afecSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
	afecSystemInitFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/system/system_initialize.h.ftl")
	afecSystemInitFile.setMarkup(True)

	afecSystemDefFile = afecComponent.createFileSymbol(None, None)
	afecSystemDefFile.setType("STRING")
	afecSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	afecSystemDefFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/system/system_definitions.h.ftl")
	afecSystemDefFile.setMarkup(True)