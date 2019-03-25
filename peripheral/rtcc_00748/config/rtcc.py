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

global rtccSym_SOSCEN_warn

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################

def setRTCCInterruptData(status):

    Database.setSymbolValue("core", rtccInterruptVector, status, 1)
    Database.setSymbolValue("core", rtccInterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", rtccInterruptHandler, rtccInstanceName.getValue() + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", rtccInterruptHandler, rtccInstanceName.getValue() + "_Handler", 1)

def updateRTCCInterruptData(symbol, event):

    if event["id"] == "RTCC_INTERRUPT_MODE":
        setRTCCInterruptData(event["value"])

    if rtccSymInterruptMode.getValue() == True and Database.getSymbolValue("core", rtccInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateSymbolVisblity(symbol, event):

    symbol.setVisible(event["value"])

def toggleMenu(menu, event):
    menu.setVisible(not(event["value"]))

def updateAlarmMenuVisiblity(symbol, event):
    '''
    This is a special menu that appears only if the alarm interval is once a week.
    '''
    symbol.setVisible(event["value"] == 7)

def _get_bitfield_names(node, outputList):
    '''
    Gets all <value > children of 'node', appending dictionary entries to 'outputList'
    Arguments:
        node - points to atdf file, parent of <value > entries currently are interested in for this fct call
        outputList - list which will have dictionary elements comprised of following:
            desc:  caption field of <value >
            key:   caption field of <value >
            value: value field of <value >
    '''
    valueNodes = node.getChildren()

    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def checkSoscSetting(symbol, event):

    # Sees if the user has not enabled secondary oscillator when selecting it as the RTCC clock source.
    # If so, will display a warning message.
    global rtccSym_SOSCEN_warn

    sosc_enbl = Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SOSCEN")

    if((sosc_enbl == "OFF") and (event["value"] == 0)):
        rtccSym_SOSCEN_warn.setVisible(True)
    else:
        rtccSym_SOSCEN_warn.setVisible(False)

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

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))

            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):

    vector_index = "-1"

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

