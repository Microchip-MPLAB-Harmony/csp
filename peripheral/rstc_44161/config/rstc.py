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

################################################################################
#### Global Variables ####
################################################################################
global interruptEnable
global interruptHandler
global interruptHandlerLock
global instanceStr
global clockFrequency

interruptEnable =       "RSTC_INTERRUPT_ENABLE"
interruptHandler =      "RSTC_INTERRUPT_HANDLER"
interruptHandlerLock =  "RSTC_INTERRUPT_HANDLER_LOCK"
interruptEnableUpdate = "RSTC_INTERRUPT_ENABLE_UPDATE"
instanceStr = ""
clockFrequency = 32000                             # If xtal = 32768, if Rc = 32000

def interruptControl(symbol, event):
    global interruptEnable
    global interruptHandler
    global interruptHandlerLock
    global instanceStr

    symObj=event["symbol"]

    Database.clearSymbolValue("core", interruptEnable)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (symObj.getSelectedKey() == "INTERRUPT"):
        Database.setSymbolValue("core", interruptEnable, True, 0)
        Database.setSymbolValue("core", interruptHandler, "RSTC" + instanceStr +  "_InterruptHandler", 0)
        Database.setSymbolValue("core", interruptHandlerLock, True, 0)


def rstcErstlToMilliSecs( erstlRegValue ):
    cycles = 2**( erstlRegValue + 1 )
    milliSeconds = (float(cycles)/clockFrequency)*1e3
    return round( milliSeconds, 3 )	


def rstcMilliSecUpdate( symbol, event ):
    global rstcErstlToMilliSecs
    symbol.setValue( rstcErstlToMilliSecs( event["value"] ), 1 )


