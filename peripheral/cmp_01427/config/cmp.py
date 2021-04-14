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

cmpValGrp_CMx_CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CCH"]')
cmpValGrp_CMx_CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CREF"]')
cmpValGrp_CMx_CON_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CPOL"]')
cmpValGrp_CMx_CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__EVPOL"]')
cmpValGrp_CMx_CON_HYSSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__HYSSEL"]')
cmpValGrp_CMx_CON_HYSPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__HYSPOL"]')
cmpValGrp_CMx_CON_CFSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CFSEL"]')
cmpValGrp_CMx_CON_CFDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1CON__CFDIV"]')

cmpBitFld_CMSTAT_SIDL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CMSTAT"]/bitfield@[name="SIDL"]')
cmpBitFld_CMSTAT_CVREFSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CMSTAT"]/bitfield@[name="CVREFSEL"]')
cmpValGrp_CMSTAT_CVREFSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CMSTAT__CVREFSEL"]')

cmpBitFld_CMx_CON_OPAON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="OPAON"]')
cmpBitFld_CMx_CON_ENPGA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="ENPGA"]')
cmpBitFld_CMx_CON_HYSPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="HYSPOL"]')
cmpBitFld_CMx_CON_HYSSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="HYSSEL"]')
cmpBitFld_CMx_CON_CFSEL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CFSEL"]')
cmpBitFld_CMx_CON_CFLTREN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CFLTREN"]')
cmpBitFld_CMx_CON_CFDIV = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CFDIV"]')
cmpBitFld_CMx_CON_CCH = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CCH"]')
cmpBitFld_CMx_CON_CREF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CREF"]')
cmpBitFld_CMx_CON_EVPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="EVPOL"]')
cmpBitFld_CMx_CON_AMPMOD = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="AMPMOD"]')
cmpBitFld_CMx_CON_OAO = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="OAO"]')
cmpBitFld_CMx_CON_OPLPWR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="OPLPWR"]')
cmpBitFld_CMx_CON_CPOL = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="CPOL"]')
cmpBitFld_CMx_CON_COE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1CON"]/bitfield@[name="COE"]')

if( ("PIC32MK" in Variables.get("__PROCESSOR")) and (("MC" in Variables.get("__PROCESSOR"))) ):
    #Register information for Blanking Function
    cmpValGrp_CMx_MSKCON_SELSRCA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/value-group@[name="CM1MSKCON__SELSRCA"]')

    cmpBitFld_CMx_MSKCON_AANEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="AANEN"]')
    cmpBitFld_CMx_MSKCON_AAEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="AAEN"]')
    cmpBitFld_CMx_MSKCON_ABNEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="ABNEN"]')
    cmpBitFld_CMx_MSKCON_ABEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="ABEN"]')
    cmpBitFld_CMx_MSKCON_ACNEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="ACNEN"]')
    cmpBitFld_CMx_MSKCON_ACEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="ACEN"]')
    cmpBitFld_CMx_MSKCON_PAGS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="PAGS"]')
    cmpBitFld_CMx_MSKCON_NAGS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="NAGS"]')
    cmpBitFld_CMx_MSKCON_OANEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OANEN"]')
    cmpBitFld_CMx_MSKCON_OAEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OAEN"]')
    cmpBitFld_CMx_MSKCON_OBNEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OBNEN"]')
    cmpBitFld_CMx_MSKCON_OBEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OBEN"]')
    cmpBitFld_CMx_MSKCON_OCNEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OCNEN"]')
    cmpBitFld_CMx_MSKCON_OCEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="OCEN"]')
    cmpBitFld_CMx_MSKCON_HLMS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="HLMS"]')
    cmpBitFld_CMx_MSKCON_SELSRCA = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]/register@[name="CM1MSKCON"]/bitfield@[name="SELSRCA"]')

################################################################################
#### Global Variables ####
################################################################################

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()


################################################################################
#### Business Logic ####
################################################################################

def _survey_bitfields(regname, destlist):
    '''
    This reads atdf file for register 'regname', and populates destlist with list of all bitfields within that register.
    Arguments:
        regname - register being looked at
        destlist - list of all bitfields present in the register
    '''
    registerGroup = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CMP"]/register-group@[name="CMP"]')
    register = registerGroup.getChildren()
    for ii in register:
        if(ii.getAttribute("name") == regname):
            bitFields = ii.getChildren()
            for jj in bitFields:
                destlist.append(jj.getAttribute("name"))

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

def getIRQnumber(string):

    for param in interruptsChildren:
        modInst = param.getAttribute("name")
        if string == modInst:
            irq_index = param.getAttribute("index")

    return irq_index

