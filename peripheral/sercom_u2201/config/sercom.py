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

global uartCapabilityId
global spiCapabilityId
global i2cCapabilityId

global InterruptVector
global InterruptHandler
global InterruptHandlerLock
global sercomInstanceName

###################################################################################################
###################################### BAUD Calculation ###########################################
###################################################################################################

#BAUD Rate Calculation for SPI
def getspiBaud(gclk, clkspeed):

    baud = int(round(float("{0:.15f}".format(float(gclk / (2 * clkspeed)))) - 1))

    if baud <= 0:
        baud = 1
    elif baud > 255:
        baud = 255

    return baud

#BAUD Rate Calculation for USART
def getUSARTBaudValue(clk, baud):

    baudValue = 0
    sampleCount = 0
    sampleRate = 0

    if "SAMD20" in sercomSym_DeviceName.getValue():
        # Sample Rate is not supported in SAMD20
        if clk >= (16 * baud):
            sampleCount = 16
        else:
            return baudValue
    else:
        if clk >= (16 * baud):
            sampleRate = 0
            sampleCount = 16
        elif clk >= (8 * baud):
            sampleRate = 2
            sampleCount = 8
        elif clk >= (3 * baud):
            sampleRate = 4
            sampleCount = 3
        else:
            return baudValue

    baudValue =  int(65536 * (1 - float("{0:.15f}".format(float(sampleCount * baud) / clk))))

    if baudValue != 0:
        usartSym_SAMPLE_COUNT.setValue(sampleCount, 2)
        usartSym_CTRLA_SAMPR.setValue(sampleRate, 2)

    return baudValue

#BAUD Rate Calculation for I2C
def geti2cBaud(gclk, clkSpeed, trise, mode):

    baudlow = int(round(((gclk / clkSpeed) * (1 - float("{0:.15f}".format(float(trise * clkSpeed) / 1000000000)))) - 10))

    if baudlow >= (0xFF * 2) or (baudlow <= 1):
        baud = 0
    else:
        if mode == 0:
            baud = ((baudlow / 2) + (((baudlow / 2) + 1) << 8)) if(baudlow & 0x1) \
            else (baudlow / 2)
        else:
            baud = ((baudlow / 3) + ((((2 * baudlow) / 3) + 1) << 8)) if(baudlow & 0x1) \
            else (baudlow / 3)

    return baud

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def onAttachmentConnected(source, target):

    global sercomSym_OperationMode

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if connectID == uartCapabilityId:
        localComponent.setCapabilityEnabled(uartCapabilityId, True)
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.setCapabilityEnabled(i2cCapabilityId, False)
        sercomSym_OperationMode.setSelectedKey("USART_INT", 2)
    elif connectID == spiCapabilityId:
        localComponent.setCapabilityEnabled(uartCapabilityId, False)
        localComponent.setCapabilityEnabled(spiCapabilityId, True)
        localComponent.setCapabilityEnabled(i2cCapabilityId, False)
        sercomSym_OperationMode.setSelectedKey("SPIM", 2)
    elif connectID == i2cCapabilityId:
        localComponent.setCapabilityEnabled(uartCapabilityId, False)
        localComponent.setCapabilityEnabled(spiCapabilityId, False)
        localComponent.setCapabilityEnabled(i2cCapabilityId, True)
        sercomSym_OperationMode.setSelectedKey("I2CM", 2)

    sercomSym_OperationMode.setReadOnly(True)

def onAttachmentDisconnected(source, target):

    global sercomSym_OperationMode

    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    localComponent.setCapabilityEnabled(uartCapabilityId, True)
    localComponent.setCapabilityEnabled(spiCapabilityId, True)
    localComponent.setCapabilityEnabled(i2cCapabilityId, True)

    sercomSym_OperationMode.setReadOnly(False)

def updateSERCOMCodeGenerationProperty(symbol, event):

    symObj = event["symbol"]

    component = symbol.getComponent()

    component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(False)

    if symObj.getSelectedKey() == "USART_INT":
        component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "SPIM":
        component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "I2CM":
        component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "I2CS":
        # To be implemented
        pass
    elif symObj.getSelectedKey() == "SPIS":
        # To be implemented
        pass
    elif symObj.getSelectedKey() == "USART_EXT":
        # To be implemented
        pass

def setSERCOMInterruptData(status, sercomMode):

    Database.setSymbolValue("core", InterruptVector, status, 2)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 2)

    if status == True:
        Database.setSymbolValue("core", InterruptHandler, sercomInstanceName.getValue() + "_" + sercomMode + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler, sercomInstanceName.getValue() + "_Handler", 2)

