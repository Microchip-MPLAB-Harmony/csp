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
global sort_alphanumeric

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def handleMessage(messageID, args):
    global spiSym_MR_MSTR
    global spiInterrupt
    global spiSym_MR_PCS
    result_dict = {}

    if (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            spiSym_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            spiSym_MR_MSTR.setSelectedKey("Master")

    elif (messageID == "SPI_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            spiSym_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            spiSym_MR_MSTR.setSelectedKey("Slave")

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            spiInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            spiInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            spiInterrupt.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if args.get("isReadOnly") != None:
            spiSym_MR_PCS.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == False:
            spiSym_MR_PCS.setSelectedKey("GPIO",1)
        if args.get("isVisible") != None:
            spiSym_MR_PCS.setVisible(args["isVisible"])

    #elif (messageID == "SPI_SLAVE_INTERRUPT_MODE"):
        # To be implemented

    return result_dict

global dummyDataDict
dummyDataDict = {
                    "_8_BIT"     :   0xFF,
                    "_9_BIT"     :   0x1FF,
                    "_10_BIT"    :   0x3FF,
                    "_11_BIT"    :   0x7FF,
                    "_12_BIT"    :   0xFFF,
                    "_13_BIT"    :   0x1FFF,
                    "_14_BIT"    :   0x3FFF,
                    "_15_BIT"    :   0x7FFF,
                    "_16_BIT"    :   0xFFFF,
                }

spiBitField_CR_FIFOEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CR"]/bitfield@[name="FIFOEN"]')

spiBitField_MR_MSTR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_MR"]/bitfield@[name="MSTR"]')
spiValGrp_MR_MSTR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_MR__MSTR"]')

spiBitField_MR_PCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_MR"]/bitfield@[name="PCS"]')
spiValGrp_MR_PCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_MR__PCS"]')

spiBitField_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="BITS"]')
spiValGrp_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__BITS"]')

spiBitField_CSR_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="CPOL"]')
spiValGrp_CSR_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__CPOL"]')

spiBitField_CSR_NCPHA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI_CSR"]/bitfield@[name="NCPHA"]')
spiValGrp_CSR_NCPHA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI_CSR__NCPHA"]')

# clock frequency symbol update callback
def SPISourceClockChanged(symbol, event):

    if event["id"] == "SPI_MR_MSTR":
        spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()
        symbol.setVisible(spiMode == "MASTER")
    else:
        symbol.setValue(event["value"], 2)

# Dependency Function to show or hide the warning message depending on Clock enable/disable status
def ClockStatusWarning(symbol, event):

    if event["value"] == False:
       symbol.setVisible(True)
    else:
       symbol.setVisible(False)

# Dependency Function to show or hide the warning message depending on Interrupt enable/disable status
def InterruptStatusWarning(symbol, event):

    global spiInterrupt

    if spiInterrupt.getValue() == True:
       symbol.setVisible(event["value"])

# Dependency Function for symbol visibility
def updateSPIDMAConfigurationVisbleProperty(symbol, event):

    symbol.setVisible(event["value"])

def ClockModeInfo(symbol, event):

    CPHA = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_CLOCK_PHASE")
    CPOL = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_CLOCK_POLARITY")

    if (CPOL == 0) and (CPHA == 0):
        symbol.setLabel("***SPI Mode 0 is Selected***")
    elif (CPOL == 0) and (CPHA == 1):
        symbol.setLabel("***SPI Mode 1 is Selected***")
    elif (CPOL == 1) and (CPHA == 0):
        symbol.setLabel("***SPI Mode 2 is Selected***")
    else:
        symbol.setLabel("***SPI Mode 3 is Selected***")

