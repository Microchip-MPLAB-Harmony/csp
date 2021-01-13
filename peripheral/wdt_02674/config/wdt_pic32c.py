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

global wdtEnableFuse
global wdtWindowSizeFuse

global wdtSym_Use
global wdtHeaderFile
global wdtSourceFile
global wdtSystemDefFile

global getWDTTimeOutPeriod
global getWDTAllowedWindowPeriod
global getWDTTimeOutPeriod_Sleep

global wdtAllowedWindowDictionary

global wdtPreScalerFuse
global LPRC_FREQ
LPRC_FREQ = 32768

wdtAllowedWindowDictionary = {

    "WINSZ_25"      :       "0.25",
    "WINSZ_37"      :       "0.375",
    "WINSZ_50"      :       "0.50",
    "WINSZ_75"      :       "0.75"
}

###################################################################################################
########################################## Callbacks ##############################################
###################################################################################################

def getWDTAllowedWindowPeriod():
        
    windowSize = Database.getSymbolValue("core", wdtWindowSizeFuse)    
    wdtFreq = Database.getSymbolValue("core", "WDT_CLOCK_FREQUENCY")/32.0
    postScaler = int(Database.getSymbolValue("core", wdtPreScalerFuse)[2:])

    period = (postScaler * 1000 * float(wdtAllowedWindowDictionary[windowSize]))/wdtFreq
    if period > 1000:
        return (str(period/1000) + " s")
    else:
        return (str(period) + " ms")

def getWDTTimeOutPeriod():
    wdtFreq = Database.getSymbolValue("core", "WDT_CLOCK_FREQUENCY")/32.0
    postScaler = int(Database.getSymbolValue("core", wdtPreScalerFuse)[2:])

    period = (postScaler * 1000)/wdtFreq
    if period > 1000:
        return (str(period/1000) + " s")
    else:
        return (str(period) + " ms")

def getWDTTimeOutPeriod_Sleep():
    wdtFreq = LPRC_FREQ/32.0
    postScaler = int(Database.getSymbolValue("core", "CONFIG_WDTPSS")[3:])

    period = (postScaler * 1000)/wdtFreq
    if period > 1000:
        return (str(period/1000) + " s")
    else:
        return (str(period) + " ms")

def updateWDTUseProperties(symbol, event):

    symbol.setReadOnly((event["value"] == "ON"))
    symbol.setValue((event["value"] == "ON"), 1)

def updateWDTTimeOutPeriodVisibleProperty(symbol, event):

    if event["id"] == "WDT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(getWDTTimeOutPeriod(), 1)

def updateWDTTimeOutPeriodVisibleProperty_Sleep(symbol, event):

    if event["id"] == "WDT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(getWDTTimeOutPeriod_Sleep(), 1)

def dswdtEnableStatusUpdate(symbol,event):
    if event["value"] == "OFF":
        symbol.setValue("DISABLED")
    else:
        symbol.setValue("ENABLED")

global getDSWDTTimeOutPeriod
def getDSWDTTimeOutPeriod():
    dswdtFreq = Database.getSymbolValue("core", "DSWDT_CLOCK_FREQUENCY")
    postScaler = int(Database.getSymbolValue("core", "CONFIG_DSWDTPS")[4:])

    period = (pow(2,postScaler+4) * 1000.0)/dswdtFreq

    if period < 1000:
        DSWDTTimeoutPeriod = (str(period) + " ms")
    elif period < 1000 * 60:
        DSWDTTimeoutPeriod = (str(period/1000) + " sec")
    elif period < 1000 * 60 * 60:
        DSWDTTimeoutPeriod = (str(period/(1000 * 60)) + " minutes")
    elif period < 1000 * 60 * 60 * 24:
        DSWDTTimeoutPeriod = (str(period/(1000 * 60 * 60)) + " hours")
    else:
        DSWDTTimeoutPeriod = (str(period/(1000 * 60 * 60 * 24)) + " days")

    return DSWDTTimeoutPeriod

def updateDSWDTTimeOutPeriodVisibleProperty(symbol, event):
    if event["id"] == "CONFIG_DSWDTEN":
        if event["value"] == "OFF":
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)
    else:
        symbol.setValue(getDSWDTTimeOutPeriod(), 1)


def updateWDTWindowModeEnableVisibleProperty(symbol, event):

    if event["id"] == "WDT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(event["value"], 1)

def updateWDTConfigCommentVisibleProperty(symbol, event):

    wdtHeaderFile.setEnabled(event["value"])
    wdtSourceFile.setEnabled(event["value"])
    wdtSystemDefFile.setEnabled(event["value"])

    symbol.setVisible(event["value"])

def updateWDTAllowedWindowPeriodVisibleProperty(symbol, event):
    global wdtPreScalerFuse
    if event["id"] == wdtWindowSizeFuse or event["id"] == wdtPreScalerFuse or event["id"] == "WDT_CLOCK_FREQUENCY":
        symbol.setValue(getWDTAllowedWindowPeriod(), 1)
    else:
        if wdtSym_Use.getValue() == True and Database.getSymbolValue("core", "CONFIG_WINDIS") == "WINDOW":
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

###################################################################################################
#############################################  WDT  ###############################################
###################################################################################################

