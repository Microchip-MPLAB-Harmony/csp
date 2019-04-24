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

#********************** Static Memory Controller Module ***********************

#------------------------------------------------------------------------------
# ATDF register references
#------------------------------------------------------------------------------
atdfModuleSmc =         '/avr-tools-device-file/modules/module@[name="SMC"]'
atdfSmcRegisterGroup =  atdfModuleSmc + '/register-group@[name="SMC"]'

#
atdfNfcConfiguration =                  atdfSmcRegisterGroup + '/register@[name="HSMC_CFG"]'
atdfNfcControl =                        atdfSmcRegisterGroup + '/register@[name="HSMC_CTRL"]'
atdfNfcInterruptEnable =                atdfSmcRegisterGroup + '/register@[name="HSMC_IER"]'
atdfNfcAddressCycleZero =               atdfSmcRegisterGroup + '/register@[name="HSMC_ADDR"]'
atdfNfcBankAddress =                    atdfSmcRegisterGroup + '/register@[name="HSMC_BANK"]'
#
atdfPmeccConfiguration =                atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCFG"]'
atdfPmeccSpareAreaSize =                atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCSAREA"]'
atdfPmeccStartAddress =                 atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCSADDR"]'
atdfPmeccEndAddress =                   atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCEADDR"]'
atdfPmeccControl =                      atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCTRL"]'
atdfPmeccInterruptEnable =              atdfSmcRegisterGroup + '/register@[name="HSMC_PMECCIER"]'
#
atdfPmeccErrorLocationConfiguration =   atdfSmcRegisterGroup + '/register@[name="HSMC_ELCFG"]'
atdfPmeccErrorLocationEnable =          atdfSmcRegisterGroup + '/register@[name="HSMC_ELEN"]'
atdfPmeccErrorLocationDisable =         atdfSmcRegisterGroup + '/register@[name="HSMC_ELDIS"]'
atdfPmeccErrorLocationInterruptEnable = atdfSmcRegisterGroup + '/register@[name="HSMC_ELIER"]'
#
atdfHsmcSetup =                         atdfModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]/register@[name="HSMC_SETUP"]'
atdfHsmcPulse =                         atdfModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]/register@[name="HSMC_PULSE"]'
atdfHsmcCycle =                         atdfModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]/register@[name="HSMC_CYCLE"]'
atdfHsmcTimings =                       atdfModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]/register@[name="HSMC_TIMINGS"]'
atdfHsmcMode =                          atdfModuleSmc + '/register-group@[name="SMC_CS_NUMBER"]/register@[name="HSMC_MODE"]'
#
atdfOffChipMemoryScrambling  =          atdfSmcRegisterGroup + '/register@[name="HSMC_OCMS"]'
atdfOffChipMemoryScramblingKey1  =      atdfSmcRegisterGroup + '/register@[name="HSMC_KEY1"]'
atdfOffChipMemoryScramblingKey2  =      atdfSmcRegisterGroup + '/register@[name="HSMC_KEY2"]'
atdfWriteProtectionMode =               atdfSmcRegisterGroup + '/register@[name="HSMC_WPMR"]'

