"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
######################################### Callbacks ###############################################
###################################################################################################

def get_bitfield_valuegroup(register, bitfield):
    bitfield_str = ("/avr-tools-device-file/modules/module@[name=\"ACC\"]"
                    "/register-group@[name=\"ACC\"]/register@[name=\"{0}\"]"
                    "/bitfield@[name=\"{1}\"]")
    val_group_str = ("/avr-tools-device-file/modules/module@[name=\"ACC\"]" 
                     "/value-group@[name=\"{0}\"]")
    bitfield = ATDF.getNode(bitfield_str.format(register, bitfield))
    return ATDF.getNode(val_group_str.format(bitfield.getAttribute("values"))).getChildren()


def update_interrupt(symbol, event):
    comp = Database.getComponentByID("core")
    acc_instance = symbol.getComponent().getID().upper()
    if event["value"]:
        comp.setSymbolValue(acc_instance + "_INTERRUPT_ENABLE", True)
        comp.setSymbolValue(acc_instance + "_INTERRUPT_HANDLER", acc_instance + "_InterruptHandler")
    else:
        comp.clearSymbolValue(acc_instance + "_INTERRUPT_ENABLE")
        comp.clearSymbolValue(acc_instance + "_INTERRUPT_HANDLER")

###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(accComponent):

    acc_instance_name = accComponent.createStringSymbol("ACC_INSTANCE_NAME", None)
    acc_instance_name.setVisible(False)
    acc_instance_name.setDefaultValue(accComponent.getID().upper())

    Database.setSymbolValue("core", acc_instance_name.getValue()+"_CLOCK_ENABLE", True)

    acc_selplus_sym = accComponent.createKeyValueSetSymbol("ACC_INPUT_SELPLUS", None)
    acc_selplus_sym.setLabel("Plus input")
    for value in get_bitfield_valuegroup("ACC_MR", "SELPLUS"):
        acc_selplus_sym.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

    acc_selminus_sym = accComponent.createKeyValueSetSymbol("ACC_INPUT_SELMINUS", None)
    acc_selminus_sym.setLabel("Minus input")
    for value in get_bitfield_valuegroup("ACC_MR", "SELMINUS"):
        acc_selminus_sym.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    
    acc_inv_sym = accComponent.createBooleanSymbol("ACC_OUTPUT_INVERT", None)
    acc_inv_sym.setLabel("Invert output")

    acc_mask_sym = accComponent.createKeyValueSetSymbol("ACC_OUTPUT_MASK", None)
    acc_mask_sym.setLabel("Output mask duration")
    for value in get_bitfield_valuegroup("ACC_ACR", "MSEL"):
        acc_mask_sym.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    acc_mask_sym.setDisplayMode("Description")

    acc_fault_sym = accComponent.createBooleanSymbol("ACC_FAULT_ENABLE", None)
    acc_fault_sym.setLabel("Enable Fault")

    acc_fault_src_sym  = accComponent.createKeyValueSetSymbol("ACC_FAULT_SOURCE", acc_fault_sym)
    acc_fault_src_sym.setLabel("Fault source")
    acc_fault_src_sym.setDisplayMode("Description")
    for value in get_bitfield_valuegroup("ACC_MR", "SELFS"):
        acc_fault_src_sym.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    acc_fault_src_sym.setDisplayMode("Description")
    acc_fault_src_sym.setOutputMode("Key")
    acc_fault_src_sym.setReadOnly(True)
    acc_fault_src_sym.setDependencies(lambda symbol, event:symbol.setReadOnly(not event["value"]), ["ACC_FAULT_ENABLE"])

    acc_interrupt_enable = accComponent.createBooleanSymbol("ACC_INTERRUPT_ENABLE", None)
    acc_interrupt_enable.setLabel("Enable Interrupt")
    acc_interrupt_enable.setDependencies(update_interrupt, ["ACC_INTERRUPT_ENABLE"])

    acc_edgetype_sym = accComponent.createKeyValueSetSymbol("ACC_INTERRUPT_EDGETYPE", acc_interrupt_enable)
    acc_edgetype_sym.setLabel("Interrupt trigger edge")
    for value in get_bitfield_valuegroup("ACC_MR", "EDGETYP"):
        acc_edgetype_sym.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    acc_edgetype_sym.setReadOnly(True)
    acc_edgetype_sym.setDependencies(lambda symbol, event:symbol.setReadOnly(not event["value"]), ["ACC_INTERRUPT_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    acc_header_file = accComponent.createFileSymbol("ACC_HEADER", None)
    acc_header_file.setSourcePath("../peripheral/acc_04597/templates/plib_acc.h.ftl")
    acc_header_file.setOutputName("plib_"+acc_instance_name.getValue().lower()+".h")
    acc_header_file.setDestPath("/peripheral/acc/")
    acc_header_file.setProjectPath("config/" + configName + "/peripheral/acc/")
    acc_header_file.setType("HEADER")
    acc_header_file.setMarkup(True)

    acc_source_file = accComponent.createFileSymbol("ACC_SOURCE", None)
    acc_source_file.setSourcePath("../peripheral/acc_04597/templates/plib_acc.c.ftl")
    acc_source_file.setOutputName("plib_"+acc_instance_name.getValue().lower()+".c")
    acc_source_file.setDestPath("/peripheral/acc/")
    acc_source_file.setProjectPath("config/" + configName + "/peripheral/acc/")
    acc_source_file.setType("SOURCE")
    acc_source_file.setMarkup(True)

    acc_sys_init_file = accComponent.createFileSymbol("ACC_SYS_INT", None)
    acc_sys_init_file.setType("STRING")
    acc_sys_init_file.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    acc_sys_init_file.setSourcePath("../peripheral/acc_04597/templates/system/initialization.c.ftl")
    acc_sys_init_file.setMarkup(True)

    acc_sys_def_file = accComponent.createFileSymbol("ACC_SYS_DEF", None)
    acc_sys_def_file.setType("STRING")
    acc_sys_def_file.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    acc_sys_def_file.setSourcePath("../peripheral/acc_04597/templates/system/definitions.h.ftl")
    acc_sys_def_file.setMarkup(True)