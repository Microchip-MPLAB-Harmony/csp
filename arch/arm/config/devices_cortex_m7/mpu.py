coreUseMPU = coreComponent.createBooleanSymbol("CoreUseMPU", devCfgMenu)
coreUseMPU.setLabel("Enable MPU?")

def showMenu(coreMPUMenu, enable):
	coreMPUMenu.setVisible(enable["value"])
	
coreMPUMenu = coreComponent.createMenuSymbol(None, coreUseMPU)
coreMPUMenu.setLabel("MPU Configuration")
coreMPUMenu.setDescription("MPU Configuration")
coreMPUMenu.setVisible(False)
coreMPUMenu.setDependencies(showMenu, ["CoreUseMPU"])

coreMPUHFNMIENA  = coreComponent.createBooleanSymbol("CoreMPU_HFNMIENA", coreMPUMenu)
coreMPUHFNMIENA.setLabel("HFNMIENA")
coreMPUHFNMIENA.setDescription("Enables the operation of MPU during hard fault, NMI, and FAULTMASK handlers")
coreMPUHFNMIENA.setDefaultValue(False)

coreUseMPUPRIVDEFENA = coreComponent.createBooleanSymbol("CoreMPU_PRIVDEFENA", coreMPUMenu)
coreUseMPUPRIVDEFENA.setLabel("PRIVDEFENA")
coreUseMPUPRIVDEFENA.setDefaultValue(False)
coreUseMPUPRIVDEFENA.setDescription("Enables privileged software access to the default memory map")

coreMPUNumRegions = coreComponent.createIntegerSymbol("NUM_REGIONS", coreMPUMenu)
coreMPUNumRegions.setLabel("Number of Regions")
coreMPUNumRegions.setDescription("No. of MPU Configuration")
coreMPUNumRegions.setDefaultValue(10)
coreMPUNumRegions.setMin(10)
coreMPUNumRegions.setMax(16)

coreMPURegion = []
coreMPURegMenu = []
coreMPURegName = []
coreMPURegAddress = []
coreMPURegSize = []
coreMPURegAccess = []
coreMPURegAttribute = []
coreMPURegEnable = []
coreMPURegXN = []
coreMPURegShare = []
coreMPUComment = []


	
regionNamesDefault = (	'ITCM','FLASH','DTCM','System RAM','System RAM'',
						'PERIPHERAL','EBI','SDRAM', 'QSPI', 'USB RAM', 'ARM PRIVATE BUS', 
						'System RAM', 'System RAM', 'System RAM', 'System RAM', 'System RAM')
						
regAddressDefault = (0x0, 0x400000, 0x20000000, 0x20400000, 0x2045F000, 
			  0x40000000, 0x60000000, 0x70000000, 0x80000000,
			  0xA0100000, 0xE0000000, 0x0, 0x0, 0x0, 0x0, 0x0)

regSizeDefault = 	(21, 21, 21, 22, 11, 27,
					27, 27, 27, 19, 19,
					4, 4, 4, 4, 4)
	
regSizeBytesDefault = 	(4194304, 4194304, 4194304, 8388608, 4096, 268435456,
							268435456, 268435456, 268435456, 1048576, 1048576,
							32, 32, 32, 32, 32)
			  
regAccessDefault = (3, 3, 5, 5, 5, 5,
					5, 5, 5, 5, 5,
					5, 5, 5, 5, 5)

regAttributeDefault = (3, 3, 4, 4, 5, 1,
			  0, 3, 0, 1, 0,
			  4, 4, 4, 4, 4)

global regionNames 
regionNames = {	'System RAM' : 0x20400000,
				'FLASH' : 0x00400000,
				'QSPI' : 0x80000000,
				'SDRAM' : 0x70000000,
				'ARM PRIVATE BUS' :0xE0000000,
				'DTCM' : 0x20000000,
				'ITCM' : 0x00000000,
				'PERIPHERAL' : 0x40000000,
				'EBI' : 0x60000000,
				'USB RAM' : 0xA0100000, 
				}
			  
def numRegions(region, count):
	regNumber = region.getComponent()
	for i in range(0,16):
		regNumber.getSymbolByID("MPU_Region_" + str(i)).setVisible(i < count["value"])

def showRegMenu(region, enable):
	region.setVisible(enable["value"])
	
