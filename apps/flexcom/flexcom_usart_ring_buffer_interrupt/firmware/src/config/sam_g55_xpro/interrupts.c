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
void MemoryManagement_Handler   ( void ) __attribute__((weak, alias("Dummy_Handler")));
void BusFault_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void UsageFault_Handler         ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SVCall_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void DebugMonitor_Handler       ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PendSV_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SysTick_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void SUPC_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void RSTC_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void RTC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void RTT_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void WDT_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PMC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void EFC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM7_InterruptHandler  ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM0_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM1_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PIOA_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PIOB_Handler               ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PDMIC0_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM2_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void MEM2MEM_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void I2SC0_Handler              ( void ) __attribute__((weak, alias("Dummy_Handler")));
void I2SC1_Handler              ( void ) __attribute__((weak, alias("Dummy_Handler")));
void PDMIC1_Handler             ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM3_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM4_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM5_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void FLEXCOM6_Handler           ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC0_CH0_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC0_CH1_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC0_CH2_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC1_CH0_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC1_CH1_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void TC1_CH2_Handler            ( void ) __attribute__((weak, alias("Dummy_Handler")));
void ADC_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void UHP_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void UDP_Handler                ( void ) __attribute__((weak, alias("Dummy_Handler")));
void CRCCU_Handler              ( void ) __attribute__((weak, alias("Dummy_Handler")));



/* Mutiple handlers for vector */



__attribute__ ((section(".vectors")))
const DeviceVectors exception_table=
{
    /* Configure Initial Stack Pointer, using linker-generated symbols */
    .pvStack = (void*) (&_stack),

    .pfnReset_Handler              = ( void * ) Reset_Handler,
    .pfnNonMaskableInt_Handler     = ( void * ) NonMaskableInt_Handler,
    .pfnHardFault_Handler          = ( void * ) HardFault_Handler,
    .pfnMemoryManagement_Handler   = ( void * ) MemoryManagement_Handler,
    .pfnBusFault_Handler           = ( void * ) BusFault_Handler,
    .pfnUsageFault_Handler         = ( void * ) UsageFault_Handler,
    .pfnSVCall_Handler             = ( void * ) SVCall_Handler,
    .pfnDebugMonitor_Handler       = ( void * ) DebugMonitor_Handler,
    .pfnPendSV_Handler             = ( void * ) PendSV_Handler,
    .pfnSysTick_Handler            = ( void * ) SysTick_Handler,
    .pfnSUPC_Handler               = ( void * ) SUPC_Handler,
    .pfnRSTC_Handler               = ( void * ) RSTC_Handler,
    .pfnRTC_Handler                = ( void * ) RTC_Handler,
    .pfnRTT_Handler                = ( void * ) RTT_Handler,
    .pfnWDT_Handler                = ( void * ) WDT_Handler,
    .pfnPMC_Handler                = ( void * ) PMC_Handler,
    .pfnEFC_Handler                = ( void * ) EFC_Handler,
    .pfnFLEXCOM7_Handler           = ( void * ) FLEXCOM7_InterruptHandler,
    .pfnFLEXCOM0_Handler           = ( void * ) FLEXCOM0_Handler,
    .pfnFLEXCOM1_Handler           = ( void * ) FLEXCOM1_Handler,
    .pfnPIOA_Handler               = ( void * ) PIOA_Handler,
    .pfnPIOB_Handler               = ( void * ) PIOB_Handler,
    .pfnPDMIC0_Handler             = ( void * ) PDMIC0_Handler,
    .pfnFLEXCOM2_Handler           = ( void * ) FLEXCOM2_Handler,
    .pfnMEM2MEM_Handler            = ( void * ) MEM2MEM_Handler,
    .pfnI2SC0_Handler              = ( void * ) I2SC0_Handler,
    .pfnI2SC1_Handler              = ( void * ) I2SC1_Handler,
    .pfnPDMIC1_Handler             = ( void * ) PDMIC1_Handler,
    .pfnFLEXCOM3_Handler           = ( void * ) FLEXCOM3_Handler,
    .pfnFLEXCOM4_Handler           = ( void * ) FLEXCOM4_Handler,
    .pfnFLEXCOM5_Handler           = ( void * ) FLEXCOM5_Handler,
    .pfnFLEXCOM6_Handler           = ( void * ) FLEXCOM6_Handler,
    .pfnTC0_CH0_Handler            = ( void * ) TC0_CH0_Handler,
    .pfnTC0_CH1_Handler            = ( void * ) TC0_CH1_Handler,
    .pfnTC0_CH2_Handler            = ( void * ) TC0_CH2_Handler,
    .pfnTC1_CH0_Handler            = ( void * ) TC1_CH0_Handler,
    .pfnTC1_CH1_Handler            = ( void * ) TC1_CH1_Handler,
    .pfnTC1_CH2_Handler            = ( void * ) TC1_CH2_Handler,
    .pfnADC_Handler                = ( void * ) ADC_Handler,
    .pfnUHP_Handler                = ( void * ) UHP_Handler,
    .pfnUDP_Handler                = ( void * ) UDP_Handler,
    .pfnCRCCU_Handler              = ( void * ) CRCCU_Handler,


};

/*******************************************************************************
 End of File
*/
