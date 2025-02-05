"""*****************************************************************************
* Copyright (C) 2018-2019 Microchip Technology Inc. and its subsidiaries.
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

import re
import xml.etree.ElementTree as ET
import os.path
from collections import OrderedDict

CORE = "core"
CLK_SRC = "CLK_SRC"
CLK_FREQ = "CLK_FREQ"
MODULE_NAME = "PTG"
PTG = "PTG"
CON = "CON"
PTGDIV = "PTGDIV"
PTG_CON__PTGDIV = "PTG_CON__PTGDIV"
MIN_COUNT = 0x0001
MAX_COUNT = 0xffff
MILLI_SECOND_COMPENSATION = 1000
MICROSECOND_COMPENSATION  = 1000000

CLK_SRC_KEY = "CLK_SRC"
CLK_FREQ_KEY = "CLK_FREQ"
CLOCK_SETTINGS_KEY = "Clock_Settings"
WATCHDOG_TRIGGER_SETTINGS_KEY  = "WatchDog_And_TriggerSettings"
PTG_WDT = "PTGWDT"
PTG_ITM = "PTGITM"
STEP_SEQUENCE_QUEUE_KEY = "StepSequenceQueue"
STEP_SEQUENCE_KEY = "StepSequence"

STEP_MENU_KEY_TEMPLATE = "STEP{}_MENU"
STEP_CMD_KEY_TEMPLATE = "STEP{}_COMMAND"
COMMAND_OPTIONS_KEY_TEMPLATE = "STEP{}_OPTIONS"
STEP_OPTION_VALUE_KEY_TEMPLATE = "STEP{}_OPTION_VALUE"
PTG_INSTANCE_NAME_KEY = "PTG_INSTANCE_NAME"
CLK_COMMENT_KEY = "CLK_COMMENT"
MAX_STEP_SIZE_PARAM = "maxStepSize"
COMMAND_OPTIONS_PARAM = "ptgCommandOptions"
PTG_CON_PTGDIV = "PTG.CON.PTGDIV"
TIMER0_PERIOD_KEY = "timer0Period"
CALCULATED_TIMER0_PERIOD_KEY = "Calculated_Timer0Period"
PTGT0LIM = "PTGT0LIM"
TIMER1_PERIOD_KEY = "timer1Period"
CALCULATED_TIMER1_PERIOD_KEY = "Calculated_Timer1Period"
PTGT1LIM = "PTGT1LIM"
STEP_DELAY_KEY = "stepDelay"
CALCULATED_STEP_DELAY_KEY = "Calculated_StepDelay"
PTGSDLIM = "PTGSDLIM"
COUNTER0_KEY = "PTGC0LIM"
COUNTER1_KEY = "PTGC1LIM"
HOLD_VALUE_KEY = "PTGHOLD"
ADJUST_VALUE_KEY = "PTGADJ"
LITERAL_VALUE_KEY = "PTGL0"
INTERRUPT_SETTINGS_KEY = "Interrupt_Settings"
INTERRUPT_MODE_TEMPLATE = "{}Interrupt"
INTERRUPT = "Interrupt"
IC_PREFIX = "INTC"
INTERRUPT_COMMENT = "INTERRUPT_COMMENT"
WARNING_INTERRUPT_DISABLED_LABEL = (
    "Warning!!! Peripheral Interrupt is Disabled in Interrupt Manager"
)

INTERRUPT_SYMBOLS = ["PTG0", "PTG1", "PTG2", "PTG3", "PTGWDT"]
# Interrupt List
# List of possible interrupt types for the SPI module.
interruptList = ["STEP", "WDT", "0","1","2","3"]
intList = []
ptgInterruptList  = []
maxStepSize = 0
interruptEnableList = []
interruptHandlerLockList = []
ptgIntSet = set()
PTGInteruptList = ["PTG0Interrupt","PTG1Interrupt","PTG2Interrupt","PTG3Interrupt"]




# ATDF Helper Functions start

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


CMD_OPTIONS_RAW  = getParameterValue(PTG, PTG, COMMAND_OPTIONS_PARAM)
CMD_OPTIONS = CMD_OPTIONS_RAW.split(',')
clock_gen_num = ''.join(filter(str.isdigit, str(getParameterValue(PTG, PTG, "clockGeneratorNum"))))
CLK_GEN10_FREQ = "clkGen{}OutFrequency".format(clock_gen_num)


def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value


def getSettingBitDefaultValue(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        regDefaultVal = registerNode.getAttribute("initval")
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return getDefaultVal(regDefaultVal, bitMask)
    return 0


def maxThreshold(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return int(bitMask, 0)
    return 0


def getValueGroupName(moduleName, registerGroup, register, bitfield):
    bitNode = getBitField(moduleName, registerGroup, register, bitfield)
    if bitNode != None:
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


def addKeystoKeyValueSymbol(bitSymbol, bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey(ii["key"], ii["value"], ii["desc"])


def getKeyValuePairBasedonValue(value, keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return (
                index  # return occurrence of <bitfield > entry which has matching value
            )
        index += 1
    print("find_key: could not find value in dictionary")  # should never get here
    return ""


def createKeyValueSetSymbol(
    component, moduleName, registerGroup, register, bitfield, parentNode=None
):
    valueGroupEntry = getValueGroupName(moduleName, registerGroup, register, bitfield)
    valGroup = getValueGroup(moduleName, valueGroupEntry)
    if valGroup != None:
        symbolKey = valueGroupEntry
        optionList = getBitfieldOptionList(valGroup)
        valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, parentNode)
        valueGroupEntryComp.setLabel(symbolKey)
        defaultValue = getSettingBitDefaultValue(
            moduleName, registerGroup, register, bitfield
        )
        valueGroupEntryComp.setDefaultValue(
            getKeyValuePairBasedonValue(defaultValue, optionList)
        )
        valueGroupEntryComp.setOutputMode("Value")
        valueGroupEntryComp.setDisplayMode("Description")
        addKeystoKeyValueSymbol(valueGroupEntryComp, optionList)
        return valueGroupEntryComp


def getBitfieldMask(moduleName, registerGroup, register, bitfield):

    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)

    if registerNode != None:
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return int(bitMask, 16)
    return 0

# ATDF Helper Functions end


def maxThreshold(moduleName, registerGroup, register, bitfield):
    regPath = (
        '/avr-tools-device-file/modules/module@[name="'
        + moduleName
        + '"]/register-group@[name="'
        + registerGroup
        + '"]/register@[name="'
        + register
        + '"]'
    )
    registerNode = ATDF.getNode(regPath)
    if registerNode != None:
        bitNode = getBitField(moduleName, registerGroup, register, bitfield)
        if bitNode != None:
            bitMask = bitNode.getAttribute("mask")
            return int(bitMask, 0)
    return 0

def calculateClockValueAfterScaling(clockValue, preScalerValue):
    if preScalerValue:
        return clockValue / preScalerValue
    return 0

def getClockValueAfterScaling(symbol, event):
    component = symbol.getComponent()
    clockValue = Database.getSymbolValue(CORE, CLK_GEN10_FREQ)
    clkDivSymbol = component.getSymbolByID(PTG_CON__PTGDIV)
    preScalerValue  = int(clkDivSymbol.getSelectedKey())
    # Perform scaling if values are valid
    clkValueAfterScaling = calculateClockValueAfterScaling(clockValue, preScalerValue)
    
    return clkValueAfterScaling


def clkFreqDependency(clkFreqSymbol, event):
    component = clkFreqSymbol.getComponent()
    clockValue = Database.getSymbolValue(CORE, CLK_GEN10_FREQ)
    preScalerValue = int(component.getSymbolByID(PTG_CON__PTGDIV).getSelectedKey())
    if preScalerValue:
     clkFreqSymbol.setValue(int( clockValue/ preScalerValue))


def updateClockComment(symbol, event):

    if event["value"] == 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def calculate_min_max(clock_frequency):
    if clock_frequency:
        ticktime = 1.0 / clock_frequency
        max_time_out_value = MAX_COUNT * ticktime * MICROSECOND_COMPENSATION
        max_time_out_value = round(max_time_out_value, 4)

        min_time_out_value = MIN_COUNT * ticktime * MICROSECOND_COMPENSATION
        min_time_out_value = round(min_time_out_value, 4)
    else:
        max_time_out_value = 0.0
        min_time_out_value = 0.0

    return max_time_out_value, min_time_out_value


def update_min_max(symbol, event):
    clock_frequency = event["value"]
    # Use the pure function to calculate min and max
    max_time_out_value, min_time_out_value = calculate_min_max(clock_frequency)
    symbol.setMin(min_time_out_value)
    symbol.setMax(max_time_out_value)
    Log.writeInfoMessage("update_min_max: Updated symbol '{}' with Min: {}, Max: {}, Clock Frequency: {}.".format(symbol.getID(), min_time_out_value, max_time_out_value, clock_frequency))


#  Calculate the timer period based on clock frequency and timer value,and update the corresponding event symbols.

def get_calculated_timer_period(timerPeriodSymbol, event):

    eventID = event["id"]
    eventValue = event["value"]

    # Initialize variables
    clock_value_after_scaling = 0
    timerValue = 0
    event_symbols = {}

    if eventID == "CLK_FREQ":
        clock_value_after_scaling = eventValue

        # Retrieve timer values
        timers = {
            "PTGT0LIM": timerPeriodSymbol.getComponent().getSymbolValue("timer0Period"),
            "PTGT1LIM": timerPeriodSymbol.getComponent().getSymbolValue("timer1Period"),
            "PTGSDLIM": timerPeriodSymbol.getComponent().getSymbolValue("stepDelay"),
        }

        # Calculate and update clock cycles for each timer
        for symbolID, timerValue in timers.items():
            requiredClockCycles = (timerValue * clock_value_after_scaling) / MICROSECOND_COMPENSATION
            timerPeriodSymbol.getComponent().getSymbolByID(symbolID).setValue(int(requiredClockCycles))

    else:
        timerValue = eventValue
        clock_value_after_scaling = timerPeriodSymbol.getComponent().getSymbolValue(CLK_FREQ_KEY)

        # Fetch the event symbols dynamically
        event_symbols = {
            "timer0Period": event["source"].getSymbolByID("PTGT0LIM"),
            "timer1Period": event["source"].getSymbolByID("PTGT1LIM"),
            "stepDelay": event["source"].getSymbolByID("PTGSDLIM"),
        }

        requiredClockCycles = (timerValue * clock_value_after_scaling) / MICROSECOND_COMPENSATION
        int_cycles = int(requiredClockCycles)

        # Update the appropriate event symbol
        event_symbol = event_symbols.get(eventID)
        if event_symbol:
            event_symbol.setValue(int_cycles)

        # Log success message for the updated timer
        Log.writeInfoMessage("Successfully updated symbol '{}'.".format(event_symbol.getID()))
        

def getOperationParameters(module_name, instance_name, target_caption=""):
    xpath_query = (
        "/avr-tools-device-file/devices/device/peripherals/module@[name=\"{0}\"]/"
        "instance@[name=\"{1}\"]/parameters"
    ).format(module_name, instance_name)

    parameters_node = ATDF.getNode(xpath_query)
    parameter_list = []

    if parameters_node is not None:
        for param_node in parameters_node.getChildren():
            caption = param_node.getAttribute("caption")
            if not target_caption or caption == target_caption:
                parameter_list.append({
                    "name": param_node.getAttribute("name"),
                    "value": param_node.getAttribute("value"),
                    "caption": caption
                })

    return parameter_list

def populateCommandOptions(module_name, instance_name):
    command_options = {}

    for command in CMD_OPTIONS:
        if command == "PTGCTRL":
            # Fetch all parameters and filter subcategories of PTGCTRL
            all_parameters = getOperationParameters(module_name, instance_name, "")
            ptgctrl_subcategories = ["PTGCTRLSTEPDELAY", "PTGCTRLTIMER", "PTGCTRLSWTRIG", "PTGCTRLBROADCAST"]
            ptgctrl_parameters = [
                param for param in all_parameters if param.get("caption") in ptgctrl_subcategories
            ]
            # Group all PTGCTRL subcategory parameters under PTGCTRL
            command_options["PTGCTRL"] = [
                {"label": param["name"].replace("_", " ").strip(), "value": param["value"]}
                for param in ptgctrl_parameters
            ]
            # Add the default "NOP" entry
            command_options["PTGCTRL"].append({
                "label": "NOP",
                "value": "0x0"
            })

        else:
            # Fetch parameters for the current caption
            parameters = getOperationParameters(module_name, instance_name, command)
            command_options[command] = [
                {"label": param["name"].replace("_", " ").strip(), "value": param["value"]}
                for param in parameters
            ]
    return command_options

command_options = populateCommandOptions(PTG, PTG)
ptgctrl_options = [option["label"] for option in command_options["PTGCTRL"]]


def updateCommandOptions(symbol, event):
    selectedCommand = event["value"] 
    options = [cmd["label"] for cmd in command_options.get(selectedCommand, [])]  
    cmd_id = event["id"]
    # Extract the step number from the cmd_id
    step_number = cmd_id.replace("STEP", "").replace("_COMMAND", "")
    cmd_option_id = COMMAND_OPTIONS_KEY_TEMPLATE.format(step_number)
    cmd_options_symbol = event["source"].getSymbolByID(cmd_option_id)
    cmd_options_symbol.setRange(options)
    Log.writeInfoMessage(
        "updateCommandOptions: Updated options for command '{}', step number '{}'. "
        "Options count: {}, First option: '{}'".format(
            selectedCommand,
            step_number,
            len(options),
            options[0] if options else "None"
        )
    )

def parseJumpState(description):
    match = re.search(r"STEP(\d+)", description)
    if match:
        return int(match.group(1))

def isJumpCommand(command):
    return command.startswith("PTGJMP")

def isInterruptCommand(command):
    return command == "PTGIRQ"


def setPtgInterruptWarnings(ptgInterruptCommentSymbol, event):
    # Define a map for interrupt-related options
    interrupt_map = {
        "Generate PTG Interrupt 0": "PTG0",
        "Generate PTG Interrupt 1": "PTG1",
        "Generate PTG Interrupt 2": "PTG2",
        "Generate PTG Interrupt 3": "PTG3"
    }
     # Initial check for all commands
    interrupt_command_found = False
    for step_number in range(maxStepSize):
        command = event["source"].getSymbolValue(STEP_CMD_KEY_TEMPLATE.format(step_number))
        if isInterruptCommand(command):
            interrupt_command_found = True

    # If no interrupt commands are found, exit early
    if not interrupt_command_found:
        ptgIntSet.clear()
        ptgInterruptCommentSymbol.setVisible(False)
        print("No interrupt commands found. Exiting...")
        return

    if event["id"] in PTGInteruptList:
        interrupt_name = event["id"].replace("Interrupt", "")
        is_interrupt_enabled = event["source"].getSymbolValue(event["id"])
        if is_interrupt_enabled:
            # Remove the interrupt from the set if it is enabled
            ptgIntSet.discard(interrupt_name)
        else:
            # Check if the interrupt command option is selected before adding
            option_found = False
            for step_number in range(maxStepSize):
                step_option = event["source"].getSymbolValue("STEP{}_OPTIONS".format(step_number))
                if step_option in interrupt_map and interrupt_map[step_option] == interrupt_name:
                    option_found = True
                    break

            if option_found and interrupt_name in interrupt_map.values():
                ptgIntSet.add(interrupt_name)

    else:
        # Iterate through all steps to determine the active interrupts
        ptgIntSet.clear()
        for step_number in range(maxStepSize):
            # Get the current option for this step
            step_option = event["source"].getSymbolValue("STEP{}_OPTIONS".format(step_number))
            # Check if the option is in the interrupt map
            if step_option in interrupt_map:
                interrupt_name = interrupt_map[step_option]
                symbolKey = interrupt_name + "Interrupt"
                is_interrupt_enabled = event["source"].getSymbolValue(symbolKey)
                if not is_interrupt_enabled:
                    ptgIntSet.add(interrupt_name)

    # Update the warning visibility and label
    showWarning = len(ptgIntSet) > 0
    ptgInterruptCommentSymbol.setVisible(showWarning)
    ptgInterruptCommentSymbol.setLabel(
        "*** Warning!!! Enable {} in Interrupts Settings Section ***".format(', '.join(ptgIntSet))
    )

    Log.writeInfoMessage("Interrupts that must be enabled in settings: {}".format(ptgIntSet))

       

def updatOptionValue(symbol, event):

    step_number = event["id"].replace("STEP", "").replace("_OPTIONS", "")
    option_value_symbol = event["source"].getSymbolByID(STEP_OPTION_VALUE_KEY_TEMPLATE.format(step_number))
    selected_option, command = event["value"], event["source"].getSymbolValue(STEP_CMD_KEY_TEMPLATE.format(step_number))
    
   # Find and process the matching option
    option_value = next(
        (int(option["value"][-1], 16) for option in command_options.get(command, []) if option["label"] == selected_option),
        None
    )

    # Adjust for jump commands
    if isJumpCommand(command):
      jump_state = parseJumpState(selected_option)
      if jump_state is not None and jump_state > 15:
       option_value = jump_state
    
    # Update option value
    if option_value is not None:
        option_value_symbol.setValue(option_value)
    
    Log.writeInfoMessage(
        "updateOptionValue: Processed step '{}'. Selected option: '{}', Command: '{}', "
        "Hexadecimal Value: '{}', Update Successful: {}.".format(
            step_number,
            selected_option,
            command,
            hex(option_value) if option_value is not None else "None",
            option_value is not None,
        )
    )

def getRegisterDefaultValue(module, register_group, register):
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

    reg_defaults = OrderedDict()  # Use OrderedDict to maintain the insertion order
    reg_por_set = ""   

    for reg in registers:
        reg_name = "{}{}".format(register_group, reg)  # Form key as register_group + reg , example : PTGCON
        reg_defaults[reg_name] = getRegisterDefaultValue(module, register_group, reg)
        
    # Format the output string with 4-space indentation per register
    for reg_name, default_val in reg_defaults.items():
        reg_por_set += "    {} = {};\n".format(reg_name, default_val)
    
    return reg_por_set

# Callback function to update 'isPtgInterruptEnabled' based on any interrupt enable/disable status
def updateAnyInterruptEnable(symbol, event):
    component = event["source"]   
    # Update the isPtgInterruptEnabled symbol
    symbol.setValue(any([component.getSymbolValue(dep) for dep in ptgInterruptList ]))

def showAllSteps(symbol, event):
    stepSequenceEnabled = event["value"]
    symbol.setVisible(stepSequenceEnabled)

# Interrupt related Helper Function
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three'
}
# Function to replace digits with words
def replace_digits_with_words(s):
    for digit, word in digit_to_word.items():
        s = s.replace(digit, word)
    return s

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
                    # intSymbolName1 = bitName.replace(compPrefix+compInstance,"").replace("IF","").lower() + "InterruptFlagBit"
                    intSymbolName = replace_digits_with_words(bitName.replace(compPrefix+compInstance,"").replace("IF","").lower() + "InterruptFlagBit")
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
                    intSymbolName = replace_digits_with_words(bitName.replace(compPrefix+compInstance,"").replace("IE","").lower() + "InterruptEnableBit")
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break                          
    
    for interrupt in interruptList:
        intSymbolName = replace_digits_with_words(interrupt.lower() + "IsrHandlerName")
        intSymbolMap[intSymbolName] = compPrefix + compInstance +interrupt+"_InterruptHandler"
    return intSymbolMap

def createInterruptSymbols(component,intSymbolMap):
    for key in intSymbolMap:
        interruptSymbol = component.createStringSymbol(key, None)
        interruptSymbol.setDefaultValue(intSymbolMap[key])
        interruptSymbol.setVisible(False)

def updateInterruptLists(interruptList):
    for interrupt in interruptList:
        intIndex = getVectorIndex(PTG + interrupt + INTERRUPT)
        interruptEnableList.append("{}.{}_{}_ENABLE".format(CORE, IC_PREFIX, intIndex))
        interruptHandlerLockList.append(
            "{}.{}_{}_HANDLER_LOCK".format(CORE, IC_PREFIX, intIndex)
        )

def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts"
    ).getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break
    return vector_index

def interruptEnableChange(symbol, event):
    interruptId = event["id"]
    intIndex = getVectorIndex(interruptId)
    # Set Database values based on the interrupt state
    enableSymbol = "INTC_{}_ENABLE".format(intIndex)
    lockSymbol = "INTC_{}_HANDLER_LOCK".format(intIndex)
    Database.setSymbolValue("core", enableSymbol, bool(event["value"]))
    Database.setSymbolValue("core", lockSymbol, bool(event["value"]))


    

def interruptStatusWarnings(symbol, event):
    match = re.search(r'INTC_(\d+)_ENABLE', event["id"])
    showWarning = False

    if match:
        vector_index = match.group(1)
        # Fetch the interrupt name and caption using the vector index
        interrupt_name, interrupt_caption = getInterruptNameAndCaptionByIndex(vector_index)   
        # Determine the interrupt symbol ID based on the type
        interrupt_symbol_id = interrupt_name
        label = interrupt_caption

        # Check the conditions
        if symbol.getComponent().getSymbolValue(interrupt_symbol_id) == True and Database.getSymbolValue("core", "INTC_{}_ENABLE".format(vector_index)) == False:
            # Add warning message if not already present
            if label not in intList:
                intList.append(label)
            showWarning = True
        else:
            # Remove the respective message if the interrupt is enabled
            if label in intList:
                intList.remove(label)

    # Determine if there's still a need to show a warning
    showWarning = len(intList) > 0

    # Update the symbol visibility and label
    symbol.setVisible(showWarning)
    symbol.setLabel("Warning!!! Enable {} in Interrupts Section of System module ".format(', '.join(str(i) for i in intList))) 

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


def updatePTGQPTRSymbol(symbol, event):
    # Extract the numeric step value from the combo box selection
    selected_step = event["value"]  # e.g., "Step 3"
    step_value = int(selected_step.split(" ")[1])  # Extract the number after "Step"
    # Update the PTGQPTR symbol value
    symbol.setValue(step_value)
    Log.writeInfoMessage("Updated PTGQPTR to {} based on selection:{}".format(step_value,selected_step))




def instantiateComponent(ptgComponent):

    global ptgInstanceName, maxStepSize

    ptgInstanceName = ptgComponent.createStringSymbol(PTG_INSTANCE_NAME_KEY, None)
    ptgInstanceName.setVisible(False)
    ptgInstanceName.setDefaultValue(ptgComponent.getID().upper())
    module_name = ptgInstanceName.getValue()
    Log.writeInfoMessage("Running " + ptgInstanceName.getValue())


    # Clock Settings
    clk_setting = ptgComponent.createMenuSymbol(CLOCK_SETTINGS_KEY, None)
    clk_setting.setLabel("Clock Settings")

    clkSrc = ptgComponent.createStringSymbol(CLK_SRC_KEY, clk_setting)
    clkSrc.setLabel("Clock Source")
    clkSrc.setDefaultValue("Clock Generator 10")
    clkSrc.setReadOnly(True)

    clkDiv = createKeyValueSetSymbol( ptgComponent, MODULE_NAME, PTG, CON, PTGDIV, clk_setting)
    clkDiv.setLabel("Clock Divider")
    clkDiv.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGCON")

    clkFreq = ptgComponent.createIntegerSymbol(CLK_FREQ_KEY, clk_setting)
    clkFreq.setLabel("Calculated Clock Frequency(Hz)")
    clkFreq.setReadOnly(True)
    clkFreq.setDefaultValue(Database.getSymbolValue(CORE, CLK_GEN10_FREQ))
    clkFreq.setDependencies(
        clkFreqDependency,
        [
            CORE + "." + CLK_GEN10_FREQ,
            PTG_CON__PTGDIV,
        ],
    )

    clkComment = ptgComponent.createCommentSymbol(CLK_COMMENT_KEY, clk_setting)
    clkComment.setLabel("Warning!!! Enable and configure Clock Generator 10 in Clock Section of System Module")
    clockValue = Database.getSymbolValue(CORE, CLK_GEN10_FREQ)
    clkComment.setVisible(clockValue == 0)
    clkComment.setDependencies(updateClockComment, [CLK_FREQ,  CORE + "." + CLK_GEN10_FREQ])


    ## WatchDog and Trigger Settings
    wdt_setting = ptgComponent.createMenuSymbol(WATCHDOG_TRIGGER_SETTINGS_KEY, None)
    wdt_setting.setLabel("Watchdog and Trigger Settings")

    # WatchDog
    watchDog = createKeyValueSetSymbol(ptgComponent, PTG, PTG, CON, PTG_WDT,wdt_setting)
    watchDog.setLabel("WatchDog Timeout (PTG Clock Cycles)")  
    watchDog.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGCON")



    # Input Trigger Mode
    ipTrgMode = createKeyValueSetSymbol(ptgComponent, PTG, PTG, CON, PTG_ITM,wdt_setting)
    ipTrgMode.setLabel("Input Trigger Mode")
    ipTrgMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGCON")

    ## Step Sequence Register Initial Values
    stepSequence = ptgComponent.createMenuSymbol(STEP_SEQUENCE_KEY, None)
    stepSequence.setLabel("Step Sequence Register Initial Values")

    max,min = calculate_min_max(clkFreq.getValue())
    delayTimeSettings = ptgComponent.createMenuSymbol("DELAY_TIME", stepSequence)
    delayTimeSettings.setLabel("Delay Time")


    # Timer 0 Time (ms)
    timer0Period = ptgComponent.createFloatSymbol(TIMER0_PERIOD_KEY,delayTimeSettings)
    timer0Period.setLabel("Timer0 Delay Time(us)")
    timer0Period.setMin(min)
    timer0Period.setMax(max)
    timer0Period.setDefaultValue(1)
    timer0Period.setDependencies(update_min_max,[CLK_FREQ_KEY])

    # Timer 1 Time (ms)
    timer1Period = ptgComponent.createFloatSymbol(TIMER1_PERIOD_KEY,delayTimeSettings)
    timer1Period.setLabel("Timer1 Delay Time(us)")
    timer1Period.setMin(min)
    timer1Period.setMax(max)
    timer1Period.setDefaultValue(1)
    timer1Period.setDependencies(update_min_max,[CLK_FREQ_KEY])


    # Step Delay Time (ms)
    stepDelay = ptgComponent.createFloatSymbol(STEP_DELAY_KEY,delayTimeSettings)
    stepDelay.setLabel("Step Delay Time(us)")
    stepDelay.setMin(min)
    stepDelay.setMax(max)
    stepDelay.setDefaultValue(1)
    stepDelay.setDependencies(update_min_max,[CLK_FREQ_KEY])


    # Default timer period values 
    clkSrcFreq = clkFreq.getValue()
    clkDivider = clkDiv.getKey(clkDiv.getValue())
    clkDivider = int(clkDivider)
    clkFreqAfterPrescaling = clkSrcFreq / clkDivider
    defaultTimerValues  = calculateDefaultCycles(clkFreqAfterPrescaling,timer0Period.getValue())

    # Timer0 Period
    ptg_T0LIM = ptgComponent.createHexSymbol(PTGT0LIM, delayTimeSettings)
    ptg_T0LIM.setDefaultValue(int(defaultTimerValues))
    ptg_T0LIM.setLabel("Timer0") 
    ptg_T0LIM.setVisible(True)
    ptg_T0LIM.setReadOnly(True)
    ptg_T0LIM.setMin(0x0)
    ptg_T0LIM.setMax(MAX_COUNT)
    ptg_T0LIM.setDependencies(get_calculated_timer_period,["timer0Period",CLK_FREQ_KEY])
    ptg_T0LIM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGT0LIM")


    # Timer1 Period
    ptg_T1LIM = ptgComponent.createHexSymbol(PTGT1LIM, delayTimeSettings)
    ptg_T1LIM.setDefaultValue(int(defaultTimerValues))
    ptg_T1LIM.setLabel("Timer1")
    ptg_T1LIM.setVisible(True)
    ptg_T1LIM.setReadOnly(True)
    ptg_T1LIM.setMin(0x0)
    ptg_T1LIM.setMax(MAX_COUNT)
    ptg_T1LIM.setDependencies(get_calculated_timer_period,["timer1Period",CLK_FREQ_KEY])
    ptg_T1LIM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGT1LIM")

    # Step Delay Period
    ptg_SDLIM = ptgComponent.createHexSymbol(PTGSDLIM, delayTimeSettings)
    ptg_SDLIM.setDefaultValue(int(defaultTimerValues))
    ptg_SDLIM.setLabel("Step Delay")
    ptg_SDLIM.setVisible(True)
    ptg_SDLIM.setReadOnly(True)
    ptg_SDLIM.setMin(0x0)
    ptg_SDLIM.setMax(MAX_COUNT)
    ptg_SDLIM.setDependencies(get_calculated_timer_period,["stepDelay", CLK_FREQ_KEY])
    ptg_SDLIM.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGSDLIM")

    # Counter 0
    counter0 = ptgComponent.createHexSymbol(COUNTER0_KEY,stepSequence)
    counter0.setLabel("Counter 0")
    counter0.setDefaultValue(MIN_COUNT)
    counter0.setMin(0x0)
    counter0.setMax(MAX_COUNT)
    counter0.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGC0LIM")


    # Counter 1
    counter1 = ptgComponent.createHexSymbol(COUNTER1_KEY,stepSequence)
    counter1.setLabel("Counter 1")
    counter1.setDefaultValue(MIN_COUNT)
    counter1.setMin(0x0)   
    counter1.setMax(MAX_COUNT)
    counter1.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGC1LIM")


    # Hold Value
    holdValue = ptgComponent.createHexSymbol(HOLD_VALUE_KEY,stepSequence)
    holdValue.setLabel("Hold Value")
    holdValue.setDefaultValue(MIN_COUNT)
    holdValue.setMin(0x0)   
    holdValue.setMax(MAX_COUNT)
    holdValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGHOLD")

    # Adjust Value check max range 
    adjustValue = ptgComponent.createHexSymbol(ADJUST_VALUE_KEY,stepSequence)
    adjustValue.setLabel("Adjust Value")
    adjustValue.setDefaultValue(MIN_COUNT)
    adjustValue.setMin(0x0) 
    adjustValue.setMax(MAX_COUNT)
    adjustValue.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGADJ")

    # Broadcast Trigger
    ptgBTESymbol = ptgComponent.createHexSymbol("PTGBTE",stepSequence)
    ptgBTESymbol.setMin(0x0)
    ptgBTESymbol.setMax(0xffffffff)  
    ptgBTESymbol.setVisible(True)
    ptgBTESymbol.setLabel("Broadcast Trigger(PTGBTE)")
    ptgBTESymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGBTE")


    ## Interrupt Settings
    interruptSettings = ptgComponent.createMenuSymbol(INTERRUPT_SETTINGS_KEY, None)
    interruptSettings.setLabel("Interrupt Settings")

    for symbol in INTERRUPT_SYMBOLS:
        interruptSymbol = ptgComponent.createBooleanSymbol(INTERRUPT_MODE_TEMPLATE.format(symbol), interruptSettings)
        interruptSymbol.setLabel("{} Interrupt".format(symbol))
        interruptSymbol.setDefaultValue(False)
        interruptSymbol.setDependencies(interruptEnableChange, [INTERRUPT_MODE_TEMPLATE.format(symbol)])
        interruptSymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:intc_04436;register:IFS4")

    # Interrupt Handling
    compPrefix = "PTG"
    compInstance = ptgComponent.getID().upper().replace(PTG,"") 
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    createInterruptSymbols(ptgComponent,intSymbolMap)
    updateInterruptLists(interruptList)

    intComment = ptgComponent.createCommentSymbol(INTERRUPT_COMMENT, None)
    intComment.setVisible(False)
    intComment.setLabel(WARNING_INTERRUPT_DISABLED_LABEL)
    intComment.setDependencies(interruptStatusWarnings, interruptEnableList)

    maxStepSize = int(getParameterValue(PTG, module_name, MAX_STEP_SIZE_PARAM))


    stepSequenceSettings = ptgComponent.createMenuSymbol("STEP_SEQUENCE_KEY", None)
    stepSequenceSettings.setLabel("Step Sequence Queue Settings")

    step_options = ["Step {}".format(i) for i in range(maxStepSize)]
    stepQueuePointerCombo = ptgComponent.createComboSymbol("STEP_QUEUE_POINTER", stepSequenceSettings, step_options)
    stepQueuePointerCombo.setLabel("Step Queue Pointer")
    stepQueuePointerCombo.setDefaultValue("Step 0")
    stepQueuePointerCombo.setVisible(True)
    stepQueuePointerCombo.setDependencies(showAllSteps, [STEP_SEQUENCE_QUEUE_KEY])

    ptgQPtrSymbol = ptgComponent.createHexSymbol("PTGQPTR", stepSequenceSettings)
    ptgQPtrSymbol.setDefaultValue(0x0)
    ptgQPtrSymbol.setVisible(False)
    ptgQPtrSymbol.setDependencies(updatePTGQPTRSymbol, ["STEP_QUEUE_POINTER"])
    ptgBTESymbol.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:ptg_05178;register:PTGQPTR")


    # PTG_INTERRUPT_COMMENT
    ptgIntrComment = ptgComponent.createCommentSymbol("PTG_INTERRUPT_COMMENT", None)
    ptgIntrComment.setVisible(False)
    # Set dependencies based on all COMMAND_OPTIONS
    ptgIntrComment.setDependencies(setPtgInterruptWarnings,[COMMAND_OPTIONS_KEY_TEMPLATE.format(i) for i in range(maxStepSize)] + PTGInteruptList )

# Loop to create steps dynamically
    for i in range(maxStepSize):
    # Step Menu
        stepMenu = ptgComponent.createMenuSymbol(STEP_MENU_KEY_TEMPLATE.format(i), stepSequenceSettings)
        stepMenu.setLabel("Step {}".format(i))
        stepMenu.setVisible(True)
        stepMenu.setDependencies(showAllSteps, ["StepSequenceQueue"])
        
    # Command Symbol
        cmd = ptgComponent.createComboSymbol(STEP_CMD_KEY_TEMPLATE.format(i), stepMenu, CMD_OPTIONS)
        cmd.setLabel("Select PTG Command")
        cmd.setDefaultValue(CMD_OPTIONS[0])
        cmd.setVisible(True)


    # Options Symbol
        commandOptions = ptgComponent.createComboSymbol(COMMAND_OPTIONS_KEY_TEMPLATE.format(i), stepMenu, ptgctrl_options)
        commandOptions.setLabel("Select Command Option")
        commandOptions.setDefaultValue("NOP")
        commandOptions.setDependencies(updateCommandOptions, [STEP_CMD_KEY_TEMPLATE.format(i)])
        
        # Options Value
        optionValue = ptgComponent.createHexSymbol(STEP_OPTION_VALUE_KEY_TEMPLATE.format(i), stepMenu)
        optionValue.setLabel("Selected Option Value")
        optionValue.setDefaultValue(0x0)
        optionValue.setVisible(True)
        optionValue.setReadOnly(True)
        optionValue.setDependencies(updatOptionValue, [COMMAND_OPTIONS_KEY_TEMPLATE.format(i)])



    ###### Code Generation File Handling #########

    configName = Variables.get("__CONFIGURATION_NAME")

    ptgHeaderFile = ptgComponent.createFileSymbol("PTG_HEADER", None)
    ptgHeaderFile.setSourcePath("../peripheral/ptg_05178/templates/plib_ptg.h.ftl")
    ptgHeaderFile.setOutputName("plib_" + ptgInstanceName.getValue().lower() + ".h" )
    ptgHeaderFile.setDestPath("peripheral/ptg")
    ptgHeaderFile.setProjectPath("config/" + configName + "/peripheral/ptg/")
    ptgHeaderFile.setType("HEADER")
    ptgHeaderFile.setMarkup(True)

    ptgSourceFile = ptgComponent.createFileSymbol("PTG_SOURCE", None)
    ptgSourceFile.setSourcePath("../peripheral/ptg_05178/templates/plib_ptg.c.ftl")
    ptgSourceFile.setOutputName("plib_" + ptgInstanceName.getValue().lower() + ".c")
    ptgSourceFile.setMarkup(True)
    ptgSourceFile.setDestPath("/peripheral/ptg/")
    ptgSourceFile.setProjectPath("config/" + configName + "/peripheral/ptg/")
    ptgSourceFile.setType("SOURCE")

    ptgSystemInitFile = ptgComponent.createFileSymbol("PTG_SYS_INIT", None)
    ptgSystemInitFile.setType("STRING")
    ptgSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ptgSystemInitFile.setSourcePath("../peripheral/ptg_05178/templates/system/initialization.c.ftl")
    ptgSystemInitFile.setMarkup(True)

    ptgSystemDefFile = ptgComponent.createFileSymbol("PTG_SYS_DEF", None)
    ptgSystemDefFile.setType("STRING")
    ptgSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ptgSystemDefFile.setSourcePath("../peripheral/ptg_05178/templates/system/definitions.h.ftl")
    ptgSystemDefFile.setMarkup(True)

 
    ###### Code Generation symbols  #########
    moduleName = ptgComponent.createStringSymbol("moduleName", None)
    moduleName.setDefaultValue(ptgComponent.getID().upper())
    moduleName.setVisible(False)

    moduleNameUpperCase = ptgComponent.createStringSymbol("moduleNameUpperCase", None)
    moduleNameUpperCase.setDefaultValue(ptgComponent.getID().upper())
    moduleNameUpperCase.setVisible(False)

    moduleNameLowerCase = ptgComponent.createStringSymbol("moduleNameLowerCase", None)
    moduleNameLowerCase.setDefaultValue(ptgComponent.getID().lower())
    moduleNameLowerCase.setVisible(False)
    
    maxStepSequence = ptgComponent.createIntegerSymbol("maxStepSequence", None)
    maxStepSequence.setValue(maxStepSize)
    maxStepSequence.setVisible(False)

    # Any Channel Interrupt Enabled
    isPtgInterruptEnabled = ptgComponent.createBooleanSymbol("isPtgInterruptEnabled", None)
    isPtgInterruptEnabled.setLabel("Any PTG Interrupt Enabled")
    isPtgInterruptEnabled.setDefaultValue(False)
    isPtgInterruptEnabled.setVisible(False) 
    # Create dependency array for each channel interrupts
    ptgInterruptList.extend(INTERRUPT_MODE_TEMPLATE.format(j) for j in INTERRUPT_SYMBOLS)
    isPtgInterruptEnabled.setDependencies(updateAnyInterruptEnable, ptgInterruptList)

     # String symbol for the POR (Power-On Reset) values of registers
    registers  = ["CON","BTE","HOLD","T0LIM","T1LIM","SDLIM","C0LIM","C1LIM","ADJ","L0","QPTR"] 
    reg_por_set  = create_reg_por_set_string(PTG, PTG, registers )
    regPorSet = ptgComponent.createStringSymbol("regPorSet", None)
    regPorSet.setDefaultValue(reg_por_set)
    regPorSet.setVisible(False)


def calculateDefaultCycles(clockFreq,time_ms):
    if time_ms is not None and clockFreq is not None:
        time_s = time_ms * 1e-3
        cycles = time_s * clockFreq
        return cycles 
    return 0   
