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
global get_val_from_str
global set_refocon_value
global set_pbdiv_value
global set_refotrim_value

global _process_valuegroup_entry
peripheralBusDict =  {"CORE": "7", # CPU or CORE
                      "CDAC3": "3",
                      "SPI2": "2",
                      "SPI3": "3",
                      "SPI1": "2",
                      "NVM": "1",
                      "RTCC": "6",
                      "SPI6": "3",
                      "SPI4": "3",
                      "SPI5": "3",
                      "CDAC1": "2",
                      "CDAC2": "3",
                      "WDT": "1",
                      "CMP": "2",
                      "ICAP5": "2",
                      "ICAP6": "2",
                      "ICAP7": "2",
                      "ICAP8": "2",
                      "ICAP1": "2",
                      "ICAP2": "2",
                      "ICAP3": "2",
                      "ICAP4": "2",
                      "EEPROM": "2",
                      "CAN": "5",
                      "ICAP9": "2",
                      "ADCHS": "5",
                      "DSCTRL": "6",
                      "CFG": "1",
                      "CTMU": "2",
                      "CRU": "1",
                      "TMR9": "2",
                      "ICAP10": "3",
                      "ICAP11": "3",
                      "ICAP12": "3",
                      "ICAP13": "3",
                      "ICAP14": "3",
                      "ICAP15": "3",
                      "ICAP16": "3",
                      "INT": "1",
                      "JTAG": "1",
                      "OCMP7": "2",
                      "OCMP8": "2",
                      "OCMP9": "2",
                      "OCMP1": "2",
                      "OCMP2": "2",
                      "OCMP3": "2",
                      "UART6": "3",
                      "OCMP4": "2",
                      "USB": "5",
                      "OCMP5": "2",
                      "OCMP6": "2",
                      "UART2": "2",
                      "UART3": "3",
                      "DMT": "1",
                      "UART4": "3",
                      "UART5": "3",
                      "GPIO": "4",
                      "UART1": "2",
                      "PMP": "2",
                      "OCMP11": "3",
                      "OCMP10": "3",
                      "OCMP15": "3",
                      "TMR8": "2",
                      "OCMP14": "3",
                      "TMR7": "2",
                      "OCMP13": "3",
                      "TMR6": "2",
                      "OCMP12": "3",
                      "TMR5": "2",
                      "TMR4": "2",
                      "TMR3": "2",
                      "TMR2": "2",
                      "OCMP16": "3",
                      "TMR1": "2"}

def updateMaxFreq(symbol, event):
    if event["value"] == 0:
        symbol.setValue(80000000, 2)
    elif event["value"] == 1:
        symbol.setValue(120000000, 2)

def periphFreqCalc(symbol, event):
    symbol.setValue(int(event["value"]), 2)
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

global calcCPUFreq
def calcCPUFreq(symbol, event):
    symbol.setValue(event["value"],1)

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
    sys_clk_freq.setLabel("System Clock Frequency (HZ)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setLabel("CPU Clock Frequency (HZ)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(node.getAttribute("value"))
    cpu_clk_freq.setDependencies(calcCPUFreq,["SYS_CLK_FREQ"])

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
        symbolRefoscFreqList[index].setVisible(False)
        targetName = "CONFIG_SYS_CLK_REFCLK"+ii+"_ENABLE"
        symbolRefoscFreqList[index].setDependencies(enableMenu, [targetName])
        # get default value from atdf file
        targetName = "__REFCLK" + ii + "_DEF_FREQ"
        params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
        paramsChildren = params.getChildren()
        for param in paramsChildren:  # find parameter we are interested in now
            if(param.getAttribute("name") == targetName):
                symbolRefoscFreqList[index].setDefaultValue(param.getAttribute("value"))
        symbolRefoscFreqList[index].setReadOnly(True)
        index += 1

def adchsClockFreqCalc(symbol, event):
    adchsClkSrc = (Database.getSymbolValue("adchs", "ADCCON3__ADCSEL"))
    if (adchsClkSrc != None and adchsClkSrc != 1):
        symbol.setValue(int(Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc])), 2)
    if adchsClkSrc == 1:
        # calculate FRC frequency
        symbol.setValue(8000000 / int(Database.getSymbolValue("core", adchs_clock_map[adchsClkSrc]).split("DIV")[1]), 2)

