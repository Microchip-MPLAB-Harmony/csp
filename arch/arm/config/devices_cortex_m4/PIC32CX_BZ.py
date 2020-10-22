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

global xc32StackInTCMSym
global xc32DTCMSizeSym
global xc32ITCMSizeSym
global tcmSize
global tcmEnable
global fuseMenu

# ///////////////////////Symbol Creation for Fuses ////////////////////////// #
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
    print("_find_key: could not find value in dictionary",val,str(value), keyname) # should never get here
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

def getMaxValue(mask):
    if mask == 0 :
        return hex(0)

    mask = int(mask, 16)
    while (mask % 2) == 0:
        mask = mask >> 1

    return mask

def xc32SetTcmSize(symbol, event):
    symObj=event["symbol"]
    if (symObj.getSelectedKey() == "0KB"):
        xc32DTCMSizeSym.setValue("")
        xc32ITCMSizeSym.setValue("")
    elif (symObj.getSelectedKey() == "2KB"):
        xc32DTCMSizeSym.setValue("0x800")
        xc32ITCMSizeSym.setValue("0x800")
    elif (symObj.getSelectedKey() == "3KB"):
        xc32DTCMSizeSym.setValue("0xC00")
        xc32ITCMSizeSym.setValue("0xC00")
    elif (symObj.getSelectedKey() == "4KB"):
        xc32DTCMSizeSym.setValue("0x1000")
        xc32ITCMSizeSym.setValue("0x1000")

def xc32SetStackInTcm(symbol, event):
    if (event["value"] == True):
        xc32StackInTCMSym.setValue("true")
    else:
        xc32StackInTCMSym.setValue("false")

def populate_config_items(basenode, baseLabel, moduleNode, component, parentMenu, visibility):
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
                if bitfields[jj].getAttribute('values') is None:
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

                if bitfields[jj].getAttribute('values') is None:
                    bitfielditem.setDefaultValue(_find_default_value(bitfields[jj], porValue))

                label = bitfields[jj].getAttribute('caption')+' ('+bitfields[jj].getAttribute('name')+')'
                bitfielditem.setLabel(label)
                bitfielditem.setDescription(bitfields[jj].getAttribute('caption'))

    # by default ATDF sets POSCMOD value to OFF, change it here
    if Database.getSymbolValue("core", "CONFIG_POSCMOD") != None:
        Database.setSymbolValue("core", "CONFIG_POSCMOD", "HS")

global getWaitStates
def getWaitStates():
    sysclk = int(Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY"))
    if sysclk <= 33000000:
        ws = 0
    else:
        ws = 1
    return ws

def calcWaitStates(symbol, event):
    symbol.setValue(getWaitStates(), 2)

# load family specific configurations
print("Loading System Services for " + Variables.get("__PROCESSOR"))

# loaded from atdf file
node = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]/register-group")
populate_config_items(node, 'CONFIG_', ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"FUSES\"]"), coreComponent, devCfgMenu, True)


# SysTick External Clock Source
systickExternal = coreComponent.createBooleanSymbol("SYSTICK_EXTERNAL_CLOCK", devCfgMenu)
systickExternal.setLabel("External Clock Source for SysTick Available")
systickExternal.setDefaultValue(False)
systickExternal.setVisible(False)

coreFPU = coreComponent.createBooleanSymbol("FPU_Available", devCfgMenu)
coreFPU.setLabel("FPU Available")
coreFPU.setDefaultValue(True)
coreFPU.setReadOnly(True)
coreFPU.setVisible(False)

deviceFamily = coreComponent.createStringSymbol("DeviceFamily", devCfgMenu)
deviceFamily.setLabel("Device Family")
deviceFamily.setDefaultValue("PIC32CX_BZ")
deviceFamily.setReadOnly(True)
deviceFamily.setVisible(False)

cortexMenu = coreComponent.createMenuSymbol("CORTEX_MENU", None)
cortexMenu.setLabel("Cortex-M4 Configuration")
cortexMenu.setDescription("Configuration for Cortex M4")

cacheMenu = coreComponent.createMenuSymbol("CACHE_MENU", cortexMenu)
cacheMenu.setLabel("CMCC Configuration")
cacheMenu.setDescription("CACHE Configuration")

# TCM exists on PIC3CX_BZ and cannot be disabled. Only its size can be  configured.
# We need this symbol defined so that the FTL will emit the code associated
# with TCM configuration.
tcmEnable = coreComponent.createBooleanSymbol("TCM_ENABLE", cacheMenu)
tcmEnable.setLabel("Enable TCM")
tcmEnable.setDefaultValue(True)
tcmEnable.setReadOnly(True)
tcmEnable.setVisible(False)

