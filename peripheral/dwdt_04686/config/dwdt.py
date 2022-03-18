
"""*****************************************************************************
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
*****************************************************************************"""

###############################################################################
######################################### Callbacks ###########################
###############################################################################
def calculate_ms(symbol,event):
    index = symbol.getID().split("_")[0].split("WDT")[1]
    name = symbol.getID().split("_")[1]
    count = event["source"].getSymbolValue("WDT{0}_{1}".format(index, name))
    presc_sym = event["source"].getSymbolByID("WDT{0}_PRESCALER".format(index))
    prescaler = int(presc_sym.getSelectedKey().split("RATIO")[1])
    symbol.setValue(count * prescaler * 1000/ 32000)


def show_config_error(symbol, event):
    show_comment = False
    error_str = "CONFIGURATION ERROR !!!: "
    index = symbol.getID().split("_")[0].split("WDT")[1]
    wdt_enable = event["source"].getSymbolValue("WDT{0}_ENABLE".format(index))
    period = event["source"].getSymbolValue("WDT{0}_PERIOD".format(index))
    level = event["source"].getSymbolValue("WDT{0}_LEVEL".format(index))
    repeat = event["source"].getSymbolValue("WDT{0}_REPEAT".format(index))
    level_enable =  event["source"].getSymbolValue(
                                        "WDT{0}_LEVEL_ENABLE".format(index))
    repeat_enable = (event["source"].getSymbolValue(
                            "WDT{0}_REPEAT_ENABLE".format(index)) != "Disable")
    comment = event["source"].getSymbolByID(
                                        "WDT{0}_ERROR_COMMENT".format(index))

    if wdt_enable:
        if repeat_enable and level_enable and repeat > level:
            error_str = error_str + "repeat threshold should be less than level threshold"
            show_comment = True
        elif level_enable and level >= period:
            error_str = error_str + "level threshold should be less than period"
            show_comment = True
        elif repeat_enable and repeat >= period:
            error_str = error_str + "repeat threshold should be less than period"
            show_comment = True
        else:
            show_comment = False

    comment.setLabel(error_str)
    comment.setVisible(show_comment)


def configure_wdt_interrupt(symbol, event):
    comp = event["source"]
    index = symbol.getID().split("_")[0].split("WDT")[1]
    wdt_enable = comp.getSymbolValue("WDT{0}_ENABLE".format(index))
    int_enable = (comp.getSymbolValue("WDT{0}_EVENT".format(index))
                                                 == "Interrupt")
    int_enable = int_enable or (comp.getSymbolValue(
                        "WDT{0}_REPEAT_ENABLE".format(index)) == "Interrupt")
    int_enable = int_enable or comp.getSymbolValue(
                        "WDT{0}_LEVEL_ENABLE".format(index))
    int_enable = int_enable or comp.getSymbolValue(
                        "WDT{0}_RLDERR_ENABLE".format(index))
    if index == "0":
        int_enable = int_enable or comp.getSymbolValue("WDT0_W1PERINT_ENABLE")
        int_enable = int_enable or comp.getSymbolValue("WDT0_W1RPTHINT_ENABLE")

    if wdt_enable and int_enable:
        Database.setSymbolValue("core",
                                "DWDT{0}_INTERRUPT_ENABLE".format(index), True)
        Database.setSymbolValue("core",
                                "DWDT{0}_INTERRUPT_HANDLER".format(index),
                                "DWDT{0}_InterruptHandler".format(index))
        symbol.setValue(True)
    else:
        Database.clearSymbolValue("core",
                                  "DWDT{0}_INTERRUPT_ENABLE".format(index))
        Database.clearSymbolValue("core",
                                "DWDT{0}_INTERRUPT_HANDLER".format(index))
        symbol.clearValue()


