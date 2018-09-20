################################################################################
##############           Callbacks               ###############################
################################################################################

def updateDIVASClockWarringStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

################################################################################
##############           DIVAS DATABASE COMPONENTS               ###############
################################################################################

def instantiateComponent(divasComponent):

    divasInstanceName = divasComponent.createStringSymbol("DIVAS_INSTANCE_NAME", None)
    divasInstanceName.setVisible(False)
    divasInstanceName.setDefaultValue(divasComponent.getID().upper())
    Log.writeInfoMessage("Running " + divasInstanceName.getValue())

    #clock enable
    Database.clearSymbolValue("core", divasInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", divasInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    #Enable or Disable lead zero optimization
    divasSym_DLZ = divasComponent.createBooleanSymbol("DIVAS_DLZ", None)
    divasSym_DLZ.setLabel("Enable Leading Zero optimization to reduce division time?")
    divasSym_DLZ.setDescription("32 bit divisions take 2-16 cycles when enabled; 16 cycles when disabled")
    divasSym_DLZ.setVisible(True)
    divasSym_DLZ.setDefaultValue(1)

    # Clock Warning status
    divasSym_ClkEnComment = divasComponent.createCommentSymbol("DIVAS_CLOCK_ENABLE_COMMENT", None)
    divasSym_ClkEnComment.setLabel("Warning!!! DIVAS Peripheral Clock is Disabled in Clock Manager")
    divasSym_ClkEnComment.setVisible(False)
    divasSym_ClkEnComment.setDependencies(updateDIVASClockWarringStatus, ["core."+divasInstanceName.getValue()+"_CLOCK_ENABLE"])

################################################################################
###################     Code Generation            #############################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    divasModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DIVAS\"]")
    divasModuleID = divasModuleNode.getAttribute("id")

    divasSym_HeaderFile = divasComponent.createFileSymbol("DIVAS_HEADER", None)
    divasSym_HeaderFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/plib_divas.h.ftl")
    divasSym_HeaderFile.setOutputName("plib_"+divasInstanceName.getValue().lower()+".h")
    divasSym_HeaderFile.setDestPath("peripheral/divas")
    divasSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_HeaderFile.setType("HEADER")
    divasSym_HeaderFile.setMarkup(True)

    divasSym_SourceFile = divasComponent.createFileSymbol("DIVAS_SOURCE", None)
    divasSym_SourceFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/plib_divas.c.ftl")
    divasSym_SourceFile.setOutputName("plib_"+divasInstanceName.getValue().lower()+".c")
    divasSym_SourceFile.setDestPath("peripheral/divas")
    divasSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_SourceFile.setType("SOURCE")
    divasSym_SourceFile.setMarkup(True)

    divasSystemDefFile = divasComponent.createFileSymbol("DIVAS_SYS_DEF", None)
    divasSystemDefFile.setType("STRING")
    divasSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    divasSystemDefFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/system/definitions.h.ftl")
    divasSystemDefFile.setMarkup(True)

    divasSystemInitFile = divasComponent.createFileSymbol("DIVAS_SYS_INIT", None)
    divasSystemInitFile.setType("STRING")
    divasSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    divasSystemInitFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/system/initialization.c.ftl")
    divasSystemInitFile.setMarkup(True)