deviceTCMsize = coreComponent.createKeyValueSetSymbol("DEVICE_TCM_SIZE", cacheMenu)
deviceTCMsize.setLabel("TCM and cache Size")
deviceTCMsize.setOutputMode("Value")
deviceTCMsize.setDisplayMode("Description")
deviceTCMsize.addKey("0KB", "2", "TCM: 0 KB, Cache: 4 KB" )
deviceTCMsize.addKey("2KB", "1", "TCM: 2 KB, Cache: 2 KB")
deviceTCMsize.addKey("3KB", "0", "TCM: 3 KB, Cache: 1 KB")
deviceTCMsize.addKey("4KB", "3", "TCM: 4 KB,  Cache: 0 KB")
deviceTCMsize.setSelectedKey("0KB")


dcacheEnable = coreComponent.createBooleanSymbol("DATA_CACHE_ENABLE", cacheMenu)
dcacheEnable.setLabel("Enable Data Cache")
dcacheEnable.setDefaultValue(False)

icacheEnable = coreComponent.createBooleanSymbol("INSTRUCTION_CACHE_ENABLE", cacheMenu)
icacheEnable.setLabel("Enable Instruction Cache")
icacheEnable.setDefaultValue(True)

stackTCM = coreComponent.createBooleanSymbol("STACK_IN_TCM", cacheMenu)
stackTCM.setLabel("Locate Stack in TCM")
stackTCM.setDefaultValue(False)
stackTCM.setVisible(False)

cacheAlign = coreComponent.createIntegerSymbol("CACHE_ALIGN", cacheMenu)
cacheAlign.setLabel("Cache Alignment Length")
cacheAlign.setVisible(False)
cacheAlign.setDefaultValue(16)

periInstanceMultiVectorSupport = coreComponent.createBooleanSymbol("PERIPHERAL_MULTI_VECTOR", None)
periInstanceMultiVectorSupport.setDefaultValue(True)
periInstanceMultiVectorSupport.setVisible(False)

def getCorePeripherals():

    # Components which are creating critical section
    corePeripherals = ["DMAC", "RTC", "TC", "SERCOM"]

    return corePeripherals

def setDMACDefaultSettings():

    triggerSettings = {
                        "Software Trigger"  : ["BLOCK", "INCREMENTED_AM", "INCREMENTED_AM", "WORD"],
                        "Standard_Transmit" : ["BEAT", "INCREMENTED_AM", "FIXED_AM", "BYTE"],
                        "Standard_Receive"  : ["BEAT", "FIXED_AM", "INCREMENTED_AM", "BYTE"]
                    }

    return triggerSettings


def setMPUDefaultSettings():
    mpuRegions = 8
    mpuSettings = {"FLASH"              : ["MPU_ATTR_NORMAL_WT",           "MPU_RASR_AP_READWRITE_Val",    "",     "",     "0x00000000",   "4MB"   ],
                    "SRAM"              : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "8MB"],
                    "PERIPHERALS"       : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                    "SYSTEM"            : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ],
                    "QSPI"              : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x04000000",   "256MB"],}
    mpuSetUpLogicList = ["FLASH", "SRAM", "PERIPHERALS", "SYSTEM", "QSPI"]

    return mpuRegions, mpuSettings, mpuSetUpLogicList

prefetchMenu = coreComponent.createMenuSymbol("PREFETCH_MENU", None)
prefetchMenu.setLabel("Prefetch and Flash Configuration")
prefetchMenu.setDescription("Configure Prefetch and Flash")

SYM_REFEN = coreComponent.createKeyValueSetSymbol("CONFIG_CHECON_PREFEN", prefetchMenu)
SYM_REFEN.setLabel("Predictive Prefetch Configuration")
SYM_REFEN.addKey("DISABLE", "0", "Disable predictive prefetch")
SYM_REFEN.addKey("ENABLE", "1", "Enable predictive prefetch for CPU instructions only")
SYM_REFEN.setOutputMode("Value")
SYM_REFEN.setDisplayMode("Description")
SYM_REFEN.setDefaultValue(1)

# load clock manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/clk_pic32cx_bz/config/clk.py")
coreComponent.addPlugin("../peripheral/clk_pic32cx_bz/plugin/clockmanager.jar")

SYM_PFMWS = coreComponent.createIntegerSymbol("CONFIG_CHECON_PFMWS", prefetchMenu)
SYM_PFMWS.setLabel("Program Flash memory Wait states")
SYM_PFMWS.setDefaultValue(getWaitStates())
SYM_PFMWS.setMin(0)
SYM_PFMWS.setMax(1)
SYM_PFMWS.setReadOnly(False)
SYM_PFMWS.setDependencies(calcWaitStates, ["CPU_CLOCK_FREQUENCY"])

# load pin manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/gpio_02467/config/gpio_pic32c.py")
coreComponent.addPlugin("../peripheral/gpio_02467/plugin/gpio_02467.jar")

# # load NVIC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/nvic/config/nvic.py")
coreComponent.addPlugin("../peripheral/nvic/plugin/nvic.jar")

