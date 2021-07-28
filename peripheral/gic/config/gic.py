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

def update_shared_interrupt(symbol, event):
    module_instances = symbol.getValue().split(" ")
    component = event["source"]
    module_interrupt = component.getSymbolByID(module_instances[0] + "_INTERRUPT_ENABLE")
    sub_interrupt_enable = False
    for instance in module_instances[1:]:
        if component.getSymbolValue(instance + "_INTERRUPT_ENABLE"):
            sub_interrupt_enable = True
            break
    if sub_interrupt_enable:
        module_interrupt.setValue(True)
    else:
        module_interrupt.clearValue()


if __name__ == "__main__":

    #instantiateComponent of core Component
    menu = coreComponent.createMenuSymbol("GIC_MENU", None)
    menu.setLabel("Interrupt (GIC)")
    menu.setDescription("Interrupt configuration")

    interrupts_node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
    max_interrupt_index = 0

    interrupt_types = [("PPI", "Private Peripheral Interrupts"), ("SPI", "Shared Peripheral Interrupts")]
    interrupt_menus =  []
    for interrupt_type in interrupt_types:
            interrupt_menu = coreComponent.createMenuSymbol("{0}_MENU".format(interrupt_type[0]), menu)
            interrupt_menu.setLabel("{0} Interrupts".format(interrupt_type[0]))
            interrupt_menu.setDescription(interrupt_type[1])
            interrupt_menus.append(interrupt_menu)
    for interrupt_node in interrupts_node.getChildren():
        name  = interrupt_node.getAttribute("name")
        index = int(interrupt_node.getAttribute("index"))
        module_instances = interrupt_node.getAttribute("module-instance").split(" ")
        caption = interrupt_node.getAttribute("caption")

        if index > max_interrupt_index:
            max_interrupt_index = index

        if index > 15:
            
            interrupt_menu = interrupt_menus[0 if index < 32 else 1]

            interrupt_sym = coreComponent.createStringSymbol("INTERRUPT_ID_{0}".format(index), interrupt_menu)
            interrupt_sym.setVisible(False)

            sym_enable = coreComponent.createBooleanSymbol ("{0}_INTERRUPT_ENABLE".format(name), interrupt_menu)
            sym_enable.setLabel("Enable {0} interrupt".format(name))
            sym_enable.setDescription(caption)
            
            sym_handler = coreComponent.createStringSymbol("{0}_INTERRUPT_HANDLER".format(name), sym_enable)
            sym_handler.setLabel("{0} Handler".format(name))
            sym_handler.setDefaultValue("{0}_Handler".format(name))

            sym_config = coreComponent.createKeyValueSetSymbol("{0}_INTERRUPT_CONFIG".format(name), sym_enable)
            sym_config.setLabel("{0} Configuration".format(name))
            sym_config.addKey("LEVEL", "0", "Level Sensitive interrupt")
            sym_config.addKey("EDGE", "2", "Edge triggered interrupt")
            sym_config.setOutputMode("Key")
            sym_config.setReadOnly(index < 32)

            sym_priority = coreComponent.createIntegerSymbol ("{0}_INTERRUPT_PRIORITY".format(name), sym_enable)
            sym_priority.setLabel(" {0} interrupt priority".format(name))
            sym_priority.setMax(255)

            sym_security = coreComponent.createComboSymbol("{0}_INTERRUPT_SECURITY".format(name), sym_enable, ["SECURE", "NON_SECURE"])
            sym_security.setLabel("{0} security".format(name))

            if len(module_instances) > 1 and index > 31:
                sym_sub_list = []
                for instance in module_instances:
                    sym_sub_enable = coreComponent.createBooleanSymbol ("{0}_INTERRUPT_ENABLE".format(instance), sym_enable)
                    sym_sub_enable.setLabel("Enable {0}".format(instance))
                    sym_sub_list.append(sym_sub_enable.getID())
                    
                    sym_sub_handler = coreComponent.createStringSymbol("{0}_INTERRUPT_HANDLER".format(instance), sym_enable)
                    sym_sub_handler.setLabel("{0} Handler".format(instance))
                    sym_sub_handler.setDefaultValue("{0}_Handler".format(instance))

                interrupt_sym.setDefaultValue (name + " " + " ".join(module_instances))
                interrupt_sym.setDependencies(update_shared_interrupt, sym_sub_list)
            
            else:
                interrupt_sym.setDefaultValue(name)
    
    sym_interrupt_max_index = coreComponent.createIntegerSymbol("GIC_INTERRUPT_MAX_INDEX", menu)
    sym_interrupt_max_index.setVisible(False)
    sym_interrupt_max_index.setDefaultValue(max_interrupt_index)

    config = Variables.get("__CONFIGURATION_NAME")

    cfile = coreComponent.createFileSymbol("GIC_SOURCE", None)
    cfile.setSourcePath("../peripheral/gic/templates/plib_gic.c.ftl")
    cfile.setOutputName("plib_gic.c")
    cfile.setDestPath("/peripheral/gic/")
    cfile.setProjectPath("config/"+config+"/peripheral/gic/")
    cfile.setType("SOURCE")
    cfile.setMarkup(True)

    hfile = coreComponent.createFileSymbol("GIC_HEADER", None)
    hfile.setSourcePath("../peripheral/gic/templates/plib_gic.h.ftl")
    hfile.setOutputName("plib_gic.h")
    hfile.setDestPath("/peripheral/gic/")
    hfile.setProjectPath("config/"+config+"/peripheral/gic/")
    hfile.setType("HEADER")
    hfile.setMarkup(True)

    sys_def_file = coreComponent.createFileSymbol( "GIC_SYS_DEFS", None )
    sys_def_file.setType( "STRING" )
    sys_def_file.setSourcePath( "../peripheral/gic/templates/system/definitions.h.ftl" )
    sys_def_file.setOutputName( "core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES" )
    sys_def_file.setMarkup( True )


    sys_init_file = coreComponent.createFileSymbol( "GIC_SYS_INIT", None )
    sys_init_file.setType( "STRING" )
    sys_init_file.setSourcePath( "../peripheral/gic/templates/system/initialization.c.ftl" )
    sys_init_file.setOutputName( "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE" )
    sys_init_file.setMarkup( True )

    interruptsHeaderFile = coreComponent.createFileSymbol( "GIC_INTERRUPT_HANDLER_DECLS", None )
    interruptsHeaderFile.setType( "STRING" )
    interruptsHeaderFile.setSourcePath( "../peripheral/gic/templates/system/interrupt_handlers_decls.h.ftl" )
    interruptsHeaderFile.setOutputName( "core.LIST_SYSTEM_INTERRUPT_HANDLER_DECLS" )
    interruptsHeaderFile.setMarkup( True )

    weakHandleFile = coreComponent.createFileSymbol( "GIC_WEAK_HANDLERS", None )
    weakHandleFile.setType( "STRING" )
    weakHandleFile.setSourcePath( "../peripheral/gic/templates/system/interrupt_weak_handlers.c.ftl" )
    weakHandleFile.setOutputName( "core.LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS" )
    weakHandleFile.setMarkup( True )

    sharedHandleFile = coreComponent.createFileSymbol( "GIC_SHARED_HANDLERS", None )
    sharedHandleFile.setType( "STRING" )
    sharedHandleFile.setSourcePath( "../peripheral/gic/templates/system/interrupt_shared_handlers.c.ftl" )
    sharedHandleFile.setOutputName( "core.LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS" )
    sharedHandleFile.setMarkup( True )

            
            



