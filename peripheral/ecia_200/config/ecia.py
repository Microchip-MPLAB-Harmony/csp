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



################################################################################
#### Global Variables ####
################################################################################
global ecia_bitfields
global nvic_dic
global nvic_vector_name_list
global nvic_vector_num_list
global interrupt_sources_list
global int_source_girqn_map
global girq_block_reg_dep_list

ecia_bitfields = {}
nvic_vector_name_list = []
nvic_vector_num_list = []
interrupt_sources_list = []
int_source_girqn_map  = {}
nvic_dic = {}
girq_block_reg_dep_list = []

girq_reg_start_index = 255
girq_reg_end_index = 0

################################################################################
#### Business Logic ####
################################################################################

# Enable GIRQn block if any interrupt source in the corresponding GIRQn register is enabled
def girqBlockRegUpdate(symbol, event):
    girq_num = int(event["id"].split("_")[3])
    value = symbol.getValue()
    if event["value"] == 0:
        value = int(value) & ~(1 << girq_num)
    else:
        value = int(value) | (1 << girq_num)
    symbol.setValue(value)

def GetNVICNum(int_source):
    for index in range(len(nvic_vector_name_list)):
        if int_source == nvic_vector_name_list[index]:
            return nvic_vector_num_list[index]

def GetBitPosition(bitMask):
    for bitpos in range (0,32):
        if bitMask & (1 << bitpos):
            return bitpos

# [31][28-24][23-16][15-8][7-0]
# [1][5-0][7-0][7-0][7-0]
# [AGG_OR_DIR][GIRQn_BIT][GIRQn_NUM][AGG_NVIC_NUM][DIRECT_NVIC_NUM]
def GenMacroValue(group_or_direct, girqn_bitpos, girqn_reg_num, group_nvic_num, direct_nvic_num):
    if direct_nvic_num == None:
        direct_nvic_num = 0
    if group_nvic_num == None:
        group_nvic_num = 0

    return ((group_or_direct << 31) | (girqn_bitpos << 24) | (girqn_reg_num << 16) | (group_nvic_num << 8) | direct_nvic_num)

# This function is called by NVIC to let ECIA enable the corresponding interrupt source in the GIRQ registers.
# Argument int_source is either the direct NVIC name (if module has enabled direct interrupt) or the Group NVIC source name (if Aggregate interrupt is enabled)
global ECIA_EN_SET_RegUpdate
def ECIA_EN_SET_RegUpdate(int_source, isEnabled): 
    for index in range (0, len(interrupt_sources_list)):
        if interrupt_sources_list[index]["name"] == int_source or interrupt_sources_list[index]["group_nvic_name"] == int_source:
            girqn_reg_num = 8 + interrupt_sources_list[index]["girqn_reg_num"]
            girqn_bitpos = interrupt_sources_list[index]["girqn_bitpos"]
            girqn_value = Database.getSymbolValue("core", "ECIA_EN_SET_" + str(girqn_reg_num) + "_VAL")
            if isEnabled == True:
                girqn_value = int(girqn_value) | int(1 << girqn_bitpos)
            else:
                girqn_value = int(girqn_value) & ~(int(1 << girqn_bitpos))
            Database.setSymbolValue("core", "ECIA_EN_SET_" + str(girqn_reg_num) + "_VAL", long(girqn_value))
            break

# This function is called by individual modules to get info about the Aggregate interrupt number, Direct interrupt number and Aggregate interrupt name
global ECIA_GetInterruptNumber
def ECIA_GetInterruptNumber(int_source):        # int_source is always the direct interrupt name (which is same as the bitfield name in ECIA registers)
    int_num_dic = {}
    for index in range (0, len(interrupt_sources_list)):
        sourceDict = interrupt_sources_list[index]
        if sourceDict["name"] == int_source:
            int_num_dic = sourceDict
            break
    return int_num_dic

# This function is called by NVIC to get the module-instance information for the given NVIC interrupt name (int_source)
global ECIA_GetNVICModuleList
def ECIA_GetNVICModuleList(int_source):
    nvic_source_module_list = {}
    nvic_source_module_list[int_source] = nvic_dic[int_source]
    return nvic_source_module_list

