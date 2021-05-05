"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

pll_Menu = []
global topsort
clkMenu = coreComponent.createMenuSymbol("PIC32CZ_CA_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")

# Clock Source Configuration
clkSourceMenu = coreComponent.createMenuSymbol("CLOCK_SOURCE", clkMenu)
clkSourceMenu.setLabel("Clock Source Configuration")

global oscctrlXosc_Menu
oscctrlXosc_Menu = coreComponent.createMenuSymbol(
    "XOSCCTRL_MENU", clkSourceMenu)
oscctrlXosc_Menu.setLabel(
    "External Crystal Oscillator Configuration")

for index in range(0, 2):
    pll_Menu.append(index)
    pll_Menu[index] = coreComponent.createMenuSymbol(
        "PLL MENU" + str(index), clkSourceMenu)
    pll_Menu[index].setLabel(
        "PLL " + str(index) + " Configuration")

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
    enable = Database.getSymbolValue(
        "core", "CONFIG_CLOCK_XOSC_ENABLE")

    if enable:
        symbol.setValue(Database.getSymbolValue(
            "core", "CONFIG_CLOCK_XOSC_FREQUENCY"), 1)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0)

####    PLL Configuration Callback Functions    ###############################
def setPLLClockFreq(symbol, event):
    index = symbol.getID().split("PLL")[1][0]
    clockOutputNum = symbol.getID().split("FREQ")[1][0]

    enable = Database.getSymbolValue(
        "core", "CONFIG_CLOCK_PLL" + index + "_ENABLE")

    if enable:
        clockSrc = Database.getSymbolValue(
            "core", "CONFIG_CLOCK_PLL" + index + "_REF_CLOCK")

        # GCLK_PLL Clock
        if clockSrc == 0:
            srcFreq = int(Database.getSymbolValue("core", "GCLK_ID_"+ str(int(index) + 1) +"_FREQ"))
        # XOSC Clock
        elif clockSrc == 1:
            srcFreq = int(Database.getSymbolValue("core", "XOSC_FREQ"))
        # DFLL48M Clock
        elif clockSrc == 2:
            srcFreq = Database.getSymbolValue("core", "DFLL_CLOCK_FREQ")
        else:
            return

        fbdiv = int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_PLLFBDIV_FBDIV"))
        refdiv = int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_PLLREFDIV_REFDIV"))
        postdiv = int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_PLLPOSTDIVA_POSTDIV" + clockOutputNum))

        pllFreq = int((srcFreq * fbdiv) / (refdiv * postdiv))

        intdiv = int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_FRACDIV_INTDIV"))
        if intdiv > 0:
            remdiv = int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_FRACDIV_REMDIV"))
            pllFreq = int(pllFreq / (2 * (intdiv + (remdiv/512))))

        prevFreq = symbol.getValue()
        if (prevFreq != pllFreq) and (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_PLLPOSTDIVA_OUTEN" + clockOutputNum) == True):
            if pllFreq > symbol.getMax():
                symbol.setValue(symbol.getMax())
            else:
                symbol.setValue(pllFreq)
        elif (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL" + index + "_PLLPOSTDIVA_OUTEN" + clockOutputNum) == False):
            symbol.setValue(0)
    else:
        if symbol.getValue() > 0:
            symbol.setValue(0)

def setDfllFreq(symbol, event):
    enable = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")
    freq = 0
    if enable:
        mode = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE")
        usbCrm = Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_USB")
        mul = int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_MUL"))
        if mode == 0:
            freq = 48000000
        elif ((mode == 1) and (usbCrm == False)):
            refFreq = int(Database.getSymbolValue("core", "GCLK_ID_0_FREQ"))
            freq = mul * refFreq

        elif (mode == 1) and (usbCrm == True):
            freq = mul * 1000

    prevFreq = symbol.getValue()

    if prevFreq != freq:
        symbol.setValue(freq)

################################################################################
#######          OSCCTRL Database Components      ##############################
################################################################################

############################   XOSC Components    ##############################
# XOSC Oscillator Enable
oscctrlSym_XOSC_CONFIG_ENABLE = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_XOSC_ENABLE", oscctrlXosc_Menu)
oscctrlSym_XOSC_CONFIG_ENABLE.setLabel(
    "External Multipurpose Crystal Oscillator(XOSC) Enable")
oscctrlSym_XOSC_CONFIG_ENABLE.setDescription(
    "External Crystal Oscillator Enable Feature")
oscctrlSym_XOSC_CONFIG_ENABLE.setDefaultValue(False)

# XOSC Auto Gain Control Loop Enable
oscctrlSym_XOSC_AGC = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_XOSC_AGC_ENABLE", oscctrlXosc_Menu)
oscctrlSym_XOSC_AGC.setLabel("Auto Gain Control Loop Enable")
oscctrlSym_XOSC_AGC.setDefaultValue(False)

# Xosc Clock Switch Enable
oscctrlSym_XOSC_SWBEN = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_XOSC_SWBEN", oscctrlXosc_Menu)
oscctrlSym_XOSC_SWBEN.setLabel("Xosc Clock Switch Enable")
oscctrlSym_XOSC_SWBEN.setDefaultValue(False)

# XOSC Oscillator Mode
oscctrlSym_XOSC_OSCILLATORMODE = coreComponent.createKeyValueSetSymbol(
    "XOSC_OSCILLATOR_MODE", oscctrlXosc_Menu)
oscctrlSym_XOSC_OSCILLATORMODE.setLabel("External Oscillator Mode ")
oscctrlSym_XOSC_OSCILLATORMODE.addKey(
    "EXTERNAL_CLOCK", "0", "xosc external clock enable")
oscctrlSym_XOSC_OSCILLATORMODE.addKey(
    "CRYSTAL", "1", "crystal oscillator enable")
oscctrlSym_XOSC_OSCILLATORMODE.setOutputMode("Value")
oscctrlSym_XOSC_OSCILLATORMODE.setDefaultValue(1)

# XOSC Oscillator Frequency
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY = coreComponent.createIntegerSymbol(
    "CONFIG_CLOCK_XOSC_FREQUENCY", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setLabel("Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDescription(
    "Setting the XOSC Frequency")
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setDefaultValue(12000000)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setMin(0)
oscctrlSym_XOSCCTRL_OSCILLATOR_FREQUENCY.setMax(48000000)

# XOSC Oscillator ONDEMAND Mode
oscctrlSym_XOSCCTRL_ONDEMAND = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_XOSC_ONDEMAND", oscctrlXosc_Menu)
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
    "CONFIG_CLOCK_XOSC_STARTUP", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_STARTUP.setLabel("Oscillator Startup Time")
oscctrlSym_XOSCCTRL_STARTUP.setDescription("Startup time for the XOSC")
oscctrlSymXOSCStartupNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"XOSCCTRLA__STARTUP\"]")
oscctrlSymXOSCStartupValues = []
oscctrlSymXOSCStartupValues = oscctrlSymXOSCStartupNode.getChildren()
for index in range(0, len(oscctrlSymXOSCStartupValues)):
    xoscstartupKeyName = oscctrlSymXOSCStartupValues[index].getAttribute("name")
    xoscstartupKeyDescription = oscctrlSymXOSCStartupValues[index].getAttribute("caption")
    xoscstartupKeyValue = oscctrlSymXOSCStartupValues[index].getAttribute("value")
    oscctrlSym_XOSCCTRL_STARTUP.addKey(xoscstartupKeyName, xoscstartupKeyValue, xoscstartupKeyDescription)
oscctrlSym_XOSCCTRL_STARTUP.setDefaultValue(14)
oscctrlSym_XOSCCTRL_STARTUP.setOutputMode("Value")
oscctrlSym_XOSCCTRL_STARTUP.setDisplayMode("Description")

# XOSC Oscillator Clock Failure Detector(CFD) Enable
oscctrlSym_XOSCCTRL_CFDEN = coreComponent.createBooleanSymbol(
    "CONFIG_CLOCK_XOSC_CFDEN", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_CFDEN.setLabel("Enable Clock Failure Detection")
oscctrlSym_XOSCCTRL_CFDEN.setDescription(
    "Clock Failure Detection enable or not")
oscctrlSym_XOSCCTRL_CFDEN.setDefaultValue(False)

# XOSC Oscillator Clock Failure Detector(CFD) Pre-Scalar
oscctrlSym_CFDPRESC_CFDPRESC = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_XOSC_CFDPRESC", oscctrlSym_XOSCCTRL_CFDEN)
oscctrlSym_CFDPRESC_CFDPRESC.setLabel("Safe Clock Frequency ")
oscctrlSym_CFDPRESC_CFDPRESC.setDescription("Startup time for the XOSC")
oscctrlSym_CFDPRESC_CFDPRESC.setVisible(True)
oscctrlSymCFDPrescNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"XOSCCTRLA__CFDPRESC\"]")
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

# XOSC Oscillator USBHS Referrence Clock Division
oscctrlSym_XOSCCTRL_USBHSDIV = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_XOSC_USBHSDIV", oscctrlXosc_Menu)
oscctrlSym_XOSCCTRL_USBHSDIV.setLabel("USBHS Referrence Clock Division")
oscctrlSym_XOSCCTRL_USBHSDIV.setDescription("USBHS Referrence Clock Division for the XOSC")
oscctrlSymXOUsbhsdivNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"XOSCCTRLA__USBHSDIV\"]")
oscctrlSymXOSCUsbhsdivValues = []
oscctrlSymXOSCUsbhsdivValues = oscctrlSymXOUsbhsdivNode.getChildren()
for index in range(0, len(oscctrlSymXOSCUsbhsdivValues)):
    xoscUsbhsdivKeyName = oscctrlSymXOSCUsbhsdivValues[index].getAttribute(
        "name")

    xoscUsbhsdivKeyDescription = oscctrlSymXOSCUsbhsdivValues[index].getAttribute(
        "caption")
    xoscUsbhsdivKeyValue = oscctrlSymXOSCUsbhsdivValues[index].getAttribute(
        "value")
    oscctrlSym_XOSCCTRL_USBHSDIV.addKey(
        xoscUsbhsdivKeyName, xoscUsbhsdivKeyValue, xoscUsbhsdivKeyDescription)

oscctrlSym_XOSCCTRL_USBHSDIV.setDefaultValue(0)
oscctrlSym_XOSCCTRL_USBHSDIV.setOutputMode("Value")
oscctrlSym_XOSCCTRL_USBHSDIV.setDisplayMode("Description")

clkSym_XOSC_Freq = coreComponent.createIntegerSymbol(
    "XOSC_FREQ", calculatedFreq_Menu)
clkSym_XOSC_Freq.setLabel("XOSC Clock Frequency")
clkSym_XOSC_Freq.setReadOnly(True)
clkSym_XOSC_Freq.setDependencies(setXOSCFreq, [
                                 "CONFIG_CLOCK_XOSC_ENABLE", "CONFIG_CLOCK_XOSC_FREQUENCY"])

############################   PLL Components    ############################
for i in range(0, 2):
    # Phase Locked Loop(PLL) Enable
    oscctrlSym_PLL_CONFIG_ENABLE = coreComponent.createBooleanSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_ENABLE", pll_Menu[i])
    oscctrlSym_PLL_CONFIG_ENABLE.setLabel(
        "Phase Locked Loop(PLL) Enable ")
    oscctrlSym_PLL_CONFIG_ENABLE.setDescription(
        "PLL Configuration enabling feature")
    oscctrlSym_PLL_CONFIG_ENABLE.setDefaultValue(False)

    # Phase Locked Loop(PLL) ONDEMAND Mode
    oscctrlSym_PLLCTRL_ONDEMAND = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_ONDEMAND", pll_Menu[i])
    oscctrlSym_PLLCTRL_ONDEMAND.setLabel("PLL On-Demand Control")
    oscctrlSym_PLLCTRL_ONDEMAND.setDescription(
        "Configures the PLL on Demand Behavior")
    oscctrlSym_PLLCTRL_ONDEMAND.setOutputMode("Value")
    oscctrlSym_PLLCTRL_ONDEMAND.setDisplayMode("Description")
    oscctrlSym_PLLCTRL_ONDEMAND.addKey("Disable", str(0), "Always Enable")
    oscctrlSym_PLLCTRL_ONDEMAND.addKey(
        "Enable", str(1), "Only on Peripheral Request")
    oscctrlSym_PLLCTRL_ONDEMAND.setDefaultValue(0)

    # Bandwidth selection
    oscctrlSym_PLLCTRL_BWSEL = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_BWSEL", pll_Menu[i])
    oscctrlSym_PLLCTRL_BWSEL.setLabel("Bandwidth selection")
    oscctrlSym_PLLCTRL_BWSEL.setDescription("Bandwidth selection for the PLL" + str(i))
    oscctrlSym_BWSELNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"OSCCTRL\"]/value-group@[name=\"PLL0CTRL__BWSEL\"]")
    oscctrlSym_BWSELValues = []
    oscctrlSym_BWSELValues = oscctrlSym_BWSELNode.getChildren()
    for index in range(0, len(oscctrlSym_BWSELValues)):
        oscctrlBWSELKeyName = oscctrlSym_BWSELValues[index].getAttribute(
            "name")
        oscctrlBWSELKeyDescription = oscctrlSym_BWSELValues[index].getAttribute(
            "caption")
        oscctrlBWSELKeyValue = oscctrlSym_BWSELValues[index].getAttribute(
            "value")
        oscctrlSym_PLLCTRL_BWSEL.addKey(
            oscctrlBWSELKeyName, oscctrlBWSELKeyValue, oscctrlBWSELKeyDescription)

    oscctrlSym_PLLCTRL_BWSEL.setDefaultValue(1)
    oscctrlSym_PLLCTRL_BWSEL.setOutputMode("Value")
    oscctrlSym_PLLCTRL_BWSEL.setDisplayMode("Key")

    # Digital Phase Locked Loop(PLL) Reference Clock
    oscctrlSym_PLLCTRL_REFCLK = coreComponent.createKeyValueSetSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_REF_CLOCK", pll_Menu[i])
    oscctrlSym_PLLCTRL_REFCLK.setLabel("PLL Reference Clock Source")
    oscctrlSym_PLLCTRL_REFCLK.setDescription(
        "PLL reference clock selection")

    oscctrlSym_PLLCTRL_REFCLK.addKey(
        "GCLK_PLL", "0", "Generic Clock for PLL")
    oscctrlSym_PLLCTRL_REFCLK.addKey(
        "XOSC", "1", "External Crystal Oscillator")
    oscctrlSym_PLLCTRL_REFCLK.addKey(
        "DFLL48M", "2", "DFLL48M Clock")

    oscctrlSym_PLLCTRL_REFCLK.setDefaultValue(2)
    oscctrlSym_PLLCTRL_REFCLK.setOutputMode("Value")
    oscctrlSym_PLLCTRL_REFCLK.setDisplayMode("Key")

    # Phase Locked Loop(PLL) PLL Feed-Back Divider Factor
    oscctrlSym_PLLFBDIV_FBDIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_PLLFBDIV_FBDIV", pll_Menu[i])
    oscctrlSym_PLLFBDIV_FBDIV.setLabel("PLL Feed-Back Divider Factor")
    oscctrlSym_PLLFBDIV_FBDIV.setDescription(
        "PLL Feed-Back Divider Factor, fVCO = fCKR * (FBDIV/REFDIV)")
    oscctrlSym_PLLFBDIV_FBDIV.setDefaultValue(225)
    oscctrlSym_PLLFBDIV_FBDIV.setMin(21)
    oscctrlSym_PLLFBDIV_FBDIV.setMax(1023)

    # Phase Locked Loop(PLL) PLL reference division factor
    oscctrlSym_PLLREFDIV_REFDIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_PLLREFDIV_REFDIV", pll_Menu[i])
    oscctrlSym_PLLREFDIV_REFDIV.setLabel("PLL reference division factor")
    oscctrlSym_PLLREFDIV_REFDIV.setDescription(
        "PLL reference division factor, fPFD = fCKR/REFDIV")
    oscctrlSym_PLLREFDIV_REFDIV.setDefaultValue(12)
    oscctrlSym_PLLREFDIV_REFDIV.setMin(1)
    oscctrlSym_PLLREFDIV_REFDIV.setMax(63)

    # Phase Locked Loop(PLL) Frequency division factor integer part
    oscctrlSym_FRACDIV_INTDIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_FRACDIV_INTDIV", pll_Menu[i])
    oscctrlSym_FRACDIV_INTDIV.setLabel("Frequency division factor integer part")
    oscctrlSym_FRACDIV_INTDIV.setDescription("Frequency division factor integer part")
    oscctrlSym_FRACDIV_INTDIV.setDefaultValue(0)
    oscctrlSym_FRACDIV_INTDIV.setMin(0)
    oscctrlSym_FRACDIV_INTDIV.setMax(32767)

    # Phase Locked Loop(PLL) Frequency division factor reminder part
    oscctrlSym_FRACDIV_REMDIV = coreComponent.createIntegerSymbol(
        "CONFIG_CLOCK_PLL" + str(i) + "_FRACDIV_REMDIV", pll_Menu[i])
    oscctrlSym_FRACDIV_REMDIV.setLabel(
        "Frequency division factor reminder part")
    oscctrlSym_FRACDIV_REMDIV.setDescription(
        "Frequency division factor reminder part")
    oscctrlSym_FRACDIV_REMDIV.setDefaultValue(0)
    oscctrlSym_FRACDIV_REMDIV.setMin(0)
    oscctrlSym_FRACDIV_REMDIV.setMax(511)

    for index in range(0, 4):
        # Phase Locked Loop(PLL) PLLx output n clock division factor
        oscctrlSym_PLLPOSTDIVA_POSTDIV = coreComponent.createIntegerSymbol(
            "CONFIG_CLOCK_PLL" + str(i) + "_PLLPOSTDIVA_POSTDIV" + str(index), pll_Menu[i])
        oscctrlSym_PLLPOSTDIVA_POSTDIV.setLabel("PLL" + str(i) + " output " + str(index) + " clock division factor")
        oscctrlSym_PLLPOSTDIVA_POSTDIV.setDescription("PLL" + str(i) + " output " + str(index) + " clock division factor")
        oscctrlSym_PLLPOSTDIVA_POSTDIV.setDefaultValue(3)
        oscctrlSym_PLLPOSTDIVA_POSTDIV.setMin(1)
        oscctrlSym_PLLPOSTDIVA_POSTDIV.setMax(63)

        # Phase Locked Loop(PLL) PLLx output n enable
        oscctrlSym_PLLPOSTDIVA_OUTEN = coreComponent.createBooleanSymbol(
            "CONFIG_CLOCK_PLL" + str(i) + "_PLLPOSTDIVA_OUTEN" + str(index), pll_Menu[i])
        oscctrlSym_PLLPOSTDIVA_OUTEN.setLabel("PLL" + str(i) + " output " + str(index) + " enable")
        oscctrlSym_PLLPOSTDIVA_OUTEN.setDescription("PLL" + str(i) + " output " + str(index) + " enable")
        oscctrlSym_PLLPOSTDIVA_OUTEN.setDefaultValue(False)

        clkSym_PLL_Freq = coreComponent.createIntegerSymbol(
            "PLL" + str(i) + "_CLOCK_FREQ" + str(index), calculatedFreq_Menu)
        clkSym_PLL_Freq.setReadOnly(True)
        clkSym_PLL_Freq.setDefaultValue(0)
        clkSym_PLL_Freq.setLabel("PLL" + str(i) + " Clock Frequency Output " + str(index))

        clkSym_PLL_Freq.setDependencies(setPLLClockFreq, ["CONFIG_CLOCK_PLL" + str(i) + "_ENABLE",
                                                            "XOSC_FREQ",
                                                            "DFLL_CLOCK_FREQ",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_REF_CLOCK",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_FRACDIV_INTDIV",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_FRACDIV_REMDIV",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_PLLFBDIV_FBDIV",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_PLLREFDIV_REFDIV",
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_PLLPOSTDIVA_POSTDIV" + str(index),
                                                            "CONFIG_CLOCK_PLL" + str(i) + "_PLLPOSTDIVA_OUTEN" + str(index),
                                                            "GCLK_ID_" + str(i + 1) + "_FREQ"
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

dfllStep = coreComponent.createIntegerSymbol(
    "CONFIG_CLOCK_DFLL_STEP", dfll_Menu)
dfllStep.setDefaultValue(1)
dfllStep.setMin(0)
dfllStep.setMax(127)
dfllStep.setLabel("Tune Maximum Step")

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
                                       "CONFIG_CLOCK_DFLL_USB",
                                       "GCLK_ID_0_FREQ"])


