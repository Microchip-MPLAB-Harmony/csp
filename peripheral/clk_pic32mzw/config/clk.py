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

""" PIC32MZW Clock Configuration File. """
from os.path import join
from xml.etree import ElementTree
global enableMenu
global updateRefFreq
global get_val_from_str
global set_refocon_value
global set_pbdiv_value
global set_refotrim_value

# atdf-specific areas
global clkValGrp_SPLLCON__SPLLICLK
global clkValGrp_OSCCON__FRCDIV
global clkRegGrp_SPLLCON
global CRUmoduleStart
global clkRegGrp_OSCCON
global clkRegGrp_UPLLCON
global clkRegGrp_EWPLLCON
global clkRegGrp_BTPLLCON
global clkRegGrp_CFGCON3
clkValGrp_CFGCON4__SOSCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGCON4__SOSCEN"]')
clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__FRCDIV"]')
clkValGrp_REFO1CON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__ROSEL"]')
clkValGrp_REFO1CON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__RODIV"]')
clkValGrp_REFO1TRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1TRIM__ROTRIM"]')
clkValGrp_SPLLCON__SPLLREFDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="SPLLCON__SPLLREFDIV"]')
clkRegGrp_SPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="SPLLCON"]')
clkValGrp_SPLLCON__SPLLICLK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="SPLLCON__SPLLICLK"]')
clkRegGrp_OSCCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="OSCCON"]')
clkRegGrp_UPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="UPLLCON"]')
clkRegGrp_EWPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="EWPLLCON"]')
clkRegGrp_BTPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="BTPLLCON"]')
clkRegGrp_CFGCON3 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGCON3"]')
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

peripheralBusDict_MZW =  {

        #Peripheral : ["Peripheral bus  "PMD register no", "PMD register bit no"]
        # if "Peripheral bus no" == -1 then clocked by SYSCLK

        "ADCHS":["2","1","0","7","8"],               # ADCHS has multiple PMD bits
        "PLVD":["1","1","4"],
        "PTG":["1","1","11"],
        "CVD":["2","1","15"],
        "RTCC":["4","1","16"],
        "DMAC":["-1","1","19"],
        "BA414E":["5","1","23"],
        "CRYPTO":["5","1","24"],
        "RNG":["5","1","26"],
        "SQI1":["3","1","29"],
        "ICAP1":["3","2","0"],
        "ICAP2":["3","2","1"],
        "ICAP3":["3","2","2"],
        "ICAP4":["3","2","3"],
        "OCMP1":["3","2","8"],
        "OCMP2":["3","2","9"],
        "OCMP3":["3","2","10"],
        "OCMP4":["3","2","11"],
        "TMR1":["1","2","16"],
        "TMR2":["1","2","17"],
        "TMR3":["1","2","18"],
        "TMR4":["1","2","19"],
        "TMR5":["1","2","20"],
        "TMR6":["1","2","21"],
        "TMR7":["1","2","22"],
        "REFO1":["-1","2","28"],
        "REFO2":["-1","2","29"],
        "REFO3":["-1","2","30"],
        "REFO4":["-1","2","31"],
        "UART1":["3","3","0"],
        "UART2":["3","3","1"],
        "UART3":["1","3","2"],
        "ETH":["3","3","4"],
        "SPI1":["3","3","8"],
        "SPI2":["3","3","9"],
        "WIFI":["4","3","12"],
        "I2C1":["2","3","16"],
        "I2C2":["3","3","17"],
        "USB1":["3","3","24"],
        "CAN1":["2","3","27"],
        "CAN2":["2","3","28"],
}

global defaultEnablePeripheralsList

defaultEnablePeripheralsList = ["PLVD", "DMAC", "REFO1", "REFO2", "REFO3", "REFO4"]

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

def update_frc_div_value(symbol, event):
    # updates this symbol value with value from key/value pair
    global per_divider
    # event["value"] is the key name.  Need the corresponding value from that key name.
    symbol.setValue(per_divider.get(event["value"]), 2)

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

def updateRefFreq(menu, event):
    if event["value"] == True:
        # get default value from atdf file and set it
        ii = event["id"].split("_")[3][-1]
        targetName = "__REFCLK" + ii + "_DEF_FREQ"
        params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
        paramsChildren = params.getChildren()
        for param in paramsChildren:  # find parameter we are interested in now
            if(param.getAttribute("name") == targetName):
                menu.setValue(param.getAttribute("value"),2)
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

def updatePoscFreq(symbol, event):
    global newPoscFreq
    newPoscFreq = event["value"]

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

    return str(hex(payload))

def refocon_update(symbol, event):
    '''
    This is the callback for REFOCON_VALUEx symbolID.
    It is called when the user changes either of the following:
        CONFIG_SYS_CLK_REFCLK_SOURCEx
        CONFIG_SYS_CLK_RODIVx
    '''
    global refconval

    # find out which clock we care about by looking at the id.  The last char in the id is clock number
    clk = int(event["id"][-1]) - 1 # "-1" is since indexing starts at 1 (and list indexing starts at 0)
    symObj = event["symbol"]
    index = int(event["id"][-1])  # the last char of the event ID is the index needed to be used

    # finally, set the symbol value to the newly-calculated value
    refconval[clk].setValue(set_refocon_value(index), 2)

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

def sysPeripheralClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]

    if "_CLOCK_ENABLE" in event["id"] and event["value"]:
        freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
    elif Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        freq = int(event["value"])

    symbol.setValue(freq, 1)

def peripheralClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]

    if "_CLOCK_ENABLE" in event["id"] and event["value"]:
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict[periName][0] + "_FREQ"))
    elif Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        freq = int(event["value"])

    symbol.setValue(freq, 1)

def sqiClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]

    if "_CLOCK_ENABLE" in event["id"] and event["value"]:
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK2_FREQ"))
    elif Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        freq = int(event["value"])

    symbol.setValue(freq, 1)

def tmr1ClockFreqCalc(symbol, event):
    global LPRC_DEFAULT_FREQ
    freq = 0
    tmr1ClkSrc = Database.getSymbolValue("tmr1", "TIMER1_SRC_SEL")
    tmr1ExtClkSrc = Database.getSymbolValue("tmr1", "TIMER1_TECS")

    if Database.getSymbolValue("core", "TMR1_CLOCK_ENABLE"):
        if tmr1ClkSrc == None or tmr1ClkSrc == 1:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict["TMR1"][0] + "_FREQ"))
        else:
            if tmr1ExtClkSrc != None:
                if tmr1ExtClkSrc == 0:
                    #LPRC Oscillator Frequency
                    freq = LPRC_DEFAULT_FREQ
                elif tmr1ExtClkSrc == 2:
                    #Secondary Oscillator Frequency
                    freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))

    symbol.setValue(freq, 1)

def rtccClockFreqCalc(symbol, event):
    global LPRC_DEFAULT_FREQ
    freq = 0
    rtccClkSrc = Database.getSymbolValue("rtcc", "RTCC_CLOCK_SOURCE")

    if Database.getSymbolValue("core", "RTCC_CLOCK_ENABLE"):
        if rtccClkSrc != None:
            if rtccClkSrc == 1:
                #LPRC Oscillator Frequency
                freq = LPRC_DEFAULT_FREQ
            else:
                #Secondary Oscillator Frequency
                freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))
        else:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict["RTCC"][0] + "_FREQ"))

    symbol.setValue(freq, 1)

