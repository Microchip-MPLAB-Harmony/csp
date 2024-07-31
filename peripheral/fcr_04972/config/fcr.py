"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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

global fcrInstanceName
global fcrfilesArray
fcrfilesArray = []

def waitStateUpdateCalc():
    global waitStates
    waitState = 6
    cpuFreq = Database.getSymbolValue("core", "CPU_CLOCK_FREQUENCY")
    for key in sorted(waitStates.keys()):
        if int(cpuFreq) <= int(key):
            waitState = waitStates.get(key)
            break
    return waitState

def waitStateUpdate(symbol, event):
    if event["id"] == "FCR_AUTOWS":
        symbol.setVisible(not(event["value"]))
    else:
        symbol.setValue(waitStateUpdateCalc())

def fcrSecurityUpdate(symbol, event):
    global fcrfilesArray
    global fcrInstanceName

    if event["value"] == False:
        fcrfilesArray[0].setSecurity("SECURE")
        fcrfilesArray[1].setSecurity("SECURE")
        fcrfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")
        fcrfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")
        Database.setSymbolValue("core", fcrInstanceName.getValue() + "_SET_NON_SECURE", False)

    else:
        fcrfilesArray[0].setSecurity("NON_SECURE")
        fcrfilesArray[1].setSecurity("NON_SECURE")
        fcrfilesArray[2].setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
        fcrfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
        Database.setSymbolValue("core", fcrInstanceName.getValue() + "_SET_NON_SECURE", True)
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(fcrComponent):

    global waitStates
    global fcrInstanceName
    global fcrfilesArray
    
    waitStates = {}
    waitStates = Database.sendMessage("core", "WAIT_STATES", waitStates)

    fcrInstanceName = fcrComponent.createStringSymbol("FCR_INSTANCE_NAME", None)
    fcrInstanceName.setVisible(False)
    fcrInstanceName.setDefaultValue(fcrComponent.getID().upper())
    Log.writeInfoMessage("Running " + fcrInstanceName.getValue())

    nvm_autows = fcrComponent.createBooleanSymbol("FCR_AUTOWS", None)
    nvm_autows.setLabel("Automatic Wait State Enable")
    nvm_autows.setDescription("If enabled, Total flash wait states = ADRWS + (Tacc + 5ns + 2 clocks); if disabled, Total flash wait states = ADRWS + FWS")
    nvm_autows.setDefaultValue(True)

    # Flash Read Wait State (RWS).
    nvm_rws = fcrComponent.createIntegerSymbol("FCR_FWS", None)
    nvm_rws.setLabel("Wait States (FWS)")
    nvm_rws.setDefaultValue(waitStateUpdateCalc())
    nvm_rws.setMin(0)
    nvm_rws.setMax(15)
    nvm_rws.setVisible(False)
    nvm_rws.setDependencies(waitStateUpdate, ["core.CPU_CLOCK_FREQUENCY", "FCR_AUTOWS"])

    nvm_adrws = fcrComponent.createBooleanSymbol("FCR_ADRWS", None)
    nvm_adrws.setLabel("Address Wait State Enable")
    nvm_adrws.setDescription("Enabling address wait state allows to use higher clock frequencies, whereas disabling it allow for higher performance at lower clock frequencies")
    nvm_adrws.setDefaultValue(False)
    
    nvm_crc = fcrComponent.createBooleanSymbol("FCR_CRC", None)
    nvm_crc.setLabel("CRC Enable")
    nvm_crc.setDescription("Enabling CRC allows CRC calculation")
    nvm_crc.setDefaultValue(True)
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    fcrSym_HeaderFile = fcrComponent.createFileSymbol("FCR_HEADER", None)
    fcrSym_HeaderFile.setSourcePath("../peripheral/fcr_04972/templates/plib_fcr.h.ftl")
    fcrSym_HeaderFile.setOutputName("plib_"+fcrInstanceName.getValue().lower()+".h")
    fcrSym_HeaderFile.setDestPath("/peripheral/fcr/")
    fcrSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/fcr/")
    fcrSym_HeaderFile.setType("HEADER")
    fcrSym_HeaderFile.setMarkup(True)

    fcrSym_SourceFile = fcrComponent.createFileSymbol("FCR_SOURCE", None)
    fcrSym_SourceFile.setSourcePath("../peripheral/fcr_04972/templates/plib_fcr.c.ftl")
    fcrSym_SourceFile.setOutputName("plib_"+fcrInstanceName.getValue().lower()+".c")
    fcrSym_SourceFile.setDestPath("/peripheral/fcr/")
    fcrSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/fcr/")
    fcrSym_SourceFile.setType("SOURCE")
    fcrSym_SourceFile.setMarkup(True)
    
    fcrSystemDefFile = fcrComponent.createFileSymbol("FCR_SYS_DEF", None)
    fcrSystemDefFile.setSourcePath("../peripheral/fcr_04972/templates/system/definitions.h.ftl")
    fcrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    fcrSystemDefFile.setType("STRING")
    fcrSystemDefFile.setMarkup(True)

    fcrSystemInitFile = fcrComponent.createFileSymbol("FCR_SYS_INIT", None)
    fcrSystemInitFile.setSourcePath("../peripheral/fcr_04972/templates/system/initialization.c.ftl")
    fcrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    fcrSystemInitFile.setType("STRING")
    fcrSystemInitFile.setMarkup(True)
    
    fcrSystemInitFile_ws = fcrComponent.createFileSymbol("FCR_SYS_INIT_0", None)
    fcrSystemInitFile_ws.setSourcePath("../peripheral/fcr_04972/templates/system/fcr_waitstate.h.ftl")
    fcrSystemInitFile_ws.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    fcrSystemInitFile_ws.setType("STRING")
    fcrSystemInitFile_ws.setMarkup(True)

    if Variables.get("__TRUSTZONE_ENABLED") != None and Variables.get("__TRUSTZONE_ENABLED") == "true":
        fcrIsNonSecure = Database.getSymbolValue("core", fcrInstanceName.getValue() + "_IS_NON_SECURE")
        fcrSystemDefFile.setDependencies(fcrSecurityUpdate, ["core." + fcrInstanceName.getValue() + "_IS_NON_SECURE"])
        
        fcrSystemInitFile_ws.setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")
        fcrfilesArray.append(fcrSym_SourceFile)
        fcrfilesArray.append(fcrSym_HeaderFile)
        fcrfilesArray.append(fcrSystemInitFile)
        fcrfilesArray.append(fcrSystemDefFile)
        #Set interrupt security
        Database.setSymbolValue("core", fcrInstanceName.getValue() + "_SET_NON_SECURE", fcrIsNonSecure)
        
        if fcrIsNonSecure == False:
            fcrfilesArray[0].setSecurity("SECURE")
            fcrfilesArray[1].setSecurity("SECURE")
            fcrfilesArray[2].setOutputName("core.LIST_SYSTEM_SECURE_INIT_C_SYS_INITIALIZE_START")
            fcrfilesArray[3].setOutputName("core.LIST_SYSTEM_DEFINITIONS_SECURE_H_INCLUDES")