################################################################################
##########              Callback Functions            ##########################
################################################################################

####    XOSC32K Configuration Callback Functions    ############################

def setXOSC32KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xoscmode = Database.getSymbolValue("core", "XOSC32K_OSCILLATOR_MODE")
    xosc_in_freq = Database.getSymbolValue("core", "XOSC32K_FREQ_IN")

    if (xosc == True) and (xoscmode == 1):
        symbol.setValue(32768, 1)
    elif (xosc == True) and (xoscmode == 0):
        symbol.setValue(xosc_in_freq, 1)
    elif (xosc == False):
        symbol.setValue(0, 1)


def setXOSC1KFreq(symbol, event):
    xosc = Database.getSymbolValue("core", "CONF_CLOCK_XOSC32K_ENABLE")
    xoscmode = Database.getSymbolValue("core", "XOSC32K_OSCILLATOR_MODE")

    if xosc and (xoscmode == 1):
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

# XOSC32K External Oscillator ONDEMAND Mode
osc32kctrlSym_XOSC32K_ONDEMAND = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_ONDEMAND", xosc32k_Menu)
osc32kctrlSym_XOSC32K_ONDEMAND.setLabel("Oscillator On-Demand Control")
osc32kctrlSym_XOSC32K_ONDEMAND.setDescription(
    "Configures the PLL on Demand Behavior")
