
# coding: utf-8
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

Log.writeInfoMessage("Loading Clock Manager for " + Variables.get("__PROCESSOR"))

from os.path import join
from xml.etree import ElementTree
from collections import defaultdict
global topsort
clkMenu = coreComponent.createMenuSymbol("SAML10_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")

# Clock Source Configuration
clkSourceMenu = coreComponent.createMenuSymbol("CLOCK_SOURCE", clkMenu)
clkSourceMenu.setLabel("Clock Source Configuration")

oscctrlosc16_Menu = coreComponent.createMenuSymbol("OSC16_MENU", clkSourceMenu)
oscctrlosc16_Menu.setLabel("16MHz Internal Oscillator Configuration")

oscctrlXosc_Menu = coreComponent.createMenuSymbol("XOSCCTRL_MENU", clkSourceMenu)
oscctrlXosc_Menu.setLabel("External Crystal Oscillator Configuration")

dfll_Menu = coreComponent.createMenuSymbol("DFLL MENU", clkSourceMenu)
dfll_Menu.setLabel("DFLL Configuration")

dpll96_Menu = coreComponent.createMenuSymbol("DPLL96M_MENU", clkSourceMenu)
dpll96_Menu.setLabel("96MHz Fractional DPLL (FDPLL96M) Configuration")

xosc32k_Menu = coreComponent.createMenuSymbol("XOSC32K_MENU", clkSourceMenu)
xosc32k_Menu.setLabel("32Khz External Oscillator Configuration")

# Clock Generator Configuration
clkGen_Menu = coreComponent.createMenuSymbol("GCLK_MENU", clkMenu)
clkGen_Menu.setLabel("Generic Clock Configuration")

gclkGen_Menu = coreComponent.createMenuSymbol("GCLK_GEN_MENU", clkGen_Menu)
gclkGen_Menu.setLabel("Generator Configuration")

gclkPeriChannel_menu = coreComponent.createMenuSymbol("GCLK_PERI_MENU",clkGen_Menu)
gclkPeriChannel_menu.setLabel("Peripheral Channel Configuration")

# Main Clock Configuration
mclkSym_Menu = coreComponent.createMenuSymbol("MCLK_MENU", clkMenu)
mclkSym_Menu.setLabel("Main Clock Configuration")

# Peripheral Clock Configuration
peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLOCK_MENU", clkMenu)
peripheralClockMenu.setLabel("Peripheral Clock Configuration")

# Calculated Frequency Menu
calculatedFreq_Menu = coreComponent.createMenuSymbol("FREQ_MENU", clkMenu)
calculatedFreq_Menu.setLabel("Calculated Clock Frequencies")

#################################################################################################
################################################################################
##########              Callback Functions            ##########################
################################################################################
################################################################################

####    XOSC Configuration callback functions    ###############################

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


def setXOSCFreq(symbol, event):

    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_XOSC_ENABLE")

    if enable:
        symbol.setValue(Database.getSymbolValue("core", "CONFIG_CLOCK_XOSC_FREQUENCY"), 1)
    else:
        symbol.setValue(0, 1)

####    OSC16M Configuration Callback Functions    #############################



def setOsc16MFreq(symbol, event):
    global osc16MFreqSel
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_OSC16M_ENABLE")

    if enable:
        freq = int(osc16MFreqSel.getSelectedKey().split("MHz")[0]) * 1000000
        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def setDfllFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")
    freq = 0
    if enable:
        mul = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_RATIO"))
        refFreq = int(Database.getSymbolValue("core", "GCLK_ID_2_FREQ"))
        div = 1 << int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_DIV"))
        freq = (mul * refFreq)/div

    prevFreq = symbol.getValue()

    if prevFreq != freq:
        symbol.setValue(freq, 2)

####    DPLL Configuration Callback Functions    ###############################

def setDPLL96MClockFreq(symbol, event):

    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")

    if enable:
        clockSrc = Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_REF_CLOCK")

        # XOSC32K Clock
        if clockSrc == 0:
            srcFreq = Database.getSymbolValue("core", "XOSC32K_FREQ")

        # XOSC Clock
        elif clockSrc == 1:
            divisor = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_DIVIDER"))
            srcFreq = int(Database.getSymbolValue("core", "XOSC_FREQ")) / (2 * (divisor + 1))

        # GCLK_DPLL Clock
        elif clockSrc == 2:
            srcFreq = int(Database.getSymbolValue("core","GCLK_ID_0_FREQ"))

        else:
            return

        ldr = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDR_INTEGER"))
        ldrFrac = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION"))
        prescalar = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_PRESCALAR"))

        dpllFreq = int(srcFreq * (ldr + 1.0 + (ldrFrac/16.0)) * (1.0 / float(2**prescalar)))

        if symbol.getValue() != dpllFreq:
            symbol.setValue(dpllFreq, 1)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0, 1)


def calcDpllMultiplier(symbol, event):
    ldr = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDR_INTEGER"))
    ldrFrac = int(Database.getSymbolValue("core","CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION"))
    multiplier = (ldr + 1.0 + (ldrFrac/16.0))
    if symbol.getValue() != multiplier:
        symbol.setValue(multiplier,2)

def calcDpllXoscDivider(symbol, event):
    divisor = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_DIVIDER"))
    div_value = (2 * (divisor + 1))
    if symbol.getValue() != div_value:
        symbol.setValue(div_value,2)

def interruptControl(symbol, event):
    if event["id"] == "CONFIG_CLOCK_XOSC_CFDEN":
        moduleInterruptName = "OSCCTRL"
    elif event["id"] == "XOSC32K_CFDEN":
        moduleInterruptName = "OSC32KCTRL"
    elif event["id"] == "MCLK_INTENSET_CKRDY":
        moduleInterruptName = "MCLK"

    InterruptVector = moduleInterruptName + "_INTERRUPT_ENABLE"
    InterruptHandler = moduleInterruptName + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = moduleInterruptName + "_INTERRUPT_HANDLER_LOCK"

    if (event["value"] == True):
        Database.setSymbolValue("core", InterruptVector, True)
        Database.setSymbolValue("core", InterruptHandler, moduleInterruptName + "_InterruptHandler")
        Database.setSymbolValue("core", InterruptHandlerLock, True)
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            Database.setSymbolValue("core", moduleInterruptName + "_SET_NON_SECURE", False)
    else :
        Database.setSymbolValue("core", InterruptVector, False)
        Database.setSymbolValue("core", InterruptHandler, moduleInterruptName + "_Handler")
        Database.setSymbolValue("core", InterruptHandlerLock, False)

################################################################################
#######          OSCCTRL Database Components      ##############################
################################################################################
############################   OSC16M Components  ##############################
global osc16MFreqSel

osc16MEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC16M_ENABLE", oscctrlosc16_Menu)
osc16MEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
osc16MEnable.setLabel("Enable 16MHz RC Oscillator")
osc16MEnable.setDescription("Enable 16MHz RC Oscillator")
osc16MEnable.setDefaultValue(True)

osc16MFreqSel = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC16M_FREQSEL", oscctrlosc16_Menu)
osc16MFreqSel.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:OSC16MCTRL")
osc16MFreqSel.setLabel("Oscillator 16M Output Frequency")
osc16MFreqSel.setDescription("Oscillator 16M Output Frequency ")
osc16MFreqSelNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_OSC16MCTRL__FSEL\"]")
osc16MFreqSelValues = []
osc16MFreqSelValues = osc16MFreqSelNode.getChildren()
for index in range(0, len(osc16MFreqSelValues)):
    osc16MFreqSelKeyName = osc16MFreqSelValues[index].getAttribute("name")
    osc16MFreqSelKeyDescription = osc16MFreqSelValues[index].getAttribute("caption")
    osc16MFreqSelKeyValue = osc16MFreqSelValues[index].getAttribute("value")
    osc16MFreqSel.addKey(osc16MFreqSelKeyName, osc16MFreqSelKeyValue , osc16MFreqSelKeyDescription)

osc16MFreqSel.setDefaultValue(0)
osc16MFreqSel.setOutputMode("Value")
osc16MFreqSel.setDisplayMode("Description")

osc16MOnDemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_OSC16M_ONDEMAND", oscctrlosc16_Menu)
osc16MOnDemand.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:OSC16MCTRL")
osc16MOnDemand.setLabel("Oscillator On-Demand Control")
osc16MOnDemand.setDescription("Configures the OSC16M on Demand Behavior")
osc16MOnDemand.setOutputMode("Key")
osc16MOnDemand.setDisplayMode("Description")
osc16MOnDemand.addKey("DISABLE",str(0),"Always Enable")
osc16MOnDemand.addKey("ENABLE",str(1),"Only on Peripheral Request")
osc16MOnDemand.setDefaultValue(0)

