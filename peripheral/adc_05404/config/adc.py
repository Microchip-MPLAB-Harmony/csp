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


# Constants
ADC = "ADC"
SOURCE = "source"
AD = "AD" 
AD_CH0CON1__PINSEL = "AD_CH0CON1__PINSEL"

ADC_MENU ="ADC_MENU"
ADC_INSTANCE_NAME = "ADC05404_INSTANCE_NAME"
SPI_INSTANCE_NUM = "instance"
ADC_CLOCK = "ADC_CLOCK"
ADC_MENU_LABEL = "ADC Configuration"
ADC_CLOCK_LABEL = "Clock Source"
ADC_CLOCK_DEFAULT_VALUE = "Clock Generator 6"
ADC_CLOCK_FREQUENCY = "ADC_CLOCK_FREQUENCY"
ADC_CLOCK_FREQUENCY_LABEL = "Clock Source Frequency (Hz)"
TAD_CORE = "TAD_CORE"
TAD_CORE_LABEL = "TADCORE (us)"
CONVERSION_TIME = "CONVERSION_TIME"
CONVERSION_TIME_LABEL = "Conversion Time (us)"
RESOLUTION_BIT_LABEL = "Resolution Bit"
PWM_PRESENT_LABEL = "PWM Present"
CONVERSION_REPEAT_TIMER_LABEL = "Conversion Repeat Timer"
ENABLE_INPUT_SCAN = "ENABLE_INPUT_SCAN"
ENABLE_INPUT_SCAN_LABEL = "Enable Input Scan"
ADC_CHANNEL_CONFIGURATION = "ADC_CHANNEL_CONFIGURATION"
ADC_CHANNEL_CONFIGURATION_LABEL = "Channel Configuration"
CON = "CON"
RPTCNT = "RPTCNT"
NUMBER_OF_CHANNELS = "numChannels"
RESOLUTION_BIT = "resolutionBit"
IS_PWM_PRESENT = "isPwmGenPresent"


CHANNEL_PREFIX = "Channel"
CH19Used = "ch6channelUsed"
CH19SECACC = "ch19secAcc"
CH19_SEC_ACC19_VALUE = "ACC19"
PINSEL_KEY = "PINSEL"
TRG1SRC_KEY = "TRG1SRC"
SAMC_KEY = "SAMC"
FRAC_KEY = "FRAC"
TRIGGER_SOURCE_1_LABEL = "Select Trigger Source 1"
ANX_LABEL = "ANx"
MODE_SELECTION_LABEL = "Mode Selection "
SAMPLE_COUNT = "Sample Count"
DATA_FORMAT_LABEL = "Select Data Format"
INTERRUPT = "Interrupt"
SAMPLING_TIME_LABEL = "Sampling Time Selection bits"
CH0CON1 = "CH0CON1"
CH0CON2 = "CH0CON2"
CHCON1 = "CH{}CON1"
CHCON2 = "CH{}CON2"
CHANNEL = "CH{}"

MODE = "Mode"
MODE_KEY = "MODE"
TRG2SRC_KEY = "TRG2SRC"
ACCNUM_KEY = "ACCNUM"
ACCBRST_KEY = "ACCBRST"
TRIGGER_SOURCE_2_LABEL = "Select Trigger Source 2"
OVERSAMPLING_OPTIONS_LABEL = "Select OverSampling options"
SECONDARY_ACCUMULATOR_LABEL = "Enable Secondary Accumulator"
OVERSAMPLING_BURST_MODE_LABEL = "OverSampling BurstMode"
MODE_CONFIGURATION_LABEL = "Mode Configuration"
SAMPLE_COUNT_SUFFIX = "_Mode_Sample_Count"
AD_CHx__SECONDARY_ACCUMULATOR = "AD_CH{}__SECONDARY_ACCUMULATOR"
AD_CHx__OVERSAMPLING_BURST_MODE = "AD_CH{}__OVERSAMPLING_BURST_MODE"
OVERSAMPLING_BURST_MODE_SUFFIX = "_Mode_OverSampling_BurstMode"
OVERSAMPLING_MODE = "Oversampling of multiple samples defined by ACCNUM[1:0] bits"
SINGLECONVERSION_MODE = "Single sample initiated by TRG1SRC[4:0] trigger"
INTEGRATION_MODE = "Integration of multiple samples defined by: CNTx[15:0] bits (ADnCNTx[15:0])"
WINDOW_MODE = "Window gated by TRG1SRC[4:0] source"
CNT_KEY = "CNT"
CHxCNT = "CH{}CNT"
SEC_ACC = "SEC_ACC"
AD_CHxCON1__MODE="AD_CH{}CON1__MODE"


