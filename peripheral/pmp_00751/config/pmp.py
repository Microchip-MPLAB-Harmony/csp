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

###################################################################################################
#################################### Global Variables #############################################
###################################################################################################

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

pmpValGrp_PMMODE_MODE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__MODE"]')
pmpValGrp_PMMODE_WAITB = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__WAITB"]')
pmpValGrp_PMMODE_WAITM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__WAITM"]')
pmpValGrp_PMMODE_WAITE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__WAITE"]')
pmpValGrp_PMMODE_MODE16 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__MODE16"]')
pmpValGrp_PMMODE_INCM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__INCM"]')
pmpValGrp_PMMODE_IRQM = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMMODE__IRQM"]')
pmpValGrp_PMCON_RDSP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMCON__RDSP"]')
pmpValGrp_PMCON_WRSP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMCON__WRSP"]')
pmpValGrp_PMCON_CS2P = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMCON__CS2P"]')
pmpValGrp_PMCON_CS1P = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMCON__CS1P"]')
pmpValGrp_PMCON_CSF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMP"]/value-group@[name="PMCON__CSF"]')

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for ii in reversed(valueNodes):

        dict = {}

        if ii.getAttribute('caption').lower() != "reserved" :
            dict['desc'] = ii.getAttribute('caption')
            dict['key'] = ii.getAttribute('caption')
            value = ii.getAttribute('value')
            dict['value'] = str(value)
            outputList.append(dict)

def pmpCONRDSPVisiblity(symbol, event):

    symbol.setVisible(event["value"])

def pmpCONWRSPVisiblity(symbol, event):

    symbol.setVisible(event["value"])

def pmpAddressPortBitWidthVisiblity(symbol, event):

    symbol.setVisible(event["value"])

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
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
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)


