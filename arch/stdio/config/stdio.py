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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def onAttachmentConnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    remoteComponent.setSymbolValue("USART_INTERRUPT_MODE", False)
    localComponent.setSymbolValue("DEBUG_PERIPHERAL", remoteID)

def onAttachmentDisconnected(source, target):

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    remoteComponent.clearSymbolValue("USART_INTERRUPT_MODE")
    localComponent.clearSymbolValue("DEBUG_PERIPHERAL")

def setBuffSymVisibility(symbol, event):
    symbol.setVisible(event["value"] == 0)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(stdioComponent):

    debugID = stdioComponent.createStringSymbol("DEBUG_PERIPHERAL", None)
    debugID.setVisible(False)

    stdinBuffMode = stdioComponent.createBooleanSymbol("STDIN_BUFF_MODE", None)
    stdinBuffMode.setLabel("Use STDIN in buffered mode")
    stdinBuffMode.setDescription("Use stdin stream in buffered mode. Valid only for XC32 toolchain")
    stdinBuffMode.setVisible(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0)
    stdinBuffMode.setDependencies(setBuffSymVisibility,["core.COMPILER_CHOICE"])

    stdoutBuffMode = stdioComponent.createBooleanSymbol("STDOUT_BUFF_MODE", None)
    stdoutBuffMode.setLabel("Use STDOUT in buffered mode")
    stdoutBuffMode.setDescription("Use stdout in buffered mode")
    stdoutBuffMode.setVisible(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0)
    stdoutBuffMode.setDependencies(setBuffSymVisibility,["core.COMPILER_CHOICE"])

    stdioInitializeFile = stdioComponent.createFileSymbol("STDIO_INITIALIZE_DEF", None)
    stdioInitializeFile.setType("STRING")
    stdioInitializeFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZER_STATIC_FUNCTIONS")
    stdioInitializeFile.setSourcePath("stdio/templates/system/stdio_buffer_init.c.ftl")
    stdioInitializeFile.setMarkup(True)

    stdioSysInitFile = stdioComponent.createFileSymbol("STDIO_INITIALIZE_CALL", None)
    stdioSysInitFile.setType("STRING")
    stdioSysInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    stdioSysInitFile.setSourcePath("stdio/templates/system/initialize.c.ftl")
    stdioSysInitFile.setMarkup(True)