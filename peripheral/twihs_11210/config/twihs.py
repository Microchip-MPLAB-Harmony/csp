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

    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None and args["isReadOnly"] == True:
            twihsOpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            twihsOpMode.setValue("MASTER")

    #elif (messageID == "I2C_SLAVE_MODE"):
        # To be implemented

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

def setEnCommentVisibility(symbol, event):

    symbol.setVisible(event["value"])

def setClockSourceFreq(symbol, event):

    symbol.setValue(event["value"], 2)

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(twihsComponent):

    global twihsInstanceName
    global twihsSymClockInvalid
    global twihsOpMode

    twihsInstanceName = twihsComponent.createStringSymbol("TWIHS_INSTANCE_NAME", None)
    twihsInstanceName.setVisible(False)
    twihsInstanceName.setDefaultValue(twihsComponent.getID().upper())

    twihsBitField_CR_THRCLR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TWIHS"]/register-group@[name="TWIHS"]/register@[name="TWIHS_CR"]/bitfield@[name="THRCLR"]')

    twihsSym_CR_THRCLR = twihsComponent.createBooleanSymbol("TWIHS_CR_THRCLR", None)
    twihsSym_CR_THRCLR.setVisible(False)
    twihsSym_CR_THRCLR.setDefaultValue(twihsBitField_CR_THRCLR != None)

    twihsOpMode = twihsComponent.createComboSymbol("TWIHS_OPMODE", None, opModeValues)
    twihsOpMode.setLabel("TWIHS Operation Mode")
    twihsOpMode.setDefaultValue("MASTER")
    twihsOpMode.setReadOnly(True)

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
    twihsSymMasterClkFreq.setDefaultValue(int(Database.getSymbolValue("core", twihsInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    twihsSymMasterClkFreq.setDependencies(setClockSourceFreq, ["core." + twihsInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    # Clock speed
    twihsSymClockSpeed = twihsComponent.createIntegerSymbol("I2C_CLOCK_SPEED", None)
    twihsSymClockSpeed.setLabel("Clock Speed")
    twihsSymClockSpeed.setDefaultValue(400000)
    twihsSymClockSpeed.setMax(400000)

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
    twihsSymClkEnComment.setVisible(False)
    twihsSymClkEnComment.setLabel("Warning!!! TWIHS Peripheral Clock is Disabled in Clock Manager")
    twihsSymClkEnComment.setDependencies(setEnCommentVisibility, ["core."+twihsInstanceName.getValue()+"_CLOCK_ENABLE"])

    # Warning for change in Interrupt Enable Symbol
    twihsSymIntEnComment = twihsComponent.createCommentSymbol("TWIHS_INT_EN_COMMENT", None)
    twihsSymIntEnComment.setVisible(False)
    twihsSymIntEnComment.setLabel("Warning!!! TWIHS Interrupt is Disabled in Interrupt Manager")
    twihsSymIntEnComment.setDependencies(setEnCommentVisibility, ["core."+twihsInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"])

    #TWIHS API Prefix
    twihsSymAPIPrefix = twihsComponent.createStringSymbol("I2C_PLIB_API_PREFIX", None)
    twihsSymAPIPrefix.setDefaultValue(twihsInstanceName.getValue())
    twihsSymAPIPrefix.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    #Master Header
    twihsMasterHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MASTER_HEADER", None)
    twihsMasterHeaderFile.setSourcePath("../peripheral/twihs_11210/plib_twihs_master.h")
    twihsMasterHeaderFile.setOutputName("plib_twihs_master.h")
    twihsMasterHeaderFile.setDestPath("/peripheral/twihs/")
    twihsMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsMasterHeaderFile.setType("HEADER")

    #Source File
    twihsMainSourceFile = twihsComponent.createFileSymbol("TWIHS_FILE_SRC_MAIN", None)
    twihsMainSourceFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs.c.ftl")
    twihsMainSourceFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + ".c")
    twihsMainSourceFile.setDestPath("/peripheral/twihs/")
    twihsMainSourceFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsMainSourceFile.setType("SOURCE")
    twihsMainSourceFile.setMarkup(True)

    #Instance Header File
    twihsInstHeaderFile = twihsComponent.createFileSymbol("TWIHS_FILE_MAIN_HEADER", None)
    twihsInstHeaderFile.setSourcePath("../peripheral/twihs_11210/templates/plib_twihs.h.ftl")
    twihsInstHeaderFile.setOutputName("plib_" + twihsInstanceName.getValue().lower() + ".h")
    twihsInstHeaderFile.setDestPath("/peripheral/twihs/")
    twihsInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/twihs/")
    twihsInstHeaderFile.setType("HEADER")
    twihsInstHeaderFile.setMarkup(True)

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
