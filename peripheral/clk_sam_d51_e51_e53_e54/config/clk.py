"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

from collections import defaultdict
from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage(
    "Loading osctrl Manager for " + Variables.get("__PROCESSOR"))

oscctrlXosc_Menu = []
dpll_Menu = []
global topsort
clkMenu = coreComponent.createMenuSymbol("SAME54_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")

# Clock Source Configuration
clkSourceMenu = coreComponent.createMenuSymbol("CLOCK_SOURCE", clkMenu)
clkSourceMenu.setLabel("Clock Source Configuration")

for index in range(0, 2):
    oscctrlXosc_Menu.append(index)
    oscctrlXosc_Menu[index] = coreComponent.createMenuSymbol(
        "XOSCCTRL_MENU" + str(index), clkSourceMenu)
    oscctrlXosc_Menu[index].setLabel(
        "External Crystal Oscillator" + str(index) + " Configuration")

for index in range(0, 2):
    dpll_Menu.append(index)
    dpll_Menu[index] = coreComponent.createMenuSymbol(
        "FDPLL MENU" + str(index), clkSourceMenu)
    dpll_Menu[index].setLabel(
        "Fractional DPLL (FDPLL) " + str(index) + " Configuration")

dfll_Menu = coreComponent.createMenuSymbol("DFLL MENU", clkSourceMenu)
dfll_Menu.setLabel("DFLL Configuration")

xosc32k_Menu = coreComponent.createMenuSymbol("XOSC32K_MENU", clkSourceMenu)
xosc32k_Menu.setLabel("32Khz External Oscillator Configuration")

# Clock Generator Configuration
clkGen_Menu = coreComponent.createMenuSymbol("GCLK_MENU", clkMenu)
clkGen_Menu.setLabel("Generic Clock Configuration")

gclkGen_Menu = coreComponent.createMenuSymbol("GCLK_GEN_MENU", clkGen_Menu)
gclkGen_Menu.setLabel("Generator Configuration")

gclkPeriChannel_menu = coreComponent.createMenuSymbol(
    "GCLK_PERI_MENU", clkGen_Menu)
gclkPeriChannel_menu.setLabel("Peripheral Channel Configuration")

# Main Clock Configuration
mclkSym_Menu = coreComponent.createMenuSymbol("MCLK_MENU", clkMenu)
mclkSym_Menu.setLabel("Main Clock Configuration")

# Peripheral Clock Configuration
peripheralClockMenu = coreComponent.createMenuSymbol(
    "PERIPHERAL_CLOCK_MENU", clkMenu)
peripheralClockMenu.setLabel("Peripheral Clock Configuration")

# Calculated Frequency Menu
calculatedFreq_Menu = coreComponent.createMenuSymbol("FREQ_MENU", clkMenu)
calculatedFreq_Menu.setLabel("Calculated Clock Frequencies")

#################################################################################################
################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC Configuration callback functions    ###############################


def setXOSCFreq(symbol, event):
    index = event["id"].split("CONFIG_CLOCK_XOSC")[1][0]
    enable = Database.getSymbolValue(
        "core", "CONFIG_CLOCK_XOSC" + index + "_ENABLE")

    if enable:
        symbol.setValue(Database.getSymbolValue(
            "core", "CONFIG_CLOCK_XOSC" + index + "_FREQUENCY"), 1)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)


####    DPLL Configuration Callback Functions    ###############################

def setDPLLClockFreq(symbol, event):

    index = symbol.getID().split("DPLL")[1][0]
    enable = Database.getSymbolValue(
        "core", "CONFIG_CLOCK_DPLL" + index + "_ENABLE")

    if enable:
        clockSrc = Database.getSymbolValue(
            "core", "CONFIG_CLOCK_DPLL" + index + "_REF_CLOCK")

        # XOSC32K Clock
        if clockSrc == 0:
            srcFreq = Database.getSymbolValue("core", "XOSC32K_FREQ")

            # XOSC0 Clock
        elif clockSrc == 1:
                divisor = int(Database.getSymbolValue(
                    "core", "CONFIG_CLOCK_DPLL" + index + "_DIVIDER"))
                srcFreq = int(Database.getSymbolValue(
                    "core", "XOSC0_FREQ")) / (2 * (divisor + 1))

            # XOSC1 Clock
        elif clockSrc == 2:
                divisor = int(Database.getSymbolValue(
                    "core", "CONFIG_CLOCK_DPLL" + index + "_DIVIDER"))
                srcFreq = int(Database.getSymbolValue(
                    "core", "XOSC1_FREQ")) / (2 * (divisor + 1))

            # GCLK_DPLL Clock
        elif clockSrc == 3:
                srcFreq = int(Database.getSymbolValue("core", "GCLK_ID_"+ str(int(index) + 1) +"_FREQ"))

        else:
            return

        ldr = int(Database.getSymbolValue(
            "core", "CONFIG_CLOCK_DPLL" + index + "_LDR_INTEGER"))
        ldrFrac = int(Database.getSymbolValue(
            "core", "CONFIG_CLOCK_DPLL" + index + "_LDRFRAC_FRACTION"))

        dpllFreq = int(srcFreq * (ldr + 1.0 + (ldrFrac / 16.0)))

        prevFreq = symbol.getValue()
        if prevFreq != dpllFreq:
            symbol.setValue(dpllFreq, 1)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)


def calcDpllMultiplier(symbol, event):
    index = symbol.getID().split("CONFIG_CLOCK_DPLL")[1][0]
    ldr = int(Database.getSymbolValue(
        "core", "CONFIG_CLOCK_DPLL" + index + "_LDR_INTEGER"))
    ldrFrac = int(Database.getSymbolValue(
        "core", "CONFIG_CLOCK_DPLL" + index + "_LDRFRAC_FRACTION"))
    multiplier = (ldr + 1.0 + (ldrFrac / 16.0))
    symbol.setValue(multiplier, 2)


def calcDpllXoscDivider(symbol, event):
    index = symbol.getID().split("CONFIG_CLOCK_DPLL")[1][0]
    divisor = int(Database.getSymbolValue(
        "core", "CONFIG_CLOCK_DPLL" + index + "_DIVIDER"))
    div_value = (2 * (divisor + 1))
    symbol.setValue(div_value, 2)


def setDfllFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")
    freq = 0
    if enable:
        mode = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE")
        if mode == 0:
            freq = 48000000
        else:
            mul = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_MUL"))
            refFreq = int(Database.getSymbolValue("core", "GCLK_ID_0_FREQ"))
            freq = mul * refFreq

    prevFreq = symbol.getValue()

    if prevFreq != freq:
        symbol.setValue(freq, 2)


def setImult(symbol, event):
    if event["value"] < 8000000:
        symbol.setValue(3, 2)
    elif event["value"] > 8000000 and event["value"] < 16000000:
        symbol.setValue(4, 2)
    elif event["value"] > 16000000 and event["value"] < 24000000:
        symbol.setValue(5, 2)
    else:
        symbol.setValue(6, 2)


def setIptat(symbol, event):
    if event["value"] < 8000000:
        symbol.setValue(2, 2)
    else:
        symbol.setValue(3, 2)


################################################################################
#######          OSCCTRL Database Components      ##############################
################################################################################

