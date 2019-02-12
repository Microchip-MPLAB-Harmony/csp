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

###################################################################################################
########################### Global variables   #################################
###################################################################################################

global adchsInstanceName

# A set of arrays for keeping track of each chanel's parameters.
adchsCHMenu = []
adchsCONMenu = []
adchsSym_CH_ENABLE = []
adchsSym_CH_NAME = []

###################################################################################################
########################### Locally Used Functions   #################################
###################################################################################################
def _find_default_value(bitfieldNode, initialRegValue):
    '''
    Helper function to lookup default value for a particular bitfield within a given register from atdf node
    Arguments:
      bitfieldNode - the particular <bitfield > entry in the atdf file being looked at
      initialRegValue - initval of <register > entry in the atdf file.  Holds initial values of
                        all fields for this register.
    '''
    # make initialRegValue an integer
    registerValue = int(initialRegValue[2:],16)   # get rid of the '0x'

    # find bitshift of lsb of field
    maskStr = bitfieldNode.getAttribute('mask').strip('L')
    if(maskStr.find('0x') != -1):
        mask = int(maskStr[2:],16)
    else:
        mask = int(maskStr)
    shift = 0
    for ii in range(0,32):
        if( ((mask >> ii) & 1) != 0):
            shift = ii
            break
    return((registerValue & mask) >> shift)

# Parse through the value fields of the value-group given by node.
# It looks at each value for a value attribute and a caption attribute.
# It ignores those captions marked "reserved" and adds the rest to the
# outputList as desc and keys.  It then adds the associated value attribute
# to the same index of the outputList.
# All together, it creates a set of 'desc', 'key', and 'value' strings suitable
# for use in creating a KeyValueSet drop down box.
#
def _get_bitfield_names(node, outputList):
    valueNodes = node.getChildren()
    for ii in reversed(valueNodes):
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)

            # Log.writeInfoMessage("desc: " + dict['desc'] + " key: " + dict['key'] + " value: " + dict['value'])
            outputList.append(dict)


def adchsATDFRegisterPath(ModuleName, RegisterName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]')
    return labelPath

def adchsATDFRegisterBitfieldPath(ModuleName, RegisterName, BitfieldName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
        + BitfieldName +'"]')
    return labelPath

def adchsATDFValueGroupPath(ModuleName, ValueGroupName):
    value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
        + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
    return value_groupPath

def adchsATDFValueGroupValuePath(ModuleName, ValueGroupName, ValueString):
    valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
        + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
        ValueString + '"]')
    return valuePath


# This creates a sub menu based on the caption attribute of a Register in the
# ATDF file.
# Parent is the parent component to the newly created component.  In this case
# it is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop down box for.
# Menu is the menu under which to create the new component.
#
# Within the ATDF file, it fins the following register:
# modules/module@[name="' + ModuleName + '"]/register-group@[name="
# ' + ModuleName + '"]/register@[name="' + RegisterName + '"]')
# The caption of this register is used in the label of the new menu.
#
def adchsAddRegisterSubMenuFromATDF(Parent, ModuleName, RegisterName, ParentMenu):
    # Log.writeInfoMessage("Adding Menu: " + ModuleName + "_MENU_" + RegisterName)
    labelPath = adchsATDFRegisterPath(ModuleName, RegisterName)
    labelNode = ATDF.getNode(labelPath)
    if labelNode is not None:
        Menu = Parent.createMenuSymbol(ModuleName + "_MENU_" + RegisterName, ParentMenu)
        Menu.setLabel(RegisterName + ': ' + labelNode.getAttribute('caption'))
        return Menu
    else:
        Log.writeErrorMessage("Adding Menu: Failed!! no such node. " + labelPath)
    return None

# This creates a ValueKeySet symbol which results in a drop down box with a
# particular register's bitfield's caption and the key-value pairs from the
# associated value group.
# It assumes that the value-group is named [REGISTER]__[BITFIELD]
#
# Parent is the parent component to the newly created component.  In this case
# it is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop down box for.
# Menu is the menu under which to create the new component.
# Visibility is wether or not to make the component visible.
#
# Within the ATDF file, it fins the following bitfield:
# /modules/module@[name="'+ModuleName+'"]/register-group@[name="
# '+ModuleName+'"]/register@[name="'+RegisterName+'"]/bitfield@[name="
# '+BitFieldName+'"]')
# It uses the "caption" attribute of this bitfield as the label for the
# keyValueSet.
#
# Within the ATDF file, it finds the following value-group:
# /modules/module@[name="+ModuleName+'"]/value-group@[name="
# '+RegisterName+'__'+BitFieldName+'"]')
#
# Within this value-group it uses the _get_bitfield_names function to get
# the Key-Value pairs.
#
def adchsAddKeyValueSetFromATDFInitValue(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding KeyValueSet" + ModuleName + " " + RegisterName
        # + " " + BitFieldName)
    registerPath = adchsATDFRegisterPath(ModuleName, RegisterName)
    registerNode = ATDF.getNode(registerPath)
    if registerNode is not None:
        labelPath = adchsATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            value_groupPath = adchsATDFValueGroupPath(ModuleName, RegisterName
                + '__' + BitFieldName)
            value_groupNode = ATDF.getNode(value_groupPath)
            if value_groupNode is not None:
                # Log.writeInfoMessage("    KeyValueSet ID String" + RegisterName + '__' +
                    # BitFieldName)
                Component = Parent.createKeyValueSetSymbol(RegisterName + '__' +
                    BitFieldName, Menu)
                adchsValGrp_names = []
                _get_bitfield_names(value_groupNode, adchsValGrp_names)

                Component.setLabel(labelNode.getAttribute('caption'))
                Component.setOutputMode("Value")
                Component.setDisplayMode("Description")
                for ii in adchsValGrp_names:
                    Component.addKey( ii['desc'], ii['value'], ii['key'] )

                initval = registerNode.getAttribute('initval')
                if initval is not None:
                    # Log.writeInfoMessage(" Register: " + RegisterName + " initval: " + initval)
                    #_find_default_value(labelNode, initval):
                    valuenode = value_groupNode.getChildren()  # look at all the <value ..> entries underneath <value-group >
                    Component.setDefaultValue(_find_default_value(labelNode, initval))
                else:
                    Component.setDefaultValue(0)

                Component.setVisible(Visibility)
                return Component

            else:
                Log.writeErrorMessage("Adding KeyValueSet: Failed!! no such node. " + value_groupPath)

        else:
            Log.writeErrorMessage("Adding KeyValueSet: Failed!! no such node. " + labelPath)
    else:
        Log.writeErrorMessage("Adding KeyValueSet: Failed!! no such node. " + registerPath)

    return None


# This creates a Boolean symbol which results in a check box with a
# particular register's bitfield's caption
#
# Parent is the parent component to the newly created component.  In this case
# it is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop down box for.
# Menu is the menu under which to create the new component.
# Visibility is wether or not to make the component visible.
#
# Within the ATDF file, it fins the following bitfield:
# /modules/module@[name="'+ModuleName+'"]/register-group@[name="
# '+ModuleName+'"]/register@[name="'+RegisterName+'"]/bitfield@[name="
# '+BitFieldName+'"]')
# It uses the "caption" attribute of this bitfield as the label for the
# keyValueSet.
#
# Within the ATDF file, it finds the following value-group:
# /modules/module@[name="+ModuleName+'"]/value-group@[name="
# '+RegisterName+'__'+BitFieldName+'"]')
#
def adchsAddBooleanFromATDF1ValueValueGroup(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    value_groupPath = adchsATDFValueGroupValuePath(ModuleName, RegisterName
        + '__' + BitFieldName, "0x1")
    labelNode = ATDF.getNode(value_groupPath)
    if labelNode is not None:
        Component = Parent.createBooleanSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('caption'))
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        Log.writeErrorMessage("Adding Boolean: Failed!! no such node. " + value_groupPath)
    return None

def adchsAddBooleanFromATDFBitfieldName(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adchsATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
    labelNode = ATDF.getNode(labelPath)
    if labelNode is not None:
        Component = Parent.createBooleanSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('name'))
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        Log.writeErrorMessage("Adding Boolean: Failed!! no such node. " + labelPath)
    return None

def adchsAddBooleanFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adchsATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
    labelNode = ATDF.getNode(labelPath)
    if labelNode is not None:
        Component = Parent.createBooleanSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('caption'))
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        Log.writeErrorMessage("Adding Boolean: Failed!! no such node. " + labelPath)
    return None

# This creates a Long symbol which results in a 32 bit unsigned number box
# with a particular register's bitfield's caption.
#
# Parent is the parent component to the newly created component.  In this case
# it is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a non numerical input
#       down box for.
# Menu is the menu under which to create the new component.
# Visibility is wether or not to make the component visible.
#
# Within the ATDF file, it fins the following register:
# modules/module@[name="' + ModuleName + '"]/register-group@[name="
# ' + ModuleName + '"]/register@[name="' + RegisterName + '"]')
# The caption of this register is used in the label of the new component.
#
def adchsAddLongFromATDFRegisterCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adchsATDFRegisterPath(ModuleName, RegisterName)
    labelNode = ATDF.getNode(labelPath)
    if labelNode is not None:
        Component = Parent.createLongSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('caption') + ' - ' + BitFieldName)
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        Log.writeErrorMessage("Adding Long: Failed!! no such node. " + labelPath)
    return None

def adchsAddLongFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adchsATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
    labelNode = ATDF.getNode(labelPath)
    if labelNode is not None:
        Component = Parent.createLongSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('caption'))
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        Log.writeErrorMessage("Adding Long: Failed!! no such node. " + labelPath)
    return None

def getIRQnumber(string):
    interrupts = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts')
    interruptsChildren = interrupts.getChildren()
    for param in interruptsChildren:
        modInst = param.getAttribute('name')
        if(string == modInst):
            irq_index = param.getAttribute('index')
    return irq_index

def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    return index

def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    regName = "IFS"+str(index)
    return regName

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################
global ADC_Max_Class_1
global ADC_Max_Signals
global ADC_Max_Class_1and2
global adchsSym_ADCTIME

# Meant to be used as a dependancy callback so that a sub element of a boolean
# symbol can become visible when the boolean becomes true.
def adchsVisibilityOnEvent(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#ADCCON1 register value
def adchsCalcADCCON1(symbol, event):
    adccon1 = 0x0
    component = symbol.getComponent()
    fract = component.getSymbolValue("ADCCON1__FRACT") << 23
    slres = component.getSymbolValue("ADCCON1__SELRES") << 21
    strgsrc = component.getSymbolValue("ADCCON1__STRGSRC") << 16
    sidl = component.getSymbolValue("ADCCON1__SIDL") << 13
    cvden = component.getSymbolValue("ADCCON1__CVDEN") << 11
    fssclken = component.getSymbolValue("ADCCON1__FSSCLKEN") << 10
    fspbcclken = component.getSymbolValue("ADCCON1__FSPBCLKEN") << 9
    irqvs = component.getSymbolValue("ADCCON1__IRQVS") << 4
    strglvl = component.getSymbolValue("ADCCON1__STRGLVL") << 3
    adccon1 = fract + slres + strgsrc + sidl + cvden + fssclken + fspbcclken + irqvs + strglvl
    symbol.setValue(adccon1, 2)

def adchsCalcADCCON2(symbol, event):
    adccon2 = 0x0
    component = symbol.getComponent()
    adcdiv = component.getSymbolValue("ADCCON2__ADCDIV") << 0
    adceis = component.getSymbolValue("ADCCON2__ADCEIS") << 8
    samc = component.getSymbolValue("ADCCON2__SAMC") << 16
    cvdcpl = component.getSymbolValue("ADCCON2__CVDCPL") << 26
    adccon2 = adcdiv + adceis + samc + cvdcpl
    symbol.setValue(adccon2, 2)

def adchsCalcADCCON3(symbol, event):
    adccon3 = 0x0
    component = symbol.getComponent()
    adcsel = component.getSymbolValue("ADCCON3__ADCSEL") << 30
    conclkdiv = (component.getSymbolValue("ADCCON3__CONCLKDIV") - 1) << 24
    vrefsel = component.getSymbolValue("ADCCON3__VREFSEL") << 13
    adccon3 = adcsel + conclkdiv + vrefsel
    symbol.setValue(adccon3, 2)

def adchsCalcADCTRGMODE(symbol, event):
    adctrgmode = 0x0
    ssampen = 0x0
    strgen = 0x0
    shalt = 0x0
    component = symbol.getComponent()
    for channelID in range(0, ADC_Max_Class_1):
        if(component.getSymbolValue("ADCHS_"+str(channelID)+"_ENABLE")):
            ssampen = ssampen + (component.getSymbolValue("ADCTRGMODE__SSAMPEN" + str(channelID)) << channelID)
            strgen = strgen + (component.getSymbolValue("ADCTRGMODE__STRGEN" + str(channelID)) << (channelID + 8))
            shalt = shalt + (component.getSymbolValue("ADCTRGMODE__SH" + str(channelID) + "ALT") << (channelID * 2 + 16))
    adctrgmode = ssampen + strgen + shalt
    symbol.setValue(adctrgmode, 2)

def adchsCalcADCIMCON1(symbol, event):
    adcimcon1 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(0, 16):
        if (component.getSymbolValue("ADCIMCON3__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON1__SIGN" + str(channelID)) << (channelID*2))
        if (component.getSymbolValue("ADCIMCON3__DIFF" + str(channelID)) != None):
            diff = diff + (component.getSymbolValue("ADCIMCON1__DIFF" + str(channelID)) << ((channelID * 2) + 1))
    adcimcon1 = sign + diff
    symbol.setValue(adcimcon1, 2)

def adchsCalcADCIMCON2(symbol, event):
    adcimcon2 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(16, 32):
        if (component.getSymbolValue("ADCIMCON3__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON2__SIGN" + str(channelID)) << ((channelID - 16) * 2))
        if (component.getSymbolValue("ADCIMCON3__DIFF" + str(channelID)) != None):
            diff = diff + (component.getSymbolValue("ADCIMCON2__DIFF" + str(channelID)) << (((channelID - 16) * 2) + 1))
    adcimcon2 = sign + diff
    symbol.setValue(adcimcon2, 2)

def adchsCalcADCIMCON3(symbol, event):
    adcimcon3 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(32, ADC_Max_Signals):
        if (component.getSymbolValue("ADCIMCON3__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON3__SIGN" + str(channelID)) << ((channelID - 32) * 2))
        if (component.getSymbolValue("ADCIMCON3__DIFF" + str(channelID)) != None):
            diff = diff + (component.getSymbolValue("ADCIMCON3__DIFF" + str(channelID)) << (((channelID - 32) * 2) + 1))
    adcimcon3 = sign + diff
    symbol.setValue(adcimcon3, 2)

def adchsCalcADCTRG1(symbol, value):
    adctrg1 = 0x0
    trgsrc = 0x0
    component = symbol.getComponent()
    for channelID in range(0, 4):
        if (component.getSymbolValue("ADCTRG1__TRGSRC" + str(channelID)) != None):
            trgsrc = trgsrc + (component.getSymbolValue("ADCTRG1__TRGSRC" + str(channelID)) << ((channelID * 8)))
    adctrg1 = trgsrc
    symbol.setValue(adctrg1, 2)

def adchsCalcADCTRG2(symbol, value):
    adctrg2 = 0x0
    trgsrc = 0x0
    component = symbol.getComponent()
    for channelID in range(4, 8):
        if (component.getSymbolValue("ADCTRG2__TRGSRC" + str(channelID)) != None):
            trgsrc = trgsrc + (component.getSymbolValue("ADCTRG2__TRGSRC" + str(channelID)) << ((channelID - 4) * 8))
    adctrg2 = trgsrc
    symbol.setValue(adctrg2, 2)

def adchsCalcADCTRG3(symbol, value):
    adctrg3 = 0x0
    trgsrc = 0x0
    component = symbol.getComponent()
    for channelID in range(8, ADC_Max_Class_1and2):
        if (component.getSymbolValue("ADCTRG3__TRGSRC" + str(channelID)) != None):
            trgsrc = trgsrc + (component.getSymbolValue("ADCTRG3__TRGSRC" + str(channelID)) << ((channelID - 8) * 8))
    adctrg3 = trgsrc
    symbol.setValue(adctrg3, 2)

def adchsCalcADCTIME(symbol, event):
    adctime = [ADC_Max_Class_1]
    component = symbol.getComponent()
    for channelID in range(0, ADC_Max_Class_1):
        samc = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__SAMC") << (0))
        adcdiv = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__ADCDIV") << (16))
        selres = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__SELRES") << (24))
        adceis = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__ADCEIS") << (26))
        adctime.append(channelID)
        adctime[channelID] = samc +  adcdiv + selres + adceis
        adchsSym_ADCTIME[channelID].setValue(adctime[channelID], 2)

def adchsCalcADCTRGSNS(symbol, event):
    adctrgsns = 0x0
    lvl = 0x0
    component = symbol.getComponent()
    for channelID in range(0, ADC_Max_Class_1and2):
        if (component.getSymbolValue("ADCTRGSNS__LVL" + str(channelID)) != None):
            lvl = trgsrc + (component.getSymbolValue("ADCTRGSNS__LVL" + str(channelID)) << (channelID))
    adctrgsns = lvl
    symbol.setValue(adctrgsns, 2)

def adchsCalcADCGIRQEN1(symbol, event):
    adcgirqen = 0x00
    agien = 0x0
    component = symbol.getComponent()
    for channelID in range(0, 32):
        if (component.getSymbolValue("ADCGIRQEN1__AGIEN" + str(channelID)) != None):
            agien = agien + (component.getSymbolValue("ADCGIRQEN1__AGIEN" + str(channelID)) << (channelID))
    adcgirqen = agien
    symbol.setValue(adcgirqen, 2)

def adchsCalcADCGIRQEN2(symbol, event):
    adcgirqen = 0x00
    agien = 0x0
    component = symbol.getComponent()
    for channelID in range(32, ADC_Max_Signals):
        if (component.getSymbolValue("ADCGIRQEN2__AGIEN" + str(channelID)) != None):
            agien = agien + (component.getSymbolValue("ADCGIRQEN2__AGIEN" + str(channelID)) << (channelID - 32))
    adcgirqen = agien
    symbol.setValue(adcgirqen, 2)

def adchsCalcADCCSS1(symbol, event):
    adccss = 0x00
    css = 0x0
    component = symbol.getComponent()
    for channelID in range(0, 32):
        if (component.getSymbolValue("ADCCSS1__CSS" + str(channelID)) != None):
            css = css + (component.getSymbolValue("ADCCSS1__CSS" + str(channelID)) << (channelID))
    adccss = css
    symbol.setValue(adccss, 2)

def adchsCalcADCCSS2(symbol, event):
    adccss = 0x00
    css = 0x0
    component = symbol.getComponent()
    for channelID in range(32, ADC_Max_Signals):
        if (component.getSymbolValue("ADCCSS2__CSS" + str(channelID)) != None):
            css = css + (component.getSymbolValue("ADCCSS2__CSS" + str(channelID)) << (channelID - 32))
    adccss = css
    symbol.setValue(adccss, 2)

def adchsCalcIEC0(symbol, event):
    iec0 = 0x00
    agien = 0x0
    component = symbol.getComponent()
    start = Irq_index % 32
    for channelID in range(0, len(adciec_depList[0])):
        if (component.getSymbolValue(adciec_depList[0][channelID]) != None):
            agien = agien + (component.getSymbolValue(adciec_depList[0][channelID]) << (start + channelID))
    iec0 = agien
    symbol.setValue(iec0, 2)

def adchsCalcIEC1(symbol, event):
    iec1 = 0x00
    agien = 0x0
    component = symbol.getComponent()
    for channelID in range(0, len(adciec_depList[1])):
        if (component.getSymbolValue(adciec_depList[1][channelID]) != None):
            agien = agien + (component.getSymbolValue(adciec_depList[1][channelID]) << (channelID))
    iec1 = agien
    symbol.setValue(iec1, 2)

def adchsCalcIEC2(symbol, event):
    iec2 = 0x00
    agien = 0x0
    component = symbol.getComponent()
    for channelID in range(0, len(adciec_depList[2])):
        if (component.getSymbolValue(adciec_depList[2][channelID]) != None):
            agien = agien + (component.getSymbolValue(adciec_depList[2][channelID]) << (channelID))
    iec2 = agien
    symbol.setValue(iec2, 2)

def adchsInterruptMode(symbol, event):
    interrupt_mode = False
    component = symbol.getComponent()
    for channelID in range(0, len(adcinterruptmode_deplist)):
        if (component.getSymbolValue(adcinterruptmode_deplist[channelID])):
            interrupt_mode = True
    symbol.setValue(interrupt_mode, 2)

    InterruptVector = "ADC_DATA" + event["id"].split("__AGIEN")[1] + "_INTERRUPT_ENABLE"
    InterruptHandlerLock = "ADC_DATA" + event["id"].split("__AGIEN")[1]  + "_INTERRUPT_HANDLER_LOCK"
    InterruptHandler = "ADC_DATA" + event["id"].split("__AGIEN")[1]  + "_INTERRUPT_HANDLER"

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)
    interruptName = InterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if(event["value"] == True):
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_Handler", 1)

