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
<#assign M4_M7_EXCEPTIONS = (CoreArchitecture == "CORTEX-M4") || (CoreArchitecture == "CORTEX-M7")>
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
         HarmonyCore.ENABLE_SYS_COMMON == true ||
         HarmonyCore.ENABLE_APP_FILE == true >
    #include "configuration.h"
    </#if>
</#if>
<#if CoreSysIntFile == true>
#include "interrupts.h"
</#if>
#include "definitions.h"
<#if ADVANCED_EXCEPTION>
#include <stdio.h>
</#if>

<#if ADVANCED_EXCEPTION>

// *****************************************************************************
// *****************************************************************************
// Section: Local functions
// *****************************************************************************
// *****************************************************************************

typedef void(*advanced_handler_t)(uint32_t * fault_args, unsigned int lr_value);


static inline void call_advanced_exception_handler(advanced_handler_t pHandler)
{
<#if CoreArchitecture == "CORTEX-M0PLUS">
    asm volatile (
        "MOVS   R0, #4\n\t"
        "MOV    R1, LR\n\t"
        "TST    R0, R1\n\t"
        "BEQ    stacking_used_MSP\n\t"
        "MRS    R0, PSP\n\t"
        "B      invoke_handler \n\t"
        "stacking_used_MSP: \n"
        "MRS    R0, MSP\n\t"
        "invoke_handler: \n"
        "BX     %0"::"r"(pHandler));
<#else>
    asm volatile (
        "TST    LR, #4\n\t"
        "ITE    EQ\n\t"
        "MRSEQ  R0, MSP\n\t"
        "MRSNE  R0, PSP\n\t"
        "MOV    R1, LR\n\t"
        "BX     %0"::"r"(pHandler));
</#if>
}

/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.6 deviated 98 times.  Deviation record ID -  H3_MISRAC_2012_R_21_6_DR_1 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
    <#if COMPILER_CHOICE == "XC32">
    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunknown-pragmas"
    </#if>
    #pragma coverity compliance block deviate:98 "MISRA C-2012 Rule 21.6" "H3_MISRAC_2012_R_21_6_DR_1"
</#if>
static void __attribute__((noreturn)) ProcessHardFaultException(uint32_t * fault_args, unsigned int lr_value)
{
    uint32_t stacked_r0;
    uint32_t stacked_r1;
    uint32_t stacked_r2;
    uint32_t stacked_r3;
    uint32_t stacked_r12;
    uint32_t stacked_lr;
    uint32_t stacked_pc;
    uint32_t stacked_psr;
<#if M4_M7_EXCEPTIONS>
    uint32_t cfsr;
    uint32_t bus_fault_address;
    uint32_t memmanage_fault_address;

    bus_fault_address       = SCB->BFAR;  // BusFault Address Register
    memmanage_fault_address = SCB->MMFAR; // MemManage Fault Address Register
    cfsr                    = SCB->CFSR;  // Configurable Fault Status Register
</#if>

    stacked_r0  = fault_args[0];
    stacked_r1  = fault_args[1];
    stacked_r2  = fault_args[2];
    stacked_r3  = fault_args[3];
    stacked_r12 = fault_args[4];
    stacked_lr  = fault_args[5];  // Link Register
    stacked_pc  = fault_args[6];  // Program Counter
    stacked_psr = fault_args[7];  // Program Status Register

    (void)printf("\r\n");
    (void)printf("[HardFault]\r\n");
    (void)printf("- Stack frame:\r\n");
    (void)printf(" R0  = 0x%08lX\r\n", stacked_r0);
    (void)printf(" R1  = 0x%08lX\r\n", stacked_r1);
    (void)printf(" R2  = 0x%08lX\r\n", stacked_r2);
    (void)printf(" R3  = 0x%08lX\r\n", stacked_r3);
    (void)printf(" R12 = 0x%08lX\r\n", stacked_r12);
    (void)printf(" LR  = 0x%08lX\r\n", stacked_lr);
    (void)printf(" PC  = 0x%08lX\r\n", stacked_pc);
    (void)printf(" PSR = 0x%08lX\r\n", stacked_psr);
<#if M4_M7_EXCEPTIONS>
    (void)printf("- FSR/FAR:\r\n");
    (void)printf(" CFSR = 0x%08lX\r\n", cfsr);
    (void)printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    (void)printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    (void)printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
    if ((cfsr & 0x0080U) != 0U)
    {
        (void)printf(" MMFAR = 0x%08lX\r\n", memmanage_fault_address);
    }
    if ((cfsr & 0x8000U) != 0U)
    {
        (void)printf(" BFAR = 0x%08lX\r\n", bus_fault_address);
    }
</#if>

    (void)printf("- Misc\r\n");
    (void)printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4U) >> 2);

    #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
    #endif

    while (true)
    {
        // Do Nothing
    }
}

