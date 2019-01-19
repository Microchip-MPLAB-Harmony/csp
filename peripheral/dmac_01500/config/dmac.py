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

from os.path import join
from xml.etree import ElementTree

Log.writeInfoMessage("Loading DMA Manager for " + Variables.get("__PROCESSOR"))

global dmaBitfield_DCH0CON_CHPRI
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
    if(maskval.find('0x')!=-1):
        value = maskval[2:]
    else:
        value = maskval
    for ii in range(0,31):
        if(int(value) & (1<<ii)):
            break
    return ii
    
global _find_channel
def _find_channel(stringval):
    nullVal = "X"
    for s in list(stringval):
        if s.isdigit():
            return s
    return nullVal
    
def dmacTriggerCalc(symbol, event):
    global per_instance
    
    # the "chan enable" boolean is for in/visible setting
    if(event["id"].find("DMAC_CHAN") != -1):
        menu.setVisible(event["value"])
        return
    else:  # get the value for the given key, namely, the interrupt number for this key name
        symbol.clearValue()
        symbol.setValue(int(per_instance.get(event["value"])), 2)

def dmacPriorityCalc(symbol, event):
    global per_priority
    
    # the "chan enable" boolean is for in/visible setting
    if(event["id"].find("DMAC_CHAN") != -1):
        menu.setVisible(event["value"])
        return
    else:  # get the value for the given key, namely, the priority number for this key name
        symbol.clearValue()
        symbol.setValue(int(per_priority.get(event["value"])), 2)
        
def channelCallback(menu, event):
    # the "chan enable" boolean is for in/visible setting
    if(event["id"].find("DMAC_CHAN") != -1):
        menu.setVisible(event["value"])
        return # nothing more to do in this function call for this event id

def checkIntSetting(menu, event):
    # Sees if the user has not enabled the particular DMAC interrupt when enabling this channel.
    # If so, will display a warning message.
    global dmacInterruptWarn
    
    # the "chan enable" boolean is for in/visible setting
    chan = _find_channel(event["id"])
    if(event["id"].find("_ENBL") == -1):
        menu.setVisible(event["value"])
        return # nothing more to do in this function call for this event id    
    else:
        chan = _find_channel(event["id"])
        targetSymId = "DMA"+chan+"_INTERRUPT_ENABLE"
        int_enbl = Database.getSymbolValue("core", targetSymId)
        if((int_enbl==False) and (event["value"]==True)):
            dmacInterruptWarn[int(chan)].setVisible(True)
        else:
            dmacInterruptWarn[int(chan)].setVisible(False)
    
def _get_enblReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IECx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        bitMask = hex(1<<bitPosn)
        regName = "IEC"+str(index)
    return regName, str(bitPosn), str(bitMask)
    
def _get_statReg_parms(vectorNumber):
    # This takes in vector index for interrupt, and returns the IFSx register name as well as 
    # mask and bit location within it for given interrupt
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 32.0
        index = int(temp)
        bit = float(temp%1)
        bitPosn = int(32.0*bit)
        bitMask = hex(1<<bitPosn)
        regName = "IFS"+str(index)
    return regName, str(bitPosn), str(bitMask)
    
