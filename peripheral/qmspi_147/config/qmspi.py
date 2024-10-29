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

def handleMessage(messageID, args):
    global qmspiInterrupt
    global qmspiMode
    global qmspiHardwareCS
    result_dict = {}

    if (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            qmspiMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            qmspiMode.setValue("SPI")

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            qmspiInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            qmspiInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            qmspiInterrupt.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if args.get("isReadOnly") != None:
            qmspiHardwareCS.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            qmspiHardwareCS.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            qmspiHardwareCS.setVisible(args["isVisible"])

    return result_dict

def onAttachmentConnected(source, target):

    global qmspiMode
    global spiCapabilityId
    global qspiCapabilityId

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

    if connectID == spiCapabilityId:
        localComponent.setCapabilityEnabled(spiCapabilityId, True)
        localComponent.setCapabilityEnabled(qspiCapabilityId, False)
        qmspiMode.setReadOnly(True)
        qmspiMode.setValue("SPI")
    elif connectID == qspiCapabilityId:
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.setCapabilityEnabled(qspiCapabilityId, True)
        qmspiMode.setReadOnly(True)
        qmspiMode.setValue("QSPI")

    qmspiMode.setReadOnly(True)


def onAttachmentDisconnected(source, target):

    global qmspiMode

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    localComponent.setCapabilityEnabled(spiCapabilityId, True)
    localComponent.setCapabilityEnabled(qspiCapabilityId, True)

    qmspiMode.setReadOnly(False)

def setQmspiClkFrequency(symbol, event):
    global qmspiInstanceName

    clock_divide = event["value"]
    if clock_divide == 0:
        clock_divide = 256
    qmspi_clk_freq = int(Database.getSymbolValue(qmspiInstanceName.getValue().lower(), "QMSPI_SRC_CLK_FREQ") / clock_divide)
    symbol.setValue(qmspi_clk_freq)

def setQMSPIInterruptData(qmspi_interrupt_name, status):
    Database.setSymbolValue("core", qmspi_interrupt_name + "_INTERRUPT_ENABLE" , status)
    Database.setSymbolValue("core", qmspi_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status)

    if status == True:
        Database.setSymbolValue("core", qmspi_interrupt_name + "_INTERRUPT_HANDLER", qmspi_interrupt_name + "_InterruptHandler")
    else:
        Database.setSymbolValue("core", qmspi_interrupt_name + "_INTERRUPT_HANDLER", qmspi_interrupt_name + "_Handler")

def setupQmspiIntHandler(symbol, event):
    global qmspiInstanceName
    global qmspiAggInterruptName

    if symbol.getID() == "QMSPI_INTERRUPT_MODE" and (event["id"] == "QMSPI_DMA_EN" or event["id"] == "QMSPI_MODE"):
        symbol.setReadOnly(event["source"].getSymbolByID("QMSPI_MODE").getValue() == "SPI" and (event["source"].getSymbolByID("QMSPI_DMA_EN").getValue() == True or event["source"].getSymbolByID("QMSPI_MODE").getReadOnly() == True))
        symbol.setValue(symbol.getReadOnly())
    else:
        interrupt_type = event["source"].getSymbolByID("QMSPI_INTERRUPT_TYPE").getSelectedKey()
        if(Database.getSymbolValue(qmspiInstanceName.getValue().lower(), "QMSPI_INTERRUPT_MODE") == True):
            if interrupt_type == "AGGREGATE":
                setQMSPIInterruptData(qmspiInstanceName.getValue(), False)
                setQMSPIInterruptData(qmspiAggInterruptName, True)
            else:
                setQMSPIInterruptData(qmspiAggInterruptName, False)
                setQMSPIInterruptData(qmspiInstanceName.getValue(), True)
        else:
            setQMSPIInterruptData(qmspiAggInterruptName, False)
            setQMSPIInterruptData(qmspiInstanceName.getValue(), False)

def nvicInterruptNameUpdate (symbol, event):
    global qmspiInstanceName
    global qmspiAggInterruptName
    if event["symbol"].getSelectedKey() == "AGGREGATE":
        symbol.setValue(qmspiAggInterruptName)
    else:
        symbol.setValue(qmspiInstanceName.getValue())

def qmspiSPIModeVisibility(symbol, event):
    if symbol.getID() == "QMSPI_HARDWARE_CS_SEL":
        qmspi_mode = event["source"].getSymbolByID("QMSPI_MODE").getValue()
        hw_cs_en = event["source"].getSymbolByID("QMSPI_HARDWARE_CS_EN").getValue()
        symbol.setVisible(qmspi_mode == "SPI" and hw_cs_en == True)
    elif symbol.getID() == "QMSPI_DESCRIPTOR_MODE_EN":
        qmspi_mode = event["source"].getSymbolByID("QMSPI_MODE").getValue()
        dma_en = event["source"].getSymbolByID("QMSPI_DMA_EN").getValue()
        symbol.setVisible(qmspi_mode == "SPI" and dma_en == True)
    else:
        symbol.setVisible(event["value"] == "SPI")

def qmspiQSPIModeVisibility(symbol, event):
    symbol.setVisible(event["value"] == "QSPI")

def qmspiQSPIModeFileGeneration(symbol, event):
    symbol.setEnabled(event["value"] == "QSPI")

def qmspiSPIModeFileGeneration(symbol, event):
    symbol.setEnabled(event["value"] == "SPI")

def instantiateComponent(qmspiComponent):
    global qmspiInstanceName
    global qmspiInstanceNum
    global qmspiAggInterruptName
    global qmspiInterrupt
    global qmspiMode
    global qspiCapabilityId
    global spiCapabilityId
    global qmspiHardwareCS

    qmspiInstanceName = qmspiComponent.createStringSymbol("QMSPI_INSTANCE_NAME", None)
    qmspiInstanceName.setVisible(False)
    qmspiInstanceName.setDefaultValue(qmspiComponent.getID().upper())
    Log.writeInfoMessage("Running " + qmspiInstanceName.getValue())

    qmspiInstanceNum = qmspiComponent.createStringSymbol("QMSPI_INSTANCE_NUM", None)
    qmspiInstanceNum.setVisible(False)
    qmspiInstanceNum.setDefaultValue(filter(str.isdigit, str(qmspiComponent.getID())))

    qspiCapabilityId = qmspiInstanceName.getValue() + "_SQI"
    spiCapabilityId = qmspiInstanceName.getValue() + "_SPI"

    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "QMSPI" + qmspiInstanceNum.getValue()})
    qmspiAggInterruptName = qmspiInstanceName.getValue() + "_GRP"

    qmspiMode = qmspiComponent.createComboSymbol("QMSPI_MODE", None, ["QSPI", "SPI"])
    qmspiMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiMode.setLabel("QMSPI Mode")
    qmspiMode.setDefaultValue("QSPI")

    qmspiCPOL = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPOL", None)
    qmspiCPOL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiCPOL.setLabel("Clock Polarity")
    qmspiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    qmspiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    qmspiCPOL.setOutputMode("Key")
    qmspiCPOL.setDisplayMode("Description")
    qmspiCPOL.setSelectedKey("LOW")

    qmspiCPHA_MOSI = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPHA_MOSI", None)
    qmspiCPHA_MOSI.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiCPHA_MOSI.setLabel("Clock phase of the Master data out")
    qmspiCPHA_MOSI.addKey("FALLING", "0", "Data changes on the falling edge of the SPI clock")
    qmspiCPHA_MOSI.addKey("RISING", "1", "Data changes on the rising edge of the SPI clock")
    qmspiCPHA_MOSI.setOutputMode("Key")
    qmspiCPHA_MOSI.setDisplayMode("Description")
    qmspiCPHA_MOSI.setSelectedKey("FALLING")
    qmspiCPHA_MOSI.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])

    qmspiCPHA_MISO = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPHA_MISO", None)
    qmspiCPHA_MISO.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiCPHA_MISO.setLabel("Clock phase of the Master data in")
    qmspiCPHA_MISO.addKey("RISING", "0", "Data is captured on the rising edge of the SPI clock")
    qmspiCPHA_MISO.addKey("FALLING", "1", "Data is captured on the falling edge of the SPI clock")
    qmspiCPHA_MISO.setOutputMode("Key")
    qmspiCPHA_MISO.setDisplayMode("Description")
    qmspiCPHA_MISO.setSelectedKey("RISING")
    qmspiCPHA_MISO.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])

    qmspiCPHA = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPHA", None)
    qmspiCPHA.setLabel("Clock Phase")
    qmspiCPHA.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiCPHA.addKey("RISING", "0", "Data is captured on the rising edge of the SPI clock")
    qmspiCPHA.addKey("FALLING", "1", "Data is captured on the falling edge of the SPI clock")
    qmspiCPHA.setOutputMode("Key")
    qmspiCPHA.setDisplayMode("Description")
    qmspiCPHA.setSelectedKey("RISING")
    qmspiCPHA.setVisible(False)
    qmspiCPHA.setDependencies(qmspiSPIModeVisibility, ["QMSPI_MODE"])

    qmspiHardwareCS = qmspiComponent.createBooleanSymbol("QMSPI_HARDWARE_CS_EN", None)
    qmspiHardwareCS.setLabel("Use Hardware Chip Select?")
    qmspiHardwareCS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiHardwareCS.setDefaultValue(False)
    qmspiHardwareCS.setVisible(False)
    qmspiHardwareCS.setDependencies(qmspiSPIModeVisibility, ["QMSPI_MODE"])

    qmspiHardwareCSSel = qmspiComponent.createKeyValueSetSymbol("QMSPI_HARDWARE_CS_SEL", qmspiHardwareCS)
    qmspiHardwareCSSel.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiHardwareCSSel.setLabel("Chip Select Line")
    qmspiHardwareCSSel.addKey("CHIP_SEL_0", "0", "Chip Select 0")
    qmspiHardwareCSSel.addKey("CHIP_SEL_1", "1", "Chip Select 1")
    qmspiHardwareCSSel.setOutputMode("Value")
    qmspiHardwareCSSel.setDisplayMode("Description")
    qmspiHardwareCSSel.setSelectedKey("CHIP_SEL_0")
    qmspiHardwareCSSel.setVisible(False)
    qmspiHardwareCSSel.setDependencies(qmspiSPIModeVisibility, ["QMSPI_MODE", "QMSPI_HARDWARE_CS_EN"])

    qmspiCLOCK_DIVIDE = qmspiComponent.createIntegerSymbol("QMSPI_CLOCK_DIVIDE", None)
    qmspiCLOCK_DIVIDE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiCLOCK_DIVIDE.setLabel("Clock Divide")
    qmspiCLOCK_DIVIDE.setMin(0)
    qmspiCLOCK_DIVIDE.setMax(255)
    qmspiCLOCK_DIVIDE.setDefaultValue(8)

    qmspiSrcClkFreq = qmspiComponent.createIntegerSymbol("QMSPI_SRC_CLK_FREQ", None)
    qmspiSrcClkFreq.setVisible(False)
    qmspiSrcClkFreq.setDefaultValue(int(ATDF.getNode('/avr-tools-device-file/variants/variant').getAttribute("speedmax")))

    clock_divide = qmspiCLOCK_DIVIDE.getValue()
    if clock_divide == 0:
        clock_divide = 256
    default_qmspi_clk_freq = int(qmspiSrcClkFreq.getValue() / clock_divide)
    qmspiClkFreq = qmspiComponent.createIntegerSymbol("QMSPI_CLK_FREQ", None)
    qmspiClkFreq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiClkFreq.setLabel("QMSPI Clock Frequency (Hz)")
    qmspiClkFreq.setMax(qmspiSrcClkFreq.getValue())
    qmspiClkFreq.setReadOnly(True)
    qmspiClkFreq.setDefaultValue(default_qmspi_clk_freq)
    qmspiClkFreq.setDependencies(setQmspiClkFrequency, ["QMSPI_CLOCK_DIVIDE"])

    qmspiHOLD_OUT_ENABLE = qmspiComponent.createBooleanSymbol("QMSPI_HOLD_OUT_ENABLE", None)
    qmspiHOLD_OUT_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiHOLD_OUT_ENABLE.setLabel("HOLD Output Enable")
    qmspiHOLD_OUT_ENABLE.setDefaultValue(False)
    qmspiHOLD_OUT_ENABLE.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])

    qmspiHOLD_OUT_VAL = qmspiComponent.createKeyValueSetSymbol("QMSPI_HOLD_OUT_VALUE", qmspiHOLD_OUT_ENABLE)
    qmspiHOLD_OUT_VAL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiHOLD_OUT_VAL.setLabel("HOLD Output Value")
    qmspiHOLD_OUT_VAL.addKey("LOW", "0", "HOLD is driven to 0")
    qmspiHOLD_OUT_VAL.addKey("HIGH", "1", "HOLD is driven to 1")
    qmspiHOLD_OUT_VAL.setOutputMode("Key")
    qmspiHOLD_OUT_VAL.setDisplayMode("Key")
    qmspiHOLD_OUT_VAL.setSelectedKey("LOW")
    qmspiHOLD_OUT_VAL.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])

    qmspiWRITE_PROTECT_OUT_ENABLE = qmspiComponent.createBooleanSymbol("QMSPI_WRITE_PROTECT_OUT_ENABLE", None)
    qmspiWRITE_PROTECT_OUT_ENABLE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiWRITE_PROTECT_OUT_ENABLE.setLabel("WRITE PROTECT Output Enable")
    qmspiWRITE_PROTECT_OUT_ENABLE.setDefaultValue(False)
    qmspiWRITE_PROTECT_OUT_ENABLE.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])


    qmspiWRITE_PROTECT_OUT_VAL = qmspiComponent.createKeyValueSetSymbol("QMSPI_WRITE_PROTECT_OUT_VALUE", qmspiWRITE_PROTECT_OUT_ENABLE)
    qmspiWRITE_PROTECT_OUT_VAL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:CTRL")
    qmspiWRITE_PROTECT_OUT_VAL.setLabel("WRITE PROTECT Output Value")
    qmspiWRITE_PROTECT_OUT_VAL.addKey("LOW", "0", "WRITE PROTECT is driven to 0")
    qmspiWRITE_PROTECT_OUT_VAL.addKey("HIGH", "1", "WRITE PROTECT is driven to 1")
    qmspiWRITE_PROTECT_OUT_VAL.setOutputMode("Key")
    qmspiWRITE_PROTECT_OUT_VAL.setDisplayMode("Key")
    qmspiWRITE_PROTECT_OUT_VAL.setSelectedKey("LOW")
    qmspiWRITE_PROTECT_OUT_VAL.setDependencies(qmspiQSPIModeVisibility, ["QMSPI_MODE"])

    qmspiNumOfDesc = qmspiComponent.createIntegerSymbol("QMSPI_NUM_OF_DESC", None)
    qmspiNumOfDesc.setVisible(False)
    qmspiNumOfDesc.setDefaultValue(int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="QMSPI"]/register-group@[name="QMSPI"]/register@[name="DESCR"]').getAttribute("count")))

    qmspiDMAEnable = qmspiComponent.createBooleanSymbol("QMSPI_DMA_EN", None)
    qmspiDMAEnable.setLabel("DMA Enable")
    qmspiDMAEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiDMAEnable.setDefaultValue(False)
    qmspiDMAEnable.setVisible(False)
    qmspiDMAEnable.setDependencies(qmspiSPIModeVisibility, ["QMSPI_MODE"])

    qmspiDMADescEnable = qmspiComponent.createBooleanSymbol("QMSPI_DESCRIPTOR_MODE_EN", qmspiDMAEnable)
    qmspiDMADescEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:MODE")
    qmspiDMADescEnable.setLabel("DMA Descriptor Enable")
    qmspiDMADescEnable.setDefaultValue(False)
    qmspiDMADescEnable.setVisible(False)
    qmspiDMADescEnable.setDependencies(qmspiSPIModeVisibility, ["QMSPI_MODE", "QMSPI_DMA_EN"])



    qmspiInterrupt = qmspiComponent.createBooleanSymbol("QMSPI_INTERRUPT_MODE", None)
    qmspiInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:IEN")
    qmspiInterrupt.setLabel("Interrupt Mode")
    qmspiInterrupt.setDefaultValue(False)
    qmspiInterrupt.setDependencies(setupQmspiIntHandler, ["QMSPI_INTERRUPT_MODE", "QMSPI_DMA_EN", "QMSPI_MODE"])

    # QMSPI Interrupt Type - Aggregate or Direct
    qmspiInterruptType = qmspiComponent.createKeyValueSetSymbol("QMSPI_INTERRUPT_TYPE", qmspiInterrupt)
    qmspiInterruptType.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:qmspi_147;register:IEN")
    qmspiInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        qmspiInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        qmspiInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    qmspiInterruptType.setDefaultValue(0)
    qmspiInterruptType.setDisplayMode("Description")
    qmspiInterruptType.setOutputMode("Key")
    qmspiInterruptType.setDependencies(setupQmspiIntHandler, ["QMSPI_INTERRUPT_TYPE"])

    interruptName = ""
    if qmspiInterruptType.getSelectedKey() == "AGGREGATE":
        interruptName = qmspiAggInterruptName
    else:
        interruptName = qmspiInstanceName.getValue()
    qmspi_NVIC_InterruptName = qmspiComponent.createStringSymbol("QMSPI_NVIC_INTERRUPT_NAME", None)
    qmspi_NVIC_InterruptName.setDefaultValue(interruptName)
    qmspi_NVIC_InterruptName.setDependencies(nvicInterruptNameUpdate, ["QMSPI_INTERRUPT_TYPE"])
    qmspi_NVIC_InterruptName.setVisible(False)

    ###################################################################################################
    ####################################### Driver Symbols ############################################
    ###################################################################################################

    #SPI Clock Phase Leading Edge Mask
    spiSym_CPHA_LE_Mask = qmspiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CPHA_LE_Mask.setDefaultValue("0x00000000")
    spiSym_CPHA_LE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CPHA_TE_Mask = qmspiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CPHA_TE_Mask.setDefaultValue("0x00000400")
    spiSym_CPHA_TE_Mask.setVisible(False)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CPOL_IL_Mask = qmspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CPOL_IL_Mask.setDefaultValue("0x00000000")
    spiSym_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CPOL_IH_Mask = qmspiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CPOL_IH_Mask.setDefaultValue("0x00000100")
    spiSym_CPOL_IH_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = qmspiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue(qmspiInstanceName.getValue() + "_SPI")
    spiSym_API_Prefix.setVisible(False)

    ###################################################################################################
    ######################################### QMSPI ###################################################
    ###################################################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    qmspiHeader1File = qmspiComponent.createFileSymbol("QMSPI_HEADER1", None)
    qmspiHeader1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi_common.h")
    qmspiHeader1File.setOutputName("plib_qmspi_common.h")
    qmspiHeader1File.setDestPath("/peripheral/qmspi/")
    qmspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiHeader1File.setType("HEADER")
    qmspiHeader1File.setEnabled(qmspiMode.getValue() == "QSPI")
    qmspiHeader1File.setDependencies(qmspiQSPIModeFileGeneration, ["QMSPI_MODE"])

    qmspiHeader2File = qmspiComponent.createFileSymbol("QMSPI_HEADER2", None)
    qmspiHeader2File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi.h.ftl")
    qmspiHeader2File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + ".h")
    qmspiHeader2File.setDestPath("/peripheral/qmspi/")
    qmspiHeader2File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiHeader2File.setType("HEADER")
    qmspiHeader2File.setMarkup(True)
    qmspiHeader2File.setOverwrite(True)
    qmspiHeader2File.setEnabled(qmspiMode.getValue() == "QSPI")
    qmspiHeader2File.setDependencies(qmspiQSPIModeFileGeneration, ["QMSPI_MODE"])

    qmspiSource1File = qmspiComponent.createFileSymbol("QMSPI_SOURCE1", None)
    qmspiSource1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi.c.ftl")
    qmspiSource1File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + ".c")
    qmspiSource1File.setDestPath("/peripheral/qmspi/")
    qmspiSource1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiSource1File.setType("SOURCE")
    qmspiSource1File.setMarkup(True)
    qmspiSource1File.setOverwrite(True)
    qmspiSource1File.setEnabled(qmspiMode.getValue() == "QSPI")
    qmspiSource1File.setDependencies(qmspiQSPIModeFileGeneration, ["QMSPI_MODE"])

    #QMSPI-SPI related files

    qmspi_spiHeader1File = qmspiComponent.createFileSymbol("QMSPI_SPI_HEADER1", None)
    qmspi_spiHeader1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi_spi_common.h.ftl")
    qmspi_spiHeader1File.setOutputName("plib_qmspi_spi_common.h")
    qmspi_spiHeader1File.setDestPath("/peripheral/qmspi/")
    qmspi_spiHeader1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspi_spiHeader1File.setType("HEADER")
    qmspi_spiHeader1File.setMarkup(True)
    qmspi_spiHeader1File.setEnabled(qmspiMode.getValue() == "SPI")
    qmspi_spiHeader1File.setDependencies(qmspiSPIModeFileGeneration, ["QMSPI_MODE"])

    qmspi_spiHeader2File = qmspiComponent.createFileSymbol("QMSPI_SPI_HEADER2", None)
    qmspi_spiHeader2File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi_spi.h.ftl")
    qmspi_spiHeader2File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + "_spi.h")
    qmspi_spiHeader2File.setDestPath("/peripheral/qmspi/")
    qmspi_spiHeader2File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspi_spiHeader2File.setType("HEADER")
    qmspi_spiHeader2File.setMarkup(True)
    qmspi_spiHeader2File.setOverwrite(True)
    qmspi_spiHeader2File.setEnabled(qmspiMode.getValue() == "SPI")
    qmspi_spiHeader2File.setDependencies(qmspiSPIModeFileGeneration, ["QMSPI_MODE"])

    qmspi_spiSource1File = qmspiComponent.createFileSymbol("QMSPI_SPI_SOURCE1", None)
    qmspi_spiSource1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi_spi.c.ftl")
    qmspi_spiSource1File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + "_spi.c")
    qmspi_spiSource1File.setDestPath("/peripheral/qmspi/")
    qmspi_spiSource1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspi_spiSource1File.setType("SOURCE")
    qmspi_spiSource1File.setMarkup(True)
    qmspi_spiSource1File.setOverwrite(True)
    qmspi_spiSource1File.setEnabled(qmspiMode.getValue() == "SPI")
    qmspi_spiSource1File.setDependencies(qmspiSPIModeFileGeneration, ["QMSPI_MODE"])

    #QMSPI Initialize
    qmspiSystemInitFile = qmspiComponent.createFileSymbol("QMSPI_INIT", None)
    qmspiSystemInitFile.setType("STRING")
    qmspiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    qmspiSystemInitFile.setSourcePath("../peripheral/qmspi_147/templates/system/initialization.c.ftl")
    qmspiSystemInitFile.setMarkup(True)

    #QMSPI definitions header
    qmspiSystemDefFile = qmspiComponent.createFileSymbol("QMSPI_DEF", None)
    qmspiSystemDefFile.setType("STRING")
    qmspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qmspiSystemDefFile.setSourcePath("../peripheral/qmspi_147/templates/system/definitions.h.ftl")
    qmspiSystemDefFile.setMarkup(True)
