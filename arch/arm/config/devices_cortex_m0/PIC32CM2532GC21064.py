print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_d21/config/clk.py")

# load pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")

devMenu = coreComponent.createMenuSymbol(None, None)
devMenu.setLabel("Device & Project Configuration")

devCfgMenu = coreComponent.createMenuSymbol(None, devMenu)
devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
devCfgMenu.setDescription("Hardware Configuration Bits")

devCfgComment = coreComponent.createCommentSymbol("Comment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

prjMenu = coreComponent.createMenuSymbol(None, devMenu)
prjMenu.setLabel("Project Configuration")
prjMenu.setDescription("Project Specific Configuration")

