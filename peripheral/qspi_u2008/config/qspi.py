# coding: utf-8
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
def calculateMax(symbol, event):
    maxBaud = event["value"]
    minBaud = event["value"] / 256

    if maxBaud > 66000000:
        maxBaud = 66000000

    symbol.setMax(maxBaud)
    symbol.setMin(minBaud)
    symbol.setValue(maxBaud, 2)

def calculateBaud(symbol, event):
    qspiFreq = Database.getSymbolValue("core", "QSPI_CLOCK_FREQUENCY")
    if event["value"] > 0:
        baud = (qspiFreq / event["value"]) - 1
        if baud < 0:
            baud = 0
        if baud > 255:
            baud = 255
    else:
        baud = 0

    if symbol.getValue() != baud:
        symbol.setValue(baud, 1)


def setFilesEnabled(symbol, event):
    symObj=event["symbol"]
    qspiHeader2File.setEnabled(symObj.getSelectedKey() == "MEMORY")
    qspiSource1File.setEnabled(symObj.getSelectedKey() == "MEMORY")
    qspiSpiHeader2File.setEnabled(symObj.getSelectedKey() == "SPI")
    qspiSpiSource1File.setEnabled(symObj.getSelectedKey() == "SPI")

def onAttachmentConnected(source, target):

    global qspiSMM
    global spiCapabilityId
    global qspiCapabilityId

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    if connectID == spiCapabilityId:
        localComponent.setCapabilityEnabled(spiCapabilityId, True)
        localComponent.setCapabilityEnabled(qspiCapabilityId, False)
        qspiSMM.setReadOnly(True)
        qspiSMM.setReadOnly(False)
        qspiSMM.setSelectedKey("SPI", 2)
    elif connectID == qspiCapabilityId:
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.setCapabilityEnabled(qspiCapabilityId, True)
        qspiSMM.setReadOnly(True)
        qspiSMM.setReadOnly(False)
        qspiSMM.setSelectedKey("MEMORY", 2)

    qspiSMM.setReadOnly(True)


def onAttachmentDisconnected(source, target):

    global qspiSMM

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    localComponent.setCapabilityEnabled(spiCapabilityId, True)
    localComponent.setCapabilityEnabled(qspiCapabilityId, True)

    qspiSMM.setReadOnly(False)

