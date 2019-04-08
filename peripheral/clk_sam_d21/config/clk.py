# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

Log.writeInfoMessage("Loading osctrl Manager for " + Variables.get("__PROCESSOR"))

from os.path import join
from xml.etree import ElementTree
from collections import defaultdict
global topsort
clkMenu = coreComponent.createMenuSymbol("SAMD21_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")

# Clock Source Configuration
clkSourceMenu = coreComponent.createMenuSymbol("CLOCK_SOURCE", clkMenu)
clkSourceMenu.setLabel("Clock Source Configuration")

sysctrl_OSC8M = coreComponent.createMenuSymbol("OSC8_MENU", clkSourceMenu)
sysctrl_OSC8M.setLabel("8MHz Internal Oscillator Configuration")

sysctrlXosc_Menu = coreComponent.createMenuSymbol("XOSCCTRL_MENU", clkSourceMenu)
sysctrlXosc_Menu.setLabel("External Crystal Oscillator Configuration")

osc32k_Menu = coreComponent.createMenuSymbol("OSC32K_MENU", clkSourceMenu)
osc32k_Menu.setLabel("32Khz Internal Oscillator Configuration")

xosc32k_Menu = coreComponent.createMenuSymbol("XOSC32K_MENU", clkSourceMenu)
xosc32k_Menu.setLabel("32Khz External Oscillator Configuration")

dfll_Menu = coreComponent.createMenuSymbol("DFLL_MENU", clkSourceMenu)
dfll_Menu.setLabel("DFLL Configuration")

dpll_Menu = coreComponent.createMenuSymbol("DPLL_MENU", clkSourceMenu)
dpll_Menu.setLabel("Fractional DPLL (FDPLL) Configuration")

# Clock Generator Configuration
clkGen_Menu = coreComponent.createMenuSymbol("GCLK_MENU", clkMenu)
clkGen_Menu.setLabel("Generic Clock Generator (GCLK) Configuration")

gclkGen_Menu = coreComponent.createMenuSymbol("GCLK_GEN_MENU", clkGen_Menu)
gclkGen_Menu.setLabel("Generator Configuration")

gclkPeriChannel_menu = coreComponent.createMenuSymbol("GCLK_PERI_MENU",clkGen_Menu)
gclkPeriChannel_menu.setLabel("Peripheral Channel Configuration")

# Main Clock Configuration
pmSym_Menu = coreComponent.createMenuSymbol("PM_MENU", clkMenu)
pmSym_Menu.setLabel("Synchronous Clock Configuration")

# Peripheral Clock Configuration
peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLOCK_MENU", clkMenu)
peripheralClockMenu.setLabel("Peripheral Clock Configuration")

# Calculated Frequency Menu
calculatedFreq_Menu = coreComponent.createMenuSymbol("FREQ_MENU", clkMenu)
calculatedFreq_Menu.setLabel("Clock Frequencies")

#################################################################################################
################################################################################
##########              Callback Functions            ##########################
################################################################################

def setOSC8MFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_OSC8M_ENABLE")
    freq = int(Database.getSymbolValue("core", "CONFIG_CLOCK_OSC8M_FREQ"))

    pres = int(Database.getSymbolValue("core", "CONFIG_CLOCK_OSC8M_PRES"))

    if enable:
        symbol.setValue((freq)/ (2**pres), 2)

    else:
        symbol.setValue(0, 2)

def setXOSCGain(symbol, event):
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


def setXOSCFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_XOSC_ENABLE")

    if enable:
        symbol.setValue(Database.getSymbolValue("core", "CONFIG_CLOCK_XOSC_FREQUENCY"), 1)
    else:
        symbol.setValue(0, 1)

def setOSC32KFreq(symbol, event):
    osc32kEnable = Database.getSymbolValue("core","OSC32K_EN32K")
    oscEnable = Database.getSymbolValue("core","CONF_CLOCK_OSC32K_ENABLE")
    if oscEnable and osc32kEnable:
        symbol.setValue(32768, 1)
    else:
        symbol.setValue(0, 1)

def setXOSC32KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xosc32k = Database.getSymbolValue("core", "XOSC32K_EN32K")

    if xosc and xosc32k:
        symbol.setValue(32768, 1)
    else:
        symbol.setValue(0, 1)

def setDfllFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")
    freq = 0
    if enable:
        mode = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE")
        if mode == 0:
            freq = 48000000
        else:
            mul =  int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_MUL"))
            refFreq = int(Database.getSymbolValue("core", "GCLK_ID_0_FREQ"))
            freq = mul*refFreq

    symbol.setValue(freq, 2)

def setDPLLClockFreq(symbol, event):

    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")

    if enable:
        clockSrc = Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_REF_CLOCK")

        # XOSC32K Clock
        if clockSrc == 0:
            srcFreq = Database.getSymbolValue("core", "XOSC32K_FREQ")

        # XOSC Clock
        elif clockSrc == 1:
            divisor = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_DIVIDER"))
            srcFreq = int(Database.getSymbolValue("core", "XOSC0_FREQ")) / (2 * (divisor + 1))

        # GCLK_DPLL Clock
        elif clockSrc == 2:
            srcFreq = int(Database.getSymbolValue("core","GCLK_ID_1_FREQ"))

        else:
            return

        ldr = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDR_INTEGER"))
        ldrFrac = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION"))

        dpllFreq = int(srcFreq * (ldr + 1.0 + (ldrFrac/16.0)))

        symbol.setValue(dpllFreq, 1)
    else:
        symbol.setValue(0, 1)


def calcDpllMultiplier(symbol, event):
    ldr = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDR_INTEGER"))
    ldrFrac = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION"))
    multiplier = (ldr + 1.0 + (ldrFrac/16.0))
    symbol.setValue(multiplier,2)

def calcDpllXoscDivider(symbol, event):
    divisor = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_DIVIDER"))
    div_value = (2 * (divisor + 1))
    symbol.setValue(div_value,2)

################################################################################
#######          SYSCTRL Database Components      ##############################
################################################################################

##############################OSC8M#############################################

osc8MEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC8M_ENABLE", sysctrl_OSC8M)
osc8MEnable.setLabel("8MHz Internal Oscillator(OSC8M) Enable")
osc8MEnable.setDescription("Internal 8mhz Oscillator Configuration enable feature")
osc8MEnable.setDefaultValue(True)

osc8MOverwrite = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC8M_CALIB_OVERWRITE", sysctrl_OSC8M)
osc8MOverwrite.setLabel("Overwrite Default Oscillator Calibration")
osc8MOverwrite.setDescription("Overwrite Default Oscillator Calibration")
osc8MOverwrite.setDefaultValue(False)

osc8MCalibValue = coreComponent.createIntegerSymbol("CONFIG_CLOCK_OSC8M_CALIB_VALUE", sysctrl_OSC8M)
osc8MCalibValue.setLabel("Oscillator Calibration Value")
osc8MCalibValue.setDescription("Set the Oscillator Calibration Value")
osc8MCalibValue.setMin(0)
osc8MCalibValue.setMax(0xFFF)
osc8MCalibValue.setDefaultValue(0)

osc8MFreqVal = coreComponent.createIntegerSymbol("CONFIG_CLOCK_OSC8M_FREQ", sysctrl_OSC8M)
osc8MFreqVal.setLabel("Set OSC8M Frequency")
osc8MFreqVal.setDescription("Default frequency range of OSC 8m can be changed using the FREQRANGE and CALIB bitfields in fuse settings")
osc8MFreqVal.setDefaultValue(8000000)

osc8MOndemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC8M_ONDEMAND", sysctrl_OSC8M)
osc8MOndemand.setLabel("Oscillator On-Demand Control")
osc8MOndemand.setOutputMode("Key")
osc8MOndemand.setDisplayMode("Description")
osc8MOndemand.setDescription("Configures the osc8m on Demand Behavior")
osc8MOndemand.addKey("DISABLE",str(0),"Always Enable")
osc8MOndemand.addKey("ENABLE",str(1),"Only on Peripheral Request")
osc8MOndemand.setDefaultValue(0)

osc8MRunstdby = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC8M_RUNSTDY", sysctrl_OSC8M)
osc8MRunstdby.setLabel("Run Oscillator in Standby Sleep Mode")
osc8MRunstdby.setDescription("osc8m run in StandBy Mode or Not")
osc8MRunstdby.setDefaultValue(False)

