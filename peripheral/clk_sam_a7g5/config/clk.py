"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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


global bootloader_default_dict
bootloader_default_dict = {
    "CLK_TD_OSCSEL": 1,

    "CLK_MOSCRCEN": False,
    "CLK_MOSCXTEN": True,
    "CLK_MOSCXT_FREQ": 24000000,
    "CLK_MOSCSEL": 1,

    "CLK_CPUPLL_EN": True,
    "CLK_CPUPLL_MUL": 32,
    "CLK_CPUPLL_FRACR": 0x155556,
    "CLK_CPUPLL_DIVPMC": 0,
    "CLK_CPUPLL_SS": None,
    "CLK_CPUPLL_SS_STEP": None,
    "CLK_CPUPLL_SS_NSTEP": None,

    "CLK_SYSPLL_EN": True,
    "CLK_SYSPLL_MUL": 49,
    "CLK_SYSPLL_FRACR": 0,
    "CLK_SYSPLL_DIVPMC": 2,
    "CLK_SYSPLL_SS": None,
    "CLK_SYSPLL_SS_STEP": None,
    "CLK_SYSPLL_SS_NSTEP": None,

    "CLK_DDRPLL_EN": True,
    "CLK_DDRPLL_MUL": 43,
    "CLK_DDRPLL_FRACR": 0x1AAAAB,
    "CLK_DDRPLL_DIVPMC": 1,
    "CLK_DDRPLL_SS": None,
    "CLK_DDRPLL_SS_STEP": None,
    "CLK_DDRPLL_SS_NSTEP": None,

    "CLK_IMGPLL_EN": True,
    "CLK_IMGPLL_MUL": 43,
    "CLK_IMGPLL_FRACR": 0x155555,
    "CLK_IMGPLL_DIVPMC": 3,
    "CLK_IMGPLL_SS": None,
    "CLK_IMGPLL_SS_STEP": None,
    "CLK_IMGPLL_SS_NSTEP": None,

    "CLK_CPU_CKR_CSS": 2,
    "CLK_CPU_CKR_PRES": 0,
    "CLK_CPU_CKR_MDIV": 2,

    "CLK_MCR_MCK1_CSS": 3,
    "CLK_MCR_MCK1_DIV": 1,

    "CLK_MCR_MCK2_CSS": 0,
    "CLK_MCR_MCK2_DIV": 0,

    "CLK_MCR_MCK3_CSS": 5,
    "CLK_MCR_MCK3_DIV": 0,

    "CLK_MCR_MCK4_CSS": 3,
    "CLK_MCR_MCK4_DIV": 0
}


global setup_bootloader_defaults
def setup_bootloader_defaults(component, use_defaults):
    for symbol_name, value in bootloader_default_dict.items():
        symbol = component.getSymbolByID(symbol_name)
        if use_defaults:
            symbol.setReadOnly(True)
            if value is not None:
                symbol.setValue(value)
        else:
            symbol.setReadOnly(False)
            symbol.clearValue()


def get_peripheral_clock_id(module_name):
    mck0_peripheral_list = ["DWDT", "SCKC", "SHDWC", "RSTC", "RTC", "RTT", "OTPC", "PIO"]
    mck3_peripheral_list = ["CSI"]
    if module_name in mck0_peripheral_list:
        mck_id = 0
    elif module_name in mck3_peripheral_list:
        mck_id = 3
    else:
        mck_id = 1
    return mck_id


def update_td_slck(symbol, event):
    osel = event['source'].getSymbolByID("CLK_TD_OSCSEL")
    value = 0
    if osel.getSelectedKey() == "RC":
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


def update_pll_core_freq(symbol, event):
    pll = symbol.getID().split("_")[0]
    
    source_freq = event['source'].getSymbolValue(pll_default_config_dict.get(pll)["source"])
    mul = event['source'].getSymbolValue("CLK_{0}_MUL".format(pll))
    fracr = event['source'].getSymbolValue("CLK_{0}_FRACR".format(pll))
    if mul > 0:
        symbol.setValue(int((source_freq * (mul + 1 + (float(fracr)/pow(2, 22))))))
    else:
        symbol.setValue(0)


def update_pll_pmc_freq(symbol, event):
    pll = symbol.getID().split("_")[0]
    pllcore_clk = event["source"].getSymbolValue("{0}_CORE_FREQUENCY".format(pll))
    enable = event['source'].getSymbolValue("CLK_{0}_EN".format(pll))
    divpmc = event['source'].getSymbolValue("CLK_{0}_DIVPMC".format(pll))
    if enable:
        symbol.setValue(int(round((pllcore_clk / (divpmc + 1)), -2)))
    else:
        symbol.setValue(0)
    

def update_pll_io_freq(symbol, event):
    pll = symbol.getID().split("_")[0]
    pllcore_clk = event["source"].getSymbolValue("{0}_CORE_FREQUENCY".format(pll))
    io_enable = event['source'].getSymbolValue("CLK_{0}_ENIOPLLCK".format(pll))
    divio = event['source'].getSymbolValue("CLK_{0}_DIVIO".format(pll))
    if io_enable:
        symbol.setValue(int(round((pllcore_clk / (divio + 1)), -2)))
    else:
        symbol.setValue(0)


def update_fclk_freq(symbol, event):
    cpu_css = event["source"].getSymbolByID("CLK_CPU_CKR_CSS")
    cpu_pres = event["source"].getSymbolByID("CLK_CPU_CKR_PRES")
    if cpu_css.getSelectedKey() == "SLOW_CLK":
        src_freq = event["source"].getSymbolValue("MD_SLOW_CLK_FREQUENCY")
    elif cpu_css.getSelectedKey() == "MAIN_CLK":
        src_freq = event["source"].getSymbolValue("MAINCK_FREQUENCY")
    elif cpu_css.getSelectedKey() == "CPUPLLCK":
        src_freq = event["source"].getSymbolValue("CPUPLL_FREQUENCY")
    else:
        src_freq = event["source"].getSymbolValue("SYSPLL_FREQUENCY")
    pres_value = int(cpu_pres.getSelectedKey().split("CLK_")[1])
    symbol.setValue(src_freq/pres_value)


