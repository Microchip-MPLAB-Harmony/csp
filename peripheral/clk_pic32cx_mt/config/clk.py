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

from os import path
from xml.etree import ElementTree as ET

#Set this to true, if the clock frequencies need to be shown on the tree view
# (used for debugging)
global show_frequency_sym
show_frequency_sym = False

#PLL clocks
global pll_dict
pll_dict = {
            "PLLA":{"source": (("TD_SLOW_CLOCK", "0", "TD slow clock"),
                               ("MAINCK", "1", "Main Clock")),
                    "mul_max": 2**15 - 1,
                    "output": 2,
                    "min_freq": 380,
                    "max_freq": 600},
            "PLLB":{"source": (("PLLACK0", "0", "PLLA output 0"),
                                ("MAINCK", "0", "Main Clock")),
                    "mul_max": 2**8 - 1,
                    "output": 1,
                    "min_freq": 300,
                    "max_freq": 600},
            "PLLC":{"source": (("PLLACK0", "0", "PLLA output 0"),
                                ("MAINCK", "0", "Main Clock")),
                    "mul_max": 2**8 - 1,
                    "output": 1,
                    "min_freq": 300,
                    "max_freq": 600}
            }

global mck1div_periph_list
mck1div_periph_list = ["MEM2MEM1", "PIOD", "UART", "MCSPI", "PWM", "MATRIX3"]

global mck1_periph_list
mck1_periph_list = ["MATRIX2"]

global mck0_periph_list
mck0_periph_list = ["SEFC0", "SEFC1", "CPKCC", "MATRIX0"]


global get_bitfield_node
def get_bitfield_node(module_node, group, register, bitfield):
    xpathstr = ("./register-group[@name=\"{0}\"]/register[@name=\"{1}\"]"
                "/bitfield[@name=\"{2}\"]").format(group, register, bitfield)
    return module_node.find(xpathstr)


global get_valuegroup_node
def get_valuegroup_node(module_node, group, register, bitfield):
    vg_name = get_bitfield_node(module_node, group,
                                             register, bitfield).get("values")
    vg_xpath = "./value-group[@name=\""+ vg_name +"\"]"
    return module_node.find(vg_xpath)


def set_symbol_attributes(symbol, module_node, group, register, bitfield,
                                                                label= True):
    bit_field_node =  get_bitfield_node(module_node, group, register, bitfield)
    if label:
        symbol.setLabel(bit_field_node.get("name"))
    symbol.setDescription(bit_field_node.get("caption"))


def set_kv_symbol_attributes(symbol, module_node, group, register, bitfield,
                                                            set_label = True):
    bitfield_node = get_bitfield_node(module_node, group, register, bitfield)
    xpathstr = "./value-group[@name=\""+ bitfield_node.get("values") +"\"]"
    val_grp_node = module_node.find(xpathstr)
    for value_node in val_grp_node:
        symbol.addKey(value_node.get("name"),
                      value_node.get("value"),
                      value_node.get("caption"))
    if set_label:
        symbol.setLabel(bitfield_node.get("name"))
        symbol.setDescription(bitfield_node.get("caption"))


def update_td_slck(symbol, event):
    osel = event['source'].getSymbolByID("CLK_TDXTALSEL")
    value = 0
    if osel.getSelectedKey() == "RC":
        symbol.clearValue()
    else:
        symbol.setValue(32768)


def update_mainck(symbol, event):
    oscsel = event['source'].getSymbolByID("CLK_MOSCSEL")
    xtfreq = event['source'].getSymbolByID("CLK_MOSCXTFREQ")
    rcen = event['source'].getSymbolByID("CLK_MOSCRCEN")
    xten = event['source'].getSymbolByID("CLK_MOSCXTEN")

    value = 0
    if oscsel.getValue() == 0:
        if rcen.getValue():
            value = 12000000
        else:
            value = 0
    else:
        if xten.getValue():
            value = xtfreq.getValue()
        else:
            value = 0
    symbol.setValue(value)


def update_pll_ref_clock(symbol, event):
    pll = symbol.getID().split("_")[0]
    pllms = int(event['source'].getSymbolValue("CLK_{0}_PLLMS".format(pll)))
    source_freq = event['source'].getSymbolValue(
                                pll_dict[pll]["source"][pllms][0]+"_FREQUENCY")
    symbol.setValue(source_freq)


def update_pll_core_freq(symbol, event):
    comp = event["source"]
    pll = symbol.getID().split("_")[0]
    enpll =  comp.getSymbolValue("CLK_{0}_ENPLL".format(pll))
    if enpll:
        source_freq = comp.getSymbolValue("{0}_REFCLK_FREQUENCY".format(pll))
        mul = comp.getSymbolValue("CLK_{0}_MUL".format(pll))
        fracr = comp.getSymbolValue("CLK_{0}_FRACR".format(pll))
        symbol.setValue(int((source_freq * (mul + 1 + (float(fracr)/2**22)))))
    else:
        symbol.clearValue()


