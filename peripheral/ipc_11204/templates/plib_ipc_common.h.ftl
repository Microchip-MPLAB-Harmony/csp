/*******************************************************************************
  Interprocessor Communications PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ipc_common.h

  Summary:
    IPC common header file

  Description:
    This file declares common interfaces and datatypes for all IPC peripherals.

  Remarks:
    None.

*******************************************************************************/
// DOM-IGNORE-BEGIN
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
#ifndef PLIB_IPC_COMMON_H
#define PLIB_IPC_COMMON_H

typedef uint32_t ipc_irq_mask_t;

<#list 0..TOTAL_IPC_IRQS - 1 as index>
#define IPC_IRQ${index}_MASK    ((uint32_t)1U << ${index})
</#list>

#define TOTAL_IPC_IRQS      ${TOTAL_IPC_IRQS}U

typedef void (*IPC_CALLBACK) (ipc_irq_mask_t irq_mask, uintptr_t context);

#endif //PLIB_IPC_COMMON_H