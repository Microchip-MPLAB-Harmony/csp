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

def updateVisibility (symbol, event):
    symbol.setVisible(event["value"])

def initFileGen (symbol, event):
    symbol.setEnabled(event["value"])

def updateNVICInterrupt(symbol, event):
    intEnable = False
    localComponent = symbol.getComponent()
    eccEnabled = localComponent.getSymbolValue("MCRAMC_ECC_TESTING_ENABLE")
    singleBitIntEnabled = localComponent.getSymbolValue("MCRAMC_ECC_SINGLE_BIT_ERR_INT_ENABLE")
    doubleBitIntEnabled = localComponent.getSymbolValue("MCRAMC_ECC_DOUBLE_BIT_ERR_INT_ENABLE")

    if eccEnabled == True and (singleBitIntEnabled == True or doubleBitIntEnabled == True):
        intEnable = True

    Database.setSymbolValue("core", "MCRAMC" + "_INTERRUPT_ENABLE", intEnable, 2)
    Database.setSymbolValue("core", "MCRAMC" + "_INTERRUPT_HANDLER_LOCK", intEnable, 2)
    if intEnable == False:
        Database.setSymbolValue("core", "MCRAMC" + "_INTERRUPT_HANDLER", "MCRAMC" + "_Handler", 2)
    else:
        Database.setSymbolValue("core", "MCRAMC" + "_INTERRUPT_HANDLER", "RAM_ECC" + "_InterruptHandler", 2)

ramInitFuncPrefix = ramComponent.createStringSymbol("RAM_INIT_FUNC_PREFIX", None)
ramInitFuncPrefix.setVisible(False)
ramInitFuncPrefix.setDefaultValue("RAM_ECC")

ramECCTestingEnable = ramComponent.createBooleanSymbol("MCRAMC_ECC_TESTING_ENABLE", None)
ramECCTestingEnable.setLabel("ECC Testing Enable")
ramECCTestingEnable.setDefaultValue(False)

ramECCDecoderEnable = ramComponent.createBooleanSymbol("MCRAMC_ECC_DECODER_ENABLE", ramECCTestingEnable)
ramECCDecoderEnable.setLabel("ECC Decoder Enable")
ramECCDecoderEnable.setDefaultValue(True)
ramECCDecoderEnable.setVisible(False)
ramECCDecoderEnable.setDependencies(updateVisibility, ["MCRAMC_ECC_TESTING_ENABLE"])

ramECCSBErrorEnable = ramComponent.createBooleanSymbol("MCRAMC_ECC_SINGLE_BIT_ERR_INT_ENABLE", ramECCTestingEnable)
ramECCSBErrorEnable.setLabel("ECC Single Bit Error Interrupt Enable")
ramECCSBErrorEnable.setDefaultValue(False)
ramECCSBErrorEnable.setVisible(False)
ramECCSBErrorEnable.setDependencies(updateVisibility, ["MCRAMC_ECC_TESTING_ENABLE"])

ramECCDBErrorEnable = ramComponent.createBooleanSymbol("MCRAMC_ECC_DOUBLE_BIT_ERR_INT_ENABLE", ramECCTestingEnable)
ramECCDBErrorEnable.setLabel("ECC Double Bit Error Interrupt Enable")
ramECCDBErrorEnable.setDefaultValue(False)
ramECCDBErrorEnable.setVisible(False)
ramECCDBErrorEnable.setDependencies(updateVisibility, ["MCRAMC_ECC_TESTING_ENABLE"])

# Internal symbol to enable NVIC interrupt
ramECCNVICInterruptEnable = ramComponent.createBooleanSymbol("MCRAMC_NVIC_INT_ENABLE", ramECCTestingEnable)
ramECCNVICInterruptEnable.setDefaultValue(False)
ramECCNVICInterruptEnable.setVisible(False)
ramECCNVICInterruptEnable.setDependencies(updateNVICInterrupt, ["MCRAMC_ECC_TESTING_ENABLE", "MCRAMC_ECC_SINGLE_BIT_ERR_INT_ENABLE", "MCRAMC_ECC_DOUBLE_BIT_ERR_INT_ENABLE"])

################################################################################
########                      Code Generation                      #############
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
ramHeaderFile = ramComponent.createFileSymbol("RAM_INSTANCE_HEADER", None)
ramHeaderFile.setSourcePath("../peripheral/ram/templates/plib_mcramc_03727.h.ftl")
ramHeaderFile.setOutputName("plib_" + ramInstanceName.getValue().lower() + ".h")
ramHeaderFile.setDestPath("/peripheral/ram/")
ramHeaderFile.setProjectPath("config/" + configName + "/peripheral/ram/")
ramHeaderFile.setType("HEADER")
ramHeaderFile.setMarkup(True)

# Source File
ramSourceFile = ramComponent.createFileSymbol("RAM_SOURCE", None)
ramSourceFile.setSourcePath("../peripheral/ram/templates/plib_mcramc_03727.c.ftl")
ramSourceFile.setOutputName("plib_" + ramInstanceName.getValue().lower() + ".c")
ramSourceFile.setDestPath("/peripheral/ram/")
ramSourceFile.setProjectPath("config/" + configName + "/peripheral/ram/")
ramSourceFile.setType("SOURCE")
ramSourceFile.setMarkup(True)

# System Definition
ramSystemDefFile = ramComponent.createFileSymbol("RAM_SYS_DEF", None)
ramSystemDefFile.setType("STRING")
ramSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
ramSystemDefFile.setSourcePath("../peripheral/ram/templates/system/definitions.h.ftl")
ramSystemDefFile.setMarkup(True)

# System Initialize
ramSystemInitFile = ramComponent.createFileSymbol("RAM_SYS_INIT", None)
ramSystemInitFile.setType("STRING")
ramSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
ramSystemInitFile.setSourcePath("../peripheral/ram/templates/system/initialization.c.ftl")
ramSystemInitFile.setMarkup(True)
ramSystemInitFile.setEnabled(False)
ramSystemInitFile.setDependencies(initFileGen, ["MCRAMC_ECC_TESTING_ENABLE"])