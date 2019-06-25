
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
    }

# Default settings
global SLCK_RC_FREQ
SLCK_RC_FREQ = 32000
global SLCK_XTAL_FREQ
SLCK_XTAL_FREQ = 32768
global RC_FREQ_DEFAULT
RC_FREQ_DEFAULT = 2

global upd_clone
def upd_clone(symbol, event):
    if symbol.getValue() != event['value']:
        symbol.setValue(event['value'])

global upd_clone_dsp
def upd_clone_dsp(symbol, event):
    if symbol.getValue() != event['value']:
        symbol.setValue(event['value'])
        if event['value'] == 0:
            symbol.setVisible(False)
        else:
            symbol.setVisible(True)

global upd_slck_bp_ro
def upd_slck_bp_ro(symbol, event):
    if event["value"] is True:
        symbol.setReadOnly(False)
    else:
        # Setting read only will reset value
        symbol.setReadOnly(True)

global upd_slck_td_freq
def upd_slck_td_freq(symbol, event):
    if event['source'].getSymbolValue("CLK_SLCK_TDXTALSEL") is False:
        freq = SLCK_RC_FREQ
    else:
        if event['source'].getSymbolValue("CLK_SLCK_OSCBYPASS") is False:
            freq = SLCK_XTAL_FREQ
        else:
            freq = event['source'].getSymbolValue("CLK_SLCK_EXT_FREQ")
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_slck_md_freq
def upd_slck_md_freq(symbol, event):
    if event['source'].getSymbolValue("CLK_SLCK_MDXTALSEL") is False:
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
    if event['source'].getSymbolValue("CLK_MAINCK_MOSCSEL") is False:
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

global upd_tick_freq
def upd_tick_freq(symbol, event):
    freq = event['value'] / 8
    if symbol.getValue() != freq:
        symbol.setValue(freq)

global upd_mck_freq
def upd_mck_freq(symbol, event):
    pres = event['source'].getSymbolValue("CLK_MCK_PRES")
    mdiv = event['source'].getSymbolValue("CLK_MCK_MDIV")
    mck_css = event['source'].getSymbolByID("CLK_MCK_CSS")
    freq = event['source'].getSymbolValue(CLK_XLAT[mck_css.getKey(mck_css.getValue())]) >> (pres + mdiv)
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
    frequency = -1
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    op_mode = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_MODE")
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
    if frequency >= 0:
        symbol.setValue(frequency)

global upd_tc_freq
def upd_tc_freq(symbol, event):
    # symbol is named as "TC{instance_number}_CH{channel_number}_CLOCK_FREQUENCY.
    # Extract the instance number
    instance_num = symbol.getID().split("TC")[1].split("_")[0]
    # extract the channel number
    channel_num = symbol.getID().split("_CH")[1].split("_")[0]

    # check if the relevant channel is enabled
    if (Database.getSymbolValue("tc" + str(instance_num), "TC" + str(channel_num) + "_ENABLE") == True):
    
        # Find the current clock source for the channel
        clk_src = Database.getSymbolValue("tc" + str(instance_num), "TC" + str(channel_num) + "_CMR_TCCLKS")
        # if clock source is processor independent GCLK
        if (clk_src == 1):
            if channel_num==0:
                clk_frequency = Database.getSymbolValue("core", "TC" + str(instance_num) + "_CHANNEL0_GCLK_FREQUENCY")
            else:
                clk_frequency = 0
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

# WARNING Messages Update Routines
global warn_event_value_0
def warn_event_value_0(symbol, event):
    if event['value'] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

global warn_slck_bp
def warn_slck_bp(symbol, event):
    td_xtal_sel = event['source'].getSymbolValue("CLK_SLCK_TDXTALSEL")
    md_xtal_sel = event['source'].getSymbolValue("CLK_SLCK_MDXTALSEL")
    bp_sel  = event['source'].getSymbolValue("CLK_SLCK_OSCBYPASS")
    symbol.setVisible(bp_sel==True and td_xtal_sel==False and md_xtal_sel==False)

global warn_mainck_not_used
def warn_mainck_not_used(symbol, event):
    rc_en = event['source'].getSymbolValue("CLK_MAINCK_MOSCRCEN")
    xtal_en = event['source'].getSymbolValue("CLK_MAINCK_MOSCXTEN")
    xtal_sel = event['source'].getSymbolValue("CLK_MAINCK_MOSCSEL")
    bp_sel = event['source'].getSymbolValue("CLK_MAINCK_MOSCXTBY")
    symbol.setVisible((rc_en==True and xtal_sel==True) or (bp_sel==True and xtal_sel==False) or (xtal_en==True and (xtal_sel==False or bp_sel==True)))

global warn_mainck_not_en
def warn_mainck_not_en(symbol, event):
    rc_en = event['source'].getSymbolValue("CLK_MAINCK_MOSCRCEN")
    xtal_en = event['source'].getSymbolValue("CLK_MAINCK_MOSCXTEN")
    xtal_sel = event['source'].getSymbolValue("CLK_MAINCK_MOSCSEL")
    bp_sel = event['source'].getSymbolValue("CLK_MAINCK_MOSCXTBY")
    symbol.setVisible((rc_en==False and xtal_sel==False) or (xtal_en==False and xtal_sel==True and bp_sel==False))

#global warn_pckx_src_not_en
#def warn_pckx_src_not_en(symbol, event):
#    idx = int(symbol.getID().split("PCK")[1].split("_")[0])
#    en = event['source'].getSymbolValue("CLK_PCK"+str(idx)+"_EN")
#    freq = event['source'].getSymbolValue("CLK_PCK"+str(idx)+"_FREQ")
#    if en==True and freq==0:
#        symbol.setVisible(True)
#    else:
#        symbol.setVisible(False)

