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
#### Global Variables ####
################################################################################
global hemcInstanceName
global hsdramcSym_CR__NR
global hsdramcSym_BURST_TYPE
global hsdramcSym_BURST_LENGTH
global hsdramcSym_CR_CAS
global hsmcCSmenu
hsmcCSmenu = []
global useHSDRAM
global commentHSDRAM
global hsdramcSymMenu_MR_MENU
global hsdramcSymMenu_features
global hsdramcSymMenu_TIMING_MENU
global useHSMC
useHSMC = []
global sdRamcs
sdRamcs = None

################################################################################
#### Register Information ####
################################################################################
ValGrp_CR__NC = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSDRAMC"]/value-group@[name="HSDRAMC_CR__NC"]')
ValGrp_CR__NR = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSDRAMC"]/value-group@[name="HSDRAMC_CR__NR"]')
ValGrp_CR__NB = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSDRAMC"]/value-group@[name="HSDRAMC_CR__NB"]')
ValGrp_CR_Banksize = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HEMC"]/value-group@[name="HEMC_CR_NCS__BANKSIZE"]')
ComboVal_CR_DBW = ["16-bits", "32-bits"]
ComboVal_BURST_TYPE = ["SEQUENTIAL", "INTERLEAVED"]

################################################################################
#### Default values and constants ####
################################################################################
# Burst Length
HSDRAMC_DEFAULT_MIN_VALUE = 0
HSDRAMC_BURST_LENGHT_MAX_VALUE = 7

# SDRAM Timing parameters default values
HSDRAMC_CR_CAS_DEFAULT_VALUE = 3
HSDRAMC_SDR_TWR_DEFAULT_VALUE = 2
HSDRAMC_SDR_TRC_TRFC_DEFAULT_VALUE = 6
HSDRAMC_SDR_TRP_DEFAULT_VALUE = 2
HSDRAMC_SDR_TRCD_DEFAULT_VALUE = 2
HSDRAMC_SDR_TRAS_DEFAULT_VALUE = 5
HSDRAMC_SDR_TXSR_DEFAULT_VALUE = 7

HSDRAMC_CFR1_TMRD_DEFAULT_VALUE = 2
HSDRAMC_REFRESH_TIME_IN_MS_DEFAULT_VALUE = 16

chipSelectCount = 6

################################################################################
#### Business Logic ####
################################################################################

# Function to calculate refresh count
def hideMenus(symbol, event):
    global hsmcCSmenu
    global useHSMC
    global useHSDRAM
    global commentHSDRAM
    global hsdramcSymMenu_MR_MENU
    global hsdramcSymMenu_features
    global hsdramcSymMenu_TIMING_MENU
    global chipSelectCount

    sdRamcs = None
    for id in range(0, chipSelectCount):
        if int(Database.getSymbolValue(event["namespace"], "CS_" + str(id) + "_MEMORY_TYPE")) == 1:
            sdRamcs = id
            if useHSDRAM.getValue() == False:
                commentHSDRAM.setVisible(False)
                useHSDRAM.setValue(True)
                hsdramcSymMenu_MR_MENU.setVisible(True)
                hsdramcSymMenu_features.setVisible(True)
                hsdramcSymMenu_TIMING_MENU.setVisible(True)
            useHSMC[id].setValue(False)
            hsmcCSmenu[id].setVisible(False)
        else:
            useHSMC[id].setValue(True)
            hsmcCSmenu[id].setVisible(True)
    
    if sdRamcs == None:
        commentHSDRAM.setVisible(True)
        useHSDRAM.setValue(False)
        #hsdramcSymMenu_MR_MENU.setVisible(False)
        hsdramcSymMenu_features.setVisible(False)
        hsdramcSymMenu_TIMING_MENU.setVisible(False)


    



def calcRefreshCount(time, rowlines, clk):
    rowlines = rowlines[-2:]
    rowlines = int(rowlines)
    rows = 2**rowlines
    count = time*(clk/rows)/1000
    return count

# Function to set label based on the Refresh time in ms as selected in Combo Symbol HSDRAMC_CR_NR


