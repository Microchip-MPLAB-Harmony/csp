global instanceName

def updateInterrupt(symbol, event):
    instanceName = symbol.getComponent().getSymbolByID("PIT_INSTANCE_NAME")
    if event['value'] == True:
        Database.setSymbolValue("core", instanceName.getValue()+"_INTERRUPT_ENABLE", True, 2)
        Database.setSymbolValue("core", instanceName.getValue()+"_INTERRUPT_HANDLER", instanceName.getValue()+"_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", instanceName.getValue()+"_INTERRUPT_ENABLE", False, 2)
        Database.clearSymbolValue("core", instanceName.getValue()+"_INTERRUPT_HANDLER")


def calcPIV(period_ms):
    clk_freq = int(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    clk_freq = clk_freq / 16;

    return int(period_ms * clk_freq / 1000)


def updatePIV(symbol, event):
    period = symbol.getComponent().getSymbolValue("PERIOD_MS")
    piv = calcPIV(period)
    symbol.setValue(piv, 1)


def provideCommonTimerSymbols( aComponent ):
    """ Symbol interface required to be a TMR provider to SYS_TIME """
    global instanceName

    timerStartApiName =     instanceName.getValue() + "_TimerStart"
    timerStopApiName =      instanceName.getValue() + "_TimerStop "
    compareSetApiName =     instanceName.getValue() + "_TimerCompareSet"
    periodSetApiName =      instanceName.getValue() + "_TimerPeriodSet"
    counterGetApiName =     instanceName.getValue() + "_TimerCounterGet"
    frequencyGetApiName =   instanceName.getValue() + "_TimerFrequencyGet"
    callbackApiName =       instanceName.getValue() + "_TimerCallbackSet"
    irqEnumName =           instanceName.getValue() + "_IRQn"

    timerWidthSymbol = aComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidthSymbol.setVisible(False)
    timerWidthSymbol.setDefaultValue(16)

    timerPeriodMaxSymbol = aComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMaxSymbol.setVisible(False)
    timerPeriodMaxSymbol.setDefaultValue("0xFFFF")

    timerStartApiNameSymbol = aComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiNameSymbol.setVisible(False)
    timerStartApiNameSymbol.setValue(timerStartApiName, 1)

    timerStopApiNameSymbol = aComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timerStopApiNameSymbol.setVisible(False)
    timerStopApiNameSymbol.setValue(timerStopApiName, 1)

    compareSetApiNameSymbol = aComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiNameSymbol.setVisible(False)
    compareSetApiNameSymbol.setValue(compareSetApiName, 1)

    periodSetApiNameSymbol = aComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiNameSymbol.setVisible(False)
    periodSetApiNameSymbol.setValue(periodSetApiName, 1)

    counterApiNameSymbol = aComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiNameSymbol.setVisible(False)
    counterApiNameSymbol.setValue(counterGetApiName, 1)

    frequencyGetApiNameSymbol = aComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiNameSymbol.setVisible(False)
    frequencyGetApiNameSymbol.setValue(frequencyGetApiName, 1)

    callbackApiNameSymbol = aComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiNameSymbol.setVisible(False)
    callbackApiNameSymbol.setValue(callbackApiName, 1)

    irqEnumNameSymbol = aComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumNameSymbol.setVisible(False)
    irqEnumNameSymbol.setValue(irqEnumName, 1)


def instantiateComponent( pitComponent ):
    global instanceName
    instanceName = pitComponent.createStringSymbol("PIT_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(pitComponent.getID().upper())

    provideCommonTimerSymbols( pitComponent )

    enable = pitComponent.createBooleanSymbol("ENABLE_COUNTER", None)
    enable.setLabel("Enable Counter")
    enable.setDefaultValue(True)

    interrupt = pitComponent.createBooleanSymbol("ENABLE_INTERRUPT", None)
    interrupt.setLabel("Enable Interrupt")
    interrupt.setDefaultValue(True)
    interrupt.setDependencies(updateInterrupt, ["ENABLE_INTERRUPT"])

    if interrupt.getValue() == True:
        Database.setSymbolValue("core", instanceName.getValue()+"_INTERRUPT_ENABLE", True, 2)
        Database.setSymbolValue("core", instanceName.getValue()+"_INTERRUPT_HANDLER", instanceName.getValue()+"_InterruptHandler", 2)

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
    File.setSourcePath("../peripheral/pit_6079/templates/system/initialization.c.ftl")
    File.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    File.setType("STRING")
    File.setMarkup(True)

    File = pitComponent.createFileSymbol("PIT_DEF", None)
    File.setSourcePath("../peripheral/pit_6079/templates/system/definitions.h.ftl")
    File.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    File.setType("STRING")
    File.setMarkup(True)
