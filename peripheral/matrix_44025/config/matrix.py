Log.writeInfoMessage("Loading Matrix for " + Variables.get("__PROCESSOR"))

configName = Variables.get("__CONFIGURATION_NAME")

matrixFile = coreComponent.createFileSymbol("MATRIX_C", None)
matrixFile.setSourcePath("../peripheral/matrix_44025/templates/plib_matrix.c")
matrixFile.setOutputName("plib_matrix.c")
matrixFile.setDestPath("peripheral/matrix/")
matrixFile.setProjectPath("config/" + configName + "/peripheral/matrix/")
matrixFile.setType("SOURCE")
matrixFile.setMarkup(False)

matrixHeader = coreComponent.createFileSymbol("MATRIX_H", None)
matrixHeader.setSourcePath("../peripheral/matrix_44025/templates/plib_matrix.h")
matrixHeader.setOutputName("plib_matrix.h")
matrixHeader.setDestPath("peripheral/matrix/")
matrixHeader.setProjectPath("config/" + configName + "/peripheral/matrix/")
matrixHeader.setType("HEADER")
matrixHeader.setMarkup(False)

matrixSystemInitFile = coreComponent.createFileSymbol("matrixSystemInitFile", None)
matrixSystemInitFile.setType("STRING")
matrixSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
matrixSystemInitFile.setSourcePath("../peripheral/matrix_44025/templates/system/initialization.c.ftl")
matrixSystemInitFile.setMarkup(True)

matrixSystemDefFile = coreComponent.createFileSymbol("matrixSystemDefFile", None)
matrixSystemDefFile.setType("STRING")
matrixSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
matrixSystemDefFile.setSourcePath("../peripheral/matrix_44025/templates/system/definitions.h.ftl")
matrixSystemDefFile.setMarkup(True)

