print("Loading PIC32CZ2038CA70144 Clock Manager")

clkMenu = coreComponent.createMenuSymbol(None, None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuraiton for Clock System Service")

clkEnable = coreComponent.createBooleanSymbol("clkEnable", clkMenu)
clkEnable.setLabel("Use Clock System Service?")
clkEnable.setDefaultValue(True)
clkEnable.setReadOnly(True)
