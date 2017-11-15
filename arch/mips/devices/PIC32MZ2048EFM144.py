DEVICE_FAMILY.setDefaultValue("PIC32MZ")
HAVE_JTAG.setDefaultValue(True)
HAVE_TRACE.setDefaultValue(True)
CRYPTO.setDefaultValue(True)

DEVCFG_FMIIEN = [
    "OFF",
    "ON"
]

DEVCFG_FETHIO = [
    "OFF",
    "ON"
]

DEVCFG_PGL1WAY = [
    "ON",
    "OFF"
]

DEVCFG_PMDL1WAY = [
    "ON",
    "OFF"
]

DEVCFG_IOL1WAY = [
    "ON",
    "OFF"
]

DEVCFG_FUSBIDIO = [
    "OFF",
    "ON"
]

DEVCFG_FPLLIDIV = [
    "DIV_1",
    "DIV_2",
    "DIV_3",
    "DIV_4",
    "DIV_5",
    "DIV_6",
    "DIV_7",
    "DIV_8"
]

DEVCFG_FPLLRNG = [
    "RANGE_BYPASS",
    "RANGE_5_10_MHZ",
    "RANGE_8_16_MHZ",
    "RANGE_13_26_MHZ",
    "RANGE_21_42_MHZ",
    "RANGE_34_68_MHZ"
]

DEVCFG_FPLLICLK = [
    "PLL_FRC",
    "PLL_POSC"
]

DEVCFG_FPLLMULT = [
    "MUL_1",
    "MUL_2",
    "MUL_3",
    "MUL_4",
    "MUL_5",
    "MUL_6",
    "MUL_7",
    "MUL_8",
    "MUL_9",
    "MUL_10",
    "MUL_11",
    "MUL_12",
    "MUL_13",
    "MUL_14",
    "MUL_15",
    "MUL_16",
    "MUL_17",
    "MUL_18",
    "MUL_19",
    "MUL_20",
    "MUL_21",
    "MUL_22",
    "MUL_23",
    "MUL_24",
    "MUL_25",
    "MUL_26",
    "MUL_27",
    "MUL_28",
    "MUL_29",
    "MUL_30",
    "MUL_31",
    "MUL_32",
    "MUL_33",
    "MUL_34",
    "MUL_35",
    "MUL_36",
    "MUL_37",
    "MUL_38",
    "MUL_39",
    "MUL_40",
    "MUL_41",
    "MUL_42",
    "MUL_43",
    "MUL_44",
    "MUL_45",
    "MUL_46",
    "MUL_47",
    "MUL_48",
    "MUL_49",
    "MUL_50",
    "MUL_51",
    "MUL_52",
    "MUL_53",
    "MUL_54",
    "MUL_55",
    "MUL_56",
    "MUL_57",
    "MUL_58",
    "MUL_59",
    "MUL_60",
    "MUL_61",
    "MUL_62",
    "MUL_63",
    "MUL_64",
    "MUL_65",
    "MUL_66",
    "MUL_67",
    "MUL_68",
    "MUL_69",
    "MUL_70",
    "MUL_71",
    "MUL_72",
    "MUL_73",
    "MUL_74",
    "MUL_75",
    "MUL_76",
    "MUL_77",
    "MUL_78",
    "MUL_79",
    "MUL_80",
    "MUL_81",
    "MUL_82",
    "MUL_83",
    "MUL_84",
    "MUL_85",
    "MUL_86",
    "MUL_87",
    "MUL_88",
    "MUL_89",
    "MUL_90",
    "MUL_91",
    "MUL_92",
    "MUL_93",
    "MUL_94",
    "MUL_95",
    "MUL_96",
    "MUL_97",
    "MUL_98",
    "MUL_99",
    "MUL_100",
    "MUL_101",
    "MUL_102",
    "MUL_103",
    "MUL_104",
    "MUL_105",
    "MUL_106",
    "MUL_107",
    "MUL_108",
    "MUL_109",
    "MUL_110",
    "MUL_111",
    "MUL_112",
    "MUL_113",
    "MUL_114",
    "MUL_115",
    "MUL_116",
    "MUL_117",
    "MUL_118",
    "MUL_119",
    "MUL_120",
    "MUL_121",
    "MUL_122",
    "MUL_123",
    "MUL_124",
    "MUL_125",
    "MUL_126",
    "MUL_127",
    "MUL_128"
]

DEVCFG_FPLLODIV = [
    "DIV_2",
    "DIV_4",
    "DIV_8",
    "DIV_16",
    "DIV_32"
]

DEVCFG_UPLLFSEL = [
    "FREQ_24MHZ",
    "FREQ_12MHZ"
]

DEVCFG_FNOSC = [
    "FRCDIV",
    "SPLL",
    "POSC",
    "SOSC",
    "LPRC"
]

DEVCFG_DMTINTV = [
    "WIN_0",
    "WIN_1_2",
    "WIN_3_4",
    "WIN_7_8",
    "WIN_15_16",
    "WIN_31_32",
    "WIN_63_64",
    "WIN_127_128"
]

DEVCFG_FSOSCEN = [
    "OFF",
    "ON"
]

DEVCFG_IESO = [
    "OFF",
    "ON"
]

DEVCFG_POSCMOD = [
    "EC",
    "HS",
    "OFF"
]

DEVCFG_OSCIOFNC = [
    "OFF",
    "ON"
]

DEVCFG_FCKSM = [
    "CSDCMD",
    "CSECMD",
    "CSDCME",
    "CSECME"
]

DEVCFG_WDTPS = [
    "PS1",
    "PS2",
    "PS4",
    "PS8",
    "PS16",
    "PS32",
    "PS64",
    "PS128",
    "PS256",
    "PS512",
    "PS1024",
    "PS2048",
    "PS4096",
    "PS8192",
    "PS16384",
    "PS32768",
    "PS65536",
    "PS131072",
    "PS262144",
    "PS524288",
    "PS1048576"
]

DEVCFG_WDTSPGM = [
    "RUN",
    "STOP"
]

DEVCFG_WINDIS = [
    "NORMAL",
    "WINDOW"
]

DEVCFG_FWDTEN = [
    "OFF",
    "ON"
]

DEVCFG_FWDTWINSZ = [
    "WINSZ_25",
    "WINSZ_37",
    "WINSZ_50",
    "WINSZ_75"
]

DEVCFG_DMTCNT = [
    "DMT8",
    "DMT9",
    "DMT10",
    "DMT11",
    "DMT12",
    "DMT13",
    "DMT14",
    "DMT15",
    "DMT16",
    "DMT17",
    "DMT18",
    "DMT19",
    "DMT20",
    "DMT21",
    "DMT22",
    "DMT23",
    "DMT24",
    "DMT25",
    "DMT26",
    "DMT27",
    "DMT28",
    "DMT29",
    "DMT30",
    "DMT31"
]

DEVCFG_FDMTEN = [
    "ON",
    "OFF"
]

DEVCFG_DEBUG = [
    "ON",
    "OFF"
]

DEVCFG_JTAGEN = [
    "ON",
    "OFF"
]

DEVCFG_ICESEL = [
    "ICS_PGx1",
    "ICS_PGx2"
]

DEVCFG_TRCEN = [
    "ON",
    "OFF"
]

DEVCFG_BOOTISA = [
    "MIPS32",
    "MICROMIPS"
]

DEVCFG_FECCCON = [
    "ON",
    "DYNAMIC",
    "OFF_LOCKED",
    "OFF_UNLOCKED"
]

DEVCFG_FSLEEP = [
    "OFF",
    "VREGS"
]

DEVCFG_DBGPER = [
    "ALLOW_PG2",
    "ALLOW_PG1",
    "ALLOW_PG0",
    "PG_1_0",
    "PG_2_0",
    "PG_2_1",
    "PG_ALL",
    "PG_NONE"
]

DEVCFG_SMCLR = [
    "MCLR_NORM",
    "MCLR_POR"
]

DEVCFG_SOSCGAIN = [
    "GAIN_2X",
    "GAIN_1_5X",
    "GAIN_0_5X",
    "GAIN_1X",
    "GAIN_LEVEL_3",
    "GAIN_LEVEL_2",
    "GAIN_LEVEL_1",
    "GAIN_LEVEL_0"
]

DEVCFG_SOSCBOOST = [
    "ON",
    "OFF"
]

DEVCFG_POSCGAIN = [
    "GAIN_2X",
    "GAIN_1_5X",
    "GAIN_0_5X",
    "GAIN_1X",
    "GAIN_LEVEL_3",
    "GAIN_LEVEL_2",
    "GAIN_LEVEL_1",
    "GAIN_LEVEL_0"
]

DEVCFG_POSCBOOST = [
    "ON",
    "OFF"
]

DEVCFG_EJTAGBEN = [
    "NORMAL",
    "REDUCED"
]

DEVCFG_CP = [
    "ON",
    "OFF"
]

devCfgMenu = coreComponent.createMenuSymbol(None, None)
devCfgMenu.setLabel("Device Configuration Bits")
devCfgMenu.setDescription("Hardware Configuration Bits")

devCfg3Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devCfg3Menu.setLabel("DEVCFG3")
devCfg3Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

USERID = coreComponent.createHexSymbol("USERID", devCfg3Menu)
USERID.setLabel("User ID (USERID)")
USERID.setDefaultValue(0xFFFF)
USERID.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FMIIEN = coreComponent.createComboSymbol("FMIIEN", devCfg3Menu, DEVCFG_FMIIEN)
FMIIEN.setLabel("Ethernet RMII/MII Enable (FMIIEN)")
FMIIEN.setDefaultValue("ON")
FMIIEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FETHIO = coreComponent.createComboSymbol("FETHIO", devCfg3Menu, DEVCFG_FETHIO)
FETHIO.setLabel("Ethernet I/O Pin Select (FETHIO)")
FETHIO.setDefaultValue("ON")
FETHIO.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

PGL1WAY = coreComponent.createComboSymbol("PGL1WAY", devCfg3Menu, DEVCFG_PGL1WAY)
PGL1WAY.setLabel("Permission Group Lock One Way Configuration (PGL1WAY)")
PGL1WAY.setDefaultValue("ON")
PGL1WAY.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

PMDL1WAY = coreComponent.createComboSymbol("PMDL1WAY", devCfg3Menu, DEVCFG_PMDL1WAY)
PMDL1WAY.setLabel("Peripheral Module Disable Configuration (PMDL1WAY)")
PMDL1WAY.setDefaultValue("ON")
PMDL1WAY.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

IOL1WAY = coreComponent.createComboSymbol("IOL1WAY", devCfg3Menu, DEVCFG_IOL1WAY)
IOL1WAY.setLabel("Peripheral Pin Select Configuration (IOL1WAY)")
IOL1WAY.setDefaultValue("ON")
IOL1WAY.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FUSBIDIO = coreComponent.createComboSymbol("FUSBIDIO", devCfg3Menu, DEVCFG_FUSBIDIO)
FUSBIDIO.setLabel("USB USBID Selection (FUSBIDIO)")
FUSBIDIO.setDefaultValue("ON")
FUSBIDIO.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

