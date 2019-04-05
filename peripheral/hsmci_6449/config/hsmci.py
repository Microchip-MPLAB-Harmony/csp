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
global hsmciInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

################################################################################
#### Business Logic ####
################################################################################
def setVisible(symbol, event):
    symbol.setVisible(event["value"])

def setValue(symbol, event):
    symbol.setValue(int(event["value"]), 2)

def destroyComponent(sdhcComponent):
    Database.setSymbolValue("core","DMA_CH_NEEDED_FOR_HSMCI", False, 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(hsmciComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global hsmciInstanceName

    hsmciInstanceName = hsmciComponent.createStringSymbol("HSMCI_INSTANCE_NAME", None)
    hsmciInstanceName.setVisible(False)
    hsmciInstanceName.setDefaultValue(hsmciComponent.getID().upper())
    Log.writeInfoMessage("Running " + hsmciInstanceName.getValue())

    xdmacInstanceName = hsmciComponent.createStringSymbol("XDMAC_INSTANCE_NAME", None)
    xdmacInstanceName.setVisible(False)
    xdmacInstanceName.setDefaultValue(Database.getSymbolValue("core", "DMA_INSTANCE_NAME"))

    # DMA_CHANNEL for HSMCI
    # Enable DMA for HSMCI
    Database.setSymbolValue("core","DMA_CH_NEEDED_FOR_HSMCI", True, 2)

    sdhcDMA = hsmciComponent.createIntegerSymbol("HSMCI_DMA", None)
    sdhcDMA.setLabel("DMA Channel For Transmit and Receive")
    sdhcDMA.setReadOnly(True)
    sdhcDMA.setDefaultValue(int(Database.getSymbolValue("core", "DMA_CH_FOR_HSMCI")))

    sdhcDMAChannelComment = hsmciComponent.createCommentSymbol("DRV_SDHC_DMA_CH_COMMENT", None)
    sdhcDMAChannelComment.setLabel("Warning!!! Couldn't Allocate DMA Channel. Check DMA Manager.")

    if(int(Database.getSymbolValue("core", "DMA_CH_FOR_HSMCI")) == -2):
        sdhcDMAChannelComment.setVisible(True)
    else:
        sdhcDMAChannelComment.setVisible(False)

    sdhcCLK = hsmciComponent.createIntegerSymbol("HSMCI_CLK", None)
    sdhcCLK.setVisible(False)
    sdhcCLK.setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
    sdhcCLK.setDependencies(setValue, ["core.MASTER_CLOCK_FREQUENCY"])

    hsmciCDSupport = hsmciComponent.createBooleanSymbol("SDCARD_SDCD_SUPPORT", None)
    hsmciCDSupport.setLabel("HSMCI SDCD Support")
    hsmciCDSupport.setDefaultValue(False)
    hsmciCDSupport.setVisible(False)

    hsmciWPSupport = hsmciComponent.createBooleanSymbol("SDCARD_SDWP_SUPPORT", None)
    hsmciWPSupport.setLabel("HSMCI SDWP Support")
    hsmciWPSupport.setDefaultValue(False)
    hsmciWPSupport.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = hsmciInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = hsmciInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = hsmciInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = hsmciInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", hsmciInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", hsmciInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, hsmciInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings


    # Dependency Status


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    hsmciCommonHeaderFile = hsmciComponent.createFileSymbol("HSMCI_COMMON_HEADER", None)
    hsmciCommonHeaderFile.setSourcePath("../peripheral/hsmci_6449/templates/plib_hsmci_common.h")
    hsmciCommonHeaderFile.setOutputName("plib_hsmci_common.h")
    hsmciCommonHeaderFile.setDestPath("peripheral/hsmci/")
    hsmciCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/hsmci/")
    hsmciCommonHeaderFile.setType("HEADER")
    hsmciCommonHeaderFile.setOverwrite(True)

    hsmciHeaderFile = hsmciComponent.createFileSymbol("HSMCI_HEADER", None)
    hsmciHeaderFile.setSourcePath("../peripheral/hsmci_6449/templates/plib_hsmci.h.ftl")
    hsmciHeaderFile.setOutputName("plib_"+hsmciInstanceName.getValue().lower()+".h")
    hsmciHeaderFile.setDestPath("peripheral/hsmci/")
    hsmciHeaderFile.setProjectPath("config/" + configName + "/peripheral/hsmci/")
    hsmciHeaderFile.setType("HEADER")
    hsmciHeaderFile.setOverwrite(True)
    hsmciHeaderFile.setMarkup(True)

    hsmciSourceFile = hsmciComponent.createFileSymbol("HSMCI_SOURCE", None)
    hsmciSourceFile.setSourcePath("../peripheral/hsmci_6449/templates/plib_hsmci.c.ftl")
    hsmciSourceFile.setOutputName("plib_"+hsmciInstanceName.getValue().lower()+".c")
    hsmciSourceFile.setDestPath("peripheral/hsmci/")
    hsmciSourceFile.setProjectPath("config/" + configName + "/peripheral/hsmci/")
    hsmciSourceFile.setType("SOURCE")
    hsmciSourceFile.setOverwrite(True)
    hsmciSourceFile.setMarkup(True)

    hsmciSystemInitFile = hsmciComponent.createFileSymbol("HSMCI_INIT", None)
    hsmciSystemInitFile.setType("STRING")
    hsmciSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    hsmciSystemInitFile.setSourcePath("../peripheral/hsmci_6449/templates/system/initialization.c.ftl")
    hsmciSystemInitFile.setMarkup(True)

    hsmciSystemDefFile = hsmciComponent.createFileSymbol("HSMCI_DEF", None)
    hsmciSystemDefFile.setType("STRING")
    hsmciSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    hsmciSystemDefFile.setSourcePath("../peripheral/hsmci_6449/templates/system/definitions.h.ftl")
    hsmciSystemDefFile.setMarkup(True)