<#if M4_M7_EXCEPTIONS>
static void __attribute__((noreturn)) ProcessDebugMonitorException(uint32_t * fault_args, unsigned int lr_value)
{
    uint32_t stacked_r0;
    uint32_t stacked_r1;
    uint32_t stacked_r2;
    uint32_t stacked_r3;
    uint32_t stacked_r12;
    uint32_t stacked_lr;
    uint32_t stacked_pc;
    uint32_t stacked_psr;
    uint32_t cfsr;

    cfsr = SCB->CFSR;  // Configurable Fault Status Register

    stacked_r0  = fault_args[0];
    stacked_r1  = fault_args[1];
    stacked_r2  = fault_args[2];
    stacked_r3  = fault_args[3];
    stacked_r12 = fault_args[4];
    stacked_lr  = fault_args[5];  // Link Register
    stacked_pc  = fault_args[6];  // Program Counter
    stacked_psr = fault_args[7];  // Program Status Register

    (void)printf("\r\n");
    (void)printf("[DebugMonitor]\r\n");
    (void)printf("- Stack frame:\r\n");
    (void)printf(" R0  = 0x%08lX\r\n", stacked_r0);
    (void)printf(" R1  = 0x%08lX\r\n", stacked_r1);
    (void)printf(" R2  = 0x%08lX\r\n", stacked_r2);
    (void)printf(" R3  = 0x%08lX\r\n", stacked_r3);
    (void)printf(" R12 = 0x%08lX\r\n", stacked_r12);
    (void)printf(" LR  = 0x%08lX\r\n", stacked_lr);
    (void)printf(" PC  = 0x%08lX\r\n", stacked_pc);
    (void)printf(" PSR = 0x%08lX\r\n", stacked_psr);

    (void)printf("- FSR/FAR:\r\n");
    (void)printf(" CFSR = 0x%08lX\r\n", cfsr);
    (void)printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    (void)printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    (void)printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status

    (void)printf("- Misc\r\n");
    (void)printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4U) >> 2);

    #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
    #endif
    while (true)
    {
        // Do Nothing
    }
}

static void __attribute__((noreturn)) ProcessMemoryManagementException(uint32_t * fault_args, unsigned int lr_value)
{
    uint32_t stacked_r0;
    uint32_t stacked_r1;
    uint32_t stacked_r2;
    uint32_t stacked_r3;
    uint32_t stacked_r12;
    uint32_t stacked_lr;
    uint32_t stacked_pc;
    uint32_t stacked_psr;
    uint32_t cfsr;
    uint32_t  mmfsr;
    uint32_t memmanage_fault_address;

    memmanage_fault_address = SCB->MMFAR;   // MemManage Fault Address Register
    cfsr                    = SCB->CFSR;    // Configurable Fault Status Register
    mmfsr = cfsr & 0xFFU;                    // MemManage Fault Status

    stacked_r0  = fault_args[0];
    stacked_r1  = fault_args[1];
    stacked_r2  = fault_args[2];
    stacked_r3  = fault_args[3];
    stacked_r12 = fault_args[4];
    stacked_lr  = fault_args[5];  // Link Register
    stacked_pc  = fault_args[6];  // Program Counter
    stacked_psr = fault_args[7];  // Program Status Register

    (void)printf("\r\n");
    (void)printf("[MemoryManagement]\r\n");
    (void)printf("- Stack frame:\r\n");
    (void)printf(" R0  = 0x%08lX\r\n", stacked_r0);
    (void)printf(" R1  = 0x%08lX\r\n", stacked_r1);
    (void)printf(" R2  = 0x%08lX\r\n", stacked_r2);
    (void)printf(" R3  = 0x%08lX\r\n", stacked_r3);
    (void)printf(" R12 = 0x%08lX\r\n", stacked_r12);
    (void)printf(" LR  = 0x%08lX\r\n", stacked_lr);
    (void)printf(" PC  = 0x%08lX\r\n", stacked_pc);
    (void)printf(" PSR = 0x%08lX\r\n", stacked_psr);

    (void)printf("- FSR/FAR:\r\n");
    (void)printf(" CFSR  = 0x%08lX\r\n", cfsr);
    (void)printf(" MMFSR = 0x%02lX\r\n", mmfsr);
    (void)printf(" HFSR  = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    (void)printf(" DFSR  = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    (void)printf(" AFSR  = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
    if ((cfsr & 0x0080U) != 0U)
    {
        (void)printf(" MMFAR = 0x%08lX\r\n", memmanage_fault_address);
    }
    (void)printf("- Misc\r\n");
    (void)printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4U)>>2 );

    #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
    #endif
    while (true)
    {
        // Do Nothing
    }
}

