################################################################################
##############           Callbacks               ###############################
################################################################################

#Divas lead Zero Optimization visible property
def setDLZVisibleProperty(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

################################################################################
##############           DIVAS DATABASE COMPONENTS               ###############
################################################################################

def instantiateComponent(divasComponent):

    num = divasComponent.getID()[-1:]
    Log.writeInfoMessage("Running DIVAS" + str(num))

    #divas main menu
    divasSym_Menu = divasComponent.createBooleanSymbol("DIVAS_MENU", None)
    divasSym_Menu.setLabel("DIVAS MODULE SETTINGS ")

    #divas index
    divasSym_INDEX = divasComponent.createIntegerSymbol("DIVAS_INDEX",divasSym_Menu)
    divasSym_INDEX.setVisible(False)
    divasSym_INDEX.setDefaultValue(int(num))

    #Enable or Disable lead zero optimization
    divasSym_DLZ= divasComponent.createBooleanSymbol("DIVAS_DLZ",divasSym_Menu)
    divasSym_DLZ.setLabel("Enable Leading Zero optimization to reduce division time?")
    divasSym_DLZ.setDescription("Enable/Disable Leading Zero optimization, 32 bit divisions = 2-16 cycles (Enabled)/ 16 cycles (Disabled) ")
    divasSym_DLZ.setVisible(False)
    divasSym_DLZ.setDefaultValue(1)
    divasSym_DLZ.setDependencies(setDLZVisibleProperty, ["DIVAS_MENU"])

################################################################################
###################     Code Generation            #############################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    divasModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DIVAS\"]")
    divasModuleID = divasModuleNode.getAttribute("id")

    divasSym_HeaderFile = divasComponent.createFileSymbol("DIVAS_HEADER", None)
    divasSym_HeaderFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/plib_divas.h.ftl")
    divasSym_HeaderFile.setOutputName("plib_divas" + str(num) +".h")
    divasSym_HeaderFile.setDestPath("peripheral/divas")
    divasSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_HeaderFile.setType("HEADER")
    divasSym_HeaderFile.setMarkup(True)

    divasSym_SourceFile = divasComponent.createFileSymbol("DIVAS_SOURCE", None)
    divasSym_SourceFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/plib_divas.c.ftl")
    divasSym_SourceFile.setOutputName("plib_divas" + str(num) + ".c")
    divasSym_SourceFile.setDestPath("peripheral/divas")
    divasSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_SourceFile.setType("SOURCE")
    divasSym_SourceFile.setMarkup(True)

    divasSystemDefFile = divasComponent.createFileSymbol("DIVAS_SYS_DEF", None)
    divasSystemDefFile.setType("STRING")
    divasSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    divasSystemDefFile.setSourcePath("../peripheral/divas_"+divasModuleID+"/templates/system/definitions.h.ftl")
    divasSystemDefFile.setMarkup(True)




