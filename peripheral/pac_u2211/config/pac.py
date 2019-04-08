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
########################################## Callbacks  #############################################
###################################################################################################

def updatePACCodeGenerationProperty(symbol, event):

    component = symbol.getComponent()
    component.getSymbolByID("PAC_HEADER").setEnabled(event["value"])
    component.getSymbolByID("PAC_SOURCE").setEnabled(event["value"])
    component.getSymbolByID("PAC_SYS_DEF").setEnabled(event["value"])

    Database.setSymbolValue("core", pacInstanceName.getValue() + "_CLOCK_ENABLE", event["value"], 1)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

global pacInstanceName

#PAC menu
pacSym_Menu = coreComponent.createMenuSymbol("PAC_MENU", None)
pacSym_Menu.setLabel("PAC")

#PAC Use
pacSym_Use = coreComponent.createBooleanSymbol("PAC_USE", pacSym_Menu)
pacSym_Use.setLabel("Use PAC ?")

pacInstanceName = coreComponent.createStringSymbol("PAC_INSTANCE_NAME", pacSym_Menu)
pacInstanceName.setVisible(False)
pacInstanceName.setDefaultValue("PAC")
pacInstanceName.setDependencies(updatePACCodeGenerationProperty, ["PAC_USE"])

pacIndex = 0

modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()
for module in range (0, len(modules)):
    moduleName = str(modules[module].getAttribute("name"))
    instances = modules[module].getChildren()
    for instance in range (0, len(instances)):
        options = instances[instance].getChildren()
        periName = str(instances[instance].getAttribute("name"))
        for option in range (0, len(options)):
            parameters = options[option].getChildren()
            for parameter in range(0, len(parameters)):
                name = str(parameters[parameter].getAttribute("name"))
                if "INSTANCE_ID" in name and moduleName not in [pacInstanceName.getValue(), "HMATRIXB"]:   #Skip which can't be protected

                    pacSym_PeripheralName = coreComponent.createStringSymbol("PAC_" + str(pacIndex) + "_PERI_NAME", pacSym_Use)
                    pacSym_PeripheralName.setDefaultValue(periName)
                    pacSym_PeripheralName.setVisible(False)

                    pacIndex += 1

pacSym_PeriCount = coreComponent.createIntegerSymbol("PAC_PERI_COUNT", pacSym_Use)
pacSym_PeriCount.setDefaultValue(pacIndex)
pacSym_PeriCount.setVisible(False)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pacSym_HeaderFile = coreComponent.createFileSymbol("PAC_HEADER", None)
pacSym_HeaderFile.setSourcePath("../peripheral/pac_u2211/templates/plib_pac.h.ftl")
pacSym_HeaderFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".h")
pacSym_HeaderFile.setDestPath("/peripheral/pac/")
pacSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_HeaderFile.setType("HEADER")
pacSym_HeaderFile.setMarkup(True)
pacSym_HeaderFile.setEnabled(False)

pacSym_SourceFile = coreComponent.createFileSymbol("PAC_SOURCE", None)
pacSym_SourceFile.setSourcePath("../peripheral/pac_u2211/templates/plib_pac.c.ftl")
pacSym_SourceFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".c")
pacSym_SourceFile.setDestPath("/peripheral/pac/")
pacSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_SourceFile.setType("SOURCE")
pacSym_SourceFile.setMarkup(True)
pacSym_SourceFile.setEnabled(False)

pacSystemDefFile = coreComponent.createFileSymbol("PAC_SYS_DEF", None)
pacSystemDefFile.setType("STRING")
pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pacSystemDefFile.setSourcePath("../peripheral/pac_u2211/templates/system/definitions.h.ftl")
pacSystemDefFile.setMarkup(True)
pacSystemDefFile.setEnabled(False)
