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

def customUpdate(sscAudioProtocol, event):
    global sscRecClkModeCKS
    global sscRecClkModeCKO
    global sscRecClkModeCKI
    global sscRecClkModeCKG
    global sscRecClkModeSTART
    global sscRecClkModeSTOP
    global sscRecClkModeSTTDLY
    global sscRecClkModePERIOD
    global sscRecFrameModeDATLEN
    global sscRecFrameModeLOOP
    global sscRecFrameModeMSBF
    global sscRecFrameModeDATNB
    global sscRecFrameModeFSLEN
    global sscRecFrameModeFSOS
    global sscRecFrameModeFSEDGE
    global sscRecFrameModeFSLEN_EXT
    global sscTmtClkModeCKS
    global sscTmtClkModeCKO
    global sscTmtClkModeCKI
    global sscTmtClkModeCKG
    global sscTmtClkModeSTART
    global sscTmtClkModeSTTDLY
    global sscTmtClkModePERIOD
    global sscTmtFrameModeDATLEN
    global sscTmtFrameModeDATDEF
    global sscTmtFrameModeMSBF
    global sscTmtFrameModeDATNB
    global sscTmtFrameModeFSLEN
    global sscTmtFrameModeFSOS
    global sscTmtFrameModeFSDEN
    global sscTmtFrameModeFSEDGE
    global custom

    if event["value"]==0:
        custom = True
    else:
        custom = False

    sscRecClkModeCKS.setVisible(custom)     
    sscRecClkModeCKO.setVisible(custom)     
    sscRecClkModeCKI.setVisible(custom)     
    sscRecClkModeCKG.setVisible(custom)     
    sscRecClkModeSTART.setVisible(custom)     
    sscRecClkModeSTOP.setVisible(custom)     
    sscRecClkModeSTTDLY.setVisible(custom)     
    sscRecClkModePERIOD.setVisible(custom)     
    sscRecFrameModeDATLEN.setVisible(custom)     
    sscRecFrameModeLOOP.setVisible(custom)     
    sscRecFrameModeMSBF.setVisible(custom)     
    sscRecFrameModeDATNB.setVisible(custom)     
    sscRecFrameModeFSLEN.setVisible(custom)     
    sscRecFrameModeFSOS.setVisible(custom)     
    sscRecFrameModeFSEDGE.setVisible(custom)     
    sscRecFrameModeFSLEN_EXT.setVisible(custom)     
    sscTmtClkModeCKS.setVisible(custom)     
    sscTmtClkModeCKO.setVisible(custom)     
    sscTmtClkModeCKI.setVisible(custom)     
    sscTmtClkModeCKG.setVisible(custom)     
    sscTmtClkModeSTART.setVisible(custom)     
    sscTmtClkModeSTTDLY.setVisible(custom)     
    sscTmtClkModePERIOD.setVisible(custom)     
    sscTmtFrameModeDATLEN.setVisible(custom)     
    sscTmtFrameModeDATDEF.setVisible(custom)     
    sscTmtFrameModeMSBF.setVisible(custom)     
    sscTmtFrameModeDATNB.setVisible(custom)     
    sscTmtFrameModeFSLEN.setVisible(custom)     
    sscTmtFrameModeFSOS.setVisible(custom)     
    sscTmtFrameModeFSDEN.setVisible(custom)     
    sscTmtFrameModeFSEDGE.setVisible(custom)

def customUpdate2(sscUsageMode, event):
    global sscClkModeRegDIV
    global sscClkModeRegDIVComment 

    if event["value"]==0:
        custom2 = True
    else:
        custom2 = False

    sscClkModeRegDIV.setVisible(custom2)
    sscClkModeRegDIVComment.setVisible(custom2) 

