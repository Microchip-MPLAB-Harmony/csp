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

#Function for initiating the UI
global rtcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

def interruptControl(symbol, event):
    global interruptVector
    global interruptHandler
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, rtcInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "RTC_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)


def rtcTHIGH(rtcSym_MR_THIGH, event):
    data = rtcSym_MR_THIGH.getComponent()
    rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
    rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
    if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
        rtcSym_MR_THIGH.setVisible(False)
    else:
        rtcSym_MR_THIGH.setVisible(True)


def rtcTPERIOD(rtcSym_MR_TPERIOD, event):
    data = rtcSym_MR_TPERIOD.getComponent()
    rtcOUT0 = data.getSymbolValue("RTC_MR_OUT0")
    rtcOUT1 = data.getSymbolValue("RTC_MR_OUT1")
    if rtcOUT0 != "PROG_PULSE" and rtcOUT1 != "PROG_PULSE":
        rtcSym_MR_TPERIOD.setVisible(False)
    else:
        rtcSym_MR_TPERIOD.setVisible(True)


def instantiateComponent(rtcComponent):
    global rtcInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    out0_names = []
    out1_names = []
    thigh_names = []
    tperiod_names = []
    timevsel_names = []
    calevsel_names = []

    rtcInstanceName = rtcComponent.createStringSymbol("RTC_INSTANCE_NAME", None)
    rtcInstanceName.setVisible(False)
    rtcInstanceName.setDefaultValue(rtcComponent.getID().upper())

    rtcBitField_MR_UTC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="UTC"]')

    rtcBitField_MR_OUT0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="OUT0"]')
    rtcValGrp_MR_OUT0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__OUT0"]')

    rtcBitField_MR_OUT1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="OUT1"]')
    rtcValGrp_MR_OUT1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__OUT1"]')

    rtcBitField_MR_THIGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="THIGH"]')
    rtcValGrp_MR_THIGH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__THIGH"]')

    rtcBitField_MR_TPERIOD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_MR"]/bitfield@[name="TPERIOD"]')
    rtcValGrp_MR_TPERIOD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_MR__TPERIOD"]')

    rtcBitField_CR_TIMEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_CR"]/bitfield@[name="TIMEVSEL"]')
    rtcValGrp_CR_TIMEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_CR__TIMEVSEL"]')

    rtcBitField_CR_CALEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/register-group@[name="RTC"]/register@[name="RTC_CR"]/bitfield@[name="CALEVSEL"]')
    rtcValGrp_CR_CALEVSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RTC"]/value-group@[name="RTC_CR__CALEVSEL"]')

    #Create the top menu
    rtcMenu = rtcComponent.createMenuSymbol("RTC_MENU_0", None)
    rtcMenu.setLabel("Hardware Settings ")
    #Create a Checkbox to enable disable interrupts
    rtcInterrupt = rtcComponent.createBooleanSymbol("rtcEnableInterrupt", rtcMenu)
    rtcInterrupt.setLabel("Enable Interrupt")
    rtcInterrupt.setDefaultValue(True)

    interruptVector = rtcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    interruptHandler = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = rtcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"

    Database.clearSymbolValue("core", interruptVector)
    Database.setSymbolValue("core", interruptVector, True, 2)
    Database.clearSymbolValue("core", interruptHandler)
    Database.setSymbolValue("core", interruptHandler, rtcInstanceName.getValue() + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", interruptHandlerLock)
    Database.setSymbolValue("core", interruptHandlerLock, True, 2)

    # Interrupt Dynamic settings
    rtcInterruptControl = rtcComponent.createBooleanSymbol("RTC_ENABLE", None)
    rtcInterruptControl.setDependencies(interruptControl, ["rtcEnableInterrupt"])
    rtcInterruptControl.setVisible(False)

    # Create a Checkbox to enable 12 -v- 24 HR mode
    rtc12HrMode = rtcComponent.createBooleanSymbol("RTC_12HR_MODE", rtcMenu)
    rtc12HrMode.setLabel("Enable 12 HR Mode")
    rtc12HrMode.setDefaultValue(False)

    if rtcBitField_MR_UTC:
        rtcSym_MR_UTC = rtcComponent.createBooleanSymbol("RTC_MR_UTC", rtcMenu)
        rtcSym_MR_UTC.setLabel("Enable UTC Mode")
        rtcSym_MR_UTC.setDefaultValue( False )

    for id in range(0,len(rtcValGrp_MR_OUT0.getChildren())):
        out0_names.append(rtcValGrp_MR_OUT0.getChildren()[id].getAttribute("name"))

    rtcSym_MR_OUT0 = rtcComponent.createComboSymbol("RTC_MR_OUT0", rtcMenu, out0_names)
    rtcSym_MR_OUT0.setLabel(rtcBitField_MR_OUT0.getAttribute("caption"))
    rtcSym_MR_OUT0.setDefaultValue("NO_WAVE")

    for id in range(0,len(rtcValGrp_MR_OUT1.getChildren())):
        out1_names.append(rtcValGrp_MR_OUT1.getChildren()[id].getAttribute("name"))

    rtcSym_MR_OUT1 = rtcComponent.createComboSymbol("RTC_MR_OUT1", rtcMenu, out1_names)
    rtcSym_MR_OUT1.setLabel(rtcBitField_MR_OUT1.getAttribute("caption"))
    rtcSym_MR_OUT1.setDefaultValue("NO_WAVE")

    for id in range(0,len(rtcValGrp_MR_THIGH.getChildren())):
        thigh_names.append(rtcValGrp_MR_THIGH.getChildren()[id].getAttribute("name"))

    rtcSym_MR_THIGH = rtcComponent.createComboSymbol("RTC_MR_THIGH", rtcMenu, thigh_names)
    rtcSym_MR_THIGH.setLabel(rtcBitField_MR_THIGH.getAttribute("caption"))
    rtcSym_MR_THIGH.setDefaultValue("H_31MS")
    rtcSym_MR_THIGH.setVisible(False)
    rtcSym_MR_THIGH.setDependencies(rtcTHIGH, ["RTC_MR_OUT0", "RTC_MR_OUT1"])

    for id in range(0,len(rtcValGrp_MR_TPERIOD.getChildren())):
        tperiod_names.append(rtcValGrp_MR_TPERIOD.getChildren()[id].getAttribute("name"))

    rtcSym_MR_TPERIOD = rtcComponent.createComboSymbol("RTC_MR_TPERIOD", rtcMenu, tperiod_names)
    rtcSym_MR_TPERIOD.setLabel(rtcBitField_MR_TPERIOD.getAttribute("caption"))
    rtcSym_MR_TPERIOD.setDefaultValue("P_1S")
    rtcSym_MR_TPERIOD.setVisible(False)
    rtcSym_MR_TPERIOD.setDependencies(rtcTPERIOD, ["RTC_MR_OUT0", "RTC_MR_OUT1"])

    for id in range(0,len(rtcValGrp_CR_TIMEVSEL.getChildren())):
        timevsel_names.append(rtcValGrp_CR_TIMEVSEL.getChildren()[id].getAttribute("name"))

    rtcSym_CR_TIMEVSEL= rtcComponent.createComboSymbol("RTC_CR_TIMEVSEL", rtcMenu, timevsel_names)
    rtcSym_CR_TIMEVSEL.setLabel(rtcBitField_CR_TIMEVSEL.getAttribute("caption"))
    rtcSym_CR_TIMEVSEL.setDefaultValue("MINUTE")

    for id in range(0,len(rtcValGrp_CR_CALEVSEL.getChildren())):
        calevsel_names.append(rtcValGrp_CR_CALEVSEL.getChildren()[id].getAttribute("name"))

    rtcSym_CR_CALEVSEL = rtcComponent.createComboSymbol("RTC_CR_CALEVSEL", rtcMenu, calevsel_names)
    rtcSym_CR_CALEVSEL.setLabel(rtcBitField_CR_CALEVSEL.getAttribute("caption"))
    rtcSym_CR_CALEVSEL.setDefaultValue("WEEK")

    configName = Variables.get("__CONFIGURATION_NAME")

    rtcCommonHeaderFile = rtcComponent.createFileSymbol("RTC_COMMON_HEADER_FILE", None)
    rtcCommonHeaderFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc_common.h")
    rtcCommonHeaderFile.setMarkup(False)
    rtcCommonHeaderFile.setOutputName("plib_rtc_common.h")
    rtcCommonHeaderFile.setOverwrite(True)
    rtcCommonHeaderFile.setDestPath("peripheral/rtc/")
    rtcCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcCommonHeaderFile.setType("HEADER")
    # Generate Output Header
    rtcHeaderFile = rtcComponent.createFileSymbol("RTC_HEADER_FILE", None)
    rtcHeaderFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.h.ftl")
    rtcHeaderFile.setMarkup(True)
    rtcHeaderFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".h")
    rtcHeaderFile.setOverwrite(True)
    rtcHeaderFile.setDestPath("peripheral/rtc/")
    rtcHeaderFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcHeaderFile.setType("HEADER")
    # Generate Output source
    rtcSourceFile = rtcComponent.createFileSymbol("RTC_C_SOURCE_FILE", None)
    rtcSourceFile.setSourcePath("../peripheral/rtc_6056/templates/plib_rtc.c.ftl")
    rtcSourceFile.setMarkup(True)
    rtcSourceFile.setOutputName("plib_"+rtcInstanceName.getValue().lower()+".c")
    rtcSourceFile.setOverwrite(True)
    rtcSourceFile.setDestPath("peripheral/rtc/")
    rtcSourceFile.setProjectPath("config/" + configName + "/peripheral/rtc/")
    rtcSourceFile.setType("SOURCE")
    rtcSystemInitFile = rtcComponent.createFileSymbol("RTC_SYSTEM_INITIALIZE_FILE", None)
    rtcSystemInitFile.setType("STRING")
    rtcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rtcSystemInitFile.setSourcePath("../peripheral/rtc_6056/templates/system/initialization.c.ftl")
    rtcSystemInitFile.setMarkup(True)

    rtcSystemDefFile = rtcComponent.createFileSymbol("RTC_SYSTEM_DEFINITION_FILE", None)
    rtcSystemDefFile.setType("STRING")
    rtcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rtcSystemDefFile.setSourcePath("../peripheral/rtc_6056/templates/system/definitions.h.ftl")
    rtcSystemDefFile.setMarkup(True)