###############################################################################
######################################### Component ###########################
###############################################################################
if __name__ == "__main__":
    max_count = 2**12 - 1

    wdt_component = coreComponent
    dwdt_menu = wdt_component.createMenuSymbol("DWDT_MENU", None)
    dwdt_menu.setLabel("DWDT")
    dwdt_menu.setDescription("Dual watchdog timer configurations")

    for index in range(2):
        error_sym_dep_list = []
        wdt_enable = wdt_component.createBooleanSymbol(
                                "WDT{0}_ENABLE".format(index), dwdt_menu)
        wdt_enable.setLabel("Enable WDT{0}".format(index))
        error_sym_dep_list.append(wdt_enable.getID())

        wdt_prescaler = wdt_component.createKeyValueSetSymbol(
            "WDT{0}_PRESCALER".format(index), wdt_enable)
        wdt_prescaler.setLabel("Prescaler")
        prescaler_node = ATDF.getNode("/avr-tools-device-file/modules/module"
            "@[name=\"DWDT\"]/register-group@[name=\"DWDT\"]/register@[name="
            "\"WDT{0}_IL\"]/bitfield@[name=\"PRESC\"]".format(index))
        prescaler_vg_name = prescaler_node.getAttribute("values")
        prescaler_vg_node = ATDF.getNode("/avr-tools-device-file/modules/module"
          "@[name=\"DWDT\"]/value-group@[name=\"" + prescaler_vg_name + "\"]")
        for value_node in prescaler_vg_node.getChildren():
            wdt_prescaler.addKey(value_node.getAttribute("name"),
                                 value_node.getAttribute("value"),
                                 value_node.getAttribute("caption"))
        wdt_prescaler.setOutputMode("Key")
        wdt_prescaler.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_event = wdt_component.createComboSymbol(
            "WDT{0}_EVENT".format(index), wdt_enable, ["Reset", "Interrupt"])
        wdt_event.setLabel ("WDT event")
        wdt_event.setDescription("Watchdog timer event configuration")
        wdt_event.setReadOnly(True)
        wdt_event.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_period = wdt_component.createIntegerSymbol(
                        "WDT{0}_PERIOD".format(index), wdt_enable)
        wdt_period.setLabel("Period count")
        wdt_period.setMin(0)
        wdt_period.setMax(max_count)
        wdt_period.setReadOnly(True)
        wdt_period.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_period_ms = wdt_component.createIntegerSymbol(
                            "WDT{0}_PERIOD_MS".format(index), wdt_enable)
        wdt_period_ms.setLabel("Period (ms)")
        wdt_period_ms.setReadOnly(True)
        wdt_period_ms.setDependencies(calculate_ms,
                                [wdt_period.getID(), wdt_prescaler.getID()])
        error_sym_dep_list.append(wdt_period.getID())

        wdt_level_enable = wdt_component.createBooleanSymbol(
                    "WDT{0}_LEVEL_ENABLE".format(index), wdt_enable)
        wdt_level_enable.setLabel("Enable level interrupt")
        wdt_level_enable.setReadOnly(True)
        wdt_level_enable.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])
        error_sym_dep_list.append(wdt_level_enable.getID())

        wdt_level = wdt_component.createIntegerSymbol(
                                "WDT{0}_LEVEL".format(index), wdt_level_enable)
        wdt_level.setLabel("Level count")
        wdt_level.setMin(0)
        wdt_level.setMax(max_count)
        wdt_level.setReadOnly(True)
        wdt_level.setDependencies(lambda symbol, event:
            symbol.setReadOnly(not event["value"]), [wdt_level_enable.getID()])
        error_sym_dep_list.append(wdt_level.getID())

        wdt_level_ms = wdt_component.createIntegerSymbol(
                        "WDT{0}_LEVEL_MS".format(index), wdt_level_enable)
        wdt_level_ms.setLabel("Level (ms)")
        wdt_level_ms.setReadOnly(True)
        wdt_level_ms.setDependencies(calculate_ms,
                                [wdt_level.getID(), wdt_prescaler.getID()])

        wdt_rpth_enable = wdt_component.createComboSymbol(
                            "WDT{0}_RPTH_ENABLE".format(index), wdt_enable,
                            ["Disable", "Reset", "Interrupt"])
        wdt_rpth_enable.setLabel("Repeat threshold violation event")
        wdt_rpth_enable.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])
        wdt_rpth_enable.setReadOnly(True)
        error_sym_dep_list.append(wdt_rpth_enable.getID())

        wdt_rpth = wdt_component.createIntegerSymbol(
                            "WDT{0}_RPTH".format(index), wdt_rpth_enable)
        wdt_rpth.setLabel("Repeat threshold count")
        wdt_rpth.setMin(0)
        wdt_rpth.setMax(max_count)
        wdt_rpth.setReadOnly(True)
        wdt_rpth.setDependencies(lambda symbol, event:
                            symbol.setReadOnly(event["value"] == "Disable"),
                            [wdt_rpth_enable.getID()])
        error_sym_dep_list.append(wdt_rpth.getID())

        wdt_rpth_ms = wdt_component.createIntegerSymbol(
                        "WDT{0}_RPTH_MS".format(index), wdt_rpth_enable)
        wdt_rpth_ms.setLabel("Repeat threshold (ms)")
        wdt_rpth_ms.setReadOnly(True)
        wdt_rpth_ms.setDependencies(calculate_ms,
                                [wdt_rpth.getID(), wdt_prescaler.getID()])

        wdt_enable.setDependencies(show_config_error, error_sym_dep_list)

        wdt_rlderr_enable = wdt_component.createBooleanSymbol(
                    "WDT{0}_RLDERR_ENABLE".format(index), wdt_enable)
        wdt_rlderr_enable.setLabel("Enable reload command error interrupt")
        wdt_rlderr_enable.setReadOnly(True)
        wdt_rlderr_enable.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        interrupt_sym_dep_list = [  wdt_enable.getID(),
                                    wdt_event.getID(),
                                    wdt_level_enable.getID(),
                                    wdt_rpth_enable.getID(),
                                    wdt_rlderr_enable.getID()]

        if index == 0:
            wdt_w1perint_enable = wdt_component.createBooleanSymbol(
                        "WDT{0}_W1PERINT_ENABLE".format(index), wdt_enable)
            wdt_w1perint_enable.setLabel("Enable watchdog 1 overflow interrupt")
            wdt_w1perint_enable.setReadOnly(True)
            wdt_w1perint_enable.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])
            interrupt_sym_dep_list.append(wdt_w1perint_enable.getID())

            wdt_w1rpthint_enable = wdt_component.createBooleanSymbol(
                        "WDT{0}_W1RPTHINT_ENABLE".format(index), wdt_enable)
            wdt_w1rpthint_enable.setLabel(
                                "Enable watchdog 1 repeat threshold interrupt")
            wdt_w1rpthint_enable.setReadOnly(True)
            wdt_w1rpthint_enable.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])
            interrupt_sym_dep_list.append(wdt_w1rpthint_enable.getID())

        wdt_interrupt_config = wdt_component.createBooleanSymbol(
                        "WDT{0}_INTERRUPT_ENABLE".format(index), wdt_enable)
        wdt_interrupt_config.setVisible(False)
        wdt_interrupt_config.setDependencies(configure_wdt_interrupt,
                                             interrupt_sym_dep_list)

        wdt_debug0_halt = wdt_component.createBooleanSymbol(
                            "WDT{0}_DBG0HLT".format(index), wdt_enable)
        wdt_debug0_halt.setLabel("Halt on core 0 debug")
        wdt_debug0_halt.setReadOnly(True)
        wdt_debug0_halt.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_debug1_halt = wdt_component.createBooleanSymbol(
                            "WDT{0}_DBG1HLT".format(index), wdt_enable)
        wdt_debug1_halt.setLabel("Halt on core 1 debug")
        wdt_debug1_halt.setReadOnly(True)
        wdt_debug1_halt.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_idle_halt = wdt_component.createBooleanSymbol(
                                    "WDT{0}_IDLEHLT".format(index), wdt_enable)
        wdt_idle_halt.setLabel("Halt on idle")
        wdt_idle_halt.setReadOnly(True)
        wdt_idle_halt.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        wdt_nrst_assert = wdt_component.createBooleanSymbol(
                                    "WDT{0}_NRSTDIS".format(index), wdt_enable)
        wdt_nrst_assert.setLabel("Assert NRST pin on Reset")
        wdt_nrst_assert.setReadOnly(True)
        wdt_nrst_assert.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])


        wdt_lock_config = wdt_component.createBooleanSymbol(
                                "WDT{0}_LOCK_CONFIG".format(index), wdt_enable)
        wdt_lock_config.setLabel("Lock configuration")
        wdt_lock_config.setDependencies(lambda symbol, event:
                symbol.setReadOnly(not event["value"]), [wdt_enable.getID()])

        if index == 1:
            wdt_limits_menu = wdt_component.createMenuSymbol(
                                "WDT{0}_LIMITS_MENU".format(index), wdt_enable)
            wdt_limits_menu.setLabel("WDT threshold limits")

            wdt_period_max = wdt_component.createIntegerSymbol(
                            "WDT{0}_PERIOD_MAX".format(index), wdt_limits_menu)
            wdt_period_max.setLabel("Maximum period value")
            wdt_period_max.setMin(0)
            wdt_period_max.setMax(max_count)
            wdt_period_max.setDefaultValue(max_count)

            wdt_period_min = wdt_component.createIntegerSymbol(
                            "WDT{0}_PERIOD_MIN".format(index), wdt_limits_menu)
            wdt_period_min.setLabel("Minimum period value")
            wdt_period_min.setMin(0)
            wdt_period_min.setMax(max_count)
            wdt_period_min.setDefaultValue(0)

            wdt_level_max = wdt_component.createIntegerSymbol(
                            "WDT{0}_LEVEL_MAX".format(index), wdt_limits_menu)
            wdt_level_max.setLabel("Maximum level value")
            wdt_level_max.setMin(0)
            wdt_level_max.setMax(max_count)
            wdt_level_max.setDefaultValue(max_count)

            wdt_level_min = wdt_component.createIntegerSymbol(
                            "WDT{0}_LEVEL_MIN".format(index), wdt_limits_menu)
            wdt_level_min.setLabel("Minimum level value")
            wdt_level_min.setMin(0)
            wdt_level_min.setMax(max_count)
            wdt_level_min.setDefaultValue(0)

            wdt_rpth_max = wdt_component.createIntegerSymbol(
                            "WDT{0}_RPTH_MAX".format(index), wdt_limits_menu)
            wdt_rpth_max.setLabel("Maximum repeat value")
            wdt_rpth_max.setMin(0)
            wdt_rpth_max.setMax(max_count)
            wdt_rpth_max.setDefaultValue(max_count)

            wdt_rpth_min = wdt_component.createIntegerSymbol(
                            "WDT{0}_RPTH_MIN".format(index), wdt_limits_menu)
            wdt_rpth_min.setLabel("Minimum repeat value")
            wdt_rpth_min.setMin(0)
            wdt_rpth_min.setMax(max_count)
            wdt_rpth_min.setDefaultValue(0)

        wdt_error_comment = wdt_component.createCommentSymbol(
                "WDT{0}_ERROR_COMMENT".format(index), wdt_enable)
        wdt_error_comment.setVisible(False)

