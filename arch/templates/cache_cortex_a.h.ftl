/*******************************************************************************
  L1, L2 Cache Header

  File Name:
    cache_cortex_a.h

  Summary:
    Preprocessor definitions to provide L1 and L2 Cache control.

  Description:
    An MPLAB PLIB or Project can include this header to perform cache cleans,
    invalidates etc. For the DCache and ICache.

  Remarks:
    This header should not define any prototypes or data definitions, or
    include any files that do.  The file only provides macro definitions for
    build-time.

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
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*******************************************************************************/
// DOM-IGNORE-END

#ifndef CACHE_CORTEX_A_H
#define CACHE_CORTEX_A_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/*  This section Includes other configuration headers necessary to completely
    define this configuration.
*/

<#if __PROCESSOR?matches("ATSAMA5.*")>
<#if L2CC_ENABLE == true >
#include <stdint.h>
#include "peripheral/l2cc/plib_l2cc.h"
</#if>
<#if INSTRUCTION_CACHE_ENABLE == true || DATA_CACHE_ENABLE == true>
#include "peripheral/mmu/plib_mmu.h"
</#if>
</#if>

// DOM-IGNORE-BEGIN
#ifdef __cplusplus  // Provide C++ Compatibility

extern "C" {

#endif
// DOM-IGNORE-END

// *****************************************************************************
// *****************************************************************************
// Section: L1, L2 Cache Configuration
// *****************************************************************************
// *****************************************************************************
<#if INSTRUCTION_CACHE_ENABLE == true>
    <#lt>#define L1_ICACHE_IN_USE                               true
    <#lt>#define L1_ICACHE_ENABLE()                             icache_Enable()
    <#lt>#define L1_ICACHE_DISABLE()                            icache_Disable()
    <#lt>#define L1_ICACHE_INVALIDATE_ALL()                     icache_InvalidateAll()
<#else>
    <#lt>#define L1_ICACHE_IN_USE                               false
    <#lt>#define L1_ICACHE_ENABLE()
    <#lt>#define L1_ICACHE_DISABLE()
    <#lt>#define L1_ICACHE_INVALIDATE_ALL()
</#if>

<#if DATA_CACHE_ENABLE == true>
    <#lt>#define L1_DCACHE_IN_USE                               true
    <#lt>#define L1_DCACHE_ENABLE()                             dcache_Enable()
    <#lt>#define L1_DCACHE_DISABLE()                            dcache_Disable()
    <#lt>#define L1_DCACHE_CLEAN_ALL()                          dcache_CleanAll()
    <#lt>#define L1_DCACHE_INVALIDATE_ALL()                     dcache_InvalidateAll()
    <#lt>#define L1_DCACHE_CLEAN_INVALIDATE_ALL()               dcache_CleanInvalidateAll()

    <#-- L1 data cache must be enabled for L2 data cache to exist -->
    <#if L2CC_ENABLE == true>
        <#lt>#define L2_DCACHE_IN_USE                               true
        <#lt>#define L2_DCACHE_CLEAN_ALL()                          PLIB_L2CC_CleanCache()
        <#lt>#define L2_DCACHE_INVALIDATE_BY_ADDR(addr,sz)          PLIB_L2CC_InvalidateCacheByAddr(addr,sz)
        <#lt>//
        <#lt>#define DCACHE_CLEAN_BY_ADDR(addr,sz)                  dcache_CleanByAddr(addr,sz);\
        <#lt>                                                       PLIB_L2CC_CleanCacheByAddr(addr,sz)
        <#lt>#define DCACHE_INVALIDATE_BY_ADDR(addr,sz)             PLIB_L2CC_InvalidateCacheByAddr(addr,sz);\
        <#lt>                                                       dcache_InvalidateByAddr(addr,sz)
        <#lt>#define DCACHE_CLEAN_INVALIDATE_BY_ADDR(addr,sz)       dcache_CleanInvalidateByAddr(addr,sz);\
        <#lt>                                                       PLIB_L2CC_CleanInvalidateCacheByAddr(addr,sz)
        <#lt>#define DCACHE_CLEAN_ALL()                             dcache_CleanAll();\
        <#lt>                                                       PLIB_L2CC_CleanCache()
        <#lt>#define DCACHE_INVALIDATE_ALL()                        PLIB_L2CC_InvalidateCache();\
        <#lt>                                                       dcache_InvalidateAll()
        <#lt>#define DCACHE_CLEAN_INVALIDATE_ALL()                  dcache_CleanInvalidateAll();\
        <#lt>                                                       PLIB_L2CC_CleanInvalidateCache()
        <#lt>//
        <#lt>#define DATA_CACHE_ENABLED                             true
    <#else>
        <#lt>#define L2_DCACHE_IN_USE                               false
        <#lt>#define L2_DCACHE_CLEAN_ALL()
        <#lt>#define L2_DCACHE_INVALIDATE_BY_ADDR(addr,sz)
        <#lt>//
        <#lt>#define DCACHE_CLEAN_BY_ADDR(addr,sz)                  dcache_CleanByAddr(addr,sz)
        <#lt>#define DCACHE_INVALIDATE_BY_ADDR(addr,sz)             dcache_InvalidateByAddr(addr,sz)
        <#lt>#define DCACHE_CLEAN_INVALIDATE_BY_ADDR(addr,sz)       dcache_CleanInvalidateByAddr(addr,sz)
        <#lt>#define DCACHE_CLEAN_ALL()                             dcache_CleanAll()
        <#lt>#define DCACHE_INVALIDATE_ALL()                        dcache_InvalidateAll()
        <#lt>#define DCACHE_CLEAN_INVALIDATE_ALL()                  dcache_CleanInvalidateAll()
        <#lt>//
        <#lt>#define DATA_CACHE_ENABLED                             false
    </#if>
<#else>
    <#lt>#define L1_DCACHE_IN_USE                               false
    <#lt>#define L1_DCACHE_ENABLE()
    <#lt>#define L1_DCACHE_DISABLE()
    <#lt>#define L1_DCACHE_CLEAN_ALL()
    <#lt>#define L1_DCACHE_INVALIDATE_ALL()
    <#lt>#define L1_DCACHE_CLEAN_INVALIDATE_ALL()

    <#lt>#define L2_DCACHE_IN_USE                               false
    <#lt>#define L2_DCACHE_CLEAN_ALL()
    <#lt>#define L2_DCACHE_INVALIDATE_BY_ADDR(addr,sz)
    <#lt>//
    <#lt>#define DCACHE_CLEAN_BY_ADDR(addr,sz)
    <#lt>#define DCACHE_INVALIDATE_BY_ADDR(addr,sz)
    <#lt>#define DCACHE_CLEAN_INVALIDATE_BY_ADDR(addr,sz)
    <#lt>#define DCACHE_CLEAN_ALL()
    <#lt>#define DCACHE_INVALIDATE_ALL()
    <#lt>#define DCACHE_CLEAN_INVALIDATE_ALL()
    <#lt>//
    <#lt>#define DATA_CACHE_ENABLED                             false
</#if>

//DOM-IGNORE-BEGIN
#ifdef __cplusplus
}
#endif
//DOM-IGNORE-END

#endif // end of header
