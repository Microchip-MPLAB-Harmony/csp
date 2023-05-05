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

###################################################################################################
##################################### Global Variables ############################################
###################################################################################################

global setERBInterruptData
global nvicInterruptUpdateERB

###################################################################################################
########################################## Callbacks ##############################################
###################################################################################################

def setERBInterruptData(erb_interrupt_name, status):

    Database.setSymbolValue("core", erb_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", erb_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", erb_interrupt_name + "_INTERRUPT_HANDLER", erb_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", erb_interrupt_name + "_INTERRUPT_HANDLER", erb_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateERB(erbInterruptType, erb_vtrx, enable):
    interruptNameDir = "VTR" + erb_vtrx + "_PAD_MON"
    interruptNameAgg = "VTR" + erb_vtrx + "_PAD_MON_GRP"

    if erbInterruptType == "AGGREGATE":
        setERBInterruptData(interruptNameDir, False)
        setERBInterruptData(interruptNameAgg, enable)
    else:
        setERBInterruptData(interruptNameAgg, False)
        setERBInterruptData(interruptNameDir, enable)

def nvicInterruptUpdate(symbol, event):
    erbInterruptType = event["source"].getSymbolByID("ERB_PAD_MON_INTERRUPT_TYPE").getSelectedKey()
    
    enable_pu = event["source"].getSymbolByID("ERB_PAD_MON_VTR1_PU_INT_EN").getValue()
    enable_pd = event["source"].getSymbolByID("ERB_PAD_MON_VTR1_PD_INT_EN").getValue()
    nvicInterruptUpdateERB(erbInterruptType, "1", (enable_pu or enable_pd))
    enable_pu = event["source"].getSymbolByID("ERB_PAD_MON_VTR2_PU_INT_EN").getValue()
    enable_pd = event["source"].getSymbolByID("ERB_PAD_MON_VTR2_PD_INT_EN").getValue()
    nvicInterruptUpdateERB(erbInterruptType, "2", (enable_pu or enable_pd))

def updateVisibilityOnVTREnable(symbol, event):
    symbol.setVisible(event["value"])

def erbCodeGeneration(symbol, event):
    symbol.setEnabled(event["value"])
###################################################################################################
#######################################  EC Register Bank #########################################
###################################################################################################

erbInstances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EC_REG_BANK\"]")

erbInstanceName = coreComponent.createStringSymbol("ERB_INSTANCE_NAME", None)
erbInstanceName.setVisible(False)
erbInstanceName.setDefaultValue(erbInstances.getAttribute("name"))

#ERB menu
erbMenu = coreComponent.createMenuSymbol("ERB_MENU", None)
erbMenu.setLabel("EC Register Bank")

erbAHBErrorCtrl = coreComponent.createBooleanSymbol("ERB_AHB_ERROR_CTRL", erbMenu)
erbAHBErrorCtrl.setLabel("AHB Error Enable")
erbAHBErrorCtrl.setDefaultValue(False)

erbAltNvicIntEn = coreComponent.createBooleanSymbol("ERB_ALT_NVIC_INT_EN", erbMenu)
erbAltNvicIntEn.setLabel("Alternate NVIC Interrupt Enable")
erbAltNvicIntEn.setDefaultValue(True)

vtr1CtrlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EC_REG_BANK\"]/register-group@[name=\"EC_REG_BANK\"]/register@[name=\"PD_MON_CTRL\"]/bitfield@[name=\"CTRL_VTR1\"]")

erbVTR1PadMonOverrideEn = coreComponent.createBooleanSymbol("ERB_VTR1_PAD_MON_OVERRIDE_EN", erbMenu)
erbVTR1PadMonOverrideEn.setLabel("VTR1 Pad Monitor Override Enable")
erbVTR1PadMonOverrideEn.setDefaultValue(False)
erbVTR1PadMonOverrideEn.setVisible(vtr1CtrlNode != None)

erbVTR1InpBuffDis = coreComponent.createBooleanSymbol("ERB_VTR1_INP_BUF_DIS", erbVTR1PadMonOverrideEn)
erbVTR1InpBuffDis.setLabel("Input Buffer Disable")
erbVTR1InpBuffDis.setDefaultValue(False)
erbVTR1InpBuffDis.setVisible(False)
erbVTR1InpBuffDis.setDependencies(updateVisibilityOnVTREnable, ["ERB_VTR1_PAD_MON_OVERRIDE_EN"])

