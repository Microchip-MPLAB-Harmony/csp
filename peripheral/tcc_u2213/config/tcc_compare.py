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

def tccComparePeriodCalc(symbol, event):
    wave = ""
    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if clock_freq != 0:
        resolution = (int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / clock_freq
        wave = tccSym_Compare_WAVE_WAVEGEN.getSelectedKey()
        if (wave == "MFRQ" or wave == "NPWM" or wave == "NFRQ"):
            slope = 1
        else:
            slope = 2
        period = tccSym_ComparePeriod.getValue()
        time = period * slope * resolution
    else:
        time = 0
    symbol.setLabel("**** Waveform Period is " + str(time) + " us ****")

    if wave == "MFRQ":
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tccEventVisible(symbol, event):
    if event["value"] == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccCompareEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TCC_OPERATION_MODE"):
        if (event["value"] == "Compare"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)
            for channelID in range(0, int(numOfChannels)):
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", False, 2)
                if component.getSymbolValue("TCC_COMPARE_EVCTRL_MCEO" + str(channelID)) == True:
                    Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", True, 2)

            if component.getSymbolValue("TCC_COMPARE_EVCTRL_OVFEO") == True:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", True, 2)
            if component.getSymbolValue("TCC_COMPARE_EVCTRL_EVACT0") == True:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", True, 2)
            if component.getSymbolValue("TCC_COMPARE_EVCTRL_EVACT1") == True:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2)
    else:
        if(event["id"] == "TCC_COMPARE_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", event["value"], 2)
        if(event["id"] == "TCC_COMPARE_EVCTRL_EVACT0"):
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", event["value"], 2)
        if(event["id"] == "TCC_COMPARE_EVCTRL_EVACT1"):
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", event["value"], 2) 
        for channelID in range(0, int(numOfChannels)):
            if component.getSymbolValue("TCC_COMPARE_EVCTRL_MCEO" + str(channelID)) == True:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", True, 2)           
            else:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", False, 2)

def tccCompareEVACTVisible(symbol, event):
    symbol.setVisible(event["value"])

def tccCompareInterrupt(symbol, event):
    component = symbol.getComponent()
    interrupt = False
    for intr in range (0, len(compareInterruptDep)-1):
        if(component.getSymbolValue(compareInterruptDep[intr]) == True):
            interrupt = True
    symbol.setValue(interrupt)

def tccCompareDirVisible(symbol, event):
    if event["value"] == "MFRQ" or event["value"] == "NFRQ" or event["value"] == "NPWM":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcccomparePeriodVisible(symbol, event):
    if event["value"] == "MFRQ":
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tccCompareIpEventVisible(symbol, event):
    if event["value"] != 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)        
###################################################################################################
####################################### Compare Mode ##############################################
###################################################################################################
global compareEvsysDep
compareEvsysDep = []
compareEvsysDep.append("TCC_OPERATION_MODE")

global compareInterruptDep
compareInterruptDep = []

#compare menu
tccSym_CompareMenu = tccComponent.createMenuSymbol("TCC_COMPARE_MENU", tccSym_OperationMode)
tccSym_CompareMenu.setLabel("Compare")
tccSym_CompareMenu.setVisible(False)
tccSym_CompareMenu.setDependencies(updateCompareMenuVisibleProperty, ["TCC_OPERATION_MODE"])

#waveform mode
global tccSym_Compare_WAVE_WAVEGEN
tccSym_Compare_WAVE_WAVEGEN = tccComponent.createKeyValueSetSymbol("TCC_COMPARE_WAVE_WAVEGEN", tccSym_CompareMenu)
tccSym_Compare_WAVE_WAVEGEN.setLabel("Waveform Mode")
tcc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]/value-group@[name=\"TCC_WAVE__WAVEGEN\"]")
childrenNodes = tcc.getChildren()
for param in range(0, len(childrenNodes)):
    tccSym_Compare_WAVE_WAVEGEN.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"),
        childrenNodes[param].getAttribute("caption"))
