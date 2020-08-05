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

from os.path import join
from xml.etree import ElementTree

global clock_id
clock_id = {}
moscrcf_names = []
gclk_id = []
gclk_src = []
procclk_src = []
procclk_pres = []
progclk_src = []
utmi_freq = []
clkSetupDep = []

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################

def slckFreq(symbol, event):

    xtalSel = int(Database.getSymbolValue("core", "SUPC_CR_MDXTALSEL"))

    if xtalSel == 1:
        freq = int(Database.getSymbolValue("core", "SLCK_EXTERNAL_VAL"))
        if freq != symbol.getValue():
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 32768:
             symbol.setValue(32768, 1)

def mainFreq(symbol, event):

    freq = 0
    clockSel = int(Database.getSymbolValue("core", "CKGR_MOR_MOSCSEL"))

    if clockSel == 1:
        enable = Database.getSymbolValue("core", "CKGR_MOR_MOSCXTEN")
        bypass = Database.getSymbolValue("core", "CKGR_MOR_MOSCXTBY")

        if enable or bypass:
            freq = int(Database.getSymbolValue("core", "MAIN_CLOCK_EXTERNAL_VAL"))
        else:
            freq = 0

        if freq != symbol.getValue():
            symbol.setValue(freq, 1)
    else:
        rcFreq = Database.getSymbolValue("core", "CKGR_MOR_MOSCRCF")

        if rcFreq == "_8_MHz":
            freq = 8000000
        elif rcFreq == "_16_MHz":
            freq = 16000000
        else:
            freq = 24000000

        if freq != symbol.getValue():
            symbol.setValue(freq, 1)

def pllaFreq(symbol, event):

    enable = Database.getSymbolValue("core", "PLLA_ENABLE")

    if enable:
        mul = int(Database.getSymbolValue("core", "CKGR_PLLAR_MULA"))
        freq = int(Database.getSymbolValue("core", "SLCK_CLOCK_FREQUENCY"))

        if Database.getSymbolValue("core", "PMC_MCKR_PLLADIV2"):
            outFreq = (freq * (mul + 1)) / 2
        else:
            outFreq = (freq * (mul + 1))

        if symbol.getValue() != outFreq:
            symbol.setValue(outFreq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def progClk(symbol, value):

    clkId = symbol.getID().split("_")[1]
    enable = Database.getSymbolValue("core", "PMC_SCER_PCK" + clkId)

    if enable:
        div = Database.getSymbolValue("core", "PMC_PCK" + clkId + "_PRES")
        src = Database.getSymbolValue("core", "PMC_PCK" + clkId + "_CSS")

        if src == "SLOW_CLK":
            freq = int(Database.getSymbolValue("core", "SLCK_CLOCK_FREQUENCY"))
        elif src == "MAIN_CLK":
            freq = int(Database.getSymbolValue("core", "MAIN_CLOCK_FREQUENCY"))
        elif src == "PLLA_CLK":
            freq = int(Database.getSymbolValue("core", "PLLA_CLOCK_FREQUENCY"))
        elif src == "MCK":
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))
        else:
            freq = 0

        freq = freq / (int(div) + 1)

        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def perifreq(symbol, event):

    enable = Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")

    if enable:
        freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))
        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def pdmicFreq(symbol, event):

    pdmicNamespace = symbol.getID().split("_CLOCK_FREQUENCY")[0].lower()
    enable = Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")

    if enable:
        src = Database.getSymbolValue(pdmicNamespace, "PDMIC_CLKSEL")
        if src == 0 or src == None:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))

        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)

    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def tcFreq(symbol, event):

    freq = 0

    peripheralId = symbol.getID().split("_CLOCK_FREQUENCY")[0]
    tcId = peripheralId.split("_")[0].split("TC")[1]
    channelId = peripheralId.split("_")[1].split("CH")[1]
    enable = Database.getSymbolValue("core", "TC" + tcId + "_CHANNEL" + channelId + "_CLOCK_ENABLE")

    if enable:
        src = int(Database.getSymbolValue("tc" + tcId, "TC" + channelId + "_CMR_TCCLKS"))
        if src == 0:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 2
        elif src == 1:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 8
        elif src == 2:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 32
        elif src == 3:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 128
        elif src == 4:
            freq = int(Database.getSymbolValue("core", "SLCK_CLOCK_FREQUENCY"))
        else:
            freq = 0

        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def usartFreq(symbol, event):

    usartId = symbol.getID().split("_CLOCK_FREQUENCY")[0].lower()
    enable = Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")

    if enable:
        clk_src = Database.getSymbolValue(usartId, "USART_CLK_SRC")
        if clk_src == 0 or clk_src == None:
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")), 1)
        elif clk_src == 1:
            symbol.setValue(int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) / 8, 1)
        else:
            symbol.setValue(int(Database.getSymbolValue("core", "SLCK_CLOCK_FREQUENCY")), 1)
    else:
        symbol.setValue(0)

