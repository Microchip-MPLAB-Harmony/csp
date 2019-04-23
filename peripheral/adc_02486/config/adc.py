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
import math

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


def adcATDFRegisterPath(ModuleName, RegisterName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]')
    return labelPath

def adcATDFRegisterBitfieldPath(ModuleName, RegisterName, BitfieldName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
        + BitfieldName +'"]')
    return labelPath

def adcATDFValueGroupPath(ModuleName, ValueGroupName):
    value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
        + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
    return value_groupPath

def adcATDFValueGroupValuePath(ModuleName, ValueGroupName, ValueString):
    valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
        + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
        ValueString + '"]')
    return valuePath


# This creates a sub menu based on the caption attribute of a Register in the
# ATDF file.
# Parent is the parent component to the newly created component.  In this case
# it is always adcComponent.
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
def adcAddRegisterSubMenuFromATDF(Parent, ModuleName, RegisterName, ParentMenu):
    # Log.writeInfoMessage("Adding Menu: " + ModuleName + "_MENU_" + RegisterName)
    labelPath = adcATDFRegisterPath(ModuleName, RegisterName)
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
# it is always adcComponent.
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
def adcAddKeyValueSetFromATDFInitValue(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding KeyValueSet" + ModuleName + " " + RegisterName
        # + " " + BitFieldName)
    registerPath = adcATDFRegisterPath(ModuleName, RegisterName)
    registerNode = ATDF.getNode(registerPath)
    if registerNode is not None:
        labelPath = adcATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            value_groupPath = adcATDFValueGroupPath(ModuleName, RegisterName
                + '__' + BitFieldName)
            value_groupNode = ATDF.getNode(value_groupPath)
            if value_groupNode is not None:
                Component = Parent.createKeyValueSetSymbol(RegisterName + '__' +
                    BitFieldName, Menu)
                adcValGrp_names = []
                _get_bitfield_names(value_groupNode, adcValGrp_names)

                Component.setLabel(labelNode.getAttribute('caption'))
                Component.setOutputMode("Value")
                Component.setDisplayMode("Description")

                initval = registerNode.getAttribute('initval')
                if initval is not None:
                    defaultValue = _find_default_value(labelNode, initval)
                    #first add the key which has default value to ensure two things:
                    #1. the key with default value doesn't get missed out from symbol due to duplication of keys in ATDF
                    #2. index of the default key is always 0, so it becomes easier to assign default value later.
                    for ii in adcValGrp_names:
                        if int(ii['value']) == defaultValue:
                            Component.addKey( ii['desc'], ii['value'], ii['key'] )
                            break
                    #add rest of the keys
                    for ii in adcValGrp_names:
                        Component.addKey( ii['desc'], ii['value'], ii['key'] )

                else:
                #if initval is not present in ATDF, add all the keys sequentially
                    for ii in adcValGrp_names:
                        Component.addKey( ii['desc'], ii['value'], ii['key'] )

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
# it is always adcComponent.
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
def adcAddBooleanFromATDF1ValueValueGroup(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    value_groupPath = adcATDFValueGroupValuePath(ModuleName, RegisterName
        + '__' + BitFieldName, "0x1")
    labelNode = ATDF.getNode(value_groupPath)
    if labelNode is not None:
        Component = Parent.createBooleanSymbol(RegisterName + '__' + BitFieldName, Menu)
        Component.setLabel(labelNode.getAttribute('caption'))
        Component.setDefaultValue(0)
        Component.setVisible(Visibility)
        return Component
    else:
        #Log.writeErrorMessage("Adding Boolean: Failed!! no such node. " + value_groupPath)
        return None

def adcAddBooleanFromATDFBitfieldName(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adcATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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

def adcAddBooleanFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adcATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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
# it is always adcComponent.
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
def adcAddLongFromATDFRegisterCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adcATDFRegisterPath(ModuleName, RegisterName)
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

def adcAddLongFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = adcATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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

###################################################################################################
########################### Callback Functions   #################################
###################################################################################################

# Meant to be used as a dependency callback so that a sub element of a boolean
# symbol can become visible when the boolean becomes true.
def adcVisibilityOnEvent(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def MuxA_PositiveInputsVisibility(symbol, event):
    if (event["value"] == False):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def adcClkDividorVisibility(symbol, event):
    if (event["value"] == 0):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def autoSampleTimeVisibility(symbol, event):
    if (event["value"] == 4):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def MuxB_InputsVisibility(symbol, event):
    if (event["value"] == 1):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


#AD1CON1 register value
def adcCalcAD1CON1(symbol, event):
    global adcSym_AD1CON1__SSRC
    global adcSym_AD1CON1__FORM
    global adcSym_AD1CON1__SIDL
    ad1con1 = 0x0
    component = symbol.getComponent()
    asam = component.getSymbolValue("AD1CON1__ASAM") << 2
    clrasam = component.getSymbolValue("AD1CON1__CLRASAM") << 4
    ssrc = int(adcSym_AD1CON1__SSRC.getKeyValue(adcSym_AD1CON1__SSRC.getValue())) << 5
    form = int(adcSym_AD1CON1__FORM.getKeyValue(adcSym_AD1CON1__FORM.getValue())) << 8
    sidl = int(adcSym_AD1CON1__SIDL.getKeyValue(adcSym_AD1CON1__SIDL.getValue())) << 13
    ad1con1 = asam + clrasam + ssrc + form + sidl
    symbol.setValue(ad1con1, 2)

def adcCalcAD1CON2(symbol, event):
    global adcSym_AD1CON2__ALTS
    global adcSym_AD1CON2__BUFM
    global adcSym_AD1CON2__SMPI
    global adcSym_AD1CON2__CSCNA
    global adcSym_AD1CON2__VCFG
    ad1con2 = 0x0

    component = symbol.getComponent()
    alts = int(adcSym_AD1CON2__ALTS.getKeyValue(adcSym_AD1CON2__ALTS.getValue())) << 0
    bufm = int(adcSym_AD1CON2__BUFM.getKeyValue(adcSym_AD1CON2__BUFM.getValue())) << 1
    smpi = int(adcSym_AD1CON2__SMPI.getKeyValue(adcSym_AD1CON2__SMPI.getValue())) << 2
    cscna = adcSym_AD1CON2__CSCNA.getValue() << 10
    vcfg = int(adcSym_AD1CON2__VCFG.getKeyValue(adcSym_AD1CON2__VCFG.getValue())) << 13
    ad1con2 = alts + bufm + smpi + cscna + vcfg
    symbol.setValue(ad1con2, 2)

def adcCalcAD1CON3(symbol, event):
    global adcSym_AD1CON3__ADRC
    ad1con3 = 0x0

    component = symbol.getComponent()
    adcs = component.getSymbolValue("AD1CON3__ADCS") << 0
    samc = component.getSymbolValue("AD1CON3__SAMC") << 8
    adrc = int(adcSym_AD1CON3__ADRC.getKeyValue(adcSym_AD1CON3__ADRC.getValue())) << 15
    ad1con3 = adcs + samc + adrc
    symbol.setValue(ad1con3, 2)

def adcCalcAD1CHS(symbol, event):
    global adcSym_AD1CHS__CH0SA
    global adcSym_AD1CHS__CH0NA
    global adcSym_AD1CHS__CH0SB
    global adcSym_AD1CHS__CH0NB
    ad1chs = 0x0

    component = symbol.getComponent()
    ch0sa = int(adcSym_AD1CHS__CH0SA.getKeyValue(adcSym_AD1CHS__CH0SA.getValue())) << 16
    ch0na = int(adcSym_AD1CHS__CH0NA.getKeyValue(adcSym_AD1CHS__CH0NA.getValue())) << 23
    ch0sb = int(adcSym_AD1CHS__CH0SB.getKeyValue(adcSym_AD1CHS__CH0SB.getValue())) << 24
    ch0nb = int(adcSym_AD1CHS__CH0NB.getKeyValue(adcSym_AD1CHS__CH0NB.getValue())) << 31
    ad1chs = ch0sa + ch0na + ch0sb + ch0nb
    symbol.setValue(ad1chs, 2)

def adcCalcAD1CSSL(symbol, event):
    ad1cssl = symbol.getValue()

    component = symbol.getComponent()
    scanPinNumber = event["id"].split("__CSSL_")[1]
    csslMask = component.getSymbolValue("AD1CSSL__CSSL_ENUM_VALUE_" + scanPinNumber)
    if event["value"] == True:
        ad1cssl = ad1cssl + csslMask
    else:
        ad1cssl = ad1cssl & (~csslMask)
    symbol.setValue(ad1cssl, 2)

def adcCalcAD1CSSL2(symbol, event):
    ad1cssl2 = symbol.getValue()

    component = symbol.getComponent()
    scanPinNumber = event["id"].split("__CSSL_")[1]
    csslMask = component.getSymbolValue("AD1CSSL__CSSL_ENUM_VALUE_" + scanPinNumber)
    if event["value"] == True:
        ad1cssl2 = ad1cssl2 + csslMask
    else:
        ad1cssl2 = ad1cssl2 & (~csslMask)

    symbol.setValue(ad1cssl2, 2)

def getTCLKValue():
    # "ADC_CLOCK_FREQUENCY" will give PB Clock frequency from clock PLIB
    clk_freq = Database.getSymbolValue("core", "ADC_CLOCK_FREQUENCY")
    dividor = Database.getSymbolValue(adcInstanceName.getValue().lower(), "AD1CON3__ADCS")
    if (clk_freq == 0):
        Log.writeErrorMessage("Peripheral Clock Frequency should not be 0")
        clk_freq = 40000000
    return float((dividor * 1000000000)/clk_freq)

def adcTCLKCalc(symbol, event):
    if Database.getSymbolValue(adcInstanceName.getValue().lower(), "AD1CON3__ADRC") == 1:
        # it means ADC source clock is FRC/2, so TAD = 250ns
        symbol.setValue(250, 2)
    else:
        symbol.setValue(getTCLKValue(), 2)

def adcInterruptControl(adcInterrupt, event):
    Database.setSymbolValue("core", "ADC_INTERRUPT_ENABLE", event["value"], 1)
    Database.setSymbolValue("core", "ADC_INTERRUPT_HANDLER_LOCK", event["value"], 1)

    if event["value"] == True:
        Database.setSymbolValue("core", "ADC_INTERRUPT_HANDLER", "ADC_InterruptHandler", 1)
    else :
        Database.setSymbolValue("core", "ADC_INTERRUPT_HANDLER", "ADC_Handler", 1)

# Dependency Function to show or hide the warning message depending on Interrupt
def InterruptStatusWarning(symbol, event):
    global adcSym_InterruptMode
    if adcSym_InterruptMode.getValue() == True and Database.getSymbolValue("core", "ADC_INTERRUPT_ENABLE_UPDATE") == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateADCClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(adcComponent):
    global adcInstanceName

    adcInstanceName = adcComponent.createStringSymbol("ADC_INSTANCE_NAME", None)
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    Module = adcInstanceName.getValue()
    Log.writeInfoMessage("Running " + Module)

    #Clock enable
    Database.setSymbolValue("core", adcInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

################################################################################
########## ADC Menu ################################################
########################################################################
    adcMenu = adcComponent.createMenuSymbol("ADC_MENU", None)
    adcMenu.setLabel("ADC Configuration")

    global adcSym_InterruptMode
    adcSym_InterruptMode = adcComponent.createBooleanSymbol("ADC_INTERRUPT", adcMenu)
    adcSym_InterruptMode.setLabel("Interrupt Mode")
    adcSym_InterruptMode.setVisible(True)
    adcSym_InterruptMode.setDefaultValue(False)
    adcSym_InterruptMode.setDependencies(adcInterruptControl, ["ADC_INTERRUPT"])

    global adcSym_AD1CON3__ADRC
    adcSym_AD1CON3__ADRC = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON3", "ADRC", adcMenu, True)

    adcSym_AD1CON3__ADCS = adcComponent.createIntegerSymbol("AD1CON3__ADCS", adcSym_AD1CON3__ADRC)
    adcSym_AD1CON3__ADCS.setDefaultValue(2)
    adcSym_AD1CON3__ADCS.setLabel("Select Clock Divider")
    adcSym_AD1CON3__ADCS.setMin(2)
    adcSym_AD1CON3__ADCS.setMax(512)
    adcSym_AD1CON3__ADCS.setVisible(True)
    adcSym_AD1CON3__ADCS.setDependencies(adcClkDividorVisibility, [adcSym_AD1CON3__ADRC.getID()])

    adcSym_TCLK = adcComponent.createFloatSymbol("ADC_TCLK", adcMenu)
    adcSym_TCLK.setLabel("ADC Clock (TAD) (nano sec)")
    adcSym_TCLK.setDefaultValue(getTCLKValue())
    adcSym_TCLK.setReadOnly(True)
    adcSym_TCLK.setDependencies(adcTCLKCalc, ["core.ADC_CLOCK_FREQUENCY", "AD1CON3__ADRC", "AD1CON3__ADCS"])

    global adcSym_AD1CON2__VCFG
    adcSym_AD1CON2__VCFG = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON2", "VCFG", adcMenu, True)
    global adcSym_AD1CON1__SIDL
    adcSym_AD1CON1__SIDL = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON1", "SIDL", adcMenu, True)

    #adcSamplingMenu = adcComponent.createMenuSymbol("ADC_SAMPLING_MENU", adcMenu)
    #adcSamplingMenu.setLabel("ADC Sampling Menu")

    global adcSym_AD1CON2__ALTS
    adcSym_AD1CON2__ALTS = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON2", "ALTS", adcMenu, True)

    global adcSym_AD1CON2__CSCNA
    adcSym_AD1CON2__CSCNA = adcComponent.createBooleanSymbol("AD1CON2__CSCNA", adcMenu)
    adcSym_AD1CON2__CSCNA.setLabel("Enable Input Scan on Mux A")
    adcSym_AD1CON2__CSCNA.setDefaultValue(False)

    adcSym_AD1CSSL__CSSL = []
    adcSym_AD1CSSL__CSSL_EnumName = []
    adcSym_AD1CSSL__CSSL_EnumValue = []
    adcSym_AD1CHS__CH0SA_EnumName = []
    adcSym_AD1CHS__CH0SA_EnumValue = []
    adcSym_AD1CHS__CH0NA_EnumName = []
    adcSym_AD1CHS__CH0NA_EnumValue = []

    ad1cssl_deplist = []
    ad1cssl2_deplist = []
    ADC_ScanInputCount = 0
    ADC_PositiveInputCount = 0
    ADC_NegativeInputCount = 0

    adcValueGroupNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADC\"]")
    for myValueGroup in adcValueGroupNode.getChildrenByName('value-group'):
        valueGroupName = myValueGroup.getAttribute("name")
        if "AD1CSSL" in valueGroupName:
            csslDescription = myValueGroup.getAttribute("caption")
            csslPinName = csslDescription.split(" ")[0]
            csslPinNumber = int(valueGroupName.split("__CSSL")[1])
            adcSym_AD1CSSL__CSSL.append(ADC_ScanInputCount)
            adcSym_AD1CSSL__CSSL[ADC_ScanInputCount] = adcComponent.createBooleanSymbol("AD1CSSL__CSSL_" + str(ADC_ScanInputCount), adcSym_AD1CON2__CSCNA)
            adcSym_AD1CSSL__CSSL[ADC_ScanInputCount].setLabel("Select " + csslPinName + " for Input Scan")
            adcSym_AD1CSSL__CSSL[ADC_ScanInputCount].setDefaultValue(False)
            adcSym_AD1CSSL__CSSL[ADC_ScanInputCount].setVisible(False)
            adcSym_AD1CSSL__CSSL[ADC_ScanInputCount].setDependencies(adcVisibilityOnEvent, ["AD1CON2__CSCNA"])

            # symbol for enum name to be used in ftl
            adcSym_AD1CSSL__CSSL_EnumName.append(ADC_ScanInputCount)
            adcSym_AD1CSSL__CSSL_EnumName[ADC_ScanInputCount] = adcComponent.createStringSymbol("AD1CSSL__CSSL_ENUM_NAME_" + str(ADC_ScanInputCount), adcSym_AD1CON2__CSCNA)
            adcSym_AD1CSSL__CSSL_EnumName[ADC_ScanInputCount].setDefaultValue(csslPinName)
            adcSym_AD1CSSL__CSSL_EnumName[ADC_ScanInputCount].setVisible(False)

            # symbol for enum value to be used in ftl
            adcSym_AD1CSSL__CSSL_EnumValue.append(ADC_ScanInputCount)
            adcSym_AD1CSSL__CSSL_EnumValue[ADC_ScanInputCount] = adcComponent.createHexSymbol("AD1CSSL__CSSL_ENUM_VALUE_" + str(ADC_ScanInputCount), adcSym_AD1CON2__CSCNA)
            adcSym_AD1CSSL__CSSL_EnumValue[ADC_ScanInputCount].setDefaultValue(1 << (csslPinNumber % 32))
            adcSym_AD1CSSL__CSSL_EnumValue[ADC_ScanInputCount].setVisible(False)

            #list created only for dependency
            if ADC_ScanInputCount < 32:
                ad1cssl_deplist.append("AD1CSSL__CSSL_" + str(ADC_ScanInputCount))
            else:
                ad1cssl2_deplist.append("AD1CSSL__CSSL_" + str(ADC_ScanInputCount))

            ADC_ScanInputCount = ADC_ScanInputCount+1

        elif valueGroupName == "AD1CHS__CH0SA":
            for CH0SA_values in myValueGroup.getChildrenByName("value"):
                CH0SA_PinName = CH0SA_values.getAttribute("name")
                if CH0SA_PinName.lower() in ["reserved", ""]:
                    continue
                CH0SA_PinNumber = int(CH0SA_values.getAttribute("value")[2:], 16)

                # symbol for enum name to be used in ftl
                adcSym_AD1CHS__CH0SA_EnumName.append(ADC_PositiveInputCount)
                adcSym_AD1CHS__CH0SA_EnumName[ADC_PositiveInputCount] = adcComponent.createStringSymbol("AD1CHS__CH0SA_ENUM_NAME_" + str(ADC_PositiveInputCount), adcMenu)
                adcSym_AD1CHS__CH0SA_EnumName[ADC_PositiveInputCount].setDefaultValue(CH0SA_PinName)
                adcSym_AD1CHS__CH0SA_EnumName[ADC_PositiveInputCount].setVisible(False)

                # symbol for enum value to be used in ftl
                adcSym_AD1CHS__CH0SA_EnumValue.append(ADC_PositiveInputCount)
                adcSym_AD1CHS__CH0SA_EnumValue[ADC_PositiveInputCount] = adcComponent.createIntegerSymbol("AD1CHS__CH0SA_ENUM_VALUE_" + str(ADC_PositiveInputCount), adcMenu)
                adcSym_AD1CHS__CH0SA_EnumValue[ADC_PositiveInputCount].setDefaultValue(CH0SA_PinNumber)
                adcSym_AD1CHS__CH0SA_EnumValue[ADC_PositiveInputCount].setVisible(False)

                ADC_PositiveInputCount = ADC_PositiveInputCount+1

        elif valueGroupName == "AD1CHS__CH0NA":
            for CH0NA_values in myValueGroup.getChildrenByName("value"):
                CH0NA_PinName = CH0NA_values.getAttribute("name")
                CH0NA_PinNumber = int(CH0NA_values.getAttribute("value")[2:], 16)

                # symbol for enum name to be used in ftl
                adcSym_AD1CHS__CH0NA_EnumName.append(ADC_NegativeInputCount)
                adcSym_AD1CHS__CH0NA_EnumName[ADC_NegativeInputCount] = adcComponent.createStringSymbol("AD1CHS__CH0NA_ENUM_NAME_" + str(ADC_NegativeInputCount), adcMenu)
                adcSym_AD1CHS__CH0NA_EnumName[ADC_NegativeInputCount].setDefaultValue(CH0NA_PinName)
                adcSym_AD1CHS__CH0NA_EnumName[ADC_NegativeInputCount].setVisible(False)

                # symbol for enum value to be used in ftl
                adcSym_AD1CHS__CH0NA_EnumValue.append(ADC_NegativeInputCount)
                adcSym_AD1CHS__CH0NA_EnumValue[ADC_NegativeInputCount] = adcComponent.createIntegerSymbol("AD1CHS__CH0NA_ENUM_VALUE_" + str(ADC_NegativeInputCount), adcMenu)
                adcSym_AD1CHS__CH0NA_EnumValue[ADC_NegativeInputCount].setDefaultValue(CH0NA_PinNumber)
                adcSym_AD1CHS__CH0NA_EnumValue[ADC_NegativeInputCount].setVisible(False)

                ADC_NegativeInputCount = ADC_NegativeInputCount+1
    # symbols to be used in ftl
    adcSym_AD1CSSL__CSSL_Count = adcComponent.createIntegerSymbol("AD1CSSL__CSSL_COUNT", adcSym_AD1CON2__CSCNA)
    adcSym_AD1CSSL__CSSL_Count.setDefaultValue(ADC_ScanInputCount)
    adcSym_AD1CSSL__CSSL_Count.setVisible(False)

    adcSym_AD1CHS__CH0SA_Count = adcComponent.createIntegerSymbol("AD1CHS__CH0SA_COUNT", adcSym_AD1CON2__CSCNA)
    adcSym_AD1CHS__CH0SA_Count.setDefaultValue(ADC_PositiveInputCount)
    adcSym_AD1CHS__CH0SA_Count.setVisible(False)

    adcSym_AD1CHS__CH0NA_Count = adcComponent.createIntegerSymbol("AD1CHS__CH0NA_COUNT", adcSym_AD1CON2__CSCNA)
    adcSym_AD1CHS__CH0NA_Count.setDefaultValue(ADC_NegativeInputCount)
    adcSym_AD1CHS__CH0NA_Count.setVisible(False)

    # ADC menu items
    global adcSym_AD1CHS__CH0NA
    adcSym_AD1CHS__CH0NA = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CHS", "CH0NA", adcMenu, True)

    global adcSym_AD1CHS__CH0SA
    adcSym_AD1CHS__CH0SA = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CHS", "CH0SA", adcMenu, True)
    adcSym_AD1CHS__CH0SA.setDependencies(MuxA_PositiveInputsVisibility, ["AD1CON2__CSCNA"])

    global adcSym_AD1CHS__CH0NB
    adcSym_AD1CHS__CH0NB = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CHS", "CH0NB", adcMenu, False)
    adcSym_AD1CHS__CH0NB.setDependencies(MuxB_InputsVisibility, ["AD1CON2__ALTS"])

    global adcSym_AD1CHS__CH0SB
    adcSym_AD1CHS__CH0SB = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CHS", "CH0SB", adcMenu, False)
    adcSym_AD1CHS__CH0SB.setDependencies(MuxB_InputsVisibility, ["AD1CON2__ALTS"])

    adcSym_AD1CON1__ASAM = adcComponent.createBooleanSymbol("AD1CON1__ASAM", adcMenu)
    adcSym_AD1CON1__ASAM.setLabel("Enable Auto Sampling")
    adcSym_AD1CON1__ASAM.setDescription("Sampling begins immediately after last conversion completes")
    adcSym_AD1CON1__ASAM.setDefaultValue(False)

    adcSym_AD1CON1__CLRASAM = adcComponent.createBooleanSymbol("AD1CON1__CLRASAM", adcSym_AD1CON1__ASAM)
    adcSym_AD1CON1__CLRASAM.setLabel("Stop Auto Sampling After First Conversion Sequence")
    adcSym_AD1CON1__CLRASAM.setDescription("If enabled, auto sampling will be stopped once first ADC interrupt is generated.\
                                              If disabled, normal operation will occur and ADC buffers will be overwritten \
                                              by next conversion sequence.")
    adcSym_AD1CON1__CLRASAM.setDefaultValue(False)
    adcSym_AD1CON1__CLRASAM.setVisible(False)
    adcSym_AD1CON1__CLRASAM.setDependencies(adcVisibilityOnEvent, ["AD1CON1__ASAM"])

    global adcSym_AD1CON1__SSRC
    adcSym_AD1CON1__SSRC = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON1", "SSRC", adcMenu, True)

    adcSym_AD1CON3__SAMC = adcComponent.createIntegerSymbol("AD1CON3__SAMC", adcSym_AD1CON1__SSRC)
    adcSym_AD1CON3__SAMC.setDefaultValue(31)
    adcSym_AD1CON3__SAMC.setLabel("Auto Sample Time (nTAD)")
    adcSym_AD1CON3__SAMC.setMin(1)
    adcSym_AD1CON3__SAMC.setMax(31)
    adcSym_AD1CON3__SAMC.setVisible(False)
    adcSym_AD1CON3__SAMC.setDependencies(autoSampleTimeVisibility, ["AD1CON1__SSRC"])

    global adcSym_AD1CON1__FORM
    adcSym_AD1CON1__FORM = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON1", "FORM", adcMenu, True)
    global adcSym_AD1CON2__BUFM
    adcSym_AD1CON2__BUFM = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON2", "BUFM", adcMenu, True)
    global adcSym_AD1CON2__SMPI
    adcSym_AD1CON2__SMPI = adcAddKeyValueSetFromATDFInitValue(adcComponent, Module, "AD1CON2", "SMPI", adcMenu, True)

    #adcConversionMenu = adcComponent.createMenuSymbol("ADC_CONVERSION_MENU", adcMenu)
    #adcConversionMenu.setLabel("ADC Conversion Menu")

###################################################################################################
########################### Register Values Calculation   #################################
###################################################################################################

    ad1con1_deplist = ["AD1CON1__ASAM", "AD1CON1__CLRASAM", "AD1CON1__SSRC", "AD1CON1__FORM", "AD1CON1__SIDL"]
    adcSym_AD1CON1 = adcComponent.createHexSymbol("ADC_AD1CON1", adcMenu)
    adcSym_AD1CON1.setLabel("AD1CON1 register value")
    adcSym_AD1CON1.setVisible(False)
    adcSym_AD1CON1.setDefaultValue(0x0)
    adcSym_AD1CON1.setDependencies(adcCalcAD1CON1, ad1con1_deplist)

    ad1con2_deplist = ["AD1CON2__ALTS", "AD1CON2__BUFM", "AD1CON2__SMPI", "AD1CON2__CSCNA", "AD1CON2__VCFG"]
    adcSym_AD1CON2 = adcComponent.createHexSymbol("ADC_AD1CON2", adcMenu)
    adcSym_AD1CON2.setLabel("AD1CON2 register value")
    adcSym_AD1CON2.setVisible(False)
    adcSym_AD1CON2.setDefaultValue(0x0)
    adcSym_AD1CON2.setDependencies(adcCalcAD1CON2, ad1con2_deplist)

    ad1con3_deplist = ["AD1CON3__ADCS", "AD1CON3__SAMC", "AD1CON3__ADRC"]
    adcSym_AD1CON3 = adcComponent.createHexSymbol("ADC_AD1CON3", adcMenu)
    adcSym_AD1CON3.setLabel("AD1CON3 register value")
    adcSym_AD1CON3.setVisible(False)
    adcSym_AD1CON3.setDefaultValue(0x0)
    adcSym_AD1CON3.setDependencies(adcCalcAD1CON3, ad1con3_deplist)

    ad1chs_deplist = ["AD1CHS__CH0SA", "AD1CHS__CH0NA", "AD1CHS__CH0SB", "AD1CHS__CH0NB"]
    adcSym_AD1CHS = adcComponent.createHexSymbol("ADC_AD1CHS", None)
    adcSym_AD1CHS.setLabel("AD1CHS Register")
    adcSym_AD1CHS.setVisible(False)
    adcSym_AD1CHS.setDefaultValue(0x0)
    adcSym_AD1CHS.setDependencies(adcCalcAD1CHS, ad1chs_deplist)

    adcSym_AD1CSSL = adcComponent.createHexSymbol("ADC_AD1CSSL", None)
    adcSym_AD1CSSL.setLabel("AD1CSSL Register")
    adcSym_AD1CSSL.setVisible(False)
    adcSym_AD1CSSL.setDefaultValue(0x0)
    adcSym_AD1CSSL.setDependencies(adcCalcAD1CSSL, ad1cssl_deplist)

    if(ADC_ScanInputCount > 32):
        adcSym_AD1CSSL2 = adcComponent.createHexSymbol("ADC_AD1CSSL2", None)
        adcSym_AD1CSSL2.setLabel("AD1CSSL2 Register")
        adcSym_AD1CSSL2.setVisible(False)
        adcSym_AD1CSSL2.setDefaultValue(0x0)
        adcSym_AD1CSSL2.setDependencies(adcCalcAD1CSSL2, ad1cssl2_deplist)

###################################################################################################
########################### Interrupts   #################################
###################################################################################################
    interruptsChildrenList = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
    for interrupt in range (0, len(interruptsChildrenList)):
        vName = str(interruptsChildrenList[interrupt].getAttribute("name"))
        if "ADC" in vName:
            irqNumber = int(interruptsChildrenList[interrupt].getAttribute("irq-index"))
            break

    # This symbol gives which IFS/IEC register should be used for interrupt handling.
    adcSym_IFS_RegIndex = adcComponent.createStringSymbol("ADC_IFS_REG_INDEX", adcMenu)
    adcSym_IFS_RegIndex.setLabel("IFS/IEC Register Index")
    adcSym_IFS_RegIndex.setDefaultValue(str((int(irqNumber))/32))
    adcSym_IFS_RegIndex.setReadOnly(True)
    adcSym_IFS_RegIndex.setVisible(False)

    # Dependency Status for interrupt
    adcSymIntEnComment = adcComponent.createCommentSymbol("ADC_EVIC_ENABLE_COMMENT", adcMenu)
    adcSymIntEnComment.setVisible(False)
    adcSymIntEnComment.setLabel("Warning!!! ADC Interrupt is Disabled in Interrupt Manager")
    adcSymIntEnComment.setDependencies(InterruptStatusWarning, ["core.ADC_INTERRUPT_ENABLE_UPDATE", "ADC_INTERRUPT"])

###################################################################################################

    # Clock Warning status
    adcSym_ClkEnComment = adcComponent.createCommentSymbol("ADC_CLOCK_ENABLE_COMMENT", None)
    adcSym_ClkEnComment.setLabel("Warning!!! " + adcInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    adcSym_ClkEnComment.setVisible(False)
    adcSym_ClkEnComment.setDependencies(updateADCClockWarningStatus, ["core." + adcInstanceName.getValue() + "_CLOCK_ENABLE"])


    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    adcHeaderFile = adcComponent.createFileSymbol("ADC_HEADER", None)
    adcHeaderFile.setSourcePath("../peripheral/adc_02486/templates/plib_adc.h.ftl")
    adcHeaderFile.setOutputName("plib_"+Module.lower() + ".h")
    adcHeaderFile.setDestPath("peripheral/adc/")
    adcHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcHeaderFile.setType("HEADER")
    adcHeaderFile.setMarkup(True)

    adcSource1File = adcComponent.createFileSymbol("ADC_SOURCE", None)
    adcSource1File.setSourcePath("../peripheral/adc_02486/templates/plib_adc.c.ftl")
    adcSource1File.setOutputName("plib_"+Module.lower()+".c")
    adcSource1File.setDestPath("peripheral/adc/")
    adcSource1File.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcSource1File.setType("SOURCE")
    adcSource1File.setMarkup(True)

    adcSystemInitFile = adcComponent.createFileSymbol("ADC_INIT", None)
    adcSystemInitFile.setType("STRING")
    adcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adcSystemInitFile.setSourcePath("../peripheral/adc_02486/templates/system/initialization.c.ftl")
    adcSystemInitFile.setMarkup(True)

    adcSystemDefFile = adcComponent.createFileSymbol("ADC_DEF", None)
    adcSystemDefFile.setType("STRING")
    adcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adcSystemDefFile.setSourcePath("../peripheral/adc_02486/templates/system/definitions.h.ftl")
    adcSystemDefFile.setMarkup(True)

 #   adcComponent.addPlugin("../peripheral/adc_02486/plugin/adc_02486.jar")