def adchsClockCalc(symbol, event):
    component = symbol.getComponent()
    symbol.setValue(Database.getSymbolValue("core", "ADCHS_CLOCK_FREQUENCY") / component.getSymbolValue("ADCCON3__CONCLKDIV"), 2)

###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(adchsComponent):
    global adchsInstanceName
    global ADC_Max_Class_1
    global ADC_Max_Signals
    global ADC_Max_Class_1and2
    global ADC_Max_Signals
    global Irq_index
    global adciec_depList
    global adcinterruptmode_deplist

    adchsInstanceName = adchsComponent.createStringSymbol("ADCHS_INSTANCE_NAME", None)
    adchsInstanceName.setVisible(False)
    adchsInstanceName.setDefaultValue(adchsComponent.getID().upper())
    Module = adchsInstanceName.getValue()
    Log.writeInfoMessage("Running " + Module)

    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))

    adchs = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]")

    ADC_Max_DedicatedChannels = 0
    ADC_Max_Signals = 0
    ADC_Max_Class_1and2 = 0
    ADC_Max_Class_1 = 0
    ADC_Max_Class_2 = 0
    # Each of the dedicated ADCHS SARs must have a DIGEN bit field in the
    # ADCCON3 SFR.  So, counting them give the number of dedicated ADC
    # channels.  Note, ADC7 should always exist as the shared SAR.
    for ChannelNumber in range(0, 7):
        labelPath = adchsATDFRegisterBitfieldPath(Module, "ADCCON3",
            "DIGEN" + str(ChannelNumber))
        # Log.writeInfoMessage("Looking for Attribute of " + labelPath)
        labelNode = ATDF.getNode(labelPath).getAttribute("values")
        if labelNode is not None:
            ADC_Max_DedicatedChannels += 1
    ADC_Max_Class_1 = ADC_Max_DedicatedChannels

    # Each Analog channel on the part must have a Data Register.  Each existing
    # Data register should indicate that there is an Analog pin for that signal.
    SignalNumber = 0
    labelPath = adchsATDFRegisterPath(Module, "ADCDATA" + str(SignalNumber))
    labelNode = ATDF.getNode(labelPath)
    while labelNode is not None:
        ADC_Max_Signals += 1
        SignalNumber += 1
        labelPath = adchsATDFRegisterPath(Module, "ADCDATA" + str(SignalNumber))
        labelNode = ATDF.getNode(labelPath)
    # for SignalNumber in range(0, 43):
        # labelPath = adchsATDFRegisterPath(Module, "ADCDATA" + str(SignalNumber))
        # labelNode = ATDF.getNode(labelPath)
        # if labelNode is not None:
            # ADC_Max_Signals += 1

    # The dedicated channels use class 1 signals.  All Class 1 AND class 2
    # signals must have a TRGSRC bit field in one of the ADCTRG SFRs.
    for RegisterNumber in range(0, 7):
        RegisterName = "ADCTRG" + str(RegisterNumber+1)
        labelPath = adchsATDFRegisterPath(Module, RegisterName)
        # Log.writeInfoMessage("Looking for Register" + labelPath)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            for SignalNumber in range(0, 4):
                signalID = (RegisterNumber * 4) + SignalNumber
                SignalName = "TRGSRC" + str(signalID)
                labelPath = adchsATDFRegisterBitfieldPath(Module, RegisterName,
                    SignalName )
                # Log.writeInfoMessage("Looking for Bitfield" + labelPath)
                labelNode = ATDF.getNode(labelPath)
                if labelNode is not None:
                    ADC_Max_Class_1and2 += 1
    ADC_Max_Class_2 = ADC_Max_Class_1and2 - ADC_Max_Class_1

    #Calculate the proper interrupt registers using IRQ#
    irqString = "ADC_DATA0"
    Irq_index = int(getIRQnumber(irqString))
    statRegName = _get_statReg_parms(Irq_index)
    enblRegIndex = _get_enblReg_parms(Irq_index)

    adchsSym_IRQ = adchsComponent.createIntegerSymbol("ADCHS_IFS_START_INDEX", None)
    adchsSym_IRQ.setVisible(False)
    adchsSym_IRQ.setDefaultValue(enblRegIndex)

    ADC_MAX_EIC_REG = 1

    #IEC REG
    adchsSym_IEC0 = adchsComponent.createStringSymbol("ADCHS_IEC0_REG", None)
    adchsSym_IEC0.setDefaultValue("IEC"+str(enblRegIndex))
    adchsSym_IEC0.setVisible(False)

