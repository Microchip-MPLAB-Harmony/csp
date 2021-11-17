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

def setDRAMAddresses(symbol, event):
    comp = event["source"]
    no_cache_size = event["value"]* pow(2,20)
    no_cache_start = int(comp.getSymbolValue("DDRAM_NO_CACHE_START_ADDR"), 16)
    cache_end = int(comp.getSymbolValue("DDRAM_CACHE_END_ADDR"), 16)
    cache_start = no_cache_start + no_cache_size
    no_cache_end = cache_start - 1
    cache_size = cache_end - cache_start + 1
    comp.setSymbolValue("DDRAM_NO_CACHE_SIZE", "0x%08X" % no_cache_size)
    comp.setSymbolValue("DDRAM_NO_CACHE_END_ADDR", "0x%08X" % no_cache_end)
    comp.setSymbolValue("DDRAM_CACHE_START_ADDR", "0x%08X" % cache_start)
    comp.setSymbolValue("DDRAM_CACHE_SIZE", "0x%08X" % cache_size)

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

#Execution start address in DDR
xc32LdAppStartAddress.setValue("0x23f00000")

#MMU Configuration data
mmu_segments = [
                ("BOOT_MEMORY", 0x00000000, 0x00100000, "normal"),
                ("ECC_ROM", 0x00100000, 0x00100000, "normal"),
                ("SRAM0", 0x00300000, 0x00100000, "normal"),
                ("SRAM1", 0x00400000, 0x00100000, "device"),
                ("UDPHS_RAM", 0x00500000, 0x00100000, "device"),
                ("UHPHS_OHCI", 0x00600000, 0x00100000, "device"),
                ("UHPHS_EHCI", 0x00700000, 0x00100000, "device"),
                ("EBI_CS0", 0x10000000, 0x10000000, "strongly-ordered"),
                ("EBI_CS2", 0x30000000, 0x10000000, "strongly-ordered"),
                ("EBI_CS3", 0x40000000, 0x10000000, "strongly-ordered"),
                ("EBI_CS4", 0x50000000, 0x10000000, "strongly-ordered"),
                ("EBI_CS5", 0x60000000, 0x10000000, "strongly-ordered"),
                ("QSPIMEM", 0x70000000, 0x10000000, "strongly-ordered"),
                ("SDMMC0", 0x80000000, 0x00100000, "strongly-ordered"),
                ("SDMMC1", 0x90000000, 0x00100000, "strongly-ordered"),
                ("OTPC", 0xEFF00000, 0x00001000, "strongly-ordered"),
                ("PERIPHERALS", 0xF0000000, 0x00100000, "strongly-ordered"),
                ("PERIPHERALS", 0xF8000000, 0x00100000, "strongly-ordered"),
                ("SYSTEM_CONTROLLER", 0xFFF00000, 0x00100000, "strongly-ordered")
            ]

#DRAM cache configuration
ddr_node = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"EBI_CS1\"]")
processor = Variables.get("__PROCESSOR")
ddr_start = int(ddr_node.getAttribute("start"), 0)
#Set 16MB as non-cacheable region and rest as cacheable region
non_cacheable_size = 16 * pow(2, 20)
if processor.endswith("1G"):
    # 1 Gbit memory
    ddr_size = (1 * pow(2,30)) / 8
elif processor.endswith("5M"):
    #512 Mbit memory
    ddr_size = (512 * pow(2,20)) / 8
    #reduce the non cacheable region to 8 MB
    non_cacheable_size = 8 * pow(2, 20)
elif processor.endswith("6K"):
    #64 Mbit memory
    ddr_size = (64 * pow(2,20)) / 8
    #reduce the non cacheable region to 8 MB
    non_cacheable_size = 8 * pow(2, 20)
else:
    #Non SiP variants, use entire DRAM region
    ddr_size = int(ddr_node.getAttribute("size"), 0)

#DRAM coherent region
dram_coherent_region = coreComponent.createIntegerSymbol("DRAM_COHERENT_REGION_SIZE", cortexMenu)
dram_coherent_region.setLabel("Size of non-cached region in DRAM (MB)")
dram_coherent_region.setMin(2)
dram_coherent_region.setMax(ddr_size/pow(2, 20))
dram_coherent_region.setDefaultValue(non_cacheable_size/pow(2, 20))

