
from os.path import join
from xml.etree import ElementTree

global fwsMaxFreqList

def updateFWSValue(clkSymFlashWaitStates, masterClkFreq):

	minFreq = maxFreq = 0
	for fws in range(0, len(fwsMaxFreqList), 1):
		
		mckFreq = int(masterClkFreq.getValue())
		maxFreq = int(fwsMaxFreqList[fws])
		
		if mckFreq <= maxFreq and mckFreq > minFreq:
			clkSymFlashWaitStates.setValue("EEFC_FMR_FWS", str(fws), 1)
			return
			
		minFreq = maxFreq
	
#PLLA Configuration
def setDividerVisibleProperty(pllaDivider, pllaClkEnable):
	if (pllaClkEnable.getValue() == True):
		pllaDivider.setVisible(True)
	else :
		pllaDivider.setVisible(False)

def setMultiplierVisibleProperty(pllaMultiplier, pllaClkEnable):
	if (pllaClkEnable.getValue() == True):
		pllaMultiplier.setVisible(True)
	else :
		pllaMultiplier.setVisible(False)

#USB Clock Configuration
def setUSBDividerVisibleProperty(upllDivider, usbHSClk):
	if (usbHSClk.getValue() == True):
		upllDivider.setVisible(True)
	else :
		upllDivider.setVisible(False)

#Peripheral clock generator configuration options
def setGenericClkSrcVisible(genericClk0Src, genericClk0Enable):
    if(genericClk0Enable.getValue() == True):
        genericClk0Src.setVisible(True)
    else :
        genericClk0Src.setVisible(False)

def setGenericClkDivVisible(genericClkDivider, genericClkEnable):
    if(genericClkEnable.getValue() == True):
        genericClkDivider.setVisible(True)
    else :
        genericClkDivider.setVisible(False)

#set/reset the readOnly property of Slow Clock Frequency
def resetReadOnlySlowClkFreq(clkSymExtClkInputFreq, clkSym_SUPC_MR_OSCBYPASS):

	if clkSym_SUPC_MR_OSCBYPASS.getValue() is True:
		clkSymExtClkInputFreq.setReadOnly(True)
	else:
		clkSymExtClkInputFreq.setReadOnly(False)

def updateExtXtalEnable(clkSymCrystalOscEnable, clkSymOscBypass):
	if clkSymOscBypass.getValue() is True:
		clkSymCrystalOscEnable.clearValue("PMC_CKGR_MOR_MOSCXTEN")
		clkSymCrystalOscEnable.setValue("PMC_CKGR_MOR_MOSCXTEN", False, 1)

# slow RC/Crystal Oscillator 
def slowClock(clkComponent, clkSymMenu, supcRegModule, resetReadOnlySlowClkFreq):

    # creates Slow Clock Configuration Menu
	clkSymMenu = clkComponent.createMenuSymbol("CLK_SLOW", clkSymMenu)
	clkSymMenu.setLabel("Slow Clock Configuration")
	
	# get SUPC register group
	supcRegGroup = supcRegModule.getRegisterGroup("SUPC")
	
	# get SUPC_CR Register
	supcReg_SUPC_CR = supcRegGroup.getRegister("SUPC_CR")
	
	# get XTALSEL Bitfield of SUPC_CR Register 
	supcBitField_SUPC_CR_XTALSEL = supcReg_SUPC_CR.getBitfield("XTALSEL")
	supcValGrp_SUPC_CR_XTALSEL = supcRegModule.getValueGroup(supcBitField_SUPC_CR_XTALSEL.getValueGroupName())

	# Create Combo symbol for XTALSEL Bitfield of SUPC_CR Register
	clkSym_SUPC_CR_XTALSEL = clkComponent.createBooleanSymbol("SUPC_CR_XTALSEL", clkSymMenu)
	clkSym_SUPC_CR_XTALSEL.setLabel(supcBitField_SUPC_CR_XTALSEL.getDescription())
	clkSym_SUPC_CR_XTALSEL.setDefaultValue(False)
	
	# get SUPC_MR Register
	supcReg_SUPC_MR = supcRegGroup.getRegister("SUPC_MR")
	
	# get OSCBYPASS Bitfield of SUPC_MR Register
	supcBitField_SUPC_MR_OSCBYPASS = supcReg_SUPC_MR.getBitfield("OSCBYPASS")

	# Create Boolean symbol for OSCBYPASS Bitfield of SUPC_MR Register
	clkSym_SUPC_MR_OSCBYPASS = clkComponent.createBooleanSymbol("SUPC_MR_OSCBYPASS", clkSym_SUPC_CR_XTALSEL)
	clkSym_SUPC_MR_OSCBYPASS.setLabel(supcBitField_SUPC_MR_OSCBYPASS.getDescription())
	clkSym_SUPC_MR_OSCBYPASS.setDefaultValue(False)
	
	# set slow clock input frequency
	clkSymExtClkInputFreq = clkComponent.createIntegerSymbol("CLK_SLOW_XTAL", clkSym_SUPC_CR_XTALSEL)
	clkSymExtClkInputFreq.setLabel("External Slow Clock Input Frequency (Hz)")
	clkSymExtClkInputFreq.setDefaultValue(32768)
	clkSymExtClkInputFreq.setReadOnly(True)
	clkSymExtClkInputFreq.setDependencies(resetReadOnlySlowClkFreq, ["SUPC_MR_OSCBYPASS"])

