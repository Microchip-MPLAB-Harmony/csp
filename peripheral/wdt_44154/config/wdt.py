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

global wdtInstanceName
global wdtInterruptEnable
global wdtInterruptHandler
global wdtInterruptHandlerLock
global wdtInterruptCauseSet
global wdtCountsToMilliSecs
global wdtMilliSecsToCounts
global wdtClockFrequency

wdtClockFrequency = 32000                               # if xtal = 32768, if rc = 32000
wdtInterruptCauseSet = set(())

def wdtUpdateInterrupt(symbol, event):
    global wdtInterruptCauseSet

    if event["symbol"].getSelectedKey() == "Interrupt":
        wdtInterruptCauseSet.add( event[ "id" ] )
    elif event[ "id" ] in wdtInterruptCauseSet:
        wdtInterruptCauseSet.remove( event[ "id" ] )

    Database.clearSymbolValue("core", wdtInterruptEnable)
    Database.clearSymbolValue("core", wdtInterruptHandler)
    Database.clearSymbolValue("core", wdtInterruptHandlerLock)

    if len( wdtInterruptCauseSet ):
        Database.setSymbolValue("core", wdtInterruptEnable, True, 2)
        Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", wdtInterruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", wdtInterruptEnable, False, 2)
        Database.setSymbolValue("core", wdtInterruptHandler, wdtInstanceName.getValue() + "_Handler", 2)
        Database.setSymbolValue("core", wdtInterruptHandlerLock, False, 2)


def wdtEnableCfgMenu(wdtCfgMenu, event):
    wdtCfgMenu.setVisible(event["value"])
    component = wdtCfgMenu.getComponent()
    component.getSymbolByID("WDT_HEADER_FILE").setEnabled(event["value"])
    component.getSymbolByID("WDT_SOURCE_FILE").setEnabled(event["value"])
    component.getSymbolByID("WDT_SYSTEM_INIT_FILE").setEnabled(event["value"])
    component.getSymbolByID("WDT_SYSTEM_DEF_FILE").setEnabled(event["value"])


def wdtCountsToMilliSecs( counts ):
    global wdtClockFrequency
    # 1000 for milliSeconds and 128 is the intrinsic value used by this HW IP
    return int( round( float( counts * 128 * 1000) / wdtClockFrequency ) )


def wdtMilliSecsToCounts( milliSecs ):
    global wdtClockFrequency
    # 128 is the intrinsic value used by this HW IP
    return int( (milliSecs * wdtClockFrequency) / (128 * 1000) )


def wdtMilliSecUpdate( symbol, event ):
    global wdtCountsToMilliSecs
    symbol.setValue( wdtCountsToMilliSecs( event["value"] ), 1 )


def wdtCountChange( symbol, event ):
    symbol.setMax( event[ 'value' ] - 1 )


wdtInstanceName = coreComponent.createStringSymbol("WDT_INSTANCE_NAME", None)
wdtInstanceName.setVisible(False)
instances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"WDT\"]").getChildren()
wdtInstanceName.setDefaultValue(instances[0].getAttribute("name"))
Log.writeInfoMessage("Loading " + wdtInstanceName.getValue() + "for " + Variables.get("__PROCESSOR"))

wdtMenu = coreComponent.createMenuSymbol("WDT_MENU", None)
wdtMenu.setLabel("WDT")

wdtEnable = coreComponent.createBooleanSymbol("WDT_ENABLE", wdtMenu)
wdtEnable.setLabel("Enable Watch Dog Timer?")
wdtEnable.setDefaultValue(False)

wdtCfgMenu = coreComponent.createMenuSymbol("WDT_CFG_MENU", wdtMenu)
wdtCfgMenu.setLabel("Configuration")
wdtCfgMenu.setDependencies(wdtEnableCfgMenu, ["WDT_ENABLE"])
wdtCfgMenu.setVisible(False)
###
wdtPeriodExpireTuple = [ ("None", "0", "No Action"), ("Interrupt", "1", "Interrupt"), ("Reset", "2", "Reset") ]
wdtPeriodExpiration = coreComponent.createKeyValueSetSymbol( "WDT_PERIOD_EXPIRATION", wdtCfgMenu )
wdtPeriodExpiration.setLabel( "Period Expiration Action" )
for tupleElem in wdtPeriodExpireTuple:
    wdtPeriodExpiration.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
