def update_td_slck(symbol, event):
    byp = event['source'].getSymbolByID("CLK_OSC32BYP")
    byp_freq = event['source'].getSymbolByID("CLK_OSC32BYP_FREQ")
    osel = event['source'].getSymbolByID("CLK_TD_OSCSEL")
    value = 0
    if byp.getValue() == True:
        value = byp_freq.getValue()
    else:
        if osel.getValue() == 0:
            value = 32000
        else:
            value = 32768
    symbol.setValue(value,0)

def update_mainck(symbol, event):
    oscsel = event['source'].getSymbolByID("CLK_MOSCSEL")
    xtfreq = event['source'].getSymbolByID("CLK_MOSCXT_FREQ")
    rcen = event['source'].getSymbolByID("CLK_MOSCRCEN")
    xten = event['source'].getSymbolByID("CLK_MOSCXTEN")

    value = 0
    if oscsel.getValue() == 0:
        if rcen.getValue() == True:
            value = 12000000
        else:
            value = 0
    else:
        if xten.getValue() == True:
            value = xtfreq.getValue()
        else:
            value = 0
    symbol.setValue(value, 0)

def update_xtal_warning(symbol, event):
    oscsel = event['source'].getSymbolByID("CLK_TD_OSCSEL")
    xten  = event['source'].getSymbolByID("CLK_OSC32EN")
    symbol.setVisible(oscsel.getValue()==1 and xten.getValue()==False)

def update_bypass_warning(symbol, event):
    xten  = event['source'].getSymbolByID("CLK_OSC32EN")
    byen  = event['source'].getSymbolByID("CLK_OSC32BYP")
    symbol.setVisible(xten.getValue()==True and byen.getValue()==True)

def update_pll_freq(symbol, event):
    mainckf = event['source'].getSymbolValue("MAINCK_FREQUENCY")
    mul = event['source'].getSymbolValue("CLK_PLL_MUL")
    fracr = event['source'].getSymbolValue("CLK_PLL_FRACR")
    divpmc = event['source'].getSymbolValue("CLK_PLL_DIVPMC")
    enable = event['source'].getSymbolValue("CLK_PLL_EN")
    if enable is True:
        pllcore_clk = (mainckf * (mul + 1 + (float(fracr)/pow(2, 22))))
        symbol.setValue(int(pllcore_clk / (divpmc + 1)), 0)
    else:
        symbol.setValue(0, 0)

def update_upll_freq(symbol, event):
    mainckf = event['source'].getSymbolValue("CLK_MOSCXT_FREQ")
    mul = event['source'].getSymbolValue("CLK_UPLL_MUL")
    fracr = event['source'].getSymbolValue("CLK_UPLL_FRACR")
    enable = event['source'].getSymbolValue("CLK_UPLL_EN")
    if enable is True:
        pllcore_clk = (mainckf * (mul + 1 + (float(fracr) / pow(2, 22))))
        symbol.setValue(int(pllcore_clk / 2), 0)
    else:
        symbol.setValue(0, 0)

def update_cpu_clk_freq(symbol, event):
    md_slck = event['source'].getSymbolByID("MD_SLOW_CLK_FREQUENCY")
    mainck = event['source'].getSymbolByID("MAINCK_FREQUENCY")
    pllack = event['source'].getSymbolByID("PLLA_FREQUENCY")
    upllck = event['source'].getSymbolByID("UPLL_FREQUENCY")
    cpu_css = event['source'].getSymbolByID("CLK_CPU_CKR_CSS")
    cpu_pres = event['source'].getSymbolByID("CLK_CPU_CKR_PRES")
    input_freq = 0
    if cpu_css.getValue() == 0:
        input_freq = md_slck.getValue()
    elif cpu_css.getValue() == 1:
        input_freq = mainck.getValue()
    elif cpu_css.getValue() == 2:
        input_freq = pllack.getValue()
    elif cpu_css.getValue() == 3:
        input_freq = upllck.getValue()
    pres = 0
    if cpu_pres.getValue() != 7:
        pres = pow(2,cpu_pres.getValue())
    else:
        pres = 3
    symbol.setValue(input_freq / pres, 0)

def update_mck_freq(symbol, event):
    cpu_clk = event['source'].getSymbolByID("CPU_CLOCK_FREQUENCY")
    cpu_mdiv = event['source'].getSymbolByID("CLK_CPU_CKR_MDIV")
    input_freq = cpu_clk.getValue()
    div = 0
    if cpu_mdiv.getValue() != 3:
        div = pow(2,cpu_mdiv.getValue())
    else:
        div = 3
    symbol.setValue(input_freq / div, 0)

def update_pck_freq(symbol, event):
    index = int(symbol.getID().split("PCK")[1].split("_")[0])
    pckx_pres = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_PRES")
    pckx_css = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_CSS")
    enabled = event['source'].getSymbolValue("CLK_PCK"+str(index)+"_EN")
    input_freq = 0
    if enabled == True:
        input_freq = event['source'].getSymbolValue(pckx_css.getKey(pckx_css.getValue())+"_FREQUENCY")
    symbol.setValue(input_freq / (pckx_pres.getValue() + 1), 0)

