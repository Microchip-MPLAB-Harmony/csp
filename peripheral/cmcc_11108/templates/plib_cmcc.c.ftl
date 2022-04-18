/*******************************************************************************
   Cortex M Cache Controller (CMCC) Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_cmcc.c

  Summary:
    CMCC Source File

  Description:
   This file defines the interface to the CMCC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/

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

#include "device.h"
#include "peripheral/cmcc/plib_cmcc.h"
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>

<#if CMCC_INSTANCE_COUNT gt 1>
<#assign CMCCI = CMCC_ICACHE_INSTANCE>
<#else>
<#assign CMCCI = "CMCC">
</#if>
<#if CMCC_INSTANCE_COUNT gt 1>
<#assign CMCCD = CMCC_DCACHE_INSTANCE>
<#else>
<#assign CMCCD = "CMCC">
</#if>

void CMCC_Disable (void )
{
<#if CMCC_INSTANCE_COUNT == 1>
    CMCC_REGS->CMCC_CTRL &=(~CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
<#else>
    /* Disable ICache controller */
    ${CMCCI}_REGS->CMCC_CTRL &=(~CMCC_CTRL_CEN_Msk);
    while((${CMCCI}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /* Wait for the operation to complete */
    }

    /* Disable DCache controller */
    ${CMCCD}_REGS->CMCC_CTRL &=(~CMCC_CTRL_CEN_Msk);
    while((${CMCCD}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /* Wait for the operation to complete */
    }
</#if>
}

<#if CMCC_CCFG_EXISTS>
void CMCC_EnableICache (void )
{
    ${CMCCI}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCI}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCI}_REGS->CMCC_CFG &= (~CMCC_CFG_ICDIS_Msk);
    ${CMCCI}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

void CMCC_DisableICache (void )
{
    ${CMCCI}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCI}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCI}_REGS->CMCC_CFG |= (CMCC_CFG_ICDIS_Msk);
    ${CMCCI}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

void CMCC_EnableDCache (void )
{
    ${CMCCD}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCD}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCD}_REGS->CMCC_CFG &= (~CMCC_CFG_DCDIS_Msk);
    ${CMCCD}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

void CMCC_DisableDCache (void )
{
    ${CMCCD}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCD}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCD}_REGS->CMCC_CFG |= (CMCC_CFG_DCDIS_Msk);
    ${CMCCD}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

</#if>
<#if CMCC_INSTANCE_COUNT == 1>

void CMCC_InvalidateAll (void )
{
    CMCC_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((CMCC_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    CMCC_REGS->CMCC_MAINT0 = CMCC_MAINT0_INVALL_Msk;
    CMCC_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}
<#else>

void CMCC_ICacheInvalidateAll (void )
{
    ${CMCCI}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCI}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCI}_REGS->CMCC_MAINT0 = CMCC_MAINT0_INVALL_Msk;
    ${CMCCI}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}

void CMCC_DCacheInvalidateAll (void )
{
    ${CMCCD}_REGS->CMCC_CTRL &= (~CMCC_CTRL_CEN_Msk);
    while((${CMCCD}_REGS->CMCC_SR & CMCC_SR_CSTS_Msk) == CMCC_SR_CSTS_Msk)
    {
        /*Wait for the operation to complete*/
    }
    ${CMCCD}_REGS->CMCC_MAINT0 = CMCC_MAINT0_INVALL_Msk;
    ${CMCCD}_REGS->CMCC_CTRL = (CMCC_CTRL_CEN_Msk);
}
</#if>
