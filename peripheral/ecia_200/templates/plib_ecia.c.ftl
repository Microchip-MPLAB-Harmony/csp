/*******************************************************************************
  ECIA PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ecia.c

  Summary:
    ECIA PLIB Source File

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

#include "device.h"
#include "plib_ecia.h"

void ECIA_Initialize(void)
{
    <#list ECIA_GIRQ_REG_START..ECIA_GIRQ_REG_END as n>
    <#assign ECIA_EN_SET_VAL = "ECIA_EN_SET_" + n + "_VAL">
    <#if .vars[ECIA_EN_SET_VAL] != "0">
    ECIA_REGS->ECIA_EN_SET${n} = 0x${.vars[ECIA_EN_SET_VAL]};
    </#if>
    </#list>

    <#if ECIA_GIRQ_BLOCK_REG_VAL != "0">
    ECIA_REGS->ECIA_BLK_EN_SET = 0x${ECIA_GIRQ_BLOCK_REG_VAL};
    </#if>
}
void ECIA_GIRQBlockEnable(ECIA_GIRQ_BLOCK_NUM block)
{
    ECIA_REGS->ECIA_BLK_EN_SET = (1U << (uint32_t)block);
}

void ECIA_GIRQBlockDisable(ECIA_GIRQ_BLOCK_NUM block)
{
    ECIA_REGS->ECIA_BLK_EN_CLR = (1U << (uint32_t)block);
}

void ECIA_GIRQBlockDisableAll(void)
{
    ECIA_REGS->ECIA_BLK_EN_CLR = 0xFFFFFFFFUL;
}

uint32_t ECIA_GIRQBlockStatusGet(ECIA_GIRQ_BLOCK_NUM block)
{
    return ECIA_REGS->ECIA_BLK_IRQ_VTOR & (1U << (uint32_t)block);
}

/* Enables the given interrupt source */
void ECIA_GIRQSourceEnable(ECIA_INT_SOURCE int_src)
{
    uint32_t* ecia_enset_ptr = (uint32_t*)&ECIA_REGS->ECIA_EN_SET8;
    ecia_enset_ptr += 5U * GIRQ_REG_GET(int_src);
    *ecia_enset_ptr = (1U << GIRQ_BIT_POS_GET(int_src));
}

/* Disables the given interrupt source */
void ECIA_GIRQSourceDisable(ECIA_INT_SOURCE int_src)
{
    uint32_t* ecia_enclr_ptr = (uint32_t*)&ECIA_REGS->ECIA_EN_CLR8;
    ecia_enclr_ptr += 5U * GIRQ_REG_GET(int_src);
    *ecia_enclr_ptr = (1U << GIRQ_BIT_POS_GET(int_src));
}

/* Returns true if interrupt for the given interrupt source is enabled, false otherwise */
bool ECIA_GIRQIsInterruptEnabled(ECIA_INT_SOURCE int_src)
{
    uint32_t* ecia_enset_ptr = (uint32_t*)&ECIA_REGS->ECIA_EN_SET8;
    ecia_enset_ptr += 5U * GIRQ_REG_GET(int_src);
    return *ecia_enset_ptr & (1U << GIRQ_BIT_POS_GET(int_src)) ? true : false;
}

/* Clears the given interrupt source */
void ECIA_GIRQSourceClear(ECIA_INT_SOURCE int_src)
{
    uint32_t* ecia_src_ptr = (uint32_t*)&ECIA_REGS->ECIA_SRC8;
    ecia_src_ptr += 5U * GIRQ_REG_GET(int_src);
    *ecia_src_ptr |= (1U << GIRQ_BIT_POS_GET(int_src));
}

/* Clear all interrupt sources in all the ECIA blocks */
void ECIA_GIRQSourceClearAll(void)
{
    uint32_t i;

    uint32_t* ecia_src_ptr = (uint32_t*)&ECIA_REGS->ECIA_SRC8;
    
    for (i = (uint32_t)ECIA_GIRQ_BLOCK_NUM8; i < (uint32_t)ECIA_GIRQ_BLOCK_NUM_MAX; i++)
    {
        *ecia_src_ptr = 0xFFFFFFFFUL;
        ecia_src_ptr += 5U;
    }
}

/* Disables all interrupt sources in all the ECIA blocks */
void ECIA_GIRQSourceDisableAll(void)
{
    uint32_t i;

    uint32_t* ecia_enclr_ptr = (uint32_t*)&ECIA_REGS->ECIA_EN_CLR8;
    
    for (i = (uint32_t)ECIA_GIRQ_BLOCK_NUM8; i < (uint32_t)ECIA_GIRQ_BLOCK_NUM_MAX; i++)
    {
        *ecia_enclr_ptr = 0xFFFFFFFFUL;
        ecia_enclr_ptr += 5U;
    }
}

/* Returns the Result bit of the given ECIA_INT_SOURCE. This API may be used to know if interrupt is active */
uint8_t ECIA_GIRQResultGet(ECIA_INT_SOURCE int_src)
{
    uint32_t* ecia_result_ptr = (uint32_t*)&ECIA_REGS->ECIA_RESULT8;
    ecia_result_ptr += 5U * GIRQ_REG_GET(int_src);
    return *ecia_result_ptr & (1U << GIRQ_BIT_POS_GET(int_src)) ? 1: 0;
}

/* Enables both ECIA and NVIC interrupt */
void ECIA_InterruptEnable(ECIA_INT_SOURCE int_src)
{
    ECIA_GIRQSourceEnable(int_src);
    ECIA_GIRQBlockEnable(1U << (GIRQ_REG_GET(int_src) + 8U));
    if (IS_INT_SRC_AGG_OR_DIR(int_src) == INT_SRC_IS_AGGREGATE)
    {
        NVIC_EnableIRQ(GIRQ_AGG_INT_NUM_GET(int_src));
    }
    else
    {
        NVIC_EnableIRQ(GIRQ_DIR_INT_NUM_GET(int_src));
    }
}

void ECIA_InterruptDisable(ECIA_INT_SOURCE int_src)
{
    ECIA_GIRQSourceDisable(int_src);
}