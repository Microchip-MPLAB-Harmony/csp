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
global ECIA_EN_SET_RegUpdate
global dmaConfiguration
global BootFlashDict
global isBFMPresent
global CORE_DSPIC33A
global CORE_PIC32A
global getAppPlacementParams

CORE_DSPIC33A  = "dsPIC33A"
CORE_PIC32A    = "PIC32A"

FlashNames          = ["FLASH", "IFLASH", "FCR_PFM"]
coreSymListOfSupportedMethods = [ "setValue", "setReadOnly", "setEnabled", "setVisible", "clearValue"]

FlashNames          = ["FLASH", "IFLASH", "IFLASH0", "FCR_PFM", "FLASH_PFM"]
#BootFlashDict      = {"bfm_region_name":[list of corresponding pfm regions], ..}
BootFlashDict       = {"FCR_BFM": ["FCR_PFM"], "BOOT_FLASH": ["FLASH"], "FLASH_BFM": ["FLASH_PFM"]}
vtableRegionList    = []

flash_start         = 0
flash_size          = 0

addr_space          = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space")
addr_space_children = addr_space.getChildren()

for mem_idx in range(0, len(addr_space_children)):
    mem_seg     = addr_space_children[mem_idx].getAttribute("name")
    mem_type    = addr_space_children[mem_idx].getAttribute("type")

    if (((any(x == mem_seg for x in FlashNames) == True) and (mem_type == "flash")) or (mem_seg == "code")):
        flash_start = int(addr_space_children[mem_idx].getAttribute("start"), 16)
        flash_size  = int(addr_space_children[mem_idx].getAttribute("size"), 16)

def getFlashParams(app_start):

    arch = Database.getSymbolValue("core", "CoreArchitecture")

    if ("CORTEX-A" in arch) or ("ARM926" in arch):
        return ("")

    app_offset  = (int(app_start,16) - flash_start)
    app_len     = str(hex(flash_size - app_offset))

    rom_origin  = "ROM_ORIGIN=" + hex(int(app_start,16))
    rom_length  = "ROM_LENGTH=" + app_len

    return (rom_origin + ";" + rom_length)

def getVtablePlacementParams(sel_vtable_reg):
    global BootFlashDict

    if sel_vtable_reg in BootFlashDict.keys():
        # the selected region is boot flash
        vector_region = "VECTOR_REGION=boot_rom"
    else:
        # the selected region is program flash
        vector_region = "VECTOR_REGION=rom"

    return vector_region

def getAppPlacementParams(appStartAddr, vtableMemRegion = None):

    flashParams = getFlashParams(appStartAddr)
    if vtableMemRegion != None:
        vtableParams = getVtablePlacementParams(vtableMemRegion)
        flashParams += ";" + vtableParams

    return flashParams

def updateAppPlacementParams(symbol, event):
    global isBFMPresent
    global getAppPlacementParams

    appStartAddr = symbol.getComponent().getSymbolValue("APP_START_ADDRESS")
    vtableMemRegion = None
    if isBFMPresent == True:
        vtableMemRegion = symbol.getComponent().getSymbolValue("VTABLE_MEM_REGION")

    symbol.setValue(getAppPlacementParams(appStartAddr, vtableMemRegion))

# Callback for all the messages sent to core component
def handleMessage(messageID, args):
    global nvmWaitStates
    global compilers
    symbolDict = {}

    if (messageID == "SYS_TIME_PUBLISH_CAPABILITIES"):

        Database.setSymbolValue("core", "SYSTICK_SYS_TIME_COMPONENT_ID", args["ID"])
        if args["ID"] != "None":
            Database.setSymbolValue("core", "SYSTICK_PUBLISH_CAPABILITIES", True)
            Database.setSymbolValue("core", "SYSTICK_BUSY", True)
        else:
            Database.setSymbolValue("core", "SYSTICK_PUBLISH_CAPABILITIES", False)
            Database.setSymbolValue("core", "SYSTICK_BUSY", False)

    elif (messageID == "SYS_TIME_TICK_RATE_CHANGED"):
        if Database.getSymbolValue("core", "SYSTICK_SYS_TIME_COMPONENT_ID") != "":
            #Set the Time Period (Milli Sec)
            #Using an intermediate long symbol to pass tick period, as setSymbolValue does not allow passing float values
            sys_time_tick_ms = (long)(args["sys_time_tick_ms"]*1000)
            Database.setSymbolValue("core","SYSTICK_PERIOD_MS_LONG_INT", sys_time_tick_ms)

    elif (messageID == "DVRT_PUBLISH_CAPABILITIES"):
        Database.setSymbolValue("core", "SYSTICK_SYS_TIME_COMPONENT_ID", args["ID"])
        if args["ID"] != "None":
            Database.setSymbolValue("core", "SYSTICK_PUBLISH_CAPABILITIES", True)
            Database.setSymbolValue("core", "SYSTICK_BUSY", True)
        else:
            Database.setSymbolValue("core", "SYSTICK_PUBLISH_CAPABILITIES", False)
            Database.setSymbolValue("core", "SYSTICK_BUSY", False)

    elif (messageID == "DVRT_TICK_RATE_CHANGED"):
        if Database.getSymbolValue("core", "SYSTICK_SYS_TIME_COMPONENT_ID") != "":
            #Set the Time Period (Milli Sec)
            #Using an intermediate long symbol to pass tick period, as setSymbolValue does not allow passing float values
            dvrt_tick_ms = (long)(args["dvrt_tick_ms"]*1000)
            Database.setSymbolValue("core","SYSTICK_PERIOD_MS_LONG_INT", dvrt_tick_ms)

    elif messageID == "PIN_LIST":              # Indicates core to return available pins for device
        symbolDict = getAvailablePins()      # this API must be defined as global in every port plibs

    elif messageID == "PIN_FUNCTION_LIST":   # Indicates core to return the function list for the pinName
        pinName = args.get('pinName')
        fnList = getFunctionListByPinName(pinName) # this API must be defined as global in every port plibs (MIPS arch)
        symbolDict.setdefault('pinName', fnList)

    elif messageID == "PIN_SET_CONFIG_VALUE":
        pinNumber = args.get('pinNumber')
        setting = args.get('setting')
        value = args.get('value')
        if pinNumber != None and setting != None and value != None:
            setPinConfigurationValue(pinNumber, setting, value)

    elif messageID == "PIN_GET_CONFIG_VALUE":
        pinNumber = args.get('pinNumber')
        setting = args.get('setting')
        if pinNumber != None and setting != None:
            value = getPinConfigurationValue(pinNumber, setting)
            symbolDict = {"value": value}

    elif messageID == "PIN_CLEAR_CONFIG_VALUE":
        pinNumber = args.get('pinNumber')
        setting = args.get('setting')
        if pinNumber != None and setting != None:
            clearPinConfigurationValue(pinNumber, setting)

    elif messageID == "SUPC_CONFIG_HW_IO":
        input, enable = args['config']
        symbolId = "SUPC_WUIR_WKUPEN{}".format(input)
        if enable == True:
            res = Database.setSymbolValue("core", symbolId, enable)
        else:
            res = Database.clearSymbolValue("core", symbolId)

        if res == True:
            symbolDict = {"Result": "Success"}
        else:
            symbolDict = {"Result": "Fail"}

    elif messageID == "AIC_CONFIG_HW_IO": # only for MPUs (aic.py)
        symbolDict = aicConfigHwIO(messageID, args)

    elif messageID == "INT_CONFIG_HW_IO": # only for MIPS
        extIntNum, enable = args['config']
        if enable == True:
            res = setExternalInterrupt(extIntNum)
        else:
            res = clearExternalInterrupt(extIntNum)

        if res == True:
            symbolDict = {"Result": "Success"}
        else:
            symbolDict = {"Result": "Fail"}

    elif messageID == "WAIT_STATES":
        symbolDict = nvmWaitStates

    elif (messageID == "DMA_CHANNEL_ENABLE"):
        Database.setSymbolValue("core", args["dma_channel"], True)

    elif (messageID == "DMA_CHANNEL_DISABLE"):
        Database.setSymbolValue("core", args["dma_channel"], False)

    elif (messageID == "HEAP_SIZE"):
        if ((compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "XC32") and
            (args["heap_size"] > Database.getSymbolValue("core", "XC32_HEAP_SIZE"))):
            Database.setSymbolValue("core", "XC32_HEAP_SIZE", args["heap_size"])
        elif ((compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "IAR") and
              (args["heap_size"] > Database.getSymbolValue("core", "IAR_HEAP_SIZE"))):
            Database.setSymbolValue("core", "IAR_HEAP_SIZE", args["heap_size"])
        elif ((compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "KEIL") and
              (args["heap_size"] > Database.getSymbolValue("core", "KEIL_HEAP_SIZE"))):
            Database.setSymbolValue("core", "KEIL_HEAP_SIZE", args["heap_size"])

    elif ("CLOCK_ENABLE" in messageID):
        Database.setSymbolValue("core", messageID, args["isEnabled"])

    elif (messageID == "SYSTICK_CONFIG"):
        if "isSystickEnRdOnly" in args:
            Database.getComponentByID("core").getSymbolByID("systickEnable").setReadOnly(args["isSystickEnRdOnly"])
        if "isSystickEn" in args:
            Database.setSymbolValue("core", "systickEnable", args["isSystickEn"])
        if "isSystickIntRdOnly" in args:
            Database.getComponentByID("core").getSymbolByID("USE_SYSTICK_INTERRUPT").setReadOnly(args["isSystickIntRdOnly"])
        if "isSystickIntEn" in args:
            Database.setSymbolValue("core", "USE_SYSTICK_INTERRUPT", args["isSystickIntEn"])

    elif (messageID == "GENERIC_TIMER_CONFIG"):
        if "isGenTmrEn" in args:
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_ENABLE").setReadOnly(True)
            Database.setSymbolValue("core", "GENERIC_TIMER_ENABLE", args["isGenTmrEn"])
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_ENABLE").setReadOnly(False)
        if "isGenTmrIntEn" in args:
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_INTERRUPT").setReadOnly(True)
            Database.setSymbolValue("core", "GENERIC_TIMER_INTERRUPT", args["isGenTmrIntEn"])
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_INTERRUPT").setReadOnly(False)
        if "isGenTmrAutoStart" in args:
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_AUTOSTART").setReadOnly(True)
            Database.setSymbolValue("core", "GENERIC_TIMER_AUTOSTART", args["isGenTmrAutoStart"])
            Database.getComponentByID("core").getSymbolByID("GENERIC_TIMER_AUTOSTART").setReadOnly(False)

    elif ((messageID == "SysTick_INTERRUPT_ENABLE") or (messageID == "SysTick_INTERRUPT_HANDLER_LOCK") or
          (messageID == "PendSV_INTERRUPT_ENABLE") or (messageID == "PendSV_INTERRUPT_HANDLER_LOCK") or
          (messageID == "SVCall_INTERRUPT_ENABLE") or (messageID == "SVCall_INTERRUPT_HANDLER_LOCK") or
          (messageID == "TIMER_1_INTERRUPT_ENABLE") or (messageID == "CORE_SOFTWARE_0_INTERRUPT_ENABLE")):
        Database.setSymbolValue("core", messageID, args["isEnabled"])
    elif ((messageID == "SysTick_INTERRUPT_HANDLER") or (messageID == "PendSV_INTERRUPT_HANDLER") or
          (messageID == "SVCall_INTERRUPT_HANDLER")):
        Database.setSymbolValue("core", messageID, args["intHandler"])

    elif (messageID == "CONTROL_REGISTER_LOCK"):
        Database.setSymbolValue("core", "IOLOCK_ENABLE", args["isEnabled"])
        Database.setSymbolValue("core", "PMDLOCK_ENABLE", args["isEnabled"])
    elif (messageID == "NVIC_INT_UPDATE"):
        ECIA_EN_SET_RegUpdate(args["int_source"], args["isEnabled"])

    elif (messageID == "NVIC_GET_MODULE_INSTANCE_LIST"):
        symbolDict = ECIA_GetNVICModuleList(args["int_source"])

    elif (messageID == "ECIA_GET_INT_SRC_DICT"):
        symbolDict = ECIA_GetInterruptNumber(args["int_source"])

    elif (messageID == "WDT_ENABLE"):
        if (Database.getSymbolValue("core", "WDT_USE") != None):
            Database.setSymbolValue("core", "WDT_USE", args["isEnabled"])
        elif (Database.getSymbolValue("core", "wdtENABLE") != None):
            Database.setSymbolValue("core", "wdtENABLE", args["isEnabled"])
    elif (messageID == "APP_START_ADDRESS"):
        Database.setSymbolValue("core", "APP_START_ADDRESS", args["start_address"])
    elif (messageID == "DMA_CONFIGURATION"):
        dmaConfiguration(args)
    elif (messageID == "FREERTOS_CONFIG"):
        for sym, attrib_dict in args.items():
            for attrib_method, attrib_val in attrib_dict.items():
                if attrib_method in coreSymListOfSupportedMethods:
                    if type (attrib_val) == str:
                        exp = 'Database.getComponentByID("core")' + '.getSymbolByID(sym)' + '.' + attrib_method + "(" + '"' + attrib_val + '"' + ")"
                    else:
                        if attrib_val == None:
                            exp = 'Database.getComponentByID("core")' + '.getSymbolByID(sym)' + '.' + attrib_method + "()"
                        else:
                            exp = 'Database.getComponentByID("core")' + '.getSymbolByID(sym)' + '.' + attrib_method + "(" + str(attrib_val) + ")"
                    eval(exp)

    return symbolDict

