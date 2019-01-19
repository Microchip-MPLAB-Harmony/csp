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
ocmpValGrp_OCxCON_OCM 	    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__OCM"]')
ocmpValGrp_OCxCON_OCTSEL    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__OCTSEL"]')
ocmpValGrp_OCxCON_OC32 	    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__OC32"]')
ocmpValGrp_OCxCON_SIDL 	    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/value-group@[name="OC1CON__SIDL"]')

ocmpBitFld_OCxCON_OCM       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/register-group@[name="OCMP"]/register@[name="OC1CON"]/bitfield@[name="OCM"]')
ocmpBitFld_OCxCON_OCTSEL    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/register-group@[name="OCMP"]/register@[name="OC1CON"]/bitfield@[name="OCTSEL"]')
ocmpBitFld_OCxCON_OC32      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/register-group@[name="OCMP"]/register@[name="OC1CON"]/bitfield@[name="OC32"]')
ocmpBitFld_OCxCON_SIDL 	    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="OCMP"]/register-group@[name="OCMP"]/register@[name="OC1CON"]/bitfield@[name="SIDL"]')
################################################################################
#### Global Variables ####
################################################################################
global ocmpInstanceName
global ocmpSym_OCxCON_OCM
global ocmpSym_OCxCON_OCTSEL
global ocmpSym_OCxCON_OC32
global ocmpSym_OCxCON_SIDL
global ocmpIPC_PriValue
global ocmpIPC_SubpriValue
global prioShift
global subprioShift

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
    ocmValue    = ocmpSym_OCxCON_OCM.getValue() << 0
    octselValue = ocmpSym_OCxCON_OCTSEL.getValue() << 3
    oc32Value   = ocmpSym_OCxCON_OC32.getValue() << 5
    sidlValue   = int(ocmpSym_OCxCON_SIDL.getValue()) << 13
    ocxconValue = sidlValue + oc32Value + octselValue + ocmValue
    symbol.setValue(ocxconValue, 2)
    print ocxconValue

