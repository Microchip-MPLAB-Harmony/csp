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

import re

def _find_default_value(bitfieldNode, initialRegValue):
    '''
    Helper function to lookup default value for a particular bitfield within a given register from atdf node
    Arguments:
      bitfieldNode - the particular <bitfield > entry in the atdf file being looked at
      initialRegValue - initval of <register > entry in the atdf file.  Holds initial values of
                        all fields for this register.
    '''
    # make initialRegValue an integer
    registerValue = int(initialRegValue[2:],16)   # get rid of the '0x'

    # find bitshift of lsb of field
    maskStr = bitfieldNode.getAttribute('mask').strip('L')
    if(maskStr.find('0x') != -1):
        mask = int(maskStr[2:],16)
    else:
        mask = int(maskStr)
    shift = 0
    for ii in range(0,32):
        if( ((mask >> ii) & 1) != 0):
            shift = ii
            break
    return((registerValue & mask) >> shift)

def _find_key(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.  Needed for setting up combo symbol value.
          value - the value to be looked for in the dictionary
          keypairs - the dictionary to be searched over
    '''
    for keyname, val in keypairs.items():
        if(val == str(value)):
            return keyname
    print("_find_key: could not find value in dictionary") # should never get here
    return ""

def _process_valuegroup_entry(node):
    '''
    Looks at input node and returns key name, description, and value for it.
       node:  <value ...> in atdf file.  A particular bitfield value for a particular register.
    '''
    stringval = node.getAttribute('value')
    newstring = stringval.replace('L','')
    value = int(newstring,16)
    return str(value)

def sort_alphanumeric(l):
    import re
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def getCorePeripheralsInterruptDataStructure():

    dmacVectName = ["DMA0Interrupt", "DMA1Interrupt", "DMA2Interrupt", "DMA3Interrupt", "DMA4Interrupt", "DMA5Interrupt","DMA6Interrupt","DMA7Interrupt"]
    dmacIntSrc = ["CHANNEL0", "CHANNEL1", "CHANNEL2", "CHANNEL3","CHANNEL4", "CHANNEL5", "CHANNEL6", "CHANNEL7"]
    uartIntSrc = ["USART_ERROR", "USART_RX", "USART_TX_COMPLETE"]
    spiIntSrc = ["SPI_ERROR", "SPI_RX", "SPI_TX_COMPLETE"]
   # i2cIntSrc = ["I2C_0", "I2C_1"]

    corePeripherals = {

            "DMAC" : {"name":dmacVectName, "INT_SRC":dmacIntSrc},

            "UART1" : {"name":["U1EInterrupt", "U1RXInterrupt", "U1TXInterrupt"], "INT_SRC":uartIntSrc},
            "UART2" : {"name":["U2EInterrupt", "U2RXInterrupt", "U2TXInterrupt"], "INT_SRC":uartIntSrc},
            "UART3" : {"name":["U3EInterrupt", "U3RXInterrupt", "U3TXInterrupt"], "INT_SRC":uartIntSrc},
            

            "SPI1" : {"name":["SPI1EInterrupt", "SPI1RXInterrupt", "SPI1TXInterrupt"], "INT_SRC":spiIntSrc},
            "SPI2" : {"name":["SPI2EInterrupt", "SPI2RXInterrupt", "SPI2TXInterrupt"], "INT_SRC":spiIntSrc},
            "SPI3" : {"name":["SPI3EInterrupt", "SPI3RXInterrupt", "SPI3TXInterrupt"], "INT_SRC":spiIntSrc},
            "SPI4" : {"name":["SPI4EInterrupt", "SPI4RXInterrupt", "SPI4TXInterrupt"], "INT_SRC":spiIntSrc},

          #  "I2C1" : {"name":["I2C1EInterrupt", "I2C1Interrupt"], "INT_SRC":i2cIntSrc},
          ##  "I2C3" : {"name":["I2C2EInterrupt", "I2C2Interrupt"], "INT_SRC":i2cIntSrc},
          #  "I2C4" : {"name":["I2C3EInterrupt", "I2C3Interrupt"], "INT_SRC":i2cIntSrc},
          #  "I2C5" : {"name":["I2C4EInterrupt", "I2C4Interrupt"], "INT_SRC":i2cIntSrc}

    }

    return corePeripherals

global calcWaitStates
global getWaitStates

    
def getWaitStates():
    return 0

def calcWaitStates(symbol, event):

    symbol.setValue(getWaitStates(), 2)
    

    

processor = Variables.get("__PROCESSOR")

print("Loading System Services for " + processor)

fuseSettings = coreComponent.createBooleanSymbol("FUSE_CONFIG_ENABLE", devCfgMenu)

fuseSettings.setLabel("Generate Fuse Settings")
fuseSettings.setDefaultValue(True)



global fuseCodeGenVal
fuseCodeGenVal = ""

fuseModuleGrp = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]')

# load device specific configurations (fuses), 
# loaded from atdf file
# Most fields are key/value pairs, but a handful of them are integer.  Need to know which ones those are.
# This line to be reviewed and updated
global bitfieldHexSymbols
bitfieldHexSymbols = [] 

global hexConfigBitPattern
hexConfigBitPattern = "FPR\d+ST_START|FPR\d+END_END|FPR\d+STBKUP_START|FPR\d+ENDBKUP_END|FEPUCB_EPUCB|FWPUCB_WPUCB"

global invalidConfigBitCaptionPattern
invalidConfigBitCaptionPattern = "FWDT_SWDTMPS|FWDT_RWDTPS"

global getConfigBitCaptionValue
def getConfigBitCaptionValue(configBitValueGroup,configBitVal):
    captionStr = ""
    atdfPath = '/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]/value-group@[name="'+ configBitValueGroup + '"]'
    valueGroupNode = ATDF.getNode(atdfPath)
    if(valueGroupNode != None):
        valGrpEntries = valueGroupNode.getChildren()
        for valGrpEntry in valGrpEntries:
            if( valGrpEntry.getAttribute("name") == configBitVal):
                captionStr = valGrpEntry.getAttribute("caption")
                break
    return captionStr 
     
global fuseConfigCb 
def fuseConfigCb(symbol, event):
    import re
    fuseCodeGenValue = ""
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]/register-group")
    register = node.getChildren()

    for reg_index in range(len(register)):
        symbolName = register[reg_index].getAttribute('name')
        fuseCodeGenValue += "\n// "+symbolName + "\n"
        bitfieldNode = register[reg_index].getChildren()
        for bitfield_index in range(len(bitfieldNode)):
             bitfieldName = bitfieldNode[bitfield_index].getAttribute('values')
             bitfieldValue = symbol.getComponent().getSymbolValue("CONFIG_"+bitfieldName)   
             if bitfieldValue is None:
                print("my bit is sad ", bitfieldName)         
             if re.match(hexConfigBitPattern, bitfieldName):
                desc = bitfieldNode[bitfield_index].getAttribute('caption')
                fuseCodeGenValue += "#pragma config {} = {}            // {}\n".format(bitfieldName, hex(int(bitfieldValue)).rstrip('L'),desc)
             else:
                desc = "" 
                if re.match(invalidConfigBitCaptionPattern, bitfieldName): 
                   desc = bitfieldNode[bitfield_index].getAttribute('caption')
                else:
                   desc = getConfigBitCaptionValue(bitfieldName, bitfieldValue)      
                fuseCodeGenValue += "#pragma config {} = {}            // {}\n".format(bitfieldName, bitfieldValue,desc)
    symbol.getComponent().setSymbolValue("FUSE_CONFIG_CODE_GEN",fuseCodeGenValue)            


node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]/register-group")
register = node.getChildren() # these are <register > fields for fuse config section
codeGenerationList = coreComponent.createListEntrySymbol("config_code", None)
for reg_index in range(len(register)):
    porValue = register[reg_index].getAttribute('initval')
    # print( " porValue %x = ", porValue)
    symbolName = register[reg_index].getAttribute('name')
    #print( " symbolName" + symbolName)
    menuitem = coreComponent.createMenuSymbol(symbolName, fuseSettings)
    menuitem.setVisible(True)
    menuitem.setLabel(symbolName)
    bitfields = register[reg_index].getChildren()
    
    fuseCodeGenVal += "\n// "+symbolName + "\n" 
    
    for bitfield_index in range(len(bitfields)):
        #bitfieldName = bitfields[bitfield_index].getAttribute('name')
        bitfieldName = bitfields[bitfield_index].getAttribute('values')
        #print( " bitfieldName" + bitfieldName)
        if re.match(hexConfigBitPattern, bitfieldName):
            bitfielditem = coreComponent.createHexSymbol('CONFIG_'+bitfieldName,menuitem) # symbol ID must match ftl file symbol
            bitfielditem.setDefaultValue(_find_default_value(bitfields[bitfield_index], porValue))
        else: # key value type symbol
            moduleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]")
            submodnode = moduleNode.getChildren()   # <value-group > entries
            for valuegroup_index in range(len(submodnode)): # scan over all <value-group ..> attributes (i.e., all bitfields) for our bitfieldName
                # extract field names from <value-group > items.  The part after the '__' is what we need here.
                name = submodnode[valuegroup_index].getAttribute('name')
                #posn = temp.find('__')
                #name = temp[posn+2:]
                #print( " value-group name" + name)
                if(name == bitfieldName):  # if we have a matching <value-group >, look at all children <value > fields
                    valuenode = submodnode[valuegroup_index].getChildren()  # look at all the <value ..> entries underneath <value-group >
                    keyVals = {}
                    for option_index in range(len(valuenode)):  # do this for each child <value ..> attribute for this bitfield
                        name2 = valuenode[option_index].getAttribute('name')
                        #print("key name = ",name2)
                        keyVals[valuenode[option_index].getAttribute("name")] = _process_valuegroup_entry(valuenode[option_index])
            bitfielditem = coreComponent.createComboSymbol('CONFIG_'+bitfieldName, menuitem, sort_alphanumeric(keyVals.keys()))
            if bitfieldName == "FWDT_WDTEN": #Deviation for WDT, Fusebits WDT Enable combo option set to default Value Software
                    if 'SW' in keyVals:
                      bitfielditem.setDefaultValue('SW')
                    else:
                        bitfielditem.setDefaultValue(_find_key(_find_default_value(bitfields[bitfield_index], porValue), keyVals))
            else:
                bitfielditem.setDefaultValue(_find_key(_find_default_value(bitfields[bitfield_index], porValue), keyVals))
        

        bitfielditem.setVisible(True)
        label = bitfields[bitfield_index].getAttribute('caption')+' ('+bitfields[bitfield_index].getAttribute('name')+')'
        bitfielditem.setLabel(label)
        description = bitfields[bitfield_index].getAttribute('caption')
        bitfielditem.setDescription(bitfields[bitfield_index].getAttribute('caption'))
        
        
        if re.match(hexConfigBitPattern, bitfieldName):
            fuseCodeGenVal += "#pragma config {} = {}            // {}\n".format(bitfieldName, hex(int(bitfielditem.getValue())).rstrip('L'),description)
        else:
            if re.match(invalidConfigBitCaptionPattern, bitfieldName) is None:
                description = getConfigBitCaptionValue(bitfieldName, bitfielditem.getValue())
            fuseCodeGenVal += "#pragma config {} = {}            // {}\n".format(bitfieldName, bitfielditem.getValue(),description)
        bitfielditem.setDependencies(fuseConfigCb,[bitfielditem.getID()])    
          
        

fuseCodeGenSymbol = coreComponent.createStringSymbol("FUSE_CONFIG_CODE_GEN", devCfgMenu)
fuseCodeGenSymbol.setVisible(False)       
fuseCodeGenSymbol.setDefaultValue(fuseCodeGenVal)
   
# End of scanning atdf file for parameters in fuse area

# The following symbols are created for the clock manager.
symbol = coreComponent.createBooleanSymbol("SYS_CLK_FSOSCEN_OVERRIDE", None)
symbol.setDefaultValue(False)
symbol.setReadOnly(True)
symbol.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(False)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

# productFamily (ID = "PRODUCT_FAMILY") symbol should be used everywhere to identify the product family
# This symbol is created inside core.py with the default value obtained from ATDF
# Since some of the ATDF doesn't give uniquely identifiable family name, same is updated in family python like this
#global productFamily
#productFamily.setDefaultValue("dsPIC33AK512MPS512")


# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_04449/config/clk.py")
#coreComponent.addPlugin("../peripheral/clk_04449/plugin/clockmanager.jar")

# load pin manager 
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_04928/config/gpio.py")
coreComponent.addPlugin("../peripheral/gpio_04928/plugin/gpio_02922.jar")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/intc_04436/config/intc.py")
coreComponent.addPlugin(
    "../../harmony-services/plugins/generic_plugin.jar",
    "INTC_04436_MANAGER",
    {
        "plugin_name": "Interrupt Configuration",
        "main_html_path": "csp/plugins/configurators/interrupt_configurators/intc_04436_interrupt_configuration/build/index.html",
        "componentId": coreComponent.getID()
    },
)

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_04650/config/wdt.py")

#load dma
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dma_04077/config/dma.py")

#load dmt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmt_04735/config/dmt.py")

#load pac
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_04649/config/pac.py")

# load dma manager information
# To be updated


#fuse bit code generation
devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
# To be added
devconSystemInitFile.setSourcePath("mchp/templates/dsPIC33AK.c.ftl")
devconSystemInitFile.setMarkup(True)
