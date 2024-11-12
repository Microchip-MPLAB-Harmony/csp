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

""" PIC32MZ Clock Configuration File. """
from os.path import join
from xml.etree import ElementTree
global enableMenu
global updateRefFreq
global get_val_from_str
global set_refocon_value
global set_pbdiv_value
global set_refotrim_value

global peripheralBusDict
peripheralBusDict = {}

global LPRC_DEFAULT_FREQ
LPRC_DEFAULT_FREQ = 32768

peripheralBusDict_EF =  {

        #Peripheral : ["Peripheral bus  "PMD register no", "PMD register bit no"]
        # if "Peripheral bus no" == -1 then clocked by SYSCLK

        "ADCHS": ["3", "1", "0"],
        "CVR": ["1", "1", "12"],
        "CMP1": ["3", "2", "0"],
        "CMP2": ["3", "2", "1"],
        "ICAP1": ["3", "3", "0"],
        "ICAP2": ["3", "3", "1"],
        "ICAP3": ["3", "3", "2"],
        "ICAP4": ["3", "3", "3"],
        "ICAP5": ["3", "3", "4"],
        "ICAP6": ["3", "3", "5"],
        "ICAP7": ["3", "3", "6"],
        "ICAP8": ["3", "3", "7"],
        "ICAP9": ["3", "3", "8"],
        "OCMP1": ["3", "3", "16"],
        "OCMP2": ["3", "3", "17"],
        "OCMP3": ["3", "3", "18"],
        "OCMP4": ["3", "3", "19"],
        "OCMP5": ["3", "3", "20"],
        "OCMP6": ["3", "3", "21"],
        "OCMP7": ["3", "3", "22"],
        "OCMP8": ["3", "3", "23"],
        "OCMP9": ["3", "3", "24"],
        "TMR1": ["3", "4", "0"],
        "TMR2": ["3", "4", "1"],
        "TMR3": ["3", "4", "2"],
        "TMR4": ["3", "4", "3"],
        "TMR5": ["3", "4", "4"],
        "TMR6": ["3", "4", "5"],
        "TMR7": ["3", "4", "6"],
        "TMR8": ["3", "4", "7"],
        "TMR9": ["3", "4", "8"],
        "UART1": ["2", "5", "0"],
        "UART2": ["2", "5", "1"],
        "UART3": ["2", "5", "2"],
        "UART4": ["2", "5", "3"],
        "UART5": ["2", "5", "4"],
        "UART6": ["2", "5", "5"],
        "SPI1": ["2", "5", "8"],
        "SPI2": ["2", "5", "9"],
        "SPI3": ["2", "5", "10"],
        "SPI4": ["2", "5", "11"],
        "SPI5": ["2", "5", "12"],
        "SPI6": ["2", "5", "13"],
        "I2C1": ["2", "5", "16"],
        "I2C2": ["2", "5", "17"],
        "I2C3": ["2", "5", "18"],
        "I2C4": ["2", "5", "19"],
        "I2C5": ["2", "5", "20"],
        "USB": ["5", "5", "24"],
        "CAN1": ["5", "5", "28"],
        "CAN2": ["5", "5", "29"],
        "RTCC": ["1", "6", "0"],
        "REFO1": ["-1", "6", "8"],
        "REFO2": ["-1", "6", "9"],
        "REFO3": ["-1", "6", "10"],
        "REFO4": ["-1", "6", "11"],
        "PMP": ["2", "6", "16"],
        "EBI": ["8", "6", "17"],
        "SQI1": ["5", "6", "23"],
        "ETH": ["5", "6", "28"],
        "DMAC": ["-1", "7", "4"],
        "RNG": ["5", "7", "20"],
        "CRYPTO": ["5", "7", "22"],
}

