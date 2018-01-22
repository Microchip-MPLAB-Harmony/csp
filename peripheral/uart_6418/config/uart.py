uartRegModule = Register.getRegisterModule("UART")
uartRegGroup = uartRegModule.getRegisterGroup("UART")

uartReg_MR = uartRegGroup.getRegister("UART_MR")
uartBitField_MR_PAR = uartReg_MR.getBitfield("PAR")
uartValGrp_MR_PAR = uartRegModule.getValueGroup(uartBitField_MR_PAR.getValueGroupName())

global lBaudClock
lBaudClock = Database.getSymbolValue("PMC", "SYS_CLK_MASTERCLK_FREQ")
#Above API is not working, so hard coding MCLK value for now
lBaudClock = 150000000

def instantiateComponent(uartComponent):

	num = uartComponent.getID()[-1:]
	print("Running UART" + str(num))
	
	uartMenu = uartComponent.createMenuSymbol(None, None)
	uartMenu.setLabel("Hardware Settings")
	
	uartIndex = uartComponent.createIntegerSymbol("INDEX", uartMenu)
	uartIndex.setVisible(False)
	uartIndex.setDefaultValue(int(num))

	uartInterrupt = uartComponent.createBooleanSymbol("INTERRUPT_MODE", uartMenu)
	print(uartInterrupt)
	uartInterrupt.setLabel("Interrupt Mode")
	uartInterrupt.setDefaultValue(True)
	
	uartBaud = uartComponent.createIntegerSymbol("BAUD_RATE", uartMenu)
	print(uartBaud)
	uartBaud.setLabel("Baud Rate")
	#Default value is triggered by calculateBRGValue callback
	
	#Local symbol related to BaudRate
	uartBRGValue = uartComponent.createIntegerSymbol("BRG_VALUE", uartMenu)
	print(uartBRGValue)
	uartBRGValue.setVisible(False)
	uartBRGValue.setDependencies(calculateBRGValue, ["BAUD_RATE"])
	uartBaud.setDefaultValue(9600)
	
	uartSym_MR_PAR = uartComponent.createComboSymbol("UART_MR_PAR", uartMenu, uartValGrp_MR_PAR.getValueNames())
	print(uartSym_MR_PAR)
	uartSym_MR_PAR.setLabel(uartBitField_MR_PAR.getDescription())
	uartSym_MR_PAR.setDefaultValue("NO")

	configName = Variables.get("__CONFIGURATION_NAME")

	uartHeaderFile = uartComponent.createFileSymbol(None, None)
	uartHeaderFile.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h")
	uartHeaderFile.setOutputName("plib_uart.h")
	uartHeaderFile.setDestPath("peripheral/uart/")
	uartHeaderFile.setProjectPath("config/" + configName + "/peripheral/uart/")
	uartHeaderFile.setType("HEADER")
	uartHeaderFile.setOverwrite(True)

	uartHeader1File = uartComponent.createFileSymbol(None, None)
	uartHeader1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.h.ftl")
	uartHeader1File.setOutputName("plib_uart" + str(num) + ".h")
	uartHeader1File.setDestPath("peripheral/uart/")
	uartHeader1File.setProjectPath("config/" + configName + "/peripheral/uart/")
	uartHeader1File.setType("HEADER")
	uartHeader1File.setOverwrite(True)
	uartHeader1File.setMarkup(True)

	uartSource1File = uartComponent.createFileSymbol(None, None)
	uartSource1File.setSourcePath("../peripheral/uart_6418/templates/plib_uart.c.ftl")
	uartSource1File.setOutputName("plib_uart" + str(num) + ".c")
	uartSource1File.setDestPath("peripheral/uart/")
	uartSource1File.setProjectPath("config/" + configName + "/peripheral/uart/")
	uartSource1File.setType("SOURCE")
	uartSource1File.setOverwrite(True)
	uartSource1File.setMarkup(True)

	uartSystemInitFile = uartComponent.createFileSymbol(None, None)
	uartSystemInitFile.setType("STRING")
	uartSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
	uartSystemInitFile.setSourcePath("../peripheral/uart_6418/templates/system/system_initialize.h.ftl")
	uartSystemInitFile.setMarkup(True)

	uartSystemIntFile = uartComponent.createFileSymbol(None, None)
	uartSystemIntFile.setType("STRING")
	uartSystemIntFile.setOutputName("core.LIST_SYSTEM_INTERRUPT_C_VECTORS")
	uartSystemIntFile.setSourcePath("../peripheral/uart_6418/templates/system/system_interrupt.c.ftl")
	uartSystemIntFile.setMarkup(True)

	uartSystemDefFile = uartComponent.createFileSymbol(None, None)
	uartSystemDefFile.setType("STRING")
	uartSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	uartSystemDefFile.setSourcePath("../peripheral/uart_6418/templates/system/system_definitions.h.ftl")
	uartSystemDefFile.setMarkup(True)

def calculateBRGValue(uartBRGValue, baudRate):
	brgCD = (lBaudClock / (16 * baudRate.getValue()))
	uartBRGValue.setValue("BRG_VALUE", brgCD, 2)
