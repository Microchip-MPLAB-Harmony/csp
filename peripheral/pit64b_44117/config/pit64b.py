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

def update_period(symbol, event):
    period = event['source'].getSymbolByID("PERIOD")
    prescaler = event['source'].getSymbolByID("PRESCALER")
    input_freq = Database.getSymbolValue("core", "PIT64B_CLOCK_FREQUENCY")
    input_freq = input_freq / (prescaler.getValue()+1)
    symbol.setValue(1000000.0 * period.getValue() / input_freq, 0)

def update_ints(symbol, event):
    period_int = event['source'].getSymbolByID("PERIOD_INT")
    ovre_int = event['source'].getSymbolByID("OVRE_INT")
    sece_int = event['source'].getSymbolByID("SECE_INT")
    instance_name = event['source'].getSymbolByID("PIT64B_INSTANCE_NAME")
    int_en = event['source'].getSymbolByID("ENABLE_INTERRUPT")

    if period_int.getValue() or ovre_int.getValue() or sece_int.getValue() :
        Database.setSymbolValue("core", instance_name.getValue() + "_INTERRUPT_ENABLE", True, 0)
        Database.setSymbolValue("core", instance_name.getValue() + "_INTERRUPT_HANDLER", "PIT64B_InterruptHandler", 0)
        Database.setSymbolValue("core", instance_name.getValue() + "_INTERRUPT_HANDLER_LOCK", True, 0)
        int_en.setValue(True, 0)
    else:
        Database.clearSymbolValue("core", instance_name.getValue() + "_INTERRUPT_ENABLE")
        Database.clearSymbolValue("core", instance_name.getValue() + "_INTERRUPT_HANDLER")
        Database.clearSymbolValue("core", instance_name.getValue() + "_INTERRUPT_HANDLER_LOCK")
        int_en.setValue(False, 0)

def update_warning(symbol, event):
    instanceName = event['source'].getSymbolByID('PIT64B_INSTANCE_NAME')
    symbol.setVisible(Database.getSymbolValue('core','CLK_'+instanceName.getValue()+'_GCLKEN') == False and event['source'].getSymbolValue('SGCLK'))


