# coding: utf-8
"""*****************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

def secStartAddressCalculate(symbol, value):
    global memoryGranularity
    bootProtSize = int(Database.getSymbolValue("core", "IDAU_BOOTPROT_SIZE"))

    symbol.setValue(bootProtSize * memoryGranularity["IDAU_BOOTPROT"])

def updateGenSecureBootsymbol(symbol, event):
    if event["value"] == 0:
        symbol.setVisible(False)
    else:
        symbol.setVisible(True)

def updateSecureEnabledState(symbol, event):
    symbol.setEnabled(not event["value"])

def updateSecureBootloaderEnabledState(symbol, event):
    symbol.setEnabled(event["value"])


global get_implib_details
def get_implib_details(boot_suffix=""):
    from os import path
    lib_name = "{0}{1}_sg_veneer.lib".format(
                    Variables.get("__SECURE_PROJECT_FOLDER_NAME").replace('.X', ''), boot_suffix)
    secure_project_path = path.join(Variables.get("__SECURE_PROJECT_FIRMWARE_PATH"),
                                     Variables.get("__SECURE_PROJECT_FOLDER_NAME"))
    lib_path = path.join(Variables.get("__NON_SECURE_PROJECT_FIRMWARE_PATH"),
                                        Variables.get("__NON_SECURE_PROJECT_FOLDER_NAME"),
                                        lib_name)
    lib_rel_path = path.relpath(lib_path, secure_project_path).replace("\\", "/")
    return lib_name, lib_rel_path


def updateSecureBootSettings(symbol, event):
    if ((event["id"] == "IDAU_ANSC_SIZE") or (event["id"] == "IDAU_BNSC_SIZE")):
        anscSize = Database.getSymbolValue("core", "IDAU_ANSC_SIZE")
        bnscSize = Database.getSymbolValue("core", "IDAU_BNSC_SIZE")

        # Do not generate the veneer library and non secure callable files if
        # Application non-secure and Boot non-secure callable region size is 0
        if ((anscSize == 0) and (bnscSize == 0)):
            symbol.setEnabled(False)
        else:
            symbol.setEnabled(True)
    else:
        id = symbol.getID()
        boot_suffix = "_boot" if event["value"] else ""

        implib_name, implib_rel_path = get_implib_details(boot_suffix)
        if id == "NONSECURE_ENTRY_C":
            symbol.setOutputName("nonsecure_entry" + boot_suffix + ".c")
        elif id == "NONSECURE_ENTRY_H":
            symbol.setOutputName("nonsecure_entry" + boot_suffix + ".h")
        elif id == "SEC_XC32_LINKER_CMSE_FLAG":
            symbol.setValue( "--out-implib={0} ,--cmse-implib".format(implib_rel_path))
        elif id == "XC32_LINKER_LIBRARY_":
            symbol.setValue( "-l:{0}".format(implib_name))


global fuseMapSymbol
global fusedependencyList
fusedependencyList = []
global memoryfusedependencyList
memoryfusedependencyList = []
global memoryFuseMaxValue
global memoryGranularity
memoryGranularity = {}


trustZonePeripheralMenu = coreComponent.createMenuSymbol("TZ_PERIPHERAL_MENU", trustZoneMenu)
trustZonePeripheralMenu.setLabel("Peripherals")
trustZoneMixSecurePeripheralMenu = coreComponent.createMenuSymbol("TZ_MIX_SECURE_PERIPHERAL_MENU", trustZoneMenu)
trustZoneMixSecurePeripheralMenu.setLabel("Mix-Secure Peripherals")
trustZoneSystemResourcesMenu = coreComponent.createMenuSymbol("TZ_SYSTEM_RESOURCES_MENU", trustZoneMenu)
trustZoneSystemResourcesMenu.setLabel("System Resources")

dummyList = coreComponent.createListSymbol( "NULL_LIST",       None )
peripheralList = coreComponent.createListEntrySymbol("TRUSTZONE_PERIPHERAL_LIST", None)
peripheralList.setVisible(False)
peripheralIndexListTempGUI = []
peripheralIndexListGUI = []
mixSecurePeripheralIndexListGUI = []
systemPeripheralIndexListGUI = []
#Sort peripheral list in alphabetical order
for key, value in sorted(fuseMapSymbol.items(), key = lambda arg:arg[0].split("_")[1] if '_' in arg[0] else arg[0]):
    trustZonePeripheralSubmenu = trustZonePeripheralMenu
    peripheralIndexListTempGUI = peripheralIndexListGUI
    if key.startswith("NONSEC") and key.split("_")[1] in mixSecurePeripheralList:
        trustZonePeripheralSubmenu = trustZoneMixSecurePeripheralMenu
        peripheralIndexListTempGUI = mixSecurePeripheralIndexListGUI
    elif key.startswith("NONSEC") and key.split("_")[1] in systemResourcesList:
        trustZonePeripheralSubmenu = trustZoneSystemResourcesMenu
        peripheralIndexListTempGUI = systemPeripheralIndexListGUI
    if key.startswith("NONSEC") and key.split("_")[1]:
        peripheralIndexListTempGUI.append(key.split("_")[1])
        peripheralIsNonSecure = coreComponent.createBooleanSymbol(key.split("_")[1] + "_IS_NON_SECURE", trustZonePeripheralSubmenu)
        peripheralIsNonSecure.setLabel(key.split("_")[1] + " is Non-Secure")
        peripheralList.addValue(key.split("_")[1])
        fusedependencyList.append(key.split("_")[1] + "_IS_NON_SECURE")
        if ((key.startswith("NONSEC") and key.split("_")[1] in mixSecurePeripheralList) or
            (key.startswith("NONSEC") and key.split("_")[1] in systemResourcesList)):
            peripheralIsNonSecure.setReadOnly(True)
        if key.startswith("NONSEC") and key.split("_")[1] == "DSU":
            peripheralIsNonSecure.setDefaultValue(True)
            peripheralIsNonSecure.setReadOnly(True)
            Database.setSymbolValue("core", fuseMapSymbol[key], 1)
peripheralList.setTarget("core.NULL_LIST")
###################################################################################################
# Below symbols is only used by TrustZone UI to know Peripherals data
peripheralsListID = coreComponent.createComboSymbol("TZ_PERIPHERAL_MENU_GUI", trustZoneMenu, peripheralIndexListGUI)
peripheralsListID.setVisible(False)
mixSecurePeripheralsListID = coreComponent.createComboSymbol("TZ_MIX_SECURE_PERIPHERAL_MENU_GUI", trustZoneMenu, mixSecurePeripheralIndexListGUI)
mixSecurePeripheralsListID.setVisible(False)
systemPeripheralsListID = coreComponent.createComboSymbol("TZ_SYSTEM_RESOURCES_MENU_GUI", trustZoneMenu, systemPeripheralIndexListGUI)
systemPeripheralsListID.setVisible(False)
#####################################################
fuseUpdateCallback = coreComponent.createBooleanSymbol("DUMMY_SYMBOL_CALLBACK", None)
fuseUpdateCallback.setVisible(False)
fuseUpdateCallback.setDependencies(setUpFuse, fusedependencyList)


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
        if key == "IDAU_DS" and size > maxDataflashSize.getValue():
            break
        if (key in ["IDAU_AS", "IDAU_ANSC", "IDAU_BS", "IDAU_BNSC", "IDAU_BOOTPROT"]) and size > maxFlashSize.getValue():
            break
        if key == "IDAU_RS" and size > maxRamSize.getValue():
            break
        sizeString = str(size) + " Bytes"
        asSizeSymbol.addKey(sizeString, str(hex(int(size))), '{:,}'.format(size) + " Bytes")
    if memoryFuseMaxValue[key][1] < asSizeSymbol.getKeyCount():
        asSizeSymbol.setDefaultValue(memoryFuseMaxValue[key][1])
    else:
        asSizeSymbol.setDefaultValue(asSizeSymbol.getKeyCount() - 1)
    asSizeSymbol.setOutputMode("Key")
    asSizeSymbol.setDisplayMode("Description")
    memoryfusedependencyList.append(str(key) + "_SIZE")
    if key == "IDAU_BOOTPROT":
        generateSecureBootMainFile = coreComponent.createBooleanSymbol("GENERATE_SECURE_BOOT_MAIN_FILE", asSizeSymbol)
        generateSecureBootMainFile.setLabel("Generate Secure Boot Main Source File")
        generateSecureBootMainFile.setDefaultValue(False)
        generateSecureBootMainFile.setVisible(False)
        generateSecureBootMainFile.setDependencies(updateGenSecureBootsymbol, [str(key) + "_SIZE"])

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

secStartAddress = coreComponent.createHexSymbol("SEC_START_ADDRESS", None)
secStartAddress.setVisible(False)
secStartAddress.setDefaultValue(int(Database.getSymbolValue("core", "IDAU_BOOTPROT_SIZE")) * memoryGranularity["IDAU_BOOTPROT"])
secStartAddress.setDependencies(secStartAddressCalculate, ["IDAU_BOOTPROT_SIZE"])

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
secintSourceFile.setDependencies(genSysSourceFile, ["CoreSysIntFile", "CoreSysFiles"])

# generate interrupts.h file
secintHeaderFile = coreComponent.createFileSymbol( "SECURE_INTERRUPTS_H", None )
secintHeaderFile.setSourcePath("templates/trustZone/interrupts.h.ftl")
secintHeaderFile.setOutputName("interrupts.h")
secintHeaderFile.setMarkup(True)
secintHeaderFile.setOverwrite(True)
secintHeaderFile.setDestPath("")
secintHeaderFile.setProjectPath("config/" + configName + "/")
secintHeaderFile.setType("HEADER")
secintHeaderFile.setSecurity("SECURE")
secintHeaderFile.setDependencies(genSysSourceFile, ["CoreSysIntFile", "CoreSysFiles"])

# generate device_vectors.h file
secintHeaderFile = coreComponent.createFileSymbol( "SECURE_DEVICE_VECTORS_H", None )
secintHeaderFile.setSourcePath("templates/trustZone/device_vectors_secure.h.ftl")
secintHeaderFile.setOutputName("device_vectors.h")
secintHeaderFile.setMarkup(True)
secintHeaderFile.setOverwrite(True)
secintHeaderFile.setDestPath("")
secintHeaderFile.setProjectPath("config/" + configName + "/")
secintHeaderFile.setType("HEADER")
secintHeaderFile.setSecurity("SECURE")

secinitSourceFile = coreComponent.createFileSymbol("SECURE_INITIALIZATION_C", None)
secinitSourceFile.setSourcePath("templates/trustZone/initialization_secure.c.ftl")
secinitSourceFile.setOutputName("initialization.c")
secinitSourceFile.setMarkup(True)
secinitSourceFile.setOverwrite(True)
secinitSourceFile.setDestPath("")
secinitSourceFile.setProjectPath("config/" + configName + "/")
secinitSourceFile.setType("SOURCE")
secinitSourceFile.setSecurity("SECURE")
secinitSourceFile.setDependencies( genSysSourceFile, [ "CoreSysInitFile", "CoreSysFiles" ] )

secmainSourceFile = coreComponent.createFileSymbol("SEC_MAIN_C", None)
secmainSourceFile.setSourcePath("templates/trustZone/main_secure.c.ftl")
secmainSourceFile.setOutputName("main.c")
secmainSourceFile.setMarkup(True)
secmainSourceFile.setOverwrite(False)
secmainSourceFile.setDestPath("../../")
secmainSourceFile.setProjectPath("")
secmainSourceFile.setType("SOURCE")
secmainSourceFile.setSecurity("SECURE")
secmainSourceFile.setDependencies( genMainSourceFile, ["CoreMainFile", "CoreMainFileName", "CPLUSPLUS_PROJECT"] )

nonsecureEntrySourceFile = coreComponent.createFileSymbol("NONSECURE_ENTRY_C", None)
nonsecureEntrySourceFile.setSourcePath("templates/trustZone/nonsecure_entry.c.ftl")
nonsecureEntrySourceFile.setOutputName("nonsecure_entry.c")
nonsecureEntrySourceFile.setMarkup(True)
nonsecureEntrySourceFile.setOverwrite(False)
nonsecureEntrySourceFile.setDestPath("../../trustZone/")
nonsecureEntrySourceFile.setProjectPath("trustZone/")
nonsecureEntrySourceFile.setType("SOURCE")
nonsecureEntrySourceFile.setSecurity("SECURE")
nonsecureEntrySourceFile.setDependencies(updateSecureBootSettings, ["GENERATE_SECURE_BOOT_MAIN_FILE", "IDAU_ANSC_SIZE", "IDAU_BNSC_SIZE"])

nonsecureEntryHeaderFile = coreComponent.createFileSymbol("NONSECURE_ENTRY_H", None)
nonsecureEntryHeaderFile.setSourcePath("templates/trustZone/nonsecure_entry.h.ftl")
nonsecureEntryHeaderFile.setOutputName("nonsecure_entry.h")
nonsecureEntryHeaderFile.setMarkup(True)
nonsecureEntryHeaderFile.setOverwrite(False)
nonsecureEntryHeaderFile.setDestPath("../../trustZone/")
nonsecureEntryHeaderFile.setProjectPath("trustZone/")
nonsecureEntryHeaderFile.setType("HEADER")
nonsecureEntryHeaderFile.setDependencies(updateSecureBootSettings, ["GENERATE_SECURE_BOOT_MAIN_FILE", "IDAU_ANSC_SIZE", "IDAU_BNSC_SIZE"])

def calculateASSize(symbol, event):
    symbol.setValue("AS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
def calculateANSCSize(symbol, event):
    symbol.setValue("ANSC_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_ANSC"]) * int(memoryGranularity["IDAU_ANSC"]))).replace("L", ""))
def calculateRSSize(symbol, event):
    symbol.setValue("RS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
def calculateBootProtSize(symbol, event):
    symbol.setValue("BOOTPROT_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))
def calculateBNSCSize(symbol, event):
    symbol.setValue("BNSC_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BNSC"]) * int(memoryGranularity["IDAU_BNSC"]))).replace("L", ""))
def calculateBSSize(symbol, event):
    symbol.setValue("BS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BS"]) * int(memoryGranularity["IDAU_BS"]))).replace("L", ""))

# for Secure Project
# set Linker Macros required for XC32
xc32LinkerMacroSecure = coreComponent.createSettingSymbol("XC32_LINKER_MACRO", None)
xc32LinkerMacroSecure.setCategory("C32-LD")
xc32LinkerMacroSecure.setKey("preprocessor-macros")
xc32LinkerMacroSecure.setValue("SECURE")
xc32LinkerMacroSecure.setAppend(True, ";")
xc32LinkerMacroSecure.setSecurity("SECURE")
xc32LinkerMacroSecure.setDependencies(updateSecureEnabledState, ["GENERATE_SECURE_BOOT_MAIN_FILE"])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_AS_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("AS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateASSize, [fuseMapSymbol["IDAU_AS"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_ANSC_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("ANSC_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_ANSC"]) * int(memoryGranularity["IDAU_ANSC"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateANSCSize, [fuseMapSymbol["IDAU_ANSC"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RS_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("RS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateRSSize, [fuseMapSymbol["IDAU_RS"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_BOOTPROT_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("BOOTPROT_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateBootProtSize, [fuseMapSymbol["IDAU_BOOTPROT"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_BNSC_SIZE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("BNSC_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BNSC"]) * int(memoryGranularity["IDAU_BNSC"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateBNSCSize, [fuseMapSymbol["IDAU_BNSC"]])
xc32LinkerMacro.setSecurity("SECURE")

# set Linker Macros required for BS (Boot Secure) Size
for key in memoryFuseMaxValue.keys():
    if key == "IDAU_BS":
        xc32LinkerMacroSecureBootSize = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_SECURE_BS", None)
        xc32LinkerMacroSecureBootSize.setCategory("C32-LD")
        xc32LinkerMacroSecureBootSize.setKey("preprocessor-macros")
        xc32LinkerMacroSecureBootSize.setValue("BS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BS"]) * int(memoryGranularity["IDAU_BS"]))).replace("L", ""))
        xc32LinkerMacroSecureBootSize.setAppend(True, ";=")
        xc32LinkerMacroSecureBootSize.setDependencies(calculateBSSize, [fuseMapSymbol["IDAU_BS"]])
        xc32LinkerMacroSecureBootSize.setSecurity("SECURE")
        break

# set Linker Macros required for SECURE_BOOTLOADER
xc32LinkerMacroSecureBootloader = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_SECURE_BOOTLOADER", None)
xc32LinkerMacroSecureBootloader.setCategory("C32-LD")
xc32LinkerMacroSecureBootloader.setKey("preprocessor-macros")
xc32LinkerMacroSecureBootloader.setValue("SECURE_BOOTLOADER")
xc32LinkerMacroSecureBootloader.setAppend(True, ";")
xc32LinkerMacroSecureBootloader.setEnabled(False)
xc32LinkerMacroSecureBootloader.setDependencies(updateSecureBootloaderEnabledState, ["GENERATE_SECURE_BOOT_MAIN_FILE"])
xc32LinkerMacroSecureBootloader.setSecurity("SECURE")

#For Non Secure
# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_AS_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("AS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_AS"]) * int(memoryGranularity["IDAU_AS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateASSize, [fuseMapSymbol["IDAU_AS"]])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_RS_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("RS_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_RS"]) * int(memoryGranularity["IDAU_RS"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
xc32LinkerMacro.setDependencies(calculateRSSize, [fuseMapSymbol["IDAU_RS"]])

# set Linker Macros required for XC32
xc32LinkerMacro = coreComponent.createSettingSymbol("XC32_LINKER_MACRO_BOOTPROT_SIZE_NON_SECURE", None)
xc32LinkerMacro.setCategory("C32-LD")
xc32LinkerMacro.setKey("preprocessor-macros")
xc32LinkerMacro.setValue("BOOTPROT_SIZE=" + str(hex(Database.getSymbolValue("core", fuseMapSymbol["IDAU_BOOTPROT"]) * int(memoryGranularity["IDAU_BOOTPROT"]))).replace("L", ""))
xc32LinkerMacro.setAppend(True, ";=")
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
defSym.setValue("../src;../src/config/" + configName + ";" + packsPath)
defSym.setAppend(True, ";")
defSym.setSecurity("SECURE")

defXc32cppSym = coreComponent.createSettingSymbol("SEC_XC32CPP_INCLUDE_DIRS", None)
defXc32cppSym.setCategory("C32CPP")
defXc32cppSym.setKey("extra-include-directories")
defXc32cppSym.setValue(defSym.getValue())
defXc32cppSym.setAppend(True, ";")
defXc32cppSym.setSecurity("SECURE")

xc32CMSECompilerFlag =  coreComponent.createSettingSymbol("SEC_XC32_CMSE_FLAG", None)
xc32CMSECompilerFlag.setCategory("C32")
xc32CMSECompilerFlag.setKey("appendMe")
xc32CMSECompilerFlag.setValue("-mcmse")
xc32CMSECompilerFlag.setAppend(True, " ")
xc32CMSECompilerFlag.setSecurity("SECURE")

xc32cppCMSECompilerFlag = coreComponent.createSettingSymbol("SEC_XC32CPP_CMSE_FLAG", None)
xc32cppCMSECompilerFlag.setCategory("C32CPP")
xc32cppCMSECompilerFlag.setKey("appendMe")
xc32cppCMSECompilerFlag.setValue(xc32CMSECompilerFlag.getValue())
xc32cppCMSECompilerFlag.setAppend(True, " ")
xc32cppCMSECompilerFlag.setSecurity("SECURE")

implib_name, implib_rel_path = get_implib_details()
xc32CMSELinkerFlag = coreComponent.createSettingSymbol("SEC_XC32_LINKER_CMSE_FLAG", None)
xc32CMSELinkerFlag.setCategory("C32-LD")
xc32CMSELinkerFlag.setKey("appendMe")
xc32CMSELinkerFlag.setValue( "--out-implib={0} ,--cmse-implib".format(implib_rel_path))
xc32CMSELinkerFlag.setAppend(True, " ")
xc32CMSELinkerFlag.setSecurity("SECURE")
xc32CMSELinkerFlag.setDependencies(updateSecureBootSettings, ["GENERATE_SECURE_BOOT_MAIN_FILE", "IDAU_ANSC_SIZE", "IDAU_BNSC_SIZE"])

xc32LinkerLibraryPath =  coreComponent.createSettingSymbol("XC32_LINKER_LIBRARY_", None)
xc32LinkerLibraryPath.setCategory("C32-LD")
xc32LinkerLibraryPath.setKey("appendMe")
xc32LinkerLibraryPath.setValue( "-l:{0}".format(implib_name))
xc32LinkerLibraryPath.setAppend(True, " ")
xc32LinkerLibraryPath.setDependencies(updateSecureBootSettings, ["GENERATE_SECURE_BOOT_MAIN_FILE", "IDAU_ANSC_SIZE", "IDAU_BNSC_SIZE"])

xc32LinkerLibraryDirectoryPath = coreComponent.createSettingSymbol("XC32_LINKER_LIBRARY_DIR_PATH", None)
xc32LinkerLibraryDirectoryPath.setCategory("C32-LD")
xc32LinkerLibraryDirectoryPath.setKey("extra-lib-directories")
xc32LinkerLibraryDirectoryPath.setValue("./")
xc32LinkerLibraryDirectoryPath.setAppend(True, ";")

# set XC32 option to not use the device startup code
xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("SEC_XC32_NO_DEVICE_STARTUP_CODE", None)
xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
xc32NoDeviceStartupCodeSym.setValue("true")
xc32NoDeviceStartupCodeSym.setSecurity("SECURE")
xc32NoDeviceStartupCodeSym.setAppend(True, ";")

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

coreComponent.addPlugin("../../harmony-services/plugins/generic_plugin.jar", "TRUSTZONE_MANAGER_ARM", {"plugin_name": "Arm TrustZone for Armv8-M", "main_html_path": "csp/plugins/configurators/trustzone_configurators/trustzone_configurator/build/index.html"})
