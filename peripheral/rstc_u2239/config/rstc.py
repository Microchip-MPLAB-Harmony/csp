###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(rstcComponent):

	rstcInstanceIndex = rstcComponent.getID()[-1:]

	rstcSym_Enable = rstcComponent.createBooleanSymbol("RSTC_ENABLE", None)
	rstcSym_Enable.setLabel("Use Reset Controller ?")
	rstcSym_Enable.setDefaultValue(True)
	rstcSym_Enable.setReadOnly(True)

	#index
	rstcSym_Index = rstcComponent.createIntegerSymbol("RSTC_INDEX", None)
	rstcSym_Index.setDefaultValue(int(rstcInstanceIndex))
	rstcSym_Index.setVisible(False)

	###################################################################################################
	####################################### Code Generation  ##########################################
	###################################################################################################

	configName = Variables.get("__CONFIGURATION_NAME")

	rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
	rstcModuleID = rstcModuleNode.getAttribute("id")

	rstcSym_HeaderFile = rstcComponent.createFileSymbol("RSTC_HEADER", None)
	rstcSym_HeaderFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/plib_rstc.h.ftl")
	rstcSym_HeaderFile.setOutputName("plib_rstc"+rstcInstanceIndex+".h")
	rstcSym_HeaderFile.setDestPath("peripheral/rstc/")
	rstcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
	rstcSym_HeaderFile.setType("HEADER")
	rstcSym_HeaderFile.setMarkup(True)

	rstcSym_SourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
	rstcSym_SourceFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/plib_rstc.c.ftl")
	rstcSym_SourceFile.setOutputName("plib_rstc"+rstcInstanceIndex+".c")
	rstcSym_SourceFile.setDestPath("peripheral/rstc/")
	rstcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
	rstcSym_SourceFile.setType("SOURCE")
	rstcSym_SourceFile.setMarkup(True)

	rstcSym_SystemDefFile = rstcComponent.createFileSymbol("RSTC_SYS_DEF", None)
	rstcSym_SystemDefFile.setType("STRING")
	rstcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	rstcSym_SystemDefFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/system/definitions.h.ftl")
	rstcSym_SystemDefFile.setMarkup(True)
