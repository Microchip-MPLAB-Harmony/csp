# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

""" SAME70 Clock Configuration File. """

from os.path import join
from xml.etree import ElementTree

global LIST_FWS_MAX_FREQ
global DICT_PCER0
global DICT_PCER1

sym_uart_clock_freq = []
sym_usart_clock_freq = []
sym_tc_ch0_clock_freq = []
sym_tc_ch1_clock_freq = []
sym_tc_ch2_clock_freq = []
sym_tc_ch3_clock_freq = []
sym_mcan_clock_freq = []

def periphFreqCalc(symbol, event):
    symbol.setValue(int(event["value"]), 2)

def mcanClockFreqCalc(symbol, event):
    mcanInstance = symbol.getID()[4]
    activeComponents = Database.getActiveComponentIDs()
    if ("mcan" + str(mcanInstance) in activeComponents):
        if (Database.getSymbolValue("core", "PMC_SCER_PCK5") == True):
            symbol.setValue(int(Database.getSymbolValue("core", "PCK5_CLOCK_FREQUENCY")))
        else:
            symbol.setValue(0)

def tcClockFreqCalc(symbol, event):
    tcInstance = symbol.getID()[2]
    chInstance = symbol.getID()[6]
    pck6_set = False
    pck7_set = False
    id = event["id"]
    activeComponents = Database.getActiveComponentIDs()
    for module in range(0, len(num_tc_instances)):
        for ch in range (0, 4):
            if("tc"+str(module) in activeComponents):
                if(Database.getSymbolValue("tc"+str(module), "TC" + str(ch) + "_ENABLE") == True):
                    if (module == 0):
                        if(Database.getSymbolValue("tc"+str(module), "TC" + str(ch) + "_CMR_TCCLKS") == 1):
                            if (Database.getSymbolValue("tc"+str(module), "TC_PCK_CLKSRC") == "PCK6"):
                                pck6_set = True
                            else:
                                pck7_set = True
                    else:
                        if(Database.getSymbolValue("tc"+str(module), "TC" + str(ch) + "_CMR_TCCLKS") == 1):
                            pck6_set = True
    if (pck6_set == False):
        Database.setSymbolValue("core", "PMC_SCER_PCK6", False, 2)
    if (pck7_set == False):
        Database.setSymbolValue("core", "PMC_SCER_PCK7", False, 2)

    if("tc"+str(tcInstance) in activeComponents):
        if (Database.getSymbolValue("tc"+str(tcInstance), "TC" + str(chInstance) + "_ENABLE") == True):
            if (id == "TC_PCK_CLKSRC"):
                clk_src = event["value"]
                if (clk_src == "PCK6"):
                    symbol.setValue(int(Database.getSymbolValue("core", "PCK6_CLOCK_FREQUENCY")), 2)
                    Database.setSymbolValue("core", "PMC_SCER_PCK6", True, 2)
                elif (clk_src == "PCK7"):
                    symbol.setValue(int(Database.getSymbolValue("core", "PCK7_CLOCK_FREQUENCY")), 2)
                    Database.setSymbolValue("core", "PMC_SCER_PCK7", True, 2)
            else:
                clk_src = Database.getSymbolValue("tc"+str(tcInstance), "TC" + str(chInstance) + "_CMR_TCCLKS")
                #clk_src will be NONE when TC PLIB is not instantiated
                if (clk_src == 0):
                    symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)
                elif (clk_src == 1):
                    if (Database.getSymbolValue("tc"+str(tcInstance), "TC_PCK_CLKSRC") == "PCK6"):
                        symbol.setValue(int(Database.getSymbolValue("core", "PCK6_CLOCK_FREQUENCY")), 2)
                        Database.setSymbolValue("core", "PMC_SCER_PCK6", True, 2)
                    else:
                        symbol.setValue(int(Database.getSymbolValue("core", "PCK7_CLOCK_FREQUENCY")), 2)
                        Database.setSymbolValue("core", "PMC_SCER_PCK7", True, 2)
                elif (clk_src == 2):
                    symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))/8, 2)
                elif (clk_src == 3):
                    symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))/32, 2)
                elif (clk_src == 4):
                    symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))/128, 2)
                elif (clk_src == 5):
                    symbol.setValue(int(Database.getSymbolValue("core", "SLOW_CLK_FREQ")), 2)
                else:
                    symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)

def uartClockFreqCalc(symbol, event):
    uartInstance = symbol.getID()[4]
    pck4_set = False
    activeComponents = Database.getActiveComponentIDs()
    for module in range(0, len(num_uart_instances)):
        if("uart"+str(module) in activeComponents):
            if(Database.getSymbolValue("uart"+str(module), "UART_CLK_SRC") == 1):
                pck4_set = True
    for module in range(0, len(num_usart_instances)):
        if("usart"+str(module) in activeComponents):
            if(Database.getSymbolValue("usart"+str(module), "USART_CLK_SRC") == 2):
                pck4_set = True
    if (pck4_set == False):
        Database.setSymbolValue("core", "PMC_SCER_PCK4", False, 2)

    if("uart"+str(uartInstance) in activeComponents):
        clk_src = (Database.getSymbolValue("uart"+str(uartInstance), "UART_CLK_SRC"))
        #clk_src will be NONE when UART PLIB is not instantiated
        symbol.clearValue()
        if (clk_src == 0):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)
        elif (clk_src == 1):
            symbol.setValue(int(Database.getSymbolValue("core", "PCK4_CLOCK_FREQUENCY")), 2)
            Database.setSymbolValue("core", "PMC_SCER_PCK4", True, 2)
        else:
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)

def usartClockFreqCalc(symbol, event):
    usartInstance = symbol.getID()[5]
    pck4_set = False
    activeComponents = Database.getActiveComponentIDs()
    for module in range(0, len(num_uart_instances)):
        if("uart"+str(module) in activeComponents):
            if(Database.getSymbolValue("uart"+str(module), "UART_CLK_SRC") == 1):
                pck4_set = True
    for module in range(0, len(num_usart_instances)):
        if("usart"+str(module) in activeComponents):
            if(Database.getSymbolValue("usart"+str(module), "USART_CLK_SRC") == 2):
                pck4_set = True
    if (pck4_set == False):
        Database.setSymbolValue("core", "PMC_SCER_PCK4", False, 2)

    if("usart"+str(usartInstance) in activeComponents):
        clk_src = (Database.getSymbolValue("usart"+str(usartInstance), "USART_CLK_SRC"))
        #clk_src will be NONE when USART PLIB is not instantiated
        symbol.clearValue()
        if (clk_src == 0):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)
        elif (clk_src == 1):
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))/8, 2)
        elif (clk_src == 2):
            symbol.setValue(int(Database.getSymbolValue("core", "PCK4_CLOCK_FREQUENCY")), 2)
            Database.setSymbolValue("core", "PMC_SCER_PCK4", True, 2)
        else:
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 2)

