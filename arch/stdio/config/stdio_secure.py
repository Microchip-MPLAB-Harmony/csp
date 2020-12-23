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

def handleMessage(messageID, args):

    result_dict = {}

    if (messageID == "REQUEST_CONFIG_PARAMS"):
        if args.get("localComponentID") != None:
            result_dict = Database.clearSymbolValue(args["localComponentID"], "UART_INTERRUPT_MODE")

            result_dict = Database.sendMessage(args["localComponentID"], "UART_BLOCKING_MODE", {"isEnabled":True, "isReadOnly":True})

    return result_dict

def onAttachmentConnected(source, target):
    global debugID

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    debugID.setValue(remoteID, 2)

def onAttachmentDisconnected(source, target):
    global debugID

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    debugID.clearValue()

    dummyDict = {}
    dummyDict = Database.sendMessage(remoteID, "UART_BLOCKING_MODE", {"isReadOnly":False})

def setBuffSymVisibility(symbol, event):
    symbol.setVisible(event["value"] == 0)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(stdioComponent):
    global debugID

    debugID = stdioComponent.createStringSymbol("SECURE_DEBUG_PERIPHERAL", None)
    debugID.setVisible(False)

    stdinBuffMode = stdioComponent.createBooleanSymbol("SECURE_STDIN_BUFF_MODE", None)
    stdinBuffMode.setLabel("Use STDIN in buffered mode")
    stdinBuffMode.setDescription("Use stdin stream in buffered mode. Valid only for XC32 toolchain")
    stdinBuffMode.setVisible(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0)
    stdinBuffMode.setDependencies(setBuffSymVisibility,["core.COMPILER_CHOICE"])

    stdoutBuffMode = stdioComponent.createBooleanSymbol("SECURE_STDOUT_BUFF_MODE", None)
    stdoutBuffMode.setLabel("Use STDOUT in buffered mode")
    stdoutBuffMode.setDescription("Use stdout in buffered mode")
    stdoutBuffMode.setVisible(Database.getSymbolValue("core", "COMPILER_CHOICE") == 0)
    stdoutBuffMode.setDependencies(setBuffSymVisibility,["core.COMPILER_CHOICE"])

    stdioInitializeFile = stdioComponent.createFileSymbol("SECURE_STDIO_INITIALIZE_DEF", None)
    stdioInitializeFile.setType("STRING")
    stdioInitializeFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_INITIALIZER_STATIC_FUNCTIONS")
    stdioInitializeFile.setSourcePath("stdio/templates/system/trustzone/secure_stdio_buffer_init.c.ftl")
    stdioInitializeFile.setMarkup(True)

    stdioSysInitFile = stdioComponent.createFileSymbol("SECURE_STDIO_INITIALIZE_CALL", None)
    stdioSysInitFile.setType("STRING")
    stdioSysInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")
    stdioSysInitFile.setSourcePath("stdio/templates/system/trustzone/secure_initialize.c.ftl")
    stdioSysInitFile.setMarkup(True)