# Create Generic Clock Entries
global create_gclk_entries
def create_gclk_entries (clock_id_name, clock_comp, clk_menu):
    gclk_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="EN"]')
    gclk_en = clock_comp.createBooleanSymbol(clock_id_name+"_GCLK_ENABLE", clk_menu)
    gclk_en.setLabel("Generic Clock Enable")
    gclk_en.setDescription(gclk_en_node.getAttribute("caption"))
    gclk_en.setDefaultValue(False)

    gclk_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKCSS"]')
    gclk_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+gclk_css_node.getAttribute("values")+'"]')
    gclk_css = clock_comp.createKeyValueSetSymbol(clock_id_name+"_GCLK_CSS", clk_menu)
    gclk_css.setLabel(gclk_css_node.getAttribute("name"))
    gclk_css.setDescription(gclk_css_node.getAttribute("caption"))
    gclk_css.setDisplayMode("Key")
    gclk_css.setOutputMode("Key")
    for value in gclk_css_vg_node.getChildren():
        gclk_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    gclk_css.setDefaultValue(0)

    gclk_div_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKDIV"]')
    gclk_div = clock_comp.createIntegerSymbol(clock_id_name+"_GCLK_DIV", clk_menu)
    gclk_div.setLabel(gclk_div_node.getAttribute("name"))
    gclk_div.setDescription(gclk_div_node.getAttribute("caption"))
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
    