def spiClockFreqCalc(symbol, event):
    spiInstance = symbol.getID().split("_")[0]
    spiClkSrc = (Database.getSymbolValue(spiInstance.lower(), "SPI_MASTER_CLOCK"))
    if spiClkSrc == 0:
        clkFreq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK1_FREQ"))
    else:
        if spiInstance in ["SPI1", "SPI2"]:
            clkFreq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ"))
        else:
            clkFreq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK3_FREQ"))
    symbol.setValue(clkFreq)

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

def upllEnableUpdate(symbol, event):
    '''
    Updates symbol value based on core symbol value, taken from DEVCFG:UPLLEN field
    '''
    targetSym = "CONFIG_UPLLEN"
    upllEn = Database.getSymbolValue("core",targetSym)
    if(upllEn == 'OFF'):
        symbol.setValue(False,2)
    else:
        symbol.setValue(True,2)

global upllval_set_visibility

def upllval_set_visibility(symbol, event):
    global UPOSCEN_VALSYM
    global UFRCEN_VALSYM
    global UsbClkSrcUPOSCEN

    if (UPOSCEN_VALSYM.getValue() == "UPLL") and (UFRCEN_VALSYM.getValue() == UsbClkSrcUPOSCEN):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


def updateUpllcon(symbol, event):
    # updates the UPLLCON register value based on any of its bitfields being changed by the user
    global UPLLCON_VALSYM
    global symbolPllIdivMask
    global pllidivKeyVals
    global symbolPllRangeMask
    global pllrangeKeyvals
    global symbolPllMultMask
    global pllmultKeyvals
    global symbolPllodivMask
    global pllodivKeyvals
    global symbolUposcenMask
    global uposcenKeyvals

    startVal = UPLLCON_VALSYM.getValue()
    if(event['id']=='PLLRANGE_VAL'):
        startVal &= ~int(Database.getSymbolValue("core","PLLRANGE_MASK"),16)
        startVal |= int(pllrangeKeyvals[event['value']]) << 0
    elif(event['id']=='PLLIDIV_VAL'):
        startVal &= ~int(Database.getSymbolValue("core","PLLIDIV_MASK"),16)
        startVal |= int(pllidivKeyVals[event['value']]) << 8
    elif(event['id']=='PLLMULT_VAL'):
        startVal &= ~int(Database.getSymbolValue("core","PLLMULT_MASK"),16)
        startVal |= int(pllmultKeyvals[event['value']]) << 16
    elif(event['id']=='PLLODIV_VAL'):
        startVal &= ~int(Database.getSymbolValue("core","PLLODIV_MASK"),16)
        startVal |= int(pllodivKeyvals[event['value']]) << 24
    elif(event['id']=='UPOSCEN_VAL'):
        startVal &= ~int(Database.getSymbolValue("core","UPOSCEN_MASK"),16)
        startVal |= int(uposcenKeyvals[event['value']]) << 29 #int(Database.getSymbolValue("core","UPOSCEN_SHIFT"),16)
    UPLLCON_VALSYM.setValue(startVal,2)

