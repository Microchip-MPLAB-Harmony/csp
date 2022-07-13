/*******************************************************************************
   PLIB MMU

  Company:
    Microchip Technology Inc.

  File Name:
    plib_mmu.c

  Summary:
    MMU implementation.

  Description:
    The MMU PLIB provies a simple interface to enable the MMU and caches.
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END

#include "device.h"

/* TTB descriptor type for Section descriptor */
#define TTB_TYPE_SECT              (2UL << 0U)

/* TTB Section Descriptor: Buffered/Non-Buffered (B) */
#define TTB_SECT_WRITE_THROUGH     (0UL << 2U)
#define TTB_SECT_WRITE_BACK        (1UL << 2U)

/* TTB Section Descriptor: Cacheable/Non-Cacheable (C) */
#define TTB_SECT_NON_CACHEABLE     (0UL << 3U)
#define TTB_SECT_CACHEABLE         (1UL << 3U)

#define TTB_SECT_STRONGLY_ORDERED  (TTB_SECT_NON_CACHEABLE | TTB_SECT_WRITE_THROUGH)
#define TTB_SECT_SHAREABLE_DEVICE  (TTB_SECT_NON_CACHEABLE | TTB_SECT_WRITE_BACK)
#define TTB_SECT_CACHEABLE_WT      (TTB_SECT_CACHEABLE | TTB_SECT_WRITE_THROUGH)
#define TTB_SECT_CACHEABLE_WB      (TTB_SECT_CACHEABLE | TTB_SECT_WRITE_BACK)

/* TTB Section Descriptor: Domain */
#define TTB_SECT_DOMAIN(x)         (((x) & 15U) << 5U)

/* TTB Section Descriptor: Execute/Execute-Never (XN) */
#define TTB_SECT_EXEC              (0UL << 4U)
#define TTB_SECT_EXEC_NEVER        (1UL << 4U)

/* TTB Section Descriptor: Access Privilege (AP) */
#define TTB_SECT_AP_PRIV_ONLY      ((0UL << 15U) | (1UL << 10U))
#define TTB_SECT_AP_NO_USER_WRITE  ((0UL << 15U) | (2UL << 10U))
#define TTB_SECT_AP_FULL_ACCESS    ((0UL << 15U) | (3UL << 10U))
#define TTB_SECT_AP_PRIV_READ_ONLY ((1UL << 15U) | (1UL << 10U))
#define TTB_SECT_AP_READ_ONLY      ((1UL << 15U) | (2UL << 10U))

/* TTB Section Descriptor: Section Base Address */
#define TTB_SECT_ADDR(x)           ((x) & 0xFFF00000U)
<#if DATA_CACHE_ENABLE>

#define L1_DATA_CACHE_BYTES            ${CACHE_ALIGN}U
#define L1_DATA_CACHE_WAYS         4U
#define L1_DATA_CACHE_SETS         256U
#define L1_DATA_CACHE_SETWAY(set, way) (((set)UL << 5U) | ((way)UL << 30U))
</#if>

__ALIGNED(16384) static uint32_t tlb[4096];

// *****************************************************************************
/* Function:
     void mmu_configure(void *tlb)

  Summary:
    Configure MMU by setting TTRB0 address.

*/
static void mmu_configure(void *p_tlb)
{
    /* Translation Table Base Register 0 */
    __set_TTBR0((uint32_t)(uint8_t*)p_tlb);

    /* Domain Access Register */
    /* only domain 15: access are not checked */
    __set_DACR(0xC0000000U);

    __DSB();
    __ISB();
}

<#if INSTRUCTION_CACHE_ENABLE>

void icache_InvalidateAll(void)
{
    L1C_InvalidateICacheAll();
}

void icache_Enable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if ((sctlr & SCTLR_I_Msk) == 0U)
    {
        L1C_InvalidateICacheAll();
        __set_SCTLR(sctlr | SCTLR_I_Msk);
    }
}

void icache_Disable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if ((sctlr & SCTLR_I_Msk) != 0U)
    {
        __set_SCTLR(sctlr & ~SCTLR_I_Msk);
        L1C_InvalidateICacheAll();
    }
}
</#if>

<#if DATA_CACHE_ENABLE>
void dcache_InvalidateAll(void)
{
    L1C_InvalidateDCacheAll();
}

void dcache_CleanAll(void)
{
    L1C_CleanDCacheAll();
}

void dcache_CleanInvalidateAll(void)
{
    L1C_CleanInvalidateDCacheAll();
}

void dcache_InvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        __set_DCIMVAC(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        __set_DCCMVAC(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanInvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        __set_DCCIMVAC((uint32_t)mva);
        __DMB();
    }
    __DSB();
}

