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

""" PIC32MX Clock Configuration File. """
from os.path import join
from xml.etree import ElementTree
import re

global enableMenu
global updateRefFreq
global get_val_from_str
global set_refocon_value
global set_refotrim_value

global peripheralModuleDisableDict
peripheralModuleDisableDict = {}

global LPRC_DEFAULT_FREQ
LPRC_DEFAULT_FREQ = 32768

peripheralModuleDisableDict_1xx_2xx_3xx_4xx = {

        #Peripheral : ["PMD register no", "PMD register bit no"]

        "ADC": ["1", "0"],
        "CTMU": ["1", "8"],
        "CVR": ["1", "12"],
        "HLVD": ["1", "20"],
        "CMP1": ["2", "0"],
        "CMP2": ["2", "1"],
        "CMP3": ["2", "2"],
        "ICAP1": ["3", "0"],
        "ICAP2": ["3", "1"],
        "ICAP3": ["3", "2"],
        "ICAP4": ["3", "3"],
        "ICAP5": ["3", "4"],
        "OCMP1": ["3", "16"],
        "OCMP2": ["3", "17"],
        "OCMP3": ["3", "18"],
        "OCMP4": ["3", "19"],
        "OCMP5": ["3", "20"],
        "TMR1": ["4", "0"],
        "TMR2": ["4", "1"],
        "TMR3": ["4", "2"],
        "TMR4": ["4", "3"],
        "TMR5": ["4", "4"],
        "UART1": ["5", "0"],
        "UART2": ["5", "1"],
        "UART3": ["5", "2"],
        "UART4": ["5", "3"],
        "UART5": ["5", "4"],
        "SPI1": ["5", "8"],
        "SPI2": ["5", "9"],
        "SPI3": ["5", "10"],
        "SPI4": ["5", "11"],
        "I2C1": ["5", "16"],
        "I2C2": ["5", "17"],
        "USB": ["5", "24"],
        "CAN1": ["5", "28"],
        "RTCC": ["6", "0"],
        "REFO": ["6", "1"],
        "PMP": ["6", "16"]
}

peripheralModuleDisableDict_5xx_6xx_7xx = {

#all the keys have empty list because 5xx/6xx/7xx series devices do not have PMD feature.

        "ADC": [],
        "CTMU": [],
        "CVR": [],
        "HLVD": [],
        "CMP1": [],
        "CMP2": [],
        "CMP3": [],
        "ICAP1": [],
        "ICAP2": [],
        "ICAP3": [],
        "ICAP4": [],
        "ICAP5": [],
        "OCMP1": [],
        "OCMP2": [],
        "OCMP3": [],
        "OCMP4": [],
        "OCMP5": [],
        "TMR1": [],
        "TMR2": [],
        "TMR3": [],
        "TMR4": [],
        "TMR5": [],
        "UART1": [],
        "UART2": [],
        "UART3": [],
        "UART4": [],
        "UART5": [],
        "UART6": [],
        "SPI1": [],
        "SPI2": [],
        "SPI3": [],
        "SPI4": [],
        "I2C1": [],
        "I2C2": [],
        "I2C3": [],
        "I2C4": [],
        "I2C5": [],
        "USB": [],
        "CAN1": [],
        "CAN2": [],
        "RTCC": [],
        "PMP": [],
        "ETH": []
}

def updateMaxFreq(symbol, event):
    if (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1185"):
        if event["value"] == 0:
            symbol.setValue(80000000, 2)
        elif event["value"] == 1:
            symbol.setValue(100000000, 2)
        elif event["value"] == 2:
            symbol.setValue(120000000, 2)
    elif (Database.getSymbolValue("core", "PRODUCT_FAMILY") in ["PIC32MX1168", "PIC32MX1290"]):
        if event["value"] == 0:
            symbol.setValue(40000000, 2)
        elif event["value"] == 1:
            symbol.setValue(50000000, 2)

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
        freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
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
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
        else:
            if tmr1ExtClkSrc != None:
                if tmr1ExtClkSrc == 0:
                    #LPRC Oscillator Frequency
                    freq = LPRC_DEFAULT_FREQ
                elif tmr1ExtClkSrc == 2:
                    #Secondary Oscillator Frequency
                    freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"))

    symbol.setValue(freq, 1)

def uartClockFreqCalc(symbol, event):

    freq = 0
    periName = symbol.getID().split("_")[0]
    uartClkSrc = Database.getSymbolValue(periName.lower(), "UART_CLKSEL")

    if Database.getSymbolValue("core", periName + "_CLOCK_ENABLE"):
        if uartClkSrc == None or uartClkSrc == 3 or uartClkSrc == 0:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))
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
            if Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK_FREQ") != None:
                freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_REFCLK_FREQ"))
        else:
            freq = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ"))

    symbol.setValue(freq, 1)

def canClockFreqCalc(symbol, event):

    symbol.setValue(int(Database.getSymbolValue("core", "SYS_CLK_FREQ")))

def updatePMDxRegValue(symbol, event):

    periName = event["id"].replace("_CLOCK_ENABLE", "")

    pmdRegId = "PMD" + peripheralModuleDisableDict[periName][0] + "_REG_VALUE"
    bitShift = 1 << int(peripheralModuleDisableDict[periName][1])

    pmdxValue = Database.getSymbolValue("core", pmdRegId)

    if event["value"]:
        pmdxValue = pmdxValue & ~bitShift
    else:
        pmdxValue = pmdxValue | bitShift

    Database.setSymbolValue("core", pmdRegId, pmdxValue, 1)

global cpuClockFreqCalc

def cpuClockFreqCalc(symbol, event):

    symbol.setValue(event["value"], 2)

global find_max_min
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

global _process_valuegroup_entry
def _process_valuegroup_entry(node):
    '''
    Looks at input node and returns key name, description, and value for it.
       node:  <value ...> in atdf file.  A particular bitfield value for a particular register.
    '''
    stringval = node.getAttribute('value')
    newstring = stringval.replace('L','') # if has a "long" indicator at end, get rid of it
    value = int(newstring,16)
    return str(value)

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
        if(ii.getAttribute('name').lower() != "reserved") and (ii.getAttribute('name').lower() != ""):
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            outputList[ii.getAttribute('name')] = str(tempint)

def check_for_usb_part(processor):
    '''
    This checks to see if the part has USB functionality in it or not.
    '''
    if(("110F016" in processor) or ("120F032" in processor) or ("130F064" in processor) or ("130F256" in processor) or
       ("170F256" in processor) or ("150F128" in processor) or ("330F064" in processor) or ("350F128" in processor) or
       ("350F256" in processor) or ("370F512" in processor) or ("120F064" in processor) or ("130F128" in processor) or
       ("150F256" in processor)  or ("170F512" in processor) or ("174F" in processor) or ("154F" in processor)):
        return False
    else:
        return True

