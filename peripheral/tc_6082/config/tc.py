###################################################################################################
########################### Global Variables   #################################
###################################################################################################
global num
global extClock

tcChannelMenu = []
tcSym_CH_Enable = []
tcSym_CH_CMR_TCCLKS = [0,0,0,0]
tcSym_CH_EXT_CLOCK = [0,0,0,0]
tcSym_CH_CLOCK_FREQ = [0,0,0,0]
tcSym_CH_PCK7 = [0,0,0,0]
tcSym_CH_Resolution = [0,0,0,0]
tcSym_CH_OperatingMode = []

tcTimerMenu = []
tcSym_CH_TimerPeriodCount = []
tcSym_CH_TimerPeriod = []
tcSym_CH_CMR_CPCSTOP = []
tcSym_CH_IER_CPCS = []

tcCaptureMenu = []
tcSym_CH_CMR_LDRA = []
tcSym_CH_CMR_LDRB = []
tcSym_CH_CAPTURE_EXT_RESET = []
tcSym_CH_CMR_ETRGEDG = []
tcSym_CH_CMR_ETRGEDG_COMMENT = []
tcSym_CH_CMR_ETRGEDG_ALERT = []
tcSym_CH_CAPTURE_IER_LDRAS = []
tcSym_CH_CAPTURE_IER_LDRBS = []
tcSym_CH_CAPTURE_IER_COVFS = []
tcSym_CH_CMR_ABETRG = []
tcSym_CH_CAPTURE_CMR_LDBSTOP = []

tcCompareMenu = []
tcSym_CH_CMR_WAVSEL = []
tcSym_CH_ComparePeriodCount = []
tcSym_CH_ComparePeriod = []
tcEventMenu = []
tcCompareAMenu = []
tcSym_CH_CompareA = []
tcSym_CH_CMR_ACPA = []
tcSym_CH_CMR_ACPC = []
tcSym_CH_CMR_AEEVT = []
tcCompareBMenu = []
tcSym_CH_CompareB = []
tcSym_CH_CMR_BCPB = []
tcSym_CH_CMR_BCPC = []
tcSym_CH_CMR_BEEVT = []
tcSym_CH_CMR_EEVT = []
tcSym_CH_CMP_CMR_ETRGEDG = []
tcSym_CH_COMPARE_IER_CPCS = []
tcSym_CH_COMPARE_CMR_CPCSTOP = []

tcSym_CH_ClockControl = []
tcSym_CH_NVICControl = []
tcSym_CH_IntEnComment = []
tcSym_CH_ClkEnComment = []

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################
#channel number is extracted as 2nd character in ID. like TC0_xxx, TC1_xxx, TC2_xxx

#Enable/Disable peripheral clock 
def tcClockControl(symbol, event):
	id = symbol.getID()
	channelID = int(id[2])
	if(tcSym_CH_EnableQEI.getValue() == True):
		Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL0")
		Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL0" , True, 2)
		Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL1")
		Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL1" , True, 2)
		if(tcSym_CH_BMR_POSEN.getValue() == "SPEED"):
			Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2")
			Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2" , True, 2)
		else:
			if(tcSym_CH_Enable[2].getValue() == True):
				Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2")
				Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2" , True, 2)	
			else:
				Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2")
				Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2" , False, 2)					
	else:
		if(tcSym_CH_Enable[channelID].getValue() == True):
			Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID))
			Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID) , True, 2)
		else:
			Database.clearSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID))
			Database.setSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID) , False, 2)			

#Enable/Disable interrupt
def tcNVICControl(symbol, event):
	id = symbol.getID()
	channelID = int(id[2])
	periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH" + str(channelID))
	NVICVector = "NVIC_" + str(periphId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(periphId) + "_HANDLER"

	if(tcSym_CH_EnableQEI.getValue() == True):
		periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH0")
		NVICVector = "NVIC_" + str(periphId) + "_ENABLE"
		NVICHandler = "NVIC_" + str(periphId) + "_HANDLER"
		Database.clearSymbolValue("core", NVICVector)
		Database.clearSymbolValue("core", NVICHandler)
		if(tcSym_CH_QIER_IDX.getValue() == True or tcSym_CH_QIER_QERR.getValue() == True):
			Database.setSymbolValue("core", NVICVector, True, 2)
			Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH0_InterruptHandler", 2)
		else:
			Database.setSymbolValue("core", NVICVector, False, 2)
			Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH0_Handler", 2)
	else:
		Database.clearSymbolValue("core", NVICVector)
		Database.clearSymbolValue("core", NVICHandler)
		if(tcSym_CH_Enable[channelID].getValue() == True):
			if(tcSym_CH_OperatingMode[channelID].getValue() == "TIMER"):
				Database.setSymbolValue("core", NVICVector, True, 2)
				Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH"+str(channelID)+"_InterruptHandler", 2)
			elif(tcSym_CH_OperatingMode[channelID].getValue() == "CAPTURE" and \
				(tcSym_CH_CAPTURE_IER_LDRAS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_LDRBS[channelID].getValue() == True or tcSym_CH_CAPTURE_IER_COVFS[channelID].getValue() == True)):
				Database.setSymbolValue("core", NVICVector, True, 2)
				Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH"+str(channelID)+"_InterruptHandler", 2)			
			elif(tcSym_CH_OperatingMode[channelID].getValue() == "COMPARE" and tcSym_CH_COMPARE_IER_CPCS[channelID].getValue() == True):
				Database.setSymbolValue("core", NVICVector, True, 2)
				Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH"+str(channelID)+"_InterruptHandler", 2)	
			else:
				Database.setSymbolValue("core", NVICVector, False, 2)
				Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH"+str(channelID)+"_Handler", 2)	
		else:
			Database.setSymbolValue("core", NVICVector, False, 2)
			Database.setSymbolValue("core", NVICHandler, "TC" + str(num) + "_CH"+str(channelID)+"_Handler", 2)	

def dependencyClockStatus(symbol, event):
	id = symbol.getID()
	channelID = int(id[2])
	clock = bool(Database.getSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID)))
	global tcSym_CH_Enable
	if (clock == False and tcSym_CH_Enable[channelID].getValue() == True):
		tcSym_CH_ClkEnComment[channelID].setVisible(True)
	else:
		tcSym_CH_ClkEnComment[channelID].setVisible(False)
		
def dependencyIntStatus(symbol, event):
	id = symbol.getID()
	channelID = int(id[2])
	global tcSym_CH_Enable
	periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH"+str(channelID))
	NVICVector = "NVIC_" + str(periphId) + "_ENABLE"
	nvic = bool(Database.getSymbolValue("core", NVICVector))
	if (tcSym_CH_Enable[channelID].getValue() == True):
		if (nvic == False):
			tcSym_CH_IntEnComment[channelID].setVisible(True)
		else:
			tcSym_CH_IntEnComment[channelID].setVisible(False)
	else:
		tcSym_CH_IntEnComment[channelID].setVisible(False)		

