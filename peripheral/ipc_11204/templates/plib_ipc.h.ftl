/*******************************************************************************
  Interprocessor Communications PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${IPC_INSTANCE_NAME?lower_case}.h

  Summary:
    ${IPC_INSTANCE_NAME} Header File

  Description:
    This file declares the interface to the IPC peripheral library.
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
#ifndef PLIB_${IPC_INSTANCE_NAME}_H
#define PLIB_${IPC_INSTANCE_NAME}_H

#include "plib_ipc_common.h"

static inline void ${IPC_INSTANCE_NAME}_SetIRQ(ipc_irq_mask_t irq)
{
    ${IPC_INSTANCE_NAME}_REGS->IPC_ISCR = irq;
}

static inline void ${IPC_INSTANCE_NAME}_ClearIRQ(ipc_irq_mask_t irq)
{
    ${IPC_INSTANCE_NAME}_REGS->IPC_ICCR = irq;
}

static inline ipc_irq_mask_t ${IPC_INSTANCE_NAME}_GetPendingIRQs(void)
{
    return ${IPC_INSTANCE_NAME}_REGS->IPC_IPR;
}

static inline void ${IPC_INSTANCE_NAME}_EnableIRQ(ipc_irq_mask_t irq)
{
<#if IPC_WRITE_PROTECT>
    ${IPC_INSTANCE_NAME}_REGS->IPC_WPMR = IPC_WPMR_WPKEY_PASSWD;
</#if>
    ${IPC_INSTANCE_NAME}_REGS->IPC_IECR = irq;
<#if IPC_WRITE_PROTECT>
    ${IPC_INSTANCE_NAME}_REGS->IPC_WPMR = (IPC_WPMR_WPKEY_PASSWD | IPC_WPMR_Msk);
</#if>
}

static inline void ${IPC_INSTANCE_NAME}_DisableIRQ(ipc_irq_mask_t irq)
{
<#if IPC_WRITE_PROTECT>
    ${IPC_INSTANCE_NAME}_REGS->IPC_WPMR = IPC_WPMR_WPKEY_PASSWD;
</#if>
    ${IPC_INSTANCE_NAME}_REGS->IPC_IDCR = irq;
<#if IPC_WRITE_PROTECT>
    ${IPC_INSTANCE_NAME}_REGS->IPC_WPMR = (IPC_WPMR_WPKEY_PASSWD | IPC_WPMR_Msk);
</#if>
}

static inline ipc_irq_mask_t ${IPC_INSTANCE_NAME}_GetEnabledIRQs(void)
{
    return ${IPC_INSTANCE_NAME}_REGS->IPC_IMR;
}

static inline ipc_irq_mask_t ${IPC_INSTANCE_NAME}_GetIRQStatus(void)
{
    return ${IPC_INSTANCE_NAME}_REGS->IPC_ISR;
}

<#if IPC_INIT_REQUIRED>
void  ${IPC_INSTANCE_NAME}_Initialize(void);
</#if>

void ${IPC_INSTANCE_NAME}_SetIRQHandler(ipc_irq_mask_t irq, IPC_CALLBACK handler, uintptr_t context);

#endif //PLIB_${IPC_INSTANCE_NAME}_H