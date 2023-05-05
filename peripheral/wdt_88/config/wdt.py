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

###################################################################################################
##################################### Global Variables ############################################
###################################################################################################

global wdtSym_Use
global wdtHeaderFile
global wdtSourceFile
global wdtSystemDefFile

global setWDTInterruptData
global nvicInterruptUpdateWDT

###################################################################################################
########################################## Callbacks ##############################################
###################################################################################################


def updateWDTConfigCommentVisibleProperty(symbol, event):

    wdtHeaderFile.setEnabled(event["value"])
    wdtSourceFile.setEnabled(event["value"])
    wdtSystemDefFile.setEnabled(event["value"])

    symbol.setVisible(event["value"])

def setWDTInterruptData(wdt_interrupt_name, status):
    global setWDTInterruptData

    Database.setSymbolValue("core", wdt_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", wdt_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", wdt_interrupt_name + "_INTERRUPT_HANDLER", wdt_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", wdt_interrupt_name + "_INTERRUPT_HANDLER", wdt_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateWDT(wdtEnable, wdtAction, wdtInterruptType):
    global setWDTInterruptData
    global nvicInterruptUpdateWDT

    interruptNameDir = "WDT"
    interruptNameAgg = "WDT" + "_GRP"

    if wdtEnable == True and wdtAction == "Generate Interrupt":
        if wdtInterruptType == "AGGREGATE":
            setWDTInterruptData(interruptNameDir, False)
            setWDTInterruptData(interruptNameAgg, True)
        else:
            setWDTInterruptData(interruptNameAgg, False)
            setWDTInterruptData(interruptNameDir, True)
    else:
        setWDTInterruptData(interruptNameAgg, False)
        setWDTInterruptData(interruptNameDir, False)

def nvicInterruptUpdate(symbol, event):
    global nvicInterruptUpdateWDT
    wdtEnable = event["source"].getSymbolByID("WDT_ENABLE").getValue()
    wdtAction = event["source"].getSymbolByID("WDT_ACTION").getValue()
    wdtInterruptType = event["source"].getSymbolByID("WDT_TMR_INTERRUPT_TYPE").getSelectedKey()
    wdtInterruptNameSym = event["source"].getSymbolByID("WDT_TMR_NVIC_INTERRUPT_NAME")

    nvicInterruptUpdateWDT(wdtEnable, wdtAction, wdtInterruptType)

    if wdtInterruptType == "AGGREGATE":
        wdtInterruptNameSym.setValue("WDT" + "_GRP")
    else:
        wdtInterruptNameSym.setValue("WDT")

def updateVisibilityOnWDTEnable(symbol, event):
    symbol.setVisible(event["value"])

def wdtInterruptTypeUpdate(symbol, event):
    wdtEnable = event["source"].getSymbolByID("WDT_ENABLE").getValue()
    wdtAction = event["source"].getSymbolByID("WDT_ACTION").getValue()

    symbol.setVisible(wdtEnable == True and wdtAction == "Generate Interrupt")

def updateTimeoutComment(symbol, event):
    if event["id"] == "WDT_ENABLE":
        symbol.setVisible(event["value"])
    else:
        timeout = 1.007 * (event["value"] + 1)
        comment = "WDT Timeout set to: " + str(timeout) + " ms"
        symbol.setLabel(comment)

def wdtCodeGeneration(symbol, event):
    symbol.setEnabled(event["value"])
###################################################################################################
#############################################  WDT  ###############################################
###################################################################################################

wdtInstances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]")

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
wdtInstanceName.setDefaultValue(wdtInstances.getAttribute("name"))

#WDT menu
wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

#WDT Use
wdtSym_Enable = coreComponent.createBooleanSymbol("WDT_ENABLE", wdtMenu)
wdtSym_Enable.setLabel("Enable WDT ?")
wdtSym_Enable.setDefaultValue(False)

wdtSym_TimeoutAction = coreComponent.createComboSymbol("WDT_ACTION", wdtMenu, ["Reset", "Generate Interrupt"])
wdtSym_TimeoutAction.setLabel("Timeout Action")
wdtSym_TimeoutAction.setDefaultValue("Reset")
wdtSym_TimeoutAction.setVisible(False)
wdtSym_TimeoutAction.setDependencies(updateVisibilityOnWDTEnable, ["WDT_ENABLE"])

## Interrupt Setup
nvic_int_num = {}
nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "WDT"})

# Interrupt type selection
wdtTmrInterruptType = coreComponent.createKeyValueSetSymbol("WDT_TMR_INTERRUPT_TYPE", wdtMenu)
wdtTmrInterruptType.setLabel("Interrupt Type")
if nvic_int_num["direct_nvic_num"] != None:
    wdtTmrInterruptType.addKey("DIRECT", "0", "Direct")
if nvic_int_num["group_nvic_num"] != None:
    wdtTmrInterruptType.addKey("AGGREGATE", "1", "Aggregate")