static void __attribute__((noreturn)) ProcessBusFaultException(uint32_t * fault_args, unsigned int lr_value)
{
    uint32_t stacked_r0;
    uint32_t stacked_r1;
    uint32_t stacked_r2;
    uint32_t stacked_r3;
    uint32_t stacked_r12;
    uint32_t stacked_lr;
    uint32_t stacked_pc;
    uint32_t stacked_psr;
    uint32_t cfsr;
    uint32_t  bfsr;
    uint32_t bus_fault_address;

    bus_fault_address = SCB->BFAR;  // BusFault Address Register
    cfsr              = SCB->CFSR;  // Configurable Fault Status Register
    bfsr = (cfsr & 0x0000FF00U) >> 8;  // Bus Fault Status

    stacked_r0  = fault_args[0];
    stacked_r1  = fault_args[1];
    stacked_r2  = fault_args[2];
    stacked_r3  = fault_args[3];
    stacked_r12 = fault_args[4];
    stacked_lr  = fault_args[5];  // Link Register
    stacked_pc  = fault_args[6];  // Program Counter
    stacked_psr = fault_args[7];  // Program Status Register

    (void)printf("\r\n");
    (void)printf("[BusFault]\r\n");
    (void)printf("- Stack frame:\r\n");
    (void)printf(" R0  = 0x%08lX\r\n", stacked_r0);
    (void)printf(" R1  = 0x%08lX\r\n", stacked_r1);
    (void)printf(" R2  = 0x%08lX\r\n", stacked_r2);
    (void)printf(" R3  = 0x%08lX\r\n", stacked_r3);
    (void)printf(" R12 = 0x%08lX\r\n", stacked_r12);
    (void)printf(" LR  = 0x%08lX\r\n", stacked_lr);
    (void)printf(" PC  = 0x%08lX\r\n", stacked_pc);
    (void)printf(" PSR = 0x%08lX\r\n", stacked_psr);

    (void)printf("- FSR/FAR:\r\n");
    (void)printf(" CFSR  = 0x%08lX\r\n", cfsr);
    (void)printf(" BFSR  = 0x%02lX\r\n", bfsr);
    (void)printf(" HFSR  = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    (void)printf(" DFSR  = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    (void)printf(" AFSR  = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status
<#if CoreArchitecture == "CORTEX-M7">
        if((bfsr & 0x04U) != 0U)
        {
            (void)printf(" ABFSR = 0x%08lX\r\n", SCB->ABFSR);
        }
</#if>
    if((bfsr & 0x80U) != 0U)
    {
        (void)printf(" BFAR = 0x%08lX\r\n", bus_fault_address);
    }
    (void)printf("- Misc\r\n");
    (void)printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4U) >> 2);

    #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
    #endif
    while (true)
    {
        // Do Nothing
    }
}