def mpuSizeCal(region, size):
	data = 2**(size["value"] + 1)
	region.setLabel("****Size is " + str(data) + " bytes*******")

def setAddress(region, name):
	region.clearValue()
	region.setValue(regionNames.get(name["value"]), 2)
	
for i in range(0,14):
	coreMPURegion.append(i)
	coreMPURegion[i] = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i)), coreMPUMenu)
	coreMPURegion[i].setLabel("Region" + str(i))
	coreMPURegion[i].setVisible(i < 10)
	coreMPURegion[i].setDefaultValue(i < 10)
	coreMPURegion[i].setDependencies(numRegions, ["NUM_REGIONS"])
	
	coreMPURegMenu.append(i)
	coreMPURegMenu[i] = coreComponent.createMenuSymbol(None, coreMPURegion[i])
	coreMPURegMenu[i].setLabel("Region Configuration")
	coreMPURegMenu[i].setDescription("Region Configuration")
	coreMPURegMenu[i].setVisible(i < 10)
	coreMPURegMenu[i].setDependencies(showRegMenu, ["MPU_Region_" + str(i)])
	
	coreMPURegName.append(i)
	coreMPURegName[i] = coreComponent.createComboSymbol(("MPU_Region_Name" + str(i)), coreMPURegMenu[i], regionNames.keys())
	coreMPURegName[i].setLabel("Memory type")
	coreMPURegName[i].setVisible(i < 10)
	coreMPURegName[i].setDefaultValue(regionNamesDefault[i])
	
	coreMPURegAddress.append(i)
	coreMPURegAddress[i] = coreComponent.createHexSymbol(("MPU_Region_" + str(i) + "_Address"), coreMPURegMenu[i])
	coreMPURegAddress[i].setLabel("Address")
	coreMPURegAddress[i].setDefaultValue(regAddressDefault[i])
	coreMPURegAddress[i].setDependencies(setAddress, ["MPU_Region_Name" + str(i)])	
	
	coreMPURegSize.append(i)
	coreMPURegSize[i] = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Size"), coreMPURegMenu[i])
	coreMPURegSize[i].setLabel("Size")
	coreMPURegSize[i].setOutputMode("Value")
	coreMPURegSize[i].setDisplayMode("Key")
	coreMPURegSize[i].addKey("32 Bytes", str(4) , "Region size is 32 bytes" )
	coreMPURegSize[i].addKey("64 Bytes", str(5) , "Region size is 64 bytes" )
	coreMPURegSize[i].addKey("128 Bytes", str(6) , "Region size is 128 bytes" )
	coreMPURegSize[i].addKey("256 Bytes", str(7) , "Region size is 256 bytes" )
	coreMPURegSize[i].addKey("512 Bytes", str(8) , "Region size is 512 bytes" )
	coreMPURegSize[i].addKey("1 KB", str(9) , "Region size is 1 KB" )
	coreMPURegSize[i].addKey("2 KB", str(10) , "Region size is 2 KB" )
	coreMPURegSize[i].addKey("4 KB", str(11) , "Region size is 4 KB" )
	coreMPURegSize[i].addKey("8 KB", str(12) , "Region size is 8 KB" )
	coreMPURegSize[i].addKey("16 KB", str(13) , "Region size is 16 KB" )
	coreMPURegSize[i].addKey("32 KB", str(14) , "Region size is 32 KB" )
	coreMPURegSize[i].addKey("64 KB", str(15) , "Region size is 64 KB" )
	coreMPURegSize[i].addKey("128 KB", str(16) , "Region size is 128 KB" )
	coreMPURegSize[i].addKey("256 KB", str(17) , "Region size is 256 KB" )
	coreMPURegSize[i].addKey("512 KB ", str(18) , "Region size is 512 KB" )
	coreMPURegSize[i].addKey("1 MB ", str(19) , "Region size is 1 MB" )
	coreMPURegSize[i].addKey("2 MB ", str(20) , "Region size is 2 MB" )
	coreMPURegSize[i].addKey("4 MB ", str(21) , "Region size is 4 MB" )
	coreMPURegSize[i].addKey("8 MB", str(22) , "Region size is 8 MB" )
	coreMPURegSize[i].addKey("16 MB", str(23) , "Region size is 16 MB" )
	coreMPURegSize[i].addKey("32 MB", str(24) , "Region size is 32 MB" )
	coreMPURegSize[i].addKey("64 MB", str(25) , "Region size is 64 MB" )
	coreMPURegSize[i].addKey("128 MB", str(26) , "Region size is 128 MB" )
	coreMPURegSize[i].addKey("256 MB", str(27) , "Region size is 256 MB" )
	coreMPURegSize[i].addKey("512 MB ", str(28) , "Region size is 512 MB" )
	coreMPURegSize[i].addKey("1 GB ", str(29) , "Region size is 1 GB" )
	coreMPURegSize[i].addKey("2 GB ", str(30) , "Region size is 2 GB" )
	coreMPURegSize[i].addKey("4 GB ", str(31) , "Region size is 4 GB" )
	coreMPURegSize[i].setDefaultValue((regSizeDefault[i] - 4))

	
	coreMPURegAccess.append(i)
	coreMPURegAccess[i] = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Access"), coreMPURegMenu[i])
	coreMPURegAccess[i].setLabel("Access Privilege")
	coreMPURegAccess[i].setOutputMode("Key")
	coreMPURegAccess[i].setDisplayMode("Description")
	coreMPURegAccess[i].addKey("MPU_RASR_AP_NOACCESS_Val", str(0) , "No access for all" )
	coreMPURegAccess[i].addKey("MPU_RASR_AP_NOACCESS_PRIV_READONLY_Val", str(1) , "No access for unprivileged, readonly for privileged" )
	coreMPURegAccess[i].addKey("MPU_RASR_AP_NOACCESS_PRIV_READWRITE_Val", str(2) , "No access for unprivileged, read/write for privileged" )
	coreMPURegAccess[i].addKey("MPU_RASR_AP_READONLY_Val", str(3) , "Readonly for all" )
	coreMPURegAccess[i].addKey("MPU_RASR_AP_READONLY_PRIV_READWRITE_Val", str(4) , "Readonly for unprivileged, read/write for privileged" )
	coreMPURegAccess[i].addKey("MPU_RASR_AP_READWRITE_Val", str(5) , "Read/Write for all" )
	coreMPURegAccess[i].setDefaultValue(regAccessDefault[i])
	
	coreMPURegAttribute.append(i)
	coreMPURegAttribute[i] = coreComponent.createKeyValueSetSymbol(("MPU_Region_" + str(i) + "_Attribute"), coreMPURegMenu[i])
	coreMPURegAttribute[i].setLabel("Attribute")
	coreMPURegAttribute[i].setOutputMode("Key")
	coreMPURegAttribute[i].setDisplayMode("Description")
	coreMPURegAttribute[i].addKey("MPU_ATTR_STRONGLY_ORDERED", str(0) , "Strongly-Ordered Shareable" )
	coreMPURegAttribute[i].addKey("MPU_ATTR_DEVICE", str(1) , "Device Shareable" )
	coreMPURegAttribute[i].addKey("MPU_ATTR_NORMAL_WT", str(2) , "Normal, Write-Through Read Allocate" )
	coreMPURegAttribute[i].addKey("MPU_ATTR_NORMAL_WB", str(3) , "Normal, Write-Back Read Allocate" )
	coreMPURegAttribute[i].addKey("MPU_ATTR_NORMAL_WB_WA", str(4) , "Normal, Write-Back Read/Write Allocate " )
	coreMPURegAttribute[i].addKey("MPU_ATTR_NORMAL", str(5) , "Normal, Non-cacheable" )
	coreMPURegAttribute[i].setLabel("Attribute")
	coreMPURegAttribute[i].setDefaultValue(regAttributeDefault[i])
	
	coreMPURegEnable.append(i)
	coreMPURegEnable[i] = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_Enable"), coreMPURegMenu[i])
	coreMPURegEnable[i].setLabel("Enable")
	coreMPURegEnable[i].setDefaultValue(i < 10)
	
	coreMPURegXN.append(i)
	coreMPURegXN[i] = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_XN"), coreMPURegMenu[i])
	coreMPURegXN[i].setLabel("Execute Never (XN)")
	coreMPURegXN[i].setDefaultValue(False)
	
	coreMPURegion.append(i)
	coreMPURegion[i] = coreComponent.createBooleanSymbol(("MPU_Region_" + str(i) + "_S" ), coreMPURegMenu[i])
	coreMPURegion[i].setLabel("Shareable")
	coreMPURegion[i].setDefaultValue(False)
	