############################   XOSC Components    ##############################
for i in range(0, 2):
    # XOSC Oscillator Enable
    oscctrlSym_XOSC_CONFIG_ENABLE = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_ENABLE", oscctrlXosc_Menu[i])
    oscctrlSym_XOSC_CONFIG_ENABLE.setLabel(
        "External Multipurpose Crystal Oscillator(XOSC) Enable")
    oscctrlSym_XOSC_CONFIG_ENABLE.setDescription(
        "External Crystal Oscillator Enable Feature")
    oscctrlSym_XOSC_CONFIG_ENABLE.setDefaultValue(False)

    # XOSC Automatic Loop Control Mode
    oscctrlSym_XOSC_ENALC = coreComponent.createBooleanSymbol(
        "XOSC" + str(i) + "_ENALC", oscctrlXosc_Menu[i])
    oscctrlSym_XOSC_ENALC.setLabel("Automatic Loop Control ")
    oscctrlSym_XOSC_ENALC.setDefaultValue(False)

    # Low Buffer Gain Enable
    oscctrlSym_XOSC_ENALC = coreComponent.createBooleanSymbol(
        "XOSC" + str(i) + "_LOWBUFGAIN", oscctrlXosc_Menu[i])
    oscctrlSym_XOSC_ENALC.setLabel("Low Buffer Gain Enable ")
    oscctrlSym_XOSC_ENALC.setDefaultValue(False)

    # Xosc Clock Switch Enable
    oscctrlSym_XOSC_SWBEN = coreComponent.createBooleanSymbol(
        "XOSC" + str(i) + "_SWBEN", oscctrlXosc_Menu[i])
    oscctrlSym_XOSC_SWBEN.setLabel("Xosc Clock Switch Enable")
    oscctrlSym_XOSC_SWBEN.setDefaultValue(False)

    # XOSC Oscillator Mode
    oscctrlSym_XOSC_OSCILLATORMODE = coreComponent.createKeyValueSetSymbol(
        "XOSC" + str(i) + "_OSCILLATOR_MODE", oscctrlXosc_Menu[i])
    oscctrlSym_XOSC_OSCILLATORMODE.setLabel("External Oscillator Mode ")
    oscctrlSym_XOSC_OSCILLATORMODE.addKey(
        "EXTERNAL_CLOCK", "0", "xosc external clock enable")
    oscctrlSym_XOSC_OSCILLATORMODE.addKey(
        "CRYSTAL", "1", "crystal oscillator enable")
    oscctrlSym_XOSC_OSCILLATORMODE.setOutputMode("Value")
    oscctrlSym_XOSC_OSCILLATORMODE.setDefaultValue(1)

    # XOSC Oscillator Frequency
    oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_FREQUENCY", oscctrlXosc_Menu[i])
    oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setLabel("Frequency")
    oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDescription(
        "Setting the XOSC Frequency")
    oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDefaultValue(8000000)
    oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setMax(32000000)

    # Oscillator Current Multiplier
    xoscImult = coreComponent.createIntegerSymbol(
        "XOSC" + str(i) + "_IMULT", oscctrlXosc_Menu[i])
    xoscImult.setLabel("Oscillator Current Multiplier")
    xoscImult.setDefaultValue(3)
    xoscImult.setVisible(False)
    xoscImult.setDependencies(
        setImult, ["CONFIG_CLOCK_XOSC" + str(i) + "_FREQUENCY"])
    # Oscillator Current Reference
    xoscIptat = coreComponent.createIntegerSymbol(
        "XOSC" + str(i) + "_IPTAT", oscctrlXosc_Menu[i])
    xoscIptat.setLabel("Oscillator Current Reference")
    xoscIptat.setDefaultValue(2)
    xoscIptat.setVisible(False)
    xoscIptat.setDependencies(
        setIptat, ["CONFIG_CLOCK_XOSC" + str(i) + "_FREQUENCY"])

    # XOSC Oscillator ONDEMAND Mode
    oscctrlSym_XOSCCTRL_ONDEMAND = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_ONDEMAND", oscctrlXosc_Menu[i])
    oscctrlSym_XOSCCTRL_ONDEMAND.setLabel("Oscillator On-Demand Control")
    oscctrlSym_XOSCCTRL_ONDEMAND.setDescription(
        "Configures the XOSC on Demand Behavior")
    oscctrlSym_XOSCCTRL_ONDEMAND.setOutputMode("Key")
    oscctrlSym_XOSCCTRL_ONDEMAND.setDisplayMode("Description")
    oscctrlSym_XOSCCTRL_ONDEMAND.addKey("DISABLE", str(0), "Always Enable")
    oscctrlSym_XOSCCTRL_ONDEMAND.addKey(
        "ENABLE", str(1), "Only on Peripheral Request")
    oscctrlSym_XOSCCTRL_ONDEMAND.setDefaultValue(0)

    # XOSC Oscillator Startup Time
    oscctrlSym_XOSCCTRL_STARTUP = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_STARTUP", oscctrlXosc_Menu[i])
    oscctrlSym_XOSCCTRL_STARTUP.setLabel("Oscillator Startup Time")
    oscctrlSym_XOSCCTRL_STARTUP.setDescription("Startup time for the XOSC ")
    oscctrlSymXOSCStartupNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_XOSCCTRL__STARTUP\"]")
    oscctrlSymXOSCStartupValues = []
    oscctrlSymXOSCStartupValues = oscctrlSymXOSCStartupNode.getChildren()
    xoscstartupDefaultValue = 6
    for index in range(0, len(oscctrlSymXOSCStartupValues)):
        xoscstartupKeyName = oscctrlSymXOSCStartupValues[index].getAttribute(
            "name")

        if (xoscstartupKeyName == "CYCLE1"):
            xoscstartupDefaultValue = index

        xoscstartupKeyDescription = oscctrlSymXOSCStartupValues[index].getAttribute(
            "caption")
        xoscstartupKeyValue = oscctrlSymXOSCStartupValues[index].getAttribute(
            "value")
        oscctrlSym_XOSCCTRL_STARTUP.addKey(
            xoscstartupKeyName, xoscstartupKeyValue, xoscstartupKeyDescription)

    oscctrlSym_XOSCCTRL_STARTUP.setDefaultValue(xoscstartupDefaultValue)
    oscctrlSym_XOSCCTRL_STARTUP.setOutputMode("Value")
    oscctrlSym_XOSCCTRL_STARTUP.setDisplayMode("Description")

    # XOSC Oscillator Run StandBy Control
    oscctrlSym_XOSCCTRL_RUNSTDBY = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_RUNSTDBY", oscctrlXosc_Menu[i])
    oscctrlSym_XOSCCTRL_RUNSTDBY.setLabel(
        "Run Oscillator in Standby Sleep Mode")
    oscctrlSym_XOSCCTRL_RUNSTDBY.setDescription(
        "External oscillator RunIn StandBy mode or not")
    oscctrlSym_XOSCCTRL_RUNSTDBY.setDefaultValue(False)

    # XOSC Oscillator Clock Failure Detector(CFD) Enable
    oscctrlSym_XOSCCTRL_CFDEN = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_CFDEN", oscctrlXosc_Menu[i])
    oscctrlSym_XOSCCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
    oscctrlSym_XOSCCTRL_CFDEN.setDescription(
        "Clock Failure Detection enable or not")
    oscctrlSym_XOSCCTRL_CFDEN.setDefaultValue(False)

    # XOSC Oscillator Clock Failure Detector(CFD) Pre-Scalar
    oscctrlSym_CFDPRESC_CFDPRESC = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_XOSC" + str(i) + "_CFDPRESC", oscctrlSym_XOSCCTRL_CFDEN)
    oscctrlSym_CFDPRESC_CFDPRESC.setLabel("Safe Clock Frequency ")
    oscctrlSym_CFDPRESC_CFDPRESC.setDescription(
        "Startup time for the XOSC " + str(i))
    oscctrlSym_CFDPRESC_CFDPRESC.setVisible(True)
    oscctrlSymCFDPrescNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_XOSCCTRL__CFDPRESC\"]")
    oscctrlSymCFDPrescNodeValues = []
    oscctrlSymCFDPrescNodeValues = oscctrlSymCFDPrescNode.getChildren()
    xosccfdprescalarDefaultValue = 0
    for index in range(0, len(oscctrlSymCFDPrescNodeValues)):
        xosccfdprescalarKeyName = oscctrlSymCFDPrescNodeValues[index].getAttribute(
            "name")

        if (xosccfdprescalarKeyName == "DIV1"):
            xosccfdprescalarDefaultValue = index

        xosccfdprescalarKeyDescription = oscctrlSymCFDPrescNodeValues[index].getAttribute(
            "caption")
        xosccfdprescalarKeyValue = oscctrlSymCFDPrescNodeValues[index].getAttribute(
            "value")
        oscctrlSym_CFDPRESC_CFDPRESC.addKey(
            xosccfdprescalarKeyName, xosccfdprescalarKeyValue, xosccfdprescalarKeyDescription)

    oscctrlSym_CFDPRESC_CFDPRESC.setDefaultValue(xosccfdprescalarDefaultValue)
    oscctrlSym_CFDPRESC_CFDPRESC.setOutputMode("Value")
    oscctrlSym_CFDPRESC_CFDPRESC.setDisplayMode("Description")

    clkSym_XOSC_Freq = coreComponent.createIntegerSymbol(
        "XOSC" + str(i) + "_FREQ", calculatedFreq_Menu)
    clkSym_XOSC_Freq.setLabel("XOSC" + str(i) + " Clock Frequency")
    clkSym_XOSC_Freq.setReadOnly(True)
    clkSym_XOSC_Freq.setDependencies(setXOSCFreq, [
                                     "CONFIG_CLOCK_XOSC" + str(i) + "_ENABLE", "CONFIG_CLOCK_XOSC" + str(i) + "_FREQUENCY"])


