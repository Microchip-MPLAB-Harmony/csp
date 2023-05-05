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

def instantiateComponent(qmspiComponent):
    global qmspiInstanceName
    global qmspiInstanceNum
    global qmspiAggInterruptName

    qmspiInstanceName = qmspiComponent.createStringSymbol("QMSPI_INSTANCE_NAME", None)
    qmspiInstanceName.setVisible(False)
    qmspiInstanceName.setDefaultValue(qmspiComponent.getID().upper())
    Log.writeInfoMessage("Running " + qmspiInstanceName.getValue())

    qmspiInstanceNum = qmspiComponent.createStringSymbol("QMSPI_INSTANCE_NUM", None)
    qmspiInstanceNum.setVisible(False)
    qmspiInstanceNum.setDefaultValue(filter(str.isdigit, str(qmspiComponent.getID())))

    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "QMSPI" + qmspiInstanceNum.getValue()})
    qmspiAggInterruptName = qmspiInstanceName.getValue() + "_GRP"

    qmspiCPOL = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPOL", None)
    qmspiCPOL.setLabel("Clock Polarity")
    qmspiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    qmspiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    qmspiCPOL.setOutputMode("Key")
    qmspiCPOL.setDisplayMode("Description")
    qmspiCPOL.setSelectedKey("LOW")

    qmspiCPHA_MOSI = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPHA_MOSI", None)
    qmspiCPHA_MOSI.setLabel("Clock phase of the Master data out")
    qmspiCPHA_MOSI.addKey("FALLING", "0", "Data changes on the falling edge of the SPI clock")
    qmspiCPHA_MOSI.addKey("RISING", "1", "Data changes on the rising edge of the SPI clock")
    qmspiCPHA_MOSI.setOutputMode("Key")
    qmspiCPHA_MOSI.setDisplayMode("Description")
    qmspiCPHA_MOSI.setSelectedKey("FALLING")

    qmspiCPHA_MISO = qmspiComponent.createKeyValueSetSymbol("QMSPI_CPHA_MISO", None)
    qmspiCPHA_MISO.setLabel("Clock phase of the Master data in")
    qmspiCPHA_MISO.addKey("RISING", "0", "Data are captured on the rising edge of the SPI clock")
    qmspiCPHA_MISO.addKey("FALLING", "1", "Data are captured on the falling edge of the SPI clock")
    qmspiCPHA_MISO.setOutputMode("Key")
    qmspiCPHA_MISO.setDisplayMode("Description")
    qmspiCPHA_MISO.setSelectedKey("RISING")

    qmspiCLOCK_DIVIDE = qmspiComponent.createIntegerSymbol("QMSPI_CLOCK_DIVIDE", None)
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
    qmspiClkFreq.setLabel("QMSPI Clock Frequency (Hz)")
    qmspiClkFreq.setMax(qmspiSrcClkFreq.getValue())
    qmspiClkFreq.setReadOnly(True)
    qmspiClkFreq.setDefaultValue(default_qmspi_clk_freq)
    qmspiClkFreq.setDependencies(setQmspiClkFrequency, ["QMSPI_CLOCK_DIVIDE"])

    qmspiHOLD_OUT_ENABLE = qmspiComponent.createBooleanSymbol("QMSPI_HOLD_OUT_ENABLE", None)
    qmspiHOLD_OUT_ENABLE.setLabel("HOLD Output Enable")
    qmspiHOLD_OUT_ENABLE.setDefaultValue(False)

    qmspiHOLD_OUT_VAL = qmspiComponent.createKeyValueSetSymbol("QMSPI_HOLD_OUT_VALUE", qmspiHOLD_OUT_ENABLE)
    qmspiHOLD_OUT_VAL.setLabel("HOLD Output Value")
    qmspiHOLD_OUT_VAL.addKey("LOW", "0", "HOLD is driven to 0")
    qmspiHOLD_OUT_VAL.addKey("HIGH", "1", "HOLD is driven to 1")
    qmspiHOLD_OUT_VAL.setOutputMode("Key")
    qmspiHOLD_OUT_VAL.setDisplayMode("Key")
    qmspiHOLD_OUT_VAL.setSelectedKey("LOW")

    qmspiWRITE_PROTECT_OUT_ENABLE = qmspiComponent.createBooleanSymbol("QMSPI_WRITE_PROTECT_OUT_ENABLE", None)
    qmspiWRITE_PROTECT_OUT_ENABLE.setLabel("WRITE PROTECT Output Enable")
    qmspiWRITE_PROTECT_OUT_ENABLE.setDefaultValue(False)

    qmspiWRITE_PROTECT_OUT_VAL = qmspiComponent.createKeyValueSetSymbol("QMSPI_WRITE_PROTECT_OUT_VALUE", qmspiWRITE_PROTECT_OUT_ENABLE)
    qmspiWRITE_PROTECT_OUT_VAL.setLabel("WRITE PROTECT Output Value")
    qmspiWRITE_PROTECT_OUT_VAL.addKey("LOW", "0", "WRITE PROTECT is driven to 0")
    qmspiWRITE_PROTECT_OUT_VAL.addKey("HIGH", "1", "WRITE PROTECT is driven to 1")
    qmspiWRITE_PROTECT_OUT_VAL.setOutputMode("Key")
    qmspiWRITE_PROTECT_OUT_VAL.setDisplayMode("Key")
    qmspiWRITE_PROTECT_OUT_VAL.setSelectedKey("LOW")

    qmspiNumOfDesc = qmspiComponent.createIntegerSymbol("QMSPI_NUM_OF_DESC", None)
    qmspiNumOfDesc.setVisible(False)
    qmspiNumOfDesc.setDefaultValue(int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="QMSPI"]/register-group@[name="QMSPI"]/register@[name="DESCR"]').getAttribute("count")))

    qmspiInterrupt = qmspiComponent.createBooleanSymbol("QMSPI_INTERRUPT_MODE", None)
    qmspiInterrupt.setLabel("Interrupt Mode")
    qmspiInterrupt.setDefaultValue(False)
    qmspiInterrupt.setDependencies(setupQmspiIntHandler, ["QMSPI_INTERRUPT_MODE"])

    # QMSPI Interrupt Type - Aggregate or Direct
    qmspiInterruptType = qmspiComponent.createKeyValueSetSymbol("QMSPI_INTERRUPT_TYPE", qmspiInterrupt)
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
    ######################################### QMSPI ###################################################
    ###################################################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    qmspiHeader1File = qmspiComponent.createFileSymbol("QMSPI_HEADER1", None)
    qmspiHeader1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi_common.h")
    qmspiHeader1File.setOutputName("plib_qmspi_common.h")
    qmspiHeader1File.setDestPath("/peripheral/qmspi/")
    qmspiHeader1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiHeader1File.setType("HEADER")

    qmspiHeader2File = qmspiComponent.createFileSymbol("QMSPI_HEADER2", None)
    qmspiHeader2File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi.h.ftl")
    qmspiHeader2File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + ".h")
    qmspiHeader2File.setDestPath("/peripheral/qmspi/")
    qmspiHeader2File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiHeader2File.setType("HEADER")
    qmspiHeader2File.setMarkup(True)
    qmspiHeader2File.setOverwrite(True)

    qmspiSource1File = qmspiComponent.createFileSymbol("QMSPI_SOURCE1", None)
    qmspiSource1File.setSourcePath("../peripheral/qmspi_147/templates/plib_qmspi.c.ftl")
    qmspiSource1File.setOutputName("plib_" + qmspiInstanceName.getValue().lower() + ".c")
    qmspiSource1File.setDestPath("/peripheral/qmspi/")
    qmspiSource1File.setProjectPath("config/" + configName + "/peripheral/qmspi/")
    qmspiSource1File.setType("SOURCE")
    qmspiSource1File.setMarkup(True)
    qmspiSource1File.setOverwrite(True)

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
