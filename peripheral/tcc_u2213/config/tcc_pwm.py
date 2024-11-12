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

tccSym_Channel_Menu = []
global tccSym_Channel_CC
tccSym_Channel_CC = []
tccSym_Channel_Polarity = []
tccSym_Channel_Polarity_NPWM = []
tccSym_Channel_WAVE_SWAP = []
tccSym_Channel_WAVE_CICCEN = []
global tccSym_Channel_WEXCTRL_DTIEN
tccSym_Channel_WEXCTRL_DTIEN = []
tccSym_Channel_INTENSET_MC = []
tccSym_Channel_EVCTRL_MCEO = []
tccSym_Channel_EVCTRL_MCEI = []
tccSym_DRVCTRL_NRE_NRV = []
tccSym_PATT_PGE = []
tccSym_PATT_PGV = []

global pwmInterruptDepList
pwmInterruptDepList = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def tccRampMenuVisible(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "NPWM"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccRampCycleMenuVisible(symbol, event):
    symbol.setVisible(event["value"])

def tccRampPeriodCirBuf(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "RAMP2C"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tccRampAPeriodCalc(symbol, event):
    global tccSym_WAVE_RAMP
    global tccSym_Channel_CC
    global tccSym_PER_PER
    if (tccSym_WAVE_RAMP.getValue() == 1): #RAMP2A
        symbol.setValue(tccSym_PER_PER.getValue())  ## PER
        symbol.setLabel("Cycle A Period Value (PER)")
    elif (tccSym_WAVE_RAMP.getValue() == 2):  #RAMP2
        symbol.setValue(tccSym_PER_PER.getValue())  ## PER
        symbol.setLabel("Cycle A Period Value (PER)")
    elif (tccSym_WAVE_RAMP.getValue() == 3): #RAMP2C
        symbol.setValue(tccSym_Channel_CC[0].getValue())  ## CC0  value  
        symbol.setLabel("Cycle A Period Value (CC0)")  

def tccRampCCBuffer(symbol, event):
    if event["value"] == 1:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccRampADutyCalc(symbol, event):
    global tccSym_WAVE_RAMP
    global tccSym_Channel_CC
    if (tccSym_WAVE_RAMP.getValue() == 1): #RAMP2A
        symbol.setValue(tccSym_Channel_CC[0].getValue())  ## CC0 buffered value
        symbol.setLabel("Cycle A Duty Value (CC0 Buffer)")
    elif (tccSym_WAVE_RAMP.getValue() == 2):  #RAMP2
        symbol.setValue(tccSym_Channel_CC[0].getValue())  ## CC0  value
        symbol.setLabel("Cycle A Duty Value (CC0)")
    elif (tccSym_WAVE_RAMP.getValue() == 3): #RAMP2C
        symbol.setValue(tccSym_Channel_CC[2].getValue())  ## CC2  value  
        symbol.setLabel("Cycle A Duty Value (CC2)")      

def tccRampBdutyCalc(symbol, event):
    global tccSym_WAVE_RAMP
    global tccSym_Channel_CC
    if (tccSym_WAVE_RAMP.getValue() == 1): #RAMP2A
        symbol.setValue(tccSym_Channel_CC[0].getValue())  ## CC0 value
        symbol.setLabel("Cycle B Duty Value (CC0)")
    elif (tccSym_WAVE_RAMP.getValue() == 2):  #RAMP2
        symbol.setValue(tccSym_Channel_CC[1].getValue())  ## CC1  value
        symbol.setLabel("Cycle B Duty Value (CC1)")
    elif (tccSym_WAVE_RAMP.getValue() == 3): #RAMP2C
        symbol.setValue(tccSym_Channel_CC[1].getValue())  ## CC1  value    
        symbol.setLabel("Cycle B Duty Value (CC1)")

def tccRampBPeriodCalc(symbol, event):
    symbol.setValue(event["value"])  
 

def tccDirVisible(symbol, event):
    if (event["id"] == "TCC_WAVE_WAVEGEN" and tccSym_Slave_Mode.getValue() == False):
        symObj = event["symbol"]
        if (symObj.getSelectedKey() == "NPWM"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    elif (event["id"] == "TCC_SLAVE_MODE"):
        symbol.setVisible(not event["value"])

def tccFaultVisible(symbol, event):
    global tccSym_EVCTRL_EVACT0
    global tccSym_EVCTRL_EVACT1
    fault0 = tccSym_EVCTRL_EVACT0.getSelectedKey()
    fault1 = tccSym_EVCTRL_EVACT1.getSelectedKey()

    if "TCC_FAULT_COMMENT" in symbol.getID():
        if (fault0 == "FAULT" or fault1 == "FAULT"):
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        if (fault0 == "FAULT" or fault1 == "FAULT"):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def tccDeadTimeVisible(symbol, event):
    global tccSym_Channel_WEXCTRL_DTIEN
    if (tccSym_Channel_WEXCTRL_DTIEN[0].getValue() == True or tccSym_Channel_WEXCTRL_DTIEN[1].getValue() == True or
        tccSym_Channel_WEXCTRL_DTIEN[2].getValue() == True or tccSym_Channel_WEXCTRL_DTIEN[3].getValue() == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccPattgenVisible(symbol, event):
    if(event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccPWMFreqCalc(symbol, event):
    if (tccSym_Slave_Mode.getValue() == False):
        clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue()+"_CLOCK_FREQUENCY")
        if clock_freq == 0:
            clock_freq = 1
        prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])

        if (tccSym_WAVE_WAVEGEN.getValue() == 0): #single slope PWM
            slope = 1
            period = tccSym_PER_PER.getValue() + 1
        else:
            slope = 2
            period = tccSym_PER_PER.getValue()
        frequency = ((clock_freq / prescaler) / period) / slope
        symbol.setLabel("**** PWM Frequency is " +str(frequency)+ " Hz ****")
        symbol.setVisible(True)
    elif (event["id"] == "TCC_SLAVE_MODE"):
        symbol.setVisible(not event["value"])

def tccDeadTimeCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    if (symbol.getID() == "TCC_DTLS_COMMENT"):
        dead_time = (tccSym_WEXCTRL_DTLS.getValue() * 1000000.0 / (clock_freq))
        symbol.setLabel("**** Low side dead time is "+str(dead_time)+ " uS ****")
    if (symbol.getID() == "TCC_DTHS_COMMENT"):
        dead_time = (tccSym_WEXCTRL_DTHS.getValue() * 1000000.0 / (clock_freq))
        symbol.setLabel("**** High side dead time is "+str(dead_time)+ " uS ****")

def tccEvent0Visible(symbol, event):
    if event["value"] == 1 or event["value"] == 2:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tccSingleSlopeVisible(symbol, event):
    if (event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccDualSlopeVisible(symbol, event):
    if (event["value"] != 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccCircularBufferVisible(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "DSBOTH"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)    

def tccPwmVisible(symbol, event):
    if event["value"] == "PWM":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)                

def tccPwmIpEventVisible(symbol, event):
    if event["value"] != 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False) 

def tccPwmInterruptMode(symbol, event):
    component = symbol.getComponent()
    interrupt = False
    for intr in range (0, len(pwmInterruptDepList)-1):
        if(component.getSymbolValue(pwmInterruptDepList[intr]) == True):
            interrupt = True
    symbol.setValue(interrupt)

def tccEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TCC_OPERATION_MODE" and event["value"] == "PWM"):
        Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
        Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", False, 2)
        Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)
        for channelID in range(0, int(numOfChannels)):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", False, 2)
            if component.getSymbolValue("TCC_EVCTRL_MCEO_" + str(channelID)) == True:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", True, 2)
            if component.getSymbolValue("TCC_EVCTRL_MCEI_" + str(channelID)) == True:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", True, 2)                

        if component.getSymbolValue("TCC_EVCTRL_OVFEO") == True:
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", True, 2)

        if component.getSymbolValue("TCC_EVCTRL_EVACT0") != 0:
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", True, 2)
        if component.getSymbolValue("TCC_EVCTRL_EVACT1") != 0:
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2)        
    else:
        if(event["id"] == "TCC_EVCTRL_OVFEO"):
            Database.setSymbolValue("evsys", "GENERATOR_"+str(tccInstanceName.getValue())+"_OVF_ACTIVE", event["value"], 2)

        if(event["id"] == "TCC_EVCTRL_EVACT0"):
            if (event["value"] != 0):
                Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_0_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_0_READY", False, 2)

        if(event["id"] == "TCC_EVCTRL_EVACT1"):
            if (event["value"] != 0):
                Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_1_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_1_READY", False, 2)

        if("EVCTRL_MCEO" in event["id"]):
            mcInstance = event["id"].split("_")[2][:2]
            event_name = "_" + (mcInstance) + "_" + event["id"].split("_")[3]
            Database.setSymbolValue("evsys", "GENERATOR_"+str(tccInstanceName.getValue())+ str(event_name)+"_ACTIVE", event["value"], 2)

        if("EVCTRL_MCEI" in event["id"]):
            mcInstance = event["id"].split("_")[2][:2]
            event_name = "_" + (mcInstance) + "_" + event["id"].split("_")[3]
            Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+ str(event_name)+"_READY", event["value"], 2)


