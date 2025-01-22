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

global nvmInstanceName

CORE = "core"
NVM_INTERRUPT = "NVMInterrupt"
INTERRUPT_ENABLE = "INTERRUPT_ENABLE"

def nvmSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])


def interruptStatusWarning(symbol, event):

    if symbol.getComponent().getSymbolValue(INTERRUPT_ENABLE) == True:
        symbol.setVisible(not event["value"])
    else:
        symbol.setVisible(False)

def handleInterruptControl(intMode):
    intIndex = getVectorIndex(NVM_INTERRUPT)

    if intMode == True:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), True)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), True)
    else:
        Database.setSymbolValue("core", "INTC_{}_ENABLE".format(intIndex), False)
        Database.setSymbolValue("core", "INTC_{}_HANDLER_LOCK".format(intIndex), False)

def defaultInterruptControl(component):

    intMode = component.getSymbolValue(INTERRUPT_ENABLE)

    handleInterruptControl(intMode)

def interruptControlHelper(symbol, event):

    intMode = event["value"]
    handleInterruptControl(intMode)

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    vectorIndex = -1
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vectorIndex = param.getAttribute("index")
            break

    return vectorIndex

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(nvmComponent):

    global nvmInstanceName
    global nvmInterruptVector
    global nvmInterruptHandlerLock
    global nvmInterruptHandler
    global nvmInterruptVectorUpdate
    global nvmInterruptEnable

    nvmInstanceName = nvmComponent.createStringSymbol("NVM_INSTANCE_NAME", None)
    nvmInstanceName.setVisible(False)
    nvmInstanceName.setDefaultValue(nvmComponent.getID().upper())
    Log.writeInfoMessage("Running " + nvmInstanceName.getValue())

    flashStartAddress = 0
    flashSize = 0
    flashStartAddressHexStr = "0x"
    flashSizeHexStr = "0x"
    addressSpaceChildren = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces").getChildren()

    for addressSpaceIndex in range(0, len(addressSpaceChildren)):
        memSegmentChilren  = addressSpaceChildren[addressSpaceIndex].getChildren()
        for memSegIndex in range(0,  len(memSegmentChilren)):
           memSeg    = memSegmentChilren[memSegIndex].getAttribute("name")
           memType    = memSegmentChilren[memSegIndex].getAttribute("type")

           if (((memType == "flash")) and (memSeg == "program")):
              flashStartAddressHexStr = memSegmentChilren[memSegIndex].getAttribute("start")
              flashStartAddress = int(flashStartAddressHexStr, 16)
              flashSizeHexStr = memSegmentChilren[memSegIndex].getAttribute("size")
              flashSize  = int(flashSizeHexStr, 16)


    ##### Do not modify below symbol names as they are used by Memory Driver #####

    #Flash Address
    nvmSym_FLASH_ADDRESS = nvmComponent.createStringSymbol("FLASH_START_ADDRESS", None)
    nvmSym_FLASH_ADDRESS.setVisible(False)
    nvmSym_FLASH_ADDRESS.setDefaultValue(flashStartAddressHexStr)

    #Flash size
    nvmSym_FLASH_SIZE = nvmComponent.createStringSymbol("FLASH_SIZE", None)
    nvmSym_FLASH_SIZE.setVisible(False)
    nvmSym_FLASH_SIZE.setDefaultValue(flashSizeHexStr)

    nvmParamNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"nvm\"]/instance@[name=\"" + nvmInstanceName.getValue() + "\"]/parameters")

    pageSize = "1024"
    rowSize = "128"
    wordWriteOpcode = ""
    rowWriteOpcode = ""
    pageEraseOpcode = ""

    if nvmParamNode != None:
        param_values = []
        param_values = nvmParamNode.getChildren()
        for index in range(0, len(param_values)):
            if "FLASH_ERASE_PAGE_SIZE_IN_INSTRUCTIONS" in param_values[index].getAttribute("name"):
                pageSize = param_values[index].getAttribute("value")

            if "FLASH_WRITE_ROW_SIZE_IN_INSTRUCTIONS" in param_values[index].getAttribute("name"):
                rowSize = param_values[index].getAttribute("value")

            if "FLASH_WORD_WRITE_OP_CODE" in param_values[index].getAttribute("name"):
                wordWriteOpcode = param_values[index].getAttribute("value")

            if "FLASH_WRITE_ROW_OP_CODE" in param_values[index].getAttribute("name"):
                rowWriteOpcode = param_values[index].getAttribute("value")

            if "FLASH_ERASE_PAGE_OP_CODE" in param_values[index].getAttribute("name"):
                pageEraseOpcode = param_values[index].getAttribute("value")

            if "FLASH_WORD_WRITE_SIZE_IN_INSTRUCTIONS" in param_values[index].getAttribute("name"):
                wordWriteSize = param_values[index].getAttribute("value")

            if "FLASH_ENDURANCE_MINIMUM" in param_values[index].getAttribute("name"):
                endurance = param_values[index].getAttribute("value")

        #Flash Row size
        nvmSym_FLASH_PROGRAM_SIZE = nvmComponent.createStringSymbol("FLASH_PROGRAM_SIZE", None)
        nvmSym_FLASH_PROGRAM_SIZE.setVisible(False)
        nvmSym_FLASH_PROGRAM_SIZE.setDefaultValue(rowSize)

        #Flash Page size
        nvmSym_ERASE_SIZE = nvmComponent.createStringSymbol("FLASH_ERASE_SIZE", None)
        nvmSym_ERASE_SIZE.setVisible(False)
        nvmSym_ERASE_SIZE.setDefaultValue(pageSize)

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    nvmSym_MemoryDriver = nvmComponent.createBooleanSymbol("DRV_MEMORY_CONNECTED", None)
    nvmSym_MemoryDriver.setLabel("Memory Driver Connected")
    nvmSym_MemoryDriver.setVisible(False)
    nvmSym_MemoryDriver.setDefaultValue(False)

    offsetStart = (int(nvmSym_FLASH_SIZE.getValue(),16) / 2)

    nvmOffset = flashStartAddress + offsetStart
    nvmOffset = format(nvmOffset, 'x')

    nvmSym_MemoryStartAddr = nvmComponent.createStringSymbol("START_ADDRESS", None)
    nvmSym_MemoryStartAddr.setLabel("NVM Media Start Address")
    nvmSym_MemoryStartAddr.setVisible(False)
    nvmSym_MemoryStartAddr.setDefaultValue(nvmOffset)
    nvmSym_MemoryStartAddr.setDependencies(nvmSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    memMediaSizeKB = (offsetStart / 1024)

    nvmSym_MemoryMediaSize = nvmComponent.createIntegerSymbol("MEMORY_MEDIA_SIZE", None)
    nvmSym_MemoryMediaSize.setLabel("NVM Media Size (KB)")
    nvmSym_MemoryMediaSize.setVisible(False)
    nvmSym_MemoryMediaSize.setDefaultValue(memMediaSizeKB)
    nvmSym_MemoryMediaSize.setDependencies(nvmSetMemoryDependency, ["DRV_MEMORY_CONNECTED"])

    nvmSym_MemoryEraseEnable = nvmComponent.createBooleanSymbol("ERASE_ENABLE", None)
    nvmSym_MemoryEraseEnable.setLabel("NVM Erase Enable")
    nvmSym_MemoryEraseEnable.setVisible(False)
    nvmSym_MemoryEraseEnable.setDefaultValue(True)
    nvmSym_MemoryEraseEnable.setReadOnly(True)

    nvmSym_MemoryEraseBufferSize = nvmComponent.createIntegerSymbol("ERASE_BUFFER_SIZE", None)
    nvmSym_MemoryEraseBufferSize.setLabel("NVM Erase Buffer Size")
    nvmSym_MemoryEraseBufferSize.setVisible(False)
    nvmSym_MemoryEraseBufferSize.setDefaultValue(int(nvmSym_ERASE_SIZE.getValue()))
    nvmSym_MemoryEraseBufferSize.setDependencies(nvmSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    nvmSym_MemoryEraseComment = nvmComponent.createCommentSymbol("ERASE_COMMENT", None)
    nvmSym_MemoryEraseComment.setVisible(False)
    nvmSym_MemoryEraseComment.setLabel("*** Should be equal to Page Erase Size ***")
    nvmSym_MemoryEraseComment.setDependencies(nvmSetMemoryDependency, ["DRV_MEMORY_CONNECTED", "ERASE_ENABLE"])

    ################# Interrupt Settings ###########################
    nvmInterruptEnable = nvmComponent.createBooleanSymbol(INTERRUPT_ENABLE, None)
    nvmInterruptEnable.setLabel("Enable Interrrupt")
    nvmInterruptEnable.setDefaultValue(True)
    nvmInterruptEnable.setDependencies(interruptControlHelper, [INTERRUPT_ENABLE])

    defaultInterruptControl(nvmInterruptEnable.getComponent())

    nvmVectorNumber = int(getVectorIndex(NVM_INTERRUPT))
    nvmInterruptComment = nvmComponent.createCommentSymbol("NVM_INTRRUPT_ENABLE_COMMENT", None)
    nvmInterruptComment.setVisible(
        not bool(Database.getSymbolValue(CORE, "INTC_{}_ENABLE".format(str(nvmVectorNumber))))
    )
    nvmInterruptComment.setLabel(
        "Warning!!! Enable NVM Interrupt in Interrupts Section of System module"
    )
    nvmInterruptComment.setDependencies(
        interruptStatusWarning, ["core." + "INTC_" + str(nvmVectorNumber) + "_ENABLE"]
    )


    nvmInterruptHandler = nvmComponent.createStringSymbol("NVM_INTERRUPT_HANDLER", None)
    nvmInterruptHandler.setDefaultValue(
        Database.getSymbolValue(CORE, "INTC_{}_INTERRUPT_HANDLER".format(str(nvmVectorNumber)))
    )
    nvmInterruptHandler.setVisible(False)


    # FTL related data
    nvmRowWriteOpcode = nvmComponent.createStringSymbol("NVM_ROW_WRITE_OPCODE", None)
    nvmRowWriteOpcode.setDefaultValue(rowWriteOpcode)
    nvmRowWriteOpcode.setVisible(False)

    nvmWordWriteOpcode = nvmComponent.createStringSymbol("NVM_WORD_WRITE_OPCODE", None)
    nvmWordWriteOpcode.setDefaultValue(wordWriteOpcode)
    nvmWordWriteOpcode.setVisible(False)

    nvmPageEraseOpcode = nvmComponent.createStringSymbol("NVM_PAGE_ERASE_OPCODE", None)
    nvmPageEraseOpcode.setDefaultValue(pageEraseOpcode)
    nvmPageEraseOpcode.setVisible(False)

    nvmWordWriteSize = nvmComponent.createStringSymbol("NVM_WORD_WRITE_SIZE", None)
    nvmWordWriteSize.setDefaultValue(wordWriteSize)
    nvmWordWriteSize.setVisible(False)

    nvmEndurance = nvmComponent.createStringSymbol("NVM_ENDURANCE", None)
    nvmEndurance.setDefaultValue(endurance)
    nvmEndurance.setVisible(False)


    # Below create family-specific register names / masking needed by ftl file
    nvmVectorNum = nvmComponent.createIntegerSymbol("NVM_VECTOR_NUMBER", None)
    nvmVectorNum.setDefaultValue(nvmVectorNumber)
    nvmVectorNum.setVisible(False)

    writeApiName = nvmComponent.getID().upper() + "_RowWrite"
    eraseApiName = nvmComponent.getID().upper() + "_PageErase"

    nvmWriteApiName = nvmComponent.createStringSymbol("WRITE_API_NAME", None)
    nvmWriteApiName.setVisible(False)
    nvmWriteApiName.setReadOnly(True)
    nvmWriteApiName.setDefaultValue(writeApiName)

    nvmEraseApiName = nvmComponent.createStringSymbol("ERASE_API_NAME", None)
    nvmEraseApiName.setVisible(False)
    nvmEraseApiName.setReadOnly(True)
    nvmEraseApiName.setDefaultValue(eraseApiName)

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmSym_HeaderFile = nvmComponent.createFileSymbol("NVM_HEADER", None)
    nvmSym_HeaderFile.setSourcePath("../peripheral/nvm_04549/templates/plib_nvm.h.ftl")
    nvmSym_HeaderFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".h")
    nvmSym_HeaderFile.setDestPath("/peripheral/nvm/")
    nvmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_HeaderFile.setType("HEADER")
    nvmSym_HeaderFile.setMarkup(True)

    nvmSym_SourceFile = nvmComponent.createFileSymbol("NVM_SOURCE", None)
    nvmSym_SourceFile.setSourcePath("../peripheral/nvm_04549/templates/plib_nvm.c.ftl")
    nvmSym_SourceFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".c")
    nvmSym_SourceFile.setDestPath("/peripheral/nvm/")
    nvmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_SourceFile.setType("SOURCE")
    nvmSym_SourceFile.setMarkup(True)

    nvmSystemDefFile = nvmComponent.createFileSymbol("NVM_SYS_DEF", None)
    nvmSystemDefFile.setSourcePath("../peripheral/nvm_04549/templates/system/definitions.h.ftl")
    nvmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmSystemDefFile.setType("STRING")
    nvmSystemDefFile.setMarkup(True)

    nvmSystemInitFile = nvmComponent.createFileSymbol("NVM_SYS_INIT", None)
    nvmSystemInitFile.setSourcePath("../peripheral/nvm_04549/templates/system/initialization.c.ftl")
    nvmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    nvmSystemInitFile.setType("STRING")
    nvmSystemInitFile.setMarkup(True)
