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
            if bitfield.getAttribute("name") == "":
                dict["key"] = bitfield.getAttribute("caption")
            else:
                dict["key"] = bitfield.getAttribute("name")

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
    global rtccSym_RTCCON_RTCCLKSEL
    sosc_enbl = Database.getSymbolValue("core", "CONFIG_SOSCEN")

    if(sosc_enbl == "OFF") and (rtccSym_RTCCON_RTCCLKSEL.getValue() == 3):
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

def updateRTCCClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

def calcRtccFinalFreq():
    global rtccSym_RTCCON2_PS
    rtccInputFreq = int(Database.getSymbolValue("core", "RTCC_CLOCK_FREQUENCY"))
    rtccDivider = int(Database.getSymbolValue("rtcc", "RTCC_CLOCK_DIVIDER"))
    #rtccPrescaler = Database.getSymbolValue("rtcc", "RTCC_CLOCK_PRESCALER")
    rtccPrescaler = int(rtccSym_RTCCON2_PS.getSelectedKey())
    rtccFractionalDivider = Database.getSymbolValue("rtcc", "RTCC_FRACTIONAL_CLOCK_DIVIDER")

    rtccFinalFreq = rtccInputFreq/(rtccPrescaler * (rtccDivider+1) + (rtccFractionalDivider/32.0) )
    return rtccFinalFreq

def calcRtccFinalFreq_callback(symbol, event):
    symbol.setValue(calcRtccFinalFreq())

def updateRTCCON2(symbol, event):
    global rtccSym_RTCCON_RTCCLKSEL
    rtccClockSource = int(rtccSym_RTCCON_RTCCLKSEL.getSelectedValue())
    rtccDivider = int(Database.getSymbolValue("rtcc", "RTCC_CLOCK_DIVIDER"))
    rtccPrescaler = int(rtccSym_RTCCON2_PS.getSelectedValue())
    rtccFractionalDivider = Database.getSymbolValue("rtcc", "RTCC_FRACTIONAL_CLOCK_DIVIDER")
    RTCCON2_Value = rtccClockSource | (rtccPrescaler << 4) | (rtccFractionalDivider << 11) | (rtccDivider << 16)
    symbol.setValue(RTCCON2_Value)