devCfg2Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devCfg2Menu.setLabel("DEVCFG2")
devCfg2Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FPLLIDIV = coreComponent.createComboSymbol("FPLLIDIV", devCfg2Menu, DEVCFG_FPLLIDIV)
FPLLIDIV.setLabel("System PLL Input Divider (FPLLIDIV)")
FPLLIDIV.setDefaultValue("DIV_8")
FPLLIDIV.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FPLLRNG = coreComponent.createComboSymbol("FPLLRNG", devCfg2Menu, DEVCFG_FPLLRNG)
FPLLRNG.setLabel("System PLL Input Range (FPLLRNG)")
FPLLRNG.setDefaultValue("RANGE_34_68_MHZ")
FPLLRNG.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FPLLICLK = coreComponent.createComboSymbol("FPLLICLK", devCfg2Menu, DEVCFG_FPLLICLK)
FPLLICLK.setLabel("System PLL Input Clock Selection (FPLLICLK)")
FPLLICLK.setDefaultValue("PLL_FRC")
FPLLICLK.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FPLLMULT = coreComponent.createComboSymbol("FPLLMULT", devCfg2Menu, DEVCFG_FPLLMULT)
FPLLMULT.setLabel("System PLL Multiplier (FPLLMULT)")
FPLLMULT.setDefaultValue("MUL_128")
FPLLMULT.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FPLLODIV = coreComponent.createComboSymbol("FPLLODIV", devCfg2Menu, DEVCFG_FPLLODIV)
FPLLODIV.setLabel("System PLL Output Clock Divider (FPLLODIV)")
FPLLODIV.setDefaultValue("DIV_32")
FPLLODIV.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

UPLLFSEL = coreComponent.createComboSymbol("UPLLFSEL", devCfg2Menu, DEVCFG_UPLLFSEL)
UPLLFSEL.setLabel("USB PLL Input Frequency Selection (UPLLFSEL)")
UPLLFSEL.setDefaultValue("FREQ_24MHZ")
UPLLFSEL.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

devCfg1Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devCfg1Menu.setLabel("DEVCFG1")
devCfg1Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FNOSC = coreComponent.createComboSymbol("FNOSC", devCfg1Menu, DEVCFG_FNOSC)
FNOSC.setLabel("Oscillator Selection Bits (FNOSC)")
FNOSC.setDefaultValue("FRCDIV")
FNOSC.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

DMTINTV = coreComponent.createComboSymbol("DMTINTV", devCfg1Menu, DEVCFG_DMTINTV)
DMTINTV.setLabel("DMT Count Window Interval (DMTINTV)")
DMTINTV.setDefaultValue("WIN_127_128")
DMTINTV.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FSOSCEN = coreComponent.createComboSymbol("FSOSCEN", devCfg1Menu, DEVCFG_FSOSCEN)
FSOSCEN.setLabel("Secondary Oscillator Enable (FSOSCEN)")
FSOSCEN.setDefaultValue("ON")
FSOSCEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

IESO = coreComponent.createComboSymbol("IESO", devCfg1Menu, DEVCFG_IESO)
IESO.setLabel("Internal/External Switch Over (IESO)")
IESO.setDefaultValue("ON")
IESO.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

POSCMOD = coreComponent.createComboSymbol("POSCMOD", devCfg1Menu, DEVCFG_POSCMOD)
POSCMOD.setLabel("Primary Oscillator Configuration (POSCMOD)")
POSCMOD.setDefaultValue("OFF")
POSCMOD.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

OSCIOFNC = coreComponent.createComboSymbol("OSCIOFNC", devCfg1Menu, DEVCFG_OSCIOFNC)
OSCIOFNC.setLabel("CLKO Output Signal Active on the OSCO Pin (OSCIOFNC)")
OSCIOFNC.setDefaultValue("OFF")
OSCIOFNC.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FCKSM = coreComponent.createComboSymbol("FCKSM", devCfg1Menu, DEVCFG_FCKSM)
FCKSM.setLabel("Clock Switching and Monitor Selection (FCKSM)")
FCKSM.setDefaultValue("CSECME")
FCKSM.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

WDTPS = coreComponent.createComboSymbol("WDTPS", devCfg1Menu, DEVCFG_WDTPS)
WDTPS.setLabel("Watchdog Timer Postscaler (WDTPS)")
WDTPS.setDefaultValue("PS1048576")
WDTPS.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

WDTSPGM = coreComponent.createComboSymbol("WDTSPGM", devCfg1Menu, DEVCFG_WDTSPGM)
WDTSPGM.setLabel("Watchdog Timer Stop During Flash Programming (WDTSPGM)")
WDTSPGM.setDefaultValue("STOP")
WDTSPGM.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

WINDIS = coreComponent.createComboSymbol("WINDIS", devCfg1Menu, DEVCFG_WINDIS)
WINDIS.setLabel("Watchdog Timer Window Mode (WINDIS)")
WINDIS.setDefaultValue("NORMAL")
WINDIS.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FWDTEN = coreComponent.createComboSymbol("FWDTEN", devCfg1Menu, DEVCFG_FWDTEN)
FWDTEN.setLabel("Watchdog Timer Enable (FWDTEN)")
FWDTEN.setDefaultValue("ON")
FWDTEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FWDTWINSZ = coreComponent.createComboSymbol("FWDTWINSZ", devCfg1Menu, DEVCFG_FWDTWINSZ)
FWDTWINSZ.setLabel("Watchdog Timer Window Size (FWDTWINSZ)")
FWDTWINSZ.setDefaultValue("WINSZ_25")
FWDTWINSZ.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

DMTCNT = coreComponent.createComboSymbol("DMTCNT", devCfg1Menu, DEVCFG_DMTCNT)
DMTCNT.setLabel("Deadman Timer Count Selection (DMTCNT)")
DMTCNT.setDefaultValue("DMT31")
DMTCNT.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FDMTEN = coreComponent.createComboSymbol("FDMTEN", devCfg1Menu, DEVCFG_FDMTEN)
FDMTEN.setLabel("Deadman Timer Enable (FDMTEN)")
FDMTEN.setDefaultValue("ON")
FDMTEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

devCfg0Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devCfg0Menu.setLabel("DEVCFG0")
devCfg0Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

DEBUG = coreComponent.createComboSymbol("DEBUG", devCfg0Menu, DEVCFG_DEBUG)
DEBUG.setLabel("Background Debugger Enable (DEBUG)")
DEBUG.setDefaultValue("OFF")
DEBUG.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

def JTAGENUpdate(JTAGEN, USE_JTAG):
	if USE_JTAG.getValue() == True:
		JTAGEN.setValue("ON")
	else:
		JTAGEN.setValue("OFF")

JTAGEN = coreComponent.createComboSymbol("JTAGEN", devCfg0Menu, DEVCFG_JTAGEN)
JTAGEN.setLabel("JTAG Enable (JTAGEN)")
JTAGEN.setDefaultValue("ON")
JTAGEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")
JTAGEN.setDependencies(JTAGENUpdate, ["SYS_DEVCON_USE_JTAG_NEEDED"])

ICESEL = coreComponent.createComboSymbol("ICESEL", devCfg0Menu, DEVCFG_ICESEL)
ICESEL.setLabel("ICE/ICD Comm Channel Select (ICESEL)")
ICESEL.setDefaultValue("ICS_PGx1")
ICESEL.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

TRCEN = coreComponent.createComboSymbol("TRCEN", devCfg0Menu, DEVCFG_TRCEN)
TRCEN.setLabel("Trace Enable (TRCEN)")
TRCEN.setDefaultValue("ON")
TRCEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

BOOTISA = coreComponent.createComboSymbol("BOOTISA", devCfg0Menu, DEVCFG_BOOTISA)
BOOTISA.setLabel("Boot ISA Selection (BOOTISA)")
BOOTISA.setDefaultValue("MIPS32")
BOOTISA.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

def showMicromipsWarning(warningComment, BOOTISA):
	warningComment.setVisible(BOOTISA.getValue() == "MICROMIPS")

micromipsWarning = coreComponent.createCommentSymbol("MICROMIPS_EXCEPTION_COMMENT", devCfg0Menu)
micromipsWarning.setLabel("**** Warning: All exceptions (and interrupts) must be compiled in microMIPS mode ****")
micromipsWarning.setDependencies(showMicromipsWarning, ["BOOTISA"])
micromipsWarning.setVisible(False)

FECCCON = coreComponent.createComboSymbol("FECCCON", devCfg0Menu, DEVCFG_FECCCON)
FECCCON.setLabel("Dynamic Flash ECC Configuration (FECCCON)")
FECCCON.setDefaultValue("OFF_UNLOCKED")
FECCCON.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

FSLEEP = coreComponent.createComboSymbol("FSLEEP", devCfg0Menu, DEVCFG_FSLEEP)
FSLEEP.setLabel("Flash Sleep Mode (FSLEEP)")
FSLEEP.setDefaultValue("OFF")
FSLEEP.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

DBGPER = coreComponent.createComboSymbol("DBGPER", devCfg0Menu, DEVCFG_DBGPER)
DBGPER.setLabel("Debug Mode CPU Access Permission (DBGPER)")
DBGPER.setDefaultValue("PG_ALL")
DBGPER.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

SMCLR = coreComponent.createComboSymbol("SMCLR", devCfg0Menu, DEVCFG_SMCLR)
SMCLR.setLabel("Soft Master Clear Enable bit (SMCLR)")
SMCLR.setDefaultValue("MCLR_NORM")
SMCLR.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

SOSCGAIN = coreComponent.createComboSymbol("SOSCGAIN", devCfg0Menu, DEVCFG_SOSCGAIN)
SOSCGAIN.setLabel("Secondary Oscillator Gain Control bits (SOSCGAIN)")
SOSCGAIN.setDefaultValue("GAIN_LEVEL_3")
SOSCGAIN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

SOSCBOOST = coreComponent.createComboSymbol("SOSCBOOST", devCfg0Menu, DEVCFG_SOSCBOOST)
SOSCBOOST.setLabel("Secondary Oscillator Boost Kick Start Enable bit (SOSCBOOST)")
SOSCBOOST.setDefaultValue("ON")
SOSCBOOST.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

POSCGAIN = coreComponent.createComboSymbol("POSCGAIN", devCfg0Menu, DEVCFG_POSCGAIN)
POSCGAIN.setLabel("Primary Oscillator Gain Control bits (POSCGAIN)")
POSCGAIN.setDefaultValue("GAIN_LEVEL_3")
POSCGAIN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

POSCBOOST = coreComponent.createComboSymbol("POSCBOOST", devCfg0Menu, DEVCFG_POSCBOOST)
POSCBOOST.setLabel("Primary Oscillator Boost Kick Start Enable bit (POSCBOOST)")
POSCBOOST.setDefaultValue("ON")
POSCBOOST.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

EJTAGBEN = coreComponent.createComboSymbol("EJTAGBEN", devCfg0Menu, DEVCFG_EJTAGBEN)
EJTAGBEN.setLabel("EJTAG Boot (EJTAGBEN)")
EJTAGBEN.setDefaultValue("NORMAL")
EJTAGBEN.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

devCp0Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devCp0Menu.setLabel("DEVCFP0")
devCp0Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

CP = coreComponent.createComboSymbol("CP", devCp0Menu, DEVCFG_CP)
CP.setLabel("Code Protect (CP)")
CP.setDefaultValue("OFF")
CP.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

devSeq3Menu = coreComponent.createMenuSymbol(None, devCfgMenu)
devSeq3Menu.setLabel("SEQ3")
devSeq3Menu.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

TSEQ = coreComponent.createHexSymbol("TSEQ", devSeq3Menu)
TSEQ.setLabel("Boot Flash True Sequence Number (TSEQ)")
TSEQ.setDefaultValue(0xFFFF)
TSEQ.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

CSEQ = coreComponent.createHexSymbol("CSEQ", devSeq3Menu)
CSEQ.setLabel("Boot Flash Complement Sequence Number (CSEQ)")
CSEQ.setDefaultValue(0xFFFF)
CSEQ.setHelp("IDH_HTML_Configuration_Bit_Settings_for_PIC32MZ2048EFM144")

rawConfigMenu = coreComponent.createMenuSymbol(None, None)
rawConfigMenu.setLabel("Raw Configuration Values")

BOOTSEL = coreComponent.createStringSymbol("BOOTSEL", rawConfigMenu)
BOOTSEL.setLabel("BOOTSEL")
BOOTSEL.setReadOnly(True)