def i2sFreq(symbol, event):

    enable = Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")

    if enable:
        i2sId = symbol.getID().split("_")[0].split("I2SC")[1]
        src = int(Database.getSymbolValue("core", "CLK_I2S" + i2sId + "_CLKSEL"))

        if src == 0:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))

        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)

def adcFreq(symbol, event):

    enable = Database.getSymbolValue("core", symbol.getID().split("_CLOCK_FREQUENCY")[0] + "_CLOCK_ENABLE")

    if enable:
        src = int(Database.getSymbolValue("adc", "ADC_CLK_SRC"))
        if src == 0:
            freq = int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY"))

        if symbol.getValue() != freq:
            symbol.setValue(freq, 1)
    else:
        if symbol.getValue() != 0:
            symbol.setValue(0, 1)

def masterFreq(symbol, event):

    src = Database.getSymbolValue("core", "PMC_MCKR_CSS")

    if src == "PLLA_CLK":
        freq = int(Database.getSymbolValue("core", "PLLA_CLOCK_FREQUENCY"))
    elif src == "SLOW_CLK":
        freq = int(Database.getSymbolValue("core", "SLCK_CLOCK_FREQUENCY"))
    else:
        freq = int(Database.getSymbolValue("core", "MAIN_CLOCK_FREQUENCY"))

    prescalar = int(Database.getSymbolValue("core", "PMC_MCKR_PRES").split("CLK_")[1])

    processorFreqVal = freq / prescalar
    masterclkFreq = processorFreqVal
    systickFreq = processorFreqVal / 8

    if int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) != processorFreqVal:
        Database.setSymbolValue("core", "CPU_CLOCK_FREQUENCY", processorFreqVal, 1)
    if int(Database.getSymbolValue("core", "MASTER_CLOCK_FREQUENCY")) != int(masterclkFreq):
        Database.setSymbolValue("core", "MASTER_CLOCK_FREQUENCY", masterclkFreq, 1)
    if int(Database.getSymbolValue("core", "FCLK_CLOCK_FREQUENCY")) != int(masterclkFreq):
        Database.setSymbolValue("core", "FCLK_CLOCK_FREQUENCY", masterclkFreq, 1)
    if int(Database.getSymbolValue("core", "SYSTICK_CLOCK_FREQUENCY")) != systickFreq:
        Database.setSymbolValue("core", "SYSTICK_CLOCK_FREQUENCY", systickFreq, 1)

def pcer0Cal(symbol, event):

    global clock_id
    peri = event["id"].split("_CLOCK_ENABLE")[0]

    for id in clock_id.keys():
        if id < 32:
            if peri == clock_id.get(id):
                if event["value"]:
                    value = symbol.getValue() | 1 << int(id)
                else:
                    value = symbol.getValue() & ~( 1 << int(id))

                symbol.setValue(value, 1)

def pcer1Cal(symbol, event):

    global clock_id
    peri = event["id"].split("_CLOCK_ENABLE")[0]

    for id in clock_id.keys():
        if id > 32:
            if peri == clock_id.get(id):
                if event["value"]:
                    value = symbol.getValue() | 1 << int(id - 32)
                else:
                    value = symbol.getValue() & ~( 1 << int(id - 32))

                symbol.setValue(value, 1)