wdtPeriodExpiration.setOutputMode( "Key" )
wdtPeriodExpiration.setDisplayMode( "Description" )
wdtPeriodExpiration.setDefaultValue( 0 )
wdtPeriodExpiration.setSelectedKey( str( wdtPeriodExpireTuple[ 0 ][ 0 ] ), 0 )
wdtPeriodExpiration.setDependencies(wdtUpdateInterrupt, ["WDT_PERIOD_EXPIRATION"])

wdtPeriodCount = coreComponent.createIntegerSymbol("WDT_PERIOD_COUNT", wdtPeriodExpiration)
wdtPeriodCount.setLabel("Period (counts)")
wdtPeriodCount.setMin(0x002)
wdtPeriodCount.setMax(0xfff)        # just under 16 seconds
wdtPeriodCount.setDefaultValue( wdtMilliSecsToCounts( 16000 ) )
wdtPeriodCount.setValue(wdtPeriodCount.getDefaultValue(), 1)

wdtPeriodMilliSeconds = coreComponent.createIntegerSymbol("WDT_PERIOD_MILLISECONDS", wdtPeriodExpiration)
wdtPeriodMilliSeconds.setLabel("Period (mSecs)")
wdtPeriodMilliSeconds.setDependencies(wdtMilliSecUpdate, ["WDT_PERIOD_COUNT"])
wdtPeriodMilliSeconds.setReadOnly(True)
wdtPeriodMilliSeconds.setDefaultValue( wdtCountsToMilliSecs( wdtPeriodCount.getValue() ) )
###
wdtLevelExpireTuple = [ ("None", "0", "No Action"), ("Interrupt", "1", "Interrupt")]
wdtLevelExpiration = coreComponent.createKeyValueSetSymbol( "WDT_LEVEL_EXPIRATION", wdtCfgMenu )
wdtLevelExpiration.setLabel( "Level Expiration Action" )
for tupleElem in wdtLevelExpireTuple:
    wdtLevelExpiration.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
wdtLevelExpiration.setOutputMode( "Key" )
wdtLevelExpiration.setDisplayMode( "Description" )
wdtLevelExpiration.setDefaultValue( 0 )
wdtLevelExpiration.setSelectedKey( str( wdtLevelExpireTuple[ 0 ][ 0 ] ), 0 )
wdtLevelExpiration.setDependencies(wdtUpdateInterrupt, ["WDT_LEVEL_EXPIRATION"])

wdtLevelThresholdCount = coreComponent.createIntegerSymbol("WDT_LEVEL_THRESHOLD_COUNT", wdtLevelExpiration)
wdtLevelThresholdCount.setLabel("Level Threshold (counts)")
wdtLevelThresholdCount.setMin(0x001)
wdtLevelThresholdCount.setMax(wdtPeriodCount.getMax() - 1)
wdtLevelThresholdCount.setDependencies(wdtCountChange, ["WDT_PERIOD_COUNT"])
wdtLevelThresholdCount.setDefaultValue( wdtMilliSecsToCounts( 15000 ) )

wdtLevelThresholdMilliSeconds = coreComponent.createIntegerSymbol("WDT_LEVEL_THRESHOLD_MILLISECONDS", wdtLevelExpiration)
wdtLevelThresholdMilliSeconds.setLabel("Level Threshold (mSecs)")
wdtLevelThresholdMilliSeconds.setDependencies(wdtMilliSecUpdate, ["WDT_LEVEL_THRESHOLD_COUNT"])
wdtLevelThresholdMilliSeconds.setReadOnly(True)
wdtLevelThresholdMilliSeconds.setDefaultValue( wdtCountsToMilliSecs( wdtLevelThresholdCount.getValue() ) )
###
wdtEarlyResetTuple = [ ("None", "0", "No Action"), ("Interrupt", "1", "Interrupt"), ("Reset", "2", "Reset") ]
wdtEarlyResetAction = coreComponent.createKeyValueSetSymbol( "WDT_EARLY_RESET_ACTION", wdtCfgMenu )
wdtEarlyResetAction.setLabel( "Early Reset Action" )
for tupleElem in wdtEarlyResetTuple:
    wdtEarlyResetAction.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
wdtEarlyResetAction.setOutputMode( "Key" )
wdtEarlyResetAction.setDisplayMode( "Description" )
wdtEarlyResetAction.setDefaultValue( 0 )
wdtEarlyResetAction.setSelectedKey( str( wdtEarlyResetTuple[ 0 ][ 0 ] ), 0 )
wdtEarlyResetAction.setDependencies(wdtUpdateInterrupt, ["WDT_EARLY_RESET_ACTION"])

