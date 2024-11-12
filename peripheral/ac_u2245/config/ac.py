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
from math import ceil
#########################################------------------ Global Variables -------start-----#############################################
global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global acInstanceName
global acSym_SCALERn
global ACfilesArray
ACfilesArray = []
#######################################################################################################################################
#####################################        Callback Funtions ----START      #########################################################
#######################################################################################################################################

def fileUpdate(symbol, event):
    global ACfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        ACfilesArray[0].setSecurity("SECURE")
        ACfilesArray[1].setSecurity("SECURE")
        ACfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        ACfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        ACfilesArray[0].setSecurity("NON_SECURE")
        ACfilesArray[1].setSecurity("NON_SECURE")
        ACfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        ACfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, True)

#Control VDD Scaler value visibility
def setacScalerVisibility(MySymbol, event):
    global acSym_COMPCTRL_MUXNEG
    id = int(filter(str.isdigit, str(MySymbol.getID())))
    if ("VSCALE" in acSym_COMPCTRL_MUXNEG[id].getSelectedKey() or
            "VSCALE" in acSym_COMPCTRL_MUXPOS[id].getSelectedKey()):
        MySymbol.setVisible(True)
    else:
        MySymbol.setVisible(False)
        
#Control Hysteresis visibility
def setacHystVisibility(MySymbol, event):
    symObj = event["symbol"]
    if symObj.getValue() == True:
        MySymbol.setVisible(False)
    else:
        MySymbol.setVisible(True)

#Update Symbol Visibility
def setacSymbolVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateACInterruptStatus(symbol, event):
    global nvicDep
    component = symbol.getComponent()
    interrupt = False
    for id in range (0, (len(nvicDep) - 1)):
        val = component.getSymbolValue(nvicDep[id])
        if val == True:
            interrupt = True

    Database.setSymbolValue("core", InterruptVector, interrupt, 2)
    Database.setSymbolValue("core", InterruptHandlerLock, interrupt, 2)
    if interrupt == True:
        Database.setSymbolValue("core", InterruptHandler, acInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, acInstanceName.getValue() + "_Handler", 2)

