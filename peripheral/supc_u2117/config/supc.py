###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateBODVDDOperationModeVisibleProperty(symbol, event):

	symbol.setVisible(event["value"])

	Log.writeInfoMessage("updateBODVDDOperationModeVisibleProperty is : " + str(event["value"]))

def updateBODVDDPrescalerVisibleProperty(symbol, event):

	if(event["value"] == "Sampling Mode"):
		symbol.setVisible(True)
	else:
		symbol.setVisible(False)

	Log.writeInfoMessage("updateBODVDDPrescalerVisibleProperty is : " + str(event["value"]))

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(supcComponent):

	supcInstanceIndex = supcComponent.getID()[-1:]

	#index
	supcSym_Index = supcComponent.createIntegerSymbol("SUPC_INDEX", None)
	supcSym_Index.setDefaultValue(int(supcInstanceIndex))
	supcSym_Index.setVisible(False)

	#interrupt mode
	supcSym_INTENSET = supcComponent.createBooleanSymbol("SUPC_INTERRRUPT_MODE", None)
	supcSym_INTENSET.setLabel("Interrupt Mode")
	supcSym_INTENSET.setDefaultValue(True)
	supcSym_INTENSET.setReadOnly(True)

	#BODVDD RUNSTDBY mode
	supcSym_BODVDD_RUNSTDBY = supcComponent.createBooleanSymbol("SUPC_BODVDD_RUNSTDBY", None)
	supcSym_BODVDD_RUNSTDBY.setLabel("Enable Brown Out Detector in Standby Sleep Mode ?")
	supcSym_BODVDD_RUNSTDBY.setDescription("Configures BODVDD operation in Standby Sleep Mode")

	supcOperationMode = ["Continuous Mode" , "Sampling Mode"]

	#BODVDD STDBYCFG mode
	supcSym_BODVDD_STDBYCFG = supcComponent.createComboSymbol("SUPC_BODVDD_STDBYCFG", supcSym_BODVDD_RUNSTDBY, supcOperationMode)
	supcSym_BODVDD_STDBYCFG.setLabel("Brown Out Detector Operation Mode in Standby Sleep Mode ?")
	supcSym_BODVDD_STDBYCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Standby Sleep mode")
	supcSym_BODVDD_STDBYCFG.setDefaultValue("Continuous Mode")
	supcSym_BODVDD_STDBYCFG.setVisible(False)
	supcSym_BODVDD_STDBYCFG.setDependencies(updateBODVDDOperationModeVisibleProperty , ["SUPC_BODVDD_RUNSTDBY"])

	#BODVDD ACTCFG mode
	supcSym_BODVDD_ACTCFG = supcComponent.createComboSymbol("SUPC_BODVDD_ACTCFG", None, supcOperationMode)
	supcSym_BODVDD_ACTCFG.setLabel("Brown Out Detector Operation Mode in Active Mode ?")
	supcSym_BODVDD_ACTCFG.setDescription("Configures whether BODVDD should operate in continuous or sampling mode in Active mode")
	supcSym_BODVDD_ACTCFG.setDefaultValue("Continuous Mode")

	#BODVDD PSEL
	supcSym_BODVDD_PSEL = supcComponent.createKeyValueSetSymbol("SUPC_BODVDD_PSEL", None)
	supcSym_BODVDD_PSEL.setLabel("Brown Out Detector Sampling Mode Clock Prescaler")
	supcSym_BODVDD_PSEL.setDescription("Configures the sampling clock prescaler when BODVDD is operating in sampling mode")
	supcSym_BODVDD_PSEL.setVisible(False)
	supcSym_BODVDD_PSEL.setDependencies(updateBODVDDPrescalerVisibleProperty , ["SUPC_BODVDD_STDBYCFG" , "SUPC_BODVDD_ACTCFG"])

	supcBODVDDPselNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_BODVDD__PSEL\"]")
	supcBODVDDPselValues = []
	supcBODVDDPselValues = supcBODVDDPselNode.getChildren()

	supcBODVDDPselDefaultValue = 0

	for index in range (0 , len(supcBODVDDPselValues)):
		supcBODVDDPselKeyName = supcBODVDDPselValues[index].getAttribute("name")

		if (supcBODVDDPselKeyName == "DIV2"):
			supcBODVDDPselDefaultValue = index

		supcBODVDDPselKeyDescription = supcBODVDDPselValues[index].getAttribute("caption")
		supcBODVDDPselKeyValue =  supcBODVDDPselValues[index].getAttribute("value")
		supcSym_BODVDD_PSEL.addKey(supcBODVDDPselKeyName , supcBODVDDPselKeyValue , supcBODVDDPselKeyDescription)

	supcSym_BODVDD_PSEL.setDefaultValue(supcBODVDDPselDefaultValue)
	supcSym_BODVDD_PSEL.setOutputMode("Key")
	supcSym_BODVDD_PSEL.setDisplayMode("Description")

	supcVREGOperationMode = ["Low Power Operation" , "Normal Operation"]

	#VREG RUNSTDBY mode
	supcSym_VREG_RUNSTDBY = supcComponent.createComboSymbol("SUPC_VREG_RUNSTDBY", None, supcVREGOperationMode)
	supcSym_VREG_RUNSTDBY.setLabel("Voltage Regulator mode in Standby Sleep ?")
	supcSym_VREG_RUNSTDBY.setDescription("Configures VREG operation in Standby Sleep Mode")
	supcSym_VREG_RUNSTDBY.setDefaultValue("Low Power Operation")

	#VREF selection
	supcSym_VREF_SEL = supcComponent.createKeyValueSetSymbol("SUPC_VREF_SEL", None)
	supcSym_VREF_SEL.setLabel("VREF Voltage Level (for ADC, SDADC and DAC) ?")
	supcSym_VREF_SEL.setDescription("Configures VREF voltage level")

	supcVREFSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]/value-group@[name=\"SUPC_VREF__SEL\"]")
	supcVREFSelectionValues = []
	supcVREFSelectionValues = supcVREFSelectionNode.getChildren()

	supcVREFSelectionDefaultValue = 0

	for index in range (0 , len(supcVREFSelectionValues)):
		supcVREFSelectionKeyName = supcVREFSelectionValues[index].getAttribute("name")

		if (supcVREFSelectionKeyName == "1V024"):
			supcVREFSelectionDefaultValue = index

		supcVREFSelectionKeyDescription = supcVREFSelectionValues[index].getAttribute("caption")
		supcVREFSelectionKeyValue =  supcVREFSelectionValues[index].getAttribute("value")
		supcSym_VREF_SEL.addKey(supcVREFSelectionKeyName , supcVREFSelectionKeyValue , supcVREFSelectionKeyDescription)

	supcSym_VREF_SEL.setDefaultValue(supcVREFSelectionDefaultValue)
	supcSym_VREF_SEL.setOutputMode("Key")
	supcSym_VREF_SEL.setDisplayMode("Description")

	supcVREFOperationModeONDEMAND = ["Always Available" , "Only on Peripheral Request"]

	#VREF ONDEMAND mode
	supcSym_VREF_ONDEMAND = supcComponent.createComboSymbol("SUPC_VREF_ONDEMAND", None, supcVREFOperationModeONDEMAND)
	supcSym_VREF_ONDEMAND.setLabel("VREF Availability")
	supcSym_VREF_ONDEMAND.setDescription("Configures the VREF On Demand behavior")
	supcSym_VREF_ONDEMAND.setDefaultValue("Always Available")

	supcVREFOperationModeRUNSTDBY = ["Disable in Standby Sleep" , "Available in Standby Sleep"]

	#VREF RUNSTDBY mode
	supcSym_VREF_RUNSTDBY = supcComponent.createComboSymbol("SUPC_VREF_RUNSTDBY", None, supcVREFOperationModeRUNSTDBY)
	supcSym_VREF_RUNSTDBY.setLabel("Voltage Reference Available in Standby Sleep ?")
	supcSym_VREF_RUNSTDBY.setDescription("Configures VREF operation in Standby Sleep Mode")
	supcSym_VREG_RUNSTDBY.setDefaultValue("Disable in Standby Sleep")

	#VREF VREFOE mode
	supcSym_VREF_VREFOE = supcComponent.createBooleanSymbol("SUPC_VREF_VREFOE", None)
	supcSym_VREF_VREFOE.setLabel("Connect VREF to ADC Channel ?")
	supcSym_VREF_VREFOE.setDescription("Configures VREF availability to ADC input")

	###################################################################################################
	####################################### Code Generation  ##########################################
	###################################################################################################

	configName = Variables.get("__CONFIGURATION_NAME")

	supcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SUPC\"]")
	supcModuleID = supcModuleNode.getAttribute("id")

	supcSym_HeaderFile = supcComponent.createFileSymbol("SUPC_HEADER", None)
	supcSym_HeaderFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/plib_supc.h.ftl")
	supcSym_HeaderFile.setOutputName("plib_supc"+supcInstanceIndex+".h")
	supcSym_HeaderFile.setDestPath("peripheral/supc/")
	supcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
	supcSym_HeaderFile.setType("HEADER")
	supcSym_HeaderFile.setMarkup(True)

	supcSym_SourceFile = supcComponent.createFileSymbol("SUPC_SOURCE", None)
	supcSym_SourceFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/plib_supc.c.ftl")
	supcSym_SourceFile.setOutputName("plib_supc"+supcInstanceIndex+".c")
	supcSym_SourceFile.setDestPath("peripheral/supc/")
	supcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
	supcSym_SourceFile.setType("SOURCE")
	supcSym_SourceFile.setMarkup(True)

	supcSym_SystemInitFile = supcComponent.createFileSymbol("SUPC_SYS_INT", None)
	supcSym_SystemInitFile.setType("STRING")
	supcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	supcSym_SystemInitFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/system/initialization.c.ftl")
	supcSym_SystemInitFile.setMarkup(True)

	supcSym_SystemDefFile = supcComponent.createFileSymbol("SUPC_SYS_DEF", None)
	supcSym_SystemDefFile.setType("STRING")
	supcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	supcSym_SystemDefFile.setSourcePath("../peripheral/supc_"+supcModuleID+"/templates/system/definitions.h.ftl")
	supcSym_SystemDefFile.setMarkup(True)
