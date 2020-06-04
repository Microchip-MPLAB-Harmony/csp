
def setUpMemFuse(symbol, event):
    global fuseMapSymbol
    Database.setSymbolValue("core", fuseMapSymbol[event["id"].split("_SIZE")[0]], long(event["value"]))

def setUpFuse(symbol, event):
    global fuseMapSymbol
    for key in fuseMapSymbol.keys():
        if '_' in key and key.split("_")[1] == event["id"].split("_IS_NON_SECURE")[0]:
            if event["value"]:
                Database.setSymbolValue("core", fuseMapSymbol[key], 1)
            else:
                Database.setSymbolValue("core", fuseMapSymbol[key], 0)

def nonSecStartAddressCalculate(symbol, value):
    global memoryGranularity
    asSize = int(Database.getSymbolValue("core", "IDAU_AS_SIZE"))
    bootProtSize = int(Database.getSymbolValue("core", "IDAU_BOOTPROT_SIZE"))

    symbol.setValue( (asSize * memoryGranularity["IDAU_AS"] ) + (bootProtSize * memoryGranularity["IDAU_BOOTPROT"]))

global fuseMapSymbol
global fusedependencyList
fusedependencyList = []
global memoryfusedependencyList
memoryfusedependencyList = []
global memoryFuseMaxValue
global memoryGranularity
memoryGranularity = {}

trustZoneMenu = coreComponent.createMenuSymbol("TRUSTZONE_MENU", devCfgMenu)
trustZoneMenu.setLabel("TrustZone Manager")

alwaysSecurePeripheralList = ["GCLK", "OSCCTRL", "OSC32KCTRL", "MCLK", "IDAU", "NVMCTRL", "PAC"]

dummyList = coreComponent.createListSymbol( "NULL_LIST",       None )
peripheralList = coreComponent.createListEntrySymbol("TRUSTZONE_PERIPHERAL_LIST", None)
peripheralList.setVisible(False)
#Sort peripheral list in alphabetical order
for key, value in sorted(fuseMapSymbol.items(), key = lambda arg:arg[0].split("_")[1] if '_' in arg[0] else arg[0]):
    if key.startswith("NONSEC") and key.split("_")[1] not in alwaysSecurePeripheralList:
        peripheralIsNonSecure = coreComponent.createBooleanSymbol(key.split("_")[1] + "_IS_NON_SECURE", trustZoneMenu)
        peripheralIsNonSecure.setLabel(key.split("_")[1] + " is Non-Secure")
        peripheralList.addValue(key.split("_")[1])
        fusedependencyList.append(key.split("_")[1] + "_IS_NON_SECURE")
peripheralList.setTarget("core.NULL_LIST")

fuseUpdateCallback = coreComponent.createBooleanSymbol("DUMMY_SYMBOL_CALLBACK", None)
fuseUpdateCallback.setVisible(False)
fuseUpdateCallback.setDependencies(setUpFuse, fusedependencyList)

memoryMenu = coreComponent.createMenuSymbol("MEMORY_MENU", devCfgMenu)
memoryMenu.setLabel("Memory configurator")

idauNode = ATDF.getNode("/avr-tools-device-file/devices/device/peripherals/module@[name=\"IDAU\"]/instance@[name=\"IDAU\"]/parameters")
for parameter in idauNode.getChildren():
    if "GRANULARITY_AS" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_AS"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_ANSC" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_ANSC"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_RS" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_RS"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_BS" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_BS"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_BNSC" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_BNSC"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_DS" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_DS"] = int(parameter.getAttribute("value"), 16)
    elif "GRANULARITY_BOOTPROT" in parameter.getAttribute("name"):
        memoryGranularity["IDAU_BOOTPROT"] = int(parameter.getAttribute("value"), 16)

addr_space          = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space")
addr_space_children = addr_space.getChildren()

