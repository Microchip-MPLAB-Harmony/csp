# coding: utf-8
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

from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

global dmaBitfield_DCH0CON_CHPRI

global dmacActiveChannels
dmacActiveChannels = []

global peridValueListSymbols
peridValueListSymbols = []

global dmacInstanceName

global dmacInterruptVectorUpdate
dmacInterruptVectorUpdate = []

global dmacHeaderFile
global dmacSourceFile
global dmacSystemInitFile
global dmacSystemDefFile

global dmacEnable

dmaReg_DMAECON_SIRQEN     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMAC"]/register-group@[name="DMAC"]/register@[name="DCH0ECON"]/bitfield@[name="SIRQEN"]')
dmaBitVal_DMAECON_SIRQEN  = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMAC"]/value-group@[name="DCH0ECON__SIRQEN"]').getChildren()
dmaValGrp_DCH0CON_CHPRI   = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMAC"]/value-group@[name="DCH0CON__CHPRI"]')
dmaBitfield_DCH0CON_CHPRI = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMAC"]/register-group@[name="DMAC"]/register@[name="DCH0CON"]/bitfield@[name="CHPRI"]')
dmacBaseAddress           = ATDF.getNode('/avr-tools-device-file/devices/device/peripherals/module@[name="DMAC"]/instance@[name="DMAC"]/register-group')

################################################################################
#### Business Logic ####
################################################################################

global _get_position

def _get_position(maskval):

    # finds the least significant bit position of maskval
    if maskval.find('0x') != -1:
        value = maskval[2:]
    else:
        value = maskval

    for ii in range(0, 31):
        if int(value) & (1 << ii):
            break

    return ii

def dmacTriggerCalc(symbol, event):

    global per_instance

    # the "chan enable" boolean is for in/visible setting
    if event["id"].find("DMAC_CHAN") != -1:
        symbol.setVisible(event["value"])
        return
    else:  # get the value for the given key, namely, the interrupt number for this key name
        symbol.setValue(int(per_instance.get(event["value"])), 2)

# This function enables DMA channel and selects respective trigger if DMA mode
# is selected for any peripheral ID.
# And once the DMA mode is unselected, then the corresponding DMA channel will
# be disabled and trigger source will be reset to "Software trigger"
def dmacChannelAllocLogic(symbol, event):

    dmaChannelCount = Database.getSymbolValue("core", "DMA_CHANNEL_COUNT")
    perID = event["id"].split('DMA_CH_NEEDED_FOR_')[1]
    channelAllocated = False

    triggerSource = perID

    if "Transmit" in perID:
        triggerSource = perID.replace("Transmit", "TX")
    elif "Receive" in perID:
        triggerSource = perID.replace("Receive", "RX")

    for dmaChannel in range(dmaChannelCount):
        dmaChannelEnable = Database.getSymbolValue("core", "DMAC_CHAN" + str(dmaChannel) + "_ENBL")
        dmaChannelPerID = str(Database.getSymbolValue("core", "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE"))

        if dmaChannelPerID == perID:
            channelAllocated = True
            break
            
        # Client requested to allocate channel
        if event["value"] == True:
            # Reserve the first available free channel
            if dmaChannelEnable == False:
                Database.setSymbolValue("core", "DMAC_CHAN" + str(dmaChannel) + "_ENBL", True, 2)
                Database.setSymbolValue("core", "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE", triggerSource, 2)
                Database.setSymbolValue("core", "DMAC_REQUEST_" + str(dmaChannel) + "_PERID_LOCK", True, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, dmaChannel, 2)
                channelAllocated = True
                break

        # Client requested to deallocate channel
        else:
            # Reset the previously allocated channel
            if triggerSource == dmaChannelPerID and dmaChannelEnable == True:
                Database.setSymbolValue("core", "DMAC_CHAN" + str(dmaChannel) + "_ENBL", False, 2)
                Database.setSymbolValue("core", "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE", "Software Trigger", 2)
                Database.setSymbolValue("core", "DMAC_REQUEST_" + str(dmaChannel) + "_PERID_LOCK", False, 2)
                Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -1, 2)

    if event["value"] == True and channelAllocated == False:
        # Couldn't find any free DMA channel, hence set warning.
        Database.clearSymbolValue("core", "DMA_CH_FOR_" + perID)
        Database.setSymbolValue("core", "DMA_CH_FOR_" + perID, -2, 2)

