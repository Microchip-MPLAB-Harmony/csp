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

import re
#********************** Static Memory Controller Module ***********************

#------------------------------------------------------------------------------
# Constants
DEFAULT_SMC_MIN_VALUE =                 0
DEFAULT_SMC_SETUP_VALUE =               2
DEFAULT_SMC_PULSE_VALUE =               7
DEFAULT_SMC_CYCLE_VALUE =               13
DEFAULT_SMC_MODE_TDF_CYCLES_VALUE =     1

#-- SMC ------------------------------------------------------------------------
ModuleSmc =                             '/avr-tools-device-file/modules/module@[name="SMC"]'
#
SmcCsNumberGroupDef =                   ModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]'
SmcRegisterGroupDef =                   ModuleSmc + '/register-group@[name="SMC"]'
#
SmcCsSetupRegister =                    SmcCsNumberGroupDef + '/register@[name="SMC_SETUP"]'
SmcCsPulseRegister =                    SmcCsNumberGroupDef + '/register@[name="SMC_PULSE"]'
SmcCsCycleRegister =                    SmcCsNumberGroupDef + '/register@[name="SMC_CYCLE"]'
SmcCsModeRegister =                     SmcCsNumberGroupDef + '/register@[name="SMC_MODE"]'
#
SmcOcmsRegister =                       SmcRegisterGroupDef + '/register@[name="SMC_OCMS"]'
SmcSrierRegister =                      SmcRegisterGroupDef + '/register@[name="SMC_SRIER"]'

#-- PMECC ---------------------------------------------------------------------------
ModulePmecc =                           '/avr-tools-device-file/modules/module@[name="PMECC"]'
#
PmeccPmeccGroupDef =                    ModulePmecc + '/register-group@[name="PMECC"]'
#
PmeccCfgRegister =                      PmeccPmeccGroupDef + '/register@[name="PMECC_CFG"]'
PmeccSareaRegister =                    PmeccPmeccGroupDef + '/register@[name="PMECC_SAREA"]'
PmeccSaddrRegister =                    PmeccPmeccGroupDef + '/register@[name="PMECC_SADDR"]'
PmeccEaddrRegister =                    PmeccPmeccGroupDef + '/register@[name="PMECC_EADDR"]'
PmeccClkRegister =                      PmeccPmeccGroupDef + '/register@[name="PMECC_CLK"]'
PmeccCtrlRegister =                     PmeccPmeccGroupDef + '/register@[name="PMECC_CTRL"]'
PmeccIerRegister =                      PmeccPmeccGroupDef + '/register@[name="PMECC_IER"]'

#-- PMERRLOC -------------------------------------------------------------------
ModulePmerrloc =                        '/avr-tools-device-file/modules/module@[name="PMERRLOC"]'
#
PmerrlocGroupDef =                      ModulePmerrloc + '/register-group@[name="PMERRLOC"]'
#
PmerrlocElcfgRegister =                 PmerrlocGroupDef + '/register@[name="PMERRLOC_ELCFG"]'
PmerrlocElierRegister =                 PmerrlocGroupDef + '/register@[name="PMERRLOC_ELIER"]'

#------------------------------------------------------------------------------
# SMC ATDF Global Variables
atdfModuleSmcOcmsRegister =             ATDF.getNode( SmcOcmsRegister )
atdfModuleSmcCsNumberGroup =            ATDF.getNode( SmcRegisterGroupDef + '/register-group@[name="SMC_CS_NUMBER"]' )
#
atdfSmcSrierBitField_SRIE =             ATDF.getNode( SmcSrierRegister + '/bitfield@[name="SRIE"]' )
#
atdfSmcOcmsBitField_TAMPCLR =           ATDF.getNode( SmcOcmsRegister + '/bitfield@[name="TAMPCLR"]' )
# Setup bit fields
atdfSmcCsSetupBitField_NWE_SETUP =      ATDF.getNode( SmcCsSetupRegister + '/bitfield@[name="NWE_SETUP"]' )
atdfSmcCsSetupBitField_NCS_WR_SETUP =   ATDF.getNode( SmcCsSetupRegister + '/bitfield@[name="NCS_WR_SETUP"]' )
atdfSmcCsSetupBitField_NRD_SETUP =      ATDF.getNode( SmcCsSetupRegister + '/bitfield@[name="NRD_SETUP"]' )
atdfSmcCsSetupBitField_NCS_RD_SETUP =   ATDF.getNode( SmcCsSetupRegister + '/bitfield@[name="NCS_RD_SETUP"]' )
# Pulse bit fields
atdfSmcCsPulseBitField_NWE_PULSE =      ATDF.getNode( SmcCsPulseRegister + '/bitfield@[name="NWE_PULSE"]' )
atdfSmcCsPulseBitField_NCS_WR_PULSE =   ATDF.getNode( SmcCsPulseRegister + '/bitfield@[name="NCS_WR_PULSE"]' )
atdfSmcCsPulseBitField_NRD_PULSE =      ATDF.getNode( SmcCsPulseRegister + '/bitfield@[name="NRD_PULSE"]' )
atdfSmcCsPulseBitField_NCS_RD_PULSE =   ATDF.getNode( SmcCsPulseRegister + '/bitfield@[name="NCS_RD_PULSE"]' )
# Cycle bit fields
atdfSmcCsCycleBitField_NWE_CYCLE =      ATDF.getNode( SmcCsCycleRegister + '/bitfield@[name="NWE_CYCLE"]' )
atdfSmcCsCycleBitField_NRD_CYCLE =      ATDF.getNode( SmcCsCycleRegister + '/bitfield@[name="NRD_CYCLE"]' )
# Mode bit fields
atdfSmcCsModeBitField_MODE_PS =         ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="PS"]' )
atdfSmcCsModeBitField_MODE_TDF_CYCLES = ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="TDF_CYCLES"]' )
atdfSmcCsModeBitField_MODE_DBW =        ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="DBW"]' )
atdfSmcCsModeBitField_MODE_BAT =        ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="BAT"]' )
atdfSmcCsModeBitField_MODE_EXNW_MODE =  ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="EXNW_MODE"]' )
atdfSmcCsModeBitField_MODE_READ_MODE =  ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="READ_MODE"]' )
atdfSmcCsModeBitField_MODE_WRITE_MODE = ATDF.getNode( SmcCsModeRegister + '/bitfield@[name="WRITE_MODE"]' )
#------------------------------------------------------------------------------
# PMECCC ATDF Global Variables
# PMECC_CFG Register bit fields
atdfPmeccCfgBitField_BCH_ERR =          ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="BCH_ERR"]' )
atdfPmeccCfgBitField_SECTORSZ =         ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="SECTORSZ"]' )
atdfPmeccCfgBitField_PAGESIZE =         ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="PAGESIZE"]' )
atdfPmeccCfgBitField_NANDWR =           ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="NANDWR"]' )
atdfPmeccCfgBitField_SPAREEN =          ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="SPAREEN"]' )
atdfPmeccCfgBitField_AUTO =             ATDF.getNode( PmeccCfgRegister + '/bitfield@[name="AUTO"]' )
# PMECC_SAREA Register bit fields
atdfPmeccSareaBitField_SPARESIZE =      ATDF.getNode( PmeccSareaRegister + '/bitfield@[name="SPARESIZE"]' )
# PMECC_SADDR Register bit fields
atdfPmeccSaddrBitField_STARTADDR =      ATDF.getNode( PmeccSaddrRegister + '/bitfield@[name="STARTADDR"]' )
# PMECC_EADDR Register bit fields
atdfPmeccEaddrBitField_ENDADDR =        ATDF.getNode( PmeccEaddrRegister + '/bitfield@[name="ENDADDR"]' )
# PMECC_CLK Register bit fields
atdfPmeccClkBitField_CLKCTRL =          ATDF.getNode( PmeccClkRegister + '/bitfield@[name="CLKCTRL"]' )
# PMECC_CTRL Register bit fields
atdfPmeccCtrlBitField_ENABLE =          ATDF.getNode( PmeccCtrlRegister + '/bitfield@[name="ENABLE"]' )
# PMECC_IER Register bit fields
atdfPmeccIerBitField_ERRIE =            ATDF.getNode( PmeccIerRegister + '/bitfield@[name="ERRIE"]' )
#------------------------------------------------------------------------------
# PMERRLOC ATDF Global Variables
# PMERRLOC_ELCFG Register bit fields
atdfPmerrlocElcfgBitField_SECTORSZ =    ATDF.getNode( PmerrlocElcfgRegister + '/bitfield@[name="SECTORSZ"]' )
# PMERRLOC_ELIER Register bit fields
atdfPmerrlocElierBitField_DONE =        ATDF.getNode( PmerrlocElierRegister + '/bitfield@[name="DONE"]' )


