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
import inspect

global sort_alphanumeric

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def handleMessage(messageID, args):
    global spiSym_SPICON_MSTEN
    global spiSym_SPICON_MSSEN
    global spiSymInterruptMode
    result_dict = {}

    if (messageID == "SPI_MASTER_MODE"):
        if args.get("isReadOnly") != None and args["isReadOnly"] == True:
            spiSym_SPICON_MSTEN.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None and args["isEnabled"] == True:
            spiSym_SPICON_MSTEN.setSelectedKey("Master mode")

    #elif (messageID == "SPI_SLAVE_MODE"):
        # To be implemented

    elif (messageID == "SPI_MASTER_INTERRUPT_MODE"):
        if args.get("isReadOnly") != None:
            spiSymInterruptMode.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None :
            spiSymInterruptMode.setValue(args["isEnabled"])
        if args.get("isVisible") != None:
            spiSymInterruptMode.setVisible(args["isVisible"])

    elif (messageID == "SPI_MASTER_HARDWARE_CS"):
        if args.get("isReadOnly") != None:
            spiSym_SPICON_MSSEN.setReadOnly(args["isReadOnly"])
        if args.get("isEnabled") != None:
            if args["isEnabled"] == False:
                spiSym_SPICON_MSSEN.setValue(1)
            else:
                spiSym_SPICON_MSSEN.setValue(0)
        if args.get("isVisible") != None:
            spiSym_SPICON_MSSEN.setVisible(args["isVisible"])

    #elif (messageID == "SPI_SLAVE_INTERRUPT_MODE"):
        # To be implemented

    return result_dict

################################################################################
#### Register Information ####
################################################################################
# SPICON Register

spiBitField_SPI2CON_ENHBUF = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="ENHBUF"]')

spiValGrp_SPI2CON_MSTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__MSTEN"]')
spiBitField_SPI2CON_MSTEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="MSTEN"]')

spiValGrp_SPI2CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__MSSEN"]')
spiBitField_SPI2CON_MSSEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="MSSEN"]')

spiValGrp_SPI2CON_MODE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__MODE32"]')
spiBitField_SPI2CON_MODE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="MODE32"]')

spiValGrp_SPI2CON_CKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__CKE"]')
spiBitField_SPI2CON_CKE = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="CKE"]')

spiValGrp_SPI2CON_CKP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__CKP"]')
spiBitField_SPI2CON_CKP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="SPI2CON"]/bitfield@[name="CKP"]')

spiValGrp_SPI2CON_SMP = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON__SMP"]')

spiValGrp_SPI2CON2_SPIROVEN = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/value-group@[name="SPI2CON2__SPIROVEN"]')

################################################################################
#### Global Variables ####
################################################################################

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

global dummyDataDict
'''
Dictionary is based off of values in ATDF file for keynames, instead of their captions.  The values will remain the same,
whereas the captions may vary between families that use this SPI PLIB.
'''
dummyDataDict = {
                    "0" : 0xFFFFFFFF,
                    "1" : 0xFFFFFFFF,
                    "2" : 0xFFFF,
                    "3" : 0xFF,
                }

################################################################################
#### Business Logic ####
################################################################################

def setSPIInterruptData(mode, status):

    for id in InterruptVector:
        if (("FAULT" in id) and (mode == "Master mode")):
            # Disable Fault interrupt for Master mode
            Database.setSymbolValue("core", id, False, 1)
        else:
            Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandlerLock:
        if (("FAULT" in id) and (mode == "Master mode")):
            Database.setSymbolValue("core", id, False, 1)
        else:
            Database.setSymbolValue("core", id, status, 1)

    for id in InterruptHandler:
        interruptName = id.split("_INTERRUPT_HANDLER")[0]
        if (("FAULT" in id) and (mode == "Master mode")):
            continue
        if status == True:
            Database.setSymbolValue("core", id, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", id, interruptName + "_Handler", 1)

def updateSPIInterruptData(symbol, event):

    mode = event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey()

    if event["id"] == "SPI_INTERRUPT_MODE":
        setSPIInterruptData(mode, event["value"])

    status = False

    for id in InterruptVectorUpdate:
        id = id.replace("core.", "")
        if (("FAULT" in id) and (mode == "Master mode")):
            continue
        elif Database.getSymbolValue("core", id) == True:
            status = True
            break

    if spiSymInterruptMode.getValue() == True and status == True:
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def _get_bitfield_names(node, outputList):

    valueNodes = node.getChildren()

    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved":  ##  skip (unused) reserved fields
            dict["desc"] = bitfield.getAttribute("caption")
            dict["key"] = bitfield.getAttribute("caption")

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            outputList.append(dict)

def getIRQIndex(string):

    irq_index = "-1"

    for param in interruptsChildren:
        if "irq-index" in param.getAttributeList():
            name = str(param.getAttribute("irq-name"))
            if string == name:
                irq_index = str(param.getAttribute("irq-index"))
                break
        else:
            break

    return irq_index

def getVectorIndex(string):

    vector_index = "-1"

    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if string == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index

def ClockModeInfo(symbol, event):

    CKEINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_PH")
    CPOLINDEX = Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_SPICON_CLK_POL")

    if event["id"] == "SPI_SPICON_CLK_PH":
        CKE = int(event["symbol"].getKeyValue(event["value"]))
        CPOL = 1 if CPOLINDEX == 0 else 0
    elif event["id"] == "SPI_SPICON_CLK_POL":
        CPOL = int(event["symbol"].getKeyValue(event["value"]))
        CKE = 1 if CKEINDEX == 0 else 0

    if (CPOL == 0) and (CKE == 1):
        symbol.setLabel("***SPI Mode 0 is Selected***")
    elif (CPOL == 0) and (CKE == 0):
        symbol.setLabel("***SPI Mode 1 is Selected***")
    elif (CPOL == 1) and (CKE == 1):
        symbol.setLabel("***SPI Mode 2 is Selected***")
    else:
        symbol.setLabel("***SPI Mode 3 is Selected***")

def showMasterDependencies(symbol, event):

    if event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey() == "Master mode":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def showSlaveDependencies(symbol, event):
    if event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey() == "Slave mode":
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def spiMasterModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey() == "Master mode")

