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

def visibility_Control(symbol, event):
    global dacLPRC_Enable
    global dacMode
    if (dacLPRC_Enable.getValue() == False) and (dacMode.getValue() == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def DACCON_RegUpdate(symbol, event):
    component = symbol.getComponent()

    outen = int(component.getSymbolValue("DAC_OUTPUT_BUFFER")) << 6
    snh = int(component.getSymbolValue("DAC_MODE")) << 7
    lprcen = int(component.getSymbolValue("DAC_LPRC_ENABLE")) << 5
    
    daccon = (outen) | (snh) | (lprcen)
    symbol.setValue(daccon)

def DACCON2_RegUpdate(symbol, event):
    component = symbol.getComponent()

    prescaler = int(component.getSymbolValue("DAC_SNH_PRESCALER")) << 29
    Period = int(component.getSymbolValue("DAC_SNH_CLOCK_PERIOD")) << 16
    Width = int(component.getSymbolValue("DAC_SNH_CLOCK_WIDTH"))
    
    daccon2 = (prescaler) | (Period) | (Width)
    symbol.setValue(daccon2) 
################################################################################
########                        DAC Data Base Components               #########
################################################################################

def instantiateComponent(dacComponent):

    evctrldep = []

    dacInstanceName = dacComponent.createStringSymbol("DAC_INSTANCE_NAME", None)
    dacInstanceName.setVisible(False)
    dacInstanceName.setDefaultValue(dacComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", dacInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    
    dacOutputBuffer = dacComponent.createBooleanSymbol("DAC_OUTPUT_BUFFER", None)
    dacOutputBuffer.setLabel("Enable Output Buffer")
    dacOutputBuffer.setDefaultValue(False)
    
    global dacMode
    dacMode = dacComponent.createKeyValueSetSymbol("DAC_MODE", None)
    dacMode.setLabel("Dac Mode")
    dacMode.addKey("Normal Mode", "0x0", "Normal Mode")
    dacMode.addKey("Low Power Mode", "0x1", "Low Power Mode")
    dacMode.setDefaultValue(0)

    global dacLPRC_Enable
    dacLPRC_Enable = dacComponent.createBooleanSymbol("DAC_LPRC_ENABLE", None)
    dacLPRC_Enable.setLabel("Enable LPRC Clock")
    dacLPRC_Enable.setDefaultValue(False)

    dacPrescaler = dacComponent.createKeyValueSetSymbol("DAC_SNH_PRESCALER", None)
    dacPrescaler.setLabel("Sample and Hold Clock Prescaler")
    dacPrescaler.addKey("DIV_1", "0x0", "Sampling Clock is same as SnH Clock")
    dacPrescaler.addKey("DIV_2", "0x1", "Sampling Clock is SnH Clock/2")
    dacPrescaler.addKey("DIV_4", "0x2", "Sampling Clock is SnH Clock/4")
    dacPrescaler.addKey("DIV_8", "0x3", "Sampling Clock is SnH Clock/8")
    dacPrescaler.addKey("DIV_16", "0x4", "Sampling Clock is SnH Clock/16")
    dacPrescaler.addKey("DIV_32", "0x5", "Sampling Clock is SnH Clock/32")
    dacPrescaler.addKey("DIV_64", "0x6", "Sampling Clock is SnH Clock/64")
    dacPrescaler.addKey("DIV_128", "0x7", "Sampling Clock is SnH Clock/128")
    dacPrescaler.setOutputMode("Value")
    dacPrescaler.setDisplayMode("Description")
    dacPrescaler.setDefaultValue(0)
    dacPrescaler.setVisible(True)
    dacPrescaler.setDependencies(visibility_Control, ["DAC_LPRC_ENABLE", "DAC_MODE"])

    dacSnhClockPeriod = dacComponent.createHexSymbol("DAC_SNH_CLOCK_PERIOD", None)
    dacSnhClockPeriod.setLabel("Sample and Hold Clock Period")
    dacSnhClockPeriod.setDefaultValue(0x0)
    dacSnhClockPeriod.setVisible(True)
    dacSnhClockPeriod.setDependencies(visibility_Control, ["DAC_LPRC_ENABLE", "DAC_MODE"])

    dacSnhClockWidth = dacComponent.createHexSymbol("DAC_SNH_CLOCK_WIDTH", None)
    dacSnhClockWidth.setLabel("Sample and Hold Clock Width")
    dacSnhClockWidth.setDefaultValue(0x0)
    dacSnhClockWidth.setVisible(True)
    dacSnhClockWidth.setDependencies(visibility_Control, ["DAC_LPRC_ENABLE", "DAC_MODE"])



    dacconRegValue = dacComponent.createHexSymbol("DACCON_REG_VALUE", None)
    dacconRegValue.setDefaultValue(0x0)
    dacconRegValue.setVisible(False)
    dacconRegValue.setDependencies(DACCON_RegUpdate, ["DAC_OUTPUT_BUFFER", "DAC_MODE", "DAC_LPRC_ENABLE"])

    daccon2RegValue = dacComponent.createHexSymbol("DACCON2_REG_VALUE", None)
    daccon2RegValue.setDefaultValue(0x0)
    daccon2RegValue.setVisible(False)
    daccon2RegValue.setDependencies(DACCON2_RegUpdate, ["DAC_SNH_PRESCALER", "DAC_SNH_CLOCK_PERIOD", "DAC_SNH_CLOCK_WIDTH"])    
   
################################################################################
########                          Code Generation                      #########
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    dacHeaderFile = dacComponent.createFileSymbol("DAC_INSTANCE_HEADER", None)
    dacHeaderFile.setSourcePath("../peripheral/dac_ctrl_05063/templates/plib_dac_ctrl.h.ftl")
    dacHeaderFile.setOutputName("plib_"+dacInstanceName.getValue().lower()+".h")
    dacHeaderFile.setDestPath("/peripheral/dac_ctrl/")
    dacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dac_ctrl/")
    dacHeaderFile.setType("HEADER")
    dacHeaderFile.setMarkup(True)

    # Source File
    dacSourceFile = dacComponent.createFileSymbol("DAC_SOURCE", None)
    dacSourceFile.setSourcePath("../peripheral/dac_ctrl_05063/templates/plib_dac_ctrl.c.ftl")
    dacSourceFile.setOutputName("plib_" + dacInstanceName.getValue().lower() + ".c")
    dacSourceFile.setDestPath("/peripheral/dac_ctrl/")
    dacSourceFile.setProjectPath("config/" + configName + "/peripheral/dac_ctrl/")
    dacSourceFile.setType("SOURCE")
    dacSourceFile.setMarkup(True)

    #System Initialization
    dacSystemInitFile = dacComponent.createFileSymbol("DAC_SYS_INIT", None)
    dacSystemInitFile.setType("STRING")
    dacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    dacSystemInitFile.setSourcePath("../peripheral/dac_ctrl_05063/templates/system/initialization.c.ftl")
    dacSystemInitFile.setMarkup(True)

    #System Definition
    dacSystemDefFile = dacComponent.createFileSymbol("DAC_SYS_DEF", None)
    dacSystemDefFile.setType("STRING")
    dacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dacSystemDefFile.setSourcePath("../peripheral/dac_ctrl_05063/templates/system/definitions.h.ftl")
    dacSystemDefFile.setMarkup(True)
