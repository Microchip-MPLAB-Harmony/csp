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

################################################################################
#### Global Variables ####
################################################################################
global qeiInstanceName

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


def qeiATDFRegisterPath(ModuleName, RegisterName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]')
    return labelPath

def qeiATDFRegisterBitfieldPath(ModuleName, RegisterName, BitfieldName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
        + BitfieldName +'"]')
    return labelPath

def qeiATDFValueGroupPath(ModuleName, ValueGroupName):
    value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
        + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
    return value_groupPath

def qeiATDFValueGroupValuePath(ModuleName, ValueGroupName, ValueString):
    valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
        + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
        ValueString + '"]')
    return valuePath


# This creates a sub menu based on the caption attribute of a Register in the
# ATDF file.
# Parent is the parent component to the newly created component.  In this case
# it is always qeiComponent.
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
def qeiAddRegisterSubMenuFromATDF(Parent, ModuleName, RegisterName, ParentMenu):
    # Log.writeInfoMessage("Adding Menu: " + ModuleName + "_MENU_" + RegisterName)
    labelPath = qeiATDFRegisterPath(ModuleName, RegisterName)
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
# it is always qeiComponent.
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
def qeiAddKeyValueSetFromATDFInitValue(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding KeyValueSet" + ModuleName + " " + RegisterName
        # + " " + BitFieldName)
    registerPath = qeiATDFRegisterPath(ModuleName, RegisterName)
    registerNode = ATDF.getNode(registerPath)
    if registerNode is not None:
        labelPath = qeiATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            value_groupPath = qeiATDFValueGroupPath(ModuleName, RegisterName
                + '__' + BitFieldName)
            value_groupNode = ATDF.getNode(value_groupPath)
            if value_groupNode is not None:
                Component = Parent.createKeyValueSetSymbol(RegisterName + '__' +
                    BitFieldName, Menu)
                qeiValGrp_names = []
                _get_bitfield_names(value_groupNode, qeiValGrp_names)

                Component.setLabel(labelNode.getAttribute('caption'))
                Component.setOutputMode("Value")
                Component.setDisplayMode("Description")
                for ii in qeiValGrp_names:
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
# it is always qeiComponent.
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
def qeiAddBooleanFromATDF1ValueValueGroup(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    value_groupPath = qeiATDFValueGroupValuePath(ModuleName, RegisterName
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

def qeiAddBooleanFromATDFBitfieldName(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = qeiATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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

def qeiAddBooleanFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = qeiATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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
# it is always qeiComponent.
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
def qeiAddLongFromATDFRegisterCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = qeiATDFRegisterPath(ModuleName, RegisterName)
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

def qeiAddLongFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = qeiATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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
    irq_index = 0
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
    regName = "IEC"+str(index)
    return regName

def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    regName = "IFS"+str(index)
    return regName

################################################################################
#### Business Logic ####
################################################################################

def qeiCalcQEICON(symbol, event):
    global instanceNum
    qeicon = 0x0
    component = symbol.getComponent()
    ccm = component.getSymbolValue("QEI"+str(instanceNum)+"CON__CCM") << 0
    gaten = component.getSymbolValue("QEI"+str(instanceNum)+"CON__GATEN") << 2
    cntpol = component.getSymbolValue("QEI"+str(instanceNum)+"CON__CNTPOL") << 3
    intdiv = component.getSymbolValue("QEI"+str(instanceNum)+"CON__INTDIV") << 4
    imv = component.getSymbolValue("QEI"+str(instanceNum)+"CON__IMV") << 8
    pimod = component.getSymbolValue("QEI"+str(instanceNum)+"CON__PIMOD") << 10
    sidl = component.getSymbolValue("QEI"+str(instanceNum)+"CON__QEISIDL") << 13
    qeicon = ccm + gaten + cntpol + intdiv + imv + pimod + sidl
    symbol.setValue(qeicon)

def qeiCalcQEIIOC(symbol, event):
    global instanceNum
    qeiioc = 0x0
    component = symbol.getComponent()
    qeapol = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__QEAPOL") << 4
    qebpol = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__QEBPOL") << 5
    idxpol = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__IDXPOL") << 6
    hompol = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__HOMPOL") << 7
    swpab = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__SWPAB") << 8
    outfnc = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__OUTFNC") << 9
    qfdiv = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__QFDIV") << 11
    fltren = component.getSymbolValue("QEI"+str(instanceNum)+"IOC__FLTREN") << 13
    qeiioc = qeapol + qebpol + idxpol + hompol + swpab + outfnc + qfdiv + fltren
    symbol.setValue(qeiioc)

def qeiCalcQEISTAT(symbol, event):
    global instanceNum
    qeistat = 0x0
    component = symbol.getComponent()
    idxien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__IDXIEN") << 0
    homien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__HOMIEN") << 2
    velovien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__VELOVIEN") << 4
    pciien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__PCIIEN") << 6
    posovien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__POSOVIEN") << 8
    pcleqien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__PCLEQIEN") << 10
    pcheqien = component.getSymbolValue("QEI"+str(instanceNum)+"STAT__PCHEQIEN") << 12
    qeistat = idxien + homien + velovien + pciien + posovien + pcleqien + pcheqien
    symbol.setValue(qeistat)

def qeiInterruptSet(symbol, event):
    global evicDeplist
    global instanceNum
    component = symbol.getComponent()
    interruptSet = False
    qeiInterruptVector = "QEI" +str(instanceNum) + "_INTERRUPT_ENABLE"
    qeiInterruptHandlerLock = "QEI" +str(instanceNum) + "_INTERRUPT_HANDLER_LOCK"
    qeiInterruptHandler = "QEI" +str(instanceNum) + "_INTERRUPT_HANDLER"
    for channel in range (0, len(evicDeplist)):
        if (component.getSymbolValue(evicDeplist[channel])):
            interruptSet = True
    if (interruptSet == True):
        Database.setSymbolValue("core", qeiInterruptVector, True, 2)
        Database.setSymbolValue("core", qeiInterruptHandlerLock, True, 2)
        interruptName = qeiInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        Database.setSymbolValue("core", qeiInterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", qeiInterruptVector, False, 2)
        Database.setSymbolValue("core", qeiInterruptHandlerLock, False, 2)
        interruptName = qeiInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        Database.setSymbolValue("core", qeiInterruptHandler, interruptName + "_Handler", 1)
    symbol.setValue(int(interruptSet), 2)

def updateQEIClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])
################################################################################
#### Component ####
################################################################################
def instantiateComponent(qeiComponent):
    global qeiInstanceName
    global instanceNum
    global evicDeplist

    qeiconDeplist = []
    qeiiocDeplist = []
    qeistatDeplist = []
    evicDeplist = []

    #instance
    qeiInstanceName = qeiComponent.createStringSymbol("QEI_INSTANCE_NAME", None)
    qeiInstanceName.setVisible(False)
    qeiInstanceName.setDefaultValue(qeiComponent.getID().upper())
    Module = "QEI"
    Log.writeInfoMessage("Running " + qeiInstanceName.getValue())

    qeiInstanceNum = qeiComponent.createStringSymbol("QEI_INSTANCE_NUM", None)
    qeiInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(qeiComponent.getID()))
    qeiInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", qeiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    qeiSym_QEICON_QEISIDL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "QEISIDL", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__QEISIDL")
    qeiSym_QEICON_INTDIV = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "INTDIV", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__INTDIV")
    qeiSym_QEICON_CCM = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "CCM", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__CCM")
    qeiSym_QEIIOC_QEAPOL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "QEAPOL", None, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__QEAPOL")
    qeiSym_QEIIOC_QEBPOL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "QEBPOL", None, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__QEBPOL")
    qeiSym_QEIIOC_SWPAB = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "SWPAB", None, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__SWPAB")
    qeiSym_QEICON_GATEN = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "GATEN", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__GATEN")
    qeiSym_QEICON_CNTPOL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "CNTPOL", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__CNTPOL")

    qeiSym_INDEX_AVAILABLE = qeiComponent.createBooleanSymbol("QEI_INDEX_AVAILABLE", None)
    qeiSym_INDEX_AVAILABLE.setLabel("Is Index Pulse Available?")
    qeiSym_QEIIOC_IDXPOL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "IDXPOL", qeiSym_INDEX_AVAILABLE, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__IDXPOL")
    qeiSym_QEICON_IMV = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "IMV", qeiSym_INDEX_AVAILABLE, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__IMV")

    qeiSym_HOME_AVAILABLE = qeiComponent.createBooleanSymbol("QEI_HOME_AVAILABLE", None)
    qeiSym_HOME_AVAILABLE.setLabel("Is Home Signal Available?")
    qeiSym_QEIIOC_HOMPOL = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "HOMPOL", qeiSym_HOME_AVAILABLE, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__HOMPOL")
    qeiSym_QEICON_PIMOD = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"CON", "PIMOD", None, True)
    qeiconDeplist.append("QEI"+str(instanceNum)+"CON__PIMOD")

    qeiSym_QEIIOC_FLTREN = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "FLTREN", None, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__FLTREN")
    qeiSym_QEIIOC_QFDIV = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "QFDIV", qeiSym_QEIIOC_FLTREN, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__QFDIV")

    qeiSym_Comparator_Menu = qeiComponent.createMenuSymbol("QEI_COMPARATOR", None)
    qeiSym_Comparator_Menu.setLabel("Position Comparator")

    qeiSym_QEICMPL = qeiComponent.createLongSymbol("QEI"+str(instanceNum)+"CMPL__CMPL", qeiSym_Comparator_Menu)
    qeiSym_QEICMPL.setLabel("Lower Compare Value")
    qeiSym_QEICMPL.setMin(0)
    qeiSym_QEICMPL.setMax(pow(2, 32) - 1)

    qeiSym_QEIICC = qeiComponent.createLongSymbol("QEI"+str(instanceNum)+"ICC__ICCH", qeiSym_Comparator_Menu)
    qeiSym_QEIICC.setLabel("Higher Compare Value")
    qeiSym_QEIICC.setMin(0)
    qeiSym_QEIICC.setMax(pow(2, 32) - 1)

    qeiSym_QEIIOC_OUTFNC = qeiAddKeyValueSetFromATDFInitValue(qeiComponent, Module, "QEI"+str(instanceNum)+"IOC", "OUTFNC", qeiSym_Comparator_Menu, True)
    qeiiocDeplist.append("QEI"+str(instanceNum)+"IOC__OUTFNC")

    qeiSym_INTERRUPTS_MENU = qeiComponent.createMenuSymbol("QEI_INTERRUPTS", None)
    qeiSym_INTERRUPTS_MENU.setLabel("Interrupts")

    qeiSym_QEISTAT_IDXIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__IDXIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_IDXIEN.setLabel("Enable Index Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__IDXIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__IDXIEN")

    qeiSym_QEISTAT_HOMIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__HOMIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_HOMIEN.setLabel("Enable Home Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__HOMIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__HOMIEN")

    qeiSym_QEISTAT_VELOVIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__VELOVIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_VELOVIEN.setLabel("Enable Velocity Counter Overflow Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__VELOVIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__VELOVIEN")

    qeiSym_QEISTAT_POSOVIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__POSOVIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_POSOVIEN.setLabel("Enable Position Counter Overflow Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__POSOVIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__POSOVIEN")

    qeiSym_QEISTAT_PCIIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__PCIIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_PCIIEN.setLabel("Enable Position Counter Initialization Complete Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__PCIIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__PCIIEN")

    qeiSym_QEISTAT_PCLEQIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__PCLEQIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_PCLEQIEN.setLabel("Enable Position Counter Less Than or Equal Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__PCLEQIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__PCLEQIEN")

    qeiSym_QEISTAT_PCHEQIEN = qeiComponent.createBooleanSymbol("QEI"+str(instanceNum)+"STAT__PCHEQIEN", qeiSym_INTERRUPTS_MENU)
    qeiSym_QEISTAT_PCHEQIEN.setLabel("Enable Position Counter Greater Than or Equal Interrupt")
    qeistatDeplist.append("QEI"+str(instanceNum)+"STAT__PCHEQIEN")
    evicDeplist.append("QEI"+str(instanceNum)+"STAT__PCHEQIEN")