def spiSlaveModeFileGeneration(symbol, event):
    symbol.setEnabled(event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey() == "Slave mode")

def updateSPISlaveBusyPinVisibility(symbol, event):

    spiMode = event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey()
    busyPinEnabled = event["source"].getSymbolByID("SPIS_USE_BUSY_PIN").getValue()
    symbol.setVisible(spiMode == "Slave mode" and busyPinEnabled == True)

def updateCNxValue(symbol, event):
    symbol.setValue(event["symbol"].getSelectedValue())

def updateIntReadOnlyAttr(symbol, event):
    symbol.setReadOnly(event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey() == "Slave mode")

def calculateBRGValue(clkfreq, baudRate):

    t_brg = 0

    if clkfreq != 0 and baudRate != 0:
        t_brg = ((int(clkfreq/baudRate) / 2) - 1)
        baudHigh = int (clkfreq / (2 * (t_brg + 1)))
        baudLow = int (clkfreq / (2 * (t_brg + 2)))
        errorHigh = baudHigh - baudRate
        errorLow = baudRate - baudLow

        if errorHigh > errorLow:
            t_brg +=1

    spiSym_BaudError_Comment.setVisible(False)

    ## Baud rate register is a 9/13 bit register
    if t_brg < 0:
        t_brg = 0
        spiSym_BaudError_Comment.setVisible(True)
    elif t_brg > spiSymMaxBRG.getValue():
        t_brg = spiSymMaxBRG.getValue()
        spiSym_BaudError_Comment.setVisible(True)

    return int(t_brg)

