################################################################################
################################# Component   ##################################
################################################################################
def instantiateComponent(pacComponent):

    pacInstanceIndex = pacComponent.getID()[-1:]

    bridgeNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PAC\"]/instance@[name=\"PAC\"]/parameters/param@[name=\"HPB_NUM\"]")

    bridgeCount = int(bridgeNode.getAttribute("value"))

    #pac main menu
    pacSym_Menu = pacComponent.createMenuSymbol("PAC_MENU", None)
    pacSym_Menu.setLabel("PAC MODULE SETTINGS ")

    pacSym_INDEX = pacComponent.createIntegerSymbol("PAC_INDEX", pacSym_Menu)
    pacSym_INDEX.setDefaultValue(int(pacInstanceIndex))
    pacSym_INDEX.setVisible(False)

    pacSym_BridgeCount = pacComponent.createIntegerSymbol("PAC_BRIDGE_COUNT", pacSym_Menu)
    pacSym_BridgeCount.setDefaultValue(bridgeCount)
    pacSym_BridgeCount.setVisible(False)

    #interrupt mode
    pacSym_INTENSET = pacComponent.createBooleanSymbol("PAC_INTERRRUPT_MODE", pacSym_Menu)
    pacSym_INTENSET.setLabel("Enable PAC Interrupt ?")
    pacSym_INTENSET.setDefaultValue(False)

    #Error Event
    pacSym_ErrEventSET = pacComponent.createBooleanSymbol("PAC_ERROR_EVENT", pacSym_Menu)
    pacSym_ErrEventSET.setLabel("Generate Peripheral Access Error Event")
    pacSym_ErrEventSET.setDefaultValue(False)
    pacSym_ErrEventSET.setVisible(False)

    for bridge in range(0 , bridgeCount):

        x = chr(ord("A") + bridge)

        PAC_bridgeSym = pacComponent.createStringSymbol("PAC_" + str(bridge) + "_BRIDGE" , pacSym_Menu)
        PAC_bridgeSym.setDefaultValue(str(x))
        PAC_bridgeSym.setVisible(False)

        bridgeXNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PAC\"]/register-group@[name=\"PAC\"]/register@[name=\"INTFLAG" + str(x) + "\"]")
        bridgeXPeripherals = []
        bridgeXPeripherals = bridgeXNode.getChildren()

        pacSym_BridgePeripheralCount = pacComponent.createIntegerSymbol("PAC_BRIDGE_" + str(bridge) + "_PERI_COUNT", pacSym_Menu)
        pacSym_BridgePeripheralCount.setDefaultValue(len(bridgeXPeripherals))
        pacSym_BridgePeripheralCount.setVisible(False)

        for bitfield in range(0 , len(bridgeXPeripherals)):

            periName = str(bridgeXPeripherals[bitfield].getAttribute("caption"))

            PAC_PeripheralSym = pacComponent.createStringSymbol("PAC_BRIDGE_" + str(bridge) + "_PERI_" + str(bitfield) + "_NAME" , pacSym_Menu)
            PAC_PeripheralSym.setDefaultValue(periName)
            PAC_PeripheralSym.setVisible(False)

            PAC_SelectionSym = pacComponent.createKeyValueSetSymbol("PAC_BRIDGE_" + str(bridge) + "_PERI_" + str(bitfield) + "_REG_PROTECT" , pacSym_Menu)
            PAC_SelectionSym.setLabel(periName + " Peripheral Registers Protection")

            PACNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PAC\"]/value-group@[name=\"PAC_WRCTRL__KEY\"]")
            PACValues = []
            PACValues = PACNode.getChildren()

            PACDefaultValue = 0

            for index in range(len(PACValues)):
                PACKeyName = PACValues[index].getAttribute("name")

                if (PACKeyName == "OFF"):
                    PACDefaultValue = index

                PACKeyDescription = PACValues[index].getAttribute("caption")
                PACKeyValue = PACValues[index].getAttribute("value")
                PAC_SelectionSym.addKey(PACKeyName, PACKeyValue , PACKeyDescription)

            PAC_SelectionSym.setDefaultValue(PACDefaultValue)
            PAC_SelectionSym.setOutputMode("Key")
            PAC_SelectionSym.setDisplayMode("Description")

################################################################################
#############             CODE GENERATION             ##########################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pacModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PAC\"]")
    pacModuleID = pacModuleNode.getAttribute("id")

    pacSym_HeaderFile = pacComponent.createFileSymbol("PAC_HEADER", None)
    pacSym_HeaderFile.setSourcePath("../peripheral/pac_u2120/templates/plib_pac.h.ftl")
    pacSym_HeaderFile.setOutputName("plib_pac" + str(pacInstanceIndex) + ".h")
    pacSym_HeaderFile.setDestPath("peripheral/pac/")
    pacSym_HeaderFile.setProjectPath("peripheral/pac/")
    pacSym_HeaderFile.setType("HEADER")
    pacSym_HeaderFile.setMarkup(True)

    pacSym_SourceFile = pacComponent.createFileSymbol("PAC_SOURCE", None)
    pacSym_SourceFile.setSourcePath("../peripheral/pac_u2120/templates/plib_pac.c.ftl")
    pacSym_SourceFile.setOutputName("plib_pac" + str(pacInstanceIndex) + ".c")
    pacSym_SourceFile.setDestPath("peripheral/pac/")
    pacSym_SourceFile.setProjectPath("peripheral/pac/")
    pacSym_SourceFile.setType("SOURCE")
    pacSym_SourceFile.setMarkup(True)

    pacSystemDefFile = pacComponent.createFileSymbol("PAC_SYS_DEF", None)
    pacSystemDefFile.setType("STRING")
    pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pacSystemDefFile.setSourcePath("../peripheral/pac_u2120/templates/system/definitions.h.ftl")
    pacSystemDefFile.setMarkup(True)
    
    pacSystemInitFile = pacComponent.createFileSymbol("PAC_SYS_INIT", None)
    pacSystemInitFile.setType("STRING")
    pacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pacSystemInitFile.setSourcePath("../peripheral/pac_u2120/templates/system/initialization.c.ftl")
    pacSystemInitFile.setMarkup(True)