global create_default_freq_sym
def create_default_freq_sym (clock_id_name, clock_comp, clk_menu):
    # Create peripheral clock frequency symbol [clock_id_name]_CLOCK_FREQUENCY
    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setReadOnly(True)
    freq_sym.setVisible(False)
    freq_sym.setDefaultValue(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
    freq_sym.setDependencies(upd_clone, ["CLK_MCK_FREQ"])

global create_flexcom_freq_sym
def create_flexcom_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)

    freq_sym = clock_comp.createIntegerSymbol(clock_id_name + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setVisible(False)
    freq_sym.setReadOnly(True)
    freq_sym.setDefaultValue(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
    freq_sym.setDependencies(upd_flexcom_freq,
        [   "CLK_MCK_FREQ",
            clock_id_name + "_GCLK_FREQUENCY",
            clock_id_name.lower() + ".FLEXCOM_MODE",
            clock_id_name.lower() + ".FLEXCOM_USART_MR_USCLKS",
            clock_id_name.lower() + ".FLEXCOM_SPI_MR_BRSRCCLK",
            clock_id_name.lower() + ".FLEXCOM_TWI_CWGR_BRSRCCLK"])

def create_hemc_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

def create_ip1553_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

def create_mcan_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

def create_spw_freq_sym(clock_id_name, clock_comp, clk_menu):
    create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    create_default_freq_sym(clock_id_name, clock_comp, clk_menu)

def create_tc_freq_sym(clock_id_name, clock_comp, clk_menu):
    id_list = clock_id_name.split("_CHANNEL")
    inst = id_list[0]
    chan = int(id_list[1])
    if chan==0:
        create_gclk_entries(clock_id_name, clock_comp, clk_menu)
    freq_sym = clock_comp.createIntegerSymbol(inst + "_CH" + str(chan) + "_CLOCK_FREQUENCY", clk_menu)
    freq_sym.setReadOnly(True)
    freq_sym.setVisible(False)
    freq_sym.setDefaultValue(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
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
        freq_dmy.setVisible(False)
        freq_dmy.setDefaultValue(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
        freq_dmy.setDependencies(upd_tc_freq,
            [   "CLK_MCK_FREQ",
                "CLK_MD_SLCK_FREQ",
                clock_id_name+"_GCLK_FREQUENCY",
                inst.lower() + ".TC" + str(chan) + "_CMR_TCCLKS",
                inst.lower() + ".TC" + str(chan) + "_ENABLE" ])

global freq_sym_const_dict
freq_sym_const_dict = { "FLEXCOM": create_flexcom_freq_sym,
                        "HEMC": create_hemc_freq_sym,
                        "IP1553": create_ip1553_freq_sym,
                        "MCAN": create_mcan_freq_sym,
                        "SPW": create_spw_freq_sym,
                        "TC": create_tc_freq_sym }

# SLOW CLOCK MENU
def __slow_clock_menu(clk_comp, clk_menu):
    slck_menu = clk_comp.createMenuSymbol("CLK_SLCK_MENU", clk_menu)
    slck_menu.setLabel("Slow Clock (SLCK)")
    slck_menu.setDescription("Slow Clock Configuration")

    # Timing Domain Slow Clock Crystal Oscillator Select (default is RC)
    slck_td_xtal_sel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_CR"]/bitfield@[name="TDXTALSEL"]')
    slck_td_xtal_sel = clk_comp.createBooleanSymbol("CLK_SLCK_TDXTALSEL", slck_menu)
    slck_td_xtal_sel.setLabel(slck_td_xtal_sel_node.getAttribute("name"))
    slck_td_xtal_sel.setDescription(slck_td_xtal_sel_node.getAttribute("caption"))
    slck_td_xtal_sel.setDefaultValue(False)

    # Monitoring Domain Slow Clock Crystal Oscillator Select (default is RC)
    slck_md_xtal_sel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_CR"]/bitfield@[name="MDXTALSEL"]')
    slck_md_xtal_sel = clk_comp.createBooleanSymbol("CLK_SLCK_MDXTALSEL", slck_menu)
    slck_md_xtal_sel.setLabel(slck_md_xtal_sel_node.getAttribute("name"))
    slck_md_xtal_sel.setDescription(slck_md_xtal_sel_node.getAttribute("caption"))
    slck_md_xtal_sel.setDefaultValue(False)

    # Slow Clock Oscillator Bypass (default is RC)
    slck_bp_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SUPC"]/register-group@[name="SUPC"]/register@[name="SUPC_MR"]/bitfield@[name="OSCBYPASS"]')
    slck_bp_sel = clk_comp.createBooleanSymbol("CLK_SLCK_OSCBYPASS", slck_menu)
    slck_bp_sel.setLabel(slck_bp_node.getAttribute("name"))
    slck_bp_sel.setDescription(slck_bp_node.getAttribute("caption"))
    slck_bp_sel.setDefaultValue(False)

    # Slow Clock External Bypass Frequency
    slck_bp_freq = clk_comp.createIntegerSymbol("CLK_SLCK_EXT_FREQ", slck_menu)
    slck_bp_freq.setLabel("External Clock Freq (Hz)")
    slck_bp_freq.setDescription("External bypass clock frequency on pin XIN32")
    slck_bp_freq.setDefaultValue(SLCK_XTAL_FREQ)
    slck_bp_freq.setMin(0)
    slck_bp_freq.setMax(10000000)
    slck_bp_freq.setReadOnly(True)
    slck_bp_freq.setDependencies(upd_slck_bp_ro, ["CLK_SLCK_OSCBYPASS"])

    # TD_SLCK Frequency Display
    slck_td_freq = clk_comp.createIntegerSymbol("CLK_TD_SLCK_FREQ", slck_menu)
    slck_td_freq.setLabel("TD_SLCK Frequency (HZ)")
    slck_td_freq.setDefaultValue(SLCK_RC_FREQ)
    slck_td_freq.setReadOnly(True)
    slck_td_freq.setVisible(False)
    slck_td_freq.setDependencies(upd_slck_td_freq, ["CLK_SLCK_OSCBYPASS", "CLK_SLCK_TDXTALSEL", "CLK_SLCK_EXT_FREQ"])

    # MD_SLCK Frequency Display
    slck_md_freq = clk_comp.createIntegerSymbol("CLK_MD_SLCK_FREQ", slck_menu)
    slck_md_freq.setLabel("MD_SLCK Frequency (HZ)")
    slck_md_freq.setDefaultValue(SLCK_RC_FREQ)
    slck_md_freq.setReadOnly(True)
    slck_md_freq.setVisible(False)
    slck_md_freq.setDependencies(upd_slck_md_freq, ["CLK_SLCK_OSCBYPASS", "CLK_SLCK_MDXTALSEL", "CLK_SLCK_EXT_FREQ"])

    # Warning message for bypass selected and xtal mux (for td_slck or md_slck) not set
    slck_warn_bp = clk_comp.createCommentSymbol("CLK_SLCK_WARN_BP", slck_menu)
    slck_warn_bp.setLabel("WARNING! Bypass selected but not used.")
    slck_warn_bp.setVisible(False)
    slck_warn_bp.setDependencies(warn_slck_bp, ["CLK_SLCK_TDXTALSEL", "CLK_SLCK_MDXTALSEL", "CLK_SLCK_OSCBYPASS"])

# MAIN CLOCK MENU
def __main_clock_menu(clk_comp, clk_menu):
    mainck_menu = clk_comp.createMenuSymbol("CLK_MAINCK_MENU", clk_menu)
    mainck_menu.setLabel("Main Clock (MAINCK)")
    mainck_menu.setDescription("Main Clock Configuration")

    # Main Clock RC Enable
    mainck_rc_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCRCEN"]')
    mainck_rc_en = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCRCEN", mainck_menu)
    mainck_rc_en.setLabel(mainck_rc_en_node.getAttribute("name"))
    mainck_rc_en.setDescription(mainck_rc_en_node.getAttribute("caption"))
    mainck_rc_en.setDefaultValue(True)

    # Main Clock RC Frequency Selection
    mainck_rc_freq_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCRCF"]')
    mainck_rc_freq_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mainck_rc_freq_node.getAttribute("values")+'"]')
    mainck_rc_freq = clk_comp.createKeyValueSetSymbol("CLK_MAINCK_MOSCRCF", mainck_menu)
    mainck_rc_freq.setLabel(mainck_rc_freq_node.getAttribute("name"))
    mainck_rc_freq.setDescription(mainck_rc_freq_node.getAttribute("caption"))
    mainck_rc_freq.setDisplayMode("Key")
    mainck_rc_freq.setOutputMode("Key")
    for value in mainck_rc_freq_vg_node.getChildren():
        mainck_rc_freq.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mainck_rc_freq.setDefaultValue(RC_FREQ_DEFAULT)

    # Main Clock Crystal Oscillator Enable
    mainck_xtal_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTEN"]')
    mainck_xtal_en = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCXTEN", mainck_menu)
    mainck_xtal_en.setLabel(mainck_xtal_en_node.getAttribute("name"))
    mainck_xtal_en.setDescription(mainck_xtal_en_node.getAttribute("caption"))
    mainck_xtal_en.setDefaultValue(False)

    # Main Clock Crystal Oscillator Select (default is RC)
    mainck_xtal_sel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCSEL"]')
    mainck_xtal_sel = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCSEL", mainck_menu)
    mainck_xtal_sel.setLabel(mainck_xtal_sel_node.getAttribute("name"))
    mainck_xtal_sel.setDescription(mainck_xtal_sel_node.getAttribute("caption"))
    mainck_xtal_sel.setDefaultValue(False)

    # Main Clock Oscillator Bypass (default is RC)
    mainck_bp_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTBY"]')
    mainck_bp_sel = clk_comp.createBooleanSymbol("CLK_MAINCK_MOSCXTBY", mainck_menu)
    mainck_bp_sel.setLabel(mainck_bp_node.getAttribute("name"))
    mainck_bp_sel.setDescription(mainck_bp_node.getAttribute("caption"))
    mainck_bp_sel.setDefaultValue(False)

    # Main Clock Startup Time
    mainck_xtal_start_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTST"]')
    mainck_xtal_start = clk_comp.createIntegerSymbol("CLK_MAINCK_MOSCXTST", mainck_menu)
    mainck_xtal_start.setLabel(mainck_xtal_start_node.getAttribute("name"))
    mainck_xtal_start.setDescription(mainck_xtal_start_node.getAttribute("caption"))
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
    mainck_freq.setVisible(False)
    mainck_freq.setDependencies(upd_mainck_freq, ["CLK_MAINCK_MOSCRCF", "CLK_MAINCK_MOSCSEL", "CLK_MAINCK_MOSCXTBY", "CLK_MAINCK_EXT_FREQ"])

    # WARNING! Clock source enabled but not used.
    mainck_warn_not_used = clk_comp.createCommentSymbol("CLK_MAINCK_WARN_NOT_USED", mainck_menu)
    mainck_warn_not_used.setLabel("WARNING! Clock source enabled but not used.")
    mainck_warn_not_used.setVisible(False)
    mainck_warn_not_used.setDependencies(warn_mainck_not_used, ["CLK_MAINCK_MOSCSEL", "CLK_MAINCK_MOSCRCEN", "CLK_MAINCK_MOSCXTEN", "CLK_MAINCK_MOSCXTBY"])

    # WARNING! Selected clock source not enabled.
    mainck_warn_not_en = clk_comp.createCommentSymbol("CLK_MAINCK_WARN_NOT_EN", mainck_menu)
    mainck_warn_not_en.setLabel("WARNING! Selected clock source not enabled.")
    mainck_warn_not_en.setVisible(False)
    mainck_warn_not_en.setDependencies(warn_mainck_not_en, ["CLK_MAINCK_MOSCSEL", "CLK_MAINCK_MOSCRCEN", "CLK_MAINCK_MOSCXTEN", "CLK_MAINCK_MOSCXTBY"])

# RC2 OSCILLATOR MENU
def __rc2_clock_menu(clk_comp, clk_menu):
    rc2ck_menu = clk_comp.createMenuSymbol("CLK_RC2_MENU", clk_menu)
    rc2ck_menu.setLabel("RC2 Oscillator (RC2CK)")
    rc2ck_menu.setDescription("RC2 Oscillator Configuration")

    # RC2 Clock Enable
    rc2ck_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_OSC2"]/bitfield@[name="EN"]')
    rc2ck_en = clk_comp.createBooleanSymbol("CLK_RC2CK_EN", rc2ck_menu)
    rc2ck_en.setLabel(rc2ck_en_node.getAttribute("name"))
    rc2ck_en.setDescription(rc2ck_en_node.getAttribute("caption"))
    rc2ck_en.setDefaultValue(True)

    # RC2 Frequency Selection
    rc2ck_sel_freq_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_OSC2"]/bitfield@[name="OSCRCF"]')
    rc2ck_sel_freq_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+rc2ck_sel_freq_node.getAttribute("values")+'"]')
    rc2ck_sel_freq = clk_comp.createKeyValueSetSymbol("CLK_RC2CK_OSCRCF", rc2ck_menu)
    rc2ck_sel_freq.setLabel(rc2ck_sel_freq_node.getAttribute("name"))
    rc2ck_sel_freq.setDescription(rc2ck_sel_freq_node.getAttribute("caption"))
    rc2ck_sel_freq.setDisplayMode("Key")
    rc2ck_sel_freq.setOutputMode("Key")
    for value in rc2ck_sel_freq_vg_node.getChildren():
        rc2ck_sel_freq.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    rc2ck_sel_freq.setDefaultValue(RC_FREQ_DEFAULT)

    # RC2 Frequency
    rc2ck_freq = clk_comp.createIntegerSymbol("CLK_RC2CK_FREQ", rc2ck_menu)
    rc2ck_freq.setLabel("RC2CK Frequency (HZ)")
    rc2ck_freq.setDefaultValue(int(rc2ck_sel_freq.getKey(rc2ck_sel_freq.getValue()).split("_")[1]) * 1000000)
    rc2ck_freq.setVisible(False)
    rc2ck_freq.setReadOnly(True)
    rc2ck_freq.setDependencies(upd_rc2ck_freq, ["CLK_RC2CK_EN", "CLK_RC2CK_OSCRCF"])

# PLLA CLOCK MENU
def __plla_clock_menu(clk_comp, clk_menu):
    pllack_menu = clk_comp.createMenuSymbol("CLK_PLLACK_MENU", clk_menu)
    pllack_menu.setLabel("PLLA Clock (PLLACK)")
    pllack_menu.setDescription("PLLA Clock Configuration")

    # Section 2.5 - A 40 MHz to 200 MHz Programmable PLL (input from 8 MHz to 20 MHz)

    # PLLA Front End Divider
    pllack_diva_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLAR"]/bitfield@[name="DIVA"]')
    pllack_diva = clk_comp.createIntegerSymbol("CLK_PLLACK_DIVA", pllack_menu)
    pllack_diva.setLabel(pllack_diva_node.getAttribute("name"))
    pllack_diva.setDescription(pllack_diva_node.getAttribute("caption"))
    pllack_diva.setDefaultValue(0)
    pllack_diva.setMin(0)
    pllack_diva.setMax(64)

    # PLLA Multiplier
    pllack_mula_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLAR"]/bitfield@[name="MULA"]')
    pllack_mula = clk_comp.createIntegerSymbol("CLK_PLLACK_MULA", pllack_menu)
    pllack_mula.setLabel(pllack_mula_node.getAttribute("name"))
    pllack_mula.setDescription(pllack_mula_node.getAttribute("caption"))
    pllack_mula.setDefaultValue(0)
    pllack_mula.setMin(0)
    pllack_mula.setMax(56)

    # PLLA Multiplier Max
    pllack_mmax_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PMMR"]/bitfield@[name="PLLA_MMAX"]')
    pllack_mmax = clk_comp.createIntegerSymbol("CLK_PLLACK_MMAX", pllack_menu)
    pllack_mmax.setLabel(pllack_mmax_node.getAttribute("name"))
    pllack_mmax.setDescription(pllack_mmax_node.getAttribute("caption"))
    pllack_mmax.setDefaultValue(2047)
    pllack_mmax.setMin(0)
    pllack_mmax.setMax(2047)

    # PLLA count of MD_SLCK cycles before LOCKB set
    pllack_cnta_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLAR"]/bitfield@[name="PLLACOUNT"]')
    pllack_cnta = clk_comp.createIntegerSymbol("CLK_PLLACK_PLLACOUNT", pllack_menu)
    pllack_cnta.setLabel(pllack_cnta_node.getAttribute("name"))
    pllack_cnta.setDescription(pllack_cnta_node.getAttribute("caption"))
    pllack_cnta.setDefaultValue(63)
    pllack_cnta.setMin(0)
    pllack_cnta.setMax(63)

    # PLLA Frequency Range
    pllack_vco_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLAR"]/bitfield@[name="FREQ_VCO"]')
    pllack_vco_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllack_vco_node.getAttribute("values")+'"]')
    pllack_vco = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_FREQ_VCO", pllack_menu)
    pllack_vco.setLabel(pllack_vco_node.getAttribute("name"))
    pllack_vco.setDescription(pllack_vco_node.getAttribute("caption"))
    pllack_vco.setDisplayMode("Key")
    pllack_vco.setOutputMode("Key")
    for value in pllack_vco_vg_node.getChildren():
        pllack_vco.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_vco.setDefaultValue(0)

    # PLLA Internal Filter Resistor Value (SRA)
    pllack_sra_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="SRA"]')
    pllack_sra_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllack_sra_node.getAttribute("values")+'"]')
    pllack_sra = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_SRA", pllack_menu)
    pllack_sra.setLabel(pllack_sra_node.getAttribute("name"))
    pllack_sra.setDescription(pllack_sra_node.getAttribute("caption"))
    pllack_sra.setDisplayMode("Key")
    pllack_sra.setOutputMode("Key")
    for value in pllack_sra_vg_node.getChildren():
        pllack_sra.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_sra.setDefaultValue(0)

    # PLLA Internal Filter Capaticance Value (SCA)
    pllack_sca_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="SCA"]')
    pllack_sca_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllack_sca_node.getAttribute("values")+'"]')
    pllack_sca = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_SCA", pllack_menu)
    pllack_sca.setLabel(pllack_sca_node.getAttribute("name"))
    pllack_sca.setDescription(pllack_sca_node.getAttribute("caption"))
    pllack_sca.setDisplayMode("Key")
    pllack_sca.setOutputMode("Key")
    for value in pllack_sca_vg_node.getChildren():
        pllack_sca.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_sca.setDefaultValue(0)

    # PLLA Output Current (OUTCUR_PLLA)
    pllack_outcur_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="OUTCUR_PLLA"]')
    pllack_outcur_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllack_outcur_node.getAttribute("values")+'"]')
    pllack_outcur = clk_comp.createKeyValueSetSymbol("CLK_PLLACK_OUTCUR", pllack_menu)
    pllack_outcur.setLabel(pllack_outcur_node.getAttribute("name"))
    pllack_outcur.setDescription(pllack_outcur_node.getAttribute("caption"))
    pllack_outcur.setDisplayMode("Key")
    pllack_outcur.setOutputMode("Key")
    for value in pllack_outcur_vg_node.getChildren():
        pllack_outcur.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllack_outcur.setDefaultValue(0)

    # PLLACK Frequency
    pllack_freq = clk_comp.createIntegerSymbol("CLK_PLLACK_FREQ", pllack_menu)
    pllack_freq.setLabel("PLLACK Frequency (HZ)")
    pllack_freq.setDefaultValue(0)
    pllack_freq.setReadOnly(True)
    pllack_freq.setVisible(False)
    pllack_freq.setDependencies(upd_pllack_freq, ["CLK_PLLACK_DIVA", "CLK_PLLACK_MULA", "CLK_MAINCK_FREQ"])

