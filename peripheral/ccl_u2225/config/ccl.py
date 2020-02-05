# coding: utf-8
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

global interruptVector
global interruptHandler
global interruptHandlerLock
global symLutctrlEnableName
global shiftDict
global CCLfilesArray
CCLfilesArray = []

def fileUpdate(symbol, event):
    global CCLfilesArray
    if event["value"] == False:
        CCLfilesArray[0].setSecurity("SECURE")
        CCLfilesArray[1].setSecurity("SECURE")
        CCLfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        CCLfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")

    else:
        CCLfilesArray[0].setSecurity("NON_SECURE")
        CCLfilesArray[1].setSecurity("NON_SECURE")
        CCLfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        CCLfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")


def cclATDFRegisterGroupPath(ModuleName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]')
    return labelPath

def cclATDFRegisterPath(ModuleName, RegisterName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]')
    return labelPath

def cclATDFRegisterBitfieldPath(ModuleName, RegisterName, BitfieldName):
    labelPath = str('/avr-tools-device-file/modules/module@[name="' +
        ModuleName + '"]/register-group@[name="' + ModuleName +
        '"]/register@[name="' + RegisterName + '"]/bitfield@[name="'
        + BitfieldName +'"]')
    return labelPath

def cclATDFValueGroupPath(ModuleName, ValueGroupName):
    value_groupPath = str('/avr-tools-device-file/modules/module@[name="'
        + ModuleName + '"]/value-group@[name="' + ValueGroupName + '"]')
    return value_groupPath

def clcATDFValueGroupValuePath(ModuleName, ValueGroupName, ValueString):
    valuePath = str('/avr-tools-device-file/modules/module@[name="' + ModuleName
        + '"]/value-group@[name="' + ValueGroupName + '"]/value@[value="' +
        ValueString + '"]')
    return valuePath

def getBitfieldNames(node, outputList):
    '''
    Parse through the value fields of the value-group given by node.
    It looks at each value for a value attribute and a caption attribute.
    It ignores those captions marked "reserved" and adds the rest to the
    outputList as desc and keys.  It then adds the associated value attribute
    to the same index of the outputList.
    All together, it creates a set of 'desc', 'key', and 'value' strings suitable
    for use in creating a KeyValueSet drop down box.    
    '''
    valueNodes = node.getChildren()
    for ii in valueNodes:
        dict = {}
        if(ii.getAttribute('caption').lower() != "reserved"):
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('name')
            value = ii.getAttribute('value')
            if(value[:2]=='0x'):
                temp = value[2:]
                tempint = int(temp,16)
            else:
                tempint = int(value)
            dict['value'] = str(tempint)
            # Log.writeInfoMessage("desc: " + dict['desc'] + " key: " + dict['key'] + " value: " + dict['value'])
            outputList.append(dict)

def findDefaultValue(bitfieldNode, initialRegValue):
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
    
def addKeyValueSetFromATDFInitValue(Parent, ModuleName, RegisterName, index, BitFieldName, Menu, Visibility):
    '''
    This creates a ValueKeySet symbol which results in a drop down box with a
    particular register's bitfield's caption and the key-value pairs from the
    associated value group.
    It assumes that the value-group is named [REGISTER]__[BITFIELD]
    
    Parent is the parent component to the newly created component.  In this case
    it is always adchsComponent.
    ModuleName is the name of the IP module within the ATDF file.
    RegisterName is the name of the register within which to find the needed
    bitfield in the ATDF file.
    BitFieldName is the name of the bitfield to create a drop down box for.
    Menu is the menu under which to create the new component.
    Visibility is wether or not to make the component visible.
    
    Within the ATDF file, it fins the following bitfield:
    /modules/module@[name="'+ModuleName+'"]/register-group@[name="
    '+ModuleName+'"]/register@[name="'+RegisterName+'"]/bitfield@[name="
    '+BitFieldName+'"]')
    It uses the "caption" attribute of this bitfield as the label for the
    keyValueSet.
    
    Within the ATDF file, it finds the value-group for the RegisterName / BitFieldName 
    given in the function call.  Within this value-group it uses the getBitfieldNames 
    function to get the Key-Value pairs.    
    '''
    Log.writeInfoMessage("Adding KeyValueSet " + ModuleName + " " + RegisterName
        + " " + BitFieldName)
    registerPath = cclATDFRegisterPath(ModuleName, RegisterName)
    registerNode = ATDF.getNode(registerPath)
    
    if registerNode is not None:
        labelPath = cclATDFRegisterBitfieldPath(ModuleName, RegisterName, BitFieldName)
        labelNode = ATDF.getNode(labelPath)
        if labelNode is not None:
            value_groupPath = cclATDFValueGroupPath(ModuleName, labelNode.getAttribute('values'))
            value_groupNode = ATDF.getNode(value_groupPath)
            if value_groupNode is not None:
                Component = Parent.createKeyValueSetSymbol(RegisterName + str(index) + '__' +
                    BitFieldName, Menu)
                cclValGrp_names = []
                getBitfieldNames(value_groupNode, cclValGrp_names)

                Component.setLabel(labelNode.getAttribute('caption'))
                Component.setOutputMode("Value")
                Component.setDisplayMode("Description")
                for ii in cclValGrp_names:
                    Component.addKey( ii['key'], ii['value'],  ii['desc'] )
                initval = registerNode.getAttribute('initval')
                if initval is not None:
                    valuenode = value_groupNode.getChildren()  # look at all the <value ..> entries underneath <value-group >
                    Component.setDefaultValue(findDefaultValue(labelNode, initval))
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