def update_cpu_clk_freq(symbol, event):
    source_freq = event["source"].getSymbolValue("FCLK_FREQUENCY")
    ratio = event["source"].getSymbolValue("CLK_CPU_RATIO")
    symbol.setValue((source_freq * (ratio + 1)) / 16)


def update_mck0_freq(symbol, event):
    source_freq = event["source"].getSymbolValue("FCLK_FREQUENCY")
    mdiv_key = event["source"].getSymbolByID("CLK_CPU_CKR_MDIV").getSelectedKey()
    if mdiv_key.startswith("PCK_DIV"):
        mdiv = int(mdiv_key.split("PCK_DIV")[1])
    else:
        mdiv = 1
    symbol.setValue(source_freq / mdiv)


def update_mckx_freq(symbol, event):
    comp = event["source"]
    mckx_id = int(symbol.getID().split("_FREQUENCY")[0].split("MCK")[1])
    mckx_css = comp.getSymbolByID("CLK_MCR_MCK{0}_CSS".format(mckx_id))
    mckx_div = comp.getSymbolByID("CLK_MCR_MCK{0}_DIV".format(mckx_id))
    src_frequency = comp.getSymbolValue(mckx_css.getSelectedKey() + "_FREQUENCY")
    divisor = int(mckx_div.getSelectedKey().split("MASTER_DIV")[1])
    symbol.setValue(src_frequency / divisor)


def update_pck_freq(symbol, event):
    index = int(symbol.getID().split("PCK")[1].split("_")[0])
    pckx_pres = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_PRES")
    pckx_css = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_CSS")
    enabled = event['source'].getSymbolValue("CLK_PCK"+str(index)+"_EN")
    input_freq = 0
    if enabled == True:
        input_freq = event['source'].getSymbolValue(pckx_css.getSelectedKey()+"_FREQUENCY")
    symbol.setValue(input_freq / (pckx_pres.getValue() + 1), 0)


def update_gclk_freq(symbol, event):
    instance_name = symbol.getID().split("_")[0]
    gclk_css = event['source'].getSymbolByID("CLK_"+instance_name+"_GCLKCSS")
    gclk_div = event['source'].getSymbolByID("CLK_"+instance_name+"_GCLKDIV")
    input_freq = event['source'].getSymbolValue(gclk_css.getSelectedKey()+"_FREQUENCY")
    enabled = event['source'].getSymbolValue("CLK_"+instance_name+"_GCLKEN")
    if enabled == True:
        symbol.setValue(input_freq / (gclk_div.getValue() + 1))
    else:
        symbol.setValue(0)

def update_bootloader_clocks(symbol, event):
    setup_bootloader_defaults(event["source"], event["value"])


#Place holder function clock frequency setup for modules that have a generic clock
def setup_generic_gclk_module_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = local_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
    pcr_freq.setVisible(False)
    pcr_freq.setReadOnly(True)
    pcr_freq.setDefaultValue(remote_comp.getSymbolValue("MCK1_FREQUENCY"))
    pcr_freq.setDependencies(lambda symbol, event: symbol.setValue(event["value"]), ["MCK1_FREQUENCY"])


def setup_adc_arm_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    clock_id = 0
    if module_name == "ARM":
        clock_id = 29
    elif module_name == "ADC":
        clock_id = 26

    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")
    
    #create a dummy clock id symbol so that the clock code generates code for GCLK
    id_name_map = local_comp.createStringSymbol("CLK_ID_NAME_" + str(clock_id), pcr_menu)
    id_name_map.setVisible(False)
    id_name_map.setDefaultValue(instance_name)

    #create peripheral frequency symbol
    pcr_freq = local_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
    pcr_freq.setVisible(False)
    pcr_freq.setDefaultValue(remote_comp.getSymbolValue(instance_name +"_GCLK_FREQUENCY"))
    pcr_freq.setDependencies(lambda symbol, event: symbol.setValue(event["value"]), [instance_name +"_GCLK_FREQUENCY"])


def setup_tc_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")   
    for channel in range(4):
        tc_ch_freq = local_comp.createIntegerSymbol("{0}_CH{1}_CLOCK_FREQUENCY".format(instance_name, channel), pcr_menu)
        tc_ch_freq.setVisible(False)
        tc_ch_freq.setReadOnly(True)
        tc_ch_freq.setDefaultValue(remote_comp.getSymbolValue("MCK1_FREQUENCY"))
        tc_ch_freq.setDependencies(update_tc_clock_frequency,
                                    ["MCK1_FREQUENCY",
                                    "MD_SLOW_CLK_FREQUENCY",
                                    "{0}_GCLK_FREQUENCY".format(instance_name),
                                    "{0}.TC{1}_CMR_TCCLKS".format(instance_name.lower(), channel),
                                    "{0}.TC{1}_ENABLE".format(instance_name.lower(), channel)])


def setup_sdmmc_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = local_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
    pcr_freq.setVisible(False)
    pcr_freq.setReadOnly(True)
    pcr_freq.setDefaultValue(remote_comp.getSymbolValue("MCK1_FREQUENCY"))
    gclk_freq = remote_comp.getSymbolByID("{0}_GCLK_FREQUENCY".format(instance_name))

    sdmmc_baseclk_freq_sym = local_comp.createIntegerSymbol(instance_name + "_BASECLK_FREQUENCY", pcr_menu)
    sdmmc_baseclk_freq_sym.setVisible(False)
    sdmmc_baseclk_freq_sym.setReadOnly(True)
    sdmmc_baseclk_freq_sym.setDefaultValue(gclk_freq.getValue() / 2)

    sdmmc_multclk_freq_sym = local_comp.createIntegerSymbol(instance_name + "_MULTCLK_FREQUENCY", pcr_menu)
    sdmmc_multclk_freq_sym.setVisible(False)
    sdmmc_multclk_freq_sym.setReadOnly(True)
    sdmmc_multclk_freq_sym.setDefaultValue(gclk_freq.getValue())

    pcr_freq.setDependencies(update_sdmmc_clock_frequency, ['MCK1_FREQUENCY', instance_name + '_GCLK_FREQUENCY'])


def setup_mcan_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = local_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
    pcr_freq.setVisible(False)
    pcr_freq.setReadOnly(True)
    gclk_freq = remote_comp.getSymbolByID("{0}_GCLK_FREQUENCY".format(instance_name))

    pcr_freq.setDefaultValue(gclk_freq.getValue())
    pcr_freq.setDependencies(lambda symbol, event: symbol.setValue(event["value"]), [gclk_freq.getID()])


