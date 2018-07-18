print("Loading System Services for " + Variables.get("__PROCESSOR"))
# load family specific configuration
execfile(Variables.get("__ARCH_DIR") + "/SAM_G54.py")