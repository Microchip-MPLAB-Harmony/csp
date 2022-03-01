# coding: utf-8
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
global sort_alphanumeric
global updateCSR_SCBR_Value

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def handleMessage(messageID, args):
    global mcspiSym_MR_MSTR
    global mcspiInterrupt
    result_dict = {}

    if (messageID == "MCSPI_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            mcspiSym_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            mcspiSym_MR_MSTR.setValue("Master")

    elif (messageID == "MCSPI_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            mcspiSym_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            mcspiSym_MR_MSTR.setValue("Slave")

    elif (messageID == "MCSPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            mcspiInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            mcspiInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            mcspiInterrupt.setVisible(args["isVisible"])

    #elif (messageID == "MCSPI_SLAVE_INTERRUPT_MODE"):
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

mcspiBitField_CR_FIFOEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_CR"]/bitfield@[name="FIFOEN"]')
mcspiBitField_MR_MSTR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_MR"]/bitfield@[name="MSTR"]')
mcspiBitField_MR_PCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_MR"]/bitfield@[name="PCS"]')
mcspiBitField_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_CSR"]/bitfield@[name="BITS"]')
mcspiValGrp_CSR_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/value-group@[name="MCSPI_CSR__BITS"]')
mcspiBitField_CSR_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_CSR"]/bitfield@[name="CPOL"]')
mcspiBitField_CSR_NCPHA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="MCSPI"]/register-group@[name="MCSPI"]/register@[name="MCSPI_CSR"]/bitfield@[name="NCPHA"]')

# clock frequency symbol update callback
def MCSPISourceClockChanged(symbol, event):

    if event["id"] == "MCSPI_MR_MSTR":
        mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
        symbol.setVisible(mcspiMode == "MASTER")
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

    global mcspiInterrupt

    if mcspiInterrupt.getValue() == True:
       symbol.setVisible(event["value"])

# Dependency Function for symbol visibility
def updateMCSPIDMAConfigurationVisbleProperty(symbol, event):
    symbol.setVisible(event["value"])

def setupSpiIntSymbolAndIntHandler(mcspiInterrupt, event):
    global mcspiSyminterruptVector
    global mcspiSyminterruptHandler
    global mcspiSyminterruptHandlerLock
    global mcspiSyminterruptVectorUpdate
    global mcspiSymIntEnComment
    global mcspiSym_MR_PCS
    global mcspiDriverControlled
    global mcspiInterruptDriverModeComment

    if(event["id"] == "MCSPI_INTERRUPT_MODE"):
        Database.clearSymbolValue("core", mcspiSyminterruptVector)
        Database.clearSymbolValue("core", mcspiSyminterruptHandler)
        Database.clearSymbolValue("core", mcspiSyminterruptHandlerLock)

        if (event["value"] == True):
            Database.setSymbolValue("core", mcspiSyminterruptVector, True, 1)
            Database.setSymbolValue("core", mcspiSyminterruptHandler, mcspiInstanceName.getValue() + "_InterruptHandler", 1)
            Database.setSymbolValue("core", mcspiSyminterruptHandlerLock, True, 1)
        else:
            Database.setSymbolValue("core", mcspiSyminterruptVector, False, 1)
            Database.setSymbolValue("core", mcspiSyminterruptHandler, mcspiInstanceName.getValue() + "_Handler", 1)
            Database.setSymbolValue("core", mcspiSyminterruptHandlerLock, False, 1)
    elif (event["id"] == "MCSPI_MR_MSTR"):
        mcspiInterrupt.setReadOnly(event["symbol"].getValue() == "SLAVE")
        if event["symbol"].getValue() == "SLAVE":
            mcspiInterrupt.setValue(True)


def getMasterClockFreq():

    clkSymMasterClockFreq = Database.getSymbolValue(mcspiInstanceName.getValue().lower(), "MCSPI_MASTER_CLOCK")
    return int(clkSymMasterClockFreq)

def mcspiMasterModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "MASTER")

def mcspiSlaveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "SLAVE")

def chipSelectUpdateOnModeChange(symbol, event):

    mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()

    if (mcspiMode == "SLAVE"):
        symbol.setReadOnly(True)
        symbol.setValue(0)
    else:
        symbol.setReadOnly(False)

def showSlaveDependencies(symbol, event):

    mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    symbol.setVisible(mcspiMode == "SLAVE")

def showMasterDependencies(mcspiSym_MR_Dependencies, event):

    if event["symbol"].getKey(event["value"]) == "MASTER":
        mcspiSym_MR_Dependencies.setVisible(True)
    else:
        mcspiSym_MR_Dependencies.setVisible(False)

def updateMCSPISlaveBusyPinVisibility(symbol, event):

    mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    busyPinEnabled = event["source"].getSymbolByID("MCSPIS_USE_BUSY_PIN").getValue() == True
    symbol.setVisible(mcspiMode == "SLAVE" and busyPinEnabled == True)

def updateCSR_SCBR_Value(symbol, baudVal, clockVal):
    SCBR = clockVal/baudVal
    mcspiSymInvalidClock.setVisible(SCBR < 1 or SCBR > 255)

    if SCBR == 0:
        SCBR = 1
    elif SCBR > 255:
        SCBR = 255

    symbol.setValue(SCBR, 1)

def updateCSRx_SCBR_Value(symbol, event):

    csx = symbol.getID()[7]
    if event["id"] == "MCSPI_MASTER_CLOCK":
        clk = int(event["value"])
        baud = Database.getSymbolValue(mcspiInstanceName.getValue().lower(), "MCSPI_CSR" + csx + "_BAUD_RATE")
    else:
        #This means there is change in baud rate provided by user in GUI
        baud = event["value"]
        clk = int(Database.getSymbolValue(mcspiInstanceName.getValue().lower(), "MCSPI_MASTER_CLOCK"))

    updateCSR_SCBR_Value(symbol, baud, clk)

def calculateCSRIndex(mcspiSymCSRIndex, event):

    mcspiSymCSRIndex.setValue(int(event["symbol"].getKeyValue(event["value"])[-1]), 1)

def DummyData_ValueUpdate(mcspiSymDummyData, event):

    mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    mcspiSymDummyData.setVisible(mcspiMode == "MASTER")

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def fifoModeVisible (symbol, event):

    if mcspiBitField_CR_FIFOEN != None:

        mcspiMode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
        interruptMode = event["source"].getSymbolByID("MCSPI_INTERRUPT_MODE").getValue()

        if mcspiMode == "SLAVE":
            symbol.setReadOnly(True)
            symbol.setVisible(True)
            symbol.setValue(True)
        else:
            if interruptMode == True:
                symbol.setReadOnly(False)
                symbol.setVisible(True)
            else:
                symbol.setVisible(False)

