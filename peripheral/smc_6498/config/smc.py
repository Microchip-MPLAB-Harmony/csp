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

#********************** Static Memory Controller Module ***********************

#------------------------------------------------------------------------------
#                               Dependency Functions
#------------------------------------------------------------------------------

# Function to convert Bitfield mask string to Integer
def smcConvertMaskToInt( aRegMask ):
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
def smcMemoryPageSizeModeVisible(symbol, event):
    id = symbol.getID()[-1]
    smcChipSelNum = int(id)

    if (event["value"] == True):
        smcSym_MODE_PS[smcChipSelNum].setVisible(True)
    else :
        smcSym_MODE_PS[smcChipSelNum].setVisible(False)

# Dependency functions definitions to enable visibility based on selection of TDF Optimization
def smcTdfCyclesModeVisible(symbol, event):
    id = symbol.getID()[-1]
    smcChipSelNum = int(id)

    if (event["value"] == True):
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setVisible(True)
    else :
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setVisible(False)


# Dependency function definition to enable visibility based on selection of Byte Access Type
def smcByteAccessSelModeVisible(symbol, event):
    symObj = event["symbol"]
    id = symbol.getID()[-1]
    smcChipSelNum = int(id)

    if (symObj.getSelectedKey() == "SMC_MODE_DBW_16_BIT"):
        smcSym_MODE_BAT[smcChipSelNum].setVisible(True)
    else :
        smcSym_MODE_BAT[smcChipSelNum].setVisible(False)

# Get SMC ID
smcRegModule    = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SMC\"]")
smcRegModuleID  = smcRegModule.getAttribute("id")

#------------------------------------------------------------------------------
#          ATDF Read to get SMC Register | Bitfield | Mask | Value Group
#------------------------------------------------------------------------------
# SMC_SETUP Register Bitfield Names and Mask
smcRegBitField_SETUP_NWE_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_SETUP"]/bitfield@[name="NWE_SETUP"]')
smcRegBitField_SETUP_NCS_WR_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_SETUP"]/bitfield@[name="NCS_WR_SETUP"]')
smcRegBitField_SETUP_NRD_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_SETUP"]/bitfield@[name="NRD_SETUP"]')
smcRegBitField_SETUP_NCS_RD_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_SETUP"]/bitfield@[name="NCS_RD_SETUP"]')

# SMC_PULSE Register Bitfield Names and Mask
smcRegBitField_PULSE_NWE_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_PULSE"]/bitfield@[name="NWE_PULSE"]')
smcRegBitField_PULSE_NCS_WR_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_PULSE"]/bitfield@[name="NCS_WR_PULSE"]')
smcRegBitField_PULSE_NRD_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_PULSE"]/bitfield@[name="NRD_PULSE"]')
smcRegBitField_PULSE_NCS_RD_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_PULSE"]/bitfield@[name="NCS_RD_PULSE"]')

# SMC_CYCLE Register Bitfield Names and Mask
smcRegBitField_CYCLE_NWE_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_CYCLE"]/bitfield@[name="NWE_CYCLE"]')
smcRegBitField_CYCLE_NRD_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_CYCLE"]/bitfield@[name="NRD_CYCLE"]')

# SMC_Mode Register Bitfield Names and Mask
smcRegBitField_MODE_TDF_CYCLES      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SMC"]/register-group@[name="SMC_CS_NUMBER"]/register@[name="SMC_MODE"]/bitfield@[name="TDF_CYCLES"]')

#------------------------------------------------------------------------------
#                     Global SMC Array sysmbol declaration
#------------------------------------------------------------------------------
smcSym_MODE_BAT = []
smcSym_MODE_PS = []
smcSym_MODE_TDF_CYCLES = []

#------------------------------------------------------------------------------
#                               Global Variables
#------------------------------------------------------------------------------

# Get the Chip Select Count from ATDF config file
global smcChipSelCount

#------------------------------------------------------------------------------
#                                   Constatns
#------------------------------------------------------------------------------