# Main RC/Crystal Oscillator
def mainClock(clkComponent, clkSymMenu, pmcRegModule, updateExtXtalEnable):

    # create Main Clock Configuration Menu
	clkSymMenu = clkComponent.createMenuSymbol("CLK_MAIN", clkSymMenu)
	clkSymMenu.setLabel("Main Clock Configuration")
	
	# get PMC register group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")
	
	# get CKGR_MOR Register
	pmcReg_CKGR_MOR = pmcRegGroup.getRegister("CKGR_MOR")
	
	# get MOSCRCEN Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCRCEN = pmcReg_CKGR_MOR.getBitfield("MOSCRCEN")
	
	# create symbol for MOSCRCEN Bitfield of CKGR_MOR Register
	clkSymRCEnable = clkComponent.createBooleanSymbol("PMC_CKGR_MOR_MOSCRCEN", clkSymMenu)
	clkSymRCEnable.setLabel(pmcBitField_CKGR_MOR_MOSCRCEN.getDescription())
	clkSymRCEnable.setDefaultValue(True)

	# get MOSCRCF Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCRCF = pmcReg_CKGR_MOR.getBitfield("MOSCRCF")
	
	# get value group for MOSCRCF Bitfield of CKGR_MOR Register
	pmcValGrp_CKGR_MOR_MOSCRCF = pmcRegModule.getValueGroup(pmcBitField_CKGR_MOR_MOSCRCF.getValueGroupName())
	
	# create symbol for MOSCRCF Bitfield of CKGR_MOR Register
	clkSymRCFreq = clkComponent.createComboSymbol("PMC_CKGR_MOR_MOSCRCF", clkSymRCEnable, pmcValGrp_CKGR_MOR_MOSCRCF.getValueNames())
	clkSymRCFreq.setLabel(pmcBitField_CKGR_MOR_MOSCRCF.getDescription())
	clkSymRCFreq.setDefaultValue("_12_MHz")
	
	# get MOSCXTBY Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCXTBY = pmcReg_CKGR_MOR.getBitfield("MOSCXTBY")
	
	# create symbol for MOSCXTBY Bitfield of CKGR_MOR Register
	clkSymOscBypass = clkComponent.createBooleanSymbol("PMC_CKGR_MOR_MOSCXTBY", clkSymMenu)
	clkSymOscBypass.setLabel(pmcBitField_CKGR_MOR_MOSCXTBY.getDescription())
	
	# get MOSCXTEN Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCXTEN = pmcReg_CKGR_MOR.getBitfield("MOSCXTEN")

	# create Boolean Symbol for MOSCXTEN Bitfield of CKGR_MOR Register
	clkSymCrystalOscEnable = clkComponent.createBooleanSymbol("PMC_CKGR_MOR_MOSCXTEN", clkSymMenu)
	clkSymCrystalOscEnable.setLabel(pmcBitField_CKGR_MOR_MOSCXTEN.getDescription())
	clkSymCrystalOscEnable.setDefaultValue(False)
	clkSymCrystalOscEnable.setDependencies(updateExtXtalEnable, ["PMC_CKGR_MOR_MOSCXTBY"])

	# create integer symbol for external main clock frequency
	clkSymExtClkInputFreq = clkComponent.createIntegerSymbol("CLK_MAIN_XTAL", clkSymCrystalOscEnable)
	clkSymExtClkInputFreq.setLabel("External Main Clock Input Frequency (Hz)")
	clkSymExtClkInputFreq.setDefaultValue(12000000)
	clkSymExtClkInputFreq.setMin(3000000)
	clkSymExtClkInputFreq.setMax(20000000)
	
	# get MOSCXTST Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCXTST = pmcReg_CKGR_MOR.getBitfield("MOSCXTST")
	
	# get symbol for MOSCXTST Bitfield of CKGR_MOR Register
	clkSymCrystalOscStartupTime = clkComponent.createIntegerSymbol("PMC_CKGR_MOR_MOSCXTST", clkSymCrystalOscEnable)
	clkSymCrystalOscStartupTime.setLabel(pmcBitField_CKGR_MOR_MOSCXTST.getDescription())
	clkSymCrystalOscStartupTime.setDefaultValue(255)
	clkSymCrystalOscStartupTime.setMin(0)
	clkSymCrystalOscStartupTime.setMax(255)

	# get MOSCSEL Bitfield of CKGR_MOR Register
	pmcBitField_CKGR_MOR_MOSCSEL = pmcReg_CKGR_MOR.getBitfield("MOSCSEL")
	
	# create symbol for main clock source
	clkSymClkSource = clkComponent.createBooleanSymbol("PMC_CKGR_MOR_MOSCSEL", clkSymMenu)
	clkSymClkSource.setLabel(pmcBitField_CKGR_MOR_MOSCSEL.getDescription())
	clkSymClkSource.setDefaultValue(False)
        
