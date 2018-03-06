#************************** SDRAM Controller Module ***************************

#------------------------------------------------------------------------------
#							  Dependency Functions 
#------------------------------------------------------------------------------

# Function to get Core Clock Frequency
def getCoreClkFrequency():
	return int(Database.getSymbolValue("core", "PROCESSORCLK_FREQ"))

# Function to get Master Clock Frequency
def getMasterClkFrequency():
	return int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))

# Function to convert Bitfield mask string to Integer
def sdramcConvertMaskToInt(sdramcRegMask):
	sdramcHexStr 	= sdramcRegMask.rstrip("0")
	print("sdramcHexStr: " + str(sdramcHexStr))
	sdramcIntValue = int(sdramcHexStr, 0)
	
	return sdramcIntValue

# Function to Enable/Disable SDRAM Memory Controller Scrambling
def sdramcMemScramVisible(sdramcMemScrambling, event) :
	sdramcMemScramblingEnable = sdramcMemScrambling.getComponent().getSymbolByID(event["id"])

	if(sdramcMemScramblingEnable.getValue() == True):
		print("Enabled SDRAM Memory Controller Scrambling")
		sdramcMemScrambling.setVisible(True)
	else :
		print("Disabled SDRAM Memory Controller Scrambling")
		sdramcMemScrambling.setVisible(False)

# Function to Enable/Disable SDRAM Low-Power Configurations
def sdramcMemDeviceLowPowVisible(sdramcMemDeviceTypeLowPower, event) :
	sdramcMemDeviceTypeLowPowerSel = sdramcMemDeviceTypeLowPower.getComponent().getSymbolByID(event["id"])

	if(sdramcMemDeviceTypeLowPowerSel.getValue() == "LOW_POWER_SDRAM"):
		print("Enabled SDRAMC Low-Power Configurations")
		sdramcMemDeviceTypeLowPower.setVisible(True)
	else :
		print("Disabled SDRAMC Low-Power Configurations")
		sdramcMemDeviceTypeLowPower.setVisible(False)

# Function to set label based on the Refresh time in ms as selected in Combo Symbol SDRAMC_CR_NR
def sdramcRefTimeInMsSetLabel(symbol, event) :
	sdramcDevFeatNumOfRowsSel = symbol.getComponent().getSymbolByID(event["id"])
	sdramNumOfRows = sdramcDevFeatNumOfRowsSel.getValue()
	
	symbol.setLabel("**** Refresh time in ms for " + str(sdramNumOfRows) + " ****")


# Get SDRAMC Register
sdramcRegModule = Register.getRegisterModule("SDRAMC")

#------------------------------------------------------------------------------
# 				SDRAMC Register | Bitfield | Mask | Value Group
#------------------------------------------------------------------------------

# SDRAMC Chip Select Register Group
sdramcRegGroup = sdramcRegModule.getRegisterGroup("SDRAMC")

# SDRAMC_MR Register Bitfield and Value Group name
sdramcReg_MR 				= sdramcRegGroup.getRegister("SDRAMC_MR")
sdramcRegBitField_MR_MODE	= sdramcReg_MR.getBitfield("MODE")
sdramcValGrp_MR_MODE 		= sdramcRegModule.getValueGroup(sdramcRegBitField_MR_MODE.getValueGroupName())

# SDRAMC_TR Register Bitfield name
sdramcReg_TR 				= sdramcRegGroup.getRegister("SDRAMC_TR")
sdramcRegBitField_TR_COUNT	= sdramcReg_TR.getBitfield("COUNT")

