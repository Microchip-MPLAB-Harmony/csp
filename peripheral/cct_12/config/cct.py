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
global sysTimeComponentId

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def sysTimePLIBModeConfig(plibMode):

    if (plibMode == "SYS_TIME_PLIB_MODE_COMPARE"):
        component = sysTimeComponentId.getComponent()
        component.getSymbolByID("CCT_ENABLE_COMPARE_0").setValue(True)
        component.getSymbolByID("CCT_CMP_INTERRUPT_EN_0").setValue(True)

def handleMessage(messageID, args):
    dummy_dict = {}
    sysTimePLIBConfig = dict()

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        modeDict = {"plib_mode": "COMPARE_MODE"}
        sysTimePLIBConfig = Database.sendMessage(args["ID"], "SYS_TIME_PLIB_CAPABILITY", modeDict)
        sysTimePLIBModeConfig(sysTimePLIBConfig["plib_mode"])

    return dummy_dict

def msecToCount(clk_hz, timeoutMs):
    global msecToCount
    countVal = (timeoutMs / 1000.0) * clk_hz    
    return countVal

def calcRTOSTimeoutInMsec(clk_hz, preload_val):
    global calcRTOSTimeoutInMsec
    timeout_msec = float(preload_val)/(clk_hz)
    timeout_msec = timeout_msec * 1000.0
    return timeout_msec

###################################################################################################
########################################## Component  #############################################
###################################################################################################
def setCCTInterruptData(cct_interrupt_name, status):
    global setCCTInterruptData

    Database.setSymbolValue("core", cct_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", cct_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", cct_interrupt_name + "_INTERRUPT_HANDLER", cct_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", cct_interrupt_name + "_INTERRUPT_HANDLER", cct_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateCCT(cctInterrupt, enable, interruptType):
    global setCCTInterruptData
    global nvicInterruptUpdateCCT

    interruptNameDir = cctInterrupt
    interruptNameAgg = cctInterrupt + "_GRP"

    if enable == True:
        if interruptType == "AGGREGATE":
            setCCTInterruptData(interruptNameDir, False)
            setCCTInterruptData(interruptNameAgg, True)
        else:
            setCCTInterruptData(interruptNameAgg, False)
            setCCTInterruptData(interruptNameDir, True)
    else:
        setCCTInterruptData(interruptNameAgg, False)
        setCCTInterruptData(interruptNameDir, False)

def nvicInterruptUpdate(symbol, event):
    global nvicInterruptUpdateCCT

    cctEnable = event["value"]
    cctInterrupt = ""

    interruptType = event["source"].getSymbolByID("CCT_INTERRUPT_TYPE").getSelectedKey()

    if "CCT_INTERRUPT_TYPE" in event["id"]:

        capChannels = event["source"].getSymbolByID("CCT_NUM_CAP_CH").getValue()
        for ch in range(0, capChannels):
            cctInterrupt = "CCT_CAP" + str(ch)
            cctEnable = event["source"].getSymbolByID("CCT_ENABLE_CAPTURE_" + str(ch)).getValue()
            cctIntEnable = event["source"].getSymbolByID("CCT_CAP_INTERRUPT_EN_" + str(ch)).getValue()
            nvicInterruptUpdateCCT(cctInterrupt, (cctEnable and cctIntEnable), interruptType)

        cmpChannels = event["source"].getSymbolByID("CCT_NUM_CMP_CH").getValue()
        for ch in range(0, cmpChannels):
            cctInterrupt = "CCT_CMP" + str(ch)
            cctEnable = event["source"].getSymbolByID("CCT_ENABLE_COMPARE_" + str(ch)).getValue()
            cctIntEnable = event["source"].getSymbolByID("CCT_CMP_INTERRUPT_EN_" + str(ch)).getValue()
            nvicInterruptUpdateCCT(cctInterrupt, (cctEnable and cctIntEnable), interruptType)

        cctInterrupt = "CCT"
        cctIntEnable = event["source"].getSymbolByID("CCT_OVF_INTERRUPT_EN").getValue()
        nvicInterruptUpdateCCT(cctInterrupt, cctIntEnable, interruptType)

    elif "CCT_ENABLE_CAPTURE_" in event["id"] or "CCT_CAP_INTERRUPT_EN_" in event["id"]:
        ch = event["id"][-1]
        cctInterrupt = "CCT_CAP" + ch
        cctEnable = event["source"].getSymbolByID("CCT_ENABLE_CAPTURE_" + ch).getValue()
        cctIntEnable = event["source"].getSymbolByID("CCT_CAP_INTERRUPT_EN_" + ch).getValue()
        nvicInterruptUpdateCCT(cctInterrupt, (cctEnable and cctIntEnable), interruptType)

    elif "CCT_ENABLE_COMPARE_" in event["id"] or "CCT_CMP_INTERRUPT_EN_" in event["id"]:
        ch = event["id"][-1]
        cctInterrupt = "CCT_CMP" + ch
        cctEnable = event["source"].getSymbolByID("CCT_ENABLE_COMPARE_" + ch).getValue()
        cctIntEnable = event["source"].getSymbolByID("CCT_CMP_INTERRUPT_EN_" + ch).getValue()
        nvicInterruptUpdateCCT(cctInterrupt, (cctEnable and cctIntEnable), interruptType)

    elif "CCT_OVF_INTERRUPT_EN" in event["id"]:
        cctInterrupt = "CCT"
        cctIntEnable = event["value"]
        nvicInterruptUpdateCCT(cctInterrupt, cctIntEnable, interruptType)


def updateVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateFilterDivVisibility(symbol, event):
    ch = symbol.getID()[-1]

    cap_en = event["source"].getSymbolByID("CCT_ENABLE_CAPTURE_" + ch).getValue()
    cap_flt_en = event["source"].getSymbolByID("CCT_INPUT_FLTR_EN_" + ch).getValue()

    symbol.setVisible(cap_en == True and cap_flt_en == True)

def irqn_update(symbol, event):
    interruptType = event["source"].getSymbolByID("CCT_INTERRUPT_TYPE").getSelectedKey()
    
    if (interruptType == "AGGREGATE"):
        nvic_int_num = {}
        nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "CCT_CMP0"})
        irqn_name = "GIRQ" + str(nvic_int_num["girqn_reg_num"] + 8) + "_IRQn"
        symbol.setValue(irqn_name)
    else:
        symbol.setValue("CCT_CMP0_IRQn")

