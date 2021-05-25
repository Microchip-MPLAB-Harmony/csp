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
def show_ps_dwdt_config_error(symbol, event):
    wdt_enable = event["source"].getSymbolValue("DWDT_PS_ENABLE")
    period = event["source"].getSymbolValue("DWDT_PS_PERIOD")

    repeat_enable = event["source"].getSymbolValue("DWDT_PS_REPEAT_THRESHOLD_ENABLE") != "Disable"
    repeat_threshold = event["source"].getSymbolValue("DWDT_PS_REPEAT_THRESHOLD")

    level_enable = event["source"].getSymbolValue("DWDT_PS_LEVEL_ENABLE")
    level_threshold = event["source"].getSymbolValue("DWDT_PS_LEVEL")

    comment = event["source"].getSymbolByID("DWDT_PS_CONFIG_ERROR_COMMENT")
    
    show_comment = False
    comment_string = "CONFIGURATION ERROR !!!: "
    if wdt_enable:
        if repeat_enable and level_enable and repeat_threshold > level_threshold:
            comment_string = comment_string + "repeat threshold should be less than level threshold"
            show_comment = True
        elif level_enable and level_threshold >= period:
            comment_string = comment_string + "level threshold should be less than period"
            show_comment = True
        elif repeat_enable and repeat_threshold >= period:
            comment_string = comment_string + "repeat threshold should be less than period"
            show_comment = True
        else:
            show_comment = False
    
    comment.setLabel(comment_string)
    comment.setVisible(show_comment)


def show_ns_dwdt_config_error(symbol, event):
    wdt_enable = event["source"].getSymbolValue("DWDT_NS_ENABLE")
    period = event["source"].getSymbolValue("DWDT_NS_PERIOD")
    period_limit = event["source"].getSymbolValue("DWDT_PS_NS_PERIOD_LIMIT")

    repeat_enable = event["source"].getSymbolValue("DWDT_NS_REPEAT_THRESHOLD_ENABLE")
    repeat_threshold = event["source"].getSymbolValue("DWDT_NS_REPEAT_THRESHOLD")
    repeat_limit = event["source"].getSymbolValue("DWDT_PS_NS_REPEAT_LIMIT")

    level_enable = event["source"].getSymbolValue("DWDT_NS_LEVEL_ENABLE")
    level_threshold = event["source"].getSymbolValue("DWDT_NS_LEVEL")
    level_limit = event["source"].getSymbolValue("DWDT_PS_NS_LEVEL_LIMIT")

    comment = event["source"].getSymbolByID("DWDT_NS_CONFIG_ERROR_COMMENT")
    
    show_comment = False
    comment_string = "CONFIGURATION ERROR !!!: "

    if wdt_enable:
        if period_limit > 0 and period > period_limit:
            comment_string = comment_string + "Period is larger than the limit set in PS settings"
            show_comment = True
        
        elif level_enable and level_limit > 0 and level_threshold > level_limit:
            comment_string = comment_string + "Level threshold is larger than the limit set in PS settings"
            show_comment = True
        
        elif repeat_enable and repeat_limit > 0 and repeat_threshold > repeat_limit:
            comment_string = comment_string + "Repeat threshold is larger than the limit set in PS settings"
            show_comment = True

        elif level_enable and level_threshold > period:
            comment_string = comment_string + "Level threshold is larger than period"
            show_comment = True 

        elif repeat_enable and level_enable and repeat_threshold > level_threshold:
            comment_string = comment_string + "Repeat threshold is larger than Level threshold"
            show_comment = True

        elif repeat_enable and repeat_threshold > period:
            comment_string = comment_string + "Repeat threshold is larger than period"
            show_comment = True                                

        else:
            show_comment = False
    
    comment.setLabel(comment_string)
    comment.setVisible(show_comment)


