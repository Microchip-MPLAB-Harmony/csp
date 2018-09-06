# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
devCfgComment = coreComponent.createCommentSymbol("CoreCfgComment1", devCfgMenu)
devCfgComment.setLabel("Note: Set Device Configuration Bits via Programming Tool")

# Device Configuration
deviceSecurity = coreComponent.createKeyValueSetSymbol("DEVICE_SECURITY", devCfgMenu)
deviceSecurity.setLabel("Security")
deviceSecurity.setOutputMode("Key")
deviceSecurity.setDisplayMode("Description")
deviceSecurity.addKey("CLEAR", "0", "Disable (Code Protection Disabled)" )
deviceSecurity.addKey("SET", "1", "Enable (Code Protection Enabled)")
deviceSecurity.setSelectedKey("CLEAR",1)


coreArch = coreComponent.createStringSymbol("CoreArchitecture", devCfgMenu)
coreArch.setLabel("Core Architecture")
coreArch.setDefaultValue("CORTEX-M0+")
coreArch.setReadOnly(True)
coreArch.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM_C20_C21")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M0+ Configuration")
cortexMenu.setDescription("Configuration for Cortex M0+")

def setDMACDefaultSettings():

    triggerSettings = {
                        "Software Trigger"  : ["TRANSACTION", "SRC", "INCREMENTED_AM", "INCREMENTED_AM",  "X1", "BYTE"],
                        "Standard_Transmit" : ["BEAT", "DST", "FIXED_AM", "INCREMENTED_AM", "X4", "BYTE"],
                        "Standard_Receive"  : ["BEAT", "DST", "FIXED_AM", "INCREMENTED_AM", "X4", "BYTE"]
                    }

    triggerRegister = {
                        "Software Trigger"  : ["None"],
                        "ADC0_RESRDY"       : ["ADC0_REGS->ADC_RESULT"],
                        "ADC1_RESRDY"       : ["ADC1_REGS->ADC_RESULT"],
                        "CAN0_EBUG"         : ["CAN0_REGS->CAN_RXBC.RBSA"],
                        "CAN1_EBUG"         : ["CAN1_REGS->CAN_RXBC.RBSA"],
                        "DAC_EMPTY"         : ["DAC_REGS->DAC_DATABUF"],
                        "PTC_EO"            : ["None"],
                        "PTC_SEQ"           : ["None"],
                        "PTC_WCOMP"         : ["None"],
                        "SDADC_RESRDY"      : ["SDADC_REGS->SDADC_RESULT"],
                        "SERCOM0_Receive"   : ["SERCOM0_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM0_Transmit"  : ["SERCOM0_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM1_Receive"   : ["SERCOM1_REGS->SPIM.SERCOM_DATA"],
                        "SERCOM1_Transmit"  : ["SERCOM1_REGS->SPIM.SERCOM_DATA"],
                        "SERCOM2_Receive"   : ["SERCOM2_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM2_Transmit"  : ["SERCOM2_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM3_Receive"   : ["SERCOM3_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM3_Transmit"  : ["SERCOM3_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM4_Receive"   : ["SERCOM4_REGS->USART.SERCOM_DATA"],
                        "SERCOM4_Transmit"  : ["SERCOM4_REGS->USART.SERCOM_DATA"],
                        "SERCOM5_Receive"   : ["SERCOM5_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM5_Transmit"  : ["SERCOM5_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM6_Receive"   : ["SERCOM6_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM6_Transmit"  : ["SERCOM6_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM7_Receive"   : ["SERCOM7_REGS->I2CM.SERCOM_DATA"],
                        "SERCOM7_Transmit"  : ["SERCOM7_REGS->I2CM.SERCOM_DATA"],
                        "TC0_OVF"           : ["TC0_REGS->COUNT16.TC_INTFLAG"],
                        "TC0_MC0"           : ["TC0_REGS->COUNT16.TC_INTFLAG"],
                        "TC0_MC1"           : ["TC0_REGS->COUNT16.TC_INTFLAG"],
                        "TC1_OVF"           : ["TC1_REGS->COUNT16.TC_INTFLAG"],
                        "TC1_MC0"           : ["TC1_REGS->COUNT16.TC_INTFLAG"],
                        "TC1_MC1"           : ["TC1_REGS->COUNT16.TC_INTFLAG"],
                        "TC2_OVF"           : ["TC2_REGS->COUNT16.TC_INTFLAG"],
                        "TC2_MC0"           : ["TC2_REGS->COUNT16.TC_INTFLAG"],
                        "TC2_MC1"           : ["TC2_REGS->COUNT16.TC_INTFLAG"],
                        "TC3_OVF"           : ["TC3_REGS->COUNT16.TC_INTFLAG"],
                        "TC3_MC0"           : ["TC3_REGS->COUNT16.TC_INTFLAG"],
                        "TC3_MC1"           : ["TC3_REGS->COUNT16.TC_INTFLAG"],
                        "TC4_OVF"           : ["TC4_REGS->COUNT16.TC_INTFLAG"],
                        "TC4_MC0"           : ["TC4_REGS->COUNT16.TC_INTFLAG"],
                        "TC4_MC1"           : ["TC4_REGS->COUNT16.TC_INTFLAG"],
                        "TC5_OVF"           : ["TC5_REGS->COUNT16.TC_INTFLAG"],
                        "TC5_MC0"           : ["TC5_REGS->COUNT16.TC_INTFLAG"],
                        "TC5_MC1"           : ["TC5_REGS->COUNT16.TC_INTFLAG"],
                        "TC6_OVF"           : ["TC6_REGS->COUNT16.TC_INTFLAG"],
                        "TC6_MC0"           : ["TC6_REGS->COUNT16.TC_INTFLAG"],
                        "TC6_MC1"           : ["TC6_REGS->COUNT16.TC_INTFLAG"],
                        "TC7_OVF"           : ["TC7_REGS->COUNT16.TC_INTFLAG"],
                        "TC7_MC0"           : ["TC7_REGS->COUNT16.TC_INTFLAG"],
                        "TC7_MC1"           : ["TC7_REGS->COUNT16.TC_INTFLAG"],
                        "TCC0_OVF"          : ["TCC0_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC0_MC0"          : ["TCC0_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC0_MC1"          : ["TCC0_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC0_MC2"          : ["TCC0_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC0_MC3"          : ["TCC0_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC1_OVF"          : ["TCC1_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC1_MC0"          : ["TCC1_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC1_MC1"          : ["TCC1_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC2_OVF"          : ["TCC2_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC2_MC0"          : ["TCC2_REGS->COUNT16.TCC_INTFLAG"],
                        "TCC2_MC1"          : ["TCC2_REGS->COUNT16.TCC_INTFLAG"],
                        "TSENS_RESRDY"      : ["TSENS_REGS->TSENS_VALUE"]

                        # All triggers are yet to be added.
                    }

    return triggerSettings, triggerRegister


def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"              : ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00000000",   "4MB"   ],
                    "RWW"               : ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00400000",   "4MB"   ],
                    "SRAM"              : ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x20000000",   "4MB"   ],}
    mpuSetUpLogicList = ["FLASH", "RWW", "SRAM"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList
    
# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_c20_c21/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_c20_c21/plugin/clk_sam_c21.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/port_u2210/config/port.py")
coreComponent.addPlugin("../peripheral/port_u2210/plugin/SAMC2xpinmanager.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/SAMC2xNVICmanager.jar")

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/MPUmanager.jar")

#load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2223/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_u2223/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_u2251/config/wdt.py")

# load device specific adc manager information
#coreComponent.addPlugin("../peripheral/afec_11147/plugin/ARM_M7_ADCmanager.jar")

# Activate Event System
Database.activateComponents(["evsys0"])

# generate startup_xc32.c file
armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("arm/templates/startup_xc32.c.ftl")
armSysStartSourceFile.setOutputName("startup.c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")


