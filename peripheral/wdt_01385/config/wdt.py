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

global getWDTTimeOutPeriod
global getWDTAllowedWindowPeriod

global wdtTimeOutDictionary
global wdtAllowedWindowDictionary

wdtTimeOutDictionary = {

    #Entry          :       [#Period,   #TimeUnit(mili-second/second)]

    "PS1"           :       ["1",        "ms"],
    "PS2"           :       ["2",        "ms"],
    "PS4"           :       ["4",        "ms"],
    "PS8"           :       ["8",        "ms"],
    "PS16"          :       ["16",       "ms"],
    "PS32"          :       ["32",       "ms"],
    "PS64"          :       ["64",       "ms"],
    "PS128"         :       ["128",      "ms"],
    "PS256"         :       ["256",      "ms"],
    "PS512"         :       ["512",      "ms"],
    "PS1024"        :       ["1.024",    "s"],
    "PS2048"        :       ["2.048",    "s"],
    "PS4096"        :       ["4.096",    "s"],
    "PS8192"        :       ["8.192",    "s"],
    "PS16384"       :       ["16.384",   "s"],
    "PS32768"       :       ["32.768",   "s"],
    "PS65536"       :       ["65.536",   "s"],
    "PS131072"      :       ["131.072",  "s"],
    "PS262144"      :       ["262.144",  "s"],
    "PS524288"      :       ["524.288",  "s"],
    "PS1048576"     :       ["1048.576", "s"]
}

wdtAllowedWindowDictionary = {

    "WINSZ_25"      :       "0.25",
    "WINSZ_37"      :       "37.5",
    "WINSZ_50"      :       "0.50",
    "WINSZ_75"      :       "0.75"
}

###################################################################################################
########################################## Callbacks ##############################################
###################################################################################################

def getWDTAllowedWindowPeriod(period, windowSize):

    allowedPeriod = str((float(wdtTimeOutDictionary[period][0]) * float(wdtAllowedWindowDictionary[windowSize])))

    return (allowedPeriod + " " + wdtTimeOutDictionary[period][1])

def getWDTTimeOutPeriod(period):

    return (wdtTimeOutDictionary[period][0] + " " + wdtTimeOutDictionary[period][1])

def updateWDTUseProperties(symbol, event):

    symbol.setReadOnly((event["value"] == "ON"))
    symbol.setValue((event["value"] == "ON"), 1)

def updateWDTTimeOutPeriodVisibleProperty(symbol, event):

    if event["id"] == "WDT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(getWDTTimeOutPeriod(event["value"]), 1)

def updateWDTWindowModeEnableVisibleProperty(symbol, event):

    if event["id"] == "WDT_USE":
        symbol.setVisible(event["value"])
    else:
        if event["value"] == "ON":
            symbol.setValue("WINDOW", 1)
        else:
            symbol.setValue("NORMAL", 1)

def updateWDTConfigCommentVisibleProperty(symbol, event):

    wdtHeaderFile.setEnabled(event["value"])
    wdtSourceFile.setEnabled(event["value"])
    wdtSystemDefFile.setEnabled(event["value"])

    symbol.setVisible(event["value"])

def updateWDTAllowedWindowPeriodVisibleProperty(symbol, event):

    if event["id"] == "CONFIG_FWDTWINSZ" or event["id"] == "CONFIG_WDTPS":
        period = Database.getSymbolValue("core", "CONFIG_WDTPS")
        windowSize = Database.getSymbolValue("core", "CONFIG_FWDTWINSZ")

        symbol.setValue(getWDTAllowedWindowPeriod(period, windowSize), 1)
    else:
        if wdtSym_Use.getValue() == True and Database.getSymbolValue("core", "CONFIG_WINDIS") == "ON":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

###################################################################################################
#############################################  WDT  ###############################################
###################################################################################################

