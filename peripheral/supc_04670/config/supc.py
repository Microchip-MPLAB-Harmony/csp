# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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
supcSym_WUMR_LPDBC = []
supcSym_WUMR_LPDBCEN = []
supcSym_IER_LPDBC = []

sclk = [1, 3, 32, 512, 4096, 32768]
vdd3v3SMTH = ["1.6 V", "1.72 V", "1.84 V", "1.96 V", "2.08 V", "2.2 V", "2.32 V", "2.44 V", "2.56 V", "2.68 V", "2.8 V", "2.92 V", "3.04 V", "3.16 V", "3.28 V", "3.4 V"]

################################################################################
#### Business Logic ####
################################################################################

def interruptControl(symbol, event):
    if ((Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_VDD3V3SMEV") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_VBATSMEV") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_LPDBC0") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_LPDBC1") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_LPDBC2") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_LPDBC3") == True) or
        (Database.getSymbolValue(supcInstanceName.getValue().lower(), "SUPC_IER_LPDBC4") == True)):
        Database.setSymbolValue("core", interruptVector, True)
        Database.setSymbolValue("core", interruptHandler, supcInstanceName.getValue() +  "_InterruptHandler")
        Database.setSymbolValue("core", interruptHandlerLock, True)
    else:
        Database.setSymbolValue("core", interruptVector, False)
        Database.setSymbolValue("core", interruptHandler, supcInstanceName.getValue() +  "_Handler")
        Database.setSymbolValue("core", interruptHandlerLock, False)

def disableWKUP(symbol, event):
    if event["value"] == True:
        symbol.setValue(False)

def calcPulseWidth(symbol, event):
    i = event["symbol"].getSelectedValue()
    numSlck = sclk[int(i, 16)]
    time = float(numSlck) / 32768
    timeUsInt = int(time * 1e6)
    timeMs = float(timeUsInt) / 1000
    wkupPrefix = "Minimum"
    if event["id"] == "SUPC_WUMR_FWUPDBC":
        wkupPrefix = "Force"
    symbol.setLabel(wkupPrefix + " WKUPx Pulse Width: " + str(timeMs) + " ms ( " + str(numSlck) + " SLCK Cycles )")

def disableBKUPRST(symbol, event):
    if event["value"] == False:
        symbol.setValue(False)

################################################################################
#### Component ####
################################################################################

