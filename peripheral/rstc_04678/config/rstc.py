"""****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
****************************************************************************"""
global interrupt_dep_list
interrupt_dep_list = []

def get_value_group_node(vg_name):

    vg_string = ("/avr-tools-device-file/modules/module@[name=\"RSTC\"]" +
                 "/value-group@[name=\"{0}\"]").format(vg_name)
    return ATDF.getNode(vg_string)


def get_bit_field_node(reg_name, bf_name):
    bf_string = ("/avr-tools-device-file/modules/module@[name=\"RSTC\"]/" +
                  "register-group/register@[name=\"{0}\"]"+
                  "/bitfield@[name=\"{1}\"]").format(reg_name, bf_name)
    return ATDF.getNode(bf_string)


def create_bool_symbols(component, parent, reg_name, bit_name):
    bit_symbol = None
    reg_string = ("/avr-tools-device-file/modules/module@[name=\"RSTC\"]/" +
                  "register-group/register@[name=\"{0}\"]".format(reg_name))
    init_val_str = ATDF.getNode(reg_string).getAttribute("initval")
    if init_val_str is not None:
        init_val = int(init_val_str, 0)
    else:
        init_val = 0
    bf_node = ATDF.getNode(reg_string +
                            "/bitfield@[name=\"{0}\"]".format(bit_name))
    if bf_node is not None:
        bit_symbol = component.createBooleanSymbol(
                                "{0}_{1}".format(reg_name, bit_name), parent)
        bit_symbol.setLabel(bf_node.getAttribute("caption"))
        mask = int(bf_node.getAttribute("mask"), 0)
        if (mask & init_val) != 0:
            bit_symbol.setDefaultValue(True)
    return bit_symbol


def handle_rstc_interrupt(symbol, event):
    interrupt_enabled = event["source"].getSymbolByID(
                    "RSTC_MR_URSTEN").getSelectedKey() == "Interrupt"
    if not interrupt_enabled:
        for sym_id in interrupt_dep_list :
            if (sym_id != "RSTC_MR_URSTEN" and
               event["source"].getSymbolValue(sym_id)):
                interrupt_enabled= True
                break

    if interrupt_enabled:
        Database.setSymbolValue("core", "RSTC_INTERRUPT_ENABLE", True)
        Database.setSymbolValue("core", "RSTC_INTERRUPT_HANDLER",
                     "RSTC_InterruptHandler")
        Database.setSymbolValue("core", "RSTC_INTERRUPT_HANDLER_LOCK", True)
    else:
        Database.clearSymbolValue("core", "RSTC_INTERRUPT_ENABLE")
        Database.clearSymbolValue("core", "RSTC_INTERRUPT_HANDLER")
        Database.clearSymbolValue("core", "RSTC_INTERRUPT_HANDLER_LOCK")

    symbol.setValue(interrupt_enabled)