# PLLB CLOCK MENU
def __pllb_clock_menu(clk_comp, clk_menu):
    pllbck_menu = clk_comp.createMenuSymbol("CLK_PLLBCK_MENU", clk_menu)
    pllbck_menu.setLabel("PLLB Clock (PLLBCK)")
    pllbck_menu.setDescription("PLLB Clock Configuration")

    # Section 2.5 - A 40 MHz to 200 MHz Programmable PLL (input from 8 MHz to 20 MHz)

    # PLLB Front End Divider
    pllbck_divb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLBR"]/bitfield@[name="DIVB"]')
    pllbck_divb = clk_comp.createIntegerSymbol("CLK_PLLBCK_DIVB", pllbck_menu)
    pllbck_divb.setLabel(pllbck_divb_node.getAttribute("name"))
    pllbck_divb.setDescription(pllbck_divb_node.getAttribute("caption"))
    pllbck_divb.setDefaultValue(0)
    pllbck_divb.setMin(0)
    pllbck_divb.setMax(64)

    # PLLB Multiplier
    pllbck_mulb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLBR"]/bitfield@[name="MULB"]')
    pllbck_mulb = clk_comp.createIntegerSymbol("CLK_PLLBCK_MULB", pllbck_menu)
    pllbck_mulb.setLabel(pllbck_mulb_node.getAttribute("name"))
    pllbck_mulb.setDescription(pllbck_mulb_node.getAttribute("caption"))
    pllbck_mulb.setDefaultValue(0)
    pllbck_mulb.setMin(0)
    pllbck_mulb.setMax(56)

    # PLLB Multiplier Max
    pllbck_mmax_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PMMR"]/bitfield@[name="PLLB_MMAX"]')
    pllbck_mmax = clk_comp.createIntegerSymbol("CLK_PLLBCK_MMAX", pllbck_menu)
    pllbck_mmax.setLabel(pllbck_mmax_node.getAttribute("name"))
    pllbck_mmax.setDescription(pllbck_mmax_node.getAttribute("caption"))
    pllbck_mmax.setDefaultValue(2047)
    pllbck_mmax.setMin(0)
    pllbck_mmax.setMax(2047)

    # PLLB count of MD_SLCK cycles before LOCKB set
    pllbck_cntb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLBR"]/bitfield@[name="PLLBCOUNT"]')
    pllbck_cntb = clk_comp.createIntegerSymbol("CLK_PLLBCK_PLLBCOUNT", pllbck_menu)
    pllbck_cntb.setLabel(pllbck_cntb_node.getAttribute("name"))
    pllbck_cntb.setDescription(pllbck_cntb_node.getAttribute("caption"))
    pllbck_cntb.setDefaultValue(63)
    pllbck_cntb.setMin(0)
    pllbck_cntb.setMax(63)

    # PLLB Frequency Range
    pllbck_vco_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLBR"]/bitfield@[name="FREQ_VCO"]')
    pllbck_vco_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllbck_vco_node.getAttribute("values")+'"]')
    pllbck_vco = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_FREQ_VCO", pllbck_menu)
    pllbck_vco.setLabel(pllbck_vco_node.getAttribute("name"))
    pllbck_vco.setDescription(pllbck_vco_node.getAttribute("caption"))
    pllbck_vco.setDisplayMode("Key")
    pllbck_vco.setOutputMode("Key")
    for value in pllbck_vco_vg_node.getChildren():
        pllbck_vco.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_vco.setDefaultValue(0)

    # PLLB Clock Source
    pllbck_srcb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_PLLBR"]/bitfield@[name="SRCB"]')
    pllbck_srcb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllbck_srcb_node.getAttribute("values")+'"]')
    pllbck_srcb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SRCB", pllbck_menu)
    pllbck_srcb.setLabel(pllbck_srcb_node.getAttribute("name"))
    pllbck_srcb.setDescription(pllbck_srcb_node.getAttribute("caption"))
    pllbck_srcb.setDisplayMode("Key")
    pllbck_srcb.setOutputMode("Key")
    for value in pllbck_srcb_vg_node.getChildren():
        pllbck_srcb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_srcb.setDefaultValue(0)

    # PLLB Internal Filter Resistor Value (SRB)
    pllbck_srb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="SRB"]')
    pllbck_srb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllbck_srb_node.getAttribute("values")+'"]')
    pllbck_srb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SRB", pllbck_menu)
    pllbck_srb.setLabel(pllbck_srb_node.getAttribute("name"))
    pllbck_srb.setDescription(pllbck_srb_node.getAttribute("caption"))
    pllbck_srb.setDisplayMode("Key")
    pllbck_srb.setOutputMode("Key")
    for value in pllbck_srb_vg_node.getChildren():
        pllbck_srb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_srb.setDefaultValue(0)

    # PLLB Internal Filter Capaticance Value (SCB)
    pllbck_scb_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="SCB"]')
    pllbck_scb_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllbck_scb_node.getAttribute("values")+'"]')
    pllbck_scb = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_SCB", pllbck_menu)
    pllbck_scb.setLabel(pllbck_scb_node.getAttribute("name"))
    pllbck_scb.setDescription(pllbck_scb_node.getAttribute("caption"))
    pllbck_scb.setDisplayMode("Key")
    pllbck_scb.setOutputMode("Key")
    for value in pllbck_scb_vg_node.getChildren():
        pllbck_scb.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_scb.setDefaultValue(0)

    # PLLB Output Current (OUTCUR_PLLB)
    pllbck_outcur_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CFG"]/bitfield@[name="OUTCUR_PLLB"]')
    pllbck_outcur_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pllbck_outcur_node.getAttribute("values")+'"]')
    pllbck_outcur = clk_comp.createKeyValueSetSymbol("CLK_PLLBCK_OUTCUR", pllbck_menu)
    pllbck_outcur.setLabel(pllbck_outcur_node.getAttribute("name"))
    pllbck_outcur.setDescription(pllbck_outcur_node.getAttribute("caption"))
    pllbck_outcur.setDisplayMode("Key")
    pllbck_outcur.setOutputMode("Key")
    for value in pllbck_outcur_vg_node.getChildren():
        pllbck_outcur.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    pllbck_outcur.setDefaultValue(0)

    # PLLBCK Frequency
    pllbck_freq = clk_comp.createIntegerSymbol("CLK_PLLBCK_FREQ", pllbck_menu)
    pllbck_freq.setLabel("PLLBCK Frequency (HZ)")
    pllbck_freq.setDefaultValue(0)
    pllbck_freq.setReadOnly(True)
    pllbck_freq.setVisible(False)
    pllbck_freq.setDependencies(upd_pllbck_freq, ["CLK_PLLBCK_DIVB", "CLK_PLLBCK_MULB", "CLK_MAINCK_FREQ", "CLK_RC2CK_FREQ", "CLK_PLLBCK_SRCB"])

