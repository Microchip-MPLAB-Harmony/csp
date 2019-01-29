
from os.path import join
from xml.etree import ElementTree

#Peripherals supporting processor independent generic clock
global generic_clock_peripheral_list
generic_clock_peripheral_list = ["FLEXCOM0", "FLEXCOM1", "FLEXCOM2", "FLEXCOM3", "FLEXCOM4",
                                 "UART0", "UART1", "UART2", "UART3", "UART4",
                                 "TWIHS0", "TWIHS1",
                                 "SDMMC0", "SDMMC1",
                                 "SPI0", "SPI1",
                                 "TC0", "TC1",
                                 "ADC",
                                 "I2SC0", "I2SC1",
                                 "PDMIC",
                                 "MCAN0", "MCAN1",
                                 "CLASSD"]

# Peripherals connected to 64 bit AHB matrix (i.e. with HS bus clocks)
global hs_peripherals_list
hs_peripherals_list = ["XDMAC0", "XDMAC1", "AESB", "MPDDRC", "SDMMC0", "SDMMC1", "LCDC", "ISC", "QSPI0", "QSPI1"]

global CLK_SAMA5D2_CONSTANTS_DICT
CLK_SAMA5D2_CONSTANTS_DICT = {"SLOW_RC_OSC_FREQ": 32000,
                              "SLOW_XTAL_OSC_FREQ": 32768,
                              "MAIN_RC_OSC_FREQ": 12000000,
                              "EXT_OSC_MIN_FREQ": 8000000,
                              "EXT_OSC_DEFAULT_FREQ": 12000000,
                              "EXT_OSC_MAX_FREQ": 24000000,
                              "PLLA_MULA_MIN": 1,
                              "PLLA_MULA_MAX": 128,
                              "PLLA_MULA_DEFAULT": 83,
                              "PLLA_DEFAULT_FREQ": 498000000,
                              "UTMI_PLL_FREQ": 480000000,
                              "PCLOCK_LS_MAX_FREQ": 83000000
                              }

global sama5d2_fixed_clk_sym_dict
sama5d2_fixed_clk_sym_dict = {}

global sama5d2_gclk_sym_dict
sama5d2_gclk_sym_dict = {}

global sama5d2_audio_clk_sym_dict
sama5d2_audio_clk_sym_dict = {}

global sama5d2_pck_clk_sym_dict
sama5d2_pck_clk_sym_dict = {}

global sama5d2_usb_clk_sym_dict
sama5d2_usb_clk_sym_dict ={}

global sama5d2_utmi_supported_freq_mhz
sama5d2_utmi_supported_freq_mhz = []

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


global get_pid_from_instance
def get_pid_from_instance(instance_name):
    from string import digits
    # module name is instance name minus the instance number (if any)
    module_name = instance_name if not instance_name[-1:].isdigit() else instance_name.rstrip(digits)

    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + module_name +
                        "\"]/instance@[name=\"" + instance_name + "\"]/parameters/param@[name=\"INSTANCE_ID\"]")
    if node is None:
        return node
    else:
        return node.getAttribute("value")


global update_slow_clock_frequency
def update_slow_clock_frequency(symbol, event):

    source_key = sama5d2_fixed_clk_sym_dict["SCK_CR_OSCSEL"].getSelectedKey()
    # Possible values of the source key are "RC" or "XTAL"
    symbol.setValue(CLK_SAMA5D2_CONSTANTS_DICT["SLOW_" + source_key + "_OSC_FREQ"], 2)


