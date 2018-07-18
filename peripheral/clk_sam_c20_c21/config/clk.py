Log.writeInfoMessage("Loading osctrl Manager for " + Variables.get("__PROCESSOR"))

from os.path import join
from xml.etree import ElementTree

clkMenu = coreComponent.createMenuSymbol("SAMC21_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")

# load clock manager information
clkEnable = coreComponent.createBooleanSymbol("clkEnable", clkMenu)
clkEnable.setLabel("Use Clock System Service?")
clkEnable.setDefaultValue(True)
clkEnable.setReadOnly(True)

################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC Configuration callback functions    ###############################

#Setting the XOSC Interrupt Mode
def setXOSCInterruptmodeProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Automatic Gain Control Visible Property
def setXOSCAMPGCmodeProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator Mode Visible Property
def setXOSCOSCILLATORModeVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator Frequency Property
def setXOSCOscillatorFREQUENCYVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator Gain Property
def setXOSCOscillatorGAINVisibleProperty(symbol, event):
    if(event["value"] <= 2000000):
        symbol.setValue(0,1)
    elif(event["value"] <= 4000000):
        symbol.setValue(1,1)
    elif(event["value"] <= 8000000):
        symbol.setValue(2,1)
    elif(event["value"] <= 16000000):
        symbol.setValue(3,1)
    else:
        symbol.setValue(4,1)

#XOSC Oscillator OnDemand Visible Property
def setXOSCONDEMANDVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator startup Visible Property
def setXOSCSTARTUPVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator Run Standby Visible Property
def setXOSCRUNSTDBYVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])


#XOSC Oscillator clock Failure Detector(CFD) Enable Visible Property
def setXOSCCFDENVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#XOSC Oscillator clock Failure Detector(CFD) Pre-Scalar VisibleProperty
def setXOSCCFDPRESCVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

####    OSC48M Configuration Callback Functions    #############################

#OSC48M Internal Oscillator OnDemand Visible Property
def setOSC48MONDEMANDVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC48M Internal Oscillator Run Standby Visible Property
def setOSC48MRUNSTDBYVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC48M Internal Oscillator Division Factor Visible Property
def setOSC48MDIVVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC48M Internal Oscillator Startup Time Visible Property
def setOSC48MSTARTUPVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

####    DPLL Configuration Callback Functions    ###############################

#DPLL Oscillator Interrupt Mode set Property
def setDPLLInterruptmodeProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator OnDemand Visible Property
def setDPLLONDEMANDVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Run Standby VisibleProperty
def setDPLLRUNSTDBYVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Loop Division Ration(LDR) integer Visible Property
def setDPLLRATIOLDRVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Loop Division Ration(LDR) Fraction Visible Property
def setDPLLRATIOLDRFRACVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Pre-Scalar Visible Property
def setDPLLPRESCVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Clock Divider Visible Property
def setDPLLLCLKDIVIDERVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Lock Bypass Visible Property
def setDPLLLBYPASSVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Lock Time Visible Property
def setDPLLLTIMEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Reference Clock Visible Property
def setDPLLREFCLKVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator WakeUp Fast Visible Property
def setDPLLWUFVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Low Power Enable Visible Property
def setDPLLLPENVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#DPLL Oscillator Proportional Integral Filter Selection Visible Property
def setDPLLFILTERVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

################################################################################
#######          OSCCTRL Database Components      ##############################
################################################################################

#Oscillator control (OSCCTRL) Menu
oscctrlSym_Menu = coreComponent.createMenuSymbol("OSCCTRL_MENU", clkMenu)
oscctrlSym_Menu.setLabel("Oscillator Configuration")

############################   XOSC Components    ##############################

#XOSC Oscillator Enable
oscctrlSym_XOSC_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_ENABLE", oscctrlSym_Menu)
oscctrlSym_XOSC_CONFIG_ENABLE.setLabel("External Multipurpose Crystal Oscillator(XOSC) Enable")
oscctrlSym_XOSC_CONFIG_ENABLE.setDescription("External Crystal Oscillator Enable Feature")
# oscctrlSym_XOSC_CONFIG_ENABLE.setDefaultValue(False)