def instantiateComponent(sscComponent):
    global sscRecClkModeCKS
    global sscRecClkModeCKO
    global sscRecClkModeCKI
    global sscRecClkModeCKG
    global sscRecClkModeSTART
    global sscRecClkModeSTOP
    global sscRecClkModeSTTDLY
    global sscRecClkModePERIOD
    global sscRecFrameModeDATLEN
    global sscRecFrameModeLOOP
    global sscRecFrameModeMSBF
    global sscRecFrameModeDATNB
    global sscRecFrameModeFSLEN
    global sscRecFrameModeFSOS
    global sscRecFrameModeFSEDGE
    global sscRecFrameModeFSLEN_EXT
    global sscTmtClkModeCKS
    global sscTmtClkModeCKO
    global sscTmtClkModeCKI
    global sscTmtClkModeCKG
    global sscTmtClkModeSTART
    global sscTmtClkModeSTTDLY
    global sscTmtClkModePERIOD
    global sscTmtFrameModeDATLEN
    global sscTmtFrameModeDATDEF
    global sscTmtFrameModeMSBF
    global sscTmtFrameModeDATNB
    global sscTmtFrameModeFSLEN
    global sscTmtFrameModeFSOS
    global sscTmtFrameModeFSDEN
    global sscTmtFrameModeFSEDGE
    global custom
    global sscInstanceName
    global sscClkModeRegDIV
    global sscClkModeRegDIVComment
    
    custom = False
    custom2 = False

    sscInstanceName = sscComponent.createStringSymbol("SSC_INSTANCE_NAME", None)
    sscInstanceName.setVisible(False)
    sscInstanceName.setDefaultValue(sscComponent.getID().upper())
    Log.writeInfoMessage("Running " + sscInstanceName.getValue())
           
    sscDMA = sscComponent.createBooleanSymbol("SSC_DMA_MODE", None)
    sscDMA.setVisible(True)
    sscDMA.setLabel("DMA Mode")
    sscDMA.setDefaultValue(True)
    sscDMA.setReadOnly(True)

    sscInterrupt = sscComponent.createBooleanSymbol("SSC_INTERRUPT_MODE", None)
    sscInterrupt.setVisible(True)
    sscInterrupt.setLabel("Interrupt Mode")
    sscInterrupt.setDefaultValue(True)
    sscInterrupt.setReadOnly(True)

    sscUsageMode = sscComponent.createKeyValueSetSymbol("SSC_USAGE_MODE", None)
    sscUsageMode.setVisible(True)
    sscUsageMode.setLabel("Usage Mode")
    sscUsageMode.addKey("MASTER", "0", "Master")
    sscUsageMode.addKey("SLAVE", "1", "Slave")
    sscUsageMode.setDisplayMode("Description")
    sscUsageMode.setOutputMode("Key")
    sscUsageMode.setDefaultValue(1)
    sscUsageMode.setDependencies(customUpdate2, ["SSC_USAGE_MODE"])

    sscAudioProtocol = sscComponent.createKeyValueSetSymbol("SSC_AUDIO_PROTOCOL", None)
    sscAudioProtocol.setVisible(True)
    sscAudioProtocol.setLabel("Audio Protocol Mode")
    sscAudioProtocol.addKey("CUSTOM", "0", "Custom")
    sscAudioProtocol.addKey("AUDIO_I2S", "1", "I2S")
    sscAudioProtocol.addKey("AUDIO_LJ", "2", "Left Justifed")
    sscAudioProtocol.setDisplayMode("Description")
    sscAudioProtocol.setOutputMode("Key")
    sscAudioProtocol.setDefaultValue(1)
    sscAudioProtocol.setDependencies(customUpdate, ["SSC_AUDIO_PROTOCOL"])

    sscBaud = sscComponent.createIntegerSymbol("SSC_BAUD_RATE", None)
    sscBaud.setVisible(False)   # depends on master true/slave false
    sscBaud.setLabel("Baud Rate")
    sscBaud.setDefaultValue(48000)

    sscDataWidth = sscComponent.createIntegerSymbol("SSC_DATA_LENGTH", None)
    sscDataWidth.setVisible(True)
    sscDataWidth.setLabel("Data Length")
    sscDataWidth.setDefaultValue(16)