def genExceptionAsmSourceFile(symbol, event):
    global compilers
    global coreArch

    if ("MIPS" in coreArch.getValue() or compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "IAR"):
        coreSysFileEnabled = Database.getSymbolValue("core", "CoreSysFiles")
        coreSysExceptionFileEnabled = Database.getSymbolValue("core", "CoreSysExceptionFile")
        coreSysAdvancedExceptionFileEnabled = Database.getSymbolValue("core", "ADVANCED_EXCEPTION")

        if ((coreSysExceptionFileEnabled == True) and
            (coreSysAdvancedExceptionFileEnabled == True) and
            (coreSysFileEnabled == True)):
            symbol.setEnabled(True)
        else:
            symbol.setEnabled(False)

        if "MIPS" in coreArch.getValue():
            symbol.setSourcePath("templates/general-exception-context_mips.S.ftl")
            symbol.setOutputName("exceptionsHandler.S")
        elif (compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "IAR"):
            symbol.setSourcePath("templates/exceptionsHandler_iar.s.ftl")
            symbol.setOutputName("exceptionsHandler.s")
        else:
            symbol.setSourcePath("templates/exceptionsHandler.s.ftl")
            symbol.setOutputName("exceptionsHandler.S")

def setFileVisibility (symbol, event):
    symbol.setVisible(event["value"])

def setSysFileVisibility (symbol, event):
    symbol.setVisible(event["value"])
    symbol.setValue(event["value"], 1)

def alignmentWarning(symbol,event):
    symbol.setVisible((event["value"] % 8) != 0)

def setKeilHeapStackSize(symbol, event):
    size = event["source"].getSymbolValue("KEIL_STACK_SIZE")
    size += event["source"].getSymbolValue("KEIL_HEAP_SIZE")
    symbol.setValue("0x%X" % size)


def genMainSourceFile(symbol, event):
    mainName    = Database.getSymbolValue("core", "CoreMainFileName")
    genMainSrc  = Database.getSymbolValue("core", "CoreMainFile")

    if (genMainSrc == True):
        if Database.getSymbolValue("core", "CPLUSPLUS_PROJECT") == True:
            symbol.setOutputName(mainName.lower() + ".cpp")
        else:
            symbol.setOutputName(mainName.lower() + ".c")
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def updateDataCacheVisibility(symbol, event):
    symbol.setVisible(event["value"] != 3)

def genSysSourceFile(symbol, event):
    global processor
    coreSysFileEnabled = Database.getSymbolValue("core", "CoreSysFiles")
    coreSysSourceFileEnabled = False

    if(event["id"] == "CoreSysDefFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysDefFile")
    elif(event["id"] == "CoreSysInitFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysInitFile")
    elif(event["id"] == "CoreSysIntFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysIntFile")
    elif(event["id"] == "CoreSysExceptionFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysExceptionFile")
    elif event["id"] == "CoreSysTrapsFile":
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysTrapsFile")
    elif(event["id"] == "CoreSysStartupFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysStartupFile")
    elif(event["id"] == "CoreSysCallsFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysCallsFile")
    elif(event["id"] == "CoreSysStdioSyscallsFile"):
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysStdioSyscallsFile")
    elif(event["id"] == "FILTERING_EXCEPTION") or (event["id"] == "ADVANCED_EXCEPTION"):
        coreSysSourceFileEnabled = True
        if "MIPS" in Database.getSymbolValue("core","CoreArchitecture"):
            if (Database.getSymbolValue("core", "FILTERING_EXCEPTION")== True) and (Database.getSymbolValue("core", "ADVANCED_EXCEPTION")== True):
                symbol.setSourcePath("templates/filtering_exceptions_xc32_mips.c.ftl")
            elif Database.getSymbolValue("core", "ADVANCED_EXCEPTION")== True:
                symbol.setSourcePath("templates/advanced_exceptions_xc32_mips.c.ftl")
            else:
                # this means basic general exception code needs to be generated
                symbol.setSourcePath("templates/exceptions_xc32_mips.c.ftl")

    if ((coreSysFileEnabled == True) and (coreSysSourceFileEnabled == True)):
        symbol.setEnabled(True)
    else:
        symbol.setEnabled(False)

def genSysIntASMSourceFile(symbol, event):

    symbol.setEnabled(False)

    #Should be enable only for FreeRTOS
    if event["value"] == "FreeRTOS":
        coreSysFileEnabled = Database.getSymbolValue("core", "CoreSysFiles")
        coreSysSourceFileEnabled = Database.getSymbolValue("core", "CoreSysIntFile")

        if coreSysFileEnabled and coreSysSourceFileEnabled:
            symbol.setEnabled(True)

def deviceCacheEnable (symbol, event):
    symbol.setEnabled(event["value"])

def AddLinkerFileToProject(symbol, event):
    compiler = event["symbol"].getSelectedKey()
    arch = event["source"].getSymbolValue("CoreArchitecture")
    #No linker file when using Cortex-M23 with IAR
    if arch == "CORTEX-M23" and compiler == "IAR":
        symbol.setValue(False)
    else:
        symbol.clearValue()
    symbol.setReadOnly(not((compiler == "XC32") and ("CORTEX-M" in arch or "MIPS" in arch)))