# SDRAMC_MR Register Bitfield and Value Group names
sdramcReg_CR 						= sdramcRegGroup.getRegister("SDRAMC_CR")
sdramcRegBitField_CR_NC				= sdramcReg_CR.getBitfield("NC")
sdramcRegBitField_CR_NR				= sdramcReg_CR.getBitfield("NR")
sdramcRegBitField_CR_NB				= sdramcReg_CR.getBitfield("NB")
sdramcRegBitField_CR_CAS			= sdramcReg_CR.getBitfield("CAS")
sdramcRegBitField_CR_DBW			= sdramcReg_CR.getBitfield("DBW")
sdramcRegBitField_CR_TWR			= sdramcReg_CR.getBitfield("TWR")
sdramcRegBitField_CR_TWR_MASK		= sdramcConvertMaskToInt("0x00000F00")
sdramcRegBitField_CR_TRC_TRFC		= sdramcReg_CR.getBitfield("TRC_TRFC")
sdramcRegBitField_CR_TRC_TRFC_MASK	= sdramcConvertMaskToInt("0x0000F000")
sdramcRegBitField_CR_TRP			= sdramcReg_CR.getBitfield("TRP")
sdramcRegBitField_CR_TRP_MASK		= sdramcConvertMaskToInt("0x000F0000")
sdramcRegBitField_CR_TRCD			= sdramcReg_CR.getBitfield("TRCD")
sdramcRegBitField_CR_TRCD_MASK		= sdramcConvertMaskToInt("0x00F00000")
sdramcRegBitField_CR_TRAS			= sdramcReg_CR.getBitfield("TRAS")
sdramcRegBitField_CR_TRAS_MASK		= sdramcConvertMaskToInt("0x0F000000")
sdramcRegBitField_CR_TXSR			= sdramcReg_CR.getBitfield("TXSR")
sdramcRegBitField_CR_TXSR_MASK		= sdramcConvertMaskToInt("0xF0000000")
sdramcValGrp_CR_NC 					= sdramcRegModule.getValueGroup(sdramcRegBitField_CR_NC.getValueGroupName())
sdramcValGrp_CR_NR 					= sdramcRegModule.getValueGroup(sdramcRegBitField_CR_NR.getValueGroupName())
sdramcValGrp_CR_NB 					= sdramcRegModule.getValueGroup(sdramcRegBitField_CR_NB.getValueGroupName())
sdramcValGrp_CR_CAS					= sdramcRegModule.getValueGroup(sdramcRegBitField_CR_CAS.getValueGroupName())

# SDRAMC_LPR Register Bitfield and Value Group name
sdramcReg_LPR 						= sdramcRegGroup.getRegister("SDRAMC_LPR")
sdramcRegBitField_LPR_LPCB			= sdramcReg_LPR.getBitfield("LPCB")
sdramcRegBitField_LPR_PASR			= sdramcReg_LPR.getBitfield("PASR")
sdramcRegBitField_LPR_TCSR			= sdramcReg_LPR.getBitfield("TCSR")
sdramcRegBitField_LPR_DS			= sdramcReg_LPR.getBitfield("DS")
sdramcRegBitField_LPR_TIMEOUT		= sdramcReg_LPR.getBitfield("TIMEOUT")
sdramcValGrp_LPR_LPCB 				= sdramcRegModule.getValueGroup(sdramcRegBitField_LPR_LPCB.getValueGroupName())
sdramcValGrp_LPR_TIMEOUT 			= sdramcRegModule.getValueGroup(sdramcRegBitField_LPR_TIMEOUT.getValueGroupName())

# SDRAMC_IER Register Bitfield name
sdramcReg_IER 				= sdramcRegGroup.getRegister("SDRAMC_IER")
sdramcRegBitField_IER_RES	= sdramcReg_IER.getBitfield("RES")

# SDRAMC_IDR Register Bitfield name
sdramcReg_IDR 				= sdramcRegGroup.getRegister("SDRAMC_IDR")
sdramcRegBitField_IDR_RES	= sdramcReg_IDR.getBitfield("RES")

# SDRAMC_IMR Register Bitfield name
sdramcReg_IMR 				= sdramcRegGroup.getRegister("SDRAMC_IMR")
sdramcRegBitField_IMR_RES	= sdramcReg_IMR.getBitfield("RES")

# SDRAMC_ISR Register Bitfield name
sdramcReg_ISR 				= sdramcRegGroup.getRegister("SDRAMC_ISR")
sdramcRegBitField_ISR_RES	= sdramcReg_ISR.getBitfield("RES")