def pllA(clkComponent, clkSymMenu, pmcRegModule, setDividerVisibleProperty, setMultiplierVisibleProperty):

    # create PLLA Configuration Menu
	clkSymMenu = clkComponent.createMenuSymbol("CLK_PLLA", clkSymMenu)
	clkSymMenu.setLabel("Clock PLL Configuration")

	# get PMC register group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")
	
	# get CKGR_PLLAR register
	pmcReg_CKGR_PLLAR = pmcRegGroup.getRegister("CKGR_PLLAR")
	
	# create symbol to enable/disable PLLA
	clkSymPLLAEnable = clkComponent.createBooleanSymbol("CLK_PLLA_ENABLE", clkSymMenu)
	clkSymPLLAEnable.setLabel("Enable PLLA Clock")
	clkSymPLLAEnable.setDefaultValue(True)

	# get DIVA Bitfield of CKGR_PLLAR Register
	pmcReg_CKGR_PLLAR_DIVA = pmcReg_CKGR_PLLAR.getBitfield("DIVA")
	
	# create symbol for DIVA Bitfield of CKGR_PLLAR Register
	clkSymDivider = clkComponent.createIntegerSymbol("PMC_CKGR_PLLAR_DIVA", clkSymPLLAEnable)
	clkSymDivider.setLabel(pmcReg_CKGR_PLLAR_DIVA.getDescription())
	clkSymDivider.setMin(0)
	clkSymDivider.setMax(255)
	clkSymDivider.setDefaultValue(1)
	clkSymDivider.setDependencies(setDividerVisibleProperty, ["CLK_PLLA_ENABLE"])

	# get MULA Bitfield of CKGR_PLLAR register
	pmcReg_CKGR_PLLAR_MULA = pmcReg_CKGR_PLLAR.getBitfield("MULA")
	
	# create symbol for MULA Bitfield of CKGR_PLLAR Register
	clkSymMultiplier = clkComponent.createIntegerSymbol("PMC_CKGR_PLLAR_MULA", clkSymPLLAEnable)
	clkSymMultiplier.setLabel(pmcReg_CKGR_PLLAR_MULA.getDescription())
	clkSymMultiplier.setMin(0)
	clkSymMultiplier.setMax(63)
	clkSymMultiplier.setDefaultValue(25)
	clkSymMultiplier.setDependencies(setMultiplierVisibleProperty, ["CLK_PLLA_ENABLE"])
    
def masterClock(clkComponent, clkSymMenu, pmcRegModule):

	# create symbol for Master Clock Menu.
	clkSymMenu = clkComponent.createMenuSymbol("CLK_MASTER", clkSymMenu)
	clkSymMenu.setLabel("Processor and Master Clock Configuration")
	
	# get PMC Register Group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")
	
	# get PMC_MCKR register
	pmcReg_PMC_MCKR = pmcRegGroup.getRegister("PMC_MCKR")
	
	# get CSS Bitfield of PMC_MCKR register
	pmcBitField_PMC_MCKR_CSS = pmcReg_PMC_MCKR.getBitfield("CSS")
	
	# get Value Group for CSS Bitfield of PMC_MCKR register
	pmcValGrp_PMC_MCKR_CSS = pmcRegModule.getValueGroup(pmcBitField_PMC_MCKR_CSS.getValueGroupName())
	
	# create symbol for CSS Bitfield of PMC_MCKR register
	clkSym_PMC_MCKR_CSS = clkComponent.createComboSymbol("PMC_MCKR_CSS", clkSymMenu, pmcValGrp_PMC_MCKR_CSS.getValueNames())
	clkSym_PMC_MCKR_CSS.setLabel(pmcBitField_PMC_MCKR_CSS.getDescription())
	clkSym_PMC_MCKR_CSS.setDefaultValue("PLLA_CLK")
	
	# get PRES Bitfield of PMC_MCKR register
	pmcBitField_PMC_MCKR_PRES = pmcReg_PMC_MCKR.getBitfield("PRES")
	
	# get Value Group for PRES Bitfield of PMC_MCKR register
	pmcValGrp_PMC_MCKR_PRES = pmcRegModule.getValueGroup(pmcBitField_PMC_MCKR_PRES.getValueGroupName())

	# create symbol for PRES Bitfield of PMC_MCKR register
	clkSym_PMC_MCKR_PRES = clkComponent.createComboSymbol("PMC_MCKR_PRES", clkSymMenu, pmcValGrp_PMC_MCKR_PRES.getValueNames())
	clkSym_PMC_MCKR_PRES.setLabel(pmcBitField_PMC_MCKR_PRES.getDescription())
	clkSym_PMC_MCKR_PRES.setDefaultValue("CLK_1")

	# get MDIV Bitfield of PMC_MCKR register
	pmcBitField_PMC_MCKR_MDIV = pmcReg_PMC_MCKR.getBitfield("MDIV")
	
	# get Value Group for MDIV Bitfield of PMC_MCKR register
	pmcValGrp_PMC_MCKR_MDIV = pmcRegModule.getValueGroup(pmcBitField_PMC_MCKR_MDIV.getValueGroupName())
	
	clkSym_PMC_MCKR_MDIV = clkComponent.createComboSymbol("PMC_MCKR_MDIV", clkSymMenu, pmcValGrp_PMC_MCKR_MDIV.getValueNames())
	clkSym_PMC_MCKR_MDIV.setLabel(pmcBitField_PMC_MCKR_MDIV.getDescription())
	clkSym_PMC_MCKR_MDIV.setDefaultValue("PCK_DIV2")
	
