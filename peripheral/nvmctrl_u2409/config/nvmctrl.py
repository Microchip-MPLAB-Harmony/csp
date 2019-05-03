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

###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
global waitStates

def updateNVICFlashInterruptState(symbol, event):
    Database.setSymbolValue("core", InterruptVector[0], event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock[0], event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler[0], nvmctrlInstanceName.getValue()+ "_Main_Interrupt_Handler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler[0], "NVMCTRL_0_Handler", 2)

def updateNVICSmartEEPInterruptState(symbol, event):
    Database.setSymbolValue("core", InterruptVector[1], event["value"], 2)
    Database.setSymbolValue("core", InterruptHandlerLock[1], event["value"], 2)

    if event["value"] == True:
        Database.setSymbolValue("core", InterruptHandler[1], nvmctrlInstanceName.getValue()+ "_SmartEEPROM_Interrupt_Handler", 2)
    else:
        Database.setSymbolValue("core", InterruptHandler[1], "NVMCTRL_1_Handler", 2)

def updateNVMCTRLInterruptWarringStatus(symbol, event):

    if nvmctrlSym_Interrupt0.getValue() == True:
        symbol.setVisible(event["value"])

def nvmctlrSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])

def waitStateUpdate(symbol, event):
    global waitStates
    cpuFreq = event["value"]
    for key in sorted(waitStates.keys()):
        if int(cpuFreq) <= int(key):
            symbol.setValue(waitStates.get(key), 2)
            break
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(nvmctrlComponent):

    global InterruptVector
    InterruptVector = []
    global InterruptHandler
    InterruptHandler = []
    global InterruptHandlerLock
    InterruptHandlerLock = []
    global InterruptVectorUpdate
    InterruptVectorUpdate = []
    global nvmctrlInstanceName
    global nvmctrlSym_Interrupt0

    global waitStates
    waitStates = {}
    waitStates = Database.sendMessage("core", "WAIT_STATES", waitStates)

    nvmctrlInstanceName = nvmctrlComponent.createStringSymbol("NVMCTRL_INSTANCE_NAME", None)
    nvmctrlInstanceName.setVisible(False)
    nvmctrlInstanceName.setDefaultValue(nvmctrlComponent.getID().upper())
    Log.writeInfoMessage("Running " + nvmctrlInstanceName.getValue())

    #Flash Address
    nvmctrlFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"FLASH\"]")
    if nvmctrlFlashNode != None:
        nvmctrlSym_FLASH_ADDRESS = nvmctrlComponent.createIntegerSymbol("FLASH_START_ADDRESS", None)
        nvmctrlSym_FLASH_ADDRESS.setVisible(False)
        nvmctrlSym_FLASH_ADDRESS.setDefaultValue(int(nvmctrlFlashNode.getAttribute("start"), 16))

        #Flash size
        nvmctrlSym_FLASH_SIZE = nvmctrlComponent.createIntegerSymbol("FLASH_SIZE", None)
        nvmctrlSym_FLASH_SIZE.setVisible(False)
        nvmctrlSym_FLASH_SIZE.setDefaultValue(int(nvmctrlFlashNode.getAttribute("size"), 16))

        #Flash Page size
        nvmctrlSym_FLASH_PROGRAM_SIZE = nvmctrlComponent.createIntegerSymbol("FLASH_PROGRAM_SIZE", None)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setVisible(False)
        nvmctrlSym_FLASH_PROGRAM_SIZE.setDefaultValue(int(nvmctrlFlashNode.getAttribute("pagesize")))


    #Other Parameters for NVMCTRL
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVMCTRL\"]/instance@[name=\""+nvmctrlInstanceName.getValue()+"\"]/parameters")
    nvmBlockSize = 0
    nvmFlashSize = 0
    parameters = []
    parameters = node.getChildren()
    for param in range (0, len(parameters)):
        if(parameters[param].getAttribute("name") == "BLOCK_SIZE"):
            nvmBlockSize = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "FLASH_SIZE"):
            nvmFlashSize = int(parameters[param].getAttribute("value"))

    #Flash Erase size
    nvmctrlSym_FLASH_ERASE_SIZE = nvmctrlComponent.createIntegerSymbol("FLASH_ERASE_SIZE", None)
    nvmctrlSym_FLASH_ERASE_SIZE.setVisible(False)
    nvmctrlSym_FLASH_ERASE_SIZE.setDefaultValue(nvmBlockSize)

    #Configures AUTOWS
    nvmctrlSym_CTRLA_AUTOWS = nvmctrlComponent.createBooleanSymbol("NVMCTRL_AUTOWS_ENABLE", None)
    nvmctrlSym_CTRLA_AUTOWS.setLabel("Enable Automatic Read-Wait-State for Flash")
    nvmctrlSym_CTRLA_AUTOWS.setDefaultValue(True)

    #Configures NVM power reduction mode
    nvmctrlSym_CTRLA_SLEEPPRM = nvmctrlComponent.createKeyValueSetSymbol("NVMCTRL_CTRLA_POWER_REDUCTION_MODE", None)
    nvmctrlSym_CTRLA_SLEEPPRM.setLabel("Power Reduction Mode During Sleep")

    nvmctrlSleepPrmNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"NVMCTRL\"]/value-group@[name=\"NVMCTRL_CTRLA__PRM\"]")
    nvmctrlSleepPrmValues = []
    nvmctrlSleepPrmValues = nvmctrlSleepPrmNode.getChildren()

    nvmctrlSleepPrmDefaultValue   = 0
    nvmctrlSleepPrmKeyDescription = ""

    waitState = 6
    cpuClkFreq = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")

    if cpuClkFreq != None:
        for key in sorted(waitStates.keys()):
            if int(cpuClkFreq) <= int(key):
                waitState = waitStates.get(key)
                break

    # Flash Read Wait State (RWS).
    nvm_rws = nvmctrlComponent.createIntegerSymbol("NVM_RWS", None)
    nvm_rws.setLabel("Wait States")
    nvm_rws.setDefaultValue(waitState)
    nvm_rws.setDependencies(waitStateUpdate, ["core.CPU_CLOCK_FREQUENCY"])

    for index in range (0 , len(nvmctrlSleepPrmValues)):
        nvmctrlSleepPrmKeyName = nvmctrlSleepPrmValues[index].getAttribute("name")

        if (nvmctrlSleepPrmKeyName == "SEMIAUTO"):
            nvmctrlSleepPrmDefaultValue = index
        nvmctrlSleepPrmKeyValue =  nvmctrlSleepPrmValues[index].getAttribute("value")
        nvmctrlSleepPrmKeyDescription = nvmctrlSleepPrmValues[index].getAttribute("name")
        nvmctrlSym_CTRLA_SLEEPPRM.addKey(nvmctrlSleepPrmKeyName , nvmctrlSleepPrmKeyValue , nvmctrlSleepPrmKeyDescription)

    nvmctrlSym_CTRLA_SLEEPPRM.setDefaultValue(nvmctrlSleepPrmDefaultValue)
    nvmctrlSym_CTRLA_SLEEPPRM.setOutputMode("Value")
    nvmctrlSym_CTRLA_SLEEPPRM.setDisplayMode("Description")

    #Disable AHB0 cache
    nvmctrlSym_CTRLA_CACHEDIS0 = nvmctrlComponent.createBooleanSymbol("NVMCTRL_AHB0_CACHE_DISABLE", None)
    nvmctrlSym_CTRLA_CACHEDIS0.setLabel("Disable NVM Line Cache for AHB0")

    #Disable AHB1 cache
    nvmctrlSym_CTRLA_CACHEDIS1 = nvmctrlComponent.createBooleanSymbol("NVMCTRL_AHB1_CACHE_DISABLE", None)
    nvmctrlSym_CTRLA_CACHEDIS1.setLabel("Disable NVM Line Cache for AHB1")

    #Enable interrupt for Flash operations
    nvmctrlSym_Interrupt0 = nvmctrlComponent.createBooleanSymbol("INTERRUPT_ENABLE", None)
    nvmctrlSym_Interrupt0.setLabel("Enable Interrupt")
    nvmctrlSym_Interrupt0.setDefaultValue(False)
    nvmctrlSym_Interrupt0.setDescription("Enables interrupt for command execution complete (DONE) condition. Rest of the interrupts need to be enabled via code")

    #Menu item for SmartEEPROM configurations
    nvmctrlSymSEEP = nvmctrlComponent.createMenuSymbol("SMARTEEP_CONFIGURATION", None)
    nvmctrlSymSEEP.setLabel("SmartEEPROM Configurations")

    #Enable interrupt for SmartEEPROM operations
    nvmctrlSym_Interrupt1 = nvmctrlComponent.createBooleanSymbol("NVM_INTERRUPT1_ENABLE", nvmctrlSymSEEP)
    nvmctrlSym_Interrupt1.setLabel("Enable Interrupt for SmartEEPROM")
    nvmctrlSym_Interrupt1.setDefaultValue(False)
    nvmctrlSym_Interrupt1.setDescription("Enables interrupt for 'SmartEEPROM sector full' (SEESFULL) condition. Rest of the interrupts need to be enabled via code")

    #Enable Buffered mode for SmartEEPROM
    nvmctrlSym_WMODE = nvmctrlComponent.createBooleanSymbol("NVM_WMODE_ENABLE", nvmctrlSymSEEP)
    nvmctrlSym_WMODE.setLabel("Enable Buffered Mode")
    nvmctrlSym_WMODE.setDefaultValue(False)

    #Automatic Page Reallocation Disable
    nvmctrlSym_APRDIS = nvmctrlComponent.createBooleanSymbol("NVM_APRDIS_ENABLE", nvmctrlSymSEEP)
    nvmctrlSym_APRDIS.setLabel("Disable Automatic Page Reallocation")
    nvmctrlSym_APRDIS.setDefaultValue(False)

    #WDT Configuration comment
    nvmctrlSym_FuseComment = nvmctrlComponent.createCommentSymbol("NVM_CONFIG_COMMENT", nvmctrlSymSEEP)
    nvmctrlSym_FuseComment.setLabel("Note: Configure SBLK and PSZ Fuses for SmartEEPROM using 'System' component")

    ############################################################################
    #### Configuration for Memory Driver ####
    ############################################################################

    #Configuration when interfaced with memory driver
    nvmctrlSym_MemoryDriver = nvmctrlComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    nvmctrlSym_MemoryDriver.setLabel("Memory Driver Connected")
    nvmctrlSym_MemoryDriver.setVisible(False)
    nvmctrlSym_MemoryDriver.setDefaultValue(False)

    offsetStart = (nvmctrlSym_FLASH_SIZE.getValue() / 2)

    nvmOffset = str(hex(nvmctrlSym_FLASH_ADDRESS.getValue() + offsetStart))

    nvmctrlSym_MemoryStartAddr = nvmctrlComponent.createStringSymbol("START_ADDRESS", None)
    nvmctrlSym_MemoryStartAddr.setLabel("NVM Media Start Address")
    nvmctrlSym_MemoryStartAddr.setVisible(False)
    nvmctrlSym_MemoryStartAddr.setDefaultValue(nvmOffset[2:])
    nvmctrlSym_MemoryStartAddr.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    nvmctrlSym_MemoryMediaSize = nvmctrlComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", None)
    nvmctrlSym_MemoryMediaSize.setLabel("NVM Media Size (KB)")
    nvmctrlSym_MemoryMediaSize.setVisible(False)
    nvmctrlSym_MemoryMediaSize.setDefaultValue(memMediaSizeKB)
    nvmctrlSym_MemoryMediaSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    nvmctrlSym_MemoryEraseEnable = nvmctrlComponent.createBooleanSymbol("ERASE_ENABLE", None)
    nvmctrlSym_MemoryEraseEnable.setLabel("NVM Erase Enable")
    nvmctrlSym_MemoryEraseEnable.setVisible(False)
    nvmctrlSym_MemoryEraseEnable.setDefaultValue(True)
    nvmctrlSym_MemoryEraseEnable.setReadOnly(True)

    nvmctrlSym_MemoryEraseBufferSize = nvmctrlComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", None)
    nvmctrlSym_MemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    nvmctrlSym_MemoryEraseBufferSize.setVisible(False)
    nvmctrlSym_MemoryEraseBufferSize.setDefaultValue(nvmBlockSize)
    nvmctrlSym_MemoryEraseBufferSize.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    nvmctrlSym_MemoryEraseComment = nvmctrlComponent.createCommentSymbol("ERASE_COMMENT", None)
    nvmctrlSym_MemoryEraseComment.setVisible(False)
    nvmctrlSym_MemoryEraseComment.setLabel("*** Should be equal to Block Erase Size ***")
    nvmctrlSym_MemoryEraseComment.setDependencies(nvmctlrSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    writeApiName = nvmctrlComponent.getID().upper() + "_PageWrite"
    eraseApiName = nvmctrlComponent.getID().upper() + "_BlockErase"

    nvmctrlWriteApiName = nvmctrlComponent.createStringSymbol("WRITE_API_NAME", None)
    nvmctrlWriteApiName.setVisible(False)
    nvmctrlWriteApiName.setReadOnly(True)
    nvmctrlWriteApiName.setDefaultValue(writeApiName)

    nvmctrlEraseApiName = nvmctrlComponent.createStringSymbol("ERASE_API_NAME", None)
    nvmctrlEraseApiName.setVisible(False)
    nvmctrlEraseApiName.setReadOnly(True)
    nvmctrlEraseApiName.setDefaultValue(eraseApiName)

    ############################################################################
    #### Dependency ####
    ############################################################################

    InterruptVector.append(nvmctrlInstanceName.getValue()+"_0_INTERRUPT_ENABLE")
    InterruptHandler.append(nvmctrlInstanceName.getValue()+"_0_INTERRUPT_HANDLER")
    InterruptHandlerLock.append(nvmctrlInstanceName.getValue()+"_0_INTERRUPT_HANDLER_LOCK")
    InterruptVectorUpdate.append(nvmctrlInstanceName.getValue()+"_0_INTERRUPT_ENABLE_UPDATE")

    InterruptVector.append(nvmctrlInstanceName.getValue()+"_1_INTERRUPT_ENABLE")
    InterruptHandler.append(nvmctrlInstanceName.getValue()+"_1_INTERRUPT_HANDLER")
    InterruptHandlerLock.append(nvmctrlInstanceName.getValue()+"_1_INTERRUPT_HANDLER_LOCK")
    InterruptVectorUpdate.append(nvmctrlInstanceName.getValue()+"_1_INTERRUPT_ENABLE_UPDATE")

    # Interrupt Dynamic settings
    nvmctrlSym_UpdateInterrupt0Status = nvmctrlComponent.createBooleanSymbol("NVMCTRL_INTERRUPT0_STATUS", None)
    nvmctrlSym_UpdateInterrupt0Status.setDependencies(updateNVICFlashInterruptState, ["INTERRUPT_ENABLE"])
    nvmctrlSym_UpdateInterrupt0Status.setVisible(False)

    # Interrupt Dynamic settings
    nvmctrlSym_UpdateInterrupt1Status = nvmctrlComponent.createBooleanSymbol("NVMCTRL_INTERRUPT1_STATUS", None)
    nvmctrlSym_UpdateInterrupt1Status.setDependencies(updateNVICSmartEEPInterruptState, ["NVM_INTERRUPT1_ENABLE"])
    nvmctrlSym_UpdateInterrupt1Status.setVisible(False)

    # Interrupt Warning status
    nvmctrlSym_IntEnComment = nvmctrlComponent.createCommentSymbol("NVMCTRL_NVM_INTERRUPT0_ENABLE_COMMENT", None)
    nvmctrlSym_IntEnComment.setVisible(False)
    nvmctrlSym_IntEnComment.setLabel("Warning!!! NVMCTRL Interrupt is Disabled in Interrupt Manager")
    nvmctrlSym_IntEnComment.setDependencies(updateNVMCTRLInterruptWarringStatus, ["core." + InterruptVectorUpdate[0]])

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmctrlSym_HeaderFile = nvmctrlComponent.createFileSymbol("NVMCTRL_HEADER", None)
    nvmctrlSym_HeaderFile.setSourcePath("../peripheral/nvmctrl_u2409/templates/plib_nvmctrl.h.ftl")
    nvmctrlSym_HeaderFile.setOutputName("plib_"+nvmctrlInstanceName.getValue().lower()+".h")
    nvmctrlSym_HeaderFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_HeaderFile.setType("HEADER")
    nvmctrlSym_HeaderFile.setMarkup(True)

    nvmctrlSym_SourceFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SOURCE", None)
    nvmctrlSym_SourceFile.setSourcePath("../peripheral/nvmctrl_u2409/templates/plib_nvmctrl.c.ftl")
    nvmctrlSym_SourceFile.setOutputName("plib_"+nvmctrlInstanceName.getValue().lower()+".c")
    nvmctrlSym_SourceFile.setDestPath("/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvmctrl/")
    nvmctrlSym_SourceFile.setType("SOURCE")
    nvmctrlSym_SourceFile.setMarkup(True)

    nvmctrlSym_SystemInitFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_INIT", None)
    nvmctrlSym_SystemInitFile.setSourcePath("../peripheral/nvmctrl_u2409/templates/system/initialization.c.ftl")
    nvmctrlSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    nvmctrlSym_SystemInitFile.setType("STRING")
    nvmctrlSym_SystemInitFile.setMarkup(True)

    nvmctrlSystemDefFile = nvmctrlComponent.createFileSymbol("NVMCTRL_SYS_DEF", None)
    nvmctrlSystemDefFile.setSourcePath("../peripheral/nvmctrl_u2409/templates/system/definitions.h.ftl")
    nvmctrlSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmctrlSystemDefFile.setType("STRING")
    nvmctrlSystemDefFile.setMarkup(True)
