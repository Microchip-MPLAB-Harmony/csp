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

global nvmInstanceName

###################################################################################################
########################################## Component  #############################################
###################################################################################################
def instantiateComponent(nvmComponent):

    global nvmInstanceName

    nvmInstanceName = nvmComponent.createStringSymbol("NVM_INSTANCE_NAME", None)
    nvmInstanceName.setVisible(False)
    nvmInstanceName.setDefaultValue(nvmComponent.getID().upper())
    Log.writeInfoMessage("Running " + nvmInstanceName.getValue())

    #Flash Address
    nvmFlashNode = ATDF.getNode("/avr-tools-device-file/devices/device/address-spaces/address-space/memory-segment@[name=\"code\"]")
    nvmSym_FLASH_ADDRESS = nvmComponent.createStringSymbol("FLASH_START_ADDRESS", None)
    nvmSym_FLASH_ADDRESS.setVisible(False)
    nvmSym_FLASH_ADDRESS.setDefaultValue(nvmFlashNode.getAttribute("start"))

    #Flash size
    nvmSym_FLASH_SIZE = nvmComponent.createStringSymbol("FLASH_SIZE", None)
    nvmSym_FLASH_SIZE.setVisible(False)
    nvmSym_FLASH_SIZE.setDefaultValue(nvmFlashNode.getAttribute("size"))

###################################################################################################
####################################### Code Generation  ##########################################
###################################################################################################

    configName = Variables.get("__CONFIGURATION_NAME")

    nvmSym_HeaderFile = nvmComponent.createFileSymbol("NVM_HEADER", None)
    nvmSym_HeaderFile.setSourcePath("../peripheral/nvm_02819/templates/plib_nvm.h.ftl")
    nvmSym_HeaderFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".h")
    nvmSym_HeaderFile.setDestPath("/peripheral/nvm/")
    nvmSym_HeaderFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_HeaderFile.setType("HEADER")
    nvmSym_HeaderFile.setMarkup(True)

    nvmSym_SourceFile = nvmComponent.createFileSymbol("NVM_SOURCE", None)
    nvmSym_SourceFile.setSourcePath("../peripheral/nvm_02819/templates/plib_nvm.c.ftl")
    nvmSym_SourceFile.setOutputName("plib_"+nvmInstanceName.getValue().lower()+".c")
    nvmSym_SourceFile.setDestPath("/peripheral/nvm/")
    nvmSym_SourceFile.setProjectPath("config/" + configName + "/peripheral/nvm/")
    nvmSym_SourceFile.setType("SOURCE")
    nvmSym_SourceFile.setMarkup(True)

    nvmSystemDefFile = nvmComponent.createFileSymbol("NVM_SYS_DEF", None)
    nvmSystemDefFile.setSourcePath("../peripheral/nvm_02819/templates/system/definitions.h.ftl")
    nvmSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    nvmSystemDefFile.setType("STRING")
    nvmSystemDefFile.setMarkup(True)
