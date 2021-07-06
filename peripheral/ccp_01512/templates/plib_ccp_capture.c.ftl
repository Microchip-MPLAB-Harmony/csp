/*******************************************************************************
  Capture/Compare/PWM/Timer Module (${CCP_INSTANCE_NAME}) Peripheral Library (PLIB)

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

<#if CCP_TIMER_INTERRUPT == true>
static CCP_TIMER_OBJECT ${CCP_INSTANCE_NAME?lower_case}TimerObj;
</#if>
<#if CCP_CAP_INTERRUPT == true>
static CCP_CAPTURE_OBJECT ${CCP_INSTANCE_NAME?lower_case}CaptureObj;
</#if>
<#--Implementation-->
// *****************************************************************************

// *****************************************************************************
// Section: ${CCP_INSTANCE_NAME} Implementation
// *****************************************************************************
// *****************************************************************************

void ${CCP_INSTANCE_NAME}_CaptureInitialize (void)
{
    /* Disable Timer */
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;

    CCP${CCP_INSTANCE_NUM}CON1 = 0x${CCPCON1_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON2 = 0x${CCPCON2_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON3 = 0x${CCPCON3_REG_VALUE};

    <#if CCP_TIMER_INTERRUPT == true>
    /* Enable Timer overflow interrupt */
    ${CCP_IEC_REG}SET = _${CCP_IEC_REG}_CCT${CCP_INSTANCE_NUM}IE_MASK;
    </#if>
    <#if CCP_CAP_INTERRUPT == true>
    /* Enable input capture interrupt */
    ${CCP_CAP_COMP_IEC_REG}SET = _${CCP_CAP_COMP_IEC_REG}_CCP${CCP_INSTANCE_NUM}IE_MASK;
    </#if>    
}


void ${CCP_INSTANCE_NAME}_CaptureStart (void)
{
    CCP${CCP_INSTANCE_NUM}CON1SET = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}


void ${CCP_INSTANCE_NAME}_CaptureStop (void)
{
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}

<#if CCP_CCPCON1_T32 == true>
uint32_t ${CCP_INSTANCE_NAME}_Capture32bitBufferRead (void)
{
    return CCP${CCP_INSTANCE_NUM}BUF;
}
<#else>
uint16_t ${CCP_INSTANCE_NAME}_Capture16bitBufferRead (void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}BUF;
}
</#if>

<#if CCP_TIMER_INTERRUPT == true>

void ${CCP_INSTANCE_NAME}_TimerCallbackRegister(CCP_TIMER_CALLBACK callback, uintptr_t context)
{
    ${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn = callback;
    ${CCP_INSTANCE_NAME?lower_case}TimerObj.context = context;
}

void CCT${CCP_INSTANCE_NUM}_InterruptHandler(void)
{
    uint32_t status = ${CCP_IFS_REG}bits.CCT${CCP_INSTANCE_NUM}IF;
    ${CCP_IFS_REG}CLR = _${CCP_IFS_REG}_CCT${CCP_INSTANCE_NUM}IF_MASK;    //Clear IRQ flag    
    if( (${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn != NULL))
    {
        ${CCP_INSTANCE_NAME?lower_case}TimerObj.callback_fn(status, ${CCP_INSTANCE_NAME?lower_case}TimerObj.context);
    }
}
</#if>

<#if CCP_CAP_INTERRUPT == true>

void ${CCP_INSTANCE_NAME}_CaptureCallbackRegister(CCP_CAPTURE_CALLBACK callback, uintptr_t context)
{
    ${CCP_INSTANCE_NAME?lower_case}CaptureObj.callback_fn = callback;
    ${CCP_INSTANCE_NAME?lower_case}CaptureObj.context = context;
}

void CCP${CCP_INSTANCE_NUM}_InterruptHandler(void)
{
    ${CCP_CAP_COMP_IFS_REG}CLR = _${CCP_CAP_COMP_IFS_REG}_CCP${CCP_INSTANCE_NUM}IF_MASK;    //Clear IRQ flag
    if( (${CCP_INSTANCE_NAME?lower_case}CaptureObj.callback_fn != NULL))
    {
        ${CCP_INSTANCE_NAME?lower_case}CaptureObj.callback_fn(${CCP_INSTANCE_NAME?lower_case}CaptureObj.context);
    }
}

<#else>

bool ${CCP_INSTANCE_NAME}_CaptureStatusGet (void)
{
    bool status = false;
    status = ((CCP${CCP_INSTANCE_NUM}STAT >> _CCP1STAT_ICBNE_POSITION) & _CCP1STAT_ICBNE_MASK);
    return status;
}
</#if>

