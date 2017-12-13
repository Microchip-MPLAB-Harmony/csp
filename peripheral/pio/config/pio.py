print("Loading PIC32CZ2038CA70144 Pin Manager")

portsMenu = coreComponent.createMenuSymbol(None, None)
portsMenu.setLabel("Ports")
portsMenu.setDescription("Configuraiton for Ports System Service")

portsEnable = coreComponent.createBooleanSymbol("portsEnable", portsMenu)
portsEnable.setLabel("Use Ports System Service?")
portsEnable.setDefaultValue(True)
portsEnable.setReadOnly(True)
