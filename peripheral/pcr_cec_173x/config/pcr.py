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
global sleep_en_reg_mask_dic
sleep_en_reg_mask_dic = {}

global priv_en_reg_mask_dic
priv_en_reg_mask_dic = {}

def setProcessorClockFreq(symbol, event):
    print event["symbol"].getSelectedValue()
    symbol.setValue(96000000/int(event["symbol"].getSelectedValue(), 16))

def sleep_reg_val_update (symbol, event):
    mskVal = sleep_en_reg_mask_dic[event["id"]]
    if event["value"] == True:
        symbol.setValue(symbol.getValue() | mskVal)
    else:
        symbol.setValue(symbol.getValue() & ~mskVal)

def priv_reg_val_update (symbol, event):
    mskVal = priv_en_reg_mask_dic[event["id"]]
    if event["value"] == True:
        symbol.setValue(symbol.getValue() | mskVal)
    else:
        symbol.setValue(symbol.getValue() & ~mskVal)

clkMenu = coreComponent.createMenuSymbol("CEC173X_PCR_CLK_MENU", None)
clkMenu.setLabel("Clock")
clkMenu.setDescription("Configuration for Clock System Service")
#-----------------------------------
# pllRefClkValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/value-group@[name=\"PCR_PLL_REF__PLL_REF_SRC\"]").getChildren()

# pllReferenceClk = coreComponent.createKeyValueSetSymbol("PLL_REFERENCE_CLOCK", clkMenu)
# pllReferenceClk.setLabel("PLL Reference Clock")

# for id in range(len(pllRefClkValues)):
    # key = pllRefClkValues[id].getAttribute("name")
    # value = pllRefClkValues[id].getAttribute("value")
    # description = pllRefClkValues[id].getAttribute("caption")
    # pllReferenceClk.addKey(key, value, description)
    # if key == "INTERNAL_SILICON_OSC":
        # pllReferenceClk.setDefaultValue(id)

# pllReferenceClk.setOutputMode("Value")
# pllReferenceClk.setDisplayMode("Description")
#-----------------------------------
processorClkDivValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/value-group@[name=\"PCR_PROC_CLK_CTRL__DIV\"]").getChildren()
processorClkInitValue = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"PROC_CLK_CTRL\"]").getAttribute("initval")
processorClkInitValue = int(processorClkInitValue, 16)

processorClkDiv = coreComponent.createKeyValueSetSymbol("PROCESSOR_CLK_DIV", clkMenu)
processorClkDiv.setLabel("Processor Clock Divide")

for id in range(len(processorClkDivValues)):
    key = processorClkDivValues[id].getAttribute("name")
    value = processorClkDivValues[id].getAttribute("value")
    description = processorClkDivValues[id].getAttribute("caption")
    processorClkDiv.addKey(key, value, description)
    if int(value , 16) == processorClkInitValue:
        processorClkDiv.setDefaultValue(id)

processorClkDiv.setOutputMode("Value")
processorClkDiv.setDisplayMode("Description")

#-----------------------------------
slowClkDivideMaxValue = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"SLOW_CLK_CTRL\"]/bitfield@[name=\"DIV\"]").getAttribute("mask")
slowClkDivideMaxValue = int(slowClkDivideMaxValue, 16)

slowClkDivideInitialValue = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"SLOW_CLK_CTRL\"]").getAttribute("initval")
slowClkDivideInitialValue = int(slowClkDivideInitialValue, 16)

slowClkDivide = coreComponent.createIntegerSymbol("SLOW_CLK_DIVIDE", clkMenu)
slowClkDivide.setLabel("Slow Clock Divide (Configures the 100KHz clock domain)")
slowClkDivide.setMin(0)
slowClkDivide.setMax(slowClkDivideMaxValue)
slowClkDivide.setDefaultValue(slowClkDivideInitialValue)

#-----------------------------------
# per32KHzClkSelValues = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"VBAT\"]/value-group@[name=\"VBAT_CLK_EN__PRPHL_32KHZ_CLK\"]").getChildren()

# per32KHzClkSel = coreComponent.createKeyValueSetSymbol("PERIPHERAL_32KHZ_CLK_SEL", clkMenu)
# per32KHzClkSel.setLabel("Peripheral 32KHz Clock Source")

