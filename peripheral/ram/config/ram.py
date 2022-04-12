"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
global plibId
plibId = None

RamNames = ["HSRAM", "HRAMC0", "HMCRAMC0", "IRAM", "IRAM0", "EBI_MPDDR", "FlexRAM", "FLEXRAM", "DRAM", "SDRAM_CS", "DDR_CS", "kseg0_data_mem", "kseg1_data_mem", "RAM_SYSTEM_RAM"]

addr_space          = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space")
addr_space_children = addr_space.getChildren()

periphNode          = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals")
peripherals         = periphNode.getChildren()

for mem_idx in range(0, len(addr_space_children)):
    mem_seg     = addr_space_children[mem_idx].getAttribute("name")
    mem_type    = addr_space_children[mem_idx].getAttribute("type")

    if ((any(x == mem_seg for x in RamNames) == True)):
        if ((mem_type == "ram") or (mem_type == "other")):
            ram_start   = addr_space_children[mem_idx].getAttribute("start")
        elif (mem_seg == "kseg0_data_mem"):
            ram_start   = "0x80000000"
        elif (mem_seg == "kseg1_data_mem"):
            ram_start   = "0xA0000000"
        else:
            ram_start = "0x0"

        ram_size    = addr_space_children[mem_idx].getAttribute("size")

        break

def ramSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])

def instantiateComponent(ramComponent):

    global plibId

    ramInstanceName = ramComponent.createStringSymbol("RAM_INSTANCE_NAME", None)
    ramInstanceName.setVisible(False)
    ramInstanceName.setDefaultValue("RAM")

    mcramcPlib = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"MCRAMC\"]")
    if mcramcPlib != None:
        mcramcPlibId = mcramcPlib.getAttribute("id")
        plibId = "mcramc_" + mcramcPlibId

    if plibId == "mcramc_03727":
        execfile(Module.getPath() + "../../csp/peripheral/ram/config/" + "mcramc_03727.py")

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    # Configures the library for interrupt mode operations
    ramSym_Interrupt = ramComponent.createBooleanSymbol("INTERRUPT_ENABLE", None)
    ramSym_Interrupt.setLabel("Enable Interrupt?")
    ramSym_Interrupt.setVisible(False)
    ramSym_Interrupt.setDefaultValue(False)

    # Configuration when interfaced with memory driver
    ramSym_MemoryDriver = ramComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    ramSym_MemoryDriver.setLabel("Memory Driver Connected")
    ramSym_MemoryDriver.setVisible(False)
    ramSym_MemoryDriver.setDefaultValue(False)

    ramSym_MemoryStartAddr = ramComponent.createStringSymbol("START_ADDRESS", None)
    ramSym_MemoryStartAddr.setLabel("RAM Media Start Address (Hex)")
    ramSym_MemoryStartAddr.setVisible(False)
    ramSym_MemoryStartAddr.setDefaultValue(ram_start[2:])
    ramSym_MemoryStartAddr.setDependencies(ramSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    mediaSizeDesc = "This option is used to define the size of Media in KB. \
                     Application needs to define an array of the mentioned size starting from RAM Media Start Address. \
                     If media has to be formatted through firmware then minimum size of media has to be 96KB. \
                     If Application is using a RAM Disk image containing FAT information then the Media size can be reduced \
                     based on disk image size."

    ramSym_MemoryMediaSize = ramComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", None)
    ramSym_MemoryMediaSize.setLabel("RAM Media Size (KB)")
    ramSym_MemoryMediaSize.setVisible(False)
    ramSym_MemoryMediaSize.setDefaultValue(96)
    ramSym_MemoryMediaSize.setDependencies(ramSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])
    ramSym_MemoryMediaSize.setDescription(mediaSizeDesc)

    ramSym_PROGRAM_SIZE = ramComponent.createStringSymbol("FLASH_PROGRAM_SIZE", None)
    ramSym_PROGRAM_SIZE.setLabel("RAM Program Size (Bytes)")
    ramSym_PROGRAM_SIZE.setVisible(False)
    ramSym_PROGRAM_SIZE.setDefaultValue("512")

    ramSym_MemoryEraseEnable = ramComponent.createBooleanSymbol("ERASE_ENABLE", None)
    ramSym_MemoryEraseEnable.setLabel("RAM Erase Enable")
    ramSym_MemoryEraseEnable.setVisible(False)
    ramSym_MemoryEraseEnable.setDefaultValue(False)
    ramSym_MemoryEraseEnable.setReadOnly(True)

    writeApiName = ramComponent.getID().upper() + "_Write"

    ramWriteApiName = ramComponent.createStringSymbol("WRITE_API_NAME", None)
    ramWriteApiName.setVisible(False)
    ramWriteApiName.setReadOnly(True)
    ramWriteApiName.setDefaultValue(writeApiName)


################################################################################
########                      Code Generation                      #############
################################################################################

    if plibId == None:
        configName = Variables.get("__CONFIGURATION_NAME")

        # Instance Header File
        ramHeaderFile = ramComponent.createFileSymbol("RAM_INSTANCE_HEADER", None)
        ramHeaderFile.setSourcePath("../peripheral/ram/templates/plib_ram.h.ftl")
        ramHeaderFile.setOutputName("plib_" + ramInstanceName.getValue().lower() + ".h")
        ramHeaderFile.setDestPath("/peripheral/ram/")
        ramHeaderFile.setProjectPath("config/" + configName + "/peripheral/ram/")
        ramHeaderFile.setType("HEADER")
        ramHeaderFile.setMarkup(True)

        # Source File
        ramSourceFile = ramComponent.createFileSymbol("RAM_SOURCE", None)
        ramSourceFile.setSourcePath("../peripheral/ram/templates/plib_ram.c.ftl")
        ramSourceFile.setOutputName("plib_" + ramInstanceName.getValue().lower() + ".c")
        ramSourceFile.setDestPath("/peripheral/ram/")
        ramSourceFile.setProjectPath("config/" + configName + "/peripheral/ram/")
        ramSourceFile.setType("SOURCE")
        ramSourceFile.setMarkup(True)

        # System Definition
        ramSystemDefFile = ramComponent.createFileSymbol("RAM_SYS_DEF", None)
        ramSystemDefFile.setType("STRING")
        ramSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        ramSystemDefFile.setSourcePath("../peripheral/ram/templates/system/definitions.h.ftl")
        ramSystemDefFile.setMarkup(True)