HSUARTEN = coreComponent.createStringSymbol("HSUARTEN", rawConfigMenu)
HSUARTEN.setLabel("HSUARTEN")
HSUARTEN.setReadOnly(True)

SOSCSEL = coreComponent.createStringSymbol("SOSCSEL", rawConfigMenu)
SOSCSEL.setLabel("SOSCSEL")
SOSCSEL.setReadOnly(True)

INT_VECT_CORE_TIMER = coreComponent.createStringSymbol("INT_VECT_CORE_TIMER", rawConfigMenu)
INT_VECT_CORE_TIMER.setLabel("INT_VECT_CORE_TIMER")
INT_VECT_CORE_TIMER.setDefaultValue("0")
INT_VECT_CORE_TIMER.setReadOnly(True)

INT_VECT_CORE_SOFTWARE_0 = coreComponent.createStringSymbol("INT_VECT_CORE_SOFTWARE_0", rawConfigMenu)
INT_VECT_CORE_SOFTWARE_0.setLabel("INT_VECT_CORE_SOFTWARE_0")
INT_VECT_CORE_SOFTWARE_0.setDefaultValue("1")
INT_VECT_CORE_SOFTWARE_0.setReadOnly(True)

INT_VECT_CORE_SOFTWARE_1 = coreComponent.createStringSymbol("INT_VECT_CORE_SOFTWARE_1", rawConfigMenu)
INT_VECT_CORE_SOFTWARE_1.setLabel("INT_VECT_CORE_SOFTWARE_1")
INT_VECT_CORE_SOFTWARE_1.setDefaultValue("2")
INT_VECT_CORE_SOFTWARE_1.setReadOnly(True)

INT_VECT_EXTERNAL_0 = coreComponent.createStringSymbol("INT_VECT_EXTERNAL_0", rawConfigMenu)
INT_VECT_EXTERNAL_0.setLabel("INT_VECT_EXTERNAL_0")
INT_VECT_EXTERNAL_0.setDefaultValue("3")
INT_VECT_EXTERNAL_0.setReadOnly(True)

INT_VECT_TIMER_1 = coreComponent.createStringSymbol("INT_VECT_TIMER_1", rawConfigMenu)
INT_VECT_TIMER_1.setLabel("INT_VECT_TIMER_1")
INT_VECT_TIMER_1.setDefaultValue("4")
INT_VECT_TIMER_1.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_1_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_1_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_1_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_1_ERROR")
INT_VECT_INPUT_CAPTURE_1_ERROR.setDefaultValue("5")
INT_VECT_INPUT_CAPTURE_1_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_1 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_1", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_1.setLabel("INT_VECT_INPUT_CAPTURE_1")
INT_VECT_INPUT_CAPTURE_1.setDefaultValue("6")
INT_VECT_INPUT_CAPTURE_1.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_1 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_1", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_1.setLabel("INT_VECT_OUTPUT_COMPARE_1")
INT_VECT_OUTPUT_COMPARE_1.setDefaultValue("7")
INT_VECT_OUTPUT_COMPARE_1.setReadOnly(True)

INT_VECT_EXTERNAL_1 = coreComponent.createStringSymbol("INT_VECT_EXTERNAL_1", rawConfigMenu)
INT_VECT_EXTERNAL_1.setLabel("INT_VECT_EXTERNAL_1")
INT_VECT_EXTERNAL_1.setDefaultValue("8")
INT_VECT_EXTERNAL_1.setReadOnly(True)

INT_VECT_TIMER_2 = coreComponent.createStringSymbol("INT_VECT_TIMER_2", rawConfigMenu)
INT_VECT_TIMER_2.setLabel("INT_VECT_TIMER_2")
INT_VECT_TIMER_2.setDefaultValue("9")
INT_VECT_TIMER_2.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_2_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_2_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_2_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_2_ERROR")
INT_VECT_INPUT_CAPTURE_2_ERROR.setDefaultValue("10")
INT_VECT_INPUT_CAPTURE_2_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_2 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_2", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_2.setLabel("INT_VECT_INPUT_CAPTURE_2")
INT_VECT_INPUT_CAPTURE_2.setDefaultValue("11")
INT_VECT_INPUT_CAPTURE_2.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_2 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_2", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_2.setLabel("INT_VECT_OUTPUT_COMPARE_2")
INT_VECT_OUTPUT_COMPARE_2.setDefaultValue("12")
INT_VECT_OUTPUT_COMPARE_2.setReadOnly(True)

INT_VECT_EXTERNAL_2 = coreComponent.createStringSymbol("INT_VECT_EXTERNAL_2", rawConfigMenu)
INT_VECT_EXTERNAL_2.setLabel("INT_VECT_EXTERNAL_2")
INT_VECT_EXTERNAL_2.setDefaultValue("13")
INT_VECT_EXTERNAL_2.setReadOnly(True)

INT_VECT_TIMER_3 = coreComponent.createStringSymbol("INT_VECT_TIMER_3", rawConfigMenu)
INT_VECT_TIMER_3.setLabel("INT_VECT_TIMER_3")
INT_VECT_TIMER_3.setDefaultValue("14")
INT_VECT_TIMER_3.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_3_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_3_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_3_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_3_ERROR")
INT_VECT_INPUT_CAPTURE_3_ERROR.setDefaultValue("15")
INT_VECT_INPUT_CAPTURE_3_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_3 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_3", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_3.setLabel("INT_VECT_INPUT_CAPTURE_3")
INT_VECT_INPUT_CAPTURE_3.setDefaultValue("16")
INT_VECT_INPUT_CAPTURE_3.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_3 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_3", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_3.setLabel("INT_VECT_OUTPUT_COMPARE_3")
INT_VECT_OUTPUT_COMPARE_3.setDefaultValue("17")
INT_VECT_OUTPUT_COMPARE_3.setReadOnly(True)

INT_VECT_EXTERNAL_3 = coreComponent.createStringSymbol("INT_VECT_EXTERNAL_3", rawConfigMenu)
INT_VECT_EXTERNAL_3.setLabel("INT_VECT_EXTERNAL_3")
INT_VECT_EXTERNAL_3.setDefaultValue("18")
INT_VECT_EXTERNAL_3.setReadOnly(True)

INT_VECT_TIMER_4 = coreComponent.createStringSymbol("INT_VECT_TIMER_4", rawConfigMenu)
INT_VECT_TIMER_4.setLabel("INT_VECT_TIMER_4")
INT_VECT_TIMER_4.setDefaultValue("19")
INT_VECT_TIMER_4.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_4_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_4_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_4_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_4_ERROR")
INT_VECT_INPUT_CAPTURE_4_ERROR.setDefaultValue("20")
INT_VECT_INPUT_CAPTURE_4_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_4 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_4", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_4.setLabel("INT_VECT_INPUT_CAPTURE_4")
INT_VECT_INPUT_CAPTURE_4.setDefaultValue("21")
INT_VECT_INPUT_CAPTURE_4.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_4 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_4", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_4.setLabel("INT_VECT_OUTPUT_COMPARE_4")
INT_VECT_OUTPUT_COMPARE_4.setDefaultValue("22")
INT_VECT_OUTPUT_COMPARE_4.setReadOnly(True)

INT_VECT_EXTERNAL_4 = coreComponent.createStringSymbol("INT_VECT_EXTERNAL_4", rawConfigMenu)
INT_VECT_EXTERNAL_4.setLabel("INT_VECT_EXTERNAL_4")
INT_VECT_EXTERNAL_4.setDefaultValue("23")
INT_VECT_EXTERNAL_4.setReadOnly(True)

INT_VECT_TIMER_5 = coreComponent.createStringSymbol("INT_VECT_TIMER_5", rawConfigMenu)
INT_VECT_TIMER_5.setLabel("INT_VECT_TIMER_5")
INT_VECT_TIMER_5.setDefaultValue("24")
INT_VECT_TIMER_5.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_5_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_5_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_5_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_5_ERROR")
INT_VECT_INPUT_CAPTURE_5_ERROR.setDefaultValue("25")
INT_VECT_INPUT_CAPTURE_5_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_5 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_5", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_5.setLabel("INT_VECT_INPUT_CAPTURE_5")
INT_VECT_INPUT_CAPTURE_5.setDefaultValue("26")
INT_VECT_INPUT_CAPTURE_5.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_5 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_5", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_5.setLabel("INT_VECT_OUTPUT_COMPARE_5")
INT_VECT_OUTPUT_COMPARE_5.setDefaultValue("27")
INT_VECT_OUTPUT_COMPARE_5.setReadOnly(True)

INT_VECT_TIMER_6 = coreComponent.createStringSymbol("INT_VECT_TIMER_6", rawConfigMenu)
INT_VECT_TIMER_6.setLabel("INT_VECT_TIMER_6")
INT_VECT_TIMER_6.setDefaultValue("28")
INT_VECT_TIMER_6.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_6_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_6_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_6_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_6_ERROR")
INT_VECT_INPUT_CAPTURE_6_ERROR.setDefaultValue("29")
INT_VECT_INPUT_CAPTURE_6_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_6 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_6", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_6.setLabel("INT_VECT_INPUT_CAPTURE_6")
INT_VECT_INPUT_CAPTURE_6.setDefaultValue("30")
INT_VECT_INPUT_CAPTURE_6.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_6 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_6", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_6.setLabel("INT_VECT_OUTPUT_COMPARE_6")
INT_VECT_OUTPUT_COMPARE_6.setDefaultValue("31")
INT_VECT_OUTPUT_COMPARE_6.setReadOnly(True)

INT_VECT_TIMER_7 = coreComponent.createStringSymbol("INT_VECT_TIMER_7", rawConfigMenu)
INT_VECT_TIMER_7.setLabel("INT_VECT_TIMER_7")
INT_VECT_TIMER_7.setDefaultValue("32")
INT_VECT_TIMER_7.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_7_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_7_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_7_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_7_ERROR")
INT_VECT_INPUT_CAPTURE_7_ERROR.setDefaultValue("33")
INT_VECT_INPUT_CAPTURE_7_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_7 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_7", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_7.setLabel("INT_VECT_INPUT_CAPTURE_7")
INT_VECT_INPUT_CAPTURE_7.setDefaultValue("34")
INT_VECT_INPUT_CAPTURE_7.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_7 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_7", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_7.setLabel("INT_VECT_OUTPUT_COMPARE_7")
INT_VECT_OUTPUT_COMPARE_7.setDefaultValue("35")
INT_VECT_OUTPUT_COMPARE_7.setReadOnly(True)

INT_VECT_TIMER_8 = coreComponent.createStringSymbol("INT_VECT_TIMER_8", rawConfigMenu)
INT_VECT_TIMER_8.setLabel("INT_VECT_TIMER_8")
INT_VECT_TIMER_8.setDefaultValue("36")
INT_VECT_TIMER_8.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_8_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_8_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_8_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_8_ERROR")
INT_VECT_INPUT_CAPTURE_8_ERROR.setDefaultValue("37")
INT_VECT_INPUT_CAPTURE_8_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_8 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_8", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_8.setLabel("INT_VECT_INPUT_CAPTURE_8")
INT_VECT_INPUT_CAPTURE_8.setDefaultValue("38")
INT_VECT_INPUT_CAPTURE_8.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_8 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_8", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_8.setLabel("INT_VECT_OUTPUT_COMPARE_8")
INT_VECT_OUTPUT_COMPARE_8.setDefaultValue("39")
INT_VECT_OUTPUT_COMPARE_8.setReadOnly(True)

