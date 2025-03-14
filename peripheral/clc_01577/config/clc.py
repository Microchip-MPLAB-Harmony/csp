# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2020 Microchip Technology Inc. and its subsidiaries.
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

def getBitField(moduleName, registerGroup, register, bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

def addKeyValueSetFromATDF(symbol, moduleName, valueGroupName, namePrefix=""):
    atdf_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/value-group@[name=\"{1}\"]".format(moduleName, valueGroupName)
    node = ATDF.getNode(atdf_path)
    value = node.getChildren()
    for index in range(len(value)):
        name = value[index].getAttribute("name") if value[index].getAttribute("name") else namePrefix + str(index)
        symbol.addKey(name,
                      value[index].getAttribute("value"),
                      value[index].getAttribute("caption"))


def configureInterrupt(symbol, event):
    global interruptList

    coreComponent = Database.getComponentByID("core")
    clcComponentID = event["source"].getSymbolValue("CLC_INSTANCE_NAME")
    if (Database.getSymbolValue("core", "CoreArchitecture") == "PIC32A" or
        Database.getSymbolValue("core", "CoreArchitecture") == "dsPIC33A"):
        if event["value"] != "Disabled":
            if event["value"] == "Rising Edge":
                coreComponent.setSymbolValue("INTC_" + getVectorIndex(interruptList[0]) + "_ENABLE", True)
                coreComponent.setSymbolValue("INTC_" + getVectorIndex(interruptList[0]) + "_HANDLER_LOCK", True)
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interruptList[1]) + "_ENABLE")
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interruptList[1]) + "_HANDLER_LOCK")
            elif event["value"] == "Falling Edge":
                coreComponent.setSymbolValue("INTC_" + getVectorIndex(interruptList[1]) + "_ENABLE", True)
                coreComponent.setSymbolValue("INTC_" + getVectorIndex(interruptList[1]) + "_HANDLER_LOCK", True)
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interruptList[0]) + "_ENABLE")
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interruptList[0]) + "_HANDLER_LOCK")
            else:
                for interrupt in interruptList:
                    coreComponent.setSymbolValue("INTC_" + getVectorIndex(interrupt) + "_ENABLE", True)
                    coreComponent.setSymbolValue("INTC_" + getVectorIndex(interrupt) + "_HANDLER_LOCK", True)
            event["source"].setSymbolValue("CLC_LOGIC_CELL_ENABLE", False)
        else:
            for interrupt in interruptList:
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interrupt) + "_ENABLE")
                coreComponent.clearSymbolValue("INTC_" + getVectorIndex(interrupt) + "_HANDLER_LOCK")
            event["source"].clearSymbolValue("CLC_LOGIC_CELL_ENABLE")
    else:
        clcVectorID = clcComponentID + "_INTERRUPT_ENABLE"
        clcHandlerID = clcComponentID + "_INTERRUPT_HANDLER"
        clcHandlerLockID = clcComponentID + "_INTERRUPT_HANDLER_LOCK"
        if event["value"] != "Disabled":
            coreComponent.setSymbolValue(clcVectorID, True)
            coreComponent.setSymbolValue(clcHandlerID, clcComponentID + "_InterruptHandler")
            coreComponent.setSymbolValue(clcHandlerLockID, True)
            event["source"].setSymbolValue("CLC_LOGIC_CELL_ENABLE", False)
        else:
            coreComponent.clearSymbolValue(clcVectorID)
            coreComponent.clearSymbolValue(clcHandlerID)
            coreComponent.clearSymbolValue(clcHandlerLockID)
            event["source"].clearSymbolValue("CLC_LOGIC_CELL_ENABLE")

def updateInterruptStatus(symbol, event):
    global interruptEnableList

    if (Database.getSymbolValue("core", "CoreArchitecture") == "PIC32A" or
        Database.getSymbolValue("core", "CoreArchitecture") == "dsPIC33A"):
        if ((event["source"].getSymbolValue("CLC_INTERRUPT_TYPE") != "Disabled") and
            (Database.getSymbolValue("core", interruptEnableList[0].replace("core.", "")) == False) and
            (Database.getSymbolValue("core", interruptEnableList[1].replace("core.", "")) == False)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        if ((event["source"].getSymbolValue("CLC_INTERRUPT_TYPE") != "Disabled") and
            (Database.getSymbolValue("core",
                                     event["source"].getSymbolValue("CLC_INSTANCE_NAME") +"_INTERRUPT_ENABLE_UPDATE"))):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def updateClcClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])


