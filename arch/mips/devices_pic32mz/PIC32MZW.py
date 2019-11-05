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

global _find_default_value

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

global _find_key

def _find_key(value, keypairs):
    '''
    Helper function that finds the keyname for the given value.  Needed for setting up combo symbol value.
          value - the value to be looked for in the dictionary
          keypairs - the dictionary to be searched over
    '''
    for keyname, val in keypairs.items():
        if(val == str(value)):
            return keyname
    print("_find_key: could not find value in dictionary",val,str(value)) # should never get here
    return ""

global _process_valuegroup_entry

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

            "SPI1" : {"name":["SPI1_FAULT", "SPI1_RX", "SPI1_TX"], "INT_SRC":spiIntSrc},
            "SPI2" : {"name":["SPI2_FAULT", "SPI2_RX", "SPI2_TX"], "INT_SRC":spiIntSrc},

            "I2C1" : {"name":["I2C1_BUS", "I2C1_MASTER"], "INT_SRC":i2cIntSrc},
            "I2C2" : {"name":["I2C2_BUS", "I2C2_MASTER"], "INT_SRC":i2cIntSrc}
    }

    return corePeripherals

global getWaitStates

def getWaitStates():

    sysclk = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    ws = 7

    if sysclk <= 250000000:
        ws = 7
    if sysclk <= 240000000:
        ws = 6
    if sysclk <= 200000000:
        ws = 5
    if sysclk <= 160000000:
        ws = 4
    if sysclk <= 120000000:
        ws = 3
    if sysclk <= 80000000:
        ws = 2
    if sysclk <= 40000000:
        ws = 1

    return ws

def calcWaitStates(symbol, event):

    symbol.setValue(getWaitStates(), 1)

global updateCFGCON3

def updateCFGCON3(menu,event):
    # updates the CFGCON3 register based on one of 3 bitfield values that can change
    value = int(Database.getSymbolValue("core", "CFGCON3_VALUE"))
    if('SPLLPOSTDIV2' in event['id']):
        mask = Database.getSymbolValue("core", "SPLLPOSTDIV2_MASK")
    elif('ETHPLLPOSTDIV2' in event['id']):
        mask = Database.getSymbolValue("core", "ETHPLLPOSTDIV2_MASK")
    elif('BTPLLPOSTDIV2' in event['id']):
        mask = Database.getSymbolValue("core", "ETHPLLPOSTDIV2_MASK")
    else:
        mask = '0'
    maskval = int(mask.split('0x')[1],16)
    newvalue = value & ~maskval
    shift = 0
    for ii in range(0,32):
        if( ((maskval >> ii) & 1) != 0):
            shift = ii
            break
    newvalue = newvalue + (int(event['value'])<<shift)
    Database.setSymbolValue("core", "CFGCON3_VALUE", newvalue, 2)

def make_config_reg_items(basenode, component, parentMenu):
    # Extracts the configuration registers that are relevant.  There are some fields that are the only way to control certain settings
    # and thus need to be exposed to the user.  
    node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/register-group/register@[name=\"CFGCON3\"]")
    cfgcon3 = component.createIntegerSymbol('CFGCON3_VALUE', parentMenu)
    cfgcon3.setVisible(False)
    cfgcon3.setDefaultValue(int(node.getAttribute('initval'),16))
    cfgcon3.setDependencies(updateCFGCON3,['CFG_SPLLPOSTDIV2', 'CFG_ETHPLLPOSTDIV2', 'CFG_BTPLLPOSTDIV2'])
    cfgcon3name = component.createStringSymbol('CFGCON3_NAME', parentMenu)
    cfgcon3name.setVisible(False)
    cfgcon3name.setDefaultValue(node.getAttribute('name'))


