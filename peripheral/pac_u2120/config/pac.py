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

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global pacInstanceName

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def updatePACInterruptStatus(symbol, event):

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler, pacInstanceName.getValue() + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, pacInstanceName.getValue() + "_Handler", 2)

def updatePACInterruptWarringStatus(symbol, event):

    if pacSym_INTENSET.getValue() == True:
        symbol.setVisible(event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pacComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global pacInstanceName
    global pacSym_INTENSET

    pacInstanceName = pacComponent.createStringSymbol("PAC_INSTANCE_NAME", None)
    pacInstanceName.setVisible(False)
    pacInstanceName.setDefaultValue(pacComponent.getID().upper())

    bridgeNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PAC\"]/instance@[name=\"" + pacInstanceName.getValue() + "\"]/parameters/param@[name=\"HPB_NUM\"]")

    bridgeCount = int(bridgeNode.getAttribute("value"))

    pacSym_BridgeCount = pacComponent.createIntegerSymbol("PAC_BRIDGE_COUNT", None)
    pacSym_BridgeCount.setDefaultValue(bridgeCount)
    pacSym_BridgeCount.setVisible(False)

    #interrupt mode
    pacSym_INTENSET = pacComponent.createBooleanSymbol("PAC_INTERRRUPT_MODE", None)
    pacSym_INTENSET.setLabel("Enable PAC Interrupt?")
    pacSym_INTENSET.setDefaultValue(True)

    #Error Event
    pacSym_ErrEventSET = pacComponent.createBooleanSymbol("PAC_ERROR_EVENT", None)
    pacSym_ErrEventSET.setLabel("Generate Peripheral Access Error Event Output")

    for bridge in range(0, bridgeCount):

        x = chr(ord("A") + bridge)

        pacSym_Bridge = pacComponent.createStringSymbol("PAC_" + str(bridge) + "_BRIDGE", None)
        pacSym_Bridge.setDefaultValue(str(x))
        pacSym_Bridge.setVisible(False)

        bridgeXNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PAC\"]/register-group@[name=\"" + pacInstanceName.getValue() + "\"]/register@[name=\"INTFLAG" + str(x) + "\"]")
        bridgeXPeripherals = []
        bridgeXPeripherals = bridgeXNode.getChildren()

        pacSym_BridgePeripheralCount = pacComponent.createIntegerSymbol("PAC_BRIDGE_" + str(bridge) + "_PERI_COUNT", None)
        pacSym_BridgePeripheralCount.setDefaultValue(len(bridgeXPeripherals))
        pacSym_BridgePeripheralCount.setVisible(False)

        for bitfield in range(0, len(bridgeXPeripherals)):

            periName = str(bridgeXPeripherals[bitfield].getAttribute("caption"))

            pacSym_PeriName = pacComponent.createStringSymbol("PAC_BRIDGE_" + str(bridge) + "_PERI_" + str(bitfield) + "_NAME", None)
            pacSym_PeriName.setDefaultValue(periName)
            pacSym_PeriName.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = pacInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = pacInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = pacInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = pacInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for Interrupt
    Database.setSymbolValue("core", InterruptVector, True, 2)
    Database.setSymbolValue("core", InterruptHandler, pacInstanceName.getValue() + "_InterruptHandler", 2)
    Database.setSymbolValue("core", InterruptHandlerLock, True, 2)

    # Interrupt Dynamic settings
    pacSym_UpdateInterruptStatus = pacComponent.createBooleanSymbol("PAC_INTERRUPT_STATUS", None)
    pacSym_UpdateInterruptStatus.setDependencies(updatePACInterruptStatus, ["PAC_INTERRRUPT_MODE"])
    pacSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    pacSym_IntEnComment = pacComponent.createCommentSymbol("PAC_INTERRUPT_ENABLE_COMMENT", None)
    pacSym_IntEnComment.setVisible(False)
    pacSym_IntEnComment.setLabel("Warning!!! PAC Interrupt is Disabled in Interrupt Manager")
    pacSym_IntEnComment.setDependencies(updatePACInterruptWarringStatus, ["core." + InterruptVectorUpdate])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pacModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PAC\"]")
    pacModuleID = pacModuleNode.getAttribute("id")

    pacSym_CommonHeaderFile = pacComponent.createFileSymbol("PAC_COMMON_HEADER", None)
    pacSym_CommonHeaderFile.setSourcePath("../peripheral/pac_" + pacModuleID + "/templates/plib_pac_common.h")
    pacSym_CommonHeaderFile.setOutputName("plib_pac_common.h")
    pacSym_CommonHeaderFile.setDestPath("/peripheral/pac/")
    pacSym_CommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/pac/")
    pacSym_CommonHeaderFile.setType("HEADER")
    pacSym_CommonHeaderFile.setMarkup(True)

    pacSym_HeaderFile = pacComponent.createFileSymbol("PAC_HEADER", None)
    pacSym_HeaderFile.setSourcePath("../peripheral/pac_" + pacModuleID + "/templates/plib_pac.h.ftl")
    pacSym_HeaderFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".h")
    pacSym_HeaderFile.setDestPath("/peripheral/pac/")
    pacSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pac/")
    pacSym_HeaderFile.setType("HEADER")
    pacSym_HeaderFile.setMarkup(True)

    pacSym_SourceFile = pacComponent.createFileSymbol("PAC_SOURCE", None)
    pacSym_SourceFile.setSourcePath("../peripheral/pac_" + pacModuleID + "/templates/plib_pac.c.ftl")
    pacSym_SourceFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".c")
    pacSym_SourceFile.setDestPath("/peripheral/pac/")
    pacSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pac/")
    pacSym_SourceFile.setType("SOURCE")
    pacSym_SourceFile.setMarkup(True)

    pacSystemDefFile = pacComponent.createFileSymbol("PAC_SYS_DEF", None)
    pacSystemDefFile.setType("STRING")
    pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pacSystemDefFile.setSourcePath("../peripheral/pac_" + pacModuleID + "/templates/system/definitions.h.ftl")
    pacSystemDefFile.setMarkup(True)

    pacSystemInitFile = pacComponent.createFileSymbol("PAC_SYS_INIT", None)
    pacSystemInitFile.setType("STRING")
    pacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pacSystemInitFile.setSourcePath("../peripheral/pac_" + pacModuleID + "/templates/system/initialization.c.ftl")
    pacSystemInitFile.setMarkup(True)
