#Function for initiating the UI
def instantiateComponent(rtccComponent):

	print("Running RTCC")
	#Create the top menu
	rtccMenu = rtccComponent.createMenuSymbol(None, None)
	rtccMenu.setLabel("Hardware Settings ")
	#Create a Checkbox to enable disable interrupts
	rtccInterrupt = rtccComponent.createBooleanSymbol("rtccEnableInterrupt", rtccMenu)
	print(rtccInterrupt)
	rtccInterrupt.setLabel("Enable Alarm")
	rtccInterrupt.setDefaultValue(True)
	
	#Generate Output Header
	rtccHeaderFile = rtccComponent.createFileSymbol(None, None)
	rtccHeaderFile.setSourcePath("../peripheral/rtcc_6056/templates/plib_rtcc.h.ftl")
	rtccHeaderFile.setOutputName("plib_rtcc.h")
	rtccHeaderFile.setOverwrite(True)
	rtccHeaderFile.setDestPath("peripheral/rtcc/")
	rtccHeaderFile.setProjectPath("peripheral/rtcc/")
	rtccHeaderFile.setType("HEADER")
	#Generate Output source
	rtccSourceFile = rtccComponent.createFileSymbol(None, None)
	rtccSourceFile.setSourcePath("../peripheral/rtcc_6056/templates/plib_rtcc.c.ftl")
	rtccSourceFile.setOutputName("plib_rtcc.c")
	rtccSourceFile.setOverwrite(True)
	rtccSourceFile.setDestPath("peripheral/rtcc/")
	rtccSourceFile.setProjectPath("peripheral/rtcc/")
	rtccSourceFile.setType("SOURCE")

