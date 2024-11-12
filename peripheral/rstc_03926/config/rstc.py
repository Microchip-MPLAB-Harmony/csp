# coding: utf-8
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

###################################################################################################
########################################## Component  #############################################
###################################################################################################
global RSTCfilesArray
RSTCfilesArray = []

def fileUpdate(symbol, event):
    global RSTCfilesArray

    if event["value"] == False:
        RSTCfilesArray[0].setSecurity("SECURE")
        RSTCfilesArray[1].setSecurity("SECURE")
        RSTCfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
    else:
        RSTCfilesArray[0].setSecurity("NON_SECURE")
        RSTCfilesArray[1].setSecurity("NON_SECURE")
        RSTCfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")


def instantiateComponent(rstcComponent):
    global rstcWakeupNum
    rstcWakeupNum = None
    rstcInstanceName = rstcComponent.createStringSymbol("RSTC_INSTANCE_NAME", None)
    rstcInstanceName.setVisible(False)
    rstcInstanceName.setDefaultValue(rstcComponent.getID().upper())

    rstcSym_Enable = rstcComponent.createBooleanSymbol("RSTC_ENABLE", None)
    rstcSym_Enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rstc_03926;register:RCAUSE")
    rstcSym_Enable.setLabel("Use Reset Controller ?")
    rstcSym_Enable.setDefaultValue(True)
    rstcSym_Enable.setReadOnly(True)

    rstcResetCause = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/register-group@[name="RSTC"]/register@[name="RCAUSE"]')
    rstcSym_RCAUSE_Index = rstcComponent.createIntegerSymbol("RSTC_RCAUSE_LENGTH", None)
    rstcSym_RCAUSE_Index.setDefaultValue(len(rstcResetCause.getChildren()))
    rstcSym_RCAUSE_Index.setVisible(False)
    for id in range(0,len(rstcResetCause.getChildren())):
        rstcSym_RCAUSE = rstcComponent.createKeyValueSetSymbol("RSTC_RCAUSE" + str(id), None)
        rstcSym_RCAUSE.setLabel(str(rstcResetCause.getChildren()[id].getAttribute("caption")))
        rstcSym_RCAUSE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rstc_03926;register:RCAUSE")
        rstcSym_RCAUSE.addKey(rstcResetCause.getChildren()[id].getAttribute("name"), str(id), rstcResetCause.getChildren()[id].getAttribute("caption"))
        rstcSym_RCAUSE.setOutputMode("Key")
        rstcSym_RCAUSE.setDisplayMode("Description")
        rstcSym_RCAUSE.setVisible(False)

    rstcBkup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RSTC"]/register-group@[name="RSTC"]/register@[name="BKUPEXIT"]')
    rstcSym_BKUPEXIT_Index = rstcComponent.createIntegerSymbol("RSTC_BKUPEXIT_LENGTH", None)
    rstcSym_BKUPEXIT_Index.setDefaultValue(len(rstcBkup.getChildren()))
    rstcSym_BKUPEXIT_Index.setVisible(False)
    for id in range(0,len(rstcBkup.getChildren())):
        rstcSym_BKUPEXIT = rstcComponent.createKeyValueSetSymbol("RSTC_BKUPEXIT" + str(id), None)
        rstcSym_BKUPEXIT.setLabel(str(rstcBkup.getChildren()[id].getAttribute("caption")))
        rstcSym_BKUPEXIT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rstc_03926;register:BKUPEXIT")
        rstcSym_BKUPEXIT.addKey(rstcBkup.getChildren()[id].getAttribute("name"), str(id), rstcBkup.getChildren()[id].getAttribute("caption"))
        rstcSym_BKUPEXIT.setOutputMode("Key")
        rstcSym_BKUPEXIT.setDisplayMode("Description")
        rstcSym_BKUPEXIT.setVisible(False)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
    rstcModuleID = rstcModuleNode.getAttribute("id")

    rstcSym_HeaderFile = rstcComponent.createFileSymbol("RSTC_HEADER", None)
    rstcSym_HeaderFile.setSourcePath("../peripheral/rstc_03926/templates/plib_rstc.h.ftl")
    rstcSym_HeaderFile.setOutputName("plib_" + rstcInstanceName.getValue().lower() + ".h")
    rstcSym_HeaderFile.setDestPath("peripheral/rstc/")
    rstcSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_HeaderFile.setType("HEADER")
    rstcSym_HeaderFile.setMarkup(True)

    rstcSym_SourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
    rstcSym_SourceFile.setSourcePath("../peripheral/rstc_03926/templates/plib_rstc.c.ftl")
    rstcSym_SourceFile.setOutputName("plib_" + rstcInstanceName.getValue().lower() + ".c")
    rstcSym_SourceFile.setDestPath("peripheral/rstc/")
    rstcSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSym_SourceFile.setType("SOURCE")
    rstcSym_SourceFile.setMarkup(True)

    rstcSym_SystemDefFile = rstcComponent.createFileSymbol("RSTC_SYS_DEF", None)
    rstcSym_SystemDefFile.setType("STRING")
    rstcSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSym_SystemDefFile.setSourcePath("../peripheral/rstc_03926/templates/system/definitions.h.ftl")
    rstcSym_SystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global RSTCfilesArray
        rstcIsNonSecure = Database.getSymbolValue("core", rstcComponent.getID().upper() + "_IS_NON_SECURE")
        rstcSym_SystemDefFile.setDependencies(fileUpdate, ["core." + rstcComponent.getID().upper() + "_IS_NON_SECURE"])
        RSTCfilesArray.append(rstcSym_HeaderFile)
        RSTCfilesArray.append(rstcSym_SourceFile)
        RSTCfilesArray.append(rstcSym_SystemDefFile)
        if rstcIsNonSecure == False:
            RSTCfilesArray[0].setSecurity("SECURE")
            RSTCfilesArray[1].setSecurity("SECURE")
            RSTCfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
