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
global ACfilesArray
ACfilesArray = []
global evsys_generatorsNamesList
evsys_generatorsNamesList = []
global evsys_usersNamesList
evsys_usersNamesList = []

def acEvsysGeneratorNamesPopulate(instanceName):
    global evsys_generatorsNamesList

    generatorNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators")
    generatorValues = generatorNode.getChildren()
    for id in range(0, len(generatorNode.getChildren())):
        if generatorValues[id].getAttribute("module-instance") == instanceName:
            evsys_generatorsNamesList.append(generatorValues[id].getAttribute("name"))

def acEvsysUserNamesPopulate(instanceName):
    global evsys_usersNamesList

    usersNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/users")
    usersValues = usersNode.getChildren()
    for id in range(0, len(usersNode.getChildren())):
        if usersValues[id].getAttribute("module-instance") == instanceName:
            evsys_usersNamesList.append(usersValues[id].getAttribute("name"))

def acEvsysGenNameGet(genNameMatchList):
    global evsys_generatorsNamesList

    for genName in evsys_generatorsNamesList:
        if all ( x in genName for x in genNameMatchList):
            return genName

def acEvsysUserNameGet(usrNameMatchList):
    global evsys_usersNamesList

    for userName in evsys_usersNamesList:
        if all ( x in userName for x in usrNameMatchList):
            return userName