# for id in range(len(per32KHzClkSelValues)):
    # key = per32KHzClkSelValues[id].getAttribute("name")
    # value = per32KHzClkSelValues[id].getAttribute("value")
    # description = per32KHzClkSelValues[id].getAttribute("caption")
    # per32KHzClkSel.addKey(key, value, description)

# per32KHzClkSel.setDefaultValue(0)
# per32KHzClkSel.setOutputMode("Value")
# per32KHzClkSel.setDisplayMode("Description")

# Calculated Frequency Menu
calculatedFreq_Menu = coreComponent.createMenuSymbol("FREQ_MENU", clkMenu)
calculatedFreq_Menu.setLabel("Calculated Clock Frequencies")

clkSym_PROCESSOR_CLK_FREQ = coreComponent.createIntegerSymbol("CPU_CLOCK_FREQUENCY", calculatedFreq_Menu)
clkSym_PROCESSOR_CLK_FREQ.setLabel("CPU Clock Frequency")
clkSym_PROCESSOR_CLK_FREQ.setReadOnly(True)
clkSym_PROCESSOR_CLK_FREQ.setDefaultValue(96000000/int(processorClkDiv.getSelectedValue(), 16))
clkSym_PROCESSOR_CLK_FREQ.setDependencies(setProcessorClockFreq, ["PROCESSOR_CLK_DIV"])

#-------------------------------------------
################################################################################
###########             Header Enum Generation              ####################
################################################################################

blockSleepMenu = coreComponent.createMenuSymbol("CEC173X_PCR_SLEEP_MENU", None)
blockSleepMenu.setLabel("Block Sleep Config")

global sleep_en_reg_dep_list
sleep_en_reg_dep_list = []

global sleep_en_reg_macros_list
sleep_en_reg_macros_list = []
numRegs = 0

pcr_registers_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]").getChildren()
for id in range(len(pcr_registers_node)):
    register_name = pcr_registers_node[id].getAttribute("name")
    if "SLP_EN" in pcr_registers_node[id].getAttribute("name"):
        sleep_en_reg_macros_list.append([])
        sleep_en_reg_dep_list.append([])
        register_index = register_name[len("SLP_EN_"):]
        slpEnableRegIndex = coreComponent.createStringSymbol("PCR_SLEEP_ENABLE" + str(numRegs) + "_REG_INDEX", None)
        slpEnableRegIndex.setVisible(False)
        slpEnableRegIndex.setDefaultValue(register_index)
        slpEnableMenu = coreComponent.createMenuSymbol("PCR_SLEEP_ENABLE_" + register_index, blockSleepMenu)
        slpEnableMenu.setLabel("Sleep Enable " + register_index)
        slpEnablexVal = coreComponent.createHexSymbol("PCR_SLEEP_ENABLE_" + register_index + "_VAL", slpEnableMenu)
        slpEnablexVal.setDefaultValue(0)
        slpEnablexVal.setVisible(False)
        reg_bit_fields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"" + register_name + "\"]").getChildren()
        for idx in range(len(reg_bit_fields)):
            bitfield_name = reg_bit_fields[idx].getAttribute("name")
            bitfield_caption = reg_bit_fields[idx].getAttribute("caption")
            slpEnableBitfield = coreComponent.createBooleanSymbol(register_name + bitfield_name, slpEnableMenu)
            slpEnableBitfield.setLabel(bitfield_caption)
            slpEnableBitfield.setDefaultValue(False)
            sleep_en_reg_dep_list[numRegs].append(register_name + bitfield_name)
            macro_dict = {"reg_index": register_index, "bitfield_name": bitfield_name}
            sleep_en_reg_macros_list[numRegs].append(macro_dict.copy())
            sleep_en_reg_mask_dic[register_name + bitfield_name] =  int(reg_bit_fields[idx].getAttribute("mask"),16)
        slpEnablexVal.setDependencies(sleep_reg_val_update, sleep_en_reg_dep_list[numRegs])
        numRegs += 1

numSleepEnRegs = coreComponent.createIntegerSymbol("NUM_SLEEP_EN_REGS", None)
numSleepEnRegs.setVisible(False)
numSleepEnRegs.setDefaultValue(numRegs)

