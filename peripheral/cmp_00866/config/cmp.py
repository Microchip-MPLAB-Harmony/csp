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

################################################################################
#### Register Information ####
################################################################################
cmpValGrp_CM1CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CCH"]')
cmpValGrp_CM1CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CREF"]')
cmpValGrp_CM1CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__EVPOL"]')
cmpValGrp_CM2CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM2CON__CREF"]')
cmpValGrp_CM2CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM2CON__CCH"]')
cmpValGrp_CM2CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM2CON__EVPOL"]')

cmpBitFld_CM1CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CCH"]')
cmpBitFld_CM1CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CREF"]')
cmpBitFld_CM1CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="EVPOL"]')
cmpBitFld_CM1CON_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CPOL"]')
cmpBitFld_CM1CON_COE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="COE"]')

cmpBitFld_CM2CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CCH"]')
cmpBitFld_CM2CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CREF"]')
cmpBitFld_CM2CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="EVPOL"]')
cmpBitFld_CM2CON_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="CPOL"]')
cmpBitFld_CM2CON_COE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM2CON"]/bitfield@[name="COE"]')

################################################################################
#### Global Variables ####
################################################################################
global cmpInstanceName
global cmpSym_CM1CON_CREF
global cmpSym_CM1CON_CCH
global cmpSym_CM1CON_EVPOL
global cmpSym_CM1CON_CPOL
global cmpSym_CM1CON_COE
global cmpSym_CM2CON_CREF
global cmpSym_CM2CON_CCH
global cmpSym_CM2CON_EVPOL
global cmpSym_CM2CON_CPOL
global cmpSym_CM2CON_COE
global cmp1IPC_PriValue
global cmp1IPC_SubpriValue
global cmp2IPC_PriValue
global cmp2IPC_SubpriValue
global cmp1PriShift
global cmp1SubShift
global cmp2PriShift
global cmp2SubShift

################################################################################
#### Business Logic ####
################################################################################
def interruptControl(symbol, event):
    if (int(event["symbol"].getKeyValue(event["value"])) != 0):
        symbol.setValue(True, 2)
    else :
        symbol.setValue(False, 2)
	
