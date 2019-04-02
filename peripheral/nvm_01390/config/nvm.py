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

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

def nvmSetMemoryDependency(symbol, event):
    symbol.setVisible(event["value"])

def setNVMInterruptData(status):

    Database.setSymbolValue("core", nvmInterruptVector, status, 1)
    Database.setSymbolValue("core", nvmInterruptHandlerLock, status, 1)

    if status == True:
        Database.setSymbolValue("core", nvmInterruptHandler, nvmInstanceName.getValue() + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", nvmInterruptHandler, "FCE_Handler", 1)

def updateNVMInterruptData(symbol, event):

    if event["id"] == "INTERRUPT_ENABLE":
        setNVMInterruptData(event["value"])

    if nvmInterruptEnable.getValue() == True and Database.getSymbolValue("core", nvmInterruptVectorUpdate) == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    return regName, str(bitPosn)

def getIRQnumber(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("name"))

            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

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

    nvmFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"code\"]")

    ##### Do not modify below symbol names as they are used by Memory Driver #####

    flashStartAddress = nvmFlashNode.getAttribute("start")

    #Convert Physical Address to Virtual Address 0x1Dxxxxx to 0x9Dxxxx
    flashStartAddress = flashStartAddress[:2] + flashStartAddress[2:].replace('1', '9')

    #Flash Address
    nvmSym_FLASH_ADDRESS = nvmComponent.createStringSymbol("FLASH_START_ADDRESS", None)
    nvmSym_FLASH_ADDRESS.setVisible(False)
    nvmSym_FLASH_ADDRESS.setDefaultValue(flashStartAddress)

    #Flash size
    nvmSym_FLASH_SIZE = nvmComponent.createStringSymbol("FLASH_SIZE", None)
    nvmSym_FLASH_SIZE.setVisible(False)
    nvmSym_FLASH_SIZE.setDefaultValue(nvmFlashNode.getAttribute("size"))

    nvmParamNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"NVM\"]/instance@[name=\"" + nvmInstanceName.getValue() + "\"]/parameters")

    pageSize = "4096"
    rowSize = "512"

    if nvmParamNode != None:
        param_values = []
        param_values = nvmParamNode.getChildren()
        for index in range(0, len(param_values)):
            if "PAGE_SIZE" in param_values[index].getAttribute("name"):
                pageSize = param_values[index].getAttribute("value")

            if "ROW_SIZE" in param_values[index].getAttribute("name"):
                rowSize = param_values[index].getAttribute("value")

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

    nvmOffset = int(flashStartAddress,16) + offsetStart
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

    # Get register names, mask values, bit shifts based on vector number
    nvmInterruptVector = "FCE_INTERRUPT_ENABLE"
    nvmInterruptHandler = "FCE_INTERRUPT_HANDLER"
    nvmInterruptHandlerLock = "FCE_INTERRUPT_HANDLER_LOCK"
    nvmInterruptVectorUpdate = "FCE_INTERRUPT_ENABLE_UPDATE"
    nvmIrq_index = int(getIRQnumber("FCE"))

    #Configures the library for interrupt mode operations
    nvmInterruptEnable = nvmComponent.createBooleanSymbol("INTERRUPT_ENABLE", None)
    nvmInterruptEnable.setLabel("Enable Interrupt?")
    nvmInterruptEnable.setDefaultValue(True)

    nvmInterruptComment = nvmComponent.createCommentSymbol("NVM_INTRRUPT_ENABLE_COMMENT", None)
    nvmInterruptComment.setLabel("Warning!!! " + nvmInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    nvmInterruptComment.setVisible(False)
    nvmInterruptComment.setDependencies(updateNVMInterruptData, ["INTERRUPT_ENABLE", "core." + nvmInterruptVectorUpdate])

    setNVMInterruptData(True)

    enblRegName, enblBitPosn = _get_enblReg_parms(nvmIrq_index)
    statRegName, statBitPosn = _get_statReg_parms(nvmIrq_index)

    # Below create family-specific register names / masking needed by ftl file
    nvmEnblRegWrt = nvmComponent.createStringSymbol("NVM_IEC_REG", None)
    nvmEnblRegWrt.setDefaultValue(enblRegName)
    nvmEnblRegWrt.setVisible(False)

    nvmEnblRegVal = nvmComponent.createStringSymbol("NVM_IEC_REG_VALUE", None)
    nvmEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
    nvmEnblRegVal.setVisible(False)

    nvmStatRegRd = nvmComponent.createStringSymbol("NVM_IFS_REG", None)
    nvmStatRegRd.setDefaultValue(statRegName)
    nvmStatRegRd.setVisible(False)

    nvmStatRegShiftVal = nvmComponent.createStringSymbol("NVM_IFS_REG_VALUE", None)
    nvmStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
    nvmStatRegShiftVal.setVisible(False)

    nvmVectorNum = nvmComponent.createIntegerSymbol("NVM_VECTOR_NUMBER", None)
    nvmVectorNum.setDefaultValue(nvmIrq_index)
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
    nvmSym_HeaderFile.setSourcePath("../peripheral/nvm_01390/templates/plib_nvm.h.ftl")
    nvmSym_HeaderFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".h")
    nvmSym_HeaderFile.setDestPath("/peripheral/nvm/")
    nvmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_HeaderFile.setType("HEADER")
    nvmSym_HeaderFile.setMarkup(True)

    nvmSym_SourceFile = nvmComponent.createFileSymbol("NVM_SOURCE", None)
    nvmSym_SourceFile.setSourcePath("../peripheral/nvm_01390/templates/plib_nvm.c.ftl")
    nvmSym_SourceFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".c")
    nvmSym_SourceFile.setDestPath("/peripheral/nvm/")
    nvmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_SourceFile.setType("SOURCE")
    nvmSym_SourceFile.setMarkup(True)

    nvmSystemDefFile = nvmComponent.createFileSymbol("NVM_SYS_DEF", None)
    nvmSystemDefFile.setSourcePath("../peripheral/nvm_01390/templates/system/definitions.h.ftl")
    nvmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmSystemDefFile.setType("STRING")
    nvmSystemDefFile.setMarkup(True)
