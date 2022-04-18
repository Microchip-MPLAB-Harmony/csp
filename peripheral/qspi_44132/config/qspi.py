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

def setFilesEnabled(symbol, event):
    symObj=event["symbol"]
    qspiHeader2File.setEnabled(symObj.getSelectedKey() == "MEMORY")
    qspiSource1File.setEnabled(symObj.getSelectedKey() == "MEMORY")
    qspiSpiHeader2File.setEnabled(symObj.getSelectedKey() == "SPI")
    qspiSpiSource1File.setEnabled(symObj.getSelectedKey() == "SPI")

def setQspiClkFrequency(symbol, event):
    if ( symbol.getID() == "QSPI_CLK_FREQ" ):
        qspi_clk_freq = Database.getSymbolValue("core", qspiInstanceName.getValue() + "_GCLK_FREQUENCY")

        if ( qspi_clk_freq > symbol.getMax()):
            qspi_clk_freq = symbol.getMax()

        symbol.setValue(qspi_clk_freq)
    elif ( symbol.getID() == "QSPI_CLK_COMMENT" ):
        qspiCoreClockFreq = Database.getSymbolValue(qspiInstanceName.getValue().lower(), "QSPI_CLK_FREQ")
        qspi_clk_sym = event["symbol"]
        if qspiCoreClockFreq == 0:
            symbol.setLabel("*** WARNING!!! " + qspiInstanceName.getValue() + " Core Clock Frequency Is Set To 0 MHz. Configure " + qspiInstanceName.getValue() + " GCLK Frequency In Clock Manager")
        elif ( qspiCoreClockFreq >= qspi_clk_sym.getMax()):
            symbol.setLabel("*** " + qspiInstanceName.getValue() + " Core Clock Frequency Is Set To Maximum " + str(qspiCoreClockFreq/1e6) + " MHz")
        else:
            symbol.setLabel("*** " + qspiInstanceName.getValue() + " Core Clock Frequency Is Set To " + str(qspiCoreClockFreq/1e6) + " MHz")

def setMasterClkDependency(qspiMasterClkComment, masterClkSymbol):
    if (masterClkSymbol["value"] == False):
        qspiMasterClkComment.setVisible(True)
    else:
        qspiMasterClkComment.setVisible(False)

def setQspiClkdiv(symbol, event):
    if ((event["value"]/1e6) / 25) > 0:
        symbol.setValue((event["value"] / 25) - 1)
    else:
        symbol.setValue(0)

def setQspiDllRange(symbol, event):
    if event["value"] > 100000000:
        symbol.setValue(True)
    else:
        symbol.setValue(False)

