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

import math
import re
import json
import os
from collections import OrderedDict

# Constants

ADC = "ADC"
SOURCE = "source"
AD = "AD" 
CHANNEL_REG_GROUP = "CH"
CLK_GEN6_KEY = "clkGen6OutFrequency"
CORE_COMPONENT = "core"
INTRUPT_PREFIX = "INTC"
CHx_INTERRUPT_COMMENT = "CH{}_INTERRUPT_COMMENT"

ADC_MENU ="ADC_MENU"
ADC_INSTANCE_NAME = "ADC_03459_INSTANCE_NAME"
ADC_INSTANCE_NUM = "instance"
ADC_CLOCK = "ADC_CLOCK"
ADC_CLOCK_DEFAULT_VALUE = "Clock Generator 6"
ADC_CLOCK_FREQUENCY = "ADC_CLOCK_FREQUENCY"
TAD_CORE = "TAD_CORE"
TAD_CORE_LABEL = "TADCORE (us)"
CONVERSION_TIME = "CONVERSION_TIME"
RESOLUTION_BIT = "resolutionBit"
CLK_COMMENT_KEY = "CLK_COMMENT"


RESOLUTION_BIT_LABEL = "Resolution Bit"
ENABLE_INPUT_SCAN = "ENABLE_INPUT_SCAN"
ADC_CHANNEL_CONFIGURATION = "ADC_CHANNEL_CONFIGURATION"
CON = "CON"
RPTCNT = "RPTCNT"
NUMBER_OF_CHANNELS = "numChannels"

ADC_MENU_LABEL = "ADC Configuration"
ADC_CLOCK_LABEL = "Clock Source"
ADC_CLOCK_FREQUENCY_LABEL = "Clock Source Frequency (Hz)"
CONVERSION_TIME_LABEL = "Conversion Time (us)"
CONVERSION_REPEAT_TIMER_LABEL = "Conversion Repeat Timer"
ENABLE_INPUT_SCAN_LABEL = "Enable Input Scan"
ADC_CHANNEL_CONFIGURATION_LABEL = "Channel Configuration"

# Channel constants
CHANNEL_PREFIX = "Channel"
CHXUsed = "ch{}channelUsed"
CHXSECACC = "ch{}SecAcc"
CHx = "CH{}"
CH19_SEC_ACC19_VALUE = "ACC19"
PINSEL_KEY = "PINSEL"
TRG1SRC_KEY = "TRG1SRC"
SAMC_KEY = "SAMC"
LEFT_KEY = "LEFT"
AD_CHxCON__PINSEL = "AD_CH{}CON__PINSEL"
AD_CH_CON__PINSEL = "AD_CH_CON__PINSEL"
SAMPLE_COUNT = "Sample Count"
INTERRUPT = "Interrupt"
CHxCON = "CH{}CON"
ANX_LABEL = "Analog Positive Input Selection"
TRIGGER_SOURCE_1_LABEL = "Select Trigger Source 1"
SAMPLING_TIME_LABEL = "Sampling Time Selection bits"
DATA_FORMAT_LABEL = "Select Data Format"

# Mode constants
MODE = "Mode"
MODE_KEY = "MODE"
TRG2SRC_KEY = "TRG2SRC"
ACCNUM_KEY = "ACCNUM"
ACCBRST_KEY = "ACCBRST"
AD_CHx__SECONDARY_ACCUMULATOR = "AD_CH{}__SECONDARY_ACCUMULATOR"
AD_CHx__OVERSAMPLING_BURST_MODE = "AD_CH{}__OVERSAMPLING_BURST_MODE"
OVERSAMPLING_MODE = "Oversampling of multiple samples defined by ACCNUM[1:0] bits"
SINGLECONVERSION_MODE = "Single sample initiated by TRG1SRC[4:0] trigger"
INTEGRATION_MODE = "Integration of multiple samples defined by: CNTx[15:0] bits (ADnCNTx[15:0])"
WINDOW_MODE = "Window gated by TRG1SRC[4:0] source"
CNT_KEY = "CNT"
CHxCNT = "CH{}CNT"
SEC_ACC = "SEC_ACC"
AD_CHxCON__MODE="AD_CH{}CON__MODE"
MODE_SELECTION_LABEL = "Mode Selection "
TRIGGER_SOURCE_2_LABEL = "Select Trigger Source 2"
OVERSAMPLING_OPTIONS_LABEL = "Select OverSampling options"
SECONDARY_ACCUMULATOR_LABEL = "Enable Secondary Accumulator"
OVERSAMPLING_BURST_MODE_LABEL = "OverSampling BurstMode"
MODE_CONFIGURATION_LABEL = "Mode Configuration"

# Comparator constants
COMPARATOR = "Comparator"
ENABLE_LABEL = "Comparator Enable"
CMPMOD = "CMPMOD"
CMPLO= "CMPLO"
CMPHI= "CMPHI"
CHxCMPHI= "CH{}CMPHI"
CHxCMPLO = "CH{}CMPLO"
chxcmpUsed = "ch{}cmpUsed"
COMPARATOR_EVENT_LABEL = "Comparator Event"
SELECT_CMP_LOW_LABEL = "Select CMP LOW"
SELECT_CMP_HIGH_LABEL = "Select CMP HIGH"

# Constants for pattern matching
MODE_PATTERN = r"AD_CH(\d+)CON__MODE"
CHANNEL_PATTERN = r"ch(\d+)channelUsed"
COMPARATOR_PATTERN = r"ch(\d+)cmpUsed"



def updateChannelSymbolVisibility(symbol, event):
    symbol_id = event.get("id")
    # Extract the digit after 'Channel_' using regex
    match = re.match(CHANNEL_PATTERN, symbol_id) 
    if match:
        channelNumber = match.group(1)       
        # Construct the symbol IDs that depend on the channel's visibility
        symbolIdToObjectMap = createDependentChannelSymbols(channelNumber)

        # Fetch symbols using their IDs
        fetched_symbols  = getSymbols(event[SOURCE], symbolIdToObjectMap )

        # Update visibility for each symbol based on the main symbol's value
        for key, fetched_symbol  in fetched_symbols.items():
            update_symbol_visibility(fetched_symbol , symbol.getValue())

def updateComparatorSymbolVisibility(symbol, event):
    """Update the visibility of comparator-related symbols based on comparator enablement."""   
    
    symbol_id = event.get("id")
    # Extract the comparator index from the symbol ID using regex
    match = re.match(COMPARATOR_PATTERN, symbol_id)  # Assuming a similar pattern for comparator IDs
    if match:
        comparatorIndex = match.group(1)

        # Construct the symbol IDs that depend on the comparator's visibility
        symbolIdToObjectMap = createDependentComparatorSymbols(comparatorIndex)

        # Fetch symbols using their IDs
        fetched_symbols = getSymbols(event[SOURCE], symbolIdToObjectMap)

        # Update visibility for each symbol based on the comparator enable symbol's value
        for key, fetched_symbol in fetched_symbols.items():
            update_symbol_visibility(fetched_symbol, symbol.getValue())

def updateSymbolVisibilityByModeSelection(symbol, event):
    symbol_id = event.get("id")
    # Extract the digit after 'MODE_' using regex
    match = re.match(MODE_PATTERN, symbol_id)
    if match:
        mode_index = int(match.group(1))
        # Construct the symbol IDs that depend on the mode selection
        symbol_id_map  = createDependentModeSymbols(mode_index)
        # Fetch the symbols from the event source using the IDs
        fetched_symbols  = getSymbols(event[SOURCE], symbol_id_map )
        # Update each symbol's visibility or read-only status
        update_sample_count(fetched_symbols["sampleCount"], symbol.getSelectedKey())
        update_trigger_source(fetched_symbols["triggerSource2"], symbol.getSelectedKey())
        update_oversampling_options(fetched_symbols["oversamplingOptions"], symbol.getSelectedKey())
        update_oversampling_burst_mode(fetched_symbols["oversamplingBurstMode"], symbol.getSelectedKey())
        update_secondary_accumulator(fetched_symbols["secondaryAccumulator"], symbol.getSelectedKey(), mode_index)

    else:
        Log.writeInfoMessage("No valid mode index found in symbol ID")


def update_symbol_visibility(symbol, value):
    """Update the visibility of the symbol based on the provided value."""
    if symbol:
        symbol.setVisible(value)

