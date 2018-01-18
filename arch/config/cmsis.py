def instantiateComponent(cmsisComponent):

	cmsisVersion = cmsisComponent.createCommentSymbol("cmsisVersion", None)
	cmsisVersion.setLabel("Version: " + "TBD")

	headerFileNames = ["cmsis_compiler.h", "cmsis_gcc.h", "tz_context.h", "arm_common_tables.h", "arm_const_structs.h", "arm_math.h"]

	for headerFileName in headerFileNames:
		headerFile = cmsisComponent.createFileSymbol(None, None)
		headerFile.setRelative(False)
		headerFile.setSourcePath(Variables.get("__CMSIS_PACK_DIR") + "/CMSIS/Include/" + headerFileName)
		headerFile.setOutputName(headerFileName)
		headerFile.setMarkup(False)
		headerFile.setOverwrite(True)
		headerFile.setDestPath("../../packs/CMSIS/CMSIS/Include/")
		headerFile.setProjectPath("packs/CMSIS/CMSIS/Include/")
		headerFile.setType("HEADER")
