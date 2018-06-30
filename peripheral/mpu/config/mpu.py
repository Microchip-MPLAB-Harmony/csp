
################################################################################
#### Global Variables ####
################################################################################
global  mpuHeaderFile1
global  mpuHeaderFile2
global  mpuSourceFile
global  mpuSystemInitFile
global  mpuSystemDefFile
global  mpuNVICVector
global  mpuNVICHandlerLock

################################################################################
#### Business Logic ####
################################################################################
global mpuSettings
# Memory Type, Data Access Permission, Instruction Access Permission, Shared Memory, Start Address, Size
mpuSettings = {"ITCM"           : ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00000000",   "4MB"   ],
                "FLASH"         : ["MPU_ATTR_NORMAL_WT",        "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x00400000",   "4MB"   ],
                "DTCM"          : ["MPU_ATTR_NORMAL",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20000000",   "4MB"   ],
                "SRAM"          : ["MPU_ATTR_NORMAL_WB_WA",     "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x20400000",   "8MB"   ],
                "PERIPHERALS"   : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0x40000000",   "256MB" ],
                "EBI_SMC"       : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x60000000",   "256MB" ],
                "EBI_SDRAM"     : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x70000000",   "256MB" ],
                "QSPI"          : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "True",     "",     "0x80000000",   "256MB" ],
                "USBHS_RAM"     : ["MPU_ATTR_DEVICE",           "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xA0100000",   "1MB"   ],
                "SYSTEM"        : ["MPU_ATTR_STRONGLY_ORDERED", "MPU_RASR_AP_READWRITE_Val",    "",         "",     "0xE0000000",   "1MB"   ]}

mpuSetUpLogicList = ['ITCM', 'FLASH', 'DTCM', 'SRAM', 'PERIPHERALS', 'EBI_SMC', 'EBI_SDRAM', 'QSPI', 'USBHS_RAM', 'SYSTEM']

def mpuSetUpLogic(mpuSym, event):
    global mpuSettings

    if event["value"] in mpuSettings:
        SymID = mpuSym.getID()

        mpuSym.clearValue()
        if "_Type" in str(SymID):
            mpuSym.setSelectedKey(str(mpuSettings[event["value"]][0]), 2)
        if "_Access" in str(SymID):
            mpuSym.setSelectedKey(str(mpuSettings[event["value"]][1]), 2)
        if "_Execute" in str(SymID):
            mpuSym.setValue(bool(mpuSettings[event["value"]][2]),2)
        if "_Share" in str(SymID):
            mpuSym.setValue(bool(mpuSettings[event["value"]][3]),2)
        if "_Address" in str(SymID):
            hex_str = str(mpuSettings[event["value"]][4])
            hex_int = int(hex_str, 0)
            mpuSym.setValue(hex_int,2)
        if "_Size" in str(SymID):
            mpuSym.setSelectedKey(str(mpuSettings[event["value"]][5]), 2)


def enableFileGen(coreMPUMenu, event):
    if(event["value"]==True):
        mpuHeaderFile1.setEnabled(True)
        mpuHeaderFile2.setEnabled(True)
        mpuSourceFile.setEnabled(True)
        mpuSystemDefFile.setEnabled(True)
    else:
        mpuHeaderFile1.setEnabled(False)
        mpuHeaderFile2.setEnabled(False)
        mpuSourceFile.setEnabled(False)
        mpuSystemDefFile.setEnabled(False)

def storeLength(symbol, event):
    symObj=event["symbol"]
    key=symObj.getSelectedKey()
    symbol.setValue(key,2)

