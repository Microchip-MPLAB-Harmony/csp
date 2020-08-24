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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateCompareMenuVisibleProperty(symbol, event):
    if event["value"] == "Compare":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateCompareMaxValue(symbol, event):
    if event["value"] == 0x1:
        symbol.setMax(255)
    elif event["value"] == 0x0:
        symbol.setMax(65535)
    elif event["value"] == 0x2:
        symbol.setMax(4294967295)

global getMaxValue
def getMaxValue(bit):
    if bit == 0x1:
        return (255)
    elif bit == 0x0:
        return (65535)
    elif bit == 0x2:
        return (4294967295)

def updatePeriod(symbol, event):
    mode = tcSym_CTRLA_MODE.getValue()
    max = getMaxValue(tcSym_CTRLA_MODE.getValue())
    symbol.setMax(max)
    wave = tcSym_Compare_WAVE_WAVEGEN.getValue()
    if mode == 1:  #8-bit
        if  wave == 0 or wave == 2: #normal
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def updateCompare0(symbol, event):
    max = getMaxValue(tcSym_CTRLA_MODE.getValue())
    wave = tcSym_Compare_WAVE_WAVEGEN.getValue()

    if wave == 1 or wave == 3: #Match modes
        symbol.setLabel("Compare 0 Value (Period)")
        symbol.setMax(max)
    else:
        symbol.setLabel("Compare 0 Value")
        if (tcSym_CTRLA_MODE.getValue() == 1):
            symbol.setMax(tcSym_ComparePeriod.getValue())
        else:
            symbol.setMax(max)


def updateCompare1(symbol, event):
    max = getMaxValue(tcSym_CTRLA_MODE.getValue())
    wave = tcSym_Compare_WAVE_WAVEGEN.getValue()
    #hide compare value for Match frequency waveform mode
    if wave == 1:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

    if wave == 0 or wave == 2: #normal modes
        if (tcSym_CTRLA_MODE.getValue() == 1):
            symbol.setMax(tcSym_ComparePeriod.getValue())
        else:
            symbol.setMax(max)
    else:
        symbol.setMax(tcSym_CompareDuty0.getValue())

def topSymbolChange(symbol, event):
    max = getMaxValue(tcSym_CTRLA_MODE.getValue())
    wave = tcSym_Compare_WAVE_WAVEGEN.getValue()
    if (wave == 0 or wave == 2): #normal modes
        if (tcSym_CTRLA_MODE.getValue() != 1):
            symbol.setVisible(True)
            symbol.setLabel("**** Period Value is " + str(hex(max)) + " ****")
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)

def tcComparePeriodCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / clock_freq
    max = getMaxValue(tcSym_CTRLA_MODE.getValue())
    mode = tcSym_CTRLA_MODE.getValue()
    wave = tcSym_Compare_WAVE_WAVEGEN.getValue()

    if (wave == 1 or wave == 3):
        period = tcSym_CompareDuty0.getValue()
    else:
        if mode == 1:
            period = tcSym_ComparePeriod.getValue()
        else:
            period = max

    time = period * resolution
    symbol.setLabel("**** Compare Period is " + str(time) + " us ****")

