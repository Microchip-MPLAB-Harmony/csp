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

qspiRegModule = Register.getRegisterModule("QSPI")
qspiRegGroup = qspiRegModule.getRegisterGroup("QSPI")

qspiReg_MR = qspiRegGroup.getRegister("QSPI_MR")

qspiBitField_MR_SMM = qspiReg_MR.getBitfield("SMM")
qspiBitField_MR_CSMODE = qspiReg_MR.getBitfield("CSMODE")

qspiValGrp_MR_SMM = qspiRegModule.getValueGroup(qspiBitField_MR_SMM.getValueGroupName())
qspiValGrp_MR_CSMODE = qspiRegModule.getValueGroup(qspiBitField_MR_CSMODE.getValueGroupName())

qspiReg_SCR = qspiRegGroup.getRegister("QSPI_SCR")

qspiBitField_SCR_CPOL = qspiReg_SCR.getBitfield("CPOL")
qspiBitField_SCR_CPHA = qspiReg_SCR.getBitfield("CPHA")
qspiBitField_SCR_SCBR = qspiReg_SCR.getBitfield("SCBR")

qspiReg_ICR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/register-group@[name="QSPI"]/register@[name="QSPI_ICR"]')

def getMasterClkFrequency():
    return int(Database.getSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_FREQUENCY"))

def getQspiClkFrequency():
    global qspiInstanceName
    return Database.getSymbolValue(qspiInstanceName.getValue().lower(), "QSPI_CLK_FREQ")

def getQspiScbrValue():
    global qspiInstanceName
    return Database.getSymbolValue(qspiInstanceName.getValue().lower(), "QSPI_SCBR")

def setQspiClkFrequency(symbol, event):
    master_clk_freq = getMasterClkFrequency()

    if ( symbol.getID() == "QSPI_CLK_FREQ" ):
        qspi_clk_freq = master_clk_freq / (getQspiScbrValue() + 1)

        if ( qspi_clk_freq > symbol.getMax()):
            qspi_clk_freq = symbol.getMax()

        symbol.clearValue()
        symbol.setValue(qspi_clk_freq, 1)

    elif ( symbol.getID() == "QSPI_CLK_COMMENT" ):
        qspi_clk_sym = event["symbol"]
        if ( getQspiClkFrequency() >= qspi_clk_sym.getMax()):
            symbol.setLabel("*** QSPI Clock Frequency Is Set To Maximum " + str(getQspiClkFrequency()) + " for Master Clock Frequency At " + str(master_clk_freq))
        else:
            symbol.setLabel("*** QSPI Clock Frequency Is Set To " + str(getQspiClkFrequency()) + " for Master Clock Frequency At " + str(master_clk_freq))

def setMasterClkDependency(qspiMasterClkComment, masterClkSymbol):
    if (masterClkSymbol["value"] == False):
        qspiMasterClkComment.setVisible(True)
    else:
        qspiMasterClkComment.setVisible(False)

def instantiateComponent(qspiComponent):

    global qspiInstanceName

    qspiInstanceName = qspiComponent.createStringSymbol("QSPI_INSTANCE_NAME", None)
    qspiInstanceName.setVisible(False)
    qspiInstanceName.setDefaultValue(qspiComponent.getID().upper())
    print("Running " + qspiInstanceName.getValue())

    #Enable Clock for QSPI instance 
    Database.clearSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    qspiMenu = qspiComponent.createMenuSymbol("QSPI", None)
    qspiMenu.setLabel("Hardware Settings ")

    qspiSMM = qspiComponent.createKeyValueSetSymbol("QSPI_SMM", qspiMenu)
    qspiSMM.setLabel(qspiBitField_MR_SMM.getDescription())
    qspiSMM.setVisible(True)
    qspiSMM.setOutputMode("Key")
    qspiSMM.setDisplayMode("Description")
    qspiSMM.setSelectedKey("MEMORY",1)
    qspiSMM.setReadOnly(True)

    count = qspiValGrp_MR_SMM.getValueCount()
    for id in range(0,count):
        valueName = qspiValGrp_MR_SMM.getValueNames()[id]
        qspiSMM.addKey(valueName, qspiValGrp_MR_SMM.getValue(valueName).getValue(), qspiValGrp_MR_SMM.getValue(valueName).getDescription())

    qspiCSMODE = qspiComponent.createComboSymbol("QSPI_CSMODE", qspiMenu, qspiValGrp_MR_CSMODE.getValueNames())
    qspiCSMODE.setVisible(False)
    qspiCSMODE.setLabel(qspiBitField_MR_CSMODE.getDescription())
    qspiCSMODE.setDefaultValue("LASTXFER")

    qspiCPOL = qspiComponent.createKeyValueSetSymbol("QSPI_CPOL", qspiMenu)
    qspiCPOL.setLabel(qspiBitField_SCR_CPOL.getDescription())
    qspiCPOL.setVisible(True)
    qspiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    qspiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    qspiCPOL.setOutputMode("Key")
    qspiCPOL.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LOW",1)

    qspiCPHA = qspiComponent.createKeyValueSetSymbol("QSPI_CPHA", qspiMenu)
    qspiCPHA.setLabel(qspiBitField_SCR_CPHA.getDescription())
    qspiCPHA.setVisible(True)
    qspiCPHA.addKey("LEADING", "1", "Data is Valid on Clock Leading Edge (CPHA=0)")
    qspiCPHA.addKey("TRAILING", "1", "Data is Valid on Clock Trailing Edge (CPHA=1)")
    qspiCPHA.setOutputMode("Key")
    qspiCPHA.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LEADING",1)

    qspiSCBR = qspiComponent.createIntegerSymbol("QSPI_SCBR", qspiMenu)
    qspiSCBR.setLabel(qspiBitField_SCR_SCBR.getDescription())
    qspiSCBR.setVisible(True)
    qspiSCBR.setMin(1)
    qspiSCBR.setMax(255)
    qspiSCBR.setDefaultValue(2)

    default_qspi_clk_freq = getMasterClkFrequency() / (qspiSCBR.getValue() + 1)

    qspiClkFreq = qspiComponent.createIntegerSymbol("QSPI_CLK_FREQ", qspiMenu)
    qspiClkFreq.setLabel("QSPI Clock Frequency")
    qspiClkFreq.setVisible(False)
    qspiClkFreq.setMax(66000000)
    qspiClkFreq.setDefaultValue(default_qspi_clk_freq)
    qspiClkFreq.setDependencies(setQspiClkFrequency, ["QSPI_SCBR", "core." + qspiInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    qspiClkComment = qspiComponent.createCommentSymbol("QSPI_CLK_COMMENT", qspiMenu)
    qspiClkComment.setVisible(True)
    qspiClkComment.setLabel("*** QSPI Clock Frequency Is Set To " + str(qspiClkFreq.getValue()) +  " for Master Clock Frequency At " + str(getMasterClkFrequency()))
    qspiClkComment.setDependencies(setQspiClkFrequency, ["QSPI_CLK_FREQ"])

    qspiMasterClkComment = qspiComponent.createCommentSymbol("QSPI_MASTER_CLK_COMMENT", qspiMenu)
    qspiMasterClkComment.setVisible(False)
    qspiMasterClkComment.setLabel("WARNING!!! QSPI Peripheral Clock Is Disabled In Clock Manager")
    qspiMasterClkComment.setDependencies(setMasterClkDependency, ["core." + qspiInstanceName.getValue() + "_CLOCK_ENABLE"])

    splitICR = qspiComponent.createBooleanSymbol("HAS_SPLIT_ICR", None)
    splitICR.setVisible(False)
    splitICR.setDefaultValue(qspiReg_ICR == None)

    configName = Variables.get("__CONFIGURATION_NAME")

    qspiHeader1File = qspiComponent.createFileSymbol("QSPI_HEADER1", None)
    qspiHeader1File.setSourcePath("../peripheral/qspi_11171/templates/plib_qspi_common.h")
    qspiHeader1File.setOutputName("plib_qspi_common.h")
    qspiHeader1File.setDestPath("/peripheral/qspi/")
    qspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader1File.setType("HEADER")

    qspiHeader2File = qspiComponent.createFileSymbol("QSPI_HEADER2", None)
    qspiHeader2File.setSourcePath("../peripheral/qspi_11171/templates/plib_qspi.h.ftl")
    qspiHeader2File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + ".h")
    qspiHeader2File.setDestPath("/peripheral/qspi/")
    qspiHeader2File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader2File.setType("HEADER")
    qspiHeader2File.setMarkup(True)
    qspiHeader2File.setOverwrite(True)

    qspiSource1File = qspiComponent.createFileSymbol("QSPI_SOURCE1", None)
    qspiSource1File.setSourcePath("../peripheral/qspi_11171/templates/plib_qspi.c.ftl")
    qspiSource1File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + ".c")
    qspiSource1File.setDestPath("/peripheral/qspi/")
    qspiSource1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiSource1File.setType("SOURCE")
    qspiSource1File.setMarkup(True)
    qspiSource1File.setOverwrite(True)

    #QSPI Initialize 
    qspiSystemInitFile = qspiComponent.createFileSymbol("QSPI_INIT", None)
    qspiSystemInitFile.setType("STRING")
    qspiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    qspiSystemInitFile.setSourcePath("../peripheral/qspi_11171/templates/system/initialization.c.ftl")
    qspiSystemInitFile.setMarkup(True)

    #QSPI definitions header
    qspiSystemDefFile = qspiComponent.createFileSymbol("QSPI_DEF", None)
    qspiSystemDefFile.setType("STRING")
    qspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qspiSystemDefFile.setSourcePath("../peripheral/qspi_11171/templates/system/definitions.h.ftl")
    qspiSystemDefFile.setMarkup(True)
