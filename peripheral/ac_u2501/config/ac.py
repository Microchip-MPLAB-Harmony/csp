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
#########################################    Global Variables ----START       #########################################################
global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global acInstanceName
global acSym_SCALERn

#######################################################################################################################################
#####################################        Callback Funtions ----START      #########################################################
#######################################################################################################################################

#Control VDD Scaler value visibility
def setacScalerVisibility(MySymbol, event):
    dep_symbol = event["symbol"].getID()
    mux_type = (dep_symbol.split('_', 2))
    if (((event["value"] == 5) and (mux_type[1] == "MUXNEG")) or ((event["value"] == 4) and (mux_type[1] == "MUXPOS"))):
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

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)

    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    if event["value"] == True:

        Database.setSymbolValue("core", InterruptHandler, acInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, acInstanceName.getValue() + "_Handler", 2)

def updateACInterruptWarningStatus(symbol, event):

    if acSym_UpdateInterruptStatus.getValue() == True:
        symbol.setVisible(event["value"])

def updateACClockWarningStatus(symbol, event):

    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        
#######################################################################################################################################
#####################################        Callback Funtions ---- END      ##########################################################
#######################################################################################################################################

#######################################################################################################################################
#####################################               Component                ##########################################################
#######################################################################################################################################

def instantiateComponent(acComponent):

    global acInstanceName
    global acSym_Enable
    global acSym_UpdateInterruptStatus
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    
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
    
    #Populate menu for all comparators in the AC peripheral
    for comparatorID in range(0, int(numOfComparators)):
        acSym_Enable.append(comparatorID)

        acSym_Enable[comparatorID] = acComponent.createBooleanSymbol("ANALOG_COMPARATOR_ENABLE_" + str(comparatorID), None)
        acSym_Enable[comparatorID].setLabel("Comparator " + str(comparatorID) + " Settings")

        #Interrupt Enable
        global acInterrupt_Enable
        acInterrupt_Enable = acComponent.createBooleanSymbol("COMP" + str(comparatorID) + "INTERRUPT_ENABLE", acSym_Enable[comparatorID])
        acInterrupt_Enable.setLabel("Comparator Interrupt Enable")
        acInterrupt_Enable.setVisible(False)
        acInterrupt_Enable.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #Single-shot Mode
        acSym_COMPCTRL_SINGLE = acComponent.createBooleanSymbol("AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_SINGLE.setLabel("Enable Single Shot Mode")
        acSym_COMPCTRL_SINGLE.setDefaultValue(False)
        acSym_COMPCTRL_SINGLE.setVisible(False)
        acSym_COMPCTRL_SINGLE.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #MUXPOS
        acSym_COMPCTRL_MUXPOS = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_MUXPOS", acSym_Enable[comparatorID])
        acSym_COMPCTRL_MUXPOS.setLabel("Positive Input Mux Selection")
        acSym_COMPCTRL_MUXPOS.setVisible(False)

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
            acSym_COMPCTRL_MUXPOS.addKey(acSym_COMPCTRL_MUXPOS_Key_Name, acSym_COMPCTRL_MUXPOS_Key_Value, acSym_COMPCTRL_MUXPOS_Key_Description)

        acSym_COMPCTRL_MUXPOS.setDefaultValue(acSym_COMPCTRL_MUXPOS_Default_Val)
        acSym_COMPCTRL_MUXPOS.setOutputMode("Key")
        acSym_COMPCTRL_MUXPOS.setDisplayMode("Description")
        acSym_COMPCTRL_MUXPOS.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #MUXNEG
        global acSym_COMPCTRL_MUXNEG
        acSym_COMPCTRL_MUXNEG = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_MUXNEG", acSym_Enable[comparatorID])
        acSym_COMPCTRL_MUXNEG.setLabel("Negative Input Mux Selection")
        acSym_COMPCTRL_MUXNEG.setVisible(False)

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
            acSym_COMPCTRL_MUXNEG.addKey(acSym_COMPCTRL_MUXNEG_Key_Name, acSym_COMPCTRL_MUXNEG_Key_Value, acSym_COMPCTRL_MUXNEG_Key_Description)
        
        
        acSym_COMPCTRL_MUXNEG.setDefaultValue(acSym_COMPCTRL_MUXNEG_Default_Val)
        acSym_COMPCTRL_MUXNEG.setOutputMode("Key")
        acSym_COMPCTRL_MUXNEG.setDisplayMode("Description")
        acSym_COMPCTRL_MUXNEG.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        
        #Scaling factor for VDD scaler
        acSym_SCALERn.append(comparatorID)
        acSym_SCALERn[comparatorID] = acComponent.createIntegerSymbol("AC_SCALER_N_" + str(comparatorID), acSym_Enable[comparatorID])
        acSym_SCALERn[comparatorID].setLabel("Scaling factor for VDD scaler")
        acSym_SCALERn[comparatorID].setMin(0)
        acSym_SCALERn[comparatorID].setMax(63)
        acSym_SCALERn[comparatorID].setDefaultValue(0)
        acSym_SCALERn[comparatorID].setVisible(False)
        #This should be enabled only when mux pos or mux neg value is VDDSCALER
        acSym_SCALERn[comparatorID].setDependencies(setacScalerVisibility, ["AC" + str(comparatorID) + "_MUXNEG", "AC" + str(comparatorID) + "_MUXPOS"])

        #Output Mode
        acSym_COMPCTRL_OUT = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_OUTPUT_TYPE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_OUT.setLabel("Output Edge Type")
        acSym_COMPCTRL_OUT.setVisible(False)

        acSym_COMPCTRL_OUT_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__OUT\"]")
        acSym_COMPCTRL_OUT_Node_Values = []
        acSym_COMPCTRL_OUT_Node_Values = acSym_COMPCTRL_OUT_Node.getChildren()

        acSym_COMPCTRL_OUT_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_OUT_Node_Values)):
            acSym_COMPCTRL_OUT_Key_Name = acSym_COMPCTRL_OUT_Node_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_OUT_Key_Name == "OFF"):
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
        acSym_COMPCTRL_HYSTEN = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_HYSTEN", acSym_AdvConf)
        acSym_COMPCTRL_HYSTEN.setLabel("Hysteresis Enable")
        acSym_COMPCTRL_HYSTEN.setDefaultValue(False)
        acSym_COMPCTRL_HYSTEN.setVisible(True)
        #Should not be shown when single-shot is selected.
        acSym_COMPCTRL_HYSTEN.setDependencies(setacHystVisibility,["AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE"])
        
        #Hysteresis selection
        acSym_COMPCTRL_HYST = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_HYST_VAL", acSym_COMPCTRL_HYSTEN)
        acSym_COMPCTRL_HYST.setLabel("Hysteresis Selection")
        acSym_COMPCTRL_HYST.setVisible(False)
        acSym_COMPCTRL_HYST_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_COMPCTRL__HYST\"]")
        acSym_COMPCTRL_HYST_Values = []
        acSym_COMPCTRL_HYST_Values = acSym_COMPCTRL_HYST_node.getChildren()

        acSym_COMPCTRL_HYST_Default_Val = 0

        for id in range(len(acSym_COMPCTRL_HYST_Values)):
            acSym_COMPCTRL_HYST_Key_Name = acSym_COMPCTRL_HYST_Values[id].getAttribute("name")

            if(acSym_COMPCTRL_HYST_Key_Name == "HYST50"):
                acSym_COMPCTRL_HYST_Default_Val = id

            acSym_COMPCTRL_HYST_Key_Description = acSym_COMPCTRL_HYST_Values[id].getAttribute("caption")
            acSym_COMPCTRL_HYST_Key_Value = acSym_COMPCTRL_HYST_Values[id].getAttribute("value")
            acSym_COMPCTRL_HYST.addKey(acSym_COMPCTRL_HYST_Key_Name, acSym_COMPCTRL_HYST_Key_Value, acSym_COMPCTRL_HYST_Key_Description)

        acSym_COMPCTRL_HYST.setDefaultValue(acSym_COMPCTRL_HYST_Default_Val)
        acSym_COMPCTRL_HYST.setOutputMode("Value")
        acSym_COMPCTRL_HYST.setDisplayMode("Description")
        acSym_COMPCTRL_HYST.setDependencies(setacSymbolVisibility,["AC" + str(comparatorID) + "_HYSTEN"])
        
        #Filter Length selection
        acSym_COMPCTRL_FLEN = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_FLEN_VAL", acSym_AdvConf)
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
        acSym_COMPCTRL_FLEN.setOutputMode("Value")
        acSym_COMPCTRL_FLEN.setDisplayMode("Description")
        
        #Event Input Enable
        acSym_EVCTRL_COMPEI = acComponent.createKeyValueSetSymbol("AC_EVCTRL_COMPEI" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEI.setLabel("Enable Event Input")
        acSym_EVCTRL_COMPEI.setVisible(False)
        acSym_EVCTRL_COMPEI.setOutputMode("Value")
        acSym_EVCTRL_COMPEI.setDisplayMode("Description")
        acSym_EVCTRL_COMPEI.addKey("DISABLED", "0", "Disabled")
        acSym_EVCTRL_COMPEI.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
        acSym_EVCTRL_COMPEI.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
        acSym_EVCTRL_COMPEI.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
    
        #Event Output Enable
        acSym_EVCTRL_COMPEO = acComponent.createBooleanSymbol("AC_EVCTRL_COMPEO" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEO.setLabel("Enable Event Output")
        acSym_EVCTRL_COMPEO.setDefaultValue(False)
        acSym_EVCTRL_COMPEO.setVisible(False)
        acSym_EVCTRL_COMPEO.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
    
    #Menu item for window configurations
    acSym_WindowConf = acComponent.createMenuSymbol("WINDOW_CONFIGURATION", None)
    acSym_WindowConf.setLabel("Comparator Window Configurations")
    
    #Window 0 configuration
    acSym_WINCTRL0 = acComponent.createBooleanSymbol("AC_WINCTRL_WIN0", acSym_WindowConf)
    acSym_WINCTRL0.setLabel("Window 0 Enable")
    acSym_WINCTRL0.setDefaultValue(False)
    
    #Window 0 Interrupt Enable
    acSym_INTENSET_WIN0 = acComponent.createBooleanSymbol("AC_INTENSET_WIN0", acSym_WINCTRL0)
    acSym_INTENSET_WIN0.setLabel("Window 0 Interrupt Enable")
    acSym_INTENSET_WIN0.setDefaultValue(False)
    acSym_INTENSET_WIN0.setVisible(False)
    acSym_INTENSET_WIN0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])
    
    #Window 0 interrupt configuration
    acSym_WNCTRL_WINT0 = acComponent.createKeyValueSetSymbol("AC_WINTSEL0", acSym_WINCTRL0)
    acSym_WNCTRL_WINT0.setLabel("AC Window 0 Interrupt Selection")
    acSym_WNCTRL_WINT0.setVisible(False)
    acSym_WNCTRL_WINT0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])
    
    acSym_WNCTRL_WINT0_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/value-group@[name=\"AC_WINCTRL__WINTSEL0\"]")
    acSym_WNCTRL_WINT0_Values = []
    acSym_WNCTRL_WINT0_Values = acSym_WNCTRL_WINT0_node.getChildren()
    
    acSym_WNCTRL_WINT0_Default_Val = 0

    for id in range(len(acSym_WNCTRL_WINT0_Values)):
        acSym_WNCTRL_WINT0_Key_Name = acSym_WNCTRL_WINT0_Values[id].getAttribute("name")

        if(acSym_WNCTRL_WINT0_Key_Name == "ABOVE"):
            acSym_WNCTRL_WINT0_Default_Val = id

        acSym_WNCTRL_WINT0_Key_Description = acSym_WNCTRL_WINT0_Values[id].getAttribute("caption")
        acSym_WNCTRL_WINT0_Key_Value = acSym_WNCTRL_WINT0_Values[id].getAttribute("value")
        acSym_WNCTRL_WINT0.addKey(acSym_WNCTRL_WINT0_Key_Name, acSym_WNCTRL_WINT0_Key_Value, acSym_WNCTRL_WINT0_Key_Description)

    acSym_WNCTRL_WINT0.setDefaultValue(acSym_WNCTRL_WINT0_Default_Val)
    acSym_WNCTRL_WINT0.setOutputMode("Value")
    acSym_WNCTRL_WINT0.setDisplayMode("Description")
    
    #Window 0 Event Output
    acSym_WINCTRL_EVENT_OUT0 = acComponent.createBooleanSymbol("AC_EVCTRL_WINEO0", acSym_WINCTRL0)
    acSym_WINCTRL_EVENT_OUT0.setLabel("Enable Window 0 Event Output")
    acSym_WINCTRL_EVENT_OUT0.setDefaultValue(False)
    acSym_WINCTRL_EVENT_OUT0.setVisible(False)
    acSym_WINCTRL_EVENT_OUT0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])
    
    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = acInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = acInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = acInstanceName.getValue()+ "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = acInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    acSym_UpdateInterruptStatus = acComponent.createBooleanSymbol("AC_INTERRUPT_STATUS", None)
    acSym_UpdateInterruptStatus.setDependencies(updateACInterruptStatus, ["COMP0INTERRUPT_ENABLE", "COMP1INTERRUPT_ENABLE", "COMP2INTERRUPT_ENABLE", "COMP3INTERRUPT_ENABLE", "AC_INTENSET_WIN0"])
    acSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    acSym_IntEnComment = acComponent.createCommentSymbol("AC_INTERRUPT_ENABLE_COMMENT", None)
    acSym_IntEnComment.setVisible(False)
    acSym_IntEnComment.setLabel("Warning!!! "+acInstanceName.getValue()+" Interrupt is Disabled in Interrupt Manager")
    acSym_IntEnComment.setDependencies(updateACInterruptWarningStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    acSym_ClkEnComment = acComponent.createCommentSymbol("AC_CLOCK_ENABLE_COMMENT", None)
    acSym_ClkEnComment.setVisible(False)
    acSym_ClkEnComment.setLabel("Warning!!! " +acInstanceName.getValue()+" Clock is Disabled in Clock Manager")
    acSym_ClkEnComment.setDependencies(updateACClockWarningStatus, ["core." + acInstanceName.getValue() + "_CLOCK_ENABLE"])
    
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    acHeader1File = acComponent.createFileSymbol("AC_HEADER", None)
    acHeader1File.setSourcePath("../peripheral/ac_u2501/templates/plib_ac.h.ftl")
    acHeader1File.setOutputName("plib_" + acInstanceName.getValue().lower() + ".h")
    acHeader1File.setMarkup(True)
    acHeader1File.setDestPath("/peripheral/ac/")
    acHeader1File.setProjectPath("config/" + configName + "/peripheral/ac/")
    acHeader1File.setType("HEADER")

    acSource1File = acComponent.createFileSymbol("AC_SOURCE", None)
    acSource1File.setSourcePath("../peripheral/ac_u2501/templates/plib_ac.c.ftl")
    acSource1File.setOutputName("plib_" + acInstanceName.getValue().lower() + ".c")
    acSource1File.setMarkup(True)
    acSource1File.setDestPath("/peripheral/ac/")
    acSource1File.setProjectPath("config/" + configName + "/peripheral/ac/")
    acSource1File.setType("SOURCE")

    acSystemInitFile = acComponent.createFileSymbol("AC_SYS_INIT", None)
    acSystemInitFile.setType("STRING")
    acSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    acSystemInitFile.setSourcePath("../peripheral/ac_u2501/templates/system/initialization.c.ftl")
    acSystemInitFile.setMarkup(True)

    acSystemDefFile = acComponent.createFileSymbol("AC_SYS_DEF", None)
    acSystemDefFile.setType("STRING")
    acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    acSystemDefFile.setSourcePath("../peripheral/ac_u2501/templates/system/definitions.h.ftl")
    acSystemDefFile.setMarkup(True)