def update_sample_count(symbol, selected_key):
    """
    Set visibility for sampleCount column.
    - Visible for 'Window' and 'Integration' modes.
    - Hidden for 'Oversampling' mode.
    """
    if symbol:
        # Visible for 'Window' and 'Integration', hidden for 'Oversampling'
        if selected_key in [WINDOW_MODE, INTEGRATION_MODE]:
            symbol.setVisible(True)
        elif selected_key == OVERSAMPLING_MODE:
            symbol.setVisible(False)
        else:
            symbol.setVisible(False)

def update_trigger_source(symbol, selected_key):
    """
    Set visibility for conversionTrgSrc2 column. Visible for 'Integration', 'Window', and 'Oversampling' modes.
    """
    if symbol:
        trigger_source_visible_modes = [INTEGRATION_MODE, WINDOW_MODE, OVERSAMPLING_MODE]
        symbol.setVisible(selected_key in trigger_source_visible_modes)

def update_secondary_accumulator(symbol, selected_key, mode_index):
    """
    Set visibility for accumulatorRollOver column. Visible in 'Integration' mode and if index is greater than SEC_ACCUMULATOR_CONST.
    """
    if symbol:
        if SEC_ACCUMULATOR_CONST is not None:
            sec_accumulator = int(SEC_ACCUMULATOR_CONST)
            if mode_index > sec_accumulator:
                symbol.setVisible(selected_key == INTEGRATION_MODE)   
            else:
                symbol.setVisible(False)

def update_oversampling_options(symbol, selected_key):
    """
    Set visibility for sampleSelection column. Visible only for 'Oversampling' mode.
    """
    if symbol:
        symbol.setVisible(selected_key == OVERSAMPLING_MODE)

def update_oversampling_burst_mode(symbol, selected_key):
    """
    Set visibility for burstMode column. Visible only for 'Oversampling' mode.
    """
    if symbol:
        symbol.setVisible(selected_key == OVERSAMPLING_MODE)


def createDependentComparatorSymbols(comparatorIndex):
    """
    Create a dictionary of dependent comparator symbols based on the comparator index.
    This function generates the necessary symbol keys for visibility control.
    """
    # Create the symbol ID map for the specified comparator index
    symbolIdToObjectMap = {
        "cmpMod": "AD_CH{}CON__CMPMOD".format(comparatorIndex),
        "cmpLow": "AD_CH{}CMPLO".format(comparatorIndex),
        "cmpHigh": "AD_CH{}CMPHI".format(comparatorIndex),
        "cmpInterrupt": "cmp{}IntEnable".format(comparatorIndex)
    }
    
    return symbolIdToObjectMap

def createDependentChannelSymbols(number):
    """Constructs symbol IDs that depend on the channel's visibility based on the prefix and number."""
    return {
        "anx": "AD_CH{}CON__PINSEL".format(number),  # Updated
        "sampleTime": "AD_CH{}CON__SAMC".format(number),  # Updated
        "triggerSource1": "AD_CH{}CON__TRG1SRC".format(number),  # Updated
        "dataFormatMenu": "AD_CH{}CON__LEFT".format(number),  # Updated
        "channel_InterruptMode": "ch{}IntEnable".format(number),  # Updated for interrupts
        "modeConfigurationSymbolID": "{}{}".format(MODE, number),
        "comparatorConfigurationID":  chxcmpUsed.format(number)
    }

def createDependentModeSymbols(mode_index):
    return {
        "sampleCount": "AD_{}__CNT".format(CHxCNT.format(mode_index)),  # Updated to use the new format
        "triggerSource2": "AD_CH{}CON__TRG2SRC".format(mode_index),  # Using the specified pattern
        "secondaryAccumulator": AD_CHx__SECONDARY_ACCUMULATOR.format(mode_index),  # Updated
        "oversamplingOptions": "AD_CH{}CON__ACCNUM".format(mode_index),  # Using the specified pattern
        "oversamplingBurstMode": "AD_CH{}CON__ACCBRST".format(mode_index),# # Updated
        "chxchannelUsed" : "ch{}channelUsed".format(mode_index)
    }

def getSymbols(source, symbol_ids):
    # Fetch and return a dictionary of symbols by their IDs
    return {
        key: source.getSymbolByID(id) for key, id in symbol_ids.items()
    }

def getRegisterDefaultValue(module, register_group, register):
    """
    Gets the default initval for a register from the ATDF using the provided module and register group names.
    """
    # Path to the register node in the ATDF structure
    reg_path = '/avr-tools-device-file/modules/module@[name="{}"]/register-group@[name="{}"]/register@[name="{}"]'.format(
        module, register_group, register
    )
    # Retrieve the register node
    register_node = ATDF.getNode(reg_path)
    
    # If the register node is found, fetch and return the initval as hex; otherwise, return "0x0UL"
    if register_node is not None:
        reg_default_val = register_node.getAttribute("initval")
        return "{}UL".format(reg_default_val) if reg_default_val else "0x0UL"
    return "0x0UL"

def create_reg_por_set_string(module, register_group, registers):
    """
    Generates a formatted string of default register values for a given module, register group, and list of registers.
    """
    reg_defaults = OrderedDict()  # Use OrderedDict to maintain the insertion order
    reg_por_set = ""   # Initialize the regPorSet output string
    
    module_name = adcInstanceName.getValue()    
    match = re.search(r'\d+$', module_name) 
    instance_number = match.group(0) if match else ""   # Extract instance number

    if register_group == CHANNEL_REG_GROUP:
        reg_por_set = create_reg_por_set_Channel_string(module, register_group, registers, instance_number)
    else:
        for reg in registers:
            reg_name = "{}{}{}".format(register_group, instance_number, reg)  # Form key as register_group + instanceNumber + reg
            reg_defaults[reg_name] = getRegisterDefaultValue(module, register_group, reg)
        
        # Format the output string with 4-space indentation per register
        for reg_name, default_val in reg_defaults.items():
            reg_por_set += "    {} = {};\n".format(reg_name, default_val)
    
    return reg_por_set

def create_reg_por_set_Channel_string(module, register_group, registers, instance_number):
    """
    Generates a formatted string of default register values for a given module and channel-specific register group.
    """
    reg_defaults = OrderedDict()  # Use OrderedDict to maintain the insertion order
    reg_por_set = ""   # Initialize the regPorSet output string

    # Sort enabled_channels to ensure the order of channel numbers
    sorted_channels = sorted(enabled_channels, key=lambda x: int(re.search(r'\d+', x).group(0)))  # Sort by channel number
    # Loop through each enabled channel and create registers for it
    for channel in sorted_channels:
        # Extract the channel number (e.g., 'ch5channelUsed' -> 5)
        channel_number = re.search(r'\d+', channel).group(0)  # Extract digits from the channel name
        
        # Generate all registers for this channel
        for reg in registers:
            reg_name = "AD{}CH{}{}".format(instance_number, channel_number, reg)
            reg_defaults[reg_name] = getRegisterDefaultValue(module, register_group, reg)
    
    # Format the output string with 4-space indentation per register
    for reg_name, default_val in reg_defaults.items():
        reg_por_set += "    {} = {};\n".format(reg_name, default_val)
    
    return reg_por_set


#########Interrupt related Helper Function start ###############################

def getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList):
    intSymbolMap= {}
    intEntryCount = len(interruptList)   
    intFlagList = [compPrefix+compInstance+interrupt+"IF" for interrupt in interruptList]
    flagRegisterGroup = getModuleRegisterGroup("intc","IFS")
    isflagDataAdded = False
    if(flagRegisterGroup != None):
        for registerNode in flagRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intFlagList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IF","").lower() + "InterruptFlagBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isflagDataAdded = True
                        break
            if isflagDataAdded:
                break        
                    
    intEntryCount = 2*intEntryCount
    isEnableDataAdded = False
    intEnableList = [compPrefix+compInstance+interrupt+"IE" for interrupt in interruptList]
    enableRegisterGroup = getModuleRegisterGroup("intc","IEC")
    if(enableRegisterGroup != None):
        for registerNode in enableRegisterGroup:
            for bitfieldNode in registerNode.getChildren():
                bitName = bitfieldNode.getAttribute("name")
                if(bitName.startswith(compPrefix+compInstance) and bitName in intEnableList):
                    intSymbolName = bitName.replace(compPrefix+compInstance,"").replace("IE","").lower() + "InterruptEnableBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break                          
    
    for interrupt in interruptList:
        intSymbolName = interrupt.lower() + "IsrHandlerName"
        intSymbolMap[intSymbolName] = compPrefix + compInstance +interrupt+"_InterruptHandler"
    
    return intSymbolMap