def instantiateComponent(qspiComponent):
    global qspiInstanceName
    global qspiCapabilityId
    global spiCapabilityId
    global qspiMenu
    global qspiSMM
    global qspiHeader2File
    global qspiSource1File
    global qspiSpiHeader2File
    global qspiSpiSource1File
    global qspiCPOL

    qspiInstanceName = qspiComponent.createStringSymbol("QSPI_INSTANCE_NAME", None)
    qspiInstanceName.setVisible(False)
    qspiInstanceName.setDefaultValue(qspiComponent.getID().upper())
    print("Running " + qspiInstanceName.getValue())

    qspiCapabilityId = qspiInstanceName.getValue() + "_SQI"
    spiCapabilityId = qspiInstanceName.getValue() + "_SPI"

    qspiMenu = qspiComponent.createMenuSymbol("QSPI", None)
    qspiMenu.setLabel("Hardware Settings ")

    qspiModeNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/value-group@[name="QSPI_CTRLB__MODE"]')
    qspiModeNodeValues = qspiModeNode.getChildren()

    # this symbol functions as the operating mode - differentiating between SPI and QSPI modes
    qspiSMM = qspiComponent.createKeyValueSetSymbol("QSPI_SMM", qspiMenu)
    qspiSMM.setLabel("Operating Mode")
    qspiSMM.setVisible(True)
    for i in range(0, len(qspiModeNodeValues)):
        key = qspiModeNodeValues[i].getAttribute("name")
        value = qspiModeNodeValues[i].getAttribute("value")
        description = qspiModeNodeValues[i].getAttribute("caption")
        qspiSMM.addKey(key, value, description)
    qspiSMM.setOutputMode("Key")
    qspiSMM.setDisplayMode("Description")
    qspiSMM.setDefaultValue(1)
    qspiSMM.setReadOnly(False)

    qspiCS = []
    qspiCSNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/value-group@[name="QSPI_CTRLB__CSMODE"]')
    qspiCSNodeValues = qspiCSNode.getChildren()
    for i in range(0, len(qspiCSNodeValues)):
        qspiCS.append(qspiCSNodeValues[i].getAttribute("name"))

    qspiCSMODE = qspiComponent.createComboSymbol("QSPI_CSMODE", qspiMenu, qspiCS)
    qspiCSMODE.setVisible(False)
    qspiCSMODE.setLabel("Chip Select Mode")
    qspiCSMODE.setDefaultValue("NORELOAD")

    qspiCPOL = qspiComponent.createKeyValueSetSymbol("QSPI_CPOL", qspiMenu)
    qspiCPOL.setLabel("Clock Polarity")
    qspiCPOL.setVisible(True)
    qspiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    qspiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    qspiCPOL.setOutputMode("Key")
    qspiCPOL.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LOW",1)

    qspiCPHA = qspiComponent.createKeyValueSetSymbol("QSPI_CPHA", qspiMenu)
    qspiCPHA.setLabel("Clock Phase")
    qspiCPHA.setVisible(True)
    qspiCPHA.addKey("LEADING", "1", "Data is Valid on Clock Leading Edge (CPHA=0)")
    qspiCPHA.addKey("TRAILING", "1", "Data is Valid on Clock Trailing Edge (CPHA=1)")
    qspiCPHA.setOutputMode("Key")
    qspiCPHA.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LEADING",1)

    qspiSCBR = qspiComponent.createIntegerSymbol("QSPI_SCBR", qspiMenu)
    qspiSCBR.setVisible(False)
    qspiSCBR.setDependencies(calculateBaud, ["QSPI_BAUD_RATE"])

    qspiBaud = qspiComponent.createIntegerSymbol("QSPI_BAUD_RATE", qspiMenu)
    qspiBaud.setDependencies(calculateMax, ["core.QSPI_CLOCK_FREQUENCY"])

    Database.setSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    ###################################################################################################
    ######################################### QSPI-SPI MODE ###########################################
    ###################################################################################################
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/qspi_u2008/config/qspi_spi.py")


    configName = Variables.get("__CONFIGURATION_NAME")

    qspiHeader1File = qspiComponent.createFileSymbol("QSPI_HEADER1", None)
    qspiHeader1File.setSourcePath("../peripheral/qspi_u2008/templates/plib_qspi_common.h")
    qspiHeader1File.setOutputName("plib_qspi_common.h")
    qspiHeader1File.setDestPath("/peripheral/qspi/")
    qspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader1File.setType("HEADER")

    qspiHeader2File = qspiComponent.createFileSymbol("QSPI_HEADER2", None)
    qspiHeader2File.setSourcePath("../peripheral/qspi_u2008/templates/plib_qspi.h.ftl")
    qspiHeader2File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + ".h")
    qspiHeader2File.setDestPath("/peripheral/qspi/")
    qspiHeader2File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader2File.setType("HEADER")
    qspiHeader2File.setMarkup(True)
    qspiHeader2File.setOverwrite(True)
    qspiHeader2File.setDependencies( setFilesEnabled, ["QSPI_SMM"] )
    qspiHeader2File.setEnabled(qspiSMM.getSelectedKey() == "MEMORY")

    qspiSource1File = qspiComponent.createFileSymbol("QSPI_SOURCE1", None)
    qspiSource1File.setSourcePath("../peripheral/qspi_u2008/templates/plib_qspi.c.ftl")
    qspiSource1File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + ".c")
    qspiSource1File.setDestPath("/peripheral/qspi/")
    qspiSource1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiSource1File.setType("SOURCE")
    qspiSource1File.setMarkup(True)
    qspiSource1File.setOverwrite(True)
    qspiSource1File.setDependencies( setFilesEnabled, ["QSPI_SMM"] )
    qspiSource1File.setEnabled(qspiSMM.getSelectedKey() == "MEMORY")

    # QSPI-spi mode header file
    qspiSpiHeader2File = qspiComponent.createFileSymbol("QSPISPI_HEADER2", None)
    qspiSpiHeader2File.setSourcePath("../peripheral/qspi_u2008/templates/plib_qspi_spi.h.ftl")
    qspiSpiHeader2File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + "_spi.h")
    qspiSpiHeader2File.setDestPath("/peripheral/qspi/")
    qspiSpiHeader2File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiSpiHeader2File.setType("HEADER")
    qspiSpiHeader2File.setMarkup(True)
    qspiSpiHeader2File.setOverwrite(True)
    qspiSpiHeader2File.setDependencies( setFilesEnabled, ["QSPI_SMM"] )
    qspiSpiHeader2File.setEnabled(qspiSMM.getSelectedKey() == "SPI")

    # QSPI-spi mode source file
    qspiSpiSource1File = qspiComponent.createFileSymbol("QSPISPI_SOURCE2", None)
    qspiSpiSource1File.setSourcePath("../peripheral/qspi_u2008/templates/plib_qspi_spi.c.ftl")
    qspiSpiSource1File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + "_spi.c")
    qspiSpiSource1File.setDestPath("/peripheral/qspi/")
    qspiSpiSource1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiSpiSource1File.setType("SOURCE")
    qspiSpiSource1File.setMarkup(True)
    qspiSpiSource1File.setOverwrite(True)
    qspiSpiSource1File.setDependencies( setFilesEnabled, ["QSPI_SMM"] )
    qspiSpiSource1File.setEnabled(qspiSMM.getSelectedKey() == "SPI")

    #QSPI Initialize
    qspiSystemInitFile = qspiComponent.createFileSymbol("QSPI_INIT", None)
    qspiSystemInitFile.setType("STRING")
    qspiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    qspiSystemInitFile.setSourcePath("../peripheral/qspi_u2008/templates/system/initialization.c.ftl")
    qspiSystemInitFile.setMarkup(True)

    #QSPI definitions header
    qspiSystemDefFile = qspiComponent.createFileSymbol("QSPI_DEF", None)
    qspiSystemDefFile.setType("STRING")
    qspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qspiSystemDefFile.setSourcePath("../peripheral/qspi_u2008/templates/system/definitions.h.ftl")
    qspiSystemDefFile.setMarkup(True)