def updateNumCSR(symbol, event):
    en_npcs0 = 0
    en_npcs1 = 0
    en_npcs2 = 0
    en_npcs3 = 0

    en_npcs0 = event["source"].getSymbolByID("MCSPI_EN_NPCS0").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS1") != None:
        en_npcs1 = event["source"].getSymbolByID("MCSPI_EN_NPCS1").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS2") != None:
        en_npcs2 = event["source"].getSymbolByID("MCSPI_EN_NPCS2").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS3") != None:
        en_npcs3 = event["source"].getSymbolByID("MCSPI_EN_NPCS3").getValue()

    symbol.setValue(en_npcs0 + en_npcs1 + en_npcs2 + en_npcs3)

def updateCSRIndex(symbol, event):
    en_npcs0 = 0
    en_npcs1 = 0
    en_npcs2 = 0
    en_npcs3 = 0

    en_npcs0 = event["source"].getSymbolByID("MCSPI_EN_NPCS0").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS1") != None:
        en_npcs1 = event["source"].getSymbolByID("MCSPI_EN_NPCS1").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS2") != None:
        en_npcs2 = event["source"].getSymbolByID("MCSPI_EN_NPCS2").getValue()

    if event["source"].getSymbolByID("MCSPI_EN_NPCS3") != None:
        en_npcs3 = event["source"].getSymbolByID("MCSPI_EN_NPCS3").getValue()

# The value of this symbol is valid only if only one CS is enabled. So, set the value of the symbol that is enabled and break.
    if en_npcs0 == True:
        symbol.setValue(0)
    elif en_npcs1 == True:
        symbol.setValue(1)
    elif en_npcs2 == True:
        symbol.setValue(2)
    elif en_npcs3 == True:
        symbol.setValue(3)

def npcs0EnableVisible(symbol, event):
    mcspi_mode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    if mcspi_mode == "MASTER":
        symbol.setLabel("Enable NPCS0/ Use GPIO?")
        symbol.setReadOnly(False)
    else:
        symbol.setLabel("Enable NPCS0")
        symbol.setValue(True)
        symbol.setReadOnly(True)

def npcsxEnableVisible(symbol, event):
    mcspi_mode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    symbol.setVisible(mcspi_mode == "MASTER")

def updateCSRx_MasterBitFields(symbol, event):
    csx = symbol.getID()[7]
    mcspi_mode = event["source"].getSymbolByID("MCSPI_MR_MSTR").getValue()
    en_npcsx = event["source"].getSymbolByID("MCSPI_EN_NPCS" + csx).getValue()
    symbol.setVisible(mcspi_mode == "MASTER" and en_npcsx == True)

def updateCSRx_BitFields(symbol, event):
    symbol.setVisible(event["value"] == True)

def updateCSRxClockModeInfo(symbol, event):
    # visibility
    csx = symbol.getID()[7]
    en_npcsx = event["source"].getSymbolByID("MCSPI_EN_NPCS" + csx).getValue()
    symbol.setVisible(en_npcsx == True)

    NCPHA = int (event["source"].getSymbolByID("MCSPI_CSR" + csx + "_NCPHA").getSelectedValue(), 16)
    CPOL = int (event["source"].getSymbolByID("MCSPI_CSR" + csx + "_CPOL").getSelectedValue(), 16)
    if (CPOL == 0) and (NCPHA == 0):
        symbol.setLabel("***MCSPI Mode 1 is Selected***")
    elif (CPOL == 0) and (NCPHA == 1):
        symbol.setLabel("***MCSPI Mode 0 is Selected***")
    elif (CPOL == 1) and (NCPHA == 0):
        symbol.setLabel("***MCSPI Mode 3 is Selected***")
    else:
        symbol.setLabel("***MCSPI Mode 2 is Selected***")

def updatePCSFromDatabase(symbol, event):
    if symbol.getReadOnly() == False:
        cs_val = symbol.getSelectedKey()
        if cs_val == "NPCS0" or cs_val == "GPIO":
            event["source"].getSymbolByID("MCSPI_EN_NPCS0").setValue(True)
        elif cs_val == "NPCS1":
            event["source"].getSymbolByID("MCSPI_EN_NPCS1").setValue(True)
            event["source"].getSymbolByID("MCSPI_EN_NPCS0").setValue(False)
        elif cs_val == "NPCS2":
            event["source"].getSymbolByID("MCSPI_EN_NPCS2").setValue(True)
            event["source"].getSymbolByID("MCSPI_EN_NPCS0").setValue(False)
        elif cs_val == "NPCS3":
            event["source"].getSymbolByID("MCSPI_EN_NPCS3").setValue(True)
            event["source"].getSymbolByID("MCSPI_EN_NPCS0").setValue(False)
        # Clear off the comment symbol aswell
        event["source"].getSymbolByID("MCSPI_CLOCK_MODE_COMMENT").setVisible(False)
        symbol.setVisible(False)
        symbol.setReadOnly(True)

def updateBaudRateFromDatabase(symbol, event):
    if symbol.getReadOnly() == False:
        cs_val = mcspiSym_MR_PCS.getSelectedKey()
        if cs_val == "NPCS0" or cs_val == "GPIO":
            event["source"].getSymbolByID("MCSPI_CSR0_BAUD_RATE").setValue(symbol.getValue())
        elif cs_val == "NPCS1":
            event["source"].getSymbolByID("MCSPI_CSR1_BAUD_RATE").setValue(symbol.getValue())
        elif cs_val == "NPCS2":
            event["source"].getSymbolByID("MCSPI_CSR2_BAUD_RATE").setValue(symbol.getValue())
        elif cs_val == "NPCS3":
            event["source"].getSymbolByID("MCSPI_CSR3_BAUD_RATE").setValue(symbol.getValue())
        symbol.setVisible(False)
        symbol.setReadOnly(True)

def updateBITSFromDatabase(symbol, event):
    if symbol.getReadOnly() == False:
        cs_val = mcspiSym_MR_PCS.getSelectedKey()
        if cs_val == "NPCS0" or cs_val == "GPIO":
            event["source"].getSymbolByID("MCSPI_CSR0_BITS").setValue(symbol.getValue())
        elif cs_val == "NPCS1":
            event["source"].getSymbolByID("MCSPI_CSR1_BITS").setValue(symbol.getValue())
        elif cs_val == "NPCS2":
            event["source"].getSymbolByID("MCSPI_CSR2_BITS").setValue(symbol.getValue())
        elif cs_val == "NPCS3":
            event["source"].getSymbolByID("MCSPI_CSR3_BITS").setValue(symbol.getValue())
        symbol.setVisible(False)
        symbol.setReadOnly(True)

def updateCPOLFromDatabase(symbol, event):
    if symbol.getReadOnly() == False:
        cs_val = mcspiSym_MR_PCS.getSelectedKey()
        if cs_val == "NPCS0" or cs_val == "GPIO":
            event["source"].getSymbolByID("MCSPI_CSR0_CPOL").setValue(symbol.getValue())
        elif cs_val == "NPCS1":
            event["source"].getSymbolByID("MCSPI_CSR1_CPOL").setValue(symbol.getValue())
        elif cs_val == "NPCS2":
            event["source"].getSymbolByID("MCSPI_CSR2_CPOL").setValue(symbol.getValue())
        elif cs_val == "NPCS3":
            event["source"].getSymbolByID("MCSPI_CSR3_CPOL").setValue(symbol.getValue())
        symbol.setVisible(False)
        symbol.setReadOnly(True)