#--------------------------------------------------------------------------------------------------------------------------------------#
# Create a list of nvic vector name and nvic vector number
nvic_vectors_list = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
for nvic_vector in range (0, len(nvic_vectors_list)):
    nvic_num = int(nvic_vectors_list[nvic_vector].getAttribute("index"), 0)
    if nvic_num >= 0:
        nvic_vector_num_list.append(nvic_num)
        nvic_vector_name_list.append(nvic_vectors_list[nvic_vector].getAttribute("name"))

# Create a list of dictionaries for each interrupt source in ECIA module. For each interrupt source, dictionary contains its name (as available in the GIRQ bitfield), its GIRQ register number, GIRQ register bit position, group NVIC number, direct NVIC number and group NVIC name
ecia_bitfields_list = []
girqn_reg_list = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"ECIA\"]/register-group@[name=\"ECIA\"]").getChildren()
for girqn_reg in range(0, len(girqn_reg_list)):
    girqn_reg_name = girqn_reg_list[girqn_reg].getAttribute("name")
    if "SRC" in girqn_reg_name:
        girqn_reg_num = girqn_reg_name[3:]
        reg_bitfield_list = ATDF.getNode('/avr-tools-device-file/modules/module@[name=\"ECIA\"]/register-group@[name=\"ECIA\"]/register@[name="' + girqn_reg_name + '"]').getChildren()
        for reg_bitfield_name in range(0, len(reg_bitfield_list)):
            int_source = reg_bitfield_list[reg_bitfield_name].getAttribute("name")
            int_source_girqn_map[int_source] = {"girqn_reg_num":int(girqn_reg_num) - 8, "girqn_bitpos": GetBitPosition(int(reg_bitfield_list[reg_bitfield_name].getAttribute("mask"), 0))}
            sourceDict = {}
            sourceDict["name"] = int_source
            sourceDict["group_nvic_num"] = GetNVICNum("GIRQ" + "{:02d}".format(int(girqn_reg_num)))      # Save the group NVIC number
            sourceDict["direct_nvic_num"] = GetNVICNum(int_source)    # Find the corresponding Direct NVIC number and save it
            sourceDict["girqn_reg_num"] = int_source_girqn_map[int_source]["girqn_reg_num"]
            sourceDict["girqn_bitpos"] = int_source_girqn_map[int_source]["girqn_bitpos"]
            # If ECIA reg has only one bitfield, then the group NVIC name is GIRQxx where xx is the ECIA register index. Else it is same as the bit-field name.
            if len(reg_bitfield_list) > 1:
                sourceDict["group_nvic_name"] = int_source
            else:
                sourceDict["group_nvic_name"] = "GIRQ" + "{:02d}".format(int(girqn_reg_num))
            interrupt_sources_list.append(sourceDict)                       # Add source dictionary to the list of interrupt sources
            ecia_bitfields_list.append(int_source + "_GRP")
        ecia_bitfields["GIRQ" + "{:02d}".format(int(girqn_reg_num))] = list(ecia_bitfields_list)    # deep-copy the list into the ecia_bitfields dictionary
        del ecia_bitfields_list[:]

        eciaEnSetVal = coreComponent.createHexSymbol("ECIA_EN_SET_" + girqn_reg_num + "_VAL", None)
        eciaEnSetVal.setDefaultValue(0x00)
        eciaEnSetVal.setVisible(False)
        girq_block_reg_dep_list.append("ECIA_EN_SET_" + girqn_reg_num + "_VAL")

        if girq_reg_start_index > int(girqn_reg_num):
            girq_reg_start_index = int(girqn_reg_num)
        if girq_reg_end_index < int(girqn_reg_num):
            girq_reg_end_index = int(girqn_reg_num) 

#--------------------------------------------------------------------------------------------------------------------------------------#
#Create a dictionary of vector name pointing to its list of module instances. This will be consumed by the NVIC module to show multiple interrupt sources on same NVIC vector number.
nvic_vectors_list = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
for nvic_vector in range (0, len(nvic_vectors_list)):
    nvic_name = nvic_vectors_list[nvic_vector].getAttribute("name")
    if "GIRQ" in nvic_name:
        # For group interrupts get the list of interrupt sources from ecia_bitfields dictionary. ecia_bitfields dictionary is populated based on the bitfields of the ECIA registers.
        nvic_dic[nvic_name] = ecia_bitfields[nvic_name]
    else:
        # For non group interrupts, read directly from the module-instance field in ATDF
        nvic_dic[nvic_name] = list(str(nvic_vectors_list[nvic_vector].getAttribute("module-instance")).split(" "))

