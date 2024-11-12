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

tmr1BitField_T1CON_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="SIDL"]')
tmr1ValGrp_T1CON_SIDL = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__SIDL\"]")

tmr1BitField_T1CON_TWDIS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TWDIS"]')
tmr1ValGrp_T1CON_TWDIS = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TWDIS\"]")

tmr1BitField_T1CON_PRESCALER = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TCKPS"]')
tmr1ValGrp_T1CON_PRESCALER = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TCKPS\"]")

tmr1BitField_T1CON_TCS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TCS"]')
tmr1ValGrp_T1CON_TCS = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TCS\"]")

tmr1BitField_PR1_BITS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="PR1"]')

tmr1BitField_T1CON_TSYNC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TSYNC"]')
tmr1ValGrp_T1CON_TSYNC = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TSYNC\"]")

tmr1BitField_T1CON_TECS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TECS"]')
tmr1ValGrp_T1CON_TECS = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TECS\"]")

tmr1BitField_T1CON_TGATE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="TMR1"]/register-group@[name="TMR1"]/register@[name="T1CON"]/bitfield@[name="TGATE"]')
tmr1ValGrp_T1CON_TGATE = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TMR1\"]/value-group@[name=\"T1CON__TGATE\"]")

################################################################################
#### Global Variables ####
################################################################################

global PrescalerDict
PrescalerDict = {
                    "1:256 prescale value": 256,
                    "1:64 prescale value" : 64,
                    "1:8 prescale value"  : 8,
                    "1:1 prescale value"  : 1,
                }
global tmrTimerUnit
tmrTimerUnit = { "millisecond" : 1000.0,
                "microsecond" : 1000000.0,
                "nanosecond"  : 1000000000.0,
                }
global sysTimeComponentId
global dvrtComponentId
global i2cbbComponentId
global tmr1Sym_T1CON_SOURCE_SEL
global tmr1SymField_T1CON_TECS
global tmr1Sym_EXT_CLOCK_FREQ

global tmr1Sym_PERIOD_MS
global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################
def calcAchievableFreq():
    global tmr1Sym_PR1
    global tmr1Sym_CLOCK_FREQ
    tickRateDict = {"tick_rate_hz": 0}
    dummy_dict = dict()

    if sysTimeComponentId.getValue() != "":
        #Read the input clock frequency of the timer instance
        source_clk_freq = tmr1Sym_CLOCK_FREQ.getValue()
        #Read the calculated timer count to achieve the set Time Period and Calculate the actual tick rate
        achievableTickRateHz = float(1.0/source_clk_freq) * tmr1Sym_PR1.getValue()
        achievableTickRateHz = (1.0/achievableTickRateHz) * 100000.0
        tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
        dummy_dict = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

    elif (dvrtComponentId.getValue() != ""):
        timer_Frequency = tmr1Sym_CLOCK_FREQ.getValue()
        #Read the calculated timer count to achieve the set Time Period and Calculate the actual tick rate
        if timer_Frequency != 0:
            achievableTickRateHz = float(1.0/timer_Frequency) * (tmr1Sym_PR1.getValue())
            if achievableTickRateHz != 0:
                achievableTickRateHz = ((1.0/achievableTickRateHz) * 100000.0)
                tickRateDict["tick_rate_hz"] = long(achievableTickRateHz)
                dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
            else:
                dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)
        else:
            dummy_dict = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_ACHIEVABLE_TICK_RATE_HZ", tickRateDict)

