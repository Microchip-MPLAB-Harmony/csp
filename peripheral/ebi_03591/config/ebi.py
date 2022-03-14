# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

#********************** External Bus Interface Module ***********************

#------------------------------------------------------------------------------
#                               Dependency Functions
#------------------------------------------------------------------------------

# Function to convert Bitfield mask string to Integer
def ebiSmcConvertMaskToInt( aRegMask ):
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
def ebiSmcMemoryPageSizeModeVisible(symbol, event):
    id = symbol.getID()[-1]
    ebiChipSelNum = int(id)

    if (event["value"] == True):
        ebiSmcSym_MODE_PS[ebiChipSelNum].setVisible(True)
    else :
        ebiSmcSym_MODE_PS[ebiChipSelNum].setVisible(False)

# Dependency functions definitions to enable visibility based on selection of TDF Optimization
def ebiSmcTdfCyclesModeVisible(symbol, event):
    id = symbol.getID()[-1]
    ebiChipSelNum = int(id)

    if (event["value"] == True):
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setVisible(True)
    else :
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setVisible(False)


# Dependency function definition to enable visibility based on selection of Byte Access Type
def ebiSmcByteAccessSelModeVisible(symbol, event):
    symObj = event["symbol"]
    id = symbol.getID()[-1]
    ebiChipSelNum = int(id)

    if (symObj.getSelectedKey() == "EBI_SMC_MODE_DBW_16_BIT"):
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setVisible(True)
    else :
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setVisible(False)

# Get EBI ID
ebiRegModule    = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EBI\"]")
ebiRegModuleID  = ebiRegModule.getAttribute("id")

#------------------------------------------------------------------------------
#          ATDF Read to get EBI Register | Bitfield | Mask | Value Group
#------------------------------------------------------------------------------
# EBI SMC_SETUP Register Bitfield Names and Mask
ebiSmcRegBitField_SETUP_NWE_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_SETUP"]/bitfield@[name="NWE_SETUP"]')
ebiSmcRegBitField_SETUP_NCS_WR_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_SETUP"]/bitfield@[name="NCS_WR_SETUP"]')
ebiSmcRegBitField_SETUP_NRD_SETUP      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_SETUP"]/bitfield@[name="NRD_SETUP"]')
ebiSmcRegBitField_SETUP_NCS_RD_SETUP   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_SETUP"]/bitfield@[name="NCS_RD_SETUP"]')

# EBI SMC_PULSE Register Bitfield Names and Mask
ebiSmcRegBitField_PULSE_NWE_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_PULSE"]/bitfield@[name="NWE_PULSE"]')
ebiSmcRegBitField_PULSE_NCS_WR_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_PULSE"]/bitfield@[name="NCS_WR_PULSE"]')
ebiSmcRegBitField_PULSE_NRD_PULSE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_PULSE"]/bitfield@[name="NRD_PULSE"]')
ebiSmcRegBitField_PULSE_NCS_RD_PULSE   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_PULSE"]/bitfield@[name="NCS_RD_PULSE"]')

# EBI SMC_CYCLE Register Bitfield Names and Mask
ebiSmcRegBitField_CYCLE_NWE_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_CYCLE"]/bitfield@[name="NWE_CYCLE"]')
ebiSmcRegBitField_CYCLE_NRD_CYCLE      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_CYCLE"]/bitfield@[name="NRD_CYCLE"]')

# EBI SMC_Mode Register Bitfield Names and Mask
ebiSmcRegBitField_MODE_TDF_CYCLES      = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EBI"]/register-group@[name="CS_X"]/register@[name="SMC_MODE"]/bitfield@[name="TDF_CYCLES"]')

#------------------------------------------------------------------------------
#                     Global SMC Array sysmbol declaration
#------------------------------------------------------------------------------
ebiSmcSym_MODE_BAT = []
ebiSmcSym_MODE_PS = []
ebiSmcSym_MODE_TDF_CYCLES = []

