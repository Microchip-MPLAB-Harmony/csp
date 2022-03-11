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
##########            EVSYS DATABASE COMPONENTS           #####################
################################################################################
global createEVSYSChannelVectorList
global evsysChannelVectorList
evsysChannelVectorList = []

global user
global generator
global path
global channel

global evsysInstanceName
global InterruptVector
global InterruptHandler
global InterruptHandlerLock

global EVSYSfilesArray
global InterruptVectorSecurity
InterruptVectorSecurity = []
EVSYSfilesArray = []

channel = 0
path = {}
user = {}
generator = {}
generator_module = {}
user_module = {}


def userStatus(symbol, event):
    global channelUserMap
    global user
    channelNumber = int(str(symbol.getID()).split(
        "EVSYS_CHANNEL_")[1].split("_USER_READY")[0])
    if event["id"].startswith("EVSYS_USER_"):
        channelAssigned = event["value"] - 1
        channelUser = user.get(int(event["id"].split("EVSYS_USER_")[1]))
        channelUserMap[event["id"]] = channelAssigned

    userAvailable = False
    for key in channelUserMap.keys():
        if channelUserMap.get(key) == channelNumber:
            if Database.getSymbolValue(event["namespace"], "USER_" + user.get(int(key.split("EVSYS_USER_")[1])) + "_READY") == False:
                userAvailable = False
                break
            else:
                userAvailable = True
    symbol.setValue(userAvailable, 2)


def channelSource(symbol, event):
    global evsysGenerator
    channelNumber = int(str(symbol.getID()).split(
        "EVSYS_CHANNEL_")[1].split("_GENERATOR_ACTIVE")[0])
    symbol.setValue(Database.getSymbolValue(event["namespace"], "GENERATOR_" + str(
        evsysGenerator[channelNumber].getSelectedKey()) + "_ACTIVE"), 2)


def channelMenu(symbol, event):
    symbol.setVisible(event["value"])


def channelClockEnable(symbol, event):
    chID = event["id"].split('EVSYS_CHANNEL_')[1]
    if event["value"] == True:
        Database.setSymbolValue(
            "core", evsysInstanceName.getValue() + "_" + chID + "_CLOCK_ENABLE", True, 1)
    else:
        Database.setSymbolValue("core", evsysInstanceName.getValue(
        ) + "_" + chID + "_CLOCK_ENABLE", False, 1)


def overrunInterrupt(interrupt, event):
    interrupt.setVisible(event["value"] != 2)


def eventInterrupt(interrupt, event):
    interrupt.setVisible(event["value"] != 2)


def evsysIntset(interrupt, val):
    global InterruptVector
    global numsyncChannels
    global evsysChannelVectorList

    channelID = int(interrupt.getID().split("EVSYS_INTERRUPT_MODE")[1])

    # First clear all the interrupt related symbols
    Database.setSymbolValue(val["namespace"], "EVSYS_INTERRUPT_MODE_OTHER", False, 2)
    Database.setSymbolValue(val["namespace"], "INTERRUPT_ACTIVE", False, 2)

    vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
    # First disable all the EVSYS channel interrupt lines, unlock them and set the default handler
    for id in range(0, len(vectorValues)):
        if vectorValues[id].getAttribute("module-instance") == "EVSYS":
            vectorName = vectorValues[id].getAttribute("name")
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", False, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", False, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_Handler", 2)

    for channel in range(0 , numsyncChannels + 1):
        event = Database.getSymbolValue(val["namespace"], "EVSYS_CHANNEL_" + str(channel) + "_EVENT")
        overflow = Database.getSymbolValue(val["namespace"], "EVSYS_CHANNEL_" + str(channel) + "_OVERRUN")
        path = interrupt.getComponent().getSymbolByID("EVSYS_CHANNEL_" + str(channel) + "_PATH").getSelectedKey()
        result = (event or overflow) and (path != "ASYNCHRONOUS")

        if channel == channelID:
            interrupt.setValue(result, 2)
        if result:
            # Get the vector name to use for the given EVSYS channel
            vectorName = evsysChannelVectorList[channel].get(str(channel))
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_ENABLE", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER_LOCK", True, 2)
            Database.setSymbolValue("core", vectorName + "_INTERRUPT_HANDLER", vectorName + "_InterruptHandler", 2)
            Database.setSymbolValue(val["namespace"], "EVSYS_INTERRUPT_MAX_CHANNEL", channel, 2)
            Database.setSymbolValue(val["namespace"], "INTERRUPT_ACTIVE", True, 2)
            if "OTHER" in vectorName:
                Database.setSymbolValue(val["namespace"], "EVSYS_INTERRUPT_MODE_OTHER", True, 2)


