# coding: utf-8
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

# Translation of selected ATDF clock names to calculated clock frequency symbol names
global CLK_XLAT
CLK_XLAT = {
        "SLOW_CLK" : "CLK_MD_SLCK_FREQ",
        "MAIN_CLK" : "CLK_MAINCK_FREQ",
        "PLLA_CLK" : "CLK_PLLACK_FREQ",
        "PLLB_CLK" : "CLK_PLLBCK_FREQ",
        "MCK_CLK"  : "CLK_MCK_FREQ",
        "MCK_RC2"  : "CLK_RC2CK_FREQ",
        "MCK"      : "CLK_MCK_FREQ",
        "MAINCK"   : "CLK_MAINCK_FREQ",
        "RC2CK"    : "CLK_RC2CK_FREQ",
        "RC2_CLK"  : "CLK_RC2CK_FREQ",
        "MD_SLCK"  : "CLK_MD_SLCK_FREQ",
        "TD_SLCK"  : "CLK_TD_SLCK_FREQ",
        "PLLACK"   : "CLK_PLLACK_FREQ",
        "PLLBCK"   : "CLK_PLLBCK_FREQ",
    }

# Default settings
global SLCK_RC_FREQ
SLCK_RC_FREQ = 32000
global SLCK_XTAL_FREQ
SLCK_XTAL_FREQ = 32768
global RC_FREQ_DEFAULT
RC_FREQ_DEFAULT = 2
global SYSTICK_EXT_DIV
SYSTICK_EXT_DIV = 2

global upd_slck_td_freq
def upd_slck_td_freq(symbol, event):
    if event['source'].getSymbolValue("CLK_SLCK_TDXTALSEL") == 0:
        freq = SLCK_RC_FREQ
    else:
        if event['source'].getSymbolValue("CLK_SLCK_OSCBYPASS") is False:
            freq = SLCK_XTAL_FREQ
        else:
            freq = event['source'].getSymbolValue("CLK_SLCK_EXT_FREQ")
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_mainck_freq
def upd_mainck_freq(symbol, event):
    if event['source'].getSymbolValue("CLK_MAINCK_MOSCSEL") == 0:
        mainck_rc_freq = event['source'].getSymbolByID("CLK_MAINCK_MOSCRCF")
        freq = int(mainck_rc_freq.getKey(mainck_rc_freq.getValue()).split("_")[1]) * 1000000
    else:
        freq = event['source'].getSymbolValue("CLK_MAINCK_EXT_FREQ")
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_rc2ck_freq
def upd_rc2ck_freq(symbol, event):
    en = event['source'].getSymbolValue("CLK_RC2CK_EN")
    if en==False:
        freq = 0
    else:
        rc2ck_sel_freq = event['source'].getSymbolByID("CLK_RC2CK_OSCRCF")
        freq = int(rc2ck_sel_freq.getKey(rc2ck_sel_freq.getValue()).split("_")[1]) * 1000000
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_pllack_freq
def upd_pllack_freq(symbol, event):
    diva = event['source'].getSymbolValue("CLK_PLLACK_DIVA")
    mula = event['source'].getSymbolValue("CLK_PLLACK_MULA")
    if diva==0 or mula==0:
        freq = 0
    else:
        freq = (event['source'].getSymbolValue("CLK_MAINCK_FREQ") * (mula + 1)) // diva
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_pllbck_freq
def upd_pllbck_freq(symbol, event):
    divb = event['source'].getSymbolValue("CLK_PLLBCK_DIVB")
    mulb = event['source'].getSymbolValue("CLK_PLLBCK_MULB")
    if divb==0 or mulb==0:
        freq = 0
    else:
        pllbck_srcb = event['source'].getSymbolByID("CLK_PLLBCK_SRCB")
        freq = (event['source'].getSymbolValue(CLK_XLAT[pllbck_srcb.getKey(pllbck_srcb.getValue())]) * (mulb + 1)) // divb
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_fclk_freq
def upd_fclk_freq(symbol, event):
    pres = event['source'].getSymbolValue("CLK_MCK_PRES")
    fclk_css = event['source'].getSymbolByID("CLK_MCK_CSS")
    freq = event['source'].getSymbolValue(CLK_XLAT[fclk_css.getKey(fclk_css.getValue())]) >> (pres)
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_systick_freq
def upd_systick_freq(symbol, event):
    freq = event['value'] / SYSTICK_EXT_DIV
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_mck_freq
def upd_mck_freq(symbol, event):
    freq = event['source'].getSymbolValue("CPU_CLOCK_FREQUENCY")
    mdiv = event['source'].getSymbolValue("CLK_MCK_MDIV")
    freq = freq >> mdiv
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_pck_freq
def upd_pck_freq(symbol, event):
    idx = int(symbol.getID().split("PCK")[1].split("_")[0])
    en = event['source'].getSymbolValue("CLK_PCK"+str(idx)+"_EN")
    if en==False:
        freq = 0
    else:
        pres = event['source'].getSymbolValue("CLK_PCK"+str(idx)+"_PRES")
        pckx_css = event['source'].getSymbolByID("CLK_PCK"+str(idx)+"_CSS")
        freq = event['source'].getSymbolValue(CLK_XLAT[pckx_css.getKey(pckx_css.getValue())]) // (pres + 1)
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_gclk_freq
def upd_gclk_freq(symbol, event):
    periph = symbol.getID().split("_GCLK_")[0]
    en = event['source'].getSymbolValue(periph+"_GCLK_ENABLE")
    if en==False:
        freq = 0
    else:
        div = event['source'].getSymbolValue(periph+"_GCLK_DIV")
        gclk_css = event['source'].getSymbolByID(periph+"_GCLK_CSS")
        freq = event['source'].getSymbolValue(CLK_XLAT[gclk_css.getKey(gclk_css.getValue())]) // (div + 1)
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_flexcom_freq
def upd_flexcom_freq(symbol,event):
    frequency = 0
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    previousFreq = int(Database.getSymbolValue("core", instance_name + "_CLOCK_FREQUENCY"))
    op_mode = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_MODE")
    if Database.getSymbolValue("core", instance_name + "_CLOCK_ENABLE"):
        # Flexcom is operating as UART
        if op_mode == 1 :
            #Get the UART mode source clock
            source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_USART_MR_USCLKS")
            # Source clock is bus clock
            if source_clock == 0:
                frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ")
            # Source clock is bus clock / 8
            elif source_clock == 1:
                frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ") / 8
            # Source clock is GCLK
            elif source_clock == 2:
                frequency = Database.getSymbolValue("core", instance_name + "_GCLK_FREQUENCY")
            # Source clock is external, set the internal frequency to zero
            else:
                frequency = 0
        #Flexcom is operating in SPI mode
        elif op_mode == 2:
            #Get the SPI mode source clock
            source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_SPI_MR_BRSRCCLK")
            # Source clock is bus clock
            if source_clock == 0:
                frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ")
            # Source clock is GCLK
            elif source_clock == 1:
                frequency = Database.getSymbolValue("core", instance_name + "_GCLK_FREQUENCY")
        #Flexcom is operating in TWI mode
        elif op_mode == 3:
            #Get the SPI mode source clock
            source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_TWI_CWGR_BRSRCCLK")
            # Source clock is bus clock
            if source_clock == 0:
                frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ")
            # Source clock is GCLK
            elif source_clock == 1:
                frequency = Database.getSymbolValue("core", instance_name + "_GCLK_FREQUENCY")

    # Update the frequency only if the clock selections are valid
    if frequency != previousFreq:
        symbol.setValue(frequency)

