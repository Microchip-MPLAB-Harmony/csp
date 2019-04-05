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
#### Register Information ####
################################################################################


################################################################################
#### Global Variables ####
################################################################################
global sdhcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################
def updateSDCDENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDWPENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDHCClkFreq(symbol, event):
    symbol.setValue(int(event["value"]), 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(sdhcComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global sdhcInstanceName

    sdhcInstanceName = sdhcComponent.createStringSymbol("SDHC_INSTANCE_NAME", None)
    sdhcInstanceName.setVisible(False)
    sdhcInstanceName.setDefaultValue(sdhcComponent.getID().upper())
    Log.writeInfoMessage("Running " + sdhcInstanceName.getValue())

    sdhcCDSupport = sdhcComponent.createBooleanSymbol("SDCARD_SDCD_SUPPORT", None)
    sdhcCDSupport.setLabel("SDHC SDCD Support")
    sdhcCDSupport.setDefaultValue(True)
    sdhcCDSupport.setVisible(False)

    sdhcWPSupport = sdhcComponent.createBooleanSymbol("SDCARD_SDWP_SUPPORT", None)
    sdhcWPSupport.setLabel("SDHC SDWP Support")
    sdhcWPSupport.setDefaultValue(True)
    sdhcWPSupport.setVisible(False)

    sdhcCD = sdhcComponent.createBooleanSymbol("SDCARD_SDCDEN", None)
    sdhcCD.setLabel("Use SD Card Detect (SDCD#) Pin")
    sdhcCD.setDefaultValue(False)
    sdhcCD.setVisible(False)

    sdhcWP = sdhcComponent.createBooleanSymbol("SDCARD_SDWPEN", None)
    sdhcWP.setLabel("Use SD Write Protect (SDWP#) Pin")
    sdhcWP.setDefaultValue(False)
    sdhcWP.setVisible(False)

    sdhcDescLines = sdhcComponent.createIntegerSymbol("SDHC_NUM_DESCRIPTOR_LINES", None)
    sdhcDescLines.setLabel("Number of ADMA2 Descriptor Lines")
    sdhcDescLines.setMin(1)
    sdhcDescLines.setMax(10)
    sdhcDescLines.setDefaultValue(1)

    sdhcSlowClockComment = sdhcComponent.createCommentSymbol("SDHC_SLOW_CLK_COMMENT", None)
    sdhcSlowClockComment.setLabel("!!!Configure SDHC Slow Clock in Clock Configuration!!!")

    sdhcCLK = sdhcComponent.createIntegerSymbol("SDHC_CLK_FREQ", None)
    sdhcCLK.setVisible(False)
    sdhcCLK.setDefaultValue(int(Database.getSymbolValue("core", sdhcInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    sdhcCLK.setDependencies(updateSDHCClkFreq, ["core." + sdhcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = sdhcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = sdhcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = sdhcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = sdhcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.setSymbolValue("core", sdhcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.setSymbolValue("core", interruptHandler, sdhcInstanceName.getValue() + "_InterruptHandler", 2)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings


    # Dependency Status


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sdhcHeaderFile = sdhcComponent.createFileSymbol("SDHC_HEADER", None)
    sdhcHeaderFile.setSourcePath("../peripheral/sdhc_u2011/templates/plib_sdhc_common.h")
    sdhcHeaderFile.setOutputName("plib_sdhc_common.h")
    sdhcHeaderFile.setDestPath("peripheral/sdhc/")
    sdhcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcHeaderFile.setType("HEADER")
    sdhcHeaderFile.setOverwrite(True)

    sdhcHeader1File = sdhcComponent.createFileSymbol("SDHC_HEADER1", None)
    sdhcHeader1File.setSourcePath("../peripheral/sdhc_u2011/templates/plib_sdhc.h.ftl")
    sdhcHeader1File.setOutputName("plib_"+sdhcInstanceName.getValue().lower()+".h")
    sdhcHeader1File.setDestPath("peripheral/sdhc/")
    sdhcHeader1File.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcHeader1File.setType("HEADER")
    sdhcHeader1File.setOverwrite(True)
    sdhcHeader1File.setMarkup(True)

    sdhcSource1File = sdhcComponent.createFileSymbol("SDHC_SOURCE1", None)
    sdhcSource1File.setSourcePath("../peripheral/sdhc_u2011/templates/plib_sdhc.c.ftl")
    sdhcSource1File.setOutputName("plib_"+sdhcInstanceName.getValue().lower()+".c")
    sdhcSource1File.setDestPath("peripheral/sdhc/")
    sdhcSource1File.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcSource1File.setType("SOURCE")
    sdhcSource1File.setOverwrite(True)
    sdhcSource1File.setMarkup(True)

    sdhcSystemInitFile = sdhcComponent.createFileSymbol("SDHC_INIT", None)
    sdhcSystemInitFile.setType("STRING")
    sdhcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sdhcSystemInitFile.setSourcePath("../peripheral/sdhc_u2011/templates/system/initialization.c.ftl")
    sdhcSystemInitFile.setMarkup(True)

    sdhcSystemDefFile = sdhcComponent.createFileSymbol("SDHC_DEF", None)
    sdhcSystemDefFile.setType("STRING")
    sdhcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sdhcSystemDefFile.setSourcePath("../peripheral/sdhc_u2011/templates/system/definitions.h.ftl")
    sdhcSystemDefFile.setMarkup(True)