enum_index = 0
for sleep_en_reg_list in sleep_en_reg_macros_list:
    # Code to generate SLEEP_ENABLE enum in header file
    sleepEnableEnum_List = coreComponent.createListSymbol("PCR_SLEEP_ENABLE" + str(enum_index) + "_ENUM_LIST", None)
    sleepEnableEnum_List.setVisible(False)

    sleepEnableEnums = coreComponent.createListEntrySymbol("PCR_SLEEP_ENABLE" + str(enum_index) + "_ENUM", None)
    sleepEnableEnums.setTarget("core." + "PCR_SLEEP_ENABLE" + str(enum_index) + "_ENUM_LIST")
    sleepEnableEnums.setVisible(False)

    enum_value = ""

    for macro_dict in sleep_en_reg_list:
        macro_val = "PCR_SLP_EN_" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + "_Msk"
        enum_value += "PCR_SLEEP_EN" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + " = " + macro_val + "," + "\n\r\t"
    sleepEnableEnums.addValue(enum_value)

    enum_index += 1

#-----------------------------------
blockPrivMenu = coreComponent.createMenuSymbol("CEC173X_PCR_PRIV_MENU", None)
blockPrivMenu.setLabel("Block Privilege Config")

global priv_en_reg_dep_list
priv_en_reg_dep_list = []

global priv_en_reg_macros_list
priv_en_reg_macros_list = []
numRegs = 0

pcr_registers_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]").getChildren()
for id in range(len(pcr_registers_node)):
    register_name = pcr_registers_node[id].getAttribute("name")
    if "EC_PRIV" in register_name:
        priv_en_reg_macros_list.append([])
        priv_en_reg_dep_list.append([])
        register_index = register_name[len("EC_PRIV_EN"):]
        privEnableRegIndex = coreComponent.createStringSymbol("PCR_PRIV_ENABLE" + str(numRegs) + "_REG_INDEX", None)
        privEnableRegIndex.setVisible(False)
        privEnableRegIndex.setDefaultValue(register_index)
        privEnableMenu = coreComponent.createMenuSymbol("PCR_PRIV_ENABLE_" + register_index, blockPrivMenu)
        privEnableMenu.setLabel("Privilege Enable " + register_index)
        privEnablexVal = coreComponent.createHexSymbol("PCR_PRIV_ENABLE_" + register_index + "_VAL", privEnableMenu)
        privEnablexVal.setDefaultValue(0)
        privEnablexVal.setVisible(False)
        reg_bit_fields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"" + register_name + "\"]").getChildren()
        for idx in range(len(reg_bit_fields)):
            bitfield_name = reg_bit_fields[idx].getAttribute("name")
            bitfield_caption = reg_bit_fields[idx].getAttribute("caption")
            privEnableBitfield = coreComponent.createBooleanSymbol(register_name + bitfield_name, privEnableMenu)
            privEnableBitfield.setLabel(bitfield_caption)
            privEnableBitfield.setDefaultValue(False)
            priv_en_reg_dep_list[numRegs].append(register_name + bitfield_name)
            macro_dict = {"reg_index": register_index, "bitfield_name": bitfield_name}
            priv_en_reg_macros_list[numRegs].append(macro_dict.copy())
            priv_en_reg_mask_dic[register_name + bitfield_name] =  int(reg_bit_fields[idx].getAttribute("mask"),16)
        privEnablexVal.setDependencies(priv_reg_val_update, priv_en_reg_dep_list[numRegs])
        numRegs += 1

numPrivEnRegs = coreComponent.createIntegerSymbol("NUM_PRIV_EN_REGS", None)
numPrivEnRegs.setVisible(False)
numPrivEnRegs.setDefaultValue(numRegs)

enum_index = 0
for priv_en_reg_list in priv_en_reg_macros_list:
    # Code to generate PRIV_ENABLE enum in header file
    privEnableEnum_List = coreComponent.createListSymbol("PCR_PRIV_ENABLE" + str(enum_index) + "_ENUM_LIST", None)
    privEnableEnum_List.setVisible(False)

    privEnableEnums = coreComponent.createListEntrySymbol("PCR_PRIV_ENABLE" + str(enum_index) + "_ENUM", None)
    privEnableEnums.setTarget("core." + "PCR_PRIV_ENABLE" + str(enum_index) + "_ENUM_LIST")
    privEnableEnums.setVisible(False)

    enum_value = ""

    for macro_dict in priv_en_reg_list:
        macro_val = "PCR_EC_PRIV_EN" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + "_Msk"
        enum_value += "PCR_PRIV_EN" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + " = " + macro_val + "," + "\n\r\t"
    privEnableEnums.addValue(enum_value)

    enum_index += 1

