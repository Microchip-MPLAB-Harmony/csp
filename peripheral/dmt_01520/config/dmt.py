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
##################################### Global Variables ############################################
###################################################################################################

global dmtHeaderFile
global dmtSourceFile
global dmtSystemDefFile

global dmtInteravalValueDictionary
global dmtCountSelectDictionary

dmtInteravalValueDictionary = {

    "WIN_0"         :   "0",
    "WIN_1_2"       :   "1/2 counter value",
    "WIN_3_4"       :   "3/4 counter value",
    "WIN_7_8"       :   "7/8 counter value",
    "WIN_15_16"     :   "15/16 counter value",
    "WIN_31_32"     :   "31/32 counter value",
    "WIN_63_64"     :   "63/64 counter value",
    "WIN_127_128"   :   "127/128 counter value"
}

dmtCountSelectDictionary = {

    "DMT8"      :   "256 (2^8) cycles",
    "DMT9"      :   "512 (2^9) cycles",
    "DMT10"     :   "1024 (2^10) cycles",
    "DMT11"     :   "2048 (2^11) cycles",
    "DMT12"     :   "4096 (2^12) cycles",
    "DMT13"     :   "8192 (2^13) cycles",
    "DMT14"     :   "16384 (2^14) cycles",
    "DMT15"     :   "32768 (2^15) cycles",
    "DMT16"     :   "65536 (2^16) cycles",
    "DMT17"     :   "131072 (2^17) cycles",
    "DMT18"     :   "262144 (2^18) cycles",
    "DMT19"     :   "524288 (2^19) cycles",
    "DMT20"     :   "1048576 (2^20) cycles",
    "DMT21"     :   "2097152 (2^21) cycles",
    "DMT22"     :   "4194304 (2^22) cycles",
    "DMT23"     :   "8388608 (2^23) cycles",
    "DMT24"     :   "16777216 (2^24) cycles",
    "DMT25"     :   "33554432 (2^25) cycles",
    "DMT26"     :   "67108864 (2^26) cycles",
    "DMT27"     :   "134217728 (2^27) cycles",
    "DMT28"     :   "268435456 (2^28) cycles",
    "DMT29"     :   "536870912 (2^29) cycles",
    "DMT30"     :   "1073741824 (2^30) cycles",
    "DMT31"     :   "2147483648 (2^31) cycles"
}

###################################################################################################
########################################## Callbacks ##############################################
###################################################################################################

def updateDMTUseProperties(symbol, event):

    symbol.setReadOnly((event["value"] == "ON"))
    symbol.setValue((event["value"] == "ON"), 1)

def updateDMTConfigCommentVisibleProperty(symbol, event):

    dmtHeaderFile.setEnabled(event["value"])
    dmtSourceFile.setEnabled(event["value"])
    dmtSystemDefFile.setEnabled(event["value"])

    symbol.setVisible(event["value"])

def updateDMTCountSelectVisibleProperty(symbol, event):

    if event["id"] == "DMT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(dmtCountSelectDictionary[event["value"]], 1)

def updateDMTCountIntervalVisibleProperty(symbol, event):

    if event["id"] == "DMT_USE":
        symbol.setVisible(event["value"])
    else:
        symbol.setValue(dmtInteravalValueDictionary[event["value"]], 1)

###################################################################################################
#############################################  DMT  ###############################################
###################################################################################################

isDMTEnabled = (Database.getSymbolValue("core", "CONFIG_FDMTEN") == "ON")
dmtCountSelect = Database.getSymbolValue("core", "CONFIG_DMTCNT")
dmtCountWindowInterval = Database.getSymbolValue("core", "CONFIG_DMTINTV")

dmtInstances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMT\"]")

dmtInstanceName = coreComponent.createStringSymbol("DMT_INSTANCE_NAME", None)
dmtInstanceName.setVisible(False)
dmtInstanceName.setDefaultValue(dmtInstances.getAttribute("name"))