def instantiateComponent(rstcComponent):
    global instanceStr

    instanceStr = rstcComponent.getID()
    instanceStr = instanceStr.upper().replace( "RSTC", "" )[-1:]

    rstcInstanceStr = rstcComponent.createStringSymbol("INSTANCE", None)
    rstcInstanceStr.setDefaultValue( instanceStr)
    rstcInstanceStr.setVisible(False)

    rstcMrExternalResetAction = rstcComponent.createKeyValueSetSymbol("RSTC_MR_EXTERNAL_RESET_ACTION", None)
    rstcMrExternalResetAction.setLabel("External reset action")
    rstcMrExternalResetAction.addKey("RESET",     "0", "Generate reset")
    rstcMrExternalResetAction.addKey("INTERRUPT", "1", "Generate interrupt")
    rstcMrExternalResetAction.addKey("IGNORE",    "2", "Ignore input")
    rstcMrExternalResetAction.setOutputMode("Key")
    rstcMrExternalResetAction.setDisplayMode("Description")
    rstcMrExternalResetAction.setSelectedKey("RESET",1)

    rstcMrExternalResetLength = rstcComponent.createIntegerSymbol("RSTC_MR_EXTERNAL_RESET_LENGTH", None)
    rstcMrExternalResetLength.setLabel("External reset length (ERSTL value)")
    rstcMrExternalResetLength.setMin( 0 )
    rstcMrExternalResetLength.setMax( 15 )
    rstcMrExternalResetLength.setDefaultValue( 0 )

    rstcMrExternalResetLengthMilliSecs = rstcComponent.createFloatSymbol("RSTC_EXTERNAL_RESET_LENGTH_MSECS", None)
    rstcMrExternalResetLengthMilliSecs.setLabel("External reset length (mSecs)")
    rstcMrExternalResetLengthMilliSecs.setDependencies( rstcMilliSecUpdate, ["RSTC_MR_EXTERNAL_RESET_LENGTH"] )
    rstcMrExternalResetLengthMilliSecs.setReadOnly(True)
    rstcMrExternalResetLengthMilliSecs.setDefaultValue( rstcErstlToMilliSecs( rstcMrExternalResetLength.getValue() ) )

    rstcMrCpuFaultReset = rstcComponent.createBooleanSymbol( "RSTC_MR_CPU_FAULT_RESET", None )
    rstcMrCpuFaultReset.setLabel("Reset on CPU fault detection")
    rstcMrCpuFaultReset.setDefaultValue(False)

    rstcMrCrystalFaultReset = rstcComponent.createBooleanSymbol( "RSTC_MR_CRYSTAL_FAULT_RESET", None )
    rstcMrCrystalFaultReset.setLabel("Crystal fault resets VDDCORE logic")
    rstcMrCrystalFaultReset.setDefaultValue(False)

    rstcMrAsynchronousReset = rstcComponent.createBooleanSymbol( "RSTC_MR_ASYNCHRONOUS_RESET", None )
    rstcMrAsynchronousReset.setLabel("Reset is asynchronous to slow clock")
    rstcMrAsynchronousReset.setDefaultValue(False)

    rstcMrImmediatGpbrClear = rstcComponent.createBooleanSymbol( "RSTC_MR_IMMEDIATE_GPBR_CLEAR", None )
    rstcMrImmediatGpbrClear.setLabel("Immediate GPBR clear on tamper detection")
    rstcMrImmediatGpbrClear.setDefaultValue(False)
    # Interrupt Dynamic settings
    rstcInterruptControl = rstcComponent.createBooleanSymbol( interruptEnable, None )
    rstcInterruptControl.setDependencies(interruptControl, ["RSTC_MR_EXTERNAL_RESET_ACTION"])
    rstcInterruptControl.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
    rstcModuleId = rstcModuleNode.getAttribute("id")

    rstcCommonHeaderFile = rstcComponent.createFileSymbol("RSTC_COMMON_HEADER", None)
    rstcCommonHeaderFile.setSourcePath("../peripheral/rstc_" + rstcModuleId + "/templates/plib_rstc_common.h")
    rstcCommonHeaderFile.setOutputName("plib_rstc_common.h")
    rstcCommonHeaderFile.setDestPath("peripheral/rstc/")
    rstcCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcCommonHeaderFile.setType("HEADER")
    rstcCommonHeaderFile.setOverwrite(True)

    rstcInstanceHeaderFile = rstcComponent.createFileSymbol("RSTC_INSTANCE_HEADER", None)
    rstcInstanceHeaderFile.setSourcePath("../peripheral/rstc_" + rstcModuleId + "/templates/plib_rstc.h.ftl")
    rstcInstanceHeaderFile.setOutputName("plib_rstc" + instanceStr + ".h")
    rstcInstanceHeaderFile.setDestPath("peripheral/rstc/")
    rstcInstanceHeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcInstanceHeaderFile.setType("HEADER")
    rstcInstanceHeaderFile.setOverwrite(True)
    rstcInstanceHeaderFile.setMarkup(True)

    rstcSourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
    rstcSourceFile.setSourcePath("../peripheral/rstc_" + rstcModuleId + "/templates/plib_rstc.c.ftl")
    rstcSourceFile.setOutputName("plib_rstc" + instanceStr + ".c")
    rstcSourceFile.setDestPath("peripheral/rstc/")
    rstcSourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSourceFile.setType("SOURCE")
    rstcSourceFile.setOverwrite(True)
    rstcSourceFile.setMarkup(True)

    rstcSystemInitFile = rstcComponent.createFileSymbol("RSTC_INIT", None)
    rstcSystemInitFile.setType("STRING")
    rstcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rstcSystemInitFile.setSourcePath("../peripheral/rstc_" + rstcModuleId + "/templates/system/initialization.c.ftl")
    rstcSystemInitFile.setMarkup(True)

    rstcSystemDefFile = rstcComponent.createFileSymbol("RSTC_DEF", None)
    rstcSystemDefFile.setType("STRING")
    rstcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSystemDefFile.setSourcePath("../peripheral/rstc_" + rstcModuleId + "/templates/system/definitions.h.ftl")
    rstcSystemDefFile.setMarkup(True)

