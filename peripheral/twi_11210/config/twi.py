
num=0

def instantiateComponent(twiComponent):

    global num
    
    num = twiComponent.getID()[-1:]
    print("Running TWI" + str(num))

    #main menu
    twiMenu = twiComponent.createMenuSymbol(None, None)
    
    twiMenu.setLabel("Hardware Settings ")

    #instance index
    twiIndex = twiComponent.createIntegerSymbol("INDEX", twiMenu)
    
    twiIndex.setVisible(False)
    twiIndex.setDefaultValue(int(num))

    #operation mode
    opModeValues = ["MASTER"]
    
    twiOpMode = twiComponent.createComboSymbol("TWI_OPMODE", twiMenu, opModeValues)
    
    twiOpMode.setLabel("TWI Operation Mode")
    twiOpMode.setDefaultValue("MASTER")
    
    #Number of Transaction request blocks
    twiNumTRBs = twiComponent.createIntegerSymbol("TWI_NUM_TRBS", twiMenu)
    
    twiNumTRBs.setLabel("Number of TRB's")
    twiNumTRBs.setDefaultValue(1)
    twiNumTRBs.setMax(255)

    #Clock speed
    twiSymClockSpeed = twiComponent.createIntegerSymbol("TWI_CLK_SPEED", twiMenu)
    
    twiSymClockSpeed.setLabel("Clock Speed")
    twiSymClockSpeed.setDefaultValue(400000)
    twiSymClockSpeed.setMax(400000)

    cldiv, chdiv, ckdiv = getTWIClockDividerValue(twiSymClockSpeed.getValue())
    
    #Clock Divider
    twiSymDivider = twiComponent.createStringSymbol("TWI_DIVIDER", twiMenu)
    
    twiSymDivider.setVisible(False)
    twiSymDivider.setDependencies(setClockDividerValue, ["TWI_CLK_SPEED", "core.MASTERCLK_FREQ"])
    
    #CLDIV
    twiSym_CWGR_CLDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CLDIV", twiMenu)
    
    twiSym_CWGR_CLDIV.setVisible(False)
    twiSym_CWGR_CLDIV.setValue(cldiv, 1)
    
    #CHDIV
    twiSym_CWGR_CHDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CHDIV", twiMenu)
    
    twiSym_CWGR_CHDIV.setVisible(False)
    twiSym_CWGR_CHDIV.setValue(chdiv, 1)
    
    #CKDIV
    twiSym_CWGR_CKDIV = twiComponent.createIntegerSymbol("TWI_CWGR_CKDIV", twiMenu)
    
    twiSym_CWGR_CKDIV.setVisible(False)
    twiSym_CWGR_CKDIV.setValue(ckdiv, 1)
    
    # Initialize peripheral clock
    Database.clearSymbolValue("core", "PMC_ID_TWI" + str(num))
    Database.setSymbolValue("core", "PMC_ID_TWI" + str(num), True, 1)
    
    # get peripheral id for TWI
    peripId = Interrupt.getInterruptIndex("TWI" + str(num))
    
    # Initialize peripheral Interrupt
    Database.clearSymbolValue("core", "NVIC_" + str(peripId) + "_ENABLE")
    Database.setSymbolValue("core", "NVIC_" + str(peripId) + "_ENABLE", True, 1)
    
    # Set Interrupt Handler Name
    Database.clearSymbolValue("core", "NVIC_" + str(peripId) + "_HANDLER")
    Database.setSymbolValue("core", "NVIC_" + str(peripId) + "_HANDLER", "TWI" + str(num) + "_InterruptHandler", 1)
    
    # Master Clock Frequency
    twiSymMasterClkFreq = twiComponent.createStringSymbol("TWI_CLK_SRC_FREQ", twiMenu)
    twiSymMasterClkFreq.setVisible(False)
    twiSymMasterClkFreq.setDefaultValue(Database.getSymbolValue("core","MASTERCLK_FREQ"))
    twiSymMasterClkFreq.setDependencies(setClockSourceFreq, ["core.MASTERCLK_FREQ"])
    
    # Warning for change in Clock Enable Symbol
    twiSymClkEnComment = twiComponent.createCommentSymbol("TWI_CLK_EN_COMMENT", twiMenu)
    twiSymClkEnComment.setVisible(False)
    twiSymClkEnComment.setLabel("Warning!!! TWI Peripheral Clock is Disabled in Clock Manager")
    twiSymClkEnComment.setDependencies(setEnCommentVisibility, ["core.PMC_ID_TWI" + str(num)])
    
    # Warning for change in Interrupt Enable Symbol
    twiSymIntEnComment = twiComponent.createCommentSymbol("TWI_INT_EN_COMMENT", twiMenu)
    twiSymIntEnComment.setVisible(False)
    twiSymIntEnComment.setLabel("Warning!!! TWI Interrupt is Disabled in Interrupt Manager")
    twiSymIntEnComment.setDependencies(setEnCommentVisibility, ["core.NVIC_" + str(peripId) + "_ENABLE"])
    
    REG_MODULE_TWI = Register.getRegisterModule("TWI")
    
    configName = Variables.get("__CONFIGURATION_NAME")
    
    #Master Header
    twiMasterHeaderFile = twiComponent.createFileSymbol(None, None)
    
    twiMasterHeaderFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/plib_twi_master.h")
    twiMasterHeaderFile.setOutputName("plib_twi_master.h")
    twiMasterHeaderFile.setDestPath("/peripheral/twi/")
    twiMasterHeaderFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiMasterHeaderFile.setType("HEADER")

    #Source File
    twiMainSourceFile = twiComponent.createFileSymbol(None, None)
    
    twiMainSourceFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/plib_twi.c.ftl")
    twiMainSourceFile.setOutputName("plib_twi" + str(num) + ".c")
    twiMainSourceFile.setDestPath("/peripheral/twi/")
    twiMainSourceFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiMainSourceFile.setType("SOURCE")
    twiMainSourceFile.setMarkup(True)
    
    #Instance Header File
    twiInstHeaderFile = twiComponent.createFileSymbol(None, None)
    
    twiInstHeaderFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/plib_twi.h.ftl")
    twiInstHeaderFile.setOutputName("plib_twi" + str(num) + ".h")
    twiInstHeaderFile.setDestPath("/peripheral/twi/")
    twiInstHeaderFile.setProjectPath("config/" + configName + "/peripheral/twi/")
    twiInstHeaderFile.setType("HEADER")
    twiInstHeaderFile.setMarkup(True)
    
    #TWI Initialize 
    twiSystemInitFile = twiComponent.createFileSymbol(None, None)
    
    twiSystemInitFile.setType("STRING")
    twiSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_DEPENDENT_DRIVERS")
    twiSystemInitFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/system/system_initialize.c.ftl")
    twiSystemInitFile.setMarkup(True)

    #TWI definitions header
    twiSystemDefFile = twiComponent.createFileSymbol(None, None)
    
    twiSystemDefFile.setType("STRING")
    twiSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    twiSystemDefFile.setSourcePath("../peripheral/twi_" + REG_MODULE_TWI.getID() + "/templates/system/system_definitions.h.ftl")
    twiSystemDefFile.setMarkup(True)
    
