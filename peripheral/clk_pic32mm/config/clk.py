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

""" PIC32MK Clock Configuration File. """
from os.path import join
from xml.etree import ElementTree

global enableMenu
global updateRefFreq
global get_val_from_str
global set_refocon_value
global set_refotrim_value

global _process_valuegroup_entry

global LPRC_DEFAULT_FREQ
LPRC_DEFAULT_FREQ = 32768

global peripheralBusDict
peripheralBusDict = {}

peripheralBusDict_GPM =  {

        #Peripheral : ["PMD register no", "PMD register bit no"]
        "ADC": ["1", "0"],
        "VREF": ["1", "12"],
        "HLVD": ["1", "20"],

        "CMP1": ["2", "0"],
        "CMP2": ["2", "1"],
        "CMP3": ["2", "2"],
        "CLC1": ["2", "24"],
        "CLC2": ["2", "25"],
        "CLC3": ["2", "26"],
        "CLC4": ["2", "27"],

        "CCP1": ["3", "8"],
        "CCP2": ["3", "9"],
        "CCP3": ["3", "10"],
        "CCP4": ["3", "11"],
        "CCP5": ["3", "12"],
        "CCP6": ["3", "13"],
        "CCP7": ["3", "14"],
        "CCP8": ["3", "15"],
        "CCP9": ["3", "16"],

        "TMR1": ["4", "0"],
        "TMR2": ["4", "1"],
        "TMR3": ["4", "2"],

        "UART1": ["5", "0"],
        "UART2": ["5", "1"],
        "UART3": ["5", "2"],
        "SPI1": ["5", "8"],
        "SPI2": ["5", "9"],
        "SPI3": ["5", "10"],
        "I2C1": ["5", "16"],
        "I2C2": ["5", "17"],
        "I2C3": ["5", "18"],
        "USB": ["5", "24"],

        "RTCC": ["6", "0"],
        "REFO1": ["6", "8"],
       
        "DMAC": ["7", "4"],
}

peripheralBusDict_GPL =  {

        #Peripheral : ["PMD register no", "PMD register bit no"]
        "ADC": ["1", "0"],
        "VREF": ["1", "12"],
        "HLVD": ["1", "20"],

        "CMP1": ["2", "0"],
        "CMP2": ["2", "1"],
        "CLC1": ["2", "24"],
        "CLC2": ["2", "25"],

        "CCP1": ["3", "8"],
        "CCP2": ["3", "9"],
        "CCP3": ["3", "10"],

        "TMR1": ["4", "0"],

        "UART1": ["5", "0"],
        "UART2": ["5", "1"],
        "SPI1": ["5", "8"],
        "SPI2": ["5", "9"],

        "RTCC": ["6", "0"],
        "REFO1": ["6", "8"],
       
        "CRC": ["7", "3"],
}

global defaultEnablePeripheralsList

defaultEnablePeripheralsList_GPM = ["DMAC", "REFO1"]
defaultEnablePeripheralsList_GPL = ["REFO1"]

def _process_valuegroup_entry(node):
    '''
    Looks at input node and returns key name, description, and value for it.
       node:  <value ...> in atdf file.  A particular bitfield value for a particular register.
    '''
    stringval = node.getAttribute('value')
    newstring = stringval.replace('L','') # if has a "long" indicator at end, get rid of it
    value = int(newstring,16)
    return str(value)

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

def peripheralClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]

    if "_CLOCK_ENABLE" in event["id"] and event["value"]:
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
    elif Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        freq = int(event["value"])

    symbol.setValue(freq, 2)

# WDT
global wdtClockFreqCalc
def wdtClockFreqCalc(symbol,event):
    global LPRC_DEFAULT_FREQ
    wdtClkSrc = Database.getSymbolValue("core", "CONFIG_RCLKSEL")
    if  wdtClkSrc == "LPRC":
        symbol.setValue(LPRC_DEFAULT_FREQ)
    elif wdtClkSrc == "SYSCLK":
        symbol.setValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))
    else:#FRC
        symbol.setValue(8000000)

