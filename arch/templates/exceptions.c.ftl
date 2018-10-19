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
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>#include "configuration.h"
    </#if>
</#if>
#include "definitions.h"
<#if ADVANCED_EXCEPTION>
#include <stdio.h>
</#if>

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

<#if ADVANCED_EXCEPTION>
<#lt>void HardFault_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
<#lt>{
<#lt>   uint32_t stacked_r0;
<#lt>   uint32_t stacked_r1;
<#lt>   uint32_t stacked_r2;
<#lt>   uint32_t stacked_r3;
<#lt>   uint32_t stacked_r12;
<#lt>   uint32_t stacked_lr;
<#lt>   uint32_t stacked_pc;
<#lt>   uint32_t stacked_psr;
    <#if CoreArchitecture != "CORTEX-M0+">
    <#lt>   uint32_t cfsr;
    <#lt>   uint32_t bus_fault_address;
    <#lt>   uint32_t memmanage_fault_address;

    <#lt>   bus_fault_address       = SCB->BFAR;  // BusFault Address Register
    <#lt>   memmanage_fault_address = SCB->MMFAR; // MemManage Fault Address Register
    <#lt>   cfsr                    = SCB->CFSR;  // Configurable Fault Status Register
    </#if>

<#lt>   stacked_r0  = hardfault_args[0];
<#lt>   stacked_r1  = hardfault_args[1];
<#lt>   stacked_r2  = hardfault_args[2];
<#lt>   stacked_r3  = hardfault_args[3];
<#lt>   stacked_r12 = hardfault_args[4];
<#lt>   stacked_lr  = hardfault_args[5];  // Link Register
<#lt>   stacked_pc  = hardfault_args[6];  // Program Counter
<#lt>   stacked_psr = hardfault_args[7];  // Program Status Register

<#lt>   printf("\r\n");
<#lt>   printf("[HardFault]\r\n");
<#lt>   printf("- Stack frame:\r\n");
<#lt>   printf(" R0  = 0x%08lX\r\n", stacked_r0);
<#lt>   printf(" R1  = 0x%08lX\r\n", stacked_r1);
<#lt>   printf(" R2  = 0x%08lX\r\n", stacked_r2);
<#lt>   printf(" R3  = 0x%08lX\r\n", stacked_r3);
<#lt>   printf(" R12 = 0x%08lX\r\n", stacked_r12);
<#lt>   printf(" LR  = 0x%08lX\r\n", stacked_lr);
<#lt>   printf(" PC  = 0x%08lX\r\n", stacked_pc);
<#lt>   printf(" PSR = 0x%08lX\r\n", stacked_psr);

    <#if CoreArchitecture != "CORTEX-M0+">
    <#lt>   printf("- FSR/FAR:\r\n");
    <#lt>   printf(" CFSR = 0x%08lX\r\n", cfsr);
    <#lt>   printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    <#lt>   printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    <#lt>   printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
    <#lt>   if (cfsr & 0x0080) printf(" MMFAR = 0x%08lX\r\n", memmanage_fault_address);
    <#lt>   if (cfsr & 0x8000) printf(" BFAR = 0x%08lX\r\n", bus_fault_address);
    </#if>

<#lt>   printf("- Misc\r\n");
<#lt>   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

    <#lt>  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>  #endif

