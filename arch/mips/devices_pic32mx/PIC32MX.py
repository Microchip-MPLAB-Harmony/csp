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

def getCorePeripheralsInterruptDataStructure():

    dmacVectName = ["DMA0", "DMA1", "DMA2", "DMA3"]
    dmacIntSrc = ["CHANNEL0", "CHANNEL1", "CHANNEL2", "CHANNEL3"]
    uartIntSrc = ["USART_ERROR", "USART_RX", "USART_TX_COMPLETE"]
    spiIntSrc = ["SPI_ERROR", "SPI_RX", "SPI_TX_COMPLETE"]
    i2cIntSrc = ["I2C_0", "I2C_1"]

    corePeripherals = {

            "DMAC" : {"name":dmacVectName, "INT_SRC":dmacIntSrc},

            "UART1" : {"name":["UART1_ERR", "UART1_RX", "UART1_TX"], "INT_SRC":uartIntSrc},
            "UART2" : {"name":["UART2_ERR", "UART2_RX", "UART2_TX"], "INT_SRC":uartIntSrc},
            "UART3" : {"name":["UART3_ERR", "UART3_RX", "UART3_TX"], "INT_SRC":uartIntSrc},
            "UART4" : {"name":["UART4_ERR", "UART4_RX", "UART4_TX"], "INT_SRC":uartIntSrc},
            "UART5" : {"name":["UART5_ERR", "UART5_RX", "UART5_TX"], "INT_SRC":uartIntSrc},

            "SPI1" : {"name":["SPI1_ERR", "SPI1_RX", "SPI1_TX"], "INT_SRC":spiIntSrc},
            "SPI2" : {"name":["SPI2_ERR", "SPI2_RX", "SPI2_TX"], "INT_SRC":spiIntSrc},
            "SPI3" : {"name":["SPI3_ERR", "SPI3_RX", "SPI3_TX"], "INT_SRC":spiIntSrc},
            "SPI4" : {"name":["SPI4_ERR", "SPI4_RX", "SPI4_TX"], "INT_SRC":spiIntSrc},

            "I2C1" : {"name":["I2C1_BUS", "I2C1_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C2" : {"name":["I2C2_BUS", "I2C2_MASTER"], "INT_SRC":i2cIntSrc}

    }

    return corePeripherals

global calcWaitStates
global getWaitStates

def getWaitStates():

    sysclk = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))

    ws = 3

    if deviceFamily.getValue() == "DS60001404":
        if sysclk <= 72000000:
            ws = 3
        if sysclk <= 54000000:
            ws = 2
        if sysclk <= 36000000:
            ws = 1
        if sysclk <= 18000000:
            ws = 0
    else:
        tempRange =  Database.getSymbolValue("core", "CONFIG_TEMPERATURE_RANGE")

        # -40 Deg to +105 Deg: 80MHz Maximum Frequency
        if tempRange == 0:
            if sysclk <= 80000000:
                ws = 2
            if sysclk <= 60000000:
                ws = 1
            if sysclk <= 30000000:
                ws = 0
        else:
        # 0 Deg to 70 Deg: 120 MHz Maximum Frequency
            if sysclk <= 120000000:
                ws = 3
        # -40 Deg to +85 Deg: 100MHz Maximum Frequency
            if sysclk <= 100000000:
                ws = 2
            if sysclk <= 80000000:
                ws = 1
            if sysclk <= 40000000:
                ws = 0

    return ws

def calcWaitStates(symbol, event):

    symbol.setValue(getWaitStates(), 2)

processor = Variables.get("__PROCESSOR")

print("Loading System Services for " + processor)

fuseModuleGrp = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]')

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
# loaded from atdf file
# Most fields are key/value pairs, but a handful of them are integer.  Need to know which ones those are.
bitfieldHexSymbols = [ 'USERID', 'TSEQ', 'CSEQ' ]

node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]/register-group")
register = node.getChildren() # these are <register > fields for fuse config section
for ii in range(len(register)):
    porValue = register[ii].getAttribute('initval')
    symbolName = register[ii].getAttribute('name')
    menuitem = coreComponent.createMenuSymbol(symbolName, devCfgMenu)
    menuitem.setVisible(True)
    menuitem.setLabel(symbolName)
    bitfields = register[ii].getChildren()
    for jj in range(len(bitfields)):
        bitfieldName = bitfields[jj].getAttribute('name')
        if(bitfieldName in bitfieldHexSymbols):
            bitfielditem = coreComponent.createHexSymbol('CONFIG_'+bitfieldName,menuitem) # symbol ID must match ftl file symbol
        else: # key value type symbol
            moduleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]")
            submodnode = moduleNode.getChildren()   # <value-group > entries
            for kk in range(len(submodnode)): # scan over all <value-group ..> attributes (i.e., all bitfields) for our bitfieldName
                # extract field names from <value-group > items.  The part after the '__' is what we need here.
                temp = submodnode[kk].getAttribute('name')
                posn = temp.find('__')
                name = temp[posn+2:]
                if(name == bitfieldName):  # if we have a matching <value-group >, look at all children <value > fields
                    valuenode = submodnode[kk].getChildren()  # look at all the <value ..> entries underneath <value-group >
                    keyVals = {}
                    for ll in range(len(valuenode)):  # do this for each child <value ..> attribute for this bitfield
                        keyVals[valuenode[ll].getAttribute("name")] = _process_valuegroup_entry(valuenode[ll])
            bitfielditem = coreComponent.createComboSymbol('CONFIG_'+bitfieldName, menuitem, sorted(keyVals.keys()))
            bitfielditem.setDefaultValue(_find_key(_find_default_value(bitfields[jj], porValue),keyVals))

        bitfielditem.setVisible(True)

        if(bitfieldName in bitfieldHexSymbols):
            bitfielditem.setDefaultValue(_find_default_value(bitfields[jj], porValue))

        label = bitfields[jj].getAttribute('caption')+' ('+bitfields[jj].getAttribute('name')+')'
        bitfielditem.setLabel(label)
        bitfielditem.setDescription(bitfields[jj].getAttribute('caption'))