def addMask(RegisterName, BitFieldName):
    # gathers information from atdf file for given bitfield for mask values, stores in shiftDict[] for later processing
    labelPath = cclATDFRegisterBitfieldPath('CCL', RegisterName, BitFieldName)
    labelNode = ATDF.getNode(labelPath)  
    dict = { 'regname':RegisterName, 'bitfield':labelNode.getAttribute('name'), 'mask':labelNode.getAttribute('mask')}
    shiftDict.append(dict)

def setEnable(symbol, event):
    cclCtrlEnable.setValue(int(event["value"]))
    # set the system CCL clock enable/disable accordingly
    if(event["value"]==1):
        Database.setSymbolValue("core", 'CCL_CLOCK_ENABLE', True, 2)
    else:
        Database.setSymbolValue("core", 'CCL_CLOCK_ENABLE', False, 2)
    
global findLsb
def findLsb(maskval):
    # finds the lsb of a mask value
    if(maskval==0):
        return None
    ii = 0
    while(((maskval & 1)!=1) and (ii<32)):
        maskval = maskval>>1
        ii += 1
    return ii
    
def findLimit(regBaseName):
    '''
    Finds the highest with a given base name, and returns that value.  Goal is to find 
    upper limit, as that can vary from device to device.
    '''
    groupPath = cclATDFRegisterGroupPath('CCL')
    minValue = 0
    node = ATDF.getNode(groupPath)
    if node is not None:
        for item in node.getChildren():
            if(regBaseName in item.getAttribute('name')):
                index = int(item.getAttribute('count'))
                if(minValue < index):
                    minValue = index
    return minValue
    
def hideMenu_clearValues(menu, event):
    '''
    This callback serves two purposes:  
        Hide/reveal menu entry based on CCL enable or LUTCTRLx enable menu settings
        
        Clear the LUTCTRLx register bitfield symbols when LUT enable for the block is set to False (this is for making the comments
        in the ftl file consistent with the register value in that case)
   
    '''
    menu.setVisible(event["value"])
    
    # Below is for when LUTCTRLx.ENABLE is cause for this callback.  See if set to disabled.
    if(('LUTCTRL' in event["id"]) and (event["value"]==0)):  # for sake of making ftl output clean, need to reset symbols to 0 if LUT block is disabled
        posn = event["id"].find("__")  # find which LUT block this callback was called for; we'll need it below
        if(posn != -1):
            lutBlock = int(event["id"][posn-1])  # the LUT block number is just before the underscore characters
            if(cclLuctrlInsel0[lutBlock].getValue()!=0):      # if statements here and below reduce time delay when deselecting LUT enable box
                cclLuctrlInsel0[lutBlock].setReadOnly(True)   # this setting of true/false is needed to make setValue() of symbol apply
                cclLuctrlInsel0[lutBlock].setReadOnly(False)
                cclLuctrlInsel0[lutBlock].setValue(0)
                cclLuctrlInsel0[lutBlock].clearValue()        # clearValue() removes the purple highlight indication from the menu
            if(cclLuctrlInsel1[lutBlock].getValue()!=0):
                cclLuctrlInsel1[lutBlock].setReadOnly(True) 
                cclLuctrlInsel1[lutBlock].setReadOnly(False)
                cclLuctrlInsel1[lutBlock].setValue(0)
                cclLuctrlInsel1[lutBlock].clearValue()
            if(cclLuctrlInsel2[lutBlock].getValue()!=0):
                cclLuctrlInsel2[lutBlock].setReadOnly(True) 
                cclLuctrlInsel2[lutBlock].setReadOnly(False)
                cclLuctrlInsel2[lutBlock].setValue(0)
                cclLuctrlInsel2[lutBlock].clearValue()
            if(cclLuctrlFiltsel[lutBlock].getValue()!=0):
                cclLuctrlFiltsel[lutBlock].setReadOnly(True) 
                cclLuctrlFiltsel[lutBlock].setReadOnly(False)
                cclLuctrlFiltsel[lutBlock].setValue(0)
                cclLuctrlFiltsel[lutBlock].clearValue()
            if(cclLuctrlLuteo[lutBlock].getValue()!=0):
                cclLuctrlLuteo[lutBlock].setReadOnly(True) 
                cclLuctrlLuteo[lutBlock].setReadOnly(False)
                cclLuctrlLuteo[lutBlock].setValue(0)
                cclLuctrlLuteo[lutBlock].clearValue()
            if(cclLuctrlLutei[lutBlock].getValue()!=0):
                cclLuctrlLutei[lutBlock].setReadOnly(True) 
                cclLuctrlLutei[lutBlock].setReadOnly(False)
                cclLuctrlLutei[lutBlock].setValue(0)
                cclLuctrlLutei[lutBlock].clearValue()
            if(cclLuctrlInvei[lutBlock].getValue()!=0):
                cclLuctrlInvei[lutBlock].setReadOnly(True) 
                cclLuctrlInvei[lutBlock].setReadOnly(False)
                cclLuctrlInvei[lutBlock].setValue(0)
                cclLuctrlInvei[lutBlock].clearValue()
            if(cclLuctrlTruth[lutBlock].getValue()!=0):
                cclLuctrlTruth[lutBlock].setReadOnly(True) 
                cclLuctrlTruth[lutBlock].setReadOnly(False)
                cclLuctrlTruth[lutBlock].setValue(0)
                cclLuctrlTruth[lutBlock].clearValue()
            if(cclLuctrlEdgesel[lutBlock].getValue()!=0):
                cclLuctrlEdgesel[lutBlock].setReadOnly(True)   
                cclLuctrlEdgesel[lutBlock].setReadOnly(False)
                cclLuctrlEdgesel[lutBlock].setValue(0)
                cclLuctrlEdgesel[lutBlock].clearValue()
        else:
            Log.writeErrorMessage("hideMenu_clearValues: invalid event id encountered")
    