# Min Zero Value
SMC_DEFAULT_MIN_VALUE               = 0

# Deafult value for SMC Setup Register
SMC_SETUP_DEFAULT_VALUE             = 16

# Deafult value for SMC Pulse Register
SMC_PULSE_DEFAULT_VALUE             = 16

# Deafult value for SMC Cycle Register
SMC_CYCLE_DEFAULT_VALUE             = 3

# Deafult value for SMC MODE TDF CYCLE Register
SMC_MODE_TDF_CYCLES_DEFAULT_VALUE   = 0

#------------------------------------------------------------------------------
#                          Instantiate SMC Component
#------------------------------------------------------------------------------
def instantiateComponent(smcComponent):

    smcInstanceName = smcComponent.createStringSymbol("SMC_INSTANCE_NAME", None)
    smcInstanceName.setVisible(False)
    smcInstanceName.setDefaultValue(smcComponent.getID().upper())
    print"--------------------------------------------------------------------"
    print("************************** Running " + smcInstanceName.getValue() + " ****************************")
    print"--------------------------------------------------------------------"

    smcRegModule    = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SMC\"]/register-group@[name=\"SMC\"]/register-group@[name=\"SMC_CS_NUMBER\"]")
    smcChipSelCount = int (smcRegModule.getAttribute("count"))

    print("Total available SMC Chip Select Count is : " + str(smcChipSelCount))

    smcMenu = smcComponent.createMenuSymbol("SMC_MENU", None)
    smcMenu.setLabel("SMC Configurations")

    # SMC Global features
    smcSym_GlobalMenu= smcComponent.createMenuSymbol("SMC_GLOBAL_MENU", smcMenu)
    smcSym_GlobalMenu.setLabel("SMC Global Features")

    smcSym_WPMR_WPEN = smcComponent.createBooleanSymbol("SMC_WRITE_PROTECTION", smcSym_GlobalMenu)
    smcSym_WPMR_WPEN.setLabel("Enable Write Protection")
    smcSym_WPMR_WPEN.setDefaultValue(False)

    smcSym_Key = smcComponent.createMenuSymbol("SMC_KEY_MENU", smcSym_GlobalMenu)
    smcSym_Key.setLabel("Scrambling Key")

    smcSym_SMC_KEY1 = smcComponent.createHexSymbol("SMC_KEY1", smcSym_Key)
    smcSym_SMC_KEY1.setLabel("Scrambling Key 1")

    smcSym_SMC_KEY2 = smcComponent.createHexSymbol("SMC_KEY2", smcSym_Key)
    smcSym_SMC_KEY2.setLabel("Scrambling Key 2")

    #--------------------------------------------------------------------------
    # SMC Chip Select Selection and Settings
    #--------------------------------------------------------------------------
    smcSym_Chip_Select = smcComponent.createMenuSymbol("SMC_CHIP_SELECT", smcMenu)
    smcSym_Chip_Select.setLabel("SMC Chip Select Selection and Settings")

    smcSym_CS_COUNT = smcComponent.createIntegerSymbol("SMC_CHIP_SELECT_COUNT", smcSym_Chip_Select)
    smcSym_CS_COUNT.setDefaultValue(smcChipSelCount)
    smcSym_CS_COUNT.setVisible(False)

    for smcChipSelNum in range(0, smcChipSelCount):
        smcSym_CS = smcComponent.createBooleanSymbol("SMC_CHIP_SELECT" + str(smcChipSelNum), smcSym_Chip_Select)
        smcSym_CS.setLabel("Enable Chip Select "+ str(smcChipSelNum))

        smcSym_OCMS_CS_SE = smcComponent.createBooleanSymbol("SMC_MEM_SCRAMBLING_CS" + str(smcChipSelNum), smcSym_CS)
        smcSym_OCMS_CS_SE.setLabel("Enable Memory Scrambling")
        smcSym_OCMS_CS_SE.setDefaultValue(False)

        # SMC Read Setup, Pulse and Cycle Timings
        smcSym_READ_TIMING_CS = smcComponent.createMenuSymbol("SMC_SETUP_TIMING_CS" + str(smcChipSelNum), smcSym_CS)
        smcSym_READ_TIMING_CS.setLabel("Read Cycle Timings")

        # SMC Read Setup Timings
        smcSym_SETUP_NRD_CS = smcComponent.createIntegerSymbol("SMC_NRD_SETUP_CS" + str(smcChipSelNum), smcSym_READ_TIMING_CS)
        smcSym_SETUP_NRD_CS.setLabel(smcRegBitField_SETUP_NRD_SETUP.getAttribute("caption"))
        smcSym_SETUP_NRD_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_SETUP_NRD_CS.setMax(smcConvertMaskToInt(smcRegBitField_SETUP_NRD_SETUP.getAttribute("mask")))
        smcSym_SETUP_NRD_CS.setDefaultValue(SMC_SETUP_DEFAULT_VALUE)

        smcSym_SETUP_NCS_RD_CS = smcComponent.createIntegerSymbol("SMC_NCS_RD_SETUP_CS" + str(smcChipSelNum), smcSym_READ_TIMING_CS)
        smcSym_SETUP_NCS_RD_CS.setLabel(smcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("caption"))
        smcSym_SETUP_NCS_RD_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_SETUP_NCS_RD_CS.setMax(smcConvertMaskToInt(smcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("mask")))
        smcSym_SETUP_NCS_RD_CS.setDefaultValue(SMC_SETUP_DEFAULT_VALUE)

        # SMC Read Pulse Timings
        smcSym_PULSE_NRD_CS = smcComponent.createIntegerSymbol("SMC_NRD_PULSE_CS" + str(smcChipSelNum), smcSym_READ_TIMING_CS)
        smcSym_PULSE_NRD_CS.setLabel(smcRegBitField_PULSE_NRD_PULSE.getAttribute("caption"))
        smcSym_PULSE_NRD_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_PULSE_NRD_CS.setMax(smcConvertMaskToInt(smcRegBitField_PULSE_NRD_PULSE.getAttribute("mask")))
        smcSym_PULSE_NRD_CS.setDefaultValue(SMC_PULSE_DEFAULT_VALUE)

        smcSym_PULSE_NCS_RD_CS = smcComponent.createIntegerSymbol("SMC_NCS_RD_PULSE_CS" + str(smcChipSelNum),smcSym_READ_TIMING_CS)
        smcSym_PULSE_NCS_RD_CS.setLabel(smcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("caption"))
        smcSym_PULSE_NCS_RD_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_PULSE_NCS_RD_CS.setMax(smcConvertMaskToInt(smcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("mask")))
        smcSym_PULSE_NCS_RD_CS.setDefaultValue(SMC_PULSE_DEFAULT_VALUE)

        # SMC Read Cycle Timings
        smcSym_SMC_CYCLE_TIMING_NRD_CS = smcComponent.createIntegerSymbol("SMC_NRD_CYCLE_CS" + str(smcChipSelNum), smcSym_READ_TIMING_CS)
        smcSym_SMC_CYCLE_TIMING_NRD_CS.setLabel(smcRegBitField_CYCLE_NRD_CYCLE.getAttribute("caption"))
        smcSym_SMC_CYCLE_TIMING_NRD_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_SMC_CYCLE_TIMING_NRD_CS.setMax(smcConvertMaskToInt(smcRegBitField_CYCLE_NRD_CYCLE.getAttribute("mask")))
        smcSym_SMC_CYCLE_TIMING_NRD_CS.setDefaultValue(SMC_CYCLE_DEFAULT_VALUE)

        # SMC Write Setup, Pulse and Cycle Timings
        smcSym_WRITE_TIMING_CS = smcComponent.createMenuSymbol("SMC_PULSE_TIMING_CS" + str(smcChipSelNum), smcSym_CS)
        smcSym_WRITE_TIMING_CS.setLabel("Write Cycle Timings")

        # SMC Write Setup Timings
        smcSym_SETUP_NWE_CS = smcComponent.createIntegerSymbol("SMC_NWE_SETUP_CS" + str(smcChipSelNum), smcSym_WRITE_TIMING_CS)
        smcSym_SETUP_NWE_CS.setLabel(smcRegBitField_SETUP_NWE_SETUP.getAttribute("caption"))
        smcSym_SETUP_NWE_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_SETUP_NWE_CS.setMax(smcConvertMaskToInt(smcRegBitField_SETUP_NWE_SETUP.getAttribute("mask")))
        smcSym_SETUP_NWE_CS.setDefaultValue(SMC_SETUP_DEFAULT_VALUE)

        smcSym_SETUP_NCS_WR_CS = smcComponent.createIntegerSymbol("SMC_NCS_WR_SETUP_CS" + str(smcChipSelNum), smcSym_WRITE_TIMING_CS)
        smcSym_SETUP_NCS_WR_CS.setLabel(smcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("caption"))
        smcSym_SETUP_NCS_WR_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_SETUP_NCS_WR_CS.setMax(smcConvertMaskToInt(smcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("mask")))
        smcSym_SETUP_NCS_WR_CS.setDefaultValue(SMC_SETUP_DEFAULT_VALUE)

        # SMC Write Pulse Timings
        smcSym_PULSE_NWE_CS = smcComponent.createIntegerSymbol("SMC_NWE_PULSE_CS" + str(smcChipSelNum), smcSym_WRITE_TIMING_CS)
        smcSym_PULSE_NWE_CS.setLabel(smcRegBitField_PULSE_NWE_PULSE.getAttribute("caption"))
        smcSym_PULSE_NWE_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_PULSE_NWE_CS.setMax(smcConvertMaskToInt(smcRegBitField_PULSE_NWE_PULSE.getAttribute("mask")))
        smcSym_PULSE_NWE_CS.setDefaultValue(SMC_PULSE_DEFAULT_VALUE)

        smcSym_PULSE_NCS_WR_CS = smcComponent.createIntegerSymbol("SMC_NCS_WR_PULSE_CS" + str(smcChipSelNum), smcSym_WRITE_TIMING_CS)
        smcSym_PULSE_NCS_WR_CS.setLabel(smcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("caption"))
        smcSym_PULSE_NCS_WR_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_PULSE_NCS_WR_CS.setMax(smcConvertMaskToInt(smcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("mask")))
        smcSym_PULSE_NCS_WR_CS.setDefaultValue(SMC_PULSE_DEFAULT_VALUE)

        # SMC Write Cycle Timings
        smcSym_CYCLE_TIMING_NWE_CS = smcComponent.createIntegerSymbol("SMC_NWE_CYCLE_CS" + str(smcChipSelNum), smcSym_WRITE_TIMING_CS)
        smcSym_CYCLE_TIMING_NWE_CS.setLabel(smcRegBitField_CYCLE_NWE_CYCLE.getAttribute("caption"))
        smcSym_CYCLE_TIMING_NWE_CS.setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_CYCLE_TIMING_NWE_CS.setMax(smcConvertMaskToInt(smcRegBitField_CYCLE_NWE_CYCLE.getAttribute("mask")))
        smcSym_CYCLE_TIMING_NWE_CS.setDefaultValue(SMC_CYCLE_DEFAULT_VALUE)

        # SMC Mode Settings
        smcSym_MODE_CS_REGISTER = smcComponent.createMenuSymbol("SMC_MODE_REGISTER_CS" + str(smcChipSelNum), smcSym_CS)
        smcSym_MODE_CS_REGISTER.setLabel("Mode Settings")


        smcSym_MODE_DBW = smcComponent.createKeyValueSetSymbol("SMC_DATA_BUS_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_DBW.setLabel("External Memory Data Bus Width")
        smcSym_MODE_DBW.setOutputMode("Key")
        smcSym_MODE_DBW.setDisplayMode("Description")
        smcSym_MODE_DBW.addKey("SMC_MODE_DBW_8_BIT", "0", "8-bit Data Bus")
        smcSym_MODE_DBW.addKey("SMC_MODE_DBW_16_BIT", "1", "16-bit Data Bus")
        smcSym_MODE_DBW.setSelectedKey("SMC_MODE_DBW_16_BIT", 2)

        smcSym_MODE_BAT.append(smcChipSelNum)
        smcSym_MODE_BAT[smcChipSelNum] = smcComponent.createKeyValueSetSymbol("SMC_BAT_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_BAT[smcChipSelNum].setOutputMode("Key")
        smcSym_MODE_BAT[smcChipSelNum].setDisplayMode("Description")
        smcSym_MODE_BAT[smcChipSelNum].setLabel("Byte Write or Byte Select Access")
        smcSym_MODE_BAT[smcChipSelNum].addKey("SMC_MODE_BAT_BYTE_SELECT", "0", "Byte Select Access Type")
        smcSym_MODE_BAT[smcChipSelNum].addKey("SMC_MODE_BAT_BYTE_WRITE", "1", "Byte Write Access Type")
        smcSym_MODE_BAT[smcChipSelNum].setSelectedKey("SMC_MODE_BAT_BYTE_SELECT", 2)
        smcSym_MODE_BAT[smcChipSelNum].setDependencies(smcByteAccessSelModeVisible, ["SMC_DATA_BUS_CS" + str(smcChipSelNum)])

        smcSym_MODE_PMEN = smcComponent.createBooleanSymbol("SMC_PMEN_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_PMEN.setLabel("Enable Page mode")
        smcSym_MODE_PMEN.setDefaultValue(False)

        smcSym_MODE_PS.append(smcChipSelNum)
        smcSym_MODE_PS[smcChipSelNum] = smcComponent.createKeyValueSetSymbol("SMC_PS_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_PS[smcChipSelNum].setOutputMode("Key")
        smcSym_MODE_PS[smcChipSelNum].setDisplayMode("Description")
        smcSym_MODE_PS[smcChipSelNum].setLabel("External Memory Page Size")
        smcSym_MODE_PS[smcChipSelNum].setVisible(False)
        smcSym_MODE_PS[smcChipSelNum].addKey("SMC_MODE_PS_4_BYTE", "0", "4-bytes")
        smcSym_MODE_PS[smcChipSelNum].addKey("SMC_MODE_PS_8_BYTE", "1", "8-bytes")
        smcSym_MODE_PS[smcChipSelNum].addKey("SMC_MODE_PS_16_BYTE", "2", "16-bytes")
        smcSym_MODE_PS[smcChipSelNum].addKey("SMC_MODE_PS_32_BYTE", "3", "32-bytes")
        smcSym_MODE_PS[smcChipSelNum].setSelectedKey("SMC_MODE_PS_4_BYTE", 2)
        smcSym_MODE_PS[smcChipSelNum].setDependencies(smcMemoryPageSizeModeVisible, ["SMC_PMEN_CS" + str(smcChipSelNum)])

        smcSym_MODE_TDF = smcComponent.createBooleanSymbol("SMC_TDF_OPTIMIZATION_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_TDF.setLabel("Enable Optimization of Data Float Time")
        smcSym_MODE_TDF.setDefaultValue(False)

        smcSym_MODE_TDF_CYCLES.append(smcChipSelNum)
        smcSym_MODE_TDF_CYCLES[smcChipSelNum] = smcComponent.createIntegerSymbol("SMC_TDF_CYCLES_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setLabel("Data Float Time (no of cycles)")
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setVisible(False)
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setMin(SMC_DEFAULT_MIN_VALUE)
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setMax(smcConvertMaskToInt(smcRegBitField_MODE_TDF_CYCLES.getAttribute("mask")))
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setDefaultValue(SMC_MODE_TDF_CYCLES_DEFAULT_VALUE)
        smcSym_MODE_TDF_CYCLES[smcChipSelNum].setDependencies(smcTdfCyclesModeVisible, ["SMC_TDF_OPTIMIZATION_CS" + str(smcChipSelNum)])

        smcSym_MODE_EXNW = smcComponent.createKeyValueSetSymbol("SMC_NWAIT_MODE_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_EXNW.setOutputMode("Key")
        smcSym_MODE_EXNW.setDisplayMode("Description")
        smcSym_MODE_EXNW.setLabel("External Wait Signal (NWAIT)")
        smcSym_MODE_EXNW.addKey("SMC_MODE_EXNW_MODE_DISABLED", "0", "Disable")
        smcSym_MODE_EXNW.addKey("SMC_MODE_EXNW_MODE_FROZEN", "2", "Frozen Mode")
        smcSym_MODE_EXNW.addKey("SMC_MODE_EXNW_MODE_READY", "3", "Ready Mode")
        smcSym_MODE_EXNW.setSelectedKey("SMC_MODE_EXNW_MODE_DISABLED", 2)

        smcSym_MODE_READ = smcComponent.createBooleanSymbol("SMC_READ_ENABLE_MODE_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_READ.setLabel("Read Operation is controlled by NRD Signal")
        smcSym_MODE_READ.setDefaultValue(True)

        smcSym_MODE_WRITE = smcComponent.createBooleanSymbol("SMC_WRITE_ENABLE_MODE_CS" + str(smcChipSelNum), smcSym_MODE_CS_REGISTER)
        smcSym_MODE_WRITE.setLabel("Write Operation is controlled by NWE Signal")
        smcSym_MODE_WRITE.setDefaultValue(True)


############################################################################
#### Dependency ####
############################################################################
    # Enable Peripheral Clock in Clock manager
    Database.clearSymbolValue("core", smcInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", smcInstanceName.getValue()+"_CLOCK_ENABLE", True, 2) 

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    smcHeader1File = smcComponent.createFileSymbol("PLIB_SMC_H", None)
    smcHeader1File.setSourcePath("../peripheral/smc_6498/templates/plib_smc.h.ftl")
    smcHeader1File.setOutputName("plib_"+smcInstanceName.getValue().lower()+".h")
    smcHeader1File.setDestPath("/peripheral/smc/")
    smcHeader1File.setProjectPath("config/" + configName + "/peripheral/smc/")
    smcHeader1File.setType("HEADER")
    smcHeader1File.setMarkup(True)

    smcSource1File = smcComponent.createFileSymbol("PLIB_SMC_C", None)
    smcSource1File.setSourcePath("../peripheral/smc_6498/templates/plib_smc.c.ftl")
    smcSource1File.setOutputName("plib_"+smcInstanceName.getValue().lower()+".c")
    smcSource1File.setDestPath("/peripheral/smc/")
    smcSource1File.setProjectPath("config/" + configName + "/peripheral/smc/")
    smcSource1File.setType("SOURCE")
    smcSource1File.setMarkup(True)

    #Add SMC related code to common files
    smcHeader1FileEntry = smcComponent.createFileSymbol("PLIB_SMC_DEFINITIONS_H", None)
    smcHeader1FileEntry.setType("STRING")
    smcHeader1FileEntry.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    smcHeader1FileEntry.setSourcePath("../peripheral/smc_6498/templates/system/definitions.h.ftl")
    smcHeader1FileEntry.setMarkup(True)

    smcSystemInitFile = smcComponent.createFileSymbol("PLIB_SMC_INITIALIZE_H", None)
    smcSystemInitFile.setType("STRING")
    smcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    smcSystemInitFile.setSourcePath("../peripheral/smc_6498/templates/system/initialization.c.ftl")
    smcSystemInitFile.setMarkup(True)