osc32kctrlSym_XOSC32K_ONDEMAND.setOutputMode("Key")
osc32kctrlSym_XOSC32K_ONDEMAND.setDisplayMode("Description")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey("DISABLE", str(0), "Always Enable")
osc32kctrlSym_XOSC32K_ONDEMAND.addKey(
    "ENABLE", str(1), "Only on Peripheral Request")
osc32kctrlSym_XOSC32K_ONDEMAND.setDefaultValue(0)

xosc32KGain = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_CGM", xosc32k_Menu)
xosc32KGain.setLabel("Control Gain Mode")
xosc32KGainNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"XOSC32K__CGM\"]")
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

# XOSC32K External Oscillator Enable Servo Loop
osc32kctrlSym_XOSC32K_ENSL = coreComponent.createBooleanSymbol(
    "XOSC32K_ENSL", xosc32k_Menu)
osc32kctrlSym_XOSC32K_ENSL.setLabel("Enable Servo Loop")

# XOSC32K External Oscillator Enable Servo Loop
osc32kctrlSym_XOSC32K_BOOST = coreComponent.createBooleanSymbol(
    "XOSC32K_BOOST", xosc32k_Menu)
osc32kctrlSym_XOSC32K_BOOST.setLabel("Gain Boost")

# XOSC32K External Oscillator 1KHz Output Frequency Mode
clkSym_XOSC1K_Freq = coreComponent.createIntegerSymbol(
    "XOSC1K_FREQ", calculatedFreq_Menu)