def dependencyStatus(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        regName = "IEC"+str(index)
    return regName, str(bitPosn)
    
def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        regName = "IFS"+str(index)
    return regName, str(bitPosn)
    
def _get_sub_priority_parms(vectorNumber):
    # This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift, 
    # and subpriority bitmask for input vector number
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 4.0
        index = int(temp)
        subPrioBit = 8*(vectorNumber & 0x3)
        prioBit = subPrioBit + 2
        regName = "IPC"+str(index)
    return regName, str(prioBit), str(subPrioBit)

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
            outputList.append(dict)        

def combine1Values(symbol, event):
    cchValue   = cmpSym_CM1CON_CCH.getValue() << 0
    crefValue  = cmpSym_CM1CON_CREF.getValue() << 4
    evpolValue = cmpSym_CM1CON_EVPOL.getValue() << 6
    cpolValue  = cmpSym_CM1CON_CPOL.getValue() << 13
    coeValue   = cmpSym_CM1CON_COE.getValue() << 14
    cmconValue = crefValue + cchValue + evpolValue + cpolValue + coeValue
    symbol.setValue(cmconValue, 2)
    print cmconValue

def combine2Values(symbol, event):
    cchValue   = cmpSym_CM2CON_CCH.getValue() << 0
    crefValue  = cmpSym_CM2CON_CREF.getValue() << 4
    evpolValue = cmpSym_CM2CON_EVPOL.getValue() << 6
    cpolValue  = cmpSym_CM2CON_CPOL.getValue() << 13
    coeValue   = cmpSym_CM2CON_COE.getValue() << 14
    cmconValue = crefValue + cchValue + evpolValue + cpolValue + coeValue
    symbol.setValue(cmconValue, 2)
    print cmconValue


    
def getIRQnumber(string):
    interrupts = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts')
    interruptsChildren = interrupts.getChildren()
    for param in interruptsChildren:  
        modInst = param.getAttribute('module-instance')
        if(string == modInst):
            irq_index = param.getAttribute('index')
    return irq_index

def updateIRQValues(symbol, event):
    irqvalue = int(event["value"])
    symbol.setValue(irqvalue, 2)

def updateHandlerName(symbol, event):
    handlername = str(event["value"])
    symbol.setValue(handlername, 2)
    
################################################################################
#### Component ####
################################################################################
def instantiateComponent(cmpComponent):
    global cmpInstanceName
    global cmpSym_CM1CON_CREF
    global cmpSym_CM1CON_CCH
    global cmpSym_CM1CON_EVPOL
    global cmpSym_CM1CON_CPOL
    global cmpSym_CM1CON_COE
    global cmpSym_CM2CON_CREF
    global cmpSym_CM2CON_CCH
    global cmpSym_CM2CON_EVPOL
    global cmpSym_CM2CON_CPOL
    global cmpSym_CM2CON_COE
    global cmp1IPC_PriValue
    global cmp1IPC_SubpriValue
    global cmp2IPC_PriValue
    global cmp2IPC_SubpriValue
    global cmp1PriShift
    global cmp1SubShift
    global cmp2PriShift
    global cmp2SubShift

    cmpInstanceName = cmpComponent.createStringSymbol("CMP_INSTANCE_NAME", None)
    cmpInstanceName.setVisible(False)
    cmpInstanceName.setDefaultValue(cmpComponent.getID().upper())
    print("Running " + cmpInstanceName.getValue())

    cmpSym_CM1CON_STRING = cmpComponent.createCommentSymbol("CMP1_STRING", None)
    cmpSym_CM1CON_STRING.setLabel("Comparator 1")
    cmpSym_CM1CON_STRING.setVisible(True)

    cmp1CREF_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_CREF, cmp1CREF_names)
    cmpSym_CM1CON_CREF = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_CREF", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CREF.setLabel(cmpBitFld_CM1CON_CREF.getAttribute("caption"))
    cmpSym_CM1CON_CREF.setDefaultValue(0)
    cmpSym_CM1CON_CREF.setOutputMode("Value")
    cmpSym_CM1CON_CREF.setDisplayMode("Description")
    for ii in cmp1CREF_names:
        cmpSym_CM1CON_CREF.addKey( ii['desc'], ii['value'], ii['key'] )    
    cmpSym_CM1CON_CREF.setVisible(True)

    cmp1CCH_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_CCH, cmp1CCH_names)       
    cmpSym_CM1CON_CCH = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_CCH", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CCH.setLabel(cmpBitFld_CM1CON_CCH.getAttribute("caption"))
    cmpSym_CM1CON_CCH.setDefaultValue(0)
    cmpSym_CM1CON_CCH.setOutputMode("Value")
    cmpSym_CM1CON_CCH.setDisplayMode("Description")
    for ii in cmp1CCH_names:
        cmpSym_CM1CON_CCH.addKey( ii['desc'], ii['value'], ii['key'] ) 
    cmpSym_CM1CON_CCH.setVisible(True)

    cmp1EVPOL_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_EVPOL, cmp1EVPOL_names)
    cmpSym_CM1CON_EVPOL = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_EVPOL", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_EVPOL.setLabel(cmpBitFld_CM1CON_EVPOL.getAttribute("caption"))
    cmpSym_CM1CON_EVPOL.setDefaultValue(0)
    cmpSym_CM1CON_EVPOL.setOutputMode("Value")
    cmpSym_CM1CON_EVPOL.setDisplayMode("Description")
    for ii in cmp1EVPOL_names:
        cmpSym_CM1CON_EVPOL.addKey( ii['desc'], ii['value'], ii['key'] )
    cmpSym_CM1CON_EVPOL.setVisible(True)

    cmpSym_CM1CON_CPOL = cmpComponent.createBooleanSymbol("CMP_CM1CON_CPOL", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CPOL.setLabel(cmpBitFld_CM1CON_CPOL.getAttribute("caption"))
    cmpSym_CM1CON_CPOL.setDefaultValue(False)
    cmpSym_CM1CON_CPOL.setVisible(True)

    cmpSym_CM1CON_COE = cmpComponent.createBooleanSymbol("CMP_CM1CON_COE", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_COE.setLabel(cmpBitFld_CM1CON_COE.getAttribute("caption"))
    cmpSym_CM1CON_COE.setDefaultValue(False)
    cmpSym_CM1CON_COE.setVisible(True)

    cmpSym_CM2CON_STRING = cmpComponent.createCommentSymbol("CMP2_STRING", None)
    cmpSym_CM2CON_STRING.setLabel("Comparator 2")
    cmpSym_CM2CON_STRING.setVisible(True)

    cmp2CREF_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_CREF, cmp2CREF_names)
    cmpSym_CM2CON_CREF = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_CREF", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CREF.setLabel(cmpBitFld_CM2CON_CREF.getAttribute("caption"))
    cmpSym_CM2CON_CREF.setDefaultValue(0)
    cmpSym_CM2CON_CREF.setOutputMode("Value")
    cmpSym_CM2CON_CREF.setDisplayMode("Description")
    for ii in cmp2CREF_names:
        cmpSym_CM2CON_CREF.addKey( ii['desc'], ii['value'], ii['key'] )     
    cmpSym_CM2CON_CREF.setVisible(True)

    cmp2CCH_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_CCH, cmp2CCH_names)
    cmpSym_CM2CON_CCH = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_CCH", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CCH.setLabel(cmpBitFld_CM2CON_CCH.getAttribute("caption"))
    cmpSym_CM2CON_CCH.setDefaultValue(0)
    cmpSym_CM2CON_CCH.setOutputMode("Value")
    cmpSym_CM2CON_CCH.setDisplayMode("Description")
    for ii in cmp2CCH_names:
        cmpSym_CM2CON_CCH.addKey( ii['desc'], ii['value'], ii['key'] )     
    cmpSym_CM2CON_CCH.setVisible(True)

    cmp2EVPOL_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_EVPOL, cmp2EVPOL_names)    
    cmpSym_CM2CON_EVPOL = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_EVPOL", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_EVPOL.setLabel(cmpBitFld_CM2CON_EVPOL.getAttribute("caption"))
    cmpSym_CM2CON_EVPOL.setDefaultValue(0)
    cmpSym_CM2CON_EVPOL.setOutputMode("Value")
    cmpSym_CM2CON_EVPOL.setDisplayMode("Description")
    for ii in cmp2EVPOL_names:
        cmpSym_CM2CON_EVPOL.addKey( ii['desc'], ii['value'], ii['key'] )     
    cmpSym_CM2CON_EVPOL.setVisible(True)

    cmpSym_CM2CON_CPOL = cmpComponent.createBooleanSymbol("CMP_CM2CON_CPOL", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CPOL.setLabel(cmpBitFld_CM2CON_CPOL.getAttribute("caption"))
    cmpSym_CM2CON_CPOL.setDefaultValue(False)
    cmpSym_CM2CON_CPOL.setVisible(True)

    cmpSym_CM2CON_COE = cmpComponent.createBooleanSymbol("CMP_CM2CON_COE", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_COE.setLabel(cmpBitFld_CM2CON_COE.getAttribute("caption"))
    cmpSym_CM2CON_COE.setDefaultValue(False)
    cmpSym_CM2CON_COE.setVisible(True)

    #Collecting user input to combine into CMPxCON register
    #CMPxCON is updated every time a user selection changes
    cmpSym_CMP1CON = cmpComponent.createHexSymbol("CM1CON_VALUE", None)
    cmpSym_CMP1CON.setDefaultValue(0)
    cmpSym_CMP1CON.setVisible(False)
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_CREF"])
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_CCH"])
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_EVPOL"])    
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_CPOL"])
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_COE"])

    cmpSym_CMP2CON = cmpComponent.createHexSymbol("CM2CON_VALUE", None)
    cmpSym_CMP2CON.setDefaultValue(0)
    cmpSym_CMP2CON.setVisible(False)
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_CREF"])
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_CCH"])
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_EVPOL"])    
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_CPOL"])
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_COE"])

    #Calculate the proper interrupt registers using IRQ#
    cmp1Irq_index = int(getIRQnumber("COMPARATOR_1"))
    cmp1EnblRegName, enblBitPosn = _get_enblReg_parms(cmp1Irq_index)
    cmp1StatRegName, statBitPosn = _get_statReg_parms(cmp1Irq_index)
    cmp1PriRegName, cmp1PriShift, cmp1SubShift = _get_sub_priority_parms(cmp1Irq_index)

    #CMP1 IEC REG
    cmp1IEC = cmpComponent.createStringSymbol("CMP1_IEC_REG", None)
    cmp1IEC.setDefaultValue(cmp1EnblRegName)
    cmp1IEC.setVisible(False)

    #CMP1 IFS REG
    cmp1IFS = cmpComponent.createStringSymbol("CMP1_IFS_REG", None)
    cmp1IFS.setDefaultValue(cmp1StatRegName)
    cmp1IFS.setVisible(False)


    #CMP1 PRIORITY VALUE
    cmp1IPC_PriValue = cmpComponent.createHexSymbol("CMP1_IPC_PRI_VALUE", None)
    cmp1IPC_PriValue.setDefaultValue(7)
    cmp1IPC_PriValue.setVisible(False)
    cmp1IPC_PriValue.setDependencies(updateIRQValues, ["core.COMPARATOR_1_PRIORITY"])

    #CMP1 SUBPRIORITY VALUE
    cmp1IPC_SubpriValue = cmpComponent.createHexSymbol("CMP1_IPC_SUBPRI_VALUE", None)
    cmp1IPC_SubpriValue.setDefaultValue(3)
    cmp1IPC_SubpriValue.setVisible(False)
    cmp1IPC_SubpriValue.setDependencies(updateIRQValues, ["core.COMPARATOR_1_SUBPRIORITY"])


    #CMP1 HANDLER NAME
    cmp1IPC_handlerStr = cmpComponent.createStringSymbol("CMP1_ISR_HANDLER_NAME", None)
    cmp1IPC_handlerStr.setDefaultValue("COMPARATOR_1_Handler")
    cmp1IPC_handlerStr.setVisible(False)
    cmp1IPC_handlerStr.setDependencies(updateHandlerName, ["core.COMPARATOR_1_HANDLER"])

    #Calculate the proper interrupt registers using IRQ#
    cmp2Irq_index = int(getIRQnumber("COMPARATOR_2"))
    cmp2EnblRegName, enblBitPosn = _get_enblReg_parms(cmp2Irq_index)
    cmp2StatRegName, statBitPosn = _get_statReg_parms(cmp2Irq_index)
    cmp2PriRegName, cmp2PriShift, cmp2SubShift = _get_sub_priority_parms(cmp2Irq_index)

    #CMP2 IEC REG
    cmp2IEC = cmpComponent.createStringSymbol("CMP2_IEC_REG", None)
    cmp2IEC.setDefaultValue(cmp2EnblRegName)
    cmp2IEC.setVisible(False)

    #CMP2 IFS REG
    cmp2IFS = cmpComponent.createStringSymbol("CMP2_IFS_REG", None)
    cmp2IFS.setDefaultValue(cmp2StatRegName)
    cmp2IFS.setVisible(False)


    #CMP2 PRIORITY VALUE
    cmp2IPC_PriValue = cmpComponent.createHexSymbol("CMP2_IPC_PRI_VALUE", None)
    cmp2IPC_PriValue.setDefaultValue(7)
    cmp2IPC_PriValue.setVisible(False)
    cmp2IPC_PriValue.setDependencies(updateIRQValues, ["core.COMPARATOR_2_PRIORITY"])

    #CMP2 SUBPRIORITY VALUE
    cmp2IPC_SubpriValue = cmpComponent.createHexSymbol("CMP2_IPC_SUBPRI_VALUE", None)
    cmp2IPC_SubpriValue.setDefaultValue(3)
    cmp2IPC_SubpriValue.setVisible(False)
    cmp2IPC_SubpriValue.setDependencies(updateIRQValues, ["core.COMPARATOR_2_SUBPRIORITY"])


    #CMP2 HANDLER NAME
    cmp2IPC_handlerStr = cmpComponent.createStringSymbol("CMP2_ISR_HANDLER_NAME", None)
    cmp2IPC_handlerStr.setDefaultValue("COMPARATOR_2_Handler")
    cmp2IPC_handlerStr.setVisible(False)
    cmp2IPC_handlerStr.setDependencies(updateHandlerName, ["core.COMPARATOR_2_HANDLER"])
    
############################################################################
#### Dependency ####
############################################################################

    # NVIC Dynamic settings
    cmpinterrupt1Control = cmpComponent.createBooleanSymbol("CMP1_INTERRUPT_ENABLE", None)
    cmpinterrupt1Control.setDependencies(interruptControl, ["CMP_CM1CON_EVPOL"])
    cmpinterrupt1Control.setVisible(False)
	
    cmpinterrupt2Control = cmpComponent.createBooleanSymbol("CMP2_INTERRUPT_ENABLE", None)
    cmpinterrupt2Control.setDependencies(interruptControl, ["CMP_CM2CON_EVPOL"])
    cmpinterrupt2Control.setVisible(False)

    # Dependency Status
    cmpSymInt1EnComment = cmpComponent.createCommentSymbol("CMP1_INTERRUPT_ENABLE_COMMENT", cmpSym_CM1CON_STRING)
    cmpSymInt1EnComment.setVisible(False)
    cmpSymInt1EnComment.setLabel("Warning!!! Comparator 1 Interrupt is Disabled in Interrupt Manager")
    cmpSymInt1EnComment.setDependencies(dependencyStatus, ["CMP1_INTERRUPT_ENABLE"])

    cmpSymInt2EnComment = cmpComponent.createCommentSymbol("CMP2_INTERRUPT_ENABLE_COMMENT", cmpSym_CM2CON_STRING)
    cmpSymInt2EnComment.setVisible(False)
    cmpSymInt2EnComment.setLabel("Warning!!! Comparator 2 Interrupt is Disabled in Interrupt Manager")
    cmpSymInt2EnComment.setDependencies(dependencyStatus, ["CMP2_INTERRUPT_ENABLE"])    
    
############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    cmpHeaderFile = cmpComponent.createFileSymbol("CMP_COMMON_HEADER", None)
    cmpHeaderFile.setMarkup(True)
    cmpHeaderFile.setSourcePath("../peripheral/cmp_00866/templates/plib_cmp_common.h")
    cmpHeaderFile.setOutputName("plib_cmp_common.h")
    cmpHeaderFile.setDestPath("peripheral/cmp/")
    cmpHeaderFile.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpHeaderFile.setType("HEADER")
    cmpHeaderFile.setOverwrite(True)

    cmpHeader1File = cmpComponent.createFileSymbol("CMP_HEADER1", None)
    cmpHeader1File.setMarkup(True)
    cmpHeader1File.setSourcePath("../peripheral/cmp_00866/templates/plib_cmp.h.ftl")
    cmpHeader1File.setOutputName("plib_"+ cmpInstanceName.getValue().lower()+ ".h")
    cmpHeader1File.setDestPath("peripheral/cmp/")
    cmpHeader1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpHeader1File.setType("HEADER")
    cmpHeader1File.setOverwrite(True)

    cmpSource1File = cmpComponent.createFileSymbol("CMP_SOURCE1", None)
    cmpSource1File.setMarkup(True)
    cmpSource1File.setSourcePath("../peripheral/cmp_00866/templates/plib_cmp.c.ftl")
    cmpSource1File.setOutputName("plib_"+cmpInstanceName.getValue().lower() + ".c")
    cmpSource1File.setDestPath("peripheral/cmp/")
    cmpSource1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpSource1File.setType("SOURCE")
    cmpSource1File.setOverwrite(True)

    cmpSystemInitFile = cmpComponent.createFileSymbol("CMP_INIT", None)
    cmpSystemInitFile.setType("STRING")
    cmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cmpSystemInitFile.setSourcePath("../peripheral/cmp_00866/templates/system/system_initialize.c.ftl")
    cmpSystemInitFile.setMarkup(True)

    cmpSystemDefFile = cmpComponent.createFileSymbol("CMP_DEF", None)
    cmpSystemDefFile.setType("STRING")
    cmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cmpSystemDefFile.setSourcePath("../peripheral/cmp_00866/templates/system/system_definitions.h.ftl")
    cmpSystemDefFile.setMarkup(True)
    