# MASTER CLOCK MENU
def __mast_clock_menu(clk_comp, clk_menu):
    mck_menu = clk_comp.createMenuSymbol("CLK_MCK_MENU", clk_menu)
    mck_menu.setLabel("Master Clock (MCK)")
    mck_menu.setDescription("Master Clock Configuration")

    # Master Clock Source
    mck_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_MCKR"]/bitfield@[name="CSS"]')
    mck_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mck_css_node.getAttribute("values")+'"]')
    mck_css = clk_comp.createKeyValueSetSymbol("CLK_MCK_CSS", mck_menu)
    mck_css.setLabel(mck_css_node.getAttribute("name"))
    mck_css.setDescription(mck_css_node.getAttribute("caption"))
    mck_css.setDisplayMode("Key")
    mck_css.setOutputMode("Key")
    for value in mck_css_vg_node.getChildren():
        mck_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_css.setDefaultValue(1)

    # Master Clock Prescaler
    mck_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_MCKR"]/bitfield@[name="PRES"]')
    mck_pres_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mck_pres_node.getAttribute("values")+'"]')
    mck_pres = clk_comp.createKeyValueSetSymbol("CLK_MCK_PRES", mck_menu)
    mck_pres.setLabel(mck_pres_node.getAttribute("name"))
    mck_pres.setDescription(mck_pres_node.getAttribute("caption"))
    mck_pres.setDisplayMode("Key")
    mck_pres.setOutputMode("Key")
    for value in mck_pres_vg_node.getChildren():
        mck_pres.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_pres.setDefaultValue(0)

    # Master Clock Divider
    mck_mdiv_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_MCKR"]/bitfield@[name="MDIV"]')
    mck_mdiv_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mck_mdiv_node.getAttribute("values")+'"]')
    mck_mdiv = clk_comp.createKeyValueSetSymbol("CLK_MCK_MDIV", mck_menu)
    mck_mdiv.setLabel(mck_mdiv_node.getAttribute("name"))
    mck_mdiv.setDescription(mck_mdiv_node.getAttribute("caption"))
    mck_mdiv.setDisplayMode("Key")
    mck_mdiv.setOutputMode("Key")
    for value in mck_mdiv_vg_node.getChildren():
        mck_mdiv.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    mck_mdiv.setDefaultValue(0)

    # Processor Free Running Clock Frequency
    fclk_freq = clk_comp.createIntegerSymbol("CPU_CLOCK_FREQUENCY", mck_menu)
    fclk_freq.setLabel("FCLK Frequency (HZ)")
    fclk_freq.setDefaultValue(Database.getSymbolValue("core", "CLK_MAINCK_FREQ"))
    fclk_freq.setReadOnly(True)
    fclk_freq.setVisible(False)
    fclk_freq.setDependencies(upd_fclk_freq, ["CLK_MCK_CSS", "CLK_MCK_PRES", "CLK_MAINCK_FREQ", "CLK_MD_SLCK_FREQ", "CLK_PLLACK_FREQ"])

    # SysTick Clock Frequency
    tick_freq = clk_comp.createIntegerSymbol("SYSTICK_CLOCK_FREQUENCY", mck_menu)
    tick_freq.setLabel("SysTick Frequency (HZ)")
    tick_freq.setDefaultValue(fclk_freq.getValue() / 8)
    tick_freq.setReadOnly(True)
    tick_freq.setVisible(False)
    tick_freq.setDependencies(upd_tick_freq, ["CPU_CLOCK_FREQUENCY"])

    # Master Clock Frequency
    mck_freq = clk_comp.createIntegerSymbol("CLK_MCK_FREQ", mck_menu)
    mck_freq.setLabel("MCK Frequency (HZ)")
    mck_freq.setDefaultValue(Database.getSymbolValue("core", "CLK_MAINCK_FREQ"))
    mck_freq.setReadOnly(True)
    mck_freq.setVisible(False)
    mck_freq.setDependencies(upd_mck_freq, ["CLK_MCK_CSS", "CLK_MCK_PRES", "CLK_MCK_MDIV", "CLK_MAINCK_FREQ", "CLK_MD_SLCK_FREQ", "CLK_PLLACK_FREQ"])

    # WARNING! Selected clock source not enabled.
    mck_warn_not_en = clk_comp.createCommentSymbol("CLK_MCK_WARN_NOT_EN", mck_menu)
    mck_warn_not_en.setLabel("WARNING! Selected clock source not enabled.")
    mck_warn_not_en.setVisible(False)
    mck_warn_not_en.setDependencies(warn_event_value_0, ["CLK_MCK_FREQ"])