def instantiateComponent(pit64Component):
    instanceName = pit64Component.createStringSymbol("PIT64B_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(pit64Component.getID().upper())

    cont_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PIT64B"]/register-group@[name="PIT64B"]/register@[name="PIT64B_MR"]/bitfield@[name="CONT"]')
    cont = pit64Component.createBooleanSymbol("CONT", None)
    cont.setLabel(cont_node.getAttribute("name"))
    cont.setDescription(cont_node.getAttribute("caption"))

    sgclk_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PIT64B"]/register-group@[name="PIT64B"]/register@[name="PIT64B_MR"]/bitfield@[name="SGCLK"]')
    sgclk = pit64Component.createBooleanSymbol("SGCLK", None)
    sgclk.setLabel(sgclk_node.getAttribute("name"))
    sgclk.setDescription(sgclk_node.getAttribute("caption"))

    sgclk_warning = pit64Component.createCommentSymbol("SGCLK_WARNING", None)
    sgclk_warning.setVisible(False)
    sgclk_warning.setLabel("WARNING: GCLK selected but not enabled")
    sgclk_warning.setDependencies(update_warning, ['core.CLK_'+instanceName.getValue()+'_GCLKEN', 'SGCLK'])

    smod_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PIT64B"]/register-group@[name="PIT64B"]/register@[name="PIT64B_MR"]/bitfield@[name="SMOD"]')
    smod = pit64Component.createBooleanSymbol("SMOD", None)
    smod.setLabel(smod_node.getAttribute("name"))
    smod.setDescription(smod_node.getAttribute("caption"))

    prescaler_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PIT64B"]/register-group@[name="PIT64B"]/register@[name="PIT64B_MR"]/bitfield@[name="PRESCALER"]')
    prescaler = pit64Component.createIntegerSymbol("PRESCALER", None)
    prescaler.setLabel(prescaler_node.getAttribute("name"))
    prescaler.setDescription(prescaler_node.getAttribute("caption"))
    prescaler.setMin(0)
    prescaler.setMax(15)

    period = pit64Component.createLongSymbol("PERIOD", None)
    period.setLabel("Timer Period")
    period.setDescription("Number of clock source ticks per period")
    period.setMin(0)

    period_msb = pit64Component.createIntegerSymbol("PERIOD_MSB", None)
    period_msb.setVisible(False)
    period_msb.setDefaultValue((period.getValue() & 0xFFFFFFFF00000000) >> 32)
    period_msb.setDependencies(lambda symbol, event:symbol.setValue((event['value'] & 0xFFFFFFFF00000000) >> 32), ['PERIOD'])

    period_lsb = pit64Component.createIntegerSymbol("PERIOD_LSB", None)
    period_lsb.setVisible(False)
    period_lsb.setDefaultValue(period.getValue() & 0xFFFFFFFF)
    period_lsb.setDependencies(lambda symbol, event:symbol.setValue(event['value'] & 0xFFFFFFFF), ['PERIOD'])

    period_us = pit64Component.createFloatSymbol("PERIOD_US", None)
    period_us.setLabel("Timer Period(us)")
    period_us.setReadOnly(True)
    input_freq = Database.getSymbolValue("core", "PIT64B_CLOCK_FREQUENCY")
    input_freq = input_freq / (prescaler.getValue()+1)
    period_us.setDefaultValue(1000000.0 * period.getValue() / input_freq)
    period_us.setDependencies(update_period, ['PERIOD', 'core.PIT64B_CLOCK_FREQUENCY'])

    freq_sym = pit64Component.createIntegerSymbol("SRC_FREQ", None)
    freq_sym.setVisible(False)
    freq_sym.setDefaultValue(Database.getSymbolValue("core", "PIT64B_CLOCK_FREQUENCY"))
    freq_sym.setDependencies(lambda symbol, event: symbol.setValue(event['value'], 0), ['core.PIT64B_CLOCK_FREQUENCY'])

    period_int = pit64Component.createBooleanSymbol("PERIOD_INT", None)
    period_int.setLabel("Timer Interrupt")

    ovre_int = pit64Component.createBooleanSymbol("OVRE_INT", None)
    ovre_int.setLabel("Overrun Error Interrupt")

    sece_int = pit64Component.createBooleanSymbol("SECE_INT", None)
    sece_int.setLabel("Safety/Security Interrupt")

    int_en = pit64Component.createBooleanSymbol("ENABLE_INTERRUPT", None)
    int_en.setVisible(False)


    period_int.setDependencies(update_ints, ['PERIOD_INT', 'OVRE_INT', 'SECE_INT'])
    ovre_int.setDependencies(update_ints, ['PERIOD_INT', 'OVRE_INT', 'SECE_INT'])
    sece_int.setDependencies(update_ints, ['PERIOD_INT', 'OVRE_INT', 'SECE_INT'])

    Database.setSymbolValue("core", instanceName.getValue() + "_CLOCK_ENABLE", True, 0)

    configName = Variables.get("__CONFIGURATION_NAME")

    File = pit64Component.createFileSymbol(None, None)
    File.setSourcePath("../peripheral/pit64b_44117/templates/plib_pit64b.h.ftl")
    File.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    File.setDestPath("peripheral/pit64b/")
    File.setProjectPath("config/"+configName+"/peripheral/pit64b/")
    File.setType("HEADER")
    File.setMarkup(True)

    File = pit64Component.createFileSymbol(None, None)
    File.setSourcePath("../peripheral/pit64b_44117/templates/plib_pit64b.c.ftl")
    File.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    File.setDestPath("peripheral/pit64b/")
    File.setProjectPath("config/"+configName+"/peripheral/pit64b/")
    File.setType("SOURCE")
    File.setMarkup(True)

    File = pit64Component.createFileSymbol(None, None)
    File.setSourcePath("../peripheral/pit64b_44117/templates/system/initialization.c.ftl")
    File.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    File.setType("STRING")
    File.setMarkup(True)

    File = pit64Component.createFileSymbol(None, None)
    File.setSourcePath("../peripheral/pit64b_44117/templates/system/definitions.h.ftl")
    File.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    File.setType("STRING")
    File.setMarkup(True)
