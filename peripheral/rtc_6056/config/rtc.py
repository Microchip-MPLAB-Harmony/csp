#Function for initiating the UI
def instantiateComponent(rtcComponent):
	
	num = rtcComponent.getID()[-1:]
	print("Running RTC")
	
	rtcRegModule = Register.getRegisterModule("RTC")
        rtcRegGroup = rtcRegModule.getRegisterGroup("RTC")

        rtcReg_MR = rtcRegGroup.getRegister("RTC_MR")
	rtcReg_CR = rtcRegGroup.getRegister("RTC_CR");
        rtcBitField_MR_OUT0 = rtcReg_MR.getBitfield("OUT0")
        rtcBitField_MR_OUT1 = rtcReg_MR.getBitfield("OUT1")
        rtcBitField_MR_THIGH = rtcReg_MR.getBitfield("THIGH")
	rtcBitField_MR_TPERIOD = rtcReg_MR.getBitfield("TPERIOD")
	rtcBitField_CR_TIMEVSEL = rtcReg_CR.getBitfield("TIMEVSEL")
	rtcBitField_CR_CALEVSEL = rtcReg_CR.getBitfield("CALEVSEL")
	rtcValGrp_MR_OUT0 = rtcRegModule.getValueGroup(rtcBitField_MR_OUT0.getValueGroupName())
        rtcValGrp_MR_OUT1 = rtcRegModule.getValueGroup(rtcBitField_MR_OUT1.getValueGroupName())
        rtcValGrp_MR_THIGH = rtcRegModule.getValueGroup(rtcBitField_MR_THIGH.getValueGroupName())
	rtcValGrp_MR_TPERIOD = rtcRegModule.getValueGroup(rtcBitField_MR_TPERIOD.getValueGroupName())
	rtcValGrp_CR_TIMEVSEL = rtcRegModule.getValueGroup(rtcBitField_CR_TIMEVSEL.getValueGroupName())
	rtcValGrp_CR_CALEVSEL = rtcRegModule.getValueGroup(rtcBitField_CR_CALEVSEL.getValueGroupName())
	
	#Create the top menu
	rtcMenu = rtcComponent.createMenuSymbol(None, None)
	rtcMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	rtcInterrupt = rtcComponent.createBooleanSymbol("rtcEnableInterrupt", rtcMenu)
	print(rtcInterrupt)
	rtcInterrupt.setLabel("Enable Interrupt")
	rtcInterrupt.setDefaultValue(True)
	
	#instance index
	rtcIndex = rtcComponent.createIntegerSymbol("INDEX", rtcMenu)
	rtcIndex.setVisible(False)
	rtcIndex.setDefaultValue(int(num))
	
	rtcSym_MR_OUT0 = rtcComponent.createComboSymbol("RTC_MR_OUT0", rtcMenu, rtcValGrp_MR_OUT0.getValueNames())
	print(rtcSym_MR_OUT0)
	rtcSym_MR_OUT0.setLabel(rtcBitField_MR_OUT0.getDescription())
	rtcSym_MR_OUT0.setDefaultValue("NO_WAVE")
	
	rtcSym_MR_OUT1 = rtcComponent.createComboSymbol("RTC_MR_OUT1", rtcMenu, rtcValGrp_MR_OUT1.getValueNames())
	print(rtcSym_MR_OUT1)
	rtcSym_MR_OUT1.setLabel("RTCOUT1 Output Source Selection")
	rtcSym_MR_OUT1.setDefaultValue("NO_WAVE")
	
	rtcSym_MR_THIGH = rtcComponent.createComboSymbol("RTC_MR_THIGH", rtcMenu, rtcValGrp_MR_THIGH.getValueNames())
	print(rtcSym_MR_THIGH)
	rtcSym_MR_THIGH.setLabel("High Duration of the Output Pulse")
	rtcSym_MR_THIGH.setDefaultValue("H_31MS")
	rtcSym_MR_THIGH.setVisible(False)
	rtcSym_MR_THIGH.setDependencies(rtcTHIGH, ["RTC_MR_OUT0", "RTC_MR_OUT1"])
	
	rtcSym_MR_TPERIOD = rtcComponent.createComboSymbol("RTC_MR_TPERIOD", rtcMenu, rtcValGrp_MR_TPERIOD.getValueNames())
	print(rtcSym_MR_TPERIOD)
	rtcSym_MR_TPERIOD.setLabel("Period of the Output Pulse")
	rtcSym_MR_TPERIOD.setDefaultValue("P_1S")
	rtcSym_MR_TPERIOD.setVisible(False)
	rtcSym_MR_TPERIOD.setDependencies(rtcTPERIOD, ["RTC_MR_OUT0", "RTC_MR_OUT1"])
	
	rtcSym_CR_TIMEVSEL= rtcComponent.createComboSymbol("RTC_CR_TIMEVSEL", rtcMenu, rtcValGrp_CR_TIMEVSEL.getValueNames())
	print(rtcSym_CR_TIMEVSEL)
	rtcSym_CR_TIMEVSEL.setLabel("Time Event Selection")
	rtcSym_CR_TIMEVSEL.setDefaultValue("MINUTE")
	
	rtcSym_CR_CALEVSEL = rtcComponent.createComboSymbol("RTC_CR_CALEVSEL", rtcMenu, rtcValGrp_CR_CALEVSEL.getValueNames())
	print(rtcSym_CR_CALEVSEL)
	rtcSym_CR_CALEVSEL.setLabel("Calendar Event Selection")
	rtcSym_CR_CALEVSEL.setDefaultValue("WEEK")
	
	configName = Variables.get("__CONFIGURATION_NAME")

	#Generate Output Header
	rtcHeaderFile = rtcComponent.createFileSymbol(None, None)
	rtcHeaderFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.h.ftl")
	rtcHeaderFile.setMarkup(True)
	rtcHeaderFile.setOutputName("plib_rtc" + str(num) + ".h")
	rtcHeaderFile.setOverwrite(True)
	rtcHeaderFile.setDestPath("peripheral/rtc/")
	rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
	rtcHeaderFile.setType("HEADER")
	#Generate Output source
	rtcSourceFile = rtcComponent.createFileSymbol(None, None)
	rtcSourceFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.c.ftl")
	rtcSourceFile.setMarkup(True)
	rtcSourceFile.setOutputName("plib_rtc" + str(num) + ".c")
	rtcSourceFile.setOverwrite(True)
	rtcSourceFile.setDestPath("peripheral/rtc/")
	rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
	rtcSourceFile.setType("SOURCE")
	
	rtcSystemInitFile = rtcComponent.createFileSymbol(None, None)
	rtcSystemInitFile.setType("STRING")
	rtcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
	rtcSystemInitFile.setSourcePath("../peripheral/rtc_6056/templates/system/system_initialize.c.ftl")
	rtcSystemInitFile.setMarkup(True)

	rtcSystemIntFile = rtcComponent.createFileSymbol(None, None)
	rtcSystemIntFile.setType("STRING")
	rtcSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	rtcSystemIntFile.setSourcePath("../peripheral/rtc_6056/templates/system/system_interrupt.c.ftl")
	rtcSystemIntFile.setMarkup(True)

	rtcSystemDefFile = rtcComponent.createFileSymbol(None, None)
	rtcSystemDefFile.setType("STRING")
	rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rtcSystemDefFile.setSourcePath("../peripheral/rtc_6056/templates/system/system_definitions.h.ftl")
	rtcSystemDefFile.setMarkup(True)

	
def rtcTHIGH(rtcSym_MR_THIGH,test):
	data = rtcSym_MR_THIGH.getComponent()
	rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
	rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
	if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
		rtcSym_MR_THIGH.setVisible(False)
	else:
		rtcSym_MR_THIGH.setVisible(True)
		
def rtcTPERIOD(rtcSym_MR_TPERIOD,test):
	data = rtcSym_MR_TPERIOD.getComponent()
	rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
	rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
	if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
		rtcSym_MR_TPERIOD.setVisible(False)
	else:
		rtcSym_MR_TPERIOD.setVisible(True)