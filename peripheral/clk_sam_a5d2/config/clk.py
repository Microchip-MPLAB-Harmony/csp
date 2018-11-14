
from os.path import join
from xml.etree import ElementTree

global generic_list
#UART, SPI, and TWI peripherals claim to be able to use GCLK but aren't in table 33-1
generic_list = {"FLEXCOM0", "FLEXCOM1", "FLEXCOM2", "FLEXCOM3", "FLEXCOM4", "TC0", "TC1", "ADC", "LCDC", "I2SC0", "I2SC1", "MCAN0", "MCAN1", "CLASSD"};

# Peripherals connected to 64 bit AHB matrix (i.e. with HS bus clocks)
hs_peripherals_list = ["XDMAC0", "XDMAC1", "AESB", "MPDDRC", "SDMMC0", "SDMMC1", "LCDC", "ISC", "QSPI0", "QSPI1"]

# Peripherals supporting multiple clock options
multi_clock_peripheral_list = ["TC"]

global DICT_PCER0
global DICT_PCER1

def periphFreqCalc(symbol, event):
    symbol.setValue(int(event["value"]), 2)

#currently this is a place holder and frequency is locked to the PCLOCK_LS
def UpdateTCClockFrequency(symbol,event):
    pass

# if any channel of TC instance is enabled, enable the peripheral clock of that instance
global UpdateTCClockEnable
def UpdateTCClockEnable(symbol, event):
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

