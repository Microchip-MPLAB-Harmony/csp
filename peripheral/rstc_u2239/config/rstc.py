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

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(rstcComponent):

    rstcSym_RCAUSE = []

    rstcInstanceName = rstcComponent.createStringSymbol("RSTC_INSTANCE_NAME", None)
    rstcInstanceName.setVisible(False)
    rstcInstanceName.setDefaultValue(rstcComponent.getID().upper())

    rstcSym_Enable = rstcComponent.createBooleanSymbol("RSTC_ENABLE", None)
    rstcSym_Enable.setLabel("Use Reset Controller ?")
    rstcSym_Enable.setDefaultValue(True)
    rstcSym_Enable.setReadOnly(True)

    rstcResetCause = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/register-group@[name="RSTC"]/register@[name="RCAUSE"]')

    rstcSym_RCAUSE_Index = rstcComponent.createIntegerSymbol("RSTC_RCAUSE_LENGTH", None)
    rstcSym_RCAUSE_Index.setDefaultValue(len(rstcResetCause.getChildren()))
    rstcSym_RCAUSE_Index.setVisible(False)

    for id in range(0,len(rstcResetCause.getChildren())):
        rstcSym_RCAUSE.append(id)
        rstcSym_RCAUSE[id] = rstcComponent.createKeyValueSetSymbol("RSTC_RCAUSE"+str(id), None)
        rstcSym_RCAUSE[id].setLabel(str(rstcResetCause.getChildren()[id].getAttribute("caption")))
        rstcSym_RCAUSE[id].addKey(rstcResetCause.getChildren()[id].getAttribute("name"), str(id), rstcResetCause.getChildren()[id].getAttribute("caption"))
        rstcSym_RCAUSE[id].setOutputMode("Key")
        rstcSym_RCAUSE[id].setDisplayMode("Description")
        rstcSym_RCAUSE[id].setVisible(False)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
    rstcModuleID = rstcModuleNode.getAttribute("id")

    rstcSym_HeaderFile = rstcComponent.createFileSymbol("RSTC_HEADER", None)
    rstcSym_HeaderFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/plib_rstc.h.ftl")
    rstcSym_HeaderFile.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".h")
    rstcSym_HeaderFile.setDestPath("peripheral/rstc/")
    rstcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_HeaderFile.setType("HEADER")
    rstcSym_HeaderFile.setMarkup(True)

    rstcSym_SourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
    rstcSym_SourceFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/plib_rstc.c.ftl")
    rstcSym_SourceFile.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".c")
    rstcSym_SourceFile.setDestPath("peripheral/rstc/")
    rstcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_SourceFile.setType("SOURCE")
    rstcSym_SourceFile.setMarkup(True)

    rstcSym_SystemDefFile = rstcComponent.createFileSymbol("RSTC_SYS_DEF", None)
    rstcSym_SystemDefFile.setType("STRING")
    rstcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSym_SystemDefFile.setSourcePath("../peripheral/rstc_"+rstcModuleID+"/templates/system/definitions.h.ftl")
    rstcSym_SystemDefFile.setMarkup(True)