def setupSpiIntSymbolAndIntHandler(spiInterrupt, event):
    global spiSyminterruptVector
    global spiSyminterruptHandler
    global spiSyminterruptHandlerLock
    global spiSyminterruptVectorUpdate
    global spiSymIntEnComment
    global spiSym_MR_PCS
    global spiDriverControlled
    global spiInterruptDriverModeComment

    if(event["id"] == "SPI_INTERRUPT_MODE"):
        Database.clearSymbolValue("core", spiSyminterruptVector)
        Database.clearSymbolValue("core", spiSyminterruptHandler)
        Database.clearSymbolValue("core", spiSyminterruptHandlerLock)

        if (event["value"] == True):
            Database.setSymbolValue("core", spiSyminterruptVector, True, 1)
            Database.setSymbolValue("core", spiSyminterruptHandler, spiInstanceName.getValue() + "_InterruptHandler", 1)
            Database.setSymbolValue("core", spiSyminterruptHandlerLock, True, 1)
        else:
            Database.setSymbolValue("core", spiSyminterruptVector, False, 1)
            Database.setSymbolValue("core", spiSyminterruptHandler, spiInstanceName.getValue() + "_Handler", 1)
            Database.setSymbolValue("core", spiSyminterruptHandlerLock, False, 1)
    elif (event["id"] == "SPI_MR_MSTR"):
        spiInterrupt.setReadOnly(event["symbol"].getSelectedKey() == "SLAVE")
        if event["symbol"].getSelectedKey() == "SLAVE":
            spiInterrupt.setValue(True)


def getMasterClockFreq():

    clkSymMasterClockFreq = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_MASTER_CLOCK")
    return int(clkSymMasterClockFreq)

def spiMasterModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getSelectedKey() == "MASTER")

def spiSlaveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getSelectedKey() == "SLAVE")

def chipSelectUpdateOnModeChange(symbol, event):

    spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()

    if (spiMode == "SLAVE"):
        symbol.setReadOnly(True)
        symbol.setValue(0)
    else:
        symbol.setReadOnly(False)

def showSlaveDependencies(symbol, event):

    spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()
    symbol.setVisible(spiMode == "SLAVE")

def showMasterDependencies(spiSym_MR_Dependencies, event):

    if event["symbol"].getKey(event["value"]) == "MASTER":
        spiSym_MR_Dependencies.setVisible(True)
    else:
        spiSym_MR_Dependencies.setVisible(False)

def updateSPISlaveBusyPinVisibility(symbol, event):

    spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()
    busyPinEnabled = event["source"].getSymbolByID("SPIS_USE_BUSY_PIN").getValue() == True
    symbol.setVisible(spiMode == "SLAVE" and busyPinEnabled == True)

