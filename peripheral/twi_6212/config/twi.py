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

################################################################################
#### Business Logic ####
################################################################################
global getTwiClockDividerValue

#Operation Mode
twiOpModeValues = ["MASTER"]

def handleMessage(messageID, args):
    global twiOpMode

    result_dict = {}

    if (messageID == "I2C_MASTER_MODE"):
        if args.get("isReadOnly") != None and args["isReadOnly"] == True:
            twiOpMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            twiOpMode.setValue("MASTER")

    #elif (messageID == "I2C_SLAVE_MODE"):
        # To be implemented

    return result_dict

def getTwiClockDividerValue(twiClkSpeed):
    ckdiv = 0
    clockDividerMaxValue = 255
    clockDividerMinValue = 7

    peripheralClockFreq = int(Database.getSymbolValue("core", twiInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    cldiv = peripheralClockFreq / ( twiClkSpeed * 2 ) - 4

    while int(cldiv) > clockDividerMaxValue and ckdiv < clockDividerMinValue:
        ckdiv += 1
        cldiv /= 2
    chdiv = cldiv

    return int(cldiv), int(chdiv), ckdiv

def setTwiClockDividerValue(symbol, event):
    cldiv, chdiv, ckdiv = getTwiClockDividerValue(Database.getSymbolValue(twiInstanceName.getValue().lower(), "I2C_CLOCK_SPEED"))

    if cldiv < 0 or cldiv > 255:
        twiClockInvalidSymbol.setVisible(True)
    else:
        twiClockInvalidSymbol.setVisible(False)

    # set CLDIV Value
    Database.setSymbolValue(twiInstanceName.getValue().lower(), "TWI_CWGR_CLDIV", cldiv)
    # set CHDIV Value
    Database.setSymbolValue(twiInstanceName.getValue().lower(), "TWI_CWGR_CHDIV", chdiv)
    # set CKDIV Value
    Database.setSymbolValue(twiInstanceName.getValue().lower(), "TWI_CWGR_CKDIV", ckdiv)

def setTwiClockSourceFreq(symbol, event):
    symbol.setValue(Database.getSymbolValue("core", twiInstanceName.getValue() + "_CLOCK_FREQUENCY"))

def symbolVisible(symbol, event):
    symbol.setVisible((event["value"] == False))

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)

def updateI2CBaudHz(symbol, event):
    symbol.setValue(event["value"])
###################################################################################################
############################################# TWI #################################################
###################################################################################################
def instantiateComponent(twiComponent):
    global twiInstanceName
    global twiClockInvalidSymbol
    global twiOpMode

    twiInstanceName = twiComponent.createStringSymbol("TWI_INSTANCE_NAME", None)
    twiInstanceName.setVisible(False)
    twiInstanceName.setDefaultValue(twiComponent.getID().upper())

    Log.writeInfoMessage("Running " + twiInstanceName.getValue())


    twiOpMode = twiComponent.createComboSymbol("TWI_OPMODE", None, twiOpModeValues)
    twiOpMode.setLabel("TWI Operation Mode")
    twiOpMode.setDefaultValue("MASTER")
    twiOpMode.setReadOnly(True)

    #Peripheral Clock Frequency
    twiClockSourceFreq = twiComponent.createIntegerSymbol("TWI_CLK_SRC_FREQ", None)
    twiClockSourceFreq.setLabel("Source Clock Frequency (Hz)")
    twiClockSourceFreq.setDefaultValue(int(Database.getSymbolValue("core", twiInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    twiClockSourceFreq.setDependencies(setTwiClockSourceFreq, ["core." + twiInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    twiClockSourceFreq.setReadOnly(True)

    #Operating speed
    twiClockSpeed = twiComponent.createIntegerSymbol("I2C_CLOCK_SPEED", None)
    twiClockSpeed.setLabel("Clock Speed (Hz)")
    twiClockSpeed.setMin(100000)
    twiClockSpeed.setMax(400000)
    twiClockSpeed.setDefaultValue(400000)

    #Operating speed (HZ)
    twiClockSpeedHz = twiComponent.createIntegerSymbol("I2C_CLOCK_SPEED_HZ", None)
    twiClockSpeedHz.setLabel("Clock Speed (Hz)")
    twiClockSpeedHz.setDefaultValue(twiClockSpeed.getValue())
    twiClockSpeedHz.setVisible(False)
    twiClockSpeedHz.setDependencies(updateI2CBaudHz, ["I2C_CLOCK_SPEED"])

    #Clock invalid comment
    twiClockInvalidSymbol = twiComponent.createCommentSymbol("TWI_INVALID_CLOCK", None)
    twiClockInvalidSymbol.setLabel("Warning!!! Cannot generate required clock speed from configured clock source")
    twiClockInvalidSymbol.setVisible(False)

    cldiv, chdiv, ckdiv = getTwiClockDividerValue(twiClockSpeed.getValue())
    #CLDIV
    twiCwgrCLDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CLDIV", None)
    twiCwgrCLDIV.setVisible(False)
    twiCwgrCLDIV.setValue(cldiv)

    #CHDIV
    twiCwgrCHDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CHDIV", None)
    twiCwgrCHDIV.setVisible(False)
    twiCwgrCHDIV.setValue(chdiv)

    #CKDIV
    twiCwgrCKDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CKDIV", None)
    twiCwgrCKDIV.setVisible(False)
    twiCwgrCKDIV.setValue(ckdiv)

    #Clock Divider
    twiClkDivider = twiComponent.createStringSymbol("TWI_CLK_DIVIDER", None)
    twiClkDivider.setVisible(False)
    twiClkDivider.setDependencies(setTwiClockDividerValue, ["I2C_CLOCK_SPEED", "core." + twiInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Enable peripheral clock
    Database.setSymbolValue("core", twiInstanceName.getValue()+"_CLOCK_ENABLE", True)

    #Enable peripheral Interrupt
    Database.setSymbolValue("core", twiInstanceName.getValue() + "_INTERRUPT_ENABLE", True)
    #Set Interrupt Handler Name
    Database.setSymbolValue("core", twiInstanceName.getValue() + "_INTERRUPT_HANDLER", twiInstanceName.getValue() + "_InterruptHandler")
    #Set Interrupt Handler Lock
    Database.setSymbolValue("core", twiInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK", True)

    #Warning for change in Clock Enable Symbol
    twiClkEnComment = twiComponent.createCommentSymbol("TWI_CLK_EN_COMMENT", None)
    twiClkEnComment.setVisible(False)
    twiClkEnComment.setLabel("Warning!!! " + twiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    twiClkEnComment.setDependencies(symbolVisible, ["core." + twiInstanceName.getValue() + "_CLOCK_ENABLE"])

    #Warning for change in Interrupt Enable Symbol
    twiIntEnComment = twiComponent.createCommentSymbol("TWI_INT_EN_COMMENT", None)
    twiIntEnComment.setVisible(False)
    twiIntEnComment.setLabel("Warning!!! " + twiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    twiIntEnComment.setDependencies(symbolVisible, ["core." + twiInstanceName.getValue() + "_INTERRUPT_ENABLE"])

    #TWI API Prefix
    twiAPIPrefix = twiComponent.createStringSymbol("I2C_PLIB_API_PREFIX", None)
    twiAPIPrefix.setDefaultValue(twiInstanceName.getValue())
    twiAPIPrefix.setVisible(False)

    REG_MODULE_TWI = Register.getRegisterModule("TWI")

    configName = Variables.get("__CONFIGURATION_NAME")

    #Master Header
    twiMasterHeaderFile = twiComponent.createFileSymbol("TWI_FILE_MASTER_HEADER", None)
    twiMasterHeaderFile.setSourcePath("../peripheral/twi_6212/plib_twi_master.h")
    twiMasterHeaderFile.setOutputName("plib_twi_master.h")
    twiMasterHeaderFile.setDestPath("/peripheral/twi/")
    twiMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiMasterHeaderFile.setType("HEADER")

    #Source File
    twiMainSourceFile = twiComponent.createFileSymbol("TWI_FILE_SRC_MAIN", None)
    twiMainSourceFile.setSourcePath("../peripheral/twi_6212/templates/plib_twi.c.ftl")
    twiMainSourceFile.setOutputName("plib_" + twiInstanceName.getValue().lower() + ".c")
    twiMainSourceFile.setDestPath("/peripheral/twi/")
    twiMainSourceFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiMainSourceFile.setType("SOURCE")
    twiMainSourceFile.setMarkup(True)

    #Instance Header File
    twiInstHeaderFile = twiComponent.createFileSymbol("TWI_FILE_MAIN_HEADER", None)
    twiInstHeaderFile.setSourcePath("../peripheral/twi_6212/templates/plib_twi.h.ftl")
    twiInstHeaderFile.setOutputName("plib_" + twiInstanceName.getValue().lower() + ".h")
    twiInstHeaderFile.setDestPath("/peripheral/twi/")
    twiInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiInstHeaderFile.setType("HEADER")
    twiInstHeaderFile.setMarkup(True)

    #TWI Initialize
    twiSystemInitFile = twiComponent.createFileSymbol("TWI_FILE_SYS_INIT", None)
    twiSystemInitFile.setType("STRING")
    twiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    twiSystemInitFile.setSourcePath("../peripheral/twi_6212/templates/system/initialization.c.ftl")
    twiSystemInitFile.setMarkup(True)

    #TWI definitions header
    twiSystemDefFile = twiComponent.createFileSymbol("TWI_FILE_SYS_DEF", None)
    twiSystemDefFile.setType("STRING")
    twiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    twiSystemDefFile.setSourcePath("../peripheral/twi_6212/templates/system/definitions.h.ftl")
    twiSystemDefFile.setMarkup(True)
