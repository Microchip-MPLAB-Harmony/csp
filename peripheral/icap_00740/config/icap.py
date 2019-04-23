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
#### Register Information ####
################################################################################
icapValGrp_IC1CON_ICM     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICM"]')
icapValGrp_IC1CON_ICI     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICI"]')
icapValGrp_IC1CON_ICTMR   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__ICTMR"]')
icapValGrp_IC1CON_C32     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__C32"]')
icapValGrp_IC1CON_FEDGE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__FEDGE"]')
icapValGrp_IC1CON_SIDL    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="ICAP"]/value-group@[name="IC1CON__SIDL"]')

cfgBifield_ICACLK           = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGCON"]/bitfield@[name="ICACLK"]')

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
global icapSym_CFGCON_ICACLK

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
################################################################################
#### Business Logic ####
################################################################################
def dependencyStatus(symbol, event):
    component = symbol.getComponent()
    num_int_lines = component.getSymbolValue("ICAP_NUM_INT_LINES")
    if(num_int_lines == 1):
        if((component.getSymbolValue("ICAP_INTERRUPT_ENABLE") or component.getSymbolValue("ICAP_ERROR_INTERRUPT_ENABLE")) \
            and (Database.getSymbolValue("core", captureInterruptVectorUpdate) == True)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)
    else:
        if(component.getSymbolValue("ICAP_INTERRUPT_ENABLE") and (Database.getSymbolValue("core", captureInterruptVectorUpdate) == True)):
            symbol.setVisible(True)
        elif(component.getSymbolValue("ICAP_ERROR_INTERRUPT_ENABLE") and (Database.getSymbolValue("core", errorInterruptVectorUpdate) == True)):
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

def getIRQIndex(string):

    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    irq_index = "-1"

    for param in interruptsChildren:
        name = param.getAttribute("name")
        if string == name:
            irq_index = param.getAttribute("index")
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))
            if "irq-name" in param.getAttributeList():
                name = str(param.getAttribute("irq-name"))
            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):

    vector_index = "-1"

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index


def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    bit = float(temp%1)
    bitPosn = int(32.0*bit)
    regName = "IEC"+str(index)
    return regName, str(bitPosn)

def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    bit = float(temp%1)
    bitPosn = int(32.0*bit)
    regName = "IFS"+str(index)
    return regName, str(bitPosn)

def combineValues(symbol, event):
    icmValue    = icapSym_ICxCON_ICM.getValue() << 0
    iciValue    = icapSym_ICxCON_ICI.getValue() << 5
    if (cfgBifield_ICACLK != None):
        if (icapSym_CFGCON_ICACLK.getValue() == False):
            ictmrValue  = icapSym_ICxCON_ICTMR.getValue() << 7
        else:
            ictmrValue  = icapSym_ICxCON_ICTMR_ALT.getValue() << 7
    else:
        ictmrValue  = icapSym_ICxCON_ICTMR.getValue() << 7
    c32Value    = icapSym_ICxCON_C32.getValue() << 8
    fedgeValue  = icapSym_ICxCON_FEDGE.getValue() << 9
    sidlValue   = int(icapSym_ICxCON_SIDL.getValue()) << 13
    icxconValue = icmValue + iciValue + ictmrValue + c32Value + fedgeValue + sidlValue
    symbol.setValue(icxconValue, 2)

def icapFirstEdgeVisible(symbol, event):
    if(event["value"] == 6):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def icapSymbolVisible(symbol, event):
    symbol.setVisible(event["value"])

def icapTimerSourceVisibility(symbol, event):
    symbol.setVisible(not event["value"])

