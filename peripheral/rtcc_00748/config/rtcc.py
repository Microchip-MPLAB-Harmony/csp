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
global rtccSym_SOSCEN_warn
################################################################################
#### Business Logic ####
################################################################################
                
def enableMenu(menu, event):
	menu.setVisible(event["value"])

def enableAlrmMenu(menu, event):
    '''
    This is a special menu that appears only if the alarm interval is once a week.
    '''
    if(event["value"]==7):
        menu.setVisible(True)
    else:
        menu.setVisible(False)

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
    for ii in valueNodes:   # do this for all <value > entries for this bitfield
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):  # skip (unused) reserved fields
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')
            
            # Get rid of leading '0x', and convert to int if was hex
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)
            outputList.append(dict)

def checkSoscSetting(menu, event):
    # Sees if the user has not enabled secondary oscillator when selecting it as the RTCC clock source.
    # If so, will display a warning message.
    global rtccSym_SOSCEN_warn
    sosc_enbl = Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SOSCEN")
    if((sosc_enbl=="OFF") and (event["value"]==0)):
        rtccSym_SOSCEN_warn.setVisible(True)
    else:
        rtccSym_SOSCEN_warn.setVisible(False)

def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR")) or ("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        bitMask = hex(1<<bitPosn)
        regName = "IEC"+str(index)
    return regName, str(bitPosn), str(bitMask)
    
def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR")) or ("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        bitMask = hex(1<<bitPosn)
        regName = "IFS"+str(index)
    return regName, str(bitPosn), str(bitMask)
    
def _get_sub_priority_parms(vectorNumber):
    # This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift, 
    # and subpriority bitmask for input vector number
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR")) or ("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 4.0
        index = int(temp)
        subPrioBit = 8*(vectorNumber & 0x3)
        subPrioMask = 0x3  # always 2 bits
        prioMask = 0x7
        prioBit = subPrioBit + 2
        regName = "IPC"+str(index)
    return regName, str(prioBit), str(prioMask), str(subPrioBit), str(subPrioMask)

def updateEnbl(menu, event):
    global rtcVectorNumString
    rtcVectorNumString.setValue(event["value"],2)
    
def updatePrio(menu, event):
    global rtcPriority
    rtcPriority.setValue(str(event["value"]),2)
    
def updateSubprio(menu, event):
    global rtcSubpriority
    rtcSubpriority.setValue(str(event["value"]),2)
    
def updateHandler(menu, event):
    global rtcHandler
    rtcHandler.setValue(event["value"],2)
    