def __update_fws_value(flash_wait_states, event):
    """
    Updates Flash Wait States with change in Master Clock Frequency

    flash_wait_states: flash wait states string symbol handle
    event: callback event dictionary
    """
    global LIST_FWS_MAX_FREQ

    min_freq = max_freq = 0
    for fws in range(0, len(LIST_FWS_MAX_FREQ), 1):

        mck_freq = int(event["value"])
        max_freq = int(LIST_FWS_MAX_FREQ[fws])

        if mck_freq <= max_freq and mck_freq > min_freq:
            flash_wait_states.setValue(str(fws), 1)
            return

        min_freq = max_freq

def __update_plla_divider_visibility(plla_divider, event):
    """
    Updates PLLA Divider Symbol visibility after enabling/disabling the PLLA

    plla_divider: plla divider integer symbol handle
    event: callback event dictionary
    """
    if event["value"] is True:
        plla_divider.setVisible(True)
    else:
        plla_divider.setVisible(False)

def __update_plla_multiplier_visibility(plla_multiplier, event):
    """
    Updates PLLA Multiplier Symbol visibility after enabling/disabling the PLLA.

    plla_multiplier: plla multiplier integer symbol handle
    event: callback event dictionary
    """
    if event["value"] is True:
        plla_multiplier.setVisible(True)
    else:
        plla_multiplier.setVisible(False)

def __update_upll_divider_visibility(upll_divider, event):
    """
    Updates UPLL Divider Symbol visibility after enabling/disabling the UPLL.

    upll_divider: upll divider integer symbol handle
    event: callback event dictionary
    """
    if event["value"] is True:
        upll_divider.setVisible(True)
    else:
        upll_divider.setVisible(False)

def __update_generic_clk_src_visibility(generic_clk_src, event):
    """
    Updates Generic Clock Source Symbol visibility after enabling/disabling
    the Generic Clock.

    generic_clk_src: Generic Clock Combo symbol handle.
    event: callback event dictionary.
    """
    if event["value"] is True:
        generic_clk_src.setVisible(True)
    else:
        generic_clk_src.setVisible(False)

def __update_generic_clk_div_visibility(generic_clk_divider, event):
    """
    Updates Generic Clock divider visibility after enabling/disabling
    the Generic Clock.

    generic_clk_divider: Generic Clock divider integer symbol handle.
    event: callback event dictionary.
    """
    if event["value"] is True:
        generic_clk_divider.setVisible(True)
    else:
        generic_clk_divider.setVisible(False)

def __update_slow_xtal_freq_ro_prop(slow_xtal_input_freq, event):
    """
    Updates the Slow Clock Frequency read only property after enabling/disabling
    oscillator bypass.

    slow_xtal_input_freq: Slow Clock XTAL input frequency integer symbol handle.
    event: callback event dictionary.
    """
    if event["value"] is True:
        slow_xtal_input_freq.setReadOnly(True)
    else:
        slow_xtal_input_freq.setReadOnly(False)

def __calc_slow_clk_freq(symbol, event):
    if event["value"] == False:
        symbol.setValue(32000)
    else:
        symbol.setValue(32768)

def __disable_main_xtal(main_xtal_enable, event):
    """
    Disables Main XTAL after enabling XTAL Bypass.

    main_xtal_enable: Main XTAL enable boolean symbol handle.
    event: callback event dictionary
    """
    if event["value"] is True:
        main_xtal_enable.clearValue("PMC_CKGR_MOR_MOSCXTEN")
        main_xtal_enable.setValue(False, 1)

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

def __slow_clock_menu(clk_comp, clk_menu, supc_reg_module, update_slow_xtal_freq_ro_prop, calc_slow_clk_freq):
    """
    Slow Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    supc_reg_module: SUPC Register Module
    update_slow_xtal_freq_ro_prop: Callback function to update Slow XTAL frequency
                                   read only property
    """
    # creates Slow Clock Configuration Menu
    clk_menu = clk_comp.createMenuSymbol("CLK_SLOW", clk_menu)
    clk_menu.setLabel("Slow Clock Configuration")

    # get SUPC register group
    supc_reg_group = supc_reg_module.getRegisterGroup("SUPC")

    # get SUPC_CR Register
    reg_supc_cr = supc_reg_group.getRegister("SUPC_CR")

    # get XTALSEL Bitfield of SUPC_CR Register
    bitfield_supc_cr_xtalsel = reg_supc_cr.getBitfield("XTALSEL")

    # Create Combo symbol for XTALSEL Bitfield of SUPC_CR Register
    sym_supc_cr_xtalsel = clk_comp.createBooleanSymbol("SUPC_CR_XTALSEL", clk_menu)
    sym_supc_cr_xtalsel.setLabel(bitfield_supc_cr_xtalsel.getDescription())
    sym_supc_cr_xtalsel.setDefaultValue(False)

    # get SUPC_MR Register
    reg_supc_mr = supc_reg_group.getRegister("SUPC_MR")

    # get OSCBYPASS Bitfield of SUPC_MR Register
    bitfield_supc_mr_oscbypass = reg_supc_mr.getBitfield("OSCBYPASS")

    # Create Boolean symbol for OSCBYPASS Bitfield of SUPC_MR Register
    sym_supc_mr_oscbypass = clk_comp.createBooleanSymbol("SUPC_MR_OSCBYPASS", sym_supc_cr_xtalsel)
    sym_supc_mr_oscbypass.setLabel(bitfield_supc_mr_oscbypass.getDescription())
    sym_supc_mr_oscbypass.setDefaultValue(False)

    # set slow clock input frequency
    sym_slow_xtal_freq = clk_comp.createIntegerSymbol("CLK_SLOW_XTAL", sym_supc_cr_xtalsel)
    sym_slow_xtal_freq.setLabel("External Slow Clock Input Frequency (Hz)")
    sym_slow_xtal_freq.setDefaultValue(32768)
    sym_slow_xtal_freq.setReadOnly(True)
    sym_slow_xtal_freq.setDependencies(update_slow_xtal_freq_ro_prop, ["SUPC_MR_OSCBYPASS"])

    sym_slow_clock_freq = clk_comp.createIntegerSymbol("SLOW_CLK_FREQ", sym_supc_cr_xtalsel)
    sym_slow_clock_freq.setLabel("Slow Clock Frequency")
    sym_slow_clock_freq.setDefaultValue(32000)
    sym_slow_clock_freq.setDependencies(calc_slow_clk_freq, ["SUPC_CR_XTALSEL"])

