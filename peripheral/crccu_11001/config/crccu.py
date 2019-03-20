"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

def instantiateComponent(crccuComponent):

    crccuInstanceName = crccuComponent.createStringSymbol("CRCCU_INSTANCE_NAME", None)
    crccuInstanceName.setVisible(False)
    crccuInstanceName.setDefaultValue(crccuComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", crccuInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)
    
    crccuPolynomialNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRCCU"]/value-group@[name="CRCCU_MR__PTYPE"]')
    crccuPolynomialValues = crccuPolynomialNode.getChildren()

    crccuPolynomial = crccuComponent.createKeyValueSetSymbol("CRCCU_POLYNOMIAL", None)
    crccuPolynomial.setLabel("Select CRC Polynomial")
    for index in range(0, len(crccuPolynomialValues)):
        crccuPolynomialKey = crccuPolynomialValues[index].getAttribute("name")
        crccuPolynomialValue = crccuPolynomialValues[index].getAttribute("value")
        crccuPolynomialCaption = crccuPolynomialValues[index].getAttribute("caption")
        crccuPolynomial.addKey(crccuPolynomialKey, crccuPolynomialValue, crccuPolynomialCaption)
    crccuPolynomial.setOutputMode("Key")
    crccuPolynomial.setDisplayMode("Description")
    crccuPolynomial.setDefaultValue(0)

    crccuBitorderNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRCCU"]/value-group@[name="CRCCU_MR__BITORDER"]')
    crccuBitorderValues = crccuBitorderNode.getChildren()

    crccuBitorder = crccuComponent.createKeyValueSetSymbol("CRCCU_BITORDER", None)
    crccuBitorder.setLabel("Select CRC Bit order")
    for index in range(0, len(crccuBitorderValues)):
        crccuBitorderKey = crccuBitorderValues[index].getAttribute("name")
        crccuBitorderValue = crccuBitorderValues[index].getAttribute("value")
        crccuBitorderCaption = crccuBitorderValues[index].getAttribute("caption")
        crccuBitorder.addKey(crccuBitorderKey, crccuBitorderValue, crccuBitorderCaption)
    crccuBitorder.setOutputMode("Value")
    crccuBitorder.setDisplayMode("Key")
    crccuBitorder.setDefaultValue(0)


    crccuTwidth = crccuComponent.createKeyValueSetSymbol("CRCCU_TWIDTH", None)
    crccuTwidth.setLabel("Select CRC Transfer Width")
    crccuTwidth.addKey("BYTE", "0", "1 byte")
    crccuTwidth.addKey("HALFWORD", "1", "2 byte")
    crccuTwidth.addKey("WORD", "2", "4 byte")
    crccuTwidth.setOutputMode("Value")
    crccuTwidth.setDisplayMode("Key")
    crccuTwidth.setDefaultValue(0)

    
    crccuDivider = crccuComponent.createIntegerSymbol("CRCCU_DIVIDER", None)
    crccuDivider.setLabel("CRC transfer Frequency Divider")
    crccuDivider.setDefaultValue(0)
    crccuDivider.setMin(0)
    crccuDivider.setMax(15)

################################################################################
########                          Code Generation                      #########
################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    crccuModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CRCCU\"]")
    crccuModuleID = crccuModuleNode.getAttribute("id")

    # Instance Header File
    crccuHeaderFile = crccuComponent.createFileSymbol("CRCCU_INSTANCE_HEADER", None)
    crccuHeaderFile.setSourcePath("../peripheral/crccu_11001/templates/plib_crccu.h.ftl")
    crccuHeaderFile.setOutputName("plib_"+crccuInstanceName.getValue().lower()+".h")
    crccuHeaderFile.setDestPath("/peripheral/crccu/")
    crccuHeaderFile.setProjectPath("config/" + configName + "/peripheral/crccu/")
    crccuHeaderFile.setType("HEADER")
    crccuHeaderFile.setMarkup(True)

    # Source File
    crccuSourceFile = crccuComponent.createFileSymbol("CRCCU_SOURCE", None)
    crccuSourceFile.setSourcePath("../peripheral/crccu_11001/templates/plib_crccu.c.ftl")
    crccuSourceFile.setOutputName("plib_" + crccuInstanceName.getValue().lower() + ".c")
    crccuSourceFile.setDestPath("/peripheral/crccu/")
    crccuSourceFile.setProjectPath("config/" + configName + "/peripheral/crccu/")
    crccuSourceFile.setType("SOURCE")
    crccuSourceFile.setMarkup(True)

    #System Initialization
    crccuSystemInitFile = crccuComponent.createFileSymbol("CRCCU_SYS_INIT", None)
    crccuSystemInitFile.setType("STRING")
    crccuSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    crccuSystemInitFile.setSourcePath("../peripheral/crccu_11001/templates/system/initialization.c.ftl")
    crccuSystemInitFile.setMarkup(True)

    #System Definition
    crccuSystemDefFile = crccuComponent.createFileSymbol("CRCCUu_SYS_DEF", None)
    crccuSystemDefFile.setType("STRING")
    crccuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    crccuSystemDefFile.setSourcePath("../peripheral/crccu_11001/templates/system/definitions.h.ftl")
    crccuSystemDefFile.setMarkup(True)