def adchsClockFreqCalc(symbol, event):

    freq = 0
    adchsClkSrc = Database.getSymbolValue("adchs", "ADCCON3__ADCSEL")

    if Database.getSymbolValue("core", "ADCHS_CLOCK_ENABLE"):
        if adchsClkSrc != None and adchsClkSrc != 1:
            freq = int(Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]))

        if adchsClkSrc == 1:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", "OSCCON_FRCDIV_VALUE") if i.isdigit()])
            freq = 8000000 / int(freqDiv)

    symbol.setValue(freq, 1)

def uartClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]
    uartClkSrc = Database.getSymbolValue(periName.lower(), "UART_CLKSEL")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if uartClkSrc == None or uartClkSrc == 3:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict[periName][0] + "_FREQ"))
        elif uartClkSrc == 2:
            freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
        elif uartClkSrc == 1:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", "OSCCON_FRCDIV_VALUE") if i.isdigit()])
            freq = 8000000 / int(freqDiv)
        elif uartClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))

    symbol.setValue(freq, 1)

def spiClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]
    spiClkSrc = Database.getSymbolValue(periName.lower(), "SPI_MASTER_CLOCK")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if spiClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))
        else:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict[periName][0] + "_FREQ"))

    symbol.setValue(freq, 1)

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

global updatePLLBwselValue

def updatePLLBwselValue(refDivider, fbDivider, postDiv, sourceUsed):

    value = None
    Fref = 0
    # POSC and FRC as the reference clock source
    if(sourceUsed == 'FRC'):  # FRC
        Fref = 8000000
    elif((sourceUsed=='POSC') or (sourceUsed=='USBCLK')):  # POSC or USBCLK(for USBPLL only)
        Fref = 40000000

    Fvco = Fref * fbDivider / refDivider

    if((refDivider == 1) and (fbDivider >= 16 and fbDivider <=400)):
        if(Fref >= _4Mhz  and Fref <  _10Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref >= _10Mhz and Fref <  _20Mhz):
            value = 2
        if(Fref >= _20Mhz and Fref <  _30Mhz):
            value = 3
        if(Fref >= _30Mhz and Fref <  _40Mhz):
            value = 4
        if(Fref >= _40Mhz and Fref <= _60Mhz):
            value = 5

    elif((refDivider == 2) and (fbDivider >= 27 and fbDivider <=800)):
        if(Fref >= _4Mhz  and Fref <  _8Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _8Mhz and Fref <  _20Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref >= _20Mhz and Fref <  _40Mhz):
            value = 2
        if(Fref >= _40Mhz and Fref < _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 3
        if(Fref == _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 4

    elif((refDivider == 3) and (fbDivider >= 40 and fbDivider <=1023)):
        if(Fref >= _4Mhz  and Fref <  _12Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _12Mhz and Fref <  _30Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref >= _30Mhz and Fref <  _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 2
        if(Fref == _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 3

    elif((refDivider == 4) and (fbDivider >= 54 and fbDivider <=1023)):
        if(Fref >= _4Mhz  and Fref <  _16Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _16Mhz and Fref <  _40Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref >= _40Mhz and Fref <= _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 2

    elif((refDivider == 5) and (fbDivider >= 67 and fbDivider <=1023)):
        if(Fref >= _5Mhz  and Fref <  _20Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _20Mhz and Fref <  _50Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref >= _50Mhz and Fref <= _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 2

    elif((refDivider == 6) and (fbDivider >= 80 and fbDivider <=1023)):
        if(Fref >= _6Mhz  and Fref <  _24Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _24Mhz and Fref <  _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)
        if(Fref == _60Mhz):
            if(CHECK_800_1600_FVCO(Fvco)==True):
                value = 2

    elif((refDivider == 7) and (fbDivider >= 94 and fbDivider <=1023)):
        if(Fref >= _7Mhz  and Fref <  _28Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _28Mhz and Fref <=  _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 8) and (fbDivider >= 107 and fbDivider <=1023)):
        if(Fref >= _8Mhz  and Fref <  _32Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _32Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 9) and (fbDivider >= 120 and fbDivider <=1023)):
        if(Fref >= _9Mhz  and Fref <  _36Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _36Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 10) and (fbDivider >= 134 and fbDivider <=1023)):
        if(Fref >= _10Mhz  and Fref <  _40Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _40Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 11) and (fbDivider >= 147 and fbDivider <=1023)):
        if(Fref >= _11Mhz  and Fref <  _44Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _44Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 12) and (fbDivider >= 160 and fbDivider <=1023)):
        if(Fref >= _12Mhz  and Fref <  _48Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _48Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 13) and (fbDivider >= 174 and fbDivider <=1023)):
        if(Fref >= _13Mhz  and Fref <  _52Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _52Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 14) and (fbDivider >= 187 and fbDivider <=1023)):
        if(Fref >= _14Mhz  and Fref <  _56Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref >= _56Mhz and Fref <= _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider == 15) and (fbDivider >= 200 and fbDivider <=1023)):
        if(Fref >= _15Mhz  and Fref <  _60Mhz):
            value = CHECK_LOW_PLL(Fvco)
        if(Fref == _60Mhz):
            value = CHECK_HIGH_PLL(Fvco)

    elif((refDivider >= 16 and refDivider <=59)):
        value = CHECK_LOW_PLL(Fvco)

    elif (refDivider == 60 and (fbDivider >= 800 and fbDivider <=1023)):
        value = 0

    return value

global bwselCB

def bwselCB(symbol, event):
    if('BTPLL' in event['id']):
        refDiv = Database.getSymbolValue("core","BTPLLCON_BTPLLREFDIV_VALUE")
        fbDiv = Database.getSymbolValue("core","BTPLLCON_BTPLLFBDIV_VALUE")
        postDiv = Database.getSymbolValue("core","BTPLLCON_BTPLLPOSTDIV1_VALUE")
        pllSource = Database.getSymbolValue("core","BTPLLCON_BTPLLCLK_VALUE")
        pllBwSelSymbolID = "BTPLLCON_BTPLLBSWSEL_VALUE"
        symId = btpllWarningItem
    elif('EWPLL' in event['id']):
        refDiv = Database.getSymbolValue("core","EWPLLCON_EWPLLREFDIV_VALUE")
        fbDiv = Database.getSymbolValue("core","EWPLLCON_EWPLLFBDIV_VALUE")
        postDiv = Database.getSymbolValue("core","EWPLLCON_EWPLLPOSTDIV1_VALUE")
        pllSource = Database.getSymbolValue("core","EWPLLCON_EWPLLICLK_VALUE")
        pllBwSelSymbolID = "EWPLLCON_EWPLLBSWSEL_VALUE"
        symId = ewpllWarningItem
    elif('SPLL' in event['id']):
        refDiv = Database.getSymbolValue("core","SPLLCON_SPLLREFDIV_VALUE")
        fbDiv = Database.getSymbolValue("core","SPLLCON_SPLLFBDIV_VALUE")
        postDiv = Database.getSymbolValue("core","SPLLCON_SPLLPOSTDIV1_VALUE")
        pllSource = Database.getSymbolValue("core","SPLLCON_SPLLICLK_VALUE")
        pllBwSelSymbolID = "SPLLCON_SPLLBSWSEL_VALUE"
        symId = spllWarningItem
    elif(('UPLL' in event['id']) or ('OSCCON' in event['id']) or('USBPLL' in event['id'])):  # one field is part of OSCCON instead of UPLLCON
        refDiv = Database.getSymbolValue("core","UPLLCON_UPLLREFDIV_VALUE")
        fbDiv = Database.getSymbolValue("core","UPLLCON_UPLLFBDIV_VALUE")
        postDiv = Database.getSymbolValue("core","UPLLCON_UPLLPOSTDIV1_VALUE")
        pllSource = Database.getSymbolValue("core","OSCCON_UFRCEN_VALUE")
        pllBwSelSymbolID = "UPLLCON_UPLLBSWSEL_VALUE"
        symId = upllWarningItem
    bwselValue = updatePLLBwselValue(refDiv, fbDiv, postDiv, pllSource)

    if(bwselValue != None):
        Database.setSymbolValue("core", pllBwSelSymbolID, bwselValue, 1)
        symId.setVisible(False)
    else:   # something was out of range - notify user
        symId.setVisible(True)

