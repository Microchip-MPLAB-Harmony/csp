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
dmtReg_DMTPRECLR_STEP1  = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMT"]/register-group@[name="DMT"]/register@[name="DMTPRECLR"]/bitfield@[name="STEP1"]')
dmtReg_DMTCLR_STEP2     = ATDF.getNode('/avr-tools-device-file/modules/module@[name="DMT"]/register-group@[name="DMT"]/register@[name="DMTCLR"]/bitfield@[name="STEP2"]')

################################################################################
#### Business Logic ####
################################################################################
global _get_position
def _get_position(maskval):
    # finds the least significant bit position of maskval
    if(maskval.find('0x')!=-1):
        value = maskval[2:]
    else:
        value = maskval
    for ii in range(0,31):
        if(int(value,16) & (1<<ii)):
            break
    return ii

def instantiateComponent(dmtComponent):
    ################################################################################
    #### Symbols in ftl code ####
    ################################################################################
    # DMTPRECLR register name
    dmtPreclrSym = dmtComponent.createStringSymbol("DMTSTEP1_REG",None)
    dmtPreclrSym.setDefaultValue('DMTPRECLR')
    dmtPreclrSym.setVisible(False)
    
    #DMTCLR register name
    dmtClrSym = dmtComponent.createStringSymbol("DMTSTEP2_REG",None)
    dmtClrSym.setDefaultValue('DMTCLR')
    dmtClrSym.setVisible(False)
    
    # STEP1 field bitshift
    symId = "DMT_STEP1_SHIFT"
    shiftVal = _get_position(dmtReg_DMTPRECLR_STEP1.getAttribute('mask'))
    dmtStep1Shift = dmtComponent.createIntegerSymbol(symId, None)
    dmtStep1Shift.setDefaultValue(shiftVal)
    dmtStep1Shift.setVisible(False) 
    
    # STEP2 field bitshift
    symId = "DMT_STEP2_SHIFT"
    shiftVal = _get_position(dmtReg_DMTCLR_STEP2.getAttribute('mask'))
    dmtStep2Shift = dmtComponent.createIntegerSymbol(symId, None)
    dmtStep2Shift.setDefaultValue(shiftVal)
    dmtStep2Shift.setVisible(False) 
    
    # STEP1 bitfield value to clear DMT
    step1ValSym = dmtComponent.createStringSymbol("STEP1_VAL",None)
    step1ValSym.setDefaultValue(str(64))
    step1ValSym.setVisible(False)
    
    # STEP2 bitfield value to clear DMT
    step2ValSym = dmtComponent.createStringSymbol("STEP2_VAL",None)
    step2ValSym.setDefaultValue(str(8))
    step2ValSym.setVisible(False)
    
    # DMTPRECLR register value
    dmtpreclrValSym = dmtComponent.createStringSymbol("DMTPRECLR_VAL",None)
    val = int(step1ValSym.getValue()) << dmtStep1Shift.getValue()
    dmtpreclrValSym.setDefaultValue(str(val))
    dmtpreclrValSym.setVisible(False)
    
    # DMTCLR register value
    dmtclrValSym = dmtComponent.createStringSymbol("DMTCLR_VAL",None)
    val = int(step2ValSym.getValue()) << dmtStep2Shift.getValue()
    dmtclrValSym.setDefaultValue(str(val))
    dmtclrValSym.setVisible(False)


    ################################################################################
    #### Code Generation ####
    ################################################################################
    configName = Variables.get("__CONFIGURATION_NAME")
    dmtModuleNode = ATDF.getNode("/avr-tools-device-file/modules/module@[name=\"DMT\"]")
    dmtModuleID = dmtModuleNode.getAttribute("id")
    
    dmtInstanceName = dmtComponent.createStringSymbol("DMT_INSTANCE_NAME", None)
    dmtInstanceName.setVisible(False)
    dmtInstanceName.setDefaultValue(dmtModuleNode.getAttribute("name"))
    Log.writeInfoMessage("Running " + dmtInstanceName.getValue())
    
    # Instance Header File
    dmtHeaderFile = dmtComponent.createFileSymbol("DMT_INSTANCE_HEADER", None)
    dmtHeaderFile.setSourcePath("../peripheral/dmt_01520/templates/plib_dmt.h.ftl")
    dmtHeaderFile.setOutputName("plib_"+dmtInstanceName.getValue().lower()+".h")
    dmtHeaderFile.setDestPath("/peripheral/dmt/")
    dmtHeaderFile.setProjectPath("config/" + configName + "/peripheral/dmt/")
    dmtHeaderFile.setType("HEADER")
    dmtHeaderFile.setMarkup(True)
    
    # Instance Source File
    dmtSourceFile = dmtComponent.createFileSymbol("DMT_TIMER_SOURCE", None)
    dmtSourceFile.setSourcePath("../peripheral/dmt_01520/templates/plib_dmt.c.ftl")
    dmtSourceFile.setOutputName("plib_"+dmtInstanceName.getValue().lower()+".c")
    dmtSourceFile.setDestPath("/peripheral/dmt/")
    dmtSourceFile.setProjectPath("config/" + configName + "/peripheral/dmt/")
    dmtSourceFile.setType("SOURCE")
    dmtSourceFile.setMarkup(True)
    
    # System Definition
    dmtSystemDefFile = dmtComponent.createFileSymbol("DMT_SYS_DEF", None)
    dmtSystemDefFile.setType("STRING")
    dmtSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
    dmtSystemDefFile.setSourcePath("../peripheral/dmt_01520/templates/system/definitions.h.ftl")
    dmtSystemDefFile.setMarkup(True)
    