COMPARATOR = "Comparator"
COMPARATOR_CONFIGURATION_SUFFIX = "_Comparator_Configuration"
COMPARATOR_ENABLE_SUFFIX = "_Comparator_Enable"  
CMP_SUFFIX = "_CMP"  
CMP_LOW_SUFFIX = "_CMP_LOW"  
CMP_HIGH_SUFFIX = "_CMP_HIGH"  
ENABLE_LABEL = "Comparator Enable"
CMP_LABEL = "CMP"
COMPARATOR_CONFIGURATION_LABEL = "Comparator Configuration" 
COMPARATOR_EVENT_LABEL = "Comparator Event"
SELECT_CMP_LOW_LABEL = "Select CMP LOW"
SELECT_CMP_HIGH_LABEL = "Select CMP HIGH"
CMPMOD = "CMPMOD"
CH0CMPLO ="CH0CMPLO"
CMPLO= "CMPLO"
CHxCMPHI= "CH{}CMPHI"
CHxCMPLO = "CH{}CMPLO"
chxcmpUsed = "ch{}cmpUsed"
CMPHI= "CMPHI"


# Constants for pattern matching
MODE_PATTERN = r"AD_CH(\d+)CON1__MODE"
CHANNEL_PATTERN = r"ch(\d+)channelUsed"
COMPARATOR_PATTERN = r"ch(\d+)cmpUsed"


def createDependentComparatorSymbols(comparatorIndex):
    """
    Create a dictionary of dependent comparator symbols based on the comparator index.
    This function generates the necessary symbol keys for visibility control.
    """
    # Create the symbol ID map for the specified comparator index
    symbolIdToObjectMap = {
        "cmpMod": "AD_CH{}CON2__CMPMOD".format(comparatorIndex),
        "cmpLow": "AD_CH{}CMPLO".format(comparatorIndex),
        "cmpHigh": "AD_CH{}CMPHI".format(comparatorIndex),
        "cmpInterrupt": "cmp{}IntEnable".format(comparatorIndex)
    }
    
    return symbolIdToObjectMap

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

def createDependentChannelSymbols(number):
    """Constructs symbol IDs that depend on the channel's visibility based on the prefix and number."""
    return {
        "anx": "AD_CH{}CON1__PINSEL".format(number),  # Updated
        "sampleTime": "AD_CH{}CON1__SAMC".format(number),  # Updated
        "triggerSource1": "AD_CH{}CON1__TRG1SRC".format(number),  # Updated
        "dataFormatMenu": "AD_CH{}CON1__FRAC".format(number),  # Updated
        "channel_InterruptMode": "ch{}IntEnable".format(number),  # Updated for interrupts
        "modeConfigurationSymbolID": "{}{}".format(MODE, number),
        "comparatorConfigurationID":  chxcmpUsed.format(number)
    }

def symbolsToUpdateOnModeChange(mode_index):
    return {
        "sampleCount": "AD_{}__CNT".format(CHxCNT.format(mode_index)),  # Updated to use the new format
        "triggerSource2": "AD_CH{}CON1__TRG2SRC".format(mode_index),  # Using the specified pattern
        "secondaryAccumulator": AD_CHx__SECONDARY_ACCUMULATOR.format(mode_index),  # Updated
        "oversamplingOptions": "AD_CH{}CON1__ACCNUM".format(mode_index),  # Using the specified pattern
        "oversamplingBurstMode": "AD_CH{}CON2__ACCBRST".format(mode_index),# # Updated
        "chxchannelUsed" : "ch{}channelUsed".format(mode_index)
    }

def getSymbols(source, symbol_ids):
    # Fetch and return a dictionary of symbols by their IDs
    return {
        key: source.getSymbolByID(id) for key, id in symbol_ids.items()
    }