def SCBR_ValueUpdate(spiSym_CSR_SCBR_VALUE, event):

    if event["id"] == "SPI_MASTER_CLOCK":
        clk = int(event["value"])
        baud = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_BAUD_RATE")
    else:
        #This means there is change in baud rate provided by user in GUI
        baud = event["value"]
        clk = int(Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_MASTER_CLOCK"))

    SCBR = clk/baud
    spiSymInvalidClock.setVisible(SCBR < 1 or SCBR > 255)

    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255

    spiSym_CSR_SCBR_VALUE.setValue(SCBR, 1)

def calculateCSRIndex(spiSymCSRIndex, event):

    spiSymCSRIndex.setValue(int(event["symbol"].getKeyValue(event["value"])[-1]), 1)

def DummyData_ValueUpdate(spiSymDummyData, event):

    if event["id"] == "SPI_CHARSIZE_BITS":
        spiSymDummyData.setValue(dummyDataDict[event["symbol"].getKey(event["value"])], 1)
        spiSymDummyData.setMax(dummyDataDict[event["symbol"].getKey(event["value"])])
    else:
        spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()
        spiSymDummyData.setVisible(spiMode == "MASTER")

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def fifoModeVisible (symbol, event):

    if spiBitField_CR_FIFOEN != None:

        spiMode = event["source"].getSymbolByID("SPI_MR_MSTR").getSelectedKey()
        interruptMode = event["source"].getSymbolByID("SPI_INTERRUPT_MODE").getValue()

        if spiMode == "SLAVE":
            symbol.setReadOnly(True)
            symbol.setVisible(True)
            symbol.setValue(True)
        else:
            if interruptMode == True:
                symbol.setReadOnly(False)
                symbol.setVisible(True)
            else:
                symbol.setVisible(False)

def instantiateComponent(spiComponent):

    global spiInstanceName
    global spiSyminterruptVector
    global spiSyminterruptHandler
    global spiSyminterruptHandlerLock
    global spiSyminterruptVectorUpdate
    global InternalinterruptVectorChange
    global spiSym_MR_MSTR

    InternalinterruptVectorChange = False

    spiInstanceName = spiComponent.createStringSymbol("SPI_INSTANCE_NAME", None)
    spiInstanceName.setVisible(False)
    spiInstanceName.setDefaultValue(spiComponent.getID().upper())

    #IDs used in NVIC Manager
    spiSyminterruptVector = spiInstanceName.getValue() + "_INTERRUPT_ENABLE"
    spiSyminterruptHandler = spiInstanceName.getValue() + "_INTERRUPT_HANDLER"
    spiSyminterruptHandlerLock = spiInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    spiSyminterruptVectorUpdate = spiInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Enable clock for SPI
    Database.setSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    global spiDriverControlled
    spiDriverControlled = spiComponent.createBooleanSymbol("SPI_DRIVER_CONTROLLED", None)
    spiDriverControlled.setVisible(False)

    global spiInterrupt
    spiInterrupt = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiInterrupt.setLabel("Interrupt Mode")
    spiInterrupt.setDefaultValue(True)

    #By Default interrupt mode is enabled and corresponding information is passed to NVIC manager
    Database.setSymbolValue("core", spiSyminterruptVector, True, 1)
    Database.setSymbolValue("core", spiSyminterruptHandler, spiInstanceName.getValue() + "_InterruptHandler", 1)
    Database.setSymbolValue("core", spiSyminterruptHandlerLock, True, 1)
    spiInterrupt.setDependencies(setupSpiIntSymbolAndIntHandler, ["SPI_INTERRUPT_MODE", "SPI_MR_MSTR"])

    spiRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPI\"]/register-group@[name=\"SPI\"]")
    spiRegisterList = spiRegisterGroup.getChildren()
    for index in range(0, len(spiRegisterList)):
        if (spiRegisterList[index].getAttribute("name") == "SPI_RPR"):
            spiDMAEnable = spiComponent.createBooleanSymbol("USE_SPI_DMA", None)
            spiDMAEnable.setLabel("Enable DMA for Transmit and Receive")
            spiDMAEnable.setDependencies(updateSPIDMAConfigurationVisbleProperty, ["SPI_INTERRUPT_MODE"])
            break

    spiSym_MR_MSTR = spiComponent.createKeyValueSetSymbol("SPI_MR_MSTR", None)
    spiSym_MR_MSTR.setLabel(spiBitField_MR_MSTR.getAttribute("caption"))
    spiSym_MR_MSTR.setOutputMode("Key")
    spiSym_MR_MSTR.setDisplayMode("Description")
    spiSym_MR_MSTR.setDefaultValue(0)
    spiSym_MR_MSTR.setReadOnly(False)

    for id in range(0, len(spiValGrp_MR_MSTR.getChildren())):
        valueName = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("name")
        value = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("value")
        description = spiValGrp_MR_MSTR.getChildren()[id].getAttribute("caption")
        spiSym_MR_MSTR.addKey(valueName, value, description)

    spisSymFIFOEnable = spiComponent.createBooleanSymbol("SPI_FIFO_ENABLE", None)
    spisSymFIFOEnable.setLabel("Enable FIFO")
    spisSymFIFOEnable.setDefaultValue(False)
    spisSymFIFOEnable.setVisible(spiBitField_CR_FIFOEN != None)
    spisSymFIFOEnable.setDependencies(fifoModeVisible, ["SPI_INTERRUPT_MODE", "SPI_MR_MSTR"])

    spiPCSMask = int(str(spiBitField_MR_PCS.getAttribute("mask")), 16)
    spiPCSValue = spiPCSMask >> 16

    DefaultPCS = 0
    global spiSym_MR_PCS
    spiSym_MR_PCS = spiComponent.createKeyValueSetSymbol("SPI_MR_PCS", None)
    spiSym_MR_PCS.setLabel(spiBitField_MR_PCS.getAttribute("caption"))
    spiSym_MR_PCS.setOutputMode("Key")
    spiSym_MR_PCS.setDisplayMode("Key")
    spiSym_MR_PCS.setDefaultValue(DefaultPCS)
    spiSym_MR_PCS.setDependencies(chipSelectUpdateOnModeChange, ["SPI_MR_MSTR"])

    spiSym_MR_PCS.addKey("NPCS0", "NPCS0", "NPCS0 as Chip Select")
    spiSym_MR_PCS.addKey("NPCS1", "NPCS1", "NPCS1 as Chip Select")

    # Check weather more than two chip select options are available
    if spiPCSValue > 3:
        spiSym_MR_PCS.addKey("NPCS2", "NPCS2", "NPCS2 as Chip Select")
        spiSym_MR_PCS.addKey("NPCS3", "NPCS3", "NPCS3 as Chip Select")

    # When User wants to control his chip select himself (through some GPIO pin),
    # then all the NPCSx lines are free to be used as PIO pins. But in MR_PCS
    # field, one of the NPCS lines still has to be selected in order to decide
    # which SPI_CSRx register will be active. Here we have used NPCS0 selection
    # for such case, it can be changed to any other NPCSx line without affecting
    # the user.
    spiSym_MR_PCS.addKey("GPIO", "NPCS0", "User Controlled Chip Select Through GPIO Pin")

    defaultIndex = int(spiSym_MR_PCS.getKey(DefaultPCS)[-1])

    # internal symbol, used to pass CSR register index to SPI FTL
    spiSymCSRIndex = spiComponent.createIntegerSymbol("SPI_CSR_INDEX", None)
    spiSymCSRIndex.setDefaultValue(defaultIndex)
    spiSymCSRIndex.setVisible(False)
    spiSymCSRIndex.setDependencies(calculateCSRIndex, ["SPI_MR_PCS"])

    defaultbaudRate = 1000000
    defaultSCBR = int(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY"))/defaultbaudRate

    # Provide a source clock selection symbol for masks that supports it
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPI\"]/value-group@[name=\"SPI_MR__BRSRCCLK\"]")
    if valueGroup != None:
        values = valueGroup.getChildren()

        spiSymClockSrc = spiComponent.createKeyValueSetSymbol("SPI_CLK_SRC", None)
        spiSymClockSrc.setLabel(valueGroup.getAttribute("caption"))

        for index in range(len(values)):
            spiSymClockSrc.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"), values[index].getAttribute("caption"))

        spiSymClockSrc.setOutputMode("Key")
        spiSymClockSrc.setDisplayMode("Key")

    # Used to pass master clock frequency to SPI FTL
    spiSymMasterClock = spiComponent.createIntegerSymbol("SPI_MASTER_CLOCK", None)
    spiSymMasterClock.setLabel("Bit rate source clock frequency (Hz)")
    spiSymMasterClock.setDefaultValue(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY" ))
    spiSymMasterClock.setReadOnly(True)
    spiSymMasterClock.setDependencies(SPISourceClockChanged, ["core." + spiInstanceName.getValue() + "_CLOCK_FREQUENCY", "SPI_MR_MSTR"])

    spiSym_CSR_SCBR = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", None)
    spiSym_CSR_SCBR.setLabel("Baud Rate in Hz")
    spiSym_CSR_SCBR.setDefaultValue(defaultbaudRate)
    spiSym_CSR_SCBR.setMin(1)
    spiSym_CSR_SCBR.setDependencies(showMasterDependencies, ["SPI_MR_MSTR"])

    global spiSymInvalidClock
    spiSymInvalidClock = spiComponent.createCommentSymbol("SPI_CLOCK_INVALID_COMMENT", None)
    spiSymInvalidClock.setLabel("Cannot generate input baud rate from the configured source clock frequency !!!")
    spiSymInvalidClock.setVisible(False)

    #local variable for code generation
    spiSym_CSR_SCBR_VALUE = spiComponent.createIntegerSymbol("SPI_CSR_SCBR_VALUE", None)
    spiSym_CSR_SCBR_VALUE.setDefaultValue(defaultSCBR)
    spiSym_CSR_SCBR_VALUE.setVisible(False)
    spiSym_CSR_SCBR_VALUE.setDependencies(SCBR_ValueUpdate, ["SPI_BAUD_RATE", "SPI_MASTER_CLOCK"])

    spiSym_CSR_BITS = spiComponent.createKeyValueSetSymbol("SPI_CHARSIZE_BITS", None)
    spiSym_CSR_BITS.setLabel(spiBitField_CSR_BITS.getAttribute("caption"))
    spiSym_CSR_BITS.setOutputMode("Key")
    spiSym_CSR_BITS.setDisplayMode("Description")
    spiSym_CSR_BITS.setDefaultValue(0)

    for id in range(0,len(spiValGrp_CSR_BITS.getChildren())):
        valueName = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_BITS.getChildren()[id].getAttribute("caption")
        spiSym_CSR_BITS.addKey(valueName, value, description)

    #SPI Transmit data register
    transmitRegister = spiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+spiInstanceName.getValue()+"_REGS->SPI_TDR)")
    transmitRegister.setVisible(False)

    #SPI Receive data register
    receiveRegister = spiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+spiInstanceName.getValue()+"_REGS->SPI_RDR)")
    receiveRegister.setVisible(False)

    #SPI 8-bit Character size Mask
    spiSym_CSR_BITS_8BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
    spiSym_CSR_BITS_8BIT.setDefaultValue("0x0")
    spiSym_CSR_BITS_8BIT.setVisible(False)

    #SPI 9-bit Character size Mask
    spiSym_CSR_BITS_9BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_9_BIT_MASK", None)
    spiSym_CSR_BITS_9BIT.setDefaultValue("0x10")
    spiSym_CSR_BITS_9BIT.setVisible(False)

    #SPI 10-bit Character size Mask
    spiSym_CSR_BITS_10BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_10_BIT_MASK", None)
    spiSym_CSR_BITS_10BIT.setDefaultValue("0x20")
    spiSym_CSR_BITS_10BIT.setVisible(False)

    #SPI 11-bit Character size Mask
    spiSym_CSR_BITS_11BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_11_BIT_MASK", None)
    spiSym_CSR_BITS_11BIT.setDefaultValue("0x30")
    spiSym_CSR_BITS_11BIT.setVisible(False)

    #SPI 12-bit Character size Mask
    spiSym_CSR_BITS_12BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_12_BIT_MASK", None)
    spiSym_CSR_BITS_12BIT.setDefaultValue("0x40")
    spiSym_CSR_BITS_12BIT.setVisible(False)

    #SPI 13-bit Character size Mask
    spiSym_CSR_BITS_13BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_13_BIT_MASK", None)
    spiSym_CSR_BITS_13BIT.setDefaultValue("0x50")
    spiSym_CSR_BITS_13BIT.setVisible(False)

    #SPI 14-bit Character size Mask
    spiSym_CSR_BITS_14BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_14_BIT_MASK", None)
    spiSym_CSR_BITS_14BIT.setDefaultValue("0x60")
    spiSym_CSR_BITS_14BIT.setVisible(False)

    #SPI 15-bit Character size Mask
    spiSym_CSR_BITS_15BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_15_BIT_MASK", None)
    spiSym_CSR_BITS_15BIT.setDefaultValue("0x70")
    spiSym_CSR_BITS_15BIT.setVisible(False)

    #SPI 16-bit Character size Mask
    spiSym_CSR_BITS_16BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", None)
    spiSym_CSR_BITS_16BIT.setDefaultValue("0x80")
    spiSym_CSR_BITS_16BIT.setVisible(False)

    spiSymDummyData = spiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
    spiSymDummyData.setLabel("Dummy Data")
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setMin(0x0)
    spiSymDummyData.setDependencies(DummyData_ValueUpdate, ["SPI_CHARSIZE_BITS", "SPI_MR_MSTR"])

    spiSym_CSR_CPOL = spiComponent.createKeyValueSetSymbol("SPI_CLOCK_POLARITY", None)
    spiSym_CSR_CPOL.setLabel(spiBitField_CSR_CPOL.getAttribute("caption"))
    spiSym_CSR_CPOL.setOutputMode("Key")
    spiSym_CSR_CPOL.setDisplayMode("Description")
    spiSym_CSR_CPOL.setDefaultValue(0)

    for id in range(0, len(spiValGrp_CSR_CPOL.getChildren())):
        valueName = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_CPOL.getChildren()[id].getAttribute("caption")
        spiSym_CSR_CPOL.addKey(valueName, value, description)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CSR_CPOL_IL_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CSR_CPOL_IL_Mask.setDefaultValue("0x0")
    spiSym_CSR_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CSR_CPOL_IH_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CSR_CPOL_IH_Mask.setDefaultValue("0x1")
    spiSym_CSR_CPOL_IH_Mask.setVisible(False)

    spiSym_CSR_NCPHA = spiComponent.createKeyValueSetSymbol("SPI_CLOCK_PHASE", None)
    spiSym_CSR_NCPHA.setLabel(spiBitField_CSR_NCPHA.getAttribute("caption"))
    spiSym_CSR_NCPHA.setOutputMode("Key")
    spiSym_CSR_NCPHA.setDisplayMode("Description")
    spiSym_CSR_NCPHA.setDefaultValue(0)
    spiSym_CSR_NCPHA.setVisible(True)

    for id in range(0, len(spiValGrp_CSR_NCPHA.getChildren())):
        valueName = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("name")
        value = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("value")
        description = spiValGrp_CSR_NCPHA.getChildren()[id].getAttribute("caption")
        spiSym_CSR_NCPHA.addKey(valueName, value, description)

    spiSymClockModeComment = spiComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", None)
    spiSymClockModeComment.setLabel("***SPI Mode 0 is Selected***")
    spiSymClockModeComment.setDependencies(ClockModeInfo, ["SPI_CLOCK_POLARITY","SPI_CLOCK_PHASE"])

    spisSym_TXBuffer_Size = spiComponent.createIntegerSymbol("SPIS_TX_BUFFER_SIZE", None)
    spisSym_TXBuffer_Size.setLabel("TX Buffer Size (in bytes)")
    spisSym_TXBuffer_Size.setMin(0)
    spisSym_TXBuffer_Size.setMax(65535)
    spisSym_TXBuffer_Size.setDefaultValue(256)
    spisSym_TXBuffer_Size.setVisible(False)
    spisSym_TXBuffer_Size.setDependencies(showSlaveDependencies, ["SPI_MR_MSTR"])

    spisSym_RXBuffer_Size = spiComponent.createIntegerSymbol("SPIS_RX_BUFFER_SIZE", None)
    spisSym_RXBuffer_Size.setLabel("RX Buffer Size (in bytes)")
    spisSym_RXBuffer_Size.setMin(0)
    spisSym_RXBuffer_Size.setMax(65535)
    spisSym_RXBuffer_Size.setDefaultValue(256)
    spisSym_RXBuffer_Size.setVisible(False)
    spisSym_RXBuffer_Size.setDependencies(showSlaveDependencies, ["SPI_MR_MSTR"])

    spisSymUseBusyPin = spiComponent.createBooleanSymbol("SPIS_USE_BUSY_PIN", None)
    spisSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
    spisSymUseBusyPin.setDefaultValue(True)
    spisSymUseBusyPin.setVisible(False)
    spisSymUseBusyPin.setDependencies(showSlaveDependencies, ["SPI_MR_MSTR"])

    spisSymBusyPin = spiComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN", spisSymUseBusyPin)
    spisSymBusyPin.setVisible(False)
    spisSymBusyPin.setLabel("Slave Busy Pin")
    spisSymBusyPin.setOutputMode("Key")
    spisSymBusyPin.setDisplayMode("Description")
    spisSymBusyPin.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MR_MSTR", "SPIS_USE_BUSY_PIN"])

    availablePinDictionary = {}

    # Send message to core to get available pins
    availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

    for pad in sort_alphanumeric(availablePinDictionary.values()):
        key = pad
        value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
        description = pad
        spisSymBusyPin.addKey(key, value, description)

    #SPI Character Size
    spisSymBusyPinLogicLevel = spiComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN_LOGIC_LEVEL", spisSymUseBusyPin)
    spisSymBusyPinLogicLevel.setLabel("Slave Busy Pin Logic Level")
    spisSymBusyPinLogicLevel.setVisible(False)
    spisSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    spisSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    spisSymBusyPinLogicLevel.setDefaultValue(1)
    spisSymBusyPinLogicLevel.setOutputMode("Key")
    spisSymBusyPinLogicLevel.setDisplayMode("Description")
    spisSymBusyPinLogicLevel.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MR_MSTR", "SPIS_USE_BUSY_PIN"])

    spisSymBusyPinConfigComment = spiComponent.createCommentSymbol("SPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT", spisSymUseBusyPin)
    spisSymBusyPinConfigComment.setVisible(False)
    spisSymBusyPinConfigComment.setLabel("***Above selected Busy pin must be configured as GPIO Output in Pin Manager***")
    spisSymBusyPinConfigComment.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MR_MSTR", "SPIS_USE_BUSY_PIN"])


    #SPI Clock Phase Leading Edge Mask
    spiSym_CSR_NCPHA_TE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CSR_NCPHA_TE_Mask.setDefaultValue("0x0")
    spiSym_CSR_NCPHA_TE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CSR_NCPHA_LE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CSR_NCPHA_LE_Mask.setDefaultValue("0x2")
    spiSym_CSR_NCPHA_LE_Mask.setVisible(False)

    #SPI Status OVERRUN Mask
    spiSym_SR_OVERES_Mask = spiComponent.createStringSymbol("SPI_STATUS_OVERRUN_MASK", None)
    spiSym_SR_OVERES_Mask.setDefaultValue("0x8")
    spiSym_SR_OVERES_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = spiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue(spiInstanceName.getValue())
    spiSym_API_Prefix.setVisible(False)

    # Dependency Status for interrupt
    global spiSymIntEnComment
    spiSymIntEnComment = spiComponent.createCommentSymbol(spiInstanceName.getValue() + "_NVIC_ENABLE_COMMENT", None)
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setDependencies(InterruptStatusWarning, ["core." + spiSyminterruptVectorUpdate])

    # Dependency Status for clock
    spiSymClkEnComment = spiComponent.createCommentSymbol(spiInstanceName.getValue() + "_CLK_ENABLE_COMMENT", None)
    spiSymClkEnComment.setVisible(False)
    spiSymClkEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    spiSymClkEnComment.setDependencies(ClockStatusWarning, ["core."+ spiInstanceName.getValue() + "_CLOCK_ENABLE"])

    # Warning message when PLIB is configured in non-interrupt mode but used with driver.
    global spiInterruptDriverModeComment
    spiInterruptDriverModeComment = spiComponent.createCommentSymbol("SPI_INT_DRIVER_COMMENT", None)
    spiInterruptDriverModeComment.setVisible(False)
    spiInterruptDriverModeComment.setLabel("Warning!!! SPI PLIB to be used with driver, must be configured in interrupt mode")

    configName = Variables.get("__CONFIGURATION_NAME")

    spimCommonHeaderFile = spiComponent.createFileSymbol("SPI_COMMON_HEADER", None)
    spimCommonHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spi_master_common.h")
    spimCommonHeaderFile.setOutputName("plib_spi_master_common.h")
    spimCommonHeaderFile.setDestPath("peripheral/spi/spi_master")
    spimCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_master")
    spimCommonHeaderFile.setType("HEADER")
    spimCommonHeaderFile.setMarkup(False)
    spimCommonHeaderFile.setOverwrite(True)
    spimCommonHeaderFile.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "MASTER")
    spimCommonHeaderFile.setDependencies(spiMasterModeFileGeneration, ["SPI_MR_MSTR"])

    spimHeaderFile = spiComponent.createFileSymbol("SPI_HEADER", None)
    spimHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spix_master.h.ftl")
    spimHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_master.h")
    spimHeaderFile.setDestPath("/peripheral/spi/spi_master")
    spimHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_master")
    spimHeaderFile.setType("HEADER")
    spimHeaderFile.setMarkup(True)
    spimHeaderFile.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "MASTER")
    spimHeaderFile.setDependencies(spiMasterModeFileGeneration, ["SPI_MR_MSTR"])

    spimSource1File = spiComponent.createFileSymbol("SPI_SOURCE", None)
    spimSource1File.setSourcePath("../peripheral/spi_6088/templates/plib_spix_master.c.ftl")
    spimSource1File.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_master.c")
    spimSource1File.setDestPath("/peripheral/spi/spi_master")
    spimSource1File.setProjectPath("config/" + configName +"/peripheral/spi/spi_master")
    spimSource1File.setType("SOURCE")
    spimSource1File.setMarkup(True)
    spimSource1File.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "MASTER")
    spimSource1File.setDependencies(spiMasterModeFileGeneration, ["SPI_MR_MSTR"])

    spisCommonHeaderFile = spiComponent.createFileSymbol("SPIS_COMMON_HEADER", None)
    spisCommonHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spi_slave_common.h")
    spisCommonHeaderFile.setOutputName("plib_spi_slave_common.h")
    spisCommonHeaderFile.setDestPath("peripheral/spi/spi_slave")
    spisCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_slave")
    spisCommonHeaderFile.setType("HEADER")
    spisCommonHeaderFile.setMarkup(False)
    spisCommonHeaderFile.setOverwrite(True)
    spisCommonHeaderFile.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "SLAVE")
    spisCommonHeaderFile.setDependencies(spiSlaveModeFileGeneration, ["SPI_MR_MSTR"])

    spisHeaderFile = spiComponent.createFileSymbol("SPIS_HEADER", None)
    spisHeaderFile.setSourcePath("../peripheral/spi_6088/templates/plib_spix_slave.h.ftl")
    spisHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_slave.h")
    spisHeaderFile.setDestPath("/peripheral/spi/spi_slave")
    spisHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_slave")
    spisHeaderFile.setType("HEADER")
    spisHeaderFile.setMarkup(True)
    spisHeaderFile.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "SLAVE")
    spisHeaderFile.setDependencies(spiSlaveModeFileGeneration, ["SPI_MR_MSTR"])

    spisSource1File = spiComponent.createFileSymbol("SPIS_SOURCE", None)
    spisSource1File.setSourcePath("../peripheral/spi_6088/templates/plib_spix_slave.c.ftl")
    spisSource1File.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_slave.c")
    spisSource1File.setDestPath("/peripheral/spi/spi_slave")
    spisSource1File.setProjectPath("config/" + configName +"/peripheral/spi/spi_slave")
    spisSource1File.setType("SOURCE")
    spisSource1File.setMarkup(True)
    spisSource1File.setEnabled(spiSym_MR_MSTR.getSelectedKey() == "SLAVE")
    spisSource1File.setDependencies(spiSlaveModeFileGeneration, ["SPI_MR_MSTR"])

    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_6088/templates/system/initialization.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_6088/templates/system/definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)