###############################################################################
####################################### Code Generation  ######################
###############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    dwdt_header_file = wdt_component.createFileSymbol("DWDT_HEADER", None)
    dwdt_header_file.setSourcePath(
                        "../peripheral/dwdt_04686/templates/plib_dwdt.h.ftl")
    dwdt_header_file.setOutputName("plib_dwdt.h")
    dwdt_header_file.setDestPath("/peripheral/dwdt/")
    dwdt_header_file.setProjectPath(
                                "config/" + configName + "/peripheral/dwdt/")
    dwdt_header_file.setType("HEADER")
    dwdt_header_file.setMarkup(True)

    dwdt_source_file = wdt_component.createFileSymbol("DWDT_SOURCE", None)
    dwdt_source_file.setSourcePath(
                        "../peripheral/dwdt_04686/templates/plib_dwdt.c.ftl")
    dwdt_source_file.setOutputName("plib_dwdt.c")
    dwdt_source_file.setDestPath("/peripheral/dwdt/")
    dwdt_source_file.setProjectPath(
                                "config/" + configName + "/peripheral/dwdt/")
    dwdt_source_file.setType("SOURCE")
    dwdt_source_file.setMarkup(True)

    dwdt_sys_init_file = wdt_component.createFileSymbol("DWDT_SYS_INT", None)
    dwdt_sys_init_file.setType("STRING")
    dwdt_sys_init_file.setOutputName(
                                "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    dwdt_sys_init_file.setSourcePath(
            "../peripheral/dwdt_04686/templates/system/initialization.c.ftl")
    dwdt_sys_init_file.setMarkup(True)

    dwdt_sys_def_file = wdt_component.createFileSymbol("DWDT_SYS_DEF", None)
    dwdt_sys_def_file.setType("STRING")
    dwdt_sys_def_file.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dwdt_sys_def_file.setSourcePath(
                "../peripheral/dwdt_04686/templates/system/definitions.h.ftl")
    dwdt_sys_def_file.setMarkup(True)