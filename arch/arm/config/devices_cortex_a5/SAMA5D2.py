def setXDMACDefaultSettings():
    triggerSettings = { "Software Trigger"  : ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Transmit" : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM",       "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Receive"  : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM",       "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    return triggerSettings

print ("Loading System Services for " + Variables.get("__PROCESSOR"))

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAMA5D2")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-A5 Configuration")
cortexMenu.setDescription("Configuration for Cortex A5")

#load MMU with default 1:1 mapping so we can use cache
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mmu_v7a/config/mmu.py")

#load Matrix -- default all peripherals to non-secure
execfile(Variables.get("__CORE_DIR") + "/../peripheral/matrix_44025/config/matrix.py")

#load L2CC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/l2cc_11160/config/l2cc.py")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_a5d2/config/clk.py")


# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11264/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11264/plugin/SAME70pinmanager.jar")

# load AIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/aic_11051/config/aic.py")
#coreComponent.addPlugin("../peripheral/aic_11051/plugin/ARM_M7_AICmanager.jar")	# to be provided later

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

# load ADC manager information
coreComponent.addPlugin("../peripheral/adc_44073/plugin/ARM_44073_ADCManager.jar")
# load AIC manager information
coreComponent.addPlugin("../peripheral/aic_11051/plugin/AICManager_11051.jar")

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("arm/templates/iar/cortex_a/SAMA5D2/sam_a5_cstartup.s.ftl")
armSysStartSourceFile.setOutputName("cstartup.s")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

#default exception handlers.
faultSourceFile = coreComponent.createFileSymbol("DFLT_FAULT_HANDLER_C", None)
faultSourceFile.setSourcePath("arm/templates/iar/cortex_a/SAMA5D2/sam_a5_vectortrap.s.ftl")
faultSourceFile.setOutputName("vectortrap.s")
faultSourceFile.setMarkup(True)
faultSourceFile.setOverwrite(True)
faultSourceFile.setDestPath("")
faultSourceFile.setProjectPath("config/" + configName + "/")
faultSourceFile.setType("SOURCE")

linkerFile = coreComponent.createFileSymbol("LINKER_SCRIPT", None)
linkerFile.setSourcePath("arm/templates/iar/cortex_a/SAMA5D2/sam_a5_ddr.icf.ftl")
linkerFile.setOutputName("ddr.icf")
linkerFile.setMarkup(True)
linkerFile.setOverwrite(True)
linkerFile.setDestPath("")
linkerFile.setProjectPath("config/" + configName + "/")
linkerFile.setType("LINKER")