def updateSymbolVisibilityByModeSelection(symbol, event):
    symbol_id = event.get("id")
    # Extract the digit after 'MODE_' using regex
    match = re.match(MODE_PATTERN, symbol_id)
    if match:
        mode_index = int(match.group(1))
        # Construct the symbol IDs that depend on the mode selection
        symbol_id_map  = symbolsToUpdateOnModeChange(mode_index)
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
    reg_defaults = {}  # Dictionary to store default values for each register
    reg_por_set = ""   # Initialize the regPorSet output string
    
    module_name = adcInstanceName.getValue()    
    match = re.search(r'\d+$', module_name) 
    instance_number = match.group(0) if match else ""   # Extract instance number
    
    # Loop through each register and fetch its default value
    for reg in registers:
        reg_name = "{}{}{}".format(register_group, instance_number, reg)  # Form key as register_group + instanceNumber + reg
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

def processBitfield(bitfield, remove_prefix=False):
    dict = {}
    caption = bitfield.getAttribute("caption")
    if caption.lower() != "reserved":  # skip (unused) reserved fields
        if remove_prefix and caption.startswith("AD1"):
            caption = caption[3:]
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
    for bitfield in valueNodes:
        processed_bitfield = processBitfield(bitfield, remove_prefix=True)
        if processed_bitfield:
            optionList.append(processed_bitfield)
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

def create_unique_suffix(prefix, index, suffix):
    """Generate a unique suffix based on a pattern."""
    return "{}_{}_{}".format(prefix, index, suffix)


def create_unique_symbolId(prefix, suffix):
    return "{}_{}".format(prefix,suffix)

def update_keys(option_list):
    for item in option_list:
        # Extract the original key
        original_key = item['key']
        
        # Update the key to the desired format
        updated_key = u'AN{}'.format(original_key[-1])  # Get the last character and format it
        
        # Assign the updated key back to the item
        item['key'] = updated_key

    return option_list


def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield, parentNode = None): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            symbolKey = valueGroupEntry       
            optionList = getBitfieldOptionList(valGroup)   
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, parentNode )
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp 

def create_boolean_symbol(
    component, unique_id, parent_node, label, default_value, index=None
):
    symbol_id = create_unique_symbolId(unique_id,"Boolean")
    symbol = component.createBooleanSymbol(symbol_id, parent_node)
    symbol.setLabel(label)
    symbol.setDefaultValue(default_value)
    symbol.setVisible(True)
    return symbol


##################################################################################
############################ Clock calculations start ##################################
##################################################################################


def getFormattedAdcClkFreq():
    return getClockValue()


def getClockValue():
    clk_freq = Database.getSymbolValue("core", "ADCHS_CLOCK_FREQUENCY")
    if clk_freq is not None:
        return clk_freq
    return "20000"


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


##################################################################################
############################ Clock calculations end ##################################
##################################################################################


