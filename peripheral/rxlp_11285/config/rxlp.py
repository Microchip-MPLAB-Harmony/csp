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

def instantiateComponent(rxlpComponent):
    instanceName = rxlpComponent.createStringSymbol("RXLP_INSTANCE_NAME", None)
    instanceName.setVisible(False)
    instanceName.setDefaultValue(rxlpComponent.getID().upper());

    filterSym = rxlpComponent.createBooleanSymbol("FILTER", None)
    filterSym.setLabel("Filter")
    filterSym.setDescription("Enable Rx Digital Filter")
    filterSym.setVisible(True)
    filterSym.setDefaultValue(False)

    mrRegParity = Register.getRegisterModule("RXLP").getRegisterGroup("RXLP").getRegister("RXLP_MR").getBitfield("PAR")
    mrRegParityValues = Register.getRegisterModule("RXLP").getValueGroup(mrRegParity.getValueGroupName())
    parity = rxlpComponent.createKeyValueSetSymbol("PARITY", None)
    parity.setLabel("Parity")
    parity.setVisible(True)
    parity.setOutputMode("Value")
    parity.setDisplayMode("Key")
    for name in mrRegParityValues.getValueNames():
        value = mrRegParityValues.getValue(name)
        parity.addKey(value.getName(), value.getValue(), value.getDescription())


    cd = rxlpComponent.createIntegerSymbol("CD", None)
    cd.setVisible(True)
    cd.setLabel("CD")
    cd.setDescription("Baud rate is 32.768Khz / (16 * CD)")
    cd.setMin(1)
    cd.setMax(3)

    cdComment = rxlpComponent.createCommentSymbol(None, None)
    cdComment.setVisible(True)
    cdComment.setLabel("Baud Rate: " + str(32768/(16 * int(cd.getValue()))))
    cdComment.setDependencies(lambda symbol, event: symbol.setLabel("Baud Rate: " + str(32768/(16*int(cd.getValue())))), ["CD"])

    val1 = rxlpComponent.createIntegerSymbol("VAL1", None)
    val1.setLabel("VAL1")
    val1.setMin(0)
    val1.setMax(255)

    val2 = rxlpComponent.createIntegerSymbol("VAL2", None)
    val2.setLabel("VAL2")
    val2.setMin(0)
    val2.setMax(255)

    configName = Variables.get("__CONFIGURATION_NAME")

    srcFile = rxlpComponent.createFileSymbol(None, None)
    srcFile.setSourcePath("../peripheral/rxlp_11285/templates/plib_rxlp.c.ftl")
    srcFile.setOutputName("plib_"+instanceName.getValue().lower()+".c")
    srcFile.setDestPath("/peripheral/rxlp/")
    srcFile.setProjectPath("config/"+configName+"/peripheral/rxlp/")
    srcFile.setType("SOURCE")
    srcFile.setOverwrite(True)
    srcFile.setMarkup(True)

    hdrFile = rxlpComponent.createFileSymbol(None, None)
    hdrFile.setSourcePath("../peripheral/rxlp_11285/templates/plib_rxlp.h.ftl")
    hdrFile.setOutputName("plib_"+instanceName.getValue().lower()+".h")
    hdrFile.setDestPath("/peripheral/rxlp/")
    hdrFile.setProjectPath("config/"+configName+"/peripheral/rxlp/")
    hdrFile.setType("HEADER")
    hdrFile.setOverwrite(True)
    hdrFile.setMarkup(True)

    rxlpSystemInitFile = rxlpComponent.createFileSymbol(None, None)
    rxlpSystemInitFile.setType("STRING")
    rxlpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rxlpSystemInitFile.setSourcePath("../peripheral/rxlp_11285/templates/system/initialization.c.ftl")
    rxlpSystemInitFile.setMarkup(True)

    rxlpSystemDefFile = rxlpComponent.createFileSymbol(None, None)
    rxlpSystemDefFile.setType("STRING")
    rxlpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rxlpSystemDefFile.setSourcePath("../peripheral/rxlp_11285/templates/system/definitions.h.ftl")
    rxlpSystemDefFile.setMarkup(True)
