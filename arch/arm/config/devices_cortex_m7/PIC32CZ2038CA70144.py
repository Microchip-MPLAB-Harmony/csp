def RSWDT_DISABLE(rswdtDisable,test):
	if test.getValue() == True:
		rswdtDisable.setVisible(False)
		rswdtDisable.setValue("rswdtDisable",True,2)
	else:
		rswdtDisable.setVisible(True)

print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_e70/config/clk.py")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")

wdtDisable = coreComponent.createBooleanSymbol("wdtDISABLE", devCfgMenu)
print(wdtDisable)
wdtDisable.setLabel("Disable Watchdog")
wdtDisable.setDefaultValue(False)

rswdtDisable = coreComponent.createBooleanSymbol("rswdtDISABLE", devCfgMenu)
print(rswdtDisable)
rswdtDisable.setLabel("Disable Reinforced Safety Watchdog")
rswdtDisable.setDefaultValue(False)
rswdtDisable.setDependencies(RSWDT_DISABLE, ["wdtDISABLE"])

# load device specific configurations (fuses) 
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# load family specific configuration
execfile(Variables.get("__ARCH_DIR") + "/PIC32CZ_CA70.py")