#------------------------------------------------------------------------------
#                               Global Variables
#------------------------------------------------------------------------------

# Get the Chip Select Count from ATDF config file
global ebiChipSelCount

#------------------------------------------------------------------------------
#                                   Constatns
#------------------------------------------------------------------------------

# Min Zero Value
EBI_SMC_DEFAULT_MIN_VALUE               = 0

# Deafult value for SMC Setup Register
EBI_SMC_SETUP_DEFAULT_VALUE             = 16

# Deafult value for SMC Pulse Register
EBI_SMC_PULSE_DEFAULT_VALUE             = 16

# Deafult value for SMC Cycle Register
EBI_SMC_CYCLE_DEFAULT_VALUE             = 3

# Deafult value for SMC MODE TDF CYCLE Register
EBI_SMC_MODE_TDF_CYCLES_DEFAULT_VALUE   = 0

#------------------------------------------------------------------------------
#                          Instantiate EBI Component
#------------------------------------------------------------------------------
def instantiateComponent(ebiComponent):

    ebiInstanceName = ebiComponent.createStringSymbol("EBI_INSTANCE_NAME", None)
    ebiInstanceName.setVisible(False)
    ebiInstanceName.setDefaultValue(ebiComponent.getID().upper())
    print("************************** Running " + ebiInstanceName.getValue() + " ****************************")

    ebiRegModule    = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"EBI\"]/register-group@[name=\"EBI\"]/register-group@[name=\"CS_X\"]")
    ebiChipSelCount = int (ebiRegModule.getAttribute("count"))

    print("Total available EBI Chip Select Count is : " + str(ebiChipSelCount))

    ebiMenu = ebiComponent.createMenuSymbol("EBI_MENU", None)
    ebiMenu.setLabel("SMC Configurations")

    # SMC Global features
    ebiSmcSym_GlobalMenu= ebiComponent.createMenuSymbol("EBI_SMC_GLOBAL_MENU", ebiMenu)
    ebiSmcSym_GlobalMenu.setLabel("SMC Global Features")

    ebiSmcSym_WPMR_WPEN = ebiComponent.createBooleanSymbol("EBI_SMC_WRITE_PROTECTION", ebiSmcSym_GlobalMenu)
    ebiSmcSym_WPMR_WPEN.setLabel("Enable Write Protection")
    ebiSmcSym_WPMR_WPEN.setDefaultValue(False)

    #--------------------------------------------------------------------------
    # EBI SMC Chip Select Selection and Settings
    #--------------------------------------------------------------------------
    ebiSmcSym_Chip_Select = ebiComponent.createMenuSymbol("EBI_SMC_CHIP_SELECT", ebiMenu)
    ebiSmcSym_Chip_Select.setLabel("SMC Chip Select Selection and Settings")

    ebiSmcSym_CS_COUNT = ebiComponent.createIntegerSymbol("EBI_SMC_CHIP_SELECT_COUNT", ebiSmcSym_Chip_Select)
    ebiSmcSym_CS_COUNT.setDefaultValue(ebiChipSelCount)
    ebiSmcSym_CS_COUNT.setVisible(False)

    for ebiChipSelNum in range(0, ebiChipSelCount):
        ebiSmcSym_CS = ebiComponent.createBooleanSymbol("EBI_SMC_CHIP_SELECT" + str(ebiChipSelNum), ebiSmcSym_Chip_Select)
        ebiSmcSym_CS.setLabel("Enable Chip Select "+ str(ebiChipSelNum))

        # EBI SMC Read Setup, Pulse and Cycle Timings
        ebiSmcSym_READ_TIMING_CS = ebiComponent.createMenuSymbol("EBI_SMC_SETUP_TIMING_CS" + str(ebiChipSelNum), ebiSmcSym_CS)
        ebiSmcSym_READ_TIMING_CS.setLabel("Read Cycle Timings")

        # EBI SMC Read Setup Timings
        ebiSmcSym_SETUP_NRD_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NRD_SETUP_CS" + str(ebiChipSelNum), ebiSmcSym_READ_TIMING_CS)
        ebiSmcSym_SETUP_NRD_CS.setLabel(ebiSmcRegBitField_SETUP_NRD_SETUP.getAttribute("caption"))
        ebiSmcSym_SETUP_NRD_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_SETUP_NRD_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_SETUP_NRD_SETUP.getAttribute("mask")))
        ebiSmcSym_SETUP_NRD_CS.setDefaultValue(EBI_SMC_SETUP_DEFAULT_VALUE)

        ebiSmcSym_SETUP_NCS_RD_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NCS_RD_SETUP_CS" + str(ebiChipSelNum), ebiSmcSym_READ_TIMING_CS)
        ebiSmcSym_SETUP_NCS_RD_CS.setLabel(ebiSmcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("caption"))
        ebiSmcSym_SETUP_NCS_RD_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_SETUP_NCS_RD_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_SETUP_NCS_RD_SETUP.getAttribute("mask")))
        ebiSmcSym_SETUP_NCS_RD_CS.setDefaultValue(EBI_SMC_SETUP_DEFAULT_VALUE)

        # SMC Read Pulse Timings
        ebiSmcSym_PULSE_NRD_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NRD_PULSE_CS" + str(ebiChipSelNum), ebiSmcSym_READ_TIMING_CS)
        ebiSmcSym_PULSE_NRD_CS.setLabel(ebiSmcRegBitField_PULSE_NRD_PULSE.getAttribute("caption"))
        ebiSmcSym_PULSE_NRD_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_PULSE_NRD_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_PULSE_NRD_PULSE.getAttribute("mask")))
        ebiSmcSym_PULSE_NRD_CS.setDefaultValue(EBI_SMC_PULSE_DEFAULT_VALUE)

        ebiSmcSym_PULSE_NCS_RD_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NCS_RD_PULSE_CS" + str(ebiChipSelNum),ebiSmcSym_READ_TIMING_CS)
        ebiSmcSym_PULSE_NCS_RD_CS.setLabel(ebiSmcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("caption"))
        ebiSmcSym_PULSE_NCS_RD_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_PULSE_NCS_RD_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_PULSE_NCS_RD_PULSE.getAttribute("mask")))
        ebiSmcSym_PULSE_NCS_RD_CS.setDefaultValue(EBI_SMC_PULSE_DEFAULT_VALUE)

        # SMC Read Cycle Timings
        ebiSmcSym_SMC_CYCLE_TIMING_NRD_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NRD_CYCLE_CS" + str(ebiChipSelNum), ebiSmcSym_READ_TIMING_CS)
        ebiSmcSym_SMC_CYCLE_TIMING_NRD_CS.setLabel(ebiSmcRegBitField_CYCLE_NRD_CYCLE.getAttribute("caption"))
        ebiSmcSym_SMC_CYCLE_TIMING_NRD_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_SMC_CYCLE_TIMING_NRD_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_CYCLE_NRD_CYCLE.getAttribute("mask")))
        ebiSmcSym_SMC_CYCLE_TIMING_NRD_CS.setDefaultValue(EBI_SMC_CYCLE_DEFAULT_VALUE)

        # SMC Write Setup, Pulse and Cycle Timings
        ebiSmcSym_WRITE_TIMING_CS = ebiComponent.createMenuSymbol("EBI_SMC_PULSE_TIMING_CS" + str(ebiChipSelNum), ebiSmcSym_CS)
        ebiSmcSym_WRITE_TIMING_CS.setLabel("Write Cycle Timings")

        # SMC Write Setup Timings
        ebiSmcSym_SETUP_NWE_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NWE_SETUP_CS" + str(ebiChipSelNum), ebiSmcSym_WRITE_TIMING_CS)
        ebiSmcSym_SETUP_NWE_CS.setLabel(ebiSmcRegBitField_SETUP_NWE_SETUP.getAttribute("caption"))
        ebiSmcSym_SETUP_NWE_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_SETUP_NWE_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_SETUP_NWE_SETUP.getAttribute("mask")))
        ebiSmcSym_SETUP_NWE_CS.setDefaultValue(EBI_SMC_SETUP_DEFAULT_VALUE)

        ebiSmcSym_SETUP_NCS_WR_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NCS_WR_SETUP_CS" + str(ebiChipSelNum), ebiSmcSym_WRITE_TIMING_CS)
        ebiSmcSym_SETUP_NCS_WR_CS.setLabel(ebiSmcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("caption"))
        ebiSmcSym_SETUP_NCS_WR_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_SETUP_NCS_WR_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_SETUP_NCS_WR_SETUP.getAttribute("mask")))
        ebiSmcSym_SETUP_NCS_WR_CS.setDefaultValue(EBI_SMC_SETUP_DEFAULT_VALUE)

        # SMC Write Pulse Timings
        ebiSmcSym_PULSE_NWE_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NWE_PULSE_CS" + str(ebiChipSelNum), ebiSmcSym_WRITE_TIMING_CS)
        ebiSmcSym_PULSE_NWE_CS.setLabel(ebiSmcRegBitField_PULSE_NWE_PULSE.getAttribute("caption"))
        ebiSmcSym_PULSE_NWE_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_PULSE_NWE_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_PULSE_NWE_PULSE.getAttribute("mask")))
        ebiSmcSym_PULSE_NWE_CS.setDefaultValue(EBI_SMC_PULSE_DEFAULT_VALUE)

        ebiSmcSym_PULSE_NCS_WR_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NCS_WR_PULSE_CS" + str(ebiChipSelNum), ebiSmcSym_WRITE_TIMING_CS)
        ebiSmcSym_PULSE_NCS_WR_CS.setLabel(ebiSmcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("caption"))
        ebiSmcSym_PULSE_NCS_WR_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_PULSE_NCS_WR_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_PULSE_NCS_WR_PULSE.getAttribute("mask")))
        ebiSmcSym_PULSE_NCS_WR_CS.setDefaultValue(EBI_SMC_PULSE_DEFAULT_VALUE)

        # SMC Write Cycle Timings
        ebiSmcSym_CYCLE_TIMING_NWE_CS = ebiComponent.createIntegerSymbol("EBI_SMC_NWE_CYCLE_CS" + str(ebiChipSelNum), ebiSmcSym_WRITE_TIMING_CS)
        ebiSmcSym_CYCLE_TIMING_NWE_CS.setLabel(ebiSmcRegBitField_CYCLE_NWE_CYCLE.getAttribute("caption"))
        ebiSmcSym_CYCLE_TIMING_NWE_CS.setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_CYCLE_TIMING_NWE_CS.setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_CYCLE_NWE_CYCLE.getAttribute("mask")))
        ebiSmcSym_CYCLE_TIMING_NWE_CS.setDefaultValue(EBI_SMC_CYCLE_DEFAULT_VALUE)

        # SMC Mode Settings
        ebiSmcSym_MODE_CS_REGISTER = ebiComponent.createMenuSymbol("EBI_SMC_MODE_REGISTER_CS" + str(ebiChipSelNum), ebiSmcSym_CS)
        ebiSmcSym_MODE_CS_REGISTER.setLabel("Mode Settings")


        ebiSmcSym_MODE_DBW = ebiComponent.createKeyValueSetSymbol("EBI_SMC_DATA_BUS_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_DBW.setLabel("External Memory Data Bus Width")
        ebiSmcSym_MODE_DBW.setOutputMode("Key")
        ebiSmcSym_MODE_DBW.setDisplayMode("Description")
        ebiSmcSym_MODE_DBW.addKey("EBI_SMC_MODE_DBW_8_BIT", "0", "8-bit Data Bus")
        ebiSmcSym_MODE_DBW.addKey("EBI_SMC_MODE_DBW_16_BIT", "1", "16-bit Data Bus")
        ebiSmcSym_MODE_DBW.setSelectedKey("EBI_SMC_MODE_DBW_16_BIT", 2)

        ebiSmcSym_MODE_BAT.append(ebiChipSelNum)
        ebiSmcSym_MODE_BAT[ebiChipSelNum] = ebiComponent.createKeyValueSetSymbol("EBI_SMC_BAT_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setOutputMode("Key")
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setDisplayMode("Description")
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setLabel("Byte Write or Byte Select Access")
        ebiSmcSym_MODE_BAT[ebiChipSelNum].addKey("EBI_SMC_MODE_BAT_BYTE_SELECT", "0", "Byte Select Access Type")
        ebiSmcSym_MODE_BAT[ebiChipSelNum].addKey("EBI_SMC_MODE_BAT_BYTE_WRITE", "1", "Byte Write Access Type")
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setSelectedKey("EBI_SMC_MODE_BAT_BYTE_SELECT", 2)
        ebiSmcSym_MODE_BAT[ebiChipSelNum].setDependencies(ebiSmcByteAccessSelModeVisible, ["EBI_SMC_DATA_BUS_CS" + str(ebiChipSelNum)])

        ebiSmcSym_MODE_PMEN = ebiComponent.createBooleanSymbol("EBI_SMC_PMEN_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_PMEN.setLabel("Enable Page mode")
        ebiSmcSym_MODE_PMEN.setDefaultValue(False)

        ebiSmcSym_MODE_PS.append(ebiChipSelNum)
        ebiSmcSym_MODE_PS[ebiChipSelNum] = ebiComponent.createKeyValueSetSymbol("EBI_SMC_PS_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_PS[ebiChipSelNum].setOutputMode("Key")
        ebiSmcSym_MODE_PS[ebiChipSelNum].setDisplayMode("Description")
        ebiSmcSym_MODE_PS[ebiChipSelNum].setLabel("External Memory Page Size")
        ebiSmcSym_MODE_PS[ebiChipSelNum].setVisible(False)
        ebiSmcSym_MODE_PS[ebiChipSelNum].addKey("EBI_SMC_MODE_PS_4_BYTE", "0", "4-bytes")
        ebiSmcSym_MODE_PS[ebiChipSelNum].addKey("EBI_SMC_MODE_PS_8_BYTE", "1", "8-bytes")
        ebiSmcSym_MODE_PS[ebiChipSelNum].addKey("EBI_SMC_MODE_PS_16_BYTE", "2", "16-bytes")
        ebiSmcSym_MODE_PS[ebiChipSelNum].addKey("EBI_SMC_MODE_PS_32_BYTE", "3", "32-bytes")
        ebiSmcSym_MODE_PS[ebiChipSelNum].setSelectedKey("EBI_SMC_MODE_PS_4_BYTE", 2)
        ebiSmcSym_MODE_PS[ebiChipSelNum].setDependencies(ebiSmcMemoryPageSizeModeVisible, ["EBI_SMC_PMEN_CS" + str(ebiChipSelNum)])

        ebiSmcSym_MODE_TDF = ebiComponent.createBooleanSymbol("EBI_SMC_TDF_OPTIMIZATION_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_TDF.setLabel("Enable Optimization of Data Float Time")
        ebiSmcSym_MODE_TDF.setDefaultValue(False)

        ebiSmcSym_MODE_TDF_CYCLES.append(ebiChipSelNum)
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum] = ebiComponent.createIntegerSymbol("EBI_SMC_TDF_CYCLES_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setLabel("Data Float Time (no of cycles)")
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setVisible(False)
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setMin(EBI_SMC_DEFAULT_MIN_VALUE)
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setMax(ebiSmcConvertMaskToInt(ebiSmcRegBitField_MODE_TDF_CYCLES.getAttribute("mask")))
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setDefaultValue(EBI_SMC_MODE_TDF_CYCLES_DEFAULT_VALUE)
        ebiSmcSym_MODE_TDF_CYCLES[ebiChipSelNum].setDependencies(ebiSmcTdfCyclesModeVisible, ["EBI_SMC_TDF_OPTIMIZATION_CS" + str(ebiChipSelNum)])

        ebiSmcSym_MODE_EXNW = ebiComponent.createKeyValueSetSymbol("EBI_SMC_NWAIT_MODE_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_EXNW.setOutputMode("Key")
        ebiSmcSym_MODE_EXNW.setDisplayMode("Description")
        ebiSmcSym_MODE_EXNW.setLabel("External Wait Signal (NWAIT)")
        ebiSmcSym_MODE_EXNW.addKey("EBI_SMC_MODE_EXNW_MODE_DISABLED", "0", "Disable")
        ebiSmcSym_MODE_EXNW.addKey("EBI_SMC_MODE_EXNW_MODE_FROZEN", "2", "Frozen Mode")
        ebiSmcSym_MODE_EXNW.addKey("EBI_SMC_MODE_EXNW_MODE_READY", "3", "Ready Mode")
        ebiSmcSym_MODE_EXNW.setSelectedKey("EBI_SMC_MODE_EXNW_MODE_DISABLED", 2)

        ebiSmcSym_MODE_READ = ebiComponent.createBooleanSymbol("EBI_SMC_READ_ENABLE_MODE_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_READ.setLabel("Read Operation is controlled by NRD Signal")
        ebiSmcSym_MODE_READ.setDefaultValue(True)

        ebiSmcSym_MODE_WRITE = ebiComponent.createBooleanSymbol("EBI_SMC_WRITE_ENABLE_MODE_CS" + str(ebiChipSelNum), ebiSmcSym_MODE_CS_REGISTER)
        ebiSmcSym_MODE_WRITE.setLabel("Write Operation is controlled by NWE Signal")
        ebiSmcSym_MODE_WRITE.setDefaultValue(True)

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    ebiHeader1File = ebiComponent.createFileSymbol("PLIB_EBI_H", None)
    ebiHeader1File.setSourcePath("../peripheral/ebi_03591/templates/plib_ebi.h.ftl")
    ebiHeader1File.setOutputName("plib_"+ebiInstanceName.getValue().lower()+".h")
    ebiHeader1File.setDestPath("/peripheral/ebi/")
    ebiHeader1File.setProjectPath("config/" + configName + "/peripheral/ebi/")
    ebiHeader1File.setType("HEADER")
    ebiHeader1File.setMarkup(True)

    ebiSource1File = ebiComponent.createFileSymbol("PLIB_EBI_C", None)
    ebiSource1File.setSourcePath("../peripheral/ebi_03591/templates/plib_ebi.c.ftl")
    ebiSource1File.setOutputName("plib_"+ebiInstanceName.getValue().lower()+".c")
    ebiSource1File.setDestPath("/peripheral/ebi/")
    ebiSource1File.setProjectPath("config/" + configName + "/peripheral/ebi/")
    ebiSource1File.setType("SOURCE")
    ebiSource1File.setMarkup(True)

    #Add EBI related code to common files
    ebiHeader1FileEntry = ebiComponent.createFileSymbol("PLIB_EBI_DEFINITIONS_H", None)
    ebiHeader1FileEntry.setType("STRING")
    ebiHeader1FileEntry.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ebiHeader1FileEntry.setSourcePath("../peripheral/ebi_03591/templates/system/definitions.h.ftl")
    ebiHeader1FileEntry.setMarkup(True)

    ebiSystemInitFile = ebiComponent.createFileSymbol("PLIB_EBI_INITIALIZE_H", None)
    ebiSystemInitFile.setType("STRING")
    ebiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ebiSystemInitFile.setSourcePath("../peripheral/ebi_03591/templates/system/initialization.c.ftl")
    ebiSystemInitFile.setMarkup(True)