osc16MRunStdby = coreComponent.createBooleanSymbol("CONFIG_CLOCK_OSC16M_RUNSTDBY", oscctrlosc16_Menu)
osc16MRunStdby.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:OSC16MCTRL")
osc16MRunStdby.setLabel("Run Oscillator in Standby Sleep Mode")
osc16MRunStdby.setDescription("OSC16M RunIn StandBy mode configuration")
osc16MRunStdby.setDefaultValue(False)

osc16MFreq = coreComponent.createIntegerSymbol("OSC16M_FREQ", calculatedFreq_Menu)
osc16MFreq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:OSC16MCTRL")
osc16MFreq.setLabel("OSC16M Clock Frequency")
osc16MFreq.setReadOnly(True)
osc16MFreq.setDefaultValue(4000000)
osc16MFreq.setDependencies(setOsc16MFreq, ["CONFIG_CLOCK_OSC16M_ENABLE", "CONFIG_CLOCK_OSC16M_FREQSEL"])
############################   XOSC Components    ##############################
#XOSC Oscillator Enable
oscctrlSym_XOSC_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_ENABLE", oscctrlXosc_Menu)
oscctrlSym_XOSC_CONFIG_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
oscctrlSym_XOSC_CONFIG_ENABLE.setLabel("External Multipurpose Crystal Oscillator(XOSC) Enable")
oscctrlSym_XOSC_CONFIG_ENABLE.setDescription("External Crystal Oscillator Enable Feature")
oscctrlSym_XOSC_CONFIG_ENABLE.setDefaultValue(False)

#XOSC Automatic Gain Control Mode
oscctrlSym_XOSC_AMPGC = coreComponent.createBooleanSymbol("XOSC_AMPGC", oscctrlXosc_Menu)
oscctrlSym_XOSC_AMPGC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
oscctrlSym_XOSC_AMPGC.setLabel("Automatic Gain Control ")
oscctrlSym_XOSC_AMPGC.setDefaultValue(False)

#XOSC Oscillator Mode
oscctrlSym_XOSC_OSCILLATORMODE = coreComponent.createKeyValueSetSymbol("XOSC_OSCILLATOR_MODE", oscctrlXosc_Menu)
oscctrlSym_XOSC_OSCILLATORMODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSC_OSCILLATORMODE.setLabel("External Oscillator Mode ")
oscctrlSym_XOSC_OSCILLATORMODE.addKey("EXTERNAL_CLOCK","0","xosc external clock enable")
oscctrlSym_XOSC_OSCILLATORMODE.addKey("CRYSTAL","1","crystal oscillator enable")
oscctrlSym_XOSC_OSCILLATORMODE.setOutputMode("Value")
oscctrlSym_XOSC_OSCILLATORMODE.setDefaultValue(1)

#XOSC Oscillator Frequency
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_FREQUENCY", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setLabel("Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDescription("Setting the XOSC Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDefaultValue(12000000)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setMax(32000000)

#XOSC Oscillator Gain
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN = coreComponent.createIntegerSymbol("CONFIG_CLOCK_XOSC_GAIN", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setLabel("Gain")
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setDefaultValue(2)
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setDescription("Setting the XOSC Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setVisible(False)
oscctrlSym_XOSCCTRL_OSCILLATOR_GAIN.setDependencies(setXOSCOscillatorGAINVisibleProperty, ["CONFIG_CLOCK_XOSC_FREQUENCY"])

#XOSC Oscillator ONDEMAND Mode
oscctrlSym_XOSCCTRL_ONDEMAND = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_ONDEMAND", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSCCTRL_ONDEMAND.setLabel("Oscillator On-Demand Control")
oscctrlSym_XOSCCTRL_ONDEMAND.setDescription("Configures the XOSC on Demand Behavior")
oscctrlSym_XOSCCTRL_ONDEMAND.setOutputMode("Key")
oscctrlSym_XOSCCTRL_ONDEMAND.setDisplayMode("Description")
oscctrlSym_XOSCCTRL_ONDEMAND.addKey("DISABLE",str(0),"Always Enable")
oscctrlSym_XOSCCTRL_ONDEMAND.addKey("ENABLE",str(1),"Only on Peripheral Request")
oscctrlSym_XOSCCTRL_ONDEMAND.setDefaultValue(0)

#XOSC Oscillator Startup Time
oscctrlSym_XOSCCTRL_STARTUP = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_STARTUP",oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_STARTUP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSCCTRL_STARTUP.setLabel("Oscillator Startup Time")
oscctrlSym_XOSCCTRL_STARTUP.setDescription("Startup time for the XOSC ")
oscctrlSymXOSCStartupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_XOSCCTRL__STARTUP\"]")
oscctrlSymXOSCStartupValues = []
oscctrlSymXOSCStartupValues = oscctrlSymXOSCStartupNode.getChildren()
xoscstartupDefaultValue = 0
for index in range(0, len(oscctrlSymXOSCStartupValues)):
    xoscstartupKeyName = oscctrlSymXOSCStartupValues[index].getAttribute("name")

    if (xoscstartupKeyName == "CYCLE64"):
        xoscstartupDefaultValue = index

    xoscstartupKeyDescription = oscctrlSymXOSCStartupValues[index].getAttribute("caption")
    xoscstartupKeyValue = oscctrlSymXOSCStartupValues[index].getAttribute("value")
    oscctrlSym_XOSCCTRL_STARTUP.addKey(xoscstartupKeyName, xoscstartupKeyValue , xoscstartupKeyDescription)

oscctrlSym_XOSCCTRL_STARTUP.setDefaultValue(xoscstartupDefaultValue)
oscctrlSym_XOSCCTRL_STARTUP.setOutputMode("Value")
oscctrlSym_XOSCCTRL_STARTUP.setDisplayMode("Description")


#XOSC Oscillator Run StandBy Control
oscctrlSym_XOSCCTRL_RUNSTDBY = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_RUNSTDBY", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSCCTRL_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")
oscctrlSym_XOSCCTRL_RUNSTDBY.setDescription("External oscillator RunIn StandBy mode or not")
oscctrlSym_XOSCCTRL_RUNSTDBY.setDefaultValue(False)


#XOSC Oscillator Clock Failure Detector(CFD) Enable
oscctrlSym_XOSCCTRL_CFDEN = coreComponent.createBooleanSymbol("CONFIG_CLOCK_XOSC_CFDEN", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_CFDEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSCCTRL")
oscctrlSym_XOSCCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
oscctrlSym_XOSCCTRL_CFDEN.setDescription("Clock Failure Detection enable or not")
oscctrlSym_XOSCCTRL_CFDEN.setDefaultValue(False)
oscctrlSym_XOSCCTRL_CFDEN.setDependencies(interruptControl, ["CONFIG_CLOCK_XOSC_CFDEN"])

#XOSC Oscillator Clock Failure Detector(CFD) Pre-Scalar
oscctrlSym_CFDPRESC_CFDPRESC = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_XOSC_CFDPRESC",oscctrlSym_XOSCCTRL_CFDEN)
oscctrlSym_CFDPRESC_CFDPRESC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:CFDPRESC")
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

clkSym_XOSC_Freq = coreComponent.createIntegerSymbol("XOSC_FREQ", calculatedFreq_Menu)
clkSym_XOSC_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_XOSC_Freq.setLabel("XOSC Clock Frequency")
clkSym_XOSC_Freq.setReadOnly(True)
clkSym_XOSC_Freq.setDependencies(setXOSCFreq, ["CONFIG_CLOCK_XOSC_ENABLE", "CONFIG_CLOCK_XOSC_FREQUENCY"])

##############################################DFLL####################################################

dfllEnable = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_ENABLE", dfll_Menu)
dfllEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
dfllEnable.setLabel("Enable DFLL")
dfllEnable.setDescription("Enable DFLL")
dfllEnable.setDefaultValue(False)

dfllOndemand = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_ONDEMAND", dfll_Menu)
dfllOndemand.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
dfllOndemand.setLabel("DFLL On-Demand Control")
dfllOndemand.setDescription("Configures the DFLL on Demand Behavior")
dfllOndemand.setOutputMode("Value")
dfllOndemand.setDisplayMode("Description")
dfllOndemand.addKey("Disable", str(0), "Always Enable")
dfllOndemand.addKey("Enable", str(1), "Only on Peripheral Request")
dfllOndemand.setDefaultValue(0)

dfllRunstdy = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_RUNSTDY", dfll_Menu)
dfllRunstdy.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPCTRL")
dfllRunstdy.setLabel("Run DFLL in Standby Sleep Mode")
dfllRunstdy.setDescription("DFLL to run in standby mode or not")
dfllRunstdy.setDefaultValue(False)

dfllDither = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_DITHER", dfll_Menu)
dfllDither.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPDITHER")
dfllDither.setLabel("Enable Tuner Dithering")
dfllDither.setDescription("Enable or Disable Tuner Dithering")
dfllDither.setDefaultValue(False)

dfllSafe = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_SAFE", dfll_Menu)
dfllSafe.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPCTRL")
dfllSafe.setLabel("Wait for DFLL Tuner to Lock")
dfllSafe.setDescription("Controls the DFLL output clock, depending on lock status")
dfllSafe.setDefaultValue(False)

dfllBinse = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DFLL_BINSE", dfll_Menu)
dfllBinse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPCTRL")
dfllBinse.setLabel("Enable Binary Search")
dfllBinse.setDescription("Maximum number of reference clock cycles to acquire lock is 8 or 256")
dfllBinse.setDefaultValue(False)

dfllDitherPer = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_DITHER_PERIOD", dfll_Menu)
dfllDitherPer.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPDITHER")
dfllDitherPer.setLabel("Dither Period")
dfllDitherPer.setDescription("Number of reference clock periods over which dithering is applied")

dfllDitherPerNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DFLLULPDITHER__PER\"]")
dfllDitherPerNodeValues = []
dfllDitherPerNodeValues = dfllDitherPerNode.getChildren()
for index in range(0, len(dfllDitherPerNodeValues)):
    dfllDitherPerKeyName = dfllDitherPerNodeValues[index].getAttribute("name")
    dfllDitherPerKeyDescription = dfllDitherPerNodeValues[index].getAttribute("caption")
    dfllDitherPerKeyValue= dfllDitherPerNodeValues[index].getAttribute("value")
    dfllDitherPer.addKey(dfllDitherPerKeyName, dfllDitherPerKeyValue , dfllDitherPerKeyDescription)

dfllDitherPer.setDefaultValue(0)
dfllDitherPer.setOutputMode("Value")
dfllDitherPer.setDisplayMode("Description")


dfllRatio = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DFLL_RATIO", dfll_Menu)
dfllRatio.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPRATIO")
dfllRatio.setDefaultValue(1)
dfllRatio.setMin(0)
dfllRatio.setMax(1024)
dfllRatio.setLabel("Target Tuner Ratio")

dfllDitherStep = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_DITHER_STEP", dfll_Menu)
dfllDitherStep.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPDITHER")
dfllDitherStep.setLabel("Dither Step")
dfllDitherStep.setDescription("The dithering step size")

dfllDitherStepNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DFLLULPDITHER__STEP\"]")
dfllDitherStepNodeValues = []
dfllDitherStepNodeValues = dfllDitherStepNode.getChildren()
for index in range(0, len(dfllDitherStepNodeValues)):
    dfllDitherStepKeyName = dfllDitherStepNodeValues[index].getAttribute("name")
    dfllDitherStepKeyDescription = dfllDitherStepNodeValues[index].getAttribute("caption")
    dfllDitherStepKeyValue= dfllDitherStepNodeValues[index].getAttribute("value")
    dfllDitherStep.addKey(dfllDitherStepKeyName, dfllDitherStepKeyValue , dfllDitherStepKeyDescription)

