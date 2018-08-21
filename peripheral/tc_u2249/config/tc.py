global tcInstanceMasterValue
global isMasterSlaveModeEnable
global tySym_Slave_Mode
global tcSym_OperationMode
###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()

    component.getSymbolByID("TC_TIMER_HEADER").setEnabled(False)
    component.getSymbolByID("TC_TIMER_SOURCE").setEnabled(False)
    component.getSymbolByID("TC_COMPARE_HEADER").setEnabled(False)
    component.getSymbolByID("TC_COMPARE_SOURCE").setEnabled(False)
    component.getSymbolByID("TC_CAPTURE_HEADER").setEnabled(False)
    component.getSymbolByID("TC_CAPTURE_SOURCE").setEnabled(False)

    if (tySym_Slave_Mode.getValue() == False):
        if tcSym_OperationMode.getValue() == "Timer":
            component.getSymbolByID("TC_TIMER_HEADER").setEnabled(True)
            component.getSymbolByID("TC_TIMER_SOURCE").setEnabled(True)
        elif tcSym_OperationMode.getValue() == "Compare":
            component.getSymbolByID("TC_COMPARE_HEADER").setEnabled(True)
            component.getSymbolByID("TC_COMPARE_SOURCE").setEnabled(True)
        elif tcSym_OperationMode.getValue() == "Capture":
            component.getSymbolByID("TC_CAPTURE_HEADER").setEnabled(True)
            component.getSymbolByID("TC_CAPTURE_SOURCE").setEnabled(True)
        
def tcSlaveModeVisible(symbol, event):
    if event["value"] == 2:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def tcSlaveModeCommentVisible(symbol, event):
    if event["value"] == 2:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
        