def instantiateComponent(cctComponent):

    """ Function to instantiate tcComponent to Active Component """
    global sysTimeComponentId
    #--------------------------------------------------------------------------------------------------------------------------#

    cctInstanceName = cctComponent.createStringSymbol("CCT_INSTANCE_NAME", None)
    cctInstanceName.setVisible(False)
    cctInstanceName.setDefaultValue(cctComponent.getID().upper())

    icctPinMap = {}
    numICCTPins = 0
    nvicUpdateDepList = []

    icct_pins = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"CCT\"]/instance@[name=\""+cctInstanceName.getValue()+"\"]/signals").getChildren()
    for index in range(0, len(icct_pins)):
        group = icct_pins[index].getAttribute("group")
        icctPinMap[group] = group.split("ICT")[1]

    numICCTPins = len(icct_pins)

    numCapRegisters = 0
    cct = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCT\"]/register-group@[name=\"CCT\"]").getChildren()
    for index in range(0, len(cct)):
        register_name = cct[index].getAttribute("name")
        if ("CAP" in register_name and "CTRL" not in register_name):
            numCapRegisters += 1

    numCmpRegisters = 0
    cct = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCT\"]/register-group@[name=\"CCT\"]").getChildren()
    for index in range(0, len(cct)):
        register_name = cct[index].getAttribute("name")
        if ("COMP" in register_name and "CTRL" not in register_name):
            numCmpRegisters += 1

    cctPinEdge_Values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCT\"]/value-group@[name=\"CAPX_CTRL__CAP_EDGE\"]").getChildren()
    cctFCLKSel_Values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CCT\"]/value-group@[name=\"CAPX_CTRL__FCLK_SEL\"]").getChildren()

    #-------------------------------------------------------------------------------------------------------------------------#

    numCapChannels = cctComponent.createIntegerSymbol("CCT_NUM_CAP_CH", None)
    numCapChannels.setDefaultValue(numCapRegisters)
    numCapChannels.setVisible(False)

    numComChannels = cctComponent.createIntegerSymbol("CCT_NUM_CMP_CH", None)
    numComChannels.setDefaultValue(numCmpRegisters)
    numComChannels.setVisible(False)

    cctFRTClockSrcDiv = cctComponent.createKeyValueSetSymbol("CCT_FRT_CLK_SRC_DIV", None)
    cctFRTClockSrcDiv.setLabel("Free Running Timer Frequency Divider")
    for index in range(len(cctFCLKSel_Values)):
        cctFRTClockSrcDiv.addKey(cctFCLKSel_Values[index].getAttribute("name"), cctFCLKSel_Values[index].getAttribute("value"), cctFCLKSel_Values[index].getAttribute("caption"))
    cctFRTClockSrcDiv.setOutputMode("Value")
    cctFRTClockSrcDiv.setDisplayMode("Description")

    # Interrupt type selection
    cctInterruptType = cctComponent.createKeyValueSetSymbol("CCT_INTERRUPT_TYPE", None)
    cctInterruptType.setLabel("Interrupt Type")
    cctInterruptType.addKey("DIRECT", "0", "Direct")
    cctInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    cctInterruptType.setDefaultValue(0)
    cctInterruptType.setDisplayMode("Description")
    cctInterruptType.setOutputMode("Key")

    nvicUpdateDepList.append("CCT_INTERRUPT_TYPE")

    cctOvfInputerruptEn = cctComponent.createBooleanSymbol("CCT_OVF_INTERRUPT_EN", None)
    cctOvfInputerruptEn.setLabel("Timer Overflow Interrupt Enable")
    cctOvfInputerruptEn.setDefaultValue(False)

    nvicUpdateDepList.append("CCT_OVF_INTERRUPT_EN")

    for capChannel in range (0, numCapRegisters):
        cctCaptureEn = cctComponent.createBooleanSymbol("CCT_ENABLE_CAPTURE_" + str(capChannel), None)
        cctCaptureEn.setLabel("Enable Capture Channel " + str(capChannel))
        cctCaptureEn.setDefaultValue(False)

        cctCapturePin = cctComponent.createKeyValueSetSymbol("CCT_PIN_CAPTURE_" + str(capChannel), cctCaptureEn)
        for key, value in icctPinMap.items():
            cctCapturePin.addKey(key, value, key)
        cctCapturePin.setOutputMode("Value")
        cctCapturePin.setDisplayMode("Description")
        cctCapturePin.setLabel("Capture Pin")
        cctCapturePin.setVisible(False)
        cctCapturePin.setDependencies(updateVisibility, ["CCT_ENABLE_CAPTURE_" + str(capChannel)])

        cctCaptureEdge = cctComponent.createKeyValueSetSymbol("CCT_PIN_EDGE_" + str(capChannel), cctCaptureEn)
        cctCaptureEdge.setLabel("Capture Edge Select")
        for index in range(len(cctPinEdge_Values)):
            cctCaptureEdge.addKey(cctPinEdge_Values[index].getAttribute("name"), cctPinEdge_Values[index].getAttribute("value"), cctPinEdge_Values[index].getAttribute("caption"))
        cctCaptureEdge.setOutputMode("Value")
        cctCaptureEdge.setDisplayMode("Description")
        cctCaptureEdge.setVisible(False)
        cctCaptureEdge.setDependencies(updateVisibility, ["CCT_ENABLE_CAPTURE_" + str(capChannel)])

        cctCapInputerruptEn = cctComponent.createBooleanSymbol("CCT_CAP_INTERRUPT_EN_" + str(capChannel), cctCaptureEn)
        cctCapInputerruptEn.setLabel("Interrupt Enable")
        cctCapInputerruptEn.setDefaultValue(False)
        cctCapInputerruptEn.setVisible(False)
        cctCapInputerruptEn.setDependencies(updateVisibility, ["CCT_ENABLE_CAPTURE_" + str(capChannel)])

        cctInputFilterEn = cctComponent.createBooleanSymbol("CCT_INPUT_FLTR_EN_" + str(capChannel), cctCaptureEn)
        cctInputFilterEn.setLabel("Input Filter Enable")
        cctInputFilterEn.setDefaultValue(False)
        cctInputFilterEn.setVisible(False)
        cctInputFilterEn.setDependencies(updateVisibility, ["CCT_ENABLE_CAPTURE_" + str(capChannel)])

        cctFilterFreqDivSel = cctComponent.createKeyValueSetSymbol("CCT_INPUT_FLTR_DIV_" + str(capChannel), cctInputFilterEn)
        cctFilterFreqDivSel.setLabel("Filter Frequency Divider")
        for index in range(len(cctFCLKSel_Values)):
            cctFilterFreqDivSel.addKey(cctFCLKSel_Values[index].getAttribute("name"), cctFCLKSel_Values[index].getAttribute("value"), cctFCLKSel_Values[index].getAttribute("caption"))
        cctFilterFreqDivSel.setOutputMode("Value")
        cctFilterFreqDivSel.setDisplayMode("Description")
        cctFilterFreqDivSel.setVisible(False)
        cctFilterFreqDivSel.setDependencies(updateFilterDivVisibility, ["CCT_ENABLE_CAPTURE_" + str(capChannel), "CCT_INPUT_FLTR_EN_" + str(capChannel)])

        nvicUpdateDepList.append("CCT_ENABLE_CAPTURE_" + str(capChannel))
        nvicUpdateDepList.append("CCT_CAP_INTERRUPT_EN_" + str(capChannel))

    for compChannel in range (0, numCmpRegisters):
        cctCompareEn = cctComponent.createBooleanSymbol("CCT_ENABLE_COMPARE_" + str(compChannel), None)
        cctCompareEn.setLabel("Enable Compare Channel " + str(compChannel))
        cctCompareEn.setDefaultValue(False)

        cctCompareVal = cctComponent.createIntegerSymbol("CCT_COMPARE_VALUE_" + str(compChannel), cctCompareEn)
        cctCompareVal.setLabel("Compare Value")
        cctCompareVal.setDefaultValue(32768)
        cctCompareVal.setVisible(False)
        cctCompareVal.setDependencies(updateVisibility, ["CCT_ENABLE_COMPARE_" + str(compChannel)])

        cctCompInputerruptEn = cctComponent.createBooleanSymbol("CCT_CMP_INTERRUPT_EN_" + str(compChannel), cctCompareEn)
        cctCompInputerruptEn.setLabel("Interrupt Enable")
        cctCompInputerruptEn.setDefaultValue(False)
        cctCompInputerruptEn.setVisible(False)
        cctCompInputerruptEn.setDependencies(updateVisibility, ["CCT_ENABLE_COMPARE_" + str(compChannel)])

        nvicUpdateDepList.append("CCT_CMP_INTERRUPT_EN_" + str(compChannel))
        nvicUpdateDepList.append("CCT_ENABLE_COMPARE_" + str(compChannel))

    # Internal symbol to update NVIC
    cctInputerruptUpdate = cctComponent.createBooleanSymbol("CCT_INTERRUPT_UPDATE", None)
    cctInputerruptUpdate.setVisible(False)
    cctInputerruptUpdate.setDependencies(nvicInterruptUpdate, nvicUpdateDepList)