for mem_idx in range(0, len(addr_space_children)):
    mem_seg     = addr_space_children[mem_idx].getAttribute("name")

    if (mem_seg == "FLASH"):
        maxFlashSize = coreComponent.createIntegerSymbol("DEVICE_FLASH_SIZE", None)
        maxFlashSize.setVisible(False)
        maxFlashSize.setDefaultValue(int(addr_space_children[mem_idx].getAttribute("size"), 16))

    if (mem_seg == "HSRAM"):
        maxRamSize = coreComponent.createIntegerSymbol("DEVICE_RAM_SIZE", None)
        maxRamSize.setVisible(False)
        maxRamSize.setDefaultValue(int(addr_space_children[mem_idx].getAttribute("size"), 16))

    if (mem_seg == "DATAFLASH"):
        maxDataflashSize = coreComponent.createIntegerSymbol("DEVICE_DATAFLASH_SIZE", None)
        maxDataflashSize.setVisible(False)
        maxDataflashSize.setDefaultValue(int(addr_space_children[mem_idx].getAttribute("size"), 16))

for key in memoryFuseMaxValue.keys():
    asSizeSymbol = coreComponent.createKeyValueSetSymbol( str(key) + "_SIZE", memoryMenu)
    asSizeSymbol.setLabel(memoryFuseMaxValue[key][2] + " size")
    for val in range(0, (memoryFuseMaxValue[key][0] + 1)):
        size = val * memoryGranularity[key]
        sizeString = str(size) + " Bytes"
        asSizeSymbol.addKey(sizeString, str(hex(int(size))), '{:,}'.format(size) + " Bytes")
    asSizeSymbol.setDefaultValue(memoryFuseMaxValue[key][1])
    asSizeSymbol.setOutputMode("Key")
    asSizeSymbol.setDisplayMode("Description")
    memoryfusedependencyList.append(str(key) + "_SIZE")

    asGranularitySymbol =  coreComponent.createIntegerSymbol( str(key) + "_GRANULARITY", memoryMenu)
    asGranularitySymbol.setVisible(False)
    asGranularitySymbol.setDefaultValue(memoryGranularity[key])

memfuseUpdateCallback = coreComponent.createBooleanSymbol("DUMMY_MEM_SYMBOL_CALLBACK", None)
memfuseUpdateCallback.setVisible(False)
memfuseUpdateCallback.setDependencies(setUpMemFuse, memoryfusedependencyList)

Database.setSymbolValue("core", "IDAU_AS_SIZE", maxFlashSize.getValue() / (memoryGranularity["IDAU_AS"] * 2) )
Database.setSymbolValue("core", "IDAU_RS_SIZE", maxRamSize.getValue() / (memoryGranularity["IDAU_RS"] * 2) )
Database.setSymbolValue("core", "IDAU_ANSC_SIZE", 512 / (memoryGranularity["IDAU_ANSC"]) )

nonSecStartAddress = coreComponent.createHexSymbol("NON_SEC_START_ADDRESS", None)
nonSecStartAddress.setVisible(False)
nonSecStartAddress.setDefaultValue((int(Database.getSymbolValue("core", "IDAU_AS_SIZE")) * memoryGranularity["IDAU_AS"])
                                 + (int(Database.getSymbolValue("core", "IDAU_BOOTPROT_SIZE")) * memoryGranularity["IDAU_BOOTPROT"]))
nonSecStartAddress.setDependencies(nonSecStartAddressCalculate, ["IDAU_AS_SIZE", "IDAU_BOOTPROT_SIZE"])

secSystemDefinitionsHeadersList =      coreComponent.createListSymbol( "LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES",       None )
secsystemIntVectorsMultipleHandlesList =   coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_MULTIPLE_HANDLERS",  None )
secsystemIntVectorsWeakHandlesList =       coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_WEAK_HANDLERS",      None )
secsystemIntVectorsHandlesList =           coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SECURE_HANDLERS",           None )

secsystemInitFuseList =        coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_CONFIG_BITS_INITIALIZATION",    None )
secsystemInitStartList =       coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START",          None )
secsystemInitCoreList =        coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE",           None )
secsystemInitPeripheral1List = coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS1",   None )
secsystemInitCore1List =       coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_CORE1",          None )
secsystemInitPeripheralList =  coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_PERIPHERALS",    None )
secsystemInterruptEnableList = coreComponent.createListSymbol( "LIST_SYSTEM_SECURE_INIT_INTERRUPTS",    None )

BspSecureHeaderIncludeList   = coreComponent.createListSymbol( "LIST_BSP_MACRO_SECURE_INCLUDES",    None )
BspSecureInitList            = coreComponent.createListSymbol( "LIST_BSP_SECURE_INITIALIZATION",    None )

