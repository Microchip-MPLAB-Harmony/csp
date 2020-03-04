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

#include "definitions.h" /* for potential custom handler names */
#include <stdbool.h>

/* Initialize segments */
extern const DeviceVectors __Vectors;

/* C library initialization routine */
extern void __main(void);

/* Declaration of Reset handler (may be custom) */
void Reset_Handler(void);

/* Device Vector information is available in interrupt.c file */

<#if CoreArchitecture == "CORTEX-M7">
<#include "arch/startup_keil_cortex_m7.c.ftl">
<#include "devices/startup_keil_${DeviceFamily}.c.ftl">
</#if>
<#if CoreArchitecture == "CORTEX-M4">
<#if FPU_Available>
<#include "arch/startup_keil_cortex_m4.c.ftl">
</#if>
<#if DATA_CACHE_ENABLE??>
<#include "devices/startup_keil_${DeviceFamily}.c.ftl">
</#if>
</#if>
/* Optional application-provided functions */
extern void __attribute__((weak)) _on_reset(void);
extern void __attribute__((weak)) _on_bootstrap(void);

/**
 * \brief This is the code that gets called on processor reset.
 * To initialize the device, and call the main() routine.
 */
void __attribute__((section(".text.Reset_Handler"))) Reset_Handler(void)
{
    uint32_t *pSrc;

    /* Call the optional application-provided _on_reset() function. */
    if (_on_reset)
    {
        _on_reset();
    }

<#if FPU_Available>
#if (__ARM_FP==14) || (__ARM_FP==4)
    /* Enable the FPU if the application is built with -mfloat-abi=softfp or -mfloat-abi=hard */
    FPU_Enable();
#endif
</#if>

<#if TCM_ENABLE??>
	TCM_Configure(${DEVICE_TCM_SIZE});
<#if TCM_ENABLE>
    /* Enable TCM   */
    TCM_Enable();
<#else>
    /* Disable TCM  */
    TCM_Disable();
</#if>
</#if>

#  ifdef SCB_VTOR_TBLOFF_Msk
    /*  Set the vector-table base address in FLASH */
    pSrc = (uint32_t *) &__Vectors;
    SCB->VTOR = ((uint32_t) pSrc & SCB_VTOR_TBLOFF_Msk);
#  endif /* SCB_VTOR_TBLOFF_Msk */

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

    /* Execute entry point to the C library initialization routine,
       which eventually executes application's main function */
    __main();

    /* Infinite loop */
    while (1) {}
}