def updateNCPHAFromDatabase(symbol, event):
    if symbol.getReadOnly() == False:
        cs_val = mcspiSym_MR_PCS.getSelectedKey()
        if cs_val == "NPCS0" or cs_val == "GPIO":
            event["source"].getSymbolByID("MCSPI_CSR0_NCPHA").setValue(symbol.getValue())
        elif cs_val == "NPCS1":
            event["source"].getSymbolByID("MCSPI_CSR1_NCPHA").setValue(symbol.getValue())
        elif cs_val == "NPCS2":
            event["source"].getSymbolByID("MCSPI_CSR2_NCPHA").setValue(symbol.getValue())
        elif cs_val == "NPCS3":
            event["source"].getSymbolByID("MCSPI_CSR3_NCPHA").setValue(symbol.getValue())

        symbol.setVisible(False)
        symbol.setReadOnly(True)


def instantiateComponent(mcspiComponent):

    global mcspiInstanceName
    global mcspiSyminterruptVector
    global mcspiSyminterruptHandler
    global mcspiSyminterruptHandlerLock
    global mcspiSyminterruptVectorUpdate
    global InternalinterruptVectorChange
    global mcspiSym_MR_MSTR
    global mcspi_CSR_Count

    InternalinterruptVectorChange = False

    mcspiInstanceName = mcspiComponent.createStringSymbol("MCSPI_INSTANCE_NAME", None)
    mcspiInstanceName.setVisible(False)
    mcspiInstanceName.setDefaultValue(mcspiComponent.getID().upper())

    localComponent = mcspiInstanceName.getComponent()

    #IDs used in NVIC Manager
    mcspiSyminterruptVector = mcspiInstanceName.getValue() + "_INTERRUPT_ENABLE"
    mcspiSyminterruptHandler = mcspiInstanceName.getValue() + "_INTERRUPT_HANDLER"
    mcspiSyminterruptHandlerLock = mcspiInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    mcspiSyminterruptVectorUpdate = mcspiInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Enable clock for MCSPI
    Database.setSymbolValue("core", mcspiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    global mcspiDriverControlled
    mcspiDriverControlled = mcspiComponent.createBooleanSymbol("MCSPI_DRIVER_CONTROLLED", None)
    mcspiDriverControlled.setVisible(False)

    global mcspiInterrupt
    mcspiInterrupt = mcspiComponent.createBooleanSymbol("MCSPI_INTERRUPT_MODE", None)
    mcspiInterrupt.setLabel("Interrupt Mode")
    mcspiInterrupt.setDefaultValue(True)

    #By Default interrupt mode is enabled and corresponding information is passed to NVIC manager
    Database.setSymbolValue("core", mcspiSyminterruptVector, True, 1)
    Database.setSymbolValue("core", mcspiSyminterruptHandler, mcspiInstanceName.getValue() + "_InterruptHandler", 1)
    Database.setSymbolValue("core", mcspiSyminterruptHandlerLock, True, 1)
    mcspiInterrupt.setDependencies(setupSpiIntSymbolAndIntHandler, ["MCSPI_INTERRUPT_MODE", "MCSPI_MR_MSTR"])

    mcspiRegisterGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCSPI\"]/register-group@[name=\"MCSPI\"]")
    mcspiRegisterList = mcspiRegisterGroup.getChildren()
    for index in range(0, len(mcspiRegisterList)):
        if (mcspiRegisterList[index].getAttribute("name") == "MCSPI_RPR"):
            mcspiDMAEnable = mcspiComponent.createBooleanSymbol("USE_MCSPI_DMA", None)
            mcspiDMAEnable.setLabel("Enable DMA for Transmit and Receive")
            mcspiDMAEnable.setDependencies(updateMCSPIDMAConfigurationVisbleProperty, ["MCSPI_INTERRUPT_MODE"])
            break

    mcspiModeValues = ["MASTER", "SLAVE"]
    mcspiSym_MR_MSTR = mcspiComponent.createComboSymbol("MCSPI_MR_MSTR", None, mcspiModeValues)
    mcspiSym_MR_MSTR.setLabel(mcspiBitField_MR_MSTR.getAttribute("caption"))
    mcspiSym_MR_MSTR.setDefaultValue(mcspiModeValues[0])
    mcspiSym_MR_MSTR.setReadOnly(False)

    # Provide a source clock selection symbol for masks that supports it
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCSPI\"]/value-group@[name=\"MCSPI_MR__BRSRCCLK\"]")
    if valueGroup != None:
        values = valueGroup.getChildren()

        mcspiSymClockSrc = mcspiComponent.createKeyValueSetSymbol("MCSPI_CLK_SRC", None)
        mcspiSymClockSrc.setLabel(valueGroup.getAttribute("caption"))

        for index in range(len(values)):
            mcspiSymClockSrc.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"), values[index].getAttribute("caption"))

        mcspiSymClockSrc.setOutputMode("Key")
        mcspiSymClockSrc.setDisplayMode("Key")

    # Used to pass master clock frequency to MCSPI FTL
    mcspiSymMasterClock = mcspiComponent.createIntegerSymbol("MCSPI_MASTER_CLOCK", None)
    mcspiSymMasterClock.setLabel("Bit rate source clock frequency (Hz)")
    mcspiSymMasterClock.setDefaultValue(Database.getSymbolValue("core", mcspiInstanceName.getValue() + "_CLOCK_FREQUENCY" ))
    mcspiSymMasterClock.setReadOnly(True)
    mcspiSymMasterClock.setDependencies(MCSPISourceClockChanged, ["core." + mcspiInstanceName.getValue() + "_CLOCK_FREQUENCY", "MCSPI_MR_MSTR"])

    global mcspiSymInvalidClock
    mcspiSymInvalidClock = mcspiComponent.createCommentSymbol("MCSPI_CLOCK_INVALID_COMMENT", None)
    mcspiSymInvalidClock.setLabel("!!! Cannot generate input baud rate from the configured source clock frequency !!!")
    mcspiSymInvalidClock.setVisible(False)

    mcspiSym_MCSPI_CSR_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCSPI\"]/register-group/register@[name=\"MCSPI_CSR\"]")
    mcspi_CSR_Count = int(mcspiSym_MCSPI_CSR_Node.getAttribute('count'),10)

