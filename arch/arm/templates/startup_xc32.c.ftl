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

#include "definitions.h" /* for potential custom handler names */
#include <libpic32c.h>
#include <sys/cdefs.h>
#include <stdbool.h>

/*
 *  The MPLAB X Simulator does not yet support simulation of programming the
 *  GPNVM bits yet. We can remove this once it supports the FRDY bit.
 */
#ifdef __MPLAB_DEBUGGER_SIMULATOR
#define __XC32_SKIP_STARTUP_GPNVM_WAIT
#endif

/*
 *  This startup code relies on features that are specific to the MPLAB XC32
 *  toolchain. Do not use it with other toolchains.
 */
#ifndef __XC32
#warning This startup code is intended for use with the MPLAB XC32 Compiler only.
#endif

/* Initialize segments */
extern uint32_t __svectors;

int main(void);
extern void __attribute__((long_call)) __libc_init_array(void);

/* Declaration of Reset handler (may be custom) */
void __attribute__((optimize("-O1"), long_call)) Reset_Handler(void);

/* Device Vector information is available in interrupt.c file */

<#if CoreArchitecture == "CORTEX-M7">
<#include "startup_xc32_cortex_m7.c.ftl">
<#include "startup_xc32_${DeviceFamily}.c.ftl">
</#if>


/* Optional application-provided functions */
extern void __attribute__((weak,long_call)) _on_reset(void);
extern void __attribute__((weak,long_call)) _on_bootstrap(void);

/* Reserved for use by the MPLAB XC32 Compiler */
extern void __attribute__((weak,long_call)) __xc32_on_reset(void);
extern void __attribute__((weak,long_call)) __xc32_on_bootstrap(void);


/**
 * \brief This is the code that gets called on processor reset.
 * To initialize the device, and call the main() routine.
 */
void __attribute__((optimize("-O1"), section(".text.Reset_Handler"), long_call)) Reset_Handler(void)
{
    uint32_t *pSrc;

    /* Call the optional application-provided _on_reset() function. */
    if (_on_reset)
    {
        _on_reset();
    }

    /* Reserved for use by MPLAB XC32. */
    if (__xc32_on_reset)
        __xc32_on_reset();

<#if FPU_Available>
#if (__ARM_FP==14) || (__ARM_FP==4)
    /* Enable the FPU if the application is built with -mfloat-abi=softfp or -mfloat-abi=hard */
    FPU_Enable();
#endif
</#if>

<#if TCM_ENABLE??>
<#if TCM_ENABLE>
	TCM_Configure(${DEVICE_TCM_SIZE});
    /* Enable TCM   */
    TCM_Enable();
<#else>
    /* Disable TCM  */
    TCM_Disable();
</#if>
</#if>

    /* Initialize data after TCM is enabled.
     * Data initialization from the XC32 .dinit template */
    __pic32c_data_initialization();
	
<#if STACK_IN_TCM??>	
<#if (STACK_IN_TCM)>
    /* Move the stack to Data Tightly Coupled Memory (DTCM) */
    __pic32c_TCM_StackInit();
</#if>
</#if>

#  ifdef SCB_VTOR_TBLOFF_Msk
    /*  Set the vector-table base address in FLASH */
    pSrc = (uint32_t *) & __svectors;
    SCB->VTOR = ((uint32_t) pSrc & SCB_VTOR_TBLOFF_Msk);
#  endif /* SCB_VTOR_TBLOFF_Msk */

    /* Initialize the C library */
    __libc_init_array();

<#if CoreUseMPU??>
<#if CoreUseMPU>
    /* Initialize MPU */
    MPU_Initialize();
</#if>
</#if>

<#if (INSTRUCTION_CACHE_ENABLE)??>
<#if (INSTRUCTION_CACHE_ENABLE)>
    /* Enable Instruction Cache */
    ICache_Enable();
</#if>
</#if>

<#if DATA_CACHE_ENABLE??>
<#if (DATA_CACHE_ENABLE)>
    /* Enable Data Cache    */
    DCache_Enable();
</#if>
</#if>

    /* Call the optional application-provided _on_bootstrap() function. */
    if (_on_bootstrap)
    {
        _on_bootstrap();
    }

    /* Reserved for use by MPLAB XC32. */
    if (__xc32_on_bootstrap)
    {
        __xc32_on_bootstrap();
    }

    /* Branch to application's main function */
    main();
<#if CoreArchitecture != "CORTEX-M0+">
#if (defined(__DEBUG) || defined(__DEBUG_D)) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
</#if>
    /* Infinite loop */
    while (1) {}
}