def update_usb_freq(symbol, event):
    pllack = event['source'].getSymbolByID("PLLA_FREQUENCY")
    upllck = event['source'].getSymbolByID("UPLL_FREQUENCY")
    moscxt_freq = event['source'].getSymbolByID("CLK_MOSCXT_FREQ")
    usbs = event['source'].getSymbolByID("CLK_USB_USBS")
    usbdiv = event['source'].getSymbolByID("CLK_USB_USBDIV")
    enable = event['source'].getSymbolByID("CLK_USB_EN")
    input_freq = 0
    if enable.getValue() == True:
        if usbs.getValue() == 0:
            input_freq = pllack.getValue()
        if usbs.getValue() == 1:
            input_freq = upllck.getValue()
        if usbs.getValue() >=2:
            input_freq = moscxt_freq.getValue()
    symbol.setValue( input_freq / (usbdiv.getValue() + 1), 0)

def update_usb_warning(symbol, event):
    symbol.setVisible((event['source'].getSymbolValue("CLK_UHP48M") != 48000000) and (event['source'].getSymbolValue("CLK_USB_EN") == True))

def update_gclk_freq(symbol, event):
    instance_name = symbol.getID().split("_")[0]
    gclk_css = event['source'].getSymbolByID("CLK_"+instance_name+"_GCLKCSS")
    gclk_div = event['source'].getSymbolByID("CLK_"+instance_name+"_GCLKDIV")
    input_freq = event['source'].getSymbolValue(gclk_css.getKey(gclk_css.getValue())+"_FREQUENCY")
    enabled = event['source'].getSymbolValue("CLK_"+instance_name+"_GCLKEN")
    if enabled == True:
        symbol.setValue(input_freq / (gclk_div.getValue() + 1), 0)
    else:
        symbol.setValue(0, 0)

def update_tc_enable(symbol, event):
    instance_num = symbol.getID()[2]
    enable_clock = False
    for channel in range(3):
        symbol_id = "TC" + str(instance_num) + "_CHANNEL" + str(channel) + "_CLOCK_ENABLE"
        if (Database.getSymbolValue("core", symbol_id) == True):
            enable_clock = True
            break
    symbol.setValue(enable_clock, 2)

def update_tc_freq(symbol, event):
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
            clk_frequency = Database.getSymbolValue("core", "TC" + str(instance_num) + "_GCLK_FREQUENCY")
        # if clock  source is MCK/8
        elif (clk_src == 2):
            clk_frequency = Database.getSymbolValue("core", "MCK_FREQUENCY") / 8
        # if clock  source is MCK/32
        elif (clk_src == 3):
            clk_frequency = Database.getSymbolValue("core", "MCK_FREQUENCY") / 32
        # if clock  source is MCK/128
        elif (clk_src == 4):
            clk_frequency = Database.getSymbolValue("core", "MCK_FREQUENCY") / 128
        # if clock  source is SLOW CLOCK
        elif (clk_src == 5):
            clk_frequency = Database.getSymbolValue("core", "MD_SLOW_CLK_FREQUENCY")
        # default  clock source is MCK (Enabled through extended registers of TC)
        else:
            clk_frequency = Database.getSymbolValue("core", "MCK_FREQUENCY")
        symbol.setValue(clk_frequency, 2)

def update_flexcomm_clock_frequency(symbol, event):
    frequency = -1
    instance_name = symbol.getID().split("_")[0]
    mck = event['source'].getSymbolByID("MCK_FREQUENCY")
    gclk = event['source'].getSymbolByID(instance_name + "_GCLK_FREQUENCY")
    op_mode = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_MODE")
    # Flexcom is operating as USART
    if op_mode == 1 :
        # Get the USART mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_USART_MR_USCLKS")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = mck.getValue()
        # Source clock is bus clock / 8
        elif source_clock == 1:
            frequency = mck.getValue() / 8
        # Source clock is GCLK
        elif source_clock == 2:
            frequency = gclk.getValue()
        # Source clock is external, set the internal frequency to zero
        else:
            frequency = 0
    #Flexcom is operating in SPI mode
    elif op_mode == 2:
        #Get the SPI mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_SPI_MR_BRSRCCLK")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = mck.getValue()
        # Source clock is GCLK
        elif source_clock == 1:
            frequency = gclk.getValue()
    #Flexcom is operating in TWI mode
    elif op_mode == 3:
        #Get the SPI mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_TWI_CWGR_BRSRCCLK")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = mck.getValue()
        # Source clock is GCLK
        elif source_clock == 1:
            frequency = gclk.getValue()

    # Update the frequency only if the clock selections are valid
    if frequency >= 0:
        symbol.setValue(frequency, 0)


def update_sdmmc_clock_frequency(symbol, event):
    sdmmc_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]

    # set the HCLOCK frequency
    mck_clk_freq = event['source'].getSymbolValue("MCK_FREQUENCY")
    symbol.setValue(mck_clk_freq, 0)

    # set the base clock frequency
    gclk_clk_freq = event['source'].getSymbolValue(sdmmc_name + "_GCLK_FREQUENCY")
    base_clk_sym = event['source'].getSymbolByID(sdmmc_name + "_BASECLK_FREQUENCY")
    base_clk_sym.setValue(gclk_clk_freq / 2)

    # set the multiplier clock frequency
    mult_clk_sym = event['source'].getSymbolByID(sdmmc_name + "_MULTCLK_FREQUENCY")
    mult_clk_sym.setValue(gclk_clk_freq)
#This maps the instance name to the symbol in that instance that determines if we use the peripheral clock or the generic clock.  For the
#generic handler we assume it is a keyvalueset and 0 maps to the peripheral clock.  Peripherals that don't match this assumption will need
#to use their own update function and map it in gclk_update_map
global gclk_dependency_map
gclk_dependency_map = {
    "ADC" : "ADC_CLK_SRC",
    "LCDC" : "SOME_SYMBOL",
    "I2SMCC" : "SOME_SYMBOL",
    "PIT64B" : "SGCLK",
    "CLASSD" : "SOME_SYMBOL",
    "DBGU" : "DBGU_CLK_SRC"
}

