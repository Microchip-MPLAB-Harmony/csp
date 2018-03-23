def instantiateComponent(dfpComponent):

	from os import listdir
	import xml.etree.ElementTree as ET

	MCC_HEADERS_SUBPATH = "/include_mcc"

	dfpDevice = dfpComponent.createCommentSymbol("dfpDevice", None)
	dfpDevice.setLabel("Device: " + Variables.get("__PROCESSOR"))

    #get pack information
	dfpInformation = dfpComponent.createCommentSymbol("dfpInformation", None)

	dfpFiles = listdir(Variables.get("__DFP_PACK_DIR"))
	dfpInfoFound = False
	for dfpFile in dfpFiles:
		if dfpFile.find(".pdsc") != -1:
			dfpDescriptionFile = open(Variables.get("__DFP_PACK_DIR") + "/" + dfpFile, "r")
			dfpDescription = ET.fromstring(dfpDescriptionFile.read())
			dfpInfoFound = True
			for release in dfpDescription.iter("release"):
				dfpInformation.setLabel("Release Information: " + str(release.attrib))
				break

	if dfpInfoFound == False:
		dfpFiles = listdir(Variables.get("__DFP_PACK_DIR")+"/..")
		for dfpFile in dfpFiles:
			if dfpFile.find(".pdsc") != -1:
				dfpDescriptionFile = open(Variables.get("__DFP_PACK_DIR") + "/../" + dfpFile, "r")
				dfpDescription = ET.fromstring(dfpDescriptionFile.read())
				for release in dfpDescription.iter("release"):
					dfpInformation.setLabel("Release Information: " + str(release.attrib))
					break

    #add pack files to a project
	headerFileNames = listdir(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component")

	for headerFileName in headerFileNames:
		szSymbol = "PART_PERIPH_{}_DEFS".format(headerFileName[:-2].upper())
		headerFile = dfpComponent.createFileSymbol(szSymbol, None)
		headerFile.setRelative(False)
		headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/component/" + headerFileName)
		headerFile.setOutputName(headerFileName)
		headerFile.setMarkup(False)
		headerFile.setOverwrite(True)
		headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/component/")
		headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/component/")
		headerFile.setType("HEADER")

	processorName = Variables.get("__PROCESSOR")

	headerFile = dfpComponent.createFileSymbol("PART_MAIN_DEFS", None)
	headerFile.setRelative(False)
	headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/" + processorName.lower() + ".h")
	headerFile.setOutputName(processorName.lower() + ".h")
	headerFile.setMarkup(False)
	headerFile.setOverwrite(True)
	headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/")
	headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/")
	headerFile.setType("HEADER")

	headerFile = dfpComponent.createFileSymbol("PART_IO_DEFS", None)
	headerFile.setRelative(False)
	headerFile.setSourcePath(Variables.get("__DFP_PACK_DIR") + MCC_HEADERS_SUBPATH + "/pio/" + processorName.lower() + ".h")
	headerFile.setOutputName(processorName.lower() + ".h")
	headerFile.setMarkup(False)
	headerFile.setOverwrite(True)
	headerFile.setDestPath("../../packs/" + Variables.get("__PROCESSOR") + "_DFP/pio/")
	headerFile.setProjectPath("packs/" + Variables.get("__PROCESSOR") + "_DFP/pio/")
	headerFile.setType("HEADER")
