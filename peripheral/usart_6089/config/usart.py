usartRegModule = Register.getRegisterModule("USART")
usartRegGroup = usartRegModule.getRegisterGroup("USART")

usartReg_MR = usartRegGroup.getRegister("US_MR")
usartBitField_MR_PAR = usartReg_MR.getBitfield("PAR")
usartValGrp_MR_PAR = usartRegModule.getValueGroup(usartBitField_MR_PAR.getValueGroupName())
usartBitField_MR_MODE9 = usartReg_MR.getBitfield("MODE9")
usartValGrp_MR_MODE9 = usartRegModule.getValueGroup(usartBitField_MR_MODE9.getValueGroupName())
usartBitField_MR_NBSTOP = usartReg_MR.getBitfield("NBSTOP")
usartValGrp_MR_NBSTOP = usartRegModule.getValueGroup(usartBitField_MR_NBSTOP.getValueGroupName())
usartBitField_MR_CHRL = usartReg_MR.getBitfield("CHRL")
usartValGrp_MR_CHRL = usartRegModule.getValueGroup(usartBitField_MR_CHRL.getValueGroupName())
usartBitField_MR_SYNC = usartReg_MR.getBitfield("SYNC")
usartValGrp_MR_SYNC = usartRegModule.getValueGroup(usartBitField_MR_NBSTOP.getValueGroupName())

global lBaudClock
lBaudClock = Database.getSymbolValue("PMC", "SYS_CLK_MASTERCLK_FREQ")
#Above API is not working, so hard coding MCLK value for now
lBaudClock = 150000000

def instantiateComponent(usartComponent):

	num = usartComponent.getID()[-1:]
	print("Running USART" + str(num))
	
	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("Hardware Settings")
	
	usartIndex = usartComponent.createIntegerSymbol("INDEX", usartMenu)
	usartIndex.setVisible(False)
	usartIndex.setDefaultValue(int(num))

	usartInterrupt = usartComponent.createBooleanSymbol("INTERRUPT_MODE", usartMenu)
	print(usartInterrupt)
	usartInterrupt.setLabel("Interrupt Mode")
	usartInterrupt.setDefaultValue(True)
	
	usartBaud = usartComponent.createIntegerSymbol("BAUD_RATE", usartMenu)
	print(usartBaud)
	usartBaud.setLabel("Baud Rate")
	#Default value is triggered by calculateBRGValue callback

	#Local symbol related to BaudRate
	usartSym_MR_OVER = usartComponent.createIntegerSymbol("USART_MR_OVER", usartMenu)
	print(usartSym_MR_OVER)
	usartSym_MR_OVER.setVisible(False)
	usartSym_MR_OVER.setDependencies(setOversampling, ["BAUD_RATE"])
	
	#Local symbol related to BaudRate
	usartBRGValue = usartComponent.createIntegerSymbol("BRG_VALUE", usartMenu)
	print(usartBRGValue)
	usartBRGValue.setVisible(False)
	usartBRGValue.setDependencies(calculateBRGValue, ["BAUD_RATE"])
	usartBaud.setDefaultValue(9600)
	
	usartSym_MR_MODE9 = usartComponent.createBooleanSymbol("USART_MR_MODE9", usartMenu)
	print(usartSym_MR_MODE9)
	usartSym_MR_MODE9.setLabel(usartBitField_MR_MODE9.getDescription())
	usartSym_MR_MODE9.setDefaultValue(False)
	
	usartSym_MR_PAR = usartComponent.createComboSymbol("USART_MR_PAR", usartMenu, usartValGrp_MR_PAR.getValueNames())
	print(usartSym_MR_PAR)
	usartSym_MR_PAR.setLabel(usartBitField_MR_PAR.getDescription())
	usartSym_MR_PAR.setDefaultValue("NO")
	
	usartSym_MR_NBSTOP = usartComponent.createComboSymbol("USART_MR_NBSTOP", usartMenu, usartValGrp_MR_NBSTOP.getValueNames())
	print(usartSym_MR_NBSTOP)
	usartSym_MR_NBSTOP.setLabel(usartBitField_MR_NBSTOP.getDescription())
	usartSym_MR_NBSTOP.setDefaultValue("_1_BIT")
	
	#Here for the future use, by default only 8 and 9 bit available for now.
	usartSym_MR_CHRL = usartComponent.createComboSymbol("USART_MR_CHRL", usartMenu, usartValGrp_MR_CHRL.getValueNames())
	print(usartSym_MR_CHRL)
	usartSym_MR_CHRL.setVisible(False)
	usartSym_MR_CHRL.setLabel(usartBitField_MR_CHRL.getDescription())
	usartSym_MR_CHRL.setDefaultValue("_8_BIT")

	usartSym_MR_SYNC = usartComponent.createBooleanSymbol("USART_MR_SYNC", usartMenu)
	print(usartSym_MR_SYNC)
	usartSym_MR_SYNC.setLabel(usartBitField_MR_SYNC.getDescription())
	usartSym_MR_SYNC.setDefaultValue(False)

	configName = Variables.get("__CONFIGURATION_NAME")

	usartHeaderFile = usartComponent.createFileSymbol(None, None)
	usartHeaderFile.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h")
	usartHeaderFile.setOutputName("plib_usart.h")
	usartHeaderFile.setDestPath("peripheral/usart/")
	usartHeaderFile.setProjectPath("config/" + configName + "/peripheral/usart/")
	usartHeaderFile.setType("HEADER")
	usartHeaderFile.setOverwrite(True)
	
	usartHeader1File = usartComponent.createFileSymbol(None, None)
	usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
	usartHeader1File.setOutputName("plib_usart" + str(num) + ".h")
	usartHeader1File.setDestPath("peripheral/usart/")
	usartHeader1File.setProjectPath("config/" + configName + "/peripheral/usart/")
	usartHeader1File.setType("HEADER")
	usartHeader1File.setOverwrite(True)
	
	usartSource1File = usartComponent.createFileSymbol(None, None)
	usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
	usartSource1File.setOutputName("plib_usart" + str(num) + ".c")
	usartSource1File.setDestPath("peripheral/usart/")
	usartSource1File.setProjectPath("config/" + configName + "/peripheral/usart/")
	usartSource1File.setType("SOURCE")
	usartSource1File.setOverwrite(True)

def setOversampling(usartSym_MR_OVER, baudRate):
	if (lBaudClock >= (16 * baudRate.getValue())):
		usartSym_MR_OVER.setValue("USART_MR_OVER", 0, 2)
	else :
		usartSym_MR_OVER.setValue("USART_MR_OVER", 1, 2)

def calculateBRGValue(usartBRGValue, baudRate):
	if (lBaudClock >= (16 * baudRate.getValue())):
		brgCD = (lBaudClock / (16 * baudRate.getValue()))
	else :
		brgCD = (lBaudClock / (8 * baudRate.getValue()))
	usartBRGValue.setValue("BRG_VALUE", brgCD, 2)