def setupQspiIntSymbolAndIntHandler(symbol, event):
    global qspiSyminterruptVector
    global qspiSyminterruptHandler
    global qspiSyminterruptHandlerLock

    if(event["symbol"].getSelectedKey() == "SPI"):
        Database.setSymbolValue("core", qspiSyminterruptVector, True)
        Database.setSymbolValue("core", qspiSyminterruptHandler, qspiInstanceName.getValue() + "_InterruptHandler")
        Database.setSymbolValue("core", qspiSyminterruptHandlerLock, True)
    else:
        Database.setSymbolValue("core", qspiSyminterruptVector, False)
        Database.setSymbolValue("core", qspiSyminterruptHandler, qspiInstanceName.getValue() + "_Handler")
        Database.setSymbolValue("core", qspiSyminterruptHandlerLock, False)

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
        qspiSMM.setSelectedKey("SPI")
    elif connectID == qspiCapabilityId:
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.setCapabilityEnabled(qspiCapabilityId, True)
        qspiSMM.setReadOnly(True)
        qspiSMM.setReadOnly(False)
        qspiSMM.setSelectedKey("MEMORY")

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
    global qspiSyminterruptVector
    global qspiSyminterruptHandler
    global qspiSyminterruptHandlerLock

    qspiInstanceName = qspiComponent.createStringSymbol("QSPI_INSTANCE_NAME", None)
    qspiInstanceName.setVisible(False)
    qspiInstanceName.setDefaultValue(qspiComponent.getID().upper())
    Log.writeInfoMessage("Running " + qspiInstanceName.getValue())

    qspiInstanceNum = qspiComponent.createStringSymbol("QSPI_INSTANCE_NUM", None)
    qspiInstanceNum.setVisible(False)
    qspiInstanceNum.setDefaultValue(filter(str.isdigit,str(qspiComponent.getID())))

    qspiSyminterruptVector = qspiInstanceName.getValue() + "_INTERRUPT_ENABLE"
    qspiSyminterruptHandler = qspiInstanceName.getValue() + "_INTERRUPT_HANDLER"
    qspiSyminterruptHandlerLock = qspiInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    qspiCapabilityId = qspiInstanceName.getValue() + "_SQI"
    spiCapabilityId = qspiInstanceName.getValue() + "_SPI"

    #Enable Clock for QSPI instance
    Database.clearSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", qspiInstanceName.getValue() + "_CLOCK_ENABLE", True)

    qspiMenu = qspiComponent.createMenuSymbol("QSPI", None)
    qspiMenu.setLabel("Hardware Settings ")

    # this symbol functions as the operating mode - differentiating between SPI and QSPI modes
    qspiSMM = qspiComponent.createKeyValueSetSymbol("QSPI_SMM", qspiMenu)
    qspiSMM.setLabel(qspiBitField_MR_SMM.getDescription())
    qspiSMM.setVisible(True)
    qspiSMM.setOutputMode("Key")
    qspiSMM.setDisplayMode("Description")
    qspiSMM.setReadOnly(False)
    qspiSMM.setDefaultValue(0)

    count = qspiValGrp_MR_SMM.getValueCount()
    for id in range(0,count):
        valueName = qspiValGrp_MR_SMM.getValueNames()[id]
        qspiSMM.addKey(valueName, qspiValGrp_MR_SMM.getValue(valueName).getValue(), qspiValGrp_MR_SMM.getValue(valueName).getDescription())
    qspiSMM.setDependencies(setupQspiIntSymbolAndIntHandler, ["QSPI_SMM"])

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
    qspiCPOL.setSelectedKey("LOW")

    qspiCPHA = qspiComponent.createKeyValueSetSymbol("QSPI_CPHA", qspiMenu)
    qspiCPHA.setLabel(qspiBitField_SCR_CPHA.getDescription())
    qspiCPHA.setVisible(True)
    qspiCPHA.addKey("LEADING", "1", "Data is Valid on Clock Leading Edge (CPHA=0)")
    qspiCPHA.addKey("TRAILING", "1", "Data is Valid on Clock Trailing Edge (CPHA=1)")
    qspiCPHA.setOutputMode("Key")
    qspiCPHA.setDisplayMode("Description")
    qspiCPOL.setSelectedKey("LEADING")

    qspiClkFreq = qspiComponent.createIntegerSymbol("QSPI_CLK_FREQ", qspiMenu)
    qspiClkFreq.setLabel("QSPI Core Clock Frequency")
    qspiClkFreq.setVisible(False)
    qspiClkFreq.setMax(200000000)
    qspiClkFreq.setDefaultValue(Database.getSymbolValue("core", qspiInstanceName.getValue() + "_GCLK_FREQUENCY"))
    qspiClkFreq.setDependencies(setQspiClkFrequency, ["core." + qspiInstanceName.getValue() + "_GCLK_FREQUENCY"])

    qspiClkComment = qspiComponent.createCommentSymbol("QSPI_CLK_COMMENT", qspiMenu)
    qspiClkComment.setVisible(True)
    if qspiClkFreq.getValue() == 0:
        qspiClkComment.setLabel("*** WARNING!!! " + qspiInstanceName.getValue() + " Core Clock Frequency Is Set To 0 MHz. Configure " + qspiInstanceName.getValue() + " GCLK Frequency In Clock Manager")
    else:
        qspiClkComment.setLabel("*** " + qspiInstanceName.getValue() + " Core Clock Frequency Is Set To " + str(qspiClkFreq.getValue()/1e6) +  " MHz")
    qspiClkComment.setDependencies(setQspiClkFrequency, ["QSPI_CLK_FREQ"])

    qspiMasterClkComment = qspiComponent.createCommentSymbol("QSPI_MASTER_CLK_COMMENT", qspiMenu)
    qspiMasterClkComment.setVisible(False)
    qspiMasterClkComment.setLabel("WARNING!!! QSPI Peripheral Clock Is Disabled In Clock Manager")
    qspiMasterClkComment.setDependencies(setMasterClkDependency, ["core." + qspiInstanceName.getValue() + "_CLOCK_ENABLE"])

    if ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/register-group@[name="QSPI"]/register@[name="QSPI_PCALCFG"]/bitfield@[name="CLKDIV"]') != None:
        qspiPcalcfgClkdiv = qspiComponent.createIntegerSymbol("QSPI_PCALCFG_CLKDIV", qspiMenu)
        qspiPcalcfgClkdiv.setLabel("Calibration Clock Division")
        qspiPcalcfgClkdiv.setVisible(False)
        qspiPcalcfgClkdiv.setDefaultValue(7)
        qspiPcalcfgClkdiv.setDependencies(setQspiClkdiv, ["core." + qspiInstanceName.getValue() + "_CLOCK_FREQUENCY"])

        qspiDllcfgRange = qspiComponent.createBooleanSymbol("QSPI_DLLCFG_RANGE", qspiMenu)
        qspiDllcfgRange.setLabel("DLL Range")
        qspiDllcfgRange.setVisible(False)
        qspiDllcfgRange.setDefaultValue((qspiClkFreq.getValue() > 100000000))
        qspiDllcfgRange.setDependencies(setQspiDllRange, ["QSPI_CLK_FREQ"])

    qspiMemAddr = qspiComponent.createStringSymbol("QSPI_MEM_ADDR", None)
    qspiMemAddr.setVisible(False)
    qspiMemoryAddress = "QSPIMEM" + qspiInstanceNum.getValue() + "_ADDR"
    if ATDF.getNode('/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name="QSPI_MEM"]') != None:
        qspiMemoryAddress = "QSPI_MEM_ADDR"
    qspiMemAddr.setDefaultValue(qspiMemoryAddress)

    if ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/value-group@[name="QSPI_IFR__PROTTYP"]/value@[name="OCTAFLASH"]') != None:
        qspiIfrOctaFlash = qspiComponent.createBooleanSymbol("QSPI_IFR_OCTAFLASH", None)
        qspiIfrOctaFlash.setDefaultValue(True)
        qspiIfrOctaFlash.setVisible(False)

    if ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/register-group@[name="QSPI"]/register@[name="QSPI_IFR"]/bitfield@[name="END"]') != None:
        qspiIfrEndian = qspiComponent.createBooleanSymbol("QSPI_IFR_END", None)
        qspiIfrEndian.setDefaultValue(True)
        qspiIfrEndian.setVisible(False)

    if ATDF.getNode('/avr-tools-device-file/modules/module@[name="QSPI"]/register-group@[name="QSPI"]/register@[name="QSPI_IFR"]/bitfield@[name="HFWBEN"]') != None:
        qspiIfrHfwben = qspiComponent.createBooleanSymbol("QSPI_IFR_HFWBEN", None)
        qspiIfrHfwben.setDefaultValue(True)
        qspiIfrHfwben.setVisible(False)

    ###################################################################################################
    ######################################### QSPI-SPI MODE ###########################################
    ###################################################################################################
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/qspi_44132/config/qspi_spi.py")

    configName = Variables.get("__CONFIGURATION_NAME")

    qspiHeader1File = qspiComponent.createFileSymbol("QSPI_HEADER1", None)
    qspiHeader1File.setSourcePath("../peripheral/qspi_44132/templates/plib_qspi_common.h.ftl")
    qspiHeader1File.setOutputName("plib_qspi_common.h")
    qspiHeader1File.setDestPath("/peripheral/qspi/")
    qspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader1File.setType("HEADER")
    qspiHeader1File.setMarkup(True)

    qspiHeader2File = qspiComponent.createFileSymbol("QSPI_HEADER2", None)
    qspiHeader2File.setSourcePath("../peripheral/qspi_44132/templates/plib_qspi.h.ftl")
    qspiHeader2File.setOutputName("plib_" + qspiInstanceName.getValue().lower() + ".h")
    qspiHeader2File.setDestPath("/peripheral/qspi/")
    qspiHeader2File.setProjectPath("config/" + configName + "/peripheral/qspi/")
    qspiHeader2File.setType("HEADER")
    qspiHeader2File.setMarkup(True)
    qspiHeader2File.setOverwrite(True)
    qspiHeader2File.setDependencies( setFilesEnabled, ["QSPI_SMM"] )
    qspiHeader2File.setEnabled(qspiSMM.getSelectedKey() == "MEMORY")

    qspiSource1File = qspiComponent.createFileSymbol("QSPI_SOURCE1", None)
    qspiSource1File.setSourcePath("../peripheral/qspi_44132/templates/plib_qspi.c.ftl")
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
    qspiSpiHeader2File.setSourcePath("../peripheral/qspi_44132/templates/plib_qspi_spi.h.ftl")
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
    qspiSpiSource1File.setSourcePath("../peripheral/qspi_44132/templates/plib_qspi_spi.c.ftl")
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
    qspiSystemInitFile.setSourcePath("../peripheral/qspi_44132/templates/system/initialization.c.ftl")
    qspiSystemInitFile.setMarkup(True)

    #QSPI definitions header
    qspiSystemDefFile = qspiComponent.createFileSymbol("QSPI_DEF", None)
    qspiSystemDefFile.setType("STRING")
    qspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qspiSystemDefFile.setSourcePath("../peripheral/qspi_44132/templates/system/definitions.h.ftl")
    qspiSystemDefFile.setMarkup(True)
