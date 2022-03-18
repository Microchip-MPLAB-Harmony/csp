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

global twihsInstanceName

#operation mode
opModeValues = ["MASTER", "SLAVE"]

def handleMessage(messageID, args):
    global twihsOpMode
    global twihsSym_Interrupt_Mode

    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None:
            twihsOpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            twihsOpMode.setValue("MASTER")

    elif (messageID == "I2C_SLAVE_MODE"):
        if args.get("isReadOnly") != None:
            twihsOpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            twihsOpMode.setValue("SLAVE")

    elif (messageID == "I2C_SLAVE_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            twihsSym_Interrupt_Mode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            twihsSym_Interrupt_Mode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            twihsSym_Interrupt_Mode.setVisible(args["isVisible"])

    return result_dict

def getMasterClockFreq():

    return int(Database.getSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CLK_SRC_FREQ"))

def getTWIHSClkSpeed():

    return Database.getSymbolValue(twihsInstanceName.getValue().lower(), "I2C_CLOCK_SPEED")

def getTWIHSLowLevelTimeLimit():

    return 384000

def getTWIHSClockDividerMaxValue():

    return 255

def getTWIHSClockDividerMinValue():

    return 7

def getTWIHSClockDividerValue(twihsClkSpeed):

    cldiv = 0
    chdiv = 0
    ckdiv = 0

    masterClockFreq = getMasterClockFreq()

    if twihsClkSpeed > getTWIHSLowLevelTimeLimit():
        cldiv = masterClockFreq // ( getTWIHSLowLevelTimeLimit() * 2) - 3
        chdiv = masterClockFreq // ((twihsClkSpeed + (twihsClkSpeed - getTWIHSLowLevelTimeLimit())) * 2 ) - 3

        while cldiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        while chdiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            chdiv //= 2
    else:
        cldiv = masterClockFreq / ( twihsClkSpeed * 2 ) - 3

        while cldiv > getTWIHSClockDividerMaxValue() and ckdiv < getTWIHSClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        chdiv = cldiv

    return cldiv, chdiv, ckdiv

def updateInterruptModeVisibility(symbol, event):
    opMode = event["source"].getSymbolByID("TWIHS_OPMODE").getValue()

    if opMode == "MASTER":
        symbol.setReadOnly(True)
        symbol.setValue(True)
    else:
        symbol.setReadOnly(False)

def updateNVICInterrupt(symbol, event):
    global twihsInstanceName

    interruptEnable = event["source"].getSymbolByID("TWIHS_INTERRUPT_MODE").getValue()

    if interruptEnable == True:
        interruptHandlerName = twihsInstanceName.getValue() + "_InterruptHandler"
    else:
        interruptHandlerName = twihsInstanceName.getValue() + "_Handler"

    # Initialize peripheral Interrupt
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_ENABLE", interruptEnable, 1)

    # Set Interrupt Handler Name
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER", interruptHandlerName, 1)

    # Set Interrupt Handler Lock
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK", interruptEnable, 1)

def showMasterDependencies(symbol, event):
    opMode = event["source"].getSymbolByID("TWIHS_OPMODE").getValue()
    symbol.setVisible(opMode == "MASTER")

def showSlaveDependencies(symbol, event):
    opMode = event["source"].getSymbolByID("TWIHS_OPMODE").getValue()
    symbol.setVisible(opMode == "SLAVE")

def twihsMasterModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "MASTER")

def twihsSlaveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["symbol"].getValue() == "SLAVE")

################################################################################
#### Business Logic ####
################################################################################

def setClockDividerValue(symbol, event):

    global twihsInstanceName
    cldiv, chdiv, ckdiv = getTWIHSClockDividerValue(getTWIHSClkSpeed())

    if cldiv < 0 or cldiv > getTWIHSClockDividerMaxValue():
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

        Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CLDIV", cldiv, 1)
        Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CHDIV", chdiv, 1)
        Database.setSymbolValue(twihsInstanceName.getValue().lower(), "TWIHS_CWGR_CKDIV", ckdiv, 1)