def tcQEIDependencyClockStatus(symbol, event):
	clock0 = bool(Database.getSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL0"))
	clock1 = bool(Database.getSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL1"))
	clock2 = bool(Database.getSymbolValue("core", "PMC_ID_TC" + str(num) + "_CHANNEL2"))
	if(tcSym_CH_EnableQEI.getValue() == True):
		if(tcSym_CH_BMR_POSEN.getValue() == "POSITION"):
			if (clock0 == False or clock1 == False):
				symbol.setVisible(True)
			else:
				symbol.setVisible(False)
		else:
			if (clock0 == False or clock1 == False or clock2 == False):
				symbol.setVisible(True)
			else:
				symbol.setVisible(False)	

def tcQEIDependencyIntStatus(symbol, event):
	periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH0")
	NVICVector = "NVIC_" + str(periphId) + "_ENABLE"
	nvic = bool(Database.getSymbolValue("core", NVICVector))
	if(tcSym_CH_EnableQEI.getValue() == True):
		if (nvic == False and (tcSym_CH_QIER_IDX.getValue() == True or tcSym_CH_QIER_QERR.getValue() == True)):
			symbol.setVisible(True)
		else:
			symbol.setVisible(False)
			
	
def tcGetMasterClock_Hz():
	main_clk_freq = int(Database.getSymbolValue("core","MASTERCLK_FREQ"))
	return main_clk_freq

def tcGetSlowClock_Hz():
	slow_clk_freq = int(Database.getSymbolValue("core","CLK_SLOW_XTAL"))
	return slow_clk_freq
	
def tcGetPCK6Clock_Hz():
	pck6_clk_freq = int(Database.getSymbolValue("core","PCK6_FREQ"))
	return pck6_clk_freq
	
def tcGetPCK7Clock_Hz():
	pck7_clk_freq = int(Database.getSymbolValue("core","PCK7_FREQ"))
	return pck7_clk_freq
	
def tcGetClockResolution(clockSource, channelID):
	resolution_nS = 0.00
	master_clock_Hz = (tcGetMasterClock_Hz())
	slow_clock_Hz = tcGetSlowClock_Hz()
	pck6_clock_Hz = (tcGetPCK6Clock_Hz())
	pck7_clock_Hz = tcGetPCK7Clock_Hz()
	global tcSym_CH_EXT_CLOCK
	if (clockSource == "MCK"):
		resolution_nS = str(1000000000.0/master_clock_Hz)
	if (clockSource == "PCK6"):
		resolution_nS = str(1000000000.0/pck6_clock_Hz)
	if (clockSource == "PCK7"):
		resolution_nS = str(1000000000.0/pck7_clock_Hz)
	if (clockSource == "MCK/8"):
		resolution_nS =  str(8000000000.0/master_clock_Hz)
	if (clockSource == "MCK/32"):
		resolution_nS =  str(32000000000.0/master_clock_Hz)
	if (clockSource == "MCK/128"):
		resolution_nS =  str(128000000000.0/master_clock_Hz)
	if (clockSource == "SLCK"):
		resolution_nS =  str(1000000000.0/slow_clock_Hz)
	if (clockSource == "XC0"):
		resolution_nS =  str(1000000000.0/tcSym_CH_EXT_CLOCK[channelID].getValue())
	if (clockSource == "XC1"):
		resolution_nS =  str(1000000000.0/tcSym_CH_EXT_CLOCK[channelID].getValue())
	if (clockSource == "XC2"):
		resolution_nS =  str(1000000000.0/tcSym_CH_EXT_CLOCK[channelID].getValue())
	return resolution_nS

def tcClockFreq	(tcSym_CH_ClockFreqLocal, event):
	id = tcSym_CH_ClockFreqLocal.getID()
	channelID = int(id[2])
	clock_Hz = 0
	master_clock_Hz = tcGetMasterClock_Hz()
	slow_clock_Hz = tcGetSlowClock_Hz()
	pck6_clock_Hz = tcGetPCK6Clock_Hz()
	pck7_clock_Hz = tcGetPCK7Clock_Hz()
	global tcSym_CH_EXT_CLOCK
	clock = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))
	if (clock == "MCK"):
		clock_Hz = (master_clock_Hz)
	if (clock == "PCK6"):
		clock_Hz = (pck6_clock_Hz)
	if (clock == "PCK7"):
		clock_Hz = (pck7_clock_Hz)	
	if (clock == "MCK/8"):
		clock_Hz =  (master_clock_Hz/8)
	if (clock == "MCK/32"):
		clock_Hz =  (master_clock_Hz/32)
	if (clock == "MCK/128"):
		clock_Hz =  (master_clock_Hz/128)
	if (clock == "SLCK"):
		clock_Hz =  (slow_clock_Hz)
	if (clock == "XC0"):
		clock_Hz =  (tcSym_CH_EXT_CLOCK[channelID].getValue())
	if (clock == "XC1"):
		clock_Hz =  (tcSym_CH_EXT_CLOCK[channelID].getValue())
	if (clock == "XC2"):
		clock_Hz =  (tcSym_CH_EXT_CLOCK[channelID].getValue())
	tcSym_CH_CLOCK_FREQ[channelID].setValue(int(clock_Hz), 1)
	
def tcClockResCalc(tcSym_CH_ResolutionLocal, event):
	id = tcSym_CH_ResolutionLocal.getID()
	channelID = int(id[2])
	resolution = None
	clock = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))
	resolution = tcGetClockResolution(clock, channelID)
	tcSym_CH_Resolution[channelID].setLabel("****Clock resolution is " + str(resolution) + " nS****")

def tcExtClockVisible(tcSym_CH_Ext_ClockLocal, event):
	id = tcSym_CH_Ext_ClockLocal.getID()
	channelID = int(id[2])
	source = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))	
	if(source == "XC0" or source == "XC1" or source == "XC2"):
		tcSym_CH_EXT_CLOCK[channelID].setVisible(True)
	else:
		tcSym_CH_EXT_CLOCK[channelID].setVisible(False)
		
def tcPCK7Set(tcSym_CH_PCK7Local, event):
	id = tcSym_CH_PCK7Local.getID()
	channelID = int(id[2])
	source = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))	
	Database.clearSymbolValue("core", "PMC_SCER_PCK7")
	Database.clearSymbolValue("core", "PMC_SCER_PCK6")
	if (source == "PCK7"):
		tcSym_CH_PCK7[channelID].clearValue()
		tcSym_CH_PCK7[channelID].setValue(True, 1)
		Database.setSymbolValue("core", "PMC_SCER_PCK7", True, 2)
	elif (source == "PCK6"):
		tcSym_CH_PCK7[channelID].clearValue()
		tcSym_CH_PCK7[channelID].setValue(False, 1)
		Database.setSymbolValue("core", "PMC_SCER_PCK6", True, 2)
	else:
		tcSym_CH_PCK7[channelID].clearValue()
		tcSym_CH_PCK7[channelID].setValue(False, 1)	

def tcTimerVisible(tcTimerMenuLocal, event):
	id = tcTimerMenuLocal.getID()
	channelID = int(id[2])
	if(event["value"] == "TIMER"):
		tcTimerMenu[channelID].setVisible(True)
	else:
		tcTimerMenu[channelID].setVisible(False)

def tcCaptureVisible(tcCaptureMenuLocal, event):
	id = tcCaptureMenuLocal.getID()
	channelID = int(id[2])
	if(event["value"] == "CAPTURE"):
		tcCaptureMenu[channelID].setVisible(True)
	else:
		tcCaptureMenu[channelID].setVisible(False)

