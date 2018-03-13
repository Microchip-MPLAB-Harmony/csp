print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_c21/config/clk.py")

# load pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")

devMenu = coreComponent.createMenuSymbol("SAMC21_MENU", None)
devMenu.setLabel("Device & Project Configuration")

devCfgMenu = coreComponent.createMenuSymbol("SAMC21_CFG_MENU", devMenu)
devCfgMenu.setLabel(Variables.get("__PROCESSOR") + " Device Configuration")
devCfgMenu.setDescription("Hardware Configuration Bits")

devCfgComment = coreComponent.createCommentSymbol("Comment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

prjMenu = coreComponent.createMenuSymbol("SAMC21_PROJ_MENU", devMenu)
prjMenu.setLabel("Project Configuration")
prjMenu.setDescription("Project Specific Configuration")