clkSym_XOSC1K_Freq.setLabel("XOSC1K Clock Frequency")
clkSym_XOSC1K_Freq.setDefaultValue(0)
clkSym_XOSC1K_Freq.setReadOnly(True)
clkSym_XOSC1K_Freq.setDependencies(setXOSC1KFreq, [
                                   "CONF_CLOCK_XOSC32K_ENABLE", "XOSC32K_OSCILLATOR_MODE"])

# XOSC32K External Oscillator StartUp Time
osc32kctrlSym_XOSC32K_STARTUP = coreComponent.createKeyValueSetSymbol(
    "XOSC32K_STARTUP", xosc32k_Menu)
osc32kctrlSym_XOSC32K_STARTUP.setLabel("Oscillator Startup Time ")
osc32kctrlSym_XOSC32K_STARTUP.setDescription("XOSC start up time ")
osc32kctrlXOSC32KStarupNode = ATDF.getNode(
    "/avr-tools-device-file/modules/module@[name=\"OSC32KCTRL\"]/value-group@[name=\"XOSC32K__STARTUP\"]")
osc32kctrlXOSC32KStarupNodeValues = []
osc32kctrlXOSC32KStarupNodeValues = osc32kctrlXOSC32KStarupNode.getChildren()
for index in range(0, len(osc32kctrlXOSC32KStarupNodeValues)):
    xosc32kstartupKeyName = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("name")
    xosc32kstartupKeyDescription = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("caption")
    xosc32kstartupKeyValue = osc32kctrlXOSC32KStarupNodeValues[index].getAttribute("value")
    osc32kctrlSym_XOSC32K_STARTUP.addKey(xosc32kstartupKeyName, xosc32kstartupKeyValue, xosc32kstartupKeyDescription)
