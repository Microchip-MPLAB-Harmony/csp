/*******************************************************************************
  System Exceptions File

  File Name:
    exceptions.c

  Summary:
    This file contains a function which overrides the default _weak_ exception
    handlers provided by the interrupt.c file.

  Description:
    This file redefines the default _weak_  exception handler with a more debug
    friendly one. If an unexpected exception occurs the code will stop in a
    while(1) loop.
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
#include <stdio.h>

// *****************************************************************************
// *****************************************************************************
// Section: Exception Handling Routine
// *****************************************************************************
// *****************************************************************************

/* Brief default interrupt handlers for core IRQs.*/

void NonMaskableInt_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
    while (1)
    {
    }
}

void HardFault_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
{
   uint32_t stacked_r0;
   uint32_t stacked_r1;
   uint32_t stacked_r2;
   uint32_t stacked_r3;
   uint32_t stacked_r12;
   uint32_t stacked_lr;
   uint32_t stacked_pc;
   uint32_t stacked_psr;

   stacked_r0  = hardfault_args[0];
   stacked_r1  = hardfault_args[1];
   stacked_r2  = hardfault_args[2];
   stacked_r3  = hardfault_args[3];
   stacked_r12 = hardfault_args[4];
   stacked_lr  = hardfault_args[5];  // Link Register
   stacked_pc  = hardfault_args[6];  // Program Counter
   stacked_psr = hardfault_args[7];  // Program Status Register

   printf("\r\n");
   printf("[HardFault]\r\n");
   printf("- Stack frame:\r\n");
   printf(" R0  = 0x%08lX\r\n", stacked_r0);
   printf(" R1  = 0x%08lX\r\n", stacked_r1);
   printf(" R2  = 0x%08lX\r\n", stacked_r2);
   printf(" R3  = 0x%08lX\r\n", stacked_r3);
   printf(" R12 = 0x%08lX\r\n", stacked_r12);
   printf(" LR  = 0x%08lX\r\n", stacked_lr);
   printf(" PC  = 0x%08lX\r\n", stacked_pc);
   printf(" PSR = 0x%08lX\r\n", stacked_psr);


   printf("- Misc\r\n");
   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
  #endif

   while (1)
   {
       // Do Nothing
   }
}

/*******************************************************************************
 End of File
 */

