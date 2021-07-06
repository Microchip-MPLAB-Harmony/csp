/*******************************************************************************
  Capture/Compare/PWM/Timer Module ${CCP_INSTANCE_NAME} Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CCP_INSTANCE_NAME?lower_case}.c

  Summary:
    ${CCP_INSTANCE_NAME} Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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
#include "plib_${CCP_INSTANCE_NAME?lower_case}.h"

<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${CCP_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
<#assign mode = CCP_COMP_CCPCON1_MOD?number>
<#assign CCP_INSTANCE_NUM = CCP_INSTANCE_NUM>

<#if CCP_TIMER_INTERRUPT == true>
static CCP_TIMER_OBJECT ${CCP_INSTANCE_NAME?lower_case}TimerObj;
</#if>
<#if CCP_COMP_INTERRUPT == true>
static CCP_COMPARE_OBJECT ${CCP_INSTANCE_NAME?lower_case}CompareObj;
</#if>
void ${CCP_INSTANCE_NAME}_CompareInitialize (void)
{
    /* Disable Timer */
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;

    CCP${CCP_INSTANCE_NUM}CON1 = 0x${CCPCON1_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON2 = 0x${CCPCON2_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON3 = 0x${CCPCON3_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}PR = ${CCP_COMP_CCPPR};
    CCP${CCP_INSTANCE_NUM}RA = ${CCP_COMP_CCPRA};
    CCP${CCP_INSTANCE_NUM}RB = ${CCP_COMP_CCPRB};

<#if CCP_TIMER_INTERRUPT == true>
    ${CCP_IEC_REG}SET = _${CCP_IEC_REG}_CCT${CCP_INSTANCE_NUM}IE_MASK;
</#if>
<#if CCP_COMP_INTERRUPT == true>
    /* Enable input compare interrupt */
    ${CCP_CAP_COMP_IEC_REG}SET = _${CCP_CAP_COMP_IEC_REG}_CCP${CCP_INSTANCE_NUM}IE_MASK;
</#if> 
}

void ${CCP_INSTANCE_NAME}_CompareStart (void)
{
    CCP${CCP_INSTANCE_NUM}CON1SET = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}

void ${CCP_INSTANCE_NAME}_CompareStop (void)
{
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}

void ${CCP_INSTANCE_NAME}_CompareAutoShutdownClear (void)
{
    CCP${CCP_INSTANCE_NUM}STATCLR = _CCP${CCP_INSTANCE_NUM}STAT_ASEVT_MASK;
}

void ${CCP_INSTANCE_NAME}_CompareAutoShutdownSet (void)
{
    CCP${CCP_INSTANCE_NUM}CON2SET = _CCP${CCP_INSTANCE_NUM}CON2_SSDG_MASK;
}

<#if mode lt 4>  <#-- single edge mode -->
<#if CCP_CCPCON1_T32 == true>
void ${CCP_INSTANCE_NAME}_Compare32bitValueSet (uint32_t value)
{
    CCP${CCP_INSTANCE_NUM}RB = (uint16_t)value;
    CCP${CCP_INSTANCE_NUM}RA = (uint16_t)(value >> 16U);
}

uint32_t ${CCP_INSTANCE_NAME}_Compare32bitValueGet (void)
{
    return ((CCP${CCP_INSTANCE_NUM}RA << 16U) | CCP${CCP_INSTANCE_NUM}RB);
}

void ${CCP_INSTANCE_NAME}_Compare32bitPeriodValueSet (uint32_t value)
{
    CCP${CCP_INSTANCE_NUM}PR = value;
}

uint32_t ${CCP_INSTANCE_NAME}_Compare32bitPeriodValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}PR;
}

<#else>
void ${CCP_INSTANCE_NAME}_Compare16bitValueSet (uint16_t value)
{
    CCP${CCP_INSTANCE_NUM}RA = (uint16_t)value;
}
uint16_t ${CCP_INSTANCE_NAME}_Compare16bitValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}RA;
}

void ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueSet (uint16_t value)
{
    CCP${CCP_INSTANCE_NUM}PR = value;
}

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}PR;
}
</#if>
</#if>

<#if mode gt 3 >  <#-- dual-edge mode/center-aligned/variable freq mode -->

void ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueSet (uint16_t value)
{
    CCP${CCP_INSTANCE_NUM}PR = value;
}

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitPeriodValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}PR;
}


void ${CCP_INSTANCE_NAME}_Compare16bitRAValueSet (uint16_t value)
{
    CCP${CCP_INSTANCE_NUM}RA = value;
}

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitRAValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}RA;
}

void ${CCP_INSTANCE_NAME}_Compare16bitRBValueSet (uint16_t value)
{
    CCP${CCP_INSTANCE_NUM}RB = value;
}

uint16_t ${CCP_INSTANCE_NAME}_Compare16bitRBValueGet (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}RB;
}
</#if>

<#if CCP_MCCP_PRESENT == true>
void ${CCP_INSTANCE_NAME}_CompareDeadTimeSet (uint8_t value)
{
    CCP${CCP_INSTANCE_NUM}CON3 = (value & _CCP${CCP_INSTANCE_NUM}CON3_DT_MASK);
}

uint8_t ${CCP_INSTANCE_NAME}_CompareDeadTimeGet (void)
{
    return (uint8_t)(CCP${CCP_INSTANCE_NUM}CON3 & _CCP${CCP_INSTANCE_NUM}CON3_DT_MASK);
}
</#if>

<#if CCP_TIMER_INTERRUPT == true>
void ${CCP_INSTANCE_NAME}_TimerCallbackRegister(CCP_TIMER_CALLBACK callback, uintptr_t context)
{
    ${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn = callback;

    ${CCP_INSTANCE_NAME?lower_case}TimerObj.context = context;
}

void CCT${CCP_INSTANCE_NUM}_InterruptHandler (void)
{
    uint32_t status = ${CCP_IFS_REG}bits.CCT${CCP_INSTANCE_NUM}IF;
    ${CCP_IFS_REG}CLR = _${CCP_IFS_REG}_CCT${CCP_INSTANCE_NUM}IF_MASK;    //Clear IRQ flag

    if( (${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn != NULL))
    {
        ${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn(status, ${CCP_INSTANCE_NAME?lower_case}TimerObj.context);
    }
}
</#if>

<#if CCP_COMP_INTERRUPT == true>
void ${CCP_INSTANCE_NAME}_CompareCallbackRegister(CCP_COMPARE_CALLBACK callback, uintptr_t context)
{
    ${CCP_INSTANCE_NAME?lower_case}CompareObj.callback_fn = callback;
    ${CCP_INSTANCE_NAME?lower_case}CompareObj.context = context;
}

void CCP${CCP_INSTANCE_NUM}_InterruptHandler(void)
{
    ${CCP_CAP_COMP_IFS_REG}CLR = _${CCP_CAP_COMP_IFS_REG}_CCP${CCP_INSTANCE_NUM}IF_MASK;    //Clear IRQ flag
    if( (${CCP_INSTANCE_NAME?lower_case}CompareObj.callback_fn != NULL))
    {
        ${CCP_INSTANCE_NAME?lower_case}CompareObj.callback_fn(${CCP_INSTANCE_NAME?lower_case}CompareObj.context);
    }
}
</#if>
