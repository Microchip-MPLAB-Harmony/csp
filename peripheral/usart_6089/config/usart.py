regModule = Register.getRegisterModule("USART")
regGroup = regModule.getRegisterGroup("USART")

modeRegister = regGroup.getRegister("US_MR")
parityBitField = modeRegister.getBitfield("PAR")
parityValueGroup = regModule.getValueGroup(parityBitField.getValueGroupName())
bit9Field = modeRegister.getBitfield("MODE9")
bit9ValueGroup = regModule.getValueGroup(bit9Field.getValueGroupName())
stopBitsField = modeRegister.getBitfield("NBSTOP")
stopBitsValueGroup = regModule.getValueGroup(stopBitsField.getValueGroupName())
syncField = modeRegister.getBitfield("SYNC")
syncValueGroup = regModule.getValueGroup(stopBitsField.getValueGroupName())

def instantiateComponent(usartComponent):

	num = usartComponent.getID()[-1:]
	print("Running USART" + str(num))
	
	usartMenu = usartComponent.createMenuSymbol(None, None)
	usartMenu.setLabel("Hardware Settings ")
	
	usartEnable = usartComponent.createBooleanSymbol("enable", usartMenu)
	print(usartEnable)
	usartEnable.setLabel("Enable")
	usartEnable.setDefaultValue(True)
	
	usartInterrupt = usartComponent.createBooleanSymbol("interruptMode", usartMenu)
	print(usartInterrupt)
	usartInterrupt.setLabel("Enable Interrupts")
	usartInterrupt.setDefaultValue(True)
	
	usartBaud = usartComponent.createIntegerSymbol("baud", usartMenu)
	print(usartBaud)
	usartBaud.setLabel("Baud Rate")
	usartBaud.setDefaultValue(9600)
	
	usartDataBits = usartComponent.createBooleanSymbol("bit9", usartMenu)
	print(usartDataBits)
	usartDataBits.setLabel(bit9Field.getDescription())
	usartDataBits.setDefaultValue(False)
	
	usartParity = usartComponent.createComboSymbol("parityBit", usartMenu, parityValueGroup.getValueNames())
	print(usartParity)
	usartParity.setLabel(parityBitField.getDescription())
	usartParity.setDefaultValue("NO")
	
	usartStopBits = usartComponent.createComboSymbol("stopBit", usartMenu, stopBitsValueGroup.getValueNames())
	print(usartStopBits)
	usartStopBits.setLabel(stopBitsField.getDescription())
	usartStopBits.setDefaultValue("_1_BIT")

	usartSyncMode = usartComponent.createBooleanSymbol("sync", usartMenu)
	print(usartSyncMode)
	usartSyncMode.setLabel(syncField.getDescription())
	usartSyncMode.setDefaultValue(False)
	
	usartIndex = usartComponent.createIntegerSymbol("INDEX", usartMenu)
	usartIndex.setVisible(False)
	usartIndex.setDefaultValue(int(num))

	configName = Variables.get("__CONFIGURATION_NAME")

	usartHeader1File = usartComponent.createFileSymbol(None, None)
	usartHeader1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.h.ftl")
	usartHeader1File.setOutputName("plib_usart" + str(num) + ".h")
	usartHeader1File.setDestPath("system_config/" + configName +"/peripheral/usart/")
	usartHeader1File.setProjectPath("system_config/" + configName +"/peripheral/usart/")
	usartHeader1File.setType("HEADER")
	
	usartSource1File = usartComponent.createFileSymbol(None, None)
	usartSource1File.setSourcePath("../peripheral/usart_6089/templates/plib_usart.c.ftl")
	usartSource1File.setOutputName("plib_usart" + str(num) + ".c")
	usartSource1File.setDestPath("system_config/" + configName +"/peripheral/usart/")
	usartSource1File.setProjectPath("system_config/" + configName +"/peripheral/usart/")
	usartSource1File.setType("SOURCE")