def configure_adc_channel(adcComponent, i, adcChannel,comparatorLowThreshold,comparatorHighThreshold,sampleCountThreshold):
    """Configures the ADC channel related symbols."""

    # channelName = "{}{}".format(CHANNEL_PREFIX, i)
    channelName = "ch{}channelUsed".format(i)
    channelMenu = adcComponent.createBooleanSymbol(channelName, adcChannel)
    channelMenu.setLabel(CHANNEL_PREFIX + " " + str(i))
    channelMenu.setDefaultValue(False)
    channelMenu.setDependencies(updateChannelSymbolVisibility, [channelName])

        

    # ANx
    con1Register = CHCON1.format(i)

    # anxMenu = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, PINSEL_KEY, channelMenu)
    # anxMenu.setVisible(False)
    # anxMenu.setLabel(ANX_LABEL)
  
    # # Trigger Source
    triggerSourceMenu = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, TRG1SRC_KEY, channelMenu)
    triggerSourceMenu.setLabel(TRIGGER_SOURCE_1_LABEL)
    triggerSourceMenu.setVisible(False)

    # # Sample Time
    sampleTime = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, SAMC_KEY, channelMenu)
    sampleTime.setLabel(SAMPLING_TIME_LABEL)
    sampleTime.setVisible(False)

    # # Data Format
    dataFormatMenu = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, FRAC_KEY, channelMenu)
    dataFormatMenu.setLabel(DATA_FORMAT_LABEL)
    dataFormatMenu.setVisible(False)

    # # Interrupt
    channelInterrupt = "ch{}IntEnable".format(i)
    channel_Interrupt = adcComponent.createBooleanSymbol(channelInterrupt, channelMenu)
    channel_Interrupt.setLabel("Enable Interrupt")
    channel_Interrupt.setDefaultValue(False)
    channel_Interrupt.setVisible(False)
    # channel_Interrupt.setDependencies(updateChannelIntEnable, [channelInterrupt])

    # Interrupt Symbols from ATDF for Code Generation 
    compPrefix = AD
    compInstance = adcComponent.getID().upper().replace(ADC,"") 
    # Add comparator interrupt (e.g., CMP0, CMP1, etc.) to the interrupt list
    interruptList = ["CH{}".format(i)]
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    createInterruptSymbols(adcComponent,intSymbolMap)


    # EIEN 
    eienSymkey = AD+"_"+con1Register+"__"+"EIEN"
    eienSym = adcComponent.createIntegerSymbol(eienSymkey, None)
    eienSym.setMin(0)
    eienSym.setMax(1)
    eienSym.setVisible(False)


    # NINSEL 
    negPinSymkey = AD+"_"+con1Register+"__"+"NISEL"
    negPin = adcComponent.createIntegerSymbol(negPinSymkey, None)
    negPin.setVisible(False)

    # DIFF 
    diffSymkey = AD+"_"+con1Register+"__"+"DIFF"
    diffSym = adcComponent.createIntegerSymbol(diffSymkey, None)
    diffSym.setVisible(False)


    # Mode Configuration
    configure_mode_configuration(adcComponent,channelMenu,con1Register, i, sampleCountThreshold)

    # Comparator Configuration
    con2Register = CHCON2.format(i)
    configure_comparator_configuration(adcComponent,channelMenu,con2Register,comparatorLowThreshold,comparatorHighThreshold,i)


def configure_mode_configuration(adcComponent,channelMenu,con1Register,index,sampleCountThreshold):
    """Configures the mode related symbols for a given channel."""
    
    mode_prefix = "{}{}".format(MODE, index)
    adcMode = adcComponent.createMenuSymbol(mode_prefix, channelMenu)
    adcMode.setLabel(MODE_CONFIGURATION_LABEL)
    adcMode.setVisible(False)

    # # Mode Selection
    modeMenu_symbol = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, MODE_KEY, adcMode)
    modeMenu_symbol.setLabel(MODE_SELECTION_LABEL)
    modeMenu_id = AD_CHxCON1__MODE.format(index)
    modeMenu_symbol.setDependencies(updateSymbolVisibilityByModeSelection, [modeMenu_id])
    # modeMenu_symbol.setDependencies(updateAnyChannelWithIntOrWinConversion, [modeMenu_id])

    # # Sample Count
    sampleCountKey = "AD_"+CHxCNT.format(index)+"__CNT"
    sampleCount = adcComponent.createHexSymbol(sampleCountKey, adcMode)
    sampleCount.setLabel(SAMPLE_COUNT)
    sampleCount_defaultValue = getSettingBitDefaultValue(ADC, AD, CHxCNT.format(index) , CNT_KEY)
    sampleCount.setMin(0)
    sampleCount.setDefaultValue(sampleCount_defaultValue)
    sampleCount.setMax(sampleCountThreshold) #to do claculate and get as argument  maxThreshold
    sampleCount.setVisible(False)

    # # Secondary Accumulator
    secondaryAccumlatorEnable = adcComponent.createBooleanSymbol(AD_CHx__SECONDARY_ACCUMULATOR.format(index),adcMode)
    secondaryAccumlatorEnable.setLabel(SECONDARY_ACCUMULATOR_LABEL)
    secondaryAccumlatorEnable.setVisible(False)
    secondaryAccumlatorEnable.setDefaultValue(False)
    secondaryAccumlatorEnable.setDependencies(updateAccro, [AD_CHx__SECONDARY_ACCUMULATOR.format(index)])


    # # Trigger Source 2
    triggerSourceMenu = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, TRG2SRC_KEY, adcMode)
    triggerSourceMenu.setVisible(False)
    triggerSourceMenu.setLabel(TRIGGER_SOURCE_2_LABEL)

    # # OverSampling Format
    overSamplingMenu = createKeyValueSetSymbol(adcComponent, ADC, AD, con1Register, ACCNUM_KEY, adcMode)
    overSamplingMenu.setLabel(OVERSAMPLING_OPTIONS_LABEL)
    overSamplingMenu.setVisible(False)

    # OverSampling BurstMode
    con2Register = CHCON2.format(index)
    overSamplingBurstMode = createKeyValueSetSymbol(adcComponent, ADC, AD, con2Register, ACCBRST_KEY, adcMode)
    overSamplingBurstMode.setLabel(OVERSAMPLING_BURST_MODE_LABEL)
    overSamplingBurstMode.setVisible(False)

    # ACCRO bit set when SecAccu set
    con2Register = CHCON2.format(index)
    accroSymkey = AD+"_"+con2Register+"__"+"ACCRO"
    accroSym = adcComponent.createStringSymbol(accroSymkey, None)
    accroSym.setVisible(False)



