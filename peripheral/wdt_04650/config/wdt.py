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

global runModePostScaler
global sleepModePostScaler
global allowedWindowSize
global getTimeOutPeriodRunMode
global getTimeOutPeriodSleepMode
global getTimeOutPeriodWindowMode 
global updateWindowVisibility

######################################### Symbol Constants ###############################################
global CONFIG_FWDT_WINDIS
CONFIG_FWDT_WINDIS = "CONFIG_FWDT_WINDIS"
global SOURCE
SOURCE = "source"
global CONFIG_FWDT_WDTEN
CONFIG_FWDT_WDTEN = "CONFIG_FWDT_WDTEN"
global CORE_COMPONENT
CORE_COMPONENT = "core"
global WDT_MENU_ID 
WDT_MENU_ID = "WDT_MENU"
global WDT_USE_ID
WDT_USE_ID = "WDT_USE"
global WDT_CONFIG_COMMENT_ID
WDT_CONFIG_COMMENT_ID = "WDT_CONFIG_COMMENT"
global WDT_OPERATION_MODE_ID
WDT_OPERATION_MODE_ID = "WDT_OPERATION_MODE"
global CLOCK_FREQUENCY_ID
CLOCK_FREQUENCY_ID = "CLOCK_FREQUENCY"
global WDT_TIMEOUT_PERIOD_RUN_ID
WDT_TIMEOUT_PERIOD_RUN_ID = "WDT_TIMEOUT_PERIOD_RUN"
global WDT_TIMEOUT_PERIOD_SLEEP_ID 
WDT_TIMEOUT_PERIOD_SLEEP_ID = "WDT_TIMEOUT_PERIOD_SLEEP"
global WDT_ALLOWED_WINDOW_SIZE_ID
WDT_ALLOWED_WINDOW_SIZE_ID = "WDT_ALLOWED_WINDOW_SIZE"
global CONVERT_TO_MILLISECONDS
CONVERT_TO_MILLISECONDS = 1000
global WDT
WDT = "WDT"
global WATCHDOG
WATCHDOG = "wdt"
global LPRC_CLOCK
LPRC_CLOCK = "LPRC_CLOCK"
global BFRC_CLOCK
BFRC_CLOCK = "BFRC_CLOCK"
global SYSTEM_CLOCK_FREQ
SYSTEM_CLOCK_FREQ = "sysClockFrequency"
global BFRC256 
global BFRC
global isWdtEnabled

######################################################################################
#### callbacks ####
################################################################################
def updateUseWDT(symbol, event):
       symbol.setReadOnly(event["value"] == "HW")
       symbol.setValue(event["value"] == "HW")

def updateConfigComment(symbol,event):
    symbol.setVisible(event["value"])

def updateOperationModeValues(symbol,event):
    if event["id"] == WDT_USE_ID:
         symbol.setVisible(event["value"])
    else:
        wdtWindow = Database.getSymbolValue(CORE_COMPONENT, CONFIG_FWDT_WINDIS)
        if wdtWindow == "OFF":
            symbol.setValue("WINDOW MODE")
        else:
            symbol.setValue("NON-WINDOW MODE") 

def updateClockFrequencies(symbol,event):
    if event["id"] == WDT_USE_ID:
        symbol.setVisible(event["value"])
    else:
        wdtClock = Database.getSymbolValue(CORE_COMPONENT, "CONFIG_FWDT_RCLKSEL")
        if wdtClock == "BFRC256":
            symbol.setValue(BFRC256)
        elif wdtClock == "SYSTEM":
            systemClockFreq = int(Database.getSymbolValue(CORE_COMPONENT, SYSTEM_CLOCK_FREQ))
            symbol.setValue(systemClockFreq / 4) 
        else:#BFRC
            symbol.setValue(BFRC)

def getTimeOutPeriodRunMode():
    wdtFreq = Database.getSymbolValue(CORE_COMPONENT, CLOCK_FREQUENCY_ID)/32.0

    if wdtFreq == 0:
        return "0 s"
    
    postScaler = int(Database.getSymbolValue(CORE_COMPONENT, runModePostScaler)[2:])
    period = (postScaler * CONVERT_TO_MILLISECONDS)/wdtFreq 

    if period > CONVERT_TO_MILLISECONDS:
        return (str(period / CONVERT_TO_MILLISECONDS) + " s")
    else:
        return (str(period) + " ms")
    
def updateTimeOutPeriodRunValue(symbol, event):
    if event["id"] == WDT_USE_ID:
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(getTimeOutPeriodRunMode())

def getTimeOutPeriodSleepMode():
    wdtFreq = BFRC256/32.0
    postScalerSleep = int(Database.getSymbolValue(CORE_COMPONENT,sleepModePostScaler)[2:])

    period = (postScalerSleep * CONVERT_TO_MILLISECONDS)/wdtFreq
    if period > CONVERT_TO_MILLISECONDS:
        return (str(period / CONVERT_TO_MILLISECONDS) + " s")
    else:
        return (str(period) + " ms")
    