global upd_mcan_freq
def upd_mcan_freq(symbol, event):
    frequency = 0
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    if Database.getSymbolValue("core", instance_name + "_GCLK_ENABLE"):
        frequency = Database.getSymbolValue("core", instance_name + "_GCLK_FREQUENCY")
    symbol.setValue(frequency)

global upd_tc_freq
def upd_tc_freq(symbol, event):
    # symbol is named as "TC{instance_number}_CH{channel_number}_CLOCK_FREQUENCY.
    # Extract the instance number
    instance_num = int(symbol.getID().split("TC")[1].split("_")[0])
    # extract the channel number
    channel_num = int(symbol.getID().split("_CH")[1].split("_")[0])

    # check if the relevant channel is enabled
    if (Database.getSymbolValue("tc" + str(instance_num), "TC" + str(channel_num) + "_ENABLE") == True):

        # Find the current clock source for the channel
        clk_src = Database.getSymbolValue("tc" + str(instance_num), "TC" + str(channel_num) + "_CMR_TCCLKS")
        # if clock source is processor independent GCLK
        if (clk_src == 1):
            clk_frequency = Database.getSymbolValue("core", "TC" + str(instance_num) + "_CHANNEL0_GCLK_FREQUENCY")
        # if clock  source is MCK/8
        elif (clk_src == 2):
            clk_frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ") / 8
        # if clock  source is MCK/32
        elif (clk_src == 3):
            clk_frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ") / 32
        # if clock  source is MCK/128
        elif (clk_src == 4):
            clk_frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ") / 128
        # if clock  source is SLOW CLOCK
        elif (clk_src == 5):
            clk_frequency = Database.getSymbolValue("core", "CLK_MD_SLCK_FREQ")
        # default  clock source is MCK (Enabled through extended registers of TC)
        else:
            clk_frequency = Database.getSymbolValue("core", "CLK_MCK_FREQ")
        symbol.setValue(clk_frequency)

    else:
        symbol.setValue(0)

# Create Generic Clock Entries
global create_gclk_entries
def create_gclk_entries (clock_id_name, clock_comp, clk_menu):
    gclk_en = clock_comp.createBooleanSymbol(clock_id_name+"_GCLK_ENABLE", clk_menu)
    gclk_en.setLabel("Generic Clock Enable")
    gclk_en.setDescription("Enables the generic clock for" + clock_id_name)
    gclk_en.setDefaultValue(False)

    gclk_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PCR__GCLKCSS"]')
    gclk_css = clock_comp.createKeyValueSetSymbol(clock_id_name+"_GCLK_CSS", clk_menu)
    gclk_css.setLabel("Clock Source")
    gclk_css.setDescription("Selects the input clock source for Generic clock")
    gclk_css.setDisplayMode("Key")
    gclk_css.setOutputMode("Key")
    for value in gclk_css_vg_node.getChildren():
        gclk_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    gclk_css.setDefaultValue(0)

    gclk_div = clock_comp.createIntegerSymbol(clock_id_name+"_GCLK_DIV", clk_menu)
    gclk_div.setLabel("GCLK Divider")
    gclk_div.setDescription("Generic clock is the selected clock period divided by GCLKDIV + 1.")
    gclk_div.setDefaultValue(0)
    gclk_div.setMin(0)
    gclk_div.setMax(15)

    gclk_freq = clock_comp.createIntegerSymbol(clock_id_name+"_GCLK_FREQUENCY", clk_menu)
    gclk_freq.setLabel("GCLK Frequency (HZ)")
    gclk_freq.setReadOnly(True)
    gclk_freq.setVisible(True)
    gclk_freq.setDefaultValue(0)    # Default SLCK_RC_FREQ
    gclk_freq.setDependencies(upd_gclk_freq,
        [   clock_id_name+"_GCLK_ENABLE",
            clock_id_name+"_GCLK_CSS",
            clock_id_name+"_GCLK_DIV",
            "CLK_MAINCK_FREQ",
            "CLK_MD_SLCK_FREQ",
            "CLK_PLLACK_FREQ",
            "CLK_PLLBCK_FREQ",
            "CLK_MCK_FREQ",
            "CLK_RC2CK_FREQ" ])