def hideSequentialSelection(menu, event):
    '''
    Helper function, used to make sequential control menu items visible if at least 1 LUT block is enabled.
    There's no need to make sequential control visible if nothing that is input to them is enabled.
    '''
    component = menu.getComponent()
    menu.setVisible(False)
    if(component.getSymbolValue("CCL_ENABLE")==True): 
        # Poll all the inidividual LUT enables.  If any of them are True, then make SEQCTRLx registers visible
        for ii in range(0,lutSize):
            if(component.getSymbolValue(symLutctrlEnableName[ii]) == True):
                menu.setVisible(True)
                break
    
def cclCalcLUTCTRL(symbol, event):
    # This callback calculates the register value for LUTCTRLx.
    regValue = cclSym_LUTCTRL[int(event["id"][7])].getValue()
    # Compute which LUTCTRLx register this callback was called for.  It's in [7] of event id.
    lutBlock = int(event["id"][7],16)
    bitfieldName = event["id"][(int(event["id"].find('__'))+2):]   # last part of event id is the bitfield name

    if(bitfieldName == 'ENABLE'):
        if(cclLutctrlEnable[lutBlock].getValue() == 0):  # if disabled, clear entire register value
            regValue = 0
        else:
            regValue &= ~int(cclLutctrlEnable_mask,16)
            regValue += cclLutctrlEnable[lutBlock].getValue() << findLsb(int(cclLutctrlEnable_mask,16))
    elif(bitfieldName == 'FILTSEL'):
        regValue &= ~int(cclLuctrlFiltsel_mask,16)
        regValue += cclLuctrlFiltsel[lutBlock].getValue() << findLsb(int(cclLuctrlFiltsel_mask,16))
    elif(bitfieldName == 'EDGESEL'):
        regValue &= ~int(cclLuctrlEdgesel_mask,16)
        regValue += cclLuctrlEdgesel[lutBlock].getValue() << findLsb(int(cclLuctrlEdgesel_mask,16))
    elif(bitfieldName == 'INSEL0'):
        regValue &= ~int(cclLuctrlInsel0_mask,16)
        regValue += cclLuctrlInsel0[lutBlock].getValue() << findLsb(int(cclLuctrlInsel0_mask,16))
    elif(bitfieldName == 'INSEL1'):
        regValue &= ~int(cclLuctrlInsel1_mask,16)
        regValue += cclLuctrlInsel1[lutBlock].getValue() << findLsb(int(cclLuctrlInsel1_mask,16))
    elif(bitfieldName == 'INSEL2'):
        regValue &= ~int(cclLuctrlInsel2_mask,16)
        regValue += cclLuctrlInsel2[lutBlock].getValue() << findLsb(int(cclLuctrlInsel2_mask,16))
    elif(bitfieldName == 'INVEI'):
        regValue &= ~int(cclLuctrlInvei_mask,16)
        regValue += cclLuctrlInvei[lutBlock].getValue() << findLsb(int(cclLuctrlInvei_mask,16))
    elif(bitfieldName == 'LUTEI'):
        regValue &= ~int(cclLuctrlLutei_mask,16)
        regValue += cclLuctrlLutei[lutBlock].getValue() << findLsb(int(cclLuctrlLutei_mask,16))
    elif(bitfieldName == 'LUTEO'):
        regValue &= ~int(cclLuctrlLuteo_mask,16)
        regValue += cclLuctrlLuteo[lutBlock].getValue() << findLsb(int(cclLuctrlLuteo_mask,16))
    elif(bitfieldName == 'TRUTH'):
        regValue &= ~int(cclLuctrlTruth_mask,16)
        regValue += cclLuctrlTruth[lutBlock].getValue() << findLsb(int(cclLuctrlTruth_mask,16))
    cclSym_LUTCTRL[int(event["id"][7])].setValue(regValue, 2)
    