#------------------------------------------------------------------------------
# Dependency Functions
#------------------------------------------------------------------------------

def handleMessage(messageID, args):
    global pmeccCtrlEnable
    result_dict = {}

    component = pmeccCtrlEnable.getComponent()

    if ("SMC_CS_ENABLE_" in messageID):
        if args.get("isReadOnly") != None:
            component.getSymbolByID(messageID).setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            component.getSymbolByID(messageID).setValue(args["isEnabled"])
    elif (messageID == "PMECC_CTRL_ENABLE"):
        if args.get("isReadOnly") != None:
            component.getSymbolByID("PMECC_CTRL_ENABLE").setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            component.getSymbolByID("PMECC_CTRL_ENABLE").setValue(args["isEnabled"])
    elif (messageID == "PMECC_IER_ERRIE"):
        if args.get("isReadOnly") != None:
            component.getSymbolByID("PMECC_IER_ERRIE").setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            component.getSymbolByID("PMECC_IER_ERRIE").setValue(args["isEnabled"])
    elif (messageID == "PMERRLOC_ELIER_DONE"):
        if args.get("isReadOnly") != None:
            component.getSymbolByID("PMERRLOC_ELIER_DONE").setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            component.getSymbolByID("PMERRLOC_ELIER_DONE").setValue(args["isEnabled"])

    return result_dict

def getNameValueCaptionTuple( aModule, aGroupName ):
    choiceNode = ATDF.getNode( aModule + '/value-group@[name="' + aGroupName + '"]' )
    tupleArray = []
    if not choiceNode:
        choiceValues = []
    else:
        choiceValues = choiceNode.getChildren()

    for ii in range( 0, len( choiceValues ) ):
        tupleArray.append( ( choiceValues[ ii ].getAttribute( "name" ),
                             choiceValues[ ii ].getAttribute( "value" ),
                             choiceValues[ ii ].getAttribute( "caption" )
                             ) )
    return tupleArray


def patternMatchCount( anAtdfNode, anAttribute, aPattern ):
    matchCount = 0
    children = anAtdfNode.getChildren()
    for ii in range( 0, len( children ) ):
        childAttribute = children[ ii ].getAttribute( anAttribute )
        if childAttribute:
            if bool( re.search( aPattern, childAttribute ) ):
                matchCount += 1

    return matchCount


def convertMaskToInt( aRegMask ):
    """ function to convert bit field mask string to integer -- assumes mask is contiguous bits"""
    numBits = 0;
    aBinStr = '{0:32b}'.format(int( aRegMask, 16 )).strip().rstrip( "0" )
    while len( aBinStr ):
        aBinCh = aBinStr[-1]
        aBinStr = aBinStr[0:-1]
        if aBinCh == '1':
            numBits += 1
        else:
            break
    return ((2**numBits) - 1)       # return max value field can contain


def updateInterrupt( symbol, event ):
    interruptName = event[ "id" ]
    idx = interruptName.find( "_" )
    if( idx >= 0 ):
        interruptName = interruptName[ 0 : idx ]

    Database.clearSymbolValue( "core", interruptName + "_INTERRUPT_ENABLE" )
    Database.clearSymbolValue( "core", interruptName + "_INTERRUPT_HANDLER" )
    Database.clearSymbolValue( "core", interruptName + "_INTERRUPT_HANDLER_LOCK" )
    if event[ 'value' ] == True:
        Database.setSymbolValue( "core", interruptName + "_INTERRUPT_ENABLE", True )
        Database.setSymbolValue( "core", interruptName + "_INTERRUPT_HANDLER", interruptName + "_InterruptHandler" )
        Database.setSymbolValue( "core", interruptName + "_INTERRUPT_HANDLER_LOCK", True )


