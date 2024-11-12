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
import re

global InterruptVector
InterruptVector = []
global InterruptHandler
InterruptHandler = []
global InterruptHandlerLock
InterruptHandlerLock = []
global InterruptVectorUpdate
InterruptVectorUpdate = []
global tccInstanceName
global intPrev
intPrev =  0
global numOfChannels
global tccSym_TimerUnit
global tccSym_Timer_TIME_MS
global sysTimeComponentId
global tccSym_SYS_TIME_CONNECTED
global sysTimePlibMode

global TCCfilesArray
global InterruptVectorSecurity
TCCfilesArray = []

global evsys_generatorsNamesList
global evsys_usersNamesList
evsys_generatorsNamesList = []
evsys_usersNamesList = []

global gclk_name
gclk_name = ""


def tccEvsysGeneratorNamesPopulate(instanceName):
    global evsys_generatorsNamesList

    generatorNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/generators")
    generatorValues = generatorNode.getChildren()
    for id in range(0, len(generatorNode.getChildren())):
        if generatorValues[id].getAttribute("module-instance") == instanceName:
            evsys_generatorsNamesList.append(generatorValues[id].getAttribute("name"))

def tccEvsysUserNamesPopulate(instanceName):
    global evsys_usersNamesList

    usersNode = ATDF.getNode("/avr-tools-device-file/devices/device/events/users")
    usersValues = usersNode.getChildren()
    for id in range(0, len(usersNode.getChildren())):
        if usersValues[id].getAttribute("module-instance") == instanceName:
            evsys_usersNamesList.append(usersValues[id].getAttribute("name"))

def tccEvsysGenNameGet(genNameMatchList):
    global evsys_generatorsNamesList

    for genName in evsys_generatorsNamesList:
        if all ( x in genName for x in genNameMatchList):
            return genName

def tccEvsysUserNameGet(usrNameMatchList):
    global evsys_usersNamesList

    for userName in evsys_usersNamesList:
        if all ( x in userName for x in usrNameMatchList):
            return userName


def getValueGroupNode__TCC(module_name, register_group, register_name, bitfield_name , mode = None):
    bitfield_node_path = ""
    value_group_node = None

    if mode != None:
        bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[modes=\"{2}\",name=\"{3}\"]/bitfield@[name=\"{4}\"]".format(module_name, register_group, mode, register_name, bitfield_name)
    else:
         bitfield_node_path = "/avr-tools-device-file/modules/module@[name=\"{0}\"]/register-group@[name=\"{1}\"]/register@[name=\"{2}\"]/bitfield@[name=\"{3}\"]".format(module_name, register_group, register_name, bitfield_name)

    print (bitfield_node_path)
    bitfield_node = ATDF.getNode(bitfield_node_path)

    if bitfield_node != None:
        if bitfield_node.getAttribute("values") == None:
            print (register_name + "_" + bitfield_name + "does not have value-group attribute")
        else:
            value_group_node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"{0}\"]/value-group@[name=\"{1}\"]".format(module_name, bitfield_node.getAttribute("values")))
            if value_group_node == None:
                print ("value-group = " + bitfield_node.getAttribute("values") + " not defined")
    else:
        print ("bitfield_name = " + bitfield_name + " not found" )

    return value_group_node
###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
def fileUpdate(symbol, event):
    global TCCfilesArray
    global InterruptVectorSecurity
    if event["value"] == False:
        TCCfilesArray[0].setSecurity("SECURE")
        TCCfilesArray[1].setSecurity("SECURE")
        TCCfilesArray[2].setSecurity("SECURE")
        TCCfilesArray[3].setSecurity("SECURE")
        TCCfilesArray[4].setSecurity("SECURE")
        TCCfilesArray[5].setSecurity("SECURE")
        TCCfilesArray[6].setSecurity("SECURE")
        TCCfilesArray[7].setSecurity("SECURE")
        TCCfilesArray[8].setSecurity("SECURE")
        TCCfilesArray[9].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TCCfilesArray[10].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, False)
    else:
        TCCfilesArray[0].setSecurity("NON_SECURE")
        TCCfilesArray[1].setSecurity("NON_SECURE")
        TCCfilesArray[2].setSecurity("NON_SECURE")
        TCCfilesArray[3].setSecurity("NON_SECURE")
        TCCfilesArray[4].setSecurity("NON_SECURE")
        TCCfilesArray[5].setSecurity("NON_SECURE")
        TCCfilesArray[6].setSecurity("NON_SECURE")
        TCCfilesArray[7].setSecurity("NON_SECURE")
        TCCfilesArray[8].setSecurity("NON_SECURE")
        TCCfilesArray[9].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        TCCfilesArray[10].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        Database.setSymbolValue("core", InterruptVectorSecurity, True)

def updateCodeGenerationProperty(symbol, event):
    component = symbol.getComponent()

    component.getSymbolByID("TCC_TIMER_HEADER").setEnabled(False)
    component.getSymbolByID("TCC_TIMER_SOURCE").setEnabled(False)
    component.getSymbolByID("TCC_COMPARE_HEADER").setEnabled(False)
    component.getSymbolByID("TCC_COMPARE_SOURCE").setEnabled(False)
    component.getSymbolByID("TCC_CAPTURE_HEADER").setEnabled(False)
    component.getSymbolByID("TCC_CAPTURE_SOURCE").setEnabled(False)
    component.getSymbolByID("TCC_PWM_HEADER").setEnabled(False)
    component.getSymbolByID("TCC_PWM_SOURCE").setEnabled(False)

    if tccSym_OperationMode.getValue() == "Timer":
        component.getSymbolByID("TCC_TIMER_HEADER").setEnabled(True)
        component.getSymbolByID("TCC_TIMER_SOURCE").setEnabled(True)
    elif tccSym_OperationMode.getValue() == "Compare":
        component.getSymbolByID("TCC_COMPARE_HEADER").setEnabled(True)
        component.getSymbolByID("TCC_COMPARE_SOURCE").setEnabled(True)
    elif tccSym_OperationMode.getValue() == "Capture":
        component.getSymbolByID("TCC_CAPTURE_HEADER").setEnabled(True)
        component.getSymbolByID("TCC_CAPTURE_SOURCE").setEnabled(True)
    elif tccSym_OperationMode.getValue() == "PWM":
        component.getSymbolByID("TCC_PWM_HEADER").setEnabled(True)
        component.getSymbolByID("TCC_PWM_SOURCE").setEnabled(True)

