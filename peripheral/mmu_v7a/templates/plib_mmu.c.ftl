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
#define TTB_TYPE_SECT              (2 << 0)

/* TTB Section Descriptor: Buffered/Non-Buffered (B) */
#define TTB_SECT_WRITE_THROUGH     (0 << 2)
#define TTB_SECT_WRITE_BACK        (1 << 2)

/* TTB Section Descriptor: Cacheable/Non-Cacheable (C) */
#define TTB_SECT_NON_CACHEABLE     (0 << 3)
#define TTB_SECT_CACHEABLE         (1 << 3)

#define TTB_SECT_STRONGLY_ORDERED  (TTB_SECT_NON_CACHEABLE | TTB_SECT_WRITE_THROUGH)
#define TTB_SECT_SHAREABLE_DEVICE  (TTB_SECT_NON_CACHEABLE | TTB_SECT_WRITE_BACK)
#define TTB_SECT_CACHEABLE_WT      (TTB_SECT_CACHEABLE | TTB_SECT_WRITE_THROUGH)
#define TTB_SECT_CACHEABLE_WB      (TTB_SECT_CACHEABLE | TTB_SECT_WRITE_BACK)

/* TTB Section Descriptor: Domain */
#define TTB_SECT_DOMAIN(x)         (((x) & 15) << 5)

/* TTB Section Descriptor: Execute/Execute-Never (XN) */
#define TTB_SECT_EXEC              (0 << 4)
#define TTB_SECT_EXEC_NEVER        (1 << 4)

/* TTB Section Descriptor: Access Privilege (AP) */
#define TTB_SECT_AP_PRIV_ONLY      ((0 << 15) | (1 << 10))
#define TTB_SECT_AP_NO_USER_WRITE  ((0 << 15) | (2 << 10))
#define TTB_SECT_AP_FULL_ACCESS    ((0 << 15) | (3 << 10))
#define TTB_SECT_AP_PRIV_READ_ONLY ((1 << 15) | (1 << 10))
#define TTB_SECT_AP_READ_ONLY      ((1 << 15) | (2 << 10))

/* TTB Section Descriptor: Section Base Address */
#define TTB_SECT_ADDR(x)           ((x) & 0xFFF00000)
<#if DATA_CACHE_ENABLE>
/* L1 data cache line size, Number of ways and Number of sets */
#define L1_DATA_CACHE_BYTES        32U
#define L1_DATA_CACHE_WAYS         4U
#define L1_DATA_CACHE_SETS         256U
#define L1_DATA_CACHE_SETWAY(set, way) (((set) << 5) | ((way) << 30))
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
    __set_TTBR0((uint32_t)p_tlb);

    /* Domain Access Register */
    /* only domain 15: access are not checked */
    __set_DACR(0xC0000000);

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

    control = __get_SCTLR();
    if ((control & SCTLR_M_Msk) == 0)
        __set_SCTLR(control | SCTLR_M_Msk);
}

<#if INSTRUCTION_CACHE_ENABLE>
void icache_InvalidateAll(void)
{
    __set_ICIALLU(0);
    __ISB();
}

void icache_Enable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if ((sctlr & SCTLR_I_Msk) == 0)
    {
        icache_InvalidateAll();
        __set_SCTLR(sctlr | SCTLR_I_Msk);
    }
}

void icache_Disable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if (sctlr & SCTLR_I_Msk)
    {
        __set_SCTLR(sctlr & ~SCTLR_I_Msk);
        icache_InvalidateAll();
    }
}
</#if>