#---------------------Symbols needed by SYS Time----------------#    

    # Symbol to save SYS Time ID
    sysTimeComponentId = cctComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")
    
    timerStartApiName = cctInstanceName.getValue() +  "_FreeRunningTimerStart"
    timerStopApiName = cctInstanceName.getValue() + "_FreeRunningTimerStop"
    counterGetApiName = cctInstanceName.getValue() +  "_FreeRunningTimerGet"
    compareSetApiName = cctInstanceName.getValue() +  "_CompareChannel0PeriodSet"
    frequencyGetApiName = cctInstanceName.getValue() + "_FrequencyGet"
    callbackApiName = cctInstanceName.getValue() + "_Compare0CallbackRegister"  # Hard-coded: Sys time uses compare channel 0 only

    timerWidth_Sym = cctComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = cctComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = cctComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = cctComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timerStopApiName)
    
    compareSetApiName_Sym = cctComponent.createStringSymbol("COMPARE_SET_API_NAME", None)
    compareSetApiName_Sym.setVisible(False)
    compareSetApiName_Sym.setDefaultValue(compareSetApiName)

    counterApiName_Sym = cctComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = cctComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = cctComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)
    
    irqEnumName_Sym = cctComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue("CCT_CMP0_IRQn")
    irqEnumName_Sym.setDependencies(irqn_update, ["CCT_INTERRUPT_TYPE"])