#Business logic to restrict the external reset edge
#if external reset signal is TIOA then load A edge and external reset edge should NOT be same.		
def tcCaptureEdgeSelect(tcSym_CH_CMR_ETRGEDGLocal, event):
	global tcSym_CH_CMR_LDRA
	global tcSym_CH_CAPTURE_EXT_RESET
	global tcSym_CH_CMR_ABETRG
	global tcSym_CH_CMR_ETRGEDG
	id = tcSym_CH_CMR_ETRGEDGLocal.getID()
	channelID = int(id[2])
	edgeA = tcSym_CH_CMR_LDRA[channelID].getValue()
	extReset = tcSym_CH_CAPTURE_EXT_RESET[channelID].getValue()
	extResetInput = tcSym_CH_CMR_ABETRG[channelID].getValue()
	extResetEdge = tcSym_CH_CMR_ETRGEDG[channelID].getValue()
	if ((extReset == True) and (extResetInput == "TIOA")):
		if (((edgeA == "RISING") and (extResetEdge == "RISING")) or ((edgeA == "FALLING") and (extResetEdge == "FALLING"))):
			tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(True)
		else:
			tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)
	else:
		tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)
			
def tcCompareVisible(tcCompareMenuLocal, event):
	id = tcCompareMenuLocal.getID()
	channelID = int(id[2])
	if(event["value"] == "COMPARE"):
		tcCompareMenu[channelID].setVisible(True)
	else:
		tcCompareMenu[channelID].setVisible(False)
		
def tcPeriodCalc(tcSym_CH_ComparePeriodLocal, event):
	global tcSym_CH_CMR_TCCLKS
	global tcSym_CH_TimerPeriodCount
	global tcSym_CH_ComparePeriodCount
	global tcSym_CH_OperatingMode
	
	id = tcSym_CH_ComparePeriodLocal.getID()
	channelID = int(id[2])
	clock = tcSym_CH_CMR_TCCLKS[channelID].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[channelID].getSelectedValue()))	
	mode = tcSym_CH_OperatingMode[channelID].getValue()
	if (mode == "TIMER"):
		count = tcSym_CH_TimerPeriodCount[channelID].getValue()
	if(mode == "COMPARE"):
		count = tcSym_CH_ComparePeriodCount[channelID].getValue()
	
	resolution_ns = tcGetClockResolution(clock, channelID)
	time_us = float(resolution_ns) * int(count) / 1000.0;

	if(mode == "COMPARE"):
		tcSym_CH_ComparePeriod[channelID].setLabel("****Waveform period is " + str(time_us) + " uS****")
	if (mode == "TIMER"):
		tcSym_CH_TimerPeriod[channelID].setLabel("****Time interval is " + str(time_us) + " uS****")
		
def tcCompareMaxCalc(tcCompare, event):
	id = tcCompare.getID()
	channelID = int(id[2])	
	tcCompare.setMax(event["value"])
	
def tcWaveformBVisible(tcWaveformB, event):
	id = tcWaveformB.getID()
	channelID = int(id[2])
	symObj = event["symbol"]
	input = symObj.getSelectedKey()
	if (input == "TIOB"):
		tcCompareBMenu[channelID].setVisible(False)
	else:
		tcCompareBMenu[channelID].setVisible(True)

def tcActionExtEvtVisible(actionExtEvt, event):	
	id = actionExtEvt.getID()
	channelID = int(id[2])
	
	if (event["value"] != "NONE"):
		if(actionExtEvt.getID().find("AEEVT") > 0):
			tcSym_CH_CMR_AEEVT[channelID].setVisible(True)
		else:
			tcSym_CH_CMR_BEEVT[channelID].setVisible(True)
	else:
		if(actionExtEvt.getID().find("AEEVT") > 0):
			tcSym_CH_CMR_AEEVT[channelID].setVisible(False)
		else:
			tcSym_CH_CMR_BEEVT[channelID].setVisible(False)	
			
def tcQuadratureVisible(tcQuadratureMenu, event):
	if(event["value"] == True):
		tcQuadratureMenu.setVisible(True)
	else:
		tcQuadratureMenu.setVisible(False)
		
def tcChannelMenuVisible(tcchannelMenu, event):
	global tcSym_CH_BMR_POSEN
	global tcSym_CH_EnableQEI
	if(tcSym_CH_EnableQEI.getValue() == True):
		tcChannelMenu[0].setVisible(False)
		tcChannelMenu[1].setVisible(False)
		if (tcSym_CH_BMR_POSEN.getValue() == "SPEED"):
			tcChannelMenu[2].setVisible(False)
		else:
			tcChannelMenu[2].setVisible(True)
	else:
		tcChannelMenu[0].setVisible(True)
		tcChannelMenu[1].setVisible(True)
		tcChannelMenu[2].setVisible(True)
		
def tcQuadratureSpeedVisible(tcSpeedMenu, event):
	if(event["value"] == "SPEED"):
		tcSpeedMenu.setVisible(True)
	else:
		tcSpeedMenu.setVisible(False)
		
def tcQuadratureTimeBaseCalculate(tcSym_CH_QEI_CH2PERIOD_COMMENT, event):
	global tcSym_CH_CMR_TCCLKS
	global tcSym_CH_QEI_CH2PERIOD
	channelID = 3
	clock = tcSym_CH_CMR_TCCLKS[3].getKeyDescription(int(tcSym_CH_CMR_TCCLKS[3].getSelectedValue()))	
	count = tcSym_CH_QEI_CH2PERIOD.getValue()
	
	resolution_ns = tcGetClockResolution(clock, 3)
	time_us = float(resolution_ns) * int(count) / 1000.0;

	tcSym_CH_QEI_CH2PERIOD_COMMENT.setLabel("****Time Base is " + str(time_us) + " uS****")
	
def tcQuadratureCommentChange(tcQuadratureComment, event):
	if(event["value"] == "POSITION"):
		tcQuadratureComment.setLabel("**** Quadrature mode uses two channels. Channel 0 to capture number of edges and Channel 1 to capture number of revolutions ****")
	else:
		tcQuadratureComment.setLabel("**** Quadrature mode uses three channels. Channel 0 and Channel 2 to capture speed and Channel 1 to capture number of revolutions ****")