def calcRefreshCount_CB(symbol, event):
    global hemcInstanceName
    global hsdramcSym_CR__NR
    clk = int(Database.getSymbolValue("core", hemcInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    time = Database.getSymbolValue(hemcInstanceName.getValue().lower(), "HSDRAMC_REFRESH_TIME_IN_MS")
    rowlines = hsdramcSym_CR__NR.getSelectedKey()
    count = calcRefreshCount(time, rowlines, clk)
    symbol.clearValue()
    symbol.setValue(count, 1)

# MRS<2:0>  -> Burst Length
# MRS<3>    -> Burst Type
# MRS<6:4>  -> CAS Latency


def calcMRS(symbol, event):
    type = hsdramcSym_BURST_TYPE.getValue()
    length = hsdramcSym_BURST_LENGTH.getValue()
    cas = hsdramcSym_CR_CAS.getValue()
    if(type == "INTERLEAVED"):
        mrs = 8+(16 * cas) + length
    else:
        mrs = (16 * cas) + length
    symbol.setValue(mrs, 1)


############################################################# HSMC ###################################################
# Function to convert Bitfield mask string to Integer
def hsmcConvertMaskToInt( aRegMask ):
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


# Dependency function definition to enable visibility based on selection of Page Mode Enable
def hsmcMemoryPageSizeModeVisible(symbol, event):
    id = symbol.getID()[-1]
    hsmcChipSelNum = int(id)

    if (event["value"] == True):
        hsmcSym_MODE_PS[hsmcChipSelNum].setVisible(True)
    else :
        hsmcSym_MODE_PS[hsmcChipSelNum].setVisible(False)

# Dependency functions definitions to enable visibility based on selection of TDF Optimization
def hsmcTdfCyclesModeVisible(symbol, event):
    id = symbol.getID()[-1]
    hsmcChipSelNum = int(id)

    if (event["value"] == True):
        hsmcSym_MODE_TDF_CYCLES[hsmcChipSelNum].setVisible(True)
    else :
        hsmcSym_MODE_TDF_CYCLES[hsmcChipSelNum].setVisible(False)


# Dependency function definition to enable visibility based on selection of Byte Access Type
def hsmcByteAccessSelModeVisible(symbol, event):
    symObj = event["symbol"]
    id = symbol.getID()[-1]
    hsmcChipSelNum = int(id)

    if (symObj.getSelectedKey() == "HSMC_MODE_DBW_16_BIT"):
        hsmcSym_MODE_BAT[hsmcChipSelNum].setVisible(True)
    else :
        hsmcSym_MODE_BAT[hsmcChipSelNum].setVisible(False)

################################################################################
#### Component ####
################################################################################


def instantiateComponent(hemcComponent):
    global hsmcCSmenu
    global hemcInstanceName
    global hsdramcSym_CR__NR
    global hsdramcSym_BURST_TYPE
    global hsdramcSym_BURST_LENGTH
    global hsdramcSym_CR_CAS
    global useHSDRAM
    global commentHSDRAM
    global hsdramcSymMenu_MR_MENU
    global hsdramcSymMenu_features
    global hsdramcSymMenu_TIMING_MENU
    global useHSMC

    hemcInstanceName = hemcComponent.createStringSymbol("HEMC_INSTANCE_NAME", None)
    hemcInstanceName.setVisible(False)
    hemcInstanceName.setDefaultValue(hemcComponent.getID().upper())

    hsdramcInstanceName = hemcComponent.createStringSymbol("HSDRAMC_INSTANCE_NAME", None)
    hsdramcInstanceName.setVisible(False)
    hsdramcInstanceName.setDefaultValue("HSDRAMC")

    hsmcInstanceName = hemcComponent.createStringSymbol("HSMC_INSTANCE_NAME", None)
    hsmcInstanceName.setVisible(False)
    hsmcInstanceName.setDefaultValue("HSMC")

    memMemu = hemcComponent.createMenuSymbol("MEMORY_MENU", None)
    memMemu.setLabel("HEMC Memory Configuration Menu")

    sdramMenu = hemcComponent.createMenuSymbol("HSDRAMC_MENU", None)
    sdramMenu.setLabel("HSDRAM Controller Menu")

    hsmcMenu = hemcComponent.createMenuSymbol("HSMC_MENU", None)
    hsmcMenu.setLabel("HSMC Menu")

    csDependencies = []
############################################## Memory configuration ################################################

    for id in range(0, chipSelectCount):
        csMenu = hemcComponent.createMenuSymbol("CS_" + str(id) + "_MEMORY_MENU", memMemu)
        csMenu.setLabel("Chip Select " + str(id) + " Memory Configuration")

        csBase = hemcComponent.createHexSymbol("CS_" + str(id) + "_MEMORY_BASE", csMenu)
        csBase.setLabel("Relative Base Address")
        csBase.setDefaultValue(0x3ffff)

        csType = hemcComponent.createKeyValueSetSymbol("CS_" + str(id) + "_MEMORY_TYPE", csMenu)
        csType.setLabel("Memory Type")
        csType.setOutputMode("Value")
        csType.setDisplayMode("Description")
        csType.addKey("HSMC", "0", "HSMC (PROM or SRAM) is connected")
        csType.addKey("SDRAMC", "1", "SDRAMC is connected")
        csDependencies.append("CS_" + str(id) + "_MEMORY_TYPE")
        
        csStart = hemcComponent.createHexSymbol("CS_" + str(id) + "_START_ADDRESS", csMenu)
        csStart.setLabel("Start  Address")
        csStart.setDefaultValue(0x60000000)
        csStart.setVisible(False)
        
        csEnd = hemcComponent.createHexSymbol("CS_" + str(id) + "_END_ADDRESS", csMenu)
        csEnd.setLabel("End  Address")
        csEnd.setDefaultValue(0x60000000)
        csEnd.setVisible(False)

        csBankSize = hemcComponent.createKeyValueSetSymbol("CS_" + str(id) + "_MEMORY_BANK_SIZE", csMenu)
        csBankSize.setLabel("Bank Size")
        csBankSize.setOutputMode("Value")
        csBankSize.setDisplayMode("Description")
        value = ValGrp_CR_Banksize.getChildren()
        for id in range(0, len(value)):
            csBankSize.addKey(value[id].getAttribute("name"), str(value[id].getAttribute("value")), value[id].getAttribute("caption"))
        csBankSize.setDefaultValue(17)

################################################ SDRAM Configuration ###############################################
    cpuclk = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    cpuclk = int(cpuclk)

    hsdramcSymClkFreq = hemcComponent.createIntegerSymbol("HSDRAMC_CPU_CLK_FREQ", sdramMenu)
    hsdramcSymClkFreq.setLabel("Get Core Clock Frequency")
    hsdramcSymClkFreq.setVisible(False)
    hsdramcSymClkFreq.setDefaultValue(cpuclk)

    useHSDRAM = hemcComponent.createBooleanSymbol("USE_HSDRAM", None)
    useHSDRAM.setVisible(False)

    commentHSDRAM = hemcComponent.createCommentSymbol("HSDRAM_COMPONENT", sdramMenu)
    commentHSDRAM.setLabel("/* Use HEMC Memory Configuration Menu to configure one of the Chip Select to use SDRAM")

    # HSDRAMC Features
    hsdramcSymMenu_features = hemcComponent.createMenuSymbol("HSDRAMC_FEATURE_MENU", sdramMenu)
    hsdramcSymMenu_features.setLabel("Configure SDRAM features")
    hsdramcSymMenu_features.setVisible(False)

    sdRamStartAddress = hemcComponent.createHexSymbol("SDRAMC_START_ADDRESS", hsdramcSymMenu_features)
    sdRamStartAddress.setLabel("SDRAMC Start Address")
    sdRamStartAddress.setDefaultValue(0x60000000)

    hsdramcSym_CR__NR = hemcComponent.createKeyValueSetSymbol("HSDRAMC_CR__NR", hsdramcSymMenu_features)
    hsdramcSym_CR__NR.setOutputMode("Key")
    hsdramcSym_CR__NR.setDisplayMode("Description")
    hsdramcSym_CR__NR.setLabel("Number of Row Bits")
    value = ValGrp_CR__NR.getChildren()
    for id in range(0, len(value)):
        hsdramcSym_CR__NR.addKey(value[id].getAttribute("name"), str(value[id].getAttribute("value")), value[id].getAttribute("caption"))
    hsdramcSym_CR__NR.setSelectedKey("ROW13", 2)

    hsdramcSym_CR__NC = hemcComponent.createKeyValueSetSymbol("HSDRAMC_CR__NC", hsdramcSymMenu_features)
    hsdramcSym_CR__NC.setOutputMode("Key")
    hsdramcSym_CR__NC.setDisplayMode("Description")
    hsdramcSym_CR__NC.setLabel("Number of Column Bits")
    value = ValGrp_CR__NC.getChildren()
    for id in range(0, len(value)):
        hsdramcSym_CR__NC.addKey(value[id].getAttribute("name"), str(value[id].getAttribute("value")), value[id].getAttribute("caption"))
    hsdramcSym_CR__NC.setSelectedKey("COL9", 2)

    hsdramcSym_CR__NB = hemcComponent.createKeyValueSetSymbol("HSDRAMC_CR__NB", hsdramcSymMenu_features)
    hsdramcSym_CR__NB.setOutputMode("Key")
    hsdramcSym_CR__NB.setDisplayMode("Description")
    hsdramcSym_CR__NB.setLabel("Number of Banks")
    value = ValGrp_CR__NB.getChildren()
    for id in range(0, len(value)):
        hsdramcSym_CR__NB.addKey(value[id].getAttribute("name"), str(value[id].getAttribute("value")), value[id].getAttribute("caption"))
    hsdramcSym_CR__NB.setSelectedKey("BANK4", 2)

    hsdramcSym_CR_DBW = hemcComponent.createComboSymbol("HSDRAMC_CR_DBW", hsdramcSymMenu_features, ComboVal_CR_DBW)
    hsdramcSym_CR_DBW.setLabel("Data Bus Width")
    hsdramcSym_CR_DBW.setDefaultValue("32-bits")
    hsdramcSym_CR_DBW.setReadOnly(False)

    # HSDRAMC Timing Parameters
    hsdramcSymMenu_TIMING_MENU = hemcComponent.createMenuSymbol("HSDRAMC_TIMING_MENU", sdramMenu)
    hsdramcSymMenu_TIMING_MENU.setLabel("Configure SDRAM Timing Parameters")
    hsdramcSymMenu_TIMING_MENU.setVisible(False)

    hsdramcSym_CR_TRCD = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TRCD", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TRCD.setLabel("Row Active to Column Read/Write Delay (TRCD)")
    hsdramcSym_CR_TRCD.setMin(0)
    hsdramcSym_CR_TRCD.setMax(15)
    hsdramcSym_CR_TRCD.setDefaultValue(HSDRAMC_SDR_TRCD_DEFAULT_VALUE)

    hsdramcSym_CR_CAS = hemcComponent.createIntegerSymbol("HSDRAMC_CR_CAS", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_CAS.setLabel("CAS Latency (TCAS)")
    hsdramcSym_CR_CAS.setMin(1)
    hsdramcSym_CR_CAS.setMax(3)
    hsdramcSym_CR_CAS.setDefaultValue(HSDRAMC_CR_CAS_DEFAULT_VALUE)

    hsdramcSym_CR_TRAS = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TRAS", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TRAS.setLabel("Row Active to Precharge Delay(RAS)")
    hsdramcSym_CR_TRAS.setMin(0)
    hsdramcSym_CR_TRAS.setMax(15)
    hsdramcSym_CR_TRAS.setDefaultValue(HSDRAMC_SDR_TRAS_DEFAULT_VALUE)

    hsdramcSym_CR_TRP = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TRP", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TRP.setLabel("Row Precharge Delay (TRP)")
    hsdramcSym_CR_TRP.setMin(0)
    hsdramcSym_CR_TRP.setMax(15)
    hsdramcSym_CR_TRP.setDefaultValue(HSDRAMC_SDR_TRP_DEFAULT_VALUE)

    hsdramcSym_CR_TRC_TRFC = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TRC_TRFC", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TRC_TRFC.setLabel("Row Cycle Delay/Row Refresh Cycle(TRC_TRFC)")
    hsdramcSym_CR_TRC_TRFC.setMin(0)
    hsdramcSym_CR_TRC_TRFC.setMax(15)
    hsdramcSym_CR_TRC_TRFC.setDefaultValue(HSDRAMC_SDR_TRC_TRFC_DEFAULT_VALUE)

    hsdramcSym_CR_TWR = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TWR", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TWR.setLabel("Write Recovery Delay (TWR)")
    hsdramcSym_CR_TWR.setMin(0)
    hsdramcSym_CR_TWR.setMax(15)
    hsdramcSym_CR_TWR.setDefaultValue(HSDRAMC_SDR_TWR_DEFAULT_VALUE)

    hsdramcSym_CFR1_TMRD = hemcComponent.createIntegerSymbol("HSDRAMC_CFR1_TMRD", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CFR1_TMRD.setLabel("Mode Register Set to Command Delay Time(TMRD)")
    hsdramcSym_CFR1_TMRD.setMin(0)
    hsdramcSym_CFR1_TMRD.setMax(15)
    hsdramcSym_CFR1_TMRD.setDefaultValue(HSDRAMC_CFR1_TMRD_DEFAULT_VALUE)

    hsdramcSym_REFRESH_TIME_IN_MS = hemcComponent.createIntegerSymbol("HSDRAMC_REFRESH_TIME_IN_MS", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_REFRESH_TIME_IN_MS.setLabel("Refresh time in ms")
    hsdramcSym_REFRESH_TIME_IN_MS.setDefaultValue(HSDRAMC_REFRESH_TIME_IN_MS_DEFAULT_VALUE)

    clk = int(Database.getSymbolValue("core", hemcInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    count = calcRefreshCount(HSDRAMC_REFRESH_TIME_IN_MS_DEFAULT_VALUE, "ROW13", clk)

    hsdramcSym_HSDRAMC_TR_COUNT = hemcComponent.createIntegerSymbol("HSDRAMC_TR_COUNT", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_HSDRAMC_TR_COUNT.setDependencies(calcRefreshCount_CB, ["HSDRAMC_REFRESH_TIME_IN_MS", "core." + hemcInstanceName.getValue() + "_CLOCK_FREQUENCY"])
    hsdramcSym_HSDRAMC_TR_COUNT.setDefaultValue(count)
    hsdramcSym_HSDRAMC_TR_COUNT.setVisible(False)

    hsdramcSym_CR_TXSR = hemcComponent.createIntegerSymbol("HSDRAMC_SDR_TXSR", hsdramcSymMenu_TIMING_MENU)
    hsdramcSym_CR_TXSR.setLabel("Exit Self Refresh to Active Time (TXSR)")
    hsdramcSym_CR_TXSR.setMin(0)
    hsdramcSym_CR_TXSR.setMax(15)
    hsdramcSym_CR_TXSR.setDefaultValue(HSDRAMC_SDR_TXSR_DEFAULT_VALUE)

    # HSDRAMC Mode Configuration
    hsdramcSymMenu_MR_MENU = hemcComponent.createMenuSymbol("HSDRAMC_MR_MENU", sdramMenu)
    hsdramcSymMenu_MR_MENU.setLabel("HSDRAMC Mode Register Configurations")
    hsdramcSymMenu_MR_MENU.setVisible(False)

    hsdramcSym_BURST_LENGTH = hemcComponent.createIntegerSymbol("HSDRAMC_BURST_LENGTH", hsdramcSymMenu_MR_MENU)
    hsdramcSym_BURST_LENGTH.setLabel("Burst Length")
    hsdramcSym_BURST_LENGTH.setMin(HSDRAMC_DEFAULT_MIN_VALUE)
    hsdramcSym_BURST_LENGTH.setMax(HSDRAMC_BURST_LENGHT_MAX_VALUE)
    hsdramcSym_BURST_LENGTH.setDefaultValue(HSDRAMC_DEFAULT_MIN_VALUE)

    hsdramcSym_BURST_TYPE = hemcComponent.createComboSymbol("HSDRAMC_BURST_TYPE", hsdramcSymMenu_MR_MENU, ComboVal_BURST_TYPE)
    hsdramcSym_BURST_TYPE.setLabel("Burst Type")
    hsdramcSym_BURST_TYPE.setDefaultValue("SEQUENTIAL")

    hsdramcSym_MRS = hemcComponent.createHexSymbol("HSDRAMC_MRS_VALUE", hsdramcSymMenu_MR_MENU)
    hsdramcSym_MRS.setDependencies(calcMRS, ["HSDRAMC_BURST_TYPE", "HSDRAMC_BURST_LENGTH", "HSDRAMC_CR_CAS"])
    hsdramcSym_MRS.setVisible(False)

##################################################### HSMC Configuration #################################################################

    # Get HSMC ID
    hsmcRegModule    = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"HSMC\"]")
    hsmcRegModuleID  = hsmcRegModule.getAttribute("id")

    #------------------------------------------------------------------------------
    #          ATDF Read to get HSMC Register | Bitfield | Mask | Value Group
    #------------------------------------------------------------------------------
    # HSMC_SETUP Register Bitfield Names and Mask
    hsmcRegBitField_SETUP_NWE_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_SETUP0"]/bitfield@[name="NWE_SETUP"]')
    hsmcRegBitField_SETUP_NCS_WR_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_SETUP0"]/bitfield@[name="NCS_WR_SETUP"]')
    hsmcRegBitField_SETUP_NRD_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_SETUP0"]/bitfield@[name="NRD_SETUP"]')
    hsmcRegBitField_SETUP_NCS_RD_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_SETUP0"]/bitfield@[name="NCS_RD_SETUP"]')

    # HSMC_PULSE Register Bitfield Names and Mask
    hsmcRegBitField_PULSE_NWE_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_PULSE0"]/bitfield@[name="NWE_PULSE"]')
    hsmcRegBitField_PULSE_NCS_WR_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_PULSE0"]/bitfield@[name="NCS_WR_PULSE"]')
    hsmcRegBitField_PULSE_NRD_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_PULSE0"]/bitfield@[name="NRD_PULSE"]')
    hsmcRegBitField_PULSE_NCS_RD_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_PULSE0"]/bitfield@[name="NCS_RD_PULSE"]')

    # HSMC_CYCLE Register Bitfield Names and Mask
    hsmcRegBitField_CYCLE_NWE_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_CYCLE0"]/bitfield@[name="NWE_CYCLE"]')
    hsmcRegBitField_CYCLE_NRD_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_CYCLE0"]/bitfield@[name="NRD_CYCLE"]')

    # HSMC_Mode Register Bitfield Names and Mask
    hsmcRegBitField_MODE_TDF_CYCLES      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="HSMC"]/register-group@[name="HSMC"]/register@[name="HSMC_MODE0"]/bitfield@[name="TDF_CYCLES"]')

    #------------------------------------------------------------------------------
    #                     Global HSMC Array sysmbol declaration
    #------------------------------------------------------------------------------
    hsmcSym_MODE_BAT = []
    hsmcSym_MODE_PS = []
    hsmcSym_MODE_TDF_CYCLES = []

    #------------------------------------------------------------------------------
    #                               Global Variables
    #------------------------------------------------------------------------------

    # Get the Chip Select Count from ATDF config file
    global hsmcChipSelCount

    #------------------------------------------------------------------------------
    #                                   Constatns
    #------------------------------------------------------------------------------

    # Min Zero Value
    HSMC_DEFAULT_MIN_VALUE               = 0

    # Deafult value for HSMC Setup Register
    HSMC_SETUP_DEFAULT_VALUE             = 16

    # Deafult value for HSMC Pulse Register
    HSMC_PULSE_DEFAULT_VALUE             = 16

    # Deafult value for HSMC Cycle Register
    HSMC_CYCLE_DEFAULT_VALUE             = 3

    # Deafult value for HSMC MODE TDF CYCLE Register
    HSMC_MODE_TDF_CYCLES_DEFAULT_VALUE   = 0

    print"--------------------------------------------------------------------"
    print("************************** Running " + hsmcInstanceName.getValue() + " ****************************")
    print"--------------------------------------------------------------------"

    hsmcChipSelCount = chipSelectCount

    print("Total available HSMC Chip Select Count is : " + str(hsmcChipSelCount))

    # HSMC Global features
    hsmcSym_GlobalMenu= hemcComponent.createMenuSymbol("HSMC_GLOBAL_MENU", hsmcMenu)
    hsmcSym_GlobalMenu.setLabel("HSMC Global Features")

    hsmcSym_WPMR_WPEN = hemcComponent.createBooleanSymbol("HSMC_WRITE_PROTECTION", hsmcSym_GlobalMenu)
    hsmcSym_WPMR_WPEN.setLabel("Enable Write Protection")
    hsmcSym_WPMR_WPEN.setDefaultValue(False)

    #--------------------------------------------------------------------------
    # HSMC Chip Select Selection and Settings
    #--------------------------------------------------------------------------
    hsmcSym_Chip_Select = hemcComponent.createMenuSymbol("HSMC_CHIP_SELECT", hsmcMenu)
    hsmcSym_Chip_Select.setLabel("HSMC Chip Select Selection and Settings")

    hsmcSym_CS_COUNT = hemcComponent.createIntegerSymbol("HSMC_CHIP_SELECT_COUNT", hsmcSym_Chip_Select)
    hsmcSym_CS_COUNT.setDefaultValue(hsmcChipSelCount)
    hsmcSym_CS_COUNT.setVisible(False)

    for hsmcChipSelNum in range(0, hsmcChipSelCount):
        hsmcSym_CS = hemcComponent.createBooleanSymbol("HSMC_CHIP_SELECT" + str(hsmcChipSelNum), hsmcSym_Chip_Select)
        hsmcSym_CS.setLabel("Enable Chip Select "+ str(hsmcChipSelNum))
        hsmcCSmenu.append(hsmcSym_CS)

        hsmcInUse = hemcComponent.createBooleanSymbol("USE_HSMC_" + str(hsmcChipSelNum), hsmcSym_Chip_Select)
        hsmcInUse.setDefaultValue(True)
        hsmcInUse.setVisible(False)
        useHSMC.append(hsmcInUse)
        # HSMC Read Setup, Pulse and Cycle Timings
        hsmcSym_READ_TIMING_CS = hemcComponent.createMenuSymbol("HSMC_SETUP_TIMING_CS" + str(hsmcChipSelNum), hsmcSym_CS)
        hsmcSym_READ_TIMING_CS.setLabel("Read Cycle Timings")

        # HSMC Read Setup Timings
        hsmcSym_SETUP_NRD_CS = hemcComponent.createIntegerSymbol("HSMC_NRD_SETUP_CS" + str(hsmcChipSelNum), hsmcSym_READ_TIMING_CS)
        hsmcSym_SETUP_NRD_CS.setLabel(hsmcRegBitField_SETUP_NRD_SETUP.getAttribute("caption"))
        hsmcSym_SETUP_NRD_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_SETUP_NRD_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_SETUP_NRD_SETUP.getAttribute("mask")))
        hsmcSym_SETUP_NRD_CS.setDefaultValue(HSMC_SETUP_DEFAULT_VALUE)

        hsmcSym_SETUP_NCS_RD_CS = hemcComponent.createIntegerSymbol("HSMC_NCS_RD_SETUP_CS" + str(hsmcChipSelNum), hsmcSym_READ_TIMING_CS)
        hsmcSym_SETUP_NCS_RD_CS.setLabel(hsmcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("caption"))
        hsmcSym_SETUP_NCS_RD_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_SETUP_NCS_RD_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("mask")))
        hsmcSym_SETUP_NCS_RD_CS.setDefaultValue(HSMC_SETUP_DEFAULT_VALUE)

        # HSMC Read Pulse Timings
        hsmcSym_PULSE_NRD_CS = hemcComponent.createIntegerSymbol("HSMC_NRD_PULSE_CS" + str(hsmcChipSelNum), hsmcSym_READ_TIMING_CS)
        hsmcSym_PULSE_NRD_CS.setLabel(hsmcRegBitField_PULSE_NRD_PULSE.getAttribute("caption"))
        hsmcSym_PULSE_NRD_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_PULSE_NRD_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_PULSE_NRD_PULSE.getAttribute("mask")))
        hsmcSym_PULSE_NRD_CS.setDefaultValue(HSMC_PULSE_DEFAULT_VALUE)

        hsmcSym_PULSE_NCS_RD_CS = hemcComponent.createIntegerSymbol("HSMC_NCS_RD_PULSE_CS" + str(hsmcChipSelNum),hsmcSym_READ_TIMING_CS)
        hsmcSym_PULSE_NCS_RD_CS.setLabel(hsmcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("caption"))
        hsmcSym_PULSE_NCS_RD_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_PULSE_NCS_RD_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("mask")))
        hsmcSym_PULSE_NCS_RD_CS.setDefaultValue(HSMC_PULSE_DEFAULT_VALUE)

        # HSMC Read Cycle Timings
        hsmcSym_HSMC_CYCLE_TIMING_NRD_CS = hemcComponent.createIntegerSymbol("HSMC_NRD_CYCLE_CS" + str(hsmcChipSelNum), hsmcSym_READ_TIMING_CS)
        hsmcSym_HSMC_CYCLE_TIMING_NRD_CS.setLabel(hsmcRegBitField_CYCLE_NRD_CYCLE.getAttribute("caption"))
        hsmcSym_HSMC_CYCLE_TIMING_NRD_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_HSMC_CYCLE_TIMING_NRD_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_CYCLE_NRD_CYCLE.getAttribute("mask")))
        hsmcSym_HSMC_CYCLE_TIMING_NRD_CS.setDefaultValue(HSMC_CYCLE_DEFAULT_VALUE)

        # HSMC Write Setup, Pulse and Cycle Timings
        hsmcSym_WRITE_TIMING_CS = hemcComponent.createMenuSymbol("HSMC_PULSE_TIMING_CS" + str(hsmcChipSelNum), hsmcSym_CS)
        hsmcSym_WRITE_TIMING_CS.setLabel("Write Cycle Timings")

        # HSMC Write Setup Timings
        hsmcSym_SETUP_NWE_CS = hemcComponent.createIntegerSymbol("HSMC_NWE_SETUP_CS" + str(hsmcChipSelNum), hsmcSym_WRITE_TIMING_CS)
        hsmcSym_SETUP_NWE_CS.setLabel(hsmcRegBitField_SETUP_NWE_SETUP.getAttribute("caption"))
        hsmcSym_SETUP_NWE_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_SETUP_NWE_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_SETUP_NWE_SETUP.getAttribute("mask")))
        hsmcSym_SETUP_NWE_CS.setDefaultValue(HSMC_SETUP_DEFAULT_VALUE)

        hsmcSym_SETUP_NCS_WR_CS = hemcComponent.createIntegerSymbol("HSMC_NCS_WR_SETUP_CS" + str(hsmcChipSelNum), hsmcSym_WRITE_TIMING_CS)
        hsmcSym_SETUP_NCS_WR_CS.setLabel(hsmcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("caption"))
        hsmcSym_SETUP_NCS_WR_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_SETUP_NCS_WR_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("mask")))
        hsmcSym_SETUP_NCS_WR_CS.setDefaultValue(HSMC_SETUP_DEFAULT_VALUE)

        # HSMC Write Pulse Timings
        hsmcSym_PULSE_NWE_CS = hemcComponent.createIntegerSymbol("HSMC_NWE_PULSE_CS" + str(hsmcChipSelNum), hsmcSym_WRITE_TIMING_CS)
        hsmcSym_PULSE_NWE_CS.setLabel(hsmcRegBitField_PULSE_NWE_PULSE.getAttribute("caption"))
        hsmcSym_PULSE_NWE_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_PULSE_NWE_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_PULSE_NWE_PULSE.getAttribute("mask")))
        hsmcSym_PULSE_NWE_CS.setDefaultValue(HSMC_PULSE_DEFAULT_VALUE)

        hsmcSym_PULSE_NCS_WR_CS = hemcComponent.createIntegerSymbol("HSMC_NCS_WR_PULSE_CS" + str(hsmcChipSelNum), hsmcSym_WRITE_TIMING_CS)
        hsmcSym_PULSE_NCS_WR_CS.setLabel(hsmcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("caption"))
        hsmcSym_PULSE_NCS_WR_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_PULSE_NCS_WR_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("mask")))
        hsmcSym_PULSE_NCS_WR_CS.setDefaultValue(HSMC_PULSE_DEFAULT_VALUE)

        # HSMC Write Cycle Timings
        hsmcSym_CYCLE_TIMING_NWE_CS = hemcComponent.createIntegerSymbol("HSMC_NWE_CYCLE_CS" + str(hsmcChipSelNum), hsmcSym_WRITE_TIMING_CS)
        hsmcSym_CYCLE_TIMING_NWE_CS.setLabel(hsmcRegBitField_CYCLE_NWE_CYCLE.getAttribute("caption"))
        hsmcSym_CYCLE_TIMING_NWE_CS.setMin(HSMC_DEFAULT_MIN_VALUE)
        hsmcSym_CYCLE_TIMING_NWE_CS.setMax(hsmcConvertMaskToInt(hsmcRegBitField_CYCLE_NWE_CYCLE.getAttribute("mask")))
        hsmcSym_CYCLE_TIMING_NWE_CS.setDefaultValue(HSMC_CYCLE_DEFAULT_VALUE)

        # HSMC Mode Settings
        hsmcSym_MODE_CS_REGISTER = hemcComponent.createMenuSymbol("HSMC_MODE_REGISTER_CS" + str(hsmcChipSelNum), hsmcSym_CS)
        hsmcSym_MODE_CS_REGISTER.setLabel("Mode Settings")


        hsmcSym_MODE_DBW = hemcComponent.createKeyValueSetSymbol("HSMC_DATA_BUS_CS" + str(hsmcChipSelNum), hsmcSym_MODE_CS_REGISTER)
        hsmcSym_MODE_DBW.setLabel("External Memory Data Bus Width")
        hsmcSym_MODE_DBW.setOutputMode("Value")
        hsmcSym_MODE_DBW.setDisplayMode("Description")
        hsmcSym_MODE_DBW.addKey("HSMC_MODE_DBW_8_BIT", "0", "8-bit Data Bus")
        hsmcSym_MODE_DBW.addKey("HSMC_MODE_DBW_16_BIT", "1", "16-bit Data Bus")
        hsmcSym_MODE_DBW.addKey("HSMC_MODE_DBW_32_BIT", "2", "16-bit Data Bus")
        hsmcSym_MODE_DBW.setSelectedKey("HSMC_MODE_DBW_32_BIT", 2)

        hsmcSym_MODE_EXNW = hemcComponent.createKeyValueSetSymbol("HSMC_NWAIT_MODE_CS" + str(hsmcChipSelNum), hsmcSym_MODE_CS_REGISTER)
        hsmcSym_MODE_EXNW.setOutputMode("Key")
        hsmcSym_MODE_EXNW.setDisplayMode("Description")
        hsmcSym_MODE_EXNW.setLabel("External Wait Signal (NWAIT)")
        hsmcSym_MODE_EXNW.addKey("HSMC_MODE_EXNW_MODE_DISABLED", "0", "Disable")
        hsmcSym_MODE_EXNW.addKey("HSMC_MODE_EXNW_MODE_FROZEN", "2", "Frozen Mode")
        hsmcSym_MODE_EXNW.addKey("HSMC_MODE_EXNW_MODE_READY", "3", "Ready Mode")
        hsmcSym_MODE_EXNW.setSelectedKey("HSMC_MODE_EXNW_MODE_DISABLED", 2)

        hsmcSym_MODE_RMW = hemcComponent.createBooleanSymbol("HSMC_MODE_RMW" + str(hsmcChipSelNum), hsmcSym_MODE_CS_REGISTER)
        hsmcSym_MODE_RMW.setLabel("Read Modify Write Enable")
        hsmcSym_MODE_RMW.setDefaultValue(True)

        hsmcSym_MODE_READ = hemcComponent.createBooleanSymbol("HSMC_READ_ENABLE_MODE_CS" + str(hsmcChipSelNum), hsmcSym_MODE_CS_REGISTER)
        hsmcSym_MODE_READ.setLabel("Read Operation is controlled by NRD Signal")
        hsmcSym_MODE_READ.setDefaultValue(True)

        hsmcSym_MODE_WRITE = hemcComponent.createBooleanSymbol("HSMC_WRITE_ENABLE_MODE_CS" + str(hsmcChipSelNum), hsmcSym_MODE_CS_REGISTER)
        hsmcSym_MODE_WRITE.setLabel("Write Operation is controlled by NWE Signal")
        hsmcSym_MODE_WRITE.setDefaultValue(True)

    hemcCsLogic = hemcComponent.createBooleanSymbol("DUMMY", None)
    hemcCsLogic.setDependencies(hideMenus, csDependencies)
    hemcCsLogic.setVisible(False)


