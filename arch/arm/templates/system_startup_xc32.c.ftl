/**
 * Copyright (c) 2016-2017 Microchip Technology Inc. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "arch/arm/device_${__PROCESSOR?lower_case}.h" /* for vectors structure and default handler names and CMSIS API */
<#if CoreUseMPU == true>
#include "arch/arch.h" /* for ARCH_CORE_MPU_Initialize() defintion */
#include "arch/arm/arm_cm_mpu.h"
</#if>
#include "system_definitions.h" /* for potential custom handler names */
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
     toolchain. Do not use it with other toolchains.
  */
#ifndef __XC32
#warning This startup code is intended for use with the MPLAB XC32 Compiler only.
#endif

/* Initialize segments */
extern uint32_t _sfixed;
extern uint32_t __svectors;
extern uint32_t _dinit_size;
extern uint32_t _dinit_addr;

int main(void);
extern void __attribute__((long_call)) __libc_init_array(void);

/* Declaration of Reset handler (may be custom) */
void <#if CoreUseCustomVector == true>
${CustomVectorName}
<#else>
Reset_Handler
</#if>(void) __attribute__((optimize("-O1"), long_call));

/* Device Vector information is available in system_interrupt.c file */

<#if CoreArchitecture == "CORTEX-M7">
<#include "system_startup_xc32_cortex_m7.c.ftl">
</#if>
<#include "system_startup_xc32_${DeviceFamily}.c.ftl">

/* Optional user-provided functions */
// extern void __attribute__((weak,long_call)) _on_reset(void); // Harmony: present in this file
extern void __attribute__((weak,long_call)) _on_bootstrap(void);

/**
 * This is the code that gets called at beginning of processor reset handler provided by XC32 startup code.
 * - Initializes the MPU regions
 */
static void _on_reset(void)
{
<#if CoreUseMPU == true>
    ARCH_CORE_MPU_Initialize();
</#if>
}

/**
 * \brief This is the code that gets called on processor reset.
 * To initialize the device, and call the main() routine.
 */
<#if CoreUseCustomVector == true>
void ${CustomVectorName}(void)
<#else>
void Reset_Handler(void)
</#if>
{
    uint32_t *pSrc;

    /* Call the optional user-provided _on_reset() function. */
    _on_reset();

#if (__ARM_FP==14)
    /* Enable the FPU iff the application is built with -mfloat-abi=softfp or -mfloat-abi=hard */
    fpu_enable();
#endif

#if !defined(__XC32_SKIP_CACHE_INIT)
    /* Enable Caches */
#  if (__ICACHE_PRESENT==1U)
    SCB_EnableICache();
#  endif
#  if (__DCACHE_PRESENT==1U)
    SCB_EnableDCache();
#  endif
#endif

    /* TCM config and init */
#if ((__ITCM_PRESENT==1) && (__DTCM_PRESENT==1))
#  ifdef __XC32_ENABLE_TCM
    TCM_ConfigureSize();
    TCM_Enable();
#  else
/*  Define the __XC32_SKIP_STARTUP_GPNVM preprocessor macro when you do not
 *  want this code to modify the GPNVM bits at runtime.
 *  Define the __XC32_SKIP_STARTUP_GPNVM_WAIT preprocessor macro when you do
 *  not want the code to poll the FRDY bit before continuing.
 */
#    if !defined(__XC32_SKIP_STARTUP_GPNVM)
    TCM_ConfigureNoSize();
#    endif /* !defined(__XC32_SKIP_STARTUP_GPNVM) */
    TCM_Disable();
#  endif /* __XC32_ENABLE_TCM */
#endif /* ((__ITCM_PRESENT==1) && (__DTCM_PRESENT==1)) */

    /* Initialize data after TCM is enabled */
    __pic32c_data_initialization();

#if defined(__XC32_STACK_IN_TCM)
    __pic32c_TCM_StackInit();
#endif

#if !defined(__XC32_SKIP_STARTUP_VTOR_INIT)
#  ifdef SCB_VTOR_TBLOFF_Msk
    /*  Set the vector-table base address. This may be in flash or TCM.
     *  The __svectors symbol is created by the XC32 linker.
     */
    pSrc = (uint32_t *) & __svectors;
    SCB->VTOR = ((uint32_t) pSrc & SCB_VTOR_TBLOFF_Msk);
#  endif /* SCB_VTOR_TBLOFF_Msk */
#endif /* __XC32_SKIP_STARTUP_VTOR_INIT */

    /* Initialize the C library */
    __libc_init_array();

    /* Call the optional application-provided _on_bootstrap() function. */
    if (_on_bootstrap)
    {
        _on_bootstrap();
    }

    /* Branch to main function */
    main();

#if defined(__DEBUG) || defined(__DEBUG_D)
    __builtin_software_breakpoint();
#endif
    /* Infinite loop */
    while (1) {}
}
