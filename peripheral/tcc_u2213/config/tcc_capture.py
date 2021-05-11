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

global tccSym_Capture_Channel
tccSym_Capture_Channel = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateCaptureMenuVisibleProperty(symbol, event):
    if event["value"] == "Capture":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTCCCaptureInterruptValue(symbol, event):
    component = symbol.getComponent()
    interrupt = False
    for intr in range (0, len(compareInterruptDep)-1):
        if(component.getSymbolValue(captureInterruptDep[intr]) == True):
            interrupt = True
    symbol.setValue(interrupt)

def tccCaptureEvsys(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "TCC_OPERATION_MODE"):
        if (event["value"] == "Capture"):
            Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_OVF_ACTIVE", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_0_READY", False, 2)
            Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)
            for channelID in range(0, int(numOfChannels)):
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", False, 2)
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", False, 2)
                if component.getSymbolValue("TCC_CAPTURE_EVCTRL_MCEO" + str(channelID)) == True:
                    Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", True, 2)
                if component.getSymbolValue("TCC_CAPTURE_CTRLA_CAPTEN"+str(channelID)) == True:
                    Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", True, 2)                    

            if component.getSymbolValue("TCC_CAPTURE_EVCTRL_EVACT1") != 0: # 0 stands for Event OFF
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2)
    else:
        if(event["id"] == "TCC_CAPTURE_EVCTRL_EVACT1"):
            if(event["value"] == 0): # 0 stands for Event OFF
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", False, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_EV_1_READY", True, 2) 
        for channelID in range(0, int(numOfChannels)):
            if component.getSymbolValue("TCC_CAPTURE_EVCTRL_MCEO" + str(channelID)) == True:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", True, 2)           
            else:
                Database.setSymbolValue("evsys", "GENERATOR_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_ACTIVE", False, 2)
            if component.getSymbolValue("TCC_CAPTURE_CTRLA_CAPTEN"+str(channelID)) == True:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", True, 2)
            else:
                Database.setSymbolValue("evsys", "USER_"+tccInstanceName.getValue()+"_MC_"+str(channelID)+"_READY", False, 2)

def tccCaptureIpEventVisible(symbol, event):
    symbol.setVisible(event["value"])

def tccCaptureMCEIComment(symbol, event):
    channelID = int(symbol.getID()[-1:])
    if channelID == 0 or channelID == 1:
        symbol.setVisible(not event["value"])

###################################################################################################
######################################## Capture Mode #############################################
###################################################################################################
global captureEvsysDep
captureEvsysDep = []
captureEvsysDep.append("TCC_OPERATION_MODE")

global captureInterruptDep
captureInterruptDep = []

#capture menu
tccSym_CaptureMenu = tccComponent.createMenuSymbol("TCC_CAPTURE_MENU", tccSym_OperationMode)
tccSym_CaptureMenu.setLabel("Capture")
tccSym_CaptureMenu.setVisible(False)
tccSym_CaptureMenu.setDependencies(updateCaptureMenuVisibleProperty, ["TCC_OPERATION_MODE"])

tccSym_CaptureNumChannels = tccComponent.createIntegerSymbol("TCC_CAPTURE_NUM_CHANNELS", tccSym_OperationMode)
tccSym_CaptureNumChannels.setLabel("Number of capture channels")
tccSym_CaptureNumChannels.setVisible(False)
tccSym_CaptureNumChannels.setDefaultValue(int(numOfChannels))



tccSym_Capture_EVCTRL_EVACT1 = tccComponent.createKeyValueSetSymbol("TCC_CAPTURE_EVCTRL_EVACT1", tccSym_CaptureMenu)
tccSym_Capture_EVCTRL_EVACT1.setLabel("Select Input Event 1 Action")
tccSym_Capture_EVCTRL_EVACT1.addKey("OFF", "0", "Disabled")
if ATDF.getNode('/avr-tools-device-file/modules/module@[name="TCC"]/value-group@[name="EVCTRL__EVACT1"]/value@[name="PPW"]') is not None:
    tccSym_Capture_EVCTRL_EVACT1.addKey("PPW", "5", "Period captured into CC0 Pulse Width on CC1")
tccSym_Capture_EVCTRL_EVACT1.addKey("PWP", "6", "Period captured into CC1 Pulse Width on CC0")
tccSym_Capture_EVCTRL_EVACT1.setDisplayMode("Description")
tccSym_Capture_EVCTRL_EVACT1.setOutputMode("Key")
captureEvsysDep.append("TCC_CAPTURE_EVCTRL_EVACT1")

