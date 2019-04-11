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

###################################################################################################
########################### Helpers   #################################
###################################################################################################
def setSymbolValueFromATDF(symbol, moduleName, valueGroupName):
    atdf_path = "/avr-tools-device-file/modules/module@[name=\"" + moduleName + "\"]/value-group@[name=\"" +\
                                                                                        valueGroupName + "\"]"
    node = ATDF.getNode(atdf_path)
    value = node.getChildren()
    for index in range(len(value)):
        symbol.addKey(value[index].getAttribute("name"),
                      value[index].getAttribute("value"),
                      value[index].getAttribute("caption"))

###################################################################################################
########################### Callback functions for dependencies   #################################
###################################################################################################
def enableSymbol(symbol, event):
    symbol.setReadOnly(not event["value"])

def UpdateClockABFrequency(symbol, event):
    clockSource = symbol.getID().split("_FREQUENCY")[0]
    enable = event["source"].getSymbolValue(clockSource + "_EN")
    pres = pow(2, int(event["source"].getSymbolByID(clockSource + "_PRES").getSelectedValue(), 16))
    div = event["source"].getSymbolValue(clockSource + "_DIV")
    freq = 0
    if enable is True:
        freq = (Database.getSymbolValue("core", pwmInstanceName.getValue() + "_CLOCK_FREQUENCY") / pres) / div
    symbol.setValue(freq, 0)

def UpdateChannelFrequency(symbol, event):
    channel = symbol.getID().split("_FREQUENCY")[0]
    frequency = 0
    enable = event["source"].getSymbolValue(channel + "_EN")
    if enable is True:
        prescalerKey = event["source"].getSymbolByID(channel + "_PRES").getSelectedKey()
        if "MCK" in prescalerKey:
            frequency = Database.getSymbolValue("core", pwmInstanceName.getValue() + "_CLOCK_FREQUENCY")
            frequency /= pow(2, int(event["source"].getSymbolByID(channel + "_PRES").getSelectedValue(), 16))
        else:
            frequency = event["source"].getSymbolValue(prescalerKey + "_FREQUENCY")
    symbol.setValue(frequency, 0)

def UpdateChannelPeriod(symbol, event):
    channel = symbol.getID().split("_PERIOD_MS")[0]
    pwmFreq = 0
    enable = event["source"].getSymbolValue(channel + "_EN")
    sourceFreq = event["source"].getSymbolValue(channel + "_FREQUENCY")
    if enable is True and sourceFreq != 0:
        periodCount = event["source"].getSymbolValue(channel + "_CPRD")
        alignMult = 1 if event["source"].getSymbolByID(channel + "_CALG").getSelectedKey() == "LEFT_ALIGNED" else 2
        pwmFreq = 1.0 /((alignMult * periodCount) / float(sourceFreq))
    symbol.setLabel("**** PWM Frequency is "+ str(pwmFreq) + " Hz ****")

def UpdatePWMClockEnable(symbol, event):
    clock_enable = False
    for channel in range(4):
        if event["source"].getSymbolValue("CH"+ str(channel)+"_EN") is True:
            clock_enable = True
            break
    Database.setSymbolValue("core", pwmInstanceName.getValue()+"_CLOCK_ENABLE", clock_enable, 2)

def UpdatePWMInterruptEnable(symbol, event):
    interruptEnable = False
    for channel in range(4):
        if event["source"].getSymbolValue("CH"+ str(channel)+"_IER_CHID") is True:
            interruptEnable = True
            break
    handlerSuffix = "_InterruptHandler" if interruptEnable is True else "_Handler"
    Database.setSymbolValue("core", pwmInstanceName.getValue() + "_INTERRUPT_ENABLE", interruptEnable, 0)
    Database.setSymbolValue("core", pwmInstanceName.getValue() + "_INTERRUPT_HANDLER",
                                            pwmInstanceName.getValue() + handlerSuffix, 0)
    Database.setSymbolValue("core", pwmInstanceName.getValue() + "_INTERRUPT_HANDLER_LOCK", interruptEnable, 0)


