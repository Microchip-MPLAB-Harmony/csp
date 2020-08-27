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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

global SERCOMfilesArray
global InterruptVectorSecurity
InterruptVectorSecurity = []
SERCOMfilesArray = []

def fileUpdate(symbol, event):
    global SERCOMfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        SERCOMfilesArray[0].setSecurity("SECURE")
        SERCOMfilesArray[1].setSecurity("SECURE")
        SERCOMfilesArray[2].setSecurity("SECURE")
        SERCOMfilesArray[3].setSecurity("SECURE")
        SERCOMfilesArray[4].setSecurity("SECURE")
        SERCOMfilesArray[5].setSecurity("SECURE")
        SERCOMfilesArray[6].setSecurity("SECURE")
        SERCOMfilesArray[7].setSecurity("SECURE")
        SERCOMfilesArray[8].setSecurity("SECURE")
        SERCOMfilesArray[9].setSecurity("SECURE")
        SERCOMfilesArray[10].setSecurity("SECURE")
        SERCOMfilesArray[11].setSecurity("SECURE")
        SERCOMfilesArray[12].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        SERCOMfilesArray[13].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, False)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        SERCOMfilesArray[0].setSecurity("NON_SECURE")
        SERCOMfilesArray[1].setSecurity("NON_SECURE")
        SERCOMfilesArray[2].setSecurity("NON_SECURE")
        SERCOMfilesArray[3].setSecurity("NON_SECURE")
        SERCOMfilesArray[4].setSecurity("NON_SECURE")
        SERCOMfilesArray[5].setSecurity("NON_SECURE")
        SERCOMfilesArray[6].setSecurity("NON_SECURE")
        SERCOMfilesArray[7].setSecurity("NON_SECURE")
        SERCOMfilesArray[8].setSecurity("NON_SECURE")
        SERCOMfilesArray[9].setSecurity("NON_SECURE")
        SERCOMfilesArray[10].setSecurity("NON_SECURE")
        SERCOMfilesArray[11].setSecurity("NON_SECURE")
        SERCOMfilesArray[12].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        SERCOMfilesArray[13].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, True)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, True)

