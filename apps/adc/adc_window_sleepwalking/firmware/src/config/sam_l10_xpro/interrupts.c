/*******************************************************************************
 System Interrupts File

  Company:
    Microchip Technology Inc.

  File Name:
    interrupt.c

  Summary:
    Interrupt vectors mapping

  Description:
    This file maps all the interrupt vectors to their corresponding
    implementations. If a particular module interrupt is used, then its ISR
    definition can be found in corresponding PLIB source file. If a module
    interrupt is not used, then its ISR implementation is mapped to dummy
    handler.
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

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************

#include "definitions.h"

// *****************************************************************************
// *****************************************************************************
// Section: System Interrupt Vector Functions
// *****************************************************************************
// *****************************************************************************

extern uint32_t _stack;

/* Brief default interrupt handler for unused IRQs.*/
void __attribute__((optimize("-O1"),section(".text.Dummy_Handler"),long_call))Dummy_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
    while (1)
    {
    }
}
/* Device vectors list dummy definition*/
void Reset_Handler              ( void ) __attribute__((weak, alias("Dummy_Handler")));
void NonMaskableInt_Handler     ( void ) __attribute__((weak, alias("Dummy_Handler")));
void HardFault_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SVCall_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PendSV_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SysTick_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SYSTEM_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void WDT_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void RTC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EIC_EXTINT_0_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EIC_EXTINT_1_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EIC_EXTINT_2_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EIC_EXTINT_3_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EIC_OTHER_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FREQM_Handler              ( void ) __attribute__((weak, alias("Dummy_Handler")));
void NVMCTRL_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PORT_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DMAC_0_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DMAC_1_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DMAC_2_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DMAC_3_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DMAC_OTHER_Handler         ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EVSYS_0_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EVSYS_1_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EVSYS_2_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EVSYS_3_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EVSYS_NSCHK_Handler        ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PAC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM0_0_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM0_1_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM0_2_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM0_OTHER_Handler      ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM1_0_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM1_1_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM1_2_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM1_OTHER_Handler      ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM2_0_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM2_1_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM2_2_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SERCOM2_OTHER_Handler      ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC0_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC1_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC2_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void ADC_OTHER_InterruptHandler ( void ) __attribute__((weak, alias("Dummy_Handler")));
void ADC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void AC_Handler                 ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DAC_UNDERRUN_A_Handler     ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DAC_EMPTY_Handler          ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PTC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TRNG_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TRAM_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));



/* Mutiple handlers for vector */



__attribute__ ((section(".vectors")))
const DeviceVectors exception_table=
{
    /* Configure Initial Stack Pointer, using linker-generated symbols */
    .pvStack = (void*) (&_stack),

    .pfnReset_Handler              = ( void * ) Reset_Handler,
    .pfnNonMaskableInt_Handler     = ( void * ) NonMaskableInt_Handler,
    .pfnHardFault_Handler          = ( void * ) HardFault_Handler,
    .pfnSVCall_Handler             = ( void * ) SVCall_Handler,
    .pfnPendSV_Handler             = ( void * ) PendSV_Handler,
    .pfnSysTick_Handler            = ( void * ) SysTick_Handler,
    .pfnSYSTEM_Handler             = ( void * ) SYSTEM_Handler,
    .pfnWDT_Handler                = ( void * ) WDT_Handler,
    .pfnRTC_Handler                = ( void * ) RTC_Handler,
    .pfnEIC_EXTINT_0_Handler       = ( void * ) EIC_EXTINT_0_Handler,
    .pfnEIC_EXTINT_1_Handler       = ( void * ) EIC_EXTINT_1_Handler,
    .pfnEIC_EXTINT_2_Handler       = ( void * ) EIC_EXTINT_2_Handler,
    .pfnEIC_EXTINT_3_Handler       = ( void * ) EIC_EXTINT_3_Handler,
    .pfnEIC_OTHER_Handler          = ( void * ) EIC_OTHER_Handler,
    .pfnFREQM_Handler              = ( void * ) FREQM_Handler,
    .pfnNVMCTRL_Handler            = ( void * ) NVMCTRL_Handler,
    .pfnPORT_Handler               = ( void * ) PORT_Handler,
    .pfnDMAC_0_Handler             = ( void * ) DMAC_0_Handler,
    .pfnDMAC_1_Handler             = ( void * ) DMAC_1_Handler,
    .pfnDMAC_2_Handler             = ( void * ) DMAC_2_Handler,
    .pfnDMAC_3_Handler             = ( void * ) DMAC_3_Handler,
    .pfnDMAC_OTHER_Handler         = ( void * ) DMAC_OTHER_Handler,
    .pfnEVSYS_0_Handler            = ( void * ) EVSYS_0_Handler,
    .pfnEVSYS_1_Handler            = ( void * ) EVSYS_1_Handler,
    .pfnEVSYS_2_Handler            = ( void * ) EVSYS_2_Handler,
    .pfnEVSYS_3_Handler            = ( void * ) EVSYS_3_Handler,
    .pfnEVSYS_NSCHK_Handler        = ( void * ) EVSYS_NSCHK_Handler,
    .pfnPAC_Handler                = ( void * ) PAC_Handler,
    .pfnSERCOM0_0_Handler          = ( void * ) SERCOM0_0_Handler,
    .pfnSERCOM0_1_Handler          = ( void * ) SERCOM0_1_Handler,
    .pfnSERCOM0_2_Handler          = ( void * ) SERCOM0_2_Handler,
    .pfnSERCOM0_OTHER_Handler      = ( void * ) SERCOM0_OTHER_Handler,
    .pfnSERCOM1_0_Handler          = ( void * ) SERCOM1_0_Handler,
    .pfnSERCOM1_1_Handler          = ( void * ) SERCOM1_1_Handler,
    .pfnSERCOM1_2_Handler          = ( void * ) SERCOM1_2_Handler,
    .pfnSERCOM1_OTHER_Handler      = ( void * ) SERCOM1_OTHER_Handler,
    .pfnSERCOM2_0_Handler          = ( void * ) SERCOM2_0_Handler,
    .pfnSERCOM2_1_Handler          = ( void * ) SERCOM2_1_Handler,
    .pfnSERCOM2_2_Handler          = ( void * ) SERCOM2_2_Handler,
    .pfnSERCOM2_OTHER_Handler      = ( void * ) SERCOM2_OTHER_Handler,
    .pfnTC0_Handler                = ( void * ) TC0_Handler,
    .pfnTC1_Handler                = ( void * ) TC1_Handler,
    .pfnTC2_Handler                = ( void * ) TC2_Handler,
    .pfnADC_OTHER_Handler          = ( void * ) ADC_OTHER_InterruptHandler,
    .pfnADC_RESRDY_Handler         = ( void * ) ADC_Handler,
    .pfnAC_Handler                 = ( void * ) AC_Handler,
    .pfnDAC_UNDERRUN_A_Handler     = ( void * ) DAC_UNDERRUN_A_Handler,
    .pfnDAC_EMPTY_Handler          = ( void * ) DAC_EMPTY_Handler,
    .pfnPTC_Handler                = ( void * ) PTC_Handler,
    .pfnTRNG_Handler               = ( void * ) TRNG_Handler,
    .pfnTRAM_Handler               = ( void * ) TRAM_Handler,


};

/*******************************************************************************
 End of File
*/