# MR PCS (Unused, maintained for backward compatibility)
    DefaultPCS = 0
    global mcspiSym_MR_PCS
    mcspiSym_MR_PCS = mcspiComponent.createKeyValueSetSymbol("MCSPI_MR_PCS", None)
    mcspiSym_MR_PCS.setLabel(mcspiBitField_MR_PCS.getAttribute("caption"))
    mcspiSym_MR_PCS.setOutputMode("Key")
    mcspiSym_MR_PCS.setDisplayMode("Key")
    mcspiSym_MR_PCS.setDefaultValue(DefaultPCS)
    mcspiSym_MR_PCS.setVisible(False)
    mcspiSym_MR_PCS.setDependencies(chipSelectUpdateOnModeChange, ["MCSPI_MR_MSTR"])

    mcspiSym_MR_PCS.addKey("NPCS0", "0", "NPCS0 as Chip Select")
    mcspiSym_MR_PCS.addKey("NPCS1", "1", "NPCS1 as Chip Select")
    # When User wants to control his chip select himself (through some GPIO pin),
    # then all the NPCSx lines are free to be used as PIO pins. But in MR_PCS
    # field, one of the NPCS lines still has to be selected in order to decide
    # which MSPI_CSRx register will be active. Here we have used NPCS0 selection
    # for such case, it can be changed to any other NPCSx line without affecting
    # the user.
    mcspiSym_MR_PCS.addKey("GPIO", "0", "User Controlled Chip Select Through GPIO Pin")
    mcspiSym_MR_PCS.addKey("DUMMY", "2", "Dummy")
    defaultIndex = int(mcspiSym_MR_PCS.getKey(DefaultPCS)[-1])
    mcspiSym_MR_PCS.setDependencies(updatePCSFromDatabase, ["MCSPI_MR_PCS"])

# MR DLYBCS
    mcspiSym_MCSPI_MR_DLYBCS = mcspiComponent.createIntegerSymbol("MCSPI_MR_DLYBCS", None)
    mcspiSym_MCSPI_MR_DLYBCS.setLabel("Delay between chip selects")
    mcspiSym_MCSPI_MR_DLYBCS.setMax(255)
    mcspiSym_MCSPI_MR_DLYBCS.setDefaultValue(0)
    mcspiSym_MCSPI_MR_DLYBCS.setVisible(True)
    mcspiSym_MCSPI_MR_DLYBCS.setDependencies(showMasterDependencies, ["MCSPI_MR_MSTR"])

# FIFO Mode
    mcspiSymFIFOEnable = mcspiComponent.createBooleanSymbol("MCSPI_FIFO_ENABLE", None)
    mcspiSymFIFOEnable.setLabel("Enable FIFO")
    mcspiSymFIFOEnable.setDefaultValue(False)
    mcspiSymFIFOEnable.setVisible(mcspiBitField_CR_FIFOEN != None)
    mcspiSymFIFOEnable.setDependencies(fifoModeVisible, ["MCSPI_INTERRUPT_MODE", "MCSPI_MR_MSTR"])

# Slave mode TX Buffer Size
    mcspiSym_TXBuffer_Size = mcspiComponent.createIntegerSymbol("MCSPIS_TX_BUFFER_SIZE", None)
    mcspiSym_TXBuffer_Size.setLabel("TX Buffer Size (in bytes)")
    mcspiSym_TXBuffer_Size.setMin(0)
    mcspiSym_TXBuffer_Size.setMax(65535)
    mcspiSym_TXBuffer_Size.setDefaultValue(256)
    mcspiSym_TXBuffer_Size.setVisible(False)
    mcspiSym_TXBuffer_Size.setDependencies(showSlaveDependencies, ["MCSPI_MR_MSTR"])

# Slave mode RX Buffer Size
    mcspiSym_RXBuffer_Size = mcspiComponent.createIntegerSymbol("MCSPIS_RX_BUFFER_SIZE", None)
    mcspiSym_RXBuffer_Size.setLabel("RX Buffer Size (in bytes)")
    mcspiSym_RXBuffer_Size.setMin(0)
    mcspiSym_RXBuffer_Size.setMax(65535)
    mcspiSym_RXBuffer_Size.setDefaultValue(256)
    mcspiSym_RXBuffer_Size.setVisible(False)
    mcspiSym_RXBuffer_Size.setDependencies(showSlaveDependencies, ["MCSPI_MR_MSTR"])

    for i in range (mcspi_CSR_Count):
        # CSR0 Enable
        mcspiSym_MCSPI_EnableNPCSx = mcspiComponent.createBooleanSymbol("MCSPI_EN_NPCS" + str(i), None)
        mcspiSym_MCSPI_EnableNPCSx.setVisible(True)
        if i == 0:
            mcspiSym_MCSPI_EnableNPCSx.setDefaultValue(True)
            mcspiSym_MCSPI_EnableNPCSx.setLabel("Enable NPCS0/ Use GPIO?")
            mcspiSym_MCSPI_EnableNPCSx.setDependencies(npcs0EnableVisible, ["MCSPI_MR_MSTR"])
        else:
            mcspiSym_MCSPI_EnableNPCSx.setDefaultValue(False)
            mcspiSym_MCSPI_EnableNPCSx.setLabel("Enable NPCS" + str(i) + "?")
            mcspiSym_MCSPI_EnableNPCSx.setDependencies(npcsxEnableVisible, ["MCSPI_MR_MSTR"])

# MULTI CSR (True if more than one CSR is enabled)
    mcspiSym_MCSPI_NumCSR = mcspiComponent.createIntegerSymbol("MCSPI_NUM_CSR", None)
    mcspiSym_MCSPI_NumCSR.setDefaultValue(1)
    mcspiSym_MCSPI_NumCSR.setVisible(False)
    mcspiSym_MCSPI_NumCSR.setDependencies(updateNumCSR, ["MCSPI_EN_NPCS0", "MCSPI_EN_NPCS1", "MCSPI_EN_NPCS2", "MCSPI_EN_NPCS3"])

# CSR Index (points to the CSR index only when MULTI CSR is false)
    mcspiSymCSRIndex = mcspiComponent.createIntegerSymbol("MCSPI_CSR_INDEX", None)
    mcspiSymCSRIndex.setDefaultValue(defaultIndex)
    mcspiSymCSRIndex.setVisible(False)
    mcspiSymCSRIndex.setDependencies(updateCSRIndex, ["MCSPI_EN_NPCS0", "MCSPI_EN_NPCS1", "MCSPI_EN_NPCS2", "MCSPI_EN_NPCS3"])

    defaultbaudRate = 1000000
    defaultSCBR = int(Database.getSymbolValue("core", mcspiInstanceName.getValue() + "_CLOCK_FREQUENCY"))/defaultbaudRate

## Deprecated symbols ----------------------------------------------##

# BAUD RATE (Unused, maintained for backward compatibility)
    mcspiSym_CSR_SCBR = mcspiComponent.createIntegerSymbol("MCSPI_BAUD_RATE", None)
    mcspiSym_CSR_SCBR.setLabel("Baud Rate in Hz")
    mcspiSym_CSR_SCBR.setDefaultValue(defaultbaudRate)
    mcspiSym_CSR_SCBR.setMin(1)
    mcspiSym_CSR_SCBR.setVisible(False)
    mcspiSym_CSR_SCBR.setDependencies(updateBaudRateFromDatabase, ["MCSPI_BAUD_RATE"])

