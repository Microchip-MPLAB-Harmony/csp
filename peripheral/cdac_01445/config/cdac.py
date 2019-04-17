# coding: utf-8
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

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if value[:2] == "0x":
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def updateCDACClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(cdacComponent):

    cdacInstanceName = cdacComponent.createStringSymbol("CDAC_INSTANCE_NAME", None)
    cdacInstanceName.setVisible(False)
    cdacInstanceName.setDefaultValue(cdacComponent.getID().upper())

    cdacInstanceNumber = cdacComponent.createStringSymbol("CDAC_INSTANCE_NUMBER", None)
    cdacInstanceNumber.setVisible(False)
    cdacInstanceNumber.setDefaultValue(cdacComponent.getID()[-1:])

    #Clock enable
    Database.setSymbolValue("core", cdacInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    # Resolution
    cdacSym_Resolution = cdacComponent.createStringSymbol("CDAC_RESOLUTION", None)
    cdacSym_Resolution.setLabel("CDAC Resolution")
    cdacSym_Resolution.setDefaultValue("12-bit")
    cdacSym_Resolution.setReadOnly(True)

    cdacReferenceValues = []
    cdacReferenceNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CDAC\"]/value-group@[name=\"DAC" + cdacInstanceNumber.getValue() + "CON__REFSEL\"]")
    _get_bitfield_names(cdacReferenceNode, cdacReferenceValues)

    # Reference Selection
    cdacSym_REFSEL = cdacComponent.createKeyValueSetSymbol("CDAC_REFSEL", None)
    cdacSym_REFSEL.setLabel(cdacReferenceNode.getAttribute("caption"))
    cdacSym_REFSEL.setDefaultValue(0)
    cdacSym_REFSEL.setOutputMode("Value")
    cdacSym_REFSEL.setDisplayMode("Description")
    cdacSym_REFSEL.setReadOnly(True)

    for dict in cdacReferenceValues:
        cdacSym_REFSEL.addKey(dict["key"], dict["value"], dict["desc"])

    cdacOutputBufferValues = []
    cdacOutputBufferNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CDAC\"]/value-group@[name=\"DAC" + cdacInstanceNumber.getValue() + "CON__DACOE\"]")
    _get_bitfield_names(cdacOutputBufferNode, cdacOutputBufferValues)

    # Output Buffer Enable
    cdacSym_DACOE = cdacComponent.createKeyValueSetSymbol("CDAC_DACOE", None)
    cdacSym_DACOE.setLabel(cdacOutputBufferNode.getAttribute("caption"))
    cdacSym_DACOE.setDefaultValue(0)
    cdacSym_DACOE.setOutputMode("Value")
    cdacSym_DACOE.setDisplayMode("Description")

    for dict in cdacOutputBufferValues:
        cdacSym_DACOE.addKey(dict["key"], dict["value"], dict["desc"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    # Clock Warning status
    cdacSym_ClkEnComment = cdacComponent.createCommentSymbol("CDAC_CLOCK_ENABLE_COMMENT", None)
    cdacSym_ClkEnComment.setLabel("Warning!!! " + cdacInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    cdacSym_ClkEnComment.setVisible(False)
    cdacSym_ClkEnComment.setDependencies(updateCDACClockWarningStatus, ["core." + cdacInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    cdacHeaderFile = cdacComponent.createFileSymbol("CDAC_INSTANCE_HEADER", None)
    cdacHeaderFile.setSourcePath("../peripheral/cdac_01445/templates/plib_cdac.h.ftl")
    cdacHeaderFile.setOutputName("plib_" + cdacInstanceName.getValue().lower() + ".h")
    cdacHeaderFile.setDestPath("/peripheral/cdac/")
    cdacHeaderFile.setProjectPath("config/" + configName + "/peripheral/cdac/")
    cdacHeaderFile.setType("HEADER")
    cdacHeaderFile.setMarkup(True)

    cdacSourceFile = cdacComponent.createFileSymbol("CDAC_SOURCE", None)
    cdacSourceFile.setSourcePath("../peripheral/cdac_01445/templates/plib_cdac.c.ftl")
    cdacSourceFile.setOutputName("plib_" + cdacInstanceName.getValue().lower() + ".c")
    cdacSourceFile.setDestPath("/peripheral/cdac/")
    cdacSourceFile.setProjectPath("config/" + configName + "/peripheral/cdac/")
    cdacSourceFile.setType("SOURCE")
    cdacSourceFile.setMarkup(True)

    cdacSystemInitFile = cdacComponent.createFileSymbol("CDAC_SYS_INIT", None)
    cdacSystemInitFile.setType("STRING")
    cdacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cdacSystemInitFile.setSourcePath("../peripheral/cdac_01445/templates/system/initialization.c.ftl")
    cdacSystemInitFile.setMarkup(True)

    cdacSystemDefFile = cdacComponent.createFileSymbol("CDAC_SYS_DEF", None)
    cdacSystemDefFile.setType("STRING")
    cdacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cdacSystemDefFile.setSourcePath("../peripheral/cdac_01445/templates/system/definitions.h.ftl")
    cdacSystemDefFile.setMarkup(True)