# SDRAMC_MDR Register Bitfield name
sdramcReg_MDR 				= sdramcRegGroup.getRegister("SDRAMC_MDR")
sdramcRegBitField_MDR_MD	= sdramcReg_MDR.getBitfield("MD")
sdramcValGrp_MDR_MD 		= sdramcRegModule.getValueGroup(sdramcRegBitField_MDR_MD.getValueGroupName())

# SDRAMC_CFR1 Register Bitfield name
sdramcReg_CFR1 					= sdramcRegGroup.getRegister("SDRAMC_CFR1")
sdramcRegBitField_CFR1_TMRD		= sdramcReg_CFR1.getBitfield("TMRD")
sdramcRegBitField_CR_TMRD_MASK	= sdramcConvertMaskToInt("0x0000000F")
sdramcRegBitField_CFR1_UNAL		= sdramcReg_CFR1.getBitfield("UNAL")
sdramcValGrp_CFR1_UNAL 			= sdramcRegModule.getValueGroup(sdramcRegBitField_CFR1_UNAL.getValueGroupName())

# SDRAMC_OCMS Register Bitfield name
sdramcReg_OCMS 					= sdramcRegGroup.getRegister("SDRAMC_OCMS")
sdramcRegBitField_OCMS_SDR_SE	= sdramcReg_OCMS.getBitfield("SDR_SE")

# SDRAMC_OCMS Register Bitfield name
sdramcReg_OCMS_KEY1 				= sdramcRegGroup.getRegister("SDRAMC_OCMS_KEY1")
sdramcRegBitField_OCMS_KEY1			= sdramcReg_OCMS_KEY1.getBitfield("KEY1")

# SDRAMC_OCMS Register Bitfield name
sdramcReg_OCMS_KEY2 		= sdramcRegGroup.getRegister("SDRAMC_OCMS_KEY2")
sdramcRegBitField_OCMS_KEY2	= sdramcReg_OCMS_KEY2.getBitfield("KEY2")

#------------------------------------------------------------------------------
#									Constants 
#------------------------------------------------------------------------------

# Min Zero Value
SDRAMC_DEFAULT_MIN_VALUE 				= 0

# Deafult value for SDRAMC Data Bus Width Register
SDRAMC_DBW_DEFAULT_VALUE 				= 16

# Deafult value for SDRAMC Off-Chip Memory Scrambling Key1 and Key2
SDRAMC_MEM_SCRAM_KEY_DEFAULT_VALUE 		= 0x00000000

# Default SDRAMC Timing value
SDRAMC_TIMING_DEFAULT_VALUE 			= 15

# Max SDRAMC Refresh Timing value
SDRAMC_REFRESH_TIME_IN_MS_MAX_VALUE		= 1000

# Min SDRAMC Refresh Timing value
SDRAMC_REFRESH_TIME_IN_MS_MIN_VALUE		= 1

# Default SDRAMC Refresh Timing value
SDRAMC_REFRESH_TIME_IN_MS_DEFAULT_VALUE	= 32

# Deafult Burst Length Value
SDRAMC_BURST_LENGHT_MAX_VALUE			= 7

# Min SDRAMC Configuration Register, CAS Latency Value
SDRAMC_CR_CAS_MIN_VALUE					= 1

# Max SDRAMC Configuration Register, CAS Latency Value
SDRAMC_CR_CAS_MAX_VALUE					= 3

# Default SDRAMC Configuration Register, Active to Precharge Delay (TRAS) Value
SDRAMC_CR_TRAS_MASK_DEFAULT_VALUE		= 6

# Default SDRAMC Configuration Register, Row to Column Delay (CR) Value
SDRAMC_CR_TRCD_DEFAULT_VALUE			= 3

# Default SDRAMC Configuration Register, Row Precharge Delay (TRP) Value
SDRAMC_CR_TRP_DEFAULT_VALUE				= 3

# Default SDRAMC Configuration Register, Row Cycle Delay and Row Refresh Cycle (TRC_TRFC) Value
SDRAMC_CR_TRC_TRFC_DEFAULT_VALUE		= 9