def handleMessage(messageID, args):
    global sercomSym_OperationMode
    global usartSym_RingBuffer_Enable
    global usartSym_Interrupt_Mode
    global spiSym_Interrupt_Mode
    global spisSym_Interrupt_Mode
    global i2csSym_Interrupt_Mode
    global mssenSupported
    global spiSym_CTRLB_MSSEN
    global i2csSym_CTRLB_SMEN
    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            sercomSym_OperationMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            sercomSym_OperationMode.setSelectedKey("I2CM", 2)

    elif (messageID == "I2C_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            sercomSym_OperationMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            sercomSym_OperationMode.setSelectedKey("I2CS", 2)

    elif (messageID == "I2C_SLAVE_SMART_MODE"):
        if args.get("isReadOnly") != None:
            i2csSym_CTRLB_SMEN.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            i2csSym_CTRLB_SMEN.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            i2csSym_CTRLB_SMEN.setVisible(args["isVisible"])

    elif (messageID == "I2C_SLAVE_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            i2csSym_Interrupt_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            i2csSym_Interrupt_Mode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            i2csSym_Interrupt_Mode.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            sercomSym_OperationMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            sercomSym_OperationMode.setSelectedKey("SPIM", 2)

    elif (messageID == "SPI_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            sercomSym_OperationMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            sercomSym_OperationMode.setSelectedKey("SPIS", 2)

    elif (messageID == "UART_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            usartSym_Interrupt_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            usartSym_Interrupt_Mode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            usartSym_Interrupt_Mode.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            spiSym_Interrupt_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            spiSym_Interrupt_Mode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            spiSym_Interrupt_Mode.setVisible(args["isVisible"])

    elif (messageID == "SPI_SLAVE_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            spisSym_Interrupt_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            spisSym_Interrupt_Mode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            spisSym_Interrupt_Mode.setVisible(args["isVisible"])

    elif (messageID == "UART_RING_BUFFER_MODE"):
        if args.get("isReadOnly") != None:
            usartSym_RingBuffer_Enable.setReadOnly(args["isReadOnly"])
        if args.get("isVisible") != None:
            usartSym_RingBuffer_Enable.setVisible(args["isVisible"])
        if args.get("isEnabled") != None:
            usartSym_RingBuffer_Enable.setValue(args["isEnabled"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if mssenSupported == True:
            if args.get("isReadOnly") != None:
                spiSym_CTRLB_MSSEN.setReadOnly(args["isReadOnly"])
            if args.get("isEnabled") != None:
                spiSym_CTRLB_MSSEN.setValue(args["isEnabled"])
            if args.get("isVisible") != None:
                spiSym_CTRLB_MSSEN.setVisible(args["isVisible"])

    return result_dict

def onAttachmentConnected(source, target):

    global sercomSym_OperationMode
    global i2csSym_Interrupt_Mode
    global i2csSym_CTRLB_SMEN

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

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteID, "REQUEST_CONFIG_PARAMS", argDict)

def onAttachmentDisconnected(source, target):

    global sercomSym_OperationMode
    global i2csSym_Interrupt_Mode
    global i2csSym_CTRLB_SMEN

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
    component.getSymbolByID("SERCOM_I2CS_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CS_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_I2CS_SLAVE_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIS_SOURCE").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIS_HEADER").setEnabled(False)
    component.getSymbolByID("SERCOM_SPIS_COMMON_HEADER").setEnabled(False)

    if symObj.getSelectedKey() == "USART_INT":
        component.getSymbolByID("SERCOM_USART_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_USART_COMMON_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "SPIM":
        component.getSymbolByID("SERCOM_SPIM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIM_COMMON_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "SPIS":
        component.getSymbolByID("SERCOM_SPIS_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIS_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_SPIS_COMMON_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "I2CM":
        component.getSymbolByID("SERCOM_I2CM_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CM_MASTER_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "I2CS":
        component.getSymbolByID("SERCOM_I2CS_SOURCE").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CS_HEADER").setEnabled(True)
        component.getSymbolByID("SERCOM_I2CS_SLAVE_HEADER").setEnabled(True)
    elif symObj.getSelectedKey() == "USART_EXT":
        # To be implemented
        pass

def setSERCOMInterruptData(status, sercomMode):

    for id in InterruptVector:
        Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandlerLock:
        Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandler:
        interruptName = id.split("_INTERRUPT_HANDLER")[0]
        if status == True:
            Database.setSymbolValue("core", id, sercomInstanceName.getValue() + "_" + sercomMode + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", id, interruptName + "_Handler", 1)

def updateSERCOMInterruptData(symbol, event):
    global sercomSym_OperationMode
    global sercomInstanceName

    sercomMode = ""
    status = False
    interruptEnable = False

    if sercomSym_OperationMode.getSelectedKey() == "USART_EXT":
        # To be implemented
        pass
    elif (sercomSym_OperationMode.getSelectedKey() == "USART_INT"):
        sercomMode = "USART"
        if (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_INTERRUPT_MODE") == True):
            interruptEnable = True
    elif (sercomSym_OperationMode.getSelectedKey() == "SPIM"):
        sercomMode = "SPI"
        if (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "SPI_INTERRUPT_MODE") == True):
            interruptEnable = True
    elif (sercomSym_OperationMode.getSelectedKey() == "SPIS"):
        sercomMode = "SPI"
        if (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "SPIS_INTERRUPT_MODE") == True):
            interruptEnable = True
    elif (sercomSym_OperationMode.getSelectedKey() == "I2CM"):
        sercomMode = "I2C"
        if (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2C_INTERRUPT_MODE") == True):
            interruptEnable = True
    elif (sercomSym_OperationMode.getSelectedKey() == "I2CS"):
        sercomMode = "I2C"
        if (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2CS_INTERRUPT_MODE") == True):
            interruptEnable = True

    if (sercomMode != "") and (event["id"] == "SERCOM_MODE" or "INTERRUPT_MODE" in event["id"]):
        setSERCOMInterruptData(interruptEnable, sercomMode)

    for id in InterruptVectorUpdate:
        id = id.replace("core.", "")
        if Database.getSymbolValue("core", id) == True:
            status = True
            break

    if ((status == True) and (interruptEnable == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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
        symbol.setValue("", 1)

def USARTFileGeneration(symbol, event):
    componentID = symbol.getID()
    filepath = ""
    ringBufferModeEnabled = event["value"]

    if componentID == "SERCOM_USART_HEADER":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/sercom_u2201/templates/plib_sercom_usart_ring_buffer.h.ftl"
        else:
            filepath = "../peripheral/sercom_u2201/templates/plib_sercom_usart.h.ftl"
    elif componentID == "SERCOM_USART_SOURCE":
        if ringBufferModeEnabled == True:
            filepath = "../peripheral/sercom_u2201/templates/plib_sercom_usart_ring_buffer.c.ftl"
        else:
            filepath = "../peripheral/sercom_u2201/templates/plib_sercom_usart.c.ftl"

    symbol.setSourcePath(filepath)

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
    global InterruptVectorUpdate
    global sercomInstanceName
    global sercomSym_OperationMode
    global sercomClkFrequencyId
    global InterruptVectorSecurity

    InterruptVector = []
    InterruptHandler = []
    InterruptHandlerLock = []
    InterruptVectorUpdate = []

    sercomInstanceName = sercomComponent.createStringSymbol("SERCOM_INSTANCE_NAME", None)
    sercomInstanceName.setVisible(False)
    sercomInstanceName.setDefaultValue(sercomComponent.getID().upper())

    Log.writeInfoMessage("Running " + sercomInstanceName.getValue())

    uartCapabilityId = sercomInstanceName.getValue() + "_UART"
    spiCapabilityId = sercomInstanceName.getValue() + "_SPI"
    i2cCapabilityId = sercomInstanceName.getValue() + "_I2C"

    sercomClkFrequencyId = sercomInstanceName.getValue() + "_CORE_CLOCK_FREQUENCY"

    #Clock enable
    Database.setSymbolValue("core", sercomInstanceName.getValue() + "_CORE_CLOCK_ENABLE", True, 2)

    #SERCOM USART mode
    sercomDisableUSART = 0
    sercomSym_Parameters = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SERCOM\"]/instance@[name=\"" + sercomInstanceName.getValue() + "\"]/parameters")
    for id in range(len(sercomSym_Parameters.getChildren())):
        if sercomSym_Parameters.getChildren()[id].getAttribute("name") == "USART" and sercomSym_Parameters.getChildren()[id].getAttribute("value") == "0":
            sercomDisableUSART = 1

    #SERCOM SPI mode
    sercomDisableSPI = 0
    for id in range(len(sercomSym_Parameters.getChildren())):
        if sercomSym_Parameters.getChildren()[id].getAttribute("name") == "SPI" and sercomSym_Parameters.getChildren()[id].getAttribute("value") == "0":
            sercomDisableSPI = 1

    #SERCOM I2CM and I2CS modes
    sercomDisableI2CM = 0
    sercomDisableI2CS = 0
    for id in range(len(sercomSym_Parameters.getChildren())):
        if sercomSym_Parameters.getChildren()[id].getAttribute("name") == "TWIM" and sercomSym_Parameters.getChildren()[id].getAttribute("value") == "0":
            sercomDisableI2CM = 1
        if sercomSym_Parameters.getChildren()[id].getAttribute("name") == "TWIS" and sercomSym_Parameters.getChildren()[id].getAttribute("value") == "0":
            sercomDisableI2CS = 1

    #SERCOM operation mode Menu - Serial Communication Interfaces
    sercomSym_OperationMode = sercomComponent.createKeyValueSetSymbol("SERCOM_MODE", None)
    sercomSym_OperationMode.setLabel("Select SERCOM Operation Mode")

    if sercomDisableUSART != 1:
        sercomSym_OperationMode.addKey("USART_INT", "1", "USART with internal Clock")
    else:
        sercomComponent.setCapabilityEnabled(sercomInstanceName.getValue() + "_UART", False)
        uartCapabilityId = ""
    if sercomDisableSPI != 1:
        sercomSym_OperationMode.addKey("SPIM", "3", "SPI Master")
    else:
        sercomComponent.setCapabilityEnabled(sercomInstanceName.getValue() + "_SPI", False)
        spiCapabilityId = ""
    if sercomDisableI2CM != 1:
        sercomSym_OperationMode.addKey("I2CM", "5", "I2C Master")
    else:
        sercomComponent.setCapabilityEnabled(sercomInstanceName.getValue() + "_I2C", False)
        i2cCapabilityId = ""
    if sercomDisableI2CS != 1:
        sercomSym_OperationMode.addKey("I2CS", "4", "I2C Slave")
    else:
        sercomComponent.setCapabilityEnabled(sercomInstanceName.getValue() + "_I2C", False)
        i2cCapabilityId = ""
    if sercomDisableSPI != 1:
        sercomSym_OperationMode.addKey("SPIS", "2", "SPI Slave")

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

    syncbusyNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SERCOM"]/register-group@[name="SERCOM"]/register@[modes="USART_INT",name="SYNCBUSY"]')

    #SERCOM is SYNCBUSY present
    sercomSym_SYNCBUSY = sercomComponent.createBooleanSymbol("SERCOM_SYNCBUSY", sercomSym_OperationMode)
    sercomSym_SYNCBUSY.setVisible(False)
    sercomSym_SYNCBUSY.setDefaultValue((syncbusyNode != None))

    ###################################################################################################
    ########################################## SERCOM MODE ############################################
    ###################################################################################################

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_usart.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_spi_master.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_spi_slave.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_i2c_master.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/sercom_u2201/config/sercom_i2c_slave.py")

    ############################################################################
    #### Dependency ####
    ############################################################################

    interruptValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for index in range(len(interruptValues)):
        moduleInstance = list(str(interruptValues[index].getAttribute("module-instance")).split(" "))
        if sercomInstanceName.getValue() in moduleInstance:

            # check weather sub-vectors or multiple peripherals are present at same interrupt line
            if len(moduleInstance) == 1:
                name = str(interruptValues[index].getAttribute("name"))
            else:
                name = sercomInstanceName.getValue()

            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append("core." + name + "_INTERRUPT_ENABLE_UPDATE")
            InterruptVectorSecurity.append(name + "_SET_NON_SECURE")

    # Initial settings for Interrupt
    if (sercomSym_OperationMode.getSelectedKey() == "USART_INT") and (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "USART_INTERRUPT_MODE") == True):
        setSERCOMInterruptData(True, "USART")
    elif (sercomSym_OperationMode.getSelectedKey() == "I2CM") and (Database.getSymbolValue(sercomInstanceName.getValue().lower(), "I2C_INTERRUPT_MODE") == True):
        setSERCOMInterruptData(True, "I2C")

    # Interrupt Warning status
    sercomSym_IntEnComment = sercomComponent.createCommentSymbol("SERCOM_INTERRUPT_ENABLE_COMMENT", None)
    sercomSym_IntEnComment.setVisible(False)
    sercomSym_IntEnComment.setLabel("Warning!!! " + sercomInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    sercomSym_IntEnComment.setDependencies(updateSERCOMInterruptData, ["SERCOM_MODE", "USART_INTERRUPT_MODE", "SPI_INTERRUPT_MODE", "SPIS_INTERRUPT_MODE", "I2CS_INTERRUPT_MODE", "I2C_INTERRUPT_MODE"] + InterruptVectorUpdate)

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
    usartHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
    usartHeaderFile.setDependencies(USARTFileGeneration, ["USART_RING_BUFFER_ENABLE"])

    usartCommonHeaderFile = sercomComponent.createFileSymbol("SERCOM_USART_COMMON_HEADER", None)
    usartCommonHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_usart_common.h.ftl")
    usartCommonHeaderFile.setOutputName("plib_sercom_usart_common.h")
    usartCommonHeaderFile.setDestPath("/peripheral/sercom/usart/")
    usartCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartCommonHeaderFile.setType("HEADER")
    usartCommonHeaderFile.setMarkup(True)
    usartCommonHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "USART_INT")

    usartSourceFile = sercomComponent.createFileSymbol("SERCOM_USART_SOURCE", None)
    usartSourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_usart.c.ftl")
    usartSourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_usart.c")
    usartSourceFile.setDestPath("/peripheral/sercom/usart/")
    usartSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/usart/")
    usartSourceFile.setType("SOURCE")
    usartSourceFile.setMarkup(True)
    usartSourceFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "USART_INT")
    usartSourceFile.setDependencies(USARTFileGeneration, ["USART_RING_BUFFER_ENABLE"])


    spiSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIM_HEADER", None)
    spiSym_HeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_master.h.ftl")
    spiSym_HeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi_master.h")
    spiSym_HeaderFile.setDestPath("/peripheral/sercom/spi_master/")
    spiSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi_master/")
    spiSym_HeaderFile.setType("HEADER")
    spiSym_HeaderFile.setMarkup(True)
    spiSym_HeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIM")

    spiSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIM_COMMON_HEADER", None)
    spiSym_Header1File.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_master_common.h")
    spiSym_Header1File.setOutputName("plib_sercom_spi_master_common.h")
    spiSym_Header1File.setDestPath("/peripheral/sercom/spi_master/")
    spiSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spi_master/")
    spiSym_Header1File.setType("HEADER")
    spiSym_Header1File.setMarkup(True)
    spiSym_Header1File.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIM")

    spiSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIM_SOURCE", None)
    spiSym_SourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_master.c.ftl")
    spiSym_SourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi_master.c")
    spiSym_SourceFile.setDestPath("/peripheral/sercom/spi_master/")
    spiSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi_master/")
    spiSym_SourceFile.setType("SOURCE")
    spiSym_SourceFile.setMarkup(True)
    spiSym_SourceFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIM")

    spiSlaveSym_HeaderFile = sercomComponent.createFileSymbol("SERCOM_SPIS_HEADER", None)
    spiSlaveSym_HeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_slave.h.ftl")
    spiSlaveSym_HeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi_slave.h")
    spiSlaveSym_HeaderFile.setDestPath("/peripheral/sercom/spi_slave/")
    spiSlaveSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi_slave/")
    spiSlaveSym_HeaderFile.setType("HEADER")
    spiSlaveSym_HeaderFile.setMarkup(True)
    spiSlaveSym_HeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIS")

    spiSlaveSym_Header1File = sercomComponent.createFileSymbol("SERCOM_SPIS_COMMON_HEADER", None)
    spiSlaveSym_Header1File.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_slave_common.h")
    spiSlaveSym_Header1File.setOutputName("plib_sercom_spi_slave_common.h")
    spiSlaveSym_Header1File.setDestPath("/peripheral/sercom/spi_slave/")
    spiSlaveSym_Header1File.setProjectPath("config/" + configName + "/peripheral/sercom/spi_slave/")
    spiSlaveSym_Header1File.setType("HEADER")
    spiSlaveSym_Header1File.setMarkup(True)
    spiSlaveSym_Header1File.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIS")

    spiSlaveSym_SourceFile = sercomComponent.createFileSymbol("SERCOM_SPIS_SOURCE", None)
    spiSlaveSym_SourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_spi_slave.c.ftl")
    spiSlaveSym_SourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_spi_slave.c")
    spiSlaveSym_SourceFile.setDestPath("/peripheral/sercom/spi_slave/")
    spiSlaveSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/spi_slave/")
    spiSlaveSym_SourceFile.setType("SOURCE")
    spiSlaveSym_SourceFile.setMarkup(True)
    spiSlaveSym_SourceFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "SPIS")

    i2cmMasterHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_MASTER_HEADER", None)
    i2cmMasterHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_master_common.h")
    i2cmMasterHeaderFile.setOutputName("plib_sercom_i2c_master_common.h")
    i2cmMasterHeaderFile.setDestPath("/peripheral/sercom/i2c_master/")
    i2cmMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_master/")
    i2cmMasterHeaderFile.setType("HEADER")
    i2cmMasterHeaderFile.setMarkup(True)
    i2cmMasterHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CM")

    i2cmHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CM_HEADER", None)
    i2cmHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_master.h.ftl")
    i2cmHeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c_master.h")
    i2cmHeaderFile.setDestPath("/peripheral/sercom/i2c_master/")
    i2cmHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_master/")
    i2cmHeaderFile.setType("HEADER")
    i2cmHeaderFile.setMarkup(True)
    i2cmHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CM")

    i2cmSourceFile = sercomComponent.createFileSymbol("SERCOM_I2CM_SOURCE", None)
    i2cmSourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_master.c.ftl")
    i2cmSourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c_master.c")
    i2cmSourceFile.setDestPath("/peripheral/sercom/i2c_master/")
    i2cmSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_master/")
    i2cmSourceFile.setType("SOURCE")
    i2cmSourceFile.setMarkup(True)
    i2cmSourceFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CM")

    i2csSlaveHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CS_SLAVE_HEADER", None)
    i2csSlaveHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_slave_common.h.ftl")
    i2csSlaveHeaderFile.setOutputName("plib_sercom_i2c_slave_common.h")
    i2csSlaveHeaderFile.setDestPath("/peripheral/sercom/i2c_slave/")
    i2csSlaveHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_slave/")
    i2csSlaveHeaderFile.setType("HEADER")
    i2csSlaveHeaderFile.setMarkup(True)
    i2csSlaveHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CS")

    i2csHeaderFile = sercomComponent.createFileSymbol("SERCOM_I2CS_HEADER", None)
    i2csHeaderFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_slave.h.ftl")
    i2csHeaderFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c_slave.h")
    i2csHeaderFile.setDestPath("/peripheral/sercom/i2c_slave/")
    i2csHeaderFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_slave/")
    i2csHeaderFile.setType("HEADER")
    i2csHeaderFile.setMarkup(True)
    i2csHeaderFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CS")

    i2csSourceFile = sercomComponent.createFileSymbol("SERCOM_I2CS_SOURCE", None)
    i2csSourceFile.setSourcePath("../peripheral/sercom_u2201/templates/plib_sercom_i2c_slave.c.ftl")
    i2csSourceFile.setOutputName("plib_" + sercomInstanceName.getValue().lower() + "_i2c_slave.c")
    i2csSourceFile.setDestPath("/peripheral/sercom/i2c_slave/")
    i2csSourceFile.setProjectPath("config/" + configName + "/peripheral/sercom/i2c_slave/")
    i2csSourceFile.setType("SOURCE")
    i2csSourceFile.setMarkup(True)
    i2csSourceFile.setEnabled(sercomSym_OperationMode.getSelectedKey() == "I2CS")

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

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global SERCOMfilesArray
        sercomIsNonSecure = Database.getSymbolValue("core", sercomComponent.getID().upper() + "_IS_NON_SECURE")
        sercomSystemDefFile.setDependencies(fileUpdate, ["core." + sercomComponent.getID().upper() + "_IS_NON_SECURE"])
        SERCOMfilesArray.append(usartHeaderFile)
        SERCOMfilesArray.append(usartCommonHeaderFile)
        SERCOMfilesArray.append(usartSourceFile)
        SERCOMfilesArray.append(spiSym_HeaderFile)
        SERCOMfilesArray.append(spiSym_Header1File)
        SERCOMfilesArray.append(spiSym_SourceFile)
        SERCOMfilesArray.append(i2cmMasterHeaderFile)
        SERCOMfilesArray.append(i2cmHeaderFile)
        SERCOMfilesArray.append(i2cmSourceFile)
        SERCOMfilesArray.append(i2csSlaveHeaderFile)
        SERCOMfilesArray.append(i2csHeaderFile)
        SERCOMfilesArray.append(i2csSourceFile)
        SERCOMfilesArray.append(sercomSystemInitFile)
        SERCOMfilesArray.append(sercomSystemDefFile)
        if len(InterruptVectorSecurity) != 1:
            for vector in InterruptVectorSecurity:
                Database.setSymbolValue("core", vector, sercomIsNonSecure)
        else:
            Database.setSymbolValue("core", InterruptVectorSecurity, sercomIsNonSecure)

        if sercomIsNonSecure == False:
            SERCOMfilesArray[0].setSecurity("SECURE")
            SERCOMfilesArray[1].setSecurity("SECURE")
            SERCOMfilesArray[2].setSecurity("SECURE")
            SERCOMfilesArray[3].setSecurity("SECURE")
            SERCOMfilesArray[4].setSecurity("SECURE")
            SERCOMfilesArray[5].setSecurity("SECURE")
            SERCOMfilesArray[6].setSecurity("SECURE")
            SERCOMfilesArray[7].setSecurity("SECURE")
            SERCOMfilesArray[8].setSecurity("SECURE")
            SERCOMfilesArray[9].setSecurity("SECURE")
            SERCOMfilesArray[10].setSecurity("SECURE")
            SERCOMfilesArray[11].setSecurity("SECURE")
            SERCOMfilesArray[12].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            SERCOMfilesArray[13].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")