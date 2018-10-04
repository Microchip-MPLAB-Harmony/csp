# coding: utf-8
"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

global wdtInstanceName

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]").getChildren()
wdtInstanceName.setDefaultValue(instances[0].getAttribute("name"))
Log.writeInfoMessage("Loading " + wdtInstanceName.getValue() + "for " + Variables.get("__PROCESSOR"))

wdtMenu = coreComponent.createMenuSymbol("WDT_MENU_0", None)
wdtMenu.setLabel("WDT")

wdtEnable = coreComponent.createBooleanSymbol("wdtENABLE", wdtMenu)
wdtEnable.setLabel("Enable Watchdog Timer?")
wdtEnable.setDefaultValue(False)

def wdtEnableCfgMenu(wdtCfgMenu, event):
    wdtCfgMenu.setVisible(event["value"])

    component = wdtCfgMenu.getComponent()
    component.getSymbolByID("wdtHeaderFile").setEnabled(event["value"])
    component.getSymbolByID("wdtSourceFile").setEnabled(event["value"])
    component.getSymbolByID("wdtSystemDefFile").setEnabled(event["value"])

    if event["value"] == False:
        Database.clearSymbolValue("core", "rswdtENABLE")
        Database.setSymbolValue("core", "rswdtENABLE", False, 1)

wdtCfgMenu = coreComponent.createMenuSymbol("WDT_SUBMENU", wdtMenu)
wdtCfgMenu.setLabel("WDT Configuration")
wdtCfgMenu.setDependencies(wdtEnableCfgMenu, ["wdtENABLE"])
wdtCfgMenu.setVisible(False)

wdtReset = coreComponent.createBooleanSymbol("wdtEnableReset", wdtCfgMenu)
wdtReset.setLabel("Enable Reset")
wdtReset.setDefaultValue(True)

def wdtResetEnable(wdtInterrupt, event):
    if event["value"] == True:
        wdtInterrupt.setVisible(False)
        wdtInterrupt.setValue(False, 2)
    else:
        wdtInterrupt.setVisible(True)

wdtInterrupt = coreComponent.createBooleanSymbol("wdtinterruptMode", wdtCfgMenu)
wdtInterrupt.setLabel("Enable Interrupts")
wdtInterrupt.setDefaultValue(False)
wdtInterrupt.setDependencies(wdtResetEnable, ["wdtEnableReset"])
wdtInterrupt.setVisible(False)

wdtCounterValue = coreComponent.createIntegerSymbol("wdtWDV", wdtCfgMenu)
wdtCounterValue.setLabel("Counter value")
wdtCounterValue.setMax(0xfff)
wdtCounterValue.setDefaultValue(0xfff)

def wdtcounter_cal(wdtCounterValueTime, event):
    data = event["value"] * 3.90625
    wdtCounterValueTime.setValue(int(round(data)),2)

wdtCounterValueTime = coreComponent.createIntegerSymbol("wdtWDVTIME", wdtCfgMenu)
wdtCounterValueTime.setLabel("WDT Counter value in ms")
wdtCounterValueTime.setDependencies(wdtcounter_cal, ["wdtWDV"])
wdtCounterValueTime.setReadOnly(True)
wdtCounterValueTime.setDefaultValue(15996)

wdtDeltaValue = coreComponent.createIntegerSymbol("wdtWDD", wdtCfgMenu)
wdtDeltaValue.setLabel("Delta value")
wdtDeltaValue.setMax(0xfff)
wdtDeltaValue.setDefaultValue(0xfff)

def wdtdelta_cal(wdtDeltaValueTime, event):
    data = event["value"] * 3.90625
    wdtDeltaValueTime.setValue(int(round(data)),2)

wdtDeltaValueTime = coreComponent.createIntegerSymbol("wdtWDDTIME", wdtCfgMenu)
wdtDeltaValueTime.setLabel("WDT Delta value in ms")
wdtDeltaValueTime.setDependencies(wdtdelta_cal, ["wdtWDD"])
wdtDeltaValueTime.setReadOnly(True)
wdtDeltaValueTime.setDefaultValue(15996)

wdtDebugHalt = coreComponent.createBooleanSymbol("wdtdebugHalt", wdtCfgMenu)
wdtDebugHalt.setLabel("Enable Debug halt")
wdtDebugHalt.setDefaultValue(False)

wdtIdleHalt = coreComponent.createBooleanSymbol("wdtidleHalt", wdtCfgMenu)
wdtIdleHalt.setLabel("Enable Idle halt")
wdtIdleHalt.setDefaultValue(False)

global wdtinterruptVector
global wdtinterruptHandler
global wdtinterruptHandlerLock

wdtinterruptVector = wdtInstanceName.getValue()+"_INTERRUPT_ENABLE"
wdtinterruptHandler = wdtInstanceName.getValue()+"_INTERRUPT_HANDLER"
wdtinterruptHandlerLock = wdtInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"

Database.clearSymbolValue("core", wdtinterruptVector)
Database.setSymbolValue("core", wdtinterruptVector, False, 2)
Database.clearSymbolValue("core", wdtinterruptHandler)
Database.setSymbolValue("core", wdtinterruptHandler, "WDT_Handler", 2)
Database.clearSymbolValue("core", wdtinterruptHandlerLock)
Database.setSymbolValue("core", wdtinterruptHandlerLock, False, 2)

def interruptControl(NVIC, event):
    global wdtinterruptVector
    global wdtinterruptHandler
    Database.clearSymbolValue("core", wdtinterruptVector)
    Database.clearSymbolValue("core", wdtinterruptHandler)
    Database.clearSymbolValue("core", wdtinterruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", wdtinterruptVector, True, 2)
        Database.setSymbolValue("core", wdtinterruptHandler, wdtInstanceName.getValue()+"_InterruptHandler", 2)
        Database.setSymbolValue("core", wdtinterruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", wdtinterruptVector, False, 2)
        Database.setSymbolValue("core", wdtinterruptHandler, "WDT_Handler", 2)
        Database.setSymbolValue("core", wdtinterruptHandlerLock, False, 2)

# NVIC Dynamic settings
wdtinterruptControl = coreComponent.createBooleanSymbol("NVIC_WDT_ENABLE", None)
wdtinterruptControl.setDependencies(interruptControl, ["wdtinterruptMode"])
wdtinterruptControl.setVisible(False)



configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("wdtHeaderFile", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_"+wdtInstanceName.getValue().lower()+".h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(False)

wdtSourceFile = coreComponent.createFileSymbol("wdtSourceFile", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_6080/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_"+wdtInstanceName.getValue().lower()+".c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(False)

wdtSystemInitFile = coreComponent.createFileSymbol("wdtSystemInitFile", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_initialize.c.ftl")
wdtSystemInitFile.setMarkup(True)

wdtSystemDefFile = coreComponent.createFileSymbol("wdtSystemDefFile", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_6080/templates/system/system_definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(False)