dfllDitherStep.setDefaultValue(0)
dfllDitherStep.setOutputMode("Value")
dfllDitherStep.setDisplayMode("Description")

dfllDiv = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DFLL_DIV", dfll_Menu)
dfllDiv.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DFLLULPCTRL")
dfllDiv.setLabel("DFLL Output divider")
dfllDiv.setDescription("DFLL Output divider")

dfllDivNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"OSCCTRL_DFLLULPCTRL__DIV\"]")
dfllDivNodeValues = []
dfllDivNodeValues = dfllDivNode.getChildren()
for index in range(0, len(dfllDivNodeValues)):
    dfllDivKeyName = dfllDivNodeValues[index].getAttribute("name")
    dfllDivKeyDescription = dfllDivNodeValues[index].getAttribute("caption")
    dfllDivKeyValue= dfllDivNodeValues[index].getAttribute("value")
    dfllDiv.addKey(dfllDivKeyName, dfllDivKeyValue , dfllDivKeyDescription)

dfllDiv.setDefaultValue(0)
dfllDiv.setOutputMode("Value")
dfllDiv.setDisplayMode("Description")

dfllFreq = coreComponent.createIntegerSymbol("DFLL_CLOCK_FREQ", calculatedFreq_Menu)
dfllFreq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
dfllFreq.setReadOnly(True)
dfllFreq.setDefaultValue(0)
dfllFreq.setLabel("DFLL Clock Frequency")
dfllFreq.setDependencies(setDfllFreq, ["CONFIG_CLOCK_DFLL_ENABLE",
                                       "CONFIG_CLOCK_DFLL_RATIO",
                                       "CONFIG_CLOCK_DFLL_DIV",
                                       "GCLK_ID_2_FREQ"])
############################   DPLL Components    ############################
#Digital Phase Locked Loop(DPLL) Enable
oscctrlSym_DPLL_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_ENABLE", dpll96_Menu)
oscctrlSym_DPLL_CONFIG_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
oscctrlSym_DPLL_CONFIG_ENABLE.setLabel("Digital Phase Locked Loop(DPLL) Enable ")
oscctrlSym_DPLL_CONFIG_ENABLE.setDescription("DPLL Configuration enabling feature")
oscctrlSym_DPLL_CONFIG_ENABLE.setDefaultValue(False)

#Digital Phase Locked Loop(DPLL) ONDEMAND Mode
oscctrlSym_DPLLCTRLA_ONDEMAND = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_ONDEMAND", dpll96_Menu)
oscctrlSym_DPLLCTRLA_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLA")
oscctrlSym_DPLLCTRLA_ONDEMAND.setLabel("DPLL On-Demand Control")
oscctrlSym_DPLLCTRLA_ONDEMAND.setDescription("Configures the DPLL on Demand Behavior")
oscctrlSym_DPLLCTRLA_ONDEMAND.setOutputMode("Value")
oscctrlSym_DPLLCTRLA_ONDEMAND.setDisplayMode("Description")
oscctrlSym_DPLLCTRLA_ONDEMAND.addKey("Disable",str(0),"Always Enable")
oscctrlSym_DPLLCTRLA_ONDEMAND.addKey("Enable",str(1),"Only on Peripheral Request")
oscctrlSym_DPLLCTRLA_ONDEMAND.setDefaultValue(0)

#Digital Phase Locked Loop(DPLL) Run StandBy Control
oscctrlSym_DPLLCTRLA_RUNSTDBY = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_RUNSTDY", dpll96_Menu)
oscctrlSym_DPLLCTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLA")
oscctrlSym_DPLLCTRLA_RUNSTDBY.setLabel("Run DPLL in Standby Sleep Mode")
oscctrlSym_DPLLCTRLA_RUNSTDBY.setDescription("DPLL to run in standby mode or not")
oscctrlSym_DPLLCTRLA_RUNSTDBY.setDefaultValue(False)

#Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Integer part
oscctrlSym_DPLLRATIO_LDR = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDR_INTEGER", dpll96_Menu)
oscctrlSym_DPLLRATIO_LDR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLRATIO")
oscctrlSym_DPLLRATIO_LDR.setLabel("DPLL Loop Divider Ratio Integer Part")
oscctrlSym_DPLLRATIO_LDR.setDescription("Loop divider ratio integer value")
oscctrlSym_DPLLRATIO_LDR.setDefaultValue(0)
oscctrlSym_DPLLRATIO_LDR.setMin(0)
oscctrlSym_DPLLRATIO_LDR.setMax(4095)

#Digital Phase Locked Loop(DPLL) Loop Divider Ration(LDR) Fraction part
oscctrlSym_DPLLRATIO_LDRFRAC = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION", dpll96_Menu)
oscctrlSym_DPLLRATIO_LDRFRAC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLRATIO")
oscctrlSym_DPLLRATIO_LDRFRAC.setLabel("DPLL Loop Divider Ratio Fractional Part")
oscctrlSym_DPLLRATIO_LDRFRAC.setDescription("loop divider ratio fraction value")
oscctrlSym_DPLLRATIO_LDRFRAC.setDefaultValue(0)
oscctrlSym_DPLLRATIO_LDRFRAC.setMin(0)
oscctrlSym_DPLLRATIO_LDRFRAC.setMax(15)

# DPLL Multiplier value to show in the UI
oscctrlSym_DPLL_MULTIPLIER_VALUE = coreComponent.createFloatSymbol("CONFIG_CLOCK_DPLL_MULTIPLIER_VALUE", dpll96_Menu)
oscctrlSym_DPLL_MULTIPLIER_VALUE.setVisible(False)
oscctrlSym_DPLL_MULTIPLIER_VALUE.setDefaultValue(1)
oscctrlSym_DPLL_MULTIPLIER_VALUE.setDependencies(calcDpllMultiplier,["CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION","CONFIG_CLOCK_DPLL_LDR_INTEGER"])

