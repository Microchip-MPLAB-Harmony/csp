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
##############           DIVAS DATABASE COMPONENTS               ###############
################################################################################

def instantiateComponent(divasComponent):

    divasInstanceName = divasComponent.createStringSymbol("DIVAS_INSTANCE_NAME", None)
    divasInstanceName.setVisible(False)
    divasInstanceName.setDefaultValue(divasComponent.getID().upper())
    Log.writeInfoMessage("Running " + divasInstanceName.getValue())

    #Enable or Disable lead zero optimization
    divasSym_DLZ = divasComponent.createBooleanSymbol("DIVAS_DLZ", None)
    divasSym_DLZ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:divas_u2258;register:%NOREGISTER%")
    divasSym_DLZ.setLabel("Enable Leading Zero optimization?")
    divasSym_DLZ.setDescription("32 bit divisions take 2-16 cycles when enabled; 16 cycles when disabled")
    divasSym_DLZ.setVisible(True)
    divasSym_DLZ.setDefaultValue(True)

    #Overload Divider operation
    divasSym_DLZ = divasComponent.createBooleanSymbol("DIVAS_DIV_OVERLOAD", None)
    divasSym_DLZ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:divas_u2258;register:%NOREGISTER%")
    divasSym_DLZ.setLabel("Overload  Divide Operator?")
    divasSym_DLZ.setVisible(True)
    divasSym_DLZ.setDefaultValue(False)

################################################################################
###################     Code Generation            #############################
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    divasModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DIVAS\"]")
    divasModuleID = divasModuleNode.getAttribute("id")

    divasSym_HeaderFile = divasComponent.createFileSymbol("DIVAS_HEADER", None)
    divasSym_HeaderFile.setSourcePath("../peripheral/divas_u2258/templates/plib_divas.h.ftl")
    divasSym_HeaderFile.setOutputName("plib_"+divasInstanceName.getValue().lower()+".h")
    divasSym_HeaderFile.setDestPath("peripheral/divas")
    divasSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_HeaderFile.setType("HEADER")
    divasSym_HeaderFile.setMarkup(True)

    divasSym_SourceFile = divasComponent.createFileSymbol("DIVAS_SOURCE", None)
    divasSym_SourceFile.setSourcePath("../peripheral/divas_u2258/templates/plib_divas.c.ftl")
    divasSym_SourceFile.setOutputName("plib_"+divasInstanceName.getValue().lower()+".c")
    divasSym_SourceFile.setDestPath("peripheral/divas")
    divasSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/divas/")
    divasSym_SourceFile.setType("SOURCE")
    divasSym_SourceFile.setMarkup(True)

    divasSystemDefFile = divasComponent.createFileSymbol("DIVAS_SYS_DEF", None)
    divasSystemDefFile.setType("STRING")
    divasSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    divasSystemDefFile.setSourcePath("../peripheral/divas_u2258/templates/system/definitions.h.ftl")
    divasSystemDefFile.setMarkup(True)

    divasSystemInitFile = divasComponent.createFileSymbol("DIVAS_SYS_INIT", None)
    divasSystemInitFile.setType("STRING")
    divasSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    divasSystemInitFile.setSourcePath("../peripheral/divas_u2258/templates/system/initialization.c.ftl")
    divasSystemInitFile.setMarkup(True)