global setLinkerScriptParams
def setLinkerScriptParams(symbol, arch, compiler, addLinkerFile):
    if compiler == "KEIL":
        configName =  Variables.get( "__CONFIGURATION_NAME" )
        symbol.setRelative(True)
        symbol.setMarkup(True)
        symbol.setSourcePath("arm/templates/keil/cortex_m/startup/scatter_file.sct")
        symbol.setOutputName(configName + ".sct")
    elif compiler == "IAR":
        symbol.setRelative(True)
        symbol.setMarkup(True)
        symbol.setSourcePath("arm/templates/iar/cortex_m/startup/iar_config_file.icf.ftl")
        symbol.setOutputName("flash.icf")
    elif compiler == "XC32":
        processor  =  Variables.get( "__PROCESSOR" )
        dfpPath    =  Variables.get("__DFP_PACK_DIR")
        symbol.setRelative(False)
        symbol.setMarkup(False)
        if "MIPS" in arch:
            if "PIC" in processor:
                processor = processor.split("PIC")[1]
            # for the device like WFI32E01 do not change processor value
            symbol.setSourcePath("{0}/xc32/{1}/p{1}.ld".format(dfpPath, processor))
            symbol.setOutputName("p{0}.ld".format(processor))
        else:
            symbol.setSourcePath("{0}/xc32/{1}/{1}.ld".format(dfpPath, processor))
            symbol.setOutputName("{0}.ld".format(processor))

    #Linker file will not be added to the project if
    #1) Compiler is IAR and the MCU arch is cortex-m23
    #2) Compiler is XC32 and option is disabled by the user
    if ((compiler == "IAR" and arch in ["CORTEX-M23"]) or
        (compiler == "XC32" and addLinkerFile == False)):
        symbol.setEnabled(False)
    else:
        symbol.setEnabled(True)


def updateLinkerScriptParams(symbol, event):
    compiler = event["source"].getSymbolByID("COMPILER_CHOICE").getSelectedKey()
    arch = event["source"].getSymbolValue("CoreArchitecture")
    addLinkerFile = event["source"].getSymbolValue("ADD_LINKER_FILE")
    setLinkerScriptParams(symbol, arch, compiler, addLinkerFile)


def generateDeviceVectorList(component):
    interrupt_dict = {}
    interruptNodes = ATDF.getNode("/avr-tools-device-file/devices/device/interrupts").getChildren()
    for index in range (0, len(interruptNodes)):
        interrupt = interruptNodes[index]
        interrupt_dict[int(interrupt.getAttribute("index"))] = (interrupt.getAttribute("name"),
                                                                interrupt.getAttribute("header:alternate-name"),
                                                                interrupt.getAttribute("caption"),
                                                                interrupt.getAttribute("header:alternate-caption"))

    min_interrupts = min(interrupt_dict.keys())
    cortexMHandlerMinSym = component.createIntegerSymbol("CORTEX_M_HANDLER_MIN", None)
    cortexMHandlerMinSym.setVisible(False)
    cortexMHandlerMinSym.setDefaultValue(min_interrupts)

    max_interrupts = max(interrupt_dict.keys())
    cortexMHandlerMaxSym = component.createIntegerSymbol("CORTEX_M_HANDLER_MAX", None)
    cortexMHandlerMaxSym.setVisible(False)
    cortexMHandlerMaxSym.setDefaultValue(max_interrupts)

    for index in range(min_interrupts, max_interrupts + 1):
        data = interrupt_dict.get(index)
        if  data is not None:
            field = "pfn_handler_t pfn{0}_Handler;".format(data[1] if data[1] else data[0])
            comment = "/* {0} {1} */".format(int(index), data[3] if (data[3] and index > 0) else data[2])
            value = field.ljust(50) + comment
        else:
            value = "pfn_handler_t pfnReserved{0}{1};".format(("C" if (index < 0) else ""), int(abs(index)))

        symName = "CORTEX_M_" + ("CORE" if (index < 0) else "PERIPHERAL") +"_HANDLER_PTR_"+ str(index)

        cortexMHandlerSym = component.createStringSymbol(symName, None)
        cortexMHandlerSym.setVisible(False)
        cortexMHandlerSym.setDefaultValue(value)

def isBootFlashPresent():
    addr_space_children = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space").getChildren()

    for mem_idx in range(0, len(addr_space_children)):
        mem_seg     = addr_space_children[mem_idx].getAttribute("name")
        mem_type    = addr_space_children[mem_idx].getAttribute("type")

        if ((any(x == mem_seg for x in BootFlashDict) == True) and (mem_type == "flash")):
            return (True, mem_seg)

    return (False, None)

def populateVtableMemRegionsList(bfm_region):
    vtableRegionList.append(bfm_region)     # this will be the default vtable region

    for region in BootFlashDict[bfm_region]:
        vtableRegionList.append(region)

