/*******************************************************************************
  Operational Amplifier  PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${OPAMP_INSTANCE_NAME?lower_case}.c

  Summary:
    OPAMP Source File

  Description:
    This file defines the interface to the OPAMP peripheral library.
    This library provides access to and control of the associated
    Operational Amplifier .

  Remarks:
    None.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
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
*******************************************************************************/
// DOM-IGNORE-END
#include "plib_${OPAMP_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${OPAMP_INSTANCE_NAME}_Initialize(void)
{
    /* Reset the peripheral */
    ${OPAMP_INSTANCE_NAME}_REGS->OPAMP_CTRLA = OPAMP_CTRLA_SWRST_Msk;
    <#list 0..2 as i>
    <#assign OPAMP_OPAMPCTRL_ENABLE = "OPAMP_OPAMPCTRL_" + i + "_ENABLE">
    <#assign OPAMP_OPAMPCTRL_MUXPOS = "OPAMP_OPAMPCTRL_" + i + "_MUXPOS">
    <#assign OPAMP_OPAMPCTRL_MUXNEG = "OPAMP_OPAMPCTRL_" + i + "_MUXNEG">
    <#assign OPAMP_OPAMPCTRL_ANAOUT = "OPAMP_OPAMPCTRL_" + i + "_ANAOUT">
    <#assign OPAMP_OPAMPCTRL_BIAS = "OPAMP_OPAMPCTRL_" + i + "_BIAS">
    <#assign OPAMP_OPAMPCTRL_RUNSTDBY = "OPAMP_OPAMPCTRL_" + i + "_RUNSTDBY">
    <#assign OPAMP_OPAMPCTRL_ONDEMAND = "OPAMP_OPAMPCTRL_" + i + "_ONDEMAND">
    <#assign OPAMP_OPAMPCTRL_RES2OUT = "OPAMP_OPAMPCTRL_" + i + "_RES2OUT">
    <#assign OPAMP_OPAMPCTRL_RES2VCC = "OPAMP_OPAMPCTRL_" + i + "_RES2VCC">
    <#assign OPAMP_OPAMPCTRL_RES1EN = "OPAMP_OPAMPCTRL_" + i + "_RES1EN">
    <#assign OPAMP_OPAMPCTRL_RES1MUX = "OPAMP_OPAMPCTRL_" + i + "_RES1MUX">
    <#assign OPAMP_OPAMPCTRL_POTMUX = "OPAMP_OPAMPCTRL_" + i + "_POTMUX">
    <#if (.vars[OPAMP_OPAMPCTRL_ENABLE] == true)>
    /* Configure OPAMPCTRL${i} */
    <@compress single_line=true>${OPAMP_INSTANCE_NAME}_REGS->OPAMP_OPAMPCTRL${i} = OPAMP_OPAMPCTRL${i}_MUXPOS(${.vars[OPAMP_OPAMPCTRL_MUXPOS]})
                                  | OPAMP_OPAMPCTRL${i}_MUXNEG(${.vars[OPAMP_OPAMPCTRL_MUXNEG]})
                                  | OPAMP_OPAMPCTRL${i}_BIAS(${.vars[OPAMP_OPAMPCTRL_BIAS]})
                                  | OPAMP_OPAMPCTRL${i}_RES1MUX(${.vars[OPAMP_OPAMPCTRL_RES1MUX]})
                                  | OPAMP_OPAMPCTRL${i}_POTMUX(${.vars[OPAMP_OPAMPCTRL_POTMUX]})
                                  ${.vars[OPAMP_OPAMPCTRL_ANAOUT]?then(' | OPAMP_OPAMPCTRL${i}_ANAOUT_Msk','')}
                                  ${.vars[OPAMP_OPAMPCTRL_RES2OUT]?then(' | OPAMP_OPAMPCTRL${i}_RES2OUT_Msk','')}
                                  ${.vars[OPAMP_OPAMPCTRL_RES1EN]?then(' | OPAMP_OPAMPCTRL${i}_RES1EN_Msk','')}
                                  ${.vars[OPAMP_OPAMPCTRL_ONDEMAND]?then(' | OPAMP_OPAMPCTRL${i}_ONDEMAND_Msk','')}
                                  ${.vars[OPAMP_OPAMPCTRL_RUNSTDBY]?then(' | OPAMP_OPAMPCTRL${i}_RUNSTDBY_Msk','')}
                                  ${.vars[OPAMP_OPAMPCTRL_ENABLE]?then(' | OPAMP_OPAMPCTRL${i}_ENABLE_Msk','')}
                                  ;</@compress>
    
    </#if>
    </#list>
    /* Enable the peripheral */
    ${OPAMP_INSTANCE_NAME}_REGS->OPAMP_CTRLA = OPAMP_CTRLA_ENABLE_Msk;
}
