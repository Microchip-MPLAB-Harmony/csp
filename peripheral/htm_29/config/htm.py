"""*****************************************************************************
* Copyright (C) 2022 Microchip Technology Inc. and its subsidiaries.
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


################################################################################
#### Business Logic ####
################################################################################


###################################################################################################
########################################## Callbacks  #############################################
###################################################################################################
global htmTmrInstanceNum

def calcTimeoutInSec(clk_hz, preload_val):
    global calcTimeoutInSec
    timeout_sec = float(preload_val)/(clk_hz)
    return "{:.2f}".format(timeout_sec)

def setHTMInterruptData(htm_interrupt_name, status):

    Database.setSymbolValue("core", htm_interrupt_name + "_INTERRUPT_ENABLE" , status, 1)
    Database.setSymbolValue("core", htm_interrupt_name + "_INTERRUPT_HANDLER_LOCK" , status, 1)

    if status == True:
        Database.setSymbolValue("core", htm_interrupt_name + "_INTERRUPT_HANDLER", htm_interrupt_name + "_InterruptHandler", 1)
    else:
        Database.setSymbolValue("core", htm_interrupt_name + "_INTERRUPT_HANDLER", htm_interrupt_name + "_Handler", 1)

def nvicInterruptUpdateHTMR(htmInterruptType):
    interruptNameDir = "HTMR" + htmTmrInstanceNum.getValue()
    interruptNameAgg = "HTMR" + htmTmrInstanceNum.getValue() + "_GRP"

    if htmInterruptType == "AGGREGATE":
        setHTMInterruptData(interruptNameDir, False)
        setHTMInterruptData(interruptNameAgg, True)
    else:
        setHTMInterruptData(interruptNameAgg, False)
        setHTMInterruptData(interruptNameDir, True)

def nvicInterruptUpdate(symbol, event):
    htmInterruptType = event["source"].getSymbolByID("HTM_TMR_INTERRUPT_TYPE").getSelectedKey()
    htmInterruptNameSym = event["source"].getSymbolByID("HTM_TMR_NVIC_INTERRUPT_NAME")

    nvicInterruptUpdateHTMR(htmInterruptType)
    if htmInterruptType == "AGGREGATE":
        htmInterruptNameSym.setValue("HTMR"  + htmTmrInstanceNum.getValue() + "_GRP")
    else:
        htmInterruptNameSym.setValue("HTMR"  + htmTmrInstanceNum.getValue())

def htmTimeoutUpdate(symbol, event):
    global calcTimeoutInSec
    clk_hz = 8
    tmr_resolution = event["source"].getSymbolByID("HTM_TMR_RESOLUTION").getSelectedKey()
    tmr_preload_val = event["source"].getSymbolByID("HTM_TMR_PRELOAD_VALUE").getValue()
    if tmr_resolution == "32768_HZ":
        clk_hz = 32768
    symbol.setLabel("Timeout = " + calcTimeoutInSec(clk_hz, tmr_preload_val) + " seconds")
###################################################################################################
########################################## Component  #############################################
###################################################################################################

def instantiateComponent(htmTmrComponent):

    global htmTmrInstanceName
    global htmTmrInstanceNum

    htmTmrInstanceName = htmTmrComponent.createStringSymbol("HTM_TMR_INSTANCE_NAME", None)
    htmTmrInstanceName.setVisible(False)
    htmTmrInstanceName.setDefaultValue(htmTmrComponent.getID().upper())
    Log.writeInfoMessage("Running " + htmTmrInstanceName.getValue())

    htmTmrInstanceNum = htmTmrComponent.createStringSymbol("HTM_TMR_INSTANCE_NUM", None)
    htmTmrInstanceNum.setVisible(False)
    instanceNum = filter(str.isdigit,str(htmTmrComponent.getID()))
    htmTmrInstanceNum.setDefaultValue(instanceNum)

    htmTmrReloadValue = htmTmrComponent.createIntegerSymbol("HTM_TMR_PRELOAD_VALUE", None)
    htmTmrReloadValue.setLabel("Timer Preload Value")
    htmTmrReloadValue.setMin(0)
    htmTmrReloadValue.setMax(65535)
    htmTmrReloadValue.setDefaultValue(65535)

    htmTmrResolution = htmTmrComponent.createKeyValueSetSymbol("HTM_TMR_RESOLUTION", None)
    htmTmrResolution.setLabel("Timer Resolution")
    htmTmrResolution.addKey("32768_HZ", "0", "32768 Hz")
    htmTmrResolution.addKey("8_HZ", "1", "8 Hz")
    htmTmrResolution.setDefaultValue(0)
    htmTmrResolution.setDisplayMode("Description")
    htmTmrResolution.setOutputMode("Key")

    htmTmrTimeoutComment = htmTmrComponent.createCommentSymbol("HTM_TMR_TIMEOUT_COMMENT", None)
    htmTmrTimeoutComment.setLabel("Timeout = " + calcTimeoutInSec(32768, 65535) + " seconds")
    htmTmrTimeoutComment.setDependencies(htmTimeoutUpdate, ["HTM_TMR_RESOLUTION", "HTM_TMR_PRELOAD_VALUE"])



    ## Interrupt Setup
    nvic_int_num = {}
    nvic_int_num = Database.sendMessage("core", "ECIA_GET_INT_SRC_DICT", {"int_source": "HTMR" + htmTmrInstanceNum.getValue()})

    # Interrupt type selection
    htmTmrInterruptType = htmTmrComponent.createKeyValueSetSymbol("HTM_TMR_INTERRUPT_TYPE", None)
    htmTmrInterruptType.setLabel("Interrupt Type")
    if nvic_int_num["direct_nvic_num"] != None:
        htmTmrInterruptType.addKey("DIRECT", "0", "Direct")
    if nvic_int_num["group_nvic_num"] != None:
        htmTmrInterruptType.addKey("AGGREGATE", "1", "Aggregate")
    htmTmrInterruptType.setDefaultValue(0)
    htmTmrInterruptType.setDisplayMode("Description")
    htmTmrInterruptType.setOutputMode("Key")

    # Trigger dependency when interrupt type changes
    htmTmrNVICUpdate = htmTmrComponent.createBooleanSymbol("HTM_TMR_UPDATE_NVIC_INTERRUPT", None)
    htmTmrNVICUpdate.setVisible(False)
    htmTmrNVICUpdate.setDependencies(nvicInterruptUpdate, ["HTM_TMR_INTERRUPT_TYPE"])

    # Set NVIC interrupt default value
    nvicInterruptUpdateHTMR(htmTmrInterruptType.getValue())

    interruptName = ""
    if htmTmrInterruptType.getSelectedKey() == "AGGREGATE":
        interruptName = "HTMR" + htmTmrInstanceNum.getValue() + "_GRP"
    else:
        interruptName = "HTMR" + htmTmrInstanceNum.getValue()
    htm_NVIC_InterruptName = htmTmrComponent.createStringSymbol("HTM_TMR_NVIC_INTERRUPT_NAME", None)
    htm_NVIC_InterruptName.setDefaultValue(interruptName)
    htm_NVIC_InterruptName.setVisible(False)


    ###################################################################################################
    ####################################### Code Generation  ##########################################
    ###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    # Instance Source File
    htmTmrSourceFile = htmTmrComponent.createFileSymbol("HTM_TMR_SOURCE", None)
    htmTmrSourceFile.setSourcePath("../peripheral/htm_29/templates/plib_htmr.c.ftl")
    htmTmrSourceFile.setOutputName("plib_" + htmTmrInstanceName.getValue().lower() + ".c")
    htmTmrSourceFile.setDestPath("/peripheral/htmr/")
    htmTmrSourceFile.setProjectPath("config/" + configName + "/peripheral/htmr/")
    htmTmrSourceFile.setType("SOURCE")
    htmTmrSourceFile.setMarkup(True)
    htmTmrSourceFile.setOverwrite(True)

    htmTmrHeaderFile = htmTmrComponent.createFileSymbol("HTM_TMR_COMMON_HEADER", None)
    htmTmrHeaderFile.setSourcePath("../peripheral/htm_29/templates/plib_htmr_common.h")
    htmTmrHeaderFile.setOutputName("plib_htm_common.h")
    htmTmrHeaderFile.setDestPath("peripheral/htmr/")
    htmTmrHeaderFile.setProjectPath("config/" + configName + "/peripheral/htmr/")
    htmTmrHeaderFile.setType("HEADER")
    htmTmrHeaderFile.setMarkup(False)
    htmTmrHeaderFile.setOverwrite(True)

    # Instance Header File
    htmTmrCmnHeaderFile = htmTmrComponent.createFileSymbol("HTM_TMR_HEADER1", None)
    htmTmrCmnHeaderFile.setSourcePath("../peripheral/htm_29/templates/plib_htmr.h.ftl")
    htmTmrCmnHeaderFile.setOutputName("plib_" + htmTmrInstanceName.getValue().lower() + ".h")
    htmTmrCmnHeaderFile.setDestPath("/peripheral/htmr/")
    htmTmrCmnHeaderFile.setProjectPath("config/" + configName + "/peripheral/htmr/")
    htmTmrCmnHeaderFile.setType("HEADER")
    htmTmrCmnHeaderFile.setMarkup(True)
    htmTmrCmnHeaderFile.setOverwrite(True)

    htmTmrSystemInitFile = htmTmrComponent.createFileSymbol("HTM_TMR_SYS_INT", None)
    htmTmrSystemInitFile.setType("STRING")
    htmTmrSystemInitFile.setOutputName("core.LIST_SYSTEM_INIT_C_SYS_INITIALIZE_PERIPHERALS")
    htmTmrSystemInitFile.setSourcePath("../peripheral/htm_29/templates/system/initialization.c.ftl")
    htmTmrSystemInitFile.setMarkup(True)

    htmTmrSystemDefFile = htmTmrComponent.createFileSymbol("HTM_TMR_SYS_DEF", None)
    htmTmrSystemDefFile.setType("STRING")
    htmTmrSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    htmTmrSystemDefFile.setSourcePath("../peripheral/htm_29/templates/system/definitions.h.ftl")
    htmTmrSystemDefFile.setMarkup(True)