############################   DPLL Components    ############################
for i in range(0, 2):
    # Digital Phase Locked Loop(DPLL) Enable
    oscctrlSym_DPLL_CONFIG_ENABLE = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_ENABLE", dpll_Menu[i])
    oscctrlSym_DPLL_CONFIG_ENABLE.setLabel(
        "Digital Phase Locked Loop(DPLL) Enable ")
    oscctrlSym_DPLL_CONFIG_ENABLE.setDescription(
        "DPLL Configuration enabling feature")
    oscctrlSym_DPLL_CONFIG_ENABLE.setDefaultValue(False)

    # Digital Phase Locked Loop(DPLL) ONDEMAND Mode
    oscctrlSym_DPLLCTRLA_ONDEMAND = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_ONDEMAND", dpll_Menu[i])
    oscctrlSym_DPLLCTRLA_ONDEMAND.setLabel("DPLL On-Demand Control")
    oscctrlSym_DPLLCTRLA_ONDEMAND.setDescription(
        "Configures the DPLL on Demand Behavior")
    oscctrlSym_DPLLCTRLA_ONDEMAND.setOutputMode("Value")
    oscctrlSym_DPLLCTRLA_ONDEMAND.setDisplayMode("Description")
    oscctrlSym_DPLLCTRLA_ONDEMAND.addKey("Disable", str(0), "Always Enable")
    oscctrlSym_DPLLCTRLA_ONDEMAND.addKey(
        "Enable", str(1), "Only on Peripheral Request")
    oscctrlSym_DPLLCTRLA_ONDEMAND.setDefaultValue(0)

    # Digital Phase Locked Loop(DPLL) Run StandBy Control
    oscctrlSym_DPLLCTRLA_RUNSTDBY = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_RUNSTDY", dpll_Menu[i])
    oscctrlSym_DPLLCTRLA_RUNSTDBY.setLabel("Run DPLL in Standby Sleep Mode")
    oscctrlSym_DPLLCTRLA_RUNSTDBY.setDescription(
        "DPLL to run in standby mode or not")
    oscctrlSym_DPLLCTRLA_RUNSTDBY.setDefaultValue(False)

    # Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Integer part
    oscctrlSym_DPLLRATIO_LDR = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_LDR_INTEGER", dpll_Menu[i])
    oscctrlSym_DPLLRATIO_LDR.setLabel("DPLL Loop Divider Ratio Integer Part")
    oscctrlSym_DPLLRATIO_LDR.setDescription("Loop divider ratio integer value")
    oscctrlSym_DPLLRATIO_LDR.setDefaultValue(0)
    oscctrlSym_DPLLRATIO_LDR.setMin(0)
    oscctrlSym_DPLLRATIO_LDR.setMax(4095)

    # Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Fraction part
    oscctrlSym_DPLLRATIO_LDRFRAC = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_LDRFRAC_FRACTION", dpll_Menu[i])
    oscctrlSym_DPLLRATIO_LDRFRAC.setLabel(
        "DPLL Loop Divider Ratio Fractional Part")
    oscctrlSym_DPLLRATIO_LDRFRAC.setDescription(
        "loop divider ratio fraction value")
    oscctrlSym_DPLLRATIO_LDRFRAC.setDefaultValue(0)
    oscctrlSym_DPLLRATIO_LDRFRAC.setMin(0)
    oscctrlSym_DPLLRATIO_LDRFRAC.setMax(15)

    # DPLL Multiplier value to show in the UI
    oscctrlSym_DPLL_MULTIPLIER_VALUE = coreComponent.createFloatSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_MULTIPLIER_VALUE", dpll_Menu[i])
    oscctrlSym_DPLL_MULTIPLIER_VALUE.setVisible(False)
    oscctrlSym_DPLL_MULTIPLIER_VALUE.setDefaultValue(1)
    oscctrlSym_DPLL_MULTIPLIER_VALUE.setDependencies(calcDpllMultiplier, [
                                                     "CONFIG_CLOCK_DPLL" + str(i) + "_LDRFRAC_FRACTION", "CONFIG_CLOCK_DPLL" + str(i) + "_LDR_INTEGER"])

    # Digital Phase Locked Loop(DPLL) Lock Bypass
    oscctrlSym_DPLLCTRLB_LBYPASS = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_LOCK_BYPASS", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_LBYPASS.setLabel("Bypass DPLL Lock?")
    oscctrlSym_DPLLCTRLB_LBYPASS.setDescription(
        "DPLL Lock signal is always asserted or DPLL Lock signal drives the DPLL controller internal logic.")
    oscctrlSym_DPLLCTRLB_LBYPASS.setDefaultValue(False)

    # DCO Filter Enable
    oscctrlSym_DPLLCTRLB_DCOEN = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_DCOEN", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_DCOEN.setLabel("DCO Filter Enable")
    oscctrlSym_DPLLCTRLB_DCOEN.setDescription("DCO Filter Enable")
    oscctrlSym_DPLLCTRLB_DCOEN.setDefaultValue(False)

    # Digital Phase Locked Loop(DPLL) Filter
    oscctrlSym_DPLLCTRLB_DCOFILTER = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_DCOFILTER", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_DCOFILTER.setLabel("Sigma-Delta DCO Filter Selection")
    oscctrlSym_DPLLCTRLB_DCOFILTER.setDescription("Sigma-Delta DCO Filter Selection")
    oscctrlSymDPLLFilterNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__DCOFILTER\"]")
    oscctrlSymDPLLFilterNodeValues = []
    oscctrlSymDPLLFilterNodeValues = oscctrlSymDPLLFilterNode.getChildren()
    dpllfilterDefaultValue = 0
    for index in range(0, len(oscctrlSymDPLLFilterNodeValues)):
        dpllfilterKeyName = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "name")

        if (dpllfilterKeyName == "DEFAULT"):
            dpllfilterDefaultValue = index

        dpllfilterKeyDescription = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "caption")
        dpllfilterKeyValue = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "value")
        oscctrlSym_DPLLCTRLB_DCOFILTER.addKey(
            dpllfilterKeyName, dpllfilterKeyValue, dpllfilterKeyDescription)

    oscctrlSym_DPLLCTRLB_DCOFILTER.setDefaultValue(dpllfilterDefaultValue)
    oscctrlSym_DPLLCTRLB_DCOFILTER.setOutputMode("Value")
    oscctrlSym_DPLLCTRLB_DCOFILTER.setDisplayMode("Description")


    # Digital Phase Locked Loop(DPLL) wakeUp Fast
    oscctrlSym_DPLLCTRLB_WUF = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_WAKEUP_FAST", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_WUF.setLabel("DPLL Fast Output Enable")
    oscctrlSym_DPLLCTRLB_WUF.setDescription(
        "DPLL clock is Output after startup and lock time or only after the startup")
    oscctrlSym_DPLLCTRLB_WUF.setDefaultValue(False)

    # Digital Phase Locked Loop(DPLL) Lock Time
    oscctrlSym_DPLLCTRLB_LTIME = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_LOCK_TIME", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_LTIME.setLabel("DPLL Lock Time-out")
    oscctrlSym_DPLLCTRLB_LTIME.setDescription(
        "select the lock time-out value:")
    oscctrlSym_DPLLCTRLB_LTIME.setVisible(False)
    oscctrlSymDPLLLockTimeNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__LTIME\"]")
    oscctrlSymDPLLLockTimeNodeValues = []
    oscctrlSymDPLLLockTimeNodeValues = oscctrlSymDPLLLockTimeNode.getChildren()
    dpllLockTimeDefaultValue = 0
    for index in range(0, len(oscctrlSymDPLLLockTimeNodeValues)):
        dpllLockTimeKeyName = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute(
            "name")

        if (dpllLockTimeKeyName == "DEFAULT"):
            dpllLockTimeDefaultValue = index

        dpllLockTimeKeyDescription = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute(
            "caption")
        dpllLockTimeKeyValue = oscctrlSymDPLLLockTimeNodeValues[index].getAttribute(
            "value")
        oscctrlSym_DPLLCTRLB_LTIME.addKey(
            dpllLockTimeKeyName, dpllLockTimeKeyValue, dpllLockTimeKeyDescription)

    oscctrlSym_DPLLCTRLB_LTIME.setDefaultValue(dpllLockTimeDefaultValue)
    oscctrlSym_DPLLCTRLB_LTIME.setOutputMode("Value")
    oscctrlSym_DPLLCTRLB_LTIME.setDisplayMode("Description")

    # Digital Phase Locked Loop(DPLL) Filter
    oscctrlSym_DPLLCTRLB_FILTER = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_FILTER", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_FILTER.setLabel("Proportional Integral Filter selection")
    oscctrlSym_DPLLCTRLB_FILTER.setDescription("Proportional Integral Filter selection")
    oscctrlSymDPLLFilterNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DPLLCTRLB__FILTER\"]")
    oscctrlSymDPLLFilterNodeValues = []
    oscctrlSymDPLLFilterNodeValues = oscctrlSymDPLLFilterNode.getChildren()
    dpllfilterDefaultValue = 0
    for index in range(0, len(oscctrlSymDPLLFilterNodeValues)):
        dpllfilterKeyName = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "name")

        if (dpllfilterKeyName == "DEFAULT"):
            dpllfilterDefaultValue = index

        dpllfilterKeyDescription = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "caption")
        dpllfilterKeyValue = oscctrlSymDPLLFilterNodeValues[index].getAttribute(
            "value")
        oscctrlSym_DPLLCTRLB_FILTER.addKey(
            dpllfilterKeyName, dpllfilterKeyValue, dpllfilterKeyDescription)

    oscctrlSym_DPLLCTRLB_FILTER.setDefaultValue(dpllfilterDefaultValue)
    oscctrlSym_DPLLCTRLB_FILTER.setOutputMode("Value")
    oscctrlSym_DPLLCTRLB_FILTER.setDisplayMode("Description")

    # Digital Phase Locked Loop(DPLL) Reference Clock
    oscctrlSym_DPLLCTRLB_REFCLK = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_REF_CLOCK", dpll_Menu[i])
    oscctrlSym_DPLLCTRLB_REFCLK.setLabel("DPLL Reference Clock Source")
    oscctrlSym_DPLLCTRLB_REFCLK.setDescription(
        "DPLL reference clock selection")

    oscctrlSym_DPLLCTRLB_REFCLK.addKey(
        "XOSC32K", "1", "32 KHz External Crystal Oscillator")
    oscctrlSym_DPLLCTRLB_REFCLK.addKey(
        "XOSC0", "2", "External Crystal 0 Oscillator ")
    oscctrlSym_DPLLCTRLB_REFCLK.addKey(
        "XOSC1", "3", "External Crystal 1 Oscillator 1")
    oscctrlSym_DPLLCTRLB_REFCLK.addKey(
        "GCLK_DPLL", "0", "Generic Clock for FDPLL")

    oscctrlSym_DPLLCTRLB_REFCLK.setDefaultValue(0)
    oscctrlSym_DPLLCTRLB_REFCLK.setOutputMode("Value")
    oscctrlSym_DPLLCTRLB_REFCLK.setDisplayMode("Key")

    # Digital Phase Locked Loop(DPLL) Clock Divider
    oscctrlSym_DPLLCTRLB_DIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_DIVIDER", oscctrlSym_DPLLCTRLB_REFCLK)
    oscctrlSym_DPLLCTRLB_DIV.setLabel("DPLL Divider")
    oscctrlSym_DPLLCTRLB_DIV.setDescription(
        "XOSC clock division factor fdiv = (fxosc/((2*DIV)+1))")
    oscctrlSym_DPLLCTRLB_DIV.setDefaultValue(0)
    oscctrlSym_DPLLCTRLB_DIV.setMin(0)
    oscctrlSym_DPLLCTRLB_DIV.setMax(2047)

    # DPLL divider value to show in UI
    oscctrlSym_DPLLCTRLB_DIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_DPLL" + str(i) + "_DIVIDER_VALUE", oscctrlSym_DPLLCTRLB_REFCLK)
    oscctrlSym_DPLLCTRLB_DIV.setDefaultValue(2)
    oscctrlSym_DPLLCTRLB_DIV.setDependencies(
        calcDpllXoscDivider, ["CONFIG_CLOCK_DPLL" + str(i) + "_DIVIDER"])

    clkSym_DPLL_Freq = coreComponent.createIntegerSymbol(
        "DPLL" + str(i) + "_CLOCK_FREQ", calculatedFreq_Menu)
    clkSym_DPLL_Freq.setReadOnly(True)
    clkSym_DPLL_Freq.setDefaultValue(0)
    clkSym_DPLL_Freq.setLabel("FDPLL" + str(i) + " Clock Frequency")

    clkSym_DPLL_Freq.setDependencies(setDPLLClockFreq, ["CONFIG_CLOCK_DPLL_ENABLE",
                                                        "XOSC32K_FREQ",
                                                        "XOSC0_FREQ",
                                                        "XOSC1_FREQ",
                                                        "CONFIG_CLOCK_DPLL" +
                                                        str(i) + "_DIVIDER",
                                                        "CONFIG_CLOCK_DPLL"
                                                        + str(i) + "_REF_CLOCK",
                                                        "CONFIG_CLOCK_DPLL" +
                                                        str(i) +
                                                        "_LDR_INTEGER",
                                                        "CONFIG_CLOCK_DPLL" +
                                                        str(i) +
                                                        "_LDRFRAC_FRACTION",
                                                        "GCLK_ID_"
                                                        + str(i + 1) + "_FREQ"
                                                        ])


##############################################DFLL####################################################

dfllEnable = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_ENABLE", dfll_Menu)
dfllEnable.setLabel("Enable DFLL")
dfllEnable.setDescription("Enable DFLL")
dfllEnable.setDefaultValue(True)

dfllOpmode = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_DFLL_OPMODE", dfll_Menu)
dfllOpmode.setLabel("DFLL operation mode")
dfllOpmode.setDescription("Selects DFLL operating mode")
dfllOpmode.setOutputMode("Value")
dfllOpmode.setDisplayMode("Description")
dfllOpmode.addKey("Open", str(0), "The DFLL operates in open-loop operation.")
dfllOpmode.addKey("Closed", str(
    1), "The DFLL operates in closed-loop operation.")
dfllOpmode.setDefaultValue(0)

dfllOndemand = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_DFLL_ONDEMAND", dfll_Menu)
dfllOndemand.setLabel("DFLL On-Demand Control")
dfllOndemand.setDescription("Configures the DFLL on Demand Behavior")
dfllOndemand.setOutputMode("Value")
dfllOndemand.setDisplayMode("Description")
dfllOndemand.addKey("Disable", str(0), "Always Enable")
dfllOndemand.addKey("Enable", str(1), "Only on Peripheral Request")
dfllOndemand.setDefaultValue(1)

dfllRunstdy = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_RUNSTDY", dfll_Menu)
dfllRunstdy.setLabel("Run DFLL in Standby Sleep Mode")
dfllRunstdy.setDescription("DFLL to run in standby mode or not")
dfllRunstdy.setDefaultValue(False)

dfllUsb = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_USB", dfll_Menu)
dfllUsb.setLabel("USB Clock Recovery Mode")
dfllUsb.setDescription("Enable or Disable USB Clock Recovery Mode")
dfllUsb.setDefaultValue(False)

dfllWaitLock = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_WAIT_LOCK", dfll_Menu)
dfllWaitLock.setLabel("Wait for DFLL lock")
dfllWaitLock.setDescription(
    "Controls the DFLL output clock, depending on lock status")
dfllWaitLock.setDefaultValue(False)

dfllBypassCoarse = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_BYPASS_COARSE", dfll_Menu)
dfllBypassCoarse.setLabel("Bypass Coarse Lock")
dfllBypassCoarse.setDescription("Controls the coarse lock procedure")
dfllBypassCoarse.setDefaultValue(False)

dfllQuickLock = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_QUICK_LOCK", dfll_Menu)
dfllQuickLock.setLabel("Quick lock disable")
dfllQuickLock.setDescription("Diable quick lock")
dfllQuickLock.setDefaultValue(False)

