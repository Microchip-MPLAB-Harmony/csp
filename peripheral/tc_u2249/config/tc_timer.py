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

def updateTimerMenuVisibleProperty(symbol, event):
    if event["value"] == "Timer":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcTimeMaxValue(symbol, event):
    clock_freq = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    prescaler = int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    resolution = (prescaler * 1000000000.0) / clock_freq
    mode = tcSym_CTRLA_MODE.getValue()
    max = 0.0
    if (mode == 0):
        max = (65535.0 * resolution / 1000000)
    elif (mode == 1):
        max = (255.0 * resolution / 1000000)
    elif (mode == 2):
        max = (4294967296.0 * resolution / 1000000)
    symbol.setMax(max)

def tcPeriodCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    prescaler = int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    resolution = (prescaler * 1000.0) / clock_freq
    time = tcSym_Timer_TIME_MS.getValue()
    period = time / resolution
    symbol.setValue(long(period), 2)

def tcTimerEvsys(symbol, event):
    Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)

###################################################################################################
######################################### Timer Mode ##############################################
###################################################################################################

#timer menu
tcSym_TimerMenu = tcComponent.createMenuSymbol("TC_TIMER_MENU", tcSym_OperationMode)
tcSym_TimerMenu.setLabel("Timer")
tcSym_TimerMenu.setDependencies(updateTimerMenuVisibleProperty, ["TC_OPERATION_MODE"])

#timer one shot mode
tcSym_Timer_CTRLBSET_ONESHOT = tcComponent.createBooleanSymbol("TC_TIMER_CTRLBSET_ONESHOT", tcSym_TimerMenu)
tcSym_Timer_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

#time in float
global tcSym_Timer_TIME_MS
resolution = (int(tcSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000000.0) / Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
max = (65535.0 * resolution / 1000000)
tcSym_Timer_TIME_MS = tcComponent.createFloatSymbol("TC_TIMER_TIME_MS", tcSym_TimerMenu)
tcSym_Timer_TIME_MS.setLabel("Timer Period (Milli Sec)")
tcSym_Timer_TIME_MS.setDefaultValue(1)
tcSym_Timer_TIME_MS.setMin(0.0)
tcSym_Timer_TIME_MS.setMax(max)
tcSym_Timer_TIME_MS.setDependencies(tcTimeMaxValue, ["TC_CTRLA_MODE", "core.CPU_CLOCK_FREQUENCY", \
    "TC_CTRLA_PRESCALER"])

#timer period
period = tcSym_Timer_TIME_MS.getValue() * 1000000 / resolution
tcSym_TimerPeriod = tcComponent.createLongSymbol("TC_TIMER_PERIOD", tcSym_TimerMenu)
tcSym_TimerPeriod.setLabel("Timer Period")
tcSym_TimerPeriod.setVisible(True)
tcSym_TimerPeriod.setDefaultValue(long(period))
tcSym_TimerPeriod.setMin(0)
tcSym_TimerPeriod.setMax(4294967296)
tcSym_TimerPeriod.setDependencies(tcPeriodCalc, ["TC_CTRLA_MODE", "core.CPU_CLOCK_FREQUENCY", \
    "TC_CTRLA_PRESCALER", "TC_TIMER_TIME_MS"])

#timer interrupt mode
global tcSym_Timer_INTENSET_OVF
tcSym_Timer_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_TIMER_INTENSET_OVF", tcSym_TimerMenu)
tcSym_Timer_INTENSET_OVF.setLabel("Enable Timer Period Interrupt")
tcSym_Timer_INTENSET_OVF.setDefaultValue(True)

tcSym_Timer_EVCTRL_OVFEO = tcComponent.createBooleanSymbol("TC_TIMER_EVCTRL_OVFEO", tcSym_TimerMenu)
tcSym_Timer_EVCTRL_OVFEO.setLabel("Enable Timer Period Overflow Event")
tcSym_Timer_EVCTRL_OVFEO.setDefaultValue(False)

global tcSym_Timer_INTENSET_MC1
tcSym_Timer_INTENSET_MC1 = tcComponent.createBooleanSymbol("TC_TIMER_INTENSET_MC1", tcSym_TimerMenu)
tcSym_Timer_INTENSET_MC1.setLabel("Enable Timer Compare Interrupt")
tcSym_Timer_INTENSET_MC1.setVisible(False)
tcSym_Timer_INTENSET_MC1.setDefaultValue(False)

tcSym_Timer_EVSYS_CONFIGURE = tcComponent.createIntegerSymbol("TC_TIMER_EVSYS_CONFIGURE", tcSym_TimerMenu)
tcSym_Timer_EVSYS_CONFIGURE.setVisible(False)
tcSym_Timer_EVSYS_CONFIGURE.setDependencies(tcTimerEvsys, ["TC_TIMER_EVCTRL_OVFEO"])