def createInterruptSymbols(component,intSymbolMap):
    for key in intSymbolMap:
        interruptSymbol = component.createStringSymbol(key, None)
        interruptSymbol.setDefaultValue(intSymbolMap[key])
        interruptSymbol.setVisible(False)

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index        

#########Interrupt related Helper Function end ###############################


# ATDF Helper Functions

def getParameterValue(module_name, instance_name, param_name):
    # Construct the XPath query based on the provided arguments
    xpath_query = (
        "/avr-tools-device-file/devices/device/peripherals/module@[name=\"{0}\"]/"
        "instance@[name=\"{1}\"]/parameters/param@[name=\"{2}\"]"
    ).format(module_name, instance_name, param_name)
    
    param_list = ATDF.getNode(xpath_query)
    
    if param_list is not None:
        param_value = param_list.getAttribute("value")
        return param_value
    else:
        return None


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value 

def getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         regDefaultVal = registerNode.getAttribute("initval")
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return getDefaultVal(regDefaultVal,bitMask)
     return 0


def maxThreshold(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)

     if(registerNode != None):
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             return int(bitMask,16)      
     return 0

def getValueGroupName(moduleName,registerGroup,register,bitfield):
    bitNode = getBitField(moduleName,registerGroup,register,bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

def getModuleRegisterGroup(moduleName, registerGroup):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]'
    )
    registerGroupNode = ATDF.getNode(atdfPath)
    if registerGroupNode != None:
        return registerGroupNode.getChildren()
    return None

def getModuleRegisterData(moduleName, registerGroup, register):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(atdfPath)
    if registerNode != None:
        return registerNode.getChildren()
    return None

def getValueGroup(moduleName, valueGroupName):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/value-group@[name="'
        + valueGroupName
        + '"]'
    )
    return ATDF.getNode(atdfPath)

def getBitField(moduleName, registerGroup, register, bitfield):
    atdfPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]/bitfield@[name="'
        + bitfield
        + '"]'
    )
    return ATDF.getNode(atdfPath)

def processBitfield(bitfield):
    dict = {}
    caption = bitfield.getAttribute("caption")
    if caption.lower() != "reserved":  # skip (unused) reserved fields            
        dict["desc"] = caption
        dict["key"] = caption

        # Get rid of leading '0x', and convert to int if was hex
        value = bitfield.getAttribute("value")
        if value[:2] == "0x":
            temp = value[2:]
            tempint = int(temp, 16)
        else:
            tempint = int(value)

        dict["value"] = str(tempint)
        return dict
    return None

def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
    for bitfield in valueNodes: 
        processed_bitfield = processBitfield(bitfield)
        if processed_bitfield:
            optionList.append(processed_bitfield)
    return optionList

def getBitfieldOptionListForAnx(node):
    valueNodes = node.getChildren()
    optionList = []
    dict = {}
    filtered_additional_analog_inputs = [pin for pin in additional_analog_inputs if pin["value"] is not None]

    for bitfield in valueNodes:
        caption = bitfield.getAttribute("caption")
        # Check if caption starts with AD1 or AD_ and is not reserved
        if (caption.startswith("AD1") or caption.startswith("AD_")) and caption.lower() != "reserved":
            caption = caption[3:]
          
            default_pin_data = next((pin for pin in filtered_additional_analog_inputs if pin["key"] == caption), None)
            is_default_pin = default_pin_data is not None

            # Skip if the pin is not in analogPinsResult and not a default pin
            if not is_default_pin and caption not in analogPinsResult:
                continue

            # Convert value to integer
            value = str(
                int(bitfield.getAttribute("value")[2:], 16)
                if bitfield.getAttribute("value").startswith("0x")
                else int(bitfield.getAttribute("value"))
            )

            # Build the dictionary
            dict = {"desc": caption, "key": caption, "value": value}
            # If the pin is a default pin, update its values from additional_analog_inputs
            if is_default_pin and default_pin_data:
                dict["desc"] = default_pin_data["value"]
                dict["key"] = default_pin_data["value"]

            # Append to the option list
            optionList.append(dict)
    return optionList


