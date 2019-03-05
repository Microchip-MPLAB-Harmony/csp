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

def instantiateComponent(lcdcComponent):
    configName = Variables.get("__CONFIGURATION_NAME")

    instanceName = lcdcComponent.createStringSymbol("LCDC_INSTANCE_NAME", None)
    instanceName.setReadOnly(True)
    instanceName.setDefaultValue(lcdcComponent.getID().upper())
    InterruptVector = instanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = instanceName.getValue() + "_INTERRUPT_HANDLER"

    #Enable the LCDC clock
    Database.setSymbolValue("core", "LCDC_CLOCK_ENABLE", True, 2)

    #Enable the LCDC Interrupt
    Database.setSymbolValue("core", InterruptVector, True, 2)
    Database.setSymbolValue("core", InterruptHandler, instanceName.getValue() + "_Interrupt_Handler", 2)


    #Generate Output Header
    lcdcHeaderFile = lcdcComponent.createFileSymbol("lcdcHeaderFile", None)
    lcdcHeaderFile.setSourcePath("../peripheral/lcdc_11062/templates/plib_lcdc.h.ftl")
    lcdcHeaderFile.setMarkup(True)
    lcdcHeaderFile.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    lcdcHeaderFile.setOverwrite(True)
    lcdcHeaderFile.setDestPath("peripheral/lcdc/")
    lcdcHeaderFile.setProjectPath("config/" + configName + "/peripheral/lcdc/")
    lcdcHeaderFile.setType("HEADER")

    #Generate Output source
    lcdcSourceFile = lcdcComponent.createFileSymbol("lcdcSourceFile", None)
    lcdcSourceFile.setSourcePath("../peripheral/lcdc_11062/templates/plib_lcdc.c.ftl")
    lcdcSourceFile.setMarkup(True)
    lcdcSourceFile.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    lcdcSourceFile.setOverwrite(True)
    lcdcSourceFile.setDestPath("peripheral/lcdc/")
    lcdcSourceFile.setProjectPath("config/" + configName + "/peripheral/lcdc/")
    lcdcSourceFile.setType("SOURCE")

    lcdcSystemDefFile = lcdcComponent.createFileSymbol("lcdcSystemDefFile", None)
    lcdcSystemDefFile.setType("STRING")
    lcdcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    lcdcSystemDefFile.setSourcePath("../peripheral/lcdc_11062/templates/system/definitions.h.ftl")
    lcdcSystemDefFile.setMarkup(True)