def tmr1ClockFreqCalc(symbol, event):
    global LPRC_DEFAULT_FREQ
    freq = 0
    
    if Database.getSymbolValue("core", "TMR1_CLOCK_ENABLE"):
        tmr1ClkSrc = Database.getSymbolValue("tmr1", "TIMER1_SRC_SEL")
        tmr1ExtClkSrcIndex = Database.getSymbolValue("tmr1", "TIMER1_TECS")

        if tmr1ClkSrc == None or tmr1ClkSrc == 1:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
        else:
            if tmr1ExtClkSrcIndex == 0:#LPRC
                freq = LPRC_DEFAULT_FREQ
            elif tmr1ExtClkSrcIndex == 2:#SOSC
                freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))
            #else:#T1CK pin
            #    freq = int(Database.getSymbolValue("tmr1", "TIMER1_EXT_CLOCK_FREQ"))
        
    symbol.setValue(freq)

def ccpClockFreqCalc(symbol, event):
    freq = 0
    periName = symbol.getID().split("_")[0]
    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        ClkSrc = Database.getSymbolValue(periName.lower(), "CCP_CCPCON1_CLKSEL")
        if ClkSrc == None:
            freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
        else:
            if ClkSrc == 0: #Sys clk
                freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
            elif ClkSrc == 1: #REFCLK
                freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))            
            elif ClkSrc == 2: #SOSC
                freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))
      
    symbol.setValue(freq)    

def rtccClockFreqCalc(symbol, event):
    global LPRC_DEFAULT_FREQ
    freq = 0

    if Database.getSymbolValue("core", "RTCC_CLOCK_ENABLE"):
        rtccClkSrcIndex = Database.getSymbolValue("rtcc", "RTCC_CLOCK_SOURCE")

        if rtccClkSrcIndex == 2: #LPRC
            freq = LPRC_DEFAULT_FREQ
        elif rtccClkSrcIndex == 3: #SOSC
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))
        elif rtccClkSrcIndex == 1: #PWRLCLK
            freq = int(Database.getSymbolValue("rtcc", "RTCC_PWRLCLK_PIN_FREQ"))            
        else: #pbclk
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
            
    symbol.setValue(freq)

def uartClockFreqCalc(symbol, event):
    freq = 0
    periName = symbol.getID().split("_")[0]
    uartClkSrc = Database.getSymbolValue(periName.lower(), "UART_CLKSEL")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if uartClkSrc == None or uartClkSrc == 3:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
        elif uartClkSrc == 2:
            freq = int(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
        elif uartClkSrc == 1:
            # calculate FRC frequency
            freqDiv = ''.join([i for i in Database.getSymbolValue("core", "CONFIG_SYS_CLK_FRCDIV") if i.isdigit()])
            freq = 8000000 / int(freqDiv)
        elif uartClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))

    symbol.setValue(freq, 1)

def adcClockFreqCalc(symbol, event):
    freq = 0
    periName = symbol.getID().split("_")[0]
    uartClkSrc = Database.getSymbolValue(periName.lower(), "AD1CON3__ADRC")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if uartClkSrc == None or uartClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
        else: #FRC
            freq = 8000000

    symbol.setValue(freq)

def spiClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]
    spiClkSrc = Database.getSymbolValue(periName.lower(), "SPI_MASTER_CLOCK")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if spiClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))
        else:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))

    symbol.setValue(freq, 1)

