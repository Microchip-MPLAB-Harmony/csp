# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
from math import ceil
#########################################    Global Variables ----START       #########################################################
global opampInstanceName
global OPAMPfilesArray
OPAMPfilesArray = []

#######################################################################################################################################
#####################################        Callback Funtions ----START      #########################################################
#######################################################################################################################################

def fileUpdate(symbol, event):
    global OPAMPfilesArray
    if event["value"] == False:
        OPAMPfilesArray[0].setSecurity("SECURE")
        OPAMPfilesArray[1].setSecurity("SECURE")
        OPAMPfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        OPAMPfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    else:
        OPAMPfilesArray[0].setSecurity("NON_SECURE")
        OPAMPfilesArray[1].setSecurity("NON_SECURE")
        OPAMPfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        OPAMPfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    
#Show warning if APB clock is not enabled
def updateOPAMPClockWarningStatus(MySymbol, event):

    if event["value"] == False:
        MySymbol.setVisible(True)
    else:
        MySymbol.setVisible(False)
        
#######################################################################################################################################
#####################################        Callback Funtions ---- END      ##########################################################
#######################################################################################################################################

#######################################################################################################################################
#####################################               Component                ##########################################################
#######################################################################################################################################

def instantiateComponent(opampComponent):
    global opampInstanceName
    global opampSym_OPAMPCTRL_ENABLE
    opampSym_OPAMPCTRL_ENABLE = []
    global opampSym_OPAMPCTRL_ANAOUT
    opampSym_OPAMPCTRL_ANAOUT = []
    global opampSym_OPAMPCTRL_BIAS
    opampSym_OPAMPCTRL_BIAS = []
    global opampSym_OPAMPCTRL_RUNSTDBY
    opampSym_OPAMPCTRL_RUNSTDBY = []
    global opampSym_OPAMPCTRL_ONDEMAND
    opampSym_OPAMPCTRL_ONDEMAND = []
    global opampSym_OPAMPCTRL_RES2OUT
    opampSym_OPAMPCTRL_RES2OUT = []
    global opampSym_OPAMPCTRL_RES2VCC
    opampSym_OPAMPCTRL_RES2VCC = []
    global opampSym_OPAMPCTRL_RES1EN
    opampSym_OPAMPCTRL_RES1EN = []
    global opampSym_OPAMPCTRL_RES1MUX
    opampSym_OPAMPCTRL_RES1MUX = []
    global opampSym_OPAMPCTRL_POTMUX
    opampSym_OPAMPCTRL_POTMUX = []
    global opampSym_OPAMPCTRL_MUXPOS
    opampSym_OPAMPCTRL_MUXPOS = []
    global opampSym_OPAMPCTRL_MUXNEG
    opampSym_OPAMPCTRL_MUXNEG = []

    opampInstanceName = opampComponent.createStringSymbol("OPAMP_INSTANCE_NAME", None)
    opampInstanceName.setVisible(False)
    opampInstanceName.setDefaultValue(opampComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", opampInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    parametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"OPAMP\"]/instance@[name=\"OPAMP""\"]/parameters")
    numOfopamps = 0
    parameters = []
    parameters = parametersNode.getChildren()
    for param in range (0, len(parameters)):
        if(parameters[param].getAttribute("name") == "NUM_OPAMPS"):
            numOfopamps = int(parameters[param].getAttribute("value"))

    opampSym_NUM_OPAMPS = opampComponent.createIntegerSymbol("OPAMP_NUM_OPAMPS", None)
    opampSym_NUM_OPAMPS.setDefaultValue(int(numOfopamps))
    opampSym_NUM_OPAMPS.setVisible(False)
    
    opampSym_CtrlaEnable = opampComponent.createBooleanSymbol("OPAMP_CTRLA_ENABLE", None)
    opampSym_CtrlaEnable.setDefaultValue(True)
    opampSym_CtrlaEnable.setVisible(False)
        
    #Populate menu for all comparators in the OPAMP peripheral
    for opampID in range(0, int(numOfopamps)):
        opampSym_Menu = opampComponent.createMenuSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "MENU", None)
        opampSym_Menu.setLabel("Op Amp " + str(opampID) + " Settings")
    
        #Enable op amp
        opampSym_OPAMPCTRL_ENABLE.append(opampID)
        opampSym_OPAMPCTRL_ENABLE[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_ENABLE", opampSym_Menu)
        opampSym_OPAMPCTRL_ENABLE[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_ENABLE[opampID].setLabel("Op Amp " + str(opampID) + " Enable")

        #MUXPOS
        opampSym_OPAMPCTRL_MUXPOS.append(opampID)
        opampSym_OPAMPCTRL_MUXPOS[opampID] = opampComponent.createKeyValueSetSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_MUXPOS", opampSym_Menu)
        opampSym_OPAMPCTRL_MUXPOS[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_MUXPOS[opampID].setLabel("Positive Input Mux Selection")

        if (opampID == 0):
            opampSym_OPAMPCTRL_MUXPOS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL0__MUXPOS\"]")
        elif (opampID == 1):
            opampSym_OPAMPCTRL_MUXPOS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL1__MUXPOS\"]")
        elif (opampID == 2):
            opampSym_OPAMPCTRL_MUXPOS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL2__MUXPOS\"]")
        opampSym_OPAMPCTRL_MUXPOS_Node_Values = []
        opampSym_OPAMPCTRL_MUXPOS_Node_Values = opampSym_OPAMPCTRL_MUXPOS_Node.getChildren()

        for id in range(len(opampSym_OPAMPCTRL_MUXPOS_Node_Values)):
            opampSym_OPAMPCTRL_MUXPOS_Key_Name = opampSym_OPAMPCTRL_MUXPOS_Node_Values[id].getAttribute("name")
            opampSym_OPAMPCTRL_MUXPOS_Key_Description = opampSym_OPAMPCTRL_MUXPOS_Node_Values[id].getAttribute("caption")
            opampSym_OPAMPCTRL_MUXPOS_Key_Value = opampSym_OPAMPCTRL_MUXPOS_Node_Values[id].getAttribute("value")
            opampSym_OPAMPCTRL_MUXPOS[opampID].addKey(opampSym_OPAMPCTRL_MUXPOS_Key_Name, opampSym_OPAMPCTRL_MUXPOS_Key_Value, opampSym_OPAMPCTRL_MUXPOS_Key_Description)

        opampSym_OPAMPCTRL_MUXPOS[opampID].setDefaultValue(0)
        opampSym_OPAMPCTRL_MUXPOS[opampID].setOutputMode("Value")
        opampSym_OPAMPCTRL_MUXPOS[opampID].setDisplayMode("Description")
        
        #MUXNEG
        opampSym_OPAMPCTRL_MUXNEG.append(opampID)
        opampSym_OPAMPCTRL_MUXNEG[opampID] = opampComponent.createKeyValueSetSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_MUXNEG", opampSym_Menu)
        opampSym_OPAMPCTRL_MUXNEG[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_MUXNEG[opampID].setLabel("Negative Input Mux Selection")

        if (opampID == 0):
            opampSym_OPAMPCTRL_MUXNEG_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL0__MUXNEG\"]")
        elif (opampID == 1):
            opampSym_OPAMPCTRL_MUXNEG_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL1__MUXNEG\"]")
        elif (opampID == 2):
            opampSym_OPAMPCTRL_MUXNEG_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL2__MUXNEG\"]")
        opampSym_OPAMPCTRL_MUXNEG_Node_Values = []
        opampSym_OPAMPCTRL_MUXNEG_Node_Values = opampSym_OPAMPCTRL_MUXNEG_Node.getChildren()

        for id in range(len(opampSym_OPAMPCTRL_MUXNEG_Node_Values)):
            opampSym_OPAMPCTRL_MUXNEG_Key_Name = opampSym_OPAMPCTRL_MUXNEG_Node_Values[id].getAttribute("name")
            opampSym_OPAMPCTRL_MUXNEG_Key_Description = opampSym_OPAMPCTRL_MUXNEG_Node_Values[id].getAttribute("caption")
            opampSym_OPAMPCTRL_MUXNEG_Key_Value = opampSym_OPAMPCTRL_MUXNEG_Node_Values[id].getAttribute("value")
            opampSym_OPAMPCTRL_MUXNEG[opampID].addKey(opampSym_OPAMPCTRL_MUXNEG_Key_Name, opampSym_OPAMPCTRL_MUXNEG_Key_Value, opampSym_OPAMPCTRL_MUXNEG_Key_Description)

        opampSym_OPAMPCTRL_MUXNEG[opampID].setDefaultValue(0)
        opampSym_OPAMPCTRL_MUXNEG[opampID].setOutputMode("Value")
        opampSym_OPAMPCTRL_MUXNEG[opampID].setDisplayMode("Description")
        
        #RES1EN
        opampSym_OPAMPCTRL_RES1EN.append(opampID)
        opampSym_OPAMPCTRL_RES1EN[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_RES1EN", opampSym_Menu)
        opampSym_OPAMPCTRL_RES1EN[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_RES1EN[opampID].setLabel("Connect R1 to the multiplexer")
        opampSym_OPAMPCTRL_RES1EN[opampID].setDescription("Connecting R1 to the MUX allows it to be connected to the op amp input, GND or the internal DAC output");
        opampSym_OPAMPCTRL_RES1EN[opampID].setDefaultValue(False)
        
        #RES1MUX
        opampSym_OPAMPCTRL_RES1MUX.append(opampID)
        opampSym_OPAMPCTRL_RES1MUX[opampID] = opampComponent.createKeyValueSetSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_RES1MUX", opampSym_OPAMPCTRL_RES1EN[opampID])
        opampSym_OPAMPCTRL_RES1MUX[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_RES1MUX[opampID].setLabel("Resistor R1 connection")
        opampSym_OPAMPCTRL_RES1MUX[opampID].setDescription("These bits select the connection of R1 resistor of the potentiometer")

        if (opampID == 0):
            opampSym_OPAMPCTRL_RES1MUX_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL0__RES1MUX\"]")
        elif (opampID == 1):
            opampSym_OPAMPCTRL_RES1MUX_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL1__RES1MUX\"]")
        elif (opampID == 2):
            opampSym_OPAMPCTRL_RES1MUX_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL2__RES1MUX\"]")

        opampSym_OPAMPCTRL_RES1MUX_Node_Values = []
        opampSym_OPAMPCTRL_RES1MUX_Node_Values = opampSym_OPAMPCTRL_RES1MUX_Node.getChildren()

        opampSym_OPAMPCTRL_RES1MUX_Default_Val = 0

        for id in range(len(opampSym_OPAMPCTRL_RES1MUX_Node_Values)):
            opampSym_OPAMPCTRL_RES1MUX_Key_Name = opampSym_OPAMPCTRL_RES1MUX_Node_Values[id].getAttribute("name")

            if(opampSym_OPAMPCTRL_RES1MUX_Key_Name == "OAxPOS"):
                opampSym_OPAMPCTRL_RES1MUX_Default_Val = id

            opampSym_OPAMPCTRL_RES1MUX_Key_Description = opampSym_OPAMPCTRL_RES1MUX_Node_Values[id].getAttribute("caption")
            opampSym_OPAMPCTRL_RES1MUX_Key_Value = opampSym_OPAMPCTRL_RES1MUX_Node_Values[id].getAttribute("value")
            opampSym_OPAMPCTRL_RES1MUX[opampID].addKey(opampSym_OPAMPCTRL_RES1MUX_Key_Name, opampSym_OPAMPCTRL_RES1MUX_Key_Value, opampSym_OPAMPCTRL_RES1MUX_Key_Description)

        opampSym_OPAMPCTRL_RES1MUX[opampID].setDefaultValue(opampSym_OPAMPCTRL_RES1MUX_Default_Val)
        opampSym_OPAMPCTRL_RES1MUX[opampID].setOutputMode("Value")
        opampSym_OPAMPCTRL_RES1MUX[opampID].setDisplayMode("Description")
        
        #RES2OUT
        opampSym_OPAMPCTRL_RES2OUT.append(opampID)
        opampSym_OPAMPCTRL_RES2OUT[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_RES2OUT", opampSym_Menu)
        opampSym_OPAMPCTRL_RES2OUT[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_RES2OUT[opampID].setLabel("Connect resistor ladder to op amp output")
        opampSym_OPAMPCTRL_RES2OUT[opampID].setDescription("Enable this if the resistor ladder is going to be used in the feedback path of the op amp");

        #RES2VCC
        opampSym_OPAMPCTRL_RES2VCC.append(opampID)
        opampSym_OPAMPCTRL_RES2VCC[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_RES2VCC", opampSym_Menu)
        opampSym_OPAMPCTRL_RES2VCC[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_RES2VCC[opampID].setLabel("Connect resistor ladder to VCC")
        opampSym_OPAMPCTRL_RES2VCC[opampID].setDefaultValue(False)
        opampSym_OPAMPCTRL_RES2VCC[opampID].setDescription("Enable this if the resistor ladder is used to form a voltage divider. In this case resistor R1 should be connected to GND");
            
        #POTMUX
        opampSym_OPAMPCTRL_POTMUX.append(opampID)
        opampSym_OPAMPCTRL_POTMUX[opampID] = opampComponent.createKeyValueSetSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_POTMUX", opampSym_Menu)
        opampSym_OPAMPCTRL_POTMUX[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_POTMUX[opampID].setLabel("Select potentiometer configuration")

        opampSym_OPAMPCTRL_POTMUX_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL__POTMUX\"]")
        opampSym_OPAMPCTRL_POTMUX_Node_Values = []
        opampSym_OPAMPCTRL_POTMUX_Node_Values = opampSym_OPAMPCTRL_POTMUX_Node.getChildren()

        opampSym_OPAMPCTRL_POTMUX_Default_Val = 0

        for id in range(len(opampSym_OPAMPCTRL_POTMUX_Node_Values)):
            opampSym_OPAMPCTRL_POTMUX_Key_Name = opampSym_OPAMPCTRL_POTMUX_Node_Values[id].getAttribute("name")

            if(opampSym_OPAMPCTRL_POTMUX_Key_Name == "OAxPOS"):
                opampSym_OPAMPCTRL_POTMUX_Default_Val = id

            opampSym_OPAMPCTRL_POTMUX_Key_Description = opampSym_OPAMPCTRL_POTMUX_Node_Values[id].getAttribute("caption")
            opampSym_OPAMPCTRL_POTMUX_Key_Value = opampSym_OPAMPCTRL_POTMUX_Node_Values[id].getAttribute("value")
            opampSym_OPAMPCTRL_POTMUX[opampID].addKey(opampSym_OPAMPCTRL_POTMUX_Key_Name, opampSym_OPAMPCTRL_POTMUX_Key_Value, opampSym_OPAMPCTRL_POTMUX_Key_Description)

        opampSym_OPAMPCTRL_POTMUX[opampID].setDefaultValue(opampSym_OPAMPCTRL_POTMUX_Default_Val)
        opampSym_OPAMPCTRL_POTMUX[opampID].setOutputMode("Value")
        opampSym_OPAMPCTRL_POTMUX[opampID].setDisplayMode("Key")
        
        #Analog Output
        opampSym_OPAMPCTRL_ANAOUT.append(opampID)
        opampSym_OPAMPCTRL_ANAOUT[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_ANAOUT", opampSym_Menu)
        opampSym_OPAMPCTRL_ANAOUT[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_ANAOUT[opampID].setLabel("Enable output to ADC or AC")
        
        #BIAS
        opampSym_OPAMPCTRL_BIAS.append(opampID)
        opampSym_OPAMPCTRL_BIAS[opampID] = opampComponent.createKeyValueSetSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_BIAS", opampSym_Menu)
        opampSym_OPAMPCTRL_BIAS[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_BIAS[opampID].setLabel("Bias Mode Selection")

        opampSym_OPAMPCTRL_BIAS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/value-group@[name=\"OPAMP_OPAMPCTRL__BIAS\"]")
        opampSym_OPAMPCTRL_BIAS_Node_Values = []
        opampSym_OPAMPCTRL_BIAS_Node_Values = opampSym_OPAMPCTRL_BIAS_Node.getChildren()

        opampSym_OPAMPCTRL_BIAS_Default_Val = 0

        for id in range(len(opampSym_OPAMPCTRL_BIAS_Node_Values)):
            opampSym_OPAMPCTRL_BIAS_Key_Name = opampSym_OPAMPCTRL_BIAS_Node_Values[id].getAttribute("name")

            if(opampSym_OPAMPCTRL_BIAS_Key_Name == "Mode 0"):
                opampSym_OPAMPCTRL_BIAS_Default_Val = id

            opampSym_OPAMPCTRL_BIAS_Key_Description = opampSym_OPAMPCTRL_BIAS_Node_Values[id].getAttribute("caption")
            opampSym_OPAMPCTRL_BIAS_Key_Value = opampSym_OPAMPCTRL_BIAS_Node_Values[id].getAttribute("value")
            opampSym_OPAMPCTRL_BIAS[opampID].addKey(opampSym_OPAMPCTRL_BIAS_Key_Name, opampSym_OPAMPCTRL_BIAS_Key_Value, opampSym_OPAMPCTRL_BIAS_Key_Description)

        opampSym_OPAMPCTRL_BIAS[opampID].setDefaultValue(opampSym_OPAMPCTRL_BIAS_Default_Val)
        opampSym_OPAMPCTRL_BIAS[opampID].setOutputMode("Value")
        opampSym_OPAMPCTRL_BIAS[opampID].setDisplayMode("Description")
        
        #RUNSTDBY
        opampSym_OPAMPCTRL_RUNSTDBY.append(opampID)
        opampSym_OPAMPCTRL_RUNSTDBY[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_RUNSTDBY", opampSym_Menu)
        opampSym_OPAMPCTRL_RUNSTDBY[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_RUNSTDBY[opampID].setLabel("Run op amp in Standby Sleep")
        
        #ONDEMAND
        opampSym_OPAMPCTRL_ONDEMAND.append(opampID)
        opampSym_OPAMPCTRL_ONDEMAND[opampID] = opampComponent.createBooleanSymbol("OPAMP_OPAMPCTRL_" + str(opampID) + "_ONDEMAND", opampSym_Menu)
        opampSym_OPAMPCTRL_ONDEMAND[opampID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:OPAMPCTRL0")
        opampSym_OPAMPCTRL_ONDEMAND[opampID].setLabel("Enable On-demand operation")
        opampSym_OPAMPCTRL_ONDEMAND[opampID].setDescription("Enable op amp only when another peripheral is requesting the op amp to be used as an input");
        
    #Disable voltage doubler
    opampSym_CTRLA_LPMUX = opampComponent.createBooleanSymbol("OPAMP_CTRLA_LPMUX", None)
    opampSym_CTRLA_LPMUX.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:CTRLA")
    opampSym_CTRLA_LPMUX.setLabel("Disable voltage doubler")
    opampSym_CTRLA_LPMUX.setDefaultValue(True)
    opampSym_CTRLA_LPMUX.setDescription("If the supply voltage is always above 2.5V, the voltage doubler can be disabled")

    #checkRESCTRL register
    resctrlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"OPAMP\"]/register-group/register@[name=\"RESCTRL\"]")
    if resctrlNode != None:
        resctrlMenu = opampComponent.createMenuSymbol("RESCTRL_MENU", None)
        resctrlMenu.setLabel("Resistor Control Menu")

        res2Out = opampComponent.createBooleanSymbol("RESCTRL_RES2OUT", resctrlMenu)
        res2Out.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:RESCTRL")
        res2Out.setLabel("Resistor ladder To Output")
        res2Out.setDefaultValue(False)

        res1En = opampComponent.createBooleanSymbol("RESCTRL_RES1EN", resctrlMenu)
        res1En.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:RESCTRL")
        res1En.setLabel("Enable Resistor 1 (DAC/REFBUF) output to Mux")
        res1En.setDefaultValue(False)

        node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OPAMP"]/value-group@[name="OPAMP_RESCTRL__RES1MUX"]')
        nodeValues = node.getChildren()
        res1Mux = opampComponent.createKeyValueSetSymbol("RESCTRL_RES1MUX", resctrlMenu)
        res1Mux.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:RESCTRL")
        res1Mux.setLabel("Resistor1 Source")
        for index in range(0, len(nodeValues)):
            key =  nodeValues[index].getAttribute("name")
            value =  nodeValues[index].getAttribute("value")
            description =  nodeValues[index].getAttribute("caption")
            res1Mux.addKey(key, value, description)
        res1Mux.setDefaultValue(0)
        res1Mux.setOutputMode("Value")
        res1Mux.setDisplayMode("Description")

        node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OPAMP"]/value-group@[name="OPAMP_RESCTRL__POTMUX"]')
        nodeValues = node.getChildren()
        resctrlPotmux = opampComponent.createKeyValueSetSymbol("RESCTRL_POTMUX", resctrlMenu)
        resctrlPotmux.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:RESCTRL")
        resctrlPotmux.setLabel("Potentiometer selection")
        for index in range(0, len(nodeValues)):
            key =  nodeValues[index].getAttribute("name")
            value =  nodeValues[index].getAttribute("value")
            description =  nodeValues[index].getAttribute("caption")
            resctrlPotmux.addKey(key, value, description)
        resctrlPotmux.setDefaultValue(0)
        resctrlPotmux.setOutputMode("Value")
        resctrlPotmux.setDisplayMode("Description")

        node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OPAMP"]/value-group@[name="OPAMP_RESCTRL__REFBUFLEVEL"]')
        nodeValues = node.getChildren()
        resctrlREFBUFLEVEL = opampComponent.createKeyValueSetSymbol("RESCTRL_REFBUFLEVEL", resctrlMenu)
        resctrlREFBUFLEVEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opamp_u2237;register:RESCTRL")
        resctrlREFBUFLEVEL.setLabel("Reference output voltage")
        for index in range(0, len(nodeValues)):
            key =  nodeValues[index].getAttribute("name")
            value =  nodeValues[index].getAttribute("value")
            description =  nodeValues[index].getAttribute("caption")
            resctrlREFBUFLEVEL.addKey(key, value, description)
        resctrlREFBUFLEVEL.setDefaultValue(0)
        resctrlREFBUFLEVEL.setOutputMode("Value")
        resctrlREFBUFLEVEL.setDisplayMode("Description")
        
    ############################################################################
    #### Dependency ####
    ############################################################################

    # Clock Warning status
    opampSym_ClkEnComment = opampComponent.createCommentSymbol("OPAMP_CLOCK_ENABLE_COMMENT", None)
    opampSym_ClkEnComment.setVisible(False)
    opampSym_ClkEnComment.setLabel("Warning!!! " +opampInstanceName.getValue()+" Clock is Disabled in Clock Manager")
    opampSym_ClkEnComment.setDependencies(updateOPAMPClockWarningStatus, ["core." + opampInstanceName.getValue() + "_CLOCK_ENABLE"])
    
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    opampHeader1File = opampComponent.createFileSymbol("OPAMP_HEADER", None)
    opampHeader1File.setSourcePath("../peripheral/opamp_u2237/templates/plib_opamp.h.ftl")
    opampHeader1File.setOutputName("plib_" + opampInstanceName.getValue().lower() + ".h")
    opampHeader1File.setMarkup(True)
    opampHeader1File.setDestPath("/peripheral/opamp/")
    opampHeader1File.setProjectPath("config/" + configName + "/peripheral/opamp/")
    opampHeader1File.setType("HEADER")

    opampSource1File = opampComponent.createFileSymbol("OPAMP_SOURCE", None)
    opampSource1File.setSourcePath("../peripheral/opamp_u2237/templates/plib_opamp.c.ftl")
    opampSource1File.setOutputName("plib_" + opampInstanceName.getValue().lower() + ".c")
    opampSource1File.setMarkup(True)
    opampSource1File.setDestPath("/peripheral/opamp/")
    opampSource1File.setProjectPath("config/" + configName + "/peripheral/opamp/")
    opampSource1File.setType("SOURCE")

    opampSystemInitFile = opampComponent.createFileSymbol("OPAMP_SYS_INIT", None)
    opampSystemInitFile.setType("STRING")
    opampSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    opampSystemInitFile.setSourcePath("../peripheral/opamp_u2237/templates/system/initialization.c.ftl")
    opampSystemInitFile.setMarkup(True)

    opampSystemDefFile = opampComponent.createFileSymbol("OPAMP_SYS_DEF", None)
    opampSystemDefFile.setType("STRING")
    opampSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    opampSystemDefFile.setSourcePath("../peripheral/opamp_u2237/templates/system/definitions.h.ftl")
    opampSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global OPAMPfilesArray
        opampIsNonSecure = Database.getSymbolValue("core", opampComponent.getID().upper() + "_IS_NON_SECURE")
        opampSystemDefFile.setDependencies(fileUpdate, ["core." + opampComponent.getID().upper() + "_IS_NON_SECURE"])
        OPAMPfilesArray.append(opampHeader1File)
        OPAMPfilesArray.append(opampSource1File)
        OPAMPfilesArray.append(opampSystemInitFile)
        OPAMPfilesArray.append(opampSystemDefFile)
        if opampIsNonSecure == False:
            OPAMPfilesArray[0].setSecurity("SECURE")
            OPAMPfilesArray[1].setSecurity("SECURE")
            OPAMPfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            OPAMPfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")