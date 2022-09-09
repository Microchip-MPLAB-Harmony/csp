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
import math

global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock = []
global InterruptVectorUpdate
global pdecInstanceName
global interruptDepList
interruptDepList = []
global eventDepList     #List to calculate EVCTRL value for QDEC mode
eventDepList = []
global eventHallDepList  #List to calculate EVCTRL value for HALL mode
eventHallDepList = []
global eventCounterDepList  #List to calculate EVCTRL value for COUNTER mode
eventCounterDepList = []
global eventConfigureList  #List to update EVSYS PLIB symbols
eventConfigureList = []
interrupt_val = 0x0
evsys_val = 0x0
pin_val = 0x7
pin_inv_val = 0x00

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()

    component.getSymbolByID("PDEC_QDEC_HEADER").setEnabled(False)
    component.getSymbolByID("PDEC_QDEC_SOURCE").setEnabled(False)
    component.getSymbolByID("PDEC_HALL_HEADER").setEnabled(False)
    component.getSymbolByID("PDEC_HALL_SOURCE").setEnabled(False)
    component.getSymbolByID("PDEC_COUNTER_HEADER").setEnabled(False)
    component.getSymbolByID("PDEC_COUNTER_SOURCE").setEnabled(False)
    if component.getSymbolValue("PDEC_CTRLA_MODE") == 0:
        component.getSymbolByID("PDEC_QDEC_HEADER").setEnabled(True)
        component.getSymbolByID("PDEC_QDEC_SOURCE").setEnabled(True)
    elif component.getSymbolValue("PDEC_CTRLA_MODE") == 1:
        component.getSymbolByID("PDEC_HALL_HEADER").setEnabled(True)
        component.getSymbolByID("PDEC_HALL_SOURCE").setEnabled(True)
    elif component.getSymbolValue("PDEC_CTRLA_MODE") == 2:
        component.getSymbolByID("PDEC_COUNTER_HEADER").setEnabled(True)
        component.getSymbolByID("PDEC_COUNTER_SOURCE").setEnabled(True)

def pdecResolutionCalc(symbol, event):
    clock_freq = Database.getSymbolValue("core", pdecInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    prescaler = int(pdecSym_PRESC_PRESC.getSelectedKey()[3:])
    resolution = (prescaler * 1000000000.0) / clock_freq
    symbol.setLabel("****PDEC Counter resolution is " + str(resolution) + " nS****")

def pdecFreqCalc(symbol, event):
    symbol.setValue(Database.getSymbolValue("core", pdecInstanceName.getValue()+"_CLOCK_FREQUENCY") / int(pdecSym_PRESC_PRESC.getSelectedKey()[3:]), 2)

def pdecRevolutionCalc(symbol, event):
    symbol.setValue(16 - event["value"], 2)

def pdecMaskCalculate(symbol, event):
    symbol.setValue(pow(2, event["value"]) - 1)

def pdecRevMaskCalculate(symbol, event):
    symbol.setValue(pow(2, 16) - pow(2, event["value"]))

def pdecOptionVisible(symbol, event):
    if(event["id"] == "PDEC_CTRLA_ANGULAR"):
        symbol.setMax(pow(2, event["value"]) - 1)
    if (event["id"] == "PDEC_CTRLA_REVOLUTION"):
        symbol.setMax(pow(2, event["value"]) - 1)
    else:
        symbol.setVisible(event["value"])

def pdecMAXCMPVisible(symbol, event):
    if (event["value"] == 4): #AUTOC mode
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pdecPhaseA(symbol, event):
    if(event["value"] == 2 or event["value"] == 3):
        symbol.setLabel("Select Quadrature Count")
    else:
        symbol.setLabel("Select Quadrature Phase A")

def pdecPhaseB(symbol, event):
    if(event["value"] == 2 or event["value"] == 3):
        symbol.setLabel("Select Quadrature Index")
    else:
        symbol.setLabel("Select Quadrature Phase B")

def pdecIndex(symbol, event):
    if(event["value"] == 2 or event["value"] == 3):
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def updatePDECInterruptStatus(symbol, event):
    component = symbol.getComponent()
    if (event["id"] == "PDEC_INTENSET_OVF") or (event["id"] == "PDEC_INTENSET_VLC") or (event["id"] == "PDEC_INTENSET_DIR") or (component.getSymbolValue("PDEC_NUM_INT_LINES") == 0):
        if (component.getSymbolValue("PDEC_INTENSET_OVF") or component.getSymbolValue("PDEC_INTENSET_VLC") or
            component.getSymbolValue("PDEC_INTENSET_DIR") or component.getSymbolValue("PDEC_INTENSET_MC_0") or component.getSymbolValue("PDEC_INTENSET_MC_1")):
            Database.setSymbolValue("core", InterruptVector[0], True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], True, 2)
            Database.setSymbolValue("core", InterruptHandler[0], pdecInstanceName.getValue() + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptVector[0], False, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], False, 2)
            Database.setSymbolValue("core", InterruptHandler[0], pdecInstanceName.getValue() + "_Handler", 2)
    else:
        mcInstance = int(event["id"].split("_")[-1])
        Database.setSymbolValue("core", InterruptVector[mcInstance+1], event["value"], 2)
        Database.setSymbolValue("core", InterruptHandlerLock[mcInstance+1], event["value"], 2)
        if event["value"] == True:
            Database.setSymbolValue("core", InterruptHandler[mcInstance+1], InterruptHandler[mcInstance+1].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", InterruptHandler[mcInstance+1], InterruptHandler[mcInstance+1].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)

def updatePDECInterruptWarningStatus(symbol, event):
    global InterruptVectorUpdate
    component = symbol.getComponent()
    if (component.getSymbolValue("PDEC_INTENSET_OVF") or component.getSymbolValue("PDEC_INTENSET_VLC") or
        component.getSymbolValue("PDEC_INTENSET_DIR")):
        if (Database.getSymbolValue("core", InterruptVectorUpdate[0].split(".")[-1]) == True):
            symbol.setVisible(True)
    elif (component.getSymbolValue("PDEC_INTENSET_MC_0") == True and
        Database.getSymbolValue("core", InterruptVectorUpdate[1].split(".")[-1]) == True):
        symbol.setVisible(True)
    elif (component.getSymbolValue("PDEC_INTENSET_MC_1") == True and
        Database.getSymbolValue("core", InterruptVectorUpdate[2].split(".")[-1]) == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updatePDECClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pdecEVSYSConfigure(symbol, event):
    component = symbol.getComponent()
    if ("EVCTRL" in event["id"]):
        Database.setSymbolValue("evsys",
            "GENERATOR_"+ str(pdecInstanceName.getValue())+ event["id"].replace("PDEC_EVCTRL","") + "_ACTIVE", event["value"], 2)
    else:
        if (event["id"] == "PDEC_CTRLA_MODE"):
            Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_0_READY", False, 2)
            Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_1_READY", False, 2)
            Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_2_READY", False, 2)
        if pdecSym_OperationMode.getValue() == 0:
            pdecQDECEVSYS(component, event)
        elif pdecSym_OperationMode.getValue() == 1:
            pdecHallEVSYS(component, event)
        else:
            pdecCounterEVSYS(component, event)

def pdecQDECEVSYS(component, event):
    if (component.getSymbolValue("PDEC_PHASE_A") == "Input Event" or component.getSymbolValue("PDEC_PHASE_A") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_0_READY", True, 2)
    if(component.getSymbolValue("PDEC_PHASE_B") == "Input Event" or component.getSymbolValue("PDEC_PHASE_B") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_1_READY", True, 2)
    if(component.getSymbolValue("PDEC_INDEX") == "Input Event" or component.getSymbolValue("PDEC_INDEX") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_2_READY", True, 2)

def pdecHallEVSYS(component, event):
    if (component.getSymbolValue("PDEC_HALL_A") == "Input Event" or component.getSymbolValue("PDEC_PHASE_A") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_0_READY", True, 2)
    if(component.getSymbolValue("PDEC_HALL_B") == "Input Event" or component.getSymbolValue("PDEC_PHASE_B") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_1_READY", True, 2)
    if(component.getSymbolValue("PDEC_HALL_C") == "Input Event" or component.getSymbolValue("PDEC_PHASE_C") == "Inverted Input Event"):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_2_READY", True, 2)

def pdecCounterEVSYS(component, event):
    if (component.getSymbolValue("PDEC_COUNTER_EVEI0") == True or component.getSymbolValue("PDEC_COUNTER_EVINV0") == True):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_0_READY", True, 2)
    if (component.getSymbolValue("PDEC_COUNTER_EVEI1") == True or component.getSymbolValue("PDEC_COUNTER_EVINV1") == True):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_1_READY", True, 2)
    if (component.getSymbolValue("PDEC_COUNTER_EVEI2") == True or component.getSymbolValue("PDEC_COUNTER_EVINV2") == True):
        Database.setSymbolValue("evsys", "USER_"+ str(pdecInstanceName.getValue())+"_EVU_2_READY", True, 2)

#INTENSET register value
def pdecINTENSET(symbol, event):
    global interrupt_val
    global interruptDepList
    component = symbol.getComponent()
    for i in range(0, len(interruptDepList)):
        if (component.getSymbolValue(interruptDepList[i]) == True):
            interrupt_val = interrupt_val | (1 << i)
    symbol.setValue(interrupt_val, 2)

#EVCTRL register value for QDEC mode
def pdecEVCTRL(symbol, event):
    global evsys_val
    global eventDepList
    component = symbol.getComponent()
    # for event users
    for i in range(0, 3):
        if (component.getSymbolValue(eventDepList[i]) == "Input Event"):
            evsys_val = evsys_val | (1 << (i + 5))
        elif (component.getSymbolValue(eventDepList[i]) == "Inverted Input Event"):
            evsys_val = evsys_val | (1 << (i + 5))
            evsys_val = evsys_val | (1 << (i + 2))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 5)))
            evsys_val = evsys_val & (~ (1 << (i + 2)))
    #for event generators
    for i in range(3, len(eventDepList)):
        if (component.getSymbolValue(eventDepList[i]) == True):
            evsys_val = evsys_val | (1 << (i + 5))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 5)))
    symbol.setValue(evsys_val, 2)

#EVCTRL register value for Hall mode
def pdecHallEVCTRL(symbol, event):
    global evsys_val
    global eventHallDepList
    component = symbol.getComponent()
    # for event users
    for i in range(0, 3):
        if (component.getSymbolValue(eventHallDepList[i]) == "Input Event"):
            evsys_val = evsys_val | (1 << (i + 5))
        elif (component.getSymbolValue(eventHallDepList[i]) == "Inverted Input Event"):
            evsys_val = evsys_val | (1 << (i + 5))
            evsys_val = evsys_val | (1 << (i + 2))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 5)))
            evsys_val = evsys_val & (~ (1 << (i + 2)))
    #for event generators
    for i in range(3, len(eventHallDepList)):
        if (component.getSymbolValue(eventHallDepList[i]) == True):
            evsys_val = evsys_val | (1 << (i + 5))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 5)))
    symbol.setValue(evsys_val, 2)