def generic_gclk_update_freq(symbol, event):
    global gclk_dependency_map
    instance_name = symbol.getID().split("_")[0]

    mck = event['source'].getSymbolByID("MCK_FREQUENCY")
    gclk = event['source'].getSymbolByID(instance_name + "_GCLK_FREQUENCY")

    periph_css = Database.getSymbolValue(instance_name.lower(), gclk_dependency_map[instance_name])

    if periph_css == None or periph_css == 0:
        symbol.setValue(mck.getValue(), 0)
    else:
        symbol.setValue(gclk.getValue(), 0)

#map of gclk capable peripherals to their update functions
gclk_update_map = {
    "FLEXCOM" : update_flexcomm_clock_frequency,
    "ADC" : generic_gclk_update_freq,
    "LCDC" : generic_gclk_update_freq,
    "I2SMCC" : generic_gclk_update_freq,
    "PIT64B" : generic_gclk_update_freq,
    "CLASSD" : generic_gclk_update_freq,
    "DBGU" : generic_gclk_update_freq
}

#instantiateComponent of core Component
menu = coreComponent.createMenuSymbol("CLK_MENU", None)
menu.setLabel("Clock (PMC)")
menu.setDescription("Clock configuration")

#slow clock
sckc_menu = coreComponent.createMenuSymbol("CLK_SCKC_MENU", menu)
sckc_menu.setLabel("Slow Clock (SCKC)")
sckc_menu.setDescription("Slow Clock Controller (SCKC)")

td_oscel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/register-group@[name="SCKC"]/register@[name="SCKC_CR"]/bitfield@[name="TD_OSCSEL"]')
td_oscel_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/value-group@[name="'+td_oscel_node.getAttribute("values")+'"]')
td_oscel = coreComponent.createKeyValueSetSymbol("CLK_TD_OSCSEL", sckc_menu)
td_oscel.setLabel(td_oscel_node.getAttribute("name"))
td_oscel.setDescription(td_oscel_node.getAttribute("caption"))
td_oscel.setDisplayMode("Key")
td_oscel.setOutputMode("Key")
for value in td_oscel_vg_node.getChildren():
    td_oscel.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
td_oscel.setDefaultValue(1)

osc32en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/register-group@[name="SCKC"]/register@[name="SCKC_CR"]/bitfield@[name="OSC32EN"]')
osc32en = coreComponent.createBooleanSymbol("CLK_OSC32EN", sckc_menu)
osc32en.setLabel(osc32en_node.getAttribute("name"))
osc32en.setDescription(osc32en_node.getAttribute("caption"))
osc32en.setDefaultValue(True)

xtal_warning = coreComponent.createCommentSymbol("CLK_XTAL_WARNING", sckc_menu)
xtal_warning.setLabel("WARNING! Crystal selected but not enabled.")
xtal_warning.setVisible(td_oscel.getValue()==1 and osc32en.getValue()==False)
xtal_warning.setDependencies(update_xtal_warning, ['CLK_OSC32EN', 'CLK_TD_OSCSEL'])

osc32byp_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/register-group@[name="SCKC"]/register@[name="SCKC_CR"]/bitfield@[name="OSC32BYP"]')
osc32byp = coreComponent.createBooleanSymbol("CLK_OSC32BYP", sckc_menu)
osc32byp.setLabel(osc32byp_node.getAttribute("name"))
osc32byp.setDescription(osc32byp_node.getAttribute("caption"))

bypass_warning = coreComponent.createCommentSymbol("CLK_BYPASS_WARNING", sckc_menu)
bypass_warning.setLabel("WARNING! Bypass cannot be enabled when the crystal is enabled.")
bypass_warning.setVisible(osc32en.getValue()==True and osc32byp.getValue()==True)
bypass_warning.setDependencies(update_bypass_warning, ['CLK_OSC32EN', 'CLK_OSC32BYP'])

osc32byp_freq = coreComponent.createIntegerSymbol("CLK_OSC32BYP_FREQ", osc32byp)
osc32byp_freq.setLabel("External SLCK Freq")
osc32byp_freq.setDescription("Frequency(Hz) of the clock connected to XIN32")
osc32byp_freq.setMin(512)
osc32byp_freq.setMax(50000)

td_slck = coreComponent.createIntegerSymbol("TD_SLOW_CLOCK_FREQUENCY", None)
td_slck.setVisible(False)
value = 0
if osc32byp.getValue() == True and td_oscel.getValue() == 1:
    value = osc32byp_freq.getValue()
else:
    if td_oscel.getValue() == 0:
        value = 32000
    else:
        value = 32768
td_slck.setDefaultValue(value)
td_slck.setDependencies(update_td_slck, ['CLK_TD_OSCSEL', 'CLK_OSC32BYP', 'CLK_OSC32BYP_FREQ'])

md_slck = coreComponent.createIntegerSymbol("MD_SLOW_CLK_FREQUENCY", None)
md_slck.setVisible(False)
md_slck.setDefaultValue(32000)

#main clock
mainck_menu = coreComponent.createMenuSymbol("CLK_MAINCK_MENU", menu)
mainck_menu.setLabel("Main Clock (MAINCK)")

moscrcen_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCRCEN"]')
moscrcen = coreComponent.createBooleanSymbol("CLK_MOSCRCEN", mainck_menu)
moscrcen.setLabel(moscrcen_node.getAttribute("name"))
moscrcen.setDescription(moscrcen_node.getAttribute("caption"))