def setPMPInterruptStatus(status):
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock

    Database.setSymbolValue("core", InterruptVector, status, 1)
    Database.setSymbolValue("core", InterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", InterruptHandler, pmpInstanceName.getValue() + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler, pmpInstanceName.getValue() + "_Handler", 1)


def updatePMPInterruptData(symbol, event):
    global InterruptVectorUpdate

    if event["id"] == "PMP_INTERRUPT_MODE":
        setPMPInterruptStatus(event["value"])

    if pmpSymInterruptMode.getValue() == True and Database.getSymbolValue("core", InterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pmpComponent):

    global pmpInstanceName
    global pmpSymInterruptMode
    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global InterruptVectorUpdate

    pmpInstanceName = pmpComponent.createStringSymbol("PMP_INSTANCE_NAME", None)
    pmpInstanceName.setVisible(False)
    pmpInstanceName.setDefaultValue(pmpComponent.getID().upper())

    #Clock enable
    Database.setSymbolValue("core", pmpInstanceName.getValue() + "_CLOCK_ENABLE", True, 2)

    #Stop in Idle mode
    pmpSym_SIDL = pmpComponent.createBooleanSymbol("PMP_SIDL", None)
    pmpSym_SIDL.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:%NOREGISTER%")
    pmpSym_SIDL.setLabel("Stop in Idle Mode bit")

    pmpMODE_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_MODE, pmpMODE_names)
    pmpCommunicationMode = pmpComponent.createKeyValueSetSymbol("PMMODE_MODE", None)
    pmpCommunicationMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpCommunicationMode.setLabel("PMP Mode Selection")
    pmpCommunicationMode.setDefaultValue(0)
    pmpCommunicationMode.setOutputMode("Value")
    pmpCommunicationMode.setDisplayMode("Description")
    for ii in pmpMODE_names:
        #Skip Slave mode options as only Master mode is supported
        if int(ii['value'], 0) > 1:
            pmpCommunicationMode.addKey( ii['desc'], ii['value'], ii['key'] )

    #Master Modes Configuration
    pmpSym_MasterModeMenu = pmpComponent.createMenuSymbol("PMP_MASTER_CONFIG", pmpCommunicationMode)
    pmpSym_MasterModeMenu.setLabel("Master Mode Configuration")

    pmpSymInterruptMode = pmpComponent.createBooleanSymbol("PMP_INTERRUPT_MODE", pmpSym_MasterModeMenu)
    pmpSymInterruptMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:%NOREGISTER%")
    pmpSymInterruptMode.setLabel("Enable Interrrupts ?")

    ## PMP IRQ
    pmpIrqVectorNum = int(getIRQIndex("PMP"))

    if pmpIrqVectorNum != -1:
        InterruptVector = pmpInstanceName.getValue() + "_INTERRUPT_ENABLE"
        InterruptHandler = pmpInstanceName.getValue() + "_INTERRUPT_HANDLER"
        InterruptHandlerLock = pmpInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
        InterruptVectorUpdate = pmpInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

        ## PMP IRQ
        pmpIrqNum = int(getIRQIndex("PMP"))

        ## PMP Error IRQ
        pmpErrIrqNum = int(getIRQIndex("PMP_ERROR"))
    else:
        ## PMP IRQ
        pmpIrqNum = int(getVectorIndex("PMP"))
        InterruptVector = pmpInstanceName.getValue() + "_INTERRUPT_ENABLE"
        InterruptHandler = pmpInstanceName.getValue() + "_INTERRUPT_HANDLER"
        InterruptHandlerLock = pmpInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK"
        InterruptVectorUpdate = pmpInstanceName.getValue() + "_INTERRUPT_ENABLE_UPDATE"

        pmpErrIrqNum = int(getVectorIndex("PMP_ERROR"))

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(pmpIrqNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(pmpIrqNum)

    ## IEC REG
    pmpIEC = pmpComponent.createStringSymbol("PMP_IEC_REG", None)
    pmpIEC.setDefaultValue(enblRegName)
    pmpIEC.setVisible(False)

    ## IEC REG MASK
    pmpIECMask = pmpComponent.createStringSymbol("PMP_IEC_REG_MASK", None)
    pmpIECMask.setDefaultValue(enblMask)
    pmpIECMask.setVisible(False)

    ## IFS REG
    pmpIFS = pmpComponent.createStringSymbol("PMP_IFS_REG", None)
    pmpIFS.setDefaultValue(statRegName)
    pmpIFS.setVisible(False)

    ## IFS REG MASK
    pmpIFSMask = pmpComponent.createStringSymbol("PMP_IFS_REG_MASK", None)
    pmpIFSMask.setDefaultValue(statMask)
    pmpIFSMask.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(pmpErrIrqNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(pmpErrIrqNum)

    ## IEC REG
    pmpErrIEC = pmpComponent.createStringSymbol("PMP_ERR_IEC_REG", None)
    pmpErrIEC.setDefaultValue(enblRegName)
    pmpErrIEC.setVisible(False)

    ## IEC REG MASK
    pmpErrIECMask = pmpComponent.createStringSymbol("PMP_ERR_IEC_REG_MASK", None)
    pmpErrIECMask.setDefaultValue(enblMask)
    pmpErrIECMask.setVisible(False)

    ## IFS REG
    pmpErrIFS = pmpComponent.createStringSymbol("PMP_ERR_IFS_REG", None)
    pmpErrIFS.setDefaultValue(statRegName)
    pmpErrIFS.setVisible(False)

    ## IFS REG MASK
    pmpErrIFSMask = pmpComponent.createStringSymbol("PMP_ERR_IFS_REG_MASK", None)
    pmpErrIFSMask.setDefaultValue(statMask)
    pmpErrIFSMask.setVisible(False)

    pmpCSF_names = []
    _get_bitfield_names(pmpValGrp_PMCON_CSF, pmpCSF_names)
    pmpCSF = pmpComponent.createKeyValueSetSymbol("PMCON_CSF", pmpSym_MasterModeMenu)
    pmpCSF.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMCON")
    pmpCSF.setLabel(pmpValGrp_PMCON_CSF.getAttribute("caption"))
    pmpCSF.setDefaultValue(0)
    pmpCSF.setOutputMode("Value")
    pmpCSF.setDisplayMode("Description")
    for ii in pmpCSF_names:
        pmpCSF.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpCS1P_names = []
    _get_bitfield_names(pmpValGrp_PMCON_CS1P, pmpCS1P_names)
    pmpCS1P = pmpComponent.createKeyValueSetSymbol("PMCON_CS1P", pmpSym_MasterModeMenu)
    pmpCS1P.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMCON")
    pmpCS1P.setLabel("Chip Select 1 Polarity bit")
    pmpCS1P.setDefaultValue(0)
    pmpCS1P.setOutputMode("Value")
    pmpCS1P.setDisplayMode("Description")
    for ii in pmpCS1P_names:
        pmpCS1P.addKey( ii['desc'], ii['value'], ii['key'] )

    if pmpValGrp_PMCON_CS2P != None:
        pmpCS2P_names = []
        _get_bitfield_names(pmpValGrp_PMCON_CS2P, pmpCS2P_names)
        pmpCS2P = pmpComponent.createKeyValueSetSymbol("PMCON_CS2P", pmpSym_MasterModeMenu)
        pmpCS2P.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMCON")
        pmpCS2P.setLabel("Chip Select 2 Polarity bit")
        pmpCS2P.setDefaultValue(0)
        pmpCS2P.setOutputMode("Value")
        pmpCS2P.setDisplayMode("Description")
        for ii in pmpCS2P_names:
            pmpCS2P.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpWAITB_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_WAITB, pmpWAITB_names)
    pmpWaitB = pmpComponent.createKeyValueSetSymbol("PMMODE_WAITB", pmpSym_MasterModeMenu)
    pmpWaitB.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpWaitB.setLabel("Data Setup Wait States")
    pmpWaitB.setDefaultValue(0)
    pmpWaitB.setOutputMode("Value")
    pmpWaitB.setDisplayMode("Description")
    for ii in pmpWAITB_names:
        pmpWaitB.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpWAITM_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_WAITM, pmpWAITM_names)
    pmpWaitM = pmpComponent.createKeyValueSetSymbol("PMMODE_WAITM", pmpSym_MasterModeMenu)
    pmpWaitM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpWaitM.setLabel("Strobe Wait States")
    pmpWaitM.setDefaultValue(0)
    pmpWaitM.setOutputMode("Value")
    pmpWaitM.setDisplayMode("Description")
    for ii in pmpWAITM_names:
        pmpWaitM.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpWAITE_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_WAITE, pmpWAITE_names)
    pmpWaitE = pmpComponent.createKeyValueSetSymbol("PMMODE_WAITE", pmpSym_MasterModeMenu)
    pmpWaitE.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpWaitE.setLabel("Data Hold Wait States")
    pmpWaitE.setDefaultValue(0)
    pmpWaitE.setOutputMode("Value")
    pmpWaitE.setDisplayMode("Description")
    for ii in pmpWAITE_names:
        pmpWaitE.addKey( ii['desc'], ii['value'], ii['key'] )

    if pmpValGrp_PMMODE_MODE16 != None:
        pmpMODE16_names = []
        _get_bitfield_names(pmpValGrp_PMMODE_MODE16, pmpMODE16_names)
        pmpMode16 = pmpComponent.createKeyValueSetSymbol("PMMODE_MODE16", pmpSym_MasterModeMenu)
        pmpMode16.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
        pmpMode16.setLabel("Transfer Size")
        pmpMode16.setDefaultValue(0)
        pmpMode16.setOutputMode("Value")
        pmpMode16.setDisplayMode("Description")
        for ii in pmpMODE16_names:
            pmpMode16.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpINCM_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_INCM, pmpINCM_names)
    pmpINCM = pmpComponent.createKeyValueSetSymbol("PMMODE_INCM", pmpSym_MasterModeMenu)
    pmpINCM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpINCM.setLabel("Address Incrment Mode")
    pmpINCM.setDefaultValue(0)
    pmpINCM.setOutputMode("Value")
    pmpINCM.setDisplayMode("Description")
    for ii in pmpINCM_names:
        #Skip Slave mode options as only Master mode is supported
        if int(ii['value'], 0) < 3:
            pmpINCM.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpIRQM_names = []
    _get_bitfield_names(pmpValGrp_PMMODE_IRQM, pmpIRQM_names)
    pmpIRQM = pmpComponent.createKeyValueSetSymbol("PMMODE_IRQM", pmpSym_MasterModeMenu)
    pmpIRQM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpIRQM.setLabel("Interrupt Request Mode")
    pmpIRQM.setVisible(False)
    pmpIRQM.setDefaultValue(1)
    pmpIRQM.setOutputMode("Value")
    pmpIRQM.setDisplayMode("Description")
    for ii in pmpIRQM_names:
        if int(ii['value'], 0) < 3:
            pmpIRQM.addKey( ii['desc'], ii['value'], ii['key'] )

    pmpReadStrobeEnable = pmpComponent.createBooleanSymbol("PMMODE_READ_STROBE", pmpSym_MasterModeMenu)
    pmpReadStrobeEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpReadStrobeEnable.setLabel("Read Strobe Enable")
    pmpReadStrobeEnable.setDefaultValue(True)

    pmpCONRDSP_names = []
    _get_bitfield_names(pmpValGrp_PMCON_RDSP, pmpCONRDSP_names)
    pmpCONRDSP = pmpComponent.createKeyValueSetSymbol("PMCON_RDSP", pmpReadStrobeEnable)
    pmpCONRDSP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMCON")
    pmpCONRDSP.setLabel(pmpValGrp_PMCON_RDSP.getAttribute("caption"))
    pmpCONRDSP.setDefaultValue(0)
    pmpCONRDSP.setOutputMode("Value")
    pmpCONRDSP.setDisplayMode("Description")
    for ii in pmpCONRDSP_names:
        pmpCONRDSP.addKey( ii['desc'], ii['value'], ii['key'] )
    pmpCONRDSP.setDependencies(pmpCONRDSPVisiblity,["PMMODE_READ_STROBE"])

    pmpWriteStrobeEnable = pmpComponent.createBooleanSymbol("PMMODE_WRITE_STROBE", pmpSym_MasterModeMenu)
    pmpWriteStrobeEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpWriteStrobeEnable.setLabel("Write Strobe Enable")
    pmpWriteStrobeEnable.setDefaultValue(True)

    pmpCONWRSP_names = []
    _get_bitfield_names(pmpValGrp_PMCON_WRSP,pmpCONWRSP_names)
    pmpCONWRSP = pmpComponent.createKeyValueSetSymbol("PMCON_WRSP", pmpWriteStrobeEnable)
    pmpCONWRSP.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMCON")
    pmpCONWRSP.setLabel(pmpValGrp_PMCON_WRSP.getAttribute("caption"))
    pmpCONWRSP.setDefaultValue(0)
    pmpCONWRSP.setOutputMode("Value")
    pmpCONWRSP.setDisplayMode("Description")
    for ii in pmpCONWRSP_names:
        pmpCONWRSP.addKey( ii['desc'], ii['value'], ii['key'] )
    pmpCONWRSP.setDependencies(pmpCONWRSPVisiblity,["PMMODE_WRITE_STROBE"])

    pmpAddressPortEnable = pmpComponent.createBooleanSymbol("PMMODE_ADDRESSPORT_ENABLE", pmpSym_MasterModeMenu)
    pmpAddressPortEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpAddressPortEnable.setLabel("Address Port Enable")

    pmpAddressPortBitWidth = pmpComponent.createIntegerSymbol("PMMODE_ADDRESS_PORT_BITWIDTH", pmpAddressPortEnable)
    pmpAddressPortBitWidth.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:pmp_00751;register:PMMODE")
    pmpAddressPortBitWidth.setLabel("Address Port Bit width")
    pmpAddressPortBitWidth.setMin(0)
    pmpAddressPortBitWidth.setMax(16)
    pmpAddressPortBitWidth.setDefaultValue(16)
    pmpAddressPortBitWidth.setVisible(False)
    pmpAddressPortBitWidth.setDependencies(pmpAddressPortBitWidthVisiblity,["PMMODE_ADDRESSPORT_ENABLE"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    pmpSymIntEnComment = pmpComponent.createCommentSymbol("PMP_INTRRUPT_ENABLE_COMMENT", None)
    pmpSymIntEnComment.setLabel("Warning!!! " + pmpInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    pmpSymIntEnComment.setVisible(False)
    pmpSymIntEnComment.setDependencies(updatePMPInterruptData, ["PMP_INTERRUPT_MODE", "core." + InterruptVectorUpdate])

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pmpHeader1File = pmpComponent.createFileSymbol("PMP_HEADER", None)
    pmpHeader1File.setSourcePath("../peripheral/pmp_00751/templates/plib_pmp.h.ftl")
    pmpHeader1File.setOutputName("plib_pmp.h")
    pmpHeader1File.setDestPath("peripheral/pmp/")
    pmpHeader1File.setProjectPath("config/" + configName + "/peripheral/pmp/")
    pmpHeader1File.setType("HEADER")
    pmpHeader1File.setMarkup(True)
    pmpHeader1File.setOverwrite(True)

    pmpSource1File = pmpComponent.createFileSymbol("PMP_SOURCE", None)
    pmpSource1File.setSourcePath("../peripheral/pmp_00751/templates/plib_pmp.c.ftl")
    pmpSource1File.setOutputName("plib_pmp.c")
    pmpSource1File.setDestPath("peripheral/pmp/")
    pmpSource1File.setProjectPath("config/" + configName + "/peripheral/pmp/")
    pmpSource1File.setType("SOURCE")
    pmpSource1File.setMarkup(True)
    pmpSource1File.setOverwrite(True)

    pmpSystemInitFile = pmpComponent.createFileSymbol("PMP_INIT", None)
    pmpSystemInitFile.setType("STRING")
    pmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pmpSystemInitFile.setSourcePath("../peripheral/pmp_00751/templates/system/initialization.c.ftl")
    pmpSystemInitFile.setMarkup(True)

    pmpSystemDefFile = pmpComponent.createFileSymbol("PMP_DEF", None)
    pmpSystemDefFile.setType("STRING")
    pmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pmpSystemDefFile.setSourcePath("../peripheral/pmp_00751/templates/system/definitions.h.ftl")
    pmpSystemDefFile.setMarkup(True)
