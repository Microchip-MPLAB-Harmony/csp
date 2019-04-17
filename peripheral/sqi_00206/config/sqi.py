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

global sqiInstanceName

def calculateSqiClkFreq(sqiClkDiv, refclk2_freq):
    sqiClkFreq = refclk2_freq

    if (sqiClkDiv != "0x0"):
        sqiClkDiv = int(sqiClkDiv, 16) * 2
        sqiClkFreq = refclk2_freq / sqiClkDiv

    return sqiClkFreq

def setClkDivComment(symbol, event):
    component = symbol.getComponent()

    refclk2_freq = Database.getSymbolValue("core", sqiInstanceName.getValue() + "_CLOCK_FREQUENCY")

    sqiClkDiv = component.getSymbolByID("SQI_CLKDIV").getSelectedValue()

    sqiClkFreq = calculateSqiClkFreq(sqiClkDiv, refclk2_freq)

    symbol.setLabel("*** SQI Clock Frequency Is Set To " + str(sqiClkFreq) +  " for REFCLK2 Frequency At " + str(refclk2_freq))

def setClockPhase(symbol, event):
    symbol.setValue(event["value"], 1)

def setFlashStatusCheck(symbol, event):
    symbol.setVisible(event["value"])

def setSQIInterruptData(status):

    Database.setSymbolValue("core", sqiInterruptVector, status, 1)
    Database.setSymbolValue("core", sqiInterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", sqiInterruptHandler, sqiInstanceName.getValue() + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", sqiInterruptHandler, sqiInstanceName.getValue() + "_Handler", 1)

