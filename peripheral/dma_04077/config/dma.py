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
 
from collections import OrderedDict

global activeChList
activeChList = []

global dmaRegDefaults
dmaRegDefaults = OrderedDict()

global isIntEnabled
isIntEnabled = False

################################################################################
#### ATDF Helper Functions  ####
################################################################################
global getModuleRegisterData
def getModuleRegisterData(moduleName,registerGroup,register):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
    registerNode = ATDF.getNode(atdfPath)
    if(registerNode != None):
        return registerNode.getChildren()
    return None

global getDefaultVal
def getDefaultVal(initVal, mask):
    value = int(initVal, 16) & int(mask, 16)
    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1
        value = value >> 1
    return value 

global getSettingBitDefaultValue
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
     
global getRegisterDefaultValue
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

global getValueGroupName
def getValueGroupName(moduleName,registerGroup,register,bitfield):
    bitNode = getBitField(moduleName,registerGroup,register,bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

global getValueGroup
def getValueGroup(moduleName,valueGroupName):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/value-group@[name="'+ valueGroupName + '"]'
    return ATDF.getNode(atdfPath)

global getBitField
def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

global getBitfieldOptionList
def getBitfieldOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
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
            optionList.append(dict)
    return optionList 

global getKeyValuePairBasedonValue
def getKeyValuePairBasedonValue(value,keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["value"] == str(value):
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find value in dictionary") # should never get here
    return ""      

global addKeystoKeyValueSymbol
def addKeystoKeyValueSymbol(bitSymbol,bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey( ii['key'],ii['value'], ii['desc'] )  

global createKeyValueSetSymbol
def createKeyValueSetSymbol(component,moduleName,symbolKey,registerGroup,register,bitfield,menu): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):      
            optionList = getBitfieldOptionList(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, menu)
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue = getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp           

global getParameterValue
def getParameterValue(moduleName, instanceName, paramName):
    atdfPath = '/avr-tools-device-file/devices/device/peripherals/module@[name="' + moduleName + '"]/instance@[name="' + instanceName + '"]/parameters/param@[name="' + paramName + '"]'
    paramNode = ATDF.getNode(atdfPath)
    if paramNode is not None:
        return paramNode.getAttribute("value")
    return None
                   
global getVectorIndex        
def getVectorIndex(interruptName):
    interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()
    vector_index = "-1"
    for param in interruptsChildren:
        name = str(param.getAttribute("name"))
        if interruptName == name:
            vector_index = str(param.getAttribute("index"))
            break

    return vector_index
        
################################################################################
#### Symbol Constants ####
################################################################################
global DMA_MENU
DMA_MENU = "DMA_MENU"

global DMA
DMA ="DMA"

global DMALOW
DMALOW = "DMALOW"

global DMAHIGH
DMAHIGH = "DMAHIGH"

global NUM_CHANNEL
NUM_CHANNEL = "num_channels"

global DMA_ENABLE
DMA_ENABLE = "dmaEnable"

global LOW_ADDR_LIMIT
LOW_ADDR_LIMIT = "dmaLowAddressLimit"

global HIGH_ADDR_LIMIT
HIGH_ADDR_LIMIT = "dmaHighAddressLimit"

global ENABLE_CH
ENABLE_CH = "DMA{}_CH__CHEN"

global CH_RELOAD_CNT
CH_RELOAD_CNT = "DMA{}_CH__RELOADC"

global CH_RELOAD_DST
CH_RELOAD_DST = "DMA{}_CH__RELOADD"

global CH_RELOAD_SRC
CH_RELOAD_SRC = "DMA{}_CH__RELOADS"

global CH_ENABLE_INT
CH_ENABLE_INT = "DMA{}_CH__DONEEN"

global CH_ENABLE_INT_CMNT
CH_ENABLE_INT_CMNT = "dmaCh{}IntEnableCmnt"

global CH_ENABLE_HALF_INT
CH_ENABLE_HALF_INT = "DMA{}_CH__HALFEN"

global CH_ENABLE_TRAP
CH_ENABLE_TRAP = "DMA{}_CH__RETEN"

global CH_TRANSFER_MODE
CH_TRANSFER_MODE = "DMA{}_CH__TRMODE"

global CH_SEL_CHSEL
CH_SEL_CHSEL = "DMA{}_SEL__CHSEL"

global CH_TRG_SRC
CH_TRG_SRC = "DMA{}CH_TRG_SRC"

global CH_SRC_ADDR_MODE
CH_SRC_ADDR_MODE = "DMA{}_CH__SAMODE"

global CH_DEST_ADDR_MODE
CH_DEST_ADDR_MODE = "DMA{}_CH__DAMODE"

global CH_DATA_SIZE
CH_DATA_SIZE = "DMA{}_CH__SIZE"

global INT_ENABLE
INT_ENABLE = "INTC_{}_ENABLE"

global INT_HANDLER_LOCK
INT_HANDLER_LOCK = "INTC_{}_HANDLER_LOCK"

global dma_ch_constants
dma_ch_constants = [
    CH_ENABLE_INT,
    CH_ENABLE_HALF_INT,
    CH_ENABLE_TRAP,
    CH_TRANSFER_MODE,
    CH_RELOAD_DST,
    CH_RELOAD_SRC,
    CH_TRG_SRC,
    CH_SRC_ADDR_MODE,
    CH_DEST_ADDR_MODE,
    CH_DATA_SIZE 
]

global MAX_NUM_CHANNEL
MAX_NUM_CHANNEL = 0

global LOW_ADDR_VALUE
LOW_ADDR_VALUE = 0x0

global HIGH_ADDR_VALUE
HIGH_ADDR_VALUE = 0xFFFFFF

global REPEATED
REPEATED = "Repeated"

global SOURCE
SOURCE = "source"

global MODULE_NAME
MODULE_NAME = "dmaModuleName"

global MAX_CHANNEL_COUNT
MAX_CHANNEL_COUNT = "MAX_CHANNEL_COUNT"

global DMA_REG_POR_SET
DMA_REG_POR_SET = "dmaRegPorSet"

global DMA_INTERRUPT_ENABLE
DMA_INTERRUPT_ENABLE = "dmaIntEnabled"

################################################################################
#### Callbacks ####
################################################################################

global dmaChEnableCb     
def dmaChEnableCb(symbol,event):
    dmaCh= symbol.getID()[3]
    dmaEnable = symbol.getComponent().getSymbolValue(DMA_ENABLE)
    symbolId = ENABLE_CH.format(dmaCh)
    symbolMon = symbol.getComponent().getSymbolByID(symbolId)
    if dmaEnable and symbolMon is not None:
        symbolMon.setVisible(True)
    else:
        symbolMon.setVisible(False)
    dmaChEnable(event[SOURCE],symbol,dmaCh)

global dmaChEnable 
def dmaChEnable(component,dmaChSymbol,dmaCh):
    for constant in dma_ch_constants:
        symbolId = constant.format(dmaCh)
        symbolMon = component.getSymbolByID(symbolId)
        if symbolMon is not None:
            symbolMon.setVisible(dmaChSymbol.getValue()) 
    if  dmaChSymbol.getValue(): 
        if dmaCh not in activeChList:
            activeChList.append(dmaCh)
        if(component.getSymbolValue(CH_ENABLE_INT.format(dmaCh))):
            updateInterruptState(dmaCh,True)                         
    else :
        updateInterruptState(dmaCh,False)
        if dmaCh in activeChList:          
            activeChList.remove(dmaCh)
    activeChList.sort()
    dmaChSymbol.getComponent().getSymbolByID(DMA_REG_POR_SET).setValue(createRegPorSetString())

global dmaChEnableIntCb
def dmaChEnableIntCb(symbol,event):
    dmaChannel = symbol.getID()[3]
    if symbol.getValue() :
        symbol.getComponent().getSymbolByID(DMA_INTERRUPT_ENABLE).setValue(True)
    updateInterruptState(dmaChannel,symbol.getValue())

global updateInterruptState
def updateInterruptState(dmaChInt,value):
    intIndex = getVectorIndex("DMA" + dmaChInt + "Interrupt")
    Database.setSymbolValue("core", INT_ENABLE.format(intIndex), value)
    Database.setSymbolValue("core", INT_HANDLER_LOCK.format(intIndex), value) 

global dmaChEnableIntCmntCb
def dmaChEnableIntCmntCb(symbol,event):
    dmaChannel = symbol.getID()[5]
    dmaChEnable = symbol.getComponent().getSymbolValue(ENABLE_CH.format(dmaChannel))
    dmaChIntVal = symbol.getComponent().getSymbolValue(CH_ENABLE_INT.format(dmaChannel))
    intIndex= getVectorIndex("DMA{}Interrupt".format(dmaChannel))
    dmaIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))
    if dmaChEnable and dmaChIntVal != dmaIntVal:
        symbol.setVisible(True)
        value = "Enable" if dmaChIntVal else "Disable"
        symbol.setLabel("Warning!!! " + value + " DMA{} Interrupt in Interrupts Section of System module".format(dmaChannel)) 
    elif dmaChEnable == False and dmaIntVal:
        symbol.setVisible(True)
        symbol.setLabel("Warning!!! Disable DMA{} Interrupt in Interrupts Section of System module".format(dmaChannel)) 
    else:
         symbol.setVisible(False)