def _get_sub_priority_parms(vectorNumber):
    # This returns the IPCx register name, priority bit shift, priority mask, subpriority bit shift, 
    # and subpriority bitmask for input vector number
    if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
        (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
        temp = float(vectorNumber) / 4.0
        index = int(temp)
        subPrioBit = 8*(vectorNumber & 0x3)
        subPrioMask = 0x3  # always 2 bits
        prioMask = 0x7
        prioBit = subPrioBit + 2
        regName = "IPC"+str(index)
    return regName, str(prioBit), str(prioMask), str(subPrioBit), str(subPrioMask)
    
def dchconCallback(symbol, event):
    # callback for setting the register DCHxCON
    global chenSym
    global dmaBitfield_DCH0CON_CHPRI
    global dmacPriorityVal
    global _get_position
    global chpriSym

    channel = 0
    for s in list(event["id"]):
        if s.isdigit():
            channel = int(s)
    if((event["id"] == "DMAC_CHAN"+str(channel)+"_ENBL") and (event["value"] == False)):  
        dmacDchconSym[channel].setValue(0,2)  # for not enabled channel, clear register
        chpriSym[channel].setValue("0",2)       # for comment in ftl file
        chenSym[channel].setValue("0",2)      # for comment in ftl file
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
    
    if((event["id"] == "DMAC_CHAN"+str(channel)+"_ENBL") and (event["value"] == False)):
        # zero out relevant variables since channel is not enabled
        sirqenSym[channel].setValue(0,2)              # for a comment in ftl code
        dmacDcheconSym[channel].setValue(0,2)
    else:
        intnum = int(dmacChanReqSrcVal[channel].getValue())  # interrupt number
        if(intnum == 0):    # software will force a transfer 
            dmacDcheconSym[channel].setValue(0,2)           # CFORCE will be set later on
            sirqenSym[channel].setValue(0,2)                # for a comment in ftl code
            dmacChanReqSrcVal[channel].setValue(0,2)
        else:                    # peripheral will start a transfer
            sirqenSym[channel].setValue(1,2)
            payload = 0x10                              # SIRQEN=1, enable 
            payload |= (intnum & 0xff) << 8  # CHSIRQ, interrupt number to trigger DMA xfer
            dmacDcheconSym[channel].setValue(payload,2)

def dchintCallback(symbol, event):
    # sets up DCHxINT register based on user-input menu settings
    global dmacDchxIntSym
    global chbcieSym
    
    channel = 0
    # callback for setting the register DCHxECON
    for s in list(event["id"]):
        if s.isdigit():
            channel = int(s)    # one digit: 0-7
            
    if((event["id"] == "DMAC_CHAN"+str(channel)+"_ENBL") and (event["value"]==False)):
        # disable channel:  do not enable any DMA interrupts
        chbcieSym[channel].setValue("0",2)              # for a comment in ftl code
        dmacDchxIntSym[channel].setValue(0, 2)
    else:   
        # always enable block transfer complete interrupts, for DMA to indicate when done
        chbcieSym[channel].setValue("1",2)                # for a comment in ftl code
        payload = 0x80000       # CHBCIE=1, block transfer complete interrupt enable
        dmacDchxIntSym[channel].setValue(payload, 2)

global _get_channel_from_nvic_name
def _get_channel_from_nvic_name(eventId):
    # due to naming symbols in interrupt side according to a predetermined format,
    # the channel number needs to be obtained from it.  Naming format is of this type:
    #     NVIC_134_0_HANDLER
    # Need to extract the vector number (134 here), and map that to channel value.
    global vectorChanMap  # set in main part of this python file
    vector = ""
    for s in list(eventId[5:]):  # skip the prefix "NVIC_".  Want the number right after it.
        if(s != "_"):
            vector += s
        else:
            break  # got the numerical value between the 1st two "_".  No more to get from event id.
    return int(vectorChanMap[vector])  # convert to channel number, and send back
    
def updatePrio(menu, event):
    # updates interrupt priority in DMA, when updated
    global dmaIrqPriority
    global _get_channel_from_nvic_name
    channel = _get_channel_from_nvic_name(event["id"])
    dmaIrqPriority[channel].setValue(str(event["value"]),2)

def updateEnbl(menu, event):
    # updates interrupt enable status in DMA, when updated
    global dmaIrqEnable
    global _get_channel_from_nvic_name
    channel = _get_channel_from_nvic_name(event["id"])
    dmaIrqEnable[channel].setValue(int(event["value"]),2)
    
def updateHandler(menu, event):
    # updates interrupt handler name in DMA, when updated
    global dmaIrqHandler
    global _get_channel_from_nvic_name
    channel = _get_channel_from_nvic_name(event["id"])
    dmaIrqHandler[channel].setValue(str(event["value"]),2)    
    
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
global chenSym
global chpriSym
global dmacInterruptWarn
global dmacPriorityVal
global dmaIrqPriority
global dmaIrqEnable
global dmaIrqHandler
global dmaVectorNum
global vectorChanMap
dmaVectorNum = []
dmaChannelNum = []
dmacChanEnblSym = []
dmacChanAutoSym = []
dmacChanCrcSym = []
dmacDchconSym = []
dmacDcheconSym = []
dmacDchxIntSym = []
dmacChanReqSrcVal = []
sirqenSym = []
chbcieSym = []
chenSym = []
dmacInterruptWarn = []
dmacPriority = []
dmacPriorityVal = []
chpriSym = []
dmaIrqPriority = []
dmaIrqEnable = []
dmaIrqHandler = []
vectorChanMap = {}

# interrupts:  needed for the DMA sources possible in menu item
per_instance = {}  # this is an array of key/value pairs
intNode = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
for ii in range(0,len(intNode)):
    per_instance[intNode[ii].getAttribute("name")] = intNode[ii].getAttribute("index")
per_instance["Software Trigger"] = 0

# priority value:  needed for the priority level in menu item
per_priority = {}
priNode = dmaValGrp_DCH0CON_CHPRI.getChildren()
for ii in range(0,len(priNode)):
    argterm = priNode[ii].getAttribute("value")
    if(argterm.find('0x') != -1):
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
    if(name[:3]=="DMA"):  # found a DMA-related interrupt from atdf file - make 
        vectorNum = int(child.getAttribute("index"))
        enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(vectorNum)
        statRegName, statBitPosn, statMask = _get_statReg_parms(vectorNum)
        prioRegName, prioShift, prioMask, subprioShift, subprioMask = _get_sub_priority_parms(vectorNum)        
        SymId = name+"_PRIOREG_WRT"
        dmaPrioRegWrt = coreComponent.createStringSymbol(SymId, None)
        dmaPrioRegWrt.setDefaultValue(prioRegName+"SET")
        dmaPrioRegWrt.setVisible(False)
        
        SymId = name + "_PRIOREG_SHIFT"
        dmaPrioRegShift = coreComponent.createStringSymbol(SymId, None)
        dmaPrioRegShift.setDefaultValue(prioShift)
        dmaPrioRegShift.setVisible(False)
        
        SymId = name + "_SUBPRIOREG_SHIFT"
        dmaSubPrioRegShift = coreComponent.createStringSymbol(SymId, None)
        dmaSubPrioRegShift.setDefaultValue(subprioShift)
        dmaSubPrioRegShift.setVisible(False)
        
        SymId = name + "_ENBLREG_RD"
        dmaEnblRegWrt = coreComponent.createStringSymbol(SymId, None)
        dmaEnblRegWrt.setDefaultValue(enblRegName)
        dmaEnblRegWrt.setVisible(False)
        
        SymId = name + "_ENBLREG_WRT"
        dmaEnblRegWrt = coreComponent.createStringSymbol(SymId, None)
        dmaEnblRegWrt.setDefaultValue(enblRegName+"SET")
        dmaEnblRegWrt.setVisible(False)
        
        SymId = name + "_ENBLREG_CLR"
        dmaEnblRegClr = coreComponent.createStringSymbol(SymId, None)
        dmaEnblRegClr.setDefaultValue(enblRegName+"CLR")
        dmaEnblRegClr.setVisible(False) 
        
        SymId = name + "_ENBLREG_SHIFT"
        dmaEnblRegShift = coreComponent.createStringSymbol(SymId, None)
        dmaEnblRegShift.setDefaultValue(enblBitPosn)
        dmaEnblRegShift.setVisible(False)
        
        SymId = name + "_ENBLREG_ENABLE_VALUE"
        dmaEnblRegVal = coreComponent.createStringSymbol(SymId, None)
        dmaEnblRegVal.setDefaultValue(str(hex(1<<int(enblBitPosn))))
        dmaEnblRegVal.setVisible(False)
        
        SymId = name + "_STATREG_CLR"
        dmaStatRegClr = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegClr.setDefaultValue(statRegName+"CLR")
        dmaStatRegClr.setVisible(False)
        
        SymId = name + "_STATREG_RD"
        dmaStatRegRd = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegRd.setDefaultValue(statRegName)
        dmaStatRegRd.setVisible(False)
        
        SymId = name + "_STATREG_SHIFT"
        dmaStatRegShift = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegShift.setDefaultValue(statBitPosn)
        dmaStatRegShift.setVisible(False)
        
        SymId = name + "_STATREG_SHIFT_VALUE"
        dmaStatRegShiftVal = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegShiftVal.setDefaultValue(str(hex(1<<int(statBitPosn))))
        dmaStatRegShiftVal.setVisible(False)
        
        SymId = name + "_STATREG_MASK"
        dmaStatRegMask = coreComponent.createStringSymbol(SymId, None)
        dmaStatRegMask.setDefaultValue(statMask)
        dmaStatRegMask.setVisible(False)
        
        #used by ftl header file
        dmaVectorNum.append(childIndex)
        SymId = "DMA_" + str(childIndex) + "_VECTOR_NUMBER"
        dmaVectorNum[childIndex] = coreComponent.createIntegerSymbol(SymId, None)
        dmaVectorNum[childIndex].setDefaultValue(vectorNum)
        dmaVectorNum[childIndex].setVisible(False)
        vectorChanMap[str(vectorNum)] = str(childIndex)
        
        #used by ftl header file
        dmaChannelNum.append(childIndex)
        SymId = "DMA_" + str(childIndex) + "_CHANNEL_NUMBER"
        dmaChannelNum[childIndex] = coreComponent.createIntegerSymbol(SymId, None)
        dmaChannelNum[childIndex].setDefaultValue(childIndex)
        dmaChannelNum[childIndex].setVisible(False)
        
        if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
            (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
            # this name could be different for different families - this isn't from the datasheet
            SymId = "DCH"+name[-1]+"INTbits_REG"
            symbol = coreComponent.createStringSymbol(SymId, None)
            symbol.setDefaultValue("DCH"+name[-1]+"INTbits")
            symbol.setVisible(False)
        
        SymId = "DCH"+name[-1]+"INT_REG"
        symbol = coreComponent.createStringSymbol(SymId, None)
        symbol.setDefaultValue("DCH"+name[-1]+"INT")
        symbol.setVisible(False)
        
        SymId = "DCH"+name[-1]+"ECONSET_REG"
        symbol = coreComponent.createStringSymbol(SymId, None)
        symbol.setDefaultValue("DCH"+name[-1]+"ECONSET")
        symbol.setVisible(False)
        
        childIndex += 1
        
# below parameters facilitate computation of register addresses at runtime
if( ("PIC32MZ" in Variables.get("__PROCESSOR")) and 
    (("EF" in Variables.get("__PROCESSOR"))) or (("DA" in Variables.get("__PROCESSOR"))) ):
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
dmaManagerSelect.setDefaultValue("dmac_01500:DMAC01500Model")    
    
# start of menu-related items
dmacMenu = coreComponent.createMenuSymbol("DMAC_MENU", None)
dmacMenu.setLabel("DMA (DMAC)")
dmacMenu.setDescription("DMA (DMAC) Configuration")

# per-channel configurations start here
for dmaChannel in range(0,numDMAChans):
    ###################################### User Menu Controls ##################################################
    # DMA channel enable - menu item
    dmacChanEnSymId = "DMAC_CHAN"+ str(dmaChannel)+"_ENBL"
    symbol = coreComponent.createBooleanSymbol(dmacChanEnSymId, dmacMenu)
    symbol.setLabel("Enable channel "+str(dmaChannel)+"?")
    symbol.setVisible(True)
    symbol.setDefaultValue(False)
    symbol.setDependencies(checkIntSetting, [dmacChanEnSymId])
    dmacChanEnblSym.append(symbol)
    
    # DMA requestor source - menu item.  Name of particular interrupt for src.  SW trigger, or peripheral-triggered.
    dmacChanReqSymId = "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE"
    symbol = coreComponent.createComboSymbol(dmacChanReqSymId, dmacChanEnblSym[dmaChannel], sorted(per_instance.keys()))
    symbol.setVisible(True)
    symbol.setLabel("DMA requestor source")
    symbol.setDefaultValue("Software Trigger")
    symbol.setDependencies(channelCallback, [dmacChanEnSymId])
    symbol.setUseSingleDynamicValue(True)
    
    # DMA channel priority
    dmacPrioritySymId = "DMAC_" + str(dmaChannel) + "_PRIORITY"
    symbol = coreComponent.createComboSymbol(dmacPrioritySymId, dmacChanEnblSym[dmaChannel], sorted(per_priority.keys()))
    symbol.setVisible(True)
    symbol.setLabel(dmaValGrp_DCH0CON_CHPRI.getAttribute("caption"))
    symbol.setDefaultValue("0")
    symbol.setDependencies(channelCallback,[dmacChanEnSymId])
    symbol.setUseSingleDynamicValue(True)

    
    ########################## Derived symbols for registers / register settings ###########################
    # Warning menu item for when DMA is enabled but interrupt has not been set - not visible by default
    dmacInterruptWarn.append(dmaChannel)
    symId = "DMAC_" + str(dmaChannel) + "_IRQ_WARNING"
    dmacInterruptWarn[dmaChannel] = coreComponent.createMenuSymbol(symId,dmacChanEnblSym[dmaChannel])
    dmacInterruptWarn[dmaChannel].setLabel("*** Warning: enable DMA Channel "+str(dmaChannel)+" Interrupt in PIC32MZ Interrupt settings ***")
    dmacInterruptWarn[dmaChannel].setVisible(False)
    
    # derived symbol, used with above:  this will have the interrupt value (which is what is actually needed)
    dmacChanReqSrcVal.append(dmaChannel)
    dmacChanReqSrcValSymId = "DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE_VALUE"
    dmacChanReqSrcVal[dmaChannel] = coreComponent.createIntegerSymbol(dmacChanReqSrcValSymId, dmacChanEnblSym[dmaChannel])
    dmacChanReqSrcVal[dmaChannel].setDefaultValue(0)  # software-generated interrupt
    dmacChanReqSrcVal[dmaChannel].setDependencies(dmacTriggerCalc, ["DMAC_REQUEST_" + str(dmaChannel) + "_SOURCE"])
    dmacChanReqSrcVal[dmaChannel].setVisible(False)

    # derived symbol, used with DMA channel priority
    dmacPriorityVal.append(dmaChannel)
    dmacPriorityValSymId = "DMAC_" + str(dmaChannel) + "_PRIORITY_VALUE"
    dmacPriorityVal[dmaChannel] = coreComponent.createIntegerSymbol(dmacPriorityValSymId, dmacChanEnblSym[dmaChannel])
    dmacPriorityVal[dmaChannel].setDefaultValue(0)
    dmacPriorityVal[dmaChannel].setDependencies(dmacPriorityCalc, ["DMAC_" + str(dmaChannel) + "_PRIORITY"])
    dmacPriorityVal[dmaChannel].setVisible(False)
    
    # Start of channel-level register values to calculate for ftl to use
    # DCHxCON register value - set by python callback function
    dmacDchconSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_CON_VALUE"
    dmacDchconSym[dmaChannel] = coreComponent.createHexSymbol(symId, dmacChanEnblSym[dmaChannel])
    dmacDchconSym[dmaChannel].setVisible(False)
    dmacDchconSym[dmaChannel].setDefaultValue(0)
    dmacDchconSym[dmaChannel].setDependencies(dchconCallback, [dmacChanEnSymId, dmacPriorityValSymId])
    
    # DCHxECON register value - set by python callback function
    dmacDcheconSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_ECON_VALUE"
    dmacDcheconSym[dmaChannel] = coreComponent.createHexSymbol(symId, dmacChanEnblSym[dmaChannel])
    dmacDcheconSym[dmaChannel].setVisible(False)
    dmacDcheconSym[dmaChannel].setDefaultValue(0x00000000)
    dmacDcheconSym[dmaChannel].setDependencies(dcheconCallback, [dmacChanEnSymId, dmacChanReqSrcValSymId])
    
    # DCHxINT register value - set by python callback function
    dmacDchxIntSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_INT_VALUE"
    dmacDchxIntSym[dmaChannel] = coreComponent.createHexSymbol(symId, dmacChanEnblSym[dmaChannel])
    dmacDchxIntSym[dmaChannel].setVisible(False)
    dmacDchxIntSym[dmaChannel].setDefaultValue(0)
    dmacDchxIntSym[dmaChannel].setDependencies(dchintCallback, [dmacChanEnSymId, dmacChanReqSrcValSymId])    

    # DCHxECON<SIRQEN> field value - set by python callback function
    sirqenSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_ECON_SIRQEN_VALUE"
    sirqenSym[dmaChannel] = coreComponent.createIntegerSymbol(symId, None)
    sirqenSym[dmaChannel].setDefaultValue(0)
    sirqenSym[dmaChannel].setVisible(False)    
    
    # DCHxINT<CHBCIE> field value - set by python callback function
    chbcieSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_INT_CHBCIE_VALUE"
    chbcieSym[dmaChannel] = coreComponent.createStringSymbol(symId, None)
    chbcieSym[dmaChannel].setDefaultValue("0")
    chbcieSym[dmaChannel].setVisible(False) 

    # DCHxCON<CHEN> field value - set by python callback function
    chenSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_CON_CHEN_VALUE"
    chenSym[dmaChannel] = coreComponent.createStringSymbol(symId, None)
    chenSym[dmaChannel].setDefaultValue("0")
    chenSym[dmaChannel].setVisible(False)
    
    chpriSym.append(dmaChannel)
    symId = "DCH" + str(dmaChannel) + "_CON_CHPRI_VALUE"
    chpriSym[dmaChannel] = coreComponent.createStringSymbol(symId, None)
    chpriSym[dmaChannel].setDefaultValue("0")
    chpriSym[dmaChannel].setVisible(False)
    
    # DCHxCON register name - used in ftl file to refer to registers set at initialization time
    SymId = "DCH_"+str(dmaChannel)+"_CONREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH"+str(dmaChannel)+"CONbits")
    symbol.setVisible(False)
    
    # DCHxECON register name - used in ftl file
    SymId = "DCH_"+str(dmaChannel)+"_ECONREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH"+str(dmaChannel)+"ECONbits")
    symbol.setVisible(False)
    
    # DCHxINT register name - used in ftl file
    SymId = "DCH_"+str(dmaChannel)+"_INTREG"
    symbol = coreComponent.createStringSymbol(SymId, None)
    symbol.setDefaultValue("DCH"+str(dmaChannel)+"INTbits")
    symbol.setVisible(False)
    
    # DCHxSSA - populated by API, not python
    # DCHxDSA - populated by API, not python    
    # DCHxSSIZ - populated by API, not python
    # DCHxDSIZ - populated by API, not python
    # DCHxSPTR - populated by API, not python
    # DCHxDPTR - populated by API, not python
    # DCHxDAT - feature not used (pattern matching)
    
    # interrupt priority:  for use in ftl file
    dmaIrqPriority.append(dmaChannel)
    dmaIrqPriority[dmaChannel] = coreComponent.createStringSymbol("DMA_"+str(dmaChannel)+"_IRQ_PRIORITY", None)
    targetSym = "NVIC_" + str(dmaVectorNum[dmaChannel].getValue()) + "_0_PRIORITY"
    val = Database.getSymbolValue("core",targetSym)
    dmaIrqPriority[dmaChannel].setDefaultValue(val)
    dmaIrqPriority[dmaChannel].setDependencies(updatePrio,["core." + targetSym])
    dmaIrqPriority[dmaChannel].setVisible(False)
    
    # interrupt enable:  for use in ftl file
    dmaIrqEnable.append(dmaChannel)
    dmaIrqEnable[dmaChannel] = coreComponent.createBooleanSymbol("DMA_"+str(dmaChannel)+"_INTERRUPT_ENABLE", None)
    targetSym = "NVIC_" + str(dmaVectorNum[dmaChannel].getValue()) + "_0_ENABLE"
    val = Database.getSymbolValue("core",targetSym)
    dmaIrqEnable[dmaChannel].setDefaultValue(val)
    dmaIrqEnable[dmaChannel].setDependencies(updateEnbl,["core." + targetSym])
    dmaIrqEnable[dmaChannel].setVisible(False)
    
    # handler name:  for use in ftl file
    dmaIrqHandler.append(dmaChannel)
    dmaIrqHandler[dmaChannel] = coreComponent.createStringSymbol("DMA_"+str(dmaChannel)+"_IRQ_HANDLER", None)
    targetSym = "NVIC_" + str(dmaVectorNum[dmaChannel].getValue()) + "_0_HANDLER"
    val = Database.getSymbolValue("core",targetSym)
    dmaIrqHandler[dmaChannel].setDefaultValue(val)
    dmaIrqHandler[dmaChannel].setDependencies(updateHandler,["core." + targetSym])
    dmaIrqHandler[dmaChannel].setVisible(False)