osc8MPres = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC8M_PRES",sysctrl_OSC8M)
osc8MPres.setLabel("Oscillator Prescalar")
osc8MPres.setDescription("The oscillator frequency is 8MHz divided by 2^PRES")
osc8mDivNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_OSC8M__PRESC\"]")
osc8mDivNodeValues = []
osc8mDivNodeValues = osc8mDivNode.getChildren()

for index in range(0, len(osc8mDivNodeValues)):
    osc8mdivKeyName = osc8mDivNodeValues[index].getAttribute("name")
    osc8mdivKeyDescription = "FREQ/" +osc8mDivNodeValues[index].getAttribute("caption")
    osc8mdivKeyValue = osc8mDivNodeValues[index].getAttribute("value")
    osc8MPres.addKey(osc8mdivKeyName, osc8mdivKeyValue , osc8mdivKeyDescription)

osc8MPres.setDefaultValue(0)
osc8MPres.setOutputMode("Value")
osc8MPres.setDisplayMode("Description")

osc8MFreq = coreComponent.createIntegerSymbol("OSC8M_CLOCK_FREQ", calculatedFreq_Menu)
osc8MFreq.setLabel("OSC 8M Clock Frequency")
osc8MFreq.setReadOnly(True)
osc8MFreq.setDefaultValue(8000000)
osc8MFreq.setDependencies(setOSC8MFreq, ["CONFIG_CLOCK_OSC8M_ENABLE", "CONFIG_CLOCK_OSC8M_PRES", "CONFIG_CLOCK_OSC8M_FREQ"])

######################################XOSC##########################################################

xoscEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_ENABLE", sysctrlXosc_Menu)
xoscEnable.setLabel("External Multipurpose Crystal Oscillator(XOSC) Enable")
xoscEnable.setDescription("External Crystal Oscillator Enable Feature")
xoscEnable.setDefaultValue(False)


xoscAmpgc = coreComponent.createBooleanSymbol("XOSC_AMPGC", sysctrlXosc_Menu)
xoscAmpgc.setLabel("Automatic Gain Control ")
xoscAmpgc.setDefaultValue(False)

xoscCryMode = coreComponent.createKeyValueSetSymbol("XOSC_OSCILLATOR_MODE", sysctrlXosc_Menu)
xoscCryMode.setLabel("External Oscillator Mode ")
xoscCryMode.addKey("EXTERNAL_CLOCK","0","xosc external clock enable")
xoscCryMode.addKey("CRYSTAL","1","crystal oscillator enable")
xoscCryMode.setOutputMode("Value")
xoscCryMode.setDefaultValue(1)

xoscInFreq = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_FREQUENCY", sysctrlXosc_Menu)
xoscInFreq.setLabel("Frequency")
xoscInFreq.setDescription("Setting the XOSC Frequency")
xoscInFreq.setDefaultValue(8000000)
xoscInFreq.setMax(32000000)
xoscInFreq.setMin(400000)

xoscGain = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_GAIN", sysctrlXosc_Menu)
xoscGain.setLabel("Gain")
xoscGain.setDefaultValue(2)
xoscGain.setDescription("Setting the XOSC Frequency")
xoscGain.setVisible(False)
xoscGain.setDependencies(setXOSCGain, ["CONFIG_CLOCK_XOSC_FREQUENCY"])


xoscOndemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_ONDEMAND", sysctrlXosc_Menu)
xoscOndemand.setLabel("Oscillator On-Demand Control")
xoscOndemand.setDescription("Configures the XOSC on Demand Behavior")
xoscOndemand.setOutputMode("Key")
xoscOndemand.setDisplayMode("Description")
xoscOndemand.addKey("DISABLE",str(0),"Always Enable")
xoscOndemand.addKey("ENABLE",str(1),"Only on Peripheral Request")
xoscOndemand.setDefaultValue(0)

xoscStartup = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_STARTUP",sysctrlXosc_Menu)
xoscStartup.setLabel("Oscillator Startup Time")
xoscStartup.setDescription("Startup time for the XOSC ")
xoscStartupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_XOSC__STARTUP\"]")
xoscStartupValues = []
xoscStartupValues = xoscStartupNode.getChildren()
for index in range(0, len(xoscStartupValues)):
    xoscstartupKeyName = xoscStartupValues[index].getAttribute("name")
    xoscstartupKeyDescription = xoscStartupValues[index].getAttribute("caption")
    xoscstartupKeyValue = xoscStartupValues[index].getAttribute("value")
    xoscStartup.addKey(xoscstartupKeyName, xoscstartupKeyValue , xoscstartupKeyDescription)

xoscStartup.setDefaultValue(0)
xoscStartup.setOutputMode("Value")
xoscStartup.setDisplayMode("Description")

xoscRunstdby = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_RUNSTDBY", sysctrlXosc_Menu)
xoscRunstdby.setLabel("Run Oscillator in Standby Sleep Mode")
xoscRunstdby.setDescription("External oscillator RunIn StandBy mode or not")
xoscRunstdby.setDefaultValue(False)

xoscFreq = coreComponent.createIntegerSymbol("XOSC_FREQ", calculatedFreq_Menu)
xoscFreq.setLabel("XOSC Frequency")
xoscFreq.setDefaultValue(0)
xoscFreq.setReadOnly(True)
xoscFreq.setDependencies(setXOSCFreq, ["CONFIG_CLOCK_XOSC_ENABLE", "CONFIG_CLOCK_XOSC_FREQUENCY"])

#################################OSC32K#########################################

osc32kEnable = coreComponent.createBooleanSymbol("CONF_CLOCK_OSC32K_ENABLE", osc32k_Menu)
osc32kEnable.setLabel("32Khz Internal Oscillator(OSC32K) Enable")
osc32kEnable.setDefaultValue(False)

#OSC32K Oscillator Run StandBy Mode
osc32kRunstdby = coreComponent.createBooleanSymbol("OSC32K_RUNSTDBY", osc32k_Menu)
osc32kRunstdby.setLabel("Run Oscillator in Standby Sleep Mode")

#OSC32K Oscillator ONDEMAND Mode
osc32kOndemand= coreComponent.createKeyValueSetSymbol("OSC32K_ONDEMAND", osc32k_Menu)
osc32kOndemand.setLabel("Oscillator On-Demand Control")
osc32kOndemand.setDescription("Configures the OSC32K on Demand Behavior")
osc32kOndemand.setOutputMode("Key")
osc32kOndemand.setDisplayMode("Description")
osc32kOndemand.addKey("DISABLE",str(0),"Always Enable")
osc32kOndemand.addKey("ENABLE",str(1),"Only on Peripheral Request")
osc32kOndemand.setDefaultValue(0)

#OSC32K Oscillator 32KHz Output Enable Mode
osc32kEn32k = coreComponent.createBooleanSymbol("OSC32K_EN32K", osc32k_Menu)
osc32kEn32k.setLabel("Enable 32KHz Output")

#OSC32K Oscillator StartUp Time
osc32kStartup = coreComponent.createKeyValueSetSymbol("OSC32K_STARTUP", osc32k_Menu)
osc32kStartup.setLabel("Oscillator Startup Time ")
osc32kStartupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_OSC32K__STARTUP\"]")
osc32kStartupValues = osc32kStartupNode.getChildren()

for index in range(0, len(osc32kStartupValues)):
    osc32kstartupKeyName = osc32kStartupValues[index].getAttribute("name")
    osc32kstartupKeyDescription = osc32kStartupValues[index].getAttribute("caption")
    osc32kstartupKeyValue= osc32kStartupValues[index].getAttribute("value")
    osc32kStartup.addKey(osc32kstartupKeyName, osc32kstartupKeyValue , osc32kstartupKeyDescription)

osc32kStartup.setDefaultValue(0)
osc32kStartup.setOutputMode("Value")
osc32kStartup.setDisplayMode("Description")

osc32kFreq = coreComponent.createIntegerSymbol("OSC32K_FREQ", calculatedFreq_Menu)
osc32kFreq.setLabel("OSC32K Frequency")
osc32kFreq.setDefaultValue(0)
osc32kFreq.setReadOnly(True)
osc32kFreq.setDependencies(setOSC32KFreq, ["OSC32K_EN32K", "CONF_CLOCK_OSC32K_ENABLE"])

#################################XOSC32K########################################

xosc32kEnable = coreComponent.createBooleanSymbol("CONF_CLOCK_XOSC32K_ENABLE", xosc32k_Menu)
xosc32kEnable.setLabel("32KHz External Crystal Oscillator(XOSC32K) Enable")
xosc32kEnable.setDefaultValue(False)

