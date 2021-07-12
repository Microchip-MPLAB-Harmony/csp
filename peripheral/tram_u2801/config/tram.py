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

global TRAMfilesArray
TRAMfilesArray = []

def fileUpdate(symbol, event):
    global TRAMfilesArray
    if event["value"] == False:
        TRAMfilesArray[0].setSecurity("SECURE")
        TRAMfilesArray[1].setSecurity("SECURE")
        TRAMfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TRAMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    else:
        TRAMfilesArray[0].setSecurity("NON_SECURE")
        TRAMfilesArray[1].setSecurity("NON_SECURE")
        TRAMfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TRAMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")

def instantiateComponent(tramComponent):
    global tramInstanceName

    tramInstanceName = tramComponent.createStringSymbol("TRAM_INSTANCE_NAME", None)
    tramInstanceName.setVisible(False)
    tramInstanceName.setDefaultValue(tramComponent.getID().upper())
    Log.writeInfoMessage("Running " + tramInstanceName.getValue())

    tramSilentAccess = tramComponent.createBooleanSymbol("TRAM_SILENT_ACCESS", None)
    tramSilentAccess.setLabel("Enable Silent Access")
    tramSilentAccess.setDefaultValue(False)

    tramDRP = tramComponent.createBooleanSymbol("TRAM_DRP", None)
    tramDRP.setLabel("Enable Data Remanence Prevention")
    tramDRP.setDefaultValue(False)

    tramTamper = tramComponent.createBooleanSymbol("TRAM_TAMPER", None)
    tramTamper.setLabel("Erase Data on Tamper Detection")
    tramTamper.setDefaultValue(False)


    tramRAMNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TRAM"]/register-group@[name="TRAM"]/register@[name="RAM"]')
    ramCount = int(tramRAMNode.getAttribute("count")) - 1

    tramRAMCount = tramComponent.createIntegerSymbol("TRAM_RAM_COUNT", None)
    tramRAMCount.setLabel("TRAM RAM Maximum Counter")
    tramRAMCount.setMin(0)
    tramRAMCount.setMax(ramCount)
    tramRAMCount.setDefaultValue(ramCount)
    tramRAMCount.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    # Generate Output Header
    tramHeaderFile = tramComponent.createFileSymbol("TRAM_FILE_0", None)
    tramHeaderFile.setSourcePath("../peripheral/tram_u2801/templates/plib_tram.h.ftl")
    tramHeaderFile.setMarkup(True)
    tramHeaderFile.setOutputName("plib_"+tramInstanceName.getValue().lower()+".h")
    tramHeaderFile.setMarkup(True)
    tramHeaderFile.setOverwrite(True)
    tramHeaderFile.setDestPath("peripheral/tram/")
    tramHeaderFile.setProjectPath("config/" + configName + "/peripheral/tram/")
    tramHeaderFile.setType("HEADER")
    # Generate Output source

    tramSourceFile = tramComponent.createFileSymbol("TRAM_FILE_1", None)
    tramSourceFile.setSourcePath("../peripheral/tram_u2801/templates/plib_tram.c.ftl")
    tramSourceFile.setMarkup(True)
    tramSourceFile.setOutputName("plib_"+tramInstanceName.getValue().lower()+".c")
    tramSourceFile.setMarkup(True)
    tramSourceFile.setOverwrite(True)
    tramSourceFile.setDestPath("peripheral/tram/")
    tramSourceFile.setProjectPath("config/" + configName + "/peripheral/tram/")
    tramSourceFile.setType("SOURCE")

    tramSystemDefFile = tramComponent.createFileSymbol("TRAM_FILE_2", None)
    tramSystemDefFile.setType("STRING")
    tramSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tramSystemDefFile.setSourcePath("../peripheral/tram_u2801/templates/system/definitions.h.ftl")
    tramSystemDefFile.setMarkup(True)

    # System Initialization
    tramSystemInitFile = tramComponent.createFileSymbol("TRAM_SYS_INIT", None)
    tramSystemInitFile.setType("STRING")
    tramSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tramSystemInitFile.setSourcePath("../peripheral/tram_u2801/templates/system/initialization.c.ftl")
    tramSystemInitFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global TRAMfilesArray
        tramIsNonSecure = Database.getSymbolValue("core", tramComponent.getID().upper() + "_IS_NON_SECURE")
        tramSystemDefFile.setDependencies(fileUpdate, ["core." + tramComponent.getID().upper() + "_IS_NON_SECURE"])
        TRAMfilesArray.append(tramHeaderFile)
        TRAMfilesArray.append(tramSourceFile)
        TRAMfilesArray.append(tramSystemInitFile)
        TRAMfilesArray.append(tramSystemDefFile)
        if tramIsNonSecure == False:
            TRAMfilesArray[0].setSecurity("SECURE")
            TRAMfilesArray[1].setSecurity("SECURE")
            TRAMfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            TRAMfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")