###################################################################################################
########################################## Component  #############################################
###################################################################################################

clkMenu = coreComponent.createMenuSymbol("CLK_MENU", None)
clkMenu.setLabel("Clock (PMC)")

clkComment = coreComponent.createCommentSymbol("CLK_COMMENT_0", clkMenu)
clkComment.setLabel("********* Use clock manager to configure the clock system *************")

slowclkMenu = coreComponent.createMenuSymbol("SLOWclkMenu", clkMenu)
slowclkMenu.setLabel("Slow Clock Configuration")

mainclkMenu = coreComponent.createMenuSymbol("MAINclkMenu", clkMenu)
mainclkMenu.setLabel("Main Clock Configuration")

pllclkMenu = coreComponent.createMenuSymbol("PLLclkMenu", clkMenu)
pllclkMenu.setLabel("PLLA Clock Configuration")

procclkMenu = coreComponent.createMenuSymbol("PROCclkMenu", clkMenu)
procclkMenu.setLabel("Processor and Master Clock Configuration")

peripheralclkMenu = coreComponent.createMenuSymbol("PERclkMenu", clkMenu)
peripheralclkMenu.setLabel("Peripheral Clock Enable")

programmableclkMenu = coreComponent.createMenuSymbol("PROGclkMenu", clkMenu)
programmableclkMenu.setLabel("Programmable Clock Configuration")

calculatedclkMenu = coreComponent.createMenuSymbol("Cal_FREQ_MENU", clkMenu)
calculatedclkMenu.setLabel("Calculated Frequencies")

#################################### CPU Max Frequency ####################################

maxCPUFrequency = int(ATDF.getNode("/avr-tools-device-file/devices/device/property-groups/property-group@[name=\"ELECTRICAL_CHARACTERISTICS\"]/property@[name=\"CHIP_FREQ_CPU_MAX\"]").getAttribute("value"))

################################ Slow clock Configuration #################################

mdSourceClock = coreComponent.createKeyValueSetSymbol("SUPC_CR_MDXTALSEL", slowclkMenu)
mdSourceClock.setLabel("Slow Clock Source")
mdSourceClock.setOutputMode("Value")
mdSourceClock.setDisplayMode("Description")
mdSourceClock.addKey("Internal RC", "0", "Internal RC Oscilator")
mdSourceClock.addKey("External Osc", "1", "External 32.768 KHz Oscillator")

externalClockVal = coreComponent.createIntegerSymbol("SLCK_EXTERNAL_VAL", slowclkMenu)
externalClockVal.setLabel("External Clock Value")
externalClockVal.setDefaultValue(32768)

xtalBypass32K = coreComponent.createBooleanSymbol("SUPC_MR_OSCBYPASS", slowclkMenu)
xtalBypass32K.setLabel("Bypass Crystal Oscillator")

slckFreqVal = coreComponent.createIntegerSymbol("SLCK_CLOCK_FREQUENCY", slowclkMenu)
slckFreqVal.setLabel("Monitoring Domain Clock Frequency")
slckFreqVal.setDefaultValue(32768)
slckFreqVal.setMin(0)
slckFreqVal.setReadOnly(True)
slckFreqVal.setDependencies(slckFreq, ["SUPC_CR_MDXTALSEL", "SLCK_EXTERNAL_VAL", "SUPC_MR_OSCBYPASS"])

############################# Main Clock Configuration #############################################

mainclkRCOSCEN = coreComponent.createBooleanSymbol("CKGR_MOR_MOSCRCEN", mainclkMenu)
mainclkRCOSCEN.setLabel("Enable RC Oscillator")
mainclkRCOSCEN.setDefaultValue(True)

pmcValGrp_CKGR_MOR_MOSCRCF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="CKGR_MOR__MOSCRCF"]')

for id in range(0, len(pmcValGrp_CKGR_MOR_MOSCRCF.getChildren())):
    moscrcf_names.append(pmcValGrp_CKGR_MOR_MOSCRCF.getChildren()[id].getAttribute("name"))