def tcEventVisible(symbol, event):
    if event["value"] == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcCompareEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TC_OPERATION_MODE"):
        evsysVal_ovf = Database.getSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE")
        tcVal_ovf = component.getSymbolValue("TC_COMPARE_EVCTRL_OVFEO")
        evsysVal_mc0 = Database.getSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_0_ACTIVE")
        tcVal_mc0 = component.getSymbolValue("TC_COMPARE_EVCTRL_MCEO0")
        evsysVal_mc1 = Database.getSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE")
        tcVal_mc1 = component.getSymbolValue("TC_COMPARE_EVCTRL_MCEO1")
        evsysVal_evu = Database.getSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY")
        tcVal_evu = component.getSymbolValue("TC_COMPARE_EVCTRL_EV")
        if (event["value"] == "Compare"):
            if (evsysVal_ovf != tcVal_ovf):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", tcVal_ovf, 2)
            if (evsysVal_mc0 != tcVal_mc0):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_0_ACTIVE", tcVal_mc0, 2)
            if (evsysVal_mc1 != tcVal_mc1):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", tcVal_mc1, 2)
            if ((evsysVal_evu) != tcVal_evu):
                Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", bool(tcVal_evu), 2)
        else:
            if(evsysVal_ovf == True and component.getSymbolValue("TC_TIMER_EVCTRL_OVFEO") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            if(evsysVal_mc0 == True and component.getSymbolValue("TC_CAPTURE_EVCTRL_MCEO0") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_0_ACTIVE", False, 2)
            if(evsysVal_mc1 == True and component.getSymbolValue("TC_CAPTURE_EVCTRL_MCEO1") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", False, 2)
            if (evsysVal_evu == True and event["value"] != "Capture"
                    and component.getSymbolValue("TC_TIMER_EVCTRL_EV") == False):
                Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", False, 2)
    else:
        if(event["id"] == "TC_COMPARE_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)
        if(event["id"] == "TC_COMPARE_EVCTRL_MCEO0"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_0_ACTIVE", event["value"], 2)
        if(event["id"] == "TC_COMPARE_EVCTRL_MCEO1"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", event["value"], 2)
        if(event["id"] == "TC_COMPARE_EVCTRL_EV"):
            Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", event["value"], 2)

def tcCompareEVACTVisible(symbol, event):
    symbol.setVisible(event["value"])

def tcCompareInterrupt(symbol, event):
    component = symbol.getComponent()
    ovf = component.getSymbolValue("TC_COMPARE_INTENSET_OVF")
    mc0 = component.getSymbolValue("TC_COMPARE_INTENSET_MC0")
    mc1 = component.getSymbolValue("TC_COMPARE_INTENSET_MC1")
    if (ovf or mc0 or mc1):
        symbol.setValue(True)
    else:
        symbol.setValue(False)

###################################################################################################
####################################### Compare Mode ##############################################
###################################################################################################

#compare menu
tcSym_CompareMenu = tcComponent.createMenuSymbol("TC_COMPARE_MENU", tcSym_OperationMode)
tcSym_CompareMenu.setLabel("Compare")
tcSym_CompareMenu.setVisible(False)
tcSym_CompareMenu.setDependencies(updateCompareMenuVisibleProperty, ["TC_OPERATION_MODE"])

#waveform mode
global tcSym_Compare_WAVE_WAVEGEN
tcSym_Compare_WAVE_WAVEGEN = tcComponent.createKeyValueSetSymbol("TC_COMPARE_CTRLA_WAVEGEN", tcSym_CompareMenu)
tcSym_Compare_WAVE_WAVEGEN.setLabel("Waveform Mode")
tc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CTRLA__WAVEGEN\"]")
childrenNodes = tc.getChildren()
for param in range(0, len(childrenNodes)):
    tcSym_Compare_WAVE_WAVEGEN.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"),
        childrenNodes[param].getAttribute("caption"))
tcSym_Compare_WAVE_WAVEGEN.setDefaultValue(1)
tcSym_Compare_WAVE_WAVEGEN.setOutputMode("Key")
tcSym_Compare_WAVE_WAVEGEN.setDisplayMode("Key")

#compare direction
tcSym_Compare_CTRLBSET_DIR = tcComponent.createKeyValueSetSymbol("TC_COMPARE_CTRLBSET_DIR", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_DIR.setLabel("Counter Direction")
tcSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_UP", "0", "UP Count")
tcSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_DOWN", "1", "DOWN Count")
tcSym_Compare_CTRLBSET_DIR.setDefaultValue(0)
tcSym_Compare_CTRLBSET_DIR.setOutputMode("Value")
tcSym_Compare_CTRLBSET_DIR.setDisplayMode("Description")

#compare period
global tcSym_ComparePeriod
tcSym_ComparePeriod = tcComponent.createLongSymbol("TC_COMPARE_PERIOD", tcSym_CompareMenu)
tcSym_ComparePeriod.setLabel("Period Value")
tcSym_ComparePeriod.setDefaultValue(65535)
tcSym_ComparePeriod.setMin(0)
tcSym_ComparePeriod.setMax(65535)
tcSym_ComparePeriod.setVisible(False)
tcSym_ComparePeriod.setDependencies(updatePeriod, ["TC_CTRLA_MODE", "TC_COMPARE_CTRLA_WAVEGEN"])

tcSym_CompareTopComment = tcComponent.createCommentSymbol("TC_COMPARE_TOP", tcSym_CompareMenu)
tcSym_CompareTopComment.setLabel("**** Period Value is 0xFFFF ****")
tcSym_CompareTopComment.setVisible(False)
tcSym_CompareTopComment.setDependencies(topSymbolChange, ["TC_CTRLA_MODE", "TC_COMPARE_CTRLA_WAVEGEN"])

#compare value
global tcSym_CompareDuty0
tcSym_CompareDuty0 = tcComponent.createLongSymbol("TC_COMPARE_CC0", tcSym_CompareMenu)
tcSym_CompareDuty0.setLabel("Compare 0 Value (Period)")
tcSym_CompareDuty0.setDefaultValue(24)
tcSym_CompareDuty0.setMin(0)
tcSym_CompareDuty0.setMax(tcSym_ComparePeriod.getValue())
tcSym_CompareDuty0.setDependencies(updateCompare0, ["TC_COMPARE_CTRLA_WAVEGEN", "TC_COMPARE_PERIOD", "TC_COMPARE_TOP",
                                    "TC_CTRLA_MODE"])

#compare value
tcSym_CompareDuty = tcComponent.createLongSymbol("TC_COMPARE_CC1", tcSym_CompareMenu)
tcSym_CompareDuty.setLabel("Compare 1 Value")
tcSym_CompareDuty.setDefaultValue(24)
tcSym_CompareDuty.setMin(0)
tcSym_CompareDuty.setMax(tcSym_ComparePeriod.getValue())
tcSym_CompareDuty.setVisible(False)
tcSym_CompareDuty.setDependencies(updateCompare1, ["TC_COMPARE_CTRLA_WAVEGEN", "TC_COMPARE_PERIOD",
                    "TC_CTRLA_MODE", "TC_COMPARE_CC0"])

#period time in us
clk_freq = Database.getSymbolValue("core", tcInstanceName.getValue() + "_CLOCK_FREQUENCY")
if clk_freq == 0:
    clk_freq = 1
resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / clk_freq
time = tcSym_CompareDuty0.getValue() * resolution
tcSym_ComparePeriod_Comment = tcComponent.createCommentSymbol("TC_COMPARE_PERIOD_COMMENT", tcSym_CompareMenu)
tcSym_ComparePeriod_Comment.setLabel("**** Compare Period is " + str(time) + " us ****")
tcSym_ComparePeriod_Comment.setDependencies(tcComparePeriodCalc, ["TC_COMPARE_PERIOD", "TC_CTRLA_PRESCALER",\
    "core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", "TC_COMPARE_CTRLA_WAVEGEN", "TC_CTRLA_MODE", "TC_COMPARE_CC0"])


#compare one shot mode
tcSym_Compare_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLBSET_ONESHOT", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

tcSym_Compare_DRVCTRL_INVEN0 = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLC_INVEN0", tcSym_CompareMenu)
tcSym_Compare_DRVCTRL_INVEN0.setLabel("Invert Output WO[0]")
tcSym_Compare_DRVCTRL_INVEN0.setDefaultValue(False)

tcSym_Compare_DRVCTRL_INVEN1 = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLC_INVEN1", tcSym_CompareMenu)
tcSym_Compare_DRVCTRL_INVEN1.setLabel("Invert Output WO[1]")
tcSym_Compare_DRVCTRL_INVEN1.setDefaultValue(False)

#compare channel counter/compare interrupt
global tcSym_Compare_INTENSET_OVF
tcSym_Compare_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_COMPARE_INTENSET_OVF", tcSym_CompareMenu)
tcSym_Compare_INTENSET_OVF.setLabel("Enable Period Interrupt")
tcSym_Compare_INTENSET_OVF.setDefaultValue(False)

tcSym_Compare_INTENSET_MC0 = tcComponent.createBooleanSymbol("TC_COMPARE_INTENSET_MC0", tcSym_CompareMenu)
tcSym_Compare_INTENSET_MC0.setLabel("Enable Compare Match 0 Interrupt")
tcSym_Compare_INTENSET_MC0.setDefaultValue(False)

tcSym_Compare_INTENSET_MC1 = tcComponent.createBooleanSymbol("TC_COMPARE_INTENSET_MC1", tcSym_CompareMenu)
tcSym_Compare_INTENSET_MC1.setLabel("Enable Compare Match 1 Interrupt")
tcSym_Compare_INTENSET_MC1.setDefaultValue(False)

global tcSym_Compare_InterruptMode
tcSym_Compare_InterruptMode = tcComponent.createBooleanSymbol("TC_COMPARE_INTERRUPT_MODE", tcSym_CompareMenu)
tcSym_Compare_InterruptMode.setVisible(False)
tcSym_Compare_InterruptMode.setDefaultValue(False)
tcSym_Compare_InterruptMode.setDependencies(tcCompareInterrupt, ["TC_COMPARE_INTENSET_OVF", "TC_COMPARE_INTENSET_MC0", "TC_COMPARE_INTENSET_MC1"])

tcSym_Compare_Events_Menu = tcComponent.createMenuSymbol("TC_COMPARE_EVENT_MENU", tcSym_CompareMenu)
tcSym_Compare_Events_Menu.setLabel("Events")

tcSym_Compare_EVCTRL_OVFEO = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_OVFEO", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_OVFEO.setLabel("Enable Compare Period Overflow Event")
tcSym_Compare_EVCTRL_OVFEO.setDefaultValue(False)

tcSym_Compare_EVCTRL_MCEO0 = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_MCEO0", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_MCEO0.setLabel("Enable Compare Match 0 Output Event")
tcSym_Compare_EVCTRL_MCEO0.setDefaultValue(False)

tcSym_Compare_EVCTRL_MCEO1 = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_MCEO1", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_MCEO1.setLabel("Enable Compare Match 1 Output Event")
tcSym_Compare_EVCTRL_MCEO1.setDefaultValue(False)
#tcSym_Compare_EVCTRL_MCEO1.setDependencies(tcEventVisible, ["TC_COMPARE_CTRLA_WAVEGEN"])

tcSym_Compare_EVCTRL_EV = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_EV", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_EV.setLabel("Enable Compare Input Event")
tcSym_Compare_EVCTRL_EV.setDefaultValue(False)

tcSym_Compare_EVCTRL_EVACT = tcComponent.createKeyValueSetSymbol("TC_COMPARE_EVCTRL_EVACT", tcSym_Compare_EVCTRL_EV)
tcSym_Compare_EVCTRL_EVACT.setLabel("Select Input Event Action")
tcSym_Compare_EVCTRL_EVACT.setVisible(False)
tcSym_Compare_EVCTRL_EVACT.addKey("START", "0", "Start Compare")
tcSym_Compare_EVCTRL_EVACT.addKey("RETRIGGER", "1", "Retrigger Compare")
tcSym_Compare_EVCTRL_EVACT.addKey("COUNT", "2", "Count on Event")
tcSym_Compare_EVCTRL_EVACT.setDependencies(tcCompareEVACTVisible, ["TC_COMPARE_EVCTRL_EV"])

tcSym_Compare_EVCTRL_TCINV = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_TCINV", tcSym_Compare_EVCTRL_EV)
tcSym_Compare_EVCTRL_TCINV.setLabel("Invert Input Event")
tcSym_Compare_EVCTRL_TCINV.setVisible(False)
tcSym_Compare_EVCTRL_TCINV.setDependencies(tcEVACTVisible, ["TC_COMPARE_EVCTRL_EV"])

tcSym_Compare_EVESYS_CONFIGURE = tcComponent.createIntegerSymbol("TC_COMPARE_EVSYS_CONFIGURE", tcSym_Compare_Events_Menu)
tcSym_Compare_EVESYS_CONFIGURE.setVisible(False)
tcSym_Compare_EVESYS_CONFIGURE.setDependencies(tcCompareEvsys, ["TC_OPERATION_MODE",
"TC_COMPARE_EVCTRL_OVFEO", "TC_COMPARE_EVCTRL_MCEO0", "TC_COMPARE_EVCTRL_MCEO1", "TC_COMPARE_EVCTRL_EV"])
