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

    


print("Loading System Services for " + Variables.get("__PROCESSOR"))

fuseModuleGrp = ATDF.getNode('/avr-tools-device-file/modules/module@[name="FUSECONFIG"]')

# load device specific configurations (fuses), temporary, to be removed once XC32 updated
# loaded from atdf file
# Most fields are key/value pairs, but a handful of them are integer.  Need to know which ones those are.
bitfieldIntegerSymbols = [ 'USERID', 'TSEQ', 'CSEQ' ]

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
        if(bitfieldName in bitfieldIntegerSymbols):
            bitfielditem = coreComponent.createIntegerSymbol('CONFIG_'+bitfieldName,menuitem) # symbol ID must match ftl file symbol
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
        
        if(bitfieldName in bitfieldIntegerSymbols):
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

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32mz/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32mz/plugin/clockmanager.jar")

# load device specific pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_02467/config/gpio.py")
#coreComponent.addPlugin("../peripheral/gpio_02467/plugin/pinmanager.jar")
print("NO JAR PINMANAGER FILE AVAILABLE FOR MZ/EF - SKIP LOADING FOR NOW")

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
devconSystemInitFile.setSourcePath("mips/templates/PIC32MZ_EF.c.ftl")
devconSystemInitFile.setMarkup(True)