# end of per-channel configurations

# DMACON register value - used in ftl
SymId = "DMACON_REG_VALUE"
symbol = coreComponent.createHexSymbol(SymId, None)
symbol.setDefaultValue(0x8000) # if any channels are enabled, will always set ON=1
symbol.setVisible(False)

# DCHxECON<SIRQEN> bitshift from lsb
symId = "SIRQEN_SHIFT"
shiftVal = _get_position(dmaReg_DMAECON_SIRQEN.getAttribute('mask'))
symbol = coreComponent.createIntegerSymbol(symId, None)
symbol.setDefaultValue(shiftVal)
symbol.setVisible(False) 

   
    
###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

configName = Variables.get("__CONFIGURATION_NAME")

# Instance Header File
dmacHeaderFile = coreComponent.createFileSymbol("DMAC_HEADER", None)
dmacHeaderFile.setSourcePath("../peripheral/dmac_01500/templates/plib_dmac.h.ftl")
dmacHeaderFile.setOutputName("plib_"+dmacInstanceName.getValue().lower()+".h")
dmacHeaderFile.setDestPath("/peripheral/dmac/")
dmacHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacHeaderFile.setType("HEADER")
dmacHeaderFile.setMarkup(True)
dmacHeaderFile.setEnabled(True)

# Source File
dmacSourceFile = coreComponent.createFileSymbol("DMAC_SOURCE", None)
dmacSourceFile.setSourcePath("../peripheral/dmac_01500/templates/plib_dmac.c.ftl")
dmacSourceFile.setOutputName("plib_"+dmacInstanceName.getValue().lower()+".c")
dmacSourceFile.setDestPath("/peripheral/dmac/")
dmacSourceFile.setProjectPath("config/" + configName + "/peripheral/dmac/")
dmacSourceFile.setType("SOURCE")
dmacSourceFile.setMarkup(True)
dmacSourceFile.setEnabled(True)

#System Initialization
dmacSystemInitFile = coreComponent.createFileSymbol("DMAC_SYS_INIT", None)
dmacSystemInitFile.setType("STRING")
dmacSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmacSystemInitFile.setSourcePath("../peripheral/dmac_01500/templates/system/initialization.c.ftl")
dmacSystemInitFile.setMarkup(True)
dmacSystemInitFile.setEnabled(True)

#System Definition
dmacSystemDefFile = coreComponent.createFileSymbol("DMAC_SYS_DEF", None)
dmacSystemDefFile.setType("STRING")
dmacSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmacSystemDefFile.setSourcePath("../peripheral/dmac_01500/templates/system/definitions.h.ftl")
dmacSystemDefFile.setMarkup(True)
dmacSystemDefFile.setEnabled(True)