tccSym_Compare_WAVE_WAVEGEN.setDefaultValue(1)
tccSym_Compare_WAVE_WAVEGEN.setOutputMode("Key")
tccSym_Compare_WAVE_WAVEGEN.setDisplayMode("Key")

#compare direction
tccSym_Compare_CTRLBSET_DIR = tccComponent.createKeyValueSetSymbol("TCC_COMPARE_CTRLBSET_DIR", tccSym_CompareMenu)
tccSym_Compare_CTRLBSET_DIR.setLabel("Counter Direction")
tccSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_UP", "0", "UP Count")
tccSym_Compare_CTRLBSET_DIR.addKey("DIR_COUNT_DOWN", "1", "DOWN Count")
tccSym_Compare_CTRLBSET_DIR.setDefaultValue(0)
tccSym_Compare_CTRLBSET_DIR.setOutputMode("Value")
tccSym_Compare_CTRLBSET_DIR.setDisplayMode("Description")
tccSym_Compare_CTRLBSET_DIR.setDependencies(tccCompareDirVisible, ["TCC_COMPARE_WAVE_WAVEGEN"])

if (outputMatrixImplemented == 1):
    tccSym_WEXCTRL_OTMX = tccComponent.createKeyValueSetSymbol("TCC_COMPARE_WEXCTRL_OTMX", tccSym_CompareMenu)
    tccSym_WEXCTRL_OTMX.setLabel("Select Output Matrix")
    tccSym_WEXCTRL_OTMX.setDefaultValue(0)
    tccSym_WEXCTRL_OTMX.setOutputMode("Value")
    tccSym_WEXCTRL_OTMX.setDisplayMode("Description")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_0", "0", "Default Channel Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_1", "1", "Modulo Half Number of Channel Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_2", "2", "Only Channel 0 Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_3", "3", "Channel 0 + Remaining Channel 1 Outputs")


#compare one shot mode
tccSym_Compare_CTRLBSET_ONESHOT = tccComponent.createBooleanSymbol("TCC_COMPARE_CTRLBSET_ONESHOT", tccSym_CompareMenu)
tccSym_Compare_CTRLBSET_ONESHOT.setLabel("Enable One-Shot Mode")

#double buffering
tccSym_Compare_CTRLBSET_LUPD = tccComponent.createBooleanSymbol("TCC_COMPARE_CTRLBSET_LUPD", tccSym_CompareMenu)
tccSym_Compare_CTRLBSET_LUPD.setLabel("Enable Double Buffering")
tccSym_Compare_CTRLBSET_LUPD.setDefaultValue(True)

#compare period
global tccSym_ComparePeriod
tccSym_ComparePeriod = tccComponent.createLongSymbol("TCC_COMPARE_PERIOD", tccSym_CompareMenu)
tccSym_ComparePeriod.setLabel("Period Register")
tccSym_ComparePeriod.setDefaultValue(65535)
tccSym_ComparePeriod.setMin(0)
tccSym_ComparePeriod.setMax((pow(2, size) - 1))
tccSym_ComparePeriod.setVisible(True)
tccSym_ComparePeriod.setDependencies(tcccomparePeriodVisible, ["TCC_COMPARE_WAVE_WAVEGEN"])

#period time in us
clk_freq = Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY")
if clk_freq != 0:
    resolution = (int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:]) * 1000000.0) / clk_freq
    wave = tccSym_Compare_WAVE_WAVEGEN.getSelectedKey()
    if (wave == "MFRQ" or wave == "NPWM" or wave == "NFRQ"):
        slope = 1
    else:
        slope = 2
    time = tccSym_ComparePeriod.getValue() * resolution * slope
else:
    time = 0
tccSym_ComparePeriod_Comment = tccComponent.createCommentSymbol("TCC_COMPARE_PERIOD_COMMENT", tccSym_CompareMenu)
tccSym_ComparePeriod_Comment.setLabel("**** Waveform Period is " + str(time) + " us ****")
tccSym_ComparePeriod_Comment.setDependencies(tccComparePeriodCalc, ["TCC_COMPARE_PERIOD", "TCC_CTRLA_PRESCALER",\
    "core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_COMPARE_WAVE_WAVEGEN"])