def updateTCCInterruptStatus(symbol, event):
    component = symbol.getComponent()
    mode = component.getSymbolValue("TCC_OPERATION_MODE")

    # For single interrupt line for peripheral
    if len(InterruptVector) == 1:
        Database.setSymbolValue("core", InterruptVector[0], False, 2)
        Database.setSymbolValue("core", InterruptHandlerLock[0], False, 2)
        Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_Handler", 2)

        if ((mode == "Timer" and component.getSymbolValue("TCC_TIMER_INTERRUPT_MODE") == True)
            or (mode == "Compare" and component.getSymbolValue("TCC_COMPARE_INTERRUPT_MODE") == True)
            or (mode == "Capture" and component.getSymbolValue("TCC_CAPTURE_INTERRUPT_MODE") == True)
            or (mode == "PWM" and component.getSymbolValue("TCC_PWM_INTERRUPT_MODE") == True)):
            Database.setSymbolValue("core", InterruptVector[0], True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], True, 2)
            Database.setSymbolValue("core", InterruptHandler[0], tccInstanceName.getValue() + "_InterruptHandler", 2)

    # For multiple interrupt lines for peripheral
    else:
        for intr in range(0, len(InterruptVector)):
            Database.setSymbolValue("core", InterruptVector[intr], False, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[intr], False, 2)
            Database.setSymbolValue("core", InterruptHandler[intr], InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0] + "_Handler", 2)

        if ((mode == "Timer" and component.getSymbolValue("TCC_TIMER_INTENSET_OVF") == True)
            or (mode == "Compare" and component.getSymbolValue("TCC_COMPARE_INTENSET_OVF") == True)
            or (mode == "Capture" and (component.getSymbolValue("TCC_CAPTURE_ERR_INTERRUPT_MODE") == True or component.getSymbolValue("TCC_CAPTURE_OVF_INTERRUPT_MODE") == True))
            or (mode == "PWM" and (component.getSymbolValue("TCC_INTENSET_OVF") == True or component.getSymbolValue("TCC_INTENSET_FAULT0") == True or component.getSymbolValue("TCC_INTENSET_FAULT1") == True))):

            Database.setSymbolValue("core", InterruptVector[0], True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[0], True, 2)
            Database.setSymbolValue("core", InterruptHandler[0],  InterruptHandler[0].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)

        if ((mode == "Timer" and component.getSymbolValue("TCC_TIMER_INTENSET_MC1") == True)):
            Database.setSymbolValue("core", InterruptVector[2], True, 2)
            Database.setSymbolValue("core", InterruptHandlerLock[2], True, 2)
            Database.setSymbolValue("core", InterruptHandler[2], InterruptHandler[2].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)

        if (mode == "Compare"):
            for intr in range(0, len(InterruptVector)):
                z = re.match("TCC\d+_MC(\d+)",InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0])
                if (z):
                    channelIndex = z.groups()[0]
                    if (component.getSymbolValue("TCC_COMPARE_INTENSET_MC" + str(channelIndex)) == True):
                        Database.setSymbolValue("core", InterruptVector[intr], True, 2)
                        Database.setSymbolValue("core", InterruptHandlerLock[intr], True, 2)
                        Database.setSymbolValue("core", InterruptHandler[intr], InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)

        if (mode == "Capture"):
            for intr in range(0, len(InterruptVector)):
                z = re.match("TCC\d+_MC(\d+)",InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0])
                if (z):
                    channelIndex = z.groups()[0]
                    if component.getSymbolValue("TCC_CAPTURE_INTENSET_MC" + str(channelIndex)) == True:
                        Database.setSymbolValue("core", InterruptVector[intr], True, 2)
                        Database.setSymbolValue("core", InterruptHandlerLock[intr], True, 2)
                        Database.setSymbolValue("core", InterruptHandler[intr], InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)

        if (mode == "PWM"):
            for intr in range(0, len(InterruptVector)):
                z = re.match("TCC\d+_MC(\d+)",InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0])
                if (z):
                    channelIndex = z.groups()[0]
                    if component.getSymbolValue("TCC_INTENSET_MC_" + str(channelIndex)) == True:
                        Database.setSymbolValue("core", InterruptVector[intr],True, 2)
                        Database.setSymbolValue("core", InterruptHandlerLock[intr], True, 2)
                        Database.setSymbolValue("core", InterruptHandler[intr], InterruptHandler[intr].split("_INTERRUPT_HANDLER")[0] + "_InterruptHandler", 2)


def updateTCCInterruptWarningStatus(symbol, event):
    global InterruptVectorUpdate
    global numOfChannels
    isVisible = False
    component = symbol.getComponent()
    if (component.getSymbolValue("TCC_INTENSET_OVF") or component.getSymbolValue("TCC_INTENSET_FAULT0") or
        component.getSymbolValue("TCC_INTENSET_FAULT1")):
        if (Database.getSymbolValue("core", InterruptVectorUpdate[0].split(".")[-1]) == True):
            isVisible = True
    else:
        for i in range(0, numOfChannels):
            if (component.getSymbolValue("TCC_INTENSET_MC_"+str(i)) == True):
                if (Database.getSymbolValue("core", InterruptVectorUpdate[1].split(".")[-1]) == True):
                    isVisible = True
    if (isVisible == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTCCClockWarningStatus(symbol, event):
    if event["value"] == False:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def updateTCCZeroClockFreqWarningStatus (symbol, event):
    symbol.setVisible(event["value"] == 0)

def tccSlaveCommentVisible(symbol, event):
    symbol.setVisible(event["value"])

def tccSlaveModeVisibility(symbol, event):
    symbol.setVisible(not event["value"])

def tccFrequencyCalc(symbol, event):
    global gclk_name
    clock_freq = Database.getSymbolValue("core", gclk_name + "_CLOCK_FREQUENCY")
    if clock_freq != 0:
        prescaler = int(tccSym_CTRLA_PRESCALER.getSelectedKey()[3:])
        freq = clock_freq /  prescaler
    else:
        freq = 0
    symbol.setValue(freq)
################################################################################
#### Dependency ####
################################################################################
def onAttachmentConnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]

    if connectID == tmrCapabilityId:
        localComponent.setCapabilityEnabled(tmrCapabilityId, True)
        localComponent.setCapabilityEnabled(pwmCapabilityId, False)
    elif connectID == pwmCapabilityId:
        localComponent.setCapabilityEnabled(tmrCapabilityId, False)
        localComponent.setCapabilityEnabled(pwmCapabilityId, True)

