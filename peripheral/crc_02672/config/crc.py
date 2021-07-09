"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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


def instantiateComponent(crcComponent):

    crcInstanceName = crcComponent.createStringSymbol("CRC_INSTANCE_NAME", None)
    crcInstanceName.setVisible(False)
    crcInstanceName.setDefaultValue(crcComponent.getID().upper())

    # Clock enable
    Database.setSymbolValue("core", crcInstanceName.getValue() + "_CLOCK_ENABLE", True)

################################################################################
########                      Code Generation                      #############
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    crcHeaderFile = crcComponent.createFileSymbol("CRC_INSTANCE_HEADER", None)
    crcHeaderFile.setSourcePath("../peripheral/crc_02672/templates/plib_crc.h.ftl")
    crcHeaderFile.setOutputName("plib_" + crcInstanceName.getValue().lower() + ".h")
    crcHeaderFile.setDestPath("/peripheral/crc/")
    crcHeaderFile.setProjectPath("config/" + configName + "/peripheral/crc/")
    crcHeaderFile.setType("HEADER")
    crcHeaderFile.setMarkup(True)

    # Source File
    crcSourceFile = crcComponent.createFileSymbol("CRC_SOURCE", None)
    crcSourceFile.setSourcePath("../peripheral/crc_02672/templates/plib_crc.c.ftl")
    crcSourceFile.setOutputName("plib_" + crcInstanceName.getValue().lower() + ".c")
    crcSourceFile.setDestPath("/peripheral/crc/")
    crcSourceFile.setProjectPath("config/" + configName + "/peripheral/crc/")
    crcSourceFile.setType("SOURCE")
    crcSourceFile.setMarkup(True)

    # System Definition
    crcSystemDefFile = crcComponent.createFileSymbol("CRC_SYS_DEF", None)
    crcSystemDefFile.setType("STRING")
    crcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    crcSystemDefFile.setSourcePath("../peripheral/crc_02672/templates/system/definitions.h.ftl")
    crcSystemDefFile.setMarkup(True)
