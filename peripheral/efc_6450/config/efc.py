#Function for initiating the UI

global instance
global peripId
global NVICVector
global NVICHandler
global NVICHandlerLock

def efcSetMemoryDependency(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def NVICControl(NVIC, event):
    global NVICVector
    global NVICHandler
    global NVICHandlerLock
    Database.clearSymbolValue("core", NVICVector)
    Database.clearSymbolValue("core", NVICHandler)
    Database.clearSymbolValue("core", NVICHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", NVICVector, True, 2)
        Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_InterruptHandler", 2)
        Database.setSymbolValue("core", NVICHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", NVICVector, False, 2)
        Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_Handler", 2)
        Database.setSymbolValue("core", NVICHandlerLock, False, 2)

def instantiateComponent(efcComponent):

    global instance
    global peripId
    global NVICVector
    global NVICHandler
    global NVICHandlerLock

    instance = efcComponent.getID()[-1:]

    Log.writeInfoMessage("Running EEFC")

    #Create the top menu
    efcMenu = efcComponent.createMenuSymbol(None, None)
    efcMenu.setLabel("Hardware Settings ")

    #Flash Details
    efcFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"IFLASH\"]")
    if efcFlashNode != None:
        efcFlashStartAddress = efcComponent.createStringSymbol("FLASH_START_ADDRESS", efcMenu)
        efcFlashStartAddress.setVisible(False)
        efcFlashStartAddress.setDefaultValue(efcFlashNode.getAttribute("start"))

        #Flash size
        efcFlashSize = efcComponent.createStringSymbol("FLASH_SIZE", efcMenu)
        efcFlashSize.setVisible(False)
        efcFlashSize.setDefaultValue(efcFlashNode.getAttribute("size"))

        #Flash Page size
        efcFlashProgramSize = efcComponent.createStringSymbol("FLASH_PROGRAM_SIZE", efcMenu)
        efcFlashProgramSize.setVisible(False)
        efcFlashProgramSize.setDefaultValue(efcFlashNode.getAttribute("pagesize"))

    #Flash Erase size
    efcFlashEraseSize = efcComponent.createStringSymbol("FLASH_ERASE_SIZE", efcMenu)
    efcFlashEraseSize.setVisible(False)
    efcFlashEraseSize.setDefaultValue("8192")

    #Create a Checkbox to enable disable interrupts
    efcInterrupt = efcComponent.createBooleanSymbol("INTERRUPT_ENABLE", efcMenu)
    efcInterrupt.setLabel("Enable Interrupts")
    efcInterrupt.setDefaultValue(True)

    efcInterruptSource = efcComponent.createStringSymbol("INTERRUPT_SOURCE", efcMenu)
    efcInterruptSource.setLabel("EFC Interrupt Source")
    efcInterruptSource.setReadOnly(True)
    efcInterruptSource.setDefaultValue("EFC_IRQn")
    efcInterruptSource.setDependencies(efcSetMemoryDependency, ["INTERRUPT_ENABLE"])

    efcMemoryDriver = efcComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", efcMenu)
    efcMemoryDriver.setLabel("Memory Driver Connected")
    efcMemoryDriver.setVisible(False)
    efcMemoryDriver.setDefaultValue(False)

    efcMemoryStartAddr = efcComponent.createHexSymbol("START_ADDRESS", efcMenu)
    efcMemoryStartAddr.setLabel("NVM Offset for File System")
    efcMemoryStartAddr.setVisible(False)
    efcMemoryStartAddr.setDefaultValue(0x500000)
    efcMemoryStartAddr.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    efcMemoryEraseEnable = efcComponent.createBooleanSymbol("ERASE_ENABLE", None)
    efcMemoryEraseEnable.setLabel("NVM Erase Enable")
    efcMemoryEraseEnable.setVisible(False)
    efcMemoryEraseEnable.setDefaultValue(True)
    efcMemoryEraseEnable.setReadOnly(True)

    efcMemoryEraseBufferSize = efcComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", efcMenu)
    efcMemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    efcMemoryEraseBufferSize.setVisible(False)
    efcMemoryEraseBufferSize.setDefaultValue(8192)
    efcMemoryEraseBufferSize.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    efcMemoryEraseComment = efcComponent.createCommentSymbol("ERASE_COMMENT", efcMenu)
    efcMemoryEraseComment.setVisible(False)
    efcMemoryEraseComment.setLabel("*** Should be equal to Sector Erase Size ***")
    efcMemoryEraseComment.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    efcMemoryMediaSize = efcComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", efcMenu)
    efcMemoryMediaSize.setLabel("NVM Memory Media Size")
    efcMemoryMediaSize.setVisible(False)
    efcMemoryMediaSize.setDefaultValue(1024)
    efcMemoryMediaSize.setDependencies(efcSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    #instance index
    efcIndex = efcComponent.createIntegerSymbol("INDEX", efcMenu)
    efcIndex.setVisible(False)
    efcIndex.setDefaultValue(int(instance))

    writeApiName = "EFC" + str(instance) + "_PageWrite"
    eraseApiName = "EFC" + str(instance) + "_SectorErase"

    efcWriteApiName = efcComponent.createStringSymbol("WRITE_API_NAME", efcMenu)
    efcWriteApiName.setVisible(False)
    efcWriteApiName.setReadOnly(True)
    efcWriteApiName.setDefaultValue(writeApiName)

    efcEraseApiName = efcComponent.createStringSymbol("ERASE_API_NAME", efcMenu)
    efcEraseApiName.setVisible(False)
    efcEraseApiName.setReadOnly(True)
    efcEraseApiName.setDefaultValue(eraseApiName)

    peripId = Interrupt.getInterruptIndex("EFC")
    NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"

    Database.clearSymbolValue("core", NVICVector)
    Database.setSymbolValue("core", NVICVector, True, 2)
    Database.clearSymbolValue("core", NVICHandler)
    Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_InterruptHandler", 2)
    Database.clearSymbolValue("core", NVICHandlerLock)
    Database.setSymbolValue("core", NVICHandlerLock, True, 2)

    # NVIC Dynamic settings
    efcNVICControl = efcComponent.createBooleanSymbol("NVIC_EFC_ENABLE", None)
    efcNVICControl.setDependencies(NVICControl, ["INTERRUPT_ENABLE"])
    efcNVICControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")
    #Generate Output Header
    efcHeaderFile = efcComponent.createFileSymbol("EFC_FILE_0", None)
    efcHeaderFile.setSourcePath("../peripheral/efc_6450/templates/plib_efc.h.ftl")
    efcHeaderFile.setMarkup(True)
    efcHeaderFile.setOutputName("plib_efc" + str(instance) + ".h")
    efcHeaderFile.setOverwrite(True)
    efcHeaderFile.setDestPath("peripheral/efc/")
    efcHeaderFile.setProjectPath("config/" + configName + "/peripheral/efc/")
    efcHeaderFile.setType("HEADER")
    #Generate Output source
    efcSourceFile = efcComponent.createFileSymbol("EFC_FILE_1", None)
    efcSourceFile.setSourcePath("../peripheral/efc_6450/templates/plib_efc.c.ftl")
    efcSourceFile.setMarkup(True)
    efcSourceFile.setOutputName("plib_efc" + str(instance) + ".c")
    efcSourceFile.setOverwrite(True)
    efcSourceFile.setDestPath("peripheral/efc/")
    efcSourceFile.setProjectPath("config/" + configName + "/peripheral/efc/")
    efcSourceFile.setType("SOURCE")

    efcSystemDefFile = efcComponent.createFileSymbol("EFC_FILE_2", None)
    efcSystemDefFile.setType("STRING")
    efcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    efcSystemDefFile.setSourcePath("../peripheral/efc_6450/templates/system/system_definitions.h.ftl")
    efcSystemDefFile.setMarkup(True)

def destroyComponent(efcComponent):

    global instance
    global NVICVector
    global NVICHandler
    global NVICHandlerLock

    Database.setSymbolValue("core", NVICVector, False, 2)
    Database.setSymbolValue("core", NVICHandler, "EFC" + str(instance) + "_Handler", 2)
    Database.setSymbolValue("core", NVICHandlerLock, False, 2)

