################################################################################
##########            EVSYS DATABASE COMPONENTS           #####################
################################################################################
global 	user
global 	generator
global  path
global channel

global instance
global peripId
global NVICVector
global NVICHandler
global NVICHandlerLock

channel = 0
instance = 0
path = {}
user = {}
generator = {}
generator_module = {}
user_module = {}

def userStatus(symbol,event):
	global channelUserMap
	global user
	channelNumber = int(str(symbol.getID()).split("EVSYS_CHANNEL_")[1].split("_USER_READY")[0])
	if event["id"].startswith("EVSYS_USER_"):
		channelAssigned = event["value"] - 1
		channelUser = user.get(int(event["id"].split("EVSYS_USER_")[1]))
		channelUserMap[event["id"]] = channelAssigned

	userAvailable = False
	for key in channelUserMap.keys():
		if channelUserMap.get(key) == channelNumber:
			if Database.getSymbolValue(event["namespace"], "USER_" + user.get(int(key.split("EVSYS_USER_")[1])) + "_READY"  ) == False:
				userAvailable = False
				break
			else:
				userAvailable = True
	symbol.setValue(userAvailable, 2)
	
	
def channelSource(symbol, event):
	global evsysGenerator
	channelNumber = int(str(symbol.getID()).split("EVSYS_CHANNEL_")[1].split("_GENERATOR_ACTIVE")[0])
	symbol.setValue(Database.getSymbolValue(event["namespace"], "GENERATOR_" + str(evsysGenerator[channelNumber].getSelectedKey()) + "_ACTIVE"), 2)
	
	
def channelMenu(symbol, event):
	symbol.setVisible(event["value"])
	
def overrunInterrupt(interrupt, event):
	interrupt.setVisible(event["value"] != 2)
	
def eventInterrupt(interrupt, event):
	interrupt.setVisible(event["value"] != 2)
	
