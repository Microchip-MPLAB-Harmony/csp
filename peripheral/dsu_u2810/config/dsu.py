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

################################################################################
#############             DSU DATABASE COMPONENTS         ######################
################################################################################
global DSUfilesArray
DSUfilesArray = []

def fileUpdate(symbol, event):
    global DSUfilesArray
    if event["value"] == False:
        DSUfilesArray[0].setSecurity("SECURE")
        DSUfilesArray[1].setSecurity("SECURE")
        DSUfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    else:
        DSUfilesArray[0].setSecurity("NON_SECURE")
        DSUfilesArray[1].setSecurity("NON_SECURE")
        DSUfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")


def instantiateComponent(dsuComponent):

    dsuInstanceName = dsuComponent.createStringSymbol("DSU_INSTANCE_NAME", None)
    dsuInstanceName.setVisible(False)
    dsuInstanceName.setDefaultValue(dsuComponent.getID().upper())
    Log.writeInfoMessage("Running " + dsuInstanceName.getValue())

    CtrlCmdNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DSU\"]/register-group@[name=\"DSU\"]/register@[name=\"CTRL\"]/bitfield@[name=\"CMD\"]")

    dsuCrcOnCommandBased = dsuComponent.createBooleanSymbol("DSU_CRC_ON_COMMAND", None)
    dsuCrcOnCommandBased.setVisible(False)
    if CtrlCmdNode is not None:
        dsuCrcOnCommandBased.setDefaultValue(True)
    else:
        dsuCrcOnCommandBased.setDefaultValue(False)

################################################################################
#############             CODE GENERATION             ##########################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    dsuSym_HeaderFile = dsuComponent.createFileSymbol("DSU_HEADER", None)
    dsuSym_HeaderFile.setSourcePath("../peripheral/dsu_u2810/templates/plib_dsu.h.ftl")
    dsuSym_HeaderFile.setOutputName("plib_"+dsuInstanceName.getValue().lower()+".h")
    dsuSym_HeaderFile.setDestPath("peripheral/dsu/")
    dsuSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/dsu/")
    dsuSym_HeaderFile.setType("HEADER")
    dsuSym_HeaderFile.setMarkup(True)

    dsuSym_SourceFile = dsuComponent.createFileSymbol("DSU_SOURCE", None)
    dsuSym_SourceFile.setSourcePath("../peripheral/dsu_u2810/templates/plib_dsu.c.ftl")
    dsuSym_SourceFile.setOutputName("plib_"+dsuInstanceName.getValue().lower() + ".c")
    dsuSym_SourceFile.setDestPath("peripheral/dsu/")
    dsuSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/dsu/")
    dsuSym_SourceFile.setType("SOURCE")
    dsuSym_SourceFile.setMarkup(True)

    dsuSystemDefFile = dsuComponent.createFileSymbol("DSU_SYS_DEF", None)
    dsuSystemDefFile.setType("STRING")
    dsuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dsuSystemDefFile.setSourcePath("../peripheral/dsu_u2810/templates/system/definitions.h.ftl")
    dsuSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global DSUfilesArray
        dsuIsNonSecure = Database.getSymbolValue("core", dsuComponent.getID().upper() + "_IS_NON_SECURE")
        dsuSystemDefFile.setDependencies(fileUpdate, ["core." + dsuComponent.getID().upper() + "_IS_NON_SECURE"])
        DSUfilesArray.append(dsuSym_HeaderFile)
        DSUfilesArray.append(dsuSym_SourceFile)
        DSUfilesArray.append(dsuSystemDefFile)
        if dsuIsNonSecure == False:
            DSUfilesArray[0].setSecurity("SECURE")
            DSUfilesArray[1].setSecurity("SECURE")
            DSUfilesArray[2].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")