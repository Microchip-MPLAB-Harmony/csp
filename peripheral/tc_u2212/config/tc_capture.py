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

NUM_CAPTURE_CHANNELS = 2
global tcSym_Capture_Channel
tcSym_Capture_Channel = []
tcSym_Capture_Trigger_Source = []
tcSym_Capture_Trigger_Edge = []
tcSym_Capture_Trigger_Action = []
tcSym_Capture_INTENSET_MC = []
tcSym_Capture_EVCTRL_MCEO = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateCaptureMenuVisibleProperty(symbol, event):
    if event["value"] == "Capture":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tcChannelVisible(symbol, event):
    id = (symbol.getID()[-1:])
    channelID = int(id)

    if tcSym_Capture_Channel[channelID].getValue() == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTCCaptureInterruptValue(symbol, event):

    errInt = Database.getSymbolValue(tcInstanceName.getValue().lower(), "TC_CAPTURE_ERR_INTERRUPT_MODE")
    ovfInt = Database.getSymbolValue(tcInstanceName.getValue().lower(), "TC_CAPTURE_OVF_INTERRUPT_MODE")
    mc0Int = Database.getSymbolValue(tcInstanceName.getValue().lower(), "TC_CAPTURE_INTSET_MC0")
    mc1Int = Database.getSymbolValue(tcInstanceName.getValue().lower(), "TC_CAPTURE_INTSET_MC1")

    symbol.clearValue()
    if errInt or ovfInt or mc0Int or mc1Int:
        symbol.setValue(True, 2)
    else:
        symbol.setValue(False, 2)

def tcCaptureEvsys(symbol, event):
    if(event["id"] == "TC_CAPTURE_EVCTRL_MCEO0"):
        Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_0_ACTIVE", event["value"], 2)
    if(event["id"] == "TC_CAPTURE_EVCTRL_MCEO1"):
        Database.setSymbolValue("evsys", "GENERATOR_"+tcInstanceName.getValue()+"_MC_1_ACTIVE", event["value"], 2)

###################################################################################################
######################################## Capture Mode #############################################
###################################################################################################

#capture menu
tcSym_CaptureMenu = tcComponent.createMenuSymbol("TC_CAPTURE_MENU", tcSym_OperationMode)
tcSym_CaptureMenu.setLabel("Capture")
tcSym_CaptureMenu.setVisible(False)
tcSym_CaptureMenu.setDependencies(updateCaptureMenuVisibleProperty, ["TC_OPERATION_MODE"])

tcSym_CaptureNumChannels = tcComponent.createIntegerSymbol("TC_NUM_CHANNELS", tcSym_OperationMode)
tcSym_CaptureNumChannels.setLabel("Number of capture channels")
tcSym_CaptureNumChannels.setVisible(False)
tcSym_CaptureNumChannels.setDefaultValue(int(NUM_CAPTURE_CHANNELS))

#Enable input event
Database.setSymbolValue("evsys", "USER_"+tcInstanceName.getValue()+"_EVU_READY", True, 2)

