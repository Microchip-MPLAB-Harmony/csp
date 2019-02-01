"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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
# is is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed 
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop dow box for.
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
# is is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed 
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop dow box for.
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
# is is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed 
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a drop dow box for.
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
    
# This creates a Long symbol which results in a 32 bit unsigned numberical box
# with a particular register's bitfield's caption.
#
# Parent is the parent component to the newly created component.  In this case
# is is always adchsComponent.
# ModuleName is the name of the IP module within the ATDF file.
# RegisterName is the name of the register within which to find the needed 
# bitfield in the ATDF file.
# BitFieldName is the name of the bitfield to create a Lon numberical input 
#       dow box for.
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
    
###################################################################################################
########################### Callback Functions   #################################
###################################################################################################


# Meant to be used as a dependancy callback so that a sub element of a boolean 
# symbol can become visible when the boolean becomes true.
def adchsVisibilityOnEvent(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)


###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(adchsComponent):
    global adchsInstanceName
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
            
            
    adchsMenu = adchsComponent.createMenuSymbol("ADCHS_MENU", None)
    adchsMenu.setLabel("ADC Module Configuration")

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
    #adchsSym_NUM_CLASS2_SIGNALS.setVisible(True)
    
    adchsCHConfMenu = adchsComponent.createMenuSymbol("ADCHS_CH_CONF", None)
    adchsCHConfMenu.setLabel("Channel Configuration")

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
    for channelID in range(0, ADC_Max_Class_1and2):
        #Channel menu
        global adchsCHMenu
        if (channelID < ADC_Max_Class_1):
            #Channel enable
            adchsSym_CH_ENABLE.append(channelID)
            adchsSym_CH_ENABLE[channelID] = adchsComponent.createBooleanSymbol(
                "ADCHS_"+str(channelID)+"_ENABLE", adchsCHConfMenu)
            adchsSym_CH_ENABLE[channelID].setLabel("Dedicated Channel " + str(channelID))
            adchsSym_CH_ENABLE[channelID].setDefaultValue(False)
            # Log.writeInfoMessage("ADCHS_"+str(channelID)+"_ENABLE is " + 
                # str(adchsSym_CH_ENABLE[channelID].getValue()))

            #Channel name
            adchsSym_CH_NAME.append(channelID)
            adchsSym_CH_NAME[channelID] = adchsComponent.createStringSymbol(
                "ADCHS_"+str(channelID)+"_NAME", adchsSym_CH_ENABLE[channelID])
            adchsSym_CH_NAME[channelID].setLabel("Name")
            adchsSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
            adchsSym_CH_NAME[channelID].setVisible(False)
            adchsSym_CH_NAME[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            #Channel Digital Enable
            adchsSym_ADCCON3__DIGEN.append(channelID)
            adchsSym_ADCCON3__DIGEN[channelID] = adchsAddKeyValueSetFromATDFInitValue(
                adchsComponent, Module, "ADCCON3", "DIGEN" + str(channelID), 
                adchsSym_CH_ENABLE[channelID], False)
            # Channel Synchronous Sample Enable
            adchsSym_ADCTRGMODE__SSAMPEN.append(channelID)
            adchsSym_ADCTRGMODE__SSAMPEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, "ADCTRGMODE", "SSAMPEN" + str(channelID), 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTRGMODE__SSAMPEN[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            # Channel PreSynchronous Trigger Enable
            adchsSym_ADCTRGMODE__STRGEN.append(channelID)
            adchsSym_ADCTRGMODE__STRGEN[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
                adchsComponent, Module, "ADCTRGMODE", "STRGEN" + str(channelID), 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTRGMODE__STRGEN[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            # Channel Analog Input Select
            adchsSym_ADCTRGMODE__SHxALT.append(channelID)
            adchsSym_ADCTRGMODE__SHxALT[channelID] = adchsAddKeyValueSetFromATDFInitValue(
                adchsComponent, Module, "ADCTRGMODE", "SH" + str(channelID) + "ALT", 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTRGMODE__SHxALT[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])

            RegisterNameBase1 = "ADC"
            RegisterNameBase2 = "TIME"
            BitFieldBaseName_SAMC = "SAMC"
            BitFieldBaseName_ADCDIV = "ADCDIV"
            BitFieldBaseName_SELRES = "SELRES"
            BitFieldBaseName_ADCEIS = "ADCEIS"
    #    for RegisterNumber in range(0, 5):
            RegisterName = str(RegisterNameBase1 + str(channelID)
                + RegisterNameBase2)
            adchsSym_ADCTIME__SAMC.append(channelID)
            adchsSym_ADCTIME__SAMC[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent, 
                Module, RegisterName, BitFieldBaseName_SAMC, 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTIME__SAMC[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
                
            adchsSym_ADCTIME__ADCDIV.append(channelID)
            adchsSym_ADCTIME__ADCDIV[channelID] = adchsAddLongFromATDFBitfieldCaption(adchsComponent, 
                Module, RegisterName, BitFieldBaseName_ADCDIV, 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTIME__ADCDIV[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
                
            adchsSym_ADCTIME__SELRES.append(channelID)
            adchsSym_ADCTIME__SELRES[channelID] = adchsAddKeyValueSetFromATDFInitValue(
                adchsComponent, Module, RegisterName, BitFieldBaseName_SELRES, 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTIME__SELRES[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
                
            adchsSym_ADCTIME__ADCEIS.append(channelID)
            adchsSym_ADCTIME__ADCEIS[channelID] = adchsAddKeyValueSetFromATDFInitValue(
                adchsComponent, Module, RegisterName, BitFieldBaseName_ADCEIS, 
                adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCTIME__ADCEIS[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])

        elif (channelID == 7):
            #Channel enable
            adchsSym_CH_ENABLE.append(channelID)
            adchsSym_CH_ENABLE[channelID] = adchsComponent.createBooleanSymbol(
                "ADCHS_"+str(channelID)+"_ENABLE", adchsCHConfMenu)
            adchsSym_CH_ENABLE[channelID].setLabel("Shared Scan Channel " + str(channelID))
            adchsSym_CH_ENABLE[channelID].setDefaultValue(False)

            #Channel name
            adchsSym_CH_NAME.append(channelID)
            adchsSym_CH_NAME[channelID] = adchsComponent.createStringSymbol(
                "ADCHS_"+str(channelID)+"_NAME", adchsSym_CH_ENABLE[channelID])
            adchsSym_CH_NAME[channelID].setLabel("Name")
            adchsSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
            adchsSym_CH_NAME[channelID].setVisible(False)
            adchsSym_CH_NAME[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            adchsSym_ADCCON1__STRGLVL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "STRGLVL", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON1__STRGLVL.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
            adchsSym_ADCCON1__STRGSRC = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "STRGSRC", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON1__STRGSRC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

            adchsSym_ADCCON1__SELRES = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, 
                "ADCCON1", "SELRES", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON1__SELRES.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
            adchsSym_ADCCON2__ADCDIV = adchsAddLongFromATDFBitfieldCaption(adchsComponent, 
                Module, "ADCCON2", "ADCDIV", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON2__ADCDIV.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
            adchsSym_ADCCON2__ADCEIS = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "ADCEIS", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON2__ADCEIS.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])
            adchsSym_ADCCON2__SAMC = adchsAddLongFromATDFBitfieldCaption(adchsComponent, 
                Module, "ADCCON2", "SAMC", adchsSym_CH_ENABLE[channelID], False)
            adchsSym_ADCCON2__SAMC.setDependencies(adchsVisibilityOnEvent, ["ADCHS_"+str(channelID)+"_ENABLE"])

            RegisterBaseName_ADCCSS = "ADCCSS"
            BitFieldBaseName_CSS = "CSS"
            adchsSym_ADCCSS__CSS = []
            for RegisterNumber in range(0, 2):
                RegisterName = RegisterBaseName_ADCCSS + str(RegisterNumber+1)
                for signalID in range(0, 32):
                    signalNum = (RegisterNumber * 32) + signalID
                    if (signalNum < ADC_Max_Signals):
                        adchsSym_ADCCSS__CSS.append(signalNum)
                        adchsSym_ADCCSS__CSS[signalNum] = adchsAddBooleanFromATDF1ValueValueGroup(
                            adchsComponent, Module, RegisterName, BitFieldBaseName_CSS + str(signalNum), 
                            adchsSym_CH_ENABLE[channelID], False)
                        adchsSym_ADCCSS__CSS[signalNum].setDependencies(adchsVisibilityOnEvent, 
                            ["ADCHS_"+str(channelID)+"_ENABLE"])
                
        else:
            #Channel enable
            adchsSym_CH_ENABLE.append(channelID)
            adchsSym_CH_ENABLE[channelID] = adchsComponent.createBooleanSymbol(
                "ADCHS_"+str(channelID)+"_ENABLE", adchsCHConfMenu)
            adchsSym_CH_ENABLE[channelID].setLabel("Class 2 Channel " + str(channelID))
            adchsSym_CH_ENABLE[channelID].setDefaultValue(False)
            #Channel name
            adchsSym_CH_NAME.append(channelID)
            adchsSym_CH_NAME[channelID] = adchsComponent.createStringSymbol(
                "ADCHS_"+str(channelID)+"_NAME", adchsSym_CH_ENABLE[channelID])
            adchsSym_CH_NAME[channelID].setLabel("Name")
            adchsSym_CH_NAME[channelID].setDefaultValue("CHANNEL_"+str(channelID))
            adchsSym_CH_NAME[channelID].setVisible(False)
            adchsSym_CH_NAME[channelID].setDependencies(adchsVisibilityOnEvent, 
                ["ADCHS_"+str(channelID)+"_ENABLE"])
            
        ## These apply to both the  Class 1 and 2 channels.
        RegisterNameBase = "ADCTRG"
        BitFieldBaseName_TRGSRC = "TRGSRC"
        RegisterName = RegisterNameBase + str((channelID/4)+1)
        adchsSym_ADCTRG__TRGSRC.append(channelID)
        adchsSym_ADCTRG__TRGSRC[channelID] = adchsAddKeyValueSetFromATDFInitValue(
            adchsComponent, Module, RegisterName, BitFieldBaseName_TRGSRC + 
            str(channelID), adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTRG__TRGSRC[channelID].setDependencies(adchsVisibilityOnEvent, 
            ["ADCHS_"+str(channelID)+"_ENABLE"])
        
        RegisterNameBase = "ADCTRGSNS"
        BitFieldBaseName_LVL = "LVL"
        #Log.writeInfoMessage("Signal: "+str(channelID))
        adchsSym_ADCTRGSNS__LVL.append(channelID)
        adchsSym_ADCTRGSNS__LVL[channelID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterNameBase, BitFieldBaseName_LVL + str(channelID), 
            adchsSym_CH_ENABLE[channelID], False)
        adchsSym_ADCTRGSNS__LVL[channelID].setDependencies(adchsVisibilityOnEvent, 
            ["ADCHS_"+str(channelID)+"_ENABLE"])

    #adchsMenu_ADCCON1 = adchsAddRegisterSubMenuFromATDF(adchsComponent, Module, "ADCCON1", adchsMenu)
    adchsSym_ADCCON1__IRQVS = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "IRQVS", adchsMenu, True)
    adchsSym_ADCCON1__FSPBCLKEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FSPBCLKEN", adchsMenu, True)
    adchsSym_ADCCON1__FSSCLKEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FSSCLKEN", adchsMenu, True)
    adchsSym_ADCCON1__CVDEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "CVDEN", adchsMenu, True)
    #adchsSym_ADCCON1__AICPMPEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "AICPMPEN", adchsMenu, True)
    adchsSym_ADCCON1__SIDL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "SIDL", adchsMenu, True)
    #adchsSym_ADCCON1__ON = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "ON", adchsMenu, True)
    adchsSym_ADCCON1__FRACT = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "FRACT", adchsMenu, True)
    #adchsSym_ADCCON1__TRBSLV = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBSLV", adchsMenu, True)
    #adchsSym_ADCCON1__TRBMST = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBMST", adchsMenu, True)
    #adchsSym_ADCCON1__TRBERR = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBERR", adchsMenu, True)
    #adchsSym_ADCCON1__TRBEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON1", "TRBEN", adchsMenu, True)

    #adchsMenu_ADCCON2 = adchsAddRegisterSubMenuFromATDF(adchsComponent, Module, "ADCCON2", adchsMenu)
    #adchsSym_ADCCON2__ADCEIOVR = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "ADCEIOVR", adchsMenu, True)
    #adchsSym_ADCCON2__EOSIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "EOSIEN", adchsMenu, True)
    #adchsSym_ADCCON2__REFFLTIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "REFFLTIEN", adchsMenu, True)
    #adchsSym_ADCCON2__BGVRIEN = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "BGVRIEN", adchsMenu, True)
    adchsSym_ADCCON2__CVDCPL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON2", "CVDCPL", adchsMenu, True)
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
    adchsSym_ADCCON3__VREFSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "VREFSEL", adchsMenu, True)
    adchsSym_ADCCON3__CONCLKDIV = adchsAddLongFromATDFBitfieldCaption(adchsComponent, Module, "ADCCON3", "CONCLKDIV", adchsMenu, True)
    adchsSym_ADCCON3__ADCSEL = adchsAddKeyValueSetFromATDFInitValue(adchsComponent, Module, "ADCCON3", "ADCSEL", adchsMenu, True)
            
            
    # Comparator Configuration Menu
    adchsComparatorConfigMenu = adchsComponent.createMenuSymbol("ADCHS_COMPARATOR_MENU", None)
    adchsComparatorConfigMenu.setLabel("ADC Comparator Configuration")
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
    
    for signalID in range(0, ADC_Max_Signals):
        #Channel menu
        global adchsCONMenu
        adchsCONMenu.append(signalID)
        adchsCONMenu[signalID] = adchsComponent.createBooleanSymbol(
            "AN"+str(signalID), adchsSignalConditionMenu)
        adchsCONMenu[signalID].setLabel("Configure Analog Input AN"+str(signalID))

        RegisterName = RegisterBaseName_ADCIMCON + str((signalID/16)+1)
        # Log.writeInfoMessage("Signal: "+str(signalID))
        adchsSym_ADCIMCON__SIGN.append(signalID)
        adchsSym_ADCIMCON__SIGN[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_SIGN + str(signalID), 
            adchsCONMenu[signalID], False)
        adchsSym_ADCIMCON__SIGN[signalID].setDependencies(adchsVisibilityOnEvent, 
            ["AN"+str(signalID)])
        adchsSym_ADCIMCON__DIFF.append(signalID)
        adchsSym_ADCIMCON__DIFF[signalID] = adchsAddBooleanFromATDF1ValueValueGroup(
            adchsComponent, Module, RegisterName, BitFieldBaseName_DIFF + str(signalID), 
            adchsCONMenu[signalID], False)
        adchsSym_ADCIMCON__DIFF[signalID].setDependencies(adchsVisibilityOnEvent, 
            ["AN"+str(signalID)])

        # for RegisterNumber in range(0, 2):
        RegisterName = RegisterBaseName_ADCGIRQEN + str((signalID/32)+1)
        # Log.writeInfoMessage("Signal: "+str(signalID))
        adchsSym_ADCGIRQEN__AGIEN.append(signalID)
        adchsSym_ADCGIRQEN__AGIEN[signalID] = adchsAddBooleanFromATDFBitfieldCaption(
            adchsComponent, Module, RegisterName, BitFieldBaseName_AGIEN + str(signalID), 
            adchsCONMenu[signalID], False)
        adchsSym_ADCGIRQEN__AGIEN[signalID].setDependencies(adchsVisibilityOnEvent, 
            ["AN"+str(signalID)])

    # for RegisterNumber in range(0, 2):
        RegisterName = RegisterBaseName_ADCEIEN + str((signalID/32)+1)
        signalName = BitFieldBaseName_EIEN + str(signalID)
        # Log.writeInfoMessage("Signal: "+str(signalID))
        adchsSym_ADCEIEN__EIEN.append(signalID)
        adchsSym_ADCEIEN__EIEN[signalID] = adchsAddBooleanFromATDFBitfieldCaption(
            adchsComponent, Module, RegisterName, signalName, 
            adchsCONMenu[signalID], False)
        adchsSym_ADCEIEN__EIEN[signalID].setDependencies(adchsVisibilityOnEvent, 
            ["AN"+str(signalID)])
            
            
    configName = Variables.get("__CONFIGURATION_NAME")

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    adchs = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ADCHS\"]")
    adchsID = adchs.getAttribute("id")

    adchsHeaderFile = adchsComponent.createFileSymbol("ADCHS_HEADER", None)
    adchsHeaderFile.setSourcePath("../peripheral/adchs_"+str(adchsID)+"/templates/plib_adchs.h.ftl")
    adchsHeaderFile.setOutputName("plib_"+Module.lower() + ".h")
    adchsHeaderFile.setDestPath("peripheral/adchs/")
    adchsHeaderFile.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsHeaderFile.setType("HEADER")
    adchsHeaderFile.setMarkup(True)

    adchsGlobalHeaderFile = adchsComponent.createFileSymbol("ADCHS_GLOBALHEADER", None)
    adchsGlobalHeaderFile.setSourcePath("../peripheral/adchs_"+str(adchsID) + "/templates/plib_adchs_common.h")
    adchsGlobalHeaderFile.setOutputName("plib_adchs_common.h")
    adchsGlobalHeaderFile.setDestPath("peripheral/adchs/")
    adchsGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsGlobalHeaderFile.setType("HEADER")

    adchsSource1File = adchsComponent.createFileSymbol("ADCHS_SOURCE", None)
    adchsSource1File.setSourcePath("../peripheral/adchs_"+str(adchsID)+"/templates/plib_adchs.c.ftl")
    adchsSource1File.setOutputName("plib_"+Module.lower()+".c")
    adchsSource1File.setDestPath("peripheral/adchs/")
    adchsSource1File.setProjectPath("config/" + configName +"/peripheral/adchs/")
    adchsSource1File.setType("SOURCE")
    adchsSource1File.setMarkup(True)

    adchsSystemInitFile = adchsComponent.createFileSymbol("ADCHS_INIT", None)
    adchsSystemInitFile.setType("STRING")
    adchsSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    adchsSystemInitFile.setSourcePath("../peripheral/adchs_"+str(adchsID)+"/templates/system/system_initialize.c.ftl")
    adchsSystemInitFile.setMarkup(True)

    adchsSystemDefFile = adchsComponent.createFileSymbol("ADCHS_DEF", None)
    adchsSystemDefFile.setType("STRING")
    adchsSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    adchsSystemDefFile.setSourcePath("../peripheral/adchs_"+str(adchsID)+"/templates/system/system_definitions.h.ftl")
    adchsSystemDefFile.setMarkup(True)
