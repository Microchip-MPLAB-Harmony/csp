def instantiateComponent(dfpComponent):

	dfpDevice = dfpComponent.createCommentSymbol("dfpDevice", None)
	dfpDevice.setLabel("Device: " + Variables.get("__PROCESSOR"))

	dfpVersion = dfpComponent.createCommentSymbol("dfpVersion", None)
	dfpVersion.setLabel("Version: " + "TBD")

	from os import listdir

	headerFileNames = listdir(Variables.get("__DFP_PACK_DIR") + "/mcc/component")

	#add pack files to a project
	for headerFileName in headerFileNames:
		headerFile = dfpComponent.createFileSymbol(None, None)
		headerFile.setRelative(False)
		headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + "/mcc/component/" + headerFileName)
		headerFile.setOutputName(headerFileName)
		headerFile.setMarkup(False)
		headerFile.setOverwrite(True)
		headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/component/")
		headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/component/")
		headerFile.setType("HEADER")

	processorName = Variables.get("__PROCESSOR")

	headerFile = dfpComponent.createFileSymbol(None, None)
	headerFile.setRelative(False)
	headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + "/mcc/" + processorName.lower() + ".h")
	headerFile.setOutputName(processorName.lower() + ".h")
	headerFile.setMarkup(False)
	headerFile.setOverwrite(True)
	headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/")
	headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/")
	headerFile.setType("HEADER")

	headerFile = dfpComponent.createFileSymbol(None, None)
	headerFile.setRelative(False)
	headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + "/mcc/pio/" + processorName.lower() + ".h")
	headerFile.setOutputName(processorName.lower() + ".h")
	headerFile.setMarkup(False)
	headerFile.setOverwrite(True)
	headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/pio/")
	headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/pio/")
	headerFile.setType("HEADER")
