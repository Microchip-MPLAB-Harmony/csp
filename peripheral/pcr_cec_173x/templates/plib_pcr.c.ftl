/*******************************************************************************
 PCR PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_pcr.c

  Summary:
    PCR PLIB Implementation File.

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

#include "plib_pcr.h"
#include "device.h"

#define PCR_PERIPH_RESET_LOCK                     (0xA6382D4DUL)
#define PCR_PERIPH_RESET_UNLOCK                   (0xA6382D4CUL)

void PCR_Initialize (void)
{
    /* Wait for PLL to lock. Output of PLL is 96 MHz. */
    while ((PCR_REGS->PCR_OSC_ID & PCR_OSC_ID_PLL_LOCK_Msk) == 0U)
    {
        /* Wait for PLL to lock */
    }

    /* Configure Processor Clock divide */
    PCR_REGS->PCR_PROC_CLK_CTRL = PCR_PROC_CLK_CTRL_DIV(${PROCESSOR_CLK_DIV});

    /* Select slow clock divide */
    PCR_REGS->PCR_SLOW_CLK_CTRL = PCR_SLOW_CLK_CTRL_DIV(${SLOW_CLK_DIVIDE});

    <#list 0..(NUM_SLEEP_EN_REGS-1) as n>
    <#assign PCR_SLEEP_EN         = "PCR_SLEEP_ENABLE" + n + "_REG_INDEX">
    <#assign PCR_SLEEP_EN_VAL = "PCR_SLEEP_ENABLE_" + .vars[PCR_SLEEP_EN] + "_VAL">
    PCR_REGS->PCR_SLP_EN_${.vars[PCR_SLEEP_EN]} = 0x${.vars[PCR_SLEEP_EN_VAL]};
    </#list>

    <#list 0..(NUM_PRIV_EN_REGS-1) as n>
    <#assign PCR_PRIV_EN         = "PCR_PRIV_ENABLE" + n + "_REG_INDEX">
    <#assign PCR_PRIV_EN_VAL = "PCR_PRIV_ENABLE_" + .vars[PCR_PRIV_EN] + "_VAL">
    PCR_REGS->PCR_EC_PRIV_EN${.vars[PCR_PRIV_EN]} = 0x${.vars[PCR_PRIV_EN_VAL]};
    </#list>
}

void PCR_PeripheralResetLock (void)
{
    PCR_REGS->PCR_PERIPH_RST_EN_LOCK = PCR_PERIPH_RESET_LOCK;
}

void PCR_PeripheralResetUnLock (void)
{
    PCR_REGS->PCR_PERIPH_RST_EN_LOCK = PCR_PERIPH_RESET_UNLOCK;
}

void PCR_PrivilegeEnLock (void)
{
    PCR_REGS->PCR_PRIV_EN_LOCK |= PCR_PRIV_EN_LOCK_LOCK_EN_Msk;
}

void PCR_PrivilegeEnUnLock (void)
{
    PCR_REGS->PCR_PRIV_EN_LOCK &= ~PCR_PRIV_EN_LOCK_LOCK_EN_Msk;
}

uint32_t PCR_PowerFailResetStatusRegGet(void)
{
    return VTR_REG_BANK_REGS->VTR_REG_BANK_PFRS;
}

void PCR_PowerFailResetStatusClear(uint32_t pfsr_bits)
{
    VTR_REG_BANK_REGS->VTR_REG_BANK_PFRS = pfsr_bits;
}


<#list 0..(NUM_SLEEP_EN_REGS-1) as n>
<#assign PCR_SLEEP_EN         = "PCR_SLEEP_ENABLE" + n + "_REG_INDEX">

void PCR_SleepEnable${.vars[PCR_SLEEP_EN]} (PCR_SLEEP_EN${.vars[PCR_SLEEP_EN]} blockId)
{
    uint32_t blockIdMsk = (uint32_t)blockId & PCR_SLP_EN_${.vars[PCR_SLEEP_EN]}_Msk;
    PCR_REGS->PCR_SLP_EN_${.vars[PCR_SLEEP_EN]} |= blockIdMsk;
}

void PCR_SleepDisable${.vars[PCR_SLEEP_EN]} (PCR_SLEEP_EN${.vars[PCR_SLEEP_EN]} blockId)
{
    uint32_t blockIdMsk = (uint32_t)blockId & PCR_SLP_EN_${.vars[PCR_SLEEP_EN]}_Msk;
    PCR_REGS->PCR_SLP_EN_${.vars[PCR_SLEEP_EN]} &= ~blockIdMsk;
}

</#list>

<#list 0..(NUM_PRIV_EN_REGS-1) as n>
<#assign PCR_PRIV_EN         = "PCR_PRIV_ENABLE" + n + "_REG_INDEX">

void PCR_PrivilegeEnable${.vars[PCR_PRIV_EN]} (PCR_PRIV_EN${.vars[PCR_PRIV_EN]} blockId)
{
    uint32_t blockIdMsk = (uint32_t)blockId & PCR_EC_PRIV_EN${.vars[PCR_PRIV_EN]}_Msk;
    PCR_REGS->PCR_EC_PRIV_EN${.vars[PCR_PRIV_EN]} |= blockIdMsk;
}

void PCR_PrivilegeDisable${.vars[PCR_PRIV_EN]} (PCR_PRIV_EN${.vars[PCR_PRIV_EN]} blockId)
{
    uint32_t blockIdMsk = (uint32_t)blockId & PCR_EC_PRIV_EN${.vars[PCR_PRIV_EN]}_Msk;
    PCR_REGS->PCR_EC_PRIV_EN${.vars[PCR_PRIV_EN]} &= ~blockIdMsk;
}

</#list>

<#list 0..(NUM_RESET_EN_REGS-1) as n>
<#assign PCR_RESET_EN         = "PCR_RESET_ENABLE" + n + "_REG_INDEX">

void PCR_ResetEnable${.vars[PCR_RESET_EN]} (PCR_RESET_EN${.vars[PCR_RESET_EN]} blockId)
{
    uint32_t blockIdMsk = (uint32_t)blockId & PCR_RST_EN_${.vars[PCR_RESET_EN]}_Msk;
    PCR_REGS->PCR_RST_EN_${.vars[PCR_RESET_EN]} |= blockIdMsk;
}

</#list>