def updatePMDxRegValue(symbol, event):

    periName = event["id"].replace("_CLOCK_ENABLE", "")

    pmdRegId = "PMD" + peripheralBusDict[periName][0] + "_REG_VALUE"
    bitShift = 1 << int(peripheralBusDict[periName][1])

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
    symbolRefoscFreqList = []

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")

    sys_clk_freq = clk_comp.createStringSymbol("SYS_CLK_FREQ", sym_calc_freq_menu)
    sys_clk_freq.setLabel("System Clock Frequency (HZ)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setLabel("CPU Clock Frequency (HZ)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(node.getAttribute("value"))
    cpu_clk_freq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])

    # Peripheral Bus clock frequency
    symbolPbFreq = clk_comp.createStringSymbol("CONFIG_SYS_CLK_PBCLK_FREQ", sym_calc_freq_menu)
    symbolPbFreq.setLabel("Peripheral Bus Clock Frequency (Hz)")
    param = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__PB_DEF_FREQ"]')
    symbolPbFreq.setDefaultValue(param.getAttribute("value"))
    symbolPbFreq.setReadOnly(True)
    symbolPbFreq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])


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
        # get default value from atdf file
        index += 1

global find_lsb_position
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
    print("getBitMask:  cannot find ",bitfield)    # should never get here
    return ''

def update_OSCTUN(symbol, event):
    global OSCTUN_REG_VALUE_SYM
    OSCTUN_Value = OSCTUN_REG_VALUE_SYM.getValue()
    
    if event["id"] == "FRC_TUNING_ENABLE":
        bit_pos_ON = 15
        if event["value"] == True:
            OSCTUN_Value |= 1 << bit_pos_ON
        else:
            OSCTUN_Value &= ~(1 << bit_pos_ON)
    elif event["id"] == "FRC_TUNING_SOURCE":
        bit_pos_SRC = 12
        if event["value"] == 1:
            OSCTUN_Value |= 1 << bit_pos_SRC
        else: #0
            OSCTUN_Value &= ~(1 << bit_pos_SRC)

    OSCTUN_REG_VALUE_SYM.setValue(OSCTUN_Value)  

global updateSPLLCON
def updateSPLLCON(symbol, event):
    global PLLMULT_VALSYM
    global PLLODIV_VALSYM

    if Database.getSymbolValue("core", "CONFIG_PLLSRC") == "FRC":
        PLLICLK_Value = 1 << 7
    else:
        PLLICLK_Value = 0

    val = int(PLLODIV_VALSYM.getSelectedValue(), 16)
    PLLODIV_Value = val  << 24

    val = int(PLLMULT_VALSYM.getSelectedValue(), 16)
    MUL_Value = val  << 16

    symbol.setValue (PLLICLK_Value | PLLODIV_Value | MUL_Value)