def updateEVSYSInterruptWarringStatus(symbol, event):
    if evsysInterrupt.getValue() == True:
        symbol.setVisible(event["value"])

def evsysNonSecCalculation(symbol, event):
    global numsyncChannels
    global evsysChannelVectorList
    nonSecure = False
    channel = int(event["id"].split("_")[2])
    if Database.getSymbolValue(event["namespace"], "EVSYS_CHANNEL_" + str(channel)):
        if not str(event["id"]).startswith("EVSYS_CHANNEL_"):
            if(event["value"] == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)))
                nonSecure = True
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))))
                nonSecure = False
        else:
            if(Database.getSymbolValue(event["namespace"], "EIC_NONSEC_" + str(channel)) == True):
                symbol.setValue((symbol.getValue() | (0x1 << channel)))
                nonSecure = True
            else:
                symbol.setValue((symbol.getValue() & (~(0x1 << channel))))
                nonSecure = False
    else:
        symbol.setValue((symbol.getValue() & (~(0x1 << channel))))
        nonSecure = False

    if channel < numsyncChannels:
        Database.setSymbolValue("core", evsysChannelVectorList[channel].get(str(channel)) + "_SET_NON_SECURE", nonSecure)

def evsysUserNonSecCalculation(symbol, event):
    user = int(event["id"].split("_")[3])
    if user > 31:
        if(event["value"] == 1):
            Database.setSymbolValue(event["namespace"], "EVSYS_NONSEC_USER1",
            ((Database.getSymbolValue(event["namespace"], "EVSYS_NONSEC_USER1") | (0x1 << (user - 32)))))
        else:
            Database.setSymbolValue(event["namespace"], "EVSYS_NONSEC_USER1",
            ((Database.getSymbolValue(event["namespace"], "EVSYS_NONSEC_USER1") & (~(0x1 << (user - 32))))))
    else:
        if(event["value"] == 1):
            Database.setSymbolValue(event["namespace"], "EVSYS_NONSEC_USER0",
            ((Database.getSymbolValue(event["namespace"], "EVSYS_NONSEC_USER0") | (0x1 << user))))
        else:
            Database.setSymbolValue(event["namespace"], "EVSYS_NONSEC_USER0",
            ((Database.getSymbolValue(event["namespace"], "EVSYS_NONSEC_USER0") & (~(0x1 << user)))))

def evsysUserNonSecVisible(symbol, event):
    if event["value"] != 0:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def fileGenLogic(symbol, event):
    global EVSYSfilesArray
    if int(Database.getSymbolValue(event["namespace"], "EVSYS_NONSEC")) > 0:
        EVSYSfilesArray[0].setEnabled(True)
        EVSYSfilesArray[1].setEnabled(True)
        EVSYSfilesArray[2].setEnabled(True)
    else:
        EVSYSfilesArray[0].setEnabled(False)
        EVSYSfilesArray[1].setEnabled(False)
        EVSYSfilesArray[2].setEnabled(False)

