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
ebiValGrp_EBIMSK0_MEMSIZE    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/value-group@[name="EBIMSK0__MEMSIZE"]')
ebiValGrp_EBIMSK0_MEMTYPE    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/value-group@[name="EBIMSK0__MEMTYPE"]')
ebiValGrp_EBIMSK0_REGSEL     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/value-group@[name="EBIMSK0__REGSEL"]')
ebiValGrp_EBISMT0_PAGESIZE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/value-group@[name="EBISMT0__PAGESIZE"]')
ebiValGrp_EBISMCON_SMDWIDTH0 = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/value-group@[name="EBISMCON__SMDWIDTH0"]')

ebiBitFld_EBICS0_CSADDR       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBICS0"]/bitfield@[name="CSADDR"]')
ebiBitFld_EBIMSK0_MEMSIZE     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBIMSK0"]/bitfield@[name="MEMSIZE"]')
ebiBitFld_EBIMSK0_MEMTYPE     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBIMSK0"]/bitfield@[name="MEMTYPE"]')
ebiBitFld_EBIMSK0_REGSEL      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBIMSK0"]/bitfield@[name="REGSEL"]')
ebiBitFld_EBISMT0_TRC         = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TRC"]')
ebiBitFld_EBISMT0_TAS         = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TAS"]')
ebiBitFld_EBISMT0_TWR         = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TWR"]')
ebiBitFld_EBISMT0_TWP         = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TWP"]')
ebiBitFld_EBISMT0_TBTA        = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TBTA"]')
ebiBitFld_EBISMT0_TPRC        = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="TPRC"]')
ebiBitFld_EBISMT0_PAGEMODE    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="PAGEMODE"]')
ebiBitFld_EBISMT0_PAGESIZE    = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="PAGESIZE"]')
ebiBitFld_EBISMT0_RDYMODE     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMT0"]/bitfield@[name="RDYMODE"]')
ebiBitFld_EBIFTRPD_TRPD       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBIFTRPD"]/bitfield@[name="TRPD"]')
ebiBitFld_EBISMCON_SMDWIDTH0  = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMCON"]/bitfield@[name="SMDWIDTH0"]')
ebiBitFld_EBISMCON_SMDWIDTH1  = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMCON"]/bitfield@[name="SMDWIDTH1"]')
ebiBitFld_EBISMCON_SMDWIDTH2  = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="EBI"]/register@[name="EBISMCON"]/bitfield@[name="SMDWIDTH2"]')
################################################################################
#### Global Variables ####
################################################################################
global ebiInstanceName
global ebiSym_EBIMSK0_MEMSIZE
global ebiSym_EBIMSK0_MEMTYPE
global ebiSym_EBIMSK0_REGSEL
global ebiSym_EBIMSK1_MEMSIZE
global ebiSym_EBIMSK1_MEMTYPE
global ebiSym_EBIMSK1_REGSEL
global ebiSym_EBIMSK2_MEMSIZE
global ebiSym_EBIMSK2_MEMTYPE
global ebiSym_EBIMSK2_REGSEL
global ebiSym_EBIMSK3_MEMSIZE
global ebiSym_EBIMSK3_MEMTYPE
global ebiSym_EBIMSK3_REGSEL
global ebiSym_EBISMT0_TRC
global ebiSym_EBISMT0_TAS
global ebiSym_EBISMT0_TWR
global ebiSym_EBISMT0_TWP
global ebiSym_EBISMT0_TBTA
global ebiSym_EBISMT0_TPRC
global ebiSym_EBISMT0_PAGEMODE
global ebiSym_EBISMT0_PAGESIZE
global ebiSym_EBISMT0_RDYMODE
global ebiSym_EBISMT1_TRC
global ebiSym_EBISMT1_TAS
global ebiSym_EBISMT1_TWR
global ebiSym_EBISMT1_TWP
global ebiSym_EBISMT1_TBTA
global ebiSym_EBISMT1_TPRC
global ebiSym_EBISMT1_PAGEMODE
global ebiSym_EBISMT1_PAGESIZE
global ebiSym_EBISMT1_RDYMODE
global ebiSym_EBISMT2_TRC
global ebiSym_EBISMT2_TAS
global ebiSym_EBISMT2_TWR
global ebiSym_EBISMT2_TWP
global ebiSym_EBISMT2_TBTA
global ebiSym_EBISMT2_TPRC
global ebiSym_EBISMT2_PAGEMODE
global ebiSym_EBISMT2_PAGESIZE
global ebiSym_EBISMT2_RDYMODE
global ebiSym_EBISMCON_SMDWIDTH0
global ebiSym_EBISMCON_SMDWIDTH1
global ebiSym_EBISMCON_SMDWIDTH2
global ebiSym_EBICS0_CSADDR
global ebiSym_EBICS1_CSADDR
global ebiSym_EBICS2_CSADDR
global ebiSym_EBICS3_CSADDR
global ebiSym_CFGEBIC_EBIDAT
global ebiSym_CFGEBIC_EBIRDYINV1
global ebiSym_CFGEBIC_EBIRDYEN1
global ebiSym_CFGEBIC_EBIRDYINV2
global ebiSym_CFGEBIC_EBIRDYEN2
global ebiSym_CFGEBIC_EBIRDYINV3
global ebiSym_CFGEBIC_EBIRDYEN3
global ebiSym_CFGEBIC_EBIRDYLVL
global ebiSym_CFGEBIC_EBIRPEN
global ebiSym_CFGEBIC_EBIWEEN
global ebiSym_CFGEBIC_EBIOEEN
global ebiSym_CFGEBIC_EBIBSEN0
global ebiSym_CFGEBIC_EBIBSEN1
global ebiSym_CFGEBIC_EBICSEN0
global ebiSym_CFGEBIC_EBICSEN1
global ebiSym_CFGEBIC_EBICSEN2
global ebiSym_CFGEBIC_EBICSEN3
################################################################################
#### Business Logic ####
################################################################################

def EBICS_config_visibility(symbol, event):
    if(event["value"] == True):
        if(symbol.getID() == "CFGEBIC_EBICSEN0"):
            ebiSym_EBICS0_CSADDR.setVisible(True)
        elif(symbol.getID() == "CFGEBIC_EBICSEN1"):
            ebiSym_EBICS1_CSADDR.setVisible(True)
        elif(symbol.getID() == "CFGEBIC_EBICSEN2"):
            ebiSym_EBICS2_CSADDR.setVisible(True)
        elif(symbol.getID() == "CFGEBIC_EBICSEN3"):
            ebiSym_EBICS3_CSADDR.setVisible(True)
    else :
        if(symbol.getID() == "CFGEBIC_EBICSEN0"):
            ebiSym_EBICS0_CSADDR.setVisible(False)
        elif(symbol.getID() == "CFGEBIC_EBICSEN1"):
            ebiSym_EBICS1_CSADDR.setVisible(False)
        elif(symbol.getID() == "CFGEBIC_EBICSEN2"):
            ebiSym_EBICS2_CSADDR.setVisible(False)
        elif(symbol.getID() == "CFGEBIC_EBICSEN3"):
            ebiSym_EBICS3_CSADDR.setVisible(False)

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

def populate_CFGEBIA_values(value, outputList):
    power = 1
    ebipinen = 2147483648
    for ii in range(0,value+1):
        dict = {}
        if(ii == 24):
            dict['desc']    = str(ii)
            dict['key']     = "  -  "
            dict['value']   = hex(0)
            outputList.append(dict)
        else:
            power *= 2
            dict['desc']    = str(ii)
            dict['key']     = str(ii) + "-bit"
            dict['value']   = hex(power + ebipinen - 1)
            outputList.append(dict)

