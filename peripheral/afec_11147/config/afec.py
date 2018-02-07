from math import ceil

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

#Trigger
afecReg_MR = afecRegGroup.getRegister("AFEC_MR")
afecBitField_MR_TRGSEL = afecReg_MR.getBitfield("TRGSEL")
adcValGroup_MR_TRGSEL = afecRegModule.getValueGroup("AFEC_MR__TRGSEL")
adcValGroup_MR_TRGSELDefault = adcValGroup_MR_TRGSEL.getValue("AFEC_TRIG0")

def afecCH1MenuVisible(afecCH1Menu, event):
	if (event["value"] != "GND"):
		print("ch0 diff mode activated")
		afecCH1Menu.setVisible(False)
	else:
		print ("ch0 diff mode disabled")
		afecCH1Menu.setVisible(True)

def afecCalcPrescal(afecSym_MR_PRESCAL, event):
	afecSym_MR_PRESCAL.setValue("AFEC_MR_PRESCAL", int(ceil(150/event["value"])), 1)
	print ("afecCalcPrescal:" + str(afecSym_MR_PRESCAL.getValue()))
	
def afecCalcConversionTime(afecSym_CONV_TIME, event):
	afecDummyPrescaler = 150/event["value"]

	afecSym_CONV_TIME.setValue((((afecDummyPrescaler * 1000000) / 150) * 23 ), 1)
	print ("Conversion Time" + str(afecSym_CONV_TIME.getValue()))
	