dfllChillCycle = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_CHILL_CYCLE", dfll_Menu)
dfllChillCycle.setLabel("Chill Cycle Disable")
dfllChillCycle.setDescription("Disable Chill Cycle")
dfllChillCycle.setDefaultValue(False)

dfllLLAW = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_LLAW", dfll_Menu)
dfllLLAW.setLabel("Lose Lock After Wake")
dfllLLAW.setDescription("Lose Lock After Wake")
dfllLLAW.setDefaultValue(False)

dfllStable = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_DFLL_STABLE", dfll_Menu)
dfllStable.setLabel("Stable DFLL Frequency")
dfllStable.setDescription(
    "FINE calibration tracks changes in output frequency")
dfllStable.setDefaultValue(False)

dfllCoarse = coreComponent.createIntegerSymbol(
    "CONFIG_CLOCK_DFLL_COARSE", dfll_Menu)
dfllCoarse.setDefaultValue(1)
dfllCoarse.setMin(0)
dfllCoarse.setMax(31)
dfllCoarse.setLabel("Coarse Maximum Step")

dfllFine = coreComponent.createIntegerSymbol(
    "CONFIG_CLOCK_DFLL_FINE", dfll_Menu)
dfllFine.setDefaultValue(1)
dfllFine.setMin(0)
dfllFine.setMax(255)
dfllFine.setLabel("Fine Maximum Step")

dfllMul = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DFLL_MUL", dfll_Menu)
dfllMul.setDefaultValue(1)
dfllMul.setMin(0)
dfllMul.setMax(65535)
dfllMul.setLabel("DFLL Multiply Factor")

dfllFreq = coreComponent.createIntegerSymbol(
    "DFLL_CLOCK_FREQ", calculatedFreq_Menu)
dfllFreq.setReadOnly(True)
dfllFreq.setDefaultValue(48000000)
dfllFreq.setLabel("DFLL Clock Frequency")
dfllFreq.setDependencies(setDfllFreq, ["CONFIG_CLOCK_DFLL_ENABLE",
                                       "CONFIG_CLOCK_DFLL_OPMODE",
                                       "CONFIG_CLOCK_DFLL_MUL",
                                       "GCLK_ID_0_FREQ"])


################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC32K Configuration Callback Functions    ############################

def setXOSC32KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xosc32k = Database.getSymbolValue("core", "XOSC32K_EN32K")
    xoscmode = Database.getSymbolValue("core", "XOSC32K_OSCILLATOR_MODE")
    xosc_in_freq = Database.getSymbolValue("core", "XOSC32K_FREQ_IN")

    if (xosc == True) and (xoscmode == 1) and (xosc32k == True):
        symbol.setValue(32768, 1)
    elif (xosc == True) and (xoscmode == 1) and (xosc32k == False):
        symbol.setValue(0, 1)
    elif (xosc == True) and (xoscmode == 0):
        symbol.setValue(xosc_in_freq, 1)
    elif (xosc == False):
        symbol.setValue(0, 1)


def setXOSC1KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xosc1k = Database.getSymbolValue("core", "XOSC32K_EN1K")
    xoscmode = Database.getSymbolValue("core", "XOSC32K_OSCILLATOR_MODE")

    if xosc and xosc1k and (xoscmode == 1):
        symbol.setValue(1024, 1)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)


################################################################################
#######          OSC32KCTRL Database Components      ###########################
################################################################################
global rtcClockSourceSelection

#####################    OSCULP32K Components    ###############################
clkSym_OSCULP32K_Freq = coreComponent.createIntegerSymbol(
    "OSCULP32K_FREQ", calculatedFreq_Menu)
clkSym_OSCULP32K_Freq.setLabel("OSCULP32K Clock Frequency")
clkSym_OSCULP32K_Freq.setDefaultValue(32768)
clkSym_OSCULP32K_Freq.setReadOnly(True)

clkSym_OSCULP1K_Freq = coreComponent.createIntegerSymbol(
    "OSCULP1K_FREQ", calculatedFreq_Menu)
clkSym_OSCULP1K_Freq.setLabel("OSCULP1K Clock Frequency")
clkSym_OSCULP1K_Freq.setDefaultValue(1024)
clkSym_OSCULP1K_Freq.setReadOnly(True)


####################    XOSC32K Components    ##################################
# XOSC32K External Oscillator Enable
osc32kctrlSym_XOSC32K_CONFIG_ENABLE = coreComponent.createBooleanSymbol(
    "CONF_CLOCK_XOSC32K_ENABLE", xosc32k_Menu)
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setLabel(
    "32KHz External Crystal Oscillator(XOSC32K) Enable")
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setDefaultValue(False)

# XOSC32K External Oscillator Mode
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_OSCILLATOR_MODE", xosc32k_Menu)
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setLabel(
    "32KHz External Oscillator Mode ")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey(
    "EXTERNAL_CLOCK", "0", "xosc32K external clock enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey(
    "CRYSTAL", "1", "crystal oscillator enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setOutputMode("Value")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setDefaultValue(1)

clkSym_XOSC32K_Input_Freq = coreComponent.createIntegerSymbol(
    "XOSC32K_FREQ_IN", xosc32k_Menu)
clkSym_XOSC32K_Input_Freq.setLabel("Frequency")
clkSym_XOSC32K_Input_Freq.setDefaultValue(32768)

# XOSC32K External Oscillator Run StandBy Mode
osc32kctrlSym_XOSC32K_RUNSTDBY = coreComponent.createBooleanSymbol(
    "XOSC32K_RUNSTDBY", xosc32k_Menu)
osc32kctrlSym_XOSC32K_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")

# XOSC32K External Oscillator ONDEMAND Mode
osc32kctrlSym_XOSC32K_ONDEMAND = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_ONDEMAND", xosc32k_Menu)
osc32kctrlSym_XOSC32K_ONDEMAND.setLabel("Oscillator On-Demand Control")
osc32kctrlSym_XOSC32K_ONDEMAND.setDescription(
    "Configures the DPLL on Demand Behavior")
osc32kctrlSym_XOSC32K_ONDEMAND.setOutputMode("Key")
osc32kctrlSym_XOSC32K_ONDEMAND.setDisplayMode("Description")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey("DISABLE", str(0), "Always Enable")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey(
    "ENABLE", str(1), "Only on Peripheral Request")
osc32kctrlSym_XOSC32K_ONDEMAND.setDefaultValue(0)

# XOSC32K External Oscillator 1KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN1K = coreComponent.createBooleanSymbol(
    "XOSC32K_EN1K", xosc32k_Menu)
osc32kctrlSym_XOSC32K_EN1K.setLabel("Enable 1KHz Output")

xosc32KGain = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_CGM", xosc32k_Menu)
xosc32KGain.setLabel("Control Gain Mode")
xosc32KGainNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"OSC32KCTRL_XOSC32K__CGM\"]")
xosc32KGainNodeValues = xosc32KGainNode.getChildren()
for index in range(0, len(xosc32KGainNodeValues)):
    xosc32KGainKeyName = xosc32KGainNodeValues[index].getAttribute("name")
    xosc32KGainKeyDescription = xosc32KGainNodeValues[index].getAttribute(
        "caption")
    xosc32KGainKeyValue = xosc32KGainNodeValues[index].getAttribute("value")
    xosc32KGain.addKey(xosc32KGainKeyName, xosc32KGainKeyValue,
                       xosc32KGainKeyDescription)

xosc32KGain.setDefaultValue(0)
xosc32KGain.setOutputMode("Value")
xosc32KGain.setDisplayMode("Description")

# XOSC32K External Oscillator 1KHz Output Frequency Mode
clkSym_XOSC1K_Freq = coreComponent.createIntegerSymbol(
    "XOSC1K_FREQ", calculatedFreq_Menu)
clkSym_XOSC1K_Freq.setLabel("XOSC1K Clock Frequency")
clkSym_XOSC1K_Freq.setDefaultValue(0)
clkSym_XOSC1K_Freq.setReadOnly(True)
clkSym_XOSC1K_Freq.setDependencies(setXOSC1KFreq, [
                                   "CONF_CLOCK_XOSC32K_ENABLE", "XOSC32K_EN1K", "XOSC32K_OSCILLATOR_MODE"])

# XOSC32K External Oscillator 32KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN32K = coreComponent.createBooleanSymbol(
    "XOSC32K_EN32K", xosc32k_Menu)
osc32kctrlSym_XOSC32K_EN32K.setLabel("Enable 32KHz Output")

# XOSC32K External Oscillator StartUp Time
osc32kctrlSym_XOSC32K_STARTUP = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_STARTUP", xosc32k_Menu)
osc32kctrlSym_XOSC32K_STARTUP.setLabel("Oscillator Startup Time ")
osc32kctrlSym_XOSC32K_STARTUP.setDescription("XOSC start up time ")
osc32kctrlXOSC32KStarupNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"OSC32KCTRL_XOSC32K__STARTUP\"]")
osc32kctrlXOSC32KStarupNodeValues = []
osc32kctrlXOSC32KStarupNodeValues = osc32kctrlXOSC32KStarupNode.getChildren()
xosc32kstartupDefaultValue = 2
for index in range(0, len(osc32kctrlXOSC32KStarupNodeValues)):
    xosc32kstartupKeyName = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute(
        "name")

    if (xosc32kstartupKeyName == "CYCLE1"):
        xosc32kstartupDefaultValue = index

    xosc32kstartupKeyDescription = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute(
        "caption")
    xosc32kstartupKeyValue = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute(
        "value")
    osc32kctrlSym_XOSC32K_STARTUP.addKey(
        xosc32kstartupKeyName, xosc32kstartupKeyValue, xosc32kstartupKeyDescription)

osc32kctrlSym_XOSC32K_STARTUP.setDefaultValue(xosc32kstartupDefaultValue)
osc32kctrlSym_XOSC32K_STARTUP.setOutputMode("Value")
osc32kctrlSym_XOSC32K_STARTUP.setDisplayMode("Description")

# RTC Clock Selection
rtcClockSourceSelection = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_RTC_SRC", xosc32k_Menu)  
rtcClockSourceSelection.setLabel("RTC Clock Selection")
rtcClockSourceSelection.setDescription("Clock Source selection for RTC")

rtcClockSourceSelection.addKey(
    "OSCULP1K", "0", "32 KHz Ultra Low-Power Internal Oscillator (1 KHz Output)")
rtcClockSourceSelection.addKey(
    "OSCULP32K", "1", "32 KHz Ultra Low-Power Internal Oscillator (32 KHz Output)")
rtcClockSourceSelection.addKey(
    "XOSC1K", "4", "32.768 KHz External Crystal Oscillator (1.024 KHz Output)")
rtcClockSourceSelection.addKey(
    "XOSC32K", "5", "32.768 KHz External Crystal Oscillator (32.768 KHz Output)")

rtcClockSourceSelection.setDefaultValue(0)
rtcClockSourceSelection.setOutputMode("Value")
rtcClockSourceSelection.setDisplayMode("Key")

# XOSC32K External Oscillator Clock Failure Detection(CFD) Enable
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN = coreComponent.createBooleanSymbol(
    "XOSC32K_CFDEN", xosc32k_Menu)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setLabel("Enable Clock Failure Detection")

