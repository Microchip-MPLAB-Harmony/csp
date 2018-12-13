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

def updateCompareDuty(symbol, event):
    if event["id"] == "TC_COMPARE_PERIOD":
        symbol.setMax(event["value"])

    #hide compare value for Match frequency waveform mode
    if event["id"] == "TC_COMPARE_WAVE_WAVEGEN":
        if event["value"] == 1:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def tcComparePeriodCalc(symbol, event):
    resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    time = tcSym_ComparePeriod.getValue() * resolution
    symbol.setLabel("**** Timer Period is " + str(time) + " us ****")

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
        evsysVal_mc1 = Database.getSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE")
        tcVal_mc1 = component.getSymbolValue("TC_COMPARE_EVCTRL_MCEO1")
        if (event["value"] == "Compare"):
            if (evsysVal_ovf != tcVal_ovf):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", tcVal_ovf, 2)
            if (evsysVal_mc1 != tcVal_mc1):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", tcVal_mc1, 2)
        else:
            if(evsysVal_ovf == True and component.getSymbolValue("TC_TIMER_EVCTRL_OVFEO") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            if(evsysVal_mc1 == True and component.getSymbolValue("TC_CAPTURE_EVCTRL_MCEO1") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", False, 2)
    else:
        if(event["id"] == "TC_COMPARE_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)
        if(event["id"] == "TC_COMPARE_EVCTRL_MCEO1"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", event["value"], 2)
###################################################################################################
####################################### Compare Mode ##############################################
###################################################################################################

#compare menu
tcSym_CompareMenu = tcComponent.createMenuSymbol("TC_COMPARE_MENU", tcSym_OperationMode)
tcSym_CompareMenu.setLabel("Compare")
tcSym_CompareMenu.setVisible(False)
tcSym_CompareMenu.setDependencies(updateCompareMenuVisibleProperty, ["TC_OPERATION_MODE"])

#waveform mode
tcSym_Compare_WAVE_WAVEGEN = tcComponent.createKeyValueSetSymbol("TC_COMPARE_WAVE_WAVEGEN", tcSym_CompareMenu)
tcSym_Compare_WAVE_WAVEGEN.setLabel("Waveform Mode")
tcSym_Compare_WAVE_WAVEGEN.addKey("MFRQ", "1", "Match Frequency")
tcSym_Compare_WAVE_WAVEGEN.addKey("MPWM", "3", "Match PWM")
tcSym_Compare_WAVE_WAVEGEN.setDefaultValue(1)
tcSym_Compare_WAVE_WAVEGEN.setOutputMode("Key")
tcSym_Compare_WAVE_WAVEGEN.setDisplayMode("Description")

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
tcSym_ComparePeriod.setDefaultValue(48)
tcSym_ComparePeriod.setMin(0)
tcSym_ComparePeriod.setMax(65535)
tcSym_ComparePeriod.setDependencies(updateCompareMaxValue, ["TC_CTRLA_MODE"])

#period time in us
resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
time = tcSym_ComparePeriod.getValue() * resolution
tcSym_ComparePeriod_Comment = tcComponent.createCommentSymbol("TC_COMPARE_PERIOD_COMMENT", tcSym_CompareMenu)
tcSym_ComparePeriod_Comment.setLabel("**** Timer Period is " + str(time) + " us ****")
tcSym_ComparePeriod_Comment.setDependencies(tcComparePeriodCalc, ["TC_COMPARE_PERIOD", "TC_CTRLA_PRESCALER",\
    "core.CPU_CLOCK_FREQUENCY"])

#compare value
tcSym_CompareDuty = tcComponent.createLongSymbol("TC_COMPARE_CC1", tcSym_CompareMenu)
tcSym_CompareDuty.setLabel("Compare Value")
tcSym_CompareDuty.setDefaultValue(24)
tcSym_CompareDuty.setMin(0)
tcSym_CompareDuty.setMax(tcSym_ComparePeriod.getValue())
tcSym_CompareDuty.setDependencies(updateCompareDuty, ["TC_COMPARE_WAVE_WAVEGEN", "TC_COMPARE_PERIOD"])

#compare one shot mode
tcSym_Compare_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLBSET_ONESHOT", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

#double buffering
tcSym_Compare_CTRLBSET_LUPD = tcComponent.createBooleanSymbol("TC_COMPARE_CTRLBSET_LUPD", tcSym_CompareMenu)
tcSym_Compare_CTRLBSET_LUPD.setLabel("Enable Double Buffering")
tcSym_Compare_CTRLBSET_LUPD.setDefaultValue(True)

tcSym_Compare_DRVCTRL_INVEN0 = tcComponent.createBooleanSymbol("TC_COMPARE_DRVCTRL_INVEN0", tcSym_CompareMenu)
tcSym_Compare_DRVCTRL_INVEN0.setLabel("Invert Output WO[0]")
tcSym_Compare_DRVCTRL_INVEN0.setDefaultValue(False)

tcSym_Compare_DRVCTRL_INVEN1 = tcComponent.createBooleanSymbol("TC_COMPARE_DRVCTRL_INVEN1", tcSym_CompareMenu)
tcSym_Compare_DRVCTRL_INVEN1.setLabel("Invert Output WO[1]")
tcSym_Compare_DRVCTRL_INVEN1.setDefaultValue(False)
tcSym_Compare_DRVCTRL_INVEN1.setDependencies(tcEventVisible, ["TC_COMPARE_WAVE_WAVEGEN"])

#compare channel counter/compare interrupt
global tcSym_Compare_INTENSET_OVF
tcSym_Compare_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_COMPARE_INTENSET_OVF", tcSym_CompareMenu)
tcSym_Compare_INTENSET_OVF.setLabel("Enable Period Interrupt")
tcSym_Compare_INTENSET_OVF.setDefaultValue(False)

tcSym_Compare_Events_Menu = tcComponent.createMenuSymbol("TC_COMPARE_EVENT_MENU", tcSym_CompareMenu)
tcSym_Compare_Events_Menu.setLabel("Events")

tcSym_Compare_EVCTRL_OVFEO = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_OVFEO", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_OVFEO.setLabel("Enable Timer Period Overflow Event")
tcSym_Compare_EVCTRL_OVFEO.setDefaultValue(False)

tcSym_Compare_EVCTRL_MCEO1 = tcComponent.createBooleanSymbol("TC_COMPARE_EVCTRL_MCEO1", tcSym_Compare_Events_Menu)
tcSym_Compare_EVCTRL_MCEO1.setLabel("Enable Compare Match 1 Event")
tcSym_Compare_EVCTRL_MCEO1.setDefaultValue(False)
tcSym_Compare_EVCTRL_MCEO1.setDependencies(tcEventVisible, ["TC_COMPARE_WAVE_WAVEGEN"])

tcSym_Compare_EVESYS_CONFIGURE = tcComponent.createIntegerSymbol("TC_COMPARE_EVSYS_CONFIGURE", tcSym_Compare_Events_Menu)
tcSym_Compare_EVESYS_CONFIGURE.setVisible(False)
tcSym_Compare_EVESYS_CONFIGURE.setDependencies(tcCompareEvsys, ["TC_OPERATION_MODE", "TC_COMPARE_EVCTRL_OVFEO", "TC_COMPARE_EVCTRL_MCEO1"])