def update_pll_output_freq(symbol, event):
    pll = symbol.getID().split("_")[0].split("CK")
    #Only PLLA has two clock outputs
    if pll[0] != "PLLA":
        pll[1] = "0"
    pllcore_clk = event["source"].getSymbolValue(
                                        "{0}_CORECLK_FREQUENCY".format(pll[0]))
    enable = event['source'].getSymbolValue(
                                    "CLK_{0}_ENPLLO{1}".format(pll[0], pll[1]))
    divpmc = event['source'].getSymbolValue(
                                    "CLK_{0}_DIVPMC{1}".format(pll[0], pll[1]))
    if enable:
        symbol.setValue(int(round((pllcore_clk / (divpmc + 1)), -2)))
    else:
        symbol.clearValue()


def update_mck0_freq(symbol, event):
    comp = event["source"]
    source_clk = comp.getSymbolByID("CLK_CPU_CKR_CSS"
                                            ).getSelectedKey() + "_FREQUENCY"
    div = comp.getSymbolByID("CLK_CPU_CKR_PRES"
                                            ).getSelectedKey().split("CLK_")[1]
    symbol.setValue(comp.getSymbolValue(source_clk)/int(div))


def update_mck1_freq(symbol, event):
    comp = event["source"]
    if comp.getSymbolValue("CLK_SCER_CPBMCK"):
        source_clk = comp.getSymbolByID("CLK_CPU_CKR_CPCSS").getSelectedKey()
        pres = comp.getSymbolByID("CLK_CPU_CKR_CPPRES").getSelectedKey()
        symbol.setValue(comp.getSymbolValue(source_clk+ "_FREQUENCY")/
                                            int(pres.split("CLK_")[1]))
    else:
        symbol.clearValue()


def update_mckdiv_freq(symbol, event):
    comp = event["source"]
    mckid = symbol.getID().split("_FREQUENCY")[0]
    src_clk = comp.getSymbolValue("MCK{0}_FREQUENCY".format(mckid[3]))
    div = 2 if comp.getSymbolValue("CLK_CPU_CKR_RATIO_" + mckid) else 1
    symbol.setValue(src_clk/div)


def update_cpu1_freq(symbol, event):
    comp = event["source"]
    cpck = comp.getSymbolValue("CLK_SCER_CPCK")
    if cpck:
        symbol.setValue(comp.getSymbolValue("MCK1_FREQUENCY"))
    else:
        symbol.clearValue()


global get_peripheral_mck_id
def get_peripheral_mck_id(instance_name):
    if instance_name in mck1div_periph_list:
        src_clk =  "MCK1DIV"
    elif instance_name in mck1_periph_list:
        src_clk = "MCK1"
    elif instance_name in mck0_periph_list:
        src_clk = "MCK0"
    else:
        src_clk = "MCK0DIV"

    return src_clk


def update_gclk_freq(symbol, event):
    comp = event["source"]
    instance_name = symbol.getID().split("_")[0]
    gclk_css = comp.getSymbolByID("CLK_"+instance_name+"_GCLKCSS")
    gclk_div = comp.getSymbolValue("CLK_"+instance_name+"_GCLKDIV")
    input_freq = comp.getSymbolValue(gclk_css.getSelectedKey()+"_FREQUENCY")
    if comp.getSymbolValue("CLK_"+instance_name+"_GCLKEN"):
        symbol.setValue(input_freq / (gclk_div + 1))
    else:
        symbol.clearValue()


#Generic module clock frequency setup
def setup_gclk_module_freq(lcomp, rcomp, module, instance):
    pcr_menu = rcomp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = lcomp.createIntegerSymbol(instance + "_CLOCK_FREQUENCY",
                                                                     pcr_menu)
    pcr_freq.setReadOnly(True)
    pcr_freq.setVisible(show_frequency_sym)
    mckid = get_peripheral_mck_id(instance)
    pcr_freq.setDefaultValue(rcomp.getSymbolValue(mckid +"_FREQUENCY"))
    pcr_freq.setDependencies(lambda symbol, event:
                         symbol.setValue(event["value"]), [mckid +"_FREQUENCY"])


def setup_flexcom_module_frequency(lcomp, rcomp, module, instance):
    pcr_menu = rcomp.getSymbolByID("CLK_PCR_MENU")
    pcr_freq = lcomp.createIntegerSymbol(instance + "_CLOCK_FREQUENCY",
                                                                     pcr_menu)
    pcr_freq.setReadOnly(True)
    pcr_freq.setVisible(show_frequency_sym)
    pcr_freq.setDefaultValue(rcomp.getSymbolValue("MCK0DIV_FREQUENCY"))
    pcr_freq.setDependencies(update_flexcom_clock_frequency,
                [  "MCK0DIV_FREQUENCY",
                    instance + "_GCLK_FREQUENCY",
                    instance.lower() + ".FLEXCOM_MODE",
                    instance.lower() + ".FLEXCOM_USART_MR_USCLKS",
                    instance.lower() + ".FLEXCOM_SPI_MR_BRSRCCLK",
                    instance.lower() + ".FLEXCOM_TWI_CWGR_BRSRCCLK"])


