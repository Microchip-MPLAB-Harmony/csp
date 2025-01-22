import re
from collections import OrderedDict

#ATDF Callbacks
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

# Callbacks
def updateSource(symbol, event):
    symbol.setVisible(event["value"])

def updateSourceType(symbol, event):
    symbol_id_suffix = symbol.getID()[-1]
    event_value = event["value"]

    if event_value == "ISRC{}".format(symbol_id_suffix):
        if "ISR_VALUE" in symbol.getID():
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    elif event_value == "IBIAS{}".format(symbol_id_suffix):
        if "IBIAS_VALUE" in symbol.getID():
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        symbol.setVisible(False)


valueGroupNode_ISELOUT0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CBG"]/value-group@[name="IBIASCON_IBIASCON__ISELOUT0"]')
valueNodes = valueGroupNode_ISELOUT0.getChildren()

# To Remove Duplicates and zero 
caption_value_dict = {
    int(node.getAttribute("caption").split()[0]): node.getAttribute("value")
    for node in valueNodes
    if int(node.getAttribute("caption").split()[0]) != 0
}
sorted_caption_value_dict = OrderedDict(sorted(caption_value_dict.items()))

def handleMessage(messageID, args):
    retDict = {}
    if (messageID == "CBG_CONFIG_HW_IO"):
        component = "cbg"
        setting, enable = args['config']

        channel = "".join(filter(lambda x: x.isdigit(), setting))

        symbolName = "USE_ISCR{}".format(channel)
        symbolTypeName = "SOURCE_TYPE{}".format(channel)

        if enable == False:
            res = Database.clearSymbolValue(component, symbolName)
            res = Database.clearSymbolValue(component, symbolTypeName)
        else:
            res = Database.setSymbolValue(component, symbolName, enable)
            if "ibias" in setting.lower():
                srcValue = "IBIAS{}".format(channel)
            else:
                srcValue = "ISRC{}".format(channel)
            res = Database.setSymbolValue(component, symbolTypeName, srcValue)
        
        if res == True:
            retDict = {"Result": "Success"}
        else:
            retDict = {"Result": "Fail"}
            
    else:
        retDict= {"Result": "ADC UnImplemented Command"}
    
    return retDict

def instantiateComponent(cbgComponent):

    current_quantity = cbgComponent.createIntegerSymbol("CURRENT_QUANTITY", None)
    current_quantity.setLabel("Number of Currents")
    current_quantity.setDefaultValue(4)
    current_quantity.setVisible(False)

    for i in range(current_quantity.getValue()):

        sourceTypes = "USE_ISCR{}".format(i)
        useISRC = cbgComponent.createBooleanSymbol(sourceTypes, None)
        useISRC.setLabel("Use ISRC{} Or IBIAS{}".format(i, i))
        useISRC.setDefaultValue(False)

        sourceTypeName = "SOURCE_TYPE{}".format(i)
        currentSourceType = cbgComponent.createComboSymbol(sourceTypeName, useISRC, ["ISRC{}".format(i), "IBIAS{}".format(i)])
        currentSourceType.setLabel("Current Source Type")
        currentSourceType.setDefaultValue("ISRC{}".format(i))
        currentSourceType.setVisible(useISRC.getValue())
        currentSourceType.setDependencies(updateSource, [sourceTypes])

        isrcName = "ISR_VALUE{}".format(i)
        isrcValue = cbgComponent.createIntegerSymbol(isrcName, currentSourceType)
        isrcValue.setLabel("ISRC Value(uA)")
        isrcValue.setDefaultValue(10)
        isrcValue.setReadOnly(True)
        isrcValue.setVisible(currentSourceType.getValue() == "ISRC{}".format(i))
        isrcValue.setDependencies(updateSourceType, [sourceTypeName])
        isrcValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:cbg_03516;register:IBIASCON")

        ibiasName = "IBIAS_VALUE{}".format(i)
        ibiasValue = cbgComponent.createKeyValueSetSymbol(ibiasName, currentSourceType)
        ibiasValue.setLabel("IBIAS Value(uA)")
        ibiasValue.setOutputMode("Value")
        ibiasValue.setDisplayMode("Description")
        for caption, value in sorted_caption_value_dict.items():
           ibiasValue.addKey(str(caption), value, str(caption))
        ibiasValue.setVisible(currentSourceType.getValue() == "IBIAS{}".format(i))
        ibiasValue.setDependencies(updateSourceType, [sourceTypeName])
        ibiasValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:cbg_03516;register:IBIASCON")

    configurePins = cbgComponent.createCommentSymbol("CONFIGURE_PIN", None)
    configurePins.setLabel("*** Configure ISRC/IBIAS Pins from Pin Manager ***")
    
    # Code Generation

    cbgInstance = cbgComponent.createStringSymbol("CBG_INSTANCE", None)
    cbgInstance.setVisible(False)
    cbgInstance.setDefaultValue(cbgComponent.getID().upper())

    ibiasconRegPor = cbgComponent.createStringSymbol("IBIAS_CON_REG_POR", None)
    ibiasconRegPor.setDefaultValue(getRegisterDefaultValue("CBG", "IBIASCON", "IBIASCON"))
    ibiasconRegPor.setVisible(False)

    # File Handling

    configName = Variables.get("__CONFIGURATION_NAME")

    cbgHeaderFile = cbgComponent.createFileSymbol("CBG_HEADER", None)
    cbgHeaderFile.setSourcePath("../peripheral/cbg_03516/templates/plib_cbg.h.ftl")
    cbgHeaderFile.setOutputName("plib_" + cbgInstance.getValue().lower() + ".h")
    cbgHeaderFile.setDestPath("/peripheral/cbg/")
    cbgHeaderFile.setProjectPath("config/" + configName + "/peripheral/cbg/")
    cbgHeaderFile.setType("HEADER")
    cbgHeaderFile.setOverwrite(True)
    cbgHeaderFile.setMarkup(True)
    
    cbgSourceFile = cbgComponent.createFileSymbol("CBG_SOURCE", None)
    cbgSourceFile.setSourcePath("../peripheral/cbg_03516/templates/plib_cbg.c.ftl")
    cbgSourceFile.setOutputName("plib_" + cbgInstance.getValue().lower() + ".c")
    cbgSourceFile.setDestPath("/peripheral/cbg/")
    cbgSourceFile.setProjectPath("config/" + configName + "/peripheral/cbg/")
    cbgSourceFile.setType("SOURCE")
    cbgSourceFile.setOverwrite(True)
    cbgSourceFile.setMarkup(True)
    
    cbgSystemInitFile = cbgComponent.createFileSymbol("CBG_INIT", None)
    cbgSystemInitFile.setType("STRING")
    cbgSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cbgSystemInitFile.setSourcePath("../peripheral/cbg_03516/templates/system/initialization.c.ftl")
    cbgSystemInitFile.setMarkup(True)

    cbgSystemDefFile = cbgComponent.createFileSymbol("CBG_DEF", None)
    cbgSystemDefFile.setType("STRING")
    cbgSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cbgSystemDefFile.setSourcePath("../peripheral/cbg_03516/templates/system/definitions.h.ftl")
    cbgSystemDefFile.setMarkup(True)