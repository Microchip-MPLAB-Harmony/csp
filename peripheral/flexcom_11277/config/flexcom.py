"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
global flexcomSym_RingBuffer_Enable
################################################################################
#### Business Logic ####
################################################################################
def handleMessage(messageID, args):
    global flexcomSym_RingBuffer_Enable
    global flexcomSym_UsartInterrupt
    global flexcomSym_SPI_InterruptMode
    global flexcomSym_OperatingMode
    global flexcomSym_SPI_MR_PCS
    global flexcomSym_Twi_Interrupt
    result_dict = {"isSuccessful": "true"}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_OperatingMode.setReadOnly(args["isReadOnly"])
            flexcomSym_Twi_OpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            flexcomSym_OperatingMode.setSelectedKey("TWI")
            flexcomSym_Twi_OpMode.setValue("MASTER")

    elif (messageID == "I2C_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_OperatingMode.setReadOnly(args["isReadOnly"])
            flexcomSym_Twi_OpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            flexcomSym_OperatingMode.setSelectedKey("TWI")
            flexcomSym_Twi_OpMode.setValue("SLAVE")

    elif (messageID == "I2C_SLAVE_INTERRUPT_MODE"):
        if flexcomSym_Twi_OpMode.getValue() == "SLAVE":
            if args.get("isReadOnly") != None:
                flexcomSym_Twi_Interrupt.setReadOnly(args["isReadOnly"])
            if args.get("isEnabled") != None:
                flexcomSym_Twi_Interrupt.setValue(args["isEnabled"])
            if args.get("isVisible") != None:
                flexcomSym_Twi_Interrupt.setVisible(args["isVisible"])
        else:
            result_dict["isSuccessful"] = "false"

    elif (messageID == "SPI_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_OperatingMode.setReadOnly(args["isReadOnly"])
            flexcomSym_SPI_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            flexcomSym_OperatingMode.setSelectedKey("SPI")
            flexcomSym_SPI_MR_MSTR.setValue("SLAVE")

    elif (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_OperatingMode.setReadOnly(args["isReadOnly"])
            flexcomSym_SPI_MR_MSTR.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            flexcomSym_OperatingMode.setSelectedKey("SPI")
            flexcomSym_SPI_MR_MSTR.setValue("MASTER")

    elif (messageID == "UART_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_UsartInterrupt.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            flexcomSym_UsartInterrupt.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            flexcomSym_UsartInterrupt.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_SPI_InterruptMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            flexcomSym_SPI_InterruptMode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            flexcomSym_SPI_InterruptMode.setVisible(args["isVisible"])

    elif (messageID == "UART_RING_BUFFER_MODE"):
        if args.get("isReadOnly") != None:
            flexcomSym_RingBuffer_Enable.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            flexcomSym_RingBuffer_Enable.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            flexcomSym_RingBuffer_Enable.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if args.get("isReadOnly") != None:
            flexcomSym_SPI_MR_PCS.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == False:
            flexcomSym_SPI_MR_PCS.setSelectedKey("GPIO")
        if args.get("isVisible") != None:
            flexcomSym_SPI_MR_PCS.setVisible(args["isVisible"])

    return result_dict

def flexcomInterruptEnableDisableCallback( uartInterruptEnableDisable, event ):
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()
    if (flexcom_mode != "NO_COM") and (Database.getSymbolValue(deviceNamespace, flexcom_mode + "_INTERRUPT_MODE") == True):
        Database.setSymbolValue( interruptNamespace, interruptSymbolEnable, True, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandler, flexcomInstanceName.getValue() + deviceHandlerLastName, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandlerLock, True, 2)
    else :
        #Do not try to restore the handler name to the default
        Database.setSymbolValue( interruptNamespace, interruptSymbolHandlerLock, False, 2)
        Database.setSymbolValue( interruptNamespace, interruptSymbolEnable, False, 2)

def dependencyStatus(symbol, event):
    if (event["value"] == False):
        status = True
    else :
        status = False

    if (event["id"] == interruptSymbolEnable):
        if ((Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x0)
        or (Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x1 and Database.getSymbolValue(deviceNamespace, "USART_INTERRUPT_MODE") == False)
        or (Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x2 and Database.getSymbolValue(deviceNamespace, "SPI_INTERRUPT_MODE") == False)
        or (Database.getSymbolValue(deviceNamespace, "FLEXCOM_MODE") == 0x3 and Database.getSymbolValue(deviceNamespace, "TWI_INTERRUPT_MODE") == False)):
            status = False

    symbol.setVisible(status)

def onCapabilityConnected(event):
    capability = event["capabilityID"]
    flexcomComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    if capability == uartCapabilityId:
        flexcomComponent.setCapabilityEnabled(uartCapabilityId, True)
        flexcomComponent.setCapabilityEnabled(spiCapabilityId, False)
        flexcomComponent.setCapabilityEnabled(i2cCapabilityId, False)
        flexcomSym_OperatingMode.setSelectedKey("USART", 2)
    elif capability == spiCapabilityId:
        flexcomComponent.setCapabilityEnabled(uartCapabilityId, False)
        flexcomComponent.setCapabilityEnabled(spiCapabilityId, True)
        flexcomComponent.setCapabilityEnabled(i2cCapabilityId, False)
        flexcomSym_OperatingMode.setSelectedKey("SPI", 2)
    elif capability == i2cCapabilityId:
        flexcomComponent.setCapabilityEnabled(uartCapabilityId, False)
        flexcomComponent.setCapabilityEnabled(spiCapabilityId, False)
        flexcomComponent.setCapabilityEnabled(i2cCapabilityId, True)
        flexcomSym_OperatingMode.setSelectedKey("TWI", 2)

    flexcomSym_OperatingMode.setReadOnly(True)

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : flexcomComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def onCapabilityDisconnected(event):
    capability = event["capabilityID"]
    flexcomComponent = event["localComponent"]

    flexcomComponent.setCapabilityEnabled(uartCapabilityId, True)
    flexcomComponent.setCapabilityEnabled(spiCapabilityId, True)
    flexcomComponent.setCapabilityEnabled(i2cCapabilityId, True)

    flexcomSym_OperatingMode.setSelectedKey("NO_COM", 2)

    flexcomSym_OperatingMode.setReadOnly(False)

def setFLEXCOMCodeGenerationProperty(symbol, event):
    global flexcomSym_RingBuffer_Enable
    global flexcomSym_Twi_OpMode
    global flexcomSym_SPI_MR_MSTR

    usartRingBufferMode = ""
    mode = ""
    modePath = ""
    ####################################### Code Generation  ##########################################
    configName = Variables.get("__CONFIGURATION_NAME")
    flexcom_mode = flexcomSym_OperatingMode.getSelectedKey()

    if flexcom_mode == "USART":
        if flexcomSym_RingBuffer_Enable.getValue() == True:
            usartRingBufferMode = "_ring_buffer"

    if flexcom_mode == "TWI":
        if flexcomSym_Twi_OpMode.getValue() == "MASTER":
            commonHeaderFile = "_master_common"
            mode = "_master"
            modePath = "/master"
        else:
            commonHeaderFile = "_slave_common"
            mode = "_slave"
            modePath = "/slave"
    elif flexcom_mode == "SPI":
        if flexcomSym_SPI_MR_MSTR.getValue() == "MASTER":
            commonHeaderFile = "_master_common"
            mode = "_master"
            modePath = "/master"
        else:
            commonHeaderFile = "_slave_common"
            mode = "_slave"
            modePath = "/slave"
    else:
        commonHeaderFile = "_local"

    if (flexcom_mode != "NO_COM"):
        flexcomHeaderFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/plib_flexcom_" + flexcom_mode.lower() + usartRingBufferMode + mode + ".h.ftl")
        flexcomHeaderFile.setOutputName("plib_" + deviceNamespace + "_" + flexcom_mode.lower() + mode + ".h")
        flexcomHeaderFile.setDestPath("/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
        flexcomHeaderFile.setProjectPath("config/" + configName + "/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
        flexcomHeaderFile.setType("HEADER")
        flexcomHeaderFile.setMarkup(True)
        flexcomHeaderFile.setEnabled(True)

        if flexcom_mode == "SPI" and flexcomSym_SPI_MR_MSTR.getValue() == "MASTER":
            flexcomCommonHeaderFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/plib_flexcom_" + flexcom_mode.lower() + commonHeaderFile + ".h.ftl")
            flexcomCommonHeaderFile.setOutputName("plib_flexcom_" + flexcom_mode.lower() + commonHeaderFile + ".h")
            flexcomCommonHeaderFile.setDestPath("/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
            flexcomCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
            flexcomCommonHeaderFile.setType("HEADER")
            flexcomCommonHeaderFile.setMarkup(True)
            flexcomCommonHeaderFile.setEnabled(True)
        else:
            flexcomCommonHeaderFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/plib_flexcom_" + flexcom_mode.lower() + commonHeaderFile + ".h")
            flexcomCommonHeaderFile.setOutputName("plib_flexcom_" + flexcom_mode.lower() + commonHeaderFile + ".h")
            flexcomCommonHeaderFile.setDestPath("/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
            flexcomCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
            flexcomCommonHeaderFile.setType("HEADER")
            flexcomCommonHeaderFile.setEnabled(True)

        flexcomSourceFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/plib_flexcom" + "_" + flexcom_mode.lower() + usartRingBufferMode + mode + ".c.ftl")
        flexcomSourceFile.setOutputName("plib_" + deviceNamespace + "_" + flexcom_mode.lower() + mode + ".c")
        flexcomSourceFile.setDestPath("/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
        flexcomSourceFile.setProjectPath("config/" + configName + "/peripheral/flexcom/" + flexcom_mode.lower() + modePath + "/")
        flexcomSourceFile.setType("SOURCE")
        flexcomSourceFile.setMarkup(True)
        flexcomSourceFile.setEnabled(True)

        flexcomSystemInitFile.setType("STRING")
        flexcomSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        flexcomSystemInitFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/system/initialization.c.ftl")
        flexcomSystemInitFile.setMarkup(True)

        flexcomSystemDefFile.setType("STRING")
        flexcomSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        flexcomSystemDefFile.setSourcePath("../peripheral/flexcom_" + flexcomModuleID + "/templates/system/definitions.h.ftl")
        flexcomSystemDefFile.setMarkup(True)
    else:
        flexcomHeaderFile.setEnabled(False)
        flexcomCommonHeaderFile.setEnabled(False)
        flexcomSourceFile.setEnabled(False)

    component = symbol.getComponent()
    if event["id"] == "FLEXCOM_MODE":
        if event["value"] == 0x1:
            component.setCapabilityEnabled(uartCapabilityId, True)
            component.setCapabilityEnabled(spiCapabilityId, False)
            component.setCapabilityEnabled(i2cCapabilityId, False)
        elif event["value"] == 0x2:
            component.setCapabilityEnabled(uartCapabilityId, False)
            component.setCapabilityEnabled(spiCapabilityId, True)
            component.setCapabilityEnabled(i2cCapabilityId, False)
        elif event["value"] == 0x3:
            component.setCapabilityEnabled(uartCapabilityId, False)
            component.setCapabilityEnabled(spiCapabilityId, False)
            component.setCapabilityEnabled(i2cCapabilityId, True)
        else:
            component.setCapabilityEnabled(uartCapabilityId, True)
            component.setCapabilityEnabled(spiCapabilityId, True)
            component.setCapabilityEnabled(i2cCapabilityId, True)

def updateFLEXCOMTxDataRegister(symbol, event):

    symObj = event["symbol"]

    if symObj.getSelectedKey() == "USART":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_US_THR)", 2)
    elif symObj.getSelectedKey() == "SPI":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_SPI_TDR)", 2)
    elif symObj.getSelectedKey() == "TWI":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_TWI_THR)", 2)
    else:
        symbol.setValue("", 2)

def updateFLEXCOMRxDataRegister(symbol, event):

    symObj = event["symbol"]

    if symObj.getSelectedKey() == "USART":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_US_RHR)", 2)
    elif symObj.getSelectedKey() == "SPI":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_SPI_RDR)", 2)
    elif symObj.getSelectedKey() == "TWI":
        symbol.setValue("&(" + flexcomInstanceName.getValue() + "_REGS->FLEX_TWI_RHR)", 2)
    else:
        symbol.setValue("", 2)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def destroyComponent(flexcomComponent):
    Database.clearSymbolValue( interruptNamespace, interruptSymbolEnable)
    Database.clearSymbolValue( interruptNamespace, interruptSymbolHandler)
    Database.clearSymbolValue( interruptNamespace, interruptSymbolHandlerLock)

def instantiateComponent(flexcomComponent):
    global uartCapabilityId
    global spiCapabilityId
    global i2cCapabilityId
    global flexcomSym_OperatingMode
    global flexcomInstanceName
    global deviceNamespace
    global interruptNamespace
    global deviceHandlerLastName
    global interruptSymbolEnable
    global interruptSymbolHandler
    global interruptSymbolHandlerLock
    global flexcomClockInvalidSym
    pdcSupported = None
    flexcomInstanceName = flexcomComponent.createStringSymbol("FLEXCOM_INSTANCE_NAME", None)
    flexcomInstanceName.setVisible(False)
    flexcomInstanceName.setDefaultValue(flexcomComponent.getID().upper())

    flexcomInstanceNumber = flexcomComponent.createStringSymbol("FLEXCOM_INSTANCE_NUMBER", None)
    flexcomInstanceNumber.setVisible(False)
    flexcomInstanceNumber.setDefaultValue(flexcomComponent.getID().replace("flexcom",""))

    Log.writeInfoMessage("Running " + flexcomInstanceName.getValue())

    uartCapabilityId = flexcomInstanceName.getValue() + "_UART"
    spiCapabilityId = flexcomInstanceName.getValue() + "_SPI"
    i2cCapabilityId = flexcomInstanceName.getValue() + "_I2C"
    interruptNamespace = "core"
    deviceNamespace = flexcomComponent.getID().lower()
    deviceHandlerLastName = "_InterruptHandler"
    interruptSymbolEnable = flexcomInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptSymbolHandler = flexcomInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptSymbolHandlerLock =  flexcomInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"

    #Flexcom Mode - NO_COM, USART, SPI, TWI
    flexcomSym_OperatingMode = flexcomComponent.createKeyValueSetSymbol("FLEXCOM_MODE", None)
    flexcomSym_OperatingMode.setLabel("FLEXCOM Operating Mode")

    flexcomSym_OperatingMode_Node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]/value-group@[name=\"FLEXCOM_MR__OPMODE\"]")
    flexcomSym_OperatingMode_Values = []
    flexcomSym_OperatingMode_Values = flexcomSym_OperatingMode_Node.getChildren()

    for index in range(len(flexcomSym_OperatingMode_Values)):
        flexcomSym_OperatingMode_Key_Name = flexcomSym_OperatingMode_Values[index].getAttribute("name")
        flexcomSym_OperatingMode_Key_Description = flexcomSym_OperatingMode_Values[index].getAttribute("caption")
        flexcomSym_OperatingMode_Key_Value = flexcomSym_OperatingMode_Values[index].getAttribute("value")
        flexcomSym_OperatingMode.addKey(flexcomSym_OperatingMode_Key_Name, flexcomSym_OperatingMode_Key_Value, flexcomSym_OperatingMode_Key_Description)

    flexcomSym_OperatingMode.setDefaultValue(0)
    flexcomSym_OperatingMode.setOutputMode("Key")
    flexcomSym_OperatingMode.setDisplayMode("Key")

    ###################### CLK and AIC Dependencies ######################
    # Initial settings for CLK
    Database.setSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    # Interrupt Dynamic Settings
    flexcomSym_InterruptControl = flexcomComponent.createBooleanSymbol("FLEXCOM_INTERRUPT_ENABLE", None)
    flexcomSym_InterruptControl.setDependencies(flexcomInterruptEnableDisableCallback, ["USART_INTERRUPT_MODE", "SPI_INTERRUPT_MODE", "TWI_INTERRUPT_MODE", "FLEXCOM_MODE"])
    flexcomSym_InterruptControl.setVisible(False)

    # Dependency Status
    flexcomSym_ClkEnComment = flexcomComponent.createCommentSymbol("FLEXCOM_CLK_ENABLE_COMMENT", None)
    if Database.getSymbolValue("core", flexcomInstanceName.getValue() + "_CLOCK_ENABLE"):
        flexcomSym_ClkEnComment.setVisible(False)
    flexcomSym_ClkEnComment.setLabel("Warning!!! " + flexcomComponent.getID().upper() + " Peripheral Clock is Disabled in Clock Manager")
    flexcomSym_ClkEnComment.setDependencies(dependencyStatus, ["core." + flexcomInstanceName.getValue() + "_CLOCK_ENABLE"])

    flexcomSym_IntEnComment = flexcomComponent.createCommentSymbol("FLEXCOM_AIC_ENABLE_COMMENT", None)
    flexcomSym_IntEnComment.setVisible(False)
    flexcomSym_IntEnComment.setLabel("Warning!!! " + flexcomComponent.getID().upper() + " Interrupt is Disabled in Interrupt Manager")
    flexcomSym_IntEnComment.setDependencies(dependencyStatus, ["core." + interruptSymbolEnable])

    flexcomClockInvalidSym = flexcomComponent.createCommentSymbol("FLEXCOM_CLOCK_INVALID_COMMENT", None)
    flexcomClockInvalidSym.setLabel(flexcomComponent.getID().upper() + " clock frequency is too low for required baud rate")
    flexcomClockInvalidSym.setVisible(False)

    ###################### Code Generation ######################
    global flexcomHeaderFile
    global flexcomCommonHeaderFile
    global flexcomSourceFile
    global flexcomSystemInitFile
    global flexcomSystemDefFile
    global flexcomModuleID
    flexcomHeaderFile = flexcomComponent.createFileSymbol(flexcomInstanceName.getValue() + "_HEADER", None)
    flexcomCommonHeaderFile = flexcomComponent.createFileSymbol(flexcomInstanceName.getValue() + "_COMMON_HEADER", None)
    flexcomSourceFile = flexcomComponent.createFileSymbol(flexcomInstanceName.getValue() + "_SOURCE", None)
    flexcomSystemInitFile = flexcomComponent.createFileSymbol("FLEXCOM_SYS_INIT", None)
    flexcomSystemDefFile = flexcomComponent.createFileSymbol("FLEXCOM_SYS_DEF", None)
    flexcomSym_CodeGeneration = flexcomComponent.createIntegerSymbol("FLEXCOM_CODE_GENERATION", None)
    flexcomSym_CodeGeneration.setDefaultValue(flexcomSym_OperatingMode.getValue())
    flexcomSym_CodeGeneration.setVisible(False)
    flexcomSym_CodeGeneration.setDependencies(setFLEXCOMCodeGenerationProperty, ["FLEXCOM_MODE", "USART_RING_BUFFER_ENABLE", "FLEXCOM_TWI_OPMODE", "FLEXCOM_SPI_MR_MSTR"])
    flexcomModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FLEXCOM\"]")
    flexcomModuleID = flexcomModuleNode.getAttribute("id")

    ###################### Driver Symbols for DMA Transfer ######################
    #FLEXCOM Transmit data register
    flexcomSym_TxRegister = flexcomComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", flexcomSym_OperatingMode)
    flexcomSym_TxRegister.setDefaultValue("")
    flexcomSym_TxRegister.setVisible(False)
    flexcomSym_TxRegister.setDependencies(updateFLEXCOMTxDataRegister, ["FLEXCOM_MODE"])

    #FLEXCOM Receive data register
    flexcomSym_RxRegister = flexcomComponent.createStringSymbol("RECEIVE_DATA_REGISTER", flexcomSym_OperatingMode)
    flexcomSym_RxRegister.setDefaultValue("")
    flexcomSym_RxRegister.setVisible(False)
    flexcomSym_RxRegister.setDependencies(updateFLEXCOMRxDataRegister, ["FLEXCOM_MODE"])

    ###################### USART, SPI and TWI Sub-modules ######################
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/flexcom_" + flexcomModuleID + "/config/flexcom_usart.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/flexcom_" + flexcomModuleID + "/config/flexcom_spi.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/flexcom_" + flexcomModuleID + "/config/flexcom_twi.py")
