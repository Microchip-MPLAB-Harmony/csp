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

#Function for initiating the UI
global interruptVector
global interruptHandler
global trngInstanceName
global interruptHandlerLock
global TRNGfilesArray
global InterruptVectorSecurity
TRNGfilesArray = []

def fileUpdate(symbol, event):
    global TRNGfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        TRNGfilesArray[0].setSecurity("SECURE")
        TRNGfilesArray[1].setSecurity("SECURE")
        TRNGfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TRNGfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        TRNGfilesArray[0].setSecurity("NON_SECURE")
        TRNGfilesArray[1].setSecurity("NON_SECURE")
        TRNGfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TRNGfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, True)

def interruptControl(NVIC, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, trngInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "TRNG_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def trngEVSYS(symbol, event):
    Database.setSymbolValue("evsys0","GENERATOR_TRNG_READY_ACTIVE", event["value"], 2)

def instantiateComponent(trngComponent):
    global interruptVector
    global interruptHandler
    global trngInstanceName
    global interruptHandlerLock
    global InterruptVectorSecurity

    trngInstanceName = trngComponent.createStringSymbol("TRNG_INSTANCE_NAME", None)
    trngInstanceName.setVisible(False)
    trngInstanceName.setDefaultValue(trngComponent.getID().upper())
    Log.writeInfoMessage("Running " + trngInstanceName.getValue())

    interruptVector = trngInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = trngInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = trngInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = trngInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"
    InterruptVectorSecurity = trngInstanceName.getValue() + "_SET_NON_SECURE"

    trngReserved = trngComponent.createBooleanSymbol("TRNG_Reserved", None)
    trngReserved.setLabel("TRNG Reserved")
    trngReserved.setVisible(False)

    trngWarning = trngComponent.createCommentSymbol("TRNG_COMMENT", None)
    trngWarning.setLabel("**** Warning: This module is used and configured by Crypto Library ****")
    trngWarning.setDependencies(showWarning, ["TRNG_Reserved"])
    trngWarning.setVisible(False)

    #Create the top menu
    trngMenu = trngComponent.createMenuSymbol("TRNG_MENU_0", None)
    trngMenu.setLabel("Hardware Settings ")
    trngMenu.setDependencies(showMenu, ["TRNG_Reserved"])

    #Create a Checkbox to enable disable interrupts
    trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
    trngInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:trng_u2242;register:INTENSET")
    trngInterrupt.setLabel("Enable Interrupts")
    trngInterrupt.setDefaultValue(False)

        #Create a Checkbox to enable disable interrupts
    trngInterrupt = trngComponent.createBooleanSymbol("trngEnableEvent", trngMenu)
    trngInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:trng_u2242;register:EVCTRL")
    trngInterrupt.setLabel("Enable Data Ready Event Output")
    trngInterrupt.setDefaultValue(False)

    trngEvent = trngComponent.createBooleanSymbol("DUMMY", trngMenu)
    trngEvent.setVisible(False)
    trngEvent.setDependencies(trngEVSYS, ["trngEnableEvent"])

    trngSTDBY = trngComponent.createBooleanSymbol("TRNG_STANDBY", trngMenu)
    trngSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:trng_u2242;register:CTRLA")
    trngSTDBY.setLabel("Run Trng in Standby sleep mode")

    Database.setSymbolValue("core", trngInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    # NVIC Dynamic settings
    trnginterruptControl = trngComponent.createBooleanSymbol("NVIC_TRNG_ENABLE", None)
    trnginterruptControl.setDependencies(interruptControl, ["trngEnableInterrupt"])
    trnginterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    #Generate Output Header
    trngHeaderFile = trngComponent.createFileSymbol("TRNG_FILE_0", None)
    trngHeaderFile.setSourcePath("../peripheral/trng_u2242/templates/plib_trng.h.ftl")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOutputName("plib_"+trngInstanceName.getValue().lower()+".h")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOverwrite(True)
    trngHeaderFile.setDestPath("peripheral/trng/")
    trngHeaderFile.setProjectPath("config/" + configName + "/peripheral/trng/")
    trngHeaderFile.setType("HEADER")
    #Generate Output source

    trngSourceFile = trngComponent.createFileSymbol("TRNG_FILE_1", None)
    trngSourceFile.setSourcePath("../peripheral/trng_u2242/templates/plib_trng.c.ftl")
    trngSourceFile.setMarkup(True)
    trngSourceFile.setOutputName("plib_"+trngInstanceName.getValue().lower()+".c")
    trngSourceFile.setMarkup(True)
    trngSourceFile.setOverwrite(True)
    trngSourceFile.setDestPath("peripheral/trng/")
    trngSourceFile.setProjectPath("config/" + configName + "/peripheral/trng/")
    trngSourceFile.setType("SOURCE")

    trngSystemDefFile = trngComponent.createFileSymbol("TRNG_FILE_2", None)
    trngSystemDefFile.setType("STRING")
    trngSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    trngSystemDefFile.setSourcePath("../peripheral/trng_u2242/templates/system/definitions.h.ftl")
    trngSystemDefFile.setMarkup(True)

    #System Initialization
    trngSystemInitFile = trngComponent.createFileSymbol("TRNG_SYS_INIT", None)
    trngSystemInitFile.setType("STRING")
    trngSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    trngSystemInitFile.setSourcePath("../peripheral/trng_u2242/templates/system/initialization.c.ftl")
    trngSystemInitFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global TRNGfilesArray
        trngIsNonSecure = Database.getSymbolValue("core", trngComponent.getID().upper() + "_IS_NON_SECURE")
        trngSystemDefFile.setDependencies(fileUpdate, ["core." + trngComponent.getID().upper() + "_IS_NON_SECURE"])
        TRNGfilesArray.append(trngHeaderFile)
        TRNGfilesArray.append(trngSourceFile)
        TRNGfilesArray.append(trngSystemInitFile)
        TRNGfilesArray.append(trngSystemDefFile)
        Database.setSymbolValue("core", InterruptVectorSecurity, trngIsNonSecure)
        if trngIsNonSecure == False:
            TRNGfilesArray[0].setSecurity("SECURE")
            TRNGfilesArray[1].setSecurity("SECURE")
            TRNGfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            TRNGfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

def showWarning(trngWarning, event):
    trngWarning.setVisible(event["value"])

def showMenu(trngMenu, event):
    trngMenu.setVisible(not event["value"])
