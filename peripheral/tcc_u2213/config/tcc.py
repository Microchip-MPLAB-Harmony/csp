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

global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock = []
global InterruptVectorUpdate
InterruptVectorUpdate = []
global tccInstanceName
global intPrev
intPrev =  0
global numOfChannels

tccSym_Channel_Menu = []
tccSym_Channel_CC = []
tccSym_Channel_Polarity = []
tccSym_Channel_WAVE_SWAP = []
tccSym_Channel_WEXCTRL_DTIEN = []
tccSym_Channel_INTENSET_MC = []
tccSym_Channel_EVCTRL_MCEO = []
tccSym_DRVCTRL_NRE_NRV = []
tccSym_PATT_PGE = []
tccSym_PATT_PGV = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def tccEvsys(symbol, event):
    if(event["id"] == "TCC_EVCTRL_OVFEO"):
        Database.setSymbolValue("evsys", "GENERATOR_"+str(tccInstanceName.getValue())+"_OVF_ACTIVE", event["value"], 2)

    if(event["id"] == "TCC_EVCTRL_EVACT"):
        Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_0_READY", False, 2)
        Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_1_READY", False, 2)
        if (event["value"] == "Event 0 Rising Edge" or event["value"] == "Event 0 Falling Edge"):
            Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_0_READY", True, 2)
        elif (event["value"] == "Event 1 Rising Edge" or event["value"] == "Event 1 Falling Edge"):
            Database.setSymbolValue("evsys", "USER_"+str(tccInstanceName.getValue())+"_EV_1_READY", True, 2)

    if("EVCTRL_MC" in event["id"]):
        mcInstance = event["id"].split("_")[2:]
        event_name = "_" + "_".join(mcInstance)
        print(event_name)
        Database.setSymbolValue("evsys", "GENERATOR_"+str(tccInstanceName.getValue())+ str(event_name)+"_ACTIVE", event["value"], 2)

def updateTCCInterruptStatus(symbol, event):
    component = symbol.getComponent()
    # For single interrupt line for peripheral
    if len(InterruptVector) == 1:
        if (component.getSymbolValue("TCC_INTENSET_OVF") or component.getSymbolValue("TCC_INTENSET_FAULT0") or
        component.getSymbolValue("TCC_INTENSET_FAULT1")):
            Database.setSymbolValue("core", InterruptVector[0], True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], True, 2)
            Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_PWMInterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptVector[0], False, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], False, 2)
            Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_Handler", 2)
    # For multiple interrupt lines for peripheral
    else:
        if (event["id"] == "TCC_INTENSET_OVF") or (event["id"] == "TCC_INTENSET_FAULT0") or (event["id"] == "TCC_INTENSET_FAULT1"):
            if (component.getSymbolValue("TCC_INTENSET_OVF") or component.getSymbolValue("TCC_INTENSET_FAULT0") or
            component.getSymbolValue("TCC_INTENSET_FAULT1")):
                Database.setSymbolValue("core", InterruptVector[0], True, 2)
                Database.setSymbolValue("core", InterruptHandlerLock[0], True, 2)
                Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_PWMInterruptHandler", 2)
            else:
                Database.setSymbolValue("core", InterruptVector[0], False, 2)
                Database.setSymbolValue("core", InterruptHandlerLock[0], False, 2)
                Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_Handler", 2)
        else:
            mcInstance = int(event["id"].split("_")[-1])
            Database.setSymbolValue("core", InterruptVector[mcInstance+1], event["value"], 2)
            Database.setSymbolValue("core", InterruptHandlerLock[mcInstance+1], event["value"], 2)
            if event["value"] == True:
                Database.setSymbolValue("core", InterruptHandler[mcInstance+1], InterruptHandler[mcInstance+1].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)
            else:
                Database.setSymbolValue("core", InterruptHandler[mcInstance+1], InterruptHandler[mcInstance+1].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)
                