# #load mpu
execfile(Variables.get("__CORE_DIR") + "/../peripheral/mpu/config/mpu.py")
coreComponent.addPlugin("../peripheral/mpu/plugin/mpu.jar")

# #load systick
execfile(Variables.get("__CORE_DIR") + "/../peripheral/systick/config/systick.py")

# # load dma manager information
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmac_u2503/config/dmac.py")
coreComponent.addPlugin("../peripheral/dmac_u2503/plugin/dmamanager.jar")

# # load wdt
periphNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"WDT\"]")
id = periphNode.getAttribute("id").lower()
execfile(Variables.get("__CORE_DIR") + "/../peripheral/wdt_" + id + "/config/wdt_pic32c.py")

# load dmt
execfile(Variables.get("__CORE_DIR") + "/../peripheral/dmt_01520/config/dmt.py")

# load PAC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/pac_u2120/config/pac.py")

#  load CMCC
execfile(Variables.get("__CORE_DIR") + "/../peripheral/cmcc_u2015/config/cmcc.py")

# Activate Event System
periphNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"EVSYS\"]")
modules = periphNode.getChildren()
components = []
for evsys_instance in range (0, len(modules)):
    components.append(str(modules[evsys_instance].getAttribute("name")).lower())
Database.activateComponents(components)

global armLibCSourceFile
global devconSystemInitFile
global compilerSpecifics

compilerSelected = compilerChoice.getSelectedKey().lower()

armSysStartSourceFile = coreComponent.createFileSymbol("STARTUP_C", None)
armSysStartSourceFile.setSourcePath("../arch/arm/templates/" + compilerSelected + "/cortex_m/startup/startup_" + compilerSelected + ".c.ftl")
armSysStartSourceFile.setOutputName("startup_" + compilerSelected + ".c")
armSysStartSourceFile.setMarkup(True)
armSysStartSourceFile.setOverwrite(True)
armSysStartSourceFile.setDestPath("")
armSysStartSourceFile.setProjectPath("config/" + configName + "/")
armSysStartSourceFile.setType("SOURCE")
armSysStartSourceFile.setDependencies(
    genSysSourceFile, ["CoreSysStartupFile", "CoreSysFiles"])

# generate libc_syscalls.c file
armLibCSourceFile = coreComponent.createFileSymbol("LIBC_SYSCALLS_C", None)
armLibCSourceFile.setSourcePath("arm/templates/xc32/libc_syscalls.c.ftl")
armLibCSourceFile.setOutputName("libc_syscalls.c")
armLibCSourceFile.setMarkup(True)
armLibCSourceFile.setOverwrite(True)
armLibCSourceFile.setDestPath("")
armLibCSourceFile.setProjectPath("config/" + configName + "/")
armLibCSourceFile.setType("SOURCE")
armLibCSourceFile.setDependencies(genSysSourceFile, ["CoreSysCallsFile", "CoreSysFiles"])

# set XC32 ITCM Size
xc32ITCMSizeSym = coreComponent.createSettingSymbol("XC32_ITCM_SIZE", None)
xc32ITCMSizeSym.setCategory("C32Global")
xc32ITCMSizeSym.setKey("mitcm")
xc32ITCMSizeSym.setValue("")
xc32ITCMSizeSym.setDependencies(xc32SetTcmSize, ["DEVICE_TCM_SIZE"])

# set XC32 DTCM Size
xc32DTCMSizeSym = coreComponent.createSettingSymbol("XC32_DTCM_SIZE", None)
xc32DTCMSizeSym.setCategory("C32Global")
xc32DTCMSizeSym.setKey("mdtcm")
xc32DTCMSizeSym.setValue("")
xc32DTCMSizeSym.setDependencies(xc32SetTcmSize, ["DEVICE_TCM_SIZE"])

# set XC32 Stack in TCM: True or False
xc32StackInTCMSym = coreComponent.createSettingSymbol("XC32_STACK_IN_TCM", None)
xc32StackInTCMSym.setCategory("C32Global")
xc32StackInTCMSym.setKey("mstacktcm")
xc32StackInTCMSym.setValue("false")
xc32StackInTCMSym.setDependencies(xc32SetStackInTcm, ["STACK_IN_TCM"])

# fuse configuration generation
devconSystemInitFile = coreComponent.createFileSymbol("DEVICE_CONFIG_SYSTEM_INIT", None)
devconSystemInitFile.setType("STRING")
devconSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION")
devconSystemInitFile.setSourcePath("arm/templates/common/fuses/PIC32CX_BZ.c.ftl")
devconSystemInitFile.setMarkup(True)

# wait state and prefetch cache setting
devconInitFile = coreComponent.createFileSymbol("DEVCON_INIT", None)
devconInitFile.setType("STRING")
devconInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE")
devconInitFile.setSourcePath("arm/templates/common/PIC32CX_BZ_DEVCON.c.ftl")
devconInitFile.setMarkup(True)

compilerSpecifics = [armSysStartSourceFile]