moscxten_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTEN"]')
moscxten = coreComponent.createBooleanSymbol("CLK_MOSCXTEN", mainck_menu)
moscxten.setLabel(moscxten_node.getAttribute("name"))
moscxten.setDescription(moscxten_node.getAttribute("caption"))
moscxten.setDefaultValue(True)

moscxtst_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTST"]')
moscxtst = coreComponent.createIntegerSymbol("CLK_MOSCXTST", mainck_menu)
moscxtst.setLabel(moscxtst_node.getAttribute("name"))
moscxtst.setDescription(moscxtst_node.getAttribute("caption"))
moscxtst.setDefaultValue(255)
moscxtst.setMin(0)
moscxtst.setMax(255)
moscxtst.setDefaultValue(18)

moscxt_freq = coreComponent.createIntegerSymbol("CLK_MOSCXT_FREQ", mainck_menu)
moscxt_freq.setLabel("Main Crystal Oscillator Freq(Hz)")
moscxt_freq.setMin(12000000)
moscxt_freq.setMax(48000000)
moscxt_freq.setDefaultValue(24000000)

moscsel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCSEL"]')
moscsel_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+moscsel_node.getAttribute("values")+'"]')
moscsel = coreComponent.createKeyValueSetSymbol("CLK_MOSCSEL", mainck_menu)
moscsel.setLabel(moscsel_node.getAttribute("name"))
moscsel.setDescription(moscsel_node.getAttribute("caption"))
moscsel.setDisplayMode("Key")
moscsel.setOutputMode("Value")
for value in moscsel_vg_node.getChildren():
    moscsel.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
moscsel.setDefaultValue(1)

mainck = coreComponent.createIntegerSymbol("MAINCK_FREQUENCY", None)
mainck.setVisible(False)
mainck.setDependencies(update_mainck, ['CLK_MOSCRCEN', 'CLK_MOSCXTEN', 'CLK_MOSCSEL', 'CLK_MOSCXT_FREQ'])
value = 0
if moscsel.getValue() == 0:
    if moscrcen.getValue() == True:
        value = 12000000
    else:
        value = 0
else:
    if moscxten.getValue() == True:
        value = moscxt_freq.getValue()
    else:
        value = 0;
mainck.setDefaultValue(value)

#pll
pll_menu = coreComponent.createMenuSymbol("CLK_PLL_MENU", menu)
pll_menu.setLabel("PLLA")

pll_en = coreComponent.createBooleanSymbol("CLK_PLL_EN", pll_menu)
pll_en.setLabel("Enable PLLA")
pll_en.setDefaultValue(True)

pll_mul_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="MUL"]')
pll_mul = coreComponent.createIntegerSymbol("CLK_PLL_MUL", pll_en)
pll_mul.setLabel(pll_mul_node.getAttribute("name"))
pll_mul.setDescription(pll_mul_node.getAttribute("caption"))
pll_mul.setMin(0)
pll_mul.setMax(127)
pll_mul.setDefaultValue(49)

pll_fracr_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="FRACR"]')
pll_fracr = coreComponent.createIntegerSymbol("CLK_PLL_FRACR", pll_en)
pll_fracr.setLabel(pll_fracr_node.getAttribute("name"))
pll_fracr.setDescription(pll_fracr_node.getAttribute("caption"))
pll_fracr.setMin(0)
pll_fracr.setMax(4194303)

pll_divpmc_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL0"]/bitfield@[name="DIVPMC"]')
pll_divpmc = coreComponent.createIntegerSymbol("CLK_PLL_DIVPMC", pll_en)
pll_divpmc.setLabel(pll_divpmc_node.getAttribute("name"))
pll_divpmc.setDescription(pll_divpmc_node.getAttribute("caption"))
pll_divpmc.setMin(0)
pll_divpmc.setMax(255)
pll_divpmc.setDefaultValue(1)

pll_ss_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="ENSPREAD"]')
pll_ss_en = coreComponent.createBooleanSymbol("CLK_PLLA_SS", pll_en)
pll_ss_en.setLabel(pll_ss_en_node.getAttribute("name"))
pll_ss_en.setDescription(pll_ss_en_node.getAttribute("caption"))

pll_ss_nstep_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="NSTEP"]')
pll_ss_nstep = coreComponent.createIntegerSymbol("CLK_PLLA_SS_NSTEP", pll_ss_en)
pll_ss_nstep.setLabel(pll_ss_nstep_node.getAttribute("name"))
pll_ss_nstep.setDescription(pll_ss_nstep_node.getAttribute("caption"))
pll_ss_nstep.setMin(0)
pll_ss_nstep.setMax(255)

pll_ss_step_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="STEP"]')
pll_ss_step = coreComponent.createIntegerSymbol("CLK_PLLA_SS_STEP", pll_ss_en)
pll_ss_step.setLabel(pll_ss_step_node.getAttribute("name"))
pll_ss_step.setDescription(pll_ss_step_node.getAttribute("caption"))
pll_ss_step.setMin(0)
pll_ss_step.setMax(65535)

pllack = coreComponent.createIntegerSymbol("PLLA_FREQUENCY", pll_en)
pllack.setVisible(False)
if pll_en.getValue() == True:
    pllack.setDefaultValue(mainck.getValue() * (pll_mul.getValue() + 1 + (pll_fracr.getValue() / pow(2,22))) / (pll_divpmc.getValue() + 1))
else:
    pllack.setDefaultValue(0)