def usbClock(clkComponent, clkSymMenu, pmcRegModule, utmiRegModule, setUSBDividerVisibleProperty):

	# create symbol for USB Clock Menu
	clkSymMenu = clkComponent.createMenuSymbol("CLK_USB", clkSymMenu)
	clkSymMenu.setLabel("USB Clock Configuration")
	
	# get PMC register group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")

	# get CKGR_UCKR register
	pmcReg_CKGR_UCKR = pmcRegGroup.getRegister("CKGR_UCKR")
	
	# get UPLLEN Bitfield of CKGR_UCKR register
	pmcBitField_CKGR_UCKR_UPLLEN = pmcReg_CKGR_UCKR.getBitfield("UPLLEN")
	
	# create symbol for UPLLEN Bitfield of CKGR_UCKR register
	clkSym_CKGR_UCKR_UPLLEN = clkComponent.createBooleanSymbol("PMC_CKGR_UCKR_UPLLEN", clkSymMenu)
	clkSym_CKGR_UCKR_UPLLEN.setLabel(pmcBitField_CKGR_UCKR_UPLLEN.getDescription())
	
	# get UTMI register group
	utmiRegGroup = utmiRegModule.getRegisterGroup("UTMI")
	
	# get UTMI_CKTRIM register
	utmiReg_UTMI_CKTRIM = utmiRegGroup.getRegister("UTMI_CKTRIM")
	
	# get FREQ bitfield of UTMI_CKTRIM register
	utmiBitField_UTMI_CKTRIM_FREQ = utmiReg_UTMI_CKTRIM.getBitfield("FREQ")
	
	# get value group for FREQ bitfield of UTMI_CKTRIM register
	utmiValGrp_UTMI_CKTRIM_FREQ = utmiRegModule.getValueGroup(utmiBitField_UTMI_CKTRIM_FREQ.getValueGroupName()) 
	
	# create symbol for FREQ bitfield of UTMI_CKTRIM register
	clkSym_UTMI_CKTRIM_FREQ = clkComponent.createComboSymbol("UTMI_CKTRIM_FREQ", clkSym_CKGR_UCKR_UPLLEN, utmiValGrp_UTMI_CKTRIM_FREQ.getValueNames())
	clkSym_UTMI_CKTRIM_FREQ.setDefaultValue("XTAL12")
	clkSym_UTMI_CKTRIM_FREQ.setVisible(False)

	# get PMC_MCKR register
	pmcReg_PMC_MCKR = pmcRegGroup.getRegister("PMC_MCKR")
	
	# get UPLLDIV2 Bitfield of PMC_MCKR register
	pmcBitField_PMC_MCKR_UPLLDIV2 = pmcReg_PMC_MCKR.getBitfield("UPLLDIV2")
	
	# create symbol for UPLLDIV2 Bitfield of PMC_MCKR register
	clkSym_PMC_MCKR_UPLLDIV2 = clkComponent.createBooleanSymbol("PMC_MCKR_UPLLDIV2", clkSym_CKGR_UCKR_UPLLEN)
	clkSym_PMC_MCKR_UPLLDIV2.setLabel(pmcBitField_PMC_MCKR_UPLLDIV2.getDescription())
	clkSym_PMC_MCKR_UPLLDIV2.setDefaultValue(False)
	clkSym_PMC_MCKR_UPLLDIV2.setVisible(False)
	clkSym_PMC_MCKR_UPLLDIV2.setDependencies(setUSBDividerVisibleProperty, ["PMC_CKGR_UCKR_UPLLEN"])

	# get PMC_SCER register
	pmcReg_PMC_SCER = pmcRegGroup.getRegister("PMC_SCER")
	
	# get USBCLK bitfield of PMC_SCER register
	pmcBitField_PMC_SCER_USBCLK = pmcReg_PMC_SCER.getBitfield("USBCLK")
	
	# get symbol for USBCLK bitfield of PMC_SCER register
	clkPMC_SCER_USBCLK = clkComponent.createBooleanSymbol("PMC_SCER_USBCLK", clkSymMenu)
	clkPMC_SCER_USBCLK.setLabel(pmcBitField_PMC_SCER_USBCLK.getDescription())

	# get PMC_USB register
	pmcReg_PMC_USB = pmcRegGroup.getRegister("PMC_USB")
	
	# get USBS bitfield of PMC_USB register
	pmcBitField_PMC_USB_USBS = pmcReg_PMC_USB.getBitfield("USBS")
	
	# get value group for USBS bitfield of PMC_USB register
	pmcValGrp_PMC_USB_USBS = pmcRegModule.getValueGroup(pmcBitField_PMC_USB_USBS.getValueGroupName())

	# create symbol for USBS bitfield of PMC_USB register
	#clkSym_PMC_USB_USBS = clkComponent.createComboSymbol("PMC_USB_USBS", clkSymMenu, pmcValGrp_PMC_USB_USBS.getValueNames())
	clkSym_PMC_USB_USBS = clkComponent.createComboSymbol("PMC_USB_USBS", clkPMC_SCER_USBCLK,["PLLA_CLK", "UPLL_CLK"])
	clkSym_PMC_USB_USBS.setLabel(pmcBitField_PMC_USB_USBS.getDescription())
	clkSym_PMC_USB_USBS.setDefaultValue("UPLL_CLK")

	# get USBDIV bitfield of PMC_USB register
	pmcBitField_PMC_USB_USBDIV = pmcReg_PMC_USB.getBitfield("USBDIV")
	
	# create symbol for USBDIV bitfield of PMC_USB register
	clkUSBDivider = clkComponent.createIntegerSymbol("PMC_USB_USBDIV", clkPMC_SCER_USBCLK)
	clkUSBDivider.setLabel(pmcBitField_PMC_USB_USBDIV.getDescription())
	clkUSBDivider.setMin(1)
	clkUSBDivider.setMax(16)
	clkUSBDivider.setDefaultValue(10)
	clkUSBDivider.setReadOnly(True)
	
