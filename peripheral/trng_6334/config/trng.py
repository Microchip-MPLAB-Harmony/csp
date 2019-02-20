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

def interruptControl(NVIC, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, trngInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "TRNG_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def instantiateComponent(trngComponent):
    global interruptVector
    global interruptHandler
    global trngInstanceName
    global interruptHandlerLock


    trngInstanceName = trngComponent.createStringSymbol("TRNG_INSTANCE_NAME", None)
    trngInstanceName.setVisible(False)
    trngInstanceName.setDefaultValue(trngComponent.getID().upper())
    Log.writeInfoMessage("Running " + trngInstanceName.getValue())

    #The KEY name is KEY on some masks and WAKEY on others.  Parse the ATDF file to grab the correct name to use the in plib code
    CRKeyName = trngComponent.createStringSymbol("CRKEYNAME", None)
    CRKeyName.setVisible(False)
    CRNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TRNG"]/register-group@[name="TRNG"]/register@[name="TRNG_CR"]')
    for bitfield in CRNode.getChildren():
        if "KEY" in bitfield.getAttribute("name"):
            valuesName = bitfield.getAttribute("values")
            valuesNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TRNG"]/value-group@[name="'+valuesName+'"]')
            value = valuesNode.getChildren()[0]
            CRKeyName.setDefaultValue(bitfield.getAttribute("name")+"_"+value.getAttribute("name"))

    interruptVector = trngInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = trngInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = trngInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = trngInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"


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
    trngInterrupt.setLabel("Enable Interrupts")
    trngInterrupt.setDefaultValue(False)

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", trngInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", trngInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    # NVIC Dynamic settings
    trnginterruptControl = trngComponent.createBooleanSymbol("NVIC_TRNG_ENABLE", None)
    trnginterruptControl.setDependencies(interruptControl, ["trngEnableInterrupt"])
    trnginterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    #Generate Output Header
    trngHeaderFile = trngComponent.createFileSymbol("TRNG_FILE_0", None)
    trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOutputName("plib_"+trngInstanceName.getValue().lower()+".h")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOverwrite(True)
    trngHeaderFile.setDestPath("peripheral/trng/")
    trngHeaderFile.setProjectPath("config/" + configName + "/peripheral/trng/")
    trngHeaderFile.setType("HEADER")
    #Generate Output source

    trngSourceFile = trngComponent.createFileSymbol("TRNG_FILE_1", None)
    trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
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
    trngSystemDefFile.setSourcePath("../peripheral/trng_6334/templates/system/definitions.h.ftl")
    trngSystemDefFile.setMarkup(True)

def showWarning(trngWarning, event):
    trngWarning.setVisible(event["value"])

def showMenu(trngMenu, event):
    trngMenu.setVisible(not event["value"])