#------------------------------------------------------------------------------
# ATDF register bit field and mask nodes
#------------------------------------------------------------------------------
# HSMC_CFG bit field
bitField_CFG_PAGESIZE =                 ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="PAGESIZE"]' )
bitField_CFG_WSPARE =                   ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="WSPARE"]' )
bitField_CFG_RSPARE =                   ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="RSPARE"]' )
bitField_CFG_EDGECTRL =                 ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="EDGECTRL"]' )
bitField_CFG_RBEDGE =                   ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="RBEDGE"]' )
bitField_CFG_DTOCYC =                   ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="DTOCYC"]' )
bitField_CFG_DTOMUL =                   ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="DTOMUL"]' )
bitField_CFG_NFCSPARESIZE =             ATDF.getNode( atdfNfcConfiguration + '/bitfield@[name="NFCSPARESIZE"]' )
# HSMC_CTRL bit field
bitField_CTRL_NFCEN =                   ATDF.getNode( atdfNfcControl + '/bitfield@[name="NFCEN"]' )
# HSMC_IER bit field
bitField_IER_RB_RISE =                  ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="RB_RISE"]' )
bitField_IER_RB_FALL =                  ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="RB_FALL"]' )
bitField_IER_XFRDONE =                  ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="XFRDONE"]' )
bitField_IER_CMDDONE =                  ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="CMDDONE"]' )
bitField_IER_DTOE =                     ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="DTOE"]' )
bitField_IER_UNDEF =                    ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="UNDEF"]' )
bitField_IER_AWB =                      ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="AWB"]' )
bitField_IER_NFCASE =                   ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="NFCASE"]' )
bitField_IER_RB_EDGE0 =                 ATDF.getNode( atdfNfcInterruptEnable + '/bitfield@[name="RB_EDGE0"]' )
# HSMC_ADDR bit field
bitField_ADDR_ADDR_CYCLE0 =             ATDF.getNode( atdfNfcAddressCycleZero + '/bitfield@[name="ADDR_CYCLE0"]' )
# HSMC_BANK bit field
bitField_BANK_BANK =                    ATDF.getNode( atdfNfcBankAddress + '/bitfield@[name="BANK"]' )
# HSMC_PMECCFG bit field
bitField_PMECCFG_BCH_ERR =              ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="BCH_ERR"]' )
bitField_PMECCFG_SECTORSZ =             ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="SECTORSZ"]' )
bitField_PMECCFG_PAGESIZE =             ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="PAGESIZE"]' )
bitField_PMECCFG_NANDWR =               ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="NANDWR"]' )
bitField_PMECCFG_SPAREEN =              ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="SPAREEN"]' )
bitField_PMECCFG_AUTO =                 ATDF.getNode( atdfPmeccConfiguration + '/bitfield@[name="AUTO"]' )
# HSMC_PMECCSAREA bit field
bitField_PMECCSAREA_SPARESIZE =         ATDF.getNode( atdfPmeccSpareAreaSize + '/bitfield@[name="SPARESIZE"]' )
# HSMC_PMECCSADDR bit field
bitField_PMECCSADDR_STARTADDR =         ATDF.getNode( atdfPmeccStartAddress + '/bitfield@[name="STARTADDR"]' )
# HSMC_PMECCEADDR bit field
bitField_PMECCEADDR_ENDADDR =           ATDF.getNode( atdfPmeccEndAddress + '/bitfield@[name="ENDADDR"]' )
# HSMC_PMECCTRL bit field
bitField_PMECCTRL_ENABLE =              ATDF.getNode( atdfPmeccControl + '/bitfield@[name="ENABLE"]' )
# HSMC_PMECCIER bit field
bitField_PMECCIER_ENABLE =              ATDF.getNode( atdfPmeccInterruptEnable + '/bitfield@[name="ERRIE"]' )
# HSMC_ELCFG bit field
bitField_ELCFG_SECTORSZ =               ATDF.getNode( atdfPmeccErrorLocationConfiguration + '/bitfield@[name="SECTORSZ"]' )
# HSMC_ELEN bit field
bitField_ELEN_ENINIT =                  ATDF.getNode( atdfPmeccErrorLocationEnable + '/bitfield@[name="ENINIT"]' )
# HSMC_ELDIS bit field
bitField_ELDIS_DIS =                    ATDF.getNode( atdfPmeccErrorLocationDisable + '/bitfield@[name="DIS"]' )
# HSMC_ELIER bit field
bitField_ELIER_DONE =                   ATDF.getNode( atdfPmeccErrorLocationInterruptEnable + '/bitfield@[name="DONE"]' )
# SMC_CS_NUMBER
atdfSmcCsNumber =                       ATDF.getNode( atdfSmcRegisterGroup + '/register-group@[name="SMC_CS_NUMBER"]' )
# HSMC_SETUP bit field
bitField_SETUP_NCS_RD =                 ATDF.getNode( atdfHsmcSetup + '/bitfield@[name="NCS_RD_SETUP"]' )
bitField_SETUP_NRD =                    ATDF.getNode( atdfHsmcSetup + '/bitfield@[name="NRD_SETUP"]' )
bitField_SETUP_NCS_WR =                 ATDF.getNode( atdfHsmcSetup + '/bitfield@[name="NCS_WR_SETUP"]' )
bitField_SETUP_NWE =                    ATDF.getNode( atdfHsmcSetup + '/bitfield@[name="NWE_SETUP"]' )
# HSMC_PULSE bit field
bitField_PULSE_NCS_RD =                 ATDF.getNode( atdfHsmcPulse + '/bitfield@[name="NCS_RD_PULSE"]' )
bitField_PULSE_NRD =                    ATDF.getNode( atdfHsmcPulse + '/bitfield@[name="NRD_PULSE"]' )
bitField_PULSE_NCS_WR =                 ATDF.getNode( atdfHsmcPulse + '/bitfield@[name="NCS_WR_PULSE"]' )
bitField_PULSE_NWE =                    ATDF.getNode( atdfHsmcPulse + '/bitfield@[name="NWE_PULSE"]' )
# HSMC_CYCLE bit field
bitField_CYCLE_NRD =                    ATDF.getNode( atdfHsmcCycle + '/bitfield@[name="NRD_CYCLE"]' )
bitField_CYCLE_NWE =                    ATDF.getNode( atdfHsmcCycle + '/bitfield@[name="NWE_CYCLE"]' )
# HSMC_TIMINGS bit field
bitField_TIMINGS_NFSEL =                ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="NFSEL"]' )
bitField_TIMINGS_TWB =                  ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="TWB"]' )
bitField_TIMINGS_TRR =                  ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="TRR"]' )
bitField_TIMINGS_OCMS =                 ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="OCMS"]' )
bitField_TIMINGS_TAR =                  ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="TAR"]' )
bitField_TIMINGS_TADL =                 ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="TADL"]' )
bitField_TIMINGS_TCLR =                 ATDF.getNode( atdfHsmcTimings + '/bitfield@[name="TCLR"]' )
# HSMC_MODE bit field
bitField_MODE_TDF_MODE =                ATDF.getNode( atdfHsmcMode + '/bitfield@[name="TDF_MODE"]' )
bitField_MODE_TDF_CYCLES  =             ATDF.getNode( atdfHsmcMode + '/bitfield@[name="TDF_CYCLES"]' )
bitField_MODE_DBW =                     ATDF.getNode( atdfHsmcMode + '/bitfield@[name="DBW"]' )
bitField_MODE_BAT =                     ATDF.getNode( atdfHsmcMode + '/bitfield@[name="BAT"]' )
bitField_MODE_EXNW_MODE =               ATDF.getNode( atdfHsmcMode + '/bitfield@[name="EXNW_MODE"]' )
bitField_MODE_WRITE_MODE =              ATDF.getNode( atdfHsmcMode + '/bitfield@[name="WRITE_MODE"]' )
bitField_MODE_READ_MODE =               ATDF.getNode( atdfHsmcMode + '/bitfield@[name="READ_MODE"]' )
# HSMC_OCMS bit field
bitField_OCMS_SMSE =                    ATDF.getNode( atdfOffChipMemoryScrambling + '/bitfield@[name="SMSE"]' )
bitField_OCMS_SRSE =                    ATDF.getNode( atdfOffChipMemoryScrambling + '/bitfield@[name="SRSE"]' )
# HSMC_KEY1 bit field
bitField_KEY1_KEY1 =                    ATDF.getNode( atdfOffChipMemoryScramblingKey1 + '/bitfield@[name="KEY1"]' )
# HSMC_KEY2 bit field
bitField_KEY2_KEY2 =                    ATDF.getNode( atdfOffChipMemoryScramblingKey2 + '/bitfield@[name="KEY2"]' )
# HSMC_WPMR bit field
bitField_WPMR_WPEN =                    ATDF.getNode( atdfWriteProtectionMode + '/bitfield@[name="WPEN"]' )

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------
DEFAULT_NFC_MIN_VALUE =             0
DEFAULT_NFC_SPARE_AREA_SIZE =       0

DEFAULT_PMECC_MIN_VALUE =           0
DEFAULT_PMECC_SPARE_AREA_SIZE =     0
DEFAULT_PMECC_START_ADDRESS =       0
DEFAULT_PMECC_END_ADDRESS =         0

DEFAULT_PMECC_ERROR_LOCATION_MIN_VALUE = 0 
DEFAULT_PMECC_ERROR_LOCATION_SECTOR_SIZE = 0
DEFAULT_PMECC_ERROR_LOCATION_CODEWORD = 0