global dmaChReloadCb
def dmaChReloadCb(symbol,event):
    dmaChannel = symbol.getID()[3]
    dmaChEnable = symbol.getComponent().getSymbolValue(ENABLE_CH.format(dmaChannel))
    if dmaChEnable:
        transferMode = event[SOURCE].getSymbolByID(CH_TRANSFER_MODE.format(dmaChannel))
        if REPEATED not in transferMode.getSelectedKey():
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)

global setVisibleOnUseDma
def setVisibleOnUseDma(symbol, event):
    symbol.setVisible(event["value"])

global updateTrgSrc
def updateTrgSrc(symbol,event):
    dmaChannel = symbol.getID()[3]
    trgSrcValueGrpName = getValueGroupName(DMA,DMA,"SEL","CHSEL")
    trgSrcValGrp = getValueGroup(DMA,trgSrcValueGrpName)
    selectedTrgSrc = symbol.getComponent().getSymbolByID(CH_TRG_SRC.format(dmaChannel)).getSelectedKey()
    for option in trgSrcValGrp.getChildren():
        if option.getAttribute("caption") == selectedTrgSrc:
            symbol.setValue(int(option.getAttribute("value"),16))

global createRegPorSetString
def createRegPorSetString():
    regPorSet = ""
    dmaChRegisterList = ["CH", "SEL", "STAT", "SRC", "DST", "CNT", "MSK", "PAT"]
    commonRegList = ["DMACON","DMABUF","DMALOW","DMAHIGH"]
    for reg in commonRegList:
        dmaRegDefaults[reg] = getRegisterDefaultValue(DMA, reg, reg)
        regPorSet += "    {} = {};\n\n".format(reg, dmaRegDefaults[reg])
    dmaChdmaRegDefaults = {}
    for reg in dmaChRegisterList:
        regName = "{}{}".format(DMA, reg)
        dmaChdmaRegDefaults[regName] = getRegisterDefaultValue(DMA ,DMA, reg)
    for ch in activeChList:
        for reg in dmaChRegisterList:
            regName = "{}{}{}".format(DMA, ch, reg)
            dmaRegDefaults[regName] = dmaChdmaRegDefaults[DMA + reg]
            regPorSet += "    {} = {};\n".format(regName, dmaRegDefaults[regName])
        regPorSet += "\n"
    return regPorSet