secdefHeaderFile = coreComponent.createFileSymbol("SECURE_DEFINITIONS_H", None)
secdefHeaderFile.setSourcePath("templates/trustZone/definitions_secure.h.ftl")
secdefHeaderFile.setOutputName("definitions.h")
secdefHeaderFile.setMarkup(True)
secdefHeaderFile.setOverwrite(True)
secdefHeaderFile.setDestPath("")
secdefHeaderFile.setProjectPath("config/" + configName + "/")
secdefHeaderFile.setType("HEADER")
secdefHeaderFile.setSecurity("SECURE")

## cache macros
secdeviceCacheHeaderFile = coreComponent.createFileSymbol("SECURE_DEVICE_CACHE_H", None)
secdeviceCacheHeaderFile.setSourcePath( "templates/cache_cortex_m.h.ftl")
secdeviceCacheHeaderFile.setOutputName("device_cache.h")
secdeviceCacheHeaderFile.setMarkup(True)
secdeviceCacheHeaderFile.setOverwrite(True)
secdeviceCacheHeaderFile.setDestPath("")
secdeviceCacheHeaderFile.setProjectPath("config/" + configName + "/")
secdeviceCacheHeaderFile.setType("HEADER")
secdeviceCacheHeaderFile.setSecurity("SECURE")

# generate interrupts.c file
secintSourceFile = coreComponent.createFileSymbol( "SECURE_INTERRUPTS_C", None )
secintSourceFile.setSourcePath("templates/trustZone/interrupts_secure.c.ftl")
secintSourceFile.setOutputName("interrupts.c")
secintSourceFile.setMarkup(True)
secintSourceFile.setOverwrite(True)
secintSourceFile.setDestPath("")
secintSourceFile.setProjectPath("config/" + configName + "/")
secintSourceFile.setType("SOURCE")
secintSourceFile.setSecurity("SECURE")

secinitSourceFile = coreComponent.createFileSymbol("SECURE_INITIALIZATION_C", None)
secinitSourceFile.setSourcePath("templates/trustZone/initialization_secure.c.ftl")
secinitSourceFile.setOutputName("initialization.c")
secinitSourceFile.setMarkup(True)
secinitSourceFile.setOverwrite(True)
secinitSourceFile.setDestPath("")
secinitSourceFile.setProjectPath("config/" + configName + "/")
secinitSourceFile.setType("SOURCE")
secinitSourceFile.setSecurity("SECURE")

secmainSourceFile = coreComponent.createFileSymbol("SEC_MAIN_C", None)
secmainSourceFile.setSourcePath("templates/trustZone/main_secure.c.ftl")
secmainSourceFile.setOutputName("main.c")
secmainSourceFile.setMarkup(True)
secmainSourceFile.setOverwrite(False)
secmainSourceFile.setDestPath("../../")
secmainSourceFile.setProjectPath("")
secmainSourceFile.setType("SOURCE")
secmainSourceFile.setSecurity("SECURE")
secmainSourceFile.setDependencies( genMainSourceFile, ["CoreMainFile", "CoreMainFileName"] )

secVeneerSourceFile = coreComponent.createFileSymbol("SECURE_VENEER_C", None)
secVeneerSourceFile.setSourcePath("templates/trustZone/veneer.c.ftl")
secVeneerSourceFile.setOutputName("veneer.c")
secVeneerSourceFile.setMarkup(True)
secVeneerSourceFile.setOverwrite(False)
secVeneerSourceFile.setDestPath("../../trustZone/")
secVeneerSourceFile.setProjectPath("trustZone/")
secVeneerSourceFile.setType("SOURCE")
secVeneerSourceFile.setSecurity("SECURE")

secVeneerHeaderFile = coreComponent.createFileSymbol("SECURE_VENEER_H", None)
secVeneerHeaderFile.setSourcePath("templates/trustZone/veneer.h.ftl")
secVeneerHeaderFile.setOutputName("veneer.h")
secVeneerHeaderFile.setMarkup(True)
secVeneerHeaderFile.setOverwrite(False)
secVeneerHeaderFile.setDestPath("../../trustZone/")
secVeneerHeaderFile.setProjectPath("trustZone/")
secVeneerHeaderFile.setType("HEADER")
secVeneerHeaderFile.setSecurity("SECURE")