def visibilityBasedOnBoolSymbol( symbol, event ):
    symbol.setVisible( event[ "value" ] )


def smcModeByteWriteOrSelectAccessVisible( symbol, event ):
    """ function to enable visibility based on selection of Byte Access Type """
    if( event[ "symbol" ].getSelectedKey() == "SMC_MODE_DBW_BIT_16" ):
        symbol.setVisible( True )
    else:
        symbol.setVisible( False )


def pmerrlocCfgSectorSize( symbol, event ):
    Database.clearSymbolValue( "smc", symbol.getID() )
    if( event["value"] != symbol.getDefaultValue() ):
        symbol.setValue( event["value"], 1 )

def updateSymbolValue( symbol, event ):
    symbol.setValue( not event[ "value" ] )

def instantiateComponent( staticMemoryComponent ):
    global pmeccCtrlEnable

    myNamespace = str( staticMemoryComponent.getID() ).upper()

    smcInstanceName = staticMemoryComponent.createStringSymbol( "SMC_INSTANCE_NAME", None )
    smcInstanceName.setVisible( False )
    smcInstanceName.setDefaultValue( myNamespace )

    pmeccInstanceName = staticMemoryComponent.createStringSymbol( "PMECC_INSTANCE_NAME", None )
    pmeccInstanceName.setVisible( False )
    pmeccInstanceName.setDefaultValue( "PMECC" )

    pmeccLocInstanceName = staticMemoryComponent.createStringSymbol( "PMERRLOC_INSTANCE_NAME", None )
    pmeccLocInstanceName.setVisible( False )
    pmeccLocInstanceName.setDefaultValue( "PMERRLOC" )

    #--------------------------------------------------------------------------
    # Peripheral clock enable in Clock Manager
    Database.clearSymbolValue( "core", myNamespace + "_CLOCK_ENABLE" )
    Database.setSymbolValue(   "core", myNamespace + "_CLOCK_ENABLE", True, 2 )

    #--------------------------------------------------------------------------
    # Top level Menus
    smcControlsMenu = staticMemoryComponent.createMenuSymbol( "SMC_CONTROLS_MENU", None )
    smcControlsMenu.setLabel( "SMC Controls" )

    pmeccCtrlEnableNameStem = "PMECC_CTRL_ENABLE"
    pmeccCtrlEnableName = pmeccCtrlEnableNameStem
    pmeccCtrlEnable = staticMemoryComponent.createBooleanSymbol( pmeccCtrlEnableName, None )
    pmeccCtrlEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CTRL")
    pmeccCtrlEnable.setLabel( atdfPmeccCtrlBitField_ENABLE.getAttribute( "caption" ) )

    pmeccControlsMenu = staticMemoryComponent.createMenuSymbol( "PMECC_CONTROLS_MENU", pmeccCtrlEnable )
    pmeccControlsMenu.setLabel( "PMECC Controls" )
    pmeccControlsMenu.setDependencies( visibilityBasedOnBoolSymbol, [ pmeccCtrlEnableName ] )
    pmeccControlsMenu.setVisible( False )

    pmerrlocControlsMenu = staticMemoryComponent.createMenuSymbol( "PMERRLOC_CONTROLS_MENU", pmeccCtrlEnable )
    pmerrlocControlsMenu.setLabel( "PMERR Controls" )
    pmerrlocControlsMenu.setDependencies( visibilityBasedOnBoolSymbol, [ pmeccCtrlEnableName ] )
    pmerrlocControlsMenu.setVisible( False )

    #--------------------------------------------------------------------------
    # SMC Global
    smcGlobalMenu = staticMemoryComponent.createMenuSymbol( "SMC_GLOBAL_MENU", smcControlsMenu )
    smcGlobalMenu.setLabel( "Global" )

    smcSrierSrieName = "SMC_SRIER_SRIE"
    smcSrierSrie = staticMemoryComponent.createBooleanSymbol( smcSrierSrieName, smcGlobalMenu )
    smcSrierSrie.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SRIER")
    smcSrierSrie.setLabel( atdfSmcSrierBitField_SRIE.getAttribute( "caption" ) )
    smcSrierSrie.setDefaultValue( False )
    smcSrierSrie.setDependencies( updateInterrupt, [ smcSrierSrieName ] )

    smcWpmrWpen = staticMemoryComponent.createBooleanSymbol( "SMC_WPMR_WPEN", smcGlobalMenu )
    smcWpmrWpen.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_WPMR")
    smcWpmrWpen.setLabel( "Enable Write Protection" )
    smcWpmrWpen.setDefaultValue( False )

    smcOcmsTampclr = staticMemoryComponent.createBooleanSymbol( "SMC_OCMS_TAMPCLR", smcGlobalMenu )
    smcOcmsTampclr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_OCMS")
    smcOcmsTampclr.setLabel( atdfSmcOcmsBitField_TAMPCLR.getAttribute( "caption" ) )
    smcOcmsTampclr.setDefaultValue( False )

    smcKeyMenu = staticMemoryComponent.createMenuSymbol( "SMC_KEY_MENU", smcGlobalMenu )
    smcKeyMenu.setLabel( "Scrambling Keys" )

    smcSmcKey1 = staticMemoryComponent.createHexSymbol( "SMC_KEY1", smcKeyMenu )
    smcSmcKey1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_KEY1")
    smcSmcKey1.setLabel( "Key 1" )

    smcSmcKey2 = staticMemoryComponent.createHexSymbol( "SMC_KEY2", smcKeyMenu )
    smcSmcKey2.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_KEY2")
    smcSmcKey2.setLabel( "Key 2" )
    #----
    # SMC Chip Select Selection and Settings
    chipSelectionAndSettingsMenu = staticMemoryComponent.createMenuSymbol( "SMC_CHIP_SELECTION_AND_SETTINGS_MENU", smcControlsMenu )
    chipSelectionAndSettingsMenu.setLabel( "Chip Selection and Settings" )

    atdfSmcOcmsEnablesCount = patternMatchCount( atdfModuleSmcOcmsRegister, "name", "CS[0-9]+SE" )
    smcOcmsEnablesCount = staticMemoryComponent.createIntegerSymbol( "SMC_OCMS_CSxSE_COUNT", chipSelectionAndSettingsMenu )
    smcOcmsEnablesCount.setDefaultValue( atdfSmcOcmsEnablesCount )
    smcOcmsEnablesCount.setVisible( False )

    atdfSmcCsCount = int( atdfModuleSmcCsNumberGroup.getAttribute( "count" ) )
    smcCsCount = staticMemoryComponent.createIntegerSymbol( "SMC_CS_COUNT", chipSelectionAndSettingsMenu )
    smcCsCount.setDefaultValue( atdfSmcCsCount )
    smcCsCount.setVisible( False )

    nandCsNum = 3
    nandAddr = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"EBI_NF\"]").getAttribute("start")
    addressSpaces = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space").getChildren()
    for index in range(len(addressSpaces)):
        if ("EBI_CS" in addressSpaces[index].getAttribute("name")) and (addressSpaces[index].getAttribute("start") == nandAddr):
            nandCsNum = addressSpaces[index].getAttribute("name").split("EBI_CS")[1]
            break
    smcNandCsNum = staticMemoryComponent.createIntegerSymbol("SMC_NAND_CS_NUM", chipSelectionAndSettingsMenu)
    smcNandCsNum.setDefaultValue(int(nandCsNum))
    smcNandCsNum.setVisible(False)

    for csNumIndex in range( 0, atdfSmcCsCount ):
        csNum = str( csNumIndex )
        smcCsEnable = staticMemoryComponent.createBooleanSymbol( "SMC_CS_ENABLE_" + csNum, chipSelectionAndSettingsMenu )
        smcCsEnable.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SETUP")
        smcCsEnable.setLabel( "Enable Chip Select " + csNum )

        if atdfSmcOcmsEnablesCount > csNumIndex:
            smcOcmsCsse = staticMemoryComponent.createBooleanSymbol( "SMC_OCMS_CS" + csNum + "SE", smcCsEnable )
            smcOcmsCsse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CTRL")
            smcOcmsCsse.setLabel( "Enable Off Chip Memory Scrambling" )
            smcOcmsCsse.setDefaultValue( False )

        # Read Setup, Pulse and Cycle Timings
        smcReadCycleTimingMenu = staticMemoryComponent.createMenuSymbol( "SMC_READ_CYCLE_TIMING_MENU_" + csNum, smcCsEnable )
        smcReadCycleTimingMenu.setLabel( "Read Cycle Timing" )

        # Read Setup Timings
        smcNrdSetup = staticMemoryComponent.createIntegerSymbol( "SMC_NRD_SETUP_" + csNum, smcReadCycleTimingMenu )
        smcNrdSetup.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SETUP")
        smcNrdSetup.setLabel( atdfSmcCsSetupBitField_NRD_SETUP.getAttribute( "caption" ) )
        smcNrdSetup.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNrdSetup.setMax( convertMaskToInt( atdfSmcCsSetupBitField_NRD_SETUP.getAttribute( "mask" ) ) )
        smcNrdSetup.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        smcNcsRdSetup = staticMemoryComponent.createIntegerSymbol( "SMC_NCS_RD_SETUP_" + csNum, smcReadCycleTimingMenu )
        smcNcsRdSetup.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SETUP")
        smcNcsRdSetup.setLabel( atdfSmcCsSetupBitField_NCS_RD_SETUP.getAttribute( "caption" ) )
        smcNcsRdSetup.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNcsRdSetup.setMax( convertMaskToInt( atdfSmcCsSetupBitField_NCS_RD_SETUP.getAttribute( "mask" ) ) )
        smcNcsRdSetup.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        # Read Pulse Timings
        smcNrdPulse = staticMemoryComponent.createIntegerSymbol( "SMC_NRD_PULSE_" + csNum, smcReadCycleTimingMenu )
        smcNrdPulse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_PULSE")
        smcNrdPulse.setLabel( atdfSmcCsPulseBitField_NRD_PULSE.getAttribute( "caption" ) )
        smcNrdPulse.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNrdPulse.setMax( convertMaskToInt( atdfSmcCsPulseBitField_NRD_PULSE.getAttribute( "mask" ) ) )
        smcNrdPulse.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        smcNcsRdPulse = staticMemoryComponent.createIntegerSymbol( "SMC_NCS_RD_PULSE_" + csNum, smcReadCycleTimingMenu )
        smcNcsRdPulse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_PULSE")
        smcNcsRdPulse.setLabel( atdfSmcCsPulseBitField_NCS_RD_PULSE.getAttribute( "caption" ) )
        smcNcsRdPulse.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNcsRdPulse.setMax( convertMaskToInt( atdfSmcCsPulseBitField_NCS_RD_PULSE.getAttribute( "mask" ) ) )
        smcNcsRdPulse.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        # Read Cycle Timings
        smcNrdCycle = staticMemoryComponent.createIntegerSymbol( "SMC_NRD_CYCLE_" + csNum, smcReadCycleTimingMenu )
        smcNrdCycle.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_CYCLE")
        smcNrdCycle.setLabel( atdfSmcCsCycleBitField_NRD_CYCLE.getAttribute( "caption" ) )
        smcNrdCycle.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNrdCycle.setMax( convertMaskToInt( atdfSmcCsCycleBitField_NRD_CYCLE.getAttribute( "mask" ) ) )
        smcNrdCycle.setDefaultValue( DEFAULT_SMC_CYCLE_VALUE )

        # Write Setup, Pulse and Cycle Timings
        smcWriteCycleTimingMenu = staticMemoryComponent.createMenuSymbol( "SMC_WRITE_CYCLE_TIMING_MENU_" + csNum, smcCsEnable )
        smcWriteCycleTimingMenu.setLabel( "Write Cycle Timing" )

        # Write Setup Timings
        smcNweSetup = staticMemoryComponent.createIntegerSymbol( "SMC_NWE_SETUP_" + csNum, smcWriteCycleTimingMenu )
        smcNweSetup.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SETUP")
        smcNweSetup.setLabel( atdfSmcCsSetupBitField_NWE_SETUP.getAttribute( "caption" ) )
        smcNweSetup.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNweSetup.setMax( convertMaskToInt( atdfSmcCsSetupBitField_NWE_SETUP.getAttribute( "mask" ) ) )
        smcNweSetup.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        smcNcsWrSetup = staticMemoryComponent.createIntegerSymbol( "SMC_NCS_WR_SETUP_" + csNum, smcWriteCycleTimingMenu )
        smcNcsWrSetup.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_SETUP")
        smcNcsWrSetup.setLabel( atdfSmcCsSetupBitField_NCS_WR_SETUP.getAttribute( "caption" ) )
        smcNcsWrSetup.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNcsWrSetup.setMax( convertMaskToInt( atdfSmcCsSetupBitField_NCS_WR_SETUP.getAttribute( "mask" ) ) )
        smcNcsWrSetup.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        # Write Pulse Timings
        smcNwePulse = staticMemoryComponent.createIntegerSymbol( "SMC_NWE_PULSE_" + csNum, smcWriteCycleTimingMenu )
        smcNwePulse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_PULSE")
        smcNwePulse.setLabel( atdfSmcCsPulseBitField_NWE_PULSE.getAttribute( "caption" ) )
        smcNwePulse.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNwePulse.setMax( convertMaskToInt( atdfSmcCsPulseBitField_NWE_PULSE.getAttribute( "mask" ) ) )
        smcNwePulse.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        smcNcsWrPulse = staticMemoryComponent.createIntegerSymbol( "SMC_NCS_WR_PULSE_" + csNum, smcWriteCycleTimingMenu )
        smcNcsWrPulse.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_PULSE")
        smcNcsWrPulse.setLabel( atdfSmcCsPulseBitField_NCS_WR_PULSE.getAttribute( "caption" ) )
        smcNcsWrPulse.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNcsWrPulse.setMax( convertMaskToInt( atdfSmcCsPulseBitField_NCS_WR_PULSE.getAttribute( "mask" ) ) )
        smcNcsWrPulse.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        # Write Cycle Timings
        smcNweCycle = staticMemoryComponent.createIntegerSymbol( "SMC_NWE_CYCLE_" + csNum, smcWriteCycleTimingMenu )
        smcNweCycle.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_CYCLE")
        smcNweCycle.setLabel( atdfSmcCsCycleBitField_NWE_CYCLE.getAttribute( "caption" ) )
        smcNweCycle.setMin( DEFAULT_SMC_MIN_VALUE )
        smcNweCycle.setMax( convertMaskToInt( atdfSmcCsCycleBitField_NWE_CYCLE.getAttribute( "mask" ) ) )
        smcNweCycle.setDefaultValue( DEFAULT_SMC_CYCLE_VALUE )

        # Mode Settings
        smcModeSettingsMenu = staticMemoryComponent.createMenuSymbol( "SMC_MODE_SETTINGS_MENU_" + csNum, smcCsEnable )
        smcModeSettingsMenu.setLabel( "Mode Settings" )

        smcModeDbwNameStem = "SMC_MODE_DBW"
        smcModeDbwName = smcModeDbwNameStem + "_" + csNum
        smcModeDbw = staticMemoryComponent.createKeyValueSetSymbol( smcModeDbwName, smcModeSettingsMenu )
        smcModeDbw.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeDbw.setLabel( atdfSmcCsModeBitField_MODE_DBW.getAttribute( "caption" ) )
        smcModeDbw.setOutputMode( "Key" )
        smcModeDbw.setDisplayMode( "Description" )
        smcModeDbw.setDefaultValue( 0 )
        smcModeValGroupPrefix = "SMC_MODE0"
        if ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/value-group@[name="SMC_MODE0__DBW"]') == None:
            smcModeValGroupPrefix = "SMC_MODE"
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__DBW" ):
            smcModeDbw.addKey( smcModeDbwNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

        smcModeBatNameStem = "SMC_MODE_BAT"
        smcModeBatName = smcModeBatNameStem + "_" + csNum
        smcModeBat = staticMemoryComponent.createKeyValueSetSymbol( smcModeBatName, smcModeSettingsMenu )
        smcModeBat.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeBat.setLabel( atdfSmcCsModeBitField_MODE_BAT.getAttribute( "caption" ) )
        smcModeBat.setOutputMode( "Key" )
        smcModeBat.setDisplayMode( "Description" )
        smcModeBat.setDefaultValue( 0 )
        # using name twice, not caption -- the atdf caption is too long; a couple of sentences
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__BAT" ):
            smcModeBat.addKey( smcModeBatNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 0 ] )
        smcModeBat.setDependencies( smcModeByteWriteOrSelectAccessVisible, [ smcModeDbwName ] )
        smcModeBat.setVisible( False )

        smcModePmenNameStem = "SMC_MODE_PMEN"
        smcModePmenName = smcModePmenNameStem + "_" + csNum
        smcModePmen = staticMemoryComponent.createBooleanSymbol( smcModePmenName, smcModeSettingsMenu )
        smcModePmen.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModePmen.setLabel( "Enable Page Mode" )
        smcModePmen.setDefaultValue( False )

        smcModePsNameStem = "SMC_MODE_PS"
        smcModePsName = smcModePsNameStem + "_" + csNum
        smcModePs = staticMemoryComponent.createKeyValueSetSymbol( smcModePsName, smcModeSettingsMenu )
        smcModePs.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModePs.setLabel( atdfSmcCsModeBitField_MODE_PS.getAttribute( "caption" ) )
        smcModePs.setOutputMode( "Key" )
        smcModePs.setDisplayMode( "Description" )
        smcModePs.setDefaultValue( 0 )
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__PS" ):
            smcModePs.addKey( smcModePsNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
        smcModePs.setDependencies( visibilityBasedOnBoolSymbol, [ smcModePmenName ] )

        smcModeTdfModeNameStem = "SMC_MODE_TDF_MODE"
        smcModeTdfModeName = smcModeTdfModeNameStem + "_" + csNum
        smcModeTdfMode = staticMemoryComponent.createBooleanSymbol( smcModeTdfModeName, smcModeSettingsMenu )
        smcModeTdfMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeTdfMode.setLabel( "Enable Data Float Time Optimization" )
        smcModeTdfMode.setDefaultValue( True )

        smcModeTdfCyclesNameStem = "SMC_MODE_TDF_CYCLES"
        smcModeTdfCyclesName = smcModeTdfCyclesNameStem + "_" + csNum
        smcModeTdfCycles = staticMemoryComponent.createIntegerSymbol( smcModeTdfCyclesName, smcModeSettingsMenu )
        smcModeTdfCycles.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeTdfCycles.setLabel( atdfSmcCsModeBitField_MODE_TDF_CYCLES.getAttribute( "caption" ) + " (cycles)" )
        smcModeTdfCycles.setMin( DEFAULT_SMC_MIN_VALUE )
        smcModeTdfCycles.setMax( convertMaskToInt( atdfSmcCsModeBitField_MODE_TDF_CYCLES.getAttribute( "mask" ) ) )
        smcModeTdfCycles.setDefaultValue( DEFAULT_SMC_MODE_TDF_CYCLES_VALUE )
        smcModeTdfCycles.setDependencies( visibilityBasedOnBoolSymbol, [ smcModeTdfModeName ] )

        smcModeExnwModeNameStem = "SMC_MODE_EXNW_MODE"
        smcModeExnwModeName = smcModeExnwModeNameStem + "_" + csNum
        smcModeExnwMode = staticMemoryComponent.createKeyValueSetSymbol( smcModeExnwModeName, smcModeSettingsMenu )
        smcModeExnwMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeExnwMode.setLabel( atdfSmcCsModeBitField_MODE_EXNW_MODE.getAttribute( "caption" ) )
        smcModeExnwMode.setOutputMode( "Key" )
        smcModeExnwMode.setDisplayMode( "Description" )
        smcModeExnwMode.setDefaultValue( 0 )
        # using name twice, not caption -- the atdf caption is too long; a couple of sentences
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__EXNW_MODE" ):
            smcModeExnwMode.addKey( smcModeExnwModeNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 0 ] )

        smcModeReadModeNameStem = "SMC_MODE_READ_MODE"
        smcModeReadModeName = smcModeReadModeNameStem + "_" + csNum
        smcModeReadMode = staticMemoryComponent.createKeyValueSetSymbol( smcModeReadModeName, smcModeSettingsMenu )
        smcModeReadMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeReadMode.setLabel( atdfSmcCsModeBitField_MODE_READ_MODE.getAttribute( "name" ) + " Control Signal" )
        smcModeReadMode.setOutputMode( "Key" )
        smcModeReadMode.setDisplayMode( "Description" )
        # using name twice, not caption -- the atdf caption is too long; a couple of sentences
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__READ_MODE" ):
            smcModeReadMode.addKey( smcModeReadModeNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 0 ] )
        if csNumIndex == smcNandCsNum.getValue():
            smcModeReadMode.setDefaultValue(1)
        else:
            smcModeReadMode.setDefaultValue(0)

        smcModeWriteModeNameStem = "SMC_MODE_WRITE_MODE"
        smcModeWriteModeName = smcModeWriteModeNameStem + "_" + csNum
        smcModeWriteMode = staticMemoryComponent.createKeyValueSetSymbol( smcModeWriteModeName, smcModeSettingsMenu )
        smcModeWriteMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SMC_MODE")
        smcModeWriteMode.setLabel( atdfSmcCsModeBitField_MODE_WRITE_MODE.getAttribute( "name" ) + " Control Signal" )
        smcModeWriteMode.setOutputMode( "Key" )
        smcModeWriteMode.setDisplayMode( "Description" )
        # using name twice, not caption -- the atdf caption is too long; a couple of sentences
        for tupleElem in getNameValueCaptionTuple( ModuleSmc, smcModeValGroupPrefix + "__WRITE_MODE" ):
            smcModeWriteMode.addKey( smcModeWriteModeNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 0 ] )
        if csNumIndex == smcNandCsNum.getValue():
            smcModeWriteMode.setDefaultValue(1)
        else:
            smcModeWriteMode.setDefaultValue(0)

        if csNumIndex == smcNandCsNum.getValue():
            smcEbiCS = staticMemoryComponent.createBooleanSymbol("SFR_CCFG_EBICSA_EBI_CS" + str(smcNandCsNum.getValue()) + "A", smcCsEnable)
            smcEbiCS.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SFR_CCFG_EBICSA")
            smcEbiCS.setLabel("Enable NAND Flash Logic")
            smcEbiCS.setDefaultValue(True)

            smcEbiCSNFD = staticMemoryComponent.createBooleanSymbol("SFR_CCFG_EBICSA_NFD0_ON_D16", smcCsEnable)
            smcEbiCSNFD.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:SFR_CCFG_EBICSA")
            smcEbiCSNFD.setLabel("Enable NAND Flash I/Os on D16-D23")
            smcEbiCSNFD.setDefaultValue(True)

    #--------------------------------------------------------------------------
    # PMECC

    # PMECC Control Register
    # Interrupt Enable
    pmeccIerErrieName = "PMECC_IER_ERRIE"
    pmeccIerErrie = staticMemoryComponent.createBooleanSymbol( pmeccIerErrieName, pmeccControlsMenu )
    pmeccIerErrie.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_IER")
    pmeccIerErrie.setLabel( atdfPmeccIerBitField_ERRIE.getAttribute( "caption" ) )
    pmeccIerErrie.setDefaultValue( False )
    pmeccIerErrie.setDependencies( updateInterrupt, [ pmeccIerErrieName ] )

    # SAREA Register
    pmeccSareaSpareSizeName = "PMECC_SAREA_SPARESIZE"
    pmeccSareaSpareSize = staticMemoryComponent.createIntegerSymbol( pmeccSareaSpareSizeName, pmeccControlsMenu )
    pmeccSareaSpareSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_SAREA")
    pmeccSareaSpareSize.setLabel( atdfPmeccSareaBitField_SPARESIZE.getAttribute( "caption" ) + " (bytes)" )
    pmeccSareaSpareSize.setMin( 1 )
    pmeccSareaSpareSize.setMax( 1 + convertMaskToInt( atdfPmeccSareaBitField_SPARESIZE.getAttribute( "mask" ) ) )
    pmeccSareaSpareSize.setDefaultValue( 56 )

    # SADDR Register
    pmeccSaddrStartAddrName = "PMECC_SADDR_STARTADDR"
    pmeccSaddrStartAddr = staticMemoryComponent.createIntegerSymbol( pmeccSaddrStartAddrName, pmeccControlsMenu )
    pmeccSaddrStartAddr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_SADDR")
    pmeccSaddrStartAddr.setLabel( atdfPmeccSaddrBitField_STARTADDR.getAttribute( "caption" ) )
    pmeccSaddrStartAddr.setMin( 0 )
    pmeccSaddrStartAddr.setMax( convertMaskToInt( atdfPmeccSaddrBitField_STARTADDR.getAttribute( "mask" ) ) )
    pmeccSaddrStartAddr.setDefaultValue( 2 )

    # EADDR Register
    pmeccEaddrEndAddrName = "PMECC_EADDR_ENDADDR"
    pmeccEaddrEndAddr = staticMemoryComponent.createIntegerSymbol( pmeccEaddrEndAddrName, pmeccControlsMenu )
    pmeccEaddrEndAddr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_EADDR")
    pmeccEaddrEndAddr.setLabel( atdfPmeccEaddrBitField_ENDADDR.getAttribute( "caption" ) )
    pmeccEaddrEndAddr.setMin( 0 )
    pmeccEaddrEndAddr.setMax( convertMaskToInt( atdfPmeccEaddrBitField_ENDADDR.getAttribute( "mask" ) ) )
    pmeccEaddrEndAddr.setDefaultValue( 57 )

    # Clk Control Register
    pmeccClkClkCtrlName = "PMECC_CLK_CLKCTRL"
    pmeccClkClkCtrl = staticMemoryComponent.createIntegerSymbol( pmeccClkClkCtrlName, pmeccControlsMenu )
    pmeccClkClkCtrl.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CLK")
    pmeccClkClkCtrl.setLabel( atdfPmeccClkBitField_CLKCTRL.getAttribute( "caption" ) + " (cycles)" )
    pmeccClkClkCtrl.setMin( 0 )
    pmeccClkClkCtrl.setMax( convertMaskToInt( atdfPmeccClkBitField_CLKCTRL.getAttribute( "mask" ) ) )
    pmeccClkClkCtrl.setDefaultValue( 0 )

    pmeccConfigurationMenu = staticMemoryComponent.createMenuSymbol( "PMECC_CONFIGURATION_MENU", pmeccControlsMenu )
    pmeccConfigurationMenu.setLabel( "Configuration" )
    pmeccConfigurationMenu.setDependencies( visibilityBasedOnBoolSymbol, [ pmeccCtrlEnableName ] )
    pmeccConfigurationMenu.setVisible( False )

    pmeccCfgSpareenName = "PMECC_CFG_SPAREEN"
    pmeccCfgSpareen = staticMemoryComponent.createBooleanSymbol( pmeccCfgSpareenName, pmeccConfigurationMenu )
    pmeccCfgSpareen.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgSpareen.setLabel( atdfPmeccCfgBitField_SPAREEN.getAttribute( "caption" ) )

    pmeccCfgAutoName = "PMECC_CFG_AUTO"
    pmeccCfgAuto = staticMemoryComponent.createBooleanSymbol( pmeccCfgAutoName, pmeccConfigurationMenu )
    pmeccCfgAuto.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgAuto.setLabel( atdfPmeccCfgBitField_AUTO.getAttribute( "caption" ) )
    pmeccCfgAuto.setDefaultValue(pmeccCfgSpareen.getValue() == False)
    pmeccCfgAuto.setReadOnly(True)
    pmeccCfgAuto.setDependencies(updateSymbolValue, ["PMECC_CFG_SPAREEN"])

    pmeccCfgNandWrName = "PMECC_CFG_NANDWR"
    pmeccCfgNandWr = staticMemoryComponent.createBooleanSymbol( pmeccCfgNandWrName, pmeccConfigurationMenu )
    pmeccCfgNandWr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgNandWr.setLabel( atdfPmeccCfgBitField_NANDWR.getAttribute( "caption" ) )

    pmeccCfgPageSizeName = "PMECC_CFG_PAGESIZE"
    pmeccCfgPageSize = staticMemoryComponent.createKeyValueSetSymbol( pmeccCfgPageSizeName, pmeccConfigurationMenu )
    pmeccCfgPageSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgPageSize.setLabel( atdfPmeccCfgBitField_PAGESIZE.getAttribute( "caption" ) )
    pmeccCfgPageSize.setOutputMode( "Value" )
    pmeccCfgPageSize.setDisplayMode( "Description" )
    pmeccCfgPageSize.setDefaultValue( 3 )
    for tupleElem in getNameValueCaptionTuple( ModulePmecc, "PMECC_CFG__PAGESIZE" ):
        pmeccCfgPageSize.addKey( pmeccCfgPageSizeName + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    pmeccCfgSectorSzName = "PMECC_CFG_SECTORSZ"
    pmeccCfgSectorSz = staticMemoryComponent.createIntegerSymbol( pmeccCfgSectorSzName, pmeccConfigurationMenu )
    pmeccCfgSectorSz.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgSectorSz.setLabel( atdfPmeccCfgBitField_SECTORSZ.getAttribute( "caption" )  + " (bytes), 0: 512, 1: 1024" )
    pmeccCfgSectorSz.setMin( 0 )
    pmeccCfgSectorSz.setMax( convertMaskToInt( atdfPmeccCfgBitField_SECTORSZ.getAttribute( "mask" ) ) )
    pmeccCfgSectorSz.setDefaultValue( 0 )

    pmeccCfgBchErrNameStem = "PMECC_CFG_BCH_ERR"
    pmeccCfgBchErrName = pmeccCfgBchErrNameStem
    pmeccCfgBchErr = staticMemoryComponent.createKeyValueSetSymbol( pmeccCfgBchErrName, pmeccConfigurationMenu )
    pmeccCfgBchErr.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMECC_CFG")
    pmeccCfgBchErr.setLabel( atdfPmeccCfgBitField_BCH_ERR.getAttribute( "caption" ) )
    pmeccCfgBchErr.setOutputMode( "Value" )
    pmeccCfgBchErr.setDisplayMode( "Description" )
    pmeccCfgBchErr.setDefaultValue( 1 )
    for tupleElem in getNameValueCaptionTuple(  ModulePmecc, "PMECC_CFG__BCH_ERR" ):
        pmeccCfgBchErr.addKey( pmeccCfgBchErrNameStem + "_" + tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    #PMECC API Prefix for NAND Flash Driver
    pmeccSym_API_Prefix = staticMemoryComponent.createStringSymbol("PMECC_API_PREFIX", None)
    pmeccSym_API_Prefix.setDefaultValue(pmeccInstanceName.getValue())
    pmeccSym_API_Prefix.setVisible(False)

    #--------------------------------------------------------------------------
    # PMERR
    # ELIER Register
    pmerrlocElierDoneName = "PMERRLOC_ELIER_DONE"
    pmerrlocElierDone = staticMemoryComponent.createBooleanSymbol( pmerrlocElierDoneName, pmerrlocControlsMenu )
    pmerrlocElierDone.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMERRLOC_ELIER")
    pmerrlocElierDone.setLabel( atdfPmerrlocElierBitField_DONE.getAttribute( "caption" ) )
    pmerrlocElierDone.setDefaultValue( False )
    pmerrlocElierDone.setDependencies( updateInterrupt, [ pmerrlocElierDoneName ] )
    # ELDIS Register
    # ELEN Register
    # ELCFG Register
    pmerrlocElcfgSectorSzName = "PMERRLOC_ELCFG_SECTORSZ"
    pmerrlocElcfgSectorSz = staticMemoryComponent.createIntegerSymbol( pmerrlocElcfgSectorSzName, pmerrlocControlsMenu )
    pmerrlocElcfgSectorSz.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:smc_6105;register:PMERRLOC_ELCFG")
    pmerrlocElcfgSectorSz.setLabel( atdfPmerrlocElcfgBitField_SECTORSZ.getAttribute( "caption" ) + " (see PMECC Configuration Menu)" )
    pmerrlocElcfgSectorSz.setMin( 0 )
    pmerrlocElcfgSectorSz.setMax( convertMaskToInt( atdfPmerrlocElcfgBitField_SECTORSZ.getAttribute( "mask" ) ) )
    pmerrlocElcfgSectorSz.setReadOnly( True )
    pmerrlocElcfgSectorSz.setDependencies( pmerrlocCfgSectorSize, [ pmeccCfgSectorSzName ] )

    #PMERRLOC API Prefix for NAND Flash Driver
    pmerrlocSym_API_Prefix = staticMemoryComponent.createStringSymbol("PMERRLOC_API_PREFIX", None)
    pmerrlocSym_API_Prefix.setDefaultValue(pmeccLocInstanceName.getValue())
    pmerrlocSym_API_Prefix.setVisible(False)

    #
    #------------------------------------------------------------------------------
    # Code Generation
    PeriphId = "6105"
    PeriphName = myNamespace.lower()
    PlibNameStem = "PLIB_" + PeriphName.upper()
    OutputNameStem = PlibNameStem.lower()
    FullTemplatePath = "../peripheral/" + PeriphName + "_" + PeriphId + "/templates/"
    FullSysPath = FullTemplatePath + "/system/"
    FullSrcPathNameStem = FullTemplatePath + OutputNameStem
    FinalDest = "/peripheral/" + PeriphName + "/"
    FullProjectPath = "config/" + Variables.get( "__CONFIGURATION_NAME" ) + FinalDest

    headerFile = staticMemoryComponent.createFileSymbol( FullSrcPathNameStem + "_H", None )
    headerFile.setSourcePath( FullSrcPathNameStem + ".h.ftl" )
    headerFile.setOutputName( OutputNameStem + ".h" )
    headerFile.setDestPath( FinalDest )
    headerFile.setProjectPath( FullProjectPath )
    headerFile.setType( "HEADER" )
    headerFile.setMarkup( True )

    sourceFile = staticMemoryComponent.createFileSymbol( PlibNameStem + "_C", None )
    sourceFile.setSourcePath( FullSrcPathNameStem + ".c.ftl" )
    sourceFile.setOutputName( OutputNameStem + ".c" )
    sourceFile.setDestPath( FinalDest )
    sourceFile.setProjectPath( FullProjectPath )
    sourceFile.setType( "SOURCE" )
    sourceFile.setMarkup( True )

    # Add related code to common files
    headerFileEntry = staticMemoryComponent.createFileSymbol( PlibNameStem + "_DEFINITIONS_H", None )
    headerFileEntry.setType( "STRING" )
    headerFileEntry.setOutputName( "core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES" )
    headerFileEntry.setSourcePath( FullSysPath + "definitions.h.ftl" )
    headerFileEntry.setMarkup( True )

    systemInitFile = staticMemoryComponent.createFileSymbol( PlibNameStem + "_INITIALIZE_H", None )
    systemInitFile.setType( "STRING" )
    systemInitFile.setOutputName( "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS" )
    systemInitFile.setSourcePath( FullSysPath + "initialization.c.ftl" )
    systemInitFile.setMarkup( True )