def enableMenu(menu, event):
    # simple visible/invisible callback for menu items
    menu.setVisible(event["value"])

def updateRefFreq(menu, event):
    if event["value"] == True:
        # get default value from atdf file
        targetName = "__REFCLK_DEF_FREQ"
        params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
        paramsChildren = params.getChildren()
        for param in paramsChildren:  # find parameter we are interested in now
            if(param.getAttribute("name") == targetName):
                menu.setValue(param.getAttribute("value"),2)
    else:
        menu.setValue("0",2)

def get_val_from_str(stringVal):
    '''
    Converts string-based number to integer
    '''
    if(stringVal.find('0x')!=-1):
        intVal = int(stringVal[2:],16)
    else:
        intVal = int(stringVal)
    return intVal

global _find_val
def _find_val(keylist, keyval):
    '''
    Finds keylist member which has value keyval and returns corresponding value from list
        keylist: entire set of keys/values
        keyval:  particular key name we are interested in getting the value of
    '''
    values = keylist.values()
    keys = keylist.keys()
    for ii in range(len(values)):
        if(keyval == keys[ii]):
            return int(values[ii])


global item_update
def item_update(symbol, event):
    '''
    General setter callback function for any particular event that was used to call this callback
    '''
    symbol.setValue(event['value'],2)

global _get_default_value
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

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")
    sys_clk_freq = clk_comp.createStringSymbol("SYS_CLK_FREQ", sym_calc_freq_menu)
    sys_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    sys_clk_freq.setLabel("System Clock Frequency (HZ)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # CPU_CLOCK_FREQUENCY symbol is needed for SYS_TIME
    cpu_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    cpu_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    cpu_clk_freq.setLabel("CPU Clock Frequency (HZ)")
    cpu_clk_freq.setReadOnly(True)
    cpu_clk_freq.setDefaultValue(Database.getSymbolValue("core", "SYS_CLK_FREQ"))
    cpu_clk_freq.setDependencies(cpuClockFreqCalc,["SYS_CLK_FREQ"])

    # Peripheral Bus clock frequencies
    targetName = "CONFIG_SYS_CLK_PBCLK_FREQ"
    symbolPbFreqList = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
    symbolPbFreqList.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    symbolPbFreqList.setLabel("Peripheral Bus Clock Frequency (Hz)")
    targetName = "__PB_DEF_FREQ"
    params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
    paramsChildren = params.getChildren()
    for param in paramsChildren:  # find parameter we are interested in now
        if(param.getAttribute("name") == targetName):
            symbolPbFreqList.setDefaultValue(param.getAttribute("value"))
    symbolPbFreqList.setReadOnly(True)

    if clkRegGrp_REFOCON is not None:
        # Reference Clock frequency
        targetName = "CONFIG_SYS_CLK_REFCLK_FREQ"
        symbolRefoscFreqList = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
        symbolRefoscFreqList.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        symbolRefoscFreqList.setLabel("Reference Clock Frequency (Hz)")
        symbolRefoscFreqList.setVisible(True)
        symbolRefoscFreqList.setDefaultValue("0")
        symbolRefoscFreqList.setReadOnly(True)
        targetName = "CONFIG_SYS_CLK_REFCLK_ENABLE"
        symbolRefoscFreqList.setDependencies(updateRefFreq, [targetName])

    dswdtValGrp_DEVCFG2__DSWDTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="DEVCFG2__DSWDTEN"]')

    if dswdtValGrp_DEVCFG2__DSWDTEN is not None:
        dswdt_clk_freq = clk_comp.createIntegerSymbol("DSWDT_CLOCK_FREQUENCY", sym_calc_freq_menu)
        dswdt_clk_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        dswdt_clk_freq.setLabel("Deep Sleep WDT Clock Frequency (Hz)")
        dswdt_clk_freq.setDefaultValue(dswdtClockDefaultFreq())
        dswdt_clk_freq.setReadOnly(True)
        dswdt_clk_freq.setDependencies(dswdtClockFreqCalc,["CONFIG_DSWDTOSC","CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])

global find_lsb_position
def find_lsb_position(field):
    '''
    Given an string field representing an integer or hex value, return the least significant nonzero bit position.  Range: 0-31
    '''
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

global updateOscTun
def updateOscTun(symbol,event):
    '''
    Callback for updating OSCTUN register value symbol whenever any of its bitfields are changed.
    '''
    global symbolOsctunTunMask
    global symbolOsctunTunLsb

    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_OSCTUN"):
        mask = int(symbolOsctunTunMask.getValue(),16)
        lsb = symbolOsctunTunLsb.getValue()
        val = int(symObj.getValue()) << lsb
    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)

global updateRefotrim
def updateRefotrim(symbol,event):
    '''
    Callback for updating REFOTRIM register value symbol whenever any of its bitfields are changed.
    '''
    global symbolRefotrimTrimMask
    global symbolRefotrimTrimLsb

    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_ROTRIM"):
        mask = int(symbolRefotrimTrimMask.getValue(),16)
        lsb = symbolRefotrimTrimLsb.getValue()
        val = int(symObj.getValue()) << lsb
    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)

global updateUpllcon
def updateUpllcon(symbol, event):
    # updates the UPLLCON register value based on any of its bitfields being changed by the user
    global upllidiv
    global upllmult
    global upllodiv

    startVal = symbol.getValue()
    if(event['id']=='CONFIG_SYS_CLK_UPLLIDIV'):
        startVal &= ~int(Database.getSymbolValue("core","UPLLIDIV_MASK"),16)
        startVal |= int(upllidiv[event['value']]) << Database.getSymbolValue("core","UPLLIDIV_MASKLSB")
    elif(event['id']=='CONFIG_SYS_CLK_UPLLMULT'):
        startVal &= ~int(Database.getSymbolValue("core","UPLLMULT_MASK"),16)
        startVal |= int(upllmult[event['value']]) << Database.getSymbolValue("core","UPLLMULT_MASKLSB")
    elif(event['id']=='CONFIG_SYS_CLK_UPLLODIV'):
        startVal &= ~int(Database.getSymbolValue("core","UPLLODIV_MASK"),16)
        startVal |= int(upllodiv[event['value']]) << Database.getSymbolValue("core","UPLLODIV_MASKLSB")
    symbol.setValue(startVal,2)

global updateRefocon
def updateRefocon(symbol,event):
    '''
    Callback for updating REFOCON register value symbol whenever any of its bitfields are changed.
    '''
    global symbolRefoconRodivMask
    global symbolRefoconRodivLsb
    global symbolRefoconRoselMask
    global symbolRefoconRoselLsb
    global rosel

    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    tempval = (symbol.getValue())
    if(event["id"] == "CONFIG_SYS_CLK_RODIV"):
        mask = int(symbolRefoconRodivMask.getValue(),16)
        lsb = symbolRefoconRodivLsb.getValue()
        val = int(symObj.getValue()) << lsb
    elif(event["id"] == "CONFIG_SYS_CLK_ROSEL"):
        mask = int(symbolRefoconRoselMask.getValue(),16)
        lsb = symbolRefoconRoselLsb.getValue()
        val = int(rosel[symObj.getValue()]) << lsb   # rosel[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval, 1)