def instantiateComponent(rtccComponent):

    global rtccInstanceName
    global rtccInterruptVector
    global rtccInterruptHandlerLock
    global rtccInterruptHandler
    global rtccInterruptVectorUpdate
    global rtccSymInterruptMode
    global rtccSym_SOSCEN_warn

    rtcBitField_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON2"]/bitfield@[name="CLKSEL"]')
    rtcValGrp_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON2__CLKSEL"]')

    rtcBitField_RTCCON2_PS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON2"]/bitfield@[name="PS"]')
    rtcValGrp_RTCCON2_PS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON2__PS"]')

    rtcBitField_RTCCON_RTCOE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON1"]/bitfield@[name="RTCOE"]')

    rtcBitField_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON1"]/bitfield@[name="OUTSEL"]')
    rtcValGrp_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON1__OUTSEL"]')

    rtcValGrp_RTCALRM_AMASK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON1__AMASK"]')

    rtcBitField_RTCALRM_ARPT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON1"]/bitfield@[name="ALMRPT"]')

    rtccInstanceName = rtccComponent.createStringSymbol("RTCC_INSTANCE_NAME", None)
    rtccInstanceName.setVisible(False)
    rtccInstanceName.setDefaultValue(rtccComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtccInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", rtccInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    rtccSymInterruptMode = rtccComponent.createBooleanSymbol("RTCC_INTERRUPT_MODE", None)
    rtccSymInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:IEC1")
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

    rtccClockMenu = rtccComponent.createMenuSymbol("RTCC_CLOCK_MENU", None)
    rtccClockMenu.setLabel("RTCC Clock Configuration")

    global rtccSym_RTCCON_RTCCLKSEL
    if rtcValGrp_RTCCON_RTCCLKSEL != None:
        # clock source
        clkSel_names = []
        _get_bitfield_names(rtcValGrp_RTCCON_RTCCLKSEL, clkSel_names)
        rtccSym_RTCCON_RTCCLKSEL = rtccComponent.createKeyValueSetSymbol("RTCC_CLOCK_SOURCE", rtccClockMenu )
        rtccSym_RTCCON_RTCCLKSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
        rtccSym_RTCCON_RTCCLKSEL.setLabel("RTCC Clock Source Select")
        rtccSym_RTCCON_RTCCLKSEL.setOutputMode( "Value" )
        rtccSym_RTCCON_RTCCLKSEL.setDisplayMode( "Description" )
        for ii in clkSel_names:
            rtccSym_RTCCON_RTCCLKSEL.addKey( ii['key'], ii['value'], ii['desc'] )
        rtccSym_RTCCON_RTCCLKSEL.setDefaultValue(2) #LPRC
        
        # Create warning menu for when user selects external source but SOSCEN not set in clock module
        rtccSym_SOSCEN_warn = rtccComponent.createMenuSymbol("SOSCEN_WARN", rtccSym_RTCCON_RTCCLKSEL)
        rtccSym_SOSCEN_warn.setLabel("*** Warning: set secondary oscillator enable to ON in clock configurator settings ***")
        rtccSym_SOSCEN_warn.setVisible(False)
        rtccSym_SOSCEN_warn.setDependencies(checkSoscSetting,["RTCC_CLOCK_SOURCE", "core.CONFIG_SOSCEN"])

    # PWRLCLK pin frequency
    rtccSym_PWRLCLK_IN_FREQ = rtccComponent.createIntegerSymbol("RTCC_PWRLCLK_PIN_FREQ", rtccClockMenu)
    rtccSym_PWRLCLK_IN_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
    rtccSym_PWRLCLK_IN_FREQ.setLabel("PWRLCLK Input Pin Frequency (Hz)")
    rtccSym_PWRLCLK_IN_FREQ.setDefaultValue(0)

    global rtccSym_RTCCON2_PS
    clkPrescaler_names = []
    _get_bitfield_names(rtcValGrp_RTCCON2_PS, clkPrescaler_names)
    rtccSym_RTCCON2_PS = rtccComponent.createKeyValueSetSymbol("RTCC_CLOCK_PRESCALER", rtccClockMenu )
    rtccSym_RTCCON2_PS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
    rtccSym_RTCCON2_PS.setLabel(rtcBitField_RTCCON2_PS.getAttribute("caption"))
    rtccSym_RTCCON2_PS.setOutputMode("Value")
    rtccSym_RTCCON2_PS.setDisplayMode("Description")
    for ii in clkPrescaler_names:
        rtccSym_RTCCON2_PS.addKey( ii['key'], ii['value'], ii['desc'] )
    rtccSym_RTCCON2_PS.setDefaultValue(3) #1:1

    rtccClkDivder = rtccComponent.createHexSymbol("RTCC_CLOCK_DIVIDER", rtccClockMenu)
    rtccClkDivder.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
    rtccClkDivder.setLabel("RTCC Clock Divider")
    rtccClkDivder.setDefaultValue(0x3FFF)
    rtccClkDivder.setMin(0)
    rtccClkDivder.setMax(0xFFFF)

    rtccSym_RTCCON2_FDIV = rtccComponent.createIntegerSymbol("RTCC_FRACTIONAL_CLOCK_DIVIDER", rtccClockMenu)
    rtccSym_RTCCON2_FDIV.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
    rtccSym_RTCCON2_FDIV.setLabel("RTCC Fractional Clock Divider")
    rtccSym_RTCCON2_FDIV.setDescription("This is to calibrate RTCC Clock")
    rtccSym_RTCCON2_FDIV.setDefaultValue(0)

    rtccSym_finalClock = rtccComponent.createFloatSymbol("RTCC_FINAL_CLOCK_FREQ", rtccClockMenu)
    rtccSym_finalClock.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON2")
    rtccSym_finalClock.setLabel("RTCC Timer Clock Frequency (Hz)")
    rtccSym_finalClock.setDescription("This frequency should be 2 Hz for correct RTCC operation")
    rtccSym_finalClock.setReadOnly(True)
    rtccSym_finalClock.setDefaultValue(calcRtccFinalFreq())
    rtccSym_finalClock.setDependencies(calcRtccFinalFreq_callback, ["core.RTCC_CLOCK_FREQUENCY", "RTCC_CLOCK_DIVIDER", "RTCC_CLOCK_PRESCALER", "RTCC_FRACTIONAL_CLOCK_DIVIDER"])

    rtccSym_finalClockWarning = rtccComponent.createCommentSymbol("RTCC_FINAL_CLOCK_COMMENT", rtccClockMenu)
    rtccSym_finalClockWarning.setLabel("RTCC Timer Clock Frequency should be 2 Hz for correct RTCC operation")
    rtccSym_finalClockWarning.setVisible(True)

    rtccSym_RTCCON2_REG = rtccComponent.createHexSymbol("RTCCON2_REG_VALUE", None)
    rtccSym_RTCCON2_REG.setDefaultValue(0x3FFF0001)
    rtccSym_RTCCON2_REG.setVisible(False)
    rtccSym_RTCCON2_REG.setDependencies(updateRTCCON2, ["RTCC_CLOCK_SOURCE", "RTCC_CLOCK_DIVIDER", "RTCC_CLOCK_PRESCALER", "RTCC_FRACTIONAL_CLOCK_DIVIDER"])

    # RTCC output enable
    rtccSym_RTCCON_RTCOE = rtccComponent.createBooleanSymbol("RTCC_OUTPUT_ENABLE", None)
    rtccSym_RTCCON_RTCOE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCCON_RTCOE.setLabel(rtcBitField_RTCCON_RTCOE.getAttribute("caption"))

    # output select
    rtcOutSel_names = []
    rtccOutputLabel = ""

    _get_bitfield_names(rtcValGrp_RTCCON_RTCOUTSEL, rtcOutSel_names)
    rtccOutputLabel = rtcBitField_RTCCON_RTCOUTSEL.getAttribute("caption")
    rtccSym_RTCCON_RTCOUTSEL = rtccComponent.createKeyValueSetSymbol("RTCC_OUTPUT_SELECT", rtccSym_RTCCON_RTCOE)
    rtccSym_RTCCON_RTCOUTSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCCON_RTCOUTSEL.setLabel(rtccOutputLabel)
    rtccSym_RTCCON_RTCOUTSEL.setOutputMode( "Value" )
    rtccSym_RTCCON_RTCOUTSEL.setDisplayMode( "Description" )
    for ii in rtcOutSel_names:
        rtccSym_RTCCON_RTCOUTSEL.addKey( ii['key'], ii['value'], ii['desc'] )
    rtccSym_RTCCON_RTCOUTSEL.setDefaultValue(0)
    rtccSym_RTCCON_RTCOUTSEL.setVisible(False)
    rtccSym_RTCCON_RTCOUTSEL.setDependencies(updateSymbolVisblity, ["RTCC_OUTPUT_ENABLE"])

    rtccSym_RTCCON_TIMEDATE = rtccComponent.createBooleanSymbol("RTC_TIMEANDDATE", None)
    rtccSym_RTCCON_TIMEDATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCTIME")
    rtccSym_RTCCON_TIMEDATE.setLabel("Initialize Time & Date")
    rtccSym_RTCCON_TIMEDATE.setDefaultValue(False)

    # Time. Note: this item is treated differently.  Single entry value spans the concatenation of bitfields.
    rtccSym_RTCTIME_TIME = rtccComponent.createStringSymbol("RTCTIME_TIME",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCTIME_TIME.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCTIME")
    rtccSym_RTCTIME_TIME.setLabel("Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_RTCTIME_TIME.setDefaultValue("235950")
    rtccSym_RTCTIME_TIME.setVisible(False)
    rtccSym_RTCTIME_TIME.setDependencies(updateSymbolVisblity, ["RTC_TIMEANDDATE"])

    # Date.  User's entry here spans most significant 24 bits of register RTCDATE
    rtccSym_RTCDATE_DATE = rtccComponent.createStringSymbol("RTCTIME_DATE",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_DATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCDATE")
    rtccSym_RTCDATE_DATE.setLabel("Date (YYMMDD, where YY:00-99, MM:01-12, DD:01-31)")
    rtccSym_RTCDATE_DATE.setDefaultValue("181231")
    rtccSym_RTCDATE_DATE.setVisible(False)
    rtccSym_RTCDATE_DATE.setDependencies(updateSymbolVisblity, ["RTC_TIMEANDDATE"])

    # Day of week.
    rtccSym_RTCDATE_WEEKDAY = rtccComponent.createIntegerSymbol("RTCTIME_WEEKDAY",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_WEEKDAY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCDATE")
    rtccSym_RTCDATE_WEEKDAY.setLabel("Weekday (0-6)")
    rtccSym_RTCDATE_WEEKDAY.setDefaultValue(0)
    rtccSym_RTCDATE_WEEKDAY.setMin(0)
    rtccSym_RTCDATE_WEEKDAY.setMax(6)
    rtccSym_RTCDATE_WEEKDAY.setVisible(False)
    rtccSym_RTCDATE_WEEKDAY.setDependencies(updateSymbolVisblity, ["RTC_TIMEANDDATE"])

    rtccSym_RTCCON_ALARMMENU = rtccComponent.createBooleanSymbol("RTC_ALARM", None)
    rtccSym_RTCCON_ALARMMENU.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCCON_ALARMMENU.setLabel("Initialize Alarm Time and Date")
    rtccSym_RTCCON_ALARMMENU.setDefaultValue(False)

    # Alarm time.  Note: the user entry spans the upper 24 bits of the register ALRMTIME
    rtccSym_ALRMTIME_TIME = rtccComponent.createStringSymbol("RTCALRM_TIME",rtccSym_RTCCON_ALARMMENU)
    rtccSym_ALRMTIME_TIME.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_ALRMTIME_TIME.setLabel("Alarm Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_ALRMTIME_TIME.setDefaultValue("235955")
    rtccSym_ALRMTIME_TIME.setVisible(False)
    rtccSym_ALRMTIME_TIME.setDependencies(updateSymbolVisblity, ["RTC_ALARM"])

    # Alarm date.  User settings span a contiguous set of bitfields.
    rtccSym_RTCCON_ALRMDATE = rtccComponent.createStringSymbol("RTCALRM_DATE",rtccSym_RTCCON_ALARMMENU)
    rtccSym_RTCCON_ALRMDATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCCON_ALRMDATE.setLabel("Alarm Date (MMDD, where MM:01-12, DD:01-31)")
    rtccSym_RTCCON_ALRMDATE.setDefaultValue("1231")
    rtccSym_RTCCON_ALRMDATE.setVisible(False)
    rtccSym_RTCCON_ALRMDATE.setDependencies(updateSymbolVisblity, ["RTC_ALARM"])

    # Alarm mask
    alrmMask_names = []
    _get_bitfield_names(rtcValGrp_RTCALRM_AMASK, alrmMask_names)
    rtccSym_RTCALRM_AMASK = rtccComponent.createKeyValueSetSymbol( "RTCC_ALARM_MASK", rtccSym_RTCCON_ALARMMENU )
    rtccSym_RTCALRM_AMASK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCALRM_AMASK.setLabel("Alarm Frequency")
    rtccSym_RTCALRM_AMASK.setOutputMode( "Value" )
    rtccSym_RTCALRM_AMASK.setDisplayMode( "Description" )
    for ii in alrmMask_names:
        rtccSym_RTCALRM_AMASK.addKey( ii['key'], ii['value'], ii['desc'] )
    rtccSym_RTCALRM_AMASK.setDefaultValue(1)
    rtccSym_RTCALRM_AMASK.setVisible(False)
    rtccSym_RTCALRM_AMASK.setDependencies(updateSymbolVisblity, ["RTC_ALARM"])

    # Alarm day of week.  Only allowed to be user-set if alarm mask is set to once a week.
    rtccSym_ALRMTIME_WDAY = rtccComponent.createIntegerSymbol("RTCALRM_DAY", rtccSym_RTCALRM_AMASK)
    rtccSym_ALRMTIME_WDAY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_ALRMTIME_WDAY.setLabel("Alarm Weekday (0-6)")
    rtccSym_ALRMTIME_WDAY.setDefaultValue(0)
    rtccSym_ALRMTIME_WDAY.setMin(0)
    rtccSym_ALRMTIME_WDAY.setMax(6)
    rtccSym_ALRMTIME_WDAY.setVisible(False)
    rtccSym_ALRMTIME_WDAY.setDependencies(updateAlarmMenuVisiblity, ["RTCC_ALARM_MASK"])

    # Alarm repeat forever
    rtccSym_RTCALRM_ARPT = rtccComponent.createBooleanSymbol("RTCC_ALARM_REPEAT_FOREVER", None)
    rtccSym_RTCALRM_ARPT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCALRM_ARPT.setVisible(True)
    rtccSym_RTCALRM_ARPT.setLabel("Alarm Repeats Forever")
    rtccSym_RTCALRM_ARPT.setDefaultValue(False)

    # Alarm repeat count
    rtccSym_RTCALRM_ARPTCNT = rtccComponent.createIntegerSymbol("RTCALRM_ARPT", rtccSym_RTCALRM_ARPT)
    rtccSym_RTCALRM_ARPTCNT.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:rtcc_02050;register:RTCCON1")
    rtccSym_RTCALRM_ARPTCNT.setVisible(True)
    rtccSym_RTCALRM_ARPTCNT.setLabel(rtcBitField_RTCALRM_ARPT.getAttribute("caption"))
    rtccSym_RTCALRM_ARPTCNT.setDescription("Alarm will repeat n+1 number of times")
    rtccSym_RTCALRM_ARPTCNT.setMin(0)
    rtccSym_RTCALRM_ARPTCNT.setMax(255)
    rtccSym_RTCALRM_ARPTCNT.setDefaultValue(0)
    rtccSym_RTCALRM_ARPTCNT.setDependencies(toggleMenu, ["RTCC_ALARM_REPEAT_FOREVER"])

    # Clock Warning status
    rtccSym_ClkEnComment = rtccComponent.createCommentSymbol("RTCC_CLOCK_ENABLE_COMMENT", None)
    rtccSym_ClkEnComment.setLabel("Warning!!! " + rtccInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    rtccSym_ClkEnComment.setVisible(False)
    rtccSym_ClkEnComment.setDependencies(updateRTCCClockWarningStatus, ["core." + rtccInstanceName.getValue() + "_CLOCK_ENABLE"])

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
    rtccSymHeaderFile.setSourcePath("../peripheral/rtcc_02050/templates/plib_rtcc.h.ftl")
    rtccSymHeaderFile.setOutputName("plib_" + rtccInstanceName.getValue().lower() + ".h")
    rtccSymHeaderFile.setDestPath("/peripheral/rtcc/")
    rtccSymHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtccSymHeaderFile.setType("HEADER")
    rtccSymHeaderFile.setMarkup(True)

    # Instance Source File
    rtccSymSourceFile = rtccComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtccSymSourceFile.setSourcePath("../peripheral/rtcc_02050/templates/plib_rtcc.c.ftl")
    rtccSymSourceFile.setOutputName("plib_" + rtccInstanceName.getValue().lower() + ".c")
    rtccSymSourceFile.setDestPath("/peripheral/rtcc/")
    rtccSymSourceFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtccSymSourceFile.setType("SOURCE")
    rtccSymSourceFile.setMarkup(True)

    #System Initialization
    rtccSymSystemInitFile = rtccComponent.createFileSymbol("RTC_SYS_INIT", None)
    rtccSymSystemInitFile.setType("STRING")
    rtccSymSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtccSymSystemInitFile.setSourcePath("../peripheral/rtcc_02050/templates/system/initialization.c.ftl")
    rtccSymSystemInitFile.setMarkup(True)

    # System Definition
    rtccSymSystemDefFile = rtccComponent.createFileSymbol("RTC_SYS_DEF", None)
    rtccSymSystemDefFile.setType("STRING")
    rtccSymSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtccSymSystemDefFile.setSourcePath("../peripheral/rtcc_02050/templates/system/definitions.h.ftl")
    rtccSymSystemDefFile.setMarkup(True)