static void __attribute__((noreturn)) ProcessUsageFaultException(uint32_t * fault_args, unsigned int lr_value)
{
    uint32_t stacked_r0;
    uint32_t stacked_r1;
    uint32_t stacked_r2;
    uint32_t stacked_r3;
    uint32_t stacked_r12;
    uint32_t stacked_lr;
    uint32_t stacked_pc;
    uint32_t stacked_psr;
    uint32_t cfsr;
    uint32_t ufsr;

    cfsr = SCB->CFSR;  // Configurable Fault Status Register
    ufsr = cfsr >> 16; // Usage Fault Status

    stacked_r0  = fault_args[0];
    stacked_r1  = fault_args[1];
    stacked_r2  = fault_args[2];
    stacked_r3  = fault_args[3];
    stacked_r12 = fault_args[4];
    stacked_lr  = fault_args[5];  // Link Register
    stacked_pc  = fault_args[6];  // Program Counter
    stacked_psr = fault_args[7];  // Program Status Register

    (void)printf("\r\n");
    (void)printf("[UsageFault]\r\n");
    (void)printf("- Stack frame:\r\n");
    (void)printf(" R0  = 0x%08lX\r\n", stacked_r0);
    (void)printf(" R1  = 0x%08lX\r\n", stacked_r1);
    (void)printf(" R2  = 0x%08lX\r\n", stacked_r2);
    (void)printf(" R3  = 0x%08lX\r\n", stacked_r3);
    (void)printf(" R12 = 0x%08lX\r\n", stacked_r12);
    (void)printf(" LR  = 0x%08lX\r\n", stacked_lr);
    (void)printf(" PC  = 0x%08lX\r\n", stacked_pc);
    (void)printf(" PSR = 0x%08lX\r\n", stacked_psr);

    (void)printf("- FSR/FAR:\r\n");
    (void)printf(" CFSR = 0x%08lX\r\n", cfsr);
    (void)printf(" UFSR = 0x%04lX\r\n",  ufsr);
    (void)printf(" HFSR = 0x%08lX\r\n", SCB->HFSR); // HardFault Status
    (void)printf(" DFSR = 0x%08lX\r\n", SCB->DFSR); // Debug Fault Status
    (void)printf(" AFSR = 0x%08lX\r\n", SCB->AFSR); // Auxiliary Fault Status

    (void)printf("- Misc\r\n");
    (void)printf(" LR/EXC_RETURN = 0x%X, Bit 2: %d\r\n", lr_value, (lr_value & 0x4U) >> 2);

    #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
    #endif
    while (true)
    {
        // Do Nothing
    }
}
</#if><#-- M4_M7_EXCEPTIONS -->
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2" "MISRA C-2012 Rule 21.6"
#pragma GCC diagnostic pop
</#if><#-- COVERITY_SUPPRESS_DEVIATION -->
</#if> <#-- ADVANCED_EXCEPTION -->

// *****************************************************************************
// *****************************************************************************
// Section: Exception Handling Routine
// *****************************************************************************
// *****************************************************************************
<#if .vars["NVIC_-14_0_ENABLE"] && .vars["NVIC_-14_0_HANDLER"] ==  "NonMaskableInt_Handler">

/* Brief default interrupt handlers for core IRQs.*/
void __attribute__((noreturn, weak)) NonMaskableInt_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
    __builtin_software_breakpoint();
#endif
    while (true)
    {
    }
}
</#if>
<#if ADVANCED_EXCEPTION>

void __attribute__((used)) HardFault_Handler(void)
{
    call_advanced_exception_handler(ProcessHardFaultException);
}

<#if M4_M7_EXCEPTIONS>
void __attribute__((used)) DebugMonitor_Handler(void)
{
    call_advanced_exception_handler(ProcessDebugMonitorException);
}

void __attribute__((used)) MemoryManagement_Handler(void)
{
    call_advanced_exception_handler(ProcessMemoryManagementException);
}

void __attribute__((used)) BusFault_Handler(void)
{
    call_advanced_exception_handler(ProcessBusFaultException);
}

void __attribute__((used)) UsageFault_Handler(void)
{
    call_advanced_exception_handler(ProcessUsageFaultException);
}
</#if> <#-- M4_M7_EXCEPTIONS -->
<#else> <#-- not ADVANCED_EXCEPTION -->
void __attribute__((noreturn, weak)) HardFault_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
#endif
   while (true)
   {
   }
}

<#if M4_M7_EXCEPTIONS>
void __attribute__((noreturn, weak)) DebugMonitor_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
#endif
   while (true)
   {
   }
}

void __attribute__((noreturn, weak)) MemoryManagement_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
#endif
   while (true)
   {
   }
}

void __attribute__((noreturn, weak)) BusFault_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
#endif
   while (true)
   {
   }
}

void __attribute__((noreturn, weak)) UsageFault_Handler(void)
{
#if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
   __builtin_software_breakpoint();
#endif
   while (true)
   {
   }
}
</#if> <#-- M4_M7_EXCEPTIONS -->
</#if><#-- ADVANCED_EXCEPTION -->
/*******************************************************************************
 End of File
 */