for channelID in range (0, NUM_CAPTURE_CHANNELS):
    #capture channel 0
    tcSym_Capture_Channel.append(channelID)
    tcSym_Capture_Channel[channelID] = tcComponent.createBooleanSymbol("TC_CAPTURE_CTRLC_CPTEN"+str(channelID), tcSym_CaptureMenu)
    tcSym_Capture_Channel[channelID].setLabel("Enable Capture Channel "+str(channelID))
    tcSym_Capture_Channel[channelID].setDefaultValue(True)
    if (channelID == 1):
        tcSym_Capture_Channel[channelID].setReadOnly(True)

    #capture channel trigger source
    if (channelID == 0):
        tcSym_Capture_Trigger_Source.append(channelID)
        tcSym_Capture_Trigger_Source[channelID] = tcComponent.createKeyValueSetSymbol("TC_CAPTURE_CTRLA_COPEN"+str(channelID), tcSym_Capture_Channel[channelID])
        tcSym_Capture_Trigger_Source[channelID].setLabel("Capture Trigger Source")
        tcSym_Capture_Trigger_Source[channelID].setReadOnly(True)
        tcSym_Capture_Trigger_Source[channelID].addKey("EVENT", "0", "Input Event")
        tcSym_Capture_Trigger_Source[channelID].setDefaultValue(0)
        tcSym_Capture_Trigger_Source[channelID].setOutputMode("Value")
        tcSym_Capture_Trigger_Source[channelID].setDisplayMode("Description")
        tcSym_Capture_Trigger_Source[channelID].setDependencies(tcChannelVisible, ["TC_CAPTURE_CTRLA_CPTEN"+str(channelID)])

        #capture trigger edge
        tcSym_Capture_Trigger_Edge.append(channelID)
        tcSym_Capture_Trigger_Edge[channelID] = tcComponent.createKeyValueSetSymbol("TC_CAPTURE_TRIGGER_EDGE"+str(channelID), tcSym_Capture_Channel[channelID])
        tcSym_Capture_Trigger_Edge[channelID].setLabel("Capture Trigger Edge")
        tcSym_Capture_Trigger_Edge[channelID].addKey("RISE_EDGE", "0", "Rising Edge")
        tcSym_Capture_Trigger_Edge[channelID].addKey("FALL_EDGE", "1", "Falling Edge")
        tcSym_Capture_Trigger_Edge[channelID].setDefaultValue(0)
        tcSym_Capture_Trigger_Edge[channelID].setOutputMode("Value")
        tcSym_Capture_Trigger_Edge[channelID].setDisplayMode("Description")
        tcSym_Capture_Trigger_Edge[channelID].setDependencies(tcChannelVisible, ["TC_CAPTURE_CTRLA_CPTEN"+str(channelID)])

        #capture event trigger action
        tcSym_Capture_Trigger_Action.append(channelID)
        tcSym_Capture_Trigger_Action[channelID] = tcComponent.createKeyValueSetSymbol("TC_CAPTURE_TRIGGER_ACTION"+str(channelID), tcSym_Capture_Channel[channelID])
        tcSym_Capture_Trigger_Action[channelID].setLabel("Capture Trigger Action")
        tcSym_Capture_Trigger_Action[channelID].addKey("PPW", "5", "Period captured in CC0, pulse width in CC1")
        tcSym_Capture_Trigger_Action[channelID].addKey("PWP", "6", "Period captured in CC1, pulse width in CC0")
        tcSym_Capture_Trigger_Action[channelID].setDefaultValue(0)
        tcSym_Capture_Trigger_Action[channelID].setVisible(True)
        tcSym_Capture_Trigger_Action[channelID].setOutputMode("Key")
        tcSym_Capture_Trigger_Action[channelID].setDisplayMode("Description")
        tcSym_Capture_Trigger_Action[channelID].setDependencies(tcChannelVisible, ["TC_CAPTURE_CTRLA_CPTEN"+str(channelID)])

    #capture channel counter/compare interrupt
    tcSym_Capture_INTENSET_MC.append(channelID)
    tcSym_Capture_INTENSET_MC[channelID] = tcComponent.createBooleanSymbol("TC_CAPTURE_INTSET_MC"+str(channelID), tcSym_Capture_Channel[channelID])
    tcSym_Capture_INTENSET_MC[channelID].setLabel("Enable Capture " + str(channelID) + " Interrupt")
    tcSym_Capture_INTENSET_MC[channelID].setDefaultValue(False)
    tcSym_Capture_INTENSET_MC[channelID].setDependencies(tcChannelVisible, ["TC_CAPTURE_CTRLC_CPTEN"+str(channelID)])

    #capture event out
    tcSym_Capture_EVCTRL_MCEO.append(channelID)
    tcSym_Capture_EVCTRL_MCEO[channelID] = tcComponent.createBooleanSymbol("TC_CAPTURE_EVCTRL_MCEO"+str(channelID), tcSym_Capture_Channel[channelID])
    tcSym_Capture_EVCTRL_MCEO[channelID].setLabel("Enable Capture " + str(channelID) + " Event Out")
    tcSym_Capture_EVCTRL_MCEO[channelID].setDefaultValue(False)
    tcSym_Capture_EVCTRL_MCEO[channelID].setDependencies(tcChannelVisible, ["TC_CAPTURE_CTRLC_CPTEN"+str(channelID)])

#capture error interrupt
tcSym_Capture_INTENSET_ERR = tcComponent.createBooleanSymbol("TC_CAPTURE_ERR_INTERRUPT_MODE", tcSym_CaptureMenu)
tcSym_Capture_INTENSET_ERR.setLabel("Enable Capture Error Interrupt")

#capture overflow interrupt
tcSym_Capture_INTENSET_OVF = tcComponent.createBooleanSymbol("TC_CAPTURE_OVF_INTERRUPT_MODE", tcSym_CaptureMenu)
tcSym_Capture_INTENSET_OVF.setLabel("Enable Capture Overflow Interrupt")

#capture interrupt
global tcSym_Capture_InterruptMode
tcSym_Capture_InterruptMode = tcComponent.createBooleanSymbol("TC_CAPTURE_INTERRUPT", tcSym_CaptureMenu)
tcSym_Capture_InterruptMode.setVisible(False)
tcSym_Capture_InterruptMode.setDependencies(updateTCCaptureInterruptValue, ["TC_CAPTURE_ERR_INTERRUPT_MODE", "TC_CAPTURE_OVF_INTERRUPT_MODE", "TC_CAPTURE_INTSET_MC0", "TC_CAPTURE_INTSET_MC1"])

tcSym_Capture_EVSYS_CONFIGURE = tcComponent.createIntegerSymbol("TC_CAPTURE_EVSYS_CONFIGURE", tcSym_CaptureMenu)
tcSym_Capture_EVSYS_CONFIGURE.setVisible(False)
tcSym_Capture_EVSYS_CONFIGURE.setDependencies(tcCaptureEvsys, ["TC_CAPTURE_EVCTRL_MCEO0", "TC_CAPTURE_EVCTRL_MCEO1"])