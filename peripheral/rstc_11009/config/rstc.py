# coding: utf-8
"""*****************************************************************************
* © 2018 Microchip Technology Inc. and its subsidiaries.
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

from math import ceil

################################################################################
#### Global Variables ####
################################################################################
global interruptVector
global interruptHandler
global interruptHandlerLock
global rstcInstanceName


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

def interruptControl(symbol, event):
    symObj=event["symbol"]

    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (symObj.getSelectedKey() == "INTERRUPT"):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, rstcInstanceName.getValue()+ "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else:
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "RSTC_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(rstcComponent):

    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global rstcInstanceName

    rstcInstanceName = rstcComponent.createStringSymbol("RSTC_INSTANCE_NAME", None)
    rstcInstanceName.setVisible(False)
    rstcInstanceName.setDefaultValue(rstcComponent.getID().upper())
    print("Running " + rstcInstanceName.getValue())

    rstcSym_MR_UserReset = rstcComponent.createKeyValueSetSymbol("RSTC_MR_URSTEN", None)
    rstcSym_MR_UserReset.setLabel("External Reset (NRST) Pin Usage")
    rstcSym_MR_UserReset.addKey("RESET", "0", "Generate Reset")
    rstcSym_MR_UserReset.addKey("INTERRUPT", "1", "Generate Interrupt")
    rstcSym_MR_UserReset.addKey("GPIO", "2", "Use as a GPIO")
    rstcSym_MR_UserReset.setOutputMode("Key")
    rstcSym_MR_UserReset.setDisplayMode("Description")
    rstcSym_MR_UserReset.setSelectedKey("RESET",1)

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

    interruptVector = rstcInstanceName.getValue()+"_INTERRUPT_ENABLE"
    interruptHandler = rstcInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = rstcInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = rstcInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    rstcinterruptControl = rstcComponent.createBooleanSymbol("NVIC_RSTC_ENABLE", None)
    rstcinterruptControl.setDependencies(interruptControl, ["RSTC_MR_URSTEN"])
    rstcinterruptControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    rstcHeader1File = rstcComponent.createFileSymbol("RSTC_HEADER1", None)
    rstcHeader1File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc_common.h")
    rstcHeader1File.setOutputName("plib_rstc_common.h")
    rstcHeader1File.setDestPath("/peripheral/rstc/")
    rstcHeader1File.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcHeader1File.setType("HEADER")
    rstcHeader1File.setOverwrite(True)

    rstcHeader2File = rstcComponent.createFileSymbol("RSTC_HEADER2", None)
    rstcHeader2File.setMarkup(True)
    rstcHeader2File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc.h.ftl")
    rstcHeader2File.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".h")
    rstcHeader2File.setDestPath("/peripheral/rstc/")
    rstcHeader2File.setProjectPath("config/" + configName + "/peripheral/rstc/")
    rstcHeader2File.setType("HEADER")
    rstcHeader2File.setOverwrite(True)

    rstcSource1File = rstcComponent.createFileSymbol("RSTC_SOURCE1", None)
    rstcSource1File.setMarkup(True)
    rstcSource1File.setSourcePath("../peripheral/rstc_11009/templates/plib_rstc.c.ftl")
    rstcSource1File.setOutputName("plib_"+rstcInstanceName.getValue().lower()+".c")
    rstcSource1File.setDestPath("/peripheral/rstc/")
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

