
from os.path import join
from xml.etree import ElementTree

global generic_list
#UART, SPI, and TWI peripherals claim to be able to use GCLK but aren't in table 33-1
generic_list = ["FLEXCOM0", "FLEXCOM1", "FLEXCOM2", "FLEXCOM3", "FLEXCOM4", "TC0", "TC1", "ADC", "LCDC", "I2SC0", "I2SC1", "MCAN0", "MCAN1", "CLASSD"]

# Peripherals connected to 64 bit AHB matrix (i.e. with HS bus clocks)
hs_peripherals_list = ["XDMAC0", "XDMAC1", "AESB", "MPDDRC", "SDMMC0", "SDMMC1", "LCDC", "ISC", "QSPI0", "QSPI1"]

# Peripherals supporting multiple clock options
multi_clock_peripheral_list = ["TC"]

global CLK_SAMA5D2_CONSTANTS_DICT
CLK_SAMA5D2_CONSTANTS_DICT = {  "SLOW_RC_OSC_FREQ":32000,
                                "SLOW_XTAL_OSC_FREQ":32768,
                                "MAIN_RC_OSC_FREQ":12000000,
                                "EXT_OSC_MIN_FREQ":8000000,
                                "EXT_OSC_DEFAULT_FREQ":12000000,
                                "EXT_OSC_MAX_FREQ":24000000,
                                "PLLA_MULA_MIN":1,
                                "PLLA_MULA_MAX":128,
                                "PLLA_MULA_DEFAULT":83,
                                "PLLA_DEFAULT_FREQ":498000000,
                                "UTMI_PLL_FREQ":480000000,
                                "PCLOCK_LS_MAX_FREQ":83000000}

global CLK_SAMA5D2_UTMI_MUL_DICT
CLK_SAMA5D2_UTMI_MUL_DICT= {12000000:0, 16000000:1, 20000000:2}

global SAMA5D2_USE_BOOTLOADER_CLOCKS
SAMA5D2_USE_BOOTLOADER_CLOCKS = True

global clk_sama5d2_symbol_dict
clk_sama5d2_symbol_dict = {}


global DICT_PCER0
global DICT_PCER1


global set_symbol_value_from_atdf
def set_symbol_value_from_atdf(symbol, module_name, value_group_name):
    atdf_path = "/avr-tools-device-file/modules/module@[name=\"" + module_name + "\"]/value-group@[name=\"" +\
                                                                                        value_group_name+ "\"]"
    node = ATDF.getNode(atdf_path)
    value = node.getChildren()
    for index in range(len(value)):
        symbol.addKey(value[index].getAttribute("name"),
                      value[index].getAttribute("value"),
                      value[index].getAttribute("caption"))



global update_slow_clock_frequency
def update_slow_clock_frequency(symbol, event):

    source_key = clk_sama5d2_symbol_dict["SCK_CR_OSCSEL"].getSelectedKey()
    #Possible values of the source key are "RC" or "XTAL"
    symbol.setValue(CLK_SAMA5D2_CONSTANTS_DICT["SLOW_" + source_key + "_OSC_FREQ"], 2)

global update_main_clock_frequency
def update_main_clock_frequency(symbol, event):

    #main crystal frequency is editable only if the crystal or bypass is enabled
    if clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTEN"].getValue() == True or \
                clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTBY"].getValue() == True:
        clk_sama5d2_symbol_dict["MAIN_CRYSTAL_FREQUENCY"].setReadOnly(False)
    else:
        clk_sama5d2_symbol_dict["MAIN_CRYSTAL_FREQUENCY"].setReadOnly(True)

    # Display a warning if the corresponding oscillators/clocks are not enabled
    if clk_sama5d2_symbol_dict["CKGR_MOR_MOSCSEL"].getSelectedKey() == "XTAL":
        show_warning = (clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTEN"].getValue() == False and \
                        clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTBY"].getValue() == False)

    else:
        show_warning = (clk_sama5d2_symbol_dict["CKGR_MOR_MOSCRCEN"].getValue() == False)

    clk_sama5d2_symbol_dict["MAIN_CLK_INVALID_COMMENT"].setVisible(show_warning)

    #if crystal is selected, use the frequency configured by the user else use embedded RC frequency.
    if clk_sama5d2_symbol_dict["CKGR_MOR_MOSCSEL"].getSelectedKey() == "XTAL":
        main_clk_freq = clk_sama5d2_symbol_dict["MAIN_CRYSTAL_FREQUENCY"].getValue()
        lock_moscxtst = False
    else:
        main_clk_freq = CLK_SAMA5D2_CONSTANTS_DICT["MAIN_RC_OSC_FREQ"]
        lock_moscxtst = True

    symbol.setValue(main_clk_freq, 2)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTST"].setReadOnly(lock_moscxtst)

global update_plla_clock_frequency
def update_plla_clock_frequency(symbol, event):
    #base frequency
    plla_freq =  clk_sama5d2_symbol_dict["MAIN_CLK_FREQUENCY"].getValue()

    #input divider
    plla_freq /= int(clk_sama5d2_symbol_dict["CKGR_PLLAR_DIVA"].getValue())

    #output multiplier
    plla_freq *= clk_sama5d2_symbol_dict["CKGR_PLLA_MULA"].getValue()

    #second divider
    plla_freq /= int(clk_sama5d2_symbol_dict["CKGR_PLLAR_PLLDIVA2"].getValue())

    symbol.setValue(plla_freq, 2)

global update_utmi_clock_frequency
def update_utmi_clock_frequency(symbol, event):
    show_warning = False
    #if UPLL is enabled
    if clk_sama5d2_symbol_dict["CKGR_UCKR_UPLLEN"].getValue() == True:
        #Get the required multiplier to get a valid UPLL frequency of 480 MHz
        plla_freq = clk_sama5d2_symbol_dict["MAIN_CLK_FREQUENCY"].getValue()
        multiplier = CLK_SAMA5D2_UTMI_MUL_DICT.get(plla_freq)

        #If the multiplier is not supported, then display warning
        if multiplier == None:
            show_warning = True
        else:
            clk_sama5d2_symbol_dict["SFR_UTMICKTRIM_FREQ"].setValue(multiplier, 2)

    clk_sama5d2_symbol_dict["CLK_UTMI_INVALID_MAIN_CLOCK"].setVisible(show_warning)

global update_processor_clock_frequency
def update_processor_clock_frequency(symbol, event):

    clock_source = clk_sama5d2_symbol_dict["PMC_MCKR_CSS"].getSelectedKey()
    input_frequency = Database.getSymbolValue("core", clock_source + "_FREQUENCY")

    prescaler = clk_sama5d2_symbol_dict["PMC_MCKR_PRES"].getSelectedKey()

    # Key can be CLOCK or CLOCK_DIV{n}
    divisor = 1 if "_DIV" not in prescaler else int(prescaler.split("_DIV")[1])

    symbol.setValue(input_frequency/divisor, 2)