#compare channel counter/compare interrupt
global tccSym_Compare_INTENSET_OVF
tccSym_Compare_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_COMPARE_INTENSET_OVF", tccSym_CompareMenu)
tccSym_Compare_INTENSET_OVF.setLabel("Enable Period Interrupt")
tccSym_Compare_INTENSET_OVF.setDefaultValue(False)
compareInterruptDep.append("TCC_COMPARE_INTENSET_OVF")
interruptDepList.append("TCC_COMPARE_INTENSET_OVF")

for channelID in range(0, int(numOfChannels)):
    #channel menu
    tccSym_Compare_Channel_Menu = tccComponent.createMenuSymbol("TCC_COMPARE_CHANNEL"+str(channelID), tccSym_CompareMenu)
    tccSym_Compare_Channel_Menu.setLabel("Channel "+str(channelID))

    #compare value
    global tccSym_CompareDuty0
    tccSym_CompareDuty0 = tccComponent.createLongSymbol("TCC_COMPARE_CC" + str(channelID), tccSym_Compare_Channel_Menu)
    tccSym_CompareDuty0.setLabel("Compare Value")
    tccSym_CompareDuty0.setDefaultValue(24)
    tccSym_CompareDuty0.setMin(0)
    tccSym_CompareDuty0.setMax(tccSym_ComparePeriod.getValue()) 

    tccSym_Compare_INTENSET_MC0 = tccComponent.createBooleanSymbol("TCC_COMPARE_INTENSET_MC" + str(channelID), tccSym_Compare_Channel_Menu)
    tccSym_Compare_INTENSET_MC0.setLabel("Enable Compare Match Interrupt")
    tccSym_Compare_INTENSET_MC0.setDefaultValue(False)
    compareInterruptDep.append("TCC_COMPARE_INTENSET_MC" + str(channelID))
    interruptDepList.append("TCC_COMPARE_INTENSET_MC" + str(channelID))

    tccSym_Compare_EVCTRL_MCEO0 = tccComponent.createBooleanSymbol("TCC_COMPARE_EVCTRL_MCEO" + str(channelID), tccSym_Compare_Channel_Menu)
    tccSym_Compare_EVCTRL_MCEO0.setLabel("Enable Compare Match Output Event")
    tccSym_Compare_EVCTRL_MCEO0.setDefaultValue(False)     
    compareEvsysDep.append("TCC_COMPARE_EVCTRL_MCEO" + str(channelID))  

tccSym_Compare_Output_Menu = tccComponent.createMenuSymbol("TCC_COMPARE_OUTPUT_MENU", tccSym_CompareMenu) 
tccSym_Compare_Output_Menu.setLabel("Outputs")

for output in range (0, int(numOfOutputs)):
    tccSym_Compare_DRVCTRL_INVEN0 = tccComponent.createBooleanSymbol("TCC_COMPARE_DRVCTRL_INVEN" + str(output), tccSym_Compare_Output_Menu)
    tccSym_Compare_DRVCTRL_INVEN0.setLabel("Invert Output WO[" + str(output) + "]")
    tccSym_Compare_DRVCTRL_INVEN0.setDefaultValue(False)

compareInterruptDep.append("TCC_OPERATION_MODE")
global tccSym_Compare_InterruptMode
tccSym_Compare_InterruptMode = tccComponent.createBooleanSymbol("TCC_COMPARE_INTERRUPT_MODE", tccSym_CompareMenu)
tccSym_Compare_InterruptMode.setVisible(False)
tccSym_Compare_InterruptMode.setDefaultValue(False)
tccSym_Compare_InterruptMode.setDependencies(tccCompareInterrupt, compareInterruptDep)

tccSym_Compare_Events_Menu = tccComponent.createMenuSymbol("TCC_COMPARE_EVENT_MENU", tccSym_CompareMenu)
tccSym_Compare_Events_Menu.setLabel("Events")

