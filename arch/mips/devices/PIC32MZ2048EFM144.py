def instantiateComponent(coreComponent):
	frameworkMenu = coreComponent.createMenuSymbol(None, None)
	frameworkMenu.setLabel("Framework Configuration Values")
	frameworkMenu.setDescription("General Framework Configuration Values")

	DEVICE_FAMILY = coreComponent.createStringSymbol("DEVICE_FAMILY", frameworkMenu)
	DEVICE_FAMILY.setLabel("Device Family")
	DEVICE_FAMILY.setDefaultValue("PIC32MX")
	DEVICE_FAMILY.setReadOnly(True)
	DEVICE_FAMILY.setDescription("The name of the device family that is currently selected.")
	
	DATASHEET_ID = coreComponent.createStringSymbol("DATASHEET_ID", frameworkMenu)
	DATASHEET_ID.setLabel("Datasheet ID")
	DATASHEET_ID.setDefaultValue(Variables.get("__DATASHEET_NAME"))
	DATASHEET_ID.setReadOnly(True)
	DATASHEET_ID.setDescription("The name of the datasheet that the currently selected processor belongs to.")
	
	PROCESSOR_NAME = coreComponent.createStringSymbol("PROCESSOR_NAME", frameworkMenu)
	PROCESSOR_NAME.setLabel("Processor Name")
	PROCESSOR_NAME.setDefaultValue(Variables.get("__PROCESSOR"))
	PROCESSOR_NAME.setReadOnly(True)
	PROCESSOR_NAME.setDescription("The name of the currently selected processor.")

	HAVE_ADC = coreComponent.createBooleanSymbol("HAVE_ADC", frameworkMenu)
	#HAVE_ADC.setReadOnly(True)
	HAVE_ADC.setDescription("short description defined in python")

	HAVE_ADC_ESCAN = coreComponent.createBooleanSymbol("HAVE_ADC_ESCAN", frameworkMenu)
	HAVE_ADC_ESCAN.setReadOnly(True)
	HAVE_ADC_ESCAN.setDescription("short description defined in python")

	HAVE_ADCP = coreComponent.createBooleanSymbol("HAVE_ADCP", frameworkMenu)
	HAVE_ADCP.setReadOnly(True)

	HAVE_ADCHS = coreComponent.createBooleanSymbol("HAVE_ADCHS", frameworkMenu)
	HAVE_ADCHS.setReadOnly(True)

	HAVE_AFEC = coreComponent.createBooleanSymbol("HAVE_AFEC", frameworkMenu)
	HAVE_AFEC.setReadOnly(True)

	HAVE_APPIO = coreComponent.createBooleanSymbol("HAVE_APPIO", frameworkMenu)
	HAVE_APPIO.setReadOnly(True)

	HAVE_BMX = coreComponent.createBooleanSymbol("HAVE_BMX", frameworkMenu)
	HAVE_BMX.setReadOnly(True)

	HAVE_CAN = coreComponent.createBooleanSymbol("HAVE_CAN", frameworkMenu)
	HAVE_CAN.setReadOnly(True)

	HAVE_CDAC = coreComponent.createBooleanSymbol("HAVE_CDAC", frameworkMenu)
	HAVE_CDAC.setReadOnly(True)

	HAVE_CLK = coreComponent.createBooleanSymbol("HAVE_CLK", frameworkMenu)
	HAVE_CLK.setReadOnly(True)

	HAVE_CMP = coreComponent.createBooleanSymbol("HAVE_CMP", frameworkMenu)
	HAVE_CMP.setReadOnly(True)

	HAVE_CTMU = coreComponent.createBooleanSymbol("HAVE_CTMU", frameworkMenu)
	HAVE_CTMU.setReadOnly(True)

	HAVE_CTR = coreComponent.createBooleanSymbol("HAVE_CTR", frameworkMenu)
	HAVE_CTR.setReadOnly(True)

	HAVE_DAC = coreComponent.createBooleanSymbol("HAVE_DAC", frameworkMenu)
	HAVE_DAC.setReadOnly(True)

	HAVE_DEVCON = coreComponent.createBooleanSymbol("HAVE_DEVCON", frameworkMenu)
	HAVE_DEVCON.setReadOnly(True)

	HAVE_DMA = coreComponent.createBooleanSymbol("HAVE_DMA", frameworkMenu)
	HAVE_DMA.setReadOnly(True)

	HAVE_DDR = coreComponent.createBooleanSymbol("HAVE_DDR", frameworkMenu)
	HAVE_DDR.setReadOnly(True)

	HAVE_DMT = coreComponent.createBooleanSymbol("HAVE_DMT", frameworkMenu)
	HAVE_DMT.setReadOnly(True)

	HAVE_EBI = coreComponent.createBooleanSymbol("HAVE_EBI", frameworkMenu)
	HAVE_EBI.setReadOnly(True)

	HAVE_EEPROM = coreComponent.createBooleanSymbol("HAVE_EEPROM", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001402":
		HAVE_EEPROM.setDefaultValue(True)
	
	HAVE_EEPROM.setReadOnly(True)

	HAVE_FPU = coreComponent.createBooleanSymbol("HAVE_FPU", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001320" or Variables.get("__DATASHEET_ID") == "DS60001402":
		HAVE_FPU.setDefaultValue(True)
	
	HAVE_FPU.setDefaultValue(True)
	HAVE_FPU.setReadOnly(True)

	HAVE_ETH = coreComponent.createBooleanSymbol("HAVE_ETH", frameworkMenu)
	HAVE_ETH.setReadOnly(True)

	HAVE_NANO2D = coreComponent.createBooleanSymbol("HAVE_NANO2D", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001361":
		HAVE_NANO2D.setDefaultValue(True)
		
	HAVE_NANO2D.setDefaultValue(True)
	HAVE_NANO2D.setReadOnly(True)

	HAVE_GLCD = coreComponent.createBooleanSymbol("HAVE_GLCD", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001361":
		HAVE_GLCD.setDefaultValue(True)
		
	HAVE_GLCD.setReadOnly(True)

	HAVE_I2C = coreComponent.createBooleanSymbol("HAVE_I2C", frameworkMenu)
	HAVE_I2C.setReadOnly(True)

	HAVE_IC = coreComponent.createBooleanSymbol("HAVE_IC", frameworkMenu)
	HAVE_IC.setReadOnly(True)

	HAVE_INT = coreComponent.createBooleanSymbol("HAVE_INT", frameworkMenu)
	HAVE_INT.setReadOnly(True)

	HAVE_JTAG = coreComponent.createBooleanSymbol("HAVE_JTAG", frameworkMenu)
	HAVE_JTAG.setReadOnly(True)

	HAVE_SWD = coreComponent.createBooleanSymbol("HAVE_SWD", frameworkMenu)
	HAVE_SWD.setReadOnly(True)

	HAVE_MPLL = coreComponent.createBooleanSymbol("HAVE_MPLL", frameworkMenu)
	HAVE_MPLL.setReadOnly(True)

	HAVE_NVM = coreComponent.createBooleanSymbol("HAVE_NVM", frameworkMenu)
	HAVE_NVM.setReadOnly(True)

	HAVE_OC = coreComponent.createBooleanSymbol("HAVE_OC", frameworkMenu)
	HAVE_OC.setReadOnly(True)

	HAVE_OSC = coreComponent.createBooleanSymbol("HAVE_OSC", frameworkMenu)
	HAVE_OSC.setReadOnly(True)

	HAVE_PCACHE = coreComponent.createBooleanSymbol("HAVE_PCACHE", frameworkMenu)
	HAVE_PCACHE.setReadOnly(True)

	HAVE_PMP = coreComponent.createBooleanSymbol("HAVE_PMP", frameworkMenu)
	HAVE_PMP.setReadOnly(True)

	HAVE_PORTS = coreComponent.createBooleanSymbol("HAVE_PORTS", frameworkMenu)
	HAVE_PORTS.setReadOnly(True)

	HAVE_PPS = coreComponent.createBooleanSymbol("HAVE_PPS", frameworkMenu)
	HAVE_PPS.setDefaultValue(True)
	HAVE_PPS.setReadOnly(True)

	HAVE_POWER = coreComponent.createBooleanSymbol("HAVE_POWER", frameworkMenu)
	HAVE_POWER.setReadOnly(True)

	HAVE_PTG = coreComponent.createBooleanSymbol("HAVE_PTG", frameworkMenu)
	HAVE_PTG.setReadOnly(True)

	HAVE_REFCLOCK = coreComponent.createBooleanSymbol("HAVE_REFCLOCK", frameworkMenu)
	HAVE_REFCLOCK.setDefaultValue(True)
	HAVE_REFCLOCK.setReadOnly(True)

	HAVE_REFCLOCK5 = coreComponent.createBooleanSymbol("HAVE_REFCLOCK5", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001361":
		HAVE_REFCLOCK5.setDefaultValue(True)
	
	HAVE_REFCLOCK5.setReadOnly(True)

	HAVE_LVD = coreComponent.createBooleanSymbol("HAVE_LVD", frameworkMenu)
	
	if Variables.get("__DATASHEET_ID") == "DS60001361":
		HAVE_LVD.setDefaultValue(True)
	
	HAVE_LVD.setReadOnly(True)

	HAVE_QEI = coreComponent.createBooleanSymbol("HAVE_QEI", frameworkMenu)
	HAVE_QEI.setReadOnly(True)

	HAVE_RESET = coreComponent.createBooleanSymbol("HAVE_RESET", frameworkMenu)
	HAVE_RESET.setReadOnly(True)

	HAVE_RTCC = coreComponent.createBooleanSymbol("HAVE_RTCC", frameworkMenu)
	HAVE_RTCC.setReadOnly(True)

	HAVE_RTCC_WITH_CLOCKSELECT = coreComponent.createBooleanSymbol("HAVE_RTCC_WITH_CLOCKSELECT", frameworkMenu)
	
	if Variables.get("__DEVICE_FAMILY") == "PIC32MX" or Variables.get("__DATASHEET_ID") == "DS60001404":
		HAVE_RTCC_WITH_CLOCKSELECT.setDefaultValue(True)
	
	HAVE_RTCC_WITH_CLOCKSELECT.setDefaultValue(True)
	HAVE_RTCC_WITH_CLOCKSELECT.setReadOnly(True)

	HAVE_TRACE = coreComponent.createBooleanSymbol("HAVE_TRACE", frameworkMenu)
	HAVE_TRACE.setReadOnly(True)

	HAVE_SDHC = coreComponent.createBooleanSymbol("HAVE_SDHC", frameworkMenu)
	HAVE_SDHC.setReadOnly(True)
	
	if Variables.get("__DATASHEET_ID") == "DS60001361":
		HAVE_SDHC.setDefaultValue(True)

	HAVE_SB = coreComponent.createBooleanSymbol("HAVE_SB", frameworkMenu)
	HAVE_SB.setReadOnly(True)

	HAVE_SPI = coreComponent.createBooleanSymbol("HAVE_SPI", frameworkMenu)
	HAVE_SPI.setReadOnly(True)

	HAVE_SQI = coreComponent.createBooleanSymbol("HAVE_SQI", frameworkMenu)
	HAVE_SQI.setReadOnly(True)

	HAVE_TMR = coreComponent.createBooleanSymbol("HAVE_TMR", frameworkMenu)
	HAVE_TMR.setReadOnly(True)

	HAVE_USART = coreComponent.createBooleanSymbol("HAVE_USART", frameworkMenu)
	HAVE_USART.setReadOnly(True)

	HAVE_USB = coreComponent.createBooleanSymbol("HAVE_USB", frameworkMenu)
	HAVE_USB.setReadOnly(True)

	HAVE_USBHS = coreComponent.createBooleanSymbol("HAVE_USBHS", frameworkMenu)
	HAVE_USBHS.setReadOnly(True)

	HAVE_WDT = coreComponent.createBooleanSymbol("HAVE_WDT", frameworkMenu)
	HAVE_WDT.setReadOnly(True)

	HAVE_RSWDT = coreComponent.createBooleanSymbol("HAVE_RSWDT", frameworkMenu)
	HAVE_RSWDT.setReadOnly(True)

	HAVE_WIFI = coreComponent.createBooleanSymbol("HAVE_WIFI", frameworkMenu)
	HAVE_WIFI.setReadOnly(True)

	HAVE_MCPWM = coreComponent.createBooleanSymbol("HAVE_MCPWM", frameworkMenu)
	HAVE_MCPWM.setReadOnly(True)

	HAVE_SMC = coreComponent.createBooleanSymbol("HAVE_SMC", frameworkMenu)
	HAVE_SMC.setReadOnly(True)

	HAVE_SDRAMC = coreComponent.createBooleanSymbol("HAVE_SDRAMC", frameworkMenu)
	HAVE_SDRAMC.setReadOnly(True)

	CRYPTO = coreComponent.createBooleanSymbol("CRYPTO", frameworkMenu)
	CRYPTO.setReadOnly(True)

	ENHANCED_BUFFER_MODE_SUPPORT = coreComponent.createBooleanSymbol("ENHANCED_BUFFER_MODE_SUPPORT", frameworkMenu)
	ENHANCED_BUFFER_MODE_SUPPORT.setReadOnly(True)

	AUDIO_CODEC_SUPPORT = coreComponent.createBooleanSymbol("AUDIO_CODEC_SUPPORT", frameworkMenu)
	AUDIO_CODEC_SUPPORT.setReadOnly(True)

	HAVE_DECODER_SUPPORT = coreComponent.createBooleanSymbol("HAVE_DECODER_SUPPORT", frameworkMenu)
	HAVE_DECODER_SUPPORT.setReadOnly(True)

	PMP_DUAL_MODE = coreComponent.createBooleanSymbol("PMP_DUAL_MODE", frameworkMenu)
	PMP_DUAL_MODE.setReadOnly(True)

	HAVE_I2S = coreComponent.createBooleanSymbol("HAVE_I2S", frameworkMenu)
	HAVE_I2S.setDefaultValue(True)
	HAVE_I2S.setReadOnly(True)

	# exec part specific script
	execfile(Module.getPath() + Variables.get("__PROCESSOR") + ".py")
	
	COMP_INCLUDE_C = coreComponent.createCompilerIncludeSymbol(None, None)
	COMP_INCLUDE_C.setType("C")
	COMP_INCLUDE_C.setPath(Variables.get("__PROJECT_SRC_PATH"))
	
	COMP_INCLUDE_CPP = coreComponent.createCompilerIncludeSymbol(None, None)
	COMP_INCLUDE_CPP.setType("CPP")
	COMP_INCLUDE_CPP.setPath(Variables.get("__PROJECT_SRC_PATH"))
	
	COMP_INCLUDE_ASM = coreComponent.createCompilerIncludeSymbol(None, None)
	COMP_INCLUDE_ASM.setType("ASM")
	COMP_INCLUDE_ASM.setPath(Variables.get("__PROJECT_SRC_PATH"))
	
	TEST_DEFINE_C = coreComponent.createCompilerDefineSymbol(None, None)
	TEST_DEFINE_C.setType("C")
	TEST_DEFINE_C.setValue("test_define_C")
	
	TEST_DEFINE_CPP = coreComponent.createCompilerDefineSymbol(None, None)
	TEST_DEFINE_CPP.setType("CPP")
	TEST_DEFINE_CPP.setValue("test_define_CPP")
	
	TEST_DEFINE_ASM = coreComponent.createCompilerDefineSymbol(None, None)
	TEST_DEFINE_ASM.setType("ASM")
	TEST_DEFINE_ASM.setValue("test_define_ASM")
	
	TEST_SOURCE_PATH = coreComponent.createSourcePathSymbol(None, None)
	TEST_SOURCE_PATH.setPath(Variables.get("__PROJECT_SRC_PATH"))
	
	HEAP_SETTING = coreComponent.createSettingSymbol(None, None)
	HEAP_SETTING.setPath("heap")
	HEAP_SETTING.setValue("512000")