# The following business logic creates a list of enabled DMA channels and sorts
# them in the descending order. The left most channel number will be the highest
# index enabled, also if the list is empty then none of the channel is enabled.
# Highest index will be used to create DMAC objects in source code.
# List empty or non-empty status helps to generate/discard DMAC code.
def dmacGlobalLogic(symbol, event):

    global dmacActiveChannels

    index = (event["id"].replace("DMAC_CHAN", "")).replace("_ENBL", "")

    try:
        index = int(index)
    except:
        return

    if event["value"] == True:
        if index not in dmacActiveChannels:
            dmacActiveChannels.append(index)
    else :
        if index in dmacActiveChannels:
            dmacActiveChannels.remove(index)

    dmacActiveChannels.sort()
    dmacActiveChannels.reverse()

    # Check if the list is not empty first since list element is accessed in the code
    if dmacActiveChannels:
        if symbol.getID() == "DMAC_HIGHEST_CHANNEL":
            symbol.setValue(int(dmacActiveChannels[0]) + 1, 2)

    if symbol.getID() == "DMA_ENABLE":
        if dmacActiveChannels and symbol.getValue() == False:
            symbol.setValue(True, 2)

        if not dmacActiveChannels:
            symbol.setValue(False, 2)

def onGlobalEnableLogic(symbol, event):

    # File generation logic
    dmacHeaderFile.setEnabled(event["value"])
    dmacSourceFile.setEnabled(event["value"])
    dmacSystemInitFile.setEnabled(event["value"])
    dmacSystemDefFile.setEnabled(event["value"])

def dmacPriorityCalc(symbol, event):

    global per_priority

    # the "chan enable" boolean is for in/visible setting
    if event["id"].find("DMAC_CHAN") != -1:
        symbol.setVisible(event["value"])
        return
    else:  # get the value for the given key, namely, the priority number for this key name
        symbol.clearValue()
        symbol.setValue(int(per_priority.get(event["value"])), 2)

