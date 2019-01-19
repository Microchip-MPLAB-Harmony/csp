# coding: utf-8
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
icapValGrp_IC1CON_ICM 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICM"]')
icapValGrp_IC1CON_ICI 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICI"]')
icapValGrp_IC1CON_ICTMR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICTMR"]')
icapValGrp_IC1CON_C32 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__C32"]')
icapValGrp_IC1CON_FEDGE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__FEDGE"]')
icapValGrp_IC1CON_SIDL 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__SIDL"]')

icapBitFld_IC1CON_ICM 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="ICM"]')
icapBitFld_IC1CON_ICI 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="ICI"]')
icapBitFld_IC1CON_ICTMR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="ICTMR"]')
icapBitFld_IC1CON_C32 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="C32"]')
icapBitFld_IC1CON_FEDGE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="FEDGE"]')
icapBitFld_IC1CON_SIDL 	= ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/register-group@[name="ICAP"]/register@[name="IC1CON"]/bitfield@[name="SIDL"]')
################################################################################
#### Global Variables ####
################################################################################
global icapInstanceName
global icapSym_ICxCON_ICM
global icapSym_ICxCON_ICI
global icapSym_ICxCON_ICTMR
global icapSym_ICxCON_C32
global icapSym_ICxCON_FEDGE
global icapSym_ICxCON_SIDL
global icapxIPC_PriValue
global icapxIPC_SubpriValue
global icapxErrIPC_PriValue
global icapxErrIPC_SubpriValue   
global prioShift
global subprioShift
global errPrioShift
global errSubprioShift

################################################################################
#### Business Logic ####
################################################################################
def interruptControl(symbol, event):
    if (event["value"] == True):
        symbol.setValue(True, 2)
    else :
	symbol.setValue(False, 2)
    
