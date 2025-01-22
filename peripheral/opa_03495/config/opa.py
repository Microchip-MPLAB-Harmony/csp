import re

#Constants for Symbols

ENABLE_OPA               = "ENABLE_OPA"
UNITY_GAIN               = "UNITY_GAIN"
HIGH_POWER_ENABLE        = "HIGH_POWER_ENABLE"
POSITIVE_INPUT_CHANNEL   = "POSITIVE_INPUT_CHANNEL"
NEGATIVE_INPUT_CHANNEL   = "NEGATIVE_INPUT_CHANNEL"
OUTPUT_CHANNEL           = "OUTPUT_CHANNEL"
CONFIGURE_PIN            = "CONFIGURE_PIN"
OUTPUT_MONITOR_SUPPORT   = "OUTPUT_MONITOR_SUPPORT"
INPUT_MONITOR_SUPPORT    = "INPUT_MONITOR_SUPPORT"
OPA_IOMONITOR_AVAILABLE  = "OPA_IOMONITOR_AVAILABLE"

MODULE_NAME              = "OPA"

# Callbacks

def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
    # Path to the register node in the ATDF structure
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, register_group, register
    )
    # Retrieve the register node
    register_node = ATDF.getNode(reg_path)

    # If the register node is found, fetch and return the initval as hex; otherwise, return "0x0UL"
    if register_node is not None:
        reg_default_val = register_node.getAttribute("initval")
        return "{}UL".format(reg_default_val) if reg_default_val else "0x0UL"
    return "0x0UL"

def generateDefineMacros(offsetCorrectionList):
    res = []
    for offset in range(min(31, len(offsetCorrectionList))):
        offsetCaption = offsetCorrectionList[offset].getAttribute("caption")
        offsetValue = str(offsetCorrectionList[offset].getAttribute("value"))
        template = "{} = {},".format(offsetCaption, offsetValue)
        res.append(template)
    return "\n".join(res)

parametersNode = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="OPA"]')

parameterNodes = [parametersNode]
positiveChannels = []
negativeChannels = []
outputChannels = []

for node in parameterNodes:
    parameters = node.getChildren()
    for param in parameters:
        opampInstance = param.getAttribute("name")
        match = re.search(r'AMP(\d+)', opampInstance)
        if match:
            instanceNumber = match.group(1)
            positiveChannel = "OA" + instanceNumber + "IN+"
            negativeChannel = "OA" + instanceNumber + "IN-"
            outputChannel = "OA" + instanceNumber + "OUT"

            positiveChannels.append(positiveChannel)
            negativeChannels.append(negativeChannel)
            outputChannels.append(outputChannel)

def getOpampInstanceCount(instanceNumber):
   return instanceNumber

opampInstanceCount = getOpampInstanceCount(instanceNumber)

def instantiateComponent(opampComponent):

    enableOpa = opampComponent.createBooleanSymbol(ENABLE_OPA, None)
    enableOpa.setLabel("Enable OPA During Initialization")
    enableOpa.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opa_03495;register:AMPxCON1")

    unityGainEnable = opampComponent.createBooleanSymbol(UNITY_GAIN, None)
    unityGainEnable.setLabel("Unity Gain")
    unityGainEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opa_03495;register:AMPxCON1")

    highPowerMode = opampComponent.createBooleanSymbol(HIGH_POWER_ENABLE, None)
    highPowerMode.setLabel("High Power Mode")
    highPowerMode.setDefaultValue(True)
    highPowerMode.setVisible(False)
    highPowerMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opa_03495;register:AMPxCON1")

    opampID = opampComponent.getID()

    positiveInputChannel = opampComponent.createComboSymbol(POSITIVE_INPUT_CHANNEL,  None, positiveChannels)
    positiveInputChannel.setLabel("OPA Positive Input Channel")
    index = int(opampID[-1]) - 1  
    if index < opampInstanceCount and index < len(positiveChannels):
         positiveInputChannel.setDefaultValue(positiveChannels[index])
    positiveInputChannel.setReadOnly(True)

    negativeInputChannel = opampComponent.createComboSymbol(NEGATIVE_INPUT_CHANNEL, None, negativeChannels)
    negativeInputChannel.setLabel("OPA Negative Input Channel")
    index = int(opampID[-1]) - 1  
    if index < opampInstanceCount and index < len(negativeChannels):
         negativeInputChannel.setDefaultValue(negativeChannels[index])
    negativeInputChannel.setReadOnly(True)
    
    outputChannel = opampComponent.createComboSymbol(OUTPUT_CHANNEL, None, outputChannels)
    outputChannel.setLabel("OPA Output Channel")
    index = int(opampID[-1]) - 1  
    if index < opampInstanceCount and index < len(outputChannels):
         outputChannel.setDefaultValue(outputChannels[index])
    outputChannel.setReadOnly(True)

    configurePins = opampComponent.createCommentSymbol(CONFIGURE_PIN, None)
    configurePins.setLabel("*** Configure Pins from Pin Manager ***")

    settingBitIMONEN = getBitField(MODULE_NAME,"AMP","CON1","IMONEN")
    if settingBitIMONEN != None:
        enableInputMonitor = opampComponent.createBooleanSymbol(INPUT_MONITOR_SUPPORT, None)
        enableInputMonitor.setLabel("Enable Input Monitor")
        enableInputMonitor.setDefaultValue(False)
        enableInputMonitor.setVisible(False)
        enableInputMonitor.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opa_03495;register:AMPxCON1")

    settingBitOMONEN = getBitField(MODULE_NAME,"AMP","CON1","OMONEN")
    if settingBitOMONEN != None:
        enableOutputMonitor = opampComponent.createBooleanSymbol(OUTPUT_MONITOR_SUPPORT, None)
        enableOutputMonitor.setLabel("Enable Output Monitor")
        enableOutputMonitor.setDefaultValue(False)
        enableOutputMonitor.setVisible(False)
        enableOutputMonitor.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:opa_03495;register:AMPxCON1")

    if settingBitIMONEN is not None and settingBitOMONEN is not None:
        ioMonitorFeatureAvailable = opampComponent.createBooleanSymbol(OPA_IOMONITOR_AVAILABLE, None)
        ioMonitorFeatureAvailable.setDefaultValue(True)
        ioMonitorFeatureAvailable.setVisible(False)