def cclCalcSEQCTRL(symbol, event):
    # Callback for setting SEQCTRLx register values
    seqBlock = int(event["id"][7],16)  # block number is at position 7
    regValue = cclsym_SEQCTRL[int(event["id"][7])].getValue()
    regValue &= ~int(cclSeqctrlSeqsel_mask,16)
    regValue += cclSeqctrlSeqsel[seqBlock].getValue() << findLsb(int(cclSeqctrlSeqsel_mask,16))
    cclsym_SEQCTRL[int(event["id"][7])].setValue(regValue,2)

def cclCalcCTRL(symbol, event):
    # Callback for setting CTRL register values
    bitfieldName = event["id"][(int(event["id"].find('__'))+2):]   # last part of event id is the bitfield name
    regValue = cclsym_CTRL.getValue()

    if(bitfieldName == 'ENABLE'):
        regValue &= ~int(cclCtrlEnable_mask,16)
        regValue += cclCtrlEnable.getValue() << findLsb(int(cclCtrlEnable_mask,16))
    elif(bitfieldName == 'RUNSTDBY'):
        #regValue &= ~int(cclCtrlEnable_mask,16)  # clear the ENABLE bit as can't set RUNSTDBY bit if it's set
        regValue &= ~int(cclCtrlRunstdby_mask,16)
        regValue += cclCtrlRunstdby.getValue() << findLsb(int(cclCtrlRunstdby_mask,16))
    cclsym_CTRL.setValue(regValue,2)

def showWarningMenu(symbol, event):
    '''
    This shows the user a warning when a sequential logic block is to be used, but both LUTs going
    into it are not enabled.  To remind the user to fix the configuration issue prior to generating code.
    '''
    component = symbol.getComponent()
    symbol.setVisible(False)
    # event["id"][-9] indicates which LUT block caused this callback, which affects which sequential logic block to look at
    sequentialBlock = int(event["id"][-9]) / 2  # map the (calling) LUT block to sequential logic block
    lutList = [2*sequentialBlock, 2*sequentialBlock+1] # the LUTs that go into the sequential block we currently care about for this callback's call
    for ii in lutList:
        if((cclLutctrlEnable[ii].getValue() == False) and                               # LUT block is not enabled
           (component.getSymbolValue('SEQCTRL'+str(sequentialBlock)+'__SEQSEL')!=0) ):  # Sequential block is enabled
            symbol.setVisible(True)
            break

def updateShiftValues():
    '''
    Populates bitshift variables, for use with register value computations.  Bitshifts are taken from ATDF file, 
    since that's where they are defined.
    '''
    global cclLutctrlEnable_mask
    global cclLuctrlFiltsel_mask
    global cclLuctrlEdgesel_mask
    global cclLuctrlInsel0_mask
    global cclLuctrlInsel1_mask
    global cclLuctrlInsel2_mask
    global cclLuctrlInvei_mask
    global cclLuctrlLutei_mask
    global cclLuctrlLuteo_mask
    global cclLuctrlTruth_mask
    global cclSeqctrlSeqsel_mask
    global cclCtrlEnable_mask
    global cclCtrlRunstdby_mask

    for ii in shiftDict:
        if(ii['regname'][:7]=='LUTCTRL'):
            if(ii['bitfield']=='ENABLE'):
                cclLutctrlEnable_mask = ii['mask']
            elif(ii['bitfield']=='FILTSEL'):
                cclLuctrlFiltsel_mask = ii['mask']
            elif(ii['bitfield']=='EDGESEL'):
                cclLuctrlEdgesel_mask = ii['mask']
            elif(ii['bitfield']=='INSEL0'):
                cclLuctrlInsel0_mask = ii['mask']
            elif(ii['bitfield']=='INSEL1'):
                cclLuctrlInsel1_mask = ii['mask']
            elif(ii['bitfield']=='INSEL2'):
                cclLuctrlInsel2_mask = ii['mask']
            elif(ii['bitfield']=='INVEI'):
                cclLuctrlInvei_mask = ii['mask']
            elif(ii['bitfield']=='LUTEI'):
                cclLuctrlLutei_mask = ii['mask']
            elif(ii['bitfield']=='LUTEO'):
                cclLuctrlLuteo_mask = ii['mask']
            elif(ii['bitfield']=='TRUTH'):
                cclLuctrlTruth_mask = ii['mask']
        elif(ii['regname'][:7]=='SEQCTRL'):
            cclSeqctrlSeqsel_mask = ii['mask']
        elif(ii['regname'][:4]=='CTRL'):
            if(ii['bitfield']=='ENABLE'):
                cclCtrlEnable_mask = ii['mask']
            elif(ii['bitfield']=='RUNSTDBY'):
                cclCtrlRunstdby_mask = ii['mask']