def configure_comparator_configuration(adcComponent, channelMenu,con2Register,comparatorLowThreshold,comparatorHighThreshold, index):
    """Configures the comparator related symbols for a given channel."""

    # Comparator Enable
    cmpUsed = "ch{}cmpUsed".format(index)
    comparatorEnable = adcComponent.createBooleanSymbol(cmpUsed,channelMenu)
    comparatorEnable.setLabel(ENABLE_LABEL)
    comparatorEnable.setDefaultValue(False)
    comparatorEnable.setDependencies(updateComparatorSymbolVisibility, [cmpUsed])

    #Comparator Format
    comparatorEvent = createKeyValueSetSymbol(adcComponent, ADC, AD, con2Register, CMPMOD, comparatorEnable)
    comparatorEvent.setLabel(COMPARATOR_EVENT_LABEL)
    comparatorEvent.setVisible(False)
    

    # CMP LOW
    cmpLowKey = "AD_"+CHxCMPLO.format(index)
    cmpLowMenu = adcComponent.createHexSymbol(cmpLowKey, comparatorEnable)
    cmpLowMenu.setLabel(SELECT_CMP_LOW_LABEL)
    cmpLowMenu_defaultValue = getSettingBitDefaultValue(ADC, AD, CHxCMPLO.format(index), CMPLO)
    cmpLowMenu.setMin(0)
    cmpLowMenu.setDefaultValue(cmpLowMenu_defaultValue)
    cmpLowMenu.setMax(comparatorLowThreshold)
    cmpLowMenu.setVisible(False)
  

    # CMP HIGH
    cmpHighKey = "AD_"+CHxCMPHI.format(index)
    cmpHighMenu = adcComponent.createHexSymbol(cmpHighKey, comparatorEnable)
    cmpHighMenu.setLabel(SELECT_CMP_HIGH_LABEL)
    cmpHighMenu_defaultValue = getSettingBitDefaultValue(ADC, AD, CHxCMPHI.format(index), CMPHI)
    cmpHighMenu.setMin(0)
    cmpHighMenu.setDefaultValue(cmpHighMenu_defaultValue)
    cmpHighMenu.setMax(comparatorHighThreshold)
    cmpHighMenu.setVisible(False)
   

    # Interrupt
    cmpInterrupt = "cmp{}IntEnable".format(index)
    cmp_Interrupt = adcComponent.createBooleanSymbol(cmpInterrupt, comparatorEnable)
    cmp_Interrupt.setLabel("CMP Interrupt")
    cmp_Interrupt.setDefaultValue(False)
    cmp_Interrupt.setVisible(False)
    # cmp_Interrupt.setDependencies(updateCmpIntEnable,[cmpInterrupt])

    # Interrupt Symbols from ATDF for Code Generation 
    compPrefix = AD
    compInstance = adcComponent.getID().upper().replace(ADC,"") 
    # Add comparator interrupt (e.g., CMP0, CMP1, etc.) to the interrupt list
    interruptList = ["CMP{}".format(index)]

    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    createInterruptSymbols(adcComponent,intSymbolMap)

channelStatusList = []
channelInterruptList  = []
cmpInterruptList  = []
modeSelectionList =[]
secAccList= []