#EVCTRL register value for Counter mode
def pdecCounterEVCTRL(symbol, event):
    global evsys_val
    global eventCounterDepList
    component = symbol.getComponent()
    # for event users
    for i in range(0, 3):
        if (component.getSymbolValue(eventCounterDepList[i]) == True):
            evsys_val = evsys_val | (1 << (i + 5))
            if (component.getSymbolValue(eventCounterDepList[i+3]) == True):
                evsys_val = evsys_val | (1 << (i + 2))
            else:
                evsys_val = evsys_val & (~ (1 << (i + 2)))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 5)))
            evsys_val = evsys_val & (~ (1 << (i + 2)))
    #for event generators
    for i in range(6, len(eventCounterDepList)):
        if (component.getSymbolValue(eventCounterDepList[i]) == True):
            evsys_val = evsys_val | (1 << (i + 2))
        else:
            evsys_val = evsys_val & (~ (1 << (i + 2)))
    symbol.setValue(evsys_val, 2)

def pdecPIN(symbol, event):
    global eventDepList
    global pin_val
    component = symbol.getComponent()
    # for io pins
    for i in range(0, 3):
        if (component.getSymbolValue(eventDepList[i]) == "IO Pin"):
            pin_val = pin_val | (1 << (i ))
        else:
            pin_val = pin_val & (~ (1 << (i )))
    symbol.setValue(pin_val, 2)

def pdecPININV(symbol, event):
    global eventDepList
    global pin_inv_val
    component = symbol.getComponent()
    # for io pins
    for i in range(0, 3):
        if (component.getSymbolValue(eventDepList[i]) == "Inverted IO Pin"):
            pin_inv_val = pin_inv_val | (1 << (i ))
        else:
            pin_inv_val = pin_inv_val & (~ (1 << (i)))
    symbol.setValue(pin_inv_val, 2)

def pdecHallPIN(symbol, event):
    global eventHallDepList
    global pin_val
    component = symbol.getComponent()
    # for io pins
    for i in range(0, 3):
        if (component.getSymbolValue(eventHallDepList[i]) == "IO Pin"):
            pin_val = pin_val | (1 << (i ))
        else:
            pin_val = pin_val & (~ (1 << (i )))
    symbol.setValue(pin_val, 2)

