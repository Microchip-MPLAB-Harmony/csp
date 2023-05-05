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


################################################################################
#### Business Logic ####
################################################################################


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################


def updatePWMFrequency(symbol):
    clockFreq = 0
    localComponent = symbol.getComponent()

    selectedClk = localComponent.getSymbolByID("PWM_CLOCK_SELECT").getSelectedKey()
    preDivisor = localComponent.getSymbolValue("PWM_CLOCK_DIVIDER")
    onTime = localComponent.getSymbolValue("PWM_ON_TIME_COUNTER")
    offTime = localComponent.getSymbolValue("PWM_OFF_TIME_COUNTER")

    preDivisor = preDivisor + 1

    if selectedClk == "CLOCK_LOW":
        clockFreq = 100000.0/preDivisor
    else:
        clockFreq = 48000000.0/preDivisor

    pwmFrequency = clockFreq/((onTime + 1) + (offTime + 1))

    return pwmFrequency

def updateDutyCycle(symbol):
    localComponent = symbol.getComponent()
    onTime = localComponent.getSymbolValue("PWM_ON_TIME_COUNTER")
    offTime = localComponent.getSymbolValue("PWM_OFF_TIME_COUNTER")

    dutyCycle = (onTime + 1.0) / ((onTime + 1.0) + (offTime + 1.0))
    dutyCycle *= 100.0

    return dutyCycle

def updatePWMOnTimeOffTime(selectedClk, preDivisor, timeCntrVal):

    preDivisor = preDivisor + 1
    timeCntrVal = timeCntrVal + 1
    
    if selectedClk == "CLOCK_LOW":
        clockFreq = 100000.0/preDivisor
    else:
        clockFreq = 48000000.0/preDivisor
    
    onOffTimeMs = float(timeCntrVal)/clockFreq
    onOffTimeMs = onOffTimeMs * 1000.0
    
    return onOffTimeMs

def updateDutyCycleCallback(symbol, event):

    dutyCycle = updateDutyCycle(symbol)

    symbol.setLabel("Duty Cycle is " + "{:.2f}".format(dutyCycle) + "%")

def updatePWMFrequencyCallback(symbol, event):

    pwmFrequency = updatePWMFrequency(symbol)

    symbol.setLabel("PWM Frequency is " + "{:.2f}".format(pwmFrequency) + " Hz")

