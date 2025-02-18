"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
#### Global Variables ####
################################################################################

global ccpTimerUnit
ccpTimerUnit = { "millisecond" : 1000.0,
                "microsecon" : 1000000.0,
                "nanosecond"  : 1000000000.0,
                }
global ccpInterruptVector
global ccpInterruptHandlerLock
global ccpInterruptHandler
global ccpInterruptVectorUpdate
global sysTimeComponentId
global ccpSym_PERIOD_MS
global moduleName
moduleName = "CCP"

################################################################################
#### Helper Functions ####
################################################################################
def getBitField(moduleName, registerGroup, register, bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

def getValueGroup(moduleName,valueGroupName):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/value-group@[name="'+ valueGroupName + '"]'
    return ATDF.getNode(atdfPath)

def setClockGeneratorData(moduleName, valueGroupName):
    clkNode = getValueGroup(moduleName,valueGroupName).getChildren()
    for bitfield in clkNode:
        if "Clock Generator" in bitfield.getAttribute("caption"):
            return bitfield.getAttribute("caption")

def isPic32aDspic33aPresent():
    return (Database.getSymbolValue("core", "CoreArchitecture") == "PIC32A" or
            Database.getSymbolValue("core", "CoreArchitecture") == "dsPIC33A")

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    return regName

def _get_bitfield_names(node, outputList):

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

def getIRQnumber(string):

    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

    for param in interruptsChildren:
        name = param.getAttribute("name")
        if string == name:
            irq_index = param.getAttribute("index")
            break

    return irq_index

def find_key_value(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.  This function is used with bitfield values for a given
    <value-group>, to set up default values for key value symbols.
    Arguments:
          value - the value to be looked for in the dictionary, a particular bitfield value to be found in 'keypairs'
          keypairs - the dictionary to be searched over, represents all bitfield values in a <value-group > to scanned over

    Without this helper function, setDefaultValue(<some_integer_value>) would not be very helpful for key/value symbols.
    Just inputting an integer value would require the user to see what order the bitfields are populated in the atdf file,
    to know what integer to use for setting a menu entry to a desired value.  This function removes the user requirement
    for figuring out what integer value should be used in order to get a particular bitfield value set by default.

    The (integer) value returned by this function call corresponds to the particular entry of the
    list that has the user-input key value.  The returned index value is dependent on the order
    of accumulation of bitfield entries from the atdf file.  This function removes that dependence by
    scanning the list (i.e., scans keypairs) for the particular key 'value' that matches what is being
    looked for, returning the element number for that (in the order it was scanned from the atdf file).

    The *.setDefaultValue( ) method that called this function will use that value to correctly populate
    the menu item.
    '''
    index = 0
    for ii in keypairs:
        if(ii["value"] == str(value)):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    Log.writeDebugMessage("find_key: could not find value in dictionary") # should never get here
    return ""

################################################################################
####  Business Logic  ####
################################################################################

def PreScaler_ValueUpdate(symbol, event):
    symbol.setValue(pow(4, event["value"]))

def autoShutdownVisibility(symbol, event):
    symObj = event["symbol"]
    val = symObj.getSelectedValue()
    if val == "0":
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def ccpExtClkVisible(symbol, event):
    symObj = event["symbol"]
    val = symObj.getSelectedValue()
    if val == "6" or val == "7" or val == "3":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def timerInterruptSet(symbol, event):
    if (event["id"] == "CCP_TIMER_INTERRUPT"):
        setTMRInterruptData(event["value"])

def captureCompareInterruptSet(symbol, event):
    global CaptureCompareIrq

    status = event["value"]
    if isPic32aDspic33aPresent():
        Database.setSymbolValue("core", "INTC_" + getIRQnumber(CaptureCompareIrq) + "_ENABLE", status)
        Database.setSymbolValue("core", "INTC_" + getIRQnumber(CaptureCompareIrq) + "_HANDLER_LOCK", status)
    else:
        Database.setSymbolValue("core", ccpCaptureCompareInterruptVector, status, 2)
        Database.setSymbolValue("core", ccpCaptureCompareInterruptHandlerLock, status, 2)
        interruptName = ccpCaptureCompareInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        if status == True:
            Database.setSymbolValue("core", ccpCaptureCompareInterruptHandler, interruptName + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", ccpCaptureCompareInterruptHandler, interruptName + "_Handler", 2)

def setTMRInterruptData(status):
    global tmrIrq

    if isPic32aDspic33aPresent():
        Database.setSymbolValue("core", "INTC_" + getIRQnumber(tmrIrq) + "_ENABLE", status)
        Database.setSymbolValue("core", "INTC_" + getIRQnumber(tmrIrq) + "_HANDLER_LOCK", status)
    else:
        Database.setSymbolValue("core", ccpInterruptVector, status, 2)
        Database.setSymbolValue("core", ccpInterruptHandlerLock, status, 2)
        interruptName = ccpInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        if status == True:
            Database.setSymbolValue("core", ccpInterruptHandler, interruptName + "_InterruptHandler", 2)
        else:
            Database.setSymbolValue("core", ccpInterruptHandler, interruptName + "_Handler", 2)

def updateTMRInterruptData(symbol, event):
    global tmrIrq

    if isPic32aDspic33aPresent():
        if ((ccpSym_TimerInterrupt.getValue() == True) and (Database.getSymbolValue("core", "INTC_" + getIRQnumber(tmrIrq) + "_ENABLE") == False)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        tmrInterruptVectorUpdate = tmrIrq + "_INTERRUPT_ENABLE_UPDATE"
        if ccpSym_TimerInterrupt.getValue() == True and Database.getSymbolValue("core", tmrInterruptVectorUpdate) == True:
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def updateCAPInterruptData(symbol, event):
    global CaptureCompareIrq

    component = symbol.getComponent()
    if isPic32aDspic33aPresent():
        if (((component.getSymbolValue("CCP_CAP_INTERRUPT") == True) and (event["source"].getSymbolByID("CCP_OPERATION_MODE").getValue() == "Capture") and (Database.getSymbolValue("core", "INTC_" + getIRQnumber(CaptureCompareIrq) + "_ENABLE") == False)) or
            ((component.getSymbolValue("CCP_COMP_INTERRUPT") == True) and (event["source"].getSymbolByID("CCP_OPERATION_MODE").getValue() == "Compare") and (Database.getSymbolValue("core", "INTC_" + getIRQnumber(CaptureCompareIrq) + "_ENABLE") == False))):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        capInterruptVectorUpdate = CaptureCompareIrq + "_INTERRUPT_ENABLE_UPDATE"
        if (component.getSymbolValue("CCP_CAP_INTERRUPT") == True or component.getSymbolValue("CCP_COMP_INTERRUPT") == True) and (Database.getSymbolValue("core", capInterruptVectorUpdate) == True):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def updateTMRClockWarningStatus(symbol, event):
    global clkGenEnableSym

    if isPic32aDspic33aPresent():
        src = int(symbol.getComponent().getSymbolValue("CCP_CCPCON1_CLKSEL"))
        if (src == 1) and (Database.getSymbolValue("core", clkGenEnableSym) == False):
            symbol.setLabel("Warning!!! (Clock input for " + ccpInstanceName.getValue() + ") Clock Generator" + clkGenEnableSym.replace("clkGen","").replace("Enable", "") + "is disabled in Clock Manager")
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        if "CLOCK_ENABLE" in event["id"]:
            symbol.setLabel("Warning!!! " + ccpInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
            symbol.setVisible(not event["value"])

def IECRegName(symbol, event):
    global tmrIrq
    tmrIrq_index = int(getIRQnumber(tmrIrq))
    enblRegName = _get_enblReg_parms(tmrIrq_index)
    symbol.setValue(enblRegName, 2)

def IFSRegName(symbol, event):
    global tmrIrq
    tmrIrq_index = int(getIRQnumber(tmrIrq))
    statRegName = _get_statReg_parms(tmrIrq_index)
    symbol.setValue(statRegName, 2)

def calcTimerFreq(symbol, event):
    global clkGenFreqSym

    component = symbol.getComponent()
    src = int(component.getSymbolValue("CCP_CCPCON1_CLKSEL"))
    prescale = component.getSymbolValue("CCP_PRESCALER_VALUE")
    if src < 3:
        if isPic32aDspic33aPresent():
            if src == 1:
                clock = int(Database.getSymbolValue("core", clkGenFreqSym)) / prescale
            else:
                clock = int(Database.getSymbolValue("core", "stdSpeedClkFreq")) / prescale
        else:
            clock = int(Database.getSymbolValue("core", ccpInstanceName.getValue() + "_CLOCK_FREQUENCY")) / prescale
        symbol.setValue(clock)
    else:
        clock = component.getSymbolValue("CCP_EXT_CLOCK_FREQ")/prescale
        symbol.setValue(clock)

def CCPCON1combineValues(symbol, event):
    ccpcon1 = symbol.getValue()
    component = symbol.getComponent()
    mode = ccpSym_OprationMode.getValue()
    t32 = int(component.getSymbolValue("CCP_CCPCON1_T32")) << 5
    prescale = int(ccpSym_CCPCON1_TMRPS.getSelectedValue()) << 6
    clk = int(ccpSym_CCPCON1_CLKSEL.getSelectedValue()) << 8
    sidl = int(component.getSymbolValue("CCP_CCPCON1_SIDL")) << 13
    sync = int(ccpSym_CCPCON1_SYNC.getSelectedValue()) << 16
    trig = int(component.getSymbolValue("CCP_CCPCON1_TRIGEN")) << 23
    ops = int(ccpSym_CCPCON1_OPS.getSelectedValue()) << 24
    oneshot = 0
    ccsel = 0

    if mode == "Timer":
        ccpMod = 0
        oneshot = int(component.getSymbolValue("CCP_CCPCON1_ONESHOT")) << 22
    elif mode == "Compare":
        ccpMod = int(ccpSym_Comp_CCPCON1_MOD.getSelectedValue())
    else: #capture mode
        ccsel = 1 << 4
        ccpMod = int(ccpSym_Cap_CCPCON1_MOD.getSelectedValue())
    ccpcon1 = ccpMod | ccsel | t32 | prescale | clk | sidl | sync | trig | ops | oneshot
    symbol.setValue(ccpcon1)


def CCPCON2combineValues(symbol, event):
    component = symbol.getComponent()
    ccpcon2 = 0
    mode = ccpSym_OprationMode.getValue()
    asdg = int(ccpSym_CCPCON2_ASDG.getSelectedValue()) << 0
    asdgm = int(ccpSym_CCPCON2_ASDGM.getSelectedValue()) << 14
    pwmrsen = int(ccpSym_CCPCON2_PWMRSEN.getSelectedValue()) << 15
    oca = ocb = occ = ocd = oce = ocf = oensync = ics = 0
    if mode == "Compare":
        oca = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCAEN")) << 24
        oensync = int(ccpSym_Comp_CCPCON2_OENSYNC.getSelectedValue()) << 31
        ics = int(ccpSym_Comp_CCPCON2_ICS.getSelectedValue()) << 16
        if mccpPresent.getValue() == True:
            ocb = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCBEN")) << 25
            occ = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCCEN")) << 26
            ocd = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCDEN")) << 27
            oce = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCEEN")) << 28
            ocf = int(component.getSymbolValue("CCP_COMP_CCPCON2_OCFEN")) << 29
    if mode == "Capture":
       ics = int(ccpSym_Cap_CCPCON2_ICS.getSelectedValue()) << 16
    ccpcon2 = (asdg) | (asdgm) | (pwmrsen) | (oca) | (ocb) | (occ) | (ocd) | (oce) | (ocf) | (oensync) | (ics)
    symbol.setValue(ccpcon2)

def CCPCON3combineValues(symbol, event):
    component = symbol.getComponent()
    ccpcon3 = 0
    mode = ccpSym_OprationMode.getValue()
    pssace = pssbdf = polace = polbdf = dt = outm = 0
    if mode == "Compare":
        pssace = int(ccpSym_CCPCON3_PSSACE.getSelectedValue()) << 18
        polace = int(ccpSym_Comp_CCPCON3_POLACE.getSelectedValue()) << 21
        if mccpPresent.getValue() == True:
            dt = component.getSymbolValue("CCP_COMP_CCPCON3_DT") << 0
            pssbdf = int(ccpSym_CCPCON3_PSSBDF.getSelectedValue()) << 16
            polbdf = int(ccpSym_Comp_CCPCON3_POLBDF.getSelectedValue()) << 20
            outm = int(ccpSym_Comp_CCPCON3_OUTM.getSelectedValue()) << 24
    ccpcon3 = (pssace) | (polace) | (dt) | (pssbdf) | (polbdf) | (outm)
    symbol.setValue(ccpcon3)

def ccpCaptureCompareInterruptByMode(symbol, event):
    component = symbol.getComponent()
    if event["value"] == "Timer":
        Database.setSymbolValue("core", ccpCaptureCompareInterruptVector, False, 2)
    elif event["value"] == "Compare":
        status = component.getSymbolValue("CCP_COMP_INTERRUPT")
        Database.setSymbolValue("core", ccpCaptureCompareInterruptVector, status, 2)
    elif event["value"] == "Capture":
        status = component.getSymbolValue("CCP_CAP_INTERRUPT")
        Database.setSymbolValue("core", ccpCaptureCompareInterruptVector, status, 2)

def ccpFileGen(symbol, event):
    component = symbol.getComponent()

    component.getSymbolByID("CCP_TIMER_HEADER").setEnabled(False)
    component.getSymbolByID("CCP_TIMER_SOURCE").setEnabled(False)
    component.getSymbolByID("CCP_COMPARE_HEADER").setEnabled(False)
    component.getSymbolByID("CCP_COMPARE_SOURCE").setEnabled(False)
    component.getSymbolByID("CCP_CAPTURE_HEADER").setEnabled(False)
    component.getSymbolByID("CCP_CAPTURE_SOURCE").setEnabled(False)

    if event["value"] == "Timer":
        component.getSymbolByID("CCP_TIMER_HEADER").setEnabled(True)
        component.getSymbolByID("CCP_TIMER_SOURCE").setEnabled(True)
    elif event["value"] == "Compare":
        component.getSymbolByID("CCP_COMPARE_HEADER").setEnabled(True)
        component.getSymbolByID("CCP_COMPARE_SOURCE").setEnabled(True)
    elif event["value"] == "Capture":
        component.getSymbolByID("CCP_CAPTURE_HEADER").setEnabled(True)
        component.getSymbolByID("CCP_CAPTURE_SOURCE").setEnabled(True)

def handleMessage(messageID, args):
    retDict = {}
    if (messageID == "CCP_CONFIG_HW_IO"):
        global ccpSym_OprationMode

        component = str(ccpInstanceName.getValue()).lower()
        opMode, outputPin, enable = args['config']

        if enable == True:
            res = ccpSym_OprationMode.setValue(opMode)
            symbol = "CCP_COMP_CCPCON2_OC{}EN".format(outputPin)
            res = Database.setSymbolValue(component, symbol, True)
        else:
            res = Database.clearSymbolValue(component, "CCP_OPERATION_MODE")

        if res == True:
            retDict = {"Result": "Success"}
        else:
            retDict = {"Result": "Fail"}

    return retDict

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(ccpComponent):

    global ccpInstanceName
    global ccpInterruptVector
    global ccpInterruptHandlerLock
    global ccpInterruptHandler
    global ccpInterruptVectorUpdate

    global ccpCaptureCompareInterruptVector
    global ccpCaptureCompareInterruptHandlerLock
    global ccpCaptureCompareInterruptHandler
    global ccpCaptureCompareInterruptVectorUpdate

    global ccpSymInterruptMode
    global instanceNum

    global ccpcon1_depList
    global ccpcon2_depList
    global ccpcon3_depList
    global tmrIrq
    global CaptureCompareIrq
    global clkGenFreqSym
    global clkGenEnableSym

    ccpcon1_depList = []
    ccpcon2_depList = []
    ccpcon3_depList = []

    ccpInstanceName = ccpComponent.createStringSymbol("CCP_INSTANCE_NAME", None)
    ccpInstanceName.setVisible(False)
    ccpInstanceName.setDefaultValue(ccpComponent.getID().upper())
    Log.writeInfoMessage("Running " + ccpInstanceName.getValue())

    ccpInstanceNum = ccpComponent.createStringSymbol("CCP_INSTANCE_NUM", None)
    ccpInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(ccpComponent.getID()))
    ccpInstanceNum.setDefaultValue(instanceNum)

    peripheralNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()
    for index in range(0, len(peripheralNode)):
        if peripheralNode[index].getAttribute("name").upper() == "CCP":
            moduleName = peripheralNode[index].getAttribute("name")
            break

    global mccpPresent
    mccpPresent = ccpComponent.createBooleanSymbol("CCP_MCCP_PRESENT", None)
    mccpPresent.setVisible(False)
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + moduleName + "\"]/instance@[name=\""+ccpInstanceName.getValue()+"\"]/parameters")
    mccp = "0"
    if node != None:
        param_values = []
        param_values = node.getChildren()
        for index in range(0, len(param_values)):
            if "MCCP_PRESENT" in param_values[index].getAttribute("name"):
                mccp = param_values[index].getAttribute("value")
    if mccp == "0":
        mccpPresent.setDefaultValue(False)
    else:
        mccpPresent.setDefaultValue(True)

    if isPic32aDspic33aPresent() == False:
        #Clock enable
        Database.setSymbolValue("core", ccpInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)
        defaultClkFreq = int(Database.getSymbolValue("core", ccpInstanceName.getValue() + "_CLOCK_FREQUENCY"))
        tmrIrq = "CCT" + ccpInstanceNum.getValue()
        CaptureCompareIrq = "CCP" + ccpInstanceNum.getValue()
    else:
        defaultClkFreq = int(Database.getSymbolValue("core", "stdSpeedClkFreq"))
        tmrIrq = "CCT" + ccpInstanceNum.getValue() + "Interrupt"
        CaptureCompareIrq = "CCP" + ccpInstanceNum.getValue() + "Interrupt"
        clockGenerator = setClockGeneratorData(moduleName, getValueGroupName(moduleName, "CCP", "CCP" + str(instanceNum) + "CON1", "CLKSEL"))
        clkGenFreqSym = "clkGen" + ''.join(filter(str.isdigit, str(clockGenerator))) + "OutFrequency"
        clkGenEnableSym = "clkGen" + ''.join(filter(str.isdigit, str(clockGenerator))) + "Enable"

    # SIDL
    ccpSym_CCPCON2_SIDL = ccpComponent.createBooleanSymbol("CCP_CCPCON1_SIDL", None)
    ccpSym_CCPCON2_SIDL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCPxCON1")
    ccpSym_CCPCON2_SIDL.setLabel("Enable Stop in Idle Mode")
    ccpcon1_depList.append("CCP_CCPCON1_SIDL")

    #clock source
    global ccpSym_CCPCON1_CLKSEL
    clock_names = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP" + str(instanceNum) + "CON1", "CLKSEL")), clock_names)
    ccpSym_CCPCON1_CLKSEL = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON1_CLKSEL", None)
    ccpSym_CCPCON1_CLKSEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_CCPCON1_CLKSEL.setLabel("Select Clock Source")
    ccpSym_CCPCON1_CLKSEL.setOutputMode("Value")
    ccpSym_CCPCON1_CLKSEL.setDisplayMode("Description")
    if int(clock_names[0]['value'], 0) != 0:
        clock_names.reverse()
    for ii in clock_names:
        ccpSym_CCPCON1_CLKSEL.addKey(ii['desc'], ii['value'], ii['key'])
    ccpSym_CCPCON1_CLKSEL.setDefaultValue(0)
    ccpcon1_depList.append("CCP_CCPCON1_CLKSEL")

    #External clock freq
    ccpSym_EXT_CLOCK_FREQ = ccpComponent.createIntegerSymbol("CCP_EXT_CLOCK_FREQ", ccpSym_CCPCON1_CLKSEL)
    ccpSym_EXT_CLOCK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_EXT_CLOCK_FREQ.setLabel("External Clock Frequency")
    ccpSym_EXT_CLOCK_FREQ.setVisible(False)
    ccpSym_EXT_CLOCK_FREQ.setDefaultValue(50000000)
    ccpSym_EXT_CLOCK_FREQ.setDependencies(ccpExtClkVisible, ["CCP_CCPCON1_CLKSEL"])

    #prescaler configuration
    global ccpSym_CCPCON1_TMRPS
    prescale_names = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP1CON1", "TMRPS")), prescale_names)
    ccpSym_CCPCON1_TMRPS = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON1_TMRPS", None)
    ccpSym_CCPCON1_TMRPS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1PR")
    ccpSym_CCPCON1_TMRPS.setLabel("Select Prescaler")
    ccpSym_CCPCON1_TMRPS.setOutputMode("Value")
    ccpSym_CCPCON1_TMRPS.setDisplayMode("Description")
    if int(prescale_names[0]['value'], 0) != 0:
        prescale_names.reverse()
    for ii in prescale_names:
        ccpSym_CCPCON1_TMRPS.addKey( ii['desc'], ii['value'], ii['key'] )
    ccpSym_CCPCON1_TMRPS.setDefaultValue(0)
    ccpcon1_depList.append("CCP_CCPCON1_TMRPS")

    #Prescaler Value
    ccpPrescalerValue = ccpComponent.createIntegerSymbol("CCP_PRESCALER_VALUE", None)
    ccpPrescalerValue.setVisible(False)
    ccpPrescalerValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1PR")
    ccpPrescalerValue.setLabel("Prescaler Value")
    ccpPrescalerValue.setDescription("Prescaler value")
    ccpPrescalerValue.setDefaultValue(1)
    ccpPrescalerValue.setMin(1)
    ccpPrescalerValue.setDependencies(PreScaler_ValueUpdate, ["CCP_CCPCON1_TMRPS"])

    ccpSym_CLOCK_FREQ = ccpComponent.createIntegerSymbol("CCP_CLOCK_FREQ", None)
    ccpSym_CLOCK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1PR")
    ccpSym_CLOCK_FREQ.setLabel("CCP Clock Frequency")
    ccpSym_CLOCK_FREQ.setReadOnly(True)
    ccpSym_CLOCK_FREQ.setDefaultValue(defaultClkFreq)
    if isPic32aDspic33aPresent():
        ccpSym_CLOCK_FREQ.setDependencies(calcTimerFreq, ["CCP_PRESCALER_VALUE",
        "CCP_CCPCON1_CLKSEL", "CCP_EXT_CLOCK_FREQ", "core.stdSpeedClkFreq", "core." + clkGenFreqSym])
    else:
        ccpSym_CLOCK_FREQ.setDependencies(calcTimerFreq, ["core." + ccpInstanceName.getValue() + "_CLOCK_FREQUENCY","CCP_PRESCALER_VALUE",
        "CCP_CCPCON1_CLKSEL", "CCP_EXT_CLOCK_FREQ"])

     #32 bit timer mode selection bits
    ccpSym_CCPCON1_T32 = ccpComponent.createBooleanSymbol("CCP_CCPCON1_T32", None)
    ccpSym_CCPCON1_T32.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1PR")
    ccpSym_CCPCON1_T32.setLabel("Enable 32 bit mode")
    ccpcon1_depList.append("CCP_CCPCON1_T32")

    # ASDG, Timer Gated Time Accumulation Enable bit
    global ccpSym_CCPCON2_ASDG
    tgate_names = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP" + str(instanceNum) + "CON2", "ASDG")), tgate_names)
    ccpSym_CCPCON2_ASDG = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON2_ASDG", None)
    ccpSym_CCPCON2_ASDG.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON2")
    ccpSym_CCPCON2_ASDG.setLabel("Select Auto Shutdown Source")
    ccpSym_CCPCON2_ASDG.setOutputMode( "Value" )
    ccpSym_CCPCON2_ASDG.setDisplayMode( "Description" )
    if isPic32aDspic33aPresent():
        ccpSym_CCPCON2_ASDG.addKey("disabled" , str(int("0x0",0)), "disabled")
        ccpSym_CCPCON2_ASDG.addKey("Comparator 1 Output" , str(int("0x1",0)), "Comparator 1 Output")
        ccpSym_CCPCON2_ASDG.addKey("Comparator 2 Output" , str(int("0x2",0)), "Comparator 2 Output")
        ccpSym_CCPCON2_ASDG.addKey("OCFC" , str(int("0x4",0)), "OCFC")
        ccpSym_CCPCON2_ASDG.addKey("OCFD" , str(int("0x8",0)), "OCFD")
        ccpSym_CCPCON2_ASDG.addKey("ICMn" , str(int("0x10",0)), "ICMn")
        ccpSym_CCPCON2_ASDG.addKey("CLC1" , str(int("0x20",0)), "CLC1")
        ccpSym_CCPCON2_ASDG.addKey("OCFA" , str(int("0x40",0)), "OCFA")
        ccpSym_CCPCON2_ASDG.addKey("OCFB" , str(int("0x80",0)), "OCFB")
    else:
        for ii in tgate_names:
            ccpSym_CCPCON2_ASDG.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON2_ASDG.setDefaultValue(0)  # gated time accumulation disabled
    ccpSym_CCPCON2_ASDG.setVisible(True)
    ccpcon2_depList.append("CCP_CCPCON2_ASDG")

    #Auto shutdown configuration
    global ccpSym_CCPCON2_ASDGM
    asdgm_names = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP1CON2", "ASDGM")), asdgm_names)
    ccpSym_CCPCON2_ASDGM = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON2_ASDGM", ccpSym_CCPCON2_ASDG)
    ccpSym_CCPCON2_ASDGM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON2")
    ccpSym_CCPCON2_ASDGM.setLabel("Select Auto Shutdown Gate Mode")
    ccpSym_CCPCON2_ASDGM.setVisible(False if ccpSym_CCPCON2_ASDG.getSelectedValue() == "0" else True)
    ccpSym_CCPCON2_ASDGM.setOutputMode( "Value" )
    ccpSym_CCPCON2_ASDGM.setDisplayMode( "Description" )
    if int(asdgm_names[0]['value'], 0) != 0:
        asdgm_names.reverse()
    for ii in asdgm_names:
        ccpSym_CCPCON2_ASDGM.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON2_ASDGM.setDependencies(autoShutdownVisibility, ["CCP_CCPCON2_ASDG"])
    ccpcon2_depList.append("CCP_CCPCON2_ASDGM")

    global ccpSym_CCPCON3_PSSACE
    shutdown_state = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP1CON3", "PSSACE")), shutdown_state)
    ccpSym_CCPCON3_PSSACE = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON3_PSSACE", ccpSym_CCPCON2_ASDG)
    ccpSym_CCPCON3_PSSACE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON2")
    ccpSym_CCPCON3_PSSACE.setLabel("Output pins (A, C, E) Shutdown State")
    ccpSym_CCPCON3_PSSACE.setVisible(False if ccpSym_CCPCON2_ASDG.getSelectedValue() == "0" else True)
    ccpSym_CCPCON3_PSSACE.setOutputMode( "Value" )
    ccpSym_CCPCON3_PSSACE.setDisplayMode( "Description" )
    if int(shutdown_state[0]['value'], 0) != 0:
        shutdown_state.reverse()
    for ii in shutdown_state:
        ccpSym_CCPCON3_PSSACE.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON3_PSSACE.setDependencies(autoShutdownVisibility, ["CCP_CCPCON2_ASDG"])
    ccpcon3_depList.append("CCP_CCPCON3_PSSACE")

    if mccpPresent.getValue() == True:
        global ccpSym_CCPCON3_PSSBDF
        ccpSym_CCPCON3_PSSBDF = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON3_PSSBDF", ccpSym_CCPCON2_ASDG)
        ccpSym_CCPCON3_PSSBDF.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON2")
        ccpSym_CCPCON3_PSSBDF.setLabel("Output pins (B, D, F) Shutdown State")
        ccpSym_CCPCON3_PSSBDF.setVisible(False if ccpSym_CCPCON2_ASDG.getSelectedValue() == "0" else True)
        ccpSym_CCPCON3_PSSBDF.setOutputMode( "Value" )
        ccpSym_CCPCON3_PSSBDF.setDisplayMode( "Description" )
        for ii in shutdown_state:
            ccpSym_CCPCON3_PSSBDF.addKey( ii['key'],ii['value'], ii['desc'] )
        ccpSym_CCPCON3_PSSBDF.setDependencies(autoShutdownVisibility, ["CCP_CCPCON2_ASDG"])
        ccpcon3_depList.append("CCP_CCPCON3_PSSBDF")

    #Auto restart enable
    global ccpSym_CCPCON2_PWMRSEN
    ccpSym_CCPCON2_PWMRSEN = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON2_PWMRSEN", ccpSym_CCPCON2_ASDG)
    ccpSym_CCPCON2_PWMRSEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON2")
    ccpSym_CCPCON2_PWMRSEN.setLabel("Select PWM Restart Option")
    restart_source = []
    valGrpName = getValueGroupName(moduleName, "CCP", "CCP1CON2", "PWMRSEN")
    if valGrpName == None:
        valGrpName = "CCP1CON2__PWMRSEN"
    _get_bitfield_names(getValueGroup(moduleName, valGrpName), restart_source)
    ccpSym_CCPCON2_PWMRSEN.setOutputMode( "Value" )
    ccpSym_CCPCON2_PWMRSEN.setDisplayMode( "Description" )
    if int(restart_source[0]['value'], 0) != 0:
        restart_source.reverse()
    for ii in restart_source:
        ccpSym_CCPCON2_PWMRSEN.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON2_PWMRSEN.setDefaultValue(0)
    ccpSym_CCPCON2_PWMRSEN.setVisible(False if ccpSym_CCPCON2_ASDG.getSelectedValue() == "0" else True)
    ccpSym_CCPCON2_PWMRSEN.setDependencies(autoShutdownVisibility, ["CCP_CCPCON2_ASDG"])
    ccpcon2_depList.append("CCP_CCPCON2_PWMRSEN")

    ccpSym_CCPCON1_TRIGEN = ccpComponent.createBooleanSymbol("CCP_CCPCON1_TRIGEN", None)
    ccpSym_CCPCON1_TRIGEN.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_CCPCON1_TRIGEN.setLabel("Enable Trigger Operation")
    ccpcon1_depList.append("CCP_CCPCON1_TRIGEN")

    # SYNC source
    global ccpSym_CCPCON1_SYNC
    sync_names = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP1CON1", "SYNC")), sync_names)
    ccpSym_CCPCON1_SYNC = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON1_SYNC", None)
    ccpSym_CCPCON1_SYNC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_CCPCON1_SYNC.setLabel("Select Trigger/Synchronization Source")
    ccpSym_CCPCON1_SYNC.setOutputMode( "Value" )
    ccpSym_CCPCON1_SYNC.setDisplayMode( "Description" )
    if int(sync_names[0]['value'], 0) != 0:
        sync_names.reverse()
    for ii in sync_names:
        ccpSym_CCPCON1_SYNC.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON1_SYNC.setDefaultValue(find_key_value(0,sync_names))
    ccpSym_CCPCON1_SYNC.setVisible(True)
    ccpcon1_depList.append("CCP_CCPCON1_SYNC")

    #Timer interrupt
    global ccpSym_TimerInterrupt
    ccpSym_TimerInterrupt = ccpComponent.createBooleanSymbol("CCP_TIMER_INTERRUPT", None)
    ccpSym_TimerInterrupt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_TimerInterrupt.setLabel("Enable Timer Interrupt")
    ccpSym_TimerInterrupt.setDefaultValue(True)

    #interrupt postscale
    global ccpSym_CCPCON1_OPS
    postscale = []
    _get_bitfield_names(getValueGroup(moduleName, getValueGroupName(moduleName, "CCP", "CCP1CON1", "OPS")), postscale)
    ccpSym_CCPCON1_OPS = ccpComponent.createKeyValueSetSymbol("CCP_CCPCON1_OPS", None)
    ccpSym_CCPCON1_OPS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_CCPCON1_OPS.setLabel("Select Interrupt Output Postscale")
    ccpSym_CCPCON1_OPS.setOutputMode( "Value" )
    ccpSym_CCPCON1_OPS.setDisplayMode( "Description" )
    if int(postscale[0]['value'], 0) != 0:
        postscale.reverse()
    for ii in postscale:
        ccpSym_CCPCON1_OPS.addKey( ii['key'],ii['value'], ii['desc'] )
    ccpSym_CCPCON1_OPS.setDefaultValue(0)
    ccpSym_CCPCON1_OPS.setVisible(True)
    ccpcon1_depList.append("CCP_CCPCON1_OPS")

    global ccpSym_OprationMode
    operationMode = ["Timer", "Compare", "Capture"]
    ccpSym_OprationMode = ccpComponent.createComboSymbol("CCP_OPERATION_MODE", None, operationMode)
    ccpSym_OprationMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ccp_01512;register:CCP1CON1")
    ccpSym_OprationMode.setLabel("Operating Mode")
    ccpSym_OprationMode.setDefaultValue("Timer")
    ccpcon1_depList.append("CCP_OPERATION_MODE")
    ccpcon2_depList.append("CCP_OPERATION_MODE")
    ccpcon3_depList.append("CCP_OPERATION_MODE")

    execfile(Variables.get("__CORE_DIR") + "/../peripheral/ccp_01512/config/ccp_timer.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/ccp_01512/config/ccp_compare.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/ccp_01512/config/ccp_capture.py")

    #CCPCON1 Reg Value
    ccpSym_CCPCON1_Value = ccpComponent.createHexSymbol("CCPCON1_REG_VALUE",None)
    ccpSym_CCPCON1_Value.setDefaultValue(0)
    ccpSym_CCPCON1_Value.setVisible(False)
    ccpSym_CCPCON1_Value.setDependencies(CCPCON1combineValues, ccpcon1_depList)

    #CCPCON2 Reg Value
    ccpSym_CCPCON2_Value = ccpComponent.createHexSymbol("CCPCON2_REG_VALUE",None)
    ccpSym_CCPCON2_Value.setDefaultValue(0)
    ccpSym_CCPCON2_Value.setVisible(False)
    ccpSym_CCPCON2_Value.setDependencies(CCPCON2combineValues, ccpcon2_depList)

    #CCPCON3 Reg Value
    ccpSym_CCPCON3_Value = ccpComponent.createHexSymbol("CCPCON3_REG_VALUE",None)
    ccpSym_CCPCON3_Value.setDefaultValue(0)
    ccpSym_CCPCON3_Value.setVisible(False)
    ccpSym_CCPCON3_Value.setDependencies(CCPCON3combineValues, ccpcon3_depList)

    #file generation
    ccpSym_FileGen = ccpComponent.createIntegerSymbol("CCP_FILE_GEN", None)
    ccpSym_FileGen.setVisible(False)
    ccpSym_FileGen.setDependencies(ccpFileGen, ["CCP_OPERATION_MODE"])

    ccpSym_CapInterruptMode = ccpComponent.createIntegerSymbol("CCP_CAPINTERRUPT_MODE", None)
    ccpSym_CapInterruptMode.setVisible(False)
    ccpSym_CapInterruptMode.setDependencies(ccpCaptureCompareInterruptByMode, ["CCP_OPERATION_MODE"])
    ############################################################################
    #### Dependency ####
    ############################################################################
    #Calculate the proper interrupt registers using CCP Timer IRQ#
    ccpIrq = "CCT" + str(instanceNum)
    ccpInterruptVector = ccpIrq + "_INTERRUPT_ENABLE"
    ccpInterruptHandler = ccpIrq + "_INTERRUPT_HANDLER"
    ccpInterruptHandlerLock = ccpIrq + "_INTERRUPT_HANDLER_LOCK"
    ccpInterruptVectorUpdate = ccpIrq + "_INTERRUPT_ENABLE_UPDATE"
    ccpIrq_index = int(getIRQnumber(tmrIrq))

    ccpSym_irq = ccpComponent.createStringSymbol("CCP_TIMER_IRQ", None)
    ccpSym_irq.setVisible(False)
    ccpSym_irq.setDependencies(timerInterruptSet, ["CCP_TIMER_INTERRUPT"])

    enblRegName = _get_enblReg_parms(ccpIrq_index)
    statRegName = _get_statReg_parms(ccpIrq_index)

    #IEC REG
    ccpIEC = ccpComponent.createStringSymbol("CCP_IEC_REG", None)
    ccpIEC.setDefaultValue(enblRegName)
    ccpIEC.setVisible(False)

    #IFS REG
    ccpIFS = ccpComponent.createStringSymbol("CCP_IFS_REG", None)
    ccpIFS.setDefaultValue(statRegName)
    ccpIFS.setVisible(False)

    ## Interrupt Dynamic settings
    setTMRInterruptData(ccpSym_TimerInterrupt.getValue())

    ccpSymIntEnComment = ccpComponent.createCommentSymbol("CCP_INTRRUPT_ENABLE_COMMENT", None)
    ccpSymIntEnComment.setLabel("Warning!!! " + ccpInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    ccpSymIntEnComment.setVisible(False)
    ccpSymIntEnComment.setDependencies(updateTMRInterruptData, ["CCP_TIMER_INTERRUPT", "core." + ccpInterruptVectorUpdate, "core.INTC_" + getIRQnumber(tmrIrq) + "_ENABLE"])

    #Calculate the proper interrupt registers using CCP Capture IRQ#
    ccpCaptureCompareIrq = "CCP" + str(instanceNum)
    ccpCaptureCompareInterruptVector = ccpCaptureCompareIrq + "_INTERRUPT_ENABLE"
    ccpCaptureCompareInterruptHandler = ccpCaptureCompareIrq + "_INTERRUPT_HANDLER"
    ccpCaptureCompareInterruptHandlerLock = ccpCaptureCompareIrq + "_INTERRUPT_HANDLER_LOCK"
    ccpCaptureCompareInterruptVectorUpdate = ccpCaptureCompareIrq + "_INTERRUPT_ENABLE_UPDATE"
    ccpCaptureCompareIrq_index = int(getIRQnumber(CaptureCompareIrq))

    ccpSym_capture_irq = ccpComponent.createStringSymbol("CCP_CAPTURE_COMPARE_IRQ", None)
    ccpSym_capture_irq.setVisible(False)
    ccpSym_capture_irq.setDependencies(captureCompareInterruptSet, ["CCP_CAP_INTERRUPT", "CCP_COMP_INTERRUPT"])

    enblRegName = _get_enblReg_parms(ccpCaptureCompareIrq_index)
    statRegName = _get_statReg_parms(ccpCaptureCompareIrq_index)

    #IEC REG
    ccpCaptureCompareIEC = ccpComponent.createStringSymbol("CCP_CAP_COMP_IEC_REG", None)
    ccpCaptureCompareIEC.setDefaultValue(enblRegName)
    ccpCaptureCompareIEC.setVisible(False)

    #IFS REG
    ccpCaptureCompareIFS = ccpComponent.createStringSymbol("CCP_CAP_COMP_IFS_REG", None)
    ccpCaptureCompareIFS.setDefaultValue(statRegName)
    ccpCaptureCompareIFS.setVisible(False)

    ccpSymIntEnComment = ccpComponent.createCommentSymbol("CCP_CAP_COMP_INTRRUPT_ENABLE_COMMENT", ccpSym_CaptureMenu)
    ccpSymIntEnComment.setLabel("Warning!!! " + ccpInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    ccpSymIntEnComment.setVisible(False)
    ccpSymIntEnComment.setDependencies(updateCAPInterruptData, ["CCP_CAP_INTERRUPT", "CCP_COMP_INTERRUPT", "core." + ccpCaptureCompareInterruptVectorUpdate, "core.INTC_" + getIRQnumber(CaptureCompareIrq) + "_ENABLE"])


    # Clock Warning status
    ccpSym_ClkEnComment = ccpComponent.createCommentSymbol("CCP_CLOCK_ENABLE_COMMENT", None)
    ccpSym_ClkEnComment.setVisible(False)
    ccpSym_ClkEnComment.setLabel("Warning!!! " + ccpInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    if isPic32aDspic33aPresent():
        ccpSym_ClkEnComment.setDependencies(updateTMRClockWarningStatus, ["CCP_CCPCON1_CLKSEL", "core." + clkGenEnableSym])
    else:
        ccpSym_ClkEnComment.setDependencies(updateTMRClockWarningStatus, ["core." + ccpInstanceName.getValue() + "_CLOCK_ENABLE", "CCP_CCPCON1_CLKSEL"])

    irqEnumName_Sym = ccpComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue(str(ccpIrq_index))
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    ccpHeaderFile = ccpComponent.createFileSymbol("CCP_COMMON_HEADER", None)
    ccpHeaderFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_common.h")
    ccpHeaderFile.setOutputName("plib_ccp_common.h")
    ccpHeaderFile.setDestPath("peripheral/ccp/")
    ccpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpHeaderFile.setType("HEADER")
    ccpHeaderFile.setMarkup(False)
    ccpHeaderFile.setOverwrite(True)

    # Instance Header File
    ccpHeaderFile = ccpComponent.createFileSymbol("CCP_TIMER_HEADER", None)
    ccpHeaderFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_timer.h.ftl")
    ccpHeaderFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".h")
    ccpHeaderFile.setDestPath("/peripheral/ccp/")
    ccpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpHeaderFile.setType("HEADER")
    ccpHeaderFile.setMarkup(True)
    ccpHeaderFile.setOverwrite(True)

    # Instance Source File
    ccpSourceFile = ccpComponent.createFileSymbol("CCP_TIMER_SOURCE", None)
    ccpSourceFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_timer.c.ftl")
    ccpSourceFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".c")
    ccpSourceFile.setDestPath("/peripheral/ccp/")
    ccpSourceFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpSourceFile.setType("SOURCE")
    ccpSourceFile.setMarkup(True)
    ccpSourceFile.setOverwrite(True)

    # Instance Header File
    ccpHeaderFile = ccpComponent.createFileSymbol("CCP_COMPARE_HEADER", None)
    ccpHeaderFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_compare.h.ftl")
    ccpHeaderFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".h")
    ccpHeaderFile.setDestPath("/peripheral/ccp/")
    ccpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpHeaderFile.setType("HEADER")
    ccpHeaderFile.setMarkup(True)
    ccpHeaderFile.setOverwrite(True)

    # Instance Source File
    ccpSourceFile = ccpComponent.createFileSymbol("CCP_COMPARE_SOURCE", None)
    ccpSourceFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_compare.c.ftl")
    ccpSourceFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".c")
    ccpSourceFile.setDestPath("/peripheral/ccp/")
    ccpSourceFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpSourceFile.setType("SOURCE")
    ccpSourceFile.setMarkup(True)
    ccpSourceFile.setOverwrite(True)

    # Instance Header File
    ccpHeaderFile = ccpComponent.createFileSymbol("CCP_CAPTURE_HEADER", None)
    ccpHeaderFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_capture.h.ftl")
    ccpHeaderFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".h")
    ccpHeaderFile.setDestPath("/peripheral/ccp/")
    ccpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpHeaderFile.setType("HEADER")
    ccpHeaderFile.setMarkup(True)
    ccpHeaderFile.setOverwrite(True)

    # Instance Source File
    ccpSourceFile = ccpComponent.createFileSymbol("CCP_CAPTURE_SOURCE", None)
    ccpSourceFile.setSourcePath("../peripheral/ccp_01512/templates/plib_ccp_capture.c.ftl")
    ccpSourceFile.setOutputName("plib_" + ccpInstanceName.getValue().lower() + ".c")
    ccpSourceFile.setDestPath("/peripheral/ccp/")
    ccpSourceFile.setProjectPath("config/" + configName + "/peripheral/ccp/")
    ccpSourceFile.setType("SOURCE")
    ccpSourceFile.setMarkup(True)
    ccpSourceFile.setOverwrite(True)

    ccpSym_SystemInitFile = ccpComponent.createFileSymbol("CCP_SYS_INT", None)
    ccpSym_SystemInitFile.setType("STRING")
    ccpSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ccpSym_SystemInitFile.setSourcePath("../peripheral/ccp_01512/templates/system/initialization.c.ftl")
    ccpSym_SystemInitFile.setMarkup(True)

    ccpSym_SystemDefFile = ccpComponent.createFileSymbol("CCP_SYS_DEF", None)
    ccpSym_SystemDefFile.setType("STRING")
    ccpSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ccpSym_SystemDefFile.setSourcePath("../peripheral/ccp_01512/templates/system/definitions.h.ftl")
    ccpSym_SystemDefFile.setMarkup(True)