global periFreq
def periFreq(symbol, event):
    enable = Database.getSymbolValue("core", symbol.getID().split(
        "_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")
    if enable:
        freq = int(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
        if symbol.getValue() != freq:
            symbol.setValue(freq)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0)

global periGclkFreq
def periGclkFreq(symbol, event):
    enable = Database.getSymbolValue("core", symbol.getID().split(
        "_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")
    if enable:
        Database.setSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] +"_GCLK_ENABLE", True)
        freq = int(Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] +"_GCLK_FREQUENCY"))
        if symbol.getValue() != freq:
            symbol.setValue(freq)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0)

global create_default_freq_sym
def create_default_freq_sym (clock_id_name, clock_comp, clk_menu):
    # Create peripheral clock frequency symbol [clock_id_name]_CLOCK_FREQUENCY
    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setReadOnly(True)
    freq_sym.setVisible(True)
    freq_sym.setDefaultValue(0)
    freq_sym.setDependencies(periFreq, ["CLK_MCK_FREQ", clock_id_name + "_CLOCK_ENABLE"])

global create_default_freq_sym_gclk
def create_default_freq_sym_gclk (clock_id_name, clock_comp, clk_menu):
    # Create peripheral clock frequency symbol [clock_id_name]_CLOCK_FREQUENCY
    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setReadOnly(True)
    freq_sym.setVisible(True)
    freq_sym.setDefaultValue(0)
    freq_sym.setDependencies(periGclkFreq, ["CLK_MCK_FREQ", clock_id_name + "_CLOCK_ENABLE", clock_id_name + "_GCLK_FREQUENCY"])

global create_flexcom_freq_sym
def create_flexcom_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)

    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setVisible(True)
    freq_sym.setReadOnly(True)
    freq_sym.setDefaultValue(0)
    freq_sym.setDependencies(upd_flexcom_freq,
        [   "CLK_MCK_FREQ",
            clock_id_name + "_CLOCK_ENABLE",
            clock_id_name + "_GCLK_FREQUENCY",
            clock_id_name.lower() + ".FLEXCOM_MODE",
            clock_id_name.lower() + ".FLEXCOM_USART_MR_USCLKS",
            clock_id_name.lower() + ".FLEXCOM_SPI_MR_BRSRCCLK",
            clock_id_name.lower() + ".FLEXCOM_TWI_CWGR_BRSRCCLK"])

def create_hemc_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym_gclk(clock_id_name, clock_comp, clk_menu)

def create_hefc_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym_gclk(clock_id_name, clock_comp, clk_menu)

def create_ip1553_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

global create_mcan_freq_sym
def create_mcan_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)

    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setVisible(True)
    freq_sym.setReadOnly(True)
    freq_sym.setDefaultValue(Database.getSymbolValue("core", clock_id_name + "_GCLK_FREQUENCY"))
    freq_sym.setDependencies(upd_mcan_freq, [clock_id_name + "_GCLK_ENABLE", clock_id_name + "_GCLK_FREQUENCY"])

def create_spw_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

def create_nmic_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym_gclk(clock_id_name, clock_comp, clk_menu)