def setup_pit64b_clock_frequency(local_comp, remote_comp, module_name, instance_name):
    pcr_menu = remote_comp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = local_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
    pcr_freq.setVisible(False)
    pcr_freq.setReadOnly(True)
    pcr_freq.setDefaultValue(remote_comp.getSymbolValue("MCK1_FREQUENCY"))
    pcr_freq.setDependencies(update_pit64b_clock_frequency, 
                                ["MCK1_FREQUENCY",
                                "{0}_GCLK_FREQUENCY".format(instance_name),
                                "{0}.SGCLK".format(instance_name.lower())])


global update_tc_clock_frequency
def update_tc_clock_frequency(symbol, event):
    # symbol is named as "TC{instance_number}_CH{channel_number}_CLOCK_FREQUENCY.
    # Extract the instance number
    instance_num = symbol.getID().split("TC")[1].split("_")[0]
    # extract the channel number
    channel_num = symbol.getID().split("_CH")[1].split("_")[0]

    #Get the tc component
    tc_comp = Database.getComponentByID("tc{0}".format(instance_num))
    clk_comp = Database.getComponentByID("core")
    mck1_freq = clk_comp.getSymbolValue("MCK1_FREQUENCY")
    
    # check if component exists and the relevant channel is enabled
    if tc_comp is not None and tc_comp.getSymbolValue("TC{0}_ENABLE".format(channel_num)):
        # Find the current clock source for the channel
        clk_src_sym = tc_comp.getSymbolByID("TC{0}_CMR_TCCLKS".format(channel_num))
        clk_src = clk_src_sym.getKeyDescription(clk_src_sym.getValue())
        
        # if clock source is processor independent GCLK
        if (clk_src == "GCLK"):
            clk_frequency = clk_comp.getSymbolValue("TC{0}_GCLK_FREQUENCY".format(instance_num))
        # if clock  source is MCK/8
        elif (clk_src == "MCK1/8"):
            clk_frequency = mck1_freq / 8
        # if clock  source is MCK/32
        elif (clk_src == "MCK1/32"):
            clk_frequency = mck1_freq / 32
        # if clock  source is MCK/128
        elif (clk_src == "MCK1/128"):
            clk_frequency = mck1_freq / 128
        # if clock  source is SLOW CLOCK
        elif (clk_src == "TD_SLCK"):
            clk_frequency = clk_comp.getSymbolValue("TD_SLOW_CLOCK_FREQUENCY")
        # default  clock source is MCK (Enabled through extended registers of TC)
        else:
            clk_frequency = mck1_freq
        symbol.setValue(clk_frequency)


global update_sdmmc_clock_frequency
def update_sdmmc_clock_frequency(symbol, event):
    sdmmc_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]

    # set the HCLOCK frequency
    mck_clk_freq = event['source'].getSymbolValue("MCK1_FREQUENCY")
    symbol.setValue(mck_clk_freq, 0)

    # set the base clock frequency
    gclk_clk_freq = event['source'].getSymbolValue(sdmmc_name + "_GCLK_FREQUENCY")
    base_clk_sym = event['source'].getSymbolByID(sdmmc_name + "_BASECLK_FREQUENCY")
    base_clk_sym.setValue(gclk_clk_freq / 2)

    # set the multiplier clock frequency
    mult_clk_sym = event['source'].getSymbolByID(sdmmc_name + "_MULTCLK_FREQUENCY")
    mult_clk_sym.setValue(gclk_clk_freq)


global update_pit64b_clock_frequency
def update_pit64b_clock_frequency(symbol, event):
    instance_name = symbol.getID().split("_")[0]
    sgclk = Database.getSymbolValue(instance_name.lower(), "SGCLK")
    if sgclk:
        symbol.setValue(event["source"].getSymbolValue("{0}_GCLK_FREQUENCY".format(instance_name)))
    else:
        symbol.setValue(event["source"].getSymbolValue("MCK1_FREQUENCY"))


def update_timestamp_frequency(symbol, event):
    if event["source"].getSymbolValue("SYSTEM_COUNTER_ENABLE"):
        symbol.setValue(event["source"].getSymbolValue("MAINCK_FREQUENCY"))
    else:
        symbol.setValue(0)



