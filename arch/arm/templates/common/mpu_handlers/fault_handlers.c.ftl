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
#include <stdint.h>
#include <stdbool.h>
<#if ADVANCED_EXCEPTION>
#include <stdio.h>
</#if>

void undefined_instruction_irq_handler (void);
void software_interrupt_irq_handler(void);
void data_abort_irq_handler(void);
void prefetch_abort_irq_handler(void);

<#if ADVANCED_EXCEPTION>
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.6 deviated 30 times.  Deviation record ID -  H3_MISRAC_2012_R_21_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    <#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
    </#if>
#pragma coverity compliance block deviate:30 "MISRA C-2012 Rule 21.6" "H3_MISRAC_2012_R_21_6_DR_1"
</#if>

#define READ_DFSR(x) asm("mrc p15, 0, %0, c5, c0, 0" : "=r"(x))
#define READ_DFAR(x) asm("mrc p15, 0, %0, c6, c0, 0" : "=r"(x))
#define READ_IFSR(x) asm("mrc p15, 0, %0, c5, c0, 1" : "=r"(x))
#define READ_IFAR(x) asm("mrc p15, 0, %0, c6, c0, 2" : "=r"(x))

<#if CoreArchitecture?matches("ARM926.*")>
static const char* prefetch_abort_status[16] = {
    NULL,
    NULL,
    "debug event",
    "access flag fault, section",
    NULL,
    "translation fault, section",
    "access flag fault, page",
    "translation fault, page",
    "synchronous external abort",
    "domain fault, section",
    NULL,
    "domain fault, page",
    "L1 translation, synchronous external abort",
    "permission fault, section",
    "L2 translation, synchronous external abort",
    "permission fault, page"
};

/* DFSR status */
static const char* data_abort_status[16] = {
    NULL,
    "alignment fault",
    "debug event",
    "access flag fault, section",
    "instruction cache maintenance fault",
    "translation fault, section",
    "access flag fault, page",
    "translation fault, page",
    "synchronous external abort, nontranslation",
    "domain fault, section",
    NULL,
    "domain fault, page",
    "1st level translation, synchronous external abort",
    "permission fault, section",
    "2nd level translation, synchronous external abort",
    "permission fault, page"
};
<#else>

/* IFSR status */
static const char* prefetch_abort_status[32] = {
    NULL,
    NULL,
    "debug event",
    "access flag fault, section",
    NULL,
    "translation fault, section",
    "access flag fault, page",
    "translation fault, page",
    "synchronous external abort",
    "domain fault, section",
    NULL,
    "domain fault, page",
    "L1 translation, synchronous external abort",
    "permission fault, section",
    "L2 translation, synchronous external abort",
    "permission fault, page",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};

/* DFSR status */
static const char* data_abort_status[32] = {
    NULL,
    "alignment fault",
    "debug event",
    "access flag fault, section",
    "instruction cache maintenance fault",
    "translation fault, section",
    "access flag fault, page",
    "translation fault, page",
    "synchronous external abort, nontranslation",
    "domain fault, section",
    NULL,
    "domain fault, page",
    "1st level translation, synchronous external abort",
    "permission fault, section",
    "2nd level translation, synchronous external abort",
    "permission fault, page",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    "asynchronous external abort",
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
};
</#if>

</#if>
void __attribute((weak, noreturn)) undefined_instruction_irq_handler (void)
{
    while(true)
    {
        /* Spin forever */
    }
}

void __attribute((weak, noreturn)) software_interrupt_irq_handler(void)
{
    while(true)
    {
        /* Spin forever */
    }
}

void __attribute((weak, noreturn)) data_abort_irq_handler(void)
{
<#if ADVANCED_EXCEPTION>
    uint32_t v1, v2, dfsr;

    READ_DFSR(v1);
    READ_DFAR(v2);

    (void)printf("\r\n");
    (void)printf("####################\r\n");
    dfsr = ((v1 >> 4U) & 0x0FU);
    (void)printf("Data Fault occured in %x domain\r\n", (unsigned int)dfsr);
<#if CoreArchitecture?matches("ARM926.*")>
    dfsr = ((v1 & 0x0FU));
<#else>
    dfsr = (((v1 & 0x400U) >> 6U) | (v1 & 0x0FU));
</#if>
    if (data_abort_status[dfsr] != NULL)
    {
        (void)printf("Data Fault reason is: %s\r\n", data_abort_status[dfsr]);
    }
    else
    {
        (void)printf("Data Fault reason is unknown\r\n");
    }
    (void)printf("Data Fault occured at address: 0x%08x\r\n", (unsigned int)v2);
    (void)printf("Data Fault status register value: 0x%x\r\n", (unsigned int)v1);
    (void)printf("####################\n\r");
</#if>
    while(true)
    {
        /* Spin forever */
    }
}

void __attribute((weak, noreturn)) prefetch_abort_irq_handler(void)
{
<#if ADVANCED_EXCEPTION>
    uint32_t v1, v2, ifsr;

    READ_IFSR(v1);
    READ_IFAR(v2);

    (void)printf("\r\n");
    (void)printf("####################\r\n");
<#if CoreArchitecture?matches("ARM926.*")>
    ifsr = (v1 & 0x0FU);
<#else>
    ifsr = (((v1 & 0x400U) >> 6U) | (v1 & 0x0FU));
</#if>
    if (prefetch_abort_status[ifsr] != NULL)
    {
        (void)printf("Prefetch Fault reason is: %s\r\n", prefetch_abort_status[ifsr]);
    }
    else
    {
        (void)printf("Prefetch Fault reason is unknown\r\n");
    }
    (void)printf("prefetch Fault occured at address: 0x%08x\r\n", (unsigned int)v2);
    (void)printf("Prefetch Fault status register value: 0x%x\r\n", (unsigned int)v1);
    (void)printf("####################\n\r");
</#if>
    while(true)
    {
        /* Spin forever */
    }
}

<#if ADVANCED_EXCEPTION>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma coverity compliance end_block "MISRA C-2012 Rule 21.6"
    <#if COMPILER_CHOICE == "XC32">
#pragma GCC diagnostic pop
    </#if>
</#if>
/* MISRAC 2012 deviation block end */
</#if>