def create_tc_freq_sym(clock_id_name, clock_comp, clk_menu):
    id_list = clock_id_name.split("_CHANNEL")
    inst = id_list[0]
    chan = int(id_list[1])
    if chan==0:
        create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    freq_sym = clock_comp.createIntegerSymbol(inst + "_CH" + str(chan) + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setReadOnly(True)
    freq_sym.setVisible(True)
    freq_sym.setDefaultValue(0)
    freq_sym.setDependencies(upd_tc_freq,
        [   "CLK_MCK_FREQ",
            "CLK_MD_SLCK_FREQ",
            clock_id_name+"_GCLK_FREQUENCY",
            inst.lower() + ".TC" + str(chan) + "_CMR_TCCLKS",
            inst.lower() + ".TC" + str(chan) + "_ENABLE" ])
    if chan==2:
        # Create additional dummy channel 3 for quadrature
        freq_dmy = clock_comp.createIntegerSymbol(inst + "_CH3_CLOCK_FREQUENCY", clk_menu)
        freq_dmy.setReadOnly(True)
        freq_dmy.setVisible(True)
        freq_dmy.setDefaultValue(0)
        freq_dmy.setDependencies(upd_tc_freq,
            [   "CLK_MCK_FREQ",
                "CLK_MD_SLCK_FREQ",
                clock_id_name+"_GCLK_FREQUENCY",
                inst.lower() + ".TC" + str(chan) + "_CMR_TCCLKS",
                inst.lower() + ".TC" + str(chan) + "_ENABLE" ])

global freq_sym_const_dict
freq_sym_const_dict = { "FLEXCOM": create_flexcom_freq_sym,
                        "HEMC": create_hemc_freq_sym,
                        "HEFC": create_hefc_freq_sym,
                        "IP1553": create_ip1553_freq_sym,
                        "MCAN": create_mcan_freq_sym,
                        "SPW": create_spw_freq_sym,
                        "TC": create_tc_freq_sym,
                        "NMIC": create_nmic_freq_sym }

# SLOW CLOCK MENU
def __slow_clock_menu(clk_comp, clk_menu):
    slck_menu = clk_comp.createMenuSymbol("CLK_SLCK_MENU", clk_menu)
    slck_menu.setLabel("Slow Clock (SLCK)")
    slck_menu.setDescription("Slow Clock Configuration")

    # Timing Domain Slow Clock Crystal Oscillator Select (default is RC)
    slck_td_xtal_sel = clk_comp.createKeyValueSetSymbol("CLK_SLCK_TDXTALSEL", slck_menu)
    slck_td_xtal_sel.setLabel("Timing Domain Clock Source")
    slck_td_xtal_sel.setDescription("This option is used to selct the source for the slow clock of the timing domain (TD_SLCK)")
    slck_td_xtal_sel.setOutputMode("Value")
    slck_td_xtal_sel.setDisplayMode("Description")
    slck_td_xtal_sel.addKey("Internal RC", str(0), "Internal RC Oscilator")
    slck_td_xtal_sel.addKey("External Osc", str(1), "External 32.768 KHz Oscillator")

    # Slow Clock Oscillator Bypass (default is RC)
    slck_bp_sel = clk_comp.createBooleanSymbol("CLK_SLCK_OSCBYPASS", slck_menu)
    slck_bp_sel.setLabel("Bypass Crystal Oscillator")
    slck_bp_sel.setDescription("The 32.768 kHz crystal oscillator is bypassed and external clock is used.")
    slck_bp_sel.setDefaultValue(False)

    # Slow Clock External Bypass Frequency
    slck_bp_freq = clk_comp.createIntegerSymbol("CLK_SLCK_EXT_FREQ", slck_menu)
    slck_bp_freq.setLabel("External Clock Freq (Hz)")
    slck_bp_freq.setDescription("External bypass clock frequency on pin XIN32")
    slck_bp_freq.setDefaultValue(SLCK_XTAL_FREQ)
    slck_bp_freq.setMin(0)
    slck_bp_freq.setMax(32768)

    # TD_SLCK Frequency Display
    slck_td_freq = clk_comp.createIntegerSymbol("CLK_TD_SLCK_FREQ", slck_menu)
    slck_td_freq.setLabel("TD_SLCK Frequency (HZ)")
    slck_td_freq.setDefaultValue(SLCK_RC_FREQ)
    slck_td_freq.setReadOnly(True)
    slck_td_freq.setVisible(True)
    slck_td_freq.setDependencies(upd_slck_td_freq, ["CLK_SLCK_OSCBYPASS", "CLK_SLCK_TDXTALSEL", "CLK_SLCK_EXT_FREQ"])

    # MD_SLCK Frequency Display
    slck_md_freq = clk_comp.createIntegerSymbol("CLK_MD_SLCK_FREQ", slck_menu)
    slck_md_freq.setLabel("MD_SLCK Frequency (HZ)")
    slck_md_freq.setDefaultValue(SLCK_RC_FREQ)
    slck_md_freq.setReadOnly(True)
    slck_md_freq.setVisible(True)

# MAIN CLOCK MENU
def __main_clock_menu(clk_comp, clk_menu):
    mainck_menu = clk_comp.createMenuSymbol("CLK_MAINCK_MENU", clk_menu)
    mainck_menu.setLabel("Main Clock (MAINCK)")
    mainck_menu.setDescription("Main Clock Configuration")

    # Main Clock RC Enable
    mainck_rc_en = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCRCEN", mainck_menu)
    mainck_rc_en.setLabel("Enable RC Oscillator")
    mainck_rc_en.setDescription("The Main RC oscillator is enabled.")
    mainck_rc_en.setDefaultValue(True)

    # Main Clock RC Frequency Selection
    mainck_rc_freq_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="CKGR_MOR__MOSCRCF"]')
    mainck_rc_freq = clk_comp.createKeyValueSetSymbol("CLK_MAINCK_MOSCRCF", mainck_menu)
    mainck_rc_freq.setLabel("RC Oscillator Frequency")
    mainck_rc_freq.setDescription("Selects the output frequency of the Main RC Oscillator")
    mainck_rc_freq.setDisplayMode("Key")
    mainck_rc_freq.setOutputMode("Key")
    for value in mainck_rc_freq_vg_node.getChildren():
        mainck_rc_freq.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mainck_rc_freq.setDefaultValue(RC_FREQ_DEFAULT)

    # Main Clock Crystal Oscillator Enable
    mainck_xtal_en = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCXTEN", mainck_menu)
    mainck_xtal_en.setLabel("Enable External Oscillator")
    mainck_xtal_en.setDescription("Enables the Main crystal oscillator. Oscillator ByPass must be disabled")
    mainck_xtal_en.setDefaultValue(False)

    # Main Clock Crystal Oscillator Select (default is RC)
    mainck_xtal_sel = clk_comp.createKeyValueSetSymbol("CLK_MAINCK_MOSCSEL", mainck_menu)
    mainck_xtal_sel.setLabel("Main Clock Source Selection")
    mainck_xtal_sel.setDescription("This option is used to selct the source for the Main Clock")
    mainck_xtal_sel.setOutputMode("Value")
    mainck_xtal_sel.setDisplayMode("Description")
    mainck_xtal_sel.addKey("Internal RC", str(0), "Internal RC Oscilator")
    mainck_xtal_sel.addKey("External Osc", str(1), "External Oscillator")

    # Main Clock Oscillator Bypass (default is RC)
    mainck_bp_sel = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCXTBY", mainck_menu)
    mainck_bp_sel.setLabel("Bypass Crystal Oscillator")
    mainck_bp_sel.setDescription("The external crystal oscillator is bypassed and external clock is used.")
    mainck_bp_sel.setDefaultValue(False)

    # Main Clock Startup Time
    mainck_xtal_start = clk_comp.createIntegerSymbol("CLK_MAINCK_MOSCXTST", mainck_menu)
    mainck_xtal_start.setLabel("External Oscillator Startup")
    mainck_xtal_start.setDescription("Specifies the number of MD_SLCK cycles multiplied by 8 for the main crystal oscillator start-up time")
    mainck_xtal_start.setDefaultValue(0)
    mainck_xtal_start.setMin(0)
    mainck_xtal_start.setMax(255)

    # Main Clock External Frequency
    mainck_bp_freq = clk_comp.createIntegerSymbol("CLK_MAINCK_EXT_FREQ", mainck_menu)
    mainck_bp_freq.setLabel("External/XTAL Freq (Hz)")
    mainck_bp_freq.setDescription("External Clock / XTAL frequency on pin XIN")
    mainck_bp_freq.setDefaultValue(10000000)
    # Datasheet section 25.2 gives 3MHz to 20Mhz
    mainck_bp_freq.setMin(3000000)
    mainck_bp_freq.setMax(20000000)

    # MAINCK Frequency
    mainck_freq = clk_comp.createIntegerSymbol("CLK_MAINCK_FREQ", mainck_menu)
    mainck_freq.setLabel("MAINCK Frequency (HZ)")
    mainck_freq.setDefaultValue(int(mainck_rc_freq.getKey(mainck_rc_freq.getValue()).split("_")[1]) * 1000000)
    mainck_freq.setReadOnly(True)
    mainck_freq.setVisible(True)
    mainck_freq.setDependencies(upd_mainck_freq, ["CLK_MAINCK_MOSCRCF", "CLK_MAINCK_MOSCSEL", "CLK_MAINCK_MOSCXTBY", "CLK_MAINCK_EXT_FREQ"])