def scan_atdf_for_osccon_fields(coreComponent, parentMenu, submenu1):
    '''
    This creates all the symbols for OSCCON register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_OSCCON
    global clkRegGrp_OSCTUN
    global clkRegGrp_REFOCON
    global clkRegGrp_REFOTRIM
    global clkRegGrp_UPLLCON
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_OSCCON__NOSC
    global clkValGrp_OSCCON__OSWEN
    global clkValGrp_OSCCON__UFRCEN
    global clkValGrp_OSCCON__DRMEN
    global clkValGrp_OSCCON__SLP2SPD
    global clkValGrp_OSCTUN__TUN
    global clkValGrp_REFOCON__OE
    global clkValGrp_REFOCON__ON
    global clkValGrp_REFOCON__RODIV
    global clkValGrp_REFOCON__ROSEL
    global clkValGrp_REFOTRIM__ROTRIM
    global clkValGrp_UPLLCON__PLLMULT
    global clkValGrp_UPLLCON__PLLODIV
    global symbolOscconFrcdivVal
    global symbolOscconFrcdivMask
    global symbolOscconFrcdivLsb
    global frcdiv
    global symbolOscconUfrcenVal
    global symbolOscconUfrcenMask
    global symbolOscconUfrcenLsb
    global ufrcen
    global symbolOscconNoscVal
    global symbolOscconNoscMask
    global symbolOscconNoscLsb
    global nosc
    global symbolOscconOswenVal
    global symbolOscconOswenMask
    global symbolOscconOswenLsb
    global oswen
    global _get_bitfield_names
    global item_update
    global _get_default_value
    global per_divider
    global symbolEnId

    # Scan through bitfields of OSCCON register that can be overridden by DEVCFG or user selections and create symbols for them
    child = clkRegGrp_OSCCON.getChildren()
    for oscconNode in child:
        if(oscconNode.getAttribute("name") == "FRCDIV"):       # OSCCON[FRCDIV] bitfield
            symbolOscconFrcdivVal = coreComponent.createKeyValueSetSymbol("CONFIG_SYS_CLK_FRCDIV", parentMenu)
            symbolOscconFrcdivVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolOscconFrcdivVal.setDescription(clkValGrp_OSCCON__FRCDIV.getAttribute("caption"))
            symbolOscconFrcdivVal.setLabel(clkValGrp_OSCCON__FRCDIV.getAttribute("caption"))
            symbolOscconFrcdivVal.setOutputMode("Value")
            symbolOscconFrcdivVal.setDisplayMode("Key")
            symbolOscconFrcdivVal.setVisible(True)

            # to be used by FTL
            symbolOscconFrcdivDefaultVal = coreComponent.createStringSymbol("FRCDIV_DEFAULT", submenu1)
            symbolOscconFrcdivDefaultVal.setVisible(False)

            for id in range(0, len(clkValGrp_OSCCON__FRCDIV.getChildren())):
                valueName = clkValGrp_OSCCON__FRCDIV.getChildren()[id].getAttribute("name")
                value = clkValGrp_OSCCON__FRCDIV.getChildren()[id].getAttribute("value")
                description = clkValGrp_OSCCON__FRCDIV.getChildren()[id].getAttribute("caption")
                symbolOscconFrcdivVal.addKey(valueName, value, description)
                if valueName == _get_default_value(clkRegGrp_OSCCON, 'FRCDIV', clkValGrp_OSCCON__FRCDIV):
                    symbolOscconFrcdivDefaultVal.setDefaultValue(value)
                    symbolOscconFrcdivVal.setDefaultValue(id)

        elif(oscconNode.getAttribute("name") == "UFRCEN"):       # OSCCON[UFRCEN] bitfield
            ufrcen = {}
            _get_bitfield_names(clkValGrp_OSCCON__UFRCEN, ufrcen)
            symbolOscconUfrcenVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_UFRCEN", submenu1,["ON", "OFF"])
            symbolOscconUfrcenVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolOscconUfrcenVal.setDescription(clkValGrp_OSCCON__UFRCEN.getAttribute("caption"))
            symbolOscconUfrcenVal.setLabel(clkValGrp_OSCCON__UFRCEN.getAttribute("caption"))
            symbolOscconUfrcenVal.setVisible(True)
            symbolOscconUfrcenVal.setDefaultValue("OFF")

def scan_atdf_for_refocon_fields(coreComponent, parentMenu, submenu1):
    '''
    This creates all the symbols for REFOCON register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_REFOCON
    global clkValGrp_REFOCON__OE
    global clkValGrp_REFOCON__ON
    global clkValGrp_REFOCON__RODIV
    global clkValGrp_REFOCON__ROSEL
    global clkValGrp_REFOTRIM__ROTRIM
    global symbolRefoconOnVal
    global per_on
    global symbolRefoconValue
    global symbolRefoconRodivMask
    global symbolRefoconRodivLsb
    global symbolRefoconOeMask
    global symbolRefoconOeLsb
    global oe
    global symbolRefoconRoselMask
    global symbolRefoconRoselLsb
    global rosel
    global _get_bitfield_names
    global item_update
    global _get_default_value
    global updateRefocon
    global enSymId

    # Scan through bitfields of REFOCON
    if clkRegGrp_REFOCON is not None:
        child = clkRegGrp_REFOCON.getChildren()
        for oscrefoconNode in child:
            if(oscrefoconNode.getAttribute("name") == "RODIV"):       # REFOCON[RODIV] bitfield
                maxValue, minValue = find_max_min(clkValGrp_REFOCON__RODIV)
                symbolRefoconRodivVal = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_RODIV", submenu1)
                symbolRefoconRodivVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                symbolRefoconRodivVal.setVisible(False)
                symbolRefoconRodivVal.setMin(minValue)
                symbolRefoconRodivVal.setMax(maxValue)
                symbolRefoconRodivVal.setDescription(clkValGrp_REFOCON__RODIV.getAttribute("caption"))
                symbolRefoconRodivVal.setLabel(clkValGrp_REFOCON__RODIV.getAttribute("caption"))
                symbolRefoconRodivVal.setDependencies(enableMenu,[enSymId])
                symbolRefoconRodivVal.setDefaultValue(0)

                # bit mask and lsb for RODIV
                symbolRefoconRodivMask = coreComponent.createStringSymbol("RODIV_MASK", None)
                symbolRefoconRodivMask.setVisible(False)
                symbolRefoconRodivMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
                symbolRefoconRodivLsb = coreComponent.createIntegerSymbol("RODIV_MASKLSB", None)
                symbolRefoconRodivLsb.setVisible(False)
                lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
                symbolRefoconRodivLsb.setDefaultValue(lsb)

            elif(oscrefoconNode.getAttribute("name") == "ON"):       # REFOCON[OE] bitfield
                # bit mask and lsb for ON
                symbolRefoconOnMask = coreComponent.createStringSymbol("ON_MASK", None)
                symbolRefoconOnMask.setVisible(False)
                symbolRefoconOnMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))

            elif(oscrefoconNode.getAttribute("name") == "OE"):       # REFOCON[OE] bitfield
                symbolRefoconOeVal = coreComponent.createBooleanSymbol("CONFIG_SYS_CLK_OE", submenu1)
                symbolRefoconOeVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                symbolRefoconOeVal.setVisible(False)
                symbolRefoconOeVal.setDescription(clkValGrp_REFOCON__OE.getAttribute("caption"))
                symbolRefoconOeVal.setLabel(clkValGrp_REFOCON__OE.getAttribute("caption"))
                symbolRefoconOeVal.setDependencies(enableMenu,[enSymId])
                symbolRefoconOeVal.setDefaultValue(False)

                # bit mask and lsb for OE
                symbolRefoconOeMask = coreComponent.createStringSymbol("OE_MASK", None)
                symbolRefoconOeMask.setVisible(False)
                symbolRefoconOeMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))

            elif(oscrefoconNode.getAttribute("name") == "ROSEL"):       # REFOCON[ROSEL] bitfield
                rosel = {}
                _get_bitfield_names(clkValGrp_REFOCON__ROSEL, rosel)
                symbolRefoconRoselVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_ROSEL", submenu1, rosel.keys())
                symbolRefoconRoselVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                symbolRefoconRoselVal.setVisible(False)
                symbolRefoconRoselVal.setDescription(clkValGrp_REFOCON__ROSEL.getAttribute("caption"))
                symbolRefoconRoselVal.setLabel(clkValGrp_REFOCON__ROSEL.getAttribute("caption"))
                symbolRefoconRoselVal.setDependencies(enableMenu,[enSymId])
                symbolRefoconRoselVal.setDefaultValue(_get_default_value(clkRegGrp_REFOCON, 'ROSEL', clkValGrp_REFOCON__ROSEL))
                # bit mask and lsb for OE
                symbolRefoconRoselMask = coreComponent.createStringSymbol("ROSEL_MASK", None)
                symbolRefoconRoselMask.setVisible(False)
                symbolRefoconRoselMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
                symbolRefoconRoselLsb = coreComponent.createIntegerSymbol("ROSEL_MASKLSB", None)
                symbolRefoconRoselLsb.setVisible(False)
                lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
                symbolRefoconRoselLsb.setDefaultValue(lsb)

        initialRefoconVal = int(clkRegGrp_REFOCON.getAttribute('initval'),16)

        # to be used by FTL
        symbolRefoconDefaultValue = coreComponent.createHexSymbol("REFOCON_DEFAULT", None)
        symbolRefoconDefaultValue.setVisible(False)
        symbolRefoconDefaultValue.setDefaultValue(initialRefoconVal)

        # get initial value of REFOCON register from 'initval' field in atdf file
        symbolRefoconValue = coreComponent.createHexSymbol("REFOCON_VALUE", None)
        symbolRefoconValue.setVisible(False)
        symbolRefoconValue.setDefaultValue(initialRefoconVal)
        symbolRefoconValue.setDependencies(updateRefocon,['CONFIG_SYS_CLK_RODIV','CONFIG_SYS_CLK_ROSEL'])