def pdecHallPININV(symbol, event):
    global eventHallDepList
    global pin_inv_val
    component = symbol.getComponent()
    # for io pins
    for i in range(0, 3):
        if (component.getSymbolValue(eventHallDepList[i]) == "Inverted IO Pin"):
            pin_inv_val = pin_inv_val | (1 << (i ))
        else:
            pin_inv_val = pin_inv_val & (~ (1 << (i)))
    symbol.setValue(pin_inv_val, 2)

def pdecModeVisible(symbol, event):
    mode = event["value"]
    pdecSym_QDEC_MENU.setVisible(False)
    pdecSym_HALL_MENU.setVisible(False)
    pdecSym_COUNTER_MENU.setVisible(False)
    if (mode == 0):
        pdecSym_QDEC_MENU.setVisible(True)
    elif (mode == 1):
        pdecSym_HALL_MENU.setVisible(True)
    else:
        pdecSym_COUNTER_MENU.setVisible(True)

def pdecInputEventsVisible(symbol, event):
    if (event["value"] == 2):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def pdecCounterLabelChange(symbol, event):
    if event["value"] == False:
        symbol.setLabel(" Period Value")
    else:
        symbol.setLabel("Compare CC0 Value")

###################################################################################################
########################### Dependency   #################################
###################################################################################################
def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    global pdecInstanceName
    if connectID == pdecInstanceName.getValue() + "_QDEC":
        localComponent.setCapabilityEnabled(pdecInstanceName.getValue() + "_QDEC", True)
        localComponent.setCapabilityEnabled(pdecInstanceName.getValue() + "_HALL", False)


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    resetSettings()
    global pdecInstanceName
    localComponent.setCapabilityEnabled(pdecInstanceName.getValue() + "_QDEC", True)
    localComponent.setCapabilityEnabled(pdecInstanceName.getValue() + "_HALL", True)


def resetSettings():
    component = str(pdecInstanceName.getValue()).lower()
    Database.setSymbolValue(component, "PDEC_CTRLA_MODE", 0)
    Database.setSymbolValue(component, "PDEC_CTRLA_ANGULAR", 10)

def handleMessage(messageID, args):

    dict = {}
    if (messageID == "PMSM_FOC_ENCODER_CONF"):
        component = str(pdecInstanceName.getValue()).lower()

        resetSettings()

        pulses = long(args['PULSES_PER_REV'])

        Database.setSymbolValue(component, "PDEC_CTRLA_MODE", 0)
        Database.setSymbolValue(component, "PDEC_CTRLA_PEREN", False)
        Database.setSymbolValue(component, "PDEC_INDEX", "Disabled")
        Database.setSymbolValue(component, "PDEC_CTRLA_ANGULAR", 16)

    return dict

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pdecComponent):

    """ Function to instantiate pdecComponent to Active Component """

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorUpdate
    InterruptVectorUpdate = []
    global eventDepList
    global eventHallDepList
    global eventCounterDepList
    global eventConfigureList
    global interruptDepList
    global pdecInstanceName

    pdecInstanceName = pdecComponent.createStringSymbol("PDEC_INSTANCE_NAME", None)
    pdecInstanceName.setVisible(False)
    pdecInstanceName.setDefaultValue(pdecComponent.getID().upper())

    Log.writeInfoMessage("Running " + pdecInstanceName.getValue())

    #clock enable
    Database.setSymbolValue("core", pdecInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    #----------------- motor control APIs ---------------------------------
    pdecStartAPI = pdecComponent.createStringSymbol("ENCODER_START_API", None)
    pdecStartAPI.setVisible(False)
    pdecStartAPI.setValue(pdecInstanceName.getValue() + "_QDECStart")

    pdecStopAPI = pdecComponent.createStringSymbol("ENCODER_STOP_API", None)
    pdecStopAPI.setVisible(False)
    pdecStopAPI.setValue(pdecInstanceName.getValue() + "_QDECStop")

    pdecPositionGetAPI = pdecComponent.createStringSymbol("ENCODER_POS_GET_API", None)
    pdecPositionGetAPI.setVisible(False)
    pdecPositionGetAPI.setValue(pdecInstanceName.getValue() + "_QDECPositionGet")

    pdecSpeedGetAPI = pdecComponent.createStringSymbol("ENCODER_SPEED_GET_API", None)
    pdecSpeedGetAPI.setVisible(False)
    pdecSpeedGetAPI.setValue("")

    pdecPositionSetAPI = pdecComponent.createStringSymbol("ENCODER_POS_SET_API", None)
    pdecPositionSetAPI.setVisible(False)
    pdecPositionSetAPI.setValue("")

    pdecSpeedSetAPI = pdecComponent.createStringSymbol("ENCODER_SPEED_SET_API", None)
    pdecSpeedSetAPI.setVisible(False)
    pdecSpeedSetAPI.setValue("")

    #prescaler
    global pdecSym_PRESC_PRESC
    pdecSym_PRESC_PRESC = pdecComponent.createKeyValueSetSymbol("PDEC_PRESC_PRESC", None)
    pdecSym_PRESC_PRESC.setLabel("Select Prescaler")
    pdecNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PDEC\"]/value-group@[name=\"PDEC_PRESC__PRESC\"]")
    pdecValues = []
    pdecValues = pdecNode.getChildren()
    pdecPrescalerSelectionDefaultValue = 0
    for index in range(len(pdecValues)):
        pdecPrescalerSelectionKeyName = pdecValues[index].getAttribute("name")
        if pdecPrescalerSelectionKeyName == "DIV1":
            pdecPrescalerSelectionDefaultValue = index
        pdecPrescalerSelectionKeyDescription = pdecValues[index].getAttribute("caption")
        pdecPrescalerSelectionKeyValue = pdecValues[index].getAttribute("value")
        pdecSym_PRESC_PRESC.addKey(pdecPrescalerSelectionKeyName, pdecPrescalerSelectionKeyValue, pdecPrescalerSelectionKeyDescription)
    pdecSym_PRESC_PRESC.setDefaultValue(pdecPrescalerSelectionDefaultValue)
    pdecSym_PRESC_PRESC.setOutputMode("Key")
    pdecSym_PRESC_PRESC.setDisplayMode("Description")

    #clock resolution display
    pdecSym_Resolution = pdecComponent.createCommentSymbol("PDEC_Resolution", None)
    clock_freq = Database.getSymbolValue("core", pdecInstanceName.getValue()+"_CLOCK_FREQUENCY")
    if clock_freq == 0:
        clock_freq = 1
    resolution = (int(pdecSym_PRESC_PRESC.getSelectedKey()[3:]) * 1000000000.0) / clock_freq
    pdecSym_Resolution.setLabel("****PDEC Counter resolution is " + str(resolution) + " nS****")
    pdecSym_Resolution.setDependencies(pdecResolutionCalc, ["core."+pdecInstanceName.getValue()+"_CLOCK_FREQUENCY", \
        "PDEC_PRESC_PRESC"])

    #PDEC clock frequency
    pdecSym_Frequency = pdecComponent.createIntegerSymbol("PDEC_FREQUENCY", None)
    pdecSym_Frequency.setLabel("Clock Frequency")
    pdecSym_Frequency.setVisible(False)
    pdecSym_Frequency.setDefaultValue(Database.getSymbolValue("core", pdecInstanceName.getValue()+"_CLOCK_FREQUENCY"))
    pdecSym_Frequency.setDependencies(pdecFreqCalc, ["core."+pdecInstanceName.getValue()+"_CLOCK_FREQUENCY", "PDEC_PRESC_PRESC"])

    #PDEC operation mode
    global pdecSym_OperationMode
    pdecSym_OperationMode = pdecComponent.createKeyValueSetSymbol("PDEC_CTRLA_MODE", None)
    pdecSym_OperationMode.setLabel("Operating Mode")
    pdecSym_OperationMode.setReadOnly(False)
    pdecNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PDEC\"]/value-group@[name=\"PDEC_CTRLA__MODE\"]")
    pdecValues = []
    pdecValues = pdecNode.getChildren()
    for index in range(len(pdecValues)):
        pdecKeyName = pdecValues[index].getAttribute("name")
        pdecKeyValue = pdecValues[index].getAttribute("value")
        pdecSym_OperationMode.addKey(pdecKeyName, pdecKeyValue, pdecKeyName)
    pdecSym_OperationMode.setDefaultValue(0)
    pdecSym_OperationMode.setOutputMode("Key")
    pdecSym_OperationMode.setDisplayMode("Description")

    global pdecSym_QDEC_MENU
    pdecSym_QDEC_MENU = pdecComponent.createMenuSymbol("PDEC_QDEC_MENU", pdecSym_OperationMode)
    pdecSym_QDEC_MENU.setLabel("Quadrature")
    pdecSym_QDEC_MENU.setDependencies(pdecModeVisible, ["PDEC_CTRLA_MODE"])

    global pdecSym_HALL_MENU
    pdecSym_HALL_MENU = pdecComponent.createMenuSymbol("PDEC_HALL_MENU", pdecSym_OperationMode)
    pdecSym_HALL_MENU.setLabel("Hall")
    pdecSym_HALL_MENU.setVisible(False)
    pdecSym_HALL_MENU.setDependencies(pdecModeVisible, ["PDEC_CTRLA_MODE"])

    global pdecSym_COUNTER_MENU
    pdecSym_COUNTER_MENU = pdecComponent.createMenuSymbol("PDEC_COUNTER_MENU", pdecSym_OperationMode)
    pdecSym_COUNTER_MENU.setLabel("Counter")
    pdecSym_COUNTER_MENU.setVisible(False)
    pdecSym_COUNTER_MENU.setDependencies(pdecModeVisible, ["PDEC_CTRLA_MODE"])