def mpuNVICControl(symbol, event):
    Database.clearSymbolValue("core", mpuNVICVector)
    Database.clearSymbolValue("core", mpuNVICHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", mpuNVICVector, True, 2)
        Database.setSymbolValue("core", mpuNVICHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", mpuNVICVector, False, 2)
        Database.setSymbolValue("core", mpuNVICHandlerLock, False, 2)

################################################################################
#### Component ####
################################################################################
mpuMenu = coreComponent.createMenuSymbol("MPU_MENU", cortexMenu)
mpuMenu.setLabel("MPU")

coreUseMPU = coreComponent.createBooleanSymbol("CoreUseMPU", mpuMenu)
coreUseMPU.setLabel("Enable MPU?")


mpuFileGen = coreComponent.createBooleanSymbol("MPU_BOOL_0", coreUseMPU)
mpuFileGen.setLabel("MPU File Generation")
mpuFileGen.setDependencies(enableFileGen, ["CoreUseMPU"])
mpuFileGen.setVisible(False)


coreMPUHFNMIENA  = coreComponent.createBooleanSymbol("CoreMPU_HFNMIENA", coreUseMPU)
coreMPUHFNMIENA.setLabel("HFNMIENA")
coreMPUHFNMIENA.setDescription("Enables MPU during HardFault, NMI, or  when FAULTMASK is set")
coreMPUHFNMIENA.setDefaultValue(False)

coreUseMPUPRIVDEFENA = coreComponent.createBooleanSymbol("CoreMPU_PRIVDEFENA", coreUseMPU)
coreUseMPUPRIVDEFENA.setLabel("PRIVDEFENA")
coreUseMPUPRIVDEFENA.setDefaultValue(False)
coreUseMPUPRIVDEFENA.setDescription("Enables privileged software access to the default memory map")

for i in range(0,16):

    coreMPURegEnable = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_Enable"), coreUseMPU)
    coreMPURegEnable.setLabel("Enable MPU Region" + str(i))

    if i<len(mpuSettings):
        coreMPURegEnable.setDefaultValue(True)
    else:
        coreMPURegEnable.setDefaultValue(False)


    coreMPURegMenu = coreComponent.createMenuSymbol("MPU_MENU_" + str(i), coreMPURegEnable)
    coreMPURegMenu.setLabel("MPU Region " + str(i) + " Settings")
    coreMPURegMenu.setDescription("Configuration for MPU Region"+ str(i))

    coreMPURegNameOptions = coreComponent.createComboSymbol(("MPU_Region_Name" + str(i) +"_Options"), coreMPURegMenu, mpuSettings.keys())
    coreMPURegNameOptions.setLabel("Region Name Options")
    coreMPURegNameOptions.setVisible(False)

    coreMPURegName = coreComponent.createStringSymbol(("MPU_Region_Name" + str(i)), coreMPURegMenu)
    coreMPURegName.setLabel("Region Name")
    # Default value is set later to trigger business logic for the first time

    coreMPURegAddress = coreComponent.createHexSymbol(("MPU_Region_" + str(i) + "_Address"), coreMPURegMenu)
    coreMPURegAddress.setLabel("Base Address")
    coreMPURegAddress.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])

    coreMPURegSize = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Size"), coreMPURegMenu)
    coreMPURegSize.setLabel("Size")
    coreMPURegSize.setOutputMode("Value")
    coreMPURegSize.setDisplayMode("Description")
    coreMPURegSize.addKey("32B", str(4) , "32 Bytes" )
    coreMPURegSize.addKey("64B", str(5) , "64 bytes" )
    coreMPURegSize.addKey("128B", str(6) , "128 bytes" )
    coreMPURegSize.addKey("256B", str(7) , "256 bytes" )
    coreMPURegSize.addKey("512B", str(8) , "512 bytes" )
    coreMPURegSize.addKey("1KB", str(9) , "1 KB" )
    coreMPURegSize.addKey("2KB", str(10) , "2 KB" )
    coreMPURegSize.addKey("4KB", str(11) , "4 KB" )
    coreMPURegSize.addKey("8KB", str(12) , "8 KB" )
    coreMPURegSize.addKey("16KB", str(13) , "16 KB" )
    coreMPURegSize.addKey("32KB", str(14) , "32 KB" )
    coreMPURegSize.addKey("64KB", str(15) , "64 KB" )
    coreMPURegSize.addKey("128KB", str(16) , "128 KB" )
    coreMPURegSize.addKey("256KB", str(17) , "256 KB" )
    coreMPURegSize.addKey("512KB", str(18) , "512 KB" )
    coreMPURegSize.addKey("1MB", str(19) , "1 MB" )
    coreMPURegSize.addKey("2MB", str(20) , "2 MB" )
    coreMPURegSize.addKey("4MB", str(21) , "4 MB" )
    coreMPURegSize.addKey("8MB", str(22) , "8 MB" )
    coreMPURegSize.addKey("16MB", str(23) , "16 MB" )
    coreMPURegSize.addKey("32MB", str(24) , "32 MB" )
    coreMPURegSize.addKey("64MB", str(25) , "64 MB" )
    coreMPURegSize.addKey("128MB", str(26) , "128 MB" )
    coreMPURegSize.addKey("256MB", str(27) , "256 MB" )
    coreMPURegSize.addKey("512MB", str(28) , "512 MB" )
    coreMPURegSize.addKey("1GB", str(29) , "1 GB" )
    coreMPURegSize.addKey("2GB", str(30) , "2 GB" )
    coreMPURegSize.addKey("4GB", str(31) , "4 GB" )
    coreMPURegSize.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])

    coreMPURegLength = coreComponent.createStringSymbol(("MPU_Region_" + str(i)) + "_Length", coreMPURegMenu)
    coreMPURegLength.setLabel("Region Length")
    coreMPURegLength.setVisible(False)
    coreMPURegLength.setDependencies(storeLength, ["MPU_Region_" + str(i) + "_Size"])


    coreMPURegType = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Type"), coreMPURegMenu)
    coreMPURegType.setLabel("Memory Type and Cache policy")
    coreMPURegType.setOutputMode("Key")
    coreMPURegType.setDisplayMode("Description")
    coreMPURegType.addKey("MPU_ATTR_STRONGLY_ORDERED", str(0) , "Strongly-Ordered Memory" )
    coreMPURegType.addKey("MPU_ATTR_DEVICE", str(1) , "Device Memory" )
    coreMPURegType.addKey("MPU_ATTR_NORMAL_WT", str(2) , "Normal memory, Write-through cache" )
    coreMPURegType.addKey("MPU_ATTR_NORMAL_WB", str(3) , "Normal memory, Write-back cache" )
    coreMPURegType.addKey("MPU_ATTR_NORMAL_WB_WA", str(4) , "Normal memory, Write-back and write-allocate cache" )
    coreMPURegType.addKey("MPU_ATTR_NORMAL", str(5) , "Normal memory, Non-cacheable" )
    coreMPURegType.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])


    coreMPURegAccess = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Access"), coreMPURegMenu)
    coreMPURegAccess.setLabel("Data Access Permission")
    coreMPURegAccess.setOutputMode("Key")
    coreMPURegAccess.setDisplayMode("Description")
    coreMPURegAccess.addKey("MPU_RASR_AP_NOACCESS_Val", str(0) , "User: No Access, Privileged: No Access" )
    coreMPURegAccess.addKey("MPU_RASR_AP_NOACCESS_PRIV_READWRITE_Val", str(1) , "User: No Access, Privileged: Read/Write" )
    coreMPURegAccess.addKey("MPU_RASR_AP_READONLY_PRIV_READWRITE_Val", str(2) , "User: Read only, Privileged: Read/Write" )
    coreMPURegAccess.addKey("MPU_RASR_AP_READWRITE_Val", str(3) , "User: Read/Write, Privileged: Read/Write" )
    coreMPURegAccess.addKey("MPU_RASR_AP_NOACCESS_PRIV_READONLY_Val", str(5) , "User: No Access, Privileged: Read only" )
    coreMPURegAccess.addKey("MPU_RASR_AP_READONLY_Val", str(7) , "User: Read only, Privileged: Read only" )
    coreMPURegAccess.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])

    coreMPURegExecute = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_Execute"), coreMPURegMenu)
    coreMPURegExecute.setLabel("Instruction Access Permission")
    coreMPURegExecute.setDefaultValue(False)
    coreMPURegExecute.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])

    coreMPURegShare= coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_Share" ), coreMPURegMenu)
    coreMPURegShare.setLabel("Shareable Attribute")
    coreMPURegShare.setDefaultValue(False)
    coreMPURegShare.setDependencies(mpuSetUpLogic, ["MPU_Region_Name" + str(i)])

    if i<len(mpuSettings):
        coreMPURegName.setDefaultValue(mpuSetUpLogicList[i])

