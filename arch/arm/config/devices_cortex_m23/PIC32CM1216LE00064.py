print("Loading System Services for " + Variables.get("__PROCESSOR"))
# load family specific configuration
execfile(Variables.get("__ARCH_DIR") + "/PIC32CM_LE00_LS00_LS60.py")