################################## Quadrature Menu #####################################
    pdecSym_CTRLA_CONF = pdecComponent.createKeyValueSetSymbol("PDEC_CTRLA_CONF", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_CONF.setLabel("Operating Mode")
    pdecNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PDEC\"]/value-group@[name=\"PDEC_CTRLA__CONF\"]")
    pdecValues = []
    pdecValues = pdecNode.getChildren()
    for index in range(len(pdecValues)):
        pdecKeyName = pdecValues[index].getAttribute("name")
        pdecKeyValue = pdecValues[index].getAttribute("value")
        pdecSym_CTRLA_CONF.addKey(pdecKeyName, pdecKeyValue, pdecValues[index].getAttribute("caption"))
    pdecSym_CTRLA_CONF.setDefaultValue(0)
    pdecSym_CTRLA_CONF.setOutputMode("Key")
    pdecSym_CTRLA_CONF.setDisplayMode("Description")

    input_options = ["Disabled", "IO Pin", "Inverted IO Pin", "Input Event", "Inverted Input Event"]

    pdecSym_PhaseA = pdecComponent.createComboSymbol("PDEC_PHASE_A", pdecSym_QDEC_MENU, input_options)
    pdecSym_PhaseA.setLabel("Select Quadrature Phase A")
    pdecSym_PhaseA.setDefaultValue("IO Pin")
    pdecSym_PhaseA.setDependencies(pdecPhaseA, ["PDEC_CTRLA_CONF"])
    eventDepList.append("PDEC_PHASE_A")

    pdecSym_PhaseB = pdecComponent.createComboSymbol("PDEC_PHASE_B", pdecSym_QDEC_MENU, input_options)
    pdecSym_PhaseB.setLabel("Select Quadrature Phase B")
    pdecSym_PhaseB.setDefaultValue("IO Pin")
    pdecSym_PhaseB.setDependencies(pdecPhaseB, ["PDEC_CTRLA_CONF"])
    eventDepList.append("PDEC_PHASE_B")

    index_input_options = ["Disabled", "IO Pin", "Inverted IO Pin", "Input Event", "Inverted Input Event"]
    pdecSym_Index = pdecComponent.createComboSymbol("PDEC_INDEX", pdecSym_QDEC_MENU, index_input_options)
    pdecSym_Index.setLabel("Select Quadrature Index")
    pdecSym_Index.setDefaultValue("IO Pin")
    pdecSym_Index.setDependencies(pdecIndex, ["PDEC_CTRLA_CONF"])
    eventDepList.append("PDEC_INDEX")

    pdecSym_FILTER = pdecComponent.createIntegerSymbol("PDEC_FILTER", pdecSym_QDEC_MENU)
    pdecSym_FILTER.setLabel("Select Filter Value")
    pdecSym_FILTER.setDefaultValue(2)
    pdecSym_FILTER.setMin(0)
    pdecSym_FILTER.setMax(255)

    pdecSym_CTRLA_SWAP = pdecComponent.createBooleanSymbol("PDEC_CTRLA_SWAP", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_SWAP.setLabel("Swap Phase A and B")
    pdecSym_CTRLA_SWAP.setDefaultValue(False)

    pdecSym_CTRLA_ANGULAR = pdecComponent.createIntegerSymbol("PDEC_CTRLA_ANGULAR", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_ANGULAR.setLabel("Select No of Bits for Angular Position")
    pdecSym_CTRLA_ANGULAR.setDefaultValue(10)
    pdecSym_CTRLA_ANGULAR.setMin(9)
    pdecSym_CTRLA_ANGULAR.setMax(16)

    pdecSym_CTRLA_REVOLUTION = pdecComponent.createIntegerSymbol("PDEC_CTRLA_REVOLUTION", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_REVOLUTION.setLabel("No of Bits for Revolution Counter")
    pdecSym_CTRLA_REVOLUTION.setReadOnly(True)
    pdecSym_CTRLA_REVOLUTION.setDefaultValue(6)
    pdecSym_CTRLA_REVOLUTION.setDependencies(pdecRevolutionCalc, ["PDEC_CTRLA_ANGULAR"])

    pdecSym_CTRLA_ANGULAR_MASK = pdecComponent.createHexSymbol("PDEC_CTRLA_ANGULAR_MASK", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_ANGULAR_MASK.setVisible(False)
    pdecSym_CTRLA_ANGULAR_MASK.setDefaultValue(pow(2, pdecSym_CTRLA_ANGULAR.getValue()) - 1)
    pdecSym_CTRLA_ANGULAR_MASK.setDependencies(pdecMaskCalculate, ["PDEC_CTRLA_ANGULAR"])

    pdecSym_CTRLA_REVOLUTION_MASK = pdecComponent.createHexSymbol("PDEC_CTRLA_REVOLUTION_MASK", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_REVOLUTION_MASK.setVisible(False)
    pdecSym_CTRLA_REVOLUTION_MASK.setDefaultValue(pow(2, 16) - pow(2, pdecSym_CTRLA_ANGULAR.getValue()))
    pdecSym_CTRLA_REVOLUTION_MASK.setDependencies(pdecRevMaskCalculate, ["PDEC_CTRLA_ANGULAR"])

    pdecSym_CTRLA_PEREN = pdecComponent.createBooleanSymbol("PDEC_CTRLA_PEREN", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_PEREN.setLabel("Enable Period Control")
    pdecSym_CTRLA_PEREN.setDefaultValue(True)

    pdecSym_CC0_ANGULAR = pdecComponent.createIntegerSymbol("PDEC_CC0_ANGULAR", pdecSym_CTRLA_PEREN)
    pdecSym_CC0_ANGULAR.setLabel("Quadrature Pulses per Revolution")
    pdecSym_CC0_ANGULAR.setVisible(True)
    pdecSym_CC0_ANGULAR.setDefaultValue(pow(2, pdecSym_CTRLA_ANGULAR.getValue()) -1 )
    pdecSym_CC0_ANGULAR.setMin(0)
    pdecSym_CC0_ANGULAR.setMax(pow(2, pdecSym_CTRLA_ANGULAR.getValue()) - 1)
    pdecSym_CC0_ANGULAR.setDependencies(pdecOptionVisible, ["PDEC_CTRLA_PEREN", "PDEC_CTRLA_ANGULAR"])

    pdecSym_CC0_REVOLUTION = pdecComponent.createIntegerSymbol("PDEC_CC0_REVOLUTION", pdecSym_CTRLA_PEREN)
    pdecSym_CC0_REVOLUTION.setLabel("Max Number of Revolutions")
    pdecSym_CC0_REVOLUTION.setVisible(True)
    pdecSym_CC0_REVOLUTION.setDefaultValue(pow(2, pdecSym_CTRLA_REVOLUTION.getValue()) - 1)
    pdecSym_CC0_REVOLUTION.setMin(0)
    pdecSym_CC0_REVOLUTION.setMax(pow(2, pdecSym_CTRLA_REVOLUTION.getValue()) - 1)
    pdecSym_CC0_REVOLUTION.setDependencies(pdecOptionVisible, ["PDEC_CTRLA_PEREN", "PDEC_CTRLA_REVOLUTION"])

    pdecSym_COMPARE = pdecComponent.createBooleanSymbol("PDEC_COMPARE", pdecSym_QDEC_MENU)
    pdecSym_COMPARE.setLabel("Enable Compare Control")
    pdecSym_COMPARE.setDefaultValue(False)

    pdecSym_CC1_ANGULAR = pdecComponent.createIntegerSymbol("PDEC_CC1_ANGULAR", pdecSym_COMPARE)
    pdecSym_CC1_ANGULAR.setLabel("Compare Value for Quadrature Pulses")
    pdecSym_CC1_ANGULAR.setVisible(False)
    pdecSym_CC1_ANGULAR.setDefaultValue((pow(2, pdecSym_CTRLA_ANGULAR.getValue())-1)/2 )
    pdecSym_CC1_ANGULAR.setMin(0)
    pdecSym_CC1_ANGULAR.setMax(pow(2, pdecSym_CTRLA_ANGULAR.getValue()) - 1)
    pdecSym_CC1_ANGULAR.setDependencies(pdecOptionVisible, ["PDEC_COMPARE", "PDEC_CTRLA_ANGULAR"])

    pdecSym_CC1_REVOLUTION = pdecComponent.createIntegerSymbol("PDEC_CC1_REVOLUTION", pdecSym_COMPARE)
    pdecSym_CC1_REVOLUTION.setLabel("Compare Value for Revolutions")
    pdecSym_CC1_REVOLUTION.setVisible(False)
    pdecSym_CC1_REVOLUTION.setDefaultValue((pow(2, pdecSym_CTRLA_REVOLUTION.getValue()) - 1)/2)
    pdecSym_CC1_REVOLUTION.setMin(0)
    pdecSym_CC1_REVOLUTION.setMax(pow(2, pdecSym_CTRLA_REVOLUTION.getValue()) - 1)
    pdecSym_CC1_REVOLUTION.setDependencies(pdecOptionVisible, ["PDEC_COMPARE", "PDEC_CTRLA_REVOLUTION"])

    pdecSym_CTRLA_MAXCMP = pdecComponent.createIntegerSymbol("PDEC_CTRLA_MAXCMP", pdecSym_QDEC_MENU)
    pdecSym_CTRLA_MAXCMP.setLabel("Select Maximum Consecutive Missing Pulses")
    pdecSym_CTRLA_MAXCMP.setDefaultValue(4)
    pdecSym_CTRLA_MAXCMP.setVisible(False)
    pdecSym_CTRLA_MAXCMP.setDependencies(pdecMAXCMPVisible, ["PDEC_CTRLA_CONF"])

################################## Hall Menu #####################################

    hall_input_options = ["IO Pin", "Inverted IO Pin", "Input Event", "Inverted Input Event"]

    pdecSym_HallA = pdecComponent.createComboSymbol("PDEC_HALL_A", pdecSym_HALL_MENU, hall_input_options)
    pdecSym_HallA.setLabel("Select Hall A")
    pdecSym_HallA.setDefaultValue("IO Pin")
    eventHallDepList.append("PDEC_HALL_A")

    pdecSym_HallB = pdecComponent.createComboSymbol("PDEC_HALL_B", pdecSym_HALL_MENU, hall_input_options)
    pdecSym_HallB.setLabel("Select Hall B")
    pdecSym_HallB.setDefaultValue("IO Pin")
    eventHallDepList.append("PDEC_HALL_B")

    pdecSym_HallC = pdecComponent.createComboSymbol("PDEC_HALL_C", pdecSym_HALL_MENU, hall_input_options)
    pdecSym_HallC.setLabel("Select Hall C")
    pdecSym_HallC.setDefaultValue("IO Pin")
    eventHallDepList.append("PDEC_HALL_C")

    pdecSym_Hall_FILTER = pdecComponent.createIntegerSymbol("PDEC_HALL_FILTER", pdecSym_HALL_MENU)
    pdecSym_Hall_FILTER.setLabel("Select Filter Value")
    pdecSym_Hall_FILTER.setDefaultValue(5)
    pdecSym_Hall_FILTER.setMin(0)
    pdecSym_Hall_FILTER.setMax(255)

################################ Counter Menu ###########################
    pdecSym_CNTR_CTRLA_PEREN = pdecComponent.createBooleanSymbol("PDEC_CNTR_CTRLA_PEREN", pdecSym_COUNTER_MENU)
    pdecSym_CNTR_CTRLA_PEREN.setLabel("Select TOP as Period")
    pdecSym_CNTR_CTRLA_PEREN.setDefaultValue(True)

    pdecSym_CNTR_CC0 = pdecComponent.createIntegerSymbol("PDEC_CNTR_CC0", pdecSym_COUNTER_MENU)
    pdecSym_CNTR_CC0.setLabel("Compare CC0 Value")
    pdecSym_CNTR_CC0.setMin(0)
    pdecSym_CNTR_CC0.setMax(65535)
    pdecSym_CNTR_CC0.setDefaultValue(2000)
    pdecSym_CNTR_CC0.setDependencies(pdecCounterLabelChange, ["PDEC_CNTR_CTRLA_PEREN"])

    pdecSym_CNTR_CC1 = pdecComponent.createIntegerSymbol("PDEC_CNTR_CC1", pdecSym_COUNTER_MENU)
    pdecSym_CNTR_CC1.setLabel("Compare CC1 Value")
    pdecSym_CNTR_CC1.setMin(0)
    pdecSym_CNTR_CC1.setMax(65535)
    pdecSym_CNTR_CC1.setDefaultValue(2000)

##################################### Interrupts ###########################

    pdecSym_Interrupts_Menu = pdecComponent.createMenuSymbol("PDEC_INTERRUPTS", None)
    pdecSym_Interrupts_Menu.setLabel("Interrupts")

    pdecSym_INTENSET_OVF = pdecComponent.createBooleanSymbol("PDEC_INTENSET_OVF", pdecSym_Interrupts_Menu)
    pdecSym_INTENSET_OVF.setLabel("Enable Overflow Interrupt")
    interruptDepList.append("PDEC_INTENSET_OVF")

    #Added for error interrupt
    interruptDepList.append("")

    pdecSym_INTENSET_DIR = pdecComponent.createBooleanSymbol("PDEC_INTENSET_DIR", pdecSym_Interrupts_Menu)
    pdecSym_INTENSET_DIR.setLabel("Enable Direction Interrupt")
    interruptDepList.append("PDEC_INTENSET_DIR")

    pdecSym_INTENSET_VLC = pdecComponent.createBooleanSymbol("PDEC_INTENSET_VLC", pdecSym_Interrupts_Menu)
    pdecSym_INTENSET_VLC.setLabel("Enable Velocity Interrupt")
    interruptDepList.append("PDEC_INTENSET_VLC")

    pdecSym_INTENSET_MC0 = pdecComponent.createBooleanSymbol("PDEC_INTENSET_MC_0", pdecSym_Interrupts_Menu)
    pdecSym_INTENSET_MC0.setLabel("Enable Compare Match 0 Interrupt")
    interruptDepList.append("PDEC_INTENSET_MC_0")

    pdecSym_INTENSET_MC1 = pdecComponent.createBooleanSymbol("PDEC_INTENSET_MC_1", pdecSym_Interrupts_Menu)
    pdecSym_INTENSET_MC1.setLabel("Enable Compare Match 1 Interrupt")
    interruptDepList.append("PDEC_INTENSET_MC_1")

    pdecSym_INTENSET = pdecComponent.createHexSymbol("PDEC_INTENSET", None)
    pdecSym_INTENSET.setVisible(False)
    pdecSym_INTENSET.setDependencies(pdecINTENSET, interruptDepList)

################################ Events ######################################
    pdecSym_Events_Menu = pdecComponent.createMenuSymbol("PDEC_EVENTS", None)
    pdecSym_Events_Menu.setLabel("Events")

    pdecSym_Input_Events = pdecComponent.createMenuSymbol("PDEC_INPUT_EVENTS", pdecSym_Events_Menu)
    pdecSym_Input_Events.setLabel("Input Events")
    pdecSym_Input_Events.setVisible(False)
    pdecSym_Input_Events.setDependencies(pdecInputEventsVisible, ["PDEC_CTRLA_MODE"])

    pdecSym_EVCTRL_EVEI0 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVEI0", pdecSym_Input_Events)
    pdecSym_EVCTRL_EVEI0.setLabel("Enable Input Event 0")
    eventCounterDepList.append("PDEC_COUNTER_EVEI0")
    pdecSym_EVCTRL_EVINV0 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVINV0", pdecSym_EVCTRL_EVEI0)
    pdecSym_EVCTRL_EVINV0.setLabel("Invert Input Event 0")

    pdecSym_EVCTRL_EVEI1 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVEI1", pdecSym_Input_Events)
    pdecSym_EVCTRL_EVEI1.setLabel("Enable Input Event 1")
    eventCounterDepList.append("PDEC_COUNTER_EVEI1")
    pdecSym_EVCTRL_EVINV1 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVINV1", pdecSym_EVCTRL_EVEI1)
    pdecSym_EVCTRL_EVINV1.setLabel("Invert Input Event 1")

    pdecSym_EVCTRL_EVEI2 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVEI2", pdecSym_Input_Events)
    pdecSym_EVCTRL_EVEI2.setLabel("Enable Input Event 2")
    eventCounterDepList.append("PDEC_COUNTER_EVEI2")
    pdecSym_EVCTRL_EVINV2 = pdecComponent.createBooleanSymbol("PDEC_COUNTER_EVINV2", pdecSym_EVCTRL_EVEI2)
    pdecSym_EVCTRL_EVINV2.setLabel("Invert Input Event 2")

    pdecSym_EVCTRL_EVACT = pdecComponent.createKeyValueSetSymbol("PDEC_EVCTRL_EVACT", pdecSym_Input_Events)
    pdecSym_EVCTRL_EVACT.setLabel("Select Event Action")
    pdecNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PDEC\"]/value-group@[name=\"PDEC_EVCTRL__EVACT\"]")
    pdecValues = []
    pdecValues = pdecNode.getChildren()
    for index in range(len(pdecValues)):
        pdecKeyName = pdecValues[index].getAttribute("name")
        pdecKeyValue = pdecValues[index].getAttribute("value")
        pdecSym_EVCTRL_EVACT.addKey(pdecKeyName, pdecKeyValue, pdecValues[index].getAttribute("caption"))
    pdecSym_EVCTRL_EVACT.setDefaultValue(0)
    pdecSym_EVCTRL_EVACT.setOutputMode("Key")
    pdecSym_EVCTRL_EVACT.setDisplayMode("Description")

    eventCounterDepList.append("PDEC_COUNTER_EVINV0")
    eventCounterDepList.append("PDEC_COUNTER_EVINV1")
    eventCounterDepList.append("PDEC_COUNTER_EVINV2")

    pdecSym_EVCTRL_OVF = pdecComponent.createBooleanSymbol("PDEC_EVCTRL_OVF", pdecSym_Events_Menu)
    pdecSym_EVCTRL_OVF.setLabel("Enable Overflow Event")
    eventDepList.append("PDEC_EVCTRL_OVF")
    eventHallDepList.append("PDEC_EVCTRL_OVF")
    eventCounterDepList.append("PDEC_EVCTRL_OVF")

    #Added for error event
    eventDepList.append("")
    eventHallDepList.append("")
    eventCounterDepList.append("")

    pdecSym_EVCTRL_DIR = pdecComponent.createBooleanSymbol("PDEC_EVCTRL_DIR", pdecSym_Events_Menu)
    pdecSym_EVCTRL_DIR.setLabel("Enable Direction Event")
    eventDepList.append("PDEC_EVCTRL_DIR")
    eventHallDepList.append("PDEC_EVCTRL_DIR")
    eventCounterDepList.append("PDEC_EVCTRL_DIR")

    pdecSym_EVCTRL_VLC = pdecComponent.createBooleanSymbol("PDEC_EVCTRL_VLC", pdecSym_Events_Menu)
    pdecSym_EVCTRL_VLC.setLabel("Enable Velocity Event")
    eventDepList.append("PDEC_EVCTRL_VLC")
    eventHallDepList.append("PDEC_EVCTRL_VLC")
    eventCounterDepList.append("PDEC_EVCTRL_VLC")

    pdecSym_EVCTRL_MC0 = pdecComponent.createBooleanSymbol("PDEC_EVCTRL_MC_0", pdecSym_Events_Menu)
    pdecSym_EVCTRL_MC0.setLabel("Enable Compare Match 0 Event")
    eventDepList.append("PDEC_EVCTRL_MC_0")
    eventHallDepList.append("PDEC_EVCTRL_MC_0")
    eventCounterDepList.append("PDEC_EVCTRL_MC_0")

    pdecSym_EVCTRL_MC1 = pdecComponent.createBooleanSymbol("PDEC_EVCTRL_MC_1", pdecSym_Events_Menu)
    pdecSym_EVCTRL_MC1.setLabel("Enable Compare Match 1 Event")
    eventDepList.append("PDEC_EVCTRL_MC_1")
    eventHallDepList.append("PDEC_EVCTRL_MC_1")
    eventCounterDepList.append("PDEC_EVCTRL_MC_1")

    pdecSym_EVCTRL = pdecComponent.createHexSymbol("PDEC_EVCTRL", None)
    pdecSym_EVCTRL.setVisible(False)
    pdecSym_EVCTRL.setDependencies(pdecEVCTRL, eventDepList)

    pdecSym_HALL_EVCTRL = pdecComponent.createHexSymbol("PDEC_HALL_EVCTRL", None)
    pdecSym_HALL_EVCTRL.setVisible(False)
    pdecSym_HALL_EVCTRL.setDependencies(pdecHallEVCTRL, eventHallDepList)

    pdecSym_COUNTER_EVCTRL = pdecComponent.createHexSymbol("PDEC_COUNTER_EVCTRL", None)
    pdecSym_COUNTER_EVCTRL.setVisible(False)
    pdecSym_COUNTER_EVCTRL.setDependencies(pdecCounterEVCTRL, eventCounterDepList)

    pdecSym_PIN = pdecComponent.createHexSymbol("PDEC_PIN", None)
    pdecSym_PIN.setVisible(False)
    pdecSym_PIN.setDefaultValue(pin_val)
    pdecSym_PIN.setDependencies(pdecPIN, eventDepList)

    pdecSym_PIN_INV = pdecComponent.createHexSymbol("PDEC_PIN_INV", None)
    pdecSym_PIN_INV.setVisible(False)
    pdecSym_PIN_INV.setDependencies(pdecPININV, eventDepList)

    pdecSym_HALL_PIN = pdecComponent.createHexSymbol("PDEC_HALL_PIN", None)
    pdecSym_HALL_PIN.setVisible(False)
    pdecSym_HALL_PIN.setDefaultValue(pin_val)
    pdecSym_HALL_PIN.setDependencies(pdecHallPIN, eventHallDepList)

    pdecSym_HALL_PIN_INV = pdecComponent.createHexSymbol("PDEC_HALL_PIN_INV", None)
    pdecSym_HALL_PIN_INV.setVisible(False)
    pdecSym_HALL_PIN_INV.setDependencies(pdecHallPININV, eventHallDepList)

    ###################################################################################################
    #################################### Sleep Configuration  #######################################
    ###################################################################################################

    #sleep configuration
    pdecSym_SleepConfiguration = pdecComponent.createMenuSymbol("PDEC_SLEEP_CONFIG", None)
    pdecSym_SleepConfiguration.setLabel("Sleep Configurations")

    #run standby mode
    pdecSym_CTRLA_RUNSTDBY = pdecComponent.createBooleanSymbol("PDEC_CTRLA_RUNSTDBY", pdecSym_SleepConfiguration)
    pdecSym_CTRLA_RUNSTDBY.setLabel("Run during Standby")

    pdecInstanceName.setDependencies(updateCodeGenerationProperty, ["PDEC_CTRLA_MODE"])

    ############################################################################
    #### Dependency ####
    ############################################################################
    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues = vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == pdecInstanceName.getValue():
            name = vectorValues[id].getAttribute("name")
            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")

    pdecSym_IntLines = pdecComponent.createIntegerSymbol("PDEC_NUM_INT_LINES", None)
    pdecSym_IntLines.setVisible(False)
    pdecSym_IntLines.setDefaultValue((len(InterruptVector) - 1))

    # Interrupt Dynamic settings
    pdecSym_UpdateInterruptStatus = pdecComponent.createBooleanSymbol("PDEC_INTERRUPT_STATUS", None)
    pdecSym_UpdateInterruptStatus.setDependencies(updatePDECInterruptStatus, interruptDepList)
    pdecSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    pdecSym_IntEnComment = pdecComponent.createCommentSymbol("PDEC_INTERRUPT_ENABLE_COMMENT", None)
    pdecSym_IntEnComment.setVisible(False)
    pdecSym_IntEnComment.setLabel("Warning!!! "+pdecInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    pdecSym_IntEnComment.setDependencies(updatePDECInterruptWarningStatus, interruptDepList+InterruptVectorUpdate)

    # Clock Warning status
    pdecSym_ClkEnComment = pdecComponent.createCommentSymbol("PDEC_CLOCK_ENABLE_COMMENT", None)
    pdecSym_ClkEnComment.setLabel("Warning!!! PDEC Peripheral Clock is Disabled in Clock Manager")
    pdecSym_ClkEnComment.setVisible(False)
    pdecSym_ClkEnComment.setDependencies(updatePDECClockWarningStatus, ["core."+pdecInstanceName.getValue()+"_CLOCK_ENABLE"])

    # events configure
    eventConfigureList = list(eventDepList)
    eventConfigureList.append("PDEC_CTRLA_MODE")
    eventConfigureList.append("PDEC_HALL_A")
    eventConfigureList.append("PDEC_HALL_B")
    eventConfigureList.append("PDEC_HALL_C")
    eventConfigureList.append("PDEC_COUNTER_EVEI0")
    eventConfigureList.append("PDEC_COUNTER_EVEI1")
    eventConfigureList.append("PDEC_COUNTER_EVEI2")
    eventConfigureList.append("PDEC_COUNTER_EVINV0")
    eventConfigureList.append("PDEC_COUNTER_EVINV1")
    eventConfigureList.append("PDEC_COUNTER_EVINV2")

    pdecSym_EventsComment = pdecComponent.createCommentSymbol("PDEC_EVENTS_COMMENT", None)
    pdecSym_EventsComment.setLabel("Events Configure")
    pdecSym_EventsComment.setVisible(False)
    pdecSym_EventsComment.setDependencies(pdecEVSYSConfigure, eventConfigureList)


    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pdecSym_CommonHeaderFile = pdecComponent.createFileSymbol("PDEC_COMMON_HEADER", None)
    pdecSym_CommonHeaderFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_common.h")
    pdecSym_CommonHeaderFile.setOutputName("plib_pdec_common.h")
    pdecSym_CommonHeaderFile.setDestPath("/peripheral/pdec/")
    pdecSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_CommonHeaderFile.setType("HEADER")
    pdecSym_CommonHeaderFile.setMarkup(False)

    pdecSym_QdecHeaderFile = pdecComponent.createFileSymbol("PDEC_QDEC_HEADER", None)
    pdecSym_QdecHeaderFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_qdec.h.ftl")
    pdecSym_QdecHeaderFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".h")
    pdecSym_QdecHeaderFile.setDestPath("/peripheral/pdec/")
    pdecSym_QdecHeaderFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_QdecHeaderFile.setType("HEADER")
    pdecSym_QdecHeaderFile.setMarkup(True)

    pdecSym_QdecSourceFile = pdecComponent.createFileSymbol("PDEC_QDEC_SOURCE", None)
    pdecSym_QdecSourceFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_qdec.c.ftl")
    pdecSym_QdecSourceFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".c")
    pdecSym_QdecSourceFile.setDestPath("/peripheral/pdec/")
    pdecSym_QdecSourceFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_QdecSourceFile.setType("SOURCE")
    pdecSym_QdecSourceFile.setMarkup(True)

    pdecSym_HallHeaderFile = pdecComponent.createFileSymbol("PDEC_HALL_HEADER", None)
    pdecSym_HallHeaderFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_hall.h.ftl")
    pdecSym_HallHeaderFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".h")
    pdecSym_HallHeaderFile.setDestPath("/peripheral/pdec/")
    pdecSym_HallHeaderFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_HallHeaderFile.setType("HEADER")
    pdecSym_HallHeaderFile.setMarkup(True)

    pdecSym_HallSourceFile = pdecComponent.createFileSymbol("PDEC_HALL_SOURCE", None)
    pdecSym_HallSourceFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_hall.c.ftl")
    pdecSym_HallSourceFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".c")
    pdecSym_HallSourceFile.setDestPath("/peripheral/pdec/")
    pdecSym_HallSourceFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_HallSourceFile.setType("SOURCE")
    pdecSym_HallSourceFile.setMarkup(True)

    pdecSym_CounterHeaderFile = pdecComponent.createFileSymbol("PDEC_COUNTER_HEADER", None)
    pdecSym_CounterHeaderFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_counter.h.ftl")
    pdecSym_CounterHeaderFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".h")
    pdecSym_CounterHeaderFile.setDestPath("/peripheral/pdec/")
    pdecSym_CounterHeaderFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_CounterHeaderFile.setType("HEADER")
    pdecSym_CounterHeaderFile.setMarkup(True)

    pdecSym_CounterSourceFile = pdecComponent.createFileSymbol("PDEC_COUNTER_SOURCE", None)
    pdecSym_CounterSourceFile.setSourcePath("../peripheral/pdec_u2263/templates/plib_pdec_counter.c.ftl")
    pdecSym_CounterSourceFile.setOutputName("plib_"+pdecInstanceName.getValue().lower()+".c")
    pdecSym_CounterSourceFile.setDestPath("/peripheral/pdec/")
    pdecSym_CounterSourceFile.setProjectPath("config/" + configName + "/peripheral/pdec/")
    pdecSym_CounterSourceFile.setType("SOURCE")
    pdecSym_CounterSourceFile.setMarkup(True)

    pdecSym_SystemInitFile = pdecComponent.createFileSymbol("PDEC_SYS_INT", None)
    pdecSym_SystemInitFile.setType("STRING")
    pdecSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pdecSym_SystemInitFile.setSourcePath("../peripheral/pdec_u2263/templates/system/initialization.c.ftl")
    pdecSym_SystemInitFile.setMarkup(True)

    pdecSym_SystemDefFile = pdecComponent.createFileSymbol("PDEC_SYS_DEF", None)
    pdecSym_SystemDefFile.setType("STRING")
    pdecSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pdecSym_SystemDefFile.setSourcePath("../peripheral/pdec_u2263/templates/system/definitions.h.ftl")
    pdecSym_SystemDefFile.setMarkup(True)