# SSC Clock Mode Register
    sscClkModeRegDIV = sscComponent.createIntegerSymbol("SSC_CMR_DIV", None)
    sscClkModeRegDIV.setLabel("Clock Divider(peripheral clock/2*DIV)")
    sscClkModeRegDIV.setDefaultValue(0) 
    sscClkModeRegDIV.setVisible(custom2) 

    sscClkModeRegDIVComment = sscComponent.createCommentSymbol("SSC_CMR_DIV_COMMENT", None)
    sscClkModeRegDIVComment.setLabel("e.g. if 49, 150 MHz/(2*49) = bit clock of 1.5306 MHz")
    sscClkModeRegDIVComment.setVisible(custom2)

# SSC Receive Clock Mode Register
    sscRecClkModeCKS = sscComponent.createKeyValueSetSymbol("SSC_RCMR_CKS", None)
    sscRecClkModeCKS.setLabel("Receiver Clock Selection")
    sscRecClkModeCKS.addKey("MCK", "0", "MCK Divided Clock")
    sscRecClkModeCKS.addKey("TK", "1", "TK Clock Signal")
    sscRecClkModeCKS.addKey("RK", "2", "RK pin")
    sscRecClkModeCKS.setDisplayMode("Description")
    sscRecClkModeCKS.setOutputMode("Value")
    sscRecClkModeCKS.setDefaultValue(2) # depends on master 0/slave 2
    sscRecClkModeCKS.setVisible(custom)

    sscRecClkModeCKO = sscComponent.createKeyValueSetSymbol("SSC_RCMR_CKO", None)
    sscRecClkModeCKO.setLabel("Receiver Clock Output Mode")
    sscRecClkModeCKO.addKey("NONE", "0", "None, RK pin is input")
    sscRecClkModeCKO.addKey("CONTINUOUS", "1", "Continuous")
    sscRecClkModeCKO.addKey("TRANSFER", "2", "Receive clock during transfer")
    sscRecClkModeCKO.setDisplayMode("Description")
    sscRecClkModeCKO.setOutputMode("Value")
    sscRecClkModeCKO.setDefaultValue(0) # depends on master 1/slave 0
    sscRecClkModeCKO.setVisible(custom)

    sscRecClkModeCKI = sscComponent.createKeyValueSetSymbol("SSC_RCMR_CKI", None)
    sscRecClkModeCKI.setLabel("Receiver Clock Inversion")
    sscRecClkModeCKI.addKey("FALLING_RISING", "0", "Falling/rising edge")
    sscRecClkModeCKI.addKey("RISING_FALLING", "1", "Rising/falling edge")
    sscRecClkModeCKI.setDisplayMode("Description")
    sscRecClkModeCKI.setOutputMode("Value")
    sscRecClkModeCKI.setDefaultValue(0)
    sscRecClkModeCKI.setVisible(custom)

    sscRecClkModeCKG = sscComponent.createKeyValueSetSymbol("SSC_RCMR_CKG", None)
    sscRecClkModeCKG.setLabel("Receiver Clock Gating")
    sscRecClkModeCKG.addKey("CONTINUOUS", "0", "Continuous")
    sscRecClkModeCKG.addKey("EN_RF_LOW", "1", "Enabled if RF low")
    sscRecClkModeCKG.addKey("EN_RF_HIGH", "2", "Enabled if RF high")
    sscRecClkModeCKG.setDisplayMode("Description")
    sscRecClkModeCKG.setOutputMode("Value")
    sscRecClkModeCKG.setDefaultValue(0)
    sscRecClkModeCKG.setVisible(custom)

    sscRecClkModeSTART = sscComponent.createKeyValueSetSymbol("SSC_RCMR_START", None)
    sscRecClkModeSTART.setLabel("Receiver Start")
    sscRecClkModeSTART.addKey("CONTINUOUS", "0", "Continuous")
    sscRecClkModeSTART.addKey("TRANSMIT", "1", "Transmit start")
    sscRecClkModeSTART.addKey("RF_LOW", "2", "Low level on RF signal")
    sscRecClkModeSTART.addKey("RF_HIGH", "3", "High level on RF signal")
    sscRecClkModeSTART.addKey("RF_FALLING", "4", "Falling edge on RF signal")
    sscRecClkModeSTART.addKey("RF_RISING", "5", "Rising edge on RF signal")
    sscRecClkModeSTART.addKey("RF_LEVEL", "6", "Level change on RF signal")
    sscRecClkModeSTART.addKey("RF_EDGE", "7", "Any edge on RF signal")
    sscRecClkModeSTART.addKey("CMP_0", "8", "Compare 0")
    sscRecClkModeSTART.setDisplayMode("Description")
    sscRecClkModeSTART.setOutputMode("Value")
    sscRecClkModeSTART.setDefaultValue(7)   # depends on master 0/slave 7
    sscRecClkModeSTART.setVisible(custom)

    sscRecClkModeSTOP= sscComponent.createKeyValueSetSymbol("SSC_RCMR_STOP", None)
    sscRecClkModeSTOP.setLabel("Receiver Stop")
    sscRecClkModeSTOP.addKey("WAIT", "0", "Wait for new Compare 0")
    sscRecClkModeSTOP.addKey("CONTINUOUS", "1", "Continuous until Compare 1")
    sscRecClkModeSTOP.setDisplayMode("Description")
    sscRecClkModeSTOP.setOutputMode("Value")
    sscRecClkModeSTOP.setDefaultValue(0)
    sscRecClkModeSTOP.setVisible(custom)

    sscRecClkModeSTTDLY = sscComponent.createIntegerSymbol("SSC_RCMR_STTDLY", None)
    sscRecClkModeSTTDLY.setLabel("Receiver Start Delay")
    sscRecClkModeSTTDLY.setDefaultValue(1)  # depends on master 0/slave 1
    sscRecClkModeSTTDLY.setVisible(custom)

    sscRecClkModePERIOD = sscComponent.createIntegerSymbol("SSC_RCMR_PERIOD", None)
    sscRecClkModePERIOD.setLabel("Receiver Period Divider")
    sscRecClkModePERIOD.setDefaultValue(0)
    sscRecClkModePERIOD.setVisible(custom)