osc32kctrlSym_XOSC32K_STARTUP.setDefaultValue(7)
osc32kctrlSym_XOSC32K_STARTUP.setOutputMode("Value")
osc32kctrlSym_XOSC32K_STARTUP.setDisplayMode("Description")

# RTC Clock Selection
rtcClockSourceSelection = coreComponent.createKeyValueSetSymbol(
    "CONFIG_CLOCK_RTC_SRC", xosc32k_Menu)
rtcClockSourceSelection.setLabel("RTC Clock Selection")
rtcClockSourceSelection.setDescription("Clock Source selection for RTC")

rtcClockSourceSelection.addKey(
    "OSCULP32K", "0", "32 KHz Ultra Low-Power Internal Oscillator (32 KHz Output)")
rtcClockSourceSelection.addKey(
    "OSCULP1K", "1", "32 KHz Ultra Low-Power Internal Oscillator (1 KHz Output)")
rtcClockSourceSelection.addKey(
    "XOSC32K", "2", "32.768 KHz External Crystal Oscillator (32.768 KHz Output)")
rtcClockSourceSelection.addKey(
    "XOSC1K", "3", "32.768 KHz External Crystal Oscillator (1.024 KHz Output)")

rtcClockSourceSelection.setDefaultValue(1)
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

        # XOSC
        if src == "XOSC":
            srcFreq = int(Database.getSymbolValue("core", "XOSC_FREQ"))

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

        # PLL0
        elif src == "PLL0_1":
            srcFreq = int(Database.getSymbolValue("core", "PLL0_CLOCK_FREQ0"))
        elif src == "PLL0_2":
            srcFreq = int(Database.getSymbolValue("core", "PLL0_CLOCK_FREQ1"))
        elif src == "PLL0_3":
            srcFreq = int(Database.getSymbolValue("core", "PLL0_CLOCK_FREQ2"))
        elif src == "PLL0_4":
            srcFreq = int(Database.getSymbolValue("core", "PLL0_CLOCK_FREQ3"))

        # PLL1
        elif src == "PLL1_1":
            srcFreq = int(Database.getSymbolValue("core", "PLL1_CLOCK_FREQ0"))
        elif src == "PLL1_2":
            srcFreq = int(Database.getSymbolValue("core", "PLL1_CLOCK_FREQ1"))
        elif src == "PLL1_3":
            srcFreq = int(Database.getSymbolValue("core", "PLL1_CLOCK_FREQ2"))
        elif src == "PLL1_4":
            srcFreq = int(Database.getSymbolValue("core", "PLL1_CLOCK_FREQ3"))

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
        "PLL0": [],
        "PLL1": [],
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
        "GCLK11": [],
        "GCLK12": [],
        "GCLK13": [],
        "GCLK14": [],
        "GCLK15": []
    }
    symbol.clearValues()
    codeList = []

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_OPMODE"))) == 1 and (Database.getSymbolValue("core", "CONFIG_CLOCK_DFLL_USB") == False)):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_0_GENSEL"))].append("DFLL")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL0_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL0_REF_CLOCK"))) == 0):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_1_GENSEL"))].append("PLL0")

    if (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL1_ENABLE")) == True:
        if((int(Database.getSymbolValue("core", "CONFIG_CLOCK_PLL1_REF_CLOCK"))) == 0):
            sourceDestmap["GCLK" + str(Database.getSymbolValue("core",
                                                               "GCLK_ID_2_GENSEL"))].append("PLL1")

    for i in range(0, 16):
        if Database.getSymbolValue("core", "GCLK_INST_NUM" + str(i)):
            if gclkSym_GENCTRL_SRC[i].getSelectedKey() in ["DFLL", "PLL0", "PLL1", "GCLK1"]:
                sourceDestmap[gclkSym_GENCTRL_SRC[i].getSelectedKey()].append(
                    "GCLK" + str(i))

    codeList = topsort(sourceDestmap)
    if len(codeList) != 0:
        cycleFormed.setValue(False, 2)
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL0_ENABLE")) == False:
            codeList.remove("PLL0")
        if (Database.getSymbolValue("core", "CONFIG_CLOCK_PLL1_ENABLE")) == False:
            codeList.remove("PLL1")
        for i in range(0, 16):
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
gclk_io_signals = [False, False, False, False, False, False, False, False,
                   False, False, False, False, False, False, False, False]  # array to save available signals
pinout = ""
numPads = 0
val = ATDF.getNode("/avr-tools-device-file/variants")
children = val.getChildren()
for index in range(0, len(children)):
    if packageName in children[index].getAttribute("package"):
        pinout = children[index].getAttribute("pinout")

children = []
val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(pinout) + "\"]")
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