def show_secure_ns_config_error(symbol, event):
    period_min = event["source"].getSymbolValue("DWDT_PS_NS_PERIOD_MIN")
    period_max = event["source"].getSymbolValue("DWDT_PS_NS_PERIOD_MAX")

    repeat_min = event["source"].getSymbolValue("DWDT_PS_NS_REPEAT_MIN")
    repeat_max = event["source"].getSymbolValue("DWDT_PS_NS_REPEAT_MAX")

    level_min = event["source"].getSymbolValue("DWDT_PS_NS_LEVEL_MIN")
    level_max = event["source"].getSymbolValue("DWDT_PS_NS_LEVEL_MAX")

    comment = event["source"].getSymbolByID("DWDT_PS_CONFIG_NS_ERROR_COMMENT")
    
    show_comment = False
    comment_string = "CONFIGURATION ERROR: "

    if period_max < period_min:
        comment_string = comment_string + "Period max cannot be less than min"
        show_comment = True
    
    elif repeat_max < repeat_min:
        comment_string = comment_string + "Repeat threshold max cannot be less than min"
        show_comment = True

    elif level_max < level_min:
        comment_string = comment_string + "interrupt level threshold max cannot be less than min"
        show_comment = True
    else:
        show_comment = False

    comment.setLabel(comment_string)
    comment.setVisible(show_comment)
    

def control_ps_interrupt(symbol, event):
    wdt_enable = event["source"].getSymbolValue("DWDT_PS_ENABLE")
    period_int = event["source"].getSymbolValue("DWDT_PS_EVENT") == "Interrupt"
    repeat_int = event["source"].getSymbolValue("DWDT_PS_REPEAT_THRESHOLD_ENABLE") == "Interrupt"
    level_int  = event["source"].getSymbolValue("DWDT_PS_LEVEL_ENABLE")
    ns_period_int = event["source"].getSymbolValue("DWDT_PS_NS_PERIOD_INTERRUPT_ENABLE")
    ns_repeat_int = event["source"].getSymbolValue("DWDT_PS_NS_REPEAT_INTERRUPT_ENABLE")

    if (wdt_enable and (period_int or repeat_int or level_int)) or ns_period_int or ns_repeat_int:
        Database.setSymbolValue("core", "DWDT_SW_INTERRUPT_ENABLE", True)
        Database.setSymbolValue("core", "DWDT_SW_INTERRUPT_HANDLER", "DWDT_SW_InterruptHandler")
    else:
        Database.clearSymbolValue("core", "DWDT_SW_INTERRUPT_ENABLE")
        Database.clearSymbolValue("core", "DWDT_SW_INTERRUPT_HANDLER")


def control_ns_interrupt(symbol, event):
    period_int = event["source"].getSymbolValue("DWDT_NS_PERIOD_ENABLE")
    repeat_int = event["source"].getSymbolValue("DWDT_NS_REPEAT_THRESHOLD_ENABLE")
    level_int  = event["source"].getSymbolValue("DWDT_NS_LEVEL_ENABLE")

    if period_int or repeat_int or level_int:
        Database.setSymbolValue("core", "DWDT_NSW_INTERRUPT_ENABLE", True)
        Database.setSymbolValue("core", "DWDT_NSW_INTERRUPT_HANDLER", "DWDT_NSW_InterruptHandler")
    else:
        Database.clearSymbolValue("core", "DWDT_NSW_INTERRUPT_ENABLE")
        Database.clearSymbolValue("core", "DWDT_NSW_INTERRUPT_HANDLER")
    
