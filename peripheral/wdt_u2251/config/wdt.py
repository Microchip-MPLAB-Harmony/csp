global wdtInstanceName
global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global wdtSym_Use
global wdtSym_CTRLA_EW

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateWDTInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, wdtInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, "WDT_Handler", 2)

def updateWDTInterruptWarringStatus(symbol, event):

    if wdtSym_CTRLA_EW.getValue() == True and wdtSym_Use.getValue() == True:
        symbol.setVisible(event["value"])

def updateWDTEnarlyInterruptVisibleProperty(symbol, event):

    component = symbol.getComponent()
    component.getSymbolByID("WDT_HEADER").setEnabled(event["value"])
    component.getSymbolByID("WDT_SOURCE").setEnabled(event["value"])
    component.getSymbolByID("WDT_SYS_DEF").setEnabled(event["value"])
    component.getSymbolByID("WDT_SYS_INIT").setEnabled(event["value"])

    symbol.setVisible(event["value"])

    if wdtSym_CTRLA_EW.getValue() == True:
        Database.clearSymbolValue("core", InterruptVector)
        Database.setSymbolValue("core", InterruptVector, event["value"], 2)

        Database.clearSymbolValue("core", InterruptHandlerLock)
        Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

        Database.clearSymbolValue("core", InterruptHandler)

        if event["value"] == True:
            Database.setSymbolValue("core", InterruptHandler, "WDT0_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptHandler, "WDT0_Handler", 2)

    Log.writeInfoMessage("updateWDTEnarlyInterruptVisibleProperty is : " + str(event["value"]))

###################################################################################################
#############################################  WDT  ###############################################
###################################################################################################

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]").getChildren()

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
wdtInstanceName.setDefaultValue(instances[0].getAttribute("name"))

#WDT menu
wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

#WDT Index
wdt_Index = coreComponent.createIntegerSymbol("WDT_INDEX", wdtMenu)
wdt_Index.setVisible(False)
wdt_Index.setDefaultValue(0)

#WDT Use
wdtSym_Use = coreComponent.createBooleanSymbol("WDT_USE", wdtMenu)
wdtSym_Use.setLabel("Use WDT ?")

#Enable Early Interrupt
wdtSym_CTRLA_EW = coreComponent.createBooleanSymbol("WDT_EW_ENABLE", wdtSym_Use)
wdtSym_CTRLA_EW.setLabel("Enable Watchdog Early Interrupt")
wdtSym_CTRLA_EW.setVisible(False)
wdtSym_CTRLA_EW.setDependencies(updateWDTEnarlyInterruptVisibleProperty, ["WDT_USE"])

############################################################################
#### Dependency ####
############################################################################

InterruptVector = wdtInstanceName.getValue() + "_INTERRUPT_ENABLE"
InterruptHandler = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER"
InterruptHandlerLock = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
InterruptVectorUpdate = wdtInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

# Interrupt Dynamic settings
wdtSym_UpdateInterruptStatus = coreComponent.createBooleanSymbol("WDT_INTERRUPT_STATUS", wdtSym_Use)
wdtSym_UpdateInterruptStatus.setDependencies(updateWDTInterruptStatus, ["WDT_EW_ENABLE"])
wdtSym_UpdateInterruptStatus.setVisible(False)

# Interrupt Warning status
wdtSym_IntEnComment = coreComponent.createCommentSymbol("WDT_INTERRUPT_ENABLE_COMMENT", wdtSym_Use)
wdtSym_IntEnComment.setVisible(False)
wdtSym_IntEnComment.setLabel("Warning!!! WDT Interrupt is Disabled in Interrupt Manager")
wdtSym_IntEnComment.setDependencies(updateWDTInterruptWarringStatus, ["core." + InterruptVectorUpdate])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"WDT\"]")
wdtModuleID = wdtModuleNode.getAttribute("id")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_" + wdtModuleID + "/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("/peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(False)

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_" + wdtModuleID + "/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("/peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(False)

wdtSystemInitFile = coreComponent.createFileSymbol("WDT_SYS_INIT", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_" + wdtModuleID + "/templates/system/initialization.c.ftl")
wdtSystemInitFile.setMarkup(True)
wdtSystemInitFile.setEnabled(False)

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_" + wdtModuleID + "/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(False)