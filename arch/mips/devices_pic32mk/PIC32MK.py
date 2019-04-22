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

    dmacVectName = ["DMA0", "DMA1", "DMA2", "DMA3", "DMA4", "DMA5", "DMA6", "DMA7"]
    dmacIntSrc = ["CHANNEL0", "CHANNEL1", "CHANNEL2", "CHANNEL3", "CHANNEL4", "CHANNEL5", "CHANNEL6", "CHANNEL7"]
    uartIntSrc = ["USART_ERROR", "USART_RX", "USART_TX_COMPLETE"]
    spiIntSrc = ["SPI_ERROR", "SPI_RX", "SPI_TX_COMPLETE"]
    i2cIntSrc = ["I2C_0", "I2C_1"]

    corePeripherals = {

            "DMAC" : {"name":dmacVectName, "INT_SRC":dmacIntSrc},

            "UART1" : {"name":["UART1_FAULT", "UART1_RX", "UART1_TX"], "INT_SRC":uartIntSrc},
            "UART2" : {"name":["UART2_FAULT", "UART2_RX", "UART2_TX"], "INT_SRC":uartIntSrc},
            "UART3" : {"name":["UART3_FAULT", "UART3_RX", "UART3_TX"], "INT_SRC":uartIntSrc},
            "UART4" : {"name":["UART4_FAULT", "UART4_RX", "UART4_TX"], "INT_SRC":uartIntSrc},
            "UART5" : {"name":["UART5_FAULT", "UART5_RX", "UART5_TX"], "INT_SRC":uartIntSrc},
            "UART6" : {"name":["UART6_FAULT", "UART6_RX", "UART6_TX"], "INT_SRC":uartIntSrc},

            "SPI1" : {"name":["SPI1_FAULT", "SPI1_RX", "SPI1_TX"], "INT_SRC":spiIntSrc},
            "SPI2" : {"name":["SPI2_FAULT", "SPI2_RX", "SPI2_TX"], "INT_SRC":spiIntSrc},
            "SPI3" : {"name":["SPI3_FAULT", "SPI3_RX", "SPI3_TX"], "INT_SRC":spiIntSrc},
            "SPI4" : {"name":["SPI4_FAULT", "SPI4_RX", "SPI4_TX"], "INT_SRC":spiIntSrc},
            "SPI5" : {"name":["SPI5_FAULT", "SPI5_RX", "SPI5_TX"], "INT_SRC":spiIntSrc},
            "SPI6" : {"name":["SPI6_FAULT", "SPI6_RX", "SPI6_TX"], "INT_SRC":spiIntSrc},

            "I2C1" : {"name":["I2C1_BUS", "I2C1_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C2" : {"name":["I2C2_BUS", "I2C2_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C3" : {"name":["I2C3_BUS", "I2C3_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C4" : {"name":["I2C4_BUS", "I2C4_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C5" : {"name":["I2C5_BUS", "I2C5_MASTER"], "INT_SRC":i2cIntSrc}

    }

    return corePeripherals

global getWaitStates

def getWaitStates():

    sysclk = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    ws = 3

    if sysclk <= 120000000:
        ws = 3
    if sysclk <= 80000000:
        ws = 2
    if sysclk <= 60000000:
        ws = 1

    return ws

def calcWaitStates(symbol, event):

    symbol.setValue(getWaitStates(), 2)

print("Loading System Services for " + Variables.get("__PROCESSOR"))

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

mipsMenu = coreComponent.createMenuSymbol("MIPS MENU", None)
mipsMenu.setLabel("MIPS Configuration")
mipsMenu.setDescription("Configuration for MIPS processor")

prefetchMenu = coreComponent.createMenuSymbol("PREFETCH_MENU", None)
prefetchMenu.setLabel("Prefetch and Flash Configuration")
prefetchMenu.setDescription("Configure Prefetch and Flash")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32mk/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32mk/plugin/clockmanager.jar")

SYM_REFEN = coreComponent.createKeyValueSetSymbol("CONFIG_CHECON_PREFEN", prefetchMenu)
SYM_REFEN.setLabel("Predictive Prefetch Configuration")
SYM_REFEN.addKey("OPTION1", "0", "Disable predictive prefetch")
SYM_REFEN.addKey("OPTION2", "1", "Enable predictive prefetch for CPU instructions only")
SYM_REFEN.setOutputMode("Value")
SYM_REFEN.setDisplayMode("Description")
SYM_REFEN.setDefaultValue(1)

SYM_PFMWS = coreComponent.createIntegerSymbol("CONFIG_CHECON_PFMWS", prefetchMenu)
SYM_PFMWS.setLabel("Program Flash memory Wait states")
SYM_PFMWS.setDefaultValue(getWaitStates())
SYM_PFMWS.setReadOnly(False)
SYM_PFMWS.setDependencies(calcWaitStates, ["CPU_CLOCK_FREQUENCY"])

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_02467/config/gpio.py")
coreComponent.addPlugin("../peripheral/gpio_02467/plugin/gpio_02467.jar")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", mipsMenu)
cacheMenu.setLabel("(no additional MIPS configuration)")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/evic_02907/config/evic.py")
coreComponent.addPlugin("../peripheral/evic_02907/plugin/evic_02907.jar")

# load dmt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmt_01520/config/dmt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_02674/config/wdt.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_01500/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_01500/plugin/dmamanager.jar")

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("mips/templates/PIC32MK.c.ftl")
devconSystemInitFile.setMarkup(True)

devconInitFile = coreComponent.createFileSymbol("DEVCON_INIT", None)
devconInitFile.setType("STRING")
devconInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
devconInitFile.setSourcePath("mips/templates/PIC32MK_DEVCON.c.ftl")
devconInitFile.setMarkup(True)