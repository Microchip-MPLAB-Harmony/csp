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
    <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
         HarmonyCore.ENABLE_SYS_COMMON == true ||
         HarmonyCore.ENABLE_APP_FILE == true >
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

typedef enum {
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
    EXCEP_IS1      = 16, // implementation specific 1
    EXCEP_CEU      = 17, // CorExtend Unusable
    EXCEP_C2E      = 18, // coprocessor 2
} excep_code;

// Use static variables, with fixed addresses, since S/W stack can be unstable
static excep_code _excep_code;
static unsigned int _excep_addr;
static uint32_t  _CP0_StatusValue;   // Status value from CP0 Register 12
static uintptr_t _StackPointerValue; // Stack pointer value
static uintptr_t _BadVirtualAddress; // Bad address for address exceptions
static uintptr_t _ReturnAddress;     // Return Address (ra)

/*******************************************************************************
  Function:
    void _general_exception_handler ( XCPT_FRAME* const pXFrame )

  Description:
    A general exception is any non-interrupt exception which occurs during program
    execution outside of bootstrap code.

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void __attribute__((nomips16, noreturn)) _general_exception_handler (XCPT_FRAME* const pXFrame)
{
    _excep_addr = pXFrame->epc;
    _excep_code = pXFrame->cause;   // capture exception type
    _excep_code = (_excep_code & 0x0000007C) >> 2;

    _CP0_StatusValue   = _CP0_GET_STATUS();
    asm volatile("sw $sp,%0" : "=m" (_StackPointerValue));
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
  Function:
    void _bootstrap_exception_handler ( void )

  Description:
    A bootstrap exception is any exception which occurs while bootstrap code is
    running (STATUS.BEV bit is 1).

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void  __attribute__((noreturn)) _bootstrap_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    _excep_code = (_CP0_GET_CAUSE() & 0x0000007C) >> 2;
    _excep_addr = _CP0_GET_EPC();

    while (1)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}

<#if __PROCESSOR?contains("PIC32MZ")>
/*******************************************************************************
  Function:
    void _cache_err_exception_handler ( void )

  Description:
    A cache-error exception occurs when an instruction or data reference detects
    a cache tag or data error. This exception is not maskable. To avoid
    disturbing the error in the cache array the exception vector is to an
    unmapped, uncached address. This exception is precise.

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void  __attribute__((noreturn)) _cache_err_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    _excep_code = (_CP0_GET_CAUSE() & 0x0000007C) >> 2;
    _excep_addr = _CP0_GET_EPC();

    while (1)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}

/*******************************************************************************
  Function:
    void _simple_tlb_refill_exception_handler ( void )

  Description:
    During an instruction fetch or data access, a TLB refill exception occurs
    when no TLB entry matches a reference to a mapped address space and the EXL
    bit is 0 in the Status register. Note that this is distinct from the case
    in which an entry matches, but has the valid bit off. In that case, a TLB
    Invalid exception occurs.

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void  __attribute__((noreturn)) _simple_tlb_refill_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    _excep_code = (_CP0_GET_CAUSE() & 0x0000007C) >> 2;
    _excep_addr = _CP0_GET_EPC();

    while (1)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}
</#if>
/*******************************************************************************
 End of File
*/