def updateDMACChannelInterruptData(symbol, event):

    # Sees if the user has not enabled the particular DMAC interrupt when enabling this channel.
    # If so, will display a warning message.

    if "_ENBL" in event["id"]:
        # the "chan enable" boolean is for in/visible setting
        channelNumber = (event["id"].replace("DMAC_CHAN", "")).replace("_ENBL", "")

        InterruptVector = dmaInterruptName + channelNumber + "_INTERRUPT_ENABLE"
        InterruptHandler = dmaInterruptName + channelNumber + "_INTERRUPT_HANDLER"
        InterruptHandlerLock = dmaInterruptName + channelNumber + "_INTERRUPT_HANDLER_LOCK"
        InterruptVectorUpdate = dmaInterruptName + channelNumber + "_INTERRUPT_ENABLE_UPDATE"

        Database.setSymbolValue("core", InterruptVector, event["value"], 1)
        Database.setSymbolValue("core", InterruptHandlerLock, event["value"], 1)

        if event["value"] == True:
            Database.setSymbolValue("core", InterruptHandler, dmaInterruptName + channelNumber + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", InterruptHandler, dmaInterruptName + channelNumber + "_Handler", 1)

    else:
        InterruptVectorUpdate = event["id"].replace("core.", "")

    if event["value"] == True and Database.getSymbolValue("core", InterruptVectorUpdate) == True :
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx/IECx register index as well as
    # mask and bit location within it for given interrupt
    temp = float(vectorNumber) / 32.0
    index = int(temp)
    bit = float(temp % 1)
    bitPosn = int(32.0 * bit)
    bitMask = hex(1 << bitPosn)
    regIndex = str(index)

    return regIndex, str(bitPosn), str(bitMask)

def dchconCallback(symbol, event):

    # callback for setting the register DCHxCON
    global dmaBitfield_DCH0CON_CHPRI
    global dmacPriorityVal
    global _get_position
    global chpriSym

    channel = 0

    for s in list(event["id"]):
        if s.isdigit():
            channel = int(s)

    if((event["id"] == "DMAC_CHAN" + str(channel) + "_ENBL") and (event["value"] == False)):
        dmacDchconSym[channel].setValue(0,2)  # for not enabled channel, clear register
        chpriSym[channel].setValue("0",2)       # for comment in ftl file
    else:
        prio_mask = dmaBitfield_DCH0CON_CHPRI.getAttribute("mask")  # get mask from atdf file
        prio_lsb = _get_position(prio_mask)  # compute shift value of CHPRI bitfield
        priority = int(dmacPriorityVal[channel].getValue())
        shifted_priority = priority << prio_lsb
        dmacDchconSym[channel].setValue(shifted_priority,2)
        chpriSym[channel].setValue(str(priority),2)       # for comment in ftl file

def dcheconCallback(symbol, event):

    # sets up DCHxECON register setting from user-set menu inputs
    global dmacChanReqSrcVal
    global dmacDcheconSym
    global sirqenSym

    channel = 0

    # callback for setting the register DCHxECON
    for s in list(event["id"]):
        if s.isdigit():
            channel = int(s)    # one digit: 0-7

    if((event["id"] == "DMAC_CHAN" + str(channel) + "_ENBL") and (event["value"] == False)):
        # zero out relevant variables since channel is not enabled
        sirqenSym[channel].setValue(0, 2)              # for a comment in ftl code
        dmacDcheconSym[channel].setValue(0, 2)
    else:
        intnum = int(dmacChanReqSrcVal[channel].getValue())  # interrupt number
        if intnum == 0:    # software will force a transfer
            dmacDcheconSym[channel].setValue(0, 2)           # CFORCE will be set later on
            sirqenSym[channel].setValue(0, 2)                # for a comment in ftl code
            dmacChanReqSrcVal[channel].setValue(0, 2)
        else:                    # peripheral will start a transfer
            sirqenSym[channel].setValue(1, 2)
            payload = 0x10                              # SIRQEN=1, enable
            payload |= (intnum & 0xff) << 8  # CHSIRQ, interrupt number to trigger DMA xfer
            dmacDcheconSym[channel].setValue(payload, 2)

################################################################################
#### Component ####
################################################################################

global per_instance
global per_priority
global dmacDchconSym
global dmacChanReqSrcVal
global dmacDchxIntSym
global dmacDcheconSym
global sirqenSym
global chbcieSym
global chpriSym
global dmacInterruptWarn
global dmacPriorityVal
global dmaIrqEnable
global dmaIrqHandler
global dmaVectorNum
global vectorChanMap
global dmaInterruptName

dmaVectorNum = []
dmaChannelNum = []
dmacChannelIds = []
dmacChanAutoSym = []
dmacChanCrcSym = []
dmacDchconSym = []
dmacDcheconSym = []
dmacDchxIntSym = []
dmacChanReqSrcVal = []
sirqenSym = []
chbcieSym = []
dmacInterruptWarn = []
dmacPriority = []
dmacPriorityVal = []
chpriSym = []
dmaIrqEnable = []
dmaIrqHandler = []
vectorChanMap = {}

# interrupts:  needed for the DMA sources possible in menu item
per_instance = {}  # this is an array of key/value pairs
intNode = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()

for ii in range(len(intNode)):

    name = intNode[ii].getAttribute("name")
    index = intNode[ii].getAttribute("index")

    if "irq-name" in intNode[ii].getAttributeList():
        name = str(intNode[ii].getAttribute("irq-name"))

    if "irq-index" in intNode[ii].getAttributeList():
        index = str(intNode[ii].getAttribute("irq-index"))

    per_instance[name] = index

per_instance["Software Trigger"] = 0

# priority value:  needed for the priority level in menu item
per_priority = {}
priNode = dmaValGrp_DCH0CON_CHPRI.getChildren()

for ii in range(len(priNode)):
    argterm = priNode[ii].getAttribute("value")

    if argterm.find('0x') != -1:
        argval = argterm[2:]
    else:
        argval = argterm

    per_priority[priNode[ii].getAttribute("name")] = argval

# DMA_NAME: Needed to map DMA system service APIs to PLIB APIs
dmacSymAPI_Prefix = coreComponent.createStringSymbol("DMA_NAME", None)
dmacSymAPI_Prefix.setDefaultValue("DMAC")
dmacSymAPI_Prefix.setVisible(False)

# number of channels present - read atdf file for parameter
numDMAChans = int(ATDF.getNode("/avr-tools-device-file/devices/device/parameters/param@[name=\"__NUM_DMA_CHANNELS\"]").getAttribute("value"))
dmacNumChans = coreComponent.createIntegerSymbol("NUM_DMA_CHANS", None)
dmacNumChans.setVisible(False)
dmacNumChans.setDefaultValue(numDMAChans)

# DMA_INSTANCE_NAME: Needed to map DMA system service APIs to PLIB APIs
# first register group in module is the name itself
node = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMAC"]').getChildren()
dmacInstanceName = coreComponent.createStringSymbol("DMA_INSTANCE_NAME", None)
dmacInstanceName.setDefaultValue(node[0].getAttribute("name"))
dmacInstanceName.setVisible(False)

# Interrupt-related logic: scan atdf file for all DMA interrupts (there are many of them)
node = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
childIndex = 0

for child in node:

    name = child.getAttribute("name")
    dmaInterruptName = name[:-1]

    if name.startswith("DMA"):  # found a DMA-related interrupt from atdf file - make

        vectorUpdate = "core.DMA" + str(childIndex) + "_INTERRUPT_ENABLE_UPDATE"
        vectorNum = int(child.getAttribute("index"))

        if child.getAttribute("irq-index") != None:
            vectorNum = int(child.getAttribute("irq-index"))
            vectorUpdate = "core.DMA_" + str(childIndex) + "_INTERRUPT_ENABLE_UPDATE"

        dmacInterruptVectorUpdate.append(vectorUpdate)
        statRegIndex, statBitPosn, statMask = _get_statReg_parms(vectorNum)

        SymId = "DMA" + str(childIndex) + "_STATREG_RD"
        dmaStatRegRd = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegRd.setDefaultValue(statRegIndex)
        dmaStatRegRd.setVisible(False)

        SymId = "DMA" + str(childIndex) + "_STATREG_SHIFT"
        dmaStatRegShift = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegShift.setDefaultValue(statBitPosn)
        dmaStatRegShift.setVisible(False)

        SymId = "DMA" + str(childIndex) + "_STATREG_SHIFT_VALUE"
        dmaStatRegShiftVal = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
        dmaStatRegShiftVal.setVisible(False)

        SymId = "DMA" + str(childIndex) + "_STATREG_MASK"
        dmaStatRegMask = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegMask.setDefaultValue(statMask)
        dmaStatRegMask.setVisible(False)

        #used by ftl header file
        dmaChannelNum.append(childIndex)
        SymId = "DMA_" + str(childIndex) + "_CHANNEL_NUMBER"
        dmaChannelNum[childIndex] = coreComponent.createIntegerSymbol(SymId, None)
        dmaChannelNum[childIndex].setDefaultValue(childIndex)
        dmaChannelNum[childIndex].setVisible(False)

        SymId = "DCH" + name[-1] + "INTbits_REG"
        symbol = coreComponent.createStringSymbol(SymId, None)
        symbol.setDefaultValue("DCH" + name[-1] + "INTbits")
        symbol.setVisible(False)

        SymId = "DCH" + name[-1] + "INT_REG"
        symbol = coreComponent.createStringSymbol(SymId, None)
        symbol.setDefaultValue("DCH" + name[-1] + "INT")
        symbol.setVisible(False)

        SymId = "DCH" + name[-1] + "ECONSET_REG"
        symbol = coreComponent.createStringSymbol(SymId, None)
        symbol.setDefaultValue("DCH" + name[-1] + "ECONSET")
        symbol.setVisible(False)

        childIndex += 1

# below parameters facilitate computation of register addresses at runtime

# base address for DMA registers - get from atdf
address = dmacBaseAddress.getAttribute("offset")
SymId = "DMAC_BASE_ADDR"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue(address)
symbol.setVisible(False)

# offset from DMAC base address for channel-level registers
SymId = "DMAC_CHAN_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x60")
symbol.setVisible(False)