# SSC Receive Frame Mode Register
    sscRecFrameModeDATLEN = sscComponent.createIntegerSymbol("SSC_RFMR_DATLEN", None)
    sscRecFrameModeDATLEN.setLabel("Receiver Data Length(n+1 is actual size)")
    sscRecFrameModeDATLEN.setDefaultValue(15)
    sscRecFrameModeDATLEN.setVisible(custom)

    sscRecFrameModeLOOP = sscComponent.createKeyValueSetSymbol("SSC_RFMR_LOOP", None)
    sscRecFrameModeLOOP.setLabel("Receiver Loop Mode")
    sscRecFrameModeLOOP.addKey("NORMAL", "0", "Normal")
    sscRecFrameModeLOOP.addKey("LOOP", "1", "Loop")
    sscRecFrameModeLOOP.setDisplayMode("Description")
    sscRecFrameModeLOOP.setOutputMode("Value")
    sscRecFrameModeLOOP.setDefaultValue(0)
    sscRecFrameModeLOOP.setVisible(custom)

    sscRecFrameModeMSBF = sscComponent.createKeyValueSetSymbol("SSC_RFMR_MSBF", None)
    sscRecFrameModeMSBF.setLabel("Receiver MSB First")
    sscRecFrameModeMSBF.addKey("LSB", "0", "LSB sampled first")
    sscRecFrameModeMSBF.addKey("MSB", "1", "MSB sampled first")
    sscRecFrameModeMSBF.setDisplayMode("Description")
    sscRecFrameModeMSBF.setOutputMode("Value")
    sscRecFrameModeMSBF.setDefaultValue(1)  # depends on master 0/slave 1
    sscRecFrameModeMSBF.setVisible(custom)

    sscRecFrameModeDATNB = sscComponent.createIntegerSymbol("SSC_RFMR_DATNB", None)
    sscRecFrameModeDATNB.setLabel("Receiver Data Number Per Frame")
    sscRecFrameModeDATNB.setDefaultValue(0)
    sscRecFrameModeDATNB.setVisible(custom)

    sscRecFrameModeFSLEN = sscComponent.createIntegerSymbol("SSC_RFMR_FSLEN", None)
    sscRecFrameModeFSLEN.setLabel("Receiver Frame Sync Length")
    sscRecFrameModeFSLEN.setDefaultValue(0)
    sscRecFrameModeFSLEN.setVisible(custom)

    sscRecFrameModeFSOS = sscComponent.createKeyValueSetSymbol("SSC_RFMR_FSOS", None)
    sscRecFrameModeFSOS.setLabel("Receiver Frame Sync Output")
    sscRecFrameModeFSOS.addKey("NONE", "0", "None, RF is input")
    sscRecFrameModeFSOS.addKey("NEGATIVE", "1", "Negative pulse")
    sscRecFrameModeFSOS.addKey("POSITIVE", "2", "Positive pulse")
    sscRecFrameModeFSOS.addKey("LOW", "3", "Driven low during transfer")
    sscRecFrameModeFSOS.addKey("HIGH", "4", "Driven high during transfer")
    sscRecFrameModeFSOS.addKey("TOGGLING", "5", "Toggling start of each transfer")
    sscRecFrameModeFSOS.setDisplayMode("Description")
    sscRecFrameModeFSOS.setOutputMode("Value")
    sscRecFrameModeFSOS.setDefaultValue(0)  # depends on master 5/slave 0
    sscRecFrameModeFSOS.setVisible(custom)

    sscRecFrameModeFSEDGE = sscComponent.createKeyValueSetSymbol("SSC_RFMR_FSEDGE", None)
    sscRecFrameModeFSEDGE.setLabel("Receiver Frame Sync Edge Detection")
    sscRecFrameModeFSEDGE.addKey("POSITIVE", "0", "Positive edge")
    sscRecFrameModeFSEDGE.addKey("NEGATIVE", "1", "Negative edge")
    sscRecFrameModeFSEDGE.setDisplayMode("Description")
    sscRecFrameModeFSEDGE.setOutputMode("Value")
    sscRecFrameModeFSEDGE.setDefaultValue(0)
    sscRecFrameModeFSEDGE.setVisible(custom)

    sscRecFrameModeFSLEN_EXT = sscComponent.createIntegerSymbol("SSC_RFMR_FSLEN_EXT", None)
    sscRecFrameModeFSLEN_EXT.setLabel("Receiver FSLEN Field Extension")
    sscRecFrameModeFSLEN_EXT.setDefaultValue(0)
    sscRecFrameModeFSLEN_EXT.setVisible(custom)