############################################################################
#### Dependency ####
############################################################################

    qeiSym_QEICON = qeiComponent.createHexSymbol("QEI_QEICON", None)
    qeiSym_QEICON.setVisible(False)
    qeiSym_QEICON.setDependencies(qeiCalcQEICON, qeiconDeplist)

    qeiSym_QEIIOC = qeiComponent.createHexSymbol("QEI_QEIIOC", None)
    qeiSym_QEIIOC.setVisible(False)
    qeiSym_QEIIOC.setDependencies(qeiCalcQEIIOC, qeiiocDeplist)

    qeiSym_QEISTAT = qeiComponent.createHexSymbol("QEI_QEISTAT", None)
    qeiSym_QEISTAT.setVisible(False)
    qeiSym_QEISTAT.setDependencies(qeiCalcQEISTAT, qeistatDeplist)

    qeiSym_EVIC = qeiComponent.createIntegerSymbol("QEI_EVIC", None)
    qeiSym_EVIC.setVisible(False)
    qeiSym_EVIC.setDependencies(qeiInterruptSet, evicDeplist)

    #Calculate the proper interrupt registers using IRQ#
    irqString = "QEI" + str(instanceNum)
    icxIrq_index = int(getIRQnumber(irqString))
    statRegName = _get_statReg_parms(icxIrq_index)
    enblRegName = _get_enblReg_parms(icxIrq_index)

    #IFS REG
    qeiSym_IFS = qeiComponent.createStringSymbol("QEI_IFS_REG", None)
    qeiSym_IFS.setDefaultValue(statRegName)
    qeiSym_IFS.setVisible(False)

    #IEC REG
    qeiSym_IEC = qeiComponent.createStringSymbol("QEI_IEC_REG", None)
    qeiSym_IEC.setDefaultValue(enblRegName)
    qeiSym_IEC.setVisible(False)

    # Clock Warning status
    qeiSym_ClkEnComment = qeiComponent.createCommentSymbol("QEI_CLOCK_ENABLE_COMMENT", None)
    qeiSym_ClkEnComment.setLabel("Warning!!! " + qeiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    qeiSym_ClkEnComment.setVisible(False)
    qeiSym_ClkEnComment.setDependencies(updateQEIClockWarningStatus, ["core." + qeiInstanceName.getValue() + "_CLOCK_ENABLE"])

############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    qeiHeaderFile = qeiComponent.createFileSymbol("QEI_COMMON_HEADER", None)
    qeiHeaderFile.setMarkup(True)
    qeiHeaderFile.setSourcePath("../peripheral/qei_01494/templates/plib_qei_common.h.ftl")
    qeiHeaderFile.setOutputName("plib_qei_common.h")
    qeiHeaderFile.setDestPath("peripheral/qei/")
    qeiHeaderFile.setProjectPath("config/" + configName + "/peripheral/qei/")
    qeiHeaderFile.setType("HEADER")
    qeiHeaderFile.setOverwrite(True)

    qeiHeader1File = qeiComponent.createFileSymbol("QEI_HEADER1", None)
    qeiHeader1File.setMarkup(True)
    qeiHeader1File.setSourcePath("../peripheral/qei_01494/templates/plib_qei.h.ftl")
    qeiHeader1File.setOutputName("plib_" + qeiInstanceName.getValue().lower() + ".h")
    qeiHeader1File.setDestPath("peripheral/qei/")
    qeiHeader1File.setProjectPath("config/" + configName + "/peripheral/qei/")
    qeiHeader1File.setType("HEADER")
    qeiHeader1File.setOverwrite(True)

    qeiSource1File = qeiComponent.createFileSymbol("QEI_SOURCE1", None)
    qeiSource1File.setMarkup(True)
    qeiSource1File.setSourcePath("../peripheral/qei_01494/templates/plib_qei.c.ftl")
    qeiSource1File.setOutputName("plib_" + qeiInstanceName.getValue().lower() + ".c")
    qeiSource1File.setDestPath("peripheral/qei/")
    qeiSource1File.setProjectPath("config/" + configName + "/peripheral/qei/")
    qeiSource1File.setType("SOURCE")
    qeiSource1File.setOverwrite(True)

    qeiSystemInitFile = qeiComponent.createFileSymbol("QEI_INIT", None)
    qeiSystemInitFile.setType("STRING")
    qeiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    qeiSystemInitFile.setSourcePath("../peripheral/qei_01494/templates/system/initialization.c.ftl")
    qeiSystemInitFile.setMarkup(True)

    qeiSystemDefFile = qeiComponent.createFileSymbol("QEI_DEF", None)
    qeiSystemDefFile.setType("STRING")
    qeiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    qeiSystemDefFile.setSourcePath("../peripheral/qei_01494/templates/system/definitions.h.ftl")
    qeiSystemDefFile.setMarkup(True)
