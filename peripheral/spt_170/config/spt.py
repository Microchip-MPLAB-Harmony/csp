"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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

################################################################################
#### Register Information ####
################################################################################


################################################################################
#### Global Variables ####
################################################################################
global sptHostIEN_Dict
global sptECIEN_Dict
global sptLock_Dict
global sptInstanceNum

sptHostIEN_Dict = {}
sptECIEN_Dict = {}
sptLock_Dict = {}

sptHostIENRegDepList = []
sptECIENRegDepList = []
sptSysConfigDepList = []


################################################################################
#### Business Logic ####
################################################################################


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def setSPTECInterruptData(spt_ec_interrupt_name, status):

    Database.setSymbolValue("core", spt_ec_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", spt_ec_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", spt_ec_interrupt_name + "_INTERRUPT_HANDLER", spt_ec_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", spt_ec_interrupt_name + "_INTERRUPT_HANDLER", spt_ec_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateSPTEC(sptECInterruptType, sptMode):
    interruptNameDir = "SPT" + sptInstanceNum.getValue()
    interruptNameAgg = "SPT" + sptInstanceNum.getValue() + "_GRP"

    if sptMode == "Advanced":
        if sptECInterruptType == "AGGREGATE":
            setSPTECInterruptData(interruptNameDir, False)
            setSPTECInterruptData(interruptNameAgg, True)
        else:
            setSPTECInterruptData(interruptNameAgg, False)
            setSPTECInterruptData(interruptNameDir, True)
    else:
        setSPTECInterruptData(interruptNameAgg, False)
        setSPTECInterruptData(interruptNameDir, False)

def nvicInterruptUpdate(symbol, event):
    sptECInterruptType = event["source"].getSymbolByID("SPT_EC_INTERRUPT_TYPE").getSelectedKey()
    sptMode = event["source"].getSymbolByID("SPT_MODE").getValue()

    nvicInterruptUpdateSPTEC(sptECInterruptType, sptMode)

def sptHostIENRegUpdate(symbol, event):
    global sptHostIEN_Dict
    bit_mask = sptHostIEN_Dict[event["id"]]
    hostIENRegVal = symbol.getValue()
    if event["value"] == True:
        hostIENRegVal |= bit_mask
    else:
        hostIENRegVal &= ~bit_mask

    symbol.setValue(hostIENRegVal)

def sptECIENRegUpdate(symbol, event):
    global sptECIEN_Dict
    bit_mask = int(sptECIEN_Dict[event["id"]], 16)
    ecIENRegVal = symbol.getValue()
    if event["value"] == True:
        ecIENRegVal |= bit_mask
    else:
        ecIENRegVal &= ~bit_mask

    symbol.setValue(ecIENRegVal)

def sptSysCfgRegUpdate(symbol, event):
    global sptLock_Dict
    bit_mask = sptLock_Dict[event["id"]]
    sysCfgRegVal = symbol.getValue()
    if event["value"] == True or event["value"] == "Simple":
        sysCfgRegVal |= bit_mask
    else:
        sysCfgRegVal &= ~bit_mask

    symbol.setValue(sysCfgRegVal)

def sptAdvancedModeVisibility(symbol, event):
    symbol.setVisible(event["value"] == "Advanced")

def sptWireConfigUpdate(symbol, event):
    if event["value"] == "Simple":
        symbol.setReadOnly(True)
        symbol.setValue("Single")
    else:
        symbol.setReadOnly(False)
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(sptComponent):

    global instanceNum
    global sptInstanceNum
    global sptHostIEN_Dict
    global sptECIEN_Dict
    global sptLock_Dict

    sptInstanceName = sptComponent.createStringSymbol("SPT_INSTANCE_NAME", None)
    sptInstanceName.setVisible(False)
    sptInstanceName.setDefaultValue(sptComponent.getID().upper())
    Log.writeInfoMessage("Running " + sptInstanceName.getValue())

    sptInstanceNum = sptComponent.createStringSymbol("SPT_INSTANCE_NUM", None)
    sptInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(sptComponent.getID()))
    sptInstanceNum.setDefaultValue(instanceNum)

    sptMode = sptComponent.createComboSymbol("SPT_MODE", None, ["Simple", "Advanced"])
    sptMode.setLabel("Mode")
    sptMode.setDefaultValue("Advanced")
    sptLock_Dict["SPT_MODE"] = (1<<18)
    sptSysConfigDepList.append("SPT_MODE")

    sptWireConfig = sptComponent.createComboSymbol("SPT_WIRE_CONFIG", None, ["Single", "Quad"])
    sptWireConfig.setLabel("Wire Configuration")
    sptWireConfig.setDefaultValue("Single")
    sptWireConfig.setDependencies(sptWireConfigUpdate, ["SPT_MODE"])

    sptWaitTime = sptComponent.createIntegerSymbol("SPT_WAIT_TIME", None)
    sptWaitTime.setLabel("Wait Time")
    sptWaitTime.setMin(0)
    sptWaitTime.setMax(255)
    sptWaitTime.setDefaultValue(4)
    sptWaitTime.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    sptTARValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPT\"]/value-group@[name=\"SPT_SPI_CFG__TAR_TIM_SEL\"]").getChildren()

    sptTARTime = sptComponent.createKeyValueSetSymbol("SPT_TAR_TIME", None)
    sptTARTime.setLabel("Turn Around Time")
    for index in range(len(sptTARValues)):
        sptTARTime.addKey(sptTARValues[index].getAttribute("name"), sptTARValues[index].getAttribute("value"), sptTARValues[index].getAttribute("caption"))
    sptTARTime.setOutputMode("Value")
    sptTARTime.setDisplayMode("Description")
    sptTARTime.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    ## Interrupt Setup
    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "SPT" + sptInstanceNum.getValue()})

    # Interrupt type selection
    sptECInterruptType = sptComponent.createKeyValueSetSymbol("SPT_EC_INTERRUPT_TYPE", None)
    sptECInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        sptECInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        sptECInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    sptECInterruptType.setDefaultValue(0)
    sptECInterruptType.setDisplayMode("Description")
    sptECInterruptType.setOutputMode("Key")
    sptECInterruptType.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    # Trigger dependency when interrupt type changes
    sptECNVICUpdate = sptComponent.createBooleanSymbol("SPT_NVIC_INTERRUPT", None)
    sptECNVICUpdate.setVisible(False)
    sptECNVICUpdate.setDependencies(nvicInterruptUpdate, ["SPT_MODE", "SPT_EC_INTERRUPT_TYPE"])

    sptHostIENBitfields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPT\"]/register-group@[name=\"SPT\"]/register@[name=\"SPI_IEN\"]").getChildren()

    sptHostIEN = sptComponent.createMenuSymbol("SPT_HOST_IEN", None)
    sptHostIEN.setLabel("Host Interrupt Enable")
    sptHostIEN.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    for index in range(len(sptHostIENBitfields)):
        caption = sptHostIENBitfields[index].getAttribute("caption")
        caption = caption[len("Enable "):]
        caption = caption[:-len(" Interrupt to SPI Master.")]
        sptHostIEN_Dict["SPT_HOST_IEN_" + sptHostIENBitfields[index].getAttribute("name")] = int(sptHostIENBitfields[index].getAttribute("mask"), 16)
        sptHostIENx = sptComponent.createBooleanSymbol("SPT_HOST_IEN_" + sptHostIENBitfields[index].getAttribute("name"), sptHostIEN)
        sptHostIENx.setLabel(caption)
        sptHostIENx.setDefaultValue(False)
        sptHostIENx.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])
        sptHostIENRegDepList.append("SPT_HOST_IEN_" + sptHostIENBitfields[index].getAttribute("name"))


    sptECIENBitfields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPT\"]/register-group@[name=\"SPT\"]/register@[name=\"EC_IEN\"]").getChildren()

    sptECIEN = sptComponent.createMenuSymbol("SPT_EC_IEN", None)
    sptECIEN.setLabel("EC Interrupt Enable")
    sptECIEN.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    for index in range(len(sptECIENBitfields)):
        caption = sptECIENBitfields[index].getAttribute("caption")
        caption = caption[len("Enable "):]
        caption = caption[:-len(" Interrupt to EC.")]
        sptECIEN_Dict["SPT_EC_IEN_" + sptECIENBitfields[index].getAttribute("name")] = sptECIENBitfields[index].getAttribute("mask")
        sptECIENx = sptComponent.createBooleanSymbol("SPT_EC_IEN_" + sptECIENBitfields[index].getAttribute("name"), sptECIEN)
        sptECIENx.setLabel(caption)
        sptECIENx.setDefaultValue(False)
        sptECIENx.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])
        sptECIENRegDepList.append("SPT_EC_IEN_" + sptECIENBitfields[index].getAttribute("name"))

    sptSycCfgBitfields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"SPT\"]/register-group@[name=\"SPT\"]/register@[name=\"SYS_CFG\"]").getChildren()

    sptLockHostWrites = sptComponent.createMenuSymbol("SPT_LOCK_HOST_WRITES", None)
    sptLockHostWrites.setLabel("Lock Host writes to:")
    sptLockHostWrites.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])

    for index in range(len(sptSycCfgBitfields)):
        if "LOCK_" in sptSycCfgBitfields[index].getAttribute("name") and "LOCK_TEST_" not in sptSycCfgBitfields[index].getAttribute("name"):
            caption = sptSycCfgBitfields[index].getAttribute("caption")
            caption = caption[len("Lock "):]
            caption = caption[:-len(", write access from SPI Master.")]
            sptLock_Dict["SPT_" + sptSycCfgBitfields[index].getAttribute("name")] = int(sptSycCfgBitfields[index].getAttribute("mask"), 16)
            sptHostLockx = sptComponent.createBooleanSymbol("SPT_" + sptSycCfgBitfields[index].getAttribute("name"), sptLockHostWrites)
            sptHostLockx.setLabel(caption)
            sptHostLockx.setDefaultValue(False)
            sptHostLockx.setDependencies(sptAdvancedModeVisibility, ["SPT_MODE"])
            sptSysConfigDepList.append("SPT_" + sptSycCfgBitfields[index].getAttribute("name"))

    sptHostIENReg = sptComponent.createHexSymbol("SPT_SPI_HOST_IEN_REG", None)
    sptHostIENReg.setDefaultValue(0)
    sptHostIENReg.setVisible(False)
    sptHostIENReg.setDependencies(sptHostIENRegUpdate, sptHostIENRegDepList)

    sptECIENReg = sptComponent.createHexSymbol("SPT_SPI_EC_IEN_REG", None)
    sptECIENReg.setDefaultValue(0)
    sptECIENReg.setVisible(False)
    sptECIENReg.setDependencies(sptECIENRegUpdate, sptECIENRegDepList)

    sptSysCfgReg = sptComponent.createHexSymbol("SPT_SYS_CFG_REG", None)
    sptSysCfgReg.setDefaultValue(1<<16)
    sptSysCfgReg.setVisible(False)
    sptSysCfgReg.setDependencies(sptSysCfgRegUpdate, sptSysConfigDepList)

    # Default interrupt setup
    nvicInterruptUpdateSPTEC(sptECInterruptType.getValue(), sptMode.getValue())

    sptECIntSourceEnum_List = sptComponent.createListSymbol("SPT_EC_INT_SOURCE_ENUM_LIST", None)
    sptECIntSourceEnum_List.setVisible(False)

    sptECIntSourceEnums = sptComponent.createListEntrySymbol("SPT_EC_INT_SOURCE_ENUM", None)
    sptECIntSourceEnums.setTarget(sptInstanceName.getValue().lower() + ".SPT_EC_INT_SOURCE_ENUM_LIST")
    sptECIntSourceEnums.setVisible(False)

    for key in sptECIEN_Dict:
        val = sptECIEN_Dict[key]
        enum_value = "SPT_EC_INT_" + key[len("SPT_EC_IEN_"):] + " = " + str(val) + "," + "\n\r\t"
        sptECIntSourceEnums.addValue(enum_value)


    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    sptHeaderFile = sptComponent.createFileSymbol("SPT_COMMON_HEADER", None)
    sptHeaderFile.setSourcePath("../peripheral/spt_170/templates/plib_spt_common.h.ftl")
    sptHeaderFile.setOutputName("plib_spt_common.h")
    sptHeaderFile.setDestPath("peripheral/spt/")
    sptHeaderFile.setProjectPath("config/" + configName + "/peripheral/spt/")
    sptHeaderFile.setType("HEADER")
    sptHeaderFile.setMarkup(True)
    sptHeaderFile.setOverwrite(True)

    # Instance Header File
    sptCmnHeaderFile = sptComponent.createFileSymbol("SPT_HEADER1", None)
    sptCmnHeaderFile.setSourcePath("../peripheral/spt_170/templates/plib_spt.h.ftl")
    sptCmnHeaderFile.setOutputName("plib_" + sptInstanceName.getValue().lower() + ".h")
    sptCmnHeaderFile.setDestPath("/peripheral/spt/")
    sptCmnHeaderFile.setProjectPath("config/" + configName + "/peripheral/spt/")
    sptCmnHeaderFile.setType("HEADER")
    sptCmnHeaderFile.setMarkup(True)
    sptCmnHeaderFile.setOverwrite(True)

    # Instance Source File
    sptSourceFile = sptComponent.createFileSymbol("SPT_SOURCE", None)
    sptSourceFile.setSourcePath("../peripheral/spt_170/templates/plib_spt.c.ftl")
    sptSourceFile.setOutputName("plib_" + sptInstanceName.getValue().lower() + ".c")
    sptSourceFile.setDestPath("/peripheral/spt/")
    sptSourceFile.setProjectPath("config/" + configName + "/peripheral/spt/")
    sptSourceFile.setType("SOURCE")
    sptSourceFile.setMarkup(True)
    sptSourceFile.setOverwrite(True)

    sptSystemInitFile = sptComponent.createFileSymbol("SPT_SYS_INT", None)
    sptSystemInitFile.setType("STRING")
    sptSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sptSystemInitFile.setSourcePath("../peripheral/spt_170/templates/system/initialization.c.ftl")
    sptSystemInitFile.setMarkup(True)

    sptSystemDefFile = sptComponent.createFileSymbol("SPT_SYS_DEF", None)
    sptSystemDefFile.setType("STRING")
    sptSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sptSystemDefFile.setSourcePath("../peripheral/spt_170/templates/system/definitions.h.ftl")
    sptSystemDefFile.setMarkup(True)