# PROGRAMMABLE CLOCK MENU
def __prog_clock_menu(clk_comp, clk_menu):
    pck_menu = clk_comp.createMenuSymbol("CLK_PCK_MENU", clk_menu)
    pck_menu.setLabel("Programmable Clocks (PCK)")
    pck_menu.setDescription("Programmable Clocks")
    
    num_pcks = int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]').getAttribute("count"))
    for pckx in range(0, num_pcks):
        pckx_en = clk_comp.createBooleanSymbol("CLK_PCK"+str(pckx)+"_EN", pck_menu)
        pckx_en.setLabel("Enable PCK"+str(pckx))
    
        pckx_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="CSS"]')
        pckx_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pckx_css_node.getAttribute("values")+'"]')
        pckx_css = clk_comp.createKeyValueSetSymbol("CLK_PCK"+str(pckx)+"_CSS", pckx_en)
        pckx_css.setLabel(pckx_css_node.getAttribute("name"))
        pckx_css.setDescription(pckx_css_node.getAttribute("caption"))
        pckx_css.setDisplayMode("Key")
        pckx_css.setOutputMode("Key")
        for value in pckx_css_vg_node.getChildren():
            pckx_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    
        pckx_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="PRES"]')
        pckx_pres = clk_comp.createIntegerSymbol("CLK_PCK"+str(pckx)+"_PRES", pckx_en)
        pckx_pres.setLabel(pckx_pres_node.getAttribute("name"))
        pckx_pres.setDescription(pckx_pres_node.getAttribute("caption"))
        pckx_pres.setMin(0)
        pckx_pres.setMax(255)
    
        pckx_freq = clk_comp.createIntegerSymbol("CLK_PCK"+str(pckx)+"_FREQ", pckx_en)
        pckx_freq.setLabel("PCK"+str(pckx)+" Frequency (HZ)")
        pckx_freq.setDefaultValue(0)
        pckx_freq.setReadOnly(True)
        pckx_freq.setVisible(False)
        pckx_freq.setDependencies(upd_pck_freq, ["CLK_PCK"+str(pckx)+"_EN", "CLK_PCK"+str(pckx)+"_CSS", "CLK_PCK"+str(pckx)+"_PRES",
                "CLK_MAINCK_FREQ", "CLK_MD_SLCK_FREQ", "CLK_PLLACK_FREQ", "CLK_PLLBCK_FREQ", "CLK_MCK_FREQ"])
    
        # WARNING! Selected clock source not enabled.
        pckx_warn_not_en = clk_comp.createCommentSymbol("CLK_PCK"+str(pckx)+"_WARN_NOT_EN", pckx_en)
        pckx_warn_not_en.setLabel("WARNING! Selected clock source not enabled.")
        pckx_warn_not_en.setVisible(False)
        #pckx_warn_not_en.setDependencies(warn_pckx_src_not_en, ["CLK_PCK"+str(pckx)+"_EN", "CLK_PCK"+str(pckx)+"_FREQ"])
        pckx_warn_not_en.setDependencies(warn_event_value_0, ["CLK_PCK"+str(pckx)+"_FREQ"])

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

