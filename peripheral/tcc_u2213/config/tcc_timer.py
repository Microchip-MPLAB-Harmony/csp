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

""" This module will instantiate and setup TCC component """

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

def tccTimeMaxValue(symbol, event):
    global size
    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq != 0:
        prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        resolution = (prescaler * 1000.0) / clock_freq   #msec
        unit = tcTimerUnit[tccSym_TimerUnit.getValue()]
        max = ((pow(2, size) + 1) * resolution * unit)
    else:
        max = 0.0
    symbol.setMax(max)

def tccPeriodCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq != 0:
        prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        resolution = (prescaler * 1000.0) / clock_freq   #mSec
        unit = tcTimerUnit[tccSym_TimerUnit.getValue()]
        period = (tccSym_Timer_TIME_MS.getValue() / (resolution * unit))        
    else:
        period = 0
    symbol.setValue(long(period))
    
    #calcAchievableFreq()

def tccTimerEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TCC_OPERATION_MODE"):
        tccVal = component.getSymbolValue("TCC_TIMER_EVCTRL_OVFEO")
        tccVal_ev0 = component.getSymbolValue("TCC_TIMER_EVCTRL_EVACT0")
        tccVal_ev1 = component.getSymbolValue("TCC_TIMER_EVCTRL_EVACT1")

        if (event["value"] == "Timer"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)

            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", tccVal, 2)
            if ((tccVal_ev0) != 0):
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", True, 2)
            if ((tccVal_ev1) != 0):
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2)                

    else:
        if(event["id"] == "TCC_TIMER_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)
        if(event["id"] == "TCC_TIMER_EVCTRL_EVACT0"):
            if (event["value"] != 0):
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", False, 2)
        if(event["id"] == "TCC_TIMER_EVCTRL_EVACT1"):
            if (event["value"] != 0):
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)                

def tccTimerIpEventVisible(symbol, event):
    if event["value"] != 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccTimerInterrupt(symbol, event):
    component = symbol.getComponent()
    interrupt = False
    if (component.getSymbolValue("TCC_TIMER_INTENSET_OVF") == True or 
        component.getSymbolValue("TCC_TIMER_INTENSET_MC1") == True) :
        interrupt = True
    symbol.setValue(interrupt)
###################################################################################################
######################################### Timer Mode ##############################################
###################################################################################################

#timer menu
tccSym_TimerMenu = tccComponent.createMenuSymbol("TCC_TIMER_MENU", tccSym_OperationMode)
tccSym_TimerMenu.setLabel("Timer")
tccSym_TimerMenu.setVisible(False)
tccSym_TimerMenu.setDependencies(updateTimerMenuVisibleProperty, ["TCC_OPERATION_MODE"])

#timer one shot mode
tccSym_Timer_CTRLBSET_ONESHOT = tccComponent.createBooleanSymbol("TCC_TIMER_CTRLBSET_ONESHOT", tccSym_TimerMenu)
tccSym_Timer_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

global tccSym_TimerUnit
timerUnit = ["millisecond", "microsecond", "nanosecond"]
tccSym_TimerUnit = tccComponent.createComboSymbol("TCC_TIMER_UNIT", tccSym_TimerMenu, timerUnit)
tccSym_TimerUnit.setLabel("Timer Period Unit")
tccSym_TimerUnit.setDefaultValue("millisecond")

#time in float
global tccSym_Timer_TIME_MS
clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY")
if clock_freq != 0:
    resolution = (int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000000.0) / clock_freq
    max = ((pow(2, size) + 1) * resolution / 1000000.0)
else:
    max = 0    
tccSym_Timer_TIME_MS = tccComponent.createFloatSymbol("TCC_TIMER_TIME_MS", tccSym_TimerMenu)
tccSym_Timer_TIME_MS.setLabel("Time")
tccSym_Timer_TIME_MS.setDefaultValue(1)
tccSym_Timer_TIME_MS.setMin(0.0)
tccSym_Timer_TIME_MS.setMax(max)
tccSym_Timer_TIME_MS.setDependencies(tccTimeMaxValue, ["core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", \
    "TCC_CTRLA_PRESCALER", "TCC_TIMER_UNIT"])

#timer period
global tccSym_TimerPeriod
period = ((tccSym_Timer_TIME_MS.getValue() * 1000000.0) / resolution)
tccSym_TimerPeriod = tccComponent.createLongSymbol("TCC_TIMER_PERIOD", tccSym_Timer_TIME_MS)
tccSym_TimerPeriod.setLabel("Period Register")
tccSym_TimerPeriod.setVisible(True)
tccSym_TimerPeriod.setReadOnly(True)
tccSym_TimerPeriod.setDefaultValue(long(period))
tccSym_TimerPeriod.setMin(0)
tccSym_TimerPeriod.setMax((pow(2, size) - 1))
tccSym_TimerPeriod.setDependencies(tccPeriodCalc, ["core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", \
    "TCC_CTRLA_PRESCALER", "TCC_TIMER_TIME_MS", "TCC_TIMER_UNIT"])

#timer interrupt mode
global tccSym_Timer_INTENSET_OVF
tccSym_Timer_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_TIMER_INTENSET_OVF", tccSym_TimerMenu)
tccSym_Timer_INTENSET_OVF.setLabel("Enable Timer Period Interrupt")
tccSym_Timer_INTENSET_OVF.setDefaultValue(True)
interruptDepList.append("TCC_TIMER_INTENSET_OVF")