def cclWarning(symbol, event):
    '''
    Generates a warning when GCLK_CCL clock is disabled but needs to be enabled for given CCL feature being used
    Any of the following require GCLK_CCL (taken from datasheet):
        GCLK_CCL is required when input events, a filter, an edge detector, or a sequential submodule is enabled.
    '''
    trigger = False
    for ii in range(0,lutSize):  # scan over all LUT blocks in CCL module seeing if anything needing the clock is set
        if(cclLutctrlEnable[ii].getValue() == True):
            if((cclLuctrlInsel0[ii].getValue() == 3) or (cclLuctrlInsel1[ii].getValue() == 3) or  # input is event type
               (cclLuctrlInsel2[ii].getValue() == 3) or                                           # input is event type
               (cclLuctrlEdgesel[ii].getValue() == 1) or                                          # edge detector is enabled
               (cclLuctrlFiltsel[ii].getValue() == 1) or (cclLuctrlFiltsel[ii].getValue() == 2)): # filter is enabled
                trigger = True
                break
    for ii in range(0,seqSize):  # scan over all sequential blocks in CCL module seeing if anything needing the clock is set
        if(cclSeqctrlSeqsel[ii].getValue() != 0):  # sequential logic is enabled
            trigger = True
            break

    if((Database.getSymbolValue("core", 'CCL_CLOCK_ENABLE') == False) and (trigger == True)):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def checkEdgeWarning(symbol, event):
    '''
    This is a callback function.
    Generates a warning message for case when the filter is disabled but edge selection is enabled.  According to the datasheet
    for when the edge selector is enabled, "In order to avoid unpredictable behavior, either the filter or synchronizer must be
    enabled."
    
    The warning message will be displayed when the error case occurs.
    '''
    if('ENABLE' in event["id"]):  # hide/visible for master enable checkbox in CCL menu
        symbol.setVisible(event["value"])
    else:  # only other way for this callback is if filter selection value was changed
        posn = event["id"].find("__")  # find which LUT block this callback was called for; we'll need it below
        if(posn != -1):
            lutBlock = int(event["id"][posn-1])
            if((cclLuctrlEdgesel[lutBlock].getValue()==1) and (cclLuctrlFiltsel[lutBlock].getValue()==0)):  # edge selector is enabled and filter is disabled
                cclLuctrlEdgeselWarning[lutBlock].setVisible(True)
            else:
                cclLuctrlEdgeselWarning[lutBlock].setVisible(False)
        else:
            Log.writeErrorMessage("checkEdgeWarning: invalid event id encountered")


