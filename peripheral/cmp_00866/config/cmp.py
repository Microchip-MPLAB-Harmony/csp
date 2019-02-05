"""*****************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################

def setCMP1InterruptData(status):

    Database.setSymbolValue("core", cmp1InterruptVector, status, 1)
    Database.setSymbolValue("core", cmp1InterruptHandlerLock, status, 1)

    interruptName = cmp1InterruptHandler.split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", cmp1InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", cmp1InterruptHandler, interruptName + "_Handler", 1)

def setCMP2InterruptData(status):

    Database.setSymbolValue("core", cmp2InterruptVector, status, 1)
    Database.setSymbolValue("core", cmp2InterruptHandlerLock, status, 1)

    interruptName = cmp2InterruptHandler.split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", cmp2InterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", cmp2InterruptHandler, interruptName + "_Handler", 1)

def updateCMP1InterruptData(symbol, event):

    status = int(cmpSym_CM1CON_EVPOL.getSelectedValue()) != 0

    if event["id"] == "CMP_CM1CON_EVPOL":
        setCMP1InterruptData(status)

    if Database.getSymbolValue("core", cmp1InterruptVectorUpdate) == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateCMP2InterruptData(symbol, event):

    status = int(cmpSym_CM2CON_EVPOL.getSelectedValue()) != 0

    if event["id"] == "CMP_CM2CON_EVPOL":
        setCMP2InterruptData(status)

    if Database.getSymbolValue("core", cmp2InterruptVectorUpdate) == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
        index = int(vectorNumber / 32)
        regName = "IEC" + str(index)
        return regName

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    if(("PIC32MZ" in Variables.get("__PROCESSOR")) and ("EF" in Variables.get("__PROCESSOR"))):
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

def combine1Values(symbol, event):

    cchValue   = cmpSym_CM1CON_CCH.getValue() << 0
    crefValue  = cmpSym_CM1CON_CREF.getValue() << 4
    evpolValue = cmpSym_CM1CON_EVPOL.getValue() << 6
    cpolValue  = cmpSym_CM1CON_CPOL.getValue() << 13
    coeValue   = cmpSym_CM1CON_COE.getValue() << 14
    cmconValue = crefValue + cchValue + evpolValue + cpolValue + coeValue

    symbol.setValue(cmconValue, 2)

def combine2Values(symbol, event):

    cchValue   = cmpSym_CM2CON_CCH.getValue() << 0
    crefValue  = cmpSym_CM2CON_CREF.getValue() << 4
    evpolValue = cmpSym_CM2CON_EVPOL.getValue() << 6
    cpolValue  = cmpSym_CM2CON_CPOL.getValue() << 13
    coeValue   = cmpSym_CM2CON_COE.getValue() << 14
    cmconValue = crefValue + cchValue + evpolValue + cpolValue + coeValue

    symbol.setValue(cmconValue, 2)

def getIRQnumber(string):

    for param in interruptsChildren:
        modInst = param.getAttribute("name")
        if string == modInst:
            irq_index = param.getAttribute("index")

    return irq_index

################################################################################
#### Component ####
################################################################################

def instantiateComponent(cmpComponent):

    global cmpInstanceName
    global cmp1InterruptVector
    global cmp1InterruptHandlerLock
    global cmp1InterruptHandler
    global cmp1InterruptVectorUpdate
    global cmp2InterruptVector
    global cmp2InterruptHandlerLock
    global cmp2InterruptHandler
    global cmp2InterruptVectorUpdate
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

    cmpInstanceName = cmpComponent.createStringSymbol("CMP_INSTANCE_NAME", None)
    cmpInstanceName.setVisible(False)
    cmpInstanceName.setDefaultValue(cmpComponent.getID().upper())
    print("Running " + cmpInstanceName.getValue())

    cmpSym_CM1CON_STRING = cmpComponent.createCommentSymbol("CMP1_STRING", None)
    cmpSym_CM1CON_STRING.setLabel("Comparator 1")

    #Positive input of Comparator 1
    cmp1CREF_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_CREF, cmp1CREF_names)
    cmpSym_CM1CON_CREF = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_CREF", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CREF.setLabel(cmpBitFld_CM1CON_CREF.getAttribute("caption"))
    cmpSym_CM1CON_CREF.setDefaultValue(0)
    cmpSym_CM1CON_CREF.setOutputMode("Value")
    cmpSym_CM1CON_CREF.setDisplayMode("Description")
    for ii in cmp1CREF_names:
        cmpSym_CM1CON_CREF.addKey( ii['desc'], ii['value'], ii['key'] )

    #Negative input of Comparator 1
    cmp1CCH_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_CCH, cmp1CCH_names)
    cmpSym_CM1CON_CCH = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_CCH", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CCH.setLabel(cmpBitFld_CM1CON_CCH.getAttribute("caption"))
    cmpSym_CM1CON_CCH.setDefaultValue(0)
    cmpSym_CM1CON_CCH.setOutputMode("Value")
    cmpSym_CM1CON_CCH.setDisplayMode("Description")
    for ii in cmp1CCH_names:
        cmpSym_CM1CON_CCH.addKey( ii['desc'], ii['value'], ii['key'] )

    #Edge selection for interrupt generation
    cmp1EVPOL_names = []
    _get_bitfield_names(cmpValGrp_CM1CON_EVPOL, cmp1EVPOL_names)
    cmpSym_CM1CON_EVPOL = cmpComponent.createKeyValueSetSymbol("CMP_CM1CON_EVPOL", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_EVPOL.setLabel(cmpBitFld_CM1CON_EVPOL.getAttribute("caption"))
    cmpSym_CM1CON_EVPOL.setDefaultValue(0)
    cmpSym_CM1CON_EVPOL.setOutputMode("Value")
    cmpSym_CM1CON_EVPOL.setDisplayMode("Description")
    for ii in cmp1EVPOL_names:
        cmpSym_CM1CON_EVPOL.addKey( ii['desc'], ii['value'], ii['key'] )

    #Comparator output invert
    cmpSym_CM1CON_CPOL = cmpComponent.createBooleanSymbol("CMP_CM1CON_CPOL", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_CPOL.setLabel(cmpBitFld_CM1CON_CPOL.getAttribute("caption"))

    #Comparator output on pin
    cmpSym_CM1CON_COE = cmpComponent.createBooleanSymbol("CMP_CM1CON_COE", cmpSym_CM1CON_STRING)
    cmpSym_CM1CON_COE.setLabel(cmpBitFld_CM1CON_COE.getAttribute("caption"))
    cmpSym_CM1CON_COE.setDefaultValue(False)

    cmpSym_CM2CON_STRING = cmpComponent.createCommentSymbol("CMP2_STRING", None)
    cmpSym_CM2CON_STRING.setLabel("Comparator 2")

    #Positive input of Comparator 2
    cmp2CREF_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_CREF, cmp2CREF_names)
    cmpSym_CM2CON_CREF = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_CREF", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CREF.setLabel(cmpBitFld_CM2CON_CREF.getAttribute("caption"))
    cmpSym_CM2CON_CREF.setDefaultValue(0)
    cmpSym_CM2CON_CREF.setOutputMode("Value")
    cmpSym_CM2CON_CREF.setDisplayMode("Description")
    for ii in cmp2CREF_names:
        cmpSym_CM2CON_CREF.addKey( ii['desc'], ii['value'], ii['key'] )

    #Negative input of Comparator 2
    cmp2CCH_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_CCH, cmp2CCH_names)
    cmpSym_CM2CON_CCH = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_CCH", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CCH.setLabel(cmpBitFld_CM2CON_CCH.getAttribute("caption"))
    cmpSym_CM2CON_CCH.setDefaultValue(0)
    cmpSym_CM2CON_CCH.setOutputMode("Value")
    cmpSym_CM2CON_CCH.setDisplayMode("Description")
    for ii in cmp2CCH_names:
        cmpSym_CM2CON_CCH.addKey( ii['desc'], ii['value'], ii['key'] )

    #Edge selection for interrupt generation
    cmp2EVPOL_names = []
    _get_bitfield_names(cmpValGrp_CM2CON_EVPOL, cmp2EVPOL_names)
    cmpSym_CM2CON_EVPOL = cmpComponent.createKeyValueSetSymbol("CMP_CM2CON_EVPOL", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_EVPOL.setLabel(cmpBitFld_CM2CON_EVPOL.getAttribute("caption"))
    cmpSym_CM2CON_EVPOL.setDefaultValue(0)
    cmpSym_CM2CON_EVPOL.setOutputMode("Value")
    cmpSym_CM2CON_EVPOL.setDisplayMode("Description")
    for ii in cmp2EVPOL_names:
        cmpSym_CM2CON_EVPOL.addKey( ii['desc'], ii['value'], ii['key'] )

    #Comparator output invert
    cmpSym_CM2CON_CPOL = cmpComponent.createBooleanSymbol("CMP_CM2CON_CPOL", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_CPOL.setLabel(cmpBitFld_CM2CON_CPOL.getAttribute("caption"))
    cmpSym_CM2CON_CPOL.setDefaultValue(False)

    #Comparator output on pin
    cmpSym_CM2CON_COE = cmpComponent.createBooleanSymbol("CMP_CM2CON_COE", cmpSym_CM2CON_STRING)
    cmpSym_CM2CON_COE.setLabel(cmpBitFld_CM2CON_COE.getAttribute("caption"))
    cmpSym_CM2CON_COE.setDefaultValue(False)

    #Collecting user input to combine into CMPxCON register
    #CMPxCON is updated every time a user selection changes
    cmpSym_CMP1CON = cmpComponent.createHexSymbol("CM1CON_VALUE", None)
    cmpSym_CMP1CON.setDefaultValue(0)
    cmpSym_CMP1CON.setVisible(False)
    cmpSym_CMP1CON.setDependencies(combine1Values, ["CMP_CM1CON_CREF", "CMP_CM1CON_CCH", "CMP_CM1CON_EVPOL", "CMP_CM1CON_CPOL", "CMP_CM1CON_COE"])

    cmpSym_CMP2CON = cmpComponent.createHexSymbol("CM2CON_VALUE", None)
    cmpSym_CMP2CON.setDefaultValue(0)
    cmpSym_CMP2CON.setVisible(False)
    cmpSym_CMP2CON.setDependencies(combine2Values, ["CMP_CM2CON_CREF", "CMP_CM2CON_CCH", "CMP_CM2CON_EVPOL", "CMP_CM2CON_CPOL", "CMP_CM2CON_COE"])

    #Calculate the proper interrupt registers using IRQ#
    cmp1Irq = "COMPARATOR_1"
    cmp1InterruptVector = cmp1Irq + "_INTERRUPT_ENABLE"
    cmp1InterruptHandler = cmp1Irq + "_INTERRUPT_HANDLER"
    cmp1InterruptHandlerLock = cmp1Irq + "_INTERRUPT_HANDLER_LOCK"
    cmp1InterruptVectorUpdate = cmp1Irq + "_INTERRUPT_ENABLE_UPDATE"
    cmp1Irq_index = int(getIRQnumber(cmp1Irq))

    cmp1EnblRegName = _get_enblReg_parms(cmp1Irq_index)
    cmp1StatRegName = _get_statReg_parms(cmp1Irq_index)

    #CMP1 IEC REG
    cmp1IEC = cmpComponent.createStringSymbol("CMP1_IEC_REG", None)
    cmp1IEC.setDefaultValue(cmp1EnblRegName)
    cmp1IEC.setVisible(False)

    #CMP1 IFS REG
    cmp1IFS = cmpComponent.createStringSymbol("CMP1_IFS_REG", None)
    cmp1IFS.setDefaultValue(cmp1StatRegName)
    cmp1IFS.setVisible(False)

    #Calculate the proper interrupt registers using IRQ#
    cmp2Irq = "COMPARATOR_2"
    cmp2InterruptVector = cmp2Irq + "_INTERRUPT_ENABLE"
    cmp2InterruptHandler = cmp2Irq + "_INTERRUPT_HANDLER"
    cmp2InterruptHandlerLock = cmp2Irq + "_INTERRUPT_HANDLER_LOCK"
    cmp2InterruptVectorUpdate = cmp2Irq + "_INTERRUPT_ENABLE_UPDATE"
    cmp2Irq_index = int(getIRQnumber(cmp2Irq))

    cmp2EnblRegName = _get_enblReg_parms(cmp2Irq_index)
    cmp2StatRegName = _get_statReg_parms(cmp2Irq_index)

    #CMP2 IEC REG
    cmp2IEC = cmpComponent.createStringSymbol("CMP2_IEC_REG", None)
    cmp2IEC.setDefaultValue(cmp2EnblRegName)
    cmp2IEC.setVisible(False)

    #CMP2 IFS REG
    cmp2IFS = cmpComponent.createStringSymbol("CMP2_IFS_REG", None)
    cmp2IFS.setDefaultValue(cmp2StatRegName)
    cmp2IFS.setVisible(False)

############################################################################
#### Dependency ####
############################################################################

    # EVIC Dynamic settings
    # Dependency Status
    cmpSymInt1EnComment = cmpComponent.createCommentSymbol("CMP1_INTERRUPT_ENABLE_COMMENT", cmpSym_CM1CON_STRING)
    cmpSymInt1EnComment.setVisible(False)
    cmpSymInt1EnComment.setLabel("Warning!!! Comparator 1 Interrupt is Disabled in Interrupt Manager")
    cmpSymInt1EnComment.setDependencies(updateCMP1InterruptData, ["CMP_CM1CON_EVPOL", "core." + cmp1InterruptVectorUpdate])

    cmpSymInt2EnComment = cmpComponent.createCommentSymbol("CMP2_INTERRUPT_ENABLE_COMMENT", cmpSym_CM2CON_STRING)
    cmpSymInt2EnComment.setVisible(False)
    cmpSymInt2EnComment.setLabel("Warning!!! Comparator 2 Interrupt is Disabled in Interrupt Manager")
    cmpSymInt2EnComment.setDependencies(updateCMP2InterruptData, ["CMP_CM2CON_EVPOL", "core." + cmp2InterruptVectorUpdate])

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
    cmpSystemInitFile.setSourcePath("../peripheral/cmp_00866/templates/system/system_initialize.c.ftl")
    cmpSystemInitFile.setMarkup(True)

    cmpSystemDefFile = cmpComponent.createFileSymbol("CMP_DEF", None)
    cmpSystemDefFile.setType("STRING")
    cmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cmpSystemDefFile.setSourcePath("../peripheral/cmp_00866/templates/system/system_definitions.h.ftl")
    cmpSystemDefFile.setMarkup(True)

