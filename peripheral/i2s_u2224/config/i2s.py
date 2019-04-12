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

def instantiateComponent(i2sComponent):
    i2sInstanceName = i2sComponent.createStringSymbol("I2S_INSTANCE_NAME", None)
    i2sInstanceName.setVisible(False)
    i2sInstanceName.setDefaultValue(i2sComponent.getID().upper())
    Log.writeInfoMessage("Running " + i2sInstanceName.getValue())

    i2sDMA = i2sComponent.createBooleanSymbol("I2S_DMA_MODE", None)
    i2sDMA.setLabel("DMA Mode")
    i2sDMA.setDefaultValue(True)
    i2sDMA.setReadOnly(True)

    i2sInterrupt = i2sComponent.createBooleanSymbol("I2S_INTERRUPT_MODE", None)
    i2sInterrupt.setLabel("Interrupt Mode")
    i2sInterrupt.setDefaultValue(True)
    i2sInterrupt.setReadOnly(True)

# Clock Control
    i2sRegisters = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2S\"]/register-group@[name=\"I2S\"]")
    i2sRegistersNames = []
    i2sRegistersNames = i2sRegisters.getChildren()
    for index in range(len(i2sRegistersNames)):
        i2sRegistersName = i2sRegistersNames[index].getAttribute("name")
        if i2sRegistersName == "CLKCTRL":
            i2sRegistersCount = int(i2sRegistersNames[index].getAttribute("count"))

            i2sNumGenericClks = i2sComponent.createIntegerSymbol("I2S_NUM_GENERIC_CLOCKS", None)
            i2sNumGenericClks.setVisible(False)
            i2sNumGenericClks.setDefaultValue(i2sRegistersCount)

            for clkctrl in range(0,i2sRegistersCount):
                i2sCtrlCKEN = i2sComponent.createBooleanSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_ENABLE", None)
                i2sCtrlCKEN.setLabel("Clock Unit " + str(clkctrl) + " Enable")
                i2sCtrlCKEN.setDefaultValue(clkctrl==0)

                i2sClkMODE = i2sComponent.createKeyValueSetSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_CLKMODE", i2sCtrlCKEN)
                i2sClkMODE.setLabel("Master/Slave Mode")
                i2sClkMODE.addKey("MASTER", "0", "Master")
                i2sClkMODE.addKey("SLAVE", "1", "Slave")
                i2sClkMODE.setDisplayMode("Description")
                i2sClkMODE.setOutputMode("Value")
                i2sClkMODE.setDefaultValue(0)

                i2sClkMCKOUTDIV = i2sComponent.createIntegerSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_MCKOUTDIV", i2sCtrlCKEN)
                # Generic clock is divided by (MCKOUTDIV+1) to obtain Master Clock n output
                i2sClkMCKOUTDIV.setLabel("Master Clock Ouput Division Factor")
                i2sClkMCKOUTDIV.setDefaultValue(3)

                i2sClkMCKDIV = i2sComponent.createIntegerSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_MCKDIV", i2sCtrlCKEN)
                # Master Clock n is divided by (MCKDIV+1) to obtain Serial Clock n
                i2sClkMCKDIV.setLabel("Master Clock Division Factor")
                i2sClkMCKDIV.setDefaultValue(8)

                i2sClkFSOUTINV = i2sComponent.createKeyValueSetSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_FSOUTINV", i2sCtrlCKEN)
                i2sClkFSOUTINV.setLabel("Frame Sync Output Invert")
                i2sClkFSOUTINV.addKey("0", "0", "FS output without inversion")
                i2sClkFSOUTINV.addKey("1", "1", "FS inverted before being output")
                i2sClkFSOUTINV.setDisplayMode("Description")
                i2sClkFSOUTINV.setOutputMode("Value")
                i2sClkFSOUTINV.setDefaultValue(0)

                i2sClkFSINV = i2sComponent.createKeyValueSetSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_FSINV", i2sCtrlCKEN)
                i2sClkFSINV.setLabel("Frame Sync Output Invert")
                i2sClkFSINV.addKey("0", "0", "FS used without inversion")
                i2sClkFSINV.addKey("1", "1", "FS inverted before being used")
                i2sClkFSINV.setDisplayMode("Description")
                i2sClkFSINV.setOutputMode("Value")
                i2sClkFSINV.setDefaultValue(0)

                i2sClkBITDELAY = i2sComponent.createKeyValueSetSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_BITDELAY", i2sCtrlCKEN)
                i2sClkBITDELAY.setLabel("Data Delay from Frame Sync")
                i2sClkBITDELAY.addKey("LJ/RJ", "0", "Left/right justified (0 delay)")
                i2sClkBITDELAY.addKey("I2S", "1", "I2S (1 bit delay)")
                i2sClkBITDELAY.setDisplayMode("Description")
                i2sClkBITDELAY.setOutputMode("Value")
                i2sClkBITDELAY.setDefaultValue(1)

                i2sClkSLOTSIZE = i2sComponent.createKeyValueSetSymbol("I2S_CLKCTRL_" + str(clkctrl) + "_SLOTSIZE", i2sCtrlCKEN)
                i2sClkSLOTSIZE.setLabel("Slot Size")
                # note: index values 1 and 3 (16 and 32 bits) referenced in drv_i2s.py
                i2sClkSLOTSIZEnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2S\"]/value-group@[name=\"I2S_CLKCTRL__SLOTSIZE\"]")
                i2sClkSLOTSIZEvalues = []
                i2sClkSLOTSIZEvalues = i2sClkSLOTSIZEnode.getChildren()
                i2sClkSLOTSIZEdefault = 0
                for index in range(len(i2sClkSLOTSIZEvalues)):
                    i2sClkSLOTSIZEcaption = i2sClkSLOTSIZEvalues[index].getAttribute("caption")
                    i2sClkSLOTSIZEname = i2sClkSLOTSIZEvalues[index].getAttribute("name")
                    i2sClkSLOTSIZEvalue = i2sClkSLOTSIZEvalues[index].getAttribute("value")
                    i2sClkSLOTSIZE.addKey(i2sClkSLOTSIZEname, i2sClkSLOTSIZEvalue, i2sClkSLOTSIZEcaption)
                    if (i2sClkSLOTSIZEdefault == 0) and ("16" in i2sClkSLOTSIZEname):
                        i2sClkSLOTSIZEdefault = index
                i2sClkSLOTSIZE.setDisplayMode("Description")
                i2sClkSLOTSIZE.setOutputMode("Value")
                i2sClkSLOTSIZE.setDefaultValue(i2sClkSLOTSIZEdefault)

