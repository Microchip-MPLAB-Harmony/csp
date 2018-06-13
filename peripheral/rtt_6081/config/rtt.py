global instance
global peripId
global NVICVector
global NVICHandler
global NVICHandlerLock

def NVICControl(rttNVIC, event):

	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	
	Database.clearSymbolValue("core", NVICVector)
	Database.clearSymbolValue("core", NVICHandler)
	Database.clearSymbolValue("core", NVICHandlerLock)
	
	if (event["value"] == True):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "RTT" + str(instance) + "_InterruptHandler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	else :
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "RTT" + str(instance) + "_Handler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, False, 2)

def instantiateComponent(rttComponent):
	
	global instance
	global peripId
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	instance = rttComponent.getID()[-1:]

	rttMenu = rttComponent.createMenuSymbol("RTT_MENU_0", None)
	rttMenu.setLabel("Hardware Settings ")
	
	rttPeriodicInterrupt = rttComponent.createBooleanSymbol("rttINCIEN", rttMenu)
	rttPeriodicInterrupt.setLabel("Enable Prescale Rollover Interrupt")
	rttPeriodicInterrupt.setDefaultValue(False)
	
	rttAlarm = rttComponent.createBooleanSymbol("rttALMIEN", rttMenu)
	rttAlarm.setLabel("Enable Alarm Interrupt")
	rttAlarm.setDefaultValue(False)
	
	rttIndex = rttComponent.createIntegerSymbol("INDEX", rttMenu)
	rttIndex.setVisible(False)
	rttIndex.setDefaultValue(int(instance))
	
	rttClkSrc = rttComponent.createBooleanSymbol("rttRTC1HZ", rttMenu)
	rttClkSrc.setLabel("Use RTC 1Hz as clock Source")
	rttClkSrc.setDefaultValue(False)	
	
	rttPrescaleValue = rttComponent.createIntegerSymbol("rttRTPRES", rttMenu)
	rttPrescaleValue.setLabel("Prescalar Value ")
	rttPrescaleValue.setMax(65536)
	rttPrescaleValue.setDefaultValue(32768)
	rttPrescaleValue.setDependencies(rttPrescaleHide, ["rttRTC1HZ"])
	
	rttPrescaleValueWarning = rttComponent.createCommentSymbol("rttRTPRESWarning", rttMenu)
	rttPrescaleValueWarning.setVisible(False)
	rttPrescaleValueWarning.setLabel("******* RTT Prescale value of 1 or 2 is invalid")
	rttPrescaleValueWarning.setDependencies(rttPrescaleWarning, ["rttRTPRES"])
	
	rttFreq = rttComponent.createStringSymbol("rttFREQ", rttMenu)
	rttFreq.setLabel("RTT Counter Clock Resolution(seconds)")
	rttFreq.setDependencies(rttFreq_cal, ["rttRTC1HZ", "rttRTPRES"])
	rttFreq.setDefaultValue(str(1))
	rttFreq.setReadOnly(True)

	peripId = Interrupt.getInterruptIndex("RTT")
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

	Database.clearSymbolValue("core", NVICVector)
	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.clearSymbolValue("core", NVICHandler)
	Database.setSymbolValue("core", NVICHandler, "RTT" + str(instance) + "_InterruptHandler", 2)
	Database.clearSymbolValue("core", NVICHandlerLock)
	Database.setSymbolValue("core", NVICHandlerLock, False, 2)

	# NVIC Dynamic settings
	rttNVICControl = rttComponent.createBooleanSymbol("NVIC_RTT_ENABLE", None)
	rttNVICControl.setDependencies(NVICControl, ["rttALMIEN", "rttINCIEN"])
	rttNVICControl.setVisible(False)
	
	configName = Variables.get("__CONFIGURATION_NAME")

	rttHeader1File = rttComponent.createFileSymbol("RTT_FILE_0", None)
	rttHeader1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.h.ftl")
	rttHeader1File.setMarkup(True)
	rttHeader1File.setOutputName("plib_rtt" + str(instance) + ".h")
	rttHeader1File.setDestPath("/peripheral/rtt/")
	rttHeader1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
	rttHeader1File.setType("HEADER")
	
	rttSource1File = rttComponent.createFileSymbol("RTT_FILE_1", None)
	rttSource1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.c.ftl")
	rttSource1File.setMarkup(True)
	rttSource1File.setOutputName("plib_rtt" + str(instance) + ".c")
	rttSource1File.setDestPath("/peripheral/rtt/")
	rttSource1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
	rttSource1File.setType("SOURCE")
	
	rttSystemInitFile = rttComponent.createFileSymbol("RTT_FILE_2", None)
	rttSystemInitFile.setType("STRING")
	rttSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	rttSystemInitFile.setSourcePath("../peripheral/rtt_6081/templates/system/system_initialize.c.ftl")
	rttSystemInitFile.setMarkup(True)

	rttSystemDefFile = rttComponent.createFileSymbol("RTT_FILE_3", None)
	rttSystemDefFile.setType("STRING")
	rttSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rttSystemDefFile.setSourcePath("../peripheral/rtt_6081/templates/system/system_definitions.h.ftl")
	rttSystemDefFile.setMarkup(True)

def rttPrescaleHide(rttPrescaleValue, event):
	if event["value"] == True:
		rttPrescaleValue.setVisible(False)
	else:
		rttPrescaleValue.setVisible(True)
		
def	rttFreq_cal(rttFreq, event):
	data = rttFreq.getComponent()
	rttData = str(float(65536) / 32768)
	rtt1K = data.getSymbolValue("rttRTC1HZ")
	if rtt1K == True:
		rttFreq.clearValue("rttFREQ")
		rttFreq.setValue(str(1),2)
	else:
		rttPres = data.getSymbolValue("rttRTPRES")
		if rttPres == 0:
			rttData = str(float(65536) / 32768)
			rttFreq.clearValue("rttFREQ")
			rttFreq.setValue(str(rttData),2)
		elif rttPres > 2:
			rttData = str(float(rttPres) / 32768)
			rttFreq.clearValue("rttFREQ")
			rttFreq.setValue(str(rttData),2)
			
def rttPrescaleWarning(comment, prescale):
	if prescale["value"] == 1 or prescale["value"] == 2:
		comment.setVisible(True)
	else :
		comment.setVisible(False)
		
def destroyComponent(efcComponent):
	
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	
	Database.setSymbolValue("core", NVICVector, False, 2)
	Database.setSymbolValue("core", NVICHandler, "RTT0_Handler", 2)
	Database.setSymbolValue("core", NVICHandlerLock, False, 2)