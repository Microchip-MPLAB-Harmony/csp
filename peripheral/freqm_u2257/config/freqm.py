################################################################################
##########             FREQM DATABASE COMPONENTS           #####################
################################################################################
def instantiateComponent(freqmComponent):

    freqmInstanceIndex = freqmComponent.getID()[-1:]
    Log.writeInfoMessage("Running FREQM" + str(freqmInstanceIndex))

    #FREQM Main Menu
    freqmSym_Menu = freqmComponent.createBooleanSymbol("FREQM_MENU", None)
    freqmSym_Menu.setLabel("FREQM MODULE SETTINGS ")

    freqmSym_Comment = freqmComponent.createCommentSymbol("FREQM_COMMENT",freqmSym_Menu)
    freqmSym_Comment.setLabel("*** The reference clock must be slower than the measurement clock ***")

    #FREQM Index
    freqmSym_INDEX = freqmComponent.createIntegerSymbol("FREQM_INDEX",freqmSym_Menu)
    freqmSym_INDEX.setVisible(False)
    freqmSym_INDEX.setDefaultValue(int(freqmInstanceIndex))

    #FREQM Setup API
    freqSym_SETUPMODE = freqmComponent.createBooleanSymbol("FREQM_SETUPMODE", freqmSym_Menu)
    freqSym_SETUPMODE.setLabel("Generate FREQM Setup API ")
    freqSym_SETUPMODE.setDescription("Selection of the API to enable in runtime or not ")
    freqSym_SETUPMODE.setDefaultValue(False)

    #FREQM Interrupt Mode
    freqSym_INTERRUPTMODE = freqmComponent.createBooleanSymbol("FREQM_INTERRUPT_MODE", freqmSym_Menu)
    freqSym_INTERRUPTMODE.setLabel("Enable Interrupt?")
    freqSym_INTERRUPTMODE.setDescription("Selection of the polled or Interrupt Mode ")
    freqSym_INTERRUPTMODE.setDefaultValue(False)

    #Selection of the Reference Clock Cycles
    freqmSym_CFGA_REFNUM = freqmComponent.createIntegerSymbol("REF_CLK_CYCLES", freqmSym_Menu)
    freqmSym_CFGA_REFNUM.setLabel("Number of the Reference Clock Cycles")
    freqmSym_CFGA_REFNUM.setDescription("selection of the freqmInstanceIndexber of ref clock cycles required")
    freqmSym_CFGA_REFNUM.setMax(255)
    freqmSym_CFGA_REFNUM.setMin(1)
    freqmSym_CFGA_REFNUM.setDefaultValue(1)

    #Selection of the division for the Reference Clock
    freqmSym_CFGA_DIVREF = freqmComponent.createBooleanSymbol("REF_CLK_DIV", freqmSym_Menu)
    freqmSym_CFGA_DIVREF.setLabel("Divide reference clock by 8")
    freqmSym_CFGA_DIVREF.setDescription("selection of either refclk1 or refclk8")
    freqmSym_CFGA_DIVREF.setDefaultValue(False)

################################################################################
##########             CODE GENERATION             #############################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    freqmModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FREQM\"]")
    freqmModuleID = freqmModuleNode.getAttribute("id")

    freqmSym_HeaderFile = freqmComponent.createFileSymbol("FREQM_HEADER", None)
    freqmSym_HeaderFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/plib_freqm.h.ftl")
    freqmSym_HeaderFile.setOutputName("plib_freqm"+str(freqmInstanceIndex)+".h")
    freqmSym_HeaderFile.setDestPath("peripheral/freqm")
    freqmSym_HeaderFile.setProjectPath("config/" + configName + "peripheral/freqm")
    freqmSym_HeaderFile.setType("HEADER")
    freqmSym_HeaderFile.setMarkup(True)

    freqmSym_SourceFile = freqmComponent.createFileSymbol("FREQM_SOURCE", None)
    freqmSym_SourceFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/plib_freqm.c.ftl")
    freqmSym_SourceFile.setOutputName("plib_freqm"+str(freqmInstanceIndex)+".c")
    freqmSym_SourceFile.setDestPath("peripheral/freqm")
    freqmSym_SourceFile.setProjectPath("config/" + configName + "peripheral/freqm")
    freqmSym_SourceFile.setType("SOURCE")
    freqmSym_SourceFile.setMarkup(True)

    freqmSystemInitFile = freqmComponent.createFileSymbol("FREQM_SYS_INIT", None)
    freqmSystemInitFile.setType("STRING")
    freqmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    freqmSystemInitFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/system/initialization.c.ftl")
    freqmSystemInitFile.setMarkup(True)

    freqmSystemDefFile = freqmComponent.createFileSymbol("FREQM_SYS_DEF", None)
    freqmSystemDefFile.setType("STRING")
    freqmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    freqmSystemDefFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/system/definitions.h.ftl")
    freqmSystemDefFile.setMarkup(True)