def handleMessage(messageID, args):
    global sysTimeComponentId
    global dvrtComponentId
    global i2cbbComponentId
    global tmr1Sym_T1CON_SOURCE_SEL
    global tmr1SymField_T1CON_TECS
    global tmr1Sym_EXT_CLOCK_FREQ

    dummy_dict = dict()
    sysTimePLIBConfig = dict()
    dvrtPLIBConfig = dict()
    dvrt_tick_ms = {"dvrt_tick_ms" : 0.0}

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        modeDict = {"plib_mode": "PERIOD_MODE"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            tmr1Sym_PERIOD_MS.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        if sysTimeComponentId.getValue() != "":
            #Set the Time Period (millisecond)
            tmr1Sym_PERIOD_MS.setValue(args["sys_time_tick_ms"])

    if (messageID == "DVRT_PUBLISH_CAPABILITIES"):
        dvrtComponentId.setValue(args["ID"])
        opemode_Dict = {"plib_mode": "PERIOD_MODE"}
        dvrtPLIBConfig = Database.sendMessage(dvrtComponentId.getValue(), "DVRT_PLIB_CAPABILITY", opemode_Dict)
        if dvrtPLIBConfig["TIMER_MODE"] == "DVRT_PLIB_MODE_PERIOD":
            tmr1Sym_PERIOD_MS.setValue(dvrtPLIBConfig["dvrt_tick_millisec"])

    if (messageID == "DVRT_TICK_RATE_CHANGED"):
        if dvrtComponentId.getValue() != "":
            #Set the Time Period (Milli Sec)
            tmr1Sym_PERIOD_MS.setValue(args["dvrt_tick_ms"])
            
    if (messageID == "TIMER_FREQ_GET"):
        print("***Message Received***")
        i2cbbComponentId.setValue(args["ID"])
        src = tmr1Sym_T1CON_SOURCE_SEL.getValue()
        ext_src = tmr1SymField_T1CON_TECS.getValue()
        if(src == 0 and ext_src == 1):
            source_clk_freq = tmr1Sym_EXT_CLOCK_FREQ.getValue()
        else:
            source_clk_freq = Database.getSymbolValue("core", tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY")
        dummy_dict["TIMER_FREQ"] = source_clk_freq    

    return dummy_dict

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

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))
            if "irq-name" in param.getAttributeList():
                name = str(param.getAttribute("irq-name"))
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
########################################## Callbacks  #############################################
###################################################################################################

def setTMR1InterruptData(status):

    Database.setSymbolValue("core", tmr1InterruptVector, status, 1)
    Database.setSymbolValue("core", tmr1InterruptHandlerLock, status, 1)

    interruptName = tmr1InterruptHandler.split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", tmr1InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", tmr1InterruptHandler, interruptName + "_Handler", 1)

