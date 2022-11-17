/*******************************************************************************
  Interprocessor Communications PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${IPC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${IPC_INSTANCE_NAME} Source File

  Description:
    This file defines the interface to the IPC peripheral library.
    This library provides access to and control of the associated
    InterProcessor Communication peripheral.

  Remarks:
    None.

*******************************************************************************/
/*******************************************************************************
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
*******************************************************************************/
<#include "system/init_logic.ftl">
#include <stddef.h>
#include "device.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "plib_${IPC_INSTANCE_NAME?lower_case}.h"

typedef struct
{
    IPC_CALLBACK handler;
    uintptr_t context;
}${IPC_INSTANCE_NAME?lower_case}_callback_object_t;

static ${IPC_INSTANCE_NAME?lower_case}_callback_object_t ${IPC_INSTANCE_NAME?lower_case}_callback_obj[TOTAL_IPC_IRQS];

<#if IPC_INIT_REQUIRED>
void  ${IPC_INSTANCE_NAME}_Initialize(void)
{
<#if IPC_ENABLE_MASK != "">
    /* Clear interrupts */
    ${IPC_INSTANCE_NAME}_REGS->IPC_ICCR = IPC_ICCR_Msk;
    /* Enable interrupts */
    ${IPC_INSTANCE_NAME}_REGS->IPC_IECR = (${IPC_ENABLE_MASK});

</#if>
<#if IPC_WRITE_PROTECT>
    /* Enable write protect */
    ${IPC_INSTANCE_NAME}_REGS->IPC_WPMR = (IPC_WPMR_WPKEY_PASSWD | IPC_WPMR_Msk);
</#if>
}
</#if>

void ${IPC_INSTANCE_NAME}_SetIRQHandler(ipc_irq_mask_t irq_mask, IPC_CALLBACK handler, uintptr_t context)
{
    for (uint32_t irq_id = 0; irq_id < TOTAL_IPC_IRQS; irq_id++)
    {
        if ((irq_mask & ((uint32_t)1U << irq_id)) != 0U)
        {
            ${IPC_INSTANCE_NAME?lower_case}_callback_obj[irq_id].handler = handler;
            ${IPC_INSTANCE_NAME?lower_case}_callback_obj[irq_id].context = context;
        }
    }
}


void  ${IPC_INSTANCE_NAME}_InterruptHandler(void)
{
    for (uint32_t irq_id = 0 ; irq_id < TOTAL_IPC_IRQS; irq_id++)
    {
        ipc_irq_mask_t irq_mask =  ((uint32_t)1U << irq_id);
        if ((${IPC_INSTANCE_NAME}_GetIRQStatus() & irq_mask) != 0U)
        {
            IPC_CALLBACK handler = ${IPC_INSTANCE_NAME?lower_case}_callback_obj[irq_id].handler;
            uintptr_t context = ${IPC_INSTANCE_NAME?lower_case}_callback_obj[irq_id].context;
            if (handler != NULL)
            {
                handler(irq_mask, context);
            }
            /* Clear interrupts */
            ${IPC_INSTANCE_NAME}_REGS->IPC_ICCR = (irq_mask);
        }
    }
}