peripheralBusDict_DA =  {

        #Peripheral : ["Peripheral bus  "PMD register no", "PMD register bit no"]
        # if "Peripheral bus no" == -1 then clocked by SYSCLK

        "ADCHS": ["3", "1", "0"],
        "CTMU": ["3", "1", "8"],
        "CVR": ["1", "1", "12"],
        "HLVD": ["1", "1", "20"],
        "CMP1": ["3", "2", "0"],
        "CMP2": ["3", "2", "1"],
        "ICAP1": ["3", "3", "0"],
        "ICAP2": ["3", "3", "1"],
        "ICAP3": ["3", "3", "2"],
        "ICAP4": ["3", "3", "3"],
        "ICAP5": ["3", "3", "4"],
        "ICAP6": ["3", "3", "5"],
        "ICAP7": ["3", "3", "6"],
        "ICAP8": ["3", "3", "7"],
        "ICAP9": ["3", "3", "8"],
        "OCMP1": ["3", "3", "16"],
        "OCMP2": ["3", "3", "17"],
        "OCMP3": ["3", "3", "18"],
        "OCMP4": ["3", "3", "19"],
        "OCMP5": ["3", "3", "20"],
        "OCMP6": ["3", "3", "21"],
        "OCMP7": ["3", "3", "22"],
        "OCMP8": ["3", "3", "23"],
        "OCMP9": ["3", "3", "24"],
        "TMR1": ["3", "4", "0"],
        "TMR2": ["3", "4", "1"],
        "TMR3": ["3", "4", "2"],
        "TMR4": ["3", "4", "3"],
        "TMR5": ["3", "4", "4"],
        "TMR6": ["3", "4", "5"],
        "TMR7": ["3", "4", "6"],
        "TMR8": ["3", "4", "7"],
        "TMR9": ["3", "4", "8"],
        "UART1": ["2", "5", "0"],
        "UART2": ["2", "5", "1"],
        "UART3": ["2", "5", "2"],
        "UART4": ["2", "5", "3"],
        "UART5": ["2", "5", "4"],
        "UART6": ["2", "5", "5"],
        "SPI1": ["2", "5", "8"],
        "SPI2": ["2", "5", "9"],
        "SPI3": ["2", "5", "10"],
        "SPI4": ["2", "5", "11"],
        "SPI5": ["2", "5", "12"],
        "SPI6": ["2", "5", "13"],
        "I2C1": ["2", "5", "16"],
        "I2C2": ["2", "5", "17"],
        "I2C3": ["2", "5", "18"],
        "I2C4": ["2", "5", "19"],
        "I2C5": ["2", "5", "20"],
        "USB": ["5", "5", "24"],
        "CAN1": ["5", "5", "28"],
        "CAN2": ["5", "5", "29"],
        "REFO1": ["-1", "6", "8"],
        "REFO2": ["-1", "6", "9"],
        "REFO3": ["-1", "6", "10"],
        "REFO4": ["-1", "6", "11"],
        "REFO5": ["-1", "6", "12"],
        "PMP": ["2", "6", "16"],
        "EBI": ["-1", "6", "17"],
        "GPU": ["-1", "6", "18"],
        "GLCD": ["-1", "6", "20"],
        "SDHC": ["5", "6", "21"],
        "SQI1": ["5", "6", "23"],
        "ETH": ["5", "6", "28"],
        "DMAC": ["-1", "7", "4"],
        "RNG": ["5", "7", "20"],
        "CRYPTO": ["5", "7", "22"],
        "DDR": ["-1", "7", "28"],
        "RTCC": ["6"],
}

def updateMaxFreq(symbol, event):
    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") != "PIC32MZDA"):
        if event["value"] == 0:
            symbol.setValue(180000000, 2)
        elif event["value"] == 1:
            symbol.setValue(252000000, 2)

def update_frc_div_value(symbol, event):
    # updates this symbol value with value from key/value pair
    global per_divider
    # event["value"] is the key name.  Need the corresponding value from that key name.
    symbol.setValue(per_divider.get(event["value"]), 2)

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