###################################################################################################
########################### Component   #################################
###################################################################################################
def instantiateComponent(pwmComponent):
    global pwmInstanceName
    pwmInstanceName = pwmComponent.createStringSymbol("PWM_INSTANCE_NAME", None)
    pwmInstanceName.setVisible(False)
    pwmInstanceName.setDefaultValue(pwmComponent.getID().upper())
    Log.writeInfoMessage("Running " + pwmInstanceName.getValue())

    #Clock A and B configurations
    clockList = ["A", "B"]
    for clock in clockList:

        # Clock menu
        pwmClockMenu = pwmComponent.createMenuSymbol("CLK" + clock + "_MENU", None)
        pwmClockMenu.setLabel("Clock " + clock + " Configurations")

        #clock enable
        pwmClockAEnable = pwmComponent.createBooleanSymbol("CLK" + clock + "_EN", pwmClockMenu)
        pwmClockAEnable.setLabel("Enable Clock ")
        pwmClockAEnable.setDefaultValue(False)

        #clock Prescaler
        pwmClockAPrescaler = pwmComponent.createKeyValueSetSymbol("CLK" + clock + "_PRES", pwmClockMenu)
        pwmClockAPrescaler.setLabel("Prescaler")
        setSymbolValueFromATDF(pwmClockAPrescaler, "PWM", "PWM_MR__PRE" + clock )
        pwmClockAPrescaler.setDisplayMode("Description")
        pwmClockAPrescaler.setOutputMode("Key")
        pwmClockAPrescaler.setReadOnly(True)
        pwmClockAPrescaler.setDependencies(enableSymbol, ["CLK" + clock + "_EN"])

        #clock Divider
        pwmClockADivider = pwmComponent.createIntegerSymbol("CLK" + clock + "_DIV", pwmClockMenu)
        pwmClockADivider.setLabel("Divider")
        pwmClockADivider.setMin(1)
        pwmClockADivider.setMax(255)
        pwmClockADivider.setReadOnly(True)
        pwmClockADivider.setDependencies(enableSymbol, ["CLK" + clock + "_EN"])

        #clock Frequency
        pwmClockAFrequency = pwmComponent.createIntegerSymbol("CLK" + clock + "_FREQUENCY", pwmClockMenu)
        pwmClockAFrequency.setLabel("Frequency")
        pwmClockAFrequency.setReadOnly(True)
        pwmClockAFrequency.setDefaultValue(0)
        pwmClockAFrequency.setDependencies(UpdateClockABFrequency, ["CLK" + clock + "_EN",
                                                                    "CLK" + clock + "_PRES",
                                                                    "CLK" + clock + "_DIV",
                                                                    "core." + pwmInstanceName.getValue() + "_CLOCK_FREQUENCY"])


    #Channel configurations
    for channel in range(4):
        #Channel menu
        pwmChannelMenu = pwmComponent.createMenuSymbol("CHANNEL " + str(channel) + "_MENU", None)
        pwmChannelMenu.setLabel("Channel " + str(channel) + " Configurations")

        #Channel enable
        pwmChannelEnable = pwmComponent.createBooleanSymbol("CH" + str(channel) + "_EN", pwmChannelMenu)
        pwmChannelEnable.setLabel("Enable")
        pwmChannelEnable.setDefaultValue(False)

        #Channel prescaler
        pwmChannelPrescaler = pwmComponent.createKeyValueSetSymbol("CH" + str(channel) + "_PRES", pwmChannelMenu)
        pwmChannelPrescaler.setLabel("Prescaler")
        setSymbolValueFromATDF(pwmChannelPrescaler, "PWM", "PWM_CMR0__CPRE")
        pwmChannelPrescaler.setDisplayMode("Description")
        pwmChannelPrescaler.setOutputMode("Key")
        pwmChannelPrescaler.setReadOnly(True)
        pwmChannelPrescaler.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel frequency
        pwmChannelFrequency = pwmComponent.createIntegerSymbol("CH" + str(channel) + "_FREQUENCY", pwmChannelMenu)
        pwmChannelFrequency.setLabel("Frequency")
        pwmChannelFrequency.setReadOnly(True)
        pwmChannelFrequency.setDefaultValue(0)
        pwmChannelFrequency.setDependencies(UpdateChannelFrequency, ["CH" + str(channel) + "_EN",
                                                                     "CH" + str(channel) + "_PRES",
                                                                     "CLKA_FREQUENCY",
                                                                     "CLKB_FREQUENCY",
                                                                     "core." + pwmInstanceName.getValue() + "_CLOCK_FREQUENCY"])

        #Channel Alignment
        pwmChannelAlignment = pwmComponent.createKeyValueSetSymbol("CH" + str(channel) + "_CALG", pwmChannelMenu)
        pwmChannelAlignment.setLabel("Alignment")
        setSymbolValueFromATDF(pwmChannelAlignment, "PWM", "PWM_CMR0__CALG")
        pwmChannelAlignment.setDisplayMode("Description")
        pwmChannelAlignment.setOutputMode("Key")
        pwmChannelAlignment.setReadOnly(True)
        pwmChannelAlignment.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel Polarity
        pwmChannelPolarity = pwmComponent.createKeyValueSetSymbol("CH" + str(channel) + "_CPOL", pwmChannelMenu)
        pwmChannelPolarity.setLabel("Polarity")
        setSymbolValueFromATDF(pwmChannelPolarity, "PWM", "PWM_CMR0__CPOL")
        pwmChannelPolarity.setDisplayMode("Description")
        pwmChannelPolarity.setOutputMode("Key")
        pwmChannelPolarity.setReadOnly(True)
        pwmChannelPolarity.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel Interrupt
        pwmChannelInterrupt = pwmComponent.createBooleanSymbol("CH" + str(channel) + "_IER_CHID", pwmChannelMenu)
        pwmChannelInterrupt.setLabel("Interrupt Enable")
        pwmChannelInterrupt.setDefaultValue(False)
        pwmChannelInterrupt.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel Period
        pwmChannelPeriodCount = pwmComponent.createIntegerSymbol("CH" + str(channel) +"_CPRD", pwmChannelMenu)
        pwmChannelPeriodCount.setLabel("Period Count")
        pwmChannelPeriodCount.setMin(1)
        pwmChannelPeriodCount.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel Duty
        pwmChannelDutyCount = pwmComponent.createIntegerSymbol("CH" + str(channel) +"_CDTY", pwmChannelMenu)
        pwmChannelDutyCount.setLabel("Duty Cycle Count")
        pwmChannelDutyCount.setMin(1)
        pwmChannelDutyCount.setDependencies(enableSymbol, ["CH" + str(channel) + "_EN"])

        #Channel period comment
        pwmChannelPeriodMs = pwmComponent.createCommentSymbol("CH" + str(channel) + "_PERIOD_MS", pwmChannelMenu)
        pwmChannelPeriodMs.setLabel("**** PWM Frequency is 0 Hz ****")
        pwmChannelPeriodMs.setDependencies(UpdateChannelPeriod, ["CH" + str(channel) + "_EN",
                                                                 "CH" + str(channel) + "_FREQUENCY",
                                                                 "CH" + str(channel) + "_CALG",
                                                                 "CH" + str(channel) + "_CPRD"])

    # Clock Dynamic settings
    pwmClockEnable = pwmComponent.createBooleanSymbol("PWM_CLOCK_ENABLE", None)
    pwmClockEnable.setDependencies(UpdatePWMClockEnable, ["CH0_EN", "CH1_EN", "CH2_EN", "CH3_EN"])
    pwmClockEnable.setVisible(False)
    pwmClockEnable.setDefaultValue(False)

    #interrupt Dynamic settings
    pwmInterruptEnable = pwmComponent.createBooleanSymbol("PWM_INTERRUPT_ENABLE", None)
    pwmInterruptEnable.setDependencies(UpdatePWMInterruptEnable, ["CH0_IER_CHID", "CH1_IER_CHID", "CH2_IER_CHID", "CH3_IER_CHID"])
    pwmInterruptEnable.setVisible(False)
    pwmInterruptEnable.setDefaultValue(False)

