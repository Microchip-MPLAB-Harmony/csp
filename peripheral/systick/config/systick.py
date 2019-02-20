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
#### Global Variables ####
################################################################################
global  systickHeaderFile
global  systickSourceFile
global  systickSystemDefFile
global  systickSystemInitFile
global  systickinterruptVector
global  systickinterruptHandlerLock
global  systickComment

Log.writeInfoMessage("Loading SYSTICK for " + Variables.get("__PROCESSOR"))

################################################################################
#### Business Logic ####
################################################################################

def systickUse(systickEnable, osal):
    if osal["value"] == "BareMetal":
        systickEnable.setVisible(True)
        systickComment.setVisible(False)
    else:
        systickEnable.setVisible(False)
        systickComment.setVisible(True)

        systickHeaderFile.setEnabled(False)
        systickSourceFile.setEnabled(False)
        systickSystemDefFile.setEnabled(False)
        systickSystemInitFile.setEnabled(False)


def sysTickEnableCfgMenu(CfgMenu, event):
    CfgMenu.setVisible(event["value"])

    if event["value"] == True:
        systickHeaderFile.setEnabled(True)
        systickSourceFile.setEnabled(True)
        systickSystemDefFile.setEnabled(True)
        systickSystemInitFile.setEnabled(True)
    else:
        systickHeaderFile.setEnabled(False)
        systickSourceFile.setEnabled(False)
        systickSystemDefFile.setEnabled(False)
        systickSystemInitFile.setEnabled(False)

def sysTickinterruptControl(symbol, event):
    Database.clearSymbolValue("core", systickinterruptVector)
    Database.clearSymbolValue("core", systickinterruptHandlerLock)

    if event["value"] == True:
        Database.setSymbolValue("core", systickinterruptVector, True, 2)
        Database.setSymbolValue("core", systickinterruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", systickinterruptVector, False, 2)
        Database.setSymbolValue("core", systickinterruptHandlerLock, False, 2)

def sysTickMax(systick, event):
    clock = 0
    freq_ext = 0
    freq_proc = 0
    max = 0

    if Database.getSymbolValue("core", "SYSTICK_EXTERNAL_CLOCK"):
        freq_ext = int(Database.getSymbolValue("core", "SYSTICK_CLOCK_FREQUENCY"))
        clock = Database.getSymbolValue("core", "SYSTICK_CLOCK")
    else:
        clock = 1

    freq_proc = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))

    systickCVRNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SysTick"]/register-group@[name="SysTick"]/register@[name="CVR"]/bitfield@[name="CURRENT"]')
    currentValueMask = str(systickCVRNode.getAttribute("mask"))

    if clock == 0:
        if freq_ext != 0 and freq_ext != None:
            max = ((float(1) / int(freq_ext)) * int(currentValueMask, 0) * 1000)
    else:
        if freq_proc != 0 and freq_proc != None:
            max = ((float(1) / int(freq_proc)) * int(currentValueMask, 0) * 1000)

    systick.setMax(float(max))

def systickCal(symbol, event):
    clock = 0
    freq_ext = 0
    freq_proc = 0
    value = 0

    if Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK"):
        clock = Database.getSymbolValue("core", "SYSTICK_CLOCK")
        freq_ext = int(Database.getSymbolValue("core", "SYSTICK_CLOCK_FREQUENCY"))
    else:
        clock = 1

    period = float(Database.getSymbolValue("core", "SYSTICK_PERIOD_MS"))
    freq_proc = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))

    if clock == 0:
        if freq_ext != 0 and freq_ext != None:
            value = int(round(float(freq_ext) * (period / 1000)))
    else:
        if freq_proc != 0 and freq_proc != None:
            value = int(round((float(freq_proc)) * (period / 1000)))

    symbol.setValue(str(hex(value)),2)
    Database.setSymbolValue("core","SYSTICK_PERIOD_US", int(round(period * 1000)), 2)

################################################################################
#### Menu ####
################################################################################

sysTickMenu = coreComponent.createMenuSymbol("SYSTICK_MENU", cortexMenu)
sysTickMenu.setLabel("SysTick")

# Interrupt Warning status
systickComment = coreComponent.createCommentSymbol("SYSTICK_COMMENT", sysTickMenu)
systickComment.setVisible(False)
systickComment.setLabel("RTOS is using SysTick for Timebase")

systickEnable = coreComponent.createBooleanSymbol("systickEnable", sysTickMenu)
systickEnable.setLabel("Enable SysTick")
systickEnable.setDependencies(systickUse, ["HarmonyCore.SELECT_RTOS"])

systickConfigMenu = coreComponent.createMenuSymbol("SYSTICK_MENU_0", systickEnable)
systickConfigMenu.setLabel("SysTick Configuration")
systickConfigMenu.setVisible(False)
systickConfigMenu.setDependencies(sysTickEnableCfgMenu, ["systickEnable"])