global dmaFileGeneration
def dmaFileGeneration(symbol, event):
    symbol.setEnabled(event["value"])

################## Symbol Creation for DMA Component ###############################################
MAX_NUM_CHANNEL = int(getParameterValue(DMA, DMA, NUM_CHANNEL))
LOW_ADDR_VALUE = long(int(getParameterValue(DMA, DMA, DMALOW),16))
HIGH_ADDR_VALUE = long(int(getParameterValue(DMA, DMA, DMAHIGH),16))

# DMA Configuration
dmaMenu = coreComponent.createMenuSymbol(DMA_MENU, None)
dmaMenu.setLabel("DMA")

# DMA Enable 
dmaEnable = coreComponent.createBooleanSymbol(DMA_ENABLE, dmaMenu)
dmaEnable.setLabel("Use DMA")
dmaEnable.setVisible(True)

# DMA Lower Address Limit - DMALOW
dmaLowerAddrLimit = coreComponent.createHexSymbol(LOW_ADDR_LIMIT, dmaEnable)
dmaLowerAddrLimit.setLabel("Lower Address Limit")
dmaLowerAddrLimit.setDefaultValue(LOW_ADDR_VALUE)   
dmaLowerAddrLimit.setMin(LOW_ADDR_VALUE)
dmaLowerAddrLimit.setMax(HIGH_ADDR_VALUE)
dmaLowerAddrLimit.setVisible(False)
dmaLowerAddrLimit.setDependencies(setVisibleOnUseDma, [DMA_ENABLE])
dmaLowerAddrLimit.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMALOW")

# DMA Higher Address Limit - DMAHIGH
dmaHigherAddrLimit = coreComponent.createHexSymbol(HIGH_ADDR_LIMIT, dmaEnable)
dmaHigherAddrLimit.setLabel("Higher Address Limit")
dmaHigherAddrLimit.setDefaultValue(HIGH_ADDR_VALUE)   
dmaHigherAddrLimit.setMin(LOW_ADDR_VALUE)
dmaHigherAddrLimit.setMax(HIGH_ADDR_VALUE) 
dmaHigherAddrLimit.setVisible(False)
dmaHigherAddrLimit.setDependencies(setVisibleOnUseDma, [DMA_ENABLE])
dmaHigherAddrLimit.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAHIGH")