# RC2 OSCILLATOR MENU
def __rc2_clock_menu(clk_comp, clk_menu):
    rc2ck_menu = clk_comp.createMenuSymbol("CLK_RC2_MENU", clk_menu)
    rc2ck_menu.setLabel("RC2 Oscillator (RC2CK)")
    rc2ck_menu.setDescription("RC2 Oscillator Configuration")

    # RC2 Clock Enable
    rc2ck_en = clk_comp.createBooleanSymbol("CLK_RC2CK_EN", rc2ck_menu)
    rc2ck_en.setLabel("Enable RC2 Oscillator")
    rc2ck_en.setDescription("Enables the 2nd fast oscillator")
    rc2ck_en.setDefaultValue(True)

    # RC2 Frequency Selection
    rc2ck_sel_freq_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_OSC2__OSCRCF"]')
    rc2ck_sel_freq = clk_comp.createKeyValueSetSymbol("CLK_RC2CK_OSCRCF", rc2ck_menu)
    rc2ck_sel_freq.setLabel("Oscillator Frequency Selection")
    rc2ck_sel_freq.setDescription("Selects the output Frequency for the second Fast RC Oscillator")
    rc2ck_sel_freq.setDisplayMode("Key")
    rc2ck_sel_freq.setOutputMode("Key")
    for value in rc2ck_sel_freq_vg_node.getChildren():
        rc2ck_sel_freq.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    rc2ck_sel_freq.setDefaultValue(RC_FREQ_DEFAULT)

    # RC2 Frequency
    rc2ck_freq = clk_comp.createIntegerSymbol("CLK_RC2CK_FREQ", rc2ck_menu)
    rc2ck_freq.setLabel("RC2CK Frequency (HZ)")
    rc2ck_freq.setDefaultValue(int(rc2ck_sel_freq.getKey(rc2ck_sel_freq.getValue()).split("_")[1]) * 1000000)
    rc2ck_freq.setVisible(True)
    rc2ck_freq.setReadOnly(True)
    rc2ck_freq.setDependencies(upd_rc2ck_freq, ["CLK_RC2CK_EN", "CLK_RC2CK_OSCRCF"])