def getKeyValuePairBasedonValue(value, keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return (
                index  # return occurrence of <bitfield > entry which has matching value
            )
        index += 1

    Log.writeInfoMessage("find_key: could not find value in dictionary")  # should never get here
    return ""


def addKeystoKeyValueSymbol(bitSymbol, bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey(ii["key"], ii["value"], ii["desc"])

def update_keys(option_list):
    for item in option_list:
        # Extract the original key
        original_key = item['key']
        
        # Update the key to the desired format
        updated_key = u'AN{}'.format(original_key[-1])  # Get the last character and format it
        
        # Assign the updated key back to the item
        item['key'] = updated_key

    return option_list

def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield, parentNode = None,index = None): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            # Determine the symbol key based on index
            symbolKey = valueGroupEntry if index is None else valueGroupEntry.replace("CH_", "CH{}".format(index))
            # Retrieve the appropriate option list based on the value group name
            optionList = getOptionListForValueGroup(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, parentNode )
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp 

def getOptionListForValueGroup(valGroup):
    """
    Retrieves the appropriate option list based on the value group.
    """
    if valGroup.getAttribute("name") == AD_CH_CON__PINSEL:
        optionList = getBitfieldOptionListForAnx(valGroup)
    else:
        optionList = getBitfieldOptionList(valGroup)    
    return optionList       

##################################################################################
############################ Clock calculations start ##################################
##################################################################################


def getFormattedAdcClkFreq():
    return str(getClockValue())


def getClockValue():
    clk_freq = Database.getSymbolValue("core", CLK_GEN6_KEY)
    if clk_freq is not None:
        return clk_freq
    return 0


def getTadCoreValue():
    return 4.0 / float(getClockValue()) if getClockValue() != 0 else 0.0


def getTsrcDisplay():
    """
    This function calculates the display value by converting the TAD core value
    (obtained from getTadCoreValue()) to microseconds using convertToMicroSec(),
    and then rounds it to 3 significant figures. If the result is 0, it returns 0.
    """
    tad_core_value = getTadCoreValue()
    micro_sec_value = convertToMicroSec(tad_core_value)

    if micro_sec_value != 0:
        return str(round(micro_sec_value, 3))
    else:
        return "0"


def conversionTimeDisplay():
    """
    This function calculates the conversion time by converting the result from
    getConTime() to microseconds using convertToMicroSec(), and then rounds it to
    3 decimal places. It returns the result as a string. If the result is 0, it returns "0".
    """
    con_time_value = getConTime()
    micro_sec_value = convertToMicroSec(con_time_value)

    if micro_sec_value != 0:
        return str(round(micro_sec_value, 3))
    else:
        return "0"


def convertToMicroSec(numInSec):
    """
    Converts the given time in seconds to microseconds by multiplying the input by 10^6.
    """
    return numInSec * 10**6


def getConTime():
    """
    This function calculates the conversion time by multiplying the TAD core value
    (obtained from getTadCoreValue()) by 2. It returns the result as a float.
    """
    return getTadCoreValue() * 2

def updateClkCalculations(clkFreqSymbol, event):
   clkFreqSymbol = event[SOURCE].getSymbolByID(ADC_CLOCK_FREQUENCY)
   clkFreqSymbol.setValue(getFormattedAdcClkFreq())
   tadCoreSymbol = event[SOURCE].getSymbolByID(TAD_CORE)
   tadCoreSymbol.setValue(getTsrcDisplay())  
   conversionTimeSymbol = event[SOURCE].getSymbolByID(CONVERSION_TIME)
   conversionTimeSymbol.setValue(conversionTimeDisplay())

def updateClockComment(symbol, event):

    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

##################################################################################
############################ Clock calculations end ##################################
##################################################################################

# Define the mapping of channels to IFS registers dynamically
def getIFSRegister(instance, channel):
   if instance == 1:  # ADC instance 1
        if channel < 8:   # Channels 0-7
            return "IFS4"
        elif channel < 16:  # Channels 8-15
            return "IFS5"
        elif channel < 20:  # Channels 16-19
            return "IFS6"
   elif instance == 2:  # ADC instance 2
        if channel < 8:   # Channels 0-7
            return "IFS7"
        elif channel < 16:  # Channels 8-15
            return "IFS8"
        elif channel < 20:  # Channels 16-19
            return "IFS9"
   return None 

def configure_adc_channel(adcComponent, i, adcChannel,comparatorLowThreshold,comparatorHighThreshold,sampleCountThreshold):
    """Configures the ADC channel related symbols."""

    # channelName = "{}{}".format(CHANNEL_PREFIX, i)
    channelName = "ch{}channelUsed".format(i)
    channelMenu = adcComponent.createBooleanSymbol(channelName, adcChannel)
    channelMenu.setLabel(CHANNEL_PREFIX + " " + str(i))
    channelMenu.setDefaultValue(False)
    channelMenu.setDependencies(updateChannelSymbolVisibility, [channelName])

    # ANx
    anxMenu = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, PINSEL_KEY, channelMenu,i)
    anxMenu.setVisible(False)
    anxMenu.setLabel(ANX_LABEL)
    anxMenu.setDependencies(updateChannelPinSelection, [AD_CHxCON__PINSEL.format(i)])
    anxMenu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))


    # Sample Time
    sampleTime = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, SAMC_KEY, channelMenu,i)
    sampleTime.setLabel(SAMPLING_TIME_LABEL)
    sampleTime.setVisible(False)
    sampleTime.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))

    # Data Format
    dataFormatMenu = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, LEFT_KEY, channelMenu,i)
    dataFormatMenu.setLabel(DATA_FORMAT_LABEL)
    dataFormatMenu.setVisible(False)
    dataFormatMenu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))

    # Interrupt
    channelInterrupt = "ch{}IntEnable".format(i)
    channel_Interrupt = adcComponent.createBooleanSymbol(channelInterrupt, channelMenu)
    channel_Interrupt.setLabel("Enable Interrupt")
    channel_Interrupt.setDefaultValue(False)
    channel_Interrupt.setVisible(False)
    channel_Interrupt.setDependencies(updateChIntEnable, [channelInterrupt,channelName])
    # Determine the IFS register for the channel
    ifsRegister = getIFSRegister(instanceNumber, i)
    
    if ifsRegister is None:
        Log.writeInfoMessage("No IFS register mapping found for instance {}, channel {}. Skipping.".format(instanceNumber, i))
        return

    # Add setHelp to the symbol
    channel_Interrupt.setHelp("atmel;device:{};comp:adc_03459;register:{}".format(Variables.get("__PROCESSOR"), ifsRegister))

    # Interrupt Symbols from ATDF for Code Generation 
    compPrefix = AD
    compInstance = adcComponent.getID().upper().replace(ADC,"") 
    # Add channel interrupt (e.g., CH0, CH1, etc.) to the interrupt list
    chInterruptList = ["CH{}".format(i)]
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,chInterruptList)
    createInterruptSymbols(adcComponent,intSymbolMap)
    updateChInterruptLists(instanceNumber, chInterruptList)


    # EIEN 
    eienSymkey = "AD_CH{}".format(i) + CON+"__"+"EIEN"
    eienSym = adcComponent.createIntegerSymbol(eienSymkey, None)
    eienSym.setMin(0)
    eienSym.setMax(1)
    eienSym.setVisible(False)

    # NINSEL 
    negPinSymkey = "AD_CH{}".format(i) + CON+"__"+"NINSEL"
    negPin = adcComponent.createIntegerSymbol(negPinSymkey, None)
    negPin.setVisible(False)

    # DIFF 
    diffSymkey = "AD_CH{}".format(i) + CON+"__"+"DIFF"
    diffSym = adcComponent.createIntegerSymbol(diffSymkey, None)
    diffSym.setVisible(False)

    # Channel PIN Select
    channelSelect = "ch{}ChannelPosPin".format(i)
    channelSelectSym = adcComponent.createStringSymbol(channelSelect, None)
    channelSelectSym.setVisible(False)


    # Mode Configuration
    configure_mode_configuration(adcComponent,channelMenu, i, sampleCountThreshold)

    # Comparator Configuration
    configure_comparator_configuration(adcComponent,channelMenu,comparatorLowThreshold,comparatorHighThreshold,channelName,i)

def configure_mode_configuration(adcComponent,channelMenu,index,sampleCountThreshold):
    """Configures the mode related symbols for a given channel."""
    
    mode_prefix = "{}{}".format(MODE, index)
    adcMode = adcComponent.createMenuSymbol(mode_prefix, channelMenu)
    adcMode.setLabel(MODE_CONFIGURATION_LABEL)
    adcMode.setVisible(False)

    # Mode Selection
    modeMenu_symbol = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, MODE_KEY, adcMode,index)
    modeMenu_symbol.setLabel(MODE_SELECTION_LABEL)
    modeMenu_id = AD_CHxCON__MODE.format(index)
    modeMenu_symbol.setDependencies(updateSymbolVisibilityByModeSelection, [modeMenu_id])
    modeMenu_symbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))

    # TRG1SRC
    triggerSource1Menu = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, TRG1SRC_KEY, adcMode,index)
    triggerSource1Menu.setLabel(TRIGGER_SOURCE_1_LABEL)
    triggerSource1Menu.setVisible(False)
    triggerSource1Menu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))


    # # Sample Count
    sampleCountKey = "AD_"+CHxCNT.format(index)+"__CNT"
    sampleCount = adcComponent.createIntegerSymbol(sampleCountKey, adcMode)
    sampleCount.setLabel(SAMPLE_COUNT)
    sampleCount_defaultValue = getSettingBitDefaultValue(ADC, CHANNEL_REG_GROUP, CNT_KEY, CNT_KEY)
    sampleCount.setMin(0)
    sampleCount.setDefaultValue(sampleCount_defaultValue)
    sampleCount.setMax(sampleCountThreshold)
    sampleCount.setVisible(False)

    # Secondary Accumulator
    secondaryAccumlatorEnable = adcComponent.createBooleanSymbol(AD_CHx__SECONDARY_ACCUMULATOR.format(index),adcMode)
    secondaryAccumlatorEnable.setLabel(SECONDARY_ACCUMULATOR_LABEL)
    secondaryAccumlatorEnable.setVisible(False)
    secondaryAccumlatorEnable.setDefaultValue(False)
    secondaryAccumlatorEnable.setDependencies(updateAccro, [AD_CHx__SECONDARY_ACCUMULATOR.format(index)])


    # Trigger Source 2
    triggerSource2Menu = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, TRG2SRC_KEY, adcMode,index)
    triggerSource2Menu.setVisible(False)
    triggerSource2Menu.setLabel(TRIGGER_SOURCE_2_LABEL)
    triggerSource2Menu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))


    # OverSampling Format
    overSamplingMenu = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, ACCNUM_KEY, adcMode, index)
    overSamplingMenu.setLabel(OVERSAMPLING_OPTIONS_LABEL)
    overSamplingMenu.setVisible(False)
    overSamplingMenu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))


    # OverSampling BurstMode
    overSamplingBurstMode = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, ACCBRST_KEY, adcMode, index)
    overSamplingBurstMode.setLabel(OVERSAMPLING_BURST_MODE_LABEL)
    overSamplingBurstMode.setVisible(False)
    overSamplingBurstMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))


    # ACCRO bit set when SecAccu set
    accroSymkey = AD+"_"+ CHxCON.format(index)+"__"+"ACCRO"
    accroSym = adcComponent.createIntegerSymbol(accroSymkey, None)
    accroSym.setVisible(False)

