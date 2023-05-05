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

####################################################################################################
#################################          Component      ##########################################
####################################################################################################

def instantiateComponent(ipc_component):

    ipc_instance_name = ipc_component.createStringSymbol("IPC_INSTANCE_NAME", None)
    ipc_instance_name.setVisible(False)
    ipc_instance_name.setDefaultValue(ipc_component.getID().upper())

    ipc_total_irqs = ipc_component.createIntegerSymbol("TOTAL_IPC_IRQS", None)
    ipc_total_irqs.setVisible(False)
    ipc_total_irqs.setDefaultValue(32)

    core_component = Database.getComponentByID("core")
    core_component.setSymbolValue(ipc_instance_name.getValue() + "_INTERRUPT_ENABLE", True)
    core_component.setSymbolValue(ipc_instance_name.getValue() + "_INTERRUPT_HANDLER",
                                    ipc_instance_name.getValue() + "_InterruptHandler")

    ipc_wp = ipc_component.createBooleanSymbol("IPC_WRITE_PROTECT", None)
    ipc_wp.setLabel("Enable Write protect")

    irq_menu = ipc_component.createMenuSymbol("IPC_IRQ_MENU", None)
    irq_menu.setLabel("IRQs")

    for irq in range(ipc_total_irqs.getValue()):
        irq_enable = ipc_component.createBooleanSymbol("IPC_IRQ{0}_ENABLE".format(irq), irq_menu)
        irq_enable.setLabel("Enable IRQ{0}".format(irq))


    ################################################################################################
    ####################################### Code Generation  #######################################
    ################################################################################################

    config_name = Variables.get("__CONFIGURATION_NAME")

    ipc_header_file = ipc_component.createFileSymbol("IPC_COMMON_HEADER", None)
    ipc_header_file.setSourcePath("../peripheral/ipc_11204/templates/plib_ipc_common.h.ftl")
    ipc_header_file.setOutputName("plib_ipc_common.h")
    ipc_header_file.setMarkup(True)
    ipc_header_file.setDestPath("/peripheral/ipc/")
    ipc_header_file.setProjectPath("config/" + config_name + "/peripheral/ipc/")
    ipc_header_file.setType("HEADER")


    ipc_header_file = ipc_component.createFileSymbol("IPC_HEADER", None)
    ipc_header_file.setSourcePath("../peripheral/ipc_11204/templates/plib_ipc.h.ftl")
    ipc_header_file.setOutputName("plib_" + ipc_instance_name.getValue().lower() + ".h")
    ipc_header_file.setMarkup(True)
    ipc_header_file.setDestPath("/peripheral/ipc/")
    ipc_header_file.setProjectPath("config/" + config_name + "/peripheral/ipc/")
    ipc_header_file.setType("HEADER")

    ipc_source_file = ipc_component.createFileSymbol("IPC_SOURCE", None)
    ipc_source_file.setSourcePath("../peripheral/ipc_11204/templates/plib_ipc.c.ftl")
    ipc_source_file.setOutputName("plib_" + ipc_instance_name.getValue().lower() + ".c")
    ipc_source_file.setMarkup(True)
    ipc_source_file.setDestPath("/peripheral/ipc/")
    ipc_source_file.setProjectPath("config/" + config_name + "/peripheral/ipc/")
    ipc_source_file.setType("SOURCE")

    ipc_sys_init_file = ipc_component.createFileSymbol("IPC_SYS_INIT", None)
    ipc_sys_init_file.setType("STRING")
    ipc_sys_init_file.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ipc_sys_init_file.setSourcePath("../peripheral/ipc_11204/templates/system/initialization.c.ftl")
    ipc_sys_init_file.setMarkup(True)

    ipc_sys_def_file = ipc_component.createFileSymbol("IPC_SYS_DEF", None)
    ipc_sys_def_file.setType("STRING")
    ipc_sys_def_file.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ipc_sys_def_file.setSourcePath("../peripheral/ipc_11204/templates/system/definitions.h.ftl")
    ipc_sys_def_file.setMarkup(True)