#--------------------------------------------------------------------------------------------------------------------------------------#

eciaIntSourceEnum_List = coreComponent.createListSymbol("ECIA_INT_SOURCE_ENUM_LIST", None)
eciaIntSourceEnum_List.setVisible(False)

eciaIntSourceEnums = coreComponent.createListEntrySymbol("ECIA_INT_SOURCE_ENUM", None)
eciaIntSourceEnums.setTarget("core.ECIA_INT_SOURCE_ENUM_LIST")
eciaIntSourceEnums.setVisible(False)

girq_block_reg = coreComponent.createHexSymbol("ECIA_GIRQ_BLOCK_REG_VAL", None)
girq_block_reg.setDefaultValue(0x00)
girq_block_reg.setDependencies(girqBlockRegUpdate, girq_block_reg_dep_list)
girq_block_reg.setVisible(False)

girq_reg_start_num = coreComponent.createIntegerSymbol("ECIA_GIRQ_REG_START", None)
girq_reg_start_num.setDefaultValue(girq_reg_start_index)
girq_reg_start_num.setVisible(False)

girq_reg_end_num = coreComponent.createIntegerSymbol("ECIA_GIRQ_REG_END", None)
girq_reg_end_num.setDefaultValue(girq_reg_end_index)
girq_reg_end_num.setVisible(False)

for index in range (0, len(interrupt_sources_list)):
    sourceDict = interrupt_sources_list[index]
    if sourceDict["group_nvic_num"] != None:
        enum_value = "ECIA_AGG_INT_SRC_" + sourceDict["name"] + " = " + str(hex(GenMacroValue(0, sourceDict["girqn_bitpos"], sourceDict["girqn_reg_num"], sourceDict["group_nvic_num"], sourceDict["direct_nvic_num"]))) + "," + "\n\r\t"
        eciaIntSourceEnums.addValue(enum_value)
    if sourceDict["direct_nvic_num"] != None:
        enum_value = "ECIA_DIR_INT_SRC_" + sourceDict["name"] + " = " + str(hex(GenMacroValue(1, sourceDict["girqn_bitpos"], sourceDict["girqn_reg_num"], sourceDict["group_nvic_num"], sourceDict["direct_nvic_num"]))) + "," + "\n\r\t"
        eciaIntSourceEnums.addValue(enum_value)


################################################################################
#### Component ####
################################################################################

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

eciaHeaderFile = coreComponent.createFileSymbol("ECIA_HEADER", None)
eciaHeaderFile.setType("HEADER")
eciaHeaderFile.setSourcePath("../peripheral/ecia_200/templates/plib_ecia.h.ftl")
eciaHeaderFile.setOutputName("plib_ecia.h")
eciaHeaderFile.setDestPath("/peripheral/ecia/")
eciaHeaderFile.setProjectPath("config/" + configName + "/peripheral/ecia/")
eciaHeaderFile.setMarkup(True)
eciaHeaderFile.setOverwrite(True)

eciaSourceFile = coreComponent.createFileSymbol("ECIA_SOURCE", None)
eciaSourceFile.setType("SOURCE")
eciaSourceFile.setSourcePath("../peripheral/ecia_200/templates/plib_ecia.c.ftl")
eciaSourceFile.setOutputName("plib_ecia.c")
eciaSourceFile.setDestPath("/peripheral/ecia/")
eciaSourceFile.setProjectPath("config/" + configName + "/peripheral/ecia/")
eciaSourceFile.setMarkup(True)
eciaSourceFile.setOverwrite(True)

eciaSystemInitFile = coreComponent.createFileSymbol("ECIA_INIT", None)
eciaSystemInitFile.setType("STRING")
eciaSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_INTERRUPTS")
eciaSystemInitFile.setSourcePath("../peripheral/ecia_200/templates/system/initialization.c.ftl")
eciaSystemInitFile.setMarkup(True)

eciaSystemDefFile = coreComponent.createFileSymbol("ECIA_DEF", None)
eciaSystemDefFile.setType("STRING")
eciaSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
eciaSystemDefFile.setSourcePath("../peripheral/ecia_200/templates/system/definitions.h.ftl")
eciaSystemDefFile.setMarkup(True)