# SSC Transmit Clock Mode Register
    sscTmtClkModeCKS = sscComponent.createKeyValueSetSymbol("SSC_TCMR_CKS", None)
    sscTmtClkModeCKS.setLabel("Transmitter Clock Selection")
    sscTmtClkModeCKS.addKey("MCK", "0", "MCK Divided Clock")
    sscTmtClkModeCKS.addKey("RK", "1", "RK Clock Signal")
    sscTmtClkModeCKS.addKey("TK", "2", "TK pin")
    sscTmtClkModeCKS.setDisplayMode("Description")
    sscTmtClkModeCKS.setOutputMode("Value")
    sscTmtClkModeCKS.setDefaultValue(2) # depends on master 0/slave 2
    sscTmtClkModeCKS.setVisible(custom)

    sscTmtClkModeCKO = sscComponent.createKeyValueSetSymbol("SSC_TCMR_CKO", None)
    sscTmtClkModeCKO.setLabel("Transmitter Clock Output Mode")
    sscTmtClkModeCKO.addKey("NONE", "0", "None, TK pin is input")
    sscTmtClkModeCKO.addKey("CONTINUOUS", "1", "Continuous transmit clock")
    sscTmtClkModeCKO.addKey("TRANSFER", "2", "Transmit clock during transfer")
    sscTmtClkModeCKO.setDisplayMode("Description")
    sscTmtClkModeCKO.setOutputMode("Value")
    sscTmtClkModeCKO.setDefaultValue(0) # depends on master 1 /slave 0
    sscTmtClkModeCKO.setVisible(custom)

    sscTmtClkModeCKI = sscComponent.createKeyValueSetSymbol("SSC_TCMR_CKI", None)
    sscTmtClkModeCKI.setLabel("Transmitter Clock Inversion")
    sscTmtClkModeCKI.addKey("FALLING_RISING", "0", "Falling/rising edge")
    sscTmtClkModeCKI.addKey("RISING_FALLING", "1", "Rising/falling edge")
    sscTmtClkModeCKI.setDisplayMode("Description")
    sscTmtClkModeCKI.setOutputMode("Value")
    sscTmtClkModeCKI.setDefaultValue(0)
    sscTmtClkModeCKI.setVisible(custom)

    sscTmtClkModeCKG = sscComponent.createKeyValueSetSymbol("SSC_TCMR_CKG", None)
    sscTmtClkModeCKG.setLabel("Transmitter Clock Gating")
    sscTmtClkModeCKG.addKey("CONTINUOUS", "0", "Continuous")
    sscTmtClkModeCKG.addKey("EN_TF_LOW", "1", "Enabled if TF low")
    sscTmtClkModeCKG.addKey("EN_TF_HIGH", "2", "Enabled if TF high")
    sscTmtClkModeCKG.setDisplayMode("Description")
    sscTmtClkModeCKG.setOutputMode("Value")
    sscTmtClkModeCKG.setDefaultValue(0)
    sscTmtClkModeCKG.setVisible(custom)

    sscTmtClkModeSTART = sscComponent.createKeyValueSetSymbol("SSC_TCMR_START", None)
    sscTmtClkModeSTART.setLabel("Transmitter Start")
    sscTmtClkModeSTART.addKey("CONTINUOUS", "0", "Continuous")
    sscTmtClkModeSTART.addKey("RECEIVE", "1", "Receiver start")
    sscTmtClkModeSTART.addKey("TF_LOW", "2", "Low level on TF signal")
    sscTmtClkModeSTART.addKey("TF_HIGH", "3", "High level on TF signal")
    sscTmtClkModeSTART.addKey("TF_FALLING", "4", "Falling edge on TF signal")
    sscTmtClkModeSTART.addKey("TF_RISING", "5", "Rising edge on TF signal")
    sscTmtClkModeSTART.addKey("T_LEVEL", "6", "Level change on TF signal")
    sscTmtClkModeSTART.addKey("TF_EDGE", "7", "Any edge on TF signal")
    sscTmtClkModeSTART.setDisplayMode("Description")
    sscTmtClkModeSTART.setOutputMode("Value")
    sscTmtClkModeSTART.setDefaultValue(7)   # depends on master 0 /slave 7
    sscTmtClkModeSTART.setVisible(custom)

    sscTmtClkModeSTTDLY = sscComponent.createIntegerSymbol("SSC_TCMR_STTDLY", None)
    sscTmtClkModeSTTDLY.setLabel("Transmitter Start Delay")
    sscTmtClkModeSTTDLY.setDefaultValue(1)  # depends on master 0/slave 1
    sscTmtClkModeSTTDLY.setVisible(custom)

    sscTmtClkModePERIOD = sscComponent.createIntegerSymbol("SSC_TCMR_PERIOD", None)
    sscTmtClkModePERIOD.setLabel("Transmitter Period Divider")
    sscTmtClkModePERIOD.setDefaultValue(0)
    sscTmtClkModePERIOD.setVisible(custom)