def __fixed_clock_menu(clk_comp, clk_menu):
    fc_menu = clk_comp.createMenuSymbol("CLK_FIXED", clk_menu);
    fc_menu.setLabel("Fixed Clocks");
    fc_menu.setDescription("List of clock values configured by the bootloader.  Changing these clocks will break any image running out of DDR.")

    clk = clk_comp.createIntegerSymbol("CLK_SLOW", fc_menu);
    clk.setLabel("Slow Clock (Hz)")
    clk.setValue(32768, 1)
    clk.setReadOnly(True)

    clk = clk_comp.createIntegerSymbol("CLK_MAIN", fc_menu);
    clk.setLabel("Main Clock (Crystal)(Hz)")
    clk.setValue(12000000, 1)
    clk.setReadOnly(True)

    clk = clk_comp.createIntegerSymbol("CLK_PLL", fc_menu);
    clk.setLabel("PLL Clock (Hz)")
    clk.setValue(498000000, 1)
    clk.setReadOnly(True)

    clk = clk_comp.createIntegerSymbol("CLK_MCK", fc_menu);
    clk.setLabel("Master Clock (MCK)(Hz)")
    clk.setValue(166000000, 1)
    clk.setReadOnly(True)

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
    clk_menu = clk_comp.createMenuSymbol("CLK_USB", clk_menu)
    clk_menu.setLabel("USB Clock Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get CKGR_UCKR register
    reg_ckgr_uckr = pmc_reg_group.getRegister("CKGR_UCKR")

    # get UPLLEN Bitfield of CKGR_UCKR register
    bitfield_ckgr_uckr_upllen = reg_ckgr_uckr.getBitfield("UPLLEN")

    # create symbol for UPLLEN Bitfield of CKGR_UCKR register
    sym_ckgr_uckr_upllen = clk_comp.createBooleanSymbol("PMC_CKGR_UCKR_UPLLEN", clk_menu)
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
    sym_pmc_scer_udp = clk_comp.createBooleanSymbol("PMC_SCER_UDPCLK", clk_menu)
    sym_pmc_scer_udp.setLabel(bitfield_pmc_scer_udpclk.getDescription())

    # get UHP bitfield of PMC_SCER register
    bitfield_pmc_scer_uhpclk = reg_pmc_scer.getBitfield("UHP")

    # get symbol for UDPCLK bitfield of PMC_SCER register
    sym_pmc_scer_uhpclk = clk_comp.createBooleanSymbol("PMC_SCER_UHPCLK", clk_menu)
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
    sym_usb_divider = clk_comp.createIntegerSymbol("PMC_USB_USBDIV", clk_menu)
    sym_usb_divider.setLabel(bitfield_pmc_usb_usbdiv.getDescription())
    sym_usb_divider.setMin(1)
    sym_usb_divider.setMax(16)
    sym_usb_divider.setDefaultValue(10)

def __generic_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Generic Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for generic clock
    clk_menu = clk_comp.createMenuSymbol("CLK_GENERIC", clk_menu)
    clk_menu.setLabel("Generic Clock Generator Configuration for select peripherals")

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
        sym_gclkx_menu = clk_comp.createMenuSymbol("CLK_GEN" + str(i), clk_menu)
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

                        sym_perip_clk.setDependencies(UpdateTCClockEnable, tc_enable_dependent_list)


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

    #currently these values are hard coded here and updated by the java gui
def __calculated_clock_frequencies(clk_comp, clk_menu):
    """
    Calculated Clock frequencies Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    """

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")

    sym_proc_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_proc_clk_freq.setLabel("Processor Clock Frequency (HZ)")
    sym_proc_clk_freq.setDefaultValue("498000000")
    sym_proc_clk_freq.setReadOnly(True)

    sym_master_clk_freq = clk_comp.createStringSymbol("MASTER_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_master_clk_freq.setLabel("Master Clock Frequency (HZ)")
    sym_master_clk_freq.setDefaultValue("166000000")
    sym_master_clk_freq.setReadOnly(True)

    periph_clk = clk_comp.createStringSymbol("PCLOCK_HS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    periph_clk.setLabel("HS Peripheral Clock Frequency (HZ)")
    periph_clk.setDefaultValue(sym_master_clk_freq.getDefaultValue())
    periph_clk.setReadOnly(True)

    periph_clk_ls = clk_comp.createStringSymbol("PCLOCK_LS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    periph_clk_ls.setLabel("LS Peripheral Clock Frequency (HZ)")
    periph_clk_ls.setDefaultValue(str(int(sym_master_clk_freq.getDefaultValue())/2))
    periph_clk_ls.setReadOnly(True)

    sym_pck0_freq = clk_comp.createStringSymbol("PCK0_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck0_freq.setLabel("Programmable clock #0 Frequency (HZ)")
    sym_pck0_freq.setDefaultValue("12000000")
    sym_pck0_freq.setReadOnly(True)

    sym_pck1_freq = clk_comp.createStringSymbol("PCK1_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck1_freq.setLabel("Programmable clock #1 Frequency (HZ)")
    sym_pck1_freq.setDefaultValue("6000000")
    sym_pck1_freq.setReadOnly(True)

    sym_pck2_freq = clk_comp.createStringSymbol("PCK2_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck2_freq.setLabel("Programmable clock #2 Frequency (HZ)")
    sym_pck2_freq.setDefaultValue("4000000")
    sym_pck2_freq.setReadOnly(True)

    sym_usb_fs_freq = clk_comp.createStringSymbol("USBFS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_usb_fs_freq.setLabel("USB Clock Frequency (HZ)")
    sym_usb_fs_freq.setDefaultValue("48000000")
    sym_usb_fs_freq.setReadOnly(True)

    sym_usb_hs_freq = clk_comp.createStringSymbol("USBHS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_usb_hs_freq.setLabel("USB High Speed Clock Frequency (HZ)")
    sym_usb_hs_freq.setDefaultValue("480000000")
    sym_usb_hs_freq.setReadOnly(True)

    for periph in generic_list:
        gen_clk = clk_comp.createStringSymbol(periph+"_PROGRAMMABLE_CLOCK_FREQUENCY", sym_calc_freq_menu)
        gen_clk.setLabel(periph + " Generic Clock Frequency (HZ)")
        #gen_clk.setDefaultValue("32768")
        gen_clk.setDefaultValue("166000000")
        gen_clk.setReadOnly(True)


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

    __fixed_clock_menu(coreComponent, SYM_CLK_MENU)

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

    # creates calculated frequencies menu
    __calculated_clock_frequencies(coreComponent, SYM_CLK_MENU)

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
                sym_peripheral_clock_freq.setDependencies(periphFreqCalc, ["core.PCLOCK_HS_CLOCK_FREQUENCY"])
            else:
                sym_peripheral_clock_freq.setDefaultValue(
                    int(Database.getSymbolValue("core", "PCLOCK_LS_CLOCK_FREQUENCY")))
                sym_peripheral_clock_freq.setDependencies(periphFreqCalc, ["core.PCLOCK_LS_CLOCK_FREQUENCY"])

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
            tc_dependent_symbol_list = ["tc"+str(tc_instance_number)+".TC"+str(tc_channel_number)+"__CMR_TCCLKS",
                                        "tc"+str(tc_instance_number)+".TC_PCK_CLKSRC",
                                        "core.PCLOCK_LS_CLOCK_FREQUENCY",
                                        "core.CLK_SLOW_XTAL",
                                        "tc"+str(tc_instance_number)+".TC"+str(tc_channel_number)+"_ENABLE"]
            tc_channel_symbol.setDependencies(UpdateTCClockFrequency, tc_dependent_symbol_list)


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