xosc32kMode = coreComponent.createKeyValueSetSymbol("XOSC32K_OSCILLATOR_MODE", xosc32k_Menu)
xosc32kMode.setLabel("32KHz External Oscillator Mode ")
xosc32kMode.addKey("EXTERNAL_CLOCK","0","xosc32K external clock enable")
xosc32kMode.addKey("CRYSTAL","1","crystal oscillator enable")
xosc32kMode.setOutputMode("Value")
xosc32kMode.setDefaultValue(1)

xosc32kRunstdby = coreComponent.createBooleanSymbol("XOSC32K_RUNSTDBY", xosc32k_Menu)
xosc32kRunstdby.setLabel("Run Oscillator in Standby Sleep Mode")

xosc32kOndemand= coreComponent.createKeyValueSetSymbol("XOSC32K_ONDEMAND", xosc32k_Menu)
xosc32kOndemand.setLabel("Oscillator On-Demand Control")
xosc32kOndemand.setDescription("Configures the XOSC32K on Demand Behavior")
xosc32kOndemand.setOutputMode("Key")
xosc32kOndemand.setDisplayMode("Description")
xosc32kOndemand.addKey("DISABLE",str(0),"Always Enable")
xosc32kOndemand.addKey("ENABLE",str(1),"Only on Peripheral Request")
xosc32kOndemand.setDefaultValue(0)

xosc32kAAMPEN = coreComponent.createBooleanSymbol("XOSC32K_AAMPEN", xosc32k_Menu)
xosc32kAAMPEN.setLabel("Enable Automatic Amplitude Control For Crystal Oscillator")

xoscEn32k = coreComponent.createBooleanSymbol("XOSC32K_EN32K", xosc32k_Menu)
xoscEn32k.setLabel("Enable 32KHz Output")

xosc32kStartup = coreComponent.createKeyValueSetSymbol("XOSC32K_STARTUP", xosc32k_Menu)
xosc32kStartup.setLabel("Oscillator Startup Time ")
xosc32kStartup.setDescription("XOSC start up time ")
xosc32kStartupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_XOSC32K__STARTUP\"]")
xosc32kStartupValues = xosc32kStartupNode.getChildren()
for index in range(0, len(xosc32kStartupValues)):
    xosc32kstartupKeyName = xosc32kStartupValues[index].getAttribute("name")
    xosc32kstartupKeyDescription = xosc32kStartupValues[index].getAttribute("caption")
    xosc32kstartupKeyValue = xosc32kStartupValues[index].getAttribute("value")
    xosc32kStartup.addKey(xosc32kstartupKeyName, xosc32kstartupKeyValue , xosc32kstartupKeyDescription)

xosc32kStartup.setDefaultValue(0)
xosc32kStartup.setOutputMode("Value")
xosc32kStartup.setDisplayMode("Description")

xosc32KFreq = coreComponent.createIntegerSymbol("XOSC32K_FREQ", calculatedFreq_Menu)
xosc32KFreq.setLabel("XOSC32K Frequency")
xosc32KFreq.setDefaultValue(0)
xosc32KFreq.setReadOnly(True)
xosc32KFreq.setDependencies(setXOSC32KFreq, ["CONF_CLOCK_XOSC32K_ENABLE", "XOSC32K_EN32K"])

#################################OSCULP32k######################################
clkSym_OSCULP32K_Freq = coreComponent.createIntegerSymbol("OSCULP32K_FREQ", calculatedFreq_Menu)
clkSym_OSCULP32K_Freq.setLabel("OSCULP32K Frequency")
clkSym_OSCULP32K_Freq.setDefaultValue(32768)
clkSym_OSCULP32K_Freq.setReadOnly(True)

################################DFLL############################################
dfllEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_ENABLE",dfll_Menu)
dfllEnable.setLabel("Enable DFLL")
dfllEnable.setDescription("Enable DFLL")
dfllEnable.setDefaultValue(False)

dfllOpmode = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_OPMODE", dfll_Menu)
dfllOpmode.setLabel("DFLL operation mode")
dfllOpmode.setDescription("Selects DFLL operating mode")
dfllOpmode.setOutputMode("Value")
dfllOpmode.setDisplayMode("Key")
dfllOpmode.addKey("Open",str(0),"The DFLL operates in open-loop operation.")
dfllOpmode.addKey("Closed",str(1),"The DFLL operates in closed-loop operation.")
dfllOpmode.setDefaultValue(0)

dfllOndemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_ONDEMAND", dfll_Menu)
dfllOndemand.setLabel("DFLL On-Demand Control")
dfllOndemand.setDescription("Configures the DFLL on Demand Behavior")
dfllOndemand.setOutputMode("Value")
dfllOndemand.setDisplayMode("Description")
dfllOndemand.addKey("Disable",str(0),"Always Enable")
dfllOndemand.addKey("Enable",str(1),"Only on Peripheral Request")
dfllOndemand.setDefaultValue(0)

dfllRunstdy = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_RUNSTDY", dfll_Menu)
dfllRunstdy.setLabel("Run DFLL in Standby Sleep Mode")
dfllRunstdy.setDescription("DFLL to run in standby mode or not")
dfllRunstdy.setDefaultValue(False)

dfllUsb = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_USB", dfll_Menu)
dfllUsb.setLabel("USB Clock Recovery Mode")
dfllUsb.setDescription("Enable or Disable USB Clock Recovery Mode")
dfllUsb.setDefaultValue(False)

dfllWaitLock = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_WAIT_LOCK", dfll_Menu)
dfllWaitLock.setLabel("Wait for DFLL lock")
dfllWaitLock.setDescription("Controls the DFLL output clock, depending on lock status")
dfllWaitLock.setDefaultValue(False)

dfllBypassCoarse = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_BYPASS_COARSE", dfll_Menu)
dfllBypassCoarse.setLabel("Bypass Coarse Lock")
dfllBypassCoarse.setDescription("Controls the coarse lock procedure")
dfllBypassCoarse.setDefaultValue(False)

dfllQuickLock = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_QUICK_LOCK", dfll_Menu)
dfllQuickLock.setLabel("Quick lock disable")
dfllQuickLock.setDescription("Disable quick lock")
dfllQuickLock.setDefaultValue(False)

dfllChillCycle = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_CHILL_CYCLE", dfll_Menu)
dfllChillCycle.setLabel("Chill Cycle Disable")
dfllChillCycle.setDescription("Disable Chill Cycle")
dfllChillCycle.setDefaultValue(False)

dfllLLAW = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_LLAW", dfll_Menu)
dfllLLAW.setLabel("Lose Lock After Wake")
dfllLLAW.setDescription("Lose Lock After Wake")
dfllLLAW.setDefaultValue(False)

dfllStable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_STABLE", dfll_Menu)
dfllStable.setLabel("Stable DFLL Frequency")
dfllStable.setDescription("FINE calibration tracks changes in output frequency")
dfllStable.setDefaultValue(False)

dfllCoarse = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DFLL_COARSE", dfll_Menu)
dfllCoarse.setDefaultValue(1)
dfllCoarse.setMin(0)
dfllCoarse.setMax(31)
dfllCoarse.setLabel("Coarse Maximum Step")

dfllFine = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DFLL_FINE", dfll_Menu)
dfllFine.setDefaultValue(1)
dfllFine.setMin(0)
dfllFine.setMax(255)
dfllFine.setLabel("Fine Maximum Step")

dfllMul = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DFLL_MUL", dfll_Menu)
dfllMul.setDefaultValue(1)
dfllMul.setMin(0)
dfllMul.setMax(65535)
dfllMul.setLabel("DFLL Multiply Factor")

dfllFreq = coreComponent.createIntegerSymbol("DFLL_CLOCK_FREQ", calculatedFreq_Menu)
dfllFreq.setReadOnly(True)
dfllFreq.setDefaultValue(0)
dfllFreq.setLabel("DFLL Clock Frequency")
dfllFreq.setDependencies(setDfllFreq,["CONFIG_CLOCK_DFLL_ENABLE",
                                     "CONFIG_CLOCK_DFLL_OPMODE",
                                     "CONFIG_CLOCK_DFLL_MUL",
                                     "GCLK_ID_0_FREQ"])
################################DPLL############################################
dpllEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_ENABLE", dpll_Menu)
dpllEnable.setLabel("Digital Phase Locked Loop(DPLL) Enable ")
dpllEnable.setDescription("DPLL Configuration enabling feature")
dpllEnable.setDefaultValue(False)

dpllOndemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_ONDEMAND", dpll_Menu)
dpllOndemand.setLabel("DPLL On-Demand Control")
dpllOndemand.setDescription("Configures the DPLL on Demand Behavior")
dpllOndemand.setOutputMode("Value")
dpllOndemand.setDisplayMode("Description")
dpllOndemand.addKey("Disable",str(0),"Always Enable")
dpllOndemand.addKey("Enable",str(1),"Only on Peripheral Request")
dpllOndemand.setDefaultValue(0)

dpllRunstdby = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_RUNSTDY", dpll_Menu)
dpllRunstdby.setLabel("Run DPLL in Standby Sleep Mode")
dpllRunstdby.setDescription("DPLL to run in standby mode or not")
dpllRunstdby.setDefaultValue(False)

dpllLdr = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDR_INTEGER", dpll_Menu)
dpllLdr.setLabel("DPLL Loop Divider Ratio Integer Part")
dpllLdr.setDescription("Loop divider ratio integer value")
dpllLdr.setDefaultValue(0)
dpllLdr.setMin(0)

dpllLdrfrac = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION", dpll_Menu)
dpllLdrfrac.setLabel("DPLL Loop Divider Ratio Fractional Part")
dpllLdrfrac.setDescription("loop divider ratio fraction value")
dpllLdrfrac.setDefaultValue(0)
dpllLdrfrac.setMin(0)

dpllLbypass = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOCK_BYPASS", dpll_Menu)
dpllLbypass.setLabel("Bypass DPLL Lock?")
dpllLbypass.setDescription("DPLL Lock signal is always asserted or DPLL Lock signal drives the DPLL controller internal logic.")
dpllLbypass.setDefaultValue(False)

# DPLL Multiplier value to show in the UI
dpllMul = coreComponent.createFloatSymbol("CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE", dpll_Menu)
dpllMul.setVisible(False)
dpllMul.setDefaultValue(1)
dpllMul.setDependencies(calcDpllMultiplier,["CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION","CONFIG_CLOCK_DPLL_LDR_INTEGER"])

dpllLpen = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE", dpll_Menu)
dpllLpen.setLabel("DPLL Low Power Enable")
dpllLpen.setDescription("Low Power Mode Enabled or not")
dpllLpen.setDefaultValue(False)

dpllWuf = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_WAKEUP_FAST", dpll_Menu)
dpllWuf.setLabel("DPLL Fast Output Enable")
dpllWuf.setDescription("DPLL clock is Output after startup and lock time or only after the startup")
dpllWuf.setDefaultValue(False)

dpllLtime = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_LOCK_TIME", dpll_Menu)
dpllLtime.setLabel("DPLL Lock Time-out")
dpllLtime.setDescription("select the lock time-out value:")
dpllLtime.setVisible(False)
dpllLtimeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_DPLLCTRLB__LTIME\"]")
dpllLtimeValues = dpllLtimeNode.getChildren()
for index in range(0, len(dpllLtimeValues)):
    dpllLockTimeKeyName = dpllLtimeValues[index].getAttribute("name")
    dpllLockTimeKeyDescription = dpllLtimeValues[index].getAttribute("caption")
    dpllLockTimeKeyValue = dpllLtimeValues[index].getAttribute("value")
    dpllLtime.addKey(dpllLockTimeKeyName, dpllLockTimeKeyValue , dpllLockTimeKeyDescription)

dpllLtime.setDefaultValue(0)
dpllLtime.setOutputMode("Value")
dpllLtime.setDisplayMode("Description")


dpllFilter = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_FILTER", dpll_Menu)
dpllFilter.setLabel("DPLL Feedback Filter Selection")
dpllFilter.setDescription("DPLL filter type selection")
dpllFilterNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_DPLLCTRLB__FILTER\"]")
dpllFilterValues = dpllFilterNode.getChildren()
for index in range(0, len(dpllFilterValues)):
    dpllfilterKeyName = dpllFilterValues[index].getAttribute("name")
    dpllfilterKeyDescription = dpllFilterValues[index].getAttribute("caption")
    dpllfilterKeyValue = dpllFilterValues[index].getAttribute("value")
    dpllFilter.addKey(dpllfilterKeyName, dpllfilterKeyValue , dpllfilterKeyDescription)

dpllFilter.setDefaultValue(0)
dpllFilter.setOutputMode("Value")
dpllFilter.setDisplayMode("Description")

dpllRef = ["XOSC32K", "XOSC", "GCLK_DPLL"]
dpllRefclk = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_REF_CLOCK", dpll_Menu)
dpllRefclk.setLabel("DPLL Reference Clock Source")
dpllRefclk.setDescription("DPLL reference clock selection")
dpllRefclk.setOutputMode("Value")
dpllRefclkNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SYSCTRL\"]/value-group@[name=\"SYSCTRL_DPLLCTRLB__REFCLK\"]")
dpllRefclkValues = dpllRefclkNode.getChildren()
for index in range(0, len(dpllRefclkValues)):
    dpllrefclockKeyName = dpllRef[index]
    dpllrefclockKeyDescription = dpllRefclkValues[index].getAttribute("caption")
    dpllrefclockKeyValue = dpllRefclkValues[index].getAttribute("value")
    dpllRefclk.addKey(dpllrefclockKeyName, dpllrefclockKeyValue , dpllrefclockKeyDescription)

dpllRefclk.setDefaultValue(0)
dpllRefclk.setOutputMode("Value")
dpllRefclk.setDisplayMode("Key")

dpllDiv = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_DIVIDER", dpll_Menu)
dpllDiv.setLabel("DPLL Divider")
dpllDiv.setDescription("XOSC clock division factor fdiv = (fxosc/((2*DIV)+1))")
dpllDiv.setDefaultValue(0)
dpllDiv.setMin(0)

# DPLL divider value to show in UI
dpllDivUI = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_DIVIDER_VALUE", dpll_Menu)
dpllDivUI.setDefaultValue(2)
dpllDivUI.setDependencies(calcDpllXoscDivider,["CONFIG_CLOCK_DPLL_DIVIDER"])

dpllFreq = coreComponent.createIntegerSymbol("DPLL_CLOCK_FREQ", calculatedFreq_Menu)
dpllFreq.setReadOnly(True)
dpllFreq.setDefaultValue(0)
dpllFreq.setLabel("DPLL Clock Frequency")

dpllFreq.setDependencies(setDPLLClockFreq, ["CONFIG_CLOCK_DPLL_ENABLE",
                                                          "XOSC32K_FREQ",
                                                          "XOSC_FREQ",
                                                          "CONFIG_CLOCK_DPLL_DIVIDER",
                                                          "CONFIG_CLOCK_DPLL_REF_CLOCK",
                                                          "CONFIG_CLOCK_DPLL_LDR_INTEGER",
                                                          "CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION",
                                                          "GCLK_ID_1_FREQ"])

