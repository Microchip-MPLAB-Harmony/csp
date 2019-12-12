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

from math import ceil

################################################################################
#### Global Variables ####
################################################################################

global interruptVector
global interruptHandler
global interruptHandlerLock
global supcInstanceName

supcSym_WUIR_WKUPEN = []
supcSym_WUIR_WKUPT = []

sclk = [1, 3, 32, 512, 4096, 32768]

################################################################################
#### Business Logic ####
################################################################################

def interruptControl(symbol, event):

    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if event["value"] == True:
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, supcInstanceName.getValue() +  "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, supcInstanceName.getValue() +  "_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def disableWKUP0(symbol, event):

    if event["value"] == True:
        symbol.setValue(False, 1)

def disableWKUP1(symbol, event):

    if event["value"] == True:
        symbol.setValue(False, 1)

def calcPulseWidth(symbol, event):

    i = event["symbol"].getSelectedValue()
    numSlck = sclk[int(i, 16)]
    time = float(numSlck) / 32768
    timeUsInt = int(time * 1e6)
    timeMs = float(timeUsInt) / 1000

    symbol.setLabel("Minimum WKUPx Pulse Width: " + str(timeMs) + " ms ( " + str(numSlck) + " SLCK Cycles )")

def disableBKUPRST(symbol, event):

    if event["value"] == False:
        symbol.setValue(False, 1)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(supcComponent):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global supcInstanceName

    supcRegister_WUMR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_WUMR"]')
    supcRegister_PWMR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_PWMR"]')
    supcBitField_CR_VROFF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_CR"]/bitfield@[name="VROFF"]')
    supcBitField_MR_ONE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="ONE"]')
    supcBitField_MR_ONEA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="ONEA"]')
    supcBitField_MR_CTPSWITCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="CTPSWITCH"]')
    supcBitField_MR_CDPSWITCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="CDPSWITCH"]')
    supcBitField_MR_PSWITCH1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="PSWITCH1"]')
    supcBitField_MR_PSWITCH2 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="PSWITCH2"]')

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())

    # SM configuration
    supcSMMenu = supcComponent.createMenuSymbol("SM_ENABLE", None)
    supcSMMenu.setLabel("Supply Monitor")

    supcSym_SMMR_SMTH = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_SMTH", supcSMMenu)
    supcSym_SMMR_SMTH.setLabel("Supply Monitor Threshold")

    supcValGrp_SMMR_SMTH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_SMMR__SMTH"]')
    supcValGrp_SMMR_SMTH_Values = supcValGrp_SMMR_SMTH.getChildren()

    for index in range(len(supcValGrp_SMMR_SMTH_Values)):
        supcValGrp_SMMR_SMTH_Key_Name = supcValGrp_SMMR_SMTH_Values[index].getAttribute("name")
        supcValGrp_SMMR_SMTH_Key_Value = supcValGrp_SMMR_SMTH_Values[index].getAttribute("value")
        supcValGrp_SMMR_SMTH_Key_Description = supcValGrp_SMMR_SMTH_Values[index].getAttribute("caption")
        supcSym_SMMR_SMTH.addKey(supcValGrp_SMMR_SMTH_Key_Name, supcValGrp_SMMR_SMTH_Key_Value, supcValGrp_SMMR_SMTH_Key_Description)

    supcSym_SMMR_SMTH.setOutputMode("Value")
    supcSym_SMMR_SMTH.setDisplayMode("Description")
    supcSym_SMMR_SMTH.setSelectedKey(supcValGrp_SMMR_SMTH_Key_Name, 1)

    supcSym_SMMR_SMSMPL = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_SMSMPL", supcSMMenu)
    supcSym_SMMR_SMSMPL.setLabel("Supply Monitor Sampling Period")

    supcValGrp_SMMR_SMSMPL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_SMMR__SMSMPL"]')
    supcValGrp_SMMR_SMSMPL_Values = supcValGrp_SMMR_SMSMPL.getChildren()

    for index in range(len(supcValGrp_SMMR_SMSMPL_Values)):
        supcValGrp_SMMR_SMSMPL_Key_Name = supcValGrp_SMMR_SMSMPL_Values[index].getAttribute("name")
        supcValGrp_SMMR_SMSMPL_Key_Value = supcValGrp_SMMR_SMSMPL_Values[index].getAttribute("value")
        supcValGrp_SMMR_SMSMPL_Key_Description = supcValGrp_SMMR_SMSMPL_Values[index].getAttribute("caption")
        supcSym_SMMR_SMSMPL.addKey(supcValGrp_SMMR_SMSMPL_Key_Name, supcValGrp_SMMR_SMSMPL_Key_Value, supcValGrp_SMMR_SMSMPL_Key_Description)

    supcSym_SMMR_SMSMPL.setOutputMode("Value")
    supcSym_SMMR_SMSMPL.setDisplayMode("Description")
    supcSym_SMMR_SMSMPL.setDefaultValue(0)

    supcSym_SMMR_SMIEN = supcComponent.createBooleanSymbol("SUPC_SMMR_SMIEN", supcSMMenu)
    supcSym_SMMR_SMIEN.setLabel("Enable Supply Monitor Interrupt")

    supcSym_SMMR_SMRSTEN = supcComponent.createBooleanSymbol("SUPC_SMMR_SMRSTEN", supcSMMenu)
    supcSym_SMMR_SMRSTEN.setLabel("Enable Supply Monitor Reset")

    supcSym_WUMR = supcComponent.createBooleanSymbol("SUPC_WUMR", None)
    supcSym_WUMR.setVisible(False)
    supcSym_WUMR.setDefaultValue(supcRegister_WUMR != None)

    supcSym_PWMR = supcComponent.createBooleanSymbol("SUPC_PWMR", None)
    supcSym_PWMR.setVisible(False)
    supcSym_PWMR.setDefaultValue(supcRegister_PWMR != None)

    supcSym_CR_VROFF = supcComponent.createBooleanSymbol("SUPC_CR_VROFF", None)
    supcSym_CR_VROFF.setVisible(False)
    supcSym_CR_VROFF.setDefaultValue(supcBitField_CR_VROFF != None)

    supcSym_MR_ONE = supcComponent.createBooleanSymbol("SUPC_MR_ONE", None)
    supcSym_MR_ONE.setVisible(False)
    supcSym_MR_ONE.setDefaultValue(supcBitField_MR_ONE != None)

    supcSym_MR_ONEA = supcComponent.createBooleanSymbol("SUPC_MR_ONEA", None)
    supcSym_MR_ONEA.setVisible(False)
    supcSym_MR_ONEA.setDefaultValue(supcBitField_MR_ONEA != None)

    GPBR = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPBR\"]/register-group@[name=\"GPBR\"]/register")
    GPBRRegNum = GPBR.getAttribute("count")

    gpbrSym_SYSGPBR = supcComponent.createIntegerSymbol("SYS_GPBR_REGISTER", None)
    gpbrSym_SYSGPBR.setVisible(False)
    gpbrSym_SYSGPBR.setDefaultValue(int(GPBRRegNum))

    supcLPMenu = supcComponent.createMenuSymbol("LOW_POWER_MENU", None)
    supcLPMenu.setLabel("Low Power Configuration")

    #Check weather wakeup support is there or not
    if supcSym_WUMR.getValue():
        supcSym_WUMR_RTCEN = supcComponent.createBooleanSymbol("SUPC_WUMR_RTCEN", supcLPMenu)
        supcSym_WUMR_RTCEN.setLabel("Enable RTC Alarm Wakeup")

        supcSym_WUMR_RTTEN = supcComponent.createBooleanSymbol("SUPC_WUMR_RTTEN", supcLPMenu)
        supcSym_WUMR_RTTEN.setLabel("Enable RTT Alarm Wakeup")

        supcSym_WUMR_SMEN = supcComponent.createBooleanSymbol("SUPC_WUMR_SMEN", supcLPMenu)
        supcSym_WUMR_SMEN.setLabel("Enable Supply Monitor Wakeup")

        supcWKUPMenu = supcComponent.createMenuSymbol("WKUP_MENU", supcLPMenu)
        supcWKUPMenu.setLabel("Configure Wakeup Pins (WKUPx)")

        supcSym_WUMR_WKUPDBC = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_WKUPDBC", supcWKUPMenu)
        supcSym_WUMR_WKUPDBC.setLabel("Minimum Pulse Width for Wakeup Input")

        supcValGrp_WUMR_WKUPDBC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_WUMR__WKUPDBC"]')
        supcValGrp_WUMR_WKUPDBC_Values = supcValGrp_WUMR_WKUPDBC.getChildren()

        for index in range(len(supcValGrp_WUMR_WKUPDBC_Values)):
            supcValGrp_WUMR_WKUPDBC_Key_Name = supcValGrp_WUMR_WKUPDBC_Values[index].getAttribute("name")
            supcValGrp_WUMR_WKUPDBC_Key_Value = supcValGrp_WUMR_WKUPDBC_Values[index].getAttribute("value")
            supcValGrp_WUMR_WKUPDBC_Key_Description = supcValGrp_WUMR_WKUPDBC_Values[index].getAttribute("caption")
            supcSym_WUMR_WKUPDBC.addKey(supcValGrp_WUMR_WKUPDBC_Key_Name, supcValGrp_WUMR_WKUPDBC_Key_Value, supcValGrp_WUMR_WKUPDBC_Key_Description)

        supcSym_WUMR_WKUPDBC.setOutputMode("Value")
        supcSym_WUMR_WKUPDBC.setDisplayMode("Description")
        supcSym_WUMR_WKUPDBC.setDefaultValue(0)

        supcSym_PULSE_WIDTH_COMMENT = supcComponent.createCommentSymbol("PULSE_WIDTH_COMMENT", supcWKUPMenu)
        supcSym_PULSE_WIDTH_COMMENT.setLabel("Minimum WKUPx Pulse Width: 0.03 ms ( 1 SLCK Cycles )")
        supcSym_PULSE_WIDTH_COMMENT.setDependencies(calcPulseWidth, ["SUPC_WUMR_WKUPDBC"])

        supcSym_WUIR = supcComponent.createHexSymbol("SUPC_WUIR", supcWKUPMenu)
        supcSym_WUIR.setVisible(False)

        supcSym_WKUP_Inputs = supcComponent.createIntegerSymbol("SUPC_WKUP_INPUTS", supcWKUPMenu)
        supcSym_WKUP_Inputs.setVisible(False)
        supcSym_WKUP_Inputs.setDefaultValue(16)

        #------------------------- ATDF Read -------------------------------------
        packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
        availablePins = []        # array to save available pins
        signal = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] #array to save available signals

        children = []
        val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(packageName) + "\"]")
        children = val.getChildren()
        for pad in range (0, len(children)):
            availablePins.append(children[pad].getAttribute("pad"))

        wakeup_signals = []
        supc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SUPC\"]/instance@[name=\"" + supcInstanceName.getValue() + "\"]/signals")
        wakeup_signals = supc.getChildren()
        for pad in range (0, len(wakeup_signals)):
            if "index" in wakeup_signals[pad].getAttributeList():
                padSignal = wakeup_signals[pad].getAttribute("pad")
                if padSignal in availablePins:
                    signal[int(wakeup_signals[pad].getAttribute("index"))] = True

        for id in range (0, len(signal)):
            supcSym_WUIR_WKUPEN.append(id)
            supcSym_WUIR_WKUPEN[id] = supcComponent.createBooleanSymbol("SUPC_WUIR_WKUPEN" + str(id), supcWKUPMenu)
            supcSym_WUIR_WKUPEN[id].setLabel("Enable WKUP" + str(id) + " Input")
            if signal[id] == False:
                supcSym_WUIR_WKUPEN[id].setVisible(False)

            supcSym_WUIR_WKUPT.append(id)
            supcSym_WUIR_WKUPT[id] = supcComponent.createKeyValueSetSymbol("SUPC_WUIR_WKUPT" + str(id), supcSym_WUIR_WKUPEN[id])
            supcSym_WUIR_WKUPT[id].setLabel("Select Wakeup Edge")
            supcSym_WUIR_WKUPT[id].addKey("LOW", "0", "Falling Edge")
            supcSym_WUIR_WKUPT[id].addKey("HIGH", "1", "Rising Edge")
            supcSym_WUIR_WKUPT[id].setOutputMode("Key")
            supcSym_WUIR_WKUPT[id].setDisplayMode("Description")
            supcSym_WUIR_WKUPT[id].setSelectedKey("LOW", 1)
            if signal[id] == False:
                supcSym_WUIR_WKUPT[id].setVisible(False)

        supcSym_WUIR_WKUPEN[0].setDependencies(disableWKUP0, ["SUPC_WUMR_LPDBCEN0"])
        supcSym_WUIR_WKUPEN[1].setDependencies(disableWKUP1, ["SUPC_WUMR_LPDBCEN1"])

    if supcBitField_MR_CDPSWITCH != None:
        supcDataRam = supcComponent.createBooleanSymbol("SUPC_CDPSWITCH", supcLPMenu)
        supcDataRam.setLabel("Power Cache Data Ram")
        supcDataRam.setDefaultValue(True)

    if supcBitField_MR_CTPSWITCH != None:
        supcTagRam = supcComponent.createBooleanSymbol("SUPC_CTPSWITCH", supcLPMenu)
        supcTagRam.setLabel("Power Cache Tag Ram")
        supcTagRam.setDefaultValue(True)

    if supcBitField_MR_PSWITCH1 != None:
        supcSRam1 = supcComponent.createBooleanSymbol("SUPC_PSWITCH1", supcLPMenu)
        supcSRam1.setLabel("SRAM1 Power Switch")
        supcSRam1.setDefaultValue(True)

    if supcBitField_MR_PSWITCH2 != None:
        supcSRam2 = supcComponent.createBooleanSymbol("SUPC_PSWITCH2", supcLPMenu)
        supcSRam2.setLabel("SRAM2 Power Switch")
        supcSRam2.setDefaultValue(True)

    if supcSym_PWMR.getValue():
        supcStartup = supcComponent.createBooleanSymbol("SUPC_STUPTIME", supcLPMenu)
        supcStartup.setLabel("Enable Fast Startup")

        for i in range(0, 7):
            supcSRam = supcComponent.createBooleanSymbol("SUPC_SRAM" + str(i), supcLPMenu)
            supcSRam.setLabel("Power SRAM Block" + str(i))
            supcSRam.setDefaultValue(True)

        supcUSBRAM = supcComponent.createBooleanSymbol("SUPC_DPRAMON", supcLPMenu)
        supcUSBRAM.setLabel("Enable USB Dual-port RAM")
        supcUSBRAM.setDefaultValue(True)

    if supcBitField_MR_CDPSWITCH == None and supcBitField_MR_CTPSWITCH == None and supcBitField_MR_PSWITCH1 == None and supcBitField_MR_PSWITCH2 == None:
        supcLPMenu.setVisible(False)

    # BOD configuration
    supcBODMenu = supcComponent.createMenuSymbol("BOD_MENU", None)
    supcBODMenu.setLabel("Configure Brownout Detector")

    supcSym_MR_BODDIS = supcComponent.createBooleanSymbol("SUPC_MR_BODDIS", supcBODMenu)
    supcSym_MR_BODDIS.setLabel("Enable Brownout detector")
    supcSym_MR_BODDIS.setDefaultValue(True)

    supcSym_MR_BODRSTEN = supcComponent.createBooleanSymbol("SUPC_MR_BODRSTEN", supcSym_MR_BODDIS)
    supcSym_MR_BODRSTEN.setLabel("Enable Brownout Detector Reset")
    supcSym_MR_BODRSTEN.setDefaultValue(True)
    supcSym_MR_BODRSTEN.setDependencies(disableBKUPRST, ["SUPC_MR_BODDIS"])

    if supcSym_WUMR.getValue():
        # Low-Power Debouncer configuration
        supcDBMenu = supcComponent.createMenuSymbol("DB_MENU", None)
        supcDBMenu.setLabel("Configure Low-Power Tamper Detection")

        supcSym_WUMR_LPDBC = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_LPDBC", supcDBMenu)
        supcSym_WUMR_LPDBC.setLabel("Minimum Pulse Width on WKUP0/WKUP1 pins")

        supcValGrp_WUMR_LPDBC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_WUMR__LPDBC"]')
        supcValGrp_WUMR_LPDBC_Values = supcValGrp_WUMR_LPDBC.getChildren()

        for index in range(len(supcValGrp_WUMR_LPDBC_Values)):
            supcValGrp_WUMR_LPDBC_Key_Name = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("name")
            supcValGrp_WUMR_LPDBC_Key_Value = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("value")
            supcValGrp_WUMR_LPDBC_Key_Description = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("caption")
            supcSym_WUMR_LPDBC.addKey(supcValGrp_WUMR_LPDBC_Key_Name, supcValGrp_WUMR_LPDBC_Key_Value, supcValGrp_WUMR_LPDBC_Key_Description)

        supcSym_WUMR_LPDBC.setOutputMode("Value")
        supcSym_WUMR_LPDBC.setDisplayMode("Description")
        supcSym_WUMR_LPDBC.setDefaultValue(0)

        supcSym_WUMR_LPDBCEN0 = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCEN0", supcDBMenu)
        supcSym_WUMR_LPDBCEN0.setLabel("Low-Power Debouncer Enable (WKUP0)")

        supcSym_WUMR_LPDBCEN1 = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCEN1", supcDBMenu)
        supcSym_WUMR_LPDBCEN1.setLabel("Low-Power Debouncer Enable (WKUP1)")

        supcSym_WUMR_LPDBCCLR = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCCLR", supcDBMenu)
        supcSym_WUMR_LPDBCCLR.setLabel("Clear general-purpose backup register (GPBR) on tamper detection ")

    ############################################################################
    #### Dependency ####
    ############################################################################

    # Setup Peripheral Interrupt in Interrupt manager
    interruptVector = supcInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = supcInstanceName.getValue() + "_INTERRUPT_HANDLER"
    interruptHandlerLock = supcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = supcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    supcinterruptControl = supcComponent.createBooleanSymbol("NVIC_SUPC_ENABLE", None)
    supcinterruptControl.setDependencies(interruptControl, ["SUPC_SMMR_SMIEN"])
    supcinterruptControl.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcHeaderFile = supcComponent.createFileSymbol("SUPC_HEADER2", None)
    supcHeaderFile.setMarkup(True)
    supcHeaderFile.setSourcePath("../peripheral/supc_11228/templates/plib_supc.h.ftl")
    supcHeaderFile.setOutputName("plib_" + supcInstanceName.getValue().lower() + ".h")
    supcHeaderFile.setDestPath("/peripheral/supc/")
    supcHeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcHeaderFile.setType("HEADER")
    supcHeaderFile.setOverwrite(True)

    supcSourceFile = supcComponent.createFileSymbol("SUPC_SOURCE1", None)
    supcSourceFile.setMarkup(True)
    supcSourceFile.setSourcePath("../peripheral/supc_11228/templates/plib_supc.c.ftl")
    supcSourceFile.setOutputName("plib_" + supcInstanceName.getValue().lower() + ".c")
    supcSourceFile.setDestPath("/peripheral/supc/")
    supcSourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSourceFile.setType("SOURCE")
    supcSourceFile.setOverwrite(True)

    supcSystemInitFile = supcComponent.createFileSymbol("SUPC_INIT", None)
    supcSystemInitFile.setType("STRING")
    supcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSystemInitFile.setSourcePath("../peripheral/supc_11228/templates/system/initialization.c.ftl")
    supcSystemInitFile.setMarkup(True)

    supcSystemDefFile = supcComponent.createFileSymbol("SUPC_DEF", None)
    supcSystemDefFile.setType("STRING")
    supcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSystemDefFile.setSourcePath("../peripheral/supc_11228/templates/system/definitions.h.ftl")
    supcSystemDefFile.setMarkup(True)