def evsysIntset(interrupt, val):
	global channel
	global NVICVector
	global NVICHandler
	global instance
	evsysInt = 0
	for id in range(0, channel):
		event = Database.getSymbolValue("evsys0","EVSYS_CHANNEL_" + str(id) + "_EVENT")
		overflow = Database.getSymbolValue("evsys0","EVSYS_CHANNEL_" + str(id) + "_OVERRUN")
		if event:
			evsysInt |= 1 << (id + 16)
		if overflow:
			evsysInt |= 1<< (id)
	interrupt.setValue(bool(evsysInt), 2)
	Database.setSymbolValue("evsys0", "EVSYS_INTERRUPT_VALUE", str(hex(evsysInt)), 2)

	if bool(evsysInt):
		Database.setSymbolValue("core", NVICVector, True, 2)
		Database.setSymbolValue("core", NVICHandler, "EVSYS" + str(instance) + "_InterruptHandler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	else:
		Database.setSymbolValue("core", NVICVector, False, 2)
		Database.setSymbolValue("core", NVICHandler, "EVSYS0_Handler", 2)
		Database.setSymbolValue("core", NVICHandlerLock, False, 2)	
	
def instantiateComponent(evsysComponent):
	global instance
	global peripId
	global NVICVector
	global NVICHandler
	global NVICHandlerLock
	
	global user
	global channel
	global channelUserMap
	channelUserMap = {}
	
	global evsysGenerator
	evsysGenerator = []
	channelUserDependency = []
	
	num = evsysComponent.getID()[-1:]
	Log.writeInfoMessage("Running EVSYS" + str(num))

	#FREQM Main Menu
	evsysSym_Menu = evsysComponent.createMenuSymbol("EVSYS_MENU", None)
	evsysSym_Menu.setLabel("EVSYS MODULE SETTINGS ")

	#EVSYS Index
	evsysSym_INDEX = evsysComponent.createIntegerSymbol("INDEX",evsysSym_Menu)
	evsysSym_INDEX.setVisible(False)
	evsysSym_INDEX.setDefaultValue(int(num))
	
	generatorSymbol = []
	generatorsNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators")
	for id in range(0,len(generatorsNode.getChildren())):
		generator[generatorsNode.getChildren()[id].getAttribute("name")] = int(generatorsNode.getChildren()[id].getAttribute("index"))	
		generatorActive = evsysComponent.createBooleanSymbol("GENERATOR_" + str(generatorsNode.getChildren()[id].getAttribute("name")) + "_ACTIVE", evsysSym_Menu)
		generatorActive.setVisible(True)
		generatorActive.setDefaultValue(False)
		generatorSymbol.append("GENERATOR_" + str(generatorsNode.getChildren()[id].getAttribute("name")) + "_ACTIVE")
	
	usersNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/users")
	for id in range(0,len(usersNode.getChildren())):
		user[int(usersNode.getChildren()[id].getAttribute("index"))] = usersNode.getChildren()[id].getAttribute("name")	
		userReady = evsysComponent.createBooleanSymbol("USER_" + str(usersNode.getChildren()[id].getAttribute("name")) + "_READY", evsysSym_Menu)
		userReady.setVisible(True)
		userReady.setDefaultValue(False)
		channelUserMap["EVSYS_USER_" + str(usersNode.getChildren()[id].getAttribute("index"))] = -1
		channelUserDependency.append("EVSYS_USER_" + str(usersNode.getChildren()[id].getAttribute("index")))
		channelUserDependency.append("USER_" + str(usersNode.getChildren()[id].getAttribute("name")) + "_READY")
		
	channelNode = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="EVSYS"]/instance/parameters')
	for id in range(0,len(channelNode.getChildren())):
		if channelNode.getChildren()[id].getAttribute("name") == "CHANNELS":
			channel = int(channelNode.getChildren()[id].getAttribute("value"))
			break
	
	evsysChannelNum = evsysComponent.createIntegerSymbol("EVSYS_CHANNEL_NUMBER",evsysSym_Menu)
	evsysChannelNum.setVisible(False)
	evsysChannelNum.setDefaultValue(int(channel))
	
		
	evsysUserNum = evsysComponent.createIntegerSymbol("EVSYS_USER_NUMBER",evsysSym_Menu)
	evsysUserNum.setVisible(False)
	evsysUserNum.setDefaultValue(int(len(user.keys())))
	for id in range(0,channel):
		evsysChannel = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" + str(id), evsysSym_Menu)
		evsysChannel.setLabel("Enable Channel" + str(id))
		evsysChannel.setDefaultValue(False)
		
		evsysChannelMenu = evsysComponent.createMenuSymbol("EVSYS_MENU_" + str(id), evsysChannel)
		evsysChannelMenu.setLabel("EVSYS Channel Configuration")
		evsysChannelMenu.setVisible(False)
		evsysChannelMenu.setDependencies(channelMenu, ["EVSYS_CHANNEL_" + str(id)])
		
		evsysGenerator.append(id)
		evsysGenerator[id] = evsysComponent.createKeyValueSetSymbol("EVSYS_CHANNEL_" +  str(id) + "_GENERATOR", evsysChannelMenu)
		evsysGenerator[id].setLabel("Event Generator")
		evsysGenerator[id].setOutputMode("Value")
		for key in generator.keys():
			evsysGenerator[id].addKey(key, str(generator.get(key)), key)
				
		evsysGeneratorActive = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" +  str(id) + "_GENERATOR_ACTIVE",evsysChannelMenu)
		evsysGeneratorActive.setDefaultValue(False)
		evsysGeneratorActive.setVisible(True)
		evsysGeneratorActive.setLabel("Channel Generator source Active")
		generatorSymbol.append("EVSYS_CHANNEL_" +  str(id) + "_GENERATOR")
		evsysGeneratorActive.setDependencies(channelSource, generatorSymbol)
		del generatorSymbol[-1]
		
		evsysPath =  evsysComponent.createKeyValueSetSymbol("EVSYS_CHANNEL_" +  str(id) + "_PATH", evsysChannelMenu)
		evsysPath.setLabel("Path Selection")
		evsysPath.setOutputMode("Value")
		pathNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EVSYS"]/value-group@[name="EVSYS_CHANNEL__PATH"]')
		for i in range(0, len(pathNode.getChildren())):
			evsysPath.addKey(pathNode.getChildren()[i].getAttribute("name"), str(pathNode.getChildren()[i].getAttribute("value")), pathNode.getChildren()[i].getAttribute("caption"))
		evsysPath.setDefaultValue(2)
		
		evsysEdge =  evsysComponent.createKeyValueSetSymbol("EVSYS_CHANNEL_" +  str(id) + "_EDGE", evsysChannelMenu)
		evsysEdge.setLabel("Event Edge Selection")
		edgeNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EVSYS"]/value-group@[name="EVSYS_CHANNEL__EDGSEL"]')
		for i in range(0, len(edgeNode.getChildren())):
			evsysEdge.addKey(edgeNode.getChildren()[i].getAttribute("name"), str(edgeNode.getChildren()[i].getAttribute("value")), edgeNode.getChildren()[i].getAttribute("caption"))			
		evsysEdge.setDefaultValue(0)
		evsysEdge.setOutputMode("Value")
		
		evsysOnDemand = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" + str(id) + "_ONDEMAND", evsysChannelMenu)
		evsysOnDemand.setLabel("Generic Clock On Demand")
		evsysOnDemand.setDefaultValue(False)
		
		evsysRunStandby = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" + str(id) + "_RUNSTANDBY", evsysChannelMenu)
		evsysRunStandby.setLabel("Run In Standby Sleep Mode")
		evsysRunStandby.setDefaultValue(False)
		
		evsysEvent = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" + str(id) + "_EVENT", evsysChannelMenu)
		evsysEvent.setLabel("Enable Event Detection Interrupt")
		evsysEvent.setDefaultValue(False)
		evsysEvent.setVisible(False)
		evsysEvent.setDependencies(eventInterrupt, ["EVSYS_CHANNEL_" +  str(id) + "_PATH"])
		
		evsysOverRun = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" + str(id) + "_OVERRUN", evsysChannelMenu)
		evsysOverRun.setLabel("Enable Overrun Interrupt")
		evsysOverRun.setDefaultValue(False)
		evsysOverRun.setVisible(False)
		evsysOverRun.setDependencies(overrunInterrupt, ["EVSYS_CHANNEL_" +  str(id) + "_PATH"])
		
		evsysUserReady = evsysComponent.createBooleanSymbol("EVSYS_CHANNEL_" +  str(id) + "_USER_READY",evsysChannelMenu)
		evsysUserReady.setDefaultValue(False)
		evsysUserReady.setVisible(True)
		evsysUserReady.setLabel("Channel" + str(id) + "Users Ready")
		evsysUserReady.setDependencies(userStatus, channelUserDependency)
		
	evsysInterrupt= evsysComponent.createBooleanSymbol("EVSYS_INTERRUPT_MODE",	evsysSym_Menu)
	evsysInterrupt.setVisible(False)
	evsysInterrupt.setDefaultValue(False)
	evsysInterrupt.setDependencies(evsysIntset, ["EVSYS_CHANNEL_0_OVERRUN", "EVSYS_CHANNEL_1_OVERRUN", "EVSYS_CHANNEL_2_OVERRUN", "EVSYS_CHANNEL_3_OVERRUN", \
													"EVSYS_CHANNEL_4_OVERRUN", "EVSYS_CHANNEL_5_OVERRUN", "EVSYS_CHANNEL_6_OVERRUN", "EVSYS_CHANNEL_7_OVERRUN", \
													"EVSYS_CHANNEL_8_OVERRUN", "EVSYS_CHANNEL_9_OVERRUN", "EVSYS_CHANNEL_10_OVERRUN", "EVSYS_CHANNEL_11_OVERRUN", \
													"EVSYS_CHANNEL_0_EVENT", "EVSYS_CHANNEL_1_EVENT", "EVSYS_CHANNEL_2_EVENT", "EVSYS_CHANNEL_3_EVENT", \
													"EVSYS_CHANNEL_4_EVENT", "EVSYS_CHANNEL_5_EVENT", "EVSYS_CHANNEL_7_EVENT", "EVSYS_CHANNEL_8_EVENT", \
													"EVSYS_CHANNEL_8_EVENT", "EVSYS_CHANNEL_9_EVENT", "EVSYS_CHANNEL_10_EVENT", "EVSYS_CHANNEL_11_EVENT"])

	evsysInterruptValue= evsysComponent.createStringSymbol("EVSYS_INTERRUPT_VALUE",	evsysSym_Menu)
	evsysInterruptValue.setVisible(False)
	evsysInterruptValue.setDefaultValue(str(hex(0)))
													
	evsysUserMenu = evsysComponent.createMenuSymbol("EVSYS_USER_MENU", evsysSym_Menu)
	evsysUserMenu.setLabel("EVSYS User SETTINGS ")
	
	for id in user.keys():
		evsysUserChannel = evsysComponent.createKeyValueSetSymbol("EVSYS_USER_" + str(id), evsysUserMenu)
		evsysUserChannel.setLabel(str(user.get(id)) + " Chanel Selection")
		evsysUserChannel.addKey("NONE", str(0), "No Channel Selected")
		for i in range(0, channel):
			evsysUserChannel.addKey("CHANNEL_" + str(i), str(hex(i + 1)), "Use Channel" + str(id))
		evsysUserChannel.setOutputMode("Value")
		
	peripId = Interrupt.getInterruptIndex("EVSYS")
	NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
	NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
	NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

	Database.clearSymbolValue("core", NVICVector)
	Database.setSymbolValue("core", NVICVector, True, 2)
	Database.clearSymbolValue("core", NVICHandler)
	Database.setSymbolValue("core", NVICHandler, "EVSYS" + str(instance) + "_InterruptHandler", 2)
	Database.clearSymbolValue("core", NVICHandlerLock)
	Database.setSymbolValue("core", NVICHandlerLock, True, 2)
	
	# ################################################################################
	# ##########             CODE GENERATION             #############################
	# ################################################################################

	configName = Variables.get("__CONFIGURATION_NAME")

	evsysSym_HeaderFile = evsysComponent.createFileSymbol(None, None)
	evsysSym_HeaderFile.setSourcePath("../peripheral/evsys_u2256/templates/plib_evsys.h.ftl")
	evsysSym_HeaderFile.setOutputName("plib_evsys"+str(num)+".h")
	evsysSym_HeaderFile.setDestPath("peripheral/evsys")
	evsysSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/evsys")
	evsysSym_HeaderFile.setType("HEADER")
	evsysSym_HeaderFile.setMarkup(True)

	evsysSym_SourceFile = evsysComponent.createFileSymbol(None, None)
	evsysSym_SourceFile.setSourcePath("../peripheral/evsys_u2256/templates/plib_evsys.c.ftl")
	evsysSym_SourceFile.setOutputName("plib_evsys"+str(num)+".c")
	evsysSym_SourceFile.setDestPath("peripheral/evsys")
	evsysSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/evsys")
	evsysSym_SourceFile.setType("SOURCE")
	evsysSym_SourceFile.setMarkup(True)

	evsysSystemInitFile = evsysComponent.createFileSymbol(None, None)
	evsysSystemInitFile.setType("STRING")
	evsysSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
	evsysSystemInitFile.setSourcePath("../peripheral/evsys_u2256/templates/system/system_initialize.c.ftl")
	evsysSystemInitFile.setMarkup(True)

	evsysSystemDefFile = evsysComponent.createFileSymbol(None, None)
	evsysSystemDefFile.setType("STRING")
	evsysSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	evsysSystemDefFile.setSourcePath("../peripheral/evsys_u2256/templates/system/system_definitions.h.ftl")
	evsysSystemDefFile.setMarkup(True)
	
	evsysComponent.addPlugin("../peripheral/evsys_u2256/plugin/eventsystem.jar")