# SSC Transmit Frame Mode Register
    sscTmtFrameModeDATLEN = sscComponent.createIntegerSymbol("SSC_TFMR_DATLEN", None)
    sscTmtFrameModeDATLEN.setLabel("Transmitter Data Length(n+1 is actual size)")
    sscTmtFrameModeDATLEN.setDefaultValue(15)
    sscTmtFrameModeDATLEN.setVisible(custom)

    sscTmtFrameModeDATDEF = sscComponent.createKeyValueSetSymbol("SSC_TFMR_DATDEF", None)
    sscTmtFrameModeDATDEF.setLabel("Transmitter Data Default")
    sscTmtFrameModeDATDEF.addKey("LOW", "0", "Low")
    sscTmtFrameModeDATDEF.addKey("HIGH", "1", "High")
    sscTmtFrameModeDATDEF.setDisplayMode("Description")
    sscTmtFrameModeDATDEF.setOutputMode("Value")
    sscTmtFrameModeDATDEF.setDefaultValue(0)
    sscTmtFrameModeDATDEF.setVisible(custom)

    sscTmtFrameModeMSBF = sscComponent.createKeyValueSetSymbol("SSC_TFMR_MSBF", None)
    sscTmtFrameModeMSBF.setLabel("Transmitter MSB First")
    sscTmtFrameModeMSBF.addKey("LSB", "0", "LSB output first")
    sscTmtFrameModeMSBF.addKey("MSB", "1", "MSB output first")
    sscTmtFrameModeMSBF.setDisplayMode("Description")
    sscTmtFrameModeMSBF.setOutputMode("Value")
    sscTmtFrameModeMSBF.setDefaultValue(1)
    sscTmtFrameModeMSBF.setVisible(custom)

    sscTmtFrameModeDATNB = sscComponent.createIntegerSymbol("SSC_TFMR_DATNB", None)
    sscTmtFrameModeDATNB.setLabel("Transmitter Data Number Per Frame")
    sscTmtFrameModeDATNB.setDefaultValue(0)
    sscTmtFrameModeDATNB.setVisible(custom)

    sscTmtFrameModeFSLEN = sscComponent.createIntegerSymbol("SSC_TFMR_FSLEN", None)
    sscTmtFrameModeFSLEN.setLabel("Transmitter Frame Sync Length")
    sscTmtFrameModeFSLEN.setDefaultValue(0)
    sscTmtFrameModeFSLEN.setVisible(custom)

    sscTmtFrameModeFSOS = sscComponent.createKeyValueSetSymbol("SSC_TFMR_FSOS", None)
    sscTmtFrameModeFSOS.setLabel("Transmitter Frame Sync Output")
    sscTmtFrameModeFSOS.addKey("NONE", "0", "None, TF is input")
    sscTmtFrameModeFSOS.addKey("NEGATIVE", "1", "Negative pulse")
    sscTmtFrameModeFSOS.addKey("POSITIVE", "2", "Positive pulse")
    sscTmtFrameModeFSOS.addKey("LOW", "3", "Driven low during transfer")
    sscTmtFrameModeFSOS.addKey("HIGH", "4", "Driven high during transfer")
    sscTmtFrameModeFSOS.addKey("TOGGLING", "5", "Toggling start of each transfer")
    sscTmtFrameModeFSOS.setDisplayMode("Description")
    sscTmtFrameModeFSOS.setOutputMode("Value")
    sscTmtFrameModeFSOS.setDefaultValue(0)  # depends on master 5/slave 0
    sscTmtFrameModeFSOS.setVisible(custom)

    sscTmtFrameModeFSDEN = sscComponent.createKeyValueSetSymbol("SSC_TFMR_FSDEN", None)
    sscTmtFrameModeFSDEN.setLabel("Transmitter Frame Sync Data Enable")
    sscTmtFrameModeFSDEN.addKey("POSITIVE", "0", "TD driven with default value")
    sscTmtFrameModeFSDEN.addKey("NEGATIVE", "1", "TSHR value shifted out")
    sscTmtFrameModeFSDEN.setDisplayMode("Description")
    sscTmtFrameModeFSDEN.setOutputMode("Value")
    sscTmtFrameModeFSDEN.setDefaultValue(0)
    sscTmtFrameModeFSDEN.setVisible(custom)    

    sscTmtFrameModeFSEDGE = sscComponent.createKeyValueSetSymbol("SSC_TFMR_FSEDGE", None)
    sscTmtFrameModeFSEDGE.setLabel("Transmitter Frame Sync Edge Detection")
    sscTmtFrameModeFSEDGE.addKey("POSITIVE", "0", "Positive edge")
    sscTmtFrameModeFSEDGE.addKey("NEGATIVE", "1", "Negative edge")
    sscTmtFrameModeFSEDGE.setDisplayMode("Description")
    sscTmtFrameModeFSEDGE.setOutputMode("Value")
    sscTmtFrameModeFSEDGE.setDefaultValue(0)
    sscTmtFrameModeFSEDGE.setVisible(custom)

    sscTmtFrameModeFSLEN_EXT = sscComponent.createIntegerSymbol("SSC_TFMR_FSLEN_EXT", None)
    sscTmtFrameModeFSLEN_EXT.setLabel("Transmitter FSLEN Field Extension")
    sscTmtFrameModeFSLEN_EXT.setDefaultValue(0)
    sscTmtFrameModeFSLEN_EXT.setVisible(custom)

    #SSC Transmit data register
    sscTxRegister = sscComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    sscTxRegister.setDefaultValue("&(SSC_REGS->SSC_THR)")
    sscTxRegister.setVisible(False)

    #SSC Receive data register
    sscRxRegister = sscComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    sscRxRegister.setDefaultValue("&(SSC_REGS->SSC_RHR)")
    sscRxRegister.setVisible(False)

    sscLRCPin = sscComponent.createStringSymbol("SSC_LRCLK_PIN_DEFINE", None)     # used for SSC_LRCLK_GET() 
    sscLRCPin.setVisible(False)
    sscSignalsNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SSC\"]" +
                                  "/instance@[name=\"" + sscInstanceName.getValue() + "\"]/signals")
    sscSignals =  sscSignalsNode.getChildren()
    sscLRCPinDefine = "Undefined"
    for pad in range(0, len(sscSignals)):
        if "TF" in sscSignals[pad].getAttribute("group"):
            sscPadSignal =  sscSignals[pad].getAttribute("pad")
            sscLRCPinPort = sscPadSignal[1:2]  # e.g. B from PB0
            sscLRCPinPad = sscPadSignal[2:]    # e.g. 0 from PB0
            sscLRCPinDefine = "((PIO" + sscLRCPinPort + "_REGS->PIO_PDSR >> " + sscLRCPinPad + ") & 0x1)"
    sscLRCPin.setDefaultValue(sscLRCPinDefine)

    ######################################################################

    configName = Variables.get("__CONFIGURATION_NAME")
       
    sscHeader1File = sscComponent.createFileSymbol("SSC_HEADER", None)
    sscHeader1File.setSourcePath("../peripheral/ssc_6078/templates/plib_ssc.h.ftl")
    sscHeader1File.setOutputName("plib_"+sscInstanceName.getValue().lower()+".h")
    sscHeader1File.setDestPath("/peripheral/ssc/")
    sscHeader1File.setProjectPath("config/" + configName +"/peripheral/ssc/")
    sscHeader1File.setType("HEADER")
    sscHeader1File.setMarkup(True)
    
    sscSource1File = sscComponent.createFileSymbol("SSC_SOURCE", None)
    sscSource1File.setSourcePath("../peripheral/ssc_6078/templates/plib_ssc.c.ftl")
    sscSource1File.setOutputName("plib_"+sscInstanceName.getValue().lower()+".c")
    sscSource1File.setDestPath("/peripheral/ssc/")
    sscSource1File.setProjectPath("config/" + configName +"/peripheral/ssc/")
    sscSource1File.setType("SOURCE")
    sscSource1File.setMarkup(True)
    
    sscSystemInitFile = sscComponent.createFileSymbol("SSC_INIT", None)
    sscSystemInitFile.setType("STRING")
    sscSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sscSystemInitFile.setSourcePath("../peripheral/ssc_6078/templates/system/initialization.c.ftl")
    sscSystemInitFile.setMarkup(True)
    
    sscSystemDefFile = sscComponent.createFileSymbol("SSC_DEF", None)
    sscSystemDefFile.setType("STRING")
    sscSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sscSystemDefFile.setSourcePath("../peripheral/ssc_6078/templates/system/definitions.h.ftl")
    sscSystemDefFile.setMarkup(True)
    
