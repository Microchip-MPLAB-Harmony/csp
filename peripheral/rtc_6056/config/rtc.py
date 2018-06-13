#Function for initiating the UI
global instance
global peripId
global NVICVector
global NVICHandler
global NVICHandlerLock

def NVICControl(rtcNVIC, event):
	global NVICVector
	global NVICHandler
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	Database.clearSymbolValue("core", NVICHandlerLock)
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "RTC" + str(instance) + "_InterruptHandler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "RTC0_Handler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, False, 2)
		
def instantiateComponent(rtcComponent):
	global instance
	global peripId
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	out0_names = []
	out1_names = []
	thigh_names = []
	tperiod_names = []
	timevsel_names = []
	calevsel_names = []
	
	instance = rtcComponent.getID()[-1:]

	rtcBitField_MR_OUT0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="OUT0"]')
	rtcValGrp_MR_OUT0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__OUT0"]')

	rtcBitField_MR_OUT1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="OUT1"]')
	rtcValGrp_MR_OUT1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__OUT1"]')

	rtcBitField_MR_THIGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="THIGH"]')
	rtcValGrp_MR_THIGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__THIGH"]')

	rtcBitField_MR_TPERIOD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="TPERIOD"]')
	rtcValGrp_MR_TPERIOD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__TPERIOD"]')

	rtcBitField_CR_TIMEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_CR"]/bitfield@[name="TIMEVSEL"]')
	rtcValGrp_CR_TIMEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_CR__TIMEVSEL"]')
	
	rtcBitField_CR_CALEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_CR"]/bitfield@[name="CALEVSEL"]')
	rtcValGrp_CR_CALEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_CR__CALEVSEL"]')
	
	#Create the top menu
	rtcMenu = rtcComponent.createMenuSymbol("RTC_MENU_0", None)
	rtcMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	rtcInterrupt = rtcComponent.createBooleanSymbol("rtcEnableInterrupt", rtcMenu)
	rtcInterrupt.setLabel("Enable Interrupt")
	rtcInterrupt.setDefaultValue(True)
	
	
	peripId = Interrupt.getInterruptIndex("RTC")
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

	Database.clearSymbolValue("core", NVICVector)
	Database.setSymbolValue("core", NVICVector, True, 2)
	Database.clearSymbolValue("core", NVICHandler)
	Database.setSymbolValue("core", NVICHandler, "RTC" + str(instance) + "_InterruptHandler", 2)
	Database.clearSymbolValue("core", NVICHandlerLock)
	Database.setSymbolValue("core", NVICHandlerLock, True, 2)

	# NVIC Dynamic settings
	rtcNVICControl = rtcComponent.createBooleanSymbol("NVIC_RTC_ENABLE", None)
	rtcNVICControl.setDependencies(NVICControl, ["rtcEnableInterrupt"])
	rtcNVICControl.setVisible(False)
	
	#instance index
	rtcIndex = rtcComponent.createIntegerSymbol("INDEX", rtcMenu)
	rtcIndex.setVisible(False)
	rtcIndex.setDefaultValue(int(instance))
	
	for id in range(0,len(rtcValGrp_MR_OUT0.getChildren())):
		out0_names.append(rtcValGrp_MR_OUT0.getChildren()[id].getAttribute("name"))
		
	rtcSym_MR_OUT0 = rtcComponent.createComboSymbol("RTC_MR_OUT0", rtcMenu, out0_names)
	rtcSym_MR_OUT0.setLabel(rtcBitField_MR_OUT0.getAttribute("caption"))
	rtcSym_MR_OUT0.setDefaultValue("NO_WAVE")
	
	for id in range(0,len(rtcValGrp_MR_OUT1.getChildren())):
		out1_names.append(rtcValGrp_MR_OUT1.getChildren()[id].getAttribute("name"))
		
	rtcSym_MR_OUT1 = rtcComponent.createComboSymbol("RTC_MR_OUT1", rtcMenu, out1_names)
	rtcSym_MR_OUT1.setLabel(rtcBitField_MR_OUT1.getAttribute("caption"))
	rtcSym_MR_OUT1.setDefaultValue("NO_WAVE")
	
	for id in range(0,len(rtcValGrp_MR_THIGH.getChildren())):
		thigh_names.append(rtcValGrp_MR_THIGH.getChildren()[id].getAttribute("name"))
		
	rtcSym_MR_THIGH = rtcComponent.createComboSymbol("RTC_MR_THIGH", rtcMenu, thigh_names)
	rtcSym_MR_THIGH.setLabel(rtcBitField_MR_THIGH.getAttribute("caption"))
	rtcSym_MR_THIGH.setDefaultValue("H_31MS")
	rtcSym_MR_THIGH.setVisible(False)
	rtcSym_MR_THIGH.setDependencies(rtcTHIGH, ["RTC_MR_OUT0", "RTC_MR_OUT1"])
	
	for id in range(0,len(rtcValGrp_MR_TPERIOD.getChildren())):
		tperiod_names.append(rtcValGrp_MR_TPERIOD.getChildren()[id].getAttribute("name"))
		
	rtcSym_MR_TPERIOD = rtcComponent.createComboSymbol("RTC_MR_TPERIOD", rtcMenu, tperiod_names)
	rtcSym_MR_TPERIOD.setLabel(rtcBitField_MR_TPERIOD.getAttribute("caption"))
	rtcSym_MR_TPERIOD.setDefaultValue("P_1S")
	rtcSym_MR_TPERIOD.setVisible(False)
	rtcSym_MR_TPERIOD.setDependencies(rtcTPERIOD, ["RTC_MR_OUT0", "RTC_MR_OUT1"])

	for id in range(0,len(rtcValGrp_CR_TIMEVSEL.getChildren())):
		timevsel_names.append(rtcValGrp_CR_TIMEVSEL.getChildren()[id].getAttribute("name"))
		
	rtcSym_CR_TIMEVSEL= rtcComponent.createComboSymbol("RTC_CR_TIMEVSEL", rtcMenu, timevsel_names)
	rtcSym_CR_TIMEVSEL.setLabel(rtcBitField_CR_TIMEVSEL.getAttribute("caption"))
	rtcSym_CR_TIMEVSEL.setDefaultValue("MINUTE")

	for id in range(0,len(rtcValGrp_CR_CALEVSEL.getChildren())):
		calevsel_names.append(rtcValGrp_CR_CALEVSEL.getChildren()[id].getAttribute("name"))	
		
	rtcSym_CR_CALEVSEL = rtcComponent.createComboSymbol("RTC_CR_CALEVSEL", rtcMenu, calevsel_names)
	rtcSym_CR_CALEVSEL.setLabel(rtcBitField_CR_CALEVSEL.getAttribute("caption"))
	rtcSym_CR_CALEVSEL.setDefaultValue("WEEK")
	
	configName = Variables.get("__CONFIGURATION_NAME")

	#Generate Output Header
	rtcHeaderFile = rtcComponent.createFileSymbol("RTC_FILE_0", None)
	rtcHeaderFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.h.ftl")
	rtcHeaderFile.setMarkup(True)
	rtcHeaderFile.setOutputName("plib_rtc" + str(instance) + ".h")
	rtcHeaderFile.setOverwrite(True)
	rtcHeaderFile.setDestPath("peripheral/rtc/")
	rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
	rtcHeaderFile.setType("HEADER")
	#Generate Output source
	rtcSourceFile = rtcComponent.createFileSymbol("RTC_FILE_1", None)
	rtcSourceFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.c.ftl")
	rtcSourceFile.setMarkup(True)
	rtcSourceFile.setOutputName("plib_rtc" + str(instance) + ".c")
	rtcSourceFile.setOverwrite(True)
	rtcSourceFile.setDestPath("peripheral/rtc/")
	rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
	rtcSourceFile.setType("SOURCE")
	
	rtcSystemInitFile = rtcComponent.createFileSymbol("RTC_FILE_2", None)
	rtcSystemInitFile.setType("STRING")
	rtcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	rtcSystemInitFile.setSourcePath("../peripheral/rtc_6056/templates/system/system_initialize.c.ftl")
	rtcSystemInitFile.setMarkup(True)

	rtcSystemDefFile = rtcComponent.createFileSymbol("RTC_FILE_3", None)
	rtcSystemDefFile.setType("STRING")
	rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rtcSystemDefFile.setSourcePath("../peripheral/rtc_6056/templates/system/system_definitions.h.ftl")
	rtcSystemDefFile.setMarkup(True)

	
def rtcTHIGH(rtcSym_MR_THIGH, event):
	data = rtcSym_MR_THIGH.getComponent()
	rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
	rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
	if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
		rtcSym_MR_THIGH.setVisible(False)
	else:
		rtcSym_MR_THIGH.setVisible(True)
		
def rtcTPERIOD(rtcSym_MR_TPERIOD, event):
	data = rtcSym_MR_TPERIOD.getComponent()
	rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
	rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
	if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
		rtcSym_MR_TPERIOD.setVisible(False)
	else:
		rtcSym_MR_TPERIOD.setVisible(True)
		
def destroyComponent(rtcComponent):
	
	global instance
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	
	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.setSymbolValue("core", NVICHandler, "RTC0_Handler", 2)
	Database.setSymbolValue("core", NVICHandlerLock, False, 2)