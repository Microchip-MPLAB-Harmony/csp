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

def pacFileGeneration(symbol, event):
    symbol.setEnabled(bool(event["value"]))
    symbol.setEnabled(bool(event["value"]))

################## Symbol Creation for DMA Component ###############################################

pacInstanceName = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="PAC"]/instance@[name="PAC"]')

pacInstance = coreComponent.createStringSymbol("PAC_INSTANCE_NAME", None)
pacInstance.setVisible(False)
pacInstance.setDefaultValue(pacInstanceName.getAttribute("name"))

# PAC Configuration
pacMenu = coreComponent.createMenuSymbol("PAC_MENU", None)
pacMenu.setLabel("PAC")

# PAC Enable 
pacEnable = coreComponent.createBooleanSymbol("PAC_ENABLE", pacMenu)
pacEnable.setLabel("Use PAC")
# pacEnable.setDefaultValue(False)
pacEnable.setVisible(True)
     
##################### Code Generation #######################################
configName = Variables.get("__CONFIGURATION_NAME")
pacHeaderFile = coreComponent.createFileSymbol("PAC_HEADER", None)
pacHeaderFile.setSourcePath("../peripheral/pac_04649/templates/plib_pac.h.ftl")
pacHeaderFile.setOutputName("plib_pac.h")
pacHeaderFile.setDestPath("/peripheral/pac/")
pacHeaderFile.setProjectPath("config/" + configName +"/peripheral/pac/")
pacHeaderFile.setType("HEADER")
pacHeaderFile.setEnabled(False)
pacHeaderFile.setMarkup(True)
pacHeaderFile.setDependencies(pacFileGeneration, ["PAC_ENABLE"])


pacSourceFile = coreComponent.createFileSymbol("PAC_SOURCE", None)
pacSourceFile.setSourcePath("../peripheral/pac_04649/templates/plib_pac.c.ftl")
pacSourceFile.setOutputName("plib_pac.c")
pacSourceFile.setDestPath("/peripheral/pac/")
pacSourceFile.setProjectPath("config/" + configName +"/peripheral/pac/")
pacSourceFile.setType("SOURCE")
pacSourceFile.setMarkup(True)
pacSourceFile.setEnabled(False)
pacSourceFile.setDependencies(pacFileGeneration, ["PAC_ENABLE"])

pacSystemDefFile = coreComponent.createFileSymbol("PAC_SYS_DEF", None)
pacSystemDefFile.setType("STRING")
pacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pacSystemDefFile.setSourcePath("../peripheral/pac_04649/templates/system/definitions.h.ftl")
pacSystemDefFile.setMarkup(True)
pacSystemDefFile.setEnabled(False)
pacSystemDefFile.setDependencies(pacFileGeneration, ["PAC_ENABLE"])
