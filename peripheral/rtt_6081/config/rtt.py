def instantiateComponent(rttComponent):

	num = rttComponent.getID()[-1:]
	print("Running RTT" )

	rttMenu = rttComponent.createMenuSymbol(None, None)
	rttMenu.setLabel("Hardware Settings ")
	
	rttPeriodicInterrupt = rttComponent.createBooleanSymbol("rttINCIEN", rttMenu)
	print(rttPeriodicInterrupt)
	rttPeriodicInterrupt.setLabel("Enable Prescale Rollover Interrupt")
	rttPeriodicInterrupt.setDefaultValue(False)
	
	rttAlarm = rttComponent.createBooleanSymbol("rttALMIEN", rttMenu)
	print(rttAlarm)
	rttAlarm.setLabel("Enable Alarm Interrupt")
	rttAlarm.setDefaultValue(False)
	
	rttIndex = rttComponent.createIntegerSymbol("INDEX", rttMenu)
	rttIndex.setVisible(False)
	rttIndex.setDefaultValue(int(num))
	
	rttClkSrc = rttComponent.createBooleanSymbol("rttRTC1HZ", rttMenu)
	print(rttClkSrc)
	rttClkSrc.setLabel("Use RTC 1Hz as clock Source")
	rttClkSrc.setDefaultValue(False)	
	
	rttPrescaleValue = rttComponent.createIntegerSymbol("rttRTPRES", rttMenu)
	rttPrescaleValue.setLabel("Prescalar Value ")
	rttPrescaleValue.setMax(65536)
	rttPrescaleValue.setDefaultValue(32768)
	rttPrescaleValue.setDependencies(rttPrescaleHide, ["rttRTC1HZ"])
	
	rttFreq = rttComponent.createStringSymbol("rttFREQ", rttMenu)
	rttFreq.setLabel("RTT period in seconds")
	rttFreq.setDependencies(rttFreq_cal, ["rttRTC1HZ", "rttRTPRES"])
	rttFreq.setReadOnly(True)
	
	configName = Variables.get("__CONFIGURATION_NAME")

	rttHeader1File = rttComponent.createFileSymbol(None, None)
	rttHeader1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.h.ftl")
	rttHeader1File.setMarkup(True)
	rttHeader1File.setOutputName("plib_rtt" + str(num) + ".h")
	rttHeader1File.setDestPath("/peripheral/rtt/")
	rttHeader1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
	rttHeader1File.setType("HEADER")
	
	rttSource1File = rttComponent.createFileSymbol(None, None)
	rttSource1File.setSourcePath("../peripheral/rtt_6081/templates/plib_rtt.c.ftl")
	rttSource1File.setMarkup(True)
	rttSource1File.setOutputName("plib_rtt" + str(num) + ".c")
	rttSource1File.setDestPath("/peripheral/rtt/")
	rttSource1File.setProjectPath("config/" + configName + "/peripheral/rtt/")
	rttSource1File.setType("SOURCE")
	
	rttSystemInitFile = rttComponent.createFileSymbol(None, None)
	rttSystemInitFile.setType("STRING")
	rttSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
	rttSystemInitFile.setSourcePath("../peripheral/rtt_6081/templates/system/system_initialize.c.ftl")
	rttSystemInitFile.setMarkup(True)

	rttSystemIntFile = rttComponent.createFileSymbol(None, None)
	rttSystemIntFile.setType("STRING")
	rttSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	rttSystemIntFile.setSourcePath("../peripheral/rtt_6081/templates/system/system_interrupt.c.ftl")
	rttSystemIntFile.setMarkup(True)

	rttSystemDefFile = rttComponent.createFileSymbol(None, None)
	rttSystemDefFile.setType("STRING")
	rttSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rttSystemDefFile.setSourcePath("../peripheral/rtt_6081/templates/system/system_definitions.h.ftl")
	rttSystemDefFile.setMarkup(True)

def rttPrescaleHide(rttPrescaleValue,test):
	if test.getValue() == True:
		rttPrescaleValue.setVisible(False)
	else:
		rttPrescaleValue.setVisible(True)
		
def	rttFreq_cal(rttFreq,test):
	data = rttFreq.getComponent()
	rttData = str(float(65536) / 32768)
	rtt1K = data.getSymbolValue("rttRTC1HZ")
	if rtt1K == True:
		rttFreq.setValue("rttFREQ",str(1),2)
	else:
		rttPres = data.getSymbolValue("rttRTPRES")
		if rttPres == 0:
			rttData = str(float(65536) / 32768)
			print str(rttData)
			rttFreq.setValue("rttFREQ",rttData,2)
		else:
			rttData = str(float(rttPres) / 32768)
			print str(rttData)
			rttFreq.setValue("rttFREQ",rttData,2)