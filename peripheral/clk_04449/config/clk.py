"""*****************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

""" dsPIC33AK Clock Configuration File. """
from os.path import join
from xml.etree import ElementTree
import re

#ATDF Helper Functions 
global getModuleRegisterGroup
def getModuleRegisterGroup(moduleName,registerGroup):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]'
    registerGroupNode = ATDF.getNode(atdfPath)
    if(registerGroupNode != None):
        return registerGroupNode.getChildren()
    return None

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

global getValueGroup   
def getValueGroup(moduleName,valueGroupName):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/value-group@[name="'+ valueGroupName + '"]'
    return ATDF.getNode(atdfPath)

global getBitField   
def getBitField(moduleName,registerGroup,register,bitfield):
    atdfPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]/bitfield@[name="'+bitfield +'"]'
    return ATDF.getNode(atdfPath)

global getValueGroupName
def getValueGroupName(moduleName,registerGroup,register,bitfield):
    bitNode = getBitField(moduleName,registerGroup,register,bitfield)
    if(bitNode != None):
        return bitNode.getAttribute("values")
    return ""

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

global getKeyValuePairBasedonKey
def getKeyValuePairBasedonKey(key,keyValueOptionList):
    index = 0
    for ii in keyValueOptionList:
        if ii["key"] == key:
            return index  # return occurrence of <bitfield > entry which has matching value
        index += 1

    print("find_key: could not find key in dictionary") # should never get here
    return ""    

global addKeystoKeyValueSymbol
def addKeystoKeyValueSymbol(bitSymbol,bitfieldOptionList):
    for ii in bitfieldOptionList:
        bitSymbol.addKey( ii['key'],ii['value'], ii['desc'] )  
 
global createKeyValueSetSymbol   
def createKeyValueSetSymbol(component,moduleName,registerGroup,register,bitfield): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            symbolKey = valueGroupEntry       
            optionList = getBitfieldOptionList(valGroup)   
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolKey, None )
            valueGroupEntryComp.setLabel(symbolKey)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp  

global handleClockSettingsMessage 
def handleClockSettingsMessage(messageID, args):
    if messageID == "CONFIGURATOR_CLOCK_AUTO_CALCULATE_PLL_DIVIDERS":
        pllClkSrc = args.get('pllClkSrcFreq')
        requestedPllFout = args.get('reqPlloFreq')
        requestedPllVcoDivider = args.get('reqPllVcoDivFreq')
        pllNo = args.get('pllNo')
        val = {}
        if requestedPllFout is not None and requestedPllVcoDivider is not None:
            val = getPlloandVcoFreqParams(pllNo, pllClkSrc, requestedPllFout, requestedPllVcoDivider, pll_mul_div_ranges, pll_freq_ranges)
        elif requestedPllFout is not None:
            val = getPlloFreqParams(pllNo, pllClkSrc, requestedPllFout, pll_mul_div_ranges, pll_freq_ranges)
            intdiv = Database.getSymbolValue("core",PLL_INTDIV.format(pllNo))
            val["calcPllVcoDivFreq"] = getCalcVcoFreq(pllClkSrc, val[PLLPRE.format(pllNo)],val[PLLFBD.format(pllNo)],intdiv) 
            
        elif requestedPllVcoDivider is not None:
            val = getPllVcoDivParams(pllNo, pllClkSrc, requestedPllVcoDivider, pll_mul_div_ranges, pll_freq_ranges)
            postdiv1 = int(Database.getSymbolValue("core",POSTDIV1.format(pllNo)))
            postdiv2 = int(Database.getSymbolValue("core",POSTDIV2.format(pllNo)))
            val["calcPlloFreq"] = getCalcPlloFreq(pllClkSrc, val[PLLPRE.format(pllNo)],val[PLLFBD.format(pllNo)],postdiv1 ,postdiv2)
        return val
    return {}     

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

global getSettingBitDefaultAndMaskValue 
def getSettingBitDefaultAndMaskValue(moduleName,registerGroup,register,bitfield):
     regPath = '/avr-tools-device-file/modules/module@[name="' + moduleName + '"]/register-group@[name="'+ registerGroup + '"]/register@[name="'+ register + '"]'
     registerNode = ATDF.getNode(regPath)
     if(registerNode != None):
         regDefaultVal = registerNode.getAttribute("initval")
         bitNode = getBitField(moduleName,registerGroup,register,bitfield)
         if(bitNode != None):
             bitMask = bitNode.getAttribute("mask")
             bitMaskVal = int( bitMask.rstrip('0'), 16)
             return{
                 "defaultValue" : getDefaultVal(regDefaultVal,bitMask),
                 "maskValue" :bitMaskVal
             }
     return  {
                 "defaultValue" : 0,
                 "maskValue" :0
             }         

#Interrupt related Helper Function

global getInterruptSymbolMapForCodeGen
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
                    intSymbolName = bitName.replace("IF","").lower() + "InterruptFlagBit"
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
                    intSymbolName = bitName.replace("IE","").lower() + "InterruptEnableBit"
                    intSymbolMap[intSymbolName] = registerNode.getAttribute("name") +"bits." +bitName
                    if(len(intSymbolMap) == intEntryCount):
                        isEnableDataAdded = True
                        break
            if isEnableDataAdded:
                break                          
        
    return intSymbolMap

global createIsrHandlerNameSymbol
def createIsrHandlerNameSymbol(component,symbolName,interrupt,menuName):
        isrName =interrupt+"_InterruptHandler"
        interruptSymbol = component.createStringSymbol(symbolName, menuName)
        interruptSymbol.setDefaultValue(isrName)
        interruptSymbol.setVisible(False)

global createInterruptSymbols
def createInterruptSymbols(component,intSymbolMap,menuName):
    for key in intSymbolMap:
        interruptSymbol = component.createStringSymbol(key, menuName)
        interruptSymbol.setDefaultValue(intSymbolMap[key])
        interruptSymbol.setVisible(False)

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
        
# def updateInterruptLists(instanceNo, interruptList):
#     for interrupt in interruptList:
#         intIndex = getVectorIndex("U" + instanceNo +interrupt +"Interrupt")
#         interruptEnableList.append("core.IC_"+intIndex+"_ENABLE")
#         interruptHandlerLockList.append("core.IC_"+intIndex+"_HANDLER_LOCK")

global INT_ENABLE
INT_ENABLE = "INTC_{}_ENABLE"

global INT_HANDLER_LOCK
INT_HANDLER_LOCK = "INTC_{}_HANDLER_LOCK"

global updateMonitorInterruptState
def updateMonitorInterruptState(clkMon ,interruptType,value):
    intIndex = getVectorIndex("CLK" + clkMon + interruptType + "Interrupt")
    Database.setSymbolValue("core", INT_ENABLE.format(intIndex), value)
    Database.setSymbolValue("core", INT_HANDLER_LOCK.format(intIndex), value)  

global clkMonThresholdEnableIntCb
def clkMonThresholdEnableIntCb(symbol,event):
    clkMon = symbol.getID()[2]
    updateMonitorInterruptState(clkMon,"F",symbol.getValue())
  
global clkMonWarnEnableIntCb
def clkMonWarnEnableIntCb(symbol,event):
    clkMon = symbol.getID()[2]
    updateMonitorInterruptState(clkMon,"W",symbol.getValue())
  
global clkMonReadyEnableIntCb
def clkMonReadyEnableIntCb(symbol,event):
    clkMon = symbol.getID()[2]
    updateMonitorInterruptState(clkMon,"R",symbol.getValue())
    
global clockFailIntEnableCb
def clockFailIntEnableCb(symbol,event):
    intIndex= getVectorIndex("CLKFInterrupt")
    Database.setSymbolValue("core", INT_ENABLE.format(intIndex), symbol.getValue())
    Database.setSymbolValue("core", INT_HANDLER_LOCK.format(intIndex), symbol.getValue())   

global clockFailIntCmntCb
def clockFailIntCmntCb(symbol,event):
    clkFailIntVal = symbol.getComponent().getSymbolValue("clockFailIntEnable")
    intIndex= getVectorIndex("CLKFInterrupt")
    intModFailIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))   
    if clkFailIntVal != intModFailIntVal:
        symbol.setVisible(True)
        value = "Enable" if clkFailIntVal else "Disable"
        symbol.setLabel("Warning!!! " + value + " Clock Fail Interrupt in Interrupts Section of System module") 
    else:
         symbol.setVisible(False) 
         
global clockMonRdyIntCmntCb
def clockMonRdyIntCmntCb(symbol,event):
    clkMon = symbol.getID()[2]
    clkMonEnable = symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMon))
    clkMonRdyIntVal = symbol.getComponent().getSymbolValue(CLK_MON_DATA_READY_ENABLE_INT.format(clkMon))
    intIndex= getVectorIndex("CLK{}RInterrupt".format(clkMon))
    intModClkMonRdyIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))   
    if clkMonEnable and clkMonRdyIntVal != intModClkMonRdyIntVal:
        symbol.setVisible(True)
        value = "Enable" if clkMonRdyIntVal else "Disable"
        symbol.setLabel("Warning!!! " + value + " Clock Monitor{} Ready Interrupt in Interrupts Section of System module".format(clkMon)) 
    elif clkMonEnable == False and intModClkMonRdyIntVal:
        symbol.setVisible(True)
        symbol.setLabel("Warning!!! Disable Clock Monitor{} Ready Interrupt in Interrupts Section of System module".format(clkMon)) 
    else:
         symbol.setVisible(False)     

global clockMonErrorIntCmntCb
def clockMonErrorIntCmntCb(symbol,event):
    clkMon = symbol.getID()[2]
    clkMonEnable = symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMon))
    intIndex= getVectorIndex("CLK{}MInterrupt".format(clkMon))
    intModClkMonErrorIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))   
    if clkMonEnable != intModClkMonErrorIntVal:
        symbol.setVisible(True)
        value = "Enable" if clkMonEnable else "Disable"
        symbol.setLabel("Warning!!! " + value + " Clock Monitor{} Error Interrupt in Interrupts Section of System module".format(clkMon)) 
    else:
         symbol.setVisible(False)

global clockMonWarnIntCmntCb
def clockMonWarnIntCmntCb(symbol,event):
    clkMon = symbol.getID()[2]
    clkMonEnable = symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMon))            
    clkMonWarnIntVal = symbol.getComponent().getSymbolValue(CLK_MON_WARN_ENABLE_INT.format(clkMon))
    intIndex= getVectorIndex("CLK{}WInterrupt".format(clkMon))
    intModClkMonWarnIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))   
    if clkMonEnable and clkMonWarnIntVal != intModClkMonWarnIntVal:
        symbol.setVisible(True)
        value = "Enable" if clkMonWarnIntVal else "Disable"
        symbol.setLabel("Warning!!! " + value + " Clock Monitor{} Warning Interrupt in Interrupts Section of System module".format(clkMon)) 
    elif clkMonEnable == False and intModClkMonWarnIntVal:
        symbol.setVisible(True)
        symbol.setLabel("Warning!!! Disable Clock Monitor{} Warning Interrupt in Interrupts Section of System module".format(clkMon)) 
    else:
        symbol.setVisible(False)    

global clockMonThresholdIntCmntCb
def clockMonThresholdIntCmntCb(symbol,event):
    clkMon = symbol.getID()[2]
    clkMonEnable = symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMon))
    clkMonFailIntVal = symbol.getComponent().getSymbolValue(CLK_MON_THRESHOLD_ENABLE_INT.format(clkMon))
    intIndex= getVectorIndex("CLK{}FInterrupt".format(clkMon))
    intModClkMonFailIntVal = symbol.getComponent().getSymbolValue(INT_ENABLE.format(intIndex))   
    if clkMonEnable and clkMonFailIntVal != intModClkMonFailIntVal:
        symbol.setVisible(True)
        value = "Enable" if clkMonFailIntVal else "Disable"
        symbol.setLabel("Warning!!! " + value + " Clock Monitor{} Fail Interrupt in Interrupts Section of System module".format(clkMon)) 
    elif clkMonEnable == False and intModClkMonFailIntVal:
        symbol.setVisible(True)
        symbol.setLabel("Warning!!! Disable Clock Monitor{} Fail Interrupt in Interrupts Section of System module".format(clkMon))
    else:
         symbol.setVisible(False)                          
     
#CLOCK configurations

global SOURCE
SOURCE = "source"

global FRC_OSCILLATOR
FRC_OSCILLATOR = "FRC"

global BACKUP_FRC_OSCILLATOR
BACKUP_FRC_OSCILLATOR = "BFRC"

global LPRC
LPRC = "LPRC"

global CLOCK_GENERATOR
CLOCK_GENERATOR = "Clock Generator "

global PARAM_CLOCK_GENERATOR_SUPPORTED
PARAM_CLOCK_GENERATOR_SUPPORTED = "Clock_Generator_Count"

global PARAM_FRC_CLOCK
PARAM_FRC_CLOCK = "FRC_CLOCK"

global PARAM_LPRC_CLOCK
PARAM_LPRC_CLOCK = "LPRC_VALUE"

global PARAM_SEC_OSC_CLOCK
PARAM_SEC_OSC_CLOCK = "SECONDARY_OSC_VALUE"

global PARAM_DEFAULT_CLK_GEN_ENABLED 
PARAM_DEFAULT_CLK_GEN_ENABLED = "DEFAULT_CLK_GEN_ENABLED"

global PARAM_CLK_GEN_DIVIDER_NOT_SUPPORTED 
PARAM_CLK_GEN_DIVIDER_NOT_SUPPORTED = "CLK_GEN_DIVIDER_NOT_SUPPORTED"

global EXTERNAL_CLOCK
EXTERNAL_CLOCK = "External Clock"

global PRIMARY_OSCILLATOR
PRIMARY_OSCILLATOR = "POSC"

global NONE
NONE = "None"


global PARAM_MIN_INPUT_PLL_FREQ_HZ
PARAM_MIN_INPUT_PLL_FREQ_HZ = "MIN_INPUT_PLL_FREQ_HZ"

global PARAM_MAX_INPUT_PLL_FREQ_HZ
PARAM_MAX_INPUT_PLL_FREQ_HZ = "MAX_INPUT_PLL_FREQ_HZ"

global PARAM_MIN_PLL_VCO_INTERIM_FREQ_HZ
PARAM_MIN_PLL_VCO_INTERIM_FREQ_HZ = "MIN_PLL_VCO_INTERIM_FREQ_HZ"

global PARAM_MAX_PLL_VCO_INTERIM_FREQ_HZ
PARAM_MAX_PLL_VCO_INTERIM_FREQ_HZ = "MAX_PLL_VCO_INTERIM_FREQ_HZ"

global PARAM_MIN_PLL_VCO_FREQ_HZ
PARAM_MIN_PLL_VCO_FREQ_HZ = "MIN_PLL_VCO_FREQ_HZ"

global PARAM_MAX_PLL_VCO_FREQ_HZ
PARAM_MAX_PLL_VCO_FREQ_HZ = "MAX_PLL_VCO_FREQ_HZ"

global PARAM_MIN_PLLO_FREQ_HZ
PARAM_MIN_PLLO_FREQ_HZ = "MIN_PLLO_FREQ_HZ"

global PARAM_MAX_PLLO_FREQ_HZ
PARAM_MAX_PLLO_FREQ_HZ = "MAX_PLLO_FREQ_HZ"

global PARAM_MIN_PLL_FEEDBACK_DIV
PARAM_MIN_PLL_FEEDBACK_DIV = "MIN_PLL_FEEDBACK_DIV"

global PARAM_MAX_PLL_FEEDBACK_DIV
PARAM_MAX_PLL_FEEDBACK_DIV = "MAX_PLL_FEEDBACK_DIV"

global PARAM_MIN_PRIMARY_OSC_XT_FREQ
PARAM_MIN_PRIMARY_OSC_XT_FREQ = "MIN_PRIMARY_OSC_XT_FREQ"

global PARAM_MAX_PRIMARY_OSC_HS_FREQ
PARAM_MAX_PRIMARY_OSC_HS_FREQ = "MAX_PRIMARY_OSC_HS_FREQ"

global PARAM_MAX_PRIMARY_OSC_XT_FREQ
PARAM_MAX_PRIMARY_OSC_XT_FREQ = "MAX_PRIMARY_OSC_XT_FREQ"

global PARAM_MIN_EXTERNAL_OSC_FREQ
PARAM_MIN_EXTERNAL_OSC_FREQ = "MIN_EXTERNAL_OSC_FREQ"

global PARAM_MAX_EXTERNAL_OSC_FREQ
PARAM_MAX_EXTERNAL_OSC_FREQ = "MAX_EXTERNAL_OSC_FREQ"

global PARAM_CLK_MON_COUNT
PARAM_CLK_MON_COUNT = "Clock_Monitor_Count"

global PARAM_REFERENCE_INPUT_SRC_COUNT
PARAM_REFERENCE_INPUT_SRC_COUNT = "REFERENCE_INPUT_SRC_COUNT"

global PARAM_Pll_GEN_COUNT
PARAM_Pll_GEN_COUNT = "Pll_Gen_Count"

global SERIAL_TEST_MODE_CLOCK
SERIAL_TEST_MODE_CLOCK = "Serial Test Mode clock (PGC)"

global INTERNAL_OSCILLATOR
INTERNAL_OSCILLATOR = "clk"

global CLOCK
CLOCK = "CLOCK"

global CLK_CON_REG_GROUP
CLK_CON_REG_GROUP = "CLK"

global CLK_CON_REG
CLK_CON_REG = "CON"

global CLK_DIV_REG
CLK_DIV_REG = "DIV"

global FRACDIV
FRACDIV = "FRACDIV"

global FRACDIV_CYCLE_COUNT
FRACDIV_CYCLE_COUNT = 512

global PLL
PLL = "pll"

global PLL_CON__NOSC
PLL_CON__NOSC = "PLL_CON__NOSC"

global PLL_REG_GROUP
PLL_REG_GROUP = "PLL"

global VCO_REG_GROUP
VCO_REG_GROUP = "VCO"

global PLL_REG_CON
PLL_REG_CON = "CON"

global PLL_REG_DIV
PLL_REG_DIV = "DIV"

global PLL_REG_VCO
PLL_REG_VCO = "VCO"

global NOSC
NOSC = "NOSC"

global BOSC
BOSC = "BOSC"

global PLLPRE
PLLPRE = "pll{}DIV__PLLPRE"

global PLLFBD
PLLFBD = "pll{}DIV__PLLFBDIV"  

global POSTDIV1
POSTDIV1 = "pll{}DIV__POSTDIV1"

global POSTDIV2
POSTDIV2 = "pll{}DIV__POSTDIV2"

global PLL_INTDIV
PLL_INTDIV = "vco{}DIV__INTDIV"

global CLK_GEN_ENABLE
CLK_GEN_ENABLE = "clkGen{}Enable"

global CLK_GEN_NOSC
CLK_GEN_NOSC = "clkGen{}CON__NOSC"

global CLK_GEN_CLK_SRC_FREQ
CLK_GEN_CLK_SRC_FREQ = "clkGen{}ClkSrcFrequency"

global CLK_GEN_DIVIDER_ENABLE
CLK_GEN_DIVIDER_ENABLE = "clkGen{}IsDividerEnabled"

global CLK_GEN_INTDIV
CLK_GEN_INTDIV = "clkGen{}DIV__INTDIV"

global CLK_GEN_FRACDIV
CLK_GEN_FRACDIV = "clkGen{}DIV__FRACDIV"

global CLK_GEN_CALCULATED_FREQ
CLK_GEN_CALCULATED_FREQ = "clkGen{}OutFrequency"

global CLK_GEN_CALCULATED_FREQ_CMNT
CLK_GEN_CALCULATED_FREQ_CMNT = "clkGen{}OutFrequencyCmnt"

global CLK_GEN_CALCULATED_FREQ_MHZ
CLK_GEN_CALCULATED_FREQ_MHZ = "clkGen{}OutFrequencyInMHz"

global CLK_GEN_FAIL_MASK
CLK_GEN_FAIL_MASK = "clkGen{}ClkFailMask"

global CLK_GEN_ENABLE_FAIL_SAFE
CLK_GEN_ENABLE_FAIL_SAFE = "clkGen{}enableFailSafeClock"

global CLK_GEN_FSCMEN
CLK_GEN_FSCMEN = "clkGen{}CON__FSCMEN"

global CLK_GEN_BOSC
CLK_GEN_BOSC = "clkGen{}CON__BOSC"

global EXT_CLK_SRC_SEL
EXT_CLK_SRC_SEL = "extClkSrcSel"

global EXT_CLK_SRC_FREQ
EXT_CLK_SRC_FREQ = "extClkSrcFreq"

global CALC_EXT_CLK_SRC_FREQ
CALC_EXT_CLK_SRC_FREQ = "calcExtClkSrcFreq"

global EXT_CLK_SRC_DEFAULT_FREQ
EXT_CLK_SRC_DEFAULT_FREQ = 8000000

global REFERENCE_INPUT
REFERENCE_INPUT = "Reference Input"

global REF_INPUT_PIN_ENABLE
REF_INPUT_PIN_ENABLE = "referenceInputPinEnable"
global REF_INPUT_PIN_FREQ
REF_INPUT_PIN_FREQ = "referenceInputPinFreq"

global REF_INPUT_DEFAULT_FREQ
REF_INPUT_DEFAULT_FREQ = 8000000

global PLL_ENABLE
PLL_ENABLE = "pll{}Enable"

global PLL_CLOCK_SOURCE
PLL_CLOCK_SOURCE = "pll{}CON__NOSC"

global PLL_CLOCK_SOURCE_FREQ
PLL_CLOCK_SOURCE_FREQ = "pll{}ClockSourceFreq"

global PLL_CALC_VCO_FREQ
PLL_CALC_VCO_FREQ = "pll{}calculatedVCOFrequency"
global PLL_CALC_PFD_FREQ
PLL_CALC_PFD_FREQ = "pll{}calculatedPfdFrequency"

global PLL_CALC_PLLO_FREQ
PLL_CALC_PLLO_FREQ = "pll{}calculatedFoutFrequency"

global PLL_CALC_VCO_FREQ_MHZ
PLL_CALC_VCO_FREQ_MHZ = "pll{}VcoFrequencyInMHz"

global PLL_CALC_PLLO_FREQ_MHZ
PLL_CALC_PLLO_FREQ_MHZ = "pll{}OutFrequencyInMHz"

global PLL_FAIL_SAFE_CLK_ENABLE
PLL_FAIL_SAFE_CLK_ENABLE = "pll{}EnableFailSafeClockPll"

global PLL_BACKUP_CLOCK_SOURCE
PLL_BACKUP_CLOCK_SOURCE = "pll{}CON__BOSC"

global PLL_FSCMEN
PLL_FSCMEN = "pll{}CON__FSCMEN" 

global PLL_GEN_FAIL_MASK
PLL_GEN_FAIL_MASK = "pll{}ClkFailMask"

global pll_constants
pll_constants = [
    PLL_CLOCK_SOURCE,
    PLL_CLOCK_SOURCE_FREQ,
    PLLPRE,
    PLLFBD,
    PLL_INTDIV,
    PLL_CALC_PFD_FREQ,
    PLL_CALC_VCO_FREQ,
    POSTDIV1,
    POSTDIV2,
    PLL_CALC_PLLO_FREQ,
    PLL_FAIL_SAFE_CLK_ENABLE,
]

global CLK_MON_GROUP
CLK_MON_GROUP = "Clock Monitor"

global CLK_MON_ENABLE
CLK_MON_ENABLE = "cm{}Enable"

global CLK_MON_ENABLE_INIT_STAGE
CLK_MON_ENABLE_INIT_STAGE = "cm{}EnableInitStage"

global CM_REG_GROUP
CM_REG_GROUP = "CM"

global CM_REG_SEL
CM_REG_SEL = "SEL"

global CM_REG_CON
CM_REG_CON = "CON"

global WINSEL
WINSEL = "WINSEL"

global CNTSEL
CNTSEL = "CNTSEL"

global CNTDIV
CNTDIV = "CNTDIV"

global CM_SEL__WINSEL
CM_SEL__WINSEL = "CM{}SEL__WINSEL"

global CM_SEL__CNTSEL
CM_SEL__CNTSEL = "CM{}SEL__CNTSEL"

global CM_CON__CNTDIV
CM_CON__CNTDIV = "CM{}CON__CNTDIV"

global CLK_MON_REF_CLK_SRC_FREQ
CLK_MON_REF_CLK_SRC_FREQ = "cm{}RefClkSrcFreq"

global CLK_MON_ACCUMULATION_WINDOW
CLK_MON_ACCUMULATION_WINDOW = "cm{}WINPRValue"

global CLK_MON_TIMER_WINDOW_PERIOD
CLK_MON_TIMER_WINDOW_PERIOD = "cm{}TimerWindowPeriod"

global CLK_MON_CLK_SRC_FREQ
CLK_MON_CLK_SRC_FREQ = "cm{}ClkSrcFreq"


global CLK_MON_SATURATION_COUNT
CLK_MON_SATURATION_COUNT = "cm{}SATValue"

global CLK_MON_BUFFER_COUNT
CLK_MON_BUFFER_COUNT = "cm{}BUFValue"

global CLK_MON_DATA_READY_ENABLE_INT
CLK_MON_DATA_READY_ENABLE_INT = "cm{}rdyIntEnable"

global CLK_MON_ERROR_INT_CMNT
CLK_MON_ERROR_INT_CMNT = "cm{}MonitorErrorIntEnableCmnt"

global CLK_MON_DATA_READY_ENABLE_INT_CMNT
CLK_MON_DATA_READY_ENABLE_INT_CMNT = "cm{}DataReadyIntEnableCmnt"

global CLK_MON_WARN_ENABLE_INT
CLK_MON_WARN_ENABLE_INT = "cm{}warnIntEnable"


global CLK_MON_WARN_ENABLE_INT_CMNT
CLK_MON_WARN_ENABLE_INT_CMNT = "cm{}WarningEnableIntCmnt"

global CLK_MON_WARN_HIGH_COUNT
CLK_MON_WARN_HIGH_COUNT = "cm{}HWARNValue"

global CLK_MON_WARN_LOW_COUNT
CLK_MON_WARN_LOW_COUNT = "cm{}LWARNValue"

global CLK_MON_WARN_FREQ_RANGE
CLK_MON_WARN_FREQ_RANGE = "cm{}WarningFreqRange"

global CLK_MON_THRESHOLD_ENABLE_INT
CLK_MON_THRESHOLD_ENABLE_INT = "cm{}failIntEnable"

global CLK_MON_THRESHOLD_ENABLE_INT_CMNT
CLK_MON_THRESHOLD_ENABLE_INT_CMNT = "cm{}FailEnableIntCmnt"

global CLK_MON_THRESHOLD_HIGH_COUNT
CLK_MON_THRESHOLD_HIGH_COUNT = "cm{}HFAILValue"

global CLK_MON_THRESHOLD_LOW_COUNT
CLK_MON_THRESHOLD_LOW_COUNT = "cm{}LFAILValue"

global CLK_MON_THRESHOLD_FREQ_RANGE
CLK_MON_THRESHOLD_FREQ_RANGE = "cm{}ThresholdFreqRange"

global CLK_MON_CMxCON_MASK
CLK_MON_CMxCON_MASK = 0xffff7fff

global clk_gen_constants
clk_gen_constants = [
    CLK_GEN_NOSC,
    CLK_GEN_CLK_SRC_FREQ,
    CLK_GEN_DIVIDER_ENABLE,
    CLK_GEN_CALCULATED_FREQ,
    CLK_GEN_ENABLE_FAIL_SAFE,
    CLK_GEN_CALCULATED_FREQ_CMNT
]

global clk_mon_constants
clk_mon_constants = [
    CLK_MON_ENABLE_INIT_STAGE,
    CM_SEL__WINSEL,
    CLK_MON_REF_CLK_SRC_FREQ,
    CLK_MON_ACCUMULATION_WINDOW,
    CLK_MON_TIMER_WINDOW_PERIOD,
    CM_SEL__CNTSEL,
    CLK_MON_CLK_SRC_FREQ,
    CM_CON__CNTDIV,
    CLK_MON_SATURATION_COUNT,
    CLK_MON_BUFFER_COUNT,
    CLK_MON_DATA_READY_ENABLE_INT,
    CLK_MON_WARN_ENABLE_INT,
    CLK_MON_THRESHOLD_ENABLE_INT,
]

global PROP_CLK_MON_SUPPORTED
PROP_CLK_MON_SUPPORTED = "Clock_Monitor_Count"

global string_to_list
def string_to_list(input_str):
    # Split the string by commas and convert each element to an integer
    return [int(num) for num in input_str.split(',')]

global getClkGenNo
def getClkGenNo(str):
    clkGenDigit1 = str[6]
    clkGenDigit2 = str[7]
    if clkGenDigit2.isdigit():
        clkGenDigit1 += clkGenDigit2
    return clkGenDigit1 

global clkSrcNamesMap
clkSrcNamesMap = {
    "Reference Input1": "REFI1",
    "Reference Input2": "REFI2",
    "PLL2 VCO Divider output": "PLL2 VCO DIV",
    "PLL1 VCO Divider output": "PLL1 VCO DIV",
    "PLL2 Out output": "PLL2 FOUT",
    "PLL1 Out output": "PLL1 FOUT",
    "LPRC": "LPRC",
    "Primary Oscillator": "POSC",
    "Backup FRC Oscillator": "BFRC",
    "FRC Oscillator": "FRC",
}

global getBitfieldClockOptionList
def getBitfieldClockOptionList(node):
    valueNodes = node.getChildren()
    optionList = []
    for bitfield in valueNodes:   ##  do this for all <value > entries for this bitfield
        dict = {}
        if bitfield.getAttribute("caption").lower() != "reserved" and bitfield.getAttribute("caption") != SERIAL_TEST_MODE_CLOCK:  ##  skip (unused) reserved fields
            name = clkSrcNamesMap.get(bitfield.getAttribute("caption"), bitfield.getAttribute("caption"))
            dict["desc"] = name
            dict["key"] = name

            ##  Get rid of leading '0x', and convert to int if was hex
            value = bitfield.getAttribute("value")

            if(value[:2] == "0x"):
                temp = value[2:]
                tempint = int(temp, 16)
            else:
                tempint = int(value)

            dict["value"] = str(tempint)
            optionList.append(dict)
    return optionList[::-1]

global getAtdfParameterValue
def getAtdfParameterValue(moduleName,instanceName,paramName):
    atdfPath = '/avr-tools-device-file/devices/device/peripherals/module@[name="' + moduleName + '"]/instance@[name="'+ instanceName + '"]/parameters/param@[name="'+paramName +'"]'
    paramNode = ATDF.getNode(atdfPath)
    if(paramNode != None):
        return paramNode.getAttribute("value")
    return None

global getAtdfParameterCaption
def getAtdfParameterCaption(moduleName,instanceName,paramName):
    atdfPath = '/avr-tools-device-file/devices/device/peripherals/module@[name="' + moduleName + '"]/instance@[name="'+ instanceName + '"]/parameters/param@[name="'+paramName +'"]'
    paramNode = ATDF.getNode(atdfPath)
    if(paramNode != None):
        return paramNode.getAttribute("caption")
    return None

global getIntValueForAtdfParam
def getIntValueForAtdfParam(moduleName,instanceName,paramName):
    atdfPath = '/avr-tools-device-file/devices/device/peripherals/module@[name="' + moduleName + '"]/instance@[name="'+ instanceName + '"]/parameters/param@[name="'+paramName +'"]'
    paramNode = ATDF.getNode(atdfPath)
    if(paramNode != None):
        return int(paramNode.getAttribute("value"))
    return 0

global getClkSourceFrequency
def getClkSourceFrequency(component,clkSrc):
    frequency = 0
    if clkSrc in [FRC_OSCILLATOR, BACKUP_FRC_OSCILLATOR]:
        frequency = getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_FRC_CLOCK)
    elif clkSrc == PRIMARY_OSCILLATOR:   
        if component.getSymbolValue(EXT_CLK_SRC_SEL) != NONE:
            frequency = component.getSymbolValue(CALC_EXT_CLK_SRC_FREQ)
    elif clkSrc == LPRC:
        frequency = getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_LPRC_CLOCK)
    elif clkSrc == "REFI1":
        if component.getSymbolValue(REF_INPUT_PIN_ENABLE + "1"):
            frequency = component.getSymbolValue(REF_INPUT_PIN_FREQ + "1")
    elif clkSrc == "REFI2":
        if component.getSymbolValue(REF_INPUT_PIN_ENABLE + "2"):
            frequency = component.getSymbolValue(REF_INPUT_PIN_FREQ + "2")
    elif clkSrc == "PLL1 VCO DIV":
        if component.getSymbolValue(PLL_ENABLE.format(1)) == True:
            frequency = component.getSymbolValue(PLL_CALC_VCO_FREQ.format(1))
    elif clkSrc == "PLL2 VCO DIV":
        if component.getSymbolValue(PLL_ENABLE.format(2)) == True:
            frequency = component.getSymbolValue(PLL_CALC_VCO_FREQ.format(2))
    elif clkSrc == "PLL1 FOUT":
        if component.getSymbolValue(PLL_ENABLE.format(1)) == True:
            frequency = component.getSymbolValue(PLL_CALC_PLLO_FREQ.format(1))
    elif clkSrc == "PLL2 FOUT":
       if component.getSymbolValue(PLL_ENABLE.format(2)) == True:
            frequency = component.getSymbolValue(PLL_CALC_PLLO_FREQ.format(2))

    return frequency

global totalClkGenCount
totalClkGenCount = getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_CLOCK_GENERATOR_SUPPORTED)

global totalRefInputSrcCount
totalRefInputSrcCount = getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_REFERENCE_INPUT_SRC_COUNT)

global totalPllCount
totalPllCount = getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_Pll_GEN_COUNT)

global totalClkMonitorCount
totalClkMonitorCount = getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_CLK_MON_COUNT)

global clkGenFreqInMhzCb
def clkGenFreqInMhzCb(symbol,event):
        symbol.setValue(convertToMHz(event["value"]))

global poscmdCb
def poscmdCb(symbol,event):
    value = 3
    extClkSrc = symbol.getComponent().getSymbolValue(EXT_CLK_SRC_SEL)
    if(extClkSrc != NONE):
        if(extClkSrc == "Primary Oscillator"):
            clkSrcFreq = symbol.getComponent().getSymbolValue(EXT_CLK_SRC_FREQ)
            if(clkSrcFreq > 10000000):
                value =2
        else:
            value =0
    symbol.setValue(value)    
global poscFreqCb
def poscFreqCb(symbol,event):
    extClkSrc = symbol.getComponent().getSymbolValue(EXT_CLK_SRC_SEL)
    value = 0
    if(extClkSrc != NONE):
            value = symbol.getComponent().getSymbolValue(EXT_CLK_SRC_FREQ)
    symbol.setValue(value)                

global primaryClockUsedCb
def primaryClockUsedCb(symbol,event):
    if(event["value"] == NONE):
        symbol.setValue(False)
    else:
        symbol.setValue(True)                

global convertToMHz
def convertToMHz(clkFreq):
    return str(round(clkFreq/1000000.0 ,6))        


global createClkIntSymbol
def createClkIntSymbol(component,symbolName,menuName,defaultAndMaskValue,label):
        clkIntSymbol = component.createIntegerSymbol(symbolName, menuName)
        clkIntSymbol.setLabel(label)
        clkIntSymbol.setDefaultValue(defaultAndMaskValue["defaultValue"])   
        clkIntSymbol.setMin(0)
        clkIntSymbol.setMax(defaultAndMaskValue["maskValue"])  
        clkIntSymbol.setVisible(False)
        return clkIntSymbol

global createKeyValueSettingSymbol
def createKeyValueSettingSymbol(component,symbolName,moduleName,registerGroup,register,bitfield,menuName): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):      
            optionList = getBitfieldClockOptionList(valGroup)   
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolName, menuName )
            valueGroupEntryComp.setLabel(symbolName)
            defaultValue =getSettingBitDefaultValue(moduleName,registerGroup,register,bitfield)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(defaultValue,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            valueGroupEntryComp.setVisible(False)
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp   

global createKeyValueSettingBoscSymbol
def createKeyValueSettingBoscSymbol(component,symbolName,moduleName,registerGroup,register,bitfield,menuName,defaultSrc): 
        valueGroupEntry = getValueGroupName(moduleName,registerGroup,register,bitfield)
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):      
            optionList = getBitfieldClockOptionList(valGroup)   
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolName, menuName )
            valueGroupEntryComp.setLabel(symbolName)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonKey(defaultSrc,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            valueGroupEntryComp.setVisible(False)
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp               

global createKeyValueClkSetSymbol
def createKeyValueClkSetSymbol(component,moduleName,valueGroupEntry,symbolName, menuName):
        valGroup = getValueGroup(moduleName,valueGroupEntry)
        if(valGroup != None):
            symbolKey = valueGroupEntry       
            optionList = getBitfieldOptionList(valGroup)
            valueGroupEntryComp = component.createKeyValueSetSymbol(symbolName, menuName )
            valueGroupEntryComp.setLabel(symbolKey)
            valueGroupEntryComp.setDefaultValue(getKeyValuePairBasedonValue(0,optionList))
            valueGroupEntryComp.setOutputMode("Value")
            valueGroupEntryComp.setDisplayMode("Description")
            addKeystoKeyValueSymbol(valueGroupEntryComp,optionList)
            return  valueGroupEntryComp

global createClkMonHexSymbol       
def createClkMonHexSymbol(component,symbolName,menuName,defaultValue,label):
        clkMonHexSymbol = component.createHexSymbol(symbolName, menuName)
        clkMonHexSymbol.setLabel(label)
        clkMonHexSymbol.setDefaultValue(defaultValue)   
        clkMonHexSymbol.setMin(0x0)
        clkMonHexSymbol.setMax(0xFFFFFFFF)  
        clkMonHexSymbol.setVisible(False)
        return clkMonHexSymbol    

global createClkMonStrSymbol
def createClkMonStrSymbol(component,symbolName,menuName,label,defaultValue,readOnly):    
        clkMonStrSymbol = component.createStringSymbol(symbolName, menuName)
        clkMonStrSymbol.setLabel(label)
        clkMonStrSymbol.setDefaultValue(defaultValue)
        clkMonStrSymbol.setReadOnly(readOnly)
        clkMonStrSymbol.setVisible(False)
        return clkMonStrSymbol

global createClkMonIntegerSymbol
def createClkMonIntegerSymbol(component,symbolName,menuName,label,defaultValue,readOnly):    
        clkMonStrSymbol = component.createIntegerSymbol(symbolName, menuName)
        clkMonStrSymbol.setLabel(label)
        clkMonStrSymbol.setDefaultValue(defaultValue)
        clkMonStrSymbol.setReadOnly(readOnly)
        clkMonStrSymbol.setVisible(False)
        return clkMonStrSymbol    

global createClkBooleanSymbol
def createClkBooleanSymbol(component,symbolName,menuName,label,defaultValue):    
        clkMonBooleanSymbol = component.createBooleanSymbol(symbolName, menuName)
        clkMonBooleanSymbol.setLabel(label)
        clkMonBooleanSymbol.setDefaultValue(defaultValue)
        clkMonBooleanSymbol.setVisible(False)
        return clkMonBooleanSymbol
 
global clkMonEnableCb     
def clkMonEnableCb(symbol,event):
        clkMonNo= symbol.getID()[2]
        clkMonEnable(event[SOURCE],symbol,clkMonNo)
 
global clkMonEnable 
def clkMonEnable(component,useClkMonSymbol,clkMonNo):
        for constant in clk_mon_constants:
                symbolId = constant.format(clkMonNo)
                symbolMon = component.getSymbolByID(symbolId)
                if symbolMon is not None:
                    symbolMon.setVisible(useClkMonSymbol.getValue()) 
        if  useClkMonSymbol.getValue():
            updateMonitorInterruptState(clkMonNo,"M",True) 
            if(component.getSymbolValue(CLK_MON_THRESHOLD_ENABLE_INT.format(clkMonNo))):
                 updateMonitorInterruptState(clkMonNo,"F",True)
            if(component.getSymbolValue(CLK_MON_WARN_ENABLE_INT.format(clkMonNo))):
                 updateMonitorInterruptState(clkMonNo,"W",True)  
            if(component.getSymbolValue(CLK_MON_DATA_READY_ENABLE_INT.format(clkMonNo))):
                 updateMonitorInterruptState(clkMonNo,"R",True)                         
        else :
            updateMonitorInterruptState(clkMonNo,"M",False)
            updateMonitorInterruptState(clkMonNo,"R",False)
            updateMonitorInterruptState(clkMonNo,"F",False)
            updateMonitorInterruptState(clkMonNo,"W",False)          

global clkMonInterruptVisibilityCb
def clkMonInterruptVisibilityCb(symbol,event):
        symbol.setVisible(event["value"])     
         
global updateClkMonRefFreq
def updateClkMonRefFreq(symbol):
    import re
    freq =0
    clkMonNo = symbol.getID()[2]
    clkMonClkSymbol =  symbol.getComponent().getSymbolByID(CM_SEL__WINSEL.format(clkMonNo))
    clkSrc= clkMonClkSymbol.getSelectedKey()
    match = re.match(CLOCK_GENERATOR, clkSrc)
    if(match):   
            clkGenNo = int(clkSrc.replace(CLOCK_GENERATOR,""))         
            freq =  symbol.getComponent().getSymbolValue(CLK_GEN_CALCULATED_FREQ.format(clkGenNo))
    else:
        freq = getClkSourceFrequency(symbol.getComponent(),clkSrc)
    symbol.setValue(freq)
       
global updateClkMonRefFreqCb
def updateClkMonRefFreqCb(symbol,event): 
       updateClkMonRefFreq(symbol)
       
global updateClkMonFreqCb
def updateClkMonFreqCb(symbol,event): 
    updateClkMonFreq(symbol)   
      
global updateClkMonFreq
def updateClkMonFreq(symbol): 
      import re
      clkMonNo = symbol.getID()[2]
      clkMonClkSymbol =  symbol.getComponent().getSymbolByID(CM_SEL__CNTSEL.format(clkMonNo))
      monClkSrc= clkMonClkSymbol.getSelectedKey()
      monClkDivSymbol= symbol.getComponent().getSymbolByID(CM_CON__CNTDIV.format(clkMonNo))
      monClkDiv = int(monClkDivSymbol.getSelectedKey().replace("Divide-by ", ""))
      freq =0
      match = re.match(CLOCK_GENERATOR, monClkSrc)
      if(match):   
             clkGenNo = int(monClkSrc.replace(CLOCK_GENERATOR,""))         
             freq =  symbol.getComponent().getSymbolValue(CLK_GEN_CALCULATED_FREQ.format(clkGenNo))
      else:
          freq = getClkSourceFrequency(symbol.getComponent(),monClkSrc)
      symbol.setValue(freq/monClkDiv)      

global useClkMonCb
def useClkMonCb(symbol,event): 
    useClkMon = False
    for i in range(1, totalClkMonitorCount+1):
        if(symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(i))):
            useClkMon = True
            break
    symbol.setValue(useClkMon)    
    
                 
global MICRO_FACTOR
MICRO_FACTOR = 1000000  


global getCalcTimerWindowPeriodInUs
global getCalcTimerWindowPeriod
global getMonClkSrcFreq
global extClkSrcSelCb
global clkPllEnableCb
global clkPllEnable
global clkPllBackUpClkSrcCb
global pllClkSrcChangeCb
global pllVcoDivFreqCb
global calcPllVcoDivFreq
global plloFreqCb
global calcPlloFreq
global clkGenBackUpClkSrcCb
global clkDivBasedCb
global clkGenFreqCb
global calcClkGenFreq
global systemClkCb
global stdSpeedCb
global slowSpeedCb


global getFormattedFrequency
def getFormattedFrequency(frequency):
    MEGA_HERTZ = 1000000.0
    KILO_HERTZ = 1000.0
    if frequency >= MEGA_HERTZ:
        decimalDigits = 6
        formatted_frequency = round(frequency / MEGA_HERTZ, decimalDigits)
        return str(formatted_frequency) + " MHz"
    else:
        decimalDigits = 3
        formatted_frequency = round(frequency / KILO_HERTZ, decimalDigits)
        return str(formatted_frequency) + " kHz"

global calcTmrWindowCb 
def calcTmrWindowCb(symbol,event):
    calcTmrWindow(symbol)

global calcTmrWindow 
def calcTmrWindow(symbol):
    clkMonNo = symbol.getID()[2]
    clkSrcFreq = symbol.getComponent().getSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(clkMonNo))
    winpr = symbol.getComponent().getSymbolValue(CLK_MON_ACCUMULATION_WINDOW.format(clkMonNo))
    symbol.setValue(str(getCalcTimerWindowPeriodInUs(clkSrcFreq,winpr)) + " us")

def getCalcTimerWindowPeriodInUs(clkSrcFreq, windowPeriod):
    if clkSrcFreq:
        return round(((windowPeriod + 1) * MICRO_FACTOR) / clkSrcFreq, 6)
    return 0

def getCalcTimerWindowPeriod(clkSrcFreq, windowPeriod):
    if clkSrcFreq:
        return (windowPeriod + 1) / clkSrcFreq
    return 0

def getMonClkSrcFreq(refClkSrcFreq, windowPeriod, monClkCountVal):
    return (refClkSrcFreq * monClkCountVal) / ((windowPeriod + 1)*1.0) 

global updateClkMonBufCountCb
def updateClkMonBufCountCb(symbol,event):
    updateClkMonBufCount(symbol)

global updateClkMonBufCount
def updateClkMonBufCount(symbol):
    clkMonNo = symbol.getID()[2]
    refClkFreq = symbol.getComponent().getSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(clkMonNo))
    winpr = symbol.getComponent().getSymbolValue(CLK_MON_ACCUMULATION_WINDOW.format(clkMonNo))
    monClkFreq = symbol.getComponent().getSymbolValue(CLK_MON_CLK_SRC_FREQ.format(clkMonNo))
    bufCountVal = hex(int(round(((winpr+1)*monClkFreq)/refClkFreq))) if refClkFreq != 0 else 0
    symbol.setValue(str(bufCountVal))  
    

    
    
global clkMonWarningRangeCb
def clkMonWarningRangeCb(symbol,event):
    clkMonNo = symbol.getID()[2]
    if symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMonNo)):
        refClkFreq = symbol.getComponent().getSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(clkMonNo))
        winpr = symbol.getComponent().getSymbolValue(CLK_MON_ACCUMULATION_WINDOW.format(clkMonNo))
        lowWarnValue = symbol.getComponent().getSymbolValue(CLK_MON_WARN_LOW_COUNT.format(clkMonNo))
        highWarnValue = symbol.getComponent().getSymbolValue(CLK_MON_WARN_HIGH_COUNT.format(clkMonNo))
        warnLowFreq = getFormattedFrequency(getMonClkSrcFreq(refClkFreq,winpr,int(lowWarnValue)))
        warnHighFreq = getFormattedFrequency(getMonClkSrcFreq(refClkFreq,winpr,int(highWarnValue)))  
        symbol.setValue(warnLowFreq + "<=Freq<=" + warnHighFreq) 
        if symbol.getComponent().getSymbolValue(CLK_MON_WARN_ENABLE_INT.format(clkMonNo)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False) 
    else:
        symbol.setVisible(False)       

global clkMonThresholdRangeCb
def clkMonThresholdRangeCb(symbol,event):
    clkMonNo = symbol.getID()[2]
    if symbol.getComponent().getSymbolValue(CLK_MON_ENABLE.format(clkMonNo)):
        refClkFreq = symbol.getComponent().getSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(clkMonNo))
        winpr = symbol.getComponent().getSymbolValue(CLK_MON_ACCUMULATION_WINDOW.format(clkMonNo))
        lowValue = symbol.getComponent().getSymbolValue(CLK_MON_THRESHOLD_LOW_COUNT.format(clkMonNo))
        highValue = symbol.getComponent().getSymbolValue(CLK_MON_THRESHOLD_HIGH_COUNT.format(clkMonNo))
        warnLowFreq = getFormattedFrequency(getMonClkSrcFreq(refClkFreq,winpr,int(lowValue)))
        warnHighFreq = getFormattedFrequency(getMonClkSrcFreq(refClkFreq,winpr,int(highValue))) 
        symbol.setValue(warnLowFreq + "<=Freq<=" + warnHighFreq)
        if symbol.getComponent().getSymbolValue(CLK_MON_THRESHOLD_ENABLE_INT.format(clkMonNo)):
            symbol.setVisible(True)
        else:
            symbol.setVisible(False)    
    else:
        symbol.setVisible(False) 
    
#PLL Callback functions
def clkPllEnableCb(symbol, event):
    clkPllNo = symbol.getID()[3]
    clkPllEnable(event["source"], symbol, clkPllNo) 

def clkPllEnable(component, enablePllSymbol, clkPllNo):
    enablePllStatus = enablePllSymbol.getValue()
    for constant in pll_constants:
        symbolId = constant.format(clkPllNo) 
        symbolMon = component.getSymbolByID(symbolId)
        # if symbolMon is not None:
        #     symbolMon.setReadOnly(not enablePllStatus)                   

def pllClkSrcChangeCb(symbol, event):   
    pllNo = symbol.getID()[3]  
    component = symbol.getComponent()
    clkSrc = component.getSymbolByID(PLL_CLOCK_SOURCE.format(pllNo)).getSelectedKey()
    value = getClkSourceFrequency(component, clkSrc) if component.getSymbolValue(PLL_ENABLE.format(pllNo)) else 0
    symbol.setValue(value)
global clkGenClkSrcChangeCb
def clkGenClkSrcChangeCb(symbol, event):   
    clkSrc = symbol.getComponent().getSymbolByID(event["id"]).getSelectedKey()
    symbol.setValue(getClkSourceFrequency(symbol.getComponent(), clkSrc))
                        
def pllVcoDivFreqCb(symbol, event):
    pllNo = symbol.getID()[3]
    component = symbol.getComponent()
    if event["id"] == PLL_CALC_VCO_FREQ.format(pllNo):
        clkSrc = "PLL" + pllNo + " VCO DIV"
        clkFreq = event["value"]
        updateClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq)
    else : 
        value = calcPllVcoDivFreq(component, pllNo) if component.getSymbolValue(PLL_ENABLE.format(pllNo)) else 0
        symbol.setValue(value)

global pllPfdDivFreqCb         
def pllPfdDivFreqCb(symbol, event):
    pllNo = symbol.getID()[3]
    component = symbol.getComponent() 
    value = calcPllVcoPfdFreq(component, pllNo) if component.getSymbolValue(PLL_ENABLE.format(pllNo)) else 0
    symbol.setValue(value)  
    
global calcPllVcoPfdFreq
def calcPllVcoPfdFreq(component, pllNo):
    pllClkSrcFreq = component.getSymbolValue(PLL_CLOCK_SOURCE_FREQ.format(pllNo))
    pllPre = component.getSymbolValue(PLLPRE.format(pllNo))
    pllFbd = component.getSymbolValue(PLLFBD.format(pllNo))
    pllVcoPfdFreq = 0
    if pllPre > 0 :
        pllVcoPfdFreq = (pllClkSrcFreq * pllFbd) / (pllPre)   
    return pllVcoPfdFreq 
          
def calcPllVcoDivFreq(component, pllNo):
    pllClkSrcFreq = component.getSymbolValue(PLL_CLOCK_SOURCE_FREQ.format(pllNo))
    pllPre = component.getSymbolValue(PLLPRE.format(pllNo))
    pllFbd = component.getSymbolValue(PLLFBD.format(pllNo))
    pllVcoDivSymbolVal = component.getSymbolValue(PLL_INTDIV.format(pllNo))
    pllVcoDiv = 2 * (pllVcoDivSymbolVal) if pllVcoDivSymbolVal > 0 else 1
    pllVcoDivFreq = 0
    if pllPre > 0 and pllVcoDiv > 0:
        pllVcoDivFreq = (pllClkSrcFreq * pllFbd) / (pllPre * pllVcoDiv)   
    return pllVcoDivFreq      

def plloFreqCb(symbol, event):
    component = symbol.getComponent() 
    pllNo = symbol.getID()[3]
    if event["id"] == PLL_CALC_PLLO_FREQ.format(pllNo):
        clkSrc = "PLL" + pllNo + " FOUT"
        clkFreq = event["value"]
        updateClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq)
    else :
        value = calcPlloFreq(component, pllNo) if component.getSymbolValue(PLL_ENABLE.format(pllNo)) else 0
        symbol.setValue(value)
       
def calcPlloFreq(component, pllNo):
    pllClkSrcFreq = component.getSymbolValue(PLL_CLOCK_SOURCE_FREQ.format(pllNo))
    pllPre = component.getSymbolValue(PLLPRE.format(pllNo))
    pllFbd = component.getSymbolValue(PLLFBD.format(pllNo))
    postDiv1 = int(component.getSymbolValue(POSTDIV1.format(pllNo)))  
    postDiv2 = int(component.getSymbolValue(POSTDIV2.format(pllNo)))
    plloFreq = 0
    if pllPre > 0 and postDiv1 > 0 and postDiv2 > 0:
        plloFreq = (pllClkSrcFreq * pllFbd) / (pllPre * postDiv1 * postDiv2)
    return plloFreq 

def clkPllBackUpClkSrcCb(symbol, event):
    component = symbol.getComponent()
    pllNo = symbol.getID()[3]
    enablePllVal = component.getSymbolValue(PLL_ENABLE.format(pllNo))
    pllFailSafeEnableVal = component.getSymbolValue(PLL_FAIL_SAFE_CLK_ENABLE.format(pllNo))
    failSafeEnableBit = component.getSymbolByID(PLL_FSCMEN.format(pllNo))
    if pllFailSafeEnableVal == True:
           failSafeEnableBit.setSelectedKey("enabled")
    else :
        failSafeEnableBit.setSelectedKey("disabled")
    # symbol.setReadOnly(not enablePllVal and not pllFailSafeEnableVal)  

# Clock Gen callback functions
def clkGenBackUpClkSrcCb(symbol, event):
    component = symbol.getComponent()
    clkPllNo = getClkGenNo(symbol.getID())
    clkGenFailSafeEnableVal = component.getSymbolValue(CLK_GEN_ENABLE_FAIL_SAFE.format(clkPllNo))
    failSafeEnableBit = component.getSymbolByID(CLK_GEN_FSCMEN.format(clkPllNo))

    if clkGenFailSafeEnableVal == True:
           failSafeEnableBit.setSelectedKey("enabled")
    else :
        failSafeEnableBit.setSelectedKey("disabled")       
    # symbol.setVisible(clkGenFailSafeEnableVal)      

def clkDivBasedCb(symbol, event):
    symbol.setVisible(event["value"])  

def clkGenFreqCb(symbol, event):
    component = symbol.getComponent()
    clkGenNo = getClkGenNo(symbol.getID())
    if(event["id"] == CLK_GEN_CALCULATED_FREQ.format(clkGenNo)):
        clkSrc = "Clock Generator " + clkGenNo
        clkFreq = event["value"]
        updateClkGenBasedClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq)  
    else:
        symbol.setValue(calcClkGenFreq(component, clkGenNo))
 
global clkGenFreqCmntCb
def clkGenFreqCmntCb(symbol, event): 
    MHz_Factor =1000000 
    clkGenNo = getClkGenNo(symbol.getID())
    maxAllowableFreq = getAtdfParameterCaption(INTERNAL_OSCILLATOR,CLOCK,"CLK_GEN_"+clkGenNo)
    clkGenDescription = "Clock Generator" if clkGenNo!= "1" else "System Clock"       
    clkGenFreq = symbol.getComponent().getSymbolValue(CLK_GEN_CALCULATED_FREQ.format(clkGenNo))
    if((int(maxAllowableFreq)*MHz_Factor) < clkGenFreq):
        symbol.setLabel("Warning!!! Ensure {} Frequency <= {}MHz".format(clkGenDescription,maxAllowableFreq))
    else:
        symbol.setLabel("Info : {} frequency limit is {}MHz".format(clkGenDescription,maxAllowableFreq))    
    
def calcClkGenFreq(component, clkGenNo):
    clkSrcFreq = component.getSymbolValue(CLK_GEN_CLK_SRC_FREQ.format(clkGenNo))
    isClkDivEnabled = component.getSymbolValue(CLK_GEN_DIVIDER_ENABLE.format(clkGenNo))
    if isClkDivEnabled:
        intdiv = component.getSymbolValue(CLK_GEN_INTDIV.format(clkGenNo))
        fracDiv = component.getSymbolValue(CLK_GEN_FRACDIV.format(clkGenNo))
        if intdiv != 0:
            return int(clkSrcFreq / (2 * (intdiv + float(fracDiv) / float(FRACDIV_CYCLE_COUNT))))
    return clkSrcFreq  

def systemClkCb(symbol, event):
    symbol.setValue(event["value"]) 

def stdSpeedCb(symbol, event):
    symbol.setValue(event["value"] / 2)      

def slowSpeedCb(symbol, event):
    symbol.setValue(event["value"] / 4)    
  
global sysClkSrcCb    
def sysClkSrcCb(symbol, event): 
    clkSrcSymbol = symbol.getComponent().getSymbolByID(event["id"])   
    symbol.setValue(clkSrcSymbol.getSelectedKey()) 

global sysFreqInMHzCb
def sysFreqInMHzCb(symbol, event):    
    symbol.setValue(event["value"])   
    
global getClkGenPaneName
def getClkGenPaneName(clkGenNo):
    paneName = "Clock Generator " + str(clkGenNo)
    if clkGenNo == 1:
        return paneName
    elif clkGenNo == 2:
        return paneName + " (FRC)"
    elif clkGenNo == 3:
        return paneName + " (BFRC)"
    else:
        paramName = "CLK_GEN_"+str(clkGenNo)
        paramValue= getAtdfParameterValue(INTERNAL_OSCILLATOR,CLOCK,paramName)
        if paramValue:
            return paneName + " (Clock Input for {})".format(paramValue)
        return paneName
         
    
global updateClkSrcFreq
def updateClkSrcFreq(coreComponent,clkSrc,clkSrcFreq):
    for i in range(1, totalPllCount+1):
        if coreComponent.getSymbolValue(PLL_ENABLE.format(i)):
            clkSymbol =  coreComponent.getSymbolByID(PLL_CLOCK_SOURCE.format(i))
            if(clkSymbol != None and clkSymbol.getSelectedKey() == clkSrc):             
                coreComponent.setSymbolValue(PLL_CLOCK_SOURCE_FREQ.format(i),clkSrcFreq)
    for j in range(1, totalClkGenCount+1):
        clkSymbol =  coreComponent.getSymbolByID(CLK_GEN_NOSC.format(j))
        if(clkSymbol != None and clkSymbol.getSelectedKey() == clkSrc):
            coreComponent.setSymbolValue(CLK_GEN_CLK_SRC_FREQ.format(j),clkSrcFreq)  
    for k in range(1, totalClkMonitorCount+1):
        clkMonRefClkSymbol =  coreComponent.getSymbolByID(CM_SEL__WINSEL.format(k))
        if(clkMonRefClkSymbol != None and clkMonRefClkSymbol.getSelectedKey() == clkSrc):
            coreComponent.setSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(k),clkSrcFreq)   
        clkMonClkSymbol =  coreComponent.getSymbolByID(CM_SEL__CNTSEL.format(k))
        if(clkMonClkSymbol != None and clkMonClkSymbol.getSelectedKey() == clkSrc):
            monClkDivSymbol= coreComponent.getSymbolByID(CM_CON__CNTDIV.format(k))
            monClkDiv = int(monClkDivSymbol.getSelectedKey().replace("Divide-by ", ""))
            coreComponent.setSymbolValue(CLK_MON_CLK_SRC_FREQ.format(k),clkSrcFreq/monClkDiv) 

global updateClkGenBasedClkSrcFreq
def updateClkGenBasedClkSrcFreq(coreComponent,clkSrc,clkSrcFreq): 
    for k in range(1, totalClkMonitorCount+1):
        clkMonRefClkSymbol =  coreComponent.getSymbolByID(CM_SEL__WINSEL.format(k))
        if(clkMonRefClkSymbol != None and clkMonRefClkSymbol.getSelectedKey() == clkSrc):
            coreComponent.setSymbolValue(CLK_MON_REF_CLK_SRC_FREQ.format(k),clkSrcFreq)   
        clkMonClkSymbol =  coreComponent.getSymbolByID(CM_SEL__CNTSEL.format(k))
        if(clkMonClkSymbol != None and clkMonClkSymbol.getSelectedKey() == clkSrc):
            monClkDivSymbol= coreComponent.getSymbolByID(CM_CON__CNTDIV.format(k))
            monClkDiv = int(monClkDivSymbol.getSelectedKey().replace("Divide-by ", ""))
            coreComponent.setSymbolValue(CLK_MON_CLK_SRC_FREQ.format(k),clkSrcFreq/monClkDiv)                     

global refInputValUpdateCb
def refInputValUpdateCb(symbol,event):
    clkEnableStatus = event["value"]
    clkSrc = "REFI" + event["id"][-1]
    refClkSrcFreqSymbol = symbol.getComponent().getSymbolByID(REF_INPUT_PIN_FREQ +event["id"][-1])
    clkFreq = refClkSrcFreqSymbol.getValue() if clkEnableStatus else 0
    refClkSrcFreqSymbol.setVisible(clkEnableStatus)
    updateClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq) 
global referenceInputFreqCb
def referenceInputFreqCb(symbol,event):
    clkSrc = "REFI" + event["id"][-1]
    clkEnableStatus = symbol.getComponent().getSymbolValue(REF_INPUT_PIN_ENABLE +event["id"][-1])
    clkFreq = event["value"] if clkEnableStatus else 0
    updateClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq)  
global referenceInputDisplayFreqCb
def referenceInputDisplayFreqCb(symbol,event):
    clkEnableStatus = symbol.getComponent().getSymbolValue(REF_INPUT_PIN_ENABLE +event["id"][-1])
    clkFreq = symbol.getComponent().getSymbolValue(REF_INPUT_PIN_FREQ +event["id"][-1]) if clkEnableStatus else 0
    symbol.setValue(clkFreq)

global extClkSrcFreqCb
def extClkSrcFreqCb(symbol,event):
    symbol.getComponent().setSymbolValue(CALC_EXT_CLK_SRC_FREQ ,event["value"])

global calcExtClkSrcFreqCb
def calcExtClkSrcFreqCb(symbol,event):
    clkSrc = PRIMARY_OSCILLATOR
    clkFreq = event["value"]
    updateClkSrcFreq(symbol.getComponent(),clkSrc,clkFreq)     
             
def extClkSrcSelCb(symbol, event):
    extClkSrcFreqSymbol = symbol.getComponent().getSymbolByID(EXT_CLK_SRC_FREQ)
    calcExtClkSrcFreq = symbol.getComponent().getSymbolByID(CALC_EXT_CLK_SRC_FREQ)
    if event["value"] == "None":
        extClkSrcFreqSymbol.setVisible(False)                                  
        calcExtClkSrcFreq.setValue(0)
    elif event["value"] == "Primary Oscillator":
        extClkSrcFreqSymbol.setVisible(True)       
        extClkSrcFreqSymbol.setMin(getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_MIN_PRIMARY_OSC_XT_FREQ))
        extClkSrcFreqSymbol.setMax(getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_MAX_PRIMARY_OSC_HS_FREQ))  
        calcExtClkSrcFreq.setValue(extClkSrcFreqSymbol.getValue())
    elif event["value"] == "External Clock":
        extClkSrcFreqSymbol.setVisible(True)        
        extClkSrcFreqSymbol.setMin(getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_MIN_EXTERNAL_OSC_FREQ))
        extClkSrcFreqSymbol.setMax(getIntValueForAtdfParam(INTERNAL_OSCILLATOR, CLOCK, PARAM_MAX_EXTERNAL_OSC_FREQ))  
        calcExtClkSrcFreq.setValue(extClkSrcFreqSymbol.getValue())                 

global clkEnableCb    
def clkEnableCb(symbol, event):
    clkGenNo = getClkGenNo(symbol.getID())
    clkGenEnable(event["source"], symbol, clkGenNo) 

global clkGenEnable
def clkGenEnable(component, enableClkGenSymbol, clkGenNo):
    # for constant in clk_gen_constants:
    #     symbolId = constant.format(clkGenNo) 
        # symbolMon = component.getSymbolByID(symbolId)
        # if symbolMon is not None:
        #     symbolMon.setVisible(enableClkGenSymbol.getValue()) 
    if  enableClkGenSymbol.getValue() == False :
            component.setSymbolValue(CLK_GEN_CALCULATED_FREQ.format(clkGenNo),0)   
    else :
        clkGenFreq = calcClkGenFreq(component,clkGenNo)
        component.setSymbolValue(CLK_GEN_CALCULATED_FREQ.format(clkGenNo),clkGenFreq)  

global split_string_by_and_comma
def split_string_by_and_comma(clk_gen_module_names):
    import re
    # Delimiting the string by `comma`, `and` and `/`
    return [re.sub(r'\s+', '_', part.strip()) for part in re.split(r',|and|/', clk_gen_module_names)]                


global useClkGen 
def useClkGen(symbol): 
    enumStr = ""
    enumStrDataInListFormat = []
    for i in range(1, totalClkGenCount+1):
        if(symbol.getComponent().getSymbolValue(CLK_GEN_ENABLE.format(i))):
            clk_gen_module_names = getAtdfParameterValue(INTERNAL_OSCILLATOR, CLOCK,"CLK_GEN_"+str(i))
            moduleNameList = ["System"]
            if i != 1:
                moduleNameList = split_string_by_and_comma(clk_gen_module_names)           
            for module in moduleNameList:  
                    enumStrDataInListFormat.append("    CLOCK_{} = {},".format(module.upper(),str(i)))                  
    lastEntry = enumStrDataInListFormat.pop() 
    for entry in enumStrDataInListFormat:
        enumStr += entry + "\n"
    enumStr += lastEntry.replace(",", "")              
    symbol.setValue(enumStr) 
    
global useClkGenCb 
def useClkGenCb(symbol, event):
    useClkGen(symbol)
    
global clockOutputPinCb
def clockOutputPinCb(symbol, event):
    if(event["value"] == "Primary Oscillator"): 
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)  

global codeGenClkOpPinCb            
def codeGenClkOpPinCb(symbol, event):
    extClkSrcSel = symbol.getComponent().getSymbolValue(EXT_CLK_SRC_SEL)
    if extClkSrcSel == "Primary Oscillator": 
        symbol.setValue(False)
    elif(symbol.getComponent().getSymbolValue("clockOutputPin")):
        symbol.setValue(True)
    else:
        symbol.setValue(False)    
                              
global pll_mul_div_ranges                              
pll_mul_div_ranges = {
    "fbdiv_max": getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"PLLFBDIV")["maskValue"],
    "fbdiv_min": getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,"MIN_PLL_FEEDBACK_DIV"),
    "pllpre_max": getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"PLLPRE")["maskValue"],
    "postdiv1_max": getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"POSTDIV1")["maskValue"],
    "postdiv2_max": getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"POSTDIV2")["maskValue"],
    "vcodiv_max": getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,VCO_REG_GROUP,PLL_REG_DIV,"INTDIV")["maskValue"]
} 
global pll_freq_ranges
pll_freq_ranges = {
    "minVcoInterimFreq": getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,"MIN_PLL_VCO_INTERIM_FREQ_HZ"),
    "maxVcoInterimFreq": getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,"MAX_PLL_VCO_INTERIM_FREQ_HZ"),
    "minPlloFreq": getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,"MIN_PLLO_FREQ_HZ"),
    "maxPlloFreq": getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,"MAX_PLLO_FREQ_HZ")
}
global round_up_to_next_number
def round_up_to_next_number(n):
    if int(n) == n:
        return int(n)
    else:
        return int(n) + 1
global round_up_to_prev_number        
def round_up_to_prev_number(n):
    if int(n) == n:
        return int(n)
    else:
        return int(n) -1  
global getPlloFreqParams
def getPlloFreqParams(pllNo,clkSrcFreq, reqPlloOutFreq, pll_mul_div_ranges, pll_freq_ranges):
    fbdiv_max = pll_mul_div_ranges["fbdiv_max"]
    fbdiv_min = pll_mul_div_ranges["fbdiv_min"]
    pllpre_max = pll_mul_div_ranges["pllpre_max"]
    postdiv1_max = pll_mul_div_ranges["postdiv1_max"]
    postdiv2_max = pll_mul_div_ranges["postdiv2_max"]
    vcodiv_max = pll_mul_div_ranges["vcodiv_max"]
    min_vco_interim_freq = pll_freq_ranges["minVcoInterimFreq"]
    max_vco_interim_freq = pll_freq_ranges["maxVcoInterimFreq"]
    min_pllo_freq = pll_freq_ranges["minPlloFreq"]
    max_pllo_freq = pll_freq_ranges["maxPlloFreq"]
    smallest_difference = -1
    pllpreVal = 1
    fbdivVal = 200
    postdiv1Val = 1
    postdiv2Val = 1
    fvcoVal = 0
    calcPlloFreqVal = 0
    for pllpre in range(1, pllpre_max + 1):
        minFbdivForPllpre_1 = max(round_up_to_next_number((min_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_min)
        maxFbdivForPllpre_1 = min(round_up_to_prev_number((max_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_max)
        for fbdiv in range(minFbdivForPllpre_1, (maxFbdivForPllpre_1 + 1)):
            interim_freq = (clkSrcFreq * fbdiv) / pllpre
            if min_vco_interim_freq <= interim_freq <= max_vco_interim_freq:
                div_factor = round((clkSrcFreq * fbdiv) / (reqPlloOutFreq *pllpre))
                for postdiv1 in range(postdiv1_max, 0, -1):  # Iterate in reverse
                    postdiv2 = 1
                    val = round(float(div_factor) / postdiv1)
                    if val >= postdiv1:
                        postdiv2 = postdiv1
                    elif val <= 1:
                        postdiv2 = 1
                    else:
                        postdiv2 = val    
                    calculated_output_freq = (clkSrcFreq * fbdiv) / (pllpre *postdiv1 * postdiv2)
                    if min_pllo_freq <= calculated_output_freq <= max_pllo_freq:
                                difference = abs(calculated_output_freq - reqPlloOutFreq)
                                if difference == 0:
                                    return {
                                        PLLPRE.format(pllNo):pllpre,
                                        PLLFBD.format(pllNo) :fbdiv,
                                        POSTDIV1.format(pllNo):str(postdiv1),
                                        POSTDIV2.format(pllNo):str(postdiv2),
                                        "calcPlloFreq":calculated_output_freq
                                    }
                                if difference < smallest_difference or smallest_difference== -1:
                                    smallest_difference = difference
                                    pllpreVal=pllpre
                                    fbdivVal =fbdiv
                                    postdiv1Val=postdiv1
                                    postdiv2Val=postdiv2
                                    calcPlloFreqVal=calculated_output_freq
    return {
        PLLPRE.format(pllNo):pllpreVal,
        PLLFBD.format(pllNo) :fbdivVal,
        POSTDIV1.format(pllNo):str(postdiv1Val),
        POSTDIV2.format(pllNo):str(postdiv2Val),
        "calcPlloFreq":calcPlloFreqVal
        }
    
global getPllVcoDivParams
def getPllVcoDivParams(pllNo,clkSrcFreq, reqVcoDivFreq, pll_mul_div_ranges, pll_freq_ranges):
    fbdiv_max = pll_mul_div_ranges["fbdiv_max"]
    fbdiv_min = pll_mul_div_ranges["fbdiv_min"]
    pllpre_max = pll_mul_div_ranges["pllpre_max"]
    vcodiv_max = pll_mul_div_ranges["vcodiv_max"]
    min_vco_interim_freq = pll_freq_ranges["minVcoInterimFreq"]
    max_vco_interim_freq = pll_freq_ranges["maxVcoInterimFreq"]
    closest_combination = None
    smallest_difference = -1
    pllpreVal = 1
    fbdivVal = 200
    vcodivVal = 1
    fvcoVal = 0
    calcVcoDivFreqVal = 0
    for pllpre in range(1, pllpre_max + 1):
        minFbdivForPllpre_1 = max(round_up_to_next_number((min_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_min)
        maxFbdivForPllpre_1 = min(round_up_to_prev_number((max_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_max)
        for fbdiv in range(minFbdivForPllpre_1, (maxFbdivForPllpre_1 + 1)):
            interim_freq = (clkSrcFreq * fbdiv) / pllpre
            if min_vco_interim_freq <= interim_freq <= max_vco_interim_freq:
                vcoDiv = 0
                if (reqVcoDivFreq < (interim_freq * 3) / 4) :
                    vcoDiv = round((clkSrcFreq * fbdiv) / (reqVcoDivFreq *pllpre*2))
                    if vcoDiv > vcodiv_max:
                        vcoDiv = vcodiv_max
                divideFactor = vcoDiv*2 if  vcoDiv > 0 else 1       
                calculated_output_freq = (clkSrcFreq * fbdiv) / (pllpre*divideFactor)    
                difference = abs(calculated_output_freq - reqVcoDivFreq)
                if difference == 0:
                    return {
                        PLLPRE.format(pllNo):pllpre,
                        PLLFBD.format(pllNo) :fbdiv,
                        PLL_INTDIV.format(pllNo):vcoDiv,
                        "calcPllVcoDivFreq":calculated_output_freq
                    }
                if difference < smallest_difference or smallest_difference== -1:
                    smallest_difference = difference
                    pllpreVal=pllpre
                    fbdivVal =fbdiv
                    vcodivVal = vcoDiv
                    calcVcoDivFreqVal=calculated_output_freq
    return {
        PLLPRE.format(pllNo):pllpreVal,
        PLLFBD.format(pllNo) :fbdivVal,
        PLL_INTDIV.format(pllNo):vcodivVal,
        "calcPllVcoDivFreq":calcVcoDivFreqVal
        }
    
global getVcodivFactor    
def getVcodivFactor(maxVcodiv,reqVcodivfreq,clkSrcFreq,vcoFreq,pllpre,fbdiv):
    vcoDiv = 0
    if (reqVcodivfreq < (vcoFreq * 3) / 4) :
        vcoDiv = round((clkSrcFreq * fbdiv) / (reqVcodivfreq *pllpre*2))
        if vcoDiv > maxVcodiv:
            vcoDiv = maxVcodiv
    divideFactor = vcoDiv*2 if  vcoDiv > 0 else 1       
    calculated_output_freq = (clkSrcFreq * fbdiv) / (pllpre*divideFactor)    
    difference = abs(calculated_output_freq - reqVcodivfreq)
    return {
        "vcodiv" : vcoDiv,
        "vcoFreq": calculated_output_freq,
        "vcoFreqDiff" : difference 
    }  
      
global getPlloandVcoFreqParams
def getPlloandVcoFreqParams(pllNo,clkSrcFreq, plloOutFreq, vcoDivFreq, pll_mul_div_ranges, pll_freq_ranges):
    fbdiv_max = pll_mul_div_ranges["fbdiv_max"]
    fbdiv_min = pll_mul_div_ranges["fbdiv_min"]
    pllpre_max = pll_mul_div_ranges["pllpre_max"]
    postdiv1_max = pll_mul_div_ranges["postdiv1_max"]
    postdiv2_max = pll_mul_div_ranges["postdiv2_max"]
    vcodiv_max = pll_mul_div_ranges["vcodiv_max"]
    min_vco_interim_freq = pll_freq_ranges["minVcoInterimFreq"]
    max_vco_interim_freq = pll_freq_ranges["maxVcoInterimFreq"]
    min_pllo_freq = pll_freq_ranges["minPlloFreq"]
    max_pllo_freq = pll_freq_ranges["maxPlloFreq"]
    smallest_Pllo_difference = -1
    smallest_Vcodiv_difference = -1
    isPlloFreqAchieved = False 
    pllpreVal = 1
    fbdivVal = 200
    postdiv1Val = 4
    postdiv2Val = 2
    vcodivVal = 1 
    calcPlloFreqVal = 0
    calcPllVcoDivFreqVal =0  
    for pllpre in range(1, pllpre_max + 1):
        minFbdivForPllpre_1 = max(round_up_to_next_number((min_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_min)
        maxFbdivForPllpre_1 = min(round_up_to_prev_number((max_vco_interim_freq*pllpre) / float(clkSrcFreq)), fbdiv_max)
        for fbdiv in range(minFbdivForPllpre_1, (maxFbdivForPllpre_1 + 1)):            
            interim_freq = (clkSrcFreq * fbdiv) / pllpre
            if min_vco_interim_freq <= interim_freq <= max_vco_interim_freq:
                div_factor = round((clkSrcFreq * fbdiv) / (plloOutFreq *pllpre))
                for postdiv1 in range(postdiv1_max, 0, -1):  # Iterate in reverse
                    postdiv2 = 1
                    val = round(float(div_factor) / postdiv1)
                    if val >= postdiv1:
                        postdiv2 = postdiv1
                    elif val <= 1:
                        postdiv2 = 1
                    else:
                        postdiv2 = val
                    calculated_output_freq = (clkSrcFreq * fbdiv) / (pllpre *postdiv1 * postdiv2)
                    if min_pllo_freq <= calculated_output_freq <= max_pllo_freq:
                                difference = abs(calculated_output_freq - plloOutFreq)
                                if difference == 0: 
                                    isPlloFreqAchieved = True                        
                                    vcoDivParams = getVcodivFactor(vcodiv_max,vcoDivFreq,clkSrcFreq,interim_freq,pllpre,fbdiv)
                                    if vcoDivParams["vcoFreqDiff"] == 0:
                                        return {                                    
                                            PLLPRE.format(pllNo):pllpre,
                                            PLLFBD.format(pllNo) :fbdiv,
                                            POSTDIV1.format(pllNo):str(postdiv1),
                                            POSTDIV2.format(pllNo):str(postdiv2),
                                            PLL_INTDIV.format(pllNo): vcoDivParams["vcodiv"],
                                            "calcPlloFreq": calculated_output_freq,
                                            "calcPllVcoDivFreq" :vcoDivParams["vcoFreq"]                              
                                        }
                                    elif vcoDivParams["vcoFreqDiff"] < smallest_Vcodiv_difference or smallest_Vcodiv_difference== -1:
                                        smallest_Vcodiv_difference = vcoDivParams["vcoFreqDiff"] 
                                        pllpreVal=pllpre
                                        fbdivVal =fbdiv
                                        postdiv1Val=postdiv1
                                        postdiv2Val=postdiv2
                                        calcPlloFreqVal = calculated_output_freq
                                        vcodivVal =  vcoDivParams["vcodiv"]     
                                        calcPllVcoDivFreqVal = vcoDivParams["vcoFreq"]  
                                elif not isPlloFreqAchieved and (difference <= smallest_Pllo_difference or smallest_Pllo_difference== -1):
                                    vcoDivParams = getVcodivFactor(vcodiv_max,vcoDivFreq,clkSrcFreq,interim_freq,pllpre,fbdiv)
                                    updatepllVcoCombination = True
                                    if difference == smallest_Pllo_difference:                                       
                                        if vcoDivParams["vcoFreqDiff"] >= smallest_Vcodiv_difference:
                                            updatepllVcoCombination = False
                                    if updatepllVcoCombination:        
                                        smallest_Vcodiv_difference = vcoDivParams["vcoFreqDiff"]
                                        smallest_Pllo_difference = difference
                                        pllpreVal=pllpre
                                        fbdivVal =fbdiv
                                        postdiv1Val=postdiv1
                                        postdiv2Val=postdiv2
                                        vcodivVal =  vcoDivParams["vcodiv"]
                                        calcPlloFreqVal = calculated_output_freq
                                        calcPllVcoDivFreqVal = vcoDivParams["vcoFreq"]
    return {
        PLLPRE.format(pllNo):pllpreVal,
        PLLFBD.format(pllNo) :fbdivVal,
        POSTDIV1.format(pllNo):str(postdiv1Val),
        POSTDIV2.format(pllNo):str(postdiv2Val),
        PLL_INTDIV.format(pllNo):vcodivVal,
        "calcPlloFreq": calcPlloFreqVal,
        "calcPllVcoDivFreq" :calcPllVcoDivFreqVal
        }
  
global getCalcPlloFreq
def getCalcPlloFreq(inputClkSrc, pllpre,fbdiv,postdiv1,postdiv2):
    return (inputClkSrc*fbdiv)/(pllpre*postdiv1*postdiv2)  

global getCalcVcoFreq
def getCalcVcoFreq(inputClkSrc, pllpre,fbdiv,intdiv):
    divider = 2*intdiv if intdiv > 0 else 1
    return (inputClkSrc*fbdiv)/(pllpre*divider)  
    
# Clock Source Configuration
clkSourceMenu = coreComponent.createMenuSymbol("CLOCK_SOURCE", None)
clkSourceMenu.setLabel("Clock")
frcFreq = coreComponent.createIntegerSymbol("FRC_FREQ",clkSourceMenu)
frcFreq.setVisible(False)
frcFreq.setDefaultValue(getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_FRC_CLOCK))
bfrcFreq = coreComponent.createIntegerSymbol("BFRC_FREQ",clkSourceMenu)
bfrcFreq.setVisible(False)
bfrcFreq.setDefaultValue(getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_FRC_CLOCK))
lprcFreq = coreComponent.createIntegerSymbol("LPRC_FREQ",clkSourceMenu)
lprcFreq.setVisible(False)
lprcFreq.setDefaultValue(getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_LPRC_CLOCK))
    
# External Input Clock Source Configuration
extInputSrcMenu = coreComponent.createMenuSymbol("EXT_CLK_SRC_MENU", clkSourceMenu)
extInputSrcMenu.setLabel("External Input Clock Source")
    
extClkSrcSel = coreComponent.createComboSymbol(EXT_CLK_SRC_SEL, extInputSrcMenu, ["None","Primary Oscillator","External Clock"])
extClkSrcSel.setDefaultValue("None")
extClkSrcSel.setLabel("External Clock Sources")
extClkSrcSel.setDependencies(extClkSrcSelCb,[EXT_CLK_SRC_SEL])

primaryClockUsed = coreComponent.createBooleanSymbol("primaryClockUsed", clkSourceMenu)
primaryClockUsed.setDefaultValue(False)
primaryClockUsed.setVisible(False)
primaryClockUsed.setDependencies(primaryClockUsedCb,[EXT_CLK_SRC_SEL])
    
extClkSrcFreq = coreComponent.createIntegerSymbol(EXT_CLK_SRC_FREQ,extInputSrcMenu)
extClkSrcFreq.setDefaultValue(EXT_CLK_SRC_DEFAULT_FREQ)
extClkSrcFreq.setLabel("Primary/External Clock Frequency")
extClkSrcFreq.setVisible(False)
extClkSrcFreq.setDependencies(extClkSrcFreqCb,[EXT_CLK_SRC_FREQ])

calcExtClkSrcFreq = coreComponent.createIntegerSymbol(CALC_EXT_CLK_SRC_FREQ,extInputSrcMenu)
calcExtClkSrcFreq.setVisible(False)
calcExtClkSrcFreq.setDefaultValue(0)
calcExtClkSrcFreq.setDependencies(calcExtClkSrcFreqCb,[EXT_CLK_SRC_FREQ,CALC_EXT_CLK_SRC_FREQ])

clkOutputPin = coreComponent.createBooleanSymbol("clockOutputPin", extInputSrcMenu)
clkOutputPin.setLabel("Enable Clock output pin")
clkOutputPin.setDefaultValue(False)
clkOutputPin.setDependencies(clockOutputPinCb,[EXT_CLK_SRC_SEL])
clkOutputPin.setHelp(
    "atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_04449;register:OSCCFG"
)

poscmdValue = coreComponent.createIntegerSymbol("poscmdValue",clkSourceMenu)
poscmdValue.setDefaultValue(1) # should this be read from ATDF
poscmdValue.setVisible(False)
poscmdValue.setDependencies(poscmdCb,[EXT_CLK_SRC_SEL,EXT_CLK_SRC_FREQ])
poscmdValue.setHelp(
    "atmel;device:" + Variables.get("__PROCESSOR") + ";comp:clk_04449;register:OSCCFG"
)

poscFreqVal = coreComponent.createIntegerSymbol("POSC_FREQ",clkSourceMenu)
poscFreqVal.setDefaultValue(0) # should this be read from ATDF
poscFreqVal.setVisible(False)
poscFreqVal.setDependencies(poscFreqCb,[EXT_CLK_SRC_SEL,EXT_CLK_SRC_FREQ])
for i in range(1, totalRefInputSrcCount+1):   
    refInpPinEnable = coreComponent.createBooleanSymbol(REF_INPUT_PIN_ENABLE+ str(i), extInputSrcMenu)
    refInpPinEnable.setLabel("Use Reference Input " +str(i))
    refInpPinEnable.setDefaultValue(False)
    refInpPinEnable.setDependencies(refInputValUpdateCb,[REF_INPUT_PIN_ENABLE + str(i)])
    refInputFreq = coreComponent.createIntegerSymbol(REF_INPUT_PIN_FREQ+str(i),refInpPinEnable)
    refInputFreq.setDefaultValue(REF_INPUT_DEFAULT_FREQ)
    refInputFreq.setLabel("Reference Input" + str(i) + " Frequency")
    refInputFreq.setVisible(False)
    refInputFreq.setDependencies(referenceInputFreqCb,[REF_INPUT_PIN_FREQ+str(i)])
    refInputDisplayFreq = coreComponent.createIntegerSymbol("REFI{}_FREQ".format(str(i)),refInpPinEnable)
    refInputDisplayFreq.setDefaultValue(0)
    refInputDisplayFreq.setVisible(False)
    refInputDisplayFreq.setDependencies(referenceInputDisplayFreqCb,[REF_INPUT_PIN_ENABLE+ str(i),REF_INPUT_PIN_FREQ+str(i)])
    
#CLK Fail Interrupt Config
clkFailIntMenu = coreComponent.createMenuSymbol("CLK_FAIL_INT_MENU", clkSourceMenu)
clkFailIntMenu.setLabel("Clock Fail Interrupt") 

clkFailInt = coreComponent.createBooleanSymbol("clockFailIntEnable", clkFailIntMenu)
clkFailInt.setDefaultValue(False)
clkFailInt.setLabel("Enable Clock Fail Interrupt")
clkFailInt.setDependencies(clockFailIntEnableCb,["clockFailIntEnable"])
clkFailInt.setHelp(
    "atmel;device:" + Variables.get("__PROCESSOR") + ";comp:intc_04436;register:IFS0"
)

intIndex= getVectorIndex("CLKFInterrupt")
dataRdyIntComment = coreComponent.createCommentSymbol("clkFailIntComment", clkFailIntMenu)
dataRdyIntComment.setVisible(False)
dataRdyIntComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
dataRdyIntComment.setDependencies(clockFailIntCmntCb, ["clockFailIntEnable", INT_ENABLE.format(intIndex)])

clkFailSymbolMap= getInterruptSymbolMapForCodeGen("","",["CLKFAIL"])
createInterruptSymbols(coreComponent,clkFailSymbolMap,clkFailIntMenu) 
createIsrHandlerNameSymbol(coreComponent,"clkfailIsrHandlerName","CLKF",clkFailIntMenu)


#PLL CLock Configuration
clkMainPllMenu = coreComponent.createMenuSymbol("CLOCK_PLL", clkSourceMenu)
clkMainPllMenu.setLabel("Phase-Locked Loop Configuration")
    
pllPreDefaultValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"PLLPRE") 
pllFbdDefaultValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"PLLFBDIV") 
pllPostDiv1DefaultValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"POSTDIV1") 
pllPostDiv2DefaultValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_DIV,"POSTDIV2") 
pllIntdivDefaultValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,VCO_REG_GROUP,PLL_REG_DIV,"INTDIV")

pllPostDiv1Options = ["{}".format(i) for i in range(1, pllPostDiv2DefaultValue["maskValue"]+1)]
pllPostDiv2Options = ["{}".format(i) for i in range(1, pllPostDiv2DefaultValue["maskValue"]+1)]
pllClkSrcDefault = {
                "defaultValue" : 0,
                "maskValue" :getIntValueForAtdfParam(INTERNAL_OSCILLATOR,CLOCK,PARAM_MAX_INPUT_PLL_FREQ_HZ) #Here , mask is referring to max value
            }

for i in range(1, totalPllCount+1):
    pllClkMenu = createClkBooleanSymbol(coreComponent, PLL_ENABLE.format(i), clkMainPllMenu, "Enable Phase Locked Loop" + str(i), False)
    pllClkMenu.setDependencies(clkPllEnableCb,[PLL_ENABLE.format(i)])
    pllClkMenu.setVisible(True)
    if i == 1:
        pllClkMenu.setValue(True)
    
    pllClkSrc = createKeyValueSettingSymbol(coreComponent,PLL_CLOCK_SOURCE.format(i),INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_CON,NOSC,pllClkMenu)
    pllClkSrc.setLabel("Clock Source")
    pllClkSrc.setVisible(True)
    pllClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxCON"
    )
    
    pllClkSrcDefault["defaultValue"] = getClkSourceFrequency(pllClkSrc.getComponent(),pllClkSrc.getSelectedKey())
    pllClkSrcFreq = createClkIntSymbol(coreComponent,PLL_CLOCK_SOURCE_FREQ.format(i),pllClkMenu,pllClkSrcDefault,"Clock Source Frequency")
    pllClkSrcFreq.setReadOnly(True)
    pllClkSrcFreq.setDependencies(pllClkSrcChangeCb,[PLL_ENABLE.format(i),PLL_CLOCK_SOURCE.format(i)])
    pllClkSrcFreq.setVisible(True)
        
    pllPre = createClkIntSymbol(coreComponent,PLLPRE.format(i),pllClkMenu,pllPreDefaultValue,"Clock Prescaler(PLLPRE)")
    pllPre.setVisible(True)
    pllPre.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxDIV"
    )
    
    pllFbd = createClkIntSymbol(coreComponent,PLLFBD.format(i),pllClkMenu,pllFbdDefaultValue,"Feedback Divider(PLLFBDIV)")
    pllFbd.setVisible(True)
    pllFbd.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxDIV"
    )
    
    pllVcoPfdFreq = coreComponent.createIntegerSymbol(PLL_CALC_PFD_FREQ.format(i),pllClkMenu)
    pllVcoPfdFreq.setDefaultValue(0)
    pllVcoPfdFreq.setLabel("Calculated PFD Divider Frequency")
    pllVcoPfdFreq.setVisible(False)
    pllVcoPfdFreq.setReadOnly(True)
    pllVcoPfdFreq.setDependencies(pllPfdDivFreqCb ,[PLL_ENABLE.format(i) ,PLL_CLOCK_SOURCE_FREQ.format(i),PLLPRE.format(i),PLLFBD.format(i)])
        
    pllVcoDiv = createClkIntSymbol(coreComponent,PLL_INTDIV.format(i),pllClkMenu,pllIntdivDefaultValue,"VCO Integer Divider(INTDIV)")
    pllVcoDiv.setVisible(True)
    pllVcoDiv.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:VCOxDIV"
    )
    
    pllVcoDivFreq = coreComponent.createIntegerSymbol(PLL_CALC_VCO_FREQ.format(i),pllClkMenu)
    pllVcoDivFreq.setDefaultValue(0)
    pllVcoDivFreq.setLabel("Calculated VCO Divider Frequency")
    pllVcoDivFreq.setVisible(True)
    pllVcoDivFreq.setReadOnly(True)
    pllVcoDivFreq.setDependencies(pllVcoDivFreqCb ,[PLL_ENABLE.format(i),PLL_CALC_VCO_FREQ.format(i) ,PLL_CLOCK_SOURCE_FREQ.format(i),PLLPRE.format(i),PLLFBD.format(i),PLL_INTDIV.format(i)])
    
    pllVcoFreqInMhz = coreComponent.createStringSymbol(PLL_CALC_VCO_FREQ_MHZ.format(i),pllClkMenu)
    pllVcoFreqInMhz.setReadOnly(True)
    pllVcoFreqInMhz.setVisible(False)
    pllVcoFreqInMhz.setDependencies(clkGenFreqInMhzCb,[PLL_CALC_VCO_FREQ.format(i)])
    pllVcoFreqInMhz.setValue(convertToMHz(pllVcoDivFreq.getValue()))
    

    pllPostDiv1 = coreComponent.createComboSymbol(POSTDIV1.format(i).format(i),pllClkMenu,pllPostDiv1Options) 
    pllPostDiv1.setLabel("Post Divider 1(POSTDIV1)")
    pllPostDiv1.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxDIV"
    )
    if i == 1:
        pllPostDiv1.setValue("4")
    else:
         pllPostDiv1.setValue("1")    

    pllPostDiv2 = coreComponent.createComboSymbol(POSTDIV2.format(i).format(i),pllClkMenu,pllPostDiv2Options) 
    pllPostDiv2.setLabel("Post Divider 2(POSTDIV2)")
    pllPostDiv2.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxDIV"
    )
    if i == 1:
        pllPostDiv2.setValue("2")
    else:
        pllPostDiv2.setValue("1")    
    
    plloFreq = coreComponent.createIntegerSymbol(PLL_CALC_PLLO_FREQ.format(i),pllClkMenu)
    plloFreq.setDefaultValue(0)
    plloFreq.setLabel("Calculated PLL Out Frequency")
    plloFreq.setVisible(True)
    plloFreq.setReadOnly(True)
    plloFreq.setDependencies(plloFreqCb ,[PLL_ENABLE.format(i),PLL_CALC_PLLO_FREQ.format(i), PLL_CLOCK_SOURCE_FREQ.format(i),PLLPRE.format(i),PLLFBD.format(i),POSTDIV1.format(i),POSTDIV2.format(i) ])
    
    plloFreqInMhz = coreComponent.createStringSymbol(PLL_CALC_PLLO_FREQ_MHZ.format(i),pllClkMenu)
    plloFreqInMhz.setReadOnly(True)
    plloFreqInMhz.setVisible(False)
    plloFreqInMhz.setDependencies(clkGenFreqInMhzCb,[PLL_CALC_PLLO_FREQ.format(i)])
    plloFreqInMhz.setValue(convertToMHz(plloFreq.getValue()))
    
    pllClkFailMask = coreComponent.createStringSymbol(PLL_GEN_FAIL_MASK.format(i),pllClkMenu)
    pllClkFailMask.setVisible(False)
    bitNode = getBitField(INTERNAL_OSCILLATOR,"CLKFAIL","CLKFAIL","PLL{}FAIL".format(i))
    bitMask = "0x0"
    if(bitNode != None):
            bitMask = bitNode.getAttribute("mask")
    pllClkFailMask.setDefaultValue(bitMask) 
            
    pllFailSafeEnable = createClkBooleanSymbol(coreComponent, PLL_FAIL_SAFE_CLK_ENABLE.format(i), pllClkMenu, "Enable Fail-Safe Clock", False)
    pllFailSafeEnable.setVisible(True)
    pllFailSafeEnable.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxCON"
    )
    
    pllFailSafeEnableBit = createKeyValueSettingSymbol(coreComponent,PLL_FSCMEN.format(i),INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_CON,"FSCMEN",pllClkMenu)
    
    pllBackUpClkSrc = createKeyValueSettingSymbol(coreComponent,PLL_BACKUP_CLOCK_SOURCE.format(i),INTERNAL_OSCILLATOR,PLL_REG_GROUP,PLL_REG_CON,BOSC,pllFailSafeEnable)
    pllBackUpClkSrc.setDependencies(clkPllBackUpClkSrcCb,[PLL_ENABLE.format(i) , PLL_FAIL_SAFE_CLK_ENABLE.format(i)])
    pllBackUpClkSrc.setLabel("Backup Clock Source")
    pllBackUpClkSrc.setVisible(True)
    pllBackUpClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:PLLxCON"
    )
    
    pllVcoDivFreq.setValue(calcPllVcoDivFreq(pllVcoDivFreq.getComponent(),i))
    plloFreq.setValue(calcPlloFreq(plloFreq.getComponent(),i))
    clkPllEnable(pllClkMenu.getComponent(),pllClkMenu,i)

#Clock Generator Configuration
commonClkGeneratorMenu = coreComponent.createMenuSymbol("CLOCK_GENERATOR", clkSourceMenu)
commonClkGeneratorMenu.setLabel("Clock Generator Configuration")

defaultEnabledClkGenList = string_to_list(getAtdfParameterValue(INTERNAL_OSCILLATOR,CLOCK,PARAM_DEFAULT_CLK_GEN_ENABLED))
clkGenDividerNotSupportedList = string_to_list(getAtdfParameterValue(INTERNAL_OSCILLATOR,CLOCK,PARAM_CLK_GEN_DIVIDER_NOT_SUPPORTED))

for i in range(1, totalClkGenCount+1):
    clkGenMenu = createClkBooleanSymbol(coreComponent, CLK_GEN_ENABLE.format(i), commonClkGeneratorMenu, "Clock Generator " + str(i), False)
    clkGenMenu.setLabel(getClkGenPaneName(i))
    clkGenMenu.setVisible(True)
    clkGenMenu.setDependencies(clkEnableCb,[CLK_GEN_ENABLE.format(i)])
    
    if i in defaultEnabledClkGenList :
        clkGenMenu.setValue(True)
        clkGenMenu.setReadOnly(True)    
       
    clkGenClkSrc = createKeyValueSettingSymbol(coreComponent,CLK_GEN_NOSC.format(i),INTERNAL_OSCILLATOR,CLK_CON_REG_GROUP,CLK_CON_REG,NOSC,clkGenMenu)
    if i ==2 :
        clkGenClkSrc.setReadOnly(True)
    
    if i==3 :
        clkGenClkSrc.setReadOnly(True) 
        clkGenClkSrc.setSelectedKey(BACKUP_FRC_OSCILLATOR)    
                   
    clkGenClkSrc.setLabel("Clock Source")
    clkGenClkSrc.setVisible(True)
    clkGenClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CLKxCON"
    )
    
    
    clkGenClkSrcFreq = coreComponent.createIntegerSymbol(CLK_GEN_CLK_SRC_FREQ.format(i),clkGenMenu)
    clkGenClkSrcFreq.setDefaultValue(getClkSourceFrequency(clkGenClkSrcFreq.getComponent(),clkGenClkSrc.getSelectedKey()))
    clkGenClkSrcFreq.setDependencies(clkGenClkSrcChangeCb,[CLK_GEN_NOSC.format(i)])
    clkGenClkSrcFreq.setLabel("Clock Source Frequency")
    clkGenClkSrcFreq.setReadOnly(True)
    clkGenClkSrcFreq.setVisible(True)
    
    if( i not in clkGenDividerNotSupportedList) :
        enableClkDiv = createClkBooleanSymbol(coreComponent, CLK_GEN_DIVIDER_ENABLE.format(i), clkGenMenu, "Enable Clock Divider", False)
        enableClkDiv.setVisible(True)
        
        intDivDefaultAndMaskValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,CLK_CON_REG_GROUP,CLK_DIV_REG,"INTDIV")
        intDiv = createClkIntSymbol(coreComponent, CLK_GEN_INTDIV.format(i), enableClkDiv,intDivDefaultAndMaskValue ,"Integer Divider(INTDIV)")
        intDiv.setDefaultValue(1)
        intDiv.setDependencies(clkDivBasedCb,[CLK_GEN_DIVIDER_ENABLE.format(i)])
        intDiv.setVisible(False)
        intDiv.setHelp(
            	"atmel;device:"
            	+ Variables.get("__PROCESSOR")
            	+ ";comp:clk_04449;register:CLKxDIV"
        )
    
        fracDivDefaultAndMaskValue = getSettingBitDefaultAndMaskValue(INTERNAL_OSCILLATOR,CLK_CON_REG_GROUP,CLK_DIV_REG,FRACDIV)
        fracDiv = createClkIntSymbol(coreComponent, CLK_GEN_FRACDIV.format(i), enableClkDiv,fracDivDefaultAndMaskValue ,"Fractional Divider(FRACDIV)")
        fracDiv.setDependencies(clkDivBasedCb,[CLK_GEN_DIVIDER_ENABLE.format(i)])
        fracDiv.setVisible(False)
        fracDiv.setHelp(
            	"atmel;device:"
            	+ Variables.get("__PROCESSOR")
            	+ ";comp:clk_04449;register:CLKxDIV"
        )
        
    if( i == 4): #condition added specifically for plugin requirement
        enableClkDiv = createClkBooleanSymbol(coreComponent, CLK_GEN_DIVIDER_ENABLE.format(i), clkGenMenu, "Enable Clock Divider", False)
        enableClkDiv.setVisible(False)
        
        intDiv = coreComponent.createIntegerSymbol(CLK_GEN_INTDIV.format(i), enableClkDiv)
        intDiv.setDefaultValue(1)
        intDiv.setVisible(False)

        fracDiv = coreComponent.createIntegerSymbol(CLK_GEN_FRACDIV.format(i), enableClkDiv)
        fracDiv.setDefaultValue(0)
        fracDiv.setVisible(False)

        
    clkGenFreqCmnt = coreComponent.createCommentSymbol(CLK_GEN_CALCULATED_FREQ_CMNT.format(i), clkGenMenu)
    paramName = "CLK_GEN_"+str(i)
    clkGenDescription = "Clock Generator" if i!= 1 else "System Clock"  
    paramCaption = getAtdfParameterCaption(INTERNAL_OSCILLATOR,CLOCK,paramName)
    clkGenFreqCmnt.setLabel("Info : {} frequency limit is {}MHz".format(clkGenDescription,paramCaption)) 
    clkGenFreqCmnt.setDependencies(clkGenFreqCmntCb,[CLK_GEN_CALCULATED_FREQ.format(i)])   
    
    clkGenFreq = coreComponent.createIntegerSymbol(CLK_GEN_CALCULATED_FREQ.format(i),clkGenMenu)
    clkGenFreq.setLabel("Clock Generator Frequency")
    clkGenFreq.setReadOnly(True)
    clkGenFreq.setDependencies( clkGenFreqCb,[CLK_GEN_CALCULATED_FREQ.format(i),CLK_GEN_CLK_SRC_FREQ.format(i),CLK_GEN_DIVIDER_ENABLE.format(i),CLK_GEN_INTDIV.format(i), CLK_GEN_FRACDIV.format(i)])
    clkGenFreq.setVisible(True)
    
    clkGenFreqInMhz = coreComponent.createStringSymbol(CLK_GEN_CALCULATED_FREQ_MHZ.format(i),clkGenMenu)
    clkGenFreqInMhz.setReadOnly(True)
    clkGenFreqInMhz.setVisible(False)
    clkGenFreqInMhz.setDependencies(clkGenFreqInMhzCb,[CLK_GEN_CALCULATED_FREQ.format(i)])
    
    
    
    if i==1: 
        clkGenMenu.setLabel("System Clock (Clock Generator 1)")
        clkGenClkSrc.setLabel("System Clock Source")
        clkGenClkSrc.setSelectedKey("PLL1 FOUT")
        
        clkGenFreq.setLabel("System Clock Frequency")
        
        systemClkFreq = coreComponent.createIntegerSymbol("sysClockFrequency",clkGenMenu)
        systemClkFreq.setVisible(False)
        systemClkFreq.setDefaultValue(clkGenFreq.getValue())
        systemClkFreq.setDependencies(systemClkCb,[CLK_GEN_CALCULATED_FREQ.format(i)]) 
        
        stdSpeedClkFreq = coreComponent.createIntegerSymbol("stdSpeedClkFreq",clkGenMenu)
        stdSpeedClkFreq.setLabel("Standard Speed Peripheral Clock (System Clock/2)")
        stdSpeedClkFreq.setReadOnly(True)
        stdSpeedClkFreq.setDefaultValue(clkGenFreq.getValue()/2)
        stdSpeedClkFreq.setDependencies(stdSpeedCb,[CLK_GEN_CALCULATED_FREQ.format(i)])
            
        slowSpeedClkFreq = coreComponent.createIntegerSymbol("slowSpeedClkFreq",clkGenMenu)
        slowSpeedClkFreq.setLabel("Slow Speed Peripheral Clock (System Clock/4)")
        slowSpeedClkFreq.setReadOnly(True)
        slowSpeedClkFreq.setDefaultValue(clkGenFreq.getValue()/4)
        slowSpeedClkFreq.setDependencies(slowSpeedCb,[CLK_GEN_CALCULATED_FREQ.format(i)])
        
        sysClockSourceComment = coreComponent.createStringSymbol("sysClockSourceComment",clkGenMenu)
        sysClockSourceComment.setVisible(False)
        sysClockSourceComment.setDependencies(sysClkSrcCb,[CLK_GEN_NOSC.format(1)])
        sysClockSourceComment.setValue(clkGenClkSrc.getSelectedKey())
        
        sysClockFrequencyComment = coreComponent.createStringSymbol("sysClockFrequencyComment",clkGenMenu)
        sysClockFrequencyComment.setVisible(False)
        sysClockFrequencyComment.setDependencies(sysFreqInMHzCb,[CLK_GEN_CALCULATED_FREQ_MHZ.format(i)])
        sysClockFrequencyComment.setValue(clkGenFreqInMhz.getValue())
    
    clkFailMask = coreComponent.createStringSymbol(CLK_GEN_FAIL_MASK.format(i),clkGenMenu)
    clkFailMask.setVisible(False)
    bitNode = getBitField(INTERNAL_OSCILLATOR,"CLKFAIL","CLKFAIL","CLKFAIL" + str(i))
    bitMask = "0x0"
    if(bitNode != None):
            bitMask = bitNode.getAttribute("mask")
    clkFailMask.setDefaultValue(bitMask)    
    
    enableFailSafeClk = createClkBooleanSymbol(coreComponent, CLK_GEN_ENABLE_FAIL_SAFE.format(i), clkGenMenu, "Enable Fail-Safe Clock", False)       
    enableFailSafeClk.setVisible(True)
    enableFailSafeClk.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CLKxCON"
    )

    failSafeEnableBit = createKeyValueSettingSymbol(coreComponent,CLK_GEN_FSCMEN.format(i),INTERNAL_OSCILLATOR,CLK_CON_REG_GROUP,CLK_CON_REG,"FSCMEN",clkGenMenu)
    
    defaultBackupClkSrc = BACKUP_FRC_OSCILLATOR if i != 3 else FRC_OSCILLATOR  #clk gen3 has BFRC as default clk src
    backUpClkSrc = createKeyValueSettingBoscSymbol(coreComponent,CLK_GEN_BOSC.format(i),INTERNAL_OSCILLATOR,CLK_CON_REG_GROUP,CLK_CON_REG,BOSC,enableFailSafeClk,defaultBackupClkSrc)
    backUpClkSrc.setLabel("Backup Clock Source")
    backUpClkSrc.setDependencies(clkGenBackUpClkSrcCb,[CLK_GEN_ENABLE_FAIL_SAFE.format(i)])
    backUpClkSrc.setVisible(True)
    backUpClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CLKxCON"
    )

    clkGenEnable(clkGenMenu.getComponent(),clkGenMenu,i)
    clkGenFreqInMhz.setValue(convertToMHz(clkGenFreq.getValue()))
    

clkMainMonMenu = coreComponent.createMenuSymbol("CLOCK_MONITOR", clkSourceMenu)
clkMainMonMenu.setLabel("Clock Monitor Configuration")



for i in range(1, totalClkMonitorCount+1):
    
    clkMonMenu = createClkBooleanSymbol(coreComponent, CLK_MON_ENABLE.format(i), clkMainMonMenu, "Use Clock Monitor " + str(i), False)
    clkMonMenu.setDependencies(clkMonEnableCb,[CLK_MON_ENABLE.format(i)])
    clkMonMenu.setVisible(True)
    clkMonMenu.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxCON"
    )

    clkMonSatInt =  createClkBooleanSymbol(coreComponent,"cm{}monIntEnable".format(i), clkMonMenu,"Enable Clock MOnitor Saturation Interrupt",True)

    intIndex= getVectorIndex("CLK{}MInterrupt".format(i))
    clkMonErrorIntComment = coreComponent.createCommentSymbol(CLK_MON_ERROR_INT_CMNT.format(i), clkMonMenu)
    clkMonErrorIntComment.setVisible(False)
    clkMonErrorIntComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
    clkMonErrorIntComment.setDependencies(clockMonErrorIntCmntCb, [CLK_MON_ENABLE.format(i), INT_ENABLE.format(intIndex)])
        
    clockMonInitEnable = createClkBooleanSymbol(coreComponent, CLK_MON_ENABLE_INIT_STAGE.format(i), clkMonMenu, "Enable Monitor During Initialization", False)
    
    clkMonRefClkSrc = createKeyValueSettingSymbol(coreComponent,CM_SEL__WINSEL.format(i),INTERNAL_OSCILLATOR,CM_REG_GROUP,CM_REG_SEL,WINSEL,clkMonMenu)
    clkMonRefClkSrc.setLabel("Reference Clock Source")
    
    clkMonRefClkSrcFreq = createClkMonIntegerSymbol(coreComponent, CLK_MON_REF_CLK_SRC_FREQ.format(i), clkMonMenu, "Reference Clock Source Frequency", 0, True)
    clkMonRefClkSrcFreq.setDependencies(updateClkMonRefFreqCb,[CM_SEL__WINSEL.format(i)])
    updateClkMonRefFreq(clkMonRefClkSrcFreq)
    

    clkMonAccumulationWindow = createClkMonHexSymbol(coreComponent, CLK_MON_ACCUMULATION_WINDOW.format(i), clkMonMenu, 0x0, "Accumulation Window(WINPR)")
    clkMonAccumulationWindow.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxWINPR"
    )

    clkMonTimerWindowPeriod = createClkMonStrSymbol(coreComponent, CLK_MON_TIMER_WINDOW_PERIOD.format(i), clkMonMenu, "Calculated Timer Window Period", "0 us", True)  
    clkMonTimerWindowPeriod.setDependencies(calcTmrWindowCb,[CLK_MON_REF_CLK_SRC_FREQ.format(i),CLK_MON_ACCUMULATION_WINDOW.format(i)])
    calcTmrWindow(clkMonTimerWindowPeriod)
    
    clkMonClkSrc = createKeyValueSettingSymbol(coreComponent,CM_SEL__CNTSEL.format(i),INTERNAL_OSCILLATOR,CM_REG_GROUP,CM_REG_SEL,WINSEL,clkMonMenu)
    clkMonClkSrc.setLabel("Monitor Clock Source")
    clkMonClkSrc.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxSEL"
    )
    
    clkMonCounterDivider = createKeyValueSettingSymbol(coreComponent, CM_CON__CNTDIV.format(i),INTERNAL_OSCILLATOR ,CM_REG_GROUP,CM_REG_CON ,CNTDIV,clkMonMenu)
    clkMonCounterDivider.setLabel("Monitor Clock Divider")
    clkMonCounterDivider.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxCON"
    )
    
    clkMonClkSrcFreq = createClkMonIntegerSymbol(coreComponent, CLK_MON_CLK_SRC_FREQ.format(i), clkMonMenu, "Monitor Clock Frequency", 0, True)
    clkMonClkSrcFreq.setDependencies(updateClkMonFreqCb,[CM_SEL__CNTSEL.format(i), CM_CON__CNTDIV.format(i)])
    updateClkMonFreq(clkMonClkSrcFreq)
    
    clkMonBufferCount = createClkMonStrSymbol(coreComponent, CLK_MON_BUFFER_COUNT.format(i), clkMonMenu, "Expected Buffer Count(BUF)", "0x0", True)
    clkMonBufferCount.setDependencies(updateClkMonBufCountCb,[CLK_MON_REF_CLK_SRC_FREQ.format(i), CLK_MON_TIMER_WINDOW_PERIOD.format(i),CLK_MON_CLK_SRC_FREQ.format(i)])
    clkMonBufferCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxBUF"
    )
    updateClkMonBufCount(clkMonBufferCount)
    
    clkMonSaturationCount = createClkMonHexSymbol(coreComponent,CLK_MON_SATURATION_COUNT.format(i),clkMonMenu,0x0,"Saturation Count(SAT)")
    clkMonSaturationCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxSAT"
    )

    clkMonDataReadyEnableInt = createClkBooleanSymbol(coreComponent,CLK_MON_DATA_READY_ENABLE_INT.format(i), clkMonMenu,"Enable Clock Data Ready Interrupt",False)
    clkMonDataReadyEnableInt.setDependencies(clkMonReadyEnableIntCb,[CLK_MON_DATA_READY_ENABLE_INT.format(i)])
    clkMonDataReadyEnableInt.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:intc_04436;register:IFS0"
    )
    
    intIndex= getVectorIndex("CLK{}RInterrupt".format(i))
    dataRdyIntComment = coreComponent.createCommentSymbol(CLK_MON_DATA_READY_ENABLE_INT_CMNT.format(i), clkMonMenu)
    dataRdyIntComment.setVisible(False)
    dataRdyIntComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
    dataRdyIntComment.setDependencies(clockMonRdyIntCmntCb, [CLK_MON_ENABLE.format(i),CLK_MON_DATA_READY_ENABLE_INT.format(i), INT_ENABLE.format(intIndex)])
    
    clkMonWarningEnableInt = createClkBooleanSymbol(coreComponent,CLK_MON_WARN_ENABLE_INT.format(i), clkMonMenu,"Enable Clock Warning Interrupt",False)
    clkMonWarningEnableInt.setDependencies(clkMonWarnEnableIntCb,[CLK_MON_WARN_ENABLE_INT.format(i)])
    clkMonWarningEnableInt.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:intc_04436;register:IFS0"
    )
    
    intIndex= getVectorIndex("CLK{}WInterrupt".format(i))
    clkMonWarningComment = coreComponent.createCommentSymbol(CLK_MON_WARN_ENABLE_INT_CMNT.format(i), clkMonMenu)
    clkMonWarningComment.setVisible(False)
    clkMonWarningComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
    clkMonWarningComment.setDependencies(clockMonWarnIntCmntCb, [CLK_MON_ENABLE.format(i),CLK_MON_WARN_ENABLE_INT.format(i), INT_ENABLE.format(intIndex)])
    
    clkMonWarningLowCount = createClkMonHexSymbol(coreComponent,CLK_MON_WARN_LOW_COUNT.format(i),clkMonWarningEnableInt,0x0,"Warning Low Count(LWARN)")
    clkMonWarningLowCount.setDependencies(clkMonInterruptVisibilityCb,[CLK_MON_WARN_ENABLE_INT.format(i)])
    clkMonWarningLowCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxLWARN"
    )
    
    clkMonWarningHighCount = createClkMonHexSymbol(coreComponent,CLK_MON_WARN_HIGH_COUNT.format(i),clkMonWarningEnableInt,0xFFFFFFFF,"Warning High Count(HWARN)")
    clkMonWarningHighCount.setDependencies(clkMonInterruptVisibilityCb,[CLK_MON_WARN_ENABLE_INT.format(i)])
    clkMonWarningHighCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxHWARN"
    )
    
    clkMonWarningFreqRange = createClkMonStrSymbol(coreComponent,CLK_MON_WARN_FREQ_RANGE.format(i),clkMonWarningEnableInt,"Monitor Clock Warning Frequency Range","Range",True)
    clkMonWarningFreqRange.setDependencies(clkMonWarningRangeCb,[CLK_MON_WARN_ENABLE_INT.format(i),CLK_MON_WARN_LOW_COUNT.format(i),CLK_MON_WARN_HIGH_COUNT.format(i),CLK_MON_REF_CLK_SRC_FREQ.format(i), CLK_MON_ACCUMULATION_WINDOW.format(i)])

    
    clkMonThresholdEnableInt = createClkBooleanSymbol(coreComponent,CLK_MON_THRESHOLD_ENABLE_INT.format(i), clkMonMenu,"Enable Clock Threshold Interrupt",False)
    clkMonThresholdEnableInt.setDependencies(clkMonThresholdEnableIntCb,[CLK_MON_THRESHOLD_ENABLE_INT.format(i)])
    
    intIndex= getVectorIndex("CLK{}FInterrupt".format(i))
    clkMonThresholdComment = coreComponent.createCommentSymbol(CLK_MON_THRESHOLD_ENABLE_INT_CMNT.format(i), clkMonMenu)
    clkMonThresholdComment.setVisible(False)
    clkMonThresholdComment.setLabel("Warning!!! Interrupt is Disabled in Interrupt Manager")
    clkMonThresholdComment.setDependencies(clockMonThresholdIntCmntCb, [CLK_MON_THRESHOLD_ENABLE_INT.format(i), INT_ENABLE.format(intIndex)])
    
    clkMonThresholdLowCount = createClkMonHexSymbol(coreComponent,CLK_MON_THRESHOLD_LOW_COUNT.format(i),clkMonThresholdEnableInt,0x0,"Fail Threshold Low Count(LFAIL)")
    clkMonThresholdLowCount.setDependencies(clkMonInterruptVisibilityCb,[CLK_MON_THRESHOLD_ENABLE_INT.format(i)])
    clkMonThresholdLowCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxLFAIL"
    )
    
    clkMonThresholdHighCount = createClkMonHexSymbol(coreComponent,CLK_MON_THRESHOLD_HIGH_COUNT.format(i),clkMonThresholdEnableInt,0xFFFFFFFF,"Fail Threshold High Count(HFAIL)")
    clkMonThresholdHighCount.setDependencies(clkMonInterruptVisibilityCb,[CLK_MON_THRESHOLD_ENABLE_INT.format(i)])
    clkMonThresholdHighCount.setHelp(
        "atmel;device:"
        + Variables.get("__PROCESSOR")
        + ";comp:clk_04449;register:CMxHFAIL"
    )
    
    clkMonThresholdFreqRange = createClkMonStrSymbol(coreComponent,CLK_MON_THRESHOLD_FREQ_RANGE .format(i),clkMonThresholdEnableInt,"Monitor Clock Fail Threshold Frequency Range","Range",True)
    clkMonThresholdFreqRange.setDependencies(clkMonThresholdRangeCb,[CLK_MON_THRESHOLD_ENABLE_INT.format(i),CLK_MON_THRESHOLD_LOW_COUNT.format(i),CLK_MON_THRESHOLD_HIGH_COUNT.format(i),CLK_MON_REF_CLK_SRC_FREQ.format(i), CLK_MON_ACCUMULATION_WINDOW.format(i)])   

    # Interrupt Symbols from ATDF for Code Generation 
    compPrefix = "C"
    compInstance = str(i)
    interruptList = ["RDY" , "WARN","FAIL","MON"]  
    intSymbolMap= getInterruptSymbolMapForCodeGen(compPrefix,compInstance,interruptList)
    createInterruptSymbols(coreComponent,intSymbolMap,clkMonMenu)
    createIsrHandlerNameSymbol(coreComponent,"c"+compInstance+"monIsrHandlerName","CLK"+compInstance+"M",clkMonMenu)
    createIsrHandlerNameSymbol(coreComponent,"c"+compInstance+"rdyIsrHandlerName","CLK"+compInstance+"R",clkMonMenu)
    createIsrHandlerNameSymbol(coreComponent,"c"+compInstance+"failIsrHandlerName","CLK"+compInstance+"F",clkMonMenu)
    createIsrHandlerNameSymbol(coreComponent,"c"+compInstance+"warnIsrHandlerName","CLK"+compInstance+"W",clkMonMenu)
    
    
        
        
# Code Generation Symbols
maxPllGen = coreComponent.createIntegerSymbol("maxPllGen",clkSourceMenu)
maxPllGen.setDefaultValue(totalPllCount)
maxPllGen.setVisible(False)

maxClockMon = coreComponent.createIntegerSymbol("maxClockGen",clkSourceMenu)
maxClockMon.setDefaultValue(totalClkGenCount) 
maxClockMon.setVisible(False)

maxClockMon = coreComponent.createIntegerSymbol("maxClockMon",clkSourceMenu)
maxClockMon.setDefaultValue(totalClkMonitorCount)
maxClockMon.setVisible(False)

useClockMon = coreComponent.createBooleanSymbol("useClockMonitor",clkSourceMenu)
useClockMon.setDefaultValue(False)
useClockMon.setVisible(False)
clkMonEnableSymbolList = [ CLK_MON_ENABLE.format(i) for i in range(1, totalClkMonitorCount + 1)]
useClockMon.setDependencies(useClkMonCb,clkMonEnableSymbolList)

clkoUsed= coreComponent.createBooleanSymbol("clkoUsed",clkSourceMenu)
clkoUsed.setDefaultValue(False)
clkoUsed.setVisible(False)
clkoUsed.setDependencies(codeGenClkOpPinCb,[EXT_CLK_SRC_SEL,"clockOutputPin"])

clockModuleString= coreComponent.createStringSymbol("clockModuleString",clkSourceMenu)
clkGenEnableSymbolList = [ CLK_GEN_ENABLE.format(i) for i in range(1, totalClkGenCount + 1)]
useClkGen(clockModuleString) #setDefaultValue
clockModuleString.setDependencies(useClkGenCb,clkGenEnableSymbolList)
clockModuleString.setVisible(False)

# File handling below
CONFIG_NAME = Variables.get("__CONFIGURATION_NAME")

CLK_HDR_FILE = coreComponent.createFileSymbol("CLK_H", None)
CLK_HDR_FILE.setSourcePath("../peripheral/clk_04449/templates/plib_clk.h.ftl")
CLK_HDR_FILE.setOutputName("plib_clk.h")
CLK_HDR_FILE.setDestPath("/peripheral/clk/")
CLK_HDR_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
CLK_HDR_FILE.setType("HEADER")
CLK_HDR_FILE.setMarkup(True)

CLK_INTERFACE_COMMON = coreComponent.createFileSymbol("CLK_COMMON_H", None)
CLK_INTERFACE_COMMON.setSourcePath("../peripheral/clk_04449/templates/plib_clk_common.h.ftl")
CLK_INTERFACE_COMMON.setOutputName("plib_clk_common.h")
CLK_INTERFACE_COMMON.setDestPath("/peripheral/clk/")
CLK_INTERFACE_COMMON.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
CLK_INTERFACE_COMMON.setType("HEADER")
CLK_INTERFACE_COMMON.setMarkup(True)

CLK_SRC_FILE = coreComponent.createFileSymbol("CLK_C", None)
CLK_SRC_FILE.setSourcePath("../peripheral/clk_04449/templates/plib_clk.c.ftl")
CLK_SRC_FILE.setOutputName("plib_clk.c")
CLK_SRC_FILE.setDestPath("/peripheral/clk/")
CLK_SRC_FILE.setProjectPath("config/" + CONFIG_NAME + "/peripheral/clk/")
CLK_SRC_FILE.setType("SOURCE")
CLK_SRC_FILE.setMarkup(True)

#Add clock related code to common files
CLK_SYS_DEF_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_DEFINITIONS_H", None)
CLK_SYS_DEF_LIST_ENTRY.setType("STRING")
CLK_SYS_DEF_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
CLK_SYS_DEF_LIST_ENTRY.setSourcePath("../peripheral/clk_04449/templates/system/definitions.h.ftl")
CLK_SYS_DEF_LIST_ENTRY.setMarkup(True)

CLK_SYS_INIT_LIST_ENTRY = coreComponent.createFileSymbol("CLK_SYSTEM_INITIALIZE_C", None)
CLK_SYS_INIT_LIST_ENTRY.setType("STRING")
CLK_SYS_INIT_LIST_ENTRY.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
CLK_SYS_INIT_LIST_ENTRY.setSourcePath("../peripheral/clk_04449/templates/system/initialization.c.ftl")
CLK_SYS_INIT_LIST_ENTRY.setMarkup(True)
