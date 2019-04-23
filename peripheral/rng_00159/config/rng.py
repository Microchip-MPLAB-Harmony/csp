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
rngValGrp_RNGCON_TRNGEN     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/value-group@[name="RNGCON__TRNGEN"]')
rngValGrp_RNGCON_PRNGEN     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/value-group@[name="RNGCON__PRNGEN"]')
rngValGrp_RNGCON_CONT       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/value-group@[name="RNGCON__CONT"]')
rngValGrp_RNGCON_TRNGMODE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/value-group@[name="RNGCON__TRNGMODE"]')

rngBitFld_RNGCON_PLEN       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/register-group@[name="RNG"]/register@[name="RNGCON"]/bitfield@[name="PLEN"]')
rngBitFld_RNGCON_TRNGEN     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/register-group@[name="RNG"]/register@[name="RNGCON"]/bitfield@[name="TRNGEN"]')
rngBitFld_RNGCON_PRNGEN     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/register-group@[name="RNG"]/register@[name="RNGCON"]/bitfield@[name="PRNGEN"]')
rngBitFld_RNGCON_CONT       = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/register-group@[name="RNG"]/register@[name="RNGCON"]/bitfield@[name="CONT"]')
rngBitFld_RNGCON_TRNGMODE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="RNG"]/register-group@[name="RNG"]/register@[name="RNGCON"]/bitfield@[name="TRNGMODE"]')
################################################################################
#### Global Variables ####
################################################################################
global rngInstanceName
global rngSym_RNGCON_PLEN
global rngSym_RNGCON_TRNGEN
global rngSym_RNGCON_PRNGEN
global rngSym_RNGCON_CONT
global rngSym_RNGCON_TRNGMODE

################################################################################
#### Business Logic ####
################################################################################

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

def combineValues(symbol, event):
    plenValue   = rngSym_RNGCON_PLEN.getValue() << 0
    trngenValue = rngSym_RNGCON_TRNGEN.getValue() << 8
    prngenValue = rngSym_RNGCON_PRNGEN.getValue() << 9
    contValue   = rngSym_RNGCON_CONT.getValue() << 10
    trngValue   = rngSym_RNGCON_TRNGMODE.getValue() << 11
    rngconValue = plenValue + trngenValue + prngenValue + contValue + trngValue
    symbol.setValue(rngconValue, 2)

def updateRNGClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################
def instantiateComponent(rngComponent):
    global rngInstanceName
    global rngSym_RNGCON_PLEN
    global rngSym_RNGCON_TRNGEN
    global rngSym_RNGCON_PRNGEN
    global rngSym_RNGCON_CONT
    global rngSym_RNGCON_TRNGMODE

    rngInstanceName = rngComponent.createStringSymbol("RNG_INSTANCE_NAME", None)
    rngInstanceName.setVisible(False)
    rngInstanceName.setDefaultValue(rngComponent.getID().upper())
    print("Running " + rngInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", rngInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    rngSym_RNGCON_PLEN = rngComponent.createIntegerSymbol("RNGCON_PLEN", None)
    rngSym_RNGCON_PLEN.setLabel(rngBitFld_RNGCON_PLEN.getAttribute("caption"))
    rngSym_RNGCON_PLEN.setDefaultValue(0)
    rngSym_RNGCON_PLEN.setMin(0)
    rngSym_RNGCON_PLEN.setMax(64)
    rngSym_RNGCON_PLEN.setVisible(True)

    rngTRNGEN_names = []
    _get_bitfield_names(rngValGrp_RNGCON_TRNGEN, rngTRNGEN_names)
    rngSym_RNGCON_TRNGEN = rngComponent.createKeyValueSetSymbol("RNGCON_TRNGEN", None)
    rngSym_RNGCON_TRNGEN.setLabel(rngBitFld_RNGCON_TRNGEN.getAttribute("caption"))
    rngSym_RNGCON_TRNGEN.setDefaultValue(0)
    rngSym_RNGCON_TRNGEN.setOutputMode("Value")
    rngSym_RNGCON_TRNGEN.setDisplayMode("Description")
    for ii in rngTRNGEN_names:
        rngSym_RNGCON_TRNGEN.addKey( ii['desc'], ii['value'], ii['key'] )
    rngSym_RNGCON_TRNGEN.setVisible(True)

    rngPRNGEN_names = []
    _get_bitfield_names(rngValGrp_RNGCON_PRNGEN, rngPRNGEN_names)
    rngSym_RNGCON_PRNGEN = rngComponent.createKeyValueSetSymbol("RNGCON_PRNGEN", None)
    rngSym_RNGCON_PRNGEN.setLabel(rngBitFld_RNGCON_PRNGEN.getAttribute("caption"))
    rngSym_RNGCON_PRNGEN.setDefaultValue(0)
    rngSym_RNGCON_PRNGEN.setOutputMode("Value")
    rngSym_RNGCON_PRNGEN.setDisplayMode("Description")
    for ii in rngPRNGEN_names:
        rngSym_RNGCON_PRNGEN.addKey( ii['desc'], ii['value'], ii['key'] )
    rngSym_RNGCON_PRNGEN.setVisible(True)

    rngCONT_names = []
    _get_bitfield_names(rngValGrp_RNGCON_CONT, rngCONT_names)
    rngSym_RNGCON_CONT = rngComponent.createKeyValueSetSymbol("RNGCON_CONT", None)
    rngSym_RNGCON_CONT.setLabel(rngBitFld_RNGCON_CONT.getAttribute("caption"))
    rngSym_RNGCON_CONT.setDefaultValue(0)
    rngSym_RNGCON_CONT.setOutputMode("Value")
    rngSym_RNGCON_CONT.setDisplayMode("Description")
    for ii in rngCONT_names:
        rngSym_RNGCON_CONT.addKey( ii['desc'], ii['value'], ii['key'] )
    rngSym_RNGCON_CONT.setVisible(True)

    rngTRNGMODE_names = []
    _get_bitfield_names(rngValGrp_RNGCON_TRNGMODE, rngTRNGMODE_names)
    rngSym_RNGCON_TRNGMODE = rngComponent.createKeyValueSetSymbol("RNGCON_TRNGMODE", None)
    rngSym_RNGCON_TRNGMODE.setLabel(rngBitFld_RNGCON_TRNGMODE.getAttribute("caption"))
    rngSym_RNGCON_TRNGMODE.setDefaultValue(0)
    rngSym_RNGCON_TRNGMODE.setOutputMode("Value")
    rngSym_RNGCON_TRNGMODE.setDisplayMode("Description")
    for ii in rngTRNGMODE_names:
        rngSym_RNGCON_TRNGMODE.addKey( ii['desc'], ii['value'], ii['key'] )
    rngSym_RNGCON_TRNGMODE.setVisible(True)

    #Collect user input to combine into RNGCON register
    rngSym_RNGCON = rngComponent.createHexSymbol("RNGCON_VALUE", None)
    rngSym_RNGCON.setDefaultValue(0)
    rngSym_RNGCON.setVisible(False)
    rngSym_RNGCON.setDependencies(combineValues, ["RNGCON_PLEN"])
    rngSym_RNGCON.setDependencies(combineValues, ["RNGCON_TRNGEN"])
    rngSym_RNGCON.setDependencies(combineValues, ["RNGCON_PRNGEN"])
    rngSym_RNGCON.setDependencies(combineValues, ["RNGCON_CONT"])
    rngSym_RNGCON.setDependencies(combineValues, ["RNGCON_TRNGMODE"])

    # Clock Warning status
    rngSym_ClkEnComment = rngComponent.createCommentSymbol("RNG_CLOCK_ENABLE_COMMENT", None)
    rngSym_ClkEnComment.setLabel("Warning!!! " + rngInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    rngSym_ClkEnComment.setVisible(False)
    rngSym_ClkEnComment.setDependencies(updateRNGClockWarningStatus, ["core." + rngInstanceName.getValue() + "_CLOCK_ENABLE"])


############################################################################
#### Dependency ####
############################################################################


############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    rngHeader1File = rngComponent.createFileSymbol("RNG_HEADER1", None)
    rngHeader1File.setMarkup(True)
    rngHeader1File.setSourcePath("../peripheral/rng_00159/templates/plib_rng.h.ftl")
    rngHeader1File.setOutputName("plib_rng.h")
    rngHeader1File.setDestPath("peripheral/rng/")
    rngHeader1File.setProjectPath("config/" + configName + "/peripheral/rng/")
    rngHeader1File.setType("HEADER")
    rngHeader1File.setOverwrite(True)

    rngSource1File = rngComponent.createFileSymbol("RNG_SOURCE1", None)
    rngSource1File.setMarkup(True)
    rngSource1File.setSourcePath("../peripheral/rng_00159/templates/plib_rng.c.ftl")
    rngSource1File.setOutputName("plib_rng.c")
    rngSource1File.setDestPath("peripheral/rng/")
    rngSource1File.setProjectPath("config/" + configName + "/peripheral/rng/")
    rngSource1File.setType("SOURCE")
    rngSource1File.setOverwrite(True)

    rngSystemInitFile = rngComponent.createFileSymbol("RNG_INIT", None)
    rngSystemInitFile.setType("STRING")
    rngSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rngSystemInitFile.setSourcePath("../peripheral/rng_00159/templates/system/initialization.c.ftl")
    rngSystemInitFile.setMarkup(True)

    rngSystemDefFile = rngComponent.createFileSymbol("RNG_DEF", None)
    rngSystemDefFile.setType("STRING")
    rngSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rngSystemDefFile.setSourcePath("../peripheral/rng_00159/templates/system/definitions.h.ftl")
    rngSystemDefFile.setMarkup(True)