# Main RC/Crystal Oscillator
def __main_clock_menu(clk_comp, clk_menu, pmc_reg_module, disable_main_xtal):
    """
    Main Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    disable_main_xtal: Callback function to disable main xtal
    """
    # create Main Clock Configuration Menu
    clk_menu = clk_comp.createMenuSymbol("CLK_MAIN", clk_menu)
    clk_menu.setLabel("Main Clock Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get CKGR_MOR Register
    reg_ckgr_mor = pmc_reg_group.getRegister("CKGR_MOR")

    # get MOSCRCEN Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscrcen = reg_ckgr_mor.getBitfield("MOSCRCEN")

    # create symbol for MOSCRCEN Bitfield of CKGR_MOR Register
    sym_rc_enable = clk_comp.createBooleanSymbol("PMC_CKGR_MOR_MOSCRCEN", clk_menu)
    sym_rc_enable.setLabel(bitfield_ckgr_mor_moscrcen.getDescription())
    sym_rc_enable.setDefaultValue(True)

    # get MOSCRCF Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscrcf = reg_ckgr_mor.getBitfield("MOSCRCF")

    # get value group for MOSCRCF Bitfield of CKGR_MOR Register
    valgrp_ckgr_mor_moscrcf = pmc_reg_module.getValueGroup(bitfield_ckgr_mor_moscrcf.getValueGroupName())

    # create symbol for MOSCRCF Bitfield of CKGR_MOR Register
    sym_rc_freq = clk_comp.createComboSymbol("PMC_CKGR_MOR_MOSCRCF", sym_rc_enable, valgrp_ckgr_mor_moscrcf.getValueNames())
    sym_rc_freq.setLabel(bitfield_ckgr_mor_moscrcf.getDescription())
    sym_rc_freq.setDefaultValue("_12_MHz")

    # get MOSCXTBY Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscxtby = reg_ckgr_mor.getBitfield("MOSCXTBY")

    # create symbol for MOSCXTBY Bitfield of CKGR_MOR Register
    sym_osc_bypass = clk_comp.createBooleanSymbol("PMC_CKGR_MOR_MOSCXTBY", clk_menu)
    sym_osc_bypass.setLabel(bitfield_ckgr_mor_moscxtby.getDescription())

    # get MOSCXTEN Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscxten = reg_ckgr_mor.getBitfield("MOSCXTEN")

    # create Boolean Symbol for MOSCXTEN Bitfield of CKGR_MOR Register
    sym_crystal_osc_enable = clk_comp.createBooleanSymbol("PMC_CKGR_MOR_MOSCXTEN", clk_menu)
    sym_crystal_osc_enable.setLabel(bitfield_ckgr_mor_moscxten.getDescription())
    sym_crystal_osc_enable.setDefaultValue(False)
    sym_crystal_osc_enable.setDependencies(disable_main_xtal, ["PMC_CKGR_MOR_MOSCXTBY"])

    # create integer symbol for external main clock frequency
    sym_main_xtal_freq = clk_comp.createIntegerSymbol("CLK_MAIN_XTAL", sym_crystal_osc_enable)
    sym_main_xtal_freq.setLabel("External Main Clock Input Frequency (Hz)")
    sym_main_xtal_freq.setDefaultValue(12000000)
    sym_main_xtal_freq.setMin(3000000)
    sym_main_xtal_freq.setMax(20000000)

    # get MOSCXTST Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscxtst = reg_ckgr_mor.getBitfield("MOSCXTST")

    # get symbol for MOSCXTST Bitfield of CKGR_MOR Register
    sym_xtal_startup_time = clk_comp.createIntegerSymbol("PMC_CKGR_MOR_MOSCXTST", sym_crystal_osc_enable)
    sym_xtal_startup_time.setLabel(bitfield_ckgr_mor_moscxtst.getDescription())
    sym_xtal_startup_time.setDefaultValue(255)
    sym_xtal_startup_time.setMin(0)
    sym_xtal_startup_time.setMax(255)

    # get MOSCSEL Bitfield of CKGR_MOR Register
    bitfield_ckgr_mor_moscsel = reg_ckgr_mor.getBitfield("MOSCSEL")

    # create symbol for main clock source
    sym_main_clk_src = clk_comp.createBooleanSymbol("PMC_CKGR_MOR_MOSCSEL", clk_menu)
    sym_main_clk_src.setLabel(bitfield_ckgr_mor_moscsel.getDescription())
    sym_main_clk_src.setDefaultValue(False)

# PLLA
def __plla_menu(clk_comp, clk_menu, pmc_reg_module, plla_div_visibility, plla_mul_visibility):
    """
    PLLA Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    plla_div_visibility: Callback to enable/disable PLLA Divider visibility
    plla_mul_visibility: Callback to enable/disable PLLA Multiplier visibility
    """
    # create PLLA Configuration Menu
    clk_menu = clk_comp.createMenuSymbol("CLK_PLLA", clk_menu)
    clk_menu.setLabel("Clock PLL Configuration")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get CKGR_PLLAR register
    reg_ckgr_pllar = pmc_reg_group.getRegister("CKGR_PLLAR")

    # create symbol to enable/disable PLLA
    sym_plla_enable = clk_comp.createBooleanSymbol("CLK_PLLA_ENABLE", clk_menu)
    sym_plla_enable.setLabel("Enable PLLA Clock")
    sym_plla_enable.setDefaultValue(True)

    # get DIVA Bitfield of CKGR_PLLAR Register
    reg_ckgr_pllar_diva = reg_ckgr_pllar.getBitfield("DIVA")

    # creates symbol for DIVA Bitfield of CKGR_PLLAR Register
    sym_divider = clk_comp.createIntegerSymbol("PMC_CKGR_PLLAR_DIVA", sym_plla_enable)
    sym_divider.setLabel(reg_ckgr_pllar_diva.getDescription())
    sym_divider.setMin(0)
    sym_divider.setMax(255)
    sym_divider.setDefaultValue(1)
    sym_divider.setDependencies(plla_div_visibility, ["CLK_PLLA_ENABLE"])

    # get MULA Bitfield of CKGR_PLLAR register
    reg_ckgr_pllar_mula = reg_ckgr_pllar.getBitfield("MULA")

    # create symbol for MULA Bitfield of CKGR_PLLAR Register
    sym_multiplier = clk_comp.createIntegerSymbol("PMC_CKGR_PLLAR_MULA", sym_plla_enable)
    sym_multiplier.setLabel(reg_ckgr_pllar_mula.getDescription())
    sym_multiplier.setMin(0)
    sym_multiplier.setMax(63)
    sym_multiplier.setDefaultValue(25)
    sym_multiplier.setDependencies(plla_mul_visibility, ["CLK_PLLA_ENABLE"])

def __master_clock_menu(clk_comp, clk_menu, pmc_reg_module):
    """
    Master Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    """
    # create symbol for Master Clock Menu.
    clk_menu = clk_comp.createMenuSymbol("CLK_MASTER", clk_menu)
    clk_menu.setLabel("Processor and Master Clock Configuration")

    # get PMC Register Group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_MCKR register
    reg_pmc_mckr = pmc_reg_group.getRegister("PMC_MCKR")

    # get CSS Bitfield of PMC_MCKR register
    bitfield_pmc_mckr_css = reg_pmc_mckr.getBitfield("CSS")

    # get Value Group for CSS Bitfield of PMC_MCKR register
    valgrp_pmc_mckr_css = pmc_reg_module.getValueGroup(bitfield_pmc_mckr_css.getValueGroupName())

    # create symbol for CSS Bitfield of PMC_MCKR register
    sym_pmc_mckr_css = clk_comp.createComboSymbol("PMC_MCKR_CSS", clk_menu, valgrp_pmc_mckr_css.getValueNames())
    sym_pmc_mckr_css.setLabel(bitfield_pmc_mckr_css.getDescription())
    sym_pmc_mckr_css.setDefaultValue("PLLA_CLK")

    # get PRES Bitfield of PMC_MCKR register
    bitfield_pmc_mckr_pres = reg_pmc_mckr.getBitfield("PRES")

    # get Value Group for PRES Bitfield of PMC_MCKR register
    valgrp_pmc_mckr_pres = pmc_reg_module.getValueGroup(bitfield_pmc_mckr_pres.getValueGroupName())

    # create symbol for PRES Bitfield of PMC_MCKR register
    sym_pmc_mckr_pres = clk_comp.createComboSymbol("PMC_MCKR_PRES", clk_menu, valgrp_pmc_mckr_pres.getValueNames())
    sym_pmc_mckr_pres.setLabel(bitfield_pmc_mckr_pres.getDescription())
    sym_pmc_mckr_pres.setDefaultValue("CLK_1")

    # get MDIV Bitfield of PMC_MCKR register
    bitfield_pmc_mckr_mdiv = reg_pmc_mckr.getBitfield("MDIV")

    # get Value Group for MDIV Bitfield of PMC_MCKR register
    valgrp_pmc_mckr_mdiv = pmc_reg_module.getValueGroup(bitfield_pmc_mckr_mdiv.getValueGroupName())

    # create symbol for MDIV Bitfield of PMC_MCKR register
    sym_pmc_mckr_mdiv = clk_comp.createComboSymbol("PMC_MCKR_MDIV", clk_menu, valgrp_pmc_mckr_mdiv.getValueNames())
    sym_pmc_mckr_mdiv.setLabel(bitfield_pmc_mckr_mdiv.getDescription())
    sym_pmc_mckr_mdiv.setDefaultValue("PCK_DIV2")

def __usb_clock_menu(clk_comp, clk_menu, pmc_reg_module, utmi_reg_module, update_upll_divider_visibility):
    """
    USB Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    utmi_reg_module: UTMI Register Module
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

    # get UTMI register group
    utmi_reg_group = utmi_reg_module.getRegisterGroup("UTMI")

    # get UTMI_CKTRIM register
    reg_utmi_cktrim = utmi_reg_group.getRegister("UTMI_CKTRIM")

    # get FREQ bitfield of UTMI_CKTRIM register
    bitfield_utmi_cktrim_freq = reg_utmi_cktrim.getBitfield("FREQ")

    # get value group for FREQ bitfield of UTMI_CKTRIM register
    valgrp_utmi_cktrim_freq = utmi_reg_module.getValueGroup(bitfield_utmi_cktrim_freq.getValueGroupName())

    # create symbol for FREQ bitfield of UTMI_CKTRIM register
    sym_utmi_cktrim_freq = clk_comp.createComboSymbol("UTMI_CKTRIM_FREQ", sym_ckgr_uckr_upllen, valgrp_utmi_cktrim_freq.getValueNames())
    sym_utmi_cktrim_freq.setDefaultValue("XTAL12")
    sym_utmi_cktrim_freq.setVisible(False)

    # get PMC_MCKR register
    reg_pmc_mckr = pmc_reg_group.getRegister("PMC_MCKR")

    # get UPLLDIV2 Bitfield of PMC_MCKR register
    bitfield_pmc_mckr_uplldiv2 = reg_pmc_mckr.getBitfield("UPLLDIV2")

    # create symbol for UPLLDIV2 Bitfield of PMC_MCKR register
    sym_pmc_mckr_uplldiv2 = clk_comp.createBooleanSymbol("PMC_MCKR_UPLLDIV2", sym_ckgr_uckr_upllen)
    sym_pmc_mckr_uplldiv2.setLabel(bitfield_pmc_mckr_uplldiv2.getDescription())
    sym_pmc_mckr_uplldiv2.setDefaultValue(False)
    sym_pmc_mckr_uplldiv2.setVisible(False)
    sym_pmc_mckr_uplldiv2.setDependencies(update_upll_divider_visibility, ["PMC_CKGR_UCKR_UPLLEN"])

    # get PMC_SCER register
    reg_pmc_scer = pmc_reg_group.getRegister("PMC_SCER")

    # get USBCLK bitfield of PMC_SCER register
    bitfield_pmc_scer_usbclk = reg_pmc_scer.getBitfield("USBCLK")

    # get symbol for USBCLK bitfield of PMC_SCER register
    sym_pmc_scer_usbclk = clk_comp.createBooleanSymbol("PMC_SCER_USBCLK", clk_menu)
    sym_pmc_scer_usbclk.setLabel(bitfield_pmc_scer_usbclk.getDescription())

    # get PMC_USB register
    reg_pmc_usb = pmc_reg_group.getRegister("PMC_USB")

    # get USBS bitfield of PMC_USB register
    bitfield_pmc_usb_usbs = reg_pmc_usb.getBitfield("USBS")

    # create symbol for USBS bitfield of PMC_USB register
    sym_pmc_usb_usbs = clk_comp.createComboSymbol("PMC_USB_USBS", sym_pmc_scer_usbclk, ["PLLA_CLK", "UPLL_CLK"])
    sym_pmc_usb_usbs.setLabel(bitfield_pmc_usb_usbs.getDescription())
    sym_pmc_usb_usbs.setDefaultValue("UPLL_CLK")

    # get USBDIV bitfield of PMC_USB register
    bitfield_pmc_usb_usbdiv = reg_pmc_usb.getBitfield("USBDIV")

    # create symbol for USBDIV bitfield of PMC_USB register
    sym_usb_divider = clk_comp.createIntegerSymbol("PMC_USB_USBDIV", sym_pmc_scer_usbclk)
    sym_usb_divider.setLabel(bitfield_pmc_usb_usbdiv.getDescription())
    sym_usb_divider.setMin(1)
    sym_usb_divider.setMax(16)
    sym_usb_divider.setDefaultValue(10)
    sym_usb_divider.setReadOnly(True)

def __generic_clock_menu(clk_comp, clk_menu, pmc_reg_module, gclk_div_visibility, gclk_src_visibility):
    """
    Generic Clock Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    pmc_reg_module: PMC Register Module
    gclk_div_visibility: Callback to enable/disable Generic Clock Divider Visibility
    gclk_src_visibility: Callback to enable/disable Generic Clock Source Visibility
    """
    # create symbol for generic clock
    clk_menu = clk_comp.createMenuSymbol("CLK_GENERIC", clk_menu)
    clk_menu.setLabel("Peripheral/Generic Clock Generator Configuration for I2S0/1")

    # get PMC register group
    pmc_reg_group = pmc_reg_module.getRegisterGroup("PMC")

    # get PMC_PCR register
    reg_pmc_pcr = pmc_reg_group.getRegister("PMC_PCR")

    for i in range(0, 2, 1):

        # create menu for Peripheral/Generic Clock for I2S0/1
        sym_gclkx_menu = clk_comp.createMenuSymbol("CLK_I2S" + str(i), clk_menu)
        sym_gclkx_menu.setLabel("Peripheral/Generic Clock for I2S" + str(i))

        # create menu for Peripheral Clock for I2S0/1
        sym_i2s_pclk_menu = clk_comp.createMenuSymbol("CLK_I2S" + str(i) + "PERIPHERAL", sym_gclkx_menu)
        sym_i2s_pclk_menu.setLabel("I2S" + str(i) +" Peripheral Clock")

        # get EN bitfield of PMC_PCR Register
        bitfield_pmc_pcr = reg_pmc_pcr.getBitfield("EN")

        # create symbol for EN bitfield of PMC_PCR Register
        sym_pmc_pcr_en = clk_comp.createBooleanSymbol("PMC_PCR_EN" + str(i), sym_i2s_pclk_menu)
        sym_pmc_pcr_en.setLabel(bitfield_pmc_pcr.getDescription())
        sym_pmc_pcr_en.setDefaultValue(False)

        # create menu for Generic clock for I2S0/1
        sym_gen_clk_menu = clk_comp.createMenuSymbol("CLK_I2S" + str(i) + "GENERIC", sym_gclkx_menu)
        sym_gen_clk_menu.setLabel("I2S" + str(i) + "Generic Clock")

        # get GCLKEN bitfield of PMC_PCR register
        bitfield_pmc_pcr_gclken = reg_pmc_pcr.getBitfield("GCLKEN")

        # create symbol for GCLKEN bitfield of PMC_PCR register
        sym_pmc_pcr_gclken = clk_comp.createBooleanSymbol("PMC_PCR_GCLK" + str(i) + "EN", sym_gen_clk_menu)
        sym_pmc_pcr_gclken.setLabel(bitfield_pmc_pcr_gclken.getDescription())

        # get GCLKDIV bitfield of PMC_PCR register
        bitfield_pmc_pcr_gclkdiv = reg_pmc_pcr.getBitfield("GCLKDIV")

        # create symbol for GCLKDIV bitfield of PMC_PCR register
        sym_pmc_pcr_gclkdiv = clk_comp.createIntegerSymbol("PMC_PCR_GCLK" + str(i) + "DIV", sym_gen_clk_menu)
        sym_pmc_pcr_gclkdiv.setLabel(bitfield_pmc_pcr_gclkdiv.getDescription())
        sym_pmc_pcr_gclkdiv.setMin(1)
        sym_pmc_pcr_gclkdiv.setMax(256)
        sym_pmc_pcr_gclkdiv.setDefaultValue(1)
        sym_pmc_pcr_gclkdiv.setVisible(False)
        sym_pmc_pcr_gclkdiv.setDependencies(gclk_div_visibility, ["PMC_PCR_GCLK" + str(i) + "EN"])

        # get GCLKCSS bitfield of PMC_PCR register
        bitfield_pmc_pcr_gclkcss = reg_pmc_pcr.getBitfield("GCLKCSS")

        # create symbol for GCLKCSS bitfield of PMC_PCR register
        sym_pmc_pcr_gclkcss = clk_comp.createKeyValueSetSymbol("PMC_PCR_GCLK" + str(i) + "CSS", sym_gen_clk_menu)
        sym_pmc_pcr_gclkcss.setLabel(bitfield_pmc_pcr_gclkcss.getDescription())
        sym_pmc_pcr_gclkcss.setVisible(False)
        sym_pmc_pcr_gclkcss.addKey("SLOW_CLK", "SLOW_CLK", "Slow Clock")
        sym_pmc_pcr_gclkcss.addKey("MAIN_CLK", "MAIN_CLK", "Main Clock")
        sym_pmc_pcr_gclkcss.addKey("PLLA_CLK", "PLLA_CLK", "PLLA Clock")
        sym_pmc_pcr_gclkcss.addKey("UPLL_CLK", "UPLL_CLK", "UPLL Clock")
        sym_pmc_pcr_gclkcss.addKey("MCK", "MCK_CLK", "Master Clock")
        sym_pmc_pcr_gclkcss.setOutputMode("Value")
        sym_pmc_pcr_gclkcss.setDisplayMode("Key")
        sym_pmc_pcr_gclkcss.setSelectedKey("SLOW_CLK",1)
        sym_pmc_pcr_gclkcss.setDependencies(gclk_src_visibility, ["PMC_PCR_GCLK" + str(i) + "EN"])

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

                    symbol_id = instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1] +"_CLOCK_ENABLE"
                    sym_perip_clk = clk_comp.createBooleanSymbol(symbol_id, clk_menu)
                    sym_perip_clk.setLabel(instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1])
                    sym_perip_clk.setDefaultValue(False)
                    sym_perip_clk.setReadOnly(True)

                    clock_id = int(param.attrib["value"])

                    if clock_id < 32:
                        list_pcer0_depend.append(symbol_id)
                        DICT_PCER0.update({symbol_id: clock_id})
                    else:
                        list_pcer1_depend.append(symbol_id)
                        DICT_PCER1.update({symbol_id: clock_id})

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

    # menu for 8 programmable clock
    for i in range(0, 8, 1):

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

        # get PRES bitfield of PMC_PCK# register
        bitfield_pmc_pck_pres = reg_pmc_pck.getBitfield("PRES")

        # create symbol for PRES bitfield of PMC_PCK# register
        sym_pmc_pck_pres = clk_comp.createIntegerSymbol("PMC_PCK" + str(i) +"_PRES", sym_pmc_scer_pck)
        sym_pmc_pck_pres.setLabel(bitfield_pmc_pck_pres.getDescription())
        sym_pmc_pck_pres.setMin(1)
        sym_pmc_pck_pres.setMax(256)
        sym_pmc_pck_pres.setDefaultValue(1)

def __calculated_clock_frequencies(clk_comp, clk_menu, update_fws_value, join_path, element_tree):
    """
    Calculated Clock frequencies Menu Implementation.

    clk_comp: Clock Component handle
    clk_menu: Clock Menu Symbol handle
    update_fws_value: Callback calculating the Flash Wait States.
    join_path: function used to create os independent paths
    element_tree: XML parser library
    """
    global LIST_FWS_MAX_FREQ

    #Calculated Clock Frequencies
    sym_calc_freq_menu = clk_comp.createMenuSymbol("CALC_CLOCK_FREQ_MENU", clk_menu)
    sym_calc_freq_menu.setLabel("Calculated Clock Frequencies")

    sym_sys_tick_freq = clk_comp.createStringSymbol("SYSTICK_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_sys_tick_freq.setLabel("System Tick Frequency (HZ)")
    sym_sys_tick_freq.setDefaultValue("150000000")
    sym_sys_tick_freq.setReadOnly(True)

    sym_proc_clk_freq = clk_comp.createStringSymbol("CPU_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_proc_clk_freq.setLabel("Processor Clock Frequency (HZ)")
    sym_proc_clk_freq.setDefaultValue("300000000")
    sym_proc_clk_freq.setReadOnly(True)

    sym_master_clk_freq = clk_comp.createStringSymbol("MASTER_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_master_clk_freq.setLabel("Master Clock Frequency (HZ)")
    sym_master_clk_freq.setDefaultValue("150000000")
    sym_master_clk_freq.setReadOnly(True)

    sym_i2s0_freq = clk_comp.createStringSymbol("I2S0_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_i2s0_freq.setLabel("I2S0 Frequency (HZ)")
    sym_i2s0_freq.setDefaultValue("75000000")
    sym_i2s0_freq.setReadOnly(True)

    sym_i2s1_freq = clk_comp.createStringSymbol("I2S1_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_i2s1_freq.setLabel("I2S1 Frequency (HZ)")
    sym_i2s1_freq.setDefaultValue("100000000")
    sym_i2s1_freq.setReadOnly(True)

    sym_pck0_freq = clk_comp.createStringSymbol("PCK0_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck0_freq.setLabel("Programmable clock #0 Frequency (HZ)")
    sym_pck0_freq.setDefaultValue("32000")
    sym_pck0_freq.setReadOnly(True)

    sym_pck1_freq = clk_comp.createStringSymbol("PCK1_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck1_freq.setLabel("Programmable clock #1 Frequency (HZ)")
    sym_pck1_freq.setDefaultValue("32000")
    sym_pck1_freq.setReadOnly(True)

    sym_pck2_freq = clk_comp.createStringSymbol("PCK2_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck2_freq.setLabel("Programmable clock #2 Frequency (HZ)")
    sym_pck2_freq.setDefaultValue("32000")
    sym_pck2_freq.setReadOnly(True)

    sym_pck3_freq = clk_comp.createStringSymbol("PCK3_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck3_freq.setLabel("Programmable clock #3 Frequency (HZ)")
    sym_pck3_freq.setDefaultValue("32000")
    sym_pck3_freq.setReadOnly(True)

    sym_pck4_freq = clk_comp.createStringSymbol("PCK4_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck4_freq.setLabel("Programmable clock #4 Frequency (HZ)")
    sym_pck4_freq.setDefaultValue("32000")
    sym_pck4_freq.setReadOnly(True)

    sym_pck5_freq = clk_comp.createStringSymbol("PCK5_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck5_freq.setLabel("Programmable clock #5 Frequency (HZ)")
    sym_pck5_freq.setDefaultValue("32000")
    sym_pck5_freq.setReadOnly(True)

    sym_pck6_freq = clk_comp.createStringSymbol("PCK6_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck6_freq.setLabel("Programmable clock #6 Frequency (HZ)")
    sym_pck6_freq.setDefaultValue("32000")
    sym_pck6_freq.setReadOnly(True)

    sym_pck7_freq = clk_comp.createStringSymbol("PCK7_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_pck7_freq.setLabel("Programmable clock #7 Frequency (HZ)")
    sym_pck7_freq.setDefaultValue("32000")
    sym_pck7_freq.setReadOnly(True)

    sym_usb_fs_freq = clk_comp.createStringSymbol("USBFS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_usb_fs_freq.setLabel("USB Clock Frequency (HZ)")
    sym_usb_fs_freq.setDefaultValue("48000000")
    sym_usb_fs_freq.setReadOnly(True)

    sym_usb_hs_freq = clk_comp.createStringSymbol("USBHS_CLOCK_FREQUENCY", sym_calc_freq_menu)
    sym_usb_hs_freq.setLabel("USB High Speed Clock Frequency (HZ)")
    sym_usb_hs_freq.setDefaultValue("480000000")
    sym_usb_hs_freq.setReadOnly(True)

    sym_flash_wait_states = clk_comp.createStringSymbol("EEFC_FMR_FWS", sym_calc_freq_menu)
    sym_flash_wait_states.setDependencies(update_fws_value, ["MASTER_CLOCK_FREQUENCY"])
    sym_flash_wait_states.setVisible(False)

    atdf_file_path = join_path(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")

    LIST_FWS_MAX_FREQ = []

    atdf_file = open(atdf_file_path, "r")
    atdf_content = element_tree.fromstring(atdf_file.read())

    # parse atdf xml file to get Electrical Characteristics
    # for Flash wait states
    for property_group in atdf_content.iter("property-group"):
        if "ELECTRICAL_CHARACTERISTICS" in property_group.attrib["name"]:
            for property_tag in property_group.iter("property"):
                if "CHIP_FREQ_FWS_" in property_tag.attrib["name"] and property_tag.attrib["name"] != "CHIP_FREQ_FWS_NUMBER":
                    LIST_FWS_MAX_FREQ.append(property_tag.attrib["value"])

    min_freq = max_freq = 0
    for fws in range(0, len(LIST_FWS_MAX_FREQ), 1):

        mck_freq = int(sym_master_clk_freq.getValue())
        max_freq = int(LIST_FWS_MAX_FREQ[fws])

        if mck_freq <= max_freq and mck_freq > min_freq:
            sym_flash_wait_states.setValue(str(fws), 1)
            return

        min_freq = max_freq

if __name__ == "__main__":
    # Clock Manager Configuration Menu
    SYM_CLK_MENU = coreComponent.createMenuSymbol("CLK_SAM_E70", None)
    SYM_CLK_MENU.setLabel("Clock (PMC)")
    SYM_CLK_MENU.setDescription("Configuration for Clock System Service")

    CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", SYM_CLK_MENU)
    CLK_MANAGER_SELECT.setVisible(False)
    CLK_MANAGER_SELECT.setDefaultValue("clk_sam_e70:SAME70ClockModel")

    CLK_MENU_COMMENT = coreComponent.createCommentSymbol("clkSettingsComment", SYM_CLK_MENU)
    CLK_MENU_COMMENT.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

    PMC_REGISTERS = Register.getRegisterModule("PMC")
    SUPC_REGISTERS = Register.getRegisterModule("SUPC")
    UTMI_REGISTERS = Register.getRegisterModule("UTMI")

    # Creates slow clock menu
    __slow_clock_menu(coreComponent, SYM_CLK_MENU, SUPC_REGISTERS, __update_slow_xtal_freq_ro_prop, __calc_slow_clk_freq)

    # creates main clock menu
    __main_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS, __disable_main_xtal)

    # creates plla menu
    __plla_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS, __update_plla_divider_visibility, __update_plla_multiplier_visibility)

    # creates master clock
    __master_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates usb clock
    __usb_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS, UTMI_REGISTERS, __update_upll_divider_visibility)

    # creates generic clock menu
    __generic_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS, __update_generic_clk_div_visibility, __update_generic_clk_src_visibility)

    # creates peripheral clock menu
    __peripheral_clock_menu(coreComponent, SYM_CLK_MENU, join, ElementTree, __update_pcer0_value, __update_pcer1_value)

    # creates programmable clock menu
    __programmable_clock_menu(coreComponent, SYM_CLK_MENU, PMC_REGISTERS)

    # creates calculated frequencies menu
    __calculated_clock_frequencies(coreComponent, SYM_CLK_MENU, __update_fws_value, join, ElementTree)

    # calculated peripheral frequencies
    peripherals = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
    modules = peripherals.getChildren()
    for module in range(0, len(modules)):
        moduleName = modules[module].getAttribute("name")
        #I2S, USB, TC, UART, USART and MCAN clock frequencies calculated separately
        if (moduleName == "I2SC" or moduleName == "USBHS" or moduleName == "TC" or moduleName == "UART" or moduleName == "USART" or moduleName == "MCAN"):
            continue
        numInstances = modules[module].getChildren()
        for moduleInstance in range(0, len(numInstances)):
            clock_present = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\""+str(moduleName)+"\"]/instance@[name=\""+numInstances[moduleInstance].getAttribute("name")+"\"]/parameters/param@[name=\"CLOCK_ID\"]")
            #skip modules which do not have clock_id
            if (clock_present == None):
                continue
            symbolID = numInstances[moduleInstance].getAttribute("name") + "_CLOCK_FREQUENCY"
            sym_peripheral_clock_freq = coreComponent.createIntegerSymbol(symbolID, None)
            sym_peripheral_clock_freq.setVisible(False)
            sym_peripheral_clock_freq.setReadOnly(True)
            sym_peripheral_clock_freq.setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
            sym_peripheral_clock_freq.setDependencies(periphFreqCalc, ["core.MASTER_CLOCK_FREQUENCY"])

    #UART
    global num_uart_instances
    num_uart_instances = []
    uart = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"UART\"]")
    num_uart_instances = uart.getChildren()
    for uartInstance in range(0, len(num_uart_instances)):
        sym_uart_clock_freq.append(uartInstance)
        sym_uart_clock_freq[uartInstance] = coreComponent.createIntegerSymbol("UART"+str(uartInstance)+"_CLOCK_FREQUENCY", None)
        sym_uart_clock_freq[uartInstance].setVisible(False)
        sym_uart_clock_freq[uartInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_uart_clock_freq[uartInstance].setDependencies(uartClockFreqCalc, ["uart"+str(uartInstance)+".UART_CLK_SRC", \
            "core.MASTER_CLOCK_FREQUENCY", "core.PCK4_CLOCK_FREQUENCY", "core.UART"+str(uartInstance)+"_CLOCK_ENABLE"])

    #USART
    global num_usart_instances
    num_usart_instances = []
    usart = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"USART\"]")
    num_usart_instances = usart.getChildren()
    for usartInstance in range(0, len(num_usart_instances)):
        sym_usart_clock_freq.append(usartInstance)
        sym_usart_clock_freq[usartInstance] = coreComponent.createIntegerSymbol("USART"+str(usartInstance)+"_CLOCK_FREQUENCY", None)
        sym_usart_clock_freq[usartInstance].setVisible(False)
        sym_usart_clock_freq[usartInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_usart_clock_freq[usartInstance].setDependencies(usartClockFreqCalc, ["usart"+str(usartInstance)+".USART_CLK_SRC", \
            "core.MASTER_CLOCK_FREQUENCY", "core.PCK4_CLOCK_FREQUENCY", "core.USART"+str(usartInstance)+"_CLOCK_ENABLE"])

    #TC
    global num_tc_instances
    num_tc_instances = []
    tc = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TC\"]")
    num_tc_instances = tc.getChildren()
    for tcInstance in range(0, len(num_tc_instances)):
        sym_tc_ch0_clock_freq.append(tcInstance)
        sym_tc_ch0_clock_freq[tcInstance] = coreComponent.createIntegerSymbol("TC"+str(tcInstance)+"_CH0_CLOCK_FREQUENCY", None)
        sym_tc_ch0_clock_freq[tcInstance].setVisible(False)
        sym_tc_ch0_clock_freq[tcInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_tc_ch0_clock_freq[tcInstance].setDependencies(tcClockFreqCalc, ["tc"+str(tcInstance)+".TC0_CMR_TCCLKS", "tc"+str(tcInstance)+".TC_PCK_CLKSRC", \
        "core.MASTER_CLOCK_FREQUENCY", "core.PCK6_CLOCK_FREQUENCY", "core.PCK7_CLOCK_FREQUENCY", "core.SLOW_CLK_FREQ", "tc"+str(tcInstance)+".TC0_ENABLE", \
        "core.TC"+str(tcInstance)+"_CHANNEL0_CLOCK_ENABLE"])

        sym_tc_ch1_clock_freq.append(tcInstance)
        sym_tc_ch1_clock_freq[tcInstance] = coreComponent.createIntegerSymbol("TC"+str(tcInstance)+"_CH1_CLOCK_FREQUENCY", None)
        sym_tc_ch1_clock_freq[tcInstance].setVisible(False)
        sym_tc_ch1_clock_freq[tcInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_tc_ch1_clock_freq[tcInstance].setDependencies(tcClockFreqCalc, ["tc"+str(tcInstance)+".TC1_CMR_TCCLKS", "tc"+str(tcInstance)+".TC_PCK_CLKSRC", \
        "core.MASTER_CLOCK_FREQUENCY", "core.PCK6_CLOCK_FREQUENCY", "core.PCK7_CLOCK_FREQUENCY", "core.SLOW_CLK_FREQ", "tc"+str(tcInstance)+".TC1_ENABLE", \
        "core.TC"+str(tcInstance)+"_CHANNEL1_CLOCK_ENABLE"])

        sym_tc_ch2_clock_freq.append(tcInstance)
        sym_tc_ch2_clock_freq[tcInstance] = coreComponent.createIntegerSymbol("TC"+str(tcInstance)+"_CH2_CLOCK_FREQUENCY", None)
        sym_tc_ch2_clock_freq[tcInstance].setVisible(False)
        sym_tc_ch2_clock_freq[tcInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_tc_ch2_clock_freq[tcInstance].setDependencies(tcClockFreqCalc, ["tc"+str(tcInstance)+".TC2_CMR_TCCLKS", "tc"+str(tcInstance)+".TC_PCK_CLKSRC", \
        "core.MASTER_CLOCK_FREQUENCY", "core.PCK6_CLOCK_FREQUENCY", "core.PCK7_CLOCK_FREQUENCY", "core.SLOW_CLK_FREQ", "tc"+str(tcInstance)+".TC2_ENABLE", \
        "core.TC"+str(tcInstance)+"_CHANNEL2_CLOCK_ENABLE"])

        #CH3 is used for quadrature speed mode
        sym_tc_ch3_clock_freq.append(tcInstance)
        sym_tc_ch3_clock_freq[tcInstance] = coreComponent.createIntegerSymbol("TC"+str(tcInstance)+"_CH3_CLOCK_FREQUENCY", None)
        sym_tc_ch3_clock_freq[tcInstance].setVisible(False)
        sym_tc_ch3_clock_freq[tcInstance].setDefaultValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")))
        sym_tc_ch3_clock_freq[tcInstance].setDependencies(tcClockFreqCalc, ["tc"+str(tcInstance)+".TC3_CMR_TCCLKS", "tc"+str(tcInstance)+".TC_PCK_CLKSRC", \
        "core.MASTER_CLOCK_FREQUENCY", "core.PCK6_CLOCK_FREQUENCY", "core.PCK7_CLOCK_FREQUENCY", "core.SLOW_CLK_FREQ", "tc"+str(tcInstance)+".TC3_ENABLE", \
        "core.TC"+str(tcInstance)+"_CHANNEL3_CLOCK_ENABLE"])

    #MCAN
    global num_mcan_instances
    num_mcan_instances = []
    mcan = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"MCAN\"]")
    num_mcan_instances = mcan.getChildren()
    for mcanInstance in range(0, len(num_mcan_instances)):
        sym_mcan_clock_freq.append(mcanInstance)
        sym_mcan_clock_freq[mcanInstance] = coreComponent.createIntegerSymbol("MCAN" + str(mcanInstance) + "_CLOCK_FREQUENCY", None)
        sym_mcan_clock_freq[mcanInstance].setVisible(False)
        sym_mcan_clock_freq[mcanInstance].setDefaultValue(int(Database.getSymbolValue("core", "PCK5_CLOCK_FREQUENCY")) if (Database.getSymbolValue("core", "PMC_SCER_PCK5") == True) else 0)
        sym_mcan_clock_freq[mcanInstance].setDependencies(mcanClockFreqCalc, ["core.PCK5_CLOCK_FREQUENCY", "core.PMC_SCER_PCK5", "core.MCAN" + str(mcanInstance) + "_CLOCK_ENABLE"])

    #File handling
    CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

    CLK_INTERFACE_HDR = coreComponent.createFileSymbol("CLK_H", None)
    CLK_INTERFACE_HDR.setSourcePath("../peripheral/clk_sam_e70/templates/plib_clk.h.ftl")
    CLK_INTERFACE_HDR.setOutputName("plib_clk.h")
    CLK_INTERFACE_HDR.setDestPath("/peripheral/clk/")
    CLK_INTERFACE_HDR.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_INTERFACE_HDR.setType("HEADER")
    CLK_INTERFACE_HDR.setMarkup(True)

    CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
    CLK_SRC_FILE.setSourcePath("../peripheral/clk_sam_e70/templates/plib_clk.c.ftl")
    CLK_SRC_FILE.setOutputName("plib_clk.c")
    CLK_SRC_FILE.setDestPath("/peripheral/clk/")
    CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
    CLK_SRC_FILE.setType("SOURCE")
    CLK_SRC_FILE.setMarkup(True)

    #Add clock related code to common files
    CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
    CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
    CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_e70/templates/system/definitions.h.ftl")
    CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

    CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
    CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
    CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
    CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_sam_e70/templates/system/initialization.c.ftl")
    CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