wdtEnableFuse = "CONFIG_FWDTEN"
wdtWindowSizeFuse = "CONFIG_FWDTWINSZ"

if Database.getSymbolValue("core", "CONFIG_FWDTEN") == None:
    wdtEnableFuse = "CONFIG_WDTEN"

if Database.getSymbolValue("core", "CONFIG_FWDTWINSZ") == None:
    wdtWindowSizeFuse = "CONFIG_WDTWINSZ"

if Database.getSymbolValue("core", "CONFIG_WDTPSR") == None:
    wdtPreScalerFuse = "CONFIG_WDTPS"
else:
    wdtPreScalerFuse = "CONFIG_WDTPSR"  

isWDTEnabled = (Database.getSymbolValue("core", wdtEnableFuse) == "ON")
isWDTWindowModeEnabled = (Database.getSymbolValue("core", "CONFIG_WINDIS") == "WINDOW")

wdtValGrp_DEVCFG1__WDTPSS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSES"]/value-group@[name="DEVCFG1__WDTPSS"]')
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
wdtSym_Use.setDependencies(updateWDTUseProperties, [wdtEnableFuse])

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
wdtSym_TimeOutPeriod.setDefaultValue(getWDTTimeOutPeriod())
wdtSym_TimeOutPeriod.setReadOnly(True)
wdtSym_TimeOutPeriod.setVisible(isWDTEnabled)
wdtSym_TimeOutPeriod.setDependencies(updateWDTTimeOutPeriodVisibleProperty, ["WDT_USE","WDT_CLOCK_FREQUENCY", wdtPreScalerFuse])

#WDT Time-out Period for Sleep Mode
if (wdtValGrp_DEVCFG1__WDTPSS is not None):
    wdtSym_TimeOutPeriodSleep = coreComponent.createStringSymbol("WDT_TIMEOUT_PERIOD_SLEEP", wdtSym_Use)
    wdtSym_TimeOutPeriodSleep.setLabel("Configured WDT Time-out Period in Sleep Mode")
    wdtSym_TimeOutPeriodSleep.setDefaultValue(getWDTTimeOutPeriod_Sleep())
    wdtSym_TimeOutPeriodSleep.setReadOnly(True)
    wdtSym_TimeOutPeriodSleep.setVisible(isWDTEnabled)
    wdtSym_TimeOutPeriodSleep.setDependencies(updateWDTTimeOutPeriodVisibleProperty_Sleep, ["WDT_USE", "CONFIG_WDTPSS"])

#WDT Allowed Window Period
wdtSym_AllowedWindowPeriod = coreComponent.createStringSymbol("WDT_ALLOWED_WINDOW_PERIOD", wdtSym_Use)
wdtSym_AllowedWindowPeriod.setLabel("Configured WDT Allowed Window Period")
wdtSym_AllowedWindowPeriod.setDefaultValue(getWDTAllowedWindowPeriod())
wdtSym_AllowedWindowPeriod.setReadOnly(True)
wdtSym_AllowedWindowPeriod.setVisible(isWDTEnabled and isWDTWindowModeEnabled)
wdtSym_AllowedWindowPeriod.setDependencies(updateWDTAllowedWindowPeriodVisibleProperty, ["WDT_USE", wdtWindowSizeFuse, "CONFIG_WINDIS", wdtPreScalerFuse,"WDT_CLOCK_FREQUENCY"])

###################################################################################################
#######################################  Deep Sleep WDT  ##########################################
###################################################################################################
dswdtMenu = coreComponent.createMenuSymbol("DSWDT_MENU", None)
dswdtMenu.setLabel("Deep Sleep WDT (DSWDT)")

dswdtSym_ConfigComment = coreComponent.createCommentSymbol("DSWDT_CONFIG_COMMENT", dswdtMenu)
dswdtSym_ConfigComment.setLabel("************** Configure DSWDT From Device Configuration Fuses ***************")

dswdtSym_EnableStatus = coreComponent.createStringSymbol("DSWDT_ENABLE_STATUS", dswdtMenu)
dswdtSym_EnableStatus.setLabel("Configured DSWDT Enable Status")
dswdtSym_EnableStatus.setDefaultValue("DISABLED")
dswdtSym_EnableStatus.setReadOnly(True)
dswdtSym_EnableStatus.setDependencies(dswdtEnableStatusUpdate, ["CONFIG_DSWDTEN"])

dswdtSym_TimeOutPeriod = coreComponent.createStringSymbol("DSWDT_TIMEOUT_PERIOD", dswdtMenu)
dswdtSym_TimeOutPeriod.setLabel("Configured DSWDT Time-out Period")
dswdtSym_TimeOutPeriod.setDefaultValue(getDSWDTTimeOutPeriod())
dswdtSym_TimeOutPeriod.setReadOnly(True)
dswdtSym_TimeOutPeriod.setVisible(False)
dswdtSym_TimeOutPeriod.setDependencies(updateDSWDTTimeOutPeriodVisibleProperty, ["CONFIG_DSWDTEN","DSWDT_CLOCK_FREQUENCY", "CONFIG_DSWDTPS"])
###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_02674/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(wdtSym_Use.getValue())

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_02674/templates/plib_wdt_pic32c.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(wdtSym_Use.getValue())

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_02674/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(wdtSym_Use.getValue())