def configure_comparator_configuration(adcComponent, channelMenu,comparatorLowThreshold,comparatorHighThreshold,channelName,index):
    """Configures the comparator related symbols for a given channel."""

    # Comparator Enable
    cmpUsed = "ch{}cmpUsed".format(index)
    comparatorEnable = adcComponent.createBooleanSymbol(cmpUsed,channelMenu)
    comparatorEnable.setLabel(ENABLE_LABEL)
    comparatorEnable.setDefaultValue(False)
    comparatorEnable.setVisible(False)
    comparatorEnable.setDependencies(updateComparatorSymbolVisibility, [cmpUsed])

    #Comparator Format
    comparatorEvent = createKeyValueSetSymbol(adcComponent, ADC, CHANNEL_REG_GROUP, CON, CMPMOD, comparatorEnable, index)
    comparatorEvent.setLabel(COMPARATOR_EVENT_LABEL)
    comparatorEvent.setVisible(False)
    comparatorEvent.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCON".format(instanceNumber))

    

    # CMP LOW
    cmpLowKey = "AD_"+CHxCMPLO.format(index)
    cmpLowMenu = adcComponent.createHexSymbol(cmpLowKey, comparatorEnable)
    cmpLowMenu.setLabel(SELECT_CMP_LOW_LABEL)
    cmpLowMenu_defaultValue = getSettingBitDefaultValue(ADC, CHANNEL_REG_GROUP, CMPLO, CMPLO)
    cmpLowMenu.setMin(0)
    cmpLowMenu.setDefaultValue(cmpLowMenu_defaultValue)
    cmpLowMenu.setMax(comparatorLowThreshold)
    cmpLowMenu.setVisible(False)
    cmpLowMenu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCMPLO".format(instanceNumber))

  

    # CMP HIGH
    cmpHighKey = "AD_"+CHxCMPHI.format(index)
    cmpHighMenu = adcComponent.createHexSymbol(cmpHighKey, comparatorEnable)
    cmpHighMenu.setLabel(SELECT_CMP_HIGH_LABEL)
    cmpHighMenu_defaultValue = getSettingBitDefaultValue(ADC, CHANNEL_REG_GROUP,CMPHI, CMPHI)
    cmpHighMenu.setMin(0)
    cmpHighMenu.setDefaultValue(cmpHighMenu_defaultValue)
    cmpHighMenu.setMax(comparatorHighThreshold)
    cmpHighMenu.setVisible(False)
    cmpHighMenu.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:AD{}CHxCMPHI".format(instanceNumber))

   

    # Interrupt
    cmpInterrupt = "cmp{}IntEnable".format(index)
    cmp_Interrupt = adcComponent.createBooleanSymbol(cmpInterrupt, comparatorEnable)
    cmp_Interrupt.setLabel("CMP Interrupt")
    cmp_Interrupt.setDefaultValue(False)
    cmp_Interrupt.setVisible(False)
    cmp_Interrupt.setDependencies(updateCmpIntEnable,[cmpInterrupt,cmpUsed,channelName])
     # Determine the IFS register for the channel
    ifsRegister = getIFSRegister(instanceNumber, index)
    
    if ifsRegister is None:
        Log.writeInfoMessage("No IFS register mapping found for instance {}, channel {}. Skipping.".format(instanceNumber, index))
        return
    # Add setHelp to the symbol
    cmp_Interrupt.setHelp("atmel;device:{};comp:adc_03459;register:{}".format(Variables.get("__PROCESSOR"), ifsRegister))

    # Interrupt Symbols from ATDF for Code Generation 
    compPrefix = AD
    compInstance = adcComponent.getID().upper().replace(ADC,"") 
    # Add comparator interrupt (e.g., CMP0, CMP1, etc.) to the interrupt list
    cmpInterruptList = ["CMP{}".format(index)]

    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,cmpInterruptList)
    createInterruptSymbols(adcComponent,intSymbolMap)
    updateCmpInterruptLists(instanceNumber, cmpInterruptList)


channelStatusList = []
channelInterruptList  = []
cmpInterruptList  = []
modeSelectionList =[]
secAccList= []
enabled_channels =[] # Need for de-initialize apis
reg_por_set_ad = ""
analogPinsResult = []
additional_analog_inputs = []