def onAttachmentDisconnected(source, target):
    localComponent = source["component"]
    remoteComponent = target["component"]
    remoteID = remoteComponent.getID()
    connectID = source["id"]
    targetID = target["id"]
    resetChannels()

    localComponent.setCapabilityEnabled(tmrCapabilityId, True)
    localComponent.setCapabilityEnabled(pwmCapabilityId, True)

    if remoteID == "sys_time":
        sysTimeComponentId.setValue("")
        tccSym_SYS_TIME_CONNECTED.setValue(False, 2)
        tccSym_OperationMode.setReadOnly(False)
        tccSym_TimerUnit.setReadOnly(False)
        tccSym_Timer_TIME_MS.setReadOnly(False)
        tccSym_Timer_INTENSET_OVF.setReadOnly(False)

# motor phases
global lastPwmChU
lastPwmChU = 0
global lastPwmChV
lastPwmChV = 1
global lastPwmChW
lastPwmChW = 2

def resetChannels():
    global lastPwmChU
    global lastPwmChV
    global lastPwmChW
    component = str(tccInstanceName.getValue()).lower()
    #disbale interrupt
    Database.setSymbolValue(component, "TCC_EVCTRL_EVACT1", 0)
    Database.setSymbolValue(component, "TCC_INTENSET_FAULT1", False)

def sysTimePLIBModeConfig(plibMode):
    global tccSym_TimerUnit
    global tccSym_OperationMode
    global tccSym_Timer_INTENSET_OVF

    if sysTimeComponentId.getValue() != "":
        if (plibMode == "SYS_TIME_PLIB_MODE_COMPARE"):
            print ("To be supported")
        if (plibMode == "SYS_TIME_PLIB_MODE_PERIOD"):
            #Set Timer mode
            tccSym_OperationMode.setReadOnly(True)
            tccSym_OperationMode.setValue("Timer")
            #Fix the timer unit to milliseconds
            tccSym_TimerUnit.setReadOnly(True)
            tccSym_TimerUnit.setValue("millisecond")
            #Enable the interrupt
            tccSym_Timer_INTENSET_OVF.setReadOnly(True)
            tccSym_Timer_INTENSET_OVF.setValue(True)