# TX Serializer
    i2sTxSerializerEN = i2sComponent.createBooleanSymbol("I2S_TX_SERIALIZER_ENABLE", None)
    i2sTxSerializerEN.setLabel("TX Serializer Enable")
    i2sTxSerializerEN.setDefaultValue(True)

    i2sTxMONO = i2sComponent.createKeyValueSetSymbol("I2S_TXCTRL_MONO", i2sTxSerializerEN)
    i2sTxMONO.setLabel("Stereo/Mono")
    i2sTxMONO.addKey("STEREO", "0", "Stereo")
    i2sTxMONO.addKey("MONO", "1", "Mono (left dup'ed to right)")
    i2sTxMONO.setDisplayMode("Description")
    i2sTxMONO.setOutputMode("Value")
    i2sTxMONO.setDefaultValue(0)

    i2sTxWORDADJ = i2sComponent.createKeyValueSetSymbol("I2S_TXCTRL_WORDADJ", i2sTxSerializerEN)
    i2sTxWORDADJ.setLabel("Data Word Formatting Adjust")
    i2sTxWORDADJ.addKey("I2S", "0", "Right justified")
    i2sTxWORDADJ.addKey("LJ", "1", "Left justified")
    i2sTxWORDADJ.setDisplayMode("Description")
    i2sTxWORDADJ.setOutputMode("Value")
    i2sTxWORDADJ.setDefaultValue(1)

    i2sTxDATASIZE = i2sComponent.createKeyValueSetSymbol("I2S_TXCTRL_DATASIZE", i2sTxSerializerEN)
    i2sTxDATASIZE.setLabel("Data Word Size")
    # note: index values 0 and 4 (32 and 16 bits) are referenced in drv_i2s.py
    i2sTxDATASIZEnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2S\"]/value-group@[name=\"I2S_TXCTRL__DATASIZE\"]")
    i2sTxDATASIZEvalues = []
    i2sTxDATASIZEvalues = i2sTxDATASIZEnode.getChildren()
    i2sTxDATASIZEdefault = 0
    for index in range(len(i2sTxDATASIZEvalues)):
        i2sTxDATASIZEcaption = i2sTxDATASIZEvalues[index].getAttribute("caption")
        i2sTxDATASIZEname = i2sTxDATASIZEvalues[index].getAttribute("name")
        i2sTxDATASIZEvalue = i2sTxDATASIZEvalues[index].getAttribute("value")
        i2sTxDATASIZE.addKey(i2sTxDATASIZEname, i2sTxDATASIZEvalue, i2sTxDATASIZEcaption)
        if (i2sTxDATASIZEdefault == 0) and ("16" in i2sTxDATASIZEname):
            i2sTxDATASIZEdefault = index
    i2sTxDATASIZE.setDisplayMode("Description")
    i2sTxDATASIZE.setOutputMode("Value")
    i2sTxDATASIZE.setDefaultValue(i2sTxDATASIZEdefault)

    i2sTxSLOTADJ = i2sComponent.createKeyValueSetSymbol("I2S_TXCTRL_SLOTADJ", i2sTxSerializerEN)
    i2sTxSLOTADJ.setLabel("Data Slot Formatting Adjust")
    i2sTxSLOTADJ.addKey("I2S", "0", "Right justified")
    i2sTxSLOTADJ.addKey("LJ", "1", "Left justified")
    i2sTxSLOTADJ.setDisplayMode("Description")
    i2sTxSLOTADJ.setOutputMode("Value")
    i2sTxSLOTADJ.setDefaultValue(1)

    i2sTxCLKSEL = i2sComponent.createKeyValueSetSymbol("I2S_TXCTRL_CLKSEL", i2sTxSerializerEN)
    i2sTxCLKSEL.setLabel("Clock Unit Selection")
    i2sTxCLKSEL.addKey("0", "0", "Use Clock Unit 0")
    i2sTxCLKSEL.addKey("1", "1", "Use Clock Unit 1")
    i2sTxCLKSEL.setDisplayMode("Description")
    i2sTxCLKSEL.setOutputMode("Value")
    i2sTxCLKSEL.setDefaultValue(0)