def instantiateComponent(adcComponent):
    global interruptCmpEnableList,interruptHandlerLockList,interruptEnableList,adcInstanceName, num_channels,SEC_ACCUMULATOR_CONST,instanceNumber, channelStatusList,channelInterruptList,cmpInterruptList,modeSelectionList, secAccList,enabled_channels,reg_por_set_ad
    interruptEnableList = []
    interruptCmpEnableList =[]
    interruptHandlerLockList = []


    adcInstanceName = adcComponent.createStringSymbol(ADC_INSTANCE_NAME, None)  
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    instance_name = adcInstanceName.getValue()
    Log.writeInfoMessage("Running " + instance_name)

    adc_instance_num = adcComponent.getID().upper().replace(ADC, "")
    instanceNumber = adcComponent.createStringSymbol(ADC_INSTANCE_NUM, None)
    instanceNumber.setDefaultValue(adc_instance_num)
    instanceNumber.setVisible(False)

    instanceNumber = int(adc_instance_num)
    SEC_ACCUMULATOR_CONST = getParameterValue(ADC, instance_name , SEC_ACC)

    analog_input_list = getParameterValue(ADC, instance_name, "analog_pins").split(',')
    # Extract AN followed by digits
    analogPinsResult.extend([re.search(r'AN\d+', item).group() for item in analog_input_list if re.search(r'AN\d+', item)])

    # List of parameter names to fetch and append
    analog_input_params = ["AN11","AN12", "AN13", "AN14", "AN15"]
    fetched_data = [
        {"key": param, "value": getParameterValue(ADC, instance_name, "AD{}{}".format(instanceNumber, param))}
        for param in analog_input_params
    ]
    additional_analog_inputs.extend(fetched_data)


    ################################################################################
    ########## ADC Menu ################################################
    ########################################################################
    adcMenu = adcComponent.createMenuSymbol(ADC_MENU, None)
    adcMenu.setLabel(ADC_MENU_LABEL)

    adcClock = adcComponent.createStringSymbol(ADC_CLOCK, adcMenu)
    adcClock.setLabel(ADC_CLOCK_LABEL)
    adcClock.setDefaultValue(ADC_CLOCK_DEFAULT_VALUE)
    adcClock.setReadOnly(True)

    adcClockFrequency = adcComponent.createStringSymbol(ADC_CLOCK_FREQUENCY, adcMenu)
    adcClockFrequency.setLabel(ADC_CLOCK_FREQUENCY_LABEL)
    adcClockFrequency.setDefaultValue(getFormattedAdcClkFreq())
    adcClockFrequency.setReadOnly(True)
    adcClockFrequency.setDependencies(updateClkCalculations, [CORE_COMPONENT + "." +CLK_GEN6_KEY])


    tadCore = adcComponent.createStringSymbol(TAD_CORE, adcMenu)
    tadCore.setLabel(TAD_CORE_LABEL)
    tadCore.setValue(getTsrcDisplay())
    tadCore.setReadOnly(True)
    tadCore.setVisible(True)

    conversionTime = adcComponent.createStringSymbol(CONVERSION_TIME, adcMenu)
    conversionTime.setLabel(CONVERSION_TIME_LABEL)
    conversionTime.setValue(conversionTimeDisplay())
    conversionTime.setReadOnly(True)
    conversionTime.setVisible(True)

    conversionRepeatTimer = createKeyValueSetSymbol(adcComponent, ADC, AD, CON, RPTCNT, adcMenu)
    conversionRepeatTimer.setLabel(CONVERSION_REPEAT_TIMER_LABEL)
    conversionRepeatTimer.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:adc_03459;register:ADnCON")


    enableInputScan = adcComponent.createBooleanSymbol(ENABLE_INPUT_SCAN, adcMenu)
    enableInputScan.setLabel(ENABLE_INPUT_SCAN_LABEL)
    enableInputScan.setDefaultValue(False)
    enableInputScan.setVisible(False)

    resolution_bit_value = getParameterValue(ADC, instance_name, RESOLUTION_BIT)
    resolution_bit = adcComponent.createStringSymbol(RESOLUTION_BIT, adcMenu)
    resolution_bit.setLabel(RESOLUTION_BIT_LABEL)
    resolution_bit.setValue(resolution_bit_value)
    resolution_bit.setVisible(True)
    resolution_bit.setReadOnly(True)

    clkComment = adcComponent.createCommentSymbol(CLK_COMMENT_KEY, adcMenu)
    clkComment.setLabel("Warning!!! Enable and configure Clock Generator 6 in Clock Section of System Module")
    clockValue = Database.getSymbolValue(CORE_COMPONENT, CLK_GEN6_KEY)
    clkComment.setVisible(clockValue == 0)
    clkComment.setDependencies(getIFSRegister, [ADC_CLOCK_FREQUENCY,  CORE_COMPONENT + "." + CLK_GEN6_KEY])

    # Channel Configuration
    adcChannelConfiguration = adcComponent.createMenuSymbol(ADC_CHANNEL_CONFIGURATION, adcMenu)
    adcChannelConfiguration.setLabel(ADC_CHANNEL_CONFIGURATION_LABEL)

    comparatorLowThreshold = maxThreshold(ADC, CHANNEL_REG_GROUP, CMPLO, CMPLO)
    comparatorHighThreshold = maxThreshold(ADC, CHANNEL_REG_GROUP, CMPHI, CMPHI)
    sampleCountThreshold = maxThreshold(ADC, CHANNEL_REG_GROUP, CNT_KEY, CNT_KEY)
    num_channels = getParameterValue(ADC, instance_name, NUMBER_OF_CHANNELS)
    # Convert to integer if not None
    if num_channels is not None:
        num_channels = int(num_channels)
        Log.writeInfoMessage("Number of channels: {}".format(num_channels))

    # Loop to configure all channels
    for i in range(num_channels):
        configure_adc_channel(adcComponent, i, adcChannelConfiguration,comparatorLowThreshold,comparatorHighThreshold,sampleCountThreshold)
        # create the secondary accumulator symbol
        create_secondary_accumulator_symbol(adcComponent, i)

    chIntComment = adcComponent.createCommentSymbol("CH_INTERRUPT_COMMENT", None)
    chIntComment.setVisible(False)
    chIntComment.setDependencies(interruptChCommentCb, interruptEnableList)

    cmpIntComment = adcComponent.createCommentSymbol("CMP_INTERRUPT_COMMENT", None)
    cmpIntComment.setVisible(False)
    cmpIntComment.setDependencies(interruptCmpCommentCb, interruptCmpEnableList)

    ###################################################################################################
    ####################################### Code Generation symbols ##########################################
    ###################################################################################################


    moduleName = adcComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue(adcComponent.getID().upper())
    moduleName.setVisible(False)

    maxChannel = adcComponent.createIntegerSymbol("maxChannel", None)
    maxChannel.setDefaultValue(num_channels)
    maxChannel.setVisible(False)

    minPWM = adcComponent.createIntegerSymbol("minPWM", None)
    minPWM.setDefaultValue(1)
    minPWM.setVisible(False)

    maxPWM = adcComponent.createIntegerSymbol("maxPWM", None)
    maxPWM.setDefaultValue(4)
    maxPWM.setVisible(False)

    triggerInitVal = adcComponent.createHexSymbol("triggerInitVal", None)
    triggerInitVal.setDefaultValue(4)
    triggerInitVal.setVisible(False)

    # Any Channel Selected    
    anyChannelSelected  = adcComponent.createBooleanSymbol("isChannelSelected", None)
    anyChannelSelected.setDefaultValue(False)
    anyChannelSelected.setVisible(False)
     # Create dependenc array for each channel
    channelStatusList = ["ch{}channelUsed".format(i) for i in range(num_channels)]
    anyChannelSelected.setDependencies(updateAnyChannelSelected, channelStatusList)

    # Any Channel Interrupt Enabled
    anychannelIntEnable = adcComponent.createBooleanSymbol("channelIntEnable", None)
    anychannelIntEnable.setLabel("Any Channel Interrupt Enabled")
    anychannelIntEnable.setDefaultValue(False)
    anychannelIntEnable.setVisible(False) 
     # Create dependency array for each channel interrupts
    channelInterruptList = ["ch{}IntEnable".format(j) for j in range(num_channels)]
    anychannelIntEnable.setDependencies(updateAnyChannelIntEnable, channelInterruptList)

    # Any Comparator Interrupt Enabled
    anyCmpIntEnable = adcComponent.createBooleanSymbol("cmpIntEnable", None)
    anyCmpIntEnable.setLabel("Any Comparator Interrupt Enabled")
    anyCmpIntEnable.setVisible(False) 
    # Create dependency array for each cmp interrupts
    cmpInterruptList = ["cmp{}IntEnable".format(k) for k in range(num_channels)]
    anyCmpIntEnable.setDependencies(updateAnyCmpIntEnable, cmpInterruptList)

    
    # Any channel with Integration or Window conversion.
    any_channel_with_int_or_win_conversion = adcComponent.createBooleanSymbol("anyChannelWithIntOrWinConversion", None)
    any_channel_with_int_or_win_conversion.setLabel("Any Channel with Integration or Window Conversion")
    any_channel_with_int_or_win_conversion.setDefaultValue(False)
    any_channel_with_int_or_win_conversion.setVisible(False)
    # List to track if channels have selected Integration or Window Sampling
    modeSelectionList = [AD_CHxCON__MODE.format(k) for k in range(num_channels)]
    any_channel_with_int_or_win_conversion.setDependencies(updateChannelConversionAndAccumulatorStatus, modeSelectionList)

    
    # Any Channel With Integration and Secondary Accumulator 
    anyChWithIntConversionAndSecAcc = adcComponent.createBooleanSymbol("chWithIntConversionAndSecAcc", None)
    anyChWithIntConversionAndSecAcc.setLabel("Any Channel with Integration and Secondary Accumulator")
    anyChWithIntConversionAndSecAcc.setDefaultValue(False)
    anyChWithIntConversionAndSecAcc.setVisible(False)
    # List to track if channels having secondary accumulator
    secAccList = [AD_CHx__SECONDARY_ACCUMULATOR.format(k) for k in range(num_channels)]
    any_channel_with_int_or_win_conversion.setDependencies(updateChannelConversionAndAccumulatorStatus, secAccList)

    # String symbol for the POR (Power-On Reset) values of registers
    registers_ad  = ["CON","DATAOVR","STAT","CMPSTAT"] 
    reg_por_set_ad  = create_reg_por_set_string(ADC, AD, registers_ad )

    regPorSet = adcComponent.createStringSymbol("regPorSet", None)
    regPorSet.setDefaultValue(reg_por_set_ad)
    regPorSet.setVisible(False)


    # String symbol for the powerMode
    powerMode = adcComponent.createStringSymbol("AD_CON__MODE", None)
    powe_mode_value = getValueByCaption("ADC", "AD_CON__MODE", "ON")
    powerMode.setValue(powe_mode_value)
    powerMode.setVisible(False)

    #File Handling 

    configName = Variables.get("__CONFIGURATION_NAME")
  
    acHeader1File = adcComponent.createFileSymbol("ADC_HEADER", None)
    acHeader1File.setSourcePath("../peripheral/adc_03459/templates/plib_adc.h.ftl")
    acHeader1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".h")
    acHeader1File.setMarkup(True)
    acHeader1File.setDestPath("/peripheral/adc/")
    acHeader1File.setProjectPath("config/" + configName + "/peripheral/adc/")
    acHeader1File.setType("HEADER")

    adcCommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcCommonHeaderFile.setSourcePath("../peripheral/adc_03459/templates/plib_adc_common.h.ftl")
    adcCommonHeaderFile.setOutputName("plib_adc_common.h")
    adcCommonHeaderFile.setDestPath("peripheral/adc/")
    adcCommonHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcCommonHeaderFile.setType("HEADER")
    adcCommonHeaderFile.setMarkup(True)

    acSource1File = adcComponent.createFileSymbol("ADC_SOURCE", None)
    acSource1File.setSourcePath("../peripheral/adc_03459/templates/plib_adc.c.ftl")
    acSource1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".c")
    acSource1File.setMarkup(True)
    acSource1File.setDestPath("/peripheral/adc/")
    acSource1File.setProjectPath("config/" + configName + "/peripheral/adc/")
    acSource1File.setType("SOURCE")

    acSystemInitFile = adcComponent.createFileSymbol("ADC_SYS_INIT", None)
    acSystemInitFile.setType("STRING")
    acSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    acSystemInitFile.setSourcePath("../peripheral/adc_03459/templates/system/initialization.c.ftl")
    acSystemInitFile.setMarkup(True)

    acSystemDefFile = adcComponent.createFileSymbol("ACC_SYS_DEF", None)
    acSystemDefFile.setType("STRING")
    acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    acSystemDefFile.setSourcePath("../peripheral/adc_03459/templates/system/definitions.h.ftl")
    acSystemDefFile.setMarkup(True)