wdtEarlyResetThresholdCount = coreComponent.createIntegerSymbol("WDT_EARLY_RESET_THRESHOLD_COUNT", wdtEarlyResetAction)
wdtEarlyResetThresholdCount.setLabel("Early Reset Threshold (counts)")
wdtEarlyResetThresholdCount.setMin(0x000)
wdtEarlyResetThresholdCount.setMax(wdtPeriodCount.getMax() - 2)
wdtEarlyResetThresholdCount.setDependencies(wdtCountChange, ["WDT_LEVEL_THRESHOLD_COUNT"])
wdtEarlyResetThresholdCount.setDefaultValue(wdtMilliSecsToCounts( 1000 ))

wdtEarlyResetThresholdMilliSeconds = coreComponent.createIntegerSymbol("WDT_EARLY_RESET_THRESHOLD_MILLISECONDS", wdtEarlyResetAction)
wdtEarlyResetThresholdMilliSeconds.setLabel("Early Reset Threshold (mSecs)")
wdtEarlyResetThresholdMilliSeconds.setDependencies( wdtMilliSecUpdate, ["WDT_EARLY_RESET_THRESHOLD_COUNT"])
wdtEarlyResetThresholdMilliSeconds.setReadOnly(True)
wdtEarlyResetThresholdMilliSeconds.setDefaultValue( wdtCountsToMilliSecs( wdtEarlyResetThresholdCount.getValue() ) )
###
wdtStopWhenIdle = coreComponent.createBooleanSymbol("WDT_STOP_WHEN_IDLE", wdtCfgMenu)
wdtStopWhenIdle.setLabel("Stop When Idle")
wdtStopWhenIdle.setDefaultValue(True)

wdtStopWhenDebugging = coreComponent.createBooleanSymbol("WDT_STOP_WHEN_DEBUGGING", wdtCfgMenu)
wdtStopWhenDebugging.setLabel("Stop When Debugging")
wdtStopWhenDebugging.setDefaultValue(True)
###
wdtInterruptEnable = wdtInstanceName.getValue() + "_INTERRUPT_ENABLE"
wdtInterruptHandler = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER"
wdtInterruptHandlerLock = wdtInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"


####################################### Code Generation  ##########################################
configName = Variables.get("__CONFIGURATION_NAME")

wdtHeaderFile = coreComponent.createFileSymbol("WDT_HEADER_FILE", None)
wdtHeaderFile.setSourcePath("../peripheral/wdt_44154/templates/plib_wdt.h.ftl")
wdtHeaderFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".h")
wdtHeaderFile.setDestPath("/peripheral/wdt/")
wdtHeaderFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtHeaderFile.setType("HEADER")
wdtHeaderFile.setMarkup(True)
wdtHeaderFile.setEnabled(False)

wdtSourceFile = coreComponent.createFileSymbol("WDT_SOURCE_FILE", None)
wdtSourceFile.setSourcePath("../peripheral/wdt_44154/templates/plib_wdt.c.ftl")
wdtSourceFile.setOutputName("plib_" + wdtInstanceName.getValue().lower() + ".c")
wdtSourceFile.setDestPath("/peripheral/wdt/")
wdtSourceFile.setProjectPath("config/" + configName + "/peripheral/wdt/")
wdtSourceFile.setType("SOURCE")
wdtSourceFile.setMarkup(True)
wdtSourceFile.setEnabled(False)

wdtSystemInitFile = coreComponent.createFileSymbol("WDT_SYSTEM_INIT_FILE", None)
wdtSystemInitFile.setType("STRING")
wdtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
wdtSystemInitFile.setSourcePath("../peripheral/wdt_44154/templates/system/initialization.c.ftl")
wdtSystemInitFile.setMarkup(True)
wdtSystemInitFile.setEnabled(False)

wdtSystemDefFile = coreComponent.createFileSymbol("WDT_SYSTEM_DEF_FILE", None)
wdtSystemDefFile.setType("STRING")
wdtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
wdtSystemDefFile.setSourcePath("../peripheral/wdt_44154/templates/system/definitions.h.ftl")
wdtSystemDefFile.setMarkup(True)
wdtSystemDefFile.setEnabled(False)
