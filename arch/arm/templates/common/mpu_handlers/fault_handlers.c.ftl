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
<#if ADVANCED_EXCEPTION>
#include <stdio.h>
#include <stdint.h>

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
    "permission fault, page"
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
    "asynchronous external abort"
};

</#if>
void __attribute((weak, noreturn)) undefined_instruction_irq_handler (void)
{
    while(1)
    {
        // Do Nothing
    }
}

void __attribute((weak, noreturn)) software_interrupt_irq_handler(void)
{
    while(1)
    {
        // Do Nothing
    }
}

void __attribute((weak, noreturn)) data_abort_irq_handler(void)
{
<#if ADVANCED_EXCEPTION>
    uint32_t v1, v2, dfsr;

    asm("mrc p15, 0, %0, c5, c0, 0" : "=r"(v1));
    asm("mrc p15, 0, %0, c6, c0, 0" : "=r"(v2));

    printf("\r\n");
    printf("####################\r\n");
    dfsr = ((v1 >> 4U) & 0x0FU);
    printf("Data Fault occured in %x domain\r\n", (unsigned int)dfsr);
    dfsr = (((v1 & 0x400U) >> 6U) | (v1 & 0x0FU));
    if (data_abort_status[dfsr])
    {
        printf("Data Fault reason is: %s\r\n", data_abort_status[dfsr]);
    }
    else
    {
        printf("Data Fault reason is unknown\r\n");
    }
    printf("Data Fault occured at address: 0x%08x\r\n", (unsigned int)v2);
    printf("Data Fault status register value: 0x%x\r\n", (unsigned int)v1);
    printf("####################\n\r");
</#if>
    while(1)
    {
        // Do Nothing
    }
}

void __attribute((weak, noreturn)) prefetch_abort_irq_handler(void)
{
<#if ADVANCED_EXCEPTION>
    uint32_t v1, v2, ifsr;

    asm("mrc p15, 0, %0, c5, c0, 1" : "=r"(v1));
    asm("mrc p15, 0, %0, c6, c0, 2" : "=r"(v2));

    printf("\r\n");
    printf("####################\r\n");
    ifsr = (((v1 & 0x400U) >> 6U) | (v1 & 0x0FU));
    if (prefetch_abort_status[ifsr])
    {
        printf("Prefetch Fault reason is: %s\r\n", prefetch_abort_status[ifsr]);
    }
    else
    {
        printf("Prefetch Fault reason is unknown\r\n");
    }
    printf("prefetch Fault occured at address: 0x%08x\r\n", (unsigned int)v2);
    printf("Prefetch Fault status register value: 0x%x\r\n", (unsigned int)v1);
    printf("####################\n\r");
</#if>
    while(1)
    {
        // Do Nothing
    }
}