mainclkRCOSFREQ = coreComponent.createComboSymbol("CKGR_MOR_MOSCRCF", mainclkMenu, moscrcf_names)
mainclkRCOSFREQ.setLabel("RC Oscillator Frequency")
mainclkRCOSFREQ.setDefaultValue("_8_MHz")

mainclkXtalEN = coreComponent.createBooleanSymbol("CKGR_MOR_MOSCXTEN", mainclkMenu)
mainclkXtalEN.setLabel("Enable External Oscillator")
mainclkXtalEN.setDefaultValue(False)

mainclkXtalStartup = coreComponent.createIntegerSymbol("CKGR_MOSCXTST", mainclkMenu)
mainclkXtalStartup.setLabel("External Oscillator Startup")
mainclkXtalStartup.setDefaultValue(255)
mainclkXtalStartup.setMax(255)
mainclkXtalStartup.setMin(0)

xtalBypass = coreComponent.createBooleanSymbol("CKGR_MOR_MOSCXTBY", mainclkMenu)
xtalBypass.setLabel("Bypass Crystal Oscillator")

mainclkFailure = coreComponent.createBooleanSymbol("CLOCK_FAILURE_DETECT", mainclkMenu)
mainclkFailure.setLabel("Enable Clock Failure Detection")

mainclksrc = coreComponent.createKeyValueSetSymbol("CKGR_MOR_MOSCSEL", mainclkMenu)
mainclksrc.setLabel("Main Clock Source")
mainclksrc.setOutputMode("Value")
mainclksrc.setDisplayMode("Description")
mainclksrc.addKey("Internal RC", "0", "Internal RC Oscilator")
mainclksrc.addKey("External Osc", "1", "External Oscillator")

externalMainClockVal = coreComponent.createIntegerSymbol("MAIN_CLOCK_EXTERNAL_VAL", mainclkMenu)
externalMainClockVal.setLabel("External Clock Value")
externalMainClockVal.setDefaultValue(12000000)
externalMainClockVal.setMin(0)

mainFreqVal = coreComponent.createIntegerSymbol("MAIN_CLOCK_FREQUENCY", mainclkMenu)
mainFreqVal.setLabel("Main Clock Frequency (Hz)")
mainFreqVal.setDefaultValue(8000000)
mainFreqVal.setDependencies(mainFreq, ["CKGR_MOR_MOSCSEL", "MAIN_CLOCK_EXTERNAL_VAL", "CKGR_MOR_MOSCRCF", "CKGR_MOR_MOSCXTEN", "CKGR_MOR_MOSCXTBY"])
mainFreqVal.setReadOnly(True)

################################# PLLA Configuration #####################################################

# PLL range is 24 MHz to 48 MHz(SAMG51/G53) or 96 MHz(SAMG54)
minPLLClkFrequency = 24000000
maxPLLClkFrequency = maxCPUFrequency

defaultPLLClkMultiplier = int(maxCPUFrequency / slckFreqVal.getValue()) - 1
defaultPLLClkFrequency = slckFreqVal.getValue() * (defaultPLLClkMultiplier + 1)

minPLLClkMultiplier = int(ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="PMC"]/instance@[name="PMC"]/parameters/param@[name="PLLA_MULA_MIN"]').getAttribute("value"))
maxPLLClkMultiplier = int(ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="PMC"]/instance@[name="PMC"]/parameters/param@[name="PLLA_MULA_MAX"]').getAttribute("value"))

pllclkEnable = coreComponent.createBooleanSymbol("PLLA_ENABLE", pllclkMenu)
pllclkEnable.setLabel("Enable PLLA")
pllclkEnable.setDefaultValue(True)

pllclkMultiplier = coreComponent.createIntegerSymbol("CKGR_PLLAR_MULA", pllclkMenu)
pllclkMultiplier.setLabel("PLLA Multiplier")
pllclkMultiplier.setMin(minPLLClkMultiplier)
pllclkMultiplier.setMax(maxPLLClkMultiplier)
pllclkMultiplier.setDefaultValue(defaultPLLClkMultiplier)