pllack.setDependencies(update_pll_freq, ['CLK_PLL_EN', 'MAINCK_FREQUENCY', 'CLK_PLL_MUL', 'CLK_PLL_FRACR', 'CLK_PLL_DIVPMC'])

#upll
upll_menu = coreComponent.createMenuSymbol("CLK_UPLL_MENU", menu)
upll_menu.setLabel("UPLL")

upll_en = coreComponent.createBooleanSymbol("CLK_UPLL_EN", upll_menu)
upll_en.setLabel("Enable UPLL")

upll_mul_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="MUL"]')
upll_mul = coreComponent.createIntegerSymbol("CLK_UPLL_MUL", upll_en)
upll_mul.setLabel(upll_mul_node.getAttribute("name"))
upll_mul.setDescription(upll_mul_node.getAttribute("caption"))
upll_mul.setMin(0)
upll_mul.setMax(127)

upll_fracr_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="FRACR"]')
upll_fracr = coreComponent.createIntegerSymbol("CLK_UPLL_FRACR", upll_en)
upll_fracr.setLabel(upll_fracr_node.getAttribute("name"))
upll_fracr.setDescription(upll_fracr_node.getAttribute("caption"))
upll_fracr.setMin(0)
upll_fracr.setMax(4194303)

upllck = coreComponent.createIntegerSymbol("UPLL_FREQUENCY", upll_en)
upllck.setVisible(False)
if upll_en.getValue() == True:
    upllck.setDefaultValue(moscxt_freq.getValue() * (upll_mul.getValue() + 1 + (upll_fracr.getValue() / pow(2,22))) / 2)
else:
    upllck.setDefaultValue(0)
upllck.setDependencies(update_upll_freq, ['CLK_UPLL_EN', 'CLK_MOSCXT_FREQ', 'CLK_UPLL_MUL', 'CLK_UPLL_FRACR'])

#Processor Clock
cpu_menu = coreComponent.createMenuSymbol("CLK_CPU_MENU", menu)
cpu_menu.setLabel("Processor Clock")

cpu_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="CSS"]')
cpu_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_css_node.getAttribute("values")+'"]')
cpu_css = coreComponent.createKeyValueSetSymbol("CLK_CPU_CKR_CSS", cpu_menu)
cpu_css.setLabel(cpu_css_node.getAttribute("name"))
cpu_css.setDescription(cpu_css_node.getAttribute("caption"))
cpu_css.setDisplayMode("Key")
cpu_css.setOutputMode("Key")
for value in cpu_css_vg_node.getChildren():
    cpu_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
cpu_css.setDefaultValue(2)

cpu_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="PRES"]')
cpu_pres_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_pres_node.getAttribute("values")+'"]')
cpu_pres = coreComponent.createKeyValueSetSymbol("CLK_CPU_CKR_PRES", cpu_menu)
cpu_pres.setLabel(cpu_pres_node.getAttribute("name"))
cpu_pres.setDescription(cpu_pres_node.getAttribute("caption"))
cpu_pres.setDisplayMode("Key")
cpu_pres.setOutputMode("Key")
for value in cpu_pres_vg_node.getChildren():
    cpu_pres.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
cpu_pres.setDefaultValue(0)

cpu_mdiv_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="MDIV"]')
cpu_mdiv_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_mdiv_node.getAttribute("values")+'"]')
cpu_mdiv = coreComponent.createKeyValueSetSymbol("CLK_CPU_CKR_MDIV", cpu_menu)
cpu_mdiv.setLabel(cpu_mdiv_node.getAttribute("name"))
cpu_mdiv.setDescription(cpu_mdiv_node.getAttribute("caption"))
cpu_mdiv.setDisplayMode("Key")
cpu_mdiv.setOutputMode("Key")
for value in cpu_mdiv_vg_node.getChildren():
    cpu_mdiv.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
cpu_mdiv.setDefaultValue(3)

cpu_clk = coreComponent.createIntegerSymbol("CPU_CLOCK_FREQUENCY", cpu_menu)
cpu_clk.setVisible(False)
input_freq = 0
if cpu_css.getValue() == 0:
    input_freq = md_slck.getValue()
elif cpu_css.getValue() == 1:
    input_freq = mainck.getValue()
elif cpu_css.getValue() == 2:
    input_freq = pllack.getValue()
elif cpu_css.getValue() == 3:
    input_freq = upllck.getValue()
pres = 0
if cpu_pres.getValue() != 7:
    pres = pow(2,cpu_pres.getValue())
else:
    pres = 3
cpu_clk.setDefaultValue(input_freq / pres)
cpu_clk.setDependencies(update_cpu_clk_freq, ['CLK_CPU_CKR_CSS', 'CLK_CPU_CKR_PRES', 'MD_SLOW_CLK_FREQUENCY', 'MAINCK_FREQUENCY', 'PLLA_FREQUENCY', 'UPLL_FREQUENCY'])

mck = coreComponent.createIntegerSymbol("MCK_FREQUENCY", cpu_menu)
mck.setVisible(False)
input_freq = cpu_clk.getValue()
div = 0
if cpu_mdiv.getValue() != 3:
    div = pow(2,cpu_mdiv.getValue())
else:
    div = 3
mck.setDefaultValue(input_freq / div)
mck.setDependencies(update_mck_freq, ['CPU_CLOCK_FREQUENCY', 'CLK_CPU_CKR_MDIV'])

pck_menu = coreComponent.createMenuSymbol("CLK_PCK_MENU", menu)
pck_menu.setLabel("PCK")
pck_menu.setDescription("Programmable Clocks")