def genericClk(clkComponent, clkSymMenu, pmcRegModule, setGenericClkDivVisible, setGenericClkSrcVisible):

	# create symbol for generic clock
	clkSymMenu = clkComponent.createMenuSymbol("CLK_GENERIC", clkSymMenu)
	clkSymMenu.setLabel("Peripheral/Generic Clock Generator Configuration for I2S0/1")
	
	# get PMC register group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")
	
	# get PMC_PCR register
	pmcReg_PMC_PCR = pmcRegGroup.getRegister("PMC_PCR")
	
	for i in range(0, 2, 1):
	
		# create menu for Peripheral/Generic Clock for I2S0/1
		clkSymI2SMenu = clkComponent.createMenuSymbol("CLK_I2S" + str(i), clkSymMenu)
		clkSymI2SMenu.setLabel("Peripheral/Generic Clock for I2S" + str(i))
		
		# create menu for Peripheral Clock for I2S0/1
		clkSymI2SPeripheralMenu = clkComponent.createMenuSymbol("CLK_I2S" + str(i) + "PERIPHERAL", clkSymI2SMenu)
		clkSymI2SPeripheralMenu.setLabel( "I2S" + str(i) +" Peripheral Clock")
		
		# get EN bitfield of PMC_PCR Register
		pmcBitField_PMC_PCR = pmcReg_PMC_PCR.getBitfield("EN")
		
		# create symbol for EN bitfield of PMC_PCR Register
		clkSym_PMC_PCR_EN = clkComponent.createBooleanSymbol("PMC_PCR_EN" + str(i), clkSymI2SPeripheralMenu)
		clkSym_PMC_PCR_EN.setLabel(pmcBitField_PMC_PCR.getDescription())
		clkSym_PMC_PCR_EN.setDefaultValue(False)
	
		# create menu for Generic clock for I2S0/1
		clkSymGenericMenu = clkComponent.createMenuSymbol("CLK_I2S" + str(i) + "GENERIC", clkSymI2SMenu)
		clkSymGenericMenu.setLabel("I2S" + str(i) + "Generic Clock")
		
		# get GCLKEN bitfield of PMC_PCR register
		pmcBitField_PMC_PCR_GCLKEN = pmcReg_PMC_PCR.getBitfield("GCLKEN")
		
		# create symbol for GCLKEN bitfield of PMC_PCR register
		clkSym_PMC_PCR_GCLKEN = clkComponent.createBooleanSymbol("PMC_PCR_GCLK" + str(i) + "EN", clkSymGenericMenu)
		clkSym_PMC_PCR_GCLKEN.setLabel(pmcBitField_PMC_PCR_GCLKEN.getDescription())
		
		# get GCLKDIV bitfield of PMC_PCR register
		pmcBitField_PMC_PCR_GCLKDIV = pmcReg_PMC_PCR.getBitfield("GCLKDIV")
		
		# create symbol for GCLKDIV bitfield of PMC_PCR register
		clkSym_PMC_PCR_GCLKDIV = clkComponent.createIntegerSymbol("PMC_PCR_GCLK" + str(i) + "DIV", clkSymGenericMenu)
		clkSym_PMC_PCR_GCLKDIV.setLabel(pmcBitField_PMC_PCR_GCLKDIV.getDescription())
		clkSym_PMC_PCR_GCLKDIV.setMin(1)
		clkSym_PMC_PCR_GCLKDIV.setMax(256)
		clkSym_PMC_PCR_GCLKDIV.setDefaultValue(1)
		clkSym_PMC_PCR_GCLKDIV.setVisible(False)
		clkSym_PMC_PCR_GCLKDIV.setDependencies(setGenericClkDivVisible, ["PMC_PCR_GCLK" + str(i) + "EN"])
		
		# get GCLKCSS bitfield of PMC_PCR register
		pmcBitField_PMC_PCR_GCLKCSS = pmcReg_PMC_PCR.getBitfield("GCLKCSS")
		
		# get Value Group for GCLKCSS bitfield of PMC_PCR register
		pmcValGrp_PMC_PCR_GCLKCSS = pmcRegModule.getValueGroup(pmcBitField_PMC_PCR_GCLKCSS.getValueGroupName())
		
		# create symbol for GCLKCSS bitfield of PMC_PCR register
		clkSym_PMC_PCR_GCLKCSS = clkComponent.createComboSymbol("PMC_PCR_GCLK" + str(i) + "CSS", clkSymGenericMenu, pmcValGrp_PMC_PCR_GCLKCSS.getValueNames())
		clkSym_PMC_PCR_GCLKCSS.setLabel(pmcBitField_PMC_PCR_GCLKCSS.getDescription())
		clkSym_PMC_PCR_GCLKCSS.setDefaultValue("SLOW_CLK")
		clkSym_PMC_PCR_GCLKCSS.setVisible(False)
		clkSym_PMC_PCR_GCLKCSS.setDependencies(setGenericClkSrcVisible, ["PMC_PCR_GCLK" + str(i) + "EN"])

