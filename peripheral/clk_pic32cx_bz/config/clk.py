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

from os.path import join
from xml.etree import ElementTree
from collections import defaultdict


global enableMenu
global updateRefFreq
global get_val_from_str
global set_refocon_value
global set_pbdiv_value
global set_refotrim_value

# atdf-specific areas
global clkValGrp_OSCCON__FRCDIV
global clkRegGrp_SPLLCON
global CRUmoduleStart
global clkRegGrp_OSCCON
clkValGrp_OSCCON__SOSCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__SOSCEN"]')
clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__FRCDIV"]')
clkValGrp_REFO1CON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__ROSEL"]')
clkValGrp_REFO1CON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__RODIV"]')
clkValGrp_REFO1TRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1TRIM__ROTRIM"]')
clkRegGrp_SPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="SPLLCON"]')
clkRegGrp_OSCCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="OSCCON"]')
CRUmoduleStart = '/avr-tools-device-file/modules/module@[name="CRU"]'

# for PLL BW selection setting for the different PLLs present
global _4Mhz
global _5Mhz
global _6Mhz
global _7Mhz
global _8Mhz
global _9Mhz
global _10Mhz
global _11Mhz
global _12Mhz
global _13Mhz
global _14Mhz
global _15Mhz
global _16Mhz
global _17Mhz
global _18Mhz
global _19Mhz
global _20Mhz
global _21Mhz
global _24Mhz
global _28Mhz
global _30Mhz
global _32Mhz
global _36Mhz
global _40Mhz
global _44Mhz
global _45Mhz
global _48Mhz
global _49Mhz
global _50Mhz
global _52Mhz
global _56Mhz
global _60Mhz
global _800_Mhz
global _1200_Mhz
global _1600_Mhz
_4Mhz = 4000000
_5Mhz = 5000000
_6Mhz = 6000000
_7Mhz = 7000000
_8Mhz = 8000000
_9Mhz = 9000000
_10Mhz = 10000000
_11Mhz = 11000000
_12Mhz = 12000000
_13Mhz = 13000000
_14Mhz = 14000000
_15Mhz = 15000000
_16Mhz = 16000000
_17Mhz = 17000000
_18Mhz = 18000000
_19Mhz = 19000000
_20Mhz = 20000000
_21Mhz = 21000000
_24Mhz = 24000000
_28Mhz = 28000000
_30Mhz = 30000000
_32Mhz = 32000000
_36Mhz = 36000000
_40Mhz = 40000000
_44Mhz = 44000000
_45Mhz = 45000000
_48Mhz = 48000000
_49Mhz = 49000000
_50Mhz = 50000000
_52Mhz = 52000000
_56Mhz = 56000000
_60Mhz = 60000000
_800_Mhz = 800000000
_1200_Mhz = 1200000000
_1600_Mhz = 1600000000


global peripheralBusDict
peripheralBusDict = {}

peripheralBusDict =  {

        #Peripheral : ["Peripheral bus  "PMD register no", "PMD register bit no"]
        # if "Peripheral bus no" == -1 then clocked by SYSCLK

        "ZIGBEE":["2","1","0"],
        "BLE":["2","1","1"],
        "MPA":["2","1","2"], # RF Hogh Power
        "LPA":["2","1","3"], # RF Low Power
        "PLVD":["1","1","4"],
        "AC":["1","1","6"],
        "ADCHS":["2","1","7","8"], # ADC has multiple PMD bits
       # "ADCSAR":["2","1","8"],
        "RTC":["4","1","16"],
        "QSPI":["3","1","29"],

        "REFO1":["-1","2","28"],
        "REFO2":["-1","2","29"],
        "REFO3":["-1","2","30"],
        "REFO4":["-1","2","31"],
        "REFO5":["-1","2","24"],
        "REFO6":["-1","2","25"],

        "SERCOM0_CORE":["3","3","0"],
        "SERCOM1_CORE":["3","3","1"],
        "SERCOM2_CORE":["1","3","2"],
        "SERCOM3_CORE":["3","3","3"],
        "ICM":["2","3","4"], # INTEGRITY CHECK MONITOR
        "PUKCC":["3","3","5"], # PUBLIC KEY CRYPTOGRAPHY CONTROLLER
        "TRNG":["3","3","6"],
        "AES":["2","3","7"], # ADVANCED ENCRYPTION STANDARD
        "TC0":["-1","3","8"],
        "TC1":["-1","3","9"],
        "TC2":["-1","3","10"],
        "TC3":["-1","3","11"],
        "TCC0":["-1","3","12"],
        "TCC1":["-1","3","13"],
        "TCC2":["-1","3","14"],
}

global defaultEnablePeripheralsList
defaultEnablePeripheralsList = ["PLVD", "REFO1", "REFO2", "REFO3", "REFO4", "REFO5", "REFO6"]

global item_update

def item_update(symbol, event):
    '''
    General setter callback function for any particular event that was used to call this callback
    '''
    symbol.setValue(event['value'],2)

def updateMaxFreq(symbol, event):
    # right now, both are at same value - leaving this logic in here in case need to add temperature range for product later
    if event["value"] == 0:
        symbol.setValue(250000000, 2)
    elif event["value"] == 1:
        symbol.setValue(250000000, 2)

global _get_bitfield_names

def _get_bitfield_names(node, outputList):
    '''
    Gets all <value > children of 'node', appending dictionary entries to 'outputList'
    Arguments:
        node - points to atdf file, parent of <value > entries currently are interested in for this fct call
        outputList - list which will have dictionary elements comprised of following:
            key:   name field of <value >
            value: value field of <value >
    '''
    valueNodes = node.getChildren()
    for ii in valueNodes:   # do this for all <value > entries for this bitfield
        if(ii.getAttribute('name').lower() != "reserved"):
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            outputList[ii.getAttribute('name')] = str(tempint)

global _get_bitfield_info

def _get_bitfield_info(atdfStartPlace, outputList, valuesField):
    # this routine works with combo symbols, generating all key/value pairs for a given bitfield
    # the function is given starting place in atdf file (top of a module), and goes from there
    base = ATDF.getNode(atdfStartPlace)
    theNodes = base.getChildren()
    for ii in theNodes:
        if(ii.getAttribute('name')==valuesField):
            valueGroupLocn = ii
    _get_bitfield_names(valueGroupLocn, outputList)
    return valueGroupLocn

def enableMenu(menu, event):
    menu.setVisible(event["value"])

def updateRODIVmin (symbol, event):
    if "_ENABLE" in event["id"]:
        symbol.setVisible(event["value"])
    elif "CONFIG_SYS_CLK_REFCLK_SOURCE" in event["id"]:
        if event["value"] == "SPLL3":
            symbol.setMin(1)
        else:
            symbol.setMin(0)

# get default value from atdf file
global refclkDefaultFreq
def refclkDefaultFreq(refClockNumber):
    defFreq = "0"
    targetName = "__REFCLK" + refClockNumber + "_DEF_FREQ"
    params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
    paramsChildren = params.getChildren()
    for param in paramsChildren:  # find parameter we are interested in now
        if(param.getAttribute("name") == targetName):
            defFreq = param.getAttribute("value")
    return defFreq

def updateRefFreq(menu, event):
    if event["value"] == True:
        ii = event["id"].split("_")[3][-1]
        menu.setValue(refclkDefaultFreq(ii))
    else:
        menu.setValue("0",2)

def get_val_from_str(stringVal):
    # converts string-based number to integer
    if(stringVal.find('0x')!=-1):
        intVal = int(stringVal[2:],16)
    else:
        intVal = int(stringVal)
    return intVal

