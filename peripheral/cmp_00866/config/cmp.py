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

cmpRegGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]').getChildren()

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

cmpBitFld_CMSTAT_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CMSTAT"]/bitfield@[name="SIDL"]')

################################################################################
#### Global Variables ####
################################################################################

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################

def setCMPxInterruptData(status, index):

    Database.setSymbolValue("core", InterruptVector[index - 1], status, 1)
    Database.setSymbolValue("core", InterruptHandlerLock[index - 1], status, 1)

    interruptName = InterruptHandler[index - 1].split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", InterruptHandler[index - 1], interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", InterruptHandler[index - 1], interruptName + "_Handler", 1)

def updateCMPxInterruptData(symbol, event):

    symbolId = symbol.getID()
    cmp_id = int((symbolId.replace("CMP", "")).replace("_INTERRUPT_ENABLE_COMMENT", ""))

    status = int(cmpSym_CMxCON_EVPOL[cmp_id - 1].getSelectedValue()) != 0

    if event["id"] == "CMP_CM" + str(cmp_id) + "CON_EVPOL":
        setCMPxInterruptData(status, cmp_id)

    if Database.getSymbolValue("core", InterruptVectorUpdate[cmp_id - 1].replace("core.", "")) == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    return regName

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for bitfield in reversed(valueNodes):   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def combineValues(symbol, event):

    symbolId = symbol.getID()
    cmp_id = int((symbolId.replace("CM", "")).replace("CON_VALUE", "")) - 1

    cchValue   = cmpSym_CMxCON_CCH[cmp_id].getValue() << 0
    crefValue  = cmpSym_CMxCON_CREF[cmp_id].getValue() << 4
    evpolValue = cmpSym_CMxCON_EVPOL[cmp_id].getValue() << 6
    cpolValue  = cmpSym_CMxCON_CPOL[cmp_id].getValue() << 13
    coeValue   = cmpSym_CMxCON_COE[cmp_id].getValue() << 14
    cmconValue = crefValue + cchValue + evpolValue + cpolValue + coeValue

    symbol.setValue(cmconValue, 2)

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))

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

def updateCMPxClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################