global update_master_clock_frequency
def update_master_clock_frequency(symbol, event):
    # MCK clock source
    clock_source = clk_sama5d2_symbol_dict["PMC_MCKR_CSS"].getSelectedKey()

    # PLLA divider
    plladiv2 = clk_sama5d2_symbol_dict["CKGR_PLLAR_PLLDIVA2"].getValue()

    # MCK divider
    mck_divider_key = clk_sama5d2_symbol_dict["PMC_MCKR_MDIV"].getSelectedKey()

    #PLLA invalid clock warning
    show_invalid_plla_warning = (clock_source == "PLLA_CLK") and (plladiv2 != "2") and (mck_divider_key == "PCK_DIV3")
    clk_sama5d2_symbol_dict["CLK_MCK_DIV_INVALID"].setVisible(show_invalid_plla_warning)

    #Processor clock frequency
    input_frequency = clk_sama5d2_symbol_dict["PROCESSOR_CLOCK_FREQUENCY"].getValue()

    #find the divider (named as EQ_PCK or PCK_DIV{n})
    if "_DIV" not in mck_divider_key:
        divisor = 1
    else:
        divisor = int(mck_divider_key.split("_DIV")[1])

    #calculate the output frequency
    output_frequency = input_frequency / divisor

    #set the master clock frequency
    symbol.setValue(output_frequency, 2)

    #set the DDR clock frequency
    clk_sama5d2_symbol_dict["DDR_CLOCK_FREQUENCY"].setValue(output_frequency, 2)
    clk_sama5d2_symbol_dict["CLK_DDR_CLOCK_INVALID"].setVisible(divisor < 2)

    #set the High speed bus clock frequency
    clk_sama5d2_symbol_dict["PCLOCK_HS_CLOCK_FREQUENCY"].setValue( output_frequency, 2)

global update_pclock_ls_frequency
def update_pclock_ls_frequency(symbol,event):
    input_frequency = clk_sama5d2_symbol_dict["MASTER_CLOCK_FREQUENCY"].getValue()

    #symbol is named as H32MXDIV{n}
    divisor = int(clk_sama5d2_symbol_dict["PMC_MCKR_H32MXDIV"].getSelectedKey().split("DIV")[1])

    output_frequency = input_frequency / divisor
    symbol.setValue(output_frequency, 2)

    show_warning = output_frequency > CLK_SAMA5D2_CONSTANTS_DICT["PCLOCK_LS_MAX_FREQ"]
    clk_sama5d2_symbol_dict["CLK_PCLOCK_LS_INVALID"].setVisible(show_warning)

def update_peripheral_clock_frequencies(symbol, event):
    symbol.setValue(int(event["value"]), 2)

def update_tc_clock_frequency(symbol, event):
    #symbol is named as "TC{instance_number}_CH{channel_number}_CLOCK_FREQUENCY.
    #Extract the instance number
    tcInstance = symbol.getID().split("TC")[1].split("_")[0]
    #extract the channel number
    chInstance = symbol.getID().split("_CH")[1].split("_")[0]

    #check if the relevant channel is enabled
    if (Database.getSymbolValue("tc" + str(tcInstance), "TC" + str(chInstance) + "_ENABLE") == True):
        #Find the current clock source for the channel
        clk_src = Database.getSymbolValue("tc" + str(tcInstance), "TC" + str(chInstance) + "_CMR_TCCLKS")
        #if clock source is MCK (Enabled through extended registers of TC)
        if (clk_src == 0):
            symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"), 2)
        #if clock source is processor independent GCLK
        elif (clk_src == 1):
            symbol.setValue(Database.getSymbolValue("core", "TC" + str(tcInstance) + "GENERIC_CLOCK_FREQUENCY"), 2)
        #if clock  source is MCK/8
        elif (clk_src == 2):
            symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")/8, 2)
        # if clock  source is MCK/32
        elif (clk_src == 3):
            symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")/32, 2)
        # if clock  source is MCK/128
        elif (clk_src == 4):
            symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY") / 128, 2)
        # if clock  source is SLOW CLOCK
        elif (clk_src == 5):
            symbol.setValue(Database.getSymbolValue("core", "SLOW_CLK_FREQUENCY"), 2)
        #set MCK/8 as the default value
        else:
            symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY") / 8, 2)

# if any channel of TC instance is enabled, enable the peripheral clock of that instance
global update_tc_clock_enable
def update_tc_clock_enable(symbol, event):
    tcInstance = symbol.getID()[2]
    enable_clock = False
    for channel in range(3):
        symbol_id = "TC" + str(tcInstance) + "_CHANNEL" + str(channel) + "_CLOCK_ENABLE"
        if (Database.getSymbolValue("core", symbol_id) == True):
            enable_clock = True
            break
    symbol.setValue(enable_clock, 2)

global update_clk_component_visability
def update_clk_component_visability(clk_comp, event):
    if event["value"] is True:
        clk_comp.setVisible(True)
    else:
        clk_comp.setVisible(False)

def __update_pcer0_value(pmc_pcer0, perip_clk):
    """
    Calculates PCER0 register value after enabling/disabling
    the peripheral clock with peripheral identifiers less than 32.

    pmc_pcer0: PMC PCER0 register hex symbol handle
    perip_clk: peripheral clock event dictionary
    """
    global DICT_PCER0

    pcer0 = pmc_pcer0.getValue()

    if perip_clk["value"] is True:
        pmc_pcer0.setValue(pcer0 | (1 << DICT_PCER0[perip_clk["id"]]), 1)
    else:
        pmc_pcer0.setValue(pcer0 & ~(1 << DICT_PCER0[perip_clk["id"]]), 1)

def __update_pcer1_value(pmc_pcer1, perip_clk):
    """
    Calculates PCER1 register value after enabling/disabling
    the peripheral clock with peripheral identifiers greater than 31.

    pmc_pcer1: PMC PCER1 register hex symbol handle
    perip_clk: peripheral clock event dictionary
    """
    global DICT_PCER1

    pcer1 = pmc_pcer1.getValue()

    if perip_clk["value"] is True:
        pmc_pcer1.setValue(pcer1 | (1 << (DICT_PCER1[perip_clk["id"]] % 32)), 1)
    else:
        pmc_pcer1.setValue(pcer1 & ~(1 << (DICT_PCER1[perip_clk["id"]] % 32)), 1)

def __slow_clock_menu(clk_comp, clk_menu):
    """
       Slow Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """

    # creates Slow Clock Configuration Menu
    slow_clk_menu = clk_comp.createMenuSymbol("CLK_SLOW_MENU", clk_menu)
    slow_clk_menu.setLabel("Slow Clock Configuration")

    #create slow clock selector symbol
    sym_slow_clock_selector = clk_comp.createKeyValueSetSymbol("SCK_CR_OSCSEL", slow_clk_menu)
    sym_slow_clock_selector.setLabel("Slow Clock Selector")

    #Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_slow_clock_selector, "SCKC", "SCKC_CR__OSCSEL")

    #set RC as the default value
    sym_slow_clock_selector.setDefaultValue(1)
    clk_sama5d2_symbol_dict["SCK_CR_OSCSEL"] = sym_slow_clock_selector

    #symbol identifying the slow clock frequency
    sym_clk_slow = clk_comp.createIntegerSymbol("SLOW_CLK_FREQUENCY", slow_clk_menu)
    sym_clk_slow.setLabel("Slow Clock (Hz)")
    sym_clk_slow.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["SLOW_XTAL_OSC_FREQ"])
    sym_clk_slow.setReadOnly(True)
    clk_sama5d2_symbol_dict["SLOW_CLK_FREQUENCY"] = sym_clk_slow
    sym_clk_slow.setDependencies(update_slow_clock_frequency, ["SCK_CR_OSCSEL"])