##### Assumption is all the data result interrupt vectors are sequential
    num_intrpt_in_first_iec = 32 - (Irq_index % 32)
    adchsSym_IFS0_INDEX = adchsComponent.createIntegerSymbol("ADCHS_IFS0_NUM_IRQ", None)
    adchsSym_IFS0_INDEX.setVisible(False)
    adchsSym_IFS0_INDEX.setDefaultValue( num_intrpt_in_first_iec)

    if ((ADC_Max_Signals - (num_intrpt_in_first_iec))) > 32:
        #IEC REG
        adchsSym_IEC1 = adchsComponent.createStringSymbol("ADCHS_IEC1_REG", None)
        adchsSym_IEC1.setDefaultValue("IEC"+str(enblRegIndex+1))
        adchsSym_IEC1.setVisible(False)
        ADC_MAX_EIC_REG = ADC_MAX_EIC_REG + 1

        adchsSym_IFS1_INDEX = adchsComponent.createIntegerSymbol("ADCHS_IFS1_NUM_IRQ", None)
        adchsSym_IFS1_INDEX.setVisible(False)
        adchsSym_IFS1_INDEX.setDefaultValue(32 + (num_intrpt_in_first_iec))

    if ((ADC_Max_Signals - (num_intrpt_in_first_iec)) % 32) != 0 :
        #IEC REG
        adchsSym_IEC2 = adchsComponent.createStringSymbol("ADCHS_IEC2_REG", None)
        adchsSym_IEC2.setDefaultValue("IEC"+str(enblRegIndex+2))
        adchsSym_IEC2.setVisible(False)
        ADC_MAX_EIC_REG = ADC_MAX_EIC_REG + 1

    adctrgmode_deplist = []
    adctrgsns_deplist = []
    adctrg_deplist = [[] for i in range (3)]
    adctime_deplist = [[] for i in range (ADC_Max_Class_1)]
    adcgirqen_deplist = [[] for i in range (2)]
    adccss_deplist = [[] for i in range (2)]
    adciec_depList = [[] for i in range (ADC_MAX_EIC_REG)]
    adcinterruptmode_deplist = []

    adchsMenu = adchsComponent.createMenuSymbol("ADCHS_MENU", None)
    adchsMenu.setLabel("ADCHS Configuration")

    #max no of channels
    adchsSym_NUM_CHANNELS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CHANNELS", adchsMenu)
    adchsSym_NUM_CHANNELS.setDefaultValue(ADC_Max_DedicatedChannels)
    adchsSym_NUM_CHANNELS.setVisible(False)
    #adchsSym_NUM_CHANNELS.setVisible(True)

    #max no of signals
    adchsSym_NUM_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_SIGNALS", adchsMenu)
    adchsSym_NUM_SIGNALS.setDefaultValue(ADC_Max_Signals)
    adchsSym_NUM_SIGNALS.setVisible(False)
    #adchsSym_NUM_SIGNALS.setVisible(True)

    #no of Class 1 signals
    adchsSym_NUM_CLASS1_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CLASS1_SIGNALS", adchsMenu)
    adchsSym_NUM_CLASS1_SIGNALS.setDefaultValue(ADC_Max_Class_1)
    adchsSym_NUM_CLASS1_SIGNALS.setVisible(False)
    #adchsSym_NUM_CLASS1_SIGNALS.setVisible(True)

    #no of Class 2 signals
    adchsSym_NUM_CLASS2_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CLASS2_SIGNALS", adchsMenu)
    adchsSym_NUM_CLASS2_SIGNALS.setDefaultValue(ADC_Max_Class_2)
    adchsSym_NUM_CLASS2_SIGNALS.setVisible(False)

    adchsCHConfMenu = adchsComponent.createMenuSymbol("ADCHS_CH_CONF", None)
    adchsCHConfMenu.setLabel("Module Configuration")

    adchsSym_ADCCON3__DIGEN = []
    adchsSym_ADCTRGMODE__SSAMPEN = []
    adchsSym_ADCTRGMODE__STRGEN = []
    adchsSym_ADCTRGMODE__SHxALT = []
    adchsSym_ADCTIME__SAMC = []
    adchsSym_ADCTIME__ADCDIV = []
    adchsSym_ADCTIME__SELRES = []
    adchsSym_ADCTIME__ADCEIS = []
    adchsSym_ADCTRG__TRGSRC = []
    adchsSym_ADCTRGSNS__LVL = []
    adchsSym_ADCCSS__CSS = []
    adchsSym_class2 = []

    for channelID in range(0, ADC_Max_Class_1):
        #Channel enable
        adchsSym_CH_ENABLE.append(channelID)
        adchsSym_CH_ENABLE[channelID] = adchsComponent.createBooleanSymbol(
            "ADCHS_"+str(channelID)+"_ENABLE", adchsCHConfMenu)
        adchsSym_CH_ENABLE[channelID].setLabel("Dedicated Module " + str(channelID))
        adchsSym_CH_ENABLE[channelID].setDefaultValue(False)

        adctrgmode_deplist.append("ADCHS_"+str(channelID)+"_ENABLE")

        #Channel name
        adchsSym_CH_NAME.append(channelID)
        adchsSym_CH_NAME[channelID] = adchsComponent.createStringSymbol(
            "ADCHS_"+str(channelID)+"_NAME", adchsSym_CH_ENABLE[channelID])
        adchsSym_CH_NAME[channelID].setLabel("Name")
        adchsSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
        adchsSym_CH_NAME[channelID].setVisible(False)
        adchsSym_CH_NAME[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])

        # Channel Synchronous Sample Enable
        adchsSym_ADCTRGMODE__SSAMPEN.append(channelID)
        adchsSym_ADCTRGMODE__SSAMPEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, "ADCTRGMODE", "SSAMPEN" + str(channelID),
            adchsSym_CH_ENABLE[channelID], False)
        # adchsSym_ADCTRGMODE__SSAMPEN[channelID].setDependencies(adchsVisibilityOnEvent,
        #     ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctrgmode_deplist.append("ADCTRGMODE__SSAMPEN" + str(channelID))
        adchsSym_ADCTRGMODE__SSAMPEN[channelID].setVisible(False)

        # Channel PreSynchronous Trigger Enable
        adchsSym_ADCTRGMODE__STRGEN.append(channelID)
        adchsSym_ADCTRGMODE__STRGEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, "ADCTRGMODE", "STRGEN" + str(channelID),
            adchsSym_CH_ENABLE[channelID], False)
        # adchsSym_ADCTRGMODE__STRGEN[channelID].setDependencies(adchsVisibilityOnEvent,
        #     ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctrgmode_deplist.append("ADCTRGMODE__STRGEN" + str(channelID))
        adchsSym_ADCTRGMODE__STRGEN[channelID].setVisible(False)

        # Channel Analog Input Select
        adchsSym_ADCTRGMODE__SHxALT.append(channelID)
        adchsSym_ADCTRGMODE__SHxALT[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, "ADCTRGMODE", "SH" + str(channelID) + "ALT",
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTRGMODE__SHxALT[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctrgmode_deplist.append("ADCTRGMODE__SH" + str(channelID) + "ALT")

        RegisterNameBase1 = "ADC"
        RegisterNameBase2 = "TIME"
        BitFieldBaseName_SAMC = "SAMC"
        BitFieldBaseName_ADCDIV = "ADCDIV"
        BitFieldBaseName_SELRES = "SELRES"
        BitFieldBaseName_ADCEIS = "ADCEIS"
        RegisterName = str(RegisterNameBase1 + str(channelID) + RegisterNameBase2)

        #clock divider
        adchsSym_ADCTIME__ADCDIV.append(channelID)
        adchsSym_ADCTIME__ADCDIV[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
            Module, RegisterName, BitFieldBaseName_ADCDIV,
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTIME__ADCDIV[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adchsSym_ADCTIME__ADCDIV[channelID].setMin(0)
        adchsSym_ADCTIME__ADCDIV[channelID].setMax(127)
        adctime_deplist[channelID].append(RegisterName + "__" + BitFieldBaseName_ADCDIV)

        #sample time
        adchsSym_ADCTIME__SAMC.append(channelID)
        adchsSym_ADCTIME__SAMC[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
            Module, RegisterName, BitFieldBaseName_SAMC,
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTIME__SAMC[channelID].setDefaultValue(2)
        adchsSym_ADCTIME__SAMC[channelID].setMin(0)
        adchsSym_ADCTIME__SAMC[channelID].setMax(1023)
        adchsSym_ADCTIME__SAMC[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctime_deplist[channelID].append(RegisterName + "__" + BitFieldBaseName_SAMC)

        #result resolution
        adchsSym_ADCTIME__SELRES.append(channelID)
        adchsSym_ADCTIME__SELRES[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, RegisterName, BitFieldBaseName_SELRES,
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTIME__SELRES[channelID].setDefaultValue(3)
        adchsSym_ADCTIME__SELRES[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctime_deplist[channelID].append(RegisterName + "__" + BitFieldBaseName_SELRES)

        #early interrupt
        adchsSym_ADCTIME__ADCEIS.append(channelID)
        adchsSym_ADCTIME__ADCEIS[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, RegisterName, BitFieldBaseName_ADCEIS,
            adchsSym_CH_ENABLE[channelID], False)
        # adchsSym_ADCTIME__ADCEIS[channelID].setDependencies(adchsVisibilityOnEvent,
        #     ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctime_deplist[channelID].append(RegisterName + "__" + BitFieldBaseName_ADCEIS)
        adchsSym_ADCTIME__ADCEIS[channelID].setVisible(False)

        RegisterNameBase = "ADCTRG"
        BitFieldBaseName_TRGSRC = "TRGSRC"
        RegisterName = RegisterNameBase + str((channelID/4)+1)
        # trigger source
        adchsSym_ADCTRG__TRGSRC.append(channelID)
        adchsSym_ADCTRG__TRGSRC[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, RegisterName, BitFieldBaseName_TRGSRC +
            str(channelID), adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTRG__TRGSRC[channelID].setLabel("Select Trigger Source")
        adchsSym_ADCTRG__TRGSRC[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctrg_deplist[int((channelID/4))].append(RegisterName + "__" + BitFieldBaseName_TRGSRC + str(channelID))

        RegisterNameBase = "ADCTRGSNS"
        BitFieldBaseName_LVL = "LVL"
        #trigger level
        adchsSym_ADCTRGSNS__LVL.append(channelID)
        adchsSym_ADCTRGSNS__LVL[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterNameBase, BitFieldBaseName_LVL + str(channelID),
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTRGSNS__LVL[channelID].setLabel("High Level Sensitivity of a Trigger")
        # adchsSym_ADCTRGSNS__LVL[channelID].setDependencies(adchsVisibilityOnEvent,
        #     ["ADCHS_"+str(channelID)+"_ENABLE"])
        adctrgsns_deplist.append(RegisterNameBase + "__" + BitFieldBaseName_LVL + str(channelID))
        adchsSym_ADCTRGSNS__LVL[channelID].setVisible(False)

        RegisterBaseName_ADCCSS = "ADCCSS1"
        BitFieldBaseName_CSS = "CSS"
        adchsSym_ADCCSS__CSS.append(channelID)
        adchsSym_ADCCSS__CSS[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterBaseName_ADCCSS, BitFieldBaseName_CSS + str(channelID),
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
        adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
        adccss_deplist[0].append(RegisterBaseName_ADCCSS + "__" + BitFieldBaseName_CSS + str(channelID))

    channelID = 7  # shared ADC module is fixed as 7. Class 2 and class 3 inputs are processed by shared ADC module.
    #Channel enable
    adchsSym_CH_ENABLE7 = adchsComponent.createBooleanSymbol(
        "ADCHS_"+str(channelID)+"_ENABLE", adchsCHConfMenu)
    adchsSym_CH_ENABLE7.setLabel("Shared Module " + str(channelID))
    adchsSym_CH_ENABLE7.setDefaultValue(False)

    #Channel name
    adchsSym_CH_NAME7 = adchsComponent.createStringSymbol(
        "ADCHS_"+str(channelID)+"_NAME", adchsSym_CH_ENABLE7)
    adchsSym_CH_NAME7.setLabel("Name")
    adchsSym_CH_NAME7.setDefaultValue("CHANNEL_"+str(channelID))
    adchsSym_CH_NAME7.setVisible(False)
    adchsSym_CH_NAME7.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    #clock divider
    adchsSym_ADCCON2__ADCDIV = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
        Module, "ADCCON2", "ADCDIV", adchsSym_CH_ENABLE7, False)
    adchsSym_ADCCON2__ADCDIV.setMin(0)
    adchsSym_ADCCON2__ADCDIV.setMax(127)
    adchsSym_ADCCON2__ADCDIV.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    #sample time
    adchsSym_ADCCON2__SAMC = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
        Module, "ADCCON2", "SAMC", adchsSym_CH_ENABLE7, False)
    adchsSym_ADCCON2__SAMC.setDefaultValue(2)
    adchsSym_ADCCON2__SAMC.setMin(0)
    adchsSym_ADCCON2__SAMC.setMax(1023)
    adchsSym_ADCCON2__SAMC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    # result resolution
    adchsSym_ADCCON1__SELRES = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module,
        "ADCCON1", "SELRES", adchsSym_CH_ENABLE7, False)
    adchsSym_ADCCON1__SELRES.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    # early interrupt
    adchsSym_ADCCON2__ADCEIS = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "ADCEIS", adchsSym_CH_ENABLE7, False)
    #adchsSym_ADCCON2__ADCEIS.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
    adchsSym_ADCCON2__ADCEIS.setVisible(False)

    for channelID in range(ADC_Max_Class_1, ADC_Max_Class_1and2):
        adchsSym_class2.append(channelID - ADC_Max_Class_1)
        adchsSym_class2[channelID - ADC_Max_Class_1] = adchsComponent.createCommentSymbol("ADCHS_CLASS2_INPUT" + str(channelID), adchsSym_CH_ENABLE7)
        adchsSym_class2[channelID - ADC_Max_Class_1].setLabel("CLASS 2 Input AN" + str(channelID))
        adchsSym_class2[channelID - ADC_Max_Class_1].setVisible(False)
        adchsSym_class2[channelID - ADC_Max_Class_1].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

        RegisterNameBase = "ADCTRG"
        BitFieldBaseName_TRGSRC = "TRGSRC"
        RegisterName = RegisterNameBase + str((channelID/4)+1)
        adchsSym_ADCTRG__TRGSRC.append(channelID)
        adchsSym_ADCTRG__TRGSRC[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, RegisterName, BitFieldBaseName_TRGSRC +
            str(channelID), adchsSym_class2[channelID - ADC_Max_Class_1], False)
        adchsSym_ADCTRG__TRGSRC[channelID].setLabel("Select Trigger Source")
        adchsSym_ADCTRG__TRGSRC[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
        adctrg_deplist[int((channelID/4))].append(RegisterName + "__" + BitFieldBaseName_TRGSRC + str(channelID))

        RegisterNameBase = "ADCTRGSNS"
        BitFieldBaseName_LVL = "LVL"
        adchsSym_ADCTRGSNS__LVL.append(channelID)
        adchsSym_ADCTRGSNS__LVL[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterNameBase, BitFieldBaseName_LVL + str(channelID),
            adchsSym_class2[channelID - ADC_Max_Class_1], False)
        adchsSym_ADCTRGSNS__LVL[channelID].setLabel("High Level Sensitivity of a Trigger")
        #adchsSym_ADCTRGSNS__LVL[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
        adctrgsns_deplist.append(RegisterNameBase + "__" + BitFieldBaseName_LVL + str(channelID))
        adchsSym_ADCTRGSNS__LVL[channelID].setVisible(False)

        RegisterBaseName_ADCCSS = "ADCCSS"
        BitFieldBaseName_CSS = "CSS"
        RegisterName = RegisterBaseName_ADCCSS + str((channelID/32)+1)
        adchsSym_ADCCSS__CSS.append(channelID)
        adchsSym_ADCCSS__CSS[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_CSS + str(channelID),
            adchsSym_class2[channelID - ADC_Max_Class_1], False)
        adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
        adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
        adccss_deplist[int(channelID/32)].append(RegisterBaseName_ADCCSS + "__" + BitFieldBaseName_CSS + str(channelID))

    adchsSym_class3 = adchsComponent.createCommentSymbol("ADCHS_CLASS3_INPUTS", adchsSym_CH_ENABLE7)
    adchsSym_class3.setLabel("CLASS 3 Inputs")
    adchsSym_class3.setVisible(False)
    adchsSym_class3.setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

    # trigger source
    adchsSym_ADCCON1__STRGSRC = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "STRGSRC", adchsSym_class3, False)
    adchsSym_ADCCON1__STRGSRC.setLabel("Select Trigger Source")
    adchsSym_ADCCON1__STRGSRC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

    # trigger level
    adchsSym_ADCCON1__STRGLVL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "STRGLVL", adchsSym_class3, False)
    adchsSym_ADCCON1__STRGLVL.setLabel("Select Trigger Level")
    #adchsSym_ADCCON1__STRGLVL.setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
    adchsSym_ADCCON1__STRGLVL.setVisible(False)

    for channelID in range(ADC_Max_Class_1and2, ADC_Max_Signals):
        RegisterBaseName_ADCCSS = "ADCCSS"
        BitFieldBaseName_CSS = "CSS"
        RegisterName = RegisterBaseName_ADCCSS + str((channelID/32)+1)
        adchsSym_ADCCSS__CSS.append(channelID)
        adchsSym_ADCCSS__CSS[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_CSS + str(channelID),
            adchsSym_class3, False)
        adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
        adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

    adchsSym_ADCCON3__ADCSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "ADCSEL", adchsMenu, True)
    adchsSym_ADCCON3__CONCLKDIV = adchsAddLongFromATDFBitfieldCaption(adchsComponent, Module, "ADCCON3", "CONCLKDIV", adchsMenu, True)
    adchsSym_ADCCON3__CONCLKDIV.setDefaultValue(3)
    adchsSym_ADCCON3__CONCLKDIV.setLabel("Select Clock Divider")
    adchsSym_ADCCON3__CONCLKDIV.setMin(1)
    adchsSym_ADCCON3__CONCLKDIV.setMax(64)

    adchsSym_CLOCK = adchsComponent.createIntegerSymbol("ADCHS_CLOCK", adchsMenu)
    adchsSym_CLOCK.setLabel("ADCHS Clock Frequency (Tq)")
    adchsSym_CLOCK.setDefaultValue((Database.getSymbolValue("core", "ADCHS_CLOCK_FREQUENCY")/adchsSym_ADCCON3__CONCLKDIV.getValue()))
    adchsSym_CLOCK.setDependencies(adchsClockCalc, ["core.ADCHS_CLOCK_FREQUENCY", "ADCCON3__CONCLKDIV"])
    adchsSym_CLOCK.setReadOnly(True)

    adchsSym_ADCCON3__VREFSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "VREFSEL", adchsMenu, True)
    #adchsSym_ADCCON1__FSPBCLKEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FSPBCLKEN", adchsMenu, True)
    #adchsSym_ADCCON1__FSSCLKEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FSSCLKEN", adchsMenu, True)
    adchsSym_ADCCON1__FRACT = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FRACT", adchsMenu, True)
    #adchsSym_ADCCON1__CVDEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "CVDEN", adchsMenu, True)
    #adchsSym_ADCCON2__CVDCPL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "CVDCPL", adchsMenu, True)
    #adchsSym_ADCCON1__IRQVS = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "IRQVS", adchsMenu, True)
    adchsSym_ADCCON1__SIDL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "SIDL", adchsMenu, True)

    #adchsMenu_ADCCON1 = adchsAddRegisterSubMenuFromATDF(adchsComponent, Module, "ADCCON1", adchsMenu)
    #adchsSym_ADCCON1__AICPMPEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "AICPMPEN", adchsMenu, True)
    #adchsSym_ADCCON1__ON = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "ON", adchsMenu, True)
    #adchsSym_ADCCON1__TRBSLV = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBSLV", adchsMenu, True)
    #adchsSym_ADCCON1__TRBMST = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBMST", adchsMenu, True)
    #adchsSym_ADCCON1__TRBERR = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBERR", adchsMenu, True)
    #adchsSym_ADCCON1__TRBEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBEN", adchsMenu, True)

    #adchsMenu_ADCCON2 = adchsAddRegisterSubMenuFromATDF(adchsComponent, Module, "ADCCON2", adchsMenu)
    #adchsSym_ADCCON2__ADCEIOVR = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "ADCEIOVR", adchsMenu, True)
    #adchsSym_ADCCON2__EOSIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "EOSIEN", adchsMenu, True)
    #adchsSym_ADCCON2__REFFLTIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "REFFLTIEN", adchsMenu, True)
    #adchsSym_ADCCON2__BGVRIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "BGVRIEN", adchsMenu, True)
    #adchsSym_ADCCON2__EOSRDY = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "EOSRDY", adchsMenu, True)
    #adchsSym_ADCCON2__REFFLT = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "REFFLT", adchsMenu, True)
    #adchsSym_ADCCON2__BGVRRDY = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "BGVRRDY", adchsMenu, True)

    #adchsMenu_ADCCON3 = adchsAddRegisterSubMenuFromATDF(adchsComponent, Module, "ADCCON3", adchsMenu)
    #adchsSym_ADCCON3__ADINSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "ADINSEL", adchsMenu, True)
    #adchsSym_ADCCON3__GSWTRG = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "GSWTRG", adchsMenu, True)
    #adchsSym_ADCCON3__GLSWTRG = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "GLSWTRG", adchsMenu, True)
    #adchsSym_ADCCON3__RQCNVRT = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "RQCNVRT", adchsMenu, True)
    #adchsSym_ADCCON3__SAMP = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "SAMP", adchsMenu, True)
    #adchsSym_ADCCON3__UPDRDY = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "UPDRDY", adchsMenu, True)
    #adchsSym_ADCCON3__UPDIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "UPDIEN", adchsMenu, True)
    #adchsSym_ADCCON3__TRGSUSP = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "TRGSUSP", adchsMenu, True)

    # Comparator Configuration Menu
    adchsComparatorConfigMenu = adchsComponent.createMenuSymbol("ADCHS_COMPARATOR_MENU", None)
    adchsComparatorConfigMenu.setLabel("ADC Comparator Configuration")
    adchsComparatorConfigMenu.setVisible(False)
    RegisterBaseName_ADCCMPEN = "ADCCMPEN"
    BitFieldBaseName_CMPE = "CMPE"
    adchsSym_ADCCMPEN__CMPE = []
    RegisterBaseName_ADCCMP = "ADCCMP"
    BitFieldBaseName_DCMPLO = "DCMPLO"
    BitFieldBaseName_DCMPHI = "DCMPHI"
    adchsComparatorMenu = []
    adchsSym_ADCCMP__DCMPLO = []
    adchsSym_ADCCMP__DCMPHI = []
    RegisterBaseName_ADCCMPCON = "ADCCMPCON"
    BitFieldBaseName_IELOLO = "IELOLO"
    BitFieldBaseName_IELOHI = "IELOHI"
    BitFieldBaseName_IEHILO = "IEHILO"
    BitFieldBaseName_IEHIHI = "IEHIHI"
    BitFieldBaseName_IEBTWN = "IEBTWN"
    BitFieldBaseName_ENDCMP = "ENDCMP"
    BitFieldBaseName_DCMPGIEN = "DCMPGIEN"
    adchsSym_ADCCMPCON__IELOLO = []
    adchsSym_ADCCMPCON__IELOHI = []
    adchsSym_ADCCMPCON__IEHILO = []
    adchsSym_ADCCMPCON__IEHIHI = []
    adchsSym_ADCCMPCON__IEBTWN = []
    adchsSym_ADCCMPCON__ENDCMP = []
    adchsSym_ADCCMPCON__DCMPGIEN = []
    for RegisterNumber in range(0, 6):
        RegisterName = RegisterBaseName_ADCCMPEN + str(RegisterNumber+1)
        adchsComparatorMenu.append(RegisterNumber)
        adchsComparatorMenu[RegisterNumber] = adchsComponent.createBooleanSymbol(
            "COMP"+str(RegisterNumber), adchsComparatorConfigMenu)
        adchsComparatorMenu[RegisterNumber].setLabel("Enable Comparator "+str(RegisterNumber))
        adchsComparatorMenu[RegisterNumber].setDefaultValue(False)

        for signalNum in range(0, 32):
            if (signalNum < ADC_Max_Signals):
                # Log.writeInfoMessage("Signal: "+str(signalNum))
                adchsSym_ADCCMPEN__CMPE.append(signalNum)
                adchsSym_ADCCMPEN__CMPE[signalNum] = adchsAddBooleanFromATDFBitfieldName(
                    adchsComponent, Module, RegisterName, BitFieldBaseName_CMPE +
                    str(signalNum), adchsComparatorMenu[RegisterNumber], False)
                adchsSym_ADCCMPEN__CMPE[signalNum].setDependencies(adchsVisibilityOnEvent,
                    ["COMP"+str(RegisterNumber)])


        RegisterName = RegisterBaseName_ADCCMP + str(RegisterNumber+1)
        adchsSym_ADCCMP__DCMPLO.append(RegisterNumber)
        adchsSym_ADCCMP__DCMPLO[RegisterNumber] = adchsAddLongFromATDFRegisterCaption(
            adchsComponent, Module, RegisterName, BitFieldBaseName_DCMPLO,
            adchsComparatorMenu[RegisterNumber], False)
        adchsSym_ADCCMP__DCMPLO[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])

        adchsSym_ADCCMP__DCMPHI.append(RegisterNumber)
        adchsSym_ADCCMP__DCMPHI[RegisterNumber] = adchsAddLongFromATDFRegisterCaption(
            adchsComponent, Module, RegisterName, BitFieldBaseName_DCMPHI,
            adchsComparatorMenu[RegisterNumber], False)
        adchsSym_ADCCMP__DCMPHI[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])

        RegisterName = RegisterBaseName_ADCCMPCON + str(RegisterNumber+1)
        # IELOLO bitfield
        adchsSym_ADCCMPCON__IELOLO.append(RegisterNumber)
        adchsSym_ADCCMPCON__IELOLO[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_IELOLO,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__IELOLO[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # IELOHI boolean
        adchsSym_ADCCMPCON__IELOHI.append(RegisterNumber)
        adchsSym_ADCCMPCON__IELOHI[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_IELOHI,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__IELOHI[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # IEHILO bitfield
        adchsSym_ADCCMPCON__IEHILO.append(RegisterNumber)
        adchsSym_ADCCMPCON__IEHILO[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_IEHILO,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__IEHILO[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # IEHIHI boolean
        adchsSym_ADCCMPCON__IEHIHI.append(RegisterNumber)
        adchsSym_ADCCMPCON__IEHIHI[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_IEHIHI,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__IEHIHI[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # IEBTWN Boolean
        adchsSym_ADCCMPCON__IEBTWN.append(RegisterNumber)
        adchsSym_ADCCMPCON__IEBTWN[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_IEBTWN,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__IEBTWN[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # ENDCMP bitfield
        adchsSym_ADCCMPCON__ENDCMP.append(RegisterNumber)
        adchsSym_ADCCMPCON__ENDCMP[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_ENDCMP,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__ENDCMP[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])
        # DCMPGIEN bitfield
        adchsSym_ADCCMPCON__DCMPGIEN.append(RegisterNumber)
        adchsSym_ADCCMPCON__DCMPGIEN[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_DCMPGIEN,
            adchsComparatorMenu[RegisterNumber], False))
        adchsSym_ADCCMPCON__DCMPGIEN[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["COMP"+str(RegisterNumber)])

    # Filter Configuration Menu
    adchsFilterConfigMenu = adchsComponent.createMenuSymbol("ADCHS_FILTER_MENU", None)
    adchsFilterConfigMenu.setLabel("ADC Filter Configuration")
    adchsFilterConfigMenu.setVisible(False)
    RegisterBaseName_ADCFLTR = "ADCFLTR"
    BitFieldBaseName_CHNLID = "CHNLID"
    BitFieldBaseName_AFGIEN = "AFGIEN"
    BitFieldBaseName_OVRSAM = "OVRSAM"
    BitFieldBaseName_DFMODE = "DFMODE"
    BitFieldBaseName_DATA16EN = "DATA16EN"
    BitFieldBaseName_AFEN = "AFEN"
    adchsFilterMenu = []
    adchsSym_ADCFLTR__CHNLID = []
    adchsSym_ADCFLTR__AFGIEN = []
    adchsSym_ADCFLTR__OVRSAM = []
    adchsSym_ADCFLTR__DFMODE = []
    adchsSym_ADCFLTR__DATA16EN = []
    adchsSym_ADCFLTR__AFEN = []
    for RegisterNumber in range(0, 6):
        RegisterName = RegisterBaseName_ADCFLTR + str(RegisterNumber+1)
        adchsFilterMenu.append(RegisterNumber)
        adchsFilterMenu[RegisterNumber] = adchsComponent.createBooleanSymbol(
            "FLTR"+str(RegisterNumber), adchsFilterConfigMenu)
        adchsFilterMenu[RegisterNumber].setLabel("Enable Filter "+str(RegisterNumber))
        adchsFilterMenu[RegisterNumber].setDefaultValue(False)
        # CHNLID bitfield
        adchsSym_ADCFLTR__CHNLID.append(RegisterNumber)
        adchsSym_ADCFLTR__CHNLID[RegisterNumber] = (adchsAddKeyValueSetFromATDFInitValue
            (adchsComponent, Module, RegisterName, BitFieldBaseName_CHNLID,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__CHNLID[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])
        # AFGIEN boolean
        adchsSym_ADCFLTR__AFGIEN.append(RegisterNumber)
        adchsSym_ADCFLTR__AFGIEN[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_AFGIEN,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__AFGIEN[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])
        # OVRSAM bitfield
        adchsSym_ADCFLTR__OVRSAM.append(RegisterNumber)
        adchsSym_ADCFLTR__OVRSAM[RegisterNumber] = (adchsAddKeyValueSetFromATDFInitValue
            (adchsComponent, Module, RegisterName, BitFieldBaseName_OVRSAM,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__OVRSAM[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])
        # DFMODE boolean
        adchsSym_ADCFLTR__DFMODE.append(RegisterNumber)
        adchsSym_ADCFLTR__DFMODE[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_DFMODE,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__DFMODE[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])
        # DATA16EN Boolean
        adchsSym_ADCFLTR__DATA16EN.append(RegisterNumber)
        adchsSym_ADCFLTR__DATA16EN[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_DATA16EN,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__DATA16EN[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])
        # AFEN bitfield
        adchsSym_ADCFLTR__AFEN.append(RegisterNumber)
        adchsSym_ADCFLTR__AFEN[RegisterNumber] = (adchsAddBooleanFromATDF1ValueValueGroup
            (adchsComponent, Module, RegisterName, BitFieldBaseName_AFEN,
            adchsFilterMenu[RegisterNumber], False))
        adchsSym_ADCFLTR__AFEN[RegisterNumber].setDependencies(adchsVisibilityOnEvent,
            ["FLTR"+str(RegisterNumber)])

    #Signal Conditioning menu
    adchsSignalConditionMenu = adchsComponent.createMenuSymbol("ADCHS_SIGNAL_CONDITION_CONF", None)
    adchsSignalConditionMenu.setLabel("Analog Signal Configuration")
    RegisterBaseName_ADCIMCON = "ADCIMCON"
    BitFieldBaseName_SIGN = "SIGN"
    BitFieldBaseName_DIFF = "DIFF"
    RegisterBaseName_ADCGIRQEN = "ADCGIRQEN"
    BitFieldBaseName_AGIEN = "AGIEN"
    adchsSym_ADCIMCON__SIGN = []
    adchsSym_ADCIMCON__DIFF = []
    adchsSym_ADCGIRQEN__AGIEN = []
    RegisterBaseName_ADCEIEN = "ADCEIEN"
    BitFieldBaseName_EIEN = "EIEN"
    adchsSym_ADCEIEN__EIEN = []
    adcimcon_deplist = [[] for i in range (3)]

    for signalID in range(0, ADC_Max_Signals):
        global adchsCONMenu
        adchsCONMenu.append(signalID)
        adchsCONMenu[signalID] = adchsComponent.createBooleanSymbol(
            "AN"+str(signalID), adchsSignalConditionMenu)
        adchsCONMenu[signalID].setLabel("Configure Analog Input AN"+str(signalID))

        RegisterName = RegisterBaseName_ADCIMCON + str((signalID/16)+1)
        index = int(((signalID/16)))

        adchsSym_ADCIMCON__SIGN.append(signalID)
        adchsSym_ADCIMCON__SIGN[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_SIGN + str(signalID),
            adchsCONMenu[signalID], False)
        adchsSym_ADCIMCON__SIGN[signalID].setDependencies(adchsVisibilityOnEvent,
            ["AN"+str(signalID)])
        adcimcon_deplist[index].append(RegisterName + "__" + BitFieldBaseName_SIGN + str(signalID))

        adchsSym_ADCIMCON__DIFF.append(signalID)
        adchsSym_ADCIMCON__DIFF[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_DIFF + str(signalID),
            adchsCONMenu[signalID], False)
        adchsSym_ADCIMCON__DIFF[signalID].setDependencies(adchsVisibilityOnEvent,
            ["AN"+str(signalID)])
        adcimcon_deplist[index].append(RegisterName + "__" + BitFieldBaseName_DIFF + str(signalID))

        RegisterName = RegisterBaseName_ADCGIRQEN + str((signalID/32)+1)
        adchsSym_ADCGIRQEN__AGIEN.append(signalID)
        adchsSym_ADCGIRQEN__AGIEN[signalID] = adchsAddBooleanFromATDFBitfieldCaption(
            adchsComponent, Module, RegisterName, BitFieldBaseName_AGIEN + str(signalID),
            adchsCONMenu[signalID], False)
        adchsSym_ADCGIRQEN__AGIEN[signalID].setDependencies(adchsVisibilityOnEvent,
            ["AN"+str(signalID)])
        adcinterruptmode_deplist.append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
        adcgirqen_deplist[int(signalID/32)].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
        if (signalID < (num_intrpt_in_first_iec)):
            adciec_depList[0].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
        elif ((signalID >= (num_intrpt_in_first_iec)) and (signalID < (32 + (num_intrpt_in_first_iec)))):
            adciec_depList[1].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
        else:
            adciec_depList[2].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))

        # RegisterName = RegisterBaseName_ADCEIEN + str((signalID/32)+1)
        # signalName = BitFieldBaseName_EIEN + str(signalID)
        # adchsSym_ADCEIEN__EIEN.append(signalID)
        # adchsSym_ADCEIEN__EIEN[signalID] = adchsAddBooleanFromATDFBitfieldCaption(
        #     adchsComponent, Module, RegisterName, signalName,
        #     adchsCONMenu[signalID], False)
        # adchsSym_ADCEIEN__EIEN[signalID].setDependencies(adchsVisibilityOnEvent,
        #     ["AN"+str(signalID)])

###################################################################################################
########################### Register Values Calculation   #################################
###################################################################################################

    adccon1_deplist = ["ADCCON1__IRQVS", "ADCCON1__SIDL", "ADCCON1__CVDEN", "ADCCON1__FRACT",
    "ADCCON1__SELRES", "ADCCON1__STRGLVL", "ADCCON1__FSSCLKEN", "ADCCON1__FSPBCLKEN"]
    adchsSym_ADCCON1 = adchsComponent.createHexSymbol("ADCHS_ADCCON1", adchsMenu)
    adchsSym_ADCCON1.setLabel("ADCCON1 register value")
    adchsSym_ADCCON1.setVisible(False)
    adchsSym_ADCCON1.setDefaultValue(0x600000)
    adchsSym_ADCCON1.setDependencies(adchsCalcADCCON1, adccon1_deplist)

    adccon2_deplist = ["ADCCON2__CVDCPL", "ADCCON2__ADCDIV", "ADCCON2__SAMC", "ADCCON2__ADCEIS"]
    adchsSym_ADCCON2 = adchsComponent.createHexSymbol("ADCHS_ADCCON2", adchsMenu)
    adchsSym_ADCCON2.setLabel("ADCCON2 register value")
    adchsSym_ADCCON2.setVisible(False)
    adchsSym_ADCCON2.setDefaultValue(0x0)
    adchsSym_ADCCON2.setDependencies(adchsCalcADCCON2, adccon2_deplist)

    adccon3_deplist = ["ADCCON3__VREFSEL", "ADCCON3__CONCLKDIV", "ADCCON3__ADCSEL"]
    adchsSym_ADCCON3 = adchsComponent.createHexSymbol("ADCHS_ADCCON3", adchsMenu)
    adchsSym_ADCCON3.setLabel("ADCCON3 register value")
    adchsSym_ADCCON3.setVisible(False)
    adchsSym_ADCCON3.setDefaultValue(0x0)
    adchsSym_ADCCON3.setDependencies(adchsCalcADCCON3, adccon3_deplist)

    adchsSym_ADCTRGMODE = adchsComponent.createHexSymbol("ADCHS_ADCTRGMODE", None)
    adchsSym_ADCTRGMODE.setLabel("ADCTRGMODE Register")
    adchsSym_ADCTRGMODE.setVisible(False)
    adchsSym_ADCTRGMODE.setDependencies(adchsCalcADCTRGMODE, adctrgmode_deplist)

    adchsSym_ADCIMCON1 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON1", None)
    adchsSym_ADCIMCON1.setLabel("ADCIMCON1 Register")
    adchsSym_ADCIMCON1.setVisible(False)
    adchsSym_ADCIMCON1.setDependencies(adchsCalcADCIMCON1, adcimcon_deplist[0])

    adchsSym_ADCIMCON2 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON2", None)
    adchsSym_ADCIMCON2.setLabel("ADCIMCON2 Register")
    adchsSym_ADCIMCON2.setVisible(False)
    adchsSym_ADCIMCON2.setDependencies(adchsCalcADCIMCON2, adcimcon_deplist[1])

    adchsSym_ADCIMCON3 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON3", None)
    adchsSym_ADCIMCON3.setLabel("ADCIMCON3 Register")
    adchsSym_ADCIMCON3.setVisible(False)
    adchsSym_ADCIMCON3.setDependencies(adchsCalcADCIMCON3, adcimcon_deplist[2])

    adchsSym_ADCTRG1 = adchsComponent.createHexSymbol("ADCHS_ADCTRG1", None)
    adchsSym_ADCTRG1.setLabel("ADCTRG1 Register")
    adchsSym_ADCTRG1.setVisible(False)
    adchsSym_ADCTRG1.setDependencies(adchsCalcADCTRG1, adctrg_deplist[0])

    adchsSym_ADCTRG2 = adchsComponent.createHexSymbol("ADCHS_ADCTRG2", None)
    adchsSym_ADCTRG2.setLabel("ADCTRG2 Register")
    adchsSym_ADCTRG2.setVisible(False)
    adchsSym_ADCTRG2.setDependencies(adchsCalcADCTRG2, adctrg_deplist[1])

    adchsSym_ADCTRG3 = adchsComponent.createHexSymbol("ADCHS_ADCTRG3", None)
    adchsSym_ADCTRG3.setLabel("ADCTRG3 Register")
    adchsSym_ADCTRG3.setVisible(False)
    adchsSym_ADCTRG3.setDependencies(adchsCalcADCTRG3, adctrg_deplist[2])

    adchsSym_ADCTGSNS = adchsComponent.createHexSymbol("ADCHS_ADCTRGSNS", None)
    adchsSym_ADCTGSNS.setLabel("ADCTRGSNS Register")
    adchsSym_ADCTGSNS.setVisible(False)
    adchsSym_ADCTGSNS.setDependencies(adchsCalcADCTRGSNS, adctrgsns_deplist)

    global adchsSym_ADCTIME
    adchsSym_ADCTIME = []
    for module_id in range (0, ADC_Max_Class_1):
        adchsSym_ADCTIME.append(module_id)
        adchsSym_ADCTIME[module_id] = adchsComponent.createHexSymbol("ADCHS_ADCTIME" + str(module_id), None)
        adchsSym_ADCTIME[module_id].setLabel("ADCTIME" + str(module_id))
        adchsSym_ADCTIME[module_id].setVisible(False)
        adchsSym_ADCTIME[module_id].setDependencies(adchsCalcADCTIME, adctime_deplist[module_id])

    adchsSym_ADCGIRQEN1 = adchsComponent.createHexSymbol("ADCHS_ADCGIRQEN1", None)
    adchsSym_ADCGIRQEN1.setLabel("ADCGIRQEN1 Register")
    adchsSym_ADCGIRQEN1.setVisible(False)
    adchsSym_ADCGIRQEN1.setDependencies(adchsCalcADCGIRQEN1, adcgirqen_deplist[0])

    adchsSym_ADCGIRQEN2 = adchsComponent.createHexSymbol("ADCHS_ADCGIRQEN2", None)
    adchsSym_ADCGIRQEN2.setLabel("ADCGIRQEN2 Register")
    adchsSym_ADCGIRQEN2.setVisible(False)
    adchsSym_ADCGIRQEN2.setDependencies(adchsCalcADCGIRQEN2, adcgirqen_deplist[1])

    adchsSym_ADCCSS1 = adchsComponent.createHexSymbol("ADCHS_ADCCSS1", None)
    adchsSym_ADCCSS1.setLabel("ADCCSS1 Register")
    adchsSym_ADCCSS1.setVisible(False)
    adchsSym_ADCCSS1.setDependencies(adchsCalcADCCSS1, adccss_deplist[0])

    adchsSym_ADCCSS2 = adchsComponent.createHexSymbol("ADCHS_ADCCSS2", None)
    adchsSym_ADCCSS2.setLabel("ADCCSS2 Register")
    adchsSym_ADCCSS2.setVisible(False)
    adchsSym_ADCCSS2.setDependencies(adchsCalcADCCSS2, adccss_deplist[1])

###################################################################################################
########################### Interrupts   #################################
###################################################################################################
    adchsSym_IEC0 = adchsComponent.createHexSymbol("ADCHS_IEC0", None)
    adchsSym_IEC0.setLabel("IEC0 Register")
    adchsSym_IEC0.setVisible(False)
    adchsSym_IEC0.setDependencies(adchsCalcIEC0, adciec_depList[0])

    if (ADC_MAX_EIC_REG > 1):
        adchsSym_IEC1 = adchsComponent.createHexSymbol("ADCHS_IEC1", None)
        adchsSym_IEC1.setLabel("IEC1 Register")
        adchsSym_IEC1.setVisible(False)
        adchsSym_IEC1.setDependencies(adchsCalcIEC1, adciec_depList[1])

    if(ADC_MAX_EIC_REG > 2):
        adchsSym_IEC2 = adchsComponent.createHexSymbol("ADCHS_IEC2", None)
        adchsSym_IEC2.setLabel("IEC2 Register")
        adchsSym_IEC2.setVisible(False)
        adchsSym_IEC2.setDependencies(adchsCalcIEC2, adciec_depList[2])

    adchsSym_InterruptMode = adchsComponent.createBooleanSymbol("ADCHS_INTERRUPT", None)
    adchsSym_InterruptMode.setVisible(False)
    adchsSym_InterruptMode.setDependencies(adchsInterruptMode, adcinterruptmode_deplist)

    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    adchs = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]")
    adchsID = adchs.getAttribute("id")

    adchsHeaderFile = adchsComponent.createFileSymbol("ADCHS_HEADER", None)
    adchsHeaderFile.setSourcePath("../peripheral/adchs_02508/templates/plib_adchs.h.ftl")
    adchsHeaderFile.setOutputName("plib_"+Module.lower() + ".h")
    adchsHeaderFile.setDestPath("peripheral/adchs/")
    adchsHeaderFile.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsHeaderFile.setType("HEADER")
    adchsHeaderFile.setMarkup(True)

    adchsGlobalHeaderFile = adchsComponent.createFileSymbol("ADCHS_GLOBALHEADER", None)
    adchsGlobalHeaderFile.setSourcePath("../peripheral/adchs_02508/templates/plib_adchs_common.h.ftl")
    adchsGlobalHeaderFile.setOutputName("plib_adchs_common.h")
    adchsGlobalHeaderFile.setDestPath("peripheral/adchs/")
    adchsGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsGlobalHeaderFile.setType("HEADER")
    adchsGlobalHeaderFile.setMarkup(True)

    adchsSource1File = adchsComponent.createFileSymbol("ADCHS_SOURCE", None)
    adchsSource1File.setSourcePath("../peripheral/adchs_02508/templates/plib_adchs.c.ftl")
    adchsSource1File.setOutputName("plib_"+Module.lower()+".c")
    adchsSource1File.setDestPath("peripheral/adchs/")
    adchsSource1File.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsSource1File.setType("SOURCE")
    adchsSource1File.setMarkup(True)

    adchsSystemInitFile = adchsComponent.createFileSymbol("ADCHS_INIT", None)
    adchsSystemInitFile.setType("STRING")
    adchsSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adchsSystemInitFile.setSourcePath("../peripheral/adchs_02508/templates/system/system_initialize.c.ftl")
    adchsSystemInitFile.setMarkup(True)

    adchsSystemDefFile = adchsComponent.createFileSymbol("ADCHS_DEF", None)
    adchsSystemDefFile.setType("STRING")
    adchsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adchsSystemDefFile.setSourcePath("../peripheral/adchs_02508/templates/system/system_definitions.h.ftl")
    adchsSystemDefFile.setMarkup(True)