def getValueGrp(module, reg_grp, reg_name, bitfield_name , mode = None):
    node_str = ""
    val_grp_node = None

    if mode != None:
        node_str = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[modes=\"{2}\",name=\"{3}\"]/bitfield@[name=\"{4}\"]".format(module, reg_grp, mode, reg_name, bitfield_name)
    else:
         node_str = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[name=\"{2}\"]/bitfield@[name=\"{3}\"]".format(module, reg_grp, reg_name, bitfield_name)
    bitfield_node = ATDF.getNode(node_str)

    if bitfield_node != None:
        val_grp = bitfield_node.getAttribute("values")
        node_str = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/value-group@[name=\"{1}\"]".format(module, val_grp)
        val_grp_node = ATDF.getNode(node_str)

    return val_grp_node
#######################################################################################################################################
#####################################        Callback Funtions ----START      #########################################################
#######################################################################################################################################
# Trustzone secure/non-secure file generation logic
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

def updateDACOutputVol(symbol, event):
    if "DACCTRL_VALUE" in event["id"]:
        dac_out_val = event["value"]
        dac_out_vol = ((3.3) * (dac_out_val))/128

        dac_out_vol_str = "{:.2f}".format(dac_out_vol)

        symbol.setLabel("[With VDD = 3.3V, DAC Output = " + str(dac_out_vol_str) + "V]")
    else:
        comparator_enabled = event["value"]
        symbol.setVisible(comparator_enabled == True)

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
        evsysGenName = acEvsysGenNameGet(["COMP", str(instance)])
        Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", event["value"], 2)

    if("AC_EVCTRL_WINEO" in event["id"]):
        instance = filter(str.isdigit,str(event["id"]))
        evsysGenName = acEvsysGenNameGet(["WIN", str(instance)])
        Database.setSymbolValue("evsys", "GENERATOR_" + evsysGenName + "_ACTIVE", event["value"], 2)

    if ("AC_EVCTRL_COMPEI" in event["id"]):
        instance = filter(str.isdigit,str(event["id"]))
        evsysUserName = acEvsysUserNameGet(["SOC", str(instance)])
        if (event["value"] > 0):
            Database.setSymbolValue("evsys", "USER_" + evsysUserName + "_READY", True, 2)
        else:
             Database.setSymbolValue("evsys", "USER_" + evsysUserName + "_READY", False, 2)

def handleMessage(messageID, args):
    retDict = {}
    if (messageID == "AC_CONFIG_HW_IO"):
        component = 'ac'
        comparatorID, muxInput, ioPin = args['config']
        symbolId = "AC{}_{}".format(comparatorID, muxInput)
        enable = args['enable']
        if enable == True:
            Database.setSymbolValue(component, "ANALOG_COMPARATOR_ENABLE_" + str(comparatorID), enable)
            if ioPin == -1:
                res = Database.clearSymbolValue(component, symbolId)
            else:
                res = Database.setSymbolValue(component, symbolId, int(ioPin))

        else:
            res = Database.clearSymbolValue(component, symbolId)
            
        if res == True:
            retDict = {"Result": "Success"}
        else:
            retDict = {"Result": "Fail"}
            
    else:
        retDict= {"Result": "AC UnImplemented Command"}
    
    return retDict

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
    global InterruptVectorSecurity
    evsysDep = []
    global nvicDep
    nvicDep = []

    acInstanceName = acComponent.createStringSymbol("AC_INSTANCE_NAME", None)
    acInstanceName.setVisible(False)
    acInstanceName.setDefaultValue(acComponent.getID().upper())

    acEvsysGeneratorNamesPopulate(acInstanceName.getValue())
    acEvsysUserNamesPopulate(acInstanceName.getValue())

    acSym_ChannelGroup = acComponent.createStringSymbol("AC_CHANNEL_GROUP", None)
    if ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"CHANNEL\"]") != None:
        acSym_ChannelGroup.setDefaultValue("CHANNEL")
    elif ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"AC\"]") != None:
        acSym_ChannelGroup.setDefaultValue("AC")
    acSym_ChannelGroup.setVisible(False)

    acSym_Enable = []
    acSym_SCALERn = []
    acSym_COMP_NUM = []
    calibBaseAddr = ""
    #Clock enable
    Database.setSymbolValue("core", acInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    ################################ ATDF ####################################################
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"AC\"]/instance@[name=\"AC""\"]/parameters")
    numOfComparators = 0
    calibRequired = -1
    channelID = -1
    cmpPresent = []   # to check which comparator id is present on the device
    parameters = []
    parameters = node.getChildren()
    for param in range (0, len(parameters)):
        if("NUM_CMP" in parameters[param].getAttribute("name")):
            numOfComparators = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "LOAD_CALIB"):
            calibRequired = int(parameters[param].getAttribute("value"))

    # If LOAD_CALIB parameter is not present, it is assumed that CALIB register update is required to maintain backward compatibility
    if calibRequired == -1:
        calibRequired = 1

    # If calibration is required then read the calibration data address
    if calibRequired == 1:
        calibBaseAddr = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"SW0\"]").getAttribute("start")

    acCalibAddr = acComponent.createStringSymbol("AC_CALIB_ADDR", None)
    acCalibAddr.setDefaultValue(calibBaseAddr)
    acCalibAddr.setVisible(False)

    #Find which comparator channel is present if there is only one comparator
    if (numOfComparators == 1):
        for param in range (0, len(parameters)):
            if("CMP_CHID_PRESENT" in parameters[param].getAttribute("name")):
                if (int(parameters[param].getAttribute("value")) >= numOfComparators):
                    numOfComparators = int(parameters[param].getAttribute("value")) + 1
                    channelID = int(parameters[param].getAttribute("value"))

    # update cmpPresent array with which channels are available
    for cmp in range (0, numOfComparators):
        cmpPresent.append(cmp)
        if channelID == -1:
            cmpPresent[cmp] = 1   #by default, all comparator channels are present.
        else:
            if cmp == channelID:
                cmpPresent[cmp] = 1


    ctrlc_reg_present = False
    acSym_CTRLC_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"AC\"]/register@[name=\"CTRLC\"]")
    if acSym_CTRLC_Node != None:
        ctrlc_reg_present = True

    dacctrl_reg_present = False
    acSym_DACCTRL_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"{0}\"]/register@[name=\"DACCTRL\"]".format(acSym_ChannelGroup.getValue()))
    if acSym_CTRLC_Node != None:
        dacctrl_reg_present = True

    compctrl_sut_bitfield_present = False
    acSym_COMPCTRL_SUT_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"{0}\"]/register@[name=\"COMPCTRL\"]/bitfield@[name=\"SUT\"]".format(acSym_ChannelGroup.getValue()))
    if acSym_COMPCTRL_SUT_Node != None:
        compctrl_sut_bitfield_present = True

    acSym_NUM_CHANNELS = acComponent.createIntegerSymbol("AC_NUM_COMPARATORS", None)
    acSym_NUM_CHANNELS.setDefaultValue(int(numOfComparators))
    acSym_NUM_CHANNELS.setVisible(False)

    acSym_LOAD_CALIB = acComponent.createIntegerSymbol("AC_LOAD_CALIB", None)
    acSym_LOAD_CALIB.setVisible(False)
    acSym_LOAD_CALIB.setDefaultValue(calibRequired)

    isDACPresent = acComponent.createBooleanSymbol("AC_IS_DAC_PRESENT", None)
    isDACPresent.setValue(dacctrl_reg_present)
    isDACPresent.setVisible(False)

    for comparatorID in range(0, int(numOfComparators)):
        if cmpPresent[comparatorID] == 1:
            break

    acSym_COMPCTRL_MUXPOS_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "MUXPOS")
    acSym_COMPCTRL_MUXPOS_Node_Values = acSym_COMPCTRL_MUXPOS_Node.getChildren()
    for id in range(len(acSym_COMPCTRL_MUXPOS_Node_Values)):
        acSym_MUXPOS_ENUM = acComponent.createStringSymbol("AC_MUXPOS_ENUM_"+str(id), None)
        acSym_MUXPOS_ENUM.setDefaultValue(acSym_COMPCTRL_MUXPOS_Node_Values[id].getAttribute("name"))
        acSym_MUXPOS_ENUM.setVisible(False)

    acSym_COMPCTRL_MUXNEG_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "MUXNEG")
    acSym_COMPCTRL_MUXNEG_Node_Values = acSym_COMPCTRL_MUXNEG_Node.getChildren()
    for id in range(len(acSym_COMPCTRL_MUXNEG_Node_Values)):
        acSym_MUXNEG_ENUM = acComponent.createStringSymbol("AC_MUXNEG_ENUM_"+str(id), None)
        acSym_MUXNEG_ENUM.setDefaultValue(acSym_COMPCTRL_MUXNEG_Node_Values[id].getAttribute("name"))
        acSym_MUXNEG_ENUM.setVisible(False)

    if ctrlc_reg_present == True:
        acSym_ChargePumpEnable = acComponent.createBooleanSymbol("ANALOG_INPUT_CHARGE_PUMP_ENABLE", None)
        acSym_ChargePumpEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:CTRLC")
        acSym_ChargePumpEnable.setLabel("Analog Input Charge Pump Enable")

    #Populate menu for all comparators in the AC peripheral
    for comparatorID in range(0, int(numOfComparators)):
        # comparator ID enum
        acSym_COMP_NUM.append(comparatorID)
        acSym_COMP_NUM[comparatorID] = acComponent.createStringSymbol("AC_COMP_ID_ENUM_"+str(comparatorID), None)
        acSym_COMP_NUM[comparatorID].setVisible(False)
        if cmpPresent[comparatorID] == 0:
            acSym_COMP_NUM[comparatorID].setValue("-1")
        else:
            acSym_COMP_NUM[comparatorID].setValue("AC_CHANNEL" + str(comparatorID))

        acSym_Enable.append(comparatorID)
        acSym_Enable[comparatorID] = acComponent.createBooleanSymbol("ANALOG_COMPARATOR_ENABLE_" + str(comparatorID), None)
        acSym_Enable[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_Enable[comparatorID].setLabel("Comparator " + str(comparatorID) + " Settings")
        if cmpPresent[comparatorID] == 0:
            acSym_Enable[comparatorID].setVisible(False)

        #Interrupt Enable
        global acInterrupt_Enable
        acInterrupt_Enable = acComponent.createBooleanSymbol("COMP" + str(comparatorID) + "INTERRUPT_ENABLE", acSym_Enable[comparatorID])
        acInterrupt_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:intenset")
        acInterrupt_Enable.setLabel("Comparator Interrupt Enable")
        acInterrupt_Enable.setVisible(False)
        acInterrupt_Enable.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        nvicDep.append("COMP" + str(comparatorID) + "INTERRUPT_ENABLE")

        #Single-shot Mode
        acSym_COMPCTRL_SINGLE = acComponent.createBooleanSymbol("AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_SINGLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_SINGLE.setLabel("Enable Single Shot Mode")
        acSym_COMPCTRL_SINGLE.setDefaultValue(False)
        acSym_COMPCTRL_SINGLE.setVisible(False)
        acSym_COMPCTRL_SINGLE.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #MUXPOS
        acSym_COMPCTRL_MUXPOS = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_MUXPOS", acSym_Enable[comparatorID])
        acSym_COMPCTRL_MUXPOS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_MUXPOS.setLabel("Positive Input Mux Selection")
        acSym_COMPCTRL_MUXPOS.setVisible(False)

        acSym_COMPCTRL_MUXPOS_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "MUXPOS")
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
        acSym_COMPCTRL_MUXNEG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_MUXNEG.setLabel("Negative Input Mux Selection")
        acSym_COMPCTRL_MUXNEG.setVisible(False)

        acSym_COMPCTRL_MUXNEG_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "MUXNEG")
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

        acSym_SCALER_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"AC\"]/register@[name=\"SCALER\"]")
        if acSym_SCALER_Node != None:
            acSym_SCALER_MaxVal = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"AC\"]/register@[name=\"SCALER\"]/bitfield@[name=\"VALUE\"]").getAttribute("mask")
            #Scaling factor for VDD scaler
            acSym_SCALERn.append(comparatorID)
            acSym_SCALERn[comparatorID] = acComponent.createIntegerSymbol("AC_SCALER_N_" + str(comparatorID), acSym_Enable[comparatorID])
            acSym_SCALERn[comparatorID].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:SCALER0")
            acSym_SCALERn[comparatorID].setLabel("Scaling factor for VDD scaler")
            acSym_SCALERn[comparatorID].setMin(0)
            acSym_SCALERn[comparatorID].setMax(int(acSym_SCALER_MaxVal, 16))
            acSym_SCALERn[comparatorID].setDefaultValue(0)
            acSym_SCALERn[comparatorID].setVisible(False)
            #This should be enabled only when mux pos or mux neg value is VDDSCALER
            acSym_SCALERn[comparatorID].setDependencies(setacScalerVisibility, ["AC" + str(comparatorID) + "_MUXNEG", "AC" + str(comparatorID) + "_MUXPOS"])

        #Output Mode
        acSym_COMPCTRL_OUT = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_OUTPUT_TYPE", acSym_Enable[comparatorID])
        acSym_COMPCTRL_OUT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_OUT.setLabel("Output Edge Type")
        acSym_COMPCTRL_OUT.setVisible(False)

        acSym_COMPCTRL_OUT_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "OUT")
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
        acSym_COMPCTRL_ISEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_ISEL.setLabel("Interrupt Selection")
        acSym_COMPCTRL_ISEL.setVisible(False)

        acSym_COMPCTRL_ISEL_Node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "INTSEL")
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

        # COMPCTRLx.SUT
        if compctrl_sut_bitfield_present == True:
            acSym_COMPCTRL_SUT = acComponent.createIntegerSymbol("AC" + str(comparatorID) + "_COMPCTRL_SUT", acSym_Enable[comparatorID])
            acSym_COMPCTRL_SUT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
            acSym_COMPCTRL_SUT.setLabel("Start-up Time")
            acSym_COMPCTRL_SUT.setMin(0)
            acSym_COMPCTRL_SUT.setMax(31)
            acSym_COMPCTRL_SUT.setDefaultValue(0)
            acSym_COMPCTRL_SUT.setVisible(False)
            acSym_COMPCTRL_SUT.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #RUNSTDBY Enable
        acSym_COMPCTRL_RUNSTDBY = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_COMPCTRL_RUNSTDBY", acSym_Enable[comparatorID])
        acSym_COMPCTRL_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_RUNSTDBY.setLabel("Enable Run in Standby")
        acSym_COMPCTRL_RUNSTDBY.setDefaultValue(False)
        acSym_COMPCTRL_RUNSTDBY.setVisible(False)
        acSym_COMPCTRL_RUNSTDBY.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        if ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"{0}\"]/register@[name=\"COMPCTRL\"]/bitfield@[name=\"SPEED\"]".format(acSym_ChannelGroup.getValue())) != None:
            acSym_COMPCTRL_SPEED = acComponent.createIntegerSymbol("AC" + str(comparatorID) + "_COMPCTRL_SPEED", acSym_Enable[comparatorID])
            acSym_COMPCTRL_SPEED.setDefaultValue(3)
            acSym_COMPCTRL_SPEED.setVisible(False)

        if dacctrl_reg_present == True:
            # Internal DAC Configuration -

            # DACCTRL.VALUEx
            acSym_DACCTRL_VALUE = acComponent.createIntegerSymbol("AC" + str(comparatorID) + "_DACCTRL_VALUE", acSym_Enable[comparatorID])
            acSym_DACCTRL_VALUE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:DACCTRL")
            acSym_DACCTRL_VALUE.setLabel("DAC Output Value")
            acSym_DACCTRL_VALUE.setMin(0)
            acSym_DACCTRL_VALUE.setMax(127)
            acSym_DACCTRL_VALUE.setDefaultValue(0)
            acSym_DACCTRL_VALUE.setVisible(False)
            acSym_DACCTRL_VALUE.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

            acSym_DAC_OutVol = acComponent.createCommentSymbol("AC" + str(comparatorID) + "_DAC_OUTPUT_COMMENT", acSym_Enable[comparatorID])
            acSym_DAC_OutVol.setLabel("[With VDD = 3.3V, DAC Output = 0V]")
            acSym_DAC_OutVol.setVisible(False)
            acSym_DAC_OutVol.setDependencies(updateDACOutputVol, ["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID), "AC" + str(comparatorID) + "_DACCTRL_VALUE"])

            # DACCTRL.SHENx
            acSym_DACCTRL_SHEN = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_DACCTRL_SHEN", acSym_Enable[comparatorID])
            acSym_DACCTRL_SHEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:DACCTRL")
            acSym_DACCTRL_SHEN.setLabel("DAC Enable Sample and Hold Operation Mode")
            acSym_DACCTRL_SHEN.addKey("0x0", "0x0", "Continuous operation mode is enabled")
            acSym_DACCTRL_SHEN.addKey("0x1", "0x1", "Sample-and-hold operation mode is enabled")
            acSym_DACCTRL_SHEN.setDefaultValue(0)
            acSym_DACCTRL_SHEN.setOutputMode("Key")
            acSym_DACCTRL_SHEN.setDisplayMode("Description")
            acSym_DACCTRL_SHEN.setVisible(False)
            acSym_DACCTRL_SHEN.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #Menu item for advanced configurations
        acSym_AdvConf = acComponent.createMenuSymbol("AC_ADVANCED_CONFIGURATION_"+ str(comparatorID),  acSym_Enable[comparatorID])
        acSym_AdvConf.setLabel("Advanced Configurations")
        acSym_AdvConf.setVisible(False)
        acSym_AdvConf.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])

        #Hysteresis Enable
        acSym_COMPCTRL_HYSTEN_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"{0}\"]/register@[name=\"COMPCTRL\"]/bitfield@[name=\"HYSTEN\"]".format(acSym_ChannelGroup.getValue()))
        if acSym_COMPCTRL_HYSTEN_Node != None:
            acSym_COMPCTRL_HYSTEN = acComponent.createBooleanSymbol("AC" + str(comparatorID) + "_HYSTEN", acSym_AdvConf)
            acSym_COMPCTRL_HYSTEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
            acSym_COMPCTRL_HYSTEN.setLabel("Hysteresis Enable")
            acSym_COMPCTRL_HYSTEN.setDefaultValue(False)
            acSym_COMPCTRL_HYSTEN.setVisible(True)
            #Should not be shown when single-shot is selected.
            acSym_COMPCTRL_HYSTEN.setDependencies(setacHystVisibility,["AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE"])

        if getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "HYST") != None:
            #Hysteresis selection
            if acSym_COMPCTRL_HYSTEN_Node != None:
                acSym_COMPCTRL_HYST = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_HYST_VAL", acSym_COMPCTRL_HYSTEN)
            else:
                acSym_COMPCTRL_HYST = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_HYST_VAL", acSym_AdvConf)
                acSym_COMPCTRL_HYST.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
            acSym_COMPCTRL_HYST.setLabel("Hysteresis Selection")
            if acSym_COMPCTRL_HYSTEN_Node != None:
                acSym_COMPCTRL_HYST.setVisible(False)
            else:
                acSym_COMPCTRL_HYST.setVisible(True)
            acSym_COMPCTRL_HYST_node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "HYST")
            acSym_COMPCTRL_HYST_Values = []
            acSym_COMPCTRL_HYST_Values = acSym_COMPCTRL_HYST_node.getChildren()

            acSym_COMPCTRL_HYST_Default_Val = 0

            for id in range(len(acSym_COMPCTRL_HYST_Values)):
                acSym_COMPCTRL_HYST_Key_Name = acSym_COMPCTRL_HYST_Values[id].getAttribute("name")

                if(int(acSym_COMPCTRL_HYST_Values[id].getAttribute("value")) == 0):
                    acSym_COMPCTRL_HYST_Default_Val = id

                acSym_COMPCTRL_HYST_Key_Description = acSym_COMPCTRL_HYST_Values[id].getAttribute("caption")
                acSym_COMPCTRL_HYST_Key_Value = acSym_COMPCTRL_HYST_Values[id].getAttribute("value")
                acSym_COMPCTRL_HYST.addKey(acSym_COMPCTRL_HYST_Key_Name, acSym_COMPCTRL_HYST_Key_Value, acSym_COMPCTRL_HYST_Key_Description)

            acSym_COMPCTRL_HYST.setDefaultValue(acSym_COMPCTRL_HYST_Default_Val)
            acSym_COMPCTRL_HYST.setOutputMode("Value")
            acSym_COMPCTRL_HYST.setDisplayMode("Description")
            if acSym_COMPCTRL_HYSTEN_Node != None:
                acSym_COMPCTRL_HYST.setDependencies(setacSymbolVisibility,["AC" + str(comparatorID) + "_HYSTEN"])
            else:
                acSym_COMPCTRL_HYST.setDependencies(setacHystVisibility,["AC_COMPCTRL_" + str(comparatorID) +"SINGLE_MODE"])

        #Filter Length selection
        acSym_COMPCTRL_FLEN = acComponent.createKeyValueSetSymbol("AC" + str(comparatorID) + "_FLEN_VAL", acSym_AdvConf)
        acSym_COMPCTRL_FLEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:COMPCTRL0")
        acSym_COMPCTRL_FLEN.setLabel("Filter Length Selection")
        acSym_COMPCTRL_FLEN.setDescription("Filtering must be disabled if continuous measurements will be done during sleep modes")
        acSym_COMPCTRL_FLEN_node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "COMPCTRL", "FLEN")
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
        acSym_EVCTRL_COMPEI = acComponent.createKeyValueSetSymbol("AC_EVCTRL_COMPEI" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEI.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:EVCTRL")
        acSym_EVCTRL_COMPEI.setLabel("Enable Event Input")
        acSym_EVCTRL_COMPEI.setVisible(False)
        acSym_EVCTRL_COMPEI.setOutputMode("Value")
        acSym_EVCTRL_COMPEI.setDisplayMode("Description")
        acSym_EVCTRL_COMPEI.addKey("DISABLED", "0", "Disabled")
        acSym_EVCTRL_COMPEI.addKey("ENABLED_RISING_EDGE", "1", "Enabled on Rising Edge")
        acSym_EVCTRL_COMPEI.addKey("ENABLED_FALLING_EDGE", "2", "Enabled on Falling Edge")
        acSym_EVCTRL_COMPEI.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        evsysDep.append("AC_EVCTRL_COMPEI" + str(comparatorID))

        #Event Output Enable
        acSym_EVCTRL_COMPEO = acComponent.createBooleanSymbol("AC_EVCTRL_COMPEO" + str(comparatorID), acSym_AdvConf)
        acSym_EVCTRL_COMPEO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:EVCTRL")
        acSym_EVCTRL_COMPEO.setLabel("Enable Event Output")
        acSym_EVCTRL_COMPEO.setDefaultValue(False)
        acSym_EVCTRL_COMPEO.setVisible(False)
        acSym_EVCTRL_COMPEO.setDependencies(setacSymbolVisibility,["ANALOG_COMPARATOR_ENABLE_" + str(comparatorID)])
        evsysDep.append("AC_EVCTRL_COMPEO" + str(comparatorID))

    #Menu item for window configurations
    acSym_WindowConf = acComponent.createMenuSymbol("WINDOW_CONFIGURATION", None)
    acSym_WindowConf.setLabel("Comparator Window Configurations")

    win0Str = "0"
    if ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"{0}\"]/register@[name=\"WINCTRL\"]/bitfield@[name=\"WEN\"]".format(acSym_ChannelGroup.getValue())) != None:
        win0Str = ""
    acSym_WINCTRL_WEN0 = acComponent.createStringSymbol("AC_WINCTRL_WEN0", None)
    acSym_WINCTRL_WEN0.setDefaultValue(win0Str)
    acSym_WINCTRL_WEN0.setVisible(False)

    if win0Str != "":
        win0Str = "0 "

    #Window 0 configuration
    acSym_WINCTRL0 = acComponent.createBooleanSymbol("AC_WINCTRL_WIN0", acSym_WindowConf)
    acSym_WINCTRL0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:WINCTRL")
    acSym_WINCTRL0.setLabel("Window " + win0Str + "Enable")
    acSym_WINCTRL0.setDefaultValue(False)

    #Window 0 Interrupt Enable
    acSym_INTENSET_WIN0 = acComponent.createBooleanSymbol("AC_INTENSET_WIN0", acSym_WINCTRL0)
    acSym_INTENSET_WIN0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:INTENSET")
    acSym_INTENSET_WIN0.setLabel("Window " + win0Str + "Interrupt Enable")
    acSym_INTENSET_WIN0.setDefaultValue(False)
    acSym_INTENSET_WIN0.setVisible(False)
    acSym_INTENSET_WIN0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])
    nvicDep.append("AC_INTENSET_WIN0")

    #Window 0 interrupt configuration
    acSym_WNCTRL_WINT0 = acComponent.createKeyValueSetSymbol("AC_WINTSEL0", acSym_WINCTRL0)
    acSym_WNCTRL_WINT0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:WINCTRL")
    acSym_WNCTRL_WINT0.setLabel("AC Window " + win0Str + "Interrupt Selection")
    acSym_WNCTRL_WINT0.setVisible(False)
    acSym_WNCTRL_WINT0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])

    acSym_WNCTRL_WINT0_node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "WINCTRL" , "WINTSEL0")
    if acSym_WNCTRL_WINT0_node == None:
        acSym_WNCTRL_WINT0_node = getValueGrp("AC", acSym_ChannelGroup.getValue(), "WINCTRL" , "WINTSEL")
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
    acSym_WINCTRL_EVENT_OUT0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:EVCTRL")
    acSym_WINCTRL_EVENT_OUT0.setLabel("Enable Window " + win0Str + "Event Output")
    acSym_WINCTRL_EVENT_OUT0.setDefaultValue(False)
    acSym_WINCTRL_EVENT_OUT0.setVisible(False)
    acSym_WINCTRL_EVENT_OUT0.setDependencies(setacSymbolVisibility,["AC_WINCTRL_WIN0"])
    evsysDep.append("AC_EVCTRL_WINEO0")

    # DAC Sample-and-hold configuration:

    if ctrlc_reg_present == True:

        #Menu item for advanced configurations
        acSym_InternalDAC_SH_Conf = acComponent.createMenuSymbol("AC_DAC_SH_CONFIG",  None)
        acSym_InternalDAC_SH_Conf.setLabel("Internal DAC Sample-Hold configuration")

        # CTRLC.PRESCALER
        acSym_CTRLC_PRESCALER_Node = getValueGrp("AC", "AC", "CTRLC" , "PRESCALER")
        acSym_CTRLC_PRESCALER_Values = acSym_CTRLC_PRESCALER_Node.getChildren()

        acSym_CTRLC_PRESCALSER = acComponent.createKeyValueSetSymbol("AC_CTRLC_PRESCALER", acSym_InternalDAC_SH_Conf)
        acSym_CTRLC_PRESCALSER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:CTRLC")
        acSym_CTRLC_PRESCALSER.setLabel("Prescaler for DAC sampling clock")

        for id in range (len(acSym_CTRLC_PRESCALER_Values)):
            acSym_CTRLC_PRESCALSER_Key_Name = acSym_CTRLC_PRESCALER_Values[id].getAttribute("name")
            acSym_CTRLC_PRESCALSER_Key_Value = acSym_CTRLC_PRESCALER_Values[id].getAttribute("value")
            acSym_CTRLC_PRESCALSER_Key_Description = acSym_CTRLC_PRESCALER_Values[id].getAttribute("caption")
            acSym_CTRLC_PRESCALSER.addKey(acSym_CTRLC_PRESCALSER_Key_Name, acSym_CTRLC_PRESCALSER_Key_Value, acSym_CTRLC_PRESCALSER_Key_Description)

        acSym_CTRLC_PRESCALSER.setDefaultValue(0)
        acSym_CTRLC_PRESCALSER.setOutputMode("Key")
        acSym_CTRLC_PRESCALSER.setDisplayMode("Description")

        # CTRLC.PERIOD
        acSym_CTRLC_PERIOD = acComponent.createIntegerSymbol("AC_CTRLC_PERIOD", acSym_InternalDAC_SH_Conf)
        acSym_CTRLC_PERIOD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:CTRLC")
        acSym_CTRLC_PERIOD.setLabel("Sample and Hold Clock Period")
        acSym_CTRLC_PERIOD.setMin(0)
        acSym_CTRLC_PERIOD.setMax(511)
        acSym_CTRLC_PERIOD.setDefaultValue(0)

        # CTRLC.WIDTH
        acSym_CTRLC_WIDTH = acComponent.createIntegerSymbol("AC_CTRLC_WIDTH", acSym_InternalDAC_SH_Conf)
        acSym_CTRLC_WIDTH.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ac_u2501;register:CTRLC")
        acSym_CTRLC_WIDTH.setLabel("Sample and Hold Clock Pulse Width")
        acSym_CTRLC_WIDTH.setMin(0)
        acSym_CTRLC_WIDTH.setMax(511)
        acSym_CTRLC_WIDTH.setDefaultValue(0)


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

    acSym_CTRLB_SIZE = acComponent.createIntegerSymbol("AC_CTRLB_SIZE", None)
    acSym_CTRLB_SIZE.setDefaultValue(int(ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"AC\"]/register-group@[name=\"AC\"]/register@[name=\"CTRLB\"]").getAttribute("size")))
    acSym_CTRLB_SIZE.setVisible(False)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global ACfilesArray
        acIsNonSecure = Database.getSymbolValue("core", acComponent.getID().upper() + "_IS_NON_SECURE")
        Database.setSymbolValue("core", InterruptVectorSecurity, acIsNonSecure)

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

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        ACfilesArray.append(acHeader1File)
        ACfilesArray.append(acSource1File)
        ACfilesArray.append(acSystemInitFile)
        ACfilesArray.append(acSystemDefFile)

        if acIsNonSecure == False:
            acHeader1File.setSecurity("SECURE")
            acSource1File.setSecurity("SECURE")
            acSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

        #callback function to check if peripheral is secure
        acSystemDefFile.setDependencies(fileUpdate, ["core." + acComponent.getID().upper() + "_IS_NON_SECURE"])