def instantiateComponent(adcComponent):
    global adcInstanceName, num_channels,SEC_ACCUMULATOR_CONST,instanceNumber, channelStatusList,channelInterruptList,cmpInterruptList,modeSelectionList, secAccList


    adcInstanceName = adcComponent.createStringSymbol(ADC_INSTANCE_NAME, None)  
    adcInstanceName.setVisible(False)
    adcInstanceName.setDefaultValue(adcComponent.getID().upper())
    module_name = adcInstanceName.getValue()
    Log.writeInfoMessage("Running " + module_name)

    adc_instance_num = adcComponent.getID().upper().replace(ADC, "")
    instanceNumber = adcComponent.createStringSymbol(SPI_INSTANCE_NUM, None)
    instanceNumber.setDefaultValue(adc_instance_num)
    instanceNumber.setVisible(False)

    instanceNumber = int(adc_instance_num)
    SEC_ACCUMULATOR_CONST = getParameterValue(ADC, module_name , SEC_ACC)


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

    tadCore = adcComponent.createStringSymbol(TAD_CORE, adcMenu)
    tadCore.setLabel(TAD_CORE_LABEL)
    tadCore.setValue(getTsrcDisplay())
    tadCore.setVisible(True)

    conversionTime = adcComponent.createStringSymbol(CONVERSION_TIME, adcMenu)
    conversionTime.setLabel(CONVERSION_TIME_LABEL)
    conversionTime.setValue(conversionTimeDisplay())
    conversionTime.setVisible(True)

    conversionRepeatTimer = createKeyValueSetSymbol(adcComponent, ADC, AD, CON, RPTCNT, adcMenu)
    conversionRepeatTimer.setLabel(CONVERSION_REPEAT_TIMER_LABEL)

    enableInputScan = adcComponent.createBooleanSymbol(ENABLE_INPUT_SCAN, adcMenu)
    enableInputScan.setLabel(ENABLE_INPUT_SCAN_LABEL)
    enableInputScan.setDefaultValue(False)
    resolution_bit_value = getParameterValue(ADC, module_name, RESOLUTION_BIT)
    resolution_bit = adcComponent.createStringSymbol(RESOLUTION_BIT, adcMenu)
    resolution_bit.setLabel(RESOLUTION_BIT_LABEL)
    resolution_bit.setValue(resolution_bit_value)
    resolution_bit.setVisible(True)
    resolution_bit.setReadOnly(True)

    is_pwm_gen_present_value = getParameterValue(ADC, module_name, IS_PWM_PRESENT)
    pwm_gen_present = adcComponent.createStringSymbol(IS_PWM_PRESENT, adcMenu)
    pwm_gen_present.setLabel(PWM_PRESENT_LABEL)
    pwm_gen_present.setValue(is_pwm_gen_present_value)
    pwm_gen_present.setVisible(True)
    pwm_gen_present.setReadOnly(True)

    # Channel Configuration
    adcChannelConfiguration = adcComponent.createMenuSymbol(ADC_CHANNEL_CONFIGURATION, adcMenu)
    adcChannelConfiguration.setLabel(ADC_CHANNEL_CONFIGURATION_LABEL)

    comparatorLowThreshold = maxThreshold(ADC, AD, CHxCMPLO.format(instanceNumber), CMPLO)
    comparatorHighThreshold = maxThreshold(ADC, AD, CHxCMPHI.format(instanceNumber), CMPHI)
    sampleCountThreshold = maxThreshold(ADC, AD, CHxCNT.format(instanceNumber), CNT_KEY)
    num_channels = getParameterValue(ADC, module_name, NUMBER_OF_CHANNELS)
    # Convert to integer if not None
    if num_channels is not None:
        num_channels = int(num_channels)
        Log.writeInfoMessage("Number of channels: {}".format(num_channels))

    # Loop to configure all channels
    for i in range(num_channels):
        configure_adc_channel(adcComponent, i, adcChannelConfiguration,comparatorLowThreshold,comparatorHighThreshold,sampleCountThreshold)



  ###################################################################################################
  ####################################### Code Generation  ##########################################
  ###################################################################################################


    moduleName = adcComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue(adcComponent.getID().upper())
    moduleName.setVisible(False)

    maxChannel = adcComponent.createIntegerSymbol("maxChannel", None)
    maxChannel.setDefaultValue(num_channels)
    maxChannel.setVisible(False)

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
    modeSelectionList = [AD_CHxCON1__MODE.format(k) for k in range(num_channels)]
    any_channel_with_int_or_win_conversion.setDependencies(updateChannelConversionAndAccumulatorStatus, modeSelectionList)

    
    # Any Channel With Integration and Secondary Accumulator 
    anyChWithIntConversionAndSecAcc = adcComponent.createBooleanSymbol("chWithIntConversionAndSecAcc", None)
    anyChWithIntConversionAndSecAcc.setLabel("Any Channel with Integration and Secondary Accumulator")
    anyChWithIntConversionAndSecAcc.setDefaultValue(False)
    anyChWithIntConversionAndSecAcc.setVisible(False)
    # List to track if channels having secondary accumulator
    secAccList = [AD_CHx__SECONDARY_ACCUMULATOR.format(k) for k in range(num_channels)]
    any_channel_with_int_or_win_conversion.setDependencies(updateChannelConversionAndAccumulatorStatus, secAccList)

   
    # String symbol to represent the secondary accumulator for Channel 19
    ch19SecAcc = adcComponent.createStringSymbol(CH19SECACC, None)
    ch19SecAcc.setLabel("Channel 19 Secondary Accumulator")
    ch19SecAcc.setDefaultValue("")
    ch19SecAcc.setVisible(False)
    ch19SecAcc.setDependencies(updateChannel19SecAccSetting, [AD_CHx__SECONDARY_ACCUMULATOR.format(19)])

    # String symbol for the POR (Power-On Reset) values of registers
    registers = ["CON", "DATAOVR", "STAT", "RSTAT", "CMPSTAT", "CH0CON1"]
    reg_por_set = create_reg_por_set_string(ADC, AD, registers)
    regPorSet = adcComponent.createStringSymbol("regPorSet", None)
    regPorSet.setLabel("Register Power-On Reset Values")
    regPorSet.setDefaultValue(reg_por_set)  # `reg_por_set` is the formatted string generated from create_reg_por_set_string
    regPorSet.setVisible(False)

    # String symbol for the powerMode
    powerMode = adcComponent.createStringSymbol("AD_CON__MODE", None)
    powe_mode_value = getValueByCaption("ADC", "AD_CON__MODE", "ON")
    powerMode.setValue(powe_mode_value)
    powerMode.setVisible(False)

    # String symbol for the ACCBRST
    # accBrst = adcComponent.createIntegerSymbol("AD_CH0CON2__ACCBRST", None)
    # accBrst.setDefaultValue(0)
    # accBrst.setVisible(True)
    # accBrst.setDependencies(getOverSamplingBurstMode,[AD_CHx__OVERSAMPLING_BURST_MODE.format()])

    #File Handling 

    configName = Variables.get("__CONFIGURATION_NAME")
  
    acHeader1File = adcComponent.createFileSymbol("ADC_HEADER", None)
    acHeader1File.setSourcePath("../peripheral/adc_05404/templates/plib_adc.h.ftl")
    acHeader1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".h")
    acHeader1File.setMarkup(True)
    acHeader1File.setDestPath("/peripheral/adc/")
    acHeader1File.setProjectPath("config/" + configName + "/peripheral/adc/")
    acHeader1File.setType("HEADER")

    adcCommonHeaderFile = adcComponent.createFileSymbol("ADC_COMMON_HEADER", None)
    adcCommonHeaderFile.setSourcePath("../peripheral/adc_05404/templates/plib_adc_common.h.ftl")
    adcCommonHeaderFile.setOutputName("plib_adc_common.h")
    adcCommonHeaderFile.setDestPath("peripheral/adc/")
    adcCommonHeaderFile.setProjectPath("config/" + configName +"/peripheral/adc/")
    adcCommonHeaderFile.setType("HEADER")
    adcCommonHeaderFile.setMarkup(True)

    acSource1File = adcComponent.createFileSymbol("ADC_SOURCE", None)
    acSource1File.setSourcePath("../peripheral/adc_05404/templates/plib_adc.c.ftl")
    acSource1File.setOutputName("plib_" + adcInstanceName.getValue().lower() + ".c")
    acSource1File.setMarkup(True)
    acSource1File.setDestPath("/peripheral/adc/")
    acSource1File.setProjectPath("config/" + configName + "/peripheral/adc/")
    acSource1File.setType("SOURCE")

    acSystemInitFile = adcComponent.createFileSymbol("ADC_SYS_INIT", None)
    acSystemInitFile.setType("STRING")
    acSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    acSystemInitFile.setSourcePath("../peripheral/adc_05404/templates/system/initialization.c.ftl")
    acSystemInitFile.setMarkup(True)

    acSystemDefFile = adcComponent.createFileSymbol("ACC_SYS_DEF", None)
    acSystemDefFile.setType("STRING")
    acSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    acSystemDefFile.setSourcePath("../peripheral/adc_05404/templates/system/definitions.h.ftl")
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
#                      updateAnyChannelWithIntOrWinConversion,updateChannel19SecAccSetting, updateAccro
##################################################################################################################

