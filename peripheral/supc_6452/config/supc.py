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

#------------------------------------------------------------------------------
#                     Global SUPC Array symbol declaration
#------------------------------------------------------------------------------
supcSym_WUIR_WKUPEN = []
supcSym_WUIR_WKUPT = []

################################################################################
#### Business Logic ####
################################################################################
#-------------------------------------------------------------------------------

def interruptControl(symbol, event):
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, supcInstanceName.getValue() +  "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "SUPC_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def disableWKUP0(symbol,event):
    if (event["value"] == True):
        symbol.clearValue()
        symbol.setValue(False, 1)

def disableWKUP1(symbol,event):
    if (event["value"] == True):
        symbol.clearValue()
        symbol.setValue(False, 1)

def enableSM(symbol,event):
    if (event["value"] == True):
        symbol.clearValue()
        symbol.setValue(True, 1)

sclk=[1,3,32,512,4096,32768]

def calcPulseWidth(symbol,event):
    symObj=event["symbol"]
    i=symObj.getSelectedValue()
    numSlck=sclk[int(i)]
    time= float(numSlck)/32768
    timeUsInt=int(time*1e6)
    timeMs=float(timeUsInt)/1000
    symbol.setLabel("Minimum WKUPx Pulse Width: " + str(timeMs) + " ms ( "+str(numSlck)+" SLCK Cycles )")

def disableBKUPRST(symbol,event):
    if (event["value"] == False):
        symbol.clearValue()
        symbol.setValue(False, 1)


