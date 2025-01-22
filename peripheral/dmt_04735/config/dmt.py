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
#### ATDF Helper Functions  ####
################################################################################
global getSettingBitMaskValue
def getSettingBitMaskValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             bitMaskInHex= long(int(bitMask,16))
             return bitMaskInHex
     return 0

global getBitField
def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

global getDefaultVal
def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value 

global getSettingBitDefaultValue
def getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         regDefaultVal = registerNode.getAttribute("initval")
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return getDefaultVal(regDefaultVal,bitMask)
     return 0

################################################################################
#### Symbol Constants ####
################################################################################
global DMT
DMT = "DMT"

global DMT_MENU
DMT_MENU = "DMT_MENU"

global USE_DMT
USE_DMT = "useDmt"

global COUNTER
COUNTER = "counter"

global WIN_INTERVAL
WIN_INTERVAL = "windowInterval"

################################################################################
#### Callbacks ####
################################################################################
global setVisibleOnUseDmt, onUseDmtChanged
def setVisibleOnUseDmt(symbol, event):
    symbol.setVisible(event["value"])

def onUseDmtChanged(symbol, event):
    symbol.setEnabled(event["value"])
    symbol.setEnabled(event["value"])

def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
    # Path to the register node in the ATDF structure
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, register_group, register
    )
    # Retrieve the register node
    register_node = ATDF.getNode(reg_path)

    # If the register node is found, fetch and return the initval as hex; otherwise, return "0x0UL"
    if register_node is not None:
        reg_default_val = register_node.getAttribute("initval")
        return "{}UL".format(reg_default_val) if reg_default_val else "0x0UL"
    return "0x0UL"

################## Symbol Creation for DMT Component ###########################
# DMT Configuration
dmtMenu = coreComponent.createMenuSymbol(DMT_MENU, None)
dmtMenu.setLabel("DMT")

# DMT Enable 
useDmt = coreComponent.createBooleanSymbol(USE_DMT, dmtMenu)
useDmt.setLabel("Use DMT")
useDmt.setVisible(True)
useDmt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmt_04735;register:DMTCON")

# DMT Counter
dmtCounter = coreComponent.createHexSymbol(COUNTER, useDmt)
dmtCounter.setLabel("Counter Value")
dmtCounter.setDefaultValue(getSettingBitDefaultValue(DMT,"PSCNT","PSCNT","PSCNT"))   
dmtCounter.setMin(0x0)
dmtCounter.setMax(getSettingBitMaskValue(DMT,"PSCNT","PSCNT","PSCNT"))
dmtCounter.setVisible(False)
dmtCounter.setDependencies(setVisibleOnUseDmt, [USE_DMT])
dmtCounter.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmt_04735;register:PSCNT")

# DMT Window Interval
dmtWindowInterval = coreComponent.createHexSymbol(WIN_INTERVAL, useDmt)
dmtWindowInterval.setLabel("Window Interval Value")
dmtWindowInterval.setDefaultValue(getSettingBitDefaultValue(DMT,"PSINTV","PSINTV","PSINTV"))   
dmtWindowInterval.setMin(0x0)
dmtWindowInterval.setMax(getSettingBitMaskValue(DMT,"PSINTV","PSINTV","PSINTV")) 
dmtWindowInterval.setVisible(False)
dmtWindowInterval.setDependencies(setVisibleOnUseDmt, [USE_DMT])
dmtWindowInterval.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dmt_04735;register:PSINTV")

##################### Code Generation ####################################
dmtInstances = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"DMT\"]")

dmtInstanceName = coreComponent.createStringSymbol("DMT_INSTANCE_NAME", None)
dmtInstanceName.setVisible(False)
dmtInstanceName.setDefaultValue(dmtInstances.getAttribute("name"))

pscntRegPor = coreComponent.createStringSymbol("PSCNT_REG_POR", None)
pscntRegPor.setDefaultValue(getRegisterDefaultValue("DMT", "PSCNT", "PSINTV"))
pscntRegPor.setVisible(False)

psintvRegPor = coreComponent.createStringSymbol("PSINTV_REG_POR", None)
psintvRegPor.setDefaultValue(getRegisterDefaultValue("DMT", "PSCNT", "PSINTV"))
psintvRegPor.setVisible(False)

configName = Variables.get("__CONFIGURATION_NAME")

dmtHeaderFile = coreComponent.createFileSymbol("DMT_HEADER", None)
dmtHeaderFile.setSourcePath("../peripheral/dmt_04735/templates/plib_dmt.h.ftl")
dmtHeaderFile.setOutputName("plib_dmt.h")
dmtHeaderFile.setDestPath("/peripheral/dmt/")
dmtHeaderFile.setProjectPath("config/" + configName +"/peripheral/dmt/")
dmtHeaderFile.setType("HEADER")
dmtHeaderFile.setMarkup(True)
dmtHeaderFile.setEnabled(False)
dmtHeaderFile.setDependencies(onUseDmtChanged, [USE_DMT])

dmtSourceFile = coreComponent.createFileSymbol("DMT_SOURCE", None)
dmtSourceFile.setSourcePath("../peripheral/dmt_04735/templates/plib_dmt.c.ftl")
dmtSourceFile.setOutputName("plib_dmt.c")
dmtSourceFile.setDestPath("/peripheral/dmt/")
dmtSourceFile.setProjectPath("config/" + configName +"/peripheral/dmt/")
dmtSourceFile.setType("SOURCE")
dmtSourceFile.setMarkup(True)
dmtSourceFile.setEnabled(False)
dmtSourceFile.setDependencies(onUseDmtChanged, [USE_DMT])

dmtSystemInitFile = coreComponent.createFileSymbol("DMT_INIT", None)
dmtSystemInitFile.setType("STRING")
dmtSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmtSystemInitFile.setSourcePath("../peripheral/dmt_04735/templates/system/initialization.c.ftl")
dmtSystemInitFile.setMarkup(True)
dmtSystemInitFile.setEnabled(False)
dmtSystemInitFile.setDependencies(onUseDmtChanged, [USE_DMT])

dmtSystemDefFile = coreComponent.createFileSymbol("DMT_SYS_DEF", None)
dmtSystemDefFile.setType("STRING")
dmtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmtSystemDefFile.setSourcePath("../peripheral/dmt_04735/templates/system/definitions.h.ftl")
dmtSystemDefFile.setMarkup(True)
dmtSystemDefFile.setEnabled(False)
dmtSystemDefFile.setDependencies(onUseDmtChanged, [USE_DMT])