global update_main_clock_frequency
def update_main_clock_frequency(symbol, event):

    # main crystal frequency is editable only if the crystal or bypass is enabled
    if sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTEN"].getValue() == True or \
                sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTBY"].getValue() == True:
        sama5d2_fixed_clk_sym_dict["MAIN_CRYSTAL_FREQUENCY"].setReadOnly(False)
    else:
        sama5d2_fixed_clk_sym_dict["MAIN_CRYSTAL_FREQUENCY"].setReadOnly(True)

    # Display a warning if the corresponding oscillators/clocks are not enabled
    if sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCSEL"].getSelectedKey() == "XTAL":
        show_warning = (sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTEN"].getValue() == False and \
                        sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTBY"].getValue() == False)

    else:
        show_warning = (sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCRCEN"].getValue() == False)

    sama5d2_fixed_clk_sym_dict["MAIN_CLK_INVALID_COMMENT"].setVisible(show_warning)

    # if crystal is selected, use the frequency configured by the user else use embedded RC frequency.
    if sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCSEL"].getSelectedKey() == "XTAL":
        main_clk_freq = sama5d2_fixed_clk_sym_dict["MAIN_CRYSTAL_FREQUENCY"].getValue()
        lock_moscxtst = False
    else:
        main_clk_freq = CLK_SAMA5D2_CONSTANTS_DICT["MAIN_RC_OSC_FREQ"]
        lock_moscxtst = True

    symbol.setValue(main_clk_freq, 2)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTST"].setReadOnly(lock_moscxtst)


global update_plla_clock_frequency
def update_plla_clock_frequency(symbol, event):
    plla_freq = 0

    #Only set the frequency if PLL multiplier is non zero
    if sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_MULA0"].getValue() == True:

        # base frequency
        plla_freq =  sama5d2_fixed_clk_sym_dict["MAIN_CLK_FREQUENCY"].getValue()

        # input divider
        plla_freq /= int(sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_DIVA"].getValue())

        # output multiplier
        plla_freq *= sama5d2_fixed_clk_sym_dict["CKGR_PLLA_MULA"].getValue()

        # second divider
        plla_freq /= int(sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_PLLDIVA2"].getValue())

    symbol.setValue(plla_freq, 2)


global update_utmi_ref_clock_frequency
def update_utmi_ref_clock_frequency(symbol, event):
    show_warning = False
    upll_frequency = 0
    # if UPLL is enabled
    if sama5d2_fixed_clk_sym_dict["PMC_CKGR_UCKR_UPLLEN"].getValue() == True:
        # Get the required multiplier to get a valid UPLL frequency of 480 MHz
        show_warning = True
        main_clk_freq = sama5d2_fixed_clk_sym_dict["MAIN_CLK_FREQUENCY"].getValue()
        for ref_freq_mhz in sama5d2_utmi_supported_freq_mhz:
            if main_clk_freq == int(ref_freq_mhz) * pow(10,6):
                sama5d2_fixed_clk_sym_dict["UTMI_CKTRIM_FREQ"].setValue(ref_freq_mhz, 2)
                show_warning = False
                upll_frequency = CLK_SAMA5D2_CONSTANTS_DICT["UTMI_PLL_FREQ"]
                break

    sama5d2_fixed_clk_sym_dict["CLK_UTMI_INVALID_MAIN_CLOCK"].setVisible(show_warning)
    sama5d2_fixed_clk_sym_dict["UPLL_CLK_FREQUENCY"].setValue(upll_frequency, 2)
    sama5d2_usb_clk_sym_dict["USBHS_CLOCK_FREQUENCY"].setValue(upll_frequency, 2)


global update_processor_clock_frequency
def update_processor_clock_frequency(symbol, event):

    clock_source = sama5d2_fixed_clk_sym_dict["PMC_MCKR_CSS"].getSelectedKey()
    input_frequency = Database.getSymbolValue("core", clock_source + "_FREQUENCY")

    prescaler = sama5d2_fixed_clk_sym_dict["PMC_MCKR_PRES"].getSelectedKey()

    # Key can be CLOCK or CLOCK_DIV{n}
    divisor = 1 if "_DIV" not in prescaler else int(prescaler.split("_DIV")[1])

    symbol.setValue(input_frequency/divisor, 2)

global update_mck_clock_frequency
def update_mck_clock_frequency(symbol, event):
    # MCK clock source
    clock_source = sama5d2_fixed_clk_sym_dict["PMC_MCKR_CSS"].getSelectedKey()

    # PLLA divider
    plladiv2 = sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_PLLDIVA2"].getValue()

    # MCK divider
    mck_divider_key = sama5d2_fixed_clk_sym_dict["PMC_MCKR_MDIV"].getSelectedKey()

    # PLLA invalid clock warning
    show_invalid_plla_warning = (clock_source == "PLLA_CLK") and (plladiv2 != "2") and (mck_divider_key == "PCK_DIV3")
    sama5d2_fixed_clk_sym_dict["CLK_MCK_DIV_INVALID"].setVisible(show_invalid_plla_warning)

    # Processor clock frequency
    input_frequency = sama5d2_fixed_clk_sym_dict["CPU_CLOCK_FREQUENCY"].getValue()

    # find the divider (named as EQ_PCK or PCK_DIV{n})
    if "_DIV" not in mck_divider_key:
        divisor = 1
    else:
        divisor = int(mck_divider_key.split("_DIV")[1])

    # calculate the output frequency
    output_frequency = input_frequency / divisor

    # set the master clock frequency
    symbol.setValue(output_frequency, 2)

    # set the DDR clock frequency
    sama5d2_fixed_clk_sym_dict["DDR_CLOCK_FREQUENCY"].setValue(output_frequency, 2)
    sama5d2_fixed_clk_sym_dict["CLK_DDR_CLOCK_INVALID"].setVisible(divisor < 2)

    # set the High speed bus clock frequency
    sama5d2_fixed_clk_sym_dict["PCLOCK_HS_CLOCK_FREQUENCY"].setValue(output_frequency, 2)

global update_pclock_ls_frequency
def update_pclock_ls_frequency(symbol,event):
    input_frequency = sama5d2_fixed_clk_sym_dict["MCK_CLK_FREQUENCY"].getValue()

    # symbol is named as H32MXDIV{n}
    divisor = int(sama5d2_fixed_clk_sym_dict["PMC_MCKR_H32MXDIV"].getSelectedKey().split("DIV")[1])

    output_frequency = input_frequency / divisor
    symbol.setValue(output_frequency, 2)

    show_warning = output_frequency > CLK_SAMA5D2_CONSTANTS_DICT["PCLOCK_LS_MAX_FREQ"]
    sama5d2_fixed_clk_sym_dict["CLK_PCLOCK_LS_INVALID"].setVisible(show_warning)

global update_generic_clock_frequency
def update_generic_clock_frequency(symbol, event):
    # get the peripheral ID
    pid = sym_gck_instance_pid.getValueForKey(symbol.getID().split("_GENERIC_CLOCK_FREQUENCY")[0])
    frequency = 0
    if sama5d2_gclk_sym_dict["PMC_PCR_PID" + str(pid) + "_GCKEN"].getValue() == True:
        # extract the symbols corresponding to the peripheral ID
        gckcss = sama5d2_gclk_sym_dict["PMC_PCR_PID" + str(pid) + "_GCKCSS"].getSelectedKey()
        gckdiv = sama5d2_gclk_sym_dict["PMC_PCR_PID" + str(pid) + "_GCKDIV"].getValue()
        frequency = Database.getSymbolValue("core", gckcss + "_FREQUENCY")/gckdiv

    symbol.setValue(frequency,2)

global update_peripheral_clock_frequencies
def update_peripheral_clock_frequencies(symbol, event):
    symbol.setValue(int(event["value"]), 2)


global update_programmable_clk_frequency
def update_programmable_clk_frequency(symbol, value):
    pck_clk_frequency = 0
    # find pck index
    pck_index = symbol.getID().split("PCK")[1].split("_")[0]
    # if pck is enabled
    if sama5d2_pck_clk_sym_dict["PMC_SCER_PCK" + pck_index].getValue() is True:
        # find the source clock
        clock_source = sama5d2_pck_clk_sym_dict["PMC_PCK" + pck_index + "_CSS"].getSelectedKey()
        # find the source clock frequency
        pck_clk_frequency = Database.getSymbolValue("core", clock_source + "_FREQUENCY")
        # divide by prescaler
        pck_clk_frequency /= sama5d2_pck_clk_sym_dict["PMC_PCK" + pck_index + "_PRES"].getValue()
    symbol.setValue(pck_clk_frequency, 2)


global update_audio_core_clock_frequency
def update_audio_core_clock_frequency(symbol, event):
    audio_core_clk_freq = 0
    if sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PLLEN"].getValue() is True:
        # core freq = main_freq * (ND + 1 + FRACR/2^22)
        audio_core_clk_freq = sama5d2_fixed_clk_sym_dict["MAIN_CLK_FREQUENCY"].getValue() * \
                              (sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_ND"].getValue() + 1 +
                               (float(sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_FRACR"].getValue()) / pow(2, 22)))

    symbol.setValue(int(audio_core_clk_freq), 2)


global update_audio_pmc_clock_frequency
def update_audio_pmc_clock_frequency(symbol, event):
    audio_pmc_clk_freq = 0
    if sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PMCEN"].getValue() is True:
        audio_pmc_clk_freq = float(sama5d2_audio_clk_sym_dict["AUDIO_CORE_CLK_FREQUENCY"].getValue())
        audio_pmc_clk_freq /= (sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_QDPMC"].getValue() + 1)
    symbol.setValue(int(audio_pmc_clk_freq), 2)


global update_audio_pad_clk_frequency
def update_audio_pad_clk_frequency(symbol, event):
    audio_pad_clk_freq = 0
    if sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PADEN"].getValue() is True:
        divisor = int(sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_DIV"].getSelectedKey().split("DIV")[1])
        divisor *= int(sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_QDAUDIO"].getValue())
        audio_pad_clk_freq = sama5d2_audio_clk_sym_dict ["AUDIO_CORE_CLK_FREQUENCY"].getValue() / divisor

    symbol.setValue(int(audio_pad_clk_freq), 2)

global update_usb_fs_clock_frequency
def update_usb_fs_clock_frequency(symbol, event):
    frequency = Database.getSymbolValue("core",sama5d2_usb_clk_sym_dict["PMC_USB_USBS"].getValue() + "_FREQUENCY")
    divider = sama5d2_usb_clk_sym_dict["PMC_USB_USBDIV"].getValue()
    symbol.setValue(frequency/divider, 2)


global update_lcd_clk_frequency
def update_lcd_clk_frequency(symbol, event):
    lcd_clk_frequency = 0
    if Database.getSymbolValue("core", "PMC_SCER_LCDCK") is True:
        lcd_clk_frequency = Database.getSymbolValue("core", "MCK_CLK_FREQUENCY") * 2
    symbol.setValue(lcd_clk_frequency, 2)


global update_isc_clk_frequency
def update_isc_clk_frequency(symbol, event):
    isc_clk_frequency = 0
    if Database.getSymbolValue("core", "PMC_SCER_ISCCK") is True:
        isc_clk_frequency = Database.getSymbolValue("core", "MCK_CLK_FREQUENCY") * 2
    symbol.setValue(isc_clk_frequency, 2)


global update_sdmmc_clock_frequency
def update_sdmmc_clock_frequency(symbol, event):
    symbol.setValue(event["value"], 2)


global update_spi_clock_frequency
def update_spi_clock_frequency(symbol, event):
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    src_clk = Database.getSymbolValue(instance_name.lower(), "SPI_CLK_SRC")
    if src_clk == 0:
        symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"), 2)
    elif src_clk == 1:
        symbol.setValue(Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY"), 2)
    # symbol does not exist in db
    else:
        pass

global update_adc_clock_frequency
def update_adc_clock_frequency(symbol, event):
    uart_instance = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    clock_source = Database.getSymbolValue(uart_instance.lower(), "ADC_CLK_SRC")
    # peripheral clock
    if clock_source == 0:
        symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"), 2)
    # Generic clock
    elif clock_source == 1:
        symbol.setValue(Database.getSymbolValue("core", uart_instance + "_GENERIC_CLOCK_FREQUENCY"), 2)
    # Symbol does not exist in database (value is None)
    else:
        pass

global update_mcan_clock_frequency
def update_mcan_clock_frequency(symbol, event):
    symbol.setValue(event["value"], 2)


global update_twihs_clock_frequency
def update_twihs_clock_frequency(symbol, event):
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    src_clk = Database.getSymbolValue(instance_name.lower(), "TWIHS_CLK_SRC")
    if src_clk == 0:
        symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"), 2)
    elif src_clk == 1:
        symbol.setValue(Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY"), 2)
    #symbol does not exist in db
    else:
        pass


global update_flexcomm_clock_frequency
def update_flexcomm_clock_frequency(symbol,event):
    frequency = -1
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    op_mode = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_MODE")
    # Flexcom is operating as UART
    if op_mode == 1 :
        #Get the UART mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_USART_MR_USCLKS")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")
        # Source clock is bus clock / 8
        elif source_clock == 1:
            frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY") / 8
        # Source clock is GCLK
        elif source_clock == 2:
            frequency = Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY")
        # Source clock is external, set the internal frequency to zero
        else:
            frequency = 0
    #Flexcom is operating in SPI mode
    elif op_mode == 2:
        #Get the SPI mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_SPI_MR_BRSRCCLK")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")
        # Source clock is GCLK
        elif source_clock == 1:
            frequency = Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY")
    #Flexcom is operating in TWI mode
    elif op_mode == 3:
        #Get the SPI mode source clock
        source_clock = Database.getSymbolValue(instance_name.lower(), "FLEXCOM_TWI_CWGR_BRSRCCLK")
        # Source clock is bus clock
        if source_clock == 0:
            frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")
        # Source clock is GCLK
        elif source_clock == 1:
            frequency = Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY")

    # Update the frequency only if the clock selections are valid
    if frequency >= 0:
        symbol.setValue(frequency, 2)


global update_tc_clock_frequency
def update_tc_clock_frequency(symbol, event):
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
            clk_frequency = Database.getSymbolValue("core", "TC" + str(instance_num) + "_GENERIC_CLOCK_FREQUENCY")
        # if clock  source is MCK/8
        elif (clk_src == 2):
            clk_frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")/8
        # if clock  source is MCK/32
        elif (clk_src == 3):
            clk_frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")/32
        # if clock  source is MCK/128
        elif (clk_src == 4):
            clk_frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY") / 128
        # if clock  source is SLOW CLOCK
        elif (clk_src == 5):
            clk_frequency = Database.getSymbolValue("core", "SLOW_CLK_FREQUENCY")
        # default  clock source is MCK (Enabled through extended registers of TC)
        else:
            clk_frequency = Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")

        symbol.setValue(clk_frequency, 2)


global update_tc_clock_enable
# if any channel of TC instance is enabled, enable the peripheral clock of that instance
def update_tc_clock_enable(symbol, event):
    instance_num = symbol.getID()[2]
    enable_clock = False
    for channel in range(3):
        symbol_id = "TC" + str(instance_num) + "_CHANNEL" + str(channel) + "_CLOCK_ENABLE"
        if (Database.getSymbolValue("core", symbol_id) == True):
            enable_clock = True
            break
    symbol.setValue(enable_clock, 2)


global update_uart_clock_frequency
def update_uart_clock_frequency(symbol, event):
    uart_instance = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    clock_source = Database.getSymbolValue(uart_instance.lower(), "UART_CLK_SRC")
    # peripheral clock
    if clock_source == 0:
        symbol.setValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"), 2)
    #Generic clock
    elif clock_source == 1:
        symbol.setValue(Database.getSymbolValue("core", uart_instance + "_GENERIC_CLOCK_FREQUENCY"), 2)
    #Symbol does not exist in database (value is None)
    else:
        pass

global set_component_editable
def set_component_editable(symbol, event):
    symbol.setReadOnly(not event["value"])


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

    # create slow clock selector symbol
    sym_slow_clock_selector = clk_comp.createKeyValueSetSymbol("SCK_CR_OSCSEL", slow_clk_menu)
    sym_slow_clock_selector.setLabel("Slow Clock Selector")

    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_slow_clock_selector, "SCKC", "SCKC_CR__OSCSEL")

    # set RC as the default value
    sym_slow_clock_selector.setDefaultValue(1)
    sama5d2_fixed_clk_sym_dict["SCK_CR_OSCSEL"] = sym_slow_clock_selector

    # symbol identifying the slow clock frequency
    sym_clk_slow = clk_comp.createIntegerSymbol("SLOW_CLK_FREQUENCY", slow_clk_menu)
    sym_clk_slow.setLabel("Slow Clock (Hz)")
    sym_clk_slow.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["SLOW_XTAL_OSC_FREQ"])
    sym_clk_slow.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["SLOW_CLK_FREQUENCY"] = sym_clk_slow
    sym_clk_slow.setDependencies(update_slow_clock_frequency, ["SCK_CR_OSCSEL"])


def __main_clock_menu(clk_comp, clk_menu):
    """
       Main Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """

    # main clock menu
    main_clock_menu = clk_comp.createMenuSymbol("CLK_MAIN_MENU", clk_menu)
    main_clock_menu.setLabel("Main clock configuration")

    # symbol for the main crystal oscillator enable
    sym_main_xtal_osc_enable = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCXTEN", main_clock_menu)
    sym_main_xtal_osc_enable.setLabel("External oscillator enable")
    sym_main_xtal_osc_enable.setDefaultValue(True)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTEN"] = sym_main_xtal_osc_enable

    # symbol for main crystal oscillator bypass
    sym_main_xtal_osc_bypass = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCXTBY", main_clock_menu)
    sym_main_xtal_osc_bypass.setLabel("External oscillator bypass")
    sym_main_xtal_osc_bypass.setDefaultValue(False)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTBY"] = sym_main_xtal_osc_bypass

    # symbol for main crystal/clock input frequency
    sym_main_xtal_input_frequency = clk_comp.createIntegerSymbol("MAIN_CRYSTAL_FREQUENCY", main_clock_menu)
    sym_main_xtal_input_frequency.setLabel("External oscillator/clock frequency")
    sym_main_xtal_input_frequency.setMin(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_MIN_FREQ"])
    sym_main_xtal_input_frequency.setMax(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_MAX_FREQ"])
    sym_main_xtal_input_frequency.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_DEFAULT_FREQ"])
    sama5d2_fixed_clk_sym_dict["MAIN_CRYSTAL_FREQUENCY"] = sym_main_xtal_input_frequency

    # symbol for main crystal stabilization cycle count
    sym_main_xtal_stabilization_count = clk_comp.createIntegerSymbol("CKGR_MOR_MOSCXTST", main_clock_menu)
    sym_main_xtal_stabilization_count.setLabel("Main crystal stabilization count ( value x 8 SCLK cycles)")
    sym_main_xtal_stabilization_count.setMin(0)
    sym_main_xtal_stabilization_count.setMax(255)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCXTST"] = sym_main_xtal_stabilization_count

    # symbol for main RC oscillator enable
    sym_rc_osc_enable = clk_comp.createBooleanSymbol("CKGR_MOR_MOSCRCEN", main_clock_menu)
    sym_rc_osc_enable.setLabel("Embedded RC oscillator enable")
    sym_rc_osc_enable.setDefaultValue(False)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCRCEN"] = sym_rc_osc_enable

    # symbol for main clock selection
    sym_main_clk_selection = clk_comp.createKeyValueSetSymbol("CKGR_MOR_MOSCSEL", main_clock_menu)
    sym_main_clk_selection.setLabel("Main clock source selection")
    sym_main_clk_selection.addKey("RC", "0", "")
    sym_main_clk_selection.addKey("XTAL", "1", "")
    sym_main_clk_selection.setDefaultValue(1)
    sama5d2_fixed_clk_sym_dict["CKGR_MOR_MOSCSEL"] = sym_main_clk_selection

    # symbol for main clock frequency
    sym_main_clk_freq = clk_comp.createIntegerSymbol("MAIN_CLK_FREQUENCY", main_clock_menu)
    sym_main_clk_freq.setLabel("Main Clock Frequency(Hz)")
    sym_main_clk_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["EXT_OSC_DEFAULT_FREQ"])
    sym_main_clk_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["MAIN_CLK_FREQUENCY"] = sym_main_clk_freq

    # symbol for invalid clock source comment
    sym_main_clk_src_invalid = clk_comp.createCommentSymbol("MAIN_CLK_INVALID_COMMENT", main_clock_menu)
    sym_main_clk_src_invalid.setLabel("Oscillator/clock for current selection is not enabled !!!")
    sym_main_clk_src_invalid.setVisible(False)
    sama5d2_fixed_clk_sym_dict["MAIN_CLK_INVALID_COMMENT"] = sym_main_clk_src_invalid


def __plla_clock_menu(clk_comp, clk_menu):
    """
       PLLA Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """
    # plla clock menu
    plla_clock_menu = clk_comp.createMenuSymbol("CLK_PLLA_MENU", clk_menu)
    plla_clock_menu.setLabel("PLLA clock configuration")

    # symbol for PLLA enable ( There is no corresponding register bit , it just sets MULA value to 0)
    sym_plla_enable = clk_comp.createBooleanSymbol("CKGR_PLLAR_MULA0", plla_clock_menu)
    sym_plla_enable.setLabel("PLLA Enable")
    sym_plla_enable.setDefaultValue(True)
    sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_MULA0"] = sym_plla_enable

    # symbol for PLLA input divider
    sym_plla_input_divider = clk_comp.createComboSymbol("CKGR_PLLAR_DIVA", plla_clock_menu, ["1", "2"])
    sym_plla_input_divider.setLabel("PLLA input divider")
    sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_DIVA"] = sym_plla_input_divider

    # symbol for output multiplier
    sym_plla_multiplier = clk_comp.createIntegerSymbol("CKGR_PLLA_MULA", plla_clock_menu)
    sym_plla_multiplier.setLabel("PLLA multiplier")
    sym_plla_multiplier.setMin(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_MIN"])
    sym_plla_multiplier.setMax(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_MAX"])
    sym_plla_multiplier.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_MULA_DEFAULT"])
    sama5d2_fixed_clk_sym_dict["CKGR_PLLA_MULA"] = sym_plla_multiplier

    # symbol for output divider
    sym_plla_output_divider = clk_comp.createComboSymbol("CKGR_PLLAR_PLLDIVA2", plla_clock_menu, ["1", "2"])
    sym_plla_output_divider.setLabel("PLLA output divider")
    sym_plla_output_divider.setDefaultValue("2")
    sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_PLLDIVA2"] = sym_plla_output_divider

    # symbol for stabilization count
    sym_plla_stabilization_count = clk_comp.createIntegerSymbol("CKGR_PLLAR_PLLACOUNT", plla_clock_menu)
    sym_plla_stabilization_count.setLabel("PLLA stabilization count (in SCLK cycles)")
    sym_plla_stabilization_count.setMin(0)
    sym_plla_stabilization_count.setMax(63)
    sama5d2_fixed_clk_sym_dict["CKGR_PLLAR_PLLACOUNT"] = sym_plla_stabilization_count

    # symbol for output clock frequency
    sym_clk_plla_freq = clk_comp.createIntegerSymbol("PLLA_CLK_FREQUENCY", plla_clock_menu)
    sym_clk_plla_freq.setLabel("PLL Clock (Hz)")
    sym_clk_plla_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["PLLA_DEFAULT_FREQ"])
    sym_clk_plla_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["PLLA_CLK_FREQUENCY"] = sym_clk_plla_freq

def __utmi_pll_clock_menu(clk_comp, clk_menu):
    """
       UTMI Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """
    # utmi clock menu
    utmi_clock_menu = clk_comp.createMenuSymbol("CLK_UTMI_PLL_MENU", clk_menu)
    utmi_clock_menu.setLabel("UTMI clock menu")

    # utmi clock enable
    sym_utmi_pllen = clk_comp.createBooleanSymbol("PMC_CKGR_UCKR_UPLLEN", utmi_clock_menu)
    sym_utmi_pllen.setLabel("UTMI PLL enable")
    sym_utmi_pllen.setDefaultValue(True)
    sama5d2_fixed_clk_sym_dict["PMC_CKGR_UCKR_UPLLEN"] = sym_utmi_pllen

    # UPLL startup time
    sym_ckgr_uckr_upllcount = clk_comp.createIntegerSymbol("PMC_CKGR_UCKR_UPLLCOUNT", utmi_clock_menu)
    sym_ckgr_uckr_upllcount.setLabel("UTMI PLL startup time")
    sym_ckgr_uckr_upllcount.setDefaultValue(15)
    sym_ckgr_uckr_upllcount.setMin(0)
    sym_ckgr_uckr_upllcount.setMax(15)
    sym_ckgr_uckr_upllcount.setReadOnly(not sym_utmi_pllen.getValue())
    sym_ckgr_uckr_upllcount.setDependencies(set_component_editable, ["PMC_CKGR_UCKR_UPLLEN"])
    sama5d2_fixed_clk_sym_dict["PMC_CKGR_UCKR_UPLLCOUNT"] = sym_ckgr_uckr_upllcount

    # create symbol for FREQ bitfield of UTMI_CKTRIM register
    valgrp_sfr_cktrim_freq = ATDF.getNode(
       "/avr-tools-device-file/modules/module@[name=\"SFR\"]/value-group@[name=\"SFR_UTMICKTRIM__FREQ\"]").getChildren()
    for index in range(0, len(valgrp_sfr_cktrim_freq)):
        sama5d2_utmi_supported_freq_mhz.append(valgrp_sfr_cktrim_freq[index].getAttribute("name").split("_")[1])
    sym_utmi_cktrim = clk_comp.createComboSymbol("UTMI_CKTRIM_FREQ", utmi_clock_menu, sama5d2_utmi_supported_freq_mhz)
    sym_utmi_cktrim.setVisible(False)
    sama5d2_fixed_clk_sym_dict["UTMI_CKTRIM_FREQ"] = sym_utmi_cktrim

    # utmi invalid main clock comment
    sym_utmi_invalid_comment = clk_comp.createCommentSymbol("CLK_UTMI_INVALID_MAIN_CLOCK", utmi_clock_menu)
    sym_utmi_invalid_comment.setLabel("Current main clock cannot generate a valid UTMI clock of 480 MHz !!!")
    sym_utmi_invalid_comment.setVisible(False)
    sama5d2_fixed_clk_sym_dict["CLK_UTMI_INVALID_MAIN_CLOCK"] = sym_utmi_invalid_comment

    # utmi clock frequency symbol
    sym_clk_utmi_freq = clk_comp.createIntegerSymbol("UPLL_CLK_FREQUENCY", utmi_clock_menu)
    sym_clk_utmi_freq.setLabel("UTMI clock frequency(Hz)")
    sym_clk_utmi_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["UTMI_PLL_FREQ"])
    sym_clk_utmi_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["UPLL_CLK_FREQUENCY"] = sym_clk_utmi_freq


def __mck_clock_menu(clk_comp, clk_menu):
    """
       MCK Clock Menu Implementation.

       clk_comp: Clock Component handle
       clk_menu: Clock Menu Symbol handle
    """

    # master clock menu
    mck_clock_menu = clk_comp.createMenuSymbol("CLK_MASTER_MENU", clk_menu)
    mck_clock_menu.setLabel("MCK clock menu")

    # MCK source selector
    sym_mck_source_selector  = clk_comp.createKeyValueSetSymbol("PMC_MCKR_CSS", mck_clock_menu)
    sym_mck_source_selector.setLabel("MCK source selector")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_source_selector, "PMC", "PMC_MCKR__CSS")
    sym_mck_source_selector.setDefaultValue(2)
    sama5d2_fixed_clk_sym_dict["PMC_MCKR_CSS"] = sym_mck_source_selector

    # MCK source pre-scaler
    sym_mck_prescaler = clk_comp.createKeyValueSetSymbol("PMC_MCKR_PRES", mck_clock_menu)
    sym_mck_prescaler.setLabel("MCK prescaler")

    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_prescaler, "PMC", "PMC_MCKR__PRES")
    sama5d2_fixed_clk_sym_dict["PMC_MCKR_PRES"] = sym_mck_prescaler

    # Processor clock frequency
    sym_processor_clk_freq = clk_comp.createIntegerSymbol("CPU_CLOCK_FREQUENCY", mck_clock_menu)
    sym_processor_clk_freq.setLabel("Processor Clock Frequency (HZ)")
    sym_processor_clk_freq.setDefaultValue(sama5d2_fixed_clk_sym_dict["PLLA_CLK_FREQUENCY"].getValue())
    sym_processor_clk_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["CPU_CLOCK_FREQUENCY"] = sym_processor_clk_freq

    # MCK divider
    sym_mck_divider = clk_comp.createKeyValueSetSymbol("PMC_MCKR_MDIV", mck_clock_menu)
    sym_mck_divider.setLabel("MCK divider")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_mck_divider, "PMC", "PMC_MCKR__MDIV")
    sym_mck_divider.setDefaultValue(3)
    sama5d2_fixed_clk_sym_dict["PMC_MCKR_MDIV"] = sym_mck_divider

    sym_invalid_mck_divider = clk_comp.createCommentSymbol("CLK_MCK_DIV_INVALID", mck_clock_menu)
    sym_invalid_mck_divider.setLabel("If MCK divider is 3 and processor clock source is PLLA, PLLA2 divider " +
                                                                            "should be enabled !!!")
    sym_invalid_mck_divider.setVisible(False)
    sama5d2_fixed_clk_sym_dict["CLK_MCK_DIV_INVALID"] = sym_invalid_mck_divider

    # MCK clock frequency
    sym_master_clk_freq = clk_comp.createIntegerSymbol("MCK_CLK_FREQUENCY", mck_clock_menu)
    sym_master_clk_freq.setLabel("MCK Clock Frequency (HZ)")
    sym_master_clk_freq.setDefaultValue(sama5d2_fixed_clk_sym_dict["PLLA_CLK_FREQUENCY"].getValue() / sym_mck_divider.getValue())
    sym_master_clk_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["MCK_CLK_FREQUENCY"] = sym_master_clk_freq

    # DDR clock frequency
    sym_ddr_clk_freq = clk_comp.createIntegerSymbol("DDR_CLOCK_FREQUENCY", mck_clock_menu)
    sym_ddr_clk_freq.setLabel("DDR clock Frequency (Hz)")
    sym_ddr_clk_freq.setDefaultValue(sym_master_clk_freq.getValue())
    sym_ddr_clk_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["DDR_CLOCK_FREQUENCY"] = sym_ddr_clk_freq

    # DDR clock invalid comment
    sym_ddr_clk_invalid_comment = clk_comp.createCommentSymbol("CLK_DDR_CLOCK_INVALID", mck_clock_menu)
    sym_ddr_clk_invalid_comment.setLabel("DDR clock is invalid when the master clock is equal to processor clock !!!")
    sym_ddr_clk_invalid_comment.setVisible(False)
    sama5d2_fixed_clk_sym_dict["CLK_DDR_CLOCK_INVALID"] = sym_ddr_clk_invalid_comment

    sym_periph_hs_clk_freq = clk_comp.createIntegerSymbol("PCLOCK_HS_CLOCK_FREQUENCY", mck_clock_menu)
    sym_periph_hs_clk_freq.setLabel("H64MX bus clock (PCLOCK_HS) (HZ)")
    sym_periph_hs_clk_freq.setDefaultValue(sym_master_clk_freq.getValue())
    sym_periph_hs_clk_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["PCLOCK_HS_CLOCK_FREQUENCY"] = sym_periph_hs_clk_freq

    # Low speed bus clock divider
    sym_h32mx_divider = clk_comp.createKeyValueSetSymbol("PMC_MCKR_H32MXDIV", mck_clock_menu)
    sym_h32mx_divider.setLabel("H32MX divider")
    # Get the value group for the bitfield from atdf
    set_symbol_value_from_atdf(sym_h32mx_divider, "PMC", "PMC_MCKR__H32MXDIV")
    sym_h32mx_divider.setDefaultValue(1)
    sama5d2_fixed_clk_sym_dict["PMC_MCKR_H32MXDIV"] = sym_h32mx_divider

    # Low speed bus clock frequency
    sym_periph_clk_ls_freq = clk_comp.createIntegerSymbol("PCLOCK_LS_CLOCK_FREQUENCY", mck_clock_menu)
    sym_periph_clk_ls_freq.setLabel("H32MX bus clock (PCLOCK_LS)(HZ)")
    sym_periph_clk_ls_freq.setDefaultValue(sym_master_clk_freq.getDefaultValue()/2)
    sym_periph_clk_ls_freq.setReadOnly(True)
    sama5d2_fixed_clk_sym_dict["PCLOCK_LS_CLOCK_FREQUENCY"] = sym_periph_clk_ls_freq

    # Low speed bus clock invalid comment
    sym_pclock_ls_invalid_comment = clk_comp.createCommentSymbol("CLK_PCLOCK_LS_INVALID", mck_clock_menu)
    sym_pclock_ls_invalid_comment.setLabel("H32MX bus clock cannot be higher than 83 MHz !!!")
    sym_pclock_ls_invalid_comment.setVisible(False)
    sama5d2_fixed_clk_sym_dict["CLK_PCLOCK_LS_INVALID"] = sym_pclock_ls_invalid_comment


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

    # get bitfields
    bitfield_pmc_audio_pll0_pllen = reg_pmc_audio_pll0.getBitfield("PLLEN")
    bitfield_pmc_audio_pll0_qdpmc = reg_pmc_audio_pll0.getBitfield("QDPMC")
    bitfield_pmc_audio_pll0_nd = reg_pmc_audio_pll0.getBitfield("ND")
    bitfield_pmc_audio_pll0_pmcen = reg_pmc_audio_pll0.getBitfield("PMCEN")
    bitfield_pmc_audio_pll0_paden = reg_pmc_audio_pll0.getBitfield("PADEN")
    bitfield_pmc_audio_pll1_qdaudio = reg_pmc_audio_pll1.getBitfield("QDAUDIO")
    bitfield_pmc_audio_pll1_div = reg_pmc_audio_pll1.getBitfield("DIV")
    bitfield_pmc_audio_pll1_fracr = reg_pmc_audio_pll1.getBitfield("FRACR")

    # get values
    bitfield_pmc_audio_pll1_div_values = pmc_reg_module.getValueGroup(bitfield_pmc_audio_pll1_div.getValueGroupName())

    # create symbols
    sym_pllen = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PLLEN", audio_clk_menu)
    sym_pllen.setLabel(bitfield_pmc_audio_pll0_pllen.getDescription())
    sym_pllen.setDefaultValue(False)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PLLEN"] = sym_pllen

    sym_qdpmc = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL0_QDPMC", audio_clk_menu)
    sym_qdpmc.setLabel(bitfield_pmc_audio_pll0_qdpmc.getDescription())
    sym_qdpmc.setMin(0)
    sym_qdpmc.setMax(127)
    sym_qdpmc.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_qdpmc.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_QDPMC"] = sym_qdpmc

    sym_nd = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL0_ND", audio_clk_menu)
    sym_nd.setLabel(bitfield_pmc_audio_pll0_nd.getDescription())
    sym_nd.setMin(0)
    sym_nd.setMax(127)
    sym_nd.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_nd.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_ND"] = sym_nd

    sym_qdaudio = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL1_QDAUDIO", audio_clk_menu)
    sym_qdaudio.setLabel(bitfield_pmc_audio_pll1_qdaudio.getDescription())
    sym_qdaudio.setMin(1)
    sym_qdaudio.setMax(31)
    sym_qdaudio.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_qdaudio.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_QDAUDIO"] = sym_qdaudio

    sym_div = clk_comp.createKeyValueSetSymbol("PMC_AUDIO_PLL1_DIV", audio_clk_menu)
    sym_div.setLabel(bitfield_pmc_audio_pll1_div.getDescription())
    for name in bitfield_pmc_audio_pll1_div_values.getValueNames():
        value = bitfield_pmc_audio_pll1_div_values.getValue(name)
        sym_div.addKey(value.getName(), value.getValue(), value.getDescription())
    sym_div.setOutputMode("Value")
    sym_div.setDisplayMode("Description")
    sym_div.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_div.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_DIV"] = sym_div

    sym_fracr = clk_comp.createIntegerSymbol("PMC_AUDIO_PLL1_FRACR", audio_clk_menu)
    sym_fracr.setLabel(bitfield_pmc_audio_pll1_fracr.getDescription())
    sym_fracr.setMin(0)
    sym_fracr.setMax(pow(2,22) - 1)
    sym_fracr.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_fracr.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL1_FRACR"] = sym_fracr

    sym_pmcen = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PMCEN", audio_clk_menu)
    sym_pmcen.setLabel(bitfield_pmc_audio_pll0_pmcen.getDescription())
    sym_pmcen.setDefaultValue(False)
    sym_pmcen.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_pmcen.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PMCEN"] = sym_pmcen

    sym_paden = clk_comp.createBooleanSymbol("PMC_AUDIO_PLL0_PADEN", audio_clk_menu)
    sym_paden.setLabel(bitfield_pmc_audio_pll0_paden.getDescription())
    sym_paden.setDefaultValue(False)
    sym_paden.setDependencies(set_component_editable, ["PMC_AUDIO_PLL0_PLLEN"])
    sym_paden.setReadOnly(True)
    sama5d2_audio_clk_sym_dict["PMC_AUDIO_PLL0_PADEN"] = sym_paden

    sym_audio_core_clk = clk_comp.createIntegerSymbol("AUDIO_CORE_CLK_FREQUENCY", audio_clk_menu)
    sym_audio_core_clk.setLabel("Audio core clock Frequency (Hz)")
    sym_audio_core_clk.setReadOnly(True)
    sym_audio_core_clk.setDependencies(update_audio_core_clock_frequency, ["PMC_AUDIO_PLL0_PLLEN",
                                                                           "MAIN_CLK_FREQUENCY",
                                                                           "PMC_AUDIO_PLL0_ND",
                                                                           "PMC_AUDIO_PLL1_FRACR"])
    sym_audio_core_clk.setVisible(False)
    sama5d2_audio_clk_sym_dict["AUDIO_CORE_CLK_FREQUENCY"] = sym_audio_core_clk

    sym_audio_pmc_clk = clk_comp.createIntegerSymbol("AUDIO_CLK_FREQUENCY", audio_clk_menu)
    sym_audio_pmc_clk.setLabel("Audio PMC clock Frequency (Hz)")
    sym_audio_pmc_clk.setReadOnly(True)
    sym_audio_pmc_clk.setDependencies(update_audio_pmc_clock_frequency, ["PMC_AUDIO_PLL0_PMCEN",
                                                                         "AUDIO_CORE_CLK_FREQUENCY",
                                                                         "PMC_AUDIO_PLL0_QDPMC"])
    sama5d2_audio_clk_sym_dict["AUDIO_CLK_FREQUENCY"] = sym_audio_pmc_clk

    sym_audio_pad_clk = clk_comp.createIntegerSymbol("AUDIO_PAD_CLK_FREQUENCY", audio_clk_menu)
    sym_audio_pad_clk.setLabel("Audio Pad clock frequency (Hz)")
    sym_audio_pad_clk.setReadOnly(True)
    sym_audio_pad_clk.setDependencies(update_audio_pad_clk_frequency,["PMC_AUDIO_PLL0_PADEN",
                                                                        "AUDIO_CORE_CLK_FREQUENCY",
                                                                        "PMC_AUDIO_PLL1_QDAUDIO",
                                                                        "PMC_AUDIO_PLL1_DIV"])


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

    # get UTMI register group
    sfr_reg_group = sfr_reg_module.getRegisterGroup("SFR")

    # get UTMI_CKTRIM register
    reg_sfr_cktrim = sfr_reg_group.getRegister("SFR_UTMICKTRIM")

    # get FREQ bitfield of UTMI_CKTRIM register
    bitfield_sfr_cktrim_freq = reg_sfr_cktrim.getBitfield("FREQ")

    # get value group for FREQ bitfield of UTMI_CKTRIM register
    valgrp_sfr_cktrim_freq = sfr_reg_module.getValueGroup(bitfield_sfr_cktrim_freq.getValueGroupName())

    # get PMC_SCER register
    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")

    # get UDP bitfield of PMC_SCER register
    bitfield_pmc_scer_udpclk = reg_pmc_scer.getBitfield("UDP")

    # get symbol for UDPCLK bitfield of PMC_SCER register
    sym_pmc_scer_udp = clk_comp.createBooleanSymbol("PMC_SCER_UDPCLK", usb_clk_menu)
    sym_pmc_scer_udp.setLabel(bitfield_pmc_scer_udpclk.getDescription())
    sama5d2_usb_clk_sym_dict["PMC_SCER_UDPCLK"] = sym_pmc_scer_udp

    # get UHP bitfield of PMC_SCER register
    bitfield_pmc_scer_uhpclk = reg_pmc_scer.getBitfield("UHP")

    # get symbol for UDPCLK bitfield of PMC_SCER register
    sym_pmc_scer_uhpclk = clk_comp.createBooleanSymbol("PMC_SCER_UHPCLK", usb_clk_menu)
    sym_pmc_scer_uhpclk.setLabel(bitfield_pmc_scer_uhpclk.getDescription())
    sama5d2_usb_clk_sym_dict["PMC_SCER_UHPCLK"] = sym_pmc_scer_uhpclk

    # get PMC_USB register
    reg_pmc_usb = pmc_reg_group.getRegister("PMC_USB")

    # get USBS bitfield of PMC_USB register
    bitfield_pmc_usb_usbs = reg_pmc_usb.getBitfield("USBS")

    # create symbol for USBS bitfield of PMC_USB register
    sym_pmc_usb_usbs = clk_comp.createComboSymbol("PMC_USB_USBS", usb_clk_menu, ["PLLA_CLK", "UPLL_CLK"])
    sym_pmc_usb_usbs.setLabel(bitfield_pmc_usb_usbs.getDescription())
    sym_pmc_usb_usbs.setDefaultValue("UPLL_CLK")
    sama5d2_usb_clk_sym_dict["PMC_USB_USBS"] = sym_pmc_usb_usbs

    # get USBDIV bitfield of PMC_USB register
    bitfield_pmc_usb_usbdiv = reg_pmc_usb.getBitfield("USBDIV")

    # create symbol for USBDIV bitfield of PMC_USB register
    sym_usb_divider = clk_comp.createIntegerSymbol("PMC_USB_USBDIV", usb_clk_menu)
    sym_usb_divider.setLabel(bitfield_pmc_usb_usbdiv.getDescription())
    sym_usb_divider.setMin(1)
    sym_usb_divider.setMax(16)
    sym_usb_divider.setDefaultValue(10)
    sama5d2_usb_clk_sym_dict["PMC_USB_USBDIV"] = sym_usb_divider

    # USB clock frequencies
    sym_usb_fs_freq = clk_comp.createIntegerSymbol("USBFS_CLOCK_FREQUENCY", usb_clk_menu)
    sym_usb_fs_freq.setLabel("USB Clock Frequency (HZ)")
    sym_usb_fs_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["UTMI_PLL_FREQ"]/sym_usb_divider.getValue())
    sym_usb_fs_freq.setDependencies(update_usb_fs_clock_frequency, ["PMC_USB_USBS",
                                                                    "PMC_USB_USBDIV",
                                                                    "UPLL_CLK_FREQUENCY",
                                                                    "PLLA_CLK_FREQUENCY"])
    sym_usb_fs_freq.setReadOnly(True)
    sama5d2_usb_clk_sym_dict["USBFS_CLOCK_FREQUENCY"] = sym_usb_fs_freq

    sym_usb_hs_freq = clk_comp.createIntegerSymbol("USBHS_CLOCK_FREQUENCY", usb_clk_menu)
    sym_usb_hs_freq.setLabel("USB High Speed Clock Frequency (HZ)")
    sym_usb_hs_freq.setDefaultValue(CLK_SAMA5D2_CONSTANTS_DICT["UTMI_PLL_FREQ"])
    sym_usb_hs_freq.setReadOnly(True)
    sama5d2_usb_clk_sym_dict["USBHS_CLOCK_FREQUENCY"] = sym_usb_hs_freq

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

    # get GCLKEN bitfield of PMC_PCR register
    bitfield_pmc_pcr_gclken = reg_pmc_pcr.getBitfield("GCKEN")

    # get GCLKDIV bitfield of PMC_PCR register
    bitfield_pmc_pcr_gckdiv = reg_pmc_pcr.getBitfield("GCKDIV")

    # get GCKCSS bitfield of PMC_PCR register
    bitfield_pmc_pcr_gckcss = reg_pmc_pcr.getBitfield("GCKCSS")
    bitfield_pmc_pcr_gckcss_values = pmc_reg_module.getValueGroup(bitfield_pmc_pcr_gckcss.getValueGroupName())

    # create a map of GCK instance to its PID for the clock UI
    global sym_gck_instance_pid
    sym_gck_instance_pid = clk_comp.createKeyValueSetSymbol("GCK_INSTANCE_PID", generic_clk_menu)
    sym_gck_instance_pid.setVisible(False)

    for periph in generic_clock_peripheral_list:

        pid = get_pid_from_instance(periph)
        if pid is None:
            print "Unable to locate periph " + periph
            continue

        # Add element to the map
        sym_gck_instance_pid.addKey(periph, pid, "")

        # create menu for Peripheral/Generic Clock
        sym_gclkx_menu = clk_comp.createMenuSymbol("CLK_GEN" + pid, generic_clk_menu)
        sym_gclkx_menu.setLabel("Generic Clock for Peripheral " + periph)

        # create symbol for GCLKEN bitfield of PMC_PCR register
        sym_pmc_pcr_gclken = clk_comp.createBooleanSymbol("PMC_PCR_PID" + pid +"_GCKEN", sym_gclkx_menu)
        sym_pmc_pcr_gclken.setLabel(bitfield_pmc_pcr_gclken.getDescription())
        sama5d2_gclk_sym_dict["PMC_PCR_PID" + pid  + "_GCKEN"] = sym_pmc_pcr_gclken

        # create symbol for GCLKDIV bitfield of PMC_PCR register
        sym_pmc_pcr_gckdiv = clk_comp.createIntegerSymbol("PMC_PCR_PID" + pid +"_GCKDIV", sym_gclkx_menu)
        sym_pmc_pcr_gckdiv.setLabel(bitfield_pmc_pcr_gckdiv.getDescription())
        sym_pmc_pcr_gckdiv.setMin(1)
        sym_pmc_pcr_gckdiv.setMax(256)
        sym_pmc_pcr_gckdiv.setDefaultValue(1)
        sym_pmc_pcr_gckdiv.setReadOnly(True)
        sym_pmc_pcr_gckdiv.setDependencies(set_component_editable, ["PMC_PCR_PID" + pid  +"_GCKEN"])
        sama5d2_gclk_sym_dict["PMC_PCR_PID" + pid  + "_GCKDIV"] = sym_pmc_pcr_gckdiv

        # create symbol for GCLKCSS bitfield of PMC_PCR register
        sym_pmc_pcr_gckcss = clk_comp.createKeyValueSetSymbol("PMC_PCR_PID" +pid  +"_GCKCSS", sym_gclkx_menu)
        sym_pmc_pcr_gckcss.setLabel(bitfield_pmc_pcr_gckcss.getDescription())
        for name in bitfield_pmc_pcr_gckcss_values.getValueNames():
            value = bitfield_pmc_pcr_gckcss_values.getValue(name)
            sym_pmc_pcr_gckcss.addKey(value.getName(), value.getValue(), value.getDescription())
        sym_pmc_pcr_gckcss.setReadOnly(True)
        sym_pmc_pcr_gckcss.setOutputMode("Value")
        sym_pmc_pcr_gckcss.setDisplayMode("Key")
        sym_pmc_pcr_gckcss.setSelectedKey("SLOW_CLK",1)
        sym_pmc_pcr_gckcss.setDependencies(set_component_editable, ["PMC_PCR_PID" + pid  + "_GCKEN"])
        sama5d2_gclk_sym_dict["PMC_PCR_PID" + pid  + "_GCKCSS"] = sym_pmc_pcr_gckcss

        # calculated generic clock frequency
        sym_gen_clk_freq = clk_comp.createIntegerSymbol(periph + "_GENERIC_CLOCK_FREQUENCY", sym_gclkx_menu)
        sym_gen_clk_freq.setLabel(periph + " Generic Clock Frequency (HZ)")
        sym_gen_clk_freq.setDefaultValue(0)
        sym_gen_clk_freq.setReadOnly(True)
        sym_gen_clk_freq.setDependencies(update_generic_clock_frequency, ["PMC_PCR_PID" + pid  + "_GCKDIV",
                                                                          "PMC_PCR_PID" + pid  + "_GCKCSS",
                                                                          "SLOW_CLK_FREQUENCY",
                                                                          "MAIN_CLK_FREQUENCY",
                                                                          "PLLA_CLK_FREQUENCY",
                                                                          "UPLL_CLK_FREQUENCY",
                                                                          "MCK_CLK_FREQUENCY"])
        sama5d2_gclk_sym_dict[periph + "_GENERIC_CLOCK_FREQUENCY"] = sym_gen_clk_freq


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


# Programmable Clock generator configuration options
def __programmable_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Programmable Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for Programmable clock menu
    pck_clk_menu = clk_comp.createMenuSymbol("CLK_PROGRAMMABLE", clk_menu)
    pck_clk_menu.setLabel("Programmable Clock Generator Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_SCER register
    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")

    # get PMC_PCK# register
    reg_pmc_pck = pmc_reg_group.getRegister("PMC_PCK")

    # menu for 3 programmable clock
    for i in range(0, 3, 1):
        # create symbol for programmable clock #
        sym_prog_clk_menu = clk_comp.createMenuSymbol("CLK_PROGRAMMABLE_" + str(i), pck_clk_menu)
        sym_prog_clk_menu.setLabel("Programmable Clock " + str(i) + " Generator Configuration")

        # get PCK# bitfield of PMC_SCER Register
        bitfield_pmc_scer_pck = reg_pmc_scer.getBitfield("PCK" + str(i))

        # create symbol for PCK# bitfield of PMC_SCER Register
        sym_pmc_scer_pck = clk_comp.createBooleanSymbol("PMC_SCER_PCK" + str(i), sym_prog_clk_menu)
        sym_pmc_scer_pck.setLabel(bitfield_pmc_scer_pck.getDescription())
        sama5d2_pck_clk_sym_dict["PMC_SCER_PCK" + str(i)] = sym_pmc_scer_pck

        # get CSS bitfield of PMC_PCK# register
        bitfield_pmc_pck_css = reg_pmc_pck.getBitfield("CSS")

        # get Value Group for CSS bitfield of PMC_PCK# register
        valgrp_pmc_pck_css = pmc_reg_module.getValueGroup(bitfield_pmc_pck_css.getValueGroupName())

        # create symbol for CSS bitfield of PMC_PCK# register
        sym_pmc_pck_css = clk_comp.createKeyValueSetSymbol("PMC_PCK" + str(i) + "_CSS", sym_prog_clk_menu)
        sym_pmc_pck_css.setLabel(bitfield_pmc_pck_css.getDescription())
        sym_pmc_pck_css.setOutputMode("Value")
        sym_pmc_pck_css.setDisplayMode("Description")
        for name in valgrp_pmc_pck_css.getValueNames():
            value = valgrp_pmc_pck_css.getValue(name)
            sym_pmc_pck_css.addKey(value.getName(), value.getValue(), value.getDescription())
        sym_pmc_pck_css.setDependencies(set_component_editable, ["PMC_SCER_PCK" + str(i)])
        sym_pmc_pck_css.setReadOnly(True)
        sama5d2_pck_clk_sym_dict["PMC_PCK" + str(i) + "_CSS"] = sym_pmc_pck_css

        # get PRES bitfield of PMC_PCK# register
        bitfield_pmc_pck_pres = reg_pmc_pck.getBitfield("PRES")

        # create symbol for PRES bitfield of PMC_PCK# register
        sym_pmc_pck_pres = clk_comp.createIntegerSymbol("PMC_PCK" + str(i) +"_PRES", sym_prog_clk_menu)
        sym_pmc_pck_pres.setLabel(bitfield_pmc_pck_pres.getDescription())
        sym_pmc_pck_pres.setMin(1)
        sym_pmc_pck_pres.setMax(256)
        sym_pmc_pck_pres.setDefaultValue(1)
        sym_pmc_pck_pres.setReadOnly(True)
        sym_pmc_pck_pres.setDependencies(set_component_editable, ["PMC_SCER_PCK" + str(i)])
        sama5d2_pck_clk_sym_dict["PMC_PCK" + str(i) +"_PRES"] = sym_pmc_pck_pres

        # calculated PCK frequencies
        sym_pck_freq = clk_comp.createIntegerSymbol("PCK" +str(i)+"_CLOCK_FREQUENCY", sym_prog_clk_menu)
        sym_pck_freq.setLabel("Programmable clock #"+str(i)+" Frequency (HZ)")
        sym_pck_freq.setDefaultValue(0)
        sym_pck_freq.setDependencies(update_programmable_clk_frequency, ["PMC_SCER_PCK" + str(i),
                                                                         "PMC_PCK" + str(i) + "_CSS",
                                                                         "PMC_PCK" + str(i) + "_PRES",
                                                                         "SLOW_CLK_FREQUENCY",
                                                                         "MAIN_CLK_FREQUENCY",
                                                                         "PLLA_CLK_FREQUENCY",
                                                                         "UPLL_CLK_FREQUENCY",
                                                                         "MCK_CLK_FREQUENCY",
                                                                         "AUDIO_CLK_FREQUENCY"])
        sym_pck_freq.setReadOnly(True)
        sama5d2_pck_clk_sym_dict["PCK" + str(i) + "_CLOCK_FREQUENCY"] = sym_pck_freq


def __lcd_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    LCD Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """

    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # enables LCDCK but clock PID and selection is all done in LCD module
    lcd_menu = clk_comp.createMenuSymbol("LCDCK", clk_menu)
    lcd_menu.setLabel("LCD Clock Configuration")

    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")
    bitfield_pmc_scer_lcdck = reg_pmc_scer.getBitfield("LCDCK")

    sym_lcdclk = clk_comp.createBooleanSymbol("PMC_SCER_LCDCK", lcd_menu)
    sym_lcdclk.setLabel(bitfield_pmc_scer_lcdck.getDescription())
    sym_lcdclk.setDefaultValue(False)

    sym_lcd_clk_freq = clk_comp.createIntegerSymbol("LCD_CLK_FREQUENCY", lcd_menu)
    sym_lcd_clk_freq.setLabel("LCD clock frequency(Hz)")
    sym_lcd_clk_freq.setReadOnly(True)
    sym_lcd_clk_freq.setDependencies(update_lcd_clk_frequency, ["MCK_CLK_FREQUENCY",
                                                                "PMC_SCER_LCDCK"])


def __isc_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    ISC Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """

    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # enables ISC but clock PID and selection is all done in ISC module
    isc_menu = clk_comp.createMenuSymbol("ISCCK", clk_menu)
    isc_menu.setLabel("ISC Clock Configuration")

    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")
    bitfield_pmc_scer_iscck = reg_pmc_scer.getBitfield("ISCCK")

    sym_iscclk = clk_comp.createBooleanSymbol("PMC_SCER_ISCCK", isc_menu)
    sym_iscclk.setLabel(bitfield_pmc_scer_iscck.getDescription())
    sym_iscclk.setDefaultValue(False)

    sym_isc_clk_freq = clk_comp.createIntegerSymbol("ISC_CLK_FREQUENCY", isc_menu)
    sym_isc_clk_freq.setLabel("ISC clock frequency(Hz)")
    sym_isc_clk_freq.setReadOnly(True)
    sym_isc_clk_freq.setDependencies(update_isc_clk_frequency, ["MCK_CLK_FREQUENCY",
                                                                "PMC_SCER_ISCCK"])


def __create_peripheral_clock_frequency_symbols(clock_comp, clk_menu):
    """
    Create peripheral clock frequency symbols
    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    """
    # iterate through all modules in ATDF
    modules = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals").getChildren()
    for module_index in range(0, len(modules)):
        module_name = modules[module_index].getAttribute("name")

        # Get the symbol constructor for the module.
        # Returns the default constructor if no specialized constructors are available for the module.
        sym_constructor = freq_sym_constructor_dict.get(module_name, create_default_freq_symbol)

        # iterate and create symbols for each instance
        instances = modules[module_index].getChildren()
        for instance_index in range(0, len(instances)):
            instance_name = instances[instance_index].getAttribute("name")
            clock_attribute = ATDF.getNode(
                "/avr-tools-device-file/devices/device/peripherals/module@[name=\"" + module_name + "\"]\
                 /instance@[name=\"" + instance_name + "\"]/parameters/param@[name=\"CLOCK_ID\"]")

            # skip instances which do not have clock_id
            if clock_attribute is not None:
                sym_constructor(instance_name, clock_comp, clk_menu)


global create_default_freq_symbol
def create_default_freq_symbol (instance_name, clock_comp, clk_menu):
    # find the bus clock freq symbol
    bus_clk_freq = "PCLOCK_HS_CLOCK_FREQUENCY" if instance_name in hs_peripherals_list else "PCLOCK_LS_CLOCK_FREQUENCY"
    
    sym_peripheral_clock_freq = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    sym_peripheral_clock_freq.setVisible(False)
    sym_peripheral_clock_freq.setReadOnly(True)
    sym_peripheral_clock_freq.setDefaultValue(Database.getSymbolValue("core", bus_clk_freq))
    sym_peripheral_clock_freq.setDependencies(update_peripheral_clock_frequencies, [bus_clk_freq])


global create_tc_clock_frequency_symbol
def create_tc_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    # each TC only has 3 channels(0,1 and 2). TC plib expects a dummy symbol for Channel 3 which
    # is related to quadrature mode calculations
    for channel_num in range(4):
        tc_channel_id = instance_name + "_CH" + str(channel_num) + "_CLOCK_FREQUENCY"
        tc_channel_symbol = clock_comp.createIntegerSymbol(tc_channel_id, clk_menu)
        tc_channel_symbol.setVisible(False)
        tc_channel_symbol.setReadOnly(True)
        tc_channel_symbol.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
        tc_channel_symbol.setDependencies(update_tc_clock_frequency,
                                          ["PCLOCK_LS_CLOCK_FREQUENCY",
                                           "SLOW_CLK_FREQUENCY",
                                           instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                           instance_name.lower() + ".TC" + str(channel_num) + "_CMR_TCCLKS",
                                           instance_name.lower() + ".TC" + str(channel_num) + "_ENABLE"])

global create_uart_clock_frequency_symbol
def create_uart_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    uart_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    uart_clock_freq_sym.setVisible(False)
    uart_clock_freq_sym.setReadOnly(True)
    uart_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    uart_clock_freq_sym.setDependencies(update_uart_clock_frequency, ["PCLOCK_LS_CLOCK_FREQUENCY",
                                                                      instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                                                      instance_name.lower() + ".UART_CLK_SRC"])


global create_flexcom_clock_frequency_symbol
def create_flexcom_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    flexcom_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    flexcom_clock_freq_sym.setVisible(False)
    flexcom_clock_freq_sym.setReadOnly(True)
    flexcom_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    flexcom_clock_freq_sym.setDependencies(update_flexcomm_clock_frequency,
                                              ["PCLOCK_LS_CLOCK_FREQUENCY",
                                               instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                               instance_name.lower() + ".FLEXCOM_MODE",
                                               instance_name.lower() + ".FLEXCOM_USART_MR_USCLKS",
                                               instance_name.lower() + ".FLEXCOM_SPI_MR_BRSRCCLK",
                                               instance_name.lower() + ".FLEXCOM_TWI_CWGR_BRSRCCLK"])


global create_twihs_clock_frequency_symbol
def create_twihs_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    twihs_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    twihs_clock_freq_sym.setVisible(False)
    twihs_clock_freq_sym.setReadOnly(True)
    twihs_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    twihs_clock_freq_sym.setDependencies(update_twihs_clock_frequency,
                                           ["PCLOCK_LS_CLOCK_FREQUENCY",
                                            instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                            instance_name.lower() + ".TWIHS_CLK_SRC"])


global create_mcan_clock_frequency_symbol
def create_mcan_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    mcan_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    mcan_clock_freq_sym.setVisible(False)
    mcan_clock_freq_sym.setReadOnly(True)
    mcan_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY"))
    mcan_clock_freq_sym.setDependencies(update_mcan_clock_frequency, [instance_name + "_GENERIC_CLOCK_FREQUENCY"])


global create_spi_clock_frequency_symbol
def create_spi_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    spi_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    spi_clock_freq_sym.setVisible(False)
    spi_clock_freq_sym.setReadOnly(True)
    spi_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    spi_clock_freq_sym.setDependencies(update_spi_clock_frequency, ["PCLOCK_LS_CLOCK_FREQUENCY",
                                                                      instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                                                      instance_name.lower() + ".SPI_CLK_SRC"])
global create_adc_clock_source_frequency_symbol
def create_adc_clock_source_frequency_symbol(instance_name, clock_comp, clk_menu):
    adc_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    adc_clock_freq_sym.setVisible(False)
    adc_clock_freq_sym.setReadOnly(True)
    adc_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY"))
    adc_clock_freq_sym.setDependencies(update_adc_clock_frequency, ["PCLOCK_LS_CLOCK_FREQUENCY",
                                                                      instance_name + "_GENERIC_CLOCK_FREQUENCY",
                                                                      instance_name.lower() + ".ADC_CLK_SRC"])

global create_sdmmc_clock_frequency_symbol
def create_sdmmc_clock_frequency_symbol(instance_name, clock_comp, clk_menu):
    sdmmc_clock_freq_sym = clock_comp.createIntegerSymbol(instance_name + "_CLOCK_FREQUENCY", clk_menu)
    sdmmc_clock_freq_sym.setVisible(False)
    sdmmc_clock_freq_sym.setReadOnly(True)
    sdmmc_clock_freq_sym.setDefaultValue(Database.getSymbolValue("core", instance_name + "_GENERIC_CLOCK_FREQUENCY"))
    sdmmc_clock_freq_sym.setDependencies(update_sdmmc_clock_frequency, [instance_name + "_GENERIC_CLOCK_FREQUENCY"])


global freq_sym_constructor_dict
freq_sym_constructor_dict = {"TC": create_tc_clock_frequency_symbol,
                             "UART": create_uart_clock_frequency_symbol,
                             "FLEXCOM": create_flexcom_clock_frequency_symbol,
                             "MCAN": create_mcan_clock_frequency_symbol,
                             "SPI": create_spi_clock_frequency_symbol,
                             "ADC": create_adc_clock_source_frequency_symbol,
                             "TWIHS": create_twihs_clock_frequency_symbol,
                             "SDMMC": create_sdmmc_clock_frequency_symbol}

# Add menu symbol dependencies
def set_fixed_clock_symbol_dependencies():
    # slow clock frequency dependencies
    sama5d2_fixed_clk_sym_dict["SLOW_CLK_FREQUENCY"].setDependencies(update_slow_clock_frequency, ["SCK_CR_OSCSEL"])

    # main clock frequency symbol dependencies
    sama5d2_fixed_clk_sym_dict["MAIN_CLK_FREQUENCY"].setDependencies(update_main_clock_frequency,
                                                                     ["CKGR_MOR_MOSCXTEN",
                                                                      "CKGR_MOR_MOSCXTBY",
                                                                      "MAIN_CRYSTAL_FREQUENCY",
                                                                      "CKGR_MOR_MOSCRCEN",
                                                                      "CKGR_MOR_MOSCSEL"])
    # PLLA clock frequency dependencies
    sama5d2_fixed_clk_sym_dict["PLLA_CLK_FREQUENCY"].setDependencies(update_plla_clock_frequency,
                                                                     ["CKGR_PLLAR_MULA0",
                                                                      "CKGR_PLLAR_DIVA",
                                                                      "CKGR_PLLA_MULA",
                                                                      "CKGR_PLLAR_PLLDIVA2"])

    # UTMI PLL clock frequency dependencies
    sama5d2_fixed_clk_sym_dict["UTMI_CKTRIM_FREQ"].setDependencies(update_utmi_ref_clock_frequency,
                                                                   ["PMC_CKGR_UCKR_UPLLEN",
                                                                    "MAIN_CLK_FREQUENCY"])

    # Processor clock symbol dependencies
    sama5d2_fixed_clk_sym_dict["CPU_CLOCK_FREQUENCY"].setDependencies(update_processor_clock_frequency,
                                                                      ["PMC_MCKR_CSS",
                                                                       "PMC_MCKR_PRES",
                                                                       "SLOW_CLK_FREQUENCY",
                                                                       "MAIN_CLK_FREQUENCY",
                                                                       "PLLA_CLK_FREQUENCY",
                                                                       "UPLL_CLK_FREQUENCY"])

    # MCK clock symbol dependencies
    sama5d2_fixed_clk_sym_dict["MCK_CLK_FREQUENCY"].setDependencies(update_mck_clock_frequency,
                                                                    ["CPU_CLOCK_FREQUENCY",
                                                                     "PMC_MCKR_MDIV"])

    # Low speed bus clock symbol dependencies
    sama5d2_fixed_clk_sym_dict["PCLOCK_LS_CLOCK_FREQUENCY"].setDependencies(update_pclock_ls_frequency,
                                                                            ["MCK_CLK_FREQUENCY",
                                                                             "PMC_MCKR_H32MXDIV"])


# Lock all fixed clock menus
def use_fixed_clocks():
    for name, symbol in sama5d2_fixed_clk_sym_dict.items():
        if symbol.getType() != "Comment":
            symbol.setReadOnly(True)


if __name__ == "__main__":
    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_SAM_A5D2", None)
    SYM_CLK_MENU.setLabel("Clock (PMC)")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

    PMC_REGISTERS = Register.getRegisterModule("PMC")
    SCKC_REGISTERS = Register.getRegisterModule("SCKC")
    SFR_REGISTERS = Register.getRegisterModule("SFR")

    # Define a symbol to identify whether the clocks configured by the bootloaders should be used or not
    # This symbol is not visible to the user
    sym_use_bootloader_clocks = coreComponent.createBooleanSymbol("USE_BOOTLOADER_CLOCKS", SYM_CLK_MENU)
    sym_use_bootloader_clocks.setVisible(False)
    sym_use_bootloader_clocks.setDefaultValue(True)

    # Slow clock
    __slow_clock_menu(coreComponent, SYM_CLK_MENU)

    # Main clock
    __main_clock_menu(coreComponent, SYM_CLK_MENU)

    # PLLA clock
    __plla_clock_menu(coreComponent, SYM_CLK_MENU)

    # UTMI clock
    __utmi_pll_clock_menu(coreComponent, SYM_CLK_MENU)

    # Master clock
    __mck_clock_menu(coreComponent, SYM_CLK_MENU)

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

    # create peripheral clock frequency symbols that gets updated based on the selected source clock
    __create_peripheral_clock_frequency_symbols(coreComponent, SYM_CLK_MENU)

    # If the system is configured to use clocks set by bootloader, do not allow the
    # user to modify the processor and master clocks
    if sym_use_bootloader_clocks.getValue() == True:
        use_fixed_clocks()
    # else enable dependency callbacks for the clock logic to work correctly
    else:
        set_fixed_clock_symbol_dependencies()

    # MPDDRC is enabled by bootloader so make sure we don't disable it
    Database.setSymbolValue("core", "MPDDRC_CLOCK_ENABLE", True, 1)

    # File handling
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

    # Add clock related code to common files
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
