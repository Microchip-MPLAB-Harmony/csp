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

################################################################################
#### Business Logic ####
################################################################################

def instantiateComponent(otpcComponent):
    otpcInstanceName = otpcComponent.createStringSymbol("OTPC_INSTANCE_NAME", None)
    otpcInstanceName.setVisible(False)
    otpcInstanceName.setDefaultValue(otpcComponent.getID().upper())
    Log.writeInfoMessage("Running " + otpcInstanceName.getValue())

    #OTPC emulation
    otpcEmulation = otpcComponent.createBooleanSymbol("ENABLE_OTPC_EMULATION", None)
    otpcEmulation.setLabel("Enable Emulation mode")
    otpcEmulation.setDefaultValue(True)

    #OTPC emulation node
    otpcEmulStartNode = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name=\"OTPC\"]/instance@[name=\"OTPC\"]/parameters/param@[name=\"EMULATION_ADDRESS\"]')
    otpcEmulationAddress = otpcComponent.createStringSymbol("OTPC_EMULATION_ADDRESS", None)
    otpcEmulationAddress.setVisible(False)
    otpcEmulationAddress.setReadOnly(True)
    otpcEmulationAddress.setDefaultValue(otpcEmulStartNode.getAttribute("value"))

    otpcEmulSizeNode = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name=\"OTPC\"]/instance@[name=\"OTPC\"]/parameters/param@[name=\"EMULATION_SIZE\"]')
    otpcEmulationSize = otpcComponent.createStringSymbol("OTPC_EMULATION_SIZE", None)
    otpcEmulationSize.setVisible(False)
    otpcEmulationSize.setReadOnly(True)
    otpcEmulationSize.setDefaultValue(otpcEmulSizeNode.getAttribute("value"))

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    otpcHeaderFile = otpcComponent.createFileSymbol("OTPC_HEADER", None)
    otpcHeaderFile.setSourcePath("../peripheral/otpc_44105/templates/plib_otpc.h.ftl")
    otpcHeaderFile.setOutputName("plib_" + otpcInstanceName.getValue().lower() + ".h")
    otpcHeaderFile.setDestPath("/peripheral/otpc/")
    otpcHeaderFile.setProjectPath("config/" + configName +"/peripheral/otpc/")
    otpcHeaderFile.setType("HEADER")
    otpcHeaderFile.setMarkup(True)

    otpcSourceFile = otpcComponent.createFileSymbol("OTPC_SOURCE", None)
    otpcSourceFile.setSourcePath("../peripheral/otpc_44105/templates/plib_otpc.c.ftl")
    otpcSourceFile.setOutputName("plib_" + otpcInstanceName.getValue().lower() + ".c")
    otpcSourceFile.setDestPath("/peripheral/otpc/")
    otpcSourceFile.setProjectPath("config/" + configName +"/peripheral/otpc/")
    otpcSourceFile.setType("SOURCE")
    otpcSourceFile.setMarkup(True)

    otpcSystemInitFile = otpcComponent.createFileSymbol("OTPC_SYS_INIT", None)
    otpcSystemInitFile.setType("STRING")
    otpcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    otpcSystemInitFile.setSourcePath("../peripheral/otpc_44105/templates/system/initialization.c.ftl")
    otpcSystemInitFile.setMarkup(True)

    otpcSystemDefFile = otpcComponent.createFileSymbol("OTPC_SYS_DEF", None)
    otpcSystemDefFile.setType("STRING")
    otpcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    otpcSystemDefFile.setSourcePath("../peripheral/otpc_44105/templates/system/definitions.h.ftl")
    otpcSystemDefFile.setMarkup(True)