# base address for channel-specific registers
SymId = "DMAC_CH_BASE_ADDR"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0xBF811060")
symbol.setVisible(False)

# size each channel takes in registers
SymId = "DMAC_CH_SPACING"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0xC0")
symbol.setVisible(False)

# offset of DCHxCON from channel base address
SymId = "DMAC_CON_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x0")
symbol.setVisible(False)

# offset of DCHxECON from channel base address
SymId = "DMAC_ECON_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x10")
symbol.setVisible(False)

# offset of DCHxINT from channel base address
SymId = "DMAC_INT_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x20")
symbol.setVisible(False)

# offset of DCHxSSA from channel base address
SymId = "DMAC_SSA_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x30")
symbol.setVisible(False)

# offset of DCHxDSA from channel base address
SymId = "DMAC_DSA_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x40")
symbol.setVisible(False)

# offset of DCHxSSIZ from channel base address
SymId = "DMAC_SSIZ_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x50")
symbol.setVisible(False)

# offset of DCHxDSIZ from channel base address
SymId = "DMAC_DSIZ_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x60")
symbol.setVisible(False)

# offset of DCHxCSIZ from channel base address
SymId = "DMAC_CSIZ_OFST"
symbol = coreComponent.createStringSymbol(SymId, None)
symbol.setDefaultValue("0x90")
symbol.setVisible(False)