# Clock Switch Back
osc32kctrlSym_XOSC32K_CFDCTRL_SWBACK = coreComponent.createBooleanSymbol(
    "XOSC32K_SWBACK", xosc32k_Menu)
osc32kctrlSym_XOSC32K_CFDCTRL_SWBACK.setLabel("Clock Switch Back")

# XOSC32K External Oscillator Clock Failure Detection(CFD) Pre-Scalar
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC = coreComponent.createBooleanSymbol(
    "XOSC32K_CFDPRESC", osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setLabel(
    "Clock Failure Backup Clock Frequency Divide-by-2")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setDefaultValue(False)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setVisible(True)

clkSym_XOSC32K_Freq = coreComponent.createIntegerSymbol(
    "XOSC32K_FREQ", calculatedFreq_Menu)
clkSym_XOSC32K_Freq.setLabel("XOSC32K Clock Frequency")
clkSym_XOSC32K_Freq.setDefaultValue(0)
clkSym_XOSC32K_Freq.setReadOnly(True)
clkSym_XOSC32K_Freq.setDependencies(setXOSC32KFreq, [
                                    "CONF_CLOCK_XOSC32K_ENABLE",
                                    "XOSC32K_EN32K",
                                    "XOSC32K_OSCILLATOR_MODE",
                                    "XOSC32K_FREQ_IN"])

################################################################################
##########             GCLK Callback Functions            ######################
################################################################################
# GCLK Peripheral Channel Write Lock visible Property


def setPCHCTRLFREQVisibleProperty(symbol, event):
    index = symbol.getID().split("_FREQ")[0]
    if "_FREQ" not in event["id"]:
        perifreq = Database.getSymbolValue("core", index + "_GENSEL")
        channel = Database.getSymbolValue("core", index + "_CHEN")
        if channel:
            srcFreq = Database.getSymbolValue("core", "GCLK_"+str(perifreq)+"_FREQ")

            prevFreq = symbol.getValue()
            if prevFreq != srcFreq:
                symbol.setValue(srcFreq, 1)
        else:
            if symbol.getValue() > 0:
                symbol.setValue(0, 1)

    else:
        if Database.getSymbolValue("core", index + "_CHEN"):
            perifreq = Database.getSymbolValue("core", index + "_GENSEL")
            generator = event["id"].split("_")[1]
            if int(perifreq) == int(generator):
                prevFreq = symbol.getValue()
                if prevFreq != event["value"]:
                    symbol.setValue(event["value"], 1)


def setGClockFreq(symbol, event):
    global gclkSym_GENCTRL_SRC
    index = symbol.getID().split("_")[1]

    enable = Database.getSymbolValue("core", "GCLK_INST_NUM" + index)

    if enable:
        src = gclkSym_GENCTRL_SRC[int(index)].getSelectedKey()

        # XOSC0
        if src == "XOSC0":
            srcFreq = int(Database.getSymbolValue("core", "XOSC0_FREQ"))

        # XOSC1
        if src == "XOSC1":
            srcFreq = int(Database.getSymbolValue("core", "XOSC1_FREQ"))

        # GCLKIN
        elif 'GCLK_IN' in str(src):
            gclk_in_symbol = "GCLK_IO_" + str(index) + "_FREQ"
            srcFreq = int(Database.getSymbolValue("core", gclk_in_symbol))

        # GCLKGEN1
        elif src == "GCLK1":
            if index != 1:
                srcFreq = int(Database.getSymbolValue("core", "GCLK_1_FREQ"))

        # OSCULP32K
        elif src == "OSCULP32K":
            srcFreq = 32768

        # XOSC32K
        elif src == "XOSC32K":
            srcFreq = int(Database.getSymbolValue("core", "XOSC32K_FREQ"))

        # DFLL
        elif src == "DFLL":
            srcFreq = int(Database.getSymbolValue("core", "DFLL_CLOCK_FREQ"))

        # FDPLL0
        elif src == "FDPLL0":
            srcFreq = int(Database.getSymbolValue("core", "DPLL0_CLOCK_FREQ"))

        # FDPLL1
        elif src == "FDPLL1":
            srcFreq = int(Database.getSymbolValue("core", "DPLL1_CLOCK_FREQ"))

        divSel = int(Database.getSymbolValue(
            "core", "GCLK_" + index + "_DIVSEL"))
        div = int(Database.getSymbolValue("core", "GCLK_" + index + "_DIV"))

        if divSel == 0:

            if div != 0:
                gclk_freq = int(srcFreq / float(div))
            else:
                gclk_freq = srcFreq

        elif divSel == 1:
            gclk_freq = int(srcFreq / float(2**(div + 1)))

        prevFreq = symbol.getValue()

        if prevFreq != gclk_freq:
            if gclk_freq < 4294967295:
                symbol.setValue(gclk_freq, 1)

    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)


def topsort(graph):
    from collections import deque

    # Initialize the degree of vetexes to zero and increment dependents by 1
    degreeList = {}
    for vertex in graph:
        degreeList[vertex] = 0

    for vertex in graph:
        for dependent in graph[vertex]:
            degreeList[dependent] = degreeList[dependent] + 1

    # initialize a dequeue pipe
    pipe = deque()

    # move vertexes with zero degree to the starting of pipe
    for vertex in degreeList:
        if degreeList[vertex] == 0:
            pipe.appendleft(vertex)

    outputList = []

    # move vertexes with degree 0 to output list
    # visit the dependent and reduce the degree by one for every visited dependent
    while pipe:
        vertex = pipe.pop()
        outputList.append(vertex)
        for dependent in graph[vertex]:
            degreeList[dependent] -= 1
            if degreeList[dependent] == 0:
                pipe.appendleft(dependent)

    # If there are no cycles that is the max degree of all vertices is 1
    # then the length of list should be equal to total number of vertices in graph else a cycle has been formed
    if len(outputList) == len(graph):
        return outputList
    else:
        return []


def codeGen(symbol, event):
    global codeGenerationDep
    global topsort
    global gclkSym_GENCTRL_SRC
    global cycleFormed
    from collections import defaultdict
    sourceDestmap = defaultdict(list)
    sourceDestmap = {
        "DFLL": [],
        "FDPLL0": [],
        "FDPLL1": [],
        "GCLK0": [],
        "GCLK1": [],
        "GCLK2": [],
        "GCLK3": [],
        "GCLK4": [],
        "GCLK5": [],
        "GCLK6": [],
        "GCLK7": [],
        "GCLK8": [],
        "GCLK9": [],
        "GCLK10": [],
        "GCLK11": []
    }
    symbol.clearValues()
    codeList = []

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE"))) == 1):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_0_GENSEL"))].append("DFLL")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL0_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL0_REF_CLOCK"))) == 3):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_1_GENSEL"))].append("FDPLL0")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL1_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL1_REF_CLOCK"))) == 3):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_2_GENSEL"))].append("FDPLL1")

    for i in range(0, 12):
        if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)):
            if gclkSym_GENCTRL_SRC[i].getSelectedKey() in ["DFLL", "FDPLL0", "FDPLL1", "GCLK1"]:
                sourceDestmap[gclkSym_GENCTRL_SRC[i].getSelectedKey()].append(
                    "GCLK" + str(i))

    codeList = topsort(sourceDestmap)
    if len(codeList) != 0:
        cycleFormed.setValue(False, 2)
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL0_ENABLE")) == False:
            codeList.remove("FDPLL0")
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL1_ENABLE")) == False:
            codeList.remove("FDPLL1")
        for i in range(0, 12):
            if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)) == False:
                codeList.remove("GCLK" + str(i))
        for i in range(0, len(codeList)):
            symbol.addValue("    " + codeList[i] + "_Initialize();")

    else:
        cycleFormed.setValue(True, 2)