def peripheralClk(clkComponent, clkSymMenu, join, ElementTree):

	# create symbol for peripheral clock
	clkSymMenu = clkComponent.createMenuSymbol("CLK_PERIPHERAL", clkSymMenu)
	clkSymMenu.setLabel("Peripheral Clock Enable Configuration")
	
	atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
	
	try:
		atdfFile = open(atdfFilePath, "r")
	except:
		print("clk.py peripheral clock: Error!!! while opening atdf file")
		
	atdfContent = ElementTree.fromstring(atdfFile.read())
	
	# parse atdf xml file to get instance name 
	# for the peripheral which has clock id
	for peripheral in atdfContent.iter("module"):
		for instance in peripheral.iter("instance"):
			for param in instance.iter("param"):
				if "CLOCK_ID" in param.attrib["name"]:
					symbolId = "PMC_ID_" + instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1]
					clkSymPeripheral = clkComponent.createBooleanSymbol(symbolId, clkSymMenu)
					clkSymPeripheral.setLabel(instance.attrib["name"] + param.attrib["name"].split("CLOCK_ID")[1])
					clkSymPeripheral.setDefaultValue(False)
					clkSymPeripheral.setReadOnly(True)
	
	# create symbol for PMC_PCERx register values
	clkSym_PMC_PCER0 = clkComponent.createStringSymbol("PMC_PCER0", clkSymMenu)
	clkSym_PMC_PCER0.setVisible(False)
	clkSym_PMC_PCER0.setDefaultValue("0x00000000")
	
	# create symbol for PMC_PCERx register values
	clkSym_PMC_PCER1 = clkComponent.createStringSymbol("PMC_PCER1", clkSymMenu)
	clkSym_PMC_PCER1.setVisible(False)
	clkSym_PMC_PCER1.setDefaultValue("0x00000000")

#Programmable Clock generator configuration options
def programmableClock(clkComponent, clkSymMenu, pmcRegModule):

	# create symbol for Programmable clock menu
	clkSymMenu = clkComponent.createMenuSymbol("CLK_PROGRAMMABLE", clkSymMenu)
	clkSymMenu.setLabel("Programmable Clock Generator Configuration")

	# get PMC register group
	pmcRegGroup = pmcRegModule.getRegisterGroup("PMC")
	
	# get PMC_SCER register 
	pmcReg_PMC_SCER = pmcRegGroup.getRegister("PMC_SCER")
	
	# get PMC_PCK# register
	pmcReg_PMC_PCK = pmcRegGroup.getRegister("PMC_PCK")
	
	# menu for 8 programmable clock
	for i in range(0, 8, 1):
	
		# create symbol for programmable clock #
		clkSymProgrammableMenu = clkComponent.createMenuSymbol("CLK_PROGRAMMABLE_" + str(i), clkSymMenu)
		clkSymProgrammableMenu.setLabel("Programmable Clock " + str(i) + " Generator Configuration")
		
		# get PCK# bitfield of PMC_SCER Register
		pmcBitField_PMC_SCER_PCK = pmcReg_PMC_SCER.getBitfield("PCK" + str(i))
		
		# create symbol for PCK# bitfield of PMC_SCER Register
		clkSym_PMC_SCER_PCK = clkComponent.createBooleanSymbol("PMC_SCER_PCK" + str(i), clkSymProgrammableMenu)
		clkSym_PMC_SCER_PCK.setLabel(pmcBitField_PMC_SCER_PCK.getDescription())
		
		# get CSS bitfield of PMC_PCK# register
		pmcBitField_PMC_PCK_CSS = pmcReg_PMC_PCK.getBitfield("CSS")
		
		# get Value Group for CSS bitfield of PMC_PCK# register
		pmcValGrp_PMC_PCK_CSS = pmcRegModule.getValueGroup(pmcBitField_PMC_PCK_CSS.getValueGroupName())
		
		# create symbol for CSS bitfield of PMC_PCK# register 
		clkSym_PMC_PCK_CSS = clkComponent.createComboSymbol("PMC_PCK" + str(i) + "_CSS", clkSym_PMC_SCER_PCK, pmcValGrp_PMC_PCK_CSS.getValueNames())
		clkSym_PMC_PCK_CSS.setLabel(pmcBitField_PMC_PCK_CSS.getDescription())
		clkSym_PMC_PCK_CSS.setDefaultValue("SLOW_CLK")

		# get PRES bitfield of PMC_PCK# register
		pmcBitField_PMC_PCK_PRES = pmcReg_PMC_PCK.getBitfield("PRES")
		
		# create symbol for PRES bitfield of PMC_PCK# register
		clkSym_PMC_PCK_PRES = clkComponent.createIntegerSymbol("PMC_PCK" + str(i) +"_PRES", clkSym_PMC_SCER_PCK)
		clkSym_PMC_PCK_PRES.setLabel(pmcBitField_PMC_PCK_PRES.getDescription())
		clkSym_PMC_PCK_PRES.setMin(1)
		clkSym_PMC_PCK_PRES.setMax(256)
		clkSym_PMC_PCK_PRES.setDefaultValue(1)

