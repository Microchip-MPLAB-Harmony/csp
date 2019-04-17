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

cvrValGrp_CVRCON_CVRSS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CVR"]/value-group@[name="CVRCON__CVRSS"]')
cvrValGrp_CVRCON_CVRR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="CVR"]/value-group@[name="CVRCON__CVRR"]')

################################################################################
#### Global Variables ####
################################################################################

global cmpInstanceName
global cvrSym_CVRCON_CVR
global cvrSym_CVRCON_CVRSS
global cvrSym_CVRCON_CVRR
global cvrSym_CVRCON_CVROE

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

    cvrValue    = cvrSym_CVRCON_CVR.getValue() << 0
    cvrssValue  = cvrSym_CVRCON_CVRSS.getValue() << 4
    cvrrValue   = cvrSym_CVRCON_CVRR.getValue() << 5
    cvroeValue  = cvrSym_CVRCON_CVROE.getValue() << 6
    cvrconValue = cvrValue + cvrssValue + cvrrValue + cvroeValue
    symbol.setValue(cvrconValue, 2)

def updateCVRClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

################################################################################
#### Component ####
################################################################################

def instantiateComponent(cvrComponent):
    global cvrInstanceName
    global cvrSym_CVRCON_CVR
    global cvrSym_CVRCON_CVRSS
    global cvrSym_CVRCON_CVRR
    global cvrSym_CVRCON_CVROE

    cvrInstanceName = cvrComponent.createStringSymbol("CVR_INSTANCE_NAME", None)
    cvrInstanceName.setVisible(False)
    cvrInstanceName.setDefaultValue(cvrComponent.getID().upper())
    print("Running " + cvrInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", cvrInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    cvrSym_CVRCON_CVR = cvrComponent.createIntegerSymbol("CVR_CVRCON_CVR", None)
    cvrSym_CVRCON_CVR.setLabel("CVREF Value Selection")
    cvrSym_CVRCON_CVR.setDefaultValue(0)
    cvrSym_CVRCON_CVR.setMin(0)
    cvrSym_CVRCON_CVR.setMax(15)

    cvrCVRSS_names = []
    _get_bitfield_names(cvrValGrp_CVRCON_CVRSS, cvrCVRSS_names)
    cvrSym_CVRCON_CVRSS = cvrComponent.createKeyValueSetSymbol("CVR_CVRCON_CVRSS", None)
    cvrSym_CVRCON_CVRSS.setLabel("CVREF Source Selection")
    cvrSym_CVRCON_CVRSS.setDefaultValue(0)
    cvrSym_CVRCON_CVRSS.setOutputMode("Value")
    cvrSym_CVRCON_CVRSS.setDisplayMode("Description")
    for ii in cvrCVRSS_names:
        cvrSym_CVRCON_CVRSS.addKey( ii['desc'], ii['value'], ii['key'] )

    cvrCVRR_names = []
    _get_bitfield_names(cvrValGrp_CVRCON_CVRR, cvrCVRR_names)
    cvrSym_CVRCON_CVRR = cvrComponent.createKeyValueSetSymbol("CVR_CVRCON_CVRR", None)
    cvrSym_CVRCON_CVRR.setLabel("CVREF Range Selection")
    cvrSym_CVRCON_CVRR.setDefaultValue(0)
    cvrSym_CVRCON_CVRR.setOutputMode("Value")
    cvrSym_CVRCON_CVRR.setDisplayMode("Description")
    for ii in cvrCVRR_names:
        cvrSym_CVRCON_CVRR.addKey( ii['desc'], ii['value'], ii['key'] )

    cvrSym_CVRCON_CVROE = cvrComponent.createBooleanSymbol("CVR_CVRCON_CVROE", None)
    cvrSym_CVRCON_CVROE.setLabel("CVREFOUT Enable")

    #Collecting user input to combine into ICxCON register
    #ICxCON is updated every time a user selection changes
    cvrSym_CVRCON = cvrComponent.createHexSymbol("CVRCON_VALUE", None)
    cvrSym_CVRCON.setDefaultValue(0)
    cvrSym_CVRCON.setVisible(False)
    cvrSym_CVRCON.setDependencies(combineValues, ["CVR_CVRCON_CVR"])
    cvrSym_CVRCON.setDependencies(combineValues, ["CVR_CVRCON_CVRSS"])
    cvrSym_CVRCON.setDependencies(combineValues, ["CVR_CVRCON_CVRR"])
    cvrSym_CVRCON.setDependencies(combineValues, ["CVR_CVRCON_CVROE"])

############################################################################
#### Dependency ####
############################################################################

    # Clock Warning status
    cvrSym_ClkEnComment = cvrComponent.createCommentSymbol("CVR_CLOCK_ENABLE_COMMENT", None)
    cvrSym_ClkEnComment.setLabel("Warning!!! " + cvrInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    cvrSym_ClkEnComment.setVisible(False)
    cvrSym_ClkEnComment.setDependencies(updateCVRClockWarningStatus, ["core." + cvrInstanceName.getValue() + "_CLOCK_ENABLE"])

############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    cvrHeader1File = cvrComponent.createFileSymbol("CVR_HEADER1", None)
    cvrHeader1File.setMarkup(True)
    cvrHeader1File.setSourcePath("../peripheral/cvr_00800/templates/plib_cvr.h.ftl")
    cvrHeader1File.setOutputName("plib_"+ cvrInstanceName.getValue().lower()+ ".h")
    cvrHeader1File.setDestPath("peripheral/cvr/")
    cvrHeader1File.setProjectPath("config/" + configName + "/peripheral/cvr/")
    cvrHeader1File.setType("HEADER")
    cvrHeader1File.setOverwrite(True)

    cvrSource1File = cvrComponent.createFileSymbol("CVR_SOURCE1", None)
    cvrSource1File.setMarkup(True)
    cvrSource1File.setSourcePath("../peripheral/cvr_00800/templates/plib_cvr.c.ftl")
    cvrSource1File.setOutputName("plib_"+cvrInstanceName.getValue().lower() + ".c")
    cvrSource1File.setDestPath("peripheral/cvr/")
    cvrSource1File.setProjectPath("config/" + configName + "/peripheral/cvr/")
    cvrSource1File.setType("SOURCE")
    cvrSource1File.setOverwrite(True)

    cvrSystemInitFile = cvrComponent.createFileSymbol("CVR_INIT", None)
    cvrSystemInitFile.setType("STRING")
    cvrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    cvrSystemInitFile.setSourcePath("../peripheral/cvr_00800/templates/system/initialization.c.ftl")
    cvrSystemInitFile.setMarkup(True)

    cvrSystemDefFile = cvrComponent.createFileSymbol("CVR_DEF", None)
    cvrSystemDefFile.setType("STRING")
    cvrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    cvrSystemDefFile.setSourcePath("../peripheral/cvr_00800/templates/system/definitions.h.ftl")
    cvrSystemDefFile.setMarkup(True)
