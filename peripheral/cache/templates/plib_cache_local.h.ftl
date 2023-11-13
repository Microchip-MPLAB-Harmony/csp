/*******************************************************************************
  PIC32MZ PLIB CACHE Localc Interface Definition

  Company:
    Microchip Technology Inc.

  File Name:
    plib_cache_local.h

  Summary:
    PIC32MZ CACHE local declarations and definitions.

  Description:
    This file contains the PLIB CACHE local declarations and definitions.
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


#ifndef PLIB_CACHE_LOCAL_H
#define PLIB_CACHE_LOCAL_H

#include "plib_cache.h"

// *****************************************************************************
// *****************************************************************************
// Section: Function prototypes of local functions
// *****************************************************************************
// *****************************************************************************
/* MISRAC 2012 deviation block start */
    /* MISRA C-2012 Rule 21.2 deviated in this file.  Deviation record ID - H3_MISRAC_2012_R_21_2_DR_20 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    <#if COMPILER_CHOICE == "XC32">
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    </#if>
    #pragma coverity compliance block deviate "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_20"

</#if>

void  __attribute__((far)) _pic32_init_cache (CACHE_COHERENCY cacheCoherency);
void  __attribute__((far)) _pic32_size_cache (void);

void  __attribute__((far)) _pic32_flush_cache (void);
void  __attribute__((far)) _pic32_flush_dcache (void);
void  __attribute__((far)) _pic32_flush_icache (void);

void  __attribute__((far)) _pic32_sync_icache (uint32_t addr, size_t len);

void  __attribute__((far)) _pic32_clean_cache (uint32_t addr, size_t len);
void  __attribute__((far)) _pic32_clean_dcache (uint32_t addr, size_t len);
void  __attribute__((far)) _pic32_clean_dcache_nowrite (uint32_t addr, size_t len);
void  __attribute__((far)) _pic32_clean_icache (uint32_t addr, size_t len);

void  __attribute__((far)) _pic32_lock_dcache (uint32_t addr, size_t len);
void  __attribute__((far)) _pic32_lock_icache (uint32_t addr, size_t len);

size_t  __attribute__((far)) _pic32_get_dcache_associativity (void);
size_t  __attribute__((far)) _pic32_get_icache_associativity (void);
size_t  __attribute__((far)) _pic32_get_dcache_linesize (void);
size_t  __attribute__((far)) _pic32_get_icache_linesize (void);
size_t  __attribute__((far)) _pic32_get_dcache_lines_per_way (void);
size_t  __attribute__((far)) _pic32_get_icache_lines_per_way (void);
size_t  __attribute__((far)) _pic32_get_dcache_size (void);
size_t  __attribute__((far)) _pic32_get_icache_size (void);

<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

    #pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
    <#if COMPILER_CHOICE == "XC32">
    #pragma GCC diagnostic pop
    </#if>
</#if>
    /* MISRAC 2012 deviation block end */

#endif //#ifndef PLIB_CACHE_LOCAL_H

/*******************************************************************************
 End of File
*/