###################################################################################################
####################################### PWM Mode ##############################################
###################################################################################################                     

#PWM menu
tccSym_PWMMenu = tccComponent.createMenuSymbol("TCC_PWM", tccSym_OperationMode)
tccSym_PWMMenu.setLabel("PWM")
tccSym_PWMMenu.setDependencies(tccPwmVisible, ["TCC_OPERATION_MODE"])

#waveform option
global tccSym_WAVE_WAVEGEN
tccSym_WAVE_WAVEGEN = tccComponent.createKeyValueSetSymbol("TCC_WAVE_WAVEGEN", tccSym_PWMMenu)
tccSym_WAVE_WAVEGEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
tccSym_WAVE_WAVEGEN.setLabel("Select PWM Type")
tccSym_WAVE_WAVEGEN.setDefaultValue(0)
tccSym_WAVE_WAVEGEN.setOutputMode("Key")
tccSym_WAVE_WAVEGEN.setDisplayMode("Key")
tccSym_WAVE_WAVEGEN.addKey("NPWM", "2", "Single slope PWM")
#tccSym_WAVE_WAVEGEN.addKey("DSCRITICAL", "4", "Dual slope critical")
tccSym_WAVE_WAVEGEN.addKey("DSBOTTOM", "5", "Dual slope PWM with interrupt/event when counter = ZERO")
tccSym_WAVE_WAVEGEN.addKey("DSBOTH", "6", "Dual slope PWM with interrupt/event when counter = ZERO or counter = TOP")
tccSym_WAVE_WAVEGEN.addKey("DSTOP", "7", "Dual slope PWM with interrupt/event when counter = TOP")
tccSym_WAVE_WAVEGEN.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])    