def calculatedClockFrequencies(clkComponent, clkSymMenu, updateFWSValue, join, ElementTree):

	global fwsMaxFreqList

	#Calculated Clock Frequencies
	calculatedFrequencies = clkComponent.createMenuSymbol("calculatedFrequencies", clkSymMenu)
	calculatedFrequencies.setLabel("Calculated Clock Frequencies")

	systemTickFreq = clkComponent.createStringSymbol("SYSTICK", calculatedFrequencies)
	systemTickFreq.setLabel("System Tick Frequency (HZ)")
	systemTickFreq.setDefaultValue("37500000")
	systemTickFreq.setReadOnly(True)

	processorClkFreq = clkComponent.createStringSymbol("PROCESSORCLK_FREQ", calculatedFrequencies)
	processorClkFreq.setLabel("Processor Clock Frequency (HZ)")
	processorClkFreq.setDefaultValue("300000000")
	processorClkFreq.setReadOnly(True)

	masterClkFreq = clkComponent.createStringSymbol("MASTERCLK_FREQ", calculatedFrequencies)
	masterClkFreq.setLabel("Master Clock Frequency (HZ)")
	masterClkFreq.setDefaultValue("150000000")
	masterClkFreq.setReadOnly(True)

	i2s0Freq = clkComponent.createStringSymbol("I2S0_FREQ", calculatedFrequencies)
	i2s0Freq.setLabel("I2S0 Frequency (HZ)")
	i2s0Freq.setDefaultValue("75000000")
	i2s0Freq.setReadOnly(True)

	i2s1Freq = clkComponent.createStringSymbol("I2S1_FREQ", calculatedFrequencies)
	i2s1Freq.setLabel("I2S1 Frequency (HZ)")
	i2s1Freq.setDefaultValue("100000000")
	i2s1Freq.setReadOnly(True)

	pck0Freq = clkComponent.createStringSymbol("PCK0_FREQ", calculatedFrequencies)
	pck0Freq.setLabel("Programmable clock #0 Frequency (HZ)")
	pck0Freq.setDefaultValue("12000000")
	pck0Freq.setReadOnly(True)

	pck1Freq = clkComponent.createStringSymbol("PCK1_FREQ", calculatedFrequencies)
	pck1Freq.setLabel("Programmable clock #1 Frequency (HZ)")
	pck1Freq.setDefaultValue("6000000")
	pck1Freq.setReadOnly(True)

	pck2Freq = clkComponent.createStringSymbol("PCK2_FREQ", calculatedFrequencies)
	pck2Freq.setLabel("Programmable clock #2 Frequency (HZ)")
	pck2Freq.setDefaultValue("4000000")
	pck2Freq.setReadOnly(True)

	pck3Freq = clkComponent.createStringSymbol("PCK3_FREQ", calculatedFrequencies)
	pck3Freq.setLabel("Programmable clock #3 Frequency (HZ)")
	pck3Freq.setDefaultValue("3000000")
	pck3Freq.setReadOnly(True)

	pck4Freq = clkComponent.createStringSymbol("PCK4_FREQ", calculatedFrequencies)
	pck4Freq.setLabel("Programmable clock #4 Frequency (HZ)")
	pck4Freq.setDefaultValue("2400000")
	pck4Freq.setReadOnly(True)

	pck5Freq = clkComponent.createStringSymbol("PCK5_FREQ", calculatedFrequencies)
	pck5Freq.setLabel("Programmable clock #5 Frequency (HZ)")
	pck5Freq.setDefaultValue("2000000")
	pck5Freq.setReadOnly(True)

	pck6Freq = clkComponent.createStringSymbol("PCK6_FREQ", calculatedFrequencies)
	pck6Freq.setLabel("Programmable clock #6 Frequency (HZ)")
	pck6Freq.setDefaultValue("1714285")
	pck6Freq.setReadOnly(True)

	pck7Freq = clkComponent.createStringSymbol("PCK7_FREQ", calculatedFrequencies)
	pck7Freq.setLabel("Programmable clock #7 Frequency (HZ)")
	pck7Freq.setDefaultValue("1500000")
	pck7Freq.setReadOnly(True)

	usbFsFreq = clkComponent.createStringSymbol("USBFS_FREQ", calculatedFrequencies)
	usbFsFreq.setLabel("USB Clock Frequency (HZ)")
	usbFsFreq.setDefaultValue("48000000")
	usbFsFreq.setReadOnly(True)

	usbHsFreq = clkComponent.createStringSymbol("USBHS_FREQ", calculatedFrequencies)
	usbHsFreq.setLabel("USB High Speed Clock Frequency (HZ)")
	usbHsFreq.setDefaultValue("480000000")
	usbHsFreq.setReadOnly(True)
	
	clkSymFlashWaitStates = clkComponent.createStringSymbol("EEFC_FMR_FWS", calculatedFrequencies)
	clkSymFlashWaitStates.setDependencies(updateFWSValue, ["MASTERCLK_FREQ"])
	
	atdfFilePath = join(Variables.get("__DFP_PACK_DIR") ,"atdf", Variables.get("__PROCESSOR") + ".atdf")
	
	fwsMaxFreqList = []
	
	try:
		atdfFile = open(atdfFilePath, "r")
	except:
		print("clk.py peripheral clock: Error!!! while opening atdf file")
		
	atdfContent = ElementTree.fromstring(atdfFile.read())
	
	# parse atdf xml file to get Electrical Characteristics 
	# for Flash wait states
	for propertyGroup in atdfContent.iter("property-group"):
		if "ELECTRICAL_CHARACTERISTICS" in propertyGroup.attrib["name"]:
			for property in propertyGroup.iter("property"):
				if "CHIP_FREQ_FWS_" in property.attrib["name"] and "CHIP_FREQ_FWS_NUMBER" != property.attrib["name"]:
					fwsMaxFreqList.append(property.attrib["value"])
	
	minFreq = maxFreq = 0
	for fws in range(0, len(fwsMaxFreqList), 1):
		
		mckFreq = int(masterClkFreq.getValue())
		maxFreq = int(fwsMaxFreqList[fws])
		
		if mckFreq <= maxFreq and mckFreq > minFreq:
			clkSymFlashWaitStates.setValue("EEFC_FMR_FWS", str(fws), 1)
			return
			
		minFreq = maxFreq