def __main_clock_menu(clk_comp, clk_menu):
    """
       Main Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """

    #main clock menu
    main_clock_menu = clk_comp.createMenuSymbol("CLK_MAIN_MENU", clk_menu)
    main_clock_menu.setLabel("Main clock configuration")

    #symbol for the main crystal oscillator enable
    sym_main_xtal_osc_enable = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCXTEN", main_clock_menu)
    sym_main_xtal_osc_enable.setLabel("External oscillator enable")
    sym_main_xtal_osc_enable.setDefaultValue(True)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTEN"] = sym_main_xtal_osc_enable

    #symbol for main crystal oscillator bypass
    sym_main_xtal_osc_bypass = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCXTBY", main_clock_menu)
    sym_main_xtal_osc_bypass.setLabel("External oscillator bypass")
    sym_main_xtal_osc_bypass.setDefaultValue(False)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTBY"] = sym_main_xtal_osc_bypass

    #symbol for main crystal/clock input frequency
    sym_main_xtal_input_frequency = clk_comp.createIntegerSymbol("MAIN_CRYSTAL_FREQUENCY", main_clock_menu)
    sym_main_xtal_input_frequency.setLabel("External oscillator/clock frequency")
    sym_main_xtal_input_frequency.setMin(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_MIN_FREQ"])
    sym_main_xtal_input_frequency.setMax(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_MAX_FREQ"])
    sym_main_xtal_input_frequency.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_DEFAULT_FREQ"])
    clk_sama5d2_symbol_dict["MAIN_CRYSTAL_FREQUENCY"] = sym_main_xtal_input_frequency

    #symbol for main crystal stabilization cycle count
    sym_main_xtal_stabilization_count = clk_comp.createIntegerSymbol("CKGR_MOR_MOSCXTST", main_clock_menu)
    sym_main_xtal_stabilization_count.setLabel("Main crystal stabilization count ( value x 8 SCLK cycles)")
    sym_main_xtal_stabilization_count.setMin(0)
    sym_main_xtal_stabilization_count.setMax(255)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCXTST"] = sym_main_xtal_stabilization_count

    #symbol for main RC oscillator enable
    sym_rc_osc_enable = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCRCEN", main_clock_menu)
    sym_rc_osc_enable.setLabel("Embedded RC oscillator enable")
    sym_rc_osc_enable.setDefaultValue(False)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCRCEN"] = sym_rc_osc_enable

    #symbol for main clock selection
    sym_main_clk_selection = clk_comp.createKeyValueSetSymbol("CKGR_MOR_MOSCSEL", main_clock_menu)
    sym_main_clk_selection.setLabel("Main clock source selection")
    sym_main_clk_selection.addKey("RC", "0", "")
    sym_main_clk_selection.addKey("XTAL", "1", "")
    sym_main_clk_selection.setDefaultValue(1)
    clk_sama5d2_symbol_dict["CKGR_MOR_MOSCSEL"] = sym_main_clk_selection

    #symbol for main clock frequency
    sym_main_clk_freq = clk_comp.createIntegerSymbol("MAIN_CLK_FREQUENCY", main_clock_menu)
    sym_main_clk_freq.setLabel("Main Clock Frequency(Hz)")
    sym_main_clk_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_DEFAULT_FREQ"])
    sym_main_clk_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["MAIN_CLK_FREQUENCY"] = sym_main_clk_freq

    #symbol for invalid clock source comment
    sym_main_clk_src_invalid = clk_comp.createCommentSymbol("MAIN_CLK_INVALID_COMMENT", main_clock_menu)
    sym_main_clk_src_invalid.setLabel("Oscillator/clock for current selection is not enabled !!!")
    sym_main_clk_src_invalid.setVisible(False)
    clk_sama5d2_symbol_dict["MAIN_CLK_INVALID_COMMENT"] = sym_main_clk_src_invalid

def __plla_clock_menu(clk_comp, clk_menu):
    """
       PLLA Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """
    #plla clock menu
    plla_clock_menu = clk_comp.createMenuSymbol("CLK_PLLA_MENU", clk_menu)
    plla_clock_menu.setLabel("PLLA clock configuration")

    #symbol for PLLA enable ( There is no corresponding register bit , it just sets MULA value to 0)
    sym_plla_enable = clk_comp.createBooleanSymbol("CKGR_PLLAR_MULA0", plla_clock_menu)
    sym_plla_enable.setLabel("PLLA Enable")
    sym_plla_enable.setDefaultValue(True)
    clk_sama5d2_symbol_dict["CKGR_PLLAR_MULA0"] = sym_plla_enable

    #symbol for PLLA input divider
    sym_plla_input_divider = clk_comp.createComboSymbol("CKGR_PLLAR_DIVA", plla_clock_menu, ["1", "2"])
    sym_plla_input_divider.setLabel("PLLA input divider")
    clk_sama5d2_symbol_dict["CKGR_PLLAR_DIVA"] = sym_plla_input_divider

    #symbol for output multiplier
    sym_plla_multiplier = clk_comp.createIntegerSymbol("CKGR_PLLA_MULA", plla_clock_menu)
    sym_plla_multiplier.setLabel("PLLA multiplier")
    sym_plla_multiplier.setMin(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_MIN"])
    sym_plla_multiplier.setMax(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_MAX"])
    sym_plla_multiplier.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_DEFAULT"])
    clk_sama5d2_symbol_dict["CKGR_PLLA_MULA"] = sym_plla_multiplier

    #symbol for output divider
    sym_plla_output_divider = clk_comp.createComboSymbol("CKGR_PLLAR_PLLDIVA2", plla_clock_menu, ["1", "2"])
    sym_plla_output_divider.setLabel("PLLA output divider")
    sym_plla_output_divider.setDefaultValue("2")
    clk_sama5d2_symbol_dict["CKGR_PLLAR_PLLDIVA2"] = sym_plla_output_divider

    #symbol for stabilization count
    sym_plla_stabilization_count = clk_comp.createIntegerSymbol("CKGR_PLLAR_PLLACOUNT", plla_clock_menu)
    sym_plla_stabilization_count.setLabel("PLLA stabilization count (in SCLK cycles)")
    sym_plla_stabilization_count.setMin(0)
    sym_plla_stabilization_count.setMax(63)
    clk_sama5d2_symbol_dict["CKGR_PLLAR_PLLACOUNT"] = sym_plla_stabilization_count

    #symbol for output clock frequency
    sym_clk_plla_freq = clk_comp.createIntegerSymbol("PLLA_CLK_FREQUENCY", plla_clock_menu)
    sym_clk_plla_freq.setLabel("PLL Clock (Hz)")
    sym_clk_plla_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_DEFAULT_FREQ"])
    sym_clk_plla_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["PLLA_CLK_FREQUENCY"] = sym_clk_plla_freq

def __utmi_pll_clock_menu(clk_comp, clk_menu):
    """
       UTMI Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """
    #utmi clock menu
    utmi_clock_menu = clk_comp.createMenuSymbol("CLK_UTMI_PLL_MENU", clk_menu)
    utmi_clock_menu.setLabel("UTMI clock menu")

    #utmi clock enable
    sym_utmi_pllen = clk_comp.createBooleanSymbol("CKGR_UCKR_UPLLEN", utmi_clock_menu)
    sym_utmi_pllen.setLabel("UTMI PLL enable")
    sym_utmi_pllen.setDefaultValue(True)
    clk_sama5d2_symbol_dict["CKGR_UCKR_UPLLEN"] = sym_utmi_pllen

    #utmi clock trimming
    sym_utmi_cktrim = clk_comp.createKeyValueSetSymbol("SFR_UTMICKTRIM_FREQ", utmi_clock_menu)
    sym_utmi_cktrim.addKey("x40", "0" ,"12MHz Reference Clock")
    sym_utmi_cktrim.addKey("x30", "1", "16MHz Reference Clock")
    sym_utmi_cktrim.addKey("x20", "2", "20MHz Reference Clock")
    sym_utmi_cktrim.setLabel("Main clock multiplication factor")
    sym_utmi_cktrim.setDefaultValue(0)
    sym_utmi_cktrim.setReadOnly(True)
    clk_sama5d2_symbol_dict["SFR_UTMICKTRIM_FREQ"] = sym_utmi_cktrim

    #utmi invalid main clock comment
    sym_utmi_invalid_comment = clk_comp.createCommentSymbol("CLK_UTMI_INVALID_MAIN_CLOCK", utmi_clock_menu)
    sym_utmi_invalid_comment.setLabel("Current main clock cannot generate a valid UTMI clock of 480 MHz !!!")
    sym_utmi_invalid_comment.setVisible(False)
    clk_sama5d2_symbol_dict["CLK_UTMI_INVALID_MAIN_CLOCK"] = sym_utmi_invalid_comment

    #utmi clock frequency symbol
    sym_clk_utmi_freq = clk_comp.createIntegerSymbol("UPLL_CLK_FREQUENCY", utmi_clock_menu)
    sym_clk_utmi_freq.setLabel("UTMI clock frequency(Hz)")
    sym_clk_utmi_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["UTMI_PLL_FREQ"])
    sym_clk_utmi_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["UPLL_CLK_FREQUENCY"] = sym_clk_utmi_freq

def __master_clock_menu(clk_comp, clk_menu):
    """
       Master Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """

    #master clock menu
    master_clock_menu = clk_comp.createMenuSymbol("CLK_MASTER_MENU", clk_menu)
    master_clock_menu.setLabel("Master clock menu")

    #MCK source selector
    sym_mck_source_selector  = clk_comp.createKeyValueSetSymbol("PMC_MCKR_CSS", master_clock_menu)
    sym_mck_source_selector.setLabel("MCK source selector")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_source_selector, "PMC", "PMC_MCKR__CSS")
    sym_mck_source_selector.setDefaultValue(2)
    clk_sama5d2_symbol_dict["PMC_MCKR_CSS"] = sym_mck_source_selector

    #MCK source pre-scaler
    sym_mck_prescaler = clk_comp.createKeyValueSetSymbol("PMC_MCKR_PRES", master_clock_menu)
    sym_mck_prescaler.setLabel("MCK prescaler")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_prescaler, "PMC", "PMC_MCKR__PRES")
    clk_sama5d2_symbol_dict["PMC_MCKR_PRES"] = sym_mck_prescaler

    #Processor clock frequency
    sym_processor_clk_freq = clk_comp.createIntegerSymbol("PROCESSOR_CLOCK_FREQUENCY", master_clock_menu)
    sym_processor_clk_freq.setLabel("Processor Clock Frequency (HZ)")
    sym_processor_clk_freq.setDefaultValue(clk_sama5d2_symbol_dict["PLLA_CLK_FREQUENCY"].getValue())
    sym_processor_clk_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["PROCESSOR_CLOCK_FREQUENCY"] = sym_processor_clk_freq

    #MCK divider
    sym_mck_divider = clk_comp.createKeyValueSetSymbol("PMC_MCKR_MDIV", master_clock_menu)
    sym_mck_divider.setLabel("MCK divider")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_divider, "PMC", "PMC_MCKR__MDIV")
    sym_mck_divider.setDefaultValue(3)
    clk_sama5d2_symbol_dict["PMC_MCKR_MDIV"] = sym_mck_divider

    sym_invalid_mck_divider = clk_comp.createCommentSymbol("CLK_MCK_DIV_INVALID", master_clock_menu)
    sym_invalid_mck_divider.setLabel("If MCK divider is 3 and processor clock source is PLLA, PLLA2 divider " +
                                                                            "should be enabled !!!")
    sym_invalid_mck_divider.setVisible(False)
    clk_sama5d2_symbol_dict["CLK_MCK_DIV_INVALID"] = sym_invalid_mck_divider

    #Master clock frequency
    sym_master_clk_freq = clk_comp.createIntegerSymbol("MASTER_CLOCK_FREQUENCY", master_clock_menu)
    sym_master_clk_freq.setLabel("Master Clock Frequency (HZ)")
    sym_master_clk_freq.setDefaultValue(clk_sama5d2_symbol_dict["PLLA_CLK_FREQUENCY"].getValue()/sym_mck_divider.getValue())
    sym_master_clk_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["MASTER_CLOCK_FREQUENCY"] = sym_master_clk_freq

    #DDR clock frequency
    sym_ddr_clk_freq = clk_comp.createIntegerSymbol("DDR_CLOCK_FREQUENCY", master_clock_menu)
    sym_ddr_clk_freq.setLabel("DDR clock Frequency (Hz)")
    sym_ddr_clk_freq.setDefaultValue(sym_master_clk_freq.getValue())
    sym_ddr_clk_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["DDR_CLOCK_FREQUENCY"] = sym_ddr_clk_freq

    #DDR clock invalid comment
    sym_ddr_clk_invalid_comment = clk_comp.createCommentSymbol("CLK_DDR_CLOCK_INVALID", master_clock_menu)
    sym_ddr_clk_invalid_comment.setLabel("DDR clock is invalid when the master clock is equal to processor clock !!!")
    sym_ddr_clk_invalid_comment.setVisible(False)
    clk_sama5d2_symbol_dict["CLK_DDR_CLOCK_INVALID"] = sym_ddr_clk_invalid_comment

    sym_periph_hs_clk_freq = clk_comp.createIntegerSymbol("PCLOCK_HS_CLOCK_FREQUENCY", master_clock_menu)
    sym_periph_hs_clk_freq.setLabel("H64MX bus clock (HZ)")
    sym_periph_hs_clk_freq.setDefaultValue(sym_master_clk_freq.getValue())
    sym_periph_hs_clk_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["PCLOCK_HS_CLOCK_FREQUENCY"] = sym_periph_hs_clk_freq

    #Low speed bus clock divider
    sym_h32mx_divider = clk_comp.createKeyValueSetSymbol("PMC_MCKR_H32MXDIV", master_clock_menu)
    sym_h32mx_divider.setLabel("H32MX divider")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_h32mx_divider, "PMC", "PMC_MCKR__H32MXDIV")
    sym_h32mx_divider.setDefaultValue(1)
    clk_sama5d2_symbol_dict["PMC_MCKR_H32MXDIV"] = sym_h32mx_divider

    #Low speed bus clock frequency
    sym_periph_clk_ls_freq = clk_comp.createIntegerSymbol("PCLOCK_LS_CLOCK_FREQUENCY", master_clock_menu)
    sym_periph_clk_ls_freq.setLabel("H32MX bus clock(HZ)")
    sym_periph_clk_ls_freq.setDefaultValue(sym_master_clk_freq.getDefaultValue()/2)
    sym_periph_clk_ls_freq.setReadOnly(True)
    clk_sama5d2_symbol_dict["PCLOCK_LS_CLOCK_FREQUENCY"] = sym_periph_clk_ls_freq

    #Low speed bus clock invalid comment
    sym_pclock_ls_invalid_comment = clk_comp.createCommentSymbol("CLK_PCLOCK_LS_INVALID", master_clock_menu)
    sym_pclock_ls_invalid_comment.setLabel("H32MX bus clock cannot be higher than 83 MHz !!!")
    sym_pclock_ls_invalid_comment.setVisible(False)
    clk_sama5d2_symbol_dict["CLK_PCLOCK_LS_INVALID"] = sym_pclock_ls_invalid_comment