def getMasterClockFreq():
    return int(Database.getSymbolValue("core", "MASTERCLK_FREQ"))
        
def getTWIClkSpeed():
    global num
    return Database.getSymbolValue('twi' + str(num), "TWI_CLK_SPEED")

def getTWILowLevelTimeLimit( ):
    return 384000

def getTWIClockDividerMaxValue( ):
    return 255

def getTWIClockDividerMinValue( ):
    return 7
        
def getTWIClockDividerValue( twiClkSpeed ):

    cldiv = 0 
    chdiv = 0
    ckdiv = 0
    
    masterClockFreq = getMasterClockFreq( )

    if twiClkSpeed > getTWILowLevelTimeLimit():
        cldiv = masterClockFreq // ( getTWILowLevelTimeLimit() * 2) - 3
        chdiv = masterClockFreq // ((twiClkSpeed + (twiClkSpeed - getTWILowLevelTimeLimit())) * 2 ) - 3

        while cldiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        while chdiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
            ckdiv += 1
            chdiv //= 2
    else:
        cldiv = masterClockFreq / ( twiClkSpeed * 2 ) - 3

        while cldiv > getTWIClockDividerMaxValue() and ckdiv < getTWIClockDividerMinValue():
            ckdiv += 1
            cldiv //= 2

        chdiv = cldiv

    return cldiv, chdiv, ckdiv
                        
def setClockDividerValue( twiSymDivider, event):
    
    global num
    cldiv, chdiv, ckdiv = getTWIClockDividerValue( getTWIClkSpeed( ) )
    
    # set CLDIV Value
    Database.setSymbolValue("twi" + str(num), "TWI_CWGR_CLDIV", cldiv, 1)

    # set CHDIV Value
    Database.setSymbolValue("twi" + str(num), "TWI_CWGR_CHDIV", chdiv, 1)
    
    # set CKDIV Value
    Database.setSymbolValue("twi" + str(num), "TWI_CWGR_CKDIV", ckdiv, 1)
    
def setEnCommentVisibility( twiSymComment, event ):
    if event["value"] is False:
        twiSymComment.setVisible(True)
    else:
        twiSymComment.setVisible(False)
        
def setClockSourceFreq( twiSymClockFreq, event ):
    masterClockFreq = Database.getSymbolValue("core", "MASTERCLK_FREQ")
    twiSymClockFreq.setValue(masterClockFreq, 1)

'''********************************End of the file*************************'''
    