def scan_atdf_for_osctun_fields(coreComponent, parentMenu):
    '''
    This creates all the symbols for OSCTUN register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkValGrp_OSCTUN__TUN
    global clkRegGrp_OSCTUN
    global updateOscTun
    global symbolOsctunTunMask
    global symbolOsctunTunLsb
    # Scan through bitfields of OSCTUN
    child = clkRegGrp_OSCTUN.getChildren()
    for osctunNode in child:
        if(osctunNode.getAttribute("name") == "TUN"):       # OSCTUN[TUN] bitfield
            maxValue, minValue = find_max_min(clkValGrp_OSCTUN__TUN)
            symbolOsctunTunVal = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_OSCTUN", parentMenu)
            symbolOsctunTunVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolOsctunTunVal.setDescription(clkValGrp_OSCTUN__TUN.getAttribute("caption"))
            symbolOsctunTunVal.setLabel(clkValGrp_OSCTUN__TUN.getAttribute("caption"))
            symbolOsctunTunVal.setMin(minValue)
            symbolOsctunTunVal.setMax(maxValue)
            symbolOsctunTunVal.setVisible(True)
            symbolOsctunTunVal.setDefaultValue(0)

            # bit mask and lsb for TUN
            symbolOsctunTunMask = coreComponent.createStringSymbol("TUN_MASK", None)
            symbolOsctunTunMask.setVisible(False)
            symbolOsctunTunMask.setDefaultValue(osctunNode.getAttribute("mask"))
            symbolOsctunTunLsb = coreComponent.createIntegerSymbol("TUN_MASKLSB", None)
            symbolOsctunTunLsb.setVisible(False)
            lsb = find_lsb_position(osctunNode.getAttribute("mask"))
            symbolOsctunTunLsb.setDefaultValue(lsb)

    # get initial value of OSCTUN register from 'initval' field in atdf file
    symbolOsctunValue = coreComponent.createHexSymbol("OSCTUN_VALUE", None)
    symbolOsctunValue.setVisible(False)
    initialOsctunVal = int((clkRegGrp_OSCTUN.getAttribute('initval')),16)

    # make updates to initialOsctunVal due to above bitfield values being changed
    symbolOsctunValue.setDefaultValue(initialOsctunVal)
    symbolOsctunValue.setDependencies(updateOscTun,['CONFIG_SYS_CLK_OSCTUN'])

def scan_atdf_for_refotrim_fields(coreComponent, parentMenu):
    '''
    This creates all the symbols for REFOTRIM register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global updateRefotrim
    global clkRegGrp_REFOTRIM
    global clkValGrp_REFOTRIM__ROTRIM
    global symbolRefotrimTrimMask
    global symbolRefotrimTrimLsb
    global enSymId
    # Scan through bitfields of REFOTRIM
    child = clkRegGrp_REFOTRIM.getChildren()
    for oscrefotrimNode in child:
        if(oscrefotrimNode.getAttribute("name") == "ROTRIM"):       # REFOTRIM[ROTRIM] bitfield
            maxValue, minValue = find_max_min(clkValGrp_REFOTRIM__ROTRIM)
            symbolRefotrimRotrimVal = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_ROTRIM", parentMenu)
            symbolRefotrimRotrimVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolRefotrimRotrimVal.setVisible(False)
            symbolRefotrimRotrimVal.setMin(minValue)
            symbolRefotrimRotrimVal.setMax(maxValue)
            symbolRefotrimRotrimVal.setDescription(clkValGrp_REFOTRIM__ROTRIM.getAttribute("caption"))
            symbolRefotrimRotrimVal.setLabel(clkValGrp_REFOTRIM__ROTRIM.getAttribute("caption"))
            symbolRefotrimRotrimVal.setDefaultValue(0)
            symbolRefotrimRotrimVal.setDependencies(enableMenu,[enSymId])
            # bit mask and lsb for ROTRIM
            symbolRefotrimTrimMask = coreComponent.createStringSymbol("ROTRIM_MASK", None)
            symbolRefotrimTrimMask.setVisible(False)
            symbolRefotrimTrimMask.setDefaultValue(oscrefotrimNode.getAttribute("mask"))
            symbolRefotrimTrimLsb = coreComponent.createIntegerSymbol("ROTRIM_MASKLSB", None)
            symbolRefotrimTrimLsb.setVisible(False)
            lsb = find_lsb_position(oscrefotrimNode.getAttribute("mask"))
            symbolRefotrimTrimLsb.setDefaultValue(lsb)

    # get initial value of REFOCON register from 'initval' field in atdf file
    symbolRefotrimValue = coreComponent.createHexSymbol("REFOTRIM_VALUE", None)
    symbolRefotrimValue.setVisible(False)
    initialRefotrimVal = int((clkRegGrp_REFOTRIM.getAttribute('initval')),16)
    symbolRefotrimValue.setDefaultValue(initialRefotrimVal)
    symbolRefotrimValue.setDependencies(updateRefotrim,['CONFIG_SYS_CLK_ROTRIM'])