def scan_atdf_for_spll_fields(coreComponent, CLK_CFG_SETTINGS):
    global _process_valuegroup_entry
    global atdf_content
    global symbolPllMultMask
    global symbolPllodivMask
    global symbolUposcenMask
    global pllmultKeyvals
    global pllodivKeyvals
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_REFO1CON__ROSEL
    global clkValGrp_REFO1CON__RODIV
    global clkValGrp_REFO1TRIM__ROTRIM
    global clkValGrp_SPLLCON__PLLMULT
    global clkValGrp_SPLLCON__PLLODIV
    global UPOSCEN_VALSYM
    global SPLL_SYM

    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):
                if(register_tag.attrib["name"] == "SPLLCON"):
                    SPLL_SYM = coreComponent.createMenuSymbol("CONFIG_SPLL", CLK_CFG_SETTINGS)
                    SPLL_SYM.setLabel("SPLL Clock Configuration")
                    SPLL_SYM.setVisible(True)

                    spllcon_RegName = coreComponent.createStringSymbol("SPLLCON_REG",None)
                    spllcon_RegName.setVisible(False)
                    spllcon_RegName.setDefaultValue(register_tag.attrib["name"])

                    for bitfield_tag in register_tag.iter("bitfield"):
                        if(bitfield_tag.attrib["name"] == "PLLMULT"):
                            '''
                            PLLMULT bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs
                            '''
                            items = clkValGrp_SPLLCON__PLLMULT.getChildren()  # all <value > children of this bitfield
                            global PLLMULT_VALSYM
                            PLLMULT_VALSYM = coreComponent.createKeyValueSetSymbol("PLLMULT_VAL", SPLL_SYM)
                            PLLMULT_VALSYM.setLabel("PLLMULT")
                            PLLMULT_VALSYM.setVisible(True)
                            PLLMULT_VALSYM.setOutputMode("Key")
                            PLLMULT_VALSYM.setDisplayMode("Key")
                            for index, ii in enumerate(items):
                                PLLMULT_VALSYM.addKey( ii.getAttribute("name"), ii.getAttribute("value"), ii.getAttribute("caption") )
                                if  ii.getAttribute("name") == "MUL_3":
                                    default = index
                                    default_MUL_Value  = int(ii.getAttribute("value"),16)
                            PLLMULT_VALSYM.setDefaultValue(default)
                        if(bitfield_tag.attrib["name"] == "PLLODIV"):  # PLLODIV field
                            '''
                            PLLODIV bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs
                            '''
                            items = clkValGrp_SPLLCON__PLLODIV.getChildren()  # all <value > children of this bitfield
                            global PLLODIV_VALSYM
                            PLLODIV_VALSYM = coreComponent.createKeyValueSetSymbol("PLLODIV_VAL", SPLL_SYM)
                            PLLODIV_VALSYM.setLabel("PLLODIV")
                            PLLODIV_VALSYM.setVisible(True)
                            PLLODIV_VALSYM.setOutputMode("Key")
                            PLLODIV_VALSYM.setDisplayMode("Key")
                            for index, ii in enumerate(items):
                                PLLODIV_VALSYM.addKey( ii.getAttribute("name"), ii.getAttribute("value"), ii.getAttribute("caption") )
                                if  ii.getAttribute("name") == "DIV_1":
                                    default = index
                                    default_PLLODIV_Value  = int(ii.getAttribute("value"),16)
                            PLLODIV_VALSYM.setDefaultValue(default)
                    
                    global updateSPLLCON
                    default_PLLICLK_Value = 1 # corresponds to CONFIG_PLLSRC = FRC
                    defaut_SPLLCON_Value = (default_MUL_Value << 16) | (default_PLLODIV_Value << 24) | (default_PLLICLK_Value << 7)
                    spllcon_RegValue = coreComponent.createHexSymbol("SPLLCON_REG_VALUE",None)
                    spllcon_RegValue.setVisible(False)
                    spllcon_RegValue.setDefaultValue(defaut_SPLLCON_Value)
                    spllcon_RegValue.setDependencies(updateSPLLCON, ["PLLODIV_VAL", "PLLMULT_VAL", "CONFIG_PLLSRC"])