def updateTMR1InterruptData(symbol, event):

    if event["id"] == "TMR1_INTERRUPT_MODE":
        setTMR1InterruptData(event["value"])

    if tmr1SymInterruptMode.getValue() == True and Database.getSymbolValue("core", tmr1InterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def T1CONcombineValues(symbol, event):

    t1conValue = symbol.getValue()

    if event["id"] == "TIMER1_SIDL":
        sidlValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_SIDL.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (sidlValue << 13)

    if event["id"] == "TIMER1_TWDIS":
        twdisValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_TWDIS.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (twdisValue << 12)

    if event["id"] == "TIMER1_TECS":
        tecsValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_TECS.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (tecsValue << 8)

    if event["id"] == "TIMER1_TGATE":
        tgateValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_TGATE.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (tgateValue << 7)

    if event["id"] == "TIMER1_PRE_SCALER":
        prescalerValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_PRESCALER.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (prescalerValue << 4)

    if event["id"] == "TIMER1_TSYNC":
        tsyncValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_TSYNC.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (tsyncValue << 2)

    if event["id"] == "TIMER1_SRC_SEL":
        tmr1SrcSelValue = int(event["symbol"].getKeyValue(event["value"]))
        maskvalue = tmr1BitField_T1CON_TCS.getAttribute("mask")
        t1conValue = t1conValue & (~int(maskvalue, 0))
        t1conValue = t1conValue | (tmr1SrcSelValue << 1)

    symbol.setValue(t1conValue, 2)

def PreScaler_ValueUpdate(symbol, event):
    symbol.setValue(PrescalerDict[event["symbol"].getKey(event["value"])], 1)

def tmr1TsyncVisible(symbol, event):
    symbol.setVisible(not bool(event["value"]))

def tmr1AsyncExtClkVisible(symbol, event):
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER1_SRC_SEL")
    ext_src = component.getSymbolValue("TIMER1_TECS")
    if (src == 0 and ext_src == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def tmr1AsyncSetting(symbol, event):
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER1_SRC_SEL")
    sync = component.getSymbolValue("TIMER1_TSYNC")
    if (src == 0 and sync == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def calcTimerFreq(symbol, event):
    global i2cbbComponentId
    
    component = symbol.getComponent()
    src = component.getSymbolValue("TIMER1_SRC_SEL")
    ext_src = component.getSymbolValue("TIMER1_TECS")
    if(src == 0 and ext_src == 1):
        clock = component.getSymbolValue("TIMER1_EXT_CLOCK_FREQ")
    else:
        clock = Database.getSymbolValue("core", tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY")
    prescaler = component.getSymbolValue("TMR1_PRESCALER_VALUE")
    symbol.setValue(int(clock)/int(prescaler), 2)
    
    #Read the input clock frequency of the timer instance
    source_clk_freq = clock
    tmrFrequencyDict = {"ID" : "", "frequency" : ""}
    tmrFrequencyDict["ID"] = tmr1InstanceName.getValue()
    tmrFrequencyDict["frequency"] = source_clk_freq
    Database.sendMessage(i2cbbComponentId.getValue(), "TIMER_FREQUENCY", tmrFrequencyDict)    

def timerMaxValue(symbol, event):
    component = symbol.getComponent()
    clock = component.getSymbolValue("TIMER1_CLOCK_FREQ")
    unit = tmrTimerUnit[component.getSymbolValue("TIMER_UNIT")]
    if(clock != 0):
        resolution = unit/float(clock)
    else:
        resolution = 0
    symbol.setMax(65537.0 * resolution)

def timerPeriodCalc(symbol, event):
    component = symbol.getComponent()
    clock = component.getSymbolValue("TIMER1_CLOCK_FREQ")
    unit = tmrTimerUnit[component.getSymbolValue("TIMER_UNIT")]
    if(clock != 0):
        resolution = unit/(clock)
        period = (component.getSymbolValue("TIMER1_TIME_PERIOD_MS") / resolution) - 1
        symbol.setValue(long(period), 2)
    else:
        symbol.setValue(0, 2)
    calcAchievableFreq()

def tmr1TgateVisible(symbol, event):
    symbol.setVisible(bool(event["value"]))

def updateTMR1ClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

def onAttachmentConnected(source, target):
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

def onAttachmentDisconnected(source, target):
    global sysTimeComponentId
    global dvrtComponentId

    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()

    if remoteID == "sys_time":
        #Reset the remote component ID to NULL
        sysTimeComponentId.setValue("")
        tmr1Sym_PERIOD_MS.setValue(0.3)

    if remoteID == "dvrt":
        dvrtComponentId.setValue("")
        #Show Time Period and clear it
        tmr1Sym_PERIOD_MS.clearValue()
    
    if (remoteID == "i2c_bb"):
        i2cbbComponentId.setValue("")

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tmr1Component):

    global tmr1InstanceName
    global tmr1InterruptVector
    global tmr1InterruptHandlerLock
    global tmr1InterruptHandler
    global tmr1InterruptVectorUpdate
    global tmr1SymInterruptMode
    global tmr1Sym_T1CON_SOURCE_SEL
    global tmr1SymField_T1CON_TECS
    global tmr1Sym_EXT_CLOCK_FREQ
    global tcs_names
    global sysTimeComponentId
    global tmr1Sym_PERIOD_MS
    global tmr1Sym_CLOCK_FREQ
    global tmr1Sym_PR1
    global dvrtComponentId
    global i2cbbComponentId

    tmr1InstanceName = tmr1Component.createStringSymbol("TMR1_INSTANCE_NAME", None)
    tmr1InstanceName.setVisible(False)
    tmr1InstanceName.setDefaultValue(tmr1Component.getID().upper())
    Log.writeInfoMessage("Running " + tmr1InstanceName.getValue())

    tmr1InstanceNum = tmr1Component.createStringSymbol("TMR1_INSTANCE_NUM", None)
    tmr1InstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(tmr1Component.getID()))
    tmr1InstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", tmr1InstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    tmr1SymInterruptMode = tmr1Component.createBooleanSymbol("TMR1_INTERRUPT_MODE", None)
    tmr1SymInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1SymInterruptMode.setLabel("Enable Interrrupts ?")
    tmr1SymInterruptMode.setDefaultValue(True)

    #Calculate the proper interrupt registers using IRQ#
    tmr1Irq = "TIMER_" + str(instanceNum)
    tmr1InterruptVector = tmr1Irq + "_INTERRUPT_ENABLE"
    tmr1InterruptHandler = tmr1Irq + "_INTERRUPT_HANDLER"
    tmr1InterruptHandlerLock = tmr1Irq + "_INTERRUPT_HANDLER_LOCK"
    tmr1InterruptVectorUpdate = tmr1Irq + "_INTERRUPT_ENABLE_UPDATE"
    tmr1Irq_index = int(getIRQIndex(tmr1Irq))

    if tmr1Irq_index == -1:
        tmr1Irq_index = int(getVectorIndex(tmr1Irq))

    enblRegName = _get_enblReg_parms(tmr1Irq_index)
    statRegName = _get_statReg_parms(tmr1Irq_index)

    #IEC REG
    tmr1IEC = tmr1Component.createStringSymbol("TMR1_IEC_REG", None)
    tmr1IEC.setDefaultValue(enblRegName)
    tmr1IEC.setVisible(False)

    #IFS REG
    tmr1IFS = tmr1Component.createStringSymbol("TMR1_IFS_REG", None)
    tmr1IFS.setDefaultValue(statRegName)
    tmr1IFS.setVisible(False)

    #TCKPS, prescaler configuration
    prescale_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_PRESCALER, prescale_names)
    tmr1Sym_T1CON_PRESCALER = tmr1Component.createKeyValueSetSymbol("TIMER1_PRE_SCALER", None)
    tmr1Sym_T1CON_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_T1CON_PRESCALER.setLabel("Select Prescaler")
    tmr1Sym_T1CON_PRESCALER.setOutputMode("Value")
    tmr1Sym_T1CON_PRESCALER.setDisplayMode("Description")
    for ii in prescale_names:
        tmr1Sym_T1CON_PRESCALER.addKey( ii['desc'], ii['value'], ii['key'] )
    tmr1Sym_T1CON_PRESCALER.setDefaultValue(find_key_value(0,prescale_names))  # 1:1 prescale value
    tmr1Sym_T1CON_PRESCALER.setVisible(True)

    #Prescaler Value
    tmr1PrescalerValue = tmr1Component.createIntegerSymbol("TMR1_PRESCALER_VALUE", None)
    tmr1PrescalerValue.setVisible(False)
    tmr1PrescalerValue.setDefaultValue(1)
    tmr1PrescalerValue.setMin(1)
    tmr1PrescalerValue.setDependencies(PreScaler_ValueUpdate, ["TIMER1_PRE_SCALER"])

    #TCS, Timer1 clock Source Slection configuration
    tcs_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_TCS, tcs_names)
    tmr1Sym_T1CON_SOURCE_SEL = tmr1Component.createKeyValueSetSymbol("TIMER1_SRC_SEL", None)
    tmr1Sym_T1CON_SOURCE_SEL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_T1CON_SOURCE_SEL.setLabel("Select Timer Clock Source")
    tmr1Sym_T1CON_SOURCE_SEL.setOutputMode("Value")
    tmr1Sym_T1CON_SOURCE_SEL.setDisplayMode("Description")
    for ii in tcs_names:
        tmr1Sym_T1CON_SOURCE_SEL.addKey( ii['key'], ii['value'], ii['desc'] )
    tmr1Sym_T1CON_SOURCE_SEL.setDefaultValue(find_key_value(0,tcs_names))   # internal peripheral clock

    #timer TECS configuration
    tecs_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_TECS, tecs_names)
    tmr1SymField_T1CON_TECS = tmr1Component.createKeyValueSetSymbol("TIMER1_TECS", tmr1Sym_T1CON_SOURCE_SEL)
    tmr1SymField_T1CON_TECS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1SymField_T1CON_TECS.setLabel(tmr1BitField_T1CON_TECS.getAttribute("caption"))
    tmr1SymField_T1CON_TECS.setOutputMode( "Value" )
    tmr1SymField_T1CON_TECS.setDisplayMode( "Description" )
    tmr1SymField_T1CON_TECS.setVisible(False)
    for ii in tecs_names:
        tmr1SymField_T1CON_TECS.addKey( ii['key'],ii['value'], ii['desc'] )
    tmr1SymField_T1CON_TECS.setDefaultValue(find_key_value(1,tecs_names))  # external clock comes from T1CK
    tmr1SymField_T1CON_TECS.setDependencies(tmr1TsyncVisible, ["TIMER1_SRC_SEL"])

    tmr1Sym_EXT_CLOCK_FREQ = tmr1Component.createIntegerSymbol("TIMER1_EXT_CLOCK_FREQ", tmr1Sym_T1CON_SOURCE_SEL)
    tmr1Sym_EXT_CLOCK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_EXT_CLOCK_FREQ.setLabel("External Clock Frequency")
    tmr1Sym_EXT_CLOCK_FREQ.setVisible(False)
    tmr1Sym_EXT_CLOCK_FREQ.setDefaultValue(50000000)
    tmr1Sym_EXT_CLOCK_FREQ.setDependencies(tmr1AsyncExtClkVisible, ["TIMER1_SRC_SEL", "TIMER1_TECS"])

    #TSYNC, Timer1 External Clock Input Synchronization Selection
    tsync_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_TSYNC, tsync_names)
    tmr1Sym_T1CON_TSYNC = tmr1Component.createKeyValueSetSymbol("TIMER1_TSYNC", tmr1Sym_T1CON_SOURCE_SEL)
    tmr1Sym_T1CON_TSYNC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_T1CON_TSYNC.setLabel(tmr1BitField_T1CON_TSYNC.getAttribute("caption"))
    tmr1Sym_T1CON_TSYNC.setOutputMode("Value")
    tmr1Sym_T1CON_TSYNC.setDisplayMode("Description")
    for ii in tsync_names:
        tmr1Sym_T1CON_TSYNC.addKey( ii['desc'], ii['value'], ii['key'] )
    tmr1Sym_T1CON_TSYNC.setDefaultValue(find_key_value(0,tsync_names))   # internal peripheral clock
    tmr1Sym_T1CON_TSYNC.setVisible(False)
    tmr1Sym_T1CON_TSYNC.setDependencies(tmr1TsyncVisible, ["TIMER1_SRC_SEL"])

    #timer TWDIS configuration
    twdis_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_TWDIS, twdis_names)
    tmr1SymField_T1CON_TWDIS = tmr1Component.createKeyValueSetSymbol("TIMER1_TWDIS", tmr1Sym_T1CON_SOURCE_SEL)
    tmr1SymField_T1CON_TWDIS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1SymField_T1CON_TWDIS.setLabel(tmr1BitField_T1CON_TWDIS.getAttribute("caption"))
    tmr1SymField_T1CON_TWDIS.setVisible(False)
    tmr1SymField_T1CON_TWDIS.setOutputMode( "Value" )
    tmr1SymField_T1CON_TWDIS.setDisplayMode( "Description" )
    for ii in twdis_names:
        tmr1SymField_T1CON_TWDIS.addKey( ii['key'],ii['value'], ii['desc'] )
    tmr1SymField_T1CON_TWDIS.setDefaultValue(find_key_value(0,twdis_names))  # back-to-back writes enabled
    tmr1SymField_T1CON_TWDIS.setDependencies(tmr1AsyncSetting, ["TIMER1_SRC_SEL", "TIMER1_TSYNC"])

    tmr1Sym_CLOCK_FREQ = tmr1Component.createIntegerSymbol("TIMER1_CLOCK_FREQ", None)
    tmr1Sym_CLOCK_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_CLOCK_FREQ.setLabel("Timer1 Clock Frequency")
    tmr1Sym_CLOCK_FREQ.setVisible(True)
    tmr1Sym_CLOCK_FREQ.setReadOnly(True)
    tmr1Sym_CLOCK_FREQ.setDefaultValue(int(Database.getSymbolValue("core", tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY")))
    tmr1Sym_CLOCK_FREQ.setDependencies(calcTimerFreq, ["core." + tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY",
        "TMR1_PRESCALER_VALUE", "TIMER1_SRC_SEL", "TIMER1_EXT_CLOCK_FREQ", "TIMER1_TECS"])

    global tmrSym_TimerUnit
    timerUnit = ["millisecond", "microsecond", "nanosecond"]
    tmrSym_TimerUnit = tmr1Component.createComboSymbol("TIMER_UNIT", None, timerUnit)
    tmrSym_TimerUnit.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmrSym_TimerUnit.setLabel("Timer Period Unit")
    tmrSym_TimerUnit.setDefaultValue("millisecond")

    clock = Database.getSymbolValue("core", tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY")
    if(clock != 0):
        resolution = 1000.0 * tmr1PrescalerValue.getValue()/float(clock)
        max = (65537.0 * resolution)
    else:
        max = 0

    tmr1Sym_PERIOD_MS = tmr1Component.createFloatSymbol("TIMER1_TIME_PERIOD_MS", None)
    tmr1Sym_PERIOD_MS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_PERIOD_MS.setLabel("Time")
    tmr1Sym_PERIOD_MS.setDefaultValue(0.3)
    tmr1Sym_PERIOD_MS.setMin(0.0)
    tmr1Sym_PERIOD_MS.setMax(max)
    tmr1Sym_PERIOD_MS.setDependencies(timerMaxValue, ["core." + tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY",
        "TIMER1_CLOCK_FREQ", "TIMER_UNIT"])

    if clock != 0:
        period = (tmr1Sym_PERIOD_MS.getValue() / resolution) - 1
    else:
        period = 0

    #Timer1 Period Register
    tmr1Sym_PR1 = tmr1Component.createLongSymbol("TIMER1_PERIOD", tmr1Sym_PERIOD_MS)
    tmr1Sym_PR1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1Sym_PR1.setLabel("Period Register")
    tmr1Sym_PR1.setDefaultValue(long(period))
    tmr1Sym_PR1.setReadOnly(True)
    tmr1Sym_PR1.setMin(0)
    tmr1Sym_PR1.setMax(65535)
    tmr1Sym_PR1.setDependencies(timerPeriodCalc, ["core." + tmr1InstanceName.getValue() + "_CLOCK_FREQUENCY",
        "TIMER1_TIME_PERIOD_MS", "TIMER1_CLOCK_FREQ", "TIMER_UNIT"])

    #timer SIDL configuration
    sidl_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_SIDL, sidl_names)
    tmr1SymField_T1CON_SIDL = tmr1Component.createKeyValueSetSymbol("TIMER1_SIDL", None)
    tmr1SymField_T1CON_SIDL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1SymField_T1CON_SIDL.setLabel(tmr1BitField_T1CON_SIDL.getAttribute("caption"))
    tmr1SymField_T1CON_SIDL.setOutputMode( "Value" )
    tmr1SymField_T1CON_SIDL.setDisplayMode( "Description" )
    for ii in sidl_names:
        tmr1SymField_T1CON_SIDL.addKey( ii['key'],ii['value'], ii['desc'] )
    tmr1SymField_T1CON_SIDL.setDefaultValue(find_key_value(0,sidl_names))  # continue operation when in idle mode

    #timer TGATE configuration
    tgate_names = []
    _get_bitfield_names(tmr1ValGrp_T1CON_TGATE, tgate_names)
    tmr1SymField_T1CON_TGATE = tmr1Component.createKeyValueSetSymbol("TIMER1_TGATE", tmr1Sym_T1CON_SOURCE_SEL)
    tmr1SymField_T1CON_TGATE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    tmr1SymField_T1CON_TGATE.setLabel(tmr1BitField_T1CON_TGATE.getAttribute("caption"))
    tmr1SymField_T1CON_TGATE.setOutputMode( "Value" )
    tmr1SymField_T1CON_TGATE.setDisplayMode( "Description" )
    for ii in tgate_names:
        tmr1SymField_T1CON_TGATE.addKey( ii['key'],ii['value'], ii['desc'] )
    tmr1SymField_T1CON_TGATE.setDefaultValue(find_key_value(0,tgate_names))  # gated time accumulation disabled
    tmr1SymField_T1CON_TGATE.setDependencies(tmr1TgateVisible, ["TIMER1_SRC_SEL"])

    #Timer1 TxCON Reg Value
    tmr1Sym_T1CON_Value = tmr1Component.createHexSymbol("TCON_REG_VALUE", None)
    default_value = (int(tmr1SymField_T1CON_SIDL.getSelectedValue()) << 13) | (int(tmr1SymField_T1CON_TWDIS.getSelectedValue()) << 12) | (int(tmr1SymField_T1CON_TECS.getSelectedValue()) << 8) | \
                    (int(tmr1SymField_T1CON_TGATE.getSelectedValue()) << 7) | (int(tmr1Sym_T1CON_PRESCALER.getSelectedValue()) << 4) | (int(tmr1Sym_T1CON_TSYNC.getSelectedValue()) << 2) | \
                    (int(tmr1Sym_T1CON_SOURCE_SEL.getSelectedValue()) << 1)
    tmr1Sym_T1CON_Value.setDefaultValue(default_value)
    tmr1Sym_T1CON_Value.setVisible(False)
    tmr1Sym_T1CON_Value.setDependencies(T1CONcombineValues,["TIMER1_SIDL", "TIMER1_TWDIS", "TIMER1_TECS", "TIMER1_TGATE", "TIMER1_PRE_SCALER", "TIMER1_TSYNC", "TIMER1_SRC_SEL"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    ## EVIC Interrupt Dynamic settings
    setTMR1InterruptData(tmr1SymInterruptMode.getValue())

    tmr1SymIntEnComment = tmr1Component.createCommentSymbol("TMR1_INTRRUPT_ENABLE_COMMENT", None)
    tmr1SymIntEnComment.setLabel("Warning!!! " + tmr1InstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    tmr1SymIntEnComment.setVisible(False)
    tmr1SymIntEnComment.setDependencies(updateTMR1InterruptData, ["TMR1_INTERRUPT_MODE", "core." + tmr1InterruptVectorUpdate])

    # Clock Warning status
    tmr1Sym_ClkEnComment = tmr1Component.createCommentSymbol("TMR1_CLOCK_ENABLE_COMMENT", None)
    tmr1Sym_ClkEnComment.setLabel("Warning!!! " + tmr1InstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    tmr1Sym_ClkEnComment.setVisible(False)
    tmr1Sym_ClkEnComment.setDependencies(updateTMR1ClockWarningStatus, ["core." + tmr1InstanceName.getValue() + "_CLOCK_ENABLE"])

    irqEnumName_Sym = tmr1Component.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue(str(tmr1Irq_index))

    sysTimeComponentId = tmr1Component.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tmr1_02141;register:%NOREGISTER%")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")

    dvrtComponentId = tmr1Component.createStringSymbol("DVRT_COMPONENT_ID", None)
    dvrtComponentId.setLabel("dvrt Component id")
    dvrtComponentId.setVisible(False)
    dvrtComponentId.setDefaultValue("")
    
    i2cbbComponentId = tmr1Component.createStringSymbol("I2C_BB_COMPONENT_ID", None)
    i2cbbComponentId.setLabel("Component id")
    i2cbbComponentId.setVisible(False)
    i2cbbComponentId.setDefaultValue("")

    timerStartApiName = tmr1InstanceName.getValue() +  "_Start"
    timerStopApiName = tmr1InstanceName.getValue() + "_Stop "
    counterGetApiName = tmr1InstanceName.getValue() +  "_CounterGet"
    frequencyGetApiName = tmr1InstanceName.getValue() + "_FrequencyGet"
    callbackApiName = tmr1InstanceName.getValue() + "_CallbackRegister"
    periodSetApiName = tmr1InstanceName.getValue() + "_PeriodSet"

    timerWidth_Sym = tmr1Component.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = tmr1Component.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = tmr1Component.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = tmr1Component.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timerStopApiName)

    counterApiName_Sym = tmr1Component.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = tmr1Component.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = tmr1Component.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)

    periodSetApiName_Sym = tmr1Component.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)
    periodSetApiName_Sym.setDefaultValue(periodSetApiName);
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tmr1HeaderFile = tmr1Component.createFileSymbol("TMR1_COMMON_HEADER", None)
    tmr1HeaderFile.setSourcePath("../peripheral/tmr1_02141/templates/plib_tmr1_common.h")
    tmr1HeaderFile.setOutputName("plib_tmr1_common.h")
    tmr1HeaderFile.setDestPath("peripheral/tmr1/")
    tmr1HeaderFile.setProjectPath("config/" + configName + "/peripheral/tmr1/")
    tmr1HeaderFile.setType("HEADER")
    tmr1HeaderFile.setMarkup(False)
    tmr1HeaderFile.setOverwrite(True)

    # Instance Header File
    tmr1HeaderFile = tmr1Component.createFileSymbol("TMR1_HEADER", None)
    tmr1HeaderFile.setSourcePath("../peripheral/tmr1_02141/templates/plib_tmr1.h.ftl")
    tmr1HeaderFile.setOutputName("plib_" + tmr1InstanceName.getValue().lower() + ".h")
    tmr1HeaderFile.setDestPath("/peripheral/tmr1/")
    tmr1HeaderFile.setProjectPath("config/" + configName + "/peripheral/tmr1/")
    tmr1HeaderFile.setType("HEADER")
    tmr1HeaderFile.setMarkup(True)
    tmr1HeaderFile.setOverwrite(True)

    # Instance Source File
    tmr1SourceFile = tmr1Component.createFileSymbol("TMR1_SOURCE", None)
    tmr1SourceFile.setSourcePath("../peripheral/tmr1_02141/templates/plib_tmr1.c.ftl")
    tmr1SourceFile.setOutputName("plib_" + tmr1InstanceName.getValue().lower() + ".c")
    tmr1SourceFile.setDestPath("/peripheral/tmr1/")
    tmr1SourceFile.setProjectPath("config/" + configName + "/peripheral/tmr1/")
    tmr1SourceFile.setType("SOURCE")
    tmr1SourceFile.setMarkup(True)
    tmr1SourceFile.setOverwrite(True)

    tmr1Sym_SystemInitFile = tmr1Component.createFileSymbol("TMR1_SYS_INT", None)
    tmr1Sym_SystemInitFile.setType("STRING")
    tmr1Sym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tmr1Sym_SystemInitFile.setSourcePath("../peripheral/tmr1_02141/templates/system/initialization.c.ftl")
    tmr1Sym_SystemInitFile.setMarkup(True)

    tmr1Sym_SystemDefFile = tmr1Component.createFileSymbol("TMR1_SYS_DEF", None)
    tmr1Sym_SystemDefFile.setType("STRING")
    tmr1Sym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tmr1Sym_SystemDefFile.setSourcePath("../peripheral/tmr1_02141/templates/system/definitions.h.ftl")
    tmr1Sym_SystemDefFile.setMarkup(True)