secSourceFile = coreComponent.createFileSymbol("SECURE_C", None)
secSourceFile.setSourcePath("templates/trustZone/secure.c.ftl")
secSourceFile.setOutputName("secure.c")
secSourceFile.setMarkup(True)
secSourceFile.setOverwrite(False)
secSourceFile.setDestPath("../../trustZone/")
secSourceFile.setProjectPath("trustZone/")
secSourceFile.setType("SOURCE")
secSourceFile.setSecurity("SECURE")

secHeaderFile = coreComponent.createFileSymbol("SECURE_H", None)
secHeaderFile.setSourcePath("templates/trustZone/secure.h.ftl")
secHeaderFile.setOutputName("secure.h")
secHeaderFile.setMarkup(True)
secHeaderFile.setOverwrite(False)
secHeaderFile.setDestPath("../../trustZone/")
secHeaderFile.setProjectPath("trustZone/")
secHeaderFile.setType("HEADER")
secHeaderFile.setSecurity("SECURE")

secVeneerHeaderFile = coreComponent.createFileSymbol("VENEER_H", None)
secVeneerHeaderFile.setSourcePath("templates/trustZone/veneer.h.ftl")
secVeneerHeaderFile.setOutputName("veneer.h")
secVeneerHeaderFile.setMarkup(True)
secVeneerHeaderFile.setOverwrite(False)
secVeneerHeaderFile.setDestPath("../../trustZone/")
secVeneerHeaderFile.setProjectPath("trustZone/")
secVeneerHeaderFile.setType("HEADER")

def calculateASSize(symbol, event):
    symbol.setValue("AS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
def calculateANSCSize(symbol, event):
    symbol.setValue("ANSC=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_ANSC"]) * int(memoryGranularity["IDAU_ANSC"]))).replace("L", ""))