# Callback function to update 'isChannelSelected' based on individual channel selections
def updateAnyChannelSelected(symbol, event):
    channel_id = event["id"] 
    component = event[SOURCE]
    Log.writeInfoMessage("Channel selection changed: {}".format(channel_id))

    # Update 'isChannelSelected' based on any channel being selected
    symbol.setValue(any([component.getSymbolValue(dep) for dep in channelStatusList]))

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

    # Update the channelIntEnable symbol
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
        mode = component.getSymbolByID(AD_CHxCON1__MODE.format(i)).getSelectedKey()
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

    # Update symbols if conditions are met, with limited logging
    if anyChannelWithIntOrWinConversionSymbol.getValue() != hasIntOrWinMode:
        anyChannelWithIntOrWinConversionSymbol.setValue(hasIntOrWinMode)
        Log.writeInfoMessage("'anyChannelWithIntOrWinConversion' updated to: {}".format(hasIntOrWinMode))

    if chWithIntConversionAndSecAccSymbol.getValue() != hasIntAndSecAcc:
        chWithIntConversionAndSecAccSymbol.setValue(hasIntAndSecAcc)
        Log.writeInfoMessage("'chWithIntConversionAndSecAcc' updated to: {}".format(hasIntAndSecAcc))

# Callback function to update 'ch19SecAcc' based on Channel 19's mode, secondary accumulator, and usage status

