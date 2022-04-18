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
global  cmccHeaderFile
global  cmccSourceFile
global  cmccSystemDefFile


symCCFGNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CMCC\"]/register-group@[name=\"CMCC\"]/register@[name=\"CMCC_CFG\"]")
symCCFGExists = coreComponent.createBooleanSymbol("CMCC_CCFG_EXISTS", None)
symCCFGExists.setDefaultValue(symCCFGNode is not None)
symCCFGExists.setVisible(False)

symNumInstance = coreComponent.createIntegerSymbol("CMCC_INSTANCE_COUNT", None)
symNumInstance.setVisible(False)

cmccModuleNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"CMCC\"]")
numInstance = len(cmccModuleNode.getChildren())
symNumInstance.setDefaultValue(numInstance)

#Multiinstance cache controller
if numInstance > 1:
    symCMCCIInstance = coreComponent.createStringSymbol("CMCC_ICACHE_INSTANCE", None)
    symCMCCIInstance.setVisible(False)
    symCMCCDInstance = coreComponent.createStringSymbol("CMCC_DCACHE_INSTANCE", None)
    symCMCCDInstance.setVisible(False)

    for instanceIndex in range (0,numInstance):
        paramsNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"CMCC\"]/instance@[name=\"CMCC{0}\"]/parameters".format(instanceIndex)).getChildren()
        for paramIndex in range (0, len(paramsNode)):
            if (paramsNode[paramIndex].getAttribute("name") == "ICACHE_PRESENT" and
                paramsNode[paramIndex].getAttribute("value") == "1"):
                symCMCCIInstance.setDefaultValue("CMCC{0}".format(instanceIndex))
            if (paramsNode[paramIndex].getAttribute("name") == "DCACHE_PRESENT" and
                paramsNode[paramIndex].getAttribute("value") == "1"):
                symCMCCDInstance.setDefaultValue("CMCC{0}".format(instanceIndex))


############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

cmccHeaderFile = coreComponent.createFileSymbol("CMCC_HEADER_FILE", None)
cmccHeaderFile.setSourcePath("../peripheral/cmcc_11108/templates/plib_cmcc.h.ftl")
cmccHeaderFile.setOutputName("plib_cmcc.h")
cmccHeaderFile.setDestPath("/peripheral/cmcc/")
cmccHeaderFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccHeaderFile.setType("HEADER")
cmccHeaderFile.setOverwrite(True)
cmccHeaderFile.setEnabled(True)
cmccHeaderFile.setMarkup(True)

cmccSourceFile = coreComponent.createFileSymbol("CMCC_SOURCE_FILE", None)
cmccSourceFile.setSourcePath("../peripheral/cmcc_11108/templates/plib_cmcc.c.ftl")
cmccSourceFile.setOutputName("plib_cmcc.c")
cmccSourceFile.setDestPath("/peripheral/cmcc/")
cmccSourceFile.setProjectPath("config/" + configName + "/peripheral/cmcc/")
cmccSourceFile.setType("SOURCE")
cmccSourceFile.setOverwrite(True)
cmccSourceFile.setMarkup(True)
cmccSourceFile.setEnabled(True)

# System Definition
cmccSystemDefFile = coreComponent.createFileSymbol("CMCC_SYS_DEF_FILE", None)
cmccSystemDefFile.setType("STRING")
cmccSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
cmccSystemDefFile.setSourcePath("../peripheral/cmcc_11108/templates/system/definitions.h.ftl")
cmccSystemDefFile.setMarkup(True)