################################################################################
#### Component ####
################################################################################
def instantiateComponent(supcComponent):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global supcInstanceName

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue(supcComponent.getID().upper())
    print("Running " + supcInstanceName.getValue())

    # SM configuration
    supcSMMenu= supcComponent.createBooleanSymbol("SM_ENABLE", None)
    supcSMMenu.setLabel("Enable Supply Monitor")
    supcSMMenu.setDependencies(enableSM,["SUPC_WUMR_SMEN"])

    supcSym_SMMR_SMTH = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_SMTH", supcSMMenu)
    supcSym_SMMR_SMTH.setLabel("Supply Monitor Threshold")
    supcSym_SMMR_SMTH.addKey("V1P6", "0", "1.6 V")
    supcSym_SMMR_SMTH.addKey("V1P72", "1", "1.72 V")
    supcSym_SMMR_SMTH.addKey("V1P84", "2", "1.84 V")
    supcSym_SMMR_SMTH.addKey("V1P96", "3", "1.96 V")
    supcSym_SMMR_SMTH.addKey("V2P08", "4", "2.08 V")
    supcSym_SMMR_SMTH.addKey("V2P2", "5", "2.2 V")
    supcSym_SMMR_SMTH.addKey("V2P32", "6", "2.32 V")
    supcSym_SMMR_SMTH.addKey("V2P44", "7", "2.44 V")
    supcSym_SMMR_SMTH.addKey("V2P56", "8", "2.56 V")
    supcSym_SMMR_SMTH.addKey("V2P68", "9", "2.68 V")
    supcSym_SMMR_SMTH.addKey("V2P8", "10", "2.8 V")
    supcSym_SMMR_SMTH.addKey("V2P92", "11", "2.92 V")
    supcSym_SMMR_SMTH.addKey("V3P04", "12", "3.04 V")
    supcSym_SMMR_SMTH.addKey("V3P16", "13", "3.16 V")
    supcSym_SMMR_SMTH.addKey("V3P28", "14", "3.28 V")
    supcSym_SMMR_SMTH.addKey("V3P4", "15", "3.4 V")
    supcSym_SMMR_SMTH.setOutputMode("Value")
    supcSym_SMMR_SMTH.setDisplayMode("Description")
    supcSym_SMMR_SMTH.setSelectedKey("V3P4",1)


    supcSym_SMMR_SMSMPL = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_SMSMPL", supcSMMenu)
    supcSym_SMMR_SMSMPL.setLabel("Supply Monitor Sampling Period")
    supcSym_SMMR_SMSMPL.addKey("_CSM", "1", "Monitor Continuously")
    supcSym_SMMR_SMSMPL.addKey("_32SLCK", "2", "Monitor 1 SLCK per 32 SLCK period")
    supcSym_SMMR_SMSMPL.addKey("_256SLCK", "3", "Monitor 1 SLCK per 256 SLCK period")
    supcSym_SMMR_SMSMPL.addKey("_2048SLCK", "4", "Monitor 1 SLCK per 2048 SLCK period")
    supcSym_SMMR_SMSMPL.setOutputMode("Key")
    supcSym_SMMR_SMSMPL.setDisplayMode("Description")
    supcSym_SMMR_SMSMPL.setSelectedKey("_CSM",1)

    supcSym_SMMR_SMIEN = supcComponent.createBooleanSymbol("SUPC_SMMR_SMIEN", supcSMMenu)
    supcSym_SMMR_SMIEN.setLabel("Enable Supply Monitor Interrupt")
    supcSym_SMMR_SMIEN.setDefaultValue(False)

    supcSym_SMMR_SMRSTEN = supcComponent.createBooleanSymbol("SUPC_SMMR_SMRSTEN", supcSMMenu)
    supcSym_SMMR_SMRSTEN.setLabel("Enable Supply Monitor Reset")
    supcSym_SMMR_SMRSTEN.setDefaultValue(False)


    # BKUP Configuration
    supcBKUPMenu = supcComponent.createMenuSymbol("BKUP_MENU", None)
    supcBKUPMenu.setLabel("Configure Backup Mode")

    supcSym_MR_BKUPRETON = supcComponent.createBooleanSymbol("SUPC_MR_BKUPRETON", supcBKUPMenu)
    supcSym_MR_BKUPRETON.setLabel("Retain Backup SRAM in Backup mode")
    supcSym_MR_BKUPRETON.setDefaultValue(True)

    supcSym_WUMR_RTCEN = supcComponent.createBooleanSymbol("SUPC_WUMR_RTCEN", supcBKUPMenu)
    supcSym_WUMR_RTCEN.setLabel("Enable RTC Alarm Wakeup")
    supcSym_WUMR_RTCEN.setDefaultValue(False)

    supcSym_WUMR_RTTEN = supcComponent.createBooleanSymbol("SUPC_WUMR_RTTEN", supcBKUPMenu)
    supcSym_WUMR_RTTEN.setLabel("Enable RTT Alarm Wakeup")
    supcSym_WUMR_RTTEN.setDefaultValue(False)

    supcSym_WUMR_SMEN = supcComponent.createBooleanSymbol("SUPC_WUMR_SMEN", supcBKUPMenu)
    supcSym_WUMR_SMEN.setLabel("Enable Supply Monitor Wakeup")
    supcSym_WUMR_SMEN.setDefaultValue(False)

    supcWKUPMenu = supcComponent.createMenuSymbol("WKUP_MENU", supcBKUPMenu)
    supcWKUPMenu.setLabel("Configure Wakeup Pins (WKUPx)")

    supcSym_WUMR_WKUPDBC = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_WKUPDBC", supcWKUPMenu)
    supcSym_WUMR_WKUPDBC.setLabel("Minimum Pulse Width for Wakeup Input")
    supcSym_WUMR_WKUPDBC.addKey("IMMEDIATE", "0", "1 SLCK Period")
    supcSym_WUMR_WKUPDBC.addKey("_3_SLCK", "1", "3 SLCK periods")
    supcSym_WUMR_WKUPDBC.addKey("_32_SLCK", "2", "32 SLCK periods")
    supcSym_WUMR_WKUPDBC.addKey("_512_SLCK", "3", "512 SLCK periods")
    supcSym_WUMR_WKUPDBC.addKey("_4096_SLCK", "4", "4096 SLCK periods")
    supcSym_WUMR_WKUPDBC.addKey("_32768_SLCK", "5", "32768 SLCK periods")
    supcSym_WUMR_WKUPDBC.setOutputMode("Value")
    supcSym_WUMR_WKUPDBC.setDisplayMode("Description")
    supcSym_WUMR_WKUPDBC.setSelectedKey("IMMEDIATE",1)

    supcSym_PULSE_WIDTH_COMMENT = supcComponent.createCommentSymbol("PULSE_WIDTH_COMMENT", supcWKUPMenu)
    supcSym_PULSE_WIDTH_COMMENT.setVisible(True)
    supcSym_PULSE_WIDTH_COMMENT.setLabel("Minimum WKUPx Pulse Width: 0.03 ms ( 1 SLCK Cycles )")
    supcSym_PULSE_WIDTH_COMMENT.setDependencies(calcPulseWidth, ["SUPC_WUMR_WKUPDBC"])

    supcSym_WUIR = supcComponent.createHexSymbol("SUPC_WUIR", supcWKUPMenu)
    supcSym_WUIR.setVisible(False)

    supcSym_WKUP_Inputs = supcComponent.createIntegerSymbol("SUPC_WKUP_INPUTS", supcWKUPMenu)
    supcSym_WKUP_Inputs.setVisible(False)
    supcSym_WKUP_Inputs.setDefaultValue(14)

    #------------------------- ATDF Read -------------------------------------
    GPBR = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPBR\"]/register-group@[name=\"GPBR\"]/register")
    GPBRRegNum = GPBR.getAttribute("count")

    gpbrSym_SYSGPBR = supcComponent.createIntegerSymbol("SYS_GPBR_REGISTER", None)
    gpbrSym_SYSGPBR.setVisible(False)
    gpbrSym_SYSGPBR.setDefaultValue(int(GPBRRegNum))

    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
    availablePins = []        # array to save available pins
    signal = [False, False, False, False, False, False, False, False, False, False, False, False, False, False] #array to save available signals

    children = []
    val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\""+str(packageName)+"\"]")
    children = val.getChildren()
    for pad in range (0, len(children)):
        availablePins.append(children[pad].getAttribute("pad"))

    wakeup_signals = []
    supc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SUPC\"]/instance@[name=\""+supcInstanceName.getValue()+"\"]/signals")
    wakeup_signals = supc.getChildren()
    for pad in range (0 , len(wakeup_signals)):
        if "index" in wakeup_signals[pad].getAttributeList():
            padSignal = wakeup_signals[pad].getAttribute("pad")
            if padSignal in availablePins :
                signal[int(wakeup_signals[pad].getAttribute("index"))] = True

    for id in range (0, len(signal)):
       supcSym_WUIR_WKUPEN.append(id)
       supcSym_WUIR_WKUPEN[id] = supcComponent.createBooleanSymbol("SUPC_WUIR_WKUPEN" + str(id), supcWKUPMenu)
       supcSym_WUIR_WKUPEN[id].setLabel("Enable WKUP"+ str(id) +" Input")
       supcSym_WUIR_WKUPEN[id].setDefaultValue(False)
       if(signal[id] == False):
           supcSym_WUIR_WKUPEN[id].setVisible(False)

       supcSym_WUIR_WKUPT.append(id)
       supcSym_WUIR_WKUPT[id] = supcComponent.createKeyValueSetSymbol("SUPC_WUIR_WKUPT" + str(id), supcSym_WUIR_WKUPEN[id])
       supcSym_WUIR_WKUPT[id].setLabel("Select Wakeup Edge")
       supcSym_WUIR_WKUPT[id].addKey("LOW", "0", "Falling Edge")
       supcSym_WUIR_WKUPT[id].addKey("HIGH", "1", "Rising Edge")
       supcSym_WUIR_WKUPT[id].setOutputMode("Key")
       supcSym_WUIR_WKUPT[id].setDisplayMode("Description")
       supcSym_WUIR_WKUPT[id].setSelectedKey("LOW",1)
       if(signal[id] == False):
           supcSym_WUIR_WKUPT[id].setVisible(False)


    supcSym_WUIR_WKUPEN[0].setDependencies(disableWKUP0,["SUPC_WUMR_LPDBCEN0"])
    supcSym_WUIR_WKUPEN[1].setDependencies(disableWKUP1,["SUPC_WUMR_LPDBCEN1"])

    # BOD configuration
    supcBODMenu = supcComponent.createMenuSymbol("BOD_MENU", None)
    supcBODMenu.setLabel("Configure Brownout Detector")

    supcSym_MR_BODDIS = supcComponent.createBooleanSymbol("SUPC_MR_BODDIS", supcBODMenu)
    supcSym_MR_BODDIS.setLabel("Enable Brownout detector")
    supcSym_MR_BODDIS.setDefaultValue(True)

    supcSym_MR_BODRSTEN = supcComponent.createBooleanSymbol("SUPC_MR_BODRSTEN", supcSym_MR_BODDIS)
    supcSym_MR_BODRSTEN.setLabel("Enable Brownout Detector Reset")
    supcSym_MR_BODRSTEN.setDefaultValue(True)
    supcSym_MR_BODRSTEN.setDependencies(disableBKUPRST,["SUPC_MR_BODDIS"])


    # Low-Power Debouncer configuration
    supcDBMenu = supcComponent.createMenuSymbol("DB_MENU", None)
    supcDBMenu.setLabel("Configure Low-Power Tamper Detection")

    supcSym_WUMR_LPDBC = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_LPDBC", supcDBMenu)
    supcSym_WUMR_LPDBC.setLabel("Minimum Pulse Width on WKUP0/WKUP1 pins")
    supcSym_WUMR_LPDBC.addKey("DISABLE", "0", "Disable")
    supcSym_WUMR_LPDBC.addKey("_2_RTCOUT", "1", "2 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_3_RTCOUT", "2", "3 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_4_RTCOUT", "3", "4 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_5_RTCOUT", "4", "5 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_6_RTCOUT", "5", "6 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_7_RTCOUT", "6", "7 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.addKey("_8_RTCOUT", "7", "8 RTCOUTx clock periods")
    supcSym_WUMR_LPDBC.setOutputMode("Value")
    supcSym_WUMR_LPDBC.setDisplayMode("Description")
    supcSym_WUMR_LPDBC.setSelectedKey("DISABLE",1)

    supcSym_WUMR_LPDBCEN0 = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCEN0", supcDBMenu)
    supcSym_WUMR_LPDBCEN0.setLabel("Low-Power Debouncer Enable (WKUP0)")
    supcSym_WUMR_LPDBCEN0.setDefaultValue(False)

    supcSym_WUMR_LPDBCEN1 = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCEN1", supcDBMenu)
    supcSym_WUMR_LPDBCEN1.setLabel("Low-Power Debouncer Enable (WKUP1)")
    supcSym_WUMR_LPDBCEN1.setDefaultValue(False)

    supcSym_WUMR_LPDBCCLR = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCCLR", supcDBMenu)
    supcSym_WUMR_LPDBCCLR.setLabel("Clear general-purpose backup register (GPBR) on tamper detection ")
    supcSym_WUMR_LPDBCCLR.setDefaultValue(False)


    ############################################################################
    #### Dependency ####
    ############################################################################

    # Setup Peripheral Interrupt in Interrupt manager
    interruptVector = supcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    interruptHandler = supcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = supcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = supcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    supcinterruptControl = supcComponent.createBooleanSymbol("NVIC_SUPC_ENABLE", None)
    supcinterruptControl.setDependencies(interruptControl, ["SUPC_SMMR_SMIEN"])
    supcinterruptControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    supcHeader1File = supcComponent.createFileSymbol("SUPC_HEADER1", None)
    supcHeader1File.setSourcePath("../peripheral/supc_6452/templates/plib_supc_common.h")
    supcHeader1File.setOutputName("plib_supc_common.h")
    supcHeader1File.setDestPath("/peripheral/supc/")
    supcHeader1File.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcHeader1File.setType("HEADER")
    supcHeader1File.setOverwrite(True)

    supcHeader2File = supcComponent.createFileSymbol("SUPC_HEADER2", None)
    supcHeader2File.setMarkup(True)
    supcHeader2File.setSourcePath("../peripheral/supc_6452/templates/plib_supc.h.ftl")
    supcHeader2File.setOutputName("plib_"+supcInstanceName.getValue().lower()+".h")
    supcHeader2File.setDestPath("/peripheral/supc/")
    supcHeader2File.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcHeader2File.setType("HEADER")
    supcHeader2File.setOverwrite(True)

    supcSource1File = supcComponent.createFileSymbol("SUPC_SOURCE1", None)
    supcSource1File.setMarkup(True)
    supcSource1File.setSourcePath("../peripheral/supc_6452/templates/plib_supc.c.ftl")
    supcSource1File.setOutputName("plib_"+supcInstanceName.getValue().lower()+".c")
    supcSource1File.setDestPath("/peripheral/supc/")
    supcSource1File.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSource1File.setType("SOURCE")
    supcSource1File.setOverwrite(True)

    supcSystemInitFile = supcComponent.createFileSymbol("SUPC_INIT", None)
    supcSystemInitFile.setType("STRING")
    supcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    supcSystemInitFile.setSourcePath("../peripheral/supc_6452/templates/system/system_initialize.c.ftl")
    supcSystemInitFile.setMarkup(True)

    supcSystemDefFile = supcComponent.createFileSymbol("SUPC_DEF", None)
    supcSystemDefFile.setType("STRING")
    supcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSystemDefFile.setSourcePath("../peripheral/supc_6452/templates/system/system_definitions.h.ftl")
    supcSystemDefFile.setMarkup(True)

