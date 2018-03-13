from math import ceil

################################################################################
#### Global Variables ####
################################################################################
global NVICVector
global NVICHandler
global instance
global peripId


################################################################################
#### Business Logic ####
################################################################################
#-----------------------------------------------------------------------------------------------------------------------

def calcExtResetAssertTime(symbol,event):
    numSlck=2**(event["value"]+1)
    time= float(numSlck)/32768
    timeUsInt=int(time*1e6)
    timeMs=float(timeUsInt)/1000   
    symbol.setLabel("External Reset Assertion Time is: " + str(timeMs) + " ms ( "+str(numSlck)+" SLCK Cycles )")

def NVICControl(symbol, event):
    symObj=event["symbol"]
    
    Database.clearSymbolValue("core", NVICVector)
    Database.clearSymbolValue("core", NVICHandler)
  
    if (symObj.getSelectedKey() == "INTERRUPT"):
        Database.setSymbolValue("core", NVICVector, True, 2)
        Database.setSymbolValue("core", NVICHandler, "RSTC" + str(instance) +  "_InterruptHandler", 2)
    else:
        Database.setSymbolValue("core", NVICVector, False, 2)
        Database.setSymbolValue("core", NVICHandler, "RSTC" + str(instance) +  "_Handler", 2)   

################################################################################
#### Component ####
################################################################################
def instantiateComponent(rstcComponent):

    global NVICVector
    global NVICHandler
    global instance
    global peripId

    instance = rstcComponent.getID()[-1:]
    print("Running RSTC" + str(instance))

    rstcIndex = rstcComponent.createIntegerSymbol("INDEX", None)
    rstcIndex.setVisible(False)
    rstcIndex.setDefaultValue(int(instance))

    rstcSym_MR_UserReset = rstcComponent.createKeyValueSetSymbol("RSTC_MR_URSTEN", None)
    rstcSym_MR_UserReset.setLabel("External Reset (NRST) Pin Usage")
    rstcSym_MR_UserReset.addKey("RESET", "0", "Generate Reset")
    rstcSym_MR_UserReset.addKey("INTERRUPT", "1", "Generate Interrupt")
    rstcSym_MR_UserReset.addKey("GPIO", "2", "Use as a GPIO")
    rstcSym_MR_UserReset.setOutputMode("Key")
    rstcSym_MR_UserReset.setDisplayMode("Description")
    rstcSym_MR_UserReset.setSelectedKey("User Reset",1)
                                 
    rstcSym_MR_ERSTL = rstcComponent.createIntegerSymbol("RSTC_MR_ERSTL", None)
    rstcSym_MR_ERSTL.setLabel("External Reset Assertion duration on WDT/SW Reset")
    rstcSym_MR_ERSTL.setMin(0)
    rstcSym_MR_ERSTL.setMax(15)
    # Default value is set later to trigger business logic for the first time

    extResetAssertTimeMessage = rstcComponent.createCommentSymbol("EXT_RESET_LENGTH_MESSAGE", None)
    extResetAssertTimeMessage.setVisible(True)
    extResetAssertTimeMessage.setLabel("External Reset Assertion Time is: 0.061 ms ( 2 SLCK Cycles )")
    extResetAssertTimeMessage.setDependencies(calcExtResetAssertTime, ["RSTC_MR_ERSTL"])    

    rstcSym_MR_ERSTL.setDefaultValue(0)

    

    ############################################################################
    #### Dependency ####
    ############################################################################
    
    # Setup Peripheral Interrupt in Interrupt manager
    peripId = Interrupt.getInterruptIndex("RSTC")
    NVICVector = "NVIC_" + str(peripId) + "_ENABLE"
    NVICHandler = "NVIC_" + str(peripId) + "_HANDLER"
    NVICHandlerLock = "NVIC_" + str(peripId) + "_HANDLER_LOCK"
      
    # NVIC Dynamic settings
    rstcNVICControl = rstcComponent.createBooleanSymbol("NVIC_RSTC_ENABLE", None)
    rstcNVICControl.setDependencies(NVICControl, ["RSTC_MR_URSTEN"])
    rstcNVICControl.setVisible(False)
    
############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rstcHeader1File = rstcComponent.createFileSymbol("RSTC_HEADER1", None)
    rstcHeader1File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc.h")
    rstcHeader1File.setOutputName("plib_rstc.h")
    rstcHeader1File.setDestPath("peripheral/rstc/")
    rstcHeader1File.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcHeader1File.setType("HEADER")
    rstcHeader1File.setOverwrite(True)  
    
    rstcHeader2File = rstcComponent.createFileSymbol("RSTC_HEADER2", None)
    rstcHeader2File.setMarkup(True)    
    rstcHeader2File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc.h.ftl")
    rstcHeader2File.setOutputName("plib_rstc" + str(instance) + ".h")
    rstcHeader2File.setDestPath("peripheral/rstc/")
    rstcHeader2File.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcHeader2File.setType("HEADER")
    rstcHeader2File.setOverwrite(True)

    rstcSource1File = rstcComponent.createFileSymbol("RSTC_SOURCE1", None)
    rstcSource1File.setMarkup(True)    
    rstcSource1File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc.c.ftl")
    rstcSource1File.setOutputName("plib_rstc" + str(instance) + ".c")
    rstcSource1File.setDestPath("peripheral/rstc/")
    rstcSource1File.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcSource1File.setType("SOURCE")
    rstcSource1File.setOverwrite(True)
    
    rstcSystemInitFile = rstcComponent.createFileSymbol("RSTC_INIT", None)
    rstcSystemInitFile.setType("STRING")
    rstcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    rstcSystemInitFile.setSourcePath("../peripheral/rstc_11009/templates/system/system_initialize.c.ftl")
    rstcSystemInitFile.setMarkup(True)

    rstcSystemDefFile = rstcComponent.createFileSymbol("RSTC_DEF", None)
    rstcSystemDefFile.setType("STRING")
    rstcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    rstcSystemDefFile.setSourcePath("../peripheral/rstc_11009/templates/system/system_definitions.h.ftl")
    rstcSystemDefFile.setMarkup(True)
    
    