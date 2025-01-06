/*******************************************************************************
Interface definition of MEM2MEM PLIB.

Company:
    Microchip Technology Inc.

File Name:
    plib_mem2mem.c

Summary:
    Interface definition of MEM2MEM Plib.

Description:
    This file defines the interface for the MEM2MEM Plib.
    It allows user to transfer data from one memory to another.
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
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAMEM2MEMED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Included Files
// *****************************************************************************
// *****************************************************************************

#include "device.h"
#include "plib_${MEM2MEM_INSTANCE_NAME?lower_case}.h"
<#if core.CoreSysIntFile == true>
#include "interrupts.h"
</#if>

// *****************************************************************************
// *****************************************************************************
// Global Data
// *****************************************************************************
// *****************************************************************************

static volatile MEM2MEM_OBJECT ${MEM2MEM_INSTANCE_NAME?lower_case}Obj;

// *****************************************************************************
// *****************************************************************************
// ${MEM2MEM_INSTANCE_NAME} PLib Interface Routines
// *****************************************************************************
// *****************************************************************************

bool ${MEM2MEM_INSTANCE_NAME}_ChannelTransfer( const void *srcAddr, const void *destAddr, size_t blockSize, MEM2MEM_TRANSFER_WIDTH twidth )
{
    bool status = false;
	const uint32_t *xdestAddr = (const uint32_t *) destAddr;
	const uint32_t *xsrcAddr = (const uint32_t *) srcAddr;

    if ((${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_ISR & MEM2MEM_ISR_RXEND_Msk) ==  MEM2MEM_ISR_RXEND_Msk)
    {
        uint16_t count = (uint16_t)(blockSize / (1UL << twidth));

        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_MR = (uint32_t)twidth;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_TPR = (uint32_t) xsrcAddr;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_TCR = count;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_RPR = (uint32_t) xdestAddr;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_RCR = count;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_IER = MEM2MEM_IER_RXEND_Msk;
        ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_PTCR = MEM2MEM_PTCR_RXTEN_Msk | MEM2MEM_PTCR_TXTEN_Msk;

        status = true;
    }

    return status;
}

void ${MEM2MEM_INSTANCE_NAME}_CallbackRegister( MEM2MEM_CALLBACK callback, uintptr_t context )
{
    ${MEM2MEM_INSTANCE_NAME?lower_case}Obj.callback = callback;

    ${MEM2MEM_INSTANCE_NAME?lower_case}Obj.context = context;
}

void __attribute__((used)) ${MEM2MEM_INSTANCE_NAME}_InterruptHandler( void )
{
    uint8_t error = (uint8_t)MEM2MEM_TRANSFER_EVENT_COMPLETE;
    uintptr_t context = ${MEM2MEM_INSTANCE_NAME?lower_case}Obj.context;

    ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_IDR = MEM2MEM_IDR_RXEND_Msk;

<#if MEM2MEM_PTSR_ERR>
    error = (uint8_t)(${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_PTSR & MEM2MEM_PTSR_ERR_Msk);

    ${MEM2MEM_INSTANCE_NAME}_REGS->MEM2MEM_PTCR = MEM2MEM_PTCR_ERRCLR_Msk;

</#if>
    if (${MEM2MEM_INSTANCE_NAME?lower_case}Obj.callback != NULL)
    {
        ${MEM2MEM_INSTANCE_NAME?lower_case}Obj.callback((MEM2MEM_TRANSFER_EVENT)error, context);
    }
}