def setup_tc_clock_frequency(lcomp, rcomp, module, instance):
    pcr_menu = rcomp.getSymbolByID("CLK_PCR_MENU")
    for channel in range(4):
        tc_ch_freq = lcomp.createIntegerSymbol(
            "{0}_CH{1}_CLOCK_FREQUENCY".format(instance, channel), pcr_menu)
        tc_ch_freq.setReadOnly(True)
        tc_ch_freq.setVisible(show_frequency_sym)
        tc_ch_freq.setDependencies(update_tc_clock_frequency,
                    ["MCK0DIV_FREQUENCY",
                    "MD_SLOW_CLK_FREQUENCY",
                    "{0}_GCLK_FREQUENCY".format(instance),
                    "{0}.TC{1}_CMR_TCCLKS".format(instance.lower(), channel),
                    "{0}.TC{1}_ENABLE".format(instance.lower(), channel)])


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
    mck0div_freq = clk_comp.getSymbolValue("MCK0DIV_FREQUENCY")

    # check if component exists and the relevant channel is enabled
    if tc_comp is not None and tc_comp.getSymbolValue("TC{0}_ENABLE".format(channel_num)):
        # Find the current clock source for the channel
        clk_src_sym = tc_comp.getSymbolByID("TC{0}_CMR_TCCLKS".format(channel_num))
        clk_src = clk_src_sym.getKeyDescription(clk_src_sym.getValue())

        # if clock source is processor independent GCLK
        if (clk_src == "GCLK"):
            clk_frequency = clk_comp.getSymbolValue("TC{0}_GCLK_FREQUENCY".format(instance_num))
        # if clock  source is MCK/8
        elif (clk_src == "MCK0DIV/8"):
            clk_frequency = mck0div_freq / 8
        # if clock  source is MCK/32
        elif (clk_src == "MCK0DIV/32"):
            clk_frequency = mck0div_freq / 32
        # if clock  source is MCK/128
        elif (clk_src == "MCK0DIV/128"):
            clk_frequency = mck0div_freq / 128
        # if clock  source is SLOW CLOCK
        elif (clk_src == "TD_SLCK"):
            clk_frequency = clk_comp.getSymbolValue("MD_SLOW_CLK_FREQUENCY")
        # default  clock source is MCK0DIV
        else:
            clk_frequency = mck0div_freq
        symbol.setValue(clk_frequency)


global update_flexcom_clock_frequency
def update_flexcom_clock_frequency(symbol,event):
    frequency = -1
    clk_sym_map = { "USART": "FLEXCOM_USART_MR_USCLKS",
                    "SPI": "FLEXCOM_SPI_MR_BRSRCCLK",
                    "TWI": "FLEXCOM_TWI_CWGR_BRSRCCLK"
                  }
    instance_name = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    flexcom_comp = Database.getComponentByID(instance_name.lower())
    if flexcom_comp is not None:
        clk_sym = clk_sym_map[flexcom_comp.getSymbolByID("FLEXCOM_MODE").getSelectedKey()]
        source_clock = flexcom_comp.getSymbolByID(clk_sym).getSelectedKey()
        mck0div_freq = event["source"].getSymbolValue("MCK0DIV_FREQUENCY")
        # Source clock is bus clock
        if source_clock == "MCK" or source_clock == "PERIPH_CLK":
            frequency = mck0div_freq
        # Source clock is bus clock / 8
        elif source_clock == "DIV":
            frequency = mck0div_freq / 8
        # Source clock is GCLK
        elif source_clock == "GCLK":
            frequency = event["source"].getSymbolValue(instance_name + "_GCLK_FREQUENCY")
        # Source clock is external, set the internal frequency to zero
        else:
            frequency = 0

        symbol.setValue(frequency)


def update_pck_freq(symbol, event):
    index = int(symbol.getID().split("PCK")[1].split("_")[0])
    pckx_pres = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_PRES")
    pckx_css = event['source'].getSymbolByID("CLK_PCK"+str(index)+"_CSS")
    enabled = event['source'].getSymbolValue("CLK_SCER_PCK"+str(index))
    input_freq = 0
    if enabled == True:
        input_freq = event['source'].getSymbolValue(
                                    pckx_css.getSelectedKey()+"_FREQUENCY")
    symbol.setValue(input_freq / (pckx_pres.getValue() + 1))