# PLLA CLOCK MENU
def __plla_clock_menu(clk_comp, clk_menu):
    pllack_menu = clk_comp.createMenuSymbol("CLK_PLLACK_MENU", clk_menu)
    pllack_menu.setLabel("PLLA Clock (PLLACK)")
    pllack_menu.setDescription("PLLA Clock Configuration")

    # Section 2.5 - A 40 MHz to 200 MHz Programmable PLL (input from 8 MHz to 20 MHz)

    # PLLA Front End Divider
    pllack_diva = clk_comp.createIntegerSymbol("CLK_PLLACK_DIVA", pllack_menu)
    pllack_diva.setLabel("PLL Front End divider")
    pllack_diva.setDescription("Divides the output of PLL. If Dicvider is set to 0 PLL is disabled")
    pllack_diva.setDefaultValue(0)
    pllack_diva.setMin(0)
    pllack_diva.setMax(64)

    # PLLA Multiplier
    pllack_mula = clk_comp.createIntegerSymbol("CLK_PLLACK_MULA", pllack_menu)
    pllack_mula.setLabel("PLLA Multiplier")
    pllack_mula.setDescription("PLLCK frequency is the PLLA input frequency multiplied by MULA + 1.")
    pllack_mula.setDefaultValue(0)
    pllack_mula.setMin(0)
    pllack_mula.setMax(56)

    # PLLA Frequency Range
    pllack_vco_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="CKGR_PLLAR__FREQ_VCO"]')
    pllack_vco = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_FREQ_VCO", pllack_menu)
    pllack_vco.setLabel("VCO Frequency Range")
    pllack_vco.setDescription("This is used to setup the output frequency range of VCO")
    pllack_vco.setDisplayMode("Description")
    pllack_vco.setOutputMode("Key")
    for value in pllack_vco_vg_node.getChildren():
        pllack_vco.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_vco.setDefaultValue(0)

    # PLLA Internal Filter Resistor Value (SRA)
    pllack_sra_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__SRA"]')
    pllack_sra = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_SRA", pllack_menu)
    pllack_sra.setLabel("Filter Internal Resistor Value")
    pllack_sra.setDescription("Internal Filter PLL – Select Internal Resistor Value")
    pllack_sra.setDisplayMode("Description")
    pllack_sra.setOutputMode("Key")
    for value in pllack_sra_vg_node.getChildren():
        pllack_sra.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_sra.setDefaultValue(0)

    # PLLA Internal Filter Capaticance Value (SCA)
    pllack_sca_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__SCA"]')
    pllack_sca = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_SCA", pllack_menu)
    pllack_sca.setLabel("Filter Internal Capaticance Value")
    pllack_sca.setDescription("Internal Filter PLL – Select Internal Capaticance Value")
    pllack_sca.setDisplayMode("Description")
    pllack_sca.setOutputMode("Key")
    for value in pllack_sca_vg_node.getChildren():
        pllack_sca.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_sca.setDefaultValue(0)

    # PLLA Output Current (OUTCUR_PLLA)
    pllack_outcur_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__OUTCUR_PLLA"]')
    pllack_outcur = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_OUTCUR", pllack_menu)
    pllack_outcur.setLabel("PLLA Output Current")
    pllack_outcur.setDescription("PLLA Output Current")
    pllack_outcur.setDisplayMode("Description")
    pllack_outcur.setOutputMode("Key")
    for value in pllack_outcur_vg_node.getChildren():
        pllack_outcur.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_outcur.setDefaultValue(0)

    # PLLACK Frequency
    pllack_freq = clk_comp.createIntegerSymbol("CLK_PLLACK_FREQ", pllack_menu)
    pllack_freq.setLabel("PLLACK Frequency (HZ)")
    pllack_freq.setDefaultValue(0)
    pllack_freq.setReadOnly(True)
    pllack_freq.setVisible(True)
    pllack_freq.setDependencies(upd_pllack_freq, ["CLK_PLLACK_DIVA", "CLK_PLLACK_MULA", "CLK_MAINCK_FREQ"])

    #default clock
    pllack_mula.setValue(9)
    pllack_diva.setValue(1)
# PLLB CLOCK MENU
def __pllb_clock_menu(clk_comp, clk_menu):
    pllbck_menu = clk_comp.createMenuSymbol("CLK_PLLBCK_MENU", clk_menu)
    pllbck_menu.setLabel("PLLB Clock (PLLBCK)")
    pllbck_menu.setDescription("PLLB Clock Configuration")

    # Section 2.5 - A 40 MHz to 200 MHz Programmable PLL (input from 8 MHz to 20 MHz)

    # PLLB Front End Divider
    pllbck_divb = clk_comp.createIntegerSymbol("CLK_PLLBCK_DIVB", pllbck_menu)
    pllbck_divb.setLabel("PLL Front End divider")
    pllbck_divb.setDescription("Divides the output of PLL. If Dicvider is set to 0 PLL is disabled")
    pllbck_divb.setDefaultValue(0)
    pllbck_divb.setMin(0)
    pllbck_divb.setMax(64)

    # PLLB Multiplier
    pllbck_mulb = clk_comp.createIntegerSymbol("CLK_PLLBCK_MULB", pllbck_menu)
    pllbck_mulb.setLabel("PLLB Multiplier")
    pllbck_mulb.setDescription("PLLCK frequency is the PLLA input frequency multiplied by MULA + 1.")
    pllbck_mulb.setDefaultValue(0)
    pllbck_mulb.setMin(0)
    pllbck_mulb.setMax(56)

    # PLLB Frequency Range
    pllbck_vco_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="CKGR_PLLBR__FREQ_VCO"]')
    pllbck_vco = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_FREQ_VCO", pllbck_menu)
    pllbck_vco.setLabel("VCO Frequency Range")
    pllbck_vco.setDescription("This is used to setup the output frequency range of VCO")
    pllbck_vco.setDisplayMode("Description")
    pllbck_vco.setOutputMode("Key")
    for value in pllbck_vco_vg_node.getChildren():
        pllbck_vco.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_vco.setDefaultValue(0)

    # PLLB Clock Source
    pllbck_srcb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="CKGR_PLLBR__SRCB"]')
    pllbck_srcb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SRCB", pllbck_menu)
    pllbck_srcb.setLabel("PLLB Source Clock Selection")
    pllbck_srcb.setDescription("Selects clock source for PLLB")
    pllbck_srcb.setDisplayMode("Description")
    pllbck_srcb.setOutputMode("Key")
    for value in pllbck_srcb_vg_node.getChildren():
        pllbck_srcb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_srcb.setDefaultValue(0)

    # PLLB Internal Filter Resistor Value (SRB)
    pllbck_srb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__SRB"]')
    pllbck_srb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SRB", pllbck_menu)
    pllbck_srb.setLabel("Filter Internal Resistor Value")
    pllbck_srb.setDescription("Internal Filter PLL – Select Internal Resistor Value")
    pllbck_srb.setDisplayMode("Description")
    pllbck_srb.setOutputMode("Key")
    for value in pllbck_srb_vg_node.getChildren():
        pllbck_srb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_srb.setDefaultValue(0)

    # PLLB Internal Filter Capaticance Value (SCB)
    pllbck_scb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__SCB"]')
    pllbck_scb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SCB", pllbck_menu)
    pllbck_scb.setLabel("Filter Internal Capaticance Value")
    pllbck_scb.setDescription("Internal Filter PLL – Select Internal Capaticance Value")
    pllbck_scb.setDisplayMode("Description")
    pllbck_scb.setOutputMode("Key")
    for value in pllbck_scb_vg_node.getChildren():
        pllbck_scb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_scb.setDefaultValue(0)

    # PLLB Output Current (OUTCUR_PLLB)
    pllbck_outcur_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PLL_CFG__OUTCUR_PLLB"]')
    pllbck_outcur = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_OUTCUR", pllbck_menu)
    pllbck_outcur.setLabel("PLLB Output Current")
    pllbck_outcur.setDescription("PLLB Output Current")
    pllbck_outcur.setDisplayMode("Description")
    pllbck_outcur.setOutputMode("Key")
    for value in pllbck_outcur_vg_node.getChildren():
        pllbck_outcur.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_outcur.setDefaultValue(0)

    # PLLBCK Frequency
    pllbck_freq = clk_comp.createIntegerSymbol("CLK_PLLBCK_FREQ", pllbck_menu)
    pllbck_freq.setLabel("PLLBCK Frequency (HZ)")
    pllbck_freq.setDefaultValue(0)
    pllbck_freq.setReadOnly(True)
    pllbck_freq.setVisible(True)
    pllbck_freq.setDependencies(upd_pllbck_freq, ["CLK_PLLBCK_DIVB", "CLK_PLLBCK_MULB", "CLK_MAINCK_FREQ", "CLK_RC2CK_FREQ", "CLK_PLLBCK_SRCB"])

