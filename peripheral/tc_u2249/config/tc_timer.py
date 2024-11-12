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

""" This module will instantiate and setup TC component """

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

global calcAchievableFreq
global tcTimerUnit
tcTimerUnit = { "millisecond" : 1,
                "microsecond" : 1000, 
                "nanosecond"  : 1000000,
                }

def updateTimerMenuVisibleProperty(symbol, event):
    if event["value"] == "Timer":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcTimeMaxValue(symbol, event):
    clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    resolution = (prescaler * 1000.0) / clock_freq  #mSec
    mode = tcSym_CTRLA_MODE.getValue()
    unit = tcTimerUnit[tcSym_TimerUnit.getValue()]

    max = 0.0
    if (mode == 0):
        max = (65536.0 * resolution * unit)
    elif (mode == 1):
        max = (256.0 * resolution * unit)
    elif (mode == 2):
        max = (4294967296.0 * resolution * unit)
    symbol.setMax(max)

def tcPeriodCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    resolution = (prescaler * 1000.0) / clock_freq   #mSec
    time = tcSym_Timer_TIME_MS.getValue()
    unit = tcTimerUnit[tcSym_TimerUnit.getValue()]
    period = (time / (resolution * unit)) - 1
    symbol.setValue(long(period), 2)
    symbol.setMax(pow(2, int(tcSym_CTRLA_MODE.getSelectedKey()[5:])) - 1)

    calcAchievableFreq()

def tcTimerEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TC_OPERATION_MODE"):
        evsysVal = Database.getSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE")
        tcVal = component.getSymbolValue("TC_TIMER_EVCTRL_OVFEO")
        evsysVal_evu = Database.getSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY")
        tcVal_evu = component.getSymbolValue("TC_TIMER_EVCTRL_EV")
        if (event["value"] == "Timer"):
            if (evsysVal != tcVal):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", tcVal, 2)
            if ((evsysVal_evu) != tcVal_evu):
                Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", bool(tcVal_evu), 2)
        else:
            if(evsysVal == True and component.getSymbolValue("TC_COMPARE_EVCTRL_OVFEO") == False):
                Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            if (evsysVal_evu == True and component.getSymbolValue("TC_CAPTURE_CTRLA_COPEN0") != 1
                    and component.getSymbolValue("TC_COMPARE_EVCTRL_EV") == False):
                Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", False, 2)
    else:
        if(event["id"] == "TC_TIMER_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)
        if(event["id"] == "TC_TIMER_EVCTRL_EV"):
            Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", event["value"], 2)

def tcEVACTVisible(symbol, event):
    symbol.setVisible(event["value"])
###################################################################################################
######################################### Timer Mode ##############################################
###################################################################################################

#timer menu
tcSym_TimerMenu = tcComponent.createMenuSymbol("TC_TIMER_MENU", tcSym_OperationMode)
tcSym_TimerMenu.setLabel("Timer")
tcSym_TimerMenu.setDependencies(updateTimerMenuVisibleProperty, ["TC_OPERATION_MODE"])

#timer one shot mode
tcSym_Timer_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_TIMER_CTRLBSET_ONESHOT", tcSym_TimerMenu)
tcSym_Timer_CTRLBSET_ONESHOT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:CTRLBSET")
tcSym_Timer_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

global tcSym_TimerUnit
timerUnit = ["millisecond", "microsecond", "nanosecond"]
tcSym_TimerUnit = tcComponent.createComboSymbol("TC_TIMER_UNIT", tcSym_TimerMenu, timerUnit)
tcSym_TimerUnit.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:%NOREGISTER%")
tcSym_TimerUnit.setLabel("Timer Period Unit")
tcSym_TimerUnit.setDefaultValue("millisecond")

#time in float
global tcSym_Timer_TIME_MS
clock_freq = Database.getSymbolValue("core", tcInstanceName.getValue() + "_CLOCK_FREQUENCY")
if clock_freq == 0:
    clock_freq = 1
resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000000.0) / clock_freq
max = (65536.0 * resolution / 1000000)
tcSym_Timer_TIME_MS = tcComponent.createFloatSymbol("TC_TIMER_TIME_MS", tcSym_TimerMenu)
tcSym_Timer_TIME_MS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:%NOREGISTER%")
tcSym_Timer_TIME_MS.setLabel("Time")
tcSym_Timer_TIME_MS.setDefaultValue(1)
tcSym_Timer_TIME_MS.setMin(0.0)
tcSym_Timer_TIME_MS.setMax(max)
tcSym_Timer_TIME_MS.setDependencies(tcTimeMaxValue, ["TC_CTRLA_MODE", "core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
    "TC_CTRLA_PRESCALER", "TC_TIMER_UNIT"])