def updateChannel19SecAccSetting(symbol, event):
    component = event[SOURCE]

    Log.writeInfoMessage("Callback triggered: Updating 'ch19SecAcc' based on Channel 19's mode selection, secondary accumulator, and usage status.")

    # Retrieve Channel 19-specific symbols
    ch19Used = component.getSymbolByID(CH19Used)  # Replace with actual ID if different
    ch19SecAcc = component.getSymbolByID(CH19SECACC)
    mode_select = component.getSymbolByID(AD_CHxCON1__MODE.format(19))
    secondary_accumulator_enabled = component.getSymbolByID(AD_CHx__SECONDARY_ACCUMULATOR.format(19)).getValue()

    # Define conditions for Channel 19: Integration mode, Secondary Accumulator enabled, and Channel 19 in use
    ch19_with_int_and_sec_acc = (
        mode_select.getSelectedKey() == INTEGRATION_MODE and
        secondary_accumulator_enabled and
        ch19Used.getValue()
    )

    # Update ch19SecAcc based on the conditions
    if ch19_with_int_and_sec_acc:
        ch19SecAcc.setValue(CH19_SEC_ACC19_VALUE)
        Log.writeInfoMessage("Channel 19 Secondary Accumulator set to ACC19.")
    else:
        ch19SecAcc.setValue("")
        Log.writeInfoMessage("Channel 19 Secondary Accumulator disabled.")

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
    accroSymKey = "{}_{}__ACCRO".format(AD, CHCON2.format(channelNumber))
    accroSym = event.get("source").getSymbolByID(accroSymKey)

    if accroSym is None:
     Log.writeInfoMessage("ACCRO symbol '{}' not found for channel {}".format(accroSymKey, channelNumber))
     return
    
    # Set the ACCRO symbol value to '1' if SecAccu is enabled, otherwise to '0'
    accroValue = "1" if secAccuEnabled else "0"
    accroSym.setValue(accroValue)

    # Log the update status
    statusMessage = "enabled" if secAccuEnabled else "disabled"
    Log.writeInfoMessage("ACCRO set to '{}' (roll-over {}) for channel {}".format(accroValue, statusMessage, channelNumber))


def getChannelNumberFromEvent(event):
    # Regular expression to find the number between "CH" and "__"
    match = re.search(r"CH(\d+)__", event["id"])
    if match:
        # Return the channel number as an integer
        return int(match.group(1))
    return None
