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

###################################################################################################
########################################## Component ##############################################
###################################################################################################

def instantiateComponent(rconComponent):

    rconInstanceName = rconComponent.createStringSymbol("RCON_INSTANCE_NAME", None)
    rconInstanceName.setVisible(False)
    rconInstanceName.setDefaultValue(rconComponent.getID().upper())

    rconSym_Enable = rconComponent.createBooleanSymbol("RCON_ENABLE", None)
    rconSym_Enable.setLabel("Use Resets ?")
    rconSym_Enable.setDefaultValue(True)
    rconSym_Enable.setReadOnly(True)

    rconRegister = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RCON"]/register-group@[name="RCON"]/register@[name="RCON"]')

    rconSym_ResetCount = rconComponent.createIntegerSymbol("RCON_CAUSE_COUNT", None)
    rconSym_ResetCount.setDefaultValue(len(rconRegister.getChildren()))
    rconSym_ResetCount.setVisible(False)

    for id in range(len(rconRegister.getChildren())):
        rconSym_Cause = rconComponent.createKeyValueSetSymbol("RCON_CAUSE_" + str(id), None)
        rconSym_Cause.setLabel(str(rconRegister.getChildren()[id].getAttribute("caption")))
        rconSym_Cause.addKey(rconRegister.getChildren()[id].getAttribute("name"), str(id), rconRegister.getChildren()[id].getAttribute("caption"))
        rconSym_Cause.setOutputMode("Key")
        rconSym_Cause.setDisplayMode("Description")
        rconSym_Cause.setVisible(False)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rconSym_HeaderFile = rconComponent.createFileSymbol("RCON_HEADER", None)
    rconSym_HeaderFile.setSourcePath("../peripheral/rcon_02028/templates/plib_rcon.h.ftl")
    rconSym_HeaderFile.setOutputName("plib_" + rconInstanceName.getValue().lower() + ".h")
    rconSym_HeaderFile.setDestPath("peripheral/rcon/")
    rconSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rcon/")
    rconSym_HeaderFile.setType("HEADER")
    rconSym_HeaderFile.setMarkup(True)

    rconSym_SourceFile = rconComponent.createFileSymbol("RCON_SOURCE", None)
    rconSym_SourceFile.setSourcePath("../peripheral/rcon_02028/templates/plib_rcon.c.ftl")
    rconSym_SourceFile.setOutputName("plib_" + rconInstanceName.getValue().lower() + ".c")
    rconSym_SourceFile.setDestPath("peripheral/rcon/")
    rconSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/rcon/")
    rconSym_SourceFile.setType("SOURCE")
    rconSym_SourceFile.setMarkup(True)

    rconSym_SystemDefFile = rconComponent.createFileSymbol("RCON_SYS_DEF", None)
    rconSym_SystemDefFile.setType("STRING")
    rconSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rconSym_SystemDefFile.setSourcePath("../peripheral/rcon_02028/templates/system/definitions.h.ftl")
    rconSym_SystemDefFile.setMarkup(True)