#----------------------------------------------------------------------------------------------------------------------------#

    configName = Variables.get("__CONFIGURATION_NAME")

    cctSourceFile = cctComponent.createFileSymbol("CCT_SOURCE", None)
    cctSourceFile.setSourcePath("../peripheral/cct_12/templates/plib_cct.c.ftl")
    cctSourceFile.setOutputName("plib_"+ cctInstanceName.getValue().lower() + ".c")
    cctSourceFile.setDestPath("/peripheral/cct/")
    cctSourceFile.setProjectPath("config/" + configName + "/peripheral/cct/")
    cctSourceFile.setType("SOURCE")
    cctSourceFile.setMarkup(True)
    cctSourceFile.setOverwrite(True)

    cctHeaderFile = cctComponent.createFileSymbol("CCT_HEADER", None)
    cctHeaderFile.setSourcePath("../peripheral/cct_12/templates/plib_cct.h.ftl")
    cctHeaderFile.setOutputName("plib_"+ cctInstanceName.getValue().lower() + ".h")
    cctHeaderFile.setDestPath("/peripheral/cct/")
    cctHeaderFile.setProjectPath("config/" + configName + "/peripheral/cct/")
    cctHeaderFile.setType("HEADER")
    cctHeaderFile.setMarkup(True)
    cctHeaderFile.setOverwrite(True)

    cctCommonHeaderFile = cctComponent.createFileSymbol("CCT_COMMON_HEADER", None)
    cctCommonHeaderFile.setSourcePath("../peripheral/cct_12/templates/plib_cct_common.h")
    cctCommonHeaderFile.setOutputName("plib_" + cctInstanceName.getValue().lower() + "_common.h")
    cctCommonHeaderFile.setDestPath("/peripheral/cct/")
    cctCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/cct/")
    cctCommonHeaderFile.setType("HEADER")
    cctCommonHeaderFile.setMarkup(False)
    cctCommonHeaderFile.setOverwrite(True)

    cctSystemInitFile = cctComponent.createFileSymbol("CCT_SYS_INT", None)
    cctSystemInitFile.setType("STRING")
    cctSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cctSystemInitFile.setSourcePath("../peripheral/cct_12/templates/system/initialization.c.ftl")
    cctSystemInitFile.setMarkup(True)
    cctSystemInitFile.setOverwrite(True)

    cctSystemDefFile = cctComponent.createFileSymbol("CCT_SYS_DEF", None)
    cctSystemDefFile.setType("STRING")
    cctSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cctSystemDefFile.setSourcePath("../peripheral/cct_12/templates/system/definitions.h.ftl")
    cctSystemDefFile.setMarkup(True)
    cctSystemDefFile.setOverwrite(True)