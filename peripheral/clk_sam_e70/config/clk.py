print("Loading Clock Manager for " + Variables.get("__PROCESSOR"))

clkMenu = coreComponent.createMenuSymbol(None, None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuraiton for Clock System Service")

clkEnable = coreComponent.createBooleanSymbol("clkEnable", clkMenu)
clkEnable.setLabel("Use Clock System Service?")
clkEnable.setDefaultValue(True)
clkEnable.setReadOnly(True)

clkServiceMode = coreComponent.createComboSymbol("SYS_CLK_MODE", clkEnable, ["STATIC", "DYNAMIC"])
clkServiceMode.setLabel("Select Service Mode")
clkServiceMode.setDefaultValue("STATIC")
clkServiceMode.setReadOnly(True)

clkSettings = coreComponent.createMenuSymbol("clkSetting", clkEnable)
clkSettings.setLabel("Clock Configuration Settings")

clkSettingsComment = coreComponent.createCommentSymbol("clkSettingsComment", clkSettings)
clkSettingsComment.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

#Main clock Configuration
def setDefaultMainRCFreq(mainRCFreqValue, mainRCFreq):
        if(mainRCFreq.getValue() == "4_MHz"):
            mainRCFreqValue.setValue("SYS_CLK_CKGR_MOR_MOSCRCF_VALUE", "SYS_CLK_RC_FREQUENCY_4_MHZ", 1)
        elif(mainRCFreq.getValue() == "8_MHz"):
            mainRCFreqValue.setValue("SYS_CLK_CKGR_MOR_MOSCRCF_VALUE", "SYS_CLK_RC_FREQUENCY_8_MHZ", 1)
        else :
            mainRCFreqValue.setValue("SYS_CLK_CKGR_MOR_MOSCRCF_VALUE", "SYS_CLK_RC_FREQUENCY_12_MHZ", 1)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "+str(mainRCFreqValue.getValue()))
        
def setClkSource(mainClkSourceValue, mainClkSource):
        if(mainClkSource.getValue() == "4_MHz"):
            mainClkSourceValue.setValue("SYS_CLK_CKGR_MOR_MOSCSEL_VALUE", "SYS_CLK_MAIN_SOURCE_RC", 1)
        else :
            mainClkSourceValue.setValue("SYS_CLK_CKGR_MOR_MOSCSEL_VALUE", "SYS_CLK_MAIN_SOURCE_XTAL", 1)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "+str(mainClkSourceValue.getValue()))
        
mainClkConfig = coreComponent.createMenuSymbol("mainClk", clkSettings)
mainClkConfig.setLabel("Main Clock Configuration")

mainClkCrystalOscEnable = coreComponent.createBooleanSymbol("SYS_CLK_CKGR_MOR_MOSCXTEN", mainClkConfig)
mainClkCrystalOscEnable.setLabel("Main Crystal Oscillator Enable")

extMainClkInputFreq = coreComponent.createStringSymbol("SYS_CLK_CONFIG_MAINCLK_XTAL", mainClkConfig)
extMainClkInputFreq.setLabel("External Main Clock Input Frequency (Hz)")
extMainClkInputFreq.setDefaultValue("120000000")

mainCrystalOscStartupTime = coreComponent.createIntegerSymbol("SYS_CLK_CKGR_MOSCXTST", mainClkConfig)
mainCrystalOscStartupTime.setLabel("Main Crystal Oscillator Startup Time")
mainCrystalOscStartupTime.setDefaultValue(255)
mainCrystalOscStartupTime.setMin(0)
mainCrystalOscStartupTime.setMax(255)

mainOscBypass = coreComponent.createBooleanSymbol("SYS_CLK_CKGR_MOR_MOSCXTBY", mainClkConfig)
mainOscBypass.setLabel("Main Crystal Oscillator Bypass")

mainRCEnable = coreComponent.createBooleanSymbol("SYS_CLK_CKGR_MOR_MOSCRCEN", mainClkConfig)
mainRCEnable.setLabel("Main RC Oscillator Enable")
mainRCEnable.setDefaultValue(True)

mainRCFreq = coreComponent.createComboSymbol("SYS_CLK_CKGR_MOR_MOSCRCF", mainClkConfig, ["4_MHz", "8_MHz", "12_MHz"])
mainRCFreq.setLabel("Main RC Oscillator Frequency (Hz)")
mainRCFreq.setDefaultValue("12_MHz")

mainRCFreqValue = coreComponent.createStringSymbol("SYS_CLK_CKGR_MOR_MOSCRCF_VALUE", None)
mainRCFreqValue.setVisible(False)
mainRCFreqValue.setDependencies(setDefaultMainRCFreq, ["SYS_CLK_CKGR_MOR_MOSCRCF"])

mainClkSource = coreComponent.createComboSymbol("SYS_CLK_CKGR_MOR_MOSCSEL", mainClkConfig, ["MAIN_RC_OSC", "MAIN_CRYSTAL_OSC"])
mainClkSource.setLabel("Main Clock Source")
mainClkSource.setDefaultValue("MAIN_RC_OSC")

mainClkSourceValue = coreComponent.createStringSymbol("SYS_CLK_CKGR_MOR_MOSCSEL_VALUE", None)
mainClkSourceValue.setVisible(False)
mainClkSourceValue.setDependencies(setClkSource, ["SYS_CLK_CKGR_MOR_MOSCSEL"])

#Slow Clock Configuration
def setDefaultClkSrcVal(slowClkSourceValue, slowClkSource):
        if(slowClkSource.getValue() == "SLOW_RC_OSC"):
            slowClkSourceValue.setValue("SYS_CLK_SUPC_CR_XTALSEL_VALUE", False, 1)
        else :
            slowClkSourceValue.setValue("SYS_CLK_SUPC_CR_XTALSEL_VALUE", True, 1)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "+str(slowClkSourceValue.getValue()))
            
slowClkConfig = coreComponent.createMenuSymbol("slowClkConfig", clkSettings)
slowClkConfig.setLabel("Slow Clock Configuration")

extSlowClkInputFreq = coreComponent.createStringSymbol("SYS_CLK_CONFIG_SLOWCLK_XTAL", slowClkConfig)
extSlowClkInputFreq.setLabel("External Slow Clock Input Frequency (Hz)")
extSlowClkInputFreq.setDefaultValue("32768")

cystalOscBypass = coreComponent.createBooleanSymbol("SYS_CLK_SUPC_MR_OSCBYPASS", slowClkConfig)
cystalOscBypass.setLabel("Crystal Oscillator Bypass")

slowClkSource = coreComponent.createComboSymbol("SYS_CLK_SUPC_CR_XTALSEL", slowClkConfig, ["SLOW_RC_OSC", "32.768k_CRYSTAL_OSC"])
slowClkSource.setLabel("Slow Clock Source")
slowClkSource.setDefaultValue("SLOW_RC_OSC")

slowClkSourceValue = coreComponent.createBooleanSymbol("SYS_CLK_SUPC_CR_XTALSEL_VALUE", None)
slowClkSourceValue.setVisible(False)
slowClkSourceValue.setDependencies(setDefaultClkSrcVal, ["SYS_CLK_SUPC_CR_XTALSEL"])

#PLLA Configuration
def setDividerVisibleProperty(pllaDivider, pllaClkEnable):
        if (pllaClkEnable.getValue() == True):
            print("PLLA Enabled")
            pllaDivider.setVisible(True)
        else :
            print("PLLA Disabled")
            pllaDivider.setVisible(False)

def setMultiplierVisibleProperty(pllaMultiplier, pllaClkEnable):
        if (pllaClkEnable.getValue() == True):
            pllaMultiplier.setVisible(True)
        else :
            pllaMultiplier.setVisible(False)
            
pllaClkConfig = coreComponent.createMenuSymbol("pllaClkConfig", clkSettings)
pllaClkConfig.setLabel("Clock PLL Configuration")

pllaClkEnable = coreComponent.createBooleanSymbol("SYS_CLK_CKGR_PLLAR_DIVA0_MULA0", pllaClkConfig)
pllaClkEnable.setLabel("Enable PLLA Clock")
pllaClkEnable.setDefaultValue(True)

pllaDivider = coreComponent.createIntegerSymbol("SYS_CLK_CKGR_PLLAR_DIVA", pllaClkEnable)
pllaDivider.setLabel("PLL Divider")
pllaDivider.setMin(0)
pllaDivider.setMax(255)
pllaDivider.setDefaultValue(1)
pllaDivider.setDependencies(setDividerVisibleProperty, ["SYS_CLK_CKGR_PLLAR_DIVA0_MULA0"])

pllaMultiplier = coreComponent.createIntegerSymbol("SYS_CLK_CKGR_PLLAR_MULA", pllaClkEnable)
pllaMultiplier.setLabel("PLL Multiplier")
pllaMultiplier.setMin(0)
pllaMultiplier.setMax(63)
pllaMultiplier.setDefaultValue(25)
pllaMultiplier.setDependencies(setMultiplierVisibleProperty, ["SYS_CLK_CKGR_PLLAR_DIVA0_MULA0"])

#Processor and Master clock configuration
def setPMCClkSrc(pmcClkValue, pmcClk):
        if(pmcClk.getValue() == "SLOW_CLK"):
            pmcClkValue.setValue("SYS_CLK_PMC_MCKR_CSS_VALUE", "SYS_CLK_SOURCE_SLOW", 1)
        elif(pmcClk.getValue() == "MAIN_CLK"):
            pmcClkValue.setValue("SYS_CLK_PMC_MCKR_CSS_VALUE", "SYS_CLK_SOURCE_MAIN", 1)
        elif(pmcClk.getValue() == "PLLA_CLK"):
            pmcClkValue.setValue("SYS_CLK_PMC_MCKR_CSS_VALUE", "SYS_CLK_SOURCE_PLLA", 1)
        else:
            pmcClkValue.setValue("SYS_CLK_PMC_MCKR_CSS_VALUE", "SYS_CLK_SOURCE_USB_PLL", 1)
            
pmcCongig = coreComponent.createMenuSymbol("pmcConfig", clkSettings)
pmcCongig.setLabel("Processor and Master Clock Configuration")

pmcClk = coreComponent.createComboSymbol("SYS_CLK_PMC_MCKR_CSS", pmcCongig, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK"])
pmcClk.setLabel("Processor and Master Clock")
pmcClk.setDefaultValue("SLOW_CLK")

pmcClkValue = coreComponent.createStringSymbol("SYS_CLK_PMC_MCKR_CSS_VALUE", None)
pmcClkValue.setVisible(False)
pmcClkValue.setDependencies(setPMCClkSrc, ["SYS_CLK_PMC_MCKR_CSS"])

clkPrescaler = coreComponent.createComboSymbol("SYS_CLK_PMC_MCKR_PRES", pmcCongig, ["DIV_1", "DIV_2", "DIV_3", "DIV_4", "DIV_8", "DIV_16","DIV_32", "DIV_64"])
clkPrescaler.setLabel("Processor Clock Prescaler")
clkPrescaler.setDefaultValue("DIV_1")

clkPrescalerValue = coreComponent.createStringSymbol("SYS_CLK_PMC_MCKR_PRES_VALUE", None)
clkPrescalerValue.setVisible(False)
# TO-DO: Add def code

clkDivider = coreComponent.createComboSymbol("SYS_CLK_PMC_MCKR_MDIV", pmcCongig, ["DIV_1", "DIV_2", "DIV_3", "DIV_4"])
clkDivider.setLabel("Master Clock Divider")
clkDivider.setDefaultValue("DIV_2")

clkDividerValue = coreComponent.createStringSymbol("SYS_CLK_PMC_MCKR_MDIV_VALUE", None)
clkDividerValue.setVisible(False)
# TO-DO: Add def code

#USB Clock Configuration
def setUSBDividerVisibleProperty(upllDivider, usbHSClk):
        if (usbHSClk.getValue() == True):
            print("USBHS Enabled")
            upllDivider.setVisible(True)
        else :
            print("USBHS Disabled")
            upllDivider.setVisible(False)
            
usbClkConfig = coreComponent.createMenuSymbol("usbClkConfig", clkSettings)
usbClkConfig.setLabel("USB Clock Configuration")

usbHSClk = coreComponent.createBooleanSymbol("SYS_CLK_CKGR_UCKR_UPLLEN", usbClkConfig)
usbHSClk.setLabel("Enable USB HS Clock")

utmiTrimFreq = coreComponent.createStringSymbol("SYS_CLK_UTMI_CKTRIM_FREQ", usbHSClk)
utmiTrimFreq.setVisible(False)

utmiTrimFreqValue = coreComponent.createIntegerSymbol("SYS_CLK_UTMI_CKTRIM_FREQ_VALUE", None)
utmiTrimFreqValue.setVisible(False)
# TO-DO: Add def code

upllDivider = coreComponent.createComboSymbol("SYS_CLK_PMC_MCKR_UPLLDIV2", usbHSClk, ["DIV_1", "DIV_2"])
upllDivider.setLabel("UPLL Divider")
upllDivider.setDefaultValue("DIV_1")
upllDivider.setVisible(False)
upllDivider.setDependencies(setUSBDividerVisibleProperty, ["SYS_CLK_CKGR_UCKR_UPLLEN"])

upllDividerValue = coreComponent.createIntegerSymbol("SYS_CLK_PMC_MCKR_UPLLDIV2_VALUE", None)
upllDividerValue.setVisible(False)
# TO-DO: Add def code

usbFSClk = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_USBCLK", usbClkConfig)
usbFSClk.setLabel("Enable USB FS Clock")

usbInputClk = coreComponent.createComboSymbol("SYS_CLK_PMC_USB_USBS", usbFSClk, ["PLLA_CLK", "UPLL_CLK"])
usbInputClk.setLabel("USB Input Clock")
usbInputClk.setDefaultValue("UPLL_CLK")

usbInputClkValue = coreComponent.createStringSymbol("SYS_CLK_PMC_USB_USBS_VALUE", None)
usbInputClkValue.setVisible(False)
# TO-DO: Add def code

usbClkDivider = coreComponent.createIntegerSymbol("SYS_CLK_PMC_USB_USBDIV", usbFSClk)
usbClkDivider.setLabel("USB_48M Clock Divider")
usbClkDivider.setEnabled(False)
usbClkDivider.setMin(1)
usbClkDivider.setMax(16)
usbClkDivider.setDefaultValue(1)

#Peripheral clock generator configuration options
def setGenericClkSrcVisible(genericClk0Src, genericClk0Enable):
    if(genericClk0Enable.getValue() == True):
        print("GCLK Enabled")
        genericClk0Src.setVisible(True)
    else :
        print("GCLK Disabled")
        genericClk0Src.setVisible(False)

def setGenericClkDivVisible(genericClk0Divider, genericClk0Enable):
    if(genericClk0Enable.getValue() == True):
        print("GCLK Enabled")
        genericClk0Divider.setVisible(True)
    else :
        print("GCLK Disabled")
        genericClk0Divider.setVisible(False)
        
peripheralClkConfig = coreComponent.createMenuSymbol("peripheralClkConfig", clkSettings)
peripheralClkConfig.setLabel("Peripheral Clock Generator Configuration")

peripheralClk0Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_PCR_EN0", peripheralClkConfig)
peripheralClk0Enable.setLabel("Enable Peripheral Clock 0")

genericClk0Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_PCR_GCLKEN0", peripheralClkConfig)
genericClk0Enable.setLabel("Enable Generic Clock 0")

genericClk0Divider = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCR_GCLKDIV0", genericClk0Enable)
genericClk0Divider.setLabel("Generic Clock Divider 0")
genericClk0Divider.setMin(1)
genericClk0Divider.setMax(256)
genericClk0Divider.setDefaultValue(1)
#genericClk0Divider.setVisible(False)
#genericClk0Divider.setDependencies(setGenericClkDivVisible, ["SYS_CLK_PMC_PCR_GCLKEN0"])

genericClk0Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCR_GCLKCSS0", genericClk0Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
genericClk0Src.setLabel("Generic Clock Source (I2S0")
genericClk0Src.setDefaultValue("SLOW_CLK")
genericClk0Src.setVisible(False)
genericClk0Src.setDependencies(setGenericClkSrcVisible, ["SYS_CLK_PMC_PCR_GCLKEN0"])

genericClk0SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCR_GCLKCSS0_VALUE", None)
genericClk0SrcValue.setVisible(False)
# TO-DO: Add def code

peripheralClk1Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_PCR_EN1", peripheralClkConfig)
peripheralClk1Enable.setLabel("Enable Peripheral Clock 1")

genericClk1Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_PCR_GCLKEN1", peripheralClkConfig)
genericClk1Enable.setLabel("Enable Generic Clock 1")

genericClk1Divider = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCR_GCLKDIV1", genericClk1Enable)
genericClk1Divider.setLabel("Generic Clock Divider 1")
genericClk1Divider.setMin(1)
genericClk1Divider.setMax(256)
genericClk1Divider.setDefaultValue(1)

genericClk1Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCR_GCLKCSS1", genericClk1Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
genericClk1Src.setLabel("Generic Clock Source (I2S1")
genericClk1Src.setDefaultValue("SLOW_CLK")

genericClk1SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCR_GCLKCSS1_VALUE", None)
genericClk1SrcValue.setVisible(False)
# TO-DO: Add def code

#Programmable Clock generator configuration options
programmableClkConfig = coreComponent.createMenuSymbol("programmableClkConfig", clkSettings)
programmableClkConfig.setLabel("Programmable Clock Generator Configuration")

pck0Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK0", programmableClkConfig)
pck0Enable.setLabel("Enable PCK0")

clk0Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK0_CSS", pck0Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk0Src.setLabel("Clock Source")
clk0Src.setDefaultValue("SLOW_CLK")

clk0SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK0_CSS_VALUE", None)
clk0SrcValue.setVisible(False)
# TO-DO: Add def code

clk0prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK0_PRES", pck0Enable)
clk0prescaler.setLabel("Prescaler")
clk0prescaler.setMin(1)
clk0prescaler.setMax(256)
clk0prescaler.setDefaultValue(1)

pck1Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK1", programmableClkConfig)
pck1Enable.setLabel("Enable PCK1")

clk1Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK1_CSS", pck1Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk1Src.setLabel("Clock Source")
clk1Src.setDefaultValue("SLOW_CLK")

clk1SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK1_CSS_VALUE", None)
clk1SrcValue.setVisible(False)
# TO-DO: Add def code

clk1prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK1_PRES", pck1Enable)
clk1prescaler.setLabel("Prescaler")
clk1prescaler.setMin(1)
clk1prescaler.setMax(256)
clk1prescaler.setDefaultValue(1)

pck2Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK2", programmableClkConfig)
pck2Enable.setLabel("Enable PCK2")

clk2Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK2_CSS", pck2Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk2Src.setLabel("Clock Source")
clk2Src.setDefaultValue("SLOW_CLK")

clk2SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK2_CSS_VALUE", None)
clk2SrcValue.setVisible(False)
# TO-DO: Add def code

clk2prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK2_PRES", pck2Enable)
clk2prescaler.setLabel("Prescaler")
clk2prescaler.setMin(1)
clk2prescaler.setMax(256)
clk2prescaler.setDefaultValue(1)

pck3Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK3", programmableClkConfig)
pck3Enable.setLabel("Enable PCK3")

clk3Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK3_CSS", pck3Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk3Src.setLabel("Clock Source")
clk3Src.setDefaultValue("SLOW_CLK")

clk3SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK3_CSS_VALUE", None)
clk3SrcValue.setVisible(False)
# TO-DO: Add def code

clk3prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK3_PRES", pck3Enable)
clk3prescaler.setLabel("Prescaler")
clk3prescaler.setMin(1)
clk3prescaler.setMax(256)
clk3prescaler.setDefaultValue(1)

pck4Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK4", programmableClkConfig)
pck4Enable.setLabel("Enable PCK4")

clk4Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK4_CSS", pck4Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk4Src.setLabel("Clock Source")
clk4Src.setDefaultValue("SLOW_CLK")

clk4SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK4_CSS_VALUE", None)
clk4SrcValue.setVisible(False)
# TO-DO: Add def code

clk4prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK4_PRES", pck4Enable)
clk4prescaler.setLabel("Prescaler")
clk4prescaler.setMin(1)
clk4prescaler.setMax(256)
clk4prescaler.setDefaultValue(1)

pck5Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK5", programmableClkConfig)
pck5Enable.setLabel("Enable PCK5")

clk5Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK5_CSS", pck5Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk5Src.setLabel("Clock Source")
clk5Src.setDefaultValue("SLOW_CLK")

clk5SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK5_CSS_VALUE", None)
clk5SrcValue.setVisible(False)
# TO-DO: Add def code

clk5prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK5_PRES", pck5Enable)
clk5prescaler.setLabel("Prescaler")
clk5prescaler.setMin(1)
clk5prescaler.setMax(256)
clk5prescaler.setDefaultValue(1)

pck6Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK6", programmableClkConfig)
pck6Enable.setLabel("Enable PCK6")

clk6Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK6_CSS", pck6Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk6Src.setLabel("Clock Source")
clk6Src.setDefaultValue("SLOW_CLK")

clk6SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK6_CSS_VALUE", None)
clk6SrcValue.setVisible(False)
# TO-DO: Add def code

clk6prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK6_PRES", pck6Enable)
clk6prescaler.setLabel("Prescaler")
clk6prescaler.setMin(1)
clk6prescaler.setMax(256)
clk6prescaler.setDefaultValue(1)

pck7Enable = coreComponent.createBooleanSymbol("SYS_CLK_PMC_SCER_PCK7", programmableClkConfig)
pck7Enable.setLabel("Enable PCK7")

clk7Src = coreComponent.createComboSymbol("SYS_CLK_PMC_PCK7_CSS", pck7Enable, ["SLOW_CLK", "MAIN_CLK", "PLLA_CLK", "UPLL_CLK", "MCK"])
clk7Src.setLabel("Clock Source")
clk7Src.setDefaultValue("SLOW_CLK")

clk7SrcValue = coreComponent.createStringSymbol("SYS_CLK_PMC_PCK7_CSS_VALUE", None)
clk7SrcValue.setVisible(False)
# TO-DO: Add def code

clk7prescaler = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCK7_PRES", pck7Enable)
clk7prescaler.setLabel("Prescaler")
clk7prescaler.setMin(1)
clk7prescaler.setMax(256)
clk7prescaler.setDefaultValue(1)

#Calculated Clock Frequencies
calculatedFrequencies = coreComponent.createMenuSymbol("calculatedFrequencies", clkSettings)
calculatedFrequencies.setLabel("Calculated Clock Frequencies")

systemTickFreq = coreComponent.createStringSymbol("SYS_CLK_SYSTICK", calculatedFrequencies)
systemTickFreq.setLabel("System Tick Frequency (HZ)")
systemTickFreq.setDefaultValue("37500000")
systemTickFreq.setReadOnly(True)

processorClkFreq = coreComponent.createStringSymbol("SYS_CLK_PROCESSORCLK_FREQ", calculatedFrequencies)
processorClkFreq.setLabel("Processor Clock Frequency (HZ)")
processorClkFreq.setDefaultValue("300000000")
processorClkFreq.setReadOnly(True)

masterClkFreq = coreComponent.createStringSymbol("SYS_CLK_MASTERCLK_FREQ", calculatedFrequencies)
masterClkFreq.setLabel("Master Clock Frequency (HZ)")
masterClkFreq.setDefaultValue("150000000")
masterClkFreq.setReadOnly(True)

i2s0Freq = coreComponent.createStringSymbol("SYS_CLK_I2S0_FREQ", calculatedFrequencies)
i2s0Freq.setLabel("I2S0 Frequency (HZ)")
i2s0Freq.setDefaultValue("75000000")
i2s0Freq.setReadOnly(True)

i2s1Freq = coreComponent.createStringSymbol("SYS_CLK_I2S1_FREQ", calculatedFrequencies)
i2s1Freq.setLabel("I2S1 Frequency (HZ)")
i2s1Freq.setDefaultValue("100000000")
i2s1Freq.setReadOnly(True)

pck0Freq = coreComponent.createStringSymbol("SYS_CLK_PCK0_FREQ", calculatedFrequencies)
pck0Freq.setLabel("Programmable clock #0 Frequency (HZ)")
pck0Freq.setDefaultValue("12000000")
pck0Freq.setReadOnly(True)

pck1Freq = coreComponent.createStringSymbol("SYS_CLK_PCK1_FREQ", calculatedFrequencies)
pck1Freq.setLabel("Programmable clock #1 Frequency (HZ)")
pck1Freq.setDefaultValue("6000000")
pck1Freq.setReadOnly(True)

pck2Freq = coreComponent.createStringSymbol("SYS_CLK_PCK2_FREQ", calculatedFrequencies)
pck2Freq.setLabel("Programmable clock #2 Frequency (HZ)")
pck2Freq.setDefaultValue("4000000")
pck2Freq.setReadOnly(True)

pck3Freq = coreComponent.createStringSymbol("SYS_CLK_PCK3_FREQ", calculatedFrequencies)
pck3Freq.setLabel("Programmable clock #3 Frequency (HZ)")
pck3Freq.setDefaultValue("3000000")
pck3Freq.setReadOnly(True)

pck4Freq = coreComponent.createStringSymbol("SYS_CLK_PCK4_FREQ", calculatedFrequencies)
pck4Freq.setLabel("Programmable clock #4 Frequency (HZ)")
pck4Freq.setDefaultValue("2400000")
pck4Freq.setReadOnly(True)

pck5Freq = coreComponent.createStringSymbol("SYS_CLK_PCK5_FREQ", calculatedFrequencies)
pck5Freq.setLabel("Programmable clock #5 Frequency (HZ)")
pck5Freq.setDefaultValue("2000000")
pck5Freq.setReadOnly(True)

pck6Freq = coreComponent.createStringSymbol("SYS_CLK_PCK6_FREQ", calculatedFrequencies)
pck6Freq.setLabel("Programmable clock #6 Frequency (HZ)")
pck6Freq.setDefaultValue("1714285")
pck6Freq.setReadOnly(True)

pck7Freq = coreComponent.createStringSymbol("SYS_CLK_PCK7_FREQ", calculatedFrequencies)
pck7Freq.setLabel("Programmable clock #7 Frequency (HZ)")
pck7Freq.setDefaultValue("1500000")
pck7Freq.setReadOnly(True)

usbFsFreq = coreComponent.createStringSymbol("SYS_CLK_USBFS_FREQ", calculatedFrequencies)
usbFsFreq.setLabel("USB Clock Frequency (HZ)")
usbFsFreq.setDefaultValue("48000000")
usbFsFreq.setReadOnly(True)

usbHsFreq = coreComponent.createStringSymbol("SYS_CLK_USBHS_FREQ", calculatedFrequencies)
usbHsFreq.setLabel("USB High Speed Clock Frequency (HZ)")
usbHsFreq.setDefaultValue("480000000")
usbHsFreq.setReadOnly(True)

#Register configurations
pid0 = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCR_PID0", None)
pid0.setDefaultValue(69)
pid0.setVisible(False)

pid1 = coreComponent.createIntegerSymbol("SYS_CLK_PMC_PCR_PID1", None)
pid1.setDefaultValue(70)
pid1.setVisible(False)

uart0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_UART0", None)
uart0.setVisible(False)

uart1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_UART1", None)
uart1.setVisible(False)

uart2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_UART2", None)
uart2.setVisible(False)

uart3 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_UART3", None)
uart3.setVisible(False)

uart4 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_UART4", None)
uart4.setVisible(False)

smc = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_SMC", None)
smc.setVisible(False)

portA = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PORTA", None)
portA.setVisible(False)

portB = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PORTB", None)
portB.setVisible(False)

portC = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PORTC", None)
portC.setVisible(False)

portD = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PORTD", None)
portD.setVisible(False)

portE = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PORTE", None)
portE.setVisible(False)

usart0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_USART0", None)
usart0.setVisible(False)

usart1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_USART1", None)
usart1.setVisible(False)

usart2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_USART2", None)
usart2.setVisible(False)

hsmci = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_HSMCI", None)
hsmci.setVisible(False)

twi0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TWI0", None)
twi0.setVisible(False)

spi0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_SPI0", None)
spi0.setVisible(False)

spi1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_SPI1", None)
spi1.setVisible(False)

ssc = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_SSC", None)
ssc.setVisible(False)

tc0channel0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC0_CHANNEL0", None)
tc0channel0.setVisible(False)

tc0channel1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC0_CHANNEL1", None)
tc0channel1.setVisible(False)

tc0channel2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC0_CHANNEL2", None)
tc0channel2.setVisible(False)

tc1channel0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC1_CHANNEL0", None)
tc1channel0.setVisible(False)

tc1channel1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC1_CHANNEL1", None)
tc1channel1.setVisible(False)

tc1channel2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC1_CHANNEL2", None)
tc1channel2.setVisible(False)

tc2channel0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC2_CHANNEL0", None)
tc2channel0.setVisible(False)

tc2channel1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC2_CHANNEL1", None)
tc2channel1.setVisible(False)

tc2channel2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC2_CHANNEL2", None)
tc2channel2.setVisible(False)

tc3channel0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC3_CHANNEL0", None)
tc3channel0.setVisible(False)

tc3channel1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC3_CHANNEL1", None)
tc3channel1.setVisible(False)

tc3channel2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TC3_CHANNEL2", None)
tc3channel2.setVisible(False)

afec0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_AFEC0", None)
afec0.setVisible(False)

afec1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_AFEC1", None)
afec1.setVisible(False)

dacc = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_DACC", None)
dacc.setVisible(False)

pwm0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PWM0", None)
pwm0.setVisible(False)

pwm1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_PWM1", None)
pwm1.setVisible(False)

icm = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_ICM", None)
icm.setVisible(False)

usbhs = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_USBHS", None)
usbhs.setVisible(False)

mcan0 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_MCAN0", None)
mcan0.setVisible(False)

mcan1 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_MCAN1", None)
mcan1.setVisible(False)

gmac = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_GMAC", None)
gmac.setVisible(False)

twihs2 = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TWIHS2", None)
twihs2.setVisible(False)

qspi = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_QSPI", None)
qspi.setVisible(False)

mlb = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_MLB", None)
mlb.setVisible(False)

aes = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_AES", None)
aes.setVisible(False)

trng = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_TRNG", None)
trng.setVisible(False)

xdmac = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_XDMAC", None)
xdmac.setVisible(False)

isi = coreComponent.createBooleanSymbol("SYS_CLK_PMC_ID_ISI", None)
isi.setVisible(False)

#To-Do: Change symbol type to Hex
pcer0 = coreComponent.createStringSymbol("SYS_CLK_PMC_PCER0", None)
pcer0.setVisible(False)

pcer1 = coreComponent.createStringSymbol("SYS_CLK_PMC_PCER1", None)
pcer1.setVisible(False)

#File handling
configName = Variables.get("__CONFIGURATION_NAME")

clkHeaderFile = coreComponent.createFileSymbol(None, None)
clkHeaderFile.setSourcePath("../peripheral/clk_sam_e70/sys_clk.h")
clkHeaderFile.setOutputName("sys_clk.h")
clkHeaderFile.setDestPath("peripheral/clk/")
clkHeaderFile.setProjectPath("config/" + configName + "/peripheral/clk/")
clkHeaderFile.setType("HEADER")

clkSourceFile = coreComponent.createFileSymbol(None, None)
clkSourceFile.setSourcePath("../peripheral/clk_sam_e70/templates/sys_clk_static_pic32cz.c.ftl")
clkSourceFile.setOutputName("sys_clk_static.c")
clkSourceFile.setDestPath("peripheral/clk/")
clkSourceFile.setProjectPath("config/" + configName + "/peripheral/clk/")
clkSourceFile.setMarkup(True)
clkSourceFile.setType("SOURCE")

#Add clock related code to common files
systemDefinitionsHeadersList.addValue("#include \"peripheral/clk/sys_clk.h\"")

clkSystemInitFile = coreComponent.createFileSymbol(None, None)
clkSystemInitFile.setType("STRING")
clkSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clkSystemInitFile.setSourcePath("../peripheral/clk_sam_e70/templates/sys_clk_system_init.c.ftl")
clkSystemInitFile.setMarkup(True)