num_pcks = int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]').getAttribute("count"))
for pckx in range(0, num_pcks):
    pckx_en = coreComponent.createBooleanSymbol("CLK_PCK"+str(pckx)+"_EN", pck_menu)
    pckx_en.setLabel("Enable PCK"+str(pckx))

    pckx_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="CSS"]')
    pckx_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pckx_css_node.getAttribute("values")+'"]')
    pckx_css = coreComponent.createKeyValueSetSymbol("CLK_PCK"+str(pckx)+"_CSS", pckx_en)
    pckx_css.setLabel(pckx_css_node.getAttribute("name"))
    pckx_css.setDescription(pckx_css_node.getAttribute("caption"))
    pckx_css.setDisplayMode("Key")
    pckx_css.setOutputMode("Key")
    for value in pckx_css_vg_node.getChildren():
        pckx_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

    pckx_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="PRES"]')
    pckx_pres = coreComponent.createIntegerSymbol("CLK_PCK"+str(pckx)+"_PRES", pckx_en)
    pckx_pres.setLabel(pckx_pres_node.getAttribute("name"))
    pckx_pres.setDescription(pckx_pres_node.getAttribute("caption"))
    pckx_pres.setMin(0)
    pckx_pres.setMax(255)

    pckx_freq = coreComponent.createIntegerSymbol("CLK_PCK"+str(pckx)+"_FREQUENCY", pckx_en)
    pckx_freq.setVisible(False)
    input_freq = 0
    if pckx_en.getValue() == True:
        input_freq = pckx_freq.getComponent().getSymbolValue(pckx_css.getKey(pckx_css.getValue())+"_FREQUENCY")
    pckx_freq.setDefaultValue(input_freq / (pckx_pres.getValue() + 1))
    pckx_freq.setDependencies(update_pck_freq, ['CLK_PCK'+str(pckx)+'_EN', 'CLK_PCK'+str(pckx)+'_CSS', 'CLK_PCK'+str(pckx)+'_PRES', 'MD_SLOW_CLK_FREQUENCY', 'TD_SLOW_CLOCK_FREQUENCY', 'MAINCK_FREQUENCY',
            'MCK_FREQUENCY', 'PLLA_FREQUENCY', 'UPLL_FREQUENCY'])

usb_menu = coreComponent.createMenuSymbol("CLK_US_MENU", menu)
usb_menu.setLabel("USB")

usb_en = coreComponent.createBooleanSymbol("CLK_USB_EN", usb_menu)
usb_en.setLabel("Enable UHP clocks")

usbs_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_USB"]/bitfield@[name="USBS"]')
usbs_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+usbs_node.getAttribute("values")+'"]')
usbs = coreComponent.createKeyValueSetSymbol("CLK_USB_USBS", usb_en)
usbs.setLabel(usbs_node.getAttribute("name"))
usbs.setDescription(usbs_node.getAttribute("caption"))
usbs.setDisplayMode("Key")
usbs.setOutputMode("Key")
for value in usbs_vg_node.getChildren():
    usbs.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

usbdiv_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_USB"]/bitfield@[name="USBDIV"]')
usbdiv = coreComponent.createIntegerSymbol("CLK_USB_USBDIV", usb_en)
usbdiv.setLabel(usbdiv_node.getAttribute("name"))
usbdiv.setDescription(usbdiv_node.getAttribute("caption"))
usbdiv.setMin(0)
usbdiv.setMax(15)

usb_freq = coreComponent.createIntegerSymbol("CLK_UHP48M", usb_en)
usb_freq.setVisible(False)
input_freq = 0
if usb_en.getValue == True:
    if usbs.getValue() == 0:
        input_freq = pllack.getValue()
    if usbs.getValue() == 1:
        input_freq = upllck.getValue()
    if usbs.getValue() >=2:
        input_freq = moscxt_freq.getValue()
usb_freq.setDefaultValue( input_freq / (usbdiv.getValue()+1))
usb_freq.setDependencies(update_usb_freq, ['CLK_USB_EN', 'PLLA_FREQUENCY', 'UPLL_FREQUENCY', 'CLK_MOSCXT_FREQ', 'CLK_USB_USBS', 'CLK_USB_USBDIV'])

usb_freq_warning = coreComponent.createCommentSymbol("CLK_USB_FREQ_WARNING", usb_en)
usb_freq_warning.setLabel("USB clocks not configured for 48 MHz")
usb_freq_warning.setVisible((usb_freq.getValue() != 48000000) and (usb_en.getValue() == True))
usb_freq_warning.setDependencies(update_usb_warning, ['CLK_UHP48M', 'CLK_USB_EN'])

#peripheral clock controller
pcr_menu = coreComponent.createMenuSymbol("CLK_PCR_MENU", menu)
pcr_menu.setLabel("Peripheral Clocks")

gclk_menu = coreComponent.createMenuSymbol("CLK_GCLK_MENU", menu)
gclk_menu.setLabel("Generic Clocks")

#find all peripherals that have PMC controlls
#generics
generic_clocks = ["FLEXCOM", "SDMMC", "TC", "ADC", "LCDC", "I2SMCC", "PIT64B", "CLASSD", "DBGU"]
#Create map of name->id's for Java code to know what supports generic clocks
generic_clocks_map = coreComponent.createKeyValueSetSymbol("GCLK_INSTANCE_PID", gclk_menu)
generic_clocks_map.setVisible(False)