# MASTER CLOCK MENU
def __mast_clock_menu(clk_comp, clk_menu):
    mck_menu = clk_comp.createMenuSymbol("CLK_MCK_MENU", clk_menu)
    mck_menu.setLabel("Master Clock (MCK)")
    mck_menu.setDescription("Master Clock Configuration")

    # Master Clock Source
    mck_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_MCKR__CSS"]')
    mck_css = clk_comp.createKeyValueSetSymbol("CLK_MCK_CSS", mck_menu)
    mck_css.setLabel("Clock Source")
    mck_css.setDescription("This option selects the source for the Master Clock")
    mck_css.setDisplayMode("Key")
    mck_css.setOutputMode("Key")
    for value in mck_css_vg_node.getChildren():
        mck_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_css.setDefaultValue(1)

    # Master Clock Prescaler
    mck_pres_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_MCKR__PRES"]')
    mck_pres = clk_comp.createKeyValueSetSymbol("CLK_MCK_PRES", mck_menu)
    mck_pres.setLabel("Clock Prescalar")
    mck_pres.setDescription("Divides the input clock by Selected prescalar")
    mck_pres.setDisplayMode("Description")
    mck_pres.setOutputMode("Key")
    for value in mck_pres_vg_node.getChildren():
        mck_pres.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_pres.setDefaultValue(0)

    # Master Clock Divider
    mck_mdiv_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_MCKR__MDIV"]')
    mck_mdiv = clk_comp.createKeyValueSetSymbol("CLK_MCK_MDIV", mck_menu)
    mck_mdiv.setLabel("Master Clock Divider")
    mck_mdiv.setDescription("Divides the output Master Clock by selected divider")
    mck_mdiv.setDisplayMode("Description")
    mck_mdiv.setOutputMode("Key")
    for value in mck_mdiv_vg_node.getChildren():
        mck_mdiv.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_mdiv.setDefaultValue(0)

    # Processor Free Running Clock Frequency
    fclk_freq = clk_comp.createIntegerSymbol("CPU_CLOCK_FREQUENCY", mck_menu)
    fclk_freq.setLabel("FCLK Frequency (HZ)")
    fclk_freq.setDefaultValue(Database.getSymbolValue("core", "CLK_MAINCK_FREQ"))
    fclk_freq.setReadOnly(True)
    fclk_freq.setVisible(True)
    fclk_freq.setDependencies(upd_fclk_freq, ["CLK_MCK_CSS", "CLK_MCK_PRES", "CLK_MAINCK_FREQ", "CLK_MD_SLCK_FREQ", "CLK_PLLACK_FREQ"])

    # SysTick External Clock Frequency
    tick_freq = clk_comp.createIntegerSymbol("SYSTICK_CLOCK_FREQUENCY", mck_menu)
    tick_freq.setLabel("SysTick Frequency (HZ)")
    tick_freq.setDefaultValue(fclk_freq.getValue() / SYSTICK_EXT_DIV)
    tick_freq.setReadOnly(True)
    tick_freq.setVisible(True)
    tick_freq.setDependencies(upd_systick_freq, ["CPU_CLOCK_FREQUENCY"])

    # Master Clock Frequency
    mck_freq = clk_comp.createIntegerSymbol("CLK_MCK_FREQ", mck_menu)
    mck_freq.setLabel("MCK Frequency (HZ)")
    mck_freq.setDefaultValue(Database.getSymbolValue("core", "CLK_MAINCK_FREQ"))
    mck_freq.setReadOnly(True)
    mck_freq.setVisible(True)
    mck_freq.setDependencies(upd_mck_freq, ["CLK_MCK_MDIV", "CPU_CLOCK_FREQUENCY"])

    #default clock
    mck_css.setValue(2)
    mck_mdiv.setValue(1)