def updatePMDxRegValue(symbol, event):

    bitShift = 0

    periName = event["id"].replace("_CLOCK_ENABLE", "")

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

def calculated_clock_frequencies(clk_comp, clk_menu, join_path, element_tree, new_posc_freq):
    """
    Calculated Clock frequencies Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    join_path: function used to create os independent paths
    element_tree: XML parser library
    new_posc_freq:  primary oscillator frequency
    """
    global LIST_FWS_MAX_FREQ
    symbolPbFreqList = []
    symbolRefoscFreqList = []

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")
    sys_clk_freq = clk_comp.createStringSymbol("SYS_CLK_FREQ", sym_calc_freq_menu)
    sys_clk_freq.setLabel("System Clock Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setLabel("CPU Clock Frequency (Hz)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(node.getAttribute("value"))
    cpu_clk_freq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])

    # output clock frequency for this BTPLL
    btpllclkFreq = clk_comp.createStringSymbol('BTCLK', sym_calc_freq_menu)
    btpllclkFreq.setDefaultValue('0')  # by default disabled
    btpllclkFreq.setLabel("Bluetooth Clock Frequency (Hz)")
    btpllclkFreq.setVisible(True)

    # output clock frequencies for this PLL - there are 2 signals generated
    ethclkFreq = clk_comp.createStringSymbol('ETHCLK', sym_calc_freq_menu)
    ethclkFreq.setDefaultValue('0')   # by default disabled
    ethclkFreq.setLabel("Ethernet Clock Frequency (Hz)")
    ethclkFreq.setVisible(True)

    wificlkFreq = clk_comp.createStringSymbol('WIFICLK', sym_calc_freq_menu)
    wificlkFreq.setDefaultValue('0')   # by default disabled
    wificlkFreq.setLabel("Wifi Clock Frequency (Hz)")
    wificlkFreq.setVisible(True)

    # output clock frequency for this PLL
    upllclkFreq = clk_comp.createStringSymbol('USBCLK', sym_calc_freq_menu)
    upllclkFreq.setDefaultValue('0')   # by default disabled
    upllclkFreq.setLabel("USB Clock Frequency (Hz)")
    upllclkFreq.setVisible(True)

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

    # Reference Clock frequencies
    index = 0
    for ii in refOscList:  # this is a list of oscillator numbers from the atdf file
        symbolRefoscFreqList.append([])
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_FREQ"
        symbolRefoscFreqList[index] = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
        symbolRefoscFreqList[index].setLabel("Reference Clock #"+ii+" Frequency (Hz)")
        symbolRefoscFreqList[index].setVisible(True)
        symbolRefoscFreqList[index].setDefaultValue("0")
        symbolRefoscFreqList[index].setReadOnly(True)
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_ENABLE"
        symbolRefoscFreqList[index].setDependencies(updateRefFreq, [targetName])
        index += 1

    dswdt_clk_freq = clk_comp.createIntegerSymbol("DSWDT_CLOCK_FREQUENCY", sym_calc_freq_menu)
    dswdt_clk_freq.setLabel("Deep Sleep WDT Clock Frequency (Hz)")
    dswdt_clk_freq.setDefaultValue(dswdtClockDefaultFreq())
    dswdt_clk_freq.setReadOnly(True)
    dswdt_clk_freq.setDependencies(dswdtClockFreqCalc,["CONFIG_DSWDTOSC","CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])

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

global updateUPLLCon

def updateUPLLCon(symbol, event):
    # updates UPLLCON register value based on any of its bitfield values changing
    startVal = symbol.getValue()  # value for the register SPLLCON
    for ii in upllcon_symbols:
        if(ii['name'] == event['id'].split('UPLLCON_')[1].split('_VALUE')[0]):
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

global updateEWPLLCon

def updateEWPLLCon(symbol, event):
    # updates EWPLLCON register value based on any of its bitfield values changing
    startVal = symbol.getValue()  # value for the register EWPLLCON
    for ii in ewpllcon_symbols:
        if(ii['name'] == event['id'].split('EWPLLCON_')[1].split('_VALUE')[0]):
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

global updateBTPLLCon

def updateBTPLLCon(symbol, event):
    # updates BTPLLCON register value based on any of its bitfield values changing
    startVal = symbol.getValue()  # value for the register EWPLLCON
    for ii in btpllcon_symbols:
        if(ii['name'] == event['id'].split('BTPLLCON_')[1].split('_VALUE')[0]):
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

def scan_atdf_for_btpllcon_fields(component, parentMenu, regNode, enableSymbolId):
    '''
    This creates all the symbols for BTPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''
    btpllconRegName = component.createStringSymbol("BTPLLCON_REG", parentMenu)
    btpllconRegName.setVisible(False)
    btpllconRegName.setDefaultValue(regNode.attrib["name"])
    global btpllWarningItem
    global btpllcon_symbols
    btpllcon_symbols = [
                        {'name':'BTPLLBSWSEL', 'symmaskname':'btpllcon_btpllbswsel_mask', 'symvaluename':'btpllcon_btpllbswsel_val', 'keyvalbuf':'btpllbswsel', 'visible':'True', 'min':'0', 'max':'7', 'readonly':True},
                        {'name':'BTPLLPWDN', 'symmaskname':'btpllcon_btpllpwdn_mask', 'symvaluename':'btpllcon_btpllpwdn_val', 'keyvalbuf':'btpllpwdn', 'visible':'True'},
                        {'name':'BTPLLPOSTDIV1', 'symmaskname':'btpllcon_btpllpostdiv1_mask', 'symvaluename':'btpllcon_btpllpostdiv1_val', 'keyvalbuf':'btpllpostdiv1', 'visible':'True', 'min':'1','max':'63'},
                        {'name':'BTPLLFLOCK', 'symmaskname':'btpllcon_btpllflock_mask', 'symvaluename':'btpllcon_btpllflock_val', 'keyvalbuf':'btpllflock', 'visible':'True'},
                        {'name':'BTPLLRST', 'symmaskname':'btpllcon_btpllrst_mask', 'symvaluename':'btpllcon_btpllrst_val', 'keyvalbuf':'btpllrst', 'visible':'True'},
                        {'name':'BTPLLFBDIV', 'symmaskname':'btpllcon_btpllfbdiv_mask', 'symvaluename':'btpllcon_btpllfbdiv_val', 'keyvalbuf':'btpllfbdiv', 'visible':'True', 'min':'16', 'max':'1023'},
                        {'name':'BTPLLREFDIV', 'symmaskname':'btpllcon_btpllrefdiv_mask', 'symvaluename':'btpllcon_btpllrefdiv_val', 'keyvalbuf':'btpllrefdiv', 'visible':'True', 'min':'1', 'max':'63'},
                        {'name':'BTCLKOUTEN', 'symmaskname':'btpllcon_btclkouten_mask', 'symvaluename':'btpllcon_btclkouten_val', 'keyvalbuf':'btclkouten', 'visible':'True'},
                        {'name':'BTPLLCLK', 'symmaskname':'btpllcon_btpllclk_mask', 'symvaluename':'btpllcon_btpllclk_val', 'keyvalbuf':'btpllclk', 'visible':'True'},
                        {'name':'BTPLL_BYP', 'symmaskname':'btpllcon_btpll_byp_mask', 'symvaluename':'btpllcon_btpll_byp_val', 'keyvalbuf':'btpll_byp', 'visible':'True'},
                      ]
    dependencyList = []
    bwselDependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in btpllcon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('BTPLLCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])
                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it
                    where = _get_bitfield_info(CRUmoduleStart, ii['keyvalbuf'], bitfield_tag.attrib["values"])
                    ii['symvaluename'] = component.createComboSymbol('BTPLLCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_BTPLLCON, ii['name'], where))
                else:   # numeric bitfield (no <value-group ..> section associated with it)
                    ii['symvaluename'] = component.createIntegerSymbol('BTPLLCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_BTPLLCON, ii['name'], 'None'))
                    if('min' in ii.keys()):
                        ii['symvaluename'].setMin(int(ii['min']))
                    if('max' in ii.keys()):
                        ii['symvaluename'].setMax(int(ii['max']))
                if('readonly' in ii.keys()):
                    ii['symvaluename'].setReadOnly(ii['readonly'])
                ii['symvaluename'].setLabel(bitfield_tag.attrib['caption'])
                if(ii['visible']=='True'):
                    ii['symvaluename'].setDependencies(enableMenu, [enableSymbolId])  # allow "enable" dialog box of parent menu decide whether this is visible
                else:
                    ii['symvaluename'].setVisible(False)
                dependencyList.append('BTPLLCON_'+ii['name'].upper()+'_VALUE')
                if((ii['name'] == 'BTPLLREFDIV') or (ii['name'] == 'BTPLLFBDIV') or (ii['name'] == 'BTPLLCLK')):
                    bwselDependencyList.append('BTPLLCON_'+ii['name']+'_VALUE')

    # add warning display if parameter combination is outside of usable range so user can make adjustments
    btpllWarningItem = component.createMenuSymbol('BTPLL_OUT_OF_RANGE', parentMenu)
    btpllWarningItem.setLabel("****REFDIV, FBDIV, source frequency combination not in usable range.  Please adjust values.****")
    btpllWarningItem.setVisible(False)
    # after have gone through all bitfields, add callback dependency for update of one of them:  BWSEL
    for ii in btpllcon_symbols:
        if(ii['name'] == 'BTPLLBSWSEL'):
            ii['symvaluename'].setDependencies(bwselCB, bwselDependencyList)

    # get initial value of BTPLLCON register from 'initval' field in atdf file
    symbolBtpllconValue = component.createHexSymbol("BTPLLCON_VALUE", parentMenu)
    symbolBtpllconValue.setVisible(False)
    initialBtpllconVal = int((clkRegGrp_BTPLLCON.getAttribute('initval')),16)
    symbolBtpllconValue.setDefaultValue(initialBtpllconVal)
    symbolBtpllconValue.setDependencies(updateBTPLLCon, dependencyList)
    # There's a register bitfield that's in CFGCON3 register; it's not part of CRU module per-se.  Need to notify user where that field is, so user can change its value
    menuitem = component.createMenuSymbol('BTPLLPOSTDIV2_DISPLAY', parentMenu)
    menuitem.setLabel("****See CFGCON3 under 'Device and Project Configuration' for BTPLL Post Divider setting****")
    menuitem.setVisible(True)
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/register-group/register@[name=\"CFGCON3\"]/bitfield@[name=\"BTPLLPOSTDIV2\"]")
    btpllpostdiv2mask = component.createStringSymbol('BTPLLPOSTDIV2_MASK', parentMenu)
    btpllpostdiv2mask.setVisible(False)
    btpllpostdiv2mask.setDefaultValue(node.getAttribute('mask'))

def scan_atdf_for_ewpllcon_fields(component, parentMenu, regNode, enableSymbolId):
    '''
    This creates all the symbols for EWPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''
    ewpllconRegName = component.createStringSymbol("EWPLLCON_REG", parentMenu)
    ewpllconRegName.setVisible(False)
    ewpllconRegName.setDefaultValue(regNode.attrib["name"])
    global ewpllWarningItem
    global ewpllcon_symbols
    ewpllcon_symbols = [
                        {'name':'EWPLLBSWSEL', 'symmaskname':'ewpllcon_ewpllbswsel_mask', 'symvaluename':'ewpllcon_ewpllbswsel_val', 'keyvalbuf':'ewpllbswsel', 'visible':'True', 'min':'0', 'max':'7', 'readonly':True},
                        {'name':'EWPLLPWDN', 'symmaskname':'ewpllcon_ewpllpwdn_mask', 'symvaluename':'ewpllcon_ewpllpwdn_val', 'keyvalbuf':'ewpllpwdn', 'visible':'True'},
                        {'name':'EWPLLPOSTDIV1', 'symmaskname':'ewpllcon_ewpllpostdiv1_mask', 'symvaluename':'ewpllcon_ewpllpostdiv1_val', 'keyvalbuf':'ewpllpostdiv1', 'visible':'True', 'min':'1','max':'63'},
                        {'name':'EWPLLFLOCK', 'symmaskname':'ewpllcon_ewpllflock_mask', 'symvaluename':'ewpllcon_ewpllflock_val', 'keyvalbuf':'ewpllflock', 'visible':'True'},
                        {'name':'EWPLLRST', 'symmaskname':'ewpllcon_ewpllrst_mask', 'symvaluename':'ewpllcon_ewpllrst_val', 'keyvalbuf':'ewpllrst', 'visible':'True'},
                        {'name':'EWPLLFBDIV', 'symmaskname':'ewpllcon_ewpllfbdiv_mask', 'symvaluename':'ewpllcon_ewpllfbdiv_val', 'keyvalbuf':'ewpllfbdiv', 'visible':'True', 'min':'16', 'max':'1023'},
                        {'name':'EWPLLREFDIV', 'symmaskname':'ewpllcon_ewpllrefdiv_mask', 'symvaluename':'ewpllcon_ewpllrefdiv_val', 'keyvalbuf':'ewpllrefdiv', 'visible':'True', 'min':'1', 'max':'63'}, # no fuse for it - option made available to user here
                        {'name':'EWPLLICLK', 'symmaskname':'ewpllcon_ewplliclk_mask', 'symvaluename':'ewpllcon_ewplliclk_val', 'keyvalbuf':'ewplliclk', 'visible':'True'},
                        {'name':'ETHCLKOUTEN', 'symmaskname':'ewpllcon_ethclkouten_mask', 'symvaluename':'ewpllcon_ethclkouten_val', 'keyvalbuf':'ethclkouten', 'visible':'True'},
                        {'name':'EWPLL_BYP', 'symmaskname':'ewpllcon_ewpll_byp_mask', 'symvaluename':'ewpllcon_ewpll_byp_val', 'keyvalbuf':'ewpll_byp', 'visible':'True'},
                      ]
    dependencyList = []
    bwselDependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in ewpllcon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('EWPLLCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])
                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it
                    where = _get_bitfield_info(CRUmoduleStart, ii['keyvalbuf'], bitfield_tag.attrib["values"])
                    ii['symvaluename'] = component.createComboSymbol('EWPLLCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_EWPLLCON, ii['name'], where))
                else:   # numeric bitfield (no <value-group ..> section associated with it)
                    ii['symvaluename'] = component.createIntegerSymbol('EWPLLCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_EWPLLCON, ii['name'], 'None'))
                    if('min' in ii.keys()):
                        ii['symvaluename'].setMin(int(ii['min']))
                    if('max' in ii.keys()):
                        ii['symvaluename'].setMax(int(ii['max']))
                ii['symvaluename'].setLabel(bitfield_tag.attrib['caption'])
                if(ii['visible']=='True'):
                    ii['symvaluename'].setDependencies(enableMenu, [enableSymbolId])  # allow "enable" dialog box of parent menu decide whether this is visible
                else:
                    ii['symvaluename'].setVisible(False)
                dependencyList.append('EWPLLCON_'+ii['name'].upper()+'_VALUE')
                if((ii['name'] == 'EWPLLREFDIV') or (ii['name'] == 'EWPLLFBDIV') or (ii['name'] == 'EWPLLICLK')):
                    bwselDependencyList.append('EWPLLCON_'+ii['name']+'_VALUE')
                if('readonly' in ii.keys()):
                    ii['symvaluename'].setReadOnly(ii['readonly'])
    # add warning display if parameter combination is outside of usable range so user can make adjustments
    ewpllWarningItem = component.createMenuSymbol('EWPLL_OUT_OF_RANGE', parentMenu)
    ewpllWarningItem.setLabel("****REFDIV, FBDIV, source frequency combination not in usable range.  Please adjust values.****")
    ewpllWarningItem.setVisible(False)
    # after have gone through all bitfields, add callback dependency for update of one of them:  BWSEL
    for ii in ewpllcon_symbols:
        if(ii['name'] == 'EWPLLBSWSEL'):
            ii['symvaluename'].setDependencies(bwselCB, bwselDependencyList)

    # get initial value of EWPLLCON register from 'initval' field in atdf file
    symbolEwpllconValue = component.createHexSymbol("EWPLLCON_VALUE", parentMenu)
    symbolEwpllconValue.setVisible(False)
    initialEwpllconVal = int((clkRegGrp_EWPLLCON.getAttribute('initval')),16)
    symbolEwpllconValue.setDefaultValue(initialEwpllconVal)
    symbolEwpllconValue.setDependencies(updateEWPLLCon, dependencyList)
    # There's a register bitfield that's in CFGCON3 register; it's not part of CRU module per-se.  Need to notify user where that field is, so user can change its value
    menuitem = component.createMenuSymbol('ETHPLLPOSTDIV2_DISPLAY', parentMenu)
    menuitem.setLabel("****See CFGCON3 under 'Device and Project Configuration' for EWPLL Post Divider setting****")
    menuitem.setVisible(True)
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/register-group/register@[name=\"CFGCON3\"]/bitfield@[name=\"ETHPLLPOSTDIV2\"]")
    ethpllpostdiv2mask = component.createStringSymbol('ETHPLLPOSTDIV2_MASK', parentMenu)
    ethpllpostdiv2mask.setVisible(False)
    ethpllpostdiv2mask.setDefaultValue(node.getAttribute('mask'))

def scan_atdf_for_upllcon_fields(component, parentMenu, regNode, enableSymbolId):
    '''
    This creates all the symbols for UPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''
    upllconRegName = component.createStringSymbol("UPLLCON_REG", parentMenu)
    upllconRegName.setVisible(False)
    upllconRegName.setDefaultValue(regNode.attrib["name"])
    global upllWarningItem
    global upllcon_symbols
    upllcon_symbols = [
                        {'name':'UPLLBSWSEL', 'symmaskname':'upllcon_upllbswsel_mask', 'symvaluename':'upllcon_upllbswsel_val', 'keyvalbuf':'upllbswsel', 'visible':'True', 'min':'0', 'max':'7', 'readonly':True},
                        {'name':'UPLLPWDN', 'symmaskname':'upllcon_upllpwdn_mask', 'symvaluename':'upllcon_upllpwdn_val', 'keyvalbuf':'upllpwdn', 'visible':'True'},
                        {'name':'UPLLPOSTDIV1', 'symmaskname':'upllcon_upllpostdiv1_mask', 'symvaluename':'upllcon_upllpostdiv1_val', 'keyvalbuf':'upllpostdiv1', 'visible':'True', 'min':'1','max':'63'},
                        {'name':'UPLLFLOCK', 'symmaskname':'upllcon_cf_mask', 'symvaluename':'upllcon_cf_val', 'keyvalbuf':'cf', 'visible':'True'},
                        {'name':'UPLLRST', 'symmaskname':'upllcon_upllrst_mask', 'symvaluename':'upllcon_upllrst_val', 'keyvalbuf':'upllrst', 'visible':'True'},
                        {'name':'UPLLFBDIV', 'symmaskname':'upllcon_upllfbdiv_mask', 'symvaluename':'upllcon_upllfbdiv_val', 'keyvalbuf':'upllfbdiv', 'visible':'True', 'min':'16', 'max':'1023'},
                        {'name':'UPLLREFDIV', 'symmaskname':'upllcon_upllrefdiv_mask', 'symvaluename':'upllcon_upllrefdiv_val', 'keyvalbuf':'upllrefdiv', 'visible':'True', 'min':'1', 'max':'63'}, # no fuse for it - option made available to user here
# read-only                        {'name':'ULOCK', 'symmaskname':'upllcon_wake2spd_mask', 'symvaluename':'upllcon_wake2spd_val', 'keyvalbuf':'wake2spd', 'visible':'True'},
                        {'name':'UPLL_BYP', 'symmaskname':'upllcon_upll_byp_mask', 'symvaluename':'upllcon_upll_byp_val', 'keyvalbuf':'upll_byp', 'visible':'True'},
                      ]
    dependencyList = []
    bwselDependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in upllcon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('UPLLCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])
                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it
                    where = _get_bitfield_info(CRUmoduleStart, ii['keyvalbuf'], bitfield_tag.attrib["values"])
                    ii['symvaluename'] = component.createComboSymbol('UPLLCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_UPLLCON, ii['name'], where))
                else:   # numeric bitfield (no <value-group ..> section associated with it)
                    ii['symvaluename'] = component.createIntegerSymbol('UPLLCON_'+ii['name']+'_VALUE', parentMenu)
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_UPLLCON, ii['name'], 'None'))
                    if('min' in ii.keys()):
                        ii['symvaluename'].setMin(int(ii['min']))
                    if('max' in ii.keys()):
                        ii['symvaluename'].setMax(int(ii['max']))
                if('readonly' in ii.keys()):
                    ii['symvaluename'].setReadOnly(ii['readonly'])
                ii['symvaluename'].setLabel(bitfield_tag.attrib['caption'])
                if(ii['visible']=='True'):
                    ii['symvaluename'].setDependencies(enableMenu, [enableSymbolId])  # allow "enable" dialog box of parent menu decide whether this is visible
                else:
                    ii['symvaluename'].setVisible(False)
                dependencyList.append('UPLLCON_'+ii['name'].upper()+'_VALUE')

                if((ii['name'] == 'UPLLREFDIV') or (ii['name'] == 'UPLLFBDIV')):
                    bwselDependencyList.append('UPLLCON_'+ii['name']+'_VALUE')
    bwselDependencyList.append('OSCCON_UFRCEN_VALUE')
    # add warning display if parameter combination is outside of usable range so user can make adjustments
    upllWarningItem = component.createMenuSymbol('UPLL_OUT_OF_RANGE', parentMenu)
    upllWarningItem.setLabel("****REFDIV, FBDIV, source frequency combination not in usable range.  Please adjust values.****")
    upllWarningItem.setVisible(False)
    # after have gone through all bitfields, add callback dependency for update of one of them:  BWSEL
    for ii in upllcon_symbols:
        if(ii['name'] == 'UPLLBSWSEL'):
            ii['symvaluename'].setDependencies(bwselCB, bwselDependencyList)

    # get initial value of UPLLCON register from 'initval' field in atdf file
    symbolUpllconValue = component.createHexSymbol("UPLLCON_VALUE", parentMenu)
    symbolUpllconValue.setVisible(False)
    initialUpllconVal = int((clkRegGrp_UPLLCON.getAttribute('initval')),16)
    symbolUpllconValue.setDefaultValue(initialUpllconVal)
    symbolUpllconValue.setDependencies(updateUPLLCon, dependencyList)

def scan_atdf_for_spllcon_fields(component, parentMenu, regNode):
    '''
    This creates all the symbols for SPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them.  Also creates symbols for integer-type fields.
    '''
    spllconRegName = component.createStringSymbol("SPLLCON_REG", parentMenu)
    spllconRegName.setVisible(False)
    spllconRegName.setDefaultValue(regNode.attrib["name"])
    global spllWarningItem
    global spllcon_symbols
    spllcon_symbols = [
                        {'name':'SPLLBSWSEL', 'symmaskname':'spllcon_spllbswsel_mask', 'symvaluename':'spllcon_spllbswsel_val', 'keyvalbuf':'spllbwsel', 'visible':'True', 'readonly':True},
                        {'name':'SPLLPWDN', 'symmaskname':'spllcon_spllpwdn_mask', 'symvaluename':'spllcon_spllpwdn_val', 'keyvalbuf':'spllpwdn', 'visible':'False'},
                        {'name':'SPLLPOSTDIV1', 'symmaskname':'spllcon_spllpostdiv1_mask', 'symvaluename':'spllcon_spllpostdiv1_val', 'keyvalbuf':'spllpostdiv1', 'visible':'True', 'min':'6', 'max':'63'}, # no fuse for it - option made available to user here
                        {'name':'SPLLFLOCK', 'symmaskname':'spllcon_spllflock_mask', 'symvaluename':'spllcon_spllflock_val', 'keyvalbuf':'spllflock', 'visible':'False'},
                        {'name':'SPLLRST', 'symmaskname':'spllcon_spllrst_mask', 'symvaluename':'spllcon_spllrst_val', 'keyvalbuf':'spllrst', 'visible':'False'},
                        {'name':'SPLLFBDIV', 'symmaskname':'spllcon_spllfbdiv_mask', 'symvaluename':'spllcon_spllfbdiv_val', 'keyvalbuf':'spllfbdiv', 'visible':'True', 'min':'16', 'max':'1023', 'readonly':True}, # no fuse for it - option made available to user here
                        {'name':'SPLLREFDIV', 'symmaskname':'spllcon_spllrefdiv_mask', 'symvaluename':'spllcon_spllrefdiv_val', 'keyvalbuf':'spllrefdiv', 'visible':'True', 'min':'1', 'max':'63', 'readonly':True}, # no fuse for it - option made available to user here
                        {'name':'SPLLICLK', 'symmaskname':'spllcon_splliclk_mask', 'symvaluename':'spllcon_splliclk_val', 'keyvalbuf':'splliclk', 'visible':'True'}, # no fuse for it - option made available to user here
                        {'name':'SPLL_BYP', 'symmaskname':'spllcon_spllbyp_mask', 'symvaluename':'spllcon_spllbyp_val', 'keyvalbuf':'spllbyp', 'visible':'True'}, # no fuse for it - option made available to user here
                      ]
    dependencyList = []
    bwselDependencyList = []
    for bitfield_tag in regNode.iter("bitfield"):
        for ii in spllcon_symbols: # find match to know what symbol names to use
            if(ii['name'] == bitfield_tag.attrib["name"]):
                ii['symmaskname'] = component.createStringSymbol('SPLLCON_'+ii['name'].upper()+'_MASK', parentMenu)
                ii['symmaskname'].setVisible(False)
                ii['symmaskname'].setDefaultValue(bitfield_tag.attrib["mask"])

                ii['keyvalbuf'] = {}
                if(bitfield_tag.get("values",None) != None):  # bitfield with <value-group ..> section associated with it
                    where = _get_bitfield_info(CRUmoduleStart, ii['keyvalbuf'], bitfield_tag.attrib["values"])
                    ii['symvaluename'] = component.createComboSymbol('SPLLCON_'+ii['name']+'_VALUE', parentMenu, ii['keyvalbuf'].keys())
                    ii['symvaluename'].setDescription(where.getAttribute('caption'))
                    ii['symvaluename'].setDefaultValue(_get_default_value(clkRegGrp_SPLLCON, ii['name'], where))
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
                if((ii['name'] == 'SPLLREFDIV') or (ii['name'] == 'SPLLFBDIV') or (ii['name'] == 'SPLLICLK')):
                    bwselDependencyList.append('SPLLCON_'+ii['name']+'_VALUE')

    # add warning display if parameter combination is outside of usable range so user can make adjustments
    spllWarningItem = component.createMenuSymbol('SPLL_OUT_OF_RANGE', parentMenu)
    spllWarningItem.setLabel("****REFDIV, FBDIV, source frequency combination not in usable range.  Please adjust values.****")
    spllWarningItem.setVisible(False)

    # Do not change SPLLBSWSEL dynamically for now 
    '''
    # after have gone through all bitfields, add callback dependency for update of one of them:  BWSEL
    for ii in spllcon_symbols:
        if(ii['name'] == 'SPLLBSWSEL'):
            ii['symvaluename'].setDependencies(bwselCB, bwselDependencyList)'''

    # get initial value of SPLLCON register from 'initval' field in atdf file
    symbolSpllconValue = component.createHexSymbol("SPLLCON_VALUE", parentMenu)
    symbolSpllconValue.setVisible(False)
    initialSpllconVal = int((clkRegGrp_SPLLCON.getAttribute('initval')),16)
    symbolSpllconValue.setDefaultValue(initialSpllconVal)
    symbolSpllconValue.setDependencies(updateSPLLCon, dependencyList)

    # There's a register bitfield that's in CFGCON3 register; it's not part of CRU module per-se.  Need to notify user where that field is, so user can change its value
    menuitem = component.createMenuSymbol('SPLLPOSTDIV2_DISPLAY', parentMenu)
    menuitem.setLabel("****See CFGCON3 under Device and Project Configuration for SPLL Post Divider setting****")
    menuitem.setVisible(True)

    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/register-group/register@[name=\"CFGCON3\"]/bitfield@[name=\"SPLLPOSTDIV2\"]")
    spllpostdiv2mask = component.createStringSymbol('SPLLPOSTDIV2_MASK', parentMenu)
    spllpostdiv2mask.setVisible(False)
    spllpostdiv2mask.setDefaultValue(node.getAttribute('mask'))

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
                        {'name':'UFRCEN', 'symmaskname':'osccon_ufrcen_mask', 'symvaluename':'osccon_ufrcen_val', 'keyvalbuf':'ufrcen', 'visible':'True'},
                        {'name':'CF', 'symmaskname':'osccon_cf_mask', 'symvaluename':'osccon_cf_val', 'keyvalbuf':'cf', 'visible':'False'},
                        {'name':'SLPEN', 'symmaskname':'osccon_slpen_mask', 'symvaluename':'osccon_slpen_val', 'keyvalbuf':'slpen', 'visible':'False'},
                        {'name':'CLKLOCK', 'symmaskname':'osccon_clklock_mask', 'symvaluename':'osccon_clklock_val', 'keyvalbuf':'clklock', 'visible':'False'},
                        {'name':'NOSC', 'symmaskname':'osccon_nosc_mask', 'symvaluename':'osccon_nosc_val', 'keyvalbuf':'nosc', 'visible':'True'}, # no fuse for it - option made available to user here
                        {'name':'WAKE2SPD', 'symmaskname':'osccon_wake2spd_mask', 'symvaluename':'osccon_wake2spd_val', 'keyvalbuf':'wake2spd', 'visible':'False'},
                        {'name':'DRMEN', 'symmaskname':'osccon_drmen_mask', 'symvaluename':'osccon_drmen_val', 'keyvalbuf':'drmen', 'visible':'False'},
                        {'name':'FRCDIV', 'symmaskname':'osccon_frcdiv_mask', 'symvaluename':'osccon_frcdiv_val', 'keyvalbuf':'frcdiv', 'visible':'True'},
                      ]
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

# Deep Sleep WDT
global dswdtClockDefaultFreq
def dswdtClockDefaultFreq():
    global LPRC_DEFAULT_FREQ
    if Database.getSymbolValue("core", "CONFIG_DSWDTOSC") == "LPRC":
        dswdtFreq = LPRC_DEFAULT_FREQ
    else:
        dswdtFreq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))
    return dswdtFreq

global dswdtClockFreqCalc
def dswdtClockFreqCalc(symbol,event):
    symbol.setValue(dswdtClockDefaultFreq())

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
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_MIPS32", None)
    SYM_CLK_MENU.setLabel("Clock Menu")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mzw:MZW1ClockModel")
    peripheralBusDict = peripheralBusDict_MZW.copy()

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

    # static or dynamic - always static
    CLK_SVC_MODE = coreComponent.createKeyValueSetSymbol("clkSvcMode", SYM_CLK_MENU)
    CLK_SVC_MODE.setDependencies(enableMenu, ["ClkSvcMenu"])
    CLK_SVC_MODE.setDescription("Static or Dynamic (clocks can be changed during runtime)")
    CLK_SVC_MODE.setOutputMode("Value")
    CLK_SVC_MODE.setDisplayMode("Description")
    CLK_SVC_MODE.addKey("STATIC", "0", "Static: Clocks do not change after being set at startup." )
    #not doing dynamic for H3   CLK_SVC_MODE.addKey("DYNAMIC", "1", "Dynamic: Clocks can be changed at runtime")
    CLK_SVC_MODE.setVisible(False)
    CLK_SVC_MODE.setSelectedKey("STATIC",1)

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

    usbPllEnSymId = "USBPLL_ENABLE"
    UPLL_CFG_SETTINGS = coreComponent.createBooleanSymbol(usbPllEnSymId, CLK_CFG_SETTINGS)
    UPLL_CFG_SETTINGS.setLabel("Enable USB PLL")
    UPLL_CFG_SETTINGS.setDescription("Sets whether to have USBPLL enabled")
    UPLL_CFG_SETTINGS.setDefaultValue(False)

    ewpllEnSymId = "EWPLL_ENABLE"
    EWPLL_CFG_SETTINGS = coreComponent.createBooleanSymbol(ewpllEnSymId, CLK_CFG_SETTINGS)
    EWPLL_CFG_SETTINGS.setLabel("Enable Ethernet/Wifi PLL")
    EWPLL_CFG_SETTINGS.setDescription("Sets whether to have EWPLL enabled")
    EWPLL_CFG_SETTINGS.setDefaultValue(False)

    btpllEnSymId = "BTPLL_ENABLE"
    BTPLL_CFG_SETTINGS = coreComponent.createBooleanSymbol(btpllEnSymId, CLK_CFG_SETTINGS)
    BTPLL_CFG_SETTINGS.setLabel("Enable Bluetooth PLL")
    BTPLL_CFG_SETTINGS.setDescription("Sets whether to have BTPLL enabled")
    BTPLL_CFG_SETTINGS.setDefaultValue(False)

    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):
                if("SPLLCON" in register_tag.attrib["name"]):
                    scan_atdf_for_spllcon_fields(coreComponent, SPLL_CFG_SETTINGS, register_tag)
                if("OSCCON" == register_tag.attrib["name"]):
                    scan_atdf_for_osccon_fields(coreComponent, CLK_CFG_SETTINGS, register_tag)
                if("UPLLCON" == register_tag.attrib["name"]):
                    scan_atdf_for_upllcon_fields(coreComponent, UPLL_CFG_SETTINGS, register_tag, usbPllEnSymId)
                if("EWPLLCON" == register_tag.attrib["name"]):
                    scan_atdf_for_ewpllcon_fields(coreComponent, EWPLL_CFG_SETTINGS, register_tag, ewpllEnSymId)
                if("BTPLLCON" == register_tag.attrib["name"]):
                    scan_atdf_for_btpllcon_fields(coreComponent, BTPLL_CFG_SETTINGS, register_tag, btpllEnSymId)

                #looking for PB1DIV, PB2DIV, ... (for making menu entries - further down, and ftl-related symbols)
                if ("PB" in register_tag.attrib["name"]) and ("DIV" in register_tag.attrib["name"]):
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
                if ("REFO" in register_tag.attrib["name"]) and ("CON" in register_tag.attrib["name"]):
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
                if ("REFO" in register_tag.attrib["name"]) and ("TRIM" in register_tag.attrib["name"]):
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

    # Menu items listed here
    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

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

    TEMP_RANGE.addKey("RANGE1", "1", "-40C to +85C, DC to 250 MHz")
    TEMP_RANGE.setDefaultValue(0)
    TEMP_RANGE.setReadOnly(True)
    max_clk_freq_for_selected_temp.setDefaultValue(250000000)

    # keep in here in case part later has 2 temerature ranges and 2 upper frequencies
    max_clk_freq_for_selected_temp.setDependencies(updateMaxFreq, ["CONFIG_TEMPERATURE_RANGE"])

    HAVE_REFCLK = coreComponent.createBooleanSymbol("CONFIG_HAVE_REFCLOCK", CLK_CFG_SETTINGS)
    HAVE_REFCLK.setLabel("Have reference clock available")
    HAVE_REFCLK.setVisible(False)
    HAVE_REFCLK.setDefaultValue(True)

    # secondary oscillator enable - made this by default enabled
    soscen = {}
    _get_bitfield_names(clkValGrp_CFGCON4__SOSCEN, soscen)
    SOSC_EN_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_CONFIG_SOSCEN", CLK_CFG_SETTINGS, sorted(soscen.keys()))
    SOSC_EN_SETTING.setLabel("Secondary oscillator enable")
    SOSC_EN_SETTING.setDescription(clkValGrp_CFGCON4__SOSCEN.getAttribute('caption'))
    SOSC_EN_SETTING.setVisible(False)

    deviceHasDDR2 = coreComponent.createBooleanSymbol("DEVICE_HAS_DDR2", CLK_CFG_SETTINGS)
    deviceHasDDR2.setVisible(False)
    deviceHasDDR2.setDefaultValue(False)

    # now create the menus for all peripheral buses present in this part
    global pbclkEnNameList
    global roselSymbolList
    global refconval
    global symbolRoselValueList
    global refotrimval
    global symbolrefotrimval
    global rotrimSymbolList
    global symbolRotrimUserVal
    global roselMap
    pbclkEnNameList = []
    enSymbolList = []
    oeSymbolList = []
    sourceSymbolList = []
    roselSymbolList = []
    rodivSymbolList = []
    rotrimSymbolList = []
    refconval = []
    symbolRoselValueList = []
    symbolRodivValueList = []
    symbolPbdivList = []        # for PBxDIV:PBDIV contains list of {symbolName, clock number}
    symbolPbdiv = []
    refotrimval = []
    symbolrefotrimval = []
    symbolRotrimUserVal = []

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
                symbolDivName.setDefaultValue( _get_default_value(ii, bitfield, 'None'))
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

        enSymId = "CONFIG_SYS_CLK_REFCLK"+clk+"_ENABLE"
        enSymbolList[listIndex] = coreComponent.createBooleanSymbol(enSymId, CLK_CFG_SETTINGS)
        enSymbolList[listIndex].setLabel("Enable Reference Clock "+clk)
        enSymbolList[listIndex].setDescription("Sets whether to have reference clock 1 enabled")
        enSymbolList[listIndex].setDefaultValue(False)

        # output enable of ref clk
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
        sourceSymbolList[listIndex].setDefaultValue("SYSCLK")
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
        rodivSymbolList[listIndex].setDependencies(enableMenu, [enSymId])
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

        # python-computed REFOxCON register setting to use in ftl file
        refconval.append([])
        refconval[listIndex] = coreComponent.createStringSymbol("REFOCON"+clk+"_VALUE", None)
        refconval[listIndex].setVisible(False)
        refconval[listIndex].setDefaultValue(set_refocon_value(clk))
        # change based on CONFIG_SYS_CLK_REFCLK_ROSELx or CONFIG_SYS_CLK_RODIVx changes
        refconval[listIndex].setDependencies(refocon_update, [srcSymId, rodivSymId])

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
    POSC_IN_FREQ.setDependencies(updatePoscFreq, ["CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL"])
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__POSC_DEF_FREQ"]')
    POSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    newPoscFreq = node.getAttribute("value")
    SOSC_IN_FREQ.setDefaultValue(int(newPoscFreq))

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
    global LPRC_DEFAULT_FREQ
    LPRC_DEFAULT_FREQ = 32768
    LPRC_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_LPRC", CLK_CFG_SETTINGS)
    LPRC_FREQ.setVisible(False)
    LPRC_FREQ.setDefaultValue(LPRC_DEFAULT_FREQ)

    # this is added to resolve a dependency in ftl file
    HAVE_REFCLK5 = coreComponent.createBooleanSymbol("CONFIG_HAVE_REFCLOCK5", CLK_CFG_SETTINGS)
    HAVE_REFCLK5.setVisible(False)
    HAVE_REFCLK5.setDefaultValue(False)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, join, ElementTree, newPoscFreq)

    availablePeripherals = []

    modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()

    for module in range(len(modules)):
        instances = modules[module].getChildren()
        for instance in range(len(instances)):
            availablePeripherals.append(str(instances[instance].getAttribute("name")))

    #ADCHS Clock source
    global adchs_clock_map
    adchs_clock_map = {}
    adchs_clock_map[0] = "CONFIG_SYS_CLK_PBCLK2_FREQ"
    adchs_clock_map[1] = "OSCCON_FRCDIV_VALUE"
    adchs_clock_map[2] = "CONFIG_SYS_CLK_REFCLK3_FREQ"
    adchs_clock_map[3] = "SYS_CLK_FREQ"

    peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLK_CONFIG", SYM_CLK_MENU)
    peripheralClockMenu.setLabel("Peripheral Clock Configuration")

    # calculated peripheral frequencies
    sym_peripheral_clock_enable = []
    sym_peripheral_clock_freq = []

    for peripheralName, peripheralBus in sorted(peripheralBusDict.items()):

        if peripheralName.startswith("REFO") or peripheralName.startswith("BA414E") or peripheralName.startswith("WIFI") or peripheralName in availablePeripherals:
            sym_peripheral_clock_enable.append(peripheralName + "_CLOCK_ENABLE")
            peripheral_clock_enable = coreComponent.createBooleanSymbol(peripheralName + "_CLOCK_ENABLE", peripheralClockMenu)
            peripheral_clock_enable.setLabel(peripheralName + " Clock Enable")
            peripheral_clock_enable.setReadOnly(len(peripheralBus) == 1)

            if peripheralName in defaultEnablePeripheralsList:
                peripheral_clock_enable.setDefaultValue(True)
            else:
                peripheral_clock_enable.setDefaultValue(False)

            sym_peripheral_clock_freq.append(peripheralName + "_CLOCK_FREQUENCY")
            peripheral_clock_freq = coreComponent.createIntegerSymbol(peripheralName + "_CLOCK_FREQUENCY", peripheral_clock_enable)
            peripheral_clock_freq.setLabel(peripheralName + " Clock Frequency")
            peripheral_clock_freq.setReadOnly(True)

            if peripheralName in defaultEnablePeripheralsList:
                if peripheralBus[0] == "-1":
                    peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))
                    peripheral_clock_freq.setDependencies(sysPeripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "SYS_CLK_FREQ"])
                else:
                    peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ")))
                    peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ"])
            else:
                peripheral_clock_freq.setDefaultValue(0)

                if peripheralName.startswith("UART"):
                    peripheral_clock_freq.setDependencies(uartClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".UART_CLKSEL", "OSCCON_FRCDIV_VALUE",
                                                                                         "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ", "CONFIG_SYS_CLK_REFCLK1_FREQ"])
                elif peripheralName == "TMR1":
                    peripheral_clock_freq.setDependencies(tmr1ClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "tmr1.TIMER1_SRC_SEL", "tmr1.TIMER1_TECS", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                         "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])
                elif peripheralName == "ADCHS":
                    peripheral_clock_freq.setDependencies(adchsClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "adchs.ADCCON3__ADCSEL", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                        "SYS_CLK_FREQ", "CONFIG_SYS_CLK_REFCLK3_FREQ", "OSCCON_FRCDIV_VALUE"])
                elif peripheralName.startswith("SPI"):
                    peripheral_clock_freq.setDependencies(spiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".SPI_MASTER_CLOCK", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                        "CONFIG_SYS_CLK_REFCLK1_FREQ"])
                elif peripheralName.startswith("SQI"):
                    peripheral_clock_freq.setDependencies(sqiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_REFCLK2_FREQ"])
                elif peripheralName == "RTCC":
                    peripheral_clock_freq.setDependencies(rtccClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "rtcc.RTCC_CLOCK_SOURCE", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                         "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])
                else:
                    peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ"])

    cfgRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]').getChildren()

    pmdCount = 0
    pmdDict = {}

    for register in cfgRegGroup:
        regName = str(register.getAttribute("name"))
        if regName.startswith("PMD"):
            mask = 0x0
            pmdCount += 1
            for bitfield in register.getChildren():
                mask |= int(str(bitfield.getAttribute("mask")), 16)
                pmdDict[pmdCount] = mask

    peripheralModuleDisableMenu = coreComponent.createMenuSymbol("PMD_CONFIG", SYM_CLK_MENU)
    peripheralModuleDisableMenu.setLabel("Peripheral Module Disable")
    peripheralModuleDisableMenu.setDependencies(updatePMDxRegValue, sym_peripheral_clock_enable)

    pmdRegCount = coreComponent.createIntegerSymbol("PMD_COUNT", peripheralModuleDisableMenu)
    pmdRegCount.setDefaultValue(pmdCount)
    pmdRegCount.setVisible(False)

    for i in range(1, pmdCount + 1):
        pmdxRegMaskValue = coreComponent.createHexSymbol("PMD" + str(i) + "_REG_VALUE", peripheralModuleDisableMenu)
        pmdxRegMaskValue.setLabel("PMD" + str(i) + " Register Value")
        pmdxRegMaskValue.setDefaultValue(pmdDict[i])
        pmdxRegMaskValue.setReadOnly(True)

    for peripheralName in defaultEnablePeripheralsList:
        if len(peripheralBusDict[peripheralName]) > 1:
            #Enable Peripheral from PMD
            periPMDRegId = "PMD" + peripheralBusDict[peripheralName][1] + "_REG_VALUE"
            pmdxValue = Database.getSymbolValue("core", periPMDRegId)
            periPMDRegBitShift = 1 << int(peripheralBusDict[peripheralName][2])
            Database.setSymbolValue("core", periPMDRegId, pmdxValue & ~periPMDRegBitShift, 1)

    # File handling below
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32mzw/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32mzw/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mzw/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mzw/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