peripherals_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
for module_node in peripherals_node.getChildren():
    for instance_node in module_node.getChildren():
        clock_id_node = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="'+module_node.getAttribute("name")+'"]/instance@[name="'+instance_node.getAttribute("name")+'"]/parameters/param@[name="CLOCK_ID"]')
        if clock_id_node is None:
            continue

        instance_name = instance_node.getAttribute("name")
        pcr_en = coreComponent.createBooleanSymbol(instance_name + "_CLOCK_ENABLE", pcr_menu)
        pcr_en.setLabel(instance_name)

        id_name_map = coreComponent.createStringSymbol("CLK_ID_NAME_"+clock_id_node.getAttribute("value"), pcr_menu)
        id_name_map.setVisible(False)
        id_name_map.setDefaultValue(instance_name)

        pcr_freq = coreComponent.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
        pcr_freq.setVisible(False)
        pcr_freq.setDefaultValue(mck.getValue())
        if module_node.getAttribute("name") not in generic_clocks:
            pcr_freq.setDependencies(lambda symbol, event: symbol.setValue(event['source'].getSymbolValue("MCK_FREQUENCY"),0), ['MCK_FREQUENCY'])

        else:
            generic_clocks_map.addKey(instance_name, clock_id_node.getAttribute("value"), "")
            gclk_periph = coreComponent.createMenuSymbol(None, gclk_menu)
            gclk_periph.setLabel(instance_name)

            gclk_en = coreComponent.createBooleanSymbol("CLK_"+instance_name+"_GCLKEN", gclk_periph)
            gclk_en.setLabel("Enable")

            gclk_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKCSS"]')
            gclk_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+gclk_css_node.getAttribute("values")+'"]')
            gclk_css = coreComponent.createKeyValueSetSymbol("CLK_" + instance_name + "_GCLKCSS", gclk_periph)
            gclk_css.setLabel(gclk_css_node.getAttribute("name"))
            gclk_css.setDescription(gclk_css_node.getAttribute("caption"))
            gclk_css.setDisplayMode("Key")
            gclk_css.setOutputMode("Key")
            for value in gclk_css_vg_node.getChildren():
                gclk_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

            gclk_div_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKDIV"]')
            gclk_div = coreComponent.createIntegerSymbol("CLK_"+instance_name+"_GCLKDIV", gclk_periph)
            gclk_div.setLabel(gclk_div_node.getAttribute("name"))
            gclk_div.setDescription(gclk_div_node.getAttribute("caption"))
            gclk_div.setMin(0)
            gclk_div.setMax(255)

            gclk_freq = coreComponent.createIntegerSymbol(instance_name+"_GCLK_FREQUENCY", gclk_periph)
            gclk_freq.setVisible(False)
            input_freq = 0
            if gclk_en.getValue() == True:
                input_freq = gclk_freq.getComponent().getSymbolValue(gclk_css.getKey(gclk_css.getValue())+"_FREQUENCY")
            gclk_freq.setDefaultValue(input_freq / (gclk_div.getValue() + 1))
            gclk_freq.setDependencies(update_gclk_freq, ['CLK_'+instance_name+'_GCLKEN',
                    'CLK_'+instance_name+'_GCLKCSS', 'CLK_'+instance_name+'_GCLKDIV',
                    'MD_SLOW_CLK_FREQUENCY', 'TD_SLOW_CLOCK_FREQUENCY', 'MAINCK_FREQUENCY',
                    'MCK_FREQUENCY', 'PLLA_FREQUENCY', 'UPLL_FREQUENCY'])

            # TC plib expects frequency and enable bits per channel. Create dummy symbols to support this
            if module_node.getAttribute("name") == "TC":
                tc_ch_en_dep_list = []
                #  create a dummy symbol per channel. TC has 3 channels. We create three ENABLE symbols( one per channel )
                #  and four FREQUENCY symbols (one per channel + one additional symbol for quadrature mode )
                for channel in range(4):
                    if channel < 3:
                        tc_ch_en_name = instance_name + "_CHANNEL" + str(channel) + "_CLOCK_ENABLE"
                        tc_ch_en = coreComponent.createBooleanSymbol(tc_ch_en_name, pcr_menu)
                        tc_ch_en.setVisible(False)
                        tc_ch_en.setReadOnly(True)
                        tc_ch_en_dep_list.append(tc_ch_en_name)

                    tc_ch_freq = coreComponent.createIntegerSymbol(
                        instance_name + "_CH" + str(channel) + "_CLOCK_FREQUENCY", pcr_menu)
                    tc_ch_freq.setVisible(False)
                    tc_ch_freq.setReadOnly(True)
                    tc_ch_freq.setDefaultValue(Database.getSymbolValue("core", "MCK_FREQUENCY"))
                    tc_ch_freq.setDependencies(update_tc_freq,
                                               ["MCK_FREQUENCY",
                                                "MD_SLOW_CLK_FREQUENCY",
                                                instance_name + "_GCLK_FREQUENCY",
                                                instance_name.lower() + ".TC" + str(channel) + "_CMR_TCCLKS",
                                                instance_name.lower() + ".TC" + str(channel) + "_ENABLE"])

                pcr_en.setDependencies(update_tc_enable, tc_ch_en_dep_list)

            # SDMMC requires two additional frequency symbols for mapping to the base clock and multiplier clock
            elif module_node.getAttribute("name") == "SDMMC":
                sdmmc_baseclk_freq_sym = coreComponent.createIntegerSymbol(instance_name + "_BASECLK_FREQUENCY", pcr_menu)
                sdmmc_baseclk_freq_sym.setVisible(False)
                sdmmc_baseclk_freq_sym.setReadOnly(True)
                sdmmc_baseclk_freq_sym.setDefaultValue(gclk_freq.getValue() / 2)

                sdmmc_multclk_freq_sym = coreComponent.createIntegerSymbol(instance_name + "_MULTCLK_FREQUENCY", pcr_menu)
                sdmmc_multclk_freq_sym.setVisible(False)
                sdmmc_multclk_freq_sym.setReadOnly(True)
                sdmmc_multclk_freq_sym.setDefaultValue(gclk_freq.getValue())

                pcr_freq.setDependencies(update_sdmmc_clock_frequency, ['MCK_FREQUENCY', instance_name + '_GCLK_FREQUENCY'])

            #Flexcomm requires additional symbol dependencies for mode selection
            elif module_node.getAttribute("name") == "FLEXCOM":
                pcr_freq.setDependencies(gclk_update_map[module_node.getAttribute("name")],
                                         ['MCK_FREQUENCY',
                                          instance_name + '_GCLK_FREQUENCY',
                                          instance_name.lower() + "." + "FLEXCOM_MODE",
                                          instance_name.lower() + "." + "FLEXCOM_USART_MR_USCLKS",
                                          instance_name.lower() + "." + "FLEXCOM_SPI_MR_BRSRCCLK",
                                          instance_name.lower() + "." + "FLEXCOM_TWI_CWGR_BRSRCCLK"])

            else:
                pcr_freq.setDependencies(gclk_update_map[module_node.getAttribute("name")],
                                         ['MCK_FREQUENCY', instance_name + '_GCLK_FREQUENCY',
                                          instance_name.lower() + "." + gclk_dependency_map[instance_name]])