###############################GCLK CALLBACKS###################################
def setPCHCTRLFREQVisibleProperty(symbol, event):
    index = symbol.getID().split("_FREQ")[0]
    if "_FREQ" not in event["id"]:
        perifreq = Database.getSymbolValue("core",index + "_GENSEL")
        channel = Database.getSymbolValue("core", index + "_CHEN")
        if channel:
            if perifreq == 0:
                srcFreq = Database.getSymbolValue("core","GCLK_0_FREQ")
                symbol.setValue(srcFreq,1)

            elif perifreq == 1:
                srcFreq = Database.getSymbolValue("core","GCLK_1_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 2:
                srcFreq = Database.getSymbolValue("core","GCLK_2_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 3:
                srcFreq = Database.getSymbolValue("core","GCLK_3_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 4:
                srcFreq = Database.getSymbolValue("core","GCLK_4_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 5:
                srcFreq = Database.getSymbolValue("core","GCLK_5_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 6:
                srcFreq = Database.getSymbolValue("core","GCLK_6_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 7:
                srcFreq = Database.getSymbolValue("core","GCLK_7_FREQ")
                symbol.setValue(srcFreq,1)
            elif perifreq == 8:
                srcFreq = Database.getSymbolValue("core","GCLK_8_FREQ")
                symbol.setValue(srcFreq,1)
            else:
                symbol.setValue(0, 1)

        else:
            symbol.setValue(0, 1)

    else:
        if Database.getSymbolValue("core", index + "_CHEN"):
            perifreq = Database.getSymbolValue("core",index + "_GENSEL")
            generator = event["id"].split("_")[1]
            if int(perifreq) == int(generator):
                symbol.setValue(event["value"],1)

def setGClockFreq(symbol, event):
    global gclkSym_GENCTRL_SRC
    index = symbol.getID().split("_")[1]

    enable = Database.getSymbolValue("core", "GCLK_INST_NUM" + index)

    if enable:
        src = gclkSym_GENCTRL_SRC[int(index)].getSelectedKey()

        #XOSC
        if src == "XOSC":
            srcFreq = int(Database.getSymbolValue("core","XOSC_FREQ"))


        elif src == "OSC32K":
            srcFreq = int(Database.getSymbolValue("core","OSC32K_FREQ"))

        elif src == "OSC8M":
            srcFreq = int(Database.getSymbolValue("core","OSC8M_CLOCK_FREQ"))

        # GCLKIN
        elif 'GCLK_IN' in str(src):
            gclk_in_symbol = "GCLK_IO_"+str(index)+"_FREQ"
            srcFreq = int(Database.getSymbolValue("core",gclk_in_symbol))

        # GCLKGEN1
        elif src == "GCLK1":
            if index != 1:
                srcFreq = int(Database.getSymbolValue("core","GCLK_1_FREQ"))

        # OSCULP32K
        elif src == "OSCULP32K":
            srcFreq = 32768

        #XOSC32K
        elif src == "XOSC32K":
            srcFreq = int(Database.getSymbolValue("core", "XOSC32K_FREQ"))

        #DFLL
        elif src == "DFLL":
            srcFreq = int(Database.getSymbolValue("core","DFLL_CLOCK_FREQ"))

        #FDPLL
        elif src == "FDPLL":
            srcFreq = int(Database.getSymbolValue("core","DPLL_CLOCK_FREQ"))


        divSel = int(Database.getSymbolValue("core","GCLK_" + index + "_DIVSEL"))
        div = int(Database.getSymbolValue("core","GCLK_" + index + "_DIV"))

        if divSel == 0:

            if div != 0:
                gclk_freq = int(srcFreq / float(div))
            else:
                gclk_freq = srcFreq

        elif divSel == 1:
            gclk_freq = int(srcFreq / float(2**(div + 1)))

        symbol.setValue(gclk_freq, 1)

    else:
        symbol.setValue(0, 1)

def topsort(graph):
    from collections import deque

    #Initialize the degree of vetexes to zero and increment dependents by 1
    degreeList = {}
    for vertex in graph:
        degreeList[vertex] = 0

    for vertex in graph:
        for dependent in graph[vertex]:
            degreeList[dependent] = degreeList[dependent] + 1

    #initialize a dequeue pipe
    pipe = deque()

    #move vertexes with zero degree to the starting of pipe
    for vertex in degreeList:
        if degreeList[vertex] == 0:
            pipe.appendleft(vertex)

    outputList = []

    #move vertexes with degree 0 to output list
    #visit the dependent and reduce the degree by one for every visited dependent
    while pipe:
        vertex = pipe.pop()
        outputList.append(vertex)
        for dependent in graph[vertex]:
            degreeList[dependent] -= 1
            if degreeList[dependent] == 0:
                pipe.appendleft(dependent)

    #If there are no cycles that is the max degree of all vertices is 1
    #then the length of list should be equal to total number of vertices in graph else a cycle has been formed
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
                    "DFLL" : [],
                    "FDPLL" : [],
                    "GCLK0" : [],
                    "GCLK1" : [],
                    "GCLK2" : [],
                    "GCLK3" : [],
                    "GCLK4" : [],
                    "GCLK5" : [],
                    "GCLK6" : [],
                    "GCLK7" : [],
                    "GCLK8" : [],
                    }
    symbol.clearValues()
    codeList = []

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == True :
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE"))) == 1):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core", "GCLK_ID_0_GENSEL"))].append("DFLL")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")) == True :
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_REF_CLOCK"))) == 2):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core", "GCLK_ID_1_GENSEL"))].append("FDPLL")

    for i in range(0, 9):
        if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)):
           if gclkSym_GENCTRL_SRC[i].getSelectedKey() in ["DFLL", "FDPLL", "GCLK1"]:
                sourceDestmap[gclkSym_GENCTRL_SRC[i].getSelectedKey()].append("GCLK"+str(i))

    codeList = topsort(sourceDestmap)
    if len(codeList) != 0:
        cycleFormed.setValue(False,2)


        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == False :
            codeList.remove("DFLL")
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")) == False :
            codeList.remove("FDPLL")
        for i in range(0, 12):
            if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)) == False:
                codeList.remove("GCLK"+str(i))

        for i in range(0,len(codeList)):
            symbol.addValue("    " + codeList[i] + "_Initialize();")
    else:
        cycleFormed.setValue(True,2)

def clkSetup(symbol, event):
    global indexSymbolMap
    symbolKey = ""
    status = False
    if "_CLOCK_ENABLE" in event["id"]:
        for key,value in indexSymbolMap.iteritems():
            for i in range(0,len(value)):
                if value[i] == event["id"].split("_CLOCK_ENABLE")[0]:
                    symbolKey = key
                    break
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            status = status | Database.getSymbolValue("core", i + "_CLOCK_ENABLE")
        Database.setSymbolValue("core", symbolKey + "_CHEN", status, 2)
        if event["value"]:
            freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
            Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", freq , 2)
        else :
            Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", 0, 2)

    if "_FREQ" in event["id"]:
        symbolKey = event["id"].split("_FREQ")[0]
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            if Database.getSymbolValue("core", i + "_CLOCK_ENABLE"):
                freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
                Database.setSymbolValue("core", i + "_CLOCK_FREQUENCY", freq , 2)

def calcGclkDivider(symbol, event):
    index = symbol.getID().split("_")[1]
    divSel = int(Database.getSymbolValue("core","GCLK_" + index + "_DIVSEL"))
    div = int(Database.getSymbolValue("core","GCLK_" + index + "_DIV"))

    if divSel == 0:
        if div != 0:
            divider = div
        else:
            divider = 1

    elif divSel == 1:
        divider = 2**(div + 1)

    symbol.setValue(divider,2)

def setGCLKIOFreq(symbol, event):
    index = int(symbol.getID().split("GCLK_IO_")[1].split("_FREQ")[0])
    enable = Database.getSymbolValue("core", "GCLK_" + str(index) + "_OUTPUTENABLE" )
    if enable:
        symbol.setValue(int (Database.getSymbolValue("core", "GCLK_" + str(index) + "_FREQ" )), 2)
    else:
        symbol.setValue(0, 2)


################################GCLK############################################

gclkDependencyList = []

global gclkSym_num,gclkSym_GENCTRL_DIVSEL,gclkSym_GENCTRL_DIV
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

#------------------------- ATDF Read -------------------------------------
packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))

channel = []
availablePins = []        # array to save available pins
gclk_io_signals = [False, False, False, False, False, False, False, False, False] #array to save available signals
pinout = ""
numPads = 0
val = ATDF.getNode("/avr-tools-device-file/variants")
children = val.getChildren()
for index in range(0, len(children)):
    if packageName in children[index].getAttribute("package"):
        pinout = children[index].getAttribute("pinout")


children = []
val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(pinout)+"\"]")
children = val.getChildren()
for pad in range(0, len(children)):
    availablePins.append(children[pad].getAttribute("pad"))


gclk = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"GCLK\"]/instance@[name=\"GCLK\"]/signals")
wakeup_signals = gclk.getChildren()
for pad in range (0 , len(wakeup_signals)):
    if "index" in wakeup_signals[pad].getAttributeList():
        padSignal = wakeup_signals[pad].getAttribute("pad")
        if padSignal in availablePins :
            gclk_io_signals[int(wakeup_signals[pad].getAttribute("index"))] = True