def scan_atdf_for_upllcon_fields(coreComponent, parentMenu):
    '''
    This creates all the symbols for UPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_UPLLCON
    global clkValGrp_UPLLCON__PLLIDIV
    global upllidiv
    global symbolUpllconPllidivMask
    global symbolUpllconPllidivLsb
    global upllmult
    global symbolUpllconPllmultMask
    global symbolUpllconPllmultLsb
    global upllodiv
    global symbolUpllconPllodivMask
    global symbolUpllconPllodivLsb
    global updateUpllcon

    # Scan through bitfields of UPLLCON
    child = clkRegGrp_UPLLCON.getChildren()
    for upllconNode in child:
        if(upllconNode.getAttribute("name") == "PLLIDIV"):       # UPLLCON[PLLIDIV] bitfield
            upllidiv = {}
            _get_bitfield_names(clkValGrp_UPLLCON__PLLIDIV, upllidiv)
            symbolUpllconPllidivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_UPLLIDIV", parentMenu, upllidiv.keys())
            symbolUpllconPllidivVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolUpllconPllidivVal.setVisible(False)
            symbolUpllconPllidivVal.setDescription(clkValGrp_UPLLCON__PLLIDIV.getAttribute("caption"))
            symbolUpllconPllidivVal.setLabel(clkValGrp_UPLLCON__PLLIDIV.getAttribute("caption"))

            # on reset, this field is set to DEVCFG2<10:8>, UPLLIDIV bitfield
            targetsym = "CONFIG_UPLLIDIV"
            upllidivVal = Database.getSymbolValue("core",targetsym)
            for ii in upllidiv:
                if(ii == upllidivVal):
                    symbolUpllconPllidivVal.setDefaultValue(ii)
            symbolUpllconPllidivVal.setDependencies(item_update, ["core."+targetsym])  # update UPLLIDIV whenever user updates DEVCFG2<10:8>

            # bit mask and lsb for PLLIDIV
            symbolUpllconPllidivMask = coreComponent.createStringSymbol("UPLLIDIV_MASK", None)
            symbolUpllconPllidivMask.setVisible(False)
            symbolUpllconPllidivMask.setDefaultValue(upllconNode.getAttribute("mask"))
            symbolUpllconPllidivLsb = coreComponent.createIntegerSymbol("UPLLIDIV_MASKLSB", None)
            symbolUpllconPllidivLsb.setVisible(False)
            lsb = find_lsb_position(upllconNode.getAttribute("mask"))
            symbolUpllconPllidivLsb.setDefaultValue(lsb)

        elif(upllconNode.getAttribute("name") == "PLLMULT"):       # UPLLCON[PLLMULT] bitfield
            upllmult = {}
            _get_bitfield_names(clkValGrp_UPLLCON__PLLMULT, upllmult)
            symbolUpllconPllmultVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_UPLLMULT", parentMenu, upllmult.keys())
            symbolUpllconPllmultVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolUpllconPllmultVal.setVisible(True)
            symbolUpllconPllmultVal.setDescription(clkValGrp_UPLLCON__PLLMULT.getAttribute("caption"))
            symbolUpllconPllmultVal.setLabel(clkValGrp_UPLLCON__PLLMULT.getAttribute("caption"))
            symbolUpllconPllmultVal.setDefaultValue(_get_default_value(clkRegGrp_UPLLCON, 'PLLMULT', clkValGrp_UPLLCON__PLLMULT))

            # bit mask and lsb for PLLMULT
            symbolUpllconPllmultMask = coreComponent.createStringSymbol("UPLLMULT_MASK", None)
            symbolUpllconPllmultMask.setVisible(False)
            symbolUpllconPllmultMask.setDefaultValue(upllconNode.getAttribute("mask"))
            symbolUpllconPllmultLsb = coreComponent.createIntegerSymbol("UPLLMULT_MASKLSB", None)
            symbolUpllconPllmultLsb.setVisible(False)
            lsb = find_lsb_position(upllconNode.getAttribute("mask"))
            symbolUpllconPllmultLsb.setDefaultValue(lsb)

        elif(upllconNode.getAttribute("name") == "PLLODIV"):       # UPLLCON[PLLODIV] bitfield
            upllodiv = {}
            _get_bitfield_names(clkValGrp_UPLLCON__PLLODIV, upllodiv)
            symbolUpllconPllodivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_UPLLODIV", parentMenu, upllodiv.keys())
            symbolUpllconPllodivVal.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            symbolUpllconPllodivVal.setVisible(True)
            symbolUpllconPllodivVal.setDescription(clkValGrp_UPLLCON__PLLODIV.getAttribute("caption"))
            symbolUpllconPllodivVal.setLabel(clkValGrp_UPLLCON__PLLODIV.getAttribute("caption"))
            symbolUpllconPllodivVal.setDefaultValue(_get_default_value(clkRegGrp_UPLLCON, 'PLLODIV', clkValGrp_UPLLCON__PLLODIV))

            # bit mask and lsb for PLLODIV
            symbolUpllconPllodivMask = coreComponent.createStringSymbol("UPLLODIV_MASK", None)
            symbolUpllconPllodivMask.setVisible(False)
            symbolUpllconPllodivMask.setDefaultValue(upllconNode.getAttribute("mask"))
            symbolUpllconPllodivLsb = coreComponent.createIntegerSymbol("UPLLODIV_MASKLSB", None)
            symbolUpllconPllodivLsb.setVisible(False)
            lsb = find_lsb_position(upllconNode.getAttribute("mask"))
            symbolUpllconPllodivLsb.setDefaultValue(lsb)

    # get initial value of UPLLCON register from 'initval' field in atdf file
    symbolUpllconValue = coreComponent.createHexSymbol("UPLLCON_VALUE", None)
    symbolUpllconValue.setVisible(False)
    initialUpllconVal = int((clkRegGrp_UPLLCON.getAttribute('initval')),16)

    # make updates to initialUpllconVal due to upllidiv value being changed by DEVCFGx registers
    initialUpllconVal &= ~int(symbolUpllconPllidivMask.getValue(),16)
    initialUpllconVal |= int(upllidiv[symbolUpllconPllidivVal.getValue()]) << symbolUpllconPllidivLsb.getValue()

    symbolUpllconValue.setDefaultValue(initialUpllconVal)
    symbolUpllconValue.setDependencies(updateUpllcon,['CONFIG_SYS_CLK_UPLLIDIV','CONFIG_SYS_CLK_UPLLMULT','CONFIG_SYS_CLK_UPLLODIV'])

    # get initial value of UPLLCON register from 'initval' field in atdf file
    symbolUpllconDefaultValue = coreComponent.createHexSymbol("UPLLCON_DEFAULT_VALUE", None)
    symbolUpllconDefaultValue.setVisible(False)
    symbolUpllconDefaultValue.setDefaultValue(initialUpllconVal)
    symbolUpllconDefaultValue.setDependencies(updateUpllcon,['CONFIG_SYS_CLK_UPLLIDIV'])

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
    global atdf_content
    global clkRegGrp_OSCCON
    global clkRegGrp_OSCTUN
    global clkRegGrp_REFOCON
    global clkRegGrp_REFOTRIM
    global clkRegGrp_UPLLCON
    global clkValGrp_OSCCON__FRCDIV
    global clkValGrp_OSCCON__NOSC
    global clkValGrp_OSCCON__OSWEN
    global clkValGrp_OSCCON__UFRCEN
    global clkValGrp_OSCTUN__TUN
    global clkValGrp_OSCCON__DRMEN
    global clkValGrp_OSCCON__SLP2SPD
    global clkValGrp_OSCCON__SLOCK
    global clkValGrp_OSCCON__LOCK
    global clkValGrp_REFOCON__OE
    global clkValGrp_REFOCON__ON
    global clkValGrp_REFOCON__RODIV
    global clkValGrp_REFOCON__ROSEL
    global clkValGrp_REFOTRIM__ROTRIM
    global clkValGrp_REFOTRIM__ROTRIM
    global clkValGrp_UPLLCON__PLLIDIV
    global clkValGrp_UPLLCON__PLLMULT
    global clkValGrp_UPLLCON__PLLODIV
    global refconval
    global symbolRoselValueList
    global refotrimval
    global rotrimSymbolList
    global uposcenKeyvals
    symbolRoselValueList = []
    global enSymId
    global symbolEnId

    # this symbol is used in ftl files
    usbPartSym = coreComponent.createBooleanSymbol("USB_PART", None)
    usbPartSym.setDefaultValue(check_for_usb_part(processor))
    usbPartSym.setVisible(False)

    # atdf-specific areas
    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") != "PIC32MX1404"):
        clkValGrp_REFOCON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__ROSEL"]')
        clkValGrp_REFOCON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__RODIV"]')
        clkValGrp_REFOTRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOTRIM__ROTRIM"]')
        clkRegGrp_REFOTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFOTRIM"]')
        clkRegGrp_REFOCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFOCON"]')
        clkValGrp_REFOCON__ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__ON"]')
        clkValGrp_REFOCON__OE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__OE"]')
    else:
        clkRegGrp_REFOTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFO1TRIM"]')
        clkRegGrp_REFOCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFO1CON"]')
        clkRegGrp_UPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="UPLLCON"]')
        clkValGrp_REFOCON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1CON__ROSEL"]')
        clkValGrp_REFOCON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1CON__RODIV"]')
        clkValGrp_REFOTRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1TRIM__ROTRIM"]')
        clkValGrp_UPLLCON__PLLIDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="UPLLCON__PLLIDIV"]')
        clkValGrp_UPLLCON__PLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="UPLLCON__PLLMULT"]')
        clkValGrp_UPLLCON__PLLODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="UPLLCON__PLLODIV"]')
        clkValGrp_REFOCON__ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1CON__ON"]')
        clkValGrp_REFOCON__OE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1CON__OE"]')

    clkRegGrp_OSCCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="OSCCON"]')
    clkRegGrp_OSCTUN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="OSCTUN"]')
    clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__FRCDIV"]')
    clkValGrp_OSCCON__NOSC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__NOSC"]')
    clkValGrp_OSCCON__OSWEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__OSWEN"]')
    clkValGrp_OSCCON__UFRCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__UFRCEN"]')
    clkValGrp_OSCTUN__TUN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCTUN__TUN"]')
    clkValGrp_OSCCON__DRMEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__DRMEN"]')
    clkValGrp_OSCCON__SLP2SPD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__SLP2SPD"]')
    clkValGrp_OSCCON__SLOCK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__SLOCK"]')
    clkValGrp_OSCCON__LOCK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__LOCK"]')

    # parse atdf file to get key parameters
    atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
    atdf_file = open(atdf_file_path, "r")
    atdf_content = ElementTree.fromstring(atdf_file.read())

    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_MIPS32", None)
    SYM_CLK_MENU.setLabel("Clock Menu")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1404"):
        CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mx_xlp:MXClockModel")
        peripheralModuleDisableDict = peripheralModuleDisableDict_1xx_2xx_3xx_4xx.copy()
    elif Database.getSymbolValue("core", "PRODUCT_FAMILY") in ["PIC32MX1168", "PIC32MX1185", "PIC32MX1290"]:
        CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mx1:MXClockModel")
        peripheralModuleDisableDict = peripheralModuleDisableDict_1xx_2xx_3xx_4xx.copy()
    else: # PIC32MX1156 and PIC32MX1143
        CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mx_no_refOsc:MXClockModel")
        peripheralModuleDisableDict = peripheralModuleDisableDict_5xx_6xx_7xx.copy()

    CLK_CFG_SETTINGS = coreComponent.createMenuSymbol("ClkCfgSettings", SYM_CLK_MENU)
    CLK_CFG_SETTINGS.setDependencies(enableMenu, ["ClkSvcMenu"])
    CLK_CFG_SETTINGS.setLabel("Clock Configurator Settings")
    CLK_CFG_SETTINGS.setDescription("Various Clock System Settings")
    CLK_CFG_SETTINGS.setVisible(True)

    # Hiding temperature range selection feature for now
    TEMP_RANGE = coreComponent.createKeyValueSetSymbol("CONFIG_TEMPERATURE_RANGE", CLK_CFG_SETTINGS)
    TEMP_RANGE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    TEMP_RANGE.setLabel("Operating Temperature Range")
    TEMP_RANGE.setDescription("Maximum allowed System Clock Frequency will depend on selected Temperature Range")
    TEMP_RANGE.setVisible(False)
    TEMP_RANGE.setOutputMode("Value")
    TEMP_RANGE.setDisplayMode("Description")

    max_clk_freq_for_selected_temp = coreComponent.createIntegerSymbol("MAX_CLK_FREQ_FOR_SELECTED_TEMP_RANGE", CLK_CFG_SETTINGS)
    max_clk_freq_for_selected_temp.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    max_clk_freq_for_selected_temp.setLabel("Max System Clock Frequency (HZ) For Selected Temperature")
    max_clk_freq_for_selected_temp.setReadOnly(True)
    max_clk_freq_for_selected_temp.setVisible(False)

    if Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1185":
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +105C, DC to 80 MHz")
        TEMP_RANGE.addKey("RANGE2", "1", "-40C to +85C, DC to 100 MHz")
        TEMP_RANGE.addKey("RANGE3", "2", "0C to +70C, DC to 120 MHz")
        TEMP_RANGE.setDefaultValue(2)
        max_clk_freq_for_selected_temp.setDefaultValue(120000000)
    elif Database.getSymbolValue("core", "PRODUCT_FAMILY") in ["PIC32MX1168","PIC32MX1290"]:
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +105C, DC to 40 MHz")
        TEMP_RANGE.addKey("RANGE2", "1", "-40C to +85C, DC to 50 MHz")
        TEMP_RANGE.setDefaultValue(1)
        max_clk_freq_for_selected_temp.setDefaultValue(50000000)
    elif Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1404":
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +105C, DC to 72 MHz")
        TEMP_RANGE.setReadOnly(True)
        TEMP_RANGE.setDefaultValue(0)
        max_clk_freq_for_selected_temp.setDefaultValue(72000000)
    elif (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1156") or \
                ((Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1143") and Variables.get("__PROCESSOR").find("032H") == -1):
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +105C, DC to 80 MHz")
        TEMP_RANGE.setReadOnly(True)
        TEMP_RANGE.setDefaultValue(0)
        max_clk_freq_for_selected_temp.setDefaultValue(80000000)
    else: # it means PIC32MX1143 datasheet 032H parts
        TEMP_RANGE.addKey("RANGE1", "0", "-40C to +105C, DC to 40 MHz")
        TEMP_RANGE.setReadOnly(True)
        TEMP_RANGE.setDefaultValue(0)
        max_clk_freq_for_selected_temp.setDefaultValue(40000000)

    max_clk_freq_for_selected_temp.setDependencies(updateMaxFreq, ["CONFIG_TEMPERATURE_RANGE"])

    USB_CFG_SETTINGS = coreComponent.createMenuSymbol("UsbCfgSettings", CLK_CFG_SETTINGS)
    USB_CFG_SETTINGS.setDependencies(enableMenu, ["ClkSvcMenu"])
    USB_CFG_SETTINGS.setLabel("USB Clock Configuration")
    USB_CFG_SETTINGS.setDescription("USB Clock Configuration")
    if(check_for_usb_part(processor) == True):
        USB_CFG_SETTINGS.setVisible(True)
    else:
        USB_CFG_SETTINGS.setVisible(False)

    # Menu items listed here
    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

    if clkRegGrp_REFOCON is not None:
        enSymId = "CONFIG_SYS_CLK_REFCLK_ENABLE"
        enSymbol = coreComponent.createBooleanSymbol(enSymId, CLK_CFG_SETTINGS)
        enSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        enSymbol.setLabel("Enable Reference Clock")
        enSymbol.setDescription("Sets whether to have reference clock enabled")
        enSymbol.setDefaultValue(False)

    # primary oscillator frequency
    POSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL", CLK_CFG_SETTINGS)
    POSC_IN_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    POSC_IN_FREQ.setLabel("Primary Oscillator Input Frequency (Hz)")
    POSC_IN_FREQ.setDependencies(updatePoscFreq, ["CONFIG_SYS_CLK_CONFIG_PRIMARY_XTAL"])
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__POSC_DEF_FREQ"]')
    POSC_IN_FREQ.setDefaultValue(int(node.getAttribute("value")))

    # secondary oscillator frequency
    SOSC_IN_FREQ = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL", CLK_CFG_SETTINGS)
    SOSC_IN_FREQ.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
    SOSC_IN_FREQ.setLabel("Secondary Oscillator Input Frequency (Hz)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SOSC_DEF_FREQ"]')
    newPoscFreq = node.getAttribute("value")
    SOSC_IN_FREQ.setDefaultValue(int(newPoscFreq))

    # OSCCON
    scan_atdf_for_osccon_fields(coreComponent, CLK_CFG_SETTINGS, USB_CFG_SETTINGS)

    # OSCTUN
    #scan_atdf_for_osctun_fields(coreComponent, CLK_CFG_SETTINGS)

    if clkRegGrp_REFOCON is not None:
        # REFOCON
        scan_atdf_for_refocon_fields(coreComponent, CLK_CFG_SETTINGS, enSymbol)

        # REFOTRIM
        scan_atdf_for_refotrim_fields(coreComponent, enSymbol)

    if(Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1404"):   # following registers only exist in this subset of PIC32MX family
        symbolEnName = coreComponent.createBooleanSymbol("CONFIG_SYS_CLK_PBCLK_ENABLE", CLK_CFG_SETTINGS)
        symbolEnName.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        symbolEnName.setLabel("Enable Peripheral Clock Bus")
        symbolEnName.setDefaultValue(True)

        # UPLLCON
        scan_atdf_for_upllcon_fields(coreComponent, USB_CFG_SETTINGS)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, join, ElementTree, newPoscFreq)

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

    peripheralClockMenu = coreComponent.createMenuSymbol("PERIPHERAL_CLK_CONFIG", SYM_CLK_MENU)
    peripheralClockMenu.setLabel("Peripheral Clock Configuration")
    if pmdCount > 0:
        peripheralClockMenu.setVisible(True)
    else:
        peripheralClockMenu.setVisible(False)

    # calculated peripheral frequencies
    sym_peripheral_clock_enable = []
    sym_peripheral_clock_freq = []

    modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()

    for module in range(len(modules)):
        instances = modules[module].getChildren()
        for instance in range(len(instances)):
            peripheralName = str(instances[instance].getAttribute("name"))
            if peripheralName == "CMP":
                cmpRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]').getChildren()
                index = 1
                for register in cmpRegGroup:
                    regName = str(register.getAttribute("name"))
                    if regName.startswith("CM") and regName.endswith("CON"):
                        if peripheralModuleDisableDict.has_key("CMP" + str(index)):
                            sym_peripheral_clock_enable.append("CMP" + str(index) + "_CLOCK_ENABLE")
                            peripheral_clock_enable = coreComponent.createBooleanSymbol("CMP" + str(index) + "_CLOCK_ENABLE", peripheralClockMenu)
                            peripheral_clock_enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                            peripheral_clock_enable.setLabel("CMP" + str(index) + " Clock Enable")
                            peripheral_clock_enable.setDefaultValue(0)

                            sym_peripheral_clock_freq.append("CMP" + str(index) + "_CLOCK_FREQUENCY")
                            peripheral_clock_freq = coreComponent.createIntegerSymbol("CMP" + str(index) + "_CLOCK_FREQUENCY", peripheral_clock_enable)
                            peripheral_clock_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                            peripheral_clock_freq.setLabel("CMP" + str(index) + " Clock Frequency")
                            peripheral_clock_freq.setReadOnly(True)
                            peripheral_clock_freq.setDefaultValue(0)
                            peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, ["CONFIG_SYS_CLK_PBCLK_FREQ"])

                        index += 1
            else:
                if peripheralModuleDisableDict.has_key(peripheralName):
                    sym_peripheral_clock_enable.append(peripheralName + "_CLOCK_ENABLE")
                    peripheral_clock_enable = coreComponent.createBooleanSymbol(peripheralName + "_CLOCK_ENABLE", peripheralClockMenu)
                    peripheral_clock_enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                    peripheral_clock_enable.setLabel(peripheralName + " Clock Enable")
                    peripheral_clock_enable.setDefaultValue(0)

                    sym_peripheral_clock_freq.append(peripheralName + "_CLOCK_FREQUENCY")
                    peripheral_clock_freq = coreComponent.createIntegerSymbol(peripheralName + "_CLOCK_FREQUENCY", peripheral_clock_enable)
                    peripheral_clock_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
                    peripheral_clock_freq.setLabel(peripheralName + " Clock Frequency")
                    peripheral_clock_freq.setReadOnly(True)
                    peripheral_clock_freq.setDefaultValue(0)

                    if Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1404" and peripheralName.startswith("UART"):
                        peripheral_clock_freq.setDependencies(uartClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".UART_CLKSEL", "CONFIG_SYS_CLK_FRCDIV",
                                                                                         "CONFIG_SYS_CLK_PBCLK_FREQ"])
                    elif Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1404" and peripheralName == "TMR1":
                        peripheral_clock_freq.setDependencies(tmr1ClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "tmr1.TIMER1_SRC_SEL", "tmr1.TIMER1_TECS", "CONFIG_SYS_CLK_PBCLK_FREQ",
                                                                                         "CONFIG_SYS_CLK_CONFIG_SECONDARY_XTAL"])
                    elif peripheralName.startswith("SPI"):
                        peripheral_clock_freq.setDependencies(spiClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", peripheralName.lower() + ".SPI_MASTER_CLOCK", "CONFIG_SYS_CLK_PBCLK_FREQ",
                                                                                        "CONFIG_SYS_CLK_REFCLK_FREQ"])
                    elif (Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1290" or Database.getSymbolValue("core", "PRODUCT_FAMILY") == "PIC32MX1156") and peripheralName.startswith("CAN"):
                        peripheral_clock_freq.setDependencies(canClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "SYS_CLK_FREQ"])
                    elif peripheralName.startswith("ETH"):
                        peripheral_clock_freq.setDependencies(sysPeripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "SYS_CLK_FREQ"])
                    else:
                        peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, [peripheralName + "_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK_FREQ"])

    if clkRegGrp_REFOCON is not None:
        sym_peripheral_clock_enable.append("REFO_CLOCK_ENABLE")
        peripheral_clock_enable = coreComponent.createBooleanSymbol("REFO_CLOCK_ENABLE", peripheralClockMenu)
        peripheral_clock_enable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        peripheral_clock_enable.setLabel("REFO Clock Enable")
        peripheral_clock_enable.setDefaultValue(True)

        sym_peripheral_clock_freq.append("REFO_CLOCK_FREQUENCY")
        peripheral_clock_freq = coreComponent.createIntegerSymbol("REFO_CLOCK_FREQUENCY", peripheral_clock_enable)
        peripheral_clock_freq.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
        peripheral_clock_freq.setLabel("REFO Clock Frequency")
        peripheral_clock_freq.setReadOnly(True)
        peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK_FREQ")))
        peripheral_clock_freq.setDependencies(peripheralClockFreqCalc, ["REFO_CLOCK_ENABLE", "CONFIG_SYS_CLK_PBCLK_FREQ"])

    if pmdCount > 0:
        peripheralModuleDisableMenu = coreComponent.createMenuSymbol("PMD_CONFIG", SYM_CLK_MENU)
        peripheralModuleDisableMenu.setLabel("Peripheral Module Disable")
        peripheralModuleDisableMenu.setDependencies(updatePMDxRegValue, sym_peripheral_clock_enable)

        pmdRegCount = coreComponent.createIntegerSymbol("PMD_COUNT", peripheralModuleDisableMenu)
        pmdRegCount.setDefaultValue(pmdCount)
        pmdRegCount.setVisible(False)

        for i in range(1, pmdCount + 1):
            pmdxRegMaskValue = coreComponent.createHexSymbol("PMD" + str(i) + "_REG_VALUE", peripheralModuleDisableMenu)
            pmdxRegMaskValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_pic32mx;register:%NOREGISTER%")
            pmdxRegMaskValue.setLabel("PMD" + str(i) + " Register Value")
            pmdxRegMaskValue.setDefaultValue(pmdDict[i])
            pmdxRegMaskValue.setReadOnly(True)

        #Enable REFO from PMD
        periPMDRegId = "PMD" + peripheralModuleDisableDict["REFO"][0] + "_REG_VALUE"
        pmdxValue = Database.getSymbolValue("core", periPMDRegId)
        periPMDRegBitShift = 1 << int(peripheralModuleDisableDict["REFO"][1])
        Database.setSymbolValue("core", periPMDRegId, pmdxValue & ~periPMDRegBitShift, 1)

    if clkValGrp_OSCCON__SLOCK is not None or clkValGrp_OSCCON__LOCK is not None:
        pllLockStatusOption = coreComponent.createStringSymbol("PLL_LOCK_STATUS_OPTION", SYM_CLK_MENU)
        pllLockStatusOption.setVisible(False)
        if clkValGrp_OSCCON__SLOCK is not None:
            pllLockStatusOption.setDefaultValue("SLOCK")
        else:
            pllLockStatusOption.setDefaultValue("LOCK")

    # File handling below
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_pic32mx/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_pic32mx/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mx/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_pic32mx/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