erbVTR1PadMonProtectEn = coreComponent.createBooleanSymbol("ERB_VTR1_PAD_MON_PROTECT_EN", erbVTR1PadMonOverrideEn)
erbVTR1PadMonProtectEn.setLabel("Power off Input/Output buffers and apply weak pull-down")
erbVTR1PadMonProtectEn.setDefaultValue(False)
erbVTR1PadMonProtectEn.setVisible(False)
erbVTR1PadMonProtectEn.setDependencies(updateVisibilityOnVTREnable, ["ERB_VTR1_PAD_MON_OVERRIDE_EN"])

vtr1_ctrl_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EC_REG_BANK\"]/value-group@[name=\"EC_REG_BANK_PD_MON_CTRL__CTRL_VTR1\"]").getChildren()

if vtr1_ctrl_values != None:
    erbVTR1Ctrl = coreComponent.createKeyValueSetSymbol("ERB_VTR1_CTRL", erbMenu)
    erbVTR1Ctrl.setLabel("Pad Monitor VTR1 I/O Rail Power")
    for index in range(len(vtr1_ctrl_values)):
        key = vtr1_ctrl_values[index].getAttribute("name")
        val = vtr1_ctrl_values[index].getAttribute("value")
        desc = vtr1_ctrl_values[index].getAttribute("caption")
        erbVTR1Ctrl.addKey(key, val, desc)
    erbVTR1Ctrl.setDisplayMode("Description")
    erbVTR1Ctrl.setOutputMode("Value")
    erbVTR1Ctrl.setDefaultValue(0)

erbVTR1PadMonPUIntEn = coreComponent.createBooleanSymbol("ERB_PAD_MON_VTR1_PU_INT_EN", erbMenu)
erbVTR1PadMonPUIntEn.setLabel("VTR1 Pad Monitor Power Up Interrupt Enable")
erbVTR1PadMonPUIntEn.setDefaultValue(False)
erbVTR1PadMonPUIntEn.setVisible(vtr1CtrlNode != None)

erbVTR1PadMonPDIntEn = coreComponent.createBooleanSymbol("ERB_PAD_MON_VTR1_PD_INT_EN", erbMenu)
erbVTR1PadMonPDIntEn.setLabel("VTR1 Pad Monitor Power Down Interrupt Enable")
erbVTR1PadMonPDIntEn.setDefaultValue(False)
erbVTR1PadMonPDIntEn.setVisible(vtr1CtrlNode != None)

vtr2CtrlNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EC_REG_BANK\"]/register-group@[name=\"EC_REG_BANK\"]/register@[name=\"PD_MON_CTRL\"]/bitfield@[name=\"CTRL_VTR2\"]")

erbVTR2PadMonOverrideEn = coreComponent.createBooleanSymbol("ERB_VTR2_PAD_MON_OVERRIDE_EN", erbMenu)
erbVTR2PadMonOverrideEn.setLabel("VTR2 Pad Monitor Override Enable")
erbVTR2PadMonOverrideEn.setDefaultValue(False)
erbVTR2PadMonOverrideEn.setVisible(vtr2CtrlNode != None)

erbVTR2InpBuffDis = coreComponent.createBooleanSymbol("ERB_VTR2_INP_BUF_DIS", erbVTR2PadMonOverrideEn)
erbVTR2InpBuffDis.setLabel("Input Buffer Disable")
erbVTR2InpBuffDis.setDefaultValue(False)
erbVTR2InpBuffDis.setVisible(False)
erbVTR2InpBuffDis.setDependencies(updateVisibilityOnVTREnable, ["ERB_VTR2_PAD_MON_OVERRIDE_EN"])

erbVTR2PadMonProtectEn = coreComponent.createBooleanSymbol("ERB_VTR2_PAD_MON_PROTECT_EN", erbVTR2PadMonOverrideEn)
erbVTR2PadMonProtectEn.setLabel("Power off Input/Output buffers and apply weak pull-down")
erbVTR2PadMonProtectEn.setDefaultValue(False)
erbVTR2PadMonProtectEn.setVisible(False)
erbVTR2PadMonProtectEn.setDependencies(updateVisibilityOnVTREnable, ["ERB_VTR2_PAD_MON_OVERRIDE_EN"])

vtr2_ctrl_values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EC_REG_BANK\"]/value-group@[name=\"EC_REG_BANK_PD_MON_CTRL__CTRL_VTR1\"]").getChildren()

if vtr2_ctrl_values != None:
    erbVTR2Ctrl = coreComponent.createKeyValueSetSymbol("ERB_VTR2_CTRL", erbMenu)
    erbVTR2Ctrl.setLabel("Pad Monitor VTR2 I/O Rail Power")
    for index in range(len(vtr2_ctrl_values)):
        key = vtr2_ctrl_values[index].getAttribute("name")
        val = vtr2_ctrl_values[index].getAttribute("value")
        desc = vtr2_ctrl_values[index].getAttribute("caption")
        erbVTR2Ctrl.addKey(key, val, desc)
    erbVTR2Ctrl.setDisplayMode("Description")
    erbVTR2Ctrl.setOutputMode("Value")
    erbVTR2Ctrl.setDefaultValue(0)

