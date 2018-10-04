"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

def customUpdate(i2scModeMODE, event):
    global i2scModeIMCKDIV
    global i2scModeIMCKFS
    global i2scModeIMCKMODE
    global customVisible

    if event["value"]==1:   # Master
        customVisible = True
    else:
        customVisible = False

    i2scModeIMCKDIV.setVisible(customVisible)
    i2scModeIMCKFS.setVisible(customVisible)
    i2scModeIMCKMODE.setVisible(customVisible)

def instantiateComponent(i2scComponent):
    global i2scInstance
    global i2scModeIMCKDIV
    global i2scModeIMCKFS
    global i2scModeIMCKMODE
    global I2SCx
    global customVisible   

    customVisible = True 

    i2scInstance = i2scComponent.getID()[-1:]   # e.g "1"
    I2SCx = "I2SC" + i2scInstance
    print("Running " + I2SCx)
    
    i2scIndex = i2scComponent.createIntegerSymbol("I2SC_INDEX", None)
    i2scIndex.setVisible(False)
    i2scIndex.setDefaultValue(int(i2scInstance))

    i2scDMA = i2scComponent.createBooleanSymbol("I2SC_DMA_MODE", None)
    i2scDMA.setLabel("DMA Mode")
    i2scDMA.setDefaultValue(True)
    i2scDMA.setReadOnly(True)

    i2scInterrupt = i2scComponent.createBooleanSymbol("I2SC_INTERRUPT_MODE", None)
    i2scInterrupt.setLabel("Interrupt Mode")
    i2scInterrupt.setDefaultValue(True)
    i2scInterrupt.setReadOnly(True)

