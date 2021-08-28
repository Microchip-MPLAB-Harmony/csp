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
########################### Global variables   #################################
###################################################################################################

global adchsInstanceName
global adchsSym_ADCTRGMODE__SHxALT
global isDMAFeatureAvailable
# A set of arrays for keeping track of each chanel's parameters.
adchsCHMenu = []
adchsCONMenu = [None] * 64
adchsSym_CH_ENABLE = []
adchsSym_CH_NAME = []

OversamplingModeDescription = [
{"0x7" : "(If DFMODE is 0) 128 samples (shift sum 3 bits to right output data is in 15.1 format) / (If DFMODE is 1) 256 samples (256 samples to be averaged)"},
{"0x6" : "(If DFMODE is 0) 32 samples (shift sum 2 bits to right output data is in 14.1 format) / (If DFMODE is 1) 128 samples (128 samples to be averaged)"},
{"0x5" : "(If DFMODE is 0) 8 samples (shift sum 1 bit to right output data is in 13.1 format) / (If DFMODE is 1) 64 samples (64 samples to be averaged)"},
{"0x4" : "(If DFMODE is 0) 2 samples (shift sum 0 bits to right output data is in 12.1 format) / (If DFMODE is 1) 32 samples (32 samples to be averaged)"},
{"0x3" : "(If DFMODE is 0) 256 samples (shift sum 4 bits to right output data is 16 bits) / (If DFMODE is 1) 16 samples (16 samples to be averaged)"},
{"0x2" : "(If DFMODE is 0) 64 samples (shift sum 3 bits to right output data is 15 bits) / (If DFMODE is 1) 8 samples (8 samples to be averaged)"},
{"0x1" : "(If DFMODE is 0) 16 samples (shift sum 2 bits to right output data is 14 bits) / (If DFMODE is 1) 4 samples (4 samples to be averaged)"},
{"0x0" : "(If DFMODE is 0) 4 samples (shift sum 1 bit to right output data is 13 bits) / (If DFMODE is 1) 2 samples (2 samples to be averaged)"}]

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
                    valuenode = value_groupNode.getChildren()  # look at all the <value ..> entries underneath <value-group >
                    Component.setDefaultValue(_find_default_value(labelNode, initval))
                else:
                    Component.setDefaultValue(0)

                Component.setVisible(Visibility)
                return Component

            else:
                Log.writeInfoMessage("Adding KeyValueSet: no such node. " + value_groupPath)
        else:
            Log.writeInfoMessage("Adding KeyValueSet: no such node. " + labelPath)
    else:
        Log.writeInfoMessage("Adding KeyValueSet: no such node. " + registerPath)

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
        #Log.writeErrorMessage("Adding Boolean: Failed!! no such node. " + value_groupPath)
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
        Log.writeInfoMessage("Adding Boolean: no such node. " + labelPath)
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
    irq_index = 0
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
global ADC_EVSYSTrigEnd
global ADC_EVSYSTrigStart
global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock = []
global InterruptVectorUpdate
InterruptVectorUpdate = []

def updateADCHSClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

def adchsEvsys(symbol, event):
    global adcEvsys_deplist
    component = symbol.getComponent()
    for trig in range (ADC_EVSYSTrigStart, ADC_EVSYSTrigEnd+1):
        key = "ADC_TRIG_" + str(trig)
        if (Database.getSymbolValue("evsys", "USER_" + key + "_READY") != False):
            Database.setSymbolValue("evsys", "USER_" + key + "_READY", False)
    for channelID in range (0, len(adcEvsys_deplist)):
        val = component.getSymbolValue(adcEvsys_deplist[channelID])
        if (adcEvsys_deplist[channelID] == "ADCCON1__STRGSRC"):
            val =  int(adchsSym_ADCCON1__STRGSRC.getSelectedValue())
        if ( val >= ADC_EVSYSTrigStart) and (val <= ADC_EVSYSTrigEnd):
            key = "ADC_TRIG_" + str(val)
            Database.setSymbolValue("evsys", "USER_" + key + "_READY", True)

