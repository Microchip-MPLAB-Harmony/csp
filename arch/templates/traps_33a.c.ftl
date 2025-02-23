/*******************************************************************************
  MPLAB Harmony TRAPS Source File

  File Name:
    ${trapsFileLowerCase}.c

  Summary:
    This is the generated source file for TRAPS  
 
  Description:
    None

 *******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2024 Microchip Technology Inc. and its subsidiaries.
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

// Section: Included Files
#include <device.h>
#include <stdbool.h>
#include "traps.h"

<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"

/* Following MISRA-C rules are deviated in the below code block */
/* MISRA C-2012 Rule 21.2 - Deviation record ID - H3_MISRAC_2012_R_21_2_DR_1 */
#pragma coverity compliance block deviate "MISRA C-2012 Rule 21.2"  "H3_MISRAC_2012_R_21_2_DR_1"
</#if>
<#if busErrorTrapAvailable == true>
void _BusErrorTrap(void);
</#if>
<#if addressErrorTrapAvailable == true>
void _AddressErrorTrap(void);
</#if>
<#if generalTrapAvailable == true>
void _GeneralTrap(void);
</#if>
<#if mathErrorTrapAvailable == true>
void _MathErrorTrap(void);
</#if>
<#if stackErrorTrapAvailable == true>
void _StackErrorTrap(void);
</#if>
<#if illegalInstructionTrapAvailable == true>
void _IllegalInstructionTrap(void);
</#if>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
</#if>

#define ERROR_HANDLER __attribute__((weak,interrupt,no_auto_psv))
#define FAILSAFE_STACK_GUARDSIZE 8
#define FAILSAFE_STACK_SIZE 32

/* Address of instruction that caused the exception. */
static uint32_t  exception_address;
 
/* Code identifying the cause of the exception. */
static uint32_t  exception_code;

// Section: Driver Interface Function Definitions

//@brief Halts
void __attribute__((weak)) ${trapsFileUpperCase}_halt_on_error(uint16_t code)  // 
{
    exception_code  = code;
    
    exception_address = PCTRAP;
    
    while(true)
    {
        #ifdef __DEBUG
        /* If we are in debug mode, cause a software breakpoint in the debugger */
        __builtin_software_breakpoint();
        #endif
    }
}

<#if stackErrorTrapAvailable == true>
#define SET_STACK_POINTER(stack) __asm__ volatile ("mov %0, W15" : : "r"(stack))

inline static void use_failsafe_stack(void)
{
    static uint8_t failsafe_stack[FAILSAFE_STACK_SIZE];

    SET_STACK_POINTER(failsafe_stack);  
    
    /* Controls where the stack pointer limit is, relative to the end of the
    * failsafe stack
    */
    SPLIM = (uint32_t)(failsafe_stack + sizeof(failsafe_stack) - (uint32_t)FAILSAFE_STACK_GUARDSIZE);
}
</#if>

<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
/* Following MISRA-C rules are deviated in the below code block */
/* MISRA C-2012 Rule 21.2 - Deviation record ID - H3_MISRAC_2012_R_21_2_DR_1 */
#pragma coverity compliance block deviate "MISRA C-2012 Rule 21.2"  "H3_MISRAC_2012_R_21_2_DR_1"
</#if>
<#if busErrorTrapAvailable == true>
/** Bus error.**/
void ERROR_HANDLER _BusErrorTrap(void)
{
    if(INTCON3bits.DMABET == 1)
    {
      INTCON3bits.DMABET = 0;  //Clear the trap flag
      TRAPS_halt_on_error(TRAPS_BUS_DMA_ERR);
    }

    if(INTCON3bits.YRAMBET == 1)
    {
      INTCON3bits.YRAMBET = 0;  //Clear the trap flag
      TRAPS_halt_on_error(TRAPS_BUS_CPU_Y_ERR);
    }

    if(INTCON3bits.XRAMBET == 1)
    {
      INTCON3bits.XRAMBET = 0;  //Clear the trap flag
      TRAPS_halt_on_error(TRAPS_BUS_CPU_X_ERR);
    }

    if(INTCON3bits.CPUBET == 1)
    {
      INTCON3bits.CPUBET = 0;  //Clear the trap flag
      TRAPS_halt_on_error(TRAPS_BUS_CPU_INSTR_ERR);
    }

    while(true)
    {
    }
}
</#if>

<#if addressErrorTrapAvailable == true>
/** Address error.**/
void ERROR_HANDLER _AddressErrorTrap(void)
{
    ${addressErrorTrapStatusBit} = 0;  //Clear the trap flag
    TRAPS_halt_on_error(TRAPS_ADDRESS_ERR);
}
</#if>

<#if generalTrapAvailable == true>
/** General error.**/
void ERROR_HANDLER _GeneralTrap(void)
{
    <#if dmtTrapAvailable == true>
    if(INTCON5bits.DMTE == 1)
    {
      ${dmtTrapStatusBit} = 0;  //Clear the trap flag 
      TRAPS_halt_on_error(TRAPS_DMT_ERR);
    }
    </#if>

    <#if softTrapAvailable == true>
    if(INTCON5bits.SOFT == 1)
    {
      ${softTrapStatusBit} = 0;  //Clear the trap flag 
      TRAPS_halt_on_error(TRAPS_SOFT_ERR);
    }
    </#if>

    <#if wdtTrapAvailable == true>
    if(INTCON5bits.WDTE == 1)
    {
      ${wdtTrapStatusBit} = 0;  //Clear the trap flag
      TRAPS_halt_on_error(TRAPS_WDT_ERR); 
    }
    </#if>
    while(true)
    {
    }
}
</#if>

<#if mathErrorTrapAvailable == true>
/** Math error.**/
void ERROR_HANDLER _MathErrorTrap(void)
{
    ${mathErrorTrapStatusBit} = 0;  //Clear the trap flag        
    TRAPS_halt_on_error(TRAPS_DIV0_ERR);
}
</#if>

<#if stackErrorTrapAvailable == true>
/** Stack error.**/
void ERROR_HANDLER _StackErrorTrap(void)
{
    /* We use a failsafe stack: the presence of a stack-pointer error
     * means that we cannot trust the stack to operate correctly unless
     * we set the stack pointer to a safe place.
     */
    use_failsafe_stack(); 
    
    ${stackErrorTrapStatusBit} = 0;  //Clear the trap flag         
    TRAPS_halt_on_error(TRAPS_STACK_ERR);
}
</#if>

<#if illegalInstructionTrapAvailable == true>
/** Illegal instruction.**/
void ERROR_HANDLER _IllegalInstructionTrap(void)
{
    ${illegalInstructionTrapStatusBit} = 0;  //Clear the trap flag   
    TRAPS_halt_on_error(TRAPS_ILLEGAL_INSTRUCTION); 
}
</#if>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
</#if>