# for DMA manager to work
dmaManagerSelect = coreComponent.createStringSymbol("DMA_MANAGER_PLUGIN_SELECT", None)
dmaManagerSelect.setVisible(False)
dmaManagerSelect.setDefaultValue("dmac_00735:DMAC00735Model")

# start of menu-related items
dmacMenu = coreComponent.createMenuSymbol("DMAC_MENU", None)
dmacMenu.setLabel("DMA (DMAC)")
dmacMenu.setDescription("DMA (DMAC) Configuration")

# DMA_ENABLE: Needed to conditionally generate API mapping in DMA System service
dmacEnable = coreComponent.createBooleanSymbol("DMA_ENABLE", dmacMenu)
dmacEnable.setLabel("Use DMA Service ?")
dmacEnable.setVisible(False)

# DMA_CHANNEL_COUNT: Needed for DMA system service to generate channel enum
dmacChCount = coreComponent.createIntegerSymbol("DMA_CHANNEL_COUNT", dmacEnable)
dmacChCount.setLabel("DMA (DMAC) Channels Count")
dmacChCount.setDefaultValue(numDMAChans)
dmacChCount.setVisible(False)

dmacFileGen = coreComponent.createBooleanSymbol("DMAC_FILE_GEN", dmacEnable)
dmacFileGen.setLabel("DMA (DMAC) File Generation")
dmacFileGen.setVisible(False)
dmacFileGen.setDependencies(onGlobalEnableLogic, ["DMA_ENABLE"])

dmacHighestCh = coreComponent.createIntegerSymbol("DMAC_HIGHEST_CHANNEL", dmacEnable)
dmacHighestCh.setLabel("DMA (DMAC) Highest Active Channel")
dmacHighestCh.setVisible(False)