for channelID in range(0, MAX_NUM_CHANNEL):
    # Enable Channel
    dmaChannelEnable = coreComponent.createBooleanSymbol(ENABLE_CH.format(channelID), dmaEnable)
    dmaChannelEnable.setLabel("Use DMA Channel " + str(channelID))
    dmaChannelEnable.setVisible(False)
    dmaChannelEnable.setDependencies(dmaChEnableCb, [ENABLE_CH.format(channelID),DMA_ENABLE])

    # Enable interrupt
    dmaChannelEnableInt = coreComponent.createBooleanSymbol(CH_ENABLE_INT.format(channelID), dmaChannelEnable)
    dmaChannelEnableInt.setLabel("Enable Interrupt")
    dmaChannelEnableInt.setVisible(False)
    dmaChannelEnableInt.setDependencies(dmaChEnableIntCb,[CH_ENABLE_INT.format(channelID)])
    dmaChannelEnableInt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:intc_04436;register:IFS2")
    
    #Interrupt Warning Comment
    intIndex= getVectorIndex("DMA{}Interrupt".format(channelID))
    dmaIntComment = coreComponent.createCommentSymbol(CH_ENABLE_INT_CMNT.format(channelID), dmaChannelEnable)
    dmaIntComment.setVisible(False)
    dmaIntComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
    dmaIntComment.setDependencies(dmaChEnableIntCmntCb, [ENABLE_CH.format(channelID),CH_ENABLE_INT.format(channelID), INT_ENABLE.format(intIndex)])

    dmaChannelHalfInt = coreComponent.createBooleanSymbol(CH_ENABLE_HALF_INT.format(channelID), dmaChannelEnable)
    dmaChannelHalfInt.setLabel("Enable 50% Completion Watermark Interrupt")
    dmaChannelHalfInt.setVisible(False)

    # Trigger Source
    dmaTrgSrc = createKeyValueSetSymbol(coreComponent, DMA, CH_TRG_SRC.format(channelID),"DMA","SEL","CHSEL",dmaChannelEnable) 
    dmaTrgSrc.setLabel("Trigger Source")
    dmaTrgSrc.setVisible(False)
    dmaTrgSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    dmaTrgSrcHex = coreComponent.createHexSymbol(CH_SEL_CHSEL.format(channelID),None)
    dmaTrgSrcHex.setDefaultValue(0)
    dmaTrgSrcHex.setVisible(False)
    dmaTrgSrcHex.setDependencies(updateTrgSrc, [CH_TRG_SRC.format(channelID)])
    dmaTrgSrcHex.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxSEL")
    
    # Source Address Mode
    dmaSourceMode = createKeyValueSetSymbol(coreComponent, DMA, CH_SRC_ADDR_MODE.format(channelID), "DMA","CH","SAMODE",dmaChannelEnable)  
    dmaSourceMode.setLabel("Source Address Mode")
    dmaSourceMode.setVisible(False)
    dmaSourceMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    # Destination Address Mode
    dmaDestinationMode = createKeyValueSetSymbol(coreComponent, DMA, CH_DEST_ADDR_MODE.format(channelID), "DMA","CH","DAMODE",dmaChannelEnable)  
    dmaDestinationMode.setLabel("Destination Address Mode")
    dmaDestinationMode.setVisible(False)
    dmaDestinationMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    # Data Size
    dmaDataSize = createKeyValueSetSymbol(coreComponent, DMA, CH_DATA_SIZE.format(channelID), "DMA","CH","SIZE",dmaChannelEnable)  
    dmaDataSize.setLabel("Data Size")
    dmaDataSize.setVisible(False)
    dmaDataSize.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    # Transfer Mode
    dmaTransferMode = createKeyValueSetSymbol(coreComponent, DMA, CH_TRANSFER_MODE.format(channelID),"DMA","CH","TRMODE", dmaChannelEnable)  
    dmaTransferMode.setLabel("Transfer Mode")
    dmaTransferMode.setVisible(False)
    dmaTransferMode.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    # Enable reload count
    dmaEnableReloadCnt = coreComponent.createBooleanSymbol(CH_RELOAD_CNT.format(channelID) , dmaTransferMode)
    dmaEnableReloadCnt.setLabel("Reload Count")
    dmaEnableReloadCnt.setVisible(False)
    dmaEnableReloadCnt.setDependencies(dmaChReloadCb,[ENABLE_CH.format(channelID),CH_TRANSFER_MODE.format(channelID)])
    dmaEnableReloadCnt.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")
    
    # Enable reload destination address
    dmaEnableReloadDst = coreComponent.createBooleanSymbol(CH_RELOAD_DST.format(channelID) , dmaTransferMode)
    dmaEnableReloadDst.setLabel("Reload Destination Address")
    dmaEnableReloadDst.setVisible(False)
    dmaEnableReloadDst.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")

    # Enable reload source address
    dmaEnableReloadSrc = coreComponent.createBooleanSymbol(CH_RELOAD_SRC.format(channelID) , dmaTransferMode)
    dmaEnableReloadSrc.setLabel("Reload Source Address")
    dmaEnableReloadSrc.setVisible(False)
    dmaEnableReloadSrc.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")
    
    dmaChannelEnableTrap = coreComponent.createBooleanSymbol(CH_ENABLE_TRAP.format(channelID), dmaChannelEnable)
    dmaChannelEnableTrap.setLabel("Enable Read Error Trap")
    dmaChannelEnableTrap.setVisible(False)
    dmaChannelEnableTrap.setHelp("atmel;device:" + Variables.get("__PROCESSOR") + ";comp:dma_04077;register:DMAxCH")
         