#XOSC Oscillator Interrupt Mode
oscctrlSym_XOSC_INTERRUPTMODE = coreComponent.createBooleanSymbol("XOSC_INTERRUPT_MODE", oscctrlSym_XOSC_CONFIG_ENABLE)
# oscctrlSym_XOSC_INTERRUPTMODE.setDefaultValue(False)
oscctrlSym_XOSC_INTERRUPTMODE.setVisible(False)
oscctrlSym_XOSC_INTERRUPTMODE.setDependencies(setXOSCInterruptmodeProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Automatic Gain Control Mode
oscctrlSym_XOSC_AMPGC = coreComponent.createBooleanSymbol("XOSC_AMPGC", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSC_AMPGC.setLabel("Automatic Gain Control ")
# oscctrlSym_XOSC_AMPGC.setDefaultValue(False)
oscctrlSym_XOSC_AMPGC.setVisible(False)
oscctrlSym_XOSC_AMPGC.setDependencies(setXOSCAMPGCmodeProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Mode
oscctrlSym_XOSC_OSCILLATORMODE = coreComponent.createKeyValueSetSymbol("XOSC_OSCILLATOR_MODE", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSC_OSCILLATORMODE.setLabel("External Oscillator Mode ")
oscctrlSym_XOSC_OSCILLATORMODE.setVisible(False)
oscctrlSym_XOSC_OSCILLATORMODE.addKey("EXTERNAL_CLOCK","0","xosc external clock enable")
oscctrlSym_XOSC_OSCILLATORMODE.addKey("CRYSTAL","1","crystal oscillator enable")
oscctrlSym_XOSC_OSCILLATORMODE.setOutputMode("Key")
oscctrlSym_XOSC_OSCILLATORMODE.setDependencies(setXOSCOSCILLATORModeVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Frequency
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_FREQUENCY", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setLabel("Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDescription("Setting the XOSC Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setVisible(False)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDefaultValue(8000000)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setMax(32000000)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDependencies(setXOSCOscillatorFREQUENCYVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Gain
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_GAIN", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setLabel("Gain")
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setDescription("Setting the XOSC Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setVisible(False)
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setDependencies(setXOSCOscillatorGAINVisibleProperty, ["CONFIG_CLOCK_XOSC_FREQUENCY"])

xoscOperationModeONDEMAND = ["Always Enable" , "Only on Peripheral Request"]

#XOSC Oscillator ONDEMAND Mode
oscctrlSym_XOSCCTRL_ONDEMAND = coreComponent.createComboSymbol("CONFIG_CLOCK_XOSC_ONDEMAND", oscctrlSym_XOSC_CONFIG_ENABLE, xoscOperationModeONDEMAND)
oscctrlSym_XOSCCTRL_ONDEMAND.setLabel("Oscillator On-Demand Control")
oscctrlSym_XOSCCTRL_ONDEMAND.setDescription("Configures the XOSC on Demand Behavior")
oscctrlSym_XOSCCTRL_ONDEMAND.setVisible(False)
oscctrlSym_XOSCCTRL_ONDEMAND.setDefaultValue("Always Enable")
oscctrlSym_XOSCCTRL_ONDEMAND.setDependencies(setXOSCONDEMANDVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Startup Time
oscctrlSym_XOSCCTRL_STARTUP = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_STARTUP",oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSCCTRL_STARTUP.setLabel("Oscillator Startup Time")
oscctrlSym_XOSCCTRL_STARTUP.setDescription("Startup time for the XOSC ")
oscctrlSym_XOSCCTRL_STARTUP.setVisible(False)
oscctrlSymXOSCStartupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_XOSCCTRL__STARTUP\"]")
oscctrlSymXOSCStartupValues = []
oscctrlSymXOSCStartupValues = oscctrlSymXOSCStartupNode.getChildren()
xoscstartupDefaultValue = 0
for index in range(0, len(oscctrlSymXOSCStartupValues)):
    xoscstartupKeyName = oscctrlSymXOSCStartupValues[index].getAttribute("name")

    if (xoscstartupKeyName == "CYCLE1"):
        xoscstartupDefaultValue = index

    xoscstartupKeyDescription = oscctrlSymXOSCStartupValues[index].getAttribute("caption")
    xoscstartupKeyValue = oscctrlSymXOSCStartupValues[index].getAttribute("value")
    oscctrlSym_XOSCCTRL_STARTUP.addKey(xoscstartupKeyName, xoscstartupKeyValue , xoscstartupKeyDescription)

oscctrlSym_XOSCCTRL_STARTUP.setDefaultValue(xoscstartupDefaultValue)
oscctrlSym_XOSCCTRL_STARTUP.setOutputMode("Value")
oscctrlSym_XOSCCTRL_STARTUP.setDisplayMode("Description")
oscctrlSym_XOSCCTRL_STARTUP.setDependencies(setXOSCSTARTUPVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Run StandBy Control
oscctrlSym_XOSCCTRL_RUNSTDBY = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_RUNSTDBY", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSCCTRL_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")
oscctrlSym_XOSCCTRL_RUNSTDBY.setDescription("External oscillator RunIn StandBy mode or not")
oscctrlSym_XOSCCTRL_RUNSTDBY.setVisible(False)
# oscctrlSym_XOSCCTRL_RUNSTDBY.setDefaultValue(False)
oscctrlSym_XOSCCTRL_RUNSTDBY.setDependencies(setXOSCRUNSTDBYVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Clock Failure Detector(CFD) Enable
oscctrlSym_XOSCCTRL_CFDEN = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_CFDEN", oscctrlSym_XOSC_CONFIG_ENABLE)
oscctrlSym_XOSCCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
oscctrlSym_XOSCCTRL_CFDEN.setDescription("Clock Failure Detection enable or not")
oscctrlSym_XOSCCTRL_CFDEN.setVisible(False)
# oscctrlSym_XOSCCTRL_CFDEN.setDefaultValue(False)
oscctrlSym_XOSCCTRL_CFDEN.setDependencies(setXOSCCFDENVisibleProperty, ["CONFIG_CLOCK_XOSC_ENABLE"])

#XOSC Oscillator Clock Failure Detector(CFD) Pre-Scalar
oscctrlSym_CFDPRESC_CFDPRESC = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_CFDPRESC",oscctrlSym_XOSCCTRL_CFDEN)
oscctrlSym_CFDPRESC_CFDPRESC.setLabel("Safe Clock Frequency ")
oscctrlSym_CFDPRESC_CFDPRESC.setDescription("Startup time for the XOSC ")
oscctrlSym_CFDPRESC_CFDPRESC.setVisible(False)
oscctrlSymCFDPrescNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_CFDPRESC__CFDPRESC\"]")
oscctrlSymCFDPrescNodeValues = []
oscctrlSymCFDPrescNodeValues = oscctrlSymCFDPrescNode.getChildren()
xosccfdprescalarDefaultValue = 0
for index in range(0, len(oscctrlSymCFDPrescNodeValues)):
    xosccfdprescalarKeyName = oscctrlSymCFDPrescNodeValues[index].getAttribute("name")

    if (xosccfdprescalarKeyName == "DIV1"):
        xosccfdprescalarDefaultValue = index

    xosccfdprescalarKeyDescription = oscctrlSymCFDPrescNodeValues[index].getAttribute("caption")
    xosccfdprescalarKeyValue= oscctrlSymCFDPrescNodeValues[index].getAttribute("value")
    oscctrlSym_CFDPRESC_CFDPRESC.addKey(xosccfdprescalarKeyName, xosccfdprescalarKeyValue , xosccfdprescalarKeyDescription)

oscctrlSym_CFDPRESC_CFDPRESC.setDefaultValue(xosccfdprescalarDefaultValue)
oscctrlSym_CFDPRESC_CFDPRESC.setOutputMode("Value")
oscctrlSym_CFDPRESC_CFDPRESC.setDisplayMode("Description")
oscctrlSym_CFDPRESC_CFDPRESC.setDependencies(setXOSCCFDPRESCVisibleProperty, ["CONFIG_CLOCK_XOSC_CFDEN"])

############################   OSC48M Components    ############################

#OSC48M Internal Oscillator Enable
oscctrlSym_OSC48M_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC48M_ENABLE", oscctrlSym_Menu)
oscctrlSym_OSC48M_CONFIG_ENABLE.setLabel("48MHz Internal Oscillator(OSC48M) Enable")
oscctrlSym_OSC48M_CONFIG_ENABLE.setDescription("Internal 48mhz Oscillator Configuration enable feature")
oscctrlSym_OSC48M_CONFIG_ENABLE.setDefaultValue(True)

osc48mOperationModeONDEMAND = ["Always Enable" , "Only on Peripheral Request"]

#OSC48M Internal Oscillator ONDEMAND Mode
oscctrlSym_OSC48MCTRL_ONDEMAND = coreComponent.createComboSymbol("CONFIG_CLOCK_OSC48M_ONDEMAND", oscctrlSym_OSC48M_CONFIG_ENABLE, osc48mOperationModeONDEMAND)
oscctrlSym_OSC48MCTRL_ONDEMAND.setLabel("Oscillator On-Demand Control")
oscctrlSym_OSC48MCTRL_ONDEMAND.setDescription("Configures the osc48m on Demand Behavior")
oscctrlSym_OSC48MCTRL_ONDEMAND.setDefaultValue("Always Enable")
oscctrlSym_OSC48MCTRL_ONDEMAND.setDependencies(setOSC48MONDEMANDVisibleProperty, ["CONFIG_CLOCK_OSC48M_ENABLE"])

#OSC48M Internal Oscillator  Run StandBy Control
oscctrlSym_OSC48MCTRL_RUNSTDBY = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC48M_RUNSTDY", oscctrlSym_OSC48M_CONFIG_ENABLE)
oscctrlSym_OSC48MCTRL_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")
oscctrlSym_OSC48MCTRL_RUNSTDBY.setDescription("osc48m run in StandBy Mode or Not")
# oscctrlSym_OSC48MCTRL_RUNSTDBY.setDefaultValue(False)
oscctrlSym_OSC48MCTRL_RUNSTDBY.setDependencies(setOSC48MRUNSTDBYVisibleProperty, ["CONFIG_CLOCK_OSC48M_ENABLE"])

#OSC48M Internal Oscillator  Division Factor
oscctrlSym_OSC48MDIV_DIV = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC48M_DIV",oscctrlSym_OSC48M_CONFIG_ENABLE)
oscctrlSym_OSC48MDIV_DIV.setLabel("Oscillator Post-Divider Frequency")
oscctrlSym_OSC48MDIV_DIV.setDescription("The oscillator frequency is 48MHz divided by DIV+1")
oscctrlSymosc48mDivNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_OSC48MDIV__DIV\"]")
oscctrlSymosc48mDivNodeValues = []
oscctrlSymosc48mDivNodeValues = oscctrlSymosc48mDivNode.getChildren()
osc48mdivDefaultValue = 0
for index in range(0, len(oscctrlSymosc48mDivNodeValues)):
    osc48mdivKeyName = oscctrlSymosc48mDivNodeValues[index].getAttribute("name")

    if (osc48mdivKeyName == "DIV12"):
        osc48mdivDefaultValue = index

    osc48mdivKeyDescription = oscctrlSymosc48mDivNodeValues[index].getAttribute("caption")
    osc48mdivKeyValue = oscctrlSymosc48mDivNodeValues[index].getAttribute("value")
    oscctrlSym_OSC48MDIV_DIV.addKey(osc48mdivKeyName, osc48mdivKeyValue , osc48mdivKeyDescription)

oscctrlSym_OSC48MDIV_DIV.setDefaultValue(osc48mdivDefaultValue)
oscctrlSym_OSC48MDIV_DIV.setOutputMode("Value")
oscctrlSym_OSC48MDIV_DIV.setDisplayMode("Description")
oscctrlSym_OSC48MDIV_DIV.setDependencies(setOSC48MDIVVisibleProperty, ["CONFIG_CLOCK_OSC48M_ENABLE"])

#OSC48M Internal Oscillator StartUp Time
oscctrlSym_OSC48STUP_STARTUP = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC48M_STARTUP",oscctrlSym_OSC48M_CONFIG_ENABLE)
oscctrlSym_OSC48STUP_STARTUP.setLabel("Oscillator Startup Delay")
oscctrlSym_OSC48STUP_STARTUP.setDescription("set up the startup time for the osc48m")
oscctrlSymosc48mStartUpNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_OSC48MSTUP__STARTUP\"]")
oscctrlSymosc48mStartUpNodeValues = []
oscctrlSymosc48mStartUpNodeValues = oscctrlSymosc48mStartUpNode.getChildren()
osc48mstartupDefaultValue = 0
for index in range(0, len(oscctrlSymosc48mStartUpNodeValues)):
    osc48mstartupKeyName = oscctrlSymosc48mStartUpNodeValues[index].getAttribute("name")

    if (osc48mstartupKeyName == "CYCLE1024"):
        osc48mstartupDefaultValue = index

    osc48mstartupKeyDescription = oscctrlSymosc48mStartUpNodeValues[index].getAttribute("caption")
    osc48mstartupKeyValue = oscctrlSymosc48mStartUpNodeValues[index].getAttribute("value")
    oscctrlSym_OSC48STUP_STARTUP.addKey(osc48mstartupKeyName, osc48mstartupKeyValue , osc48mstartupKeyDescription)

oscctrlSym_OSC48STUP_STARTUP.setDefaultValue(osc48mstartupDefaultValue)
oscctrlSym_OSC48STUP_STARTUP.setOutputMode("Value")
oscctrlSym_OSC48STUP_STARTUP.setDisplayMode("Description")
oscctrlSym_OSC48STUP_STARTUP.setDependencies(setOSC48MSTARTUPVisibleProperty, ["CONFIG_CLOCK_OSC48M_ENABLE"])

############################   DPLL Components    ############################

#Digital Phase Locked Loop(DPLL) Enable
oscctrlSym_DPLL_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_ENABLE", oscctrlSym_Menu)
oscctrlSym_DPLL_CONFIG_ENABLE.setLabel("Digital Phase Locked Loop(DPLL) Enable ")
oscctrlSym_DPLL_CONFIG_ENABLE.setDescription("DPLL Configuration enabling feature")
# oscctrlSym_DPLL_CONFIG_ENABLE.setDefaultValue(False)

#Digital Phase Locked Loop(DPLL) Interrupt Mode
oscctrlSym_DPLL_INTERRUPTMODE = coreComponent.createBooleanSymbol("DPLL_INTERRUPT_MODE", oscctrlSym_DPLL_CONFIG_ENABLE)
# oscctrlSym_DPLL_INTERRUPTMODE.setDefaultValue(False)
oscctrlSym_DPLL_INTERRUPTMODE.setVisible(False)
oscctrlSym_DPLL_INTERRUPTMODE.setDependencies(setDPLLInterruptmodeProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

dpllOperationModeONDEMAND = ["Always Enable" , "Only on Peripheral Request"]

#Digital Phase Locked Loop(DPLL) ONDEMAND Mode
oscctrlSym_DPLLCTRLA_ONDEMAND = coreComponent.createComboSymbol("CONFIG_CLOCK_DPLL_ONDEMAND", oscctrlSym_DPLL_CONFIG_ENABLE, dpllOperationModeONDEMAND)
oscctrlSym_DPLLCTRLA_ONDEMAND.setLabel("DPLL On-Demand Control")
oscctrlSym_DPLLCTRLA_ONDEMAND.setDescription("Configures the DPLL on Demand Behavior")
oscctrlSym_DPLLCTRLA_ONDEMAND.setVisible(False)
oscctrlSym_DPLLCTRLA_ONDEMAND.setDefaultValue("Always Enable")
oscctrlSym_DPLLCTRLA_ONDEMAND.setDependencies(setDPLLONDEMANDVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Run StandBy Control
oscctrlSym_DPLLCTRLA_RUNSTDBY = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_RUNSTDY", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLA_RUNSTDBY.setLabel("Run DPLL in Standby Sleep Mode")
oscctrlSym_DPLLCTRLA_RUNSTDBY.setDescription("DPLL to run in standby mode or not")
oscctrlSym_DPLLCTRLA_RUNSTDBY.setVisible(False)
# oscctrlSym_DPLLCTRLA_RUNSTDBY.setDefaultValue(False)
oscctrlSym_DPLLCTRLA_RUNSTDBY.setDependencies(setDPLLRUNSTDBYVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Integer part
oscctrlSym_DPLLRATIO_LDR = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDR_INTEGER", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLRATIO_LDR.setLabel("DPLL Loop Divider Ratio Integer Part")
oscctrlSym_DPLLRATIO_LDR.setDescription("Loop divider ratio integer value")
oscctrlSym_DPLLRATIO_LDR.setVisible(False)
oscctrlSym_DPLLRATIO_LDR.setDefaultValue(0)
oscctrlSym_DPLLRATIO_LDR.setDependencies(setDPLLRATIOLDRVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Fraction part
oscctrlSym_DPLLRATIO_LDRFRAC = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLRATIO_LDRFRAC.setLabel("DPLL Loop Divider Ratio Fractional Part")
oscctrlSym_DPLLRATIO_LDRFRAC.setDescription("loop divider ratio fraction value")
oscctrlSym_DPLLRATIO_LDRFRAC.setVisible(False)
oscctrlSym_DPLLRATIO_LDRFRAC.setDefaultValue(0)
oscctrlSym_DPLLRATIO_LDRFRAC.setDependencies(setDPLLRATIOLDRFRACVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Pre-Scalar
oscctrlSym_DPLLPRESC_PRESC = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_PRESCALAR", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLPRESC_PRESC.setLabel("DPLL Output Pre-Scalar")
oscctrlSym_DPLLPRESC_PRESC.setDescription("Selection of the DPLL Pre-Scalar value ")
oscctrlSym_DPLLPRESC_PRESC.setVisible(False)
oscctrlSymDPLLPrescNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLPRESC__PRESC\"]")
oscctrlSymDPLLPrescNodeValues = []
oscctrlSymDPLLPrescNodeValues = oscctrlSymDPLLPrescNode.getChildren()
dpllprescalarDefaultValue = 0
for index in range(0, len(oscctrlSymDPLLPrescNodeValues)):
    dpllprescalarKeyName = oscctrlSymDPLLPrescNodeValues[index].getAttribute("name")

    if (dpllprescalarKeyName == "DIV1"):
        dpllprescalarDefaultValue = index

    dpllprescalarKeyDescription = oscctrlSymDPLLPrescNodeValues[index].getAttribute("caption")
    dpllprescalarKeyValue = oscctrlSymDPLLPrescNodeValues[index].getAttribute("value")
    oscctrlSym_DPLLPRESC_PRESC.addKey(dpllprescalarKeyName, dpllprescalarKeyValue , dpllprescalarKeyDescription)

oscctrlSym_DPLLPRESC_PRESC.setDefaultValue(dpllprescalarDefaultValue)
oscctrlSym_DPLLPRESC_PRESC.setOutputMode("Value")
oscctrlSym_DPLLPRESC_PRESC.setDisplayMode("Description")
oscctrlSym_DPLLPRESC_PRESC.setDependencies(setDPLLPRESCVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Lock Bypass
oscctrlSym_DPLLCTRLB_LBYPASS = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOCK_BYPASS", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_LBYPASS.setLabel("Bypass DPLL Lock?")
oscctrlSym_DPLLCTRLB_LBYPASS.setDescription("DPLL Lock signal is always asserted or DPLL Lock signal drives the DPLL controller internal logic.")
oscctrlSym_DPLLCTRLB_LBYPASS.setVisible(False)
# oscctrlSym_DPLLCTRLB_LBYPASS.setDefaultValue(False)
oscctrlSym_DPLLCTRLB_LBYPASS.setDependencies(setDPLLLBYPASSVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Low Power Enable
oscctrlSym_DPLLCTRLB_LPEN = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_LPEN.setLabel("DPLL Low Power Enable")
oscctrlSym_DPLLCTRLB_LPEN.setDescription("Low Power Mode Enabled or not")
oscctrlSym_DPLLCTRLB_LPEN.setVisible(False)
# oscctrlSym_DPLLCTRLB_LPEN.setDefaultValue(False)
oscctrlSym_DPLLCTRLB_LPEN.setDependencies(setDPLLLPENVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) wakeUp Fast
oscctrlSym_DPLLCTRLB_WUF = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_WAKEUP_FAST", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_WUF.setLabel("DPLL Fast Output Enable")
oscctrlSym_DPLLCTRLB_WUF.setDescription("DPLL clock is Output after startup and lock time or only after the startup")
oscctrlSym_DPLLCTRLB_WUF.setVisible(False)
# oscctrlSym_DPLLCTRLB_WUF.setDefaultValue(False)
oscctrlSym_DPLLCTRLB_WUF.setDependencies(setDPLLWUFVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Lock Time
oscctrlSym_DPLLCTRLB_LTIME = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_LOCK_TIME", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_LTIME.setLabel("DPLL Lock Time-out")
oscctrlSym_DPLLCTRLB_LTIME.setDescription("select the lock time-out value:")
oscctrlSym_DPLLCTRLB_LTIME.setVisible(False)
oscctrlSymDPLLLockTimeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__LTIME\"]")
oscctrlSymDPLLLockTimeNodeValues = []
oscctrlSymDPLLLockTimeNodeValues = oscctrlSymDPLLLockTimeNode.getChildren()
dpllLockTimeDefaultValue = 0
for index in range(0, len(oscctrlSymDPLLLockTimeNodeValues)):
    dpllLockTimeKeyName = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute("name")

    if (dpllLockTimeKeyName == "DEFAULT"):
        dpllLockTimeDefaultValue = index

    dpllLockTimeKeyDescription = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute("caption")
    dpllLockTimeKeyValue = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute("value")
    oscctrlSym_DPLLCTRLB_LTIME.addKey(dpllLockTimeKeyName, dpllLockTimeKeyValue , dpllLockTimeKeyDescription)

oscctrlSym_DPLLCTRLB_LTIME.setDefaultValue(dpllLockTimeDefaultValue)
oscctrlSym_DPLLCTRLB_LTIME.setOutputMode("Value")
oscctrlSym_DPLLCTRLB_LTIME.setDisplayMode("Description")
oscctrlSym_DPLLCTRLB_LTIME.setDependencies(setDPLLLTIMEVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Filter
oscctrlSym_DPLLCTRLB_FILTER = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_FILTER", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_FILTER.setLabel("DPLL Feedback Filter Selection")
oscctrlSym_DPLLCTRLB_FILTER.setDescription("DPLL filter type selection")
oscctrlSym_DPLLCTRLB_FILTER.setVisible(False)
oscctrlSymDPLLFilterNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__FILTER\"]")
oscctrlSymDPLLFilterNodeValues = []
oscctrlSymDPLLFilterNodeValues = oscctrlSymDPLLFilterNode.getChildren()
dpllfilterDefaultValue = 0
for index in range(0, len(oscctrlSymDPLLFilterNodeValues)):
    dpllfilterKeyName = oscctrlSymDPLLFilterNodeValues[index].getAttribute("name")

    if (dpllfilterKeyName == "DEFAULT"):
        dpllfilterDefaultValue = index

    dpllfilterKeyDescription = oscctrlSymDPLLFilterNodeValues[index].getAttribute("caption")
    dpllfilterKeyValue = oscctrlSymDPLLFilterNodeValues[index].getAttribute("value")
    oscctrlSym_DPLLCTRLB_FILTER.addKey(dpllfilterKeyName, dpllfilterKeyValue , dpllfilterKeyDescription)

oscctrlSym_DPLLCTRLB_FILTER.setDefaultValue(dpllfilterDefaultValue)
oscctrlSym_DPLLCTRLB_FILTER.setOutputMode("Value")
oscctrlSym_DPLLCTRLB_FILTER.setDisplayMode("Description")
oscctrlSym_DPLLCTRLB_FILTER.setDependencies(setDPLLFILTERVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Reference Clock
oscctrlSym_DPLLCTRLB_REFCLK = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_REF_CLOCK", oscctrlSym_DPLL_CONFIG_ENABLE)
oscctrlSym_DPLLCTRLB_REFCLK.setLabel("DPLL Reference Clock Source")
oscctrlSym_DPLLCTRLB_REFCLK.setDescription("DPLL reference clock selection")
oscctrlSym_DPLLCTRLB_REFCLK.setVisible(False)
oscctrlSymDPLLRefClkNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__REFCLK\"]")
oscctrlSymDPLLRefClkNodeValues = []
oscctrlSymDPLLRefClkNodeValues = oscctrlSymDPLLRefClkNode.getChildren()
dpllrefclockDefaultValue = 0
for index in range(0, len(oscctrlSymDPLLRefClkNodeValues)):
    dpllrefclockKeyName = oscctrlSymDPLLRefClkNodeValues[index].getAttribute("name")

    if (dpllrefclockKeyName == "XOSC32K"):
        dpllrefclockDefaultValue = index

    dpllrefclockKeyDescription = oscctrlSymDPLLRefClkNodeValues[index].getAttribute("caption")
    dpllrefclockKeyValue = oscctrlSymDPLLRefClkNodeValues[index].getAttribute("value")
    oscctrlSym_DPLLCTRLB_REFCLK.addKey(dpllrefclockKeyName, dpllrefclockKeyValue , dpllrefclockKeyDescription)

oscctrlSym_DPLLCTRLB_REFCLK.setDefaultValue(dpllrefclockDefaultValue)
oscctrlSym_DPLLCTRLB_REFCLK.setOutputMode("Value")
oscctrlSym_DPLLCTRLB_REFCLK.setDisplayMode("Description")
oscctrlSym_DPLLCTRLB_REFCLK.setDependencies(setDPLLREFCLKVisibleProperty, ["CONFIG_CLOCK_DPLL_ENABLE"])

#Digital Phase Locked Loop(DPLL) Clock Divider
oscctrlSym_DPLLCTRLB_DIV = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_DIVIDER", oscctrlSym_DPLLCTRLB_REFCLK)
oscctrlSym_DPLLCTRLB_DIV.setLabel("DPLL Divider")
oscctrlSym_DPLLCTRLB_DIV.setDescription("XOSC clock division factor fdiv = (fxosc/((2*DIV)+1))")
oscctrlSym_DPLLCTRLB_DIV.setDefaultValue(0)
oscctrlSym_DPLLCTRLB_DIV.setVisible(False)
oscctrlSym_DPLLCTRLB_DIV.setDependencies(setDPLLLCLKDIVIDERVisibleProperty, ["CONFIG_CLOCK_DPLL_REF_CLOCK"])

################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC32K Configuration Callback Functions    ############################

#XOSC32K External Oscillator Interrupt Mode
def setXOSC32KInterruptmodeProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setValue(True,1)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator Mode Visible Property
def setxosc32kOscillatorModeVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator Run Standby Visible Property
def setxosc32kctrlRUNSTDBYVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator OnDemand Visible Property
def setxosc32kctrlONDEMANDVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator 1KHz Output Enable Visible Property
def setxosc32kctrlEN1KVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator 32KHz Output Enable Visible Property
def setxosc32kctrlEN32KVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)


#XOSC32K External Oscillator Write Lock Visible Property
def setxosc32kctrlWRTLOCKVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator StartUp Time Visible Property
def setxosc32kSTARTUPVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator Clock Failure Detection(CFD) Enable Visible Property
def setxosc32kctrlCFDENVisibleProperty(symbol, event):
    if(event["value"] == 1):
        symbol.setVisible(True)
    else :
        symbol.setVisible(False)

#XOSC32K External Oscillator Clock Failure Detection(CFD) pre-Scalar Visible Property
def setxosc32kctrlCFDPRESCVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#####    OSC32K Configuration Callback Functions    ############################

#OSC32K Oscillator Run Standby Visible Property
def setosc32kctrlRUNSTDBYVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC32K Oscillator OnDemand Visible Property
def setosc32kctrlONDEMANDVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC32K Oscillator 1KHz Output Enable Visible Property
def setosc32kctrlEN1KVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC32K Oscillator 32KHz Output Enable Visible Property
def setosc32kctrlEN32KVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC32K Oscillator Write Lock Visible Property
def setosc32kctrlWRTLOCKVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSC32K Oscillator StartUp Time Visible Property
def setosc32kSTARTUPVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

##########   OSCULP32K Configuration Callback Functions   ######################

#OSCULP32K Oscillator Calibration Enable Visible Property
def setosculp32kCALIBENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSCULP32K Oscillator Calibration value Visible Property
def setosculp32kCALIBVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#OSCULP32K Oscillator Write Lock Visible Property
def setosculp32kWRTLOCKVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

################################################################################
#######          OSC32KCTRL Database Components      ###########################
################################################################################

#32Khz Oscillator Control(OSC32KCTRL) Menu
osc32kctrlSym_Menu = coreComponent.createMenuSymbol("OSC32KCTRL_MENU", clkMenu)
osc32kctrlSym_Menu.setLabel("32KHz Oscillator Configuration")

#####################    OSCULP32K Components    ###############################

#OSCULP32K Oscillator Factory Calibration Enable
osc32kctrlSym_OSCULP32K_CALIB_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSCULP32K_CALIB_ENABLE", osc32kctrlSym_Menu)
osc32kctrlSym_OSCULP32K_CALIB_ENABLE.setLabel("Override Factory Calibration Value(in OSCULP32K)")

#OSCULP32K Oscillator Calibration value
osc32kctrlSym_OSCULP32K_CALIB = coreComponent.createIntegerSymbol("OSCULP32K_CALIB_VALUE", osc32kctrlSym_OSCULP32K_CALIB_ENABLE)
osc32kctrlSym_OSCULP32K_CALIB.setLabel("Calibration Value")
osc32kctrlSym_OSCULP32K_CALIB.setVisible(False)
osc32kctrlSym_OSCULP32K_CALIB.setDependencies(setosculp32kCALIBVisibleProperty, ["CONFIG_CLOCK_OSCULP32K_CALIB_ENABLE"])

####################    XOSC32K Components    ##################################

#XOSC32K External Oscillator Enable
osc32kctrlSym_XOSC32K_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONF_CLOCK_XOSC32K_ENABLE", osc32kctrlSym_Menu)
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setLabel("32KHz External Crystal Oscillator(XOSC32K) Enable")
# osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setDefaultValue(False)

#XOSC32K External Oscillator Interrupt Mode
osc32kctrlSym_XOSC32K_INTERRUPTMODE = coreComponent.createBooleanSymbol("XOSC32K_INTERRUPT_MODE", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
# osc32kctrlSym_XOSC32K_INTERRUPTMODE.setDefaultValue(False)
osc32kctrlSym_XOSC32K_INTERRUPTMODE.setVisible(False)
osc32kctrlSym_XOSC32K_INTERRUPTMODE.setDependencies(setXOSC32KInterruptmodeProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator Mode
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE = coreComponent.createKeyValueSetSymbol("XOSC32K_OSCILLATOR_MODE", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setLabel("32KHz External Oscillator Mode ")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setVisible(False)
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey("EXTERNAL_CLOCK","0","xosc32K external clock enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey("CRYSTAL","1","crystal oscillator enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setOutputMode("Key")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setDependencies(setxosc32kOscillatorModeVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator Run StandBy Mode
osc32kctrlSym_XOSC32K_RUNSTDBY = coreComponent.createBooleanSymbol("XOSC32K_RUNSTDBY", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")
osc32kctrlSym_XOSC32K_RUNSTDBY.setVisible(False)
osc32kctrlSym_XOSC32K_RUNSTDBY.setDependencies(setxosc32kctrlRUNSTDBYVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

osc32kctrlModeONDEMAND = ["Always Enable" , "Only on Peripheral Request"]

#XOSC32K External Oscillator ONDEMAND Mode

osc32kctrlSym_XOSC32K_ONDEMAND= coreComponent.createComboSymbol("XOSC32K_ONDEMAND", osc32kctrlSym_XOSC32K_CONFIG_ENABLE, osc32kctrlModeONDEMAND)
osc32kctrlSym_XOSC32K_ONDEMAND.setLabel("Oscillator On-Demand Control")
osc32kctrlSym_XOSC32K_ONDEMAND.setDescription("Configures the DPLL on Demand Behavior")
osc32kctrlSym_XOSC32K_ONDEMAND.setVisible(False)
osc32kctrlSym_XOSC32K_ONDEMAND.setDefaultValue("Always Enable")
osc32kctrlSym_XOSC32K_ONDEMAND.setDependencies(setxosc32kctrlONDEMANDVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator 1KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN1K = coreComponent.createBooleanSymbol("XOSC32K_EN1K", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_EN1K.setLabel("Enable 1KHz Output")
osc32kctrlSym_XOSC32K_EN1K.setVisible(False)
osc32kctrlSym_XOSC32K_EN1K.setDependencies(setxosc32kctrlEN1KVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator 32KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN32K = coreComponent.createBooleanSymbol("XOSC32K_EN32K", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_EN32K.setLabel("Enable 32KHz Output")
osc32kctrlSym_XOSC32K_EN32K.setVisible(False)
osc32kctrlSym_XOSC32K_EN32K.setDependencies(setxosc32kctrlEN32KVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator StartUp Time
osc32kctrlSym_XOSC32K_STARTUP = coreComponent.createKeyValueSetSymbol("XOSC32K_STARTUP", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_STARTUP.setLabel("Oscillator Startup Time ")
osc32kctrlSym_XOSC32K_STARTUP.setDescription("XOSC start up time ")
osc32kctrlSym_XOSC32K_STARTUP.setVisible(False)
osc32kctrlXOSC32KStarupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"OSC32KCTRL_XOSC32K__STARTUP\"]")
osc32kctrlXOSC32KStarupNodeValues = []
osc32kctrlXOSC32KStarupNodeValues = osc32kctrlXOSC32KStarupNode.getChildren()
xosc32kstartupDefaultValue = 0
for index in range(0, len(osc32kctrlXOSC32KStarupNodeValues)):
    xosc32kstartupKeyName = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("name")

    if (xosc32kstartupKeyName == "CYCLE1"):
        xosc32kstartupDefaultValue = index

    xosc32kstartupKeyDescription = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("caption")
    xosc32kstartupKeyValue = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("value")
    osc32kctrlSym_XOSC32K_STARTUP.addKey(xosc32kstartupKeyName, xosc32kstartupKeyValue , xosc32kstartupKeyDescription)

osc32kctrlSym_XOSC32K_STARTUP.setDefaultValue(xosc32kstartupDefaultValue)
osc32kctrlSym_XOSC32K_STARTUP.setOutputMode("Value")
osc32kctrlSym_XOSC32K_STARTUP.setDisplayMode("Description")
osc32kctrlSym_XOSC32K_STARTUP.setDependencies(setxosc32kSTARTUPVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator Clock Failure Detection(CFD) Enable
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN = coreComponent.createBooleanSymbol("XOSC32K_CFDEN", osc32kctrlSym_XOSC32K_CONFIG_ENABLE)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setVisible(False)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setDependencies(setxosc32kctrlCFDENVisibleProperty, ["CONF_CLOCK_XOSC32K_ENABLE"])

#XOSC32K External Oscillator Clock Failure Detection(CFD) Pre-Scalar
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC = coreComponent.createBooleanSymbol("XOSC32K_CFDPRESC", osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setLabel("Clock Failure Backup Clock Frequency Divide-by-2")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setVisible(False)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setDependencies(setxosc32kctrlCFDPRESCVisibleProperty, ["XOSC32K_CFDEN"])

#######################   OSC32K Components    #################################

#OSC32K Oscillator Enable
osc32kctrlSym_OSC32K_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONF_CLOCK_OSC32K_ENABLE", osc32kctrlSym_Menu)
osc32kctrlSym_OSC32K_CONFIG_ENABLE.setLabel("32Khz Internal Oscillator(OSC32K) Enable")
# osc32kctrlSym_OSC32K_CONFIG_ENABLE.setDefaultValue(False)

#OSC32K Oscillator Run StandBy Mode
osc32kctrlSym_OSC32K_RUNSTDBY = coreComponent.createBooleanSymbol("OSC32K_RUNSTDBY", osc32kctrlSym_OSC32K_CONFIG_ENABLE)
osc32kctrlSym_OSC32K_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")
osc32kctrlSym_OSC32K_RUNSTDBY.setVisible(False)
osc32kctrlSym_OSC32K_RUNSTDBY.setDependencies(setosc32kctrlRUNSTDBYVisibleProperty, ["CONF_CLOCK_OSC32K_ENABLE"])

osc32kctrlModeONDEMAND = ["Always Enable" , "Only on Peripheral Request"]

#OSC32K Oscillator ONDEMAND Mode
osc32kctrlSym_OSC32K_ONDEMAND= coreComponent.createComboSymbol("OSC32K_ONDEMAND", osc32kctrlSym_OSC32K_CONFIG_ENABLE, osc32kctrlModeONDEMAND)
osc32kctrlSym_OSC32K_ONDEMAND.setLabel("Oscillator On-Demand Control")
osc32kctrlSym_OSC32K_ONDEMAND.setDescription("Configures the DPLL on Demand Behavior")
osc32kctrlSym_OSC32K_ONDEMAND.setVisible(False)
osc32kctrlSym_OSC32K_ONDEMAND.setDefaultValue("Always Enable")
osc32kctrlSym_OSC32K_ONDEMAND.setDependencies(setosc32kctrlONDEMANDVisibleProperty, ["CONF_CLOCK_OSC32K_ENABLE"])

#OSC32K Oscillator 1KHz Output Enable Mode
osc32kctrlSym_OSC32K_EN1K = coreComponent.createBooleanSymbol("OSC32K_EN1K", osc32kctrlSym_OSC32K_CONFIG_ENABLE)
osc32kctrlSym_OSC32K_EN1K.setLabel("Enable 1KHz Output")
osc32kctrlSym_OSC32K_EN1K.setVisible(False)
osc32kctrlSym_OSC32K_EN1K.setDependencies(setosc32kctrlEN1KVisibleProperty, ["CONF_CLOCK_OSC32K_ENABLE"])

#OSC32K Oscillator 32KHz Output Enable Mode
osc32kctrlSym_OSC32K_EN32K = coreComponent.createBooleanSymbol("OSC32K_EN32K", osc32kctrlSym_OSC32K_CONFIG_ENABLE)
osc32kctrlSym_OSC32K_EN32K.setLabel("Enable 32KHz Output")
osc32kctrlSym_OSC32K_EN32K.setVisible(False)
osc32kctrlSym_OSC32K_EN32K.setDependencies(setosc32kctrlEN32KVisibleProperty, ["CONF_CLOCK_OSC32K_ENABLE"])

#OSC32K Oscillator StartUp Time
osc32kctrlSym_OSC32K_STARTUP = coreComponent.createKeyValueSetSymbol("OSC32K_STARTUP", osc32kctrlSym_OSC32K_CONFIG_ENABLE)
osc32kctrlSym_OSC32K_STARTUP.setLabel("Oscillator Startup Time ")
osc32kctrlSym_OSC32K_STARTUP.setVisible(False)
osc32kctrlOSC32KStarupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"OSC32KCTRL_OSC32K__STARTUP\"]")
osc32kctrlOSC32KStarupNodeValues = []
osc32kctrlOSC32KStarupNodeValues = osc32kctrlOSC32KStarupNode.getChildren()
osc32kstartupDefaultValue = 0
for index in range(0, len(osc32kctrlOSC32KStarupNodeValues)):
    osc32kstartupKeyName = osc32kctrlOSC32KStarupNodeValues[index].getAttribute("name")

    if (osc32kstartupKeyName == "CYCLE3"):
        osc32kstartupDefaultValue = index

    osc32kstartupKeyDescription = osc32kctrlOSC32KStarupNodeValues[index].getAttribute("caption")
    osc32kstartupKeyValue= osc32kctrlOSC32KStarupNodeValues[index].getAttribute("value")
    osc32kctrlSym_OSC32K_STARTUP.addKey(osc32kstartupKeyName, osc32kstartupKeyValue , osc32kstartupKeyDescription)

osc32kctrlSym_OSC32K_STARTUP.setDefaultValue(osc32kstartupDefaultValue)
osc32kctrlSym_OSC32K_STARTUP.setOutputMode("Value")
osc32kctrlSym_OSC32K_STARTUP.setDisplayMode("Description")
osc32kctrlSym_OSC32K_STARTUP.setDependencies(setosc32kSTARTUPVisibleProperty, ["CONF_CLOCK_OSC32K_ENABLE"])

################################################################################
##########             GCLK Callback Functions            ######################
################################################################################

#GCLK Generator Control Configuration Enable Visible Property
def setgclkconfigenableVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Run Standby Visible Property
def setgenctrlRunInstandbyVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Output Enable Visible Property
def setgenctrlOEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Output Off Value Visible Property
def setgenctrlOOVVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Improve Duty Cycle Visible Property
def setgenctrlIDCVisibleProperty(symbol, event):
    if((event["value"] & 1 )== 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#GCLK Generator Control Division Selection Visible Property
def setgenctrlDIVSELVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Division Factor Visible Property
def setgenctrlDIVVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Generator Control Source Selection Visible Property
def setgenctrlSRCVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])


#GCLK Peripheral Channel Generator Visible Property
def setPCHCTRLGENVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#GCLK Peripheral Channel Write Lock visible Property
def setPCHCTRLWRTLOCKVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

################################################################################
#######          GCLK Database Components            ###########################
################################################################################

#GCLK Main Menu
gclkSym_Menu = coreComponent.createMenuSymbol("GCLK_MENU", clkMenu)
gclkSym_Menu.setLabel("GCLK Configuration")
gclkSym_Menu.setDescription("Configuration for the GCLK Generators")

global gclkSym_num,gclkSym_GENCTRL_DIVSEL,gclkSym_GENCTRL_DIV
gclkSym_num = []
gclkSym_GENCTRL_RUNSTDBY = []
gclkSym_GENCTRL_OE = []
gclkSym_GENCTRL_OOV = []
global gclkSym_GENCTRL_IDC
gclkSym_GENCTRL_IDC = []
gclkSym_GENCTRL_GENEN = []
gclkSym_GENCTRL_DIVSEL = []
gclkSym_GENCTRL_DIV = []
gclkSym_GENCTRL_SRC = []
gclkSym_index = []

for gclknumber in range(0,9):
    gclkSym_num.append(gclknumber)
    gclkSym_num[gclknumber] = coreComponent.createBooleanSymbol("GCLK_INST_NUM" + str(gclknumber),gclkSym_Menu)
    gclkSym_num[gclknumber].setLabel("Enable Generic Clock Generator " + str(gclknumber))
    gclkSym_num[gclknumber].setVisible(True)
    gclkSym_num[gclknumber].setDependencies(setgclkconfigenableVisibleProperty, ["GCLK_MENU"])
    if( gclknumber == 0):
        gclkSym_num[gclknumber].setValue(True,1)

    #GCLK Generator Run StandBy
    gclkSym_GENCTRL_RUNSTDBY.append(gclknumber)
    gclkSym_GENCTRL_RUNSTDBY[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_RUNSTDBY", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setLabel("GCLK should keep running in Standby mode")
    if(gclknumber != 0):
        gclkSym_GENCTRL_RUNSTDBY[gclknumber].setVisible(False)
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setDependencies(setgenctrlRunInstandbyVisibleProperty, ["GCLK_INST_NUM" + str(gclknumber)])

        #GCLK Generator Source Selection
    gclkSym_GENCTRL_SRC.append(gclknumber)
    gclkSym_GENCTRL_SRC[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_SRC", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_SRC[gclknumber].setLabel("Source Selection")
    if(gclknumber != 0):
        gclkSym_GENCTRL_SRC[gclknumber].setVisible(False)
    gclkSymsourceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_GENCTRL__SRC\"]")
    gclkSymsourceNodeValues = []
    gclkSymsourceNodeValues = gclkSymsourceNode.getChildren()
    glckgensrcDefaultValue = 0
    glckgensrcXOSCValue = 0
    for index in range(0, len(gclkSymsourceNodeValues)):
        glckgensrcKeyName = gclkSymsourceNodeValues[index].getAttribute("name")

        if (glckgensrcKeyName == "OSC48M"):
            glckgensrcDefaultValue = index
        elif (glckgensrcKeyName == "XOSC"):
            glckgensrcXOSCValue = index

        glckgensrcKeyDescription = gclkSymsourceNodeValues[index].getAttribute("caption")
        glckgensrcKeyValue = gclkSymsourceNodeValues[index].getAttribute("value")
        if((gclknumber > 0) and (glckgensrcKeyName == "GCLKGEN1")):
            Log.writeInfoMessage("nothing")
        else:
            gclkSym_GENCTRL_SRC[gclknumber].addKey(glckgensrcKeyName, glckgensrcKeyValue , glckgensrcKeyDescription)

    if(gclknumber == 0):
        gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(glckgensrcDefaultValue)
    else:
        gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(glckgensrcXOSCValue)
    gclkSym_GENCTRL_SRC[gclknumber].setOutputMode("Value")
    gclkSym_GENCTRL_SRC[gclknumber].setDisplayMode("Description")
    gclkSym_GENCTRL_SRC[gclknumber].setDependencies(setgenctrlSRCVisibleProperty, ["GCLK_INST_NUM" + str(gclknumber)])

    #GCLK Generator Output Enable
    gclkSym_GENCTRL_OE.append(gclknumber)
    gclkSym_GENCTRL_OE[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_OUTPUTENABLE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_OE[gclknumber].setLabel("Output GCLK clock signal on IO pin?")
    if(gclknumber != 0):
        gclkSym_GENCTRL_OE[gclknumber].setVisible(False)
    gclkSym_GENCTRL_OE[gclknumber].setDependencies(setgenctrlOEVisibleProperty, ["GCLK_INST_NUM" + str(gclknumber)])

    #GCLK Generator Output Off Value
    gclkSym_GENCTRL_OOV.append(gclknumber)
    gclkSym_GENCTRL_OOV[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_OUTPUTOFFVALUE", gclkSym_GENCTRL_OE[gclknumber])
    gclkSym_GENCTRL_OOV[gclknumber].setLabel("Output Off Value")
    if(gclknumber != 0):
        gclkSym_GENCTRL_OOV[gclknumber].setVisible(False)
    gclkSym_GENCTRL_OOV[gclknumber].addKey("LOW","0","Logic Level 0")
    gclkSym_GENCTRL_OOV[gclknumber].addKey("HIGH","1","Logic Level 1")
    gclkSym_GENCTRL_OOV[gclknumber].setDefaultValue(0)
    gclkSym_GENCTRL_OOV[gclknumber].setOutputMode("Key")
    gclkSym_GENCTRL_OOV[gclknumber].setDisplayMode("Description")
    gclkSym_GENCTRL_OOV[gclknumber].setDependencies(setgenctrlOOVVisibleProperty, ["GCLK_" + str(gclknumber) + "_OUTPUTENABLE"])

    #GCLK Generator Division Selection
    gclkSym_GENCTRL_DIVSEL.append(gclknumber)
    gclkSym_GENCTRL_DIVSEL[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_DIVSEL", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVSEL[gclknumber].setLabel("Divide Selection")
    if(gclknumber != 0):
        gclkSym_GENCTRL_DIVSEL[gclknumber].setVisible(False)
    gclkSymGenDivSelNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_GENCTRL__DIVSEL\"]")
    gclkSymGenDivSelNodeValues = []
    gclkSymGenDivSelNodeValues = gclkSymGenDivSelNode.getChildren()
    gclkSymGenDivSelDefaultValue = 0
    for index in range(0, len(gclkSymGenDivSelNodeValues)):
        gclkSymGenDivSelKeyName = gclkSymGenDivSelNodeValues[index].getAttribute("name")

        if (gclkSymGenDivSelKeyName == "DIV1"):
            gclkSymGenDivSelDefaultValue = index

        gclkSymGenDivSelKeyDescription = gclkSymGenDivSelNodeValues[index].getAttribute("caption")
        gclkSymGenDivSelKeyValue = gclkSymGenDivSelNodeValues[index].getAttribute("value")
        gclkSym_GENCTRL_DIVSEL[gclknumber].addKey(gclkSymGenDivSelKeyName, gclkSymGenDivSelKeyValue , gclkSymGenDivSelKeyDescription)

    gclkSym_GENCTRL_DIVSEL[gclknumber].setDefaultValue(gclkSymGenDivSelDefaultValue)
    gclkSym_GENCTRL_DIVSEL[gclknumber].setOutputMode("Key")
    gclkSym_GENCTRL_DIVSEL[gclknumber].setDisplayMode("Description")
    gclkSym_GENCTRL_DIVSEL[gclknumber].setDependencies(setgenctrlDIVSELVisibleProperty, ["GCLK_INST_NUM" + str(gclknumber)])

    #GCLK Generator Division Factor
    gclkSym_GENCTRL_DIV.append(gclknumber)
    gclkSym_GENCTRL_DIV[gclknumber] = coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_DIV", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIV[gclknumber].setLabel("Division Factor")
    if(gclknumber != 0):
        gclkSym_GENCTRL_DIV[gclknumber].setVisible(False)
    if(gclknumber == 1):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFFFF)
    else:
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFF)
    gclkSym_GENCTRL_DIV[gclknumber].setDependencies(setgenctrlDIVVisibleProperty, ["GCLK_INST_NUM" + str(gclknumber)])

    #GCLK Generator Improve Duty Cycle
    gclkSym_GENCTRL_IDC.append(gclknumber)
    gclkSym_GENCTRL_IDC[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_IMPROVE_DUTYCYCLE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_IDC[gclknumber].setLabel("Enable 50/50 Duty Cycle")
    gclkSym_GENCTRL_IDC[gclknumber].setVisible(False)
    gclkSym_GENCTRL_IDC[gclknumber].setDependencies(setgenctrlIDCVisibleProperty, ["GCLK_" + str(gclknumber) + "_DIV" ])



#GCLK Peripheral Channel Menu
gclkSym_PerChannel_sel = coreComponent.createMenuSymbol("PERI_CHAN_SEL",gclkSym_Menu)
gclkSym_PerChannel_sel.setLabel("Peripheral Channel Settings")

maxGCLKId = 0

atdfFilePath = join(Variables.get("__DFP_PACK_DIR") , "atdf" , Variables.get("__PROCESSOR") + ".atdf")

try:
    atdfFile = open(atdfFilePath, "r")
except:
    Log.writeInfoMessage("clk.py peripheral clock: Error!!! while opening atdf file")

atdfContent = ElementTree.fromstring(atdfFile.read())

# parse atdf xml file to get instance name
# for the peripheral which has gclk id
for peripheral in atdfContent.iter("module"):
    for instance in peripheral.iter("instance"):
        for param in instance.iter("param"):
            if "GCLK_ID" in param.attrib["name"]:

                symbolId = "GCLK_ID_" + str(maxGCLKId)
                indexID = param.attrib["value"]
                symbolValue = instance.attrib["name"] + param.attrib["name"].split("GCLK_ID")[1]

                #GCLK Peripheral Channel Enable
                clkSymPeripheral = coreComponent.createBooleanSymbol(symbolId + "_CHEN", gclkSym_PerChannel_sel)
                clkSymPeripheral.setLabel(symbolValue + " Clock Channel Enable")
                # clkSymPeripheral.setDefaultValue(False)
                # clkSymPeripheral.setReadOnly(True)

                #GCLK Peripheral Channel Name
                gclkSym_PERCHANNEL_NAME = coreComponent.createStringSymbol(symbolId + "_NAME", clkSymPeripheral)
                gclkSym_PERCHANNEL_NAME.setLabel(symbolValue)
                gclkSym_PERCHANNEL_NAME.setVisible(False)
                gclkSym_PERCHANNEL_NAME.setDefaultValue(symbolValue)

                #GCLK Peripheral Channel Index
                gclkSym_PERCHANNEL_INDEX = coreComponent.createIntegerSymbol(symbolId + "_INDEX", clkSymPeripheral)
                gclkSym_PERCHANNEL_INDEX.setVisible(False)
                gclkSym_PERCHANNEL_INDEX.setDefaultValue(int(indexID))

                #Peripheral Channel Generator Selection
                gclkSym_PCHCTRL_GEN = coreComponent.createKeyValueSetSymbol(symbolId + "_GENSEL", clkSymPeripheral)
                gclkSym_PCHCTRL_GEN.setLabel("Generator Selection")
                gclkSym_PCHCTRL_GEN.setVisible(False)

                gclkSymPCHCTRLGenNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_PCHCTRL__GEN\"]")
                gclkSymPCHCTRLGenNodeValues = []
                gclkSymPCHCTRLGenNodeValues = gclkSymPCHCTRLGenNode.getChildren()

                gclkSymPCHCTRLGenDefaultValue = 0

                for index in range(0, len(gclkSymPCHCTRLGenNodeValues)):
                    gclkSymPCHCTRLGenKeyName = gclkSymPCHCTRLGenNodeValues[index].getAttribute("name")

                    if (gclkSymPCHCTRLGenKeyName == "GCLK0"):
                        gclkSymPCHCTRLGenDefaultValue = index

                    gclkSymPCHCTRLGenKeyDescription = gclkSymPCHCTRLGenNodeValues[index].getAttribute("caption")
                    ggclkSymPCHCTRLGenKeyValue = gclkSymPCHCTRLGenNodeValues[index].getAttribute("value")
                    gclkSym_PCHCTRL_GEN.addKey(gclkSymPCHCTRLGenKeyName, ggclkSymPCHCTRLGenKeyValue , gclkSymPCHCTRLGenKeyDescription)

                gclkSym_PCHCTRL_GEN.setDefaultValue(gclkSymPCHCTRLGenDefaultValue)
                gclkSym_PCHCTRL_GEN.setOutputMode("Value")
                gclkSym_PCHCTRL_GEN.setDisplayMode("Description")
                gclkSym_PCHCTRL_GEN.setDependencies(setPCHCTRLGENVisibleProperty, [symbolId + "_CHEN"])

                #GCLK Peripheral Channel Lock
                gclkSym_PCHCTRL_WRTLOCK = coreComponent.createBooleanSymbol(symbolId + "_WRITELOCK", clkSymPeripheral)
                gclkSym_PCHCTRL_WRTLOCK.setLabel("Write Lock")
                gclkSym_PCHCTRL_WRTLOCK.setVisible(False)
                gclkSym_PCHCTRL_WRTLOCK.setDependencies(setPCHCTRLWRTLOCKVisibleProperty, [symbolId + "_CHEN"])

                maxGCLKId += 1

gclkSym_PeriIdMax = coreComponent.createIntegerSymbol("GCLK_MAX_ID", clkSymPeripheral)
gclkSym_PeriIdMax.setVisible(False)
gclkSym_PeriIdMax.setDefaultValue(int(maxGCLKId))

################################################################################
##########              MCLK Callback Functions            #####################
################################################################################

#MCLK AHB Clocks Visible Property
def setAHBCLOCKENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#MCLK APBA Clocks Visible Property
def setAPBACLOCKENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#MCLK APBB Clock Visible Property
def setAPBBCLOCKENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#MCLK APBC Clocks Visible Property
def setAPBCCLOCKENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#MCLK APBD Clocks Visible Property
def setAPBDCLOCKENABLEVisibleProperty(symbol, event):
    symbol.setVisible(event["value"])

#MCLK AHB Clocks Value Set Property
def setAHBCLOCKvalue(symbol, event):
    symbol.clearValue()
    if event["id"] == "CONFIG_AHB_APBA_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_APBB_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_APBC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_DSU_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_HMATRIXHS_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_NVMCTRL_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_HSRAM_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_DMAC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_CAN0_CLOCK" and event["value"] == True:
        symbol.setValue(0x100,2)
    elif event["id"] == "CONFIG_AHB_CAN1_CLOCK" and event["value"] == True:
        symbol.setValue(0x200,2)
    elif event["id"] == "CONFIG_AHB_PAC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_DIVAS_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_AHB_APBD_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)

#MCLK APBA Clocks Value Set Property
def setAPBACLOCKvalue(symbol, event):
    symbol.clearValue()
    if event["id"] == "CONFIG_APBA_PAC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_PM_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_MCLK_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_RSTC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_OSCCTRL_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_OSC32KCTRL_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_SUPC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_GCLK_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_WDT_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_RTC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_EIC_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_FREQM_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBA_TSENS_CLOCK" and event["value"] == True:
        symbol.setValue(0x1000,2)

#MCLK APBB Clocks Value Set Property
def setAPBBCLOCKvalue(symbol, event):
    symbol.clearValue()
    if event["id"] == "CONFIG_APBB_PORT_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBB_DSU_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBB_NVMCTRL_CLOCK" and event["value"] == False:
        symbol.setValue(0x00,2)
    elif event["id"] == "CONFIG_APBB_HMATRIXHS_CLOCK" and event["value"] == True:
        symbol.setValue(0x20,2)

#MCLK APBC Clocks Value Set Property
def setAPBCCLOCKvalue(symbol, event):
    symbol.clearValue()
    if event["id"] == "CONFIG_APBC_EVSYS_CLOCK" and event["value"] == True:
        symbol.setValue(0x01,2)
    elif event["id"] == "CONFIG_APBC_SERCOM0_CLOCK" and event["value"] == True:
        symbol.setValue(0x02,2)
    elif event["id"] == "CONFIG_APBC_SERCOM1_CLOCK" and event["value"] == True:
        symbol.setValue(0x04,2)
    elif event["id"] == "CONFIG_APBC_SERCOM2_CLOCK" and event["value"] == True:
        symbol.setValue(0x08,2)
    elif event["id"] == "CONFIG_APBC_SERCOM3_CLOCK" and event["value"] == True:
        symbol.setValue(0x10,2)
    elif event["id"] == "CONFIG_APBC_SERCOM4_CLOCK" and event["value"] == True:
        symbol.setValue(0x20,2)
    elif event["id"] == "CONFIG_APBC_SERCOM5_CLOCK" and event["value"] == True:
        symbol.setValue(0x40,2)
    elif event["id"] == "CONFIG_APBC_TCC0_CLOCK" and event["value"] == True:
        symbol.setValue(0x200,2)
    elif event["id"] == "CONFIG_APBC_TCC1_CLOCK" and event["value"] == True:
        symbol.setValue(0x400,2)
    elif event["id"] == "CONFIG_APBC_TCC2_CLOCK" and event["value"] == True:
        symbol.setValue(0x800,2)
    elif event["id"] == "CONFIG_APBC_TC0_CLOCK" and event["value"] == True:
        symbol.setValue(0x1000,2)
    elif event["id"] == "CONFIG_APBC_TC1_CLOCK" and event["value"] == True:
        symbol.setValue(0x2000,2)
    elif event["id"] == "CONFIG_APBC_TC2_CLOCK" and event["value"] == True:
        symbol.setValue(0x4000,2)
    elif event["id"] == "CONFIG_APBC_TC3_CLOCK" and event["value"] == True:
        symbol.setValue(0x8000,2)
    elif event["id"] == "CONFIG_APBC_TC4_CLOCK" and event["value"] == True:
        symbol.setValue(0x10000,2)
    elif event["id"] == "CONFIG_APBC_ADC0_CLOCK" and event["value"] == True:
        symbol.setValue(0x20000,2)
    elif event["id"] == "CONFIG_APBC_ADC1_CLOCK" and event["value"] == True:
        symbol.setValue(0x40000,2)
    elif event["id"] == "CONFIG_APBC_SDADC_CLOCK" and event["value"] == True:
        symbol.setValue(0x80000,2)
    elif event["id"] == "CONFIG_APBC_AC_CLOCK" and event["value"] == True:
        symbol.setValue(0x100000,2)
    elif event["id"] == "CONFIG_APBC_DAC_CLOCK" and event["value"] == True:
        symbol.setValue(0x200000,2)
    elif event["id"] == "CONFIG_APBC_PTC_CLOCK" and event["value"] == True:
        symbol.setValue(0x400000,2)
    elif event["id"] == "CONFIG_APBC_CCL_CLOCK" and event["value"] == True:
        symbol.setValue(0x800000,2)

#MCLK APBD Clocks Value Set Property
def setAPBDCLOCKvalue(symbol, event):
    symbol.clearValue()
    if event["id"] == "CONFIG_APBD_SERCOM6_CLOCK" and event["value"] == True:
        symbol.setValue(0x01,2)
    elif event["id"] == "CONFIG_APBD_SERCOM7_CLOCK" and event["value"] == True:
        symbol.setValue(0x02,2)
    elif event["id"] == "CONFIG_APBD_TC5_CLOCK" and event["value"] == True:
        symbol.setValue(0x04,2)
    elif event["id"] == "CONFIG_APBD_TC6_CLOCK" and event["value"] == True:
        symbol.setValue(0x08,2)
    elif event["id"] == "CONFIG_APBD_TC7_CLOCK" and event["value"] == True:
        symbol.setValue(0x10,2)

#MCLK AHB Bridge Initial Value set Property
def ahbInitialValueset(symbol, event):
    ahbClockValue = 0
    for ahbclocknames in range(0,len(ahbclocks)):
        ahbClockGetValue= Database.getSymbolValue("core", "CONFIG_AHB_"+ahbclocks[ahbclocknames]+"_Value")
        ahbClockValue = ahbClockValue | ahbClockGetValue

    ahbClockValue = 0x800 | ahbClockValue
    Log.writeInfoMessage("ahb Clock Value is"+str(ahbClockValue))
    symbol.clearValue()
    symbol.setValue(ahbClockValue,2)

#MCLK APBA Bridge Initial Value set Property
def APBAInitialValueset(symbol, event):
    apbAClockValue = 0
    for apbAclocknames in range(0,len(apbAclocks)):
        apbAClockGetValue= Database.getSymbolValue("core", "CONFIG_APBA_"+apbAclocks[apbAclocknames]+"_Value")
        apbAClockValue = apbAClockValue | apbAClockGetValue

    Log.writeInfoMessage("apbA Clock Value is"+str(apbAClockValue))
    symbol.clearValue()
    symbol.setValue(apbAClockValue,2)

#MCLK APBB Bridge Initial Value set Property
def APBBInitialValueset(symbol, event):
    apbBClockValue = 0
    for apbBclocknames in range(0,len(apbBclocks)):
        apbBClockGetValue= Database.getSymbolValue("core", "CONFIG_APBB_"+apbBclocks[apbBclocknames]+"_Value")
        apbBClockValue = apbBClockValue | apbBClockGetValue

    Log.writeInfoMessage("apbB Clock Value is"+str(apbBClockValue))
    symbol.clearValue()
    symbol.setValue(apbBClockValue,2)

#MCLK APBC Bridge Initial Value set Property
def APBCInitialValueset(symbol, event):
    apbCClockValue = 0
    for apbCclocknames in range(0,len(apbCclocks)):
        apbCClockGetValue= Database.getSymbolValue("core", "CONFIG_APBC_"+apbCclocks[apbCclocknames]+"_Value")
        apbCClockValue = apbCClockValue | apbCClockGetValue

    Log.writeInfoMessage("apbC Clock Value is"+str(apbCClockValue))
    symbol.clearValue()
    symbol.setValue(apbCClockValue,2)

#MCLK APBD Bridge Initial Value set Property
def APBDInitialValueset(symbol, event):
    apbDClockValue = 0
    for apbDclocknames in range(0,len(apbDclocks)):
        apbDClockGetValue= Database.getSymbolValue("core", "CONFIG_APBD_"+apbDclocks[apbDclocknames]+"_Value")
        apbDClockValue = apbDClockValue | apbDClockGetValue

    Log.writeInfoMessage("apbD Clock Value is"+str(apbDClockValue))
    symbol.clearValue()
    symbol.setValue(apbDClockValue,2)

################################################################################
#######          MCLK Database Components            ###########################
################################################################################

#MCLK Main Menu
mclkSym_Menu = coreComponent.createMenuSymbol("MCLK_MENU", clkMenu)
mclkSym_Menu.setLabel("MCLK Configuration")

#MCLK CPU Division
mclkSym_CPUDIV_CPUDIV = coreComponent.createKeyValueSetSymbol("CONF_CPU_CLOCK_DIVIDER",mclkSym_Menu)
mclkSym_CPUDIV_CPUDIV.setLabel("CPU Clock Division Factor")
mclkSym_CPUDIV_CPUDIV.setVisible(True)
mclkcpudivNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCLK\"]/value-group@[name=\"MCLK_CPUDIV__CPUDIV\"]")
mclkcpudivNodeValues = []
mclkcpudivNodeValues = mclkcpudivNode.getChildren()
mclkcpudivDefaultValue = 0
for index in range(0, len(mclkcpudivNodeValues)):
    mclkcpudivKeyName= mclkcpudivNodeValues[index].getAttribute("name")

    if (mclkcpudivKeyName == "DIV1"):
        mclkcpudivDefaultValue = index

    mclkcpudivKeyDescription = mclkcpudivNodeValues[index].getAttribute("caption")
    mclkcpudivKeyValue = mclkcpudivNodeValues[index].getAttribute("value")
    mclkSym_CPUDIV_CPUDIV.addKey(mclkcpudivKeyName, mclkcpudivKeyValue , mclkcpudivKeyDescription)

mclkSym_CPUDIV_CPUDIV.setDefaultValue(mclkcpudivDefaultValue)
mclkSym_CPUDIV_CPUDIV.setOutputMode("Value")
mclkSym_CPUDIV_CPUDIV.setDisplayMode("Description")

#MCLK AHB Menu
mclkSym_AHBMASK_SETTINGS = coreComponent.createMenuSymbol("AHB_BRIDGE_SETTINGS",mclkSym_Menu)
mclkSym_AHBMASK_SETTINGS.setLabel("AHB Bridge Clock Settings ")

global ahbclocks

ahbclocks = ["APBA", "APBB", "APBC", "DSU", "HMATRIXHS", "NVMCTRL",
             "HSRAM", "DMAC", "CAN0", "CAN1", "PAC", "DIVAS", "APBD"]

global mclkSym_AHBMASK_CLOCKEN,mclkSym_AHBMASK_CLOCKValue

mclkSym_AHBMASK_CLOCKEN = []
mclkSym_AHBMASK_CLOCKValue = []
ahbBridgeList = []

for ahbclockname in range(0,len(ahbclocks)):
    mclkSym_AHBMASK_CLOCKEN.append(ahbclockname)
    #MCLK AHB Channels Enable
    mclkSym_AHBMASK_CLOCKEN[ahbclockname] = coreComponent.createBooleanSymbol("CONFIG_AHB_" + ahbclocks[ahbclockname] + "_CLOCK",mclkSym_AHBMASK_SETTINGS)
    mclkSym_AHBMASK_CLOCKEN[ahbclockname].setLabel("Enable AHB Clock to "+ahbclocks[ahbclockname])
    if ((ahbclockname == 8) or (ahbclockname == 9 )):
        mclkSym_AHBMASK_CLOCKEN[ahbclockname].setDefaultValue(0)
    else:
        mclkSym_AHBMASK_CLOCKEN[ahbclockname].setDefaultValue(1)

    mclkSym_AHBMASK_CLOCKValue.append(ahbclockname)
    mclkSym_AHBMASK_CLOCKValue[ahbclockname] = coreComponent.createIntegerSymbol("CONFIG_AHB_" + ahbclocks[ahbclockname] + "_Value",mclkSym_AHBMASK_SETTINGS)
    if ahbclockname == 0 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x1)
    elif ahbclockname == 1 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x2)
    elif ahbclockname == 2 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x04)
    elif ahbclockname == 3 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x08)
    elif ahbclockname == 4 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x10)
    elif ahbclockname == 5 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x20)
    elif ahbclockname == 6 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x40)
    elif ahbclockname == 7 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x80)
    elif ahbclockname == 10 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x400)
    elif ahbclockname == 11 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x1000)
    elif ahbclockname == 12 :
        mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDefaultValue(0x2000)

    mclkSym_AHBMASK_CLOCKValue[ahbclockname].setVisible(False)
    mclkSym_AHBMASK_CLOCKValue[ahbclockname].setDependencies(setAHBCLOCKvalue, ["CONFIG_AHB_" + ahbclocks[ahbclockname] + "_CLOCK"])

    ahbBridgeList.append("CONFIG_AHB_" + ahbclocks[ahbclockname] + "_Value")

#AHB Bridge Clock Initial Settings
mclk_AHB_Clock_Value = coreComponent.createIntegerSymbol("MCLK_AHB_INITIAL_VALUE",None)
mclk_AHB_Clock_Value.setDefaultValue(0x3CFF)
mclk_AHB_Clock_Value.setVisible(False)
mclk_AHB_Clock_Value.setDependencies(ahbInitialValueset, ahbBridgeList)

#MCLK APBA Menu
mclkSym_APBAMASK_SETTINGS = coreComponent.createMenuSymbol("APBA_BRIDGE_SETTINGS",mclkSym_Menu)
mclkSym_APBAMASK_SETTINGS.setLabel("APBA Bridge Clock Settings ")

global apbAclocks

apbAclocks = ["PAC", "PM", "MCLK", "RSTC", "OSCCTRL", "OSC32KCTRL",
              "SUPC", "GCLK", "WDT", "RTC", "EIC", "FREQM", "TSENS"]

global mclkSym_APBAMASK_CLOCKEN

mclkSym_APBAMASK_CLOCKEN = []
mclkSym_APBAMASK_CLOCKValue = []
apbABridgeList = []

for apbAclockname in range(0,len(apbAclocks)):
    mclkSym_APBAMASK_CLOCKEN.append(apbAclockname)
    #MCLK APBA Channels Enable
    mclkSym_APBAMASK_CLOCKEN[apbAclockname] = coreComponent.createBooleanSymbol("CONFIG_APBA_" + apbAclocks[apbAclockname] + "_CLOCK",mclkSym_APBAMASK_SETTINGS)
    mclkSym_APBAMASK_CLOCKEN[apbAclockname].setLabel("Enable APBA Clock to " + apbAclocks[apbAclockname])
    if apbAclockname == 12:
        mclkSym_APBAMASK_CLOCKEN[apbAclockname].setDefaultValue(0)
    else:
        mclkSym_APBAMASK_CLOCKEN[apbAclockname].setDefaultValue(1)

    mclkSym_APBAMASK_CLOCKValue.append(apbAclockname)
    mclkSym_APBAMASK_CLOCKValue[apbAclockname] = coreComponent.createHexSymbol("CONFIG_APBA_" + apbAclocks[apbAclockname] + "_Value",mclkSym_APBAMASK_SETTINGS)
    if apbAclockname == 0 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x1)
    elif apbAclockname == 1 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x2)
    elif apbAclockname == 2 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x04)
    elif apbAclockname == 3 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x08)
    elif apbAclockname == 4 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x10)
    elif apbAclockname == 5 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x20)
    elif apbAclockname == 6 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x40)
    elif apbAclockname == 7 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x80)
    elif apbAclockname == 8 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x100)
    elif apbAclockname == 9 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x200)
    elif apbAclockname == 10 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x400)
    elif apbAclockname == 11 :
        mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDefaultValue(0x800)

    mclkSym_APBAMASK_CLOCKValue[apbAclockname].setVisible(False)
    mclkSym_APBAMASK_CLOCKValue[apbAclockname].setDependencies(setAPBACLOCKvalue, ["CONFIG_APBA_" + apbAclocks[apbAclockname] + "_CLOCK"])

    apbABridgeList.append("CONFIG_APBA_" + apbAclocks[apbAclockname] + "_Value")

#APBA Bridge Clock Initial Settings
mclk_APBA_Clock_Value = coreComponent.createIntegerSymbol("MCLK_APBA_INITIAL_VALUE",None)
mclk_APBA_Clock_Value.setDefaultValue(0xFFF)
mclk_APBA_Clock_Value.setVisible(False)
mclk_APBA_Clock_Value.setDependencies(APBAInitialValueset,apbABridgeList)

#MCLK APBB Menu
mclkSym_APBBMASK_SETTINGS = coreComponent.createMenuSymbol("APBB_BRIDGE_SETTINGS",mclkSym_Menu)
mclkSym_APBBMASK_SETTINGS.setLabel("APBB Bridge Clock Settings ")

global apbBclocks

apbBclocks = ["PORT", "DSU", "NVMCTRL", "HMATRIXHS"]

global mclkSym_APBBMASK_CLOCKEN

mclkSym_APBBMASK_CLOCKEN = []
mclkSym_APBBMASK_CLOCKValue = []
apbBBridgeList = []

for apbBclockname in range(0,len(apbBclocks)):
    mclkSym_APBBMASK_CLOCKEN.append(apbBclockname)
    #MCLK APBB Channels Enable
    mclkSym_APBBMASK_CLOCKEN[apbBclockname] = coreComponent.createBooleanSymbol("CONFIG_APBB_" + apbBclocks[apbBclockname] + "_CLOCK",mclkSym_APBBMASK_SETTINGS)
    mclkSym_APBBMASK_CLOCKEN[apbBclockname].setLabel("Enable APBB Clock to " + apbBclocks[apbBclockname])
    if apbBclockname == 3:
        mclkSym_APBBMASK_CLOCKEN[apbBclockname].setDefaultValue(0)
    else:
        mclkSym_APBBMASK_CLOCKEN[apbBclockname].setDefaultValue(1)

    mclkSym_APBBMASK_CLOCKValue.append(apbBclockname)
    mclkSym_APBBMASK_CLOCKValue[apbBclockname] = coreComponent.createHexSymbol("CONFIG_APBB_" + apbBclocks[apbBclockname] + "_Value",mclkSym_APBBMASK_SETTINGS)
    if apbBclockname == 0 :
        mclkSym_APBBMASK_CLOCKValue[apbBclockname].setDefaultValue(0x1)
    elif apbBclockname == 1 :
        mclkSym_APBBMASK_CLOCKValue[apbBclockname].setDefaultValue(0x2)
    elif apbBclockname == 2 :
        mclkSym_APBBMASK_CLOCKValue[apbBclockname].setDefaultValue(0x04)

    mclkSym_APBBMASK_CLOCKValue[apbBclockname].setVisible(False)
    mclkSym_APBBMASK_CLOCKValue[apbBclockname].setDependencies(setAPBBCLOCKvalue, ["CONFIG_APBB_" + apbBclocks[apbBclockname] + "_CLOCK"])

    apbBBridgeList.append("CONFIG_APBB_" + apbBclocks[apbBclockname] + "_Value")

#APBB Bridge Clock Initial Settings
mclk_APBB_Clock_Value = coreComponent.createIntegerSymbol("MCLK_APBB_INITIAL_VALUE",None)
mclk_APBB_Clock_Value.setDefaultValue(0x07)
mclk_APBB_Clock_Value.setVisible(False)
mclk_APBB_Clock_Value.setDependencies(APBBInitialValueset,apbBBridgeList)

#MCLK APBC Menu
mclkSym_APBCMASK_SETTINGS = coreComponent.createMenuSymbol("APBC_BRIDGE_SETTINGS",mclkSym_Menu)
mclkSym_APBCMASK_SETTINGS.setLabel("APBC Bridge Clock Settings ")

global apbCclocks

apbCclocks = ["EVSYS", "SERCOM0", "SERCOM1", "SERCOM2", "SERCOM3", "SERCOM4",
                "SERCOM5", "TCC0", "TCC1", "TCC2", "TC0", "TC1", "TC2", "TC3",
                "TC4", "ADC0", "ADC1", "SDADC", "AC", "DAC", "PTC", "CCL"]

global mclkSym_APBCMASK_CLOCKEN

mclkSym_APBCMASK_CLOCKEN = []
mclkSym_APBCMASK_CLOCKValue = []
apbCBridgeList = []

for apbCclockname in range(0,len(apbCclocks)):
    mclkSym_APBCMASK_CLOCKEN.append(apbCclockname)
    #MCLK APBC Channels Enable
    mclkSym_APBCMASK_CLOCKEN[apbCclockname] = coreComponent.createBooleanSymbol("CONFIG_APBC_" + apbCclocks[apbCclockname] + "_CLOCK",mclkSym_APBCMASK_SETTINGS)
    mclkSym_APBCMASK_CLOCKEN[apbCclockname].setLabel("Enable APBC Clock to " + apbCclocks[apbCclockname])
    mclkSym_APBCMASK_CLOCKEN[apbCclockname].setVisible(True)

    mclkSym_APBCMASK_CLOCKValue.append(apbCclockname)
    mclkSym_APBCMASK_CLOCKValue[apbCclockname] = coreComponent.createHexSymbol("CONFIG_APBC_" + apbCclocks[apbCclockname] + "_Value",mclkSym_APBCMASK_SETTINGS)
    mclkSym_APBCMASK_CLOCKValue[apbCclockname].setVisible(False)
    mclkSym_APBCMASK_CLOCKValue[apbCclockname].setDependencies(setAPBCCLOCKvalue, ["CONFIG_APBC_" + apbCclocks[apbCclockname] + "_CLOCK"])

    apbCBridgeList.append("CONFIG_APBC_" + apbCclocks[apbCclockname] + "_Value")

#APBC Bridge Clock Initial Settings
mclk_APBC_Clock_Value = coreComponent.createIntegerSymbol("MCLK_APBC_INITIAL_VALUE",None)
mclk_APBC_Clock_Value.setDefaultValue(0x00)
mclk_APBC_Clock_Value.setVisible(False)
mclk_APBC_Clock_Value.setDependencies(APBCInitialValueset,apbCBridgeList)

#MCLK APBD Menu
mclkSym_APBDMASK_SETTINGS = coreComponent.createMenuSymbol("APBD_BRIDGE_SETTINGS",mclkSym_Menu)
mclkSym_APBDMASK_SETTINGS.setLabel("APBD Bridge Clock Settings ")

global apbDclocks

apbDclocks = ["SERCOM6", "SERCOM7", "TC5", "TC6", "TC7"]

global mclkSym_APBDMASK_CLOCKEN

mclkSym_APBDMASK_CLOCKEN = []
mclkSym_APBDMASK_CLOCKValue = []
apbDBridgeList = []

#MCLK APBD Menu
for apbDclockname in range(0,len(apbDclocks)):
    mclkSym_APBDMASK_CLOCKEN.append(apbDclockname)
    #MCLK APBD Channels Enable
    mclkSym_APBDMASK_CLOCKEN[apbDclockname] = coreComponent.createBooleanSymbol("CONFIG_APBD_" + apbDclocks[apbDclockname] + "_CLOCK",mclkSym_APBDMASK_SETTINGS)
    mclkSym_APBDMASK_CLOCKEN[apbDclockname].setLabel("Enable APBD Clock for "+apbDclocks[apbDclockname])
    mclkSym_APBDMASK_CLOCKEN[apbDclockname].setVisible(True)

    mclkSym_APBDMASK_CLOCKValue.append(apbDclockname)
    mclkSym_APBDMASK_CLOCKValue[apbDclockname] = coreComponent.createHexSymbol("CONFIG_APBD_" + apbDclocks[apbDclockname] + "_Value",mclkSym_APBDMASK_SETTINGS)
    mclkSym_APBDMASK_CLOCKValue[apbDclockname].setVisible(False)
    mclkSym_APBDMASK_CLOCKValue[apbDclockname].setDependencies(setAPBDCLOCKvalue, ["CONFIG_APBD_" + apbDclocks[apbDclockname] + "_CLOCK"])

    apbDBridgeList.append("CONFIG_APBD_" + apbDclocks[apbDclockname] + "_Value")

#APBD Bridge Clock Initial Settings
mclk_APBD_Clock_Value = coreComponent.createIntegerSymbol("MCLK_APBD_INITIAL_VALUE",None)
mclk_APBD_Clock_Value.setDefaultValue(0x00)
mclk_APBD_Clock_Value.setVisible(False)
mclk_APBD_Clock_Value.setDependencies(APBDInitialValueset,apbDBridgeList)

################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clockSym_OSCCTRL_HeaderFile = coreComponent.createFileSymbol("SAMC21_CLOCK_HEADER", None)
clockSym_OSCCTRL_HeaderFile.setSourcePath("../peripheral/clk_sam_c20_c21/templates/plib_clock.h.ftl")
clockSym_OSCCTRL_HeaderFile.setOutputName("plib_clock.h")
clockSym_OSCCTRL_HeaderFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setType("HEADER")
clockSym_OSCCTRL_HeaderFile.setMarkup(True)

clockSym_OSCCTRL_SourceFile = coreComponent.createFileSymbol("SAMC21_CLOCK_SOURCE", None)
clockSym_OSCCTRL_SourceFile.setSourcePath("../peripheral/clk_sam_c20_c21/templates/plib_clock.c.ftl")
clockSym_OSCCTRL_SourceFile.setOutputName("plib_clock.c")
clockSym_OSCCTRL_SourceFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setType("SOURCE")
clockSym_OSCCTRL_SourceFile.setMarkup(True)

clockSystemInitFile = coreComponent.createFileSymbol("SAMC21_CLOCK_INIT", None)
clockSystemInitFile.setType("STRING")
clockSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
clockSystemInitFile.setSourcePath("../peripheral/clk_sam_c20_c21/templates/system/initialization.c.ftl")
clockSystemInitFile.setMarkup(True)

clockSystemDefFile = coreComponent.createFileSymbol("SAMC21_CLOCK_SYS_DEF", None)
clockSystemDefFile.setType("STRING")
clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clockSystemDefFile.setSourcePath("../peripheral/clk_sam_c20_c21/templates/system/definitions.h.ftl")
clockSystemDefFile.setMarkup(True)
