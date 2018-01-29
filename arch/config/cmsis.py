def instantiateComponent(cmsisComponent):

	cmsisSupportedVersion = "5.2.0"

	cmsisInformation = cmsisComponent.createCommentSymbol("cmsisInformation", None)
	cmsisError = cmsisComponent.createCommentSymbol("cmsisError", None)
	cmsisError.setLabel("Error: This version of CMSIS Pack is not supported! Supported version is " + cmsisSupportedVersion)
	cmsisError.setVisible(False)

	import xml.etree.ElementTree as ET
	cmsisDescriptionFile = open(Variables.get("__CMSIS_PACK_DIR") + "/ARM.CMSIS.pdsc", "r")
	cmsisDescription = ET.fromstring(cmsisDescriptionFile.read())
	for release in cmsisDescription.iter("release"):
		cmsisInformation.setLabel("Release Information: " + str(release.attrib))
		if release.attrib['version'] != cmsisSupportedVersion:
			print("Error: This version of CMSIS Pack is not supported! Supported version is " + cmsisSupportedVersion)
			cmsisError.setVisible(True)
			return
		break

	#add core header files
	headerFileNames = ["cmsis_compiler.h", "cmsis_gcc.h", "tz_context.h"]

	for headerFileName in headerFileNames:
		headerFile = cmsisComponent.createFileSymbol(None, None)
		headerFile.setRelative(False)
		headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Core/Include/" + headerFileName)
		headerFile.setOutputName(headerFileName)
		headerFile.setMarkup(False)
		headerFile.setOverwrite(True)
		headerFile.setDestPath("../../packs/CMSIS/CMSIS/Core/Include/")
		headerFile.setProjectPath("packs/CMSIS/CMSIS/Core/Include/")
		headerFile.setType("HEADER")

	#add dsp header files
	headerFileNames = ["arm_common_tables.h", "arm_const_structs.h", "arm_math.h"]

	for headerFileName in headerFileNames:
		headerFile = cmsisComponent.createFileSymbol(None, None)
		headerFile.setRelative(False)
		headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/DSP/Include/" + headerFileName)
		headerFile.setOutputName(headerFileName)
		headerFile.setMarkup(False)
		headerFile.setOverwrite(True)
		headerFile.setDestPath("../../packs/CMSIS/CMSIS/DSP/Include/")
		headerFile.setProjectPath("packs/CMSIS/CMSIS/DSP/Include/")
		headerFile.setType("HEADER")