isWDTEnabled = (Database.getSymbolValue("core", "CONFIG_FWDTEN") == "ON")
isWDTWindowModeEnabled = (Database.getSymbolValue("core", "CONFIG_WINDIS") == "ON")
wdtTimeOut = Database.getSymbolValue("core", "CONFIG_WDTPS")
wdtAllowedWindowSize = Database.getSymbolValue("core", "CONFIG_FWDTWINSZ")

wdtInstances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]")

wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
wdtInstanceName.setDefaultValue(wdtInstances.getAttribute("name"))

#WDT menu
wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

#WDT Use
wdtSym_Use = coreComponent.createBooleanSymbol("WDT_USE", wdtMenu)
wdtSym_Use.setLabel("Use WDT ?")
wdtSym_Use.setDefaultValue(isWDTEnabled)
wdtSym_Use.setReadOnly(isWDTEnabled)
wdtSym_Use.setDependencies(updateWDTUseProperties, ["CONFIG_FWDTEN"])

#WDT Configuration comment
wdtSym_ConfigComment = coreComponent.createCommentSymbol("WDT_CONFIG_COMMENT", wdtSym_Use)
wdtSym_ConfigComment.setLabel("************** Configure WDT From Device Configuration Fuses ***************")
wdtSym_ConfigComment.setVisible(isWDTEnabled)
wdtSym_ConfigComment.setDependencies(updateWDTConfigCommentVisibleProperty, ["WDT_USE"])

#WDT Operation mode
wdtSym_WindowMode = coreComponent.createComboSymbol("WDT_MODE", wdtSym_Use, ["NORMAL", "WINDOW"])
wdtSym_WindowMode.setLabel("Configured WDT Operation Mode")
if isWDTEnabled and isWDTWindowModeEnabled:
    wdtSym_WindowMode.setDefaultValue("WINDOW")
else:
    wdtSym_WindowMode.setDefaultValue("NORMAL")
wdtSym_WindowMode.setVisible(isWDTEnabled)
wdtSym_WindowMode.setReadOnly(True)
wdtSym_WindowMode.setDependencies(updateWDTWindowModeEnableVisibleProperty, ["WDT_USE", "CONFIG_WINDIS"])

#WDT Time-out Period
wdtSym_TimeOutPeriod = coreComponent.createStringSymbol("WDT_TIMEOUT_PERIOD", wdtSym_Use)
wdtSym_TimeOutPeriod.setLabel("Configured WDT Time-out Period")
wdtSym_TimeOutPeriod.setDefaultValue(getWDTTimeOutPeriod(wdtTimeOut))
wdtSym_TimeOutPeriod.setReadOnly(True)
wdtSym_TimeOutPeriod.setVisible(isWDTEnabled)
wdtSym_TimeOutPeriod.setDependencies(updateWDTTimeOutPeriodVisibleProperty, ["WDT_USE", "CONFIG_WDTPS"])

#WDT Allowed Window Period
wdtSym_AllowedWindowPeriod = coreComponent.createStringSymbol("WDT_ALLOWED_WINDOW_PERIOD", wdtSym_Use)
wdtSym_AllowedWindowPeriod.setLabel("Configured WDT Allowed Window Period")
wdtSym_AllowedWindowPeriod.setDefaultValue(getWDTAllowedWindowPeriod(wdtTimeOut, wdtAllowedWindowSize))
wdtSym_AllowedWindowPeriod.setReadOnly(True)
wdtSym_AllowedWindowPeriod.setVisible(isWDTEnabled and isWDTWindowModeEnabled)
wdtSym_AllowedWindowPeriod.setDependencies(updateWDTAllowedWindowPeriodVisibleProperty, ["WDT_USE", "CONFIG_FWDTWINSZ", "CONFIG_WINDIS", "CONFIG_WDTPS"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_01385/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(wdtSym_Use.getValue())

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_01385/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(wdtSym_Use.getValue())

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_01385/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(wdtSym_Use.getValue())