# Code generation Helper functions
#########################################

def getValueByCaption(moduleName, valueGroupName, targetCaption):
    # Get the value group node using the getValueGroup function
    valueGroupNode = getValueGroup(moduleName, valueGroupName)
    # Check if the value group node is valid
    if valueGroupNode is None:
        Log.writeInfoMessage("Value group not found for module: {} and valueGroupName: {}".format(moduleName, valueGroupName))
        return "0x0"   # Default to 0x0 if value group is not found
    
    # Iterate over the child nodes (options) in the value group
    for valueNode in valueGroupNode.getChildren():
        # Check if the current node has a 'caption' attribute matching the target caption
        if valueNode.getAttribute("caption") == targetCaption:
            # Return the 'value' attribute if the caption matches
            return valueNode.getAttribute("value")
        
    # Log an info message if no matching caption was found
    Log.writeInfoMessage("No option found with caption '{}' in module: {} and valueGroupName: {}".format(targetCaption, moduleName, valueGroupName))
    return 0x0


##################################################################################################################
## Callback functions: updateAnyChannelSelected, updateAnyChannelIntEnable, updateAnyCmpIntEnable
#                      updateChannelConversionAndAccumulatorStatus,updateChannelSecAccSetting, updateAccro
##################################################################################################################

# Callback function to update 'isChannelSelected' and 'regPorSet' based on individual channel selections
def updateAnyChannelSelected(symbol, event):
 
    channel_id = event["id"]
    component = event[SOURCE]

    # Get the current selection state of the channel
    is_channel_selected = component.getSymbolValue(channel_id)

    # Add or remove channel based on selection state, and log only if changed
    if is_channel_selected and channel_id not in enabled_channels:
        enabled_channels.append(str(channel_id))
    elif not is_channel_selected and channel_id in enabled_channels:
        enabled_channels.remove(channel_id)

    # Log the updated list of selected channels
    Log.writeInfoMessage("Selected channels: {}".format(enabled_channels))

    # update reg_por_set based on channel selected
    registers_channel = ["CON","DATA","CNT","CMPLO","CMPHI"]
    reg_por_set_channel = create_reg_por_set_string(ADC, CHANNEL_REG_GROUP, registers_channel)

    regPorSetSym = event[SOURCE].getSymbolByID("regPorSet")
    regPorSet = reg_por_set_ad + reg_por_set_channel
    regPorSetSym.setValue(regPorSet)

    # Update 'isChannelSelected' based on any channel being selected
    symbol.setValue(bool(enabled_channels))

# Callback function to update 'channelIntEnable' based on any channel interrupt enable/disable status
def updateAnyChannelIntEnable(symbol, event):
    channel_int = event["id"] 
    component = event[SOURCE]
    Log.writeInfoMessage("Channel Interrupts status changed: {}".format(channel_int))
   
    # Update the channelIntEnable symbol
    symbol.setValue(any([component.getSymbolValue(dep) for dep in channelInterruptList ]))

# Callback function to update 'cmpIntEnable' based on comparator interrupts
def updateAnyCmpIntEnable(symbol, event):
    cmp_int = event["id"] 
    component = event[SOURCE]
    Log.writeInfoMessage("Compartor Interrupts status changed: {}".format(cmp_int))

    # Update the cmpIntEnable symbol
    symbol.setValue(any([component.getSymbolValue(dep) for dep in cmpInterruptList ]))

#################################################################
## Callback function:
# updateChannelConversionAndAccumulatorStatus
##   Sets 'anyChannelWithIntOrWinConversion' to True if any channel
##   selects Integration or Window Sampling.
##  Sets 'chWithIntConversionAndSecAccSymbol' to True if any channel
##   selects Integration and secd Accumulator enabled.

#################################################################

def updateChannelConversionAndAccumulatorStatus(symbol, event):

    Log.writeInfoMessage("Callback triggered for updateChannelConversionAndAccumulatorStatus by event: {}".format(event["id"]))

    component = event[SOURCE]

    # Retrieve the overall symbols to update
    anyChannelWithIntOrWinConversionSymbol = component.getSymbolByID("anyChannelWithIntOrWinConversion")
    chWithIntConversionAndSecAccSymbol = component.getSymbolByID("chWithIntConversionAndSecAcc")

    # Track conditions across all channels
    hasIntOrWinMode = False
    hasIntAndSecAcc = False

    # Check all channels to see if they meet the criteria for either symbol
    for i in range(num_channels):
        # Get mode and secondary accumulator status for each channel
        mode = component.getSymbolByID(AD_CHxCON__MODE.format(i)).getSelectedKey()
        sec_acc_enabled = component.getSymbolByID(AD_CHx__SECONDARY_ACCUMULATOR.format(i)).getValue()

        # Check for Integration or Window mode
        if mode in [INTEGRATION_MODE, WINDOW_MODE]:
            hasIntOrWinMode = True
        
        # Check for Integration mode with Secondary Accumulator
        if mode == INTEGRATION_MODE and sec_acc_enabled:
            hasIntAndSecAcc = True

        # Break early if both conditions are met to save processing time
        if hasIntOrWinMode and hasIntAndSecAcc:
            break

    # Update symbols if conditions are met
    if anyChannelWithIntOrWinConversionSymbol.getValue() != hasIntOrWinMode:
        anyChannelWithIntOrWinConversionSymbol.setValue(hasIntOrWinMode)
        Log.writeInfoMessage("anyChannelWithIntOrWinConversion' updated to: {}".format(hasIntOrWinMode))

    if chWithIntConversionAndSecAccSymbol.getValue() != hasIntAndSecAcc:
        chWithIntConversionAndSecAccSymbol.setValue(hasIntAndSecAcc)
        Log.writeInfoMessage("'chWithIntConversionAndSecAcc' updated to: {}".format(hasIntAndSecAcc))

# Callback function to update 'chSecAcc' based on Channel's mode, secondary accumulator

def updateChannelSecAccSetting(symbol, event):
    component = event[SOURCE]
    Log.writeInfoMessage("Callback triggered: Updating 'chxSecAcc' based on Channel's mode selection,secondary accumulator")
    channelNumber = getChannelNumberFromEvent(event)

    # Retrieve Channel-specific symbols
    chUsed = component.getSymbolByID(CHXUsed.format(channelNumber))  # Replace with actual ID if different
    chSecAcc = component.getSymbolByID(CHXSECACC.format(channelNumber))
    mode_select = component.getSymbolByID(AD_CHxCON__MODE.format(channelNumber))
    secondary_accumulator_enabled = component.getSymbolByID(AD_CHx__SECONDARY_ACCUMULATOR.format(channelNumber)).getValue()

    # Check if the channel supports and has a secondary accumulator enabled
    chx_with_int_and_sec_acc = (
        mode_select.getSelectedKey() == INTEGRATION_MODE and 
        secondary_accumulator_enabled and
        chUsed.getValue()
    )

    # Update chSecAcc based on the conditions
    if chx_with_int_and_sec_acc:
        chSecAcc.setValue("ACC{0}".format(channelNumber))
        Log.writeInfoMessage("Channel {0}: Secondary Accumulator set to ACC{0}.".format(channelNumber))
    else:
        chSecAcc.setValue("")
        Log.writeInfoMessage("Channel {0}: Secondary Accumulator disabled.".format(channelNumber))

# callback function to dynamically adjust ACCRO based on SecAccu
# Update the ACCRO bit based on the SecAccu status.
# If SecAccu is enabled, ACCRO will be set to '1' to allow roll-over.

def updateAccro(symbol, event):

    secAccuEnabled = event["value"]
    channelNumber = getChannelNumberFromEvent(event)

    if channelNumber is None:
        Log.writeInfoMessage("Channel number could not be extracted from event ID: {}".format(event.get("id")))
        return

    # Construct the symbol key for ACCRO based on the channel number
    accroSymKey = "{}_{}__ACCRO".format(AD, CHxCON.format(channelNumber))
    accroSym = event.get("source").getSymbolByID(accroSymKey)

    if accroSym is None:
     Log.writeInfoMessage("ACCRO symbol '{}' not found for channel {}".format(accroSymKey, channelNumber))
     return
    
    # Set the ACCRO symbol value to '1' if SecAccu is enabled, otherwise to '0'
    accroValue = 1 if secAccuEnabled else 0
    accroSym.setValue(accroValue)

    # Log the update status
    statusMessage = "enabled" if secAccuEnabled else "disabled"
    Log.writeInfoMessage("ACCRO set to '{}' (roll-over {}) for channel {}".format(accroValue, statusMessage, channelNumber))