def instantiateComponent(rtcComponent):
    global rtccSym_SOSCEN_warn
    
    rtcBitField_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCCLKSEL"]')
    rtcValGrp_RTCCON_RTCCLKSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCCLKSEL"]')
    
    rtcBitField_RTCCON_RTCOE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCOE"]')
    rtcValGrp_RTCCON_RTCOE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCOE"]')

    rtcBitField_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCCON"]/bitfield@[name="RTCOUTSEL"]')
    rtcValGrp_RTCCON_RTCOUTSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCCON__RTCOUTSEL"]')

    rtcBitField_RTCALRM_AMASK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCALRM"]/bitfield@[name="AMASK"]')
    rtcValGrp_RTCALRM_AMASK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/value-group@[name="RTCALRM__AMASK"]')

    rtcBitField_RTCALRM_ARPT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTCC"]/register-group@[name="RTCC"]/register@[name="RTCALRM"]/bitfield@[name="ARPT"]')
    rtcIrq = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts/interrupt@[name="RTCC"]')
    
    rtcInstanceName = rtcComponent.createStringSymbol("RTC_INSTANCE_NAME", None)
    rtcInstanceName.setVisible(False)
    rtcInstanceName.setDefaultValue(rtcComponent.getID().upper())
    Log.writeInfoMessage("Running " + rtcInstanceName.getValue())
    
    # Get register names, mask values, bit shifts based on vector number
    vectorNum = int(rtcIrq.getAttribute("index"))
    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(vectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(vectorNum)
    prioRegName, prioShift, prioMask, subprioShift, subprioMask = _get_sub_priority_parms(vectorNum)

    # Below create family-specific register names / masking needed by ftl file
    rtcPrioRegWrt = rtcComponent.createStringSymbol("RTC_PRIOREG_WRT", None)
    rtcPrioRegWrt.setDefaultValue(prioRegName+"SET")
    rtcPrioRegWrt.setVisible(False)
    rtcPrioRegShift = rtcComponent.createStringSymbol("RTC_PRIOREG_SHIFT", None)
    rtcPrioRegShift.setDefaultValue(prioShift)
    rtcPrioRegShift.setVisible(False)
    rtcSubPrioRegShift = rtcComponent.createStringSymbol("RTC_SUBPRIOREG_SHIFT", None)
    rtcSubPrioRegShift.setDefaultValue(subprioShift)
    rtcSubPrioRegShift.setVisible(False)
    rtcEnblRegWrt = rtcComponent.createStringSymbol("RTC_ENBLREG_RD", None)
    rtcEnblRegWrt.setDefaultValue(enblRegName)
    rtcEnblRegWrt.setVisible(False)
    rtcEnblRegWrt = rtcComponent.createStringSymbol("RTC_ENBLREG_WRT", None)
    rtcEnblRegWrt.setDefaultValue(enblRegName+"SET")
    rtcEnblRegWrt.setVisible(False)
    rtcEnblRegClr = rtcComponent.createStringSymbol("RTC_ENBLREG_CLR", None)
    rtcEnblRegClr.setDefaultValue(enblRegName+"CLR")
    rtcEnblRegClr.setVisible(False) 
    rtcEnblRegShift = rtcComponent.createStringSymbol("RTC_ENBLREG_SHIFT", None)
    rtcEnblRegShift.setDefaultValue(enblBitPosn)
    rtcEnblRegShift.setVisible(False)
    rtcEnblRegVal = rtcComponent.createStringSymbol("RTC_ENBLREG_ENABLE_VALUE", None)
    rtcEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
    rtcEnblRegVal.setVisible(False)
    rtcStatRegClr = rtcComponent.createStringSymbol("RTC_STATREG_CLR", None)
    rtcStatRegClr.setDefaultValue(statRegName+"CLR")
    rtcStatRegClr.setVisible(False)
    rtcStatRegRd = rtcComponent.createStringSymbol("RTC_STATREG_RD", None)
    rtcStatRegRd.setDefaultValue(statRegName)
    rtcStatRegRd.setVisible(False)
    rtcStatRegShift = rtcComponent.createStringSymbol("RTC_STATREG_SHIFT", None)
    rtcStatRegShift.setDefaultValue(statBitPosn)
    rtcStatRegShift.setVisible(False)
    rtcStatRegShiftVal = rtcComponent.createStringSymbol("RTC_STATREG_SHIFT_VALUE", None)
    rtcStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
    rtcStatRegShiftVal.setVisible(False)
    rtcStatRegMask = rtcComponent.createStringSymbol("RTC_STATREG_MASK", None)
    rtcStatRegMask.setDefaultValue(statMask)
    rtcStatRegMask.setVisible(False)
    rtcVectorNum = rtcComponent.createIntegerSymbol("RTC_VECTOR_NUMBER", None)
    rtcVectorNum.setDefaultValue(vectorNum)
    rtcVectorNum.setVisible(False)

    # for use in ftl file
    global rtcVectorNumString
    rtcVectorNumString = rtcComponent.createBooleanSymbol("RTC_VEC_ENABLE", None)
    rtcVectorNumString.setVisible(False)
    targetSym = "NVIC_" + str(rtcVectorNum.getValue()) + "_0_ENABLE"
    rtcVectorNumString.setDependencies(updateEnbl,["core." + targetSym])

    # for use in ftl file
    global rtcHandler
    rtcHandler = rtcComponent.createStringSymbol("RTC_HANDLER", None)
    targetSym = "NVIC_" + str(rtcVectorNum.getValue()) + "_0_HANDLER"
    val = Database.getSymbolValue("core",targetSym)
    rtcHandler.setDefaultValue(val)
    rtcHandler.setDependencies(updateHandler,["core." + targetSym])   
    rtcHandler.setVisible(False)
    
    # for use in ftl file
    global rtcPriority
    rtcPriority = rtcComponent.createStringSymbol("RTC_PRIORITY", None)
    targetSym = "NVIC_" + str(rtcVectorNum.getValue()) + "_0_PRIORITY"
    val = Database.getSymbolValue("core",targetSym)
    rtcPriority.setDefaultValue(val)
    rtcPriority.setDependencies(updatePrio,["core." + targetSym])    
    rtcPriority.setVisible(False)
    
    # for use in ftl file
    global rtcSubpriority
    rtcSubpriority = rtcComponent.createStringSymbol("RTC_SUBPRIORITY", None)
    targetSym = "NVIC_" + str(rtcVectorNum.getValue()) + "_0_SUBPRIORITY"
    val = Database.getSymbolValue("core",targetSym)
    rtcSubpriority.setDefaultValue(val)
    rtcSubpriority.setDependencies(updateSubprio,["core." + targetSym])    
    rtcSubpriority.setVisible(False)
    
    # This symbol is used as main entrypoint for RTCC code in ftl files
    rtccSym_USE_SVC = rtcComponent.createBooleanSymbol("USE_SYS_RTCC", None)
    rtccSym_USE_SVC.setVisible(False)
    rtccSym_USE_SVC.setDefaultValue(True)

    # clock source
    clkSel_names = []
    _get_bitfield_names(rtcValGrp_RTCCON_RTCCLKSEL, clkSel_names)
    rtccSym_RTCCON_RTCCLKSEL = rtcComponent.createKeyValueSetSymbol("RTCC_CLOCK_SOURCE", None )
    rtccSym_RTCCON_RTCCLKSEL.setLabel(rtcBitField_RTCCON_RTCCLKSEL.getAttribute("caption"))
    rtccSym_RTCCON_RTCCLKSEL.setOutputMode( "Value" )
    rtccSym_RTCCON_RTCCLKSEL.setDisplayMode( "Description" )
    for ii in clkSel_names:
        rtccSym_RTCCON_RTCCLKSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    rtccSym_RTCCON_RTCCLKSEL.setDefaultValue(0)
    rtccSym_RTCCON_RTCCLKSEL.setDependencies(checkSoscSetting,["RTCC_CLOCK_SOURCE"])

    # Create warning menu for when user selects external source but SOSCEN not set in clock module
    rtccSym_SOSCEN_warn = rtcComponent.createMenuSymbol("SOSCEN_WARN",rtccSym_RTCCON_RTCCLKSEL)
    rtccSym_SOSCEN_warn.setLabel("*** Warning: set secondary oscillator enable to ON in clock configurator settings ***")
    rtccSym_SOSCEN_warn.setVisible(False)

    # RTCC output enable
    rtccSym_RTCCON_RTCOE = rtcComponent.createBooleanSymbol("RTCC_OUTPUT_ENABLE", None)
    rtccSym_RTCCON_RTCOE.setVisible(True)
    rtccSym_RTCCON_RTCOE.setLabel(rtcBitField_RTCCON_RTCOE.getAttribute("caption"))
    rtccSym_RTCCON_RTCOE.setDefaultValue(False)
    
    # output select
    rtcOutSel_names = []
    _get_bitfield_names(rtcValGrp_RTCCON_RTCOUTSEL, rtcOutSel_names)
    rtccSym_RTCCON_RTCOUTSEL = rtcComponent.createKeyValueSetSymbol( "RTCC_OUTPUT_SELECT", rtccSym_RTCCON_RTCOE )
    rtccSym_RTCCON_RTCOUTSEL.setLabel(rtcBitField_RTCCON_RTCOUTSEL.getAttribute("caption"))
    rtccSym_RTCCON_RTCOUTSEL.setOutputMode( "Value" )
    rtccSym_RTCCON_RTCOUTSEL.setDisplayMode( "Description" )
    for ii in rtcOutSel_names:
        rtccSym_RTCCON_RTCOUTSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    rtccSym_RTCCON_RTCOUTSEL.setDefaultValue(0)
    rtccSym_RTCCON_RTCOUTSEL.setDependencies(enableMenu,["RTCC_OUTPUT_ENABLE"])
    
    rtccSym_RTCCON_TIMEDATE = rtcComponent.createMenuSymbol("RTC_TIMEANDDATE", None)
    rtccSym_RTCCON_TIMEDATE.setLabel("Time & Date")

    # Time. Note: this item is treated differently.  Single entry value spans the concatenation of bitfields.    
    rtccSym_RTCTIME_TIME = rtcComponent.createStringSymbol("RTCTIME_TIME",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCTIME_TIME.setLabel("Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_RTCTIME_TIME.setDefaultValue("235950")
    rtccSym_RTCTIME_TIME.setVisible(True)
    
    # Date.  User's entry here spans most significant 24 bits of register RTCDATE
    rtccSym_RTCDATE_DATE = rtcComponent.createStringSymbol("RTCTIME_DATE",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_DATE.setLabel("Date (YYMMDD, where YY:00-99, MM:01-12, DD:01-31)")
    rtccSym_RTCDATE_DATE.setDefaultValue("180101")
    rtccSym_RTCDATE_DATE.setVisible(True)
    
    # Day of week.
    rtccSym_RTCDATE_WEEKDAY = rtcComponent.createIntegerSymbol("RTCTIME_WEEKDAY",rtccSym_RTCCON_TIMEDATE)
    rtccSym_RTCDATE_WEEKDAY.setLabel("Weekday (0-6)")
    rtccSym_RTCDATE_WEEKDAY.setDefaultValue(0)
    rtccSym_RTCDATE_WEEKDAY.setVisible(True)
    
    rtccSym_RTCCON_ALARMMENU = rtcComponent.createMenuSymbol("RTC_ALARM", None)
    rtccSym_RTCCON_ALARMMENU.setLabel("Alarm")
    
    # Alarm time.  Note: the user entry spans the upper 24 bits of the register ALRMTIME
    rtccSym_ALRMTIME_TIME = rtcComponent.createStringSymbol("RTCALRM_TIME",rtccSym_RTCCON_ALARMMENU)
    rtccSym_ALRMTIME_TIME.setLabel("Alarm Time (HHMMSS, where HH:00-24, MM:00-59, SS:00-59)")
    rtccSym_ALRMTIME_TIME.setDefaultValue("000005")
    rtccSym_ALRMTIME_TIME.setVisible(True)
    
    # Alarm date.  User settings span a contiguous set of bitfields.
    rtccSym_RTCCON_ALRMDATE = rtcComponent.createStringSymbol("RTCALRM_DATE",rtccSym_RTCCON_ALARMMENU)
    rtccSym_RTCCON_ALRMDATE.setLabel("Alarm Date (MMDD, where MM:01-12, DD:01-31)")
    rtccSym_RTCCON_ALRMDATE.setDefaultValue("0101")
    rtccSym_RTCCON_ALRMDATE.setVisible(True)
    
    # Alarm mask
    alrmMask_names = []
    _get_bitfield_names(rtcValGrp_RTCALRM_AMASK, alrmMask_names)
    rtccSym_RTCALRM_AMASK = rtcComponent.createKeyValueSetSymbol( "RTCC_ALARM_MASK", None )
    rtccSym_RTCALRM_AMASK.setLabel(rtcBitField_RTCALRM_AMASK.getAttribute("caption"))
    rtccSym_RTCALRM_AMASK.setOutputMode( "Value" )
    rtccSym_RTCALRM_AMASK.setDisplayMode( "Description" )
    for ii in alrmMask_names:
        rtccSym_RTCALRM_AMASK.addKey( ii['desc'], ii['value'], ii['key'] )
    rtccSym_RTCALRM_AMASK.setDefaultValue(0)

    # Alarm day of week.  Only allowed to be user-set if alarm mask is set to once a week.
    rtccSym_ALRMTIME_WDAY = rtcComponent.createIntegerSymbol("RTCALRM_DAY",rtccSym_RTCALRM_AMASK)
    rtccSym_ALRMTIME_WDAY.setLabel("Alarm Weekday (0-6)")
    rtccSym_ALRMTIME_WDAY.setDefaultValue(0)
    rtccSym_ALRMTIME_WDAY.setMin(0)
    rtccSym_ALRMTIME_WDAY.setMax(255)
    rtccSym_ALRMTIME_WDAY.setVisible(False)
    rtccSym_ALRMTIME_WDAY.setDependencies(enableAlrmMenu,["RTCC_ALARM_MASK"])

    # Alarm repeat forever
    rtccSym_RTCALRM_ARPT = rtcComponent.createBooleanSymbol("RTCC_ALARM_REPEAT_FOREVER", None)
    rtccSym_RTCALRM_ARPT.setVisible(True)
    rtccSym_RTCALRM_ARPT.setLabel("Alarm Repeats Forever")
    rtccSym_RTCALRM_ARPT.setDefaultValue(False)
    
    # Alarm repeat count
    rtccSym_RTCALRM_ARPTCNT = rtcComponent.createIntegerSymbol("RTCALRM_ARPT",rtccSym_RTCALRM_ARPT)
    rtccSym_RTCALRM_ARPTCNT.setVisible(True)
    rtccSym_RTCALRM_ARPTCNT.setLabel(rtcBitField_RTCALRM_ARPT.getAttribute("caption"))
    rtccSym_RTCALRM_ARPTCNT.setMin(0)
    rtccSym_RTCALRM_ARPTCNT.setMax(255)
    rtccSym_RTCALRM_ARPTCNT.setDefaultValue(0)
    rtccSym_RTCALRM_ARPTCNT.setDependencies(enableMenu, ["RTCC_ALARM_REPEAT_FOREVER"])

    ################################ Code Generation ###############################
    configName = Variables.get("__CONFIGURATION_NAME")

    rtcModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"RTCC\"]")
    rtcModuleID = rtcModuleNode.getAttribute("id")

    # Instance Header File
    rtcHeaderFile = rtcComponent.createFileSymbol("RTC_INSTANCE_HEADER", None)
    rtcHeaderFile.setSourcePath("../peripheral/rtcc_00748/templates/plib_rtcc.h.ftl")
    rtcHeaderFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".h")
    rtcHeaderFile.setDestPath("/peripheral/rtcc/")
    rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtcHeaderFile.setType("HEADER")
    rtcHeaderFile.setMarkup(True)
    
    # Instance Source File
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_TIMER_SOURCE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtcc_00748/templates/plib_rtcc.c.ftl")
    rtcSourceFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".c")
    rtcSourceFile.setDestPath("/peripheral/rtcc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtcc/")
    rtcSourceFile.setType("SOURCE")
    rtcSourceFile.setMarkup(True)

    #System Initialization
    rtcSystemInitFile = rtcComponent.createFileSymbol("RTC_SYS_INIT", None)
    rtcSystemInitFile.setType("STRING")
    rtcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtcSystemInitFile.setSourcePath("../peripheral/rtcc_00748/templates/system/initialization.c.ftl")
    rtcSystemInitFile.setMarkup(True)

    # System Definition
    rtcSystemDefFile = rtcComponent.createFileSymbol("RTC_SYS_DEF", None)
    rtcSystemDefFile.setType("STRING")
    rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtcSystemDefFile.setSourcePath("../peripheral/rtcc_00748/templates/system/definitions.h.ftl")
    rtcSystemDefFile.setMarkup(True)