###################################################################################################
######################################### Component ###############################################
###################################################################################################
if __name__ == "__main__":
    global md_slow_clk
    md_slow_clk = 32000
    max_count = 2**12 - 1

    ps_config_error_dep_list = []
    ps_interrupt_dep_list = []

    dwdt_menu = coreComponent.createMenuSymbol("DWDT_MENU", None)
    dwdt_menu.setLabel("DWDT")
    dwdt_menu.setDescription("Dual watchdog timer configurations")

    dwdt_ps_enable = coreComponent.createBooleanSymbol("DWDT_PS_ENABLE", dwdt_menu)
    dwdt_ps_enable.setLabel("Enable PS WDT")
    dwdt_ps_enable.setDescription("Enable Programmable secure watchdog timer")
    ps_interrupt_dep_list.append(dwdt_ps_enable.getID())
    ps_config_error_dep_list.append(dwdt_ps_enable.getID())

    ps_wdt_event = coreComponent.createComboSymbol("DWDT_PS_EVENT", dwdt_ps_enable, ["Reset", "Interrupt"])
    ps_wdt_event.setLabel ("WDT event")
    ps_wdt_event.setDescription("Programmable secure watchdog timer event configuration")
    ps_wdt_event.setReadOnly(True)
    ps_wdt_event.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])
    ps_config_error_dep_list.append(ps_wdt_event.getID())
    ps_interrupt_dep_list.append(ps_wdt_event.getID())

    ps_wdt_period = coreComponent.createIntegerSymbol("DWDT_PS_PERIOD", dwdt_ps_enable)
    ps_wdt_period.setLabel("Period count")
    ps_wdt_period.setMin(0)
    ps_wdt_period.setMax(max_count)
    ps_wdt_period.setReadOnly(True)
    ps_wdt_period.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])
    ps_config_error_dep_list.append(ps_wdt_period.getID())

    ps_wdt_period_ms = coreComponent.createIntegerSymbol("DWDT_PS_PERIOD_MS", dwdt_ps_enable)
    ps_wdt_period_ms.setLabel("Period (ms)")
    ps_wdt_period_ms.setReadOnly(True)
    ps_wdt_period_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_PS_PERIOD"])

    ps_wdt_lvl_enable = coreComponent.createBooleanSymbol("DWDT_PS_LEVEL_ENABLE", dwdt_ps_enable)
    ps_wdt_lvl_enable.setLabel("Enable level interrupt")
    ps_wdt_lvl_enable.setReadOnly(True)
    ps_wdt_lvl_enable.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])
    ps_config_error_dep_list.append(ps_wdt_lvl_enable.getID())
    ps_interrupt_dep_list.append(ps_wdt_lvl_enable.getID())

    ps_wdt_level = coreComponent.createIntegerSymbol("DWDT_PS_LEVEL", ps_wdt_lvl_enable)
    ps_wdt_level.setLabel("Level count")
    ps_wdt_level.setMin(0)
    ps_wdt_level.setMax(max_count)
    ps_wdt_level.setReadOnly(True)
    ps_wdt_level.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_LEVEL_ENABLE"])
    ps_config_error_dep_list.append(ps_wdt_level.getID())

    ps_wdt_level_ms = coreComponent.createIntegerSymbol("DWDT_PS_LEVEL_MS", ps_wdt_lvl_enable)
    ps_wdt_level_ms.setLabel("Level (ms)")
    ps_wdt_level_ms.setReadOnly(True)
    ps_wdt_level_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_PS_LEVEL"])

    ps_wdt_repeat_enable = coreComponent.createComboSymbol("DWDT_PS_REPEAT_THRESHOLD_ENABLE", dwdt_ps_enable, ["Disable", "Reset", "Interrupt"])
    ps_wdt_repeat_enable.setLabel("Repeat threshold violation event")
    ps_wdt_repeat_enable.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])
    ps_wdt_repeat_enable.setReadOnly(True)
    ps_config_error_dep_list.append(ps_wdt_repeat_enable.getID())
    ps_interrupt_dep_list.append(ps_wdt_repeat_enable.getID())

    ps_wdt_rpt_thrshold = coreComponent.createIntegerSymbol("DWDT_PS_REPEAT_THRESHOLD", ps_wdt_repeat_enable)
    ps_wdt_rpt_thrshold.setLabel("Repeat threshold count")
    ps_wdt_rpt_thrshold.setMin(0)
    ps_wdt_rpt_thrshold.setMax(max_count)
    ps_wdt_rpt_thrshold.setReadOnly(True)
    ps_wdt_rpt_thrshold.setDependencies(lambda symbol, event: symbol.setReadOnly(event["value"] == "Disable"), ["DWDT_PS_REPEAT_THRESHOLD_ENABLE"])
    ps_config_error_dep_list.append(ps_wdt_rpt_thrshold.getID())

    ps_wdt_rpt_thrshold_ms = coreComponent.createIntegerSymbol("DWDT_PS_REPEAT_THRESHOLD_MS", ps_wdt_repeat_enable)
    ps_wdt_rpt_thrshold_ms.setLabel("Repeat threshold (ms)")
    ps_wdt_rpt_thrshold_ms.setReadOnly(True)
    ps_wdt_rpt_thrshold_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_PS_REPEAT_THRESHOLD"])

    ps_wdt_debug_halt = coreComponent.createBooleanSymbol("DWDT_PS_DEBUG_HALT", dwdt_ps_enable)
    ps_wdt_debug_halt.setLabel("Halt on debug")
    ps_wdt_debug_halt.setReadOnly(True)
    ps_wdt_debug_halt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])

    ps_wdt_idle_halt = coreComponent.createBooleanSymbol("DWDT_PS_IDLE_HALT", dwdt_ps_enable)
    ps_wdt_idle_halt.setLabel("Halt on idle")
    ps_wdt_idle_halt.setReadOnly(True)
    ps_wdt_idle_halt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_PS_ENABLE"])

    ps_wdt_lock_config = coreComponent.createBooleanSymbol("DWDT_PS_LOCK_CONFIG", dwdt_ps_enable)
    ps_wdt_lock_config.setLabel("Lock changes")

    ps_wdt_config_error = coreComponent.createStringSymbol("DWDT_PS_CONFIG_ERROR", dwdt_ps_enable)
    ps_wdt_config_error.setVisible(False)
    ps_wdt_config_error.setDependencies(show_ps_dwdt_config_error, ps_config_error_dep_list)

    ps_wdt_config_error_comment = coreComponent.createCommentSymbol("DWDT_PS_CONFIG_ERROR_COMMENT", dwdt_ps_enable)
    ps_wdt_config_error_comment.setVisible(False)

    ps_wdt_ns_menu = coreComponent.createMenuSymbol("DWDT_PS_CONFIG_NS", dwdt_menu)
    ps_wdt_ns_menu.setLabel("Secure configurations for NS WDT")

    ps_wdt_ns_config_deps = []

    ps_wdt_ns_period_interrupt = coreComponent.createBooleanSymbol("DWDT_PS_NS_PERIOD_INTERRUPT_ENABLE", ps_wdt_ns_menu)
    ps_wdt_ns_period_interrupt.setLabel("Generate secure interrupt on NS WDT period event")
    ps_interrupt_dep_list.append(ps_wdt_ns_period_interrupt.getID())

    ps_wdt_ns_repeat_interrupt = coreComponent.createBooleanSymbol("DWDT_PS_NS_REPEAT_INTERRUPT_ENABLE", ps_wdt_ns_menu)
    ps_wdt_ns_repeat_interrupt.setLabel("Generate secure interrupt on NS WDT repeat event")
    ps_interrupt_dep_list.append(ps_wdt_ns_repeat_interrupt.getID())

    ps_wdt_ns_period_limit_menu = coreComponent.createMenuSymbol("DWDT_PS_NS_PERIOD_LIMIT_MENU", ps_wdt_ns_menu)
    ps_wdt_ns_period_limit_menu.setLabel("NS WDT period limits")

    ps_wdt_ns_period_max_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_PERIOD_MAX", ps_wdt_ns_period_limit_menu)
    ps_wdt_ns_period_max_limit.setLabel("Max")
    ps_wdt_ns_period_max_limit.setMin(0)
    ps_wdt_ns_period_max_limit.setMax(max_count)
    ps_wdt_ns_period_max_limit.setDefaultValue(max_count)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_period_max_limit.getID())

    ps_wdt_ns_period_min_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_PERIOD_MIN", ps_wdt_ns_period_limit_menu)
    ps_wdt_ns_period_min_limit.setLabel("Min")
    ps_wdt_ns_period_min_limit.setMin(0)
    ps_wdt_ns_period_min_limit.setMax(max_count)
    ps_wdt_ns_period_min_limit.setDefaultValue(0)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_period_min_limit.getID())

    ps_wdt_ns_repeat_limit_menu = coreComponent.createMenuSymbol("DWDT_PS_NS_REPEAT_LIMIT_MENU", ps_wdt_ns_menu)
    ps_wdt_ns_repeat_limit_menu.setLabel("NS WDT repeat threshold limits")

    ps_wdt_ns_repeat_max_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_REPEAT_MAX", ps_wdt_ns_repeat_limit_menu)
    ps_wdt_ns_repeat_max_limit.setLabel("Max")
    ps_wdt_ns_repeat_max_limit.setMin(0)
    ps_wdt_ns_repeat_max_limit.setMax(max_count)
    ps_wdt_ns_repeat_max_limit.setDefaultValue(max_count)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_repeat_max_limit.getID())

    ps_wdt_ns_repeat_min_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_REPEAT_MIN", ps_wdt_ns_repeat_limit_menu)
    ps_wdt_ns_repeat_min_limit.setLabel("Min")
    ps_wdt_ns_repeat_min_limit.setMin(0)
    ps_wdt_ns_repeat_min_limit.setMax(max_count)
    ps_wdt_ns_repeat_min_limit.setDefaultValue(0)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_repeat_min_limit.getID())

    ps_wdt_ns_level_limit_menu = coreComponent.createMenuSymbol("DWDT_PS_NS_LEVEL_LIMIT_MENU", ps_wdt_ns_menu)
    ps_wdt_ns_level_limit_menu.setLabel("NS WDT level threshold limits")

    ps_wdt_ns_level_max_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_LEVEL_MAX", ps_wdt_ns_level_limit_menu)
    ps_wdt_ns_level_max_limit.setLabel("Min")
    ps_wdt_ns_level_max_limit.setMin(0)
    ps_wdt_ns_level_max_limit.setMax(max_count)
    ps_wdt_ns_level_max_limit.setDefaultValue(max_count)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_level_max_limit.getID())

    ps_wdt_ns_level_min_limit = coreComponent.createIntegerSymbol("DWDT_PS_NS_LEVEL_MIN", ps_wdt_ns_level_limit_menu)
    ps_wdt_ns_level_min_limit.setLabel("Max")
    ps_wdt_ns_level_min_limit.setMin(0)
    ps_wdt_ns_level_min_limit.setMax(max_count)
    ps_wdt_ns_level_min_limit.setDefaultValue(0)
    ps_wdt_ns_config_deps.append(ps_wdt_ns_level_min_limit.getID())

    ps_wdt_ns_config_error = coreComponent.createStringSymbol("DWDT_PS_CONFIG_NS_ERROR", ps_wdt_ns_menu)
    ps_wdt_ns_config_error.setVisible(False)
    ps_wdt_ns_config_error.setDependencies(show_secure_ns_config_error, ps_wdt_ns_config_deps)

    ps_wdt_ns_config_error_comment = coreComponent.createCommentSymbol("DWDT_PS_CONFIG_NS_ERROR_COMMENT", ps_wdt_ns_menu)
    ps_wdt_ns_config_error_comment.setVisible(False)

    ps_wdt_interrupt_control = coreComponent.createBooleanSymbol("DWDT_PS_INTERRUPT_CONTROL", dwdt_ps_enable)
    ps_wdt_interrupt_control.setVisible(False)
    ps_wdt_interrupt_control.setDependencies(control_ps_interrupt, ps_interrupt_dep_list)

    ns_config_error_dep_list = ["DWDT_PS_NS_PERIOD_LIMIT", "DWDT_PS_NS_REPEAT_LIMIT", "DWDT_PS_NS_LEVEL_LIMIT"]

    ns_wdt_enable = coreComponent.createBooleanSymbol("DWDT_NS_ENABLE", dwdt_menu)
    ns_wdt_enable.setLabel("Enable NS WDT")
    ns_wdt_enable.setDescription("Never secure watchdog timer event configuaration")
    ns_config_error_dep_list.append(ns_wdt_enable.getID())

    ns_wdt_period = coreComponent.createIntegerSymbol("DWDT_NS_PERIOD", ns_wdt_enable)
    ns_wdt_period.setLabel("Period count")
    ns_wdt_period.setMin(0)
    ns_wdt_period.setMax(max_count)
    ns_wdt_period.setReadOnly(True)
    ns_wdt_period.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_period.getID())

    ns_wdt_period_ms = coreComponent.createIntegerSymbol("DWDT_NS_PERIOD_MS", ns_wdt_enable)
    ns_wdt_period_ms.setLabel("Period (ms)")
    ns_wdt_period_ms.setReadOnly(True)
    ns_wdt_period_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_NS_PERIOD"])

    ns_wdt_period_interrupt = coreComponent.createBooleanSymbol("DWDT_NS_PERIOD_ENABLE", ns_wdt_enable)
    ns_wdt_period_interrupt.setLabel("Enable period failure interrupt")
    ns_wdt_period_interrupt.setReadOnly(True)
    ns_wdt_period_interrupt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_period_interrupt.getID())

    ns_wdt_level_interrupt = coreComponent.createBooleanSymbol("DWDT_NS_LEVEL_ENABLE", ns_wdt_enable)
    ns_wdt_level_interrupt.setLabel("Enable level threshold failure interrupt")
    ns_wdt_level_interrupt.setReadOnly(True)
    ns_wdt_level_interrupt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_level_interrupt.getID())

    ns_wdt_level = coreComponent.createIntegerSymbol("DWDT_NS_LEVEL", ns_wdt_level_interrupt)
    ns_wdt_level.setLabel("Level threshold count")
    ns_wdt_level.setMin(0)
    ns_wdt_level.setMax(max_count)
    ns_wdt_level.setReadOnly(True)
    ns_wdt_level.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_LEVEL_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_level.getID())

    ns_wdt_level_ms = coreComponent.createIntegerSymbol("DWDT_NS_LEVEL_MS", ns_wdt_level_interrupt)
    ns_wdt_level_ms.setLabel("Repeat threshold (ms)")
    ns_wdt_level_ms.setReadOnly(True)
    ns_wdt_level_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_NS_LEVEL"])

    ns_wdt_repeat = coreComponent.createIntegerSymbol("DWDT_NS_REPEAT_THRESHOLD", ns_wdt_enable)
    ns_wdt_repeat.setLabel("Repeat threshold count")
    ns_wdt_repeat.setMin(0)
    ns_wdt_repeat.setMax(max_count)
    ns_wdt_repeat.setReadOnly(True)
    ns_wdt_repeat.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_repeat.getID())

    ns_wdt_repeat_ms = coreComponent.createIntegerSymbol("DWDT_NS_REPEAT_THRESHOLD_MS", ns_wdt_enable)
    ns_wdt_repeat_ms.setLabel("Repeat threshold (ms)")
    ns_wdt_repeat_ms.setReadOnly(True)
    ns_wdt_repeat_ms.setDependencies(lambda symbol, event: symbol.setValue((event["value"]*128*1000)/md_slow_clk), ["DWDT_NS_REPEAT_THRESHOLD"])

    ns_wdt_repeat_interrupt = coreComponent.createBooleanSymbol("DWDT_NS_REPEAT_THRESHOLD_ENABLE", ns_wdt_enable)
    ns_wdt_repeat_interrupt.setLabel("Enable repeat threshold failure interrupt")
    ns_wdt_repeat_interrupt.setReadOnly(True)
    ns_wdt_repeat_interrupt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])
    ns_config_error_dep_list.append(ns_wdt_repeat_interrupt.getID())


    ns_wdt_debug_halt = coreComponent.createBooleanSymbol("DWDT_NS_DEBUG_HALT", ns_wdt_enable)
    ns_wdt_debug_halt.setLabel("Halt on debug")
    ns_wdt_debug_halt.setReadOnly(True)
    ns_wdt_debug_halt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])

    ns_wdt_idle_halt = coreComponent.createBooleanSymbol("DWDT_NS_IDLE_HALT", ns_wdt_enable)
    ns_wdt_idle_halt.setLabel("Halt on idle")
    ns_wdt_idle_halt.setReadOnly(True)
    ns_wdt_idle_halt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])

    ns_wdt_rpthalm = coreComponent.createBooleanSymbol("DWDT_NS_RPTHALM", ns_wdt_enable)
    ns_wdt_rpthalm.setLabel("Repeat Threshold Alarm")
    ns_wdt_rpthalm.setDescription("Enable Repeat Threshold Alarm to security module")
    ns_wdt_rpthalm.setReadOnly(True)
    ns_wdt_rpthalm.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["DWDT_NS_ENABLE"])

    ns_wdt_lock_config = coreComponent.createBooleanSymbol("DWDT_NS_LOCK_CONFIG", ns_wdt_enable)
    ns_wdt_lock_config.setLabel("Lock changes")

    ns_wdt_config_error = coreComponent.createStringSymbol("DWDT_NS_CONFIG_ERROR", ns_wdt_enable)
    ns_wdt_config_error.setVisible(False)
    ns_wdt_config_error.setDependencies(show_ns_dwdt_config_error, ns_config_error_dep_list)

    ns_wdt_rpt_threshold_comment = coreComponent.createCommentSymbol("DWDT_NS_CONFIG_ERROR_COMMENT", ns_wdt_enable)
    ns_wdt_rpt_threshold_comment.setVisible(False)

    ns_wdt_interrupt_control = coreComponent.createBooleanSymbol("DWDT_NS_INTERRUPT_CONTROL", ns_wdt_enable)
    ns_wdt_interrupt_control.setVisible(False)
    ns_wdt_interrupt_control.setDependencies(control_ns_interrupt, ["DWDT_NS_PERIOD_ENABLE", "DWDT_NS_REPEAT_THRESHOLD_ENABLE", "DWDT_NS_LEVEL_ENABLE"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    dwdt_header_file = coreComponent.createFileSymbol("DWDT_HEADER", None)
    dwdt_header_file.setSourcePath("../peripheral/dwdt_44149/templates/plib_dwdt.h.ftl")
    dwdt_header_file.setOutputName("plib_dwdt.h")
    dwdt_header_file.setDestPath("/peripheral/dwdt/")
    dwdt_header_file.setProjectPath("config/" + configName + "/peripheral/dwdt/")
    dwdt_header_file.setType("HEADER")
    dwdt_header_file.setMarkup(True)

    dwdt_source_file = coreComponent.createFileSymbol("DWDT_SOURCE", None)
    dwdt_source_file.setSourcePath("../peripheral/dwdt_44149/templates/plib_dwdt.c.ftl")
    dwdt_source_file.setOutputName("plib_dwdt.c")
    dwdt_source_file.setDestPath("/peripheral/dwdt/")
    dwdt_source_file.setProjectPath("config/" + configName + "/peripheral/dwdt/")
    dwdt_source_file.setType("SOURCE")
    dwdt_source_file.setMarkup(True)

    dwdt_sys_init_file = coreComponent.createFileSymbol("DWDT_SYS_INT", None)
    dwdt_sys_init_file.setType("STRING")
    dwdt_sys_init_file.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    dwdt_sys_init_file.setSourcePath("../peripheral/dwdt_44149/templates/system/initialization.c.ftl")
    dwdt_sys_init_file.setMarkup(True)

    dwdt_sys_def_file = coreComponent.createFileSymbol("DWDT_SYS_DEF", None)
    dwdt_sys_def_file.setType("STRING")
    dwdt_sys_def_file.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dwdt_sys_def_file.setSourcePath("../peripheral/dwdt_44149/templates/system/definitions.h.ftl")
    dwdt_sys_def_file.setMarkup(True)