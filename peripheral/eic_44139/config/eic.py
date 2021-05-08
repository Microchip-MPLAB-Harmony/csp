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

def show_polarity(symbol, event):
    index = symbol.getID().split("EIC_SRC")[1].split("_")[0]
    edge_combo = event["source"].getSymbolByID("EIC_SRC{0}_POLARITY_EDGE".format(index))
    level_combo = event["source"].getSymbolByID("EIC_SRC{0}_POLARITY_LEVEL".format(index))
    edge_combo.setVisible(event["value"] == "Edge")
    level_combo.setVisible(event["value"] == "Level")


def show_glitch_filter_value(symbol, event):
    index = symbol.getID().split("EIC_SRC")[1].split("_")[0]

    event["source"].getSymbolByID("EIC_SRC{0}_GLITCH_FILTER_VALUE".format(index)).setReadOnly(not event["value"])
    event["source"].getSymbolByID("EIC_SRC{0}_GLITCH_FILTER_VALUE".format(index)).setVisible(event["value"])


def show_eic_symbols(symbol, event):
    index = symbol.getID().split("EIC_SRC")[1].split("_")[0]
    
    event["source"].getSymbolByID("EIC_SRC{0}_DETECT".format(index)).setReadOnly(not event["value"])
    event["source"].getSymbolByID("EIC_SRC{0}_GLITCH_FILTER_ENABLE".format(index)).setReadOnly(not event["value"])
    
    event["source"].getSymbolByID("EIC_SRC{0}_DETECT".format(index)).setVisible(event["value"])
    event["source"].getSymbolByID("EIC_SRC{0}_GLITCH_FILTER_ENABLE".format(index)).setVisible(event["value"])

    if event["value"]:
        Database.setSymbolValue("core", "EIC_EXT_IRQ{0}_INTERRUPT_ENABLE".format(index), True)
        Database.setSymbolValue("core", "EIC_EXT_IRQ{0}_INTERRUPT_HANDLER".format(index),
                                 "EIC_EXT_IRQ{0}_InterruptHandler".format(index))
    else:
        Database.clearSymbolValue("core", "EIC_EXT_IRQ{0}_INTERRUPT_ENABLE".format(index))
        Database.clearSymbolValue("core", "EIC_EXT_IRQ{0}_INTERRUPT_HANDLER".format(index))


###################################################################################################
######################################### Component ###############################################
###################################################################################################