void dcache_Enable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if ((sctlr & SCTLR_C_Msk) == 0U)
    {
        L1C_InvalidateDCacheAll();
        __set_SCTLR(sctlr | SCTLR_C_Msk);
    }
}

void dcache_Disable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if ((sctlr & SCTLR_C_Msk) != 0U)
    {
        L1C_CleanDCacheAll();
        __set_SCTLR(sctlr & ~SCTLR_C_Msk);
        L1C_InvalidateDCacheAll();
    }
}

</#if>

// *****************************************************************************
/* Function:
    void MMU_Initialize(void);

  Summary:
    Initialize and enable MMU.

  Description:
    Initialize the MMU with a flat address map (e.g. physical and virtual
    addresses are the same) and enable MMU and caches.

  Precondition:
    None.

  Parameters:
    None.

  Returns:
    None.
*/
void MMU_Initialize(void)
{
    uint32_t addr;

    /* Reset table entries */
    for (addr = 0U; addr < 4096U; addr++)
    {
        tlb[addr] = 0;
    }

<#list 0..MMU_SEG_COUNT - 1 as i>
<#assign SEG_START_ADDR = .vars["MMU_SEG" + i +"_START"]>
<#assign SEG_END_ADDR = .vars["MMU_SEG" + i +"_END"]>
<#assign SEG_LOOP = .vars["MMU_SEG" + i +"_LOOP"]>
<#assign SEG_DESC = .vars["MMU_SEG" + i + "_DESC"]>
<#assign RO_FLAG = .vars["MMU_SEG" + i +"_RO"]?string("TTB_SECT_AP_READ_ONLY", "TTB_SECT_AP_FULL_ACCESS")>
<#assign EXEC_FLAG = .vars["MMU_SEG" + i + "_EXEC"]?string("TTB_SECT_EXEC", "TTB_SECT_EXEC_NEVER")>
<#if .vars["MMU_SEG" + i + "_TYPE"] == "strongly-ordered">
<#assign TYPE_FLAG = "TTB_SECT_STRONGLY_ORDERED">
<#elseif .vars["MMU_SEG" + i + "_TYPE"] == "device">
<#assign TYPE_FLAG = "TTB_SECT_SHAREABLE_DEVICE">
<#else>
<#assign TYPE_FLAG = "TTB_SECT_CACHEABLE_WB">
</#if>
<#if SEG_LOOP>

    /* ${SEG_START_ADDR}00000: ${SEG_DESC} */
    for (addr = ${SEG_START_ADDR}U; addr < ${SEG_END_ADDR}U; addr++)
    {
        tlb[addr] = TTB_SECT_ADDR(addr << 20U)
                    | ${RO_FLAG}
                    | TTB_SECT_DOMAIN(0xFU)
                    | ${EXEC_FLAG}
                    | ${TYPE_FLAG}
                    | TTB_TYPE_SECT;
    }
<#else>

    /* ${SEG_START_ADDR}00000: ${SEG_DESC} */
    tlb[${SEG_START_ADDR}] = TTB_SECT_ADDR(${SEG_START_ADDR}00000U)
                  |  ${RO_FLAG}
                  | TTB_SECT_DOMAIN(0xFU)
                  | ${EXEC_FLAG}
                  | ${TYPE_FLAG}
                  | TTB_TYPE_SECT;
</#if>
</#list>

    /* ${DDRAM_NO_CACHE_START_ADDR}: DDR Chip Select */
    /* (${DRAM_COHERENT_REGION_SIZE}MB strongly ordered) */
    for (addr = ${DDRAM_NO_CACHE_START_ADDR?remove_ending("00000")}U; addr < ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}U; addr++)
    {
        tlb[addr] = TTB_SECT_ADDR(addr << 20)
                    | TTB_SECT_AP_FULL_ACCESS
                    | TTB_SECT_DOMAIN(0xfU)
                    | TTB_SECT_EXEC
                    | TTB_SECT_STRONGLY_ORDERED
                    | TTB_TYPE_SECT;
    }

    /*Remainder of the DRAM is configured as cacheable */
    for (addr = ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}U; addr < ${DDRAM_BOUNDARY_ADDR?remove_ending("00000")}U; addr++)
    {
        tlb[addr] = TTB_SECT_ADDR(addr << 20)
                    | TTB_SECT_AP_FULL_ACCESS
                    | TTB_SECT_DOMAIN(0xfU)
                    | TTB_SECT_EXEC
                    | TTB_SECT_CACHEABLE_WB
                    | TTB_TYPE_SECT;
    }

    /* Enable MMU, I-Cache and D-Cache */
    mmu_configure(tlb);
<#if INSTRUCTION_CACHE_ENABLE>
    icache_Enable();
</#if>
    MMU_Enable();
<#if DATA_CACHE_ENABLE>
    dcache_Enable();
</#if>
}
