Log.writeInfoMessage("Loading RSWDT for " + Variables.get("__PROCESSOR"))

global rswdtinterruptVector
global rswdtinterruptHandler
global rswdtinterruptHandlerLock

rswdtMenu = coreComponent.createMenuSymbol("RSWDT_MENU_0", None)
rswdtMenu.setLabel("RSWDT")

rswdtEnable = coreComponent.createBooleanSymbol("rswdtENABLE", rswdtMenu)
rswdtEnable.setLabel("Enable Reinforced Safety Watchdog Timer (RSWDT)?")
rswdtEnable.setDefaultValue(False)

def rswdtEnableCfgMenu(rswdtCfgMenu, event):
    rswdtCfgMenu.setVisible(event["value"])

    component = rswdtCfgMenu.getComponent()
    component.getSymbolByID("rswdtHeaderFile").setEnabled(event["value"])
    component.getSymbolByID("rswdtSourceFile").setEnabled(event["value"])
    component.getSymbolByID("rswdtSystemDefFile").setEnabled(event["value"])

rswdtCfgMenu = coreComponent.createMenuSymbol("RSWDT_MENU_1", rswdtMenu)
rswdtCfgMenu.setLabel("RSWDT Configuration")
rswdtCfgMenu.setDependencies(rswdtEnableCfgMenu, ["rswdtENABLE"])
rswdtCfgMenu.setVisible(False)

rswdtReset = coreComponent.createBooleanSymbol("rswdtEnableReset", rswdtCfgMenu)
rswdtReset.setLabel("Enable Reset")
rswdtReset.setDefaultValue(True)

def rswdtResetEnable(rswdtInterrupt,event):
    if event["value"] == True:
        rswdtInterrupt.setVisible(False)
        rswdtInterrupt.setValue(False,2)
    else:
        rswdtInterrupt.setVisible(True)

rswdtInterrupt = coreComponent.createBooleanSymbol("rswdtinterruptMode", rswdtCfgMenu)
rswdtInterrupt.setLabel("Enable Interrupts")
rswdtInterrupt.setDefaultValue(False)
rswdtInterrupt.setDependencies(rswdtResetEnable, ["rswdtEnableReset"])
rswdtInterrupt.setVisible(False)

rswdtCounterValue = coreComponent.createIntegerSymbol("rswdtWDV", rswdtCfgMenu)
rswdtCounterValue.setLabel("Counter value")
rswdtCounterValue.setMax(0xfff)
rswdtCounterValue.setDefaultValue(0xfff)

def rswdtcounter_cal(rswdtCounterValueTime, event):
    data = event["value"] * 3.90625
    rswdtCounterValueTime.setValue(int(round(data)),2)

rswdtCounterValueTime = coreComponent.createIntegerSymbol("rswdtWDVTIME", rswdtCfgMenu)
rswdtCounterValueTime.setLabel("Counter value in ms")
rswdtCounterValueTime.setDependencies(rswdtcounter_cal, ["rswdtWDV"])
rswdtCounterValueTime.setReadOnly(True)
rswdtCounterValueTime.setDefaultValue(15996)

rswdtDebugHalt = coreComponent.createBooleanSymbol("rswdtdebugHalt", rswdtCfgMenu)
rswdtDebugHalt.setLabel("Enable Debug halt")
rswdtDebugHalt.setDefaultValue(False)

rswdtIndex = coreComponent.createIntegerSymbol("rswdtIndex", rswdtCfgMenu)
rswdtIndex.setVisible(False)
rswdtIndex.setDefaultValue(0)

rswdtIdleHalt = coreComponent.createBooleanSymbol("rswdtidleHalt", rswdtCfgMenu)
rswdtIdleHalt.setLabel("Enable Idle halt")
rswdtIdleHalt.setDefaultValue(False)

rswdtinterruptVector = "RSWDT_INTERRUPT_ENABLE"
rswdtinterruptHandler = "RSWDT_INTERRUPT_HANDLER"
rswdtinterruptHandlerLock = "RSWDT_INTERRUPT_HANDLER_LOCK"

Database.clearSymbolValue("core", rswdtinterruptVector)
Database.setSymbolValue("core", rswdtinterruptVector, False, 2)
Database.clearSymbolValue("core", rswdtinterruptHandler)
Database.setSymbolValue("core", rswdtinterruptHandler, "RSWDT_Handler", 2)
Database.clearSymbolValue("core", rswdtinterruptHandlerLock)
Database.setSymbolValue("core", rswdtinterruptHandlerLock, False, 2)

def interruptControl(NVIC, event):
    global rswdtinterruptVector
    global rswdtinterruptHandler
    Database.clearSymbolValue("core", rswdtinterruptVector)
    Database.clearSymbolValue("core", rswdtinterruptHandler)
    Database.clearSymbolValue("core", rswdtinterruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", rswdtinterruptVector, True, 2)
        Database.setSymbolValue("core", rswdtinterruptHandler, "RSWDT0_InterruptHandler", 2)
        Database.setSymbolValue("core", rswdtinterruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", rswdtinterruptVector, False, 2)
        Database.setSymbolValue("core", rswdtinterruptHandler, "RSWDT_Handler", 2)
        Database.setSymbolValue("core", rswdtinterruptHandlerLock, False, 2)

# NVIC Dynamic settings
rswdtinterruptControl = coreComponent.createBooleanSymbol("NVIC_RSWDT_ENABLE", None)
rswdtinterruptControl.setDependencies(interruptControl, ["rswdtinterruptMode"])
rswdtinterruptControl.setVisible(False)

configName = Variables.get("__CONFIGURATION_NAME")

rswdtHeaderFile = coreComponent.createFileSymbol("rswdtHeaderFile", None)
rswdtHeaderFile.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.h.ftl")
rswdtHeaderFile.setOutputName("plib_rswdt0.h")
rswdtHeaderFile.setDestPath("peripheral/rswdt/")
rswdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/rswdt/")
rswdtHeaderFile.setType("HEADER")
rswdtHeaderFile.setMarkup(True)
rswdtHeaderFile.setEnabled(False)

rswdtSourceFile = coreComponent.createFileSymbol("rswdtSourceFile", None)
rswdtSourceFile.setSourcePath("../peripheral/rswdt_11110/templates/plib_rswdt.c.ftl")
rswdtSourceFile.setOutputName("plib_rswdt0.c")
rswdtSourceFile.setDestPath("peripheral/rswdt/")
rswdtSourceFile.setProjectPath("config/" + configName + "/peripheral/rswdt/")
rswdtSourceFile.setType("SOURCE")
rswdtSourceFile.setMarkup(True)
rswdtSourceFile.setEnabled(False)

rswdtSystemInitFile = coreComponent.createFileSymbol("rswdtSystemInitFile", None)
rswdtSystemInitFile.setType("STRING")
rswdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
rswdtSystemInitFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_initialize.c.ftl")
rswdtSystemInitFile.setMarkup(True)

rswdtSystemDefFile = coreComponent.createFileSymbol("rswdtSystemDefFile", None)
rswdtSystemDefFile.setType("STRING")
rswdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
rswdtSystemDefFile.setSourcePath("../peripheral/rswdt_11110/templates/system/system_definitions.h.ftl")
rswdtSystemDefFile.setMarkup(True)
rswdtSystemDefFile.setEnabled(False)