if __name__ == "__main__":
    rstc_component = coreComponent
    all_mode_bits = ["BADXTRST", "CPEREN", "CORSMIEN", "URSTASYNC",
                  "SFTPMCRS","WDTPMC0","WDTPMC1", "CPUFEN", "SCKSW"]
    available_mode_bits = ""
    interrupt_src_bits = ["CORSMIEN"]
    interrupt_enabled = False

    rstc_menu = rstc_component.createMenuSymbol("RSTC_MENU", None)
    rstc_menu.setLabel("RSTC")

    rstc_name = rstc_component.createStringSymbol("RSTC_INSTANCE_NAME",
                                                                    rstc_menu)
    rstc_name.setVisible(False)
    rstc_name.setDefaultValue("RSTC")
    print("Running " + rstc_name.getValue())

    per_reset_support = rstc_component.createBooleanSymbol(
                                                "RSTC_PERRST_SUPPORT", None)
    per_reset_support.setVisible(False)
    per_reset_support.setDefaultValue(get_bit_field_node("RSTC_CR", "PERRST")
                                                                is not None)

    ursten = rstc_component.createKeyValueSetSymbol("RSTC_MR_URSTEN",
                                                                    rstc_menu)
    ursten.setLabel("Low level on NRST pin will trigger")
    ursten.addKey("Reset", "0", "Generates Reset")
    ursten.addKey("Interrupt", "1", "Generates Interrupt")
    ursten.addKey("No action", "2", "Generates no action")
    ursten.setOutputMode("Key")
    ursten.setDisplayMode("Key")
    interrupt_dep_list.append(ursten.getID())

    pwrsw_node = get_bit_field_node("RSTC_MR", "PWRSW")
    if pwrsw_node is not None:
        pwrsw = rstc_component.createKeyValueSetSymbol("RSTC_MR_PWRSW",
                                                                 rstc_menu)
        pwrsw.setLabel(pwrsw_node.getAttribute("caption"))
        pwrsw_vg_node = get_value_group_node(pwrsw_node.getAttribute("values"))
        for value in pwrsw_vg_node.getChildren():
            pwrsw.addKey(value.getAttribute("name"),
                         value.getAttribute("value"),
                         value.getAttribute("caption"))
        pwrsw.setDisplayMode("Description")
        pwrsw.setOutputMode("Value")


    for mode_bit in all_mode_bits:
        bit_symbol = create_bool_symbols(rstc_component, rstc_menu,
                                                    "RSTC_MR", mode_bit)
        if bit_symbol is not None:
            available_mode_bits = available_mode_bits + ":" + mode_bit
            if mode_bit == "CPEREN":
                bit_symbol.setValue(True)
            if mode_bit in interrupt_src_bits:
                interrupt_dep_list.append(bit_symbol.getID())
                interrupt_enabled = interrupt_enabled or bit_symbol.getValue()

    mode_bits_str = rstc_component.createStringSymbol("RSTC_MODE_BITS",
                                                                    rstc_menu)
    mode_bits_str.setVisible(False)
    mode_bits_str.setDefaultValue(available_mode_bits.lstrip(":"))

    cprocen = rstc_component.createBooleanSymbol("RSTC_MR_CPROCEN", rstc_menu)
    cprocen.setVisible(False)
    cprocen_node = get_bit_field_node("RSTC_MR", "CPROCEN")
    cprocen.setDefaultValue(cprocen_node is not None)

    rstc_interrupt = rstc_component.createBooleanSymbol(
                                            "INTERRUPT_ENABLE", rstc_menu)
    rstc_interrupt.setVisible(False)
    rstc_interrupt.setDefaultValue(interrupt_enabled)
    rstc_interrupt.setDependencies(handle_rstc_interrupt, interrupt_dep_list)
    if interrupt_enabled:
        Database.setSymbolValue("core", "RSTC_INTERRUPT_ENABLE", True)
        Database.setSymbolValue("core", "RSTC_INTERRUPT_HANDLER",
                     "RSTC_InterruptHandler")
        Database.setSymbolValue("core", "RSTC_INTERRUPT_HANDLER_LOCK", True)

    erstl_node = get_bit_field_node("RSTC_MR", "ERSTL")
    if erstl_node is not None:
        erstl = rstc_component.createIntegerSymbol("RSTC_MR_ERSTL", rstc_menu)
        erstl.setLabel(erstl_node.getAttribute("caption"))
        erstl.setMin(0)
        erstl.setMax(2**4 - 1)

    ###########################################################################
    #### Code Generation ####
    ###########################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rstc_header_file = rstc_component.createFileSymbol("RSTC_INSTANCE_HEADER", None)
    rstc_header_file.setSourcePath("../peripheral/rstc_04678/templates/plib_rstc.h.ftl")
    rstc_header_file.setOutputName("plib_rstc.h")
    rstc_header_file.setDestPath("peripheral/rstc/")
    rstc_header_file.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstc_header_file.setType("HEADER")
    rstc_header_file.setOverwrite(True)
    rstc_header_file.setMarkup(True)

    rstc_source_file = rstc_component.createFileSymbol("RSTC_SOURCE", None)
    rstc_source_file.setSourcePath("../peripheral/rstc_04678/templates/plib_rstc.c.ftl")
    rstc_source_file.setOutputName("plib_rstc.c")
    rstc_source_file.setDestPath("peripheral/rstc/")
    rstc_source_file.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstc_source_file.setType("SOURCE")
    rstc_source_file.setOverwrite(True)
    rstc_source_file.setMarkup(True)

    rstc_sysinit_string = rstc_component.createFileSymbol("RSTC_INIT", None)
    rstc_sysinit_string.setType("STRING")
    rstc_sysinit_string.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    rstc_sysinit_string.setSourcePath("../peripheral//rstc_04678//templates/system/initialization.c.ftl")
    rstc_sysinit_string.setMarkup(True)

    rstc_sysdef_string = rstc_component.createFileSymbol("RSTC_DEF", None)
    rstc_sysdef_string.setType("STRING")
    rstc_sysdef_string.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstc_sysdef_string.setSourcePath("../peripheral//rstc_04678//templates/system/definitions.h.ftl")
    rstc_sysdef_string.setMarkup(True)