def updateTimeOutPeriodSleepValue(symbol,event):
    if event["id"] == WDT_USE_ID:
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(getTimeOutPeriodSleepMode())

def getTimeOutPeriodWindowMode():
    windowSize = int(Database.getSymbolValue(CORE_COMPONENT, allowedWindowSize)[3:])
    windowSize = windowSize / 100.0 
    wdtFreq = Database.getSymbolValue(CORE_COMPONENT, CLOCK_FREQUENCY_ID)/32.0

    if wdtFreq == 0:
        return "0 s"
    postScaler = int(Database.getSymbolValue(CORE_COMPONENT, runModePostScaler)[2:])

    period = (postScaler * CONVERT_TO_MILLISECONDS * windowSize)/wdtFreq
   
    if period > CONVERT_TO_MILLISECONDS:
        return (str(period / CONVERT_TO_MILLISECONDS) + " s")
    else:
        return (str(period) + " ms")
    
def updateAllowedWindowSizeTimeOutPeriod(symbol, event):
    if event["id"] == allowedWindowSize or event["id"] == runModePostScaler or event["id"] == CLOCK_FREQUENCY_ID:
        symbol.setValue(getTimeOutPeriodWindowMode())
    else:
        windowVisible = event[SOURCE].getSymbolByID(CONFIG_FWDT_WINDIS)
        wdtEnable = event[SOURCE].getSymbolByID(WDT_USE_ID)
        
        updateWindowVisibility(symbol, windowVisible, wdtEnable)

def updateWindowVisibility(wdtWindow, windowVisible, wdtEnable):
    if wdtEnable.getValue() == True:
            if windowVisible.getValue() == "OFF":
                wdtWindow.setVisible(True)
            else:
                wdtWindow.setVisible(False)
    else:
        wdtWindow.setVisible(False)

def getAtdfParameterValue(moduleName, instanceName, paramName):
    atdfPath = '/avr-tools-device-file/devices/device/peripherals/module@[name="' + moduleName + '"]/instance@[name="' + instanceName + '"]/parameters/param@[name="' + paramName + '"]'
    paramNode = ATDF.getNode(atdfPath)
    if paramNode is not None:
        return paramNode.getAttribute("value")
    return None

def onUseWdtChanged(symbol, event):
    symbol.setEnabled(event["value"])
    symbol.setEnabled(event["value"])

##################### ATDF Data ############################################################
BFRC256 = int(getAtdfParameterValue(WATCHDOG, WDT, LPRC_CLOCK))
BFRC =  int(getAtdfParameterValue(WATCHDOG, WDT, BFRC_CLOCK))

valueGroupNode_RWDTPS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="FWDT_RWDTPS"]')
if valueGroupNode_RWDTPS is not None:
    runModePostScaler = "CONFIG_FWDT_RWDTPS"

valueGroupNode_SWDTMPS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="FWDT_SWDTMPS"]')
if valueGroupNode_SWDTMPS is not None:
    sleepModePostScaler = "CONFIG_FWDT_SWDTMPS"

valueGroupNode_WDTWIN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="FWDT_WDTWIN"]')
if valueGroupNode_WDTWIN is not None:
    allowedWindowSize = "CONFIG_FWDT_WDTWIN"

global isWDTEnabled
isWDTEnabled = (Database.getSymbolValue(CORE_COMPONENT, CONFIG_FWDT_WDTEN) == "HW")
isWDTWindowDisabled = (Database.getSymbolValue(CORE_COMPONENT, CONFIG_FWDT_WINDIS) == "ON") 

################## Symbol Creation for WDT Component ###############################################
wdtInstanceName = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="wdt"]/instance@[name="WDT"]')

wdtInstance = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstance.setVisible(False)
wdtInstance.setDefaultValue(wdtInstanceName.getAttribute("name"))

#WDT menu
wdtMenu = coreComponent.createMenuSymbol(WDT_MENU_ID, None)
wdtMenu.setLabel("WDT")

# Use WDT 
wdtSys_Use = coreComponent.createBooleanSymbol(WDT_USE_ID, wdtMenu)
wdtSys_Use.setLabel("Use WDT")
wdtSys_Use.setDefaultValue(isWDTEnabled) 
wdtSys_Use.setReadOnly(isWDTEnabled)
wdtSys_Use.setDependencies(updateUseWDT, [CONFIG_FWDT_WDTEN])
wdtSys_Use.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:wdt_04650;register:WDTCON")

#WDT Configuration comment
wdtSys_ConfigComment = coreComponent.createCommentSymbol(WDT_CONFIG_COMMENT_ID, wdtSys_Use) 
wdtSys_ConfigComment.setLabel("**** Configure WDT From Device Configuration bits Values ****")
wdtSys_ConfigComment.setVisible(isWDTEnabled)
wdtSys_ConfigComment.setDependencies(updateConfigComment, [WDT_USE_ID])