def icapInterruptSet(symbol, event):
    component = symbol.getComponent()
    num_int_lines = component.getSymbolValue("ICAP_NUM_INT_LINES")
    if (num_int_lines == 1):
        if (component.getSymbolValue("ICAP_INTERRUPT_ENABLE") or component.getSymbolValue("ICAP_ERROR_INTERRUPT_ENABLE")):
            Database.setSymbolValue("core", captureInterruptVector,True, 2)
            Database.setSymbolValue("core", captureInterruptHandlerLock, True, 2)
            interruptName = captureInterruptHandler.split("_INTERRUPT_HANDLER")[0]
            Database.setSymbolValue("core", captureInterruptHandler, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", captureInterruptVector,False, 2)
            Database.setSymbolValue("core", captureInterruptHandlerLock, False, 2)
            interruptName = captureInterruptHandler.split("_INTERRUPT_HANDLER")[0]
            Database.setSymbolValue("core", captureInterruptHandler, interruptName + "_Handler", 1)

    else:
        if (event["id"] == "ICAP_INTERRUPT_ENABLE"):
            Database.setSymbolValue("core", captureInterruptVector, event["value"], 2)
            Database.setSymbolValue("core", captureInterruptHandlerLock, event["value"], 2)
            interruptName = captureInterruptHandler.split("_INTERRUPT_HANDLER")[0]
            if(event["value"] == True):
                Database.setSymbolValue("core", captureInterruptHandler, interruptName + "_InterruptHandler", 1)
            else:
                Database.setSymbolValue("core", captureInterruptHandler, interruptName + "_Handler", 1)
        if (event["id"] == "ICAP_ERROR_INTERRUPT_ENABLE"):
            Database.setSymbolValue("core", errorInterruptVector, event["value"], 2)
            Database.setSymbolValue("core", errorInterruptHandlerLock, event["value"], 2)
            interruptName = errorInterruptHandler.split("_INTERRUPT_HANDLER")[0]
            if(event["value"] == True):
                Database.setSymbolValue("core", errorInterruptHandler, interruptName + "_InterruptHandler", 1)
            else:
                Database.setSymbolValue("core", errorInterruptHandler, interruptName + "_Handler", 1)

def updateICAPClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])
################################################################################
#### Component ####
################################################################################
def instantiateComponent(icapComponent):
    global icapInstanceName
    global icapSym_ICxCON_ICM
    global icapSym_ICxCON_ICI
    global icapSym_CFGCON_ICACLK
    global icapSym_ICxCON_ICTMR
    global icapSym_ICxCON_ICTMR_ALT
    global icapSym_ICxCON_C32
    global icapSym_ICxCON_FEDGE
    global icapSym_ICxCON_SIDL
    global captureInterruptVector
    global captureInterruptHandlerLock
    global captureInterruptHandler
    global captureInterruptVectorUpdate
    global errorInterruptVector
    global errorInterruptHandlerLock
    global errorInterruptHandler
    global errorInterruptVectorUpdate

    #instance
    icapInstanceName = icapComponent.createStringSymbol("ICAP_INSTANCE_NAME", None)
    icapInstanceName.setVisible(False)
    icapInstanceName.setDefaultValue(icapComponent.getID().upper())
    Log.writeInfoMessage("Running " + icapInstanceName.getValue())

    icapInstanceNum = icapComponent.createStringSymbol("ICAP_INSTANCE_NUM", None)
    icapInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(icapComponent.getID()))
    icapInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", icapInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    icapxICM_names = []
    _get_bitfield_names(icapValGrp_IC1CON_ICM, icapxICM_names)
    icapSym_ICxCON_ICM = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICM", None)
    icapSym_ICxCON_ICM.setLabel("Select Input Capture Mode")
    icapSym_ICxCON_ICM.setDefaultValue(1)
    icapSym_ICxCON_ICM.setOutputMode("Value")
    icapSym_ICxCON_ICM.setDisplayMode("Description")
    for ii in icapxICM_names:
        icapSym_ICxCON_ICM.addKey( ii['desc'], ii['value'], ii['key'] )
    icapSym_ICxCON_ICM.setVisible(True)

    if (cfgBifield_ICACLK != None):
        icapSym_CFGCON_ICACLK = icapComponent.createBooleanSymbol("ICAP_CFGCON_ICACLK", None)
        icapSym_CFGCON_ICACLK.setLabel("Use Alternate Timer Source")
        icapSym_CFGCON_ICACLK.setDefaultValue(0)

    #Timer source
    icapxICTMR_names = []
    icapSym_ICxCON_ICTMR = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICTMR", None)
    icapSym_ICxCON_ICTMR.setLabel("Select Timer Source")
    icapSym_ICxCON_ICTMR.setDefaultValue(0)
    icapSym_ICxCON_ICTMR.setOutputMode("Value")
    icapSym_ICxCON_ICTMR.setDisplayMode("Description")
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ICAP\"]/instance@[name=\""+icapInstanceName.getValue()+"\"]/parameters")
    icapxICTMR_names = node.getChildren()
    for ii in range(len(icapxICTMR_names)):
        if("TMR_SRC" in icapxICTMR_names[ii].getAttribute("name") ):
            icapSym_ICxCON_ICTMR.addKey(icapxICTMR_names[ii].getAttribute("name"),
            icapxICTMR_names[ii].getAttribute("value"), icapxICTMR_names[ii].getAttribute("caption") )
    icapSym_ICxCON_ICTMR.setVisible(True)
    icapSym_ICxCON_ICTMR.setDependencies(icapTimerSourceVisibility, ["ICAP_CFGCON_ICACLK"])

    #Timer source
    icapxICTMR_names = []
    icapSym_ICxCON_ICTMR_ALT = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICTMR_ALT", None)
    icapSym_ICxCON_ICTMR_ALT.setLabel("Select Timer Source")
    icapSym_ICxCON_ICTMR_ALT.setDefaultValue(0)
    icapSym_ICxCON_ICTMR_ALT.setOutputMode("Value")
    icapSym_ICxCON_ICTMR_ALT.setDisplayMode("Description")
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"ICAP\"]/instance@[name=\""+icapInstanceName.getValue()+"\"]/parameters")
    icapxICTMR_names = node.getChildren()
    for ii in range(len(icapxICTMR_names)):
        if("TMR_ALTERNATE_SRC" in icapxICTMR_names[ii].getAttribute("name") ):
            icapSym_ICxCON_ICTMR_ALT.addKey(icapxICTMR_names[ii].getAttribute("name"),
            icapxICTMR_names[ii].getAttribute("value"), icapxICTMR_names[ii].getAttribute("caption") )
    icapSym_ICxCON_ICTMR_ALT.setVisible(False)
    icapSym_ICxCON_ICTMR_ALT.setDependencies(icapSymbolVisible, ["ICAP_CFGCON_ICACLK"])

    icapSym_TIMER_COMMENT = icapComponent.createCommentSymbol("ICAP_TIMER_COMMENT", None)
    icapSym_TIMER_COMMENT.setLabel("**** Configure Selected Timer Source (Timer x) in TMRx Component ****")
    icapSym_TIMER_COMMENT.setVisible(True)

    icapxC32_names = []
    _get_bitfield_names(icapValGrp_IC1CON_C32, icapxC32_names)
    icapSym_ICxCON_C32 = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_C32", None)
    icapSym_ICxCON_C32.setLabel("Select Timer Width")
    icapSym_ICxCON_C32.setDefaultValue(0)
    icapSym_ICxCON_C32.setOutputMode("Value")
    icapSym_ICxCON_C32.setDisplayMode("Description")
    for ii in icapxC32_names:
        icapSym_ICxCON_C32.addKey( ii['desc'], ii['value'], ii['key'] )
    icapSym_ICxCON_C32.setVisible(True)

    icapxFEDGE_names = []
    _get_bitfield_names(icapValGrp_IC1CON_FEDGE, icapxFEDGE_names)
    icapSym_ICxCON_FEDGE = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_FEDGE", None)
    icapSym_ICxCON_FEDGE.setLabel("Select First Capture Edge")
    icapSym_ICxCON_FEDGE.setDefaultValue(0)
    icapSym_ICxCON_FEDGE.setVisible(False)
    icapSym_ICxCON_FEDGE.setOutputMode("Value")
    icapSym_ICxCON_FEDGE.setDisplayMode("Description")
    for ii in icapxFEDGE_names:
        icapSym_ICxCON_FEDGE.addKey( ii['desc'], ii['value'], ii['key'] )
    icapSym_ICxCON_FEDGE.setVisible(False)
    icapSym_ICxCON_FEDGE.setDependencies(icapFirstEdgeVisible, ["ICAP_ICxCON_ICM"])

    icapSym_ICxCON_SIDL = icapComponent.createBooleanSymbol("ICAP_ICxCON_SIDL", None)
    icapSym_ICxCON_SIDL.setLabel("Stop in IDLE")
    icapSym_ICxCON_SIDL.setDefaultValue(False)
    icapSym_ICxCON_SIDL.setVisible(True)

    #Collecting user input to combine into ICxCON register
    #ICxCON is updated every time a user selection changes
    icapSym_ICxCON = icapComponent.createHexSymbol("ICxCON_VALUE", None)
    icapSym_ICxCON.setDefaultValue(0x1)
    icapSym_ICxCON.setVisible(False)
    icapSym_ICxCON.setDependencies(combineValues, ["ICAP_ICxCON_ICM", "ICAP_ICxCON_ICI", "ICAP_ICxCON_ICTMR",\
        "ICAP_ICxCON_ICTMR_ALT", "ICAP_ICxCON_C32", "ICAP_ICxCON_FEDGE", "ICAP_ICxCON_SIDL", "ICAP_CFGCON_ICACLK"])

    #Calculate the proper interrupt registers using IRQ#
    irqString = "INPUT_CAPTURE_" + str(instanceNum)
    icxIrq_index = int(getIRQIndex(irqString))
    int_lines = 1

    if icxIrq_index == -1:
        int_lines = 2
        icxIrq_index = int(getVectorIndex(irqString))

    statRegName, statBitPosn = _get_statReg_parms(icxIrq_index)
    enblRegName, enblBitPosn = _get_enblReg_parms(icxIrq_index)

    icapSym_NUM_INT_LINES = icapComponent.createIntegerSymbol("ICAP_NUM_INT_LINES", None)
    icapSym_NUM_INT_LINES.setVisible(False)
    icapSym_NUM_INT_LINES.setDefaultValue(int_lines)

    #IFS REG
    icapxIFS = icapComponent.createStringSymbol("ICAPx_IFS_REG", None)
    icapxIFS.setDefaultValue(statRegName)
    icapxIFS.setVisible(False)

    #IEC REG
    icapxIEC = icapComponent.createStringSymbol("ICAPx_IEC_REG", None)
    icapxIEC.setDefaultValue(enblRegName)
    icapxIEC.setVisible(False)

    #Calculate the proper interrupt registers using ERROR IRQ#
    irqString = "INPUT_CAPTURE_" + str(instanceNum) + "_ERROR"
    icxIrq_index = int(getIRQIndex(irqString))
    if icxIrq_index == -1:
        icxIrq_index = int(getVectorIndex(irqString))
    errStatRegName, statBitPosn = _get_statReg_parms(icxIrq_index)
    errEnblRegName, enblBitPosn = _get_enblReg_parms(icxIrq_index)

    #ERROR IEC REG
    icapxErrIEC = icapComponent.createStringSymbol("ERROR_IEC_REG", None)
    icapxErrIEC.setDefaultValue(errEnblRegName)
    icapxErrIEC.setVisible(False)

    #ERROR IFS REG
    icapxErrIFS = icapComponent.createStringSymbol("ERROR_IFS_REG", None)
    icapxErrIFS.setDefaultValue(errStatRegName)
    icapxErrIFS.setVisible(False)


    # NVIC Dynamic settings
    icapinterrupt1Control = icapComponent.createBooleanSymbol("ICAP_INTERRUPT_ENABLE", None)
    icapinterrupt1Control.setVisible(True)
    icapinterrupt1Control.setLabel("Enable Capture Interrupt")
    icapinterrupt1Control.setDefaultValue(False)

    icapxICI_names = []
    _get_bitfield_names(icapValGrp_IC1CON_ICI, icapxICI_names)
    icapSym_ICxCON_ICI = icapComponent.createKeyValueSetSymbol("ICAP_ICxCON_ICI", icapinterrupt1Control)
    icapSym_ICxCON_ICI.setLabel("Select Interrupt Mode")
    icapSym_ICxCON_ICI.setDefaultValue(0)
    icapSym_ICxCON_ICI.setOutputMode("Value")
    icapSym_ICxCON_ICI.setDisplayMode("Description")
    for ii in icapxICI_names:
        icapSym_ICxCON_ICI.addKey( ii['desc'], ii['value'], ii['key'] )
    icapSym_ICxCON_ICI.setVisible(False)
    icapSym_ICxCON_ICI.setDependencies(icapSymbolVisible, ["ICAP_INTERRUPT_ENABLE"])

    icapinterrupt2Control = icapComponent.createBooleanSymbol("ICAP_ERROR_INTERRUPT_ENABLE", None)
    icapinterrupt2Control.setVisible(True)
    icapinterrupt2Control.setLabel("Enable Error Interrupt")
    icapinterrupt2Control.setDefaultValue(False)

