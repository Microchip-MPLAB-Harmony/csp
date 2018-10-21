/*******************************************************************************
  FREQUENCY METER(${FREQM_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${FREQM_INSTANCE_NAME?lower_case}.c

  Summary:
    ${FREQM_INSTANCE_NAME} PLIB Implementation File.

  Description:
    This file defines the interface to the FREQM peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

  Remarks:
    None.

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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "plib_${FREQM_INSTANCE_NAME?lower_case}.h"

// *****************************************************************************
// *****************************************************************************
// Section: Global Data
// *****************************************************************************
// *****************************************************************************

<#if FREQM_INTERRUPT_MODE == true>
typedef struct
{
    FREQM_CALLBACK callback;

    uintptr_t context;

} FREQM_OBJECT;

FREQM_OBJECT ${FREQM_INSTANCE_NAME?lower_case}Obj;
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: ${FREQM_INSTANCE_NAME} Interface Implementations
// *****************************************************************************
// *****************************************************************************

void ${FREQM_INSTANCE_NAME}_Initialize(void)
{
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_CFGA = FREQM_CFGA_REFNUM(${FREQM_REF_CLK_CYCLES}) ${FREQM_REF_CLK_DIV?then('| FREQM_CFGA_DIVREF_Msk', '')};
<#if FREQM_INTERRUPT_MODE == true>

    /* Enable DONE Interrupt */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTENSET = FREQM_INTENSET_DONE_Msk;
</#if>

    /* Enable FREQM */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_CTRLA = FREQM_CTRLA_ENABLE_Msk;

    /* Wait for Sync */
    while(${FREQM_INSTANCE_NAME}_REGS->FREQM_SYNCBUSY);
}

bool ${FREQM_INSTANCE_NAME}_MeasurementStart(void)
{
    bool status = false;

    /* Check if measurement is already in progress */
    if((${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) != FREQM_STATUS_BUSY_Msk)
    {
        /* Clear the Done Interrupt flag */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTFLAG = FREQM_INTFLAG_DONE_Msk;

        /* Start measurement */
        ${FREQM_INSTANCE_NAME}_REGS->FREQM_CTRLB = FREQM_CTRLB_START_Msk;

        status = true;
    }

    return status;
}

bool ${FREQM_INSTANCE_NAME}_IsBusy(void)
{
    bool freqmIsBusy = false;

    if((${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_BUSY_Msk) == FREQM_STATUS_BUSY_Msk)
    {
        freqmIsBusy = true;
    }

    return freqmIsBusy;
}

FREQM_ERROR ${FREQM_INSTANCE_NAME}_ErrorGet(void)
{
    FREQM_ERROR errorStatus = FREQM_ERROR_NONE;

    errorStatus = ${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS & FREQM_STATUS_OVF_Msk;

    /* Clear overflow status */
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_STATUS = FREQM_STATUS_OVF_Msk;

    return errorStatus;
}

static uint64_t ${FREQM_INSTANCE_NAME}_Mul32x32(uint32_t r0, uint32_t r1)
{
    uint16_t r0h = r0 >> 16, r0l = r0 & 0xFFFF;
    uint16_t r1h = r1 >> 16, r1l = r1 & 0xFFFF;

    return ((uint64_t)(r0h * r1h) << 32)
         + ((uint64_t)(r0h * r1l) << 16)
         + ((uint64_t)(r0l * r1h) << 16)
         + ((uint64_t)(r0l * r1l) << 0);
}

uint32_t ${FREQM_INSTANCE_NAME}_FrequencyGet(void)
{
    uint64_t result = 0;

    result = ${FREQM_INSTANCE_NAME}_Mul32x32(${FREQM_INSTANCE_NAME}_REGS->FREQM_VALUE, ${FREQM_REF_CLOCK_FREQUENCY}UL);

    result = (result >> ${FREQM_RESULT_RIGHT_SHIFT});

    return (uint32_t)result;
}

<#if FREQM_INTERRUPT_MODE == true>
void ${FREQM_INSTANCE_NAME}_CallbackRegister(FREQM_CALLBACK freqmCallback, uintptr_t context)
{
    ${FREQM_INSTANCE_NAME?lower_case}Obj.callback = freqmCallback;

    ${FREQM_INSTANCE_NAME?lower_case}Obj.context = context;
}

void ${FREQM_INSTANCE_NAME}_InterruptHandler(void)
{
    ${FREQM_INSTANCE_NAME}_REGS->FREQM_INTFLAG = FREQM_INTFLAG_DONE_Msk;

    if(${FREQM_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${FREQM_INSTANCE_NAME?lower_case}Obj.callback(${FREQM_INSTANCE_NAME?lower_case}Obj.context);
    }
}
</#if>