#Digital Phase Locked Loop(DPLL) Pre-Scalar
oscctrlSym_DPLLPRESC_PRESC = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_PRESCALAR", dpll96_Menu)
oscctrlSym_DPLLPRESC_PRESC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLPRESC")
oscctrlSym_DPLLPRESC_PRESC.setLabel("DPLL Output Pre-Scalar")
oscctrlSym_DPLLPRESC_PRESC.setDescription("Selection of the DPLL Pre-Scalar value ")
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
oscctrlSym_DPLLPRESC_PRESC.setDisplayMode("Key")

#Digital Phase Locked Loop(DPLL) Lock Bypass
oscctrlSym_DPLLCTRLB_LBYPASS = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOCK_BYPASS", dpll96_Menu)
oscctrlSym_DPLLCTRLB_LBYPASS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_LBYPASS.setLabel("Bypass DPLL Lock?")
oscctrlSym_DPLLCTRLB_LBYPASS.setDescription("DPLL Lock signal is always asserted or DPLL Lock signal drives the DPLL controller internal logic.")
oscctrlSym_DPLLCTRLB_LBYPASS.setDefaultValue(False)

#Digital Phase Locked Loop(DPLL) Low Power Enable
oscctrlSym_DPLLCTRLB_LPEN = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_LOWPOWER_ENABLE", dpll96_Menu)
oscctrlSym_DPLLCTRLB_LPEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_LPEN.setLabel("DPLL Low Power Enable")
oscctrlSym_DPLLCTRLB_LPEN.setDescription("Low Power Mode Enabled or not")
oscctrlSym_DPLLCTRLB_LPEN.setDefaultValue(False)


#Digital Phase Locked Loop(DPLL) wakeUp Fast
oscctrlSym_DPLLCTRLB_WUF = coreComponent.createBooleanSymbol("CONFIG_CLOCK_DPLL_WAKEUP_FAST", dpll96_Menu)
oscctrlSym_DPLLCTRLB_WUF.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_WUF.setLabel("DPLL Fast Output Enable")
oscctrlSym_DPLLCTRLB_WUF.setDescription("DPLL clock is Output after startup and lock time or only after the startup")
oscctrlSym_DPLLCTRLB_WUF.setDefaultValue(False)

#Digital Phase Locked Loop(DPLL) Lock Time
oscctrlSym_DPLLCTRLB_LTIME = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_LOCK_TIME", dpll96_Menu)
oscctrlSym_DPLLCTRLB_LTIME.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
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


#Digital Phase Locked Loop(DPLL) Filter
oscctrlSym_DPLLCTRLB_FILTER = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_FILTER", dpll96_Menu)
oscctrlSym_DPLLCTRLB_FILTER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_FILTER.setLabel("DPLL Feedback Filter Selection")
oscctrlSym_DPLLCTRLB_FILTER.setDescription("DPLL filter type selection")
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

#Digital Phase Locked Loop(DPLL) Reference Clock
oscctrlSym_DPLLCTRLB_REFCLK = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_DPLL_REF_CLOCK", dpll96_Menu)
oscctrlSym_DPLLCTRLB_REFCLK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_REFCLK.setLabel("DPLL Reference Clock Source")
oscctrlSym_DPLLCTRLB_REFCLK.setDescription("DPLL reference clock selection")

oscctrlSym_DPLLCTRLB_REFCLK.addKey("XOSC32K", "0", "32 KHz External Crystal Oscillator")
oscctrlSym_DPLLCTRLB_REFCLK.addKey("XOSC", "1", "External Crystal Oscillator")
oscctrlSym_DPLLCTRLB_REFCLK.addKey("GCLK_DPLL", "2", "Generic Clock for FDPLL96M")

oscctrlSym_DPLLCTRLB_REFCLK.setDefaultValue(0)
oscctrlSym_DPLLCTRLB_REFCLK.setOutputMode("Value")
oscctrlSym_DPLLCTRLB_REFCLK.setDisplayMode("Key")

#Digital Phase Locked Loop(DPLL) Clock Divider
oscctrlSym_DPLLCTRLB_DIV = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_DIVIDER", oscctrlSym_DPLLCTRLB_REFCLK)
oscctrlSym_DPLLCTRLB_DIV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:DPLLCTRLB")
oscctrlSym_DPLLCTRLB_DIV.setLabel("DPLL Divider")
oscctrlSym_DPLLCTRLB_DIV.setDescription("XOSC clock division factor fdiv = (fxosc/((2*DIV)+1))")
oscctrlSym_DPLLCTRLB_DIV.setDefaultValue(0)
oscctrlSym_DPLLCTRLB_DIV.setMin(0)
oscctrlSym_DPLLCTRLB_DIV.setMax(2047)

# DPLL divider value to show in UI
oscctrlSym_DPLLCTRLB_DIV = coreComponent.createIntegerSymbol("CONFIG_CLOCK_DPLL_DIVIDER_VALUE", oscctrlSym_DPLLCTRLB_REFCLK)
oscctrlSym_DPLLCTRLB_DIV.setVisible(False)
oscctrlSym_DPLLCTRLB_DIV.setDefaultValue(2)
oscctrlSym_DPLLCTRLB_DIV.setDependencies(calcDpllXoscDivider,["CONFIG_CLOCK_DPLL_DIVIDER"])


clkSym_DPLL96M_Freq = coreComponent.createIntegerSymbol("DPLL96M_CLOCK_FREQ", calculatedFreq_Menu)
clkSym_DPLL96M_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_DPLL96M_Freq.setReadOnly(True)
clkSym_DPLL96M_Freq.setDefaultValue(0)
clkSym_DPLL96M_Freq.setLabel("FDPLL96M Clock Frequency")

clkSym_DPLL96M_Freq.setDependencies(setDPLL96MClockFreq, ["CONFIG_CLOCK_DPLL_ENABLE",
                                                          "XOSC32K_FREQ",
                                                          "XOSC_FREQ",
                                                          "CONFIG_CLOCK_DPLL_DIVIDER",
                                                          "CONFIG_CLOCK_DPLL_REF_CLOCK",
                                                          "CONFIG_CLOCK_DPLL_LDR_INTEGER",
                                                          "CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION",
                                                          "GCLK_ID_0_FREQ",
                                                          "CONFIG_CLOCK_DPLL_PRESCALAR"])

################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC32K Configuration Callback Functions    ############################

def setXOSC32KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xosc32k = Database.getSymbolValue("core", "XOSC32K_EN32K")
    xoscmode = Database.getSymbolValue("core","XOSC32K_OSCILLATOR_MODE")
    xosc_in_freq = Database.getSymbolValue("core","XOSC32K_FREQ_IN")

    if (xosc == True) and (xoscmode == 1) and (xosc32k == True):
        symbol.setValue(32768, 1)
    elif (xosc == True) and (xoscmode == 1) and (xosc32k == False):
        symbol.setValue(0, 1)
    elif (xosc == True) and (xoscmode==0):
        symbol.setValue(xosc_in_freq, 1)
    elif (xosc == False):
        symbol.setValue(0, 1)

def setXOSC1KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xosc1k = Database.getSymbolValue("core", "XOSC32K_EN1K")
    xoscmode = Database.getSymbolValue("core","XOSC32K_OSCILLATOR_MODE")

    if xosc and xosc1k and (xoscmode==1):
        symbol.setValue(1024, 1)
    else:
        symbol.setValue(0, 1)

################################################################################
#######          OSC32KCTRL Database Components      ###########################
################################################################################

global rtcClockSourceSelection
#####################    OSCULP32K Components    ###############################
clkSym_OSCULP32K_Freq = coreComponent.createIntegerSymbol("OSCULP32K_FREQ", calculatedFreq_Menu)
clkSym_OSCULP32K_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:OSCULP32K")
clkSym_OSCULP32K_Freq.setLabel("OSCULP32K Clock Frequency")
clkSym_OSCULP32K_Freq.setDefaultValue(32768)
clkSym_OSCULP32K_Freq.setReadOnly(True)

clkSym_OSCULP1K_Freq = coreComponent.createIntegerSymbol("OSCULP1K_FREQ", calculatedFreq_Menu)
clkSym_OSCULP1K_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_OSCULP1K_Freq.setLabel("OSCULP1K Clock Frequency")
clkSym_OSCULP1K_Freq.setDefaultValue(1024)
clkSym_OSCULP1K_Freq.setReadOnly(True)


