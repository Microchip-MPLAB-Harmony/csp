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

################################################################################
#### Business Logic ####
################################################################################
#-----------------------------------------------------------------------------------------------------------------------
def interruptControl(symbol, event):
    symObj=event["symbol"]

    Database.clearSymbolValue("core", interruptEnable)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (symObj.getSelectedKey() == "INTERRUPT"):
        Database.setSymbolValue("core", interruptEnable, True, 2)
        Database.setSymbolValue("core", interruptHandler, "RSTC" + instanceStr +  "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptEnable, False, 2)
        Database.setSymbolValue("core", interruptHandler, "RSTC_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(rstcComponent):

    global interruptEnable
    global interruptHandler
    global interruptHandlerLock
    global instanceStr

    instanceStr = rstcComponent.getID()
    instanceStr = instanceStr.upper().replace( "RSTC", "" )[-1:]

    rstcInstanceStr = rstcComponent.createStringSymbol("INSTANCE", None)
    rstcInstanceStr.setDefaultValue( instanceStr)
    rstcInstanceStr.setVisible(False)

    rstcSym_MR_UserReset = rstcComponent.createKeyValueSetSymbol("RSTC_MR_URSTEN", None)
    rstcSym_MR_UserReset.setLabel("External Reset (NRST) Pin Usage")
    rstcSym_MR_UserReset.addKey("RESET", "0", "Generate Reset")
    rstcSym_MR_UserReset.addKey("INTERRUPT", "1", "Generate Interrupt")
    rstcSym_MR_UserReset.addKey("IGNORE", "2", "Ignore Input")
    rstcSym_MR_UserReset.setOutputMode("Key")
    rstcSym_MR_UserReset.setDisplayMode("Description")
    rstcSym_MR_UserReset.setSelectedKey("RESET",1)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptEnable = "RSTC_INTERRUPT_ENABLE"
    interruptHandler = "RSTC_INTERRUPT_HANDLER"
    interruptHandlerLock = "RSTC_INTERRUPT_HANDLER_LOCK"
    interruptEnableUpdate = "RSTC_INTERRUPT_ENABLE_UPDATE"

    # Interrupt Dynamic settings
    rstcInterruptControl = rstcComponent.createBooleanSymbol("RSTC_INT_ENABLE", None)
    rstcInterruptControl.setDependencies(interruptControl, ["RSTC_MR_URSTEN"])
    rstcInterruptControl.setVisible(False)

	############################################################################
	#### Code Generation ####
	############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rstcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RSTC\"]")
    rstcModuleID = rstcModuleNode.getAttribute("id")

    rstcCommonHeaderFile = rstcComponent.createFileSymbol("RSTC_COMMON_HEADER", None)
    rstcCommonHeaderFile.setSourcePath("../peripheral/rstc_" + rstcModuleID + "/templates/plib_rstc_common.h")
    rstcCommonHeaderFile.setOutputName("plib_rstc_common.h")
    rstcCommonHeaderFile.setDestPath("peripheral/rstc/")
    rstcCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcCommonHeaderFile.setType("HEADER")
    rstcCommonHeaderFile.setOverwrite(True)

    rstcInstanceHeaderFile = rstcComponent.createFileSymbol("RSTC_INSTANCE_HEADER", None)
    rstcInstanceHeaderFile.setSourcePath("../peripheral/rstc_" + rstcModuleID + "/templates/plib_rstc.h.ftl")
    rstcInstanceHeaderFile.setOutputName("plib_rstc" + instanceStr + ".h")
    rstcInstanceHeaderFile.setDestPath("peripheral/rstc/")
    rstcInstanceHeaderFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcInstanceHeaderFile.setType("HEADER")
    rstcInstanceHeaderFile.setOverwrite(True)
    rstcInstanceHeaderFile.setMarkup(True)

    rstcSourceFile = rstcComponent.createFileSymbol("RSTC_SOURCE", None)
    rstcSourceFile.setSourcePath("../peripheral/rstc_" + rstcModuleID + "/templates/plib_rstc.c.ftl")
    rstcSourceFile.setOutputName("plib_rstc" + instanceStr + ".c")
    rstcSourceFile.setDestPath("peripheral/rstc/")
    rstcSourceFile.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSourceFile.setType("SOURCE")
    rstcSourceFile.setOverwrite(True)
    rstcSourceFile.setMarkup(True)

    rstcSystemInitFile = rstcComponent.createFileSymbol("RSTC_INIT", None)
    rstcSystemInitFile.setType("STRING")
    rstcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rstcSystemInitFile.setSourcePath("../peripheral/rstc_" + rstcModuleID + "/templates/system/initialization.c.ftl")
    rstcSystemInitFile.setMarkup(True)

    rstcSystemDefFile = rstcComponent.createFileSymbol("RSTC_DEF", None)
    rstcSystemDefFile.setType("STRING")
    rstcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSystemDefFile.setSourcePath("../peripheral/rstc_" + rstcModuleID + "/templates/system/definitions.h.ftl")
    rstcSystemDefFile.setMarkup(True)