def calculateRSSize(symbol, event):
    symbol.setValue("RS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
def calculateBootProtSize(symbol, event):
    symbol.setValue("BOOTPROT=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))

# for Secure Project
# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("SECURE")
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_AS_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("AS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateASSize, [fuseMapSymbol["IDAU_AS"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_ANSC_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("ANSC=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_ANSC"]) * int(memoryGranularity["IDAU_ANSC"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateANSCSize, [fuseMapSymbol["IDAU_ANSC"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RS_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("RS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateRSSize, [fuseMapSymbol["IDAU_RS"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_BOOTPROT_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("BOOTPROT=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateBootProtSize, [fuseMapSymbol["IDAU_BOOTPROT"]])
xc32LinkerMacro.setSecurity("SECURE")

#For Non Secure
# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_AS_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("AS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
xc32LinkerMacro.setDependencies(calculateASSize, [fuseMapSymbol["IDAU_AS"]])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RS_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("RS=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateRSSize, [fuseMapSymbol["IDAU_RS"]])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_BOOTPROT_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("BOOTPROT=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";")
xc32LinkerMacro.setDependencies(calculateBootProtSize, [fuseMapSymbol["IDAU_BOOTPROT"]])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("NONSECURE")
xc32LinkerMacro.setAppend(True, ";")

defSym = coreComponent.createSettingSymbol("SEC_XC32_INCLUDE_DIRS", None)
defSym.setCategory("C32")
defSym.setKey("extra-include-directories")
defSym.setValue( "../src;../src/config/" + configName
                + ";../src/packs/" + processor + "_DFP;"
                + corePath
                + ";../src/packs/CMSIS/;../src/" + baseArchDir
                )
defSym.setAppend(True, ";")
defSym.setSecurity("SECURE")

xc32CMSECompilerFlag =  coreComponent.createSettingSymbol("SEC_XC32_CMSE_FLAG", None)
xc32CMSECompilerFlag.setCategory("C32")
xc32CMSECompilerFlag.setKey("appendMe")
xc32CMSECompilerFlag.setValue("-mcmse")
xc32CMSECompilerFlag.setAppend(True, ";")
xc32CMSECompilerFlag.setSecurity("SECURE")

xc32CMSELinkerFlag =  coreComponent.createSettingSymbol("SEC_XC32_LINKER_CMSE_FLAG", None)
xc32CMSELinkerFlag.setCategory("C32-LD")
xc32CMSELinkerFlag.setKey("appendMe")
xc32CMSELinkerFlag.setValue( "--out-implib=" + str(Variables.get("__SECURE_PROJECT_FOLDER_NAME")).replace('.X', '') + "_sg_veneer.lib" + " ,--cmse-implib")
xc32CMSELinkerFlag.setAppend(True, ";")
xc32CMSELinkerFlag.setSecurity("SECURE")

xc32LinkerLibraryPath =  coreComponent.createSettingSymbol("XC32_LINKER_LIBRARY_", None)
xc32LinkerLibraryPath.setCategory("C32-LD")
xc32LinkerLibraryPath.setKey("appendMe")
xc32LinkerLibraryPath.setValue( "-l:" + str(Variables.get("__SECURE_PROJECT_FOLDER_NAME")).replace('.X', '') + "_sg_veneer.lib")
xc32LinkerLibraryPath.setAppend(True, ";")

xc32LinkerLibraryDirectoryPath = coreComponent.createSettingSymbol("XC32_LINKER_LIBRARY_DIR_PATH", None)
xc32LinkerLibraryDirectoryPath.setCategory("C32-LD")
xc32LinkerLibraryDirectoryPath.setKey("extra-lib-directories")
xc32LinkerLibraryDirectoryPath.setValue("../../../Secure/firmware/" + str(Variables.get("__SECURE_PROJECT_FOLDER_NAME")))
xc32LinkerLibraryDirectoryPath.setAppend(True, ";")

# set XC32 option to not use the device startup code
xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("SEC_XC32_NO_DEVICE_STARTUP_CODE", None)
xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
xc32NoDeviceStartupCodeSym.setValue("true")
xc32NoDeviceStartupCodeSym.setSecurity("SECURE")

## toolchain specifics
toolChainSpecifics = coreComponent.createFileSymbol( "SEC_TOOLCHAIN_SPECIFICS_H", None )
toolChainSpecifics.setSourcePath( baseArchDir + "/templates/toolchain_specifics.h.ftl" )
toolChainSpecifics.setOutputName( "toolchain_specifics.h" );
toolChainSpecifics.setMarkup( True )
toolChainSpecifics.setOverwrite( True )
toolChainSpecifics.setDestPath("")
toolChainSpecifics.setProjectPath("config/" + configName + "/")
toolChainSpecifics.setSecurity("SECURE")
toolChainSpecifics.setType("HEADER")

global secdebugSourceFile
global compilerSelected
compilerSelected = compilerChoice.getSelectedKey().replace( naQualifier, "" ).lower()
secdebugSourceFile = coreComponent.createFileSymbol( "SECURE_DEBUG_CONSOLE_C", None )
secdebugSourceFile.setMarkup( True )
secdebugSourceFile.setOverwrite( True )
secdebugSourceFile.setDestPath( "/stdio/" )
secdebugSourceFile.setProjectPath( "config/" + configName + "/stdio/" )
secdebugSourceFile.setType( "SOURCE" )
secdebugSourceFile.setDependencies( genSysSourceFile, [ "CoreSysStdioSyscallsFile", "CoreSysFiles" ] )
secdebugSourceFile.setSourcePath( "../arch/arm/templates/" + compilerSelected + "/stdio/trustZone/" + compilerSelected + "_monitor.c.ftl" )
secdebugSourceFile.setOutputName( compilerSelected + "_monitor.c" )
secdebugSourceFile.setSecurity("SECURE")

secexceptSourceFile = coreComponent.createFileSymbol("SECURE_EXCEPTIONS_C", None)
secexceptSourceFile.setSourcePath("templates/trustZone/exceptions_xc32_cortex_m_secure.c.ftl")
secexceptSourceFile.setOutputName("exceptions.c")
secexceptSourceFile.setMarkup(True)
secexceptSourceFile.setOverwrite(True)
secexceptSourceFile.setDestPath("")
secexceptSourceFile.setProjectPath("config/" + configName + "/")
secexceptSourceFile.setType("SOURCE")
secexceptSourceFile.setDependencies( genSysSourceFile, [ "CoreSysExceptionFile", "CoreSysFiles", "ADVANCED_EXCEPTION" ] )
secexceptSourceFile.setSecurity("SECURE")

coreComponent.addPlugin("../arch/config/plugin/trustzone_manager.jar")