# Clock Manager Configuration Menu
print("Loading Clock Manager for " + Variables.get("__PROCESSOR"))

clkSymMenu = coreComponent.createMenuSymbol(None, None)
clkSymMenu.setLabel("Clock (PMC)")
clkSymMenu.setDescription("Configuration for Clock System Service")

clkSymManagerSelect = coreComponent.createStringSymbol("CLK_MANAGER_PLUGIN", clkSymMenu)
clkSymManagerSelect.setVisible(False)
clkSymManagerSelect.setDefaultValue("SAME70:SAME70ClockModel")

clkSymMenuComment = coreComponent.createCommentSymbol("clkSettingsComment", clkSymMenu)
clkSymMenuComment.setLabel("**** All settings listed here can be configured using the Clock Configurator ****")

pmcRegModule  = Register.getRegisterModule("PMC")
supcRegModule = Register.getRegisterModule("SUPC")
utmiRegModule = Register.getRegisterModule("UTMI")

# Create slow clock menu
slowClock(coreComponent, clkSymMenu, supcRegModule, resetReadOnlySlowClkFreq)

# create main clock menu
mainClock(coreComponent, clkSymMenu, pmcRegModule, updateExtXtalEnable)

# create plla menu
pllA(coreComponent, clkSymMenu, pmcRegModule, setDividerVisibleProperty, setMultiplierVisibleProperty)

# master clock
masterClock(coreComponent, clkSymMenu, pmcRegModule)

# usb clock
usbClock(coreComponent, clkSymMenu, pmcRegModule, utmiRegModule, setUSBDividerVisibleProperty)

# generic clock
genericClk(coreComponent, clkSymMenu, pmcRegModule, setGenericClkDivVisible, setGenericClkSrcVisible)

# peripheral clock
peripheralClk(coreComponent, clkSymMenu, join, ElementTree)

# programmable clock
programmableClock(coreComponent, clkSymMenu, pmcRegModule)

# calculated Frequencies
calculatedClockFrequencies(coreComponent, clkSymMenu, updateFWSValue, join, ElementTree)

#File handling
configName = Variables.get("__CONFIGURATION_NAME")

clkHeaderFile = coreComponent.createFileSymbol(None, None)
clkHeaderFile.setSourcePath("../peripheral/clk_sam_e70/templates/clk.h.ftl")
clkHeaderFile.setOutputName("clk.h")
clkHeaderFile.setDestPath("/peripheral/clk/")
clkHeaderFile.setProjectPath("config/" + configName + "/peripheral/clk/")
clkHeaderFile.setType("HEADER")
clkHeaderFile.setMarkup(True)

clkSourceFile = coreComponent.createFileSymbol(None, None)
clkSourceFile.setSourcePath("../peripheral/clk_sam_e70/templates/clk.c.ftl")
clkSourceFile.setOutputName("clk.c")
clkSourceFile.setDestPath("/peripheral/clk/")
clkSourceFile.setProjectPath("config/" + configName + "/peripheral/clk/")
clkSourceFile.setType("SOURCE")
clkSourceFile.setMarkup(True)

#Add clock related code to common files
clkHeaderFileListEntry = coreComponent.createListEntrySymbol(None, None)
clkHeaderFileListEntry.setTarget("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
clkHeaderFileListEntry.addValue("#include \"peripheral/clk/clk.h\"")


clkSystemInitFile = coreComponent.createFileSymbol(None, None)
clkSystemInitFile.setType("STRING")
clkSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
clkSystemInitFile.setSourcePath("../peripheral/clk_sam_e70/templates/clk_system_init.c.ftl")
clkSystemInitFile.setMarkup(True)


