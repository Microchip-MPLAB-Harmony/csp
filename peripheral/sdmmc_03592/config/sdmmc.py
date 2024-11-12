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
global sdmmcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock
global InterruptVectorSecurity
global sdmmcfilesArray
sdmmcfilesArray = []
################################################################################
#### Business Logic ####
################################################################################
def updateSDCDENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDWPENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDMMCClkFreq(symbol, event):
    symbol.setValue(int(event["value"]), 2)


def fileUpdate(symbol, event):
    global sdmmcfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        sdmmcfilesArray[0].setSecurity("SECURE")
        sdmmcfilesArray[1].setSecurity("SECURE")
        sdmmcfilesArray[2].setSecurity("SECURE")
        sdmmcfilesArray[3].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        sdmmcfilesArray[4].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        sdmmcfilesArray[0].setSecurity("NON_SECURE")
        sdmmcfilesArray[1].setSecurity("NON_SECURE")
        sdmmcfilesArray[2].setSecurity("NON_SECURE")
        sdmmcfilesArray[3].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        sdmmcfilesArray[4].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, True)    

################################################################################
#### Component ####
################################################################################
def instantiateComponent(sdmmcComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global sdmmcInstanceName
    global InterruptVectorSecurity

    sdmmcInstanceName = sdmmcComponent.createStringSymbol("SDMMC_INSTANCE_NAME", None)
    sdmmcInstanceName.setVisible(False)
    sdmmcInstanceName.setDefaultValue(sdmmcComponent.getID().upper())
    Log.writeInfoMessage("Running " + sdmmcInstanceName.getValue())

    sdmmcCDSupport = sdmmcComponent.createBooleanSymbol("SDCARD_SDCD_SUPPORT", None)
    sdmmcCDSupport.setLabel("SDMMC SDCD Support")
    sdmmcCDSupport.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmcCDSupport.setDefaultValue(True)
    sdmmcCDSupport.setVisible(False)

    sdmmcWPSupport = sdmmcComponent.createBooleanSymbol("SDCARD_SDWP_SUPPORT", None)
    sdmmcWPSupport.setLabel("SDMMC SDWP Support")
    sdmmcWPSupport.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmcWPSupport.setDefaultValue(True)
    sdmmcWPSupport.setVisible(False)

    sdmmc8BitSupport = sdmmcComponent.createBooleanSymbol("SDCARD_8BIT_SUPPORT", None)
    sdmmc8BitSupport.setLabel("SDMMC 8 Bit Support")
    sdmmc8BitSupport.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmc8BitSupport.setDefaultValue(False)
    sdmmc8BitSupport.setVisible(False)

    sdmmcEMMCSupport = sdmmcComponent.createBooleanSymbol("SDCARD_EMMC_SUPPORT", None)
    sdmmcEMMCSupport.setLabel("SDMMC EMMC Support")
    sdmmcEMMCSupport.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmcEMMCSupport.setDefaultValue(True)
    sdmmcEMMCSupport.setVisible(False)

    sdmmcCD = sdmmcComponent.createBooleanSymbol("SDCARD_SDCDEN", None)
    sdmmcCD.setLabel("Use SD Card Detect (SDCD#) Pin")
    sdmmcCD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmcCD.setDefaultValue(False)
    sdmmcCD.setVisible(False)

    sdmmcWP = sdmmcComponent.createBooleanSymbol("SDCARD_SDWPEN", None)
    sdmmcWP.setLabel("Use SD Write Protect (SDWP#) Pin")
    sdmmcWP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:%NOREGISTER%")
    sdmmcWP.setDefaultValue(False)
    sdmmcWP.setVisible(False)

    sdmmcUseEMMC = sdmmcComponent.createBooleanSymbol("SDCARD_EMMCEN", None)
    sdmmcUseEMMC.setReadOnly(True)
    sdmmcUseEMMC.setVisible(False)
    sdmmcUseEMMC.setDefaultValue(False)

    sdmmcDescLines = sdmmcComponent.createIntegerSymbol("SDMMC_NUM_DESCRIPTOR_LINES", None)
    sdmmcDescLines.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:sdmmc_03592;register:CA0R")
    sdmmcDescLines.setLabel("Number of ADMA2 Descriptor Lines")
    sdmmcDescLines.setMin(1)
    sdmmcDescLines.setMax(10)
    sdmmcDescLines.setDefaultValue(1)

    sdmmcSlowClockComment = sdmmcComponent.createCommentSymbol("SDMMC_SLOW_CLK_COMMENT", None)
    sdmmcSlowClockComment.setLabel("!!!Configure SDMMC Slow Clock in Clock Configuration!!!")

    sdmmcCLK = sdmmcComponent.createIntegerSymbol("SDMMC_CLK_FREQ", None)
    sdmmcCLK.setVisible(False)
    sdmmcCLK.setDefaultValue(int(Database.getSymbolValue("core", sdmmcInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    sdmmcCLK.setDependencies(updateSDMMCClkFreq, ["core." + sdmmcInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptVector = sdmmcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = sdmmcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = sdmmcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = sdmmcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    InterruptVectorSecurity = sdmmcInstanceName.getValue() + "_SET_NON_SECURE"    

    # Initial settings for CLK and NVIC
    Database.setSymbolValue("core", sdmmcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.setSymbolValue("core", interruptHandler, sdmmcInstanceName.getValue() + "_InterruptHandler", 2)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # NVIC Dynamic settings


    # Dependency Status


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sdmmcHeaderFile = sdmmcComponent.createFileSymbol("SDMMC_HEADER", None)
    sdmmcHeaderFile.setSourcePath("../peripheral/sdmmc_03592/templates/plib_sdmmc_common.h.ftl")
    sdmmcHeaderFile.setOutputName("plib_sdmmc_common.h")
    sdmmcHeaderFile.setDestPath("peripheral/sdmmc/")
    sdmmcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcHeaderFile.setType("HEADER")
    sdmmcHeaderFile.setOverwrite(True)
    sdmmcHeaderFile.setMarkup(True)

    sdmmcHeader1File = sdmmcComponent.createFileSymbol("SDMMC_HEADER1", None)
    sdmmcHeader1File.setSourcePath("../peripheral/sdmmc_03592/templates/plib_sdmmc.h.ftl")
    sdmmcHeader1File.setOutputName("plib_"+sdmmcInstanceName.getValue().lower()+".h")
    sdmmcHeader1File.setDestPath("peripheral/sdmmc/")
    sdmmcHeader1File.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcHeader1File.setType("HEADER")
    sdmmcHeader1File.setOverwrite(True)
    sdmmcHeader1File.setMarkup(True)

    sdmmcSource1File = sdmmcComponent.createFileSymbol("SDMMC_SOURCE1", None)
    sdmmcSource1File.setSourcePath("../peripheral/sdmmc_03592/templates/plib_sdmmc.c.ftl")
    sdmmcSource1File.setOutputName("plib_"+sdmmcInstanceName.getValue().lower()+".c")
    sdmmcSource1File.setDestPath("peripheral/sdmmc/")
    sdmmcSource1File.setProjectPath("config/" + configName + "/peripheral/sdmmc/")
    sdmmcSource1File.setType("SOURCE")
    sdmmcSource1File.setOverwrite(True)
    sdmmcSource1File.setMarkup(True)

    sdmmcSystemInitFile = sdmmcComponent.createFileSymbol("SDMMC_INIT", None)
    sdmmcSystemInitFile.setType("STRING")
    sdmmcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sdmmcSystemInitFile.setSourcePath("../peripheral/sdmmc_03592/templates/system/initialization.c.ftl")
    sdmmcSystemInitFile.setMarkup(True)

    sdmmcSystemDefFile = sdmmcComponent.createFileSymbol("SDMMC_DEF", None)
    sdmmcSystemDefFile.setType("STRING")
    sdmmcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sdmmcSystemDefFile.setSourcePath("../peripheral/sdmmc_03592/templates/system/definitions.h.ftl")
    sdmmcSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global sdmmcfilesArray
        sdmmcIsNonSecure = Database.getSymbolValue("core", sdmmcComponent.getID().upper() + "_IS_NON_SECURE")
        Database.setSymbolValue("core", InterruptVectorSecurity, sdmmcIsNonSecure) 
        sdmmcfilesArray.append(sdmmcHeaderFile)
        sdmmcfilesArray.append(sdmmcHeader1File)
        sdmmcfilesArray.append(sdmmcSource1File)
        sdmmcfilesArray.append(sdmmcSystemInitFile)
        sdmmcfilesArray.append(sdmmcSystemDefFile)

        if sdmmcIsNonSecure == False:
            sdmmcHeaderFile.setSecurity("SECURE")
            sdmmcHeader1File.setSecurity("SECURE")
            sdmmcSource1File.setSecurity("SECURE")
            sdmmcSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            sdmmcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

        sdmmcSystemDefFile.setDependencies(fileUpdate, ["core." + sdmmcComponent.getID().upper() + "_IS_NON_SECURE"])


