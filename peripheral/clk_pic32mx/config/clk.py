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
global enableMenu
global get_val_from_str
global set_refocon_value
global set_pbdiv_value
global set_refotrim_value

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
        if(ii.getAttribute('name').lower() != "reserved"):
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
       ("150F256" in processor)  or ("170F512" in processor)):
        return False
    else:
        return True

            
def enableMenu(menu, event):
    # simple visible/invisible callback for menu items
    menu.setVisible(event["value"])

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

global pbitem_update    
def pbitem_update(symbol, event):
    '''
    Callback used to set an integer field, PBDIV[PBDIV].  Only certain devices of PIC32MX family have this register.
    '''
    global _find_val
    global pbdiv
    symbol.setValue(_find_val(pbdiv,event['value']),2)    
    
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
    sys_clk_freq.setLabel("System Clock Frequency (HZ)")
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__SYS_DEF_FREQ"]')
    sys_clk_freq.setDefaultValue(node.getAttribute("value"))
    sys_clk_freq.setReadOnly(True)

    # Peripheral Bus clock frequencies
    targetName = "CONFIG_SYS_CLK_PBCLK_FREQ"
    symbolPbFreqList = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
    symbolPbFreqList.setLabel("Peripheral Bus Clock Frequency (Hz)")
    targetName = "__PB_DEF_FREQ"
    params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
    paramsChildren = params.getChildren()
    for param in paramsChildren:  # find parameter we are interested in now
        if(param.getAttribute("name") == targetName):
            symbolPbFreqList.setDefaultValue(param.getAttribute("value"))
    symbolPbFreqList.setReadOnly(True)

    # Reference Clock frequency
    targetName = "CONFIG_SYS_CLK_REFCLK_FREQ"
    symbolRefoscFreqList = clk_comp.createStringSymbol(targetName, sym_calc_freq_menu)
    symbolRefoscFreqList.setLabel("Reference Clock Frequency (Hz)")
    targetName = "CONFIG_SYS_CLK_REFCLK_ENABLE"
    symbolRefoscFreqList.setDependencies(enableMenu, [targetName])
    # get default value from atdf file
    targetName = "__REFCLK_DEF_FREQ"
    params = ATDF.getNode('/avr-tools-device-file/devices/device/parameters')
    paramsChildren = params.getChildren()
    for param in paramsChildren:  # find parameter we are interested in now
        if(param.getAttribute("name") == targetName):
            symbolRefoscFreqList.setDefaultValue(param.getAttribute("value"))
    symbolRefoscFreqList.setReadOnly(True)


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
   

def updateUpllcon(symbol, event):
    # updates the UPLLCON register value based on any of its bitfields being changed by the user
    global UPLLCON_VALSYM
    global symbolPllIdivMask
    global pllidivKeyVals
    global symbolPllMultMask
    global pllmultKeyvals
    global symbolPllodivMask
    global pllodivKeyvals
    global symbolUposcenMask
    global uposcenKeyvals

    startVal = UPLLCON_VALSYM.getValue()
    if(event['id']=='PLLIDIV_VAL'):
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
        startVal |= int(uposcenKeyvals[event['value']]) << 29 
    UPLLCON_VALSYM.setValue(startVal,2)

    
    


                            
global updateOscCon
def updateOscCon(symbol,event):
    '''
    Callback for updating OSCCON register value symbol whenever any of its bitfields are changed.
    '''
    global symbolOscconFrcdivVal
    global symbolOscconFrcdivMask
    global symbolOscconFrcdivLsb
    global frcdiv
    global symbolOscconUfrcenVal
    global symbolOscconUfrcenMask
    global symbolOscconUfrcenLsb
    global ufrcen
    global symbolOscconSoscenVal
    global symbolOscconSoscenMask
    global symbolOscconSoscenLsb
    global soscen
    global symbolOscconNoscVal
    global symbolOscconNoscMask
    global symbolOscconNoscLsb
    global nosc
    global symbolOscconOswenVal
    global symbolOscconOswenMask
    global symbolOscconOswenLsb
    global oswen
    global ds60001404
    if(ds60001404 == False):
        global symbolOscconPllodivMask
        global symbolOscconPllodivLsb 
        global pllodiv
        global symbolOscconPllmultMask
        global symbolOscconPllmultLsb 
        global pllmult

    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_FRCDIV"):
        mask = int(symbolOscconFrcdivMask.getValue(),16)
        lsb = symbolOscconFrcdivLsb.getValue()
        val = int(frcdiv[symObj.getValue()]) << lsb   # frcdiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == 'CONFIG_SYS_CLK_UFRCEN'):
        mask = int(symbolOscconUfrcenMask.getValue(),16)
        lsb = symbolOscconUfrcenLsb.getValue()
        val = int(ufrcen[symObj.getValue()]) << lsb
    elif(event["id"] == 'CONFIG_SYS_CLK_SOSCEN'):
        mask = int(symbolOscconSoscenMask.getValue(),16)
        lsb = symbolOscconSoscenLsb.getValue()
        val = int(soscen[symObj.getValue()]) << lsb
    elif(event["id"] == 'CONFIG_SYS_CLK_NOSC'):
        mask = int(symbolOscconNoscMask.getValue(),16)
        lsb = symbolOscconNoscLsb.getValue()  
        val = int(nosc[symObj.getValue()]) << lsb
    elif(event["id"] == 'CONFIG_SYS_CLK_OSWEN'):
        mask = int(symbolOscconOswenMask.getValue(),16)
        lsb = symbolOscconOswenLsb.getValue()
        val = int(oswen[symObj.getValue()]) << lsb
    elif(event["id"] == 'CONFIG_SYS_CLK_PLLODIV'):
        mask = int(symbolOscconPllodivMask.getValue(),16)
        lsb = symbolOscconPllodivLsb.getValue()
        val = int(pllodiv[symObj.getValue()]) << lsb
    elif(event["id"] == 'CONFIG_SYS_CLK_PLLMULT'):
        mask = int(symbolOscconPllmultMask.getValue(),16)
        lsb = symbolOscconPllmultLsb.getValue()
        val = int(pllmult[symObj.getValue()]) << lsb

    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)
        
global updateOscTun
def updateOscTun(symbol,event):
    '''
    Callback for updating OSCTUN register value symbol whenever any of its bitfields are changed.
    '''
    global symbolOsctunTunMask
    global symbolOsctunTunLsb
    global tun
    
        
    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_OSCTUN"):
        mask = int(symbolOsctunTunMask.getValue(),16)
        lsb = symbolOsctunTunLsb.getValue()
        val = int(tun[symObj.getValue()]) << lsb   # tun[] is key/value pair.  We're given the key from the symObj, but need corresponding value
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
    global rotrim
    
    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_ROTRIM"):
        mask = int(symbolRefotrimTrimMask.getValue(),16)
        lsb = symbolRefotrimTrimLsb.getValue()
        val = int(rotrim[symObj.getValue()]) << lsb   # rotrim[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)
    
global updateSpllcon
def updateSpllcon(symbol,event):    
    '''
    Callback for updating SPLLCON register value symbol whenever any of its bitfields are changed.
    '''
    global symbolSpllconPlliclkMask
    global symbolSpllconPlliclkLsb
    global plliclk
    global symbolSpllconPllidivMask
    global symbolSpllconPllidivLsb
    global pllidiv    
    global symbolSpllconPllmultMask
    global symbolSpllconPllmultLsb
    global pllmult
    global symbolSpllconPllodivMask
    global symbolSpllconPllodivLsb
    global pllodiv
    
    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_PLLICLK"):
        mask = int(symbolSpllconPlliclkMask.getValue(),16)
        lsb = symbolSpllconPlliclkLsb.getValue()
        val = int(plliclk[symObj.getValue()]) << lsb   # plliclk[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_PLLIDIV"):
        mask = int(symbolSpllconPllidivMask.getValue(),16)
        lsb = symbolSpllconPllidivLsb.getValue()
        val = int(pllidiv[symObj.getValue()]) << lsb   # pllidiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_PLLMULT"):
        mask = int(symbolSpllconPllmultMask.getValue(),16)
        lsb = symbolSpllconPllmultLsb.getValue()
        val = int(pllmult[symObj.getValue()]) << lsb   # pllmult[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_PLLODIV"):
        mask = int(symbolSpllconPllodivMask.getValue(),16)
        lsb = symbolSpllconPllodivLsb.getValue()
        val = int(pllodiv[symObj.getValue()]) << lsb   # pllodiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
        
    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)
    