def SPIBRG_ValueUpdate(symbol, event):
    clkFreq = int(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    BaudRate = int (Database.getSymbolValue(spiInstanceName.getValue().lower(), "SPI_BAUD_RATE"))

    if event["id"] == "SPI_BAUD_RATE":
        BaudRate = int(event["value"])
    elif "_CLOCK_FREQUENCY" in event["id"]:
        clkFreq = int(event["value"])

    t_brg = calculateBRGValue(clkFreq, BaudRate)
    symbol.setValue(t_brg, 1)

global _find_key
def _find_key(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.
          value - the value to be looked for in the dictionary
          keypairs - the dictionary to be searched over
    '''
    for ii in mode_names:
        if(ii["key"] == str(value)):
            return ii["value"]


    print("_find_key: could not find value in dictionary") # should never get here
    return ""

def DummyData_ValueUpdate(symbol, event):
    spiMode = event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey()

    if event["id"] == "SPI_MSTR_MODE_EN":
        symbol.setVisible(spiMode == "Master mode")

    elif spiMode == "Master mode" and event["id"] == "SPI_SPICON_MODE":
        symbol.setValue(dummyDataDict[str(event["value"])], 1)
        symbol.setMax(dummyDataDict[str(event["value"])])

def updateSPIClockWarningStatus(symbol, event):

    symbol.setVisible(not event["value"])

def onCapabilityConnected(event):
    localComponent = event["localComponent"]
    remoteComponent = event["remoteComponent"]

    # This message should indicate to the dependent component that PLIB has finished its initialization and
    # is ready to accept configuration parameters from the dependent component
    argDict = {"localComponentID" : localComponent.getID()}
    argDict = Database.sendMessage(remoteComponent.getID(), "REQUEST_CONFIG_PARAMS", argDict)



def updateCNxValue (symbol, event):

    cnPinCountNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"PORT\"]/instance@[name=\"PORT\"]/parameters/param@[name=\"CN_PIN_COUNT\"]")
    CnPinCount = int(cnPinCountNode.getAttribute("value"))

    for i in range(CnPinCount):

        key = Database.getSymbolValue("core", "CN_PIN_" + str(i) + "_NAME")
        value = "CN" + str(i) + "_PIN"
        desc = key.split("_",2)
        symbol.addKey(key, value, desc[2])

def showCSPinConfigOptions (symbol, event):
    mode = event["source"].getSymbolByID("SPI_MSTR_MODE_EN").getSelectedKey()
    symbol.setVisible(mode == "Slave mode")

def getChipSelectPinList(ss_pin):
    # parse XML
    global pinoutXmlPath
    global spiSym_SPICON_MSTEN
    gpioIP = ""
    final_pin_list = []

    deviceFamily = Database.getSymbolValue("core", "PRODUCT_FAMILY")
    if deviceFamily in ["PIC32MX1185", "PIC32MX1290", "PIC32MX1404", "PIC32MX1168"]:
        gpioIP = "gpio_01618"
    elif deviceFamily in ["PIC32MX1156", "PIC32MX1143"]:
        gpioIP = "gpio_01166"
    else:
        gpioIP = "gpio_02467"

    currentPath = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
    gpioPlibPath = os.path.split(currentPath)[0]
    gpioPlibPath = os.path.split(gpioPlibPath)[0]
    gpioPlibPath = os.path.join(gpioPlibPath, gpioIP)
    deviceXmlPath = os.path.join(gpioPlibPath, "plugin/pin_xml/components/" + Variables.get("__PROCESSOR") + ".xml")
    deviceXmlTree = ET.parse(deviceXmlPath)
    deviceXmlRoot = deviceXmlTree.getroot()

    if gpioIP == "gpio_01166":
        spiSym_SPICON_MSTEN.setReadOnly(True)
    else:
        pinoutXmlName = deviceXmlRoot.get("families")
        pinoutXmlPath = os.path.join(gpioPlibPath, "plugin/pin_xml/families/" + pinoutXmlName + ".xml")
        pinoutXmlPath = os.path.normpath(pinoutXmlPath)

        tree = ET.parse(pinoutXmlPath)
        root = tree.getroot()
        tag_list = [elem.tag for elem in root.iter()]
        # Get all elements with tag = "group" and having attribute "id"
        group_elements = root.findall(".//group/[@id]")
        # Get a list of all group elements. Each element of list is a dictionary.
        # key is tag and value is attribute which is another dictionary.
        group_elements_list = [{t.tag : t.attrib} for t in group_elements]
        final_pin_list = []
        for group_elem in group_elements_list:
            target_elements = root.findall(".//group/[@id='" + group_elem["group"]["id"] + "']/*")
            # Create a list containing a dictionary of "tag":"attrib"
            # Each element of list is a dictionary. t.attrib is another dictionary.
            result = [{t.tag : t.attrib} for t in target_elements]
            for dic in result:
                if "function" in dic:
                    if ss_pin in dic["function"]["name"] and dic["function"]["direction"] == "in":
                        # Found the group containing the SSx function
                        for dic in result:
                            if "pin" in dic:
                                pin = dic["pin"]["name"]
                                # Discard any pin that does not start with character 'R'. Example: "PTG30"
                                if pin.startswith('R'):
                                    final_pin_list.append(pin.replace('P', ''))
                        break

    final_pin_list.sort()
    return final_pin_list

def instantiateComponent(spiComponent):

    global spiSym_BaudError_Comment
    global spiInstanceName
    global InterruptVector
    global InterruptHandlerLock
    global InterruptHandler
    global InterruptVectorUpdate
    global spiSymInterruptMode
    global spiSymMaxBRG
    global mode_names
    global spiSym_SPICON_MSTEN
    global spiSym_SPICON_MSSEN

    InterruptVector = []
    InterruptHandler = []
    InterruptHandlerLock = []
    InterruptVectorUpdate = []

    spiInstanceName = spiComponent.createStringSymbol("SPI_INSTANCE_NAME", None)
    spiInstanceName.setVisible(False)
    spiInstanceName.setDefaultValue(spiComponent.getID().upper())
    Log.writeInfoMessage("Running " + spiInstanceName.getValue())

    spiInstanceNum = spiComponent.createStringSymbol("SPI_INSTANCE_NUM", None)
    spiInstanceNum.setVisible(False)
    componentName = str(spiComponent.getID())
    instanceNum = filter(str.isdigit,componentName)
    spiInstanceNum.setDefaultValue(instanceNum)

    #Clock enable
    Database.setSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_ENABLE", True, 1)

    spiSymInterruptMode = spiComponent.createBooleanSymbol("SPI_INTERRUPT_MODE", None)
    spiSymInterruptMode.setLabel("Enable Interrrupts ?")
    spiSymInterruptMode.setDefaultValue(True)
    spiSymInterruptMode.setDependencies(updateIntReadOnlyAttr, ["SPI_MSTR_MODE_EN"])

    spiIrq = "SPI_" + spiInstanceNum.getValue()
    spiVectorNum = getVectorIndex(spiIrq)

    if spiVectorNum != "-1":
        InterruptVector.append(spiIrq + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrq + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrq + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrq + "_INTERRUPT_ENABLE_UPDATE")

        ## SPI Error IRQ
        spiIrqFault = spiInstanceName.getValue() + "_ERR"
        spiFaultVectorNum = int(getIRQIndex(spiIrqFault))

        ## SPI RX IRQ
        spiIrqrRx = spiInstanceName.getValue() + "_RX"
        spiRxVectorNum = int(getIRQIndex(spiIrqrRx))

        ## SPI TX IRQ
        spiIrqTx = spiInstanceName.getValue() + "_TX"
        spiTxVectorNum = int(getIRQIndex(spiIrqTx))
    else:
        ## SPI Fault Interrrupt
        spiIrqFault = spiInstanceName.getValue() + "_FAULT"
        InterruptVector.append(spiIrqFault + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrqFault + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrqFault + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrqFault + "_INTERRUPT_ENABLE_UPDATE")
        spiFaultVectorNum = int(getVectorIndex(spiIrqFault))

        ## SPI RX Interrupt
        spiIrqrRx = spiInstanceName.getValue() + "_RX"
        InterruptVector.append(spiIrqrRx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrqrRx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrqrRx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrqrRx + "_INTERRUPT_ENABLE_UPDATE")
        spiRxVectorNum = int(getVectorIndex(spiIrqrRx))

        ## SPI TX Interrupt
        spiIrqTx = spiInstanceName.getValue() + "_TX"
        InterruptVector.append(spiIrqTx + "_INTERRUPT_ENABLE")
        InterruptHandler.append(spiIrqTx + "_INTERRUPT_HANDLER")
        InterruptHandlerLock.append(spiIrqTx + "_INTERRUPT_HANDLER_LOCK")
        InterruptVectorUpdate.append("core." + spiIrqTx + "_INTERRUPT_ENABLE_UPDATE")
        spiTxVectorNum = int(getVectorIndex(spiIrqTx))

    spiInterruptCount = spiComponent.createIntegerSymbol("SPI_INTERRUPT_COUNT", None)
    spiInterruptCount.setDefaultValue(len(InterruptVector))
    spiInterruptCount.setVisible(False)


    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiFaultVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiFaultVectorNum)

    ## IEC REG
    spiIEC = spiComponent.createStringSymbol("SPI_FLT_IEC_REG", None)
    spiIEC.setDefaultValue(enblRegName)
    spiIEC.setVisible(False)

    ## IEC REG MASK
    spiIECMask = spiComponent.createStringSymbol("SPI_FLT_IEC_REG_MASK", None)
    spiIECMask.setDefaultValue(enblMask)
    spiIECMask.setVisible(False)

    ## IFS REG
    spiIFS = spiComponent.createStringSymbol("SPI_FLT_IFS_REG", None)
    spiIFS.setDefaultValue(statRegName)
    spiIFS.setVisible(False)

    ## IFS REG MASK
    spiIFSMask = spiComponent.createStringSymbol("SPI_FLT_IFS_REG_MASK", None)
    spiIFSMask.setDefaultValue(statMask)
    spiIFSMask.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiRxVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiRxVectorNum)

    ## IEC REG
    spiRXIEC = spiComponent.createStringSymbol("SPI_RX_IEC_REG", None)
    spiRXIEC.setDefaultValue(enblRegName)
    spiRXIEC.setVisible(False)

    ## IEC REG MASK
    spiRXIECMask = spiComponent.createStringSymbol("SPI_RX_IEC_REG_MASK", None)
    spiRXIECMask.setDefaultValue(enblMask)
    spiRXIECMask.setVisible(False)

    ## IFS REG
    spiRXIFS = spiComponent.createStringSymbol("SPI_RX_IFS_REG", None)
    spiRXIFS.setDefaultValue(statRegName)
    spiRXIFS.setVisible(False)

    ## IFS REG MASK
    spiRXIFSMask = spiComponent.createStringSymbol("SPI_RX_IFS_REG_MASK", None)
    spiRXIFSMask.setDefaultValue(statMask)
    spiRXIFSMask.setVisible(False)

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(spiTxVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(spiTxVectorNum)


    ## IEC REG
    spiTXIEC = spiComponent.createStringSymbol("SPI_TX_IEC_REG", None)
    spiTXIEC.setDefaultValue(enblRegName)
    spiTXIEC.setVisible(False)

    ## IEC REG MASK
    spiTXIECMask = spiComponent.createStringSymbol("SPI_TX_IEC_REG_MASK", None)
    spiTXIECMask.setDefaultValue(enblMask)
    spiTXIECMask.setVisible(False)

    ## IFS REG
    spiTXIFS = spiComponent.createStringSymbol("SPI_TX_IFS_REG", None)
    spiTXIFS.setDefaultValue(statRegName)
    spiTXIFS.setVisible(False)

    ## IFS REG MASK
    spiTXIFSMask = spiComponent.createStringSymbol("SPI_TX_IFS_REG_MASK", None)
    spiTXIFSMask.setDefaultValue(statMask)
    spiTXIFSMask.setVisible(False)

    ## MSTEN Selection Bit
    msten_names = []
    _get_bitfield_names(spiValGrp_SPI2CON_MSTEN, msten_names)
    spiSym_SPICON_MSTEN = spiComponent.createKeyValueSetSymbol( "SPI_MSTR_MODE_EN",None)
    spiSym_SPICON_MSTEN.setLabel(spiBitField_SPI2CON_MSTEN.getAttribute("caption"))
    spiSym_SPICON_MSTEN.setDefaultValue(0)
    spiSym_SPICON_MSTEN.setReadOnly(False)
    spiSym_SPICON_MSTEN.setOutputMode( "Value" )
    spiSym_SPICON_MSTEN.setDisplayMode( "Description" )
    for ii in msten_names:
        spiSym_SPICON_MSTEN.addKey( ii['key'],ii['value'], ii['desc'] )

    ## CLock Polarity
    clkpol_names = []
    _get_bitfield_names(spiValGrp_SPI2CON_CKP, clkpol_names)
    spiSym_SPICON_CLKPOL = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_CLK_POL",None)
    spiSym_SPICON_CLKPOL.setLabel(spiBitField_SPI2CON_CKP.getAttribute("caption"))
    spiSym_SPICON_CLKPOL.setDefaultValue(1)
    spiSym_SPICON_CLKPOL.setOutputMode( "Value" )
    spiSym_SPICON_CLKPOL.setDisplayMode( "Description" )
    for ii in clkpol_names:
        spiSym_SPICON_CLKPOL.addKey( ii['key'],ii['value'], ii['desc'] )

    ## Clock Phase Bit
    clkph_names = []
    _get_bitfield_names(spiValGrp_SPI2CON_CKE, clkph_names)
    spiSym_SPICON_CLKPH = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_CLK_PH",None)
    spiSym_SPICON_CLKPH.setLabel(spiBitField_SPI2CON_CKE.getAttribute("caption"))
    spiSym_SPICON_CLKPH.setDefaultValue(0)
    spiSym_SPICON_CLKPH.setOutputMode( "Value" )
    spiSym_SPICON_CLKPH.setDisplayMode( "Description" )
    for ii in clkph_names:
        spiSym_SPICON_CLKPH.addKey( ii['key'],ii['value'], ii['desc'] )

    ## input sample Bit
    smp_names = []
    _get_bitfield_names(spiValGrp_SPI2CON_SMP, smp_names)
    spiSym_SPICON_SMP = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_SMP",None)
    spiSym_SPICON_SMP.setLabel("SPI Data Input Sample Phase bit")
    spiSym_SPICON_SMP.setDefaultValue(1)
    spiSym_SPICON_SMP.setOutputMode( "Value" )
    spiSym_SPICON_SMP.setDisplayMode( "Description" )
    for ii in smp_names:
        spiSym_SPICON_SMP.addKey( ii['key'],ii['value'], ii['desc'] )
    spiSym_SPICON_SMP.setDependencies(showMasterDependencies, ["SPI_MSTR_MODE_EN"])

    ## Slave slect pin enable bit
    if spiBitField_SPI2CON_MSSEN is not None:
        ssen_names = []
        _get_bitfield_names(spiValGrp_SPI2CON_MSSEN, ssen_names)
        spiSym_SPICON_MSSEN = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_MSSEN",None)
        spiSym_SPICON_MSSEN.setLabel(spiBitField_SPI2CON_MSSEN.getAttribute("caption"))
        spiSym_SPICON_MSSEN.setDefaultValue(0)
        spiSym_SPICON_MSSEN.setOutputMode( "Value" )
        spiSym_SPICON_MSSEN.setDisplayMode( "Description" )
        for ii in ssen_names:
            spiSym_SPICON_MSSEN.addKey( ii['key'],ii['value'], ii['desc'] )
        spiSym_SPICON_MSSEN.setDependencies(showMasterDependencies, ["SPI_MSTR_MODE_EN"])

    ## SPI data width(Mode)
    spiSym_SPICON_MODE = spiComponent.createKeyValueSetSymbol( "SPI_SPICON_MODE",None)
    spiSym_SPICON_MODE.setLabel("Data Width")
    spiSym_SPICON_MODE.setDefaultValue(3)
    spiSym_SPICON_MODE.setOutputMode( "Value" )
    spiSym_SPICON_MODE.setDisplayMode( "Description" )

    spiSym_SPICON_MODE.addKey( "32-bit ", "3", "32-bit")
    spiSym_SPICON_MODE.addKey( "32-bit", "2", "32-bit")
    spiSym_SPICON_MODE.addKey( "16-bit", "1", "16-bit")
    spiSym_SPICON_MODE.addKey( "8-bit", "0", "8-bit")

    spiSym_Baud_Rate = spiComponent.createIntegerSymbol("SPI_BAUD_RATE", None)
    spiSym_Baud_Rate.setLabel("Baud Rate in Hz")
    spiSym_Baud_Rate.setDefaultValue(1000000)
    spiSym_Baud_Rate.setMin(1)
    spiSym_Baud_Rate.setMax(50000000)
    spiSym_Baud_Rate.setDependencies(showMasterDependencies, ["SPI_MSTR_MODE_EN"])

    #SPI Baud Rate not supported comment
    spiSym_BaudError_Comment = spiComponent.createCommentSymbol("SPI_BAUD_ERROR_COMMENT", None)
    spiSym_BaudError_Comment.setLabel("********** WARNING!: Baud Rate is out of range **********")
    spiSym_BaudError_Comment.setVisible(False)

    spixBRG = spiInstanceName.getValue() + "BRG"
    spixBRG_Bitfield = ATDF.getNode('/avr-tools-device-file/modules/module@[name="SPI"]/register-group@[name="SPI"]/register@[name="' + spixBRG + '"]/bitfield@[name="' + spixBRG + '"]')
    spiMaxBRG = int(str(spixBRG_Bitfield.getAttribute("mask")), 0)

    spiSymMaxBRG = spiComponent.createIntegerSymbol("SPI_MAX_BRG", None)
    spiSymMaxBRG.setDefaultValue(spiMaxBRG)
    spiSymMaxBRG.setVisible(False)

    ## Baud Rate generation
    spiDefaultMasterFreq = int(Database.getSymbolValue("core", spiInstanceName.getValue() + "_CLOCK_FREQUENCY"))
    defaultSPIBR = calculateBRGValue(spiDefaultMasterFreq, spiSym_Baud_Rate.getValue())

    spiSym_SPIBRG_VALUE = spiComponent.createIntegerSymbol("SPI_BRG_VALUE", None)
    spiSym_SPIBRG_VALUE.setVisible(False)
    spiSym_SPIBRG_VALUE.setDependencies(SPIBRG_ValueUpdate, ["SPI_BAUD_RATE", "core." + spiInstanceName.getValue() + "_CLOCK_FREQUENCY"])

    #Use setValue instead of setDefaultValue to store symbol value in default.xml
    spiSym_SPIBRG_VALUE.setValue(defaultSPIBR, 1)

    spiSymDummyData = spiComponent.createHexSymbol("SPI_DUMMY_DATA", None)
    spiSymDummyData.setLabel("Dummy Data")
    spiSymDummyData.setDescription("Dummy Data to be written during SPI Read")
    spiSymDummyData.setDefaultValue(0xFF)
    spiSymDummyData.setMin(0x0)
    spiSymDummyData.setDependencies(DummyData_ValueUpdate, ["SPI_SPICON_MODE", "SPI_MSTR_MODE_EN"])

    spiSymClockModeComment = spiComponent.createCommentSymbol("SPI_CLOCK_MODE_COMMENT", None)
    spiSymClockModeComment.setLabel("***SPI Mode 0 Selected***")
    spiSymClockModeComment.setDependencies(ClockModeInfo, ["SPI_SPICON_CLK_POL", "SPI_SPICON_CLK_PH"])

    # SPIS_TX_BUFFER_SIZE
    spisSym_TXBuffer_Size = spiComponent.createIntegerSymbol("SPIS_TX_BUFFER_SIZE", None)
    spisSym_TXBuffer_Size.setLabel("TX Buffer Size (in bytes)")
    spisSym_TXBuffer_Size.setMin(1)
    spisSym_TXBuffer_Size.setMax(65535)
    spisSym_TXBuffer_Size.setDefaultValue(256)
    spisSym_TXBuffer_Size.setVisible(False)
    spisSym_TXBuffer_Size.setDependencies(showSlaveDependencies, ["SPI_MSTR_MODE_EN"])

    # SPIS_RX_BUFFER_SIZE
    spisSym_RXBuffer_Size = spiComponent.createIntegerSymbol("SPIS_RX_BUFFER_SIZE", None)
    spisSym_RXBuffer_Size.setLabel("RX Buffer Size (in bytes)")
    spisSym_RXBuffer_Size.setMin(1)
    spisSym_RXBuffer_Size.setMax(65535)
    spisSym_RXBuffer_Size.setDefaultValue(256)
    spisSym_RXBuffer_Size.setVisible(False)
    spisSym_RXBuffer_Size.setDependencies(showSlaveDependencies, ["SPI_MSTR_MODE_EN"])

    spisSymCSPin = spiComponent.createKeyValueSetSymbol("SPIS_CS_PIN", None)
    spisSymCSPin.setVisible(False)
    spisSymCSPin.setLabel("Chip Select Pin")
    spisSymCSPin.setOutputMode("Key")
    spisSymCSPin.setDisplayMode("Description")
    spisSymCSPin.setDependencies(showSlaveDependencies, ["SPI_MSTR_MODE_EN"])

    # SPIS_CS_PIN
    slaveSelectPinList = getChipSelectPinList("SS" + spiInstanceNum.getValue())

    for pin in slaveSelectPinList:
        spisSymCSPin.addKey(pin, pin, pin)

    # SPIS_CS_PIN_LOGIC_LEVEL
    spisSymCSPinLogicLevel = spiComponent.createKeyValueSetSymbol("SPIS_CS_PIN_LOGIC_LEVEL", spisSymCSPin)
    spisSymCSPinLogicLevel.setLabel("Chip Select Pin Logic Level")
    spisSymCSPinLogicLevel.setVisible(False)
    spisSymCSPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    spisSymCSPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    spisSymCSPinLogicLevel.setDefaultValue(0)
    spisSymCSPinLogicLevel.setOutputMode("Key")
    spisSymCSPinLogicLevel.setDisplayMode("Description")
    spisSymCSPinLogicLevel.setDependencies(showCSPinConfigOptions, ["SPI_MSTR_MODE_EN"])

    # SPIS_CS_PIN_CONFIG_COMMENT
    spisSymCSPinConfigComment = spiComponent.createCommentSymbol("SPIS_CS_PIN_CONFIG_COMMENT", spisSymCSPin)
    spisSymCSPinConfigComment.setVisible(False)
    spisSymCSPinConfigComment.setLabel("***Enable Change Notification on the Chip Select pin in Pin Manager***")
    spisSymCSPinConfigComment.setDependencies(showCSPinConfigOptions, ["SPI_MSTR_MODE_EN"])

    # SPIS_USE_BUSY_PIN
    spisSymUseBusyPin = spiComponent.createBooleanSymbol("SPIS_USE_BUSY_PIN", None)
    spisSymUseBusyPin.setLabel("Use GPIO pin as Busy signal?")
    spisSymUseBusyPin.setDefaultValue(True)
    spisSymUseBusyPin.setVisible(False)
    spisSymUseBusyPin.setDependencies(showSlaveDependencies, ["SPI_MSTR_MODE_EN"])

    # SPIS_BUSY_PIN
    spisSymBusyPin = spiComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN", spisSymUseBusyPin)
    spisSymBusyPin.setVisible(False)
    spisSymBusyPin.setLabel("Slave Busy Pin")
    spisSymBusyPin.setOutputMode("Key")
    spisSymBusyPin.setDisplayMode("Description")
    spisSymBusyPin.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MSTR_MODE_EN", "SPIS_USE_BUSY_PIN"])

    availablePinDictionary = {}

    # Send message to core to get available pins
    availablePinDictionary = Database.sendMessage("core", "PIN_LIST", availablePinDictionary)

    for pad in sort_alphanumeric(availablePinDictionary.values()):
        key = pad
        value = list(availablePinDictionary.keys())[list(availablePinDictionary.values()).index(pad)]
        description = pad
        spisSymBusyPin.addKey(key, value, description)

    # SPIS_BUSY_PIN_LOGIC_LEVEL
    spisSymBusyPinLogicLevel = spiComponent.createKeyValueSetSymbol("SPIS_BUSY_PIN_LOGIC_LEVEL", spisSymUseBusyPin)
    spisSymBusyPinLogicLevel.setLabel("Slave Busy Pin Logic Level")
    spisSymBusyPinLogicLevel.setVisible(False)
    spisSymBusyPinLogicLevel.addKey("ACTIVE_LOW", "0", "Active Low")
    spisSymBusyPinLogicLevel.addKey("ACTIVE_HIGH", "1", "Active High")
    spisSymBusyPinLogicLevel.setDefaultValue(1)
    spisSymBusyPinLogicLevel.setOutputMode("Key")
    spisSymBusyPinLogicLevel.setDisplayMode("Description")
    spisSymBusyPinLogicLevel.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MSTR_MODE_EN", "SPIS_USE_BUSY_PIN"])

    # SPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT
    spisSymBusyPinConfigComment = spiComponent.createCommentSymbol("SPIS_SLAVE_BUSY_PIN_CONFIG_COMMENT", spisSymUseBusyPin)
    spisSymBusyPinConfigComment.setVisible(False)
    spisSymBusyPinConfigComment.setLabel("***Configure Busy pin as GPIO Output in Pin Manager***")
    spisSymBusyPinConfigComment.setDependencies(updateSPISlaveBusyPinVisibility, ["SPI_MSTR_MODE_EN", "SPIS_USE_BUSY_PIN"])

    if spiValGrp_SPI2CON2_SPIROVEN != None:
        spiCON2RegAvailable = spiComponent.createBooleanSymbol("SPI_CON2_SPIROVEN", None)
        spiCON2RegAvailable.setDefaultValue(True)
        spiCON2RegAvailable.setVisible(True)
    ############################################################################
    #### Dependency ####
    ############################################################################

    setSPIInterruptData(spiSym_SPICON_MSTEN.getSelectedKey(), spiSymInterruptMode.getValue())

    spiSymIntEnComment = spiComponent.createCommentSymbol("SPI_INTRRUPT_ENABLE_COMMENT", None)
    spiSymIntEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Interrupt is Disabled in Interrupt Manager")
    spiSymIntEnComment.setVisible(False)
    spiSymIntEnComment.setDependencies(updateSPIInterruptData, ["SPI_INTERRUPT_MODE"] + InterruptVectorUpdate)

    # Clock Warning status
    spiSym_ClkEnComment = spiComponent.createCommentSymbol("SPI_CLOCK_ENABLE_COMMENT", None)
    spiSym_ClkEnComment.setLabel("Warning!!! " + spiInstanceName.getValue() + " Peripheral Clock is Disabled in Clock Manager")
    spiSym_ClkEnComment.setVisible(False)
    spiSym_ClkEnComment.setDependencies(updateSPIClockWarningStatus, ["core." + spiInstanceName.getValue() + "_CLOCK_ENABLE"])

    ###################################################################################################
    ####################################### Driver Symbols ############################################
    ###################################################################################################

    #SPI 8-bit Character size Mask
    spiSym_CHSIZE_8BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_8_BIT_MASK", None)
    spiSym_CHSIZE_8BIT.setDefaultValue("0x00000000")
    spiSym_CHSIZE_8BIT.setVisible(False)

    #SPI 16-bit Character size Mask
    spiSym_CHSIZE_16BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_16_BIT_MASK", None)
    spiSym_CHSIZE_16BIT.setDefaultValue("0x00000400")
    spiSym_CHSIZE_16BIT.setVisible(False)

    #SPI 32-bit Character size Mask
    spiSym_CHSIZE_32BIT = spiComponent.createStringSymbol("SPI_CHARSIZE_BITS_32_BIT_MASK", None)
    spiSym_CHSIZE_32BIT.setDefaultValue("0x00000800")
    spiSym_CHSIZE_32BIT.setVisible(False)

    #SPI Clock Phase Leading Edge Mask
    spiSym_CPHA_LE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_LEADING_MASK", None)
    spiSym_CPHA_LE_Mask.setDefaultValue("0x00000100")
    spiSym_CPHA_LE_Mask.setVisible(False)

    #SPI Clock Phase Trailing Edge Mask
    spiSym_CPHA_TE_Mask = spiComponent.createStringSymbol("SPI_CLOCK_PHASE_TRAILING_MASK", None)
    spiSym_CPHA_TE_Mask.setDefaultValue("0x00000000")
    spiSym_CPHA_TE_Mask.setVisible(False)

    #SPI Clock Polarity Idle Low Mask
    spiSym_CPOL_IL_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_LOW_MASK", None)
    spiSym_CPOL_IL_Mask.setDefaultValue("0x00000000")
    spiSym_CPOL_IL_Mask.setVisible(False)

    #SPI Clock Polarity Idle High Mask
    spiSym_CPOL_IH_Mask = spiComponent.createStringSymbol("SPI_CLOCK_POLARITY_HIGH_MASK", None)
    spiSym_CPOL_IH_Mask.setDefaultValue("0x00000040")
    spiSym_CPOL_IH_Mask.setVisible(False)

    #SPI API Prefix
    spiSym_API_Prefix = spiComponent.createStringSymbol("SPI_PLIB_API_PREFIX", None)
    spiSym_API_Prefix.setDefaultValue(spiInstanceName.getValue())
    spiSym_API_Prefix.setVisible(False)

    #SPI Transmit data register
    transmitRegister = spiComponent.createStringSymbol("TRANSMIT_DATA_REGISTER", None)
    transmitRegister.setDefaultValue("&(" + spiInstanceName.getValue() + "BUF)")
    transmitRegister.setVisible(False)

    #SPI Receive data register
    receiveRegister = spiComponent.createStringSymbol("RECEIVE_DATA_REGISTER", None)
    receiveRegister.setDefaultValue("&(" + spiInstanceName.getValue() + "BUF)")
    receiveRegister.setVisible(False)

    ############################################################################
    #### Code Generation ####
    ############################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    spimCommonHeaderFile = spiComponent.createFileSymbol("SPI_COMMON_HEADER", None)
    spimCommonHeaderFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_master_common.h")
    spimCommonHeaderFile.setOutputName("plib_spi_master_common.h")
    spimCommonHeaderFile.setDestPath("peripheral/spi/spi_master")
    spimCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_master")
    spimCommonHeaderFile.setType("HEADER")
    spimCommonHeaderFile.setMarkup(False)
    spimCommonHeaderFile.setOverwrite(True)
    spimCommonHeaderFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Master mode")
    spimCommonHeaderFile.setDependencies(spiMasterModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    spimHeaderFile = spiComponent.createFileSymbol("SPI_HEADER", None)
    spimHeaderFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_master.h.ftl")
    spimHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_master.h")
    spimHeaderFile.setDestPath("/peripheral/spi/spi_master")
    spimHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_master")
    spimHeaderFile.setType("HEADER")
    spimHeaderFile.setMarkup(True)
    spimHeaderFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Master mode")
    spimHeaderFile.setDependencies(spiMasterModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    spimSourceFile = spiComponent.createFileSymbol("SPI_SOURCE", None)
    if spiBitField_SPI2CON_ENHBUF is not None:
        spimSourceFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_master.c.ftl")
    else:
        spimSourceFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_master_2.c.ftl")
    spimSourceFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_master.c")
    spimSourceFile.setDestPath("/peripheral/spi/spi_master")
    spimSourceFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_master")
    spimSourceFile.setType("SOURCE")
    spimSourceFile.setMarkup(True)
    spimSourceFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Master mode")
    spimSourceFile.setDependencies(spiMasterModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    # SPI slave mode files
    spisCommonHeaderFile = spiComponent.createFileSymbol("SPIS_COMMON_HEADER", None)
    spisCommonHeaderFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_slave_common.h")
    spisCommonHeaderFile.setOutputName("plib_spi_slave_common.h")
    spisCommonHeaderFile.setDestPath("peripheral/spi/spi_slave")
    spisCommonHeaderFile.setProjectPath("config/" + configName + "/peripheral/spi/spi_slave")
    spisCommonHeaderFile.setType("HEADER")
    spisCommonHeaderFile.setMarkup(False)
    spisCommonHeaderFile.setOverwrite(True)
    spisCommonHeaderFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Slave mode")
    spisCommonHeaderFile.setDependencies(spiSlaveModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    spisHeaderFile = spiComponent.createFileSymbol("SPIS_HEADER", None)
    spisHeaderFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_slave.h.ftl")
    spisHeaderFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_slave.h")
    spisHeaderFile.setDestPath("/peripheral/spi/spi_slave")
    spisHeaderFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_slave")
    spisHeaderFile.setType("HEADER")
    spisHeaderFile.setMarkup(True)
    spisHeaderFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Slave mode")
    spisHeaderFile.setDependencies(spiSlaveModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    spisSourceFile = spiComponent.createFileSymbol("SPIS_SOURCE", None)
    if spiBitField_SPI2CON_ENHBUF is not None:
        spisSourceFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_slave.c.ftl")
    else:
        spisSourceFile.setSourcePath("../peripheral/spi_00753/templates/plib_spi_slave_2.c.ftl")
    spisSourceFile.setOutputName("plib_" + spiInstanceName.getValue().lower() + "_slave.c")
    spisSourceFile.setDestPath("/peripheral/spi/spi_slave")
    spisSourceFile.setProjectPath("config/" + configName +"/peripheral/spi/spi_slave")
    spisSourceFile.setType("SOURCE")
    spisSourceFile.setMarkup(True)
    spisSourceFile.setEnabled(spiSym_SPICON_MSTEN.getSelectedKey() == "Slave mode")
    spisSourceFile.setDependencies(spiSlaveModeFileGeneration, ["SPI_MSTR_MODE_EN"])

    # Common files
    spiSystemInitFile = spiComponent.createFileSymbol("SPI_INIT", None)
    spiSystemInitFile.setType("STRING")
    spiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    spiSystemInitFile.setSourcePath("../peripheral/spi_00753/templates/system/initialization.c.ftl")
    spiSystemInitFile.setMarkup(True)

    spiSystemDefFile = spiComponent.createFileSymbol("SPI_DEF", None)
    spiSystemDefFile.setType("STRING")
    spiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    spiSystemDefFile.setSourcePath("../peripheral/spi_00753/templates/system/definitions.h.ftl")
    spiSystemDefFile.setMarkup(True)
