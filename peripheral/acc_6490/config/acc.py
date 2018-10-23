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
accRegModule = Register.getRegisterModule("ACC")
accValGrp_MR_SELMINUS = accRegModule.getValueGroup("ACC_MR__SELMINUS")
accValGrp_MR_SELPLUS = accRegModule.getValueGroup("ACC_MR__SELPLUS")
accValGrp_MR_EDGETYP = accRegModule.getValueGroup("ACC_MR__EDGETYP")
accValGrp_MR_SELFS = accRegModule.getValueGroup("ACC_MR__SELFS")
accValGrp_ACR_ISEL = accRegModule.getValueGroup("ACC_ACR__ISEL")

################################################################################
#### Global Variables ####
################################################################################
global interruptVector
global interruptHandler
global interruptHandlerLock
global accInstanceName

################################################################################
#### Business Logic ####
################################################################################
def interruptControl(symbol, event):
    Database.clearSymbolValue("core", interruptVector)
    Database.clearSymbolValue("core", interruptHandler)
    Database.clearSymbolValue("core", interruptHandlerLock)

    if (event["value"] == True):
        Database.setSymbolValue("core", interruptVector, True, 2)
        Database.setSymbolValue("core", interruptHandler, accInstanceName.getValue() + "_InterruptHandler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, True, 2)
    else :
        Database.setSymbolValue("core", interruptVector, False, 2)
        Database.setSymbolValue("core", interruptHandler, "ACC_Handler", 2)
        Database.setSymbolValue("core", interruptHandlerLock, False, 2)

def accFaultSourceSelect(symbol,event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)

################################################################################
#### Component ####
################################################################################
def instantiateComponent(accComponent):
    global accInstanceName
    global interruptVector
    global interruptHandler
    global interruptHandlerLock

    accInstanceName = accComponent.createStringSymbol("ACC_INSTANCE_NAME", None)
    accInstanceName.setVisible(False)
    accInstanceName.setDefaultValue(accComponent.getID().upper())
    print("Running " + accInstanceName.getValue())

    accSym_MR_SELPLUS = accComponent.createKeyValueSetSymbol("ACC_MR_SELPLUS", None)
    accSym_MR_SELPLUS.setLabel("Select Positive Input")
    accSym_MR_SELPLUS.setDefaultValue(0)
    accSym_MR_SELPLUS.setOutputMode("Value")
    accSym_MR_SELPLUS.setDisplayMode("Key")
    accSym_MR_SELPLUS.setVisible(True)

    count = accValGrp_MR_SELPLUS.getValueCount()
    for id in range(0, count):
        valueName = accValGrp_MR_SELPLUS.getValueNames()[id]
        accSym_MR_SELPLUS.addKey(valueName, accValGrp_MR_SELPLUS.getValue(valueName).getValue(), accValGrp_MR_SELPLUS.getValue(valueName).getDescription())

    accSym_MR_SELMINUS = accComponent.createKeyValueSetSymbol("ACC_MR_SELMINUS", None)
    accSym_MR_SELMINUS.setLabel("Select Negative Input")
    accSym_MR_SELMINUS.setDefaultValue(0)
    accSym_MR_SELMINUS.setOutputMode("Value")
    accSym_MR_SELMINUS.setDisplayMode("Key")
    accSym_MR_SELMINUS.setVisible(True)

    count = accValGrp_MR_SELMINUS.getValueCount()
    for id in range(0, count):
        valueName = accValGrp_MR_SELMINUS.getValueNames()[id]
        accSym_MR_SELMINUS.addKey(valueName, accValGrp_MR_SELMINUS.getValue(valueName).getValue(), accValGrp_MR_SELMINUS.getValue(valueName).getDescription())


    accSym_MR_INV = accComponent.createBooleanSymbol("ACC_ACR_INV", None)
    accSym_MR_INV.setLabel("Invert Comparator Output")
    accSym_MR_INV.setDefaultValue(False)


    accSym_MR_EDGETYP = accComponent.createKeyValueSetSymbol("ACC_MR_EDGETYPE", None)
    accSym_MR_EDGETYP.setLabel("Select Comparison Edge")
    accSym_MR_EDGETYP.setDefaultValue(0)
    accSym_MR_EDGETYP.setOutputMode("Value")
    accSym_MR_EDGETYP.setDisplayMode("Description")
    accSym_MR_EDGETYP.setVisible(True)


    accInterrupt = accComponent.createBooleanSymbol("INTERRUPT_MODE", None)
    accInterrupt.setLabel("Enable Comparison Edge Interrupt")
    accInterrupt.setDefaultValue(False)

    count = accValGrp_MR_EDGETYP.getValueCount()
    for id in range(0, count):
        valueName = accValGrp_MR_EDGETYP.getValueNames()[id]
        accSym_MR_EDGETYP.addKey(valueName, accValGrp_MR_EDGETYP.getValue(valueName).getValue(), accValGrp_MR_EDGETYP.getValue(valueName).getDescription())

    accSym_ACR_ISEL = accComponent.createKeyValueSetSymbol("ACC_ACR_ISEL", None)
    accSym_ACR_ISEL.setLabel("Select Current")
    accSym_ACR_ISEL.setDefaultValue(0)
    accSym_ACR_ISEL.setOutputMode("Key")
    accSym_ACR_ISEL.setDisplayMode("Description")
    accSym_ACR_ISEL.setVisible(True)

    count = accValGrp_ACR_ISEL.getValueCount()
    for id in range(0, count):
        valueName = accValGrp_ACR_ISEL.getValueNames()[id]
        accSym_ACR_ISEL.addKey(valueName, accValGrp_ACR_ISEL.getValue(valueName).getValue(),
                                                  accValGrp_ACR_ISEL.getValue(valueName).getDescription())

    accSym_ACR_HYST = accComponent.createKeyValueSetSymbol("ACC_ACR_HYST", None)
    accSym_ACR_HYST.setLabel("Select Hysteresis")
    accSym_ACR_HYST.addKey("NO_HYSTERESIS", "0", "No Hysteresis")
    accSym_ACR_HYST.addKey("MEDIUM_HYSTERESIS", "1", "Medium Hysteresis")
    accSym_ACR_HYST.addKey("HIGH_HYSTERESIS", "3", "High Hysteresis")
    accSym_ACR_HYST.setOutputMode("Value")
    accSym_ACR_HYST.setDisplayMode("Description")
    accSym_ACR_HYST.setDefaultValue(0)


    accSym_MR_FE = accComponent.createBooleanSymbol("ACC_ACR_FE", None)
    accSym_MR_FE.setLabel("Enable Fault Output")
    accSym_MR_FE.setDefaultValue(False)

    accSym_MR_SELFS = accComponent.createKeyValueSetSymbol("ACC_MR_SELFS", accSym_MR_FE)
    accSym_MR_SELFS.setLabel("Select Source for Fault Output")
    accSym_MR_SELFS.addKey("CE", "0", "Comparison Edge")
    accSym_MR_SELFS.addKey("OUTPUT", "1", "Comparator Output")
    accSym_MR_SELFS.setOutputMode("Key")
    accSym_MR_SELFS.setVisible(False)
    accSym_MR_SELFS.setDisplayMode("Description")
    accSym_MR_SELFS.setDefaultValue(0)
    accSym_MR_SELFS.setDependencies(accFaultSourceSelect, ["ACC_ACR_FE"])

    ############################################################################
    #### Dependency ####
    ############################################################################

    # Enable Peripheral Clock in Clock manager
    Database.clearSymbolValue("core", accInstanceName.getValue()+"_CLOCK_ENABLE")
    Database.setSymbolValue("core", accInstanceName.getValue()+"_CLOCK_ENABLE", True, 2)

    interruptVector = accInstanceName.getValue()+"_INTERRUPT_ENABLE"
    interruptHandler = accInstanceName.getValue()+"_INTERRUPT_HANDLER"
    interruptHandlerLock = accInstanceName.getValue()+"_INTERRUPT_HANDLER_LOCK"
    interruptVectorUpdate = accInstanceName.getValue()+"_INTERRUPT_ENABLE_UPDATE"

    # NVIC Dynamic settings
    accinterruptControl = accComponent.createBooleanSymbol("NVIC_ACC_ENABLE", None)
    accinterruptControl.setDependencies(interruptControl, ["INTERRUPT_MODE"])
    accinterruptControl.setVisible(False)

############################################################################
#### Code Generation ####
############################################################################
    configName = Variables.get("__CONFIGURATION_NAME")

    accHeaderFile = accComponent.createFileSymbol("ACC_COMMON_HEADER", None)
    accHeaderFile.setMarkup(True)
    accHeaderFile.setSourcePath("../peripheral/acc_6490/templates/plib_acc_common.h")
    accHeaderFile.setOutputName("plib_acc_common.h")
    accHeaderFile.setDestPath("peripheral/acc/")
    accHeaderFile.setProjectPath("config/" + configName + "/peripheral/acc/")
    accHeaderFile.setType("HEADER")
    accHeaderFile.setOverwrite(True)

    accHeader1File = accComponent.createFileSymbol("ACC_HEADER1", None)
    accHeader1File.setMarkup(True)
    accHeader1File.setSourcePath("../peripheral/acc_6490/templates/plib_acc.h.ftl")
    accHeader1File.setOutputName("plib_"+ accInstanceName.getValue().lower()+ ".h")
    accHeader1File.setDestPath("peripheral/acc/")
    accHeader1File.setProjectPath("config/" + configName + "/peripheral/acc/")
    accHeader1File.setType("HEADER")
    accHeader1File.setOverwrite(True)

    accSource1File = accComponent.createFileSymbol("ACC_SOURCE1", None)
    accSource1File.setMarkup(True)
    accSource1File.setSourcePath("../peripheral/acc_6490/templates/plib_acc.c.ftl")
    accSource1File.setOutputName("plib_"+accInstanceName.getValue().lower() + ".c")
    accSource1File.setDestPath("peripheral/acc/")
    accSource1File.setProjectPath("config/" + configName + "/peripheral/acc/")
    accSource1File.setType("SOURCE")
    accSource1File.setOverwrite(True)

    accSystemInitFile = accComponent.createFileSymbol("ACC_INIT", None)
    accSystemInitFile.setType("STRING")
    accSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    accSystemInitFile.setSourcePath("../peripheral/acc_6490/templates/system/system_initialize.c.ftl")
    accSystemInitFile.setMarkup(True)

    accSystemDefFile = accComponent.createFileSymbol("ACC_DEF", None)
    accSystemDefFile.setType("STRING")
    accSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    accSystemDefFile.setSourcePath("../peripheral/acc_6490/templates/system/system_definitions.h.ftl")
    accSystemDefFile.setMarkup(True)