global updateUpllcon
def updateUpllcon(symbol,event):
    '''
    Callback for updating UPLLCON register value symbol whenever any of its bitfields are changed.
    '''
    global symbolUpllconPllidivMask
    global symbolUpllconPllidivLsb
    global upllidiv
    global symbolUpllconPllmultMask
    global symbolUpllconPllmultLsb
    global upllmult
    global symbolUpllconPllodivMask
    global symbolUpllconPllodivLsb
    global upllodiv

    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_UPLLIDIV"):
        mask = int(symbolUpllconPllidivMask.getValue(),16)
        lsb = symbolUpllconPllidivLsb.getValue()
        val = int(upllidiv[symObj.getValue()]) << lsb   # upllidiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_UPLLMULT"):
        mask = int(symbolUpllconPllmultMask.getValue(),16)
        lsb = symbolUpllconPllmultLsb.getValue()
        val = int(upllmult[symObj.getValue()]) << lsb   # upllmult[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_UPLLODIV"):
        mask = int(symbolUpllconPllodivMask.getValue(),16)
        lsb = symbolUpllconPllodivLsb.getValue()
        val = int(upllodiv[symObj.getValue()]) << lsb   # upllodiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
        
    tempval = (symbol.getValue())
    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)
    
    
global updatePbdiv
def updatePbdiv(symbol,event):
    '''
    Callback for updating PBDIV1 register value symbol whenever any of its bitfields are changed.
    '''
    global symbolPbdivPbdivMask
    global symbolPbdivPbdivLsb
    global symbolPbdivValue
    global pbdiv
    global symbolPbdivOnMask
    global symbolPbdivOnLsb
    global ds60001404
    
    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    if(event["id"] == "CONFIG_SYS_CLK_PBDIV"):
        mask = int(symbolPbdivPbdivMask.getValue(),16)
        lsb = symbolPbdivPbdivLsb.getValue()
        if(ds60001404 == True):  # integer type
            val = symObj.getValue() << lsb
        else:                    # key/value type
            val = int(pbdiv[symObj.getValue()]) << lsb   # pbdiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
        tempval = (symbol.getValue())
    else:
        mask = int(symbolPbdivOnMask.getValue(),16)
        lsb = symbolPbdivOnLsb.getValue()
        val = int(symObj.getValue())<<lsb
        tempval = symbolPbdivValue.getValue()
    
    tempval &= ~mask
    tempval |= val
    symbolPbdivValue.setValue(tempval,1)  # hard coded on purpose
    
global updateRefoconOn
def updateRefoconOn(symbol,event):
    '''
    Callback for updating REFOCON[ON] bit from reference clock enable menu item
    '''
    symObj = event["symbol"]
    val = int(symObj.getValue())
    if(val==0):
        symbol.setValue("DISABLE",1)
    else:
        symbol.setValue("ENABLE",1)

    
    
global updateRefocon
def updateRefocon(symbol,event):
    '''
    Callback for updating REFOCON register value symbol whenever any of its bitfields are changed.
    '''
    global symbolRefoconRodivMask
    global symbolRefoconRodivLsb
    global rodiv
    global symbolRefoconOnMask
    global symbolRefoconOnLsb
    global on
    global symbolRefoconOeMask
    global symbolRefoconOeLsb
    global oe
    global symbolRefoconRoselMask
    global symbolRefoconRoselLsb
    global rosel
    global symbolRefoconValue
    
    symObj = event["symbol"]       # this gets the symbol for the causing event for this dependency function call
    tempval = (symbol.getValue())
    if(event["id"] == "CONFIG_SYS_CLK_RODIV"):
        mask = int(symbolRefoconRodivMask.getValue(),16)
        lsb = symbolRefoconRodivLsb.getValue()
        val = int(rodiv[symObj.getValue()]) << lsb   # rodiv[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_ON"):
        mask = int(symbolRefoconOnMask.getValue(),16)
        lsb = symbolRefoconOnLsb.getValue()
        val = int(on[symObj.getValue()]) << lsb   # on[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_OE"):
        mask = int(symbolRefoconOeMask.getValue(),16)
        lsb = symbolRefoconOeLsb.getValue()
        val = int(oe[symObj.getValue()]) << lsb   # oe[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_ROSEL"):
        mask = int(symbolRefoconRoselMask.getValue(),16)
        lsb = symbolRefoconRoselLsb.getValue()
        val = int(rosel[symObj.getValue()]) << lsb   # rosel[] is key/value pair.  We're given the key from the symObj, but need corresponding value
    elif(event["id"] == "CONFIG_SYS_CLK_REFCLK_ENABLE"):
        mask = int(symbolRefoconOnMask.getValue(),16)
        lsb = symbolRefoconOnLsb.getValue()
        val = int(symObj.getValue()) << lsb   

    tempval &= ~mask
    tempval |= val
    symbol.setValue(tempval,1)

    

