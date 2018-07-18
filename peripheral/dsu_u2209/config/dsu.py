################################################################################
#############             DSU DATABASE COMPONENTS         ######################
################################################################################

def instantiateComponent(dsuComponent):

    dsuInstanceIndex = dsuComponent.getID()[-1:]
    Log.writeInfoMessage("Running DSU" + str(dsuInstanceIndex))

    #dsu main menu
    dsuSym_Menu = dsuComponent.createBooleanSymbol("DSU_MENU", None)
    dsuSym_Menu.setLabel("DSU MODULE SETTINGS ")
    dsuSym_Menu.setVisible(False)
    dsuSym_Menu.setDefaultValue(True)

    dsuSym_Comment = dsuComponent.createCommentSymbol(None, None)
    dsuSym_Comment.setLabel("*** This component does not contain any configuration settings ***")

    dsuSym_INDEX = dsuComponent.createIntegerSymbol("DSU_INDEX",dsuSym_Menu)
    dsuSym_INDEX.setDefaultValue(int(dsuInstanceIndex))
    dsuSym_INDEX.setVisible(False)

################################################################################
#############             CODE GENERATION             ##########################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    dsuModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DSU\"]")
    dsuModuleID = dsuModuleNode.getAttribute("id")

    dsuSym_HeaderFile = dsuComponent.createFileSymbol("DSU_HEADER", None)
    dsuSym_HeaderFile.setSourcePath("../peripheral/dsu_"+dsuModuleID+"/templates/plib_dsu.h.ftl")
    dsuSym_HeaderFile.setOutputName("plib_dsu" + str(dsuInstanceIndex) + ".h")
    dsuSym_HeaderFile.setDestPath("peripheral/dsu/")
    dsuSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/dsu/")
    dsuSym_HeaderFile.setType("HEADER")
    dsuSym_HeaderFile.setMarkup(True)

    dsuSym_SourceFile = dsuComponent.createFileSymbol("DSU_SOURCE", None)
    dsuSym_SourceFile.setSourcePath("../peripheral/dsu_"+dsuModuleID+"/templates/plib_dsu.c.ftl")
    dsuSym_SourceFile.setOutputName("plib_dsu" + str(dsuInstanceIndex) + ".c")
    dsuSym_SourceFile.setDestPath("peripheral/dsu/")
    dsuSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/dsu/")
    dsuSym_SourceFile.setType("SOURCE")
    dsuSym_SourceFile.setMarkup(True)

    dsuSystemDefFile = dsuComponent.createFileSymbol("DSU_SYS_DEF", None)
    dsuSystemDefFile.setType("STRING")
    dsuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dsuSystemDefFile.setSourcePath("../peripheral/dsu_"+dsuModuleID+"/templates/system/definitions.h.ftl")
    dsuSystemDefFile.setMarkup(True)