def createEVSYSChannelVectorList(evsysChannelCount, localComponent):
    # Returns a list containing dictionary {channel_number : vector_name}, where vector_name is read from ATDF
    # The list index corelates to EVSYS channel and contains a dictionary with channel number and the vector name to use for that channel
    # Total size of the list will be equal to EVSYS_CHANNEL_NUMBER (read from ATDF)
    # Example: evsysChannelVectorList = [{0 : EVSYS_0}, {1 : EVSYS_1}, {2 : EVSYS_2}, {3 : EVSYS_3}, ... {31 : EVSYS_31}]
    global evsysChannelVectorList
    evsysVectorNameList = []

    vectorValues = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

    for id in range(0, len(vectorValues)):
        if vectorValues[id].getAttribute("module-instance") == "EVSYS":
            evsysVectorNameList.append(vectorValues[id].getAttribute("name"))

    for n in evsysVectorNameList:
        if "OTHER" in n:
            for y in range(len(evsysChannelVectorList), evsysChannelCount):
                evsysChannelVectorList.append({str(y): n})

            evsysIntOther = localComponent.createBooleanSymbol("EVSYS_INTERRUPT_MODE_OTHER", None)
            evsysIntOther.setVisible(False)

        else:
            channelList = n[6:].split("_")
            if len(channelList) == 1:
                evsysChannelVectorList.append({channelList[0]: n})
            else:
                startCh = channelList[0]
                endCh = channelList[1]
                for x in range(int(startCh), int(endCh) + 1):
                    evsysChannelVectorList.append({str(x): n})

    return evsysChannelVectorList