############################################################################
#### Dependency ####
############################################################################
    # Enable Peripheral Clock in Clock manager
    Database.clearSymbolValue("core", hemcInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", hemcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

############################################################################
#### Code Generation ####
############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    hemcHeader1File = hemcComponent.createFileSymbol("HEMC_H", None)
    hemcHeader1File.setSourcePath("../peripheral/hemc_44121/templates/plib_hemc.h.ftl")
    hemcHeader1File.setOutputName("plib_"+hemcInstanceName.getValue().lower()+".h")
    hemcHeader1File.setDestPath("/peripheral/hemc/")
    hemcHeader1File.setProjectPath("config/" + configName + "/peripheral/hemc/")
    hemcHeader1File.setType("HEADER")
    hemcHeader1File.setMarkup(True)

    hemcSource1File = hemcComponent.createFileSymbol("HEMC_C", None)
    hemcSource1File.setSourcePath("../peripheral/hemc_44121/templates/plib_hemc.c.ftl")
    hemcSource1File.setOutputName("plib_"+hemcInstanceName.getValue().lower()+".c")
    hemcSource1File.setDestPath("/peripheral/hemc/")
    hemcSource1File.setProjectPath("config/" + configName + "/peripheral/hemc/")
    hemcSource1File.setType("SOURCE")
    hemcSource1File.setMarkup(True)

    # Add hemc related code to common files
    hemcHeader1FileEntry = hemcComponent.createFileSymbol("HEMC_SYSTEM_DEFINITIONS_H", None)
    hemcHeader1FileEntry.setType("STRING")
    hemcHeader1FileEntry.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    hemcHeader1FileEntry.setSourcePath("../peripheral/hemc_44121/templates/system/definitions.h.ftl")
    hemcHeader1FileEntry.setMarkup(True)

    hemcSystemInitFile = hemcComponent.createFileSymbol("HEMC_SYSTEM_INITIALIZE_C", None)
    hemcSystemInitFile.setType("STRING")
    hemcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    hemcSystemInitFile.setSourcePath("../peripheral/hemc_44121/templates/system/initialization.c.ftl")
    hemcSystemInitFile.setMarkup(True)
   
    hemcComponent.addPlugin("../peripheral/hemc_44121/plugin/hemc_44121.jar")