tccSym_Capture_EVCTRL_TCINV1 = tccComponent.createBooleanSymbol("TCC_CAPTURE_EVCTRL_TCINV1", tccSym_Capture_EVCTRL_EVACT1)
tccSym_Capture_EVCTRL_TCINV1.setLabel("Invert Input Event 1")
tccSym_Capture_EVCTRL_TCINV1.setVisible(False)
tccSym_Capture_EVCTRL_TCINV1.setDependencies(tccCaptureIpEventVisible, ["TCC_CAPTURE_EVCTRL_EVACT1"])

tccSym_Capture_Event_Comment = tccComponent.createCommentSymbol("TCC_CAPTURE_EVENT_COMMENT", tccSym_Capture_EVCTRL_EVACT1)
tccSym_Capture_Event_Comment.setLabel("** Enable capture channel 0 and 1 to capture Period and Pulse Width **")
tccSym_Capture_Event_Comment.setVisible(False)
tccSym_Capture_Event_Comment.setDependencies(tccCaptureIpEventVisible, ["TCC_CAPTURE_EVCTRL_EVACT1"])

for channelID in range (0, int(numOfChannels)):

    #capture channel 0
    tccSym_Capture_Channel.append(channelID)
    tccSym_Capture_Channel[channelID] = tccComponent.createBooleanSymbol("TCC_CAPTURE_CTRLA_CAPTEN"+str(channelID), tccSym_CaptureMenu)
    tccSym_Capture_Channel[channelID].setLabel("Enable Capture Channel "+str(channelID))
    captureEvsysDep.append("TCC_CAPTURE_CTRLA_CAPTEN"+str(channelID))

    tccSym_Capture_Interrupt = tccComponent.createBooleanSymbol("TCC_CAPTURE_INTENSET_MC"+str(channelID), tccSym_Capture_Channel[channelID])
    tccSym_Capture_Interrupt.setLabel("Enable Capture Interrupt")
    captureInterruptDep.append("TCC_CAPTURE_INTENSET_MC"+str(channelID))
    interruptDepList.append("TCC_CAPTURE_INTENSET_MC"+str(channelID))

    tccSym_Capture_Event_Out = tccComponent.createBooleanSymbol("TCC_CAPTURE_EVCTRL_MCEO"+str(channelID), tccSym_Capture_Channel[channelID])
    tccSym_Capture_Event_Out.setLabel("Enable Capture Event OUT")
    captureEvsysDep.append("TCC_CAPTURE_EVCTRL_MCEO"+str(channelID))

    tccSym_Capture_Comment = tccComponent.createCommentSymbol("TCC_CAPTURE_COMMENT_EVCTRL_MCEI"+str(channelID), tccSym_Capture_Channel[channelID])
    tccSym_Capture_Comment.setLabel("** Connect waveform signal to Input Capture Event MC_" + str(channelID))
    tccSym_Capture_Comment.setDependencies(tccCaptureMCEIComment, ["TCC_CAPTURE_EVCTRL_EVACT1"])


#capture error interrupt
tccSym_Capture_INTENSET_ERR = tccComponent.createBooleanSymbol("TCC_CAPTURE_ERR_INTERRUPT_MODE", tccSym_CaptureMenu)
tccSym_Capture_INTENSET_ERR.setLabel("Enable Capture Error Interrupt")
captureInterruptDep.append("TCC_CAPTURE_ERR_INTERRUPT_MODE")
interruptDepList.append("TCC_CAPTURE_ERR_INTERRUPT_MODE")

#capture overflow interrupt
tccSym_Capture_INTENSET_OVF = tccComponent.createBooleanSymbol("TCC_CAPTURE_OVF_INTERRUPT_MODE", tccSym_CaptureMenu)
tccSym_Capture_INTENSET_OVF.setLabel("Enable Capture Overflow Interrupt")
captureInterruptDep.append("TCC_CAPTURE_OVF_INTERRUPT_MODE")
interruptDepList.append("TCC_CAPTURE_OVF_INTERRUPT_MODE")

#capture interrupt
captureInterruptDep.append("TCC_OPERATION_MODE")
global tccSym_Capture_InterruptMode
tccSym_Capture_InterruptMode = tccComponent.createBooleanSymbol("TCC_CAPTURE_INTERRUPT_MODE", tccSym_CaptureMenu)
tccSym_Capture_InterruptMode.setVisible(False)
tccSym_Capture_InterruptMode.setDependencies(updateTCCCaptureInterruptValue, captureInterruptDep)

tccSym_Capture_EVSYS_CONFIGURE = tccComponent.createIntegerSymbol("TCC_CAPTURE_EVSYS_CONFIGURE", tccSym_CaptureMenu)
tccSym_Capture_EVSYS_CONFIGURE.setVisible(False)
tccSym_Capture_EVSYS_CONFIGURE.setDependencies(tccCaptureEvsys, captureEvsysDep)