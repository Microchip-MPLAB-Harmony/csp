RCON_ENABLE_SYMBOL = "RCON_ENABLE"
RCON_CAUSE_COUNT_SYMBOL = "RCON_CAUSE_COUNT"

################# Symbol creation #############################################

def instantiateComponent(rconComponent):

    rcon_Enable = rconComponent.createBooleanSymbol(RCON_ENABLE_SYMBOL, None)
    rcon_Enable.setLabel("Use Resets ")
    rcon_Enable.setDefaultValue(True)
    rcon_Enable.setReadOnly(True)

    rcon_Instance = rconComponent.createStringSymbol("RCON_INSTANCE_NAME", None) 
    rcon_Instance.setVisible(False)
    rcon_Instance.setDefaultValue(rconComponent.getID().upper())

    rconRegister = ATDF.getNode('/avr-tools-device-file/modules/module@[name="rcon"]/register-group@[name="RCON"]/register@[name="RCON"]')

    bitfieldCount = 0

    # Iterate through the bitfields of the RCON register
    for bitfield in rconRegister.getChildren():
      bitfieldName = bitfield.getAttribute("name")
      bitfieldCount += 1
      if bitfieldName == "CM":
        break
    
    rcon_ResetCount = rconComponent.createIntegerSymbol(RCON_CAUSE_COUNT_SYMBOL, None)
    rcon_ResetCount.setDefaultValue(bitfieldCount)
    rcon_ResetCount.setVisible(False)
 
    for resetCause in range(len(rconRegister.getChildren())):
        rcon_Cause = rconComponent.createKeyValueSetSymbol("RCON_CAUSE_" + str(resetCause), None)
        rcon_Cause.setLabel(str(rconRegister.getChildren()[resetCause].getAttribute("name")))
        rcon_Cause.addKey(rconRegister.getChildren()[resetCause].getAttribute("name"), str(resetCause), rconRegister.getChildren()[resetCause].getAttribute("name"))
        rcon_Cause.setOutputMode("Key")
        rcon_Cause.setDisplayMode("Description")
        rcon_Cause.setVisible(False)
        rcon_Cause.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rcon_04449;register:RCON")

############################ Code Generation #####################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rcon_HeaderFile = rconComponent.createFileSymbol("RCON_HEADER", None)
    rcon_HeaderFile.setSourcePath("../peripheral/rcon/templates/plib_rcon.h.ftl")
    rcon_HeaderFile.setOutputName("plib_" + rcon_Instance.getValue().lower() + ".h")
    rcon_HeaderFile.setDestPath("peripheral/rcon/")
    rcon_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rcon/")
    rcon_HeaderFile.setType("HEADER")
    rcon_HeaderFile.setMarkup(True)

    rcon_SourceFile = rconComponent.createFileSymbol("RCON_SOURCE", None)
    rcon_SourceFile.setSourcePath("../peripheral/rcon/templates/plib_rcon.c.ftl")
    rcon_SourceFile.setOutputName("plib_" + rcon_Instance.getValue().lower() + ".c")
    rcon_SourceFile.setDestPath("peripheral/rcon/")
    rcon_SourceFile.setProjectPath("config/" + configName + "/peripheral/rcon/")
    rcon_SourceFile.setType("SOURCE")
    rcon_SourceFile.setMarkup(True)

    rcon_SystemDefFile = rconComponent.createFileSymbol("RCON_SYS_DEF", None)
    rcon_SystemDefFile.setType("STRING")
    rcon_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rcon_SystemDefFile.setSourcePath("../peripheral/rcon/templates/system/definitions.h.ftl")
    rcon_SystemDefFile.setMarkup(True)