def updateSERCOMInterruptStatus(symbol, event):

    global i2cSym_Interrupt_Mode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode
    global sercomSym_OperationMode

    sercomMode = ""

    if event["id"] == "SERCOM_MODE":
        if sercomSym_OperationMode.getSelectedKey() == "I2CS":
            # To be implemented
            pass
        elif sercomSym_OperationMode.getSelectedKey() == "SPIS":
            # To be implemented
            pass
        elif sercomSym_OperationMode.getSelectedKey() == "USART_EXT":
            # To be implemented
            pass
        else:
            sercomInterruptStatus = False
            sercomUSARTMode = (sercomSym_OperationMode.getSelectedKey() == "USART_INT") and (usartSym_Interrupt_Mode.getValue() == True)
            sercomSPIMode = (sercomSym_OperationMode.getSelectedKey() == "SPIM") and (spiSym_Interrupt_Mode.getValue() == True)
            sercomI2CMode = (sercomSym_OperationMode.getSelectedKey() == "I2CM") and (i2cSym_Interrupt_Mode.getValue() == True)

            if sercomUSARTMode == True:
                sercomMode = "USART"
                sercomInterruptStatus = True
            elif sercomSPIMode == True:
                sercomMode = "SPI"
                sercomInterruptStatus = True
            elif sercomI2CMode == True:
                sercomMode = "I2C"
                sercomInterruptStatus = True

            setSERCOMInterruptData(sercomInterruptStatus, sercomMode)
    else:
        if sercomSym_OperationMode.getSelectedKey() == "USART_INT":
            sercomMode = "USART"
        elif sercomSym_OperationMode.getSelectedKey() == "SPIM":
            sercomMode = "SPI"

        setSERCOMInterruptData(event["value"], sercomMode)

def updateSERCOMInterruptWarningStatus(symbol, event):

    global i2cSym_Interrupt_Mode
    global spiSym_Interrupt_Mode
    global usartSym_Interrupt_Mode
    global sercomSym_OperationMode

    if sercomSym_OperationMode.getSelectedKey() == "I2CS":
        # To be implemented
        pass
    elif sercomSym_OperationMode.getSelectedKey() == "SPIS":
        # To be implemented
        pass
    elif sercomSym_OperationMode.getSelectedKey() == "USART_EXT":
        # To be implemented
        pass
    else:
        sercomUSARTMode = (sercomSym_OperationMode.getSelectedKey() == "USART_INT") and (usartSym_Interrupt_Mode.getValue() == True)
        sercomSPIMode = (sercomSym_OperationMode.getSelectedKey() == "SPIM") and (spiSym_Interrupt_Mode.getValue() == True)
        sercomI2CMode = (sercomSym_OperationMode.getSelectedKey() == "I2CM") and (i2cSym_Interrupt_Mode.getValue() == True)

        if sercomUSARTMode == True or sercomSPIMode == True or sercomI2CMode == True:
            symbol.setVisible(event["value"])

def updateSERCOMClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def updateSERCOMDMATransferRegister(symbol, event):

    symObj = event["symbol"]

    if symObj.getSelectedKey() == "USART_INT":
        symbol.setValue("&(" + sercomInstanceName.getValue() + "_REGS->USART_INT.SERCOM_DATA)", 2)
    elif symObj.getSelectedKey() == "SPIM":
        symbol.setValue("&(" + sercomInstanceName.getValue() + "_REGS->SPIM.SERCOM_DATA)", 2)
    elif symObj.getSelectedKey() == "I2CS":
        # To be implemented
        pass
    elif symObj.getSelectedKey() == "SPIS":
        # To be implemented
        pass
    elif symObj.getSelectedKey() == "USART_EXT":
        # To be implemented
        pass
    else:
        symbol.setValue("", 2)