for gclknumber in range(0, 16):
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
        "XOSC", "0", "External Crystal Oscillator")

    gclk_in = "GCLK_IN[" + str(gclknumber) + "]"
    gclk_in_desc = "Generator Input Pad (" + \
        "GCLK_IN[" + str(gclknumber) + "])"

    if(gclk_io_signals[gclknumber] == True):
        gclkSym_GENCTRL_SRC[gclknumber].addKey(gclk_in, "1", gclk_in_desc)

    if gclknumber != 1:
        gclkSym_GENCTRL_SRC[gclknumber].addKey(
            "GCLK1", "2", "GCLK Generator 1")

    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "OSCULP32K", "3", "32 KHz Ultra Low-Power Internal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "XOSC32K", "4", "32.768 KHz External Crystal Oscillator")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "DFLL", "5", "DFLL Oscillator Output")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL0_1", "6", "PLL0 Output 1")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL0_2", "7", "PLL0 Output 2")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL0_3", "8", "PLL0 Output 3")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL0_4", "9", "PLL0 Output 4")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL1_1", "10", "PLL1 Output 1")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL1_2", "11", "PLL1 Output 2")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL1_3", "12", "PLL1 Output 3")
    gclkSym_GENCTRL_SRC[gclknumber].addKey(
        "PLL1_4", "13", "PLL1 Output 4")
    gclkSym_GENCTRL_SRC[gclknumber].setDefaultValue(5)
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
        "/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"GENCTRL__DIVSEL\"]")
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
               "XOSC_FREQ",
               "PLL0_CLOCK_FREQ0",
               "PLL0_CLOCK_FREQ1",
               "PLL0_CLOCK_FREQ2",
               "PLL0_CLOCK_FREQ3",
               "PLL1_CLOCK_FREQ0",
               "PLL1_CLOCK_FREQ1",
               "PLL1_CLOCK_FREQ2",
               "PLL1_CLOCK_FREQ3",
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
               "GCLK_IN_11_FREQ",
               "GCLK_IN_12_FREQ",
               "GCLK_IN_13_FREQ",
               "GCLK_IN_14_FREQ",
               "GCLK_IN_15_FREQ"
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
        "/avr-tools-device-file/modules/module@[name=\"GCLK\"]/value-group@[name=\"PCHCTRL__GEN\"]")
    gclkSymPCHCTRLGenNodeValues = []
    gclkSymPCHCTRLGenNodeValues = gclkSymPCHCTRLGenNode.getChildren()

    gclkSymPCHCTRLGenDefaultValue = 0

    for i in range(0, len(gclkSymPCHCTRLGenNodeValues)):
        gclkSymPCHCTRLGenKeyName = gclkSymPCHCTRLGenNodeValues[i].getAttribute(
            "name")

        if (gclkSymPCHCTRLGenKeyName == "GCLK1"):
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
        "GCLK_11_FREQ",
        "GCLK_12_FREQ",
        "GCLK_13_FREQ",
        "GCLK_14_FREQ",
        "GCLK_15_FREQ"])
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
codeGenerationDep.append("CONFIG_CLOCK_PLL0_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_PLL1_REF_CLOCK")
codeGenerationDep.append("CONFIG_CLOCK_PLL0_ENABLE")
codeGenerationDep.append("CONFIG_CLOCK_PLL1_ENABLE")
codeGenerationDep.append("CONFIG_CLOCK_DFLL_USB")
codeGenerationList.setDependencies(codeGen, codeGenerationDep)
codeGenerationList.addValue("   DFLL_Initialize();")
codeGenerationList.addValue("   GCLK0_Initialize();")
codeGenerationList.setTarget("core.CLK_INIT_LIST")