INT_VECT_TIMER_9 = coreComponent.createStringSymbol("INT_VECT_TIMER_9", rawConfigMenu)
INT_VECT_TIMER_9.setLabel("INT_VECT_TIMER_9")
INT_VECT_TIMER_9.setDefaultValue("40")
INT_VECT_TIMER_9.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_9_ERROR = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_9_ERROR", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_9_ERROR.setLabel("INT_VECT_INPUT_CAPTURE_9_ERROR")
INT_VECT_INPUT_CAPTURE_9_ERROR.setDefaultValue("41")
INT_VECT_INPUT_CAPTURE_9_ERROR.setReadOnly(True)

INT_VECT_INPUT_CAPTURE_9 = coreComponent.createStringSymbol("INT_VECT_INPUT_CAPTURE_9", rawConfigMenu)
INT_VECT_INPUT_CAPTURE_9.setLabel("INT_VECT_INPUT_CAPTURE_9")
INT_VECT_INPUT_CAPTURE_9.setDefaultValue("42")
INT_VECT_INPUT_CAPTURE_9.setReadOnly(True)

INT_VECT_OUTPUT_COMPARE_9 = coreComponent.createStringSymbol("INT_VECT_OUTPUT_COMPARE_9", rawConfigMenu)
INT_VECT_OUTPUT_COMPARE_9.setLabel("INT_VECT_OUTPUT_COMPARE_9")
INT_VECT_OUTPUT_COMPARE_9.setDefaultValue("43")
INT_VECT_OUTPUT_COMPARE_9.setReadOnly(True)

INT_VECT_ADC = coreComponent.createStringSymbol("INT_VECT_ADC", rawConfigMenu)
INT_VECT_ADC.setLabel("INT_VECT_ADC")
INT_VECT_ADC.setDefaultValue("44")
INT_VECT_ADC.setReadOnly(True)

INT_VECT_ADC_FIFO = coreComponent.createStringSymbol("INT_VECT_ADC_FIFO", rawConfigMenu)
INT_VECT_ADC_FIFO.setLabel("INT_VECT_ADC_FIFO")
INT_VECT_ADC_FIFO.setDefaultValue("45")
INT_VECT_ADC_FIFO.setReadOnly(True)

INT_VECT_ADC_DC1 = coreComponent.createStringSymbol("INT_VECT_ADC_DC1", rawConfigMenu)
INT_VECT_ADC_DC1.setLabel("INT_VECT_ADC_DC1")
INT_VECT_ADC_DC1.setDefaultValue("46")
INT_VECT_ADC_DC1.setReadOnly(True)

INT_VECT_ADC_DC2 = coreComponent.createStringSymbol("INT_VECT_ADC_DC2", rawConfigMenu)
INT_VECT_ADC_DC2.setLabel("INT_VECT_ADC_DC2")
INT_VECT_ADC_DC2.setDefaultValue("47")
INT_VECT_ADC_DC2.setReadOnly(True)

INT_VECT_ADC_DC3 = coreComponent.createStringSymbol("INT_VECT_ADC_DC3", rawConfigMenu)
INT_VECT_ADC_DC3.setLabel("INT_VECT_ADC_DC3")
INT_VECT_ADC_DC3.setDefaultValue("48")
INT_VECT_ADC_DC3.setReadOnly(True)

INT_VECT_ADC_DC4 = coreComponent.createStringSymbol("INT_VECT_ADC_DC4", rawConfigMenu)
INT_VECT_ADC_DC4.setLabel("INT_VECT_ADC_DC4")
INT_VECT_ADC_DC4.setDefaultValue("49")
INT_VECT_ADC_DC4.setReadOnly(True)

INT_VECT_ADC_DC5 = coreComponent.createStringSymbol("INT_VECT_ADC_DC5", rawConfigMenu)
INT_VECT_ADC_DC5.setLabel("INT_VECT_ADC_DC5")
INT_VECT_ADC_DC5.setDefaultValue("50")
INT_VECT_ADC_DC5.setReadOnly(True)

INT_VECT_ADC_DC6 = coreComponent.createStringSymbol("INT_VECT_ADC_DC6", rawConfigMenu)
INT_VECT_ADC_DC6.setLabel("INT_VECT_ADC_DC6")
INT_VECT_ADC_DC6.setDefaultValue("51")
INT_VECT_ADC_DC6.setReadOnly(True)

INT_VECT_ADC_DF1 = coreComponent.createStringSymbol("INT_VECT_ADC_DF1", rawConfigMenu)
INT_VECT_ADC_DF1.setLabel("INT_VECT_ADC_DF1")
INT_VECT_ADC_DF1.setDefaultValue("52")
INT_VECT_ADC_DF1.setReadOnly(True)

INT_VECT_ADC_DF2 = coreComponent.createStringSymbol("INT_VECT_ADC_DF2", rawConfigMenu)
INT_VECT_ADC_DF2.setLabel("INT_VECT_ADC_DF2")
INT_VECT_ADC_DF2.setDefaultValue("53")
INT_VECT_ADC_DF2.setReadOnly(True)

INT_VECT_ADC_DF3 = coreComponent.createStringSymbol("INT_VECT_ADC_DF3", rawConfigMenu)
INT_VECT_ADC_DF3.setLabel("INT_VECT_ADC_DF3")
INT_VECT_ADC_DF3.setDefaultValue("54")
INT_VECT_ADC_DF3.setReadOnly(True)

INT_VECT_ADC_DF4 = coreComponent.createStringSymbol("INT_VECT_ADC_DF4", rawConfigMenu)
INT_VECT_ADC_DF4.setLabel("INT_VECT_ADC_DF4")
INT_VECT_ADC_DF4.setDefaultValue("55")
INT_VECT_ADC_DF4.setReadOnly(True)

INT_VECT_ADC_DF5 = coreComponent.createStringSymbol("INT_VECT_ADC_DF5", rawConfigMenu)
INT_VECT_ADC_DF5.setLabel("INT_VECT_ADC_DF5")
INT_VECT_ADC_DF5.setDefaultValue("56")
INT_VECT_ADC_DF5.setReadOnly(True)

INT_VECT_ADC_DF6 = coreComponent.createStringSymbol("INT_VECT_ADC_DF6", rawConfigMenu)
INT_VECT_ADC_DF6.setLabel("INT_VECT_ADC_DF6")
INT_VECT_ADC_DF6.setDefaultValue("57")
INT_VECT_ADC_DF6.setReadOnly(True)

INT_VECT_ADC_FAULT = coreComponent.createStringSymbol("INT_VECT_ADC_FAULT", rawConfigMenu)
INT_VECT_ADC_FAULT.setLabel("INT_VECT_ADC_FAULT")
INT_VECT_ADC_FAULT.setDefaultValue("58")
INT_VECT_ADC_FAULT.setReadOnly(True)

INT_VECT_ADC_DATA0 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA0", rawConfigMenu)
INT_VECT_ADC_DATA0.setLabel("INT_VECT_ADC_DATA0")
INT_VECT_ADC_DATA0.setDefaultValue("59")
INT_VECT_ADC_DATA0.setReadOnly(True)

INT_VECT_ADC_DATA1 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA1", rawConfigMenu)
INT_VECT_ADC_DATA1.setLabel("INT_VECT_ADC_DATA1")
INT_VECT_ADC_DATA1.setDefaultValue("60")
INT_VECT_ADC_DATA1.setReadOnly(True)

INT_VECT_ADC_DATA2 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA2", rawConfigMenu)
INT_VECT_ADC_DATA2.setLabel("INT_VECT_ADC_DATA2")
INT_VECT_ADC_DATA2.setDefaultValue("61")
INT_VECT_ADC_DATA2.setReadOnly(True)

INT_VECT_ADC_DATA3 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA3", rawConfigMenu)
INT_VECT_ADC_DATA3.setLabel("INT_VECT_ADC_DATA3")
INT_VECT_ADC_DATA3.setDefaultValue("62")
INT_VECT_ADC_DATA3.setReadOnly(True)

INT_VECT_ADC_DATA4 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA4", rawConfigMenu)
INT_VECT_ADC_DATA4.setLabel("INT_VECT_ADC_DATA4")
INT_VECT_ADC_DATA4.setDefaultValue("63")
INT_VECT_ADC_DATA4.setReadOnly(True)

INT_VECT_ADC_DATA5 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA5", rawConfigMenu)
INT_VECT_ADC_DATA5.setLabel("INT_VECT_ADC_DATA5")
INT_VECT_ADC_DATA5.setDefaultValue("64")
INT_VECT_ADC_DATA5.setReadOnly(True)

INT_VECT_ADC_DATA6 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA6", rawConfigMenu)
INT_VECT_ADC_DATA6.setLabel("INT_VECT_ADC_DATA6")
INT_VECT_ADC_DATA6.setDefaultValue("65")
INT_VECT_ADC_DATA6.setReadOnly(True)

INT_VECT_ADC_DATA7 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA7", rawConfigMenu)
INT_VECT_ADC_DATA7.setLabel("INT_VECT_ADC_DATA7")
INT_VECT_ADC_DATA7.setDefaultValue("66")
INT_VECT_ADC_DATA7.setReadOnly(True)

INT_VECT_ADC_DATA8 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA8", rawConfigMenu)
INT_VECT_ADC_DATA8.setLabel("INT_VECT_ADC_DATA8")
INT_VECT_ADC_DATA8.setDefaultValue("67")
INT_VECT_ADC_DATA8.setReadOnly(True)

INT_VECT_ADC_DATA9 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA9", rawConfigMenu)
INT_VECT_ADC_DATA9.setLabel("INT_VECT_ADC_DATA9")
INT_VECT_ADC_DATA9.setDefaultValue("68")
INT_VECT_ADC_DATA9.setReadOnly(True)

INT_VECT_ADC_DATA10 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA10", rawConfigMenu)
INT_VECT_ADC_DATA10.setLabel("INT_VECT_ADC_DATA10")
INT_VECT_ADC_DATA10.setDefaultValue("69")
INT_VECT_ADC_DATA10.setReadOnly(True)

INT_VECT_ADC_DATA11 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA11", rawConfigMenu)
INT_VECT_ADC_DATA11.setLabel("INT_VECT_ADC_DATA11")
INT_VECT_ADC_DATA11.setDefaultValue("70")
INT_VECT_ADC_DATA11.setReadOnly(True)

INT_VECT_ADC_DATA12 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA12", rawConfigMenu)
INT_VECT_ADC_DATA12.setLabel("INT_VECT_ADC_DATA12")
INT_VECT_ADC_DATA12.setDefaultValue("71")
INT_VECT_ADC_DATA12.setReadOnly(True)

INT_VECT_ADC_DATA13 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA13", rawConfigMenu)
INT_VECT_ADC_DATA13.setLabel("INT_VECT_ADC_DATA13")
INT_VECT_ADC_DATA13.setDefaultValue("72")
INT_VECT_ADC_DATA13.setReadOnly(True)

INT_VECT_ADC_DATA14 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA14", rawConfigMenu)
INT_VECT_ADC_DATA14.setLabel("INT_VECT_ADC_DATA14")
INT_VECT_ADC_DATA14.setDefaultValue("73")
INT_VECT_ADC_DATA14.setReadOnly(True)

INT_VECT_ADC_DATA15 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA15", rawConfigMenu)
INT_VECT_ADC_DATA15.setLabel("INT_VECT_ADC_DATA15")
INT_VECT_ADC_DATA15.setDefaultValue("74")
INT_VECT_ADC_DATA15.setReadOnly(True)

INT_VECT_ADC_DATA16 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA16", rawConfigMenu)
INT_VECT_ADC_DATA16.setLabel("INT_VECT_ADC_DATA16")
INT_VECT_ADC_DATA16.setDefaultValue("75")
INT_VECT_ADC_DATA16.setReadOnly(True)

