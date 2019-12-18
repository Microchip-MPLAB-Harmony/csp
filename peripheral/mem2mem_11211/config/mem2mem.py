# coding: utf-8
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
#### Component ####
################################################################################

def instantiateComponent(mem2memComponent):

    mem2memInstanceName = mem2memComponent.createStringSymbol("MEM2MEM_INSTANCE_NAME", None)
    mem2memInstanceName.setVisible(False)
    mem2memInstanceName.setDefaultValue(mem2memComponent.getID().upper())

    mem2memBitField_PTSR_ERR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MEM2MEM"]/register-group@[name="MEM2MEM"]/register@[name="MEM2MEM_PTSR"]/bitfield@[name="ERR"]')

    # Transfer Bus Error Report
    mem2memSym_PTSR_ERR = mem2memComponent.createBooleanSymbol("MEM2MEM_PTSR_ERR", None)
    mem2memSym_PTSR_ERR.setVisible(False)
    mem2memSym_PTSR_ERR.setDefaultValue(mem2memBitField_PTSR_ERR != None)

    Database.setSymbolValue("core", mem2memInstanceName.getValue() + "_CLOCK_ENABLE", True)

    interruptVector = mem2memInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = mem2memInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = mem2memInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, mem2memInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    mem2memHeader1File = mem2memComponent.createFileSymbol("MEM2MEM_FILE_0", None)
    mem2memHeader1File.setSourcePath("../peripheral/mem2mem_11211/templates/plib_mem2mem.h.ftl")
    mem2memHeader1File.setMarkup(True)
    mem2memHeader1File.setOutputName("plib_" + mem2memInstanceName.getValue().lower() + ".h")
    mem2memHeader1File.setDestPath("/peripheral/mem2mem/")
    mem2memHeader1File.setProjectPath("config/" + configName + "/peripheral/mem2mem/")
    mem2memHeader1File.setType("HEADER")

    mem2memSource1File = mem2memComponent.createFileSymbol("MEM2MEM_FILE_1", None)
    mem2memSource1File.setSourcePath("../peripheral/mem2mem_11211/templates/plib_mem2mem.c.ftl")
    mem2memSource1File.setMarkup(True)
    mem2memSource1File.setOutputName("plib_" + mem2memInstanceName.getValue().lower() + ".c")
    mem2memSource1File.setDestPath("/peripheral/mem2mem/")
    mem2memSource1File.setProjectPath("config/" + configName + "/peripheral/mem2mem/")
    mem2memSource1File.setType("SOURCE")

    mem2memSystemDefFile = mem2memComponent.createFileSymbol("MEM2MEM_FILE_3", None)
    mem2memSystemDefFile.setType("STRING")
    mem2memSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mem2memSystemDefFile.setSourcePath("../peripheral/mem2mem_11211/templates/system/definitions.h.ftl")
    mem2memSystemDefFile.setMarkup(True)