def _find_key(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.  Needed for setting up combo symbol value.
          value - the value to be looked for in the dictionary
          keypairs - the dictionary to be searched over
    '''
    for keyname, val in keypairs.items():
        if(val == str(value)):
            return keyname
    print("_find_key: could not find value in dictionary") # should never get here
    return ""

global _get_default_value

def _get_default_value(register, bitfield, value_group):
    '''
    Extracts the default value from 'initval' field of given value-group, based on register bitfield
    Input arguments:
        register - atdf node, register name to get the intial value
        bitfield - the bitfield in the register we are interested in (to get mask value from)
        value_group - atdf node, the value group from which we want ('None' here means this bitfield is integer type; there is no <value-group> for it)

    Returns:
        String, representing the key value default name of that bitfield
    '''
    initialValue = int(register.getAttribute('initval'),16)
    childNodes = register.getChildren()
    for ii in childNodes:  # scan over all <bitfield ..> to find right bitfield
        if(ii.getAttribute('name') == bitfield):
            maskval = ii.getAttribute('mask')
            if(maskval.find('0x')!= -1):
                mask = int(maskval,16)
            else:
                mask = int(maskval)
            bitPosn = 0
            while((mask & (1<<bitPosn)) == 0):
                bitPosn += 1
    value = str(hex((initialValue & mask) >> bitPosn)).strip('L')  # has initial value of bitfield, shifted down to bit0
    keyDefault = ''
    if(value_group != 'None'):
        childNodes = value_group.getChildren() # get all <value ..> to find the one that matches the value
        for ii in childNodes:
            if(ii.getAttribute('value') == value):
                keyDefault = ii.getAttribute('name')
        return keyDefault
    else:
        return int(value,16)

global _get_default_index

def _get_default_index(register, bitfield, value_group):
    '''
    Extracts the default value from 'initval' field of given value-group, based on register bitfield
    Input arguments:
        register - atdf node, register name to get the intial value
        bitfield - the bitfield in the register we are interested in (to get mask value from)
        value_group - atdf node, the value group from which we want ('None' here means this bitfield is integer type; there is no <value-group> for it)

    Returns:
        String, representing the key value default name of that bitfield
    '''
    initialValue = int(register.getAttribute('initval'),16)
    childNodes = register.getChildren()
    for ii in childNodes:  # scan over all <bitfield ..> to find right bitfield
        if(ii.getAttribute('name') == bitfield):
            maskval = ii.getAttribute('mask')
            if(maskval.find('0x')!= -1):
                mask = int(maskval,16)
            else:
                mask = int(maskval)
            bitPosn = 0
            while((mask & (1<<bitPosn)) == 0):
                bitPosn += 1
    value = str(hex((initialValue & mask) >> bitPosn)).strip('L')  # has initial value of bitfield, shifted down to bit0
    if(value_group != 'None'):
        childNodes = value_group.getChildren() # get all <value ..> to find the one that matches the value
        for index in range(len(childNodes)):
            if(childNodes[index].getAttribute('value') == value):
                return index
    else:
        return 0

def _get_default_value_num(register, bitfield, value_group):
    '''
    Extracts the default value from 'initval' field of given value-group, based on register bitfield
    Input arguments:
        register - atdf node, register name to get the intial value
        bitfield - the bitfield in the register we are interested in (to get mask value from)
        value_group - atdf node, the value group from which we want

    Returns:
        default name of that bitfield
    '''
    initialValue = int(register.getAttribute('initval'),16)
    childNodes = register.getChildren()
    for ii in childNodes:  # scan over all <bitfield ..> to find right bitfield
        if(ii.getAttribute('name') == bitfield):
            maskval = ii.getAttribute('mask')
            if(maskval.find('0x')!= -1):
                mask = int(maskval,16)
            else:
                mask = int(maskval)
            bitPosn = 0
            while((mask & (1<<bitPosn)) == 0):
                bitPosn += 1
    value = str((initialValue & mask) >> bitPosn)  # has initial value of bitfield, shifted down to bit0
    return value

def setRoselDefault_clk(symbol, event):
    global symbolRoselMaskLsbList
    global symbolRoselMaskList
    global roselSymbolList
    # have to figure out clock from event id, so can use the right symbol during the setValue call
    clk = int(event["id"][-1]) - 1 # "-1" is since indexing starts at 1 (and list indexing starts at 0)
    symObj=event["symbol"]
    roselSymbolList[clk].setValue(int(symObj.getSelectedValue()),1)

    mydict = {}
    for ii in symbolRoselMaskLsbList:   # find the right entry in this list
        mydict = dict(ii)
        if(mydict['index'] == str(event["id"])):
            masklsb = mydict['symbol']

    for jj in symbolRoselMaskList:      # find the right entry in this list
        mydict = dict(jj)
        if(mydict['index'] == str(event["id"])):
            mask = get_val_from_str(mydict['symbol'].getValue())

    for kk in roselSymbolList:
        mydict = dict(kk)
        if(mydict['index'] == str(event["id"])):
            temp = mydict['symbol'].getValue()
            if(temp.find('0x')!=-1):
                mask = int(temp[2:],16)
            else:
                mask = int(temp)

    payload = int(symbolName.getValue()) << int(masklsb.getValue())
    payload = payload & int(mask)

def set_refocon_value(clknum):
    # calculates the vlaue to set the REFOCON register to
    global symbolRoselMaskLsbList
    global symbolRoselMaskList
    global sourceSymbolList
    global symbolRoselValueList
    global symbolRodivValueList
    global symbolRodivMask
    global symbolRodivMaskLsb
    global roselMap

    # calculates the vlaue to set the REFOCON register to
    mydict = {}
    # get the ROSEL field bit shift value
    for ii in symbolRoselMaskLsbList:   # find the right entry in this list, indicated by last char of event["id"]
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):
            masklsb = mydict['symbol']

    # get the ROSEL mask value
    for ii in symbolRoselMaskList:      # find the right entry in this list, indicated by last char of event["id"]
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):
            mask = get_val_from_str(mydict['symbol'].getValue())

    # get the DIVSWEN mask value
    for ii in symbolDivswenMask:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):
            divswenmask = get_val_from_str(mydict['symbol'].getValue())

    # get the RODIV mask value
    for ii in symbolRodivMask:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):
            rodivmask = get_val_from_str(mydict['symbol'].getValue())

    # get the RODIV field bit shift value
    for ii in symbolRodivMaskLsb:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):
            rodivmasklsb = get_val_from_str(mydict['symbol'].getValue())

    payload = 0
    # get the user-set value for the ROSEL field (in symbolRoselValueList[ ], symbolID: CONFIG_SYS_CLK_REFCLK_SOURCEx)
    # modify payload value based on that user-set value
    for ii in symbolRoselValueList:         # find the right entry in this list, indicated by last char of event["id"]
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # have found right symbol (indicated in symbolID REFOCONx_VALUE)
            payload = int(roselMap[mydict['symbol'].getValue()]) << int(masklsb.getValue())
            payload = payload & int(mask)
            payload = payload | divswenmask

    # get the user-set value for the RODIV field (in symbolRodivValueList[ ], symbolID: CONFIG_SYS_CLK_RODIV)
    # modify payload value based on that user-set value
    for ii in symbolRodivValueList:         # find the right entry in this list, indicated by last char of event["id"]
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # have found right symbol (indicated in symbolID REFOCONx_VALUE)
            contributor = rodivmask & (mydict['symbol'].getValue() << rodivmasklsb)
            payload = payload | contributor

    return (str(hex(payload)))

global RSLP_MASK
RSLP_MASK = 0x00000800
global SIDL_MASK
SIDL_MASK = 0x00002000

def refocon_update(symbol, event):
    #This is the callback for REFOCON_VALUEx symbolID.
    
    global refconval
    global rslpSymbolList
    global sidlSymbolList

    # find out which clock we care about by looking at the id.  The last char in the id is clock number
    clk = int(event["id"][-1]) - 1 # "-1" is since indexing starts at 1 (and list indexing starts at 0)
    index = int(event["id"][-1])  # the last char of the event ID is the index needed to be used
    
    newValueWithoutRSLP_SIDL = int(set_refocon_value(index), 16)

    if rslpSymbolList[clk].getValue() == False:
        newValue = newValueWithoutRSLP_SIDL & (~RSLP_MASK)
    else: 
        newValue = newValueWithoutRSLP_SIDL | RSLP_MASK

    if sidlSymbolList[clk].getValue() == False:
        newValue = newValue & (~SIDL_MASK)
    else: 
        newValue = newValue | SIDL_MASK

    # finally, set the symbol value to the newly-calculated value
    refconval[clk].setValue(str(hex(newValue)))

def set_pbdiv_value(clknum):
    '''
    Sets the value to use in PBxDIV when enabling a Peripheral Bus for a register
    '''
    global symbolPbRegMaskLsb
    global symbolPbRegMask
    global symbolPbOnMask
    global symbolPbdivList
    mydict = {}

    # get the PBDIV bit shift value
    for ii in symbolPbRegMaskLsb:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            masklsb = mydict['symbol']

    # get the mask for PBDIV field
    for ii in symbolPbRegMask:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            mask = mydict['symbol']

    # get the mask for the ON field
    for ii in symbolPbOnMask:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            onmaskval = get_val_from_str(mydict['symbol'].getValue())

    # get the user-set value in PBDIV field
    payload = 0
    for ii in symbolPbdivList:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            payload = (int(mydict['symbol'].getValue())-1) << int(masklsb.getValue())
            payload = payload & int(mask.getValue(),16)
            if(clknum != '1'):  # PB1DIV does not have an ON bitfield:  always on
                payload = payload | onmaskval
    return str(hex(payload))

def pbdiv_update(symbol, event):
    '''
    This is the callback for REFOCON_VALUEx symbolID.
    It is called when the user changes either of the following:
        CONFIG_SYS_CLK_REFCLK_SOURCEx
        CONFIG_SYS_CLK_RODIVx
    '''
    # find out which bus applies by looking at the id.  The last char in the id is bus number
    bus = int(event["id"][-1])
    symbol.setValue(set_pbdiv_value(bus),2)

def set_refotrim_value(clknum):
    '''
    Sets the value to use in REFOxTRIM
    '''
    global refotrimval
    global symbolRotrimmaskLsb
    global symbolRotrimMask
    global symbolrefotrimval
    global symbolRotrimUserVal

    mydict = {}

    # get the REFOTRIM mask value
    for ii in symbolRotrimMask:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            mask = get_val_from_str(mydict['symbol'].getValue())

    # get the mask for REFOTRIM bit shift position
    for ii in symbolRotrimmaskLsb:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            masklsb = get_val_from_str(mydict['symbol'].getValue())

    # get the user-set value in ROTRIM, symbolID CONFIG_SYS_CLK_ROTRIMx
    payload = 0
    for ii in symbolRotrimUserVal:
        mydict = dict(ii)
        if(mydict['index'] == str(clknum)):  # find the entry for this peripheral bus number
            payload = int(mydict['symbol'].getValue()) << masklsb
            payload = payload & mask
    return str(hex(payload)).strip('L')

def refotrim_update(symbol, event):
    '''
    This is the callback for REFOxTRIM_VALUE symbolID.
    It is called when the user changes the following:
        CONFIG_SYS_CLK_ROTRIMx
    '''
    # find out which bus applies by looking at the id.  The last char in the id is bus number
    bus = int(event["id"][-1])
    symbol.setValue(set_refotrim_value(bus),2)

global cpuClockFreqCalc

def cpuClockFreqCalc(symbol, event):

    symbol.setValue(event["value"], 1)

def clkSetup(symbol, event):
    global indexSymbolMap
    symbolKey = ""
    status = False
    if "_CLOCK_ENABLE" in event["id"]:
        for key,value in indexSymbolMap.iteritems():
            for i in range(0,len(value)):
                if value[i] == event["id"].split("_CLOCK_ENABLE")[0]:
                    symbolKey = key
                    break
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            status = status | Database.getSymbolValue("core", i + "_CLOCK_ENABLE")
        Database.setSymbolValue("core", symbolKey + "_CHEN", status, 2)
        if event["value"]:
            freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
            Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", freq , 2)
        else :
            Database.setSymbolValue("core", event["id"].split("_CLOCK_ENABLE")[0] + "_CLOCK_FREQUENCY", 0, 2)

    if "_FREQ" in event["id"]:
        symbolKey = event["id"].split("_FREQ")[0]
        symbolValues = indexSymbolMap.get(symbolKey)
        for i in symbolValues:
            if Database.getSymbolValue("core", i + "_CLOCK_ENABLE"):
                freq = Database.getSymbolValue("core", symbolKey + "_FREQ")
                Database.setSymbolValue("core", i + "_CLOCK_FREQUENCY", freq , 2)

def setGclkFreq(symbol, event):
    index = symbol.getID().split("_FREQ")[0]
    channelEnabled = Database.getSymbolValue("core", index + "_CHEN")

    component = symbol.getComponent()
    periSourceIndex = Database.getSymbolValue("core",index + "_GENSEL")
    periSource = (component.getSymbolByID(index + "_GENSEL")).getKey(periSourceIndex)

    if "_FREQ" not in event["id"]:
        if channelEnabled:
            if "REFO" in periSource :
                srcFreq = int(Database.getSymbolValue("core","CONFIG_SYS_CLK_REFCLK"+ periSource.replace("REFO", "") + "_FREQ"))
                symbol.setValue(srcFreq,1)
            elif periSource == "LPCLK":
                symbol.setValue(Database.getSymbolValue("core", "LPCLK_FREQ"),1)
            else:
                symbol.setValue(0, 1)
        else:
            symbol.setValue(0, 1)

    elif ("_FREQ" in event["id"]) and ("REFCLK" in event["id"]):
        if channelEnabled:
            generator = event["id"].split("_")[3].replace("REFCLK", "REFO")
            if periSource == generator:
                symbol.setValue(int(event["value"]))
    elif ("LPCLK_FREQ" in event["id"]):
        if channelEnabled:
            generator = event["id"].split("_")[0]
            if periSource == generator:
                symbol.setValue(int(event["value"]))

def updateGENSEL(symbol, event):
    if event["value"] == True: # if peripheral is enabled, set REFCLK1 as its clock source by default
        symbol.setValue(1)
    else: # if peripheral is disabled, set no clock as its clock source by default
        symbol.setValue(0)

global setCFGPCLKGENx_Reg
def setCFGPCLKGENx_Reg (symbol, event):
    clockNumber = int(event["id"].split("_")[2])
    registerNumber = str(clockNumber/8 + 1)
    regValue = Database.getSymbolValue("core", "CFGPCLKGEN"+registerNumber+"_REG")

    
    if "CHEN" in event["id"]:
        bitFieldPosition = ((clockNumber % 8)*4) + 3
        if event["value"]:
            regValue |= (1 << bitFieldPosition)
        else:
            regValue &= (~(1 << bitFieldPosition))
    elif "GENSEL" in event["id"]:   
        bitFieldPosition = ((clockNumber % 8)*4) + 0
        bitFieldMask = 7 << bitFieldPosition

        component = symbol.getComponent()
        genselIndex = event["value"]
        gensel = int((component.getSymbolByID(event["id"])).getKeyValue(genselIndex),16)

        regValue = (regValue & (~bitFieldMask)) | (gensel << bitFieldPosition)

    Database.setSymbolValue("core", "CFGPCLKGEN"+registerNumber+"_REG", regValue )

global CHECK_LOW_PLL

def CHECK_LOW_PLL(Fvco):
    if( (Fvco >= _800_Mhz) and (Fvco < _1200_Mhz) ):   #RANGE1
        return 0
    elif( (Fvco >= _1200_Mhz) and (Fvco <= _1600_Mhz) ):  #RANGE2
        return 6

global CHECK_HIGH_PLL

def CHECK_HIGH_PLL(Fvco):
    if( (Fvco >= _800_Mhz) and (Fvco < _1200_Mhz) ): # RANGE1
        return 1
    elif( (Fvco >= _1200_Mhz) and (Fvco <= _1600_Mhz) ): # RANGE2
        return 7

global CHECK_800_1600_FVCO

def CHECK_800_1600_FVCO(Fvco):
    if( (Fvco >= _800_Mhz) and (Fvco <= _1600_Mhz)):
        return True
    else:
        return False

def updatePMDxRegValue(symbol, event):

    bitShift = 0
    if "REFCLK" in event["id"]:
        periName = event["id"].split("_")[3].replace("CLK", "O") # find the REF OSC name matching with PMD field
    else:    
        periName = event["id"].replace("_CLOCK_ENABLE", "")

    if periName in peripheralBusDict:
        pmdRegId = "PMD" + peripheralBusDict[periName][1] + "_REG_VALUE"
        pmdxValue = Database.getSymbolValue("core", pmdRegId)

        # Check if peripheral is having multiple PMD bits
        if len(peripheralBusDict[periName]) > 3:
            for i in range(2, len(peripheralBusDict[periName])):
                bitShift |= 1 << int(peripheralBusDict[periName][i])
        else:
            bitShift = 1 << int(peripheralBusDict[periName][2])

        if event["value"]:
            pmdxValue = pmdxValue & ~bitShift
        else:
            pmdxValue = pmdxValue | bitShift

        Database.setSymbolValue("core", pmdRegId, pmdxValue, 1)

# POSC with POSCMOD effect
global poscOutDefaultFreq 
def poscOutDefaultFreq():
    if Database.getSymbolValue("core", "CONFIG_POSCMOD") == "OFF":
        return 0
    else:
        return Database.getSymbolValue("core","CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL")

global poscOutFreqCalc 
def poscOutFreqCalc(symbol, event):
    symbol.setValue(int(poscOutDefaultFreq()))

# SOSC with LPOSCEN effect
global soscOutDefaultFreq 
def soscOutDefaultFreq():
    if Database.getSymbolValue("core", "CONFIG_LPOSCEN") == "OFF":
        return 0
    else:
        return Database.getSymbolValue("core","CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL")

global soscOutFreqCalc 
def soscOutFreqCalc(symbol, event):
    symbol.setValue(int(soscOutDefaultFreq()))

# SPLL3 or RFPLL
global spll3DefaultFreq 
def spll3DefaultFreq():
    return (Database.getSymbolValue("core","POSC_OUT_FREQ") * 6)

global spll3OutFreqCalc 
def spll3OutFreqCalc(symbol, event):
    symbol.setValue(spll3DefaultFreq())

# SPLL1
global spll1DefaultFreq
def spll1DefaultFreq():

    freq = Database.getSymbolValue("core", "SPLL3_RFPLL_FREQ")
    dividor = Database.getSymbolValue("core","SPLLCON_SPLLPOSTDIV1_VALUE")

    if dividor == 0: # meaning it is divide by 1
        return freq
    elif dividor == 1: # meaning it is divide by 1.5
        return (freq * 2)/3
    else:
        return (freq/dividor)

global spll1ClockFreqCalc
def spll1ClockFreqCalc(symbol, event):
    symbol.setValue(spll1DefaultFreq())

# SPLL2
global spll2DefaultFreq
def spll2DefaultFreq():
    spll2_source_index = Database.getSymbolValue("core", "SPLLCON_SPLL_BYP_VALUE")
    for ii in spllcon_symbols:
        if(ii['name'] == "SPLL_BYP"):
            spllcon_spllbyp_val = ii['symvaluename']
        elif(ii['name'] == "SPLLPOSTDIV2"):
            spllcon_spllpostdiv2_val = ii['symvaluename']

    spll2_source = spllcon_spllbyp_val.getKey(spll2_source_index)
    if "SPLL3" in spll2_source:
        freq = int(Database.getSymbolValue("core", "SPLL3_RFPLL_FREQ"))
    elif "POSC" in spll2_source:
        freq = int(Database.getSymbolValue("core", "POSC_OUT_FREQ"))
    else: # FRC
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_FRC"))

    dividor_index = Database.getSymbolValue("core", "SPLLCON_SPLLPOSTDIV2_VALUE")
    dividor = int(spllcon_spllpostdiv2_val.getKeyValue(dividor_index)[2:], 16)
    if dividor == 0:
        spll2 = 0
    else:
        spll2 = freq/dividor

    return spll2

global spll2ClockFreqCalc
def spll2ClockFreqCalc(symbol, event):
    symbol.setValue(int(spll2DefaultFreq()))

# LPCLK Freq
global lpclkClockFreqCalc
def lpclkClockFreqCalc(symbol, event):
    inputFreq = VBKP_32KCSEL_MuxOutput()
    
    if Database.getSymbolValue("core", "CONFIG_LPCLK_MOD") == "DIV_1":
        dividor = 1
    else:
        dividor = 1.024

    outputFreq = inputFreq/dividor
    symbol.setValue(int(outputFreq))

# WDT
global wdtClockFreqCalc
def wdtClockFreqCalc(symbol,event):
    if Database.getSymbolValue("core", "CONFIG_WDTRMCS") == "LPRC":
        symbol.setValue(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_LPRC"))
    else:
        symbol.setValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))

global VBKP_32KCSEL_MuxOutput
def VBKP_32KCSEL_MuxOutput():
    mux = Database.getSymbolValue("core", "CONFIG_VBKP_32KCSEL")

    if mux == "SOSC":
        muxOutputFreq = Database.getSymbolValue("core", "SOSC_OUT_FREQ")
    elif mux == "LPRC":
        muxOutputFreq = lprcDefaultFreq
    elif mux == "POSC":
        muxOutputFreq = Database.getSymbolValue("core", "POSC_OUT_FREQ")/500
    else: # FRC will be divided to give 32000
        muxOutputFreq = 32000

    return muxOutputFreq

# Deep Sleep WDT
global dswdtClockDefaultFreq
def dswdtClockDefaultFreq():
    if Database.getSymbolValue("core", "CONFIG_DSWDTOSC") == "LPRC":
        dswdtFreq = Database.getSymbolValue("core", "LPCLK_FREQ")
    else:
        dswdtFreq = VBKP_32KCSEL_MuxOutput()
    return dswdtFreq

global dswdtClockFreqCalc
def dswdtClockFreqCalc(symbol,event):
    symbol.setValue(dswdtClockDefaultFreq())

# RTC Freq
global rtcClockFreqCalc
def rtcClockFreqCalc(symbol, event):
    inputFreq = VBKP_32KCSEL_MuxOutput()

    if Database.getSymbolValue("core", "CONFIG_RTCNTM_CSEL") == "RAW":
        cselOutput = inputFreq
    else: 
        cselOutput = Database.getSymbolValue("core", "LPCLK_FREQ")

    if Database.getSymbolValue("core", "CONFIG_VBKP_DIVSEL") == "DIV_32":
        divselOutput = inputFreq/32
    else: 
        divselOutput = inputFreq/31.25

    if Database.getSymbolValue("core", "CONFIG_VBKP_1KCSEL") == "_32K":
        symbol.setValue(cselOutput)
    else:
        symbol.setValue(int(divselOutput))

# QSPI Freq
global qspiClockFreqCalc
def qspiClockFreqCalc(symbol, event):
    if Database.getSymbolValue("core", "QSPI_CLOCK_ENABLE"):
        symbol.setValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ")))
    else:
        symbol.setValue(0)

# ADCHS Freq
def adchsClockFreqCalc(symbol, event):
    freq = 0
    #Enable SPLL2 for charge pump
    Database.setSymbolValue("core", "SPLLCON_SPLLPOSTDIV2_VALUE", 1)
    adchsClkSrc = Database.getSymbolValue("adchs", "ADCCON3__ADCSEL")

    if Database.getSymbolValue("core", "ADCHS_CLOCK_ENABLE"):
        if adchsClkSrc != None and adchsClkSrc != 1:
            if "REFCLK" in adchs_clock_map[adchsClkSrc]:
                Database.setSymbolValue("core", "CONFIG_SYS_CLK_REFCLK3_ENABLE", True)
            freq = int(Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]))

        if adchsClkSrc == 1:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]) if i.isdigit()])
            freq = 8000000 / int(freqDiv)

    symbol.setValue(freq, 1)

def calculated_clock_frequencies(clk_comp, clk_menu):
    """
    Calculated Clock frequencies Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    """
    global LIST_FWS_MAX_FREQ
    symbolPbFreqList = []
    symbolRefoscFreqList = []

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")

    sys_clk_freq = clk_comp.createStringSymbol("SYS_CLK_FREQ", sym_calc_freq_menu)
    sys_clk_freq.setLabel("System (CPU) Clock Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setLabel("CPU Clock Frequency (Hz)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(node.getAttribute("value"))
    cpu_clk_freq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])
    cpu_clk_freq.setVisible(False)

    POSC_OUT_FREQ = clk_comp.createIntegerSymbol("POSC_OUT_FREQ", sym_calc_freq_menu)
    POSC_OUT_FREQ.setLabel("Primary Oscillator Output Frequency (Hz)")
    POSC_OUT_FREQ.setDefaultValue(poscOutDefaultFreq())
    POSC_OUT_FREQ.setReadOnly(True)
    POSC_OUT_FREQ.setDependencies(poscOutFreqCalc, ["CONFIG_POSCMOD", "CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL"])

    SOSC_OUT_FREQ = clk_comp.createIntegerSymbol("SOSC_OUT_FREQ", sym_calc_freq_menu)
    SOSC_OUT_FREQ.setLabel("Secondary Oscillator Output Frequency (Hz)")
    SOSC_OUT_FREQ.setDefaultValue(soscOutDefaultFreq())
    SOSC_OUT_FREQ.setReadOnly(True)
    SOSC_OUT_FREQ.setDependencies(soscOutFreqCalc, ["CONFIG_LPOSCEN", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])

    # RFPLL frequency
    spll3_rfpll_freq = clk_comp.createIntegerSymbol("SPLL3_RFPLL_FREQ", sym_calc_freq_menu)
    spll3_rfpll_freq.setLabel("SPLL3 Clock (RFPLL) Frequency (Hz)")
    spll3_rfpll_freq.setDefaultValue(spll3DefaultFreq())
    spll3_rfpll_freq.setReadOnly(True)
    spll3_rfpll_freq.setDependencies(spll3OutFreqCalc, ["POSC_OUT_FREQ"])

    spll1_clk_freq = clk_comp.createIntegerSymbol("SPLL1_FREQ", sym_calc_freq_menu)
    spll1_clk_freq.setLabel("SPLL1 Clock Frequency (Hz)")
    spll1_clk_freq.setDefaultValue(spll1DefaultFreq())
    spll1_clk_freq.setReadOnly(True)
    spll1_clk_freq.setDependencies(spll1ClockFreqCalc,["SPLL3_RFPLL_FREQ","SPLLCON_SPLLPOSTDIV1_VALUE"])

    spll2_clk_freq = clk_comp.createIntegerSymbol("SPLL2_FREQ", sym_calc_freq_menu)
    spll2_clk_freq.setLabel("SPLL2 Clock (for ADC Charge Pump) Frequency (Hz)")
    spll2_clk_freq.setDefaultValue(spll2DefaultFreq())
    spll2_clk_freq.setReadOnly(True)
    spll2_clk_freq.setDependencies(spll2ClockFreqCalc,["POSC_OUT_FREQ","SPLL3_RFPLL_FREQ","SPLLCON_SPLLPOSTDIV2_VALUE", "SPLLCON_SPLL_BYP_VALUE"])

    # internal symbol for java to show error
    spll2_clk_max_freq = clk_comp.createIntegerSymbol("SPLL2_FREQ_MAX", sym_calc_freq_menu)
    spll2_clk_max_freq.setLabel("SPLL2 Clock (for ADC Charge Pump) Max Frequency (Hz)")
    spll2_clk_max_freq.setDefaultValue(24000000)
    spll2_clk_max_freq.setReadOnly(True)
    spll2_clk_max_freq.setVisible(False)

     # internal symbol for java to show error
    spll2_clk_min_freq = clk_comp.createIntegerSymbol("SPLL2_FREQ_MIN", sym_calc_freq_menu)
    spll2_clk_min_freq.setLabel("SPLL2 Clock (for ADC Charge Pump) Min Frequency (Hz)")
    spll2_clk_min_freq.setDefaultValue(8000000)
    spll2_clk_min_freq.setReadOnly(True)
    spll2_clk_min_freq.setVisible(False)
	
    lpclk_clk_freq = clk_comp.createIntegerSymbol("LPCLK_FREQ", sym_calc_freq_menu)
    lpclk_clk_freq.setLabel("Low Power Clock (LPCLK) Frequency (Hz)")
    lpclk_clk_freq.setDefaultValue(32000)
    lpclk_clk_freq.setReadOnly(True)
    lpclk_clk_freq.setDependencies(lpclkClockFreqCalc,["CONFIG_LPCLK_MOD","CONFIG_VBKP_32KCSEL", "SOSC_OUT_FREQ", "POSC_OUT_FREQ"])

    # Peripheral Bus clock frequencies
    index = 0
    for ii in pbclkEnNameList:  # this list has  "CONFIG_SYS_CLK_PBCLK"+pbus+"_ENABLE", where pbus is index from atdf file
        # get index value, as need that separately below
        posn = ii.find("_ENABLE")
        clkInstance = ii[posn-1]   # get the pbus number for this instance
        symbolPbFreqList.append([])
        targetName = "CONFIG_SYS_CLK_PBCLK" + clkInstance + "_FREQ"
        symbolPbFreqList[index] = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
        symbolPbFreqList[index].setLabel("Peripheral Bus Clock #"+clkInstance+" Frequency (Hz)")
        targetName = "__PB" + clkInstance + "_DEF_FREQ"
        params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
        paramsChildren = params.getChildren()
        for param in paramsChildren:  # find parameter we are interested in now
            if(param.getAttribute("name") == targetName):
                symbolPbFreqList[index].setDefaultValue(param.getAttribute("value"))
        symbolPbFreqList[index].setReadOnly(True)
        index += 1

     # internal symbol for java to show error
    pbclk3_clk_max_freq = clk_comp.createIntegerSymbol("PBCLK3_FREQ_MAX", sym_calc_freq_menu)
    pbclk3_clk_max_freq.setLabel("PBCLK3 Max Frequency (Hz)")
    pbclk3_clk_max_freq.setDefaultValue(6400000)
    pbclk3_clk_max_freq.setReadOnly(True)
    pbclk3_clk_max_freq.setVisible(False)

    # Reference Clock frequencies
    index = 0
    for ii in refOscList:  # this is a list of oscillator numbers from the atdf file
        symbolRefoscFreqList.append([])
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_FREQ"
        symbolRefoscFreqList[index] = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
        symbolRefoscFreqList[index].setLabel("Reference Clock #"+ii+" Frequency (Hz)")
        symbolRefoscFreqList[index].setVisible(True)
        if ii == "1":   # REFCLK1 is ON by default, so its default freq is also taken from ATDF
            symbolRefoscFreqList[index].setDefaultValue(refclkDefaultFreq(ii))
        else:
            symbolRefoscFreqList[index].setDefaultValue("0")
        symbolRefoscFreqList[index].setReadOnly(True)
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_ENABLE"
        symbolRefoscFreqList[index].setDependencies(updateRefFreq, [targetName])
        index += 1

    wdt_clk_freq = clk_comp.createIntegerSymbol("WDT_CLOCK_FREQUENCY", sym_calc_freq_menu)
    wdt_clk_freq.setLabel("WDT Clock Frequency (Hz)")
    wdt_clk_freq.setDefaultValue(lprcDefaultFreq)
    wdt_clk_freq.setReadOnly(True)
    wdt_clk_freq.setDependencies(wdtClockFreqCalc,["CONFIG_WDTRMCS","SYS_CLK_FREQ"])

    dswdt_clk_freq = clk_comp.createIntegerSymbol("DSWDT_CLOCK_FREQUENCY", sym_calc_freq_menu)
    dswdt_clk_freq.setLabel("Deep Sleep WDT Clock Frequency (Hz)")
    dswdt_clk_freq.setDefaultValue(dswdtClockDefaultFreq())
    dswdt_clk_freq.setReadOnly(True)
    dswdt_clk_freq.setDependencies(dswdtClockFreqCalc,["CONFIG_DSWDTOSC","LPCLK_FREQ", "CONFIG_VBKP_32KCSEL"])

    sercomSlowClockFrequency= clk_comp.createIntegerSymbol("SERCOM_SLOW_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sercomSlowClockFrequency.setLabel("SERCOM Slow Clock Frequency")
    sercomSlowClockFrequency.setDefaultValue(Database.getSymbolValue("core", "LPCLK_FREQ"))
    sercomSlowClockFrequency.setReadOnly(True)
    sercomSlowClockFrequency.setDependencies(item_update, ["LPCLK_FREQ"])

def find_lsb_position(field):
    # Take a field, and return the least significant bit position.  Range: 0-31
    if(field[:2] == "0x"):
        field_int = int(field,16)
    else:
        field_int = int(field)
    for i in range(0,31):
        if(field_int & 1 == 1):
            break
        else:
            field_int  = field_int>>1
    return i

def find_max_min(node):
    # Finds the maximum and minimum values from atdf file for a given <value-group >
    children = node.getChildren()
    maxval = 0
    minval = 0xffffffff

    for ii in range(0,len(children)):
        val = children[ii].getAttribute("value")
        if(val[:2] == "0x"):
            test = int(val,16)
        else:
            test = int(val)
        if(maxval < test):
            maxval = test
        if(minval > test):
            minval = test
    return maxval, minval

def getBitMask(node, bitfield):
    '''
    returns mask value for given bitfield

    Input:
        node - node of <register ...>
        bitfield - name of bitfield needing mask from

    Returns:
        string, mask value of bitfield
    '''
    children = node.getChildren()
    for ii in children:
        if(ii.getAttribute('name') == bitfield):
            return ii.getAttribute('mask')
    return ''  # should never get here

global updateSPLLCon

def updateSPLLCon(symbol, event):
    # updates the register SPLLCON value based on any of its bitfield values changing
    startVal = symbol.getValue()  # value for the register SPLLCON
    for ii in spllcon_symbols:
        if(ii['name'] == event['id'].split('SPLLCON_')[1].split('_VALUE')[0]):
            maskval = ii['symmaskname'].getValue()
            if(maskval.find('0x')!= -1):
                mask = int(maskval,16)
            else:
                mask = int(maskval)
            startVal &= ~mask
            bitPosn = 0
            while((mask & (1<<bitPosn)) == 0):
                bitPosn += 1
            if(len(ii['keyvalbuf']) > 0):  # bitfield which has <value-group ..> section associated with it
                startVal |= int(ii['keyvalbuf'][event['value']]) << bitPosn
            else:   # integer bitfield (no <value-group ..> section associated with it)
                startVal |= int(event['value']) << bitPosn

    symbol.setValue(startVal,2)

global updateOSCCon

def updateOSCCon(symbol, event):
    # updates OSCCON register value based on any of its bitfield values changing
    startVal = symbol.getValue()  # value for the register SPLLCON
    for ii in osccon_symbols:
        if(ii['name'] == event['id'].split('OSCCON_')[1].split('_VALUE')[0]):
            maskval = ii['symmaskname'].getValue()
            if(maskval.find('0x')!= -1):
                mask = int(maskval,16)
            else:
                mask = int(maskval)
            startVal &= ~mask
            bitPosn = 0
            while((mask & (1<<bitPosn)) == 0):
                bitPosn += 1
            if(len(ii['keyvalbuf']) > 0):  # bitfield which has <value-group ..> section associated with it
                startVal |= int(ii['keyvalbuf'][event['value']]) << bitPosn
            else:   # integer bitfield (no <value-group ..> section associated with it)
                startVal |= int(event['value']) << bitPosn
            if(ii['name']=='FRCDIV'):
                frcdivBfValSym.setValue(int(ii['keyvalbuf'][event['value']]))
    symbol.setValue(startVal,2)


def scan_atdf_for_spllcon_fields(component, parentMenu, regNode):
    '''
    This creates all the symbols for SPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''
    spllconRegName = component.createStringSymbol("SPLLCON_REG", parentMenu)
    spllconRegName.setVisible(False)
    spllconRegName.setDefaultValue(regNode.attrib["name"])

    global spllcon_symbols
    spllcon_symbols = [
                        {'name':'SPLLPWDN', 'symmaskname':'spllcon_spllpwdn_mask', 'symvaluename':'spllcon_spllpwdn_val', 'keyvalbuf':'spllpwdn', 'visible':'False'},
                        {'name':'SPLLPOSTDIV1', 'symmaskname':'spllcon_spllpostdiv1_mask', 'symvaluename':'spllcon_spllpostdiv1_val', 'keyvalbuf':'spllpostdiv1', 'visible':'True', 'min':'1', 'max':'255'},
                        {'name':'SPLL_BYP', 'symmaskname':'spllcon_spllbyp_mask', 'symvaluename':'spllcon_spllbyp_val', 'keyvalbuf':'spllbyp', 'visible':'True'},
                        {'name':'SPLLPOSTDIV2', 'symmaskname':'spllcon_spllpostdiv2_mask', 'symvaluename':'spllcon_spllpostdiv2_val', 'keyvalbuf':'spllpostdiv2', 'visible':'True', 'min':'1', 'max':'15'}, 
                        {'name':'SPLLFLOCK', 'symmaskname':'spllcon_spllflock_mask', 'symvaluename':'spllcon_spllflock_val', 'keyvalbuf':'spllflock', 'visible':'False'},
                        {'name':'SPLLRST', 'symmaskname':'spllcon_spllrst_mask', 'symvaluename':'spllcon_spllrst_val', 'keyvalbuf':'spllrst', 'visible':'False'}]

    dependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in spllcon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('SPLLCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])

                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it

                    base = ATDF.getNode(CRUmoduleStart)
                    theNodes = base.getChildren()
                    for j in theNodes:
                        if(j.getAttribute('name') == bitfield_tag.attrib["values"]):
                            where = j


                    valueNodeList = where.getChildren()
                    #ii['symvaluename'] = component.createComboSymbol('SPLLCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'] = component.createKeyValueSetSymbol('SPLLCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setOutputMode("Value")
                    ii['symvaluename'].setDisplayMode("Key")

                    for i in range(0, len(valueNodeList)):
                        key = valueNodeList[i].getAttribute("name")
                        description = valueNodeList[i].getAttribute("caption")
                        value = valueNodeList[i].getAttribute("value")
                        ii['symvaluename'].addKey(key, value , description)

                    ii['symvaluename'].setDefaultValue(_get_default_index(clkRegGrp_SPLLCON, ii['name'], where))
                else:   # numeric bitfield (no <value-group ..> section associated with it)
                    ii['symvaluename'] = component.createIntegerSymbol('SPLLCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_SPLLCON, ii['name'], 'None'))
                    if('min' in ii.keys()):
                        ii['symvaluename'].setMin(int(ii['min']))
                    if('max' in ii.keys()):
                        ii['symvaluename'].setMax(int(ii['max']))
                if('readonly' in ii.keys()):
                    ii['symvaluename'].setReadOnly(ii['readonly'])
                ii['symvaluename'].setLabel(bitfield_tag.attrib['caption'])
                if(ii['visible']=='True'):
                    ii['symvaluename'].setVisible(True)
                else:
                    ii['symvaluename'].setVisible(False)

                dependencyList.append('SPLLCON_'+ii['name'].upper()+'_VALUE')

    # get initial value of SPLLCON register from 'initval' field in atdf file and then add dependency
    symbolSpllconValue = component.createHexSymbol("SPLLCON_VALUE", parentMenu)
    symbolSpllconValue.setVisible(False)
    initialSpllconVal = int((clkRegGrp_SPLLCON.getAttribute('initval')),16)
    symbolSpllconValue.setDefaultValue(initialSpllconVal)
    symbolSpllconValue.setDependencies(updateSPLLCon, dependencyList)

def scan_atdf_for_osccon_fields(component, parentMenu, regNode):
    '''
    This creates all the symbols for OSCCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''

    global frcdivBfValSym
    oscconRegName = component.createStringSymbol("OSCCON_REG", parentMenu)
    oscconRegName.setVisible(False)
    oscconRegName.setDefaultValue(regNode.attrib["name"])

    global osccon_symbols
    osccon_symbols = [
                        {'name':'OSWEN', 'symmaskname':'osccon_oswen_mask', 'symvaluename':'osccon_oswen_val', 'keyvalbuf':'oswen', 'visible':'False'},
                        {'name':'SOSCEN', 'symmaskname':'osccon_soscen_mask', 'symvaluename':'osccon_soscen_val', 'keyvalbuf':'soscen', 'visible':'True'},
                        {'name':'CF', 'symmaskname':'osccon_cf_mask', 'symvaluename':'osccon_cf_val', 'keyvalbuf':'cf', 'visible':'False'},
                        {'name':'SLPEN', 'symmaskname':'osccon_slpen_mask', 'symvaluename':'osccon_slpen_val', 'keyvalbuf':'slpen', 'visible':'False'},
                        {'name':'CLKLOCK', 'symmaskname':'osccon_clklock_mask', 'symvaluename':'osccon_clklock_val', 'keyvalbuf':'clklock', 'visible':'False'},
                        {'name':'NOSC', 'symmaskname':'osccon_nosc_mask', 'symvaluename':'osccon_nosc_val', 'keyvalbuf':'nosc', 'visible':'True'}, # no fuse for it - option made available to user here
                        {'name':'WAKE2SPD', 'symmaskname':'osccon_wake2spd_mask', 'symvaluename':'osccon_wake2spd_val', 'keyvalbuf':'wake2spd', 'visible':'False'},
                        {'name':'DRMEN', 'symmaskname':'osccon_drmen_mask', 'symvaluename':'osccon_drmen_val', 'keyvalbuf':'drmen', 'visible':'False'},
                        {'name':'FRCDIV', 'symmaskname':'osccon_frcdiv_mask', 'symvaluename':'osccon_frcdiv_val', 'keyvalbuf':'frcdiv', 'visible':'True'}]
    dependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in osccon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('OSCCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])

                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it
                    where = _get_bitfield_info(CRUmoduleStart, ii['keyvalbuf'], bitfield_tag.attrib["values"])
                    ii['symvaluename'] = component.createComboSymbol('OSCCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_OSCCON, ii['name'], where))
                    if(ii['name']=='SOSCEN'):   # on reset, this field is set to DEVCFG4:SOSCEN bitfield
                        targetSym = 'CONFIG_SOSCEN'
                        soscenVal = Database.getSymbolValue("core",targetSym)
                        for jj in ii['keyvalbuf']:
                            if(jj == soscenVal):
                                ii['symvaluename'].setDefaultValue(jj)
                        ii['symvaluename'].setDependencies(item_update, ["core."+targetSym])  # update SOSCEN whenever user updates DEVCFG4:SOSCEN
                else:   # numeric bitfield (no <value-group ..> section associated with it)
                    ii['symvaluename'] = component.createIntegerSymbol('OSCCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_OSCCON, ii['name'], 'None'))
                    if('min' in ii.keys()):
                        ii['symvaluename'].setMin(int(ii['min']))
                    if('max' in ii.keys()):
                        ii['symvaluename'].setMax(int(ii['max']))
                ii['symvaluename'].setLabel(bitfield_tag.attrib['caption'])
                if(ii['visible']=='True'):
                    ii['symvaluename'].setVisible(True)
                else:
                    ii['symvaluename'].setVisible(False)
                if(ii['name']=='FRCDIV'):
                    frcdivBfValSym = component.createIntegerSymbol('SYS_CLK_FRCDIV',None)
                    frcdivBfValSym.setVisible(False)
                    frcdivBfValSym.setDefaultValue(int(ii['keyvalbuf'][(_get_default_value(clkRegGrp_OSCCON, ii['name'], where))]))

                dependencyList.append('OSCCON_'+ii['name'].upper()+'_VALUE')

    # get initial value of OSCCON register from 'initval' field in atdf file
    symbolOscconValue = component.createHexSymbol("OSCCON_VALUE", parentMenu)
    symbolOscconValue.setVisible(False)
    initialOscconVal = int((clkRegGrp_OSCCON.getAttribute('initval')),16)
    symbolOscconValue.setDefaultValue(initialOscconVal)
    symbolOscconValue.setDependencies(updateOSCCon, dependencyList)

if __name__ == "__main__":

    global refOscList
    global symbolPbRegMaskLsb
    global symbolPbRegMask
    global symbolPbOnMask
    global symbolRoselMaskList
    global symbolRoselMaskLsbList
    global sourceSymbolList
    global symbolDivswenMask
    global symbolRodivValueList
    global symbolRodivMask
    global symbolRodivMaskLsb
    global roselmap
    global symbolPbdivList
    global symbolRotrimmaskLsb
    global symbolRotrimMask
    global per_divider
    global indexSymbolMap
    indexSymbolMap = defaultdict(list)

    # divider value:  get values/keys from atdf
    per_divider = {}
    node = clkValGrp_OSCCON__FRCDIV.getChildren()
    for ii in range(0,len(node)):
        argterm = node[ii].getAttribute("value")
        if(argterm.find('0x') != -1):
            argval = argterm[2:]
        else:
            argval = argterm
        per_divider[node[ii].getAttribute("name")] = argval

    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_PIC32CX_BZ", None)
    SYM_CLK_MENU.setLabel("Clock Menu")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    # Menu items listed here
    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here should be ideally configured using the Clock Configurator ****")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    CLK_MANAGER_SELECT.setDefaultValue("clk_pic32cx_bz:MZClockModel")

    # parse atdf file to get key parameters
    atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
    atdf_file = open(atdf_file_path, "r")
    atdf_content = ElementTree.fromstring(atdf_file.read())
    pbList = []
    symbolName = []
    symbolPbRegMaskLsb = []     # for REFOxCON:PBxDIV field bit shift, contains list of {symbolName, bus number}
    symbolPbRegMask = []        # for REFOxCON:PBxDIV mask, contains list of {symbolName, bus number}
    symbolPbOnMask = []         # for REFOxCON:ON mask, contains list of {symbolName, bus number}
    symbolRoselMaskList = []    # for PBxDIV:ROSEL mask, contains list of {symbolName, bus number}
    symbolRoselMaskLsbList = [] # for PBxDIV:ROSEL field bit shift, contains list of {symbolName, bus number}
    symbolDivswenMask = []      # for PBxDIV:DIVSWEN mask, contains list of {symbolName, bus number}
    symbolRodivMask = []        # for REFOxCON:RODIV mask, contains list of {symbolName, clock number}
    symbolRodivMaskLsb = []     # for REFOxCON:RODIV field bit shift, contains list of {symbolName, clock number}
    symbolRotrimmaskLsb = []    # for REFOxTRIM:ROTRIM field bit shift, contains list of {symbolName, clock number)
    symbolRotrimMask = []       # for REFOxTRIM:ROTRIM mask, contains list of {symbolName, clock number)
    refOscList = []
    index = 0

    CLK_CFG_SETTINGS = coreComponent.createMenuSymbol("ClkCfgSettings", SYM_CLK_MENU)
    CLK_CFG_SETTINGS.setDependencies(enableMenu, ["ClkSvcMenu"])
    CLK_CFG_SETTINGS.setLabel("Clock Configurator Settings")
    CLK_CFG_SETTINGS.setDescription("Various Clock System Settings")
    CLK_CFG_SETTINGS.setVisible(True)

    SPLL_CFG_SETTINGS = coreComponent.createMenuSymbol("SpllCfgSettings", CLK_CFG_SETTINGS)
    SPLL_CFG_SETTINGS.setDependencies(enableMenu, ["ClkSvcMenu"])
    SPLL_CFG_SETTINGS.setLabel("System PLL Configurator Settings")
    SPLL_CFG_SETTINGS.setDescription("Various PLL System Settings")
    SPLL_CFG_SETTINGS.setVisible(True)

    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):
                if("SPLLCON" == register_tag.attrib["name"]):
                    scan_atdf_for_spllcon_fields(coreComponent, SPLL_CFG_SETTINGS, register_tag)
                if("OSCCON" == register_tag.attrib["name"]):
                    scan_atdf_for_osccon_fields(coreComponent, CLK_CFG_SETTINGS, register_tag)
                

                #looking for PB1DIV, PB2DIV, ... (for making menu entries - further down, and ftl-related symbols)
                if ("PB" in register_tag.attrib["name"]) and ("DIV" == register_tag.attrib["name"][-3:]):
                    clockNum = register_tag.attrib["name"][2]  # get the clock number (char position 2 of field)
                    pbList.append(clockNum)
                    for bitfield_tag in register_tag.iter("bitfield"):
                        if(bitfield_tag.attrib["name"] == "PBDIV"):  # PBDIV field
                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("PBREGMASK"+clockNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPbRegMask.append({'symbol':symbolName[index], 'index':clockNum})
                            index += 1
                            # this is for bit shift for PBxDIV field

                            symbolName.append([])
                            lsb = find_lsb_position(bitfield_tag.attrib["mask"])
                            symbolName[index] = coreComponent.createStringSymbol("PBREGMASKLSB"+clockNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(str(lsb))
                            symbolPbRegMaskLsb.append({'symbol':symbolName[index], 'index':clockNum})
                            index += 1

                        elif(bitfield_tag.attrib["name"] == "PBDIVON"):  # ON field mask
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("PBONMASK"+clockNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPbOnMask.append({'symbol':symbolName[index], 'index':clockNum})
                            index += 1
                    # this is for actual register name - put  into a symbol for ftl file retrieval
                    symbolName.append([])

                    symbolName[index] = coreComponent.createStringSymbol("PBREGNAME"+clockNum, None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"])
                    index += 1
                    symbolName.append([])
                    symbolName[index] = coreComponent.createStringSymbol("PBREGNAME"+clockNum+"_CLR", None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"]+"CLR")
                    index += 1
                    symbolName.append([])
                    symbolName[index] = coreComponent.createStringSymbol("PBREGNAME"+clockNum+"_SET", None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"]+"SET")
                    index += 1

                #looking for REFO1CON, REFO2CON, ...
                if ("REFO" in register_tag.attrib["name"]) and ("CON" == register_tag.attrib["name"][-3:]):
                    refoscNum = register_tag.attrib["name"][4]  # get the clock number (char position 4 of REFOxCON field in atdf file)
                    refOscList.append(refoscNum)
                    symbolName.append([])
                    symbolName[index] = coreComponent.createStringSymbol("REFCON"+refoscNum+"REG", None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"])
                    index += 1
                    for bitfield_tag in register_tag.iter("bitfield"):
                        if(bitfield_tag.attrib["name"] == "ROSEL"):  # ROSEL field
                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("ROSELMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolRoselMaskList.append({'symbol':symbolName[index],'index':refoscNum})
                            index += 1
                            # this is for bit shift for ROSEL field
                            lsb = find_lsb_position(bitfield_tag.attrib["mask"])
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("ROSELMASKLSB"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(str(lsb))
                            symbolRoselMaskLsbList.append({'symbol':symbolName[index],'index':refoscNum})
                            index += 1
                        elif(bitfield_tag.attrib["name"] == "OE"):  # OE field
                            # get mask of this field - needed in ftl file
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("REFOCON_OEMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            index += 1
                        elif(bitfield_tag.attrib["name"] == "DIVSWEN"):  # DIVSWEN field
                            # get mask of this field - needed in ftl file
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("REFOCON_DIVSWENMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolDivswenMask.append({'symbol':symbolName[index],'index':refoscNum})
                            index += 1
                        elif(bitfield_tag.attrib["name"] == "RODIV"):  # RODIV field
                            # get mask of this field - needed in ftl file
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("REFOCON_RODIVMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolRodivMask.append({'symbol':symbolName[index], 'index':refoscNum})
                            index += 1
                            # this is for bit shift for ROSEL field
                            lsb = find_lsb_position(bitfield_tag.attrib["mask"])
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("RODIVMASKLSB"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(str(lsb))
                            symbolRodivMaskLsb.append({'symbol':symbolName[index], 'index':refoscNum})
                            index += 1
                        elif(bitfield_tag.attrib["name"] == "ON"):  # ON field
                            # get mask of this field - needed in ftl file
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("REFOCON_ONMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            index += 1

                # looking for REFO1TRIM, REFO2TRIM, ... in atdf file
                if ("REFO" in register_tag.attrib["name"]) and ("TRIM" == register_tag.attrib["name"][-4:]):
                    refoscNum = register_tag.attrib["name"][4]  # get the clock number (char position 4 of REFOxCON field in atdf file)
                    symbolName.append([])
                    symbolName[index] = coreComponent.createStringSymbol("REFTRIM"+refoscNum+"REG", None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"])
                    index += 1
                    for bitfield_tag in register_tag.iter("bitfield"):
                        if(bitfield_tag.attrib["name"] == "ROTRIM"):  # ROTRIM field
                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("ROTRIMMASK"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolRotrimMask.append({'symbol':symbolName[index],'index':refoscNum})
                            index += 1
                            # this is for bit shift for ROSEL field
                            lsb = find_lsb_position(bitfield_tag.attrib["mask"])
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("ROTRIMMASKLSB"+refoscNum, None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(str(lsb))
                            symbolRotrimmaskLsb.append({'symbol':symbolName[index],'index':refoscNum})
                            index += 1

    # ftl file will use this to know how many times to loop through its code (once per reference osc found in atdf file)
    symbolLen = coreComponent.createIntegerSymbol("NUM_REFOSC_ELEMENTS", None)
    symbolLen.setVisible(False)
    symbolLen.setDefaultValue(len(refOscList))
    # end of generation of ftl file-related symbols (values derived from atdf file)

    # Hiding temperature range selection feature for now - no such specification mentioned
    TEMP_RANGE = coreComponent.createKeyValueSetSymbol("CONFIG_TEMPERATURE_RANGE", CLK_CFG_SETTINGS)
    TEMP_RANGE.setLabel("Operating Temperature Range")
    TEMP_RANGE.setDescription("Maximum allowed System Clock Frequency will depend on selected Temperature Range")
    TEMP_RANGE.setVisible(False)
    TEMP_RANGE.setOutputMode("Value")
    TEMP_RANGE.setDisplayMode("Description")

    max_clk_freq_for_selected_temp = coreComponent.createIntegerSymbol("MAX_CLK_FREQ_FOR_SELECTED_TEMP_RANGE", CLK_CFG_SETTINGS)
    max_clk_freq_for_selected_temp.setLabel("Max System Clock Frequency (HZ) For Selected Temperature")
    max_clk_freq_for_selected_temp.setReadOnly(True)
    max_clk_freq_for_selected_temp.setVisible(False)

    TEMP_RANGE.addKey("RANGE1", "1", "-40C to +85C, DC to 64 MHz")
    TEMP_RANGE.setDefaultValue(0)
    TEMP_RANGE.setReadOnly(True)
    max_clk_freq_for_selected_temp.setDefaultValue(64000000)

    # keep in here in case part later has 2 temerature ranges and 2 upper frequencies
    max_clk_freq_for_selected_temp.setDependencies(updateMaxFreq, ["CONFIG_TEMPERATURE_RANGE"])

    # secondary oscillator enable
    soscen = {}
    _get_bitfield_names(clkValGrp_OSCCON__SOSCEN, soscen)
    SOSC_EN_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_CONFIG_SOSCEN", CLK_CFG_SETTINGS, sorted(soscen.keys()))
    SOSC_EN_SETTING.setLabel("Secondary oscillator enable")
    SOSC_EN_SETTING.setDescription(clkValGrp_OSCCON__SOSCEN.getAttribute('caption'))
    SOSC_EN_SETTING.setVisible(False)

    # now create the menus for all peripheral buses present in this part
    global pbclkEnNameList
    global roselSymbolList
    global refconval
    global symbolRoselValueList
    global refotrimval
    global symbolrefotrimval
    global rotrimSymbolList
    global rslpSymbolList
    global sidlSymbolList
    global symbolRotrimUserVal
    global roselMap
    pbclkEnNameList = []
    enSymbolList = []
    oeSymbolList = []
    sourceSymbolList = []
    roselSymbolList = []
    rodivSymbolList = []
    rotrimSymbolList = []
    rslpSymbolList = []
    sidlSymbolList = []
    refconval = []
    symbolRoselValueList = []
    symbolRodivValueList = []
    symbolPbdivList = []        # for PBxDIV:PBDIV contains list of {symbolName, clock number}
    symbolPbdiv = []
    refotrimval = []
    symbolrefotrimval = []
    symbolRotrimUserVal = []
    triggerdepList = []
    sym_peripheral_clock_enable = []

    # Peripheral Bus symbol creation
    # pbList was all Peripheral Bus clock indices found in the atdf file.
    pbindex = 0
    for pbus in pbList:
        symbolEnId = "CONFIG_SYS_CLK_PBCLK"+pbus+"_ENABLE"
        labelEnVal = "Enable Peripheral Clock Bus #"+pbus
        symbolDivId = "CONFIG_SYS_CLK_PBDIV"+pbus
        labelDivVal = "Peripheral Clock Bus #"+pbus+" Divisor (1-128)"
        symbolEnName = coreComponent.createBooleanSymbol(symbolEnId, CLK_CFG_SETTINGS)
        pbclkEnNameList.append(symbolEnId)
        symbolEnName.setLabel(labelEnVal)
        if(pbus=='1'):
            symbolEnName.setReadOnly(True)  # cannot disable peripheral bus 1
        symbolEnName.setDefaultValue(True)

        # PBDIV field
        symbolDivName = coreComponent.createIntegerSymbol(symbolDivId, symbolEnName)
        if(pbus!='1'):  # cannot disable peripheral bus 1
            symbolDivName.setDependencies(enableMenu, [symbolEnId])
        symbolDivName.setLabel(labelDivVal)
        symbolDivName.setMin(1)
        symbolDivName.setMax(128)
        # get defaults from atdf file

        regname = "PB"+str(pbus)+"DIV"
        children = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]').getChildren()
        bitfield = 'PBDIV'
        for ii in children:
            if(ii.getAttribute('name') == regname):
                if pbus != "3":
                    symbolDivName.setDefaultValue( _get_default_value(ii, bitfield, 'None'))
                else:
                    symbolDivName.setDefaultValue(10)
        symbolDivName.setVisible(True)
        symbolPbdivList.append({"symbol":symbolDivName, "index":pbus})

        # Setting for PBxDIV to use in ftl file - for when a Peripheral Bus has been enabled
        symbolPbdiv.append([])
        symbolPbdiv[pbindex] = coreComponent.createStringSymbol("PB"+pbus+"DIV_VALUE", None)
        symbolPbdiv[pbindex].setVisible(False)
        symbolPbdiv[pbindex].setDefaultValue(set_pbdiv_value(pbus))
        symbolPbdiv[pbindex].setDependencies(pbdiv_update,[symbolDivId])  # depends on when user changes CONFIG_SYS_CLK_PBDIVx
        pbindex += 1

    # Reference Clock symbol creation
    listIndex = 0
    for clk in refOscList:
        enSymbolList.append([])
        oeSymbolList.append([])
        sourceSymbolList.append([])
        roselSymbolList.append([])
        rodivSymbolList.append([])
        rotrimSymbolList.append([])
        rslpSymbolList.append([])
        sidlSymbolList.append([])

        enSymId = "CONFIG_SYS_CLK_REFCLK"+clk+"_ENABLE"
        enSymbolList[listIndex] = coreComponent.createBooleanSymbol(enSymId, CLK_CFG_SETTINGS)
        enSymbolList[listIndex].setLabel("Enable Reference Clock "+clk)
        enSymbolList[listIndex].setDescription("Sets whether to have reference clock enabled")
        if clk == "1": # enable refclk1 by default as this clock will be used by peripherals by default
            enSymbolList[listIndex].setDefaultValue(True)
        else:
            enSymbolList[listIndex].setDefaultValue(False)
        sym_peripheral_clock_enable.append(enSymId) # needed for PMD manipulation

        # output enable of ref clk
        if clk in ["1", "2", "3", "4"]: #since REFO5 and REFO6 pins are not available, remove corresponding OE symbols also
            oeSymId = "CONFIG_SYS_CLK_REFCLK"+clk+"_OE"
            oeSymbolList[listIndex] = coreComponent.createBooleanSymbol(oeSymId, enSymbolList[listIndex])
            oeSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
            oeSymbolList[listIndex].setLabel("Reference Clock "+clk+" Output Enable")
            oeSymbolList[listIndex].setDescription("Sets whether to have reference clock 1 output enable")
            oeSymbolList[listIndex].setReadOnly(False)
            oeSymbolList[listIndex].setDefaultValue(False)
            oeSymbolList[listIndex].setVisible(False)

        # ROSEL
        srcSymId = "CONFIG_SYS_CLK_REFCLK_SOURCE" + clk
        labelName = "clkValGrp_REFO" + clk + "CON__ROSEL"
        roselMap = {}
        roselsrc = {}
        _get_bitfield_names(clkValGrp_REFO1CON__ROSEL, roselsrc)
        sourceSymbolList[listIndex] = coreComponent.createComboSymbol(srcSymId, enSymbolList[listIndex], sorted(roselsrc.keys()))
        sourceSymbolList[listIndex].setLabel("Reference Clock Source Select ROSEL")
        sourceSymbolList[listIndex].setDescription(clkValGrp_REFO1CON__ROSEL.getAttribute('caption'))
        sourceSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
        sourceSymbolList[listIndex].setDefaultValue("SPLL1")
        sourceSymbolList[listIndex].setVisible(False)
        symbolRoselValueList.append({'symbol':sourceSymbolList[listIndex],'index':clk})
        for ii in roselsrc:
            roselMap[ii] = roselsrc[ii]

        # RODIV
        # pull min, max values out of atdf file
        maxValue, minValue = find_max_min(clkValGrp_REFO1CON__RODIV)
        rodivSymId = "CONFIG_SYS_CLK_RODIV"+clk
        rodivSymbolList[listIndex] = coreComponent.createIntegerSymbol(rodivSymId, enSymbolList[listIndex])
        rodivSymbolList[listIndex].setLabel("Select Reference Clock Output Divider RODIV")
        rodivSymbolList[listIndex].setDependencies(updateRODIVmin, [enSymId, srcSymId])
        rodivSymbolList[listIndex].setMin(minValue)
        rodivSymbolList[listIndex].setMax(maxValue)
        rodivSymbolList[listIndex].setDefaultValue(0)
        rodivSymbolList[listIndex].setVisible(False)
        symbolRodivValueList.append({'symbol':rodivSymbolList[listIndex],'index':clk})

        # ROTRIM
        maxValue, minValue = find_max_min(clkValGrp_REFO1TRIM__ROTRIM)
        rotrimSymId = "CONFIG_SYS_CLK_ROTRIM"+clk
        rotrimSymbolList[listIndex] = coreComponent.createIntegerSymbol(rotrimSymId, enSymbolList[listIndex])
        rotrimSymbolList[listIndex].setLabel("Select Reference Clock Output Trim Value ROTRIM")
        rotrimSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
        rotrimSymbolList[listIndex].setMin(minValue)
        rotrimSymbolList[listIndex].setMax(maxValue)
        rotrimSymbolList[listIndex].setDefaultValue(0)
        rotrimSymbolList[listIndex].setVisible(False)
        symbolRotrimUserVal.append({'symbol':rotrimSymbolList[listIndex],'index':clk})

        #RSLP
        rslpSymId = "CONFIG_SYS_CLK_REFCLK_RSLP" + clk
        rslpSymbolList[listIndex] = coreComponent.createBooleanSymbol(rslpSymId, enSymbolList[listIndex])
        rslpSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
        rslpSymbolList[listIndex].setLabel("Reference Clock "+clk+" Run in Sleep Mode")
        rslpSymbolList[listIndex].setDescription("Sets whether to run the reference clock 1 output in sleep mode or not")
        rslpSymbolList[listIndex].setReadOnly(False)
        rslpSymbolList[listIndex].setDefaultValue(False)
        rslpSymbolList[listIndex].setVisible(False)

        #SIDL
        sidlSymId = "CONFIG_SYS_CLK_REFCLK_SIDL" + clk
        sidlSymbolList[listIndex] = coreComponent.createBooleanSymbol(sidlSymId, enSymbolList[listIndex])
        sidlSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
        sidlSymbolList[listIndex].setLabel("Reference Clock "+clk+" Run in Idle Mode")
        sidlSymbolList[listIndex].setDescription("Sets whether to run the reference clock 1 output in idle mode or not")
        sidlSymbolList[listIndex].setReadOnly(False)
        sidlSymbolList[listIndex].setDefaultValue(False)
        sidlSymbolList[listIndex].setVisible(False)

        # python-computed REFOxCON register setting to use in ftl file
        refconval.append([])
        refconval[listIndex] = coreComponent.createStringSymbol("REFOCON"+clk+"_VALUE", None)
        refconval[listIndex].setVisible(False)
        refconval[listIndex].setDefaultValue(set_refocon_value(clk))
        # change based on CONFIG_SYS_CLK_REFCLK_ROSELx or CONFIG_SYS_CLK_RODIVx changes
        refconval[listIndex].setDependencies(refocon_update, [srcSymId, rodivSymId, sidlSymId, rslpSymId])

        # python-computed REFOxTRIM register setting to use in ftl file
        refotrimval.append([])
        refotrimval[listIndex] = coreComponent.createStringSymbol("REFO"+clk+"TRIM_VALUE", None)
        refotrimval[listIndex].setVisible(False)
        refotrimval[listIndex].setDefaultValue(set_refotrim_value(clk))
        # change based on CONFIG_SYS_CLK_ROTRIMx changes
        refotrimval[listIndex].setDependencies(refotrim_update, [rotrimSymId])
        symbolrefotrimval.append({"symbol":refotrimval[listIndex], "index":clk})

        listIndex += 1  # needs to be at end of for loop

    # primary oscillator frequency
    POSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL", CLK_CFG_SETTINGS)
    POSC_IN_FREQ.setLabel("Primary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__POSC_DEF_FREQ"]')
    POSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))
    POSC_IN_FREQ.setReadOnly(True)

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    SOSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))

    # REFCLKI pin frequency
    REFCLKI_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_REFCLKI_PIN", CLK_CFG_SETTINGS)
    REFCLKI_IN_FREQ.setLabel("REFCLKI Input Pin Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__REFCLKI_DEF_FREQ"]')
    newRefclkiFreq = node.getAttribute("value")
    REFCLKI_IN_FREQ.setDefaultValue(int(newRefclkiFreq))

    # FRC default frequency
    FRC_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_FRC", CLK_CFG_SETTINGS)
    FRC_FREQ.setVisible(False)
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__FRC_DEF_FREQ"]')
    FrcFreq = node.getAttribute("value")
    FRC_FREQ.setDefaultValue(int(FrcFreq))

    # LPRC default frequency
    global lprcDefaultFreq
    lprcDefaultFreq = 32768
    LPRC_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_LPRC", CLK_CFG_SETTINGS)
    LPRC_FREQ.setVisible(False)
    LPRC_FREQ.setDefaultValue(lprcDefaultFreq)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU)

    # Peripheral Channel Configuration menu
    gclkPeriChannel_menu = coreComponent.createMenuSymbol("GCLK_PERI_MENU",SYM_CLK_MENU)
    gclkPeriChannel_menu.setLabel("Peripheral Channel Configuration")

    # get peripheral clock index (or GCLK ID) information from ATDF
    atdfFilePath = join(Variables.get("__DFP_PACK_DIR") , "atdf" , Variables.get("__PROCESSOR") + ".atdf")

    try:
        atdfFile = open(atdfFilePath, "r")
    except:
        Log.writeInfoMessage("clk.py peripheral clock: Error!!! while opening atdf file")

    atdfContent = ElementTree.fromstring(atdfFile.read())

    maxGCLKId = 0
    # parse atdf xml file to get instance name
    # for the peripheral which has gclk id
    for peripheral in atdfContent.iter("module"):
        for instance in peripheral.iter("instance"):
            for param in instance.iter("param"):
                if "GCLK_ID" in param.attrib["name"]:

                    indexID = param.attrib["value"]
                    symbolValue = instance.attrib["name"] + param.attrib["name"].split("GCLK_ID")[1]
                    symbolId = "GCLK_ID_" + str(indexID)
                    indexSymbolMap[symbolId].append(symbolValue)

                    if maxGCLKId < int(indexID):
                        maxGCLKId = int(indexID)

    PeriGenRegCount = maxGCLKId/8 + 1
    # for FTL
    gclkSym_PeriGenRegCount = coreComponent.createIntegerSymbol("PER_GEN_REG_COUNT", SYM_CLK_MENU)
    gclkSym_PeriGenRegCount.setVisible(False)
    gclkSym_PeriGenRegCount.setDefaultValue(int(PeriGenRegCount))

    channelMap = {}
    for key in indexSymbolMap.keys():
        index=key.split("GCLK_ID_")[1]
        channelMap[int(index)]=key

    Gclk_Channel_CFGPCLKGEN_list = []
    for index in sorted(channelMap.iterkeys()):
        key=channelMap[index]
        name = indexSymbolMap.get(key)
        name = " ".join(name)

        #GCLK Peripheral Channel Enable
        clkSymPeripheral = coreComponent.createBooleanSymbol(key + "_CHEN", gclkPeriChannel_menu)
        clkSymPeripheral.setLabel("Peripheral Channel " + str(index) + " Clock Enable")
        clkSymPeripheral.setDefaultValue(False)
        Gclk_Channel_CFGPCLKGEN_list.append(key + "_CHEN")

        #GCLK Peripheral Channel Name
        gclkSym_PERCHANNEL_NAME = coreComponent.createStringSymbol(key + "_NAME", clkSymPeripheral)
        gclkSym_PERCHANNEL_NAME.setLabel("Peripheral")
        gclkSym_PERCHANNEL_NAME.setReadOnly(True)
        gclkSym_PERCHANNEL_NAME.setDefaultValue(name)

        #Peripheral Channel Generator Selection
        gclkSym_PCHCTRL_GEN = coreComponent.createKeyValueSetSymbol(key + "_GENSEL", clkSymPeripheral)
        gclkSym_PCHCTRL_GEN.setLabel("Generator Selection")
        gclkSym_PCHCTRL_GEN.setDependencies(updateGENSEL, [key + "_CHEN"])
        Gclk_Channel_CFGPCLKGEN_list.append(key + "_GENSEL")

        gclkSymPCHCTRLGenNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/value-group@[name=\"PCLKGENSEL\"]")
        gclkSymPCHCTRLGenNodeValues = []
        gclkSymPCHCTRLGenNodeValues = gclkSymPCHCTRLGenNode.getChildren()

        gclkSymPCHCTRLGenDefaultValue = 0

        for i in range(0, len(gclkSymPCHCTRLGenNodeValues)):
            gclkSymPCHCTRLGenKeyName = gclkSymPCHCTRLGenNodeValues[i].getAttribute("name")
            gclkSymPCHCTRLGenKeyDescription = gclkSymPCHCTRLGenNodeValues[i].getAttribute("caption")
            ggclkSymPCHCTRLGenKeyValue = gclkSymPCHCTRLGenNodeValues[i].getAttribute("value")
            gclkSym_PCHCTRL_GEN.addKey(gclkSymPCHCTRLGenKeyName, ggclkSymPCHCTRLGenKeyValue , gclkSymPCHCTRLGenKeyDescription)

        gclkSym_PCHCTRL_GEN.setDefaultValue(gclkSymPCHCTRLGenDefaultValue)
        gclkSym_PCHCTRL_GEN.setOutputMode("Value")
        gclkSym_PCHCTRL_GEN.setDisplayMode("Key")

        gclkSym_PCHCTRL_FREQ = coreComponent.createIntegerSymbol(key + "_FREQ", clkSymPeripheral)
        gclkSym_PCHCTRL_FREQ.setLabel("Peripheral Channel " + str(index) + " Frequency ")
        gclkSym_PCHCTRL_FREQ.setReadOnly(True)
        gclkSym_PCHCTRL_FREQ.setDefaultValue(0)
        gclkSym_PCHCTRL_FREQ.setDependencies(setGclkFreq, [key + "_CHEN", key + "_GENSEL", "LPCLK_FREQ", "CONFIG_SYS_CLK_REFCLK1_FREQ", "CONFIG_SYS_CLK_REFCLK2_FREQ", "CONFIG_SYS_CLK_REFCLK3_FREQ", "CONFIG_SYS_CLK_REFCLK4_FREQ",
                                                                                        "CONFIG_SYS_CLK_REFCLK5_FREQ", "CONFIG_SYS_CLK_REFCLK6_FREQ"])
        triggerdepList.append(key + "_FREQ")

    for i in range(1, (PeriGenRegCount + 1)):
        gclkSym_CFGPCLKGENx_REG = coreComponent.createHexSymbol("CFGPCLKGEN" + str(i) + "_REG", gclkPeriChannel_menu)
        gclkSym_CFGPCLKGENx_REG.setLabel("Peripheral Clock Generetor Register" + str(i))
        gclkSym_CFGPCLKGENx_REG.setReadOnly(True)
        gclkSym_CFGPCLKGENx_REG.setVisible(False)
        gclkSym_CFGPCLKGENx_REG.setDefaultValue(0x00000000)

    gclkSym_CFGPCLKGENx_REG.setDependencies(setCFGPCLKGENx_Reg, Gclk_Channel_CFGPCLKGEN_list)


    peripheralList = []
    for value in indexSymbolMap.values():
        for i in range (0,len(value)):
            peripheralList.append(value[i])

    peripheralList.sort()

    peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLK_CONFIG", SYM_CLK_MENU)
    peripheralClockMenu.setLabel("Peripheral Clock Configuration")

    for name in peripheralList:
        #GCLK Peripheral Channel Enable
        clkSymExtPeripheral = coreComponent.createBooleanSymbol(name + "_CLOCK_ENABLE", peripheralClockMenu)
        clkSymExtPeripheral.setLabel(name + " Clock Enable")
        clkSymExtPeripheral.setDefaultValue(False)
        triggerdepList.append(name + "_CLOCK_ENABLE") # needed to update frequency for different peripherals
        sym_peripheral_clock_enable.append(name + "_CLOCK_ENABLE") # needed for PMD manipulation

        clkSymExtPeripheralFreq = coreComponent.createIntegerSymbol(name + "_CLOCK_FREQUENCY", clkSymExtPeripheral)
        clkSymExtPeripheralFreq.setLabel(name + " Clock Frequency")
        clkSymExtPeripheralFreq.setReadOnly(True)
        
    # symbol created only to trigger the clock setup logic
    clockTrigger = coreComponent.createBooleanSymbol("TRIGGER_LOGIC", None)
    clockTrigger.setVisible(False)
    clockTrigger.setDependencies(clkSetup, triggerdepList)

    for peripheralName, PmdReg in sorted(peripheralBusDict.items()):
        if (peripheralName not in peripheralList) and ("REF" not in peripheralName):
            clksym_CLK_ENABLE = coreComponent.createBooleanSymbol(peripheralName + "_CLOCK_ENABLE", peripheralClockMenu)
            clksym_CLK_ENABLE.setLabel(peripheralName + " Clock Enable")
            if peripheralName in defaultEnablePeripheralsList:
                clksym_CLK_ENABLE.setDefaultValue(True)
            else:
                clksym_CLK_ENABLE.setDefaultValue(False)
            sym_peripheral_clock_enable.append(peripheralName + "_CLOCK_ENABLE") # needed for PMD manipulation
    
    component = clksym_CLK_ENABLE.getComponent()
    rtcClockFrequency = coreComponent.createIntegerSymbol("RTC_CLOCK_FREQUENCY", component.getSymbolByID("RTC_CLOCK_ENABLE"))
    rtcClockFrequency.setLabel("RTC Clock Frequency")
    rtcClockFrequency.setReadOnly(True)
    rtcClockFrequency.setDefaultValue(32000)
    rtcClockFrequency.setDependencies(rtcClockFreqCalc,["LPCLK_FREQ","CONFIG_VBKP_32KCSEL", "SOSC_OUT_FREQ","CONFIG_VBKP_DIVSEL","CONFIG_VBKP_1KCSEL","CONFIG_RTCNTM_CSEL"])
    
    qspiClockFrequency= coreComponent.createIntegerSymbol("QSPI_CLOCK_FREQUENCY", component.getSymbolByID("QSPI_CLOCK_ENABLE"))
    qspiClockFrequency.setLabel("QSPI Clock Frequency")
    qspiClockFrequency.setDefaultValue(0)
    qspiClockFrequency.setReadOnly(True)
    qspiClockFrequency.setDependencies(qspiClockFreqCalc, ["QSPI_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK2_FREQ"])

    #ADCHS Clock source
    global adchs_clock_map
    adchs_clock_map = {}

    adchs_clock_map[0] = "CONFIG_SYS_CLK_PBCLK1_FREQ"
    adchs_clock_map[1] = "OSCCON_FRCDIV_VALUE"
    adchs_clock_map[2] = "CONFIG_SYS_CLK_REFCLK3_FREQ"
    adchs_clock_map[3] = "SYS_CLK_FREQ"

    adchsClockFrequency = coreComponent.createIntegerSymbol("ADCHS_CLOCK_FREQUENCY", component.getSymbolByID("ADCHS_CLOCK_ENABLE"))
    adchsClockFrequency.setLabel("ADCHS Clock Frequency")
    adchsClockFrequency.setDefaultValue(0)
    adchsClockFrequency.setReadOnly(True)
    adchsClockFrequency.setDependencies(adchsClockFreqCalc, ["ADCHS_CLOCK_ENABLE", "adchs.ADCCON3__ADCSEL", "CONFIG_SYS_CLK_PBCLK1_FREQ",
                                            "SYS_CLK_FREQ", "CONFIG_SYS_CLK_REFCLK3_FREQ", "OSCCON_FRCDIV_VALUE"])

    #############################################################################################
    # PMD
    #############################################################################################    
    cfgRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]').getChildren()

    pmdCount = 0
    pmdDict = {}

    # create a map of PMD register vs its mask value
    for register in cfgRegGroup:
        regName = str(register.getAttribute("name"))
        if regName.startswith("PMD") and regName[-1].isdigit():
            mask = 0x0
            pmdCount += 1
            for bitfield in register.getChildren():
                bitMask = int(str(bitfield.getAttribute("mask")), 16)
                if bitfield.getAttribute("name")[:-2] in defaultEnablePeripheralsList:
                    mask &= ~bitMask
                else:    
                    mask |= bitMask
                pmdDict[pmdCount] = mask

    peripheralModuleDisableMenu = coreComponent.createMenuSymbol("PMD_CONFIG", SYM_CLK_MENU)
    peripheralModuleDisableMenu.setLabel("Peripheral Module Disable")
    peripheralModuleDisableMenu.setDependencies(updatePMDxRegValue, sym_peripheral_clock_enable)

    for i in range(1, pmdCount + 1):
        pmdxRegMaskValue = coreComponent.createHexSymbol("PMD" + str(i) + "_REG_VALUE", peripheralModuleDisableMenu)
        pmdxRegMaskValue.setLabel("PMD" + str(i) + " Register Value")
        pmdxRegMaskValue.setDefaultValue(pmdDict[i])
        pmdxRegMaskValue.setReadOnly(True)

    # for FTL
    pmdRegCount = coreComponent.createIntegerSymbol("PMD_COUNT", peripheralModuleDisableMenu)
    pmdRegCount.setDefaultValue(pmdCount)
    pmdRegCount.setVisible(False)

    #############################################################################################
    # File handling below
    #############################################################################################
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32cx_bz/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32cx_bz/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32cx_bz/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32cx_bz/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