def tcClockSymbols(tcComponent, channelID, menu):		
	#clock selection
	#Added keys here as this symbol combines two bit-fields CMR_TCCLKS and EMR_NODIVCLK
	global tcSym_CH_CMR_TCCLKS
	i = 0 #value of the key. As keys are added conditionally, incrementing value with variable i
	tcSym_CH_CMR_TCCLKS[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_TCCLKS", menu)
	tcSym_CH_CMR_TCCLKS[channelID].setLabel("Select Clock Source")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("", str(i), "MCK")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK1", str(i + 1), "PCK6")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK2", str(i + 2), "MCK/8")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK3", str(i + 3), "MCK/32")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK4", str(i + 4), "MCK/128")
	tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK5", str(i + 5), "SLCK")
	i = i + 5	
	if(extClock[0] == True):
		tcSym_CH_CMR_TCCLKS[channelID].addKey("XC0", str(i + 1), "XC0")
		i = i + 1
	if(extClock[1] == True):
		tcSym_CH_CMR_TCCLKS[channelID].addKey("XC1", str(i + 1), "XC1")
		i = i + 1
	if(extClock[2] == True):		
		tcSym_CH_CMR_TCCLKS[channelID].addKey("XC2", str(i + 1), "XC2")	
		i = i + 1 
	if(int(num) == 0):
		tcSym_CH_CMR_TCCLKS[channelID].addKey("TIMER_CLOCK1", str(i + 1), "PCK7")		
	tcSym_CH_CMR_TCCLKS[channelID].setDefaultValue(0)
	tcSym_CH_CMR_TCCLKS[channelID].setOutputMode("Key")
	tcSym_CH_CMR_TCCLKS[channelID].setDisplayMode("Description")
	
	#PCK7 and also enable clock PCK6 or PCK7
	tcSym_CH_PCK7[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_PCK7", menu)
	tcSym_CH_PCK7[channelID].setLabel("PCK7")
	tcSym_CH_PCK7[channelID].setVisible(False)
	tcSym_CH_PCK7[channelID].setDefaultValue(False)
	tcSym_CH_PCK7[channelID].setDependencies(tcPCK7Set, ["TC"+str(channelID)+"_CMR_TCCLKS"])
	
	#external clock frequency
	global tcSym_CH_EXT_CLOCK
	tcSym_CH_EXT_CLOCK[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_EXT_CLOCK", menu)
	tcSym_CH_EXT_CLOCK[channelID].setLabel("External Clock Frequency (Hz)")
	tcSym_CH_EXT_CLOCK[channelID].setVisible(False)
	tcSym_CH_EXT_CLOCK[channelID].setDefaultValue(50000000)
	tcSym_CH_EXT_CLOCK[channelID].setDependencies(tcExtClockVisible, ["TC"+str(channelID)+"_CMR_TCCLKS"])
	
	#Save clock frequency
	tcSym_CH_CLOCK_FREQ[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_CLOCK_FREQ", menu)
	tcSym_CH_CLOCK_FREQ[channelID].setLabel("Clock Frequency (Hz)")
	tcSym_CH_CLOCK_FREQ[channelID].setVisible(False)
	tcSym_CH_CLOCK_FREQ[channelID].setDefaultValue(150000000)
	tcSym_CH_CLOCK_FREQ[channelID].setDependencies(tcClockFreq, ["TC"+str(channelID)+"_CMR_TCCLKS"])
	
	#clock resolution display
	tcSym_CH_Resolution[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_Resolution", menu)
	tcSym_CH_Resolution[channelID].setLabel("****Timer resolution is " + str(6.66) + " nS****")
	tcSym_CH_Resolution[channelID].setDependencies(tcClockResCalc, ["TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
		"core.MASTERCLK_FREQ", "core.CLK_SLOW_XTAL", "core.PCK6_FREQ", "core.PCK7_FREQ"])	
		

###################################################################################################
########################### Instantiation   #################################
###################################################################################################	
def instantiateComponent(tcComponent):
	global num
	num = tcComponent.getID()[-1:]
	print("Running TC" + str(num))
	
	#*********** Restrict the channel mode as per ATDF file **************************
	packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
	availablePins = []		# array to save available pins
	channel = [False, False, False] #array to save available channels
	global extClock
	extClock = [False, False, False] #array to save if ext clock pin is available
	
	# Save pins in availablePins array as per selected package 
	children = []
	val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(packageName)+"\"]")
	children = val.getChildren()
	for pad in range (0, len(children)):
		availablePins.append(children[pad].getAttribute("pad"))
	
	#Find available channels and available external clock pins
	tc_signals = []
	tc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\"TC"+str(num)+"\"]/signals")
	tc_signals = tc.getChildren()
	for pad in range (0 , len(tc_signals)):
		if "TIOA" in tc_signals[pad].getAttribute("group"):
			padSignal = tc_signals[pad].getAttribute("pad")
			if padSignal in availablePins :
				channel[int(tc_signals[pad].getAttribute("index"))%3] = True
			else:
				channel[int(tc_signals[pad].getAttribute("index"))%3] = False
		if "TCLK" in tc_signals[pad].getAttribute("group"):
			padSignal = tc_signals[pad].getAttribute("pad")
			if padSignal in availablePins :
				extClock[int(tc_signals[pad].getAttribute("index"))%3] = True
			else:
				extClock[int(tc_signals[pad].getAttribute("index"))%3] = False
	
	#*****************************QUADRATURE******************************	
	#channel enable
	global tcSym_CH_EnableQEI
	tcSym_CH_EnableQEI = tcComponent.createBooleanSymbol("TC_ENABLE_QEI", None)
	tcSym_CH_EnableQEI.setLabel("Enable Quadrature Encoder Mode")
	tcSym_CH_EnableQEI.setDefaultValue(False)
	#Quadrature interface is not available if channel 0 and channel 1 pins are not available
	if (channel[0] == True and channel[1] == True):
		tcSym_CH_EnableQEI.setVisible(True)
	else:
		tcSym_CH_EnableQEI.setVisible(False)
		
	# Dependency Status
	tcSym_QEI_ClkEnComment = tcComponent.createCommentSymbol("TC_CLK_ENABLE_COMMENT", tcSym_CH_EnableQEI)
	tcSym_QEI_ClkEnComment.setVisible(False)
	tcSym_QEI_ClkEnComment.setLabel("Warning!!! TC" +str(num) + " Channel Peripheral Clock is Disabled in Clock Manager")
	tcSym_QEI_ClkEnComment.setDependencies(tcQEIDependencyClockStatus, ["core.PMC_ID_TC" + str(num) + "_CHANNEL0", \
		"core.PMC_ID_TC" + str(num) + "_CHANNEL1", "core.PMC_ID_TC" + str(num) + "_CHANNEL2", "TC_ENABLE_QEI", "TC_BMR_POSEN"])
	
	periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH0")
	NVICVector = "NVIC_" + str(periphId) + "_ENABLE"
	tcSym_QEI_IntEnComment = tcComponent.createCommentSymbol("TC_NVIC_ENABLE_COMMENT", tcSym_CH_EnableQEI)
	tcSym_QEI_IntEnComment.setVisible(False)
	tcSym_QEI_IntEnComment.setLabel("Warning!!! TC" +str(num)+"_CH0 Interrupt is Disabled in Interrupt Manager")
	tcSym_QEI_IntEnComment.setDependencies(tcQEIDependencyIntStatus, ["core." + NVICVector, "TC_ENABLE_QEI", "TC_QIER_IDX", "TC_QIER_QERR"])

	#quadrature menu
	tcQuadratureMenu = tcComponent.createMenuSymbol("TC_QUADRATURE", tcSym_CH_EnableQEI)
	tcQuadratureMenu.setLabel("Quadrature")
	tcQuadratureMenu.setVisible(False)
	tcQuadratureMenu.setDependencies(tcQuadratureVisible, ["TC_ENABLE_QEI"])
	
	tcQuadratureComment = tcComponent.createCommentSymbol("TC_QUADRATURE_COMMENT", tcQuadratureMenu)
	tcQuadratureComment.setLabel("**** Quadrature mode uses two channels. Channel 0 to capture number of edges and Channel 1 to capture number of revolutions ****")
	tcQuadratureComment.setDependencies(tcQuadratureCommentChange, ["TC_BMR_POSEN"])
	
	# Swap PhA and PhB
	tcSym_CH_QEI_BMR_SWAP = tcComponent.createBooleanSymbol("TC_BMR_SWAP", tcQuadratureMenu)
	tcSym_CH_QEI_BMR_SWAP.setLabel("Swap Phase A and Phase B Signals")
	tcSym_CH_QEI_BMR_SWAP.setDefaultValue(False)
	
	# Filter value
	tcSym_CH_BMR_MAXFILT = tcComponent.createIntegerSymbol("TC_BMR_MAXFILT", tcQuadratureMenu)
	tcSym_CH_BMR_MAXFILT.setLabel("Select Input Signal Filter Count")
	tcSym_CH_BMR_MAXFILT.setDefaultValue(2)	
	tcSym_CH_BMR_MAXFILT.setMin(0)
	tcSym_CH_BMR_MAXFILT.setMax(63)
	
	#Mode
	global tcSym_CH_BMR_POSEN
	tcSym_CH_BMR_POSEN = tcComponent.createComboSymbol("TC_BMR_POSEN", tcQuadratureMenu, ["POSITION", "SPEED"])
	tcSym_CH_BMR_POSEN.setLabel("Select Mode")
	tcSym_CH_BMR_POSEN.setDefaultValue("POSITION")
	
	#speed menu
	tcSpeedMenu = tcComponent.createMenuSymbol("TC_QUADRATURE_SPEED", tcSym_CH_BMR_POSEN)
	tcSpeedMenu.setLabel("Speed Measurement")
	tcSpeedMenu.setVisible(False)
	tcSpeedMenu.setDependencies(tcQuadratureSpeedVisible, ["TC_BMR_POSEN"])	

	# clock selection for channel 2. For quadrature mode, channel ID 3 is used to distinguish between channel numbers and quadrature mode
	tcClockSymbols(tcComponent, 3, tcSpeedMenu)
	
	# CH2 time period
	global tcSym_CH_QEI_CH2PERIOD
	tcSym_CH_QEI_CH2PERIOD = tcComponent.createIntegerSymbol("TC_QEI_PERIOD", tcSpeedMenu)
	tcSym_CH_QEI_CH2PERIOD.setLabel("Select Speed Time Base")
	tcSym_CH_QEI_CH2PERIOD.setDefaultValue(15015)
	
	# CH2 time in us comment
	tcSym_CH_QEI_CH2PERIOD_COMMENT = tcComponent.createCommentSymbol("TC_QEI_PERIOD_COMMENT", tcSpeedMenu)
	tcSym_CH_QEI_CH2PERIOD_COMMENT.setLabel("**** Time Base is 100 uS  ****")
	tcSym_CH_QEI_CH2PERIOD_COMMENT.setDependencies(tcQuadratureTimeBaseCalculate, ["TC_QEI_PERIOD", "TC3_CMR_TCCLKS", \
		"core.MASTERCLK_FREQ", "core.CLK_SLOW_XTAL", "core.PCK6_FREQ", "core.PCK7_FREQ"])

	# enable index interrupt
	global tcSym_CH_QIER_IDX
	tcSym_CH_QIER_IDX = tcComponent.createBooleanSymbol("TC_QIER_IDX", tcQuadratureMenu)
	tcSym_CH_QIER_IDX.setLabel("Enable Index Interrupt")
	tcSym_CH_QIER_IDX.setDefaultValue(False)
	
	# enable quadrature error interrupt
	global tcSym_CH_QIER_QERR
	tcSym_CH_QIER_QERR = tcComponent.createBooleanSymbol("TC_QIER_QERR", tcQuadratureMenu)
	tcSym_CH_QIER_QERR.setLabel("Enable Quadrature Error Interrupt")
	tcSym_CH_QIER_QERR.setDefaultValue(False)	
	
	#*************************CHANNEL CONFIGURATIONS ******************************
	for channelID in range(0, 3):
		#channel menu
		tcChannelMenu.append(channelID)
		tcChannelMenu[channelID] = tcComponent.createMenuSymbol("Channel "+str(channelID), None)
		tcChannelMenu[channelID].setLabel("Channel "+str(channelID))
		tcChannelMenu[channelID].setDependencies(tcChannelMenuVisible, ["TC_ENABLE_QEI", "TC_BMR_POSEN"])
		
		#channel enable
		tcSym_CH_Enable.append(channelID)
		tcSym_CH_Enable[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_ENABLE", tcChannelMenu[channelID])
		tcSym_CH_Enable[channelID].setLabel("Enable")
		tcSym_CH_Enable[channelID].setDefaultValue(False)
		
		############################################################################
		#### Dependency ####
		############################################################################
		# Clock dynamic settings
		tcSym_CH_ClockControl.append(channelID)
		tcSym_CH_ClockControl[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CLOCK_ENABLE", None)
		tcSym_CH_ClockControl[channelID].setDependencies(tcClockControl, ["TC"+str(channelID)+"_ENABLE", "TC_ENABLE_QEI", "TC_BMR_POSEN"])
		tcSym_CH_ClockControl[channelID].setVisible(False)		
		
		# NVIC Dynamic settings
		tcSym_CH_NVICControl.append(channelID)
		tcSym_CH_NVICControl[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_NVIC_ENABLE", None)
		tcSym_CH_NVICControl[channelID].setDependencies(tcNVICControl, ["TC"+str(channelID)+"_ENABLE", "TC_ENABLE_QEI", "TC"+str(channelID)+"_OPERATING_MODE", \
			"TC"+str(channelID)+"_CAPTURE_IER_LDRAS", "TC"+str(channelID)+"_CAPTURE_IER_LDRBS", "TC"+str(channelID)+"_CAPTURE_IER_COVFS", \
			"TC"+str(channelID)+"_COMPARE_IER_CPCS", "TC_QIER_IDX", "TC_QIER_QERR"])
		tcSym_CH_NVICControl[channelID].setVisible(False)
		
		# Dependency Status
		tcSym_CH_ClkEnComment.append(channelID)
		tcSym_CH_ClkEnComment[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CLK_ENABLE_COMMENT", tcChannelMenu[channelID])
		tcSym_CH_ClkEnComment[channelID].setVisible(False)
		tcSym_CH_ClkEnComment[channelID].setLabel("Warning!!! TC" +str(num)+"_CH"+str(channelID)+" Peripheral Clock is Disabled in Clock Manager")
		tcSym_CH_ClkEnComment[channelID].setDependencies(dependencyClockStatus, ["core.PMC_ID_TC" + str(num) + "_CHANNEL"+str(channelID), "TC"+str(channelID)+"_ENABLE"])
		
		periphId = Interrupt.getInterruptIndex("TC" + str(num)+ "_CH" + str(channelID))
		NVICVector = "NVIC_" + str(periphId) + "_ENABLE"

		tcSym_CH_IntEnComment.append(channelID)
		tcSym_CH_IntEnComment[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_NVIC_ENABLE_COMMENT", tcChannelMenu[channelID])
		tcSym_CH_IntEnComment[channelID].setVisible(False)
		tcSym_CH_IntEnComment[channelID].setLabel("Warning!!! TC" +str(num)+"_CH"+str(channelID)+" Interrupt is Disabled in Interrupt Manager")
		tcSym_CH_IntEnComment[channelID].setDependencies(dependencyIntStatus, ["core." + NVICVector, "TC"+str(channelID)+"_ENABLE"])
		
		############################################################################
		#### Dependency END ####
		############################################################################
		
		#Clock symbols
		tcClockSymbols(tcComponent, channelID, tcSym_CH_Enable[channelID])
		
		if(channel[channelID] == True):
			tcModeValues = ["TIMER", "CAPTURE", "COMPARE"]
		else:
			tcModeValues = ["TIMER"]
		#operating mode
		tcSym_CH_OperatingMode.append(channelID)
		tcSym_CH_OperatingMode[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_OPERATING_MODE", tcSym_CH_Enable[channelID], tcModeValues)
		tcSym_CH_OperatingMode[channelID].setLabel("Operating Mode")
		tcSym_CH_OperatingMode[channelID].setDefaultValue("TIMER")
		
		#*****************************TIMER******************************
		#timer menu
		tcTimerMenu.append(channelID)
		tcTimerMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_TIMER", tcSym_CH_OperatingMode[channelID])
		tcTimerMenu[channelID].setLabel("Timer")
		tcTimerMenu[channelID].setDependencies(tcTimerVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])
		
		#timer period count
		global tcSym_CH_TimerPeriodCount
		tcSym_CH_TimerPeriodCount.append(channelID)
		tcSym_CH_TimerPeriodCount[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_TIMER_PERIOD_COUNT", tcTimerMenu[channelID])
		tcSym_CH_TimerPeriodCount[channelID].setLabel("Timer Period")
		tcSym_CH_TimerPeriodCount[channelID].setDefaultValue(10000)
		tcSym_CH_TimerPeriodCount[channelID].setMin(0)
		tcSym_CH_TimerPeriodCount[channelID].setMax(65535)
		
		#timer period in uS
		tcSym_CH_TimerPeriod.append(channelID)
		tcSym_CH_TimerPeriod[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_TIMER_PERIOD", tcTimerMenu[channelID])
		tcSym_CH_TimerPeriod[channelID].setLabel("****Timer period is  66.6 uS****")
		tcSym_CH_TimerPeriod[channelID].setDependencies(tcPeriodCalc, \
			["TC"+str(channelID)+"_TIMER_PERIOD_COUNT", "TC"+str(channelID)+"_CMR_TCCLKS", "TC"+str(channelID)+"_EXT_CLOCK", \
			"core.MASTERCLK_FREQ", "core.CLK_SLOW_XTAL", "core.PCK6_FREQ", "core.PCK7_FREQ"])
		
		#one-shot timer
		tcSym_CH_CMR_CPCSTOP.append(channelID)
		tcSym_CH_CMR_CPCSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CMR_CPCSTOP", tcTimerMenu[channelID])
		tcSym_CH_CMR_CPCSTOP[channelID].setLabel("Enable One Shot Mode")
		tcSym_CH_CMR_CPCSTOP[channelID].setDefaultValue(False)
		
		#period interrupt
		tcSym_CH_IER_CPCS.append(channelID)
		tcSym_CH_IER_CPCS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_IER_CPCS", tcTimerMenu[channelID])
		tcSym_CH_IER_CPCS[channelID].setLabel("Enable Period Interrupt")
		tcSym_CH_IER_CPCS[channelID].setReadOnly(True)
		tcSym_CH_IER_CPCS[channelID].setDefaultValue(True)
		
		#****************************CAPTURE*****************************
		#capture menu
		tcCaptureMenu.append(channelID)
		tcCaptureMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_CAPTURE", tcSym_CH_OperatingMode[channelID])
		tcCaptureMenu[channelID].setLabel("Capture")
		tcCaptureMenu[channelID].setDependencies(tcCaptureVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])
		tcCaptureMenu[channelID].setVisible(False)
		
		#one-shot timer
		tcSym_CH_CAPTURE_CMR_LDBSTOP.append(channelID)
		tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_CMR_LDBSTOP", tcCaptureMenu[channelID])
		tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID].setLabel("Enable One Shot Mode")
		tcSym_CH_CAPTURE_CMR_LDBSTOP[channelID].setDefaultValue(False)		
		
		#edge for capture A
		global tcSym_CH_CMR_LDRA
		childrenNodes = []
		loadEdgeA = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__LDRA\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			loadEdgeA.append(childrenNodes[param].getAttribute("name"))
		tcSym_CH_CMR_LDRA.append(channelID)
		tcSym_CH_CMR_LDRA[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_LDRA", tcCaptureMenu[channelID], loadEdgeA)
		tcSym_CH_CMR_LDRA[channelID].setLabel("Select TIOA Input Edge for Capture A")
		tcSym_CH_CMR_LDRA[channelID].setDefaultValue(loadEdgeA[1])
		
		#edge for capture B
		childrenNodes = []
		loadEdgeB = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__LDRB\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			loadEdgeB.append(childrenNodes[param].getAttribute("name"))
		tcSym_CH_CMR_LDRB.append(channelID)
		tcSym_CH_CMR_LDRB[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_LDRB", tcCaptureMenu[channelID], loadEdgeB)
		tcSym_CH_CMR_LDRB[channelID].setLabel("Select TIOA Input Edge for Capture B")
		tcSym_CH_CMR_LDRB[channelID].setDefaultValue(loadEdgeB[2])
		
		#Capture external reset
		global tcSym_CH_CAPTURE_EXT_RESET
		tcSym_CH_CAPTURE_EXT_RESET.append(channelID)
		tcSym_CH_CAPTURE_EXT_RESET[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_EXT_RESET", tcCaptureMenu[channelID])
		tcSym_CH_CAPTURE_EXT_RESET[channelID].setLabel("Reset Timer on External Event")
		tcSym_CH_CAPTURE_EXT_RESET[channelID].setDefaultValue(True)
		
		#external event signal
		global tcSym_CH_CMR_ABETRG
		tcValGroup_ABETRG = ["TIOA", "TIOB"]
		tcSym_CH_CMR_ABETRG.append(channelID)
		tcSym_CH_CMR_ABETRG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ABETRG", tcSym_CH_CAPTURE_EXT_RESET[channelID], tcValGroup_ABETRG)
		tcSym_CH_CMR_ABETRG[channelID].setLabel("Select External Event Input")
		tcSym_CH_CMR_ABETRG[channelID].setDefaultValue("TIOA")
		
		#external event edge
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ETRGEDG\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))		
		tcSym_CH_CMR_ETRGEDG.append(channelID)
		tcSym_CH_CMR_ETRGEDG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ETRGEDG", tcSym_CH_CAPTURE_EXT_RESET[channelID], comboOptions)
		tcSym_CH_CMR_ETRGEDG[channelID].setLabel("Select External Event Edge")
		tcSym_CH_CMR_ETRGEDG[channelID].setDefaultValue(comboOptions[2])
		
		#external event edge comment
		tcSym_CH_CMR_ETRGEDG_COMMENT.append(channelID)
		tcSym_CH_CMR_ETRGEDG_COMMENT[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CMR_ETRGEDG_COMMENT", tcSym_CH_CAPTURE_EXT_RESET[channelID])
		tcSym_CH_CMR_ETRGEDG_COMMENT[channelID].setLabel("** When 'external event input' is TIOA, 'external event edge' should NOT be same as 'capture A edge' **")
		
		#external event edge alert
		tcSym_CH_CMR_ETRGEDG_ALERT.append(channelID)
		tcSym_CH_CMR_ETRGEDG_ALERT[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_CMR_ETRGEDG_ALERT", tcSym_CH_CAPTURE_EXT_RESET[channelID])
		tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setLabel("**** EXTRNAL EVENT EDGE IS SAME AS CAPTURE A EDGE ****")		
		tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setVisible(False)
		tcSym_CH_CMR_ETRGEDG_ALERT[channelID].setDependencies(tcCaptureEdgeSelect, ["TC"+str(channelID)+"_CMR_ETRGEDG", "TC"+str(channelID)+"_CAPTURE_EXT_RESET", "TC"+str(channelID)+"_CMR_ABETRG", "TC"+str(channelID)+"_CMR_LDRA"])		
		
		#capture A interrupt
		tcSym_CH_CAPTURE_IER_LDRAS.append(channelID)
		tcSym_CH_CAPTURE_IER_LDRAS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_LDRAS", tcCaptureMenu[channelID])
		tcSym_CH_CAPTURE_IER_LDRAS[channelID].setLabel("Enable Capture A Interrupt")
		tcSym_CH_CAPTURE_IER_LDRAS[channelID].setDefaultValue(True)
		
		#capture B interrupt
		tcSym_CH_CAPTURE_IER_LDRBS.append(channelID)
		tcSym_CH_CAPTURE_IER_LDRBS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_LDRBS", tcCaptureMenu[channelID])
		tcSym_CH_CAPTURE_IER_LDRBS[channelID].setLabel("Enable Capture B Interrupt")
		tcSym_CH_CAPTURE_IER_LDRBS[channelID].setDefaultValue(False)
		
		#counter overflow interrupt
		tcSym_CH_CAPTURE_IER_COVFS.append(channelID)
		tcSym_CH_CAPTURE_IER_COVFS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_CAPTURE_IER_COVFS", tcCaptureMenu[channelID])
		tcSym_CH_CAPTURE_IER_COVFS[channelID].setLabel("Enable Counter Overflow Interrupt")
		tcSym_CH_CAPTURE_IER_COVFS[channelID].setDefaultValue(False)
		
		#***************************COMPARE*******************************
		#compare menu
		tcCompareMenu.append(channelID)
		tcCompareMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPARE", tcSym_CH_OperatingMode[channelID])
		tcCompareMenu[channelID].setLabel("Compare")
		tcCompareMenu[channelID].setDependencies(tcCompareVisible, ["TC"+str(channelID)+"_OPERATING_MODE"])
		tcCompareMenu[channelID].setVisible(False)
		
		#waveform type
		tcSym_CH_CMR_WAVSEL.append(channelID)
		tcSym_CH_CMR_WAVSEL[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_WAVSEL", tcCompareMenu[channelID])
		tcSym_CH_CMR_WAVSEL[channelID].setLabel("Select Waveform Mode")
		tcSym_CH_CMR_WAVSEL[channelID].addKey("UP_RC", "0", "UP Count Mode")
		tcSym_CH_CMR_WAVSEL[channelID].addKey("UPDOWN_RC", "0", "UP and DOWN Count Mode")
		tcSym_CH_CMR_WAVSEL[channelID].setDefaultValue(0)
		tcSym_CH_CMR_WAVSEL[channelID].setDisplayMode("Description")
		tcSym_CH_CMR_WAVSEL[channelID].setOutputMode("Key")
	
		#one-shot timer
		tcSym_CH_COMPARE_CMR_CPCSTOP.append(channelID)
		tcSym_CH_COMPARE_CMR_CPCSTOP[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_COMPARE_CMR_CPCSTOP", tcCompareMenu[channelID])
		tcSym_CH_COMPARE_CMR_CPCSTOP[channelID].setLabel("Enable One Shot Mode")
		tcSym_CH_COMPARE_CMR_CPCSTOP[channelID].setDefaultValue(False)		
		
		#period count
		global tcSym_CH_ComparePeriodCount
		tcSym_CH_ComparePeriodCount.append(channelID)
		tcSym_CH_ComparePeriodCount[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_PERIOD_COUNT", tcCompareMenu[channelID])
		tcSym_CH_ComparePeriodCount[channelID].setLabel("Period Value")
		tcSym_CH_ComparePeriodCount[channelID].setDefaultValue(10000)
		tcSym_CH_ComparePeriodCount[channelID].setMin(0)
		tcSym_CH_ComparePeriodCount[channelID].setMax(65535)
		
		#period time in uS
		tcSym_CH_ComparePeriod.append(channelID)
		tcSym_CH_ComparePeriod[channelID] = tcComponent.createCommentSymbol("TC"+str(channelID)+"_COMPARE_PERIOD", tcCompareMenu[channelID])
		tcSym_CH_ComparePeriod[channelID].setLabel("****Timer Period is 66.6 uS****")
		tcSym_CH_ComparePeriod[channelID].setDependencies(tcPeriodCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT", "TC"+str(channelID)+"_CMR_TCCLKS", \
			"core.MASTERCLK_FREQ", "core.CLK_SLOW_XTAL", "core.PCK6_FREQ", "core.PCK7_FREQ"])	

		#External Event Menu
		tcEventMenu.append(channelID)
		tcEventMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_EXT_EVENT", tcCompareMenu[channelID])
		tcEventMenu[channelID].setLabel("External Event Input Configuration")
		
		#external reset signal
		tcSym_CH_CMR_EEVT.append(channelID)
		tcSym_CH_CMR_EEVT[channelID] = tcComponent.createKeyValueSetSymbol("TC"+str(channelID)+"_CMR_EEVT", tcEventMenu[channelID])
		tcSym_CH_CMR_EEVT[channelID].setLabel("Select External Event Input")
		childrenNodes = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__EEVT\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			tcSym_CH_CMR_EEVT[channelID].addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"), childrenNodes[param].getAttribute("caption"))	
		tcSym_CH_CMR_EEVT[channelID].setDefaultValue(0)
		tcSym_CH_CMR_EEVT[channelID].setDisplayMode("Description")
		tcSym_CH_CMR_EEVT[channelID].setOutputMode("Key")
		
		#External reset edge
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__EEVTEDG\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))		
		tcSym_CH_CMP_CMR_ETRGEDG.append(channelID)
		tcSym_CH_CMP_CMR_ETRGEDG[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMP_CMR_ETRGEDG", tcEventMenu[channelID], comboOptions)
		tcSym_CH_CMP_CMR_ETRGEDG[channelID].setLabel("Select External Event Edge")
		tcSym_CH_CMP_CMR_ETRGEDG[channelID].setDefaultValue(comboOptions[0])
		
		#Waveform A menu
		tcCompareAMenu.append(channelID)
		tcCompareAMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPAREA", tcCompareMenu[channelID])
		tcCompareAMenu[channelID].setLabel("Compare A Output (TIOA) Configuration")
		
		#compare A
		global tcSym_CH_CompareA
		tcSym_CH_CompareA.append(channelID)
		tcSym_CH_CompareA[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_A", tcCompareAMenu[channelID])
		tcSym_CH_CompareA[channelID].setLabel("Compare Value")
		tcSym_CH_CompareA[channelID].setDefaultValue(5000)
		tcSym_CH_CompareA[channelID].setMin(0)
		tcSym_CH_CompareA[channelID].setMax(tcSym_CH_ComparePeriodCount[channelID].getValue())
		tcSym_CH_CompareA[channelID].setDependencies(tcCompareMaxCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT"])
		
		#action on compare A
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ACPA\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_ACPA.append(channelID)
		tcSym_CH_CMR_ACPA[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ACPA", tcCompareAMenu[channelID], comboOptions)
		tcSym_CH_CMR_ACPA[channelID].setLabel("Action on Compare Match A")
		tcSym_CH_CMR_ACPA[channelID].setDefaultValue(comboOptions[1])
		
		#action on compare C
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__ACPC\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_ACPC.append(channelID)
		tcSym_CH_CMR_ACPC[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_ACPC", tcCompareAMenu[channelID], comboOptions)
		tcSym_CH_CMR_ACPC[channelID].setLabel("Action on Compare Match C")
		tcSym_CH_CMR_ACPC[channelID].setDefaultValue(comboOptions[2])
		
		#action on external event
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__AEEVT\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_AEEVT.append(channelID)
		tcSym_CH_CMR_AEEVT[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_AEEVT", tcCompareAMenu[channelID], comboOptions)
		tcSym_CH_CMR_AEEVT[channelID].setLabel("Action on External Event")
		tcSym_CH_CMR_AEEVT[channelID].setDefaultValue(comboOptions[2])
		tcSym_CH_CMR_AEEVT[channelID].setDependencies(tcActionExtEvtVisible, ["TC"+str(channelID)+"_CMP_CMR_ETRGEDG"])
		tcSym_CH_CMR_AEEVT[channelID].setVisible(False)
		
		#waveform B menu
		tcCompareBMenu.append(channelID)
		tcCompareBMenu[channelID] = tcComponent.createMenuSymbol("TC"+str(channelID)+"_COMPAREB", tcCompareMenu[channelID])
		tcCompareBMenu[channelID].setLabel("Compare B Output (TIOB) Configuration")
		tcCompareBMenu[channelID].setDependencies(tcWaveformBVisible, ["TC"+str(channelID)+"_CMR_EEVT"])
		
		#Compare B
		global tcSym_CH_CompareB
		tcSym_CH_CompareB.append(channelID)
		tcSym_CH_CompareB[channelID] = tcComponent.createIntegerSymbol("TC"+str(channelID)+"_COMPARE_B", tcCompareBMenu[channelID])
		tcSym_CH_CompareB[channelID].setLabel("Compare Value")
		tcSym_CH_CompareB[channelID].setDefaultValue(3000)
		tcSym_CH_CompareB[channelID].setMin(0)
		tcSym_CH_CompareB[channelID].setMax(tcSym_CH_ComparePeriodCount[channelID].getValue())
		tcSym_CH_CompareB[channelID].setDependencies(tcCompareMaxCalc, ["TC"+str(channelID)+"_COMPARE_PERIOD_COUNT"])
		
		#Action on compare B
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BCPB\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_BCPB.append(channelID)
		tcSym_CH_CMR_BCPB[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BCPB", tcCompareBMenu[channelID], comboOptions)
		tcSym_CH_CMR_BCPB[channelID].setLabel("Action on Compare Match B")
		tcSym_CH_CMR_BCPB[channelID].setDefaultValue(comboOptions[1])
		
		#Action on compare C
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BCPC\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_BCPC.append(channelID)
		tcSym_CH_CMR_BCPC[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BCPC", tcCompareBMenu[channelID], comboOptions)
		tcSym_CH_CMR_BCPC[channelID].setLabel("Action on Compare Match C")
		tcSym_CH_CMR_BCPC[channelID].setDefaultValue(comboOptions[2])	
		
		#Action on external event
		childrenNodes = []
		comboOptions = []
		tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CMR0__BEEVT\"]")
		childrenNodes = tc.getChildren()	
		for param in range (0 , len(childrenNodes)):
			comboOptions.append(childrenNodes[param].getAttribute("name"))			
		tcSym_CH_CMR_BEEVT.append(channelID)
		tcSym_CH_CMR_BEEVT[channelID] = tcComponent.createComboSymbol("TC"+str(channelID)+"_CMR_BEEVT", tcCompareBMenu[channelID], comboOptions)
		tcSym_CH_CMR_BEEVT[channelID].setLabel("Action on External Event")
		tcSym_CH_CMR_BEEVT[channelID].setDefaultValue(comboOptions[2])
		tcSym_CH_CMR_BEEVT[channelID].setDependencies(tcActionExtEvtVisible, ["TC"+str(channelID)+"_CMP_CMR_ETRGEDG"])
		tcSym_CH_CMR_BEEVT[channelID].setVisible(False)
		
		#period interrupt
		tcSym_CH_COMPARE_IER_CPCS.append(channelID)
		tcSym_CH_COMPARE_IER_CPCS[channelID] = tcComponent.createBooleanSymbol("TC"+str(channelID)+"_COMPARE_IER_CPCS", tcCompareMenu[channelID])
		tcSym_CH_COMPARE_IER_CPCS[channelID].setLabel("Enable Period Interrupt")
		tcSym_CH_COMPARE_IER_CPCS[channelID].setDefaultValue(True)
		
	tcIndex = tcComponent.createIntegerSymbol("INDEX", tcChannelMenu[channelID])
	tcIndex.setVisible(False)
	tcIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")
	
###################################################################################################
########################### Code Generation   #################################
###################################################################################################	
	tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]")
	tcID = tc.getAttribute("id")	
	
	tcHeaderFile = tcComponent.createFileSymbol(None, None)
	tcHeaderFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/plib_tc.h.ftl")
	tcHeaderFile.setOutputName("plib_tc" + str(num) + ".h")
	tcHeaderFile.setDestPath("/peripheral/tc/")
	tcHeaderFile.setProjectPath("/peripheral/tc/")
	tcHeaderFile.setType("HEADER")
	tcHeaderFile.setOverwrite(True)
	tcHeaderFile.setMarkup(True)
		
	tcSource1File = tcComponent.createFileSymbol(None, None)
	tcSource1File.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/plib_tc.c.ftl")
	tcSource1File.setOutputName("plib_tc" + str(num) + ".c")
	tcSource1File.setDestPath("/peripheral/tc/")
	tcSource1File.setProjectPath("/peripheral/tc/")
	tcSource1File.setType("SOURCE")
	tcSource1File.setOverwrite(True)	
	tcSource1File.setMarkup(True)

	tcGlobalHeaderFile = tcComponent.createFileSymbol(None, None)
	tcGlobalHeaderFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/plib_tc.h")
	tcGlobalHeaderFile.setOutputName("plib_tc" + ".h")
	tcGlobalHeaderFile.setDestPath("/peripheral/tc/")
	tcGlobalHeaderFile.setProjectPath("/peripheral/tc/")
	tcGlobalHeaderFile.setType("HEADER")
	tcGlobalHeaderFile.setMarkup(False)
	
	tcSystemInitFile = tcComponent.createFileSymbol(None, None)
	tcSystemInitFile.setType("STRING")
	tcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
	tcSystemInitFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/system/system_init.c.ftl")
	tcSystemInitFile.setMarkup(True)

	tcSystemDefinitionFile = tcComponent.createFileSymbol(None, None)
	tcSystemDefinitionFile.setType("STRING")
	tcSystemDefinitionFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	tcSystemDefinitionFile.setSourcePath("../peripheral/tc_"+str(tcID)+"/templates/system/system_definitions.h.ftl")
	tcSystemDefinitionFile.setMarkup(True)