tccSym_TimerEventMenu = tccComponent.createMenuSymbol("TCC_TIMER_EVENT_MENU", tccSym_TimerMenu)
tccSym_TimerEventMenu.setLabel("Events")

tccSym_Timer_EVCTRL_OVFEO = tccComponent.createBooleanSymbol("TCC_TIMER_EVCTRL_OVFEO", tccSym_TimerEventMenu)
tccSym_Timer_EVCTRL_OVFEO.setLabel("Enable Timer Period Overflow Event")
tccSym_Timer_EVCTRL_OVFEO.setDefaultValue(False)

global tccSym_Timer_EVCTRL_EVACT0
tccSym_Timer_EVCTRL_EVACT0 = tccComponent.createKeyValueSetSymbol("TCC_TIMER_EVCTRL_EVACT0", tccSym_TimerEventMenu)
tccSym_Timer_EVCTRL_EVACT0.setLabel("Select Input Event 0 Action")
tccSym_Timer_EVCTRL_EVACT0.addKey("OFF", "0", "Disabled")
tccSym_Timer_EVCTRL_EVACT0.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_Timer_EVCTRL_EVACT0.addKey("COUNTEV", "2", "Count on event")
tccSym_Timer_EVCTRL_EVACT0.addKey("START", "3", "Start counter")
tccSym_Timer_EVCTRL_EVACT0.addKey("INC", "4", "Increment counter")
tccSym_Timer_EVCTRL_EVACT0.addKey("COUNT", "5", "Count on active state of asynchronous event")
tccSym_Timer_EVCTRL_EVACT0.setDisplayMode("Description")
tccSym_Timer_EVCTRL_EVACT0.setOutputMode("Key")

tccSym_Timer_EVCTRL_TCINV0 = tccComponent.createBooleanSymbol("TCC_TIMER_EVCTRL_TCINV0", tccSym_Timer_EVCTRL_EVACT0)
tccSym_Timer_EVCTRL_TCINV0.setLabel("Invert Input Event 0")
tccSym_Timer_EVCTRL_TCINV0.setVisible(False)
tccSym_Timer_EVCTRL_TCINV0.setDependencies(tccTimerIpEventVisible, ["TCC_TIMER_EVCTRL_EVACT0"])

global tccSym_Timer_EVCTRL_EVACT1
tccSym_Timer_EVCTRL_EVACT1 = tccComponent.createKeyValueSetSymbol("TCC_TIMER_EVCTRL_EVACT1", tccSym_TimerEventMenu)
tccSym_Timer_EVCTRL_EVACT1.setLabel("Select Input Event 1 Action")
tccSym_Timer_EVCTRL_EVACT1.addKey("OFF", "0", "Disabled")
tccSym_Timer_EVCTRL_EVACT1.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_Timer_EVCTRL_EVACT1.addKey("DIR", "2", "Direction control")
tccSym_Timer_EVCTRL_EVACT1.addKey("STOP", "3", "Stop counter")
tccSym_Timer_EVCTRL_EVACT1.addKey("DEC", "4", "Decrement counter")
tccSym_Timer_EVCTRL_EVACT1.setDisplayMode("Description")
tccSym_Timer_EVCTRL_EVACT1.setOutputMode("Key")

tccSym_Timer_EVCTRL_TCINV1 = tccComponent.createBooleanSymbol("TCC_TIMER_EVCTRL_TCINV1", tccSym_Timer_EVCTRL_EVACT1)
tccSym_Timer_EVCTRL_TCINV1.setLabel("Invert Input Event 1")
tccSym_Timer_EVCTRL_TCINV1.setVisible(False)
tccSym_Timer_EVCTRL_TCINV1.setDependencies(tccTimerIpEventVisible, ["TCC_TIMER_EVCTRL_EVACT1"])

global tccSym_Timer_INTENSET_MC1
tccSym_Timer_INTENSET_MC1 = tccComponent.createBooleanSymbol("TCC_TIMER_INTENSET_MC1", tccSym_TimerMenu)
tccSym_Timer_INTENSET_MC1.setLabel("Enable Timer Compare Interrupt")
tccSym_Timer_INTENSET_MC1.setVisible(False)
tccSym_Timer_INTENSET_MC1.setDefaultValue(False)
interruptDepList.append("TCC_TIMER_INTENSET_MC1")

tccSym_Timer_EVSYS_CONFIGURE = tccComponent.createIntegerSymbol("TCC_TIMER_EVSYS_CONFIGURE", tccSym_TimerMenu)
tccSym_Timer_EVSYS_CONFIGURE.setVisible(False)
tccSym_Timer_EVSYS_CONFIGURE.setDependencies(tccTimerEvsys, ["TCC_OPERATION_MODE", "TCC_TIMER_EVCTRL_OVFEO", "TCC_TIMER_EVCTRL_EVACT0", "TCC_TIMER_EVCTRL_EVACT1"])

tccSym_Timer_Interrupt_Mode = tccComponent.createBooleanSymbol("TCC_TIMER_INTERRUPT_MODE", None)
tccSym_Timer_Interrupt_Mode.setVisible(False)
tccSym_Timer_Interrupt_Mode.setDependencies(tccTimerInterrupt, ["TCC_TIMER_INTENSET_OVF", "TCC_TIMER_INTENSET_MC1", "TCC_OPERATION_MODE"])