#WDT Operation Mode
wdtSys_OperationMode = coreComponent.createComboSymbol(WDT_OPERATION_MODE_ID, wdtSys_Use, ["NON-WINDOW MODE","WINDOW MODE"])
wdtSys_OperationMode.setLabel("Configure WDT Operation Mode")
if isWDTWindowDisabled:
   wdtSys_OperationMode.setDefaultValue("NON-WINDOW MODE")
else:
     wdtSys_OperationMode.setDefaultValue("WINDOW MODE")
wdtSys_OperationMode.setVisible(isWDTEnabled)
wdtSys_OperationMode.setReadOnly(True)
wdtSys_OperationMode.setDependencies(updateOperationModeValues, [WDT_USE_ID, CONFIG_FWDT_WINDIS])
wdtSys_OperationMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:wdt_04650;register:WDTCON")

#WDT Clock
wdtSys_ClockFrequency = coreComponent.createIntegerSymbol(CLOCK_FREQUENCY_ID, wdtSys_Use)
wdtSys_ClockFrequency.setLabel("WDT Clock Frequency (in Hz)")
wdtSys_ClockFrequency.setVisible(isWDTEnabled)
wdtSys_ClockFrequency.setReadOnly(True)
wdtSys_ClockFrequency.setDefaultValue(BFRC256)
wdtSys_ClockFrequency.setDependencies(updateClockFrequencies, [WDT_USE_ID, "CONFIG_FWDT_RCLKSEL", CORE_COMPONENT+"."+SYSTEM_CLOCK_FREQ])
wdtSys_ClockFrequency.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:wdt_04650;register:WDTCON")

#Timeout Period in Run Mode
wdtSys_TimeOutPeriodRun = coreComponent.createStringSymbol(WDT_TIMEOUT_PERIOD_RUN_ID, wdtSys_Use)
wdtSys_TimeOutPeriodRun.setLabel("Configured WDT Time-out Period in Run Mode")
wdtSys_TimeOutPeriodRun.setDefaultValue(getTimeOutPeriodRunMode())
wdtSys_TimeOutPeriodRun.setReadOnly(True)
wdtSys_TimeOutPeriodRun.setVisible(isWDTEnabled)
wdtSys_TimeOutPeriodRun.setDependencies(updateTimeOutPeriodRunValue, [WDT_USE_ID, CLOCK_FREQUENCY_ID, runModePostScaler])
wdtSys_TimeOutPeriodRun.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:wdt_04650;register:WDTCON")

#Timeout Period in Sleep Mode
wdtSys_TimeOutPeriodSleep = coreComponent.createStringSymbol(WDT_TIMEOUT_PERIOD_SLEEP_ID, wdtSys_Use)
wdtSys_TimeOutPeriodSleep.setLabel("Configured WDT Time-out Period in Sleep Mode")
wdtSys_TimeOutPeriodSleep.setVisible(isWDTEnabled)
wdtSys_TimeOutPeriodSleep.setReadOnly(True)
wdtSys_TimeOutPeriodSleep.setDefaultValue(getTimeOutPeriodSleepMode())
wdtSys_TimeOutPeriodSleep.setDependencies(updateTimeOutPeriodSleepValue, [WDT_USE_ID, sleepModePostScaler])

#Window period
wdtSys_AllowedWindowSize = coreComponent.createStringSymbol(WDT_ALLOWED_WINDOW_SIZE_ID, wdtSys_Use)
wdtSys_AllowedWindowSize.setLabel("Configured WDT Time-out Period in Allowed Window Size")
wdtSys_AllowedWindowSize.setReadOnly(True)
wdtSys_AllowedWindowSize.setDefaultValue(getTimeOutPeriodWindowMode())
wdtSys_AllowedWindowSize.setVisible(False)
wdtSys_AllowedWindowSize.setDependencies(updateAllowedWindowSizeTimeOutPeriod, [ WDT_USE_ID, allowedWindowSize, CONFIG_FWDT_WINDIS, runModePostScaler, CLOCK_FREQUENCY_ID ])
wdtSys_TimeOutPeriodSleep.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:wdt_04650;register:WDTCON")

##################### Code Generation #######################################

configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_04650/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_wdt.h")
wdtHeaderFile.setDestPath("/peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName +"/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(False)
wdtHeaderFile.setDependencies(onUseWdtChanged, [WDT_USE_ID])

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_04650/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_wdt.c")
wdtSourceFile.setDestPath("/peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName +"/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(False)
wdtSourceFile.setDependencies(onUseWdtChanged, [WDT_USE_ID])

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYS_DEF", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_04650/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(False)
wdtSystemDefFile.setDependencies(onUseWdtChanged, [WDT_USE_ID])