def updateACInterruptWarningStatus(symbol, event):
    global nvicDep
    component = symbol.getComponent()
    interrupt = False
    for id in range (0, (len(nvicDep) - 1)):
        val = component.getSymbolValue(nvicDep[id])
        if val == True:
            interrupt = True
    
    InterruptVectorUpdate = acInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    if ((interrupt == True) and (Database.getSymbolValue("core", InterruptVectorUpdate) == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateACClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def acEvesysConfigure(symbol, event):
    if("AC_EVCTRL_COMPEO" in event["id"]):
        instance = filter(str.isdigit,str(event["id"]))
        Database.setSymbolValue("evsys", "GENERATOR_AC_COMP_"+str(instance) + "_ACTIVE", event["value"], 2)

    if("AC_EVCTRL_WINEO" in event["id"]):
        instance = filter(str.isdigit,str(event["id"]))
        Database.setSymbolValue("evsys", "GENERATOR_AC_WIN_"+str(instance) + "_ACTIVE", event["value"], 2)

    if ("AC_EVCTRL_COMPEI" in event["id"]):
        instance = filter(str.isdigit,str(event["id"]))
        Database.setSymbolValue("evsys", "USER_AC_SOC_"+str(instance) + "_READY", event["value"], 2)


#######################################################################################################################################
#####################################        Callback Funtions ---- END      ##########################################################
#######################################################################################################################################

#######################################################################################################################################
#####################################       Database Components      ##########################################################
#######################################################################################################################################

def instantiateComponent(acComponent):

    global acInstanceName
    global acSym_Enable
    global acSym_UpdateInterruptStatus
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorSecurity
    global acSym_COMPCTRL_MUXNEG
    acSym_COMPCTRL_MUXNEG = []
    global acSym_COMPCTRL_MUXPOS
    acSym_COMPCTRL_MUXPOS = []
    evsysDep = []
    global nvicDep
    nvicDep = []    
    
    acInstanceName = acComponent.createStringSymbol("AC_INSTANCE_NAME", None)
    acInstanceName.setVisible(False)
    acInstanceName.setDefaultValue(acComponent.getID().upper())

    acSym_Enable = []
    acSym_SCALERn = []
    #Clock enable
    Database.setSymbolValue("core", acInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    ################################ ATDF ####################################################
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AC\"]/instance@[name=\"AC""\"]/parameters")
    numOfComparators = 0
    parameters = []
    parameters = node.getChildren()
    for param in range (0, len(parameters)):
        if(parameters[param].getAttribute("name") == "NUM_CMP"):
            numOfComparators = int(parameters[param].getAttribute("value"))
            
    acSym_NUM_CHANNELS = acComponent.createIntegerSymbol("AC_NUM_COMPARATORS", None)
    acSym_NUM_CHANNELS.setDefaultValue(int(numOfComparators))
    acSym_NUM_CHANNELS.setVisible(False)

    acSym_COMPCTRL_MUXPOS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__MUXPOS\"]")
    acSym_COMPCTRL_MUXPOS_Node_Values = acSym_COMPCTRL_MUXPOS_Node.getChildren()   
    for id in range(len(acSym_COMPCTRL_MUXPOS_Node_Values)):
        acSym_MUXPOS_ENUM = acComponent.createStringSymbol("AC_MUXPOS_ENUM_"+str(id), None)
        acSym_MUXPOS_ENUM.setDefaultValue(acSym_COMPCTRL_MUXPOS_Node_Values[id].getAttribute("name"))
        acSym_MUXPOS_ENUM.setVisible(False)

    acSym_COMPCTRL_MUXNEG_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__MUXNEG\"]")
    acSym_COMPCTRL_MUXNEG_Node_Values = acSym_COMPCTRL_MUXNEG_Node.getChildren()   
    for id in range(len(acSym_COMPCTRL_MUXNEG_Node_Values)):
        acSym_MUXNEG_ENUM = acComponent.createStringSymbol("AC_MUXNEG_ENUM_"+str(id), None)
        acSym_MUXNEG_ENUM.setDefaultValue(acSym_COMPCTRL_MUXNEG_Node_Values[id].getAttribute("name"))
        acSym_MUXNEG_ENUM.setVisible(False)        
    
    #Populate menu for all comparators in the AC peripheral
    for comparatorID in range(0, int(numOfComparators)):
        acSym_Enable.append(comparatorID)

        acSym_Enable[comparatorID] = acComponent.createBooleanSymbol("ANALOG_COMPARATOR_ENABLE_" + str(comparatorID), None)
        acSym_Enable[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:compctrl0")
        acSym_Enable[comparatorID].setLabel("Comparator " + str(comparatorID) + " Settings")

        #Interrupt Enable
        global acInterrupt_Enable
        acInterrupt_Enable = acComponent.createBooleanSymbol("COMP" + str(comparatorID) + "INTERRUPT_ENABLE", acSym_Enable[comparatorID])
        acInterrupt_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:intenset")
        acInterrupt_Enable.setLabel("Comparator Interrupt Enable")
        acInterrupt_Enable.setVisible(False)
        acInterrupt_Enable.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        nvicDep.append("COMP" + str(comparatorID) + "INTERRUPT_ENABLE")

        #Single-shot Mode
        acSym_COMPCTRL_SINGLE = acComponent.createBooleanSymbol("AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_SINGLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_SINGLE.setLabel("Enable Single Shot Mode")
        acSym_COMPCTRL_SINGLE.setDefaultValue(False)
        acSym_COMPCTRL_SINGLE.setVisible(False)
        acSym_COMPCTRL_SINGLE.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #MUXPOS
        acSym_COMPCTRL_MUXPOS.append(comparatorID)
        acSym_COMPCTRL_MUXPOS[comparatorID] = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_MUX_POS", acSym_Enable[comparatorID])
        acSym_COMPCTRL_MUXPOS[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_MUXPOS[comparatorID].setLabel("Positive Input Mux Selection")
        acSym_COMPCTRL_MUXPOS[comparatorID].setVisible(False)

        acSym_COMPCTRL_MUXPOS_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__MUXPOS\"]")
        acSym_COMPCTRL_MUXPOS_Node_Values = []
        acSym_COMPCTRL_MUXPOS_Node_Values = acSym_COMPCTRL_MUXPOS_Node.getChildren()

        acSym_COMPCTRL_MUXPOS_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_MUXPOS_Node_Values)):
            acSym_COMPCTRL_MUXPOS_Key_Name = acSym_COMPCTRL_MUXPOS_Node_Values[id].getAttribute("name")
            if(acSym_COMPCTRL_MUXPOS_Key_Name == "PIN0"):
                acSym_COMPCTRL_MUXPOS_Default_Val = id
            acSym_COMPCTRL_MUXPOS_Key_Description = acSym_COMPCTRL_MUXPOS_Node_Values[id].getAttribute("caption")
            acSym_COMPCTRL_MUXPOS_Key_Value = acSym_COMPCTRL_MUXPOS_Node_Values[id].getAttribute("value")
            acSym_COMPCTRL_MUXPOS[comparatorID].addKey(acSym_COMPCTRL_MUXPOS_Key_Name, acSym_COMPCTRL_MUXPOS_Key_Value, acSym_COMPCTRL_MUXPOS_Key_Description)

        acSym_COMPCTRL_MUXPOS[comparatorID].setDefaultValue(acSym_COMPCTRL_MUXPOS_Default_Val)
        acSym_COMPCTRL_MUXPOS[comparatorID].setOutputMode("Key")
        acSym_COMPCTRL_MUXPOS[comparatorID].setDisplayMode("Description")
        acSym_COMPCTRL_MUXPOS[comparatorID].setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #MUXNEG
        acSym_COMPCTRL_MUXNEG.append(comparatorID)
        acSym_COMPCTRL_MUXNEG[comparatorID] = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_MUX_NEG", acSym_Enable[comparatorID])
        acSym_COMPCTRL_MUXNEG[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_MUXNEG[comparatorID].setLabel("Negative Input Mux Selection")
        acSym_COMPCTRL_MUXNEG[comparatorID].setVisible(False)

        acSym_COMPCTRL_MUXNEG_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__MUXNEG\"]")
        acSym_COMPCTRL_MUXNEG_Node_Values = []
        acSym_COMPCTRL_MUXNEG_Node_Values = acSym_COMPCTRL_MUXNEG_Node.getChildren()

        acSym_COMPCTRL_MUXNEG_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_MUXNEG_Node_Values)):
            acSym_COMPCTRL_MUXNEG_Key_Name = acSym_COMPCTRL_MUXNEG_Node_Values[id].getAttribute("name")
            if(acSym_COMPCTRL_MUXNEG_Key_Name == "GND"):
                acSym_COMPCTRL_MUXNEG_Default_Val = id
            acSym_COMPCTRL_MUXNEG_Key_Description = acSym_COMPCTRL_MUXNEG_Node_Values[id].getAttribute("caption")
            acSym_COMPCTRL_MUXNEG_Key_Value = acSym_COMPCTRL_MUXNEG_Node_Values[id].getAttribute("value")
            acSym_COMPCTRL_MUXNEG[comparatorID].addKey(acSym_COMPCTRL_MUXNEG_Key_Name, acSym_COMPCTRL_MUXNEG_Key_Value, acSym_COMPCTRL_MUXNEG_Key_Description)    
        
        acSym_COMPCTRL_MUXNEG[comparatorID].setDefaultValue(acSym_COMPCTRL_MUXNEG_Default_Val)
        acSym_COMPCTRL_MUXNEG[comparatorID].setOutputMode("Key")
        acSym_COMPCTRL_MUXNEG[comparatorID].setDisplayMode("Description")
        acSym_COMPCTRL_MUXNEG[comparatorID].setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        
        #Scaling factor for VDD scaler
        acSym_SCALERn.append(comparatorID)
        acSym_SCALERn[comparatorID] = acComponent.createIntegerSymbol("AC_SCALER_N_" + str(comparatorID), acSym_Enable[comparatorID])
        acSym_SCALERn[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:scalern0")
        acSym_SCALERn[comparatorID].setLabel("Scaling factor for VDD scaler")
        acSym_SCALERn[comparatorID].setMin(0)
        acSym_SCALERn[comparatorID].setMax(63)
        acSym_SCALERn[comparatorID].setDefaultValue(0)
        acSym_SCALERn[comparatorID].setVisible(False)
        #This should be enabled only when mux neg value is VDDSCALER
        acSym_SCALERn[comparatorID].setDependencies(setacScalerVisibility, ["AC" + str(comparatorID) + "_MUX_NEG", "AC" + str(comparatorID) + "_MUX_POS"])

        #Output Mode
        acSym_COMPCTRL_OUT = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_OUTPUT_TYPE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_OUT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_OUT.setLabel("Output Edge Type")
        acSym_COMPCTRL_OUT.setVisible(False)

        acSym_COMPCTRL_OUT_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__OUT\"]")
        acSym_COMPCTRL_OUT_Node_Values = []
        acSym_COMPCTRL_OUT_Node_Values = acSym_COMPCTRL_OUT_Node.getChildren()

        acSym_COMPCTRL_OUT_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_OUT_Node_Values)):
            acSym_COMPCTRL_OUT_Key_Name = acSym_COMPCTRL_OUT_Node_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_OUT_Key_Name == "ASYNC"):
                acSym_COMPCTRL_OUT_Default_Val = id

            acSym_COMPCTRL_OUT_Key_Description = acSym_COMPCTRL_OUT_Node_Values[id].getAttribute("caption")
            acSym_COMPCTRL_OUT_Key_Value = acSym_COMPCTRL_OUT_Node_Values[id].getAttribute("value")
            acSym_COMPCTRL_OUT.addKey(acSym_COMPCTRL_OUT_Key_Name, acSym_COMPCTRL_OUT_Key_Value, acSym_COMPCTRL_OUT_Key_Description)

        acSym_COMPCTRL_OUT.setDefaultValue(acSym_COMPCTRL_OUT_Default_Val)
        acSym_COMPCTRL_OUT.setOutputMode("Key")
        acSym_COMPCTRL_OUT.setDisplayMode("Description")
        acSym_COMPCTRL_OUT.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #ISEL
        acSym_COMPCTRL_ISEL = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_ISEL", acSym_Enable[comparatorID])
        acSym_COMPCTRL_ISEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_ISEL.setLabel("Interrupt Selection")
        acSym_COMPCTRL_ISEL.setVisible(False)

        acSym_COMPCTRL_ISEL_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__INTSEL\"]")
        acSym_COMPCTRL_ISEL_Node_Values = []
        acSym_COMPCTRL_ISEL_Node_Values = acSym_COMPCTRL_ISEL_Node.getChildren()

        acSym_COMPCTRL_ISEL_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_ISEL_Node_Values)):
            acSym_COMPCTRL_ISEL_Key_Name = acSym_COMPCTRL_ISEL_Node_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_ISEL_Key_Name == "TOGGLE"):
                acSym_COMPCTRL_ISEL_Default_Val = id

            acSym_COMPCTRL_ISEL_Key_Description = acSym_COMPCTRL_ISEL_Node_Values[id].getAttribute("caption")
            acSym_COMPCTRL_ISEL_Key_Value = acSym_COMPCTRL_ISEL_Node_Values[id].getAttribute("value")
            acSym_COMPCTRL_ISEL.addKey(acSym_COMPCTRL_ISEL_Key_Name, acSym_COMPCTRL_ISEL_Key_Value, acSym_COMPCTRL_ISEL_Key_Description)

        acSym_COMPCTRL_ISEL.setDefaultValue(acSym_COMPCTRL_ISEL_Default_Val)
        acSym_COMPCTRL_ISEL.setOutputMode("Key")
        acSym_COMPCTRL_ISEL.setDisplayMode("Description")
        acSym_COMPCTRL_ISEL.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #RUNSTDBY Enable
        acSym_COMPCTRL_RUNSTDBY = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_COMPCTRL_RUNSTDBY", acSym_Enable[comparatorID])
        acSym_COMPCTRL_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_RUNSTDBY.setLabel("Enable Run in Standby")
        acSym_COMPCTRL_RUNSTDBY.setDefaultValue(False)
        acSym_COMPCTRL_RUNSTDBY.setVisible(False)
        acSym_COMPCTRL_RUNSTDBY.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        
        #Menu item for advanced configurations
        acSym_AdvConf = acComponent.createMenuSymbol("AC_ADVANCED_CONFIGURATION_"+ str(comparatorID),  acSym_Enable[comparatorID])
        acSym_AdvConf.setLabel("Advanced Configurations")
        acSym_AdvConf.setVisible(False)
        acSym_AdvConf.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
    
        #Hysteresis Enable
        acSym_COMPCTRL_HYST = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_HYSTEN", acSym_AdvConf)
        acSym_COMPCTRL_HYST.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_HYST.setLabel("Hysteresis Enable")
        acSym_COMPCTRL_HYST.setDefaultValue(False)
        acSym_COMPCTRL_HYST.setVisible(True)
        #Should not be shown when single-shot is selected.
        acSym_COMPCTRL_HYST.setDependencies(setacHystVisibility,["AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE"])
 
        acSym_COMPCTRL_HYST_LEVEL_PRESENT = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_HYST_LVL_PRESENT", acSym_COMPCTRL_HYST)
        acSym_COMPCTRL_HYST_LEVEL_PRESENT.setVisible(False)
        acSym_COMPCTRL_HYST_LEVEL_PRESENT.setDefaultValue(False)
        ################################ ATDF ####################################################
        node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AC\"]/instance@[name=\"AC""\"]/parameters")
        parameters = []
        parameters = node.getChildren()
        for param in range (0, len(parameters)):
            if(parameters[param].getAttribute("name") == "HYST_LVL_CONFIG"):
                #Hysteresis level
                acSym_COMPCTRL_HYST_LEVEL_PRESENT.setDefaultValue(True)
                
                acSym_COMPCTRL_HYST_LEVEL = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_HYS_LVL", acSym_COMPCTRL_HYST)
                acSym_COMPCTRL_HYST_LEVEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
                acSym_COMPCTRL_HYST_LEVEL.setLabel("Hysteresis Level")
                
                ################################ ATDF ####################################################
                acSym_COMPCTRL_HYST_LEVEL_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__HYST\"]")
                acSym_COMPCTRL_HYST_Values = []
                acSym_COMPCTRL_HYST_Values = acSym_COMPCTRL_HYST_LEVEL_node.getChildren()       
                
                acSym_COMPCTRL_HYST_Default_Val = 0
                
                for id in range(len(acSym_COMPCTRL_HYST_Values)):
                    acSym_COMPCTRL_HYST_Key_Name = acSym_COMPCTRL_HYST_Values[id].getAttribute("name")

                    if(acSym_COMPCTRL_HYST_Key_Name == "HYST50"):
                        acSym_COMPCTRL_HYST_Default_Val = id       
                   
                    acSym_COMPCTRL_HYST_Key_Description = acSym_COMPCTRL_HYST_Values[id].getAttribute("caption")
                    acSym_COMPCTRL_HYST_Key_Value = acSym_COMPCTRL_HYST_Values[id].getAttribute("value")
                    acSym_COMPCTRL_HYST_LEVEL.addKey(acSym_COMPCTRL_HYST_Key_Name, acSym_COMPCTRL_HYST_Key_Value, acSym_COMPCTRL_HYST_Key_Description)        
                
                acSym_COMPCTRL_HYST_LEVEL.setDefaultValue(acSym_COMPCTRL_HYST_Default_Val)
                acSym_COMPCTRL_HYST_LEVEL.setOutputMode("Value")
                acSym_COMPCTRL_HYST_LEVEL.setDisplayMode("Description")
                acSym_COMPCTRL_HYST_LEVEL.setVisible(False)
                acSym_COMPCTRL_HYST_LEVEL.setDependencies(setacSymbolVisibility,["AC" + str(comparatorID) + "_HYSTEN"])
        
        #Speed selection
        acSym_COMPCTRL_SPEED = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_SPEED", acSym_AdvConf)
        acSym_COMPCTRL_SPEED.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_SPEED.setLabel("Speed Selection")
        acSym_COMPCTRL_SPEED.setVisible(False)
        
        acSym_COMPCTRL_SPEED_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__SPEED\"]")
        acSym_COMPCTRL_SPEED_Values = []
        acSym_COMPCTRL_SPEED_Values = acSym_COMPCTRL_SPEED_node.getChildren()

        acSym_COMPCTRL_SPEED_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_SPEED_Values)):
            acSym_COMPCTRL_SPEED_Key_Name = acSym_COMPCTRL_SPEED_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_SPEED_Key_Name == "LOW"):
                acSym_COMPCTRL_SPEED_Default_Val = id

            acSym_COMPCTRL_SPEED_Key_Description = acSym_COMPCTRL_SPEED_Values[id].getAttribute("caption")
            acSym_COMPCTRL_SPEED_Key_Value = acSym_COMPCTRL_SPEED_Values[id].getAttribute("value")
            acSym_COMPCTRL_SPEED.addKey(acSym_COMPCTRL_SPEED_Key_Name, acSym_COMPCTRL_SPEED_Key_Value, acSym_COMPCTRL_SPEED_Key_Description)

        acSym_COMPCTRL_SPEED.setDefaultValue(acSym_COMPCTRL_SPEED_Default_Val)
        acSym_COMPCTRL_SPEED.setOutputMode("Value")
        acSym_COMPCTRL_SPEED.setDisplayMode("Description")
        acSym_COMPCTRL_SPEED.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #Filter Length selection
        acSym_COMPCTRL_FLEN = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_FLEN_VAL", acSym_AdvConf)
        acSym_COMPCTRL_FLEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:COMPCTRL0")
        acSym_COMPCTRL_FLEN.setLabel("Filter Length Selection")
        acSym_COMPCTRL_FLEN.setDescription("Filtering must be disabled if continuous measurements will be done during sleep modes")
        acSym_COMPCTRL_FLEN_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__FLEN\"]")
        acSym_COMPCTRL_FLEN_Values = []
        acSym_COMPCTRL_FLEN_Values = acSym_COMPCTRL_FLEN_node.getChildren()

        acSym_COMPCTRL_FLEN_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_FLEN_Values)):
            acSym_COMPCTRL_FLEN_Key_Name = acSym_COMPCTRL_FLEN_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_FLEN_Key_Name == "OFF"):
                acSym_COMPCTRL_FLEN_Default_Val = id

            acSym_COMPCTRL_FLEN_Key_Description = acSym_COMPCTRL_FLEN_Values[id].getAttribute("caption")
            acSym_COMPCTRL_FLEN_Key_Value = acSym_COMPCTRL_FLEN_Values[id].getAttribute("value")
            acSym_COMPCTRL_FLEN.addKey(acSym_COMPCTRL_FLEN_Key_Name, acSym_COMPCTRL_FLEN_Key_Value, acSym_COMPCTRL_FLEN_Key_Description)

        acSym_COMPCTRL_FLEN.setDefaultValue(acSym_COMPCTRL_FLEN_Default_Val)
        acSym_COMPCTRL_FLEN.setOutputMode("Key")
        acSym_COMPCTRL_FLEN.setDisplayMode("Description")

        #Event Input Enable
        acSym_EVCTRL_COMPEI = acComponent.createBooleanSymbol("AC_EVCTRL_COMPEI" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEI.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:EVCTRL")
        acSym_EVCTRL_COMPEI.setLabel("Enable Event Input")
        acSym_EVCTRL_COMPEI.setDefaultValue(False)
        acSym_EVCTRL_COMPEI.setVisible(False)
        acSym_EVCTRL_COMPEI.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        evsysDep.append("AC_EVCTRL_COMPEI" + str(comparatorID))
        
        #Event Output Enable
        acSym_EVCTRL_COMPEO = acComponent.createBooleanSymbol("AC_EVCTRL_COMPEO" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:EVCTRL")
        acSym_EVCTRL_COMPEO.setLabel("Enable Event Output")
        acSym_EVCTRL_COMPEO.setDefaultValue(False)
        acSym_EVCTRL_COMPEO.setVisible(False)
        acSym_EVCTRL_COMPEO.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        evsysDep.append("AC_EVCTRL_COMPEO" + str(comparatorID))
    
    node1 = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AC\"]/instance@[name=\"AC""\"]/parameters")
    numOfWindowMonitors = 0
    parameters1 = []
    parameters1 = node1.getChildren()
    for param in range (0, len(parameters1)):
        if(parameters[param].getAttribute("name") == "PAIRS"):
            numOfWindowMonitors = int(parameters[param].getAttribute("value"))
    
    #Menu item for window configurations
    acSym_WindowConf = acComponent.createMenuSymbol("WINDOW_CONFIGURATION", None)
    acSym_WindowConf.setLabel("Comparator Window Configurations")
    
    acSym_WINCTRL = []
    acSym_INTENSET_WIN = []
    acSym_WNCTRL_WINT = []
    acSym_WINCTRL_EVENT_OUT = []
    acSym_WNCTRL_WINT_node = []
    
    for num in range (0, numOfWindowMonitors):

        #Window 0 configuration
        acSym_WINCTRL.append(num)
        acSym_WINCTRL[num] = acComponent.createBooleanSymbol("AC_WINCTRL_WIN"+str(num), acSym_WindowConf)
        acSym_WINCTRL[num].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:WINCTRL")
        acSym_WINCTRL[num].setLabel("Window "+ str(num) +" Enable")
        acSym_WINCTRL[num].setDefaultValue(False)
        
        #Window 0 Interrupt Enable
        acSym_INTENSET_WIN.append(num)
        acSym_INTENSET_WIN[num] = acComponent.createBooleanSymbol("AC_INTENSET_WIN"+str(num), acSym_WINCTRL[num])
        acSym_INTENSET_WIN[num].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:INTENSET")
        acSym_INTENSET_WIN[num].setLabel("Window Interrupt Enable")
        acSym_INTENSET_WIN[num].setDefaultValue(False)
        acSym_INTENSET_WIN[num].setVisible(False)
        acSym_INTENSET_WIN[num].setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN"+str(num)])
        nvicDep.append("AC_INTENSET_WIN"+str(num))
        
        #Window 0 interrupt configuration
        acSym_WNCTRL_WINT.append(num)
        acSym_WNCTRL_WINT[num] = acComponent.createKeyValueSetSymbol("AC_WINTSEL"+str(num), acSym_WINCTRL[num])
        acSym_WNCTRL_WINT[num].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:winctrl")
        acSym_WNCTRL_WINT[num].setLabel("AC Window Interrupt Selection")

        acSym_WNCTRL_WINT_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_WINCTRL__WINTSEL0\"]")
        acSym_WNCTRL_WINT_Values = []
        acSym_WNCTRL_WINT_Values = acSym_WNCTRL_WINT_node.getChildren()
        acSym_WNCTRL_WINT0_Default_Val = 0

        for id in range(len(acSym_WNCTRL_WINT_Values)):
            acSym_WNCTRL_WINT0_Key_Name = acSym_WNCTRL_WINT_Values[id].getAttribute("name")

            if(acSym_WNCTRL_WINT0_Key_Name == "ABOVE"):
                acSym_WNCTRL_WINT0_Default_Val = id

            acSym_WNCTRL_WINT0_Key_Description = acSym_WNCTRL_WINT_Values[id].getAttribute("caption")
            acSym_WNCTRL_WINT0_Key_Value = acSym_WNCTRL_WINT_Values[id].getAttribute("value")
            acSym_WNCTRL_WINT[num].addKey(acSym_WNCTRL_WINT0_Key_Name, acSym_WNCTRL_WINT0_Key_Value, acSym_WNCTRL_WINT0_Key_Description)

        acSym_WNCTRL_WINT[num].setDefaultValue(acSym_WNCTRL_WINT0_Default_Val)
        acSym_WNCTRL_WINT[num].setOutputMode("Value")
        acSym_WNCTRL_WINT[num].setDisplayMode("Description")
        acSym_WNCTRL_WINT[num].setVisible(False)
        acSym_WNCTRL_WINT[num].setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN"+str(num)])
        
        #Window 0 Event Output
        acSym_WINCTRL_EVENT_OUT.append(num)
        acSym_WINCTRL_EVENT_OUT[num] = acComponent.createBooleanSymbol("AC_EVCTRL_WINEO"+str(num), acSym_WINCTRL[num])
        acSym_WINCTRL_EVENT_OUT[num].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2245;register:EVCTRL")
        acSym_WINCTRL_EVENT_OUT[num].setLabel("Enable Window Event Output")
        acSym_WINCTRL_EVENT_OUT[num].setDefaultValue(False)
        acSym_WINCTRL_EVENT_OUT[num].setVisible(False)
        acSym_WINCTRL_EVENT_OUT[num].setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN"+str(num)])
        evsysDep.append("AC_EVCTRL_WINEO"+str(num))        
    
    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = acInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = acInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = acInstanceName.getValue()+ "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = acInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    nvicDep.append("core." + InterruptVectorUpdate)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        InterruptVectorSecurity = acInstanceName.getValue() + "_SET_NON_SECURE"

    # Interrupt Dynamic settings
    acSym_UpdateInterruptStatus = acComponent.createBooleanSymbol("AC_INTERRUPT_STATUS", None)
    acSym_UpdateInterruptStatus.setDependencies(updateACInterruptStatus, nvicDep)
    acSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    acSym_IntEnComment = acComponent.createCommentSymbol("AC_INTERRUPT_ENABLE_COMMENT", None)
    acSym_IntEnComment.setVisible(False)
    acSym_IntEnComment.setLabel("Warning!!! "+acInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    acSym_IntEnComment.setDependencies(updateACInterruptWarningStatus, nvicDep)

    # Clock Warning status
    acSym_ClkEnComment = acComponent.createCommentSymbol("AC_CLOCK_ENABLE_COMMENT", None)
    acSym_ClkEnComment.setVisible(False)
    acSym_ClkEnComment.setLabel("Warning!!! " +acInstanceName.getValue()+" Clock is Disabled in Clock Manager")
    acSym_ClkEnComment.setDependencies(updateACClockWarningStatus, ["core." + acInstanceName.getValue() + "_CLOCK_ENABLE"])
    

    acSym_EVESYS_CONFIGURE = acComponent.createIntegerSymbol("AC_EVESYS_CONFIGURE", None)
    acSym_EVESYS_CONFIGURE.setVisible(False)
    acSym_EVESYS_CONFIGURE.setDependencies(acEvesysConfigure, evsysDep)    
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global ACfilesArray
        acIsNonSecure = Database.getSymbolValue("core", acComponent.getID().upper() + "_IS_NON_SECURE")
        Database.setSymbolValue("core", InterruptVectorSecurity, acIsNonSecure)

    acHeader1File = acComponent.createFileSymbol("AC_HEADER", None)
    acHeader1File.setSourcePath("../peripheral/ac_u2245/templates/plib_ac.h.ftl")
    acHeader1File.setOutputName("plib_" + acInstanceName.getValue().lower() + ".h")
    acHeader1File.setMarkup(True)
    acHeader1File.setDestPath("/peripheral/ac/")
    acHeader1File.setProjectPath("config/" + configName + "/peripheral/ac/")
    acHeader1File.setType("HEADER")
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ACfilesArray.append(acHeader1File)
        if acIsNonSecure == False:
            acHeader1File.setSecurity("SECURE")

    acSource1File = acComponent.createFileSymbol("AC_SOURCE", None)
    acSource1File.setSourcePath("../peripheral/ac_u2245/templates/plib_ac.c.ftl")
    acSource1File.setOutputName("plib_" + acInstanceName.getValue().lower() + ".c")
    acSource1File.setMarkup(True)
    acSource1File.setDestPath("/peripheral/ac/")
    acSource1File.setProjectPath("config/" + configName + "/peripheral/ac/")
    acSource1File.setType("SOURCE")
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ACfilesArray.append(acSource1File)
        if acIsNonSecure == False:
            acSource1File.setSecurity("SECURE")

    acSystemInitFile = acComponent.createFileSymbol("AC_SYS_INIT", None)
    acSystemInitFile.setType("STRING")
    acSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    acSystemInitFile.setSourcePath("../peripheral/ac_u2245/templates/system/initialization.c.ftl")
    acSystemInitFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ACfilesArray.append(acSystemInitFile)
        if acIsNonSecure == False:
            acSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")

    acSystemDefFile = acComponent.createFileSymbol("AC_SYS_DEF", None)
    acSystemDefFile.setType("STRING")
    acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    acSystemDefFile.setSourcePath("../peripheral/ac_u2245/templates/system/definitions.h.ftl")
    acSystemDefFile.setMarkup(True)
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ACfilesArray.append(acSystemDefFile)
        acSystemDefFile.setDependencies(fileUpdate, ["core." + acComponent.getID().upper() + "_IS_NON_SECURE"])
        if acIsNonSecure == False:
            acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
            