INT_VECT_ADC_DATA17 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA17", rawConfigMenu)
INT_VECT_ADC_DATA17.setLabel("INT_VECT_ADC_DATA17")
INT_VECT_ADC_DATA17.setDefaultValue("76")
INT_VECT_ADC_DATA17.setReadOnly(True)

INT_VECT_ADC_DATA18 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA18", rawConfigMenu)
INT_VECT_ADC_DATA18.setLabel("INT_VECT_ADC_DATA18")
INT_VECT_ADC_DATA18.setDefaultValue("77")
INT_VECT_ADC_DATA18.setReadOnly(True)

INT_VECT_ADC_DATA19 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA19", rawConfigMenu)
INT_VECT_ADC_DATA19.setLabel("INT_VECT_ADC_DATA19")
INT_VECT_ADC_DATA19.setDefaultValue("78")
INT_VECT_ADC_DATA19.setReadOnly(True)

INT_VECT_ADC_DATA20 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA20", rawConfigMenu)
INT_VECT_ADC_DATA20.setLabel("INT_VECT_ADC_DATA20")
INT_VECT_ADC_DATA20.setDefaultValue("79")
INT_VECT_ADC_DATA20.setReadOnly(True)

INT_VECT_ADC_DATA21 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA21", rawConfigMenu)
INT_VECT_ADC_DATA21.setLabel("INT_VECT_ADC_DATA21")
INT_VECT_ADC_DATA21.setDefaultValue("80")
INT_VECT_ADC_DATA21.setReadOnly(True)

INT_VECT_ADC_DATA22 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA22", rawConfigMenu)
INT_VECT_ADC_DATA22.setLabel("INT_VECT_ADC_DATA22")
INT_VECT_ADC_DATA22.setDefaultValue("81")
INT_VECT_ADC_DATA22.setReadOnly(True)

INT_VECT_ADC_DATA23 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA23", rawConfigMenu)
INT_VECT_ADC_DATA23.setLabel("INT_VECT_ADC_DATA23")
INT_VECT_ADC_DATA23.setDefaultValue("82")
INT_VECT_ADC_DATA23.setReadOnly(True)

INT_VECT_ADC_DATA24 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA24", rawConfigMenu)
INT_VECT_ADC_DATA24.setLabel("INT_VECT_ADC_DATA24")
INT_VECT_ADC_DATA24.setDefaultValue("83")
INT_VECT_ADC_DATA24.setReadOnly(True)

INT_VECT_ADC_DATA25 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA25", rawConfigMenu)
INT_VECT_ADC_DATA25.setLabel("INT_VECT_ADC_DATA25")
INT_VECT_ADC_DATA25.setDefaultValue("84")
INT_VECT_ADC_DATA25.setReadOnly(True)

INT_VECT_ADC_DATA26 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA26", rawConfigMenu)
INT_VECT_ADC_DATA26.setLabel("INT_VECT_ADC_DATA26")
INT_VECT_ADC_DATA26.setDefaultValue("85")
INT_VECT_ADC_DATA26.setReadOnly(True)

INT_VECT_ADC_DATA27 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA27", rawConfigMenu)
INT_VECT_ADC_DATA27.setLabel("INT_VECT_ADC_DATA27")
INT_VECT_ADC_DATA27.setDefaultValue("86")
INT_VECT_ADC_DATA27.setReadOnly(True)

INT_VECT_ADC_DATA28 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA28", rawConfigMenu)
INT_VECT_ADC_DATA28.setLabel("INT_VECT_ADC_DATA28")
INT_VECT_ADC_DATA28.setDefaultValue("87")
INT_VECT_ADC_DATA28.setReadOnly(True)

INT_VECT_ADC_DATA29 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA29", rawConfigMenu)
INT_VECT_ADC_DATA29.setLabel("INT_VECT_ADC_DATA29")
INT_VECT_ADC_DATA29.setDefaultValue("88")
INT_VECT_ADC_DATA29.setReadOnly(True)

INT_VECT_ADC_DATA30 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA30", rawConfigMenu)
INT_VECT_ADC_DATA30.setLabel("INT_VECT_ADC_DATA30")
INT_VECT_ADC_DATA30.setDefaultValue("89")
INT_VECT_ADC_DATA30.setReadOnly(True)

INT_VECT_ADC_DATA31 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA31", rawConfigMenu)
INT_VECT_ADC_DATA31.setLabel("INT_VECT_ADC_DATA31")
INT_VECT_ADC_DATA31.setDefaultValue("90")
INT_VECT_ADC_DATA31.setReadOnly(True)

INT_VECT_ADC_DATA32 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA32", rawConfigMenu)
INT_VECT_ADC_DATA32.setLabel("INT_VECT_ADC_DATA32")
INT_VECT_ADC_DATA32.setDefaultValue("91")
INT_VECT_ADC_DATA32.setReadOnly(True)

INT_VECT_ADC_DATA33 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA33", rawConfigMenu)
INT_VECT_ADC_DATA33.setLabel("INT_VECT_ADC_DATA33")
INT_VECT_ADC_DATA33.setDefaultValue("92")
INT_VECT_ADC_DATA33.setReadOnly(True)

INT_VECT_ADC_DATA34 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA34", rawConfigMenu)
INT_VECT_ADC_DATA34.setLabel("INT_VECT_ADC_DATA34")
INT_VECT_ADC_DATA34.setDefaultValue("93")
INT_VECT_ADC_DATA34.setReadOnly(True)

INT_VECT_ADC_DATA35 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA35", rawConfigMenu)
INT_VECT_ADC_DATA35.setLabel("INT_VECT_ADC_DATA35")
INT_VECT_ADC_DATA35.setDefaultValue("94")
INT_VECT_ADC_DATA35.setReadOnly(True)

INT_VECT_ADC_DATA36 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA36", rawConfigMenu)
INT_VECT_ADC_DATA36.setLabel("INT_VECT_ADC_DATA36")
INT_VECT_ADC_DATA36.setDefaultValue("95")
INT_VECT_ADC_DATA36.setReadOnly(True)

INT_VECT_ADC_DATA37 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA37", rawConfigMenu)
INT_VECT_ADC_DATA37.setLabel("INT_VECT_ADC_DATA37")
INT_VECT_ADC_DATA37.setDefaultValue("96")
INT_VECT_ADC_DATA37.setReadOnly(True)

INT_VECT_ADC_DATA38 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA38", rawConfigMenu)
INT_VECT_ADC_DATA38.setLabel("INT_VECT_ADC_DATA38")
INT_VECT_ADC_DATA38.setDefaultValue("97")
INT_VECT_ADC_DATA38.setReadOnly(True)

INT_VECT_ADC_DATA39 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA39", rawConfigMenu)
INT_VECT_ADC_DATA39.setLabel("INT_VECT_ADC_DATA39")
INT_VECT_ADC_DATA39.setDefaultValue("98")
INT_VECT_ADC_DATA39.setReadOnly(True)

INT_VECT_ADC_DATA40 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA40", rawConfigMenu)
INT_VECT_ADC_DATA40.setLabel("INT_VECT_ADC_DATA40")
INT_VECT_ADC_DATA40.setDefaultValue("99")
INT_VECT_ADC_DATA40.setReadOnly(True)

INT_VECT_ADC_DATA41 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA41", rawConfigMenu)
INT_VECT_ADC_DATA41.setLabel("INT_VECT_ADC_DATA41")
INT_VECT_ADC_DATA41.setDefaultValue("100")
INT_VECT_ADC_DATA41.setReadOnly(True)

INT_VECT_ADC_DATA42 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA42", rawConfigMenu)
INT_VECT_ADC_DATA42.setLabel("INT_VECT_ADC_DATA42")
INT_VECT_ADC_DATA42.setDefaultValue("101")
INT_VECT_ADC_DATA42.setReadOnly(True)

INT_VECT_ADC_DATA43 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA43", rawConfigMenu)
INT_VECT_ADC_DATA43.setLabel("INT_VECT_ADC_DATA43")
INT_VECT_ADC_DATA43.setDefaultValue("102")
INT_VECT_ADC_DATA43.setReadOnly(True)

INT_VECT_ADC_DATA44 = coreComponent.createStringSymbol("INT_VECT_ADC_DATA44", rawConfigMenu)
INT_VECT_ADC_DATA44.setLabel("INT_VECT_ADC_DATA44")
INT_VECT_ADC_DATA44.setDefaultValue("103")
INT_VECT_ADC_DATA44.setReadOnly(True)

INT_VECT_CORE_PERF_COUNT = coreComponent.createStringSymbol("INT_VECT_CORE_PERF_COUNT", rawConfigMenu)
INT_VECT_CORE_PERF_COUNT.setLabel("INT_VECT_CORE_PERF_COUNT")
INT_VECT_CORE_PERF_COUNT.setDefaultValue("104")
INT_VECT_CORE_PERF_COUNT.setReadOnly(True)

INT_VECT_CORE_FAST_DEBUG_CHAN = coreComponent.createStringSymbol("INT_VECT_CORE_FAST_DEBUG_CHAN", rawConfigMenu)
INT_VECT_CORE_FAST_DEBUG_CHAN.setLabel("INT_VECT_CORE_FAST_DEBUG_CHAN")
INT_VECT_CORE_FAST_DEBUG_CHAN.setDefaultValue("105")
INT_VECT_CORE_FAST_DEBUG_CHAN.setReadOnly(True)

INT_VECT_SYSTEM_BUS_PROTECTION = coreComponent.createStringSymbol("INT_VECT_SYSTEM_BUS_PROTECTION", rawConfigMenu)
INT_VECT_SYSTEM_BUS_PROTECTION.setLabel("INT_VECT_SYSTEM_BUS_PROTECTION")
INT_VECT_SYSTEM_BUS_PROTECTION.setDefaultValue("106")
INT_VECT_SYSTEM_BUS_PROTECTION.setReadOnly(True)

INT_VECT_CRYPTO = coreComponent.createStringSymbol("INT_VECT_CRYPTO", rawConfigMenu)
INT_VECT_CRYPTO.setLabel("INT_VECT_CRYPTO")
INT_VECT_CRYPTO.setDefaultValue("107")
INT_VECT_CRYPTO.setReadOnly(True)

INT_VECT_SPI1_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI1_FAULT", rawConfigMenu)
INT_VECT_SPI1_FAULT.setLabel("INT_VECT_SPI1_FAULT")
INT_VECT_SPI1_FAULT.setDefaultValue("109")
INT_VECT_SPI1_FAULT.setReadOnly(True)

INT_VECT_SPI1_RX = coreComponent.createStringSymbol("INT_VECT_SPI1_RX", rawConfigMenu)
INT_VECT_SPI1_RX.setLabel("INT_VECT_SPI1_RX")
INT_VECT_SPI1_RX.setDefaultValue("110")
INT_VECT_SPI1_RX.setReadOnly(True)

INT_VECT_SPI1_TX = coreComponent.createStringSymbol("INT_VECT_SPI1_TX", rawConfigMenu)
INT_VECT_SPI1_TX.setLabel("INT_VECT_SPI1_TX")
INT_VECT_SPI1_TX.setDefaultValue("111")
INT_VECT_SPI1_TX.setReadOnly(True)

INT_VECT_UART1_FAULT = coreComponent.createStringSymbol("INT_VECT_UART1_FAULT", rawConfigMenu)
INT_VECT_UART1_FAULT.setLabel("INT_VECT_UART1_FAULT")
INT_VECT_UART1_FAULT.setDefaultValue("112")
INT_VECT_UART1_FAULT.setReadOnly(True)

INT_VECT_UART1_RX = coreComponent.createStringSymbol("INT_VECT_UART1_RX", rawConfigMenu)
INT_VECT_UART1_RX.setLabel("INT_VECT_UART1_RX")
INT_VECT_UART1_RX.setDefaultValue("113")
INT_VECT_UART1_RX.setReadOnly(True)

