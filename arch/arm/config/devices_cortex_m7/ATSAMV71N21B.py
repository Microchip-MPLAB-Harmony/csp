# load device specific configurations (fuses)
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# load family specific configuration
execfile(Variables.get("__ARCH_DIR") + "/DS60001527.py")

