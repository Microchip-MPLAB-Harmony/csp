################################################################################
#### Global Variables ####
################################################################################
global  systickHeaderFile
global  systickSourceFile
global  systickSystemDefFile
global  systickSystemInitFile
global  systickNVICVector
global  systickNVICHandlerLock

Log.writeInfoMessage("Loading SYSTICK for " + Variables.get("__PROCESSOR"))


def systickUse(systickEnable, osal):
    if osal["value"] == "BareMetal":
        systickEnable.setVisible(True)
    else:
        systickEnable.setVisible(False)
        systickHeaderFile.setEnabled(False)
        systickSourceFile.setEnabled(False)
        systickSystemDefFile.setEnabled(False)
        systickSystemInitFile.setEnabled(False)

sysTickMenu = coreComponent.createMenuSymbol("SYSTICK_MENU", cortexMenu)
sysTickMenu.setLabel("SysTick")

systickEnable = coreComponent.createBooleanSymbol("systickEnable", sysTickMenu)
systickEnable.setLabel("Enable SysTick")
systickEnable.setDependencies(systickUse, ["HarmonyCore.SELECT_RTOS"])



def showMenu(menu, show):
    menu.setVisible(show["value"])

def sysTickEnableCfgMenu(CfgMenu, event):
    CfgMenu.setVisible(event["value"])

    if(event["value"] == True):
        systickHeaderFile.setEnabled(True)
        systickSourceFile.setEnabled(True)
        systickSystemDefFile.setEnabled(True)
        systickSystemInitFile.setEnabled(True)
    else:
        systickHeaderFile.setEnabled(False)
        systickSourceFile.setEnabled(False)
        systickSystemDefFile.setEnabled(False)
        systickSystemInitFile.setEnabled(False)