# Default SDRAMC Configuration Register, Write Recovery Delay (TWR) Value
SDARMC_CR_TWR_DEFAULT_VALUE				= 2

# Default SDRAMC Configuration Register, Exit Self-Refresh to Active Delay (TXSR) Value
SDARMC_CR_TXSR_DEFAULT_VALUE			= 15

# Default SDRAMC Configuration Register1, Load Mode Register Command to Active or Refresh Command (TMRD) Value
SDARMC_CR_TMRD_DEFAULT_VALUE			= 2

# Max SDRAMC Low Power Register, (PASR) Partial Array Self-refresh (only for low-power SDRAM) Value
SDRAMC_LPR_PASR_MAX_VALUE				= 7

# Max SDRAMC Low Power Register, (TCSR) Temperature Compensated Self-Refresh (only for low-power SDRAM) Value
SDRAMC_LPR_TCSR_MAX_VALUE				= 7

# Max SDRAMC Low Power Register, (DS) Drive Strength (only for low-power SDRAM) Value
SDRAMC_LPR_DS_MAX_VALUE					= 3

#------------------------------------------------------------------------------
#							  Combo Symbol Values
#------------------------------------------------------------------------------

# Number of Column Bits.
comboSdramColBitValues 			= ["256_COLS", "512_COLS", "1024_COLS", "2048_COLS"]

# Number of Row Bits.
comboSdramRowBitValues 			= ["2048_ROWS", "4096_ROWS", "8192_ROWS"]

# Number of Banks.
comboSdramBankValues 			= ["2_BANKS", "4_BANKS"]

# Number of Banks.
comboSdramBurstTypeValues		= ["SEQUENTIAL", "INTERLEAVED"]

# Memory Device Type.
comboSdramMemDevTypeValues		= ["SDRAM", "LOW_POWER_SDRAM"]

# Memory Device Type.
comboSdramLowPowLastXfrValues	= ["LAST_TRANSFER_NO_DELAY", "LAST_TRANSFER_64_CYCLES", "LAST_TRANSFER_128_CYCLES"]