def dependencyStatus(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

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

def combineValues(symbol, event):
    icmValue    = icapSym_ICxCON_ICM.getValue() << 0
    iciValue    = icapSym_ICxCON_ICI.getValue() << 5 
    ictmrValue  = icapSym_ICxCON_ICTMR.getValue() << 7
    c32Value    = icapSym_ICxCON_C32.getValue() << 8
    fedgeValue  = icapSym_ICxCON_FEDGE.getValue() << 9
    sidlValue   = int(icapSym_ICxCON_SIDL.getValue()) << 13
    icxconValue = icmValue + iciValue + ictmrValue + c32Value + fedgeValue + sidlValue
    symbol.setValue(icxconValue, 2)

def combineIPC_Values(symbol, event):
    ipcPri = int(icapxIPC_PriValue.getValue()) << int(prioShift)
    ipcSub = int(icapxIPC_SubpriValue.getValue()) << int(subprioShift)
    ipc = ipcPri + ipcSub
    symbol.setValue(ipc, 2)

def combineErrIPC_Values(symbol, event):
    errIpcPri = int(icapxErrIPC_PriValue.getValue()) << int(errPrioShift)
    errIpcSub = int(icapxErrIPC_SubpriValue.getValue()) << int(errSubprioShift)
    errIpc = errIpcPri + errIpcSub
    symbol.setValue(errIpc, 2)
    
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
def instantiateComponent(icapComponent):
    global icapInstanceName
    global icapSym_ICxCON_ICM
    global icapSym_ICxCON_ICI
    global icapSym_ICxCON_ICTMR
    global icapSym_ICxCON_C32
    global icapSym_ICxCON_FEDGE
    global icapSym_ICxCON_SIDL
    global icapxIPC_PriValue
    global icapxIPC_SubpriValue
    global icapxErrIPC_PriValue
    global icapxErrIPC_SubpriValue    
    global prioShift
    global subprioShift
    global errPrioShift
    global errSubprioShift

    icapInstanceIndex = icapComponent.createStringSymbol("INDEX", None)
    icapInstanceIndex.setVisible(False)
    componentName = str(icapComponent.getID())
    for s in list(componentName):
        if s.isdigit():
            index = s
    icapInstanceIndex.setDefaultValue(index)
    
    icapxICM_names = []
    _get_bitfield_names(icapValGrp_IC1CON_ICM, icapxICM_names)
    icapSym_ICxCON_ICM = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICM", None)
    icapSym_ICxCON_ICM.setLabel(icapBitFld_IC1CON_ICM.getAttribute("caption"))
    icapSym_ICxCON_ICM.setDefaultValue(0)
    icapSym_ICxCON_ICM.setOutputMode("Value")
    icapSym_ICxCON_ICM.setDisplayMode("Description")
    for ii in icapxICM_names:
        icapSym_ICxCON_ICM.addKey( ii['desc'], ii['value'], ii['key'] )    
    icapSym_ICxCON_ICM.setVisible(True)
	
    icapxICI_names = []
    _get_bitfield_names(icapValGrp_IC1CON_ICI, icapxICI_names)
    icapSym_ICxCON_ICI = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICI", None)
    icapSym_ICxCON_ICI.setLabel(icapBitFld_IC1CON_ICI.getAttribute("caption"))
    icapSym_ICxCON_ICI.setDefaultValue(0)
    icapSym_ICxCON_ICI.setOutputMode("Value")
    icapSym_ICxCON_ICI.setDisplayMode("Description")
    for ii in icapxICI_names:
        icapSym_ICxCON_ICI.addKey( ii['desc'], ii['value'], ii['key'] )    
    icapSym_ICxCON_ICI.setVisible(True)

    icapxICTMR_names = []
    _get_bitfield_names(icapValGrp_IC1CON_ICTMR, icapxICTMR_names)
    icapSym_ICxCON_ICTMR = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICTMR", None)
    icapSym_ICxCON_ICTMR.setLabel(icapBitFld_IC1CON_ICTMR.getAttribute("caption"))
    icapSym_ICxCON_ICTMR.setDefaultValue(0)
    icapSym_ICxCON_ICTMR.setOutputMode("Value")
    icapSym_ICxCON_ICTMR.setDisplayMode("Description")
    for ii in icapxICTMR_names:
        icapSym_ICxCON_ICTMR.addKey( ii['desc'], ii['value'], ii['key'] )    
    icapSym_ICxCON_ICTMR.setVisible(True)

    icapxC32_names = []
    _get_bitfield_names(icapValGrp_IC1CON_C32, icapxC32_names)
    icapSym_ICxCON_C32 = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_C32", None)
    icapSym_ICxCON_C32.setLabel(icapBitFld_IC1CON_C32.getAttribute("caption"))
    icapSym_ICxCON_C32.setDefaultValue(0)
    icapSym_ICxCON_C32.setOutputMode("Value")
    icapSym_ICxCON_C32.setDisplayMode("Description")
    for ii in icapxC32_names:
        icapSym_ICxCON_C32.addKey( ii['desc'], ii['value'], ii['key'] )    
    icapSym_ICxCON_C32.setVisible(True)
    
    icapxFEDGE_names = []
    _get_bitfield_names(icapValGrp_IC1CON_FEDGE, icapxFEDGE_names)
    icapSym_ICxCON_FEDGE = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_FEDGE", None)
    icapSym_ICxCON_FEDGE.setLabel(icapBitFld_IC1CON_FEDGE.getAttribute("caption"))
    icapSym_ICxCON_FEDGE.setDefaultValue(0)
    icapSym_ICxCON_FEDGE.setOutputMode("Value")
    icapSym_ICxCON_FEDGE.setDisplayMode("Description")
    for ii in icapxFEDGE_names:
        icapSym_ICxCON_FEDGE.addKey( ii['desc'], ii['value'], ii['key'] )    
    icapSym_ICxCON_FEDGE.setVisible(True)
    
    icapSym_ICxCON_SIDL = icapComponent.createBooleanSymbol("ICAP_ICxCON_SIDL", None)
    icapSym_ICxCON_SIDL.setLabel(icapBitFld_IC1CON_SIDL.getAttribute("caption"))
    icapSym_ICxCON_SIDL.setDefaultValue(False)
    icapSym_ICxCON_SIDL.setVisible(True)

    #Collecting user input to combine into ICxCON register
    #ICxCON is updated every time a user selection changes
    icapSym_ICxCON = icapComponent.createHexSymbol("ICxCON_VALUE", None)
    icapSym_ICxCON.setDefaultValue(0)
    icapSym_ICxCON.setVisible(False)
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_ICM"])
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_ICI"])
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_ICTMR"])
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_C32"])    
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_FEDGE"])
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_SIDL"])

    #Calculate the proper interrupt registers using IRQ#
    irqString = "INPUT_CAPTURE_" + icapInstanceIndex.getValue()
    icxIrq_index = int(getIRQnumber(irqString))
    enblRegName, enblBitPosn = _get_enblReg_parms(icxIrq_index)
    statRegName, statBitPosn = _get_statReg_parms(icxIrq_index)
    prioRegName, prioShift, subprioShift = _get_sub_priority_parms(icxIrq_index)

    #IEC REG
    icapxIEC = icapComponent.createStringSymbol("ICAPx_IEC_REG", None)
    icapxIEC.setDefaultValue(enblRegName)
    icapxIEC.setVisible(False)

    #IFS REG
    icapxIFS = icapComponent.createStringSymbol("ICAPx_IFS_REG", None)
    icapxIFS.setDefaultValue(statRegName)
    icapxIFS.setVisible(False)

    #IPC REG
    icapxIPC = icapComponent.createStringSymbol("ICAPx_IPC_REG", None)
    icapxIPC.setDefaultValue(prioRegName)
    icapxIPC.setVisible(False)

    #PRIORITY VALUE
    priValueString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_PRIORITY"
    icapxIPC_PriValue = icapComponent.createHexSymbol("ICAPx_IPC_PRI_VALUE", None)
    icapxIPC_PriValue.setDefaultValue(7)
    icapxIPC_PriValue.setVisible(False)
    icapxIPC_PriValue.setDependencies(updateIRQValues, [priValueString])

    #SUBPRIORITY VALUE
    subpriValueString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_SUBPRIORITY"
    icapxIPC_SubpriValue = icapComponent.createHexSymbol("ICAPx_IPC_SUBPRI_VALUE", None)
    icapxIPC_SubpriValue.setDefaultValue(3)
    icapxIPC_SubpriValue.setVisible(False)
    icapxIPC_SubpriValue.setDependencies(updateIRQValues, [subpriValueString])

    #IPC VALUE
    icapxIPC = icapComponent.createHexSymbol("IPC_VALUE", None)
    icapxIPC.setDefaultValue(0)
    icapxIPC.setVisible(False)    
    icapxIPC.setDependencies(combineIPC_Values, ["ICAPx_IPC_PRI_VALUE"])
    icapxIPC.setDependencies(combineIPC_Values, ["ICAPx_IPC_SUBPRI_VALUE"])

    #HANDLER NAME
    handlerString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_HANDLER"
    icapxIPC_handlerStr = icapComponent.createStringSymbol("ISR_HANDLER_NAME", None)
    icapxIPC_handlerStr.setDefaultValue("INPUT_CAPTURE_"+ str(index) + "_Handler")
    icapxIPC_handlerStr.setVisible(False)
    icapxIPC_handlerStr.setDependencies(updateHandlerName, [handlerString])

    #Calculate the proper interrupt registers using ERROR IRQ#
    irqString = "INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_ERROR"
    icxIrq_index = int(getIRQnumber(irqString))
    errEnblRegName, enblBitPosn = _get_enblReg_parms(icxIrq_index)
    errStatRegName, statBitPosn = _get_statReg_parms(icxIrq_index)
    errPrioRegName, errPrioShift, errSubprioShift = _get_sub_priority_parms(icxIrq_index)

    #ERROR IEC REG
    icapxErrIEC = icapComponent.createStringSymbol("ERROR_IEC_REG", None)
    icapxErrIEC.setDefaultValue(errEnblRegName)
    icapxErrIEC.setVisible(False)

    #ERROR IFS REG
    icapxErrIFS = icapComponent.createStringSymbol("ERROR_IFS_REG", None)
    icapxErrIFS.setDefaultValue(errStatRegName)
    icapxErrIFS.setVisible(False)

    #ERROR IPC REG
    icapxErrIPC = icapComponent.createStringSymbol("ERROR_IPC_REG", None)
    icapxErrIPC.setDefaultValue(errPrioRegName)
    icapxErrIPC.setVisible(False)

    #ERROR PRIORITY VALUE
    errpriValueString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_ERROR_PRIORITY"
    icapxErrIPC_PriValue = icapComponent.createHexSymbol("ICAPx_ERROR_IPC_PRI_VALUE", None)
    icapxErrIPC_PriValue.setDefaultValue(7)
    icapxErrIPC_PriValue.setVisible(False)
    icapxErrIPC_PriValue.setDependencies(updateIRQValues, [errpriValueString])

    #ERROR SUBPRIORITY VALUE
    errsubpriValueString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_ERROR_SUBPRIORITY"
    icapxErrIPC_SubpriValue = icapComponent.createHexSymbol("ICAPx_ERROR_IPC_SUBPRI_VALUE", None)
    icapxErrIPC_SubpriValue.setDefaultValue(3)
    icapxErrIPC_SubpriValue.setVisible(False)
    icapxErrIPC_SubpriValue.setDependencies(updateIRQValues, [errsubpriValueString])

    #ERROR IPC VALUE
    icapxErrIPC = icapComponent.createHexSymbol("ERROR_IPC_VALUE", None)
    icapxErrIPC.setDefaultValue(0)
    icapxErrIPC.setVisible(False)    
    icapxErrIPC.setDependencies(combineErrIPC_Values, ["ICAPx_ERROR_IPC_PRI_VALUE"])
    icapxErrIPC.setDependencies(combineErrIPC_Values, ["ICAPx_ERROR_IPC_SUBPRI_VALUE"])

    #ERROR HANDLER NAME
    errhandlerString = "core.INPUT_CAPTURE_" + icapInstanceIndex.getValue() + "_ERROR_HANDLER"
    icapxErrIPC_handlerStr = icapComponent.createStringSymbol("ISR_ERROR_HANDLER_NAME", None)
    icapxErrIPC_handlerStr.setDefaultValue("INPUT_CAPTURE_"+ str(index) + "_ERROR_Handler")
    icapxErrIPC_handlerStr.setVisible(False)
    icapxErrIPC_handlerStr.setDependencies(updateHandlerName, [errhandlerString])
    
############################################################################
#### Dependency ####
############################################################################
    
    # NVIC Dynamic settings
    icapinterrupt1Control = icapComponent.createBooleanSymbol("ICAP_INTERRUPT_ENABLE", None)
    icapinterrupt1Control.setVisible(True)
    icapinterrupt1Control.setLabel("Interrupt Enable")
    icapinterrupt1Control.setDefaultValue(False)    
    icapinterrupt1Control.setDependencies(interruptControl, ["ICAP_INTERRUPT_ENABLE"])

    icapinterrupt2Control = icapComponent.createBooleanSymbol("ICAP_ERROR_INTERRUPT_ENABLE", None)
    icapinterrupt2Control.setVisible(True)
    icapinterrupt2Control.setLabel("Error Interrupt Enable")
    icapinterrupt2Control.setDefaultValue(False)       
    icapinterrupt2Control.setDependencies(interruptControl, ["ICAP_ERROR_INTERRUPT_ENABLE"])

    # Dependency Status
    icapSymIntEnComment = icapComponent.createCommentSymbol("IC_INTERRUPT_ENABLE_COMMENT", icapinterrupt1Control)
    icapSymIntEnComment.setVisible(False)
    icapSymIntEnComment.setLabel("Warning!!! Input Capture " + str(index) + " Interrupt is Disabled in Interrupt Manager")
    icapSymIntEnComment.setDependencies(dependencyStatus, ["ICAP_INTERRUPT_ENABLE"])

    icapSymInt2EnComment = icapComponent.createCommentSymbol("IC_ERROR_INTERRUPT_ENABLE_COMMENT", icapinterrupt2Control)
    icapSymInt2EnComment.setVisible(False)
    icapSymInt2EnComment.setLabel("Warning!!! Input Capture " + str(index) + " Error Interrupt is Disabled in Interrupt Manager")
    icapSymInt2EnComment.setDependencies(dependencyStatus, ["ICAP_ERROR_INTERRUPT_ENABLE"])    
    
############################################################################
#### Code Generation ####
############################################################################
    
    configName = Variables.get("__CONFIGURATION_NAME")

    icapHeaderFile = icapComponent.createFileSymbol("ICAP_COMMON_HEADER", None)
    icapHeaderFile.setMarkup(True)
    icapHeaderFile.setSourcePath("../peripheral/icap_00740/templates/plib_icap_common.h")
    icapHeaderFile.setOutputName("plib_icap_common.h")
    icapHeaderFile.setDestPath("peripheral/icap/")
    icapHeaderFile.setProjectPath("config/" + configName + "/peripheral/icap/")
    icapHeaderFile.setType("HEADER")
    icapHeaderFile.setOverwrite(True)

    icapHeader1File = icapComponent.createFileSymbol("ICAP_HEADER1", None)
    icapHeader1File.setMarkup(True)
    icapHeader1File.setSourcePath("../peripheral/icap_00740/templates/plib_icap.h.ftl")
    icapHeader1File.setOutputName("plib_icap"+ str(index) + ".h")
    icapHeader1File.setDestPath("peripheral/icap/")
    icapHeader1File.setProjectPath("config/" + configName + "/peripheral/icap/")
    icapHeader1File.setType("HEADER")
    icapHeader1File.setOverwrite(True)

    icapSource1File = icapComponent.createFileSymbol("ICAP_SOURCE1", None)
    icapSource1File.setMarkup(True)
    icapSource1File.setSourcePath("../peripheral/icap_00740/templates/plib_icap.c.ftl")
    icapSource1File.setOutputName("plib_icap" + str(index) + ".c")
    icapSource1File.setDestPath("peripheral/icap/")
    icapSource1File.setProjectPath("config/" + configName + "/peripheral/icap/")
    icapSource1File.setType("SOURCE")
    icapSource1File.setOverwrite(True)

    icapSystemInitFile = icapComponent.createFileSymbol("ICAP_INIT", None)
    icapSystemInitFile.setType("STRING")
    icapSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    icapSystemInitFile.setSourcePath("../peripheral/icap_00740/templates/system/system_initialize.c.ftl")
    icapSystemInitFile.setMarkup(True)

    icapSystemDefFile = icapComponent.createFileSymbol("ICAP_DEF", None)
    icapSystemDefFile.setType("STRING")
    icapSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    icapSystemDefFile.setSourcePath("../peripheral/icap_00740/templates/system/system_definitions.h.ftl")
    icapSystemDefFile.setMarkup(True)
 