def instantiateComponent(cmpComponent):

    global cmpInstanceName
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global InterruptVectorUpdate
    global cmpSym_CMxCON_CREF
    global cmpSym_CMxCON_CCH
    global cmpSym_CMxCON_EVPOL
    global cmpSym_CMxCON_CPOL
    global cmpSym_CMxCON_COE

    InterruptVector = []
    InterruptHandler = []
    InterruptHandlerLock = []
    InterruptVectorUpdate = []

    cmpSym_CMxCON_CREF = []
    cmpSym_CMxCON_CCH = []
    cmpSym_CMxCON_EVPOL = []
    cmpSym_CMxCON_CPOL = []
    cmpSym_CMxCON_COE = []

    cmpInstanceName = cmpComponent.createStringSymbol("CMP_INSTANCE_NAME", None)
    cmpInstanceName.setVisible(False)
    cmpInstanceName.setDefaultValue(cmpComponent.getID().upper())

    #Stop in Idle mode
    if cmpBitFld_CMSTAT_SIDL != None:
        cmpSym_CMSTAT_SIDL = cmpComponent.createBooleanSymbol("CMP_CMSTAT_SIDL", None)
        cmpSym_CMSTAT_SIDL.setLabel(cmpBitFld_CMSTAT_SIDL.getAttribute("caption"))
        cmpSym_CMSTAT_SIDL.setDefaultValue(False)

    index = 1

    for register in cmpRegGroup:
        regName = str(register.getAttribute("name"))
        if regName.startswith("CM") and regName.endswith("CON"):
            index = int((regName.replace("CM", "")).replace("CON", ""))

            cmpSym_Menu = cmpComponent.createMenuSymbol("CMP" + str(index) + "_MENU", None)
            cmpSym_Menu.setLabel("Comparator " + str(index))

            #Clock enable
            Database.setSymbolValue("core", "CMP" + str(index) + "_CLOCK_ENABLE", True, 1)

            #Positive input of Comparator
            cmp1CREF_names = []
            _get_bitfield_names(cmpValGrp_CM1CON_CREF, cmp1CREF_names)
            cmpSym_CMxCON_CREF.append(index)
            cmpSym_CMxCON_CREF[index - 1] = cmpComponent.createKeyValueSetSymbol("CMP_CM" + str(index) + "CON_CREF", cmpSym_Menu)
            cmpSym_CMxCON_CREF[index - 1].setLabel(cmpBitFld_CM1CON_CREF.getAttribute("caption"))
            cmpSym_CMxCON_CREF[index - 1].setDefaultValue(0)
            cmpSym_CMxCON_CREF[index - 1].setOutputMode("Value")
            cmpSym_CMxCON_CREF[index - 1].setDisplayMode("Description")
            for ii in cmp1CREF_names:
                cmpSym_CMxCON_CREF[index - 1].addKey( ii['desc'], ii['value'], ii['key'] )

            #Negative input of Comparator
            cmp1CCH_names = []
            _get_bitfield_names(cmpValGrp_CM1CON_CCH, cmp1CCH_names)
            cmpSym_CMxCON_CCH.append(index)
            cmpSym_CMxCON_CCH[index - 1] = cmpComponent.createKeyValueSetSymbol("CMP_CM" + str(index) + "CON_CCH", cmpSym_Menu)
            cmpSym_CMxCON_CCH[index - 1].setLabel(cmpBitFld_CM1CON_CCH.getAttribute("caption"))
            cmpSym_CMxCON_CCH[index - 1].setDefaultValue(0)
            cmpSym_CMxCON_CCH[index - 1].setOutputMode("Value")
            cmpSym_CMxCON_CCH[index - 1].setDisplayMode("Description")
            for ii in cmp1CCH_names:
                cmpSym_CMxCON_CCH[index - 1].addKey( ii['desc'], ii['value'], ii['key'] )

            #Edge selection for interrupt generation
            cmp1EVPOL_names = []
            _get_bitfield_names(cmpValGrp_CM1CON_EVPOL, cmp1EVPOL_names)
            cmpSym_CMxCON_EVPOL.append(index)
            cmpSym_CMxCON_EVPOL[index - 1] = cmpComponent.createKeyValueSetSymbol("CMP_CM" + str(index) + "CON_EVPOL", cmpSym_Menu)
            cmpSym_CMxCON_EVPOL[index - 1].setLabel(cmpBitFld_CM1CON_EVPOL.getAttribute("caption"))
            cmpSym_CMxCON_EVPOL[index - 1].setDefaultValue(0)
            cmpSym_CMxCON_EVPOL[index - 1].setOutputMode("Value")
            cmpSym_CMxCON_EVPOL[index - 1].setDisplayMode("Description")
            for ii in cmp1EVPOL_names:
                cmpSym_CMxCON_EVPOL[index - 1].addKey( ii['desc'], ii['value'], ii['key'] )

            #Comparator output invert
            cmpSym_CMxCON_CPOL.append(index)
            cmpSym_CMxCON_CPOL[index - 1] = cmpComponent.createBooleanSymbol("CMP_CM" + str(index) + "CON_CPOL", cmpSym_Menu)
            cmpSym_CMxCON_CPOL[index - 1].setLabel(cmpBitFld_CM1CON_CPOL.getAttribute("caption"))

            #Comparator output on pin
            cmpSym_CMxCON_COE.append(index)
            cmpSym_CMxCON_COE[index - 1] = cmpComponent.createBooleanSymbol("CMP_CM" + str(index) + "CON_COE", cmpSym_Menu)
            cmpSym_CMxCON_COE[index - 1].setLabel(cmpBitFld_CM1CON_COE.getAttribute("caption"))

            #Collecting user input to combine into CMPxCON register
            #CMPxCON is updated every time a user selection changes
            cmpSym_CMP1CON = cmpComponent.createHexSymbol("CM" + str(index) + "CON_VALUE", None)
            cmpSym_CMP1CON.setDefaultValue(0)
            cmpSym_CMP1CON.setVisible(False)
            cmpSym_CMP1CON.setDependencies(combineValues, ["CMP_CM" + str(index) + "CON_CREF", "CMP_CM" + str(index) + "CON_CCH", "CMP_CM" + str(index) + "CON_EVPOL", "CMP_CM" + str(index) + "CON_CPOL", "CMP_CM" + str(index) + "CON_COE"])

            #Calculate the proper interrupt registers using IRQ#
            cmpxIrq = "COMPARATOR_" + str(index)
            InterruptVector.append(cmpxIrq + "_INTERRUPT_ENABLE")
            InterruptHandler.append(cmpxIrq + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(cmpxIrq + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append("core." + cmpxIrq + "_INTERRUPT_ENABLE_UPDATE")

            cmpxIrq_index = int(getIRQIndex(cmpxIrq))

            if cmpxIrq_index == -1:
                cmpxIrq_index = int(getVectorIndex(cmpxIrq))

            cmpxEnblRegName = _get_enblReg_parms(cmpxIrq_index)
            cmpxStatRegName = _get_statReg_parms(cmpxIrq_index)

            #CMPx IEC REG
            cmpxIEC = cmpComponent.createStringSymbol("CMP" + str(index) + "_IEC_REG", None)
            cmpxIEC.setDefaultValue(cmpxEnblRegName)
            cmpxIEC.setVisible(False)

            #CMPx IFS REG
            cmpxIFS = cmpComponent.createStringSymbol("CMP" + str(index) + "_IFS_REG", None)
            cmpxIFS.setDefaultValue(cmpxStatRegName)
            cmpxIFS.setVisible(False)

            ############################################################################
            #### Dependency ####
            ############################################################################

            # EVIC Dynamic settings
            # Dependency Status
            cmpSymIntxEnComment = cmpComponent.createCommentSymbol("CMP" + str(index) + "_INTERRUPT_ENABLE_COMMENT", cmpSym_Menu)
            cmpSymIntxEnComment.setVisible(False)
            cmpSymIntxEnComment.setLabel("Warning!!! Comparator " + str(index) + " Interrupt is Disabled in Interrupt Manager")
            cmpSymIntxEnComment.setDependencies(updateCMPxInterruptData, ["CMP_CM" + str(index) + "CON_EVPOL", InterruptVectorUpdate[index - 1]])

            # Clock Warning status
            cmpSym_ClkxEnComment = cmpComponent.createCommentSymbol("CMP" + str(index) + "_CLOCK_ENABLE_COMMENT", cmpSym_Menu)
            cmpSym_ClkxEnComment.setLabel("Warning!!! Comparator " + str(index) + " Peripheral Clock is Disabled in Clock Manager")
            cmpSym_ClkxEnComment.setVisible(False)
            cmpSym_ClkxEnComment.setDependencies(updateCMPxClockWarningStatus, ["core.CMP" + str(index) + "_CLOCK_ENABLE"])

    cmpSym_Count = cmpComponent.createIntegerSymbol("CMP_COUNT", cmpSym_Menu)
    cmpSym_Count.setDefaultValue(index)
    cmpSym_Count.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    cmpHeader1File = cmpComponent.createFileSymbol("CMP_HEADER1", None)
    cmpHeader1File.setMarkup(True)
    cmpHeader1File.setSourcePath("../peripheral/cmp_00866/templates/plib_cmp.h.ftl")
    cmpHeader1File.setOutputName("plib_" + cmpInstanceName.getValue().lower() + ".h")
    cmpHeader1File.setDestPath("peripheral/cmp/")
    cmpHeader1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpHeader1File.setType("HEADER")
    cmpHeader1File.setOverwrite(True)

    cmpSource1File = cmpComponent.createFileSymbol("CMP_SOURCE1", None)
    cmpSource1File.setMarkup(True)
    cmpSource1File.setSourcePath("../peripheral/cmp_00866/templates/plib_cmp.c.ftl")
    cmpSource1File.setOutputName("plib_" + cmpInstanceName.getValue().lower() + ".c")
    cmpSource1File.setDestPath("peripheral/cmp/")
    cmpSource1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpSource1File.setType("SOURCE")
    cmpSource1File.setOverwrite(True)

    cmpSystemInitFile = cmpComponent.createFileSymbol("CMP_INIT", None)
    cmpSystemInitFile.setType("STRING")
    cmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cmpSystemInitFile.setSourcePath("../peripheral/cmp_00866/templates/system/initialization.c.ftl")
    cmpSystemInitFile.setMarkup(True)

    cmpSystemDefFile = cmpComponent.createFileSymbol("CMP_DEF", None)
    cmpSystemDefFile.setType("STRING")
    cmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cmpSystemDefFile.setSourcePath("../peripheral/cmp_00866/templates/system/definitions.h.ftl")
    cmpSystemDefFile.setMarkup(True)

