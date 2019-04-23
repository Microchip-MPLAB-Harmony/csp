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
#### Register Information ####
################################################################################

tmrBitField_T2CON_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="SIDL"]')
tmrValGrp_T2CON_SIDL = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__SIDL\"]")

tmrBitField_T2CON_ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="ON"]')
tmrValGrp_T2CON_ON = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__ON\"]")

tmrBitField_T2CON_SYNC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="SYNC"]')
tmrValGrp_T2CON_SYNC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__SYNC\"]")

tmrBitField_T2CON_TGATE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="TGATE"]')
tmrValGrp_T2CON_TGATE = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__TGATE\"]")

tmrBitField_T2CON_PRESCALER = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="TCKPS"]')
tmrValGrp_T2CON_PRESCALER = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__TCKPS\"]")

tmrBitField_T2CON_TCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="TCS"]')
tmrValGrp_T2CON_TCS = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__TCS\"]")

tmrBitField_T2CON_T32 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="T2CON"]/bitfield@[name="T32"]')
tmrValGrp_T2CON_T32 = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR\"]/value-group@[name=\"T2CON__T32\"]")

tmrBitField_PR2_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR"]/register-group@[name="TMR"]/register@[name="PR2"]')

################################################################################
#### Global Variables ####
################################################################################

global PrescalerDict
PrescalerDict = {
                    "1:256 prescale value": 256,
                    "1:64 prescale value" : 64,
                    "1:32 prescale value" : 32,
                    "1:16 prescale value" : 16,
                    "1:8 prescale value"  : 8,
                    "1:4 prescale value"  : 4,
                    "1:2 prescale value"  : 2,
                    "1:1 prescale value"  : 1,
                }
global tmrInterruptVector
global tmrInterruptHandlerLock
global tmrInterruptHandler
global tmrInterruptVectorUpdate
################################################################################
#### Business Logic ####
################################################################################
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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def timerInterruptSet(symbol, event):
    if (event["id"] == "TMR_INTERRUPT_MODE"):
        setTMRInterruptData(event["value"])

def setTMRInterruptData(status):
    Database.setSymbolValue("core", tmrInterruptVector, status, 2)
    Database.setSymbolValue("core", tmrInterruptHandlerLock, status, 2)
    interruptName = tmrInterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if status == True:
        Database.setSymbolValue("core", tmrInterruptHandler, interruptName + "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", tmrInterruptHandler, interruptName + "_Handler", 2)

