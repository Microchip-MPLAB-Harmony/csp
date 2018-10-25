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
global InterruptHandler
global InterruptHandlerLock
global tccInstanceName

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

def updateTCCInterruptStatus(symbol, event):

    Database.clearSymbolValue("core", InterruptVector)
    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandlerLock)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    Database.clearSymbolValue("core", InterruptHandler)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, tccInstanceName.getValue() + "_PWMInterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, tccInstanceName.getValue() + "_Handler", 2)

def updateTCCInterruptWarringStatus(symbol, event):

    if tccSym_INTENSET_OVF.getValue() == True:
        symbol.setVisible(event["value"])

def updateTCCClockWarringStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tccDirVisible(symbol, event):
    symObj = event["symbol"]
    if (symObj.getSelectedKey() == "NPWM"):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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
        
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tccComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global tccInstanceName
    global tccSym_INTENSET_OVF

    tccInstanceName = tccComponent.createStringSymbol("TCC_INSTANCE_NAME", None)
    tccInstanceName.setVisible(False)
    tccInstanceName.setDefaultValue(tccComponent.getID().upper())
    
    #clock enable

    Database.clearSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_ENABLE")

    Database.setSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    ################################ ATDF ####################################################
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters")
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
    ###########################################################################################
    
    #prescaler configuration
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
    
    #waveform option
    tccSym_WAVE_WAVEGEN = tccComponent.createKeyValueSetSymbol("TCC_WAVE_WAVEGEN", None)
    tccSym_WAVE_WAVEGEN.setLabel("Select PWM Type")
    tccSym_WAVE_WAVEGEN.setDefaultValue(0)
    tccSym_WAVE_WAVEGEN.setOutputMode("Key")
    tccSym_WAVE_WAVEGEN.setDisplayMode("Description")
    tccSym_WAVE_WAVEGEN.addKey("NPWM", "2", "Single slope PWM")
    tccSym_WAVE_WAVEGEN.addKey("DSBOTTOM", "5", "Dual slope PWM with interrupt/event when counter = ZERO")
    tccSym_WAVE_WAVEGEN.addKey("DSBOTH", "6", "Dual slope PWM with interrupt/event when counter = ZERO or counter = TOP")
    tccSym_WAVE_WAVEGEN.addKey("DSTOP", "7", "Dual slope PWM with interrupt/event when counter = TOP")
    
    tccSym_CTRLBSET_DIR = tccComponent.createBooleanSymbol("TCC_CTRLBSET_DIR", None)
    tccSym_CTRLBSET_DIR.setLabel("PWM Direction - Count Down")
    tccSym_CTRLBSET_DIR.setDefaultValue(False)
    tccSym_CTRLBSET_DIR.setDependencies(tccDirVisible, ["TCC_WAVE_WAVEGEN"])
    
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
    tccSym_PER_PER = tccComponent.createIntegerSymbol("TCC_PER_PER", None)
    tccSym_PER_PER.setLabel("Period Value")
    tccSym_PER_PER.setDefaultValue(2400)
    tccSym_PER_PER.setMin(0)
    if (size == 16):
        tccSym_PER_PER.setMax(65535)
    else:
        tccSym_PER_PER.setMax(16777215)
        
    #Calculated frequency
    tccSym_Frequency = tccComponent.createCommentSymbol("TCC_FREQUENCY", None)
    tccSym_Frequency.setLabel("**** PWM Frequency is 10,000 Hz ****")
    #tccSym_Frequency.setDependencies(tccPWMFreqCalc, ["TCC_PER_PER", "TCC_WAVE_WAVEGEN", "TCC_CTRLA_PRESCALER"])
    
    #Period interrupt
    tccSym_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_INTENSET_OVF", None)
    tccSym_INTENSET_OVF.setLabel("Enable Period Interrupt")
    tccSym_INTENSET_OVF.setDefaultValue(False)
    
    #Period out event
    tccSym_EVCTRL_OVFEO = tccComponent.createBooleanSymbol("TCC_EVCTRL_OVFEO", None)
    tccSym_EVCTRL_OVFEO.setLabel("Enable Period Event Out")
    tccSym_EVCTRL_OVFEO.setDefaultValue(False)
    
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
        if (size == 16):
            tccSym_Channel_CC[channelID].setMax(65535)
        else:
            tccSym_Channel_CC[channelID].setMax(16777215)
        
        #output polarity
        tccSym_Channel_Polarity.append(channelID)
        tccSym_Channel_Polarity[channelID] = tccComponent.createKeyValueSetSymbol("TCC_"+str(channelID)+"_WAVE_POL", tccSym_Channel_Menu[channelID])
        tccSym_Channel_Polarity[channelID].setLabel("Output Polarity")
        tccSym_Channel_Polarity[channelID].addKey("LOW","0","Waveform starts at low level")
        tccSym_Channel_Polarity[channelID].addKey("HIGH","1","Waveform starts at high level")
        tccSym_Channel_Polarity[channelID].setOutputMode("Value")
        tccSym_Channel_Polarity[channelID].setDisplayMode("Description")
        
        if (deadTimeImplemented == 1):
            #dead time
            tccSym_Channel_WEXCTRL_DTIEN.append(channelID)
            tccSym_Channel_WEXCTRL_DTIEN[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WEXCTRL_DTIEN", tccSym_Channel_Menu[channelID])
            tccSym_Channel_WEXCTRL_DTIEN[channelID].setLabel("Enable Dead Time")
            tccSym_Channel_WEXCTRL_DTIEN[channelID].setDefaultValue(True)
        
        if (swapImplemented == 1):
            #swap dead time outputs
            tccSym_Channel_WAVE_SWAP.append(channelID)
            tccSym_Channel_WAVE_SWAP[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_WAVE_SWAP", tccSym_Channel_Menu[channelID])
            tccSym_Channel_WAVE_SWAP[channelID].setLabel("Swap Outputs")
            tccSym_Channel_WAVE_SWAP[channelID].setDefaultValue(False)
        
        #compare match event out
        tccSym_Channel_EVCTRL_MCEO.append(channelID)
        tccSym_Channel_EVCTRL_MCEO[channelID] = tccComponent.createBooleanSymbol("TCC_"+str(channelID)+"_EVCTRL_MCEO", tccSym_Channel_Menu[channelID])
        tccSym_Channel_EVCTRL_MCEO[channelID].setLabel("Enable Compare Match Output Event")
        tccSym_Channel_EVCTRL_MCEO[channelID].setDefaultValue(False)

    #dead time menu
    tccSym_DeadTime_Menu = tccComponent.createMenuSymbol("TCC_DEAD_TIME_MENU", None)
    tccSym_DeadTime_Menu.setLabel("Dead Time")
    if (deadTimeImplemented == 1):
        tccSym_DeadTime_Menu.setVisible(True)
    else:
        tccSym_DeadTime_Menu.setVisible(False)
    tccSym_DeadTime_Menu.setDependencies(tccDeadTimeVisible, ["TCC_0_WEXCTRL_DTIEN","TCC_1_WEXCTRL_DTIEN", "TCC_2_WEXCTRL_DTIEN", "TCC_3_WEXCTRL_DTIEN"])
    
    #Low dead time
    tccSym_WEXCTRL_DTLS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTLS", tccSym_DeadTime_Menu)
    tccSym_WEXCTRL_DTLS.setLabel("Dead Time for Low Side Output")
    tccSym_WEXCTRL_DTLS.setDefaultValue(64)
    tccSym_WEXCTRL_DTLS.setMin(0)
    tccSym_WEXCTRL_DTLS.setMax(255)
    
    #High dead time
    tccSym_WEXCTRL_DTHS = tccComponent.createIntegerSymbol("TCC_WEXCTRL_DTHS", tccSym_DeadTime_Menu)
    tccSym_WEXCTRL_DTHS.setLabel("Dead Time for High Side Output")
    tccSym_WEXCTRL_DTHS.setDefaultValue(64)
    tccSym_WEXCTRL_DTHS.setMin(0)
    tccSym_WEXCTRL_DTHS.setMax(255)
    
    #Fault menu
    tccSym_Fault_Menu = tccComponent.createMenuSymbol("TCC_FAULT_MENU", None)
    tccSym_Fault_Menu.setLabel("Fault Configurations")
    
    #fault source
    fault_source = ["Disabled", "Event 0", "Event 1"]
    tccSym_EVCTRL_EVACT = tccComponent.createComboSymbol("TCC_EVCTRL_EVACT", tccSym_Fault_Menu, fault_source)
    tccSym_EVCTRL_EVACT.setLabel("Select Fault Source")
    
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

    InterruptVector = tccInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = tccInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = tccInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = tccInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    tccSym_UpdateInterruptStatus = tccComponent.createBooleanSymbol("TCC_INTERRUPT_STATUS", None)
    tccSym_UpdateInterruptStatus.setDependencies(updateTCCInterruptStatus, ["TCC_INTENSET_OVF"])
    tccSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    tccSym_IntEnComment = tccComponent.createCommentSymbol("TCC_INTERRUPT_ENABLE_COMMENT", None)
    tccSym_IntEnComment.setVisible(False)
    tccSym_IntEnComment.setLabel("Warning!!! " + tccInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    tccSym_IntEnComment.setDependencies(updateTCCInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    tccSym_ClkEnComment = tccComponent.createCommentSymbol("TCC_CLOCK_ENABLE_COMMENT", None)
    tccSym_ClkEnComment.setLabel("Warning!!! TCC Peripheral Clock is Disabled in Clock Manager")
    tccSym_ClkEnComment.setVisible(False)
    tccSym_ClkEnComment.setDependencies(updateTCCClockWarringStatus, ["core." + tccInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tccModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]")
    tccModuleID = tccModuleNode.getAttribute("id")

    tccSym_PWMHeaderFile = tccComponent.createFileSymbol("TCC_HEADER", None)
    tccSym_PWMHeaderFile.setSourcePath("../peripheral/tcc_" + tccModuleID + "/templates/plib_tcc.h.ftl")
    tccSym_PWMHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_PWMHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMHeaderFile.setType("HEADER")
    tccSym_PWMHeaderFile.setMarkup(True)

    tccSym_PWMSourceFile = tccComponent.createFileSymbol("TCC_SOURCE", None)
    tccSym_PWMSourceFile.setSourcePath("../peripheral/tcc_" + tccModuleID + "/templates/plib_tcc.c.ftl")
    tccSym_PWMSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_PWMSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMSourceFile.setType("SOURCE")
    tccSym_PWMSourceFile.setMarkup(True)
    
    tccSym_PWMGlobalHeaderFile = tccComponent.createFileSymbol("TCC_GLOBAL_HEADER", None)
    tccSym_PWMGlobalHeaderFile.setSourcePath("../peripheral/tcc_"+str(tccModuleID)+"/templates/plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setOutputName("plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setType("HEADER")
    tccSym_PWMGlobalHeaderFile.setMarkup(False)

    tccSym_SystemInitFile = tccComponent.createFileSymbol("TC_SYS_INT", None)
    tccSym_SystemInitFile.setType("STRING")
    tccSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tccSym_SystemInitFile.setSourcePath("../peripheral/tcc_" + tccModuleID + "/templates/system/initialization.c.ftl")
    tccSym_SystemInitFile.setMarkup(True)

    tccSym_SystemDefFile = tccComponent.createFileSymbol("TC_SYS_DEF", None)
    tccSym_SystemDefFile.setType("STRING")
    tccSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tccSym_SystemDefFile.setSourcePath("../peripheral/tcc_" + tccModuleID + "/templates/system/definitions.h.ftl")
    tccSym_SystemDefFile.setMarkup(True)
