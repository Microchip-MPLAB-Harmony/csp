/*******************************************************************************
  CCP Peripheral Library Interface Source File

  Company
    Microchip Technology Inc.

  File Name
    plib_${CCP_INSTANCE_NAME?lower_case}.c

  Summary
    ${CCP_INSTANCE_NAME} peripheral library source file.

  Description
    This file implements the interface to the CCP peripheral library.  This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${CCP_INSTANCE_NAME?lower_case}.h"

<#if CCP_TIMER_INTERRUPT == true>
static CCP_TIMER_OBJECT ${CCP_INSTANCE_NAME?lower_case}Obj;
</#if>


void ${CCP_INSTANCE_NAME}_TimerInitialize(void)
{
    /* Disable Timer */
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;

    CCP${CCP_INSTANCE_NUM}CON1 = 0x${CCPCON1_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON2 = 0x${CCPCON2_REG_VALUE};

    CCP${CCP_INSTANCE_NUM}CON3 = 0x${CCPCON3_REG_VALUE};

    /* Clear counter */
    CCP${CCP_INSTANCE_NUM}TMR = 0x0;

    /*Set period */
    CCP${CCP_INSTANCE_NUM}PR = ${CCP_PERIOD}U;

    <#if CCP_TIMER_INTERRUPT == true>
    ${CCP_IEC_REG}SET = _${CCP_IEC_REG}_CCT${CCP_INSTANCE_NUM}IE_MASK;
    </#if>

}


void ${CCP_INSTANCE_NAME}_TimerStart(void)
{
    CCP${CCP_INSTANCE_NUM}CON1SET = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}


void ${CCP_INSTANCE_NAME}_TimerStop (void)
{
    CCP${CCP_INSTANCE_NUM}CON1CLR = _CCP${CCP_INSTANCE_NUM}CON1_ON_MASK;
}

<#if CCP_CCPCON1_T32 == false>
void ${CCP_INSTANCE_NAME}_Timer16bitPeriodSet(uint16_t period)
{
    CCP${CCP_INSTANCE_NUM}PR  = period;
}

uint16_t ${CCP_INSTANCE_NAME}_Timer16bitPeriodGet(void)
{
    return (uint16_t)CCP${CCP_INSTANCE_NUM}PR;
}

uint16_t ${CCP_INSTANCE_NAME}_Timer16bitCounterGet(void)
{
    return (uint16_t)(CCP${CCP_INSTANCE_NUM}TMR);
}

<#else>
void ${CCP_INSTANCE_NAME}_Timer32bitPeriodSet(uint32_t period)
{
    CCP${CCP_INSTANCE_NUM}PR  = period;
}

uint32_t ${CCP_INSTANCE_NAME}_Timer32bitPeriodGet(void)
{
    return CCP${CCP_INSTANCE_NUM}PR;
}

uint32_t ${CCP_INSTANCE_NAME}_Timer32bitCounterGet(void)
{
    return (CCP${CCP_INSTANCE_NUM}TMR);
}

</#if>

uint32_t ${CCP_INSTANCE_NAME}_TimerFrequencyGet(void)
{
    return (${CCP_CLOCK_FREQ});
}

<#if CCP_TIMER_INTERRUPT == true>
void CCT${CCP_INSTANCE_NUM}_InterruptHandler (void)
{
    uint32_t status = ${CCP_IFS_REG}bits.CCT${CCP_INSTANCE_NUM}IF;
    ${CCP_IFS_REG}CLR = _${CCP_IFS_REG}_CCT${CCP_INSTANCE_NUM}IF_MASK;

    if((${CCP_INSTANCE_NAME?lower_case}Obj.callback_fn != NULL))
    {
        ${CCP_INSTANCE_NAME?lower_case}Obj.callback_fn(status, ${CCP_INSTANCE_NAME?lower_case}Obj.context);
    }
}


void ${CCP_INSTANCE_NAME}_TimerInterruptEnable(void)
{

    ${CCP_IEC_REG}SET = _${CCP_IEC_REG}_CCP${CCP_INSTANCE_NUM}IE_MASK;
}


void ${CCP_INSTANCE_NAME}_TimerInterruptDisable(void)
{
    ${CCP_IEC_REG}CLR = _${CCP_IEC_REG}_CCP${CCP_INSTANCE_NUM}IE_MASK;
}


void ${CCP_INSTANCE_NAME}_TimerCallbackRegister( CCP_TIMER_CALLBACK callback_fn, uintptr_t context )
{
    /* Save callback_fn and context in local memory */
    ${CCP_INSTANCE_NAME?lower_case}Obj.callback_fn = callback_fn;
    ${CCP_INSTANCE_NAME?lower_case}Obj.context = context;
}
</#if>