pllClkFreq = coreComponent.createIntegerSymbol("PLLA_CLOCK_FREQUENCY", pllclkMenu)
pllClkFreq.setLabel("PLLA Clock Frequency (Hz)")
pllClkFreq.setDefaultValue(defaultPLLClkFrequency)
pllClkFreq.setDependencies(pllaFreq, ["CKGR_PLLAR_MULA", "PLLA_ENABLE", "SLCK_CLOCK_FREQUENCY", "PMC_MCKR_PLLADIV2"])
pllClkFreq.setReadOnly(True)

pllClkMinFreq = coreComponent.createIntegerSymbol("PLLA_MIN_CLOCK_FREQUENCY", pllclkMenu)
pllClkMinFreq.setLabel("PLLA Minimum Clock Frequency (Hz)")
pllClkMinFreq.setDefaultValue(minPLLClkFrequency)
pllClkMinFreq.setVisible(False)

pllClkMaxFreq = coreComponent.createIntegerSymbol("PLLA_MAX_CLOCK_FREQUENCY", pllclkMenu)
pllClkMaxFreq.setLabel("PLLA Maximum Clock Frequency (Hz)")
pllClkMaxFreq.setDefaultValue(maxPLLClkFrequency)
pllClkMaxFreq.setVisible(False)

################################################### Peripheral and Generic Clocks #####################################

atdf_file_path = join(Variables.get("__DFP_PACK_DIR"), "atdf", Variables.get("__PROCESSOR") + ".atdf")
atdf_file = open(atdf_file_path, "r")
atdf_content = ElementTree.fromstring(atdf_file.read())

# parse atdf xml file to get instance name
# for the peripheral which has clock id
for peripheral in atdf_content.iter("module"):
    for instance in peripheral.iter("instance"):
        for param in instance.iter("param"):
            if "CLOCK_ID" in param.attrib["name"]:
                global clock_id
                clock_id[int(param.attrib["value"])] = instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1]
                symbol_id = instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1] + "_CLOCK_ENABLE"

                sym_perip_clk = coreComponent.createBooleanSymbol(symbol_id, peripheralclkMenu)
                sym_perip_clk.setLabel(instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1])
                clkSetupDep.append(symbol_id)

######################################### Processor and Main clock #######################################

pmcValGrp_PMC_MCKR_CSS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_MCKR__CSS"]')

for id in range(0, len(pmcValGrp_PMC_MCKR_CSS.getChildren())):
    procclk_src.append(pmcValGrp_PMC_MCKR_CSS.getChildren()[id].getAttribute("name"))

pmcValGrp_PMC_MCKR_PRES = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_MCKR__PRES"]')

for id in range(0, len(pmcValGrp_PMC_MCKR_PRES.getChildren())):
    procclk_pres.append(pmcValGrp_PMC_MCKR_PRES.getChildren()[id].getAttribute("name"))

procclkPLLADIV = coreComponent.createBooleanSymbol("PMC_MCKR_PLLADIV2", procclkMenu)
procclkPLLADIV.setLabel("Enable PLLA Divisor by 2")

procclkSRC = coreComponent.createComboSymbol("PMC_MCKR_CSS", procclkMenu, procclk_src)
procclkSRC.setLabel("Master Clock Source Selection")
procclkSRC.setDefaultValue("PLLA_CLK")

procclkPRES = coreComponent.createComboSymbol("PMC_MCKR_PRES", procclkMenu, procclk_pres)
procclkPRES.setLabel("Processor Clock Prescalar")
procclkPRES.setDefaultValue("CLK_1")

############################# Programmable clock ############################################################

pmcValGrp_PMC_PCK_CSS = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PMC"]/value-group@[name="PMC_PCK__CSS"]')

for id in range(0, len(pmcValGrp_PMC_PCK_CSS.getChildren())):
    progclk_src.append(pmcValGrp_PMC_PCK_CSS.getChildren()[id].getAttribute("name"))

