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
global ledInstanceNum
breathing_led_dependencyList = []
blinking_led_dependencyList = []

################################################################################
#### Business Logic ####
################################################################################


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def setLEDInterruptData(led_wdt_interrupt_name, status):

    Database.setSymbolValue("core", led_wdt_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", led_wdt_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", led_wdt_interrupt_name + "_INTERRUPT_HANDLER", led_wdt_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", led_wdt_interrupt_name + "_INTERRUPT_HANDLER", led_wdt_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateLEDWDT(ledInterruptType, ledMode, clk_src):
    interruptNameDir = "LED" + ledInstanceNum.getValue()
    interruptNameAgg = "LED" + ledInstanceNum.getValue() + "_GRP"

    if ledMode == "LED_BLINKING" and clk_src == "LED_CLK_SRC_48MHZ":
        if ledInterruptType == "AGGREGATE":
            setLEDInterruptData(interruptNameDir, False)
            setLEDInterruptData(interruptNameAgg, True)
        else:
            setLEDInterruptData(interruptNameAgg, False)
            setLEDInterruptData(interruptNameDir, True)
    else:
        setLEDInterruptData(interruptNameAgg, False)
        setLEDInterruptData(interruptNameDir, False)

def nvicInterruptUpdate(symbol, event):
    ledInterruptType = event["source"].getSymbolByID("LED_WDT_INTERRUPT_TYPE").getSelectedKey()
    ledMode = event["source"].getSymbolByID("LED_MODE").getSelectedKey()
    clk_src = event["source"].getSymbolByID("LED_CLK_SRC").getSelectedKey()

    nvicInterruptUpdateLEDWDT(ledInterruptType, ledMode, clk_src)

def ledBreathingModeVisibility(symbol, event):
    localComponent = symbol.getComponent()
    ledMode = localComponent.getSymbolByID("LED_MODE").getSelectedKey()
    symbol.setVisible(ledMode == "LED_BREATHING")

def ledBlinkingModeVisibility(symbol, event):
    localComponent = symbol.getComponent()
    ledMode = localComponent.getSymbolByID("LED_MODE").getSelectedKey()
    if symbol.getID() != "LED_WDT_RELOAD" and symbol.getID() != "LED_WDT_INTERRUPT_TYPE":
        symbol.setVisible(ledMode == "LED_BLINKING")
    else:
        clk_src = localComponent.getSymbolByID("LED_CLK_SRC").getSelectedKey()
        symbol.setVisible(ledMode == "LED_BLINKING" and clk_src == "LED_CLK_SRC_48MHZ")

def pwmTimeCalc(localComponent):
    global pwmTimeCalc
    clk_src = localComponent.getSymbolByID("LED_CLK_SRC").getSelectedKey()
    prescaler = localComponent.getSymbolByID("LED_CLK_PRESCALER").getValue()
    duty_cycle = localComponent.getSymbolByID("LED_DUTY_CYCLE").getValue()
    wdt_reload = localComponent.getSymbolByID("LED_WDT_RELOAD").getValue()

    clk_val = 48000000

    if clk_src == "LED_CLK_SRC_32KHZ":
        clk_val = 32768

    clk_val = float(clk_val)/(prescaler + 1)
    pwm_on_time = duty_cycle * (1.0/clk_val)
    pwm_off_time = (256-duty_cycle) * (1.0/clk_val)
    pwm_freq = 1.0/(pwm_on_time + pwm_off_time)

    if wdt_reload == 0 or clk_src != "LED_CLK_SRC_48MHZ":
        wdt_timeout = 0
    else:
        wdt_timeout = (1.0/5) * wdt_reload

    return pwm_on_time, pwm_off_time, pwm_freq, wdt_timeout

def ledTimeCalc(localComponent):
    global ledTimeCalc
    pwm_size = int(localComponent.getSymbolByID("LED_PWM_SIZE").getSelectedValue(), 16)
    min_duty_cycle = localComponent.getSymbolByID("LED_DUTY_CYCLE_MIN").getValue() >> pwm_size
    max_duty_cycle = localComponent.getSymbolByID("LED_DUTY_CYCLE_MAX").getValue() >> pwm_size
    low_delay = localComponent.getSymbolByID("LED_LOW_DELAY").getValue() + 1
    high_delay = localComponent.getSymbolByID("LED_HIGH_DELAY").getValue() + 1
    symmetry = localComponent.getSymbolByID("LED_SYMMETRY").getSelectedKey()

    ramp_up_time = 0
    ramp_down_time = 0
    total_time = 0

    pwm_cycle_time = (1.0/32768) * (256 >> pwm_size)

    pwm_duty_cycle = min_duty_cycle

    if symmetry == "LED_ASYMMETRY":
        while pwm_duty_cycle < max_duty_cycle:
            segment = (pwm_duty_cycle & (0xc0 >> pwm_size)) >> (6 - pwm_size)
            step = (localComponent.getSymbolByID("LED_UPDATE_STEPSIZE_" + str(segment)).getValue() >> pwm_size) + 1
            interval = localComponent.getSymbolByID("LED_UPDATE_INTERVAL_" + str(segment)).getValue() + 1
            pwm_duty_cycle += step
            ramp_up_time += interval * pwm_cycle_time

        pwm_duty_cycle = max_duty_cycle
        while pwm_duty_cycle > min_duty_cycle:
            segment = (pwm_duty_cycle & (0xc0 >> pwm_size)) >> (6 - pwm_size)
            segment |= 0x04
            step = (localComponent.getSymbolByID("LED_UPDATE_STEPSIZE_" + str(segment)).getValue() >> pwm_size) + 1
            interval = localComponent.getSymbolByID("LED_UPDATE_INTERVAL_" + str(segment)).getValue() + 1
            pwm_duty_cycle -= step
            ramp_down_time += interval * pwm_cycle_time

    else:
        while pwm_duty_cycle < max_duty_cycle:
            segment = (pwm_duty_cycle & (0xe0 >> pwm_size)) >> (5 - pwm_size)
            step = (localComponent.getSymbolByID("LED_UPDATE_STEPSIZE_" + str(segment)).getValue() >> pwm_size) + 1
            interval = localComponent.getSymbolByID("LED_UPDATE_INTERVAL_" + str(segment)).getValue() + 1
            pwm_duty_cycle += step
            ramp_up_time += interval * pwm_cycle_time
        ramp_down_time = ramp_up_time

    total_time = ramp_up_time + ramp_down_time + ((low_delay + high_delay) * pwm_cycle_time)

    return ramp_up_time, ramp_down_time, total_time

def ledTimeUpdate(symbol, event):
    global ledTimeCalc

    localComponent = symbol.getComponent()

    ramp_up_time_sym = localComponent.getSymbolByID("LED_RAMPUP_TIME")
    ramp_down_time_sym = localComponent.getSymbolByID("LED_RAMPDOWN_TIME")
    total_time_sym = localComponent.getSymbolByID("LED_TOTAL_TIME")
    led_mode = localComponent.getSymbolByID("LED_MODE").getSelectedKey()

    if event["id"] == "LED_MODE":
        ramp_up_time_sym.setVisible(led_mode == "LED_BREATHING")
        ramp_down_time_sym.setVisible(led_mode == "LED_BREATHING")
        total_time_sym.setVisible(led_mode == "LED_BREATHING")
    else:

        ramp_up_time, ramp_down_time, total_time = ledTimeCalc(localComponent)

        ramp_up_time_sym.setLabel("Ramp-up Time = " +  "{:.2f}".format(ramp_up_time * 1000) + " ms")
        ramp_down_time_sym.setLabel("Ramp-down Time = " + "{:.2f}".format(ramp_down_time * 1000) + " ms")
        total_time_sym.setLabel("Total Time = " + "{:.2f}".format(total_time * 1000) + " ms")

def pwmTimeUpdate(symbol, event):
    global pwmTimeCalc

    localComponent = symbol.getComponent()

    pwm_on_time_sym = localComponent.getSymbolByID("LED_PWM_ON_TIME")
    pwm_off_time_sym = localComponent.getSymbolByID("LED_PWM_OFF_TIME")
    pwm_freq_sym = localComponent.getSymbolByID("LED_PWM_FREQ")
    wdt_timeout_sym = localComponent.getSymbolByID("LED_WDT_TIMEOUT_TIME")
    led_mode = localComponent.getSymbolByID("LED_MODE").getSelectedKey()
    clk_src = localComponent.getSymbolByID("LED_CLK_SRC").getSelectedKey()

    if event["id"] == "LED_MODE":
        pwm_on_time_sym.setVisible(led_mode == "LED_BLINKING")
        pwm_off_time_sym.setVisible(led_mode == "LED_BLINKING")
        pwm_freq_sym.setVisible(led_mode == "LED_BLINKING")
        wdt_timeout_sym.setVisible(led_mode == "LED_BLINKING" and clk_src == "LED_CLK_SRC_48MHZ")
    else:
        pwm_on_time, pwm_off_time, pwm_freq, wdt_timeout = pwmTimeCalc(localComponent)

        pwm_on_time_sym.setLabel("PWM On Time = " +  "{:.2f}".format(pwm_on_time * 1000) + " ms")
        pwm_off_time_sym.setLabel("PWM Off Time = " + "{:.2f}".format(pwm_off_time * 1000) + " ms")
        pwm_freq_sym.setLabel("PWM Frequency = " + "{:.2f}".format(pwm_freq) + " Hz")
        if wdt_timeout == 0:
            wdt_timeout_sym.setLabel("WDT Disabled")
            wdt_timeout_sym.setVisible(led_mode == "LED_BLINKING" and clk_src == "LED_CLK_SRC_48MHZ")
        else:
            wdt_timeout_sym.setLabel("WDT Timeout = " + "{:.2f}".format(wdt_timeout) + " sec")
            wdt_timeout_sym.setVisible(led_mode == "LED_BLINKING" and clk_src == "LED_CLK_SRC_48MHZ")

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(ledComponent):

    global instanceNum
    global ledTimeCalc
    global pwmTimeCalc
    global ledInstanceNum

    ledInstanceName = ledComponent.createStringSymbol("LED_INSTANCE_NAME", None)
    ledInstanceName.setVisible(False)
    ledInstanceName.setDefaultValue(ledComponent.getID().upper())
    Log.writeInfoMessage("Running " + ledInstanceName.getValue())

    ledInstanceNum = ledComponent.createStringSymbol("LED_INSTANCE_NUM", None)
    ledInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(ledComponent.getID()))
    ledInstanceNum.setDefaultValue(instanceNum)

    ledCtrl_Values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"LED\"]/value-group@[name=\"LED_CFG__CTRL\"]").getChildren()
    ledPWMSize_Values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"LED\"]/value-group@[name=\"LED_CFG__PWM_SIZE\"]").getChildren()
    ledClkSrc_Values = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"LED\"]/value-group@[name=\"LED_CFG__CLK_SRC\"]").getChildren()

    ledMode = ledComponent.createKeyValueSetSymbol("LED_MODE", None)
    ledMode.setLabel("Operating Mode")
    for index in range(len(ledCtrl_Values)):
        if ledCtrl_Values[index].getAttribute("value") == "0x1" or ledCtrl_Values[index].getAttribute("value") == "0x2":
            ledMode.addKey(ledCtrl_Values[index].getAttribute("name"), ledCtrl_Values[index].getAttribute("value"), ledCtrl_Values[index].getAttribute("caption"))
    ledMode.setOutputMode("Key")
    ledMode.setDisplayMode("Description")
    breathing_led_dependencyList.append("LED_MODE")
    blinking_led_dependencyList.append("LED_MODE")

    ledClkSrc = ledComponent.createKeyValueSetSymbol("LED_CLK_SRC", ledMode)
    ledClkSrc.setLabel("Clock Source")
    for index in range(len(ledClkSrc_Values)):
        ledClkSrc.addKey(ledClkSrc_Values[index].getAttribute("name"), ledClkSrc_Values[index].getAttribute("value"), ledClkSrc_Values[index].getAttribute("caption"))
    ledClkSrc.setOutputMode("Value")
    ledClkSrc.setDisplayMode("Description")
    ledClkSrc.setVisible(False)
    ledClkSrc.setDependencies(ledBlinkingModeVisibility, ["LED_MODE"])
    blinking_led_dependencyList.append("LED_CLK_SRC")

    ledClkPrescaler = ledComponent.createIntegerSymbol("LED_CLK_PRESCALER", ledMode)
    ledClkPrescaler.setLabel("Clock Prescaler")
    ledClkPrescaler.setMin(0)
    ledClkPrescaler.setMax(4095)
    ledClkPrescaler.setDefaultValue(0)
    ledClkPrescaler.setVisible(False)
    ledClkPrescaler.setDependencies(ledBlinkingModeVisibility, ["LED_MODE"])
    blinking_led_dependencyList.append("LED_CLK_PRESCALER")

    ledDutyCycle = ledComponent.createIntegerSymbol("LED_DUTY_CYCLE", ledMode)
    ledDutyCycle.setLabel("Duty Cycle")
    ledDutyCycle.setMin(0)
    ledDutyCycle.setMax(255)
    ledDutyCycle.setDefaultValue(127)
    ledDutyCycle.setVisible(False)
    ledDutyCycle.setDependencies(ledBlinkingModeVisibility, ["LED_MODE"])
    blinking_led_dependencyList.append("LED_DUTY_CYCLE")

    ledWDTReloadVal = ledComponent.createIntegerSymbol("LED_WDT_RELOAD", ledMode)
    ledWDTReloadVal.setLabel("WDT Reload Value")
    ledWDTReloadVal.setMin(0)
    ledWDTReloadVal.setMax(255)
    ledWDTReloadVal.setDefaultValue(20)
    ledWDTReloadVal.setVisible(False)
    ledWDTReloadVal.setDependencies(ledBlinkingModeVisibility, ["LED_MODE", "LED_CLK_SRC"])
    blinking_led_dependencyList.append("LED_WDT_RELOAD")

    ## Interrupt Setup
    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "LED" + ledInstanceNum.getValue()})

    # Interrupt type selection
    ledWDTInterruptType = ledComponent.createKeyValueSetSymbol("LED_WDT_INTERRUPT_TYPE", ledMode)
    ledWDTInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        ledWDTInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        ledWDTInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    ledWDTInterruptType.setDefaultValue(0)
    ledWDTInterruptType.setDisplayMode("Description")
    ledWDTInterruptType.setOutputMode("Key")
    ledWDTInterruptType.setVisible(False)
    ledWDTInterruptType.setDependencies(ledBlinkingModeVisibility, ["LED_MODE", "LED_CLK_SRC"])

    # Trigger dependency when interrupt type changes
    ledWDTNVICUpdate = ledComponent.createBooleanSymbol("LED_UPDATE_NVIC_INTERRUPT", None)
    ledWDTNVICUpdate.setVisible(False)
    ledWDTNVICUpdate.setDependencies(nvicInterruptUpdate, ["LED_MODE", "LED_WDT_INTERRUPT_TYPE", "LED_CLK_SRC"])

    ledPWMSize = ledComponent.createKeyValueSetSymbol("LED_PWM_SIZE", ledMode)
    ledPWMSize.setLabel("PWM Size")
    for index in range(len(ledPWMSize_Values)):
        ledPWMSize.addKey(ledPWMSize_Values[index].getAttribute("name"), ledPWMSize_Values[index].getAttribute("value"), ledPWMSize_Values[index].getAttribute("caption"))
    ledPWMSize.setOutputMode("Value")
    ledPWMSize.setDisplayMode("Description")
    ledPWMSize.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledPWMSize.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_PWM_SIZE")

    ledSymmetry = ledComponent.createKeyValueSetSymbol("LED_SYMMETRY", ledMode)
    ledSymmetry.setLabel("Rising and Falling Ramp Symmetry")
    ledSymmetry.addKey("LED_SYMMETRY", "0", "Symmetrical")
    ledSymmetry.addKey("LED_ASYMMETRY", "1", "Asymmetrical")
    ledSymmetry.setOutputMode("Value")
    ledSymmetry.setDisplayMode("Description")
    ledSymmetry.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledSymmetry.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_SYMMETRY")

    ledDutyCycleMin = ledComponent.createIntegerSymbol("LED_DUTY_CYCLE_MIN", ledMode)
    ledDutyCycleMin.setLabel("LED Duty Cycle Min")
    ledDutyCycleMin.setMin(0)
    ledDutyCycleMin.setMax(255)
    ledDutyCycleMin.setDefaultValue(0)
    ledDutyCycleMin.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledDutyCycleMin.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_DUTY_CYCLE_MIN")

    ledDutyCycleMax = ledComponent.createIntegerSymbol("LED_DUTY_CYCLE_MAX", ledMode)
    ledDutyCycleMax.setLabel("LED Duty Cycle Max")
    ledDutyCycleMax.setMin(0)
    ledDutyCycleMax.setMax(255)
    ledDutyCycleMax.setDefaultValue(255)
    ledDutyCycleMax.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledDutyCycleMax.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_DUTY_CYCLE_MAX")

    ledHighDelay = ledComponent.createIntegerSymbol("LED_HIGH_DELAY", ledMode)
    ledHighDelay.setLabel("High Delay (PWM cycles to wait when duty cycle reaches MAX)")
    ledHighDelay.setMin(0)
    ledHighDelay.setMax(4095)
    ledHighDelay.setDefaultValue(0)
    ledHighDelay.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledHighDelay.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_HIGH_DELAY")

    ledLowDelay = ledComponent.createIntegerSymbol("LED_LOW_DELAY", ledMode)
    ledLowDelay.setLabel("Low Delay (PWM cycles to wait when duty cycle reaches MIN)")
    ledLowDelay.setMin(0)
    ledLowDelay.setMax(4095)
    ledLowDelay.setDefaultValue(0)
    ledLowDelay.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledLowDelay.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
    breathing_led_dependencyList.append("LED_LOW_DELAY")

    ledUpdateStepSize = ledComponent.createCommentSymbol("LED_UPDATE_STEPSIZE", ledMode)
    ledUpdateStepSize.setLabel("Duty cycle update step size")
    ledUpdateStepSize.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledUpdateStepSize.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])

    for x in range(8):
        ledSegmentUpdateStepSize = ledComponent.createIntegerSymbol("LED_UPDATE_STEPSIZE_" + str(x) , ledUpdateStepSize)
        ledSegmentUpdateStepSize.setLabel("Segment " + str(x) + " Update Step Size")
        ledSegmentUpdateStepSize.setMin(0)
        ledSegmentUpdateStepSize.setMax(15)
        ledSegmentUpdateStepSize.setDefaultValue(0)
        ledSegmentUpdateStepSize.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
        ledSegmentUpdateStepSize.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
        breathing_led_dependencyList.append("LED_UPDATE_STEPSIZE_" + str(x))

    ledUpdateInterval = ledComponent.createCommentSymbol("LED_UPDATE_INTERVAL", ledMode)
    ledUpdateInterval.setLabel("Duty cycle update interval in PWM periods")
    ledUpdateInterval.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
    ledUpdateInterval.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])

    for x in range(8):
        ledSegmentUpdateInterval = ledComponent.createIntegerSymbol("LED_UPDATE_INTERVAL_" + str(x) , ledUpdateInterval)
        ledSegmentUpdateInterval.setLabel("Segment " + str(x) + " Update Interval")
        ledSegmentUpdateInterval.setMin(0)
        ledSegmentUpdateInterval.setMax(15)
        ledSegmentUpdateInterval.setDefaultValue(0)
        ledSegmentUpdateInterval.setVisible(ledMode.getSelectedKey() == "LED_BREATHING")
        ledSegmentUpdateInterval.setDependencies(ledBreathingModeVisibility, ["LED_MODE"])
        breathing_led_dependencyList.append("LED_UPDATE_INTERVAL_" + str(x))

    ramp_up_time, ramp_down_time, total_time = ledTimeCalc(ledInstanceName.getComponent())

    ledRampUpTimeComment = ledComponent.createCommentSymbol("LED_RAMPUP_TIME", ledMode)
    ledRampUpTimeComment.setLabel("Ramp-up Time = " +  "{:.2f}".format(ramp_up_time * 1000) + " ms")

    ledRampDownTimeComment = ledComponent.createCommentSymbol("LED_RAMPDOWN_TIME", ledMode)
    ledRampDownTimeComment.setLabel("Ramp-down Time = " + "{:.2f}".format(ramp_down_time * 1000) + " ms")

    ledTotalTimeComment = ledComponent.createCommentSymbol("LED_TOTAL_TIME", ledMode)
    ledTotalTimeComment.setLabel("Total Time = " + "{:.2f}".format(total_time * 1000) + " ms")

    #Common callback for ramp_down_time, ramp_up_time and total_time update
    ledTotalTimeComment.setDependencies(ledTimeUpdate, breathing_led_dependencyList)

    pwm_on_time, pwm_off_time, pwm_freq, wdt_timeout = pwmTimeCalc(ledInstanceName.getComponent())

    ledPwmOnTimeComment = ledComponent.createCommentSymbol("LED_PWM_ON_TIME", ledMode)
    ledPwmOnTimeComment.setLabel("PWM On Time = " +  "{:.2f}".format(pwm_on_time * 1000) + " ms")
    ledPwmOnTimeComment.setVisible(False)

    ledPwmOffTimeComment = ledComponent.createCommentSymbol("LED_PWM_OFF_TIME", ledMode)
    ledPwmOffTimeComment.setLabel("PWM Off Time = " + "{:.2f}".format(pwm_off_time * 1000) + " ms")
    ledPwmOffTimeComment.setVisible(False)

    ledPwmFreqComment = ledComponent.createCommentSymbol("LED_PWM_FREQ", ledMode)
    ledPwmFreqComment.setLabel("PWM Frequency = " + "{:.2f}".format(pwm_freq) + " Hz")
    ledPwmFreqComment.setVisible(False)

    ledWDTTimeoutTimeComment = ledComponent.createCommentSymbol("LED_WDT_TIMEOUT_TIME", ledMode)
    ledWDTTimeoutTimeComment.setLabel("WDT Timeout = " + "{:.2f}".format(wdt_timeout) + " sec")
    ledWDTTimeoutTimeComment.setVisible(False)

    #Common callback for pwm_on_time, pwm_off_time, pwm_freq and wdt_timeout update
    ledWDTTimeoutTimeComment.setDependencies(pwmTimeUpdate, blinking_led_dependencyList)


    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    ledHeaderFile = ledComponent.createFileSymbol("LED_COMMON_HEADER", None)
    ledHeaderFile.setSourcePath("../peripheral/led_111/templates/plib_led_common.h")
    ledHeaderFile.setOutputName("plib_led_common.h")
    ledHeaderFile.setDestPath("peripheral/led/")
    ledHeaderFile.setProjectPath("config/" + configName + "/peripheral/led/")
    ledHeaderFile.setType("HEADER")
    ledHeaderFile.setMarkup(False)
    ledHeaderFile.setOverwrite(True)

    # Instance Header File
    ledCmnHeaderFile = ledComponent.createFileSymbol("LED_HEADER1", None)
    ledCmnHeaderFile.setSourcePath("../peripheral/led_111/templates/plib_led.h.ftl")
    ledCmnHeaderFile.setOutputName("plib_" + ledInstanceName.getValue().lower() + ".h")
    ledCmnHeaderFile.setDestPath("/peripheral/led/")
    ledCmnHeaderFile.setProjectPath("config/" + configName + "/peripheral/led/")
    ledCmnHeaderFile.setType("HEADER")
    ledCmnHeaderFile.setMarkup(True)
    ledCmnHeaderFile.setOverwrite(True)

    # Instance Source File
    ledSourceFile = ledComponent.createFileSymbol("LED_SOURCE", None)
    ledSourceFile.setSourcePath("../peripheral/led_111/templates/plib_led.c.ftl")
    ledSourceFile.setOutputName("plib_" + ledInstanceName.getValue().lower() + ".c")
    ledSourceFile.setDestPath("/peripheral/led/")
    ledSourceFile.setProjectPath("config/" + configName + "/peripheral/led/")
    ledSourceFile.setType("SOURCE")
    ledSourceFile.setMarkup(True)
    ledSourceFile.setOverwrite(True)

    ledSystemInitFile = ledComponent.createFileSymbol("LEDSYS_INT", None)
    ledSystemInitFile.setType("STRING")
    ledSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    ledSystemInitFile.setSourcePath("../peripheral/led_111/templates/system/initialization.c.ftl")
    ledSystemInitFile.setMarkup(True)

    ledSystemDefFile = ledComponent.createFileSymbol("LED_SYS_DEF", None)
    ledSystemDefFile.setType("STRING")
    ledSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    ledSystemDefFile.setSourcePath("../peripheral/led_111/templates/system/definitions.h.ftl")
    ledSystemDefFile.setMarkup(True)