# PROGRAMMABLE CLOCK MENU
def __prog_clock_menu(clk_comp, clk_menu):
    pck_menu = clk_comp.createMenuSymbol("CLK_PCK_MENU", clk_menu)
    pck_menu.setLabel("Programmable Clocks (PCK)")
    pck_menu.setDescription("Programmable Clocks")

    num_pcks = int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]').getAttribute("count"))
    for pckx in range(0, num_pcks):
        pckx_en = clk_comp.createBooleanSymbol("CLK_PCK"+str(pckx)+"_EN", pck_menu)
        pckx_en.setLabel("Enable PCK"+str(pckx))

        pckx_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PCK__CSS"]')
        pckx_css = clk_comp.createKeyValueSetSymbol("CLK_PCK"+str(pckx)+"_CSS", pckx_en)
        pckx_css.setLabel("Clock Source")
        pckx_css.setDescription("Selects source for the programmable clock")
        pckx_css.setDisplayMode("Key")
        pckx_css.setOutputMode("Key")
        for value in pckx_css_vg_node.getChildren():
            pckx_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

        pckx_pres = clk_comp.createIntegerSymbol("CLK_PCK"+str(pckx)+"_PRES", pckx_en)
        pckx_pres.setLabel("Programmable Clock Prescalar")
        pckx_pres.setDescription("Divides the input clock by PRES+1.")
        pckx_pres.setMin(0)
        pckx_pres.setMax(255)

        pckx_freq = clk_comp.createIntegerSymbol("CLK_PCK"+str(pckx)+"_FREQ", pckx_en)
        pckx_freq.setLabel("PCK"+str(pckx)+" Frequency (HZ)")
        pckx_freq.setDefaultValue(0)
        pckx_freq.setReadOnly(True)
        pckx_freq.setVisible(True)
        pckx_freq.setDependencies(upd_pck_freq, ["CLK_PCK"+str(pckx)+"_EN", "CLK_PCK"+str(pckx)+"_CSS", "CLK_PCK"+str(pckx)+"_PRES",
                "CLK_MAINCK_FREQ", "CLK_MD_SLCK_FREQ", "CLK_PLLACK_FREQ", "CLK_PLLBCK_FREQ", "CLK_MCK_FREQ"])


# PERIPHERAL CLOCK MENU
def __peri_clock_menu(clk_comp, clk_menu):
    pcr_menu = clk_comp.createMenuSymbol("CLK_PCR_MENU", clk_menu)
    pcr_menu.setLabel("Peripheral Clock Configuration")

    # [INSTANCE]_CLOCK_ENABLE
    # [INSTANCE]_CLOCK_FREQUENCY
    # CLK_ID_NAME_x
    peripherals_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
    # Look at each of the peripherals
    for module_node in peripherals_node.getChildren():
        module_name = module_node.getAttribute("name")
        sym_constructor = freq_sym_const_dict.get(module_name, create_default_freq_sym)
        # Look at each instance in the peripheral
        for instance_node in module_node.getChildren():
            instance_name = instance_node.getAttribute("name")
            parameters_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="'+module_name+'"]/instance@[name="'+instance_name+'"]/parameters')
            if parameters_node is None:
                continue
            # Look at each param entry for this instance
            param_scan = True
            for param_entry in parameters_node.getChildren():
                if param_entry is None:
                    continue

                param_name = param_entry.getAttribute("name")

                if "CLOCK_ID" in param_name:
                    clock_id_name = instance_name + param_entry.getAttribute("name").split("CLOCK_ID")[1]
                    clock_id = int(param_entry.getAttribute("value"))

                    periph_menu = clk_comp.createMenuSymbol("CLK_"+clock_id_name+"_MENU", pcr_menu)
                    periph_menu.setLabel(clock_id_name)

                    # Create peripheral clock enable symbol [instance]_CLOCK_ENABLE
                    periph_en = clk_comp.createBooleanSymbol(clock_id_name+"_CLOCK_ENABLE", periph_menu)
                    periph_en.setLabel("Peripheral Clock Enable")
                    periph_en.setDefaultValue(False)

                    periph_id = clk_comp.createStringSymbol("CLK_ID_NAME_"+str(clock_id), periph_menu)
                    periph_id.setDefaultValue(clock_id_name)
                    periph_id.setReadOnly(True)
                    periph_id.setVisible(False)

                    # Create peripheral clock frequency symbol [instance]_CLOCK_FREQUENCY
                    sym_constructor(clock_id_name, clk_comp, periph_menu)


if __name__ == "__main__":

    global perifreq
    # Main clock configuration menu
    clk_menu = coreComponent.createMenuSymbol("CLK_MENU", None)
    clk_menu.setLabel("Clock (PMC)")
    clk_menu.setDescription("Clock configuration")

    # Create clock sub menus
    __slow_clock_menu(coreComponent, clk_menu)
    __main_clock_menu(coreComponent, clk_menu)
    __rc2_clock_menu( coreComponent, clk_menu)
    __plla_clock_menu(coreComponent, clk_menu)
    __pllb_clock_menu(coreComponent, clk_menu)
    __mast_clock_menu(coreComponent, clk_menu)
    __prog_clock_menu(coreComponent, clk_menu)
    __peri_clock_menu(coreComponent, clk_menu)


    #File handling
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_sam_rh71/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_sam_rh71/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_rh71/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_rh71/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