def updateTCCInterruptWarningStatus(symbol, event):
    global InterruptVectorUpdate
    global numOfChannels
    isVisible = False
    component = symbol.getComponent()
    if (component.getSymbolValue("TCC_INTENSET_OVF") or component.getSymbolValue("TCC_INTENSET_FAULT0") or
        component.getSymbolValue("TCC_INTENSET_FAULT1")):
        if (Database.getSymbolValue("core", InterruptVectorUpdate[0].split(".")[-1]) == True):
            isVisible = True
    else:
        for i in range(0, numOfChannels):
            if (component.getSymbolValue("TCC_INTENSET_MC_"+str(i)) == True):
                if (Database.getSymbolValue("core", InterruptVectorUpdate[1].split(".")[-1]) == True):
                    isVisible = True
    if (isVisible == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTCCClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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
    if(event["value"] == "Disabled"):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tccDeadTimeVisible(symbol, event):
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
        period = tccSym_PER_PER.getValue() + 1
        if (tccSym_WAVE_WAVEGEN.getValue() == 0): #single slope PWM
            slope = 1
        else:
            slope = 2
        frequency = ((clock_freq / prescaler) / period) / slope
        symbol.setLabel("**** PWM Frequency is " +str(frequency)+ " Hz ****")
        symbol.setVisible(True)
    elif (event["id"] == "TCC_SLAVE_MODE"):
        symbol.setVisible(not event["value"])
    
def tccDeadTimeCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    if (symbol.getID() == "TCC_DTLS_COMMENT"):
        dead_time = (tccSym_WEXCTRL_DTLS.getValue() * 1000000.0 / (clock_freq / prescaler))
        symbol.setLabel("**** Low side dead time is "+str(dead_time)+ " uS ****")
    if (symbol.getID() == "TCC_DTHS_COMMENT"):
        dead_time = (tccSym_WEXCTRL_DTHS.getValue() * 1000000.0 / (clock_freq / prescaler))
        symbol.setLabel("**** High side dead time is "+str(dead_time)+ " uS ****")

def tccSlaveCommentVisible(symbol, event):
    symbol.setVisible(event["value"])

def tccFault0IntVisible(symbol, event):
    if ("Event 0" in event["value"]):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
    
def tccFault1IntVisible(symbol, event):
    if ("Event 1" in event["value"]):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccSlaveModeVisibility(symbol, event):
    print(not event["value"])
    symbol.setVisible(not event["value"])
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tccComponent):

    global InterruptVector 
    global InterruptHandler
    global InterruptHandlerLock
    global tccInstanceName
    global tccSym_INTENSET_OVF
    global InterruptVectorUpdate
    eventDepList = []
    interruptDepList = []

    tccInstanceName = tccComponent.createStringSymbol("TCC_INSTANCE_NAME", None)
    tccInstanceName.setVisible(False)
    tccInstanceName.setDefaultValue(tccComponent.getID().upper())
    
    #clock enable
    Database.setSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    ################################ ATDF ####################################################
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters")
    global numOfChannels
    numOfChannels = 4
    deadTimeImplemented = 1
    swapImplemented = 1
    outputMatrixImplemented = 1
    patternGenImplemented = 1
    numOfOutputs = 8
    size = 24
    parameters = []
    parameters = node.getChildren()
    for param in range (0, len(parameters)):
        if(parameters[param].getAttribute("name") == "CC_NUM"):
            numOfChannels = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "DTI"):
            deadTimeImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "SWAP"):
            swapImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "OTMX"):
            outputMatrixImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "OW_NUM"):
            numOfOutputs = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "PG"):
            patternGenImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "SIZE"):
            size = int(parameters[param].getAttribute("value"))
            
    tccSym_NUM_CHANNELS = tccComponent.createIntegerSymbol("TCC_NUM_CHANNELS", None)
    tccSym_NUM_CHANNELS.setDefaultValue(int(numOfChannels))
    tccSym_NUM_CHANNELS.setVisible(False)
    
    tccSym_NUM_OUTPUTS = tccComponent.createIntegerSymbol("TCC_NUM_OUTPUTS", None)
    tccSym_NUM_OUTPUTS.setDefaultValue(int(numOfOutputs))
    tccSym_NUM_OUTPUTS.setVisible(False)
    
    tccSym_Is_DeadTime = tccComponent.createIntegerSymbol("TCC_IS_DEAD_TIME", None)
    tccSym_Is_DeadTime.setDefaultValue(int(deadTimeImplemented))
    tccSym_Is_DeadTime.setVisible(False)
    
    tccSym_Is_Swap = tccComponent.createIntegerSymbol("TCC_IS_SWAP", None)
    tccSym_Is_Swap.setDefaultValue(int(swapImplemented))
    tccSym_Is_Swap.setVisible(False)
    
    tccSym_Is_OTM = tccComponent.createIntegerSymbol("TCC_IS_OTM", None)
    tccSym_Is_OTM.setDefaultValue(int(outputMatrixImplemented))
    tccSym_Is_OTM.setVisible(False)
    
    tccSym_Is_PG = tccComponent.createIntegerSymbol("TCC_IS_PG", None)
    tccSym_Is_PG.setDefaultValue(int(patternGenImplemented))
    tccSym_Is_PG.setVisible(False)
    
    tccSym_SIZE = tccComponent.createIntegerSymbol("TCC_SIZE", None)
    tccSym_SIZE.setDefaultValue(int(size))
    tccSym_SIZE.setVisible(False)
    
    tccSym_MCU_FAMILY = tccComponent.createStringSymbol("TCC_MCU_FAMILY", None)
    tccSym_MCU_FAMILY.setVisible(False)
    node = ATDF.getNode("/avr-tools-device-file/devices")
    series = node.getChildren()[0].getAttribute("family")
    tccSym_MCU_FAMILY.setDefaultValue(node.getChildren()[0].getAttribute("family"))
    
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]/register-group@[name=\"TCC\"]")
    register_names = []
    register_names = node.getChildren()
    
    tccSym_CBUF_REG_NAME = tccComponent.createStringSymbol("TCC_CBUF_REG_NAME", None)
    tccSym_CBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "CCBUF" in register_names[index].getAttribute("name"):
            tccSym_CBUF_REG_NAME.setDefaultValue("CCBUF")
            break
        else:
            tccSym_CBUF_REG_NAME.setDefaultValue("CCB")
         
    tccSym_PBUF_REG_NAME = tccComponent.createStringSymbol("TCC_PBUF_REG_NAME", None)
    tccSym_PBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "PERBUF" in register_names[index].getAttribute("name"):
            tccSym_PBUF_REG_NAME.setDefaultValue("PERBUF")
            break
        else:
            tccSym_PBUF_REG_NAME.setDefaultValue("PERB")

    tccSym_PATBUF_REG_NAME = tccComponent.createStringSymbol("TCC_PATBUF_REG_NAME", None)
    tccSym_PATBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "PATTBUF" in register_names[index].getAttribute("name"):
            tccSym_PATBUF_REG_NAME.setDefaultValue("PATTBUF")
            break
        else:
            tccSym_PATBUF_REG_NAME.setDefaultValue("PATTB")
            
    # master slave mode
    tccInstanceMasterValue = 0
    tccInstanceMasterNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters/param@[name=\"MASTER_SLAVE_MODE\"]")
    if (tccInstanceMasterNode != None):
        tccInstanceMasterValue = int(tccInstanceMasterNode.getAttribute("value"))
        if (tccInstanceMasterValue == 2):  #slave
            activeComponentList = Database.getActiveComponentIDs()
            temp = int(tccInstanceName.getValue().split("TCC")[1])
            masterComponentID = "TCC" + str(temp - 1)

    global tccSym_Slave_Mode
    tccSym_Slave_Mode = tccComponent.createBooleanSymbol("TCC_SLAVE_MODE", None)
    tccSym_Slave_Mode.setLabel("Enable Slave")
    tccSym_Slave_Mode.setDefaultValue(False)
    if ((tccInstanceMasterValue == 2)):
        tccSym_Slave_Mode.setVisible(True)
    else:
        tccSym_Slave_Mode.setVisible(False)
    
    if (tccInstanceMasterValue == 2):  #slave
        tccSym_Slave_Mode_Comment = tccComponent.createCommentSymbol("TCC_SLAVE_MODE_COMMENT", None)
        tccSym_Slave_Mode_Comment.setLabel("**** Ensure Master - " + str(masterComponentID) + " is in active components ****")
        tccSym_Slave_Mode_Comment.setVisible(False)
        tccSym_Slave_Mode_Comment.setDependencies(tccSlaveCommentVisible, ["TCC_SLAVE_MODE"])
    ###########################################################################################
    
    #prescaler configuration
    global tccSym_CTRLA_PRESCALER
    tccSym_CTRLA_PRESCALER = tccComponent.createKeyValueSetSymbol("TCC_CTRLA_PRESCALER", None)
    tccSym_CTRLA_PRESCALER.setLabel("Select Prescaler")
    tccSym_CTRLA_PRESCALER.setDefaultValue(0)
    tccSym_CTRLA_PRESCALER.setOutputMode("Key")
    tccSym_CTRLA_PRESCALER.setDisplayMode("Description")
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]/value-group@[name=\"TCC_CTRLA__PRESCALER\"]")
    values = []
    values = node.getChildren()
    for index in range(0, len(values)):
        tccSym_CTRLA_PRESCALER.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"), 
        values[index].getAttribute("caption"))
    tccSym_CTRLA_PRESCALER.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])
    
    #waveform option
    global tccSym_WAVE_WAVEGEN
    tccSym_WAVE_WAVEGEN = tccComponent.createKeyValueSetSymbol("TCC_WAVE_WAVEGEN", None)
    tccSym_WAVE_WAVEGEN.setLabel("Select PWM Type")
    tccSym_WAVE_WAVEGEN.setDefaultValue(0)
    tccSym_WAVE_WAVEGEN.setOutputMode("Key")
    tccSym_WAVE_WAVEGEN.setDisplayMode("Description")
    tccSym_WAVE_WAVEGEN.addKey("NPWM", "2", "Single slope PWM")
    tccSym_WAVE_WAVEGEN.addKey("DSBOTTOM", "5", "Dual slope PWM with interrupt/event when counter = ZERO")
    tccSym_WAVE_WAVEGEN.addKey("DSBOTH", "6", "Dual slope PWM with interrupt/event when counter = ZERO or counter = TOP")
    tccSym_WAVE_WAVEGEN.addKey("DSTOP", "7", "Dual slope PWM with interrupt/event when counter = TOP")
    tccSym_WAVE_WAVEGEN.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])

    tccSym_CTRLBSET_DIR = tccComponent.createBooleanSymbol("TCC_CTRLBSET_DIR", None)
    tccSym_CTRLBSET_DIR.setLabel("PWM Direction - Count Down")
    tccSym_CTRLBSET_DIR.setDefaultValue(False)
    tccSym_CTRLBSET_DIR.setDependencies(tccDirVisible, ["TCC_WAVE_WAVEGEN", "TCC_SLAVE_MODE"])
    
    if (outputMatrixImplemented == 1):
        tccSym_WEXCTRL_OTMX = tccComponent.createKeyValueSetSymbol("TCC_WEXCTRL_OTMX", None)
        tccSym_WEXCTRL_OTMX.setLabel("Select Output Matrix")
        tccSym_WEXCTRL_OTMX.setDefaultValue(0)
        tccSym_WEXCTRL_OTMX.setOutputMode("Value")
        tccSym_WEXCTRL_OTMX.setDisplayMode("Description")
        tccSym_WEXCTRL_OTMX.addKey("OTMX_0", "0", "Default Channel Outputs")
        tccSym_WEXCTRL_OTMX.addKey("OTMX_1", "1", "Modulo Half Number of Channel Outputs")
        tccSym_WEXCTRL_OTMX.addKey("OTMX_2", "2", "Only Channel 0 Outputs")
        tccSym_WEXCTRL_OTMX.addKey("OTMX_3", "3", "Channel 0 + Remaining Channel 1 Outputs")
        
    #Period Value
    global tccSym_PER_PER
    tccSym_PER_PER = tccComponent.createIntegerSymbol("TCC_PER_PER", None)
    tccSym_PER_PER.setLabel("Period Value")
    tccSym_PER_PER.setDefaultValue(2399)
    tccSym_PER_PER.setMin(0)
    tccSym_PER_PER.setMax(pow(2, size) - 1)
    tccSym_PER_PER.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])

    clock_freq = Database.getSymbolValue("core", tccInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])
    period = tccSym_PER_PER.getValue() + 1
    if (tccSym_WAVE_WAVEGEN.getValue() == 0):
        slope = 1
    else:
        slope = 2
    frequency = ((clock_freq / prescaler) / period) / slope
    #Calculated frequency
    tccSym_Frequency = tccComponent.createCommentSymbol("TCC_FREQUENCY", None)
    tccSym_Frequency.setLabel("**** PWM Frequency is "+str(frequency)+" Hz ****")
    tccSym_Frequency.setDependencies(tccPWMFreqCalc, ["core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_PER_PER", "TCC_WAVE_WAVEGEN", "TCC_CTRLA_PRESCALER", "TCC_SLAVE_MODE"])
    
    #Period interrupt
    tccSym_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_INTENSET_OVF", None)
    tccSym_INTENSET_OVF.setLabel("Enable Period Interrupt")
    tccSym_INTENSET_OVF.setDefaultValue(False)
    interruptDepList.append("TCC_INTENSET_OVF")
    
    #Period out event
    tccSym_EVCTRL_OVFEO = tccComponent.createBooleanSymbol("TCC_EVCTRL_OVFEO", None)
    tccSym_EVCTRL_OVFEO.setLabel("Enable Period Event Out")
    tccSym_EVCTRL_OVFEO.setDefaultValue(False)
    eventDepList.append("TCC_EVCTRL_OVFEO")
    
    tccSym_MainChannel_Menu = tccComponent.createMenuSymbol("TCC_CHANNEL", None)
    tccSym_MainChannel_Menu.setLabel("Channel Configurations")
    
    for channelID in range(0, int(numOfChannels)):
        #channel menu
        tccSym_Channel_Menu.append(channelID)
        tccSym_Channel_Menu[channelID] = tccComponent.createMenuSymbol("TCC_CHANNEL"+str(channelID), tccSym_MainChannel_Menu)
        tccSym_Channel_Menu[channelID].setLabel("Channel "+str(channelID))
        
        #Duty
        tccSym_Channel_CC.append(channelID)
        tccSym_Channel_CC[channelID] = tccComponent.createIntegerSymbol("TCC_"+str(channelID)+"_CC", tccSym_Channel_Menu[channelID])
        tccSym_Channel_CC[channelID].setLabel("Duty Value")
        tccSym_Channel_CC[channelID].setMin(0)
        tccSym_Channel_CC[channelID].setMax(pow(2, size) - 1)

        #output polarity
        tccSym_Channel_Polarity.append(channelID)
        tccSym_Channel_Polarity[channelID] = tccComponent.createKeyValueSetSymbol("TCC_"+str(channelID)+"_WAVE_POL", tccSym_Channel_Menu[channelID])
        tccSym_Channel_Polarity[channelID].setLabel("Output Polarity")
        tccSym_Channel_Polarity[channelID].addKey("LOW","0","Waveform starts at low level")
        tccSym_Channel_Polarity[channelID].addKey("HIGH","1","Waveform starts at high level")
        tccSym_Channel_Polarity[channelID].setOutputMode("Value")
        tccSym_Channel_Polarity[channelID].setDisplayMode("Description")
        
        if (deadTimeImplemented == 1 and (channelID < (numOfOutputs/2))):
            #dead time
            tccSym_Channel_WEXCTRL_DTIEN.append(channelID)
            tccSym_Channel_WEXCTRL_DTIEN[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WEXCTRL_DTIEN", tccSym_Channel_Menu[channelID])
            tccSym_Channel_WEXCTRL_DTIEN[channelID].setLabel("Enable Dead Time")
            tccSym_Channel_WEXCTRL_DTIEN[channelID].setDefaultValue(True)
        
        if (swapImplemented == 1 and (channelID < (numOfOutputs/2))):
            #swap dead time outputs
            tccSym_Channel_WAVE_SWAP.append(channelID)
            tccSym_Channel_WAVE_SWAP[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WAVE_SWAP", tccSym_Channel_Menu[channelID])
            tccSym_Channel_WAVE_SWAP[channelID].setLabel("Swap Outputs")
            tccSym_Channel_WAVE_SWAP[channelID].setDefaultValue(False)
        
        #compare match event out
        tccSym_Channel_INTENSET_MC.append(channelID)
        tccSym_Channel_INTENSET_MC[channelID] = tccComponent.createBooleanSymbol("TCC_INTENSET_MC_"+str(channelID), tccSym_Channel_Menu[channelID])
        tccSym_Channel_INTENSET_MC[channelID].setLabel("Enable Compare Match Interrupt")
        tccSym_Channel_INTENSET_MC[channelID].setDefaultValue(False)
        interruptDepList.append("TCC_INTENSET_MC_"+str(channelID))
        
        #compare match event out
        tccSym_Channel_EVCTRL_MCEO.append(channelID)
        tccSym_Channel_EVCTRL_MCEO[channelID] = tccComponent.createBooleanSymbol("TCC_EVCTRL_MC_"+str(channelID), tccSym_Channel_Menu[channelID])
        tccSym_Channel_EVCTRL_MCEO[channelID].setLabel("Enable Compare Match Event Out")
        tccSym_Channel_EVCTRL_MCEO[channelID].setDefaultValue(False)
        eventDepList.append("TCC_EVCTRL_MC_"+str(channelID))

    #dead time menu
    tccSym_DeadTime_Menu = tccComponent.createMenuSymbol("TCC_DEAD_TIME_MENU", None)
    tccSym_DeadTime_Menu.setLabel("Dead Time")
    if (deadTimeImplemented == 1):
        tccSym_DeadTime_Menu.setVisible(True)
    else:
        tccSym_DeadTime_Menu.setVisible(False)
    tccSym_DeadTime_Menu.setDependencies(tccDeadTimeVisible, ["TCC_0_WEXCTRL_DTIEN","TCC_1_WEXCTRL_DTIEN", "TCC_2_WEXCTRL_DTIEN", "TCC_3_WEXCTRL_DTIEN"])
    
    #Low dead time
    global tccSym_WEXCTRL_DTLS
    tccSym_WEXCTRL_DTLS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTLS", tccSym_DeadTime_Menu)
    tccSym_WEXCTRL_DTLS.setLabel("Dead Time for Low Side Output")
    tccSym_WEXCTRL_DTLS.setDefaultValue(64)
    tccSym_WEXCTRL_DTLS.setMin(0)
    tccSym_WEXCTRL_DTLS.setMax(255)

    low_deadtime = (tccSym_WEXCTRL_DTLS.getValue() * 1000000.0 / (clock_freq / prescaler))

    tccSym_DTLS_COMMENT = tccComponent. createCommentSymbol("TCC_DTLS_COMMENT", tccSym_DeadTime_Menu)
    tccSym_DTLS_COMMENT.setLabel("**** Low side dead time is "+str(low_deadtime)+ " uS ****")
    tccSym_DTLS_COMMENT.setDependencies(tccDeadTimeCalc, ["TCC_WEXCTRL_DTLS", "core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_CTRLA_PRESCALER"])
    
    #High dead time
    global tccSym_WEXCTRL_DTHS
    tccSym_WEXCTRL_DTHS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTHS", tccSym_DeadTime_Menu)
    tccSym_WEXCTRL_DTHS.setLabel("Dead Time for High Side Output")
    tccSym_WEXCTRL_DTHS.setDefaultValue(64)
    tccSym_WEXCTRL_DTHS.setMin(0)
    tccSym_WEXCTRL_DTHS.setMax(255)

    high_deadtime = (tccSym_WEXCTRL_DTHS.getValue() * 1000000.0 / (clock_freq / prescaler))

    tccSym_DTHS_COMMENT = tccComponent. createCommentSymbol("TCC_DTHS_COMMENT", tccSym_DeadTime_Menu)
    tccSym_DTHS_COMMENT.setLabel("**** High side dead time is "+str(high_deadtime)+ " uS ****")
    tccSym_DTHS_COMMENT.setDependencies(tccDeadTimeCalc, ["TCC_WEXCTRL_DTHS", "core."+tccInstanceName.getValue()+"_CLOCK_FREQUENCY", "TCC_CTRLA_PRESCALER"])
    
    #Fault menu
    tccSym_Fault_Menu = tccComponent.createMenuSymbol("TCC_FAULT_MENU", None)
    tccSym_Fault_Menu.setLabel("Fault Configurations")
    
    #fault source
    fault_source = ["Disabled", "Event 0 Rising Edge", "Event 0 Falling Edge", "Event 1 Rising Edge", "Event 1 Falling Edge"]
    tccSym_EVCTRL_EVACT = tccComponent.createComboSymbol("TCC_EVCTRL_EVACT", tccSym_Fault_Menu, fault_source)
    tccSym_EVCTRL_EVACT.setLabel("Select Fault Source")
    eventDepList.append("TCC_EVCTRL_EVACT")
    
    #fault filter value
    tccSym_DRVCTRL_FILTERVAL = tccComponent.createIntegerSymbol("TCC_DRVCTRL_FILTERVAL", tccSym_EVCTRL_EVACT)
    tccSym_DRVCTRL_FILTERVAL.setLabel("Filter Value")
    tccSym_DRVCTRL_FILTERVAL.setMin(0)
    tccSym_DRVCTRL_FILTERVAL.setMax(15)
    tccSym_DRVCTRL_FILTERVAL.setDefaultValue(0)
    tccSym_DRVCTRL_FILTERVAL.setVisible(False)
    tccSym_DRVCTRL_FILTERVAL.setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT"])
    
    #output polarity after fault
    for output in range(0, numOfOutputs):
        tccSym_DRVCTRL_NRE_NRV.append(output)
        tccSym_DRVCTRL_NRE_NRV[output] = tccComponent.createKeyValueSetSymbol("TCC_"+str(output)+"_DRVCTRL_NRE_NRV", tccSym_EVCTRL_EVACT)
        tccSym_DRVCTRL_NRE_NRV[output].setLabel("Select Level for Output " +str(output))
        tccSym_DRVCTRL_NRE_NRV[output].setVisible(False)
        tccSym_DRVCTRL_NRE_NRV[output].addKey("Tri-state", "-1", "Tri-state")
        tccSym_DRVCTRL_NRE_NRV[output].addKey("Low", "0", "Low")
        tccSym_DRVCTRL_NRE_NRV[output].addKey("High", "1", "High")
        tccSym_DRVCTRL_NRE_NRV[output].setOutputMode("Value")
        tccSym_DRVCTRL_NRE_NRV[output].setDisplayMode("Description")
        tccSym_DRVCTRL_NRE_NRV[output].setDependencies(tccFaultVisible, ["TCC_EVCTRL_EVACT"])
    
    tccSym_INTENSET_FAULT0 = tccComponent.createBooleanSymbol("TCC_INTENSET_FAULT0", tccSym_EVCTRL_EVACT)
    tccSym_INTENSET_FAULT0.setLabel("Enable Fault 0 Interrupt")
    tccSym_INTENSET_FAULT0.setDefaultValue(False)
    tccSym_INTENSET_FAULT0.setVisible(False)
    tccSym_INTENSET_FAULT0.setDependencies(tccFault0IntVisible, ["TCC_EVCTRL_EVACT"])
    interruptDepList.append("TCC_INTENSET_FAULT0")
    
    tccSym_INTENSET_FAULT1 = tccComponent.createBooleanSymbol("TCC_INTENSET_FAULT1", tccSym_EVCTRL_EVACT)
    tccSym_INTENSET_FAULT1.setLabel("Enable Fault 1 Interrupt")
    tccSym_INTENSET_FAULT1.setDefaultValue(False)
    tccSym_INTENSET_FAULT1.setVisible(False)
    tccSym_INTENSET_FAULT1.setDependencies(tccFault1IntVisible, ["TCC_EVCTRL_EVACT"])
    interruptDepList.append("TCC_INTENSET_FAULT1")

    if (patternGenImplemented == 1):
        #Pattern Generation menu
        tccSym_PatGen_Menu = tccComponent.createMenuSymbol("TCC_PATGEN_MENU", None)
        tccSym_PatGen_Menu.setLabel("Pattern Generation")

        for output in range(0, numOfOutputs):
            tccSym_PATT_PGE.append(output)
            tccSym_PATT_PGE[output] = tccComponent.createBooleanSymbol("TCC_"+str(output)+"PATT_PGE", tccSym_PatGen_Menu)
            tccSym_PATT_PGE[output].setLabel("Enable for Output " +str(output))
            tccSym_PATT_PGE[output].setDefaultValue(False)
            
            tccSym_PATT_PGV.append(output)
            tccSym_PATT_PGV[output] = tccComponent.createKeyValueSetSymbol("TCC_"+str(output)+"PATT_PGV", tccSym_PATT_PGE[output])
            tccSym_PATT_PGV[output].setLabel("Select Pattern Level for Output " +str(output))
            tccSym_PATT_PGV[output].setVisible(False)
            tccSym_PATT_PGV[output].addKey("Low", "0", "Low")
            tccSym_PATT_PGV[output].addKey("High", "1", "High")
            tccSym_PATT_PGV[output].setOutputMode("Value")
            tccSym_PATT_PGV[output].setDisplayMode("Description")
            tccSym_PATT_PGV[output].setDependencies(tccPattgenVisible, ["TCC_"+str(output)+"PATT_PGE"])

    ############################################################################
    #### Dependency ####
    ############################################################################
    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues = vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == tccInstanceName.getValue():
            name = vectorValues[id].getAttribute("name")
            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")

    tccSym_IntLines = tccComponent.createIntegerSymbol("TCC_NUM_INT_LINES", None)
    tccSym_IntLines.setVisible(False)
    tccSym_IntLines.setDefaultValue((len(InterruptVector) - 1))

    # Interrupt Dynamic settings
    tccSym_UpdateInterruptStatus = tccComponent.createBooleanSymbol("TCC_INTERRUPT_STATUS", None)
    tccSym_UpdateInterruptStatus.setDependencies(updateTCCInterruptStatus, interruptDepList)
    tccSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    tccSym_IntEnComment = tccComponent.createCommentSymbol("TCC_INTERRUPT_ENABLE_COMMENT", None)
    tccSym_IntEnComment.setVisible(False)
    tccSym_IntEnComment.setLabel("Warning!!! " + tccInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    tccSym_IntEnComment.setDependencies(updateTCCInterruptWarningStatus, interruptDepList + InterruptVectorUpdate)

    # Clock Warning status
    tccSym_ClkEnComment = tccComponent.createCommentSymbol("TCC_CLOCK_ENABLE_COMMENT", None)
    tccSym_ClkEnComment.setLabel("Warning!!! TCC Peripheral Clock is Disabled in Clock Manager")
    tccSym_ClkEnComment.setVisible(False)
    tccSym_ClkEnComment.setDependencies(updateTCCClockWarningStatus, ["core." + tccInstanceName.getValue() + "_CLOCK_ENABLE"])
    
    tccSym_EVSYS_CONFIGURE = tccComponent.createIntegerSymbol("TCC_TIMER_EVSYS_CONFIGURE", None)
    tccSym_EVSYS_CONFIGURE.setVisible(False)
    tccSym_EVSYS_CONFIGURE.setDependencies(tccEvsys, eventDepList)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tccSym_PWMHeaderFile = tccComponent.createFileSymbol("TCC_HEADER", None)
    tccSym_PWMHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc.h.ftl")
    tccSym_PWMHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_PWMHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMHeaderFile.setType("HEADER")
    tccSym_PWMHeaderFile.setMarkup(True)

    tccSym_PWMSourceFile = tccComponent.createFileSymbol("TCC_SOURCE", None)
    tccSym_PWMSourceFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc.c.ftl")
    tccSym_PWMSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_PWMSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMSourceFile.setType("SOURCE")
    tccSym_PWMSourceFile.setMarkup(True)
    
    tccSym_PWMGlobalHeaderFile = tccComponent.createFileSymbol("TCC_GLOBAL_HEADER", None)
    tccSym_PWMGlobalHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setOutputName("plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setType("HEADER")
    tccSym_PWMGlobalHeaderFile.setMarkup(False)

    tccSym_SystemInitFile = tccComponent.createFileSymbol("TC_SYS_INT", None)
    tccSym_SystemInitFile.setType("STRING")
    tccSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tccSym_SystemInitFile.setSourcePath("../peripheral/tcc_u2213/templates/system/initialization.c.ftl")
    tccSym_SystemInitFile.setMarkup(True)

    tccSym_SystemDefFile = tccComponent.createFileSymbol("TC_SYS_DEF", None)
    tccSym_SystemDefFile.setType("STRING")
    tccSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tccSym_SystemDefFile.setSourcePath("../peripheral/tcc_u2213/templates/system/definitions.h.ftl")
    tccSym_SystemDefFile.setMarkup(True)