if __name__ == "__main__":

    #Get a local variable to avoid linter warning everywhere
    clk_component = coreComponent

    menu = clk_component.createMenuSymbol("CLK_MENU", None)
    menu.setLabel("Clock (PMC)")
    menu.setDescription("Clock configuration")

    #Get a handle to this components remote interface
    clk_remote_component = menu.getComponent()

    bootloader_clocks = clk_component.createBooleanSymbol("USE_BOOTLOADER_GENERATORS", menu)
    bootloader_clocks.setLabel("Use Clock generators configured by at91bootstrap")
    bootloader_clocks.setDefaultValue(True)
    bootloader_clocks.setDependencies(update_bootloader_clocks, ["USE_BOOTLOADER_GENERATORS"])

    #slow clock
    sckc_menu = clk_component.createMenuSymbol("CLK_SCKC_MENU", menu)
    sckc_menu.setLabel("Slow Clock (SCKC)")
    sckc_menu.setDescription("Slow Clock Controller (SCKC)")
    
    td_oscel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/register-group@[name="SCKC"]/register@[name="SCKC_CR"]/bitfield@[name="TD_OSCSEL"]')
    td_oscel_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SCKC"]/value-group@[name="'+td_oscel_node.getAttribute("values")+'"]')
    td_oscel = clk_component.createKeyValueSetSymbol("CLK_TD_OSCSEL", sckc_menu)
    td_oscel.setLabel(td_oscel_node.getAttribute("name"))
    td_oscel.setDescription(td_oscel_node.getAttribute("caption"))
    td_oscel.setDisplayMode("Key")
    td_oscel.setOutputMode("Key")
    for value in td_oscel_vg_node.getChildren():
        td_oscel.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    
    td_slck = clk_component.createIntegerSymbol("TD_SLOW_CLOCK_FREQUENCY", sckc_menu)
    td_slck.setReadOnly(True)
    value = 0
    if td_oscel.getSelectedKey() == "RC":
        value = 32000
    else:
        value = 32768
    td_slck.setDefaultValue(value)
    td_slck.setDependencies(update_td_slck, ['CLK_TD_OSCSEL'])

    md_slck = clk_component.createIntegerSymbol("MD_SLOW_CLK_FREQUENCY", sckc_menu)
    md_slck.setReadOnly(True)
    md_slck.setDefaultValue(32000)


    #main clock
    mainck_menu = clk_component.createMenuSymbol("CLK_MAINCK_MENU", menu)
    mainck_menu.setLabel("Main Clock (MAINCK)")

    moscrcen_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCRCEN"]')
    moscrcen = clk_component.createBooleanSymbol("CLK_MOSCRCEN", mainck_menu)
    moscrcen.setLabel(moscrcen_node.getAttribute("name"))
    moscrcen.setDescription(moscrcen_node.getAttribute("caption"))
    moscrcen.setDefaultValue(True)
    
    moscxten_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTEN"]')
    moscxten = clk_component.createBooleanSymbol("CLK_MOSCXTEN", mainck_menu)
    moscxten.setLabel(moscxten_node.getAttribute("name"))
    moscxten.setDescription(moscxten_node.getAttribute("caption"))

    moscxtst_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCXTST"]')
    moscxtst = clk_component.createIntegerSymbol("CLK_MOSCXTST", mainck_menu)
    moscxtst.setLabel(moscxtst_node.getAttribute("name"))
    moscxtst.setDescription(moscxtst_node.getAttribute("caption"))
    moscxtst.setDefaultValue(255)
    moscxtst.setMin(0)
    moscxtst.setMax(255)
    moscxtst.setDefaultValue(18)

    moscxt_freq = clk_component.createIntegerSymbol("CLK_MOSCXT_FREQ", mainck_menu)
    moscxt_freq.setLabel("Main Crystal Oscillator Freq(Hz)")
    moscxt_freq.setMin(12000000)
    moscxt_freq.setMax(50000000)
    moscxt_freq.setDefaultValue(24000000)

    moscsel_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="CKGR_MOR"]/bitfield@[name="MOSCSEL"]')
    moscsel_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+moscsel_node.getAttribute("values")+'"]')
    moscsel = clk_component.createKeyValueSetSymbol("CLK_MOSCSEL", mainck_menu)
    moscsel.setLabel(moscsel_node.getAttribute("name"))
    moscsel.setDescription(moscsel_node.getAttribute("caption"))
    moscsel.setDisplayMode("Key")
    moscsel.setOutputMode("Value")
    for value in moscsel_vg_node.getChildren():
        moscsel.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))

    mainck = clk_component.createIntegerSymbol("MAINCK_FREQUENCY", mainck_menu)
    mainck.setReadOnly(True)
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
            value = 0
    mainck.setDefaultValue(value)


    #PLL clocks
    pll_list = ["CPUPLL", "SYSPLL", "DDRPLL", "IMGPLL", "BAUDPLL", "AUDIOPLL", "ETHPLL"]

    #pll freqs
    
    global pll_default_config_dict
    pll_default_config_dict = { 
                        "CPUPLL": {"source": "MAINCK_FREQUENCY", "ioclock": False, "enable": True, "mul": 94, "fracr": 0, "div": 1},
                        "SYSPLL": {"source": "MAINCK_FREQUENCY", "ioclock": False, "enable": True, "mul": 62, "fracr": 0, "div": 1},
                        "DDRPLL": {"source": "MAINCK_FREQUENCY", "ioclock": False, "enable": False, "mul": 0, "fracr": 0, "div": 0},
                        "IMGPLL": {"source": "MAINCK_FREQUENCY", "ioclock": False, "enable": False, "mul": 0, "fracr": 0, "div": 0},
                        "BAUDPLL": {"source": "MAINCK_FREQUENCY", "ioclock": False, "enable": False, "mul": 0, "fracr": 0, "div": 0},
                        "AUDIOPLL":{"source": "CLK_MOSCXT_FREQ", "ioclock": True, "enable": False, "mul": 0, "fracr": 0, "div": 0},
                        "ETHPLL": {"source": "CLK_MOSCXT_FREQ", "ioclock": True, "enable": False, "mul": 0, "fracr": 0, "div": 0},
                    }

                    
    for index, pll in enumerate(pll_list):
        pll_menu = clk_component.createMenuSymbol("CLK_{0}_MENU".format(pll), menu)
        pll_menu.setLabel(pll)

        pll_en = clk_component.createBooleanSymbol("CLK_{0}_EN".format(pll), pll_menu)
        pll_en.setLabel("Enable PLL".format(pll))
        pll_en.setDefaultValue(pll_default_config_dict[pll]["enable"])

        pll_mul_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="MUL"]')
        pll_mul = clk_component.createIntegerSymbol("CLK_{0}_MUL".format(pll), pll_en)
        pll_mul.setLabel(pll_mul_node.getAttribute("name"))
        pll_mul.setDescription(pll_mul_node.getAttribute("caption"))
        pll_mul.setMin(0)
        pll_mul.setMax(255)
        pll_mul.setDefaultValue(pll_default_config_dict[pll]["mul"])

        pll_fracr_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL1"]/bitfield@[name="FRACR"]')
        pll_fracr = clk_component.createIntegerSymbol("CLK_{0}_FRACR".format(pll), pll_en)
        pll_fracr.setLabel(pll_fracr_node.getAttribute("name"))
        pll_fracr.setDescription(pll_fracr_node.getAttribute("caption"))
        pll_fracr.setMin(0)
        pll_fracr.setMax(4194303)
        pll_fracr.setDefaultValue(pll_default_config_dict[pll]["fracr"])

        pll_divpmc_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL0"]/bitfield@[name="DIVPMC"]')
        pll_divpmc = clk_component.createIntegerSymbol("CLK_{0}_DIVPMC".format(pll), pll_en)
        pll_divpmc.setLabel(pll_divpmc_node.getAttribute("name"))
        pll_divpmc.setDescription(pll_divpmc_node.getAttribute("caption"))
        pll_divpmc.setMin(0)
        pll_divpmc.setMax(255)
        pll_divpmc.setDefaultValue((pll_default_config_dict[pll]["div"]))

        pll_ss_en_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="ENSPREAD"]')
        pll_ss_en = clk_component.createBooleanSymbol("CLK_{0}_SS".format(pll), pll_en)
        pll_ss_en.setLabel(pll_ss_en_node.getAttribute("name"))
        pll_ss_en.setDescription(pll_ss_en_node.getAttribute("caption"))

        pll_ss_nstep_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="NSTEP"]')
        pll_ss_nstep = clk_component.createIntegerSymbol("CLK_{0}_SS_NSTEP".format(pll), pll_ss_en)
        pll_ss_nstep.setLabel(pll_ss_nstep_node.getAttribute("name"))
        pll_ss_nstep.setDescription(pll_ss_nstep_node.getAttribute("caption"))
        pll_ss_nstep.setMin(0)
        pll_ss_nstep.setMax(255)

        pll_ss_step_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_SSR"]/bitfield@[name="STEP"]')
        pll_ss_step = clk_component.createIntegerSymbol("CLK_{0}_SS_STEP".format(pll), pll_ss_en)
        pll_ss_step.setLabel(pll_ss_step_node.getAttribute("name"))
        pll_ss_step.setDescription(pll_ss_step_node.getAttribute("caption"))
        pll_ss_step.setMin(0)
        pll_ss_step.setMax(65535)

        pll_core_frequency = clk_component.createIntegerSymbol("{0}_CORE_FREQUENCY".format(pll), pll_menu)
        pll_core_frequency.setReadOnly(True)
        pll_core_frequency.setVisible(True)
        if pll_default_config_dict[pll]["source"] == "MAINCK_FREQUENCY":
            pll_src_freq = mainck.getValue()
        else:
            pll_src_freq = moscxt_freq.getValue()
        
        if pll_mul.getValue() > 0:
            pll_core_frequency.setDefaultValue(int(pll_src_freq * (pll_mul.getValue() + 1 + (float(pll_fracr.getValue()) / pow(2,22)))))
        else:
            pll_core_frequency.setDefaultValue(0)
        pll_core_frequency.setDependencies(update_pll_core_freq, [  pll_default_config_dict.get(pll)["source"],
                                                                    "CLK_{0}_MUL".format(pll),
                                                                    "CLK_{0}_FRACR".format(pll)])
        
        pll_pmc_frequency = clk_component.createIntegerSymbol("{0}_FREQUENCY".format(pll), pll_menu)
        pll_pmc_frequency.setReadOnly(True)
        if pll_en.getValue() == True:
            pll_pmc_frequency.setDefaultValue(int(round(pll_core_frequency.getValue() / (pll_divpmc.getValue() + 1), -2)))
        else:
            pll_pmc_frequency.setDefaultValue(0)
        pll_pmc_frequency.setDependencies(update_pll_pmc_freq, ["CLK_{0}_EN".format(pll),
                                                                "{0}_CORE_FREQUENCY".format(pll),
                                                                "CLK_{0}_DIVPMC".format(pll)])

        #if PLL has an IO clock
        if pll_default_config_dict.get(pll)["ioclock"]:
            pll_divio_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL0"]/bitfield@[name="DIVIO"]')
            pll_divio = clk_component.createIntegerSymbol("CLK_{0}_DIVIO".format(pll), pll_en)
            pll_divio.setLabel(pll_divio_node.getAttribute("name"))
            pll_divio.setDescription(pll_divio_node.getAttribute("caption"))
            pll_divio.setMin(0)
            pll_divio.setMax(255)

            pll_enio_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PLL_CTRL0"]/bitfield@[name="ENIOPLLCK"]')
            pll_enio = clk_component.createBooleanSymbol("CLK_{0}_ENIOPLLCK".format(pll), pll_en)
            pll_enio.setLabel(pll_enio_node.getAttribute("name"))
            pll_enio.setDescription(pll_enio_node.getAttribute("caption"))
            pll_enio.setDefaultValue(False)
        
            pll_io_frequency = clk_component.createIntegerSymbol("{0}_IO_FREQUENCY".format(pll), pll_menu)
            pll_io_frequency.setReadOnly(True)
            if pll_enio.getValue() == True:
                pll_io_frequency.setDefaultValue(int(pll_core_frequency.getValue() / (pll_divio.getValue() + 1)))
            else:
                pll_io_frequency.setDefaultValue(0)
            pll_io_frequency.setDependencies(update_pll_pmc_freq, ["CLK_{0}_ENIOPLLCK".format(pll),
                                                                   "{0}_CORE_FREQUENCY".format(pll),
                                                                   "CLK_{0}_DIVIO".format(pll)])
                                                     

    #Processor Clock
    cpu_menu = clk_component.createMenuSymbol("CLK_CPU_MENU", menu)
    cpu_menu.setLabel("Processor Clock")

    cpu_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="CSS"]')
    cpu_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_css_node.getAttribute("values")+'"]')
    cpu_css = clk_component.createKeyValueSetSymbol("CLK_CPU_CKR_CSS", cpu_menu)
    cpu_css.setLabel(cpu_css_node.getAttribute("name"))
    cpu_css.setDescription(cpu_css_node.getAttribute("caption"))
    cpu_css.setDisplayMode("Key")
    cpu_css.setOutputMode("Key")
    for value in cpu_css_vg_node.getChildren():
        cpu_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    cpu_css.setDefaultValue(2)

    cpu_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="PRES"]')
    cpu_pres_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_pres_node.getAttribute("values")+'"]')
    cpu_pres = clk_component.createKeyValueSetSymbol("CLK_CPU_CKR_PRES", cpu_menu)
    cpu_pres.setLabel(cpu_pres_node.getAttribute("name"))
    cpu_pres.setDescription(cpu_pres_node.getAttribute("caption"))
    cpu_pres.setDisplayMode("Key")
    cpu_pres.setOutputMode("Key")
    for value in cpu_pres_vg_node.getChildren():
        cpu_pres.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    cpu_pres.setDefaultValue(0)

    cpu_mdiv_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_CKR"]/bitfield@[name="MDIV"]')
    cpu_mdiv_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+cpu_mdiv_node.getAttribute("values")+'"]')
    cpu_mdiv = clk_component.createKeyValueSetSymbol("CLK_CPU_CKR_MDIV", cpu_menu)
    cpu_mdiv.setLabel(cpu_mdiv_node.getAttribute("name"))
    cpu_mdiv.setDescription(cpu_mdiv_node.getAttribute("caption"))
    cpu_mdiv.setDisplayMode("Key")
    cpu_mdiv.setOutputMode("Key")
    for value in cpu_mdiv_vg_node.getChildren():
        cpu_mdiv.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
    cpu_mdiv.setDefaultValue(2)

    cpu_ratio_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_CPU_RATIO"]/bitfield@[name="RATIO"]')
    cpu_ratio = clk_component.createIntegerSymbol("CLK_CPU_RATIO", cpu_menu)
    cpu_ratio.setLabel(cpu_ratio_node.getAttribute("name"))
    cpu_ratio.setDescription(cpu_ratio_node.getAttribute("caption"))
    cpu_ratio.setMax(15)
    cpu_ratio.setMin(0)
    cpu_ratio.setDefaultValue(15)

    fclk_freq = clk_component.createIntegerSymbol("FCLK_FREQUENCY", cpu_menu)
    fclk_freq.setReadOnly(True)
    if cpu_css.getSelectedKey() == "SLOW_CLK":
        src_freq = md_slck.getValue()
    elif cpu_css.getSelectedKey() == "MAIN_CLK":
        src_freq = mainck.getValue()
    elif cpu_css.getSelectedKey() == "CPUPLLCK":
        src_freq = clk_remote_component.getSymbolValue("CPUPLL_FREQUENCY")
    else:
        src_freq = clk_remote_component.getSymbolValue("SYSPLL_FREQUENCY")
        
    pres_value = int(cpu_pres.getSelectedKey().split("CLK_")[1])
    fclk_freq.setDefaultValue(src_freq/pres_value)
    fclk_freq.setDependencies(update_fclk_freq, ["MAINCK_FREQUENCY", "CPUPLL_FREQUENCY", "SYSPLL_FREQUENCY", "CLK_CPU_CKR_PRES"])

    cpu_freq = clk_component.createIntegerSymbol("CPU_CLOCK_FREQUENCY", cpu_menu)
    cpu_freq.setReadOnly(True)
    cpu_freq.setDefaultValue((fclk_freq.getValue() * (cpu_ratio.getValue() + 1)) / 16)
    cpu_freq.setDependencies(update_cpu_clk_freq, ["FCLK_FREQUENCY", "CLK_CPU_RATIO"])

    mck0_freq = clk_component.createIntegerSymbol("MCK0_FREQUENCY", cpu_menu)
    mck0_freq.setReadOnly(True)
    mck0_freq.setDefaultValue(fclk_freq.getValue()/(int(cpu_mdiv.getSelectedKey().split("PCK_DIV")[1])))
    mck0_freq.setDependencies(update_mck0_freq, ["FCLK_FREQUENCY", "CLK_CPU_CKR_MDIV"])
    
    
    #MCKx clocks
    mckx_config_dict = {1: [["MD_SLOW_CLK", "MAINCK", "MCK0", "SYSPLL"],"SYSPLL", "MASTER_DIV2"],
                2: [["DDRPLL"], "DDRPLL", 0],
                3: [["MD_SLOW_CLK", "MAINCK", "MCK0", "SYSPLL", "DDRPLL", "IMGPLL"], "MD_SLOW_CLK", "MASTER_DIV1"],
                4: [["MD_SLOW_CLK", "MAINCK", "MCK0", "SYSPLL"], "SYSPLL", "MASTER_DIV1"]
                }
    
    mckx_menu = clk_component.createMenuSymbol("CLK_MCKx_MENU", menu)
    mckx_menu.setLabel("MCKx Clock")

    mckx_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_MCR"]/bitfield@[name="CSS"]')
    mckx_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mckx_css_node.getAttribute("values")+'"]')
    
    mckx_div_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_MCR"]/bitfield@[name="DIV"]')
    mckx_div_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+mckx_div_node.getAttribute("values")+'"]')
    for x in range(1, 5):
        mckx_css =clk_component.createKeyValueSetSymbol("CLK_MCR_MCK{0}_CSS".format(x), mckx_menu)
        mckx_css.setLabel("MCK{0}_CSS".format(x))
        mckx_css.setDescription("Clock source selection for MCK{0}".format(x))
        index = 0
        default = 0
        for value in mckx_css_vg_node.getChildren():
            if value.getAttribute("name") in mckx_config_dict[x][0]:
                mckx_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
                if value.getAttribute("name") == mckx_config_dict[x][1]:
                    default = index
                index = index + 1
        mckx_css.setDisplayMode("Key")
        mckx_css.setOutputMode("Key")
        mckx_css.setDefaultValue(default)

        mckx_div = clk_component.createKeyValueSetSymbol("CLK_MCR_MCK{0}_DIV".format(x), mckx_menu)
        mckx_div.setLabel("MCK{0}_DIV".format(x))
        mckx_div.setDescription("Divisor value for MCK{0}".format(x))
        index = 0
        default = 0
        for value in mckx_div_vg_node.getChildren():
            mckx_div.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
            if value.getAttribute("name") == mckx_config_dict[x][2]:
                default = index
            index = index + 1
        mckx_div.setDisplayMode("Key")
        mckx_div.setOutputMode("Key")
        mckx_div.setDefaultValue(default)
        mckx_freq = clk_component.createIntegerSymbol("MCK{0}_FREQUENCY".format(x), mckx_menu)
        mckx_freq.setReadOnly(True)

        mckx_src_freq = clk_remote_component.getSymbolValue(mckx_css.getSelectedKey() + "_FREQUENCY")
        mckx_divisor = int(mckx_div.getSelectedKey().split("MASTER_DIV")[1])
        mckx_freq.setDefaultValue(mckx_src_freq/mckx_divisor)

        mckx_freq_deps = ["CLK_MCR_MCK{0}_CSS".format(x), "CLK_MCR_MCK{0}_DIV".format(x)]
        for src in mckx_config_dict[x][0]:
            mckx_freq_deps.append(src + "_FREQUENCY")
        mckx_freq.setDependencies(update_mckx_freq, mckx_freq_deps)

    
    #Set bootloader defaults to the clock generator
    if bootloader_clocks.getValue():
        setup_bootloader_defaults(bootloader_clocks.getComponent(), True)

    # Programmable clock Menu
    pck_menu = clk_component.createMenuSymbol("CLK_PCK_MENU", menu)
    pck_menu.setLabel("PCK")
    pck_menu.setDescription("Programmable Clocks")
    
    num_pcks = int(ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]').getAttribute("count"))
    num_pckx_sym = clk_component.createIntegerSymbol("CLK_NUM_PCKS", pck_menu)
    num_pckx_sym.setVisible(False)
    num_pckx_sym.setDefaultValue(num_pcks)

    for pckx in range(0, num_pcks):
        pckx_freq_deps = []
        pckx_en = clk_component.createBooleanSymbol("CLK_PCK"+str(pckx)+"_EN", pck_menu)
        pckx_en.setLabel("Enable PCK"+str(pckx))
        pckx_freq_deps.append(pckx_en.getID())

        pckx_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="CSS"]')
        pckx_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+pckx_css_node.getAttribute("values")+'"]')
        pckx_css = clk_component.createKeyValueSetSymbol("CLK_PCK"+str(pckx)+"_CSS", pckx_en)
        pckx_css.setLabel(pckx_css_node.getAttribute("name"))
        pckx_css.setDescription(pckx_css_node.getAttribute("caption"))
        pckx_css.setDisplayMode("Key")
        pckx_css.setOutputMode("Key")
        for value in pckx_css_vg_node.getChildren():
            pckx_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
            pckx_freq_deps.append(value.getAttribute("name") + "_FREQUENCY")
        pckx_freq_deps.append(pckx_css.getID())

        pckx_pres_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCK"]/bitfield@[name="PRES"]')
        pckx_pres = clk_component.createIntegerSymbol("CLK_PCK"+str(pckx)+"_PRES", pckx_en)
        pckx_pres.setLabel(pckx_pres_node.getAttribute("name"))
        pckx_pres.setDescription(pckx_pres_node.getAttribute("caption"))
        pckx_pres.setMin(0)
        pckx_pres.setMax(255)
        pckx_freq_deps.append(pckx_pres.getID())

        pckx_freq = clk_component.createIntegerSymbol("CLK_PCK"+str(pckx)+"_FREQUENCY", pckx_en)
        pckx_freq.setReadOnly(True)
        input_freq = 0
        if pckx_en.getValue() == True:
            input_freq = pckx_freq.getComponent().getSymbolValue(pckx_css.getKey(pckx_css.getValue())+"_FREQUENCY")
        pckx_freq.setDefaultValue(input_freq / (pckx_pres.getValue() + 1))
 
        pckx_freq.setDependencies(update_pck_freq, pckx_freq_deps)

    #peripheral clock controller
    pcr_menu = clk_component.createMenuSymbol("CLK_PCR_MENU", menu)
    pcr_menu.setLabel("Peripheral Clocks")

    gclk_menu = clk_component.createMenuSymbol("CLK_GCLK_MENU", menu)
    gclk_menu.setLabel("Generic Clocks")

    gclk_map = {    "ADC": (["SYSPLL", "BAUDPLL", "AUDIOPLL"], 100, setup_adc_arm_clock_frequency),
                    "ARM": (["SYSPLL", "DDRPLL"], 50, setup_adc_arm_clock_frequency),
                    "ASRC": (["AUDIOPLL"], 200, setup_generic_gclk_module_clock_frequency),
                    "CSI": (["DDRPLL", "IMGPLL"], 27, setup_generic_gclk_module_clock_frequency),
                    "FLEXCOM": (["SYSPLL", "BAUDPLL"], 200, setup_generic_gclk_module_clock_frequency),
                    "GEMAC": (["ETHPLL"], 125, setup_generic_gclk_module_clock_frequency),
                    "I2SMCC": (["SYSPLL", "AUDIOPLL"], 100, setup_generic_gclk_module_clock_frequency),
                    "MCAN": (["SYSPLL", "BAUDPLL"], 200, setup_mcan_clock_frequency),
                    "PDMC":(["SYSPLL", "AUDIOPLL"], 50, setup_generic_gclk_module_clock_frequency),
                    "PIT64B": (["SYSPLL", "IMGPLL", "BAUDPLL", "AUDIOPLL", "ETHPLL"], 200, setup_pit64b_clock_frequency),
                    "QSPI": (["SYSPLL", "BAUDPLL"], 200, setup_generic_gclk_module_clock_frequency),
                    "SDMMC": (["SYSPLL", "BAUDPLL"], 200, setup_sdmmc_clock_frequency),
                    "SPDIFRX": (["SYSPLL", "AUDIOPLL"], 150, setup_generic_gclk_module_clock_frequency),
                    "SPDIFTX": (["SYSPLL", "AUDIOPLL"], 25, setup_generic_gclk_module_clock_frequency),
                    "TC": (["SYSPLL", "IMGPLL", "BAUDPLL", "AUDIOPLL", "ETHPLL"], 200, setup_tc_clock_frequency),
                    "TCPC":([], 0.32, setup_generic_gclk_module_clock_frequency)
                    }
    
    #Create map of name->id's for Java code to know what peripheral supports generic clocks
    generic_clocks_map = coreComponent.createKeyValueSetSymbol("GCLK_INSTANCE_PID", gclk_menu)
    generic_clocks_map.setVisible(False)
    generic_clocks_map.addKey("ADC", "26", "")

    peripherals_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
    max_clock_id = 0
    for module_node in peripherals_node.getChildren():
        module_name = module_node.getAttribute("name")
        mck_id = get_peripheral_clock_id(module_name)
        for instance_node in module_node.getChildren():
            instance_name = instance_node.getAttribute("name")
            parameters_node = instance_node.getChildrenByName("parameters")
            if len(parameters_node) > 0:
                for param_node in parameters_node[0].getChildren():
                    if param_node.getAttribute("name").startswith("CLOCK_ID"):
                        clock_id  = param_node.getAttribute("value")
                        clock_id_suffix = instance_name + param_node.getAttribute("name").split("CLOCK_ID")[1] 
                        pcr_en = clk_component.createBooleanSymbol(clock_id_suffix + "_CLOCK_ENABLE", pcr_menu)
                        pcr_en.setLabel(clock_id_suffix)

                        if int(clock_id) > max_clock_id:
                            max_clock_id = int(clock_id)

                        id_name_map = clk_component.createStringSymbol("CLK_ID_NAME_" + clock_id, pcr_menu)
                        id_name_map.setVisible(False)
                        id_name_map.setDefaultValue(clock_id_suffix)
                        
                        if module_node.getAttribute("name") not in gclk_map.keys():
                            pcr_freq = clk_component.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", pcr_menu)
                            pcr_freq.setVisible(False)
                            pcr_freq.setDefaultValue(clk_remote_component.getSymbolValue("MCK{0}_FREQUENCY".format(mck_id)))
                            pcr_freq.setDependencies(lambda symbol, event: symbol.setValue(event["value"]),
                             ['MCK{0}_FREQUENCY'.format(mck_id)])
                        
                        if module_name  in gclk_map.keys():
                            if module_name not in ["TC0", "TC1"] or clock_id_suffix.endswith("CHANNEL0"):
                                generic_clocks_map.addKey(instance_name, clock_id, "")

            if module_name  in gclk_map.keys():
                gclk_periph = clk_component.createMenuSymbol(None, gclk_menu)
                gclk_periph.setLabel(instance_name)
                gclk_srcs = gclk_map[module_name][0]
                gclk_freq_deps = [src + "_FREQUENCY" for src in gclk_srcs]

                gclk_en = clk_component.createBooleanSymbol("CLK_"+instance_name+"_GCLKEN", gclk_periph)
                gclk_en.setLabel("Enable")
                gclk_freq_deps.append(gclk_en.getID())

                gclk_css_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKCSS"]')
                gclk_css_vg_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="'+gclk_css_node.getAttribute("values")+'"]')
                gclk_css = clk_component.createKeyValueSetSymbol("CLK_" + instance_name + "_GCLKCSS", gclk_periph)
                gclk_css.setLabel(gclk_css_node.getAttribute("name"))
                gclk_css.setDescription(gclk_css_node.getAttribute("caption"))
                gclk_css.setDisplayMode("Key")
                gclk_css.setOutputMode("Value")
                if module_name == "TCPC":
                    value = gclk_css_vg_node.getChildren()[0]
                    gclk_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
                else:
                    for value in gclk_css_vg_node.getChildren():
                        if "PLL" not in value.getAttribute("name") or value.getAttribute("name") in gclk_srcs:
                            gclk_css.addKey(value.getAttribute("name"), value.getAttribute("value"), value.getAttribute("caption"))
                gclk_freq_deps.append(gclk_css.getID())

                gclk_div_node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/register-group@[name="PMC"]/register@[name="PMC_PCR"]/bitfield@[name="GCLKDIV"]')
                gclk_div = clk_component.createIntegerSymbol("CLK_"+instance_name+"_GCLKDIV", gclk_periph)
                gclk_div.setLabel(gclk_div_node.getAttribute("name"))
                gclk_div.setDescription(gclk_div_node.getAttribute("caption"))
                gclk_div.setMin(0)
                gclk_div.setMax(255)
                gclk_freq_deps.append(gclk_div.getID())

                gclk_freq = clk_component.createIntegerSymbol(instance_name+"_GCLK_FREQUENCY", gclk_periph)
                gclk_freq.setReadOnly(True)
                input_freq = 0
                if gclk_en.getValue() == True:
                    input_freq = gclk_freq.getComponent().getSymbolValue(gclk_css.getSelectedKey()+"_FREQUENCY")
                gclk_freq.setDefaultValue(input_freq / (gclk_div.getValue() + 1))
                gclk_freq.setDependencies(update_gclk_freq, gclk_freq_deps)

                #create module specific gclk dependencies
                gclk_map[module_name][2](clk_component, clk_remote_component, module_name, instance_name) 

    
    max_clock_id_sym = clk_component.createIntegerSymbol("CLK_MAX_PERIPHERAL_ID", pcr_menu)
    max_clock_id_sym.setVisible(False)
    max_clock_id_sym.setDefaultValue(max_clock_id)

    system_counter_menu = clk_component.createMenuSymbol("CLK_SYSTEM_COUNTER_MENU", menu)
    system_counter_menu.setLabel("System Counter")

    system_counter_enable = clk_component.createBooleanSymbol("SYSTEM_COUNTER_ENABLE", system_counter_menu)
    system_counter_enable.setLabel("Enable System Counter")
    system_counter_enable.setDefaultValue(True)

    system_counter_frequency = clk_component.createIntegerSymbol("SYSTEM_COUNTER_FREQUENCY", system_counter_menu)
    system_counter_frequency.setLabel("System counter frequency")
    system_counter_frequency.setReadOnly(True)
    system_counter_frequency.setDefaultValue(clk_remote_component.getSymbolValue("MAINCK_FREQUENCY"))
    system_counter_frequency.setDependencies(update_timestamp_frequency, ["SYSTEM_COUNTER_ENABLE", "MAINCK_FREQUENCY"])
       
    config = Variables.get("__CONFIGURATION_NAME")

    cfile = clk_component.createFileSymbol("CLK_C", None)
    cfile.setSourcePath("../peripheral/clk_sam_a7g5/templates/plib_clk.c.ftl")
    cfile.setOutputName("plib_clk.c")
    cfile.setDestPath("/peripheral/clk/")
    cfile.setProjectPath("config/"+config+"/peripheral/clk/")
    cfile.setType("SOURCE")
    cfile.setMarkup(True)

    hfile = clk_component.createFileSymbol("CLK_H", None)
    hfile.setSourcePath("../peripheral/clk_sam_a7g5/templates/plib_clk.h.ftl")
    hfile.setOutputName("plib_clk.h")
    hfile.setDestPath("/peripheral/clk/")
    hfile.setProjectPath("config/"+config+"/peripheral/clk/")
    hfile.setType("HEADER")
    hfile.setMarkup(True)

    # Add clock related code to common files
    sys_def_list = clk_component.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    sys_def_list.setType("STRING")
    sys_def_list.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sys_def_list.setSourcePath("../peripheral/clk_sam_a7g5/templates/system/definitions.h.ftl")
    sys_def_list.setMarkup(True)

    sys_init_list = clk_component.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    sys_init_list.setType("STRING")
    sys_init_list.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    sys_init_list.setSourcePath("../peripheral/clk_sam_a7g5/templates/system/initialization.c.ftl")
    sys_init_list.setMarkup(True)
