/*******************************************************************************
  Output Compare ${OCMP_INSTANCE_NAME} Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${OCMP_INSTANCE_NAME?lower_case}.c

  Summary:
    ${OCMP_INSTANCE_NAME} Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
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
*******************************************************************************/
#include "plib_${OCMP_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${OCMP_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
<#assign mode = OCMP_OCxCON_OCM?number>
<#assign INDEX = OCMP_INSTANCE_NAME?remove_beginning("OCMP")>

<#if OCMP_INTERRUPT_ENABLE == true>

OCMP_OBJECT ${OCMP_INSTANCE_NAME?lower_case}Obj;
</#if>

void ${OCMP_INSTANCE_NAME}_Initialize (void)
{
    /*Setup OC${INDEX}CON        */
    /*OCM         = ${OCMP_OCxCON_OCM}        */
    /*OCTSEL    = ${OCMP_CFGCON_OCACLK?then('${OCMP_OCxCON_OCTSEL_ALT}','${OCMP_OCxCON_OCTSEL}')}        */
    /*OC32         = ${OCMP_OCxCON_OC32}        */
    /*SIDL         = ${OCMP_OCxCON_SIDL?then('true', 'false')}    */

    OC${INDEX}CON = 0x${OCxCON_VALUE};

  <#if OCMP_CFGCON_OCACLK?c == 'true'>
    CFGCON |= _CFGCON_OCACLK_MASK;
  </#if>

<#if OCMP_INTERRUPT_ENABLE == true>
    ${IEC_REG} = _${IEC_REG}_OC${INDEX}IE_MASK;
</#if>
}

void ${OCMP_INSTANCE_NAME}_Enable (void)
{
    OC${INDEX}CONSET = _OC${INDEX}CON_ON_MASK;
}

void ${OCMP_INSTANCE_NAME}_Disable (void)
{
    OC${INDEX}CONCLR = _OC${INDEX}CON_ON_MASK;
}

<#if mode == 7>
bool ${OCMP_INSTANCE_NAME}_FaultStatusGet (void)
{
    return (bool)(OC${INDEX}CON & _OC${INDEX}CON_OCFLT_MASK);
}
</#if>

<#if mode lt 6>
void ${OCMP_INSTANCE_NAME}_CompareValueSet (uint32_t value)
{
    OC${INDEX}R = value;
}
</#if>

uint32_t ${OCMP_INSTANCE_NAME}_CompareValueGet (void)
{
    return OC${INDEX}R;
}

<#if mode gt 3 >
void ${OCMP_INSTANCE_NAME}_CompareSecondaryValueSet (uint32_t value)
{
    OC${INDEX}RS = value;
}

uint32_t ${OCMP_INSTANCE_NAME}_CompareSecondaryValueGet (void)
{
    return OC${INDEX}RS;
}
</#if>

<#if OCMP_INTERRUPT_ENABLE == true>
void ${OCMP_INSTANCE_NAME}_CallbackRegister(OCMP_CALLBACK callback, uintptr_t context)
{
    ${OCMP_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${OCMP_INSTANCE_NAME?lower_case}Obj.context = context;
}

void OUTPUT_COMPARE_${INDEX}_InterruptHandler (void)
{
    ${IFS_REG}CLR = _${IFS_REG}_IC${INDEX}IF_MASK;    //Clear IRQ flag

    if( (${OCMP_INSTANCE_NAME?lower_case}Obj.callback != NULL))
    {
        ${OCMP_INSTANCE_NAME?lower_case}Obj.callback(${OCMP_INSTANCE_NAME?lower_case}Obj.context);
    }
}

</#if>