def combineIPC_Values(symbol, event):
    ocmpPri = int(ocmpIPC_PriValue.getValue()) << int(prioShift)
    ocmpSub = int(ocmpIPC_SubpriValue.getValue()) << int(subprioShift)
    ipc = ocmpPri + ocmpSub
    symbol.setValue(ipc, 2)

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
def instantiateComponent(ocmpComponent):
    global ocmpInstanceName
    global ocmpSym_OCxCON_OCM
    global ocmpSym_OCxCON_OCTSEL
    global ocmpSym_OCxCON_OC32
    global ocmpSym_OCxCON_SIDL
    global ocmpIPC_PriValue
    global ocmpIPC_SubpriValue
    global prioShift
    global subprioShift

    ocmpInstanceIndex = ocmpComponent.createStringSymbol("INDEX", None)
    ocmpInstanceIndex.setVisible(False)
    componentName = str(ocmpComponent.getID())
    for s in list(componentName):
        if s.isdigit():
            index = s
    ocmpInstanceIndex.setDefaultValue(index)
    
    ocmpxOCM_names = []
    _get_bitfield_names(ocmpValGrp_OCxCON_OCM, ocmpxOCM_names)
    ocmpSym_OCxCON_OCM = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OCM", None)
    ocmpSym_OCxCON_OCM.setLabel(ocmpBitFld_OCxCON_OCM.getAttribute("caption"))
    ocmpSym_OCxCON_OCM.setDefaultValue(0)
    ocmpSym_OCxCON_OCM.setOutputMode("Value")
    ocmpSym_OCxCON_OCM.setDisplayMode("Description")
    for ii in ocmpxOCM_names:
        ocmpSym_OCxCON_OCM.addKey( ii['desc'], ii['value'], ii['key'] )    
    ocmpSym_OCxCON_OCM.setVisible(True)

    ocmpxOCTSEL_names = []
    _get_bitfield_names(ocmpValGrp_OCxCON_OCTSEL, ocmpxOCTSEL_names)
    ocmpSym_OCxCON_OCTSEL = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OCTSEL", None)
    ocmpSym_OCxCON_OCTSEL.setLabel(ocmpBitFld_OCxCON_OCTSEL.getAttribute("caption"))
    ocmpSym_OCxCON_OCTSEL.setDefaultValue(0)
    ocmpSym_OCxCON_OCTSEL.setOutputMode("Value")
    ocmpSym_OCxCON_OCTSEL.setDisplayMode("Description")
    for ii in ocmpxOCTSEL_names:
        ocmpSym_OCxCON_OCTSEL.addKey( ii['desc'], ii['value'], ii['key'] )    
    ocmpSym_OCxCON_OCTSEL.setVisible(True)

    ocmpxOC32_names = []
    _get_bitfield_names(ocmpValGrp_OCxCON_OC32, ocmpxOC32_names)
    ocmpSym_OCxCON_OC32 = ocmpComponent.createKeyValueSetSymbol("OCMP_OCxCON_OC32", None)
    ocmpSym_OCxCON_OC32.setLabel(ocmpBitFld_OCxCON_OC32.getAttribute("caption"))
    ocmpSym_OCxCON_OC32.setDefaultValue(0)
    ocmpSym_OCxCON_OC32.setOutputMode("Value")
    ocmpSym_OCxCON_OC32.setDisplayMode("Description")
    for ii in ocmpxOC32_names:
        ocmpSym_OCxCON_OC32.addKey( ii['desc'], ii['value'], ii['key'] )    
    ocmpSym_OCxCON_OC32.setVisible(True)
    
    ocmpSym_OCxCON_SIDL = ocmpComponent.createBooleanSymbol("OCMP_OCxCON_SIDL", None)
    ocmpSym_OCxCON_SIDL.setLabel(ocmpBitFld_OCxCON_SIDL.getAttribute("caption"))
    ocmpSym_OCxCON_SIDL.setDefaultValue(False)
    ocmpSym_OCxCON_SIDL.setVisible(True)
	
    #Collect user input to combine into OCxCON register
    ocmpSym_ICM = ocmpComponent.createHexSymbol("OCxCON_VALUE", None)
    ocmpSym_ICM.setDefaultValue(0)
    ocmpSym_ICM.setVisible(False)
    ocmpSym_ICM.setDependencies(combineValues, ["OCMP_OCxCON_OCM"])
    ocmpSym_ICM.setDependencies(combineValues, ["OCMP_OCxCON_OCTSEL"])
    ocmpSym_ICM.setDependencies(combineValues, ["OCMP_OCxCON_OC32"])
    ocmpSym_ICM.setDependencies(combineValues, ["OCMP_OCxCON_SIDL"])
    
    #Calculate the proper interrupt registers for IEC, IFS, IPC, priority shift, and subpriority shift
    irqString = "OUTPUT_COMPARE_" + str(index)
    vectorNum = int(getIRQnumber(irqString))
    enblRegName, enblBitPosn = _get_enblReg_parms(vectorNum)
    statRegName, statBitPosn = _get_statReg_parms(vectorNum)
    prioRegName, prioShift, subprioShift = _get_sub_priority_parms(vectorNum)

    #IEC_REG
    ocmpIEC = ocmpComponent.createStringSymbol("IEC_REG", None)
    ocmpIEC.setDefaultValue(enblRegName)
    ocmpIEC.setVisible(False)

    #IFS_REG
    ocmpIFS = ocmpComponent.createStringSymbol("IFS_REG", None)
    ocmpIFS.setDefaultValue(statRegName)
    ocmpIFS.setVisible(False)

    #IPC_REG
    ocmpIPC = ocmpComponent.createStringSymbol("IPC_REG", None)
    ocmpIPC.setDefaultValue(prioRegName)
    ocmpIPC.setVisible(False)

    #PRIORITY VALUE
    priValueString = "core.OUTPUT_COMPARE_" + str(index) + "_PRIORITY"
    ocmpIPC_PriValue = ocmpComponent.createHexSymbol("IPC_PRI_VALUE", None)
    ocmpIPC_PriValue.setDefaultValue(7)
    ocmpIPC_PriValue.setVisible(False)
    ocmpIPC_PriValue.setDependencies(updateIRQValues, [priValueString])

    #SUBPRIORITY VALUE
    subpriValueString = "core.OUTPUT_COMPARE_" + str(index) + "_SUBPRIORITY"
    ocmpIPC_SubpriValue = ocmpComponent.createHexSymbol("IPC_SUBPRI_VALUE", None)
    ocmpIPC_SubpriValue.setDefaultValue(3)
    ocmpIPC_SubpriValue.setVisible(False)
    ocmpIPC_SubpriValue.setDependencies(updateIRQValues, [subpriValueString])

    #IPC VALUE
    ocmpIPC = ocmpComponent.createHexSymbol("IPC_VALUE", None)
    ocmpIPC.setDefaultValue(0)
    ocmpIPC.setVisible(False)    
    ocmpIPC.setDependencies(combineIPC_Values, ["IPC_PRI_VALUE"])
    ocmpIPC.setDependencies(combineIPC_Values, ["IPC_SUBPRI_VALUE"])

    #HANDLER NAME
    handlerString = "core.OUTPUT_COMPARE_" + str(index) + "_HANDLER"
    ocmpIPC_handlerStr = ocmpComponent.createStringSymbol("ISR_HANDLER_NAME", None)
    ocmpIPC_handlerStr.setDefaultValue("OUTPUT_COMPARE_"+ str(index) + "_Handler")
    ocmpIPC_handlerStr.setVisible(False)
    ocmpIPC_handlerStr.setDependencies(updateHandlerName, [handlerString])
    