# Meant to be used as a dependancy callback so that a sub element of a boolean
# symbol can become visible when the boolean becomes true.
def adchsVisibilityOnEvent(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

#ADCCON1 register value
def adchsCalcADCCON1(symbol, event):
    global isDMAFeatureAvailable
    global adchsSym_ADCCON1__STRGSRC
    adccon1 = 0x0
    dmabl = 0
    component = symbol.getComponent()
    fract = component.getSymbolValue("ADCCON1__FRACT") << 23
    slres = component.getSymbolValue("ADCCON1__SELRES") << 21
    strgsrc = int(adchsSym_ADCCON1__STRGSRC.getSelectedValue()) << 16
    sidl = component.getSymbolValue("ADCCON1__SIDL") << 13
    if isDMAFeatureAvailable == True:
        dmabl = int(component.getSymbolByID("ADCCON1__DMABL").getSelectedValue())

    adccon1 = fract + slres + strgsrc + sidl + dmabl
    symbol.setValue(adccon1, 2)

def adchsCalcADCCON2(symbol, event):
    adccon2 = 0x0
    component = symbol.getComponent()
    adcdiv = component.getSymbolValue("ADCCON2__ADCDIV") << 0
    samc = component.getSymbolValue("ADCCON2__SAMC") << 16
    eos = int(component.getSymbolValue("ADCCON2__EOSIEN")) << 13
    adccon2 = adcdiv + samc + eos
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
            shalt = shalt + (component.getSymbolValue("ADCTRGMODE__SH" + str(channelID) + "ALT") << (channelID * 2 + 16))
    adctrgmode = shalt
    symbol.setValue(adctrgmode, 2)

def adchsCalcADCIMCON1(symbol, event):
    adcimcon1 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(0, 16):
        if (component.getSymbolValue("ADCIMCON1__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON1__SIGN" + str(channelID)) << (channelID*2))
        if (component.getSymbolValue("ADCIMCON1__DIFF" + str(channelID)) != None):
            diff = diff + (component.getSymbolValue("ADCIMCON1__DIFF" + str(channelID)) << ((channelID * 2) + 1))
    adcimcon1 = sign + diff
    symbol.setValue(adcimcon1, 2)

def adchsCalcADCIMCON2(symbol, event):
    adcimcon2 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(16, 32):
        if (component.getSymbolValue("ADCIMCON2__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON2__SIGN" + str(channelID)) << ((channelID - 16) * 2))
        if (component.getSymbolValue("ADCIMCON2__DIFF" + str(channelID)) != None):
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

def adchsCalcADCIMCON4(symbol, event):
    adcimcon4 = 0x0
    sign = 0x0
    diff = 0x0
    component = symbol.getComponent()
    for channelID in range(48, ADC_Max_Signals):
        if (component.getSymbolValue("ADCIMCON4__SIGN" + str(channelID)) != None):
            sign = sign + (component.getSymbolValue("ADCIMCON4__SIGN" + str(channelID)) << ((channelID - 48) * 2))
        if (component.getSymbolValue("ADCIMCON4__DIFF" + str(channelID)) != None):
            diff = diff + (component.getSymbolValue("ADCIMCON4__DIFF" + str(channelID)) << (((channelID - 48) * 2) + 1))
    adcimcon4 = sign + diff
    symbol.setValue(adcimcon4, 2)

def adchsCalcADCTRG(symbol, event):
    adctrg = 0x0
    trgsrc = 0x0
    global adchsSym_ADCTRG__TRGSRC
    component = symbol.getComponent()
    if(event["id"][:7] == "ADCTRG1"):
        for channelID in range(0, 4):
            if (component.getSymbolValue("ADCTRG1__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << (channelID * 8))
    elif(event["id"][:7] == "ADCTRG2"):
        for channelID in range(4, 8):
            if (component.getSymbolValue("ADCTRG2__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 4) * 8))
    elif(event["id"][:7] == "ADCTRG3"):
        for channelID in range(8, 12):
            if (component.getSymbolValue("ADCTRG3__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 8) * 8))
    elif(event["id"][:7] == "ADCTRG4"):
        for channelID in range(12, 16):
            if (component.getSymbolValue("ADCTRG4__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 12) * 8))
    elif(event["id"][:7] == "ADCTRG5"):
        for channelID in range(16, 20):
            if (component.getSymbolValue("ADCTRG5__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 16) * 8))
    elif(event["id"][:7] == "ADCTRG6"):
        for channelID in range(20, 24):
            if (component.getSymbolValue("ADCTRG6__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 20) * 8))
    elif(event["id"][:7] == "ADCTRG7"):
        for channelID in range(24, ADC_Max_Class_1and2):
            if (component.getSymbolValue("ADCTRG7__TRGSRC" + str(channelID)) != None):
                trgsrc = trgsrc + (int(adchsSym_ADCTRG__TRGSRC[channelID].getSelectedValue()) << ((channelID - 24) * 8))

    adctrg = trgsrc
    symbol.setValue(adctrg, 2)

def adchsCalcADCTIME(symbol, event):
    global isDMAFeatureAvailable
    adctime = [ADC_Max_Class_1]
    bchen = 0
    component = symbol.getComponent()
    for channelID in range(0, ADC_Max_Class_1):
        samc = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__SAMC") << (0))
        adcdiv = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__ADCDIV") << (16))
        selres = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__SELRES") << (24))
        if isDMAFeatureAvailable == True:
            bchen = (component.getSymbolValue("ADC"+ str(channelID)+"TIME__BCHEN") << (23))
        adctime.append(channelID)
        adctime[channelID] = samc +  adcdiv + selres + bchen
        adchsSym_ADCTIME[channelID].setValue(adctime[channelID], 2)

def adchsCalcADCDSTAT (symbol, event):
    adcdstat = 0
    rafien = 0
    rbfien = 0
    dmagen = 0

    component = symbol.getComponent()
    for channelID in range(0, ADC_Max_Class_1):
        if component.getSymbolValue("ADC" + str(channelID) + "TIME__BCHEN") == True:
            dmagen = ((0x1) << (31))        # Enable global DMA bit if any channel's DMA is enabled
            rafien |= (component.getSymbolValue("ADCDSTAT__RAFIEN" + str(channelID)) << (8 + channelID))
            rbfien |= (component.getSymbolValue("ADCDSTAT__RBFIEN" + str(channelID)) << (24 + channelID))

    if rafien != 0 or rbfien != 0:
        component.setSymbolValue("ADC_DMA_INT_ENABLED", True)
    else:
        component.setSymbolValue("ADC_DMA_INT_ENABLED", False)

    dmacen = (component.getSymbolValue("ADCDSTAT__DMACEN") << (15))

    adcdstat = dmagen + rbfien + dmacen + rafien
    symbol.setValue(adcdstat)

def adchsADCCMPCON_Update(symbol, event):
    component = symbol.getComponent()
    regIndex = symbol.getID()[-1]

    adccmpcon = 0

    if component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__ENDCMP") ==  True:
        endcmp = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__ENDCMP") << 7
        dcmpgien = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__DCMPGIEN") << 6
        iebtwn = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__IEBTWN") << 4
        iehihi = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__IEHIHI") << 3
        iehilo = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__IEHILO") << 2
        ielohi = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__IELOHI") << 1
        ielolo = component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__IELOLO")

        adccmpcon = endcmp + dcmpgien + iebtwn + iehihi + iehilo + ielohi + ielolo

    symbol.setValue(adccmpcon)

    # Enable EVIC interrupt if both comparator and interrupt are enabled
    if component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__ENDCMP") ==  True and component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__DCMPGIEN") == True:
        component.setSymbolValue("ADCHS_DC" + str(regIndex) + "_INT_ENABLED", True)
    else:
        component.setSymbolValue("ADCHS_DC" + str(regIndex) + "_INT_ENABLED", False)


def adchsADCCMPEN_Update(symbol, event):
    component = symbol.getComponent()
    regIndex = symbol.getID()[-1]

    cmpe = 0

    if component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__ENDCMP") ==  True:
        for index in range (0, 31):
            cmpe |= component.getSymbolValue("ADCCMPEN" + str(regIndex) + "__CMPE" + str(index)) << index

    symbol.setValue(cmpe)

def adchsADCCMP_Update(symbol, event):
    component = symbol.getComponent()
    regIndex = symbol.getID()[-1]

    adccmp = 0

    if component.getSymbolValue("ADCCMPCON" + str(regIndex) + "__ENDCMP") ==  True:
        dcmphi = component.getSymbolValue("ADCCMP" + str(regIndex) + "__DCMPHI") << 16
        dcmplo = component.getSymbolValue("ADCCMP" + str(regIndex) + "__DCMPLO")

        adccmp = dcmphi + dcmplo

    symbol.setValue(adccmp)

def adchsADCFLTR_Update (symbol, event):
    component = symbol.getComponent()
    regIndex = symbol.getID()[-1]

    adcfltr = 0

    if component.getSymbolValue("ADCFLTR" + str(regIndex) + "__AFEN") == True:
        afen = component.getSymbolValue("ADCFLTR" + str(regIndex) + "__AFEN") << 31
        dfmode = int(component.getSymbolByID("ADCFLTR" + str(regIndex) + "__DFMODE").getSelectedValue()) << 29
        ovrsam = int(component.getSymbolByID("ADCFLTR" + str(regIndex) + "__OVRSAM").getSelectedValue(), 16) << 26
        afgien = component.getSymbolValue("ADCFLTR" + str(regIndex) + "__AFGIEN") << 25
        chnlid = component.getSymbolValue("ADCFLTR" + str(regIndex) + "__CHNLID") << 16

        adcfltr = afen + dfmode + ovrsam + afgien + chnlid

    symbol.setValue(adcfltr)

    # Enable EVIC interrupt if both filter and interrupt are enabled
    if component.getSymbolValue("ADCFLTR" + str(regIndex) + "__AFEN") ==  True and component.getSymbolValue("ADCFLTR" + str(regIndex) + "__AFGIEN") == True:
        component.setSymbolValue("ADCHS_DF" + str(regIndex) + "_INT_ENABLED", True)
    else:
        component.setSymbolValue("ADCHS_DF" + str(regIndex) + "_INT_ENABLED", False)

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

def adchsEOSInterrupt(symbol, event):
    InterruptVector = "ADC_EOS_INTERRUPT_ENABLE"
    InterruptHandlerLock = "ADC_EOS_INTERRUPT_HANDLER_LOCK"
    InterruptHandler = "ADC_EOS_INTERRUPT_HANDLER"

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)
    interruptName = InterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if(event["value"] == True):
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_Handler", 1)

def adchsDMAInterrupt(symbol, event):
    InterruptVector = "ADC_DMA_INTERRUPT_ENABLE"
    InterruptHandlerLock = "ADC_DMA_INTERRUPT_HANDLER_LOCK"
    InterruptHandler = "ADC_DMA_INTERRUPT_HANDLER"

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)
    interruptName = InterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if(event["value"] == True):
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_Handler", 1)

def adchsCMPInterrupt(symbol, event):
    cmpIndex = symbol.getID()[len("ADCHS_DC")]

    InterruptVector = "ADC_DC" + cmpIndex +"_INTERRUPT_ENABLE"
    InterruptHandlerLock = "ADC_DC" + cmpIndex + "_INTERRUPT_HANDLER_LOCK"
    InterruptHandler = "ADC_DC" + cmpIndex + "_INTERRUPT_HANDLER"

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)
    interruptName = InterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if(event["value"] == True):
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_Handler", 1)

def adchsFLTInterrupt(symbol, event):
    cmpIndex = symbol.getID()[len("ADCHS_DF")]

    InterruptVector = "ADC_DF" + cmpIndex +"_INTERRUPT_ENABLE"
    InterruptHandlerLock = "ADC_DF" + cmpIndex + "_INTERRUPT_HANDLER_LOCK"
    InterruptHandler = "ADC_DF" + cmpIndex + "_INTERRUPT_HANDLER"

    Database.setSymbolValue("core", InterruptVector, event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 2)
    interruptName = InterruptHandler.split("_INTERRUPT_HANDLER")[0]
    if(event["value"] == True):
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, interruptName + "_Handler", 1)

def adchsNVICInterrupt(symbol, event):
    interrupt_mode = False
    channelInterrupt = False
    component = symbol.getComponent()
    for channelID in range(0, len(adcinterruptmode_deplist)):
        if (component.getSymbolValue(adcinterruptmode_deplist[channelID])):
            interrupt_mode = True
            if ("AGIEN" in adcinterruptmode_deplist[channelID]):
                channelInterrupt = True
    symbol.setValue(channelInterrupt, 2)
    Database.setSymbolValue("core", InterruptVector[0], interrupt_mode)
    Database.setSymbolValue("core", InterruptHandlerLock[0], interrupt_mode)
    if (interrupt_mode == True):
        Database.setSymbolValue("core", InterruptHandler[0], "ADCHS_InterruptHandler")
    else:
        Database.setSymbolValue("core", InterruptHandler[0], "ADCHS_Handler")

def getTCLKValue():
    clk_freq = Database.getSymbolValue("core", "ADCHS_CLOCK_FREQUENCY")
    if (clk_freq == 0):
        #clk_freq = 1
        return 0
    else:
        return float((1.0/clk_freq) * 1000000000)

def adchsClockCalc(symbol, event):
    component = symbol.getComponent()
    if getTCLKValue() == 0:
        symbol.setValue(0.00)
    else:
        symbol.setValue(getTCLKValue() * component.getSymbolValue("ADCCON3__CONCLKDIV"), 2)

def adchsTCLKCalc(symbol, event):
    symbol.setValue((getTCLKValue()), 2)

def adchsTADCCalc(symbol, event):
    component = symbol.getComponent()
    channelID = symbol.getID()[-1]
    tq = component.getSymbolValue("ADCHS_TQ")
    clk_div = component.getSymbolValue("ADC"+str(channelID)+"TIME__ADCDIV")
    if (clk_div == 0):
        symbol.setValue(tq , 2)
    else:
        symbol.setValue(tq * 2 *clk_div, 2)
    ch_enable = component.getSymbolValue("ADCHS_"+str(channelID)+"_ENABLE")
    symbol.setVisible(ch_enable)

def adchsSharedTADCCalc(symbol, event):
    component = symbol.getComponent()
    channelID = symbol.getID()[-1]
    tq = component.getSymbolValue("ADCHS_TQ")
    clk_div = component.getSymbolValue("ADCCON2__ADCDIV")
    if (clk_div == 0):
        symbol.setValue(tq , 2)
    else:
        symbol.setValue(tq * 2 * clk_div, 2)
    ch_enable = component.getSymbolValue("ADCHS_"+str(channelID)+"_ENABLE")
    symbol.setVisible(ch_enable)

def adchsConvRateCalc(symbol, event):
    component = symbol.getComponent()
    channelID = (symbol.getID()[-1])
    tadc = component.getSymbolValue("ADCHS_TADC"+str(channelID))
    samc = component.getSymbolValue("ADC"+str(channelID)+"TIME__SAMC")
    resolution = component.getSymbolValue("ADC"+str(channelID)+"TIME__SELRES")
    resolution = (resolution * 2) + 7
    if tadc <= 0.0:
        symbol.setValue(0)
    else:
        symbol.setValue((1000000.0 / ((2 + samc + resolution) * tadc )), 2)
    ch_enable = component.getSymbolValue("ADCHS_"+str(channelID)+"_ENABLE")
    symbol.setVisible(ch_enable)

def adchsSharedConvRateCalc(symbol, event):
    component = symbol.getComponent()
    channelID = (symbol.getID()[-1])
    tadc = component.getSymbolValue("ADCHS_TADC"+str(channelID))
    samc = component.getSymbolValue("ADCCON2__SAMC")
    resolution = component.getSymbolValue("ADCCON1__SELRES")
    resolution = (resolution * 2) + 7
    if tadc <= 0.0:
        symbol.setValue(0)
    else:
        symbol.setValue((1000000.0 / ((2 + samc + resolution) * tadc )), 2)
    ch_enable = component.getSymbolValue("ADCHS_"+str(channelID)+"_ENABLE")
    symbol.setVisible(ch_enable)

def adcCompVisibility (symbol, event):
    symbol.setVisible(event["value"])

def adcFilterVisibility (symbol, event):
    symbol.setVisible(event["value"])
###################################################################################################
########################### Dependency   #################################
###################################################################################################
def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]


def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    resetChannels()


global lastAdcChU
lastAdcChU = 0
global lastAdcChV
lastAdcChV = 4
global lastADCChPot
lastADCChPot = 7
global lastADCChVdc
lastADCChVdc = 7

def resetChannels():
    global lastAdcChU
    global lastAdcChV
    global lastADCChPot
    global lastADCChVdc

    component = str(adchsInstanceName.getValue()).lower()
    Database.setSymbolValue(component, "ADCHS_"+str(lastAdcChU)+"_ENABLE", False)
    Database.setSymbolValue(component, "ADCHS_"+str(lastAdcChV)+"_ENABLE", False)
    Database.setSymbolValue(component, "ADCHS_"+str(lastADCChPot)+"_ENABLE", False)
    Database.setSymbolValue(component, "ADCHS_"+str(lastADCChVdc)+"_ENABLE", False)

    Database.setSymbolValue(component, "ADCGIRQEN"+str((lastAdcChU/4) + 1)+"__AGIEN"+str(lastAdcChU), False)

def handleMessage(messageID, args):
    global adchsSym_ADCTRGMODE__SHxALT
    global adchsSym_ADCCON1__SELRES
    global adchsSym_ADCTRG__TRGSRC
    global lastAdcChU
    global lastAdcChV
    global lastADCChPot
    global lastADCChVdc
    dict = {}

    if (messageID == "PMSM_FOC_ADC_CH_CONF"):
        component = str(adchsInstanceName.getValue()).lower()

        resetChannels()

        dict['ADC_MAX_CH'] = ADC_Max_Signals
        dict['ADC_MAX_MODULES'] = 8

        lastAdcChU = phUModule = args['PHASE_U']
        phUCh = args['PHASE_U_CH']
        lastAdcChV = phVModule = args['PHASE_V']
        phVCh = args['PHASE_V_CH']
        lastADCChVdc = phDCBusModule = args['VDC']
        phDCBusCh = args['VDC_CH']
        lastADCChPot = phPotModule = args['POT']
        phPotCh = args['POT_CH']
        resolution = args['RESOLUTION']
        trigger = args['TRIGGER']

        # Find the key index of the trigger as a PWM channel as per TRIGGER argument
        count = adchsSym_ADCTRG__TRGSRC[(phUModule/4) + 1].getKeyCount()
        triggerIndex = 0
        for i in range(0,count):
            if ("PWM Generator "+str(trigger) in adchsSym_ADCTRG__TRGSRC[(phUModule/4) + 1].getKey(i) ):
                triggerIndex = i
                break

        # Enable ADC modules, alternate channel, trigger as PWM Phase U, Ph U interrupt
        if (phUModule < 7):
            Database.setSymbolValue(component, "ADC_CH_PHASE_U", "ADCHS_CH"+str(phUModule))
            Database.setSymbolValue(component, "ADCTRG"+str((phUModule/4) + 1)+"__TRGSRC"+str(phUModule), triggerIndex)
            Database.setSymbolValue(component, "INTERRUPT_ADC_RESULT", "INT_SOURCE_ADC_DATA"+str(phUModule))
            Database.setSymbolValue(component, "AN"+str(phUModule), True)
            #interrupt of Ph U channel
            Database.setSymbolValue(component, "ADCGIRQEN"+str((phUModule/4) + 1)+"__AGIEN"+str(phUModule), True)
            adchsSym_ADCTRGMODE__SHxALT[phUModule].setSelectedKey("AN"+str(args['PHASE_U_CH']))
            #resolution
            adchsSym_ADCTIME__SELRES[phUModule].setSelectedKey(str(resolution)+" bits")

        else:
            Database.setSymbolValue(component, "ADC_CH_PHASE_U", "ADCHS_CH"+str(phUCh))
            Database.setSymbolValue(component, "ADCTRG"+str((phUModule/4) + 1)+"__TRGSRC"+str(phUCh), triggerIndex)
            Database.setSymbolValue(component, "INTERRUPT_ADC_RESULT", "INT_SOURCE_ADC_DATA"+str(phUCh))
            #interrupt of Ph U channel
            Database.setSymbolValue(component, "ADCGIRQEN"+str((phUModule/4) + 1)+"__AGIEN"+str(phUCh), True)
            Database.setSymbolValue(component, "AN"+str(phUCh), True)
            #resolution
            if resolution == "12":
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits (default)")
            else:
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits")

        if (phVModule < 7):
            Database.setSymbolValue(component, "ADC_CH_PHASE_V", "ADCHS_CH"+str(phVModule))
            Database.setSymbolValue(component, "ADCTRG"+str((phVModule/4) + 1)+"__TRGSRC"+str(phVModule), triggerIndex)
            adchsSym_ADCTRGMODE__SHxALT[phVModule].setSelectedKey("AN"+str(args['PHASE_V_CH']))
            Database.setSymbolValue(component, "AN"+str(phVModule), True)
            adchsSym_ADCTIME__SELRES[phVModule].setSelectedKey(str(resolution)+" bits")
        else:
            Database.setSymbolValue(component, "ADC_CH_PHASE_V", "ADCHS_CH"+str(phVCh))
            Database.setSymbolValue(component, "ADCTRG"+str((phVModule/4) + 1)+"__TRGSRC"+str(phVCh), triggerIndex)
            Database.setSymbolValue(component, "AN"+str(phVCh), True)
            #resolution
            if resolution == "12":
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits (default)")
            else:
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits")

        if (phDCBusModule < 7):
            Database.setSymbolValue(component, "ADC_CH_VDC_BUS", "ADCHS_CH"+str(phDCBusModule))
            Database.setSymbolValue(component, "ADCTRG"+str((phDCBusModule/4) + 1)+"__TRGSRC"+str(phDCBusModule), triggerIndex)
            adchsSym_ADCTRGMODE__SHxALT[phDCBusModule].setSelectedKey("AN"+str(args['VDC_CH']))
            Database.setSymbolValue(component, "AN"+str(phDCBusModule), True)
            adchsSym_ADCTIME__SELRES[phDCBusModule].setSelectedKey(str(resolution)+" bits")
        else:
            Database.setSymbolValue(component, "ADC_CH_VDC_BUS", "ADCHS_CH"+str(phDCBusCh))
            Database.setSymbolValue(component, "ADCTRG"+str((phDCBusCh/4) + 1)+"__TRGSRC"+str(phDCBusCh), triggerIndex)
            Database.setSymbolValue(component, "AN"+str(phDCBusCh), True)
            #resolution
            if resolution == "12":
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits (default)")
            else:
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits")

        if (phPotModule < 7):
            Database.setSymbolValue(component, "ADC_CH_POT", "ADCHS_CH"+str(phPotModule))
            Database.setSymbolValue(component, "ADCTRG"+str((phPotModule/4) + 1)+"__TRGSRC"+str(phPotModule), triggerIndex)
            adchsSym_ADCTRGMODE__SHxALT[phPotModule].setSelectedKey("AN"+str(args['POT_CH']))
            Database.setSymbolValue(component, "AN"+str(phPotModule), True)
            adchsSym_ADCTIME__SELRES[phPotModule].setSelectedKey(str(resolution)+" bits")
        else:
            Database.setSymbolValue(component, "ADC_CH_POT", "ADCHS_CH"+str(phPotCh))
            Database.setSymbolValue(component, "ADCTRG"+str((phPotCh/4) + 1)+"__TRGSRC"+str(phPotCh), triggerIndex)
            Database.setSymbolValue(component, "AN"+str(phPotCh), True)
            #resolution
            if str(resolution) == "12":
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits (default)")
            else:
                adchsSym_ADCCON1__SELRES.setSelectedKey(str(resolution)+" bits")

        #Enable ADC Module
        Database.setSymbolValue(component, "ADCHS_"+str(phUModule)+"_ENABLE", True)
        Database.setSymbolValue(component, "ADCHS_"+str(phVModule)+"_ENABLE", True)
        Database.setSymbolValue(component, "ADCHS_"+str(phDCBusModule)+"_ENABLE", True)
        Database.setSymbolValue(component, "ADCHS_"+str(phPotModule)+"_ENABLE", True)

    return dict
###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(adchsComponent):
    global adchsInstanceName
    global ADC_Max_Class_1
    global ADC_Max_Signals
    global ADC_Max_Class_1and2
    global Irq_index
    global adciec_depList
    global adcinterruptmode_deplist
    global adchsSym_ADCCON1__STRGSRC
    global adchsSym_ADCTRG__TRGSRC
    global adcEvsys_deplist
    global ADC_EVSYSTrigStart
    global ADC_EVSYSTrigEnd
    global ADC_MIPS_Interrupt
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorUpdate
    global isDMAFeatureAvailable

    MAX_AVAILABLE_SIGNALS = 64

    adchsInstanceName = adchsComponent.createStringSymbol("ADCHS_INSTANCE_NAME", None)
    adchsInstanceName.setVisible(False)
    adchsInstanceName.setDefaultValue(adchsComponent.getID().upper())
    Module = adchsInstanceName.getValue()
    Log.writeInfoMessage("Running " + Module)

    isDMAFeatureAvailable = False
    if "PIC32MK" in Database.getSymbolValue("core", "PRODUCT_FAMILY"):
        isDMAFeatureAvailable = True

    numComparators = 0
    numFilters = 0
    adchs = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]/register-group@[name=\"ADCHS\"]").getChildren()
    for index in range(0, len(adchs)):
        register_name = adchs[index].getAttribute("name")
        if "ADCCMPEN" in register_name:
            numComparators = numComparators + 1
        if "ADCFLTR" in register_name:
            numFilters = numFilters + 1

    adchsSym_nComparators = adchsComponent.createIntegerSymbol("ADCHS_NUM_COMPARATORS", None)
    adchsSym_nComparators.setVisible(False)
    adchsSym_nComparators.setDefaultValue(numComparators)

    adchsSym_nFilters = adchsComponent.createIntegerSymbol("ADCHS_NUM_FILTERS", None)
    adchsSym_nFilters.setVisible(False)
    adchsSym_nFilters.setDefaultValue(numFilters)

    adchsSym_IsDMAAvailable = adchsComponent.createBooleanSymbol("ADC_IS_DMA_AVAILABLE", None)
    adchsSym_IsDMAAvailable.setDefaultValue(isDMAFeatureAvailable)
    adchsSym_IsDMAAvailable.setVisible(False)

    #----------------- motor control APIs ---------------------------------
    adchsConvAPI = adchsComponent.createStringSymbol("ADC_START_CONV_API", None)
    adchsConvAPI.setVisible(False)
    adchsConvAPI.setValue("ADCHS_ChannelConversionStart")

    adchsResultAPI = adchsComponent.createStringSymbol("ADC_GET_RESULT_API", None)
    adchsResultAPI.setVisible(False)
    adchsResultAPI.setValue("ADCHS_ChannelResultGet")

    adchsResultReadyAPI = adchsComponent.createStringSymbol("ADC_IS_RESULT_READY_API", None)
    adchsResultReadyAPI.setVisible(False)
    adchsResultReadyAPI.setValue("ADCHS_ChannelResultIsReady")

    adchsCallbackAPI = adchsComponent.createStringSymbol("ADC_CALLBACK_API", None)
    adchsCallbackAPI.setVisible(False)
    adchsCallbackAPI.setValue("ADCHS_CallbackRegister")

    adchsPhUCh = adchsComponent.createStringSymbol("ADC_CH_PHASE_U", None)
    adchsPhUCh.setVisible(False)
    adchsPhUCh.setValue("ADCHS_CH0")

    adchsPhVCh = adchsComponent.createStringSymbol("ADC_CH_PHASE_V", None)
    adchsPhVCh.setVisible(False)
    adchsPhVCh.setValue("ADCHS_CH4")

    adchsVdcCh = adchsComponent.createStringSymbol("ADC_CH_VDC_BUS", None)
    adchsVdcCh.setVisible(False)
    adchsVdcCh.setValue("ADCHS_CH10")

    adchsPotCh = adchsComponent.createStringSymbol("ADC_CH_POT", None)
    adchsPotCh.setVisible(False)
    adchsPotCh.setValue("ADCHS_CH15")

    adchsResultInt = adchsComponent.createStringSymbol("INTERRUPT_ADC_RESULT", None)
    adchsResultInt.setVisible(False)
    adchsResultInt.setValue("INT_SOURCE_ADC_DATA0")

    #Clock enable
    Database.setSymbolValue("core", adchsInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    #------------------------- ATDF Read -------------------------------------
    packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))

    adchs = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]")

    ADC_Max_DedicatedChannels = 0
    ADC_Max_Signals = 0
    ADC_Max_Class_1and2 = 0
    ADC_Max_Class_1 = 0
    ADC_Max_Class_2 = 0
    ADC_Input_Signals_List = [False] * MAX_AVAILABLE_SIGNALS

    # Each of the dedicated ADCHS SARs must have a DIGEN bit field in the
    # ADCCON3 SFR.
    # ATDF files can skip a channel (e.g., DIGEN6 is absent).  We therefore
    # need to poll the ATDF file to see what channels are present.  They are
    # set in channelList[].
    channelList = []
    registerPath = ATDF.getNode(adchsATDFRegisterPath(Module, "ADCCON3"))
    bitfields = registerPath.getChildren()
    for ii in bitfields:
        if(("DIGEN" in ii.getAttribute("name")) and (ii.getAttribute("values")!=None)):
            if(ii.getAttribute("values")[-1] != '7'):  # channel 7 is shared - do not include in channelList
                channelList.append(ii.getAttribute("values")[-1]) # the last char is a digit

    for ChannelNumber in channelList:
        labelPath = adchsATDFRegisterBitfieldPath(Module, "ADCCON3",
            "DIGEN" + str(ChannelNumber))
        labelNode = ATDF.getNode(labelPath).getAttribute("values")
        if labelNode is not None:
            ADC_Max_DedicatedChannels += 1
    ADC_Max_Class_1 = ADC_Max_DedicatedChannels

    #For PIC32C devices: ATDF lists signals and available pins.
    # If ADCHS signal pin is present in the pinouts, indicate that there is an Analog pin for the signal.
    signal_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADCHS\"]/instance@[name=\""+adchsInstanceName.getValue()+"\"]/signals")
    if (signal_node != None and signal_node.getChildren() != None):
        # First find the available pins on the selected package
        packageName = str(Database.getSymbolValue("core", "COMPONENT_PACKAGE"))
        availablePins = []      # array to save available pins
        pinout = ""

        val = ATDF.getNode("/avr-tools-device-file/variants")
        children = val.getChildren()
        for index in range(0, len(children)):
            if packageName in children[index].getAttribute("package"):
                pinout = children[index].getAttribute("pinout")

        val = ATDF.getNode("/avr-tools-device-file/pinouts/pinout")
        children = val.getChildren()
        for pad in range(0, len(children)):
            availablePins.append(children[pad].getAttribute("pad"))

        #Find ADC input pins from ADCHS signals
        adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADCHS\"]/instance@[name=\""+adchsInstanceName.getValue()+"\"]/signals")
        adc_signals = adc.getChildren()
        for pad in range(0, len(adc_signals)):
            group = adc_signals[pad].getAttribute("group")
            if (("AIN" in group) and ("index" in adc_signals[pad].getAttributeList())):
                padSignal = adc_signals[pad].getAttribute("pad")
                if padSignal in availablePins:
                    ADC_Input_Signals_List[int(adc_signals[pad].getAttribute("index"))] = True

        #Find internal ADC signals from ADCHS parameters
        adc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ADCHS\"]/instance@[name=\""+adchsInstanceName.getValue()+"\"]/parameters")
        if (adc != None):
            adc_parameters = adc.getChildren()
            for pad in range(0, len(adc_parameters)):
                if ("AIN" in adc_parameters[pad].getAttribute("name")):
                    ADC_Input_Signals_List[int(adc_parameters[pad].getAttribute("value"))] = True

    # For PIC32M devices: Each Analog channel on the part must have a Data Register.  Each existing
    # Data register should indicate that there is an Analog pin for that signal.
    SignalNumber = 0
    for SignalNumber in range (0, MAX_AVAILABLE_SIGNALS):
        labelPath = adchsATDFRegisterPath(Module, "ADCDATA" + str(SignalNumber))
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            if (signal_node == None):
                ADC_Input_Signals_List[SignalNumber] = True
            ADC_Max_Signals = SignalNumber + 1

    # The dedicated channels use class 1 signals.  All Class 1 AND class 2
    # signals must have a TRGSRC bit field in one of the ADCTRG SFRs.
    for RegisterNumber in range(0, 7):
        RegisterName = "ADCTRG" + str(RegisterNumber+1)
        labelPath = adchsATDFRegisterPath(Module, RegisterName)
        #Log.writeInfoMessage("Looking for Register" + labelPath)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
             for SignalNumber in range(0, 4):
                signalID = (RegisterNumber * 4) + SignalNumber
                SignalName = "TRGSRC" + str(signalID)
                labelPath = adchsATDFRegisterBitfieldPath(Module, RegisterName,
                    SignalName )
                labelNode = ATDF.getNode(labelPath)
                if labelNode is not None:
                    ADC_Max_Class_1and2 += 1
    ADC_Max_Class_2 = ADC_Max_Class_1and2 - ADC_Max_Class_1

    ADC_EVSYSTrigEnd = 0
    ADC_EVSYSTrigStart = 0
    triggerList = []
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]/value-group@[name=\"ADCCON1__STRGSRC\"]")
    trigger = node.getChildren()
    for index in range (0, len(trigger)):
        if "ADC_TRIG" in trigger[index].getAttribute("caption"):
            triggerList.append(int(filter(str.isdigit, str(trigger[index].getAttribute("caption")))))
    if len(triggerList) != 0:
        ADC_EVSYSTrigStart = min(triggerList)
        ADC_EVSYSTrigEnd = max(triggerList)

    ADC_MIPS_Interrupt = False
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"INT\"]")
    if node != None:    #if MIPS Interrupt unit is present
        ADC_MIPS_Interrupt = True

        if isDMAFeatureAvailable == True:
            #Calculate the proper ADC_DMA interrupt registers using IRQ#
            irqString = "ADC_DMA"
            Irq_index = int(getIRQnumber(irqString))
            statRegName = _get_statReg_parms(Irq_index)
            enblRegIndex = _get_enblReg_parms(Irq_index)

            #IEC REG
            adchsSym_DMA_IEC = adchsComponent.createStringSymbol("ADCHS_DMA_IEC_REG", None)
            adchsSym_DMA_IEC.setDefaultValue("IEC"+str(enblRegIndex))
            adchsSym_DMA_IEC.setVisible(False)

            #IFS REG
            adchsSym_DMA_IFS = adchsComponent.createStringSymbol("ADCHS_DMA_IFS_REG", None)
            adchsSym_DMA_IFS.setDefaultValue("IFS"+str(enblRegIndex))
            adchsSym_DMA_IFS.setVisible(False)

        #Calculate the proper ADC_EOS interrupt registers using IRQ#
        irqString = "ADC_EOS"
        Irq_index = int(getIRQnumber(irqString))
        statRegName = _get_statReg_parms(Irq_index)
        enblRegIndex = _get_enblReg_parms(Irq_index)

        #IEC REG
        adchsSym_EOS_IEC = adchsComponent.createStringSymbol("ADCHS_EOS_IEC_REG", None)
        adchsSym_EOS_IEC.setDefaultValue("IEC"+str(enblRegIndex))
        adchsSym_EOS_IEC.setVisible(False)

        #IFS REG
        adchsSym_EOS_IFS = adchsComponent.createStringSymbol("ADCHS_EOS_IFS_REG", None)
        adchsSym_EOS_IFS.setDefaultValue("IFS"+str(enblRegIndex))
        adchsSym_EOS_IFS.setVisible(False)

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
        num_intrpt_in_first_iec = int(32 - (Irq_index % 32))
        adchsSym_IFS0_INDEX = adchsComponent.createIntegerSymbol("ADCHS_IFS0_NUM_IRQ", None)
        adchsSym_IFS0_INDEX.setVisible(False)
        adchsSym_IFS0_INDEX.setDefaultValue( num_intrpt_in_first_iec)

        if ((ADC_Max_Signals - (num_intrpt_in_first_iec))) >= 1:
            #IEC REG
            adchsSym_IEC1 = adchsComponent.createStringSymbol("ADCHS_IEC1_REG", None)
            adchsSym_IEC1.setDefaultValue("IEC"+str(enblRegIndex+1))
            adchsSym_IEC1.setVisible(False)
            ADC_MAX_EIC_REG = ADC_MAX_EIC_REG + 1

            adchsSym_IFS1_INDEX = adchsComponent.createIntegerSymbol("ADCHS_IFS1_NUM_IRQ", None)
            adchsSym_IFS1_INDEX.setVisible(False)
            adchsSym_IFS1_INDEX.setDefaultValue(32 + (num_intrpt_in_first_iec))

        if ((ADC_Max_Signals - (num_intrpt_in_first_iec + 32))) >= 1 :
            #IEC REG
            adchsSym_IEC2 = adchsComponent.createStringSymbol("ADCHS_IEC2_REG", None)
            adchsSym_IEC2.setDefaultValue("IEC"+str(enblRegIndex+2))
            adchsSym_IEC2.setVisible(False)
            ADC_MAX_EIC_REG = ADC_MAX_EIC_REG + 1