def instantiateComponent(clcComponent):
    global interruptList
    global interruptEnableList

    interruptList = []
    interruptEnableList = []

    clcInstanceName = clcComponent.createStringSymbol("CLC_INSTANCE_NAME", None)
    clcInstanceName.setVisible(False)
    clcInstanceName.setDefaultValue(clcComponent.getID().upper())
    clcID = clcComponent.getID().split("clc")[1]

    Log.writeInfoMessage("Running " + clcInstanceName.getValue())

    if (Database.getSymbolValue("core", "CoreArchitecture") == "PIC32A" or
        Database.getSymbolValue("core", "CoreArchitecture") == "dsPIC33A"):
        interruptList = [clcInstanceName.getValue() + "PInterrupt" , clcInstanceName.getValue() + "NInterrupt"]
        for interrupt in interruptList:
            interruptEnableList.append("core.INTC_" + getVectorIndex(interrupt) + "_ENABLE")
    else:
        interruptList = [clcInstanceName.getValue()]
        # Enable clock
        Database.setSymbolValue("core", clcInstanceName.getValue() + "_CLOCK_ENABLE", True)

        clcSymClkEnComment = clcComponent.createCommentSymbol("CLC_CLOCK_ENABLE_COMMENT", None)
        clcSymClkEnComment.setLabel("Warning!!! " + clcInstanceName.getValue() + " peripheral clock is disabled in Clock Manager")
        clcSymClkEnComment.setVisible(False)
        clcSymClkEnComment.setDependencies(updateClcClockWarningStatus, ["core." + clcInstanceName.getValue() + "_CLOCK_ENABLE"])

    clcDSMenu = clcComponent.createMenuSymbol("CLC_DATA_SOURCES_MENU", None)
    clcDSMenu.setLabel("Data Sources")
    for dsCount in range(1,5):
        clcSourceSelection = clcComponent.createKeyValueSetSymbol("CLC_DS{0}_OUTPUT".format(dsCount), clcDSMenu)
        clcSourceSelection.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1SEL")
        clcSourceSelection.setLabel("Data Source {0}".format(dsCount))
        addKeyValueSetFromATDF(clcSourceSelection, "CLC", getValueGroupName("CLC", "CLC", "CLC{0}SEL".format(clcID), "DS{0}".format(dsCount)), "SEL__DS")
        clcSourceSelection.setDefaultValue(0)
        clcSourceSelection.setDisplayMode("Description")
        clcSourceSelection.setOutputMode("Value")
        for index in range (0 , clcSourceSelection.getKeyCount()):
            if int(clcSourceSelection.getKeyValue(index), 16) == 0:
                clcSourceSelection.setDefaultValue(index)
                break

    clcGatesMenu = clcComponent.createMenuSymbol("CLC_GATES_MENU", None)
    clcGatesMenu.setLabel("Gates")
    for gateCount in range(1,5):
        clcGateMenu = clcComponent.createMenuSymbol("CLC_GATE{0}_MENU".format(gateCount), clcGatesMenu)
        clcGateMenu.setLabel("Gate {0}".format(gateCount))

        clcGateInputMenu = clcComponent.createMenuSymbol("CLC_GATE{0}_INPUT_MENU".format(gateCount), clcGateMenu)
        clcGateInputMenu.setLabel("Inputs (Ouput is logical OR of all enabled inputs)")
        for dsCount in range(1, 5):
            clcGateInput = clcComponent.createBooleanSymbol("CLC_GATE{0}_DS{1}_ENABLE".format(gateCount, dsCount),clcGateInputMenu)
            clcGateInput.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1SEL")
            clcGateInput.setLabel("Enable Data Source {0}".format(dsCount))

            clcGateInputNeg = clcComponent.createBooleanSymbol("CLC_GATE{0}_DS{1}_NEG_ENABLE".format(gateCount, dsCount), clcGateInputMenu)
            clcGateInputNeg.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1SEL")
            clcGateInputNeg.setLabel("Enable Data Source {0} inverted".format(dsCount))

        clcGateOutputPolarity = clcComponent.createBooleanSymbol("CLC_GATE{0}_OUTPUT_POLARITY".format(gateCount), clcGateMenu)
        clcGateOutputPolarity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1GLS")
        clcGateOutputPolarity.setLabel("Invert output".format(gateCount))

    clcLogicCellMenu = clcComponent.createMenuSymbol("CLC_LOGIC_CELL_MENU", None)
    clcLogicCellMenu.setLabel ("Logic Cell ")

    clcLogicCellEnable = clcComponent.createBooleanSymbol("CLC_LOGIC_CELL_ENABLE", clcLogicCellMenu)
    clcLogicCellEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1CON")
    clcLogicCellEnable.setLabel("Enable Logic Cell")
    clcLogicCellEnable.setDefaultValue(True)

    clcLogicCellMode = clcComponent.createKeyValueSetSymbol("CLC_LOGIC_CELL_MODE", clcLogicCellMenu)
    clcLogicCellMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1CON")
    clcLogicCellMode.setLabel("Mode")
    addKeyValueSetFromATDF(clcLogicCellMode, "CLC", getValueGroupName("CLC", "CLC", "CLC{0}CON".format(clcID), "MODE"), "CON__MODE")
    clcLogicCellMode.setDisplayMode("Description")
    clcLogicCellMode.setOutputMode("Value")
    for index in range (0 , clcLogicCellMode.getKeyCount()):
        if int(clcLogicCellMode.getKeyValue(index), 16) == 0:
            clcLogicCellMode.setDefaultValue(index)
            break

    clcLogicCellOutputPolarity = clcComponent.createBooleanSymbol("CLC_LOGIC_CELL_OUTPUT_POLARITY", clcLogicCellMenu)
    clcLogicCellOutputPolarity.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1CON")
    clcLogicCellOutputPolarity.setLabel("Invert output")

    clcLogicInterruptType = clcComponent.createComboSymbol("CLC_INTERRUPT_TYPE",clcLogicCellMenu,  ["Disabled", "Rising Edge", "Falling Edge", "Both Edge"])
    clcLogicInterruptType.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1CON")
    clcLogicInterruptType.setLabel("Enable Interrupt")
    clcLogicInterruptType.setDependencies(configureInterrupt, ["CLC_INTERRUPT_TYPE"])

    clcSymIntEnComment = clcComponent.createCommentSymbol("CLC_INTERRUPT_ENABLE_COMMENT", clcLogicCellMenu)
    clcSymIntEnComment.setLabel("Warning!!! " + clcInstanceName.getValue() + " interrupt is disabled in Interrupt Manager")
    clcSymIntEnComment.setVisible(False)
    clcSymIntEnComment.setDependencies(updateInterruptStatus, ["CLC_INTERRUPT_TYPE", "core." + clcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"] + interruptEnableList)

    clcSymIrqRegIndex = clcComponent.createStringSymbol("CLC_IRQ_REG_INDEX", clcLogicCellMenu)
    clcSymIrqRegIndex.setVisible(False)
    clcSymIrqRegIndex.setReadOnly(True)
    irqNode = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts/interrupt@[name=\"{0}\"]'.format(interruptList[0]))
    clcSymIrqRegIndex.setDefaultValue(str(int(irqNode.getAttribute("index"))/32))

    if len(interruptList) > 1:
        clcSymIrqRegIndex1 = clcComponent.createStringSymbol("CLC_IRQ_REG_INDEX1", clcLogicCellMenu)
        clcSymIrqRegIndex1.setVisible(False)
        clcSymIrqRegIndex1.setReadOnly(True)
        irqNode1 = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts/interrupt@[name=\"{0}\"]'.format(interruptList[1]))
        clcSymIrqRegIndex1.setDefaultValue(str(int(irqNode1.getAttribute("index"))/32))

    clcLogicPortEnable = clcComponent.createBooleanSymbol("CLC_PORT_ENABLE", clcLogicCellMenu)
    clcLogicPortEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clc_01577;register:CLC1CON")
    clcLogicPortEnable.setLabel("Enable output pin")

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    clcCommonHeaderFile = clcComponent.createFileSymbol("CLC_COMMON_HEADER", None)
    clcCommonHeaderFile.setSourcePath("../peripheral/clc_01577/templates/plib_clc_common.h")
    clcCommonHeaderFile.setOutputName("plib_clc_common.h")
    clcCommonHeaderFile.setDestPath("/peripheral/clc/")
    clcCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/clc/")
    clcCommonHeaderFile.setType("HEADER")
    clcCommonHeaderFile.setMarkup(False)

    clcHeaderFile = clcComponent.createFileSymbol("CLC_INSTANCE_HEADER", None)
    clcHeaderFile.setSourcePath("../peripheral/clc_01577/templates/plib_clc.h.ftl")
    clcHeaderFile.setOutputName("plib_" + clcInstanceName.getValue().lower() + ".h")
    clcHeaderFile.setDestPath("/peripheral/clc/")
    clcHeaderFile.setProjectPath("config/" + configName + "/peripheral/clc/")
    clcHeaderFile.setType("HEADER")
    clcHeaderFile.setMarkup(True)

    clcSourceFile = clcComponent.createFileSymbol("CLC_INSTANCE_SOURCE", None)
    clcSourceFile.setSourcePath("../peripheral/clc_01577/templates/plib_clc.c.ftl")
    clcSourceFile.setOutputName("plib_" + clcInstanceName.getValue().lower() + ".c")
    clcSourceFile.setDestPath("/peripheral/clc/")
    clcSourceFile.setProjectPath("config/" + configName + "/peripheral/clc/")
    clcSourceFile.setType("SOURCE")
    clcSourceFile.setMarkup(True)

    clcSystemInitFile = clcComponent.createFileSymbol("CLC_SYS_INIT", None)
    clcSystemInitFile.setType("STRING")
    clcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    clcSystemInitFile.setSourcePath("../peripheral/clc_01577/templates/system/initialization.c.ftl")
    clcSystemInitFile.setMarkup(True)

    clcSystemDefFile = clcComponent.createFileSymbol("CLC_SYS_DEF", None)
    clcSystemDefFile.setType("STRING")
    clcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    clcSystemDefFile.setSourcePath("../peripheral/clc_01577/templates/system/definitions.h.ftl")
    clcSystemDefFile.setMarkup(True)