############################################################################
#### Dependency ####
############################################################################
    
    # NVIC Dynamic settings
    ocmpinterrupt1Control = ocmpComponent.createBooleanSymbol("OCMP_INTERRUPT_ENABLE", None)
    ocmpinterrupt1Control.setVisible(True)
    ocmpinterrupt1Control.setLabel("Interrupt Enable")
    ocmpinterrupt1Control.setDefaultValue(False)
    ocmpinterrupt1Control.setDependencies(interruptControl, ["OCMP_INTERRUPT_ENABLE"])
    
    # Dependency Status
    ocmpSymInt1EnComment = ocmpComponent.createCommentSymbol("INTERRUPT_ENABLE_COMMENT", ocmpinterrupt1Control)
    ocmpSymInt1EnComment.setVisible(False)
    ocmpSymInt1EnComment.setLabel("Warning!!! Output Compare " + str(index) + " Interrupt is Disabled in Interrupt Manager")
    ocmpSymInt1EnComment.setDependencies(dependencyStatus, ["OCMP_INTERRUPT_ENABLE"])
    
############################################################################
#### Code Generation ####
############################################################################
    
    configName = Variables.get("__CONFIGURATION_NAME")

    ocmpHeaderFile = ocmpComponent.createFileSymbol("OCMP_COMMON_HEADER", None)
    ocmpHeaderFile.setMarkup(True)
    ocmpHeaderFile.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp_common.h")
    ocmpHeaderFile.setOutputName("plib_ocmp_common.h")
    ocmpHeaderFile.setDestPath("peripheral/ocmp/")
    ocmpHeaderFile.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpHeaderFile.setType("HEADER")
    ocmpHeaderFile.setOverwrite(True)

    ocmpHeader1File = ocmpComponent.createFileSymbol("OCMP_HEADER1", None)
    ocmpHeader1File.setMarkup(True)
    ocmpHeader1File.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp.h.ftl")
    ocmpHeader1File.setOutputName("plib_ocmp"+ str(index) + ".h")
    ocmpHeader1File.setDestPath("peripheral/ocmp/")
    ocmpHeader1File.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpHeader1File.setType("HEADER")
    ocmpHeader1File.setOverwrite(True)

    ocmpSource1File = ocmpComponent.createFileSymbol("OCMP_SOURCE1", None)
    ocmpSource1File.setMarkup(True)
    ocmpSource1File.setSourcePath("../peripheral/ocmp_00749/templates/plib_ocmp.c.ftl")
    ocmpSource1File.setOutputName("plib_ocmp"+ str(index) + ".c")
    ocmpSource1File.setDestPath("peripheral/ocmp/")
    ocmpSource1File.setProjectPath("config/" + configName + "/peripheral/ocmp/")
    ocmpSource1File.setType("SOURCE")
    ocmpSource1File.setOverwrite(True)

    ocmpSystemInitFile = ocmpComponent.createFileSymbol("OCMP_INIT", None)
    ocmpSystemInitFile.setType("STRING")
    ocmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ocmpSystemInitFile.setSourcePath("../peripheral/ocmp_00749/templates/system/system_initialize.c.ftl")
    ocmpSystemInitFile.setMarkup(True)

    ocmpSystemDefFile = ocmpComponent.createFileSymbol("OCMP_DEF", None)
    ocmpSystemDefFile.setType("STRING")
    ocmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ocmpSystemDefFile.setSourcePath("../peripheral/ocmp_00749/templates/system/system_definitions.h.ftl")
    ocmpSystemDefFile.setMarkup(True)
 