def instantiateComponent( coreComponent ):
    global compilers
    global compilerSpecifics
    global armLibCSourceFile
    global devconSystemInitFile
    global debugSourceFile
    global secdebugSourceFile
    global naQualifier
    global xc32Menu
    global xc32Available
    global iarMenu
    global iarAvailable
    global processor
    global keilMenu
    global keilAvailable
    global coreArch
    global isBFMPresent

    compilerSpecifics =     None
    armLibCSourceFile =     None
    devconSystemInitFile =  None
    naQualifier = " (n/a)"      ## warn not to use; but don't prohibit

    processor =     Variables.get( "__PROCESSOR" )
    configName =    Variables.get( "__CONFIGURATION_NAME" )

    isCortexA =     False
    isCortexM =     False
    isMips    =     False
    isArm926  =     False

    xc32Available = False
    iarAvailable =  False
    keilAvailable =  False
    iarAllStacks =  False
    xc32AllStacks =  False
    iarVisiblity =  False
    xc32Visibility = False
    xcDSCVisibility = False
    xcDSCAvailable = False
    multiCompilerSupport = False

    # core architecture symbol
    coreArch = coreComponent.createStringSymbol( "CoreArchitecture", None )

    #family series symbol
    coreSeries = coreComponent.createStringSymbol( "CoreSeries", None )
    archName = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "architecture" )
    seriesName = ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "series" )
    if "33Axxx" in archName:
        if CORE_PIC32A in seriesName:
            coreArch.setDefaultValue(CORE_PIC32A)
        else: #"dsPIC33A"
            coreArch.setDefaultValue(CORE_DSPIC33A)
    else:
        coreArch.setDefaultValue( ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "architecture" ) )

    coreArch.setReadOnly( True )
    coreArch.setVisible( True )

    coreSeries.setDefaultValue( ATDF.getNode( "/avr-tools-device-file/devices/device" ).getAttribute( "series" ) )
    coreSeries.setReadOnly( True )
    coreSeries.setVisible( False )

    # productFamily (ID = "PRODUCT_FAMILY") symbol should be used everywhere to identify the product family.
    # Its default value is obtained from ATDF, but since some of the ATDF doesn't give uniquely identifiable
    # family name, same can be updated in family python like it is done in PIC32MX.py
    global productFamily
    productFamily = coreComponent.createStringSymbol("PRODUCT_FAMILY", None)
    productFamily.setReadOnly(True)
    productFamily.setVisible(False)
    productFamily.setDefaultValue(ATDF.getNode('/avr-tools-device-file/devices/device').getAttribute('family'))

    if "CORTEX-A" in coreArch.getValue():
        isCortexA = True
        baseArchDir = "arm"
        compilers = [ "XC32", "IAR", "KEIL" + naQualifier ]
        xc32Available = True
        xc32Visibility = True
        iarAvailable = True
        iarAllStacks = True
        xc32AllStacks = True
        multiCompilerSupport = True
        deviceCacheHeaderName = "cache_cortex_a.h.ftl"
    elif "CORTEX-M" in coreArch.getValue():
        isCortexM = True
        baseArchDir = "arm"
        compilers = [ "XC32", "IAR", "KEIL" ]
        xc32Available = True
        xc32Visibility = True
        iarAvailable = True
        keilAvailable = True
        multiCompilerSupport = True
        deviceCacheHeaderName = "cache_cortex_m.h.ftl"
    elif "ARM926" in coreArch.getValue():
        isArm926 = True
        baseArchDir = "arm"
        compilers = [ "XC32", "IAR", "KEIL" + naQualifier ]
        xc32Available = True
        xc32Visibility = True
        iarAvailable = True
        iarVisiblity = True
        iarAllStacks = True
        xc32AllStacks = True
        multiCompilerSupport = True
        deviceCacheHeaderName = "cache_arm9.h.ftl"
    elif CORE_DSPIC33A in coreArch.getValue(): # "dspic33a"
        #isMips = True
        baseArchDir = "mchp"
        compilers = ["XCDSC"]
        #deviceCacheHeaderName = "cache_dspic33a.h.ftl"
        xcDSCAvailable = True
        xcDSCVisibility = True
    elif CORE_PIC32A in coreArch.getValue(): # "PIC32A"
        #isMips = True
        baseArchDir = "mchp"
        compilers = ["XC32"]
        #deviceCacheHeaderName = "cache_dspic33a.h.ftl"
        xc32Available = True
        xc32Visibility = True
    else: # "mips"
        isMips = True
        baseArchDir = "mips"
        compilers = [ "XC32", "IAR" + naQualifier, "KEIL" + naQualifier ]
        deviceCacheHeaderName = "cache_pic32mz.h.ftl"
        xc32Available = True
        xc32Visibility = True

    autoComponentIDTable = [ "dfp", "cmsis" ]
    res = Database.activateComponents(autoComponentIDTable)

    devMenu = coreComponent.createMenuSymbol("CoreDevMenu", None)
    devMenu.setLabel("Device & Project Configuration")

    devCfgMenu = coreComponent.createMenuSymbol("CoreCfgMenu", devMenu)
    devCfgMenu.setLabel( Variables.get( "__PROCESSOR" ) + " Device Configuration" )
    devCfgMenu.setDescription("Hardware Configuration Bits")
    devCfgMenu.setVisible( True )

    projMenu = coreComponent.createMenuSymbol("CoreProjMenu", devMenu)
    projMenu.setLabel("Project Configuration")
    if (("dsPIC33A" not in coreArch.getValue()) and ("PIC32A" not in coreArch.getValue())):
       cplusplusProject = coreComponent.createBooleanSymbol("CPLUSPLUS_PROJECT", projMenu)
       cplusplusProject.setLabel("Generate C++ Project")
       cplusplusProject.setDescription("Generate Main Source File (main) and Application Source File (app) with .cpp file extension")
       cplusplusProject.setDefaultValue(False)

    genMainFile = coreComponent.createBooleanSymbol("CoreMainFile", projMenu)
    genMainFile.setLabel("Generate Main Source File")
    genMainFile.setDefaultValue(True)

    genMainFileName = coreComponent.createStringSymbol("CoreMainFileName", genMainFile)
    genMainFileName.setLabel("Main File Name")
    genMainFileName.setDescription("Main File Name")
    genMainFileName.setDefaultValue("main")
    genMainFileName.setDependencies(setFileVisibility, ["CoreMainFile"])

    genSysFiles = coreComponent.createBooleanSymbol("CoreSysFiles", projMenu)
    genSysFiles.setDefaultValue(True)
    genSysFiles.setLabel("Generate System Source Files")

    genSysDefFile = coreComponent.createBooleanSymbol("CoreSysDefFile", genSysFiles)
    genSysDefFile.setLabel("Generate System Definition")
    genSysDefFile.setDefaultValue(True)
    genSysDefFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysInitFile = coreComponent.createBooleanSymbol("CoreSysInitFile", genSysFiles)
    genSysInitFile.setLabel("Generate System Initialization")
    genSysInitFile.setDefaultValue(True)
    genSysInitFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysIntFile = coreComponent.createBooleanSymbol("CoreSysIntFile", genSysFiles)
    genSysIntFile.setLabel("Generate System Interrupts")
    genSysIntFile.setDefaultValue(True)
    genSysIntFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    genSysTrapsFile = coreComponent.createBooleanSymbol("CoreSysTrapsFile", genSysFiles)
    genSysTrapsFile.setLabel("Generate System Traps")
    genSysTrapsFile.setDefaultValue(True)
    genSysTrapsFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

    if ((CORE_DSPIC33A not in coreArch.getValue()) and (CORE_PIC32A not in coreArch.getValue())):
        genSysCallsFile = coreComponent.createBooleanSymbol("CoreSysCallsFile", genSysFiles)
        genSysCallsFile.setLabel("Generate LIBC Syscalls")
        genSysCallsFile.setDefaultValue(True)
        genSysCallsFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

        genSysStartupFile = coreComponent.createBooleanSymbol("CoreSysStartupFile", genSysFiles)
        genSysStartupFile.setLabel("Generate System Startup")
        genSysStartupFile.setDefaultValue(True)
        genSysStartupFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

        genSysDebugConsoleFile = coreComponent.createBooleanSymbol("CoreSysStdioSyscallsFile", genSysFiles)
        genSysDebugConsoleFile.setLabel("Generate STDIO Syscalls")
        genSysDebugConsoleFile.setDefaultValue(True)
        genSysDebugConsoleFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

        genSysExceptionFile = coreComponent.createBooleanSymbol("CoreSysExceptionFile", genSysFiles)
        genSysExceptionFile.setLabel("Generate System Exception")
        genSysExceptionFile.setDefaultValue(True)
        genSysExceptionFile.setDependencies(setSysFileVisibility, ["CoreSysFiles"])

        exceptionHandling = coreComponent.createBooleanSymbol("ADVANCED_EXCEPTION", genSysExceptionFile)
        exceptionHandling.setLabel("Use Advanced Exception Handling")
        exceptionHandling.setDefaultValue(False)
        exceptionHandling.setDependencies(setFileVisibility, ["CoreSysExceptionFile"])

        filteringExceptionHandling = coreComponent.createBooleanSymbol("FILTERING_EXCEPTION", exceptionHandling)
        filteringExceptionHandling.setLabel("Use Advanced Exception Handling With Filtering Support")
        filteringExceptionHandling.setDefaultValue(False)
        filteringExceptionHandling.setVisible(False)
        if isMips:
            filteringExceptionHandling.setDependencies(setFileVisibility, ["ADVANCED_EXCEPTION"])

        ## cache macros
        deviceCacheHeaderFile = coreComponent.createFileSymbol("DEVICE_CACHE_H", None)
        deviceCacheHeaderFile.setSourcePath( "/templates/" + deviceCacheHeaderName )
        deviceCacheHeaderFile.setOutputName("device_cache.h")
        deviceCacheHeaderFile.setMarkup(True)
        deviceCacheHeaderFile.setOverwrite(True)
        deviceCacheHeaderFile.setDestPath("")
        deviceCacheHeaderFile.setProjectPath("config/" + configName + "/")
        deviceCacheHeaderFile.setType("HEADER")
    if isMips:
        deviceCacheHeaderFile.setEnabled(False)
        deviceCacheHeaderFile.setDependencies(deviceCacheEnable, ["USE_CACHE_MAINTENANCE"])

    ## toolchain specifics
    toolChainSpecifics = coreComponent.createFileSymbol( None, None )
    toolChainSpecifics.setSourcePath( baseArchDir + "/templates/toolchain_specifics.h.ftl" )
    toolChainSpecifics.setOutputName( "toolchain_specifics.h" );
    toolChainSpecifics.setMarkup( True )
    toolChainSpecifics.setOverwrite( True )
    toolChainSpecifics.setDestPath("")
    toolChainSpecifics.setProjectPath("config/" + configName + "/")
    toolChainSpecifics.setType("HEADER")

    ## toolChainMenu
    toolChainMenu = coreComponent.createMenuSymbol("CoreToolChainMenu", projMenu)
    toolChainMenu.setLabel("Tool Chain Selections")

    ## compiler choice
    compilerChoice = coreComponent.createKeyValueSetSymbol( "COMPILER_CHOICE", toolChainMenu )
    compilerChoice.setLabel( "Compiler" )
    compilerChoice.setOutputMode( "Key" )
    compilerChoice.setDisplayMode( "Key" )
    compilerChoice.setVisible( True )
    compilerDefaultFound = False
    for index in range( 0, len( compilers ) ):
        if naQualifier not in compilers[index]:
            compilerChoice.addKey( compilers[ index ], str( index ), compilers[ index ] )
            if (not compilerDefaultFound) and (naQualifier not in compilers[ index ]):
                compilerDefaultFound = True
                compilerChoice.setDefaultValue( index )
                compilerChoice.setValue( index, 2 )

    compilerChoice.setReadOnly(not multiCompilerSupport)

    if ((CORE_DSPIC33A not in coreArch.getValue()) and (CORE_PIC32A not in coreArch.getValue())):
        #Linker Settings
        addLinkerFile = coreComponent.createBooleanSymbol("ADD_LINKER_FILE", toolChainMenu)
        addLinkerFile.setLabel("Add linker file to project")
        addLinkerFile.setDescription("Copies linker file into the project "
        "configuration folder and uses it for linking the project. Uncheck this "
        "option, if a custom linker script is used.")
        addLinkerFile.setDefaultValue(True)

        #We only allow disabling custom linker script when using XC32 compiler with non-MPU masks
        addLinkerFile.setReadOnly( not((compilerChoice.getSelectedKey() == "XC32") and
                                         ("CORTEX-M" in coreArch.getValue() or "MIPS" in coreArch.getValue())))

        addLinkerFile.setDependencies(AddLinkerFileToProject, ["COMPILER_CHOICE"])

        ## Dummy Symbol to trigger compilerUpdate callback on compiler choice change
        compilerUpdateSym = coreComponent.createBooleanSymbol("COMPILER_UPDATE", toolChainMenu)
        compilerUpdateSym.setVisible(False)
        compilerUpdateSym.setDependencies( compilerUpdate, [ "COMPILER_CHOICE" ] )

        ## xc32 Tool Config
        xc32Menu = coreComponent.createMenuSymbol("CoreXC32Menu", toolChainMenu)
        xc32Menu.setLabel("XC32 Global Options")
        xc32Menu.setVisible( xc32Available & xc32Visibility )


        xc32LdMenu = coreComponent.createMenuSymbol("CoreXC32_LD", xc32Menu)
        xc32LdMenu.setLabel("Linker")

        xc32LdGeneralMenu = coreComponent.createMenuSymbol("CoreXC32_LD_General", xc32LdMenu)
        xc32LdGeneralMenu.setLabel("General")

        xc32HeapSize = coreComponent.createIntegerSymbol("XC32_HEAP_SIZE", xc32LdGeneralMenu)
        xc32HeapSize.setLabel("Heap Size (bytes)")
        xc32HeapSize.setDefaultValue( 512 )

        xc32DataInit = coreComponent.createBooleanSymbol("XC32_DATA_INIT", xc32LdGeneralMenu)
        xc32DataInit.setLabel("Initialize Data")
        xc32DataInit.setDefaultValue(True)
        xc32DataInit.setReadOnly(True)

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            xc32SecureHeapSize = coreComponent.createIntegerSymbol("XC32_SECURE_HEAP_SIZE", xc32LdGeneralMenu)
            xc32SecureHeapSize.setLabel("Secure Heap Size (bytes)")
            xc32SecureHeapSize.setDefaultValue( 512 )

        if isCortexA == True or isArm926 == True:
            xc32UsrStackSize = coreComponent.createIntegerSymbol("XC32_USR_STACK_SIZE", xc32LdGeneralMenu)
            xc32UsrStackSize.setLabel( "User/System Stack Size (bytes)" )
            xc32UsrStackSize.setDefaultValue( 4096 )
            xc32UsrStackSize.setVisible( xc32Available )

            xc32FiqStackSize = coreComponent.createIntegerSymbol("XC32_FIQ_STACK_SIZE", xc32LdGeneralMenu)
            xc32FiqStackSize.setLabel("FIQ Stack Size (bytes)")
            xc32FiqStackSize.setDefaultValue(96)
            xc32FiqStackSize.setVisible( xc32AllStacks )

            xc32IrqStackSize = coreComponent.createIntegerSymbol("XC32_IRQ_STACK_SIZE", xc32LdGeneralMenu)
            xc32IrqStackSize.setLabel("IRQ Stack Size (bytes)")
            xc32IrqStackSize.setDefaultValue(96)
            xc32IrqStackSize.setVisible( xc32AllStacks )

            xc32SvcStackSize = coreComponent.createIntegerSymbol("XC32_SVC_STACK_SIZE", xc32LdGeneralMenu)
            xc32SvcStackSize.setLabel("Supervisor Stack Size (bytes)")
            xc32SvcStackSize.setDefaultValue(4096)
            xc32SvcStackSize.setVisible( xc32AllStacks )

            xc32AbtStackSize = coreComponent.createIntegerSymbol("XC32_ABT_STACK_SIZE", xc32LdGeneralMenu)
            xc32AbtStackSize.setLabel("Abort Stack Size (bytes)")
            xc32AbtStackSize.setDefaultValue(64)
            xc32AbtStackSize.setVisible( xc32AllStacks )

            xc32UndStackSize = coreComponent.createIntegerSymbol("XC32_UND_STACK_SIZE", xc32LdGeneralMenu)
            xc32UndStackSize.setLabel("Undefined Stack Size (bytes)")
            xc32UndStackSize.setDefaultValue(64)
            xc32UndStackSize.setVisible( xc32AllStacks )
        elif isMips == True:
            xc32ISAMode = coreComponent.createBooleanSymbol("XC32_ISA_MODE", xc32Menu)
            if "PIC32MX" in processor: #MIPS16 mode
                xc32ISAMode.setLabel("Generate MIPS16 16-bit Code")
            else: #microMIPS mode
                xc32ISAMode.setLabel("Generate microMIPS Compressed Code")
            xc32ISAMode.setDefaultValue(False)



        xc32LdSymbolsMacrosMenu = coreComponent.createMenuSymbol("CoreXC32_SYMBOLS_MACROS", xc32LdMenu)
        xc32LdSymbolsMacrosMenu.setLabel("Symbols & Macros")
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            xc32LdSymbolsMacrosMenu.setVisible(False)

        xc32LdAppStartAddress = coreComponent.createStringSymbol("APP_START_ADDRESS", xc32LdSymbolsMacrosMenu)
        xc32LdAppStartAddress.setLabel("Application Start Address (Hex)")
        xc32LdAppStartAddress.setDefaultValue(str(hex(flash_start))[2:])

        isBFMPresent, bfm_region = isBootFlashPresent()

        #Exception for BZ3/BZ6 series. For WBZ35 device, the VTABLE must be in PFM although it has Boot Flash Memory.
        if any(ele in  Database.getSymbolValue("core", "CoreSeries") for ele in ["BZ3", "BZ6"]):
            isBFMPresent = False

        if isBFMPresent == True:
            populateVtableMemRegionsList(bfm_region)
            xc32LdAppVtableMemRegion = coreComponent.createComboSymbol("VTABLE_MEM_REGION", xc32LdSymbolsMacrosMenu, vtableRegionList)
            xc32LdAppVtableMemRegion.setLabel("Place Vector Table in ")
            xc32LdAppVtableMemRegion.setDefaultValue(vtableRegionList[0])

        # set XC32-LD option to Modify ROM Start address and length
        xc32LdPreprocessroMacroSym = coreComponent.createSettingSymbol("XC32_LINKER_PREPROC_MARCOS", xc32LdSymbolsMacrosMenu)
        xc32LdPreprocessroMacroSym.setCategory("C32-LD")
        xc32LdPreprocessroMacroSym.setKey("preprocessor-macros")
        xc32LdMacorVal = ""
        if isBFMPresent == True:
            xc32LdMacorVal = getVtablePlacementParams(xc32LdAppVtableMemRegion.getValue())

        xc32LdPreprocessroMacroSym.setAppend(True, ";=")
        xc32LdPreprocessroMacroSym.setDependencies(updateAppPlacementParams, ["APP_START_ADDRESS", "VTABLE_MEM_REGION"])

        ## iar Tool Config
        iarMenu = coreComponent.createMenuSymbol("CoreIARMenu", toolChainMenu)
        iarMenu.setLabel("IAR Global Options")
        iarMenu.setVisible( iarAvailable & iarVisiblity )

        iarLdMenu = coreComponent.createMenuSymbol("CoreIAR_LD", iarMenu)
        iarLdMenu.setLabel( "Linker" )

        iarLdGeneralMenu = coreComponent.createMenuSymbol("CoreIAR_LD_General", iarLdMenu)
        iarLdGeneralMenu.setLabel( "General" )

        iarHeapSize = coreComponent.createIntegerSymbol("IAR_HEAP_SIZE", iarLdGeneralMenu)
        iarHeapSize.setLabel( "Heap Size (bytes)" )
        iarHeapSize.setDefaultValue( 512 )
        iarHeapSize.setVisible( iarAvailable )

        iarUsrStackSize = coreComponent.createIntegerSymbol("IAR_USR_STACK_SIZE", iarLdGeneralMenu)
        iarUsrStackSize.setLabel( "User{} Stack Size (bytes)".format("/System" if iarAllStacks else "") )
        iarUsrStackSize.setDefaultValue( 4096 )
        iarUsrStackSize.setVisible( iarAvailable )

        ## iarAllStacks
        iarFiqStackSize = coreComponent.createIntegerSymbol("IAR_FIQ_STACK_SIZE", iarLdGeneralMenu)
        iarFiqStackSize.setLabel("FIQ Stack Size (bytes)")
        iarFiqStackSize.setDefaultValue(96)
        iarFiqStackSize.setVisible( iarAllStacks )

        iarIrqStackSize = coreComponent.createIntegerSymbol("IAR_IRQ_STACK_SIZE", iarLdGeneralMenu)
        iarIrqStackSize.setLabel("IRQ Stack Size (bytes)")
        iarIrqStackSize.setDefaultValue(96)
        iarIrqStackSize.setVisible( iarAllStacks )

        iarSvcStackSize = coreComponent.createIntegerSymbol("IAR_SVC_STACK_SIZE", iarLdGeneralMenu)
        iarSvcStackSize.setLabel("Supervisor Stack Size (bytes)")
        iarSvcStackSize.setDefaultValue(4096)
        iarSvcStackSize.setVisible( iarAllStacks )

        iarAbtStackSize = coreComponent.createIntegerSymbol("IAR_ABT_STACK_SIZE", iarLdGeneralMenu)
        iarAbtStackSize.setLabel("Abort Stack Size (bytes)")
        iarAbtStackSize.setDefaultValue(64)
        iarAbtStackSize.setVisible( iarAllStacks )

        iarUndStackSize = coreComponent.createIntegerSymbol("IAR_UND_STACK_SIZE", iarLdGeneralMenu)
        iarUndStackSize.setLabel("Undefined Stack Size (bytes)")
        iarUndStackSize.setDefaultValue(64)
        iarUndStackSize.setVisible( iarAllStacks )

        ## keil Tool Config
        keilMenu = coreComponent.createMenuSymbol("CoreKEILMenu", toolChainMenu)
        keilMenu.setLabel("KEIL Global Options")
        keilMenu.setVisible( keilAvailable == True)

        keilLdMenu = coreComponent.createMenuSymbol("CoreKEIL_LD", keilMenu)
        keilLdMenu.setLabel( "Linker" )

        keilLdGeneralMenu = coreComponent.createMenuSymbol("CoreKEIL_LD_General", keilLdMenu)
        keilLdGeneralMenu.setLabel( "General" )

        keilStackSize = coreComponent.createIntegerSymbol("KEIL_STACK_SIZE", keilLdGeneralMenu)
        keilStackSize.setLabel( "Stack Size (bytes)" )
        keilStackSize.setDefaultValue( 4096 )

        keilStackWarning = coreComponent.createMenuSymbol("KEIL_STACK_WARNING", keilLdGeneralMenu)
        keilStackWarning.setLabel("******** Main stack size needs to be integer multiple of 8 *******")
        keilStackWarning.setVisible( False )
        keilStackWarning.setDependencies(alignmentWarning, ["KEIL_STACK_SIZE"])

        keilHeapSize = coreComponent.createIntegerSymbol("KEIL_HEAP_SIZE", keilLdGeneralMenu)
        keilHeapSize.setLabel( "Heap Size (bytes)" )
        keilHeapSize.setDefaultValue( 512 )

        keilHeapWarning = coreComponent.createMenuSymbol("KEIL_HEAP_WARNING", keilLdGeneralMenu)
        keilHeapWarning.setLabel("******** Heap size needs to be an integer multiple of 8 *******")
        keilHeapWarning.setVisible( False )
        keilHeapWarning.setDependencies(alignmentWarning, ["KEIL_HEAP_SIZE"])

        keilHeapStackSize = coreComponent.createStringSymbol("KEIL_STACK_HEAP_SIZE", keilLdGeneralMenu)
        keilHeapStackSize.setVisible(False)
        keilHeapStackSize.setValue("0x%X" % (keilStackSize.getValue() + keilHeapSize.getValue()))
        keilHeapStackSize.setDependencies(setKeilHeapStackSize, ["KEIL_STACK_SIZE", "KEIL_HEAP_SIZE"])

    # Device name symbol
    deviceName = coreComponent.createStringSymbol("DEVICE_NAME", None)
    deviceName.setVisible(False)
    deviceName.setDefaultValue(Variables.get("__PROCESSOR"))

    if "CORTEX-M" in coreArch.getValue():
        #Generate device vector handler related string symbols
        generateDeviceVectorList(coreComponent)

        #ROM and RAM memory map
        nodeIFLASH = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[type=\"flash\"]")
        if nodeIFLASH is not None:
            startAddressIROM1 = coreComponent.createStringSymbol("IROM1_START", None)
            startAddressIROM1.setVisible(False)
            startAddressIROM1.setDefaultValue(nodeIFLASH.getAttribute("start"))

            sizeAddressIROM1 = coreComponent.createStringSymbol("IROM1_SIZE", None)
            sizeAddressIROM1.setVisible(False)
            sizeAddressIROM1.setDefaultValue(nodeIFLASH.getAttribute("size"))

            endAddressIROM1 = coreComponent.createStringSymbol("IROM1_END", None)
            endAddressIROM1.setVisible(False)
            startAddressInt = int(nodeIFLASH.getAttribute("start"), 16)
            sizeInt = int(nodeIFLASH.getAttribute("size"), 16)
            endAddressInt = startAddressInt + sizeInt - 1
            endAddressIROM1.setDefaultValue("0x%08X" % endAddressInt)

        if coreArch.getValue() == "CORTEX-M33":
            nodeIRAM = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"HSRAM_RET\"]")
            if nodeIRAM == None:
                nodeIRAM = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[type=\"ram\"]")
        else:
            nodeIRAM = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[type=\"ram\"]")

        if nodeIRAM is not None:
            startAddressIRAM1 = coreComponent.createStringSymbol("IRAM1_START", None)
            startAddressIRAM1.setVisible(False)
            startAddressIRAM1.setDefaultValue(nodeIRAM.getAttribute("start"))

            sizeAddressIRAM1 = coreComponent.createStringSymbol("IRAM1_SIZE", None)
            sizeAddressIRAM1.setVisible(False)
            sizeAddressIRAM1.setDefaultValue(nodeIRAM.getAttribute("size"))

            endAddressIRAM1 = coreComponent.createStringSymbol("IRAM1_END", None)
            endAddressIRAM1.setVisible(False)
            startAddressInt = int(nodeIRAM.getAttribute("start"), 16)
            sizeInt = int(nodeIRAM.getAttribute("size"), 16)
            endAddressInt = startAddressInt + sizeInt - 1
            endAddressIRAM1.setDefaultValue("0x%08X" % endAddressInt)


    ############################# MISRAC Menu #################################
    misracMenu = coreComponent.createMenuSymbol("MISRAC_MENU", projMenu)
    misracMenu.setLabel( "MISRA-C:2012" )

    suppressionMenu = coreComponent.createMenuSymbol("SUPPRESS_DEVIATIONS_MENU", misracMenu)
    suppressionMenu.setLabel("Suppress Deviations")

    coveritySuppression = coreComponent.createBooleanSymbol("COVERITY_SUPPRESS_DEVIATION", suppressionMenu)
    coveritySuppression.setLabel("Suppress for Coverity")

    #################### Main File ####################
    # generate main.c file
    mainSourceFile = coreComponent.createFileSymbol("MAIN_C", None)
    mainSourceFile.setSourcePath("templates/main.c.ftl")
    mainSourceFile.setOutputName("main.c")
    mainSourceFile.setMarkup(True)
    mainSourceFile.setOverwrite(False)
    mainSourceFile.setDestPath("../../")
    mainSourceFile.setProjectPath("")
    mainSourceFile.setType("SOURCE")
    mainSourceFile.setDependencies( genMainSourceFile, ["CoreMainFile", "CoreMainFileName", "CPLUSPLUS_PROJECT"] )

    bspHeaderInclude =          coreComponent.createListSymbol( "LIST_BSP_MACRO_INCLUDES", None )
    bspHeaderInclude =          coreComponent.createListSymbol( "LIST_BSP_INITIALIZATION", None )

    # list of SYS_PORTS
    systemPortIncludesList =    coreComponent.createListSymbol( "LIST_SYS_PORT_INCLUDES", None )

    # list for configuration.h
    systemConfigIncludesList =  coreComponent.createListSymbol( "LIST_SYSTEM_CONFIG_H_GLOBAL_INCLUDES",                 None )
    systemConfigSysList =       coreComponent.createListSymbol( "LIST_SYSTEM_CONFIG_H_SYSTEM_SERVICE_CONFIGURATION",    None )
    systemConfigDrvList =       coreComponent.createListSymbol( "LIST_SYSTEM_CONFIG_H_DRIVER_CONFIGURATION",            None )
    systemConfigMWList =        coreComponent.createListSymbol( "LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION",        None )
    systemConfigAppList =       coreComponent.createListSymbol( "LIST_SYSTEM_CONFIG_H_APPLICATION_CONFIGURATION",       None )

    # list for sys_task.h file
    taskHandleDeclList =        coreComponent.createListSymbol( "LIST_SYSTEM_TASKS_HANDLE_DECLARATION",     None )

    # list for task.c file
    taskSysList =               coreComponent.createListSymbol( "LIST_SYSTEM_TASKS_C_CALL_SYSTEM_TASKS",    None )
    taskDrvList =               coreComponent.createListSymbol( "LIST_SYSTEM_TASKS_C_CALL_DRIVER_TASKS",    None )
    taskLibList =               coreComponent.createListSymbol( "LIST_SYSTEM_TASKS_C_CALL_LIB_TASKS",       None )
    taskGenAppList =            coreComponent.createListSymbol( "LIST_SYSTEM_TASKS_C_GEN_APP",              None )
    taskGenRtosAppList =        coreComponent.createListSymbol( "LIST_SYSTEM_RTOS_TASKS_C_GEN_APP",         None )
    taskRtosDefList =           coreComponent.createListSymbol( "LIST_SYSTEM_RTOS_TASKS_C_DEFINITIONS",     None )
    taskRtosSchedList =         coreComponent.createListSymbol( "LIST_SYSTEM_RTOS_TASKS_C_CALL_SCHEDULAR",  None )

    #################### System Files ####################
    # generate definitions.h file
    defHeaderFile = coreComponent.createFileSymbol("DEFINITIONS_H", None)
    defHeaderFile.setSourcePath("templates/definitions.h.ftl")
    defHeaderFile.setOutputName("definitions.h")
    defHeaderFile.setMarkup(True)
    defHeaderFile.setOverwrite(True)
    defHeaderFile.setDestPath("")
    defHeaderFile.setProjectPath("config/" + configName + "/")
    defHeaderFile.setType("HEADER")
    defHeaderFile.setDependencies( genSysSourceFile, [ "CoreSysDefFile", "CoreSysFiles" ] )

    systemDefinitionsHeadersList =      coreComponent.createListSymbol( "LIST_SYSTEM_DEFINITIONS_H_INCLUDES",       None )
    systemDefinitionsObjList =          coreComponent.createListSymbol( "LIST_SYSTEM_DEFINITIONS_H_OBJECTS",        None )
    systemDefinitionsExternsList =      coreComponent.createListSymbol( "LIST_SYSTEM_DEFINITIONS_H_EXTERNS",        None )
    systemAppDefinitionsHeadersList =   coreComponent.createListSymbol( "LIST_SYSTEM_APP_DEFINITIONS_H_INCLUDES",   None )

    # generate initialization.c file
    initSourceFile =            coreComponent.createFileSymbol("INITIALIZATION_C", None)
    initSourceFile.setSourcePath("templates/initialization.c.ftl")
    initSourceFile.setOutputName("initialization.c")
    initSourceFile.setMarkup(True)
    initSourceFile.setOverwrite(True)
    initSourceFile.setDestPath("")
    initSourceFile.setProjectPath("config/" + configName + "/")
    initSourceFile.setType("SOURCE")
    initSourceFile.setDependencies( genSysSourceFile, [ "CoreSysInitFile", "CoreSysFiles" ] )

    systemInitFuseList =        coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_CONFIG_BITS_INITIALIZATION",    None )
    systemInitDrvList =         coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_DRIVER_INITIALIZATION_DATA",    None )
    systemInitLibList =         coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_LIBRARY_INITIALIZATION_DATA",   None )
    systemInitStaticFuncList =  coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_INITIALIZER_STATIC_FUNCTIONS",  None )
    systemInitSysList =         coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYSTEM_INITIALIZATION",         None )
    systemAppInitDataList =     coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_APP_INITIALIZE_DATA",           None )

    systemInitStart1List =      coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START1",         None )
    systemInitStartList =       coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START",          None )
    systemInitCoreList =        coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE",           None )
    systemInitPeripheral1List = coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS1",   None )
    systemInitCore1List =       coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_CORE1",          None )
    systemInitInterruptList =   coreComponent.createListSymbol( "LIST_SYSTEM_INIT_INTERRUPTS",                      None )
    systemInitPeripheralList =  coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS",    None )
    systemInitDriverList =      coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DRIVERS",        None )
    systemInitSysList =         coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_INITIALIZE_SYSTEM_SERVICES",    None )
    systemInitMWList =          coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_INITIALIZE_MIDDLEWARE",         None )
    systemInitEndList =         coreComponent.createListSymbol( "LIST_SYSTEM_INIT_C_SYS_INITIALIZE_END",            None )

    # generate interrupts.c file
    intSourceFile = coreComponent.createFileSymbol( "INTERRUPTS_C", None )
    intSourceFile.setSourcePath("templates/interrupts.c.ftl")
    intSourceFile.setOutputName("interrupts.c")
    intSourceFile.setMarkup(True)
    intSourceFile.setOverwrite(True)
    intSourceFile.setDestPath("")
    intSourceFile.setProjectPath("config/" + configName + "/")
    intSourceFile.setType("SOURCE")
    intSourceFile.setDependencies(genSysSourceFile, ["CoreSysIntFile", "CoreSysFiles"])

    # generate interrupts.h file
    intHeaderFile = coreComponent.createFileSymbol( "INTERRUPTS_H", None )
    intHeaderFile.setSourcePath("templates/interrupts.h.ftl")
    intHeaderFile.setOutputName("interrupts.h")
    intHeaderFile.setMarkup(True)
    intHeaderFile.setOverwrite(True)
    intHeaderFile.setDestPath("")
    intHeaderFile.setProjectPath("config/" + configName + "/")
    intHeaderFile.setType("HEADER")
    intHeaderFile.setDependencies(genSysSourceFile, ["CoreSysIntFile", "CoreSysFiles"])

    if "CORTEX-M" in coreArch.getValue():
    # generate device_vectors.h file
        intHeaderFile = coreComponent.createFileSymbol( "DEVICE_VECTORS_H", None )
        intHeaderFile.setSourcePath("templates/device_vectors.h.ftl")
        intHeaderFile.setOutputName("device_vectors.h")
        intHeaderFile.setMarkup(True)
        intHeaderFile.setOverwrite(True)
        intHeaderFile.setDestPath("")
        intHeaderFile.setProjectPath("config/" + configName + "/")
        intHeaderFile.setType("HEADER")


    if "MIPS" in Database.getSymbolValue("core","CoreArchitecture"):
        intASMSourceFile = coreComponent.createFileSymbol("INTERRUPTS_ASM", None)
        intASMSourceFile.setSourcePath("templates/interrupts_a.S.ftl")
        intASMSourceFile.setOutputName("interrupts_a.S")
        intASMSourceFile.setDestPath("")
        intASMSourceFile.setProjectPath("config/" + configName + "/")
        intASMSourceFile.setType("SOURCE")
        intASMSourceFile.setMarkup(True)
        intASMSourceFile.setOverwrite(True)
        intASMSourceFile.setEnabled(False)
        intASMSourceFile.setDependencies(genSysIntASMSourceFile, ["CoreSysIntFile", "CoreSysFiles", "HarmonyCore.SELECT_RTOS", "FreeRTOS.SET_RTOS"])

    systemIntHeadersList =                  coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_C_INCLUDES",         None )
    systemIntHandlerdeclsList =             coreComponent.createListSymbol("LIST_SYSTEM_INTERRUPT_HANDLER_DECLS",       None)
    systemIntVectorsList =                  coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_C_VECTORS",          None )
    systemIntVectorsMultipleHandlesList =   coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_MULTIPLE_HANDLERS",  None )
    systemIntVectorsWeakHandlesList =       coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_WEAK_HANDLERS",      None )
    systemIntVectorsSharedHandlesList =     coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_SHARED_HANDLERS",    None )
    systemIntVectorsHandlesList =           coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_HANDLERS",           None )
    systemIntVectorsASMList =               coreComponent.createListSymbol( "LIST_SYSTEM_INTERRUPT_ASM",                None )

    if ("CORTEX-M" in coreArch.getValue()) or ("MIPS" in coreArch.getValue()):
        # generate exceptions.c file
        exceptSourceFile = coreComponent.createFileSymbol("EXCEPTIONS_C", None)
        if "MIPS" in coreArch.getValue():
            exceptSourceFile.setSourcePath("templates/exceptions_xc32_mips.c.ftl")
        else:
            exceptSourceFile.setSourcePath("templates/exceptions_xc32_cortex_m.c.ftl")
        exceptSourceFile.setOutputName("exceptions.c")
        exceptSourceFile.setMarkup(True)
        exceptSourceFile.setOverwrite(True)
        exceptSourceFile.setDestPath("")
        exceptSourceFile.setProjectPath("config/" + configName + "/")
        exceptSourceFile.setType("SOURCE")
        exceptSourceFile.setDependencies( genSysSourceFile, [ "CoreSysExceptionFile", "CoreSysFiles", "FILTERING_EXCEPTION", "ADVANCED_EXCEPTION" ] )

        # generate exceptionsHandler.s file
        exceptionAsmSourceFile = coreComponent.createFileSymbol("EXCEPTIONS_ASM", None)
        if "MIPS" in coreArch.getValue():
            exceptionAsmSourceFile.setSourcePath("templates/general-exception-context_mips.S.ftl")
        elif (compilers[Database.getSymbolValue("core", "COMPILER_CHOICE")] == "IAR"):
            exceptionAsmSourceFile.setSourcePath("templates/exceptionsHandler_iar.s.ftl")
        else:
            exceptionAsmSourceFile.setSourcePath("templates/exceptionsHandler.s.ftl")
        exceptionAsmSourceFile.setOutputName("exceptionsHandler.S")
        exceptionAsmSourceFile.setMarkup(True)
        exceptionAsmSourceFile.setOverwrite(True)
        exceptionAsmSourceFile.setDestPath("")
        exceptionAsmSourceFile.setProjectPath("config/" + configName + "/")
        exceptionAsmSourceFile.setType("SOURCE")
        exceptionAsmSourceFile.setEnabled(False)
        exceptionAsmSourceFile.setDependencies( genExceptionAsmSourceFile, ["CoreSysFiles", "CoreSysExceptionFile", "ADVANCED_EXCEPTION"])

        linkerFile = coreComponent.createFileSymbol("LINKER_SCRIPT", None)
        linkerFile.setOverwrite(True)
        linkerFile.setType("LINKER")
        linkerFile.setProjectPath("config/" + configName + "/")
        linkerFile.setDestPath("")
        setLinkerScriptParams(linkerFile, coreArch.getValue(), compilerChoice.getSelectedKey(), addLinkerFile.getValue())
        linkerFile.setDependencies(updateLinkerScriptParams, ["COMPILER_CHOICE", "ADD_LINKER_FILE"])

        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            linkerFile = coreComponent.createFileSymbol("SECURE_LINKER_SCRIPT", None)
            linkerFile.setOverwrite(True)
            linkerFile.setType("LINKER")
            linkerFile.setProjectPath("config/" + configName + "/")
            linkerFile.setDestPath("")
            linkerFile.setSecurity("SECURE")
            setLinkerScriptParams(linkerFile, coreArch.getValue(), compilerChoice.getSelectedKey(), addLinkerFile.getValue())
            linkerFile.setDependencies(updateLinkerScriptParams, ["COMPILER_CHOICE", "ADD_LINKER_FILE"])


    if "MIPS" in coreArch.getValue():
        # set XC32 ISA mode
        xc32ISAModeSettingSym = coreComponent.createSettingSymbol("XC32_ISA_MODE_SETTING", None)
        xc32ISAModeSettingSym.setCategory("C32")
        if "PIC32MX" in processor: #MIPS16 mode
            xc32ISAModeSettingSym.setKey("generate-16-bit-code")
        else: #microMIPS mode
            xc32ISAModeSettingSym.setKey("generate-micro-compressed-code")
        xc32ISAModeSettingSym.setValue("false")
        xc32ISAModeSettingSym.setDependencies(ISA_modeCallBack, ["XC32_ISA_MODE"])

        # set XC32 ISA mode
        xc32cppISAModeSettingSym = coreComponent.createSettingSymbol("XC32CPP_ISA_MODE_SETTING", None)
        xc32cppISAModeSettingSym.setCategory("C32CPP")
        if "PIC32MX" in processor: #MIPS16 mode
            xc32cppISAModeSettingSym.setKey("generate-16-bit-code")
        else: #microMIPS mode
            xc32cppISAModeSettingSym.setKey("generate-micro-compressed-code")
        xc32cppISAModeSettingSym.setValue("false")
        xc32cppISAModeSettingSym.setDependencies(ISA_modeCallBack, ["XC32_ISA_MODE"])

    if ((CORE_DSPIC33A in coreArch.getValue()) or (CORE_PIC32A in coreArch.getValue())):
        # generate traps.c file
        trapsSourceFile = coreComponent.createFileSymbol("TRAPS_33A_C", None)
        trapsSourceFile.setSourcePath("templates/traps_33a.c.ftl")
        trapsSourceFile.setOutputName("traps.c")
        trapsSourceFile.setMarkup(True)
        trapsSourceFile.setOverwrite(True)
        trapsSourceFile.setDestPath("")
        trapsSourceFile.setProjectPath("config/" + configName + "/")
        trapsSourceFile.setType("SOURCE")
        trapsSourceFile.setDependencies(
            genSysSourceFile,
            ["CoreSysTrapsFile", "CoreSysFiles"],
        )

        # generate traps.h file
        trapsHeaderFile = coreComponent.createFileSymbol("TRAPS_33A_H", None)
        trapsHeaderFile.setSourcePath("templates/traps_33a.h.ftl")
        trapsHeaderFile.setOutputName("traps.h")
        trapsHeaderFile.setMarkup(True)
        trapsHeaderFile.setOverwrite(True)
        trapsHeaderFile.setDestPath("")
        trapsHeaderFile.setProjectPath("config/" + configName + "/")
        trapsHeaderFile.setType("HEADER")
        trapsHeaderFile.setDependencies(
            genSysSourceFile,
            ["CoreSysTrapsFile", "CoreSysFiles"],
        )


    if ((CORE_DSPIC33A not in coreArch.getValue()) and (CORE_PIC32A not in coreArch.getValue())):
        # set XC32 heap size
        xc32HeapSizeSym = coreComponent.createSettingSymbol("XC32_HEAP", None)
        xc32HeapSizeSym.setCategory("C32-LD")
        xc32HeapSizeSym.setKey("heap-size")
        xc32HeapSizeSym.setValue(str(xc32HeapSize.getValue()))
        xc32HeapSizeSym.setDependencies(heapSizeCallBack, ["XC32_HEAP_SIZE"])

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        xc32SecureHeapSizeSym = coreComponent.createSettingSymbol("XC32_SECURE_HEAP", None)
        xc32SecureHeapSizeSym.setCategory("C32-LD")
        xc32SecureHeapSizeSym.setKey("heap-size")
        xc32SecureHeapSizeSym.setValue(str(xc32SecureHeapSize.getValue()))
        xc32SecureHeapSizeSym.setDependencies(heapSizeCallBack, ["XC32_SECURE_HEAP_SIZE"])
        xc32SecureHeapSizeSym.setSecurity("SECURE")

    # set include path and monitor file
    packsPath = ""
    if "CORTEX-A" in Database.getSymbolValue("core","CoreArchitecture"):
        packsPath = "../src/packs/" + processor + "_DFP;../src/packs/CMSIS/CMSIS/Core_A/Include" + ";../src/packs/CMSIS/"
    elif "CORTEX-M" in Database.getSymbolValue("core","CoreArchitecture"):
        packsPath = "../src/packs/" + processor + "_DFP;../src/packs/CMSIS/CMSIS/Core/Include" + ";../src/packs/CMSIS/"
    elif "ARM9" in Database.getSymbolValue("core","CoreArchitecture"):
        packsPath = "../src/packs/" + processor + "_DFP;"
    else: #mips and 33Axxx
        packsPath = ""

    if  CORE_DSPIC33A in coreArch.getValue():
        defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
        defSym.setCategory("C30")
        defSym.setKey("extra-include-directories")
        defSym.setValue( "../src;../src/config/" + configName + ";" + packsPath)
        defSym.setAppend(True, ";")
    elif CORE_PIC32A in coreArch.getValue():
        defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
        defSym.setCategory("C32")
        defSym.setKey("extra-include-directories")
        defSym.setValue( "../src;../src/config/" + configName + ";" + packsPath)
        defSym.setAppend(True, ";")
    else:
        defSym = coreComponent.createSettingSymbol("XC32_INCLUDE_DIRS", None)
        defSym.setCategory("C32")
        defSym.setKey("extra-include-directories")
        defSym.setValue( "../src;../src/config/" + configName + ";" + packsPath)
        defSym.setAppend(True, ";")

        defXc32cppSym = coreComponent.createSettingSymbol("XC32CPP_INCLUDE_DIRS", None)
        defXc32cppSym.setCategory("C32CPP")
        defXc32cppSym.setKey("extra-include-directories")
        defXc32cppSym.setValue(defSym.getValue())
        defXc32cppSym.setAppend(True, ";")

        # set XC32 option to not use the device startup code
        xc32NoDeviceStartupCodeSym = coreComponent.createSettingSymbol("XC32_NO_DEVICE_STARTUP_CODE", None)
        xc32NoDeviceStartupCodeSym.setCategory("C32-LD")
        xc32NoDeviceStartupCodeSym.setKey("no-device-startup-code")
        xc32NoDeviceStartupCodeSym.setValue("true")



    global compilerSelected
    compilerSelected = compilerChoice.getSelectedKey().replace( naQualifier, "" ).lower()
    if ((CORE_DSPIC33A not in coreArch.getValue()) and (CORE_PIC32A not in coreArch.getValue())):
        debugSourceFile = coreComponent.createFileSymbol( "DEBUG_CONSOLE_C", None )
        debugSourceFile.setMarkup( True )
        debugSourceFile.setOverwrite( True )
        debugSourceFile.setDestPath( "/stdio/" )
        debugSourceFile.setProjectPath( "config/" + configName + "/stdio/" )
        debugSourceFile.setType( "SOURCE" )
        debugSourceFile.setDependencies( genSysSourceFile, [ "CoreSysStdioSyscallsFile", "CoreSysFiles" ] )
        debugSourceFile.setSourcePath( "../arch/arm/templates/" + compilerSelected + "/stdio/" + compilerSelected + "_monitor.c.ftl" )
        debugSourceFile.setOutputName( compilerSelected + "_monitor.c" )

    # load device specific information, clock and pin manager
    execfile( Variables.get( "__ARCH_DIR") + "/" + processor + ".py" )