# Setup Peripheral Interrupt in Interrupt manager
mpuPeripId = Interrupt.getInterruptIndex("MemoryManagement")
mpuNVICVector = "NVIC_" + str(mpuPeripId) + "_ENABLE"
mpuNVICHandlerLock = "NVIC_" + str(mpuPeripId) + "_HANDLER_LOCK"

# NVIC Dynamic settings
MPU_NVICControl = coreComponent.createBooleanSymbol("NVIC_MPU_ENABLE", coreUseMPU)
MPU_NVICControl.setDependencies(mpuNVICControl, ["CoreUseMPU"])
MPU_NVICControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
configName = Variables.get("__CONFIGURATION_NAME")

mpuHeaderFile1 = coreComponent.createFileSymbol("PLIB_MPU_H", None)
mpuHeaderFile1.setMarkup(True)
mpuHeaderFile1.setSourcePath("../peripheral/mpu/templates/plib_mpu.h.ftl")
mpuHeaderFile1.setOutputName("plib_mpu.h")
mpuHeaderFile1.setDestPath("/peripheral/mpu/")
mpuHeaderFile1.setProjectPath("config/" + configName + "/peripheral/mpu/")
mpuHeaderFile1.setType("HEADER")
mpuHeaderFile1.setOverwrite(True)
mpuHeaderFile1.setEnabled(False)