def tcSlaveModeSet(symbol, event):
    if event["value"] == 2:
        symbol.setVisible(True)
        symbol.setValue(True, 2)
    else:
        symbol.setVisible(False)
        symbol.setValue(False, 2)
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tcComponent):

    """ Function to instantiate tcComponent to Active Component """

    tcInstanceIndex = tcComponent.getID()[-1:]
    Log.writeInfoMessage("Running TC" + str(tcInstanceIndex))

    #index
    tcSym_Index = tcComponent.createIntegerSymbol("TC_INDEX", None)
    tcSym_Index.setDefaultValue(int(tcInstanceIndex))
    tcSym_Index.setVisible(False)
    tcSym_Index.setDependencies(updateCodeGenerationProperty, ["TC_OPERATION_MODE", "TC_SLAVE_MODE"])

    tcInstanceMasterNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]/instance@[name=\"TC" + tcInstanceIndex + "\"]/parameters/param@[name=\"MASTER_SLAVE_MODE\"]")
    tcInstanceMasterValue = int(tcInstanceMasterNode.getAttribute("value"))
    isMasterSlaveModeEnable = False
    
    if (tcInstanceMasterValue == 2):
        activeComponentList = Database.getActiveComponentIDs()
        masterComponentID = "tc" + str(int(tcInstanceIndex) - 1)
        masterComponentSymbolId = masterComponentID + ".TC_CTRLA_MODE"

        if masterComponentID in activeComponentList:
            value = Database.getSymbolValue(masterComponentID, "TC_CTRLA_MODE")
            print("counter mode " + str(value))
            if value == 2:
                isMasterSlaveModeEnable = True

    global tySym_Slave_Mode
    tySym_Slave_Mode = tcComponent.createBooleanSymbol("TC_SLAVE_MODE", None)
    tySym_Slave_Mode.setDefaultValue(isMasterSlaveModeEnable)
    tySym_Slave_Mode.setVisible(True)
    if (tcInstanceMasterValue == 2):
        tySym_Slave_Mode.setDependencies(tcSlaveModeSet, [masterComponentSymbolId])

    #counter mode
    tcSym_CTRLA_MODE = tcComponent.createKeyValueSetSymbol("TC_CTRLA_MODE", None)
    tcSym_CTRLA_MODE.setLabel("Counter Mode")
    tcModeNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CTRLA__MODE\"]")
    tcModeValues = []
    tcModeValues = tcModeNode.getChildren()
    tcModeDefaultValue = 0
    for index in range(len(tcModeValues)):
        tcModeKeyName = tcModeValues[index].getAttribute("name")
        if tcModeKeyName == "COUNT16":
            tcModeDefaultValue = index
        if tcModeKeyName == "COUNT32" and tcInstanceMasterValue != 1:
            continue
        tcModeKeyDescription = tcModeValues[index].getAttribute("caption")
        tcModeKeyValue = tcModeValues[index].getAttribute("value")
        tcSym_CTRLA_MODE.addKey(tcModeKeyName, tcModeKeyValue, tcModeKeyDescription)
    tcSym_CTRLA_MODE.setDefaultValue(tcModeDefaultValue)
    tcSym_CTRLA_MODE.setOutputMode("Key")
    tcSym_CTRLA_MODE.setDisplayMode("Description")
    if (tcInstanceMasterValue == 2):
        tcSym_CTRLA_MODE.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #prescaler
    tcSym_CTRLA_PRESCALER = tcComponent.createKeyValueSetSymbol("TC_CTRLA_PRESCALER", None)
    tcSym_CTRLA_PRESCALER.setLabel("Select Prescaler")
    tcPrescalerSelectionNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]/value-group@[name=\"TC_CTRLA__PRESCALER\"]")
    tcPrescalerSelectionValues = []
    tcPrescalerSelectionValues = tcPrescalerSelectionNode.getChildren()
    tcPrescalerSelectionDefaultValue = 0
    for index in range(len(tcPrescalerSelectionValues)):
        tcPrescalerSelectionKeyName = tcPrescalerSelectionValues[index].getAttribute("name")
        if tcPrescalerSelectionKeyName == "DIV1":
            tcPrescalerSelectionDefaultValue = index
        tcPrescalerSelectionKeyDescription = tcPrescalerSelectionValues[index].getAttribute("caption")
        tcPrescalerSelectionKeyValue = tcPrescalerSelectionValues[index].getAttribute("value")
        tcSym_CTRLA_PRESCALER.addKey(tcPrescalerSelectionKeyName, tcPrescalerSelectionKeyValue, tcPrescalerSelectionKeyDescription)
    tcSym_CTRLA_PRESCALER.setDefaultValue(tcPrescalerSelectionDefaultValue)
    tcSym_CTRLA_PRESCALER.setOutputMode("Key")
    tcSym_CTRLA_PRESCALER.setDisplayMode("Description")
    if (tcInstanceMasterValue == 2):
        tcSym_CTRLA_PRESCALER.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #clock resolution display
    tcSym_Resolution = tcComponent.createCommentSymbol("TC_Resolution", None)
    tcSym_Resolution.setLabel("****Timer resolution is " + str(20.83) + " nS****")
    if (tcInstanceMasterValue == 2):
        tcSym_Resolution.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #TC clock frequency
    tcSym_Frequency = tcComponent.createIntegerSymbol("TC_FREQUENCY", None)
    tcSym_Frequency.setLabel("Clock Frequency")
    tcSym_Frequency.setVisible(False)
    tcSym_Frequency.setDefaultValue(48000000)
    if (tcInstanceMasterValue == 2):
        tcSym_Frequency.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #tc operation mode
    tcOperationModeList = ["Timer", "Compare", "Capture"]
    global tcSym_OperationMode
    tcSym_OperationMode = tcComponent.createComboSymbol("TC_OPERATION_MODE", None, tcOperationModeList)
    tcSym_OperationMode.setLabel("Operating Mode")
    tcSym_OperationMode.setDefaultValue("Timer")
    if (tcInstanceMasterValue == 2):
        tcSym_OperationMode.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])
        
    tcSym_SlaveMode_Comment = tcComponent.createCommentSymbol("TC_SLAVE_MODE_COMMENT", None)
    tcSym_SlaveMode_Comment.setVisible(False)
    tcSym_SlaveMode_Comment.setLabel("TC is configured in Slave mode to support 32-bit operation")
    if (tcInstanceMasterValue == 2):
        tcSym_SlaveMode_Comment.setDependencies(tcSlaveModeCommentVisible, [masterComponentSymbolId])

    ###################################################################################################
    #################################### Sleep Configuration  #######################################
    ###################################################################################################

    #sleep configuration
    tcSym_SleepConfiguration = tcComponent.createMenuSymbol("TC_SLEEP_CONFIG", None)
    tcSym_SleepConfiguration.setLabel("Sleep Configurations")
    if (tcInstanceMasterValue == 2):
        tcSym_SleepConfiguration.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])

    #run standby mode
    tcSym_CTRLA_RUNSTDBY = tcComponent.createBooleanSymbol("TC_CTRLA_RUNSTDBY", tcSym_SleepConfiguration)
    tcSym_CTRLA_RUNSTDBY.setLabel("Run during Standby")

    #on demand mode
    tcSym_CTRLA_ONDEMAND = tcComponent.createBooleanSymbol("TC_CTRLA_ONDEMAND", tcSym_SleepConfiguration)
    tcSym_CTRLA_ONDEMAND.setLabel("Clock On Demand")

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TC\"]")
    tcModuleID = tcModuleNode.getAttribute("id")

    tcSym_CommonHeaderFile = tcComponent.createFileSymbol("TC_COMMON_HEADER", None)
    tcSym_CommonHeaderFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/plib_tc.h")
    tcSym_CommonHeaderFile.setOutputName("plib_tc.h")
    tcSym_CommonHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CommonHeaderFile.setType("HEADER")
    tcSym_CommonHeaderFile.setMarkup(True)

    tcSym_TimerHeaderFile = tcComponent.createFileSymbol("TC_TIMER_HEADER", None)
    tcSym_TimerHeaderFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_timer.h.ftl")
    tcSym_TimerHeaderFile.setOutputName("plib_tc" + tcInstanceIndex + ".h")
    tcSym_TimerHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_TimerHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_TimerHeaderFile.setType("HEADER")
    tcSym_TimerHeaderFile.setMarkup(True)

    tcSym_TimerSourceFile = tcComponent.createFileSymbol("TC_TIMER_SOURCE", None)
    tcSym_TimerSourceFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_timer.c.ftl")
    tcSym_TimerSourceFile.setOutputName("plib_tc" + tcInstanceIndex + ".c")
    tcSym_TimerSourceFile.setDestPath("/peripheral/tc/")
    tcSym_TimerSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_TimerSourceFile.setType("SOURCE")
    tcSym_TimerSourceFile.setMarkup(True)

    tcSym_CompareHeaderFile = tcComponent.createFileSymbol("TC_COMPARE_HEADER", None)
    tcSym_CompareHeaderFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_compare.h.ftl")
    tcSym_CompareHeaderFile.setOutputName("plib_tc" + tcInstanceIndex + ".h")
    tcSym_CompareHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CompareHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CompareHeaderFile.setType("HEADER")
    tcSym_CompareHeaderFile.setMarkup(True)

    tcSym_CompareSourceFile = tcComponent.createFileSymbol("TC_COMPARE_SOURCE", None)
    tcSym_CompareSourceFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_compare.c.ftl")
    tcSym_CompareSourceFile.setOutputName("plib_tc" + tcInstanceIndex + ".c")
    tcSym_CompareSourceFile.setDestPath("/peripheral/tc/")
    tcSym_CompareSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CompareSourceFile.setType("SOURCE")
    tcSym_CompareSourceFile.setMarkup(True)

    tcSym_CaptureHeaderFile = tcComponent.createFileSymbol("TC_CAPTURE_HEADER", None)
    tcSym_CaptureHeaderFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_capture.h.ftl")
    tcSym_CaptureHeaderFile.setOutputName("plib_tc" + tcInstanceIndex + ".h")
    tcSym_CaptureHeaderFile.setDestPath("/peripheral/tc/")
    tcSym_CaptureHeaderFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CaptureHeaderFile.setType("HEADER")
    tcSym_CaptureHeaderFile.setMarkup(True)

    tcSym_CaptureSourceFile = tcComponent.createFileSymbol("TC_CAPTURE_SOURCE", None)
    tcSym_CaptureSourceFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/plib_tc_capture.c.ftl")
    tcSym_CaptureSourceFile.setOutputName("plib_tc" + tcInstanceIndex + ".c")
    tcSym_CaptureSourceFile.setDestPath("/peripheral/tc/")
    tcSym_CaptureSourceFile.setProjectPath("config/" + configName + "/peripheral/tc/")
    tcSym_CaptureSourceFile.setType("SOURCE")
    tcSym_CaptureSourceFile.setMarkup(True)

    tcSym_SystemInitFile = tcComponent.createFileSymbol("TC_SYS_INT", None)
    tcSym_SystemInitFile.setType("STRING")
    tcSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tcSym_SystemInitFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/system/initialization.c.ftl")
    tcSym_SystemInitFile.setMarkup(True)

    tcSym_SystemDefFile = tcComponent.createFileSymbol("TC_SYS_DEF", None)
    tcSym_SystemDefFile.setType("STRING")
    tcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tcSym_SystemDefFile.setSourcePath("../peripheral/tc_" + tcModuleID + "/templates/system/definitions.h.ftl")
    tcSym_SystemDefFile.setMarkup(True)

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2249/config/tc_timer.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2249/config/tc_compare.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tc_u2249/config/tc_capture.py")