if __name__ == "__main__":

    # global interruptVector
    # global interruptHandler
    # global interruptHandlerLock
    # global supcInstanceName

    supcComponent = coreComponent

    supcInstanceName = supcComponent.createStringSymbol("SUPC_INSTANCE_NAME", None)
    supcInstanceName.setVisible(False)
    supcInstanceName.setDefaultValue("SUPC")

    cpu_id =  Database.getSymbolValue("core", "CPU_CORE_ID")
    if cpu_id is None or cpu_id == 0:

        supcMenu = supcComponent.createMenuSymbol("SUPC_MENU", None)
        supcMenu.setLabel("Supply Controller (SUPC)")

        # SM configuration
        supcSMMenu = supcComponent.createMenuSymbol("SM_ENABLE", supcMenu)
        supcSMMenu.setLabel("Supply Monitor")

        supcSym_SMMR_VDD3V3SMTH = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_VDD3V3SMTH", supcSMMenu)
        supcSym_SMMR_VDD3V3SMTH.setLabel("VDD3V3 Supply Monitor Threshold")
        for index in range(len(vdd3v3SMTH)):
            supcSym_SMMR_VDD3V3SMTH.addKey(vdd3v3SMTH[index], str(index), vdd3v3SMTH[index])
        supcSym_SMMR_VDD3V3SMTH.setOutputMode("Value")
        supcSym_SMMR_VDD3V3SMTH.setDisplayMode("Description")
        supcSym_SMMR_VDD3V3SMTH.setSelectedKey(vdd3v3SMTH[len(vdd3v3SMTH) - 1])

        supcSym_SMMR_VDD3V3SMSMPL = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_VDD3V3SMSMPL", supcSMMenu)
        supcSym_SMMR_VDD3V3SMSMPL.setLabel("VDD3V3 Supply Monitor Sampling Period")
        supcValGrp_SMMR_VDD3V3SMSMPL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_SMMR__VDD3V3SMSMPL"]')
        supcValGrp_SMMR_VDD3V3SMSMPL_Values = supcValGrp_SMMR_VDD3V3SMSMPL.getChildren()
        for index in range(len(supcValGrp_SMMR_VDD3V3SMSMPL_Values)):
            supcValGrp_SMMR_VDD3V3SMSMPL_Key_Name = supcValGrp_SMMR_VDD3V3SMSMPL_Values[index].getAttribute("name")
            supcValGrp_SMMR_VDD3V3SMSMPL_Key_Value = supcValGrp_SMMR_VDD3V3SMSMPL_Values[index].getAttribute("value")
            supcValGrp_SMMR_VDD3V3SMSMPL_Key_Description = supcValGrp_SMMR_VDD3V3SMSMPL_Values[index].getAttribute("caption")
            supcSym_SMMR_VDD3V3SMSMPL.addKey(supcValGrp_SMMR_VDD3V3SMSMPL_Key_Name, supcValGrp_SMMR_VDD3V3SMSMPL_Key_Value, supcValGrp_SMMR_VDD3V3SMSMPL_Key_Description)
        supcSym_SMMR_VDD3V3SMSMPL.setOutputMode("Value")
        supcSym_SMMR_VDD3V3SMSMPL.setDisplayMode("Description")
        supcSym_SMMR_VDD3V3SMSMPL.setDefaultValue(0)

        supcSym_IER_VDD3V3SMEV = supcComponent.createBooleanSymbol("SUPC_IER_VDD3V3SMEV", supcSym_SMMR_VDD3V3SMSMPL)
        supcSym_IER_VDD3V3SMEV.setLabel("Enable VDD3V3 Supply Monitor Event Interrupt")

        supcSym_SMMR_VDD3V3SMPWRM = supcComponent.createKeyValueSetSymbol("SUPC_SMMR_VDD3V3SMPWRM", supcSMMenu)
        supcSym_SMMR_VDD3V3SMPWRM.setLabel("VDD3V3 Supply Monitor Power Supply Mode")
        supcValGrp_SMMR_VDD3V3SMPWRM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_SMMR__VDD3V3SMPWRM"]')
        supcValGrp_SMMR_VDD3V3SMPWRM_Values = supcValGrp_SMMR_VDD3V3SMPWRM.getChildren()
        for index in range(len(supcValGrp_SMMR_VDD3V3SMPWRM_Values)):
            supcValGrp_SMMR_VDD3V3SMPWRM_Key_Name = supcValGrp_SMMR_VDD3V3SMPWRM_Values[index].getAttribute("name")
            supcValGrp_SMMR_VDD3V3SMPWRM_Key_Value = supcValGrp_SMMR_VDD3V3SMPWRM_Values[index].getAttribute("value")
            supcValGrp_SMMR_VDD3V3SMPWRM_Key_Description = supcValGrp_SMMR_VDD3V3SMPWRM_Values[index].getAttribute("caption")
            supcSym_SMMR_VDD3V3SMPWRM.addKey(supcValGrp_SMMR_VDD3V3SMPWRM_Key_Name, supcValGrp_SMMR_VDD3V3SMPWRM_Key_Value, supcValGrp_SMMR_VDD3V3SMPWRM_Key_Description)
        supcSym_SMMR_VDD3V3SMPWRM.setOutputMode("Value")
        supcSym_SMMR_VDD3V3SMPWRM.setDisplayMode("Description")
        supcSym_SMMR_VDD3V3SMPWRM.setDefaultValue(0)

        supcSym_SMMR_VDD3V3SMRSTEN = supcComponent.createBooleanSymbol("SUPC_SMMR_VDD3V3SMRSTEN", supcSMMenu)
        supcSym_SMMR_VDD3V3SMRSTEN.setLabel("Enable VDD3V3 Supply Monitor Reset")

        supcSym_MR_IO_BACKUP_ISO = supcComponent.createBooleanSymbol("SUPC_MR_IO_BACKUP_ISO", supcMenu)
        supcSym_MR_IO_BACKUP_ISO.setLabel("Backup Domain IO Isolation Control")
        supcSym_MR_IO_BACKUP_ISO.setDefaultValue(True)

        supcSym_MR_CORSMDIS = supcComponent.createBooleanSymbol("SUPC_MR_CORSMDIS", supcMenu)
        supcSym_MR_CORSMDIS.setLabel("Disable VDDCORE Supply Monitor")

        supcSym_MR_CORSMRSTEN = supcComponent.createBooleanSymbol("SUPC_MR_CORSMRSTEN", supcMenu)
        supcSym_MR_CORSMRSTEN.setLabel("Enable VDDCORE Supply Monitor Reset")
        supcSym_MR_CORSMRSTEN.setDefaultValue(True)

        supcSym_MR_VREGDIS = supcComponent.createBooleanSymbol("SUPC_MR_VREGDIS", supcMenu)
        supcSym_MR_VREGDIS.setLabel("Disable Internal VDDCORE Voltage Regulator")

        supcSym_MR_CORSMM = supcComponent.createBooleanSymbol("SUPC_MR_CORSMM", supcMenu)
        supcSym_MR_CORSMM.setLabel("VDDCORE Supply Monitor Output Mode")

        supcSym_EMR_COREBGEN = supcComponent.createBooleanSymbol("SUPC_EMR_COREBGEN", supcMenu)
        supcSym_EMR_COREBGEN.setLabel("Enable VDDCORE Voltage Regulator Bandgap")

        supcSym_EMR_FULLGPBRC = supcComponent.createBooleanSymbol("SUPC_EMR_FULLGPBRC", supcMenu)
        supcSym_EMR_FULLGPBRC.setLabel("Full GPBR Clean")

        supcSym_EMR_FLRSGPBR = supcComponent.createBooleanSymbol("SUPC_EMR_FLRSGPBR", supcMenu)
        supcSym_EMR_FLRSGPBR.setLabel("Flash Erase GPBR")

        supcBMRMenu = supcComponent.createMenuSymbol("SUPC_BACKUP_MODE", supcMenu)
        supcBMRMenu.setLabel("Backup Mode Configuration")

        supcSym_BMR_RTTWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_RTTWKEN", supcBMRMenu)
        supcSym_BMR_RTTWKEN.setLabel("Enable Real-time Timer Wake-up")

        supcSym_BMR_RTCWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_RTCWKEN", supcBMRMenu)
        supcSym_BMR_RTCWKEN.setLabel("Enable Real-time Clock Wake-up")

        supcSym_BMR_VBATWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_VBATWKEN", supcBMRMenu)
        supcSym_BMR_VBATWKEN.setLabel("Enable VBAT Supply Monitor Wake-up")

        supcSym_BMR_FWUPEN = supcComponent.createBooleanSymbol("SUPC_BMR_FWUPEN", supcBMRMenu)
        supcSym_BMR_FWUPEN.setLabel("Enable Force Wake-up Pin Wake-up")

        supcSym_BMR_CORPORWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_CORPORWKEN", supcBMRMenu)
        supcSym_BMR_CORPORWKEN.setLabel("Enable VDDCORE POR Wake-up")

        supcSym_BMR_VDD3V3SMWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_VDD3V3SMWKEN", supcBMRMenu)
        supcSym_BMR_VDD3V3SMWKEN.setLabel("Enable VDD3V3 Supply Monitor Wake-up")

        supcSym_BMR_VBATREN = supcComponent.createBooleanSymbol("SUPC_BMR_VBATREN", supcBMRMenu)
        supcSym_BMR_VBATREN.setLabel("Enable Battery Voltage Event Report")

        supcSym_IER_VBATSMEV = supcComponent.createBooleanSymbol("SUPC_IER_VBATSMEV", supcSym_BMR_VBATREN)
        supcSym_IER_VBATSMEV.setLabel("Enable VBAT Supply Monitor Event Interrupt")

        supcSym_BMR_MRTCOUT = supcComponent.createBooleanSymbol("SUPC_BMR_MRTCOUT", supcBMRMenu)
        supcSym_BMR_MRTCOUT.setLabel("RTCOUT0 Outputs Drive Mode")

        supcSym_BMR_BADXTWKEN = supcComponent.createBooleanSymbol("SUPC_BMR_BADXTWKEN", supcBMRMenu)
        supcSym_BMR_BADXTWKEN.setLabel("Enable Slow Crystal Oscillator Frequency Error Wake-up")

        supcRegister_WUMR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_WUMR"]')
        supcSym_WUMR = supcComponent.createBooleanSymbol("SUPC_WUMR", supcMenu)
        supcSym_WUMR.setVisible(False)
        supcSym_WUMR.setDefaultValue(supcRegister_WUMR != None)

        supcBitField_CR_VROFF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_CR"]/bitfield@[name="VROFF"]')
        supcSym_CR_VROFF = supcComponent.createBooleanSymbol("SUPC_CR_VROFF", supcMenu)
        supcSym_CR_VROFF.setVisible(False)
        supcSym_CR_VROFF.setDefaultValue(supcBitField_CR_VROFF != None)

        supcLPMenu = supcComponent.createMenuSymbol("LOW_POWER_MENU", supcMenu)
        supcLPMenu.setLabel("Low Power Configuration")

        #Check wether wakeup support is there or not
        if supcSym_WUMR.getValue():
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

            supcSym_WUMR_FWUPDBC = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_FWUPDBC", supcWKUPMenu)
            supcSym_WUMR_FWUPDBC.setLabel("Force Pulse Width for Wakeup Input")

            supcValGrp_WUMR_FWUPDBC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_WUMR__FWUPDBC"]')
            supcValGrp_WUMR_FWUPDBC_Values = supcValGrp_WUMR_FWUPDBC.getChildren()

            for index in range(len(supcValGrp_WUMR_FWUPDBC_Values)):
                supcValGrp_WUMR_FWUPDBC_Key_Name = supcValGrp_WUMR_FWUPDBC_Values[index].getAttribute("name")
                supcValGrp_WUMR_FWUPDBC_Key_Value = supcValGrp_WUMR_FWUPDBC_Values[index].getAttribute("value")
                supcValGrp_WUMR_FWUPDBC_Key_Description = supcValGrp_WUMR_FWUPDBC_Values[index].getAttribute("caption")
                supcSym_WUMR_FWUPDBC.addKey(supcValGrp_WUMR_FWUPDBC_Key_Name, supcValGrp_WUMR_FWUPDBC_Key_Value, supcValGrp_WUMR_FWUPDBC_Key_Description)

            supcSym_WUMR_FWUPDBC.setOutputMode("Value")
            supcSym_WUMR_FWUPDBC.setDisplayMode("Description")
            supcSym_WUMR_FWUPDBC.setDefaultValue(0)

            supcSym_FORCE_PULSE_WIDTH_COMMENT = supcComponent.createCommentSymbol("FORCE_PULSE_WIDTH_COMMENT", supcWKUPMenu)
            supcSym_FORCE_PULSE_WIDTH_COMMENT.setLabel("Force WKUPx Pulse Width: 0.03 ms ( 1 SLCK Cycles )")
            supcSym_FORCE_PULSE_WIDTH_COMMENT.setDependencies(calcPulseWidth, ["SUPC_WUMR_FWUPDBC"])

            supcSym_WUIR = supcComponent.createHexSymbol("SUPC_WUIR", supcWKUPMenu)
            supcSym_WUIR.setVisible(False)

            supcSym_WKUP_Inputs = supcComponent.createIntegerSymbol("SUPC_WKUP_INPUTS", supcWKUPMenu)
            supcSym_WKUP_Inputs.setVisible(False)
            supcSym_WKUP_Inputs.setDefaultValue(15)

            #------------------------- ATDF Read -------------------------------------
            packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
            print("Package name is: " + packageName)
            availablePins = []        # array to save available pins
            signal = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] #array to save available signals

            children = []
            val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout@[name=\"" + str(packageName) + "\"]")
            children = val.getChildren()
            for pad in range (0, len(children)):
                availablePins.append(children[pad].getAttribute("pad"))

            wakeup_signals = []
            supc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"SUPC\"]/instance@[name=\"SUPC\"]/signals")
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

            supcSym_WUIR_WKUPEN[0].setDependencies(disableWKUP, ["SUPC_WUMR_LPDBCEN0"])
            supcSym_WUIR_WKUPEN[1].setDependencies(disableWKUP, ["SUPC_WUMR_LPDBCEN1"])
            supcSym_WUIR_WKUPEN[2].setDependencies(disableWKUP, ["SUPC_WUMR_LPDBCEN2"])
            supcSym_WUIR_WKUPEN[3].setDependencies(disableWKUP, ["SUPC_WUMR_LPDBCEN3"])
            supcSym_WUIR_WKUPEN[4].setDependencies(disableWKUP, ["SUPC_WUMR_LPDBCEN4"])

        if supcSym_WUMR.getValue():
            # Low-Power Debouncer configuration
            supcDBMenu = supcComponent.createMenuSymbol("DB_MENU", supcMenu)
            supcDBMenu.setLabel("Configure Low-Power Tamper Detection")

            for id in range (0, 5):
                supcSym_WUMR_LPDBC.append(id)
                supcSym_WUMR_LPDBC[id] = supcComponent.createKeyValueSetSymbol("SUPC_WUMR_LPDBC" + str(id), supcDBMenu)
                supcSym_WUMR_LPDBC[id].setLabel("Minimum Pulse Width on WKUP" + str(id) + " pin")
                supcValGrp_WUMR_LPDBC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/value-group@[name="SUPC_WUMR__LPDBC' + str(id) + '"]')
                supcValGrp_WUMR_LPDBC_Values = supcValGrp_WUMR_LPDBC.getChildren()
                for index in range(len(supcValGrp_WUMR_LPDBC_Values)):
                    supcValGrp_WUMR_LPDBC_Key_Name = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("name")
                    supcValGrp_WUMR_LPDBC_Key_Value = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("value")
                    supcValGrp_WUMR_LPDBC_Key_Description = supcValGrp_WUMR_LPDBC_Values[index].getAttribute("caption")
                    supcSym_WUMR_LPDBC[id].addKey(supcValGrp_WUMR_LPDBC_Key_Name, supcValGrp_WUMR_LPDBC_Key_Value, supcValGrp_WUMR_LPDBC_Key_Description)
                supcSym_WUMR_LPDBC[id].setOutputMode("Value")
                supcSym_WUMR_LPDBC[id].setDisplayMode("Description")
                supcSym_WUMR_LPDBC[id].setDefaultValue(0)

                supcSym_WUMR_LPDBCEN.append(id)
                supcSym_WUMR_LPDBCEN[id] = supcComponent.createBooleanSymbol("SUPC_WUMR_LPDBCEN" + str(id), supcDBMenu)
                supcSym_WUMR_LPDBCEN[id].setLabel("Enable Low-Power Debouncer WKUP" + str(id))

                supcSym_IER_LPDBC.append(id)
                supcSym_IER_LPDBC[id] = supcComponent.createBooleanSymbol("SUPC_IER_LPDBC" + str(id), supcDBMenu)
                supcSym_IER_LPDBC[id].setLabel("Enable WKUP" + str(id) + " Pin Tamper Detection Interrupt")

            ############################################################################
            #### Dependency ####
            ############################################################################

            # Setup Peripheral Interrupt in Interrupt manager
            interruptVector = supcInstanceName.getValue() + "_INTERRUPT_ENABLE"
            interruptHandler = supcInstanceName.getValue() + "_INTERRUPT_HANDLER"
            interruptHandlerLock = supcInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
            interruptVectorUpdate = supcInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

            # NVIC Dynamic settings
            supcinterruptControl = supcComponent.createBooleanSymbol("NVIC_SUPC_ENABLE", supcMenu)
            supcinterruptControl.setDependencies(interruptControl, ["SUPC_IER_VDD3V3SMEV", "SUPC_IER_VBATSMEV", "SUPC_IER_LPDBC0", "SUPC_IER_LPDBC1", "SUPC_IER_LPDBC2", "SUPC_IER_LPDBC3", "SUPC_IER_LPDBC4"])
            supcinterruptControl.setVisible(False)

    GPBR = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"GPBR\"]/register-group@[name=\"GPBR\"]/register@[name=\"SYS_GPBR\"]")
    GPBRRegNum = GPBR.getAttribute("count")

    gpbrSym_SYSGPBR = supcComponent.createIntegerSymbol("SYS_GPBR_REGISTER", supcMenu)
    gpbrSym_SYSGPBR.setVisible(False)
    gpbrSym_SYSGPBR.setDefaultValue(int(GPBRRegNum))

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    supcHeaderFile = supcComponent.createFileSymbol("SUPC_HEADER_H", None)
    supcHeaderFile.setMarkup(True)
    supcHeaderFile.setSourcePath("../peripheral/supc_04670/templates/plib_supc.h.ftl")
    supcHeaderFile.setOutputName("plib_" + supcInstanceName.getValue().lower() + ".h")
    supcHeaderFile.setDestPath("/peripheral/supc/")
    supcHeaderFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcHeaderFile.setType("HEADER")
    supcHeaderFile.setOverwrite(True)

    supcSourceFile = supcComponent.createFileSymbol("SUPC_SOURCE_C", None)
    supcSourceFile.setMarkup(True)
    supcSourceFile.setSourcePath("../peripheral/supc_04670/templates/plib_supc.c.ftl")
    supcSourceFile.setOutputName("plib_" + supcInstanceName.getValue().lower() + ".c")
    supcSourceFile.setDestPath("/peripheral/supc/")
    supcSourceFile.setProjectPath("config/" + configName + "/peripheral/supc/")
    supcSourceFile.setType("SOURCE")
    supcSourceFile.setOverwrite(True)

    supcSystemInitFile = supcComponent.createFileSymbol("SUPC_INIT", None)
    supcSystemInitFile.setType("STRING")
    supcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    supcSystemInitFile.setSourcePath("../peripheral/supc_04670/templates/system/initialization.c.ftl")
    supcSystemInitFile.setMarkup(True)

    supcSystemDefFile = supcComponent.createFileSymbol("SUPC_DEF", None)
    supcSystemDefFile.setType("STRING")
    supcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    supcSystemDefFile.setSourcePath("../peripheral/supc_04670/templates/system/definitions.h.ftl")
    supcSystemDefFile.setMarkup(True)