for id in range(0, 3):
    sym_prog_clk = coreComponent.createBooleanSymbol("PMC_SCER_PCK" + str(id), programmableclkMenu)
    sym_prog_clk.setLabel("Enable Programmable Clock " + str(id))
    sym_prog_clk.setDefaultValue(False)

    prog_clk_menu = coreComponent.createMenuSymbol("PROG_CLK_MENU" + str(id), sym_prog_clk)
    prog_clk_menu.setLabel("Clock configuration")

    prog_clk_div = coreComponent.createIntegerSymbol("PMC_PCK" + str(id) + "_PRES", prog_clk_menu)
    prog_clk_div.setLabel("Programmable Clock Divider")
    prog_clk_div.setDefaultValue(0)
    prog_clk_div.setMax(255)

    prog_clk_src = coreComponent.createComboSymbol("PMC_PCK" + str(id) + "_CSS", prog_clk_menu, progclk_src)
    prog_clk_src.setLabel("Clock Source")
    prog_clk_src.setDefaultValue("MAIN_CLK")

    progClkFreq = coreComponent.createIntegerSymbol("PROG_" + str(id) + "_CLOCK_FREQUENCY", prog_clk_menu)
    progClkFreq.setLabel("Programmable Clock " + str(id) + " Frequency (Hz)")
    progClkFreq.setDefaultValue(0)
    progClkFreq.setDependencies(progClk, ["PMC_SCER_PCK" + str(id),
                                          "PMC_PCK" + str(id) + "_PRES",
                                          "PMC_PCK" + str(id) + "_CSS",
                                          "MASTER_CLOCK_FREQUENCY",
                                          "SLCK_CLOCK_FREQUENCY",
                                          "PLLA_CLOCK_FREQUENCY",
                                          "MAIN_CLOCK_FREQUENCY"
                                         ])

####################################### Calculated Frequencies ############################################

systickFreq = coreComponent.createIntegerSymbol("SYSTICK_CLOCK_FREQUENCY", calculatedclkMenu)
systickFreq.setLabel("SysTick Clock Frequency (Hz)")
systickFreq.setDefaultValue(defaultPLLClkFrequency / 8)
systickFreq.setReadOnly(True)

processorFreq = coreComponent.createIntegerSymbol("CPU_CLOCK_FREQUENCY", calculatedclkMenu)
processorFreq.setLabel("Processor Clock Frequency (Hz)")
processorFreq.setDefaultValue(defaultPLLClkFrequency)
processorFreq.setReadOnly(True)

freeRunningProcessorFreq = coreComponent.createIntegerSymbol("FCLK_CLOCK_FREQUENCY", calculatedclkMenu)
freeRunningProcessorFreq.setLabel("Free Running Processor Clock Frequency (Hz)")
freeRunningProcessorFreq.setDefaultValue(defaultPLLClkFrequency)
freeRunningProcessorFreq.setReadOnly(True)

masterFreqVal = coreComponent.createIntegerSymbol("MASTER_CLOCK_FREQUENCY", calculatedclkMenu)
masterFreqVal.setLabel("Master Clock Frequency (Hz)")
masterFreqVal.setDefaultValue(defaultPLLClkFrequency)
masterFreqVal.setReadOnly(True)
masterFreqVal.setDependencies(masterFreq, ["PMC_MCKR_CSS", "PMC_MCKR_PRES", "PMC_MCKR_MDIV", "PLLA_CLOCK_FREQUENCY", "SLCK_CLOCK_FREQUENCY", "MAIN_CLOCK_FREQUENCY"])

clocks = clock_id.keys()