###################################################################################################
########################### Code Generation   #################################
###################################################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    pwm = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"PWM\"]")
    pwmID = pwm.getAttribute("id")

    pwmHeaderFile = pwmComponent.createFileSymbol("PWM_HEADER", None)
    pwmHeaderFile.setSourcePath("../peripheral/pwm_6044/templates/plib_pwm.h.ftl")
    pwmHeaderFile.setOutputName("plib_"+pwmInstanceName.getValue().lower()+ ".h")
    pwmHeaderFile.setDestPath("/peripheral/pwm/")
    pwmHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmHeaderFile.setType("HEADER")
    pwmHeaderFile.setOverwrite(True)
    pwmHeaderFile.setMarkup(True)

    pwmSource1File = pwmComponent.createFileSymbol("PWM_SOURCE", None)
    pwmSource1File.setSourcePath("../peripheral/pwm_6044/templates/plib_pwm.c.ftl")
    pwmSource1File.setOutputName("plib_"+pwmInstanceName.getValue().lower()+".c")
    pwmSource1File.setDestPath("/peripheral/pwm/")
    pwmSource1File.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmSource1File.setType("SOURCE")
    pwmSource1File.setOverwrite(True)
    pwmSource1File.setMarkup(True)

    pwmGlobalHeaderFile = pwmComponent.createFileSymbol("PWM_COMMON_HEADER", None)
    pwmGlobalHeaderFile.setSourcePath("../peripheral/pwm_6044/templates/plib_pwm_common.h")
    pwmGlobalHeaderFile.setOutputName("plib_pwm_common.h")
    pwmGlobalHeaderFile.setDestPath("/peripheral/pwm/")
    pwmGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/pwm/")
    pwmGlobalHeaderFile.setType("HEADER")
    pwmGlobalHeaderFile.setMarkup(False)

    pwmSystemInitFile = pwmComponent.createFileSymbol("PWM_INIT", None)
    pwmSystemInitFile.setType("STRING")
    pwmSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    pwmSystemInitFile.setSourcePath("../peripheral/pwm_6044/templates/system/initialization.c.ftl")
    pwmSystemInitFile.setMarkup(True)

    pwmSystemDefinitionFile = pwmComponent.createFileSymbol("PWM_DEF", None)
    pwmSystemDefinitionFile.setType("STRING")
    pwmSystemDefinitionFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    pwmSystemDefinitionFile.setSourcePath("../peripheral/pwm_6044/templates/system/definitions.h.ftl")
    pwmSystemDefinitionFile.setMarkup(True)