def _get_default_value(register, bitfield, value_group):
    '''
    Extracts the default value from 'initval' field of given value-group, based on register bitfield
    Input arguments:
        register - atdf node, register name to get the intial value
        bitfield - the bitfield in the register we are interested in (to get mask value from)
        value_group - atdf node, the value group from which we want

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
    value = str(hex((initialValue & mask) >> bitPosn))  # has initial value of bitfield, shifted down to bit0
    keyDefault = ''
    childNodes = value_group.getChildren() # get all <value ..> to find the one that matches the value
    for ii in childNodes:
        if(ii.getAttribute('value') == value):
            keyDefault = ii.getAttribute('name')
    return keyDefault
    #return str((initialValue & mask) >> bitPosn)

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

def sdhcClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]

    if "_CLOCK_ENABLE" in event["id"] and event["value"]:
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK4_FREQ"))
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
        if adchsClkSrc != None and adchsClkSrc != 3:
            freq = int(Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]))

        if adchsClkSrc == 3:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]) if i.isdigit()])
            freq = 8000000 / int(freqDiv)

    symbol.setValue(freq, 1)

def uartClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]
    uartClkSrc = Database.getSymbolValue(periName.lower(), "UART_CLKSEL")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if uartClkSrc == None or uartClkSrc == 3 or uartClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBusDict[periName][0] + "_FREQ"))
        elif uartClkSrc == 2:
            freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
        elif uartClkSrc == 1:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", "CONFIG_SYS_CLK_FRCDIV") if i.isdigit()])
            freq = 8000000 / int(freqDiv)

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

def updatePMDxRegValue(symbol, event):

    periName = event["id"].replace("_CLOCK_ENABLE", "")

    pmdRegId = "PMD" + peripheralBusDict[periName][1] + "_REG_VALUE"
    bitShift = 1 << int(peripheralBusDict[periName][2])

    pmdxValue = Database.getSymbolValue("core", pmdRegId)

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
    sys_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    sys_clk_freq.setLabel("System Clock Frequency (HZ)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    cpu_clk_freq.setLabel("CPU Clock Frequency (HZ)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(node.getAttribute("value"))
    cpu_clk_freq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])

    # Peripheral Bus clock frequencies
    index = 0
    for ii in pbclkEnNameList:  # this list has  "CONFIG_SYS_CLK_PBCLK"+pbus+"_ENABLE", where pbus is index from atdf file
        # get index value, as need that separately below
        posn = ii.find("_ENABLE")
        clkInstance = ii[posn-1]   # get the pbus number for this instance
        symbolPbFreqList.append([])
        targetName = "CONFIG_SYS_CLK_PBCLK" + clkInstance + "_FREQ"
        symbolPbFreqList[index] = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
        symbolPbFreqList[index].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
        symbolRefoscFreqList[index].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        symbolRefoscFreqList[index].setLabel("Reference Clock #"+ii+" Frequency (Hz)")
        symbolRefoscFreqList[index].setVisible(True)
        symbolRefoscFreqList[index].setDefaultValue("0")
        symbolRefoscFreqList[index].setReadOnly(True)
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_ENABLE"
        symbolRefoscFreqList[index].setDependencies(updateRefFreq, [targetName])
        index += 1
    dswdtValGrp_DEVCFG2__DSWDTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="DEVCFG2__DSWDTEN"]')

    if dswdtValGrp_DEVCFG2__DSWDTEN is not None:
        dswdt_clk_freq = clk_comp.createIntegerSymbol("DSWDT_CLOCK_FREQUENCY", sym_calc_freq_menu)
        dswdt_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
    print("getBitMask:  cannot find ",bitfield)
    return ''  # should never get here

def updateMpllBitfield(symbol, event):
    # updates a bitfield value
    global MPLLDIS_VALUE
    global MPLLIDIV_VALUE
    global MPLLMULT_VALUE
    global MPLLODIV1_VALUE
    global MPLLODIV2_VALUE
    global MPLLVREGDIS_VALUE
    global MPLLINTVREFCON_VALUE

    if(event["id"]=="CLK_MPLLDIS"):
        MPLLDIS_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_MPLLIDIV"):
        MPLLIDIV_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_MPLLMULT"):
        MPLLMULT_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_MPLLODIV1"):
        MPLLODIV1_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_MPLLODIV2"):
        MPLLODIV2_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_MPLLVREGDIS"):
        MPLLVREGDIS_VALUE.setValue(event["value"],2)
    elif(event["id"]=="CLK_INTVREFCON"):
        MPLLINTVREFCON_VALUE.setValue(event["value"],2)

def updateCfgMpll(symbol, event):
    # updates the CFGMPLL register based on its constituent bitfields changing value
    global CFGMPLL_REGVALUE
    global MPLLDIS_BITFIELDMASK
    global MPLLIDIV_BITFIELDMASK
    global MPLLMULT_BITFIELDMASK
    global MPLLODIV1_BITFIELDMASK
    global MPLLODIV2_BITFIELDMASK
    global MPLLVREGDIS_BITFIELDMASK
    global MPLLINTVREFCON_BITFIELDMASK
    global mpllDisable
    global mpllidiv
    global mpllmult
    global mpllodiv1
    global mpllodiv2
    global mpllvregdis
    global mpllintvrefcon
    global MPLLDIS_BIT_VALUE
    global MPLLIDIV_BITS_VALUE
    global MPLLMULT_BITS_VALUE
    global MPLLODIV1_BITS_VALUE
    global MPLLODIV2_BITS_VALUE
    global MPLLVREGDIS_BIT_VALUE
    global MPLLINTVREFCON_BIT_VALUE

    startVal = int(CFGMPLL_REGVALUE.getValue(),16)
    if(event["id"]=='CLK_MPLLDIS_VALUE'):
        mask = int(MPLLDIS_BITFIELDMASK.getValue())
        newValue = mpllDisable[event["value"]]
        MPLLDIS_BIT_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLIDIV_VALUE'):
        mask = int(MPLLIDIV_BITFIELDMASK.getValue())
        newValue = mpllidiv[event["value"]]
        MPLLIDIV_BITS_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLMULT_VALUE'):
        mask = int(MPLLMULT_BITFIELDMASK.getValue())
        newValue = mpllmult[event["value"]]
        MPLLMULT_BITS_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLODIV1_VALUE'):
        mask = int(MPLLODIV1_BITFIELDMASK.getValue())
        newValue = mpllodiv1[event["value"]]
        MPLLODIV1_BITS_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLODIV2_VALUE'):
        mask = int(MPLLODIV2_BITFIELDMASK.getValue())
        newValue = mpllodiv2[event["value"]]
        MPLLODIV2_BITS_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLVREGDIS_VALUE'):
        mask = int(MPLLVREGDIS_BITFIELDMASK.getValue())
        newValue = mpllvregdis[event["value"]]
        MPLLVREGDIS_BIT_VALUE.setValue(newValue,1)
    elif(event["id"]=='CLK_MPLLINTVREFCON_VALUE'):
        mask = int(MPLLINTVREFCON_BITFIELDMASK.getValue())
        newValue = mpllintvrefcon[event["value"]]
        MPLLINTVREFCON_BIT_VALUE.setValue(newValue,1)

    bitPosn = 0  # find bitshift from mask
    while( (mask & (1<<bitPosn)) == 0):
        bitPosn += 1
    startVal = startVal & ~mask
    startVal = startVal | (int(newValue) << bitPosn)
    CFGMPLL_REGVALUE.setValue(str(hex(startVal)),1)

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

    # atdf-specific areas
    clkValGrp_DEVCFG1__FSOSCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="DEVCFG1__FSOSCEN"]')
    clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__FRCDIV"]')
    clkValGrp_REFO1CON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__ROSEL"]')
    clkValGrp_REFO1CON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__RODIV"]')
    clkValGrp_REFO1TRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1TRIM__ROTRIM"]')

    clkReg_CFGMPLL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGMPLL"]')
    clkValGrp_CFGMPLL__MPLLIDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLIDIV"]')
    clkValGrp_CFGMPLL__MPLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLMULT"]')
    clkValGrp_CFGMPLL__MPLLODIV1 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLODIV1"]')
    clkValGrp_CFGMPLL__MPLLODIV2 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLODIV2"]')
    clkValGrp_CFGMPLL__MPLLDIS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLDIS"]')
    clkValGrp_CFGMPLL__MPLLVREGDIS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__MPLLVREGDIS"]')
    clkValGrp_CFGMPLL__INTVREFCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/value-group@[name="CFGMPLL__INTVREFCON"]')

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
    if( Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA"):
        CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mzda:MZDAClockModel")
        peripheralBusDict = peripheralBusDict_DA.copy()
    else:
        CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mz:MZClockModel")
        peripheralBusDict = peripheralBusDict_EF.copy()

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

    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):
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

                        elif(bitfield_tag.attrib["name"] == "ON"):  # ON field mask
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

    # Hiding temperature range selection feature for now
    TEMP_RANGE = coreComponent.createKeyValueSetSymbol("CONFIG_TEMPERATURE_RANGE", CLK_CFG_SETTINGS)
    TEMP_RANGE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    TEMP_RANGE.setLabel("Operating Temperature Range")
    TEMP_RANGE.setDescription("Maximum allowed System Clock Frequency will depend on selected Temperature Range")
    TEMP_RANGE.setVisible(False)
    TEMP_RANGE.setOutputMode("Value")
    TEMP_RANGE.setDisplayMode("Description")

    max_clk_freq_for_selected_temp = coreComponent.createIntegerSymbol("MAX_CLK_FREQ_FOR_SELECTED_TEMP_RANGE", CLK_CFG_SETTINGS)
    max_clk_freq_for_selected_temp.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    max_clk_freq_for_selected_temp.setLabel("Max System Clock Frequency (HZ) For Selected Temperature")
    max_clk_freq_for_selected_temp.setReadOnly(True)
    max_clk_freq_for_selected_temp.setVisible(False)

    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA"):
        TEMP_RANGE.addKey("RANGE1", "1", "-40C to +85C, DC to 200 MHz")
        TEMP_RANGE.setDefaultValue(0)
        TEMP_RANGE.setReadOnly(True)
        max_clk_freq_for_selected_temp.setDefaultValue(200000000)
    else:
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +125C, DC to 180 MHz")
        TEMP_RANGE.addKey("RANGE2", "1", "-40C to +85C, DC to 252 MHz")
        TEMP_RANGE.setDefaultValue(1)
        max_clk_freq_for_selected_temp.setDefaultValue(252000000)

    max_clk_freq_for_selected_temp.setDependencies(updateMaxFreq, ["CONFIG_TEMPERATURE_RANGE"])

    frcdiv = {}
    _get_bitfield_names(clkValGrp_OSCCON__FRCDIV, frcdiv)
    FRC_CLK_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_FRCDIV", CLK_CFG_SETTINGS, frcdiv.keys())
    FRC_CLK_SETTING.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    FRC_CLK_SETTING.setLabel("FRC Clock Divider")
    FRC_CLK_SETTING.setDescription(clkValGrp_OSCCON__FRCDIV.getAttribute('caption'))
    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA"):
        FRC_CLK_SETTING.setDefaultValue("DIV1")
    else:
        FRC_CLK_SETTING.setDefaultValue("OSC_FRC_DIV_1")
    FRC_CLK_SETTING.setVisible(True)

    # derived from above symbol - used in ftl file
    FRC_CLK_VALUE = coreComponent.createStringSymbol("SYS_CLK_FRCDIV", None)
    FRC_CLK_VALUE.setVisible(False)
    FRC_CLK_VALUE.setDefaultValue("0")
    FRC_CLK_VALUE.setDependencies(update_frc_div_value,["CONFIG_SYS_CLK_FRCDIV"])

    HAVE_REFCLK = coreComponent.createBooleanSymbol("CONFIG_HAVE_REFCLOCK", CLK_CFG_SETTINGS)
    HAVE_REFCLK.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    HAVE_REFCLK.setLabel("Have reference clock available")
    HAVE_REFCLK.setVisible(False)
    HAVE_REFCLK.setDefaultValue(True)

    # secondary oscillator enable - made this by default enabled
    soscen = {}
    _get_bitfield_names(clkValGrp_DEVCFG1__FSOSCEN, soscen)
    SOSC_EN_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_CONFIG_SOSCEN", CLK_CFG_SETTINGS, sorted(soscen.keys()))
    SOSC_EN_SETTING.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    SOSC_EN_SETTING.setLabel("Secondary oscillator enable")
    SOSC_EN_SETTING.setDescription(clkValGrp_DEVCFG1__FSOSCEN.getAttribute('caption'))
    SOSC_EN_SETTING.setVisible(False)

    deviceHasDDR2 = coreComponent.createBooleanSymbol("DEVICE_HAS_DDR2", CLK_CFG_SETTINGS)
    deviceHasDDR2.setVisible(False)

    # MPLL, which is only in certain families of MIPS devices
    if clkReg_CFGMPLL is not None:
        deviceHasDDR2.setDefaultValue(True)

        # MPLLDIS bitfield
        global mpllDisable
        mpllDisable = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLDIS, mpllDisable)
        MPLLDIS_SYM = coreComponent.createComboSymbol("CLK_MPLLDIS", CLK_CFG_SETTINGS, sorted(mpllDisable.keys()))
        MPLLDIS_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLDIS_SYM.setLabel(clkValGrp_CFGMPLL__MPLLDIS.getAttribute('caption'))
        MPLLDIS_SYM.setDescription(clkValGrp_CFGMPLL__MPLLDIS.getAttribute('caption'))
        MPLLDIS_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLDIS', clkValGrp_CFGMPLL__MPLLDIS))
        MPLLDIS_SYM.setVisible(True)

        global MPLLDIS_BITFIELDMASK
        MPLLDIS_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLDIS_MASK",None)
        MPLLDIS_BITFIELDMASK.setVisible(False)
        MPLLDIS_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLDIS'),16))

        global MPLLDIS_VALUE
        MPLLDIS_VALUE = coreComponent.createStringSymbol("CLK_MPLLDIS_VALUE",None)
        MPLLDIS_VALUE.setVisible(False)
        MPLLDIS_VALUE.setDefaultValue(MPLLDIS_SYM.getValue())
        MPLLDIS_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLDIS'])

        global MPLLDIS_BIT_VALUE
        MPLLDIS_BIT_VALUE =  coreComponent.createStringSymbol("CLK_MPLLDIS_BIT_VALUE",None)
        MPLLDIS_BIT_VALUE.setVisible(False)
        MPLLDIS_BIT_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLDIS', clkValGrp_CFGMPLL__MPLLDIS))

        # MPLLIDIV bitfield
        global mpllidiv
        mpllidiv = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLIDIV, mpllidiv)
        MPLLIDIV_SYM = coreComponent.createComboSymbol("CLK_MPLLIDIV", CLK_CFG_SETTINGS, sorted(mpllidiv.keys()))
        MPLLIDIV_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLIDIV_SYM.setLabel(clkValGrp_CFGMPLL__MPLLIDIV.getAttribute('caption'))
        MPLLIDIV_SYM.setDescription(clkValGrp_CFGMPLL__MPLLIDIV.getAttribute('caption'))
        MPLLIDIV_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLIDIV', clkValGrp_CFGMPLL__MPLLIDIV))
        MPLLIDIV_SYM.setVisible(True)

        global MPLLIDIV_BITFIELDMASK
        MPLLIDIV_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLIDIV_MASK",None)
        MPLLIDIV_BITFIELDMASK.setVisible(False)
        MPLLIDIV_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLIDIV'),16))

        global MPLLIDIV_VALUE
        MPLLIDIV_VALUE = coreComponent.createStringSymbol("CLK_MPLLIDIV_VALUE",None)
        MPLLIDIV_VALUE.setVisible(False)
        MPLLIDIV_VALUE.setDefaultValue(MPLLIDIV_SYM.getValue())
        MPLLIDIV_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLIDIV'])

        global MPLLIDIV_BITS_VALUE
        MPLLIDIV_BITS_VALUE =  coreComponent.createStringSymbol("CLK_MPLLIDIV_BITS_VALUE",None)
        MPLLIDIV_BITS_VALUE.setVisible(False)
        MPLLIDIV_BITS_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLIDIV', clkValGrp_CFGMPLL__MPLLIDIV))

        # MPLLMULT bitfield
        global mpllmult
        mpllmult = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLMULT, mpllmult)
        MPLLMULT_SYM = coreComponent.createComboSymbol("CLK_MPLLMULT", CLK_CFG_SETTINGS, sorted(mpllmult.keys()))
        MPLLMULT_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLMULT_SYM.setLabel(clkValGrp_CFGMPLL__MPLLMULT.getAttribute('caption'))
        MPLLMULT_SYM.setDescription(clkValGrp_CFGMPLL__MPLLMULT.getAttribute('caption'))
        MPLLMULT_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLMULT', clkValGrp_CFGMPLL__MPLLMULT))
        MPLLMULT_SYM.setVisible(True)

        global MPLLMULT_BITFIELDMASK
        MPLLMULT_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLMULT_MASK",None)
        MPLLMULT_BITFIELDMASK.setVisible(False)
        MPLLMULT_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLMULT'),16))

        global MPLLMULT_VALUE
        MPLLMULT_VALUE = coreComponent.createStringSymbol("CLK_MPLLMULT_VALUE",None)
        MPLLMULT_VALUE.setVisible(False)
        MPLLMULT_VALUE.setDefaultValue(MPLLMULT_SYM.getValue())
        MPLLMULT_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLMULT'])

        global MPLLMULT_BITS_VALUE
        MPLLMULT_BITS_VALUE =  coreComponent.createStringSymbol("CLK_MPLLMULT_BITS_VALUE",None)
        MPLLMULT_BITS_VALUE.setVisible(False)
        MPLLMULT_BITS_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLMULT', clkValGrp_CFGMPLL__MPLLMULT))

        # MPLLODIV1 bitfield
        global mpllodiv1
        mpllodiv1 = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLODIV1, mpllodiv1)
        MPLLODIV1_SYM = coreComponent.createComboSymbol("CLK_MPLLODIV1", CLK_CFG_SETTINGS, sorted(mpllodiv1.keys()))
        MPLLODIV1_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLODIV1_SYM.setLabel(clkValGrp_CFGMPLL__MPLLODIV1.getAttribute('caption'))
        MPLLODIV1_SYM.setDescription(clkValGrp_CFGMPLL__MPLLODIV1.getAttribute('caption'))
        MPLLODIV1_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLODIV1', clkValGrp_CFGMPLL__MPLLODIV1))
        MPLLODIV1_SYM.setVisible(True)

        global MPLLODIV1_BITFIELDMASK
        MPLLODIV1_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLODIV1_MASK",None)
        MPLLODIV1_BITFIELDMASK.setVisible(False)
        MPLLODIV1_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLODIV1'),16))

        global MPLLODIV1_VALUE
        MPLLODIV1_VALUE = coreComponent.createStringSymbol("CLK_MPLLODIV1_VALUE",None)
        MPLLODIV1_VALUE.setVisible(False)
        MPLLODIV1_VALUE.setDefaultValue(MPLLODIV1_SYM.getValue())
        MPLLODIV1_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLODIV1'])

        global MPLLODIV1_BITS_VALUE
        MPLLODIV1_BITS_VALUE =  coreComponent.createStringSymbol("CLK_MPLLODIV1_BITS_VALUE",None)
        MPLLODIV1_BITS_VALUE.setVisible(False)
        MPLLODIV1_BITS_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLODIV1', clkValGrp_CFGMPLL__MPLLODIV1))

        # MPLLODIV2 bitfield
        global mpllodiv2
        mpllodiv2 = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLODIV2, mpllodiv2)
        MPLLODIV2_SYM = coreComponent.createComboSymbol("CLK_MPLLODIV2", CLK_CFG_SETTINGS, sorted(mpllodiv2.keys()))
        MPLLODIV2_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLODIV2_SYM.setLabel(clkValGrp_CFGMPLL__MPLLODIV2.getAttribute('caption'))
        MPLLODIV2_SYM.setDescription(clkValGrp_CFGMPLL__MPLLODIV2.getAttribute('caption'))
        MPLLODIV2_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLODIV2', clkValGrp_CFGMPLL__MPLLODIV2))
        MPLLODIV2_SYM.setVisible(True)

        global MPLLODIV2_BITFIELDMASK
        MPLLODIV2_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLODIV2_MASK",None)
        MPLLODIV2_BITFIELDMASK.setVisible(False)
        MPLLODIV2_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLODIV2'),16))

        global MPLLODIV2_VALUE
        MPLLODIV2_VALUE = coreComponent.createStringSymbol("CLK_MPLLODIV2_VALUE",None)
        MPLLODIV2_VALUE.setVisible(False)
        MPLLODIV2_VALUE.setDefaultValue(MPLLODIV2_SYM.getValue())
        MPLLODIV2_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLODIV2'])

        global MPLLODIV2_BITS_VALUE
        MPLLODIV2_BITS_VALUE =  coreComponent.createStringSymbol("CLK_MPLLODIV2_BITS_VALUE",None)
        MPLLODIV2_BITS_VALUE.setVisible(False)
        MPLLODIV2_BITS_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLODIV2', clkValGrp_CFGMPLL__MPLLODIV2))

        # MPLLVREGDIS bitfield
        global mpllvregdis
        mpllvregdis = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__MPLLVREGDIS, mpllvregdis)
        MPLLVREGDIS_SYM = coreComponent.createComboSymbol("CLK_MPLLVREGDIS", CLK_CFG_SETTINGS, sorted(mpllvregdis.keys()))
        MPLLVREGDIS_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLVREGDIS_SYM.setLabel(clkValGrp_CFGMPLL__MPLLVREGDIS.getAttribute('caption'))
        MPLLVREGDIS_SYM.setDescription(clkValGrp_CFGMPLL__MPLLVREGDIS.getAttribute('caption'))
        MPLLVREGDIS_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'MPLLVREGDIS', clkValGrp_CFGMPLL__MPLLVREGDIS))
        MPLLVREGDIS_SYM.setVisible(True)

        global MPLLVREGDIS_BITFIELDMASK
        MPLLVREGDIS_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLVREGDIS_MASK",None)
        MPLLVREGDIS_BITFIELDMASK.setVisible(False)
        MPLLVREGDIS_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'MPLLVREGDIS'),16))

        global MPLLVREGDIS_VALUE
        MPLLVREGDIS_VALUE = coreComponent.createStringSymbol("CLK_MPLLVREGDIS_VALUE",None)
        MPLLVREGDIS_VALUE.setVisible(False)
        MPLLVREGDIS_VALUE.setDefaultValue(MPLLVREGDIS_SYM.getValue())
        MPLLVREGDIS_VALUE.setDependencies(updateMpllBitfield, ['CLK_MPLLVREGDIS'])

        global MPLLVREGDIS_BIT_VALUE
        MPLLVREGDIS_BIT_VALUE =  coreComponent.createStringSymbol("CLK_MPLLVREGDIS_BIT_VALUE",None)
        MPLLVREGDIS_BIT_VALUE.setVisible(False)
        MPLLVREGDIS_BIT_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'MPLLVREGDIS', clkValGrp_CFGMPLL__MPLLVREGDIS))

        #INTVREFCON bitfield
        global mpllintvrefcon
        mpllintvrefcon = {}
        _get_bitfield_names(clkValGrp_CFGMPLL__INTVREFCON, mpllintvrefcon)
        MPLLINTVREFCON_SYM = coreComponent.createComboSymbol("CLK_INTVREFCON", CLK_CFG_SETTINGS, sorted(mpllintvrefcon.keys()))
        MPLLINTVREFCON_SYM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        MPLLINTVREFCON_SYM.setLabel(clkValGrp_CFGMPLL__INTVREFCON.getAttribute('caption'))
        MPLLINTVREFCON_SYM.setDescription(clkValGrp_CFGMPLL__INTVREFCON.getAttribute('caption'))
        MPLLINTVREFCON_SYM.setDefaultValue(_get_default_value(clkReg_CFGMPLL, 'INTVREFCON', clkValGrp_CFGMPLL__INTVREFCON))
        MPLLINTVREFCON_SYM.setVisible(True)

        global MPLLINTVREFCON_BITFIELDMASK
        MPLLINTVREFCON_BITFIELDMASK = coreComponent.createHexSymbol("CLK_MPLLINTVREFCON_MASK",None)
        MPLLINTVREFCON_BITFIELDMASK.setVisible(False)
        MPLLINTVREFCON_BITFIELDMASK.setDefaultValue(int(getBitMask(clkReg_CFGMPLL, 'INTVREFCON'),16))

        global MPLLINTVREFCON_VALUE
        MPLLINTVREFCON_VALUE = coreComponent.createStringSymbol("CLK_MPLLINTVREFCON_VALUE",None)
        MPLLINTVREFCON_VALUE.setVisible(False)
        MPLLINTVREFCON_VALUE.setDefaultValue(MPLLINTVREFCON_SYM.getValue())
        MPLLINTVREFCON_VALUE.setDependencies(updateMpllBitfield, ['CLK_INTVREFCON'])

        global MPLLINTVREFCON_BIT_VALUE
        MPLLINTVREFCON_BIT_VALUE =  coreComponent.createStringSymbol("CLK_MPLLINTVREFCON_BIT_VALUE",None)
        MPLLINTVREFCON_BIT_VALUE.setVisible(False)
        MPLLINTVREFCON_BIT_VALUE.setDefaultValue(_get_default_value_num(clkReg_CFGMPLL, 'INTVREFCON', clkValGrp_CFGMPLL__INTVREFCON))

        # CFGMPLL register
        CFGMPLL_REGNAME = coreComponent.createStringSymbol("CLK_CFGMPLL_REG",None)
        CFGMPLL_REGNAME.setVisible(False)
        CFGMPLL_REGNAME.setDefaultValue(clkReg_CFGMPLL.getAttribute('name'))

        # CFGMPLL value
        global CFGMPLL_REGVALUE
        CFGMPLL_REGVALUE = coreComponent.createStringSymbol("CLK_CFGMPLL_REGVALUE",None)
        CFGMPLL_REGVALUE.setVisible(False)
        CFGMPLL_REGVALUE.setDefaultValue(clkReg_CFGMPLL.getAttribute('initval'))
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLDIS_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLIDIV_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLMULT_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLODIV1_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLODIV2_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLVREGDIS_VALUE'])
        CFGMPLL_REGVALUE.setDependencies(updateCfgMpll, ['CLK_MPLLINTVREFCON_VALUE'])
        # End of PIC32MZDA-specific registers

    else:
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
        symbolEnName.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        pbclkEnNameList.append(symbolEnId)
        symbolEnName.setLabel(labelEnVal)
        if(pbus=='1'):
            symbolEnName.setReadOnly(True)  # cannot disable peripheral bus 1
        symbolEnName.setDefaultValue(True)

        # PBDIV field
        symbolDivName = coreComponent.createIntegerSymbol(symbolDivId, symbolEnName)
        symbolDivName.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        if(pbus!='1'):  # cannot disable peripheral bus 1
            symbolDivName.setDependencies(enableMenu, [symbolEnId])
        symbolDivName.setLabel(labelDivVal)
        symbolDivName.setMin(1)
        symbolDivName.setMax(128)
        # get defaults from atdf file
        targetName = "__PB"+pbus+"_DEF_DIV"   # look for particular peripheral bus default divisor value
        params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
        paramsChildren = params.getChildren()
        for param in paramsChildren:
            if(param.getAttribute("name") == targetName):
                symbolDivName.setDefaultValue(int(param.getAttribute("value")))
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
        enSymbolList[listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        enSymbolList[listIndex].setLabel("Enable Reference Clock "+clk)
        enSymbolList[listIndex].setDescription("Sets whether to have reference clock 1 enabled")
        enSymbolList[listIndex].setDefaultValue(False)

        if( (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZEF") or ((Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA") and (int(clk) in [1,3,4])) ):
            # output enable of ref clk
            oeSymId = "CONFIG_SYS_CLK_REFCLK"+clk+"_OE"
            oeSymbolList[listIndex] = coreComponent.createBooleanSymbol(oeSymId, enSymbolList[listIndex])
            oeSymbolList[listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
        sourceSymbolList[listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
        rodivSymbolList[listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
        rotrimSymbolList[listIndex].setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
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
    POSC_IN_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    POSC_IN_FREQ.setLabel("Primary Oscillator Input Frequency (Hz)")
    POSC_IN_FREQ.setDependencies(updatePoscFreq, ["CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL"])
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__POSC_DEF_FREQ"]')
    POSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    newPoscFreq = node.getAttribute("value")
    SOSC_IN_FREQ.setDefaultValue(int(newPoscFreq))

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
            if str(instances[instance].getAttribute("name")) == "CMP":
                cmpRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]').getChildren()
                index = 1
                for register in cmpRegGroup:
                    regName = str(register.getAttribute("name"))
                    if regName.startswith("CM") and regName.endswith("CON"):
                        availablePeripherals.append("CMP" + str(index))
                        index += 1
            else:
                availablePeripherals.append(str(instances[instance].getAttribute("name")))

    #ADCHS Clock source
    global adchs_clock_map
    adchs_clock_map = {}
    adchs_clock_map[0] = "CONFIG_SYS_CLK_PBCLK3_FREQ"
    adchs_clock_map[1] = "SYS_CLK_FREQ"
    adchs_clock_map[2] = "CONFIG_SYS_CLK_REFCLK3_FREQ"
    adchs_clock_map[3] = "CONFIG_SYS_CLK_FRCDIV"

    peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLK_CONFIG", SYM_CLK_MENU)
    peripheralClockMenu.setLabel("Peripheral Clock Configuration")

    # calculated peripheral frequencies
    sym_peripheral_clock_enable = []
    sym_peripheral_clock_freq = []

    for peripheralName, peripheralBus in sorted(peripheralBusDict.items()):

        if peripheralName.startswith("REFO") or peripheralName in availablePeripherals:
            sym_peripheral_clock_enable.append(peripheralName + "_CLOCK_ENABLE")
            peripheral_clock_enable = coreComponent.createBooleanSymbol(peripheralName + "_CLOCK_ENABLE", peripheralClockMenu)
            peripheral_clock_enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
            peripheral_clock_enable.setLabel(peripheralName + " Clock Enable")
            peripheral_clock_enable.setReadOnly(len(peripheralBus) == 1)

            if ((peripheralBus[0] == "-1" or len(peripheralBus) == 1) and peripheralName != "DDR"):
                peripheral_clock_enable.setDefaultValue(True)
            elif peripheralName == "USB":
                peripheral_clock_enable.setDefaultValue(True)
            else:
                peripheral_clock_enable.setDefaultValue(False)

            sym_peripheral_clock_freq.append(peripheralName + "_CLOCK_FREQUENCY")
            peripheral_clock_freq = coreComponent.createIntegerSymbol(peripheralName + "_CLOCK_FREQUENCY", peripheral_clock_enable)
            peripheral_clock_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
            peripheral_clock_freq.setLabel(peripheralName + " Clock Frequency")
            peripheral_clock_freq.setReadOnly(True)

            if peripheralBus[0] == "-1" or len(peripheralBus) == 1:
                if peripheralName == "RTCC":
                    sym_peripheral_clock_enable.remove("RTCC_CLOCK_ENABLE")
                    peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ")))
                    peripheral_clock_freq.setDependencies(rtccClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "rtcc.RTCC_CLOCK_SOURCE", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                         "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])
                elif peripheralName == "DDR":
                    peripheral_clock_freq.setDefaultValue(0)
                    peripheral_clock_freq.setDependencies(sysPeripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "SYS_CLK_FREQ"])
                else:
                    peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))
                    peripheral_clock_freq.setDependencies(sysPeripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "SYS_CLK_FREQ"])
            elif peripheralName == "USB":
                peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ")))
                peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ"])
            else:
                peripheral_clock_freq.setDefaultValue(0)

                if (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA") and peripheralName.startswith("UART"):
                    peripheral_clock_freq.setDependencies(uartClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".UART_CLKSEL", "CONFIG_SYS_CLK_FRCDIV",
                                                                                         "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ"])
                elif (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MZDA") and peripheralName == "TMR1":
                    peripheral_clock_freq.setDependencies(tmr1ClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "tmr1.TIMER1_SRC_SEL", "tmr1.TIMER1_TECS", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                         "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])
                elif peripheralName == "ADCHS":
                    peripheral_clock_freq.setDependencies(adchsClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "adchs.ADCCON3__ADCSEL", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                        "SYS_CLK_FREQ", "CONFIG_SYS_CLK_REFCLK3_FREQ", "CONFIG_SYS_CLK_FRCDIV"])
                elif peripheralName.startswith("SPI"):
                    peripheral_clock_freq.setDependencies(spiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".SPI_MASTER_CLOCK", "CONFIG_SYS_CLK_PBCLK" + peripheralBus[0] + "_FREQ",
                                                                                        "CONFIG_SYS_CLK_REFCLK1_FREQ"])
                elif peripheralName.startswith("SQI"):
                    peripheral_clock_freq.setDependencies(sqiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_REFCLK2_FREQ"])
                elif peripheralName.startswith("SDHC"):
                    peripheral_clock_freq.setDependencies(sdhcClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_REFCLK4_FREQ"])
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
        pmdxRegMaskValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mz;register:%NOREGISTER%")
        pmdxRegMaskValue.setLabel("PMD" + str(i) + " Register Value")
        pmdxRegMaskValue.setDefaultValue(pmdDict[i])
        pmdxRegMaskValue.setReadOnly(True)

    defaultPMDxEnableDict = {k: v for k, v in peripheralBusDict.items() if((v[0] == "-1" and k != "DDR") or k == "USB")}

    for peripheralName, peripheralBus in defaultPMDxEnableDict.items():
        if peripheralName.startswith("REFO") or peripheralName in availablePeripherals:
            #Enable Peripheral from PMD
            periPMDRegId = "PMD" + peripheralBus[1] + "_REG_VALUE"
            pmdxValue = Database.getSymbolValue("core", periPMDRegId)
            periPMDRegBitShift = 1 << int(peripheralBus[2])
            Database.setSymbolValue("core", periPMDRegId, pmdxValue & ~periPMDRegBitShift, 1)

    # File handling below
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32mz/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32mz/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mz/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mz/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