<#lt>   while (1)
<#lt>   {
<#lt>       // Do Nothing
<#lt>   }
<#lt>}

    <#if CoreArchitecture != "CORTEX-M0+">
    <#lt>void DebugMonitor_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
    <#lt>{
    <#lt>   uint32_t stacked_r0;
    <#lt>   uint32_t stacked_r1;
    <#lt>   uint32_t stacked_r2;
    <#lt>   uint32_t stacked_r3;
    <#lt>   uint32_t stacked_r12;
    <#lt>   uint32_t stacked_lr;
    <#lt>   uint32_t stacked_pc;
    <#lt>   uint32_t stacked_psr;
    <#lt>   uint32_t cfsr;

    <#lt>   cfsr = SCB->CFSR;  // Configurable Fault Status Register

    <#lt>   stacked_r0  = hardfault_args[0];
    <#lt>   stacked_r1  = hardfault_args[1];
    <#lt>   stacked_r2  = hardfault_args[2];
    <#lt>   stacked_r3  = hardfault_args[3];
    <#lt>   stacked_r12 = hardfault_args[4];
    <#lt>   stacked_lr  = hardfault_args[5];  // Link Register
    <#lt>   stacked_pc  = hardfault_args[6];  // Program Counter
    <#lt>   stacked_psr = hardfault_args[7];  // Program Status Register

    <#lt>   printf("\r\n");
    <#lt>   printf("[DebugFault]\r\n");
    <#lt>   printf("- Stack frame:\r\n");
    <#lt>   printf(" R0  = 0x%08lX\r\n", stacked_r0);
    <#lt>   printf(" R1  = 0x%08lX\r\n", stacked_r1);
    <#lt>   printf(" R2  = 0x%08lX\r\n", stacked_r2);
    <#lt>   printf(" R3  = 0x%08lX\r\n", stacked_r3);
    <#lt>   printf(" R12 = 0x%08lX\r\n", stacked_r12);
    <#lt>   printf(" LR  = 0x%08lX\r\n", stacked_lr);
    <#lt>   printf(" PC  = 0x%08lX\r\n", stacked_pc);
    <#lt>   printf(" PSR = 0x%08lX\r\n", stacked_psr);

    <#lt>   printf("- FSR/FAR:\r\n");
    <#lt>   printf(" CFSR = 0x%08lX\r\n", cfsr);
    <#lt>   printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    <#lt>   printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    <#lt>   printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status

    <#lt>   printf("- Misc\r\n");
    <#lt>   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

    <#lt>  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>  #endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>       // Do Nothing
    <#lt>   }
    <#lt>}

    <#lt>void MemoryManagement_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
    <#lt>{
    <#lt>   uint32_t stacked_r0;
    <#lt>   uint32_t stacked_r1;
    <#lt>   uint32_t stacked_r2;
    <#lt>   uint32_t stacked_r3;
    <#lt>   uint32_t stacked_r12;
    <#lt>   uint32_t stacked_lr;
    <#lt>   uint32_t stacked_pc;
    <#lt>   uint32_t stacked_psr;
    <#lt>   uint32_t cfsr;
    <#lt>   uint8_t  mmfsr;
    <#lt>   uint32_t memmanage_fault_address;

    <#lt>   memmanage_fault_address = SCB->MMFAR;   // MemManage Fault Address Register
    <#lt>   cfsr                    = SCB->CFSR;    // Configurable Fault Status Register
    <#lt>   mmfsr = cfsr & 0xFF;                    // MemManage Fault Status

    <#lt>   stacked_r0  = hardfault_args[0];
    <#lt>   stacked_r1  = hardfault_args[1];
    <#lt>   stacked_r2  = hardfault_args[2];
    <#lt>   stacked_r3  = hardfault_args[3];
    <#lt>   stacked_r12 = hardfault_args[4];
    <#lt>   stacked_lr  = hardfault_args[5];  // Link Register
    <#lt>   stacked_pc  = hardfault_args[6];  // Program Counter
    <#lt>   stacked_psr = hardfault_args[7];  // Program Status Register

    <#lt>   printf("\r\n");
    <#lt>   printf("[MemoryManagement]\r\n");
    <#lt>   printf("- Stack frame:\r\n");
    <#lt>   printf(" R0  = 0x%08lX\r\n", stacked_r0);
    <#lt>   printf(" R1  = 0x%08lX\r\n", stacked_r1);
    <#lt>   printf(" R2  = 0x%08lX\r\n", stacked_r2);
    <#lt>   printf(" R3  = 0x%08lX\r\n", stacked_r3);
    <#lt>   printf(" R12 = 0x%08lX\r\n", stacked_r12);
    <#lt>   printf(" LR  = 0x%08lX\r\n", stacked_lr);
    <#lt>   printf(" PC  = 0x%08lX\r\n", stacked_pc);
    <#lt>   printf(" PSR = 0x%08lX\r\n", stacked_psr);

    <#lt>   printf("- FSR/FAR:\r\n");
    <#lt>   printf(" CFSR  = 0x%08lX\r\n", cfsr);
    <#lt>   printf(" MMFSR = 0x%02X\r\n", mmfsr);
    <#lt>   printf(" HFSR  = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    <#lt>   printf(" DFSR  = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    <#lt>   printf(" AFSR  = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
    <#lt>   if (cfsr & 0x0080) printf(" MMFAR = 0x%08lX\r\n", memmanage_fault_address);

    <#lt>   printf("- Misc\r\n");
    <#lt>   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

    <#lt>  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>  #endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>       // Do Nothing
    <#lt>   }
    <#lt>}

    <#lt>void BusFault_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
    <#lt>{
    <#lt>   uint32_t stacked_r0;
    <#lt>   uint32_t stacked_r1;
    <#lt>   uint32_t stacked_r2;
    <#lt>   uint32_t stacked_r3;
    <#lt>   uint32_t stacked_r12;
    <#lt>   uint32_t stacked_lr;
    <#lt>   uint32_t stacked_pc;
    <#lt>   uint32_t stacked_psr;
    <#lt>   uint32_t cfsr;
    <#lt>   uint8_t  bfsr;
    <#lt>   uint32_t bus_fault_address;

    <#lt>   bus_fault_address = SCB->BFAR;  // BusFault Address Register
    <#lt>   cfsr              = SCB->CFSR;  // Configurable Fault Status Register
    <#lt>   bfsr = ( cfsr & 0x0000FF00 ) >>8;  // Bus Fault Status

    <#lt>   stacked_r0  = hardfault_args[0];
    <#lt>   stacked_r1  = hardfault_args[1];
    <#lt>   stacked_r2  = hardfault_args[2];
    <#lt>   stacked_r3  = hardfault_args[3];
    <#lt>   stacked_r12 = hardfault_args[4];
    <#lt>   stacked_lr  = hardfault_args[5];  // Link Register
    <#lt>   stacked_pc  = hardfault_args[6];  // Program Counter
    <#lt>   stacked_psr = hardfault_args[7];  // Program Status Register

    <#lt>   printf("\r\n");
    <#lt>   printf("[BusFault]\r\n");
    <#lt>   printf("- Stack frame:\r\n");
    <#lt>   printf(" R0  = 0x%08lX\r\n", stacked_r0);
    <#lt>   printf(" R1  = 0x%08lX\r\n", stacked_r1);
    <#lt>   printf(" R2  = 0x%08lX\r\n", stacked_r2);
    <#lt>   printf(" R3  = 0x%08lX\r\n", stacked_r3);
    <#lt>   printf(" R12 = 0x%08lX\r\n", stacked_r12);
    <#lt>   printf(" LR  = 0x%08lX\r\n", stacked_lr);
    <#lt>   printf(" PC  = 0x%08lX\r\n", stacked_pc);
    <#lt>   printf(" PSR = 0x%08lX\r\n", stacked_psr);

    <#lt>   printf("- FSR/FAR:\r\n");
    <#lt>   printf(" CFSR  = 0x%08lX\r\n", cfsr);
    <#lt>   printf(" BFSR  = 0x%02X\r\n",  bfsr);
    <#lt>   printf(" HFSR  = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    <#lt>   printf(" DFSR  = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    <#lt>   printf(" AFSR  = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
    <#lt>   if (bfsr & 0x04) printf(" ABFSR = 0x%08lX\r\n", SCB->ABFSR);
    <#lt>   if (bfsr & 0x80) printf(" BFAR = 0x%08lX\r\n", bus_fault_address);

    <#lt>   printf("- Misc\r\n");
    <#lt>   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

    <#lt>  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>  #endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>       // Do Nothing
    <#lt>   }
    <#lt>}

    <#lt>void UsageFault_Handler_C(uint32_t * hardfault_args, unsigned int lr_value)
    <#lt>{
    <#lt>   uint32_t stacked_r0;
    <#lt>   uint32_t stacked_r1;
    <#lt>   uint32_t stacked_r2;
    <#lt>   uint32_t stacked_r3;
    <#lt>   uint32_t stacked_r12;
    <#lt>   uint32_t stacked_lr;
    <#lt>   uint32_t stacked_pc;
    <#lt>   uint32_t stacked_psr;
    <#lt>   uint32_t cfsr;
    <#lt>   uint16_t ufsr;

    <#lt>   cfsr = SCB->CFSR;  // Configurable Fault Status Register
    <#lt>   ufsr = cfsr >> 16; // Usage Fault Status

    <#lt>   stacked_r0  = hardfault_args[0];
    <#lt>   stacked_r1  = hardfault_args[1];
    <#lt>   stacked_r2  = hardfault_args[2];
    <#lt>   stacked_r3  = hardfault_args[3];
    <#lt>   stacked_r12 = hardfault_args[4];
    <#lt>   stacked_lr  = hardfault_args[5];  // Link Register
    <#lt>   stacked_pc  = hardfault_args[6];  // Program Counter
    <#lt>   stacked_psr = hardfault_args[7];  // Program Status Register

    <#lt>   printf("\r\n");
    <#lt>   printf("[UsageFault]\r\n");
    <#lt>   printf("- Stack frame:\r\n");
    <#lt>   printf(" R0  = 0x%08lX\r\n", stacked_r0);
    <#lt>   printf(" R1  = 0x%08lX\r\n", stacked_r1);
    <#lt>   printf(" R2  = 0x%08lX\r\n", stacked_r2);
    <#lt>   printf(" R3  = 0x%08lX\r\n", stacked_r3);
    <#lt>   printf(" R12 = 0x%08lX\r\n", stacked_r12);
    <#lt>   printf(" LR  = 0x%08lX\r\n", stacked_lr);
    <#lt>   printf(" PC  = 0x%08lX\r\n", stacked_pc);
    <#lt>   printf(" PSR = 0x%08lX\r\n", stacked_psr);

    <#lt>   printf("- FSR/FAR:\r\n");
    <#lt>   printf(" CFSR = 0x%08lX\r\n", cfsr);
    <#lt>   printf(" UFSR = 0x%04X\r\n",  ufsr);
    <#lt>   printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    <#lt>   printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    <#lt>   printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status

    <#lt>   printf("- Misc\r\n");
    <#lt>   printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4)>>2 );

    <#lt>  #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>  #endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>       // Do Nothing
    <#lt>   }
    <#lt>}
    </#if>
<#else>
<#lt>void HardFault_Handler(void)
<#lt>{
<#lt>#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
<#lt>   __builtin_software_breakpoint();
<#lt>#endif
<#lt>   while (1)
<#lt>   {
<#lt>   }
<#lt>}

    <#if CoreArchitecture != "CORTEX-M0+">
    <#lt>void DebugMonitor_Handler(void)
    <#lt>{
    <#lt>#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>#endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>   }
    <#lt>}

    <#lt>void MemoryManagement_Handler(void)
    <#lt>{
    <#lt>#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>#endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>   }
    <#lt>}

    <#lt>void BusFault_Handler(void)
    <#lt>{
    <#lt>#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>#endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>   }
    <#lt>}

    <#lt>void UsageFault_Handler(void)
    <#lt>{
    <#lt>#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    <#lt>   __builtin_software_breakpoint();
    <#lt>#endif
    <#lt>   while (1)
    <#lt>   {
    <#lt>   }
    <#lt>}
    </#if>
</#if>
/*******************************************************************************
 End of File
 */

