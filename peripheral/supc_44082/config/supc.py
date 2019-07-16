# coding: utf-8
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
#### Component ####
################################################################################
def instantiateComponent(supcComponent):

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())
    print("Running " + supcInstanceName.getValue())

    # SM configuration
    supcSMMenu= supcComponent.createBooleanSymbol("SM_ENABLE", None)
    supcSMMenu.setLabel("Enable Supply Monitor")
    supcSMMenu.setDefaultValue(True)

    supcSym_SMMR_SMRSTEN = supcComponent.createBooleanSymbol("SUPC_SMMR_SMRSTEN", supcSMMenu)
    supcSym_SMMR_SMRSTEN.setLabel("Enable Supply Monitor Reset")
    supcSym_SMMR_SMRSTEN.setDefaultValue(True)


############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    supcHeader2File = supcComponent.createFileSymbol("SUPC_HEADER", None)
    supcHeader2File.setMarkup(True)
    supcHeader2File.setSourcePath("../peripheral/supc_44082/templates/plib_supc.h.ftl")
    supcHeader2File.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcHeader2File.setDestPath("/peripheral/supc/")
    supcHeader2File.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcHeader2File.setType("HEADER")
    supcHeader2File.setOverwrite(True)

    supcSource1File = supcComponent.createFileSymbol("SUPC_SOURCE1", None)
    supcSource1File.setMarkup(True)
    supcSource1File.setSourcePath("../peripheral/supc_44082/templates/plib_supc.c.ftl")
    supcSource1File.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSource1File.setDestPath("/peripheral/supc/")
    supcSource1File.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSource1File.setType("SOURCE")
    supcSource1File.setOverwrite(True)

    supcSystemInitFile = supcComponent.createFileSymbol("SUPC_INIT", None)
    supcSystemInitFile.setType("STRING")
    supcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSystemInitFile.setSourcePath("../peripheral/supc_44082/templates/system/initialization.c.ftl")
    supcSystemInitFile.setMarkup(True)

    supcSystemDefFile = supcComponent.createFileSymbol("SUPC_DEF", None)
    supcSystemDefFile.setType("STRING")
    supcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSystemDefFile.setSourcePath("../peripheral/supc_44082/templates/system/definitions.h.ftl")
    supcSystemDefFile.setMarkup(True)

