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

global eepromInstanceName
global getWaitStates

def getWaitStates():

    sysclk = int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_FREQ"))
    ws = 7

    if sysclk >= 100000000 and sysclk <= 120000000:
        ws = 12
    if sysclk >=  75000000 and sysclk <  100000000:
        ws = 9
    if sysclk >=  50000000 and sysclk <   75000000:
        ws = 7
    if sysclk >=  25000000 and sysclk <   50000000:
        ws = 4
    if sysclk <   25000000:
        ws = 2

    return ws

def calcWaitStates(symbol, event):

    symbol.setValue(getWaitStates(), 2)

def updateEEPROMClockWarningStatus(symbol, event):
    symbol.setVisible(not event["value"])

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(eepromComponent):
    global eepromInstanceName

    eepromInstanceName = eepromComponent.createStringSymbol("EEPROM_INSTANCE_NAME", None)
    eepromInstanceName.setVisible(False)
    eepromInstanceName.setDefaultValue(eepromComponent.getID().upper())

    Log.writeInfoMessage("Running " + eepromInstanceName.getValue())

    #Clock enable
    Database.setSymbolValue("core", eepromInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    #EEPROM Configuration Menu
    eepromMenu = eepromComponent.createMenuSymbol("EEPROM_MENU", None)
    eepromMenu.setLabel("EEPROM Memory Configuration")
    eepromMenu.setDescription("EEPROM Memory Configuration")

    eepromCFGCON_EEWS = eepromComponent.createIntegerSymbol("EEPROM_CFGCON_EEWS", eepromMenu)
    eepromCFGCON_EEWS.setLabel("EEPROM Memory Wait states")
    eepromCFGCON_EEWS.setDescription("Number of Wait states configured.")
    eepromCFGCON_EEWS.setDefaultValue(getWaitStates())
    eepromCFGCON_EEWS.setReadOnly(True)
    eepromCFGCON_EEWS.setDependencies(calcWaitStates, ["core.CONFIG_SYS_CLK_PBCLK2_FREQ"])

    # Clock Warning status
    eepromSym_ClkEnComment = eepromComponent.createCommentSymbol("EPPROM_CLOCK_ENABLE_COMMENT", None)
    eepromSym_ClkEnComment.setLabel("Warning!!! " + eepromInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    eepromSym_ClkEnComment.setVisible(False)
    eepromSym_ClkEnComment.setDependencies(updateEEPROMClockWarningStatus, ["core." + eepromInstanceName.getValue() + "_CLOCK_ENABLE"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    # Enable Peripheral Clock in Clock manager
    Database.clearSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_ENABLE")
    Database.setSymbolValue("core", "CONFIG_SYS_CLK_PBCLK2_ENABLE", True, 2)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    eepromSym_HeaderFile = eepromComponent.createFileSymbol("EEPROM_HEADER", None)
    eepromSym_HeaderFile.setSourcePath("../peripheral/eeprom_02514/templates/plib_eeprom.h.ftl")
    eepromSym_HeaderFile.setOutputName("plib_"+eepromInstanceName.getValue().lower()+".h")
    eepromSym_HeaderFile.setDestPath("/peripheral/eeprom/")
    eepromSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/eeprom/")
    eepromSym_HeaderFile.setType("HEADER")
    eepromSym_HeaderFile.setMarkup(True)

    eepromSym_SourceFile = eepromComponent.createFileSymbol("EEPROM_SOURCE", None)
    eepromSym_SourceFile.setSourcePath("../peripheral/eeprom_02514/templates/plib_eeprom.c.ftl")
    eepromSym_SourceFile.setOutputName("plib_"+eepromInstanceName.getValue().lower()+".c")
    eepromSym_SourceFile.setDestPath("/peripheral/eeprom/")
    eepromSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/eeprom/")
    eepromSym_SourceFile.setType("SOURCE")
    eepromSym_SourceFile.setMarkup(True)

    eepromSystemInitFile = eepromComponent.createFileSymbol("EEPROM_INIT", None)
    eepromSystemInitFile.setSourcePath("../peripheral/eeprom_02514/templates/system/initialization.c.ftl")
    eepromSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    eepromSystemInitFile.setType("STRING")
    eepromSystemInitFile.setMarkup(True)

    eepromSystemDefFile = eepromComponent.createFileSymbol("EEPROM_DEF", None)
    eepromSystemDefFile.setSourcePath("../peripheral/eeprom_02514/templates/system/definitions.h.ftl")
    eepromSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    eepromSystemDefFile.setType("STRING")
    eepromSystemDefFile.setMarkup(True)