DEFAULT_SMC_SETUP_VALUE =           16
DEFAULT_SMC_SETUP_MIN_VALUE =       1
DEFAULT_SMC_PULSE_VALUE =           16
DEFAULT_SMC_PULSE_MIN_VALUE =       1
DEFAULT_SMC_CYCLE_MIN_VALUE =       4
DEFAULT_SMC_TIMINGS_VALUE =         0
DEFAULT_SMC_TIMINGS_MIN_VALUE =     0
DEFAULT_SMC_MODE_MIN_VALUE =        0
DEFAULT_SMC_MODE_TDF_CYCLES_VALUE = 0

global myNamespace
global nfcDataTimeOutCycleName
global nfcDataTimeOutMultiplierName
global setupNCsRdNameStem
global setupNRdNameStem
global setupNCsWrNameStem
global setupNWeNameStem
global pulseNCsRdNameStem
global pulseNRdNameStem
global pulseNCsWrNameStem
global pulseNWeNameStem
global cycleNRdNameStem
global cycleNWeNameStem
global timingsNfSelNameStem
global timingsTwbNameStem
global timingsTrrNameStem
global timingsOcmsNameStem
global timingsTarNameStem
global timingsTadlNameStem
global timingsTclrNameStem
global modeTdfModeNameStem
global modeTdfCyclesNameStem
global modeDbwNameStem
global modeBatNameStem
global modeNWaitNameStem
global modeWriteModeNameStem
global modeReadModeNameStem

#------------------------------------------------------------------------------
# Dependency Functions
#------------------------------------------------------------------------------
def getNameValueCaptionTuple( aGroupName ):
    choiceNode = ATDF.getNode( atdfModuleSmc + '/value-group@[name="' + aGroupName + '"]' )
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


def visibilityBasedOnBoolSymbol( symbol, event ):
    symbol.setVisible( event[ "value" ] )


def smcModeByteWriteOrSelectAccessVisible( symbol, event ):
    """ function to enable visibility based on selection of Byte Access Type """ 
    if( event[ "symbol" ].getSelectedKey() == "SMC_DBW_16_BIT" ):
        symbol.setVisible( True )
    else:
        symbol.setVisible( False )