systickInterrupt = coreComponent.createBooleanSymbol("USE_SYSTICK_INTERRUPT", systickConfigMenu)
systickInterrupt.setLabel("Enable Interrupt")

systickClock = coreComponent.createKeyValueSetSymbol("SYSTICK_CLOCK", systickConfigMenu)
systickClock.setLabel("SysTick Clock")
systickClock.setOutputMode("Value")
systickClock.setDisplayMode("Description")
if Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK"):
    systickClock.addKey("HCLK/2", str(0) , "SysTick External clock" )
systickClock.addKey("HCLK", str(1) , "Processor clock" )
systickClock.setDefaultValue(int(Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK")))

systickNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SysTick"]/register-group@[name="SysTick"]/register@[name="CVR"]/bitfield@[name="CURRENT"]')
maxCount = str(systickNode.getAttribute("mask"))
max = ((float(1) / int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))) * int(maxCount, 0) * 1000)

systickPeriodMS = coreComponent.createFloatSymbol("SYSTICK_PERIOD_MS", systickConfigMenu)
systickPeriodMS.setLabel("Systick Period(Milliseconds)")
systickPeriodMS.setVisible(True)
systickPeriodMS.setDefaultValue(float(1.0))
systickPeriodMS.setMin(0)
systickPeriodMS.setMax(float(max))
systickPeriodMS.setDependencies(sysTickMax, ["core.CPU_CLOCK_FREQUENCY", "SYSTICK_CLOCK", "core.SYSTICK_CLOCK_FREQUENCY"])


systickDefault = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / 1000
systickPeriod = coreComponent.createStringSymbol("SYSTICK_PERIOD", systickConfigMenu)
systickPeriod.setLabel("SysTick Period")
systickPeriod.setVisible(False)
systickPeriod.setDefaultValue(str(hex(systickDefault)))
systickPeriod.setDependencies(systickCal, ["SYSTICK_PERIOD_MS", "SYSTICK_CLOCK", "core.CPU_CLOCK_FREQUENCY", "core.SYSTICK_CLOCK_FREQUENCY"])

systickPeriodUS = coreComponent.createIntegerSymbol("SYSTICK_PERIOD_US", systickConfigMenu)
systickPeriodUS.setVisible(False)
systickPeriodUS.setDefaultValue(1000)
systickPeriodUS.setMin(0)

# Setup Peripheral Interrupt in Interrupt manager
systickinterruptVector = "SysTick_INTERRUPT_ENABLE"
systickinterruptHandlerLock = "SysTick_INTERRUPT_HANDLER_LOCK"

# NVIC Dynamic settings
SYSTICK_interruptControl = coreComponent.createBooleanSymbol("NVIC_SYSTICK_ENABLE", systickConfigMenu)
SYSTICK_interruptControl.setDependencies(sysTickinterruptControl, ["USE_SYSTICK_INTERRUPT"])
SYSTICK_interruptControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

systickHeaderFile = coreComponent.createFileSymbol("SYSTICK_FILE_0", None)
systickHeaderFile.setSourcePath("../peripheral/systick/templates/plib_systick.h.ftl")
systickHeaderFile.setOutputName("plib_systick.h")
systickHeaderFile.setDestPath("/peripheral/systick/")
systickHeaderFile.setProjectPath("config/" + configName + "/peripheral/systick/")
systickHeaderFile.setType("HEADER")
systickHeaderFile.setOverwrite(True)
systickHeaderFile.setEnabled(False)
systickHeaderFile.setMarkup(True)

systickSourceFile = coreComponent.createFileSymbol("SYSTICK_FILE_1", None)
systickSourceFile.setSourcePath("../peripheral/systick/templates/plib_systick.c.ftl")
systickSourceFile.setOutputName("plib_systick.c")
systickSourceFile.setDestPath("/peripheral/systick/")
systickSourceFile.setProjectPath("config/" + configName + "/peripheral/systick/")
systickSourceFile.setType("SOURCE")
systickSourceFile.setOverwrite(True)
systickSourceFile.setMarkup(True)
systickSourceFile.setEnabled(False)

systickSystemDefFile = coreComponent.createFileSymbol("SYSTICK_FILE_2", None)
systickSystemDefFile.setType("STRING")
systickSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
systickSystemDefFile.setSourcePath("../peripheral/systick/templates/system/definitions.h.ftl")
systickSystemDefFile.setMarkup(True)
systickSystemDefFile.setEnabled(False)

systickSystemInitFile = coreComponent.createFileSymbol("systickSystemInitFile", None)
systickSystemInitFile.setType("STRING")
systickSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
systickSystemInitFile.setSourcePath("../peripheral/systick/templates/system/initialization.c.ftl")
systickSystemInitFile.setMarkup(True)
systickSystemInitFile.setEnabled(False)
