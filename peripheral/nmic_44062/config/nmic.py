"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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


def instantiateComponent(nmicComponent):
    global nmicInterruptEnabled

    # instance index
    nmicInstance = nmicComponent.createStringSymbol("NMIC_INSTANCE_NAME", None)
    nmicInstance.setVisible(False)
    nmicInstance.setDefaultValue(nmicComponent.getID().upper())

    numSource = 0
    captions = {}
    parametersNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NMIC\"]/instance@[name=\""+nmicInstance.getValue()+"\"]/parameters")
    for parameter in parametersNode.getChildren():
        if "NUM_NMIC_SOURCE" in parameter.getAttribute("name"):
            paramSym = nmicComponent.createIntegerSymbol(parameter.getAttribute("name"), None)
            paramSym.setVisible(False)
            paramSym.setDefaultValue(int(parameter.getAttribute("value")))
            numSource = int(parameter.getAttribute("value"))

        elif parameter.getAttribute("name").startswith("NMIC_SOURCE_"):
            paramSym = nmicComponent.createStringSymbol("NMIC_SOURCE_" + str(parameter.getAttribute("value")), None)
            paramSym.setVisible(False)
            paramSym.setDefaultValue(parameter.getAttribute("name"))
            captions["NMIC_SOURCE_" + str(parameter.getAttribute("value"))] = parameter.getAttribute("caption")

    NVICVector = nmicInstance.getValue() + "_INTERRUPT_ENABLE"
    NVICHandler = nmicInstance.getValue() + "_INTERRUPT_HANDLER"
    NVICHandlerLock = nmicInstance.getValue() + "_INTERRUPT_HANDLER_LOCK"

    nmicInterruptEnabled = nmicComponent.createHexSymbol("NMIC_INTERRUPT", None)
    nmicInterruptEnabled.setVisible(False)
    nmicInterruptEnabled.setDefaultValue(0)

    Database.setSymbolValue("core", nmicInstance.getValue().upper() + "_CLOCK_ENABLE", True, 2)

    Database.setSymbolValue("core", "NonMaskableInt_INTERRUPT_HANDLER", "NMIC_InterruptHandler", 2)

    for id in range(0, numSource):
        nmicSRCEnable = nmicComponent.createBooleanSymbol("NMIC_SRC_EN_" + str(id), None)
        nmicSRCEnable.setLabel(captions["NMIC_SOURCE_" + str(id)])
        nmicSRCEnable.setDefaultValue(False)

        nmicConfigurationMenu = nmicComponent.createMenuSymbol("NMIC_MENU_" + str(id), nmicSRCEnable)
        nmicConfigurationMenu.setLabel("NMIC Source Configuration")
        nmicConfigurationMenu.setDependencies(menuDisplay, ["NMIC_SRC_EN_" + str(id)])
        nmicConfigurationMenu.setVisible(False)

        nmicConfigurationLVL = nmicComponent.createKeyValueSetSymbol(("NMIC_SRC_" + str(id) + "_LVL"), nmicConfigurationMenu)
        nmicConfigurationLVL.setLabel("Level/Edge selection")
        nmicConfigurationLVL.setOutputMode("Value")
        nmicConfigurationLVL.setDisplayMode("Description")
        nmicConfigurationLVL.addKey("EDG", str(0), "Source interrupt status is set on valid edge")
        nmicConfigurationLVL.addKey("LVL", str(1), "Source interrupt status is set on valid level")
        nmicConfigurationLVL.setVisible(id == 0)

        nmicConfigurationPOL = nmicComponent.createKeyValueSetSymbol(("NMIC_SRC_" + str(id) + "_POL"), nmicConfigurationMenu)
        nmicConfigurationPOL.setLabel("Polarity selection")
        nmicConfigurationPOL.setOutputMode("Value")
        nmicConfigurationPOL.setDisplayMode("Description")
        nmicConfigurationPOL.addKey("LOW", str(0), "Falling edge / Low Level")
        nmicConfigurationPOL.addKey("HIGH", str(1), "Raising edge / High level")
        nmicConfigurationPOL.setVisible(id == 0)

        nmicGFEnable = nmicComponent.createBooleanSymbol("NMIC_SRC_GF_EN_" + str(id), nmicConfigurationMenu)
        nmicGFEnable.setLabel("Enable Glitch Filter")
        nmicGFEnable.setDefaultValue(False)
        nmicGFEnable.setVisible(id == 0)

        nmicGFSEL = nmicComponent.createIntegerSymbol("NMIC_SRC_GFSEL_" + str(id), nmicConfigurationMenu)
        nmicGFSEL.setLabel("Glitch Filter Selector")
        nmicGFSEL.setDefaultValue(1)
        nmicGFSEL.setMax(3)
        nmicGFSEL.setMin(0)
        nmicGFSEL.setDependencies(selectorDisplay, ["NMIC_SRC_GF_EN_" + str(id)])
        nmicGFSEL.setVisible(False)

        nmicGCLKComment = nmicComponent.createCommentSymbol("NMIC_GCLK_CMENT" + str(id), nmicConfigurationMenu)
        nmicGCLKComment.setLabel("***************** Configure Generick Clock Using Clock Manager**********")
        nmicGCLKComment.setVisible(False)
        nmicGCLKComment.setDependencies(gclkComment, ["NMIC_SRC_GF_EN_" + str(id)])

        nmicFZEnable = nmicComponent.createBooleanSymbol("NMIC_SRC_FZ_" + str(id), nmicConfigurationMenu)
        nmicFZEnable.setLabel("Freeze Configuration")
        nmicFZEnable.setDefaultValue(False)
        nmicFZEnable.setVisible(id == 0)

    configName = Variables.get("__CONFIGURATION_NAME")
    # Generate Output Header
    nmicHeaderFile = nmicComponent.createFileSymbol("NMIC_FILE_0", None)
    nmicHeaderFile.setSourcePath("../peripheral/nmic_44062/templates/plib_nmic.h.ftl")
    nmicHeaderFile.setMarkup(True)
    nmicHeaderFile.setOutputName("plib_" + nmicInstance.getValue().lower() + ".h")
    nmicHeaderFile.setOverwrite(True)
    nmicHeaderFile.setDestPath("peripheral/nmic/")
    nmicHeaderFile.setProjectPath("config/" + configName + "/peripheral/nmic/")
    nmicHeaderFile.setType("HEADER")
    # Generate Output source
    nmicSourceFile = nmicComponent.createFileSymbol("NMIC_FILE_1", None)
    nmicSourceFile.setSourcePath("../peripheral/nmic_44062/templates/plib_nmic.c.ftl")
    nmicSourceFile.setMarkup(True)
    nmicSourceFile.setOutputName("plib_" + nmicInstance.getValue().lower() + ".c")
    nmicSourceFile.setOverwrite(True)
    nmicSourceFile.setDestPath("peripheral/nmic/")
    nmicSourceFile.setProjectPath("config/" + configName + "/peripheral/nmic/")
    nmicSourceFile.setType("SOURCE")

    nmicSystemDefFile = nmicComponent.createFileSymbol("NMIC_FILE_2", None)
    nmicSystemDefFile.setType("STRING")
    nmicSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nmicSystemDefFile.setSourcePath("../peripheral/nmic_44062/templates/system/definitions.h.ftl")
    nmicSystemDefFile.setMarkup(True)

    nmicSystemInitFile = nmicComponent.createFileSymbol("NMIC_SYS_INIT", None)
    nmicSystemInitFile.setSourcePath("../peripheral/nmic_44062/templates/system/initialization.c.ftl")
    nmicSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    nmicSystemInitFile.setType("STRING")
    nmicSystemInitFile.setMarkup(True)


def menuDisplay(symbol, event):
    global nmicInterruptEnabled
    count = nmicInterruptEnabled.getValue()
    if event["id"] == "NMIC_SRC_EN_0":
        symbol.setVisible(event["value"])
    else:
        symbol.setVisible(False)
    if event["value"] == True:
        count |= 1 << (int(str(symbol.getID()).split("NMIC_MENU_")[1]))
    else:
        count &= ~(1 << (int(str(symbol.getID()).split("NMIC_MENU_")[1])))
    nmicInterruptEnabled.setValue(count, 2)


def selectorDisplay(symbol, event):
    symbol.setVisible(event["value"])


def gclkComment(symbol, event):
    symbol.setVisible(event["value"])
