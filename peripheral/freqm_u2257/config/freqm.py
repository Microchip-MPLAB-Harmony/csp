global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global freqmInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateFREQMInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, freqmInstanceName.getValue()+ "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "FREQM_Handler", 2)

def updateFREQMInterruptWarringStatus(symbol, event):

    if freqmSym_INTERRUPTMODE.getValue() == True:
        symbol.setVisible(event["value"])

def updateFREQMREFClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateFREQMMSRClockWarringStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

################################################################################
##########             FREQM DATABASE COMPONENTS           #####################
################################################################################

def instantiateComponent(freqmComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global freqmInstanceName
    global freqmSym_INTERRUPTMODE

    freqmInstanceName = freqmComponent.createStringSymbol("FREQM_INSTANCE_NAME", None)
    freqmInstanceName.setVisible(False)
    freqmInstanceName.setDefaultValue(freqmComponent.getID().upper())
    Log.writeInfoMessage("Running " + freqmInstanceName.getValue())

    #clock enable
    Database.clearSymbolValue("core", freqmInstanceName.getValue()+"_REF_CLOCK_ENABLE")
    Database.setSymbolValue("core", freqmInstanceName.getValue()+"_REF_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", freqmInstanceName.getValue()+"_MSR_CLOCK_ENABLE")
    Database.setSymbolValue("core", freqmInstanceName.getValue()+"_MSR_CLOCK_ENABLE", True, 2)

    #FREQM Interrupt Mode
    freqmSym_INTERRUPTMODE = freqmComponent.createBooleanSymbol("FREQM_INTERRUPT_MODE", None)
    freqmSym_INTERRUPTMODE.setLabel("Enable Interrupt?")
    freqmSym_INTERRUPTMODE.setDescription("Selection of polled or Interrupt Mode")
    freqmSym_INTERRUPTMODE.setDefaultValue(False)

    #Selection of the Reference Clock Cycles
    freqmSym_CFGA_REFNUM = freqmComponent.createIntegerSymbol("REF_CLK_CYCLES", None)
    freqmSym_CFGA_REFNUM.setLabel("Number of Reference Clock Cycles")
    freqmSym_CFGA_REFNUM.setDescription("Duration of measurement in number of ref clock cycles")
    freqmSym_CFGA_REFNUM.setMax(255)
    freqmSym_CFGA_REFNUM.setMin(1)
    freqmSym_CFGA_REFNUM.setDefaultValue(1)

    #Selection of the division for the Reference Clock
    freqmSym_CFGA_DIVREF = freqmComponent.createBooleanSymbol("REF_CLK_DIV", None)
    freqmSym_CFGA_DIVREF.setLabel("Divide reference clock by 8")
    freqmSym_CFGA_DIVREF.setDescription("selection of either refclk1 or refclk8")
    freqmSym_CFGA_DIVREF.setDefaultValue(False)

    #FREQM Setup API
    freqSym_SETUPMODE = freqmComponent.createBooleanSymbol("FREQM_SETUPMODE", None)
    freqSym_SETUPMODE.setLabel("Generate FREQM Setup API ")
    freqSym_SETUPMODE.setDescription("Generation of  API to enable in runtime or not ")
    freqSym_SETUPMODE.setDefaultValue(False)

    freqmSym_Comment = freqmComponent.createCommentSymbol("FREQM_COMMENT",None)
    freqmSym_Comment.setLabel("*** Reference clock must be slower than Measurement clock ***")

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = freqmInstanceName.getValue()+"_INTERRUPT_ENABLE"
    InterruptHandler = freqmInstanceName.getValue()+"_INTERRUPT_HANDLER"
    InterruptHandlerLock = freqmInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = freqmInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    freqmSym_UpdateInterruptStatus = freqmComponent.createBooleanSymbol("FREQM_INTERRUPT_STATUS", None)
    freqmSym_UpdateInterruptStatus.setDependencies(updateFREQMInterruptStatus, ["FREQM_INTERRUPT_MODE"])
    freqmSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    freqmSym_IntEnComment = freqmComponent.createCommentSymbol("FREQM_INTERRUPT_ENABLE_COMMENT", None)
    freqmSym_IntEnComment.setVisible(False)
    freqmSym_IntEnComment.setLabel("Warning!!! FREQM Interrupt is Disabled in Interrupt Manager")
    freqmSym_IntEnComment.setDependencies(updateFREQMInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    freqmSym_REFClkEnComment = freqmComponent.createCommentSymbol("FREQM_REF_CLOCK_ENABLE_COMMENT", None)
    freqmSym_REFClkEnComment.setLabel("Warning!!! FREQM Peripheral Reference Clock is Disabled in Clock Manager")
    freqmSym_REFClkEnComment.setVisible(False)
    freqmSym_REFClkEnComment.setDependencies(updateFREQMREFClockWarringStatus, ["core."+freqmInstanceName.getValue()+"_REF_CLOCK_ENABLE"])

    freqmSym_MSRClkEnComment = freqmComponent.createCommentSymbol("FREQM_MSR_CLOCK_ENABLE_COMMENT", None)
    freqmSym_MSRClkEnComment.setLabel("Warning!!! FREQM Peripheral Measurement Clock is Disabled in Clock Manager")
    freqmSym_MSRClkEnComment.setVisible(False)
    freqmSym_MSRClkEnComment.setDependencies(updateFREQMMSRClockWarringStatus, ["core."+freqmInstanceName.getValue()+"_MSR_CLOCK_ENABLE"])

################################################################################
##########             CODE GENERATION             #############################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    freqmModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FREQM\"]")
    freqmModuleID = freqmModuleNode.getAttribute("id")

    freqmSym_HeaderFile = freqmComponent.createFileSymbol("FREQM_HEADER", None)
    freqmSym_HeaderFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/plib_freqm.h.ftl")
    freqmSym_HeaderFile.setOutputName("plib_"+freqmInstanceName.getValue().lower()+".h")
    freqmSym_HeaderFile.setDestPath("/peripheral/freqm")
    freqmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/freqm")
    freqmSym_HeaderFile.setType("HEADER")
    freqmSym_HeaderFile.setMarkup(True)

    freqmSym_SourceFile = freqmComponent.createFileSymbol("FREQM_SOURCE", None)
    freqmSym_SourceFile.setSourcePath("../peripheral/freqm_"+freqmModuleID+"/templates/plib_freqm.c.ftl")
    freqmSym_SourceFile.setOutputName("plib_"+freqmInstanceName.getValue().lower()+".c")
    freqmSym_SourceFile.setDestPath("/peripheral/freqm")
    freqmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/freqm")
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