INT_VECT_UART1_TX = coreComponent.createStringSymbol("INT_VECT_UART1_TX", rawConfigMenu)
INT_VECT_UART1_TX.setLabel("INT_VECT_UART1_TX")
INT_VECT_UART1_TX.setDefaultValue("114")
INT_VECT_UART1_TX.setReadOnly(True)

INT_VECT_I2C1_BUS = coreComponent.createStringSymbol("INT_VECT_I2C1_BUS", rawConfigMenu)
INT_VECT_I2C1_BUS.setLabel("INT_VECT_I2C1_BUS")
INT_VECT_I2C1_BUS.setDefaultValue("115")
INT_VECT_I2C1_BUS.setReadOnly(True)

INT_VECT_I2C1_SLAVE = coreComponent.createStringSymbol("INT_VECT_I2C1_SLAVE", rawConfigMenu)
INT_VECT_I2C1_SLAVE.setLabel("INT_VECT_I2C1_SLAVE")
INT_VECT_I2C1_SLAVE.setDefaultValue("116")
INT_VECT_I2C1_SLAVE.setReadOnly(True)

INT_VECT_I2C1_MASTER = coreComponent.createStringSymbol("INT_VECT_I2C1_MASTER", rawConfigMenu)
INT_VECT_I2C1_MASTER.setLabel("INT_VECT_I2C1_MASTER")
INT_VECT_I2C1_MASTER.setDefaultValue("117")
INT_VECT_I2C1_MASTER.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_A = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_A", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_A.setLabel("INT_VECT_CHANGE_NOTICE_A")
INT_VECT_CHANGE_NOTICE_A.setDefaultValue("118")
INT_VECT_CHANGE_NOTICE_A.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_B = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_B", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_B.setLabel("INT_VECT_CHANGE_NOTICE_B")
INT_VECT_CHANGE_NOTICE_B.setDefaultValue("119")
INT_VECT_CHANGE_NOTICE_B.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_C = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_C", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_C.setLabel("INT_VECT_CHANGE_NOTICE_C")
INT_VECT_CHANGE_NOTICE_C.setDefaultValue("120")
INT_VECT_CHANGE_NOTICE_C.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_D = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_D", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_D.setLabel("INT_VECT_CHANGE_NOTICE_D")
INT_VECT_CHANGE_NOTICE_D.setDefaultValue("121")
INT_VECT_CHANGE_NOTICE_D.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_E = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_E", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_E.setLabel("INT_VECT_CHANGE_NOTICE_E")
INT_VECT_CHANGE_NOTICE_E.setDefaultValue("122")
INT_VECT_CHANGE_NOTICE_E.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_F = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_F", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_F.setLabel("INT_VECT_CHANGE_NOTICE_F")
INT_VECT_CHANGE_NOTICE_F.setDefaultValue("123")
INT_VECT_CHANGE_NOTICE_F.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_G = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_G", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_G.setLabel("INT_VECT_CHANGE_NOTICE_G")
INT_VECT_CHANGE_NOTICE_G.setDefaultValue("124")
INT_VECT_CHANGE_NOTICE_G.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_H = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_H", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_H.setLabel("INT_VECT_CHANGE_NOTICE_H")
INT_VECT_CHANGE_NOTICE_H.setDefaultValue("125")
INT_VECT_CHANGE_NOTICE_H.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_J = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_J", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_J.setLabel("INT_VECT_CHANGE_NOTICE_J")
INT_VECT_CHANGE_NOTICE_J.setDefaultValue("126")
INT_VECT_CHANGE_NOTICE_J.setReadOnly(True)

INT_VECT_CHANGE_NOTICE_K = coreComponent.createStringSymbol("INT_VECT_CHANGE_NOTICE_K", rawConfigMenu)
INT_VECT_CHANGE_NOTICE_K.setLabel("INT_VECT_CHANGE_NOTICE_K")
INT_VECT_CHANGE_NOTICE_K.setDefaultValue("127")
INT_VECT_CHANGE_NOTICE_K.setReadOnly(True)

INT_VECT_PMP = coreComponent.createStringSymbol("INT_VECT_PMP", rawConfigMenu)
INT_VECT_PMP.setLabel("INT_VECT_PMP")
INT_VECT_PMP.setDefaultValue("128")
INT_VECT_PMP.setReadOnly(True)

INT_VECT_PMP_ERROR = coreComponent.createStringSymbol("INT_VECT_PMP_ERROR", rawConfigMenu)
INT_VECT_PMP_ERROR.setLabel("INT_VECT_PMP_ERROR")
INT_VECT_PMP_ERROR.setDefaultValue("129")
INT_VECT_PMP_ERROR.setReadOnly(True)

INT_VECT_COMPARATOR_1 = coreComponent.createStringSymbol("INT_VECT_COMPARATOR_1", rawConfigMenu)
INT_VECT_COMPARATOR_1.setLabel("INT_VECT_COMPARATOR_1")
INT_VECT_COMPARATOR_1.setDefaultValue("130")
INT_VECT_COMPARATOR_1.setReadOnly(True)

INT_VECT_COMPARATOR_2 = coreComponent.createStringSymbol("INT_VECT_COMPARATOR_2", rawConfigMenu)
INT_VECT_COMPARATOR_2.setLabel("INT_VECT_COMPARATOR_2")
INT_VECT_COMPARATOR_2.setDefaultValue("131")
INT_VECT_COMPARATOR_2.setReadOnly(True)

INT_VECT_USB = coreComponent.createStringSymbol("INT_VECT_USB", rawConfigMenu)
INT_VECT_USB.setLabel("INT_VECT_USB")
INT_VECT_USB.setDefaultValue("132")
INT_VECT_USB.setReadOnly(True)

INT_VECT_USB_DMA = coreComponent.createStringSymbol("INT_VECT_USB_DMA", rawConfigMenu)
INT_VECT_USB_DMA.setLabel("INT_VECT_USB_DMA")
INT_VECT_USB_DMA.setDefaultValue("133")
INT_VECT_USB_DMA.setReadOnly(True)

INT_VECT_DMA0 = coreComponent.createStringSymbol("INT_VECT_DMA0", rawConfigMenu)
INT_VECT_DMA0.setLabel("INT_VECT_DMA0")
INT_VECT_DMA0.setDefaultValue("134")
INT_VECT_DMA0.setReadOnly(True)

INT_VECT_DMA1 = coreComponent.createStringSymbol("INT_VECT_DMA1", rawConfigMenu)
INT_VECT_DMA1.setLabel("INT_VECT_DMA1")
INT_VECT_DMA1.setDefaultValue("135")
INT_VECT_DMA1.setReadOnly(True)

INT_VECT_DMA2 = coreComponent.createStringSymbol("INT_VECT_DMA2", rawConfigMenu)
INT_VECT_DMA2.setLabel("INT_VECT_DMA2")
INT_VECT_DMA2.setDefaultValue("136")
INT_VECT_DMA2.setReadOnly(True)

INT_VECT_DMA3 = coreComponent.createStringSymbol("INT_VECT_DMA3", rawConfigMenu)
INT_VECT_DMA3.setLabel("INT_VECT_DMA3")
INT_VECT_DMA3.setDefaultValue("137")
INT_VECT_DMA3.setReadOnly(True)

INT_VECT_DMA4 = coreComponent.createStringSymbol("INT_VECT_DMA4", rawConfigMenu)
INT_VECT_DMA4.setLabel("INT_VECT_DMA4")
INT_VECT_DMA4.setDefaultValue("138")
INT_VECT_DMA4.setReadOnly(True)

INT_VECT_DMA5 = coreComponent.createStringSymbol("INT_VECT_DMA5", rawConfigMenu)
INT_VECT_DMA5.setLabel("INT_VECT_DMA5")
INT_VECT_DMA5.setDefaultValue("139")
INT_VECT_DMA5.setReadOnly(True)

INT_VECT_DMA6 = coreComponent.createStringSymbol("INT_VECT_DMA6", rawConfigMenu)
INT_VECT_DMA6.setLabel("INT_VECT_DMA6")
INT_VECT_DMA6.setDefaultValue("140")
INT_VECT_DMA6.setReadOnly(True)

INT_VECT_DMA7 = coreComponent.createStringSymbol("INT_VECT_DMA7", rawConfigMenu)
INT_VECT_DMA7.setLabel("INT_VECT_DMA7")
INT_VECT_DMA7.setDefaultValue("141")
INT_VECT_DMA7.setReadOnly(True)

INT_VECT_SPI2_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI2_FAULT", rawConfigMenu)
INT_VECT_SPI2_FAULT.setLabel("INT_VECT_SPI2_FAULT")
INT_VECT_SPI2_FAULT.setDefaultValue("142")
INT_VECT_SPI2_FAULT.setReadOnly(True)

INT_VECT_SPI2_RX = coreComponent.createStringSymbol("INT_VECT_SPI2_RX", rawConfigMenu)
INT_VECT_SPI2_RX.setLabel("INT_VECT_SPI2_RX")
INT_VECT_SPI2_RX.setDefaultValue("143")
INT_VECT_SPI2_RX.setReadOnly(True)

INT_VECT_SPI2_TX = coreComponent.createStringSymbol("INT_VECT_SPI2_TX", rawConfigMenu)
INT_VECT_SPI2_TX.setLabel("INT_VECT_SPI2_TX")
INT_VECT_SPI2_TX.setDefaultValue("144")
INT_VECT_SPI2_TX.setReadOnly(True)

INT_VECT_UART2_FAULT = coreComponent.createStringSymbol("INT_VECT_UART2_FAULT", rawConfigMenu)
INT_VECT_UART2_FAULT.setLabel("INT_VECT_UART2_FAULT")
INT_VECT_UART2_FAULT.setDefaultValue("145")
INT_VECT_UART2_FAULT.setReadOnly(True)

INT_VECT_UART2_RX = coreComponent.createStringSymbol("INT_VECT_UART2_RX", rawConfigMenu)
INT_VECT_UART2_RX.setLabel("INT_VECT_UART2_RX")
INT_VECT_UART2_RX.setDefaultValue("146")
INT_VECT_UART2_RX.setReadOnly(True)

INT_VECT_UART2_TX = coreComponent.createStringSymbol("INT_VECT_UART2_TX", rawConfigMenu)
INT_VECT_UART2_TX.setLabel("INT_VECT_UART2_TX")
INT_VECT_UART2_TX.setDefaultValue("147")
INT_VECT_UART2_TX.setReadOnly(True)

INT_VECT_I2C2_BUS = coreComponent.createStringSymbol("INT_VECT_I2C2_BUS", rawConfigMenu)
INT_VECT_I2C2_BUS.setLabel("INT_VECT_I2C2_BUS")
INT_VECT_I2C2_BUS.setDefaultValue("148")
INT_VECT_I2C2_BUS.setReadOnly(True)

INT_VECT_I2C2_SLAVE = coreComponent.createStringSymbol("INT_VECT_I2C2_SLAVE", rawConfigMenu)
INT_VECT_I2C2_SLAVE.setLabel("INT_VECT_I2C2_SLAVE")
INT_VECT_I2C2_SLAVE.setDefaultValue("149")
INT_VECT_I2C2_SLAVE.setReadOnly(True)

INT_VECT_I2C2_MASTER = coreComponent.createStringSymbol("INT_VECT_I2C2_MASTER", rawConfigMenu)
INT_VECT_I2C2_MASTER.setLabel("INT_VECT_I2C2_MASTER")
INT_VECT_I2C2_MASTER.setDefaultValue("150")
INT_VECT_I2C2_MASTER.setReadOnly(True)