def updateSERCOMClockFrequencyValueProperty(symbol, event):

    symbol.setValue(int(event["value"]), 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(sercomComponent):

    global uartCapabilityId
    global spiCapabilityId
    global i2cCapabilityId
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global sercomInstanceName
    global sercomSym_DeviceName
    global sercomSym_OperationMode

    sercomInstanceName = sercomComponent.createStringSymbol("SERCOM_INSTANCE_NAME", None)
    sercomInstanceName.setVisible(False)
    sercomInstanceName.setDefaultValue(sercomComponent.getID().upper())

    Log.writeInfoMessage("Running " + sercomInstanceName.getValue())

    uartCapabilityId = sercomInstanceName.getValue() + "_UART"
    spiCapabilityId = sercomInstanceName.getValue() + "_SPI"
    i2cCapabilityId = sercomInstanceName.getValue() + "_I2C"

    #Device name
    sercomSym_DeviceName = sercomComponent.createStringSymbol("SERCOM_DEVICE_NAME", None)
    sercomSym_DeviceName.setVisible(False)
    sercomSym_DeviceName.setDefaultValue(Variables.get("__PROCESSOR"))

    #Clock enable
    Database.setSymbolValue("core", sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE", True, 2)

    #SERCOM operation mode Menu - Serial Communication Interfaces
    sercomSym_OperationMode = sercomComponent.createKeyValueSetSymbol("SERCOM_MODE", None)
    sercomSym_OperationMode.setLabel("Select SERCOM Operation Mode")
    sercomSym_OperationMode.addKey("USART_INT", "1", "USART with internal Clock")
    sercomSym_OperationMode.addKey("SPIM", "3", "SPI Master")
    sercomSym_OperationMode.addKey("I2CM", "5", "I2C Master")
    sercomSym_OperationMode.setDefaultValue(0)
    sercomSym_OperationMode.setOutputMode("Key")
    sercomSym_OperationMode.setDisplayMode("Description")

    #SERCOM code generation dependecy based on selected mode
    sercomSym_CodeGeneration = sercomComponent.createBooleanSymbol("SERCOM_CODE_GENERATION", sercomSym_OperationMode)
    sercomSym_CodeGeneration.setVisible(False)
    sercomSym_CodeGeneration.setDependencies(updateSERCOMCodeGenerationProperty, ["SERCOM_MODE"])

    #SERCOM Transmit data register
    sercomSym_TxRegister = sercomComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", sercomSym_OperationMode)
    sercomSym_TxRegister.setDefaultValue("&(" + sercomInstanceName.getValue() + "_REGS->USART_INT.SERCOM_DATA)")
    sercomSym_TxRegister.setVisible(False)
    sercomSym_TxRegister.setDependencies(updateSERCOMDMATransferRegister, ["SERCOM_MODE"])

    #SERCOM Receive data register
    sercomSym_RxRegister = sercomComponent.createStringSymbol("RECEIVE_DATA_REGISTER", sercomSym_OperationMode)
    sercomSym_RxRegister.setDefaultValue("&(" + sercomInstanceName.getValue() + "_REGS->USART_INT.SERCOM_DATA)")
    sercomSym_RxRegister.setVisible(False)
    sercomSym_RxRegister.setDependencies(updateSERCOMDMATransferRegister, ["SERCOM_MODE"])

    sercomClkFrequencyId = sercomInstanceName.getValue() + "_CORE_CLOCK_FREQUENCY"
    sercomClkFrequency = int(Database.getSymbolValue("core", sercomClkFrequencyId))

    #SERCOM Clock Frequency
    sercomSym_ClockFrequency = sercomComponent.createIntegerSymbol("SERCOM_CLOCK_FREQUENCY", None)
    sercomSym_ClockFrequency.setLabel(sercomInstanceName.getValue() + " Clock Frequency")
    sercomSym_ClockFrequency.setDefaultValue(sercomClkFrequency)
    sercomSym_ClockFrequency.setVisible(False)
    sercomSym_ClockFrequency.setDependencies(updateSERCOMClockFrequencyValueProperty, ["core." + sercomClkFrequencyId])

    ###################################################################################################
    ########################################## SERCOM MODE ############################################
    ###################################################################################################

    sercomModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SERCOM\"]")
    sercomModuleID = sercomModuleNode.getAttribute("id")

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_usart.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_spi_master.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_i2c_master.py")

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector = sercomInstanceName.getValue() + "_INTERRUPT_ENABLE"
    InterruptHandler = sercomInstanceName.getValue() + "_INTERRUPT_HANDLER"
    InterruptHandlerLock = sercomInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    InterruptVectorUpdate = sercomInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # Initial settings for Interrupt
    setSERCOMInterruptData(True, "USART")

    # Interrupt Dynamic settings
    sercomSym_UpdateInterruptStatus = sercomComponent.createBooleanSymbol("SERCOM_INTERRUPT_STATUS", None)
    sercomSym_UpdateInterruptStatus.setDependencies(updateSERCOMInterruptStatus, ["SERCOM_MODE", "USART_INTERRUPT_MODE", "SPI_INTERRUPT_MODE"])
    sercomSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    sercomSym_IntEnComment = sercomComponent.createCommentSymbol("SERCOM_INTERRUPT_ENABLE_COMMENT", None)
    sercomSym_IntEnComment.setVisible(False)
    sercomSym_IntEnComment.setLabel("Warning!!! " + sercomInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    sercomSym_IntEnComment.setDependencies(updateSERCOMInterruptWarningStatus, ["core." + InterruptVectorUpdate])

    # Clock Warning status
    sercomSym_ClkEnComment = sercomComponent.createCommentSymbol("SERCOM_CLOCK_ENABLE_COMMENT", None)
    sercomSym_ClkEnComment.setLabel("Warning!!! " + sercomInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    sercomSym_ClkEnComment.setVisible(False)
    sercomSym_ClkEnComment.setDependencies(updateSERCOMClockWarningStatus, ["core." + sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    usartHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_HEADER", None)
    usartHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_usart.h.ftl")
    usartHeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_usart.h")
    usartHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartHeaderFile.setType("HEADER")
    usartHeaderFile.setMarkup(True)

    usartCommonHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_COMMON_HEADER", None)
    usartCommonHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_usart_common.h")
    usartCommonHeaderFile.setOutputName("plib_sercom_usart_common.h")
    usartCommonHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartCommonHeaderFile.setType("HEADER")
    usartCommonHeaderFile.setMarkup(True)

    usartSourceFile = sercomComponent.createFileSymbol("SERCOM_USART_SOURCE", None)
    usartSourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_usart.c.ftl")
    usartSourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_usart.c")
    usartSourceFile.setDestPath("/peripheral/sercom/usart/")
    usartSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartSourceFile.setType("SOURCE")
    usartSourceFile.setMarkup(True)

    spiSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIM_HEADER", None)
    spiSym_HeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi.h.ftl")
    spiSym_HeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi.h")
    spiSym_HeaderFile.setDestPath("/peripheral/sercom/spim/")
    spiSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spim/")
    spiSym_HeaderFile.setType("HEADER")
    spiSym_HeaderFile.setMarkup(True)
    spiSym_HeaderFile.setEnabled(False)

    spiSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIM_COMMON_HEADER", None)
    spiSym_Header1File.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_common.h")
    spiSym_Header1File.setOutputName("plib_sercom_spi_common.h")
    spiSym_Header1File.setDestPath("/peripheral/sercom/spim/")
    spiSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spim/")
    spiSym_Header1File.setType("HEADER")
    spiSym_Header1File.setMarkup(True)
    spiSym_Header1File.setEnabled(False)

    spiSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIM_SOURCE", None)
    spiSym_SourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi.c.ftl")
    spiSym_SourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi.c")
    spiSym_SourceFile.setDestPath("/peripheral/sercom/spim/")
    spiSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/spim/")
    spiSym_SourceFile.setType("SOURCE")
    spiSym_SourceFile.setMarkup(True)
    spiSym_SourceFile.setEnabled(False)

    i2cmMasterHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_MASTER_HEADER", None)
    i2cmMasterHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setOutputName("plib_sercom_i2c_master.h")
    i2cmMasterHeaderFile.setDestPath("/peripheral/sercom/i2cm/")
    i2cmMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmMasterHeaderFile.setType("HEADER")
    i2cmMasterHeaderFile.setMarkup(True)
    i2cmMasterHeaderFile.setEnabled(False)

    i2cmHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_HEADER", None)
    i2cmHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c.h.ftl")
    i2cmHeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c.h")
    i2cmHeaderFile.setDestPath("/peripheral/sercom/i2cm/")
    i2cmHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmHeaderFile.setType("HEADER")
    i2cmHeaderFile.setMarkup(True)
    i2cmHeaderFile.setEnabled(False)

    i2cmSourceFile = sercomComponent.createFileSymbol("SERCOM_I2CM_SOURCE", None)
    i2cmSourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c.c.ftl")
    i2cmSourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c.c")
    i2cmSourceFile.setDestPath("/peripheral/sercom/i2cm/")
    i2cmSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2cm/")
    i2cmSourceFile.setType("SOURCE")
    i2cmSourceFile.setMarkup(True)
    i2cmSourceFile.setEnabled(False)

    sercomSystemInitFile = sercomComponent.createFileSymbol("SERCOM_SYS_INIT", None)
    sercomSystemInitFile.setType("STRING")
    sercomSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sercomSystemInitFile.setSourcePath("../peripheral/sercom_u2201/templates/system/initialization.c.ftl")
    sercomSystemInitFile.setMarkup(True)

    sercomSystemDefFile = sercomComponent.createFileSymbol("SERCOM_SYS_DEF", None)
    sercomSystemDefFile.setType("STRING")
    sercomSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sercomSystemDefFile.setSourcePath("../peripheral/sercom_u2201/templates/system/definitions.h.ftl")
    sercomSystemDefFile.setMarkup(True)