def combineCFGEBIC_Values(symbol, event):
    ebidatValue     = int(ebiSym_CFGEBIC_EBIDAT.getKey(ebiSym_CFGEBIC_EBIDAT.getValue()))
    ebicsen0Value   = ebiSym_CFGEBIC_EBICSEN0.getValue() << 4
    ebicsen1Value   = ebiSym_CFGEBIC_EBICSEN1.getValue() << 5
    ebicsen2Value   = ebiSym_CFGEBIC_EBICSEN2.getValue() << 6
    ebicsen3Value   = ebiSym_CFGEBIC_EBICSEN3.getValue() << 7
    ebibsen0Value   = ebiSym_CFGEBIC_EBIBSEN0.getValue() << 8
    ebibsen1Value   = ebiSym_CFGEBIC_EBIBSEN1.getValue() << 9
    ebioeenValue    = ebiSym_CFGEBIC_EBIOEEN.getValue() << 12
    ebiweenValue    = ebiSym_CFGEBIC_EBIWEEN.getValue() << 13
    ebirpenValue    = ebiSym_CFGEBIC_EBIRPEN.getValue() << 16
    ebirdylvlValue  = ebiSym_CFGEBIC_EBIRDYLVL.getValue() << 17
    ebirdyen1Value  = ebiSym_CFGEBIC_EBIRDYEN1.getValue() << 25
    ebirdyen2Value  = ebiSym_CFGEBIC_EBIRDYEN2.getValue() << 26
    ebirdyen3Value  = ebiSym_CFGEBIC_EBIRDYEN3.getValue() << 27
    ebirdyinv1Value = ebiSym_CFGEBIC_EBIRDYINV1.getValue() << 29
    ebirdyinv2Value = ebiSym_CFGEBIC_EBIRDYINV2.getValue() << 30
    ebirdyinv3Value = ebiSym_CFGEBIC_EBIRDYINV3.getValue() << 31
    cfgebicValue    = (ebirdyinv1Value + ebirdyen1Value + ebirdyinv2Value + ebirdyen2Value
                      + ebirdyinv3Value + ebirdyen3Value + ebirdylvlValue + ebirpenValue
                      + ebiweenValue + ebioeenValue + ebibsen0Value + ebibsen1Value + ebicsen0Value
                      + ebicsen1Value + ebicsen2Value + ebicsen3Value + ebidatValue)
    symbol.setValue(cfgebicValue, 2)

def setEBIDAT0_Values(symbol, event):
    value = int(ebiSym_CFGEBIC_EBIDAT.getKey(ebiSym_CFGEBIC_EBIDAT.getValue()))
    if((value == 1) | (value == 3)):
        symbol.setValue(1, 2)

def setEBIDAT1_Values(symbol, event):
    value = int(ebiSym_CFGEBIC_EBIDAT.getKey(ebiSym_CFGEBIC_EBIDAT.getValue()))
    if(value == 3):
        symbol.setValue(1, 2)

def combineMSK0_Values(symbol, event):
    memsizeValue = ebiSym_EBIMSK0_MEMSIZE.getValue() << 0
    memtypeValue = int(ebiSym_EBIMSK0_MEMTYPE.getSelectedValue()) << 5
    regselValue  = ebiSym_EBIMSK0_REGSEL.getValue() << 8
    mskValue = memsizeValue + memtypeValue + regselValue
    symbol.setValue(mskValue, 2)

def combineMSK1_Values(symbol, event):
    memsizeValue = ebiSym_EBIMSK1_MEMSIZE.getValue() << 0
    memtypeValue = int(ebiSym_EBIMSK1_MEMTYPE.getSelectedValue()) << 5
    regselValue  = ebiSym_EBIMSK1_REGSEL.getValue() << 8
    mskValue = memsizeValue + memtypeValue + regselValue
    symbol.setValue(mskValue, 2)

def combineMSK2_Values(symbol, event):
    memsizeValue = ebiSym_EBIMSK2_MEMSIZE.getValue() << 0
    memtypeValue = int(ebiSym_EBIMSK2_MEMTYPE.getSelectedValue()) << 5
    regselValue  = ebiSym_EBIMSK2_REGSEL.getValue() << 8
    mskValue = memsizeValue + memtypeValue + regselValue
    symbol.setValue(mskValue, 2)

def combineMSK3_Values(symbol, event):
    memsizeValue = ebiSym_EBIMSK3_MEMSIZE.getValue() << 0
    memtypeValue = int(ebiSym_EBIMSK3_MEMTYPE.getSelectedValue()) << 5
    regselValue  = ebiSym_EBIMSK3_REGSEL.getValue() << 8
    mskValue = memsizeValue + memtypeValue + regselValue
    symbol.setValue(mskValue, 2)

def combineSMT0_Values(symbol, event):
    trcValue = ebiSym_EBISMT0_TRC.getValue() << 0
    tasValue = ebiSym_EBISMT0_TAS.getValue() << 6
    twrValue = ebiSym_EBISMT0_TWR.getValue() << 8
    twpValue = ebiSym_EBISMT0_TWP.getValue() << 10
    tbtaValue = ebiSym_EBISMT0_TBTA.getValue() << 16
    tprcValue = ebiSym_EBISMT0_TPRC.getValue() << 19
    pagemodeValue = int(ebiSym_EBISMT0_PAGEMODE.getValue()) << 23
    pagesizeValue = ebiSym_EBISMT0_PAGESIZE.getValue() << 24
    rdymodeValue = int(ebiSym_EBISMT0_RDYMODE.getValue()) << 26
    smtValue = trcValue + tasValue + twrValue + twpValue + tbtaValue + tprcValue + pagemodeValue + pagesizeValue + rdymodeValue
    symbol.setValue(smtValue, 2)

def combineSMT1_Values(symbol, event):
    trcValue = ebiSym_EBISMT1_TRC.getValue() << 0
    tasValue = ebiSym_EBISMT1_TAS.getValue() << 6
    twrValue = ebiSym_EBISMT1_TWR.getValue() << 8
    twpValue = ebiSym_EBISMT1_TWP.getValue() << 10
    tbtaValue = ebiSym_EBISMT1_TBTA.getValue() << 16
    tprcValue = ebiSym_EBISMT1_TPRC.getValue() << 19
    pagemodeValue = int(ebiSym_EBISMT1_PAGEMODE.getValue()) << 23
    pagesizeValue = ebiSym_EBISMT1_PAGESIZE.getValue() << 24
    rdymodeValue = int(ebiSym_EBISMT1_RDYMODE.getValue()) << 26
    smtValue = trcValue + tasValue + twrValue + twpValue + tbtaValue + tprcValue + pagemodeValue + pagesizeValue + rdymodeValue
    symbol.setValue(smtValue, 2)

def combineSMT2_Values(symbol, event):
    trcValue = ebiSym_EBISMT2_TRC.getValue() << 0
    tasValue = ebiSym_EBISMT2_TAS.getValue() << 6
    twrValue = ebiSym_EBISMT2_TWR.getValue() << 8
    twpValue = ebiSym_EBISMT2_TWP.getValue() << 10
    tbtaValue = ebiSym_EBISMT2_TBTA.getValue() << 16
    tprcValue = ebiSym_EBISMT2_TPRC.getValue() << 19
    pagemodeValue = int(ebiSym_EBISMT2_PAGEMODE.getValue()) << 23
    pagesizeValue = ebiSym_EBISMT2_PAGESIZE.getValue() << 24
    rdymodeValue = int(ebiSym_EBISMT2_RDYMODE.getValue()) << 26
    smtValue = trcValue + tasValue + twrValue + twpValue + tbtaValue + tprcValue + pagemodeValue + pagesizeValue + rdymodeValue
    symbol.setValue(smtValue, 2)

def combineSMCON_Values(symbol, event):
    smdwidth0Value = int(ebiSym_EBISMCON_SMDWIDTH0.getSelectedValue()) << 7
    smdwidth1Value = int(ebiSym_EBISMCON_SMDWIDTH1.getSelectedValue()) << 10
    smdwidth2Value = int(ebiSym_EBISMCON_SMDWIDTH2.getSelectedValue()) << 13
    smrp = 1
    smconValue = smdwidth0Value + smdwidth1Value + smdwidth2Value + smrp
    symbol.setValue(smconValue, 2)

def shiftEBICS0_Values(symbol, event):
    shiftedValue = ebiSym_EBICS0_CSADDR.getValue() << 16
    symbol.setValue(shiftedValue, 2)

def shiftEBICS1_Values(symbol, event):
    shiftedValue = ebiSym_EBICS1_CSADDR.getValue() << 16
    symbol.setValue(shiftedValue, 2)

def shiftEBICS2_Values(symbol, event):
    shiftedValue = ebiSym_EBICS2_CSADDR.getValue() << 16
    symbol.setValue(shiftedValue, 2)

def shiftEBICS3_Values(symbol, event):
    shiftedValue = ebiSym_EBICS3_CSADDR.getValue() << 16
    symbol.setValue(shiftedValue, 2)

def updateEBIClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################
def instantiateComponent(ebiComponent):
    global ebiInstanceName
    global ebiSym_EBIMSK0_MEMSIZE
    global ebiSym_EBIMSK0_MEMTYPE
    global ebiSym_EBIMSK0_REGSEL
    global ebiSym_EBIMSK1_MEMSIZE
    global ebiSym_EBIMSK1_MEMTYPE
    global ebiSym_EBIMSK1_REGSEL
    global ebiSym_EBIMSK2_MEMSIZE
    global ebiSym_EBIMSK2_MEMTYPE
    global ebiSym_EBIMSK2_REGSEL
    global ebiSym_EBIMSK3_MEMSIZE
    global ebiSym_EBIMSK3_MEMTYPE
    global ebiSym_EBIMSK3_REGSEL
    global ebiSym_EBISMT0_TRC
    global ebiSym_EBISMT0_TAS
    global ebiSym_EBISMT0_TWR
    global ebiSym_EBISMT0_TWP
    global ebiSym_EBISMT0_TBTA
    global ebiSym_EBISMT0_TPRC
    global ebiSym_EBISMT0_PAGEMODE
    global ebiSym_EBISMT0_PAGESIZE
    global ebiSym_EBISMT0_RDYMODE
    global ebiSym_EBISMT1_TRC
    global ebiSym_EBISMT1_TAS
    global ebiSym_EBISMT1_TWR
    global ebiSym_EBISMT1_TWP
    global ebiSym_EBISMT1_TBTA
    global ebiSym_EBISMT1_TPRC
    global ebiSym_EBISMT1_PAGEMODE
    global ebiSym_EBISMT1_PAGESIZE
    global ebiSym_EBISMT1_RDYMODE
    global ebiSym_EBISMT2_TRC
    global ebiSym_EBISMT2_TAS
    global ebiSym_EBISMT2_TWR
    global ebiSym_EBISMT2_TWP
    global ebiSym_EBISMT2_TBTA
    global ebiSym_EBISMT2_TPRC
    global ebiSym_EBISMT2_PAGEMODE
    global ebiSym_EBISMT2_PAGESIZE
    global ebiSym_EBISMT2_RDYMODE
    global ebiSym_EBISMCON_SMDWIDTH0
    global ebiSym_EBISMCON_SMDWIDTH1
    global ebiSym_EBISMCON_SMDWIDTH2
    global ebiSym_EBICS0_CSADDR
    global ebiSym_EBICS1_CSADDR
    global ebiSym_EBICS2_CSADDR
    global ebiSym_EBICS3_CSADDR
    global ebiSym_CFGEBIC_EBIDAT
    global ebiSym_CFGEBIC_EBIRDYINV1
    global ebiSym_CFGEBIC_EBIRDYEN1
    global ebiSym_CFGEBIC_EBIRDYINV2
    global ebiSym_CFGEBIC_EBIRDYEN2
    global ebiSym_CFGEBIC_EBIRDYINV3
    global ebiSym_CFGEBIC_EBIRDYEN3
    global ebiSym_CFGEBIC_EBIRDYLVL
    global ebiSym_CFGEBIC_EBIRPEN
    global ebiSym_CFGEBIC_EBIWEEN
    global ebiSym_CFGEBIC_EBIOEEN
    global ebiSym_CFGEBIC_EBIBSEN0
    global ebiSym_CFGEBIC_EBIBSEN1
    global ebiSym_CFGEBIC_EBICSEN0
    global ebiSym_CFGEBIC_EBICSEN1
    global ebiSym_CFGEBIC_EBICSEN2
    global ebiSym_CFGEBIC_EBICSEN3

    ebiInstanceName = ebiComponent.createStringSymbol("EBI_INSTANCE_NAME", None)
    ebiInstanceName.setVisible(False)
    ebiInstanceName.setDefaultValue(ebiComponent.getID().upper())
    print("Running " + ebiInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", ebiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    #Get Address Lines
    addressLines = 0
    addLines = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGEBIA"]')
    addLinesChildren = addLines.getChildren()
    for param in addLinesChildren:
        caption = param.getAttribute('caption')
        if(caption.find("EBI Address Pin Enable bit") != -1):
            addressLines += 1

    #Get Chip Selects
    chipSelects = False
    chipSelectLines = 0
    chipLines = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CFG"]/register-group@[name="CFG"]/register@[name="CFGEBIC"]')
    chipLinesChildren = chipLines.getChildren()
    for param in chipLinesChildren:
        name = param.getAttribute('name')
        if((name == "EBICSEN0") | (name == "EBICSEN1") | (name == "EBICSEN2") | (name == "EBICSEN3")):
            chipSelectLines += 1
    if(chipSelectLines > 1):
        chipSelects = True

    #EBI PIN CONFIG
    ebiSym_PIN_SETUP = ebiComponent.createCommentSymbol("EBI_PIN_SETUP", None)
    ebiSym_PIN_SETUP.setLabel("EBI Pin Configuration")
    ebiSym_PIN_SETUP.setVisible(True)

    #CFGEBIA
    ebiADDWIDTH_names = []
    populate_CFGEBIA_values(addressLines, ebiADDWIDTH_names)
    ebiSym_CFGEBIA_EBIADD = ebiComponent.createKeyValueSetSymbol("CFGEBIA_EBIADD", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIA_EBIADD.setLabel("Address Bus Width")
    ebiSym_CFGEBIA_EBIADD.setDefaultValue(24)
    ebiSym_CFGEBIA_EBIADD.setOutputMode("Value")
    ebiSym_CFGEBIA_EBIADD.setDisplayMode("Description")
    for ii in ebiADDWIDTH_names:
        ebiSym_CFGEBIA_EBIADD.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_CFGEBIA_EBIADD.setVisible(True)

    ebiSym_CFGEBIC_EBIDAT = ebiComponent.createKeyValueSetSymbol("CFGEBIC_EBIDAT", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIDAT.setLabel("Data Bus Width")
    ebiSym_CFGEBIC_EBIDAT.setDefaultValue(0)
    ebiSym_CFGEBIC_EBIDAT.setOutputMode("Value")
    ebiSym_CFGEBIC_EBIDAT.setDisplayMode("Description")
    ebiSym_CFGEBIC_EBIDAT.addKey( str(0), "0", "  -  " )
    ebiSym_CFGEBIC_EBIDAT.addKey( str(1), "1", "8-bit" )
    ebiSym_CFGEBIC_EBIDAT.addKey( str(3), "3", "16-bit" )
    ebiSym_CFGEBIC_EBIDAT.setVisible(True)

    #CFGEBIC_EBIDAT0
    ebiSym_CFGEBIC_EBIDAT0 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIDAT0", None)
    ebiSym_CFGEBIC_EBIDAT0.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIDAT0.setVisible(False)
    ebiSym_CFGEBIC_EBIDAT0.setDependencies(setEBIDAT0_Values, ["CFGEBIC_EBIDAT"])

    #CFGEBIC_EBIDAT1
    ebiSym_CFGEBIC_EBIDAT1 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIDAT1", None)
    ebiSym_CFGEBIC_EBIDAT1.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIDAT1.setVisible(False)
    ebiSym_CFGEBIC_EBIDAT1.setDependencies(setEBIDAT1_Values, ["CFGEBIC_EBIDAT"])

    #EBI PIN CONFIG
    ebiSym_EBIRDYPIN_SETUP = ebiComponent.createCommentSymbol("EBIRDY_PIN_SETUP", ebiSym_PIN_SETUP)
    ebiSym_EBIRDYPIN_SETUP.setLabel("EBIRDY Pins")
    ebiSym_EBIRDYPIN_SETUP.setVisible(True)

    #EBIRDYINV1_ENABLE
    ebiSym_CFGEBIC_EBIRDYINV1 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYINV1", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYINV1.setLabel("EBIRDY1 Inversion Control bit")
    ebiSym_CFGEBIC_EBIRDYINV1.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYINV1.setVisible(True)

    #EBIRDYEN1_ENABLE
    ebiSym_CFGEBIC_EBIRDYEN1 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYEN1", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYEN1.setLabel("EBIRDY1 Pin Enable bit")
    ebiSym_CFGEBIC_EBIRDYEN1.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYEN1.setVisible(True)

    #EBIRDYINV2_ENABLE
    ebiSym_CFGEBIC_EBIRDYINV2 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYINV2", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYINV2.setLabel("EBIRDY2 Inversion Control bit")
    ebiSym_CFGEBIC_EBIRDYINV2.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYINV2.setVisible(True)

    #EBIRDYEN2_ENABLE
    ebiSym_CFGEBIC_EBIRDYEN2 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYEN2", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYEN2.setLabel("EBIRDY2 Pin Enable bit")
    ebiSym_CFGEBIC_EBIRDYEN2.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYEN2.setVisible(True)

    #EBIRDYINV3_ENABLE
    ebiSym_CFGEBIC_EBIRDYINV3 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYINV3", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYINV3.setLabel("EBIRDY3 Inversion Control bit")
    ebiSym_CFGEBIC_EBIRDYINV3.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYINV3.setVisible(True)

    #EBIRDYEN3_ENABLE
    ebiSym_CFGEBIC_EBIRDYEN3 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYEN3", ebiSym_EBIRDYPIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYEN3.setLabel("EBIRDY3 Pin Enable bit")
    ebiSym_CFGEBIC_EBIRDYEN3.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYEN3.setVisible(True)

    #EBIRDYLVL_ENABLE
    ebiSym_CFGEBIC_EBIRDYLVL = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRDYLVL", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIRDYLVL.setLabel("EBIRDYx Pin Sensitivity Control bit")
    ebiSym_CFGEBIC_EBIRDYLVL.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRDYLVL.setVisible(True)

    #EBIRPEN_ENABLE
    ebiSym_CFGEBIC_EBIRPEN = ebiComponent.createBooleanSymbol("CFGEBIC_EBIRPEN", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIRPEN.setLabel("/EBIRP Pin Sensitivity Control bit")
    ebiSym_CFGEBIC_EBIRPEN.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIRPEN.setVisible(True)

    #EBIWEEN_ENABLE
    ebiSym_CFGEBIC_EBIWEEN = ebiComponent.createBooleanSymbol("CFGEBIC_EBIWEEN", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIWEEN.setLabel("/EBIWE Pin Enable bit")
    ebiSym_CFGEBIC_EBIWEEN.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIWEEN.setVisible(True)

    #EBIOEEN_ENABLE
    ebiSym_CFGEBIC_EBIOEEN = ebiComponent.createBooleanSymbol("CFGEBIC_EBIOEEN", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIOEEN.setLabel("/EBIOE Pin Enable bit")
    ebiSym_CFGEBIC_EBIOEEN.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIOEEN.setVisible(True)

    #EBIBSEN0_ENABLE
    ebiSym_CFGEBIC_EBIBSEN0 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIBSEN0", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIBSEN0.setLabel("/EBIBS1 Pin Enable bit")
    ebiSym_CFGEBIC_EBIBSEN0.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIBSEN0.setVisible(True)

    #EBIBSEN1_ENABLE
    ebiSym_CFGEBIC_EBIBSEN1 = ebiComponent.createBooleanSymbol("CFGEBIC_EBIBSEN1", ebiSym_PIN_SETUP)
    ebiSym_CFGEBIC_EBIBSEN1.setLabel("/EBIBS0 Pin Enable bit")
    ebiSym_CFGEBIC_EBIBSEN1.setDefaultValue(False)
    ebiSym_CFGEBIC_EBIBSEN1.setVisible(True)

    #EBICS0_ENABLE
    ebiSym_CFGEBIC_EBICSEN0 = ebiComponent.createBooleanSymbol("CFGEBIC_EBICSEN0", None)
    ebiSym_CFGEBIC_EBICSEN0.setLabel("/EBICS0 Pin Enable bit")
    ebiSym_CFGEBIC_EBICSEN0.setDefaultValue(False)
    ebiSym_CFGEBIC_EBICSEN0.setVisible(True)
    ebiSym_CFGEBIC_EBICSEN0.setDependencies(EBICS_config_visibility,["CFGEBIC_EBICSEN0"]);

    #EBICS0
    ebiSym_EBICS0_CSADDR = ebiComponent.createHexSymbol("EBICS0_CSADDR", ebiSym_CFGEBIC_EBICSEN0)
    ebiSym_EBICS0_CSADDR.setLabel("EBICS0 " + ebiBitFld_EBICS0_CSADDR.getAttribute("caption"))
    ebiSym_EBICS0_CSADDR.setDefaultValue(0x20000000)
    ebiSym_EBICS0_CSADDR.setVisible(False)

    #EBICS0_VALUE
    ebiSym_EBICS0_VALUE = ebiComponent.createHexSymbol("EBICS0_VALUE", None)
    ebiSym_EBICS0_VALUE.setDefaultValue(0x20000000)
    ebiSym_EBICS0_VALUE.setVisible(False)
    ebiSym_EBICS0_VALUE.setDependencies(shiftEBICS0_Values, ["EBICS0_CSADDR"])

    #EBICS1_ENABLE
    ebiSym_CFGEBIC_EBICSEN1 = ebiComponent.createBooleanSymbol("CFGEBIC_EBICSEN1", None)
    ebiSym_CFGEBIC_EBICSEN1.setLabel("/EBICS1 Pin Enable bit")
    ebiSym_CFGEBIC_EBICSEN1.setDefaultValue(False)
    ebiSym_CFGEBIC_EBICSEN1.setVisible(chipSelects)
    ebiSym_CFGEBIC_EBICSEN1.setDependencies(EBICS_config_visibility,["CFGEBIC_EBICSEN1"]);


    #EBICS1
    ebiSym_EBICS1_CSADDR = ebiComponent.createHexSymbol("EBICS1_CSADDR", ebiSym_CFGEBIC_EBICSEN1)
    ebiSym_EBICS1_CSADDR.setLabel("EBICS1 " + ebiBitFld_EBICS0_CSADDR.getAttribute("caption"))
    ebiSym_EBICS1_CSADDR.setDefaultValue(0x10000000)
    ebiSym_EBICS1_CSADDR.setVisible(False)

    #EBICS1_VALUE
    ebiSym_EBICS1_VALUE = ebiComponent.createHexSymbol("EBICS1_VALUE", None)
    ebiSym_EBICS1_VALUE.setDefaultValue(0x10000000)
    ebiSym_EBICS1_VALUE.setVisible(False)
    ebiSym_EBICS1_VALUE.setDependencies(shiftEBICS1_Values, ["EBICS1_CSADDR"])

    #EBICS2_ENABLE
    ebiSym_CFGEBIC_EBICSEN2 = ebiComponent.createBooleanSymbol("CFGEBIC_EBICSEN2", None)
    ebiSym_CFGEBIC_EBICSEN2.setLabel("/EBICS2 Pin Enable bit")
    ebiSym_CFGEBIC_EBICSEN2.setDefaultValue(False)
    ebiSym_CFGEBIC_EBICSEN2.setVisible(chipSelects)
    ebiSym_CFGEBIC_EBICSEN2.setDependencies(EBICS_config_visibility,["CFGEBIC_EBICSEN2"]);

    #EBICS2
    ebiSym_EBICS2_CSADDR = ebiComponent.createHexSymbol("EBICS2_CSADDR", ebiSym_CFGEBIC_EBICSEN2)
    ebiSym_EBICS2_CSADDR.setLabel("EBICS2 " + ebiBitFld_EBICS0_CSADDR.getAttribute("caption"))
    ebiSym_EBICS2_CSADDR.setDefaultValue(0x20400000)
    ebiSym_EBICS2_CSADDR.setVisible(False)

    #EBICS2_VALUE
    ebiSym_EBICS2_VALUE = ebiComponent.createHexSymbol("EBICS2_VALUE", None)
    ebiSym_EBICS2_VALUE.setDefaultValue(0x20400000)
    ebiSym_EBICS2_VALUE.setVisible(False)
    ebiSym_EBICS2_VALUE.setDependencies(shiftEBICS2_Values, ["EBICS2_CSADDR"])

    #EBICS3_ENABLE
    ebiSym_CFGEBIC_EBICSEN3 = ebiComponent.createBooleanSymbol("CFGEBIC_EBICSEN3", None)
    ebiSym_CFGEBIC_EBICSEN3.setLabel("/EBICS3 Pin Enable bit")
    ebiSym_CFGEBIC_EBICSEN3.setDefaultValue(False)
    ebiSym_CFGEBIC_EBICSEN3.setVisible(chipSelects)
    ebiSym_CFGEBIC_EBICSEN3.setDependencies(EBICS_config_visibility,["CFGEBIC_EBICSEN3"]);


    #EBICS3
    ebiSym_EBICS3_CSADDR = ebiComponent.createHexSymbol("EBICS3_CSADDR", ebiSym_CFGEBIC_EBICSEN3)
    ebiSym_EBICS3_CSADDR.setLabel("EBICS3 " + ebiBitFld_EBICS0_CSADDR.getAttribute("caption"))
    ebiSym_EBICS3_CSADDR.setDefaultValue(0x10400000)
    ebiSym_EBICS3_CSADDR.setVisible(False)

    #EBICS3_VALUE
    ebiSym_EBICS3_VALUE = ebiComponent.createHexSymbol("EBICS3_VALUE", None)
    ebiSym_EBICS3_VALUE.setDefaultValue(0x10400000)
    ebiSym_EBICS3_VALUE.setVisible(False)
    ebiSym_EBICS3_VALUE.setDependencies(shiftEBICS3_Values, ["EBICS3_CSADDR"])

    #CFGEBIC_VALUE
    ebiSym_CFGEBIC_VALUE = ebiComponent.createHexSymbol("CFGEBIC_VALUE", None)
    ebiSym_CFGEBIC_VALUE.setDefaultValue(0)
    ebiSym_CFGEBIC_VALUE.setVisible(False)
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIDAT"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYINV1"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYEN1"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYINV2"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYEN2"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYINV3"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYEN3"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRDYLVL"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIRPEN"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIWEEN"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIOEEN"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIBSEN0"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBIBSEN1"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBICSEN0"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBICSEN1"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBICSEN2"])
    ebiSym_CFGEBIC_VALUE.setDependencies(combineCFGEBIC_Values, ["CFGEBIC_EBICSEN3"])

    #EBIMSK0
    ebiMEMSIZE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMSIZE, ebiMEMSIZE_names)
    ebiSym_EBIMSK0_MEMSIZE = ebiComponent.createKeyValueSetSymbol("EBIMSK0_MEMSIZE", ebiSym_EBICS0_CSADDR)
    ebiSym_EBIMSK0_MEMSIZE.setLabel(ebiBitFld_EBIMSK0_MEMSIZE.getAttribute("caption"))
    ebiSym_EBIMSK0_MEMSIZE.setDefaultValue(0)
    ebiSym_EBIMSK0_MEMSIZE.setOutputMode("Value")
    ebiSym_EBIMSK0_MEMSIZE.setDisplayMode("Description")
    for ii in ebiMEMSIZE_names:
        ebiSym_EBIMSK0_MEMSIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK0_MEMSIZE.setVisible(True)

    ebiMEMTYPE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMTYPE, ebiMEMTYPE_names)
    ebiSym_EBIMSK0_MEMTYPE = ebiComponent.createKeyValueSetSymbol("EBIMSK0_MEMTYPE", ebiSym_EBICS0_CSADDR)
    ebiSym_EBIMSK0_MEMTYPE.setLabel(ebiBitFld_EBIMSK0_MEMTYPE.getAttribute("caption"))
    ebiSym_EBIMSK0_MEMTYPE.setDefaultValue(0)
    ebiSym_EBIMSK0_MEMTYPE.setOutputMode("Value")
    ebiSym_EBIMSK0_MEMTYPE.setDisplayMode("Description")
    for ii in ebiMEMTYPE_names:
        ebiSym_EBIMSK0_MEMTYPE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK0_MEMTYPE.setVisible(True)


    ebiREGSEL_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_REGSEL, ebiREGSEL_names)
    ebiSym_EBIMSK0_REGSEL = ebiComponent.createKeyValueSetSymbol("EBIMSK0_REGSEL", ebiSym_EBICS0_CSADDR)
    ebiSym_EBIMSK0_REGSEL.setLabel(ebiBitFld_EBIMSK0_REGSEL.getAttribute("caption"))
    ebiSym_EBIMSK0_REGSEL.setDefaultValue(0)
    ebiSym_EBIMSK0_REGSEL.setOutputMode("Value")
    ebiSym_EBIMSK0_REGSEL.setDisplayMode("Description")
    for ii in ebiREGSEL_names:
        ebiSym_EBIMSK0_REGSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK0_REGSEL.setVisible(True)

    #EBIMSK0_Value
    ebiSym_EBIMSK0_VALUE = ebiComponent.createHexSymbol("EBIMSK0_VALUE", None)
    ebiSym_EBIMSK0_VALUE.setDefaultValue(0x20)
    ebiSym_EBIMSK0_VALUE.setVisible(False)
    ebiSym_EBIMSK0_VALUE.setDependencies(combineMSK0_Values, ["EBIMSK0_MEMSIZE","EBIMSK0_MEMTYPE","EBIMSK0_REGSEL"])

    #EBIMSK1
    ebiMEMSIZE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMSIZE, ebiMEMSIZE_names)
    ebiSym_EBIMSK1_MEMSIZE = ebiComponent.createKeyValueSetSymbol("EBIMSK1_MEMSIZE", ebiSym_EBICS1_CSADDR)
    ebiSym_EBIMSK1_MEMSIZE.setLabel(ebiBitFld_EBIMSK0_MEMSIZE.getAttribute("caption"))
    ebiSym_EBIMSK1_MEMSIZE.setDefaultValue(0)
    ebiSym_EBIMSK1_MEMSIZE.setOutputMode("Value")
    ebiSym_EBIMSK1_MEMSIZE.setDisplayMode("Description")
    for ii in ebiMEMSIZE_names:
        ebiSym_EBIMSK1_MEMSIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK1_MEMSIZE.setVisible(True)

    ebiMEMTYPE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMTYPE, ebiMEMTYPE_names)
    ebiSym_EBIMSK1_MEMTYPE = ebiComponent.createKeyValueSetSymbol("EBIMSK1_MEMTYPE", ebiSym_EBICS1_CSADDR)
    ebiSym_EBIMSK1_MEMTYPE.setLabel(ebiBitFld_EBIMSK0_MEMTYPE.getAttribute("caption"))
    ebiSym_EBIMSK1_MEMTYPE.setDefaultValue(0)
    ebiSym_EBIMSK1_MEMTYPE.setOutputMode("Value")
    ebiSym_EBIMSK1_MEMTYPE.setDisplayMode("Description")
    for ii in ebiMEMTYPE_names:
        ebiSym_EBIMSK1_MEMTYPE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK1_MEMTYPE.setVisible(True)

    ebiREGSEL_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_REGSEL, ebiREGSEL_names)
    ebiSym_EBIMSK1_REGSEL = ebiComponent.createKeyValueSetSymbol("EBIMSK1_REGSEL", ebiSym_EBICS1_CSADDR)
    ebiSym_EBIMSK1_REGSEL.setLabel(ebiBitFld_EBIMSK0_REGSEL.getAttribute("caption"))
    ebiSym_EBIMSK1_REGSEL.setDefaultValue(0)
    ebiSym_EBIMSK1_REGSEL.setOutputMode("Value")
    ebiSym_EBIMSK1_REGSEL.setDisplayMode("Description")
    for ii in ebiREGSEL_names:
        ebiSym_EBIMSK1_REGSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK1_REGSEL.setVisible(True)

    #EBIMSK1_Value
    ebiSym_EBIMSK1_VALUE = ebiComponent.createHexSymbol("EBIMSK1_VALUE", None)
    ebiSym_EBIMSK1_VALUE.setDefaultValue(0x20)
    ebiSym_EBIMSK1_VALUE.setVisible(False)
    ebiSym_EBIMSK1_VALUE.setDependencies(combineMSK1_Values, ["EBIMSK1_MEMSIZE","EBIMSK1_MEMTYPE","EBIMSK1_REGSEL"])

    #EBIMSK2
    ebiMEMSIZE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMSIZE, ebiMEMSIZE_names)
    ebiSym_EBIMSK2_MEMSIZE = ebiComponent.createKeyValueSetSymbol("EBIMSK2_MEMSIZE", ebiSym_EBICS2_CSADDR)
    ebiSym_EBIMSK2_MEMSIZE.setLabel(ebiBitFld_EBIMSK0_MEMSIZE.getAttribute("caption"))
    ebiSym_EBIMSK2_MEMSIZE.setDefaultValue(0)
    ebiSym_EBIMSK2_MEMSIZE.setOutputMode("Value")
    ebiSym_EBIMSK2_MEMSIZE.setDisplayMode("Description")
    for ii in ebiMEMSIZE_names:
        ebiSym_EBIMSK2_MEMSIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK2_MEMSIZE.setVisible(True)

    ebiMEMTYPE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMTYPE, ebiMEMTYPE_names)
    ebiSym_EBIMSK2_MEMTYPE = ebiComponent.createKeyValueSetSymbol("EBIMSK2_MEMTYPE", ebiSym_EBICS2_CSADDR)
    ebiSym_EBIMSK2_MEMTYPE.setLabel(ebiBitFld_EBIMSK0_MEMTYPE.getAttribute("caption"))
    ebiSym_EBIMSK2_MEMTYPE.setDefaultValue(0)
    ebiSym_EBIMSK2_MEMTYPE.setOutputMode("Value")
    ebiSym_EBIMSK2_MEMTYPE.setDisplayMode("Description")
    for ii in ebiMEMTYPE_names:
        ebiSym_EBIMSK2_MEMTYPE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK2_MEMTYPE.setVisible(True)

    ebiREGSEL_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_REGSEL, ebiREGSEL_names)
    ebiSym_EBIMSK2_REGSEL = ebiComponent.createKeyValueSetSymbol("EBIMSK2_REGSEL", ebiSym_EBICS2_CSADDR)
    ebiSym_EBIMSK2_REGSEL.setLabel(ebiBitFld_EBIMSK0_REGSEL.getAttribute("caption"))
    ebiSym_EBIMSK2_REGSEL.setOutputMode("Value")
    ebiSym_EBIMSK2_REGSEL.setDisplayMode("Description")
    for ii in ebiREGSEL_names:
        ebiSym_EBIMSK2_REGSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK2_REGSEL.setDefaultValue(1)
    ebiSym_EBIMSK2_REGSEL.setVisible(True)

    #EBIMSK2_Value
    ebiSym_EBIMSK2_VALUE = ebiComponent.createHexSymbol("EBIMSK2_VALUE", None)
    ebiSym_EBIMSK2_VALUE.setDefaultValue(0x120)
    ebiSym_EBIMSK2_VALUE.setVisible(False)
    ebiSym_EBIMSK2_VALUE.setDependencies(combineMSK2_Values, ["EBIMSK2_MEMSIZE","EBIMSK2_MEMTYPE","EBIMSK2_REGSEL"])

    #EBIMSK3
    ebiMEMSIZE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMSIZE, ebiMEMSIZE_names)
    ebiSym_EBIMSK3_MEMSIZE = ebiComponent.createKeyValueSetSymbol("EBIMSK3_MEMSIZE", ebiSym_EBICS3_CSADDR)
    ebiSym_EBIMSK3_MEMSIZE.setLabel(ebiBitFld_EBIMSK0_MEMSIZE.getAttribute("caption"))
    ebiSym_EBIMSK3_MEMSIZE.setDefaultValue(0)
    ebiSym_EBIMSK3_MEMSIZE.setOutputMode("Value")
    ebiSym_EBIMSK3_MEMSIZE.setDisplayMode("Description")
    for ii in ebiMEMSIZE_names:
        ebiSym_EBIMSK3_MEMSIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK3_MEMSIZE.setVisible(True)

    ebiMEMTYPE_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_MEMTYPE, ebiMEMTYPE_names)
    ebiSym_EBIMSK3_MEMTYPE = ebiComponent.createKeyValueSetSymbol("EBIMSK3_MEMTYPE", ebiSym_EBICS3_CSADDR)
    ebiSym_EBIMSK3_MEMTYPE.setLabel(ebiBitFld_EBIMSK0_MEMTYPE.getAttribute("caption"))
    ebiSym_EBIMSK3_MEMTYPE.setDefaultValue(0)
    ebiSym_EBIMSK3_MEMTYPE.setOutputMode("Value")
    ebiSym_EBIMSK3_MEMTYPE.setDisplayMode("Description")
    for ii in ebiMEMTYPE_names:
        ebiSym_EBIMSK3_MEMTYPE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK3_MEMTYPE.setVisible(True)

    ebiREGSEL_names = []
    _get_bitfield_names(ebiValGrp_EBIMSK0_REGSEL, ebiREGSEL_names)
    ebiSym_EBIMSK3_REGSEL = ebiComponent.createKeyValueSetSymbol("EBIMSK3_REGSEL", ebiSym_EBICS3_CSADDR)
    ebiSym_EBIMSK3_REGSEL.setLabel(ebiBitFld_EBIMSK0_REGSEL.getAttribute("caption"))
    ebiSym_EBIMSK3_REGSEL.setOutputMode("Value")
    ebiSym_EBIMSK3_REGSEL.setDisplayMode("Description")
    for ii in ebiREGSEL_names:
        ebiSym_EBIMSK3_REGSEL.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBIMSK3_REGSEL.setDefaultValue(1)
    ebiSym_EBIMSK3_REGSEL.setVisible(True)

    #EBIMSK3_Value
    ebiSym_EBIMSK3_VALUE = ebiComponent.createHexSymbol("EBIMSK3_VALUE", None)
    ebiSym_EBIMSK3_VALUE.setDefaultValue(0x120)
    ebiSym_EBIMSK3_VALUE.setVisible(False)
    ebiSym_EBIMSK3_VALUE.setDependencies(combineMSK3_Values, ["EBIMSK3_MEMSIZE","EBIMSK3_MEMTYPE","EBIMSK3_REGSEL"])

    #EBISMT0
    ebiSym_EBISMT0_Comment = ebiComponent.createCommentSymbol("EBISMT0_LABEL", None)
    ebiSym_EBISMT0_Comment.setVisible(True)
    ebiSym_EBISMT0_Comment.setLabel("EBI Static Memory Timing 0 (EBISMT0)")

    ebiSym_EBISMT0_TRC = ebiComponent.createIntegerSymbol("EBISMT0_TRC", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TRC.setLabel(ebiBitFld_EBISMT0_TRC.getAttribute("caption"))
    ebiSym_EBISMT0_TRC.setDefaultValue(11)
    ebiSym_EBISMT0_TRC.setMin(0)
    ebiSym_EBISMT0_TRC.setMax(63)
    ebiSym_EBISMT0_TRC.setVisible(True)

    ebiSym_EBISMT0_TAS = ebiComponent.createIntegerSymbol("EBISMT0_TAS", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TAS.setLabel(ebiBitFld_EBISMT0_TAS.getAttribute("caption"))
    ebiSym_EBISMT0_TAS.setDefaultValue(1)
    ebiSym_EBISMT0_TAS.setMin(0)
    ebiSym_EBISMT0_TAS.setMax(3)
    ebiSym_EBISMT0_TAS.setVisible(True)

    ebiSym_EBISMT0_TWR = ebiComponent.createIntegerSymbol("EBISMT0_TWR", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TWR.setLabel(ebiBitFld_EBISMT0_TWR.getAttribute("caption"))
    ebiSym_EBISMT0_TWR.setDefaultValue(1)
    ebiSym_EBISMT0_TWR.setMin(0)
    ebiSym_EBISMT0_TWR.setMax(3)
    ebiSym_EBISMT0_TWR.setVisible(True)

    ebiSym_EBISMT0_TWP = ebiComponent.createIntegerSymbol("EBISMT0_TWP", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TWP.setLabel(ebiBitFld_EBISMT0_TWP.getAttribute("caption"))
    ebiSym_EBISMT0_TWP.setDefaultValue(11)
    ebiSym_EBISMT0_TWP.setMin(0)
    ebiSym_EBISMT0_TWP.setMax(63)
    ebiSym_EBISMT0_TWP.setVisible(True)

    ebiSym_EBISMT0_TBTA = ebiComponent.createIntegerSymbol("EBISMT0_TBTA", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TBTA.setLabel(ebiBitFld_EBISMT0_TBTA.getAttribute("caption"))
    ebiSym_EBISMT0_TBTA.setDefaultValue(4)
    ebiSym_EBISMT0_TBTA.setMin(0)
    ebiSym_EBISMT0_TBTA.setMax(7)
    ebiSym_EBISMT0_TBTA.setVisible(True)

    ebiSym_EBISMT0_TPRC = ebiComponent.createIntegerSymbol("EBISMT0_TPRC", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_TPRC.setLabel(ebiBitFld_EBISMT0_TPRC.getAttribute("caption"))
    ebiSym_EBISMT0_TPRC.setDefaultValue(3)
    ebiSym_EBISMT0_TPRC.setMin(0)
    ebiSym_EBISMT0_TPRC.setMax(15)
    ebiSym_EBISMT0_TPRC.setVisible(True)

    ebiSym_EBISMT0_PAGEMODE = ebiComponent.createBooleanSymbol("EBISMT0_PAGEMODE", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_PAGEMODE.setLabel(ebiBitFld_EBISMT0_PAGEMODE.getAttribute("caption"))
    ebiSym_EBISMT0_PAGEMODE.setDefaultValue(False)
    ebiSym_EBISMT0_PAGEMODE.setVisible(True)

    ebiPAGESIZE_names = []
    _get_bitfield_names(ebiValGrp_EBISMT0_PAGESIZE, ebiPAGESIZE_names)
    ebiSym_EBISMT0_PAGESIZE = ebiComponent.createKeyValueSetSymbol("EBISMT0_PAGESIZE", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_PAGESIZE.setLabel(ebiBitFld_EBISMT0_PAGESIZE.getAttribute("caption"))
    ebiSym_EBISMT0_PAGESIZE.setDefaultValue(0)
    ebiSym_EBISMT0_PAGESIZE.setOutputMode("Value")
    ebiSym_EBISMT0_PAGESIZE.setDisplayMode("Description")
    for ii in ebiPAGESIZE_names:
        ebiSym_EBISMT0_PAGESIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMT0_PAGESIZE.setVisible(True)

    ebiSym_EBISMT0_RDYMODE = ebiComponent.createBooleanSymbol("EBISMT0_RDYMODE", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMT0_RDYMODE.setLabel(ebiBitFld_EBISMT0_RDYMODE.getAttribute("caption"))
    ebiSym_EBISMT0_RDYMODE.setDefaultValue(False)
    ebiSym_EBISMT0_RDYMODE.setVisible(True)

    #EBISMT0_Value
    ebiSym_EBISMT0_VALUE = ebiComponent.createHexSymbol("EBISMT0_VALUE", None)
    ebiSym_EBISMT0_VALUE.setDefaultValue(68955467)
    ebiSym_EBISMT0_VALUE.setVisible(False)
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TRC"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TAS"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TWR"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TWP"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TBTA"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_TPRC"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_PAGEMODE"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_PAGESIZE"])
    ebiSym_EBISMT0_VALUE.setDependencies(combineSMT0_Values, ["EBISMT0_RDYMODE"])

    #EBISMT1
    ebiSym_EBISMT1_Comment = ebiComponent.createCommentSymbol("EBISMT1_LABEL", None)
    ebiSym_EBISMT1_Comment.setVisible(True)
    ebiSym_EBISMT1_Comment.setLabel("EBI Static Memory Timing 1 (EBISMT1)")

    ebiSym_EBISMT1_TRC = ebiComponent.createIntegerSymbol("EBISMT1_TRC", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TRC.setLabel(ebiBitFld_EBISMT0_TRC.getAttribute("caption"))
    ebiSym_EBISMT1_TRC.setDefaultValue(11)
    ebiSym_EBISMT1_TRC.setMin(0)
    ebiSym_EBISMT1_TRC.setMax(63)
    ebiSym_EBISMT1_TRC.setVisible(True)

    ebiSym_EBISMT1_TAS = ebiComponent.createIntegerSymbol("EBISMT1_TAS", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TAS.setLabel(ebiBitFld_EBISMT0_TAS.getAttribute("caption"))
    ebiSym_EBISMT1_TAS.setDefaultValue(1)
    ebiSym_EBISMT1_TAS.setMin(0)
    ebiSym_EBISMT1_TAS.setMax(3)
    ebiSym_EBISMT1_TAS.setVisible(True)

    ebiSym_EBISMT1_TWR = ebiComponent.createIntegerSymbol("EBISMT1_TWR", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TWR.setLabel(ebiBitFld_EBISMT0_TWR.getAttribute("caption"))
    ebiSym_EBISMT1_TWR.setDefaultValue(1)
    ebiSym_EBISMT1_TWR.setMin(0)
    ebiSym_EBISMT1_TWR.setMax(3)
    ebiSym_EBISMT1_TWR.setVisible(True)

    ebiSym_EBISMT1_TWP = ebiComponent.createIntegerSymbol("EBISMT1_TWP", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TWP.setLabel(ebiBitFld_EBISMT0_TWP.getAttribute("caption"))
    ebiSym_EBISMT1_TWP.setDefaultValue(11)
    ebiSym_EBISMT1_TWP.setMin(0)
    ebiSym_EBISMT1_TWP.setMax(63)
    ebiSym_EBISMT1_TWP.setVisible(True)

    ebiSym_EBISMT1_TBTA = ebiComponent.createIntegerSymbol("EBISMT1_TBTA", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TBTA.setLabel(ebiBitFld_EBISMT0_TBTA.getAttribute("caption"))
    ebiSym_EBISMT1_TBTA.setDefaultValue(4)
    ebiSym_EBISMT1_TBTA.setMin(0)
    ebiSym_EBISMT1_TBTA.setMax(7)
    ebiSym_EBISMT1_TBTA.setVisible(True)

    ebiSym_EBISMT1_TPRC = ebiComponent.createIntegerSymbol("EBISMT1_TPRC", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_TPRC.setLabel(ebiBitFld_EBISMT0_TPRC.getAttribute("caption"))
    ebiSym_EBISMT1_TPRC.setDefaultValue(3)
    ebiSym_EBISMT1_TPRC.setMin(0)
    ebiSym_EBISMT1_TPRC.setMax(15)
    ebiSym_EBISMT1_TPRC.setVisible(True)

    ebiSym_EBISMT1_PAGEMODE = ebiComponent.createBooleanSymbol("EBISMT1_PAGEMODE", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_PAGEMODE.setLabel(ebiBitFld_EBISMT0_PAGEMODE.getAttribute("caption"))
    ebiSym_EBISMT1_PAGEMODE.setDefaultValue(False)
    ebiSym_EBISMT1_PAGEMODE.setVisible(True)

    ebiPAGESIZE_names = []
    _get_bitfield_names(ebiValGrp_EBISMT0_PAGESIZE, ebiPAGESIZE_names)
    ebiSym_EBISMT1_PAGESIZE = ebiComponent.createKeyValueSetSymbol("EBISMT1_PAGESIZE", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_PAGESIZE.setLabel(ebiBitFld_EBISMT0_PAGESIZE.getAttribute("caption"))
    ebiSym_EBISMT1_PAGESIZE.setDefaultValue(0)
    ebiSym_EBISMT1_PAGESIZE.setOutputMode("Value")
    ebiSym_EBISMT1_PAGESIZE.setDisplayMode("Description")
    for ii in ebiPAGESIZE_names:
        ebiSym_EBISMT1_PAGESIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMT1_PAGESIZE.setVisible(True)

    ebiSym_EBISMT1_RDYMODE = ebiComponent.createBooleanSymbol("EBISMT1_RDYMODE", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMT1_RDYMODE.setLabel(ebiBitFld_EBISMT0_RDYMODE.getAttribute("caption"))
    ebiSym_EBISMT1_RDYMODE.setDefaultValue(False)
    ebiSym_EBISMT1_RDYMODE.setVisible(True)

    #EBISMT1_Value
    ebiSym_EBISMT1_VALUE = ebiComponent.createHexSymbol("EBISMT1_VALUE", None)
    ebiSym_EBISMT1_VALUE.setDefaultValue(68955467)
    ebiSym_EBISMT1_VALUE.setVisible(False)
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TRC"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TAS"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TWR"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TWP"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TBTA"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_TPRC"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_PAGEMODE"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_PAGESIZE"])
    ebiSym_EBISMT1_VALUE.setDependencies(combineSMT1_Values, ["EBISMT1_RDYMODE"])

    #EBISMT2
    ebiSym_EBISMT2_Comment = ebiComponent.createCommentSymbol("EBISMT2_LABEL", None)
    ebiSym_EBISMT2_Comment.setVisible(True)
    ebiSym_EBISMT2_Comment.setLabel("EBI Static Memory Timing 2 (EBISMT2)")

    ebiSym_EBISMT2_TRC = ebiComponent.createIntegerSymbol("EBISMT2_TRC", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TRC.setLabel(ebiBitFld_EBISMT0_TRC.getAttribute("caption"))
    ebiSym_EBISMT2_TRC.setDefaultValue(11)
    ebiSym_EBISMT2_TRC.setMin(0)
    ebiSym_EBISMT2_TRC.setMax(63)
    ebiSym_EBISMT2_TRC.setVisible(True)

    ebiSym_EBISMT2_TAS = ebiComponent.createIntegerSymbol("EBISMT2_TAS", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TAS.setLabel(ebiBitFld_EBISMT0_TAS.getAttribute("caption"))
    ebiSym_EBISMT2_TAS.setDefaultValue(1)
    ebiSym_EBISMT2_TAS.setMin(0)
    ebiSym_EBISMT2_TAS.setMax(3)
    ebiSym_EBISMT2_TAS.setVisible(True)

    ebiSym_EBISMT2_TWR = ebiComponent.createIntegerSymbol("EBISMT2_TWR", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TWR.setLabel(ebiBitFld_EBISMT0_TWR.getAttribute("caption"))
    ebiSym_EBISMT2_TWR.setDefaultValue(1)
    ebiSym_EBISMT2_TWR.setMin(0)
    ebiSym_EBISMT2_TWR.setMax(3)
    ebiSym_EBISMT2_TWR.setVisible(True)

    ebiSym_EBISMT2_TWP = ebiComponent.createIntegerSymbol("EBISMT2_TWP", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TWP.setLabel(ebiBitFld_EBISMT0_TWP.getAttribute("caption"))
    ebiSym_EBISMT2_TWP.setDefaultValue(11)
    ebiSym_EBISMT2_TWP.setMin(0)
    ebiSym_EBISMT2_TWP.setMax(63)
    ebiSym_EBISMT2_TWP.setVisible(True)

    ebiSym_EBISMT2_TBTA = ebiComponent.createIntegerSymbol("EBISMT2_TBTA", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TBTA.setLabel(ebiBitFld_EBISMT0_TBTA.getAttribute("caption"))
    ebiSym_EBISMT2_TBTA.setDefaultValue(4)
    ebiSym_EBISMT2_TBTA.setMin(0)
    ebiSym_EBISMT2_TBTA.setMax(7)
    ebiSym_EBISMT2_TBTA.setVisible(True)

    ebiSym_EBISMT2_TPRC = ebiComponent.createIntegerSymbol("EBISMT2_TPRC", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_TPRC.setLabel(ebiBitFld_EBISMT0_TPRC.getAttribute("caption"))
    ebiSym_EBISMT2_TPRC.setDefaultValue(3)
    ebiSym_EBISMT2_TPRC.setMin(0)
    ebiSym_EBISMT2_TPRC.setMax(15)
    ebiSym_EBISMT2_TPRC.setVisible(True)

    ebiSym_EBISMT2_PAGEMODE = ebiComponent.createBooleanSymbol("EBISMT2_PAGEMODE", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_PAGEMODE.setLabel(ebiBitFld_EBISMT0_PAGEMODE.getAttribute("caption"))
    ebiSym_EBISMT2_PAGEMODE.setDefaultValue(False)
    ebiSym_EBISMT2_PAGEMODE.setVisible(True)

    ebiPAGESIZE_names = []
    _get_bitfield_names(ebiValGrp_EBISMT0_PAGESIZE, ebiPAGESIZE_names)
    ebiSym_EBISMT2_PAGESIZE = ebiComponent.createKeyValueSetSymbol("EBISMT2_PAGESIZE", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_PAGESIZE.setLabel(ebiBitFld_EBISMT0_PAGESIZE.getAttribute("caption"))
    ebiSym_EBISMT2_PAGESIZE.setDefaultValue(0)
    ebiSym_EBISMT2_PAGESIZE.setOutputMode("Value")
    ebiSym_EBISMT2_PAGESIZE.setDisplayMode("Description")
    for ii in ebiPAGESIZE_names:
        ebiSym_EBISMT2_PAGESIZE.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMT2_PAGESIZE.setVisible(True)

    ebiSym_EBISMT2_RDYMODE = ebiComponent.createBooleanSymbol("EBISMT2_RDYMODE", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMT2_RDYMODE.setLabel(ebiBitFld_EBISMT0_RDYMODE.getAttribute("caption"))
    ebiSym_EBISMT2_RDYMODE.setDefaultValue(False)
    ebiSym_EBISMT2_RDYMODE.setVisible(True)

    #EBISMT2_Value
    ebiSym_EBISMT2_VALUE = ebiComponent.createHexSymbol("EBISMT2_VALUE", None)
    ebiSym_EBISMT2_VALUE.setDefaultValue(68955467)
    ebiSym_EBISMT2_VALUE.setVisible(False)
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TRC"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TAS"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TWR"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TWP"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TBTA"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_TPRC"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_PAGEMODE"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_PAGESIZE"])
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMT2_Values, ["EBISMT2_RDYMODE"])

    #EBIFTRPD
    ebiSym_EBIFTRPD_TRPD = ebiComponent.createHexSymbol("EBIFTRPD_TRPD", None)
    ebiSym_EBIFTRPD_TRPD.setLabel(ebiBitFld_EBIFTRPD_TRPD.getAttribute("caption"))
    ebiSym_EBIFTRPD_TRPD.setDefaultValue(200)
    ebiSym_EBIFTRPD_TRPD.setMin(0)
    ebiSym_EBIFTRPD_TRPD.setMax(4095)
    ebiSym_EBIFTRPD_TRPD.setVisible(True)

    #EBISMCON
    ebiSMDWIDTH_names = []
    _get_bitfield_names(ebiValGrp_EBISMCON_SMDWIDTH0, ebiSMDWIDTH_names)
    ebiSym_EBISMCON_SMDWIDTH0 = ebiComponent.createKeyValueSetSymbol("EBISMCON_SMDWIDTH0", ebiSym_EBISMT0_Comment)
    ebiSym_EBISMCON_SMDWIDTH0.setLabel(ebiBitFld_EBISMCON_SMDWIDTH0.getAttribute("caption"))

    ebiSym_EBISMCON_SMDWIDTH0.setOutputMode("Value")
    ebiSym_EBISMCON_SMDWIDTH0.setDisplayMode("Description")
    for ii in ebiSMDWIDTH_names:
        ebiSym_EBISMCON_SMDWIDTH0.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMCON_SMDWIDTH0.setDefaultValue(1)
    ebiSym_EBISMCON_SMDWIDTH0.setVisible(True)

    ebiSym_EBISMCON_SMDWIDTH1 = ebiComponent.createKeyValueSetSymbol("EBISMCON_SMDWIDTH1", ebiSym_EBISMT1_Comment)
    ebiSym_EBISMCON_SMDWIDTH1.setLabel(ebiBitFld_EBISMCON_SMDWIDTH1.getAttribute("caption"))
    ebiSym_EBISMCON_SMDWIDTH1.setDefaultValue(0)
    ebiSym_EBISMCON_SMDWIDTH1.setOutputMode("Value")
    ebiSym_EBISMCON_SMDWIDTH1.setDisplayMode("Description")
    for ii in ebiSMDWIDTH_names:
        ebiSym_EBISMCON_SMDWIDTH1.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMCON_SMDWIDTH1.setVisible(True)

    ebiSym_EBISMCON_SMDWIDTH2 = ebiComponent.createKeyValueSetSymbol("EBISMCON_SMDWIDTH2", ebiSym_EBISMT2_Comment)
    ebiSym_EBISMCON_SMDWIDTH2.setLabel(ebiBitFld_EBISMCON_SMDWIDTH2.getAttribute("caption"))
    ebiSym_EBISMCON_SMDWIDTH2.setDefaultValue(0)
    ebiSym_EBISMCON_SMDWIDTH2.setOutputMode("Value")
    ebiSym_EBISMCON_SMDWIDTH2.setDisplayMode("Description")
    for ii in ebiSMDWIDTH_names:
        ebiSym_EBISMCON_SMDWIDTH2.addKey( ii['desc'], ii['value'], ii['key'] )
    ebiSym_EBISMCON_SMDWIDTH2.setVisible(True)

    #EBISMCON_Value
    ebiSym_EBISMT2_VALUE = ebiComponent.createHexSymbol("EBISMCON_VALUE", None)
    ebiSym_EBISMT2_VALUE.setDefaultValue(513)
    ebiSym_EBISMT2_VALUE.setVisible(False)
    ebiSym_EBISMT2_VALUE.setDependencies(combineSMCON_Values, ["EBISMCON_SMDWIDTH0","EBISMCON_SMDWIDTH1","EBISMCON_SMDWIDTH2"])

    # Clock Warning status
    ebiSym_ClkEnComment = ebiComponent.createCommentSymbol("EBI_CLOCK_ENABLE_COMMENT", None)
    ebiSym_ClkEnComment.setLabel("Warning!!! " + ebiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    ebiSym_ClkEnComment.setVisible(False)
    ebiSym_ClkEnComment.setDependencies(updateEBIClockWarningStatus, ["core." + ebiInstanceName.getValue() + "_CLOCK_ENABLE"])

############################################################################
#### Dependency ####
############################################################################


############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    ebiHeader1File = ebiComponent.createFileSymbol("EBI_HEADER1", None)
    ebiHeader1File.setMarkup(True)
    ebiHeader1File.setSourcePath("../peripheral/ebi_00109/templates/plib_ebi.h.ftl")
    ebiHeader1File.setOutputName("plib_ebi.h")
    ebiHeader1File.setDestPath("peripheral/ebi/")
    ebiHeader1File.setProjectPath("config/" + configName + "/peripheral/ebi/")
    ebiHeader1File.setType("HEADER")
    ebiHeader1File.setOverwrite(True)

    ebiSource1File = ebiComponent.createFileSymbol("EBI_SOURCE1", None)
    ebiSource1File.setMarkup(True)
    ebiSource1File.setSourcePath("../peripheral/ebi_00109/templates/plib_ebi.c.ftl")
    ebiSource1File.setOutputName("plib_ebi.c")
    ebiSource1File.setDestPath("peripheral/ebi/")
    ebiSource1File.setProjectPath("config/" + configName + "/peripheral/ebi/")
    ebiSource1File.setType("SOURCE")
    ebiSource1File.setOverwrite(True)

    ebiSystemInitFile = ebiComponent.createFileSymbol("EBI_INIT", None)
    ebiSystemInitFile.setType("STRING")
    ebiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ebiSystemInitFile.setSourcePath("../peripheral/ebi_00109/templates/system/initialization.c.ftl")
    ebiSystemInitFile.setMarkup(True)

    ebiSystemDefFile = ebiComponent.createFileSymbol("EBI_DEF", None)
    ebiSystemDefFile.setType("STRING")
    ebiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ebiSystemDefFile.setSourcePath("../peripheral/ebi_00109/templates/system/definitions.h.ftl")
    ebiSystemDefFile.setMarkup(True)

