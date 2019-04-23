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
global mcpwmInstanceName

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


def mcpwmATDFRegisterPath(ModuleName, RegisterName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]')
    return labelPath

def mcpwmATDFRegisterBitfieldPath(ModuleName, RegisterName, BitfieldName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
        + BitfieldName +'"]')
    return labelPath

def mcpwmATDFValueGroupPath(ModuleName, ValueGroupName):
    value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
        + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
    return value_groupPath

def mcpwmATDFValueGroupValuePath(ModuleName, ValueGroupName, ValueString):
    valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
        + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
        ValueString + '"]')
    return valuePath


# This creates a sub menu based on the caption attribute of a Register in the
# ATDF file.
# Parent is the parent component to the newly created component.  In this case
# it is always mcpwmComponent.
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
def mcpwmAddRegisterSubMenuFromATDF(Parent, ModuleName, RegisterName, ParentMenu):
    # Log.writeInfoMessage("Adding Menu: " + ModuleName + "_MENU_" + RegisterName)
    labelPath = mcpwmATDFRegisterPath(ModuleName, RegisterName)
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
# it is always mcpwmComponent.
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
def mcpwmAddKeyValueSetFromATDFInitValue(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding KeyValueSet" + ModuleName + " " + RegisterName
        # + " " + BitFieldName)
    registerPath = mcpwmATDFRegisterPath(ModuleName, RegisterName)
    registerNode = ATDF.getNode(registerPath)
    if registerNode is not None:
        labelPath = mcpwmATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            value_groupPath = mcpwmATDFValueGroupPath(ModuleName, RegisterName
                + '__' + BitFieldName)
            value_groupNode = ATDF.getNode(value_groupPath)
            if value_groupNode is not None:
                Component = Parent.createKeyValueSetSymbol(RegisterName + '__' +
                    BitFieldName, Menu)
                mcpwmValGrp_names = []
                _get_bitfield_names(value_groupNode, mcpwmValGrp_names)

                Component.setLabel(labelNode.getAttribute('caption'))
                Component.setOutputMode("Value")
                Component.setDisplayMode("Description")
                for ii in mcpwmValGrp_names:
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
# it is always mcpwmComponent.
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
def mcpwmAddBooleanFromATDF1ValueValueGroup(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    value_groupPath = mcpwmATDFValueGroupValuePath(ModuleName, RegisterName
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

def mcpwmAddBooleanFromATDFBitfieldName(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = mcpwmATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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

def mcpwmAddBooleanFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Boolean: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = mcpwmATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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
# it is always mcpwmComponent.
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
def mcpwmAddLongFromATDFRegisterCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = mcpwmATDFRegisterPath(ModuleName, RegisterName)
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

def mcpwmAddLongFromATDFBitfieldCaption(Parent, ModuleName, RegisterName, BitFieldName, Menu, Visibility):
    # Log.writeInfoMessage("Adding Long: " + ModuleName + " " + RegisterName +
        # " " + BitFieldName)
    labelPath = mcpwmATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
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

def _get_num_outputs(channelID):
    children = []
    node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name=\"MCPWM\"]/instance@[name=\"MCPWM\"]/parameters')
    children = node.getChildren()
    for ch in range (0, len(children)):
        if (children[ch].getAttribute("name") == "MCPWM_CH"+str(channelID)+"_OUTPUTS"):
            num_outputs = children[ch].getAttribute("value")
    return num_outputs
################################################################################
#### Business Logic ####
################################################################################

def mcpwmCalcPTCON(symbol, event):
    ptcon = 0x0
    component = symbol.getComponent()
    sevtps = component.getSymbolValue("PTCON__SEVTPS") << 0
    pclkdiv = component.getSymbolValue("PTCON__PCLKDIV") << 4
    seien = component.getSymbolValue("PTCON__SEIEN") << 11
    ptcon = sevtps + pclkdiv + seien
    symbol.setValue(ptcon, 2)


def mcpwmCalcSTCON(symbol, event):
    stcon = 0x0
    component = symbol.getComponent()
    sevtps = component.getSymbolValue("STCON__SEVTPS") << 0
    sclkdiv = component.getSymbolValue("STCON__SCLKDIV") << 4
    ssein = component.getSymbolValue("STCON__SSEIEN") << 11
    stcon = sevtps + sclkdiv + ssein
    symbol.setValue(stcon, 2)

def mcpwmCalcPWMCON(symbol, event):
    pwmcon = 0x0
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    mtbs = component.getSymbolValue("PWMCON"+str(channelID)+"__MTBS") << 3
    ptdir = component.getSymbolValue("PWMCON"+str(channelID)+"__PTDIR") << 4
    itb  = component.getSymbolValue("PWMCON"+str(channelID)+"__ITB") << 9
    ecam = component.getSymbolValue("PWMCON"+str(channelID)+"__ECAM") << 10
    dtcp = component.getSymbolValue("PWMCON"+str(channelID)+"__DTCP") << 5
    dtc = component.getSymbolValue("PWMCON"+str(channelID)+"__DTC") << 6

    #interrupts
    pwmhien = component.getSymbolValue("PWMCON"+str(channelID)+"__PWMHIEN") << 19
    pwmlien = component.getSymbolValue("PWMCON"+str(channelID)+"__PWMLIEN") << 20
    trgien = component.getSymbolValue("PWMCON"+str(channelID)+"__TRGIEN") << 21
    clien = component.getSymbolValue("PWMCON"+str(channelID)+"__CLIEN") << 22
    fltien = component.getSymbolValue("PWMCON"+str(channelID)+"__FLTIEN") << 23

    pwmcon = mtbs + ptdir + ecam + dtcp + dtc + itb + pwmhien +  pwmlien + trgien + clien + fltien
    symbol.setValue(pwmcon, 2)

def mcpwmCalcIOCON(symbol, event):
    iocon = 0x0
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    swap = component.getSymbolValue("IOCON"+str(channelID)+"__SWAP") << 2
    id = component.getSymbolByID("IOCON"+str(channelID)+"__PMOD")
    pmod = int(id.getSelectedValue()) << 10
    poll = component.getSymbolValue("IOCON"+str(channelID)+"__POLL") << 11
    polh = component.getSymbolValue("IOCON"+str(channelID)+"__POLH") << 12

    fltdat_pwmh = component.getSymbolValue("IOCON"+str(channelID)+"__FLTDAT_PWMH") << 5
    fltdat_pwml = component.getSymbolValue("IOCON"+str(channelID)+"__FLTDAT_PWML") << 4
    id = component.getSymbolByID("IOCON"+str(channelID)+"__FLTMOD")
    fltmod = int(id.getSelectedValue()) << 16
    fltpol = component.getSymbolValue("IOCON"+str(channelID)+"__FLTPOL") << 18
    id = component.getSymbolByID("IOCON"+str(channelID)+"__FLTSRC")
    fltsrc = int(id.getSelectedValue()) << 19

    cldat_pwmh = component.getSymbolValue("IOCON"+str(channelID)+"__CLDAT_PWMH") << 3
    cldat_pwml = component.getSymbolValue("IOCON"+str(channelID)+"__CLDAT_PWML") << 2
    clmod = component.getSymbolValue("IOCON"+str(channelID)+"__CLMOD") << 24
    clpol = component.getSymbolValue("IOCON"+str(channelID)+"__CLPOL") << 25
    id = component.getSymbolByID("IOCON"+str(channelID)+"__CLSRC")
    clsrc = int(id.getSelectedValue()) << 26

    iocon = swap + pmod + poll + polh + (0x3 << 14) + \
            fltdat_pwmh + fltdat_pwml + fltmod + fltpol + fltsrc + \
            cldat_pwmh + cldat_pwml + clmod + clpol + clsrc
    symbol.setValue(iocon, 2)

def mcpwmCalcLEBCON(symbol, event):
    lebcon = 0x0
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    cl = int(component.getSymbolValue("LEBCON"+str(channelID)+"__CLLENBEN")) << 10
    flt = int(component.getSymbolValue("LEBCON"+str(channelID)+"__FLTLEBEN")) << 11
    plf = component.getSymbolValue("LEBCON"+str(channelID)+"__PLF") << 12
    plr = component.getSymbolValue("LEBCON"+str(channelID)+"__PLR") << 13
    phf = component.getSymbolValue("LEBCON"+str(channelID)+"__PHF") << 14
    phr = component.getSymbolValue("LEBCON"+str(channelID)+"__PHR") << 15
    lebcon = cl + flt + plf + plr + phf + phr
    symbol.setValue(lebcon, 2)

def mcpwmDutyMax(symbol, event):
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    if (component.getSymbolValue("PWMCON"+str(channelID)+"__ITB") == 1):
        max = component.getSymbolValue("PHASE"+str(channelID)+"__PHASE")
    else:
        if (component.getSymbolValue("PWMCON"+str(channelID)+"__MTBS") == 1):
            max = component.getSymbolValue("PTPER__PTPER")
        else:
            max = component.getSymbolValue("STPER__STPER")
    symbol.setMax(int(max))
    if (symbol.getID() == "SDC"+str(channelID)+"__SDC"):
        if (component.getSymbolValue("PWMCON"+str(channelID)+"__ECAM") == (2 or 3)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

def mcpwmPeriodCalc(symbol, event):
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    if (component.getSymbolValue("PWMCON"+str(channelID)+"__ITB") == 1):
        max = component.getSymbolValue("PHASE"+str(channelID)+"__PHASE")
    else:
        if (component.getSymbolValue("PWMCON"+str(channelID)+"__MTBS") == 0):
            max = component.getSymbolValue("PTPER__PTPER")
        else:
            max = component.getSymbolValue("STPER__STPER")
    symbol.setValue(int(max), 2)

def mcpwmChFreq(symbol, event):
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    clock = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    period = component.getSymbolValue("MCPWM_PERIOD_CH"+str(channelID))
    if (component.getSymbolValue("PWMCON"+str(channelID)+"__MTBS") == 0):
        prescaler = pow(2, component.getSymbolValue("PTCON__PCLKDIV"))
    else:
        prescaler = pow(2, component.getSymbolValue("STCON__SCLKDIV"))
    mode = component.getSymbolValue("PWMCON"+str(channelID)+"__ECAM")
    if (mode > 0):
        div = 2
    else:
        div = 1
    if (period != 0):
        freq = clock/float(period)/div/prescaler
    else:
        freq = 0
    symbol.setLabel("**** PWM Frequency is " + str(freq) + " Hz ****")

def mcpwmDTCompensation(symbol, event):
    if event["value"] == 3:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def mcpwmFreqCalc(symbol, event):
    component = symbol.getComponent()
    clock = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    if (symbol.getID() == "MCPWM_PRI_FREQ"):
        div = pow(2, int(component.getSymbolValue("PTCON__PCLKDIV")))
        period = component.getSymbolValue("PTPER__PTPER")
    else:
        div = pow(2, int(component.getSymbolValue("STCON__SCLKDIV")))
        period = component.getSymbolValue("STPER__STPER")
    if (period != 0):
        freq = (float(clock)/div) / float(period)
    else:
        freq = 0
    symbol.setValue(freq, 2)

def mcpwmDeadTimeCalc(symbol, event):
    deadtime = 0
    component = symbol.getComponent()
    channelID = filter(str.isdigit,str(symbol.getID()))
    clock = float(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    if (clock != 0):
        if (symbol.getID() == "MCPWM_LEADING_DEADTIME"+str(channelID)):
            deadtime = component.getSymbolValue("DTR"+str(channelID)+"__DTR") * 1000000.0 / clock
            symbol.setLabel("**** Leading edge dead time is " +  str(deadtime) + " uS ****")
        else:
            deadtime = component.getSymbolValue("ALTDTR"+str(channelID)+"__ALTDTR") * 1000000.0 / clock
            symbol.setLabel("**** Trailing edge dead time is " +  str(deadtime) + " uS ****")

def mcpwmInterruptSet(symbol, event):
    global evicDeplist
    component = symbol.getComponent()
    channelID = int(filter(str.isdigit,str(symbol.getID())))
    interruptSet = False
    mcpwmInterruptVector = "PWM" + str(channelID) + "_INTERRUPT_ENABLE"
    mcpwmInterruptHandlerLock = "PWM" + str(channelID) + "_INTERRUPT_HANDLER_LOCK"
    mcpwmInterruptHandler = "PWM" + str(channelID) + "_INTERRUPT_HANDLER"
    for channel in range (0, len(evicDeplist[channelID - 1])):
        if (component.getSymbolValue(evicDeplist[channelID - 1][channel])):
            interruptSet = True
    if (interruptSet == True):
        Database.setSymbolValue("core", mcpwmInterruptVector, True, 2)
        Database.setSymbolValue("core", mcpwmInterruptHandlerLock, True, 2)
        interruptName = mcpwmInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", mcpwmInterruptVector, False, 2)
        Database.setSymbolValue("core", mcpwmInterruptHandlerLock, False, 2)
        interruptName = mcpwmInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_Handler", 1)
    symbol.setValue(int(interruptSet), 2)

def mcpwmSpecialInterruptSet(symbol, event):
    if (event["id"] == "PTCON__SEIEN"):
        mcpwmInterruptVector = "PWM_PRI_INTERRUPT_ENABLE"
        mcpwmInterruptHandlerLock = "PWM_PRI_INTERRUPT_HANDLER_LOCK"
        mcpwmInterruptHandler = "PWM_PRI_INTERRUPT_HANDLER"
        Database.setSymbolValue("core", mcpwmInterruptVector, event["value"], 2)
        Database.setSymbolValue("core", mcpwmInterruptHandlerLock, event["value"], 2)
        interruptName = mcpwmInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        if (event["value"] == True):
            Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_Handler", 1)
    else:
        mcpwmInterruptVector = "PWM_SEC_INTERRUPT_ENABLE"
        mcpwmInterruptHandlerLock = "PWM_SEC_INTERRUPT_HANDLER_LOCK"
        mcpwmInterruptHandler = "PWM_SEC_INTERRUPT_HANDLER"
        Database.setSymbolValue("core", mcpwmInterruptVector, event["value"], 2)
        Database.setSymbolValue("core", mcpwmInterruptHandlerLock, event["value"], 2)
        interruptName = mcpwmInterruptHandler.split("_INTERRUPT_HANDLER")[0]
        if (event["value"] == True):
            Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", mcpwmInterruptHandler, interruptName + "_Handler", 1)

def updateMCPWMClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

def mcpwmChClockEnable(symbol, event):
    channelID = int(filter(str.isdigit,str(symbol.getID())))
    if(event["value"] == True):
        #Clock enable
        Database.setSymbolValue("core", mcpwmInstanceName.getValue() + str(channelID) + "_CLOCK_ENABLE", True, 1)
    else:
        Database.setSymbolValue("core", mcpwmInstanceName.getValue() + str(channelID) + "_CLOCK_ENABLE", False, 1)
################################################################################
#### Component ####
################################################################################
def instantiateComponent(mcpwmComponent):
    global mcpwmInstanceName
    global evicDeplist

    #instance
    mcpwmInstanceName = mcpwmComponent.createStringSymbol("MCPWM_INSTANCE_NAME", None)
    mcpwmInstanceName.setVisible(False)
    mcpwmInstanceName.setDefaultValue(mcpwmComponent.getID().upper())
    Module = mcpwmInstanceName.getValue()
    Log.writeInfoMessage("Running " + mcpwmInstanceName.getValue())

    mcpwmInstanceNum = mcpwmComponent.createStringSymbol("MCPWM_INSTANCE_NUM", None)
    mcpwmInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(mcpwmComponent.getID()))
    mcpwmInstanceNum.setDefaultValue(instanceNum)

    MCPWM_MAX_CHANNELS = 12

    mcpwmSym_NUM_CHANNELS = mcpwmComponent.createIntegerSymbol("MCPWM_NUM_CHANNELS", None)
    mcpwmSym_NUM_CHANNELS.setVisible(False)
    mcpwmSym_NUM_CHANNELS.setDefaultValue(MCPWM_MAX_CHANNELS)

    ptconDepList = []
    stconDepList = []
    pwmconDepList = [[] for i in range (MCPWM_MAX_CHANNELS)]
    ioconDepList = [[] for i in range (MCPWM_MAX_CHANNELS)]
    lebconDepList = [[] for i in range (MCPWM_MAX_CHANNELS)]
    evicDeplist = [[] for i in range (MCPWM_MAX_CHANNELS)]

    #PWM common Configurations
    mcpwmSym_PWM_CONF = mcpwmComponent.createMenuSymbol("MCPWM_CONF", None)
    mcpwmSym_PWM_CONF.setLabel("PWM Configurations")

    #Primary Time base
    mcpwmSym_PRIMARY_TIMEBASE_CONF = mcpwmComponent.createMenuSymbol("MCPWM_PRI_TIMEBASE_CONF", mcpwmSym_PWM_CONF)
    mcpwmSym_PRIMARY_TIMEBASE_CONF.setLabel("Primary Time Base Configurations")

    mcpwmSym_PTCON_PCLKDIV = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PTCON", "PCLKDIV", mcpwmSym_PRIMARY_TIMEBASE_CONF, True)
    ptconDepList.append("PTCON__PCLKDIV")

    mcpwm_PTPER_PTPER = mcpwmComponent.createIntegerSymbol("PTPER__PTPER", mcpwmSym_PRIMARY_TIMEBASE_CONF)
    mcpwm_PTPER_PTPER.setLabel("Primary Master Time Base Period")
    mcpwm_PTPER_PTPER.setDefaultValue(2000)
    mcpwm_PTPER_PTPER.setMin(0)
    mcpwm_PTPER_PTPER.setMax(pow(2, 16) - 1)

    mcpwmSym_PRI_FREQUENCY = mcpwmComponent.createFloatSymbol("MCPWM_PRI_FREQ", mcpwmSym_PRIMARY_TIMEBASE_CONF)
    mcpwmSym_PRI_FREQUENCY.setLabel("Primary Frequency (Hz)")
    mcpwmSym_PRI_FREQUENCY.setVisible(False)
    mcpwmSym_PRI_FREQUENCY.setReadOnly(True)
    div = pow(2, int(mcpwmSym_PTCON_PCLKDIV.getValue()))
    period = mcpwm_PTPER_PTPER.getValue()
    mcpwmSym_PRI_FREQUENCY.setDefaultValue((float(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / div) / period)
    mcpwmSym_PRI_FREQUENCY.setDependencies(mcpwmFreqCalc, ["core.CPU_CLOCK_FREQUENCY", "PTCON__PCLKDIV", "PTPER__PTPER"])

    mcpwmSym_PTCON_SEVTPS = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PTCON", "SEVTPS", mcpwmSym_PRIMARY_TIMEBASE_CONF, True)
    ptconDepList.append("PTCON__SEVTPS")

    mcpwm_SEVTCMP_SEVTCMP = mcpwmComponent.createIntegerSymbol("SEVTCMP_SEVTCMP", mcpwmSym_PRIMARY_TIMEBASE_CONF)
    mcpwm_SEVTCMP_SEVTCMP.setLabel("Primary Special Event Compare")
    mcpwm_SEVTCMP_SEVTCMP.setDefaultValue(10)
    mcpwm_SEVTCMP_SEVTCMP.setMin(0)
    mcpwm_SEVTCMP_SEVTCMP.setMax(pow(2, 16) - 1)

    mcpwmSym_PTCON_SEIEN = mcpwmComponent.createBooleanSymbol("PTCON__SEIEN", mcpwmSym_PRIMARY_TIMEBASE_CONF)
    mcpwmSym_PTCON_SEIEN.setLabel("Primary Special Event Interrupt Enable")
    mcpwmSym_PTCON_SEIEN.setDefaultValue(False)
    ptconDepList.append("PTCON__SEIEN")

    #Secondary Time base
    mcpwmSym_SECONDARY_TIMEBASE_CONF = mcpwmComponent.createMenuSymbol("MCPWM_SEC_TIMEBASE_CONF", mcpwmSym_PWM_CONF)
    mcpwmSym_SECONDARY_TIMEBASE_CONF.setLabel("Secondary Time Base Configurations")

    mcpwmSym_STCON_SCLKDIV = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "STCON", "SCLKDIV", mcpwmSym_SECONDARY_TIMEBASE_CONF, True)
    stconDepList.append("STCON__SCLKDIV")

    mcpwm_STPER_STPER = mcpwmComponent.createIntegerSymbol("STPER__STPER", mcpwmSym_SECONDARY_TIMEBASE_CONF)
    mcpwm_STPER_STPER.setLabel("Secondary Master Time Base Period")
    mcpwm_STPER_STPER.setDefaultValue(2000)
    mcpwm_STPER_STPER.setMin(0)
    mcpwm_STPER_STPER.setMax(pow(2, 16) - 1)

    mcpwmSym_SEC_FREQUENCY = mcpwmComponent.createFloatSymbol("MCPWM_SEC_FREQ", mcpwmSym_SECONDARY_TIMEBASE_CONF)
    mcpwmSym_SEC_FREQUENCY.setLabel("Secondary Frequency (Hz)")
    mcpwmSym_SEC_FREQUENCY.setVisible(False)
    mcpwmSym_SEC_FREQUENCY.setReadOnly(True)
    div = pow(2, int(mcpwmSym_STCON_SCLKDIV.getValue()))
    period = mcpwm_STPER_STPER.getValue()
    mcpwmSym_SEC_FREQUENCY.setDefaultValue((float(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / div) / period)
    mcpwmSym_SEC_FREQUENCY.setDependencies(mcpwmFreqCalc, ["core.CPU_CLOCK_FREQUENCY", "STCON__SCLKDIV", "STPER__STPER"])

    mcpwmSym_STCON_SEVTPS = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "STCON", "SEVTPS", mcpwmSym_SECONDARY_TIMEBASE_CONF, True)
    stconDepList.append("STCON__SEVTPS")

    mcpwm_SSEVTCMP_SEVTCMP = mcpwmComponent.createIntegerSymbol("SSEVTCMP_SEVTCMP", mcpwmSym_SECONDARY_TIMEBASE_CONF)
    mcpwm_SSEVTCMP_SEVTCMP.setLabel("Secondary Special Event Compare")
    mcpwm_SSEVTCMP_SEVTCMP.setDefaultValue(10)
    mcpwm_SSEVTCMP_SEVTCMP.setMin(0)
    mcpwm_SSEVTCMP_SEVTCMP.setMax(pow(2, 16) - 1)

    mcpwmSym_STCON_SSEIEN = mcpwmComponent.createBooleanSymbol("STCON__SSEIEN", mcpwmSym_SECONDARY_TIMEBASE_CONF)
    mcpwmSym_STCON_SSEIEN.setLabel("Secondary Special Event Interrupt Enable")
    mcpwmSym_STCON_SSEIEN.setDefaultValue(False)
    stconDepList.append("STCON__SSEIEN")

    # channel configurations
    for channelID in range (1, mcpwmSym_NUM_CHANNELS.getValue() + 1):
        mcpwmSym_CHANNEL_MENU = mcpwmComponent.createBooleanSymbol("MCPWM_CHANNEL"+str(channelID), None)
        mcpwmSym_CHANNEL_MENU.setLabel("Enable PWM Channel " + str(channelID))

        mcpwmSym_CLOCK_ENABLE = mcpwmComponent.createStringSymbol("MCPWM_CH_CLOCK_ENABLE"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_CLOCK_ENABLE.setVisible(False)
        mcpwmSym_CLOCK_ENABLE.setDependencies(mcpwmChClockEnable, ["MCPWM_CHANNEL"+str(channelID)])

        # Clock Warning status
        mcpwmSym_ClkEnComment = mcpwmComponent.createCommentSymbol("MCPWM_CLOCK_ENABLE_COMMENT"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_ClkEnComment.setLabel("Warning!!! " + mcpwmInstanceName.getValue() + str(channelID) + " Clock is Disabled in Clock Manager")
        mcpwmSym_ClkEnComment.setVisible(False)
        mcpwmSym_ClkEnComment.setDependencies(updateMCPWMClockWarningStatus, ["core." + mcpwmInstanceName.getValue() + str(channelID) + "_CLOCK_ENABLE"])

        mcpwmSym_PWMCON_MTBS = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "MTBS", mcpwmSym_CHANNEL_MENU, True)
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__MTBS")
        mcpwmSym_PWMCON_ITB = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "ITB", mcpwmSym_CHANNEL_MENU, True)
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__ITB")
        mcpwmSym_PWMCON_PTDIR = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "PTDIR", mcpwmSym_CHANNEL_MENU, True)
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__PTDIR")
        mcpwmSym_PWMCON_ECAM = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "ECAM", mcpwmSym_CHANNEL_MENU, True)
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__ECAM")

        mcpwmSym_IOCON_SWAP = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "SWAP", mcpwmSym_CHANNEL_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__SWAP")

        num_outputs = _get_num_outputs(channelID)

        if (num_outputs == "1"):
            mcpwmSym_IOCON_PMOD = mcpwmComponent.createKeyValueSetSymbol("IOCON"+str(channelID)+"__PMOD", mcpwmSym_CHANNEL_MENU)
            mcpwmSym_IOCON_PMOD.setLabel("PWM x I/O Pin Mode bits")
            mcpwmSym_IOCON_PMOD.addKey("PWMxL output is held at logic 0 (adjusted by the POLL bit)", "0x3", "0x3")
            mcpwmSym_IOCON_PMOD.setOutputMode("Value")
            mcpwmSym_IOCON_PMOD.setReadOnly(True)
        else:
            mcpwmSym_IOCON_PMOD = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "PMOD", mcpwmSym_CHANNEL_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__PMOD")

        mcpwmSym_IOCON_POLH = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "POLH", mcpwmSym_CHANNEL_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__POLH")
        mcpwmSym_IOCON_POLL = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "POLL", mcpwmSym_CHANNEL_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__POLL")

        mcpwm_PHASE_PHASE = mcpwmComponent.createIntegerSymbol("PHASE"+str(channelID)+"__PHASE", mcpwmSym_CHANNEL_MENU)
        mcpwm_PHASE_PHASE.setLabel("Phase Shift")
        mcpwm_PHASE_PHASE.setDefaultValue(0)
        mcpwm_PHASE_PHASE.setMin(0)
        mcpwm_PHASE_PHASE.setMax(pow(2, 16) - 1)

        mcpwm_CH_PERIOD = mcpwmComponent.createIntegerSymbol("MCPWM_PERIOD_CH"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwm_CH_PERIOD.setLabel("PWM Period")
        mcpwm_CH_PERIOD.setDefaultValue(2000)
        mcpwm_CH_PERIOD.setMin(0)
        mcpwm_CH_PERIOD.setMax(pow(2, 16) - 1)
        mcpwm_CH_PERIOD.setReadOnly(True)
        mcpwm_CH_PERIOD.setDependencies(mcpwmPeriodCalc, ["PWMCON"+str(channelID)+"__ITB", "PWMCON"+str(channelID)+"__MTBS",
                "PWMCON"+str(channelID)+"__ECAM", "PTPER__PTPER", "STPER__STPER", "PHASE"+str(channelID)+"__PHASE"])

        freq = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / mcpwm_CH_PERIOD.getValue()
        mcpwmSym_PWM_FREQ = mcpwmComponent.createCommentSymbol("MCPWM_FREQ_CH"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_PWM_FREQ.setLabel("**** PWM Frequency is " + str(freq) + " Hz ****")
        mcpwmSym_PWM_FREQ.setDependencies(mcpwmChFreq, ["MCPWM_PERIOD_CH"+str(channelID), "core.CPU_CLOCK_FREQUENCY", \
            "PWMCON"+str(channelID)+"__ECAM", "PWMCON"+str(channelID)+"__MTBS", "PTCON__PCLKDIV", "STCON__SCLKDIV"])

        mcpwm_PDC_PDC = mcpwmComponent.createIntegerSymbol("PDC"+str(channelID)+"__PDC", mcpwmSym_CHANNEL_MENU)
        mcpwm_PDC_PDC.setLabel("Primary Duty Cycle")
        mcpwm_PDC_PDC.setDefaultValue(1000)
        mcpwm_PDC_PDC.setMin(0)
        mcpwm_PDC_PDC.setMax(pow(2, 16) - 1)
        mcpwm_PDC_PDC.setDependencies(mcpwmDutyMax, ["PWMCON"+str(channelID)+"__ITB", "PWMCON"+str(channelID)+"__MTBS",
                "PWMCON"+str(channelID)+"__ECAM", "PTPER__PTPER", "STPER__STPER", "PHASE"+str(channelID)+"__PHASE"])

        mcpwm_SDC_SDC = mcpwmComponent.createIntegerSymbol("SDC"+str(channelID)+"__SDC", mcpwmSym_CHANNEL_MENU)
        mcpwm_SDC_SDC.setLabel("Secondary Duty Cycle")
        mcpwm_SDC_SDC.setDefaultValue(500)
        mcpwm_SDC_SDC.setMin(0)
        mcpwm_SDC_SDC.setMax(pow(2, 16) - 1)
        mcpwm_SDC_SDC.setVisible(False)
        mcpwm_SDC_SDC.setDependencies(mcpwmDutyMax, ["PWMCON"+str(channelID)+"__ITB", "PWMCON"+str(channelID)+"__MTBS",
                "PWMCON"+str(channelID)+"__ECAM", "PTPER__PTPER", "STPER__STPER", "PHASE"+str(channelID)+"__PHASE"])

        mcpwmSym_PWMCON_PWMHIEN = mcpwmComponent.createBooleanSymbol("PWMCON"+str(channelID)+"__PWMHIEN", mcpwmSym_CHANNEL_MENU)
        mcpwmSym_PWMCON_PWMHIEN.setLabel("Enable Period Match Interrupt")
        mcpwmSym_PWMCON_PWMHIEN.setDefaultValue(False)
        evicDeplist[channelID - 1].append("PWMCON"+str(channelID)+"__PWMHIEN")
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__PWMHIEN")

        mcpwmSym_PWMCON_PWMLIEN = mcpwmComponent.createBooleanSymbol("PWMCON"+str(channelID)+"__PWMLIEN", mcpwmSym_CHANNEL_MENU)
        mcpwmSym_PWMCON_PWMLIEN.setLabel("Enable Zero Match Interrupt")
        mcpwmSym_PWMCON_PWMLIEN.setDefaultValue(False)
        evicDeplist[channelID - 1].append("PWMCON"+str(channelID)+"__PWMLIEN")
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__PWMLIEN")

        mcpwmSym_DEADTIME_MENU = mcpwmComponent.createMenuSymbol("MCPWM_DEADTIME"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_DEADTIME_MENU.setLabel("Dead Time")

        mcpwmSym_PWMCON_DTC = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "DTC", mcpwmSym_DEADTIME_MENU, True)
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__DTC")

        mcpwmSym_PWMCON_DTCP = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "PWMCON"+str(channelID), "DTCP", mcpwmSym_DEADTIME_MENU, False)
        mcpwmSym_PWMCON_DTCP.setDependencies(mcpwmDTCompensation, ["PWMCON"+str(channelID)+"__DTC"])
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__DTCP")

        mcpwm_DTR_DTR = mcpwmComponent.createIntegerSymbol("DTR"+str(channelID)+"__DTR", mcpwmSym_DEADTIME_MENU)
        mcpwm_DTR_DTR.setLabel("Leading Edge Dead Time")
        mcpwm_DTR_DTR.setDefaultValue(75)
        mcpwm_DTR_DTR.setMin(0)
        mcpwm_DTR_DTR.setMax(pow(2, 14) - 1)

        deadtime = (mcpwm_DTR_DTR.getValue() * 1000000.0) / float(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
        mcpwmSym_HIGH_DEADTIME = mcpwmComponent.createCommentSymbol("MCPWM_LEADING_DEADTIME"+str(channelID), mcpwmSym_DEADTIME_MENU)
        mcpwmSym_HIGH_DEADTIME.setLabel("**** Leading edge dead time is " +  str(deadtime) + " uS ****")
        mcpwmSym_HIGH_DEADTIME.setDependencies(mcpwmDeadTimeCalc, ["core.CPU_CLOCK_FREQUENCY", "DTR"+str(channelID)+"__DTR"])

        mcpwm_ALTDTR_ALTDTR = mcpwmComponent.createIntegerSymbol("ALTDTR"+str(channelID)+"__ALTDTR", mcpwmSym_DEADTIME_MENU)
        mcpwm_ALTDTR_ALTDTR.setLabel("Trailing Edge Dead Time")
        mcpwm_ALTDTR_ALTDTR.setDefaultValue(75)
        mcpwm_ALTDTR_ALTDTR.setMin(0)
        mcpwm_ALTDTR_ALTDTR.setMax(pow(2, 14) - 1)

        deadtime = (mcpwm_ALTDTR_ALTDTR.getValue() * 1000000.0) / float(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
        mcpwmSym_LOW_DEADTIME = mcpwmComponent.createCommentSymbol("MCPWM_TRAILING_DEADTIME"+str(channelID), mcpwmSym_DEADTIME_MENU)
        mcpwmSym_LOW_DEADTIME.setLabel("**** Trailing edge dead time is " +  str(deadtime) + " uS ****")
        mcpwmSym_LOW_DEADTIME.setDependencies(mcpwmDeadTimeCalc, ["core.CPU_CLOCK_FREQUENCY", "ALTDTR"+str(channelID)+"__ALTDTR"])

        mcpwm_DTCOMP_DTCOMP = mcpwmComponent.createIntegerSymbol("DTCOMP"+str(channelID)+"__DTCOMP", mcpwmSym_DEADTIME_MENU)
        mcpwm_DTCOMP_DTCOMP.setLabel("Dead Time Compensation Value")
        mcpwm_DTCOMP_DTCOMP.setDefaultValue(75)
        mcpwm_DTCOMP_DTCOMP.setMin(0)
        mcpwm_DTCOMP_DTCOMP.setMax(pow(2, 14) - 1)
        mcpwm_DTCOMP_DTCOMP.setVisible(False)
        mcpwm_DTCOMP_DTCOMP.setDependencies(mcpwmDTCompensation, ["PWMCON"+str(channelID)+"__DTC"])

        mcpwmSym_TRIGGER_MENU = mcpwmComponent.createMenuSymbol("MCPWM_TRIGGER"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_TRIGGER_MENU.setLabel("Trigger Configurations")

        mcpwmSym_TRGCON_TRGDIV = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "TRGCON"+str(channelID), "TRGDIV", mcpwmSym_TRIGGER_MENU, True)

        mcpwmSym_TRGCON_TRGSEL = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "TRGCON"+str(channelID), "TRGSEL", mcpwmSym_TRIGGER_MENU, True)
        mcpwmSym_TRGCON_DTM = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "TRGCON"+str(channelID), "DTM", mcpwmSym_TRIGGER_MENU, True)

        mcpwm_TRIG_TRGCMP = mcpwmComponent.createIntegerSymbol("TRIG"+str(channelID)+"__TRGCMP", mcpwmSym_TRIGGER_MENU)
        mcpwm_TRIG_TRGCMP.setLabel("Primary Trigger Value")
        mcpwm_TRIG_TRGCMP.setDefaultValue(0)
        mcpwm_TRIG_TRGCMP.setMin(0)
        mcpwm_TRIG_TRGCMP.setMax(pow(2, 16) - 1)

        mcpwmSym_TRGCON_STRGSEL = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "TRGCON"+str(channelID), "STRGSEL", mcpwmSym_TRIGGER_MENU, True)

        mcpwm_STRIG_STRGCMP = mcpwmComponent.createIntegerSymbol("STRIG"+str(channelID)+"__STRGCMP", mcpwmSym_TRIGGER_MENU)
        mcpwm_STRIG_STRGCMP.setLabel("Secondary Trigger Value")
        mcpwm_STRIG_STRGCMP.setDefaultValue(0)
        mcpwm_STRIG_STRGCMP.setMin(0)
        mcpwm_STRIG_STRGCMP.setMax(pow(2, 16) - 1)

        mcpwmSym_PWMCON_TRIGIEN = mcpwmComponent.createBooleanSymbol("PWMCON"+str(channelID)+"__TRGIEN", mcpwmSym_TRIGGER_MENU)
        mcpwmSym_PWMCON_TRIGIEN.setLabel("Enable Trigger Interrupt")
        mcpwmSym_PWMCON_TRIGIEN.setDefaultValue(False)
        evicDeplist[channelID - 1].append("PWMCON"+str(channelID)+"__TRGIEN")
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__TRGIEN")

        mcpwmSym_FAULT_MENU = mcpwmComponent.createMenuSymbol("MCPWM_FAULT_MENU"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_FAULT_MENU.setLabel("Fault Configurations")

        mcpwmSym_IOCON_FLTSRC = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "FLTSRC", mcpwmSym_FAULT_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__FLTSRC")
        mcpwmSym_IOCON_FLTMOD = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "FLTMOD", mcpwmSym_FAULT_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__FLTMOD")
        mcpwmSym_IOCON_FLTPOL = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "FLTPOL", mcpwmSym_FAULT_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__FLTPOL")

        mcpwmSym_IOCON_FLTDAT_PWMH = mcpwmComponent.createKeyValueSetSymbol("IOCON"+str(channelID)+"__FLTDAT_PWMH", mcpwmSym_FAULT_MENU)
        mcpwmSym_IOCON_FLTDAT_PWMH.setLabel("PWMH State")
        mcpwmSym_IOCON_FLTDAT_PWMH.addKey("Low", "0", "Low")
        mcpwmSym_IOCON_FLTDAT_PWMH.addKey("High", "1", "High")
        mcpwmSym_IOCON_FLTDAT_PWMH.setOutputMode("Value")
        mcpwmSym_IOCON_FLTDAT_PWMH.setDisplayMode("Key")
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__FLTDAT_PWMH")

        mcpwmSym_IOCON_FLTDAT_PWML = mcpwmComponent.createKeyValueSetSymbol("IOCON"+str(channelID)+"__FLTDAT_PWML", mcpwmSym_FAULT_MENU)
        mcpwmSym_IOCON_FLTDAT_PWML.setLabel("PWML State")
        mcpwmSym_IOCON_FLTDAT_PWML.addKey("Low", "0", "Low")
        mcpwmSym_IOCON_FLTDAT_PWML.addKey("High", "1", "High")
        mcpwmSym_IOCON_FLTDAT_PWML.setOutputMode("Value")
        mcpwmSym_IOCON_FLTDAT_PWML.setDisplayMode("Key")
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__FLTDAT_PWML")

        mcpwmSym_PWMCON_FLTIEN = mcpwmComponent.createBooleanSymbol("PWMCON"+str(channelID)+"__FLTIEN", mcpwmSym_FAULT_MENU)
        mcpwmSym_PWMCON_FLTIEN.setLabel("Enable Fault Interrupt")
        mcpwmSym_PWMCON_FLTIEN.setDefaultValue(False)
        evicDeplist[channelID - 1].append("PWMCON"+str(channelID)+"__FLTIEN")
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__FLTIEN")

        mcpwmSym_CURLIM_MENU = mcpwmComponent.createMenuSymbol("MCPWM_CURLIM_MENU"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_CURLIM_MENU.setLabel("Current Limit Configurations")

        mcpwmSym_IOCON_CLSRC = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "CLSRC", mcpwmSym_CURLIM_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__CLSRC")
        mcpwmSym_IOCON_CLMOD = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "CLMOD", mcpwmSym_CURLIM_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__CLMOD")
        mcpwmSym_IOCON_CLPOL = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "IOCON"+str(channelID), "CLPOL", mcpwmSym_CURLIM_MENU, True)
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__CLPOL")

        mcpwmSym_IOCON_CLDAT_PWMH = mcpwmComponent.createKeyValueSetSymbol("IOCON"+str(channelID)+"__CLDAT_PWMH", mcpwmSym_CURLIM_MENU)
        mcpwmSym_IOCON_CLDAT_PWMH.setLabel("PWMH State")
        mcpwmSym_IOCON_CLDAT_PWMH.addKey("Low", "0", "Low")
        mcpwmSym_IOCON_CLDAT_PWMH.addKey("High", "1", "High")
        mcpwmSym_IOCON_CLDAT_PWMH.setOutputMode("Value")
        mcpwmSym_IOCON_CLDAT_PWMH.setDisplayMode("Key")
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__CLDAT_PWMH")

        mcpwmSym_IOCON_CLDAT_PWML = mcpwmComponent.createKeyValueSetSymbol("IOCON"+str(channelID)+"__CLDAT_PWML", mcpwmSym_CURLIM_MENU)
        mcpwmSym_IOCON_CLDAT_PWML.setLabel("PWML State")
        mcpwmSym_IOCON_CLDAT_PWML.addKey("Low", "0", "Low")
        mcpwmSym_IOCON_CLDAT_PWML.addKey("High", "1", "High")
        mcpwmSym_IOCON_CLDAT_PWML.setOutputMode("Value")
        mcpwmSym_IOCON_CLDAT_PWML.setDisplayMode("Key")
        ioconDepList[channelID - 1].append("IOCON"+str(channelID)+"__CLDAT_PWML")

        mcpwmSym_PWMCON_CLIEN = mcpwmComponent.createBooleanSymbol("PWMCON"+str(channelID)+"__CLIEN", mcpwmSym_CURLIM_MENU)
        mcpwmSym_PWMCON_CLIEN.setLabel("Enable Current Limit Interrupt")
        mcpwmSym_PWMCON_CLIEN.setDefaultValue(False)
        evicDeplist[channelID - 1].append("PWMCON"+str(channelID)+"__CLIEN")
        pwmconDepList[channelID - 1].append("PWMCON"+str(channelID)+"__CLIEN")

        mcpwmSym_LEB_MENU = mcpwmComponent.createMenuSymbol("MCPWM_LEB_MENU"+str(channelID), mcpwmSym_CHANNEL_MENU)
        mcpwmSym_LEB_MENU.setLabel("Leading Edge Blanking Configurations")

        mcpwmSym_LEBCON_CLLENBEN = mcpwmComponent.createBooleanSymbol("LEBCON"+str(channelID)+"__CLLENBEN", mcpwmSym_LEB_MENU)
        mcpwmSym_LEBCON_CLLENBEN.setLabel("Enable Leading Edge Blanking for Current Limit Input")
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__CLLENBEN")

        mcpwmSym_LEBCON_FLTLENBEN = mcpwmComponent.createBooleanSymbol("LEBCON"+str(channelID)+"__FLTLEBEN", mcpwmSym_LEB_MENU)
        mcpwmSym_LEBCON_FLTLENBEN.setLabel("Enable Leading Edge Blanking for Fault Input")
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__FLTLEBEN")

        mcpwmSym_LEBCON_PLF = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "LEBCON"+str(channelID), "PLF", mcpwmSym_LEB_MENU, True)
        mcpwmSym_LEBCON_PLR = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "LEBCON"+str(channelID), "PLR", mcpwmSym_LEB_MENU, True)
        mcpwmSym_LEBCON_PHF = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "LEBCON"+str(channelID), "PHF", mcpwmSym_LEB_MENU, True)
        mcpwmSym_LEBCON_PHR = mcpwmAddKeyValueSetFromATDFInitValue(mcpwmComponent, Module, "LEBCON"+str(channelID), "PHR", mcpwmSym_LEB_MENU, True)
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__PLF")
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__PLR")
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__PHF")
        lebconDepList[channelID - 1].append("LEBCON"+str(channelID)+"__PHR")

        mcpwmSym_LEBDLY = mcpwmComponent.createIntegerSymbol("LEBDLY"+str(channelID)+"__LEB", mcpwmSym_LEB_MENU)
        mcpwmSym_LEBDLY.setLabel("Leading Edge Blanking Delay")
        mcpwmSym_LEBDLY.setDefaultValue(10)
        mcpwmSym_LEBDLY.setMin(0)
        mcpwmSym_LEBDLY.setMax(pow(2, 12) - 1)

############################################################################
#### Dependency ####
############################################################################

    mcpwmSym_PTCON = mcpwmComponent.createHexSymbol("MCPWM_PTCON", None)
    mcpwmSym_PTCON.setVisible(False)
    mcpwmSym_PTCON.setDependencies(mcpwmCalcPTCON, ptconDepList)

    mcpwmSym_SPECIAL_EVIC = mcpwmComponent.createStringSymbol("MCPWM_SPECIAL_EVIC", None)
    mcpwmSym_SPECIAL_EVIC.setVisible(False)
    mcpwmSym_SPECIAL_EVIC.setDependencies(mcpwmSpecialInterruptSet, ["PTCON__SEIEN", "STCON__SSEIEN"])

    mcpwmSym_STCON = mcpwmComponent.createHexSymbol("MCPWM_STCON", None)
    mcpwmSym_STCON.setVisible(False)
    mcpwmSym_STCON.setDependencies(mcpwmCalcSTCON, stconDepList)

    #Calculate the proper interrupt registers using IRQ#
    irqString = "PWM_PRI"
    icxIrq_index = int(getIRQnumber(irqString))
    statRegName = _get_statReg_parms(icxIrq_index)
    enblRegName = _get_enblReg_parms(icxIrq_index)

    #IFS REG
    mcpwmSym_IFS_PRI = mcpwmComponent.createStringSymbol("MCPWM_IFS_PRI", None)
    mcpwmSym_IFS_PRI.setDefaultValue(statRegName)
    mcpwmSym_IFS_PRI.setVisible(False)

    #IEC REG
    mcpwmSym_IEC_PRI = mcpwmComponent.createStringSymbol("MCPWM_IEC_PRI", None)
    mcpwmSym_IEC_PRI.setDefaultValue(enblRegName)
    mcpwmSym_IEC_PRI.setVisible(False)

    #Calculate the proper interrupt registers using IRQ#
    irqString = "PWM_SEC"
    icxIrq_index = int(getIRQnumber(irqString))
    statRegName = _get_statReg_parms(icxIrq_index)
    enblRegName = _get_enblReg_parms(icxIrq_index)

    #IFS REG
    mcpwmSym_IFS_SEC = mcpwmComponent.createStringSymbol("MCPWM_IFS_SEC", None)
    mcpwmSym_IFS_SEC.setDefaultValue(statRegName)
    mcpwmSym_IFS_SEC.setVisible(False)

    #IEC REG
    mcpwmSym_IEC_SEC = mcpwmComponent.createStringSymbol("MCPWM_IEC_SEC", None)
    mcpwmSym_IEC_SEC.setDefaultValue(str(enblRegName))
    mcpwmSym_IEC_SEC.setVisible(False)

    for channelID in range (1, mcpwmSym_NUM_CHANNELS.getValue() + 1):
        mcpwmSym_PWMCON = mcpwmComponent.createHexSymbol("MCPWM_PWMCON"+str(channelID), None)
        mcpwmSym_PWMCON.setVisible(False)
        mcpwmSym_PWMCON.setDependencies(mcpwmCalcPWMCON, pwmconDepList[channelID - 1])

        mcpwmSym_IOCON = mcpwmComponent.createHexSymbol("MCPWM_IOCON"+str(channelID), None)
        mcpwmSym_IOCON.setVisible(False)
        num_outputs = _get_num_outputs(channelID)
        if (num_outputs == "1"):
            mcpwmSym_IOCON.setValue(0xcc00, 2)
        else:
            mcpwmSym_IOCON.setValue(0xc000, 2)
        mcpwmSym_IOCON.setDependencies(mcpwmCalcIOCON, ioconDepList[channelID - 1])

        mcpwmSym_LEBCON = mcpwmComponent.createHexSymbol("MCPWM_LEBCON"+str(channelID), None)
        mcpwmSym_LEBCON.setVisible(False)
        mcpwmSym_LEBCON.setDependencies(mcpwmCalcLEBCON, lebconDepList[channelID - 1])

        mcpwmSym_EVIC = mcpwmComponent.createIntegerSymbol("MCPWM_EVIC"+str(channelID), None)
        mcpwmSym_EVIC.setVisible(False)
        mcpwmSym_EVIC.setDependencies(mcpwmInterruptSet, evicDeplist[channelID - 1])

        #Calculate the proper interrupt registers using IRQ#
        irqString = "PWM" + str(channelID)
        icxIrq_index = int(getIRQnumber(irqString))
        statRegName = _get_statReg_parms(icxIrq_index)
        enblRegName = _get_enblReg_parms(icxIrq_index)

        #IFS REG
        mcpwmSym_IFS = mcpwmComponent.createStringSymbol("MCPWM_IFS_REG"+str(channelID), None)
        mcpwmSym_IFS.setDefaultValue(statRegName)
        mcpwmSym_IFS.setVisible(False)

        #IEC REG
        mcpwmSym_IEC = mcpwmComponent.createStringSymbol("MCPWM_IEC_REG"+str(channelID), None)
        mcpwmSym_IEC.setDefaultValue(enblRegName)
        mcpwmSym_IEC.setVisible(False)
############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    mcpwmHeaderFile = mcpwmComponent.createFileSymbol("MCPWM_COMMON_HEADER", None)
    mcpwmHeaderFile.setMarkup(True)
    mcpwmHeaderFile.setSourcePath("../peripheral/mcpwm_01477/templates/plib_mcpwm_common.h.ftl")
    mcpwmHeaderFile.setOutputName("plib_mcpwm_common.h")
    mcpwmHeaderFile.setDestPath("peripheral/mcpwm/")
    mcpwmHeaderFile.setProjectPath("config/" + configName + "/peripheral/mcpwm/")
    mcpwmHeaderFile.setType("HEADER")
    mcpwmHeaderFile.setOverwrite(True)

    mcpwmHeader1File = mcpwmComponent.createFileSymbol("MCPWM_HEADER1", None)
    mcpwmHeader1File.setMarkup(True)
    mcpwmHeader1File.setSourcePath("../peripheral/mcpwm_01477/templates/plib_mcpwm.h.ftl")
    mcpwmHeader1File.setOutputName("plib_" + mcpwmInstanceName.getValue().lower() + ".h")
    mcpwmHeader1File.setDestPath("peripheral/mcpwm/")
    mcpwmHeader1File.setProjectPath("config/" + configName + "/peripheral/mcpwm/")
    mcpwmHeader1File.setType("HEADER")
    mcpwmHeader1File.setOverwrite(True)

    mcpwmSource1File = mcpwmComponent.createFileSymbol("MCPWM_SOURCE1", None)
    mcpwmSource1File.setMarkup(True)
    mcpwmSource1File.setSourcePath("../peripheral/mcpwm_01477/templates/plib_mcpwm.c.ftl")
    mcpwmSource1File.setOutputName("plib_" + mcpwmInstanceName.getValue().lower() + ".c")
    mcpwmSource1File.setDestPath("peripheral/mcpwm/")
    mcpwmSource1File.setProjectPath("config/" + configName + "/peripheral/mcpwm/")
    mcpwmSource1File.setType("SOURCE")
    mcpwmSource1File.setOverwrite(True)

    mcpwmSystemInitFile = mcpwmComponent.createFileSymbol("MCPWM_INIT", None)
    mcpwmSystemInitFile.setType("STRING")
    mcpwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    mcpwmSystemInitFile.setSourcePath("../peripheral/mcpwm_01477/templates/system/initialization.c.ftl")
    mcpwmSystemInitFile.setMarkup(True)

    mcpwmSystemDefFile = mcpwmComponent.createFileSymbol("MCPWM_DEF", None)
    mcpwmSystemDefFile.setType("STRING")
    mcpwmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    mcpwmSystemDefFile.setSourcePath("../peripheral/mcpwm_01477/templates/system/definitions.h.ftl")
    mcpwmSystemDefFile.setMarkup(True)