def instantiateComponent( smcComponent ):
    """ Create the menu display and symbols for the SMC component """ 
    global myNamespace 
    global nfcDataTimeOutCycleName
    global nfcDataTimeOutMultiplierName
    global setupNCsRdNameStem,      setupNCsWrNameStem,     pulseNCsRdNameStem,     pulseNCsWrNameStem
    global setupNRdNameStem,        setupNWeNameStem,       pulseNRdNameStem,       pulseNWeNameStem
    global cycleNRdNameStem,        cycleNWeNameStem
    global timingsNfSelNameStem,    timingsTwbNameStem,     timingsTrrNameStem,     timingsOcmsNameStem
    global timingsTarNameStem,      timingsTadlNameStem,    timingsTclrNameStem
    global modeTdfModeNameStem,     modeTdfCyclesNameStem,  modeDbwNameStem,        modeBatNameStem
    global modeNWaitNameStem,       modeReadModeNameStem,   modeWriteModeNameStem
    
    myNamespace = str( smcComponent.getID() )
    smcInstanceName = smcComponent.createStringSymbol( "SMC_INSTANCE_NAME", None )
    smcInstanceName.setVisible( False )
    smcInstanceName.setDefaultValue( myNamespace.upper() )
    #--------------------------------------------------------------------------
    nandFlashControllerMenu = smcComponent.createMenuSymbol( "SMC_NAND_FLASH_CONTROLLER", None ) 
    nandFlashControllerMenu.setLabel( "NAND Flash Controller" )
    # ----- 
    nfcConfigurationMenu = smcComponent.createMenuSymbol( "SMC_NFC_CONFIGURATION", nandFlashControllerMenu ) 
    nfcConfigurationMenu.setLabel( "NFC Configuration" )
    # ----- 
    nfcControllerEnable = smcComponent.createBooleanSymbol( "SMC_NFC_CONTROLLER_ENABLE", nfcConfigurationMenu ) 
    nfcControllerEnable.setLabel( bitField_CTRL_NFCEN.getAttribute( "caption" ) ) 

    nfcPageSize = smcComponent.createKeyValueSetSymbol( "SMC_NFC_PAGE_SIZE", nfcConfigurationMenu ) 
    nfcPageSize.setLabel( bitField_CFG_PAGESIZE.getAttribute( "caption" ) )
    nfcPageSize.setOutputMode( "Key" )
    nfcPageSize.setDisplayMode( "Description" )
    nfcPageSize.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_CFG__PAGESIZE" ):
        nfcPageSize.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    nfcWriteSpare = smcComponent.createBooleanSymbol( "SMC_NFC_WRITE_SPARE", nfcConfigurationMenu ) 
    nfcWriteSpare.setLabel( bitField_CFG_WSPARE.getAttribute( "caption" ) )

    nfcReadSpare = smcComponent.createBooleanSymbol( "SMC_NFC_READ_SPARE", nfcConfigurationMenu ) 
    nfcReadSpare.setLabel( bitField_CFG_RSPARE.getAttribute( "caption" ) )

    nfcEdgeDetect = smcComponent.createBooleanSymbol( "SMC_NFC_EDGE_DETECT", nfcConfigurationMenu ) 
    nfcEdgeDetect.setLabel( bitField_CFG_EDGECTRL.getAttribute( "caption" ) )

    nfcReadyBusyDetect = smcComponent.createBooleanSymbol( "SMC_NFC_READY_BUSY_DETECT", nfcConfigurationMenu ) 
    nfcReadyBusyDetect.setLabel( bitField_CFG_RBEDGE.getAttribute( "caption" ) )

    nfcDataTimeOutCycleName = "SMC_NFC_DATA_TIMEOUT_CYCLE"
    nfcDataTimeOutCycle = smcComponent.createIntegerSymbol( nfcDataTimeOutCycleName, nfcConfigurationMenu ) 
    nfcDataTimeOutCycle.setLabel( bitField_CFG_DTOCYC.getAttribute( "caption" ) )
    nfcDataTimeOutCycle.setMin( DEFAULT_NFC_MIN_VALUE )
    nfcDataTimeOutCycle.setMax( convertMaskToInt( bitField_CFG_DTOCYC.getAttribute( "mask" ) ) )

    nfcDataTimeOutMultiplierName = "SMC_NFC_DATA_TIMEOUT_MULTIPLIER"
    nfcDataTimeOutMuliplier = smcComponent.createKeyValueSetSymbol( nfcDataTimeOutMultiplierName, nfcConfigurationMenu )
    nfcDataTimeOutMuliplier.setLabel( bitField_CFG_DTOMUL.getAttribute( "caption" ) )
    nfcDataTimeOutMuliplier.setOutputMode( "Key" )
    nfcDataTimeOutMuliplier.setDisplayMode( "Description" )
    nfcDataTimeOutMuliplier.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_CFG__DTOMUL" ):
        nfcDataTimeOutMuliplier.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
    
    nfcSpareAreaSizeName = "SMC_NFC_SPARE_AREA_SIZE"
    nfcSpareAreaSizeCaption = bitField_CFG_NFCSPARESIZE.getAttribute( "caption" )
    nfcSpareAreaSize = smcComponent.createIntegerSymbol( nfcSpareAreaSizeName, nfcConfigurationMenu ) 
    nfcSpareAreaSize.setLabel( nfcSpareAreaSizeCaption )
    nfcSpareAreaSize.setMin( DEFAULT_NFC_MIN_VALUE )
    nfcSpareAreaSize.setMax( convertMaskToInt( bitField_CFG_NFCSPARESIZE.getAttribute( "mask" ) ) )
    nfcSpareAreaSize.setDefaultValue( DEFAULT_NFC_SPARE_AREA_SIZE )
    # -----     
    nfcAddressCycle0 = smcComponent.createIntegerSymbol( "SMC_NFC_ADDRESS_CYCLE_0", nandFlashControllerMenu ) 
    nfcAddressCycle0.setLabel( bitField_ADDR_ADDR_CYCLE0.getAttribute( "caption" ) ) 
    nfcAddressCycle0.setMin( DEFAULT_NFC_MIN_VALUE )
    nfcAddressCycle0.setMax( convertMaskToInt( bitField_ADDR_ADDR_CYCLE0.getAttribute( "mask" ) ) )
    nfcAddressCycle0.setDefaultValue( DEFAULT_NFC_MIN_VALUE )

    nfcBankAddress = smcComponent.createIntegerSymbol( "SMC_NFC_BANK_ADDRESS", nandFlashControllerMenu ) 
    nfcBankAddress.setLabel( bitField_BANK_BANK.getAttribute( "caption" ) ) 
    nfcBankAddress.setMin( DEFAULT_NFC_MIN_VALUE )
    nfcBankAddress.setMax( convertMaskToInt( bitField_BANK_BANK.getAttribute( "mask" ) ) )
    nfcBankAddress.setDefaultValue( DEFAULT_NFC_MIN_VALUE )
    # ----- 
    pmeccMenu = smcComponent.createMenuSymbol( "SMC_PMECC", None ) 
    pmeccMenu.setLabel( "Programmable Multi-bit Error Correction Code" )
    # ----- 
    pmeccEnable = smcComponent.createBooleanSymbol( "SMC_PMECC_ENABLE", pmeccMenu ) 
    pmeccEnable.setLabel( bitField_PMECCTRL_ENABLE.getAttribute( "caption" ) )
    # ----- 
    pmeccErrorCorrectionCapability = smcComponent.createKeyValueSetSymbol( "SMC_PMECC_ERROR_CORRECTION_CAPABILITY", pmeccMenu )
    pmeccErrorCorrectionCapability.setLabel( bitField_PMECCFG_BCH_ERR.getAttribute( "caption" ) )
    pmeccErrorCorrectionCapability.setOutputMode( "Key" )
    pmeccErrorCorrectionCapability.setDisplayMode( "Description" )
    pmeccErrorCorrectionCapability.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_PMECCFG__BCH_ERR" ):
        pmeccErrorCorrectionCapability.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    pmeccSectorSize = smcComponent.createKeyValueSetSymbol( "SMC_PMECC_SECTOR_SIZE", pmeccMenu ) 
    pmeccSectorSize.setLabel( bitField_PMECCFG_SECTORSZ.getAttribute( "caption" ) )
    pmeccSectorSize.setOutputMode( "Key" )
    pmeccSectorSize.setDisplayMode( "Description" )
    pmeccSectorSize.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_PMECCFG__SECTORSZ" ):
        pmeccSectorSize.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    pmeccSectorsPerPage = smcComponent.createKeyValueSetSymbol( "SMC_PMECC_SECTORS_PER_PAGE", pmeccMenu ) 
    pmeccSectorsPerPage.setLabel( bitField_PMECCFG_PAGESIZE.getAttribute( "caption" ) )
    pmeccSectorsPerPage.setOutputMode( "Key" )
    pmeccSectorsPerPage.setDisplayMode( "Description" )
    pmeccSectorsPerPage.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_PMECCFG__PAGESIZE" ):
        pmeccSectorsPerPage.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

    pmeccNandWriteAccess = smcComponent.createBooleanSymbol( "SMC_PMECC_NAND_WRITE_ACCESS", pmeccMenu ) 
    pmeccNandWriteAccess.setLabel( bitField_PMECCFG_NANDWR.getAttribute( "caption" ) )

    pmeccSpareAreaEnable = smcComponent.createBooleanSymbol( "SMC_PMECC_SPARE_AREA_ENABLE", pmeccMenu ) 
    pmeccSpareAreaEnable.setLabel( bitField_PMECCFG_SPAREEN.getAttribute( "caption" ) )

    pmeccAutomaticModeEnable = smcComponent.createBooleanSymbol( "SMC_PMECC_AUTOMATIC_MODE_ENABLE", pmeccMenu ) 
    pmeccAutomaticModeEnable.setLabel( bitField_PMECCFG_AUTO.getAttribute( "caption" ) )
    # ----- 
    pmeccSpareAreaSize = smcComponent.createIntegerSymbol( "SMC_PMECC_SPARE_AREA_SIZE", pmeccMenu ) 
    pmeccSpareAreaSize.setLabel( bitField_PMECCSAREA_SPARESIZE.getAttribute( "caption" ) )
    pmeccSpareAreaSize.setMin( DEFAULT_PMECC_MIN_VALUE )
    pmeccSpareAreaSize.setMax( convertMaskToInt( bitField_PMECCSAREA_SPARESIZE.getAttribute( "mask" ) ) )
    pmeccSpareAreaSize.setDefaultValue( DEFAULT_PMECC_SPARE_AREA_SIZE )
    # ----- 
    pmeccStartAddress = smcComponent.createIntegerSymbol( "SMC_PMECC_START_ADDRESS", pmeccMenu ) 
    pmeccStartAddress.setLabel( bitField_PMECCSADDR_STARTADDR.getAttribute( "caption" ) )
    pmeccStartAddress.setMin( DEFAULT_PMECC_MIN_VALUE )
    pmeccStartAddress.setMax( convertMaskToInt( bitField_PMECCSADDR_STARTADDR.getAttribute( "mask" ) ) )
    pmeccStartAddress.setDefaultValue( DEFAULT_PMECC_START_ADDRESS )
    # ----- 
    pmeccEndAddress = smcComponent.createIntegerSymbol( "SMC_PMECC_END_ADDRESS", pmeccMenu ) 
    pmeccEndAddress.setLabel( bitField_PMECCEADDR_ENDADDR.getAttribute( "caption" ) )
    pmeccEndAddress.setMin( DEFAULT_PMECC_MIN_VALUE )
    pmeccEndAddress.setMax( convertMaskToInt( bitField_PMECCEADDR_ENDADDR.getAttribute( "mask" ) ) )
    pmeccEndAddress.setDefaultValue( DEFAULT_PMECC_END_ADDRESS )
    # ----- 
    pmeccErrorLocationMenu = smcComponent.createMenuSymbol( "SMC_PMECC_ERROR_LOCATION", None ) 
    pmeccErrorLocationMenu.setLabel( "PMECC Error Location" )
    # ----- 
    pmeccErrorLocationDisable = smcComponent.createBooleanSymbol( "SMC_PMECC_ERROR_LOCATION_DISABLE", pmeccErrorLocationMenu ) 
    pmeccErrorLocationDisable.setLabel( bitField_ELDIS_DIS.getAttribute( "caption" ) )
    # -----
    pmeccErrorLocationEnable = smcComponent.createIntegerSymbol( "SMC_PMECC_ERROR_LOCATION_ENABLE_CODEWORD", pmeccErrorLocationMenu ) 
    pmeccErrorLocationEnable.setLabel( bitField_ELEN_ENINIT.getAttribute( "caption" ) )
    pmeccErrorLocationEnable.setMin( DEFAULT_PMECC_ERROR_LOCATION_MIN_VALUE )
    pmeccErrorLocationEnable.setMax( convertMaskToInt( bitField_ELEN_ENINIT.getAttribute( "mask" ) ) )
    pmeccErrorLocationEnable.setDefaultValue( DEFAULT_PMECC_ERROR_LOCATION_CODEWORD )
    # ----- 
    pmeccErrorLocationSectorSize = smcComponent.createKeyValueSetSymbol( "SMC_PMECC_ERROR_LOCATION_SECTOR_SIZE", pmeccErrorLocationMenu ) 
    pmeccErrorLocationSectorSize.setLabel( bitField_ELCFG_SECTORSZ.getAttribute( "caption" ) )
    pmeccErrorLocationSectorSize.setOutputMode( "Key" )
    pmeccErrorLocationSectorSize.setDisplayMode( "Description" )
    pmeccErrorLocationSectorSize.setDefaultValue( 0 )
    for tupleElem in getNameValueCaptionTuple( "HSMC_ELCFG__SECTORSZ" ):
        pmeccErrorLocationSectorSize.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
    # ----- 
    chipSelectionMenu = smcComponent.createMenuSymbol( "SMC_CHIP_SELECTION", None ) 
    chipSelectionMenu.setLabel( "Chip Selection and Settings" )

    smcCsCount = int( atdfSmcCsNumber.getAttribute( "count" ) )
    csCountSymbol = smcComponent.createIntegerSymbol( "SMC_CS_COUNT", chipSelectionMenu )
    csCountSymbol.setDefaultValue( smcCsCount )
    csCountSymbol.setVisible( False )
    for csNumIndex in range(0, smcCsCount):
        csNum = str( csNumIndex )
        chipSelectEnable = smcComponent.createBooleanSymbol( "SMC_CHIP_SELECT_ENABLE" + csNum, chipSelectionMenu)
        chipSelectEnable.setLabel( "Chip Select " + csNum + " Enable" ) 
        # Mode register
        modeSettingsMenu = smcComponent.createMenuSymbol( "SMC_MODE_SETTINGS" + csNum, chipSelectEnable )
        modeSettingsMenu.setLabel( "Mode Settings" )

        modeTdfModeNameStem = "SMC_MODE_TDF_MODE"
        modeTdfModeName = modeTdfModeNameStem + csNum  
        modeTdfMode = smcComponent.createBooleanSymbol( modeTdfModeName, modeSettingsMenu )
        modeTdfMode.setLabel( bitField_MODE_TDF_MODE.getAttribute( "caption" ) )
        modeTdfMode.setDefaultValue( False )

        modeTdfCyclesNameStem = "SMC_MODE_TDF_CYCLES"
        modeTdfCyclesName = modeTdfCyclesNameStem + csNum  
        modeTdfCycles = smcComponent.createIntegerSymbol( modeTdfCyclesName, modeSettingsMenu )
        modeTdfCycles.setLabel( bitField_MODE_TDF_CYCLES.getAttribute( "caption" ) )
        modeTdfCycles.setMin( DEFAULT_SMC_MODE_MIN_VALUE )
        modeTdfCycles.setMax( convertMaskToInt( bitField_MODE_TDF_CYCLES.getAttribute( "mask" ) ) )
        modeTdfCycles.setDefaultValue( DEFAULT_SMC_MODE_TDF_CYCLES_VALUE)
        modeTdfCycles.setDependencies( visibilityBasedOnBoolSymbol, [modeTdfModeName] )

        modeDbwNameStem = "SMC_MODE_DBW"
        modeDbwName = modeDbwNameStem + csNum  
        modeDbw = smcComponent.createKeyValueSetSymbol( modeDbwName, modeSettingsMenu ) 
        modeDbw.setLabel( bitField_MODE_DBW.getAttribute( "caption" ) )
        modeDbw.setOutputMode( "Key" )
        modeDbw.setDisplayMode( "Description" )
        modeDbw.setDefaultValue( 1 )
        for tupleElem in getNameValueCaptionTuple( "HSMC_MODE0__DBW" ):
            modeDbw.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

        modeBatNameStem = "SMC_MODE_BAT"
        modeBatName = modeBatNameStem + csNum  
        modeBat = smcComponent.createKeyValueSetSymbol( modeBatName, modeSettingsMenu ) 
        modeBat.setLabel( bitField_MODE_BAT.getAttribute( "caption" ) )
        modeBat.setOutputMode( "Key" )
        modeBat.setDisplayMode( "Description" )
        modeBat.setDefaultValue( 1 )
        for tupleElem in getNameValueCaptionTuple( "HSMC_MODE0__BAT" ):
            modeBat.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )
        modeBat.setDependencies( smcModeByteWriteOrSelectAccessVisible, [modeDbwName] )

        modeNWaitNameStem = "SMC_MODE_NWAIT"
        modeNWaitName = modeNWaitNameStem + csNum  
        modeNWait = smcComponent.createKeyValueSetSymbol( modeNWaitName, modeSettingsMenu )
        modeNWait.setLabel( bitField_MODE_EXNW_MODE.getAttribute( "caption" ) )
        modeNWait.setOutputMode( "Key" )
        modeNWait.setDisplayMode( "Description" )
        modeNWait.setDefaultValue( 0 )
        for tupleElem in getNameValueCaptionTuple( "HSMC_MODE0__EXNW_MODE" ):
            modeNWait.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

        # "Read Cycle Configuration"
        readCycleConfiguration = smcComponent.createMenuSymbol( "SMC_READ_CYCLE_CONFIGURATION" + csNum, chipSelectEnable)
        readCycleConfiguration.setLabel( "Read Cycle Configuration" )
        # "Write Cycle Configuration"
        writeCycleConfiguration = smcComponent.createMenuSymbol( "SMC_WRITE_CYCLE_CONFIGURATION" + csNum, chipSelectEnable)
        writeCycleConfiguration.setLabel( "Write Cycle Configuration" )
        #####
        modeReadModeNameStem = "SMC_MODE_READ_MODE"
        modeReadModeName = modeReadModeNameStem + csNum  
        modeReadMode = smcComponent.createKeyValueSetSymbol( modeReadModeName, readCycleConfiguration )
        modeReadMode.setLabel( bitField_MODE_READ_MODE.getAttribute( "caption" ) )
        modeReadMode.setOutputMode( "Key" )
        modeReadMode.setDisplayMode( "Description" )
        modeReadMode.setDefaultValue( 1 )
        for tupleElem in getNameValueCaptionTuple( "HSMC_MODE0__READ_MODE" ):
            modeReadMode.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

        setupNCsRdNameStem = "SMC_SETUP_NCS_RD"
        setupNCsRdName = setupNCsRdNameStem + csNum  
        setupNCsRdCaption = bitField_SETUP_NCS_RD.getAttribute( "caption" )
        setupNCsRd = smcComponent.createIntegerSymbol( setupNCsRdName, readCycleConfiguration)
        setupNCsRd.setLabel( setupNCsRdCaption )
        setupNCsRd.setMin( DEFAULT_SMC_SETUP_MIN_VALUE )
        setupNCsRd.setMax( convertMaskToInt( bitField_SETUP_NCS_RD.getAttribute( "mask" ) ) )
        setupNCsRd.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        pulseNCsRdNameStem = "SMC_PULSE_NCS_RD"
        pulseNCsRdName = pulseNCsRdNameStem + csNum  
        pulseNCsRdCaption = bitField_PULSE_NCS_RD.getAttribute( "caption" )
        pulseNCsRd = smcComponent.createIntegerSymbol( pulseNCsRdName, readCycleConfiguration)
        pulseNCsRd.setLabel( pulseNCsRdCaption )
        pulseNCsRd.setMin( DEFAULT_SMC_PULSE_MIN_VALUE )
        pulseNCsRd.setMax( convertMaskToInt( bitField_PULSE_NCS_RD.getAttribute( "mask" ) ) )
        pulseNCsRd.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        setupNRdNameStem = "SMC_SETUP_NRD"
        setupNRdName = setupNRdNameStem + csNum  
        setupNRdCaption = bitField_SETUP_NRD.getAttribute( "caption" )
        setupNRd = smcComponent.createIntegerSymbol( setupNRdName, readCycleConfiguration)
        setupNRd.setLabel( setupNRdCaption )
        setupNRd.setMin( DEFAULT_SMC_SETUP_MIN_VALUE )
        setupNRd.setMax( convertMaskToInt( bitField_SETUP_NRD.getAttribute( "mask" ) ) )
        setupNRd.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        pulseNRdNameStem = "SMC_PULSE_NRD"
        pulseNRdName = pulseNRdNameStem + csNum  
        pulseNRdCaption = bitField_PULSE_NRD.getAttribute( "caption" )
        pulseNRd = smcComponent.createIntegerSymbol( pulseNRdName, readCycleConfiguration)
        pulseNRd.setLabel( pulseNRdCaption )
        pulseNRd.setMin( DEFAULT_SMC_PULSE_MIN_VALUE )
        pulseNRd.setMax( convertMaskToInt( bitField_PULSE_NRD.getAttribute( "mask" ) ) )
        pulseNRd.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        cycleNRdNameStem = "SMC_CYCLE_NRD"
        cycleNRdName = cycleNRdNameStem + csNum  
        cycleNRdCaption = bitField_CYCLE_NRD.getAttribute( "caption" )
        cycleNRd = smcComponent.createIntegerSymbol( cycleNRdName, readCycleConfiguration )
        cycleNRd.setLabel( cycleNRdCaption )
        cycleNRd.setMin( DEFAULT_SMC_CYCLE_MIN_VALUE )
        cycleNRd.setMax( convertMaskToInt( bitField_CYCLE_NRD.getAttribute( "mask" ) ) )
        cycleNRd.setDefaultValue( DEFAULT_SMC_CYCLE_MIN_VALUE )
        #####
        modeWriteModeNameStem = "SMC_MODE_WRITE_MODE"
        modeWriteModeName = modeWriteModeNameStem + csNum  
        modeWriteMode = smcComponent.createKeyValueSetSymbol( modeWriteModeName, writeCycleConfiguration )
        modeWriteMode.setLabel( bitField_MODE_WRITE_MODE.getAttribute( "caption" ) )
        modeWriteMode.setOutputMode( "Key" )
        modeWriteMode.setDisplayMode( "Description" )
        modeWriteMode.setDefaultValue( 1 )
        for tupleElem in getNameValueCaptionTuple( "HSMC_MODE0__WRITE_MODE" ):
            modeWriteMode.addKey( tupleElem[ 0 ], tupleElem[ 1 ], tupleElem[ 2 ] )

        setupNCsWrNameStem = "SMC_SETUP_NCS_WR"
        setupNCsWrName = setupNCsWrNameStem + csNum  
        setupNCsWrCaption = bitField_SETUP_NCS_WR.getAttribute( "caption" )
        setupNCsWr = smcComponent.createIntegerSymbol( setupNCsWrName, writeCycleConfiguration)
        setupNCsWr.setLabel( setupNCsWrCaption )
        setupNCsWr.setMin( DEFAULT_SMC_SETUP_MIN_VALUE )
        setupNCsWr.setMax( convertMaskToInt( bitField_SETUP_NCS_WR.getAttribute( "mask" ) ) )
        setupNCsWr.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        pulseNCsWrNameStem = "SMC_PULSE_NCS_WR"
        pulseNCsWrName = pulseNCsWrNameStem + csNum  
        pulseNCsWrCaption = bitField_PULSE_NCS_WR.getAttribute( "caption" )
        pulseNCsWr = smcComponent.createIntegerSymbol( pulseNCsWrName, writeCycleConfiguration)
        pulseNCsWr.setLabel( pulseNCsWrCaption )
        pulseNCsWr.setMin( DEFAULT_SMC_PULSE_MIN_VALUE )
        pulseNCsWr.setMax( convertMaskToInt( bitField_PULSE_NCS_WR.getAttribute( "mask" ) ) )
        pulseNCsWr.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        setupNWeNameStem = "SMC_SETUP_NWE"
        setupNWeName = setupNWeNameStem + csNum  
        setupNWeCaption = bitField_SETUP_NWE.getAttribute( "caption" )
        setupNWe = smcComponent.createIntegerSymbol( setupNWeName, writeCycleConfiguration )
        setupNWe.setLabel( setupNWeCaption )
        setupNWe.setMin( DEFAULT_SMC_SETUP_MIN_VALUE )
        setupNWe.setMax( convertMaskToInt( bitField_SETUP_NWE.getAttribute( "mask" ) ) )
        setupNWe.setDefaultValue( DEFAULT_SMC_SETUP_VALUE )

        pulseNWeNameStem = "SMC_PULSE_NWE"
        pulseNWeName = pulseNWeNameStem + csNum  
        pulseNWeCaption = bitField_PULSE_NWE.getAttribute( "caption" )
        pulseNWe = smcComponent.createIntegerSymbol( pulseNWeName, writeCycleConfiguration )
        pulseNWe.setLabel( pulseNWeCaption )
        pulseNWe.setMin( DEFAULT_SMC_PULSE_MIN_VALUE )
        pulseNWe.setMax( convertMaskToInt( bitField_PULSE_NWE.getAttribute( "mask" ) ) )
        pulseNWe.setDefaultValue( DEFAULT_SMC_PULSE_VALUE )

        cycleNWeNameStem = "SMC_CYCLE_NWE"
        cycleNWeName = cycleNWeNameStem + csNum  
        cycleNWeCaption = bitField_CYCLE_NWE.getAttribute( "caption" )
        cycleNWe = smcComponent.createIntegerSymbol( cycleNWeName, writeCycleConfiguration)
        cycleNWe.setLabel( cycleNWeCaption )
        cycleNWe.setMin( DEFAULT_SMC_CYCLE_MIN_VALUE )
        cycleNWe.setMax( convertMaskToInt( bitField_CYCLE_NWE.getAttribute( "mask" ) ) )
        cycleNWe.setDefaultValue( DEFAULT_SMC_CYCLE_MIN_VALUE )
        # Timings register
        timingsMenu = smcComponent.createMenuSymbol( "SMC_TIMINGS" + csNum, chipSelectEnable)
        timingsMenu.setLabel( "Timings" )

        timingsNfSelNameStem = "SMC_TIMINGS_NFSEL"
        timingsNfSelName = timingsNfSelNameStem + csNum  
        timingsNfSel = smcComponent.createBooleanSymbol( timingsNfSelName, timingsMenu)
        timingsNfSel.setLabel( bitField_TIMINGS_NFSEL.getAttribute( "caption" ) )
        timingsNfSel.setDefaultValue( False )

        timingsTwbNameStem = "SMC_TIMINGS_TWB"
        timingsTwbName = timingsTwbNameStem + csNum  
        timingsTwbCaption = bitField_TIMINGS_TWB.getAttribute( "caption" )
        timingsTwb = smcComponent.createIntegerSymbol( timingsTwbName, timingsMenu)
        timingsTwb.setLabel( timingsTwbCaption )
        timingsTwb.setMin( DEFAULT_SMC_TIMINGS_MIN_VALUE )
        timingsTwb.setMax( convertMaskToInt( bitField_TIMINGS_TWB.getAttribute( "mask" ) ) )
        timingsTwb.setDefaultValue( DEFAULT_SMC_TIMINGS_VALUE )

        timingsTrrNameStem = "SMC_TIMINGS_TRR"
        timingsTrrName = timingsTrrNameStem + csNum  
        timingsTrrCaption = bitField_TIMINGS_TRR.getAttribute( "caption" )
        timingsTrr = smcComponent.createIntegerSymbol( timingsTrrName, timingsMenu)
        timingsTrr.setLabel( timingsTrrCaption )
        timingsTrr.setMin( DEFAULT_SMC_TIMINGS_MIN_VALUE )
        timingsTrr.setMax( convertMaskToInt( bitField_TIMINGS_TRR.getAttribute( "mask" ) ) )
        timingsTrr.setDefaultValue( DEFAULT_SMC_TIMINGS_VALUE )

        timingsOcmsNameStem = "SMC_TIMINGS_OCMS"
        timingsOcmsName = timingsOcmsNameStem + csNum  
        timingsOcms = smcComponent.createBooleanSymbol( timingsOcmsName, timingsMenu )
        timingsOcms.setLabel( bitField_TIMINGS_OCMS.getAttribute( "caption" ) )
        timingsOcms.setDefaultValue( False )

        timingsTarNameStem = "SMC_TIMINGS_TAR"
        timingsTarName = timingsTarNameStem + csNum  
        timingsTarCaption = bitField_TIMINGS_TAR.getAttribute( "caption" )
        timingsTar = smcComponent.createIntegerSymbol( timingsTarName, timingsMenu)
        timingsTar.setLabel( timingsTarCaption )
        timingsTar.setMin( DEFAULT_SMC_TIMINGS_MIN_VALUE )
        timingsTar.setMax( convertMaskToInt( bitField_TIMINGS_TAR.getAttribute( "mask" ) ) )
        timingsTar.setDefaultValue( DEFAULT_SMC_TIMINGS_VALUE )

        timingsTadlNameStem = "SMC_TIMINGS_TADL"
        timingsTadlName = timingsTadlNameStem + csNum  
        timingsTadlCaption = bitField_TIMINGS_TADL.getAttribute( "caption" )
        timingsTadl = smcComponent.createIntegerSymbol( timingsTadlName, timingsMenu )
        timingsTadl.setLabel( timingsTadlCaption )
        timingsTadl.setMin( DEFAULT_SMC_TIMINGS_MIN_VALUE )
        timingsTadl.setMax( convertMaskToInt( bitField_TIMINGS_TADL.getAttribute( "mask" ) ) )
        timingsTadl.setDefaultValue( DEFAULT_SMC_TIMINGS_VALUE )

        timingsTclrNameStem = "SMC_TIMINGS_TCLR"
        timingsTclrName = timingsTclrNameStem + csNum  
        timingsTclrCaption = bitField_TIMINGS_TCLR.getAttribute( "caption" )
        timingsTclr = smcComponent.createIntegerSymbol( timingsTclrName, timingsMenu)
        timingsTclr.setLabel( timingsTclrCaption )
        timingsTclr.setMin( DEFAULT_SMC_TIMINGS_MIN_VALUE )
        timingsTclr.setMax( convertMaskToInt( bitField_TIMINGS_TCLR.getAttribute( "mask" ) ) )
        timingsTclr.setDefaultValue( DEFAULT_SMC_TIMINGS_VALUE )
    # ----- 
    offChipMemoryScramblingMenu = smcComponent.createMenuSymbol( "SMC_OCMS_MENU", None )
    offChipMemoryScramblingMenu.setLabel( "Off Chip Memory Scrambling" )
    ocmsScramblingEnable = smcComponent.createBooleanSymbol( "SMC_OCMS_SCRAMBLING_ENABLE", offChipMemoryScramblingMenu )
    ocmsScramblingEnable.setLabel( bitField_OCMS_SMSE.getAttribute( "caption" ) )
    ocmsSramScramblingEnable = smcComponent.createBooleanSymbol( "SMC_OCMS_SRAM_SCRAMBLING_ENABLE", offChipMemoryScramblingMenu )
    ocmsSramScramblingEnable.setLabel( bitField_OCMS_SRSE.getAttribute( "caption" ) )
    scramblingKey1 = smcComponent.createHexSymbol( "SMC_KEY1", offChipMemoryScramblingMenu )
    scramblingKey1.setLabel( bitField_KEY1_KEY1.getAttribute( "caption" ) )
    scramblingKey2 = smcComponent.createHexSymbol( "SMC_KEY2", offChipMemoryScramblingMenu )
    scramblingKey2.setLabel( bitField_KEY2_KEY2.getAttribute( "caption" ) )
    writeProtectionEnable = smcComponent.createBooleanSymbol( "SMC_WRITE_PROTECTION", None )
    writeProtectionEnable.setLabel( bitField_WPMR_WPEN.getAttribute( "caption" ) )
    writeProtectionEnable.setDefaultValue( False )

    #------------------------------------------------------------------------------
    # Dependency
    #------------------------------------------------------------------------------
    # Enable Peripheral Clock in Clock manager
    Database.setSymbolValue(    "core", myNamespace.upper() + "_CLOCK_ENABLE", True, 2 ) 
    #------------------------------------------------------------------------------
    # Code Generation
    #------------------------------------------------------------------------------
    configName = Variables.get( "__CONFIGURATION_NAME" )

    smcHeaderFile = smcComponent.createFileSymbol( "PLIB_SMC_H", None)
    smcHeaderFile.setSourcePath( "../peripheral/smc_11036/templates/plib_smc.h.ftl" )
    smcHeaderFile.setOutputName( "plib_" + myNamespace.lower() + ".h" )
    smcHeaderFile.setDestPath( "/peripheral/smc/" )
    smcHeaderFile.setProjectPath( "config/" + configName + "/peripheral/smc/" )
    smcHeaderFile.setType( "HEADER" )
    smcHeaderFile.setMarkup( True )

    smcSource1File = smcComponent.createFileSymbol( "PLIB_SMC_C", None)
    smcSource1File.setSourcePath( "../peripheral/smc_11036/templates/plib_smc.c.ftl" )
    smcSource1File.setOutputName( "plib_" + myNamespace.lower() + ".c" )
    smcSource1File.setDestPath( "/peripheral/smc/" )
    smcSource1File.setProjectPath( "config/" + configName + "/peripheral/smc/" )
    smcSource1File.setType( "SOURCE" )
    smcSource1File.setMarkup( True )

    # Add SMC related code to common files
    smcHeaderFileEntry = smcComponent.createFileSymbol( "PLIB_SMC_DEFINITIONS_H", None)
    smcHeaderFileEntry.setType( "STRING" )
    smcHeaderFileEntry.setOutputName( "core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES" )
    smcHeaderFileEntry.setSourcePath( "../peripheral/smc_11036/templates/system/definitions.h.ftl" )
    smcHeaderFileEntry.setMarkup( True )

    smcSystemInitFile = smcComponent.createFileSymbol( "PLIB_SMC_INITIALIZE_H", None)
    smcSystemInitFile.setType( "STRING" )
    smcSystemInitFile.setOutputName( "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS" )
    smcSystemInitFile.setSourcePath( "../peripheral/smc_11036/templates/system/initialization.c.ftl" )
    smcSystemInitFile.setMarkup( True )