def sysTickNVICControl(symbol, event):
    Database.clearSymbolValue("core", systickNVICVector)
    Database.clearSymbolValue("core", systickNVICHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", systickNVICVector, True, 2)
        Database.setSymbolValue("core", systickNVICHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", systickNVICVector, False, 2)
        Database.setSymbolValue("core", systickNVICHandlerLock, False, 2)

systickMenu = coreComponent.createMenuSymbol("SYSTICK_MENU_0", systickEnable)
systickMenu.setLabel("SysTick Configuration")
systickMenu.setDependencies(showMenu, ["systickEnable"])
systickMenu.setVisible(False)
systickMenu.setDependencies(sysTickEnableCfgMenu, ["systickEnable"])

systickInterrupt = coreComponent.createBooleanSymbol("USE_SYSTICK_INTERRUPT", systickMenu)
systickInterrupt.setLabel("Enable Interrupt")

systickClock = coreComponent.createKeyValueSetSymbol("SYSTICK_CLOCK", systickMenu)
systickClock.setLabel("SysTick Clock")
systickClock.setOutputMode("Value")
systickClock.setDisplayMode("Description")
if Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK"):
    systickClock.addKey("HCLK/2", str(0) , "SysTick External clock (HCLK/2)" )
systickClock.addKey("HCLK", str(1) , "Processor clock (HCLK)" )

def sysTickMax(systick, event):
	clock = 0
	freq_ext = 0
	freq_proc = 0
	max = 0
	if Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK"):
		freq_ext = Database.getSymbolValue("core", "SYSTICK")
		clock = Database.getSymbolValue("core", "SYSTICK_CLOCK")
	else:
		clock = 1
	freq_proc = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")

	if clock == 0:
		if (int(freq_ext) != 0):
			max = ((float(1) / int(freq_ext)) * 16777215 * 1000)
	else:
		if (int(freq_proc) !=0):
			max = ((float(1) / int(freq_proc)) * 16777215 * 1000)
	systick.setMax(float(max))
	


def systickCal(symbol, event):	
	if Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK"):
		clock = Database.getSymbolValue("core", "SYSTICK_CLOCK")
		freq_ext = Database.getSymbolValue("core", "SYSTICK")
	else:
		clock = 1
	period = Database.getSymbolValue("core", "SYSTICK_PERIOD_MS")
	freq_proc = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
	
	if clock == 0:
		if (int(freq_ext) != 0):
			value = int((float(freq_ext) / 1000) * period)
	else:
		if (int(freq_proc) !=0):
			value = int((float(freq_proc) / 1000) * period)
			
	symbol.setValue(str(hex(value)),2)
	Database.setSymbolValue("core","SYSTICK_PERIOD_US", int(period * 1000), 2)
	
systickPeriodMS = coreComponent.createFloatSymbol("SYSTICK_PERIOD_MS", systickMenu)
systickPeriodMS.setLabel("Systick Period(Milli sec)")
systickPeriodMS.setVisible(True)
systickPeriodMS.setDefaultValue(float(1.0))
systickPeriodMS.setMin(0)
systickPeriodMS.setDependencies(sysTickMax, ["core.CPU_CLOCK_FREQUENCY", "SYSTICK_CLOCK", "core.SYSTICK_CLOCK_FREQUENCY"])
systickClock.setDefaultValue(int(Database.getSymbolValue("core","SYSTICK_EXTERNAL_CLOCK")))

systickDefault = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")) / 1000
systickPeriod = coreComponent.createStringSymbol("SYSTICK_PERIOD", systickMenu)
systickPeriod.setLabel("SysTick Period")
systickPeriod.setVisible(False)
systickPeriod.setDefaultValue(str(hex(systickDefault)))
systickPeriod.setDependencies(systickCal, ["SYSTICK_PERIOD_MS", "SYSTICK_CLOCK", "core.CPU_CLOCK_FREQUENCY", "core.SYSTICK_CLOCK_FREQUENCY"])

systickPeriodUS = coreComponent.createIntegerSymbol("SYSTICK_PERIOD_US", systickMenu)
systickPeriodUS.setVisible(False)
systickPeriodUS.setDefaultValue(1000)
systickPeriodUS.setMin(0)


# Setup Peripheral Interrupt in Interrupt manager
systickPeripId = Interrupt.getInterruptIndex("SysTick")
systickNVICVector = "NVIC_" + str(systickPeripId) + "_ENABLE"
systickNVICHandlerLock = "NVIC_" + str(systickPeripId) + "_HANDLER_LOCK"

# NVIC Dynamic settings
SYSTICK_NVICControl = coreComponent.createBooleanSymbol("NVIC_SYSTICK_ENABLE", systickMenu)
SYSTICK_NVICControl.setDependencies(sysTickNVICControl, ["USE_SYSTICK_INTERRUPT"])
SYSTICK_NVICControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

systickHeaderFile = coreComponent.createFileSymbol("SYSTICK_FILE_0", None)
systickHeaderFile.setSourcePath("../peripheral/systick/templates/plib_systick.h.ftl")
systickHeaderFile.setOutputName("plib_systick.h")
systickHeaderFile.setDestPath("/peripheral/systick/")
systickHeaderFile.setProjectPath("config/" + configName + "/peripheral/systick/")
systickHeaderFile.setType("HEADER")
systickHeaderFile.setOverwrite(True)
systickHeaderFile.setEnabled(False)
systickHeaderFile.setMarkup(True)

systickSourceFile = coreComponent.createFileSymbol("SYSTICK_FILE_1", None)
systickSourceFile.setSourcePath("../peripheral/systick/templates/plib_systick.c.ftl")
systickSourceFile.setOutputName("plib_systick.c")
systickSourceFile.setDestPath("/peripheral/systick/")
systickSourceFile.setProjectPath("config/" + configName + "/peripheral/systick/")
systickSourceFile.setType("SOURCE")
systickSourceFile.setOverwrite(True)
systickSourceFile.setMarkup(True)
systickSourceFile.setEnabled(False)

systickSystemDefFile = coreComponent.createFileSymbol("SYSTICK_FILE_2", None)
systickSystemDefFile.setType("STRING")
systickSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
systickSystemDefFile.setSourcePath("../peripheral/systick/templates/system/system_definitions.h.ftl")
systickSystemDefFile.setMarkup(True)
systickSystemDefFile.setEnabled(False)

systickSystemInitFile = coreComponent.createFileSymbol("systickSystemInitFile", None)
systickSystemInitFile.setType("STRING")
systickSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
systickSystemInitFile.setSourcePath("../peripheral/systick/templates/system/system_initialize.c.ftl")
systickSystemInitFile.setMarkup(True)
systickSystemInitFile.setEnabled(False)