tccSym_Compare_EVCTRL_OVFEO = tccComponent.createBooleanSymbol("TCC_COMPARE_EVCTRL_OVFEO", tccSym_Compare_Events_Menu)
tccSym_Compare_EVCTRL_OVFEO.setLabel("Enable Compare Period Overflow Event")
tccSym_Compare_EVCTRL_OVFEO.setDefaultValue(False)
compareEvsysDep.append("TCC_COMPARE_EVCTRL_OVFEO")

global tccSym_Compare_EVCTRL_EVACT0
tccSym_Compare_EVCTRL_EVACT0 = tccComponent.createKeyValueSetSymbol("TCC_COMPARE_EVCTRL_EVACT0", tccSym_Compare_Events_Menu)
tccSym_Compare_EVCTRL_EVACT0.setLabel("Select Input Event 0 Action")
tccSym_Compare_EVCTRL_EVACT0.addKey("OFF", "0", "Disabled")
tccSym_Compare_EVCTRL_EVACT0.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_Compare_EVCTRL_EVACT0.addKey("COUNTEV", "2", "Count on event")
tccSym_Compare_EVCTRL_EVACT0.addKey("START", "3", "Start counter")
tccSym_Compare_EVCTRL_EVACT0.addKey("INC", "4", "Increment counter")
tccSym_Compare_EVCTRL_EVACT0.addKey("COUNT", "5", "Count on active state of asynchronous event")
tccSym_Compare_EVCTRL_EVACT0.setDisplayMode("Description")
tccSym_Compare_EVCTRL_EVACT0.setOutputMode("Key")
compareEvsysDep.append("TCC_COMPARE_EVCTRL_EVACT0")

tccSym_Compare_EVCTRL_TCINV0 = tccComponent.createBooleanSymbol("TCC_COMPARE_EVCTRL_TCINV0", tccSym_Compare_EVCTRL_EVACT0)
tccSym_Compare_EVCTRL_TCINV0.setLabel("Invert Input Event 0")
tccSym_Compare_EVCTRL_TCINV0.setVisible(False)
tccSym_Compare_EVCTRL_TCINV0.setDependencies(tccCompareIpEventVisible, ["TCC_COMPARE_EVCTRL_EVACT0"])

global tccSym_Compare_EVCTRL_EVACT1
tccSym_Compare_EVCTRL_EVACT1 = tccComponent.createKeyValueSetSymbol("TCC_COMPARE_EVCTRL_EVACT1", tccSym_Compare_Events_Menu)
tccSym_Compare_EVCTRL_EVACT1.setLabel("Select Input Event 1 Action")
tccSym_Compare_EVCTRL_EVACT1.addKey("OFF", "0", "Disabled")
tccSym_Compare_EVCTRL_EVACT1.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_Compare_EVCTRL_EVACT1.addKey("DIR", "2", "Direction control")
tccSym_Compare_EVCTRL_EVACT1.addKey("STOP", "3", "Stop counter")
tccSym_Compare_EVCTRL_EVACT1.addKey("DEC", "4", "Decrement counter")
tccSym_Compare_EVCTRL_EVACT1.setDisplayMode("Description")
tccSym_Compare_EVCTRL_EVACT1.setOutputMode("Key")
compareEvsysDep.append("TCC_COMPARE_EVCTRL_EVACT1")

tccSym_Compare_EVCTRL_TCINV1 = tccComponent.createBooleanSymbol("TCC_COMPARE_EVCTRL_TCINV1", tccSym_Compare_EVCTRL_EVACT1)
tccSym_Compare_EVCTRL_TCINV1.setLabel("Invert Input Event 1")
tccSym_Compare_EVCTRL_TCINV1.setVisible(False)
tccSym_Compare_EVCTRL_TCINV1.setDependencies(tccCompareIpEventVisible, ["TCC_COMPARE_EVCTRL_EVACT1"])

tccSym_Compare_EVESYS_CONFIGURE = tccComponent.createIntegerSymbol("TCC_COMPARE_EVSYS_CONFIGURE", tccSym_Compare_Events_Menu)
tccSym_Compare_EVESYS_CONFIGURE.setVisible(False)
tccSym_Compare_EVESYS_CONFIGURE.setDependencies(tccCompareEvsys, compareEvsysDep)