# Extract the selected channel position pin value from the symbol
def updateChannelPinSelection(anxSymbol, event):
  channelPospinValue= anxSymbol.getSelectedKey()

  channelNumber = getChannelNumberFromEvent(event)

  if channelNumber is None:
    Log.writeInfoMessage("Channel number could not be extracted from event ID: {}".format(event.get("id")))
    return

  # Construct the symbol key for PINSEL based on the channel number
  channelSelectKey = "ch{}ChannelPosPin".format(channelNumber)
  channelSelectSym = event.get("source").getSymbolByID(channelSelectKey)

  Log.writeInfoMessage("Updated symbol '{}' for channel {} with value '{}'.".format(channelSelectKey, channelNumber, channelPospinValue))
  
  channelSelectSym.setValue(channelPospinValue)


def getChannelNumberFromEvent(event):
    # Regular expression to find the number between "CH" and "__"
    match = re.search(r"AD_CH(\d+)", event["id"])
    if match:
        # Return the channel number as an integer
        return int(match.group(1))
    print("No match found for channel number.")
    return None

# Creates secondary accumulator symbol for a specific channel.
def create_secondary_accumulator_symbol(adcComponent, channel):
    secAccSymbolID = "ch{}SecAcc".format(channel)
    chXSecAcc = adcComponent.createStringSymbol(secAccSymbolID, None)
    chXSecAcc.setDefaultValue("")
    chXSecAcc.setVisible(False)
    chXSecAcc.setDependencies(updateChannelSecAccSetting, [AD_CHx__SECONDARY_ACCUMULATOR.format(channel)])

def setCoreInterruptSymbols(chIntValue, chNumber, interruptType):

    # Determine the interrupt ID pattern based on the type
    interruptId = (AD + str(instanceNumber) + (CHx if interruptType == "CHx" else "CMP{}").format(chNumber) + INTERRUPT)
    intIndex = getVectorIndex(interruptId)
    
    # Set Database values based on the interrupt state
    enableSymbol = "INTC_{}_ENABLE".format(intIndex)
    lockSymbol = "INTC_{}_HANDLER_LOCK".format(intIndex)
    Database.setSymbolValue("core", enableSymbol, chIntValue)
    Database.setSymbolValue("core", lockSymbol, chIntValue)

def setCoreChInterruptSymbols(chIntValue, chNumber):
    setCoreInterruptSymbols(chIntValue, chNumber, "CHx")

def setCoreCmpInterruptSymbols(chIntValue, chNumber):
    setCoreInterruptSymbols(chIntValue, chNumber, "CMPx")


def updateChIntEnable(symbol, event):
    # Match for interrupt or channel
    interrupt_match = re.search(r"ch(\d+)IntEnable", event["id"])
    channel_usage_match = re.search(r"ch(\d+)channelUsed", event["id"])

    # Determine the channel number based on the match
    if interrupt_match:
        channel_number = interrupt_match.group(1)
    elif channel_usage_match:
        channel_number = channel_usage_match.group(1)

    channel_symbol= CHXUsed.format(channel_number)
    interrupt_symbol = "ch{}IntEnable".format(channel_number)

    # Get symbol values
    is_channel_used = event[SOURCE].getSymbolValue(channel_symbol)
    is_interrupt_enabled = event[SOURCE].getSymbolValue(interrupt_symbol) 

    # Set core channel interrupt symbols based on conditions
    if interrupt_match or channel_usage_match:
        setCoreChInterruptSymbols(is_interrupt_enabled and is_channel_used, channel_number)

def updateCmpIntEnable(symbol, event):
    interrupt_match = re.search(r"cmp(\d+)IntEnable", event["id"])
    channel_usage_match = re.search(r"ch(\d+)channelUsed", event["id"])
    comparator_usage_match = re.search(r"ch(\d+)cmpUsed", event["id"])

    # Determine the channel number based on the matches
    if interrupt_match:
        channel_number = interrupt_match.group(1)
    elif channel_usage_match:
        channel_number = channel_usage_match.group(1)
    elif comparator_usage_match:
        channel_number = comparator_usage_match.group(1)

    # Construct symbol names dynamically
    interrupt_symbol = "cmp{}IntEnable".format(channel_number)
    channel_symbol = CHXUsed.format(channel_number)
    comparator_symbol = "ch{}cmpUsed".format(channel_number)

    # Retrieve symbol values
    is_interrupt_enabled = event[SOURCE].getSymbolValue(interrupt_symbol)
    is_channel_used = event[SOURCE].getSymbolValue(channel_symbol)
    is_comparator_enabled = event[SOURCE].getSymbolValue(comparator_symbol)

    # Combine conditions for setting the comparator interrupt
    should_enable_interrupt = is_interrupt_enabled and is_channel_used and is_comparator_enabled

    # Update comparator interrupt symbol
    if interrupt_match or channel_usage_match or comparator_usage_match:
        setCoreCmpInterruptSymbols(should_enable_interrupt, channel_number)


def interruptCommentHandler(symbol, event, interruptType):
    match = re.search(r'INTC_(\d+)_ENABLE', event["id"])
    if match:
        vector_index = match.group(1)
        # Fetch the interrupt name and caption using the vector index
        interrupt_name, interrupt_caption = getInterruptNameAndCaptionByIndex(vector_index)    
        # Determine the interrupt symbol ID based on the type
        if interruptType == "CHANNEL":
            interrupt_symbol_id = getChannelInterruptSymbolId(interrupt_name)
            label = 'Warning!!! Enable "{}" in Interrupts Section of System module'.format(interrupt_caption)
        elif interruptType == "CMP":
            interrupt_symbol_id = getCmpInterruptSymbolId(interrupt_name)
            label = 'Warning!!! Enable "{}" in Interrupts Section of System module'.format(interrupt_caption)
        else:
            return  # Invalid type; no action required

        # Update visibility based on interrupt state
        if symbol.getComponent().getSymbolValue(interrupt_symbol_id) == True:
            symbol.setLabel(label)
            symbol.setVisible(not event["value"])
        else:
            symbol.setVisible(False)


def interruptChCommentCb(symbol, event):
     interruptCommentHandler(symbol, event, "CHANNEL")

def interruptCmpCommentCb(symbol, event):
   interruptCommentHandler(symbol, event, "CMP")


def getInterruptNameAndCaptionByIndex(vector_index):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    interrupt_name = ""
    interrupt_caption = ""
    for param in interruptsChildren:
        if vector_index == str(param.getAttribute("index")):
            interrupt_name = str(param.getAttribute("name"))
            interrupt_caption = str(param.getAttribute("caption"))
            break
    return interrupt_name ,interrupt_caption

def getChannelInterruptSymbolId(interrupt_name):
    match = re.search(r'CH(\d+)', interrupt_name) 
    if match:
        channel_number = match.group(1)  
        return "ch{}IntEnable".format(channel_number)
    else:
        return None

def getCmpInterruptSymbolId(interrupt_name):
    match = re.search(r'CMP(\d+)', interrupt_name) 
    if match:
        channel_number = match.group(1)  
        return "cmp{}IntEnable".format(channel_number)
    else:
        return None    


def updateInterruptListsHelper(instanceNo, interruptList, enableList, lockList):
    for interrupt in interruptList:
        intIndex = getVectorIndex(AD + str(instanceNo) + interrupt + INTERRUPT)
        enableList.append("{}.{}_{}_ENABLE".format(CORE_COMPONENT, INTRUPT_PREFIX, intIndex))
        lockList.append("{}.{}_{}_HANDLER_LOCK".format(CORE_COMPONENT, INTRUPT_PREFIX, intIndex))

def updateChInterruptLists(instanceNo, interruptList):
    updateInterruptListsHelper(instanceNo, interruptList, interruptEnableList, interruptHandlerLockList)

def updateCmpInterruptLists(instanceNo, interruptList):
    updateInterruptListsHelper(instanceNo, interruptList, interruptCmpEnableList, interruptHandlerLockList)