############################################################################
#### Dependency ####
############################################################################
    captureIrq = "INPUT_CAPTURE_" + str(instanceNum)
    captureInterruptVector = captureIrq + "_INTERRUPT_ENABLE"
    captureInterruptHandler = captureIrq + "_INTERRUPT_HANDLER"
    captureInterruptHandlerLock = captureIrq + "_INTERRUPT_HANDLER_LOCK"
    captureInterruptVectorUpdate = captureIrq + "_INTERRUPT_ENABLE_UPDATE"

    errorIrq = "INPUT_CAPTURE_" + str(instanceNum) + "_ERROR"
    errorInterruptVector = errorIrq + "_INTERRUPT_ENABLE"
    errorInterruptHandler = errorIrq + "_INTERRUPT_HANDLER"
    errorInterruptHandlerLock = errorIrq + "_INTERRUPT_HANDLER_LOCK"
    errorInterruptVectorUpdate = errorIrq + "_INTERRUPT_ENABLE_UPDATE"

    icapSym_EVIC_SYMBOL = icapComponent.createStringSymbol("ICAP_EVIC_SYMBOL_SET", None)
    icapSym_EVIC_SYMBOL.setVisible(False)
    icapSym_EVIC_SYMBOL.setDependencies(icapInterruptSet, ["ICAP_INTERRUPT_ENABLE", "ICAP_ERROR_INTERRUPT_ENABLE"])

    # Dependency Status
    icapSymInt1EnComment = icapComponent.createCommentSymbol("INTERRUPT_ENABLE_COMMENT", None)
    icapSymInt1EnComment.setVisible(False)
    icapSymInt1EnComment.setLabel("Warning!!! " + icapInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    icapSymInt1EnComment.setDependencies(dependencyStatus, ["ICAP_INTERRUPT_ENABLE", "ICAP_ERROR_INTERRUPT_ENABLE", \
        "core."+captureInterruptVectorUpdate, "core."+errorInterruptVectorUpdate])

    # Clock Warning status
    icapSym_ClkEnComment = icapComponent.createCommentSymbol("ICAP_CLOCK_ENABLE_COMMENT", None)
    icapSym_ClkEnComment.setLabel("Warning!!! " + icapInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    icapSym_ClkEnComment.setVisible(False)
    icapSym_ClkEnComment.setDependencies(updateICAPClockWarningStatus, ["core." + icapInstanceName.getValue() + "_CLOCK_ENABLE"])
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
    icapHeader1File.setOutputName("plib_" + icapInstanceName.getValue().lower() + ".h")
    icapHeader1File.setDestPath("peripheral/icap/")
    icapHeader1File.setProjectPath("config/" + configName + "/peripheral/icap/")
    icapHeader1File.setType("HEADER")
    icapHeader1File.setOverwrite(True)

    icapSource1File = icapComponent.createFileSymbol("ICAP_SOURCE1", None)
    icapSource1File.setMarkup(True)
    icapSource1File.setSourcePath("../peripheral/icap_00740/templates/plib_icap.c.ftl")
    icapSource1File.setOutputName("plib_" + icapInstanceName.getValue().lower() + ".c")
    icapSource1File.setDestPath("peripheral/icap/")
    icapSource1File.setProjectPath("config/" + configName + "/peripheral/icap/")
    icapSource1File.setType("SOURCE")
    icapSource1File.setOverwrite(True)

    icapSystemInitFile = icapComponent.createFileSymbol("ICAP_INIT", None)
    icapSystemInitFile.setType("STRING")
    icapSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    icapSystemInitFile.setSourcePath("../peripheral/icap_00740/templates/system/initialization.c.ftl")
    icapSystemInitFile.setMarkup(True)

    icapSystemDefFile = icapComponent.createFileSymbol("ICAP_DEF", None)
    icapSystemDefFile.setType("STRING")
    icapSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    icapSystemDefFile.setSourcePath("../peripheral/icap_00740/templates/system/definitions.h.ftl")
    icapSystemDefFile.setMarkup(True)