# per-channel configurations start here
for dmaChannel in range(0, numDMAChans):
    ###################################### User Menu Controls ##################################################

    # DMA channel enable - menu item
    dmacChanEnSymId = "DMAC_CHAN" + str(dmaChannel) + "_ENBL"
    dmacChannelEnable = coreComponent.createBooleanSymbol(dmacChanEnSymId, dmacMenu)
    dmacChannelEnable.setLabel("Enable Channel " + str(dmaChannel) + " ?")
    dmacChannelIds.append(dmacChanEnSymId)

    # DMA requestor source - menu item.  Name of particular interrupt for src.  SW trigger, or peripheral-triggered.
    dmacChanReqSymId = "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE"
    symbol = coreComponent.createComboSymbol(dmacChanReqSymId, dmacChannelEnable, sorted(per_instance.keys()))
    symbol.setLabel("DMA requestor source")
    symbol.setDefaultValue("Software Trigger")
    symbol.setUseSingleDynamicValue(True)

    # DMA manager will use LOCK symbol to lock the "DMAC_CHCTRLB_TRIGSRC_CH_ + str(dmaChannel)" symbol
    symbol = coreComponent.createBooleanSymbol("DMAC_REQUEST_" + str(dmaChannel) + "_PERID_LOCK", dmacChannelEnable)
    symbol.setLabel("Lock DMA Request")
    symbol.setVisible(False)
    symbol.setUseSingleDynamicValue(True)

    # DMA channel priority
    dmacPrioritySymId = "DMAC_" + str(dmaChannel) + "_PRIORITY"
    symbol = coreComponent.createComboSymbol(dmacPrioritySymId, dmacChannelEnable, sorted(per_priority.keys()))
    symbol.setLabel(dmaValGrp_DCH0CON_CHPRI.getAttribute("caption"))
    symbol.setDefaultValue("0")
    symbol.setUseSingleDynamicValue(True)

    ########################## Derived symbols for registers / register settings ###########################

    # Warning menu item for when DMA is enabled but interrupt has not been set - not visible by default
    dmacInterruptWarn.append(dmaChannel)
    symId = "DMAC_" + str(dmaChannel) + "_IRQ_WARNING"
    dmacInterruptWarn[dmaChannel] = coreComponent.createCommentSymbol(symId, dmacChannelEnable)
    dmacInterruptWarn[dmaChannel].setLabel("*** Warning: enable DMA Channel " + str(dmaChannel) + " Interrupt in Interrupt settings ***")
    dmacInterruptWarn[dmaChannel].setVisible(False)
    dmacInterruptWarn[dmaChannel].setDependencies(updateDMACChannelInterruptData, [dmacInterruptVectorUpdate[dmaChannel], dmacChanEnSymId])

    # derived symbol, used with above:  this will have the interrupt value (which is what is actually needed)
    dmacChanReqSrcVal.append(dmaChannel)
    dmacChanReqSrcValSymId = "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE_VALUE"
    dmacChanReqSrcVal[dmaChannel] = coreComponent.createIntegerSymbol(dmacChanReqSrcValSymId, dmacChannelEnable)
    dmacChanReqSrcVal[dmaChannel].setDefaultValue(0)  # software-generated interrupt
    dmacChanReqSrcVal[dmaChannel].setDependencies(dmacTriggerCalc, ["DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE"])
    dmacChanReqSrcVal[dmaChannel].setVisible(False)

    # derived symbol, used with DMA channel priority
    dmacPriorityVal.append(dmaChannel)
    dmacPriorityValSymId = "DMAC_" + str(dmaChannel) + "_PRIORITY_VALUE"
    dmacPriorityVal[dmaChannel] = coreComponent.createIntegerSymbol(dmacPriorityValSymId, dmacChannelEnable)
    dmacPriorityVal[dmaChannel].setDefaultValue(0)
    dmacPriorityVal[dmaChannel].setDependencies(dmacPriorityCalc, ["DMAC_" + str(dmaChannel) + "_PRIORITY"])
    dmacPriorityVal[dmaChannel].setVisible(False)

    # Start of channel-level register values to calculate for ftl to use
    # DCHxCON register value - set by python callback function
    dmacDchconSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_CON_VALUE"
    dmacDchconSym[dmaChannel] = coreComponent.createHexSymbol(symId, dmacChannelEnable)
    dmacDchconSym[dmaChannel].setVisible(False)
    dmacDchconSym[dmaChannel].setDefaultValue(0)
    dmacDchconSym[dmaChannel].setDependencies(dchconCallback, [dmacChanEnSymId, dmacPriorityValSymId])

    # DCHxECON register value - set by python callback function
    dmacDcheconSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_ECON_VALUE"
    dmacDcheconSym[dmaChannel] = coreComponent.createHexSymbol(symId, dmacChannelEnable)
    dmacDcheconSym[dmaChannel].setVisible(False)
    dmacDcheconSym[dmaChannel].setDefaultValue(0x00000000)
    dmacDcheconSym[dmaChannel].setDependencies(dcheconCallback, [dmacChanEnSymId, dmacChanReqSrcValSymId])

    # DCHxECON<SIRQEN> field value - set by python callback function
    sirqenSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_ECON_SIRQEN_VALUE"
    sirqenSym[dmaChannel] = coreComponent.createIntegerSymbol(symId, None)
    sirqenSym[dmaChannel].setDefaultValue(0)
    sirqenSym[dmaChannel].setVisible(False)

    chpriSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_CON_CHPRI_VALUE"
    chpriSym[dmaChannel] = coreComponent.createStringSymbol(symId, None)
    chpriSym[dmaChannel].setDefaultValue("0")
    chpriSym[dmaChannel].setVisible(False)

    # DCHxCON register name - used in ftl file to refer to registers set at initialization time
    SymId = "DCH_" + str(dmaChannel) + "_CONREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH" + str(dmaChannel) + "CONbits")
    symbol.setVisible(False)

    # DCHxECON register name - used in ftl file
    SymId = "DCH_" + str(dmaChannel) + "_ECONREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH" + str(dmaChannel) + "ECONbits")
    symbol.setVisible(False)

    # DCHxINT register name - used in ftl file
    SymId = "DCH_" + str(dmaChannel) + "_INTREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH" + str(dmaChannel) + "INTbits")
    symbol.setVisible(False)

    # DCHxSSA - populated by API, not python
    # DCHxDSA - populated by API, not python
    # DCHxSSIZ - populated by API, not python
    # DCHxDSIZ - populated by API, not python
    # DCHxSPTR - populated by API, not python
    # DCHxDPTR - populated by API, not python
    # DCHxDAT - feature not used (pattern matching)