tccSym_CTRLBSET_DIR = tccComponent.createBooleanSymbol("TCC_CTRLBSET_DIR", tccSym_PWMMenu)
tccSym_CTRLBSET_DIR.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:CTRLBSET")
tccSym_CTRLBSET_DIR.setLabel("PWM Direction - Count Down")
tccSym_CTRLBSET_DIR.setDefaultValue(False)
tccSym_CTRLBSET_DIR.setDependencies(tccDirVisible, ["TCC_WAVE_WAVEGEN", "TCC_SLAVE_MODE"]) 

#Period Value
global tccSym_PER_PER
if size == 32:
    tccSym_PER_PER = tccComponent.createLongSymbol("TCC_PER_PER", tccSym_PWMMenu)
else:
    tccSym_PER_PER = tccComponent.createIntegerSymbol("TCC_PER_PER", tccSym_PWMMenu)
    tccSym_PER_PER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:PER")
tccSym_PER_PER.setLabel("Period Value")
tccSym_PER_PER.setDefaultValue(2399)
tccSym_PER_PER.setMin(0)
tccSym_PER_PER.setMax(pow(2, size) - 1)
tccSym_PER_PER.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])

clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue()+"_CLOCK_FREQUENCY")
if clock_freq != 0:
    prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])

    if (tccSym_WAVE_WAVEGEN.getSelectedKey() == "NFRQ" or tccSym_WAVE_WAVEGEN.getSelectedKey() == "MFRQ" 
        or tccSym_WAVE_WAVEGEN.getSelectedKey() == "NPWM"):
        slope = 1
        period = tccSym_PER_PER.getValue() + 1
    else:
        slope = 2
        period = tccSym_PER_PER.getValue()
    frequency = ((clock_freq / prescaler) / period) / slope
else:
    frequency = 0

#Calculated frequency
tccSym_Frequency = tccComponent.createCommentSymbol("TCC_FREQUENCY", tccSym_PWMMenu)
tccSym_Frequency.setLabel("**** PWM Frequency is "+str(frequency)+" Hz ****")
tccSym_Frequency.setDependencies(tccPWMFreqCalc, ["core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_PER_PER", "TCC_WAVE_WAVEGEN", "TCC_CTRLA_PRESCALER", "TCC_SLAVE_MODE"])

#Period interrupt
tccSym_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_INTENSET_OVF", tccSym_PWMMenu)
tccSym_INTENSET_OVF.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:INTENSET")
tccSym_INTENSET_OVF.setLabel("Enable Period Interrupt")
tccSym_INTENSET_OVF.setDefaultValue(False)
interruptDepList.append("TCC_INTENSET_OVF")
pwmInterruptDepList.append("TCC_INTENSET_OVF")

#Period out event
tccSym_EVCTRL_OVFEO = tccComponent.createBooleanSymbol("TCC_EVCTRL_OVFEO", tccSym_PWMMenu)
tccSym_EVCTRL_OVFEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
tccSym_EVCTRL_OVFEO.setLabel("Enable Period Event Out")
tccSym_EVCTRL_OVFEO.setDefaultValue(False)
eventDepList.append("TCC_EVCTRL_OVFEO")   

if (outputMatrixImplemented == 1):
    tccSym_WEXCTRL_OTMX = tccComponent.createKeyValueSetSymbol("TCC_WEXCTRL_OTMX", tccSym_PWMMenu)
    tccSym_WEXCTRL_OTMX.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WEXCTRL")
    tccSym_WEXCTRL_OTMX.setLabel("Select Output Matrix")
    tccSym_WEXCTRL_OTMX.setDefaultValue(0)
    tccSym_WEXCTRL_OTMX.setOutputMode("Value")
    tccSym_WEXCTRL_OTMX.setDisplayMode("Description")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_0", "0", "Default Channel Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_1", "1", "Modulo Half Number of Channel Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_2", "2", "Only Channel 0 Outputs")
    tccSym_WEXCTRL_OTMX.addKey("OTMX_3", "3", "Channel 0 + Remaining Channel 1 Outputs")

tccSym_MainChannel_Menu = tccComponent.createMenuSymbol("TCC_CHANNEL", tccSym_PWMMenu)
tccSym_MainChannel_Menu.setLabel("Channel Configurations")

