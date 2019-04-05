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

################################################################################
#### Register Information ####
################################################################################


################################################################################
#### Global Variables ####
################################################################################
global sdhcInstanceName
global interruptVector
global interruptHandler
global interruptHandlerLock

global interruptsChildren
interruptsChildren = ATDF.getNode('/avr-tools-device-file/devices/device/interrupts').getChildren()

################################################################################
#### Business Logic ####
################################################################################
def updateSDCDENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDWPENCommentVisibility(symbol, event):
    symbol.setVisible(event["value"])

def updateSDHCClkFreq(symbol, event):
    symbol.setValue(int(event["value"]), 2)

def _get_enblReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IECx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IEC" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def _get_statReg_parms(vectorNumber):

    # This takes in vector index for interrupt, and returns the IFSx register name as well as
    # mask and bit location within it for given interrupt
    index = int(vectorNumber / 32)
    regName = "IFS" + str(index)
    bitPosn = int(vectorNumber % 32)
    bitMask = hex(1 << bitPosn)

    return regName, str(bitPosn), str(bitMask)

def getIRQnumber(string):

    for param in interruptsChildren:
        name = param.getAttribute("name")
        if string == name:
            irq_index = param.getAttribute("index")
            break

    return irq_index

def setSDHCInterruptData(status):

    for id in interruptVector:
        Database.setSymbolValue("core", id, status, 1)

    for id in interruptHandlerLock:
        Database.setSymbolValue("core", id, status, 1)

    for id in interruptHandler:
        interruptName = id.split("_INTERRUPT_HANDLER")[0]
        if status == True:
            Database.setSymbolValue("core", id, interruptName + "_InterruptHandler", 1)
        else:
            Database.setSymbolValue("core", id, interruptName + "_Handler", 1)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(sdhcComponent):
    global interruptVector
    global interruptHandler
    global interruptHandlerLock
    global interruptVectorUpdate
    global sdhcInstanceName

    interruptVector = []
    interruptHandler = []
    interruptHandlerLock = []
    interruptVectorUpdate = []

    sdhcInstanceName = sdhcComponent.createStringSymbol("SDHC_INSTANCE_NAME", None)
    sdhcInstanceName.setVisible(False)
    sdhcInstanceName.setDefaultValue(sdhcComponent.getID().upper())
    Log.writeInfoMessage("Running " + sdhcInstanceName.getValue())

    sdhcCDSupport = sdhcComponent.createBooleanSymbol("SDCARD_SDCD_SUPPORT", None)
    sdhcCDSupport.setLabel("SDHC SDCD Support")
    sdhcCDSupport.setDefaultValue(True)
    sdhcCDSupport.setVisible(False)

    sdhcWPSupport = sdhcComponent.createBooleanSymbol("SDCARD_SDWP_SUPPORT", None)
    sdhcWPSupport.setLabel("SDHC SDWP Support")
    sdhcWPSupport.setDefaultValue(True)
    sdhcWPSupport.setVisible(False)

    sdhcCD = sdhcComponent.createBooleanSymbol("SDCARD_SDCDEN", None)
    sdhcCD.setLabel("Use SD Card Detect (SDCD#) Pin")
    sdhcCD.setDefaultValue(False)
    sdhcCD.setVisible(False)

    sdhcWP = sdhcComponent.createBooleanSymbol("SDCARD_SDWPEN", None)
    sdhcWP.setLabel("Use SD Write Protect (SDWP#) Pin")
    sdhcWP.setDefaultValue(False)
    sdhcWP.setVisible(False)

    sdhcDescLines = sdhcComponent.createIntegerSymbol("SDHC_NUM_DESCRIPTOR_LINES", None)
    sdhcDescLines.setLabel("Number of ADMA2 Descriptor Lines")
    sdhcDescLines.setMin(1)
    sdhcDescLines.setMax(10)
    sdhcDescLines.setDefaultValue(1)

    sdhcCLK = sdhcComponent.createIntegerSymbol("SDHC_CLK_FREQ", None)
    sdhcCLK.setVisible(False)
    sdhcCLK.setDefaultValue(int(Database.getSymbolValue("core", "CONFIG_SYS_CLK_PBCLK5_FREQ")))
    sdhcCLK.setDependencies(updateSDHCClkFreq, ["CONFIG_SYS_CLK_PBCLK5_FREQ", "CONFIG_SYS_CLK_REFCLK4_FREQ"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    # Initial settings for CLK and NVIC

    # EVIC Dynamic settings
    sdhcIrq = sdhcInstanceName.getValue()
    interruptVector.append(sdhcIrq + "_INTERRUPT_ENABLE")
    interruptHandler.append(sdhcIrq + "_INTERRUPT_HANDLER")
    interruptHandlerLock.append(sdhcIrq + "_INTERRUPT_HANDLER_LOCK")
    interruptVectorUpdate.append("core." + sdhcIrq + "_INTERRUPT_ENABLE_UPDATE")
    sdhcVectorNum = int(getIRQnumber(sdhcIrq))

    enblRegName, enblBitPosn, enblMask = _get_enblReg_parms(sdhcVectorNum)
    statRegName, statBitPosn, statMask = _get_statReg_parms(sdhcVectorNum)

    ## IEC REG
    sdhcIEC = sdhcComponent.createStringSymbol("SDHC_IEC_REG", None)
    sdhcIEC.setDefaultValue(enblRegName)
    sdhcIEC.setVisible(False)

    ## IEC REG MASK
    sdhcIECMask = sdhcComponent.createStringSymbol("SDHC_IEC_REG_MASK", None)
    sdhcIECMask.setDefaultValue(enblMask)
    sdhcIECMask.setVisible(False)

    ## IFS REG
    sdhcIFS = sdhcComponent.createStringSymbol("SDHC_IFS_REG", None)
    sdhcIFS.setDefaultValue(statRegName)
    sdhcIFS.setVisible(False)

    ## IFS REG MASK
    sdhcIFSMask = sdhcComponent.createStringSymbol("SDHC_IFS_REG_MASK", None)
    sdhcIFSMask.setDefaultValue(statMask)
    sdhcIFSMask.setVisible(False)


    setSDHCInterruptData(True)


    print("Loading System Services for " + Variables.get("__PROCESSOR"))
    # Dependency Status


    ############################################################################
    #### Code Generation ####
    ############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    sdhcHeaderFile = sdhcComponent.createFileSymbol("SDHC_HEADER", None)
    sdhcHeaderFile.setSourcePath("../peripheral/sdhc_00187/templates/plib_sdhc_common.h")
    sdhcHeaderFile.setOutputName("plib_sdhc_common.h")
    sdhcHeaderFile.setDestPath("peripheral/sdhc/")
    sdhcHeaderFile.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcHeaderFile.setType("HEADER")
    sdhcHeaderFile.setOverwrite(True)

    sdhcHeader1File = sdhcComponent.createFileSymbol("SDHC_HEADER1", None)
    sdhcHeader1File.setSourcePath("../peripheral/sdhc_00187/templates/plib_sdhc.h.ftl")
    sdhcHeader1File.setOutputName("plib_"+sdhcInstanceName.getValue().lower()+".h")
    sdhcHeader1File.setDestPath("peripheral/sdhc/")
    sdhcHeader1File.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcHeader1File.setType("HEADER")
    sdhcHeader1File.setOverwrite(True)
    sdhcHeader1File.setMarkup(True)

    sdhcSource1File = sdhcComponent.createFileSymbol("SDHC_SOURCE1", None)
    sdhcSource1File.setSourcePath("../peripheral/sdhc_00187/templates/plib_sdhc.c.ftl")
    sdhcSource1File.setOutputName("plib_"+sdhcInstanceName.getValue().lower()+".c")
    sdhcSource1File.setDestPath("peripheral/sdhc/")
    sdhcSource1File.setProjectPath("config/" + configName + "/peripheral/sdhc/")
    sdhcSource1File.setType("SOURCE")
    sdhcSource1File.setOverwrite(True)
    sdhcSource1File.setMarkup(True)

    sdhcSystemInitFile = sdhcComponent.createFileSymbol("SDHC_INIT", None)
    sdhcSystemInitFile.setType("STRING")
    sdhcSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    sdhcSystemInitFile.setSourcePath("../peripheral/sdhc_00187/templates/system/initialization.c.ftl")
    sdhcSystemInitFile.setMarkup(True)

    sdhcSystemDefFile = sdhcComponent.createFileSymbol("SDHC_DEF", None)
    sdhcSystemDefFile.setType("STRING")
    sdhcSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    sdhcSystemDefFile.setSourcePath("../peripheral/sdhc_00187/templates/system/definitions.h.ftl")
    sdhcSystemDefFile.setMarkup(True)