def updatePWMOnTimeOffTimeCallback(symbol, event):
    localComponent = symbol.getComponent()
    
    if symbol.getID() == "PWM_ON_TIME_MS":
        timeCntrVal = localComponent.getSymbolValue("PWM_ON_TIME_COUNTER")
    else:
        timeCntrVal = localComponent.getSymbolValue("PWM_OFF_TIME_COUNTER")
        
    selectedClk = localComponent.getSymbolByID("PWM_CLOCK_SELECT").getSelectedKey()
    preDivisor = localComponent.getSymbolValue("PWM_CLOCK_DIVIDER")
    
    if symbol.getID() == "PWM_ON_TIME_MS":
        symbol.setLabel("PWM On-time is " + "{:.4f}".format(updatePWMOnTimeOffTime(selectedClk, preDivisor, timeCntrVal)) + " msec")
    else:
        symbol.setLabel("PWM Off-time is " + "{:.4f}".format(updatePWMOnTimeOffTime(selectedClk, preDivisor, timeCntrVal)) + " msec")
    
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(pwmComponent):

    global instanceNum

    pwmInstanceName = pwmComponent.createStringSymbol("PWM_INSTANCE_NAME", None)
    pwmInstanceName.setVisible(False)
    pwmInstanceName.setDefaultValue(pwmComponent.getID().upper())
    Log.writeInfoMessage("Running " + pwmInstanceName.getValue())

    pwmInstanceNum = pwmComponent.createStringSymbol("PWM_INSTANCE_NUM", None)
    pwmInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(pwmComponent.getID()))
    pwmInstanceNum.setDefaultValue(instanceNum)

    pwmClkSelect = pwmComponent.createKeyValueSetSymbol("PWM_CLOCK_SELECT", None)
    pwmClkSelect.setLabel("PWM Clock Select")
    pwmClkSelect.addKey("CLOCK_LOW", "1", "Clock Low (100 KHz)")
    pwmClkSelect.addKey("CLOCK_HIGH", "0", "Clock High (48 MHz)")
    pwmClkSelect.setDefaultValue(1)
    pwmClkSelect.setDisplayMode("Description")
    pwmClkSelect.setOutputMode("Value")

    pwmClkDivider = pwmComponent.createIntegerSymbol("PWM_CLOCK_DIVIDER", None)
    pwmClkDivider.setLabel("PWM Clock Divider")
    pwmClkDivider.setMin(0)
    pwmClkDivider.setMax(15)
    pwmClkDivider.setDefaultValue(0)

    pwmOnTimeCounter = pwmComponent.createIntegerSymbol("PWM_ON_TIME_COUNTER", None)
    pwmOnTimeCounter.setLabel("PWM On Time Counter")
    pwmOnTimeCounter.setDefaultValue(100)

    pwmOffTimeCounter = pwmComponent.createIntegerSymbol("PWM_OFF_TIME_COUNTER", None)
    pwmOffTimeCounter.setLabel("PWM Off Time Counter")
    pwmOffTimeCounter.setDefaultValue(100)

    pwmOutputInvert = pwmComponent.createBooleanSymbol("PWM_OUTPUT_INVERT", None)
    pwmOutputInvert.setLabel("PWM Output Invert?")
    pwmOutputInvert.setDefaultValue(False)

    pwmFrequency = pwmComponent.createCommentSymbol("PWM_FREQUENCY", None)
    pwmFrequency.setDependencies(updatePWMFrequencyCallback, ["PWM_ON_TIME_COUNTER", "PWM_OFF_TIME_COUNTER", "PWM_CLOCK_DIVIDER", "PWM_CLOCK_SELECT"])
    pwmFrequency.setLabel("PWM Frequency is " + "{:.2f}".format(updatePWMFrequency(pwmFrequency)) + " Hz")

    pwmDutyCycle = pwmComponent.createCommentSymbol("PWM_DUTY_CYCLE", None)
    pwmDutyCycle.setDependencies(updateDutyCycleCallback, ["PWM_ON_TIME_COUNTER", "PWM_OFF_TIME_COUNTER"])
    pwmDutyCycle.setLabel("Duty Cycle is " + "{:.2f}".format(updateDutyCycle(pwmDutyCycle)) + "%")
    
    pwmOnTimeMs = pwmComponent.createCommentSymbol("PWM_ON_TIME_MS", None)
    pwmOnTimeMs.setDependencies(updatePWMOnTimeOffTimeCallback, ["PWM_ON_TIME_COUNTER", "PWM_CLOCK_SELECT", "PWM_CLOCK_DIVIDER"])
    pwmOnTimeMs.setLabel("PWM On-time is " + "{:.4f}".format(updatePWMOnTimeOffTime(pwmClkSelect.getSelectedKey(), pwmClkDivider.getValue(), pwmOnTimeCounter.getValue())) + " msec")
    
    pwmOffTimeMs = pwmComponent.createCommentSymbol("PWM_OFF_TIME_MS", None)
    pwmOffTimeMs.setDependencies(updatePWMOnTimeOffTimeCallback, ["PWM_OFF_TIME_COUNTER", "PWM_CLOCK_SELECT", "PWM_CLOCK_DIVIDER"])
    pwmOffTimeMs.setLabel("PWM Off-time is " + "{:.4f}".format(updatePWMOnTimeOffTime(pwmClkSelect.getSelectedKey(), pwmClkDivider.getValue(), pwmOffTimeCounter.getValue())) + " msec")

    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    pwmHeaderFile = pwmComponent.createFileSymbol("PWM_COMMON_HEADER", None)
    pwmHeaderFile.setSourcePath("../peripheral/pwm_54/templates/plib_pwm_common.h")
    pwmHeaderFile.setOutputName("plib_pwm_common.h")
    pwmHeaderFile.setDestPath("peripheral/pwm/")
    pwmHeaderFile.setProjectPath("config/" + configName + "/peripheral/pwm/")
    pwmHeaderFile.setType("HEADER")
    pwmHeaderFile.setMarkup(False)
    pwmHeaderFile.setOverwrite(True)

    # Instance Header File
    pwmCmnHeaderFile = pwmComponent.createFileSymbol("PWM_HEADER1", None)
    pwmCmnHeaderFile.setSourcePath("../peripheral/pwm_54/templates/plib_pwm.h.ftl")
    pwmCmnHeaderFile.setOutputName("plib_" + pwmInstanceName.getValue().lower() + ".h")
    pwmCmnHeaderFile.setDestPath("/peripheral/pwm/")
    pwmCmnHeaderFile.setProjectPath("config/" + configName + "/peripheral/pwm/")
    pwmCmnHeaderFile.setType("HEADER")
    pwmCmnHeaderFile.setMarkup(True)
    pwmCmnHeaderFile.setOverwrite(True)

    # Instance Source File
    pwmSourceFile = pwmComponent.createFileSymbol("PWM_SOURCE", None)
    pwmSourceFile.setSourcePath("../peripheral/pwm_54/templates/plib_pwm.c.ftl")
    pwmSourceFile.setOutputName("plib_" + pwmInstanceName.getValue().lower() + ".c")
    pwmSourceFile.setDestPath("/peripheral/pwm/")
    pwmSourceFile.setProjectPath("config/" + configName + "/peripheral/pwm/")
    pwmSourceFile.setType("SOURCE")
    pwmSourceFile.setMarkup(True)
    pwmSourceFile.setOverwrite(True)

    pwmSystemInitFile = pwmComponent.createFileSymbol("PWM_SYS_INT", None)
    pwmSystemInitFile.setType("STRING")
    pwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pwmSystemInitFile.setSourcePath("../peripheral/pwm_54/templates/system/initialization.c.ftl")
    pwmSystemInitFile.setMarkup(True)

    pwmSystemDefFile = pwmComponent.createFileSymbol("PWM_SYS_DEF", None)
    pwmSystemDefFile.setType("STRING")
    pwmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pwmSystemDefFile.setSourcePath("../peripheral/pwm_54/templates/system/definitions.h.ftl")
    pwmSystemDefFile.setMarkup(True)