def clkSetup(symbol, event):
    global indexSymbolMap
    symbolKey = ""
    status = False
    if "_CLOCK_ENABLE" in event["id"]:
        for key, value in indexSymbolMap.iteritems():
            for i in range(0, len(value)):
                if value[i] == event["id"].split("_CLOCK_ENABLE")[0]:
                    symbolKey = key
                    break
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            status = status | Database.getSymbolValue(
                "core", i + "_CLOCK_ENABLE")
        Database.setSymbolValue("core", symbolKey + "_CHEN", status, 2)
        if event["value"]:
            freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
            Database.setSymbolValue("core", event["id"].split(
                "_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", freq, 2)
        else:
            Database.setSymbolValue("core", event["id"].split(
                "_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", 0, 2)

    if "_FREQ" in event["id"]:
        symbolKey = event["id"].split("_FREQ")[0]
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            if Database.getSymbolValue("core", i + "_CLOCK_ENABLE"):
                freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
                Database.setSymbolValue(
                    "core", i + "_CLOCK_FREQUENCY", freq, 2)


def calcGclkDivider(symbol, event):
    index = symbol.getID().split("_")[1]
    divSel = int(Database.getSymbolValue("core", "GCLK_" + index + "_DIVSEL"))
    div = int(Database.getSymbolValue("core", "GCLK_" + index + "_DIV"))

    if divSel == 0:
        if div != 0:
            divider = div
        else:
            divider = 1

    elif divSel == 1:
        divider = 2**(div + 1)

    symbol.setValue(divider, 2)


def setGCLKIOFreq(symbol, event):
    index = int(symbol.getID().split("GCLK_IO_")[1].split("_FREQ")[0])
    enable = Database.getSymbolValue(
        "core", "GCLK_" + str(index) + "_OUTPUTENABLE")
    if enable:
        symbol.setValue(int(Database.getSymbolValue(
            "core", "GCLK_" + str(index) + "_FREQ")), 2)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)

################################################################################
#######          GCLK Database Components            ###########################
################################################################################


gclkDependencyList = []

global gclkSym_num, gclkSym_GENCTRL_DIVSEL, gclkSym_GENCTRL_DIV
gclkSym_num = []
gclkSym_GENCTRL_RUNSTDBY = []
gclkSym_GENCTRL_OE = []
gclkSym_GENCTRL_OOV = []
global gclkSym_GENCTRL_IDC
gclkSym_GENCTRL_IDC = []
gclkSym_GCLK_IO_FREQ = []
gclkSym_GENCTRL_GENEN = []
gclkSym_GENCTRL_DIVSEL = []
gclkSym_GENCTRL_DIV = []
gclkSym_GENCTRL_DIVIDER_VALUE = []
global gclkSym_GENCTRL_SRC
gclkSym_GENCTRL_SRC = []
gclkSym_index = []
gclkSym_Freq = []
global codeGenerationDep
codeGenerationDep = []
triggerdepList = []
global indexSymbolMap
indexSymbolMap = defaultdict(list)
global cycleFormed

# ------------------------- ATDF Read -------------------------------------
packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
channel = []
availablePins = []        # array to save available pins
gclk_io_signals = [False, False, False, False, False, False, False,
                   False, False, False, False, False]  # array to save available signals
pinout = ""
numPads = 0
val = ATDF.getNode("/avr-tools-device-file/variants")
children = val.getChildren()
for index in range(0, len(children)):
    if packageName in children[index].getAttribute("package"):
        pinout = children[index].getAttribute("pinout")

children = []
val = ATDF.getNode(
    "/avr-tools-device-file/pinouts/pinout@[name=\"" + str(pinout) + "\"]")
children = val.getChildren()
for pad in range(0, len(children)):
    availablePins.append(children[pad].getAttribute("pad"))


gclk = ATDF.getNode(
    "/avr-tools-device-file/devices/device/peripherals/module@[name=\"GCLK\"]/instance@[name=\"GCLK\"]/signals")
wakeup_signals = gclk.getChildren()
for pad in range(0, len(wakeup_signals)):
    if "index" in wakeup_signals[pad].getAttributeList():
        padSignal = wakeup_signals[pad].getAttribute("pad")
        if padSignal in availablePins:
            gclk_io_signals[int(
                wakeup_signals[pad].getAttribute("index"))] = True

for gclknumber in range(0, 12):
    gclkSym_num.append(gclknumber)
    gclkSym_num[gclknumber] = coreComponent.createBooleanSymbol(
        "GCLK_INST_NUM" + str(gclknumber), gclkGen_Menu)
    gclkSym_num[gclknumber].setLabel(
        "Enable Generic Clock Generator " + str(gclknumber))
    if(gclknumber == 0):
        gclkSym_num[gclknumber].setDefaultValue(True)
        gclkSym_num[gclknumber].setReadOnly(True)

    # GCLK Generator Run StandBy
    gclkSym_GENCTRL_RUNSTDBY.append(gclknumber)
    gclkSym_GENCTRL_RUNSTDBY[gclknumber] = coreComponent.createBooleanSymbol(
        "GCLK_" + str(gclknumber) + "_RUNSTDBY", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setLabel(
        "GCLK should keep running in Standby mode")

    # GCLK External Clock input frequency

    if(gclk_io_signals[gclknumber] == True):
        numPads = numPads + 1
        gclkSym_GCLK_IO_FREQ.append(gclknumber)
        gclkSym_GCLK_IO_FREQ[gclknumber] = coreComponent.createIntegerSymbol(
            "GCLK_IO_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
        gclkSym_GCLK_IO_FREQ[gclknumber].setLabel(
            "External Input (GCLK_IO[" + str(gclknumber) + "]) Frequency")
        gclkSym_GCLK_IO_FREQ[gclknumber].setDefaultValue(0)
        gclkSym_GCLK_IO_FREQ[gclknumber].setDependencies(setGCLKIOFreq, [
                                                         "GCLK_" + str(gclknumber) + "_FREQ", "GCLK_" + str(gclknumber) + "_OUTPUTENABLE"])

    # GCLK Generator Source Selection
    gclkSym_GENCTRL_SRC.append(gclknumber)
    gclkSym_GENCTRL_SRC[gclknumber] = coreComponent.createKeyValueSetSymbol(
        "GCLK_" + str(gclknumber) + "_SRC", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_SRC[gclknumber].setLabel("Source Selection")

    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "XOSC0", "0", "External Crystal 0 Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "XOSC1", "1", "External Crystal 1 Oscillator")

    gclk_in = "GCLK_IN[" + str(gclknumber) + "]"
    gclk_in_desc = "Generator Input Pad (" + \
        "GCLK_IN[" + str(gclknumber) + "])"

    if(gclk_io_signals[gclknumber] == True):
        gclkSym_GENCTRL_SRC[gclknumber].addKey(gclk_in, "2", gclk_in_desc)

    if gclknumber != 1:
        gclkSym_GENCTRL_SRC[gclknumber].addKey(
            "GCLK1", "3", "GCLK Generator 1")

    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "OSCULP32K", "4", "32 KHz Ultra Low-Power Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "XOSC32K", "5", "32.768 KHz External Crystal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "DFLL", "6", "DFLL Oscillator Output")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "FDPLL0", "7", "Franctional DPLL0 Output")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "FDPLL1", "8", "Franctional DPLL1 Output")
    gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(6)
    gclkSym_GENCTRL_SRC[gclknumber].setOutputMode("Value")
    gclkSym_GENCTRL_SRC[gclknumber].setDisplayMode("Key")

    # GCLK Generator Output Enable
    if(gclk_io_signals[gclknumber] == True):
        gclkSym_GENCTRL_OE.append(gclknumber)
        gclkSym_GENCTRL_OE[gclknumber] = coreComponent.createBooleanSymbol(
            "GCLK_" + str(gclknumber) + "_OUTPUTENABLE", gclkSym_num[gclknumber])
        gclkSym_GENCTRL_OE[gclknumber].setLabel(
            "Output GCLK clock signal on IO pin?")

    # GCLK Generator Output Off Value
    if(gclk_io_signals[gclknumber] == True):
        gclkSym_GENCTRL_OOV.append(gclknumber)
        gclkSym_GENCTRL_OOV[gclknumber] = coreComponent.createKeyValueSetSymbol(
            "GCLK_" + str(gclknumber) + "_OUTPUTOFFVALUE", gclkSym_GENCTRL_OE[gclknumber])
        gclkSym_GENCTRL_OOV[gclknumber].setLabel("Output Off Value")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("LOW", "0", "Logic Level 0")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("HIGH", "1", "Logic Level 1")
        gclkSym_GENCTRL_OOV[gclknumber].setDefaultValue(0)
        gclkSym_GENCTRL_OOV[gclknumber].setOutputMode("Key")
        gclkSym_GENCTRL_OOV[gclknumber].setDisplayMode("Description")

        gclkInFreq = coreComponent.createBooleanSymbol(
            "GCLK_IN_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
        gclkInFreq.setLabel("Gclk Input Frequency")
        gclkInFreq.setDefaultValue(0)

    # GCLK Generator Division Selection
    gclkSym_GENCTRL_DIVSEL.append(gclknumber)
    gclkSym_GENCTRL_DIVSEL[gclknumber] = coreComponent.createKeyValueSetSymbol(
        "GCLK_" + str(gclknumber) + "_DIVSEL", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVSEL[gclknumber].setLabel("Divide Selection")
    gclkSymGenDivSelNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_GENCTRL__DIVSEL\"]")
    gclkSymGenDivSelNodeValues = []
    gclkSymGenDivSelNodeValues = gclkSymGenDivSelNode.getChildren()
    gclkSymGenDivSelDefaultValue = 0
    for index in range(0, len(gclkSymGenDivSelNodeValues)):
        gclkSymGenDivSelKeyName = gclkSymGenDivSelNodeValues[index].getAttribute(
            "name")

        if (gclkSymGenDivSelKeyName == "DIV1"):
            gclkSymGenDivSelDefaultValue = index

        gclkSymGenDivSelKeyDescription = gclkSymGenDivSelNodeValues[index].getAttribute(
            "caption")
        gclkSymGenDivSelKeyValue = gclkSymGenDivSelNodeValues[index].getAttribute(
            "value")
        gclkSym_GENCTRL_DIVSEL[gclknumber].addKey(
            gclkSymGenDivSelKeyName, gclkSymGenDivSelKeyValue, gclkSymGenDivSelKeyDescription)

    gclkSym_GENCTRL_DIVSEL[gclknumber].setDefaultValue(
        gclkSymGenDivSelDefaultValue)
    gclkSym_GENCTRL_DIVSEL[gclknumber].setOutputMode("Key")
    gclkSym_GENCTRL_DIVSEL[gclknumber].setDisplayMode("Description")

    # GCLK Generator Division Factor
    gclkSym_GENCTRL_DIV.append(gclknumber)
    gclkSym_GENCTRL_DIV[gclknumber] = coreComponent.createIntegerSymbol(
        "GCLK_" + str(gclknumber) + "_DIV", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIV[gclknumber].setLabel("Division Factor")
    if (gclknumber == 1):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFFFF)
    else:
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFF)

    gclkSym_GENCTRL_DIV[gclknumber].setMin(0)
    gclkSym_GENCTRL_DIV[gclknumber].setDefaultValue(1)

    # GCLK Generator Division Factor to show in the UI
    gclkSym_GENCTRL_DIVIDER_VALUE.append(gclknumber)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber] = coreComponent.createIntegerSymbol(
        "GCLK_" + str(gclknumber) + "_DIVIDER_VALUE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setVisible(False)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDefaultValue(1)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDependencies(calcGclkDivider, [
                                                              "GCLK_" + str(gclknumber) + "_DIV", "GCLK_" + str(gclknumber) + "_DIVSEL"])

    # GCLK Generator Improve Duty Cycle
    gclkSym_GENCTRL_IDC.append(gclknumber)
    gclkSym_GENCTRL_IDC[gclknumber] = coreComponent.createBooleanSymbol(
        "GCLK_" + str(gclknumber) + "_IMPROVE_DUTYCYCLE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_IDC[gclknumber].setLabel("Enable 50/50 Duty Cycle")

    gclkSym_Freq.append(gclknumber)
    gclkSym_Freq[gclknumber] = coreComponent.createIntegerSymbol(
        "GCLK_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
    gclkSym_Freq[gclknumber].setLabel(
        "GCLK" + str(gclknumber) + " Clock Frequency")
    gclkSym_Freq[gclknumber].setReadOnly(True)
    if(gclknumber == 0):
        gclkSym_Freq[gclknumber].setDefaultValue(0)
    else:
        gclkSym_Freq[gclknumber].setDefaultValue(0)

    depList = ["GCLK_" + str(gclknumber) + "_DIVSEL",
               "GCLK_" + str(gclknumber) + "_DIV",
               "GCLK_" + str(gclknumber) + "_SRC",
               "GCLK_INST_NUM" + str(gclknumber),
               "XOSC0_FREQ",
               "XOSC1_FREQ",
               "OSC48M_CLOCK_FREQ",
               "DPLL0_CLOCK_FREQ",
               "DPLL1_CLOCK_FREQ",
               "DFLL_CLOCK_FREQ",
               "XOSC32K_FREQ",
               "GCLK_IN_0_FREQ",
               "GCLK_IN_1_FREQ",
               "GCLK_IN_2_FREQ",
               "GCLK_IN_3_FREQ",
               "GCLK_IN_4_FREQ",
               "GCLK_IN_5_FREQ",
               "GCLK_IN_6_FREQ",
               "GCLK_IN_7_FREQ",
               "GCLK_IN_8_FREQ",
               "GCLK_IN_9_FREQ",
               "GCLK_IN_10_FREQ",
               "GCLK_IN_11_FREQ"
               ]
    if gclknumber != 1:
        depList.append("GCLK_1_FREQ")
    gclkSym_Freq[gclknumber].setDependencies(setGClockFreq, depList)

    codeGenerationDep.append("GCLK_" + str(gclknumber) + "_SRC")
    codeGenerationDep.append("GCLK_INST_NUM" + str(gclknumber))

maxGCLKId = 0

gclkIOpads = coreComponent.createIntegerSymbol("GCLK_NUM_PADS", None)
gclkIOpads.setVisible(False)
gclkIOpads.setDefaultValue(numPads)

cycleFormed = coreComponent.createBooleanSymbol("GCLK_CYCLE_FORMED", clkMenu)
cycleFormed.setDefaultValue(False)
cycleFormed.setVisible(False)

atdfFilePath = join(Variables.get("__DFP_PACK_DIR"), "atdf",
                    Variables.get("__PROCESSOR") + ".atdf")

try:
    atdfFile = open(atdfFilePath, "r")
except:
    Log.writeInfoMessage(
        "clk.py peripheral clock: Error!!! while opening atdf file")

atdfContent = ElementTree.fromstring(atdfFile.read())

# parse atdf xml file to get instance name
# for the peripheral which has gclk id
for peripheral in atdfContent.iter("module"):
    for instance in peripheral.iter("instance"):
        for param in instance.iter("param"):
            if "GCLK_ID" in param.attrib["name"]:

                indexID = param.attrib["value"]
                symbolValue = instance.attrib["name"] + \
                    param.attrib["name"].split("GCLK_ID")[1]
                symbolId = "GCLK_ID_" + str(indexID)
                indexSymbolMap[symbolId].append(symbolValue)

                if maxGCLKId < int(indexID):
                    maxGCLKId = int(indexID)


channelMap = {}
for key in indexSymbolMap.keys():
    index = key.split("GCLK_ID_")[1]
    channelMap[int(index)] = key

for index in sorted(channelMap.iterkeys()):
    key = channelMap[index]
    name = indexSymbolMap.get(key)
    name = " ".join(name)

    # GCLK Peripheral Channel Enable
    clkSymPeripheral = coreComponent.createBooleanSymbol(
        key + "_CHEN", gclkPeriChannel_menu)
    clkSymPeripheral.setLabel(
        "Peripheral Channel " + str(index) + " Clock Enable")
    clkSymPeripheral.setDefaultValue(False)

    # GCLK Peripheral Channel Name
    gclkSym_PERCHANNEL_NAME = coreComponent.createStringSymbol(
        key + "_NAME", clkSymPeripheral)
    gclkSym_PERCHANNEL_NAME.setLabel("Peripheral")
    gclkSym_PERCHANNEL_NAME.setReadOnly(True)
    gclkSym_PERCHANNEL_NAME.setDefaultValue(name)

    # GCLK Peripheral Channel Index
    gclkSym_PERCHANNEL_INDEX = coreComponent.createIntegerSymbol(
        key + "_INDEX", clkSymPeripheral)
    gclkSym_PERCHANNEL_INDEX.setVisible(False)
    gclkSym_PERCHANNEL_INDEX.setDefaultValue(int(index))

    # Peripheral Channel Generator Selection
    gclkSym_PCHCTRL_GEN = coreComponent.createKeyValueSetSymbol(
        key + "_GENSEL", clkSymPeripheral)
    gclkSym_PCHCTRL_GEN.setLabel("Generator Selection")

    gclkSymPCHCTRLGenNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_PCHCTRL__GEN\"]")
    gclkSymPCHCTRLGenNodeValues = []
    gclkSymPCHCTRLGenNodeValues = gclkSymPCHCTRLGenNode.getChildren()

    gclkSymPCHCTRLGenDefaultValue = 0

    for i in range(0, len(gclkSymPCHCTRLGenNodeValues)):
        gclkSymPCHCTRLGenKeyName = gclkSymPCHCTRLGenNodeValues[i].getAttribute(
            "name")

        if (gclkSymPCHCTRLGenKeyName == "GCLK0"):
            gclkSymPCHCTRLGenDefaultValue = i

        gclkSymPCHCTRLGenKeyDescription = gclkSymPCHCTRLGenNodeValues[i].getAttribute(
            "caption")
        ggclkSymPCHCTRLGenKeyValue = gclkSymPCHCTRLGenNodeValues[i].getAttribute(
            "value")
        gclkSym_PCHCTRL_GEN.addKey(
            gclkSymPCHCTRLGenKeyName, ggclkSymPCHCTRLGenKeyValue, gclkSymPCHCTRLGenKeyDescription)

    gclkSym_PCHCTRL_GEN.setDefaultValue(gclkSymPCHCTRLGenDefaultValue)
    gclkSym_PCHCTRL_GEN.setOutputMode("Value")
    gclkSym_PCHCTRL_GEN.setDisplayMode("Key")

    gclkSym_PCHCTRL_FREQ = coreComponent.createIntegerSymbol(
        key + "_FREQ", clkSymPeripheral)
    gclkSym_PCHCTRL_FREQ.setLabel(
        "Peripheral Channel " + str(index) + " Frequency ")
    gclkSym_PCHCTRL_FREQ.setReadOnly(True)
    gclkSym_PCHCTRL_FREQ.setDependencies(setPCHCTRLFREQVisibleProperty, [
        key + "_CHEN", key + "_GENSEL",
        "GCLK_0_FREQ",
        "GCLK_1_FREQ",
        "GCLK_2_FREQ",
        "GCLK_3_FREQ",
        "GCLK_4_FREQ",
        "GCLK_5_FREQ",
        "GCLK_6_FREQ",
        "GCLK_7_FREQ",
        "GCLK_8_FREQ",
        "GCLK_9_FREQ",
        "GCLK_10_FREQ",
        "GCLK_11_FREQ", ])
    triggerdepList.append(key + "_FREQ")
    # GCLK Peripheral Channel Lock
    gclkSym_PCHCTRL_WRTLOCK = coreComponent.createBooleanSymbol(
        key + "_WRITELOCK", clkSymPeripheral)
    gclkSym_PCHCTRL_WRTLOCK.setLabel("Write Lock")

peripheralList = []
for value in indexSymbolMap.values():
    for i in range(0, len(value)):
        peripheralList.append(value[i])

peripheralList.sort()

for name in peripheralList:
    # GCLK Peripheral Channel Enable
    clkSymExtPeripheral = coreComponent.createBooleanSymbol(
        name + "_CLOCK_ENABLE", peripheralClockMenu)
    clkSymExtPeripheral.setLabel(name + " Clock Enable")
    clkSymExtPeripheral.setDefaultValue(False)
    triggerdepList.append(name + "_CLOCK_ENABLE")

    clkSymExtPeripheral = coreComponent.createIntegerSymbol(
        name + "_CLOCK_FREQUENCY", clkSymExtPeripheral)
    clkSymExtPeripheral.setLabel(name + " Clock Frequency")
    clkSymExtPeripheral.setReadOnly(True)
    gclkDependencyList.append(name + "_CLOCK_ENABLE")

clockTrigger = coreComponent.createBooleanSymbol("TRIGGER_LOGIC", None)
clockTrigger.setVisible(False)
clockTrigger.setDependencies(clkSetup, triggerdepList)

gclkSym_PeriIdMax = coreComponent.createIntegerSymbol(
    "GCLK_MAX_ID", clkSymPeripheral)
gclkSym_PeriIdMax.setVisible(False)
gclkSym_PeriIdMax.setDefaultValue(int(maxGCLKId))

clkInitList = coreComponent.createListSymbol("CLK_INIT_LIST", None)

codeGenerationList = coreComponent.createListEntrySymbol("GCLK_CODE", None)
codeGenerationList.setVisible(False)
codeGenerationDep.append("GCLK_ID_0_GENSEL")
codeGenerationDep.append("GCLK_ID_1_GENSEL")
codeGenerationDep.append("GCLK_ID_2_GENSEL")
codeGenerationDep.append("CONFIG_CLOCK_DPLL0_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_DPLL1_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_DPLL0_ENABLE")
codeGenerationDep.append("CONFIG_CLOCK_DPLL1_ENABLE")
codeGenerationList.setDependencies(codeGen, codeGenerationDep)
codeGenerationList.addValue("   GCLK0_Initialize();")
codeGenerationList.addValue("   DFLL_Initialize();")
codeGenerationList.setTarget("core.CLK_INIT_LIST")


################################################################################
##########              MCLK Callback Functions            #####################
################################################################################
def ahbValue(symbol, event):
    global ahbInit
    global mclkDic

    perInstance = event["id"].split("_CLOCK_ENABLE")[0]
    if perInstance == "CAN0" or perInstance == "CAN1":
        for key in mclkDic.keys():
            if mclkDic.get(key) == perInstance:
                if key.startswith("AHB_"):
                    bitmask = int(key.split("AHB_")[1])
                    ahbVal = int(symbol.getValue(), 16)
                    if event["value"] == True:
                        ahbVal = ahbVal | bitmask
                        symbol.setValue(hex(ahbVal), 2)
                        break
                    else:
                        ahbVal = ahbVal & ~(bitmask)
                        symbol.setValue(hex(ahbVal), 2)
                        break


def apbValue(symbol, event):
    global apbInit
    global mclkDic
    enable = event["value"]
    perInstance = event["id"].split("_CLOCK_ENABLE")[0]
    if "_CORE" in perInstance:
        perInstance = perInstance.split("_CORE")[0]

    if "_ANA" in perInstance:
        perInstance = perInstance.split("_ANA")[0]

    if "_MSR" in perInstance:
        perInstance = perInstance.split("_MSR")[0]

    if "_SLOW" in perInstance:
        return

    if "_DIG" in perInstance:
        return

    if "_REF" in perInstance:
        return

    if "EVSYS" in perInstance:
        perInstance = perInstance.split("_")[0]
        for i in range (0,12):
            if Database.getSymbolValue("core", "EVSYS_" + str(i) + "_CLOCK_ENABLE") == True:
                enable = enable | True
                break



    for key in mclkDic.keys():
        if mclkDic.get(key) == perInstance:
            if key.startswith("APB"):
                bridge = key.split("_")[0]

                bitmask = int(key.split("_")[1])
                apbVal = int(Database.getSymbolValue("core", "MCLK_" + bridge + "_INITIAL_VALUE"),16)
                if enable == True:
                    apbVal =  apbVal | bitmask
                    Database.setSymbolValue("core", "MCLK_" + bridge + "_INITIAL_VALUE", hex(apbVal),2)
                    break
                else:
                    apbVal =  apbVal & ~(bitmask)
                    Database.setSymbolValue("core", "MCLK_" + bridge + "_INITIAL_VALUE", hex(apbVal),2)
                    break


################################################################################
#######          MCLK Database Components            ###########################
################################################################################
global ahbInit
numAPB = 0
ahbInit = 0x0
global mclkDic
mclkDic = {}
global apbInit

ahbNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group")
for index in range(0, len(ahbNode.getChildren())):
    if ahbNode.getChildren()[index].getAttribute("name") == "AHBMASK":
        ahbInit = hex(int(ahbNode.getChildren()[
                      index].getAttribute("initval"), 16))

# AHB Bridge Clock Initial Settings
mclk_AHB_Clock_Value = coreComponent.createStringSymbol(
    "MCLK_AHB_INITIAL_VALUE", mclkSym_Menu)
mclk_AHB_Clock_Value.setDefaultValue(str(ahbInit))
mclk_AHB_Clock_Value.setDependencies(ahbValue, gclkDependencyList)
mclk_AHB_Clock_Value.setReadOnly(True)

ahbMaskNode = ATDF.getNode(
    '/avr-tools-device-file/modules/module@[name="MCLK"]/register-group@[name="MCLK"]/register@[name="AHBMASK"]')
ahbMaskValues = ahbMaskNode.getChildren()
for index in range(0, len(ahbMaskValues)):
    mclkDic["AHB_" + str(int(ahbMaskValues[index].getAttribute("mask"), 16))
            ] = ahbMaskValues[index].getAttribute("name").split("_")[0]
    if ahbMaskValues[index].getAttribute("name").startswith("HPB"):
        numAPB = numAPB + 1

bridges = ["APBA", "APBB", "APBC", "APBD"]
apbInit = {"APBA": "",
           "APBB": "",
           "APBC": "",
           "APBD": ""
           }
for index in range(0, numAPB):
    bridgeName = bridges[index]
    path = "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group@[name=\"MCLK\"]/register@[name=\"" + bridgeName + "MASK\"]"
    apbNode = ATDF.getNode(path)
    apbValues = apbNode.getChildren()
    for bitpos in range(0, len(apbValues)):
        mclkDic[bridgeName + "_" + str(int(apbValues[bitpos].getAttribute(
            "mask"), 16))] = apbValues[bitpos].getAttribute("name").split("_")[0]

    apbInitNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group")
    for index in range(0, len(apbInitNode.getChildren())):
        if apbInitNode.getChildren()[index].getAttribute("name") == (bridgeName + "MASK"):
            apbInit[bridgeName] = hex(
                int(apbInitNode.getChildren()[index].getAttribute("initval"), 16))

    # APB Bridge Clock Initial Settings
    mclk_Clock_Value = coreComponent.createStringSymbol(
        "MCLK_" + bridgeName + "_INITIAL_VALUE", mclkSym_Menu)
    mclk_Clock_Value.setDefaultValue(str(apbInit[bridgeName]))
    mclk_Clock_Value.setReadOnly(True)
# /////////////////////////Callback///////////////////////////////////////////#
def setQspiFreq(symbol, event):
    clockEnable = Database.getSymbolValue(event["namespace"], "QSPI_CLOCK_ENABLE")
    if clockEnable:
        freq = Database.getSymbolValue(event["namespace"], "MAIN_CLOCK_FREQUENCY")
        symbol.setValue(int(freq), 2)
    else:
        symbol.setValue(0, 2)

################Peripheral which donot have a GCLKID but have MCLKID######################
peripheralsWithoutGclk = ["TRNG", "AES", "ICM", "PUKCC"]
for i in range(0,len(peripheralsWithoutGclk)):
    peripheralClock = coreComponent.createBooleanSymbol(
        peripheralsWithoutGclk[i] + "_CLOCK_ENABLE", peripheralClockMenu)
    peripheralClock.setLabel(peripheralsWithoutGclk[i] + " Clock Enable")
    peripheralClock.setDefaultValue(False)
    gclkDependencyList.append( peripheralsWithoutGclk[i] + "_CLOCK_ENABLE")

qspiClock = coreComponent.createBooleanSymbol(
    "QSPI_CLOCK_ENABLE", peripheralClockMenu)
qspiClock.setLabel("QSPI Clock Enable")
qspiClock.setDefaultValue(False)

qspiClockFrequency= coreComponent.createIntegerSymbol(
    "QSPI_CLOCK_FREQUENCY", qspiClock)
qspiClockFrequency.setDefaultValue(0)
qspiClockFrequency.setReadOnly(True)
qspiClockFrequency.setDependencies(setQspiFreq, ["QSPI_CLOCK_ENABLE", "MAIN_CLOCK_FREQUENCY"])

#########################################################################################
gclkDependencyList.append("QSPI_CLOCK_ENABLE")
mclk_Clock_Value.setDependencies(apbValue, gclkDependencyList)

# MCLK CPU Division
mclkSym_CPUDIV_CPUDIV = coreComponent.createKeyValueSetSymbol(
    "CONF_CPU_CLOCK_DIVIDER", mclkSym_Menu)
mclkSym_CPUDIV_CPUDIV.setLabel("CPU Clock Division Factor")
mclkcpudivNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/value-group@[name=\"MCLK_CPUDIV__DIV\"]")
mclkcpudivNodeValues = []
mclkcpudivNodeValues = mclkcpudivNode.getChildren()
mclkcpudivDefaultValue = 0

for index in range(0, len(mclkcpudivNodeValues)):
    mclkcpudivKeyName = mclkcpudivNodeValues[index].getAttribute("name")

    if (mclkcpudivKeyName == "DIV1"):
        mclkcpudivDefaultValue = index

    mclkcpudivKeyDescription = mclkcpudivNodeValues[index].getAttribute(
        "caption")
    mclkcpudivKeyValue = mclkcpudivNodeValues[index].getAttribute("value")
    mclkSym_CPUDIV_CPUDIV.addKey(
        mclkcpudivKeyName, mclkcpudivKeyValue, mclkcpudivKeyDescription)

mclkSym_CPUDIV_CPUDIV.setDefaultValue(mclkcpudivDefaultValue)
mclkSym_CPUDIV_CPUDIV.setOutputMode("Value")
mclkSym_CPUDIV_CPUDIV.setDisplayMode("Key")

################################################################################
#######          Calculated Clock Frequencies        ###########################
################################################################################


def setMainClockFreq(symbol, event):
    divider = int(Database.getSymbolValue("core", "CONF_CPU_CLOCK_DIVIDER"))
    gclk0_freq = int(Database.getSymbolValue("core", "GCLK_0_FREQ"))

    symbol.setValue(gclk0_freq / (1 << divider), 1)
    Database.setSymbolValue(event["namespace"], "MAIN_CLOCK_FREQUENCY", gclk0_freq, 2)


def setFreq(symbol, event):
    global rtcClockSourceSelection
    src = rtcClockSourceSelection.getSelectedKey()

    freq = 0
    if src == "OSCULP1K":
        freq = int(Database.getSymbolValue("core", "OSCULP1K_FREQ"))
    elif src == "OSCULP32K":
        freq = int(Database.getSymbolValue("core", "OSCULP32K_FREQ"))
    elif src == "XOSC1K":
        freq = int(Database.getSymbolValue("core", "XOSC1K_FREQ"))
    else:
        freq = int(Database.getSymbolValue("core", "XOSC32K_FREQ"))

    symbol.setValue(freq, 2)


clkSym_MAIN_CLK_FREQ = coreComponent.createIntegerSymbol(
    "CPU_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_MAIN_CLK_FREQ.setLabel("CPU Clock Frequency")
clkSym_MAIN_CLK_FREQ.setReadOnly(True)
clkSym_MAIN_CLK_FREQ.setDependencies(
    setMainClockFreq, ["GCLK_0_FREQ", "CONF_CPU_CLOCK_DIVIDER"])

divider = mclkSym_CPUDIV_CPUDIV.getValue()
gclk0_freq = int(gclkSym_Freq[0].getValue())
clkSym_MAIN_CLK_FREQ.setValue(gclk0_freq / (divider + 1), 1)

clkMclkFreq = coreComponent.createIntegerSymbol(
    "MAIN_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkMclkFreq.setLabel("Main Clock Frequency")
clkMclkFreq.setReadOnly(True)
clkMclkFreq.setDefaultValue(int(gclkSym_Freq[0].getValue()))

peripherals = ATDF.getNode(
    "/avr-tools-device-file/devices/device@[name=\"" + Variables.get("__PROCESSOR") + "\"]/peripherals")
module_list = peripherals.getChildren()

clkSym_WDT_CLK_FREQ = coreComponent.createIntegerSymbol(
    "WDT_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_WDT_CLK_FREQ.setLabel("WDT Clock Frequency")
clkSym_WDT_CLK_FREQ.setReadOnly(True)
clkSym_WDT_CLK_FREQ.setDefaultValue(32768)

clkSym_RTC_CLK_FREQ = coreComponent.createIntegerSymbol(
    "RTC_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_RTC_CLK_FREQ.setLabel("RTC Clock Frequency")
clkSym_RTC_CLK_FREQ.setReadOnly(True)
clkSym_RTC_CLK_FREQ.setDefaultValue(1024)
clkSym_RTC_CLK_FREQ.setDependencies(setFreq, [
                                    "CONFIG_CLOCK_RTC_SRC", "OSCULP32K_FREQ", "OSC1K_FREQ", "XOSC32K_FREQ", "XOSC1K_FREQ"])

#########################Default Clock##########################################
gclkSym_num[2].setValue(True, 2)
gclkSym_GENCTRL_SRC[2].setValue(6, 2)
gclkSym_GENCTRL_DIV[2].setValue(48, 2)
Database.setSymbolValue("core", "GCLK_ID_1_CHEN", True, 2)
Database.setSymbolValue("core", "GCLK_ID_1_GENSEL", 2, 2)
Database.setSymbolValue("core", "CONFIG_CLOCK_DPLL0_ENABLE", True, 2)
Database.setSymbolValue("core", "CONFIG_CLOCK_DPLL0_REF_CLOCK", 3, 2)
Database.setSymbolValue("core", "CONFIG_CLOCK_DPLL0_LDR_INTEGER", 119, 2)
gclkSym_GENCTRL_SRC[0].setValue(7, 2)
################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clockSym_OSCCTRL_HeaderFile = coreComponent.createFileSymbol(
    "CLOCK_HEADER_FILE", None)
clockSym_OSCCTRL_HeaderFile.setSourcePath(
    "../peripheral/clk_sam_d51_e51_e53_e54/templates/plib_clock.h.ftl")
clockSym_OSCCTRL_HeaderFile.setOutputName("plib_clock.h")
clockSym_OSCCTRL_HeaderFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setProjectPath(
    "config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setType("HEADER")
clockSym_OSCCTRL_HeaderFile.setMarkup(True)

clockSym_OSCCTRL_SourceFile = coreComponent.createFileSymbol(
    "CLOCK_SOURCE_FILE", None)
clockSym_OSCCTRL_SourceFile.setSourcePath(
    "../peripheral/clk_sam_d51_e51_e53_e54/templates/plib_clock.c.ftl")
clockSym_OSCCTRL_SourceFile.setOutputName("plib_clock.c")
clockSym_OSCCTRL_SourceFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setProjectPath(
    "config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setType("SOURCE")
clockSym_OSCCTRL_SourceFile.setMarkup(True)

clockSystemInitFile = coreComponent.createFileSymbol("CLOCK_INIT", None)
clockSystemInitFile.setType("STRING")
clockSystemInitFile.setOutputName(
    "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clockSystemInitFile.setSourcePath(
    "../peripheral/clk_sam_d51_e51_e53_e54/templates/system/initialization.c.ftl")
clockSystemInitFile.setMarkup(True)

clockSystemDefFile = coreComponent.createFileSymbol("CLOCK_SYS_DEF", None)
clockSystemDefFile.setType("STRING")
clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clockSystemDefFile.setSourcePath(
    "../peripheral/clk_sam_d51_e51_e53_e54/templates/system/definitions.h.ftl")
clockSystemDefFile.setMarkup(True)