def __audio_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Audio Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for Master Clock Menu.
    audio_clk_menu = clk_comp.createMenuSymbol("CLK_AUDIO", clk_menu)
    audio_clk_menu.setLabel("Audio PLL Configuration")
    audio_clk_menu.setDescription("Configure Audio PLL CLock")

    # get PMC Register Group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_AUDIO_PLLx registers
    reg_pmc_audio_pll0 = pmc_reg_group.getRegister("PMC_AUDIO_PLL0")
    reg_pmc_audio_pll1 = pmc_reg_group.getRegister("PMC_AUDIO_PLL1")

    #get bitfields
    bitfield_pmc_audio_pll0_pllen = reg_pmc_audio_pll0.getBitfield("PLLEN")
    bitfield_pmc_audio_pll0_qdpmc = reg_pmc_audio_pll0.getBitfield("QDPMC")
    bitfield_pmc_audio_pll0_nd = reg_pmc_audio_pll0.getBitfield("ND")
    bitfield_pmc_audio_pll0_pmcen = reg_pmc_audio_pll0.getBitfield("PMCEN")
    bitfield_pmc_audio_pll0_paden = reg_pmc_audio_pll0.getBitfield("PADEN")
    bitfield_pmc_audio_pll1_qdaudio = reg_pmc_audio_pll1.getBitfield("QDAUDIO")
    bitfield_pmc_audio_pll1_div = reg_pmc_audio_pll1.getBitfield("DIV")
    bitfield_pmc_audio_pll1_fracr = reg_pmc_audio_pll1.getBitfield("FRACR")

    #get values
    bitfield_pmc_audio_pll1_div_values = pmc_reg_module.getValueGroup(bitfield_pmc_audio_pll1_div.getValueGroupName())

    # create symbols
    sym_pllen = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PLLEN", audio_clk_menu)
    sym_pllen.setLabel(bitfield_pmc_audio_pll0_pllen.getDescription())
    sym_pllen.setDefaultValue(False)

    sym_qdpmc = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL0_QDPMC", sym_pllen)
    sym_qdpmc.setLabel(bitfield_pmc_audio_pll0_qdpmc.getDescription())
    sym_qdpmc.setMin(0)
    sym_qdpmc.setMax(127)
    sym_qdpmc.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_qdpmc.setVisible(False)

    sym_nd = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL0_ND", sym_pllen)
    sym_nd.setLabel(bitfield_pmc_audio_pll0_nd.getDescription())
    sym_nd.setMin(0)
    sym_nd.setMax(127)
    sym_nd.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_nd.setVisible(False)

    sym_qdaudio = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL1_QDAUDIO", sym_pllen)
    sym_qdaudio.setLabel(bitfield_pmc_audio_pll1_qdaudio.getDescription())
    sym_qdaudio.setMin(1)
    sym_qdaudio.setMax(31)
    sym_qdaudio.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_qdaudio.setVisible(False)

    sym_div = clk_comp.createKeyValueSetSymbol("PMC_AUDIO_PLL1_DIV", sym_pllen)
    sym_div.setLabel(bitfield_pmc_audio_pll1_div.getDescription())
    sym_div.setOutputMode("Value")
    sym_div.setDisplayMode("Description")
    for name in bitfield_pmc_audio_pll1_div_values.getValueNames():
        value = bitfield_pmc_audio_pll1_div_values.getValue(name)
        sym_div.addKey(value.getName(), value.getValue(), value.getDescription())
    sym_div.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_div.setVisible(False)

    sym_fracr = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL1_FRACR", sym_pllen)
    sym_fracr.setLabel(bitfield_pmc_audio_pll1_fracr.getDescription())
    sym_fracr.setMin(0)
    sym_fracr.setMax(65535)
    sym_fracr.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_fracr.setVisible(False)

    sym_pmcen = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PMCEN", sym_pllen)
    sym_pmcen.setLabel(bitfield_pmc_audio_pll0_pmcen.getDescription())
    sym_pmcen.setDefaultValue(False)
    sym_pmcen.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_pmcen.setVisible(False)

    sym_paden = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PADEN", sym_pllen)
    sym_paden.setLabel(bitfield_pmc_audio_pll0_paden.getDescription())
    sym_paden.setDefaultValue(False)
    sym_paden.setDependencies(update_clk_component_visability, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_paden.setVisible(False)

def __usb_clock_menu(clk_comp, clk_menu, pmc_reg_module, sfr_reg_module):
    """
    USB Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    sfr_reg_module: SFR Register Module
    update_upll_divider_visibility: Callback to enable/disable UPLL Divider visibility
    """
    # create symbol for USB Clock Menu
    usb_clk_menu = clk_comp.createMenuSymbol("CLK_USB", clk_menu)
    usb_clk_menu.setLabel("USB Clock Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get CKGR_UCKR register
    reg_ckgr_uckr = pmc_reg_group.getRegister("CKGR_UCKR")

    # get UPLLEN Bitfield of CKGR_UCKR register
    bitfield_ckgr_uckr_upllen = reg_ckgr_uckr.getBitfield("UPLLEN")

    # create symbol for UPLLEN Bitfield of CKGR_UCKR register
    sym_ckgr_uckr_upllen = clk_comp.createBooleanSymbol("PMC_CKGR_UCKR_UPLLEN", usb_clk_menu)
    sym_ckgr_uckr_upllen.setLabel(bitfield_ckgr_uckr_upllen.getDescription())

    # UPLLCOUNT
    bitfield_ckgr_uckr_upllcount = reg_ckgr_uckr.getBitfield("UPLLCOUNT")

    sym_ckgr_uckr_upllcount = clk_comp.createIntegerSymbol("PMC_CKGR_UCKR_UPLLCOUNT", sym_ckgr_uckr_upllen)
    sym_ckgr_uckr_upllcount.setLabel(bitfield_ckgr_uckr_upllcount.getDescription())
    sym_ckgr_uckr_upllcount.setDefaultValue(15)
    sym_ckgr_uckr_upllcount.setMin(0)
    sym_ckgr_uckr_upllcount.setMax(15)
    sym_ckgr_uckr_upllcount.setVisible(False)
    sym_ckgr_uckr_upllcount.setDependencies(update_clk_component_visability, ["PMC_CKGR_UCKR_UPLLEN"])

    # get UTMI register group
    sfr_reg_group = sfr_reg_module.getRegisterGroup("SFR")

    # get UTMI_CKTRIM register
    reg_sfr_cktrim = sfr_reg_group.getRegister("SFR_UTMICKTRIM")

    # get FREQ bitfield of UTMI_CKTRIM register
    bitfield_sfr_cktrim_freq = reg_sfr_cktrim.getBitfield("FREQ")

    # get value group for FREQ bitfield of UTMI_CKTRIM register
    valgrp_sfr_cktrim_freq = sfr_reg_module.getValueGroup(bitfield_sfr_cktrim_freq.getValueGroupName())

    # create symbol for FREQ bitfield of UTMI_CKTRIM register
    sym_sfr_cktrim_freq = clk_comp.createComboSymbol("UTMI_CKTRIM_FREQ", sym_ckgr_uckr_upllen, valgrp_sfr_cktrim_freq.getValueNames())
    sym_sfr_cktrim_freq.setDefaultValue("_12")
    sym_sfr_cktrim_freq.setVisible(False)

    # get PMC_SCER register
    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")

    # get UDP bitfield of PMC_SCER register
    bitfield_pmc_scer_udpclk = reg_pmc_scer.getBitfield("UDP")

    # get symbol for UDPCLK bitfield of PMC_SCER register
    sym_pmc_scer_udp = clk_comp.createBooleanSymbol("PMC_SCER_UDPCLK", usb_clk_menu)
    sym_pmc_scer_udp.setLabel(bitfield_pmc_scer_udpclk.getDescription())

    # get UHP bitfield of PMC_SCER register
    bitfield_pmc_scer_uhpclk = reg_pmc_scer.getBitfield("UHP")

    # get symbol for UDPCLK bitfield of PMC_SCER register
    sym_pmc_scer_uhpclk = clk_comp.createBooleanSymbol("PMC_SCER_UHPCLK", usb_clk_menu)
    sym_pmc_scer_uhpclk.setLabel(bitfield_pmc_scer_uhpclk.getDescription())

    # get PMC_USB register
    reg_pmc_usb = pmc_reg_group.getRegister("PMC_USB")

    # get USBS bitfield of PMC_USB register
    bitfield_pmc_usb_usbs = reg_pmc_usb.getBitfield("USBS")

    # create symbol for USBS bitfield of PMC_USB register
    sym_pmc_usb_usbs = clk_comp.createComboSymbol("PMC_USB_USBS", clk_menu, ["PLLA_CLK", "UPLL_CLK"])
    sym_pmc_usb_usbs.setLabel(bitfield_pmc_usb_usbs.getDescription())
    sym_pmc_usb_usbs.setDefaultValue("UPLL_CLK")

    # get USBDIV bitfield of PMC_USB register
    bitfield_pmc_usb_usbdiv = reg_pmc_usb.getBitfield("USBDIV")

    # create symbol for USBDIV bitfield of PMC_USB register
    sym_usb_divider = clk_comp.createIntegerSymbol("PMC_USB_USBDIV", usb_clk_menu)
    sym_usb_divider.setLabel(bitfield_pmc_usb_usbdiv.getDescription())
    sym_usb_divider.setMin(1)
    sym_usb_divider.setMax(16)
    sym_usb_divider.setDefaultValue(10)

    #USB clock frequencies
    sym_usb_fs_freq = clk_comp.createStringSymbol("USBFS_CLOCK_FREQUENCY", usb_clk_menu)
    sym_usb_fs_freq.setLabel("USB Clock Frequency (HZ)")
    sym_usb_fs_freq.setDefaultValue("48000000")
    sym_usb_fs_freq.setReadOnly(True)

    sym_usb_hs_freq = clk_comp.createStringSymbol("USBHS_CLOCK_FREQUENCY", usb_clk_menu)
    sym_usb_hs_freq.setLabel("USB High Speed Clock Frequency (HZ)")
    sym_usb_hs_freq.setDefaultValue("480000000")
    sym_usb_hs_freq.setReadOnly(True)

def __generic_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Generic Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for generic clock
    generic_clk_menu = clk_comp.createMenuSymbol("CLK_GENERIC", clk_menu)
    generic_clk_menu.setLabel("Generic Clock Generator Configuration for select peripherals")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_PCR register
    reg_pmc_pcr = pmc_reg_group.getRegister("PMC_PCR")

    #for periph in ["FLEXCOM0", "FLEXCOM1", "FLEXCOM2", "FLEXCOM3", "FLEXCOM4", "TC0", "TC1", "ADC", "LCDC", "I2SC0", "I2SC1", "MCAN0", "MCAN1", "CLASSD"]:
    for periph in generic_list:
        module = periph
        if module[-1:].isdigit():
            module = module[:-1]
        node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\""+module+"\"]/instance@[name=\""+periph+"\"]")
        if node is None:
            print "Unable to locate periph " + periph
            continue
        i = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\""+module+"\"]/instance@[name=\""+periph+"\"]/parameters/param@[name=\"INSTANCE_ID\"]").getAttribute("value")

        # create menu for Peripheral/Generic Clock
        sym_gclkx_menu = clk_comp.createMenuSymbol("CLK_GEN" + str(i), generic_clk_menu)
        sym_gclkx_menu.setLabel("Generic Clock for Peripheral " + periph)

        # get GCLKEN bitfield of PMC_PCR register
        bitfield_pmc_pcr_gclken = reg_pmc_pcr.getBitfield("GCKEN")

        # create symbol for GCLKEN bitfield of PMC_PCR register
        sym_pmc_pcr_gclken = clk_comp.createBooleanSymbol("PMC_PCR_GCLK" + str(i) + "EN", sym_gclkx_menu)
        sym_pmc_pcr_gclken.setLabel(bitfield_pmc_pcr_gclken.getDescription())

        # get GCLKDIV bitfield of PMC_PCR register
        bitfield_pmc_pcr_gckdiv = reg_pmc_pcr.getBitfield("GCKDIV")

        # create symbol for GCLKDIV bitfield of PMC_PCR register
        sym_pmc_pcr_gckdiv = clk_comp.createIntegerSymbol("PMC_PCR_GCK" + str(i) + "DIV", sym_gclkx_menu)
        sym_pmc_pcr_gckdiv.setLabel(bitfield_pmc_pcr_gckdiv.getDescription())
        sym_pmc_pcr_gckdiv.setMin(0)
        sym_pmc_pcr_gckdiv.setMax(255)
        sym_pmc_pcr_gckdiv.setDefaultValue(1)
        sym_pmc_pcr_gckdiv.setVisible(False)
        sym_pmc_pcr_gckdiv.setDependencies(update_clk_component_visability, ["PMC_PCR_GCLK" + str(i) + "EN"])

        # get GCKCSS bitfield of PMC_PCR register
        bitfield_pmc_pcr_gckcss = reg_pmc_pcr.getBitfield("GCKCSS")
        bitfield_pmc_pcr_gckcss_values = pmc_reg_module.getValueGroup(bitfield_pmc_pcr_gckcss.getValueGroupName())

        # create symbol for GCLKCSS bitfield of PMC_PCR register
        sym_pmc_pcr_gckcss = clk_comp.createKeyValueSetSymbol("PMC_PCR_GCK" + str(i) + "CSS", sym_gclkx_menu)
        sym_pmc_pcr_gckcss.setLabel(bitfield_pmc_pcr_gckcss.getDescription())
        for name in bitfield_pmc_pcr_gckcss_values.getValueNames():
            value = bitfield_pmc_pcr_gckcss_values.getValue(name)
            sym_pmc_pcr_gckcss.addKey(value.getName(), value.getValue(), value.getDescription())
        sym_pmc_pcr_gckcss.setVisible(False)
        sym_pmc_pcr_gckcss.setOutputMode("Value")
        sym_pmc_pcr_gckcss.setDisplayMode("Key")
        sym_pmc_pcr_gckcss.setSelectedKey("SLOW_CLK",1)
        sym_pmc_pcr_gckcss.setDependencies(update_clk_component_visability, ["PMC_PCR_GCLK" + str(i) + "EN"])

        #calculated generic clock frequency
        gen_clk_freq = clk_comp.createIntegerSymbol(periph + "_GENERIC_CLOCK_FREQUENCY", sym_gclkx_menu)
        gen_clk_freq.setLabel(periph + " Generic Clock Frequency (HZ)")
        gen_clk_freq.setDefaultValue(166000000)
        gen_clk_freq.setReadOnly(True)