mpuHeaderFile2 = coreComponent.createFileSymbol("PLIB_MPU_LOCAL_H", None)
mpuHeaderFile2.setMarkup(True)
mpuHeaderFile2.setSourcePath("../peripheral/mpu/templates/plib_mpu_local.h.ftl")
mpuHeaderFile2.setOutputName("plib_mpu_local.h")
mpuHeaderFile2.setDestPath("/peripheral/mpu/")
mpuHeaderFile2.setProjectPath("config/" + configName + "/peripheral/mpu/")
mpuHeaderFile2.setType("HEADER")
mpuHeaderFile2.setOverwrite(True)
mpuHeaderFile2.setEnabled(False)

mpuSourceFile = coreComponent.createFileSymbol("PLIB_MPU_C", None)
mpuSourceFile.setMarkup(True)
mpuSourceFile.setSourcePath("../peripheral/mpu/templates/plib_mpu.c.ftl")
mpuSourceFile.setOutputName("plib_mpu.c")
mpuSourceFile.setDestPath("/peripheral/mpu/")
mpuSourceFile.setProjectPath("config/" + configName + "/peripheral/mpu/")
mpuSourceFile.setType("SOURCE")
mpuSourceFile.setOverwrite(True)
mpuSourceFile.setEnabled(False)

mpuSystemDefFile = coreComponent.createFileSymbol("MPU_SYSTEM_DEFINITIONS_H", None)
mpuSystemDefFile.setType("STRING")
mpuSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
mpuSystemDefFile.setSourcePath("../peripheral/mpu/templates/system/system_definitions.h.ftl")
mpuSystemDefFile.setMarkup(True)
mpuSystemDefFile.setEnabled(False)