def updateSQIInterruptData(symbol, event):

    if event["id"] == "INTERRUPT_ENABLE":
        setSQIInterruptData(event["value"])

    if sqiInterruptEnable.getValue() == True and Database.getSymbolValue("core", sqiInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def getIRQnumber(string):

    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

    for param in interruptsChildren:
        modInst = param.getAttribute("name")
        if string == modInst:
            irq_index = param.getAttribute("index")

    return irq_index

def updateSQIClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def instantiateComponent(sqiComponent):
    global sqiInstanceName
    global sqiInterruptVector
    global sqiInterruptHandlerLock
    global sqiInterruptHandler
    global sqiInterruptVectorUpdate
    global sqiInterruptEnable

    sqiInstanceName = sqiComponent.createStringSymbol("SQI_INSTANCE_NAME", None)
    sqiInstanceName.setVisible(False)
    sqiInstanceName.setDefaultValue(sqiComponent.getID().upper())

    print("Running " + sqiInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", sqiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    sqiMenu = sqiComponent.createMenuSymbol("SQI", None)
    sqiMenu.setLabel("Hardware Settings ")

    sqiCSEN = sqiComponent.createKeyValueSetSymbol("SQI_CSEN", sqiMenu)
    sqiCSEN.setLabel("Chip Select Output Enable Bits")
    sqiCSEN.addKey("SQI_CS_NONE", "0x0", "None")
    sqiCSEN.addKey("SQI_CS_0", "0x1", "Chip Select 0 is used")
    sqiCSEN.addKey("SQI_CS_1", "0x2", "Chip Select 1 is used")
    sqiCSEN.addKey("SQI_CS_0_1", "0x3", "Chip Select 0 and Chip Select 1 are used")
    sqiCSEN.setOutputMode("Value")
    sqiCSEN.setDisplayMode("Description")
    sqiCSEN.setDefaultValue(3)

    sqiCPOL = sqiComponent.createKeyValueSetSymbol("SQI_CPOL", sqiMenu)
    sqiCPOL.setLabel("Clock Polarity")
    sqiCPOL.addKey("LOW", "0", "Clock is Low when inactive (CPOL=0)")
    sqiCPOL.addKey("HIGH", "1", "Clock is High when inactive (CPOL=1)")
    sqiCPOL.setOutputMode("Key")
    sqiCPOL.setDisplayMode("Description")
    sqiCPOL.setDefaultValue(0)

    sqiCPHA = sqiComponent.createKeyValueSetSymbol("SQI_CPHA", sqiMenu)
    sqiCPHA.setLabel("Clock Phase")
    sqiCPHA.addKey("LEADING", "0", "Data is Valid on Clock Leading Edge (CPHA=0)")
    sqiCPHA.addKey("TRAILING", "1", "Data is Valid on Clock Trailing Edge (CPHA=1)")
    sqiCPHA.setOutputMode("Key")
    sqiCPHA.setDisplayMode("Description")
    sqiCPHA.setDefaultValue(0)
    sqiCPHA.setReadOnly(True)
    sqiCPHA.setDependencies(setClockPhase, ["SQI_CPOL"])

    sqiLSBF = sqiComponent.createKeyValueSetSymbol("SQI_LSBF", sqiMenu)
    sqiLSBF.setLabel("Data Format")
    sqiLSBF.addKey("MSB", "0", "MSB is sent or received first")
    sqiLSBF.addKey("LSB", "1", "LSB is sent or received first")
    sqiLSBF.setOutputMode("Key")
    sqiLSBF.setDisplayMode("Description")
    sqiLSBF.setDefaultValue(0)

    sqiClkDiv = sqiComponent.createKeyValueSetSymbol("SQI_CLKDIV", sqiMenu)
    sqiClkDiv.setLabel("SQI Clock Divider")
    sqiClkDiv.addKey("SQI_CLK_DIV_2048", "0x400", "Base clock is divided by 2048")
    sqiClkDiv.addKey("SQI_CLK_DIV_1024", "0x200", "Base clock is divided by 1024")
    sqiClkDiv.addKey("SQI_CLK_DIV_512", "0x100", "Base clock is divided by 512")
    sqiClkDiv.addKey("SQI_CLK_DIV_256", "0x80", "Base clock is divided by 256")
    sqiClkDiv.addKey("SQI_CLK_DIV_128", "0x40", "Base clock is divided by 128")
    sqiClkDiv.addKey("SQI_CLK_DIV_64", "0x20", "Base clock is divided by 64")
    sqiClkDiv.addKey("SQI_CLK_DIV_32", "0x10", "Base clock is divided by 32")
    sqiClkDiv.addKey("SQI_CLK_DIV_16", "0x8", "Base clock is divided by 16")
    sqiClkDiv.addKey("SQI_CLK_DIV_8", "0x4", "Base clock is divided by 8")
    sqiClkDiv.addKey("SQI_CLK_DIV_4", "0x2", "Base clock is divided by 4")
    sqiClkDiv.addKey("SQI_CLK_DIV_2", "0x1", "Base clock is divided by 2")
    sqiClkDiv.addKey("SQI_CLK_DIV_0", "0x0", "Equals Base clock")
    sqiClkDiv.setOutputMode("Value")
    sqiClkDiv.setDisplayMode("Description")
    sqiClkDiv.setDefaultValue(11)

    refclk2_freq = Database.getSymbolValue("core", sqiInstanceName.getValue() + "_CLOCK_FREQUENCY")

    sqiClkFreq = calculateSqiClkFreq(sqiClkDiv.getSelectedValue(), refclk2_freq)

    sqiClkDivComment = sqiComponent.createCommentSymbol("SQI_CLK_DIV_COMMENT", sqiMenu)
    sqiClkDivComment.setLabel("*** SQI Clock Frequency Is Set To " + str(sqiClkFreq) +  " for REFCLK2 Frequency At " + str(refclk2_freq))
    sqiClkDivComment.setVisible(True)
    sqiClkDivComment.setDependencies(setClkDivComment, ["core." + sqiInstanceName.getValue() + "_CLOCK_FREQUENCY", "SQI_CLKDIV"])

    ################# Interrupt Settings ###########################

    # Get register names, mask values, bit shifts based on vector number
    sqiInterruptVector = sqiInstanceName.getValue() + "_INTERRUPT_ENABLE"
    sqiInterruptHandler = sqiInstanceName.getValue() + "_INTERRUPT_HANDLER"
    sqiInterruptHandlerLock = sqiInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    sqiInterruptVectorUpdate = sqiInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"
    sqiIrq_index = int(getIRQnumber(sqiInstanceName.getValue()))

    sqiInterruptEnable = sqiComponent.createBooleanSymbol("INTERRUPT_ENABLE", sqiMenu)
    sqiInterruptEnable.setLabel("SQI Interrupt Enabled")
    sqiInterruptEnable.setDefaultValue(True)
    sqiInterruptEnable.setReadOnly(True)

    sqiInterruptComment = sqiComponent.createCommentSymbol("SQI_INTRRUPT_ENABLE_COMMENT", sqiMenu)
    sqiInterruptComment.setLabel("Warning!!! " + sqiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    sqiInterruptComment.setVisible(False)
    sqiInterruptComment.setDependencies(updateSQIInterruptData, ["INTERRUPT_ENABLE", "core." + sqiInterruptVectorUpdate])

    # Clock Warning status
    sqiSym_ClkEnComment = sqiComponent.createCommentSymbol("SQI_CLOCK_ENABLE_COMMENT", None)
    sqiSym_ClkEnComment.setLabel("Warning!!! " + sqiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    sqiSym_ClkEnComment.setVisible(False)
    sqiSym_ClkEnComment.setDependencies(updateSQIClockWarningStatus, ["core." + sqiInstanceName.getValue() + "_CLOCK_ENABLE"])

    setSQIInterruptData(True)

    enblRegName, enblBitPosn = _get_enblReg_parms(sqiIrq_index)
    statRegName, statBitPosn = _get_statReg_parms(sqiIrq_index)

    # Below create family-specific register names / masking needed by ftl file
    sqiEnblRegWrt = sqiComponent.createStringSymbol("SQI_IEC_REG", sqiMenu)
    sqiEnblRegWrt.setDefaultValue(enblRegName)
    sqiEnblRegWrt.setVisible(False)

    sqiEnblRegVal = sqiComponent.createStringSymbol("SQI_IEC_REG_VALUE", sqiMenu)
    sqiEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
    sqiEnblRegVal.setVisible(False)

    sqiStatRegRd = sqiComponent.createStringSymbol("SQI_IFS_REG", sqiMenu)
    sqiStatRegRd.setDefaultValue(statRegName)
    sqiStatRegRd.setVisible(False)

    sqiStatRegShiftVal = sqiComponent.createStringSymbol("SQI_IFS_REG_VALUE", sqiMenu)
    sqiStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
    sqiStatRegShiftVal.setVisible(False)

    sqiVectorNum = sqiComponent.createIntegerSymbol("SQI_VECTOR_NUMBER", sqiMenu)
    sqiVectorNum.setDefaultValue(sqiIrq_index)
    sqiVectorNum.setVisible(False)

    sqiFlashStatusCheck = sqiComponent.createBooleanSymbol("SQI_FLASH_STATUS_CHECK", sqiMenu)
    sqiFlashStatusCheck.setLabel("Enable Flash Status Check?")
    sqiFlashStatusCheck.setDefaultValue(True)

    sqiStatBytes = sqiComponent.createKeyValueSetSymbol("SQI_STATBYTES", sqiFlashStatusCheck)
    sqiStatBytes.setLabel("Number of Status Command/Read Bytes")
    sqiStatBytes.addKey("SQI_STATUS_BYTES_1", "0x1", "1 byte long")
    sqiStatBytes.addKey("SQI_STATUS_BYTES_2", "0x2", "2 bytes long")
    sqiStatBytes.setOutputMode("Value")
    sqiStatBytes.setDisplayMode("Description")
    sqiStatBytes.setDefaultValue(1)
    sqiStatBytes.setVisible(sqiFlashStatusCheck.getValue())
    sqiStatBytes.setDependencies(setFlashStatusCheck, ["SQI_FLASH_STATUS_CHECK"])

    sqiStatType = sqiComponent.createComboSymbol("SQI_STATTYPE", sqiFlashStatusCheck, ["SINGLE", "DUAL", "QUAD"])
    sqiStatType.setLabel("Status Command/Read Lane Mode")
    sqiStatType.setDefaultValue("QUAD")
    sqiStatType.setVisible(sqiFlashStatusCheck.getValue())
    sqiStatType.setDependencies(setFlashStatusCheck, ["SQI_FLASH_STATUS_CHECK"])

    sqiStatPos = sqiComponent.createKeyValueSetSymbol("SQI_STATPOS", sqiFlashStatusCheck)
    sqiStatPos.setLabel("Status Register Busy Bit Position")
    sqiStatPos.addKey("SQI_STATUS_BIT_0", "0x0", "Position 0")
    sqiStatPos.addKey("SQI_STATUS_BIT_7", "0x1", "Position 7")
    sqiStatPos.setOutputMode("Value")
    sqiStatPos.setDisplayMode("Description")
    sqiStatPos.setDefaultValue(1)
    sqiStatPos.setVisible(sqiFlashStatusCheck.getValue())
    sqiStatPos.setDependencies(setFlashStatusCheck, ["SQI_FLASH_STATUS_CHECK"])

    sqiStatCmd = sqiComponent.createHexSymbol("SQI_STATCMD", sqiFlashStatusCheck)
    sqiStatCmd.setLabel("Status Command")
    sqiStatCmd.setDefaultValue(0x05)
    sqiStatCmd.setVisible(sqiFlashStatusCheck.getValue())
    sqiStatCmd.setDependencies(setFlashStatusCheck, ["SQI_FLASH_STATUS_CHECK"])

    processor = Variables.get( "__PROCESSOR" )

    if (("PIC32MZ" in processor) and ("DA" in processor)):
        sqiSdhcDisableComment = sqiComponent.createCommentSymbol("SQI_SDHC_DISABLE", sqiMenu)
        sqiSdhcDisableComment.setLabel("!!! SDHC peripheral will be disabled as SQI and SDHC share Port Pins !!!")

    configName = Variables.get("__CONFIGURATION_NAME")

    sqiCommonHeaderFile = sqiComponent.createFileSymbol("SQI_COMMON_HEADER", None)
    sqiCommonHeaderFile.setSourcePath("../peripheral/sqi_00206/templates/plib_sqi_common.h")
    sqiCommonHeaderFile.setOutputName("plib_sqi_common.h")
    sqiCommonHeaderFile.setDestPath("/peripheral/sqi/")
    sqiCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/sqi/")
    sqiCommonHeaderFile.setType("HEADER")

    sqiHeaderFile = sqiComponent.createFileSymbol("SQI_HEADER", None)
    sqiHeaderFile.setSourcePath("../peripheral/sqi_00206/templates/plib_sqi.h.ftl")
    sqiHeaderFile.setOutputName("plib_" + sqiInstanceName.getValue().lower() + ".h")
    sqiHeaderFile.setDestPath("/peripheral/sqi/")
    sqiHeaderFile.setProjectPath("config/" + configName + "/peripheral/sqi/")
    sqiHeaderFile.setType("HEADER")
    sqiHeaderFile.setMarkup(True)
    sqiHeaderFile.setOverwrite(True)

    sqiSourceFile = sqiComponent.createFileSymbol("SQI_SOURCE", None)
    sqiSourceFile.setSourcePath("../peripheral/sqi_00206/templates/plib_sqi.c.ftl")
    sqiSourceFile.setOutputName("plib_" + sqiInstanceName.getValue().lower() + ".c")
    sqiSourceFile.setDestPath("/peripheral/sqi/")
    sqiSourceFile.setProjectPath("config/" + configName + "/peripheral/sqi/")
    sqiSourceFile.setType("SOURCE")
    sqiSourceFile.setMarkup(True)
    sqiSourceFile.setOverwrite(True)

    #SQI Initialize
    sqiSystemInitFile = sqiComponent.createFileSymbol("SQI_INIT", None)
    sqiSystemInitFile.setType("STRING")
    sqiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sqiSystemInitFile.setSourcePath("../peripheral/sqi_00206/templates/system/initialization.c.ftl")
    sqiSystemInitFile.setMarkup(True)

    #SQI definitions header
    sqiSystemDefFile = sqiComponent.createFileSymbol("SQI_DEF", None)
    sqiSystemDefFile.setType("STRING")
    sqiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sqiSystemDefFile.setSourcePath("../peripheral/sqi_00206/templates/system/definitions.h.ftl")
    sqiSystemDefFile.setMarkup(True)