INT_VECT_CAN1 = coreComponent.createStringSymbol("INT_VECT_CAN1", rawConfigMenu)
INT_VECT_CAN1.setLabel("INT_VECT_CAN1")
INT_VECT_CAN1.setDefaultValue("151")
INT_VECT_CAN1.setReadOnly(True)

INT_VECT_CAN2 = coreComponent.createStringSymbol("INT_VECT_CAN2", rawConfigMenu)
INT_VECT_CAN2.setLabel("INT_VECT_CAN2")
INT_VECT_CAN2.setDefaultValue("152")
INT_VECT_CAN2.setReadOnly(True)

INT_VECT_ETHERNET = coreComponent.createStringSymbol("INT_VECT_ETHERNET", rawConfigMenu)
INT_VECT_ETHERNET.setLabel("INT_VECT_ETHERNET")
INT_VECT_ETHERNET.setDefaultValue("153")
INT_VECT_ETHERNET.setReadOnly(True)

INT_VECT_SPI3_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI3_FAULT", rawConfigMenu)
INT_VECT_SPI3_FAULT.setLabel("INT_VECT_SPI3_FAULT")
INT_VECT_SPI3_FAULT.setDefaultValue("154")
INT_VECT_SPI3_FAULT.setReadOnly(True)

INT_VECT_SPI3_RX = coreComponent.createStringSymbol("INT_VECT_SPI3_RX", rawConfigMenu)
INT_VECT_SPI3_RX.setLabel("INT_VECT_SPI3_RX")
INT_VECT_SPI3_RX.setDefaultValue("155")
INT_VECT_SPI3_RX.setReadOnly(True)

INT_VECT_SPI3_TX = coreComponent.createStringSymbol("INT_VECT_SPI3_TX", rawConfigMenu)
INT_VECT_SPI3_TX.setLabel("INT_VECT_SPI3_TX")
INT_VECT_SPI3_TX.setDefaultValue("156")
INT_VECT_SPI3_TX.setReadOnly(True)

INT_VECT_UART3_FAULT = coreComponent.createStringSymbol("INT_VECT_UART3_FAULT", rawConfigMenu)
INT_VECT_UART3_FAULT.setLabel("INT_VECT_UART3_FAULT")
INT_VECT_UART3_FAULT.setDefaultValue("157")
INT_VECT_UART3_FAULT.setReadOnly(True)

INT_VECT_UART3_RX = coreComponent.createStringSymbol("INT_VECT_UART3_RX", rawConfigMenu)
INT_VECT_UART3_RX.setLabel("INT_VECT_UART3_RX")
INT_VECT_UART3_RX.setDefaultValue("158")
INT_VECT_UART3_RX.setReadOnly(True)

INT_VECT_UART3_TX = coreComponent.createStringSymbol("INT_VECT_UART3_TX", rawConfigMenu)
INT_VECT_UART3_TX.setLabel("INT_VECT_UART3_TX")
INT_VECT_UART3_TX.setDefaultValue("159")
INT_VECT_UART3_TX.setReadOnly(True)

INT_VECT_I2C3_BUS = coreComponent.createStringSymbol("INT_VECT_I2C3_BUS", rawConfigMenu)
INT_VECT_I2C3_BUS.setLabel("INT_VECT_I2C3_BUS")
INT_VECT_I2C3_BUS.setDefaultValue("160")
INT_VECT_I2C3_BUS.setReadOnly(True)

INT_VECT_I2C3_SLAVE = coreComponent.createStringSymbol("INT_VECT_I2C3_SLAVE", rawConfigMenu)
INT_VECT_I2C3_SLAVE.setLabel("INT_VECT_I2C3_SLAVE")
INT_VECT_I2C3_SLAVE.setDefaultValue("161")
INT_VECT_I2C3_SLAVE.setReadOnly(True)

INT_VECT_I2C3_MASTER = coreComponent.createStringSymbol("INT_VECT_I2C3_MASTER", rawConfigMenu)
INT_VECT_I2C3_MASTER.setLabel("INT_VECT_I2C3_MASTER")
INT_VECT_I2C3_MASTER.setDefaultValue("162")
INT_VECT_I2C3_MASTER.setReadOnly(True)

INT_VECT_SPI4_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI4_FAULT", rawConfigMenu)
INT_VECT_SPI4_FAULT.setLabel("INT_VECT_SPI4_FAULT")
INT_VECT_SPI4_FAULT.setDefaultValue("163")
INT_VECT_SPI4_FAULT.setReadOnly(True)

INT_VECT_SPI4_RX = coreComponent.createStringSymbol("INT_VECT_SPI4_RX", rawConfigMenu)
INT_VECT_SPI4_RX.setLabel("INT_VECT_SPI4_RX")
INT_VECT_SPI4_RX.setDefaultValue("164")
INT_VECT_SPI4_RX.setReadOnly(True)

INT_VECT_SPI4_TX = coreComponent.createStringSymbol("INT_VECT_SPI4_TX", rawConfigMenu)
INT_VECT_SPI4_TX.setLabel("INT_VECT_SPI4_TX")
INT_VECT_SPI4_TX.setDefaultValue("165")
INT_VECT_SPI4_TX.setReadOnly(True)

INT_VECT_RTCC = coreComponent.createStringSymbol("INT_VECT_RTCC", rawConfigMenu)
INT_VECT_RTCC.setLabel("INT_VECT_RTCC")
INT_VECT_RTCC.setDefaultValue("166")
INT_VECT_RTCC.setReadOnly(True)

INT_VECT_FLASH_CONTROL = coreComponent.createStringSymbol("INT_VECT_FLASH_CONTROL", rawConfigMenu)
INT_VECT_FLASH_CONTROL.setLabel("INT_VECT_FLASH_CONTROL")
INT_VECT_FLASH_CONTROL.setDefaultValue("167")
INT_VECT_FLASH_CONTROL.setReadOnly(True)

INT_VECT_PREFETCH = coreComponent.createStringSymbol("INT_VECT_PREFETCH", rawConfigMenu)
INT_VECT_PREFETCH.setLabel("INT_VECT_PREFETCH")
INT_VECT_PREFETCH.setDefaultValue("168")
INT_VECT_PREFETCH.setReadOnly(True)

INT_VECT_SQI1 = coreComponent.createStringSymbol("INT_VECT_SQI1", rawConfigMenu)
INT_VECT_SQI1.setLabel("INT_VECT_SQI1")
INT_VECT_SQI1.setDefaultValue("169")
INT_VECT_SQI1.setReadOnly(True)

INT_VECT_UART4_FAULT = coreComponent.createStringSymbol("INT_VECT_UART4_FAULT", rawConfigMenu)
INT_VECT_UART4_FAULT.setLabel("INT_VECT_UART4_FAULT")
INT_VECT_UART4_FAULT.setDefaultValue("170")
INT_VECT_UART4_FAULT.setReadOnly(True)

INT_VECT_UART4_RX = coreComponent.createStringSymbol("INT_VECT_UART4_RX", rawConfigMenu)
INT_VECT_UART4_RX.setLabel("INT_VECT_UART4_RX")
INT_VECT_UART4_RX.setDefaultValue("171")
INT_VECT_UART4_RX.setReadOnly(True)

INT_VECT_UART4_TX = coreComponent.createStringSymbol("INT_VECT_UART4_TX", rawConfigMenu)
INT_VECT_UART4_TX.setLabel("INT_VECT_UART4_TX")
INT_VECT_UART4_TX.setDefaultValue("172")
INT_VECT_UART4_TX.setReadOnly(True)

INT_VECT_I2C4_BUS = coreComponent.createStringSymbol("INT_VECT_I2C4_BUS", rawConfigMenu)
INT_VECT_I2C4_BUS.setLabel("INT_VECT_I2C4_BUS")
INT_VECT_I2C4_BUS.setDefaultValue("173")
INT_VECT_I2C4_BUS.setReadOnly(True)

INT_VECT_I2C4_SLAVE = coreComponent.createStringSymbol("INT_VECT_I2C4_SLAVE", rawConfigMenu)
INT_VECT_I2C4_SLAVE.setLabel("INT_VECT_I2C4_SLAVE")
INT_VECT_I2C4_SLAVE.setDefaultValue("174")
INT_VECT_I2C4_SLAVE.setReadOnly(True)

INT_VECT_I2C4_MASTER = coreComponent.createStringSymbol("INT_VECT_I2C4_MASTER", rawConfigMenu)
INT_VECT_I2C4_MASTER.setLabel("INT_VECT_I2C4_MASTER")
INT_VECT_I2C4_MASTER.setDefaultValue("175")
INT_VECT_I2C4_MASTER.setReadOnly(True)

INT_VECT_SPI5_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI5_FAULT", rawConfigMenu)
INT_VECT_SPI5_FAULT.setLabel("INT_VECT_SPI5_FAULT")
INT_VECT_SPI5_FAULT.setDefaultValue("176")
INT_VECT_SPI5_FAULT.setReadOnly(True)

INT_VECT_SPI5_RX = coreComponent.createStringSymbol("INT_VECT_SPI5_RX", rawConfigMenu)
INT_VECT_SPI5_RX.setLabel("INT_VECT_SPI5_RX")
INT_VECT_SPI5_RX.setDefaultValue("177")
INT_VECT_SPI5_RX.setReadOnly(True)

INT_VECT_SPI5_TX = coreComponent.createStringSymbol("INT_VECT_SPI5_TX", rawConfigMenu)
INT_VECT_SPI5_TX.setLabel("INT_VECT_SPI5_TX")
INT_VECT_SPI5_TX.setDefaultValue("178")
INT_VECT_SPI5_TX.setReadOnly(True)

INT_VECT_UART5_FAULT = coreComponent.createStringSymbol("INT_VECT_UART5_FAULT", rawConfigMenu)
INT_VECT_UART5_FAULT.setLabel("INT_VECT_UART5_FAULT")
INT_VECT_UART5_FAULT.setDefaultValue("179")
INT_VECT_UART5_FAULT.setReadOnly(True)

INT_VECT_UART5_RX = coreComponent.createStringSymbol("INT_VECT_UART5_RX", rawConfigMenu)
INT_VECT_UART5_RX.setLabel("INT_VECT_UART5_RX")
INT_VECT_UART5_RX.setDefaultValue("180")
INT_VECT_UART5_RX.setReadOnly(True)

INT_VECT_UART5_TX = coreComponent.createStringSymbol("INT_VECT_UART5_TX", rawConfigMenu)
INT_VECT_UART5_TX.setLabel("INT_VECT_UART5_TX")
INT_VECT_UART5_TX.setDefaultValue("181")
INT_VECT_UART5_TX.setReadOnly(True)

INT_VECT_I2C5_BUS = coreComponent.createStringSymbol("INT_VECT_I2C5_BUS", rawConfigMenu)
INT_VECT_I2C5_BUS.setLabel("INT_VECT_I2C5_BUS")
INT_VECT_I2C5_BUS.setDefaultValue("182")
INT_VECT_I2C5_BUS.setReadOnly(True)

INT_VECT_I2C5_SLAVE = coreComponent.createStringSymbol("INT_VECT_I2C5_SLAVE", rawConfigMenu)
INT_VECT_I2C5_SLAVE.setLabel("INT_VECT_I2C5_SLAVE")
INT_VECT_I2C5_SLAVE.setDefaultValue("183")
INT_VECT_I2C5_SLAVE.setReadOnly(True)

INT_VECT_I2C5_MASTER = coreComponent.createStringSymbol("INT_VECT_I2C5_MASTER", rawConfigMenu)
INT_VECT_I2C5_MASTER.setLabel("INT_VECT_I2C5_MASTER")
INT_VECT_I2C5_MASTER.setDefaultValue("184")
INT_VECT_I2C5_MASTER.setReadOnly(True)

