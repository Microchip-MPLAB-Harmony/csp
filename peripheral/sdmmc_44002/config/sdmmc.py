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
#### Business Logic ####
################################################################################
def updateSDCDENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDWPENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDMMCClkFreq(symbol, event):
    symbol.setValue(int(event["value"]), 2)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def interruptStatusWarning(symbol, event):
    if Database.getSymbolValue(sdmmcInstanceName.getValue().lower(), "INTERRUPT_MODE") == True:
        symbol.setVisible(event["value"])

# Dependency Function to show or hide the warning message depending on Clock enable/disable status
def clockStatusWarning(symbol, event):
    if event["value"] == False:
       symbol.setVisible(True)
    else:
       symbol.setVisible(False)

################################################################################
#### Component ####
################################################################################
def destroyComponent(sdmmcComponent):
    Database.clearSymbolValue(coreNamespace, interruptEnable)
    Database.clearSymbolValue(coreNamespace, interruptHandler)
    Database.clearSymbolValue(coreNamespace, interruptHandlerLock)

def instantiateComponent(sdmmcComponent):
    global coreNamespace
    global interruptEnable
    global interruptHandler
    global interruptHandlerLock
    global sdmmcInstanceName

    sdmmcInstanceName = sdmmcComponent.createStringSymbol("SDMMC_INSTANCE_NAME", None)
    sdmmcInstanceName.setVisible(False)
    sdmmcInstanceName.setDefaultValue(sdmmcComponent.getID().upper())
    Log.writeInfoMessage("Running " + sdmmcInstanceName.getValue())

    coreNamespace = "core"
    interruptEnable = sdmmcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = sdmmcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = sdmmcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptEnableUpdate = sdmmcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK
    Database.setSymbolValue(coreNamespace, sdmmcInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    # Initial settings for Interrupt
    Database.setSymbolValue(coreNamespace, interruptEnable, True, 2)
    Database.setSymbolValue(coreNamespace, interruptHandler, sdmmcInstanceName.getValue() + "_InterruptHandler", 2)
    Database.setSymbolValue(coreNamespace, interruptHandlerLock, True, 2)
    sdmmcInterrupt = sdmmcComponent.createBooleanSymbol("INTERRUPT_MODE", None)
    sdmmcInterrupt.setLabel("Interrupt Mode")
    sdmmcInterrupt.setDefaultValue(True)
    sdmmcInterrupt.setReadOnly(True)

    sdmmcCD = sdmmcComponent.createBooleanSymbol("SDMMC_SDCDEN", None)
    sdmmcCD.setLabel("Use SD Card Detect (SDCD#) Pin")
    sdmmcCD.setDefaultValue(True)

    sdmmcCDComment = sdmmcComponent.createCommentSymbol("SDMMC_SDCDEN_COMMENT", sdmmcCD)
    sdmmcCDComment.setLabel("!!!Configure SDCD pin in Pin Configuration!!!")
    sdmmcCDComment.setVisible(sdmmcCD.getValue())
    sdmmcCDComment.setDependencies(updateSDCDENCommentVisibility, ["SDMMC_SDCDEN"])

    sdmmcWP = sdmmcComponent.createBooleanSymbol("SDMMC_SDWPEN", None)
    sdmmcWP.setLabel("Use SD Write Protect (SDWP#) Pin")
    sdmmcWP.setDefaultValue(True)

    sdmmcWPComment = sdmmcComponent.createCommentSymbol("SDMMC_SDWPEN_COMMENT", sdmmcWP)
    sdmmcWPComment.setLabel("!!!Configure SDWP pin in Pin Configuration!!!")
    sdmmcWPComment.setVisible(sdmmcWP.getValue())
    sdmmcWPComment.setDependencies(updateSDWPENCommentVisibility, ["SDMMC_SDWPEN"])

    sdmmcDescLines = sdmmcComponent.createIntegerSymbol("SDMMC_NUM_DESCRIPTOR_LINES", None)
    sdmmcDescLines.setLabel("Number of ADMA2 Descriptor Lines")
    sdmmcDescLines.setMin(1)
    sdmmcDescLines.setMax(10)
    sdmmcDescLines.setDefaultValue(1)

    sdmmcCLK = sdmmcComponent.createIntegerSymbol("SDMMC_CLK_FREQ", None)
    sdmmcCLK.setVisible(False)
    sdmmcCLK.setDefaultValue(int(Database.getSymbolValue("core", sdmmcInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    sdmmcCLK.setDependencies(updateSDMMCClkFreq, ["core." + sdmmcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    sdmmcClockSourceComment = sdmmcComponent.createCommentSymbol("SDMMC_CLOCK_SOURCE_COMMENT", None)
    sdmmcClockSourceComment.setLabel("!!!Configure " + sdmmcInstanceName.getValue() + " Clock in Clock Configuration!!!")

    # Dependency Status for interrupt
    sdmmcSymIntEnComment = sdmmcComponent.createCommentSymbol(sdmmcInstanceName.getValue() + "_INTERRUPT_ENABLE_COMMENT", None)
    sdmmcSymIntEnComment.setVisible(False)
    sdmmcSymIntEnComment.setLabel("Warning!!! " + sdmmcInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    sdmmcSymIntEnComment.setDependencies(interruptStatusWarning, ["core." + interruptEnableUpdate])

    # Dependency Status for clock
    sdmmcSymClkEnComment = sdmmcComponent.createCommentSymbol(sdmmcInstanceName.getValue() + "_CLK_ENABLE_COMMENT", None)
    sdmmcSymClkEnComment.setVisible(False)
    sdmmcSymClkEnComment.setLabel("Warning!!! " + sdmmcInstanceName.getValue() + " Clock is Disabled in Clock Manager")
    sdmmcSymClkEnComment.setDependencies(clockStatusWarning, ["core."+ sdmmcInstanceName.getValue() + "_CLOCK_ENABLE"])

    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sdmmcHeaderFile = sdmmcComponent.createFileSymbol("SDMMC_HEADER", None)
    sdmmcHeaderFile.setSourcePath("../peripheral/sdmmc_44002/templates/plib_sdmmc_common.h")
    sdmmcHeaderFile.setOutputName("plib_sdmmc_common.h")
    sdmmcHeaderFile.setDestPath("peripheral/sdmmc/")
    sdmmcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcHeaderFile.setType("HEADER")
    sdmmcHeaderFile.setOverwrite(True)

    sdmmcHeader1File = sdmmcComponent.createFileSymbol("SDMMC_HEADER1", None)
    sdmmcHeader1File.setSourcePath("../peripheral/sdmmc_44002/templates/plib_sdmmc.h.ftl")
    sdmmcHeader1File.setOutputName("plib_"+sdmmcInstanceName.getValue().lower()+".h")
    sdmmcHeader1File.setDestPath("peripheral/sdmmc/")
    sdmmcHeader1File.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcHeader1File.setType("HEADER")
    sdmmcHeader1File.setOverwrite(True)
    sdmmcHeader1File.setMarkup(True)

    sdmmcSource1File = sdmmcComponent.createFileSymbol("SDMMC_SOURCE1", None)
    sdmmcSource1File.setSourcePath("../peripheral/sdmmc_44002/templates/plib_sdmmc.c.ftl")
    sdmmcSource1File.setOutputName("plib_"+sdmmcInstanceName.getValue().lower()+".c")
    sdmmcSource1File.setDestPath("peripheral/sdmmc/")
    sdmmcSource1File.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcSource1File.setType("SOURCE")
    sdmmcSource1File.setOverwrite(True)
    sdmmcSource1File.setMarkup(True)

    sdmmcSystemInitFile = sdmmcComponent.createFileSymbol("SDMMC_INIT", None)
    sdmmcSystemInitFile.setType("STRING")
    sdmmcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sdmmcSystemInitFile.setSourcePath("../peripheral/sdmmc_44002/templates/system/system_initialize.c.ftl")
    sdmmcSystemInitFile.setMarkup(True)

    sdmmcSystemDefFile = sdmmcComponent.createFileSymbol("SDMMC_DEF", None)
    sdmmcSystemDefFile.setType("STRING")
    sdmmcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sdmmcSystemDefFile.setSourcePath("../peripheral/sdmmc_44002/templates/system/system_definitions.h.ftl")
    sdmmcSystemDefFile.setMarkup(True)