def heapSizeCallBack(symbol, event):
    symbol.setValue(str(event["value"]))

def ISA_modeCallBack(symbol, event):
    if event["value"]:
       symbol.setValue("true")
    else:
        symbol.setValue("false")

def updatePath(symbol, compilerSelected):
    import re
    sourcePath = symbol.getSourcePath()
    pattern = '|'.join(str(p).lower() for p in compilers)
    sourcePath = re.sub(pattern, compilerSelected, sourcePath)
    symbol.setSourcePath(sourcePath)
    outputName = symbol.getOutputName()
    outputName = re.sub(pattern, compilerSelected, outputName)
    symbol.setOutputName(outputName)

def compilerUpdate( symbol, event ):
    global compilerSpecifics        # used in processor + ".py" modules
    global devconSystemInitFile     # set in processor + ".py" modules
    global armLibCSourceFile        # set in processor + ".py" modules
    global secarmLibCSourceFile
    global debugSourceFile          # set in core/system/console/config/sys_console.py
    global naQualifier              # warning not use; but not prohibited
    global xc32Menu
    global xc32Available
    global iarMenu
    global iarAvailable
    global processor
    global keilMenu

    compilersVisibleFlag = True

    compilerSelected = event[ "symbol" ].getSelectedKey()
    if naQualifier in compilerSelected:
        compilersVisibleFlag = False
        compilerSelected = compilerSelected.replace( naQualifier, "" )

    xc32Menu.setVisible( compilersVisibleFlag and xc32Available )
    iarMenu.setVisible(  compilersVisibleFlag and iarAvailable )
    keilMenu.setVisible(compilersVisibleFlag and keilAvailable)

    if not compilerSpecifics:
        compilerSpecifics = []
    compilerSpecifics.append( debugSourceFile )
    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
       compilerSpecifics.append( secdebugSourceFile )

    if compilerSelected == "IAR":
        xc32Menu.setVisible(False)
        keilMenu.setVisible(False)
        if devconSystemInitFile != None:
            devconSystemInitFile.setEnabled( False )
        if armLibCSourceFile != None:
            armLibCSourceFile.setEnabled( False )
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            if secarmLibCSourceFile != None:
                secarmLibCSourceFile.setEnabled( False )
    elif compilerSelected == "XC32":
        iarMenu.setVisible(False)
        keilMenu.setVisible(False)
        if devconSystemInitFile != None:
            devconSystemInitFile.setEnabled( True )
        if armLibCSourceFile != None:
            armLibCSourceFile.setEnabled( True )
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            if secarmLibCSourceFile != None:
                secarmLibCSourceFile.setEnabled( True )
    elif compilerSelected == "XCDSC":
        iarMenu.setVisible(False)
        keilMenu.setVisible(False)
        if devconSystemInitFile != None:
            devconSystemInitFile.setEnabled( True )
    elif compilerSelected == "KEIL":
        xc32Menu.setVisible(False)
        iarMenu.setVisible(False)
        if devconSystemInitFile != None:
            devconSystemInitFile.setEnabled( False )
        if armLibCSourceFile != None:
            armLibCSourceFile.setEnabled( False )
        if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
            if secarmLibCSourceFile != None:
                secarmLibCSourceFile.setEnabled( False )

    for file in compilerSpecifics:
        updatePath( file, compilerSelected.lower() )