moduleName = coreComponent.createStringSymbol(MODULE_NAME, None)
moduleName.setDefaultValue(DMA)
moduleName.setVisible(False)

numChannel = coreComponent.createIntegerSymbol(MAX_CHANNEL_COUNT, None)
numChannel.setDefaultValue(MAX_NUM_CHANNEL)
numChannel.setVisible(False)     

regPorSet = coreComponent.createStringSymbol(DMA_REG_POR_SET, None)
regPorSet.setDefaultValue(createRegPorSetString())
regPorSet.setVisible(False)

intEnabled = coreComponent.createBooleanSymbol(DMA_INTERRUPT_ENABLE, None)
intEnabled.setDefaultValue(False)
intEnabled.setVisible(False)

##################### Code Generation #######################################
configName = Variables.get("__CONFIGURATION_NAME")

#Header file
dmaHeaderFile = coreComponent.createFileSymbol("DMA_HEADER", None)
dmaHeaderFile.setSourcePath("../peripheral/dma_04077/templates/plib_dma.h.ftl")
dmaHeaderFile.setOutputName("plib_dma.h")
dmaHeaderFile.setDestPath("/peripheral/dma/")
dmaHeaderFile.setProjectPath("config/" + configName +"/peripheral/dma/")
dmaHeaderFile.setType("HEADER")
dmaHeaderFile.setMarkup(True)
dmaHeaderFile.setEnabled(False)
dmaHeaderFile.setDependencies(dmaFileGeneration, [DMA_ENABLE])

#Source File
dmaSourceFile = coreComponent.createFileSymbol("DMA_SOURCE", None)
dmaSourceFile.setSourcePath("../peripheral/dma_04077/templates/plib_dma.c.ftl")
dmaSourceFile.setOutputName("plib_dma.c")
dmaSourceFile.setDestPath("/peripheral/dma/")
dmaSourceFile.setProjectPath("config/" + configName +"/peripheral/dma/")
dmaSourceFile.setType("SOURCE")
dmaSourceFile.setMarkup(True)
dmaSourceFile.setEnabled(False)
dmaSourceFile.setDependencies(dmaFileGeneration, [DMA_ENABLE])

#System Initialization
dmaSystemInitFile = coreComponent.createFileSymbol("DMA_SYS_INIT", None)
dmaSystemInitFile.setType("STRING")
dmaSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
dmaSystemInitFile.setSourcePath("../peripheral/dma_04077/templates/system/initialization.c.ftl")
dmaSystemInitFile.setMarkup(True)
dmaSystemInitFile.setEnabled(False)
dmaSystemInitFile.setDependencies(dmaFileGeneration, [DMA_ENABLE])

#System Definition
dmaSystemDefFile = coreComponent.createFileSymbol("DMA_SYS_DEF", None)
dmaSystemDefFile.setType("STRING")
dmaSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
dmaSystemDefFile.setSourcePath("../peripheral/dma_04077/templates/system/definitions.h.ftl")
dmaSystemDefFile.setMarkup(True)
dmaSystemDefFile.setEnabled(False)
dmaSystemDefFile.setDependencies(dmaFileGeneration, [DMA_ENABLE])