erbVTR2PadMonPUIntEn = coreComponent.createBooleanSymbol("ERB_PAD_MON_VTR2_PU_INT_EN", erbMenu)
erbVTR2PadMonPUIntEn.setLabel("VTR2 Pad Monitor Power Up Interrupt Enable")
erbVTR2PadMonPUIntEn.setDefaultValue(False)
erbVTR2PadMonPUIntEn.setVisible(vtr2CtrlNode != None)

erbVTR2PadMonPDIntEn = coreComponent.createBooleanSymbol("ERB_PAD_MON_VTR2_PD_INT_EN", erbMenu)
erbVTR2PadMonPDIntEn.setLabel("VTR2 Pad Monitor Power Down Interrupt Enable")
erbVTR2PadMonPDIntEn.setDefaultValue(False)
erbVTR2PadMonPDIntEn.setVisible(vtr2CtrlNode != None)

## Interrupt Setup
nvic_int_num = {}
nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "VTR1_PAD_MON"})

# Interrupt type selection
erbInterruptType = coreComponent.createKeyValueSetSymbol("ERB_PAD_MON_INTERRUPT_TYPE", erbMenu)
erbInterruptType.setLabel("Interrupt Type")
if nvic_int_num["direct_nvic_num"] != None:
    erbInterruptType.addKey("DIRECT", "0", "Direct")
if nvic_int_num["group_nvic_num"] != None:
    erbInterruptType.addKey("AGGREGATE", "1", "Aggregate")
erbInterruptType.setDefaultValue(0)
erbInterruptType.setDisplayMode("Description")
erbInterruptType.setOutputMode("Key")

# Trigger dependency when interrupt type changes
erbTmrNVICUpdate = coreComponent.createBooleanSymbol("ERB_UPDATE_NVIC_INTERRUPT", None)
erbTmrNVICUpdate.setVisible(False)
erbTmrNVICUpdate.setDependencies(nvicInterruptUpdate, ["ERB_PAD_MON_INTERRUPT_TYPE", "ERB_PAD_MON_VTR1_PU_INT_EN", "ERB_PAD_MON_VTR1_PD_INT_EN", "ERB_PAD_MON_VTR2_PU_INT_EN", "ERB_PAD_MON_VTR2_PD_INT_EN"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################


configName = Variables.get("__CONFIGURATION_NAME")

erbHeaderFile = coreComponent.createFileSymbol("ERB_HEADER", None)
erbHeaderFile.setSourcePath("../peripheral/ec_reg_bank_95/templates/plib_ec_reg_bank.h.ftl")
erbHeaderFile.setOutputName("plib_" + erbInstanceName.getValue().lower() + ".h")
erbHeaderFile.setDestPath("peripheral/ec_reg_bank/")
erbHeaderFile.setProjectPath("config/" + configName + "/peripheral/ec_reg_bank/")
erbHeaderFile.setType("HEADER")
erbHeaderFile.setMarkup(True)
erbHeaderFile.setEnabled(True)

erbSourceFile = coreComponent.createFileSymbol("ERB_SOURCE", None)
erbSourceFile.setSourcePath("../peripheral/ec_reg_bank_95/templates/plib_ec_reg_bank.c.ftl")
erbSourceFile.setOutputName("plib_" + erbInstanceName.getValue().lower() + ".c")
erbSourceFile.setDestPath("peripheral/ec_reg_bank/")
erbSourceFile.setProjectPath("config/" + configName + "/peripheral/ec_reg_bank/")
erbSourceFile.setType("SOURCE")
erbSourceFile.setMarkup(True)
erbSourceFile.setEnabled(True)

erbSystemDefFile = coreComponent.createFileSymbol("ERB_SYS_DEF", None)
erbSystemDefFile.setType("STRING")
erbSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
erbSystemDefFile.setSourcePath("../peripheral/ec_reg_bank_95/templates/system/definitions.h.ftl")
erbSystemDefFile.setMarkup(True)
erbSystemDefFile.setEnabled(True)

erbSystemInitFile = coreComponent.createFileSymbol("ERB_SYS_INT", None)
erbSystemInitFile.setType("STRING")
erbSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
erbSystemInitFile.setSourcePath("../peripheral/ec_reg_bank_95/templates/system/initialization.c.ftl")
erbSystemInitFile.setMarkup(True)
erbSystemInitFile.setEnabled(True)