for id in clocks:
    name = clock_id.get(id)
    if "TC" in clock_id.get(id) and "CHANNEL" in clock_id.get(id):
        name = clock_id.get(id).replace("CHANNEL", "CH")

    peripClock = coreComponent.createIntegerSymbol(str(name) + "_CLOCK_FREQUENCY", calculatedclkMenu)
    peripClock.setLabel(str(clock_id.get(id)) + " Clock Frequency (Hz)")
    peripClock.setDefaultValue(0)
    peripClock.setReadOnly(True)

    if "TC" in clock_id.get(id) and "CHANNEL" in clock_id.get(id):
        tcId = clock_id.get(id).split("_")[0].split("TC")[1]
        channel = clock_id.get(id).split("_")[1].split("CHANNEL")[1]
        peripClock.setDependencies(tcFreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE", "tc" + str(tcId) + ".TC" + str(channel) + "_CMR_TCCLKS"])
    elif "I2SC" in clock_id.get(id):
        i2sId = clock_id.get(id).split("I2SC")[1]
        peripClock.setDependencies(i2sFreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE", "CLK_I2S" + str(i2sId) + "_CLKSEL"])
    elif "PDMIC" in clock_id.get(id):
        pdmicId = clock_id.get(id).split("PDMIC")[1]
        peripClock.setDependencies(pdmicFreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE", "pdmic" + str(pdmicId) + ".PDMIC_CLKSEL"])
    elif "ADC" in clock_id.get(id):
        peripClock.setDependencies(adcFreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE", "adc.ADC_CLK_SRC"])
    elif "USART" in clock_id.get(id):
        peripClock.setDependencies(usartFreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE", "usart.USART_CLK_SRC"])
    else:
        peripClock.setDependencies(perifreq, ["MASTER_CLOCK_FREQUENCY", str(clock_id.get(id)) + "_CLOCK_ENABLE"])

CLK_MANAGER_SELECT = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", None)
CLK_MANAGER_SELECT.setVisible(False)
CLK_MANAGER_SELECT.setDefaultValue("clk_sam_g51_g53_g54:SAMG51G53G54ClockModel")

####################################### WAIT STATE ############################################

pmcClockEnable0 = coreComponent.createHexSymbol("PMC_PCER0", None)
pmcClockEnable0.setDefaultValue(0x0)
pmcClockEnable0.setVisible(False)
pmcClockEnable0.setDependencies(pcer0Cal, clkSetupDep)

pmcClockEnable1 = coreComponent.createHexSymbol("PMC_PCER1", None)
pmcClockEnable1.setDefaultValue(0x0)
pmcClockEnable1.setVisible(False)
pmcClockEnable1.setDependencies(pcer1Cal, clkSetupDep)

Database.setSymbolValue("core", "PIOA_CLOCK_ENABLE", True, 1)
Database.setSymbolValue("core", "PIOB_CLOCK_ENABLE", True, 1)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

clkHeaderFile = coreComponent.createFileSymbol("SAM_G51_G53_G54_CLOCK_HEADER", None)
clkHeaderFile.setSourcePath("../peripheral/clk_sam_g51_g53_g54/templates/plib_clock.h.ftl")
clkHeaderFile.setMarkup(True)
clkHeaderFile.setOutputName("plib_clock.h")
clkHeaderFile.setOverwrite(True)
clkHeaderFile.setDestPath("peripheral/clock/")
clkHeaderFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clkHeaderFile.setType("HEADER")

clkSourceFile = coreComponent.createFileSymbol("SAM_G51_G53_G54_CLOCK_SOURCE", None)
clkSourceFile.setSourcePath("../peripheral/clk_sam_g51_g53_g54/templates/plib_clock.c.ftl")
clkSourceFile.setMarkup(True)
clkSourceFile.setOutputName("plib_clock.c")
clkSourceFile.setOverwrite(True)
clkSourceFile.setDestPath("peripheral/clock/")
clkSourceFile.setProjectPath("config/" + configName + "/peripheral/clock/")
clkSourceFile.setType("SOURCE")

clkSystemDefFile = coreComponent.createFileSymbol("SAM_G51_G53_G54_CLOCK_SYS_INIT", None)
clkSystemDefFile.setType("STRING")
clkSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clkSystemDefFile.setSourcePath("../peripheral/clk_sam_g51_g53_g54/templates/system/definitions.h.ftl")
clkSystemDefFile.setMarkup(True)

clkSystemInitFile = coreComponent.createFileSymbol("SAM_G51_G53_G54_CLOCK_SYS_DEF", None)
clkSystemInitFile.setType("STRING")
clkSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clkSystemInitFile.setSourcePath("../peripheral/clk_sam_g51_g53_g54/templates/system/initialization.c.ftl")
clkSystemInitFile.setMarkup(True)
