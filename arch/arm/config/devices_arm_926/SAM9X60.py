"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""
def setXDMACDefaultSettings():
    triggerSettings = { "Software Trigger"  : ["MEM_TRAN", "PER2MEM", "HWR_CONNECTED", "INCREMENTED_AM", "INCREMENTED_AM", "AHB_IF1", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Transmit" : ["PER_TRAN", "MEM2PER", "HWR_CONNECTED", "INCREMENTED_AM", "FIXED_AM",       "AHB_IF0", "AHB_IF1", "BYTE", "CHK_1", "SINGLE"],
                        "Standard_Receive"  : ["PER_TRAN", "PER2MEM", "HWR_CONNECTED", "FIXED_AM",       "INCREMENTED_AM", "AHB_IF1", "AHB_IF0", "BYTE", "CHK_1", "SINGLE"]}

    return triggerSettings

# SYSIO Pin configuration information (Required by PIO 11104)
# SYSIO configuration is not available for 9X6
global getArchSYSIOInformation
def getArchSYSIOInformation():
    return None, None, None

print ("Loading System Services for " + Variables.get("__PROCESSOR"))

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("SAM9X60")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("ARM 926 Configuration")
cortexMenu.setDescription("Configuration for ARM 926")

freeRTOSVectors = coreComponent.createBooleanSymbol("USE_FREERTOS_VECTORS", None)
freeRTOSVectors.setVisible(False)
freeRTOSVectors.setReadOnly(True)
freeRTOSVectors.setDefaultValue(False)

threadXVectors = coreComponent.createBooleanSymbol("USE_THREADX_VECTORS", None)
threadXVectors.setVisible(False)
threadXVectors.setReadOnly(True)
threadXVectors.setDefaultValue(False)

#Low memory footprint device, set load address to DRAM base + 1MB
sipVariant =  Variables.get("__PROCESSOR").split("SAM9X60")[1]
if sipVariant:
    if sipVariant == "D6K":
        xc32LdAppStartAddress.setValue("0x20100000")
    else:
        xc32LdAppStartAddress.setValue("0x21000000")
else:
    xc32LdAppStartAddress.setValue("0x23f00000")

# load MMU
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mmu_sam_9x60/config/mmu.py")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_sam_9x60/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_sam_9x60/plugin/clk_sam_9x60.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pio_11004/config/pio.py")
coreComponent.addPlugin("../peripheral/pio_11004/plugin/pio_11004.jar")

# load AIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/aic_11051/config/aic.py")
coreComponent.addPlugin("../peripheral/aic_11051/plugin/aic_11051.jar")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/xdmac_11161/config/xdmac.py")
coreComponent.addPlugin("../peripheral/xdmac_11161/plugin/dmamanager.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_44154/config/wdt.py")


syscSharedInterruptFile = coreComponent.createFileSymbol("SYSC_INITIALIZE_DEF", None)
syscSharedInterruptFile.setType("STRING")
syscSharedInterruptFile.setOutputName("core.LIST_SYSTEM_INIT_C_INITIALIZER_STATIC_FUNCTIONS")
syscSharedInterruptFile.setSourcePath("arm/templates/common/shared_interrupt/SAM9X6.c.ftl")
syscSharedInterruptFile.setMarkup(True)

syscSharedInterruptSysInitFile = coreComponent.createFileSymbol("SYSC_INITIALIZE_CALL", None)
syscSharedInterruptSysInitFile.setType("STRING")
syscSharedInterruptSysInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
syscSharedInterruptSysInitFile.setSourcePath("arm/templates/common/shared_interrupt/sysc_initialize.c.ftl")
syscSharedInterruptSysInitFile.setMarkup(True)

compiler_choice = deviceFamily.getComponent().getSymbolByID("COMPILER_CHOICE")
#if compiler_choice.getSelectedKey() == "XC32":
armSysStartSourceFile = coreComponent.createFileSymbol(None, None)
armSysStartSourceFile.setSourcePath("arm/templates/xc32/arm_926/SAM9X60/cstartup.S.ftl")
armSysStartSourceFile.setOutputName("cstartup.S")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setEnabled(compiler_choice.getSelectedKey() == "XC32")
armSysStartSourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "XC32"), ["COMPILER_CHOICE"])

#default exception handlers.
faultSourceFile = coreComponent.createFileSymbol(None, None)
faultSourceFile.setSourcePath("arm/templates/xc32/arm_926/SAM9X60/vectortrap.s")
faultSourceFile.setOutputName("vectortrap.s")
faultSourceFile.setMarkup(False)
faultSourceFile.setOverwrite(True)
faultSourceFile.setDestPath("")
faultSourceFile.setProjectPath("config/" + configName + "/")
faultSourceFile.setType("SOURCE")
faultSourceFile.setEnabled(compiler_choice.getSelectedKey() == "XC32")
faultSourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "XC32"), ["COMPILER_CHOICE"])

#linker file
linkerFile = coreComponent.createFileSymbol(None, None)
linkerFile.setSourcePath("arm/templates/xc32/arm_926/SAM9X60/ddram.ld.ftl")
linkerFile.setOutputName("ddram.ld")
linkerFile.setMarkup(True)
linkerFile.setOverwrite(True)
linkerFile.setDestPath("")
linkerFile.setProjectPath("config/" + configName + "/")
linkerFile.setType("LINKER")
linkerFile.setEnabled(compiler_choice.getSelectedKey() == "XC32")
linkerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "XC32"), ["COMPILER_CHOICE"])
#elif compiler_choice.getSelectedKey() == "IAR":
armSysStartSourceFile = coreComponent.createFileSymbol(None, None)
armSysStartSourceFile.setSourcePath("arm/templates/iar/arm_926/SAM9X60/cstartup.s.ftl")
armSysStartSourceFile.setOutputName("cstartup.s")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setEnabled(compiler_choice.getSelectedKey() == "IAR")
armSysStartSourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "IAR"), ["COMPILER_CHOICE"])

#default exception handlers.
faultSourceFile = coreComponent.createFileSymbol(None, None)
faultSourceFile.setSourcePath("arm/templates/iar/arm_926/SAM9X60/vectortrap.s")
faultSourceFile.setOutputName("vectortrap.s")
faultSourceFile.setMarkup(False)
faultSourceFile.setOverwrite(True)
faultSourceFile.setDestPath("")
faultSourceFile.setProjectPath("config/" + configName + "/")
faultSourceFile.setType("SOURCE")
faultSourceFile.setEnabled(compiler_choice.getSelectedKey() == "IAR")
faultSourceFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "IAR"), ["COMPILER_CHOICE"])

#linker file
linkerFile = coreComponent.createFileSymbol(None, None)
linkerFile.setSourcePath("arm/templates/iar/arm_926/SAM9X60/ddram.icf.ftl")
linkerFile.setOutputName("ddram.icf")
linkerFile.setMarkup(True)
linkerFile.setOverwrite(True)
linkerFile.setDestPath("")
linkerFile.setProjectPath("config/" + configName + "/")
linkerFile.setType("LINKER")
linkerFile.setEnabled(compiler_choice.getSelectedKey() == "IAR")
linkerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "IAR"), ["COMPILER_CHOICE"])