def instantiateComponent(evsysComponent):
    global evsysInstanceName
    global InterruptVector
    InterruptVector=[]
    global InterruptHandler
    InterruptHandler=[]
    global InterruptHandlerLock
    InterruptHandlerLock=[]
    InterruptVectorUpdate=[]
    global evsysInterrupt
    global numsyncChannels
    global user
    global channel
    global channelUserMap
    channelUserMap={}
    evsysnonSecList = []
    evsysUserNonSecList = []
    global evsysGenerator
    evsysGenerator=[]
    channelUserDependency=[]

    # Get the number of channels supporting Synchronous and asynchronous path
    dummyNode=ATDF.getNode(
        '/avr-tools-device-file/modules/module@[name="EVSYS"]/register-group@[name="EVSYS"]/register@[name="INTSTATUS"]')
    numsyncChannels=len(dummyNode.getChildren()) - 1
    evsysInstanceName=evsysComponent.createStringSymbol(
        "EVSYS_INSTANCE_NAME", None)
    evsysInstanceName.setVisible(False)
    evsysInstanceName.setDefaultValue(evsysComponent.getID().upper())
    Log.writeInfoMessage("Running " + evsysInstanceName.getValue())

    # EVSYS Main Menu
    evsysSym_Menu=evsysComponent.createMenuSymbol("EVSYS_MENU", None)
    evsysSym_Menu.setLabel("EVSYS MODULE SETTINGS ")

    generatorSymbol=[]
    generatorsNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/events/generators")
    for id in range(0, len(generatorsNode.getChildren())):
        generator[generatorsNode.getChildren()[id].getAttribute("name")]=int(
            generatorsNode.getChildren()[id].getAttribute("index"))
        generatorActive=evsysComponent.createBooleanSymbol(
            "GENERATOR_" + str(generatorsNode.getChildren()[id].getAttribute("name")) + "_ACTIVE", evsysSym_Menu)
        generatorActive.setVisible(False)
        generatorActive.setDefaultValue(False)
        generatorSymbol.append(
            "GENERATOR_" + str(generatorsNode.getChildren()[id].getAttribute("name")) + "_ACTIVE")

    usersNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/events/users")
    for id in range(0, len(usersNode.getChildren())):
        user[int(usersNode.getChildren()[id].getAttribute("index"))
             ]=usersNode.getChildren()[id].getAttribute("name")
        userReady=evsysComponent.createBooleanSymbol(
            "USER_" + str(usersNode.getChildren()[id].getAttribute("name")) + "_READY", evsysSym_Menu)
        userReady.setVisible(False)
        userReady.setDefaultValue(False)
        channelUserMap["EVSYS_USER_"
                       + str(usersNode.getChildren()[id].getAttribute("index"))]= -1
        channelUserDependency.append(
            "EVSYS_USER_" + str(usersNode.getChildren()[id].getAttribute("index")))
        channelUserDependency.append(
            "USER_" + str(usersNode.getChildren()[id].getAttribute("name")) + "_READY")

    channelNode=ATDF.getNode(
        '/avr-tools-device-file/devices/device/peripherals/module@[name="EVSYS"]/instance@[name="' + evsysInstanceName.getValue() + '"]/parameters')
    for id in range(0, len(channelNode.getChildren())):
        if (channelNode.getChildren()[id].getAttribute("name") == "CHANNELS") or (channelNode.getChildren()[id].getAttribute("name") == "CHIP_EVSYS_CHANNELS"):
            channel=int(channelNode.getChildren()[id].getAttribute("value"))
            break

    evsysChannelNum=evsysComponent.createIntegerSymbol(
        "EVSYS_CHANNEL_NUMBER", evsysSym_Menu)
    evsysChannelNum.setVisible(False)
    evsysChannelNum.setDefaultValue(int(channel))
    evsysChannelNum.setVisible(False)

    evsysChannelNum=evsysComponent.createIntegerSymbol(
        "NUM_SYNC_CHANNELS", evsysSym_Menu)
    evsysChannelNum.setVisible(False)
    evsysChannelNum.setDefaultValue(int(numsyncChannels))

    evsysUserNum=evsysComponent.createIntegerSymbol(
        "EVSYS_USER_NUMBER", evsysSym_Menu)
    evsysUserNum.setVisible(False)
    evsysUserNum.setDefaultValue(int(max(user.keys())))

    evsysPriority=evsysComponent.createKeyValueSetSymbol(
        "EVSYS_CHANNEL_SCHEDULING", evsysSym_Menu)
    evsysPriority.setLabel("Scheduling Policy")
    evsysPriority.addKey(
        "STATIC", "0", "Static scheduling scheme for channels with level priority")
    evsysPriority.addKey(
        "ROUND-ROBIN", "1", "Round-robin scheduling scheme for channels with level priority")
    evsysPriority.setOutputMode("Value")

    createEVSYSChannelVectorList(int(channel), evsysComponent)

    for id in range(0, channel):
        evsysChannel=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id), evsysSym_Menu)
        evsysChannel.setLabel("Enable Channel " + str(id))
        evsysChannel.setDefaultValue(False)

        # Dummy symbol to control clock enable
        evsysClockEnable=evsysComponent.createBooleanSymbol(
            "EVSYS_CLOCK_ENABLE_" + str(id), evsysSym_Menu)
        evsysClockEnable.setDefaultValue(False)
        evsysClockEnable.setVisible(False)
        evsysClockEnable.setDependencies(
            channelClockEnable, ["EVSYS_CHANNEL_" + str(id)])

        evsysChannelMenu=evsysComponent.createMenuSymbol(
            "EVSYS_MENU_" + str(id), evsysChannel)
        evsysChannelMenu.setLabel("EVSYS Channel Configuration")
        evsysChannelMenu.setVisible(False)
        evsysChannelMenu.setDependencies(
            channelMenu, ["EVSYS_CHANNEL_" + str(id)])

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            evsysSecurity = evsysComponent.createKeyValueSetSymbol("EVSYS_NONSEC_" + str(id), evsysChannelMenu)
            evsysSecurity.setLabel("Security mode")
            evsysSecurity.addKey("SECURE", "0", "False")
            evsysSecurity.addKey("NON-SECURE", "1", "True")
            evsysSecurity.setOutputMode("Key")
            evsysSecurity.setDisplayMode("Key")
            evsysSecurity.setVisible(True)
            evsysSecurity.setDefaultValue(0)
            evsysnonSecList.append("EVSYS_NONSEC_" + str(id))
            evsysnonSecList.append("EVSYS_CHANNEL_" + str(id))



        evsysGenerator.append(id)
        evsysGenerator[id]=evsysComponent.createKeyValueSetSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_GENERATOR", evsysChannelMenu)
        evsysGenerator[id].setLabel("Event Generator")
        evsysGenerator[id].setOutputMode("Value")
        for key in sorted(generator.keys()):
            evsysGenerator[id].addKey(key, str(generator.get(key)), key)

        evsysGeneratorActive=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_GENERATOR_ACTIVE", evsysChannelMenu)
        evsysGeneratorActive.setDefaultValue(False)
        evsysGeneratorActive.setVisible(True)
        evsysGeneratorActive.setLabel("Channel Generator source Active")
        evsysGeneratorActive.setReadOnly(True)
        generatorSymbol.append("EVSYS_CHANNEL_" + str(id) + "_GENERATOR")
        evsysGeneratorActive.setDependencies(channelSource, generatorSymbol)
        del generatorSymbol[-1]

        evsysPath=evsysComponent.createKeyValueSetSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_PATH", evsysChannelMenu)
        evsysPath.setLabel("Path Selection")
        evsysPath.setOutputMode("Value")
        pathNode=ATDF.getNode(
            '/avr-tools-device-file/modules/module@[name="EVSYS"]/value-group@[name="EVSYS_CHANNEL__PATH"]')
        for i in range(0, len(pathNode.getChildren())):
            evsysPath.addKey(pathNode.getChildren()[i].getAttribute("name"), str(pathNode.getChildren()[
                             i].getAttribute("value")), pathNode.getChildren()[i].getAttribute("caption"))
            if pathNode.getChildren()[i].getAttribute("name") == "ASYNCHRONOUS":
                defaultIndex = i
        evsysPath.setDefaultValue(defaultIndex)
        if id > numsyncChannels:
            evsysPath.setReadOnly(True)

        evsysEdge=evsysComponent.createKeyValueSetSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_EDGE", evsysChannelMenu)
        evsysEdge.setLabel("Event Edge Selection")
        edgeNode=ATDF.getNode(
            '/avr-tools-device-file/modules/module@[name="EVSYS"]/value-group@[name="EVSYS_CHANNEL__EDGSEL"]')
        for i in range(0, len(edgeNode.getChildren())):
            evsysEdge.addKey(edgeNode.getChildren()[i].getAttribute("name"), str(edgeNode.getChildren()[
                             i].getAttribute("value")), edgeNode.getChildren()[i].getAttribute("caption"))
        evsysEdge.setDefaultValue(0)
        evsysEdge.setOutputMode("Value")

        evsysOnDemand=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_ONDEMAND", evsysChannelMenu)
        evsysOnDemand.setLabel("Generic Clock On Demand")
        evsysOnDemand.setDefaultValue(False)

        evsysRunStandby=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_RUNSTANDBY", evsysChannelMenu)
        evsysRunStandby.setLabel("Run In Standby Sleep Mode")
        evsysRunStandby.setDefaultValue(False)

        evsysEvent=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_EVENT", evsysChannelMenu)
        evsysEvent.setLabel("Enable Event Detection Interrupt")
        evsysEvent.setDefaultValue(False)
        evsysEvent.setVisible(False)
        evsysEvent.setDependencies(
            eventInterrupt, ["EVSYS_CHANNEL_" + str(id) + "_PATH"])

        evsysOverRun=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_OVERRUN", evsysChannelMenu)
        evsysOverRun.setLabel("Enable Overrun Interrupt")
        evsysOverRun.setDefaultValue(False)
        evsysOverRun.setVisible(False)
        evsysOverRun.setDependencies(
            overrunInterrupt, ["EVSYS_CHANNEL_" + str(id) + "_PATH"])

        evsysUserReady=evsysComponent.createBooleanSymbol(
            "EVSYS_CHANNEL_" + str(id) + "_USER_READY", evsysChannelMenu)
        evsysUserReady.setDefaultValue(False)
        evsysUserReady.setVisible(True)
        evsysUserReady.setLabel("Channel Users Ready")
        evsysUserReady.setReadOnly(True)
        evsysUserReady.setDependencies(userStatus, channelUserDependency)

        if id <= numsyncChannels:
            evsysInterrupt=evsysComponent.createBooleanSymbol(
                "EVSYS_INTERRUPT_MODE" + str(id),  evsysSym_Menu)
            evsysInterrupt.setVisible(False)
            evsysInterrupt.setDefaultValue(False)
            evsysInterrupt.setDependencies(evsysIntset, [
                                           "EVSYS_CHANNEL_" + str(id) + "_OVERRUN", "EVSYS_CHANNEL_" + str(id) + "_EVENT", "EVSYS_CHANNEL_" + str(id) + "_PATH"])

    evsysUserMenu=evsysComponent.createMenuSymbol(
        "EVSYS_USER_MENU", evsysSym_Menu)
    evsysUserMenu.setLabel("EVSYS User SETTINGS ")

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        nonSecReg = evsysComponent.createHexSymbol("EVSYS_NONSEC" , None)
        nonSecReg.setDefaultValue(0)
        nonSecReg.setVisible(False)
        nonSecReg.setDependencies(evsysNonSecCalculation, evsysnonSecList)

    for id in user.keys():
        evsysUserChannel=evsysComponent.createKeyValueSetSymbol(
            "EVSYS_USER_" + str(id), evsysUserMenu)
        evsysUserChannel.setLabel(str(user.get(id)) + " Channel Selection")
        evsysUserChannel.addKey("NONE", str(0), "No Channel Selected")
        for i in range(0, channel):
            evsysUserChannel.addKey(
                "CHANNEL_" + str(i), str(hex(i + 1)), "Use Channel" + str(id))
        evsysUserChannel.setOutputMode("Value")
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            evsysUserSecurity = evsysComponent.createKeyValueSetSymbol("EVSYS_USER_NONSEC_" + str(id), evsysUserChannel)
            evsysUserSecurity.setLabel("Security mode")
            evsysUserSecurity.addKey("SECURE", "0", "False")
            evsysUserSecurity.addKey("NON-SECURE", "1", "True")
            evsysUserSecurity.setOutputMode("Key")
            evsysUserSecurity.setDisplayMode("Key")
            evsysUserSecurity.setVisible(False)
            evsysUserSecurity.setDefaultValue(0)
            evsysUserSecurity.setDependencies(evsysUserNonSecVisible, ["EVSYS_USER_" + str(id)])
            evsysUserNonSecList.append("EVSYS_USER_NONSEC_" + str(id))

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        nonSecUser0Reg = evsysComponent.createHexSymbol("EVSYS_NONSEC_USER0" , None)
        nonSecUser0Reg.setDefaultValue(0)
        nonSecUser0Reg.setVisible(False)
        nonSecUser0Reg.setDependencies(evsysUserNonSecCalculation, evsysUserNonSecList)
        if (evsysUserNum.getValue() > 31):
            nonSecUser1Reg = evsysComponent.createHexSymbol("EVSYS_NONSEC_USER1" , None)
            nonSecUser1Reg.setDefaultValue(0)
            nonSecUser1Reg.setVisible(False)
            nonSecUser1Reg.setDependencies(evsysUserNonSecCalculation, evsysUserNonSecList)

        evsysUserNonSecRegNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="EVSYS"]/register-group@[name="EVSYS"]/register@[name="NONSECUSER0"]')
        evsysUserNonSecReg = evsysComponent.createBooleanSymbol("EVSYS_NONSEC_USER_REG", None)
        evsysUserNonSecReg.setDefaultValue((evsysUserNonSecRegNode != None))
        evsysUserNonSecReg.setVisible(False)

    ############################################################################
    #### Dependency ####
    ############################################################################
    evsysNumIntLines = 0

    vectorNode=ATDF.getNode(
        "/avr-tools-device-file/devices/device/interrupts")
    vectorValues=vectorNode.getChildren()
    for id in range(0, len(vectorNode.getChildren())):
        if vectorValues[id].getAttribute("module-instance") == "EVSYS":
            name=vectorValues[id].getAttribute("name")
            InterruptVector.append(name + "_INTERRUPT_ENABLE")
            InterruptHandler.append(name + "_INTERRUPT_HANDLER")
            InterruptHandlerLock.append(name + "_INTERRUPT_HANDLER_LOCK")
            InterruptVectorUpdate.append(
                "core." + name + "_INTERRUPT_ENABLE_UPDATE")
            InterruptVectorSecurity.append(name + "_SET_NON_SECURE")

            evsysIntName = evsysComponent.createStringSymbol("EVSYS_INT_NAME_" + str(evsysNumIntLines) , evsysUserMenu)
            evsysIntName.setDefaultValue(vectorValues[id].getAttribute("name").replace("EVSYS_", ""))
            evsysIntName.setVisible(False)

            evsysNumIntLines = evsysNumIntLines + 1

    evsysIntLines = evsysComponent.createIntegerSymbol("EVSYS_INT_LINES", evsysUserMenu)
    evsysIntLines.setDefaultValue(evsysNumIntLines)
    evsysIntLines.setVisible(False)

    # Interrupt Warning status
    evsysSym_IntEnComment=evsysComponent.createCommentSymbol(
        "EVSYS_INTERRUPT_ENABLE_COMMENT", None)
    evsysSym_IntEnComment.setVisible(False)
    evsysSym_IntEnComment.setLabel(
        "Warning!!! EVSYS Interrupt is Disabled in Interrupt Manager")
    evsysSym_IntEnComment.setDependencies(
        updateEVSYSInterruptWarringStatus, InterruptVectorUpdate)

    evsysInterruptMode = evsysComponent.createBooleanSymbol("INTERRUPT_ACTIVE", None)
    evsysInterruptMode.setDefaultValue(False)
    evsysInterruptMode.setVisible(False)

    evsysIntEnableForMaxChannel = evsysComponent.createIntegerSymbol("EVSYS_INTERRUPT_MAX_CHANNEL", evsysSym_Menu)
    evsysIntEnableForMaxChannel.setVisible(False)
    evsysIntEnableForMaxChannel.setDefaultValue(0)
    # ################################################################################
    # ##########             CODE GENERATION             #############################
    # ################################################################################

    configName=Variables.get("__CONFIGURATION_NAME")

    evsysSym_HeaderFile=evsysComponent.createFileSymbol("EVSYS_HEADER", None)
    evsysSym_HeaderFile.setSourcePath(
        "../peripheral/evsys_u2504/templates/plib_evsys.h.ftl")
    evsysSym_HeaderFile.setOutputName(
        "plib_" + evsysInstanceName.getValue().lower() + ".h")
    evsysSym_HeaderFile.setDestPath("peripheral/evsys")
    evsysSym_HeaderFile.setProjectPath(
        "config/" + configName + "/peripheral/evsys")
    evsysSym_HeaderFile.setType("HEADER")
    evsysSym_HeaderFile.setMarkup(True)

    evsysSym_SourceFile=evsysComponent.createFileSymbol("EVSYS_SOURCE", None)
    evsysSym_SourceFile.setSourcePath(
        "../peripheral/evsys_u2504/templates/plib_evsys.c.ftl")
    evsysSym_SourceFile.setOutputName(
        "plib_" + evsysInstanceName.getValue().lower() + ".c")
    evsysSym_SourceFile.setDestPath("peripheral/evsys")
    evsysSym_SourceFile.setProjectPath(
        "config/" + configName + "/peripheral/evsys")
    evsysSym_SourceFile.setType("SOURCE")
    evsysSym_SourceFile.setMarkup(True)

    evsysSystemInitFile=evsysComponent.createFileSymbol(
        "EVSYS_SYS_INIT", None)
    evsysSystemInitFile.setType("STRING")
    evsysSystemInitFile.setOutputName(
        "core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    evsysSystemInitFile.setSourcePath(
        "../peripheral/evsys_u2504/templates/system/initialization.c.ftl")
    evsysSystemInitFile.setMarkup(True)

    evsysSystemDefFile=evsysComponent.createFileSymbol("EVSYS_SYS_DEF", None)
    evsysSystemDefFile.setType("STRING")
    evsysSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    evsysSystemDefFile.setSourcePath(
        "../peripheral/evsys_u2504/templates/system/definitions.h.ftl")
    evsysSystemDefFile.setMarkup(True)

    evsysComponent.addPlugin(
        "../peripheral/evsys_u2504/plugin/eventsystem.jar")

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        nonSecevsysSym_HeaderFile=evsysComponent.createFileSymbol("EVSYS_HEADER_NON_SEC", None)
        nonSecevsysSym_HeaderFile.setSourcePath("../peripheral/evsys_u2504/templates/trustZone/plib_evsys.h.ftl")
        nonSecevsysSym_HeaderFile.setOutputName("plib_" + evsysInstanceName.getValue().lower() + ".h")
        nonSecevsysSym_HeaderFile.setDestPath("peripheral/evsys")
        nonSecevsysSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/evsys")
        nonSecevsysSym_HeaderFile.setType("HEADER")
        nonSecevsysSym_HeaderFile.setMarkup(True)
        nonSecevsysSym_HeaderFile.setEnabled(False)

        nonSecevsysSym_SourceFile=evsysComponent.createFileSymbol("EVSYS_SOURCE_NON_SEC", None)
        nonSecevsysSym_SourceFile.setSourcePath("../peripheral/evsys_u2504/templates/trustZone/plib_evsys.c.ftl")
        nonSecevsysSym_SourceFile.setOutputName("plib_" + evsysInstanceName.getValue().lower() + ".c")
        nonSecevsysSym_SourceFile.setDestPath("peripheral/evsys")
        nonSecevsysSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/evsys")
        nonSecevsysSym_SourceFile.setType("SOURCE")
        nonSecevsysSym_SourceFile.setMarkup(True)
        nonSecevsysSym_SourceFile.setEnabled(False)

        nonSecevsysSystemDefFile=evsysComponent.createFileSymbol("EVSYS_SYS_DEF_NON_SEC", None)
        nonSecevsysSystemDefFile.setType("STRING")
        nonSecevsysSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        nonSecevsysSystemDefFile.setSourcePath("../peripheral/evsys_u2504/templates/system/definitions.h.ftl")
        nonSecevsysSystemDefFile.setMarkup(True)
        nonSecevsysSystemDefFile.setEnabled(False)
        nonSecevsysSystemDefFile.setDependencies(fileGenLogic, ["EVSYS_NONSEC"])

        EVSYSfilesArray.append(nonSecevsysSym_HeaderFile)
        EVSYSfilesArray.append(nonSecevsysSym_SourceFile)
        EVSYSfilesArray.append(nonSecevsysSystemDefFile)


        evsysSym_HeaderFile.setSecurity("SECURE")
        evsysSym_SourceFile.setSecurity("SECURE")
        evsysSystemInitFile.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS")
        evsysSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")