def updateClockWarning(symbol, event):
    global twihsInstanceName

    clockEnabled = bool(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_ENABLE"))
    symbol.setVisible(clockEnabled == False)

def updateInterruptWarning(symbol, event):
    global twihsInstanceName

    nvic_interrupt_status = bool(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"))
    isInterruptEnabled = event["source"].getSymbolByID("TWIHS_INTERRUPT_MODE").getValue()

    symbol.setVisible(isInterruptEnabled == True and nvic_interrupt_status == True)

def setClockSourceFreq(symbol, event):

    if event["id"] == "TWIHS_OPMODE":
        opMode = event["source"].getSymbolByID("TWIHS_OPMODE").getValue()
        symbol.setVisible(opMode == "MASTER")
    else:
        symbol.setValue(event["value"], 2)

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def updateI2CBaudHz(symbol, event):
    symbol.setValue(event["value"])

def updateTimeoutCount(symbol, event):
    # Counter value obtained by dividing CPU clock frequency with 5000 gives a delay of 200usec (enough to transmit 10 bits of I2C running at 50 kHz).
    # 200usec delay assumes each instruction takes 1 CPU clock to execute. In practice the delay will be ~10 times higher, roughly 2-3 msec.
    symbol.setValue(int(event["value"])/5000)
################################################################################
#### Component ####
################################################################################

def instantiateComponent(twihsComponent):

    global twihsInstanceName
    global twihsSymClockInvalid
    global twihsOpMode
    global twihsSym_Interrupt_Mode

    twihsInstanceName = twihsComponent.createStringSymbol("TWIHS_INSTANCE_NAME", None)
    twihsInstanceName.setVisible(False)
    twihsInstanceName.setDefaultValue(twihsComponent.getID().upper())

    twihsBitField_CR_THRCLR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TWIHS"]/register-group@[name="TWIHS"]/register@[name="TWIHS_CR"]/bitfield@[name="THRCLR"]')
    twihsBitField_SMR_NACKEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TWIHS"]/register-group@[name="TWIHS"]/register@[name="TWIHS_SMR"]/bitfield@[name="NACKEN"]')

    twihsSym_CR_THRCLR = twihsComponent.createBooleanSymbol("TWIHS_CR_THRCLR", None)
    twihsSym_CR_THRCLR.setVisible(False)
    twihsSym_CR_THRCLR.setDefaultValue(twihsBitField_CR_THRCLR != None)

    twihsSym_SMR_NACKEN = twihsComponent.createBooleanSymbol("TWIHS_SMR_NACKEN", None)
    twihsSym_SMR_NACKEN.setVisible(False)
    twihsSym_SMR_NACKEN.setDefaultValue(twihsBitField_SMR_NACKEN != None)

    twihsOpMode = twihsComponent.createComboSymbol("TWIHS_OPMODE", None, opModeValues)
    twihsOpMode.setLabel("TWIHS Operation Mode")
    twihsOpMode.setDefaultValue("MASTER")

    # Provide a source clock selection symbol for masks that supports it
    valueGroup = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TWIHS\"]/value-group@[name=\"TWIHS_CWGR__CKSRC\"]")
    if valueGroup is not None:
        values = valueGroup.getChildren()
        twihsSymClockSrc = twihsComponent.createKeyValueSetSymbol("TWIHS_CLK_SRC", None)
        twihsSymClockSrc.setLabel(valueGroup.getAttribute("caption"))
        for index in range(len(values)):
            twihsSymClockSrc.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"), values[index].getAttribute("caption"))
        twihsSymClockSrc.setOutputMode("Key")
        twihsSymClockSrc.setDisplayMode("Key")

    # Source Clock Frequency
    twihsSymMasterClkFreq = twihsComponent.createIntegerSymbol("TWIHS_CLK_SRC_FREQ", None)
    twihsSymMasterClkFreq.setLabel("Source Clock Frequency (Hz)")
    twihsSymMasterClkFreq.setReadOnly(True)
    twihsSymMasterClkFreq.setVisible(twihsOpMode.getValue() == "MASTER")
    twihsSymMasterClkFreq.setDefaultValue(int(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    twihsSymMasterClkFreq.setDependencies(setClockSourceFreq, ["core." + twihsInstanceName.getValue() + "_CLOCK_FREQUENCY", "TWIHS_OPMODE"])

    # Clock speed
    twihsSymClockSpeed = twihsComponent.createIntegerSymbol("I2C_CLOCK_SPEED", None)
    twihsSymClockSpeed.setLabel("Clock Speed (Hz)")
    twihsSymClockSpeed.setDefaultValue(400000)
    twihsSymClockSpeed.setMax(400000)
    twihsSymClockSpeed.setDependencies(showMasterDependencies, ["TWIHS_OPMODE"])
    
    # Clock speed (Hz)
    twihsSymClockSpeedHz = twihsComponent.createIntegerSymbol("I2C_CLOCK_SPEED_HZ", None)
    twihsSymClockSpeedHz.setLabel("Clock Speed (Hz)")
    twihsSymClockSpeedHz.setDefaultValue(twihsSymClockSpeed.getValue())
    twihsSymClockSpeedHz.setVisible(False)
    twihsSymClockSpeedHz.setDependencies(updateI2CBaudHz, ["I2C_CLOCK_SPEED"])


    # Slave Address
    twihsSym_ADDR = twihsComponent.createHexSymbol("TWIHS_SLAVE_ADDRESS", None)
    twihsSym_ADDR.setLabel("I2C Slave Address (7-bit)")
    twihsSym_ADDR.setMax(1023)
    twihsSym_ADDR.setVisible(False)
    twihsSym_ADDR.setDefaultValue(0x54)
    twihsSym_ADDR.setDependencies(showSlaveDependencies, ["TWIHS_OPMODE"])

    #I2C Interrupt Mode
    twihsSym_Interrupt_Mode = twihsComponent.createBooleanSymbol("TWIHS_INTERRUPT_MODE", None)
    twihsSym_Interrupt_Mode.setLabel("Enable Interrupts ?")
    twihsSym_Interrupt_Mode.setDefaultValue(True)
    twihsSym_Interrupt_Mode.setReadOnly(twihsOpMode.getValue() == "MASTER")
    twihsSym_Interrupt_Mode.setDependencies(updateInterruptModeVisibility, ["TWIHS_OPMODE"])

    twihsSym_Interrupt_Update = twihsComponent.createBooleanSymbol("TWIHS_INTERRUPT_UPDATE", None)
    twihsSym_Interrupt_Update.setLabel("Interrupt Update")
    twihsSym_Interrupt_Update.setVisible(False)
    twihsSym_Interrupt_Update.setDependencies(updateNVICInterrupt, ["TWIHS_OPMODE", "TWIHS_INTERRUPT_MODE"])

    #clock invalid comment
    twihsSymClockInvalid = twihsComponent.createCommentSymbol("TW_HS_INVALID_CLOCK", None)
    twihsSymClockInvalid.setLabel("Cannot generate required clock speed from configured clock source !!!")
    twihsSymClockInvalid.setVisible(False)

    cldiv, chdiv, ckdiv = getTWIHSClockDividerValue(twihsSymClockSpeed.getValue())

    #Clock Divider
    twihsSymDivider = twihsComponent.createStringSymbol("TWIHS_DIVIDER", None)
    twihsSymDivider.setVisible(False)
    twihsSymDivider.setDependencies(setClockDividerValue, ["I2C_CLOCK_SPEED", "TWIHS_CLK_SRC_FREQ"])

    #CLDIV
    twihsSym_CWGR_CLDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CLDIV", None)
    twihsSym_CWGR_CLDIV.setVisible(False)
    twihsSym_CWGR_CLDIV.setDefaultValue(cldiv)

    #CHDIV
    twihsSym_CWGR_CHDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CHDIV", None)
    twihsSym_CWGR_CHDIV.setVisible(False)
    twihsSym_CWGR_CHDIV.setDefaultValue(chdiv)

    #CKDIV
    twihsSym_CWGR_CKDIV = twihsComponent.createIntegerSymbol("TWIHS_CWGR_CKDIV", None)
    twihsSym_CWGR_CKDIV.setVisible(False)
    twihsSym_CWGR_CKDIV.setDefaultValue(ckdiv)

    # Initialize peripheral clock
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_ENABLE")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    # Initialize peripheral Interrupt
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "INTERRUPT_ENABLE")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_ENABLE", True, 1)

    # Set Interrupt Handler Name
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER", twihsInstanceName.getValue() + "_InterruptHandler", 1)

    # Set Interrupt Handler Lock
    Database.clearSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK")
    Database.setSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK", True, 1)

    # Warning for change in Clock Enable Symbol
    twihsSymClkEnComment = twihsComponent.createCommentSymbol("TWIHS_CLK_EN_COMMENT", None)
    twihsSymClkEnComment.setVisible(bool(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_ENABLE")) == False)
    twihsSymClkEnComment.setLabel("Warning!!! TWIHS Peripheral Clock is Disabled in Clock Manager")
    twihsSymClkEnComment.setDependencies(updateClockWarning, ["core." + twihsInstanceName.getValue() + "_CLOCK_ENABLE"])

    # Warning for change in Interrupt Enable Symbol
    twihsSymIntEnComment = twihsComponent.createCommentSymbol("TWIHS_INT_EN_COMMENT", None)
    twihsSymIntEnComment.setVisible(bool(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE")) == True)
    twihsSymIntEnComment.setLabel("Warning!!! TWIHS Interrupt is Disabled in Interrupt Manager")
    twihsSymIntEnComment.setDependencies(updateInterruptWarning, ["core." + twihsInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"])

    #TWIHS API Prefix
    twihsSymAPIPrefix = twihsComponent.createStringSymbol("I2C_PLIB_API_PREFIX", None)
    twihsSymAPIPrefix.setDefaultValue(twihsInstanceName.getValue())
    twihsSymAPIPrefix.setVisible(False)

    cpu_clock = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))

    twihsSym_TimeoutCountVal = twihsComponent.createIntegerSymbol("TWIHS_TIMEOUT_COUNT_VAL", None)
    twihsSym_TimeoutCountVal.setVisible(False)
    twihsSym_TimeoutCountVal.setDefaultValue(cpu_clock/5000)
    twihsSym_TimeoutCountVal.setDependencies(updateTimeoutCount, ["core.CPU_CLOCK_FREQUENCY"])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # TWIHS Master Common Header
    twihsMasterCommonHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MASTER_HEADER", None)
    twihsMasterCommonHeaderFile.setSourcePath("../peripheral/twihs_11210/plib_twihs_master_common.h")
    twihsMasterCommonHeaderFile.setOutputName("plib_twihs_master_common.h")
    twihsMasterCommonHeaderFile.setDestPath("/peripheral/twihs/master/")
    twihsMasterCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/master/")
    twihsMasterCommonHeaderFile.setType("HEADER")
    twihsMasterCommonHeaderFile.setEnabled(twihsOpMode.getValue() == "MASTER")
    twihsMasterCommonHeaderFile.setDependencies(twihsMasterModeFileGeneration, ["TWIHS_OPMODE"])

    # TWIHS Master Source File
    twihsMasterSourceFile = twihsComponent.createFileSymbol("TWIHS_FILE_SRC_MAIN", None)
    twihsMasterSourceFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs_master.c.ftl")
    twihsMasterSourceFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + "_master.c")
    twihsMasterSourceFile.setDestPath("/peripheral/twihs/master")
    twihsMasterSourceFile.setProjectPath("config/" + configName + "/peripheral/twihs/master")
    twihsMasterSourceFile.setType("SOURCE")
    twihsMasterSourceFile.setMarkup(True)
    twihsMasterSourceFile.setEnabled(twihsOpMode.getValue() == "MASTER")
    twihsMasterSourceFile.setDependencies(twihsMasterModeFileGeneration, ["TWIHS_OPMODE"])

    # TWIHS Master Header File
    twihsMasterHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MAIN_HEADER", None)
    twihsMasterHeaderFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs_master.h.ftl")
    twihsMasterHeaderFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + "_master.h")
    twihsMasterHeaderFile.setDestPath("/peripheral/twihs/master")
    twihsMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/master")
    twihsMasterHeaderFile.setType("HEADER")
    twihsMasterHeaderFile.setMarkup(True)
    twihsMasterHeaderFile.setEnabled(twihsOpMode.getValue() == "MASTER")
    twihsMasterHeaderFile.setDependencies(twihsMasterModeFileGeneration, ["TWIHS_OPMODE"])

    # TWIHS Slave Common Header
    twihsSlaveCommonHeaderFile = twihsComponent.createFileSymbol("TWIHS_SLAVE_COMMON_HEADER", None)
    twihsSlaveCommonHeaderFile.setSourcePath("../peripheral/twihs_11210/plib_twihs_slave_common.h")
    twihsSlaveCommonHeaderFile.setOutputName("plib_twihs_slave_common.h")
    twihsSlaveCommonHeaderFile.setDestPath("/peripheral/twihs/slave/")
    twihsSlaveCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/slave/")
    twihsSlaveCommonHeaderFile.setType("HEADER")
    twihsSlaveCommonHeaderFile.setEnabled(twihsOpMode.getValue() == "SLAVE")
    twihsSlaveCommonHeaderFile.setDependencies(twihsSlaveModeFileGeneration, ["TWIHS_OPMODE"])

    # TWIHS Slave Source File
    twihsSlaveSourceFile = twihsComponent.createFileSymbol("TWIHS_SLAVE_SOURCE", None)
    twihsSlaveSourceFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs_slave.c.ftl")
    twihsSlaveSourceFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + "_slave.c")
    twihsSlaveSourceFile.setDestPath("/peripheral/twihs/slave")
    twihsSlaveSourceFile.setProjectPath("config/" + configName + "/peripheral/twihs/slave")
    twihsSlaveSourceFile.setType("SOURCE")
    twihsSlaveSourceFile.setMarkup(True)
    twihsSlaveSourceFile.setEnabled(twihsOpMode.getValue() == "SLAVE")
    twihsSlaveSourceFile.setDependencies(twihsSlaveModeFileGeneration, ["TWIHS_OPMODE"])

    # TWIHS Slave Header File
    twihsInstHeaderFile = twihsComponent.createFileSymbol("TWIHS_SLAVE_HEADER", None)
    twihsInstHeaderFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs_slave.h.ftl")
    twihsInstHeaderFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + "_slave.h")
    twihsInstHeaderFile.setDestPath("/peripheral/twihs/slave")
    twihsInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/slave")
    twihsInstHeaderFile.setType("HEADER")
    twihsInstHeaderFile.setMarkup(True)
    twihsInstHeaderFile.setEnabled(twihsOpMode.getValue() == "SLAVE")
    twihsInstHeaderFile.setDependencies(twihsSlaveModeFileGeneration, ["TWIHS_OPMODE"])

    #TWIHS Initialize
    twihsSystemInitFile = twihsComponent.createFileSymbol("TWIHS_FILE_SYS_INIT", None)
    twihsSystemInitFile.setType("STRING")
    twihsSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    twihsSystemInitFile.setSourcePath("../peripheral/twihs_11210/templates/system/initialization.c.ftl")
    twihsSystemInitFile.setMarkup(True)

    #TWIHS definitions header
    twihsSystemDefFile = twihsComponent.createFileSymbol("TWIHS_FILE_SYS_DEF", None)
    twihsSystemDefFile.setType("STRING")
    twihsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    twihsSystemDefFile.setSourcePath("../peripheral/twihs_11210/templates/system/definitions.h.ftl")
    twihsSystemDefFile.setMarkup(True)