################################################################################
#######          MCLK Database Components            ###########################
################################################################################
mclkSym_CLKDIV = []

for count in range(0, 2):
    # MCLK Clock Divider Control
    mclkSym_CLKDIV.append(count)
    mclkSym_CLKDIV[count] = coreComponent.createKeyValueSetSymbol(
        "CONF_MCLK_CLKDIV" + str(count), mclkSym_Menu)
    mclkSym_CLKDIV[count].setLabel("Clock Domain Division Factor " + str(count))
    mclkcpudivNode = ATDF.getNode(
        "/avr-tools-device-file/modules/module@[name=\"MCLK\"]/value-group@[name=\"CLKDIV__DIV\"]")
    mclkcpudivNodeValues = []
    mclkcpudivNodeValues = mclkcpudivNode.getChildren()
    for index in range(0, len(mclkcpudivNodeValues)):
        mclkcpudivKeyName = mclkcpudivNodeValues[index].getAttribute("name")
        mclkcpudivKeyDescription = mclkcpudivNodeValues[index].getAttribute("caption")
        mclkcpudivKeyValue = mclkcpudivNodeValues[index].getAttribute("value")
        mclkSym_CLKDIV[count].addKey(mclkcpudivKeyName, mclkcpudivKeyValue, mclkcpudivKeyDescription)
    mclkSym_CLKDIV[count].setDefaultValue(0 if (count == 0) else 1)
    mclkSym_CLKDIV[count].setOutputMode("Value")
    mclkSym_CLKDIV[count].setDisplayMode("Key")