def scan_atdf_for_osccon_fields(coreComponent, parentMenu, submenu1, pbmenu):
    '''
    This creates all the symbols for OSCCON register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_OSCCON 
    global clkRegGrp_OSCTUN 
    global clkRegGrp_PBDIV 
    global clkRegGrp_REFOCON 
    global clkRegGrp_REFOTRIM 
    global clkRegGrp_SPLLCON 
    global clkRegGrp_UPLLCON 
    global clkValGrp_OSCCON__FRCDIV 
    global clkValGrp_OSCCON__NOSC 
    global clkValGrp_OSCCON__OSWEN
    global clkValGrp_OSCCON__PLLMULT 
    global clkValGrp_OSCCON__PLLODIV 
    global clkValGrp_OSCCON__SOSCEN 
    global clkValGrp_OSCCON__UFRCEN 
    global clkValGrp_OSCCON__DRMEN
    global clkValGrp_OSCCON__SLP2SPD
    global clkValGrp_OSCTUN__TUN 
    global clkValGrp_PBDIV__ON 
    global clkValGrp_PBDIV__PBDIV 
    global clkValGrp_REFOCON__OE 
    global clkValGrp_REFOCON__ON 
    global clkValGrp_REFOCON__RODIV 
    global clkValGrp_REFOCON__ROSEL 
    global clkValGrp_REFOCON__ROTRIM 
    global clkValGrp_REFOTRIM__ROTRIM 
    global clkValGrp_SPLLCON__PLLICLK 
    global clkValGrp_SPLLCON__PLLIDIV 
    global clkValGrp_SPLLCON__PLLMULT 
    global clkValGrp_SPLLCON__PLLODIV 
    global clkValGrp_UPLLCON__PLLIDIV 
    global clkValGrp_UPLLCON__PLLMULT 
    global clkValGrp_UPLLCON__PLLODIV 
    global clkValGrp_OSCCON__PBDIV
    global symbolOscconFrcdivVal
    global symbolOscconFrcdivMask
    global symbolOscconFrcdivLsb
    global frcdiv
    global symbolOscconUfrcenVal
    global symbolOscconUfrcenMask
    global symbolOscconUfrcenLsb
    global ufrcen
    global symbolOscconSoscenVal
    global symbolOscconSoscenMask
    global symbolOscconSoscenLsb
    global soscen
    global symbolOscconNoscVal
    global symbolOscconNoscMask
    global symbolOscconNoscLsb
    global nosc
    global symbolOscconOswenVal
    global symbolOscconOswenMask
    global symbolOscconOswenLsb
    global oswen
    global symbolOscconPllodivMask
    global symbolOscconPllodivLsb
    global pllodiv
    global symbolOscconPllmultMask
    global symbolOscconPllmultLsb
    global pllmult
    global _get_bitfield_names
    global item_update
    global _get_default_value
    global updateOscCon
    global per_divider
    global symbolEnId

    # Scan through bitfields of OSCCON register that can be overridden by DEVCFG or user selections and create symbols for them
    child = clkRegGrp_OSCCON.getChildren()
    for oscconNode in child:
        if(oscconNode.getAttribute("name") == "FRCDIV"):       # OSCCON[FRCDIV] bitfield
            frcdiv = {}
            _get_bitfield_names(clkValGrp_OSCCON__FRCDIV, frcdiv)
            symbolOscconFrcdivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_FRCDIV", parentMenu, frcdiv.keys())
            symbolOscconFrcdivVal.setDescription(clkValGrp_OSCCON__FRCDIV.getAttribute("caption"))
            symbolOscconFrcdivVal.setLabel(clkValGrp_OSCCON__FRCDIV.getAttribute("caption"))
            symbolOscconFrcdivVal.setVisible(True)
            # FRCDIV divider value:  get values/keys from atdf file.  They're stored in per_divider[]
            per_divider = {}
            node = clkValGrp_OSCCON__FRCDIV.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_divider[node[ii].getAttribute("name")] = argval
            symbolOscconFrcdivVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'FRCDIV', clkValGrp_OSCCON__FRCDIV))

            # bit mask and lsb for FRCDIV
            symbolOscconFrcdivMask = coreComponent.createStringSymbol("FRCDIV_MASK", None)
            symbolOscconFrcdivMask.setVisible(False)
            symbolOscconFrcdivMask.setDefaultValue(oscconNode.getAttribute("mask"))
            symbolOscconFrcdivLsb = coreComponent.createIntegerSymbol("FRCDIV_MASKLSB", None)
            symbolOscconFrcdivLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))            
            symbolOscconFrcdivLsb.setDefaultValue(lsb)

        elif(oscconNode.getAttribute("name") == "DRMEN"):       # OSCCON[DRMEN] bitfield
            drmen = {}
            _get_bitfield_names(clkValGrp_OSCCON__DRMEN, drmen)
            symbolOscconDrmenVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_DRMEN", parentMenu, drmen.keys())
            symbolOscconDrmenVal.setDescription(clkValGrp_OSCCON__DRMEN.getAttribute("caption"))
            symbolOscconDrmenVal.setLabel(clkValGrp_OSCCON__DRMEN.getAttribute("caption"))
            symbolOscconDrmenVal.setVisible(False)
            symbolOscconDrmenVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'DRMEN', clkValGrp_OSCCON__DRMEN))
            
        elif(oscconNode.getAttribute("name") == "SLP2SPD"):       # OSCCON[SLP2SPD] bitfield
            slp2spd = {}
            _get_bitfield_names(clkValGrp_OSCCON__SLP2SPD, slp2spd)
            symbolOscconSlp2spdVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_SLP2SPD", parentMenu, slp2spd.keys())
            symbolOscconSlp2spdVal.setDescription(clkValGrp_OSCCON__SLP2SPD.getAttribute("caption"))
            symbolOscconSlp2spdVal.setLabel(clkValGrp_OSCCON__SLP2SPD.getAttribute("caption"))
            symbolOscconSlp2spdVal.setVisible(False)
            symbolOscconSlp2spdVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'SLP2SPD', clkValGrp_OSCCON__SLP2SPD))
            
        elif(oscconNode.getAttribute("name") == "UFRCEN"):       # OSCCON[UFRCEN] bitfield
            ufrcen = {}
            _get_bitfield_names(clkValGrp_OSCCON__UFRCEN, ufrcen)
            symbolOscconUfrcenVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_UFRCEN", submenu1, ufrcen.keys())
            symbolOscconUfrcenVal.setDescription(clkValGrp_OSCCON__UFRCEN.getAttribute("caption"))
            symbolOscconUfrcenVal.setLabel(clkValGrp_OSCCON__UFRCEN.getAttribute("caption"))
            symbolOscconUfrcenVal.setVisible(True)
            symbolOscconUfrcenVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'UFRCEN', clkValGrp_OSCCON__UFRCEN))

            # bit mask and lsb for UFRCEN
            symbolOscconUfrcenMask = coreComponent.createStringSymbol("UFRCEN_MASK", None)
            symbolOscconUfrcenMask.setVisible(False)
            symbolOscconUfrcenMask.setDefaultValue(oscconNode.getAttribute("mask"))
            symbolOscconUfrcenLsb = coreComponent.createIntegerSymbol("UFRCEN_MASKLSB", None)
            symbolOscconUfrcenLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconUfrcenLsb.setDefaultValue(lsb)
            
        elif(oscconNode.getAttribute("name") == "SOSCEN"):       # OSCCON[SOSCEN] bitfield
            soscen = {}
            _get_bitfield_names(clkValGrp_OSCCON__SOSCEN, soscen)
            symbolOscconSoscenVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_SOSCEN", parentMenu, soscen.keys())
            symbolOscconSoscenVal.setVisible(True)
            symbolOscconSoscenVal.setDescription(clkValGrp_OSCCON__SOSCEN.getAttribute("caption"))
            symbolOscconSoscenVal.setLabel(clkValGrp_OSCCON__SOSCEN.getAttribute("caption"))
            symbolOscconSoscenVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'SOSCEN', clkValGrp_OSCCON__SOSCEN))

            # bit mask and lsb for SOSCEN
            symbolOscconSoscenMask = coreComponent.createStringSymbol("SOSCEN_MASK", None)
            symbolOscconSoscenMask.setVisible(False)
            symbolOscconSoscenMask.setDefaultValue(oscconNode.getAttribute("mask"))
            symbolOscconSoscenLsb = coreComponent.createIntegerSymbol("SOSCEN_MASKLSB", None)
            symbolOscconSoscenLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconSoscenLsb.setDefaultValue(lsb)
    
        elif(oscconNode.getAttribute("name") == "NOSC"):       # OSCCON[NOSC] bitfield
            nosc = {}
            _get_bitfield_names(clkValGrp_OSCCON__NOSC, nosc)
            symbolOscconNoscVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_NOSC", parentMenu, nosc.keys())
            symbolOscconNoscVal.setVisible(False)
            # on reset, this field is set to DEVCFG1<2:0>, FNOSC bitfield
            targetsym = "CONFIG_FNOSC"
            fnoscVal = Database.getSymbolValue("core",targetsym)
            for ii in nosc:
                if(ii == fnoscVal):
                    symbolOscconNoscVal.setDefaultValue(str(ii))
            symbolOscconNoscVal.setDependencies(item_update, ["core."+targetsym])  # update NOSC whenever user updates DEVCFG1<2:0>, FNOSC

            # bit mask and lsb for NOSC
            symbolOscconNoscMask = coreComponent.createStringSymbol("NOSC_MASK", None)
            symbolOscconNoscMask.setVisible(False)
            symbolOscconNoscMask.setDefaultValue(oscconNode.getAttribute("mask"))
            symbolOscconNoscLsb = coreComponent.createIntegerSymbol("NOSC_MASKLSB", None)
            symbolOscconNoscLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconNoscLsb.setDefaultValue(lsb)
            
        elif(oscconNode.getAttribute("name") == "OSWEN"):       # OSCCON[OSWEN] bitfield
            oswen = {}
            _get_bitfield_names(clkValGrp_OSCCON__OSWEN, oswen)
            symbolOscconOswenVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_OSWEN", parentMenu, oswen.keys())
            symbolOscconOswenVal.setVisible(False)
            # on reset, this field is set to DEVCFG1<7>, IESO bitfield
            targetsym = "CONFIG_IESO"
            oswenVal = Database.getSymbolValue("core",targetsym)
            for ii in oswen:
                if(ii == oswenVal):
                    symbolOscconOswenVal.setDefaultValue(str(ii))
            symbolOscconOswenVal.setDependencies(item_update, ["core."+targetsym])  # update NOSC whenever user updates DEVCFG1<2:0>, FNOSC

            # bit mask and lsb for OSWEN
            symbolOscconOswenMask = coreComponent.createStringSymbol("OSWEN_MASK", None)
            symbolOscconOswenMask.setVisible(False)
            symbolOscconOswenMask.setDefaultValue(oscconNode.getAttribute("mask"))            
            symbolOscconOswenLsb = coreComponent.createIntegerSymbol("OSWEN_MASKLSB", None)
            symbolOscconOswenLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconOswenLsb.setDefaultValue(lsb)
            
        elif(oscconNode.getAttribute("name") == "PLLODIV"):       # OSCCON[PLLODIV] bitfield, if present in this register
            pllodiv = {}
            _get_bitfield_names(clkValGrp_OSCCON__PLLODIV, pllodiv)
            symbolOscconPllodivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLODIV", parentMenu, pllodiv.keys())
            symbolOscconPllodivVal.setVisible(True)
            symbolOscconPllodivVal.setLabel(clkValGrp_OSCCON__PLLODIV.getAttribute("caption"))

            # on reset, this field is set to DEVCFG2<18:16>, FPLLODIV bitfield
            targetsym = "CONFIG_FPLLODIV"
            pllodivVal = Database.getSymbolValue("core",targetsym)
            for ii in pllodiv:
                if(ii == pllodivVal):
                    symbolOscconPllodivVal.setDefaultValue(str(ii))
            symbolOscconPllodivVal.setDependencies(item_update, ["core."+targetsym])  # update PLLODIV whenever user updates DEVCFG2<18:16>, FPLLODIV

            # bit mask and lsb for PLLODIV
            symbolOscconPllodivMask = coreComponent.createStringSymbol("PLLODIV_MASK", None)
            symbolOscconPllodivMask.setVisible(False)
            symbolOscconPllodivMask.setDefaultValue(oscconNode.getAttribute("mask"))            
            symbolOscconPllodivLsb = coreComponent.createIntegerSymbol("PLLODIV_MASKLSB", None)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconPllodivLsb.setDefaultValue(lsb)            
            symbolOscconPllodivLsb.setVisible(False)
            
        elif(oscconNode.getAttribute("name") == "PLLMULT"):       # OSCCON[PLLMULT] bitfield, if present in this register
            pllmult = {}
            _get_bitfield_names(clkValGrp_OSCCON__PLLMULT, pllmult)
            symbolOscconPllmultVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLMULT", parentMenu, pllmult.keys())
            symbolOscconPllmultVal.setVisible(True)
            symbolOscconPllmultVal.setLabel(clkValGrp_OSCCON__PLLMULT.getAttribute("caption"))
            # on reset, this field is set to DEVCFG2<6:4>, FPLLMUL bitfield
            targetsym = "CONFIG_FPLLMUL"
            pllmulVal = Database.getSymbolValue("core",targetsym)
            for ii in pllmult:
                if(ii == pllmulVal):
                    symbolOscconPllmultVal.setDefaultValue(str(ii))
            symbolOscconPllmultVal.setDependencies(item_update, ["core."+targetsym])  # update PLLODIV whenever user updates DEVCFG2<6:4>, FPLLMUL

            # bit mask and lsb for PLLMULT
            symbolOscconPllmultMask = coreComponent.createStringSymbol("PLLMULT_MASK", None)
            symbolOscconPllmultMask.setVisible(False)
            symbolOscconPllmultMask.setDefaultValue(oscconNode.getAttribute("mask"))            
            symbolOscconPllmultLsb = coreComponent.createIntegerSymbol("PLLMULT_MASKLSB", None)
            symbolOscconPllmultLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconPllmultLsb.setDefaultValue(lsb)
            
        elif(oscconNode.getAttribute("name") == "PBDIV"):       # OSCCON[PBDIV] bitfield, if present in this register
            pbdiv = {}
            _get_bitfield_names(clkValGrp_OSCCON__PBDIV, pbdiv)
            symbolOscconPbdivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PBDIV", pbmenu, pbdiv.keys())
            symbolOscconPbdivVal.setVisible(True)
            symbolOscconPbdivVal.setDefaultValue(_get_default_value(clkRegGrp_OSCCON, 'PBDIV', clkValGrp_OSCCON__PBDIV))
            symbolOscconPbdivVal.setLabel(clkValGrp_OSCCON__PBDIV.getAttribute("caption"))

            # on reset, this field is set to DEVCFG1<13:12>, FPBDIV bitfield
            targetsym = "CONFIG_FPBDIV"
            pbdivVal = Database.getSymbolValue("core",targetsym)
            for ii in pbdiv:
                if(ii == pbdivVal):
                    symbolOscconPbdivVal.setDefaultValue(str(ii))
            symbolOscconPbdivVal.setDependencies(item_update, ["core."+targetsym])  # update PBDIV whenever user updates DEVCFG1<13:12>, FPBDIV           

            # bit mask and lsb for PBDIV
            symbolOscconPbdivMask = coreComponent.createStringSymbol("PBDIV_MASK", None)
            symbolOscconPbdivMask.setVisible(False)
            symbolOscconPbdivMask.setDefaultValue(oscconNode.getAttribute("mask"))            
            symbolOscconPbdivLsb = coreComponent.createIntegerSymbol("PBDIV_MASKLSB", None)
            symbolOscconPbdivLsb.setVisible(False)
            lsb = find_lsb_position(oscconNode.getAttribute("mask"))
            symbolOscconPbdivLsb.setDefaultValue(lsb)
            
    # get initial value of OSCCON register from 'initval' field in atdf file
    symbolOscconValue = coreComponent.createHexSymbol("OSCCON_VALUE", None)
    symbolOscconValue.setVisible(False)
    initialOscconVal = int((clkRegGrp_OSCCON.getAttribute('initval')),16)

    # make updates to initialOscconVal due to above bitfield values being changed by DEVCFGx registers
    initialOscconVal &= ~int(symbolOscconNoscMask.getValue(),16)
    initialOscconVal |= int(nosc[symbolOscconNoscVal.getValue()]) << symbolOscconNoscLsb.getValue()
    initialOscconVal &= ~int(symbolOscconOswenMask.getValue(),16)
    initialOscconVal |= int(oswen[symbolOscconOswenVal.getValue()]) << symbolOscconOswenLsb.getValue()    
    if(oscconNode.getAttribute("name") == "PLLODIV"):
        initialOscconVal &= ~int(symbolOscconPllodivMask.getValue(),16)
        initialOscconVal |= int(pllodiv[symbolOscconPllodivVal.getValue()]) << symbolOscconPllodivLsb.getValue()
    elif(oscconNode.getAttribute("name") == "PLLMULT"): 
        initialOscconVal &= ~int(symbolOscconPllmultMask.getValue(),16)
        initialOscconVal |= int(pllmult[symbolOscconPllmultVal.getValue()]) << symbolOscconPllmultLsb.getValue()
    symbolOscconValue.setDefaultValue(initialOscconVal)
    symbolOscconValue.setDependencies(updateOscCon,['CONFIG_SYS_CLK_FRCDIV','CONFIG_SYS_CLK_UFRCEN','CONFIG_SYS_CLK_SOSCEN','CONFIG_SYS_CLK_NOSC','CONFIG_SYS_CLK_OSWEN'])
    if(ds60001404 == False):  # some bitfields are not present in OSCCON for some devices of PIC32MX family    
        symbolOscconValue.setDependencies(updateOscCon,['CONFIG_SYS_CLK_PLLODIV','CONFIG_SYS_CLK_PLLMULT'])
        

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
    global clkValGrp_REFOCON__ROTRIM 
    global clkValGrp_REFOTRIM__ROTRIM 
    global symbolRefoconOnVal
    global per_on
    global symbolRefoconValue
    global symbolRefoconRodivMask
    global symbolRefoconRodivLsb
    global rodiv
    global symbolRefoconOnMask
    global symbolRefoconOnLsb
    global on
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
    child = clkRegGrp_REFOCON.getChildren()
    for oscrefoconNode in child:
        if(oscrefoconNode.getAttribute("name") == "RODIV"):       # REFOCON[RODIV] bitfield
            rodiv = {}
            _get_bitfield_names(clkValGrp_REFOCON__RODIV, rodiv)
            symbolRefoconRodivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_RODIV", submenu1, rodiv.keys())
            symbolRefoconRodivVal.setVisible(False)
            symbolRefoconRodivVal.setDescription(clkValGrp_REFOCON__RODIV.getAttribute("caption"))
            symbolRefoconRodivVal.setLabel(clkValGrp_REFOCON__RODIV.getAttribute("caption")) 
            symbolRefoconRodivVal.setDependencies(enableMenu,[enSymId])
            # TUN value:  get values/keys from atdf file.  They're stored in per_rodiv[]
            per_rodiv = {}
            node = clkValGrp_REFOCON__RODIV.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_rodiv[node[ii].getAttribute("name")] = argval
            symbolRefoconRodivVal.setDefaultValue(_get_default_value(clkRegGrp_REFOCON, 'RODIV', clkValGrp_REFOCON__RODIV))

            # bit mask and lsb for RODIV
            symbolRefoconRodivMask = coreComponent.createStringSymbol("RODIV_MASK", None)
            symbolRefoconRodivMask.setVisible(False)
            symbolRefoconRodivMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
            symbolRefoconRodivLsb = coreComponent.createIntegerSymbol("RODIV_MASKLSB", None)
            symbolRefoconRodivLsb.setVisible(False)
            lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
            symbolRefoconRodivLsb.setDefaultValue(lsb)
            
        elif(oscrefoconNode.getAttribute("name") == "ON"):       # REFOCON[ON] bitfield
            on = {}
            _get_bitfield_names(clkValGrp_REFOCON__ON, on)
            symbolRefoconOnVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_ON", parentMenu, on.keys())
            symbolRefoconOnVal.setVisible(False)
            # ON value:  value is set by user selection of "Enable Reference Clock REFCLK" menu item
            per_on = {}
            node = clkValGrp_REFOCON__ON.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_on[node[ii].getAttribute("name")] = argval
            symbolRefoconOnVal.setDefaultValue(_get_default_value(clkRegGrp_REFOCON, 'ON', clkValGrp_REFOCON__ON))
            symbolRefoconOnVal.setDependencies(updateRefoconOn,['CONFIG_SYS_CLK_REFCLK_ENABLE'])
            
            # bit mask and lsb for ON
            symbolRefoconOnMask = coreComponent.createStringSymbol("ON_MASK", None)
            symbolRefoconOnMask.setVisible(False)
            symbolRefoconOnMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
            symbolRefoconOnLsb = coreComponent.createIntegerSymbol("ON_MASKLSB", None)
            symbolRefoconOnLsb.setVisible(False)
            lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
            symbolRefoconOnLsb.setDefaultValue(lsb)      
            
        elif(oscrefoconNode.getAttribute("name") == "OE"):       # REFOCON[OE] bitfield
            oe = {}
            _get_bitfield_names(clkValGrp_REFOCON__OE, oe)
            symbolRefoconOeVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_OE", submenu1, oe.keys())
            symbolRefoconOeVal.setVisible(True)
            symbolRefoconOeVal.setDescription(clkValGrp_REFOCON__OE.getAttribute("caption"))
            symbolRefoconOeVal.setLabel(clkValGrp_REFOCON__OE.getAttribute("caption"))
            symbolRefoconOeVal.setDependencies(enableMenu,[enSymId])
            # OE value:  get values/keys from atdf file.  They're stored in oe[]
            per_oe = {}
            node = clkValGrp_REFOCON__OE.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_oe[node[ii].getAttribute("name")] = argval
            symbolRefoconOeVal.setDefaultValue(_get_default_value(clkRegGrp_REFOCON, 'OE', clkValGrp_REFOCON__OE))

            # bit mask and lsb for OE
            symbolRefoconOeMask = coreComponent.createStringSymbol("OE_MASK", None)
            symbolRefoconOeMask.setVisible(False)
            symbolRefoconOeMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
            symbolRefoconOeLsb = coreComponent.createIntegerSymbol("OE_MASKLSB", None)
            symbolRefoconOeLsb.setVisible(False)
            lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
            symbolRefoconOeLsb.setDefaultValue(lsb)         
            
        elif(oscrefoconNode.getAttribute("name") == "ROSEL"):       # REFOCON[ROSEL] bitfield
            rosel = {}
            _get_bitfield_names(clkValGrp_REFOCON__ROSEL, rosel)
            symbolRefoconRoselVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_ROSEL", submenu1, rosel.keys())
            symbolRefoconRoselVal.setVisible(False)
            symbolRefoconRoselVal.setDescription(clkValGrp_REFOCON__ROSEL.getAttribute("caption"))
            symbolRefoconRoselVal.setLabel(clkValGrp_REFOCON__ROSEL.getAttribute("caption"))
            symbolRefoconRoselVal.setDependencies(enableMenu,[enSymId])
            # ROSEL value:  get values/keys from atdf file.  They're stored in rosel[]
            per_rosel = {}
            node = clkValGrp_REFOCON__ROSEL.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_rosel[node[ii].getAttribute("name")] = argval
            symbolRefoconRoselVal.setDefaultValue(_get_default_value(clkRegGrp_REFOCON, 'ROSEL', clkValGrp_REFOCON__ROSEL))
            # bit mask and lsb for OE
            symbolRefoconRoselMask = coreComponent.createStringSymbol("ROSEL_MASK", None)
            symbolRefoconRoselMask.setVisible(False)
            symbolRefoconRoselMask.setDefaultValue(oscrefoconNode.getAttribute("mask"))
            symbolRefoconRoselLsb = coreComponent.createIntegerSymbol("ROSEL_MASKLSB", None)
            symbolRefoconRoselLsb.setVisible(False)
            lsb = find_lsb_position(oscrefoconNode.getAttribute("mask"))
            symbolRefoconRoselLsb.setDefaultValue(lsb) 
            
    # get initial value of REFOCON register from 'initval' field in atdf file
    symbolRefoconValue = coreComponent.createHexSymbol("REFOCON_VALUE", None)
    symbolRefoconValue.setVisible(False)
    initialRefoconVal = int((clkRegGrp_REFOCON.getAttribute('initval')),16)
    symbolRefoconValue.setDefaultValue(initialRefoconVal)
    symbolRefoconValue.setDependencies(updateRefocon,['CONFIG_SYS_CLK_RODIV','CONFIG_SYS_CLK_ON','CONFIG_SYS_CLK_OE','CONFIG_SYS_CLK_ROSEL','CONFIG_SYS_CLK_REFCLK_ENABLE'])


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
    global tun
    # Scan through bitfields of OSCTUN
    child = clkRegGrp_OSCTUN.getChildren()
    for osctunNode in child:
        if(osctunNode.getAttribute("name") == "TUN"):       # OSCTUN[TUN] bitfield
            tun = {}
            _get_bitfield_names(clkValGrp_OSCTUN__TUN, tun)
            symbolOsctunTunVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_OSCTUN", parentMenu, tun.keys())
            symbolOsctunTunVal.setDescription(clkValGrp_OSCTUN__TUN.getAttribute("caption"))
            symbolOsctunTunVal.setLabel(clkValGrp_OSCTUN__TUN.getAttribute("caption"))
            symbolOsctunTunVal.setVisible(True)
            # TUN value:  get values/keys from atdf file.  They're stored in per_tun[]
            per_tun = {}
            node = clkValGrp_OSCTUN__TUN.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_tun[node[ii].getAttribute("name")] = argval
            symbolOsctunTunVal.setDefaultValue(_get_default_value(clkRegGrp_OSCTUN, 'TUN', clkValGrp_OSCTUN__TUN))

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
    global clkValGrp_REFOCON__ROTRIM
    global symbolRefotrimTrimMask
    global symbolRefotrimTrimLsb
    global rotrim
    # Scan through bitfields of REFOTRIM
    child = clkRegGrp_REFOTRIM.getChildren()
    for oscrefotrimNode in child:
        if(oscrefotrimNode.getAttribute("name") == "ROTRIM"):       # REFOTRIM[ROTRIM] bitfield
            rotrim = {}
            _get_bitfield_names(clkValGrp_REFOCON__ROTRIM, rotrim)
            symbolRefotrimRotrimVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_ROTRIM", parentMenu, rotrim.keys())
            symbolRefotrimRotrimVal.setVisible(True)
            symbolRefotrimRotrimVal.setDescription(clkValGrp_REFOCON__ROTRIM.getAttribute("caption"))
            symbolRefotrimRotrimVal.setLabel(clkValGrp_REFOCON__ROTRIM.getAttribute("caption")) 
            # ROTRIM value:  get values/keys from atdf file.  They're stored in per_rotrim[]
            per_rotrim = {}
            node = clkValGrp_REFOCON__ROTRIM.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_rotrim[node[ii].getAttribute("name")] = argval
            symbolRefotrimRotrimVal.setDefaultValue(_get_default_value(clkRegGrp_REFOTRIM, 'ROTRIM', clkValGrp_REFOCON__ROTRIM))
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
        
        
def scan_atdf_for_spllcon_fields(coreComponent, parentMenu):
    '''
    This creates all the symbols for SPLLCON register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_SPLLCON
    global clkValGrp_SPLLCON__PLLICLK
    global symbolSpllconPlliclkMask
    global symbolSpllconPlliclkLsb
    global symbolSpllconPllidivMask
    global symbolSpllconPllidivLsb
    global symbolSpllconPllmultMask
    global symbolSpllconPllmultLsb
    global symbolSpllconPllodivMask
    global symbolSpllconPllodivLsb
    global plliclk
    global pllidiv
    global pllmult
    global pllodiv
    global item_update
    global updateSpllcon
    
    # Scan through bitfields of SPLLCON
    child = clkRegGrp_SPLLCON.getChildren()
    for spllconNode in child:
        if(spllconNode.getAttribute("name") == "PLLICLK"):       # SPLLCON[PLLICLK] bitfield
            plliclk = {}
            _get_bitfield_names(clkValGrp_SPLLCON__PLLICLK, plliclk)
            symbolSpllconPlliclkVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLICLK", parentMenu, plliclk.keys())
            symbolSpllconPlliclkVal.setVisible(False)
            symbolSpllconPlliclkVal.setDescription(clkValGrp_SPLLCON__PLLICLK.getAttribute("caption"))
            symbolSpllconPlliclkVal.setLabel(clkValGrp_SPLLCON__PLLICLK.getAttribute("caption")) 
            # on reset, this field is set to DEVCFG2<7>, FPLLICLK bitfield
            targetsym = "CONFIG_FPLLICLK"
            fplliclkVal = Database.getSymbolValue("core",targetsym)
            for ii in plliclk:
                if(ii == fplliclkVal):
                    symbolSpllconPlliclkVal.setDefaultValue(str(ii))
            symbolSpllconPlliclkVal.setDependencies(item_update, ["core."+targetsym])  # update PLLICLK whenever user updatesDEVCFG2<7>, FPLLICLK
            # PLLICLK value:  get values/keys from atdf file.  They're stored in per_plliclk[]
            per_plliclk = {}
            node = clkValGrp_SPLLCON__PLLICLK.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_plliclk[node[ii].getAttribute("name")] = argval

            # bit mask and lsb for PLLICLK
            symbolSpllconPlliclkMask = coreComponent.createStringSymbol("PLLICLK_MASK", None)
            symbolSpllconPlliclkMask.setVisible(False)
            symbolSpllconPlliclkMask.setDefaultValue(spllconNode.getAttribute("mask"))
            symbolSpllconPlliclkLsb = coreComponent.createIntegerSymbol("PLLICLK_MASKLSB", None)
            symbolSpllconPlliclkLsb.setVisible(False)
            lsb = find_lsb_position(spllconNode.getAttribute("mask"))
            symbolSpllconPlliclkLsb.setDefaultValue(lsb)

        elif(spllconNode.getAttribute("name") == "PLLIDIV"):       # SPLLCON[PLLIDIV] bitfield
            pllidiv = {}
            _get_bitfield_names(clkValGrp_SPLLCON__PLLIDIV, pllidiv)
            symbolSpllconPllidivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLIDIV", parentMenu, pllidiv.keys())
            symbolSpllconPllidivVal.setVisible(False)
            symbolSpllconPllidivVal.setDescription(clkValGrp_SPLLCON__PLLIDIV.getAttribute("caption"))
            symbolSpllconPllidivVal.setLabel(clkValGrp_SPLLCON__PLLIDIV.getAttribute("caption")) 
            # on reset, this field is set to DEVCFG2<7>, FPLLIDIVK bitfield
            targetsym = "CONFIG_FPLLIDIV"
            fpllidivVal = Database.getSymbolValue("core",targetsym)
            for ii in pllidiv:
                if(ii == fpllidivVal):
                    symbolSpllconPllidivVal.setDefaultValue(str(ii))
            symbolSpllconPllidivVal.setDependencies(item_update, ["core."+targetsym])  # update PLLICLK whenever user updatesDEVCFG2<7>, FPLLIDIV
            
            # PLLIDIV value:  get values/keys from atdf file.  They're stored in per_pllidiv[]
            per_pllidiv = {}
            node = clkValGrp_SPLLCON__PLLIDIV.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_pllidiv[node[ii].getAttribute("name")] = argval

            # bit mask and lsb for PLLIDIV
            symbolSpllconPllidivMask = coreComponent.createStringSymbol("PLLIDIV_MASK", None)
            symbolSpllconPllidivMask.setVisible(False)
            symbolSpllconPllidivMask.setDefaultValue(spllconNode.getAttribute("mask"))
            symbolSpllconPllidivLsb = coreComponent.createIntegerSymbol("PLLIDIV_MASKLSB", None)
            symbolSpllconPllidivLsb.setVisible(False)
            lsb = find_lsb_position(spllconNode.getAttribute("mask"))
            symbolSpllconPllidivLsb.setDefaultValue(lsb)
            
        elif(spllconNode.getAttribute("name") == "PLLMULT"):       # SPLLCON[PLLMULT] bitfield
            pllmult = {}
            _get_bitfield_names(clkValGrp_SPLLCON__PLLMULT, pllmult)
            symbolSpllconPllmultVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLMULT", parentMenu, pllmult.keys())
            symbolSpllconPllmultVal.setVisible(False)
            symbolSpllconPllmultVal.setDescription(clkValGrp_SPLLCON__PLLMULT.getAttribute("caption"))
            symbolSpllconPllmultVal.setLabel(clkValGrp_SPLLCON__PLLMULT.getAttribute("caption")) 
            # on reset, this field is set to DEVCFG2<6:0>, FPLLMUL bitfield
            targetsym = "CONFIG_FPLLMUL"
            fpllmulVal = Database.getSymbolValue("core",targetsym)
            for ii in pllmult:
                if(ii == fpllmulVal):
                    symbolSpllconPllmultVal.setDefaultValue(str(ii))
            symbolSpllconPllmultVal.setDependencies(item_update, ["core."+targetsym])  # update PLLODIV whenever user updates DEVCFG2<6:0>, FPLLMUL

            # bit mask and lsb for PLLMULT
            symbolSpllconPllmultMask = coreComponent.createStringSymbol("PLLIMULT_MASK", None)
            symbolSpllconPllmultMask.setVisible(False)
            symbolSpllconPllmultMask.setDefaultValue(spllconNode.getAttribute("mask"))
            symbolSpllconPllmultLsb = coreComponent.createIntegerSymbol("PLLIMULT_MASKLSB", None)
            symbolSpllconPllmultLsb.setVisible(False)
            lsb = find_lsb_position(spllconNode.getAttribute("mask"))
            symbolSpllconPllmultLsb.setDefaultValue(lsb)

        elif(spllconNode.getAttribute("name") == "PLLODIV"):       # SPLLCON[PLLODIV] bitfield
            pllodiv = {}
            _get_bitfield_names(clkValGrp_SPLLCON__PLLODIV, pllodiv)
            symbolSpllconPllodivVal = coreComponent.createComboSymbol("CONFIG_SYS_CLK_PLLODIV", parentMenu, pllodiv.keys())
            symbolSpllconPllodivVal.setVisible(False)
            symbolSpllconPllodivVal.setDescription(clkValGrp_SPLLCON__PLLODIV.getAttribute("caption"))
            symbolSpllconPllodivVal.setLabel(clkValGrp_SPLLCON__PLLODIV.getAttribute("caption")) 
            # on reset, this field is set to DEVCFG2<18:16>, FPLLODIV bitfield
            targetsym = "CONFIG_FPLLODIV"
            fpllodivVal = Database.getSymbolValue("core",targetsym)
            for ii in pllodiv:
                if(ii == fpllodivVal):
                    symbolSpllconPllodivVal.setDefaultValue(str(ii))
            symbolSpllconPllodivVal.setDependencies(item_update, ["core."+targetsym])  # update PLLODIV whenever user updates DEVCFG2<18:16>, FPLLODIV

            # bit mask and lsb for PLLODIV
            symbolSpllconPllodivMask = coreComponent.createStringSymbol("PLLODIV_MASK", None)
            symbolSpllconPllodivMask.setVisible(False)
            symbolSpllconPllodivMask.setDefaultValue(spllconNode.getAttribute("mask"))
            symbolSpllconPllodivLsb = coreComponent.createIntegerSymbol("PLLODIV_MASKLSB", None)
            symbolSpllconPllodivLsb.setVisible(False)
            lsb = find_lsb_position(spllconNode.getAttribute("mask"))
            symbolSpllconPllodivLsb.setDefaultValue(lsb)
            
    # get initial value of SPLLCON register from 'initval' field in atdf file
    symbolSpllconValue = coreComponent.createHexSymbol("SPLLCON_VALUE", None)
    symbolSpllconValue.setVisible(False)
    initialSpllconVal = int((clkRegGrp_SPLLCON.getAttribute('initval')),16)
    # make updates to initialRefoconVal due to above bitfield values being changed by DEVCFGx register values
    initialSpllconVal &= ~int(symbolSpllconPlliclkMask.getValue(),16)
    initialSpllconVal |= int(plliclk[symbolSpllconPlliclkVal.getValue()]) << symbolSpllconPlliclkLsb.getValue()
    initialSpllconVal &= ~int(symbolSpllconPllmultMask.getValue(),16)
    initialSpllconVal |= int(pllmult[symbolSpllconPllmultVal.getValue()]) << symbolSpllconPllmultLsb.getValue()
    initialSpllconVal &= ~int(symbolSpllconPllidivMask.getValue(),16)
    initialSpllconVal |= int(pllidiv[symbolSpllconPllidivVal.getValue()]) << symbolSpllconPllidivLsb.getValue()      
    initialSpllconVal &= ~int(symbolSpllconPllodivMask.getValue(),16)
    initialSpllconVal |= int(pllidiv[symbolSpllconPllodivVal.getValue()]) << symbolSpllconPllodivLsb.getValue()            
    symbolSpllconValue.setDefaultValue(initialSpllconVal)
    symbolSpllconValue.setDependencies(updateSpllcon,['CONFIG_SYS_CLK_PLLICLK','CONFIG_SYS_CLK_PLLIDIV','CONFIG_SYS_CLK_PLLMULT','CONFIG_SYS_CLK_PLLODIV'])
    
        
        
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
            symbolUpllconPllidivVal.setVisible(True)
            symbolUpllconPllidivVal.setDescription(clkValGrp_UPLLCON__PLLIDIV.getAttribute("caption"))
            symbolUpllconPllidivVal.setLabel(clkValGrp_UPLLCON__PLLIDIV.getAttribute("caption")) 
            # PLLIDIV value:  get values/keys from atdf file.  They're stored in per_pllidiv[]
            per_pllidiv = {}
            node = clkValGrp_UPLLCON__PLLIDIV.getChildren()     # look at all bitfield values of this bitfield
            for ii in range(0,len(node)):
                argterm = node[ii].getAttribute("value")
                if(argterm.find('0x') != -1):
                    argval = argterm[2:]
                else:
                    argval = argterm
                per_pllidiv[node[ii].getAttribute("name")] = argval
            symbolUpllconPllidivVal.setDefaultValue(_get_default_value(clkRegGrp_UPLLCON, 'PLLIDIV', clkValGrp_UPLLCON__PLLIDIV))

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
    symbolUpllconValue.setDefaultValue(initialUpllconVal)
    symbolUpllconValue.setDependencies(updateUpllcon,['CONFIG_SYS_CLK_UPLLIDIV','CONFIG_SYS_CLK_UPLLMULT','CONFIG_SYS_CLK_UPLLODIV'])
        
        