def __peripheral_clock_menu(clk_comp, clk_menu, join_path, element_tree, update_pcer0_value, update_pcer1_value):
    """
    Peripheral Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    join_path: function used to create os independent paths
    element_tree: XML parser library
    update_pcer0_value: Callback to calculate PCER0 Register Value.
    update_pcer1_value: Callback to calculate PCER1 Register Value.
    """

    global DICT_PCER0
    global DICT_PCER1

    DICT_PCER0 = {}
    DICT_PCER1 = {}

    list_pcer0_depend = []
    list_pcer1_depend = []

    # create symbol for peripheral clock
    clk_menu = clk_comp.createMenuSymbol("CLK_PERIPHERAL", clk_menu)
    clk_menu.setLabel("Peripheral Clock Enable Configuration")

    atdf_file_path = join_path(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")

    atdf_file = open(atdf_file_path, "r")
    atdf_content = element_tree.fromstring(atdf_file.read())

    # parse atdf xml file to get instance name
    # for the peripheral which has clock id
    for peripheral in atdf_content.iter("module"):
        for instance in peripheral.iter("instance"):
                
            for param in instance.iter("param"):
                if "CLOCK_ID" in param.attrib["name"]:

                    symbol_id = instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1]
                    sym_perip_clk = clk_comp.createBooleanSymbol(symbol_id + "_CLOCK_ENABLE", clk_menu)
                    sym_perip_clk.setLabel(symbol_id)
                    sym_perip_clk.setDefaultValue(False)
                    sym_perip_clk.setReadOnly(True)

                    clock_id = int(param.attrib["value"])

                    if clock_id < 32:
                        list_pcer0_depend.append(symbol_id + "_CLOCK_ENABLE")
                        DICT_PCER0.update({""+symbol_id+"_CLOCK_ENABLE": clock_id})
                    else:
                        list_pcer1_depend.append(symbol_id + "_CLOCK_ENABLE")
                        DICT_PCER1.update({""+symbol_id+"_CLOCK_ENABLE": clock_id})

                    # SAMA5D2 has only one peripheral clock associated with each timer instance. Other masks provide
                    # clocks per channel of an instance. The current design of the TC plib expects symbols per
                    # channel. For compatibility we create symbols per channel which are are added as dependency
                    # for the instance symbols
                    if peripheral.attrib["name"] == "TC":
                        tc_enable_dependent_list =[]

                        #create a dummy symbol per channel
                        for channel_number in range(3):
                            tc_enable_symbol_id = instance.attrib["name"] + "_CHANNEL" + str(channel_number) + "_CLOCK_ENABLE"
                            tc_channel_enable_symbol = clk_comp.createBooleanSymbol(tc_enable_symbol_id, None)
                            tc_channel_enable_symbol.setVisible(False)
                            tc_channel_enable_symbol.setReadOnly(True)
                            tc_channel_enable_symbol.setDefaultValue(False)
                            tc_enable_dependent_list.append("core." + tc_enable_symbol_id)

                        sym_perip_clk.setDependencies(update_tc_clock_enable, tc_enable_dependent_list)


    # create symbol for PMC_PCERx register values
    sym_pmc_pcer0 = clk_comp.createHexSymbol("PMC_PCER0", clk_menu)
    sym_pmc_pcer0.setVisible(False)
    sym_pmc_pcer0.setDefaultValue(00000000)
    sym_pmc_pcer0.setDependencies(update_pcer0_value, list_pcer0_depend)

    # create symbol for PMC_PCERx register values
    sym_pmc_pcer1 = clk_comp.createHexSymbol("PMC_PCER1", clk_menu)
    sym_pmc_pcer1.setVisible(False)
    sym_pmc_pcer1.setDefaultValue(00000000)
    sym_pmc_pcer1.setDependencies(update_pcer1_value, list_pcer1_depend)

