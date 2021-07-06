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


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def ccpTimerVisible(symbol, event):
    if event["value"] == "Timer":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def timerMaxValue(symbol, event):
    component = symbol.getComponent()
    src = int(component.getSymbolValue("CCP_CCPCON1_CLKSEL"))
    unit = ccpTimerUnit[component.getSymbolValue("CCP_UNIT")]
    if(src >= 3):
        clock = component.getSymbolValue("CCP_EXT_CLOCK_FREQ")
    else:
        clock = Database.getSymbolValue("core", ccpInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if(clock != 0):
        resolution = unit * component.getSymbolValue("CCP_PRESCALER_VALUE")/float(clock)
    else:
        resolution = 0
    mode_32 = component.getSymbolValue("CCP_CCPCON1_T32")
    if(mode_32 == True):
        symbol.setMax(4294967297.0 * resolution)
    else:
        symbol.setMax(65537.0 * resolution)

def timerPeriodCalc(symbol, event):
    component = symbol.getComponent()
    clock = component.getSymbolValue("CCP_CLOCK_FREQ")
    unit = ccpTimerUnit[component.getSymbolValue("CCP_UNIT")]

    if(clock != 0):
        resolution = unit/clock
        period = (component.getSymbolValue("CCP_TIME_PERIOD_MS") / resolution) - 1
        symbol.setValue(long(period), 2)
        mode_32 = component.getSymbolValue("CCP_CCPCON1_T32")
        if(mode_32 == True):
            symbol.setMax(4294967295)
        else:
            symbol.setMax(65535)
    else:
        symbol.setValue(0, 2)

###################################################################################################
########################################## Timer  #############################################
###################################################################################################

ccpSym_TimerMenu = ccpComponent.createMenuSymbol("CCP_TIMER_MENU", ccpSym_OprationMode)
ccpSym_TimerMenu.setLabel("Timer")
ccpSym_TimerMenu.setVisible(True)
ccpSym_TimerMenu.setDependencies(ccpTimerVisible, ["CCP_OPERATION_MODE"])

global ccpSym_TimerUnit
timerUnit = ["millisecond", "microsecond", "nanosecond"]
ccpSym_TimerUnit = ccpComponent.createComboSymbol("CCP_UNIT", ccpSym_TimerMenu, timerUnit)
ccpSym_TimerUnit.setLabel("Timer Period Unit")
ccpSym_TimerUnit.setDefaultValue("millisecond")          

clock = Database.getSymbolValue("core", ccpInstanceName.getValue() + "_CLOCK_FREQUENCY")
if(clock != 0):
    resolution = 1000.0 * ccpPrescalerValue.getValue()/float(clock)
    max = (65537.0 * resolution)
else:
    max = 0

ccpSym_PERIOD_MS = ccpComponent.createFloatSymbol("CCP_TIME_PERIOD_MS", ccpSym_TimerMenu)
ccpSym_PERIOD_MS.setLabel("Time")
ccpSym_PERIOD_MS.setDefaultValue(0.3)
ccpSym_PERIOD_MS.setMin(0.0)
ccpSym_PERIOD_MS.setMax(max)
ccpSym_PERIOD_MS.setDependencies(timerMaxValue, ["core." + ccpInstanceName.getValue() + "_CLOCK_FREQUENCY", "CCP_CLOCK_FREQ",
    "CCP_CCPCON1_T32", "CCP_UNIT"])

if clock != 0:
    period = (ccpSym_PERIOD_MS.getValue() / resolution) - 1
else:
    period = 0

#Timer1 Period Register
ccpSym_PR2 = ccpComponent.createLongSymbol("CCP_PERIOD", ccpSym_PERIOD_MS)
ccpSym_PR2.setLabel("Period Register")
ccpSym_PR2.setDefaultValue(long(period))
ccpSym_PR2.setReadOnly(True)
ccpSym_PR2.setMin(0)
ccpSym_PR2.setMax(65535)
ccpSym_PR2.setDependencies(timerPeriodCalc, ["core." + ccpInstanceName.getValue() + "_CLOCK_FREQUENCY", "CCP_TIME_PERIOD_MS",
    "CCP_CLOCK_FREQ", "CCP_CCPCON1_T32", "CCP_UNIT"])

ccpSym_CCPCON1_ONESHOT = ccpComponent.createBooleanSymbol("CCP_CCPCON1_ONESHOT", ccpSym_TimerMenu)
ccpSym_CCPCON1_ONESHOT.setLabel("Enable One Shot")
ccpcon1_depList.append("CCP_CCPCON1_ONESHOT")

    