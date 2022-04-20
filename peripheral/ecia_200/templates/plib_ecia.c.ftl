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
    ECIA_REGS->ECIA_BLK_EN_SET = (1UL << (uint32_t)block);
}

void ECIA_GIRQBlockDisable(ECIA_GIRQ_BLOCK_NUM block)
{
    ECIA_REGS->ECIA_BLK_EN_CLR = (1UL << (uint32_t)block);
}

void ECIA_GIRQBlockDisableAll(void)
{
    ECIA_REGS->ECIA_BLK_EN_CLR = 0xFFFFFFFFUL;
}

uint32_t ECIA_GIRQBlockStatusGet(ECIA_GIRQ_BLOCK_NUM block)
{
    return ECIA_REGS->ECIA_BLK_IRQ_VTOR & (1UL << (uint32_t)block);
}

/* Enables the given interrupt source */
void ECIA_GIRQSourceEnable(ECIA_INT_SOURCE int_src)
{
    uint32_t ecia_enset_addr = ECIA_BASE_ADDRESS + ECIA_EN_SET8_REG_OFST + (20U * GIRQ_REG_GET(int_src));
    uint32_t* ecia_enset_ptr = (uint32_t*)ecia_enset_addr;
    *ecia_enset_ptr = (1UL << GIRQ_BIT_POS_GET(int_src));
}

/* Disables the given interrupt source */
void ECIA_GIRQSourceDisable(ECIA_INT_SOURCE int_src)
{
    uint32_t ecia_enclr_addr = ECIA_BASE_ADDRESS + ECIA_EN_CLR8_REG_OFST + (20U * GIRQ_REG_GET(int_src));
    uint32_t* ecia_enclr_ptr = (uint32_t*)(ecia_enclr_addr);
    *ecia_enclr_ptr = (1UL << GIRQ_BIT_POS_GET(int_src));
}

/* Returns true if interrupt for the given interrupt source is enabled, false otherwise */
bool ECIA_GIRQIsInterruptEnabled(ECIA_INT_SOURCE int_src)
{
    uint32_t ecia_enset_addr = ECIA_BASE_ADDRESS + ECIA_EN_SET8_REG_OFST + (20U * GIRQ_REG_GET(int_src));
    uint32_t* ecia_enset_ptr = (uint32_t*)(ecia_enset_addr);
    return ((*ecia_enset_ptr & (1UL << GIRQ_BIT_POS_GET(int_src))) > 0U) ? true : false;
}

/* Clears the given interrupt source */
void ECIA_GIRQSourceClear(ECIA_INT_SOURCE int_src)
{
    uint32_t ecia_src_addr = ECIA_BASE_ADDRESS + ECIA_SRC8_REG_OFST + (20U * GIRQ_REG_GET(int_src));
    uint32_t* ecia_src_ptr = (uint32_t*)ecia_src_addr;
    *ecia_src_ptr |= (1UL << GIRQ_BIT_POS_GET(int_src));
}

/* Clear all interrupt sources in all the ECIA blocks */
void ECIA_GIRQSourceClearAll(void)
{
    uint32_t i;
    uint32_t* ecia_src_ptr = (uint32_t*)(ECIA_BASE_ADDRESS + ECIA_SRC8_REG_OFST);

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
    uint32_t* ecia_enclr_ptr = (uint32_t*)(ECIA_BASE_ADDRESS + ECIA_EN_CLR8_REG_OFST);

    for (i = (uint32_t)ECIA_GIRQ_BLOCK_NUM8; i < (uint32_t)ECIA_GIRQ_BLOCK_NUM_MAX; i++)
    {
        *ecia_enclr_ptr = 0xFFFFFFFFUL;
        ecia_enclr_ptr += 5U;
    }
}

/* Returns the Result bit of the given ECIA_INT_SOURCE. This API may be used to know if interrupt is active */
uint8_t ECIA_GIRQResultGet(ECIA_INT_SOURCE int_src)
{
    uint32_t ecia_result_addr = ECIA_BASE_ADDRESS + ECIA_RESULT8_REG_OFST + (20U * GIRQ_REG_GET(int_src));
    uint32_t* ecia_result_ptr = (uint32_t*)ecia_result_addr;
    return ((*ecia_result_ptr & (1UL << GIRQ_BIT_POS_GET(int_src))) > 0U) ? 1U: 0U;
}

/* Enables both ECIA and NVIC interrupt */
void ECIA_InterruptEnable(ECIA_INT_SOURCE int_src)
{
    uint32_t nvic_int_num;
    uint32_t girq_block_num = (1UL << (GIRQ_REG_GET(int_src) + 8U));
    ECIA_GIRQSourceEnable(int_src);
    ECIA_GIRQBlockEnable((ECIA_GIRQ_BLOCK_NUM)girq_block_num);
    if (IS_INT_SRC_AGG_OR_DIR(int_src) == INT_SRC_IS_AGGREGATE)
    {
        nvic_int_num = GIRQ_AGG_INT_NUM_GET(int_src);
    }
    else
    {
        nvic_int_num = GIRQ_DIR_INT_NUM_GET(int_src);
    }
    NVIC_EnableIRQ((IRQn_Type)nvic_int_num);
}

void ECIA_InterruptDisable(ECIA_INT_SOURCE int_src)
{
    ECIA_GIRQSourceDisable(int_src);
}