# I2SC Mode Register
    i2scModeMODE = i2scComponent.createKeyValueSetSymbol("I2SC_MR_MODE", None)
    i2scModeMODE.setLabel("Master/Slave Mode")
    i2scModeMODE.addKey("SLAVE", "0", "Slave")
    i2scModeMODE.addKey("MASTER", "1", "Master")
    i2scModeMODE.setDisplayMode("Description")
    i2scModeMODE.setOutputMode("Value")
    i2scModeMODE.setDefaultValue(1)
    i2scModeMODE.setDependencies(customUpdate, ["I2SC_MR_MODE"])

    i2scModeDATALENGTH = i2scComponent.createKeyValueSetSymbol("I2SC_MR_DATALENGTH", None)
    i2scModeDATALENGTH.setLabel("Data Word Length")
    # note: index values 0 and 4 (32 and 16 bits) are referenced in drv_i2s.py
    i2scModeDATALENGTHnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2SC\"]/value-group@[name=\"I2SC_MR__DATALENGTH\"]")
    i2scModeDATALENGTHvalues = i2scModeDATALENGTHnode.getChildren()
    i2scModeDATALENGTHdefault = 0
    for index in range(len(i2scModeDATALENGTHvalues)):
        i2scModeDATALENGTHcaption = i2scModeDATALENGTHvalues[index].getAttribute("caption")
        i2scModeDATALENGTHname = i2scModeDATALENGTHvalues[index].getAttribute("name")
        i2scModeDATALENGTHvalue = i2scModeDATALENGTHvalues[index].getAttribute("value")
        if '.' in i2scModeDATALENGTHcaption:
            caption = i2scModeDATALENGTHcaption.split('.')
            i2scModeDATALENGTHcaption = caption[0]
        i2scModeDATALENGTH.addKey(i2scModeDATALENGTHname, i2scModeDATALENGTHvalue, i2scModeDATALENGTHcaption)
        if (i2scModeDATALENGTHdefault == 0) and ("16_BITS" in i2scModeDATALENGTHname):
            i2scModeDATALENGTHdefault = index
    i2scModeDATALENGTH.setDisplayMode("Description")
    i2scModeDATALENGTH.setOutputMode("Value")
    i2scModeDATALENGTH.setDefaultValue(i2scModeDATALENGTHdefault)

    i2scModeFORMAT = i2scComponent.createKeyValueSetSymbol("I2SC_FORMAT", None)
    i2scModeFORMAT.setLabel("Data Format")
    i2scModeFORMAT.addKey("I2S", "0", "I2S")
    i2scModeFORMAT.addKey("LJ", "1", "Left justified")
    i2scModeFORMAT.setDisplayMode("Description")
    i2scModeFORMAT.setReadOnly(True)    # left-justified not supported for E70
    i2scModeFORMAT.setOutputMode("Value")
    i2scModeFORMAT.setDefaultValue(0)

    i2scModeRXMONO = i2scComponent.createKeyValueSetSymbol("I2SC_MR_RXMONO", None)
    i2scModeRXMONO.setLabel("Receiver Stereo/Mono")
    i2scModeRXMONO.addKey("STEREO", "0", "Stereo")
    i2scModeRXMONO.addKey("MONO", "1", "Mono (left dup'ed to right)")
    i2scModeRXMONO.setDisplayMode("Description")
    i2scModeRXMONO.setOutputMode("Value")
    i2scModeRXMONO.setDefaultValue(0)

    i2scModeRXDMA = i2scComponent.createKeyValueSetSymbol("I2SC_MR_RXDMA", None)
    i2scModeRXDMA.setLabel("# of DMA Channels for Receiver")
    i2scModeRXDMA.addKey("SINGLE", "0", "Single")
    i2scModeRXDMA.addKey("MULTIPLE", "1", "Multiple (1/channel)")
    i2scModeRXDMA.setDisplayMode("Description")
    i2scModeRXDMA.setOutputMode("Value")
    i2scModeRXDMA.setDefaultValue(0)

    i2scModeRXLOOP= i2scComponent.createKeyValueSetSymbol("I2SC_MR_RXLOOP", None)
    i2scModeRXLOOP.setLabel("Loopback Test Mode")
    i2scModeRXLOOP.addKey("NORMAL", "0", "Normal")
    i2scModeRXLOOP.addKey("LOOP", "1", "Loop mode")
    i2scModeRXLOOP.setDisplayMode("Description")
    i2scModeRXLOOP.setOutputMode("Value")
    i2scModeRXLOOP.setDefaultValue(0)

    i2scModeTXMONO = i2scComponent.createKeyValueSetSymbol("I2SC_MR_TXMONO", None)
    i2scModeTXMONO.setLabel("Transmitter Stereo/Mono")
    i2scModeTXMONO.addKey("STEREO", "0", "Stereo")
    i2scModeTXMONO.addKey("MONO", "1", "Mono (left dup'ed to right)")
    i2scModeTXMONO.setDisplayMode("Description")
    i2scModeTXMONO.setOutputMode("Value")
    i2scModeTXMONO.setDefaultValue(0)

    i2scModeTXDMA = i2scComponent.createKeyValueSetSymbol("I2SC_MR_TXDMA", None)
    i2scModeTXDMA .setLabel("# of DMA Channels for Transmitter")
    i2scModeTXDMA .addKey("SINGLE", "0", "Single")
    i2scModeTXDMA .addKey("MULTIPLE", "1", "Multiple (1/channel)")
    i2scModeTXDMA .setDisplayMode("Description")
    i2scModeTXDMA .setOutputMode("Value")
    i2scModeTXDMA .setDefaultValue(0)

    i2scModeTXSAME = i2scComponent.createKeyValueSetSymbol("I2SC_MR_TXSAME", None)
    i2scModeTXSAME.setLabel("Transmit Data When Underrun")
    i2scModeTXSAME.addKey("TMT_0", "0", "Transmit 0")
    i2scModeTXSAME.addKey("TMT_PREVIOUS", "1", "Transmit previous")
    i2scModeTXSAME.setDisplayMode("Description")
    i2scModeTXSAME.setOutputMode("Value")
    i2scModeTXSAME.setDefaultValue(0)

    i2scModeIWS = i2scComponent.createKeyValueSetSymbol("I2SC_MR_IWS", None)
    i2scModeIWS.setLabel("Slot Width")
    i2scModeIWS.addKey("32_WIDE", "0", "32 bits wide for 18/20/24 bits")
    i2scModeIWS.addKey("24_WIDE", "1", "24 bits wide for 18/20/24 bits")
    i2scModeIWS.setDisplayMode("Description")
    i2scModeIWS.setOutputMode("Value")
    i2scModeIWS.setDefaultValue(0)

    i2scModeIMCKDIV = i2scComponent.createIntegerSymbol("I2SC_MR_IMCKDIV", None)
    i2scModeIMCKDIV.setVisible(customVisible)
    i2scModeIMCKDIV.setLabel("Selected Clock to IMCK Ratio")
    i2scModeIMCKDIV.setDefaultValue(int(1))
    # can't be 0 -- should add check and issue warning

    i2scModeIMCKFS = i2scComponent.createKeyValueSetSymbol("I2SC_MR_IMCKFS", None)
    i2scModeIMCKFS.setVisible(customVisible)
    i2scModeIMCKFS.setLabel("Master Clock to Sample Rate Ratio")
    i2scModeIMCKFSnode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"I2SC\"]/value-group@[name=\"I2SC_MR__IMCKFS\"]")
    i2scModeIMCKFSvalues = i2scModeIMCKFSnode.getChildren()
    i2scModeIMCKFSdefault = 0
    for index in range(len(i2scModeIMCKFSvalues)):
        i2scModeIMCKFScaption = i2scModeIMCKFSvalues[index].getAttribute("caption")
        i2scModeIMCKFSname = i2scModeIMCKFSvalues[index].getAttribute("name")
        i2scModeIMCKFSvalue = i2scModeIMCKFSvalues[index].getAttribute("value")
        i2scModeIMCKFS.addKey(i2scModeIMCKFSname, i2scModeIMCKFSvalue, i2scModeIMCKFScaption)
        if "256" in i2scModeIMCKFSname:
            i2scModeIMCKFSdefault = index
    i2scModeIMCKFS.setDisplayMode("Description")
    i2scModeIMCKFS.setOutputMode("Value")
    i2scModeIMCKFS.setDefaultValue(i2scModeIMCKFSdefault)

    i2scModeIMCKMODE = i2scComponent.createKeyValueSetSymbol("I2SC_MR_IMCKMODE", None)
    i2scModeIMCKMODE.setVisible(customVisible)
    i2scModeIMCKMODE.setLabel("Master Clock Mode")
    i2scModeIMCKMODE.addKey("NONE", "0", "No master clock generated")
    i2scModeIMCKMODE.addKey("MCK_GEN", "1", "Master clock generated")
    i2scModeIMCKMODE.setDisplayMode("Description")
    i2scModeIMCKMODE.setOutputMode("Value")
    i2scModeIMCKMODE.setDefaultValue(1)

    #I2SC Transmit data register
    i2scTxRegister = i2scComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    i2scTxRegister.setDefaultValue("&(I2SC" + str(i2scInstance) + "_REGS->I2SC_THR)")
    i2scTxRegister.setVisible(False)

    #I2SC Receive data register
    i2scRxRegister = i2scComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    i2scRxRegister.setDefaultValue("&(I2SC" + str(i2scInstance) + "_REGS->I2SC_RHR)")
    i2scRxRegister.setVisible(False)

    ######################################################################
   
    configName = Variables.get("__CONFIGURATION_NAME")
    
    i2scHeader1File = i2scComponent.createFileSymbol("I2SC_HEADER", None)
    i2scHeader1File.setSourcePath("../peripheral/i2sc_11241/templates/plib_i2sc.h.ftl")
    i2scHeader1File.setOutputName("plib_i2sc" + str(i2scInstance) + ".h")
    i2scHeader1File.setDestPath("/peripheral/i2sc/")
    i2scHeader1File.setProjectPath("config/" + configName +"/peripheral/i2sc/")
    i2scHeader1File.setType("HEADER")
    i2scHeader1File.setMarkup(True)
    
    i2scSource1File = i2scComponent.createFileSymbol("I2SC_SOURCE", None)
    i2scSource1File.setSourcePath("../peripheral/i2sc_11241/templates/plib_i2sc.c.ftl")
    i2scSource1File.setOutputName("plib_i2sc" + str(i2scInstance) + ".c")
    i2scSource1File.setDestPath("/peripheral/i2sc/")
    i2scSource1File.setProjectPath("config/" + configName +"/peripheral/i2sc/")
    i2scSource1File.setType("SOURCE")
    i2scSource1File.setMarkup(True)
    
    i2scSystemInitFile = i2scComponent.createFileSymbol("I2SC_INIT", None)
    i2scSystemInitFile.setType("STRING")
    i2scSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    i2scSystemInitFile.setSourcePath("../peripheral/i2sc_11241/templates/system/system_initialize.c.ftl")
    i2scSystemInitFile.setMarkup(True)
    
    i2scSystemDefFile = i2scComponent.createFileSymbol("I2SC_DEF", None)
    i2scSystemDefFile.setType("STRING")
    i2scSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    i2scSystemDefFile.setSourcePath("../peripheral/i2sc_11241/templates/system/system_definitions.h.ftl")
    i2scSystemDefFile.setMarkup(True)
    
