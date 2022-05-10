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
Copyright (c) 2019 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
*******************************************************************************/
// DOM-IGNORE-END

#include "device.h"
#include "peripheral/mmu/cp15.h"

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

/* TTB Section Descriptor: Should-Be-One (SBO) */
#define TTB_SECT_SBO               (1UL << 4U)

/* TTB Section Descriptor: Access Privilege (AP) */
#define TTB_SECT_AP_PRIV_ONLY      (1UL << 10U)
#define TTB_SECT_AP_NO_USER_WRITE  (2UL << 10U)
#define TTB_SECT_AP_FULL_ACCESS    (3UL << 10U)

/* TTB Section Descriptor: Section Base Address */
#define TTB_SECT_ADDR(x)           ((x) & 0xFFF00000U)
<#if DATA_CACHE_ENABLE>
/* L1 data cache line size, Number of ways and Number of sets */
#define L1_DATA_CACHE_BYTES        32U
#define L1_DATA_CACHE_WAYS         4U
#define L1_DATA_CACHE_SETS         256U
#define L1_DATA_CACHE_SETWAY(set, way) (((set) << 5) | ((way) << 30))
</#if>

__ALIGNED(16384) static uint32_t trns_tbl[4096];

// *****************************************************************************
/* Function:
     void mmu_configure(void *trns_tbl)

  Summary:
    Configure MMU by setting TTRB0 address.

*/
static void mmu_configure(void *p_trns_tbl)
{
    /* Translation Table Base Register 0 */
    cp15_write_ttbr0((uint32_t)((uint8_t*)p_trns_tbl));

    /* Domain Access Register */
    /* only domain 15: access are not checked */
    cp15_write_dacr(0xC0000000U);

    __DSB();
    __ISB();
}

// *****************************************************************************
/* Function:
     void mmu_enable(void)

  Summary:
    Enable the MMU.

*/
static void mmu_enable(void)
{
    uint32_t control;

    control = cp15_read_sctlr();
    if ((control & CP15_SCTLR_M) == 0U)
    {
        cp15_write_sctlr(control | CP15_SCTLR_M);
    }
}

<#if INSTRUCTION_CACHE_ENABLE>
void icache_InvalidateAll(void)
{
    cp15_icache_invalidate();
    __ISB();
}

void icache_Enable(void)
{
    uint32_t sctlr = cp15_read_sctlr();
    if ((sctlr & CP15_SCTLR_I) == 0U)
    {
        icache_InvalidateAll();
        cp15_write_sctlr(sctlr | CP15_SCTLR_I);
    }
}

void icache_Disable(void)
{
    uint32_t sctlr = cp15_read_sctlr();
    if ((sctlr & CP15_SCTLR_I) != 0U)
    {
        cp15_write_sctlr(sctlr & ~CP15_SCTLR_I);
        icache_InvalidateAll();
    }
}
</#if>

<#if DATA_CACHE_ENABLE>
void dcache_InvalidateAll(void)
{
    uint32_t set, way;

    for (way = 0U; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0U; set < L1_DATA_CACHE_SETS; set++)
        {
            cp15_dcache_invalidate_setway(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_CleanAll(void)
{
    uint32_t set, way;

    for (way = 0U; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0U; set < L1_DATA_CACHE_SETS; set++)
        {
            cp15_dcache_clean_setway(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_CleanInvalidateAll(void)
{
    uint32_t set, way;

    for (way = 0U; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0U; set < L1_DATA_CACHE_SETS; set++)
        {
            cp15_dcache_clean_invalidate_setway(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_InvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        cp15_dcache_invalidate_mva(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        cp15_dcache_clean_mva(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanInvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1U);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        cp15_dcache_clean_invalidate_mva((uint32_t)mva);
        __DMB();
    }
    __DSB();
}

void dcache_Enable(void)
{
    uint32_t sctlr = cp15_read_sctlr();
    if ((sctlr & CP15_SCTLR_C) == 0U)
    {
        dcache_InvalidateAll();
        cp15_write_sctlr(sctlr | CP15_SCTLR_C);
    }
}

void dcache_Disable(void)
{
    uint32_t sctlr = cp15_read_sctlr();
    if ((sctlr & CP15_SCTLR_C) != 0U)
    {
        dcache_CleanAll();
        cp15_write_sctlr(sctlr & ~CP15_SCTLR_C);
        dcache_InvalidateAll();
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
    for (addr = 0U; addr < 4096U; addr++) {
        trns_tbl[addr] = 0;
    }

<#list 0..MMU_SEG_COUNT - 1 as i>
<#assign SEG_START_ADDR = .vars["MMU_SEG" + i +"_START"]>
<#assign SEG_END_ADDR = .vars["MMU_SEG" + i +"_END"]>
<#assign SEG_LOOP = .vars["MMU_SEG" + i +"_LOOP"]>
<#assign SEG_DESC = .vars["MMU_SEG" + i + "_DESC"]>
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
        trns_tbl[addr] = TTB_SECT_ADDR(addr << 20U)
                    | TTB_SECT_AP_FULL_ACCESS
                    | TTB_SECT_DOMAIN(0xFU)
                    | ${TYPE_FLAG}
                    | TTB_SECT_SBO
                    | TTB_TYPE_SECT;
    }
<#else>

    /* ${SEG_START_ADDR}00000: ${SEG_DESC} */
    trns_tbl[${SEG_START_ADDR}] = TTB_SECT_ADDR(${SEG_START_ADDR}00000U)
                  | TTB_SECT_AP_FULL_ACCESS
                  | TTB_SECT_DOMAIN(0xFU)
                  | ${TYPE_FLAG}
                  | TTB_SECT_SBO
                  | TTB_TYPE_SECT;
</#if>
</#list>

    /* ${DDRAM_NO_CACHE_START_ADDR}: DDR Chip Select */
    /* (${DRAM_COHERENT_REGION_SIZE}MB strongly ordered) */
    for (addr = ${DDRAM_NO_CACHE_START_ADDR?remove_ending("00000")}U; addr < ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}U; addr++)
    {
            trns_tbl[addr] = TTB_SECT_ADDR(addr << 20)
                      | TTB_SECT_AP_FULL_ACCESS
                      | TTB_SECT_DOMAIN(0xfu)
                      | TTB_SECT_STRONGLY_ORDERED
                      | TTB_SECT_SBO
                      | TTB_TYPE_SECT;
    }

    /* Remainder of the DRAM is configured as cacheable */
    for (addr = ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}U; addr < ${DDRAM_BOUNDARY_ADDR?remove_ending("00000")}U; addr++)
    {
            trns_tbl[addr] = TTB_SECT_ADDR(addr << 20)
                      | TTB_SECT_AP_FULL_ACCESS
                      | TTB_SECT_DOMAIN(0xfu)
                      | TTB_SECT_CACHEABLE_WB
                      | TTB_SECT_SBO
                      | TTB_TYPE_SECT;
    }

    /* Enable MMU, I-Cache and D-Cache */
    mmu_configure(trns_tbl);
<#if INSTRUCTION_CACHE_ENABLE>
    icache_Enable();
</#if>
    mmu_enable();
<#if DATA_CACHE_ENABLE>
    dcache_Enable();
</#if>

    // disable the processor alignment fault testing
    uint32_t sctlrValue = cp15_read_sctlr();
    sctlrValue &= ~0x00000002U;
    cp15_write_sctlr( sctlrValue );
}
