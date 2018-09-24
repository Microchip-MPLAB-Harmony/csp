def calcPIV(period_ms):
    clk_freq = int(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    clk_freq = clk_freq / 16;

    return int(period_ms * clk_freq / 1000)

def updatePIV(symbol, event):
    period = symbol.getComponent().getSymbolValue("PERIOD_MS")
    piv = calcPIV(period)
    symbol.setValue(piv, 1)

def instantiateComponent(pitComponent):
    instanceName = pitComponent.createStringSymbol("PERIPH_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(pitComponent.getID().upper())

    enable = pitComponent.createBooleanSymbol("ENABLE_COUNTER", None)
    enable.setLabel("Enable Counter")
    enable.setDefaultValue(True)

    useInterrupt = pitComponent.createBooleanSymbol("USE_INTERRUPT", None)
    useInterrupt.setLabel("Interrupt Mode")
    useInterrupt.setDefaultValue(True)

    interrupt = pitComponent.createBooleanSymbol("ENABLE_INTERRUPT", useInterrupt)
    interrupt.setLabel("Enable Interrupt")
    interrupt.setDefaultValue(True)
    interrupt.setDependencies(lambda symbol, event: symbol.setVisible(event["value"]), ["USE_INTERRUPT"])

    Database.clearSymbolValue("core", "PIT_INTERRUPT_ENABLE")
    Database.setSymbolValue("core", "PIT_INTERRUPT_ENABLE", True, 2)
    Database.clearSymbolValue("core", "PIT_INTERRUPT_HANDLER")
    Database.setSymbolValue("core", "PIT_INTERRUPT_HANDLER", "PIT_InterruptHandler", 2)

    period = pitComponent.createFloatSymbol("PERIOD_MS", None)
    period.setLabel("Period (ms)")
    period.setMax(101.06)
    period.setMin(0)
    period.setDefaultValue(100.0)

    piv = calcPIV(period.getValue())
    piv_sym = pitComponent.createIntegerSymbol("PERIOD_TICKS", None)
    piv_sym.setLabel("Period")
    piv_sym.setDefaultValue(piv)
    piv_sym.setReadOnly(True)
    piv_sym.setDependencies(updatePIV,["PERIOD_MS", "core.PCLOCK_LS_CLOCK_FREQUENCY"])

    configName = Variables.get("__CONFIGURATION_NAME")

    File = pitComponent.createFileSymbol("PIT_HEADER", None)
    File.setSourcePath("../peripheral/pit_6079/templates/plib_pit.h.ftl")
    File.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    File.setDestPath("peripheral/pit/")
    File.setProjectPath("config/"+configName+"/peripheral/pit/")
    File.setType("HEADER")
    File.setMarkup(True)

    File = pitComponent.createFileSymbol("PIT_SRC", None)
    File.setSourcePath("../peripheral/pit_6079/templates/plib_pit.c.ftl")
    File.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    File.setDestPath("peripheral/pit/")
    File.setProjectPath("config/"+configName+"/peripheral/pit/")
    File.setType("SOURCE")
    File.setMarkup(True)

    File = pitComponent.createFileSymbol("PIT_INIT", None)
    File.setSourcePath("../peripheral/pit_6079/templates/system/system_initialize.c.ftl")
    File.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    File.setType("STRING")
    File.setMarkup(True)

    File = pitComponent.createFileSymbol("PIT_DEF", None)
    File.setSourcePath("../peripheral/pit_6079/templates/system/system_definitions.h.ftl")
    File.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    File.setType("STRING")
    File.setMarkup(True)