def scan_atdf_for_pbdiv_fields(coreComponent, parentMenu, on_off):
    '''
    This creates all the symbols for PBDIV1 register, obtaining all key/value pairs from atdf file
    and default values for them
    '''
    global clkRegGrp_PBDIV
    global clkValGrp_PBDIV__PBDIV
    global updatePbdiv
    global pbitem_update
    global symbolPbdivPbdivMask
    global symbolPbdivPbdivLsb
    global symbolPbdivValue
    global symbolPbdivOnMask
    global symbolPbdivOnLsb
    global pbdiv
    global ds60001404  # PBDIV is represented differently for this subset of PIC32MX family

    # Scan through bitfields of PB1DIV
    child = clkRegGrp_PBDIV.getChildren()

    for pbdivNode in child:
        if(pbdivNode.getAttribute("name") == "PBDIV"):       # PBDIV bitfield
            pbdiv = {}
            _get_bitfield_names(clkValGrp_PBDIV__PBDIV, pbdiv)
            symbolPbdivPbdivVal = coreComponent.createIntegerSymbol("CONFIG_SYS_CLK_PBDIV", parentMenu)
            symbolPbdivPbdivVal.setVisible(True)
            symbolPbdivPbdivVal.setMin(0)
            symbolPbdivPbdivVal.setMax(127)
            symbolPbdivPbdivVal.setDescription(clkValGrp_PBDIV__PBDIV.getAttribute("caption"))
            symbolPbdivPbdivVal.setLabel(clkValGrp_PBDIV__PBDIV.getAttribute("caption")) 
                
            # on reset, this field is set to DEVCFG1<13:12>, FPBDIV bitfield
            targetsym = "CONFIG_FPBDIV"
            fpbdivVal = Database.getSymbolValue("core",targetsym)
            for ii in pbdiv:
                if(ii == fpbdivVal):
                    symbolPbdivPbdivVal.setDefaultValue(_find_val(pbdiv,ii))  # integer type
            symbolPbdivPbdivVal.setDependencies(pbitem_update, ["core."+targetsym])  # update PBDIV whenever user updates DEVCFG1<13:12>, FPBDIV

            # bit mask and lsb for PBDIV
            symbolPbdivPbdivMask = coreComponent.createStringSymbol("PBDIV_MASK", None)
            symbolPbdivPbdivMask.setVisible(False)
            symbolPbdivPbdivMask.setDefaultValue(pbdivNode.getAttribute("mask"))
            symbolPbdivPbdivLsb = coreComponent.createIntegerSymbol("PBDIV_MASKLSB", None)
            symbolPbdivPbdivLsb.setVisible(False)
            lsb = find_lsb_position(pbdivNode.getAttribute("mask"))
            symbolPbdivPbdivLsb.setDefaultValue(lsb) 
        elif(pbdivNode.getAttribute("name") == "ON"):       #  ON bitfield
            on = {}
            _get_bitfield_names(clkValGrp_PBDIV__PBDIV, on)  # PBDIV in different register in this case

            # bit mask and lsb for ON
            symbolPbdivOnMask = coreComponent.createStringSymbol("PBDIVON_MASK", None)
            symbolPbdivOnMask.setVisible(False)
            symbolPbdivOnMask.setDefaultValue(pbdivNode.getAttribute("mask"))
            symbolPbdivOnLsb = coreComponent.createIntegerSymbol("PBDIVON_MASKLSB", None)
            symbolPbdivOnLsb.setVisible(False)
            lsb = find_lsb_position(pbdivNode.getAttribute("mask"))
            symbolPbdivOnLsb.setDefaultValue(lsb)
        
    # get initial value of PB1DIV register from 'initval' field in atdf file
    symbolPbdivValue = coreComponent.createHexSymbol("PBDIV_VALUE", None)
    symbolPbdivValue.setVisible(False)
    initialPbdivVal = int((clkRegGrp_PBDIV.getAttribute('initval')),16)

    # override fields that are set by DEVCFGx register fields
    initialPbdivVal &= ~int(symbolPbdivPbdivMask.getValue(),16)
    initialPbdivVal |= symbolPbdivPbdivVal.getValue() << symbolPbdivPbdivLsb.getValue()

    if(on_off == False):
        initialPbdivVal &= ~int(symbolPbdivOnMask.getValue(),16)
    else:
        initialPbdivVal |= int(symbolPbdivOnMask.getValue(),16);
    symbolPbdivValue.setDefaultValue(initialPbdivVal)
    symbolPbdivValue.setDependencies(updatePbdiv,['CONFIG_SYS_CLK_PBDIV'])
 
    
    
        
        