#------------------------------------------------------------------------------		
#							Instantiate SDRAMC Component
#------------------------------------------------------------------------------
def instantiateComponent(sdramcComponent):

	num = sdramcComponent.getID()[-1:]

	Log.writeInfoMessage("--------------------------------------------------------------------")
	Log.writeInfoMessage("************************** Running SDRAMC"+ str(num) +" *************************")
	Log.writeInfoMessage("--------------------------------------------------------------------")
	
	sdramcMenu = sdramcComponent.createMenuSymbol(None, None)
	sdramcMenu.setLabel("SDRAMC Configurations")

	# SDRAMC Device features.
	sdramcSym_GlobalFeat = sdramcComponent.createMenuSymbol("SDRAMC_GLOBAL_FEAT", sdramcMenu)
	sdramcSym_GlobalFeat.setLabel("SDRAMC Device Features")

	sdramcSymCoreClockFreq = getCoreClkFrequency()

	sdramcSymClkFreq = sdramcComponent.createIntegerSymbol("SDRAMC_CORE_CLK_FREQ", sdramcSym_GlobalFeat)
	sdramcSymClkFreq.setLabel("Get Core Clock Frequency")
	sdramcSymClkFreq.setVisible(False)
	sdramcSymClkFreq.setDefaultValue(sdramcSymCoreClockFreq)

	sdramcSymMasterClockFreq = getMasterClkFrequency()

	sdramcSymMasterClkFreq = sdramcComponent.createIntegerSymbol("SDRAMC_MASTER_CLK_FREQ", sdramcSym_GlobalFeat)
	sdramcSymMasterClkFreq.setLabel("Get System Clock Frequency")
	sdramcSymMasterClkFreq.setVisible(False)
	sdramcSymMasterClkFreq.setDefaultValue(sdramcSymMasterClockFreq)

	sdramcSym_MDR = sdramcComponent.createComboSymbol("SDRAMC_MDR", sdramcSym_GlobalFeat, comboSdramMemDevTypeValues)
	sdramcSym_MDR.setLabel(sdramcRegBitField_MDR_MD.getDescription())
	sdramcSym_MDR.setDefaultValue("SDRAM")

	sdramcSym_CR_NC = sdramcComponent.createComboSymbol("SDRAMC_CR_NC", sdramcSym_GlobalFeat, comboSdramColBitValues)
	sdramcSym_CR_NC.setLabel(sdramcRegBitField_CR_NC.getDescription())
	sdramcSym_CR_NC.setDefaultValue("256_COLS")

	sdramcSym_CR_NR = sdramcComponent.createComboSymbol("SDRAMC_CR_NR", sdramcSym_GlobalFeat, comboSdramRowBitValues)
	sdramcSym_CR_NR.setLabel(sdramcRegBitField_CR_NR.getDescription())
	sdramcSym_CR_NR.setDefaultValue("2048_ROWS")

	sdramcSym_CR_NB = sdramcComponent.createComboSymbol("SDRAMC_CR_NB", sdramcSym_GlobalFeat, comboSdramBankValues)
	sdramcSym_CR_NB.setLabel(sdramcRegBitField_CR_NB.getDescription())
	sdramcSym_CR_NB.setDefaultValue("2_BANKS")

	sdramcSym_CR_DBW = sdramcComponent.createIntegerSymbol("SDRAMC_CR_DBW", sdramcSym_GlobalFeat)
	sdramcSym_CR_DBW.setLabel(sdramcRegBitField_CR_DBW.getDescription())
	sdramcSym_CR_DBW.setMin(SDRAMC_DBW_DEFAULT_VALUE)
	sdramcSym_CR_DBW.setMax(SDRAMC_DBW_DEFAULT_VALUE)
	sdramcSym_CR_DBW.setDefaultValue(SDRAMC_DBW_DEFAULT_VALUE)
	sdramcSym_CR_DBW.setReadOnly(True)

	sdramcSym_OCMS_SDR_SE = sdramcComponent.createBooleanSymbol("SDRAMC_OCMS_SDR_SE", sdramcSym_GlobalFeat)
	sdramcSym_OCMS_SDR_SE.setLabel("Enable Memory Scrambling?")

	# Off-chip Memory Scrambling configuration options.	
	sdramcSymMenu_OCMS_MENU = sdramcComponent.createMenuSymbol("SDRAMC_OCMS_MENU", sdramcSym_GlobalFeat)
	sdramcSymMenu_OCMS_MENU.setLabel("SDRAMC Off-Chip Memory Scrambling Configurations")
	sdramcSymMenu_OCMS_MENU.setVisible(False)
	sdramcSymMenu_OCMS_MENU.setDependencies(sdramcMemScramVisible, ["SDRAMC_OCMS_SDR_SE"])

	sdramcSym_OCMS_KEY1 = sdramcComponent.createHexSymbol("SDRAMC_OCMS_KEY1", sdramcSymMenu_OCMS_MENU)
	sdramcSym_OCMS_KEY1.setLabel(sdramcRegBitField_OCMS_KEY1.getDescription())
	sdramcSym_OCMS_KEY1.setDefaultValue(SDRAMC_MEM_SCRAM_KEY_DEFAULT_VALUE)

	sdramcSym_OCMS_KEY2 = sdramcComponent.createHexSymbol("SDRAMC_OCMS_KEY2", sdramcSymMenu_OCMS_MENU)
	sdramcSym_OCMS_KEY2.setLabel(sdramcRegBitField_OCMS_KEY2.getDescription())
	sdramcSym_OCMS_KEY2.setDefaultValue(SDRAMC_MEM_SCRAM_KEY_DEFAULT_VALUE)

	# SDRAMC Mode Configuration
	sdramcSymMenu_MR_MENU = sdramcComponent.createMenuSymbol("SDRAMC_MR_MENU", sdramcSym_GlobalFeat)
	sdramcSymMenu_MR_MENU.setLabel("SDRAMC Mode Register Configurations")

	sdramcSym_BURST_LENGTH = sdramcComponent.createIntegerSymbol("SDRAMC_BURST_LENGTH", sdramcSymMenu_MR_MENU)
	sdramcSym_BURST_LENGTH.setLabel("Burst Length")
	sdramcSym_BURST_LENGTH.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_BURST_LENGTH.setMax(SDRAMC_BURST_LENGHT_MAX_VALUE)
	sdramcSym_BURST_LENGTH.setDefaultValue(SDRAMC_DEFAULT_MIN_VALUE)

	sdramcSym_BURST_TYPE = sdramcComponent.createComboSymbol("SDRAMC_BURST_TYPE", sdramcSymMenu_MR_MENU, comboSdramBurstTypeValues)
	sdramcSym_BURST_TYPE.setLabel("Burst Type")
	sdramcSym_BURST_TYPE.setDefaultValue("SEQUENTIAL")

	# SDRAMC Timing Parameters
	sdramcSymMenu_TIMING_MENU = sdramcComponent.createMenuSymbol("SDRAMC_TIMING_MENU", sdramcSym_GlobalFeat)
	sdramcSymMenu_TIMING_MENU.setLabel("SDRAMC Timing Register Parameters")

	sdramcSym_CR_TRCD = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TRCD", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_TRCD.setLabel(sdramcRegBitField_CR_TRCD.getDescription())
	sdramcSym_CR_TRCD.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TRCD.setMax(sdramcRegBitField_CR_TRCD_MASK)
	sdramcSym_CR_TRCD.setDefaultValue(SDRAMC_CR_TRCD_DEFAULT_VALUE)

	sdramcSym_CR_CAS = sdramcComponent.createIntegerSymbol("SDRAMC_CR_CAS", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_CAS.setLabel(sdramcRegBitField_CR_CAS.getDescription())
	sdramcSym_CR_CAS.setMin(SDRAMC_CR_CAS_MIN_VALUE)
	sdramcSym_CR_CAS.setMax(SDRAMC_CR_CAS_MAX_VALUE)
	sdramcSym_CR_CAS.setDefaultValue(SDRAMC_CR_CAS_MAX_VALUE)

	sdramcSym_CR_TRAS = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TRAS", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_TRAS.setLabel(sdramcRegBitField_CR_TRAS.getDescription())
	sdramcSym_CR_TRAS.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TRAS.setMax(sdramcRegBitField_CR_TRAS_MASK)
	sdramcSym_CR_TRAS.setDefaultValue(SDRAMC_CR_TRAS_MASK_DEFAULT_VALUE)

	sdramcSym_CR_TRP = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TRP", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_TRP.setLabel(sdramcRegBitField_CR_TRP.getDescription())
	sdramcSym_CR_TRP.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TRP.setMax(sdramcRegBitField_CR_TRP_MASK)
	sdramcSym_CR_TRP.setDefaultValue(SDRAMC_CR_TRP_DEFAULT_VALUE)

	sdramcSym_CR_TRC_TRFC = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TRC_TRFC", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_TRC_TRFC.setLabel(sdramcRegBitField_CR_TRC_TRFC.getDescription())
	sdramcSym_CR_TRC_TRFC.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TRC_TRFC.setMax(sdramcRegBitField_CR_TRC_TRFC_MASK)
	sdramcSym_CR_TRC_TRFC.setDefaultValue(SDRAMC_CR_TRC_TRFC_DEFAULT_VALUE)

	sdramcSym_CR_TWR = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TWR", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CR_TWR.setLabel(sdramcRegBitField_CR_TWR.getDescription())
	sdramcSym_CR_TWR.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TWR.setMax(sdramcRegBitField_CR_TWR_MASK)
	sdramcSym_CR_TWR.setDefaultValue(SDARMC_CR_TWR_DEFAULT_VALUE)

	sdramcSym_CFR1_TMRD = sdramcComponent.createIntegerSymbol("SDRAMC_CFR1_TMRD", sdramcSymMenu_TIMING_MENU)
	sdramcSym_CFR1_TMRD.setLabel(sdramcRegBitField_CFR1_TMRD.getDescription())
	sdramcSym_CFR1_TMRD.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CFR1_TMRD.setMax(sdramcRegBitField_CR_TMRD_MASK)
	sdramcSym_CFR1_TMRD.setDefaultValue(SDARMC_CR_TMRD_DEFAULT_VALUE)

	sdramcSym_REF_TIME_IN_MS_COMMENT = sdramcComponent.createCommentSymbol("SDRAMC_REFRESH_TIME_IN_MS_COMMENT", sdramcSymMenu_TIMING_MENU)
	sdramcSym_REF_TIME_IN_MS_COMMENT.setLabel("**** Refresh time in ms for 2048_ROWS ****")
	sdramcSym_REF_TIME_IN_MS_COMMENT.setVisible(True)
	sdramcSym_REF_TIME_IN_MS_COMMENT.setDependencies(sdramcRefTimeInMsSetLabel, ["SDRAMC_CR_NR"])

	sdramcSym_REFRESH_TIME_IN_MS = sdramcComponent.createIntegerSymbol("SDRAMC_REFRESH_TIME_IN_MS", sdramcSym_REF_TIME_IN_MS_COMMENT)
	sdramcSym_REFRESH_TIME_IN_MS.setLabel("Refresh time in ms")
	sdramcSym_REFRESH_TIME_IN_MS.setMin(SDRAMC_REFRESH_TIME_IN_MS_MIN_VALUE)
	sdramcSym_REFRESH_TIME_IN_MS.setMax(SDRAMC_REFRESH_TIME_IN_MS_MAX_VALUE)
	sdramcSym_REFRESH_TIME_IN_MS.setDefaultValue(SDRAMC_REFRESH_TIME_IN_MS_DEFAULT_VALUE)
	
	# Low-power configuration options.
	sdramcSymMenu_LOW_POW_MENU = sdramcComponent.createMenuSymbol("SDRAMC_LOW_POW_MENU", sdramcSym_GlobalFeat)
	sdramcSymMenu_LOW_POW_MENU.setLabel("SDRAMC Low-Power Configurations")
	sdramcSymMenu_LOW_POW_MENU.setVisible(False)
	sdramcSymMenu_LOW_POW_MENU.setDependencies(sdramcMemDeviceLowPowVisible, ["SDRAMC_MDR"])

	sdramcSym_LPR_LPCB = sdramcComponent.createComboSymbol("SDRAMC_LPR_LPCB", sdramcSymMenu_LOW_POW_MENU, sdramcValGrp_LPR_LPCB.getValueNames())
	sdramcSym_LPR_LPCB.setLabel(sdramcRegBitField_LPR_LPCB.getDescription())
	sdramcSym_LPR_LPCB.setDefaultValue("SELF_REFRESH")

	sdramcSym_LPR_TIMEOUT = sdramcComponent.createComboSymbol("SDRAMC_LPR_TIMEOUT", sdramcSymMenu_LOW_POW_MENU, comboSdramLowPowLastXfrValues)
	sdramcSym_LPR_TIMEOUT.setLabel(sdramcRegBitField_LPR_TIMEOUT.getDescription())
	sdramcSym_LPR_TIMEOUT.setDefaultValue("LAST_TRANSFER_NO_DELAY")

	sdramcSym_CR_TXSR = sdramcComponent.createIntegerSymbol("SDRAMC_CR_TXSR", sdramcSymMenu_LOW_POW_MENU)
	sdramcSym_CR_TXSR.setLabel(sdramcRegBitField_CR_TXSR.getDescription())
	sdramcSym_CR_TXSR.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_CR_TXSR.setMax(sdramcRegBitField_CR_TXSR_MASK)
	sdramcSym_CR_TXSR.setDefaultValue(SDARMC_CR_TXSR_DEFAULT_VALUE)

	# Extended Mode Low-power configuration options.
	sdramcSymMenu_EXT_LOW_POW_MENU = sdramcComponent.createMenuSymbol("SDRAMC_EXT_LOW_POW_MENU", sdramcSymMenu_LOW_POW_MENU)
	sdramcSymMenu_EXT_LOW_POW_MENU.setLabel("Extended Low-Power Mode Configurations")

	sdramcSym_LPR_PASR = sdramcComponent.createIntegerSymbol("SDRAMC_LPR_PASR", sdramcSymMenu_EXT_LOW_POW_MENU)
	sdramcSym_LPR_PASR.setLabel(sdramcRegBitField_LPR_PASR.getDescription())
	sdramcSym_LPR_PASR.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_LPR_PASR.setMax(SDRAMC_LPR_PASR_MAX_VALUE)
	sdramcSym_LPR_PASR.setDefaultValue(SDRAMC_DEFAULT_MIN_VALUE)

	sdramcSym_LPR_TCSR = sdramcComponent.createIntegerSymbol("SDRAMC_LPR_TCSR", sdramcSymMenu_EXT_LOW_POW_MENU)
	sdramcSym_LPR_TCSR.setLabel(sdramcRegBitField_LPR_PASR.getDescription())
	sdramcSym_LPR_TCSR.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_LPR_TCSR.setMax(SDRAMC_LPR_TCSR_MAX_VALUE)
	sdramcSym_LPR_TCSR.setDefaultValue(SDRAMC_DEFAULT_MIN_VALUE)

	sdramcSym_LPR_DS = sdramcComponent.createIntegerSymbol("SDRAMC_LPR_DS", sdramcSymMenu_EXT_LOW_POW_MENU)
	sdramcSym_LPR_DS.setLabel(sdramcRegBitField_LPR_DS.getDescription())
	sdramcSym_LPR_DS.setMin(SDRAMC_DEFAULT_MIN_VALUE)
	sdramcSym_LPR_DS.setMax(SDRAMC_LPR_DS_MAX_VALUE)
	sdramcSym_LPR_DS.setDefaultValue(SDRAMC_DEFAULT_MIN_VALUE)

	sdramcIndex = sdramcComponent.createIntegerSymbol("INDEX", sdramcMenu)
	sdramcIndex.setVisible(False)
	sdramcIndex.setDefaultValue(int(num))	

	configName = Variables.get("__CONFIGURATION_NAME")

	sdramcHeader1File = sdramcComponent.createFileSymbol(None, None)
	sdramcHeader1File.setSourcePath("../peripheral/sdramc_" + sdramcRegModule.getID() + "/templates/plib_sdramc.h.ftl")
	sdramcHeader1File.setOutputName("plib_sdramc" + str(num) + ".h")
	sdramcHeader1File.setDestPath("/peripheral/sdramc/")
	sdramcHeader1File.setProjectPath("config/" + configName + "/peripheral/sdramc/")
	sdramcHeader1File.setType("HEADER")
	sdramcHeader1File.setMarkup(True)

	sdramcSource1File = sdramcComponent.createFileSymbol(None, None)
	sdramcSource1File.setSourcePath("../peripheral/sdramc_" + sdramcRegModule.getID() + "/templates/plib_sdramc.c.ftl")
	sdramcSource1File.setOutputName("plib_sdramc" + str(num) + ".c")
	sdramcSource1File.setDestPath("/peripheral/sdramc/")
	sdramcSource1File.setProjectPath("config/" + configName + "/peripheral/sdramc/")
	sdramcSource1File.setType("SOURCE")
	sdramcSource1File.setMarkup(True)

	#Add SDRAMC related code to common files
	sdramcHeader1FileEntry = sdramcComponent.createFileSymbol(None, None)
	sdramcHeader1FileEntry.setType("STRING")
	sdramcHeader1FileEntry.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	sdramcHeader1FileEntry.setSourcePath("../peripheral/sdramc_" + sdramcRegModule.getID() + "/templates/system/system_definitions.h.ftl")
	sdramcHeader1FileEntry.setMarkup(True)

	sdramSystemInitFile = sdramcComponent.createFileSymbol(None, None)
	sdramSystemInitFile.setType("STRING")
	sdramSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	sdramSystemInitFile.setSourcePath("../peripheral/sdramc_" + sdramcRegModule.getID() + "/templates/system/system_initialize.c.ftl")
	sdramSystemInitFile.setMarkup(True)