sys_clk_menu = coreComponent.createMenuSymbol("CLK_SYSTEM_CLK_MENU", menu)
sys_clk_menu.setLabel("System Clocks")

ddr = coreComponent.createBooleanSymbol("CLK_DDR_ENABLE", sys_clk_menu)
ddr.setLabel("Enbable DDR Clock")
ddr.setDefaultValue(True)

ddr_frq = coreComponent.createIntegerSymbol("DDRCLK_FREQUENCY", sys_clk_menu)
ddr_frq.setVisible(False)
if ddr.getValue() == True:
    ddr_frq.setDefaultValue(mck.getValue() * 2)
else:
    ddr_frq.setDefaultValue(0)
ddr_frq.setDependencies(lambda symbol, event: symbol.setValue(((event['source'].getSymbolValue('MCK_FREQUENCY') * 2)
                        if event['source'].getSymbolValue('CLK_DDR_ENABLE') is True else 0),0),
                        ['MCK_FREQUENCY','CLK_DDR_ENABLE'])

qspi_clk = coreComponent.createBooleanSymbol("CLK_QSPICLK_ENABLE", sys_clk_menu)
qspi_clk.setLabel("Enbable QSPI Clock")

qspi_frq = coreComponent.createIntegerSymbol("QSPICLK_FREQUENCY", sys_clk_menu)
qspi_frq.setVisible(False)
qspi_frq.setDefaultValue((mck.getValue() * 2) if qspi_clk.getValue() is True else 0)
qspi_frq.setDependencies(lambda symbol, event: symbol.setValue(((event['source'].getSymbolValue('MCK_FREQUENCY') * 2)
                         if event['source'].getSymbolValue('CLK_QSPICLK_ENABLE') is True else 0), 0),
                         ['MCK_FREQUENCY', 'CLK_QSPICLK_ENABLE'])

gen_code = coreComponent.createBooleanSymbol("CLK_GENERATOR_CODE", menu)
gen_code.setLabel("Enable generator initialization code")
gen_code.setDescription("Generate code for initializing Slow clocks, mainclock, and PLL's.  This should only be done if running out of SRAM.  This is mainly intended for writing booloaders.")

gen_code_comment = coreComponent.createCommentSymbol(None, gen_code)
gen_code_comment.setLabel("WARNING: This could cause lock ups if running out of DDR.  Only enable if running out of SRAM.")

pit = coreComponent.createIntegerSymbol("PIT_CLOCK_FREQUENCY", None)
pit.setVisible(False)
pit.setDefaultValue(mck.getValue())
pit.setDependencies(lambda symbol, event: symbol.setValue(event['value'],0), ['MCK_FREQUENCY'])

config = Variables.get("__CONFIGURATION_NAME")

cfile = coreComponent.createFileSymbol(None, None)
cfile.setSourcePath("../peripheral/clk_sam_9x60/templates/plib_clk.c.ftl")
cfile.setOutputName("plib_clk.c")
cfile.setDestPath("/peripheral/clk/")
cfile.setProjectPath("config/"+config+"/peripheral/clk/")
cfile.setType("SOURCE")
cfile.setMarkup(True)

chdr = coreComponent.createFileSymbol(None, None)
chdr.setSourcePath("../peripheral/clk_sam_9x60/templates/plib_clk.h.ftl")
chdr.setOutputName("plib_clk.h")
chdr.setDestPath("/peripheral/clk/")
chdr.setProjectPath("config/"+config+"/peripheral/clk/")
chdr.setType("HEADER")
chdr.setMarkup(True)

defFile = coreComponent.createFileSymbol(None, None)
defFile.setType("STRING")
defFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
defFile.setSourcePath("../peripheral/clk_sam_9x60/templates/system/definitions.h.ftl")
defFile.setMarkup(True)

initFile = coreComponent.createFileSymbol(None, None)
initFile.setType("STRING")
initFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
initFile.setSourcePath("../peripheral/clk_sam_9x60/templates/system/initialization.c.ftl")
initFile.setMarkup(True)