def scan_atdf_for_upll_fields(coreComponent):
    global _process_valuegroup_entry
    global upllval_set_visibility
    global atdf_content
    global symbolPllRangeMask
    global symbolPllIdivMask
    global symbolPllMultMask
    global symbolPllodivMask
    global symbolUposcenMask
    global pllidivKeyVals
    global pllrangeKeyvals
    global pllmultKeyvals
    global pllodivKeyvals
    global uposcenKeyvals
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_REFO1CON__ROSEL
    global clkValGrp_REFO1CON__RODIV
    global clkValGrp_REFO1TRIM__ROTRIM
    global clkValGrp_UPLLCON__PLLRANGE
    global clkValGrp_UPLLCON__PLLIDIV
    global clkValGrp_UPLLCON__PLLMULT
    global clkValGrp_UPLLCON__PLLODIV
    global clkValGrp_UPLLCON__UPOSCEN
    global UPOSCEN_VALSYM
    global UPLL_SYM
    symbolName = []
    index = 0

    for register_group in atdf_content.iter("register-group"):
        if "CRU" in register_group.attrib["name"]:
            for register_tag in register_group.iter("register"):

                # looking for UPLLCON in atdf file

                if(register_tag.attrib["name"] == "UPLLCON"):
                    # register name for use in ftl file
                    symbolName.append([])
                    symbolName[index] = coreComponent.createStringSymbol("UPLLCON_REG",None)
                    symbolName[index].setVisible(False)
                    symbolName[index].setDefaultValue(register_tag.attrib["name"])
                    index += 1
                    for bitfield_tag in register_tag.iter("bitfield"):
                        if(bitfield_tag.attrib["name"] == "PLLRANGE"):  # PLLRANGE field
                            '''
                            PLLRANGE bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs

                                Default value set by DEVCFG2::FPLLRNG field
                            '''
                            items = clkValGrp_UPLLCON__PLLRANGE.getChildren()  # all <value > children of this bitfield
                            keyVals = {}
                            for ii in items:
                                if(ii.getAttribute("name") != ""):
                                    keyVals[ii.getAttribute("name")] = _process_valuegroup_entry(ii)
                            pllrangeKeyvals = keyVals
                            PLLRANGE_VALSYM = coreComponent.createComboSymbol("PLLRANGE_VAL", UPLL_SYM, sorted(keyVals.keys()))
                            PLLRANGE_VALSYM.setLabel("PLLRANGE")
                            PLLRANGE_VALSYM.setVisible(True)
                            PLLRANGE_VALSYM.setDefaultValue("RANGE_8_16_MHZ")
                            PLLRANGE_VALSYM.setDependencies(upllval_set_visibility, ["UPOSCEN_VAL","UFRCEN_VAL"])

                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            PLLRANGE_SYM = coreComponent.createStringSymbol("PLLRANGE_MASK", None)
                            PLLRANGE_SYM.setVisible(False)
                            PLLRANGE_SYM.setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPllRangeMask.append(PLLRANGE_SYM)

                        if(bitfield_tag.attrib["name"] == "PLLIDIV"):  # PLLIDIV field
                            '''
                            PLLIDIV bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs
                            '''
                            items = clkValGrp_UPLLCON__PLLIDIV.getChildren()  # all <value > children of this bitfield
                            keyVals = {}
                            for ii in items:
                                if(ii.getAttribute("name") != ""):
                                    keyVals[ii.getAttribute("name")] = _process_valuegroup_entry(ii)
                            pllidivKeyVals = keyVals
                            PLLIDIV_VALSYM = coreComponent.createComboSymbol("PLLIDIV_VAL", UPLL_SYM, sorted(keyVals.keys()))
                            PLLIDIV_VALSYM.setLabel("PLLIDIV")
                            PLLIDIV_VALSYM.setVisible(True)
                            PLLIDIV_VALSYM.setDefaultValue("DIV_1")
                            PLLIDIV_VALSYM.setDependencies(upllval_set_visibility, ["UPOSCEN_VAL", "UFRCEN_VAL"])

                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("PLLIDIV_MASK", None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPllIdivMask.append(symbolName[index])
                            index += 1

                        if(bitfield_tag.attrib["name"] == "PLLMULT"):  # PLLRANGE field
                            '''
                            PLLMULT bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs
                            '''
                            items = clkValGrp_UPLLCON__PLLMULT.getChildren()  # all <value > children of this bitfield
                            keyVals = {}
                            for ii in items:
                                if(ii.getAttribute("name") != ""):
                                    keyVals[ii.getAttribute("name")] = _process_valuegroup_entry(ii)
                            pllmultKeyvals = keyVals
                            PLLMULT_VALSYM = coreComponent.createComboSymbol("PLLMULT_VAL", UPLL_SYM, sorted(keyVals.keys()))
                            PLLMULT_VALSYM.setLabel("PLLMULT")
                            PLLMULT_VALSYM.setVisible(True)
                            PLLMULT_VALSYM.setDefaultValue("MUL_32")
                            PLLMULT_VALSYM.setDependencies(upllval_set_visibility, ["UPOSCEN_VAL", "UFRCEN_VAL"])

                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("PLLMULT_MASK", None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPllMultMask.append(symbolName[index])
                            index += 1

                        if(bitfield_tag.attrib["name"] == "PLLODIV"):  # PLLODIV field
                            '''
                            PLLODIV bitfield value
                                get key/value pairs first from atdf file
                                then define the combo symbol using those pairs
                            '''
                            items = clkValGrp_UPLLCON__PLLODIV.getChildren()  # all <value > children of this bitfield
                            keyVals = {}
                            for ii in items:
                                if(ii.getAttribute("name") != ""):
                                    keyVals[ii.getAttribute("name")] = _process_valuegroup_entry(ii)
                            pllodivKeyvals = keyVals
                            PLLODIV_VALSYM = coreComponent.createComboSymbol("PLLODIV_VAL", UPLL_SYM, sorted(keyVals.keys()))
                            PLLODIV_VALSYM.setLabel("PLLODIV")
                            PLLODIV_VALSYM.setVisible(True)
                            PLLODIV_VALSYM.setDefaultValue("DIV_8")
                            PLLODIV_VALSYM.setDependencies(upllval_set_visibility, ["UPOSCEN_VAL", "UFRCEN_VAL"])

                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("PLLODIV_MASK", None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolPllodivMask.append(symbolName[index])
                            index += 1

                        if(bitfield_tag.attrib["name"] == "UPOSCEN"):  # UPOSCEN field
                            # this is for bitfield mask value - put into a symbol for ftl file retrieval
                            symbolName.append([])
                            symbolName[index] = coreComponent.createStringSymbol("UPOSCEN_MASK", None)
                            symbolName[index].setVisible(False)
                            symbolName[index].setDefaultValue(bitfield_tag.attrib["mask"])
                            symbolUposcenMask.append(symbolName[index])
                            index += 1



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
    global symbolUposcenMask
    global symbolPllodivMask
    global symbolPllMultMask
    global symbolPllIdivMask
    global symbolPllRangeMask
    global roselmap
    global symbolPbdivList
    global symbolRotrimmaskLsb
    global symbolRotrimMask
    global per_divider
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_REFO1CON__ROSEL
    global clkValGrp_REFO1CON__RODIV
    global clkValGrp_REFO1TRIM__ROTRIM
    global clkValGrp_UPLLCON__PLLRANGE
    global clkValGrp_UPLLCON__PLLIDIV
    global clkValGrp_UPLLCON__PLLMULT
    global clkValGrp_UPLLCON__PLLODIV
    global clkValGrp_UPLLCON__UPOSCEN
    global UPOSCEN_VALSYM
    global UFRCEN_VALSYM
    global UPLLCON_VALSYM
    global pllrangeKeyvals
    global pllidivKeyVals
    global pllmultKeyvals
    global pllodivKeyvals
    global UPLL_SYM
    global UsbClkSrcUPOSCEN

    # atdf-specific areas
    clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="OSCCON__FRCDIV"]')
    clkValGrp_REFO1CON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__ROSEL"]')
    clkValGrp_REFO1CON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1CON__RODIV"]')
    clkValGrp_REFO1TRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="REFO1TRIM__ROTRIM"]')
    clkValGrp_UPLLCON__PLLRANGE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="UPLLCON__PLLRANGE"]')
    clkValGrp_UPLLCON__PLLIDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="UPLLCON__PLLIDIV"]')
    clkValGrp_UPLLCON__PLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="UPLLCON__PLLMULT"]')
    clkValGrp_UPLLCON__PLLODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="UPLLCON__PLLODIV"]')
    clkValGrp_UPLLCON__UPOSCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CRU"]/value-group@[name="UPLLCON__UPOSCEN"]')

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

    # Used to include family-specific code in ftl file
    PROC_FAM_SYMBOL = coreComponent.createStringSymbol("PROC_FAMILY",None)
    PROC_FAM_SYMBOL.setVisible(False)
    PROC_FAM_SYMBOL.setDefaultValue('Default')              # set to nominal value
    if("PIC32MK" in Variables.get("__PROCESSOR")):
        PROC_FAM_SYMBOL.setDefaultValue('PIC32MK')

    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_MIPS32", None)
    SYM_CLK_MENU.setLabel("Clock Menu")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mk:MKClockModel")

    # see if UPLL is enabled through FUSE configuration
    upllEnableSym = coreComponent.createBooleanSymbol("UPLL_EN", None)
    upllEnableSym.setVisible(False)
    targetSym = "CONFIG_UPLLEN"
    upllEn = Database.getSymbolValue("core",targetSym)
    if(upllEn == 'OFF'):
        upllEnableSym.setDefaultValue(False)
    else:
        upllEnableSym.setDefaultValue(True)
    upllEnableSym.setDependencies(upllEnableUpdate, [targetSym]) # in case user changes DEFCFG2:UPLLEN


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
    symbolUposcenMask = []      # for UPLLCON:UPOSCEN mask, contains list of symbols
    symbolPllodivMask = []      # for UPLLCON:PLLODIV mask, contains list of symbols
    symbolPllMultMask = []      # for UPLLCON:PLLMULT mask, contains list of symbols
    symbolPllIdivMask = []      # for UPLLCON:PLLIDIV mask, contains list of symbols
    symbolPllRangeMask = []     # for UPLLCON:PLLRANGE mask, contains list of symbols
    refOscList = []
    index = 0


    # parse atdf file to get key parameters
    atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
    atdf_file = open(atdf_file_path, "r")
    atdf_content = ElementTree.fromstring(atdf_file.read())
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
    TEMP_RANGE.setLabel("Operating Temperature Range")
    TEMP_RANGE.setDescription("Maximum allowed System Clock Frequency will depend on selected Temperature Range")
    TEMP_RANGE.setVisible(False)
    TEMP_RANGE.setOutputMode("Value")
    TEMP_RANGE.setDisplayMode("Description")
    TEMP_RANGE.addKey("RANGE1", "0", "-40C to +125C, DC to 80 MHz")
    TEMP_RANGE.addKey("RANGE2", "1", "-40C to +85C, DC to 120 MHz")
    TEMP_RANGE.setDefaultValue(1)

    max_clk_freq_for_selected_temp = coreComponent.createIntegerSymbol("MAX_CLK_FREQ_FOR_SELECTED_TEMP_RANGE", CLK_CFG_SETTINGS)
    max_clk_freq_for_selected_temp.setLabel("Max System Clock Frequency (HZ) For Selected Temperature")
    max_clk_freq_for_selected_temp.setReadOnly(True)
    max_clk_freq_for_selected_temp.setVisible(False)
    max_clk_freq_for_selected_temp.setDefaultValue(120000000)
    max_clk_freq_for_selected_temp.setDependencies(updateMaxFreq, ["CONFIG_TEMPERATURE_RANGE"])

    frcdiv = {}
    _get_bitfield_names(clkValGrp_OSCCON__FRCDIV, frcdiv)
    FRC_CLK_SETTING = coreComponent.createComboSymbol("CONFIG_SYS_CLK_FRCDIV", CLK_CFG_SETTINGS, frcdiv.keys())
    FRC_CLK_SETTING.setLabel("FRC Clock Divider")
    FRC_CLK_SETTING.setDescription(clkValGrp_OSCCON__FRCDIV.getAttribute('caption'))
    FRC_CLK_SETTING.setDefaultValue("DIV1")
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
    global uposcenKeyvals
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
        if(pbus=='1') or (pbus=='7'):
            symbolEnName.setReadOnly(True)  # cannot disable peripheral bus 1
        symbolEnName.setDefaultValue(True)

        # PBDIV field
        symbolDivName = coreComponent.createIntegerSymbol(symbolDivId, symbolEnName)
        if(pbus!='1') or (pbus!='7') :  # cannot disable peripheral bus 1 or 7
            symbolDivName.setDependencies(enableMenu, [symbolEnId])
        if(pbus=='7'):
            symbolDivName.setReadOnly(True)
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
    POSC_IN_FREQ.setVisible(True)

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    newPoscFreq = node.getAttribute("value")
    SOSC_IN_FREQ.setDefaultValue(int(newPoscFreq))
    SOSC_IN_FREQ.setVisible(True)

    # UPLL
    UPLL_SYM = coreComponent.createMenuSymbol("CONFIG_UPLL", CLK_CFG_SETTINGS)
    UPLL_SYM.setLabel("USB Clock Configuration")
    UPLL_SYM.setVisible(True)

    # UPOSCEN, Output Enable bit
    '''
        get key/value pairs first from atdf file
        then define the combo symbol using those pairs
    '''
    UsbClkSrcUPOSCEN = "USB Input Clock Source 1"
    items = clkValGrp_UPLLCON__UPOSCEN.getChildren()
    keyVals = {}
    for ii in items:  # get all key values from atdf file for this bitfield
        if(ii.getAttribute("name") != ""):
            keyVals[ii.getAttribute("name")] = _process_valuegroup_entry(ii)
    uposcenKeyvals = keyVals
    UPOSCEN_VALSYM = coreComponent.createComboSymbol("UPOSCEN_VAL",UPLL_SYM, ["UPLL","POSC"])
    UPOSCEN_VALSYM.setLabel(UsbClkSrcUPOSCEN)
    UPOSCEN_VALSYM.setVisible(True)
    UPOSCEN_VALSYM.setDefaultValue("UPLL")  # USB input clock is UPLL

    UFRCEN_VALSYM = coreComponent.createComboSymbol("UFRCEN_VAL", UPLL_SYM, ["FRC",UsbClkSrcUPOSCEN])
    UFRCEN_VALSYM.setLabel("USB Input Clock Source")
    UFRCEN_VALSYM.setVisible(True)
    UFRCEN_VALSYM.setDefaultValue(UsbClkSrcUPOSCEN)  # USB input clock is selected from UPOSCEN

    scan_atdf_for_upll_fields(coreComponent)


    # UPLLCON register value for use in ftl files
    UPLLCON_VALSYM = coreComponent.createHexSymbol("UPLLCON_REG_VALUE",None)
    UPLLCON_VALSYM.setVisible(False)
    defaultValue = int(pllrangeKeyvals[Database.getSymbolValue("core","PLLRANGE_VAL")]) << 0 | \
                   (int(pllidivKeyVals[Database.getSymbolValue("core","PLLIDIV_VAL")]) << 8) | \
                   (int(pllmultKeyvals[Database.getSymbolValue("core","PLLMULT_VAL")]) << 16) | \
                   (int(pllodivKeyvals[Database.getSymbolValue("core","PLLODIV_VAL")]) << 24) | \
                   (int(uposcenKeyvals[Database.getSymbolValue("core","UPOSCEN_VAL")]) << 29)
    UPLLCON_VALSYM.setDefaultValue(defaultValue)
    UPLLCON_VALSYM.setDependencies(updateUpllcon, ['PLLRANGE_VAL', 'PLLIDIV_VAL', 'PLLMULT_VAL', 'PLLODIV_VAL', 'UPOSCEN_VAL'])



    # this is added to resolve a dependency in ftl file
    HAVE_REFCLK5 = coreComponent.createBooleanSymbol("CONFIG_HAVE_REFCLOCK5", CLK_CFG_SETTINGS)
    HAVE_REFCLK5.setVisible(False)
    HAVE_REFCLK5.setDefaultValue(False)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, join, ElementTree, newPoscFreq)

    #ADCHS Clock source
    global adchs_clock_map
    adchs_clock_map = {}
    adchs_clock_map[0] = "CONFIG_SYS_CLK_PBCLK5_FREQ"
    adchs_clock_map[1] = "CONFIG_SYS_CLK_FRCDIV"
    adchs_clock_map[2] = "CONFIG_SYS_CLK_REFCLK3_FREQ"
    adchs_clock_map[3] = "SYS_CLK_FREQ"

    i = 0
    sym_peripheral_clock_freq = []
    # calculated peripheral frequencies
    for peripheralName, peripheralBus in peripheralBusDict.items():
        symbolID = peripheralName + "_CLOCK_FREQUENCY"
        sym_peripheral_clock_freq.append(i)
        sym_peripheral_clock_freq[i] = coreComponent.createIntegerSymbol(symbolID, None)
        sym_peripheral_clock_freq[i].setVisible(False)
        sym_peripheral_clock_freq[i].setReadOnly(True)
        sym_peripheral_clock_freq[i].setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK" + peripheralBus + "_FREQ")))
        if peripheralName == "ADCHS" :
            sym_peripheral_clock_freq[i].setDependencies(adchsClockFreqCalc, ["adchs.ADCCON3__ADCSEL", "CONFIG_SYS_CLK_PBCLK5_FREQ",
                                                                            "SYS_CLK_FREQ", "CONFIG_SYS_CLK_REFCLK3_FREQ", "CONFIG_SYS_CLK_FRCDIV"])
        elif "SPI" in peripheralName:
            sym_peripheral_clock_freq[i].setDependencies(spiClockFreqCalc, [peripheralName + ".SPI_MASTER_CLOCK", "CONFIG_SYS_CLK_PBCLK" + peripheralBus + "_FREQ", "CONFIG_SYS_CLK_REFCLK1_FREQ"])
        else:
            sym_peripheral_clock_freq[i].setDependencies(periphFreqCalc, ["CONFIG_SYS_CLK_PBCLK" + peripheralBus + "_FREQ"])
        i = i + 1

    # File handling below
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32mk/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32mk/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mk/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mk/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