#Programmable Clock generator configuration options
def __programmable_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Programmable Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for Programmable clock menu
    clk_menu = clk_comp.createMenuSymbol("CLK_PROGRAMMABLE", clk_menu)
    clk_menu.setLabel("Programmable Clock Generator Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_SCER register
    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")

    # get PMC_PCK# register
    reg_pmc_pck = pmc_reg_group.getRegister("PMC_PCK")

    # menu for 3 programmable clock
    for i in range(0, 3, 1):

        # create symbol for programmable clock #
        sym_prog_clk_menu = clk_comp.createMenuSymbol("CLK_PROGRAMMABLE_" + str(i), clk_menu)
        sym_prog_clk_menu.setLabel("Programmable Clock " + str(i) + " Generator Configuration")

        # get PCK# bitfield of PMC_SCER Register
        bitfield_pmc_scer_pck = reg_pmc_scer.getBitfield("PCK" + str(i))

        # create symbol for PCK# bitfield of PMC_SCER Register
        sym_pmc_scer_pck = clk_comp.createBooleanSymbol("PMC_SCER_PCK" + str(i), sym_prog_clk_menu)
        sym_pmc_scer_pck.setLabel(bitfield_pmc_scer_pck.getDescription())

        # get CSS bitfield of PMC_PCK# register
        bitfield_pmc_pck_css = reg_pmc_pck.getBitfield("CSS")

        # get Value Group for CSS bitfield of PMC_PCK# register
        valgrp_pmc_pck_css = pmc_reg_module.getValueGroup(bitfield_pmc_pck_css.getValueGroupName())

        # create symbol for CSS bitfield of PMC_PCK# register
        sym_pmc_pck_css = clk_comp.createComboSymbol("PMC_PCK" + str(i) + "_CSS", sym_pmc_scer_pck, valgrp_pmc_pck_css.getValueNames())
        sym_pmc_pck_css.setLabel(bitfield_pmc_pck_css.getDescription())
        sym_pmc_pck_css.setDefaultValue("SLOW_CLK")
        sym_pmc_pck_css.setVisible(False)
        sym_pmc_pck_css.setDependencies(update_clk_component_visability, ["PMC_SCER_PCK"+str(i)])

        # get PRES bitfield of PMC_PCK# register
        bitfield_pmc_pck_pres = reg_pmc_pck.getBitfield("PRES")

        # create symbol for PRES bitfield of PMC_PCK# register
        sym_pmc_pck_pres = clk_comp.createIntegerSymbol("PMC_PCK" + str(i) +"_PRES", sym_pmc_scer_pck)
        sym_pmc_pck_pres.setLabel(bitfield_pmc_pck_pres.getDescription())
        sym_pmc_pck_pres.setMin(1)
        sym_pmc_pck_pres.setMax(256)
        sym_pmc_pck_pres.setDefaultValue(1)
        sym_pmc_pck_pres.setVisible(False)
        sym_pmc_pck_pres.setDependencies(update_clk_component_visability, ["PMC_SCER_PCK"+str(i)])

    #calculated PCK frequencies
    sym_pck0_freq = clk_comp.createStringSymbol("PCK0_CLOCK_FREQUENCY", sym_prog_clk_menu)
    sym_pck0_freq.setLabel("Programmable clock #0 Frequency (HZ)")
    sym_pck0_freq.setDefaultValue("12000000")
    sym_pck0_freq.setReadOnly(True)

    sym_pck1_freq = clk_comp.createStringSymbol("PCK1_CLOCK_FREQUENCY", sym_prog_clk_menu)
    sym_pck1_freq.setLabel("Programmable clock #1 Frequency (HZ)")
    sym_pck1_freq.setDefaultValue("6000000")
    sym_pck1_freq.setReadOnly(True)

    sym_pck2_freq = clk_comp.createStringSymbol("PCK2_CLOCK_FREQUENCY", sym_prog_clk_menu)
    sym_pck2_freq.setLabel("Programmable clock #2 Frequency (HZ)")
    sym_pck2_freq.setDefaultValue("4000000")
    sym_pck2_freq.setReadOnly(True)

def __lcd_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    LCD Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """

    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    #enables LCDCK but clock PID and selection is all done in LCD module
    lcd_menu = clk_comp.createMenuSymbol("LCDCK", clk_menu)
    lcd_menu.setLabel("LCD Clock Configuration")

    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")
    bitfield_pmc_scer_lcdck = reg_pmc_scer.getBitfield("LCDCK")

    sym_lcdclk = clk_comp.createBooleanSymbol("PMC_SCER_LCDCK", lcd_menu)
    sym_lcdclk.setLabel(bitfield_pmc_scer_lcdck.getDescription())
    sym_lcdclk.setDefaultValue(False)

def __isc_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    ISC Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """

    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    #enables ISC but clock PID and selection is all done in LCD module
    isc_menu = clk_comp.createMenuSymbol("ISCCK", clk_menu)
    isc_menu.setLabel("ISC Clock Configuration")

    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")
    bitfield_pmc_scer_iscck = reg_pmc_scer.getBitfield("ISCCK")

    sym_iscclk = clk_comp.createBooleanSymbol("PMC_SCER_ISCCK", isc_menu)
    sym_iscclk.setLabel(bitfield_pmc_scer_iscck.getDescription())
    sym_iscclk.setDefaultValue(False)

#Add menu symbol dependencies
def set_clock_symbol_dependencies():

    #slow clock frequency dependencies
    clk_sama5d2_symbol_dict["SLOW_CLK_FREQUENCY"].setDependencies(update_slow_clock_frequency, ["SCK_CR_OSCSEL"])

    #main clock frequency symbol dependencies
    clk_sama5d2_symbol_dict["MAIN_CLK_FREQUENCY"].setDependencies(update_main_clock_frequency,
                                                                   ["CKGR_MOR_MOSCXTEN",
                                                                    "CKGR_MOR_MOSCXTBY",
                                                                    "MAIN_CRYSTAL_FREQUENCY",
                                                                    "CKGR_MOR_MOSCRCEN",
                                                                    "CKGR_MOR_MOSCSEL"])
    #PLLA clock frequency dependencies
    clk_sama5d2_symbol_dict["PLLA_CLK_FREQUENCY"].setDependencies(update_plla_clock_frequency,
                                                                   ["CKGR_PLLAR_MULA0",
                                                                    "CKGR_PLLAR_DIVA",
                                                                    "CKGR_PLLA_MULA",
                                                                    "CKGR_PLLAR_PLLDIVA2"])

    #UTMI clock symbol dependencies
    clk_sama5d2_symbol_dict["SFR_UTMICKTRIM_FREQ"].setDependencies(update_utmi_clock_frequency,
                                                                  ["CKGR_UCKR_UPLLEN",
                                                                   "MAIN_CLK_FREQUENCY"])

    #Processor clock symbol dependencies
    clk_sama5d2_symbol_dict["PROCESSOR_CLOCK_FREQUENCY"].setDependencies(update_processor_clock_frequency,
                                                                           ["PMC_MCKR_CSS",
                                                                            "PMC_MCKR_PRES",
                                                                            "SLOW_CLK_FREQUENCY",
                                                                            "MAIN_CLK_FREQUENCY",
                                                                            "PLLA_CLK_FREQUENCY",
                                                                            "UPLL_CLK_FREQUENCY"])

    #Master clock symbol dependencies
    clk_sama5d2_symbol_dict["MASTER_CLOCK_FREQUENCY"].setDependencies(update_master_clock_frequency,
                                                                      ["PROCESSOR_CLOCK_FREQUENCY",
                                                                       "PMC_MCKR_MDIV"])

    #Low speed bus clock symbol dependencies
    clk_sama5d2_symbol_dict["PCLOCK_LS_CLOCK_FREQUENCY"].setDependencies(update_pclock_ls_frequency,
                                                                      ["MASTER_CLOCK_FREQUENCY",
                                                                       "PMC_MCKR_H32MXDIV"])


#Lock all fixed clock menus
def use_fixed_clocks():

    for name, symbol in clk_sama5d2_symbol_dict.items():
        if symbol.getType() != "Comment":
            symbol.setReadOnly(True)


if __name__ == "__main__":
    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_SAM_A5D2", None)
    SYM_CLK_MENU.setLabel("Clock (PMC)")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    #Uncomment when plugin is available
    #CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    #CLK_MANAGER_SELECT.setVisible(False)
    #CLK_MANAGER_SELECT.setDefaultValue("SAME70:SAME70ClockModel")

    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

    PMC_REGISTERS = Register.getRegisterModule("PMC")
    SCKC_REGISTERS = Register.getRegisterModule("SCKC")
    SFR_REGISTERS = Register.getRegisterModule("SFR")

    #Slow clock
    __slow_clock_menu(coreComponent, SYM_CLK_MENU)

    #Main clock
    __main_clock_menu(coreComponent, SYM_CLK_MENU)

    #PLLA clock
    __plla_clock_menu(coreComponent, SYM_CLK_MENU)

    #UTMI clock
    __utmi_pll_clock_menu(coreComponent, SYM_CLK_MENU)

    #Master clock
    __master_clock_menu(coreComponent, SYM_CLK_MENU)

    # Audio PLL
    __audio_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates programmable clock menu
    __programmable_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates generic clock menu
    __generic_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates peripheral clock menu
    __peripheral_clock_menu(coreComponent, SYM_CLK_MENU, join, ElementTree, __update_pcer0_value, __update_pcer1_value)

    # LCDC Clock Controller
    __lcd_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # ISC clock controller
    __isc_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates usb clock
    __usb_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS, SFR_REGISTERS)

    #If the system is configured to use clocks set by bootloader, do not allow the
    #user to modify the clock sources for processor and peripherals
    if SAMA5D2_USE_BOOTLOADER_CLOCKS == True:
        use_fixed_clocks()
    #else enable dependency callbacks for the clock logic to work correctly
    else:
        set_clock_symbol_dependencies()

    # calculated peripheral frequencies
    peripherals = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
    modules = peripherals.getChildren()
    for module in range(0, len(modules)):
        module_name = modules[module].getAttribute("name")

        # if module supports multiple clock options, it will be handled separately
        if module_name in multi_clock_peripheral_list:
            continue

        # iterate and create symbols for each instance
        module_instances = modules[module].getChildren()
        for module_instance_index in range(0, len(module_instances)):
            clock_attribute = ATDF.getNode(
                "/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + str(module_name) + "\"]\
                 /instance@[name=\"" + module_instances[module_instance_index].getAttribute("name") + "\"]\
                 /parameters/param@[name=\"CLOCK_ID\"]")

            # skip instances which do not have clock_id
            if (clock_attribute == None):
                continue

            symbolID = module_instances[module_instance_index].getAttribute("name") + "_CLOCK_FREQUENCY"
            sym_peripheral_clock_freq = coreComponent.createIntegerSymbol(symbolID, None)
            sym_peripheral_clock_freq.setVisible(False)
            sym_peripheral_clock_freq.setReadOnly(True)

            # Set clock frequency based on what bus they are connected to
            if module_name in hs_peripherals_list:
                sym_peripheral_clock_freq.setDefaultValue(
                    int(Database.getSymbolValue("core", "PCLOCK_HS_CLOCK_FREQUENCY")))
                sym_peripheral_clock_freq.setDependencies(update_peripheral_clock_frequencies, ["core.PCLOCK_HS_CLOCK_FREQUENCY"])
            else:
                sym_peripheral_clock_freq.setDefaultValue(
                    int(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")))
                sym_peripheral_clock_freq.setDependencies(update_peripheral_clock_frequencies, ["core.PCLOCK_LS_CLOCK_FREQUENCY"])

    #TC clock symbol generation is handled seperately to accomodate per channel configuration
    tc_module = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]")
    num_tc_instances = tc_module.getChildren()

    for tc_instance_number in range(0, len(num_tc_instances)):
        tc_enable_dependent_list = []

        #each TC only has 3 channels(0,1 and 2). TC plib expects a dummy symbol for Channel 3 which
        # is related to quadrature mode calculations
        for tc_channel_number in range(4):
            tc_channel_id = "TC"+str(tc_instance_number)+"_CH" +str(tc_channel_number)+"_CLOCK_FREQUENCY"
            tc_channel_symbol = coreComponent.createIntegerSymbol(tc_channel_id, None)
            tc_channel_symbol.setVisible(False)
            tc_channel_symbol.setReadOnly(True)
            tc_channel_symbol.setDefaultValue(int(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")))
            tc_dependent_symbol_list = ["core.PCLOCK_LS_CLOCK_FREQUENCY",
                                        "core.SLOW_CLK_FREQUENCY",
                                        "core.TC" + str(tc_instance_number) + "_GENERIC_CLOCK_FREQUENCY",
                                        "tc" + str(tc_instance_number) + ".TC" + str(tc_channel_number) + "_CMR_TCCLKS",
                                        "tc"+str(tc_instance_number)+".TC"+str(tc_channel_number)+"_ENABLE"]
            tc_channel_symbol.setDependencies(update_tc_clock_frequency, tc_dependent_symbol_list)


    #MPDDRC is enabled by bootloader so make sure we don't disable it
    Database.setSymbolValue("core", "MPDDRC_CLOCK_ENABLE", True, 1)

    #File handling
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_sam_a5d2/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_sam_a5d2/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_a5d2/templates/system/system_definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_a5d2/templates/system/system_initialize.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)