def setXDMACDefaultSettings():
    triggerSettings = { "Software Trigger"  : ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Transmit" : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM",       "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Receive"  : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM",       "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    triggerRegister = { "Software Trigger"  : ["None"],
                        "TWIHS0_Transmit"   : ["TWIHS0_REGS->TWIHS_THR"],
                        "TWIHS0_Receive"    : ["TWIHS0_REGS->TWIHS_RHR"],
                        "TWIHS1_Transmit"   : ["TWIHS1_REGS->TWIHS_THR"],
                        "TWIHS1_Receive"    : ["TWIHS1_REGS->TWIHS_RHR"],
                        "QSPI0_Transmit"    : ["QSPI0_REGS->QSPI_TDR"],
                        "QSPI0_Receive"     : ["QSPI0_REGS->QSPI_RDR"],
                        "SPI0_Transmit"     : ["SPI0_REGS->SPI_TDR"],
                        "SPI0_Receive"      : ["SPI0_REGS->SPI_RDR"],
                        "SPI1_Transmit"     : ["SPI1_REGS->SPI_TDR"],
                        "SPI1_Receive"      : ["SPI1_REGS->SPI_RDR"],
                        "PWM_Transmit"      : ["None"],
                        "FLEXCOM0_Transmit" : ["None"],
                        "FLEXCOM0_Receive"  : ["None"],
                        "FLEXCOM1_Transmit" : ["None"],
                        "FLEXCOM1_Receive"  : ["None"],
                        "FLEXCOM2_Transmit" : ["None"],
                        "FLEXCOM2_Receive"  : ["None"],
                        "FLEXCOM3_Transmit" : ["None"],
                        "FLEXCOM3_Receive"  : ["None"],
                        "FLEXCOM4_Transmit" : ["None"],
                        "FLEXCOM4_Receive"  : ["None"],
                        "SSC0_Transmit"     : ["SSC0_REGS->SSC_THR"],
                        "SSC0_Receive"      : ["SSC0_REGS->SSC_RHR"],
                        "SSC1_Transmit"     : ["SSC1_REGS->SSC_THR"],
                        "SSC1_Receive"      : ["SSC1_REGS->SSC_RHR"],
                        "ADC_Receive"       : ["None"],
                        "AES_Transmit"      : ["None"],
                        "AES_Receive"       : ["None"],
                        "TDES_Transmit"     : ["None"],
                        "TDES_Receive"      : ["None"],
                        "SHA_Transmit"      : ["None"],
                        "I2SC0_Transmit"    : ["I2SC0_REGS->I2SC_THR"],
                        "I2SC0_Receive"     : ["I2SC0_REGS->I2SC_RHR"],
                        "I2SC1_Transmit"    : ["I2SC0_REGS->I2SC_THR"],
                        "I2SC1_Receive"     : ["I2SC0_REGS->I2SC_RHR"],
                        "UART0_Transmit"    : ["USART0_REGS->US_THR"],
                        "UART0_Receive"     : ["USART0_REGS->US_RHR"],
                        "UART1_Transmit"    : ["USART1_REGS->US_THR"],
                        "UART1_Receive"     : ["USART1_REGS->US_RHR"],
                        "UART2_Transmit"    : ["USART2_REGS->US_THR"],
                        "UART2_Receive"     : ["USART2_REGS->US_RHR"],
                        "UART3_Transmit"    : ["USART3_REGS->US_THR"],
                        "UART3_Receive"     : ["USART3_REGS->US_RHR"],
                        "UART4_Transmit"    : ["USART4_REGS->US_THR"],
                        "UART4_Receive"     : ["USART4_REGS->US_RHR"],
                        "TC0_Receive"       : ["None"],
                        "TC1_Receive"       : ["None"],
                        "CLASSD_Transmit"   : ["None"],
                        "QSPI1_Transmit"    : ["QSPI1_REGS->QSPI_TDR"],
                        "QSPI1_Receive"     : ["QSPI1_REGS->QSPI_RDR"],
                        "PDMIC_Receive"     : ["None"] }
    return triggerSettings, triggerRegister

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

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_a5d2/config/clk.py")


# load device specific pin manager information

# load AIC

# load PIT

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_6080/config/wdt.py")

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("arm/templates/a5_cstartup.s.ftl")
armSysStartSourceFile.setOutputName("cstartup.s")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

#default exception handlers.
faultSourceFile = coreComponent.createFileSymbol("DFLT_FAULT_HANDLER_C", None)
faultSourceFile.setSourcePath("arm/templates/a5_vectortrap.s.ftl")
faultSourceFile.setOutputName("vectortrap.s")
faultSourceFile.setMarkup(True)
faultSourceFile.setOverwrite(True)
faultSourceFile.setDestPath("")
faultSourceFile.setProjectPath("config/" + configName + "/")
faultSourceFile.setType("SOURCE")

linkerFile = coreComponent.createFileSymbol("LINKER_SCRIPT", None)
linkerFile.setSourcePath("arm/templates/a5_ddr.icf")
linkerFile.setOutputName("ddr.icf")
linkerFile.setMarkup(False)
linkerFile.setOverwrite(True)
linkerFile.setDestPath("")
linkerFile.setProjectPath("config/"+configName+"/")
linkerFile.setType("LINKER")