############################## Dependency Lists ##################################
    adctrgmode_deplist = []
    adctrgsns_deplist = []
    if ADC_Max_Class_1 != 0:
        adctrg_deplist = [[] for i in range ((ADC_Max_Class_1and2 / 4))]
    else:
        adctrg_deplist = [[] for i in range ((ADC_Max_Class_1and2 / 4)+1)]
    adctime_deplist = [[] for i in range (ADC_Max_Class_1)]
    adcgirqen_deplist = [[] for i in range (2)]
    adccss_deplist = [[] for i in range (2)]
    if ADC_MIPS_Interrupt == True:
        adciec_depList = [[] for i in range (ADC_MAX_EIC_REG)]
    adcinterruptmode_deplist = []
    adcimcon_deplist = [[] for i in range (int(math.ceil(ADC_Max_Signals / 16.0)))]
    adcEvsys_deplist = []
    adcDMAStat_deplist = []
############################## Dependency Lists End ##################################

################################################################################
########## ADCHS Menu ################################################
########################################################################
    adchsMenu = adchsComponent.createMenuSymbol("ADCHS_MENU", None)
    adchsMenu.setLabel("ADCHS Configuration")

    #max no of channels
    adchsSym_NUM_CHANNELS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CHANNELS", adchsMenu)
    adchsSym_NUM_CHANNELS.setDefaultValue(ADC_Max_DedicatedChannels)
    adchsSym_NUM_CHANNELS.setVisible(False)

    #max no of signals
    adchsSym_NUM_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_SIGNALS", adchsMenu)
    adchsSym_NUM_SIGNALS.setDefaultValue(ADC_Max_Signals)
    adchsSym_NUM_SIGNALS.setVisible(False)

    #no of Class 1 signals
    adchsSym_NUM_CLASS1_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CLASS1_SIGNALS", adchsMenu)
    adchsSym_NUM_CLASS1_SIGNALS.setDefaultValue(ADC_Max_Class_1)
    adchsSym_NUM_CLASS1_SIGNALS.setVisible(False)

    #no of Class 2 signals
    adchsSym_NUM_CLASS2_SIGNALS = adchsComponent.createIntegerSymbol("ADCHS_NUM_CLASS2_SIGNALS", adchsMenu)
    adchsSym_NUM_CLASS2_SIGNALS.setDefaultValue(ADC_Max_Class_2)
    adchsSym_NUM_CLASS2_SIGNALS.setVisible(False)

    adchsSym_MIPS_INTERRUPT = adchsComponent.createBooleanSymbol("ADCHS_MIPS_INT_PRESENT", adchsMenu)
    adchsSym_MIPS_INTERRUPT.setDefaultValue(ADC_MIPS_Interrupt)
    adchsSym_MIPS_INTERRUPT.setVisible(False)

    adchsSym_EARLY_INTERRUPT = adchsComponent.createBooleanSymbol("ADCHS_EARLY_INTERRUPT", adchsMenu)
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]/register-group/register@[name=\"ADCEIEN1\"]")
    if (node != None):
        adchsSym_EARLY_INTERRUPT.setDefaultValue(True)
    else:
        adchsSym_EARLY_INTERRUPT.setDefaultValue(False)
    adchsSym_EARLY_INTERRUPT.setVisible(False)

    adchsSym_ADCCON3__ADCSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "ADCSEL", adchsMenu, True)

    adchsSym_TCLK = adchsComponent.createFloatSymbol("ADCHS_TCLK", adchsMenu)
    adchsSym_TCLK.setLabel("ADCHS Clock (Tclk) (nano sec)")
    adchsSym_TCLK.setDefaultValue(getTCLKValue())
    adchsSym_TCLK.setReadOnly(True)
    adchsSym_TCLK.setDependencies(adchsTCLKCalc, ["core.ADCHS_CLOCK_FREQUENCY", "ADCCON3__CONCLKDIV"])

    adchsSym_ADCCON3__CONCLKDIV = adchsAddLongFromATDFBitfieldCaption(adchsComponent, Module, "ADCCON3", "CONCLKDIV", adchsMenu, True)
    adchsSym_ADCCON3__CONCLKDIV.setDefaultValue(2)
    adchsSym_ADCCON3__CONCLKDIV.setLabel("Select Clock Divider")
    adchsSym_ADCCON3__CONCLKDIV.setMin(1)
    adchsSym_ADCCON3__CONCLKDIV.setMax(64)

    adchsSym_CLOCK = adchsComponent.createFloatSymbol("ADCHS_TQ", adchsMenu)
    adchsSym_CLOCK.setLabel("ADCHS Control clock (Tq) (nano sec)")
    adchsSym_CLOCK.setDefaultValue((getTCLKValue() * adchsSym_ADCCON3__CONCLKDIV.getValue()))
    adchsSym_CLOCK.setMin(0.0)
    adchsSym_CLOCK.setDependencies(adchsClockCalc, ["core.ADCHS_CLOCK_FREQUENCY", "ADCCON3__CONCLKDIV"])
    adchsSym_CLOCK.setReadOnly(True)

    adchsSym_ADCCON3__VREFSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "VREFSEL", adchsMenu, True)
    adchsSym_ADCCON1__FRACT = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FRACT", adchsMenu, True)
    adchsSym_ADCCON1__SIDL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "SIDL", adchsMenu, True)

    if isDMAFeatureAvailable == True:
        adchsSym_ADCCON1__DMABL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "DMABL", adchsMenu, True)

        adchsSym_ADCDSTAT__DMACEN = adchsComponent.createBooleanSymbol("ADCDSTAT__DMACEN", adchsMenu)
        adchsSym_ADCDSTAT__DMACEN.setLabel("Enable storing of sample count in DMA buffer")
        adchsSym_ADCDSTAT__DMACEN.setDefaultValue(False)
        adcDMAStat_deplist.append("ADCDSTAT__DMACEN")

        # Internal symbol to indicate if DMA interrupt is enabled or not (used in FTL)
        adchsSym_DMAINTEN = adchsComponent.createBooleanSymbol("ADC_DMA_INT_ENABLED", None)
        adchsSym_DMAINTEN.setDefaultValue(False)
        adchsSym_DMAINTEN.setVisible(False)
        adchsSym_DMAINTEN.setDependencies(adchsDMAInterrupt, ["ADC_DMA_INT_ENABLED"])

        # Internal symbol to indicate DMA flag mask (used in FTL)
        dma_flag_mask = (((2 ** ADC_Max_Class_1) -1) << 16) | ((2 ** ADC_Max_Class_1) -1) | (1 << 23)
        adchsSym_DMAINTFLAG_MASK = adchsComponent.createHexSymbol("ADC_DMA_INT_FLAG_MASK", None)
        adchsSym_DMAINTFLAG_MASK.setDefaultValue(dma_flag_mask)
        adchsSym_DMAINTFLAG_MASK.setVisible(False)