def populate_config_items(basenode, bitfieldHexSymbols, baseLabel, moduleNode, component, parentMenu, visibility):
    no_symbol_list = ['CFGCON0','CFGCON1','CFGCON2','CFGCON4','CFGPG']  # not needed to populate symbols that user does not control
    register = basenode.getChildren() # these are <register > fields for fuse or cfg sections
    for ii in range(len(register)):
        porValue = register[ii].getAttribute('initval')
        if((porValue != None) and (register[ii].getAttribute('name') not in no_symbol_list)):
            symbolName = register[ii].getAttribute('name')
            menuitem = component.createMenuSymbol(symbolName, parentMenu)
            menuitem.setVisible(visibility)
            menuitem.setLabel(symbolName)
            bitfields = register[ii].getChildren()
            for jj in range(len(bitfields)):
                bitfieldName = bitfields[jj].getAttribute('name')
                if(bitfieldName in bitfieldHexSymbols):
                    bitfielditem = component.createHexSymbol(baseLabel+bitfieldName,menuitem) # symbol ID must match ftl file symbol
                else: # key value type symbol
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
                    bitfielditem = component.createComboSymbol(baseLabel+bitfieldName, menuitem, sorted(keyVals.keys()))
                    bitfielditem.setDefaultValue(_find_key(_find_default_value(bitfields[jj], porValue),keyVals))

                bitfielditem.setVisible(visibility)

                if(bitfieldName in bitfieldHexSymbols):
                    bitfielditem.setDefaultValue(_find_default_value(bitfields[jj], porValue))

                label = bitfields[jj].getAttribute('caption')+' ('+bitfields[jj].getAttribute('name')+')'
                bitfielditem.setLabel(label)
                bitfielditem.setDescription(bitfields[jj].getAttribute('caption'))

clkValGrp_DEVCFG0__FECCCON = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]/value-group@[name="DEVCFG0__FECCCON"]')
print("Loading System Services for " + Variables.get("__PROCESSOR"))
fuseModuleGrp = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]')

# loaded from atdf file
# Most fields are key/value pairs, but a handful of them are integer.  Need to know which ones those are.
bitfieldHexSymbols = [ 'USERID', 'SOSCCFG', 'CANFDDIV', 'USBDMTRIM', 'USBDPTRIM' ]
node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]/register-group")
populate_config_items(node, bitfieldHexSymbols, 'CONFIG_', ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSECONFIG\"]"), coreComponent, devCfgMenu, True)

bitfieldHexSymbols = ['SPLLPOSTDIV2', 'ETHPLLPOSTDIV2', 'BTPLLPOSTDIV2']
node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]/register-group")
populate_config_items(node, bitfieldHexSymbols, 'CFG_', ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"CFG\"]"), coreComponent, devCfgMenu, True)
make_config_reg_items(node, coreComponent, devCfgMenu)

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
prefetchMenu.setLabel("Flash Configuration")
prefetchMenu.setDescription("Configure Prefetch and Flash")

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32mzw/config/clk.py")
#coreComponent.addPlugin("../peripheral/clk_pic32mzw/plugin/clockmanager.jar")

SYM_PFMWS = coreComponent.createIntegerSymbol("CONFIG_PRECON_PFMWS", prefetchMenu)
SYM_PFMWS.setReadOnly(False)
SYM_PFMWS.setDefaultValue(getWaitStates())
SYM_PFMWS.setLabel("Program Flash memory wait states")
SYM_PFMWS.setDependencies(calcWaitStates, ["CPU_CLOCK_FREQUENCY"])

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_02467/config/gpio.py")
coreComponent.addPlugin("../peripheral/gpio_02467/plugin/gpio_02467.jar")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", mipsMenu)
cacheMenu.setLabel("CACHE")
cacheMenu.setDescription("CACHE Configuration")

#execfile(Variables.get("__CORE_DIR") + "/../peripheral/cache/config/cache.py")

execfile(Variables.get("__CORE_DIR") + "/../peripheral/evic_02907/config/evic.py")
coreComponent.addPlugin("../peripheral/evic_02907/plugin/evic_02907.jar")

# load dmt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmt_01520/config/dmt.py")

# load wdt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_02674/config/wdt.py")

# load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_01500/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_01500/plugin/dmamanager.jar")

MLDOInitFile = coreComponent.createFileSymbol("MLDO_C_INIT", None)
MLDOInitFile.setSourcePath("templates/system_pmu_mldo_trim.c.ftl")
MLDOInitFile.setOutputName("system_pmu_mldo_trim.c")
MLDOInitFile.setDestPath("/")
MLDOInitFile.setProjectPath("config/" + CONFIG_NAME)
MLDOInitFile.setType("SOURCE")
MLDOInitFile.setMarkup(True)

devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("mips/templates/PIC32MZ_W.c.ftl")
devconSystemInitFile.setMarkup(True)

devconInitFile = coreComponent.createFileSymbol("DEVCON_INIT", None)
devconInitFile.setType("STRING")
devconInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
devconInitFile.setSourcePath("mips/templates/PIC32MZ_DEVCON.c.ftl")
devconInitFile.setMarkup(True)