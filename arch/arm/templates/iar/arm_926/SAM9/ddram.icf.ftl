define memory mem with size = 4G;
define region RAM_region           = mem:[from 0x00300000 to 0x0030FFFF];
define region DDRAM_NOCACHE_region = mem:[from ${DDRAM_NO_CACHE_START_ADDR} to ${DDRAM_NO_CACHE_END_ADDR}];
define region DDRAM_region         = mem:[from ${DDRAM_CACHE_START_ADDR} to ${DDRAM_CACHE_END_ADDR}];

<#lt><#assign HEAP_SIZE = IAR_HEAP_SIZE!"0x200">
<#lt><#assign USR_STACK_SIZE = IAR_USR_STACK_SIZE!"0x1000">
<#lt><#assign FIQ_STACK_SIZE = IAR_FIQ_STACK_SIZE!"0x60">
<#lt><#assign IRQ_STACK_SIZE = IAR_IRQ_STACK_SIZE!"0x60">
<#lt><#assign SVC_STACK_SIZE = IAR_SVC_STACK_SIZE!"0x1000">
<#lt><#assign ABT_STACK_SIZE = IAR_ABT_STACK_SIZE!"0x40">
<#lt><#assign UND_STACK_SIZE = IAR_UND_STACK_SIZE!"0x40">
<#lt><#if HEAP_SIZE != 0 >
define block HEAP      with alignment = 4, size = ${HEAP_SIZE}{};
<#lt></#if>
<#lt><#if USR_STACK_SIZE != 0 >
define block CSTACK    with alignment = 8, size = ${USR_STACK_SIZE}{};
<#lt></#if>
<#lt><#if FIQ_STACK_SIZE != 0 >
define block FIQ_STACK with alignment = 8, size = ${FIQ_STACK_SIZE}{};
<#lt></#if>
<#lt><#if IRQ_STACK_SIZE != 0 >
define block IRQ_STACK with alignment = 8, size = ${IRQ_STACK_SIZE}{};
<#lt></#if>
<#lt><#if SVC_STACK_SIZE != 0 >
define block SVC_STACK with alignment = 8, size = ${SVC_STACK_SIZE}{};
<#lt></#if>
<#lt><#if ABT_STACK_SIZE != 0 >
define block ABT_STACK with alignment = 8, size = ${ABT_STACK_SIZE}{};
<#lt></#if>
<#lt><#if UND_STACK_SIZE != 0 >
define block UND_STACK with alignment = 8, size = ${UND_STACK_SIZE}{};
<#lt></#if>

define block SRAM { section .region_sram  };
define block DDRAM { section .region_ddr };

/* Please see drivers/mm/cache.h for details on the "Cache-aligned" sections */
define block NO_CACHE { section .region_nocache };
define block CACHE_ALIGNED with alignment = 32 { section .region_cache_aligned };
define block CACHE_ALIGNED_CONST with alignment = 32 { section .region_cache_aligned_const };

initialize by copy with packing=none { section .vectors };
do not initialize { section .region_sram };
do not initialize { section .region_ddr };
do not initialize { section .region_nocache };
do not initialize { section .region_cache_aligned };

place at start of RAM_region { section .vectors };
place in RAM_region { block SRAM };

place at address 0x23f00000 { section .cstartup };
place in DDRAM_region { ro };
place in DDRAM_region { rw };
place in DDRAM_region { block CACHE_ALIGNED_CONST };
place in DDRAM_region { zi };
place in DDRAM_region { block CACHE_ALIGNED };
place in DDRAM_region { block DDRAM };
place in DDRAM_region { block HEAP };
place in DDRAM_region { block CSTACK };
place in DDRAM_region { block FIQ_STACK };
place in DDRAM_region { block IRQ_STACK };
place in DDRAM_region { block SVC_STACK };
place in DDRAM_region { block ABT_STACK };
place in DDRAM_region { block UND_STACK };

place in DDRAM_NOCACHE_region { block NO_CACHE };

<#if USE_THREADX_VECTORS>
place in DDRAM_region { last section FREE_MEM};
</#if>