# BITS (Unused, maintained for backward compatibility)
    mcspiSym_CSR_BITS = mcspiComponent.createKeyValueSetSymbol("MCSPI_CHARSIZE_BITS", None)
    mcspiSym_CSR_BITS.setLabel(mcspiBitField_CSR_BITS.getAttribute("caption"))
    mcspiSym_CSR_BITS.setOutputMode("Key")
    mcspiSym_CSR_BITS.setDisplayMode("Description")
    mcspiSym_CSR_BITS.setDefaultValue(0)
    mcspiSym_CSR_BITS.setVisible(False)
    mcspiSym_CSR_BITS.setDependencies(updateBITSFromDatabase, ["MCSPI_CHARSIZE_BITS"])

    for id in range(0,len(mcspiValGrp_CSR_BITS.getChildren())):
        valueName = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("name")
        value = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("value")
        description = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("caption")
        mcspiSym_CSR_BITS.addKey(valueName, value, description)

# CPOL (Unused, maintained for backward compatibility)
    mcspiSym_CSR_CPOL = mcspiComponent.createKeyValueSetSymbol("MCSPI_CLOCK_POLARITY", None)
    mcspiSym_CSR_CPOL.setLabel(mcspiBitField_CSR_CPOL.getAttribute("caption"))
    mcspiSym_CSR_CPOL.setOutputMode("Value")
    mcspiSym_CSR_CPOL.setDisplayMode("Description")
    mcspiSym_CSR_CPOL.setDefaultValue(0)
    mcspiSym_CSR_CPOL.addKey("CPOL0", "0", "The inactive state value of SPCK is logic level zero (CPOL=0)")
    mcspiSym_CSR_CPOL.addKey("CPOL1", "1", "The inactive state value of SPCK is logic level one (CPOL=1)")
    mcspiSym_CSR_CPOL.setVisible(False)
    mcspiSym_CSR_CPOL.setDependencies(updateCPOLFromDatabase, ["MCSPI_CLOCK_POLARITY"])

# NCPHA (Unused, maintained for backward compatibility)
    mcspiSym_CSR_NCPHA = mcspiComponent.createKeyValueSetSymbol("MCSPI_CLOCK_PHASE", None)
    mcspiSym_CSR_NCPHA.setLabel(mcspiBitField_CSR_NCPHA.getAttribute("caption"))
    mcspiSym_CSR_NCPHA.setOutputMode("Value")
    mcspiSym_CSR_NCPHA.setDisplayMode("Description")
    mcspiSym_CSR_NCPHA.setDefaultValue(1)
    mcspiSym_CSR_NCPHA.addKey("NCPHA0", "0", "Data are changed on the leading edge of SPCK and captured on the following edge of SPCK (NCPHA=0)")
    mcspiSym_CSR_NCPHA.addKey("NCPHA1", "1", "Data are captured on the leading edge of SPCK and changed on the following edge of SPCK (NCPHA=1)")
    mcspiSym_CSR_NCPHA.setVisible(False)
    mcspiSym_CSR_NCPHA.setDependencies(updateNCPHAFromDatabase, ["MCSPI_CLOCK_PHASE"])

# CLOCK MODE Comment(Unused, maintained for backward compatibility)
    mcspiSymClockModeComment = mcspiComponent.createCommentSymbol("MCSPI_CLOCK_MODE_COMMENT", None)
    mcspiSymClockModeComment.setLabel("***SPI Mode 0 is Selected***")
    mcspiSymClockModeComment.setVisible(False)