if __name__ == "__main__":
    global atdf_content
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
    global symbolPllodivMask
    global symbolPllMultMask
    global roselmap
    global symbolRotrimmaskLsb
    global symbolRotrimMask
    global per_divider
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_REFO1CON__ROSEL
    global clkValGrp_REFO1CON__RODIV
    global clkValGrp_REFO1TRIM__ROTRIM
    global clkValGrp_SPLLCON__PLLMULT
    global clkValGrp_SPLLCON__PLLODIV
    global SPLLCON_VALSYM
    global pllmultKeyvals
    global pllodivKeyvals
    global SPLL_SYM
    global LPRC_DEFAULT_FREQ

    # atdf-specific areas
    clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__FRCDIV"]')
    clkValGrp_REFO1CON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__ROSEL"]')
    clkValGrp_REFO1CON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__RODIV"]')
    clkValGrp_REFO1TRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1TRIM__ROTRIM"]')
    clkValGrp_SPLLCON__PLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="SPLLCON__PLLMULT"]')
    clkValGrp_SPLLCON__PLLODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="SPLLCON__PLLODIV"]')

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
    CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mm:MMClockModel")
    if( Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MM1324"):
        peripheralBusDict = peripheralBusDict_GPL.copy()
        defaultEnablePeripheralsList = defaultEnablePeripheralsList_GPL
    else: #PIC32MM1387
        peripheralBusDict = peripheralBusDict_GPM.copy()
        defaultEnablePeripheralsList = defaultEnablePeripheralsList_GPM

    pbList = []
    symbolName = []
    symbolPbRegMaskLsb = []     # for REFOxCON:PBxDIV field bit shift, contains list of {symbolName, bus number}
    symbolPbRegMask = []        # for REFOxCON:PBxDIV mask, contains list of {symbolName, bus number}
    symbolPbOnMask = []         # for REFOxCON:ON mask, contains list of {symbolName, bus number}
    symbolRoselMaskList = []    # for REFOxCON:ROSEL mask, contains list of {symbolName, bus number}
    symbolRoselMaskLsbList = [] # for REFOxCON:ROSEL field bit shift, contains list of {symbolName, bus number}
    symbolDivswenMask = []      # for REFOxCON:DIVSWEN mask, contains list of {symbolName, bus number}
    symbolRodivMask = []        # for REFOxCON:RODIV mask, contains list of {symbolName, clock number}
    symbolRodivMaskLsb = []     # for REFOxCON:RODIV field bit shift, contains list of {symbolName, clock number}
    symbolRotrimmaskLsb = []    # for REFOxTRIM:ROTRIM field bit shift, contains list of {symbolName, clock number)
    symbolRotrimMask = []       # for REFOxTRIM:ROTRIM mask, contains list of {symbolName, clock number)
    symbolPllodivMask = []      # for SPLLCON:PLLODIV mask, contains list of symbols
    symbolPllMultMask = []      # for SPLLCON:PLLMULT mask, contains list of symbols
    refOscList = []
    index = 0

    # parse atdf file to get key parameters
    atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
    atdf_file = open(atdf_file_path, "r")
    atdf_content = ElementTree.fromstring(atdf_file.read())
    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):
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
    TEMP_RANGE.setLabel("Operating Temperature Range")
    TEMP_RANGE.setDescription("Maximum allowed System Clock Frequency will depend on selected Temperature Range")
    TEMP_RANGE.setVisible(False)
    TEMP_RANGE.setOutputMode("Value")
    TEMP_RANGE.setDisplayMode("Description")
    TEMP_RANGE.addKey("RANGE1", "0", "-40C to +125C, DC to 25 MHz")
    TEMP_RANGE.setDefaultValue(0)

    max_clk_freq_for_selected_temp = coreComponent.createIntegerSymbol("MAX_CLK_FREQ_FOR_SELECTED_TEMP_RANGE", CLK_CFG_SETTINGS)
    max_clk_freq_for_selected_temp.setLabel("Max System Clock Frequency (HZ) For Selected Temperature")
    max_clk_freq_for_selected_temp.setReadOnly(True)
    max_clk_freq_for_selected_temp.setVisible(False)
    max_clk_freq_for_selected_temp.setDefaultValue(25000000)

    frcdiv = {}
    _get_bitfield_names(clkValGrp_OSCCON__FRCDIV, frcdiv)
    FRC_CLK_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_FRCDIV", CLK_CFG_SETTINGS, frcdiv.keys())
    FRC_CLK_SETTING.setLabel("FRC Clock Divider")
    FRC_CLK_SETTING.setDescription(clkValGrp_OSCCON__FRCDIV.getAttribute('caption'))
    FRC_CLK_SETTING.setDefaultValue("DIV_1")
    FRC_CLK_SETTING.setVisible(True)

    # derived from above symbol - used in ftl file
    FRC_CLK_VALUE = coreComponent.createStringSymbol("SYS_CLK_FRCDIV", None)
    FRC_CLK_VALUE.setVisible(False)
    FRC_CLK_VALUE.setDefaultValue("0")
    FRC_CLK_VALUE.setDependencies(update_frc_div_value,["CONFIG_SYS_CLK_FRCDIV"])

    HAVE_REFCLK = coreComponent.createBooleanSymbol("CONFIG_HAVE_REFCLOCK", CLK_CFG_SETTINGS)
    HAVE_REFCLK.setLabel("Have reference clock available")
    HAVE_REFCLK.setVisible(False)
    HAVE_REFCLK.setDefaultValue(True)


    global roselSymbolList
    global refconval
    global symbolRoselValueList
    global refotrimval
    global symbolrefotrimval
    global rotrimSymbolList
    global symbolRotrimUserVal
    global roselMap
    global uposcenKeyvals
    enSymbolList = []
    oeSymbolList = []
    sourceSymbolList = []
    roselSymbolList = []
    rodivSymbolList = []
    rotrimSymbolList = []
    refconval = []
    symbolRoselValueList = []
    symbolRodivValueList = []
    symbolPbdiv = []
    refotrimval = []
    symbolrefotrimval = []
    symbolRotrimUserVal = []

    scan_atdf_for_spll_fields(coreComponent, CLK_CFG_SETTINGS)

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

    if ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/register-group@[name="CRU"]/register@[name="OSCTUN"]/bitfield@[name="ON"]') != None:
        OSCTUN_SYM = coreComponent.createMenuSymbol("CONFIG_OSCTUN", CLK_CFG_SETTINGS)
        OSCTUN_SYM.setLabel("FRC Tuning Configuration")
        OSCTUN_SYM.setVisible(True)

        frcTuningEnable_SYM = coreComponent.createBooleanSymbol("FRC_TUNING_ENABLE", OSCTUN_SYM)
        frcTuningEnable_SYM.setLabel("FRC Self Tuning Enable")
        frcTuningEnable_SYM.setDefaultValue(False)

        tuningSource_SYM = coreComponent.createKeyValueSetSymbol("FRC_TUNING_SOURCE", OSCTUN_SYM)
        tuningSource_SYM.setLabel("FRC Self Tuning Source")
        tuningSource_SYM.setVisible(True)
        tuningSource_SYM.setOutputMode("Value")
        tuningSource_SYM.setDisplayMode("Key")
        tuningSource_SYM.addKey( "32.768 kHz SOSC Clock", "0x0", "32.768 kHz SOSC Clock is used to tune FRC" )
        tuningSource_SYM.addKey( "USB Host Clock", "0x1", "USB Host Clock is used to tune FRC" )
        tuningSource_SYM.setDefaultValue(0)       

        global OSCTUN_REG_VALUE_SYM
        OSCTUN_REG_VALUE_SYM = coreComponent.createHexSymbol("OSCTUN_REG_VALUE", OSCTUN_SYM)
        OSCTUN_REG_VALUE_SYM.setDefaultValue(0x0)
        OSCTUN_REG_VALUE_SYM.setVisible(False)
        OSCTUN_REG_VALUE_SYM.setDependencies(update_OSCTUN, ["FRC_TUNING_ENABLE", "FRC_TUNING_SOURCE"])
          

    # primary oscillator frequency
    POSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL", CLK_CFG_SETTINGS)
    POSC_IN_FREQ.setLabel("Primary Oscillator Input Frequency (Hz)")
    POSC_IN_FREQ.setDependencies(updatePoscFreq, ["CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL"])
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__POSC_DEF_FREQ"]')
    POSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))
    POSC_IN_FREQ.setVisible(True)

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    newPoscFreq = node.getAttribute("value")
    SOSC_IN_FREQ.setDefaultValue(int(newPoscFreq))
    SOSC_IN_FREQ.setVisible(True)

    # REFCLKI pin frequency
    REFCLKI_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_REFCLKI_PIN", CLK_CFG_SETTINGS)
    REFCLKI_IN_FREQ.setLabel("REFCLKI Input Pin Frequency (Hz)")
    REFCLKI_IN_FREQ.setDefaultValue(32768)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, join, ElementTree, newPoscFreq)

    peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLK_CONFIG", SYM_CLK_MENU)
    peripheralClockMenu.setLabel("Peripheral Clock Configuration")

    sym_peripheral_clock_enable = []

    # Create "clock enable" and "clock frequency" symbols for all the peripherals which aare associated with PMD
    for peripheralName in sorted(peripheralBusDict.keys()):
        sym_peripheral_clock_enable.append(peripheralName + "_CLOCK_ENABLE")
        peripheral_clock_enable = coreComponent.createBooleanSymbol(peripheralName + "_CLOCK_ENABLE", peripheralClockMenu)
        peripheral_clock_enable.setLabel(peripheralName + " Clock Enable")
        peripheral_clock_enable.setReadOnly(False)

        if peripheralName in defaultEnablePeripheralsList:
            peripheral_clock_enable.setDefaultValue(True)
        else:
            peripheral_clock_enable.setDefaultValue(False)

        peripheral_clock_freq = coreComponent.createIntegerSymbol(peripheralName + "_CLOCK_FREQUENCY", peripheral_clock_enable)
        peripheral_clock_freq.setLabel(peripheralName + " Clock Frequency")
        peripheral_clock_freq.setReadOnly(True)

        if peripheralName in defaultEnablePeripheralsList:
            peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))
        else:
            peripheral_clock_freq.setDefaultValue(0)

        if peripheralName == "RTCC":
            peripheral_clock_freq.setDependencies(rtccClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "rtcc.RTCC_CLOCK_SOURCE", "CONFIG_SYS_CLK_PBCLK_FREQ",
                                                                                    "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", "rtcc.RTCC_PWRLCLK_PIN_FREQ"])                                                                                               
        elif peripheralName == "TMR1":
            peripheral_clock_freq.setDependencies(tmr1ClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "tmr1.TIMER1_SRC_SEL", "tmr1.TIMER1_TECS", "CONFIG_SYS_CLK_PBCLK_FREQ",
                                                                                    "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", "tmr1.TIMER1_EXT_CLOCK_FREQ"])
        elif peripheralName.startswith("SPI"):
            peripheral_clock_freq.setDependencies(spiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".SPI_MASTER_CLOCK", "CONFIG_SYS_CLK_REFCLK1_FREQ",
                                                                                    "CONFIG_SYS_CLK_PBCLK_FREQ"])
        elif peripheralName.startswith("UART"):
            peripheral_clock_freq.setDependencies(uartClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".UART_CLKSEL", "CONFIG_SYS_CLK_REFCLK1_FREQ",
                                                                                    "CONFIG_SYS_CLK_PBCLK_FREQ", "CONFIG_SYS_CLK_FRCDIV", "SYS_CLK_FREQ"])
        elif peripheralName.startswith("ADC"):
            peripheral_clock_freq.setDependencies(adcClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".AD1CON3__ADRC", "CONFIG_SYS_CLK_PBCLK_FREQ"])       
        elif peripheralName.startswith("CCP"):
            peripheral_clock_freq.setDependencies(ccpClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".CCP_CCPCON1_CLKSEL", "SYS_CLK_FREQ",
                                                                                    "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", "CONFIG_SYS_CLK_REFCLK1_FREQ"])            
        else:
            peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK_FREQ"])


    cfgRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]').getChildren()

    pmdCount = 0
    pmdDict = {}

    for register in cfgRegGroup:
        regName = str(register.getAttribute("name"))
        if regName.startswith("PMD") and regName != "PMDCON":
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
            periPMDRegId = "PMD" + peripheralBusDict[peripheralName][0] + "_REG_VALUE"
            pmdxValue = Database.getSymbolValue("core", periPMDRegId)
            periPMDRegBitShift = 1 << int(peripheralBusDict[peripheralName][1])
            Database.setSymbolValue("core", periPMDRegId, pmdxValue & ~periPMDRegBitShift, 1)

    # File handling below
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32mm/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32mm/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mm/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mm/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
    