def handleMessage(messageID, args):
    global lastPwmChU
    global lastPwmChV
    global lastPwmChW

    global sysTimeComponentId
    global tccSym_SYS_TIME_CONNECTED
    global sysTimePlibMode
    global tccSym_Timer_TIME_MS

    global gclk_name

    component = str(tccInstanceName.getValue()).lower()
    dict = {}
    if (messageID == "PMSM_FOC_PWM_CONF"):
        resetChannels()

        dict['PWM_MAX_CH'] = 4

        lastPwmChU = pwmChU = args['PWM_PH_U']
        lastPwmChV = pwmChV = args['PWM_PH_V']
        lastPwmChW = pwmChW = args['PWM_PH_W']

        freq = args['PWM_FREQ']
        clock = int(Database.getSymbolValue("core", gclk_name + "_CLOCK_FREQUENCY"))
        period = int(clock)/int(freq)/2

        Database.setSymbolValue(component, "TCC_PER_PER", period)
        Database.setSymbolValue(component, "TCC_WAVE_WAVEGEN", 1)
        Database.setSymbolValue(component, "TCC_EVCTRL_OVFEO", True)

        Database.setSymbolValue(component, "TCC_"+str(pwmChU)+"_CC", 0)
        Database.setSymbolValue(component, "TCC_"+str(pwmChV)+"_CC", 0)
        Database.setSymbolValue(component, "TCC_"+str(pwmChW)+"_CC", 0)

        #macros for channel numbers
        Database.setSymbolValue(component, "PWM_PH_U", tccInstanceName.getValue()+"_CHANNEL"+str(pwmChU))
        Database.setSymbolValue(component, "PWM_PH_V", tccInstanceName.getValue()+"_CHANNEL"+str(pwmChV))
        Database.setSymbolValue(component, "PWM_PH_W", tccInstanceName.getValue()+"_CHANNEL"+str(pwmChW))
        Database.setSymbolValue(component, "INTR_PWM_FAULT", tccInstanceName.getValue()+"_OTHER_IRQn")
        mask = (1 << pwmChU) + (1 << pwmChV) + (1 << pwmChW)
        tccPhMask.setValue(mask)

        tccPatternMask.setValue((mask << 4) + mask)

        #dead-Time
        dt = args['PWM_DEAD_TIME']
        deadtime = int((clock) * float(dt)) / 1000000
        Database.setSymbolValue(component, "TCC_"+str(pwmChU)+"_WEXCTRL_DTIEN", True)
        Database.setSymbolValue(component, "TCC_"+str(pwmChV)+"_WEXCTRL_DTIEN", True)
        Database.setSymbolValue(component, "TCC_"+str(pwmChW)+"_WEXCTRL_DTIEN", True)
        Database.setSymbolValue(component, "TCC_WEXCTRL_DTHS", deadtime)
        Database.setSymbolValue(component, "TCC_WEXCTRL_DTLS", deadtime)

        #Fault
        Database.setSymbolValue(component, "TCC_EVCTRL_EVACT1", 5)
        Database.setSymbolValue(component, "TCC_INTENSET_FAULT1", True)
        fault = args['PWM_FAULT']
        Database.setSymbolValue(component, "TCC_0_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_1_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_2_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_3_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_4_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_5_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_6_DRVCTRL_NRE_NRV", 1)
        Database.setSymbolValue(component, "TCC_7_DRVCTRL_NRE_NRV", 1)

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):
        sysTimeComponentId.setValue(args["ID"])
        tccSym_SYS_TIME_CONNECTED.setValue(True, 2)
        modeDict = {"plib_mode": "PERIOD_MODE"}
        sysTimePLIBConfig = Database.sendMessage(sysTimeComponentId.getValue(), "SYS_TIME_PLIB_CAPABILITY", modeDict)
        sysTimePlibMode.setValue(sysTimePLIBConfig["plib_mode"])
        # Set up timer for either period mode or compare mode operation
        sysTimePLIBModeConfig(sysTimePLIBConfig["plib_mode"])
        # For period mode operation, also setup the time period
        if sysTimePLIBConfig["plib_mode"] == "SYS_TIME_PLIB_MODE_PERIOD":
            tccSym_Timer_TIME_MS.setReadOnly(True)
            tccSym_Timer_TIME_MS.setValue(sysTimePLIBConfig["sys_time_tick_ms"])

    if ((messageID == "SYS_TIME_PLIB_MODE_COMPARE") or (messageID == "SYS_TIME_PLIB_MODE_PERIOD")):
        sysTimePlibMode.setValue(messageID)
        sysTimePLIBModeConfig(messageID)

    if (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        tccSym_Timer_TIME_MS.setValue(args["sys_time_tick_ms"])

    return dict
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(tccComponent):

    global InterruptVector
    global InterruptHandler
    global InterruptHandlerLock
    global tccInstanceName
    global tccSym_INTENSET_OVF
    global InterruptVectorUpdate
    global InterruptVectorSecurity
    global size
    global sysTimePlibMode
    global tccSym_SYS_TIME_CONNECTED
    global sysTimeComponentId
    global tmrCapabilityId
    global pwmCapabilityId
    global gclk_name

    eventDepList = []
    interruptDepList = []

    tccInstanceName = tccComponent.createStringSymbol("TCC_INSTANCE_NAME", None)
    tccInstanceName.setVisible(False)
    tccInstanceName.setDefaultValue(tccComponent.getID().upper())

    tmrCapabilityId = tccInstanceName.getValue() + "_TMR"
    pwmCapabilityId = tccInstanceName.getValue() + "_PWM"

    tccEvsysGeneratorNamesPopulate(tccInstanceName.getValue())
    tccEvsysUserNamesPopulate(tccInstanceName.getValue())

    InterruptVectorSecurity = tccInstanceName.getValue() + "_SET_NON_SECURE"

    tcc_param_node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters")

    parameters = tcc_param_node.getChildren()

    gclk_name = ""
    for param in range (0, len(parameters)):
        if "GCLK_ID" in parameters[param].getAttribute("name"):
            gclk_name = tccInstanceName.getValue() + parameters[param].getAttribute("name").replace("GCLK_ID", "")

    #clock enable
    Database.setSymbolValue("core", gclk_name + "_CLOCK_ENABLE", True, 2)

    ################################ ATDF ####################################################
    node = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters")
    global numOfChannels
    numOfChannels = 4
    deadTimeImplemented = 1
    swapImplemented = 1
    outputMatrixImplemented = 1
    patternGenImplemented = 1
    numOfOutputs = 8
    size = 24
    parameters = []
    parameters = node.getChildren()
    for param in range (0, len(parameters)):
        if(parameters[param].getAttribute("name") == "CC_NUM"):
            numOfChannels = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "DTI"):
            deadTimeImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "SWAP"):
            swapImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "OTMX"):
            outputMatrixImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "OW_NUM"):
            numOfOutputs = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "PG"):
            patternGenImplemented = int(parameters[param].getAttribute("value"))
        if(parameters[param].getAttribute("name") == "SIZE"):
            size = int(parameters[param].getAttribute("value"))

    tccSym_NUM_CHANNELS = tccComponent.createIntegerSymbol("TCC_NUM_CHANNELS", None)
    tccSym_NUM_CHANNELS.setDefaultValue(int(numOfChannels))
    tccSym_NUM_CHANNELS.setVisible(False)

    tccSym_NUM_OUTPUTS = tccComponent.createIntegerSymbol("TCC_NUM_OUTPUTS", None)
    tccSym_NUM_OUTPUTS.setDefaultValue(int(numOfOutputs))
    tccSym_NUM_OUTPUTS.setVisible(False)

    tccSym_Is_DeadTime = tccComponent.createIntegerSymbol("TCC_IS_DEAD_TIME", None)
    tccSym_Is_DeadTime.setDefaultValue(int(deadTimeImplemented))
    tccSym_Is_DeadTime.setVisible(False)

    tccSym_Is_Swap = tccComponent.createIntegerSymbol("TCC_IS_SWAP", None)
    tccSym_Is_Swap.setDefaultValue(int(swapImplemented))
    tccSym_Is_Swap.setVisible(False)

    tccSym_Is_OTM = tccComponent.createIntegerSymbol("TCC_IS_OTM", None)
    tccSym_Is_OTM.setDefaultValue(int(outputMatrixImplemented))
    tccSym_Is_OTM.setVisible(False)

    tccSym_Is_PG = tccComponent.createIntegerSymbol("TCC_IS_PG", None)
    tccSym_Is_PG.setDefaultValue(int(patternGenImplemented))
    tccSym_Is_PG.setVisible(False)

    tccSym_SIZE = tccComponent.createIntegerSymbol("TCC_SIZE", None)
    tccSym_SIZE.setDefaultValue(int(size))
    tccSym_SIZE.setVisible(False)

    tccSym_MCU_FAMILY = tccComponent.createStringSymbol("TCC_MCU_FAMILY", None)
    tccSym_MCU_FAMILY.setVisible(False)
    node = ATDF.getNode("/avr-tools-device-file/devices")
    series = node.getChildren()[0].getAttribute("family")
    tccSym_MCU_FAMILY.setDefaultValue(node.getChildren()[0].getAttribute("family"))

    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"TCC\"]/register-group@[name=\"TCC\"]")
    register_names = []
    register_names = node.getChildren()

    tccSym_CBUF_REG_NAME = tccComponent.createStringSymbol("TCC_CBUF_REG_NAME", None)
    tccSym_CBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "CCBUF" in register_names[index].getAttribute("name"):
            tccSym_CBUF_REG_NAME.setDefaultValue("CCBUF")
            break
        else:
            tccSym_CBUF_REG_NAME.setDefaultValue("CCB")

    tccSym_PBUF_REG_NAME = tccComponent.createStringSymbol("TCC_PBUF_REG_NAME", None)
    tccSym_PBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "PERBUF" in register_names[index].getAttribute("name"):
            tccSym_PBUF_REG_NAME.setDefaultValue("PERBUF")
            break
        else:
            tccSym_PBUF_REG_NAME.setDefaultValue("PERB")

    tccSym_PATBUF_REG_NAME = tccComponent.createStringSymbol("TCC_PATBUF_REG_NAME", None)
    tccSym_PATBUF_REG_NAME.setVisible(False)
    for index in range(0, len(register_names)):
        if "PATTBUF" in register_names[index].getAttribute("name"):
            tccSym_PATBUF_REG_NAME.setDefaultValue("PATTBUF")
            break
        else:
            tccSym_PATBUF_REG_NAME.setDefaultValue("PATTB")

    # master slave mode
    tccInstanceMasterValue = 0
    tccInstanceMasterNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"TCC\"]/instance@[name=\""+tccInstanceName.getValue()+"\"]/parameters/param@[name=\"MASTER_SLAVE_MODE\"]")
    if (tccInstanceMasterNode != None):
        tccInstanceMasterValue = int(tccInstanceMasterNode.getAttribute("value"))
        if (tccInstanceMasterValue == 2):  #slave
            activeComponentList = Database.getActiveComponentIDs()
            temp = int(tccInstanceName.getValue().split("TCC")[1])
            masterComponentID = "TCC" + str(temp - 1)

    global tccSym_Slave_Mode
    tccSym_Slave_Mode = tccComponent.createBooleanSymbol("TCC_SLAVE_MODE", None)
    tccSym_Slave_Mode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:CTRLA")
    tccSym_Slave_Mode.setLabel("Enable Slave")
    tccSym_Slave_Mode.setDefaultValue(False)
    if ((tccInstanceMasterValue == 2)):
        tccSym_Slave_Mode.setVisible(True)
    else:
        tccSym_Slave_Mode.setVisible(False)

    if (tccInstanceMasterValue == 2):  #slave
        tccSym_Slave_Mode_Comment = tccComponent.createCommentSymbol("TCC_SLAVE_MODE_COMMENT", None)
        tccSym_Slave_Mode_Comment.setLabel("**** Ensure Master - " + str(masterComponentID) + " is in active components ****")
        tccSym_Slave_Mode_Comment.setVisible(False)
        tccSym_Slave_Mode_Comment.setDependencies(tccSlaveCommentVisible, ["TCC_SLAVE_MODE"])
    ###########################################################################################

    #------------------------Motor Control APIs----------------------------------------------------

    tccStartApi = tccComponent.createStringSymbol("PWM_START_API", None)
    tccStartApi.setVisible(False)
    tccStartApi.setValue(tccInstanceName.getValue()+"_PWMStart")

    tccStopApi = tccComponent.createStringSymbol("PWM_STOP_API", None)
    tccStopApi.setVisible(False)
    tccStopApi.setValue(tccInstanceName.getValue()+"_PWMStop")

    tccPeriodApi = tccComponent.createStringSymbol("PWM_GET_PERIOD_API", None)
    tccPeriodApi.setVisible(False)
    tccPeriodApi.setValue(tccInstanceName.getValue()+"_PWM"+str(size)+"bitPeriodGet")

    tccDutyApi = tccComponent.createStringSymbol("PWM_SET_DUTY_API", None)
    tccDutyApi.setVisible(False)
    tccDutyApi.setValue(tccInstanceName.getValue() + "_PWM"+str(size)+"bitDutySet")

    tccOpDisableApi = tccComponent.createStringSymbol("PWM_OUTPUT_DISABLE_API", None)
    tccOpDisableApi.setVisible(False)
    tccOpDisableApi.setValue(tccInstanceName.getValue() + "_PWMPatternSet")

    tccOpEnableApi = tccComponent.createStringSymbol("PWM_OUTPUT_ENABLE_API", None)
    tccOpEnableApi.setVisible(False)
    tccOpEnableApi.setValue(tccInstanceName.getValue() + "_PWMPatternSet")

    tccCallbackApi = tccComponent.createStringSymbol("PWM_CALLBACK_API", None)
    tccCallbackApi.setVisible(False)
    tccCallbackApi.setValue(tccInstanceName.getValue() + "_PWMCallbackRegister")

    tccPhU = tccComponent.createStringSymbol("PWM_PH_U", None)
    tccPhU.setVisible(False)
    tccPhU.setValue(tccInstanceName.getValue() + "CHANNEL0")

    tccPhV = tccComponent.createStringSymbol("PWM_PH_V", None)
    tccPhV.setVisible(False)
    tccPhV.setValue(tccInstanceName.getValue() + "CHANNEL1")

    tccPhW = tccComponent.createStringSymbol("PWM_PH_W", None)
    tccPhW.setVisible(False)
    tccPhW.setValue(tccInstanceName.getValue() + "CHANNEL2")

    global tccPhMask
    tccPhMask = tccComponent.createHexSymbol("PWM_PH_MASK", None)
    tccPhMask.setVisible(False)
    tccPhMask.setValue(0x7)

    global tccPatternMask
    tccPatternMask = tccComponent.createHexSymbol("PWM_PATTERN_MASK", None)
    tccPatternMask.setVisible(False)
    tccPatternMask.setValue(0x77)

    tccFaultInt = tccComponent.createStringSymbol("INTR_PWM_FAULT", None)
    tccFaultInt.setVisible(False)
    tccFaultInt.setValue(tccInstanceName.getValue()+"_OTHER_IRQn")


    tccSym_CTRLA_RUNSTDBY = tccComponent.createBooleanSymbol("TCC_CTRLA_RUNSTDBY", None)
    tccSym_CTRLA_RUNSTDBY.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:CTRLA")
    tccSym_CTRLA_RUNSTDBY.setLabel("Run during Standby")

    #prescaler configuration
    global tccSym_CTRLA_PRESCALER
    tccSym_CTRLA_PRESCALER = tccComponent.createKeyValueSetSymbol("TCC_CTRLA_PRESCALER", None)
    tccSym_CTRLA_PRESCALER.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:CTRLA")
    tccSym_CTRLA_PRESCALER.setLabel("Select Prescaler")
    tccSym_CTRLA_PRESCALER.setDefaultValue(0)
    tccSym_CTRLA_PRESCALER.setOutputMode("Key")
    tccSym_CTRLA_PRESCALER.setDisplayMode("Description")
    node = getValueGroupNode__TCC("TCC", "TCC", "CTRLA", "PRESCALER")
    values = []
    values = node.getChildren()
    for index in range(0, len(values)):
        tccSym_CTRLA_PRESCALER.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"),
        values[index].getAttribute("caption"))
    #tccSym_CTRLA_PRESCALER.setDependencies(tccSlaveModeVisibility, ["TCC_SLAVE_MODE"])

    tccSym_CTRLA_PRESCYNC = tccComponent.createKeyValueSetSymbol("TCC_CTRLA_PRESCYNC", None)
    tccSym_CTRLA_PRESCYNC.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:tcc_u2213;register:STATUS")
    tccSym_CTRLA_PRESCYNC.setLabel("Prescaler and Counter Synchronization")
    tccSym_CTRLA_PRESCYNC.setDefaultValue(1)
    tccSym_CTRLA_PRESCYNC.setOutputMode("Key")
    tccSym_CTRLA_PRESCYNC.setDisplayMode("Description")
    node = getValueGroupNode__TCC("TCC", "TCC", "CTRLA", "PRESCSYNC")
    values = []
    values = node.getChildren()
    for index in range(0, len(values)):
        tccSym_CTRLA_PRESCYNC.addKey(values[index].getAttribute("name"), values[index].getAttribute("value"),
        values[index].getAttribute("caption"))

    tccSym_Frequency = tccComponent.createIntegerSymbol("TCC_MODULE_FREQUENCY", None)
    tccSym_Frequency.setVisible(False)
    tccSym_Frequency.setDefaultValue(int(Database.getSymbolValue("core", gclk_name + "_CLOCK_FREQUENCY")))
    tccSym_Frequency.setDependencies(tccFrequencyCalc, ["TCC_CTRLA_PRESCALER", "core."+ gclk_name +"_CLOCK_FREQUENCY"])

    #tcc operation mode
    tccOperationModeList = ["PWM", "Timer", "Compare", "Capture"]
    global tccSym_OperationMode
    tccSym_OperationMode = tccComponent.createComboSymbol("TCC_OPERATION_MODE", None, tccOperationModeList)
    tccSym_OperationMode.setLabel("Operating Mode")
    tccSym_OperationMode.setDefaultValue("PWM")
    # if isMasterSlaveModeEnable == True:
    #     tccSym_OperationMode.setVisible(False)
    # if (tcInstanceMasterValue == 2):
    #     tccSym_OperationMode.setDependencies(tcSlaveModeVisible, [masterComponentSymbolId])


    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tcc_u2213/config/tcc_pwm.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tcc_u2213/config/tcc_timer.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tcc_u2213/config/tcc_compare.py")
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/tcc_u2213/config/tcc_capture.py")
    
    tccSym_OtherIntHandler = tccComponent.createStringSymbol("TCC_OTHER_INT_HANDLER_NAME", None)
    tccSym_OtherIntHandler.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################
    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues = vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == tccInstanceName.getValue():
            name = vectorValues[id].getAttribute("name")
            if any (int_name in name for int_name in ["OTHER", "DFS"]):
                tccSym_OtherIntHandler.setDefaultValue(name.replace(tccInstanceName.getValue() + "_", ""))
            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")

    tccSym_IntLines = tccComponent.createIntegerSymbol("TCC_NUM_INT_LINES", None)
    tccSym_IntLines.setVisible(False)
    tccSym_IntLines.setDefaultValue((len(InterruptVector) - 1))

    interruptDepList.append("TCC_OPERATION_MODE")
    # Interrupt Dynamic settings
    tccSym_UpdateInterruptStatus = tccComponent.createBooleanSymbol("TCC_INTERRUPT_STATUS", None)
    tccSym_UpdateInterruptStatus.setDependencies(updateTCCInterruptStatus, ["TCC_TIMER_INTERRUPT_MODE", "TCC_PWM_INTERRUPT_MODE",
            "TCC_COMPARE_INTERRUPT_MODE", "TCC_CAPTURE_INTERRUPT_MODE", "TCC_OPERATION_MODE"])
    tccSym_UpdateInterruptStatus.setVisible(False)

    # Interrupt Warning status
    tccSym_IntEnComment = tccComponent.createCommentSymbol("TCC_INTERRUPT_ENABLE_COMMENT", None)
    tccSym_IntEnComment.setVisible(False)
    tccSym_IntEnComment.setLabel("Warning!!! " + tccInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    #tccSym_IntEnComment.setDependencies(updateTCCInterruptWarningStatustccSym_IntEnComment.setDependencies(updateTCCInterruptWarningStatus, interruptDepList + InterruptVectorUpdate)

    # Clock Warning status
    tccSym_ClkEnComment = tccComponent.createCommentSymbol("TCC_CLOCK_ENABLE_COMMENT", None)
    tccSym_ClkEnComment.setLabel("Warning!!! TCC Peripheral Clock is Disabled in Clock Manager")
    tccSym_ClkEnComment.setVisible(False)
    tccSym_ClkEnComment.setDependencies(updateTCCClockWarningStatus, ["core." + gclk_name + "_CLOCK_ENABLE"])

    # Zero Clock Frequency Warning status
    tccSym_ZeroClkFreqComment = tccComponent.createCommentSymbol("TCC_ZERO_CLOCK_FREQ_COMMENT", None)
    tccSym_ZeroClkFreqComment.setLabel("Warning!!! TCC Peripheral Clock is 0 Hz")
    tccSym_ZeroClkFreqComment.setVisible(Database.getSymbolValue("core", tccInstanceName.getValue() + "_CLOCK_FREQUENCY") == 0)
    tccSym_ZeroClkFreqComment.setDependencies(updateTCCZeroClockFreqWarningStatus, ["core." + tccInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    tccInstanceName.setDependencies(updateCodeGenerationProperty, ["TCC_OPERATION_MODE"])
#------------------------------------------------------------
# Common Symbols needed for SYS_TIME usage
#------------------------------------------------------------
    sysTimePlibMode = tccComponent.createStringSymbol("SYS_TIME_PLIB_OPERATION_MODE", None)
    sysTimePlibMode.setLabel("SysTime PLIB Operation Mode")
    sysTimePlibMode.setVisible(False)
    sysTimePlibMode.setDefaultValue("")

    sysTimeComponentId = tccComponent.createStringSymbol("SYS_TIME_COMPONENT_ID", None)
    sysTimeComponentId.setLabel("Component id")
    sysTimeComponentId.setVisible(False)
    sysTimeComponentId.setDefaultValue("")

    # sysTimeTrigger_Sym = tccComponent.createBooleanSymbol("SYS_TIME", None)
    # sysTimeTrigger_Sym.setVisible(False)
    # sysTimeTrigger_Sym.setDependencies(sysTime_APIUpdate, ["TC_CTRLA_MODE"])

    tccSym_SYS_TIME_CONNECTED = tccComponent.createBooleanSymbol("TCC_SYS_TIME_CONNECTED", None)
    tccSym_SYS_TIME_CONNECTED.setDefaultValue(False)
    tccSym_SYS_TIME_CONNECTED.setVisible(False)

    tccTimerPrefix = tccInstanceName.getValue() + "_Timer"
    if tccSym_SIZE.getValue() == 32:
        tccTimerPrefix += "32bit"
    elif tccSym_SIZE.getValue() == 24:
        tccTimerPrefix += "24bit"
    else:
        tccTimerPrefix += "16bit"


    timerStartApiName = tccInstanceName.getValue() + "_TimerStart"
    timerStopApiName = tccInstanceName.getValue() + "_TimerStop "
    counterGetApiName = tccTimerPrefix +  "CounterGet"
    frequencyGetApiName = tccInstanceName.getValue() + "_TimerFrequencyGet"
    callbackApiName = tccInstanceName.getValue() + "_TimerCallbackRegister"
    periodSetApiName = tccTimerPrefix + "PeriodSet"

    timerWidth_Sym = tccComponent.createIntegerSymbol("TIMER_WIDTH", None)
    timerWidth_Sym.setVisible(False)
    timerWidth_Sym.setDefaultValue(32)

    timerPeriodMax_Sym = tccComponent.createStringSymbol("TIMER_PERIOD_MAX", None)
    timerPeriodMax_Sym.setVisible(False)
    timerPeriodMax_Sym.setDefaultValue("0xFFFFFFFF")

    timerStartApiName_Sym = tccComponent.createStringSymbol("TIMER_START_API_NAME", None)
    timerStartApiName_Sym.setVisible(False)
    timerStartApiName_Sym.setDefaultValue(timerStartApiName)

    timeStopApiName_Sym = tccComponent.createStringSymbol("TIMER_STOP_API_NAME", None)
    timeStopApiName_Sym.setVisible(False)
    timeStopApiName_Sym.setDefaultValue(timerStopApiName)

    counterApiName_Sym = tccComponent.createStringSymbol("COUNTER_GET_API_NAME", None)
    counterApiName_Sym.setVisible(False)
    counterApiName_Sym.setDefaultValue(counterGetApiName)

    frequencyGetApiName_Sym = tccComponent.createStringSymbol("FREQUENCY_GET_API_NAME", None)
    frequencyGetApiName_Sym.setVisible(False)
    frequencyGetApiName_Sym.setDefaultValue(frequencyGetApiName)

    callbackApiName_Sym = tccComponent.createStringSymbol("CALLBACK_API_NAME", None)
    callbackApiName_Sym.setVisible(False)
    callbackApiName_Sym.setDefaultValue(callbackApiName)

    periodSetApiName_Sym = tccComponent.createStringSymbol("PERIOD_SET_API_NAME", None)
    periodSetApiName_Sym.setVisible(False)
    periodSetApiName_Sym.setDefaultValue(periodSetApiName)

    irqEnumName_Sym = tccComponent.createStringSymbol("IRQ_ENUM_NAME", None)
    irqEnumName_Sym.setVisible(False)
    irqEnumName_Sym.setDefaultValue(InterruptVector[0][:-len("_INTERRUPT_ENABLE")] + "_IRQn")
#------------------------------------------------------------
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    tccSym_PWMHeaderFile = tccComponent.createFileSymbol("TCC_PWM_HEADER", None)
    tccSym_PWMHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_pwm.h.ftl")
    tccSym_PWMHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_PWMHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMHeaderFile.setType("HEADER")
    tccSym_PWMHeaderFile.setMarkup(True)

    tccSym_PWMSourceFile = tccComponent.createFileSymbol("TCC_PWM_SOURCE", None)
    tccSym_PWMSourceFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_pwm.c.ftl")
    tccSym_PWMSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_PWMSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_PWMSourceFile.setType("SOURCE")
    tccSym_PWMSourceFile.setMarkup(True)

    tccSym_TimerHeaderFile = tccComponent.createFileSymbol("TCC_TIMER_HEADER", None)
    tccSym_TimerHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_timer.h.ftl")
    tccSym_TimerHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_TimerHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_TimerHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_TimerHeaderFile.setType("HEADER")
    tccSym_TimerHeaderFile.setMarkup(True)

    tccSym_TimerSourceFile = tccComponent.createFileSymbol("TCC_TIMER_SOURCE", None)
    tccSym_TimerSourceFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_timer.c.ftl")
    tccSym_TimerSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_TimerSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_TimerSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_TimerSourceFile.setType("SOURCE")
    tccSym_TimerSourceFile.setMarkup(True)

    tccSym_CompareHeaderFile = tccComponent.createFileSymbol("TCC_COMPARE_HEADER", None)
    tccSym_CompareHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_compare.h.ftl")
    tccSym_CompareHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_CompareHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_CompareHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_CompareHeaderFile.setType("HEADER")
    tccSym_CompareHeaderFile.setMarkup(True)

    tccSym_CompareSourceFile = tccComponent.createFileSymbol("TCC_COMPARE_SOURCE", None)
    tccSym_CompareSourceFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_compare.c.ftl")
    tccSym_CompareSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_CompareSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_CompareSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_CompareSourceFile.setType("SOURCE")
    tccSym_CompareSourceFile.setMarkup(True)

    tccSym_CaptureHeaderFile = tccComponent.createFileSymbol("TCC_CAPTURE_HEADER", None)
    tccSym_CaptureHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_capture.h.ftl")
    tccSym_CaptureHeaderFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".h")
    tccSym_CaptureHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_CaptureHeaderFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_CaptureHeaderFile.setType("HEADER")
    tccSym_CaptureHeaderFile.setMarkup(True)

    tccSym_CaptureSourceFile = tccComponent.createFileSymbol("TCC_CAPTURE_SOURCE", None)
    tccSym_CaptureSourceFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_capture.c.ftl")
    tccSym_CaptureSourceFile.setOutputName("plib_"+tccInstanceName.getValue().lower()+".c")
    tccSym_CaptureSourceFile.setDestPath("/peripheral/tcc/")
    tccSym_CaptureSourceFile.setProjectPath("config/" + configName + "/peripheral/tcc/")
    tccSym_CaptureSourceFile.setType("SOURCE")
    tccSym_CaptureSourceFile.setMarkup(True)

    tccSym_PWMGlobalHeaderFile = tccComponent.createFileSymbol("TCC_GLOBAL_HEADER", None)
    tccSym_PWMGlobalHeaderFile.setSourcePath("../peripheral/tcc_u2213/templates/plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setOutputName("plib_tcc_common.h")
    tccSym_PWMGlobalHeaderFile.setDestPath("/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setProjectPath("config/" + configName +"/peripheral/tcc/")
    tccSym_PWMGlobalHeaderFile.setType("HEADER")
    tccSym_PWMGlobalHeaderFile.setMarkup(False)

    tccSym_SystemInitFile = tccComponent.createFileSymbol("TC_SYS_INT", None)
    tccSym_SystemInitFile.setType("STRING")
    tccSym_SystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    tccSym_SystemInitFile.setSourcePath("../peripheral/tcc_u2213/templates/system/initialization.c.ftl")
    tccSym_SystemInitFile.setMarkup(True)

    tccSym_SystemDefFile = tccComponent.createFileSymbol("TC_SYS_DEF", None)
    tccSym_SystemDefFile.setType("STRING")
    tccSym_SystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    tccSym_SystemDefFile.setSourcePath("../peripheral/tcc_u2213/templates/system/definitions.h.ftl")
    tccSym_SystemDefFile.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        global TCCfilesArray
        tccIsNonSecure = Database.getSymbolValue("core", tccComponent.getID().upper() + "_IS_NON_SECURE")
        tccSym_SystemDefFile.setDependencies(fileUpdate, ["core." + tccComponent.getID().upper() + "_IS_NON_SECURE"])
        TCCfilesArray.append(tccSym_PWMHeaderFile)
        TCCfilesArray.append(tccSym_PWMSourceFile)
        TCCfilesArray.append(tccSym_PWMGlobalHeaderFile)

        TCCfilesArray.append(tccSym_TimerHeaderFile)
        TCCfilesArray.append(tccSym_TimerSourceFile)
        TCCfilesArray.append(tccSym_CompareHeaderFile)
        TCCfilesArray.append(tccSym_CompareSourceFile)
        TCCfilesArray.append(tccSym_CaptureHeaderFile)
        TCCfilesArray.append(tccSym_CaptureSourceFile)

        TCCfilesArray.append(tccSym_SystemInitFile)
        TCCfilesArray.append(tccSym_SystemDefFile)
        Database.setSymbolValue("core", InterruptVectorSecurity, tccIsNonSecure)
        if tccIsNonSecure == False:
            TCCfilesArray[0].setSecurity("SECURE")
            TCCfilesArray[1].setSecurity("SECURE")
            TCCfilesArray[2].setSecurity("SECURE")
            TCCfilesArray[3].setSecurity("SECURE")
            TCCfilesArray[4].setSecurity("SECURE")
            TCCfilesArray[5].setSecurity("SECURE")
            TCCfilesArray[6].setSecurity("SECURE")
            TCCfilesArray[7].setSecurity("SECURE")
            TCCfilesArray[8].setSecurity("SECURE")

            TCCfilesArray[9].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
            TCCfilesArray[10].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