## Deprecated symbols ----------------------------------------------##

    for i in range (mcspi_CSR_Count):
        # CSRx BAUD RATE
        mcspiSym_MCSPI_CSRx_Baudrate = mcspiComponent.createIntegerSymbol("MCSPI_CSR" + str(i) + "_BAUD_RATE", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_Baudrate.setLabel("Baud Rate (Hz)")
        mcspiSym_MCSPI_CSRx_Baudrate.setDefaultValue(defaultbaudRate)
        mcspiSym_MCSPI_CSRx_Baudrate.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_Baudrate.setDependencies(updateCSRx_MasterBitFields, ["MCSPI_MR_MSTR", "MCSPI_EN_NPCS" + str(i)])

        mcspiSym_MCSPI_CSRx_SCBR_VALUE = mcspiComponent.createIntegerSymbol("MCSPI_CSR" + str(i) + "_SCBR_VALUE", None)
        mcspiSym_MCSPI_CSRx_SCBR_VALUE.setDefaultValue(defaultSCBR)
        mcspiSym_MCSPI_CSRx_SCBR_VALUE.setReadOnly(True)
        mcspiSym_MCSPI_CSRx_SCBR_VALUE.setVisible(False)
        mcspiSym_MCSPI_CSRx_SCBR_VALUE.setDependencies(updateCSRx_SCBR_Value, ["MCSPI_CSR" + str(i) + "_BAUD_RATE", "MCSPI_MASTER_CLOCK"])

        # CSRx BITS
        mcspiSym_MCSPI_CSRx_BITS = mcspiComponent.createKeyValueSetSymbol("MCSPI_CSR" + str(i) + "_BITS", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_BITS.setLabel("Bits Per Transfer")
        mcspiSym_MCSPI_CSRx_BITS.setOutputMode("Key")
        mcspiSym_MCSPI_CSRx_BITS.setDisplayMode("Description")
        mcspiSym_MCSPI_CSRx_BITS.setDefaultValue(0)
        mcspiSym_MCSPI_CSRx_BITS.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_BITS.setDependencies(updateCSRx_BitFields, ["MCSPI_EN_NPCS" + str(i)])

        for id in range(0,len(mcspiValGrp_CSR_BITS.getChildren())):
            valueName = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("name")
            value = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("value")
            description = mcspiValGrp_CSR_BITS.getChildren()[id].getAttribute("caption")
            mcspiSym_MCSPI_CSRx_BITS.addKey(valueName, value, description)

        # CSRx CPOL
        mcspiSym_MCSPI_CSRx_CPOL = mcspiComponent.createKeyValueSetSymbol("MCSPI_CSR" + str(i) + "_CPOL", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_CPOL.setLabel("Clock Polarity")
        mcspiSym_MCSPI_CSRx_CPOL.setOutputMode("Value")
        mcspiSym_MCSPI_CSRx_CPOL.setDisplayMode("Description")
        mcspiSym_MCSPI_CSRx_CPOL.setDefaultValue(0)
        mcspiSym_MCSPI_CSRx_CPOL.addKey("CPOL0", "0", "The inactive state value of SPCK is logic level zero (CPOL=0)")
        mcspiSym_MCSPI_CSRx_CPOL.addKey("CPOL1", "1", "The inactive state value of SPCK is logic level one (CPOL=1)")
        mcspiSym_MCSPI_CSRx_CPOL.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_CPOL.setDependencies(updateCSRx_BitFields, ["MCSPI_EN_NPCS" + str(i)])

        # CSRx NCPHA
        mcspiSym_MCSPI_CSRx_NCPHA = mcspiComponent.createKeyValueSetSymbol("MCSPI_CSR" + str(i) + "_NCPHA", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_NCPHA.setLabel("Clock Phase")
        mcspiSym_MCSPI_CSRx_NCPHA.setOutputMode("Value")
        mcspiSym_MCSPI_CSRx_NCPHA.setDisplayMode("Description")
        mcspiSym_MCSPI_CSRx_NCPHA.setDefaultValue(1)
        mcspiSym_MCSPI_CSRx_NCPHA.addKey("NCPHA0", "0", "Data are changed on the leading edge of SPCK and captured on the following edge of SPCK (NCPHA=0)")
        mcspiSym_MCSPI_CSRx_NCPHA.addKey("NCPHA1", "1", "Data are captured on the leading edge of SPCK and changed on the following edge of SPCK (NCPHA=1)")
        mcspiSym_MCSPI_CSRx_NCPHA.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_NCPHA.setDependencies(updateCSRx_BitFields, ["MCSPI_EN_NPCS" + str(i)])

        # CSRx DLYBS
        mcspiSym_MCSPI_CSRx_DLYBS = mcspiComponent.createIntegerSymbol("MCSPI_CSR" + str(i) + "_DLYBS", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_DLYBS.setLabel("Delay before SPCK")
        mcspiSym_MCSPI_CSRx_DLYBS.setMax(255)
        mcspiSym_MCSPI_CSRx_DLYBS.setDefaultValue(0)
        mcspiSym_MCSPI_CSRx_DLYBS.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_DLYBS.setDependencies(updateCSRx_MasterBitFields, ["MCSPI_MR_MSTR", "MCSPI_EN_NPCS" + str(i)])

        # CSRx DLYBCT
        mcspiSym_MCSPI_CSRx_DLYBCT = mcspiComponent.createIntegerSymbol("MCSPI_CSR" + str(i) + "_DLYBCT", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_DLYBCT.setLabel("Delay between consecutive transfers")
        mcspiSym_MCSPI_CSRx_DLYBCT.setMax(255)
        mcspiSym_MCSPI_CSRx_DLYBCT.setDefaultValue(0)
        mcspiSym_MCSPI_CSRx_DLYBCT.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_DLYBCT.setDependencies(updateCSRx_MasterBitFields, ["MCSPI_MR_MSTR", "MCSPI_EN_NPCS" + str(i)])

        # CSRx CLOCK MODE Comment
        mcspiSym_MCSPI_CSRx_ClockModeComment = mcspiComponent.createCommentSymbol("MCSPI_CSR" + str(i) + "_CLOCK_MODE_COMMENT", localComponent.getSymbolByID("MCSPI_EN_NPCS" + str(i)))
        mcspiSym_MCSPI_CSRx_ClockModeComment.setLabel("***SPI Mode 0 is Selected***")
        mcspiSym_MCSPI_CSRx_ClockModeComment.setVisible(i == 0)
        mcspiSym_MCSPI_CSRx_ClockModeComment.setDependencies(updateCSRxClockModeInfo, ["MCSPI_EN_NPCS" + str(i), "MCSPI_CSR" + str(i) + "_CPOL", "MCSPI_CSR" + str(i) +"_NCPHA"])

    #MCSPI Transmit data register
    transmitRegister = mcspiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&("+mcspiInstanceName.getValue()+"_REGS->MCSPI_TDR)")
    transmitRegister.setVisible(False)

    #MCSPI Receive data register
    receiveRegister = mcspiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&("+mcspiInstanceName.getValue()+"_REGS->MCSPI_RDR)")
    receiveRegister.setVisible(False)

    #MCSPI 8-bit Character size Mask
    mcspiSym_CSR_BITS_8BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_8_BIT_MASK", None)
    mcspiSym_CSR_BITS_8BIT.setDefaultValue("0x0")
    mcspiSym_CSR_BITS_8BIT.setVisible(False)

    #MCSPI 9-bit Character size Mask
    mcspiSym_CSR_BITS_9BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_9_BIT_MASK", None)
    mcspiSym_CSR_BITS_9BIT.setDefaultValue("0x10")
    mcspiSym_CSR_BITS_9BIT.setVisible(False)

    #MCSPI 10-bit Character size Mask
    mcspiSym_CSR_BITS_10BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_10_BIT_MASK", None)
    mcspiSym_CSR_BITS_10BIT.setDefaultValue("0x20")
    mcspiSym_CSR_BITS_10BIT.setVisible(False)

    #MCSPI 11-bit Character size Mask
    mcspiSym_CSR_BITS_11BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_11_BIT_MASK", None)
    mcspiSym_CSR_BITS_11BIT.setDefaultValue("0x30")
    mcspiSym_CSR_BITS_11BIT.setVisible(False)

    #MCSPI 12-bit Character size Mask
    mcspiSym_CSR_BITS_12BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_12_BIT_MASK", None)
    mcspiSym_CSR_BITS_12BIT.setDefaultValue("0x40")
    mcspiSym_CSR_BITS_12BIT.setVisible(False)

    #MCSPI 13-bit Character size Mask
    mcspiSym_CSR_BITS_13BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_13_BIT_MASK", None)
    mcspiSym_CSR_BITS_13BIT.setDefaultValue("0x50")
    mcspiSym_CSR_BITS_13BIT.setVisible(False)

    #MCSPI 14-bit Character size Mask
    mcspiSym_CSR_BITS_14BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_14_BIT_MASK", None)
    mcspiSym_CSR_BITS_14BIT.setDefaultValue("0x60")
    mcspiSym_CSR_BITS_14BIT.setVisible(False)

    #MCSPI 15-bit Character size Mask
    mcspiSym_CSR_BITS_15BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_15_BIT_MASK", None)
    mcspiSym_CSR_BITS_15BIT.setDefaultValue("0x70")
    mcspiSym_CSR_BITS_15BIT.setVisible(False)

    #MCSPI 16-bit Character size Mask
    mcspiSym_CSR_BITS_16BIT = mcspiComponent.createStringSymbol("MCSPI_CHARSIZE_BITS_16_BIT_MASK", None)
    mcspiSym_CSR_BITS_16BIT.setDefaultValue("0x80")
    mcspiSym_CSR_BITS_16BIT.setVisible(False)

    mcspiSymDummyData = mcspiComponent.createHexSymbol("MCSPI_DUMMY_DATA", None)
    mcspiSymDummyData.setLabel("Dummy Data")
    mcspiSymDummyData.setDescription("Dummy Data to be written during MCSPI Read")
    mcspiSymDummyData.setDefaultValue(0xFF)
    mcspiSymDummyData.setMin(0x0)
    mcspiSymDummyData.setDependencies(DummyData_ValueUpdate, ["MCSPI_MR_MSTR"])

    #MCSPI Clock Polarity Idle Low Mask
    mcspiSym_CSR_CPOL_IL_Mask = mcspiComponent.createStringSymbol("MCSPI_CLOCK_POLARITY_LOW_MASK", None)
    mcspiSym_CSR_CPOL_IL_Mask.setDefaultValue("0x0")
    mcspiSym_CSR_CPOL_IL_Mask.setVisible(False)

    #MCSPI Clock Polarity Idle High Mask
    mcspiSym_CSR_CPOL_IH_Mask = mcspiComponent.createStringSymbol("MCSPI_CLOCK_POLARITY_HIGH_MASK", None)
    mcspiSym_CSR_CPOL_IH_Mask.setDefaultValue("0x1")
    mcspiSym_CSR_CPOL_IH_Mask.setVisible(False)

    mcspiSymUseBusyPin = mcspiComponent.createBooleanSymbol("MCSPIS_USE_BUSY_PIN", None)
    mcspiSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
    mcspiSymUseBusyPin.setDefaultValue(True)
    mcspiSymUseBusyPin.setVisible(False)
    mcspiSymUseBusyPin.setDependencies(showSlaveDependencies, ["MCSPI_MR_MSTR"])

    mcspiSymBusyPin = mcspiComponent.createKeyValueSetSymbol("MCSPIS_BUSY_PIN", mcspiSymUseBusyPin)
    mcspiSymBusyPin.setVisible(False)
    mcspiSymBusyPin.setLabel("Slave Busy Pin")
    mcspiSymBusyPin.setOutputMode("Key")
    mcspiSymBusyPin.setDisplayMode("Description")
    mcspiSymBusyPin.setDependencies(updateMCSPISlaveBusyPinVisibility, ["MCSPI_MR_MSTR", "MCSPIS_USE_BUSY_PIN"])

    availablePinDictionary = {}

    # Send message to core to get available pins
    availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

    for pad in sort_alphanumeric(availablePinDictionary.values()):
        key = pad
        value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
        description = pad
        mcspiSymBusyPin.addKey(key, value, description)

    #MCSPI Character Size
    mcspiSymBusyPinLogicLevel = mcspiComponent.createKeyValueSetSymbol("MCSPIS_BUSY_PIN_LOGIC_LEVEL", mcspiSymUseBusyPin)
    mcspiSymBusyPinLogicLevel.setLabel("Slave Busy Pin Logic Level")
    mcspiSymBusyPinLogicLevel.setVisible(False)
    mcspiSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    mcspiSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    mcspiSymBusyPinLogicLevel.setDefaultValue(1)
    mcspiSymBusyPinLogicLevel.setOutputMode("Key")
    mcspiSymBusyPinLogicLevel.setDisplayMode("Description")
    mcspiSymBusyPinLogicLevel.setDependencies(updateMCSPISlaveBusyPinVisibility, ["MCSPI_MR_MSTR", "MCSPIS_USE_BUSY_PIN"])

    mcspiSymBusyPinConfigComment = mcspiComponent.createCommentSymbol("MCSPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT", mcspiSymUseBusyPin)
    mcspiSymBusyPinConfigComment.setVisible(False)
    mcspiSymBusyPinConfigComment.setLabel("***Above selected Busy pin must be configured as GPIO Output in Pin Manager***")
    mcspiSymBusyPinConfigComment.setDependencies(updateMCSPISlaveBusyPinVisibility, ["MCSPI_MR_MSTR", "MCSPIS_USE_BUSY_PIN"])

    if mcspi_CSR_Count == 2:
        mcspiSymSPI_MR_PCS_NPCS0 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS0", None)
        mcspiSymSPI_MR_PCS_NPCS0.setDefaultValue("0x02")
        mcspiSymSPI_MR_PCS_NPCS0.setVisible(False)

        mcspiSymSPI_MR_PCS_NPCS1 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS1", None)
        mcspiSymSPI_MR_PCS_NPCS1.setDefaultValue("0x01")
        mcspiSymSPI_MR_PCS_NPCS1.setVisible(False)

    if mcspi_CSR_Count == 4:
        mcspiSymSPI_MR_PCS_NPCS0 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS0", None)
        mcspiSymSPI_MR_PCS_NPCS0.setDefaultValue("0x0E")
        mcspiSymSPI_MR_PCS_NPCS0.setVisible(False)

        mcspiSymSPI_MR_PCS_NPCS1 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS1", None)
        mcspiSymSPI_MR_PCS_NPCS1.setDefaultValue("0x0D")
        mcspiSymSPI_MR_PCS_NPCS1.setVisible(False)

        mcspiSymSPI_MR_PCS_NPCS2 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS2", None)
        mcspiSymSPI_MR_PCS_NPCS2.setDefaultValue("0x0B")
        mcspiSymSPI_MR_PCS_NPCS2.setVisible(False)

        mcspiSymSPI_MR_PCS_NPCS3 = mcspiComponent.createStringSymbol("MCSPI_MR_PCS_NPCS3", None)
        mcspiSymSPI_MR_PCS_NPCS3.setDefaultValue("0x07")
        mcspiSymSPI_MR_PCS_NPCS3.setVisible(False)

    #MCSPI Clock Phase Leading Edge Mask
    mcspiSym_CSR_NCPHA_TE_Mask = mcspiComponent.createStringSymbol("MCSPI_CLOCK_PHASE_TRAILING_MASK", None)
    mcspiSym_CSR_NCPHA_TE_Mask.setDefaultValue("0x0")
    mcspiSym_CSR_NCPHA_TE_Mask.setVisible(False)

    #MCSPI Clock Phase Trailing Edge Mask
    mcspiSym_CSR_NCPHA_LE_Mask = mcspiComponent.createStringSymbol("MCSPI_CLOCK_PHASE_LEADING_MASK", None)
    mcspiSym_CSR_NCPHA_LE_Mask.setDefaultValue("0x2")
    mcspiSym_CSR_NCPHA_LE_Mask.setVisible(False)

    #MCSPI Status OVERRUN Mask
    mcspiSym_SR_OVERES_Mask = mcspiComponent.createStringSymbol("MCSPI_STATUS_OVERRUN_MASK", None)
    mcspiSym_SR_OVERES_Mask.setDefaultValue("0x8")
    mcspiSym_SR_OVERES_Mask.setVisible(False)

    #MCSPI API Prefix
    mcspiSym_API_Prefix = mcspiComponent.createStringSymbol("MCSPI_PLIB_API_PREFIX", None)
    mcspiSym_API_Prefix.setDefaultValue(mcspiInstanceName.getValue())
    mcspiSym_API_Prefix.setVisible(False)

    # Dependency Status for interrupt
    global mcspiSymIntEnComment
    mcspiSymIntEnComment = mcspiComponent.createCommentSymbol(mcspiInstanceName.getValue() + "_NVIC_ENABLE_COMMENT", None)
    mcspiSymIntEnComment.setVisible(False)
    mcspiSymIntEnComment.setLabel("Warning!!! " + mcspiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    mcspiSymIntEnComment.setDependencies(InterruptStatusWarning, ["core." + mcspiSyminterruptVectorUpdate])

    # Dependency Status for clock
    mcspiSymClkEnComment = mcspiComponent.createCommentSymbol(mcspiInstanceName.getValue() + "_CLK_ENABLE_COMMENT", None)
    mcspiSymClkEnComment.setVisible(False)
    mcspiSymClkEnComment.setLabel("Warning!!! " + mcspiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    mcspiSymClkEnComment.setDependencies(ClockStatusWarning, ["core."+ mcspiInstanceName.getValue() + "_CLOCK_ENABLE"])

    # Warning message when PLIB is configured in non-interrupt mode but used with driver.
    global mcspiInterruptDriverModeComment
    mcspiInterruptDriverModeComment = mcspiComponent.createCommentSymbol("MCSPI_INT_DRIVER_COMMENT", None)
    mcspiInterruptDriverModeComment.setVisible(False)
    mcspiInterruptDriverModeComment.setLabel("Warning!!! MCSPI PLIB to be used with driver, must be configured in interrupt mode")

    configName = Variables.get("__CONFIGURATION_NAME")

    mcspimCommonHeaderFile = mcspiComponent.createFileSymbol("MCSPI_COMMON_HEADER", None)
    mcspimCommonHeaderFile.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspi_master_common.h.ftl")
    mcspimCommonHeaderFile.setOutputName("plib_mcspi_master_common.h")
    mcspimCommonHeaderFile.setDestPath("peripheral/mcspi/mcspi_master")
    mcspimCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcspi/mcspi_master")
    mcspimCommonHeaderFile.setType("HEADER")
    mcspimCommonHeaderFile.setMarkup(True)
    mcspimCommonHeaderFile.setOverwrite(True)
    mcspimCommonHeaderFile.setEnabled(mcspiSym_MR_MSTR.getValue() == "MASTER")
    mcspimCommonHeaderFile.setDependencies(mcspiMasterModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspimHeaderFile = mcspiComponent.createFileSymbol("MCSPI_HEADER", None)
    mcspimHeaderFile.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspix_master.h.ftl")
    mcspimHeaderFile.setOutputName("plib_" + mcspiInstanceName.getValue().lower() + "_master.h")
    mcspimHeaderFile.setDestPath("/peripheral/mcspi/mcspi_master")
    mcspimHeaderFile.setProjectPath("config/" + configName +"/peripheral/mcspi/mcspi_master")
    mcspimHeaderFile.setType("HEADER")
    mcspimHeaderFile.setMarkup(True)
    mcspimHeaderFile.setEnabled(mcspiSym_MR_MSTR.getValue() == "MASTER")
    mcspimHeaderFile.setDependencies(mcspiMasterModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspimSource1File = mcspiComponent.createFileSymbol("MCSPI_SOURCE", None)
    mcspimSource1File.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspix_master.c.ftl")
    mcspimSource1File.setOutputName("plib_" + mcspiInstanceName.getValue().lower() + "_master.c")
    mcspimSource1File.setDestPath("/peripheral/mcspi/mcspi_master")
    mcspimSource1File.setProjectPath("config/" + configName +"/peripheral/mcspi/mcspi_master")
    mcspimSource1File.setType("SOURCE")
    mcspimSource1File.setMarkup(True)
    mcspimSource1File.setEnabled(mcspiSym_MR_MSTR.getValue() == "MASTER")
    mcspimSource1File.setDependencies(mcspiMasterModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspisCommonHeaderFile = mcspiComponent.createFileSymbol("MCSPIS_COMMON_HEADER", None)
    mcspisCommonHeaderFile.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspi_slave_common.h")
    mcspisCommonHeaderFile.setOutputName("plib_mcspi_slave_common.h")
    mcspisCommonHeaderFile.setDestPath("peripheral/mcspi/mcspi_slave")
    mcspisCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcspi/mcspi_slave")
    mcspisCommonHeaderFile.setType("HEADER")
    mcspisCommonHeaderFile.setMarkup(False)
    mcspisCommonHeaderFile.setOverwrite(True)
    mcspisCommonHeaderFile.setEnabled(mcspiSym_MR_MSTR.getValue() == "SLAVE")
    mcspisCommonHeaderFile.setDependencies(mcspiSlaveModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspisHeaderFile = mcspiComponent.createFileSymbol("MCSPIS_HEADER", None)
    mcspisHeaderFile.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspix_slave.h.ftl")
    mcspisHeaderFile.setOutputName("plib_" + mcspiInstanceName.getValue().lower() + "_slave.h")
    mcspisHeaderFile.setDestPath("/peripheral/mcspi/mcspi_slave")
    mcspisHeaderFile.setProjectPath("config/" + configName +"/peripheral/mcspi/mcspi_slave")
    mcspisHeaderFile.setType("HEADER")
    mcspisHeaderFile.setMarkup(True)
    mcspisHeaderFile.setEnabled(mcspiSym_MR_MSTR.getValue() == "SLAVE")
    mcspisHeaderFile.setDependencies(mcspiSlaveModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspisSource1File = mcspiComponent.createFileSymbol("MCSPIS_SOURCE", None)
    mcspisSource1File.setSourcePath("../peripheral/mcspi_04462/templates/plib_mcspix_slave.c.ftl")
    mcspisSource1File.setOutputName("plib_" + mcspiInstanceName.getValue().lower() + "_slave.c")
    mcspisSource1File.setDestPath("/peripheral/mcspi/mcspi_slave")
    mcspisSource1File.setProjectPath("config/" + configName +"/peripheral/mcspi/mcspi_slave")
    mcspisSource1File.setType("SOURCE")
    mcspisSource1File.setMarkup(True)
    mcspisSource1File.setEnabled(mcspiSym_MR_MSTR.getValue() == "SLAVE")
    mcspisSource1File.setDependencies(mcspiSlaveModeFileGeneration, ["MCSPI_MR_MSTR"])

    mcspiSystemInitFile = mcspiComponent.createFileSymbol("MCSPI_INIT", None)
    mcspiSystemInitFile.setType("STRING")
    mcspiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    mcspiSystemInitFile.setSourcePath("../peripheral/mcspi_04462/templates/system/initialization.c.ftl")
    mcspiSystemInitFile.setMarkup(True)

    mcspiSystemDefFile = mcspiComponent.createFileSymbol("MCSPI_DEF", None)
    mcspiSystemDefFile.setType("STRING")
    mcspiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mcspiSystemDefFile.setSourcePath("../peripheral/mcspi_04462/templates/system/definitions.h.ftl")
    mcspiSystemDefFile.setMarkup(True)