for gclknumber in range(0,9):
    gclkSym_num.append(gclknumber)
    gclkSym_num[gclknumber] = coreComponent.createBooleanSymbol("GCLK_INST_NUM" + str(gclknumber),gclkGen_Menu)
    gclkSym_num[gclknumber].setLabel("Enable Generic Clock Generator " + str(gclknumber))
    if( gclknumber == 0):
        gclkSym_num[gclknumber].setDefaultValue(True)
        gclkSym_num[gclknumber].setReadOnly(True)

    #GCLK Generator Run StandBy
    gclkSym_GENCTRL_RUNSTDBY.append(gclknumber)
    gclkSym_GENCTRL_RUNSTDBY[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_RUNSTDBY", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setLabel("GCLK should keep running in Standby mode")

    #GCLK External Clock input frequency

    if(gclk_io_signals[gclknumber]==True):
            numPads = numPads + 1
            gclkSym_GCLK_IO_FREQ.append(gclknumber)
            gclkSym_GCLK_IO_FREQ[gclknumber] = coreComponent.createIntegerSymbol("GCLK_IO_" + str(gclknumber) +"_FREQ", gclkSym_num[gclknumber])
            gclkSym_GCLK_IO_FREQ[gclknumber].setLabel("External Input (GCLK_IO[" + str(gclknumber) + "]) Frequency")
            gclkSym_GCLK_IO_FREQ[gclknumber].setDefaultValue(0)
            gclkSym_GCLK_IO_FREQ[gclknumber].setDependencies(setGCLKIOFreq, ["GCLK_" + str(gclknumber) + "_FREQ", "GCLK_" + str(gclknumber) + "_OUTPUTENABLE" ])

    #GCLK Generator Source Selection
    gclkSym_GENCTRL_SRC.append(gclknumber)
    gclkSym_GENCTRL_SRC[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_SRC", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_SRC[gclknumber].setLabel("Source Selection")

    gclkSym_GENCTRL_SRC[gclknumber].addKey("XOSC", "0", "External Crystal Oscillator")

    gclk_in="GCLK_IN["+str(gclknumber)+"]"
    gclk_in_desc= "Generator Input Pad ("+"GCLK_IN["+str(gclknumber)+"])"

    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_SRC[gclknumber].addKey(gclk_in, "1", gclk_in_desc)

    if gclknumber !=1:
        gclkSym_GENCTRL_SRC[gclknumber].addKey("GCLK1", "2", "GCLK Generator 1")

    gclkSym_GENCTRL_SRC[gclknumber].addKey("OSCULP32K", "3", "32 KHz Ultra Low-Power Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("OSC32K", "4", "32 KHz Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("XOSC32K", "5", "32.768 KHz External Crystal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("OSC8M", "6", "OSC8M Internal RC Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("DFLL", "7", "DFLL Oscillator Output")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("FDPLL", "8", "Franctional DPLL Output")
    gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(6)
    gclkSym_GENCTRL_SRC[gclknumber].setOutputMode("Value")
    gclkSym_GENCTRL_SRC[gclknumber].setDisplayMode("Key")



    #GCLK Generator Output Enable
    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_OE.append(gclknumber)
        gclkSym_GENCTRL_OE[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_OUTPUTENABLE", gclkSym_num[gclknumber])
        gclkSym_GENCTRL_OE[gclknumber].setLabel("Output GCLK clock signal on IO pin?")

    #GCLK Generator Output Off Value
    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_OOV.append(gclknumber)
        gclkSym_GENCTRL_OOV[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_OUTPUTOFFVALUE", gclkSym_GENCTRL_OE[gclknumber])
        gclkSym_GENCTRL_OOV[gclknumber].setLabel("Output Off Value")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("LOW","0","Logic Level 0")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("HIGH","1","Logic Level 1")
        gclkSym_GENCTRL_OOV[gclknumber].setDefaultValue(0)
        gclkSym_GENCTRL_OOV[gclknumber].setOutputMode("Key")
        gclkSym_GENCTRL_OOV[gclknumber].setDisplayMode("Description")

        gclkInFreq = coreComponent.createIntegerSymbol("GCLK_IN_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
        gclkInFreq.setLabel("Gclk Input Frequency")
        gclkInFreq.setDefaultValue(0)

    #GCLK Generator Division Selection
    gclkSym_GENCTRL_DIVSEL.append(gclknumber)
    gclkSym_GENCTRL_DIVSEL[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_DIVSEL", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVSEL[gclknumber].setLabel("Divide Selection")
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

    #GCLK Generator Division Factor
    gclkSym_GENCTRL_DIV.append(gclknumber)
    gclkSym_GENCTRL_DIV[gclknumber] = coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_DIV", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIV[gclknumber].setLabel("Division Factor")
    if (gclknumber == 0):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFF)
    elif (gclknumber == 1):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFFFF)
    elif (gclknumber == 2):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0x1F)
    else:
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xFF)

    gclkSym_GENCTRL_DIV[gclknumber].setMin(0)
    gclkSym_GENCTRL_DIV[gclknumber].setDefaultValue(1)


    #GCLK Generator Division Factor to show in the UI
    gclkSym_GENCTRL_DIVIDER_VALUE.append(gclknumber)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber] = coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_DIVIDER_VALUE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setVisible(False)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDefaultValue(1)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDependencies(calcGclkDivider,["GCLK_" + str(gclknumber) + "_DIV", "GCLK_" + str(gclknumber) + "_DIVSEL"])

    #GCLK Generator Improve Duty Cycle
    gclkSym_GENCTRL_IDC.append(gclknumber)
    gclkSym_GENCTRL_IDC[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_IMPROVE_DUTYCYCLE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_IDC[gclknumber].setLabel("Enable 50/50 Duty Cycle")

    gclkSym_Freq.append(gclknumber)
    gclkSym_Freq[gclknumber]=coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
    gclkSym_Freq[gclknumber].setLabel("GCLK" + str(gclknumber) + " Clock Frequency")
    gclkSym_Freq[gclknumber].setReadOnly(True)
    if(gclknumber == 0):
        gclkSym_Freq[gclknumber].setDefaultValue(0)
    else:
        gclkSym_Freq[gclknumber].setDefaultValue(0)

    depList = [ "GCLK_" + str(gclknumber) + "_DIVSEL",
                "GCLK_" + str(gclknumber) + "_DIV",
                "GCLK_" + str(gclknumber) + "_SRC",
                "GCLK_INST_NUM" + str(gclknumber),
                "XOSC_FREQ",
                "OSC8M_CLOCK_FREQ",
                "DPLL_CLOCK_FREQ",
                "DFLL_CLOCK_FREQ",
                "XOSC32K_FREQ",
                "OSC32K_FREQ",
                "GCLK_IN_0_FREQ","GCLK_IN_1_FREQ","GCLK_IN_2_FREQ","GCLK_IN_3_FREQ","GCLK_IN_4_FREQ","GCLK_IN_5_FREQ","GCLK_IN_6_FREQ","GCLK_IN_7_FREQ","GCLK_IN_8_FREQ"
                ]
    if gclknumber != 1:
        depList.append("GCLK_1_FREQ")
    gclkSym_Freq[gclknumber].setDependencies(setGClockFreq, depList)
    gclkSym_Freq[gclknumber].setDefaultValue(Database.getSymbolValue("core", "OSC8M_CLOCK_FREQ"))
    codeGenerationDep.append("GCLK_" + str(gclknumber) + "_SRC")
    codeGenerationDep.append("GCLK_INST_NUM" + str(gclknumber))

maxGCLKId = 0

gclkIOpads = coreComponent.createIntegerSymbol("GCLK_NUM_PADS", None)
gclkIOpads.setVisible(False)
gclkIOpads.setDefaultValue(numPads)

cycleFormed = coreComponent.createBooleanSymbol("GCLK_CYCLE_FORMED", clkMenu)
cycleFormed.setDefaultValue(False)
cycleFormed.setVisible(False)

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

                indexID = param.attrib["value"]
                symbolValue = instance.attrib["name"] + param.attrib["name"].split("GCLK_ID")[1]
                symbolId = "GCLK_ID_" + str(indexID)
                indexSymbolMap[symbolId].append(symbolValue)

                if maxGCLKId < int(indexID):
                    maxGCLKId = int(indexID)


channelMap = {}
for key in indexSymbolMap.keys():
    index=key.split("GCLK_ID_")[1]
    channelMap[int(index)]=key

for index in sorted(channelMap.iterkeys()):
    key=channelMap[index]
    name = indexSymbolMap.get(key)
    name = " ".join(name)

    #GCLK Peripheral Channel Enable
    clkSymPeripheral = coreComponent.createBooleanSymbol(key + "_CHEN", gclkPeriChannel_menu)
    clkSymPeripheral.setLabel("Peripheral Channel " + str(index) + " Clock Enable")
    clkSymPeripheral.setDefaultValue(False)

    #GCLK Peripheral Channel Name
    gclkSym_PERCHANNEL_NAME = coreComponent.createStringSymbol(key + "_NAME", clkSymPeripheral)
    gclkSym_PERCHANNEL_NAME.setLabel("Peripheral")
    gclkSym_PERCHANNEL_NAME.setReadOnly(True)
    gclkSym_PERCHANNEL_NAME.setDefaultValue(name)

    #GCLK Peripheral Channel Index
    gclkSym_PERCHANNEL_INDEX = coreComponent.createIntegerSymbol(key + "_INDEX", clkSymPeripheral)
    gclkSym_PERCHANNEL_INDEX.setVisible(False)
    gclkSym_PERCHANNEL_INDEX.setDefaultValue(int(index))

    #Peripheral Channel Generator Selection
    gclkSym_PCHCTRL_GEN = coreComponent.createKeyValueSetSymbol(key + "_GENSEL", clkSymPeripheral)
    gclkSym_PCHCTRL_GEN.setLabel("Generator Selection")

    gclkSymPCHCTRLGenNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_CLKCTRL__GEN\"]")
    gclkSymPCHCTRLGenNodeValues = []
    gclkSymPCHCTRLGenNodeValues = gclkSymPCHCTRLGenNode.getChildren()

    gclkSymPCHCTRLGenDefaultValue = 0

    for i in range(0, len(gclkSymPCHCTRLGenNodeValues)):
        gclkSymPCHCTRLGenKeyName = gclkSymPCHCTRLGenNodeValues[i].getAttribute("name")

        if (gclkSymPCHCTRLGenKeyName == "GCLK0"):
            gclkSymPCHCTRLGenDefaultValue = i

        gclkSymPCHCTRLGenKeyDescription = gclkSymPCHCTRLGenNodeValues[i].getAttribute("caption")
        ggclkSymPCHCTRLGenKeyValue = gclkSymPCHCTRLGenNodeValues[i].getAttribute("value")
        gclkSym_PCHCTRL_GEN.addKey(gclkSymPCHCTRLGenKeyName, ggclkSymPCHCTRLGenKeyValue , gclkSymPCHCTRLGenKeyDescription)

    gclkSym_PCHCTRL_GEN.setDefaultValue(gclkSymPCHCTRLGenDefaultValue)
    gclkSym_PCHCTRL_GEN.setOutputMode("Value")
    gclkSym_PCHCTRL_GEN.setDisplayMode("Key")

    gclkSym_PCHCTRL_FREQ = coreComponent.createIntegerSymbol(key + "_FREQ", clkSymPeripheral)
    gclkSym_PCHCTRL_FREQ.setLabel("Peripheral Channel " + str(index) + " Frequency ")
    gclkSym_PCHCTRL_FREQ.setReadOnly(True)
    gclkSym_PCHCTRL_FREQ.setDependencies(setPCHCTRLFREQVisibleProperty, [key + "_CHEN",key + "_GENSEL", "GCLK_0_FREQ", "GCLK_1_FREQ", "GCLK_2_FREQ", "GCLK_3_FREQ", "GCLK_4_FREQ",
                                                                                    "GCLK_5_FREQ", "GCLK_6_FREQ", "GCLK_7_FREQ", "GCLK_8_FREQ"])
    triggerdepList.append(key + "_FREQ")
    #GCLK Peripheral Channel Lock
    gclkSym_PCHCTRL_WRTLOCK = coreComponent.createBooleanSymbol(key + "_WRITELOCK", clkSymPeripheral)
    gclkSym_PCHCTRL_WRTLOCK.setLabel("Write Lock")

peripheralList = []
for value in indexSymbolMap.values():
    for i in range (0,len(value)):
        peripheralList.append(value[i])

peripheralList.sort()

for name in peripheralList:
    #GCLK Peripheral Channel Enable
    clkSymExtPeripheral = coreComponent.createBooleanSymbol(name + "_CLOCK_ENABLE", peripheralClockMenu)
    clkSymExtPeripheral.setLabel(name + " Clock Enable")
    clkSymExtPeripheral.setDefaultValue(False)
    triggerdepList.append(name + "_CLOCK_ENABLE")

    clkSymExtPeripheral = coreComponent.createIntegerSymbol(name + "_CLOCK_FREQUENCY", clkSymExtPeripheral)
    clkSymExtPeripheral.setLabel(name + " Clock Frequency")
    clkSymExtPeripheral.setReadOnly(True)
    gclkDependencyList.append(name + "_CLOCK_ENABLE")

pacEnable = coreComponent.createBooleanSymbol("PAC_CLOCK_ENABLE", peripheralClockMenu)
pacEnable.setLabel("PAC Clock Enable")
pacEnable.setDefaultValue(False)
gclkDependencyList.append("PAC_CLOCK_ENABLE")

clockTrigger = coreComponent.createBooleanSymbol("TRIGGER_LOGIC", None)
clockTrigger.setVisible(False)
clockTrigger.setDependencies(clkSetup, triggerdepList)

gclkSym_PeriIdMax = coreComponent.createIntegerSymbol("GCLK_MAX_ID", clkSymPeripheral)
gclkSym_PeriIdMax.setVisible(False)
gclkSym_PeriIdMax.setDefaultValue(int(maxGCLKId))

clkInitList = coreComponent.createListSymbol("CLK_INIT_LIST", None)

codeGenerationList = coreComponent.createListEntrySymbol("GCLK_CODE", None)
codeGenerationList.setVisible(False)
codeGenerationDep.append("GCLK_ID_0_GENSEL")
codeGenerationDep.append("GCLK_ID_1_GENSEL")
codeGenerationDep.append("CONFIG_CLOCK_DPLL_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_DPLL_ENABLE")
codeGenerationDep.append("CONFIG_CLOCK_DFLL_ENABLE")
codeGenerationList.setDependencies(codeGen, codeGenerationDep)
codeGenerationList.addValue("    GCLK0_Initialize();")
codeGenerationList.setTarget("core.CLK_INIT_LIST")

##############################PM Callback######################################
def setMainClockFreq(symbol, event):
    divider = int(Database.getSymbolValue("core","CONF_CPU_CLOCK_DIVIDER"))
    gclk0_freq = int(Database.getSymbolValue("core","GCLK_0_FREQ"))

    symbol.setValue(gclk0_freq / (1 << divider), 1)
    if (gclk0_freq > 19000000 and gclk0_freq < 38000000):
        Database.setSymbolValue("core", "NVM_RWS", "NVMCTRL_CTRLB_RWS_HALF_Val", 2)
    elif (gclk0_freq >= 38000000):
        Database.setSymbolValue("core", "NVM_RWS", "NVMCTRL_CTRLB_RWS_DUAL_Val", 2)
    else:
        Database.setSymbolValue("core", "NVM_RWS", "NVMCTRL_CTRLB_RWS_SINGLE_Val", 2)

def ahbValue(symbol,event):
    global ahbInit
    global pmDic

    perInstance = event["id"].split("_CLOCK_ENABLE")[0]
    if perInstance == "CAN0" or perInstance == "CAN1":
        for key in pmDic.keys():
            if pmDic.get(key) == perInstance:
                if key.startswith("AHB_"):
                    bitmask =  int(key.split("AHB_")[1])
                    ahbVal = int(symbol.getValue(),16)
                    if event["value"] == True:
                        ahbVal =  ahbVal | bitmask
                        symbol.setValue(hex(ahbVal),2)
                        break
                    else:
                        ahbVal =  ahbVal & ~(bitmask)
                        symbol.setValue(hex(ahbVal),2)
                        break


def apbValue(symbol,event):
    global apbInit
    global pmDic
    enable = event["value"]
    perInstance = event["id"].split("_CLOCK_ENABLE")[0]
    if "_CORE" in perInstance:
        perInstance = perInstance.split("_CORE")[0]

    if "_ANA" in perInstance:
        perInstance = perInstance.split("_ANA")[0]

    if "_SLOW" in perInstance:
        return

    if "_DIG" in perInstance:
        return

    if "PAC" in perInstance:
        perInstance = "PAC2"

    if "EVSYS" in perInstance:
        perInstance = perInstance.split("_")[0]
        for i in range (0,12):
            if Database.getSymbolValue("core", "EVSYS_" + str(i) + "_CLOCK_ENABLE") == True:
                enable = enable | True
                break



    for key in pmDic.keys():
        if pmDic.get(key) == perInstance:
            if key.startswith("APB"):
                bridge = key.split("_")[0]

                bitmask = int(key.split("_")[1])
                apbVal = int(Database.getSymbolValue("core", "PM_" + bridge + "_INITIAL_VALUE"),16)
                if enable == True:
                    apbVal =  apbVal | bitmask
                    Database.setSymbolValue("core", "PM_" + bridge + "_INITIAL_VALUE", hex(apbVal),2)
                    break
                else:
                    apbVal =  apbVal & ~(bitmask)
                    Database.setSymbolValue("core", "PM_" + bridge + "_INITIAL_VALUE", hex(apbVal),2)
                    break

###############################PM###############################################
global ahbInit
numAPB = 0
ahbInit = 0x0
global pmDic
pmDic = {}
global apbInit

ahbNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/register-group")
for index in range(0, len(ahbNode.getChildren())):
    if ahbNode.getChildren()[index].getAttribute("name") == "AHBMASK":
        ahbInit = hex(int(ahbNode.getChildren()[index].getAttribute("initval"),16))

#AHB Bridge Clock Initial Settings
pm_AHB_Clock_Value = coreComponent.createStringSymbol("PM_AHB_INITIAL_VALUE",pmSym_Menu)
pm_AHB_Clock_Value.setDefaultValue(str(ahbInit))
pm_AHB_Clock_Value.setDependencies(ahbValue, gclkDependencyList)
pm_AHB_Clock_Value.setVisible(False)

ahbMaskNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PM"]/register-group@[name="PM"]/register@[name="AHBMASK"]')
ahbMaskValues = ahbMaskNode.getChildren()
for index in range(0, len(ahbMaskValues)):
    pmDic["AHB_" + str(int(ahbMaskValues[index].getAttribute("mask"),16))] = ahbMaskValues[index].getAttribute("name").split("_")[0]
    if ahbMaskValues[index].getAttribute("name").startswith("HPB"):
        numAPB = numAPB + 1

bridges = ["APBA", "APBB", "APBC", "APBD"]
apbInit = {"APBA" : "",
           "APBB" : "",
           "APBC" : "",
           "APBD" : ""
           }

for index in range(0, numAPB):
    bridgeName = "PM_" + bridges[index] + "SEL__" + bridges[index]
    path = "/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"" + bridgeName + "DIV\"]"
    apbDivNode = ATDF.getNode(path)
    apbDivValues = apbDivNode.getChildren()

    pmAPBDiv = coreComponent.createKeyValueSetSymbol("PM_" + bridges[index] +"_DIV", pmSym_Menu)
    pmAPBDiv.setLabel(bridges[index] + " Divider")
    for i in range(0, len(apbDivValues)):
        key = apbDivValues[i].getAttribute("name")
        value = apbDivValues[i].getAttribute("value")
        caption = apbDivValues[i].getAttribute("caption")
        pmAPBDiv.addKey(key, value, caption)

    pmAPBDiv.setOutputMode("Value")
    pmAPBDiv.setDisplayMode("Key")
    pmAPBDiv.setDefaultValue(0)


for index in range(0, numAPB):
    bridgeName = bridges[index]
    path = "/avr-tools-device-file/modules/module@[name=\"PM\"]/register-group@[name=\"PM\"]/register@[name=\"" + bridgeName + "MASK\"]"
    apbNode = ATDF.getNode(path)
    apbValues = apbNode.getChildren()
    for bitpos in range(0, len(apbValues)):
        pmDic[bridgeName + "_" + str(int(apbValues[bitpos].getAttribute("mask"),16))] = apbValues[bitpos].getAttribute("name").split("_")[0]

    apbInitNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/register-group")
    for index in range(0, len(apbInitNode.getChildren())):
        if apbInitNode.getChildren()[index].getAttribute("name") == (bridgeName + "MASK"):
            apbInit[bridgeName] = hex(int(apbInitNode.getChildren()[index].getAttribute("initval"),16))

    #APB Bridge Clock Initial Settings
    pm_Clock_Value = coreComponent.createStringSymbol("PM_" + bridgeName +"_INITIAL_VALUE",pmSym_Menu)
    pm_Clock_Value.setDefaultValue(str(apbInit[bridgeName]))
    pm_Clock_Value.setVisible(False)

pm_Clock_Value.setDependencies(apbValue, gclkDependencyList)

#MCLK CPU Division
pmSym_CPUDIV_CPUDIV = coreComponent.createKeyValueSetSymbol("CONF_CPU_CLOCK_DIVIDER",pmSym_Menu)
pmSym_CPUDIV_CPUDIV.setLabel("CPU Clock Division Factor")
pmcpudivNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PM\"]/value-group@[name=\"PM_CPUSEL__CPUDIV\"]")
pmcpudivNodeValues = []
pmcpudivNodeValues = pmcpudivNode.getChildren()
pmcpudivDefaultValue = 0

for index in range(0, len(pmcpudivNodeValues)):
    pmcpudivKeyName= pmcpudivNodeValues[index].getAttribute("name")

    if (pmcpudivKeyName == "DIV1"):
        pmcpudivDefaultValue = index

    pmcpudivKeyDescription = pmcpudivNodeValues[index].getAttribute("caption")
    pmcpudivKeyValue = pmcpudivNodeValues[index].getAttribute("value")
    pmSym_CPUDIV_CPUDIV.addKey(pmcpudivKeyName, pmcpudivKeyValue , pmcpudivKeyDescription)

pmSym_CPUDIV_CPUDIV.setDefaultValue(pmcpudivDefaultValue)
pmSym_CPUDIV_CPUDIV.setOutputMode("Value")
pmSym_CPUDIV_CPUDIV.setDisplayMode("Key")

# Flash Read Wait State (RWS). Values given in  'NVM Characteristics'
nvm_rws = coreComponent.createStringSymbol("NVM_RWS", pmSym_Menu)
nvm_rws.setReadOnly(True)
nvm_rws.setDefaultValue("NVMCTRL_CTRLB_RWS_SINGLE_Val")
nvm_rws.setVisible(False)

clkSym_MAIN_CLK_FREQ = coreComponent.createIntegerSymbol("CPU_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_MAIN_CLK_FREQ.setLabel("Main Clock Frequency")
clkSym_MAIN_CLK_FREQ.setReadOnly(True)
clkSym_MAIN_CLK_FREQ.setDependencies(setMainClockFreq, ["GCLK_0_FREQ", "CONF_CPU_CLOCK_DIVIDER"])

divider = pmSym_CPUDIV_CPUDIV.getValue()
gclk0_freq = int(gclkSym_Freq[0].getValue())
clkSym_MAIN_CLK_FREQ.setValue(gclk0_freq / (divider + 1), 1)


#####################Default clock Setup####################################
#Enable DFLL
dfllEnable.setValue(True, 1)

#Select DFLL as default clock source
gclkSym_GENCTRL_SRC[0].setValue(7, 1)

#Disable RC oscillator
osc8MEnable.setValue(False, 1)

################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clockSym_OSCCTRL_HeaderFile = coreComponent.createFileSymbol("SAMD21_CLOCK_HEADER", None)
clockSym_OSCCTRL_HeaderFile.setSourcePath("../peripheral/clk_sam_d21/templates/plib_clock.h.ftl")
clockSym_OSCCTRL_HeaderFile.setOutputName("plib_clock.h")
clockSym_OSCCTRL_HeaderFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setType("HEADER")
clockSym_OSCCTRL_HeaderFile.setMarkup(True)

clockSym_OSCCTRL_SourceFile = coreComponent.createFileSymbol("SAMD21_CLOCK_SOURCE", None)
clockSym_OSCCTRL_SourceFile.setSourcePath("../peripheral/clk_sam_d21/templates/plib_clock.c.ftl")
clockSym_OSCCTRL_SourceFile.setOutputName("plib_clock.c")
clockSym_OSCCTRL_SourceFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setType("SOURCE")
clockSym_OSCCTRL_SourceFile.setMarkup(True)

clockSystemInitFile = coreComponent.createFileSymbol("SAMD21_CLOCK_INIT", None)
clockSystemInitFile.setType("STRING")
clockSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clockSystemInitFile.setSourcePath("../peripheral/clk_sam_d21/templates/system/initialization.c.ftl")
clockSystemInitFile.setMarkup(True)

clockSystemDefFile = coreComponent.createFileSymbol("SAMD21_CLOCK_SYS_DEF", None)
clockSystemDefFile.setType("STRING")
clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clockSystemDefFile.setSourcePath("../peripheral/clk_sam_d21/templates/system/definitions.h.ftl")
clockSystemDefFile.setMarkup(True)