######### Code Generation ###########

    opampInstance = opampComponent.createStringSymbol("OPAMP_INSTANCE", None)
    opampInstance.setVisible(False)
    opampInstance.setDefaultValue(opampComponent.getID().upper().replace("AMP",""))

    moduleName = opampComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue("OPA"+opampInstance.getValue())
    moduleName.setVisible(False)

    con1regPor = opampComponent.createStringSymbol("CON1_REG_POR", None)
    con1regPor.setDefaultValue(getRegisterDefaultValue("OPA", "AMP", "CON1"))
    con1regPor.setVisible(False)

    con2regPor = opampComponent.createStringSymbol("CON2_REG_POR", None)
    con2regPor.setDefaultValue(getRegisterDefaultValue("OPA", "AMP", "CON2"))
    con2regPor.setVisible(False)

    valueGroupNode_offSet = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OPA"]/value-group@[name="AMP_CON2__NOFFSETLP"]')
    offsetCorrectionList = valueGroupNode_offSet.getChildren()

    offsetCorrection = opampComponent.createStringSymbol("OFFSET_CORRECTION", None)
    offsetCorrection.setDefaultValue(generateDefineMacros(offsetCorrectionList))
    offsetCorrection.setVisible(False)

#File Handling   
 
    configName = Variables.get("__CONFIGURATION_NAME")
    
    opaCommonHeaderFile = opampComponent.createFileSymbol("OPAMP_COMMON_HEADER", None)
    opaCommonHeaderFile.setSourcePath("../peripheral/opa_03495/templates/plib_opa_common.h.ftl")
    opaCommonHeaderFile.setOutputName("plib_opa_common.h")
    opaCommonHeaderFile.setDestPath("peripheral/opa/")
    opaCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/opa/")
    opaCommonHeaderFile.setType("HEADER")
    opaCommonHeaderFile.setMarkup(True)
    opaCommonHeaderFile.setOverwrite(True)

    opaHeaderFile = opampComponent.createFileSymbol("OPA_HEADER", None)
    opaHeaderFile.setSourcePath("../peripheral/opa_03495/templates/plib_opa.h.ftl")
    opaHeaderFile.setOutputName("plib_" + moduleName.getValue().lower() + ".h")
    opaHeaderFile.setDestPath("/peripheral/opa/")
    opaHeaderFile.setProjectPath("config/" + configName + "/peripheral/opa/")
    opaHeaderFile.setType("HEADER")
    opaHeaderFile.setOverwrite(True)
    opaHeaderFile.setMarkup(True)
    
    opaSourceFile = opampComponent.createFileSymbol("OPA_SOURCE", None)
    opaSourceFile.setSourcePath("../peripheral/opa_03495/templates/plib_opa.c.ftl")
    opaSourceFile.setOutputName("plib_" + moduleName.getValue().lower() + ".c")
    opaSourceFile.setDestPath("/peripheral/opa/")
    opaSourceFile.setProjectPath("config/" + configName + "/peripheral/opa/")
    opaSourceFile.setType("SOURCE")
    opaSourceFile.setOverwrite(True)
    opaSourceFile.setMarkup(True)
    
    opaSystemInitFile = opampComponent.createFileSymbol("OPA_INIT", None)
    opaSystemInitFile.setType("STRING")
    opaSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    opaSystemInitFile.setSourcePath("../peripheral/opa_03495/templates/system/initialization.c.ftl")
    opaSystemInitFile.setMarkup(True)

    opaSystemDefFile = opampComponent.createFileSymbol("OPA_DEF", None)
    opaSystemDefFile.setType("STRING")
    opaSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    opaSystemDefFile.setSourcePath("../peripheral/opa_03495/templates/system/definitions.h.ftl")
    opaSystemDefFile.setMarkup(True)