#timer period
global tcSym_TimerPeriod
period = (tcSym_Timer_TIME_MS.getValue() * 1000000 / resolution) - 1
tcSym_TimerPeriod = tcComponent.createLongSymbol("TC_TIMER_PERIOD", tcSym_Timer_TIME_MS)
tcSym_TimerPeriod.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:CC")
tcSym_TimerPeriod.setLabel("Timer Period")
tcSym_TimerPeriod.setVisible(True)
tcSym_TimerPeriod.setReadOnly(True)
tcSym_TimerPeriod.setDefaultValue(long(period))
tcSym_TimerPeriod.setMin(0)
tcSym_TimerPeriod.setMax((2**32) - 1)
tcSym_TimerPeriod.setDependencies(tcPeriodCalc, ["TC_CTRLA_MODE", "core."+tcInstanceName.getValue()+"_CLOCK_FREQUENCY", \
    "TC_CTRLA_PRESCALER", "TC_TIMER_TIME_MS", "TC_TIMER_UNIT"])

#timer interrupt mode
global tcSym_Timer_INTENSET_OVF
tcSym_Timer_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_TIMER_INTENSET_OVF", tcSym_TimerMenu)
tcSym_Timer_INTENSET_OVF.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:INTENSET")
tcSym_Timer_INTENSET_OVF.setLabel("Enable Timer Period Interrupt")
tcSym_Timer_INTENSET_OVF.setDefaultValue(True)

tcSym_TimerEventMenu = tcComponent.createMenuSymbol("TC_TIMER_EVENT_MENU", tcSym_TimerMenu)
tcSym_TimerEventMenu.setLabel("Events")

tcSym_Timer_EVCTRL_OVFEO = tcComponent.createBooleanSymbol("TC_TIMER_EVCTRL_OVFEO", tcSym_TimerEventMenu)
tcSym_Timer_EVCTRL_OVFEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:EVCTRL")
tcSym_Timer_EVCTRL_OVFEO.setLabel("Enable Timer Period Overflow Event")
tcSym_Timer_EVCTRL_OVFEO.setDefaultValue(False)

tcSym_Timer_EVCTRL_EV = tcComponent.createBooleanSymbol("TC_TIMER_EVCTRL_EV", tcSym_TimerEventMenu)
tcSym_Timer_EVCTRL_EV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:EVCTRL")
tcSym_Timer_EVCTRL_EV.setLabel("Enable Timer Input Event")
tcSym_Timer_EVCTRL_EV.setDefaultValue(False)

tcSym_Timer_EVCTRL_EVACT = tcComponent.createKeyValueSetSymbol("TC_TIMER_EVCTRL_EVACT", tcSym_Timer_EVCTRL_EV)
tcSym_Timer_EVCTRL_EVACT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:EVCTRL")
tcSym_Timer_EVCTRL_EVACT.setLabel("Select Input Event Action")
tcSym_Timer_EVCTRL_EVACT.setVisible(False)
tcSym_Timer_EVCTRL_EVACT.addKey("START", "0", "Start Timer")
tcSym_Timer_EVCTRL_EVACT.addKey("RETRIGGER", "1", "Retrigger Timer")
tcSym_Timer_EVCTRL_EVACT.addKey("COUNT", "2", "Count on Event")
tcSym_Timer_EVCTRL_EVACT.setDependencies(tcEVACTVisible, ["TC_TIMER_EVCTRL_EV"])

tcSym_Timer_EVCTRL_TCINV = tcComponent.createBooleanSymbol("TC_TIMER_EVCTRL_TCINV", tcSym_Timer_EVCTRL_EV)
tcSym_Timer_EVCTRL_TCINV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:EVCTRL")
tcSym_Timer_EVCTRL_TCINV.setLabel("Invert Input Event")
tcSym_Timer_EVCTRL_TCINV.setVisible(False)
tcSym_Timer_EVCTRL_TCINV.setDependencies(tcEVACTVisible, ["TC_TIMER_EVCTRL_EV"])

global tcSym_Timer_INTENSET_MC1
tcSym_Timer_INTENSET_MC1 = tcComponent.createBooleanSymbol("TC_TIMER_INTENSET_MC1", tcSym_TimerMenu)
tcSym_Timer_INTENSET_MC1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tc_u2249;register:INTENSET")
tcSym_Timer_INTENSET_MC1.setLabel("Enable Timer Compare Interrupt")
tcSym_Timer_INTENSET_MC1.setVisible(False)
tcSym_Timer_INTENSET_MC1.setDefaultValue(False)

tcSym_Timer_EVSYS_CONFIGURE = tcComponent.createIntegerSymbol("TC_TIMER_EVSYS_CONFIGURE", tcSym_TimerMenu)
tcSym_Timer_EVSYS_CONFIGURE.setVisible(False)
tcSym_Timer_EVSYS_CONFIGURE.setDependencies(tcTimerEvsys, ["TC_OPERATION_MODE", "TC_TIMER_EVCTRL_OVFEO", "TC_TIMER_EVCTRL_EV"])