for channelID in range(0, int(numOfChannels)):
    #channel menu
    tccSym_Channel_Menu.append(channelID)
    tccSym_Channel_Menu[channelID] = tccComponent.createMenuSymbol("TCC_CHANNEL"+str(channelID), tccSym_MainChannel_Menu)
    tccSym_Channel_Menu[channelID].setLabel("Channel "+str(channelID))

    #Duty
    tccSym_Channel_CC.append(channelID)
    if size == 32:
        tccSym_Channel_CC[channelID] = tccComponent.createLongSymbol("TCC_"+str(channelID)+"_CC", tccSym_Channel_Menu[channelID])
    else:
        tccSym_Channel_CC[channelID] = tccComponent.createIntegerSymbol("TCC_"+str(channelID)+"_CC", tccSym_Channel_Menu[channelID])
        tccSym_Channel_CC[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:CC")
    tccSym_Channel_CC[channelID].setLabel("Duty Value")
    tccSym_Channel_CC[channelID].setMin(0)
    tccSym_Channel_CC[channelID].setMax(pow(2, size) - 1)

    #output polarity for dual slope
    tccSym_Channel_Polarity.append(channelID)
    tccSym_Channel_Polarity[channelID] = tccComponent.createKeyValueSetSymbol("TCC_"+str(channelID)+"_WAVE_POL", tccSym_Channel_Menu[channelID])
    tccSym_Channel_Polarity[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
    tccSym_Channel_Polarity[channelID].setLabel("Output Polarity")
    tccSym_Channel_Polarity[channelID].addKey("LOW","0","Output is ~DIR when counter matches CCx value")
    tccSym_Channel_Polarity[channelID].addKey("HIGH","1","Output is DIR when counter matches CCx value")
    tccSym_Channel_Polarity[channelID].setOutputMode("Value")
    tccSym_Channel_Polarity[channelID].setDisplayMode("Description")
    tccSym_Channel_Polarity[channelID].setVisible(False)
    tccSym_Channel_Polarity[channelID].setDependencies(tccDualSlopeVisible, ["TCC_WAVE_WAVEGEN"])

    #output polarity for single slope
    tccSym_Channel_Polarity_NPWM.append(channelID)
    tccSym_Channel_Polarity_NPWM[channelID] = tccComponent.createKeyValueSetSymbol("TCC_"+str(channelID)+"_WAVE_POL_NPWM", tccSym_Channel_Menu[channelID])
    tccSym_Channel_Polarity_NPWM[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
    tccSym_Channel_Polarity_NPWM[channelID].setLabel("Output Polarity")
    tccSym_Channel_Polarity_NPWM[channelID].addKey("LOW","0","Output is ~DIR and set to DIR when counter matches CCx value")
    tccSym_Channel_Polarity_NPWM[channelID].addKey("HIGH","1","Output is DIR and set to ~DIR when counter matches CCx value")
    tccSym_Channel_Polarity_NPWM[channelID].setOutputMode("Value")
    tccSym_Channel_Polarity_NPWM[channelID].setDisplayMode("Description")
    tccSym_Channel_Polarity_NPWM[channelID].setVisible(True)
    tccSym_Channel_Polarity_NPWM[channelID].setDependencies(tccSingleSlopeVisible, ["TCC_WAVE_WAVEGEN"])

    if (deadTimeImplemented != 0 and (channelID < (numOfOutputs/2))):
        #dead time
        tccSym_Channel_WEXCTRL_DTIEN.append(channelID)
        tccSym_Channel_WEXCTRL_DTIEN[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WEXCTRL_DTIEN", tccSym_Channel_Menu[channelID])
        tccSym_Channel_WEXCTRL_DTIEN[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WEXCTRL")
        tccSym_Channel_WEXCTRL_DTIEN[channelID].setLabel("Enable Dead Time")
        tccSym_Channel_WEXCTRL_DTIEN[channelID].setDefaultValue(True)

    if (swapImplemented == 1 and (channelID < (numOfOutputs/2))):
        #swap dead time outputs
        tccSym_Channel_WAVE_SWAP.append(channelID)
        tccSym_Channel_WAVE_SWAP[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WAVE_SWAP", tccSym_Channel_Menu[channelID])
        tccSym_Channel_WAVE_SWAP[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
        tccSym_Channel_WAVE_SWAP[channelID].setLabel("Swap Outputs")
        tccSym_Channel_WAVE_SWAP[channelID].setDefaultValue(False)

    if ((channelID < (numOfOutputs/2))):
        #circular buffer
        tccSym_Channel_WAVE_CICCEN.append(channelID)
        tccSym_Channel_WAVE_CICCEN[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WAVE_CICCEN", tccSym_Channel_Menu[channelID])
        tccSym_Channel_WAVE_CICCEN[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
        tccSym_Channel_WAVE_CICCEN[channelID].setLabel("Enable Circular Buffer")
        tccSym_Channel_WAVE_CICCEN[channelID].setDefaultValue(False)   
        tccSym_Channel_WAVE_CICCEN[channelID].setVisible(False) 
        tccSym_Channel_WAVE_CICCEN[channelID].setDependencies(tccCircularBufferVisible, ["TCC_WAVE_WAVEGEN"])

    #compare match event out
    tccSym_Channel_INTENSET_MC.append(channelID)
    tccSym_Channel_INTENSET_MC[channelID] = tccComponent.createBooleanSymbol("TCC_INTENSET_MC_"+str(channelID), tccSym_Channel_Menu[channelID])
    tccSym_Channel_INTENSET_MC[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:INTENSET")
    tccSym_Channel_INTENSET_MC[channelID].setLabel("Enable Compare Match Interrupt")
    tccSym_Channel_INTENSET_MC[channelID].setDefaultValue(False)
    interruptDepList.append("TCC_INTENSET_MC_"+str(channelID))
    pwmInterruptDepList.append("TCC_INTENSET_MC_"+str(channelID))

    #compare match event out
    tccSym_Channel_EVCTRL_MCEO.append(channelID)
    tccSym_Channel_EVCTRL_MCEO[channelID] = tccComponent.createBooleanSymbol("TCC_EVCTRL_MCEO_"+str(channelID), tccSym_Channel_Menu[channelID])
    tccSym_Channel_EVCTRL_MCEO[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
    tccSym_Channel_EVCTRL_MCEO[channelID].setLabel("Enable Compare Match Event OUT")
    tccSym_Channel_EVCTRL_MCEO[channelID].setDefaultValue(False)
    eventDepList.append("TCC_EVCTRL_MCEO_"+str(channelID))

    #compare match event in
    tccSym_Channel_EVCTRL_MCEI.append(channelID)
    tccSym_Channel_EVCTRL_MCEI[channelID] = tccComponent.createBooleanSymbol("TCC_EVCTRL_MCEI_"+str(channelID), tccSym_Channel_Menu[channelID])
    tccSym_Channel_EVCTRL_MCEI[channelID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
    tccSym_Channel_EVCTRL_MCEI[channelID].setLabel("Enable Compare Match Event IN")
    tccSym_Channel_EVCTRL_MCEI[channelID].setDefaultValue(False)
    eventDepList.append("TCC_EVCTRL_MCEI_"+str(channelID))

#Invert outputs
tccSym_Outputs_Menu = tccComponent.createMenuSymbol("TCC_OUTPUTS", tccSym_PWMMenu)
tccSym_Outputs_Menu.setLabel("Outputs")

for output in range (0, numOfOutputs):
    tccSym_DRVCTRL_INVEN = tccComponent.createBooleanSymbol("TCC_DRVCTRL_INVEN"+str(output), tccSym_Outputs_Menu)
    tccSym_DRVCTRL_INVEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:DRVCTRL")
    tccSym_DRVCTRL_INVEN.setLabel("Invert Output " + str(output))

#dead time menu
tccSym_DeadTime_Menu = tccComponent.createMenuSymbol("TCC_DEAD_TIME_MENU", tccSym_PWMMenu)
tccSym_DeadTime_Menu.setLabel("Dead Time")
if (deadTimeImplemented == 0):
    tccSym_DeadTime_Menu.setVisible(False)
else:
    tccSym_DeadTime_Menu.setVisible(True)
tccSym_DeadTime_Menu.setDependencies(tccDeadTimeVisible, ["TCC_0_WEXCTRL_DTIEN","TCC_1_WEXCTRL_DTIEN", "TCC_2_WEXCTRL_DTIEN", "TCC_3_WEXCTRL_DTIEN"])

#Low dead time
global tccSym_WEXCTRL_DTLS
tccSym_WEXCTRL_DTLS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTLS", tccSym_DeadTime_Menu)
tccSym_WEXCTRL_DTLS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WEXCTRL")
tccSym_WEXCTRL_DTLS.setLabel("Dead Time for Low Side Output")
tccSym_WEXCTRL_DTLS.setDefaultValue(64)
tccSym_WEXCTRL_DTLS.setMin(0)
tccSym_WEXCTRL_DTLS.setMax(255)

if clock_freq != 0:
    low_deadtime = (tccSym_WEXCTRL_DTLS.getValue() * 1000000.0 / (clock_freq))
else:
    low_deadtime = 0

tccSym_DTLS_COMMENT = tccComponent. createCommentSymbol("TCC_DTLS_COMMENT", tccSym_DeadTime_Menu)
tccSym_DTLS_COMMENT.setLabel("**** Low side dead time is "+str(low_deadtime)+ " uS ****")
tccSym_DTLS_COMMENT.setDependencies(tccDeadTimeCalc, ["TCC_WEXCTRL_DTLS", "core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_CTRLA_PRESCALER"])

#High dead time
global tccSym_WEXCTRL_DTHS
tccSym_WEXCTRL_DTHS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTHS", tccSym_DeadTime_Menu)
tccSym_WEXCTRL_DTHS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WEXCTRL")
tccSym_WEXCTRL_DTHS.setLabel("Dead Time for High Side Output")
tccSym_WEXCTRL_DTHS.setDefaultValue(64)
tccSym_WEXCTRL_DTHS.setMin(0)
tccSym_WEXCTRL_DTHS.setMax(255)

if clock_freq != 0:
    high_deadtime = (tccSym_WEXCTRL_DTHS.getValue() * 1000000.0 / (clock_freq))
else:
    high_deadtime =0

tccSym_DTHS_COMMENT = tccComponent. createCommentSymbol("TCC_DTHS_COMMENT", tccSym_DeadTime_Menu)
tccSym_DTHS_COMMENT.setLabel("**** High side dead time is "+str(high_deadtime)+ " uS ****")
tccSym_DTHS_COMMENT.setDependencies(tccDeadTimeCalc, ["TCC_WEXCTRL_DTHS", "core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_CTRLA_PRESCALER"])


if (patternGenImplemented == 1):
    #Pattern Generation menu
    tccSym_PatGen_Menu = tccComponent.createMenuSymbol("TCC_PATGEN_MENU", tccSym_PWMMenu)
    tccSym_PatGen_Menu.setLabel("Pattern Generation")

    for output in range(0, numOfOutputs):
        tccSym_PATT_PGE.append(output)
        tccSym_PATT_PGE[output] = tccComponent.createBooleanSymbol("TCC_"+str(output)+"PATT_PGE", tccSym_PatGen_Menu)
        tccSym_PATT_PGE[output].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:PATT")
        tccSym_PATT_PGE[output].setLabel("Enable for Output " +str(output))
        tccSym_PATT_PGE[output].setDefaultValue(False)

        tccSym_PATT_PGV.append(output)
        tccSym_PATT_PGV[output] = tccComponent.createKeyValueSetSymbol("TCC_"+str(output)+"PATT_PGV", tccSym_PATT_PGE[output])
        tccSym_PATT_PGV[output].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:PATT")
        tccSym_PATT_PGV[output].setLabel("Select Pattern Level for Output " +str(output))
        tccSym_PATT_PGV[output].setVisible(False)
        tccSym_PATT_PGV[output].addKey("Low", "0", "Low")
        tccSym_PATT_PGV[output].addKey("High", "1", "High")
        tccSym_PATT_PGV[output].setOutputMode("Value")
        tccSym_PATT_PGV[output].setDisplayMode("Description")
        tccSym_PATT_PGV[output].setDependencies(tccPattgenVisible, ["TCC_"+str(output)+"PATT_PGE"])

#### Ramp #####
# Ramp feature is available only for NPWM mode
tccSym_Ramp_Menu = tccComponent.createMenuSymbol("TCC_RAMP_MENU", tccSym_PWMMenu)
tccSym_Ramp_Menu.setLabel("Ramp Configurations")
tccSym_Ramp_Menu.setDependencies (tccRampMenuVisible, ["TCC_WAVE_WAVEGEN"])

global tccSym_WAVE_RAMP
tccSym_WAVE_RAMP = tccComponent.createKeyValueSetSymbol("TCC_WAVE_RAMP", tccSym_Ramp_Menu)
tccSym_WAVE_RAMP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
tccSym_WAVE_RAMP.setLabel("Select Ramp")
tcc = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]/value-group@[name=\"TCC_WAVE__RAMP\"]")
childrenNodes = tcc.getChildren()
for param in range(0, len(childrenNodes)):
    tccSym_WAVE_RAMP.addKey(childrenNodes[param].getAttribute("name"), childrenNodes[param].getAttribute("value"),
        childrenNodes[param].getAttribute("caption"))
tccSym_WAVE_RAMP.setDefaultValue(0)
tccSym_WAVE_RAMP.setOutputMode("Key")
tccSym_WAVE_RAMP.setDisplayMode("Key")

#Cycle A and cycle B menu will be visible only for RAMP2, RAMP2A, RAMP2C
tccSym_Ramp_CycleA_Menu = tccComponent.createMenuSymbol("TCC_RAMP_CYCLEA", tccSym_Ramp_Menu)
tccSym_Ramp_CycleA_Menu.setLabel("Cycle A")
tccSym_Ramp_CycleA_Menu.setVisible(False)
tccSym_Ramp_CycleA_Menu.setDependencies(tccRampCycleMenuVisible, ["TCC_WAVE_RAMP"])

if size == 32:
    tccSym_Ramp_Period = tccComponent.createLongSymbol("TCC_RAMP_CYCLEA_PERIOD", tccSym_Ramp_CycleA_Menu)
else:
    tccSym_Ramp_Period = tccComponent.createIntegerSymbol("TCC_RAMP_CYCLEA_PERIOD", tccSym_Ramp_CycleA_Menu)
    tccSym_Ramp_Period.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:%NOREGISTER%")
tccSym_Ramp_Period.setLabel("Cycle A Period Value (PER)")
tccSym_Ramp_Period.setValue(tccSym_PER_PER.getValue())
tccSym_Ramp_Period.setReadOnly(True)
tccSym_Ramp_Period.setDependencies(tccRampAPeriodCalc, ["TCC_WAVE_RAMP", "TCC_PER_PER", "TCC_0_CC"])

tccSym_WAVE_CICCEN0 = tccComponent.createBooleanSymbol("TCC_WAVE_CICCEN0", tccSym_Ramp_CycleA_Menu)
tccSym_WAVE_CICCEN0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
tccSym_WAVE_CICCEN0.setLabel("Enable CC0 Circular Buffer")
tccSym_WAVE_CICCEN0.setDefaultValue(True)
tccSym_WAVE_CICCEN0.setVisible(False)
tccSym_WAVE_CICCEN0.setReadOnly(True)
tccSym_WAVE_CICCEN0.setDependencies(tccRampCCBuffer, ["TCC_WAVE_RAMP"])

if size == 32:
    tccSym_Ramp_Ch1_Duty = tccComponent.createLongSymbol("TCC_RAMP_CH1_DUTY", tccSym_Ramp_CycleA_Menu)
else:
    tccSym_Ramp_Ch1_Duty = tccComponent.createIntegerSymbol("TCC_RAMP_CH1_DUTY", tccSym_Ramp_CycleA_Menu)
    tccSym_Ramp_Ch1_Duty.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:%NOREGISTER%")
tccSym_Ramp_Ch1_Duty.setLabel("Cycle A Duty Value")
tccSym_Ramp_Ch1_Duty.setValue(0)
tccSym_Ramp_Ch1_Duty.setReadOnly(True)
tccSym_Ramp_Ch1_Duty.setDependencies(tccRampADutyCalc, ["TCC_WAVE_RAMP", "TCC_0_CC", "TCC_2_CC"])

tccSym_Ramp_CycleB_Menu = tccComponent.createMenuSymbol("TCC_RAMP_CYCLEB", tccSym_Ramp_Menu)
tccSym_Ramp_CycleB_Menu.setLabel("Cycle B")
tccSym_Ramp_CycleB_Menu.setVisible(False)
tccSym_Ramp_CycleB_Menu.setDependencies(tccRampCycleMenuVisible, ["TCC_WAVE_RAMP"])

global tccSym_WAVE_CIPEREN
tccSym_WAVE_CIPEREN = tccComponent.createBooleanSymbol("TCC_WAVE_CIPEREN", tccSym_Ramp_CycleB_Menu)
tccSym_WAVE_CIPEREN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:WAVE")
tccSym_WAVE_CIPEREN.setLabel("Enable Period Circular Buffer")
tccSym_WAVE_CIPEREN.setDependencies(tccRampPeriodCirBuf, ["TCC_WAVE_RAMP"])

if size == 32:
    tccSym_Ramp_CycleB_Period = tccComponent.createLongSymbol("TCC_RAMP_CYCLEB_PERIOD", tccSym_Ramp_CycleB_Menu)
else:
    tccSym_Ramp_CycleB_Period = tccComponent.createIntegerSymbol("TCC_RAMP_CYCLEB_PERIOD", tccSym_Ramp_CycleB_Menu)
    tccSym_Ramp_CycleB_Period.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:%NOREGISTER%")
tccSym_Ramp_CycleB_Period.setLabel("Cycle B Period Value (PER)")
tccSym_Ramp_CycleB_Period.setValue(tccSym_PER_PER.getValue())
tccSym_Ramp_CycleB_Period.setReadOnly(True)
tccSym_Ramp_CycleB_Period.setDependencies(tccRampBPeriodCalc, ["TCC_PER_PER"])

if size == 32:
    tccSym_Ramp_Ch2_Duty = tccComponent.createLongSymbol("TCC_RAMP_CH2_DUTY", tccSym_Ramp_CycleB_Menu)
else:
    tccSym_Ramp_Ch2_Duty = tccComponent.createIntegerSymbol("TCC_RAMP_CH2_DUTY", tccSym_Ramp_CycleB_Menu)
    tccSym_Ramp_Ch2_Duty.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:%NOREGISTER%")
tccSym_Ramp_Ch2_Duty.setLabel("Cycle B Duty Value")
tccSym_Ramp_Ch2_Duty.setDependencies(tccRampBdutyCalc, ["TCC_WAVE_RAMP", "TCC_0_CC", "TCC_1_CC"])
tccSym_Ramp_Ch2_Duty.setReadOnly(True)


##### Input Events ######
tccSym_InputEvents_Menu = tccComponent.createMenuSymbol("TCC_INPUT_EVENTS", tccSym_PWMMenu)
tccSym_InputEvents_Menu.setLabel("Input Events Configuration")

global tccSym_EVCTRL_EVACT0
tccSym_EVCTRL_EVACT0 = tccComponent.createKeyValueSetSymbol("TCC_EVCTRL_EVACT0", tccSym_InputEvents_Menu)
tccSym_EVCTRL_EVACT0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
tccSym_EVCTRL_EVACT0.setLabel("Select Input Event 0 Action")
tccSym_EVCTRL_EVACT0.addKey("OFF", "0", "Disabled")
tccSym_EVCTRL_EVACT0.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_EVCTRL_EVACT0.addKey("COUNTEV", "2", "Count on event")
tccSym_EVCTRL_EVACT0.addKey("START", "3", "Start counter")
tccSym_EVCTRL_EVACT0.addKey("INC", "4", "Increment counter")
tccSym_EVCTRL_EVACT0.addKey("COUNT", "5", "Count on active state of asynchronous event")
tccSym_EVCTRL_EVACT0.addKey("FAULT", "7", "Non-recoverable fault")
tccSym_EVCTRL_EVACT0.setDisplayMode("Description")
tccSym_EVCTRL_EVACT0.setOutputMode("Key")
eventDepList.append("TCC_EVCTRL_EVACT0")

tccSym_EVCTRL_TCINV0 = tccComponent.createBooleanSymbol("TCC_EVCTRL_TCINV0", tccSym_EVCTRL_EVACT0)
tccSym_EVCTRL_TCINV0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
tccSym_EVCTRL_TCINV0.setLabel("Invert Input Event 0")
tccSym_EVCTRL_TCINV0.setVisible(False)
tccSym_EVCTRL_TCINV0.setDependencies(tccPwmIpEventVisible, ["TCC_EVCTRL_EVACT0"])

global tccSym_EVCTRL_EVACT1
tccSym_EVCTRL_EVACT1 = tccComponent.createKeyValueSetSymbol("TCC_EVCTRL_EVACT1", tccSym_InputEvents_Menu)
tccSym_EVCTRL_EVACT1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
tccSym_EVCTRL_EVACT1.setLabel("Select Input Event 1 Action")
tccSym_EVCTRL_EVACT1.addKey("OFF", "0", "Disabled")
tccSym_EVCTRL_EVACT1.addKey("RETRIGGER", "1", "Start, restart or retrigger counter")
tccSym_EVCTRL_EVACT1.addKey("DIR", "2", "Direction control")
tccSym_EVCTRL_EVACT1.addKey("STOP", "3", "Stop counter")
tccSym_EVCTRL_EVACT1.addKey("DEC", "4", "Decrement counter")
tccSym_EVCTRL_EVACT1.addKey("FAULT", "7", "Non-recoverable fault")
tccSym_EVCTRL_EVACT1.setDisplayMode("Description")
tccSym_EVCTRL_EVACT1.setOutputMode("Key")
eventDepList.append("TCC_EVCTRL_EVACT1")

tccSym_EVCTRL_TCINV1 = tccComponent.createBooleanSymbol("TCC_EVCTRL_TCINV1", tccSym_EVCTRL_EVACT1)
tccSym_EVCTRL_TCINV1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:EVCTRL")
tccSym_EVCTRL_TCINV1.setLabel("Invert Input Event 1")
tccSym_EVCTRL_TCINV1.setVisible(False)
tccSym_EVCTRL_TCINV1.setDependencies(tccPwmIpEventVisible, ["TCC_EVCTRL_EVACT1"])

#Fault menu
tccSym_Fault_Menu = tccComponent.createMenuSymbol("TCC_FAULT_MENU", tccSym_PWMMenu)
tccSym_Fault_Menu.setLabel("Fault Configurations")

tccSym_Fault_Comment = tccComponent.createCommentSymbol("TCC_FAULT_COMMENT", tccSym_Fault_Menu)
tccSym_Fault_Comment.setLabel("**** Select input event action as non-recoverable fault ****")
tccSym_Fault_Comment.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])

#fault filter value
tccSym_DRVCTRL_FILTERVAL = tccComponent.createIntegerSymbol("TCC_DRVCTRL_FILTERVAL", tccSym_Fault_Menu)
tccSym_DRVCTRL_FILTERVAL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:DRVCTRL")
tccSym_DRVCTRL_FILTERVAL.setLabel(" Fault 0 Filter Value")
tccSym_DRVCTRL_FILTERVAL.setMin(0)
tccSym_DRVCTRL_FILTERVAL.setMax(15)
tccSym_DRVCTRL_FILTERVAL.setDefaultValue(0)
tccSym_DRVCTRL_FILTERVAL.setVisible(False)
tccSym_DRVCTRL_FILTERVAL.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])

tccSym_DRVCTRL_FILTERVAL1 = tccComponent.createIntegerSymbol("TCC_DRVCTRL_FILTERVAL1", tccSym_Fault_Menu)
tccSym_DRVCTRL_FILTERVAL1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:DRVCTRL")
tccSym_DRVCTRL_FILTERVAL1.setLabel(" Fault 1 Filter Value")
tccSym_DRVCTRL_FILTERVAL1.setMin(0)
tccSym_DRVCTRL_FILTERVAL1.setMax(15)
tccSym_DRVCTRL_FILTERVAL1.setDefaultValue(0)
tccSym_DRVCTRL_FILTERVAL1.setVisible(False)
tccSym_DRVCTRL_FILTERVAL1.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])

#output polarity after fault
for output in range(0, numOfOutputs):
    tccSym_DRVCTRL_NRE_NRV.append(output)
    tccSym_DRVCTRL_NRE_NRV[output] = tccComponent.createKeyValueSetSymbol("TCC_"+str(output)+"_DRVCTRL_NRE_NRV", tccSym_Fault_Menu)
    tccSym_DRVCTRL_NRE_NRV[output].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:DRVCTRL")
    tccSym_DRVCTRL_NRE_NRV[output].setLabel("Select Level for Output " +str(output))
    tccSym_DRVCTRL_NRE_NRV[output].setVisible(False)
    tccSym_DRVCTRL_NRE_NRV[output].addKey("Tri-state", "-1", "Tri-state")
    tccSym_DRVCTRL_NRE_NRV[output].addKey("Low", "0", "Low")
    tccSym_DRVCTRL_NRE_NRV[output].addKey("High", "1", "High")
    tccSym_DRVCTRL_NRE_NRV[output].setOutputMode("Value")
    tccSym_DRVCTRL_NRE_NRV[output].setDisplayMode("Description")
    tccSym_DRVCTRL_NRE_NRV[output].setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])

tccSym_INTENSET_FAULT0 = tccComponent.createBooleanSymbol("TCC_INTENSET_FAULT0", tccSym_Fault_Menu)
tccSym_INTENSET_FAULT0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:INTENSET")
tccSym_INTENSET_FAULT0.setLabel("Enable Fault 0 Interrupt")
tccSym_INTENSET_FAULT0.setDefaultValue(False)
tccSym_INTENSET_FAULT0.setVisible(False)
tccSym_INTENSET_FAULT0.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])
interruptDepList.append("TCC_INTENSET_FAULT0")
pwmInterruptDepList.append("TCC_INTENSET_FAULT0")

tccSym_INTENSET_FAULT1 = tccComponent.createBooleanSymbol("TCC_INTENSET_FAULT1", tccSym_Fault_Menu)
tccSym_INTENSET_FAULT1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:INTENSET")
tccSym_INTENSET_FAULT1.setLabel("Enable Fault 1 Interrupt")
tccSym_INTENSET_FAULT1.setDefaultValue(False)
tccSym_INTENSET_FAULT1.setVisible(False)
tccSym_INTENSET_FAULT1.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT0", "TCC_EVCTRL_EVACT1"])
interruptDepList.append("TCC_INTENSET_FAULT1")
pwmInterruptDepList.append("TCC_INTENSET_FAULT1")

pwmInterruptDepList.append("TCC_OPERATION_MODE")
tccSym_PWM_Interrupt_Mode = tccComponent.createBooleanSymbol("TCC_PWM_INTERRUPT_MODE", None)
tccSym_PWM_Interrupt_Mode.setVisible(False)
tccSym_PWM_Interrupt_Mode.setDependencies(tccPwmInterruptMode, pwmInterruptDepList)

eventDepList.append("TCC_OPERATION_MODE")
tccSym_EVSYS_CONFIGURE = tccComponent.createIntegerSymbol("TCC_EVSYS_CONFIGURE", None)
tccSym_EVSYS_CONFIGURE.setVisible(False)
tccSym_EVSYS_CONFIGURE.setDependencies(tccEvsys, eventDepList)