wdtTmrInterruptType.setDefaultValue(0)
wdtTmrInterruptType.setDisplayMode("Description")
wdtTmrInterruptType.setOutputMode("Key")
wdtTmrInterruptType.setVisible(False)
wdtTmrInterruptType.setDependencies(wdtInterruptTypeUpdate, ["WDT_ENABLE", "WDT_ACTION"])

# Trigger dependency when interrupt type changes
wdtTmrNVICUpdate = coreComponent.createBooleanSymbol("WDT_TMR_UPDATE_NVIC_INTERRUPT", None)
wdtTmrNVICUpdate.setVisible(False)
wdtTmrNVICUpdate.setDependencies(nvicInterruptUpdate, ["WDT_TMR_INTERRUPT_TYPE", "WDT_ENABLE", "WDT_ACTION"])

# Set NVIC interrupt default value
nvicInterruptUpdateWDT(wdtSym_Enable.getValue(), wdtSym_TimeoutAction.getValue(), wdtTmrInterruptType.getValue())

interruptName = ""
if wdtTmrInterruptType.getSelectedKey() == "AGGREGATE":
    interruptName = "WDT" + "_GRP"
else:
    interruptName = "WDT"
wdt_NVIC_InterruptName = coreComponent.createStringSymbol("WDT_TMR_NVIC_INTERRUPT_NAME", None)
wdt_NVIC_InterruptName.setDefaultValue(interruptName)
wdt_NVIC_InterruptName.setVisible(False)

wdtSym_JtagStall = coreComponent.createBooleanSymbol("WDT_JTAG_STALL", wdtMenu)
wdtSym_JtagStall.setLabel("Stall WDT if JTAG/SWD is Enabled?")
wdtSym_JtagStall.setDefaultValue(False)
wdtSym_JtagStall.setVisible(False)
wdtSym_JtagStall.setDependencies(updateVisibilityOnWDTEnable, ["WDT_ENABLE"])

wdtSym_WeekTimerStall = coreComponent.createBooleanSymbol("WDT_WEEK_TIMER_STALL", wdtMenu)
wdtSym_WeekTimerStall.setLabel("Stall WDT if Week Timer is Enabled?")
wdtSym_WeekTimerStall.setDefaultValue(False)
wdtSym_WeekTimerStall.setVisible(False)
wdtSym_WeekTimerStall.setDependencies(updateVisibilityOnWDTEnable, ["WDT_ENABLE"])

wdtSym_HibTimerStall = coreComponent.createBooleanSymbol("WDT_HIBERNATION_TIMER_STALL", wdtMenu)
wdtSym_HibTimerStall.setLabel("Stall WDT if Hibernation Timer is Enabled?")
wdtSym_HibTimerStall.setDefaultValue(False)
wdtSym_HibTimerStall.setVisible(False)
wdtSym_HibTimerStall.setDependencies(updateVisibilityOnWDTEnable, ["WDT_ENABLE"])

wdtSym_TimeOutPeriod = coreComponent.createIntegerSymbol("WDT_TIMEOUT_PERIOD", wdtMenu)
wdtSym_TimeOutPeriod.setLabel("WDT Time-out Period")
wdtSym_TimeOutPeriod.setMin(1)
wdtSym_TimeOutPeriod.setMax(65535)
wdtSym_TimeOutPeriod.setDefaultValue(65535)
wdtSym_TimeOutPeriod.setVisible(False)
wdtSym_TimeOutPeriod.setDependencies(updateVisibilityOnWDTEnable, ["WDT_ENABLE"])

wdtSym_TimeOutComment = coreComponent.createCommentSymbol("WDT_TIMEOUT_IN_MS", wdtMenu)
wdtSym_TimeOutComment.setVisible(False)
timeout = 1.007 * (wdtSym_TimeOutPeriod.getDefaultValue() + 1)
wdtSym_TimeOutComment.setLabel("WDT Timeout set to: " + str(timeout) + " ms")
wdtSym_TimeOutComment.setDependencies(updateTimeoutComment, ["WDT_TIMEOUT_PERIOD", "WDT_ENABLE"])


###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_88/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(wdtSym_Enable.getValue())
wdtHeaderFile.setDependencies(wdtCodeGeneration, ["WDT_ENABLE"])

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_88/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(wdtSym_Enable.getValue())
wdtSourceFile.setDependencies(wdtCodeGeneration, ["WDT_ENABLE"])

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_88/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(wdtSym_Enable.getValue())
wdtSystemDefFile.setDependencies(wdtCodeGeneration, ["WDT_ENABLE"])

wdtSystemInitFile = coreComponent.createFileSymbol("WDT_SYS_INT", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_88/templates/system/initialization.c.ftl")
wdtSystemInitFile.setMarkup(True)
wdtSystemInitFile.setEnabled(wdtSym_Enable.getValue())
wdtSystemInitFile.setDependencies(wdtCodeGeneration, ["WDT_ENABLE"])