################################################################################
########## ADCHS Module Configurations  ################################################
########################################################################
    adchsSym_ADCCON3__DIGEN = []
    global adchsSym_ADCTRGMODE__SHxALT
    adchsSym_ADCTRGMODE__SHxALT = []
    adchsSym_ADCTIME__SAMC = []
    adchsSym_ADCTIME__ADCDIV = []
    global adchsSym_ADCTIME__SELRES
    adchsSym_ADCTIME__SELRES = []
    adchsSym_ADCTIME__BCHEN = []
    adchsSym_ADCDMASTAT__RAFIEN = []
    adchsSym_ADCDMASTAT__RBFIEN = []
    adchsSym_ADCTRG__TRGSRC = [None] * MAX_AVAILABLE_SIGNALS
    adchsSym_ADCTRGSNS__LVL = []
    adchsSym_ADCCSS__CSS = [None] * MAX_AVAILABLE_SIGNALS
    adchsSym_class2 = [None] * ADC_Max_Class_2
    adcSym_TADC = []
    adcSym_CONV_RATE = []

    adchsCHConfMenu = adchsComponent.createMenuSymbol("ADCHS_CH_CONF", None)
    adchsCHConfMenu.setLabel("Module Configuration")

    if (ADC_Max_Class_1 != 0):
        adchsDedicatedADCMenu = adchsComponent.createMenuSymbol("ADCHS_DEDICATED_ADC_CONF", adchsCHConfMenu)
        adchsDedicatedADCMenu.setLabel("Dedicated ADC Modules")

    for channelID in range(0, ADC_Max_Class_1):
        #Channel enable
        adchsSym_CH_ENABLE.append(channelID)
        adchsSym_CH_ENABLE[channelID] = adchsComponent.createBooleanSymbol(
            "ADCHS_"+str(channelID)+"_ENABLE", adchsDedicatedADCMenu)
        adchsSym_CH_ENABLE[channelID].setLabel("ADC " + str(channelID))
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
        RegisterName = str(RegisterNameBase1 + str(channelID) + RegisterNameBase2)

        #clock divider
        adchsSym_ADCTIME__ADCDIV.append(channelID)
        adchsSym_ADCTIME__ADCDIV[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
            Module, RegisterName, BitFieldBaseName_ADCDIV,
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTIME__ADCDIV[channelID].setDependencies(adchsVisibilityOnEvent,
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        adchsSym_ADCTIME__ADCDIV[channelID].setMin(1)
        adchsSym_ADCTIME__ADCDIV[channelID].setMax(127)
        adctime_deplist[channelID].append(RegisterName + "__" + BitFieldBaseName_ADCDIV)

        adcSym_TADC.append(channelID)
        adcSym_TADC[channelID] = adchsComponent.createFloatSymbol("ADCHS_TADC" + str(channelID), adchsSym_CH_ENABLE[channelID])
        adcSym_TADC[channelID].setLabel("ADC" + str(channelID) + " Clock (Tadc) (nano sec)")
        adcSym_TADC[channelID].setReadOnly(True)
        adcSym_TADC[channelID].setDefaultValue(adchsSym_CLOCK.getValue())
        adcSym_TADC[channelID].setMin(0.0)
        adcSym_TADC[channelID].setDependencies(adchsTADCCalc, ["ADCHS_TQ", "ADC"+str(channelID)+"TIME__ADCDIV", "ADCHS_"+str(channelID)+"_ENABLE"])

        #sample time
        adchsSym_ADCTIME__SAMC.append(channelID)
        adchsSym_ADCTIME__SAMC[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
            Module, RegisterName, BitFieldBaseName_SAMC,
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTIME__SAMC[channelID].setDefaultValue(1)
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

        conv_rate = (1000.0 / ((2 + 13) * adchsSym_CLOCK.getValue() ))
        adcSym_CONV_RATE.append(channelID)
        adcSym_CONV_RATE[channelID] = adchsComponent.createFloatSymbol("ADCHS_CONV_RATE"+str(channelID), adchsSym_CH_ENABLE[channelID])
        adcSym_CONV_RATE[channelID].setLabel("ADC"+str(channelID)+" Conversion Rate (ksps)")
        adcSym_CONV_RATE[channelID].setReadOnly(True)
        adcSym_CONV_RATE[channelID].setDependencies(adchsConvRateCalc, ["ADCHS_TADC"+str(channelID), \
            "ADC"+str(channelID)+"TIME__SAMC", "ADC"+str(channelID)+"TIME__SELRES", "ADCHS_"+str(channelID)+"_ENABLE"])

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

        RegisterBaseName_ADCCSS = "ADCCSS1"
        BitFieldBaseName_CSS = "CSS"
        adchsSym_ADCCSS__CSS.append(channelID)
        adchsSym_ADCCSS__CSS[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterBaseName_ADCCSS, BitFieldBaseName_CSS + str(channelID),
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
        adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
        adccss_deplist[0].append(RegisterBaseName_ADCCSS + "__" + BitFieldBaseName_CSS + str(channelID))

        if isDMAFeatureAvailable == True:
            # ADCTIME__BCHEN (Enable DMA?)
            RegisterBaseName_ADCTIME = "ADC" + str(channelID) + "TIME"
            BitFieldBaseName_BCHEN = "BCHEN"

            adchsSym_ADCTIME__BCHEN.append(channelID)
            adchsSym_ADCTIME__BCHEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterBaseName_ADCTIME, BitFieldBaseName_BCHEN,
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTIME__BCHEN[channelID].setLabel("Enable DMA?")
            adchsSym_ADCTIME__BCHEN[channelID].setDefaultValue(False)
            adchsSym_ADCTIME__BCHEN[channelID].setDependencies(adchsVisibilityOnEvent,
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            adctime_deplist[channelID].append(RegisterBaseName_ADCTIME + "__" + BitFieldBaseName_BCHEN)
            adcDMAStat_deplist.append(RegisterBaseName_ADCTIME + "__" + BitFieldBaseName_BCHEN)

            # ADCDMASTAT__RBFIEN (Enable BufferA Full Interrupt?)
            RegisterBaseName_ADCDSTAT = "ADCDSTAT"
            BitFieldBaseName_RAFIEN = "RAFIEN" + str(channelID)

            adchsSym_ADCDMASTAT__RAFIEN.append(channelID)
            adchsSym_ADCDMASTAT__RAFIEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterBaseName_ADCDSTAT, BitFieldBaseName_RAFIEN,
                adchsSym_ADCTIME__BCHEN[channelID], False)
            adchsSym_ADCDMASTAT__RAFIEN[channelID].setLabel("Enable Buffer A Full Interrupt?")
            adchsSym_ADCDMASTAT__RAFIEN[channelID].setDefaultValue(False)
            adchsSym_ADCDMASTAT__RAFIEN[channelID].setDependencies(adchsVisibilityOnEvent,
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            adcDMAStat_deplist.append(RegisterBaseName_ADCDSTAT + "__" + BitFieldBaseName_RAFIEN)

            # ADCDMASTAT__RBFIEN (Enable BufferB Full Interrupt?)
            RegisterBaseName_ADCDSTAT = "ADCDSTAT"
            BitFieldBaseName_RBFIEN = "RBFIEN" + str(channelID)

            adchsSym_ADCDMASTAT__RBFIEN.append(channelID)
            adchsSym_ADCDMASTAT__RBFIEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterBaseName_ADCDSTAT, BitFieldBaseName_RBFIEN,
                adchsSym_ADCTIME__BCHEN[channelID], False)
            adchsSym_ADCDMASTAT__RBFIEN[channelID].setLabel("Enable Buffer B Full Interrupt?")
            adchsSym_ADCDMASTAT__RBFIEN[channelID].setDefaultValue(False)
            adchsSym_ADCDMASTAT__RBFIEN[channelID].setDependencies(adchsVisibilityOnEvent,
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            adcDMAStat_deplist.append(RegisterBaseName_ADCDSTAT + "__" + BitFieldBaseName_RBFIEN)

    adchsSharedADCMenu = adchsComponent.createMenuSymbol("ADCHS_SHARED_ADC_CONF", adchsCHConfMenu)
    adchsSharedADCMenu.setLabel("Shared ADC Module")

    channelID = 7  # shared ADC module is fixed as 7. Class 2 and class 3 inputs are processed by shared ADC module.
    #Channel enable
    adchsSym_CH_ENABLE7 = adchsComponent.createBooleanSymbol(
        "ADCHS_"+str(channelID)+"_ENABLE", adchsSharedADCMenu)
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
    adchsSym_ADCCON2__ADCDIV.setMin(1)
    adchsSym_ADCCON2__ADCDIV.setMax(127)
    adchsSym_ADCCON2__ADCDIV.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    adcSym_TADC7 = adchsComponent.createFloatSymbol("ADCHS_TADC" + str(channelID), adchsSym_CH_ENABLE7)
    adcSym_TADC7.setLabel("ADC" + str(channelID) + " Clock (Tadc) (nano sec)")
    adcSym_TADC7.setVisible(False)
    adcSym_TADC7.setReadOnly(True)
    adcSym_TADC7.setMin(0.0)
    adcSym_TADC7.setDefaultValue(adchsSym_CLOCK.getValue())
    adcSym_TADC7.setDependencies(adchsSharedTADCCalc, ["ADCHS_TQ", "ADCCON2__ADCDIV", "ADCHS_"+str(channelID)+"_ENABLE"])

    #sample time
    adchsSym_ADCCON2__SAMC = adchsAddLongFromATDFBitfieldCaption(adchsComponent,
        Module, "ADCCON2", "SAMC", adchsSym_CH_ENABLE7, False)
    adchsSym_ADCCON2__SAMC.setDefaultValue(1)
    adchsSym_ADCCON2__SAMC.setMin(0)
    adchsSym_ADCCON2__SAMC.setMax(1023)
    adchsSym_ADCCON2__SAMC.setDefaultValue(2)
    adchsSym_ADCCON2__SAMC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    # result resolution
    global adchsSym_ADCCON1__SELRES
    adchsSym_ADCCON1__SELRES = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module,
        "ADCCON1", "SELRES", adchsSym_CH_ENABLE7, False)
    adchsSym_ADCCON1__SELRES.setDefaultValue(3)
    adchsSym_ADCCON1__SELRES.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

    conv_rate = (1000.0 / ((2 + 13) * adchsSym_CLOCK.getValue() ))
    adcSym_CONV_RATE7 = adchsComponent.createFloatSymbol("ADCHS_CONV_RATE"+str(channelID), adchsSym_CH_ENABLE7)
    adcSym_CONV_RATE7.setLabel("ADC"+str(channelID)+" Conversion Rate (ksps)")
    adcSym_CONV_RATE7.setVisible(False)
    adcSym_CONV_RATE7.setReadOnly(True)
    adcSym_CONV_RATE7.setDependencies(adchsSharedConvRateCalc, ["ADCHS_TADC"+str(channelID), \
        "ADCCON2__SAMC", "ADCCON1__SELRES", "ADCHS_"+str(channelID)+"_ENABLE"])

    for channelID in range(ADC_Max_Class_1, ADC_Max_Class_1and2):
        if (ADC_Input_Signals_List[channelID] == True):
            adchsSym_class2[channelID - ADC_Max_Class_1] = adchsComponent.createCommentSymbol("ADCHS_CLASS2_INPUT" + str(channelID), adchsSym_CH_ENABLE7)
            adchsSym_class2[channelID - ADC_Max_Class_1].setLabel("CLASS 2 Input AN" + str(channelID))
            adchsSym_class2[channelID - ADC_Max_Class_1].setVisible(False)
            adchsSym_class2[channelID - ADC_Max_Class_1].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

            RegisterNameBase = "ADCTRG"
            BitFieldBaseName_TRGSRC = "TRGSRC"
            RegisterName = RegisterNameBase + str((channelID/4)+1)
            component = adchsAddKeyValueSetFromATDFInitValue(
                adchsComponent, Module, RegisterName, BitFieldBaseName_TRGSRC +
                str(channelID), adchsSym_class2[channelID - ADC_Max_Class_1], False)
            if(component != None):
                adchsSym_ADCTRG__TRGSRC[channelID] = component
                adchsSym_ADCTRG__TRGSRC[channelID].setLabel("Select Trigger Source")
                adchsSym_ADCTRG__TRGSRC[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
                adctrg_deplist[int((channelID/4))].append(RegisterName + "__" + BitFieldBaseName_TRGSRC + str(channelID))
                adcEvsys_deplist.append(RegisterName + "__" + BitFieldBaseName_TRGSRC + str(channelID))

            RegisterBaseName_ADCCSS = "ADCCSS"
            BitFieldBaseName_CSS = "CSS"
            RegisterName = RegisterBaseName_ADCCSS + str((channelID/32)+1)
            component = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterName, BitFieldBaseName_CSS + str(channelID),
                adchsSym_class2[channelID - ADC_Max_Class_1], False)
            if (component != None):
                adchsSym_ADCCSS__CSS[channelID] = component
                adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
                adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
                adccss_deplist[int(channelID/32)].append(RegisterName + "__" + BitFieldBaseName_CSS + str(channelID))


    adchsSym_class3 = adchsComponent.createCommentSymbol("ADCHS_CLASS3_INPUTS", adchsSym_CH_ENABLE7)
    adchsSym_class3.setLabel("CLASS 3 Inputs")
    adchsSym_class3.setVisible(False)
    adchsSym_class3.setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])

    # trigger source
    adchsSym_ADCCON1__STRGSRC = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "STRGSRC", adchsSym_class3, False)
    adchsSym_ADCCON1__STRGSRC.setLabel("Select Trigger Source")
    adchsSym_ADCCON1__STRGSRC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
    adcEvsys_deplist.append("ADCCON1__STRGSRC")

    #End of scan interrupt
    adchsSym_ADCCON2__EOSIEN = adchsAddBooleanFromATDF1ValueValueGroup(
        adchsComponent, Module, "ADCCON2", "EOSIEN", adchsSym_class3, True)
    adchsSym_ADCCON2__EOSIEN.setLabel("Enable End Of Scan (EOS) Interrupt")

    for channelID in range(ADC_Max_Class_1and2, ADC_Max_Signals):
        if (ADC_Input_Signals_List[channelID] == True):
            RegisterBaseName_ADCCSS = "ADCCSS"
            BitFieldBaseName_CSS = "CSS"
            RegisterName = RegisterBaseName_ADCCSS + str((channelID/32)+1)
            component = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterName, BitFieldBaseName_CSS + str(channelID),
                adchsSym_class3, False)
            if(component != None):
                adchsSym_ADCCSS__CSS[channelID] = component
                adchsSym_ADCCSS__CSS[channelID].setLabel("Select AN" + str(channelID) + " for Input Scan")
                adchsSym_ADCCSS__CSS[channelID].setDependencies(adchsVisibilityOnEvent, ["ADCHS_7_ENABLE"])
                adccss_deplist[int(channelID/32)].append(RegisterName + "__" + BitFieldBaseName_CSS + str(channelID))

    #Signal Conditioning menu
    adchsSignalConditionMenu = adchsComponent.createMenuSymbol("ADCHS_SIGNAL_CONDITION_CONF", None)
    adchsSignalConditionMenu.setLabel("Analog Signal Configuration")
    RegisterBaseName_ADCIMCON = "ADCIMCON"
    BitFieldBaseName_SIGN = "SIGN"
    BitFieldBaseName_DIFF = "DIFF"
    RegisterBaseName_ADCGIRQEN = "ADCGIRQEN"
    BitFieldBaseName_AGIEN = "AGIEN"
    adchsSym_ADCIMCON__SIGN = [None] * MAX_AVAILABLE_SIGNALS
    adchsSym_ADCIMCON__DIFF = [None] * MAX_AVAILABLE_SIGNALS
    adchsSym_ADCGIRQEN__AGIEN = [None] * MAX_AVAILABLE_SIGNALS
    RegisterBaseName_ADCEIEN = "ADCEIEN"
    BitFieldBaseName_EIEN = "EIEN"
    adchsSym_ADCEIEN__EIEN = [None] * MAX_AVAILABLE_SIGNALS

    if (ADC_Max_Class_1 != 0):
        adchsClass1SignalMenu = adchsComponent.createMenuSymbol("ADCHS_CLASS1_SIGNALS_CONF", adchsSignalConditionMenu)
        adchsClass1SignalMenu.setLabel("Class 1 Signals")

    adchsClass2SignalMenu = adchsComponent.createMenuSymbol("ADCHS_CLASS2_SIGNALS_CONF", adchsSignalConditionMenu)
    adchsClass2SignalMenu.setLabel("Class 2 Signals")

    adchsClass3SignalMenu = adchsComponent.createMenuSymbol("ADCHS_CLASS3_SIGNALS_CONF", adchsSignalConditionMenu)
    adchsClass3SignalMenu.setLabel("Class 3 Signals")

    for signalID in range(0, ADC_Max_Signals):
        if ADC_Input_Signals_List[signalID] == True:
            if (signalID < ADC_Max_Class_1):
                menu = adchsClass1SignalMenu
            elif ((signalID >= ADC_Max_Class_1) and (signalID < ADC_Max_Class_1and2)):
                menu = adchsClass2SignalMenu
            else:
                menu = adchsClass3SignalMenu

            adchsCONMenu[signalID] = adchsComponent.createBooleanSymbol(
                "AN"+str(signalID), menu)
            adchsCONMenu[signalID].setLabel("Configure Analog Input AN"+str(signalID))

            RegisterName = RegisterBaseName_ADCIMCON + str((signalID/16)+1)
            index = int(((signalID/16)))

            adchsSym_ADCIMCON__SIGN[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterName, BitFieldBaseName_SIGN + str(signalID),
                adchsCONMenu[signalID], False)
            if adchsSym_ADCIMCON__SIGN[signalID] != None:
                adchsSym_ADCIMCON__SIGN[signalID].setDependencies(adchsVisibilityOnEvent,
                    ["AN"+str(signalID)])
                adcimcon_deplist[index].append(RegisterName + "__" + BitFieldBaseName_SIGN + str(signalID))

            adchsSym_ADCIMCON__DIFF[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, RegisterName, BitFieldBaseName_DIFF + str(signalID),
                adchsCONMenu[signalID], False)
            if adchsSym_ADCIMCON__DIFF[signalID] != None:
                adchsSym_ADCIMCON__DIFF[signalID].setDependencies(adchsVisibilityOnEvent,
                    ["AN"+str(signalID)])
                adcimcon_deplist[index].append(RegisterName + "__" + BitFieldBaseName_DIFF + str(signalID))

            RegisterName = RegisterBaseName_ADCGIRQEN + str((signalID/32)+1)
            component = adchsAddBooleanFromATDFBitfieldCaption(
                adchsComponent, Module, RegisterName, BitFieldBaseName_AGIEN + str(signalID),
                adchsCONMenu[signalID], False)
            if(component != None):
                adchsSym_ADCGIRQEN__AGIEN[signalID] = component
                adchsSym_ADCGIRQEN__AGIEN[signalID].setDependencies(adchsVisibilityOnEvent,
                    ["AN"+str(signalID)])
                adcinterruptmode_deplist.append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
                adcgirqen_deplist[int(signalID/32)].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))

                if ADC_MIPS_Interrupt == True:
                    if (signalID < (num_intrpt_in_first_iec)):
                        adciec_depList[0].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
                    elif ((signalID >= (num_intrpt_in_first_iec)) and (signalID < (32 + (num_intrpt_in_first_iec)))):
                        adciec_depList[1].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))
                    else:
                        adciec_depList[2].append(RegisterName + "__" + BitFieldBaseName_AGIEN + str(signalID))

    adchsCompMenu = adchsComponent.createMenuSymbol("ADCHS_COMPARATOR_MENU", None)
    adchsCompMenu.setLabel("Digital Comparator Configuration")

    adchsSym_ADCCMPCON_deplist = []
    adchsSym_ADCCMPEN_deplist = []
    adchsSym_ADCCMP_deplist = []

    for n in range(1, numComparators + 1):
        adchsSym_ADCCMPCON_deplist.append([])
        adchsSym_ADCCMPEN_deplist.append([])
        adchsSym_ADCCMP_deplist.append([])

        #Calculate the proper ADC_DCx interrupt registers using IRQ#
        irqString = "ADC_DC" + str(n)
        adc_dcx_irq_index = int(getIRQnumber(irqString))
        statRegName = _get_statReg_parms(adc_dcx_irq_index)
        enblRegIndex = _get_enblReg_parms(adc_dcx_irq_index)

        #IEC REG
        adchsSym_DCx_IEC = adchsComponent.createStringSymbol("ADCHS_DC" + str(n) + "_IEC_REG", None)
        adchsSym_DCx_IEC.setDefaultValue("IEC"+str(enblRegIndex))
        adchsSym_DCx_IEC.setVisible(False)

        #IFS REG
        adchsSym_DCx_IFS = adchsComponent.createStringSymbol("ADCHS_DC" + str(n) + "_IFS_REG", None)
        adchsSym_DCx_IFS.setDefaultValue("IFS"+str(enblRegIndex))
        adchsSym_DCx_IFS.setVisible(False)

        adchsSym_ADCCMPCON_ENDCMP = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__ENDCMP", adchsCompMenu)
        adchsSym_ADCCMPCON_ENDCMP.setLabel("Digital Comparator " + str(n) + " Enable")
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__ENDCMP")
        adchsSym_ADCCMPEN_deplist[n-1].append("ADCCMPCON" + str(n) + "__ENDCMP")
        adchsSym_ADCCMP_deplist[n-1].append("ADCCMPCON" + str(n) + "__ENDCMP")

        adchsSym_ADCCMP_DCMPHI = adchsComponent.createIntegerSymbol("ADCCMP" + str(n) + "__DCMPHI", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMP_DCMPHI.setLabel("High Limit")
        adchsSym_ADCCMP_DCMPHI.setMin(0)
        adchsSym_ADCCMP_DCMPHI.setMax(65535)
        adchsSym_ADCCMP_DCMPHI.setDefaultValue(0)
        adchsSym_ADCCMP_DCMPHI.setVisible(False)
        adchsSym_ADCCMP_DCMPHI.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMP_deplist[n-1].append("ADCCMP" + str(n) + "__DCMPHI")

        adchsSym_ADCCMP_DCMPLO = adchsComponent.createIntegerSymbol("ADCCMP" + str(n) + "__DCMPLO", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMP_DCMPLO.setLabel("Low Limit")
        adchsSym_ADCCMP_DCMPLO.setMin(0)
        adchsSym_ADCCMP_DCMPLO.setMax(65535)
        adchsSym_ADCCMP_DCMPLO.setDefaultValue(0)
        adchsSym_ADCCMP_DCMPLO.setVisible(False)
        adchsSym_ADCCMP_DCMPLO.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMP_deplist[n-1].append("ADCCMP" + str(n) + "__DCMPLO")

        adchsSym_ADCCMPCON_IEHIHI = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__IEHIHI", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_IEHIHI.setLabel("Enable Comparision Event - ADC value >= High Limit")
        adchsSym_ADCCMPCON_IEHIHI.setDefaultValue(False)
        adchsSym_ADCCMPCON_IEHIHI.setVisible(False)
        adchsSym_ADCCMPCON_IEHIHI.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__IEHIHI")

        adchsSym_ADCCMPCON_IEHILO = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__IEHILO", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_IEHILO.setLabel("Enable Comparision Event - ADC value < High Limit")
        adchsSym_ADCCMPCON_IEHILO.setDefaultValue(False)
        adchsSym_ADCCMPCON_IEHILO.setVisible(False)
        adchsSym_ADCCMPCON_IEHILO.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__IEHILO")

        adchsSym_ADCCMPCON_IELOHI = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__IELOHI", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_IELOHI.setLabel("Enable Comparision Event - ADC value >= Low Limit")
        adchsSym_ADCCMPCON_IELOHI.setDefaultValue(False)
        adchsSym_ADCCMPCON_IELOHI.setVisible(False)
        adchsSym_ADCCMPCON_IELOHI.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__IELOHI")

        adchsSym_ADCCMPCON_IELOLO = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__IELOLO", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_IELOLO.setLabel("Enable Comparision Event - ADC value < Low Limit")
        adchsSym_ADCCMPCON_IELOLO.setDefaultValue(False)
        adchsSym_ADCCMPCON_IELOLO.setVisible(False)
        adchsSym_ADCCMPCON_IELOLO.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__IELOLO")

        adchsSym_ADCCMPCON_IEBTWN = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__IEBTWN", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_IEBTWN.setLabel("Enable Comparision Event - Low Limit <= ADC Value < High Limit")
        adchsSym_ADCCMPCON_IEBTWN.setDefaultValue(False)
        adchsSym_ADCCMPCON_IEBTWN.setVisible(False)
        adchsSym_ADCCMPCON_IEBTWN.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__IEBTWN")

        adchsSym_ADCCMPCON_DCMPGIEN = adchsComponent.createBooleanSymbol("ADCCMPCON" + str(n) + "__DCMPGIEN", adchsSym_ADCCMPCON_ENDCMP)
        adchsSym_ADCCMPCON_DCMPGIEN.setLabel("Enable Interrupt")
        adchsSym_ADCCMPCON_DCMPGIEN.setDefaultValue(False)
        adchsSym_ADCCMPCON_DCMPGIEN.setVisible(False)
        adchsSym_ADCCMPCON_DCMPGIEN.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
        adchsSym_ADCCMPCON_deplist[n-1].append("ADCCMPCON" + str(n) + "__DCMPGIEN")

        for index in range (0, 32):
            adchsSym_ADCCMPEN_CMPE = adchsComponent.createBooleanSymbol("ADCCMPEN" + str(n) + "__CMPE" + str(index), adchsSym_ADCCMPCON_ENDCMP)
            adchsSym_ADCCMPEN_CMPE.setLabel("Enable Comparator on Analog Input AN" + str(index))
            adchsSym_ADCCMPEN_CMPE.setVisible(False)
            adchsSym_ADCCMPEN_CMPE.setDependencies(adcCompVisibility, ["ADCCMPCON" + str(n) + "__ENDCMP"])
            adchsSym_ADCCMPEN_deplist[n-1].append("ADCCMPEN" + str(n) + "__CMPE" + str(index))

        adchsSym_ADCCMPCON = adchsComponent.createHexSymbol("ADCHS_ADCCMPCON" + str(n), None)
        adchsSym_ADCCMPCON.setVisible(False)
        adchsSym_ADCCMPCON.setDefaultValue(0x00)
        adchsSym_ADCCMPCON.setDependencies(adchsADCCMPCON_Update, adchsSym_ADCCMPCON_deplist[n-1])

        adchsSym_ADCCMPEN = adchsComponent.createHexSymbol("ADCHS_ADCCMPEN" + str(n), None)
        adchsSym_ADCCMPEN.setVisible(False)
        adchsSym_ADCCMPEN.setDefaultValue(0x00)
        adchsSym_ADCCMPEN.setDependencies(adchsADCCMPEN_Update, adchsSym_ADCCMPEN_deplist[n-1])

        adchsSym_ADCCMP = adchsComponent.createHexSymbol("ADCHS_ADCCMP" + str(n), None)
        adchsSym_ADCCMP.setVisible(False)
        adchsSym_ADCCMP.setDefaultValue(0x00)
        adchsSym_ADCCMP.setDependencies(adchsADCCMP_Update, adchsSym_ADCCMP_deplist[n-1])

        # Internal symbol to indicate if ADC CMP interrupt is enabled or not (used in FTL)
        adchsSym_DCINTEN = adchsComponent.createBooleanSymbol("ADCHS_DC" + str(n) + "_INT_ENABLED", None)
        adchsSym_DCINTEN.setDefaultValue(False)
        adchsSym_DCINTEN.setVisible(False)
        adchsSym_DCINTEN.setDependencies(adchsCMPInterrupt, ["ADCHS_DC" + str(n) + "_INT_ENABLED"])



    adchsFilterMenu = adchsComponent.createMenuSymbol("ADCHS_FILTER_MENU", None)
    adchsFilterMenu.setLabel("Digital Filter Configuration")

    adchsSym_ADCFLTR_deplist = []

    for n in range(1, numFilters + 1):
        adchsSym_ADCFLTR_deplist.append([])

        #Calculate the proper ADC_DFx interrupt registers using IRQ#
        irqString = "ADC_DF" + str(n)
        adc_dfx_irq_index = int(getIRQnumber(irqString))
        statRegName = _get_statReg_parms(adc_dfx_irq_index)
        enblRegIndex = _get_enblReg_parms(adc_dfx_irq_index)

        #IEC REG
        adchsSym_DFx_IEC = adchsComponent.createStringSymbol("ADCHS_DF" + str(n) + "_IEC_REG", None)
        adchsSym_DFx_IEC.setDefaultValue("IEC"+str(enblRegIndex))
        adchsSym_DFx_IEC.setVisible(False)

        #IFS REG
        adchsSym_DFx_IFS = adchsComponent.createStringSymbol("ADCHS_DF" + str(n) + "_IFS_REG", None)
        adchsSym_DFx_IFS.setDefaultValue("IFS"+str(enblRegIndex))
        adchsSym_DFx_IFS.setVisible(False)

        adchsSym_ADCFLTR_AFEN = adchsComponent.createBooleanSymbol("ADCFLTR" + str(n) + "__AFEN", adchsFilterMenu)
        adchsSym_ADCFLTR_AFEN.setLabel("Digital Filter " + str(n) + " Enable")
        adchsSym_ADCFLTR_deplist[n-1].append("ADCFLTR" + str(n) + "__AFEN")

        adchsSym_ADCFLTR_DFMODE = adchsComponent.createKeyValueSetSymbol("ADCFLTR" + str(n) + "__DFMODE", adchsSym_ADCFLTR_AFEN)
        adchsSym_ADCFLTR_DFMODE.setLabel("Filter Mode")
        adchsSym_ADCFLTR_DFMODE.addKey("0", "0", "Oversampling Mode")
        adchsSym_ADCFLTR_DFMODE.addKey("1", "1", "Averaging Mode")
        adchsSym_ADCFLTR_DFMODE.setDefaultValue(0)
        adchsSym_ADCFLTR_DFMODE.setOutputMode("Key")
        adchsSym_ADCFLTR_DFMODE.setDisplayMode("Description")
        adchsSym_ADCFLTR_DFMODE.setVisible(False)
        adchsSym_ADCFLTR_DFMODE.setDependencies(adcFilterVisibility, ["ADCFLTR" + str(n) + "__AFEN"])
        adchsSym_ADCFLTR_deplist[n-1].append("ADCFLTR" + str(n) + "__DFMODE")

        adchsSym_ADCFLTR_OVRSAM = adchsComponent.createKeyValueSetSymbol("ADCFLTR" + str(n) + "__OVRSAM", adchsSym_ADCFLTR_AFEN)
        adchsSym_ADCFLTR_OVRSAM.setLabel("Oversampling Ratio")
        for id in range(len(OversamplingModeDescription)):
            for key, desc in OversamplingModeDescription[id].items():
                key = key
                value = key
                description = desc             # ATDF does not have proper description attribute. Hence reading from a python list to avoid updating all ATDFs.
            adchsSym_ADCFLTR_OVRSAM.addKey(key, value, description)
        adchsSym_ADCFLTR_OVRSAM.setDefaultValue(0)
        adchsSym_ADCFLTR_OVRSAM.setOutputMode("Value")
        adchsSym_ADCFLTR_OVRSAM.setDisplayMode("Description")
        adchsSym_ADCFLTR_OVRSAM.setVisible(False)
        adchsSym_ADCFLTR_OVRSAM.setDependencies(adcFilterVisibility, ["ADCFLTR" + str(n) + "__AFEN"])
        adchsSym_ADCFLTR_deplist[n-1].append("ADCFLTR" + str(n) + "__OVRSAM")

        adchsSym_ADCFLTR_CHNLID = adchsComponent.createIntegerSymbol("ADCFLTR" + str(n) + "__CHNLID", adchsSym_ADCFLTR_AFEN)
        adchsSym_ADCFLTR_CHNLID.setLabel("Channel ID to Filter")
        adchsSym_ADCFLTR_CHNLID.setMin(0)
        adchsSym_ADCFLTR_CHNLID.setMax(31)
        adchsSym_ADCFLTR_CHNLID.setDefaultValue(0)
        adchsSym_ADCFLTR_CHNLID.setVisible(False)
        adchsSym_ADCFLTR_CHNLID.setDependencies(adcFilterVisibility, ["ADCFLTR" + str(n) + "__AFEN"])
        adchsSym_ADCFLTR_deplist[n-1].append("ADCFLTR" + str(n) + "__CHNLID")

        adchsSym_ADCFLTR_AFGIEN = adchsComponent.createBooleanSymbol("ADCFLTR" + str(n) + "__AFGIEN", adchsSym_ADCFLTR_AFEN)
        adchsSym_ADCFLTR_AFGIEN.setLabel("Enable Interrupt")
        adchsSym_ADCFLTR_AFGIEN.setVisible(False)
        adchsSym_ADCFLTR_AFGIEN.setDependencies(adcFilterVisibility, ["ADCFLTR" + str(n) + "__AFEN"])
        adchsSym_ADCFLTR_deplist[n-1].append("ADCFLTR" + str(n) + "__AFGIEN")

        adchsSym_ADCFLTR = adchsComponent.createHexSymbol("ADCHS_ADCFLTR" + str(n), None)
        adchsSym_ADCFLTR.setVisible(False)
        adchsSym_ADCFLTR.setDefaultValue(0x00)
        adchsSym_ADCFLTR.setDependencies(adchsADCFLTR_Update, adchsSym_ADCFLTR_deplist[n-1])

        # Internal symbol to indicate if ADC Filter interrupt is enabled or not (used in FTL)
        adchsSym_DFINTEN = adchsComponent.createBooleanSymbol("ADCHS_DF" + str(n) + "_INT_ENABLED", None)
        adchsSym_DFINTEN.setDefaultValue(False)
        adchsSym_DFINTEN.setVisible(False)
        adchsSym_DFINTEN.setDependencies(adchsFLTInterrupt, ["ADCHS_DF" + str(n) + "_INT_ENABLED"])




###################################################################################################
########################### Register Values Calculation   #################################
###################################################################################################

    adccon1_deplist = ["ADCCON1__IRQVS", "ADCCON1__SIDL", "ADCCON1__CVDEN", "ADCCON1__FRACT",
    "ADCCON1__SELRES", "ADCCON1__STRGLVL", "ADCCON1__FSSCLKEN", "ADCCON1__FSPBCLKEN", "ADCCON1__STRGSRC", "ADCCON1__DMABL"]
    adchsSym_ADCCON1 = adchsComponent.createHexSymbol("ADCHS_ADCCON1", adchsMenu)
    adchsSym_ADCCON1.setLabel("ADCCON1 register value")
    adchsSym_ADCCON1.setVisible(False)
    adchsSym_ADCCON1.setDefaultValue(0x600000)
    adchsSym_ADCCON1.setDependencies(adchsCalcADCCON1, adccon1_deplist)

    adccon2_deplist = ["ADCCON2__CVDCPL", "ADCCON2__ADCDIV", "ADCCON2__SAMC", "ADCHS_7_ENABLE", "ADCCON2__EOSIEN"]
    adchsSym_ADCCON2 = adchsComponent.createHexSymbol("ADCHS_ADCCON2", adchsMenu)
    adchsSym_ADCCON2.setLabel("ADCCON2 register value")
    adchsSym_ADCCON2.setVisible(False)
    adchsSym_ADCCON2.setDefaultValue(0x0)
    adchsSym_ADCCON2.setDependencies(adchsCalcADCCON2, adccon2_deplist)

    adccon3_deplist = ["ADCCON3__VREFSEL", "ADCCON3__CONCLKDIV", "ADCCON3__ADCSEL"]
    adchsSym_ADCCON3 = adchsComponent.createHexSymbol("ADCHS_ADCCON3", adchsMenu)
    adchsSym_ADCCON3.setLabel("ADCCON3 register value")
    adchsSym_ADCCON3.setVisible(False)
    adchsSym_ADCCON3.setDefaultValue(0x1000000)
    adchsSym_ADCCON3.setDependencies(adchsCalcADCCON3, adccon3_deplist)

    adchsSym_ADCTRGMODE = adchsComponent.createHexSymbol("ADCHS_ADCTRGMODE", None)
    adchsSym_ADCTRGMODE.setLabel("ADCTRGMODE Register")
    adchsSym_ADCTRGMODE.setVisible(False)
    adchsSym_ADCTRGMODE.setDependencies(adchsCalcADCTRGMODE, adctrgmode_deplist)

    adchsSym_ADCIMCON1 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON1", None)
    adchsSym_ADCIMCON1.setLabel("ADCIMCON1 Register")
    adchsSym_ADCIMCON1.setVisible(False)
    adchsSym_ADCIMCON1.setDependencies(adchsCalcADCIMCON1, adcimcon_deplist[0])

    if (len(adcimcon_deplist) > 1):
        adchsSym_ADCIMCON2 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON2", None)
        adchsSym_ADCIMCON2.setLabel("ADCIMCON2 Register")
        adchsSym_ADCIMCON2.setVisible(False)
        adchsSym_ADCIMCON2.setDependencies(adchsCalcADCIMCON2, adcimcon_deplist[1])

    if (len(adcimcon_deplist) > 2):
        adchsSym_ADCIMCON3 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON3", None)
        adchsSym_ADCIMCON3.setLabel("ADCIMCON3 Register")
        adchsSym_ADCIMCON3.setVisible(False)
        adchsSym_ADCIMCON3.setDependencies(adchsCalcADCIMCON3, adcimcon_deplist[2])

    if (len(adcimcon_deplist) > 3):
        adchsSym_ADCIMCON4 = adchsComponent.createHexSymbol("ADCHS_ADCIMCON4", None)
        adchsSym_ADCIMCON4.setLabel("ADCIMCON4 Register")
        adchsSym_ADCIMCON4.setVisible(False)
        adchsSym_ADCIMCON4.setDependencies(adchsCalcADCIMCON4, adcimcon_deplist[3])

    ADCTRG_NUM = 0
    ModuleName = "ADCHS"

    ADCTRG_childrens = ATDF.getNode('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName + '"]').getChildren()

    for register in ADCTRG_childrens:
        if("ADC Trigger Source" in register.getAttribute("caption")):
           ADCTRG_NUM += 1

    global adchsSym_ADCTRG
    adchsSym_ADCTRG = [None]
    for ctrg_id in range(1,ADCTRG_NUM+1):
        adchsSym_ADCTRG.append(ctrg_id)
        if (adctrg_deplist[ctrg_id - 1] != []):
            adchsSym_ADCTRG[ctrg_id] = adchsComponent.createHexSymbol("ADCHS_ADCTRG" + str(ctrg_id), None)
            adchsSym_ADCTRG[ctrg_id].setLabel("ADCTRG" + str(ctrg_id) + "Register")
            adchsSym_ADCTRG[ctrg_id].setVisible(False)
            adchsSym_ADCTRG[ctrg_id].setDependencies(adchsCalcADCTRG,adctrg_deplist[ctrg_id - 1])

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
        adchsSym_ADCTIME[module_id].setDefaultValue(0x3000001)
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

    if isDMAFeatureAvailable == True:
        adchsSym_ADCDSTAT = adchsComponent.createHexSymbol("ADCHS_ADCDSTAT", None)
        adchsSym_ADCDSTAT.setLabel("ADCDSTAT Register")
        adchsSym_ADCDSTAT.setVisible(False)
        adchsSym_ADCDSTAT.setDependencies(adchsCalcADCDSTAT, adcDMAStat_deplist)

###################################################################################################
########################### Events   #################################
###################################################################################################
    events = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EVSYS\"]")
    if (events != None):
        adchsSym_Evsys = adchsComponent.createStringSymbol("ADCHS_EVSYS", None)
        adchsSym_Evsys.setVisible(False)
        adchsSym_Evsys.setDependencies(adchsEvsys, adcEvsys_deplist)

###################################################################################################
########################### Interrupts   #################################
###################################################################################################
    if ADC_MIPS_Interrupt == True:
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

        adchsSym_EOSInterrupt = adchsComponent.createStringSymbol("ADCHS_EOS_INTERRUPT", None)
        adchsSym_EOSInterrupt.setVisible(False)
        adchsSym_EOSInterrupt.setDependencies(adchsEOSInterrupt, ["ADCCON2__EOSIEN"])

    else:
        vectorNode=ATDF.getNode("/avr-tools-device-file/devices/device/interrupts")
        vectorValues = vectorNode.getChildren()
        for id in range(0, len(vectorNode.getChildren())):
            if vectorValues[id].getAttribute("module-instance") == adchsInstanceName.getValue():
                name = vectorValues[id].getAttribute("name")
                InterruptVector.append(name + "_INTERRUPT_ENABLE")
                InterruptHandler.append(name + "_INTERRUPT_HANDLER")
                InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
                InterruptVectorUpdate.append("core." + name + "_INTERRUPT_ENABLE_UPDATE")

        adcinterruptmode_deplist.append("ADCCON2__EOSIEN")

        adchsSym_UpdateInterrupt = adchsComponent.createBooleanSymbol("ADCHS_INTERRUPT", None)
        adchsSym_UpdateInterrupt.setVisible(False)
        adchsSym_UpdateInterrupt.setDependencies(adchsNVICInterrupt, adcinterruptmode_deplist)


    # Clock Warning status
    adchsSym_ClkEnComment = adchsComponent.createCommentSymbol("ADCHS_CLOCK_ENABLE_COMMENT", None)
    adchsSym_ClkEnComment.setLabel("Warning!!! " + adchsInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    adchsSym_ClkEnComment.setVisible(False)
    adchsSym_ClkEnComment.setDependencies(updateADCHSClockWarningStatus, ["core." + adchsInstanceName.getValue() + "_CLOCK_ENABLE"])

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
    if "PIC32M" in Database.getSymbolValue("core", "PRODUCT_FAMILY"):
        adchsSource1File.setSourcePath("../peripheral/adchs_02508/templates/plib_adchs.c.ftl")
    else:
        adchsSource1File.setSourcePath("../peripheral/adchs_02508/templates/plib_adchs_pic32c.c.ftl")
    adchsSource1File.setOutputName("plib_"+Module.lower()+".c")
    adchsSource1File.setDestPath("peripheral/adchs/")
    adchsSource1File.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsSource1File.setType("SOURCE")
    adchsSource1File.setMarkup(True)

    adchsSystemInitFile = adchsComponent.createFileSymbol("ADCHS_INIT", None)
    adchsSystemInitFile.setType("STRING")
    adchsSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adchsSystemInitFile.setSourcePath("../peripheral/adchs_02508/templates/system/initialization.c.ftl")
    adchsSystemInitFile.setMarkup(True)

    adchsSystemDefFile = adchsComponent.createFileSymbol("ADCHS_DEF", None)
    adchsSystemDefFile.setType("STRING")
    adchsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adchsSystemDefFile.setSourcePath("../peripheral/adchs_02508/templates/system/definitions.h.ftl")
    adchsSystemDefFile.setMarkup(True)

    adchsComponent.addPlugin("../peripheral/adchs_02508/plugin/adchs_02508.jar")