def getDefaultValueNum(register, bitfield, value_group):
    '''
    Extracts the default value from 'initval' field of given value-group, based on register bitfield
    Input arguments:
        register - atdf node, register name to get the intial value
        bitfield - the bitfield in the register we are interested in (to get mask value from)
        value_group - atdf node, the value group from which we want

    Returns:
        default name of that bitfield
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
    value = str((initialValue & mask) >> bitPosn)  # has initial value of bitfield, shifted down to bit0
    return value

def computeRegValue(symbolList, maskList):
    '''
    Computes register value from constituent bitfield values.
    '''
    value = 0
    for ii in range(len(symbolList)):
        value = value + (int(symbolList[ii].getValue()) << findLsb(int(maskList[ii],16)))
    return value

def instantiateComponent(cclComponent):
    global cclInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    global canCoreClockInvalidSym
    global canTimeQuantaInvalidSym
    global cclCtrlEnable
    global cclCtrlEnable_mask
    global cclCtrlRunstdby
    global cclCtrlRunstdby_mask
    global cclLuctrlFiltsel
    global cclLuctrlFiltsel_mask
    global cclLuctrlEdgesel
    global cclLuctrlEdgeselWarning
    global cclLuctrlEdgesel_mask
    global cclLuctrlInsel0
    global cclLuctrlInsel0_mask
    global cclLuctrlInsel1
    global cclLuctrlInsel1_mask
    global cclLuctrlInsel2
    global cclLuctrlInsel2_mask
    global cclLuctrlInvei
    global cclLuctrlInvei_mask
    global cclLuctrlLutei
    global cclLuctrlLuteo
    global cclLuctrlLuteo_mask
    global cclLuctrlTruth
    global cclLuctrlTruth_mask
    global cclSym_LUTCTRL
    global symLutctrlEnableName
    global cclLutctrlEnable
    global cclLutctrlEnable_mask
    global shiftDict
    global cclsym_CTRL
    global cclsym_SEQCTRL
    global cclSeqctrlSeqsel
    global cclSeqctrlSeqsel_mask
    global lutSize
    global seqSize
    
    shiftDict = []

    cclInstanceName = cclComponent.createStringSymbol("CCL_INSTANCE_NAME", None)
    cclInstanceName.setVisible(False)
    cclInstanceName.setDefaultValue(cclComponent.getID().upper())
    print("Running " + cclInstanceName.getValue())

    # Enable for entire CCL module
    cclEnSymId = cclInstanceName.getValue() + "_ENABLE"
    cclEnable = cclComponent.createBooleanSymbol(cclEnSymId, None)
    cclEnable.setLabel("Enable CCL Module?")
    
    # CTRL register bitfields
    regName = "CTRL"
    fieldName = "ENABLE"
    cclCtrlEnable = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, 0, fieldName, None, False)
    cclCtrlEnable.setDependencies(setEnable,[cclEnSymId])
    addMask(regName, fieldName)
    
    fieldName = "RUNSTDBY"
    cclCtrlRunstdby = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, 0, fieldName, cclEnable, True)
    cclCtrlRunstdby.setDependencies(setEnable,[cclEnSymId])
    addMask(regName, fieldName)

    # SWRST mask value for use in ftl file
    fieldName = "SWRST"
    cclCtrlSwrstMask = cclComponent.createHexSymbol("CCL_CTRL_SWRST_MASK",None)
    labelPath = cclATDFRegisterBitfieldPath('CCL', regName, fieldName)
    labelNode = ATDF.getNode(labelPath)
    cclCtrlSwrstMask.setDefaultValue(int(labelNode.getAttribute('mask'),16))
    cclCtrlSwrstMask.setVisible(False)

    # register SEQCTRLx value for ftl file
    cclsym_CTRL = cclComponent.createHexSymbol("CCL_CTRL_REGVALUE", None)
    cclsym_CTRL.setVisible(False)
    cclsym_CTRL.setLabel("CTRL register value")
    cclsym_CTRL.setDependencies(cclCalcCTRL, ['CTRL0__RUNSTDBY','CTRL0__ENABLE'])

    cclWarningCclClk = cclComponent.createMenuSymbol('GCLK_CCL_WARNING', cclEnable)
    cclWarningCclClk.setLabel("*** Warning: GCLK_CCL clock needs to be enabled under Peripheral Clock Configuration of Clock menu ***")
    cclWarningCclClk.setVisible(False)
    
   
    # LUTCTRLx register bitfields    
    symLutctrlEnableName = []
    cclLutctrlEnable = []
    cclLuctrlInsel0 = []
    cclLuctrlInsel1 = []
    cclLuctrlInsel2 = []
    cclLuctrlEdgesel = []
    cclLuctrlEdgeselWarning = []
    cclLuctrlFiltsel = []
    cclLuctrlLuteo = []
    cclLuctrlLutei = []
    cclLuctrlInvei = []
    cclLuctrlTruth = []
    clccon_LUTCTRL_deplist = []
    cclSym_LUTCTRL = []
    cclSeqctrlWarning = []
    cclWarningCclClkDeplist = []
    cclSeqctrlDeplist = []

    lutSize = findLimit("LUTCTRL")
    numLutsPresent = cclComponent.createIntegerSymbol("NUM_LUT_BLOCKS", None)   # for use in ftl file
    numLutsPresent.setVisible(False)
    numLutsPresent.setDefaultValue(lutSize)
    cclSeqctrlDeplist.append(cclEnSymId)
        
    for lut in range(0,lutSize):  # scan over all LUTCTRLx registers available in device
        regName = "LUTCTRL"
        symLutctrlEnableName.append(lut)
        symLutctrlEnableName[lut] = "LUTCTRL"+str(lut)+"__ENABLE"
        cclSeqctrlDeplist.append(symLutctrlEnableName[lut])
        
        fieldName = "ENABLE"
        cclLutctrlEnable.append(lut)
        cclLutctrlEnable[lut] = cclComponent.createBooleanSymbol(symLutctrlEnableName[lut], cclEnable)
        cclLutctrlEnable[lut].setLabel("Enable LUT"+str(lut)+"?")
        cclLutctrlEnable[lut].setVisible(False)
        cclLutctrlEnable[lut].setDependencies(hideMenu_clearValues, [cclEnSymId])
        addMask(regName, fieldName)
        
        fieldName = "INSEL0"
        cclLuctrlInsel0.append(lut)
        cclLuctrlInsel0[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlInsel0[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        
        fieldName = "INSEL1"
        cclLuctrlInsel1.append(lut)
        cclLuctrlInsel1[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlInsel1[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        
        fieldName = "INSEL2"
        cclLuctrlInsel2.append(lut)
        cclLuctrlInsel2[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlInsel2[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        
        fieldName = "EDGESEL"
        cclLuctrlEdgesel.append(lut)
        cclLuctrlEdgesel[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlEdgesel[lut].setDependencies(checkEdgeWarning, [regName+'__EDGESEL', symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        

        # warning message if edge selection is enabled but filter selection is disabled
        cclLuctrlEdgeselWarning.append(lut)
        cclLuctrlEdgeselWarning[lut] = cclComponent.createMenuSymbol('EDGESEL_WARNING'+str(lut), cclEnable)
        cclLuctrlEdgeselWarning[lut].setVisible(False)
        cclLuctrlEdgeselWarning[lut].setLabel("***Warning: either the filter should be enabled or synchronizer on.  Unpredictable results may occur with filter off. ***")
            
        fieldName = "FILTSEL"
        cclLuctrlFiltsel.append(lut)
        cclLuctrlFiltsel[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlFiltsel[lut].setDependencies(checkEdgeWarning, [regName+'__FILTSEL',symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        
        fieldName = "LUTEO"
        cclLuctrlLuteo.append(lut)
        cclLuctrlLuteo[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlLuteo[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        
        fieldName = "LUTEI"
        cclLuctrlLutei.append(lut)
        cclLuctrlLutei[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlLutei[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        
        fieldName = "INVEI"
        cclLuctrlInvei.append(lut)
        cclLuctrlInvei[lut] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, lut, fieldName, cclLutctrlEnable[lut], False)
        cclLuctrlInvei[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)

        fieldName = "TRUTH"
        cclLuctrlTruth.append(lut)
        cclLuctrlTruth[lut] = cclComponent.createHexSymbol(regName+str(lut)+'__'+fieldName, cclLutctrlEnable[lut])
        cclLuctrlTruth[lut].setDefaultValue(0)
        cclLuctrlTruth[lut].setVisible(False)
        cclLuctrlTruth[lut].setLabel("Truth Table")
        cclLuctrlTruth[lut].setMin(0)
        cclLuctrlTruth[lut].setMax(255)
        cclLuctrlTruth[lut].setDependencies(hideMenu_clearValues, [symLutctrlEnableName[lut]])
        addMask(regName, fieldName)
        
        # register LUTCTRLx value for ftl file
        clccon_LUTCTRL_deplist.append(lut)
        clccon_LUTCTRL_deplist[lut] = [ regName+str(lut)+"__ENABLE", regName+str(lut)+"__FILTSEL", regName+str(lut)+"__EDGESEL",
                                regName+str(lut)+"__INSEL0", regName+str(lut)+"__INSEL1", regName+str(lut)+"__INSEL2", 
                                regName+str(lut)+"__INVEI", regName+str(lut)+"__LUTEI", regName+str(lut)+"__LUTEO",
                                regName+str(lut)+"__TRUTH" ]
        cclSym_LUTCTRL.append(lut)
        cclSym_LUTCTRL[lut] = cclComponent.createHexSymbol("CCL_LUTCTRL_REGVALUE"+str(lut), None)
        cclSym_LUTCTRL[lut].setLabel("LUTCTRL"+str(lut)+" register value")
        cclSym_LUTCTRL[lut].setVisible(False)
        cclSym_LUTCTRL[lut].setDependencies(cclCalcLUTCTRL, clccon_LUTCTRL_deplist[lut])
        
    # SEQCTRLx bitfield
    cclSeqctrlSeqsel = []
    cclsym_SEQCTRL = []
    seqSize = findLimit("SEQCTRL")
    numSeqsPresent = cclComponent.createIntegerSymbol("NUM_SEQUENTIAL_BLOCKS", None)
    numSeqsPresent.setVisible(False)
    numSeqsPresent.setDefaultValue(seqSize)
    
    for ii in range(0,seqSize):  # scan over all SEQCTRLx registers in device
        regName = "SEQCTRL"
        fieldName = "SEQSEL"
        cclSeqctrlSeqsel.append(ii)
        cclSeqctrlSeqsel[ii] = addKeyValueSetFromATDFInitValue(cclComponent, 'CCL', regName, ii, fieldName, cclEnable, True)
        cclSeqctrlSeqsel[ii].setDependencies(hideSequentialSelection, cclSeqctrlDeplist)
        addMask(regName, fieldName)
        cclWarningCclClkDeplist.append(regName+'__'+fieldName)
        
        # warning message for if sequential logic enabled AND not having both LUT outputs going into it enabled
        cclSeqctrlWarning.append(ii)
        cclSeqctrlWarning[ii] = cclComponent.createMenuSymbol(fieldName+str(ii)+'_WARNING', cclEnable)
        cclSeqctrlWarning[ii].setVisible(False)
        cclSeqctrlWarning[ii].setLabel("*** Warning: both LUT outputs need to be enabled if using sequential logic block "+str(ii)+" ***")
        cclSeqctrlWarning[ii].setDependencies(showWarningMenu, ["LUTCTRL"+str(2*ii)+"__ENABLE", "LUTCTRL"+str(2*ii+1)+"__ENABLE", "SEQCTRL"+str(ii)+"__SEQSEL"])

        # register SEQCTRLx value for ftl file
        cclsym_SEQCTRL.append(ii)
        cclsym_SEQCTRL[ii] = cclComponent.createHexSymbol("CCL_SEQCTRL_REGVALUE"+str(ii), None)
        cclsym_SEQCTRL[ii].setVisible(False)
        cclsym_SEQCTRL[ii].setLabel("SEQCTRL"+str(ii)+" register value")
        cclsym_SEQCTRL[ii].setDependencies(cclCalcSEQCTRL, ['SEQCTRL'+str(ii)+'__SEQSEL'])

    configName = Variables.get("__CONFIGURATION_NAME")

    # update bit shift values of individual bitfields - for use in register value computations that ftl file will use
    updateShiftValues()
    # since now have bit shifts of all bitfields, can now compute default values (based on atdf file 'initval' fields)
    cclsym_CTRL.setDefaultValue(computeRegValue([cclCtrlEnable, cclCtrlRunstdby], [cclCtrlEnable_mask, cclCtrlRunstdby_mask]))
    for lut in range(0,lutSize):  # scan over all LUTCTRLx registers available in device
        cclSym_LUTCTRL[lut].setDefaultValue(computeRegValue([cclLutctrlEnable[lut], cclLuctrlInsel0[lut], cclLuctrlInsel1[lut], cclLuctrlInsel2[lut],
                                                            cclLuctrlEdgesel[lut], cclLuctrlFiltsel[lut], cclLuctrlLuteo[lut], cclLuctrlLutei[lut], 
                                                            cclLuctrlInvei[lut], cclLuctrlTruth[lut]], 
                                                            [cclLutctrlEnable_mask, cclLuctrlInsel0_mask, cclLuctrlInsel1_mask, cclLuctrlInsel2_mask,
                                                            cclLuctrlEdgesel_mask, cclLuctrlFiltsel_mask, cclLuctrlLuteo_mask, cclLuctrlLutei_mask,
                                                            cclLuctrlInvei_mask, cclLuctrlTruth_mask]))
    for ii in range(0,seqSize):  # scan over all SEQCTRLx registers in device
        cclsym_SEQCTRL[ii].setDefaultValue(computeRegValue([cclSeqctrlSeqsel[ii]],[cclSeqctrlSeqsel_mask]))

    # dependencies are set so can link callback to them at this time
    cclWarningCclClkDeplist.append('core.CCL_CLOCK_ENABLE')
    cclWarningCclClk.setDependencies(cclWarning, cclWarningCclClkDeplist)
    
    #Instance Source File
    cclMainSourceFile = cclComponent.createFileSymbol("sourceFile", None)
    cclMainSourceFile.setSourcePath("../peripheral/ccl_u2225/templates/plib_ccl.c.ftl")
    cclMainSourceFile.setOutputName("plib_"+cclInstanceName.getValue().lower()+".c")
    cclMainSourceFile.setDestPath("/peripheral/ccl/")
    cclMainSourceFile.setProjectPath("config/" + configName + "/peripheral/ccl/")
    cclMainSourceFile.setType("SOURCE")
    cclMainSourceFile.setMarkup(True)

    #Instance Header File
    cclInstHeaderFile = cclComponent.createFileSymbol("instHeaderFile", None)
    cclInstHeaderFile.setSourcePath("../peripheral/ccl_u2225/templates/plib_ccl.h.ftl")
    cclInstHeaderFile.setOutputName("plib_"+cclInstanceName.getValue().lower()+".h")
    cclInstHeaderFile.setDestPath("/peripheral/ccl/")
    cclInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/ccl/")
    cclInstHeaderFile.setType("HEADER")
    cclInstHeaderFile.setMarkup(True)

    #CCL Initialize
    cclSystemInitFile = cclComponent.createFileSymbol("initFile", None)
    cclSystemInitFile.setType("STRING")
    cclSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS")
    cclSystemInitFile.setSourcePath("../peripheral/ccl_u2225/templates/system/initialization.c.ftl")
    cclSystemInitFile.setMarkup(True)

    #CCL definitions header
    cclSystemDefFile = cclComponent.createFileSymbol("defFile", None)
    cclSystemDefFile.setType("STRING")
    cclSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cclSystemDefFile.setSourcePath("../peripheral/ccl_u2225/templates/system/definitions.h.ftl")
    cclSystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global CCLfilesArray
        cclIsNonSecure = Database.getSymbolValue("core", cclComponent.getID().upper() + "_IS_NON_SECURE")
        cclSystemDefFile.setDependencies(fileUpdate, ["core." + cclComponent.getID().upper() + "_IS_NON_SECURE"])
        CCLfilesArray.append(cclMainSourceFile)
        CCLfilesArray.append(cclInstHeaderFile)
        CCLfilesArray.append(cclSystemInitFile)
        CCLfilesArray.append(cclSystemDefFile)
        if cclIsNonSecure == False:
            CCLfilesArray[0].setSecurity("SECURE")
            CCLfilesArray[1].setSecurity("SECURE")
            CCLfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            CCLfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