####################    XOSC32K Components    ##################################
#XOSC32K External Oscillator Enable
osc32kctrlSym_XOSC32K_CONFIG_ENABLE = coreComponent.createBooleanSymbol("CONF_CLOCK_XOSC32K_ENABLE", xosc32k_Menu)
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setLabel("32KHz External Crystal Oscillator(XOSC32K) Enable")
osc32kctrlSym_XOSC32K_CONFIG_ENABLE.setDefaultValue(False)

#XOSC32K External Oscillator Mode
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE = coreComponent.createKeyValueSetSymbol("XOSC32K_OSCILLATOR_MODE", xosc32k_Menu)
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setLabel("32KHz External Oscillator Mode ")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey("EXTERNAL_CLOCK","0","xosc32K external clock enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.addKey("CRYSTAL","1","crystal oscillator enable")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setOutputMode("Value")
osc32kctrlSym_XOSC32K_OSCILLATOR_MODE.setDefaultValue(1)

clkSym_XOSC32K_Input_Freq = coreComponent.createIntegerSymbol("XOSC32K_FREQ_IN", xosc32k_Menu)
clkSym_XOSC32K_Input_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
clkSym_XOSC32K_Input_Freq.setLabel("Frequency")
clkSym_XOSC32K_Input_Freq.setDefaultValue(32768)

#XOSC32K External Oscillator Run StandBy Mode
osc32kctrlSym_XOSC32K_RUNSTDBY = coreComponent.createBooleanSymbol("XOSC32K_RUNSTDBY", xosc32k_Menu)
osc32kctrlSym_XOSC32K_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_RUNSTDBY.setLabel("Run Oscillator in Standby Sleep Mode")

#XOSC32K External Oscillator ONDEMAND Mode
osc32kctrlSym_XOSC32K_ONDEMAND= coreComponent.createKeyValueSetSymbol("XOSC32K_ONDEMAND", xosc32k_Menu)
osc32kctrlSym_XOSC32K_ONDEMAND.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_ONDEMAND.setLabel("Oscillator On-Demand Control")
osc32kctrlSym_XOSC32K_ONDEMAND.setDescription("Configures the DPLL on Demand Behavior")
osc32kctrlSym_XOSC32K_ONDEMAND.setOutputMode("Key")
osc32kctrlSym_XOSC32K_ONDEMAND.setDisplayMode("Description")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey("DISABLE",str(0),"Always Enable")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey("ENABLE",str(1),"Only on Peripheral Request")
osc32kctrlSym_XOSC32K_ONDEMAND.setDefaultValue(0)

#XOSC32K External Oscillator 1KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN1K = coreComponent.createBooleanSymbol("XOSC32K_EN1K", xosc32k_Menu)
osc32kctrlSym_XOSC32K_EN1K.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_EN1K.setLabel("Enable 1KHz Output")

#XOSC32K External Oscillator 1KHz Output Frequency Mode
clkSym_XOSC1K_Freq = coreComponent.createIntegerSymbol("XOSC1K_FREQ", calculatedFreq_Menu)
clkSym_XOSC1K_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_XOSC1K_Freq.setLabel("XOSC1K Clock Frequency")
clkSym_XOSC1K_Freq.setDefaultValue(0)
clkSym_XOSC1K_Freq.setReadOnly(True)
clkSym_XOSC1K_Freq.setDependencies(setXOSC1KFreq, ["CONF_CLOCK_XOSC32K_ENABLE", "XOSC32K_EN1K", "XOSC32K_OSCILLATOR_MODE"])

#XOSC32K External Oscillator 32KHz Output Enable Mode
osc32kctrlSym_XOSC32K_EN32K = coreComponent.createBooleanSymbol("XOSC32K_EN32K", xosc32k_Menu)
osc32kctrlSym_XOSC32K_EN32K.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_EN32K.setLabel("Enable 32KHz Output")

#XOSC32K External Oscillator StartUp Time
osc32kctrlSym_XOSC32K_STARTUP = coreComponent.createKeyValueSetSymbol("XOSC32K_STARTUP", xosc32k_Menu)
osc32kctrlSym_XOSC32K_STARTUP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_STARTUP.setLabel("Oscillator Startup Time ")
osc32kctrlSym_XOSC32K_STARTUP.setDescription("XOSC start up time ")
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

#RTC Clock Selection
rtcClockSourceSelection = coreComponent.createKeyValueSetSymbol("CONFIG_CLOCK_RTC_SRC",xosc32k_Menu) # FIXME base component by Kathir
rtcClockSourceSelection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:RTCCTRL")
rtcClockSourceSelection.setLabel("RTC Clock Selection")
rtcClockSourceSelection.setDescription("Clock Source selection for RTC")

rtcClockSourceSelection.addKey("OSCULP1K", "0", "32 KHz Ultra Low-Power Internal Oscillator (1 KHz Output)")
rtcClockSourceSelection.addKey("OSCULP32K", "1", "32 KHz Ultra Low-Power Internal Oscillator (32 KHz Output)")
rtcClockSourceSelection.addKey("XOSC1K", "4", "32.768 KHz External Crystal Oscillator (1.024 KHz Output)")
rtcClockSourceSelection.addKey("XOSC32K", "5", "32.768 KHz External Crystal Oscillator (32.768 KHz Output)")

rtcClockSourceSelection.setDefaultValue(0)
rtcClockSourceSelection.setOutputMode("Value")
rtcClockSourceSelection.setDisplayMode("Key")

#XOSC32K External Oscillator Clock Failure Detection(CFD) Enable
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN = coreComponent.createBooleanSymbol("XOSC32K_CFDEN", xosc32k_Menu)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN.setDependencies(interruptControl, ["XOSC32K_CFDEN"])

#XOSC32K External Oscillator Clock Failure Detection(CFD) Pre-Scalar
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC = coreComponent.createBooleanSymbol("XOSC32K_CFDPRESC", osc32kctrlSym_XOSC32K_CFDCTRL_CFDEN)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:CFDCTRL")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setLabel("Clock Failure Backup Clock Frequency Divide-by-2")
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setDefaultValue(False)
osc32kctrlSym_XOSC32K_CFDCTRL_CFDPRESC.setVisible(False)

clkSym_XOSC32K_Freq = coreComponent.createIntegerSymbol("XOSC32K_FREQ", calculatedFreq_Menu)
clkSym_XOSC32K_Freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:XOSC32K")
clkSym_XOSC32K_Freq.setLabel("XOSC32K Clock Frequency")
clkSym_XOSC32K_Freq.setDefaultValue(0)
clkSym_XOSC32K_Freq.setReadOnly(True)
clkSym_XOSC32K_Freq.setDependencies(setXOSC32KFreq, ["CONF_CLOCK_XOSC32K_ENABLE", "XOSC32K_EN32K", "XOSC32K_OSCILLATOR_MODE", "XOSC32K_FREQ_IN"])


################################################################################
##########             GCLK Callback Functions            ######################
################################################################################
#GCLK Peripheral Channel Write Lock visible Property
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

        #OSC16M
        elif src == "OSC16M":
            srcFreq = int(Database.getSymbolValue("core", "OSC16M_FREQ"))

        #OSC16M
        elif src == "DFLL":
            srcFreq = int(Database.getSymbolValue("core", "DFLL_CLOCK_FREQ"))

        #DPLL96M
        elif src == "FDPLL":
            srcFreq = int(Database.getSymbolValue("core","DPLL96M_CLOCK_FREQ"))

        divSel = int(Database.getSymbolValue("core","GCLK_" + index + "_DIVSEL"))
        div = int(Database.getSymbolValue("core","GCLK_" + index + "_DIV"))

        if divSel == 0:

            if div != 0:
                gclk_freq = int(srcFreq / float(div))
            else:
                gclk_freq = srcFreq

        elif divSel == 1:
            gclk_freq = int(srcFreq / float(2**(div + 1)))

        if symbol.getValue() != gclk_freq:
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
    global topsort
    global gclkSym_GENCTRL_SRC
    global cycleFormed
    from collections import defaultdict
    sourceDestmap = defaultdict(list)
    sourceDestmap = {
                    "FDPLL" : [],
                    "DFLL"  : [],
                    "GCLK0" : [],
                    "GCLK1" : [],
                    "GCLK2" : [],
                    "GCLK3" : [],
                    "GCLK4" : []
                    }
    symbol.clearValues()
    codeList = []

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == True:
        sourceDestmap["GCLK" + str(Database.getSymbolValue("core", "GCLK_ID_2_GENSEL"))].append("DFLL")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")) == True :
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_REF_CLOCK"))) == 2):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core", "GCLK_ID_0_GENSEL"))].append("FDPLL")

    for i in range(0, 5):
        if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)):
           if gclkSym_GENCTRL_SRC[i].getSelectedKey() in ["FDPLL", "GCLK1", "DFLL"]:
                sourceDestmap[gclkSym_GENCTRL_SRC[i].getSelectedKey()].append("GCLK"+str(i))

    codeList = topsort(sourceDestmap)
    if len(codeList) != 0:
        cycleFormed.setValue(False,2)

        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DPLL_ENABLE")) == False :
            codeList.remove("FDPLL")
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == False :
            codeList.remove("DFLL")
        for i in range(0, 5):
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
            freq = int(Database.getSymbolValue("core", symbolKey + "_FREQ"))
            if int( Database.getSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY")) != freq:
                Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", freq , 2)
        else :
            if int( Database.getSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY")) > 0:
                Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", 0, 2)

    if "_FREQ" in event["id"]:
        symbolKey = event["id"].split("_FREQ")[0]
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            if Database.getSymbolValue("core", i + "_CLOCK_ENABLE"):
                freq = int(Database.getSymbolValue("core", symbolKey + "_FREQ"))
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

    if symbol.getValue != divider:
        symbol.setValue(divider,2)

def setGCLKIOFreq(symbol, event):
    index = int(symbol.getID().split("GCLK_IO_")[1].split("_FREQ")[0])
    enable = Database.getSymbolValue("core", "GCLK_" + str(index) + "_OUTPUTENABLE" )
    if enable:
        if symbol.getValue() != int (Database.getSymbolValue("core", "GCLK_" + str(index) + "_FREQ" )):
            symbol.setValue(int (Database.getSymbolValue("core", "GCLK_" + str(index) + "_FREQ" )), 2)
    else:
        if symbol.getValue() > 2:
            symbol.setValue(0, 2)

def gclkMaxset(symbol, event):
    global gclkSym_GENCTRL_DIV
    generator = int(symbol.getID().split("GCLK_")[1].split("_DIV")[0])
    if event["value"] == 1:
        if (generator == 1):
            symbol.setMax(16)
        else:
            symbol.setMax(8)
    else:
        if (generator == 1):
            symbol.setMax(0xffff)
        else:
            symbol.setMax(0xff)


################################################################################
#######          GCLK Database Components            ###########################
################################################################################

################################Peripheral Clock Max Value Callbacks#################################

#######################################################################################
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
codeGenerationDep = []
triggerdepList = []
global indexSymbolMap
indexSymbolMap = defaultdict(list)


#------------------------- ATDF Read -------------------------------------
packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
channel = []
availablePins = []        # array to save available pins
gclk_io_signals = [False, False, False, False, False, False, False, False, False, False] #array to save available signals
pinout = ""
numPads = 0
global cycleFormed
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

for gclknumber in range(0,5):
    gclkSym_num.append(gclknumber)
    gclkSym_num[gclknumber] = coreComponent.createBooleanSymbol("GCLK_INST_NUM" + str(gclknumber),gclkGen_Menu)
    gclkSym_num[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    gclkSym_num[gclknumber].setLabel("Enable Generic Clock Generator " + str(gclknumber))
    if( gclknumber == 0):
        gclkSym_num[gclknumber].setDefaultValue(True)
        gclkSym_num[gclknumber].setReadOnly(False)

    #GCLK Generator Run StandBy
    gclkSym_GENCTRL_RUNSTDBY.append(gclknumber)
    gclkSym_GENCTRL_RUNSTDBY[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_RUNSTDBY", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
    gclkSym_GENCTRL_RUNSTDBY[gclknumber].setLabel("GCLK should keep running in Standby mode")

    #GCLK External Clock input frequency
    if(gclk_io_signals[gclknumber]==True):
        numPads = numPads + 1
        gclkSym_GCLK_IO_FREQ.append(gclknumber)
        gclkSym_GCLK_IO_FREQ[gclknumber] = coreComponent.createIntegerSymbol("GCLK_IO_" + str(gclknumber) +"_FREQ", gclkSym_num[gclknumber])
        gclkSym_GCLK_IO_FREQ[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
        gclkSym_GCLK_IO_FREQ[gclknumber].setLabel("External Input (GCLK_IO[" + str(gclknumber) + "]) Frequency")
        gclkSym_GCLK_IO_FREQ[gclknumber].setDefaultValue(0)
        gclkSym_GCLK_IO_FREQ[gclknumber].setDependencies(setGCLKIOFreq, ["GCLK_" + str(gclknumber) + "_FREQ", "GCLK_" + str(gclknumber) + "_OUTPUTENABLE" ])

    #GCLK Generator Source Selection
    gclkSym_GENCTRL_SRC.append(gclknumber)
    gclkSym_GENCTRL_SRC[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_SRC", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_SRC[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
    gclkSym_GENCTRL_SRC[gclknumber].setLabel("Source Selection")

    gclkSym_GENCTRL_SRC[gclknumber].addKey("XOSC", "0", "External Crystal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("OSC16M", "5", "16 MHz Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("DFLL", "6", "DFLL 48MHz")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("FDPLL", "7", "96 MHz Franctional DPLL")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("OSCULP32K", "3", "32 KHz Ultra Low-Power Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey("XOSC32K", "4", "32.768 KHz External Crystal Oscillator")

    gclk_in="GCLK_IN["+str(gclknumber)+"]"
    gclk_in_desc= "Generator Input Pad ("+"GCLK_IN["+str(gclknumber)+"])"

    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_SRC[gclknumber].addKey(gclk_in, "1", gclk_in_desc)

    if gclknumber !=1:
        gclkSym_GENCTRL_SRC[gclknumber].addKey("GCLK1", "2", "GCLK Generator 1")

    gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(1)
    gclkSym_GENCTRL_SRC[gclknumber].setOutputMode("Value")
    gclkSym_GENCTRL_SRC[gclknumber].setDisplayMode("Key")



    #GCLK Generator Output Enable
    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_OE.append(gclknumber)
        gclkSym_GENCTRL_OE[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_OUTPUTENABLE", gclkSym_num[gclknumber])
        gclkSym_GENCTRL_OE[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
        gclkSym_GENCTRL_OE[gclknumber].setLabel("Output GCLK clock signal on IO pin?")

    #GCLK Generator Output Off Value
    if(gclk_io_signals[gclknumber]==True):
        gclkSym_GENCTRL_OOV.append(gclknumber)
        gclkSym_GENCTRL_OOV[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_OUTPUTOFFVALUE", gclkSym_GENCTRL_OE[gclknumber])
        gclkSym_GENCTRL_OOV[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
        gclkSym_GENCTRL_OOV[gclknumber].setLabel("Output Off Value")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("LOW","0","Logic Level 0")
        gclkSym_GENCTRL_OOV[gclknumber].addKey("HIGH","1","Logic Level 1")
        gclkSym_GENCTRL_OOV[gclknumber].setDefaultValue(0)
        gclkSym_GENCTRL_OOV[gclknumber].setOutputMode("Key")
        gclkSym_GENCTRL_OOV[gclknumber].setDisplayMode("Description")

        gclkInFreq = coreComponent.createIntegerSymbol("GCLK_IN_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
        gclkInFreq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
        gclkInFreq.setLabel("Gclk Input Frequency")
        gclkInFreq.setDefaultValue(0)

    #GCLK Generator Division Selection
    gclkSym_GENCTRL_DIVSEL.append(gclknumber)
    gclkSym_GENCTRL_DIVSEL[gclknumber] = coreComponent.createKeyValueSetSymbol("GCLK_" + str(gclknumber) + "_DIVSEL", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVSEL[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
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


    gclkSym_GENCTRL_DIVSEL[gclknumber].setOutputMode("Key")
    gclkSym_GENCTRL_DIVSEL[gclknumber].setDisplayMode("Description")

    #GCLK Generator Division Factor
    gclkSym_GENCTRL_DIV.append(gclknumber)
    gclkSym_GENCTRL_DIV[gclknumber] = coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_DIV", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIV[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
    gclkSym_GENCTRL_DIV[gclknumber].setLabel("Division Factor")
    gclkSym_GENCTRL_DIV[gclknumber].setMin(0)
    if (gclknumber == 1):
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xffff)
    else:
        gclkSym_GENCTRL_DIV[gclknumber].setMax(0xff)
    gclkSym_GENCTRL_DIV[gclknumber].setDefaultValue(1)
    gclkSym_GENCTRL_DIV[gclknumber].setDependencies(gclkMaxset, ["GCLK_" + str(gclknumber) + "_DIVSEL"])
    gclkSym_GENCTRL_DIVSEL[gclknumber].setDefaultValue(gclkSymGenDivSelDefaultValue)

  #GCLK Generator Division Factor to show in the UI
    gclkSym_GENCTRL_DIVIDER_VALUE.append(gclknumber)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber] = coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_DIVIDER_VALUE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setVisible(False)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDefaultValue(1)
    gclkSym_GENCTRL_DIVIDER_VALUE[gclknumber].setDependencies(calcGclkDivider,["GCLK_" + str(gclknumber) + "_DIV", "GCLK_" + str(gclknumber) + "_DIVSEL"])

    #GCLK Generator Improve Duty Cycle
    gclkSym_GENCTRL_IDC.append(gclknumber)
    gclkSym_GENCTRL_IDC[gclknumber] = coreComponent.createBooleanSymbol("GCLK_" + str(gclknumber) + "_IMPROVE_DUTYCYCLE", gclkSym_num[gclknumber])
    gclkSym_GENCTRL_IDC[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:GENCTRL")
    gclkSym_GENCTRL_IDC[gclknumber].setLabel("Enable 50/50 Duty Cycle")

    gclkSym_Freq.append(gclknumber)
    gclkSym_Freq[gclknumber]=coreComponent.createIntegerSymbol("GCLK_" + str(gclknumber) + "_FREQ", gclkSym_num[gclknumber])
    gclkSym_Freq[gclknumber].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    gclkSym_Freq[gclknumber].setLabel("GCLK" + str(gclknumber) + " Clock Frequency")
    gclkSym_Freq[gclknumber].setReadOnly(True)
    if(gclknumber == 0):
        gclkSym_Freq[gclknumber].setDefaultValue(osc16MFreq.getValue())
    else:
        gclkSym_Freq[gclknumber].setDefaultValue(0)


    depList = [ "GCLK_" + str(gclknumber) + "_DIVSEL",
                "GCLK_" + str(gclknumber) + "_DIV",
                "GCLK_" + str(gclknumber) + "_SRC",
                "GCLK_INST_NUM" + str(gclknumber),
                "XOSC_FREQ",
                "OSC16M_FREQ",
                "DPLL96M_CLOCK_FREQ",
                "DFLL_CLOCK_FREQ",
                "XOSC32K_FREQ",
                "GCLK_IN_0_FREQ","GCLK_IN_1_FREQ","GCLK_IN_2_FREQ","GCLK_IN_3_FREQ","GCLK_IN_4_FREQ"
                ]
    if gclknumber != 1:
        depList.append("GCLK_1_FREQ")
    gclkSym_Freq[gclknumber].setDependencies(setGClockFreq, depList)

    codeGenerationDep.append("GCLK_" + str(gclknumber) + "_SRC")
    codeGenerationDep.append("GCLK_INST_NUM" + str(gclknumber))

gclkIOpads = coreComponent.createIntegerSymbol("GCLK_NUM_PADS", None)
gclkIOpads.setVisible(False)
gclkIOpads.setDefaultValue(numPads)

maxGCLKId = 0

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
    clkSymPeripheral.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    clkSymPeripheral.setLabel("Peripheral Channel " + str(index) + " Clock Enable")
    clkSymPeripheral.setDefaultValue(False)

    #GCLK Peripheral Channel Name
    gclkSym_PERCHANNEL_NAME = coreComponent.createStringSymbol(key + "_NAME", clkSymPeripheral)
    gclkSym_PERCHANNEL_NAME.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    gclkSym_PERCHANNEL_NAME.setLabel("Peripheral")
    gclkSym_PERCHANNEL_NAME.setReadOnly(True)
    gclkSym_PERCHANNEL_NAME.setDefaultValue(name)

    #GCLK Peripheral Channel Index
    gclkSym_PERCHANNEL_INDEX = coreComponent.createIntegerSymbol(key + "_INDEX", clkSymPeripheral)
    gclkSym_PERCHANNEL_INDEX.setVisible(False)
    gclkSym_PERCHANNEL_INDEX.setDefaultValue(int(index))

    #Peripheral Channel Generator Selection
    gclkSym_PCHCTRL_GEN = coreComponent.createKeyValueSetSymbol(key + "_GENSEL", clkSymPeripheral)
    gclkSym_PCHCTRL_GEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:PCHCTRL")
    gclkSym_PCHCTRL_GEN.setLabel("Generator Selection")

    gclkSymPCHCTRLGenNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GCLK_PCHCTRL__GEN\"]")
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
    gclkSym_PCHCTRL_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    gclkSym_PCHCTRL_FREQ.setLabel("Peripheral Channel " + str(index) + " Frequency ")
    gclkSym_PCHCTRL_FREQ.setReadOnly(True)
    gclkSym_PCHCTRL_FREQ.setDependencies(setPCHCTRLFREQVisibleProperty, [key + "_CHEN",key + "_GENSEL", "GCLK_0_FREQ", "GCLK_1_FREQ", "GCLK_2_FREQ", "GCLK_3_FREQ", "GCLK_4_FREQ",
                                                                                    "GCLK_5_FREQ", "GCLK_6_FREQ", "GCLK_7_FREQ", "GCLK_8_FREQ"])
    triggerdepList.append(key + "_FREQ")

    #GCLK Peripheral Channel Lock
    gclkSym_PCHCTRL_WRTLOCK = coreComponent.createBooleanSymbol(key + "_WRITELOCK", clkSymPeripheral)
    gclkSym_PCHCTRL_WRTLOCK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:PCHCTRL")
    gclkSym_PCHCTRL_WRTLOCK.setLabel("Write Lock")

peripheralList = []
symbolIndexMapinverse = {}
for key in indexSymbolMap.keys():
    for i in range (0,len(indexSymbolMap.get(key))):
        peripheralList.append(indexSymbolMap.get(key)[i])
        symbolIndexMapinverse[indexSymbolMap.get(key)[i]] = key

peripheralList.sort()

for name in peripheralList:
    #GCLK Peripheral Channel Enable
    clkSymExtPeripheral = coreComponent.createBooleanSymbol(name + "_CLOCK_ENABLE", peripheralClockMenu)
    clkSymExtPeripheral.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    clkSymExtPeripheral.setLabel(name + " Clock Enable")
    clkSymExtPeripheral.setDefaultValue(False)
    triggerdepList.append(name + "_CLOCK_ENABLE")

    clkSymExtPeripheralFreq = coreComponent.createIntegerSymbol(name + "_CLOCK_FREQUENCY", clkSymExtPeripheral)
    clkSymExtPeripheralFreq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
    clkSymExtPeripheralFreq.setLabel(name + " Clock Frequency")
    clkSymExtPeripheralFreq.setReadOnly(True)

    gclkDependencyList.append(name + "_CLOCK_ENABLE")

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
codeGenerationDep.append("CONFIG_CLOCK_DPLL_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_DPLL_ENABLE")
codeGenerationDep.append("CONFIG_CLOCK_DFLL_ENABLE")
codeGenerationDep.append("GCLK_ID_2_GENSEL")
codeGenerationList.setDependencies(codeGen, codeGenerationDep)
codeGenerationList.addValue("   GCLK0_Initialize();")
codeGenerationList.setTarget("core.CLK_INIT_LIST")


################################################################################
##########              MCLK Callback Functions            #####################
################################################################################
def ahbValue(symbol,event):
    global ahbInit
    global mclkDic

    perInstance = event["id"].split("_CLOCK_ENABLE")[0]
    if perInstance == "CAN0" or perInstance == "CAN1":
        for key in mclkDic.keys():
            if mclkDic.get(key) == perInstance:
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
    global mclkDic
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
                    apbVal =  (apbVal & ~(bitmask)) | int(apbInit[bridge], 16)
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

ahbNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group")
for index in range(0, len(ahbNode.getChildren())):
    if ahbNode.getChildren()[index].getAttribute("name") == "AHBMASK":
        ahbInit = hex(int(ahbNode.getChildren()[index].getAttribute("initval"),16))

#AHB Bridge Clock Initial Settings
mclk_AHB_Clock_Value = coreComponent.createStringSymbol("MCLK_AHB_INITIAL_VALUE",mclkSym_Menu)
mclk_AHB_Clock_Value.setDefaultValue(str(ahbInit))
mclk_AHB_Clock_Value.setDependencies(ahbValue, gclkDependencyList)
mclk_AHB_Clock_Value.setReadOnly(True)
ahbMaskNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCLK"]/register-group@[name="MCLK"]/register@[name="AHBMASK"]')
ahbMaskValues = ahbMaskNode.getChildren()
for index in range(0, len(ahbMaskValues)):
    mclkDic["AHB_" + str(int(ahbMaskValues[index].getAttribute("mask"),16))] = ahbMaskValues[index].getAttribute("name").split("_")[0]
    if ahbMaskValues[index].getAttribute("name").startswith("APB"):
        numAPB = numAPB + 1

bridges = ["APBA", "APBB", "APBC", "APBD", "APBE"]
apbInit = {"APBA" : "",
           "APBB" : "",
           "APBC" : "",
           "APBD" : "",
           "APBE" : ""
           }
for index in range(0, numAPB):
    bridgeName = bridges[index]
    path = "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group@[name=\"MCLK\"]/register@[name=\"" + bridgeName + "MASK\"]"
    apbNode = ATDF.getNode(path)
    apbValues = apbNode.getChildren()
    for bitpos in range(0, len(apbValues)):
        mclkDic[bridgeName + "_" + str(int(apbValues[bitpos].getAttribute("mask"),16))] = apbValues[bitpos].getAttribute("name").split("_")[0]

    apbInitNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCLK\"]/register-group")
    for index in range(0, len(apbInitNode.getChildren())):
        if apbInitNode.getChildren()[index].getAttribute("name") == (bridgeName + "MASK"):
            apbInit[bridgeName] = hex(int(apbInitNode.getChildren()[index].getAttribute("initval"),16))

    #APB Bridge Clock Initial Settings
    mclk_Clock_Value = coreComponent.createStringSymbol("MCLK_" + bridgeName +"_INITIAL_VALUE",mclkSym_Menu)
    mclk_Clock_Value.setDefaultValue(str(apbInit[bridgeName]))
    mclk_Clock_Value.setReadOnly(True)
mclk_Clock_Value.setDependencies(apbValue, gclkDependencyList)

#MCLK source Selection
mclkSrc = coreComponent.createKeyValueSetSymbol("MCLK_SRC", mclkSym_Menu)
mclkSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
mclkSrc.setLabel("Main Clock Source Selection")
mclkSrc.addKey("GCLK0", "0", "GCLK0")
mclkSrc.addKey("DFLLULP", "1", "DFLLULP")
mclkSrc.setDefaultValue(0)
mclkSrc.setOutputMode("Value")
mclkSrc.setDisplayMode("Key")

#MCLK CPU Division
mclkSym_CPUDIV_CPUDIV = coreComponent.createKeyValueSetSymbol("CONF_CPU_CLOCK_DIVIDER",mclkSym_Menu)
mclkSym_CPUDIV_CPUDIV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:CPUDIV")
mclkSym_CPUDIV_CPUDIV.setLabel("CPU Clock Division Factor")
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
mclkSym_CPUDIV_CPUDIV.setDisplayMode("Key")

#MCLK Enable Clock Ready Interrupt
mclkSym_MCLK_INTENSET_CKRDY = coreComponent.createBooleanSymbol("MCLK_INTENSET_CKRDY", mclkSym_Menu)
mclkSym_MCLK_INTENSET_CKRDY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:INTENSET")
mclkSym_MCLK_INTENSET_CKRDY.setLabel("Enable Clock Ready Interrupt")
mclkSym_MCLK_INTENSET_CKRDY.setDependencies(interruptControl, ["MCLK_INTENSET_CKRDY"])

################################################################################
#######          Calculated Clock Frequencies        ###########################
################################################################################
def setMainClockFreq(symbol, event):
    divider = int(Database.getSymbolValue("core","CONF_CPU_CLOCK_DIVIDER"))
    src = int(Database.getSymbolValue("core","MCLK_SRC"))
    if src == 0:
        freq = int(Database.getSymbolValue("core","GCLK_0_FREQ"))
    else:
        freq = int(Database.getSymbolValue("core","DFLL_CLOCK_FREQ"))

    symbol.setValue(freq / (1 << divider), 1)



def setRTCFreq(symbol, event):
    global rtcClockSourceSelection
    src = rtcClockSourceSelection.getSelectedKey()

    freq = 0
    if src == "OSCULP1K":
        freq = int(Database.getSymbolValue("core","OSCULP1K_FREQ"))
    elif src == "OSCULP32K":
        freq = int(Database.getSymbolValue("core","OSCULP32K_FREQ"))
    elif src == "XOSC1K":
        freq = int(Database.getSymbolValue("core","XOSC1K_FREQ"))
    else:
        freq = int(Database.getSymbolValue("core","XOSC32K_FREQ"))

    symbol.setValue(freq, 2)



###############################################################################################
clkSym_MAIN_CLK_FREQ = coreComponent.createIntegerSymbol("CPU_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_MAIN_CLK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_MAIN_CLK_FREQ.setLabel("Main Clock Frequency")
clkSym_MAIN_CLK_FREQ.setReadOnly(True)
clkSym_MAIN_CLK_FREQ.setDependencies(setMainClockFreq, ["GCLK_0_FREQ", "CONF_CPU_CLOCK_DIVIDER", "MCLK_SRC", "DFLL_CLOCK_FREQ"])

divider = mclkSym_CPUDIV_CPUDIV.getValue()
gclk0_freq = int(gclkSym_Freq[0].getValue())
clkSym_MAIN_CLK_FREQ.setValue(gclk0_freq / (divider + 1), 1)

peripherals = ATDF.getNode("/avr-tools-device-file/devices/device@[name=\"" + Variables.get("__PROCESSOR") + "\"]/peripherals")
module_list = peripherals.getChildren()

clkSym_WDT_CLK_FREQ = coreComponent.createIntegerSymbol("WDT_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_WDT_CLK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_WDT_CLK_FREQ.setLabel("WDT Clock Frequency")
clkSym_WDT_CLK_FREQ.setReadOnly(True)
clkSym_WDT_CLK_FREQ.setDefaultValue(1024)

clkSym_RTC_CLK_FREQ = coreComponent.createIntegerSymbol("RTC_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_RTC_CLK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_sam_l10_l11;register:%NOREGISTER%")
clkSym_RTC_CLK_FREQ.setLabel("RTC Clock Frequency")
clkSym_RTC_CLK_FREQ.setReadOnly(True)
clkSym_RTC_CLK_FREQ.setDefaultValue(1024)
clkSym_RTC_CLK_FREQ.setDependencies(setRTCFreq,["CONFIG_CLOCK_RTC_SRC", "OSCULP32K_FREQ", "OSCULP1K_FREQ", "XOSC32K_FREQ", "XOSC1K_FREQ"])


############################Default clock Settings######################
#Enable DFLL
oscctrlSym_DPLL_CONFIG_ENABLE.setValue(True, 1)

#Select DFLL as default clock source
gclkSym_GENCTRL_SRC[1].setValue(1, 1)

gclkSym_GENCTRL_DIV[1].setValue(4,1)

gclkSym_num[1].setValue(True, 2)

Database.setSymbolValue("core", "GCLK_ID_0_GENSEL", 1, 0)

Database.setSymbolValue("core", "GCLK_ID_0_CHEN", True, 0)

Database.setSymbolValue("core", "CONFIG_CLOCK_DPLL_REF_CLOCK", 2, 2)

Database.setSymbolValue("core", "CONFIG_CLOCK_DPLL_LDR_INTEGER", 63, 2)

#Select DFLL as default clock source
gclkSym_GENCTRL_SRC[0].setValue(3, 1)

gclkSym_GENCTRL_DIV[0].setValue(2, 1)

################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clockSym_OSCCTRL_HeaderFile = coreComponent.createFileSymbol("SAML10_CLOCK_HEADER", None)
clockSym_OSCCTRL_HeaderFile.setSourcePath("../peripheral/clk_sam_l10_l11/templates/plib_clock.h.ftl")
clockSym_OSCCTRL_HeaderFile.setOutputName("plib_clock.h")
clockSym_OSCCTRL_HeaderFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setType("HEADER")
clockSym_OSCCTRL_HeaderFile.setMarkup(True)

clockSym_OSCCTRL_SourceFile = coreComponent.createFileSymbol("SAML10_CLOCK_SOURCE", None)
clockSym_OSCCTRL_SourceFile.setSourcePath("../peripheral/clk_sam_l10_l11/templates/plib_clock.c.ftl")
clockSym_OSCCTRL_SourceFile.setOutputName("plib_clock.c")
clockSym_OSCCTRL_SourceFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_SourceFile.setType("SOURCE")
clockSym_OSCCTRL_SourceFile.setMarkup(True)

clockSystemInitFile = coreComponent.createFileSymbol("SAML10_CLOCK_INIT", None)
clockSystemInitFile.setType("STRING")
clockSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clockSystemInitFile.setSourcePath("../peripheral/clk_sam_l10_l11/templates/system/initialization.c.ftl")
clockSystemInitFile.setMarkup(True)

clockSystemDefFile = coreComponent.createFileSymbol("SAML10_CLOCK_SYS_DEF", None)
clockSystemDefFile.setType("STRING")
clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clockSystemDefFile.setSourcePath("../peripheral/clk_sam_l10_l11/templates/system/definitions.h.ftl")
clockSystemDefFile.setMarkup(True)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    clockSym_OSCCTRL_HeaderFile.setSecurity("SECURE")
    clockSym_OSCCTRL_SourceFile.setSecurity("SECURE")
    clockSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE")
    clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")