def setCMPxInterruptData(status, cmp_id):

    comparator_id = str(cmp_id)

    cmpxInterruptVector = "COMPARATOR_" + comparator_id + "_INTERRUPT_ENABLE"
    cmpxInterruptHandler = "COMPARATOR_" + comparator_id + "_INTERRUPT_HANDLER"
    cmpxInterruptHandlerLock = "COMPARATOR_" + comparator_id + "_INTERRUPT_HANDLER_LOCK"
    cmpxInterruptVectorUpdate ="COMPARATOR_" + comparator_id + "_INTERRUPT_ENABLE_UPDATE"

    Database.setSymbolValue("core", cmpxInterruptVector, status, 1)
    Database.setSymbolValue("core", cmpxInterruptHandlerLock, status, 1)

    interruptName = cmpxInterruptHandler.split("_INTERRUPT_HANDLER")[0]

    if status == True:
        Database.setSymbolValue("core", cmpxInterruptHandler, interruptName + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", cmpxInterruptHandler, interruptName + "_Handler", 1)

def updateCMPxInterruptData(MySymbol, event):

    dep_symbol = event["symbol"].getID()
    symbol_parts = (dep_symbol.split('_', 2))
    cmp_id = int(symbol_parts[1])

    cmpxInterruptVectorUpdate = "COMPARATOR_" + str(cmp_id) + "_INTERRUPT_ENABLE_UPDATE"
    cmpxEvpolId = "CMP_" + str(cmp_id) + "_CON_EVPOL"

    #Comparator IDs starts from 1 but the array index starts from 0
    #Use 'cmp_id - 1' when accessing config value arrays
    status = int(cmpSym_CMx_CON_EVPOL[cmp_id - 1].getSelectedValue()) != 0

    if event["id"] == cmpxEvpolId:
        setCMPxInterruptData(status, cmp_id)

    if Database.getSymbolValue("core", cmpxInterruptVectorUpdate) == True and status == True:
        MySymbol.setVisible(True)
    else:
        MySymbol.setVisible(False)

def combineCMSTATConfigValues(MySymbol, event):
    global cmpSym_CMSTAT_SIDL
    global cmpSym_CMSTAT_CVREFSEL
    cvrefselValue = 0
    sidlValue     = int(cmpSym_CMSTAT_SIDL.getValue()) << 13
    if event["id"] == "CMP_CMSTAT_CVREFSEL":
        cvrefselValue    = cmpSym_CMSTAT_CVREFSEL.getValue() << 8
    cmstatValue = sidlValue | cvrefselValue
    MySymbol.setValue(cmstatValue)

def combineCMxCONConfigValues(MySymbol, event):

    dep_symbol = event["symbol"].getID()
    symbol_parts = (dep_symbol.split('_', 2))
    cmp_id = int(symbol_parts[1]) - 1

    cchValue     = cmpSym_CMx_CON_CCH[cmp_id].getValue() << 0
    crefValue    = cmpSym_CMx_CON_CREF[cmp_id].getValue() << 4
    evpolValue   = cmpSym_CMx_CON_EVPOL[cmp_id].getValue() << 6
    if cmpSym_CMx_CON_AMPMOD_present[cmp_id] == True:
        ampmodValue  = cmpSym_CMx_CON_AMPMOD[cmp_id].getValue() << 10
    else:
        ampmodValue = 0
    if cmpSym_CMx_CON_OAO_present[cmp_id] == True:
        oaoValue     = cmpSym_CMx_CON_OAO[cmp_id].getValue() << 11
    else:
        oaoValue = 0
    oplpwrValue  = cmpSym_CMx_CON_OPLPWR[cmp_id].getValue() << 12
    cpolValue    = cmpSym_CMx_CON_CPOL[cmp_id].getValue() << 13
    coeValue     = cmpSym_CMx_CON_COE[cmp_id].getValue() << 14
    cfdivValue   = cmpSym_CMx_CON_CFDIV[cmp_id].getValue() << 16
    cfltrenValue = cmpSym_CMx_CON_CFLTREN[cmp_id].getValue() << 19
    cfselValue   = cmpSym_CMx_CON_CFSEL[cmp_id].getValue() << 20
    hysselValue  = cmpSym_CMx_CON_HYSSEL[cmp_id].getValue() << 24
    hyspolValue  = cmpSym_CMx_CON_HYSPOL[cmp_id].getValue() << 28
    enpgaValue   = cmpSym_CMx_CON_ENPGA[cmp_id].getValue() << 30
    opaonValue   = cmpSym_CMx_CON_OPAON[cmp_id].getValue() << 31

    cmconValue = crefValue + cchValue + evpolValue + ampmodValue + oaoValue + cpolValue + coeValue + cfdivValue + cfltrenValue + cfselValue + hysselValue + hyspolValue + enpgaValue + opaonValue
    MySymbol.setValue(cmconValue, 2)

#Control HLMS visibility
def setHLMSVisibility(MySymbol, event):

    dep_symbol = event["symbol"].getID()
    symbol_parts = (dep_symbol.split('_', 2))
    cmp_id = int(symbol_parts[1]) - 1

    symObj = event["symbol"]
    if symObj.getValue() == True:
        cmpSym_CMx_MSKCON_HLMS[cmp_id].setValue(False,2)
    else:
        cmpSym_CMx_MSKCON_HLMS[cmp_id].setValue(True,2)

def combineCMxMSKCONConfigValues(MySymbol, event):

    dep_symbol = event["symbol"].getID()
    symbol_parts = (dep_symbol.split('_', 2))
    cmp_id = int(symbol_parts[1]) - 1

    aanenValue   = cmpSym_CMx_MSKCON_AANEN[cmp_id].getValue() << 0
    aaenValue    = cmpSym_CMx_MSKCON_AAEN[cmp_id].getValue() << 1
    abnenValue   = cmpSym_CMx_MSKCON_ABNEN[cmp_id].getValue() << 2
    abenValue    = cmpSym_CMx_MSKCON_ABEN[cmp_id].getValue() << 3
    acnenValue   = cmpSym_CMx_MSKCON_ACNEN[cmp_id].getValue() << 4
    acenValue    = cmpSym_CMx_MSKCON_ACEN[cmp_id].getValue() << 5
    pagsValue    = cmpSym_CMx_MSKCON_PAGS[cmp_id].getValue() << 6
    nagsValue    = cmpSym_CMx_MSKCON_NAGS[cmp_id].getValue() << 7
    oanenValue   = cmpSym_CMx_MSKCON_OANEN[cmp_id].getValue() << 8
    oaenValue    = cmpSym_CMx_MSKCON_OAEN[cmp_id].getValue() << 9
    obnenValue   = cmpSym_CMx_MSKCON_OBNEN[cmp_id].getValue() << 10
    obenValue    = cmpSym_CMx_MSKCON_OBEN[cmp_id].getValue() << 11
    ocnenValue   = cmpSym_CMx_MSKCON_OCNEN[cmp_id].getValue() << 12
    ocenValue    = cmpSym_CMx_MSKCON_OCEN[cmp_id].getValue() << 13
    hlmsValue    = cmpSym_CMx_MSKCON_HLMS[cmp_id].getValue() << 15
    selsrcaValue = cmpSym_CMx_MSKCON_SELSRCA[cmp_id].getValue() << 16
    selsrcbValue = cmpSym_CMx_MSKCON_SELSRCB[cmp_id].getValue() << 20
    selsrccValue = cmpSym_CMx_MSKCON_SELSRCC[cmp_id].getValue() << 24

    cmxmskconValue = aanenValue + aaenValue + abnenValue + abenValue + acnenValue + acenValue + pagsValue + nagsValue + oanenValue + oaenValue + obnenValue + obenValue + ocnenValue + ocenValue + hlmsValue + selsrcaValue + selsrcbValue + selsrccValue

    MySymbol.setValue(cmxmskconValue, 2)

def updateCMPxClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def updateOPAMPxClockData(symbol, event):

    opampId = symbol.getID().split("_")[0]
    index = opampId.replace("OPAMP", "")

    #Comparator IDs starts from 1 but the array index starts from 0
    #Use 'cmp_id - 1' when accessing config value arrays
    status = cmpSym_CMx_CON_AMPMOD[int(index) - 1].getValue()

    if "_CON_AMPMOD" in event["id"]:
        Database.setSymbolValue("core", opampId + "_CLOCK_ENABLE", event["value"], 1)

    if Database.getSymbolValue("core", opampId + "_CLOCK_ENABLE") == False and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

################################################################################
#### Component ####
################################################################################

def instantiateComponent(cmpComponent):

    global cmpInstanceName

    global cmpxIEC
    cmpxIEC = []
    global cmpxIFS
    cmpxIFS = []
    global cmp_x_InterruptVector
    cmp_x_InterruptVector = []
    global cmp_x_InterruptHandlerLock
    cmp_x_InterruptHandlerLock = []
    global cmp_x_InterruptHandler
    cmp_x_InterruptHandlerLock = []
    global cmp_x_InterruptVectorUpdate
    cmp_x_InterruptVectorUpdate = []

    global cmpSym_CMx_CON_CREF
    cmpSym_CMx_CON_CREF = []
    global cmpSym_CMx_CON_CCH
    cmpSym_CMx_CON_CCH = []
    global cmpSym_CMx_CON_EVPOL
    cmpSym_CMx_CON_EVPOL = []
    global cmpSym_CMx_CON_AMPMOD
    cmpSym_CMx_CON_AMPMOD = []
    global cmpSym_CMx_CON_AMPMOD_present
    cmpSym_CMx_CON_AMPMOD_present = []
    global cmpSym_CMx_CON_OAO
    cmpSym_CMx_CON_OAO = []
    global cmpSym_CMx_CON_OAO_present
    cmpSym_CMx_CON_OAO_present = []
    global cmpSym_CMx_CON_OPLPWR
    cmpSym_CMx_CON_OPLPWR = []
    global cmpSym_CMx_CON_OPLPWR_present
    cmpSym_CMx_CON_OPLPWR_present = []
    global cmpSym_CMx_CON_CPOL
    cmpSym_CMx_CON_CPOL = []
    global cmpSym_CMx_CON_COE
    cmpSym_CMx_CON_COE = []
    global cmpSym_CMx_CON_OPAON
    cmpSym_CMx_CON_OPAON = []
    global cmpSym_CMx_CON_OPAON_present
    cmpSym_CMx_CON_OPAON_present = []
    global cmpSym_CMx_CON_ENPGA
    cmpSym_CMx_CON_ENPGA = []
    global cmpSym_CMx_CON_ENPGA_present
    cmpSym_CMx_CON_ENPGA_present = []
    global cmpSym_CMx_CON_HYSPOL
    cmpSym_CMx_CON_HYSPOL = []
    global cmpSym_CMx_CON_HYSPOL_present
    cmpSym_CMx_CON_HYSPOL_present = []
    global cmpSym_CMx_CON_HYSSEL
    cmpSym_CMx_CON_HYSSEL = []
    global cmpSym_CMx_CON_HYSSEL_present
    cmpSym_CMx_CON_HYSSEL_present = []
    global cmpSym_CMx_CON_CFSEL
    cmpSym_CMx_CON_CFSEL = []
    global cmpSym_CMx_CON_CFSEL_present
    cmpSym_CMx_CON_CFSEL_present = []
    global cmpSym_CMx_CON_CFLTREN
    cmpSym_CMx_CON_CFLTREN = []
    global cmpSym_CMx_CON_CFLTREN_present
    cmpSym_CMx_CON_CFLTREN_present = []
    global cmpSym_CMx_CON_CFDIV
    cmpSym_CMx_CON_CFDIV = []
    global cmpSym_CMx_CON_CFDIV_present
    cmpSym_CMx_CON_CFDIV_present = []

    global cmpSym_CMxCON
    cmpSym_CMxCON = []
    global cmpSym_CMxMSKCON
    cmpSym_CMxMSKCON = []

    global cmpSymIntxEnComment
    cmpSymIntxEnComment = []
    global cmpSym_CMx_CON_STRING
    cmpSym_CMx_CON_STRING = []

    if( ("PIC32MK" in Variables.get("__PROCESSOR")) and (("MC" in Variables.get("__PROCESSOR"))) ):
        global cmpSym_CMx_MSKCON_STRING
        cmpSym_CMx_MSKCON_STRING = []
        global cmpSym_CMx_MSKCON_SUBMENU_MASKA
        cmpSym_CMx_MSKCON_SUBMENU_MASKA = []
        global cmpSym_CMx_MSKCON_SUBMENU_MASKB
        cmpSym_CMx_MSKCON_SUBMENU_MASKB = []
        global cmpSym_CMx_MSKCON_SUBMENU_MASKC
        cmpSym_CMx_MSKCON_SUBMENU_MASKC = []
        global cmpSym_CMx_MSKCON_SELSRCA
        cmpSym_CMx_MSKCON_SELSRCA = []
        global cmpSym_CMx_MSKCON_SELSRCB
        cmpSym_CMx_MSKCON_SELSRCB = []
        global cmpSym_CMx_MSKCON_SELSRCC
        cmpSym_CMx_MSKCON_SELSRCC = []
        global cmpSym_CMx_MSKCON_AANEN
        cmpSym_CMx_MSKCON_AANEN = []
        global cmpSym_CMx_MSKCON_AAEN
        cmpSym_CMx_MSKCON_AAEN = []
        global cmpSym_CMx_MSKCON_ABNEN
        cmpSym_CMx_MSKCON_ABNEN = []
        global cmpSym_CMx_MSKCON_ABEN
        cmpSym_CMx_MSKCON_ABEN = []
        global cmpSym_CMx_MSKCON_ACNEN
        cmpSym_CMx_MSKCON_ACNEN = []
        global cmpSym_CMx_MSKCON_ACEN
        cmpSym_CMx_MSKCON_ACEN = []
        global cmpSym_CMx_MSKCON_PAGS
        cmpSym_CMx_MSKCON_PAGS = []
        global cmpSym_CMx_MSKCON_NAGS
        cmpSym_CMx_MSKCON_NAGS = []
        global cmpSym_CMx_MSKCON_OANEN
        cmpSym_CMx_MSKCON_OANEN = []
        global cmpSym_CMx_MSKCON_OAEN
        cmpSym_CMx_MSKCON_OAEN = []
        global cmpSym_CMx_MSKCON_OBNEN
        cmpSym_CMx_MSKCON_OBNEN = []
        global cmpSym_CMx_MSKCON_OBEN
        cmpSym_CMx_MSKCON_OBEN = []
        global cmpSym_CMx_MSKCON_OCNEN
        cmpSym_CMx_MSKCON_OCNEN = []
        global cmpSym_CMx_MSKCON_OCEN
        cmpSym_CMx_MSKCON_OCEN = []
        global cmpSym_CMx_MSKCON_HLMS
        cmpSym_CMx_MSKCON_HLMS = []

    cmpInstanceName = cmpComponent.createStringSymbol("CMP_INSTANCE_NAME", None)
    cmpInstanceName.setVisible(False)
    cmpInstanceName.setDefaultValue(cmpComponent.getID().upper())
    print("Running " + cmpInstanceName.getValue())

    #Stop in Idle mode if device is not
    global cmpSym_CMSTAT_SIDL
    cmpSym_CMSTAT_SIDL = cmpComponent.createBooleanSymbol("CMP_CMSTAT_SIDL", None)
    cmpSym_CMSTAT_SIDL.setLabel(cmpBitFld_CMSTAT_SIDL.getAttribute("caption"))
    cmpSym_CMSTAT_SIDL.setDefaultValue(False)

    global cmpSym_CMSTAT_CVREFSEL
    if cmpValGrp_CMSTAT_CVREFSEL is not None:
        CMSTAT_CVREFSEL_names = []
        _get_bitfield_names(cmpValGrp_CMSTAT_CVREFSEL, CMSTAT_CVREFSEL_names)
        cmpSym_CMSTAT_CVREFSEL = cmpComponent.createKeyValueSetSymbol("CMP_CMSTAT_CVREFSEL", None)
        cmpSym_CMSTAT_CVREFSEL.setLabel(cmpBitFld_CMSTAT_CVREFSEL.getAttribute("caption"))
        cmpSym_CMSTAT_CVREFSEL.setDefaultValue(0)
        cmpSym_CMSTAT_CVREFSEL.setOutputMode("Value")
        cmpSym_CMSTAT_CVREFSEL.setDisplayMode("Description")
        for ii in CMSTAT_CVREFSEL_names:
            cmpSym_CMSTAT_CVREFSEL.addKey( ii['desc'], ii['value'], ii['key'] )

    #Collecting user input to combine into CMSTAT register
    #CMSTAT is updated every time a user selection changes
    cmpSym_CMSTAT = cmpComponent.createHexSymbol("CMP_CMSTAT_VALUE", None)
    cmpSym_CMSTAT.setDefaultValue(0)
    cmpSym_CMSTAT.setVisible(False)
    cmpSym_CMSTAT.setDependencies(combineCMSTATConfigValues, ["CMP_CMSTAT_SIDL", "CMP_CMSTAT_CVREFSEL"])

    #Generate menu for all comparators and Op Amps in the CMP peripheral
    node = ATDF.getNode('/avr-tools-device-file/devices/device/parameters/param@[name="__NUM_CMP_CHANNELS"]')
    numOfCMPInstances = int(node.getAttribute("value"))

    cmpSym_CMP_NUM = cmpComponent.createIntegerSymbol("CMP_NUM_OF_INSTANCES", None)
    cmpSym_CMP_NUM.setVisible(False)
    cmpSym_CMP_NUM.setDefaultValue(numOfCMPInstances)

    for id in range(0, numOfCMPInstances):
        # generate list of all bitfields present in CMxCON register - varies from family to family, and within certain families as well
        CMxCON_list = []
        _survey_bitfields("CM"+str(id+1)+"CON", CMxCON_list)  # CMxCON_list is used below, to prevent accessing (absent) elements in the atdf file   
        cmpSym_CMx_CON_STRING.append(id)
        cmpSym_CMx_CON_STRING[id] = cmpComponent.createCommentSymbol("cmp_x_STRING_" + str(id + 1), None)
        if(("OPAON" in CMxCON_list) or (("AMPMOD" in CMxCON_list) and (id != 3))):
            cmpSym_CMx_CON_STRING[id].setLabel("Op amp / Comparator " + str(id + 1))
        else:
            cmpSym_CMx_CON_STRING[id].setLabel("Comparator " + str(id + 1))

        #Clock enable
        Database.setSymbolValue("core", "CMP" + str(id + 1) + "_CLOCK_ENABLE", True, 1)

        #Positive input of Comparator x
        cmp_x_CREF_names = []
        cmpSym_CMx_CON_CREF.append(id)
        _get_bitfield_names(cmpValGrp_CMx_CON_CREF, cmp_x_CREF_names)
        cmpSym_CMx_CON_CREF[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_CON_CREF", cmpSym_CMx_CON_STRING[id])
        cmpSym_CMx_CON_CREF[id].setLabel(cmpBitFld_CMx_CON_CREF.getAttribute("caption"))
        cmpSym_CMx_CON_CREF[id].setDefaultValue(0)
        cmpSym_CMx_CON_CREF[id].setOutputMode("Value")
        cmpSym_CMx_CON_CREF[id].setDisplayMode("Description")
        for ii in cmp_x_CREF_names:
            cmpSym_CMx_CON_CREF[id].addKey( ii['desc'], ii['value'], ii['key'] )

        #Negative input of Comparator x
        cmp_x_CCH_names = []
        cmpSym_CMx_CON_CCH.append(id)
        _get_bitfield_names(cmpValGrp_CMx_CON_CCH, cmp_x_CCH_names)
        cmpSym_CMx_CON_CCH[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_CON_CCH", cmpSym_CMx_CON_STRING[id])
        cmpSym_CMx_CON_CCH[id].setLabel(cmpValGrp_CMx_CON_CCH.getAttribute("caption"))
        cmpSym_CMx_CON_CCH[id].setDefaultValue(0)
        cmpSym_CMx_CON_CCH[id].setOutputMode("Value")
        cmpSym_CMx_CON_CCH[id].setDisplayMode("Description")
        for ii in cmp_x_CCH_names:
            cmpSym_CMx_CON_CCH[id].addKey( ii['desc'], ii['value'], ii['key'] )

        #Edge selection for interrupt generation
        cmp_x_EVPOL_names = []
        cmpSym_CMx_CON_EVPOL.append(id)
        _get_bitfield_names(cmpValGrp_CMx_CON_EVPOL, cmp_x_EVPOL_names)
        cmpSym_CMx_CON_EVPOL[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_CON_EVPOL", cmpSym_CMx_CON_STRING[id])
        cmpSym_CMx_CON_EVPOL[id].setLabel(cmpBitFld_CMx_CON_EVPOL.getAttribute("caption"))
        cmpSym_CMx_CON_EVPOL[id].setDefaultValue(0)
        cmpSym_CMx_CON_EVPOL[id].setOutputMode("Value")
        cmpSym_CMx_CON_EVPOL[id].setDisplayMode("Description")
        for ii in cmp_x_EVPOL_names:
            cmpSym_CMx_CON_EVPOL[id].addKey( ii['desc'], ii['value'], ii['key'] )

        #Op amp Mode Enable - bitfield not present in all devices
        #Not available on Op Amp Comparator 4 (CM4)
        cmpSym_CMx_CON_AMPMOD.append(id)
        cmpSym_CMx_CON_AMPMOD_present.append(id)
        if (id != 3):
            cmpSym_CMx_CON_AMPMOD[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_AMPMOD", cmpSym_CMx_CON_STRING[id])
            if("AMPMOD" in CMxCON_list):
                cmpSym_CMx_CON_AMPMOD[id].setLabel(cmpBitFld_CMx_CON_AMPMOD.getAttribute("caption"))
                cmpSym_CMx_CON_AMPMOD_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_AMPMOD_PRESENT", cmpSym_CMx_CON_STRING[id])
                cmpSym_CMx_CON_AMPMOD_present[id].setVisible(False)
            else:
                cmpSym_CMx_CON_AMPMOD[id].setVisible(False)  # use default, false value - results in no impact to computed register value
            cmpSym_CMx_CON_AMPMOD[id].setDefaultValue(False)

        #Op amp Output Enable
        #Not available on Op Amp Comparator 4 (CM4)
        cmpSym_CMx_CON_OAO.append(id)
        cmpSym_CMx_CON_OAO_present.append(id)
        if (id != 3):
            cmpSym_CMx_CON_OAO[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OAO", cmpSym_CMx_CON_STRING[id])
            if("OAO" in CMxCON_list):
                cmpSym_CMx_CON_OAO[id].setLabel(cmpBitFld_CMx_CON_OAO.getAttribute("caption"))
                cmpSym_CMx_CON_OAO_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OAO_PRESENT", cmpSym_CMx_CON_STRING[id])
                cmpSym_CMx_CON_OAO_present[id].setVisible(False)
            else:
                cmpSym_CMx_CON_OAO[id].setVisible(False)
            cmpSym_CMx_CON_OAO[id].setDefaultValue(False)

        #Op amp Power Mode - bitfield not present in all devices
        cmpSym_CMx_CON_OPLPWR.append(id)
        cmpSym_CMx_CON_OPLPWR_present.append(id)
        cmpSym_CMx_CON_OPLPWR[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OPLPWR", cmpSym_CMx_CON_STRING[id])
        if(("OPLPWR" in CMxCON_list) and ("OPAON" in CMxCON_list)):
            cmpSym_CMx_CON_OPLPWR[id].setLabel("Op Amp Low Power Mode Enable bit")
            cmpSym_CMx_CON_OPLPWR_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OPLPWR_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_OPLPWR_present[id].setVisible(False)
        else:
            cmpSym_CMx_CON_OPLPWR[id].setVisible(False)
        cmpSym_CMx_CON_OPLPWR[id].setDefaultValue(False)

        #Comparator output invert
        cmp_x_CPOL_names = []
        _get_bitfield_names(cmpValGrp_CMx_CON_CPOL, cmp_x_CPOL_names)
        cmpSym_CMx_CON_CPOL.append(id)
        cmpSym_CMx_CON_CPOL[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_CON_CPOL", cmpSym_CMx_CON_STRING[id])
        cmpSym_CMx_CON_CPOL[id].setLabel(cmpBitFld_CMx_CON_CPOL.getAttribute("caption"))
        cmpSym_CMx_CON_CPOL[id].setOutputMode("Value")
        cmpSym_CMx_CON_CPOL[id].setDisplayMode("Description")
        for ii in cmp_x_CPOL_names:
            cmpSym_CMx_CON_CPOL[id].addKey( ii['desc'], ii['value'], ii['key'] )

        #Comparator output on pin
        cmpSym_CMx_CON_COE.append(id)
        cmpSym_CMx_CON_COE[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_COE", cmpSym_CMx_CON_STRING[id])
        cmpSym_CMx_CON_COE[id].setLabel(cmpBitFld_CMx_CON_COE.getAttribute("caption"))
        cmpSym_CMx_CON_COE[id].setDefaultValue(False)

        #Op amp enable - bitfield not present in all devices
        cmpSym_CMx_CON_OPAON.append(id)
        cmpSym_CMx_CON_OPAON_present.append(id)
        cmpSym_CMx_CON_OPAON[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OPAON", cmpSym_CMx_CON_STRING[id])
        if("OPAON" in CMxCON_list):
            cmpSym_CMx_CON_OPAON[id].setLabel(cmpBitFld_CMx_CON_OPAON.getAttribute("caption"))
            cmpSym_CMx_CON_OPAON_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_OPAON_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_OPAON_present[id].setVisible(False)
        else:
            cmpSym_CMx_CON_OPAON[id].setVisible(False)
        cmpSym_CMx_CON_OPAON[id].setDefaultValue(False)

        #Op amp fixed gain enable - bitfield not present in all devices
        cmpSym_CMx_CON_ENPGA.append(id)
        cmpSym_CMx_CON_ENPGA_present.append(id)
        cmpSym_CMx_CON_ENPGA[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_ENPGA", cmpSym_CMx_CON_STRING[id])
        if("ENPGA" in CMxCON_list):
            cmpSym_CMx_CON_ENPGA[id].setLabel("Opamp 1X Gain Mode Enable bit")
            cmpSym_CMx_CON_ENPGA_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_ENPGA_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_ENPGA_present[id].setVisible(False)
        else:
            cmpSym_CMx_CON_ENPGA[id].setVisible(False)
        cmpSym_CMx_CON_ENPGA[id].setDefaultValue(False)

        #Op amp Hysteresis Polarity Selection - bitfield not present in all devices
        cmp_x_HYSPOL_names = []
        cmpSym_CMx_CON_HYSPOL.append(id)
        cmpSym_CMx_CON_HYSPOL_present.append(id)
        cmpSym_CMx_CON_HYSPOL[id] =  cmpComponent.createKeyValueSetSymbol("CMP_"+str(id+1)+"_CON_HYSPOL", cmpSym_CMx_CON_STRING[id])
        if("HYSPOL" in CMxCON_list):
            _get_bitfield_names(cmpValGrp_CMx_CON_HYSPOL, cmp_x_HYSPOL_names)
            cmpSym_CMx_CON_HYSPOL[id].setLabel(cmpBitFld_CMx_CON_HYSPOL.getAttribute("caption"))
            cmpSym_CMx_CON_HYSPOL[id].setOutputMode("Value")
            cmpSym_CMx_CON_HYSPOL[id].setDisplayMode("Description")
            for ii in cmp_x_HYSPOL_names:
                cmpSym_CMx_CON_HYSPOL[id].addKey( ii['desc'], ii['value'], ii['key'] )            
            cmpSym_CMx_CON_HYSPOL_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_HYSPOL_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_HYSPOL_present[id].setVisible(False)
        else:
            cmpSym_CMx_CON_HYSPOL[id].setVisible(False)
        cmpSym_CMx_CON_HYSPOL[id].setDefaultValue(False)

        #Op amp Hysteresis Selection - bitfield not present in all devices
        cmpSym_CMx_CON_HYSSEL.append(id)
        cmpSym_CMx_CON_HYSSEL_present.append(id)
        if("HYSSEL" in CMxCON_list):
            cmpSym_CMx_CON_HYSSEL_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_HYSSEL_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_HYSSEL_present[id].setVisible(False)
            cmp_x_HYSSEL_names = []
            _get_bitfield_names(cmpValGrp_CMx_CON_HYSSEL, cmp_x_HYSSEL_names)
            cmpSym_CMx_CON_HYSSEL[id] =  cmpComponent.createKeyValueSetSymbol("CMP_"+str(id+1)+"_CON_HYSSEL", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_HYSSEL[id].setLabel(cmpBitFld_CMx_CON_HYSSEL.getAttribute("caption"))
            cmpSym_CMx_CON_HYSSEL[id].setDefaultValue(0)
            for ii in cmp_x_HYSSEL_names:
                cmpSym_CMx_CON_HYSSEL[id].addKey( ii['desc'], ii['value'], ii['key'] )
        else:
            cmpSym_CMx_CON_HYSSEL[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_HYSSEL", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_HYSSEL[id].setVisible(False)
            cmpSym_CMx_CON_HYSSEL[id].setDefaultValue(False)

        #Op amp Comparator Output Filter Clock Source Select - bitfield not present in all devices
        cmpSym_CMx_CON_CFSEL.append(id)
        cmpSym_CMx_CON_CFSEL_present.append(id)
        if("CFSEL" in CMxCON_list):
            cmpSym_CMx_CON_CFSEL_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFSEL_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFSEL_present[id].setVisible(False)
            cmp_x_CFSEL_names = []
            _get_bitfield_names(cmpValGrp_CMx_CON_CFSEL, cmp_x_CFSEL_names)
            cmpSym_CMx_CON_CFSEL[id] =  cmpComponent.createKeyValueSetSymbol("CMP_"+str(id+1)+"_CON_CFSEL", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFSEL[id].setLabel(cmpBitFld_CMx_CON_CFSEL.getAttribute("caption"))
            cmpSym_CMx_CON_CFSEL[id].setDefaultValue(0)
            for ii in cmp_x_CFSEL_names:
                cmpSym_CMx_CON_CFSEL[id].addKey( ii['desc'], ii['value'], ii['key'] )
        else:
            cmpSym_CMx_CON_CFSEL[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFSEL", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFSEL[id].setVisible(False)
            cmpSym_CMx_CON_CFSEL[id].setDefaultValue(False)

        #Op amp Comparator Output Digital Filter Enable - bitfield not present in all devices
        cmpSym_CMx_CON_CFLTREN.append(id)
        cmpSym_CMx_CON_CFLTREN_present.append(id)
        cmpSym_CMx_CON_CFLTREN[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFLTREN", cmpSym_CMx_CON_STRING[id])
        if("CFLTREN" in CMxCON_list):
            cmpSym_CMx_CON_CFLTREN[id].setLabel(cmpBitFld_CMx_CON_CFLTREN.getAttribute("caption"))
            cmpSym_CMx_CON_CFLTREN_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFLTREN_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFLTREN_present[id].setVisible(False)
        else:
            cmpSym_CMx_CON_CFLTREN[id].setVisible(False)
        cmpSym_CMx_CON_CFLTREN[id].setDefaultValue(False)

        #Op amp Comparator Output Filter Clock Divide Select - bitfield not present in all devices
        cmpSym_CMx_CON_CFDIV.append(id)
        cmpSym_CMx_CON_CFDIV_present.append(id)
        if("CFSEL" in CMxCON_list):
            cmpSym_CMx_CON_CFDIV_present[id] = cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFDIV_PRESENT", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFDIV_present[id].setVisible(False)
            cmp_x_CFDIV_names = []
            _get_bitfield_names(cmpValGrp_CMx_CON_CFDIV, cmp_x_CFDIV_names)
            cmpSym_CMx_CON_CFDIV[id] =  cmpComponent.createKeyValueSetSymbol("CMP_"+str(id+1)+"_CON_CFDIV", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFDIV[id].setLabel(cmpBitFld_CMx_CON_CFDIV.getAttribute("caption"))
            cmpSym_CMx_CON_CFDIV[id].setDefaultValue(0)
            for ii in cmp_x_CFDIV_names:
                cmpSym_CMx_CON_CFDIV[id].addKey( ii['desc'], ii['value'], ii['key'] )
        else:
            cmpSym_CMx_CON_CFDIV[id] =  cmpComponent.createBooleanSymbol("CMP_"+str(id+1)+"_CON_CFDIV", cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_CON_CFDIV[id].setVisible(False)
            cmpSym_CMx_CON_CFDIV[id].setDefaultValue(False)

        #Collecting user input to combine into CMPxCON register
        #CMPxCON is updated every time a user selection changes
        cmpSym_CMxCON.append(id)
        cmpSym_CMxCON[id] = cmpComponent.createHexSymbol("CMP_" +  str(id + 1) + "_CON_VALUE", None)
        cmpSym_CMxCON[id].setDefaultValue(0)
        cmpSym_CMxCON[id].setVisible(False)
        cmpSym_CMxCON[id].setDependencies(combineCMxCONConfigValues, ["CMP_"+str(id+1)+"_CON_CREF", "CMP_"+str(id+1)+"_CON_CCH", "CMP_"+str(id+1)+"_CON_EVPOL", "CMP_"+str(id+1)+"_CON_AMPMOD", "CMP_"+str(id+1)+"_CON_OAO", "CMP_"+str(id+1)+"_CON_CPOL", "CMP_"+str(id+1)+"_CON_COE", "CMP_"+str(id+1)+"_CON_OPAON", "CMP_"+str(id+1)+"_CON_ENPGA", "CMP_"+str(id+1)+"_CON_HYSPOL", "CMP_"+str(id+1)+"_CON_HYSSEL", "CMP_"+str(id+1)+"_CON_CFSEL", "CMP_"+str(id+1)+"_CON_CFLTREN", "CMP_"+str(id+1)+"_CON_CFDIV", "CMP_"+str(id+1)+"_CON_OPLPWR"])


        #Menu item for output blanking. Only available on PIC32MKxxMCxx devices.
        if( ("PIC32MK" in Variables.get("__PROCESSOR")) and (("MC" in Variables.get("__PROCESSOR"))) ):
            cmpSym_CMx_MSKCON_STRING.append(id)
            cmpSym_CMx_MSKCON_STRING[id] = cmpComponent.createCommentSymbol("cmp_x_MSKCON_STRING_" + str(id + 1), cmpSym_CMx_CON_STRING[id])
            cmpSym_CMx_MSKCON_STRING[id].setLabel("Output Blanking")

            #High or Low Level Masking Select
            #Takes the inverted value of CPOL
            cmpSym_CMx_MSKCON_HLMS.append(id)
            cmpSym_CMx_MSKCON_HLMS[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_HLMS", cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_HLMS[id].setLabel(cmpBitFld_CMx_MSKCON_HLMS.getAttribute("caption"))
            cmpSym_CMx_MSKCON_HLMS[id].setVisible(False)
            cmpSym_CMx_MSKCON_HLMS[id].setDependencies(setHLMSVisibility, ["CMP_" +  str(id + 1) + "_CON_CPOL"])

            #SubMenu item for Mask A configuration
            cmpSym_CMx_MSKCON_SUBMENU_MASKA.append(id)
            cmpSym_CMx_MSKCON_SUBMENU_MASKA[id] = cmpComponent.createCommentSymbol("cmp_x_SUBMENU_MASKA" + str(id + 1), cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_SUBMENU_MASKA[id].setLabel("Mask A configuration")

            #Mask A Input Select
            cmp_x_SELSRCA_names = []
            cmpSym_CMx_MSKCON_SELSRCA.append(id)
            _get_bitfield_names(cmpValGrp_CMx_MSKCON_SELSRCA, cmp_x_SELSRCA_names)
            cmpSym_CMx_MSKCON_SELSRCA[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_MSKCON_SELSRCA", cmpSym_CMx_MSKCON_SUBMENU_MASKA[id])
            cmpSym_CMx_MSKCON_SELSRCA[id].setLabel("Mask A Input Select bits")
            cmpSym_CMx_MSKCON_SELSRCA[id].setDefaultValue(0)
            cmpSym_CMx_MSKCON_SELSRCA[id].setOutputMode("Value")
            cmpSym_CMx_MSKCON_SELSRCA[id].setDisplayMode("Description")
            for ii in cmp_x_SELSRCA_names:
                cmpSym_CMx_MSKCON_SELSRCA[id].addKey( ii['desc'], ii['value'], ii['key'] )

            #AND Gate 'A' Inverted Input Enable
            cmpSym_CMx_MSKCON_AANEN.append(id)
            cmpSym_CMx_MSKCON_AANEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_AANEN", cmpSym_CMx_MSKCON_SUBMENU_MASKA[id])
            cmpSym_CMx_MSKCON_AANEN[id].setLabel(cmpBitFld_CMx_MSKCON_AANEN.getAttribute("caption"))

            #AND Gate 'A' Input Enable
            cmpSym_CMx_MSKCON_AAEN.append(id)
            cmpSym_CMx_MSKCON_AAEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_AAEN", cmpSym_CMx_MSKCON_SUBMENU_MASKA[id])
            cmpSym_CMx_MSKCON_AAEN[id].setLabel(cmpBitFld_CMx_MSKCON_AAEN.getAttribute("caption"))

            #OR Gate 'A' Inverted Input Enable
            cmpSym_CMx_MSKCON_OANEN.append(id)
            cmpSym_CMx_MSKCON_OANEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OANEN", cmpSym_CMx_MSKCON_SUBMENU_MASKA[id])
            cmpSym_CMx_MSKCON_OANEN[id].setLabel(cmpBitFld_CMx_MSKCON_OANEN.getAttribute("caption"))

            #OR Gate 'A' Input  Enable
            cmpSym_CMx_MSKCON_OAEN.append(id)
            cmpSym_CMx_MSKCON_OAEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OAEN", cmpSym_CMx_MSKCON_SUBMENU_MASKA[id])
            cmpSym_CMx_MSKCON_OAEN[id].setLabel(cmpBitFld_CMx_MSKCON_OAEN.getAttribute("caption"))

            #SubMenu item for Mask B configuration
            cmpSym_CMx_MSKCON_SUBMENU_MASKB.append(id)
            cmpSym_CMx_MSKCON_SUBMENU_MASKB[id] = cmpComponent.createCommentSymbol("cmp_x_SUBMENU_MASKB"+str(id+1), cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_SUBMENU_MASKB[id].setLabel("Mask B configuration")

            #Mask B Input Select
            cmpSym_CMx_MSKCON_SELSRCB.append(id)
            cmpSym_CMx_MSKCON_SELSRCB[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_MSKCON_SELSRCB", cmpSym_CMx_MSKCON_SUBMENU_MASKB[id])
            cmpSym_CMx_MSKCON_SELSRCB[id].setLabel("Mask B Input Select bits")
            cmpSym_CMx_MSKCON_SELSRCB[id].setDefaultValue(0)
            cmpSym_CMx_MSKCON_SELSRCB[id].setOutputMode("Value")
            cmpSym_CMx_MSKCON_SELSRCB[id].setDisplayMode("Description")
            for ii in cmp_x_SELSRCA_names:
                cmpSym_CMx_MSKCON_SELSRCB[id].addKey( ii['desc'], ii['value'], ii['key'] )

            #AND Gate 'B' Inverted Input Enable
            cmpSym_CMx_MSKCON_ABNEN.append(id)
            cmpSym_CMx_MSKCON_ABNEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_ABNEN", cmpSym_CMx_MSKCON_SUBMENU_MASKB[id])
            cmpSym_CMx_MSKCON_ABNEN[id].setLabel(cmpBitFld_CMx_MSKCON_ABNEN.getAttribute("caption"))

            #AND Gate 'B' Input Enable
            cmpSym_CMx_MSKCON_ABEN.append(id)
            cmpSym_CMx_MSKCON_ABEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_ABEN", cmpSym_CMx_MSKCON_SUBMENU_MASKB[id])
            cmpSym_CMx_MSKCON_ABEN[id].setLabel(cmpBitFld_CMx_MSKCON_ABEN.getAttribute("caption"))

            #OR Gate 'B' Inverted Input Enable
            cmpSym_CMx_MSKCON_OBNEN.append(id)
            cmpSym_CMx_MSKCON_OBNEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OBNEN", cmpSym_CMx_MSKCON_SUBMENU_MASKB[id])
            cmpSym_CMx_MSKCON_OBNEN[id].setLabel(cmpBitFld_CMx_MSKCON_OBNEN.getAttribute("caption"))

            #OR Gate 'B' Input  Enable
            cmpSym_CMx_MSKCON_OBEN.append(id)
            cmpSym_CMx_MSKCON_OBEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OBEN", cmpSym_CMx_MSKCON_SUBMENU_MASKB[id])
            cmpSym_CMx_MSKCON_OBEN[id].setLabel(cmpBitFld_CMx_MSKCON_OBEN.getAttribute("caption"))

            #SubMenu item for Mask C configuration
            cmpSym_CMx_MSKCON_SUBMENU_MASKC.append(id)
            cmpSym_CMx_MSKCON_SUBMENU_MASKC[id] = cmpComponent.createCommentSymbol("cmp_x_SUBMENU_MASKC"+str(id+1), cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_SUBMENU_MASKC[id].setLabel("Mask C configuration")

            #Mask C Input Select
            cmpSym_CMx_MSKCON_SELSRCC.append(id)
            cmpSym_CMx_MSKCON_SELSRCC[id] = cmpComponent.createKeyValueSetSymbol("CMP_" +  str(id + 1) + "_MSKCON_SELSRCC", cmpSym_CMx_MSKCON_SUBMENU_MASKC[id])
            cmpSym_CMx_MSKCON_SELSRCC[id].setLabel("Mask C Input Select bits")
            cmpSym_CMx_MSKCON_SELSRCC[id].setDefaultValue(0)
            cmpSym_CMx_MSKCON_SELSRCC[id].setOutputMode("Value")
            cmpSym_CMx_MSKCON_SELSRCC[id].setDisplayMode("Description")
            for ii in cmp_x_SELSRCA_names:
                cmpSym_CMx_MSKCON_SELSRCC[id].addKey( ii['desc'], ii['value'], ii['key'] )

            #AND Gate 'C' Inverted Input Enable
            cmpSym_CMx_MSKCON_ACNEN.append(id)
            cmpSym_CMx_MSKCON_ACNEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_ACNEN", cmpSym_CMx_MSKCON_SUBMENU_MASKC[id])
            cmpSym_CMx_MSKCON_ACNEN[id].setLabel(cmpBitFld_CMx_MSKCON_ACNEN.getAttribute("caption"))

            #AND Gate 'C' Input Enable
            cmpSym_CMx_MSKCON_ACEN.append(id)
            cmpSym_CMx_MSKCON_ACEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_ACEN", cmpSym_CMx_MSKCON_SUBMENU_MASKC[id])
            cmpSym_CMx_MSKCON_ACEN[id].setLabel(cmpBitFld_CMx_MSKCON_ACEN.getAttribute("caption"))

            #OR Gate 'C' Inverted Input Enable
            cmpSym_CMx_MSKCON_OCNEN.append(id)
            cmpSym_CMx_MSKCON_OCNEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OCNEN", cmpSym_CMx_MSKCON_SUBMENU_MASKC[id])
            cmpSym_CMx_MSKCON_OCNEN[id].setLabel(cmpBitFld_CMx_MSKCON_OCNEN.getAttribute("caption"))

            #OR Gate 'C' Input  Enable
            cmpSym_CMx_MSKCON_OCEN.append(id)
            cmpSym_CMx_MSKCON_OCEN[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_OCEN", cmpSym_CMx_MSKCON_SUBMENU_MASKC[id])
            cmpSym_CMx_MSKCON_OCEN[id].setLabel(cmpBitFld_CMx_MSKCON_OCEN.getAttribute("caption"))

            #Positive AND Gate Output Select
            cmpSym_CMx_MSKCON_PAGS.append(id)
            cmpSym_CMx_MSKCON_PAGS[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_PAGS", cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_PAGS[id].setLabel(cmpBitFld_CMx_MSKCON_PAGS.getAttribute("caption"))

            #Negative AND Gate Output Select
            cmpSym_CMx_MSKCON_NAGS.append(id)
            cmpSym_CMx_MSKCON_NAGS[id] = cmpComponent.createBooleanSymbol("CMP_" +  str(id + 1) + "_MSKCON_NAGS", cmpSym_CMx_MSKCON_STRING[id])
            cmpSym_CMx_MSKCON_NAGS[id].setLabel(cmpBitFld_CMx_MSKCON_NAGS.getAttribute("caption"))

            #Collecting user input to combine into CMxMSKCON register
            #CMxMSKCON is updated every time a user selection changes
            cmpSym_CMxMSKCON.append(id)
            cmpSym_CMxMSKCON[id] = cmpComponent.createHexSymbol("CMP_" +  str(id + 1) + "_CMxMSKCON_VALUE", None)
            cmpSym_CMxMSKCON[id].setDefaultValue(0)
            cmpSym_CMxMSKCON[id].setVisible(False)
            cmpSym_CMxMSKCON[id].setDependencies(combineCMxMSKCONConfigValues, ["CMP_" +  str(id + 1) + "_MSKCON_HLMS", "CMP_" +  str(id + 1) + "_MSKCON_SELSRCA", "CMP_" +  str(id + 1) + "_MSKCON_AANEN", "CMP_" +  str(id + 1) + "_MSKCON_AAEN", "CMP_" +  str(id + 1) + "_MSKCON_OANEN", "CMP_" +  str(id + 1) + "_MSKCON_OAEN", "CMP_" +  str(id + 1) + "_MSKCON_SELSRCB", "CMP_" +  str(id + 1) + "_MSKCON_ABNEN", "CMP_" +  str(id + 1) + "_MSKCON_ABEN", "CMP_" +  str(id + 1) + "_MSKCON_OBNEN", "CMP_" +  str(id + 1) + "_MSKCON_OBEN", "CMP_" +  str(id + 1) + "_MSKCON_SELSRCC", "CMP_" +  str(id + 1) + "_MSKCON_ACNEN", "CMP_" +  str(id + 1) + "_MSKCON_ACEN", "CMP_" +  str(id + 1) + "_MSKCON_OCNEN", "CMP_" +  str(id + 1) + "_MSKCON_OCEN", "CMP_" +  str(id + 1) + "_MSKCON_PAGS", "CMP_" +  str(id + 1) + "_MSKCON_NAGS"])

        #Calculate the interrupt register using IRQ#
        cmpxIrq = "COMPARATOR_" + str(id + 1)
        cmpxIrq_index = int(getIRQnumber(cmpxIrq))
        cmpxEnblRegName = _get_enblReg_parms(cmpxIrq_index)
        cmpxStatRegName = _get_statReg_parms(cmpxIrq_index)

        #CMPx IEC REG
        cmpxIEC.append(id)
        cmpxIEC[id] = cmpComponent.createStringSymbol("CMP_" +  str(id + 1) + "_IEC_REG", None)
        cmpxIEC[id].setDefaultValue(cmpxEnblRegName)
        cmpxIEC[id].setVisible(False)

        #CMPx IFS REG
        cmpxIFS.append(id)
        cmpxIFS[id] = cmpComponent.createStringSymbol("CMP_" +  str(id + 1) + "_IFS_REG", None)
        cmpxIFS[id].setDefaultValue(cmpxStatRegName)
        cmpxIFS[id].setVisible(False)

        ############################################################################
        #### Dependency ####
        ############################################################################

        # EVIC Dynamic settings
        # If the user disables interrupt via Interrupt configuration menu in 'System' component
        # The following comment will be made visible.
        cmpSymIntxEnComment.append(id)
        cmpSymIntxEnComment[id] = cmpComponent.createCommentSymbol("CMP_" +  str(id + 1) + "_INTERRUPT_ENABLE_COMMENT", cmpSym_CMx_CON_STRING[id])
        cmpSymIntxEnComment[id].setVisible(False)
        cmpSymIntxEnComment[id].setLabel("Warning!!! Comparator " +  str(id + 1) + " Interrupt is Disabled in Interrupt Manager")
        cmpSymIntxEnComment[id].setDependencies(updateCMPxInterruptData, ["CMP_" +  str(id + 1) + "_CON_EVPOL", "core." + "COMPARATOR_" +  str(id + 1) + "_INTERRUPT_ENABLE_UPDATE"])

        # Clock Warning status
        cmpSym_ClkxEnComment = cmpComponent.createCommentSymbol("CMP" + str(id + 1) + "_CLOCK_ENABLE_COMMENT", cmpSym_CMx_CON_STRING[id])
        cmpSym_ClkxEnComment.setLabel("Warning!!! Comparator " + str(id + 1) + " Peripheral Clock is Disabled in Clock Manager")
        cmpSym_ClkxEnComment.setVisible(False)
        cmpSym_ClkxEnComment.setDependencies(updateCMPxClockWarningStatus, ["core.CMP" + str(id + 1) + "_CLOCK_ENABLE"])

        if id != 3:
            # Clock Warning status
            opampSym_ClkxEnComment = cmpComponent.createCommentSymbol("OPAMP" + str(id + 1) + "_CLOCK_ENABLE_COMMENT", cmpSym_CMx_CON_STRING[id])
            opampSym_ClkxEnComment.setLabel("Warning!!! OPAMP" + str(id + 1) + " Peripheral Clock is Disabled in Clock Manager")
            opampSym_ClkxEnComment.setVisible(False)
            opampSym_ClkxEnComment.setDependencies(updateOPAMPxClockData, ["core.OPAMP" + str(id + 1) + "_CLOCK_ENABLE", "CMP_" + str(id + 1) + "_CON_AMPMOD"])

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    cmpHeader1File = cmpComponent.createFileSymbol("CMP_HEADER1", None)
    cmpHeader1File.setMarkup(True)
    cmpHeader1File.setSourcePath("../peripheral/cmp_01427/templates/plib_cmp.h.ftl")
    cmpHeader1File.setOutputName("plib_" + cmpInstanceName.getValue().lower() + ".h")
    cmpHeader1File.setDestPath("peripheral/cmp/")
    cmpHeader1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpHeader1File.setType("HEADER")
    cmpHeader1File.setOverwrite(True)

    cmpSource1File = cmpComponent.createFileSymbol("CMP_SOURCE1", None)
    cmpSource1File.setMarkup(True)
    cmpSource1File.setSourcePath("../peripheral/cmp_01427/templates/plib_cmp.c.ftl")
    cmpSource1File.setOutputName("plib_" + cmpInstanceName.getValue().lower() + ".c")
    cmpSource1File.setDestPath("peripheral/cmp/")
    cmpSource1File.setProjectPath("config/" + configName + "/peripheral/cmp/")
    cmpSource1File.setType("SOURCE")
    cmpSource1File.setOverwrite(True)

    cmpSystemInitFile = cmpComponent.createFileSymbol("CMP_INIT", None)
    cmpSystemInitFile.setType("STRING")
    cmpSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cmpSystemInitFile.setSourcePath("../peripheral/cmp_01427/templates/system/system_initialize.c.ftl")
    cmpSystemInitFile.setMarkup(True)

    cmpSystemDefFile = cmpComponent.createFileSymbol("CMP_DEF", None)
    cmpSystemDefFile.setType("STRING")
    cmpSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cmpSystemDefFile.setSourcePath("../peripheral/cmp_01427/templates/system/system_definitions.h.ftl")
    cmpSystemDefFile.setMarkup(True)