<#if DATA_CACHE_ENABLE>
void dcache_InvalidateAll(void)
{
    uint32_t set, way;

    for (way = 0; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0; set < L1_DATA_CACHE_SETS; set++)
        {
            __set_DCISW(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_CleanAll(void)
{
    uint32_t set, way;

    for (way = 0; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0; set < L1_DATA_CACHE_SETS; set++)
        {
            __set_DCCSW(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_CleanInvalidateAll(void)
{
    uint32_t set, way;

    for (way = 0; way < L1_DATA_CACHE_WAYS; way++)
    {
        for (set = 0; set < L1_DATA_CACHE_SETS; set++)
        {
            __set_DCCISW(L1_DATA_CACHE_SETWAY(set, way));
        }
    }
    __DSB();
}

void dcache_InvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        __set_DCIMVAC(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1);

    for ( ; mva < ((uint32_t)addr + size); mva += L1_DATA_CACHE_BYTES)
    {
        __set_DCCMVAC(mva);
        __DMB();
    }
    __DSB();
}

void dcache_CleanInvalidateByAddr (uint32_t *addr, uint32_t size)
{
    uint32_t mva = (uint32_t)addr & ~(L1_DATA_CACHE_BYTES - 1);

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
    if ((sctlr & SCTLR_C_Msk) == 0)
    {
        dcache_InvalidateAll();
        __set_SCTLR(sctlr | SCTLR_C_Msk);
    }
}

void dcache_Disable(void)
{
    uint32_t sctlr = __get_SCTLR();
    if (sctlr & SCTLR_C_Msk)
    {
        dcache_CleanAll();
        __set_SCTLR(sctlr & ~SCTLR_C_Msk);
        dcache_InvalidateAll();
    }
}

</#if>

static inline uint32_t cp15_read_sctlr(void)
{
    uint32_t sctlr = 0;
    asm("mrc p15, 0, %0, c1, c0, 0" : "=r"(sctlr));
    return sctlr;
}

static inline void cp15_write_sctlr(uint32_t value)
{
    asm("mcr p15, 0, %0, c1, c0, 0" :: "r"(value));
}

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
    for (addr = 0; addr < 4096; addr++)
        tlb[addr] = 0;

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
    for (addr = ${SEG_START_ADDR}; addr < ${SEG_END_ADDR}; addr++)
    {
        tlb[addr] = TTB_SECT_ADDR(addr << 20U)
                    | ${RO_FLAG}
                    | TTB_SECT_DOMAIN(0xF)
                    | ${EXEC_FLAG}
                    | ${TYPE_FLAG}
                    | TTB_TYPE_SECT;
    }
<#else>

    /* ${SEG_START_ADDR}00000: ${SEG_DESC} */
    tlb[${SEG_START_ADDR}] = TTB_SECT_ADDR(${SEG_START_ADDR}00000)
                  |  ${RO_FLAG}
                  | TTB_SECT_DOMAIN(0xF)
                  | ${EXEC_FLAG}
                  | ${TYPE_FLAG}
                  | TTB_TYPE_SECT; 
</#if>
</#list>

    /* ${DDRAM_NO_CACHE_START_ADDR}: DDR Chip Select */
    /* (${DRAM_COHERENT_REGION_SIZE}MB strongly ordered) */
    for (addr = ${DDRAM_NO_CACHE_START_ADDR?remove_ending("00000")}; addr < ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}; addr++)
        tlb[addr] = TTB_SECT_ADDR(addr << 20)
                      | TTB_SECT_AP_FULL_ACCESS
                      | TTB_SECT_DOMAIN(0xf)
                      | TTB_SECT_EXEC
                      | TTB_SECT_STRONGLY_ORDERED
                      | TTB_TYPE_SECT;

    /*Remainder of the DRAM is configured as cacheable */          
    for (addr = ${DDRAM_CACHE_START_ADDR?remove_ending("00000")}; addr < ${DDRAM_BOUNDARY_ADDR?remove_ending("00000")}; addr++)
        tlb[addr] = TTB_SECT_ADDR(addr << 20)
                      | TTB_SECT_AP_FULL_ACCESS
                      | TTB_SECT_DOMAIN(0xf)
                      | TTB_SECT_EXEC
                      | TTB_SECT_CACHEABLE_WB
                      | TTB_TYPE_SECT;

    /* Enable MMU, I-Cache and D-Cache */
    mmu_configure(tlb);
<#if INSTRUCTION_CACHE_ENABLE>
    icache_Enable();
</#if>
    mmu_enable();
<#if DATA_CACHE_ENABLE>
    dcache_Enable();
</#if>

    // disable the processor alignment fault testing
    uint32_t sctlrValue = cp15_read_sctlr();
    sctlrValue &= ~0x00000002;
    cp15_write_sctlr( sctlrValue );
}