def instantiateComponent(afecComponent):

	num = afecComponent.getID()[-1:]
	print("Running AFEC" + str(num))
	
	#------------------------------------------------------------------------------------

	afecMenu = afecComponent.createMenuSymbol(None, None)
	afecMenu.setLabel("Configurations")

	afecSym_Clock = afecComponent.createIntegerSymbol("AFEC_CLK", afecMenu)
	print(afecSym_Clock)
	afecSym_Clock.setLabel("Clock (MHz)")
	#afecSym_Clock.setMin(4)
	#afecSym_Clock.setMax(40)
	afecSym_Clock.setDefaultValue(30)
	
	afecSym_EMR_RES = afecComponent.createComboSymbol("AFEC_EMR_RES", afecMenu, adcValGroup_EMR_RES.getValueNames())
	afecSym_EMR_RES.setLabel ("Result Resolution")
	afecSym_EMR_RES.setDefaultValue(adcValGroup_EMR_RESDefault.getName())
	
	afecSym_MR_PRESCAL = afecComponent.createIntegerSymbol("AFEC_MR_PRESCAL", afecMenu)
	afecSym_MR_PRESCAL.setVisible(False)
	afecSym_MR_PRESCAL.setDefaultValue(5)
	afecSym_MR_PRESCAL.setDependencies(afecCalcPrescal, ["AFEC_CLK"])
	
	afecSym_CONV_TIME = afecComponent.createIntegerSymbol("AFEC_CONV_TIME", afecMenu)
	afecSym_CONV_TIME.setLabel("Conversion Time ")
	afecSym_CONV_TIME.setReadOnly(True)
	afecSym_CONV_TIME.setDefaultValue(766666)
	afecSym_CONV_TIME.setDependencies(afecCalcConversionTime, ["AFEC_CLK"])
	
	afecSym_EMR_SIGNMODE = afecComponent.createComboSymbol("AFEC_EMR_SIGNMODE", afecMenu, adcValGroup_EMR_SIGNMODE.getValueNames())
	afecSym_EMR_SIGNMODE.setLabel ("Result Sign")
	afecSym_EMR_SIGNMODE.setDefaultValue(adcValGroup_EMR_SIGNMODEDefault.getName())
	
	afecSym_MR_FREERUN = afecComponent.createBooleanSymbol("AFEC_MR_FREERUN", afecMenu)
	afecSym_MR_FREERUN.setLabel("Free Run")
	afecSym_MR_FREERUN.setDefaultValue(False)
	
	afecSym_MR_TRGEN = afecComponent.createBooleanSymbol("AFEC_MR_TRGEN", afecMenu)
	afecSym_MR_TRGEN.setLabel("Enable Hardware Trigger")
	afecSym_MR_TRGEN.setDefaultValue(False)
	
	afecSym_MR_TRGSEL = afecComponent.createComboSymbol("AFEC_MR_TRGSEL", afecMenu, adcValGroup_MR_TRGSEL.getValueNames())
	afecSym_MR_TRGSEL.setLabel ("Hardware Trigger")
	afecSym_MR_TRGSEL.setDefaultValue(adcValGroup_MR_TRGSELDefault.getName())

	#------------------------------------------------------------------------------------

	afecUserSeq = afecComponent.createMenuSymbol("AFEC_USER_SEQ", None)
	afecUserSeq.setLabel("User Defined Channel Conversion Sequence")
	
	afecSym_MR_USEQ = afecComponent.createBooleanSymbol("AFEC_MR_USEQ", afecUserSeq)
	afecSym_MR_USEQ.setLabel("Enable User Sequence")
	afecSym_MR_USEQ.setDefaultValue(False)
	
	afecChannelsValues = ["NONE","CH0", "CH1", "CH2", "CH3", "CH4", "CH5", "CH6", "CH7", "CH8", "CH9", "CH10", "CH11"]
	
	afecSym_SEQ1R_USCH0 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH0", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH0.setLabel ("Sequence 0")
	afecSym_SEQ1R_USCH0.setDefaultValue(afecChannelsValues[0])

	
	afecSym_SEQ1R_USCH1 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH1", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH1.setLabel ("Sequence 1")
	afecSym_SEQ1R_USCH1.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH2 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH2", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH2.setLabel ("Sequence 2")
	afecSym_SEQ1R_USCH2.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH3 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH3", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH3.setLabel ("Sequence 3")
	afecSym_SEQ1R_USCH3.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH4 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH4", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH4.setLabel ("Sequence 4")
	afecSym_SEQ1R_USCH4.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH5 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH5", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH5.setLabel ("Sequence 5")
	afecSym_SEQ1R_USCH5.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH6 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH6", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH6.setLabel ("Sequence 6")
	afecSym_SEQ1R_USCH6.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH7 = afecComponent.createComboSymbol("AFEC_SEQ1R_USCH7", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH7.setLabel ("Sequence 7")
	afecSym_SEQ1R_USCH7.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH8 = afecComponent.createComboSymbol("AFEC_SEQ2R_USCH8", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH8.setLabel ("Sequence 8")
	afecSym_SEQ1R_USCH8.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH9 = afecComponent.createComboSymbol("AFEC_SEQ2R_USCH9", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH9.setLabel ("Sequence 9")
	afecSym_SEQ1R_USCH9.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH10 = afecComponent.createComboSymbol("AFEC_SEQ2R_USCH10", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH10.setLabel ("Sequence 10")
	afecSym_SEQ1R_USCH10.setDefaultValue(afecChannelsValues[0])
	
	afecSym_SEQ1R_USCH11 = afecComponent.createComboSymbol("AFEC_SEQ2R_USCH11", afecSym_MR_USEQ, afecChannelsValues)
	afecSym_SEQ1R_USCH11.setLabel ("Sequence 11")
	afecSym_SEQ1R_USCH11.setDefaultValue(afecChannelsValues[0])
	#--------------------------------------------------------------------------------------

	afecCH0Menu = afecComponent.createMenuSymbol("CH0", None)
	afecCH0Menu.setLabel("Channel 0 ")
	
	afecSym_CHER_CH0 = afecComponent.createBooleanSymbol("AFEC_CHER_CH0", afecCH0Menu)
	afecSym_CHER_CH0.setLabel("Enable")
	afecSym_CHER_CH0.setDefaultValue(False)
	
	afecSym_CH0_NAME = afecComponent.createStringSymbol("CH0_NAME", afecSym_CHER_CH0)
	afecSym_CH0_NAME.setLabel ("Name")
	afecSym_CH0_NAME.setDefaultValue("CHANNEL_0")
		
	afecCH0PositiveInput = afecComponent.createStringSymbol("AFEC_CH0_POS_INP", afecSym_CHER_CH0)
	afecCH0PositiveInput.setLabel ("Positive Input")
	afecCH0PositiveInput.setDefaultValue("AN0")
	afecCH0PositiveInput.setReadOnly(True)
	
	afecSym_CH0_NEG_INPValues = ["GND", "AN1"]
	
	afecSym_CH0_NEG_INP = afecComponent.createComboSymbol("AFEC_CH0_NEG_INP", afecSym_CHER_CH0, afecSym_CH0_NEG_INPValues)
	afecSym_CH0_NEG_INP.setLabel ("Negative Input")
	afecSym_CH0_NEG_INP.setDefaultValue("GND")

	afecSym_SHMR_DUAL0 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL0", afecSym_CHER_CH0)
	afecSym_SHMR_DUAL0.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL0.setDefaultValue(False)
	
	afecGainValues = ["X1", "X2", "X4"]
	afecSym_CGR_GAIN0 = afecComponent.createComboSymbol("AFEC_CGR_GAIN0", afecSym_CHER_CH0, afecGainValues)
	afecSym_CGR_GAIN0.setLabel("Gain")
	afecSym_CGR_GAIN0.setDefaultValue("X1")
		
	afecSym_COCR_AOFF0 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF0", afecSym_CHER_CH0)
	afecSym_COCR_AOFF0.setLabel("Offset")
	afecSym_COCR_AOFF0.setDefaultValue(512)

	afecSym_IER_EOC0 = afecComponent.createBooleanSymbol("AFEC_IER_EOC0", afecSym_CHER_CH0)
	afecSym_IER_EOC0.setLabel("End of conversion interrupt")
	afecSym_IER_EOC0.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	
	afecCH1Menu = afecComponent.createMenuSymbol("CH1", None)
	afecCH1Menu.setLabel("Channel 1 ")
	afecCH1Menu.setDependencies(afecCH1MenuVisible, ["AFEC_CH0_NEG_INP"])
	
	afecSym_CHER_CH1 = afecComponent.createBooleanSymbol("AFEC_CHER_CH1", afecCH1Menu)
	afecSym_CHER_CH1.setLabel("Enable")
	afecSym_CHER_CH1.setDefaultValue(False)
	
	afecSym_CH1_NAME = afecComponent.createStringSymbol("CH1_NAME", afecSym_CHER_CH1)
	afecSym_CH1_NAME.setLabel ("Name")
	afecSym_CH1_NAME.setDefaultValue("CHANNEL_1")
		
	afecSym_CH0_POS_INP = afecComponent.createStringSymbol("AFEC_CH1_POS_INP", afecSym_CHER_CH1)
	afecSym_CH0_POS_INP.setLabel ("Positive Input")
	afecSym_CH0_POS_INP.setDefaultValue("AN1")
	afecSym_CH0_POS_INP.setReadOnly(True)
	
	afecSym_SHMR_DUAL1 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL1", afecSym_CHER_CH1)
	afecSym_SHMR_DUAL1.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL1.setDefaultValue(False)
	
	afecSym_CGR_GAIN1 = afecComponent.createComboSymbol("AFEC_CGR_GAIN1", afecSym_CHER_CH1, afecGainValues)
	afecSym_CGR_GAIN1.setLabel("Gain")
	afecSym_CGR_GAIN1.setDefaultValue("X1")
	
	afecSym_COCR_AOFF1 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF1", afecSym_CHER_CH1)
	afecSym_COCR_AOFF1.setLabel("Offset")
	afecSym_COCR_AOFF1.setDefaultValue(512)

	afecSym_IER_EOC1 = afecComponent.createBooleanSymbol("AFEC_IER_EOC1", afecSym_CHER_CH1)
	afecSym_IER_EOC1.setLabel("End of conversion interrupt")
	afecSym_IER_EOC1.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	
	afecCH2Menu = afecComponent.createMenuSymbol("CH2", None)
	afecCH2Menu.setLabel("Channel 2 ")
	
	afecSym_CHER_CH2 = afecComponent.createBooleanSymbol("AFEC_CHER_CH2", afecCH2Menu)
	afecSym_CHER_CH2.setLabel("Enable")
	afecSym_CHER_CH2.setDefaultValue(False)
	
	afecSym_CH2_NAME = afecComponent.createStringSymbol("CH2_NAME", afecSym_CHER_CH2)
	afecSym_CH2_NAME.setLabel ("Name")
	afecSym_CH2_NAME.setDefaultValue("CHANNEL_2")
	
	afecSym_CH2_POS_INP = afecComponent.createStringSymbol("AFEC_CH2_POS_INP", afecSym_CHER_CH2)
	afecSym_CH2_POS_INP.setLabel ("Positive Input")
	afecSym_CH2_POS_INP.setDefaultValue("AN2")
	afecSym_CH2_POS_INP.setReadOnly(True)
	
	afecSym_CH2_NEG_INPValues = ["GND", "AN3"]
	
	afecSym_CH2_NEG_INP = afecComponent.createComboSymbol("AFEC_CH2_NEG_INP", afecSym_CHER_CH2, afecSym_CH2_NEG_INPValues)
	afecSym_CH2_NEG_INP.setLabel ("Negative Input")
	afecSym_CH2_NEG_INP.setDefaultValue("GND")

	afecSym_SHMR_DUAL2 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL2", afecSym_CHER_CH2)
	afecSym_SHMR_DUAL2.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL2.setDefaultValue(False)
	
	afecSym_CGR_GAIN2 = afecComponent.createComboSymbol("AFEC_CGR_GAIN2", afecSym_CHER_CH2, afecGainValues)
	afecSym_CGR_GAIN2.setLabel("Gain")
	afecSym_CGR_GAIN2.setDefaultValue("X1")
	
	afecSym_COCR_AOFF2 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF2", afecSym_CHER_CH2)
	afecSym_COCR_AOFF2.setLabel("Offset")
	afecSym_COCR_AOFF2.setDefaultValue(512)

	afecSym_IER_EOC2 = afecComponent.createBooleanSymbol("AFEC_IER_EOC2", afecSym_CHER_CH2)
	afecSym_IER_EOC2.setLabel("End of conversion interrupt")
	afecSym_IER_EOC2.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	
	afecCH3Menu = afecComponent.createMenuSymbol("CH3", None)
	afecCH3Menu.setLabel("Channel 3 ")
	
	afecSym_CHER_CH3 = afecComponent.createBooleanSymbol("AFEC_CHER_CH3", afecCH3Menu)
	afecSym_CHER_CH3.setLabel("Enable")
	afecSym_CHER_CH3.setDefaultValue(False)
	
	afecSym_CH3_NAME = afecComponent.createStringSymbol("CH3_NAME", afecSym_CHER_CH3)
	afecSym_CH3_NAME.setLabel ("Name")
	afecSym_CH3_NAME.setDefaultValue("CHANNEL_3")
	
	afecSym_CH3_POS_INP = afecComponent.createStringSymbol("AFEC_CH3_POS_INP", afecSym_CHER_CH3)
	afecSym_CH3_POS_INP.setLabel ("Positive Input")
	afecSym_CH3_POS_INP.setDefaultValue("AN3")
	afecSym_CH3_POS_INP.setReadOnly(True)

	afecSym_SHMR_DUAL3 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL3", afecSym_CHER_CH3)
	afecSym_SHMR_DUAL3.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL3.setDefaultValue(False)
	
	afecSym_CGR_GAIN3 = afecComponent.createComboSymbol("AFEC_CGR_GAIN3", afecSym_CHER_CH3, afecGainValues)
	afecSym_CGR_GAIN3.setLabel("Gain")
	afecSym_CGR_GAIN3.setDefaultValue("X1")
	
	afecSym_COCR_AOFF3 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF3", afecSym_CHER_CH3)
	afecSym_COCR_AOFF3.setLabel("Offset")
	afecSym_COCR_AOFF3.setDefaultValue(512)

	afecSym_IER_EOC3 = afecComponent.createBooleanSymbol("AFEC_IER_EOC3", afecSym_CHER_CH3)
	afecSym_IER_EOC3.setLabel("End of conversion interrupt")
	afecSym_IER_EOC3.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH4Menu = afecComponent.createMenuSymbol("CH4", None)
	afecCH4Menu.setLabel("Channel 4 ")
	
	afecSym_CHER_CH4 = afecComponent.createBooleanSymbol("AFEC_CHER_CH4", afecCH4Menu)
	afecSym_CHER_CH4.setLabel("Enable")
	afecSym_CHER_CH4.setDefaultValue(False)
	
	afecSym_CH4_NAME = afecComponent.createStringSymbol("CH4_NAME", afecSym_CHER_CH4)
	afecSym_CH4_NAME.setLabel ("Name")
	afecSym_CH4_NAME.setDefaultValue("CHANNEL_4")
	
	afecSym_CH4_POS_INP = afecComponent.createStringSymbol("AFEC_CH4_POS_INP", afecSym_CHER_CH4)
	afecSym_CH4_POS_INP.setLabel ("Positive Input")
	afecSym_CH4_POS_INP.setDefaultValue("AN4")
	afecSym_CH4_POS_INP.setReadOnly(True)
	
	afecSym_CH4_NEG_INPValues = ["GND", "AN5"]
	
	afecSym_CH4_NEG_INP = afecComponent.createComboSymbol("AFEC_CH4_NEG_INP", afecSym_CHER_CH4, afecSym_CH4_NEG_INPValues)
	afecSym_CH4_NEG_INP.setLabel ("Negative Input")
	afecSym_CH4_NEG_INP.setDefaultValue("GND")

	afecSym_SHMR_DUAL4 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL4", afecSym_CHER_CH4)
	afecSym_SHMR_DUAL4.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL4.setDefaultValue(False)
	
	afecSym_CGR_GAIN4 = afecComponent.createComboSymbol("AFEC_CGR_GAIN4", afecSym_CHER_CH4, afecGainValues)
	afecSym_CGR_GAIN4.setLabel("Gain")
	afecSym_CGR_GAIN4.setDefaultValue("X1")
	
	afecSym_COCR_AOFF4 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF4", afecSym_CHER_CH4)
	afecSym_COCR_AOFF4.setLabel("Offset")
	afecSym_COCR_AOFF4.setDefaultValue(512)

	afecSym_IER_EOC4 = afecComponent.createBooleanSymbol("AFEC_IER_EOC4", afecSym_CHER_CH4)
	afecSym_IER_EOC4.setLabel("End of conversion interrupt")
	afecSym_IER_EOC4.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH5Menu = afecComponent.createMenuSymbol("CH5", None)
	afecCH5Menu.setLabel("Channel 5 ")
	
	afecSym_CHER_CH5 = afecComponent.createBooleanSymbol("AFEC_CHER_CH5", afecCH5Menu)
	afecSym_CHER_CH5.setLabel("Enable")
	afecSym_CHER_CH5.setDefaultValue(False)
	
	afecSym_CH5_NAME = afecComponent.createStringSymbol("CH5_NAME", afecSym_CHER_CH5)
	afecSym_CH5_NAME.setLabel ("Name")
	afecSym_CH5_NAME.setDefaultValue("CHANNEL_5")
	
	afecSym_CH5_POS_INP = afecComponent.createStringSymbol("AFEC_CH5_POS_INP", afecSym_CHER_CH5)
	afecSym_CH5_POS_INP.setLabel ("Positive Input")
	afecSym_CH5_POS_INP.setDefaultValue("AN5")
	afecSym_CH5_POS_INP.setReadOnly(True)

	afecSym_SHMR_DUAL5 = afecComponent.createBooleanSymbol("AFEC_SHMR_DUAL5", afecSym_CHER_CH5)
	afecSym_SHMR_DUAL5.setLabel("Dual Sample and Hold")
	afecSym_SHMR_DUAL5.setDefaultValue(False)
	
	afecSym_CGR_GAIN5 = afecComponent.createComboSymbol("AFEC_CGR_GAIN5", afecSym_CHER_CH5, afecGainValues)
	afecSym_CGR_GAIN5.setLabel("Gain")
	afecSym_CGR_GAIN5.setDefaultValue("X1")
	
	afecSym_COCR_AOFF5 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF5", afecSym_CHER_CH5)
	afecSym_COCR_AOFF5.setLabel("Offset")
	afecSym_COCR_AOFF5.setDefaultValue(512)

	afecSym_IER_EOC5 = afecComponent.createBooleanSymbol("AFEC_IER_EOC5", afecSym_CHER_CH5)
	afecSym_IER_EOC5.setLabel("End of conversion interrupt")
	afecSym_IER_EOC5.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH6Menu = afecComponent.createMenuSymbol("CH6", None)
	afecCH6Menu.setLabel("Channel 6 ")
	
	afecSym_CHER_CH6 = afecComponent.createBooleanSymbol("AFEC_CHER_CH6", afecCH6Menu)
	afecSym_CHER_CH6.setLabel("Enable")
	afecSym_CHER_CH6.setDefaultValue(False)
	
	afecSym_CH6_NAME = afecComponent.createStringSymbol("CH6_NAME", afecSym_CHER_CH6)
	afecSym_CH6_NAME.setLabel ("Name")
	afecSym_CH6_NAME.setDefaultValue("CHANNEL_6")
	
	afecSym_CH6_POS_INP = afecComponent.createStringSymbol("AFEC_CH6_POS_INP", afecSym_CHER_CH6)
	afecSym_CH6_POS_INP.setLabel ("Positive Input")
	afecSym_CH6_POS_INP.setDefaultValue("AN6")
	afecSym_CH6_POS_INP.setReadOnly(True)
	
	afecSym_CH6_NEG_INPValues = ["GND", "AN7"]
	
	afecSym_CH6_NEG_INP = afecComponent.createComboSymbol("AFEC_CH6_NEG_INP", afecSym_CHER_CH6, afecSym_CH6_NEG_INPValues)
	afecSym_CH6_NEG_INP.setLabel ("Negative Input")
	afecSym_CH6_NEG_INP.setDefaultValue("GND")
	
	afecSym_CGR_GAIN6 = afecComponent.createComboSymbol("AFEC_CGR_GAIN6", afecSym_CHER_CH6, afecGainValues)
	afecSym_CGR_GAIN6.setLabel("Gain")
	afecSym_CGR_GAIN6.setDefaultValue("X1")
	
	afecSym_COCR_AOFF6 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF6", afecSym_CHER_CH6)
	afecSym_COCR_AOFF6.setLabel("Offset")
	afecSym_COCR_AOFF6.setDefaultValue(512)

	afecSym_IER_EOC6 = afecComponent.createBooleanSymbol("AFEC_IER_EOC6", afecSym_CHER_CH6)
	afecSym_IER_EOC6.setLabel("End of conversion interrupt")
	afecSym_IER_EOC6.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH7Menu = afecComponent.createMenuSymbol("CH7", None)
	afecCH7Menu.setLabel("Channel 7 ")
	
	afecSym_CHER_CH7 = afecComponent.createBooleanSymbol("AFEC_CHER_CH7", afecCH7Menu)
	afecSym_CHER_CH7.setLabel("Enable")
	afecSym_CHER_CH7.setDefaultValue(False)
	
	afecSym_CH7_NAME = afecComponent.createStringSymbol("CH7_NAME", afecSym_CHER_CH7)
	afecSym_CH7_NAME.setLabel ("Name")
	afecSym_CH7_NAME.setDefaultValue("CHANNEL_7")
	
	afecSym_CH7_POS_INP = afecComponent.createStringSymbol("AFEC_CH7_POS_INP", afecSym_CHER_CH7)
	afecSym_CH7_POS_INP.setLabel ("Positive Input")
	afecSym_CH7_POS_INP.setDefaultValue("AN7")
	afecSym_CH7_POS_INP.setReadOnly(True)
	
	afecSym_CGR_GAIN7 = afecComponent.createComboSymbol("AFEC_CGR_GAIN7", afecSym_CHER_CH7, afecGainValues)
	afecSym_CGR_GAIN7.setLabel("Gain")
	afecSym_CGR_GAIN7.setDefaultValue("X1")
	
	afecSym_COCR_AOFF7 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF7", afecSym_CHER_CH7)
	afecSym_COCR_AOFF7.setLabel("Offset")
	afecSym_COCR_AOFF7.setDefaultValue(512)

	afecSym_IER_EOC7 = afecComponent.createBooleanSymbol("AFEC_IER_EOC7", afecSym_CHER_CH7)
	afecSym_IER_EOC7.setLabel("End of conversion interrupt")
	afecSym_IER_EOC7.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH8Menu = afecComponent.createMenuSymbol("CH8", None)
	afecCH8Menu.setLabel("Channel 8 ")
	
	afecSym_CHER_CH8 = afecComponent.createBooleanSymbol("AFEC_CHER_CH8", afecCH8Menu)
	afecSym_CHER_CH8.setLabel("Enable")
	afecSym_CHER_CH8.setDefaultValue(False)
	
	afecSym_CH8_NAME = afecComponent.createStringSymbol("CH8_NAME", afecSym_CHER_CH8)
	afecSym_CH8_NAME.setLabel ("Name")
	afecSym_CH8_NAME.setDefaultValue("CHANNEL_8")
	
	afecSym_CH8_POS_INP = afecComponent.createStringSymbol("AFEC_CH8_POS_INP", afecSym_CHER_CH8)
	afecSym_CH8_POS_INP.setLabel ("Positive Input")
	afecSym_CH8_POS_INP.setDefaultValue("AN8")
	afecSym_CH8_POS_INP.setReadOnly(True)
	
	afecSym_CH8_NEG_INPValues = ["GND", "AN9"]
	
	afecSym_CH8_NEG_INP = afecComponent.createComboSymbol("AFEC_CH8_NEG_INP", afecSym_CHER_CH8, afecSym_CH8_NEG_INPValues)
	afecSym_CH8_NEG_INP.setLabel ("Negative Input")
	afecSym_CH8_NEG_INP.setDefaultValue("GND")
	
	afecSym_CGR_GAIN8 = afecComponent.createComboSymbol("AFEC_CGR_GAIN8", afecSym_CHER_CH8, afecGainValues)
	afecSym_CGR_GAIN8.setLabel("Gain")
	afecSym_CGR_GAIN8.setDefaultValue("X1")
	
	afecSym_COCR_AOFF8 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF8", afecSym_CHER_CH8)
	afecSym_COCR_AOFF8.setLabel("Offset")
	afecSym_COCR_AOFF8.setDefaultValue(512)

	afecSym_IER_EOC8 = afecComponent.createBooleanSymbol("AFEC_IER_EOC8", afecSym_CHER_CH8)
	afecSym_IER_EOC8.setLabel("End of conversion interrupt")
	afecSym_IER_EOC8.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH9Menu = afecComponent.createMenuSymbol("CH9", None)
	afecCH9Menu.setLabel("Channel 9 ")
	
	afecSym_CHER_CH9 = afecComponent.createBooleanSymbol("AFEC_CHER_CH9", afecCH9Menu)
	afecSym_CHER_CH9.setLabel("Enable")
	afecSym_CHER_CH9.setDefaultValue(False)
	
	afecSym_CH9_NAME = afecComponent.createStringSymbol("CH9_NAME", afecSym_CHER_CH9)
	afecSym_CH9_NAME.setLabel ("Name")
	afecSym_CH9_NAME.setDefaultValue("CHANNEL_9")
	
	afecSym_CH9_POS_INP = afecComponent.createStringSymbol("AFEC_CH9_POS_INP", afecSym_CHER_CH9)
	afecSym_CH9_POS_INP.setLabel ("Positive Input")
	afecSym_CH9_POS_INP.setDefaultValue("AN9")
	afecSym_CH9_POS_INP.setReadOnly(True)
	
	afecSym_CGR_GAIN9 = afecComponent.createComboSymbol("AFEC_CGR_GAIN9", afecSym_CHER_CH9, afecGainValues)
	afecSym_CGR_GAIN9.setLabel("Gain")
	afecSym_CGR_GAIN9.setDefaultValue("X1")
	
	afecSym_COCR_AOFF9 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF9", afecSym_CHER_CH9)
	afecSym_COCR_AOFF9.setLabel("Offset")
	afecSym_COCR_AOFF9.setDefaultValue(512)

	afecSym_IER_EOC9 = afecComponent.createBooleanSymbol("AFEC_IER_EOC9", afecSym_CHER_CH9)
	afecSym_IER_EOC9.setLabel("End of conversion interrupt")
	afecSym_IER_EOC9.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH10Menu = afecComponent.createMenuSymbol("CH10", None)
	afecCH10Menu.setLabel("Channel 10 ")
	
	afecSym_CHER_CH10 = afecComponent.createBooleanSymbol("AFEC_CHER_CH10", afecCH10Menu)
	afecSym_CHER_CH10.setLabel("Enable")
	afecSym_CHER_CH10.setDefaultValue(False)
	
	afecSym_CH10_NAME = afecComponent.createStringSymbol("CH10_NAME", afecSym_CHER_CH10)
	afecSym_CH10_NAME.setLabel ("Name")
	afecSym_CH10_NAME.setDefaultValue("CHANNEL_10")
	
	afecSym_CH10_POS_INP = afecComponent.createStringSymbol("AFEC_CH10_POS_INP", afecSym_CHER_CH10)
	afecSym_CH10_POS_INP.setLabel ("Positive Input")
	afecSym_CH10_POS_INP.setDefaultValue("AN10")
	afecSym_CH10_POS_INP.setReadOnly(True)
	
	afecSym_CH10_NEG_INPValues = ["GND", "AN11"]
	
	afecSym_CH10_NEG_INP = afecComponent.createComboSymbol("AFEC_CH10_NEG_INP", afecSym_CHER_CH10, afecSym_CH10_NEG_INPValues)
	afecSym_CH10_NEG_INP.setLabel ("Negative Input")
	afecSym_CH10_NEG_INP.setDefaultValue("GND")
	
	afecSym_CGR_GAIN10 = afecComponent.createComboSymbol("AFEC_CGR_GAIN10", afecSym_CHER_CH10, afecGainValues)
	afecSym_CGR_GAIN10.setLabel("Gain")
	afecSym_CGR_GAIN10.setDefaultValue("X1")
	
	afecSym_COCR_AOFF10 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF10", afecSym_CHER_CH10)
	afecSym_COCR_AOFF10.setLabel("Offset")
	afecSym_COCR_AOFF10.setDefaultValue(512)

	afecSym_IER_EOC10 = afecComponent.createBooleanSymbol("AFEC_IER_EOC10", afecSym_CHER_CH10)
	afecSym_IER_EOC10.setLabel("End of conversion interrupt")
	afecSym_IER_EOC10.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	afecCH11Menu = afecComponent.createMenuSymbol("CH11", None)
	afecCH11Menu.setLabel("Channel 11 ")
	
	afecSym_CHER_CH11 = afecComponent.createBooleanSymbol("AFEC_CHER_CH11", afecCH11Menu)
	afecSym_CHER_CH11.setLabel("Enable")
	afecSym_CHER_CH11.setDefaultValue(False)
	
	afecSym_CH11_NAME = afecComponent.createStringSymbol("CH11_NAME", afecSym_CHER_CH11)
	afecSym_CH11_NAME.setLabel ("Name")
	afecSym_CH11_NAME.setDefaultValue("CHANNEL_11")
	
	afecSym_CH11_POS_INP = afecComponent.createStringSymbol("AFEC_CH11_POS_INP", afecSym_CHER_CH11)
	afecSym_CH11_POS_INP.setLabel ("Positive Input")
	afecSym_CH11_POS_INP.setDefaultValue("AN11")
	afecSym_CH11_POS_INP.setReadOnly(True)
	
	afecSym_CGR_GAIN11 = afecComponent.createComboSymbol("AFEC_CGR_GAIN11", afecSym_CHER_CH11, afecGainValues)
	afecSym_CGR_GAIN11.setLabel("Gain")
	afecSym_CGR_GAIN11.setDefaultValue("X1")
	
	afecSym_COCR_AOFF11 = afecComponent.createIntegerSymbol("AFEC_COCR_AOFF11", afecSym_CHER_CH11)
	afecSym_COCR_AOFF11.setLabel("Offset")
	afecSym_COCR_AOFF11.setDefaultValue(512)

	afecSym_IER_EOC11 = afecComponent.createBooleanSymbol("AFEC_IER_EOC11", afecSym_CHER_CH11)
	afecSym_IER_EOC11.setLabel("End of conversion interrupt")
	afecSym_IER_EOC11.setDefaultValue(False)
	
	#--------------------------------------------------------------------------------------
	
	
	afecIndex = afecComponent.createIntegerSymbol("INDEX", afecMenu)
	afecIndex.setVisible(False)
	afecIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")

	afecHeaderFile = afecComponent.createFileSymbol(None, None)
	afecHeaderFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/plib_afec.h.ftl")
	afecHeaderFile.setOutputName("plib_afec" + str(num) + ".h")
	afecHeaderFile.setDestPath("peripheral/afec/")
	afecHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
	afecHeaderFile.setType("HEADER")
	
	afecGlobalHeaderFile = afecComponent.createFileSymbol(None, None)
	afecGlobalHeaderFile.setSourcePath("../peripheral/afec_"+afecRegModule.getID() + "/plib_afec.h")
	afecGlobalHeaderFile.setOutputName("plib_afec.h")
	afecGlobalHeaderFile.setDestPath("peripheral/afec/")
	afecGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/afec/")
	afecGlobalHeaderFile.setType("HEADER")
	
	afecSource1File = afecComponent.createFileSymbol(None, None)
	afecSource1File.setSourcePath("../peripheral/afec_"+afecRegModule.getID()+"/templates/plib_afec.c.ftl")
	afecSource1File.setOutputName("plib_afec" + str(num) + ".c")
	afecSource1File.setDestPath("peripheral/afec/")
	afecSource1File.setProjectPath("config/" + configName +"/peripheral/afec/")
	afecSource1File.setType("SOURCE")
	