#DRAM internal symbols for MMU and linker scripts
dram_non_cacheable_start_addr = coreComponent.createStringSymbol("DDRAM_NO_CACHE_START_ADDR", None)
dram_non_cacheable_start_addr.setVisible(False)
dram_non_cacheable_start_addr.setDefaultValue("0x%08X" % ddr_start)

dram_non_cacheable_size = coreComponent.createStringSymbol("DDRAM_NO_CACHE_SIZE", None)
dram_non_cacheable_size.setVisible(False)
dram_non_cacheable_size.setLabel("Coherent region size in DRAM")
dram_non_cacheable_size.setDefaultValue("0x%08X" % non_cacheable_size)
dram_non_cacheable_size.setDependencies(setDRAMAddresses, ["DRAM_COHERENT_REGION_SIZE"])

dram_non_cacheable_end_addr = coreComponent.createStringSymbol("DDRAM_NO_CACHE_END_ADDR", None)
dram_non_cacheable_end_addr.setVisible(False)
dram_non_cacheable_end_addr.setDefaultValue("0x%08X" % (ddr_start + non_cacheable_size - 1))

dram_cacheable_start_addr = coreComponent.createStringSymbol("DDRAM_CACHE_START_ADDR", None)
dram_cacheable_start_addr.setVisible(False)
dram_cacheable_start_addr.setDefaultValue("0x%08X" % (ddr_start + non_cacheable_size))

dram_cacheable_size = coreComponent.createStringSymbol("DDRAM_CACHE_SIZE", None)
dram_cacheable_size.setVisible(False)
dram_cacheable_size.setDefaultValue("0x%08X" % (ddr_size - non_cacheable_size))

dram_cacheable_end_addr = coreComponent.createStringSymbol("DDRAM_CACHE_END_ADDR", None)
dram_cacheable_end_addr.setVisible(False)
dram_cacheable_end_addr.setDefaultValue("0x%08X" % (ddr_start + ddr_size - 1))

dram_boundary_addr = coreComponent.createStringSymbol("DDRAM_BOUNDARY_ADDR", None)
dram_boundary_addr.setVisible(False)
dram_boundary_addr.setDefaultValue("0x%08X" % (ddr_start + ddr_size))

# load MMU
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mmu_sam9/config/mmu.py")

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
syscSharedInterruptFile.setSourcePath("arm/templates/common/shared_interrupt/SAM9.c.ftl")
syscSharedInterruptFile.setMarkup(True)

syscSharedInterruptSysInitFile = coreComponent.createFileSymbol("SYSC_INITIALIZE_CALL", None)
syscSharedInterruptSysInitFile.setType("STRING")
syscSharedInterruptSysInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
syscSharedInterruptSysInitFile.setSourcePath("arm/templates/common/shared_interrupt/sysc_initialize.c.ftl")
syscSharedInterruptSysInitFile.setMarkup(True)

compiler_choice = deviceFamily.getComponent().getSymbolByID("COMPILER_CHOICE")
#if compiler_choice.getSelectedKey() == "XC32":
armSysStartSourceFile = coreComponent.createFileSymbol(None, None)
armSysStartSourceFile.setSourcePath("arm/templates/xc32/arm_926/SAM9/cstartup.S.ftl")
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
faultSourceFile.setSourcePath("arm/templates/xc32/arm_926/SAM9/vectortrap.s")
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
linkerFile.setSourcePath("arm/templates/xc32/arm_926/SAM9/ddram.ld.ftl")
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
armSysStartSourceFile.setSourcePath("arm/templates/iar/arm_926/SAM9/cstartup.s.ftl")
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
faultSourceFile.setSourcePath("arm/templates/iar/arm_926/SAM9/vectortrap.s")
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
linkerFile.setSourcePath("arm/templates/iar/arm_926/SAM9/ddram.icf.ftl")
linkerFile.setOutputName("ddram.icf")
linkerFile.setMarkup(True)
linkerFile.setOverwrite(True)
linkerFile.setDestPath("")
linkerFile.setProjectPath("config/" + configName + "/")
linkerFile.setType("LINKER")
linkerFile.setEnabled(compiler_choice.getSelectedKey() == "IAR")
linkerFile.setDependencies(lambda symbol, event: symbol.setEnabled(event["symbol"].getSelectedKey() == "IAR"), ["COMPILER_CHOICE"])