# End of scanning atdf file for parameters in fuse area

# The following symbols are not used in Chicagoland, but are created for the clock manager.
symbol = coreComponent.createBooleanSymbol("SYS_CLK_FSOSCEN_OVERRIDE", None)
symbol.setDefaultValue(False)
symbol.setReadOnly(True)
symbol.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

ds60001168Regex = re.compile(r'[12][12357]0F\d+[BCD]')  #PIC32MX1XX/2XX
ds60001185Regex = re.compile(r'[34][357]0F')            #PIC32MX330/350/370/430/450/470
ds60001290Regex = re.compile(r'[125][2357]0F\d+[HL]')   #PIC32MX1XX/2XX/5XX
ds60001404Regex = re.compile(r'[12][57]4F')             #PIC32MX1XX/2XX XLP

global deviceFamily

deviceFamily = coreComponent.createStringSymbol("DEVICE_FAMILY", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

mipsMenu = coreComponent.createMenuSymbol("MIPS MENU", None)
mipsMenu.setLabel("MIPS Configuration")
mipsMenu.setDescription("Configuration for MIPS processor")

# decide on the family this processor belongs
if  ds60001168Regex.search(processor):
    deviceFamily.setDefaultValue("DS60001168")
elif ds60001185Regex.search(processor):
    deviceFamily.setDefaultValue("DS60001185")
elif ds60001290Regex.search(processor):
    deviceFamily.setDefaultValue("DS60001290")
elif ds60001404Regex.search(processor):
    deviceFamily.setDefaultValue("DS60001404")

pcacheNode = ATDF.getNode('/avr-tools-device-file/modules/module@[name="PCACHE"]')

if pcacheNode != None:
    prefetchMenu = coreComponent.createMenuSymbol("PREFETCH_MENU", None)
    prefetchMenu.setLabel("Prefetch and Flash Configuration")
    prefetchMenu.setDescription("Configure Prefetch and Flash")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32mx/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32mx/plugin/clockmanager.jar")

if pcacheNode != None:
    SYM_REFEN = coreComponent.createKeyValueSetSymbol("CONFIG_CHECON_PREFEN", prefetchMenu)
    SYM_REFEN.setLabel("Predictive Prefetch Configuration")
    SYM_REFEN.addKey("OPTION1", "0", "Disable predictive prefetch")
    SYM_REFEN.addKey("OPTION2", "1", "Enable predictive prefetch for cacheable regions only")
    SYM_REFEN.addKey("OPTION3", "2", "Enable predictive prefetch for non-cacheable regions only")
    SYM_REFEN.addKey("OPTION4", "3", "Enable predictive prefetch for both cacheable and non-cacheable regions")
    SYM_REFEN.setOutputMode("Value")
    SYM_REFEN.setDisplayMode("Description")
    SYM_REFEN.setDefaultValue(3)

    SYM_PFMWS = coreComponent.createIntegerSymbol("CONFIG_CHECON_PFMWS", prefetchMenu)
    SYM_PFMWS.setLabel("Program Flash memory Wait states")
    SYM_PFMWS.setDefaultValue(getWaitStates())
    SYM_PFMWS.setReadOnly(True)
    SYM_PFMWS.setDependencies(calcWaitStates, ["CPU_CLOCK_FREQUENCY", "CONFIG_TEMPERATURE_RANGE"])

if deviceFamily.getValue() == "DS60001185":
    execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_01618/config/gpio.py")
    coreComponent.addPlugin("../peripheral/gpio_01618/plugin/gpio_01618.jar")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", mipsMenu)
cacheMenu.setLabel("(no additional MIPS configuration)")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/evic_02907/config/evic.py")
coreComponent.addPlugin("../peripheral/evic_02907/plugin/evic_02907.jar")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_01385/config/wdt.py")

# load dma manager information
#  execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_01500/config/dmac.py")
#  coreComponent.addPlugin("../peripheral/dmac_01500/plugin/dmamanager.jar")

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("mips/templates/PIC32MX.c.ftl")
devconSystemInitFile.setMarkup(True)

devconInitFile = coreComponent.createFileSymbol("DEVCON_INIT", None)
devconInitFile.setType("STRING")
devconInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
devconInitFile.setSourcePath("mips/templates/PIC32MX_DEVCON.c.ftl")
devconInitFile.setMarkup(True)