if __name__ == "__main__":
    global atdf_content
    global ds60001404  # subset of PIC32MX family have extra registers / bitfields others don't have.    
    global clkRegGrp_OSCCON 
    global clkRegGrp_OSCTUN 
    global clkRegGrp_PBDIV 
    global clkRegGrp_REFOCON 
    global clkRegGrp_REFOTRIM 
    global clkRegGrp_SPLLCON 
    global clkRegGrp_UPLLCON 
    global clkValGrp_OSCCON__FRCDIV 
    global clkValGrp_OSCCON__NOSC 
    global clkValGrp_OSCCON__OSWEN 
    global clkValGrp_OSCCON__PLLMULT 
    global clkValGrp_OSCCON__PLLODIV
    global clkValGrp_OSCCON__PBDIV
    global clkValGrp_OSCCON__SOSCEN 
    global clkValGrp_OSCCON__UFRCEN 
    global clkValGrp_OSCTUN__TUN 
    global clkValGrp_OSCCON__DRMEN
    global clkValGrp_OSCCON__SLP2SPD
    global clkValGrp_PBDIV__ON 
    global clkValGrp_PBDIV__PBDIV 
    global clkValGrp_REFOCON__OE 
    global clkValGrp_REFOCON__ON 
    global clkValGrp_REFOCON__RODIV 
    global clkValGrp_REFOCON__ROSEL 
    global clkValGrp_REFOCON__ROTRIM 
    global clkValGrp_REFOTRIM__ROTRIM 
    global clkValGrp_SPLLCON__PLLICLK 
    global clkValGrp_SPLLCON__PLLIDIV 
    global clkValGrp_SPLLCON__PLLMULT 
    global clkValGrp_SPLLCON__PLLODIV 
    global clkValGrp_UPLLCON__PLLIDIV 
    global clkValGrp_UPLLCON__PLLMULT 
    global clkValGrp_UPLLCON__PLLODIV 
    global pbclkEnName
    global refconval
    global symbolRoselValueList
    global refotrimval
    global rotrimSymbolList
    global uposcenKeyvals
    symbolRoselValueList = []
    global enSymId
    global symbolEnId

    processor = Variables.get("__PROCESSOR")
    # One subset of devices in this family has registers the other members do not.  Need to differentiate between them.
    if(("154F128" in processor) or ("174F256" in processor) or ("254F128" in processor) or ("274F256" in processor)):
        ds60001404 = True
    else:
        ds60001404 = False

    # this symbol is used in ftl files
    ds60001404Sym = coreComponent.createBooleanSymbol("DS60001404_SERIES", None)
    if(ds60001404 == True):
        ds60001404Sym.setDefaultValue(True)
    else:
        ds60001404Sym.setDefaultValue(False)
    ds60001404Sym.setVisible(False)

    # atdf-specific areas
    if(ds60001404 == False):
        clkValGrp_REFOCON__ROSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__ROSEL"]')
        clkValGrp_REFOCON__RODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__RODIV"]')
        clkValGrp_REFOTRIM__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOTRIM__ROTRIM"]')
        clkRegGrp_REFOTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFOTRIM"]')
        clkRegGrp_REFOCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="REFOCON"]')
        clkValGrp_OSCCON__PLLODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__PLLODIV"]')
        clkValGrp_OSCCON__PBDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__PBDIV"]')
        clkValGrp_OSCCON__PLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__PLLMULT"]')
        clkValGrp_REFOCON__ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__ON"]')
        clkValGrp_REFOCON__OE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOCON__OE"]')
        clkValGrp_REFOCON__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFOTRIM__ROTRIM"]')
    else:
        clkRegGrp_PBDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="PB1DIV"]')
        clkRegGrp_SPLLCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="SPLLCON"]')
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
        clkValGrp_REFOCON__ROTRIM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="REFO1TRIM__ROTRIM"]') 
        clkValGrp_SPLLCON__PLLICLK = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="SPLLCON__PLLICLK"]')
        clkValGrp_SPLLCON__PLLIDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="SPLLCON__PLLIDIV"]')
        clkValGrp_SPLLCON__PLLMULT = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="SPLLCON__PLLMULT"]')
        clkValGrp_SPLLCON__PLLODIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="SPLLCON__PLLODIV"]')
        clkValGrp_PBDIV__PBDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="PB1DIV__PBDIV"]')
        clkValGrp_PBDIV__ON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="PB1DIV__ON"]')

    clkRegGrp_OSCCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="OSCCON"]')
    clkRegGrp_OSCTUN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/register-group@[name="OSC"]/register@[name="OSCTUN"]')
    clkValGrp_OSCCON__FRCDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__FRCDIV"]')
    clkValGrp_OSCCON__SOSCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__SOSCEN"]')
    clkValGrp_OSCCON__NOSC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__NOSC"]')
    clkValGrp_OSCCON__OSWEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__OSWEN"]')
    clkValGrp_OSCCON__UFRCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__UFRCEN"]')
    clkValGrp_OSCTUN__TUN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCTUN__TUN"]')
    clkValGrp_OSCCON__DRMEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__DRMEN"]')
    clkValGrp_OSCCON__SLP2SPD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OSC"]/value-group@[name="OSCCON__SLP2SPD"]')

    # parse atdf file to get key parameters
    atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
    atdf_file = open(atdf_file_path, "r")
    atdf_content = ElementTree.fromstring(atdf_file.read())
    
    # Used to include family-specific code in ftl file
    PROC_FAM_SYMBOL = coreComponent.createStringSymbol("PROC_FAMILY",None)
    PROC_FAM_SYMBOL.setVisible(False)
    PROC_FAM_SYMBOL.setDefaultValue('Default')              # set to nominal value
    PROC_FAM_SYMBOL.setDefaultValue('PIC32MX')

    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_MIPS32", None)
    SYM_CLK_MENU.setLabel("Clock Menu")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    CLK_MANAGER_SELECT.setDefaultValue("clk_pic32mx:MKClockModel")

    CLK_CFG_SETTINGS = coreComponent.createMenuSymbol("ClkCfgSettings", SYM_CLK_MENU)
    CLK_CFG_SETTINGS.setDependencies(enableMenu, ["ClkSvcMenu"])
    CLK_CFG_SETTINGS.setLabel("Clock Configurator Settings")
    CLK_CFG_SETTINGS.setDescription("Various Clock System Settings")
    CLK_CFG_SETTINGS.setVisible(True)

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

    # static or dynamic - always static
    CLK_SVC_MODE = coreComponent.createKeyValueSetSymbol("clkSvcMode", SYM_CLK_MENU)
    CLK_SVC_MODE.setDependencies(enableMenu, ["ClkSvcMenu"])
    CLK_SVC_MODE.setDescription("Static or Dynamic (clocks can be changed during runtime)")
    CLK_SVC_MODE.setOutputMode("Value")
    CLK_SVC_MODE.setDisplayMode("Description")
    CLK_SVC_MODE.addKey("STATIC", "0", "Static: Clocks do not change after being set at startup." )
    CLK_SVC_MODE.setVisible(False)
    CLK_SVC_MODE.setSelectedKey("STATIC",1)

    # now create the menus for all peripheral buses present in this part
    # Peripheral Bus symbol creation
    symbolEnId = "CONFIG_SYS_CLK_PBCLK_ENABLE"
    labelEnVal = "Enable Peripheral Clock Bus"
    symbolDivId = "CONFIG_SYS_CLK_PBDIV"
    labelDivVal = "Peripheral Clock Bus Divisor (1-128)"
    symbolEnName = coreComponent.createBooleanSymbol(symbolEnId, CLK_CFG_SETTINGS)
    pbclkEnName = symbolEnId
    symbolEnName.setLabel(labelEnVal)
    symbolEnName.setDefaultValue(True)
    if(ds60001404 == True):     # to set the ON bit of PB1DIV register - does not exist for most devices in the family
        symbolEnName.setDependencies(updatePbdiv, [symbolEnId])

    enSymId = "CONFIG_SYS_CLK_REFCLK_ENABLE"
    enSymbol = coreComponent.createBooleanSymbol(enSymId, CLK_CFG_SETTINGS)
    enSymbol.setLabel("Enable Reference Clock REFCLKO")
    enSymbol.setDescription("Sets whether to have reference clock 1 enabled")
    enSymbol.setDefaultValue(False)

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

    # OSCCON
    scan_atdf_for_osccon_fields(coreComponent, CLK_CFG_SETTINGS, USB_CFG_SETTINGS, symbolEnName)

    # OSCTUN
    scan_atdf_for_osctun_fields(coreComponent, CLK_CFG_SETTINGS)
    
    # REFOCON
    scan_atdf_for_refocon_fields(coreComponent, CLK_CFG_SETTINGS, enSymbol)

    # REFOTRIM
    scan_atdf_for_refotrim_fields(coreComponent, CLK_CFG_SETTINGS)
    
    if(ds60001404 == True):   # following registers only exist in this subset of PIC32MX family    
        # PB1DIV
        scan_atdf_for_pbdiv_fields(coreComponent, symbolEnName, symbolEnName.getValue())    
        
        # SPLLCON
        scan_atdf_for_spllcon_fields(coreComponent, CLK_CFG_SETTINGS)

        # UPLLCON
        scan_atdf_for_upllcon_fields(coreComponent, USB_CFG_SETTINGS)

    # creates calculated frequencies menu
    calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, join, ElementTree, newPoscFreq)
    
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

