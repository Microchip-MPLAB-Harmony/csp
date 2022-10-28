# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2018 Microchip Technology Inc. and its subsidiaries.
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

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("CEC_173X")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M4 Configuration")
cortexMenu.setDescription("Configuration for Cortex M4")

# periInstanceMultiVectorSupport = coreComponent.createBooleanSymbol("PERIPHERAL_MULTI_VECTOR", None)
# periInstanceMultiVectorSupport.setDefaultValue(True)
# periInstanceMultiVectorSupport.setVisible(False)

# def getCorePeripherals():

    # # Components which are creating critical section
    # corePeripherals = ["DMAC", "I2S", "RTC", "TC", "SERCOM"]

    # return corePeripherals

# def setDMACDefaultSettings():

    # triggerSettings = {
                        # "Software Trigger"  : ["BLOCK", "INCREMENTED_AM", "INCREMENTED_AM", "WORD"],
                        # "Standard_Transmit" : ["BEAT", "INCREMENTED_AM", "FIXED_AM", "BYTE"],
                        # "Standard_Receive"  : ["BEAT", "FIXED_AM", "INCREMENTED_AM", "BYTE"]
                    # }

    # return triggerSettings


def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"              : ["MPU_ATTR_NORMAL_WT",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00000000",   "4MB"   ],
                    "SRAM"              : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "8MB"],
                    "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                    "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ],
                    "QSPI"              : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x04000000",   "256MB"],}
    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM", "QSPI"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList

# # load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_26/config/gpio.py")
coreComponent.addPlugin("../peripheral/gpio_26/plugin/gpio_26.jar")

# # # load clock
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pcr_cec_173x/config/pcr.py")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/ecia_200/config/ecia.py")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "NVIC_MANAGER_SG3", {"plugin_name": "NVIC Configuration", "main_html_path": "../csp/peripheral/nvic/plugin/sg3_interupt_manager/build/index.html"})

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# #load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")


# # load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dma_85/config/dma.py")
#coreComponent.addPlugin("../peripheral/dma_85/plugin/dmamanager.jar")

global armLibCSourceFile
global compilerSpecifics
compilerSelected = compilerChoice.getSelectedKey().lower()

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("../arch/arm/templates/" + compilerSelected + "/cortex_m/startup/startup_" + compilerSelected + ".c.ftl")
armSysStartSourceFile.setOutputName("startup_" + compilerSelected + ".c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setDependencies(
    genSysSourceFile, ["CoreSysStartupFile", "CoreSysFiles"])

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")
armLibCSourceFile.setDependencies(genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])

compilerSpecifics = [armSysStartSourceFile]