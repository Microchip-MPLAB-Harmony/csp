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

def enable_generic_timer(symbol, event):
    component = event["source"]
    
    sys_counter = component.getSymbolByID("SYSTEM_COUNTER_ENABLE")
    sys_counter.setReadOnly(event["value"])
    if event["value"]:
        sys_counter.setValue(True)
    else:
        sys_counter.clearValue()

    component.getSymbolByID("GENERIC_TIMER_SOURCE").setEnabled(event["value"])
    component.getSymbolByID("GENERIC_TIMER_HEADER").setEnabled(event["value"])
    component.getSymbolByID("GENERIC_TIMER_SYS_DEF").setEnabled(event["value"])
    component.getSymbolByID("GENERIC_TIMER_SYS_INIT").setEnabled(event["value"])


def update_generic_timer_delta(symbol, event):
    component = event["source"]
    interrupt_prefix = component.getSymbolValue("GENERIC_TIMER_INTERRUPT_PREFIX")
    if component.getSymbolValue("GENERIC_TIMER_INTERRUPT"):
        sourceFreq = component.getSymbolValue("SYSTEM_COUNTER_FREQUENCY")
        targetPeriodMs = component.getSymbolValue("GENERIC_TIMER_PERIOD")
        rtosHandler = component.getSymbolValue("RTOS_INTERRUPT_HANDLER")
        component.setSymbolValue(interrupt_prefix + "_INTERRUPT_ENABLE", True)
        component.setSymbolValue(interrupt_prefix + "_INTERRUPT_HANDLER", 
            rtosHandler if rtosHandler != "" else "GENERIC_TIMER_InterruptHandler")
        symbol.setValue((sourceFreq / 1000) * targetPeriodMs)
    else:
        component.clearSymbolValue(interrupt_prefix + "_INTERRUPT_ENABLE")
        component.clearSymbolValue(interrupt_prefix + "_INTERRUPT_HANDLER")
        symbol.clearValue()


if __name__ == "__main__":
    gen_timer_menu = coreComponent.createMenuSymbol("GENERIC_TIMER_MENU", cortexMenu)
    gen_timer_menu.setLabel("Generic Timer")

    gen_timer_enable = coreComponent.createBooleanSymbol("GENERIC_TIMER_ENABLE", gen_timer_menu)
    gen_timer_enable.setLabel("Enable Generic Timer")
    gen_timer_enable.setDependencies(enable_generic_timer, ["GENERIC_TIMER_ENABLE"])

    gen_timer_interrupt = coreComponent.createBooleanSymbol("GENERIC_TIMER_INTERRUPT", gen_timer_enable)
    gen_timer_interrupt.setLabel("Enable timer interrupt")
    gen_timer_interrupt.setReadOnly(True)
    gen_timer_interrupt.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["GENERIC_TIMER_ENABLE"])

    gen_timer_period = coreComponent.createIntegerSymbol("GENERIC_TIMER_PERIOD", gen_timer_interrupt)
    gen_timer_period.setLabel("Timer period (milliseconds)")
    gen_timer_period.setMin(1)
    gen_timer_period.setMax(10000)
    gen_timer_period.setDefaultValue(1)
    gen_timer_period.setReadOnly(True)
    gen_timer_period.setDependencies(lambda symbol, event: symbol.setReadOnly(not event["value"]), ["GENERIC_TIMER_INTERRUPT"])

    gen_timer_compare_delta = coreComponent.createIntegerSymbol("GENERIC_TIMER_COMPARE_DELTA", gen_timer_menu)
    gen_timer_compare_delta.setVisible(False)
    gen_timer_compare_delta.setDependencies(update_generic_timer_delta, ["GENERIC_TIMER_INTERRUPT", "GENERIC_TIMER_PERIOD"])

    gen_timer_interrupt_prefix = coreComponent.createStringSymbol("GENERIC_TIMER_INTERRUPT_PREFIX", gen_timer_menu)
    gen_timer_interrupt_prefix.setVisible(False)
    gen_timer_interrupt_prefix.setValue("SecPhysTimer")

    gen_timer_rtos_vector = coreComponent.createStringSymbol("RTOS_INTERRUPT_HANDLER", None)
    gen_timer_rtos_vector.setVisible(False)

    
    config = Variables.get("__CONFIGURATION_NAME")

    cfile = coreComponent.createFileSymbol("GENERIC_TIMER_SOURCE", None)
    cfile.setSourcePath("../peripheral/generic_timer/templates/plib_generic_timer.c.ftl")
    cfile.setOutputName("plib_generic_timer.c")
    cfile.setDestPath("/peripheral/generic_timer/")
    cfile.setProjectPath("config/"+config+"/peripheral/generic_timer/")
    cfile.setType("SOURCE")
    cfile.setMarkup(True)
    cfile.setEnabled(False)

    hfile = coreComponent.createFileSymbol("GENERIC_TIMER_HEADER", None)
    hfile.setSourcePath("../peripheral/generic_timer/templates/plib_generic_timer.h.ftl")
    hfile.setOutputName("plib_generic_timer.h")
    hfile.setDestPath("/peripheral/generic_timer/")
    hfile.setProjectPath("config/"+config+"/peripheral/generic_timer/")
    hfile.setType("HEADER")
    hfile.setMarkup(True)
    hfile.setEnabled(False)

    sysDefFile = coreComponent.createFileSymbol( "GENERIC_TIMER_SYS_DEF", None )
    sysDefFile.setType( "STRING" )
    sysDefFile.setSourcePath( "../peripheral/generic_timer/templates/system/definitions.h.ftl" )
    sysDefFile.setOutputName( "core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sysDefFile.setMarkup(True)
    sysDefFile.setEnabled(False)

    sysInitFile = coreComponent.createFileSymbol( "GENERIC_TIMER_SYS_INIT", None )
    sysInitFile.setType( "STRING" )
    sysInitFile.setSourcePath( "../peripheral/generic_timer/templates/system/initialization.c.ftl" )
    sysInitFile.setOutputName( "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    sysInitFile.setMarkup(True)
    sysInitFile.setEnabled(False)

