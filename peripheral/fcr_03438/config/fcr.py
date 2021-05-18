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

###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(fcrComponent):

    global waitStates
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
    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    fcrSym_HeaderFile = fcrComponent.createFileSymbol("FCR_HEADER", None)
    fcrSym_HeaderFile.setSourcePath("../peripheral/fcr_03438/templates/plib_fcr.h.ftl")
    fcrSym_HeaderFile.setOutputName("plib_"+fcrInstanceName.getValue().lower()+".h")
    fcrSym_HeaderFile.setDestPath("/peripheral/fcr/")
    fcrSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/fcr/")
    fcrSym_HeaderFile.setType("HEADER")
    fcrSym_HeaderFile.setMarkup(True)

    fcrSym_SourceFile = fcrComponent.createFileSymbol("FCR_SOURCE", None)
    fcrSym_SourceFile.setSourcePath("../peripheral/fcr_03438/templates/plib_fcr.c.ftl")
    fcrSym_SourceFile.setOutputName("plib_"+fcrInstanceName.getValue().lower()+".c")
    fcrSym_SourceFile.setDestPath("/peripheral/fcr/")
    fcrSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/fcr/")
    fcrSym_SourceFile.setType("SOURCE")
    fcrSym_SourceFile.setMarkup(True)
    
# for PIC32CZ-CA family of device, auto waitstate is set by default, so no need of setting through this code
    #fcrSym_SystemInitFile1 = fcrComponent.createFileSymbol("FCR_SYS_INIT_0", None)
    #fcrSym_SystemInitFile1.setSourcePath("../peripheral/fcr_03438/templates/system/fcr_waitstate.h.ftl")
    #fcrSym_SystemInitFile1.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_START")
    #fcrSym_SystemInitFile1.setType("STRING")
    #fcrSym_SystemInitFile1.setMarkup(True)
    
    fcrSystemDefFile = fcrComponent.createFileSymbol("FCR_SYS_DEF", None)
    fcrSystemDefFile.setSourcePath("../peripheral/fcr_03438/templates/system/definitions.h.ftl")
    fcrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    fcrSystemDefFile.setType("STRING")
    fcrSystemDefFile.setMarkup(True)

    fcrSystemInitFile = fcrComponent.createFileSymbol("FCR_SYS_INIT", None)
    fcrSystemInitFile.setSourcePath("../peripheral/fcr_03438/templates/system/initialization.c.ftl")
    fcrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    fcrSystemInitFile.setType("STRING")
    fcrSystemInitFile.setMarkup(True)