#DMT menu
dmtMenu = coreComponent.createMenuSymbol("DMT_MENU", None)
dmtMenu.setLabel("DMT")

#DMT Use
dmtSym_Use = coreComponent.createBooleanSymbol("DMT_USE", dmtMenu)
dmtSym_Use.setLabel("Use DMT ?")
dmtSym_Use.setDefaultValue(isDMTEnabled)
dmtSym_Use.setReadOnly(isDMTEnabled)
dmtSym_Use.setDependencies(updateDMTUseProperties, ["CONFIG_FDMTEN"])

#DMT Configuration comment
dmtSym_ConfigComment = coreComponent.createCommentSymbol("DMT_CONFIG_COMMENT", dmtSym_Use)
dmtSym_ConfigComment.setLabel("************** Configure DMT From Device Configuration Fuses ***************")
dmtSym_ConfigComment.setVisible(isDMTEnabled)
dmtSym_ConfigComment.setDependencies(updateDMTConfigCommentVisibleProperty, ["DMT_USE"])

#DMT Count Select
dmtSym_CountSelect = coreComponent.createStringSymbol("DMT_COUNT_SELECT", dmtSym_Use)
dmtSym_CountSelect.setLabel("Configured DMT Count Value")
dmtSym_CountSelect.setDefaultValue(dmtCountSelectDictionary[dmtCountSelect])
dmtSym_CountSelect.setReadOnly(True)
dmtSym_CountSelect.setVisible(isDMTEnabled)
dmtSym_CountSelect.setDependencies(updateDMTCountSelectVisibleProperty, ["DMT_USE", "CONFIG_DMTCNT"])

#DMT Count Interval
dmtSym_CountInterval = coreComponent.createStringSymbol("DMT_COUNT_INTERVAL", dmtSym_Use)
dmtSym_CountInterval.setLabel("Configured DMT Window Interval Value")
dmtSym_CountInterval.setDefaultValue(dmtInteravalValueDictionary[dmtCountWindowInterval])
dmtSym_CountInterval.setReadOnly(True)
dmtSym_CountInterval.setVisible(isDMTEnabled)
dmtSym_CountInterval.setDependencies(updateDMTCountIntervalVisibleProperty, ["DMT_USE", "CONFIG_DMTINTV"])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

dmtHeaderFile = coreComponent.createFileSymbol("DMT_HEADER", None)
dmtHeaderFile.setSourcePath("../peripheral/dmt_01520/templates/plib_dmt.h.ftl")
dmtHeaderFile.setOutputName("plib_" + dmtInstanceName.getValue().lower() + ".h")
dmtHeaderFile.setDestPath("/peripheral/dmt/")
dmtHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmt/")
dmtHeaderFile.setType("HEADER")
dmtHeaderFile.setMarkup(True)
dmtHeaderFile.setEnabled(dmtSym_Use.getValue())

dmtSourceFile = coreComponent.createFileSymbol("DMT_SOURCE", None)
dmtSourceFile.setSourcePath("../peripheral/dmt_01520/templates/plib_dmt.c.ftl")
dmtSourceFile.setOutputName("plib_" + dmtInstanceName.getValue().lower() + ".c")
dmtSourceFile.setDestPath("/peripheral/dmt/")
dmtSourceFile.setProjectPath("config/" + configName + "/peripheral/dmt/")
dmtSourceFile.setType("SOURCE")
dmtSourceFile.setMarkup(True)
dmtSourceFile.setEnabled(dmtSym_Use.getValue())

dmtSystemDefFile = coreComponent.createFileSymbol("DMT_SYS_DEF", None)
dmtSystemDefFile.setType("STRING")
dmtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmtSystemDefFile.setSourcePath("../peripheral/dmt_01520/templates/system/definitions.h.ftl")
dmtSystemDefFile.setMarkup(True)
dmtSystemDefFile.setEnabled(dmtSym_Use.getValue())