INT_VECT_SPI6_FAULT = coreComponent.createStringSymbol("INT_VECT_SPI6_FAULT", rawConfigMenu)
INT_VECT_SPI6_FAULT.setLabel("INT_VECT_SPI6_FAULT")
INT_VECT_SPI6_FAULT.setDefaultValue("185")
INT_VECT_SPI6_FAULT.setReadOnly(True)

INT_VECT_SPI6_RX = coreComponent.createStringSymbol("INT_VECT_SPI6_RX", rawConfigMenu)
INT_VECT_SPI6_RX.setLabel("INT_VECT_SPI6_RX")
INT_VECT_SPI6_RX.setDefaultValue("186")
INT_VECT_SPI6_RX.setReadOnly(True)

INT_VECT_SPI6_TX = coreComponent.createStringSymbol("INT_VECT_SPI6_TX", rawConfigMenu)
INT_VECT_SPI6_TX.setLabel("INT_VECT_SPI6_TX")
INT_VECT_SPI6_TX.setDefaultValue("187")
INT_VECT_SPI6_TX.setReadOnly(True)

INT_VECT_UART6_FAULT = coreComponent.createStringSymbol("INT_VECT_UART6_FAULT", rawConfigMenu)
INT_VECT_UART6_FAULT.setLabel("INT_VECT_UART6_FAULT")
INT_VECT_UART6_FAULT.setDefaultValue("188")
INT_VECT_UART6_FAULT.setReadOnly(True)

INT_VECT_UART6_RX = coreComponent.createStringSymbol("INT_VECT_UART6_RX", rawConfigMenu)
INT_VECT_UART6_RX.setLabel("INT_VECT_UART6_RX")
INT_VECT_UART6_RX.setDefaultValue("189")
INT_VECT_UART6_RX.setReadOnly(True)

INT_VECT_UART6_TX = coreComponent.createStringSymbol("INT_VECT_UART6_TX", rawConfigMenu)
INT_VECT_UART6_TX.setLabel("INT_VECT_UART6_TX")
INT_VECT_UART6_TX.setDefaultValue("190")
INT_VECT_UART6_TX.setReadOnly(True)

INT_VECT_ADC_EOS = coreComponent.createStringSymbol("INT_VECT_ADC_EOS", rawConfigMenu)
INT_VECT_ADC_EOS.setLabel("INT_VECT_ADC_EOS")
INT_VECT_ADC_EOS.setDefaultValue("192")
INT_VECT_ADC_EOS.setReadOnly(True)

INT_VECT_ADC_ARDY = coreComponent.createStringSymbol("INT_VECT_ADC_ARDY", rawConfigMenu)
INT_VECT_ADC_ARDY.setLabel("INT_VECT_ADC_ARDY")
INT_VECT_ADC_ARDY.setDefaultValue("193")
INT_VECT_ADC_ARDY.setReadOnly(True)

INT_VECT_ADC_URDY = coreComponent.createStringSymbol("INT_VECT_ADC_URDY", rawConfigMenu)
INT_VECT_ADC_URDY.setLabel("INT_VECT_ADC_URDY")
INT_VECT_ADC_URDY.setDefaultValue("194")
INT_VECT_ADC_URDY.setReadOnly(True)

INT_VECT_ADC_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC_EARLY", rawConfigMenu)
INT_VECT_ADC_EARLY.setLabel("INT_VECT_ADC_EARLY")
INT_VECT_ADC_EARLY.setDefaultValue("196")
INT_VECT_ADC_EARLY.setReadOnly(True)

INT_VECT_ADC0_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC0_EARLY", rawConfigMenu)
INT_VECT_ADC0_EARLY.setLabel("INT_VECT_ADC0_EARLY")
INT_VECT_ADC0_EARLY.setDefaultValue("198")
INT_VECT_ADC0_EARLY.setReadOnly(True)

INT_VECT_ADC1_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC1_EARLY", rawConfigMenu)
INT_VECT_ADC1_EARLY.setLabel("INT_VECT_ADC1_EARLY")
INT_VECT_ADC1_EARLY.setDefaultValue("199")
INT_VECT_ADC1_EARLY.setReadOnly(True)

INT_VECT_ADC2_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC2_EARLY", rawConfigMenu)
INT_VECT_ADC2_EARLY.setLabel("INT_VECT_ADC2_EARLY")
INT_VECT_ADC2_EARLY.setDefaultValue("200")
INT_VECT_ADC2_EARLY.setReadOnly(True)

INT_VECT_ADC3_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC3_EARLY", rawConfigMenu)
INT_VECT_ADC3_EARLY.setLabel("INT_VECT_ADC3_EARLY")
INT_VECT_ADC3_EARLY.setDefaultValue("201")
INT_VECT_ADC3_EARLY.setReadOnly(True)

INT_VECT_ADC4_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC4_EARLY", rawConfigMenu)
INT_VECT_ADC4_EARLY.setLabel("INT_VECT_ADC4_EARLY")
INT_VECT_ADC4_EARLY.setDefaultValue("202")
INT_VECT_ADC4_EARLY.setReadOnly(True)

INT_VECT_ADC7_EARLY = coreComponent.createStringSymbol("INT_VECT_ADC7_EARLY", rawConfigMenu)
INT_VECT_ADC7_EARLY.setLabel("INT_VECT_ADC7_EARLY")
INT_VECT_ADC7_EARLY.setDefaultValue("205")
INT_VECT_ADC7_EARLY.setReadOnly(True)

INT_VECT_ADC0_WARM = coreComponent.createStringSymbol("INT_VECT_ADC0_WARM", rawConfigMenu)
INT_VECT_ADC0_WARM.setLabel("INT_VECT_ADC0_WARM")
INT_VECT_ADC0_WARM.setDefaultValue("206")
INT_VECT_ADC0_WARM.setReadOnly(True)

INT_VECT_ADC1_WARM = coreComponent.createStringSymbol("INT_VECT_ADC1_WARM", rawConfigMenu)
INT_VECT_ADC1_WARM.setLabel("INT_VECT_ADC1_WARM")
INT_VECT_ADC1_WARM.setDefaultValue("207")
INT_VECT_ADC1_WARM.setReadOnly(True)

INT_VECT_ADC2_WARM = coreComponent.createStringSymbol("INT_VECT_ADC2_WARM", rawConfigMenu)
INT_VECT_ADC2_WARM.setLabel("INT_VECT_ADC2_WARM")
INT_VECT_ADC2_WARM.setDefaultValue("208")
INT_VECT_ADC2_WARM.setReadOnly(True)

INT_VECT_ADC3_WARM = coreComponent.createStringSymbol("INT_VECT_ADC3_WARM", rawConfigMenu)
INT_VECT_ADC3_WARM.setLabel("INT_VECT_ADC3_WARM")
INT_VECT_ADC3_WARM.setDefaultValue("209")
INT_VECT_ADC3_WARM.setReadOnly(True)

INT_VECT_ADC4_WARM = coreComponent.createStringSymbol("INT_VECT_ADC4_WARM", rawConfigMenu)
INT_VECT_ADC4_WARM.setLabel("INT_VECT_ADC4_WARM")
INT_VECT_ADC4_WARM.setDefaultValue("210")
INT_VECT_ADC4_WARM.setReadOnly(True)

INT_VECT_ADC7_WARM = coreComponent.createStringSymbol("INT_VECT_ADC7_WARM", rawConfigMenu)
INT_VECT_ADC7_WARM.setLabel("INT_VECT_ADC7_WARM")
INT_VECT_ADC7_WARM.setDefaultValue("213")
INT_VECT_ADC7_WARM.setReadOnly(True)

PFM_ADDR_START = coreComponent.createStringSymbol("PFM_ADDR_START", rawConfigMenu)
PFM_ADDR_START.setLabel("PFM_ADDR_START")
PFM_ADDR_START.setDefaultValue("0x1d000000")
PFM_ADDR_START.setReadOnly(True)

PFM_ADDR_END = coreComponent.createStringSymbol("PFM_ADDR_END", rawConfigMenu)
PFM_ADDR_END.setLabel("PFM_ADDR_END")
PFM_ADDR_END.setDefaultValue("0x1d200000")
PFM_ADDR_END.setReadOnly(True)

PFM_ADDR_SIZE = coreComponent.createStringSymbol("PFM_ADDR_SIZE", rawConfigMenu)
PFM_ADDR_SIZE.setLabel("PFM_ADDR_SIZE")
PFM_ADDR_SIZE.setDefaultValue("0x200000")
PFM_ADDR_SIZE.setReadOnly(True)

SRAM_ADDR_START = coreComponent.createStringSymbol("SRAM_ADDR_START", rawConfigMenu)
SRAM_ADDR_START.setLabel("SRAM_ADDR_START")
SRAM_ADDR_START.setDefaultValue("0x0")
SRAM_ADDR_START.setReadOnly(True)

SRAM_ADDR_END = coreComponent.createStringSymbol("SRAM_ADDR_END", rawConfigMenu)
SRAM_ADDR_END.setLabel("SRAM_ADDR_END")
SRAM_ADDR_END.setDefaultValue("0x80000")
SRAM_ADDR_END.setReadOnly(True)

SRAM_ADDR_SIZE = coreComponent.createStringSymbol("SRAM_ADDR_SIZE", rawConfigMenu)
SRAM_ADDR_SIZE.setLabel("SRAM_ADDR_SIZE")
SRAM_ADDR_SIZE.setDefaultValue("0x80000")
SRAM_ADDR_SIZE.setReadOnly(True)

BOOT_ADDR_START = coreComponent.createStringSymbol("BOOT_ADDR_START", rawConfigMenu)
BOOT_ADDR_START.setLabel("BOOT_ADDR_START")
BOOT_ADDR_START.setDefaultValue("0x1fc00000")
BOOT_ADDR_START.setReadOnly(True)

BOOT_ADDR_END = coreComponent.createStringSymbol("BOOT_ADDR_END", rawConfigMenu)
BOOT_ADDR_END.setLabel("BOOT_ADDR_END")
BOOT_ADDR_END.setDefaultValue("0x1fc0ff00")
BOOT_ADDR_END.setReadOnly(True)

BOOT_ADDR_SIZE = coreComponent.createStringSymbol("BOOT_ADDR_SIZE", rawConfigMenu)
BOOT_ADDR_SIZE.setLabel("BOOT_ADDR_SIZE")
BOOT_ADDR_SIZE.setDefaultValue("0xff00")
BOOT_ADDR_SIZE.setReadOnly(True)

configName = Variables.get("__CONFIGURATION_NAME")

testFile = coreComponent.createFileSymbol(None, None)
testFile.setSourcePath("src/testfile.c.ftl")
testFile.setDestPath("system_config/" + configName + "/testfile.c")
testFile.setProjectPath("system_config/" + configName)
testFile.setType("SOURCE")

testHeaderFile = coreComponent.createFileSymbol(None, None)
testHeaderFile.setSourcePath("src/testfile.h.ftl")
testHeaderFile.setDestPath("system_config/" + configName + "/testfile.h")
testHeaderFile.setType("HEADER")

testResourceFile = coreComponent.createFileSymbol(None, None)
testResourceFile.setSourcePath("src/testresfile.c")
testResourceFile.setDestPath("system_config/" + configName + "/testresfile.c")
testResourceFile.setType("SOURCE")
testResourceFile.setMarkup(False)

testAppFile = coreComponent.createFileSymbol(None, None)
testAppFile.setSourcePath("src/testapp.c.ftl")
testAppFile.setDestPath("system_config/" + configName + "/testapp.c")
testAppFile.setType("SOURCE")
testAppFile.setTracked(False)
testAppFile.setOverwrite(False)


testLibrary = coreComponent.createLibrarySymbol(None, None)
testLibrary.setPath("src/test.a")