################################################################################
#### Global Variables ####
################################################################################
global  systickHeaderFile
global  systickSourceFile
global  systickSystemDefFile
global  systickSystemInitFile
   

Log.writeInfoMessage("Loading SYSTICK for " + Variables.get("__PROCESSOR"))

systickMax = 0x00ffffff
systickDefault = 0x0000927c

def systickUse(systickEnable, osal):
	if osal["value"] == 0:
		systickEnable.setVisible(True)
	else:
		systickEnable.setVisible(False)
		systickHeaderFile.setEnabled(False)
		systickSourceFile.setEnabled(False)
		systickSystemDefFile.setEnabled(False)
		systickSystemInitFile.setEnabled(False)
	
systickEnable = coreComponent.createBooleanSymbol("systickEnable", devCfgMenu)
systickEnable.setLabel("Use SysTick?")
systickEnable.setDependencies(systickUse, ["OSAL.OSAL_RTOS"])


	
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
        
systickMenu = coreComponent.createMenuSymbol("SYSTICK_MENU_0", systickEnable)
systickMenu.setLabel("SysTick Configuration")
systickMenu.setDependencies(showMenu, ["systickEnable"])
systickMenu.setVisible(False)
systickMenu.setDependencies(sysTickEnableCfgMenu, ["systickEnable"])

systickInterrupt = coreComponent.createBooleanSymbol("USE_SYSTICK_INTERRUPT", systickMenu)
systickInterrupt.setLabel("Enable Interrupt")

systickPeriod = coreComponent.createHexSymbol("SYSTICK_PERIOD", systickMenu)
systickPeriod.setLabel("SysTick Period")
systickPeriod.setMax(systickMax)
systickPeriod.setDefaultValue(systickDefault)

systickClock = coreComponent.createKeyValueSetSymbol("SYSTICK_CLOCK", systickMenu)
systickClock.setLabel("SysTick Clock")
systickClock.setOutputMode("Value")
systickClock.setDisplayMode("Description")
systickClock.addKey("HCLK/8", str(0) , "SysTick External clock" )
systickClock.addKey("HCLK", str(1) , "Processor clock" )
systickClock.setDefaultValue(0)

def systickCal(systickPeriod, data):
    freq_ext = Database.getSymbolValue("core", "SYSTICK")
    period = Database.getSymbolValue("core", "SYSTICK_PERIOD")
    clock = Database.getSymbolValue("core", "SYSTICK_CLOCK")
    freq_proc = Database.getSymbolValue("core", "PROCESSORCLK_FREQ")
    if clock == 0:
        delay = (float(1) / int(freq_ext)) * (int(period) * 1000)
    else:
        delay = (float(1) / int(freq_proc)) * (int(period) * 1000)
    systickPeriod.setLabel("*********SysTick will create a periodic tick of " + str(delay) +" milli seccond*************")
    


systickPeriodComment = coreComponent.createCommentSymbol("SYSTICK_PERIOD_COMMENT", systickMenu)
systickPeriodComment.setLabel("*********Systick will create a periodic tick of 1 milli seccond*************")
systickPeriodComment.setDependencies(systickCal, ["core.SYSTICK", "SYSTICK_PERIOD", "core.PROCESSORCLK_FREQ", "SYSTICK_CLOCK"])

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