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

global pacInstanceName
global pacSym_Use

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def generateFiles(symbol, event):

    component = symbol.getComponent()
    isPAC_Enabled = Database.getSymbolValue("core", "PAC_USE")
    
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        isPAC_NonSecure = Database.getSymbolValue("core", "PAC_IS_NON_SECURE")

        if isPAC_NonSecure == True:    
            component.getSymbolByID("PAC_HEADER").setSecurity("NON_SECURE")
            component.getSymbolByID("PAC_SOURCE").setSecurity("NON_SECURE")
            component.getSymbolByID("PAC_SYS_DEF").setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
            component.getSymbolByID("PAC_SYS_INIT").setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        else:
            component.getSymbolByID("PAC_HEADER").setSecurity("SECURE")
            component.getSymbolByID("PAC_SOURCE").setSecurity("SECURE")
            component.getSymbolByID("PAC_SYS_DEF").setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
            component.getSymbolByID("PAC_SYS_INIT").setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    
    component.getSymbolByID("PAC_HEADER").setEnabled(isPAC_Enabled)
    component.getSymbolByID("PAC_SOURCE").setEnabled(isPAC_Enabled)
    component.getSymbolByID("PAC_SYS_DEF").setEnabled(isPAC_Enabled)
    component.getSymbolByID("PAC_SYS_INIT").setEnabled(isPAC_Enabled)    
    
###################################################################################################
########################################## Component  #############################################
###################################################################################################


# PAC menu
pacSym_Menu = coreComponent.createMenuSymbol("PAC_MENU", None)
pacSym_Menu.setLabel("PAC")

instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PAC\"]").getChildren()

pacInstanceName = coreComponent.createStringSymbol("PAC_INSTANCE_NAME", pacSym_Menu)
pacInstanceName.setVisible(False)
pacInstanceName.setDefaultValue(instances[0].getAttribute("name"))

# PAC Use
pacSym_Use = coreComponent.createBooleanSymbol("PAC_USE", pacSym_Menu)
pacSym_Use.setLabel("Use PAC ?")


pacIndex = 0

modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()
for module in range(0, len(modules)):
    instances = modules[module].getChildren()
    for instance in range(0, len(instances)):
        options = instances[instance].getChildren()
        for option in range(0, len(options)):
            parameters = options[option].getChildren()
            for parameter in range(0, len(parameters)):
                name = str(parameters[parameter].getAttribute("name"))
                if "INSTANCE_ID" in name:
                    periName = str(instances[instance].getAttribute("name"))

                    pacSym_PeripheralName = coreComponent.createStringSymbol("PAC_" + str(pacIndex) + "_PERI_NAME", pacSym_Use)
                    pacSym_PeripheralName.setDefaultValue(periName)
                    pacSym_PeripheralName.setVisible(False)

                    pacIndex += 1

pacSym_PeriCount = coreComponent.createIntegerSymbol("PAC_PERI_COUNT", pacSym_Use)
pacSym_PeriCount.setDefaultValue(pacIndex)
pacSym_PeriCount.setVisible(False)

############################################################################
#### Dependency ####
############################################################################


###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pacSym_HeaderFile = coreComponent.createFileSymbol("PAC_HEADER", None)
pacSym_HeaderFile.setSourcePath("../peripheral/pac_04298/templates/plib_pac.h.ftl")
pacSym_HeaderFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".h")
pacSym_HeaderFile.setDestPath("/peripheral/pac/")
pacSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_HeaderFile.setType("HEADER")
pacSym_HeaderFile.setMarkup(True)
pacSym_HeaderFile.setEnabled(False)

pacSym_SourceFile = coreComponent.createFileSymbol("PAC_SOURCE", None)
pacSym_SourceFile.setSourcePath("../peripheral/pac_04298/templates/plib_pac.c.ftl")
pacSym_SourceFile.setOutputName("plib_" + pacInstanceName.getValue().lower() + ".c")
pacSym_SourceFile.setDestPath("/peripheral/pac/")
pacSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/pac/")
pacSym_SourceFile.setType("SOURCE")
pacSym_SourceFile.setMarkup(True)
pacSym_SourceFile.setEnabled(False)

pacSystemDefFile = coreComponent.createFileSymbol("PAC_SYS_DEF", None)
pacSystemDefFile.setType("STRING")
pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pacSystemDefFile.setSourcePath("../peripheral/pac_04298/templates/system/definitions.h.ftl")
pacSystemDefFile.setMarkup(True)
pacSystemDefFile.setEnabled(False)

pacSystemInitFile = coreComponent.createFileSymbol("PAC_SYS_INIT", None)
pacSystemInitFile.setType("STRING")
pacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
pacSystemInitFile.setSourcePath("../peripheral/pac_04298/templates/system/initialization.c.ftl")
pacSystemInitFile.setMarkup(True)
pacSystemInitFile.setEnabled(False)

pacSym_fileGen = coreComponent.createBooleanSymbol("PAC_FILE_GEN_LOGIC", None)
pacSym_fileGen.setVisible(False)

if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
    pacSym_HeaderFile.setSecurity("SECURE")
    pacSym_SourceFile.setSecurity("SECURE")
    pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
    pacSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pacSym_fileGen.setDependencies(generateFiles, ["PAC_USE", "core.PAC_IS_NON_SECURE"])
else:
    pacSym_fileGen.setDependencies(generateFiles, ["PAC_USE"])