# Calculated Clock Frequencies MENU
def __calc_clock_menu(clk_comp, clk_menu):
    calc_freq_menu = clk_comp.createMenuSymbol("CLK_FREQ_MENU", clk_menu)
    calc_freq_menu.setLabel("Calculated Clock Frequencies")

    # TD_SLCK Frequency Display
    calc_slck_td_freq = clk_comp.createIntegerSymbol("CALC_TD_SLCK_FREQ", calc_freq_menu)
    calc_slck_td_freq.setLabel("TD_SLCK Frequency (HZ)")
    calc_slck_td_freq.setDefaultValue(SLCK_RC_FREQ)
    calc_slck_td_freq.setReadOnly(True)
    calc_slck_td_freq.setVisible(True)
    calc_slck_td_freq.setDependencies(upd_clone, ["CLK_TD_SLCK_FREQ"])

    # MD_SLCK Frequency Display
    calc_slck_md_freq = clk_comp.createIntegerSymbol("CALC_MD_SLCK_FREQ", calc_freq_menu)
    calc_slck_md_freq.setLabel("MD_SLCK Frequency (HZ)")
    calc_slck_md_freq.setDefaultValue(SLCK_RC_FREQ)
    calc_slck_md_freq.setReadOnly(True)
    calc_slck_md_freq.setVisible(True)
    calc_slck_md_freq.setDependencies(upd_clone, ["CLK_MD_SLCK_FREQ"])

    # MAINCK Frequency Display
    calc_mainck_freq = clk_comp.createIntegerSymbol("CALC_MAINCK_FREQ", calc_freq_menu)
    calc_mainck_freq.setLabel("MAINCK Frequency (HZ)")
    mainck_rc_freq = calc_mainck_freq.getComponent().getSymbolByID("CLK_MAINCK_MOSCRCF")
    calc_mainck_freq.setDefaultValue(int(mainck_rc_freq.getKey(mainck_rc_freq.getValue()).split("_")[1]) * 1000000)
    calc_mainck_freq.setReadOnly(True)
    calc_mainck_freq.setVisible(True)
    calc_mainck_freq.setDependencies(upd_clone, ["CLK_MAINCK_FREQ"])

    # RC2CK Frequency Display
    calc_rc2ck_freq = clk_comp.createIntegerSymbol("CALC_RC2CK_FREQ", calc_freq_menu)
    calc_rc2ck_freq.setLabel("RC2CK Frequency (HZ)")
    rc2ck_sel_freq = calc_rc2ck_freq.getComponent().getSymbolByID("CLK_RC2CK_OSCRCF")
    calc_rc2ck_freq.setDefaultValue(int(rc2ck_sel_freq.getKey(rc2ck_sel_freq.getValue()).split("_")[1]) * 1000000)
    calc_rc2ck_freq.setReadOnly(True)
    calc_rc2ck_freq.setVisible(True)
    calc_rc2ck_freq.setDependencies(upd_clone_dsp, ["CLK_RC2CK_FREQ"])

    # PLLACK Frequency Display
    calc_pllack_freq = clk_comp.createIntegerSymbol("CALC_PLLACK_FREQ", calc_freq_menu)
    calc_pllack_freq.setLabel("PLLACK Frequency (HZ)")
    calc_pllack_freq.setDefaultValue(0)
    calc_pllack_freq.setReadOnly(True)
    calc_pllack_freq.setVisible(False)
    calc_pllack_freq.setDependencies(upd_clone_dsp, ["CLK_PLLACK_FREQ"])

    # PLLBCK Frequency Display
    calc_pllbck_freq = clk_comp.createIntegerSymbol("CALC_PLLBCK_FREQ", calc_freq_menu)
    calc_pllbck_freq.setLabel("PLLBCK Frequency (HZ)")
    calc_pllbck_freq.setDefaultValue(0)
    calc_pllbck_freq.setReadOnly(True)
    calc_pllbck_freq.setVisible(False)
    calc_pllbck_freq.setDependencies(upd_clone_dsp, ["CLK_PLLBCK_FREQ"])

    # MCK Frequency Display
    calc_mck_freq = clk_comp.createIntegerSymbol("CALC_MCK_FREQ", calc_freq_menu)
    calc_mck_freq.setLabel("MCK Frequency (HZ)")
    calc_mck_freq.setDefaultValue(Database.getSymbolValue("core", "CLK_MCK_FREQ"))
    calc_mck_freq.setReadOnly(True)
    calc_mck_freq.setVisible(True)
    calc_mck_freq.setDependencies(upd_clone, ["CLK_MCK_FREQ"])

    # FCLK Frequency Display
    calc_fclk_freq = clk_comp.createIntegerSymbol("CALC_FCLK_FREQ", calc_freq_menu)
    calc_fclk_freq.setLabel("CPU Frequency (HZ)")
    calc_fclk_freq.setDefaultValue(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    calc_fclk_freq.setReadOnly(True)
    calc_fclk_freq.setVisible(True)
    calc_fclk_freq.setDependencies(upd_clone, ["CPU_CLOCK_FREQUENCY"])

    # SysTick Frequency Display
    calc_tick_freq = clk_comp.createIntegerSymbol("CALC_TICK_FREQ", calc_freq_menu)
    calc_tick_freq.setLabel("SysTick Frequency (HZ)")
    calc_tick_freq.setDefaultValue(Database.getSymbolValue("core", "SYSTICK_CLOCK_FREQUENCY"))
    calc_tick_freq.setReadOnly(True)
    calc_tick_freq.setVisible(True)
    calc_tick_freq.setDependencies(upd_clone, ["SYSTICK_CLOCK_FREQUENCY"])

    num_pcks = int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]').getAttribute("count"))
    for pckx in range(0, num_pcks):
        calc_pckx_freq = clk_comp.createIntegerSymbol("CALC_PCK"+str(pckx)+"_FREQ", calc_freq_menu)
        calc_pckx_freq.setLabel("PCK"+str(pckx)+" Frequency (HZ)")
        calc_pckx_freq.setDefaultValue(0)
        calc_pckx_freq.setReadOnly(True)
        calc_pckx_freq.setVisible(False)
        calc_pckx_freq.setDependencies(upd_clone_dsp, ["CLK_PCK"+str(pckx)+"_FREQ"])

if __name__ == "__main__":
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
    __calc_clock_menu(coreComponent, clk_menu)

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