if __name__ == "__main__":

    #Get a local variable to avoid linter warning everywhere
    clk_component = coreComponent

    atdf_file_path = path.join(Variables.get("__DFP_PACK_DIR"),
                               "atdf",
                               Variables.get("__PROCESSOR") + ".atdf")
    atdf_root = ET.parse(atdf_file_path).getroot()

    pmc_node = atdf_root.find( "modules/module[@name=\"PMC\"]")
    supc_node = atdf_root.find( "modules/module[@name=\"SUPC\"]")

    menu = clk_component.createMenuSymbol("CLK_MENU", None)
    menu.setLabel("Clock")
    menu.setDescription("Clock configuration")

    #Get a handle to this components remote interface
    clk_remote_component = menu.getComponent()

    #############################  Slow clock  ################################

    supc_menu = clk_component.createMenuSymbol("CLK_SUPC_MENU", menu)
    supc_menu.setLabel("Slow Clock (SLCK)")

    td_xtalsel = clk_component.createKeyValueSetSymbol("CLK_TDXTALSEL",
                                                                    supc_menu)
    set_kv_symbol_attributes(td_xtalsel,
                             supc_node, "SUPC", "SUPC_CR", "TDXTALSEL")

    oscbypass = clk_component.createBooleanSymbol("CLK_OSCBYPASS", supc_menu)
    set_symbol_attributes(oscbypass, supc_node,"SUPC", "SUPC_MR", "OSCBYPASS")

    md_slck = clk_component.createIntegerSymbol("MD_SLOW_CLK_FREQUENCY",
                                                                    supc_menu)
    md_slck.setReadOnly(True)
    md_slck.setDefaultValue(32000)

    td_slck = clk_component.createIntegerSymbol("TD_SLOW_CLOCK_FREQUENCY",
                                                                    supc_menu)
    td_slck.setReadOnly(True)
    td_slck.setDependencies(update_td_slck, ["CLK_TDXTALSEL"])
    td_slck.setDefaultValue(32000)

    #############################  Main clock  ################################

    mainck_menu = clk_component.createMenuSymbol("CLK_MAINCK_MENU", menu)
    mainck_menu.setLabel("Main Clock (MAINCK)")

    moscrcen = clk_component.createBooleanSymbol("CLK_MOSCRCEN", mainck_menu)
    set_symbol_attributes(moscrcen, pmc_node,"PMC", "CKGR_MOR", "MOSCRCEN")
    moscrcen.setDefaultValue(True)

    moscxten = clk_component.createBooleanSymbol("CLK_MOSCXTEN", mainck_menu)
    set_symbol_attributes(moscxten, pmc_node,"PMC", "CKGR_MOR", "MOSCXTEN")

    moscxtby = clk_component.createBooleanSymbol("CLK_MOSCXTBY", mainck_menu)
    set_symbol_attributes(moscxtby, pmc_node,"PMC", "CKGR_MOR", "MOSCXTBY")

    moscxtst = clk_component.createIntegerSymbol("CLK_MOSCXTST", mainck_menu)
    set_symbol_attributes(moscxtst, pmc_node,"PMC", "CKGR_MOR", "MOSCXTST")
    moscxtst.setMin(0)
    moscxtst.setMax(255)

    moscsel = clk_component.createKeyValueSetSymbol("CLK_MOSCSEL",
                                                                mainck_menu)
    set_kv_symbol_attributes(moscsel, pmc_node, "PMC", "CKGR_MOR", "MOSCSEL")

    moscxtfreq = clk_component.createIntegerSymbol("CLK_MOSCXTFREQ",
                                                                mainck_menu)
    moscxtfreq.setLabel("MOSCXTFREQ")
    moscxtfreq.setDescription("Main Oscillator/External Clock Frequency")
    moscxtfreq.setMin(12000000)
    moscxtfreq.setMax(48000000)

    mainck = clk_component.createIntegerSymbol("MAINCK_FREQUENCY", mainck_menu)
    mainck.setReadOnly(True)
    mainck.setDefaultValue(12000000)
    mainck.setDependencies(update_mainck, ['CLK_MOSCRCEN', 'CLK_MOSCXTEN',
                                           'CLK_MOSCSEL', 'CLK_MOSCXTFREQ'])

    ###############################  PLLs  ####################################

    for pll in sorted(pll_dict.keys()):
        pll_menu = clk_component.createMenuSymbol("CLK_{0}_MENU".format(pll),
                                                                         menu)
        pll_menu.setLabel(pll)

        enpll = clk_component.createBooleanSymbol("CLK_{0}_ENPLL".format(pll),
                                                   pll_menu)
        set_symbol_attributes(enpll, pmc_node,"PMC", "PMC_PLL_CTRL0", "ENPLL")

        pllms = clk_component.createKeyValueSetSymbol(
                                        "CLK_{0}_PLLMS".format(pll), enpll)
        set_symbol_attributes(pllms, pmc_node,"PMC", "PMC_PLL_CTRL0", "PLLMS")
        for kvd_tuple in pll_dict[pll]["source"]:
            pllms.addKey(kvd_tuple[0], kvd_tuple[1], kvd_tuple[2])
        pllms.setOutputMode("Value")

        mul = clk_component.createIntegerSymbol("CLK_{0}_MUL".format(pll),
                                                                     enpll)
        set_symbol_attributes(mul, pmc_node,"PMC", "PMC_PLL_CTRL1", "MUL")
        mul.setMin(0)
        mul.setMax(pll_dict[pll]["mul_max"])

        fracr = clk_component.createIntegerSymbol("CLK_{0}_FRACR".format(pll),
                                                                     enpll)
        set_symbol_attributes(fracr, pmc_node,"PMC", "PMC_PLL_CTRL2", "FRACR")
        fracr.setMin(0)
        fracr.setMax(2**22 - 1)

        enspread = clk_component.createBooleanSymbol(
                                      "CLK_{0}_ENSPREAD".format(pll), enpll)
        set_symbol_attributes(enspread, pmc_node,"PMC",
                                                "PMC_PLL_SSR", "ENSPREAD")

        step = clk_component.createIntegerSymbol("CLK_{0}_STEP".format(pll),
                                                                     enspread)
        set_symbol_attributes(step, pmc_node,"PMC", "PMC_PLL_SSR", "STEP")
        step.setMin(0)
        step.setMax(2**16 - 1)

        nstep = clk_component.createIntegerSymbol("CLK_{0}_NSTEP".format(pll),
                                                                     enspread)
        set_symbol_attributes(nstep, pmc_node,"PMC", "PMC_PLL_SSR", "NSTEP")
        nstep.setMin(0)
        nstep.setMax(2**8 -1)

        pllrefclk =  clk_component.createIntegerSymbol(
                                "{0}_REFCLK_FREQUENCY".format(pll),pll_menu)
        pllrefclk.setVisible(show_frequency_sym)
        pllrefclk.setDefaultValue(clk_remote_component.getSymbolValue(
                                pll_dict[pll]["source"][0][0]+"_FREQUENCY"))
        pllrefclk.setDependencies(update_pll_ref_clock,
                                [pll_dict[pll]["source"][0][0]+"_FREQUENCY",
                                 pll_dict[pll]["source"][1][0]+"_FREQUENCY",
                                 "CLK_{0}_PLLMS".format(pll)])

        corepllckmin = clk_component.createIntegerSymbol(
                            "{0}_MINCORECLK_FREQUENCY".format(pll),pll_menu)
        corepllckmin.setVisible(show_frequency_sym)
        corepllckmin.setDefaultValue(pll_dict[pll]["min_freq"] * 10**6)

        corepllck = clk_component.createIntegerSymbol(
                                "{0}_CORECLK_FREQUENCY".format(pll),pll_menu)
        corepllck.setVisible(show_frequency_sym)
        corepllck.setDependencies(update_pll_core_freq,
                                 ["{0}_REFCLK_FREQUENCY".format(pll),
                                  "CLK_{0}_ENPLL".format(pll),
                                  "CLK_{0}_MUL".format(pll),
                                  "CLK_{0}_FRACR".format(pll)])

        corepllckmax = clk_component.createIntegerSymbol(
                            "{0}_MAXCORECLK_FREQUENCY".format(pll),pll_menu)
        corepllckmax.setVisible(show_frequency_sym)
        corepllckmax.setDefaultValue(pll_dict[pll]["max_freq"] * 10**6)

        for index in range(pll_dict[pll]["output"]):
            enpllo = clk_component.createBooleanSymbol(
                            "CLK_{0}_ENPLLO{1}".format(pll, index), enpll)
            set_symbol_attributes(enpllo, pmc_node,"PMC",
                                        "PMC_PLL_CTRL0", "ENPLLO"+str(index))

            divpmc = clk_component.createIntegerSymbol(
                        "CLK_{0}_DIVPMC{1}".format(pll,index), enpllo)
            set_symbol_attributes(divpmc, pmc_node,"PMC",
                                        "PMC_PLL_CTRL0", "DIVPMC"+str(index))
            divpmc.setMin(0)
            divpmc.setMax(2**8 - 1)

            pllofreq_sym_name = "{0}CK{1}_FREQUENCY".format(pll,
                                  index if pll_dict[pll]["output"] > 1 else "")

            pllofreq = clk_component.createIntegerSymbol(pllofreq_sym_name,
                                                                    pll_menu)
            pllofreq.setReadOnly(True)
            pllofreq.setDependencies(update_pll_output_freq,
                                     ["{0}_CORECLK_FREQUENCY".format(pll),
                                      "CLK_{0}_DIVPMC{1}".format(pll,index),
                                      "CLK_{0}_ENPLLO{1}".format(pll, index)])

    ##################### Processor and System clocks #########################

    cpu_menu = clk_component.createMenuSymbol("CLK_CPU_MENU", menu)
    cpu_menu.setLabel("Processor Clock ")

    css = clk_component.createKeyValueSetSymbol("CLK_CPU_CKR_CSS", cpu_menu)
    set_kv_symbol_attributes(css, pmc_node, "PMC", "PMC_CPU_CKR", "CSS")
    css.setDefaultValue(1)

    pres = clk_component.createKeyValueSetSymbol("CLK_CPU_CKR_PRES", cpu_menu)
    set_kv_symbol_attributes(pres, pmc_node, "PMC", "PMC_CPU_CKR", "PRES")

    mck0freq = clk_component.createIntegerSymbol("MCK0_FREQUENCY",cpu_menu)
    mck0freq_dep_list = ["CLK_CPU_CKR_CSS", "CLK_CPU_CKR_PRES"]
    css_vg_node = get_valuegroup_node(pmc_node, "PMC", "PMC_CPU_CKR", "CSS")
    for css_value_node in css_vg_node:
        mck0freq_dep_list.append(css_value_node.get("name")+"_FREQUENCY")
    mck0freq.setDependencies(update_mck0_freq, mck0freq_dep_list)
    mck0freq.setReadOnly(True)
    mck0freq.setDefaultValue(mainck.getValue())

    if clk_remote_component.getSymbolValue("CPU_CORE_ID") == 1:
        cpu0_freq_name = "CPU0_CLOCK_FREQUENCY"
        systick0_freq_name = "SYSTICK0_CLOCK_FREQUENCY"
    else:
        cpu0_freq_name = "CPU_CLOCK_FREQUENCY"
        systick0_freq_name = "SYSTICK_CLOCK_FREQUENCY"

    cpufreq = clk_component.createIntegerSymbol(cpu0_freq_name, cpu_menu)
    cpufreq.setDependencies(lambda symbol,
                event:symbol.setValue(event["value"]), ["MCK0_FREQUENCY"])
    cpufreq.setReadOnly(True)
    cpufreq.setDefaultValue(mck0freq.getValue())

    systick_ext_freq = clk_component.createIntegerSymbol(systick0_freq_name, cpu_menu)
    systick_ext_freq.setDependencies(lambda symbol,
                event:symbol.setValue(event["value"]/8), ["MCK0_FREQUENCY"])
    systick_ext_freq.setReadOnly(True)
    systick_ext_freq.setDefaultValue(mck0freq.getValue()/8)

    ratio_mck0div = clk_component.createBooleanSymbol(
                                        "CLK_CPU_CKR_RATIO_MCK0DIV", cpu_menu)
    set_symbol_attributes(ratio_mck0div, pmc_node,"PMC", "PMC_CPU_CKR",
                                                            "RATIO_MCK0DIV")

    mck0divfreq = clk_component.createIntegerSymbol("MCK0DIV_FREQUENCY",
                                                                    cpu_menu)
    mck0divfreq.setDependencies(update_mckdiv_freq,
                            ["MCK0_FREQUENCY", "CLK_CPU_CKR_RATIO_MCK0DIV"])
    mck0divfreq.setReadOnly(True)
    mck0divfreq.setDefaultValue(mck0freq.getValue())

    ratio_mck0div2 = clk_component.createBooleanSymbol(
                                        "CLK_CPU_CKR_RATIO_MCK0DIV2", cpu_menu)
    set_symbol_attributes(ratio_mck0div2, pmc_node,"PMC", "PMC_CPU_CKR",
                                                            "RATIO_MCK0DIV2")

    mck0div2freq = clk_component.createIntegerSymbol("MCK0DIV2_FREQUENCY",
                                                                    cpu_menu)
    mck0div2freq.setDependencies(update_mckdiv_freq,
                            ["MCK0_FREQUENCY", "CLK_CPU_CKR_RATIO_MCK0DIV2"])
    mck0div2freq.setReadOnly(True)
    mck0div2freq.setDefaultValue(mck0freq.getValue())

    cpcss = clk_component.createKeyValueSetSymbol(
                                            "CLK_CPU_CKR_CPCSS", cpu_menu)
    set_kv_symbol_attributes(cpcss, pmc_node, "PMC", "PMC_CPU_CKR", "CPCSS")

    cppres = clk_component.createKeyValueSetSymbol(
                                            "CLK_CPU_CKR_CPPRES", cpu_menu)
    set_kv_symbol_attributes(cppres, pmc_node, "PMC", "PMC_CPU_CKR", "CPPRES")

    ratio_mck1div = clk_component.createBooleanSymbol(
                                        "CLK_CPU_CKR_RATIO_MCK1DIV", cpu_menu)
    set_symbol_attributes(ratio_mck1div, pmc_node,"PMC", "PMC_CPU_CKR",
                                                            "RATIO_MCK1DIV")

    cpbmck = clk_component.createBooleanSymbol("CLK_SCER_CPBMCK", cpu_menu)
    set_symbol_attributes(cpbmck, pmc_node,"PMC", "PMC_SCER", "CPBMCK")

    mck1freq = clk_component.createIntegerSymbol("MCK1_FREQUENCY",cpu_menu)
    mck1freq_dep_list = ["CLK_CPU_CKR_CPCSS",
                         "CLK_CPU_CKR_CPPRES",
                         "CLK_SCER_CPBMCK"]
    cpcss_vg_node = get_valuegroup_node(pmc_node, "PMC", "PMC_CPU_CKR",
                                                                    "CPCSS")
    for cpcss_value_node in cpcss_vg_node:
        mck1freq_dep_list.append(cpcss_value_node.get("name")+"_FREQUENCY")
    mck1freq.setDependencies(update_mck1_freq, mck1freq_dep_list)
    mck1freq.setReadOnly(True)

    mck1divfreq = clk_component.createIntegerSymbol("MCK1DIV_FREQUENCY",
                                                                    cpu_menu)
    mck1divfreq.setDependencies(update_mckdiv_freq,
                            ["MCK1_FREQUENCY", "CLK_CPU_CKR_RATIO_MCK1DIV"])
    mck1divfreq.setReadOnly(True)

    if get_bitfield_node(pmc_node,"PMC", "PMC_SCER", "CPCK")is not None:
        cpck = clk_component.createBooleanSymbol("CLK_SCER_CPCK", cpu_menu)
        set_symbol_attributes(cpck, pmc_node,"PMC", "PMC_SCER", "CPCK")

        if clk_remote_component.getSymbolValue("CPU_CORE_ID") == 1:
            cpck.setDefaultValue(True)
            cpu1_freq_name = "CPU_CLOCK_FREQUENCY"
            systick1_freq_name = "SYSTICK_CLOCK_FREQUENCY"
        else:
            cpu1_freq_name = "CPU1_CLOCK_FREQUENCY"
            systick1_freq_name = "SYSTICK1_CLOCK_FREQUENCY"

        cpu1freq = clk_component.createIntegerSymbol(cpu1_freq_name, cpu_menu)
        cpu1freq.setDependencies(update_cpu1_freq, ["CLK_SCER_CPCK",
                                                    "MCK1_FREQUENCY"])
        cpu1freq.setReadOnly(True)

        systick1_ext_freq = clk_component.createIntegerSymbol(systick1_freq_name, cpu_menu)
        systick1_ext_freq.setDependencies(lambda symbol,
                event:symbol.setValue(event["value"]/8), ["MCK1_FREQUENCY"])

    ################### Peripheral and Generic clocks #########################
    gclk_dict = {"FLEXCOM":[range(0,8), setup_flexcom_module_frequency],
                "QSPI":[range(0,8), setup_gclk_module_freq],
                "ADC":[range(0,8), setup_gclk_module_freq],
                "TC":[range(0,8), setup_tc_clock_frequency],
                "EMAFE":[range(0,8), setup_gclk_module_freq],
                "UART":[range(0,8), setup_gclk_module_freq],
                "MCSPI":[range(0,8), setup_gclk_module_freq],
    }

    pcr_menu = clk_component.createMenuSymbol("CLK_PCR_MENU", menu)
    pcr_menu.setLabel("Peripheral Clocks")

    gclk_menu = clk_component.createMenuSymbol("CLK_GCLK_MENU", menu)
    gclk_menu.setLabel("Generic Clocks")

    #Key value set symbol for UI to identify peripherals with GCLK support */
    gclk_ui_map = clk_component.createKeyValueSetSymbol("GCLK_INSTANCE_PID",
                                                                     gclk_menu)
    gclk_ui_map.setVisible(False)

    max_clock_id = 0
    peripheral_clock_list = []
    gclkcss_vg_node = get_valuegroup_node(pmc_node, "PMC", "PMC_PCR", "GCLKCSS")
    for module_node in atdf_root.find("devices/device/peripherals"):
        module_name = module_node.get("name")
        for instance_node in module_node:
            instance_name = instance_node.get("name")
            mck_id = get_peripheral_mck_id(instance_name)
            parameters_node = instance_node.find("parameters")
            if parameters_node is None:
                continue
            for param_node in parameters_node:
                if param_node.get("name").startswith("CLOCK_ID"):
                    clock_id  = param_node.get("value")
                    clock_id_suffix = instance_name +\
                         param_node.get("name").split("CLOCK_ID")[1]
                    pcr_en = clk_component.createBooleanSymbol(
                                clock_id_suffix + "_CLOCK_ENABLE", pcr_menu)
                    pcr_en.setLabel(clock_id_suffix)
                    peripheral_clock_list.append(clock_id_suffix + "_CLOCK_ENABLE")

                    if int(clock_id) > max_clock_id:
                        max_clock_id = int(clock_id)

                    id_name_map = clk_component.createStringSymbol(
                                        "CLK_ID_NAME_" + clock_id, pcr_menu)
                    id_name_map.setVisible(False)
                    id_name_map.setDefaultValue(clock_id_suffix)

                    if module_name not in gclk_dict.keys():
                        pcr_freq = clk_component.createIntegerSymbol(
                                instance_name + "_CLOCK_FREQUENCY", pcr_menu)
                        pcr_freq.setReadOnly(True)
                        pcr_freq.setVisible(show_frequency_sym)
                        pcr_freq.setDefaultValue(
                                clk_remote_component.getSymbolValue(
                                        mck_id +"_FREQUENCY"))
                        pcr_freq.setDependencies(
                                            lambda symbol, event:
                                            symbol.setValue(event["value"]),
                                            [mck_id + '_FREQUENCY'])
                    elif (module_name != "TC" or
                          clock_id_suffix.endswith("_CHANNEL0")):
                        gclk_ui_map.addKey(instance_name, clock_id, "")

            if module_name  in gclk_dict.keys():
                gclk_freq_deps = []
                gclk_periph = clk_component.createMenuSymbol(
                        "CLK_" + instance_name + "GCLK_MENU", gclk_menu)
                gclk_periph.setLabel(instance_name)

                gclk_en = clk_component.createBooleanSymbol(
                            "CLK_"+instance_name+"_GCLKEN", gclk_periph)
                gclk_en.setLabel("GCLKEN")
                gclk_freq_deps.append(gclk_en.getID())

                gclk_css = clk_component.createKeyValueSetSymbol(
                            "CLK_"+instance_name+"_GCLKCSS", gclk_periph)
                gclk_css.setLabel("GCLKCSS")
                gclk_css.setOutputMode("Value")
                for val_node in gclkcss_vg_node:
                    if int(val_node.get("value"), 0) in gclk_dict[module_name][0]:
                        gclk_css.addKey(val_node.get("name"),
                                        val_node.get("value"),
                                        val_node.get("caption"))
                        gclk_freq_deps.append(val_node.get("name") +
                                              "_FREQUENCY")
                gclk_freq_deps.append(gclk_css.getID())

                gclk_div = clk_component.createIntegerSymbol(
                            "CLK_"+instance_name+"_GCLKDIV", gclk_periph)
                gclk_div.setLabel("GCLKDIV")
                gclk_div.setMin(0)
                gclk_div.setMax(255)
                gclk_freq_deps.append(gclk_div.getID())

                gclk_freq = clk_component.createIntegerSymbol(
                    instance_name+"_GCLK_FREQUENCY", gclk_periph)
                gclk_freq.setReadOnly(True)
                gclk_freq.setDependencies(update_gclk_freq, gclk_freq_deps)

                gclk_dict[module_name][1](clk_component, clk_remote_component,
                                        module_name, instance_name)

    #Combo symbol for UI to identify peripherals with PMC clock */
    periph_clk_ui_list_sym = clk_component.createComboSymbol(
                     "PERIPHERAL_CLOCK_CONFIG", None, peripheral_clock_list)
    periph_clk_ui_list_sym.setVisible(False)

    max_clock_id_sym = clk_component.createIntegerSymbol(
                                            "CLK_MAX_PERIPHERAL_ID", pcr_menu)
    max_clock_id_sym.setVisible(False)
    max_clock_id_sym.setDefaultValue(max_clock_id)


    ######################## Programmable clocks ##############################
    pck_menu = clk_component.createMenuSymbol("CLK_PCK_MENU", menu)
    pck_menu.setLabel("Programmable Clocks")

    num_pcks = int(pmc_node.find(
            "register-group/register[@name=\"PMC_PCK\"]").get("count"))
    num_pckx_sym = clk_component.createIntegerSymbol("CLK_NUM_PCKS", pck_menu)
    num_pckx_sym.setVisible(False)
    num_pckx_sym.setDefaultValue(num_pcks)

    for pckx in range(0, num_pcks):
        pckx_freq_deps = []
        pckx_en = clk_component.createBooleanSymbol(
                                        "CLK_SCER_PCK"+str(pckx), pck_menu)
        pckx_en.setLabel("PCK"+str(pckx))
        pckx_freq_deps.append(pckx_en.getID())

        pckx_css = clk_component.createKeyValueSetSymbol(
                                        "CLK_PCK"+str(pckx)+"_CSS", pckx_en)
        set_kv_symbol_attributes(pckx_css, pmc_node, "PMC", "PMC_PCK", "CSS")
        pckx_freq_deps.append(pckx_css.getID())
        for value_node in get_valuegroup_node(pmc_node, "PMC", "PMC_PCK", "CSS"):
            pckx_freq_deps.append(value_node.get("name") + "_FREQUENCY")

        pckx_pres = clk_component.createIntegerSymbol(
                                        "CLK_PCK"+str(pckx)+"_PRES", pckx_en)
        set_symbol_attributes(pckx_css, pmc_node, "PMC", "PMC_PCK", "PRES")
        pckx_pres.setMin(0)
        pckx_pres.setMax(255)
        pckx_freq_deps.append(pckx_pres.getID())

        pckx_freq = clk_component.createIntegerSymbol(
                                    "PCK"+str(pckx)+"_FREQUENCY", pckx_en)
        pckx_freq.setReadOnly(True)
        pckx_freq.setDependencies(update_pck_freq, pckx_freq_deps)


    ###################### Default clock settings #############################
    #Configure XTAL as the slow clock source
    td_xtalsel.setSelectedKey("XTAL")

    #Turn off main RC
    moscrcen.setValue(False)

    #Configure PLLA0 to generate 20 MHz and PLLA1 to generate 200 MHz
    clk_remote_component.setSymbolValue("CLK_PLLA_MUL", 12206)
    clk_remote_component.setSymbolValue("CLK_PLLA_FRACR", 131072)
    clk_remote_component.setSymbolValue("CLK_PLLA_ENPLL", True)
    clk_remote_component.setSymbolValue("CLK_PLLA_DIVPMC0", 19)
    clk_remote_component.setSymbolValue("CLK_PLLA_ENPLLO0", True)
    clk_remote_component.setSymbolValue("CLK_PLLA_DIVPMC1", 1)
    clk_remote_component.setSymbolValue("CLK_PLLA_ENPLLO1", True)

    #Configure PLLB to generate 240 MHz
    clk_remote_component.setSymbolValue("CLK_PLLB_MUL", 23)
    clk_remote_component.setSymbolValue("CLK_PLLB_ENPLL", True)
    clk_remote_component.setSymbolValue("CLK_PLLB_DIVPMC0", 1)
    clk_remote_component.setSymbolValue("CLK_PLLB_ENPLLO0", True)

    #configure MCK0, Processor clock to 200 MHz and MCK0DIV to true
    css.setSelectedKey("PLLACK1")
    ratio_mck0div.setValue(True)

    #Configure MCK1 to 240 MHz and MCK1DIV to true
    cpcss.setSelectedKey("PLLBCK")
    cpbmck.setValue(True)
    ratio_mck1div.setValue(True)




    config = Variables.get("__CONFIGURATION_NAME")

    cfile = clk_component.createFileSymbol(None, None)
    cfile.setSourcePath("../peripheral/clk_pic32cx_mt/templates/plib_clk.c.ftl")
    cfile.setOutputName("plib_clk.c")
    cfile.setDestPath("/peripheral/clk/")
    cfile.setProjectPath("config/"+config+"/peripheral/clk/")
    cfile.setType("SOURCE")
    cfile.setMarkup(True)

    hfile = clk_component.createFileSymbol(None, None)
    hfile.setSourcePath("../peripheral/clk_pic32cx_mt/templates/plib_clk.h.ftl")
    hfile.setOutputName("plib_clk.h")
    hfile.setDestPath("/peripheral/clk/")
    hfile.setProjectPath("config/"+config+"/peripheral/clk/")
    hfile.setType("HEADER")
    hfile.setMarkup(True)

    #Add clock related code to common files
    sysdeffile = clk_component.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    sysdeffile.setType("STRING")
    sysdeffile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sysdeffile.setSourcePath("../peripheral/clk_pic32cx_bz/templates/system/definitions.h.ftl")
    sysdeffile.setMarkup(True)

    sysinitcfile = clk_component.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    sysinitcfile.setType("STRING")
    sysinitcfile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    sysinitcfile.setSourcePath("../peripheral/clk_pic32cx_bz/templates/system/initialization.c.ftl")
    sysinitcfile.setMarkup(True)