# end of per-channel configurations

dmacEnable.setDependencies(dmacGlobalLogic, dmacChannelIds)
dmacHighestCh.setDependencies(dmacGlobalLogic, dmacChannelIds)

# DMACON register value - used in ftl
SymId = "DMACON_REG_VALUE"
symbol = coreComponent.createHexSymbol(SymId, None)
symbol.setDefaultValue(0x8000) # if any channels are enabled, will always set ON=1
symbol.setVisible(False)

#Interface for Peripheral clients
for per in per_instance.keys():

    name = per

    if "TX" in per:
        name = name.replace('TX', 'Transmit')
    elif "RX" in per:
        name = name.replace('RX', 'Receive')

    dmacChannelNeeded = coreComponent.createBooleanSymbol("DMA_CH_NEEDED_FOR_" + str(name), dmacMenu)
    dmacChannelNeeded.setLabel("Local DMA_CH_NEEDED_FOR_" + str(name))
    dmacChannelNeeded.setVisible(False)
    peridValueListSymbols.append("DMA_CH_NEEDED_FOR_" + str(name))

    dmacChannel = coreComponent.createIntegerSymbol("DMA_CH_FOR_" + str(name), dmacMenu)
    dmacChannel.setLabel("Local DMA_CH_FOR_" + str(name))
    dmacChannel.setDefaultValue(-1)
    dmacChannel.setVisible(False)

dmacPERIDChannelUpdate = coreComponent.createBooleanSymbol("DMA_CHANNEL_ALLOC", dmacMenu)
dmacPERIDChannelUpdate.setLabel("Local dmacChannelAllocLogic")
dmacPERIDChannelUpdate.setVisible(False)
dmacPERIDChannelUpdate.setDependencies(dmacChannelAllocLogic, peridValueListSymbols)

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmacHeaderFile = coreComponent.createFileSymbol("DMAC_HEADER", None)
dmacHeaderFile.setSourcePath("../peripheral/dmac_00735/templates/plib_dmac.h.ftl")
dmacHeaderFile.setOutputName("plib_" + dmacInstanceName.getValue().lower() + ".h")
dmacHeaderFile.setDestPath("/peripheral/dmac/")
dmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacHeaderFile.setType("HEADER")
dmacHeaderFile.setMarkup(True)
dmacHeaderFile.setEnabled(False)

# Source File
dmacSourceFile = coreComponent.createFileSymbol("DMAC_SOURCE", None)
dmacSourceFile.setSourcePath("../peripheral/dmac_00735/templates/plib_dmac.c.ftl")
dmacSourceFile.setOutputName("plib_" + dmacInstanceName.getValue().lower() + ".c")
dmacSourceFile.setDestPath("/peripheral/dmac/")
dmacSourceFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacSourceFile.setType("SOURCE")
dmacSourceFile.setMarkup(True)
dmacSourceFile.setEnabled(False)

#System Initialization
dmacSystemInitFile = coreComponent.createFileSymbol("DMAC_SYS_INIT", None)
dmacSystemInitFile.setType("STRING")
dmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmacSystemInitFile.setSourcePath("../peripheral/dmac_00735/templates/system/initialization.c.ftl")
dmacSystemInitFile.setMarkup(True)
dmacSystemInitFile.setEnabled(False)

#System Definition
dmacSystemDefFile = coreComponent.createFileSymbol("DMAC_SYS_DEF", None)
dmacSystemDefFile.setType("STRING")
dmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmacSystemDefFile.setSourcePath("../peripheral/dmac_00735/templates/system/definitions.h.ftl")
dmacSystemDefFile.setMarkup(True)
dmacSystemDefFile.setEnabled(False)