def instantiateComponent(eicComponent):
    eic_instance_name = eicComponent.createStringSymbol("EIC_INSTANCE_NAME", None)
    eic_instance_name.setVisible(False)
    eic_instance_name.setDefaultValue(eicComponent.getID().upper())

    # Enable clock
    Database.setSymbolValue("core", eic_instance_name.getValue()+"_CLOCK_ENABLE", True)
    
    #Find number of EIC configuration registers
    num_registers = 0
    for register in ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EIC\"]/register-group@[name=\"EIC\"]").getChildren():
        if register.getAttribute("name").startswith("EIC_SCFG"):
            num_registers = num_registers + 1
    
    eic_num_interrupts = eicComponent.createIntegerSymbol("EIC_NUM_INTERRUPTS", None)
    eic_num_interrupts.setVisible(False)
    eic_num_interrupts.setDefaultValue(num_registers)

    for index in range (0, num_registers):
        activate_sym = eicComponent.createBooleanSymbol("EIC_SRC{0}_ACTIVATE".format(index), None)
        activate_sym.setLabel("Activate EIC Interrupt {0}".format(index))
        activate_sym.setDescription(("Generates code for interrupt {0}.User should "
                                   " still enable the interrupt after registering"
                                   " the callback using its APIs".format(index)))


        detection_sym = eicComponent.createComboSymbol("EIC_SRC{0}_DETECT".format(index),
                                                        activate_sym, 
                                                        ["Edge", "Level"])
        detection_sym.setLabel("Detection")
        detection_sym.setDescription ("Edge or Level Interrupt")
        detection_sym.setVisible(False)                                                               

        polarity_edge_sym = eicComponent.createComboSymbol("EIC_SRC{0}_POLARITY_EDGE".format(index),
                                                            detection_sym,
                                                            ["Falling Edge", "Rising Edge"])
        polarity_edge_sym.setLabel("Polarity")
        polarity_edge_sym.setDescription("Trigger interrupt on Rising or falling edge")

        polarity_level_sym = eicComponent.createComboSymbol("EIC_SRC{0}_POLARITY_LEVEL".format(index),
                                                            detection_sym,
                                                            ["Active Low", "Active High"])
        polarity_level_sym.setLabel("Polarity")
        polarity_level_sym.setDescription("Trigger interrupt on Low or High level")
        polarity_level_sym.setVisible(False)

        detection_comment_sym = eicComponent.createCommentSymbol("EIC_SRC{0}_DETECT_COMMENT".format(index),
                                                                 detection_sym)
        detection_comment_sym.setLabel("Set the appropriate interrupt type (Level/Edge) in the interrupt controller")

        glitch_filter_enable_sym = eicComponent.createBooleanSymbol("EIC_SRC{0}_GLITCH_FILTER_ENABLE".format(index), activate_sym)
        glitch_filter_enable_sym.setLabel("Glitch Filter")
        glitch_filter_enable_sym.setDescription ("Enable glitch filter for EIC{0}".format(index))
        glitch_filter_enable_sym.setVisible(False)

        glitch_filter_select_sym = eicComponent.createKeyValueSetSymbol("EIC_SRC{0}_GLITCH_FILTER_VALUE".format(index), glitch_filter_enable_sym)
        glitch_filter_select_sym.setLabel("Glitch Filter Selector")
        glitch_filter_select_sym.setDescription("Input level is forwarded only if it is maintained for x cycles")
        for cycles in range(0,4):
            glitch_filter_select_sym.addKey("{0}_CYCLE{1}".format(2**cycles, "S" if cycles else ""),
                                            str(cycles),
                                            "{0} clock cycle{1}".format(2**cycles, "s" if cycles else ""))
            glitch_filter_select_sym.setDisplayMode("Description")
        glitch_filter_select_sym.setVisible(False)
        glitch_filter_select_sym.setOutputMode("Value")

        #Set symbol dependency callback after all symbols are created
        activate_sym.setDependencies(show_eic_symbols, ["EIC_SRC{0}_ACTIVATE".format(index)])
        detection_sym.setDependencies(show_polarity, ["EIC_SRC{0}_DETECT".format(index)])
        glitch_filter_enable_sym.setDependencies(show_glitch_filter_value, ["EIC_SRC{0}_GLITCH_FILTER_ENABLE".format(index)])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eic_header_file = eicComponent.createFileSymbol("EIC_HEADER", None)
    eic_header_file.setSourcePath("../peripheral/eic_44139/templates/plib_eic.h.ftl")
    eic_header_file.setOutputName("plib_"+eic_instance_name.getValue().lower()+".h")
    eic_header_file.setDestPath("/peripheral/eic/")
    eic_header_file.setProjectPath("config/" + configName + "/peripheral/eic/")
    eic_header_file.setType("HEADER")
    eic_header_file.setMarkup(True)

    eic_source_file = eicComponent.createFileSymbol("EIC_SOURCE", None)
    eic_source_file.setSourcePath("../peripheral/eic_44139/templates/plib_eic.c.ftl")
    eic_source_file.setOutputName("plib_"+eic_instance_name.getValue().lower()+".c")
    eic_source_file.setDestPath("/peripheral/eic/")
    eic_source_file.setProjectPath("config/" + configName + "/peripheral/eic/")
    eic_source_file.setType("SOURCE")
    eic_source_file.setMarkup(True)

    eic_sys_init_file = eicComponent.createFileSymbol("EIC_SYS_INT", None)
    eic_sys_init_file.setType("STRING")
    eic_sys_init_file.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eic_sys_init_file.setSourcePath("../peripheral/eic_44139/templates/system/initialization.c.ftl")
    eic_sys_init_file.setMarkup(True)

    eic_sys_def_file = eicComponent.createFileSymbol("EIC_SYS_DEF", None)
    eic_sys_def_file.setType("STRING")
    eic_sys_def_file.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eic_sys_def_file.setSourcePath("../peripheral/eic_44139/templates/system/definitions.h.ftl")
    eic_sys_def_file.setMarkup(True)

