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

#ifndef TOOLCHAIN_SPECIFICS_H
#define TOOLCHAIN_SPECIFICS_H

<#if "XC32" == COMPILER_CHOICE>
    <#lt>#include <sys/types.h>

    <#lt>#define NO_INIT                        __attribute__((section(".no_init")))
    <#lt>#define SECTION(a)                     __attribute__((__section__(a)))

/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.1 deviated 13 times. Deviation record ID -  H3_MISRAC_2012_R_21_1_DR_3 */
/* MISRA C-2012 Rule 21.2 deviated 26 times. Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_3 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block \
   (deviate:13 "MISRA C-2012 Rule 21.1" "H3_MISRAC_2012_R_21_1_DR_3")\
   (deviate:26 "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_3")
</#if>
    <#lt>#ifndef   __ASM
    <#lt>    #define __ASM                      __asm__
    <#lt>#endif
    <#lt>#ifndef   __INLINE
    <#lt>    #define __INLINE                   __inline__
    <#lt>#endif
    <#lt>#ifndef   __STATIC_INLINE
    <#lt>    #define __STATIC_INLINE            static __inline__
    <#lt>#endif
    <#lt>#ifndef   __STATIC_FORCEINLINE
    <#lt>    #define __STATIC_FORCEINLINE       __attribute__((always_inline)) static __inline__
    <#lt>#endif
    <#lt>#ifndef   __NO_RETURN
    <#lt>    #define __NO_RETURN                __attribute__((__noreturn__))
    <#lt>#endif
    <#lt>#ifndef   __USED
    <#lt>    #define __USED                     __attribute__((used))
    <#lt>#endif
    <#lt>#ifndef   __WEAK
    <#lt>    #define __WEAK                     __attribute__((weak))
    <#lt>#endif
    <#lt>#ifndef   __PACKED
    <#lt>    #define __PACKED                   __attribute__((packed, aligned(1)))
    <#lt>#endif
    <#lt>#ifndef   __PACKED_STRUCT
    <#lt>    #define __PACKED_STRUCT            struct __attribute__((packed, aligned(1)))
    <#lt>#endif
    <#lt>#ifndef   __PACKED_UNION
    <#lt>    #define __PACKED_UNION             union __attribute__((packed, aligned(1)))
    <#lt>#endif
    <#lt>#ifndef   __COHERENT
    <#lt>    #define __COHERENT                 __attribute__((coherent))
    <#lt>#endif
    <#lt>#ifndef   __ALIGNED
    <#lt>    #define __ALIGNED(x)               __attribute__((aligned(x)))
    <#lt>#endif
    <#lt>#ifndef   __RESTRICT
    <#lt>    #define __RESTRICT                 __restrict__
    <#lt>#endif

    <#if CACHE_ALIGN?? >
        <#lt>#define CACHE_LINE_SIZE                (${CACHE_ALIGN}u)
        <#lt>#define CACHE_ALIGN                    __COHERENT
    <#else>
        <#lt>#define CACHE_LINE_SIZE                (4u)
        <#lt>#define CACHE_ALIGN
    </#if>

    <#lt>#define CACHE_ALIGNED_SIZE_GET(size)     (size + ((size % CACHE_LINE_SIZE)? (CACHE_LINE_SIZE - (size % CACHE_LINE_SIZE)) : 0))

    <#lt>#ifndef FORMAT_ATTRIBUTE
    <#lt>   #define FORMAT_ATTRIBUTE(archetype, string_index, first_to_check)  __attribute__ ((format (archetype, string_index, first_to_check)))
    <#lt>#endif
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma coverity compliance end_block "MISRA C-2012 Rule 21.1" "MISRA C-2012 Rule 21.2"
#pragma GCC diagnostic pop
</#if>
</#if>

#endif // end of header