# RX Serializer
    i2sRxSerializerEN = i2sComponent.createBooleanSymbol("I2S_RX_SERIALIZER_ENABLE", None)
    i2sRxSerializerEN.setLabel("RX Serializer Enable")
    i2sRxSerializerEN.setDefaultValue(True)

    i2sRxMONO = i2sComponent.createKeyValueSetSymbol("I2S_RXCTRL_MONO", i2sRxSerializerEN)
    i2sRxMONO.setLabel("Stereo/Mono")
    i2sRxMONO.addKey("STEREO", "0", "Stereo")
    i2sRxMONO.addKey("MONO", "1", "Mono (left dup'ed to right)")
    i2sRxMONO.setDisplayMode("Description")
    i2sRxMONO.setOutputMode("Value")
    i2sRxMONO.setDefaultValue(0)

    i2sRxWORDADJ = i2sComponent.createKeyValueSetSymbol("I2S_RXCTRL_WORDADJ", i2sRxSerializerEN)
    i2sRxWORDADJ.setLabel("Data Word Formatting Adjust")
    i2sRxWORDADJ.addKey("I2S", "0", "Right justified")
    i2sRxWORDADJ.addKey("LJ", "1", "Left justified")
    i2sRxWORDADJ.setDisplayMode("Description")
    i2sRxWORDADJ.setOutputMode("Value")
    i2sRxWORDADJ.setDefaultValue(1)

    i2sRxDATASIZE = i2sComponent.createKeyValueSetSymbol("I2S_RXCTRL_DATASIZE", i2sRxSerializerEN)
    i2sRxDATASIZE.setLabel("Data Word Size")
    # note: index values 0 and 4 (32 and 16 bits) are referenced in drv_i2s.py
    i2sRxDATASIZEnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2S\"]/value-group@[name=\"I2S_RXCTRL__DATASIZE\"]")
    i2sRxDATASIZEvalues = []
    i2sRxDATASIZEvalues = i2sRxDATASIZEnode.getChildren()
    i2sRxDATASIZEdefault = 0
    for index in range(len(i2sRxDATASIZEvalues)):
        i2sRxDATASIZEcaption = i2sRxDATASIZEvalues[index].getAttribute("caption")
        i2sRxDATASIZEname = i2sRxDATASIZEvalues[index].getAttribute("name")
        i2sRxDATASIZEvalue = i2sRxDATASIZEvalues[index].getAttribute("value")
        i2sRxDATASIZE.addKey(i2sRxDATASIZEname, i2sRxDATASIZEvalue, i2sRxDATASIZEcaption)
        if (i2sRxDATASIZEdefault == 0) and ("16" in i2sRxDATASIZEname):
            i2sRxDATASIZEdefault = index
    i2sRxDATASIZE.setDisplayMode("Description")
    i2sRxDATASIZE.setOutputMode("Value")
    i2sRxDATASIZE.setDefaultValue(i2sRxDATASIZEdefault)

    i2sRxSLOTADJ = i2sComponent.createKeyValueSetSymbol("I2S_RXCTRL_SLOTADJ", i2sRxSerializerEN)
    i2sRxSLOTADJ.setLabel("Data Slot Formatting Adjust")
    i2sRxSLOTADJ.addKey("I2S", "0", "Right justified")
    i2sRxSLOTADJ.addKey("LJ", "1", "Left justified")
    i2sRxSLOTADJ.setDisplayMode("Description")
    i2sRxSLOTADJ.setOutputMode("Value")
    i2sRxSLOTADJ.setDefaultValue(1)

    i2sRxCLKSEL = i2sComponent.createKeyValueSetSymbol("I2S_RXCTRL_CLKSEL", i2sRxSerializerEN)
    i2sRxCLKSEL.setLabel("Clock Unit Selection")
    i2sRxCLKSEL.addKey("0", "0", "Use Clock Unit 0")
    i2sRxCLKSEL.addKey("1", "1", "Use Clock Unit 1")
    i2sRxCLKSEL.setDisplayMode("Description")
    i2sRxCLKSEL.setOutputMode("Value")
    i2sRxCLKSEL.setDefaultValue(0)

    #I2S Transmit data register
    i2sTxRegister = i2sComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    i2sTxRegister.setDefaultValue("&(I2S_REGS->I2S_TXDATA)")
    i2sTxRegister.setVisible(False)

    #I2S Receive data register
    i2sRxRegister = i2sComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    i2sRxRegister.setDefaultValue("&(I2S_REGS->I2S_RXDATA)")
    i2sRxRegister.setVisible(False)

    i2sLRCPin = i2sComponent.createKeyValueSetSymbol("I2S_LRCLK_PIN_DEFINE", None)     # used for I2Sx_LRCLK_Get() macro
    i2sLRCPin.setLabel("Frame Select Pin")
    i2sLRCPin.setVisible(True)
    i2sSignalsNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"I2S\"]/instance@[name=\"I2S\"]/signals")
    i2sSignals =  i2sSignalsNode.getChildren()
    for pad in range(0, len(i2sSignals)):
        if "FS" in i2sSignals[pad].getAttribute("group"):
            i2sPadSignal =  i2sSignals[pad].getAttribute("pad")
            i2sLRCPinPort = i2sPadSignal[1:2]  # e.g. A from PA09
            i2sLRCPinPad = i2sPadSignal[2:]    # e.g. 09 from PA09
            i2sLRCPinGroup = "ABCD".index(i2sLRCPinPort)    # convert alpha port to group 0-3
            if (len(i2sLRCPinPad)==2) and (i2sLRCPinPad[0:1]=='0'):
                i2sLRCPinPad = i2sLRCPinPad[1:]   # get rid of leading 0 so not interpreted as octal
            i2sLRCPinDefine = "((PORT_REGS->GROUP[" + str(i2sLRCPinGroup) + "].PORT_IN >> " + i2sLRCPinPad + ") & 0x1)"
            i2sLRCPin.addKey(str(pad), i2sLRCPinDefine, i2sPadSignal)
    i2sLRCPin.setDisplayMode("Description")
    i2sLRCPin.setOutputMode("Value")

    i2sLRCINV = i2sComponent.createKeyValueSetSymbol("I2S_LRCLK_INVERT", i2sLRCPin)
    i2sLRCINV.setLabel("Invert")
    i2sLRCINV.addKey("0", "0", "Normal LRCLK_Get Return Value")
    i2sLRCINV.addKey("1", "1", "Invert LRCLK_Get Return Value")
    i2sLRCINV.setDisplayMode("Description")
    i2sLRCINV.setOutputMode("Value")
    i2sLRCINV.setDefaultValue(0)

    ######################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    i2sHeader1File = i2sComponent.createFileSymbol("I2S_HEADER", None)
    i2sHeader1File.setSourcePath("../peripheral/i2s_u2224/templates/plib_i2s.h.ftl")
    i2sHeader1File.setOutputName("plib_i2s.h")
    i2sHeader1File.setDestPath("/peripheral/i2s/")
    i2sHeader1File.setProjectPath("config/" + configName +"/peripheral/i2s/")
    i2sHeader1File.setType("HEADER")
    i2sHeader1File.setMarkup(True)

    i2sSource1File = i2sComponent.createFileSymbol("I2S_SOURCE", None)
    i2sSource1File.setSourcePath("../peripheral/i2s_u2224/templates/plib_i2s.c.ftl")
    i2sSource1File.setOutputName("plib_i2s.c")
    i2sSource1File.setDestPath("/peripheral/i2s/")
    i2sSource1File.setProjectPath("config/" + configName +"/peripheral/i2s/")
    i2sSource1File.setType("SOURCE")
    i2sSource1File.setMarkup(True)

    i2sSystemInitFile = i2sComponent.createFileSymbol("I2S_INIT", None)
    i2sSystemInitFile.setType("STRING")
    i2sSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    i2sSystemInitFile.setSourcePath("../peripheral/i2s_u2224/templates/system/initialization.c.ftl")
    i2sSystemInitFile.setMarkup(True)

    i2sSystemDefFile = i2sComponent.createFileSymbol("I2S_DEF", None)
    i2sSystemDefFile.setType("STRING")
    i2sSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    i2sSystemDefFile.setSourcePath("../peripheral/i2s_u2224/templates/system/definitions.h.ftl")
    i2sSystemDefFile.setMarkup(True)

