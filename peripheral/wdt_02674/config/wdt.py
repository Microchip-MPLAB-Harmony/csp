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

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]")
wdtInstanceName.setDefaultValue(instances.getAttribute("name"))
wdtModuleID = instances.getAttribute("id")
Log.writeInfoMessage("Loading " + wdtInstanceName.getValue() + " for " + Variables.get("__PROCESSOR"))

wdtMenu = coreComponent.createMenuSymbol("WDT_MENU_0", None)
wdtMenu.setLabel("WDT")
wdtMenu.setVisible(True)

wdtEnable = coreComponent.createBooleanSymbol("USE_SYS_WDT", wdtMenu)
wdtEnable.setVisible(True)
wdtEnable.setLabel("Enable WDT?")
wdtEnable.setDefaultValue(True)

configName = Variables.get("__CONFIGURATION_NAME")
wdtHeaderFile = coreComponent.createFileSymbol("wdtHeaderFile", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_"+ wdtModuleID +"/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_"+wdtInstanceName.getValue().lower()+".h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(True)

wdtSourceFile = coreComponent.createFileSymbol("wdtSourceFile", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_"+ wdtModuleID +"/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_"+wdtInstanceName.getValue().lower()+".c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(True)

wdtSystemInitFile = coreComponent.createFileSymbol("wdtSystemInitFile", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_"+ wdtModuleID +"/templates/system/system_initialize.c.ftl")
wdtSystemInitFile.setMarkup(True)

wdtSystemDefFile = coreComponent.createFileSymbol("wdtSystemDefFile", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_"+ wdtModuleID +"/templates/system/system_definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(True)

