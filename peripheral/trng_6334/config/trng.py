#Function for initiating the UI
global interruptVector
global interruptHandler
global trngInstanceName
global interruptHandlerLock

def interruptControl(NVIC, event):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)
    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, trngInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "TRNG_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def instantiateComponent(trngComponent):
    global interruptVector
    global interruptHandler
    global trngInstanceName
    global interruptHandlerLock

    trngInstanceName = trngComponent.createStringSymbol("TRNG_INSTANCE_NAME", None)
    trngInstanceName.setVisible(False)
    trngInstanceName.setDefaultValue(trngComponent.getID().upper())
    Log.writeInfoMessage("Running " + trngInstanceName.getValue())

    interruptVector = trngInstanceName.getValue() + "_INTERRUPT_ENABLE"
    interruptHandler = trngInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = trngInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = trngInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"


    trngReserved = trngComponent.createBooleanSymbol("TRNG_Reserved", None)
    trngReserved.setLabel("TRNG Reserved")
    trngReserved.setVisible(False)

    trngWarning = trngComponent.createCommentSymbol("TRNG_COMMENT", None)
    trngWarning.setLabel("**** Warning: This module is used and configured by Crypto Library ****")
    trngWarning.setDependencies(showWarning, ["TRNG_Reserved"])
    trngWarning.setVisible(False)

    #Create the top menu
    trngMenu = trngComponent.createMenuSymbol("TRNG_MENU_0", None)
    trngMenu.setLabel("Hardware Settings ")
    trngMenu.setDependencies(showMenu, ["TRNG_Reserved"])

    #Create a Checkbox to enable disable interrupts
    trngInterrupt = trngComponent.createBooleanSymbol("trngEnableInterrupt", trngMenu)
    trngInterrupt.setLabel("Enable Interrupts")
    trngInterrupt.setDefaultValue(False)

    # Initial settings for CLK and NVIC
    Database.clearSymbolValue("core", trngInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", trngInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    # NVIC Dynamic settings
    trnginterruptControl = trngComponent.createBooleanSymbol("NVIC_TRNG_ENABLE", None)
    trnginterruptControl.setDependencies(interruptControl, ["trngEnableInterrupt"])
    trnginterruptControl.setVisible(False)

    configName = Variables.get("__CONFIGURATION_NAME")

    #Generate Output Header
    trngHeaderFile = trngComponent.createFileSymbol("TRNG_FILE_0", None)
    trngHeaderFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.h.ftl")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOutputName("plib_"+trngInstanceName.getValue().lower()+".h")
    trngHeaderFile.setMarkup(True)
    trngHeaderFile.setOverwrite(True)
    trngHeaderFile.setDestPath("peripheral/trng/")
    trngHeaderFile.setProjectPath("config/" + configName + "/peripheral/trng/")
    trngHeaderFile.setType("HEADER")
    #Generate Output source

    trngSourceFile = trngComponent.createFileSymbol("TRNG_FILE_1", None)
    trngSourceFile.setSourcePath("../peripheral/trng_6334/templates/plib_trng.c.ftl")
    trngSourceFile.setMarkup(True)
    trngSourceFile.setOutputName("plib_"+trngInstanceName.getValue().lower()+".c")
    trngSourceFile.setMarkup(True)
    trngSourceFile.setOverwrite(True)
    trngSourceFile.setDestPath("peripheral/trng/")
    trngSourceFile.setProjectPath("config/" + configName + "/peripheral/trng/")
    trngSourceFile.setType("SOURCE")

    trngSystemDefFile = trngComponent.createFileSymbol("TRNG_FILE_2", None)
    trngSystemDefFile.setType("STRING")
    trngSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    trngSystemDefFile.setSourcePath("../peripheral/trng_6334/templates/system/system_definitions.h.ftl")
    trngSystemDefFile.setMarkup(True)

def showWarning(trngWarning, event):
    trngWarning.setVisible(event["value"])

def showMenu(trngMenu, event):
    trngMenu.setVisible(not event["value"])
