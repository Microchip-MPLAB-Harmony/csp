def instantiateComponent(lcdcComponent):
    configName = Variables.get("__CONFIGURATION_NAME")

    instanceName = lcdcComponent.createStringSymbol("LCDC_INSTANCE_NAME", None)
    instanceName.setReadOnly(True)
    instanceName.setDefaultValue(lcdcComponent.getID().upper())

    #Enable the LCDC clock
    Database.setSymbolValue("core", "LCDC_CLOCK_ENABLE", True, 2)

    #Generate Output Header
    lcdcHeaderFile = lcdcComponent.createFileSymbol("lcdcHeaderFile", None)
    lcdcHeaderFile.setSourcePath("../peripheral/lcdc_11062/templates/plib_lcdc.h.ftl")
    lcdcHeaderFile.setMarkup(True)
    lcdcHeaderFile.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    lcdcHeaderFile.setOverwrite(True)
    lcdcHeaderFile.setDestPath("peripheral/lcdc/")
    lcdcHeaderFile.setProjectPath("config/" + configName + "/peripheral/lcdc/")
    lcdcHeaderFile.setType("HEADER")
    #Generate Output source
    lcdcSourceFile = lcdcComponent.createFileSymbol("lcdcSourceFile", None)
    lcdcSourceFile.setSourcePath("../peripheral/lcdc_11062/templates/plib_lcdc.c.ftl")
    lcdcSourceFile.setMarkup(True)
    lcdcSourceFile.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    lcdcSourceFile.setOverwrite(True)
    lcdcSourceFile.setDestPath("peripheral/lcdc/")
    lcdcSourceFile.setProjectPath("config/" + configName + "/peripheral/lcdc/")
    lcdcSourceFile.setType("SOURCE")

    lcdcSystemDefFile = lcdcComponent.createFileSymbol("lcdcSystemDefFile", None)
    lcdcSystemDefFile.setType("STRING")
    lcdcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    lcdcSystemDefFile.setSourcePath("../peripheral/lcdc_11062/templates/system/system_definitions.h.ftl")
    lcdcSystemDefFile.setMarkup(True)

