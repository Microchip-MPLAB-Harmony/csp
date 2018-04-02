print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load watch dog timer information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