################################################################################
#######          Calculated Clock Frequencies        ###########################
################################################################################


def setMainClockFreq(symbol, event):
    divider = int(Database.getSymbolValue("core", "CONF_MCLK_CLKDIV0"))
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
    setMainClockFreq, ["GCLK_0_FREQ", "CONF_MCLK_CLKDIV0"])

divider = mclkSym_CLKDIV[0].getValue()
gclk0_freq = int(gclkSym_Freq[0].getValue())
clkSym_MAIN_CLK_FREQ.setValue(gclk0_freq / (divider + 1), 1)

clkMclkFreq = coreComponent.createIntegerSymbol("MAIN_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkMclkFreq.setLabel("Main Clock Frequency")
clkMclkFreq.setReadOnly(True)
clkMclkFreq.setDefaultValue(int(gclkSym_Freq[0].getValue()))

peripherals = ATDF.getNode("/avr-tools-device-file/devices/device@[name=\"" + Variables.get("__PROCESSOR") + "\"]/peripherals")
module_list = peripherals.getChildren()

clkSym_WDT_CLK_FREQ = coreComponent.createIntegerSymbol("WDT_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_WDT_CLK_FREQ.setLabel("WDT Clock Frequency")
clkSym_WDT_CLK_FREQ.setReadOnly(True)
clkSym_WDT_CLK_FREQ.setDefaultValue(1024)

clkSym_RTC_CLK_FREQ = coreComponent.createIntegerSymbol("RTC_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_RTC_CLK_FREQ.setLabel("RTC Clock Frequency")
clkSym_RTC_CLK_FREQ.setReadOnly(True)
clkSym_RTC_CLK_FREQ.setDefaultValue(1024)
clkSym_RTC_CLK_FREQ.setDependencies(setFreq, ["CONFIG_CLOCK_RTC_SRC", "OSCULP32K_FREQ", "OSCULP1K_FREQ", "XOSC32K_FREQ", "XOSC1K_FREQ"])

#########################Default Clock##########################################
gclkSym_num[1].setValue(True)
gclkSym_GENCTRL_SRC[1].setSelectedKey("PLL0_1")
gclkSym_GENCTRL_DIV[1].setValue(2)
Database.setSymbolValue("core", "CONFIG_CLOCK_PLL0_ENABLE", True)
Database.setSymbolValue("core", "CONFIG_CLOCK_PLL0_PLLPOSTDIVA_OUTEN0", True)
gclkSym_GENCTRL_SRC[0].setSelectedKey("PLL0_1")
################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clockSym_OSCCTRL_HeaderFile = coreComponent.createFileSymbol(
    "CLOCK_HEADER_FILE", None)
clockSym_OSCCTRL_HeaderFile.setSourcePath(
    "../peripheral/clk_pic32cz_ca/templates/plib_clock.h.ftl")
clockSym_OSCCTRL_HeaderFile.setOutputName("plib_clock.h")
clockSym_OSCCTRL_HeaderFile.setDestPath("peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setProjectPath(
    "config/" + configName + "/peripheral/clock/")
clockSym_OSCCTRL_HeaderFile.setType("HEADER")
clockSym_OSCCTRL_HeaderFile.setMarkup(True)

clockSym_OSCCTRL_SourceFile = coreComponent.createFileSymbol(
    "CLOCK_SOURCE_FILE", None)
clockSym_OSCCTRL_SourceFile.setSourcePath(
    "../peripheral/clk_pic32cz_ca/templates/plib_clock.c.ftl")
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
    "../peripheral/clk_pic32cz_ca/templates/system/initialization.c.ftl")
clockSystemInitFile.setMarkup(True)

clockSystemDefFile = coreComponent.createFileSymbol("CLOCK_SYS_DEF", None)
clockSystemDefFile.setType("STRING")
clockSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clockSystemDefFile.setSourcePath(
    "../peripheral/clk_pic32cz_ca/templates/system/definitions.h.ftl")
clockSystemDefFile.setMarkup(True)
