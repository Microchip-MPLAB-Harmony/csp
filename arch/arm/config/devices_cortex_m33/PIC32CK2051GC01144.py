print("Loading System Services for " + Variables.get("__PROCESSOR"))
# load family specific configuration
execfile(Variables.get("__ARCH_DIR") + "/PIC32CK_GC_SG.py")