def updateTMRInterruptData(symbol, event):
    component = symbol.getComponent()
    tmrIrq = "TIMER_" + str(instanceNum)
    tmrInterruptVectorUpdate = tmrIrq + "_INTERRUPT_ENABLE_UPDATE"
    if tmrSymInterruptMode.getValue() == True and Database.getSymbolValue("core", tmrInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def IECRegName(symbol, event):
    tmrIrq = "TIMER_" + str(int(instanceNum))
    tmrIrq_index = int(getIRQnumber(tmrIrq))
    enblRegName = _get_enblReg_parms(tmrIrq_index)
    symbol.setValue(enblRegName, 2)

def IFSRegName(symbol, event):
    tmrIrq = "TIMER_" + str(int(instanceNum))
    tmrIrq_index = int(getIRQnumber(tmrIrq))
    statRegName = _get_statReg_parms(tmrIrq_index)
    symbol.setValue(statRegName, 2)

def T2CONcombineValues(symbol, event):
    t2conValue = symbol.getValue()
    if event["id"] == "TIMER_SIDL":
        sidlValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_SIDL.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (sidlValue << 13)
    if event["id"] == "TIMER_SYNC":
        syncValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_SYNC.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (syncValue << 8)
    if event["id"] == "TIMER_TGATE":
        gateValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_TGATE.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (gateValue << 7)
    if event["id"] == "TIMER_PRE_SCALER":
        prescalerValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_PRESCALER.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (prescalerValue << 4)
    if event["id"] == "TIMER_32BIT_MODE_SEL":
        T32Value = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_T32.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (T32Value << 3)
    if event["id"] == "TIMER_SRC_SEL":
        tmrSrcSelValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmrBitField_T2CON_TCS.getAttribute("mask")
        t2conValue = t2conValue & (~int(maskvalue, 0))
        t2conValue = t2conValue | (tmrSrcSelValue << 1)
    symbol.setValue(t2conValue, 2)

def PreScaler_ValueUpdate(symbol, event):
    symbol.setValue(PrescalerDict[event["symbol"].getKey(event["value"])], 1)

def tmr1TsyncVisible(symbol, event):
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER_SRC_SEL")
    if (src == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def calcTimerFreq(symbol, event):
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER_SRC_SEL")
    if(src == 0):
        clock = component.getSymbolValue("TIMER_EXT_CLOCK_FREQ")
    else:
        clock = Database.getSymbolValue("core", tmrInstanceName.getValue() + "_CLOCK_FREQUENCY")
    prescaler = component.getSymbolValue("TMR_PRESCALER_VALUE")
    symbol.setValue(int(clock)/int(prescaler), 2)

def timerMaxValue(symbol, event):
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER_SRC_SEL")
    if(src == 0):
        clock = component.getSymbolValue("TIMER_EXT_CLOCK_FREQ")
    else:
        clock = Database.getSymbolValue("core", tmrInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if(clock == 0):
        clock = 1
    resolution = 1000.0 * component.getSymbolValue("TMR_PRESCALER_VALUE")/float(clock)
    mode_32 = component.getSymbolValue("TIMER_32BIT_MODE_SEL")
    if(mode_32 == 0):
        symbol.setMax(4294967295.0 * resolution)
    else:
        symbol.setMax(65535.0 * resolution)

def timerPeriodCalc(symbol, event):
    component = symbol.getComponent()
    clock = component.getSymbolValue("TIMER_CLOCK_FREQ")
    if(clock != 0):
        resolution = 1000.0/clock
        period = component.getSymbolValue("TIMER_TIME_PERIOD_MS") / resolution
        symbol.setValue(long(period), 2)
        mode_32 = component.getSymbolValue("TIMER_32BIT_MODE_SEL")
        if(mode_32 == 0):
            symbol.setMax(4294967295)
        else:
            symbol.setMax(65535)
    else:
        symbol.setValue(0, 2)

def tmrTgateVisible(symbol, event):
    symbol.setVisible(bool(event["value"]))

def updateTMRClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

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

    print("find_key: could not find value in dictionary") # should never get here
    return ""

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tmrComponent):

    global tmrInstanceName
    global tmrInterruptVector
    global tmrInterruptHandlerLock
    global tmrInterruptHandler
    global tmrInterruptVectorUpdate
    global tmrSymInterruptMode
    global instanceNum

    tmrInstanceName = tmrComponent.createStringSymbol("TMR_INSTANCE_NAME", None)
    tmrInstanceName.setVisible(False)
    tmrInstanceName.setDefaultValue(tmrComponent.getID().upper())
    Log.writeInfoMessage("Running " + tmrInstanceName.getValue())

    tmrInstanceNum = tmrComponent.createStringSymbol("TMR_INSTANCE_NUM", None)
    tmrInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(tmrComponent.getID()))
    tmrInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", tmrInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    tmrSymInterruptMode = tmrComponent.createBooleanSymbol("TMR_INTERRUPT_MODE", None)
    tmrSymInterruptMode.setLabel("Enable Interrrupts ?")
    tmrSymInterruptMode.setDefaultValue(True)

    #prescaler configuration
    prescale_names = []
    _get_bitfield_names(tmrValGrp_T2CON_PRESCALER, prescale_names)
    tmrSym_T2CON_PRESCALER = tmrComponent.createKeyValueSetSymbol("TIMER_PRE_SCALER", None)
    tmrSym_T2CON_PRESCALER.setLabel("Select Prescaler")
    tmrSym_T2CON_PRESCALER.setOutputMode("Value")
    tmrSym_T2CON_PRESCALER.setDisplayMode("Description")
    for ii in prescale_names:
        tmrSym_T2CON_PRESCALER.addKey( ii['desc'], ii['value'], ii['key'] )
    tmrSym_T2CON_PRESCALER.setDefaultValue(7)

    #Prescaler Value
    tmrPrescalerValue = tmrComponent.createIntegerSymbol("TMR_PRESCALER_VALUE", None)
    tmrPrescalerValue.setVisible(False)
    tmrPrescalerValue.setLabel("Prescaler Value")
    tmrPrescalerValue.setDescription("Timer Prescaler value")
    tmrPrescalerValue.setDefaultValue(1)
    tmrPrescalerValue.setMin(1)
    tmrPrescalerValue.setDependencies(PreScaler_ValueUpdate, ["TIMER_PRE_SCALER"])

     #32 bit timer mode selection bits
    t32_names = []
    _get_bitfield_names(tmrValGrp_T2CON_T32, t32_names)
    tmrSym_T2CON_32BIT_MODE_SEL = tmrComponent.createKeyValueSetSymbol("TIMER_32BIT_MODE_SEL", None)
    tmrSym_T2CON_32BIT_MODE_SEL.setLabel(tmrBitField_T2CON_T32.getAttribute("caption"))
    tmrSym_T2CON_32BIT_MODE_SEL.setOutputMode("Value")
    tmrSym_T2CON_32BIT_MODE_SEL.setDisplayMode("Description")
    for ii in t32_names:
        tmrSym_T2CON_32BIT_MODE_SEL.addKey( ii['desc'], ii['value'], ii['key'] )
    tmrSym_T2CON_32BIT_MODE_SEL.setDefaultValue(1)

    #Timer clock Source Slection configuration
    tcs_names = []
    _get_bitfield_names(tmrValGrp_T2CON_TCS, tcs_names)
    tmrSym_T2CON_SOURCE_SEL = tmrComponent.createKeyValueSetSymbol("TIMER_SRC_SEL", None)
    tmrSym_T2CON_SOURCE_SEL.setLabel("Select Timer Clock Source")
    tmrSym_T2CON_SOURCE_SEL.setOutputMode("Value")
    tmrSym_T2CON_SOURCE_SEL.setDisplayMode("Description")
    for ii in tcs_names:
        tmrSym_T2CON_SOURCE_SEL.addKey( ii['desc'], ii['value'], ii['key'] )
    tmrSym_T2CON_SOURCE_SEL.setDefaultValue(1)


    # TGATE, Timer Gated Time Accumulation Enable bit
    tgate_names = []
    _get_bitfield_names(tmrValGrp_T2CON_TGATE, tgate_names)
    tmrSym_T2CON_TGATE = tmrComponent.createKeyValueSetSymbol("TIMER_TGATE", tmrSym_T2CON_SOURCE_SEL)
    tmrSym_T2CON_TGATE.setLabel(tmrBitField_T2CON_TGATE.getAttribute("caption"))
    tmrSym_T2CON_TGATE.setOutputMode( "Value" )
    tmrSym_T2CON_TGATE.setDisplayMode( "Description" )
    for ii in tgate_names:
        tmrSym_T2CON_TGATE.addKey( ii['key'],ii['value'], ii['desc'] )
    tmrSym_T2CON_TGATE.setDefaultValue(find_key_value(0,tgate_names))  # gated time accumulation disabled
    tmrSym_T2CON_TGATE.setDependencies(tmrTgateVisible, ["TIMER_SRC_SEL"])
    tmrSym_T2CON_TGATE.setVisible(True)

    # SYNC, TMRx Synchronized Timer Start/Stop Enable bit
    sync_names = []
    _get_bitfield_names(tmrValGrp_T2CON_SYNC, sync_names)
    tmrSym_T2CON_SYNC = tmrComponent.createKeyValueSetSymbol("TIMER_SYNC", None)
    tmrSym_T2CON_SYNC.setLabel(tmrBitField_T2CON_SYNC.getAttribute("caption"))
    tmrSym_T2CON_SYNC.setOutputMode( "Value" )
    tmrSym_T2CON_SYNC.setDisplayMode( "Description" )
    for ii in sync_names:
        tmrSym_T2CON_SYNC.addKey( ii['key'],ii['value'], ii['desc'] )
    tmrSym_T2CON_SYNC.setDefaultValue(find_key_value(0,sync_names))
    tmrSym_T2CON_SYNC.setVisible(True)

    tmrSym_EXT_CLOCK_FREQ = tmrComponent.createIntegerSymbol("TIMER_EXT_CLOCK_FREQ", tmrSym_T2CON_SOURCE_SEL)
    tmrSym_EXT_CLOCK_FREQ.setLabel("External Clock Frequency")
    tmrSym_EXT_CLOCK_FREQ.setVisible(False)
    tmrSym_EXT_CLOCK_FREQ.setDefaultValue(50000000)
    tmrSym_EXT_CLOCK_FREQ.setDependencies(tmr1TsyncVisible, ["TIMER_SRC_SEL"])

    tmrSym_CLOCK_FREQ = tmrComponent.createIntegerSymbol("TIMER_CLOCK_FREQ", None)
    tmrSym_CLOCK_FREQ.setLabel("Timer1 Clock Frequency")
    tmrSym_CLOCK_FREQ.setReadOnly(True)
    tmrSym_CLOCK_FREQ.setDefaultValue(int(Database.getSymbolValue("core", tmrInstanceName.getValue() + "_CLOCK_FREQUENCY")))
    tmrSym_CLOCK_FREQ.setDependencies(calcTimerFreq, ["core." + tmrInstanceName.getValue() + "_CLOCK_FREQUENCY","TMR_PRESCALER_VALUE",
        "TIMER_SRC_SEL", "TIMER_EXT_CLOCK_FREQ"])

    clock = Database.getSymbolValue("core", tmrInstanceName.getValue() + "_CLOCK_FREQUENCY")
    if(clock != 0):
        resolution = 1000.0 * tmrPrescalerValue.getValue()/float(clock)
        max = (65535.0 * resolution)
    else:
        max = 0

    tmrSym_PERIOD_MS = tmrComponent.createFloatSymbol("TIMER_TIME_PERIOD_MS", None)
    tmrSym_PERIOD_MS.setLabel("Timer Period (Milli Sec)")
    tmrSym_PERIOD_MS.setDefaultValue(0.3)
    tmrSym_PERIOD_MS.setMin(0.0)
    tmrSym_PERIOD_MS.setMax(max)
    tmrSym_PERIOD_MS.setDependencies(timerMaxValue, ["core." + tmrInstanceName.getValue() + "_CLOCK_FREQUENCY", "TIMER_CLOCK_FREQ",
        "TIMER_32BIT_MODE_SEL"])

    if clock != 0:
        period = tmrSym_PERIOD_MS.getValue() / resolution
    else:
        period = 0

    #Timer1 Period Register
    tmrSym_PR2 = tmrComponent.createLongSymbol("TIMER_PERIOD", tmrSym_PERIOD_MS)
    tmrSym_PR2.setLabel("Period Register")
    tmrSym_PR2.setDefaultValue(long(period))
    tmrSym_PR2.setReadOnly(True)
    tmrSym_PR2.setMin(0)
    tmrSym_PR2.setMax(65535)
    tmrSym_PR2.setDependencies(timerPeriodCalc, ["core." + tmrInstanceName.getValue() + "_CLOCK_FREQUENCY", "TIMER_TIME_PERIOD_MS",
        "TIMER_CLOCK_FREQ", "TIMER_32BIT_MODE_SEL"])

    #timer SIDL configuration
    sidl_names = []
    _get_bitfield_names(tmrValGrp_T2CON_SIDL, sidl_names)
    tmrSymField_T2CON_SIDL = tmrComponent.createKeyValueSetSymbol("TIMER_SIDL", None)
    tmrSymField_T2CON_SIDL.setLabel(tmrBitField_T2CON_SIDL.getAttribute("caption"))
    tmrSymField_T2CON_SIDL.setOutputMode( "Value" )
    tmrSymField_T2CON_SIDL.setDisplayMode( "Description" )
    for ii in sidl_names:
        tmrSymField_T2CON_SIDL.addKey( ii['key'],ii['value'], ii['desc'] )
    tmrSymField_T2CON_SIDL.setDefaultValue(1)

    #Timer TxCON Reg Value
    tmrSym_T2CON_Value = tmrComponent.createHexSymbol("TCON_REG_VALUE",None)
    tmrSym_T2CON_Value.setDefaultValue((int(tmrSymField_T2CON_SIDL.getSelectedValue()) << 13) | (int(tmrSym_T2CON_SYNC.getSelectedValue()) << 8) \
    | (int (tmrSym_T2CON_TGATE.getSelectedValue()) << 7) | (int (tmrSym_T2CON_PRESCALER.getSelectedValue()) << 4) \
    | (int(tmrSym_T2CON_32BIT_MODE_SEL.getSelectedValue()) << 3) | (int(tmrSym_T2CON_SOURCE_SEL.getSelectedValue()) << 1))
    tmrSym_T2CON_Value.setVisible(False)
    tmrSym_T2CON_Value.setDependencies(T2CONcombineValues,["TIMER_SIDL", "TIMER_SYNC", "TIMER_TGATE", "TIMER_PRE_SCALER", "TIMER_32BIT_MODE_SEL", "TIMER_SRC_SEL"])

    ############################################################################
    #### Dependency ####
    ############################################################################
    #Calculate the proper interrupt registers using IRQ#
    tmrIrq = "TIMER_" + str(instanceNum)
    if (tmrSym_T2CON_32BIT_MODE_SEL.getValue() == 0):
        tmrIrq = "TIMER_" + str(int(instanceNum) + 1)

    tmrInterruptVector = tmrIrq + "_INTERRUPT_ENABLE"
    tmrInterruptHandler = tmrIrq + "_INTERRUPT_HANDLER"
    tmrInterruptHandlerLock = tmrIrq + "_INTERRUPT_HANDLER_LOCK"
    tmrInterruptVectorUpdate = tmrIrq + "_INTERRUPT_ENABLE_UPDATE"
    tmrIrq_index = int(getIRQnumber(tmrIrq))

    tmrSym_irq = tmrComponent.createStringSymbol("TIMER_IRQ", None)
    tmrSym_irq.setVisible(False)
    tmrSym_irq.setDependencies(timerInterruptSet, ["TMR_INTERRUPT_MODE"])

    enblRegName = _get_enblReg_parms(tmrIrq_index)
    statRegName = _get_statReg_parms(tmrIrq_index)

    #IEC REG
    tmrIEC = tmrComponent.createStringSymbol("TMR_IEC_REG", None)
    tmrIEC.setDefaultValue(enblRegName)
    tmrIEC.setVisible(False)

    #IFS REG
    tmrIFS = tmrComponent.createStringSymbol("TMR_IFS_REG", None)
    tmrIFS.setDefaultValue(statRegName)
    tmrIFS.setVisible(False)

    ## EVIC Interrupt Dynamic settings
    setTMRInterruptData(tmrSymInterruptMode.getValue())

    tmrSymIntEnComment = tmrComponent.createCommentSymbol("TMR_INTRRUPT_ENABLE_COMMENT", None)
    tmrSymIntEnComment.setLabel("Warning!!! " + tmrInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    tmrSymIntEnComment.setVisible(False)
    tmrSymIntEnComment.setDependencies(updateTMRInterruptData, ["TIMER_32BIT_MODE_SEL","TMR_INTERRUPT_MODE", "core." + tmrInterruptVectorUpdate])

    # Clock Warning status
    tmrSym_ClkEnComment = tmrComponent.createCommentSymbol("TMR_CLOCK_ENABLE_COMMENT", None)
    tmrSym_ClkEnComment.setLabel("Warning!!! " + tmrInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    tmrSym_ClkEnComment.setVisible(False)
    tmrSym_ClkEnComment.setDependencies(updateTMRClockWarningStatus, ["core." + tmrInstanceName.getValue() + "_CLOCK_ENABLE"])
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tmrHeaderFile = tmrComponent.createFileSymbol("TMR_COMMON_HEADER", None)
    tmrHeaderFile.setSourcePath("../peripheral/tmr_02815/templates/plib_tmr_common.h")
    tmrHeaderFile.setOutputName("plib_tmr_common.h")
    tmrHeaderFile.setDestPath("peripheral/tmr/")
    tmrHeaderFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrHeaderFile.setType("HEADER")
    tmrHeaderFile.setMarkup(False)
    tmrHeaderFile.setOverwrite(True)

    # Instance Header File
    tmrHeaderFile = tmrComponent.createFileSymbol("TMR_HEADER1", None)
    tmrHeaderFile.setSourcePath("../peripheral/tmr_02815/templates/plib_tmr.h.ftl")
    tmrHeaderFile.setOutputName("plib_" + tmrInstanceName.getValue().lower() + ".h")
    tmrHeaderFile.setDestPath("/peripheral/tmr/")
    tmrHeaderFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrHeaderFile.setType("HEADER")
    tmrHeaderFile.setMarkup(True)
    tmrHeaderFile.setOverwrite(True)

    # Instance Source File
    tmrSourceFile = tmrComponent.createFileSymbol("TMR_SOURCE", None)
    tmrSourceFile.setSourcePath("../peripheral/tmr_02815/templates/plib_tmr.c.ftl")
    tmrSourceFile.setOutputName("plib_" + tmrInstanceName.getValue().lower() + ".c")
    tmrSourceFile.setDestPath("/peripheral/tmr/")
    tmrSourceFile.setProjectPath("config/" + configName + "/peripheral/tmr/")
    tmrSourceFile.setType("SOURCE")
    tmrSourceFile.setMarkup(True)
    tmrSourceFile.setOverwrite(True)

    tmrSym_SystemInitFile = tmrComponent.createFileSymbol("TMR_SYS_INT", None)
    tmrSym_SystemInitFile.setType("STRING")
    tmrSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tmrSym_SystemInitFile.setSourcePath("../peripheral/tmr_02815/templates/system/initialization.c.ftl")
    tmrSym_SystemInitFile.setMarkup(True)

    tmrSym_SystemDefFile = tmrComponent.createFileSymbol("TMR_SYS_DEF", None)
    tmrSym_SystemDefFile.setType("STRING")
    tmrSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tmrSym_SystemDefFile.setSourcePath("../peripheral/tmr_02815/templates/system/definitions.h.ftl")
    tmrSym_SystemDefFile.setMarkup(True)
