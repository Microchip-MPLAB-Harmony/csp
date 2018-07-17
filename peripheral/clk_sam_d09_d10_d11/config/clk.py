print("Loading Clock Manager for " + Variables.get("__PROCESSOR"))

clkMenu = coreComponent.createMenuSymbol("SAM_D09_D10_D11_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuraiton for Clock System Service")

clkEnable = coreComponent.createBooleanSymbol("clkEnable", clkMenu)
clkEnable.setLabel("Use Clock System Service?")
clkEnable.setDefaultValue(True)
clkEnable.setReadOnly(True)