def instantiateComponent(rtccComponent):

    global rtccInstanceName
    global rtccInterruptVector
    global rtccInterruptHandlerLock
    global rtccInterruptHandler
    global rtccInterruptVectorUpdate
    global rtccSymInterruptMode
    global rtccSym_SOSCEN_warn

    rtcBitField_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCCLKSEL"]')
    rtcValGrp_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCCLKSEL"]')

    rtcBitField_RTCCON_RTCOE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCOE"]')
    rtcValGrp_RTCCON_RTCOE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCOE"]')

    rtcBitField_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCOUTSEL"]')
    rtcValGrp_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCOUTSEL"]')

    rtcBitField_RTCCON_RTSECSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTSECSEL"]')
    rtcValGrp_RTCCON_RTSECSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTSECSEL"]')

    rtcBitField_RTCALRM_AMASK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCALRM"]/bitfield@[name="AMASK"]')
    rtcValGrp_RTCALRM_AMASK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCALRM__AMASK"]')

    rtcBitField_RTCALRM_ARPT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCALRM"]/bitfield@[name="ARPT"]')

    rtccInstanceName = rtccComponent.createStringSymbol("RTCC_INSTANCE_NAME", None)
    rtccInstanceName.setVisible(False)
    rtccInstanceName.setDefaultValue(rtccComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtccInstanceName.getValue())

    rtccSymInterruptMode = rtccComponent.createBooleanSymbol("RTCC_INTERRUPT_MODE", None)
    rtccSymInterruptMode.setLabel("Enable Interrupt ?")

    # Get register names, mask values, bit shifts based on vector number
    rtccInterruptVector = rtccInstanceName.getValue() + "_INTERRUPT_ENABLE"
    rtccInterruptHandler = rtccInstanceName.getValue() + "_INTERRUPT_HANDLER"
    rtccInterruptHandlerLock = rtccInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    rtccInterruptVectorUpdate = rtccInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    rtcIrq_index = int(getIRQIndex(rtccInstanceName.getValue()))

    if rtcIrq_index == -1:
        rtcIrq_index = int(getVectorIndex(rtccInstanceName.getValue()))

    enblRegName, enblBitPosn = _get_enblReg_parms(rtcIrq_index)
    statRegName, statBitPosn = _get_statReg_parms(rtcIrq_index)

    # Below create family-specific register names / masking needed by ftl file
    rtcEnblRegWrt = rtccComponent.createStringSymbol("RTCC_IEC_REG", None)
    rtcEnblRegWrt.setDefaultValue(enblRegName)
    rtcEnblRegWrt.setVisible(False)

    rtcEnblRegVal = rtccComponent.createStringSymbol("RTCC_ENBLREG_ENABLE_VALUE", None)
    rtcEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
    rtcEnblRegVal.setVisible(False)

    rtcStatRegRd = rtccComponent.createStringSymbol("RTCC_IFS_REG", None)
    rtcStatRegRd.setDefaultValue(statRegName)
    rtcStatRegRd.setVisible(False)

    rtcStatRegShiftVal = rtccComponent.createStringSymbol("RTCC_STATREG_SHIFT_VALUE", None)
    rtcStatRegShiftVal.setDefaultValue(str(hex(1 << int(statBitPosn))))
    rtcStatRegShiftVal.setVisible(False)

    rtcVectorNum = rtccComponent.createIntegerSymbol("RTCC_VECTOR_NUMBER", None)
    rtcVectorNum.setDefaultValue(rtcIrq_index)
    rtcVectorNum.setVisible(False)

    if rtcValGrp_RTCCON_RTCCLKSEL != None:
        # clock source
        clkSel_names = []
        _get_bitfield_names(rtcValGrp_RTCCON_RTCCLKSEL, clkSel_names)
        rtccSym_RTCCON_RTCCLKSEL = rtccComponent.createKeyValueSetSymbol("RTCC_CLOCK_SOURCE", None )
        rtccSym_RTCCON_RTCCLKSEL.setLabel(rtcBitField_RTCCON_RTCCLKSEL.getAttribute("caption"))
        rtccSym_RTCCON_RTCCLKSEL.setOutputMode( "Value" )
        rtccSym_RTCCON_RTCCLKSEL.setDisplayMode( "Description" )
        for ii in clkSel_names:
            rtccSym_RTCCON_RTCCLKSEL.addKey( ii['desc'], ii['value'], ii['key'] )
        rtccSym_RTCCON_RTCCLKSEL.setDefaultValue(1)
        rtccSym_RTCCON_RTCCLKSEL.setDependencies(checkSoscSetting,["RTCC_CLOCK_SOURCE"])

        # Create warning menu for when user selects external source but SOSCEN not set in clock module
        rtccSym_SOSCEN_warn = rtccComponent.createMenuSymbol("SOSCEN_WARN", rtccSym_RTCCON_RTCCLKSEL)
        rtccSym_SOSCEN_warn.setLabel("*** Warning: set secondary oscillator enable to ON in clock configurator settings ***")
        rtccSym_SOSCEN_warn.setVisible(False)

    # RTCC output enable
    rtccSym_RTCCON_RTCOE = rtccComponent.createBooleanSymbol("RTCC_OUTPUT_ENABLE", None)
    rtccSym_RTCCON_RTCOE.setLabel(rtcBitField_RTCCON_RTCOE.getAttribute("caption"))

    # output select
    rtcOutSel_names = []
    rtccOutputLabel = ""
    rtccOutputBitName = ""

    if rtcValGrp_RTCCON_RTCOUTSEL != None:
        _get_bitfield_names(rtcValGrp_RTCCON_RTCOUTSEL, rtcOutSel_names)
        rtccOutputLabel = rtcBitField_RTCCON_RTCOUTSEL.getAttribute("caption")
        rtccOutputBitName = "RTCOUTSEL"
    else:
        _get_bitfield_names(rtcValGrp_RTCCON_RTSECSEL, rtcOutSel_names)
        rtccOutputLabel = rtcValGrp_RTCCON_RTSECSEL.getAttribute("caption")
        rtccOutputBitName = "RTSECSEL"

    rtccSym_RTCCON_RTCOUTSEL = rtccComponent.createKeyValueSetSymbol("RTCC_OUTPUT_SELECT", rtccSym_RTCCON_RTCOE)
    rtccSym_RTCCON_RTCOUTSEL.setLabel(rtccOutputLabel)
    rtccSym_RTCCON_RTCOUTSEL.setOutputMode( "Value" )
    rtccSym_RTCCON_RTCOUTSEL.setDisplayMode( "Description" )
    for ii in rtcOutSel_names:
        rtccSym_RTCCON_RTCOUTSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    rtccSym_RTCCON_RTCOUTSEL.setDefaultValue(0)
    rtccSym_RTCCON_RTCOUTSEL.setVisible(False)
    rtccSym_RTCCON_RTCOUTSEL.setDependencies(updateSymbolVisblity, ["RTCC_OUTPUT_ENABLE"])

    rtccSym_OutputSelectBit = rtccComponent.createStringSymbol("RTCC_OUTPUT_SELECT_BITNAME", rtccSym_RTCCON_RTCOE)
    rtccSym_OutputSelectBit.setDefaultValue(rtccOutputBitName)
    rtccSym_OutputSelectBit.setVisible(False)

    rtccSym_RTCCON_TIMEDATE = rtccComponent.createMenuSymbol("RTC_TIMEANDDATE", None)
    rtccSym_RTCCON_TIMEDATE.setLabel("Time & Date")

    # Time. Note: this item is treated differently.  Single entry value spans the concatenation of bitfields.
    rtccSym_RTCTIME_TIME = rtccComponent.createStringSymbol("RTCTIME_TIME",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCTIME_TIME.setLabel("Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_RTCTIME_TIME.setDefaultValue("235950")

    # Date.  User's entry here spans most significant 24 bits of register RTCDATE
    rtccSym_RTCDATE_DATE = rtccComponent.createStringSymbol("RTCTIME_DATE",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_DATE.setLabel("Date (YYMMDD, where YY:00-99, MM:01-12, DD:01-31)")
    rtccSym_RTCDATE_DATE.setDefaultValue("181231")

    # Day of week.
    rtccSym_RTCDATE_WEEKDAY = rtccComponent.createIntegerSymbol("RTCTIME_WEEKDAY",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_WEEKDAY.setLabel("Weekday (0-6)")
    rtccSym_RTCDATE_WEEKDAY.setDefaultValue(0)

    rtccSym_RTCCON_ALARMMENU = rtccComponent.createMenuSymbol("RTC_ALARM", None)
    rtccSym_RTCCON_ALARMMENU.setLabel("Alarm")

    # Alarm time.  Note: the user entry spans the upper 24 bits of the register ALRMTIME
    rtccSym_ALRMTIME_TIME = rtccComponent.createStringSymbol("RTCALRM_TIME",rtccSym_RTCCON_ALARMMENU)
    rtccSym_ALRMTIME_TIME.setLabel("Alarm Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_ALRMTIME_TIME.setDefaultValue("235955")

    # Alarm date.  User settings span a contiguous set of bitfields.
    rtccSym_RTCCON_ALRMDATE = rtccComponent.createStringSymbol("RTCALRM_DATE",rtccSym_RTCCON_ALARMMENU)
    rtccSym_RTCCON_ALRMDATE.setLabel("Alarm Date (MMDD, where MM:01-12, DD:01-31)")
    rtccSym_RTCCON_ALRMDATE.setDefaultValue("1231")

    # Alarm mask
    alrmMask_names = []
    _get_bitfield_names(rtcValGrp_RTCALRM_AMASK, alrmMask_names)
    rtccSym_RTCALRM_AMASK = rtccComponent.createKeyValueSetSymbol( "RTCC_ALARM_MASK", rtccSym_RTCCON_ALARMMENU )
    rtccSym_RTCALRM_AMASK.setLabel(rtcBitField_RTCALRM_AMASK.getAttribute("caption"))
    rtccSym_RTCALRM_AMASK.setOutputMode( "Value" )
    rtccSym_RTCALRM_AMASK.setDisplayMode( "Description" )
    for ii in alrmMask_names:
        rtccSym_RTCALRM_AMASK.addKey( ii['desc'], ii['value'], ii['key'] )
    rtccSym_RTCALRM_AMASK.setDefaultValue(1)

    # Alarm day of week.  Only allowed to be user-set if alarm mask is set to once a week.
    rtccSym_ALRMTIME_WDAY = rtccComponent.createIntegerSymbol("RTCALRM_DAY", rtccSym_RTCALRM_AMASK)
    rtccSym_ALRMTIME_WDAY.setLabel("Alarm Weekday (0-6)")
    rtccSym_ALRMTIME_WDAY.setDefaultValue(0)
    rtccSym_ALRMTIME_WDAY.setMin(0)
    rtccSym_ALRMTIME_WDAY.setMax(6)
    rtccSym_ALRMTIME_WDAY.setVisible(False)
    rtccSym_ALRMTIME_WDAY.setDependencies(updateAlarmMenuVisiblity, ["RTCC_ALARM_MASK"])

    # Alarm repeat forever
    rtccSym_RTCALRM_ARPT = rtccComponent.createBooleanSymbol("RTCC_ALARM_REPEAT_FOREVER", rtccSym_RTCCON_ALARMMENU)
    rtccSym_RTCALRM_ARPT.setVisible(True)
    rtccSym_RTCALRM_ARPT.setLabel("Alarm Repeats Forever")
    rtccSym_RTCALRM_ARPT.setDefaultValue(False)

    # Alarm repeat count
    rtccSym_RTCALRM_ARPTCNT = rtccComponent.createIntegerSymbol("RTCALRM_ARPT", rtccSym_RTCALRM_ARPT)
    rtccSym_RTCALRM_ARPTCNT.setVisible(True)
    rtccSym_RTCALRM_ARPTCNT.setLabel(rtcBitField_RTCALRM_ARPT.getAttribute("caption"))
    rtccSym_RTCALRM_ARPTCNT.setMin(0)
    rtccSym_RTCALRM_ARPTCNT.setMax(255)
    rtccSym_RTCALRM_ARPTCNT.setDefaultValue(0)
    rtccSym_RTCALRM_ARPTCNT.setDependencies(toggleMenu, ["RTCC_ALARM_REPEAT_FOREVER"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    rtccSymIntEnComment = rtccComponent.createCommentSymbol("RTCC_INTRRUPT_ENABLE_COMMENT", None)
    rtccSymIntEnComment.setLabel("Warning!!! " + rtccInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    rtccSymIntEnComment.setVisible(False)
    rtccSymIntEnComment.setDependencies(updateRTCCInterruptData, ["RTCC_INTERRUPT_MODE", "core." + rtccInterruptVectorUpdate])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Header File
    rtccSymHeaderFile = rtccComponent.createFileSymbol("RTC_INSTANCE_HEADER", None)
    rtccSymHeaderFile.setSourcePath("../peripheral/rtcc_00748/templates/plib_rtcc.h.ftl")
    rtccSymHeaderFile.setOutputName("plib_" + rtccInstanceName.getValue().lower() + ".h")
    rtccSymHeaderFile.setDestPath("/peripheral/rtcc/")
    rtccSymHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtccSymHeaderFile.setType("HEADER")
    rtccSymHeaderFile.setMarkup(True)

    # Instance Source File
    rtccSymSourceFile = rtccComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtccSymSourceFile.setSourcePath("../peripheral/rtcc_00748/templates/plib_rtcc.c.ftl")
    rtccSymSourceFile.setOutputName("plib_" + rtccInstanceName.getValue().lower() + ".c")
    rtccSymSourceFile.setDestPath("/peripheral/rtcc/")
    rtccSymSourceFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtccSymSourceFile.setType("SOURCE")
    rtccSymSourceFile.setMarkup(True)

    #System Initialization
    rtccSymSystemInitFile = rtccComponent.createFileSymbol("RTC_SYS_INIT", None)
    rtccSymSystemInitFile.setType("STRING")
    rtccSymSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtccSymSystemInitFile.setSourcePath("../peripheral/rtcc_00748/templates/system/initialization.c.ftl")
    rtccSymSystemInitFile.setMarkup(True)

    # System Definition
    rtccSymSystemDefFile = rtccComponent.createFileSymbol("RTC_SYS_DEF", None)
    rtccSymSystemDefFile.setType("STRING")
    rtccSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtccSymSystemDefFile.setSourcePath("../peripheral/rtcc_00748/templates/system/definitions.h.ftl")
    rtccSymSystemDefFile.setMarkup(True)
