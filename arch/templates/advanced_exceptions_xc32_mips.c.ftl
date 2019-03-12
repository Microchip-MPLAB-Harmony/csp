/*******************************************************************************
  MPLAB Harmony Advanced Exceptions Source File

  File Name:
    exceptions.c

  Summary:
    This file contains a function which overrides the default _weak_ exception
    handler provided by the XC32 compiler.

  Description:
    This file redefines the default _weak_  exception handler with a more debug
    friendly one. If an unexpected exception occurs the code will stop in a
    while(1) loop.  The debugger can be halted and variables can be examined to
    determine the cause and address where the exception occurred.
 *******************************************************************************/

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

// *****************************************************************************
// *****************************************************************************
// Section: Exception handling
// *****************************************************************************
// *****************************************************************************
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>#include "configuration.h"
    </#if>
</#if>
#include "definitions.h"
#include <stdio.h>


typedef struct _XCPT_FRAME  // access to all major registers from the instruction that caused the exception
{
    uint32_t at;
    uint32_t v0;
    uint32_t v1;
    uint32_t a0;
    uint32_t a1;
    uint32_t a2;
    uint32_t a3;
    uint32_t t0;
    uint32_t t1;
    uint32_t t2;
    uint32_t t3;
    uint32_t t4;
    uint32_t t5;
    uint32_t t6;
    uint32_t t7;
    uint32_t t8;
    uint32_t t9;
    uint32_t ra;
    uint32_t lo;
    uint32_t hi;
    uint32_t cause;
    uint32_t status;
    uint32_t epc;

} XCPT_FRAME;

static enum {
    EXCEP_IRQ      =  0, // interrupt
    EXCEP_AdEL     =  4, // address error exception (load or ifetch)
    EXCEP_AdES     =  5, // address error exception (store)
    EXCEP_IBE      =  6, // bus error (ifetch)
    EXCEP_DBE      =  7, // bus error (load/store)
    EXCEP_Sys      =  8, // syscall
    EXCEP_Bp       =  9, // breakpoint
    EXCEP_RI       = 10, // reserved instruction
    EXCEP_CpU      = 11, // coprocessor unusable
    EXCEP_Overflow = 12, // arithmetic overflow
    EXCEP_Trap     = 13, // trap (possible divide by zero)
    EXCEP_IS1      = 16, // implementation specfic 1
    EXCEP_CEU      = 17, // CorExtend Unuseable
    EXCEP_C2E      = 18, // coprocessor 2
} _excep_code;

// Use static variables, with fixed addresses, since S/W stack can be unstable
static unsigned int _excep_code;
static unsigned int _excep_addr;
static uint32_t  _CP0_StatusValue;   // Status value from CP0 Register 12
static uintptr_t _StackPointerValue; // Stack pointer value
static uintptr_t _BadVirtualAddress; // Bad address for address exceptions
static uintptr_t _ReturnAddress;     // Return Address (ra)

void __attribute__((nomips16)) _general_exception_handler (XCPT_FRAME* const pXFrame)
{
    register uint32_t _localStackPointerValue asm("sp");

    _excep_addr = pXFrame->epc;
    _excep_code = pXFrame->cause;   // capture exception type
    _excep_code = (_excep_code & 0x0000007C) >> 2;

    _CP0_StatusValue   = _CP0_GET_STATUS();
    _StackPointerValue = _localStackPointerValue;
    _BadVirtualAddress = _CP0_GET_BADVADDR();
    _ReturnAddress     = pXFrame->ra;

    printf("**EXCEPTION:*\r\n"
           " ECode: %d, EAddr: 0x%08X, CPO Status: 0x%08X\r\n"
           " Stack Ptr: 0x%08X, Bad Addr: 0x%08X, Return Addr: 0x%08X\r\n"
           "**EXCEPTION:*\r\n",
           _excep_code,_excep_addr,_CP0_StatusValue,
           _StackPointerValue,_BadVirtualAddress,_ReturnAddress);

    while(1)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}
/*******************************************************************************
 End of File
*/