#-----------------------------------
global reset_en_reg_macros_list
reset_en_reg_macros_list = []
numRegs = 0

pcr_registers_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]").getChildren()
for id in range(len(pcr_registers_node)):
    register_name = pcr_registers_node[id].getAttribute("name")
    if ("RST_EN" in register_name) and ("LOCK" not in register_name):
        reset_en_reg_macros_list.append([])
        register_index = register_name[len("RST_EN_"):]
        resetEnableRegIndex = coreComponent.createStringSymbol("PCR_RESET_ENABLE" + str(numRegs) + "_REG_INDEX", None)
        resetEnableRegIndex.setVisible(False)
        resetEnableRegIndex.setDefaultValue(register_index)
        reg_bit_fields = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PCR\"]/register-group@[name=\"PCR\"]/register@[name=\"" + register_name + "\"]").getChildren()
        for idx in range(len(reg_bit_fields)):
            bitfield_name = reg_bit_fields[idx].getAttribute("name")
            macro_dict = {"reg_index": register_index, "bitfield_name": bitfield_name}
            reset_en_reg_macros_list[numRegs].append(macro_dict.copy())
        numRegs += 1

numResetEnRegs = coreComponent.createIntegerSymbol("NUM_RESET_EN_REGS", None)
numResetEnRegs.setVisible(False)
numResetEnRegs.setDefaultValue(numRegs)

enum_index = 0
for reset_en_reg_list in reset_en_reg_macros_list:
    # Code to generate RESET_ENABLE enum in header file
    resetEnableEnum_List = coreComponent.createListSymbol("PCR_RESET_ENABLE" + str(enum_index) + "_ENUM_LIST", None)
    resetEnableEnum_List.setVisible(False)

    resetEnableEnums = coreComponent.createListEntrySymbol("RESET_PRIV_ENABLE" + str(enum_index) + "_ENUM", None)
    resetEnableEnums.setTarget("core." + "PCR_RESET_ENABLE" + str(enum_index) + "_ENUM_LIST")
    resetEnableEnums.setVisible(False)

    enum_value = ""

    for macro_dict in reset_en_reg_list:
        macro_val = "PCR_RST_EN_" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + "_Msk"
        enum_value += "PCR_RESET_EN" + macro_dict["reg_index"] + "_" + macro_dict["bitfield_name"] + " = " + macro_val + "," + "\n\r\t"
    resetEnableEnums.addValue(enum_value)

    enum_index += 1


################################################################################
###########             CODE GENERATION                     ####################
################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

pcr_HeaderFile = coreComponent.createFileSymbol("PCR_HEADER_FILE", None)
pcr_HeaderFile.setSourcePath("../peripheral/pcr_cec_173x/templates/plib_pcr.h.ftl")
pcr_HeaderFile.setOutputName("plib_pcr.h")
pcr_HeaderFile.setDestPath("peripheral/pcr/")
pcr_HeaderFile.setProjectPath("config/" + configName + "/peripheral/pcr/")
pcr_HeaderFile.setType("HEADER")
pcr_HeaderFile.setMarkup(True)

pcr_SourceFile = coreComponent.createFileSymbol("PCR_SOURCE_FILE", None)
pcr_SourceFile.setSourcePath("../peripheral/pcr_cec_173x/templates/plib_pcr.c.ftl")
pcr_SourceFile.setOutputName("plib_pcr.c")
pcr_SourceFile.setDestPath("peripheral/pcr/")
pcr_SourceFile.setProjectPath("config/" + configName + "/peripheral/pcr/")
pcr_SourceFile.setType("SOURCE")
pcr_SourceFile.setMarkup(True)

pcr_InitFile = coreComponent.createFileSymbol("PCR_INIT", None)
pcr_InitFile.setType("STRING")
pcr_InitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
pcr_InitFile.setSourcePath("../peripheral/pcr_cec_173x/templates/system/initialization.c.ftl")
pcr_InitFile.setMarkup(True)

pcr_SystemDefFile = coreComponent.createFileSymbol("PCR_SYS_DEF", None)
pcr_SystemDefFile.setType("STRING")
pcr_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
pcr_SystemDefFile.setSourcePath("../peripheral/pcr_cec_173x/templates/system/definitions.h.ftl")
pcr_SystemDefFile.setMarkup(True)

