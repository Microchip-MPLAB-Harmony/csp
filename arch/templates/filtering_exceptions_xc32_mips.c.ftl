/*******************************************************************************
  MPLAB Harmony Filtering Advanced Exception Source File

  File Name:
    exceptions.c

  Summary:
    This file contains a function which overrides the default _weak_ exception
    handler provided by the XC32 compiler.

  Description:
    The standard exception handling provided by the compiler's installation is
    insufficient to handle overflow exception that can happen inside of assembly
    IIR routines.

    Exceptions are handled by the default code by simply throwing the application
    into a while (1) loop, which simply ends all processing of the application.
    This new code attempts to return control back to the application.

    If an overflow exception is trapped, a fall-back return value is written to
    the $v0 register for use by the IIR primitive that generated the overflow.
    The application can use +1 (0x7FFF) or Zero, or random noise as the fall-back
    return value.
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
<#if PRODUCT_FAMILY?contains("PIC32MZ")>
<#assign DEVIATION_COUNT = 8>
<#else>
<#assign DEVIATION_COUNT = 4>
</#if>

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

//Get stack pointer value
#ifndef GET_EXCEP_SP
#define GET_EXCEP_SP(var) asm volatile("sw $sp,%0" : "=m" (var))
#endif

/* Exception codes */
#define EXCEP_IRQ       0U // interrupt
#define EXCEP_AdEL      4U // address error exception (load or ifetch)
#define EXCEP_AdES      5U // address error exception (store)
#define EXCEP_IBE       6U // bus error (ifetch)
#define EXCEP_DBE       7U // bus error (load/store)
#define EXCEP_Sys       8U // syscall
#define EXCEP_Bp        9U // breakpoint
#define EXCEP_RI        10U // reserved instruction
#define EXCEP_CpU       11U // coprocessor unusable
#define EXCEP_Overflow  12U // arithmetic overflow
#define EXCEP_Trap      13U // trap (possible divide by zero)
#define EXCEP_IS1       16U // implementation specfic 1
#define EXCEP_CEU       17U // CorExtend Unuseable
#define EXCEP_C2E       18U // coprocessor 2

typedef struct XCPT_FRAME_tag  // access to all major registers from the instruction that caused the exception
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

/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.2 deviated ${DEVIATION_COUNT} times. Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_4 */
/* MISRA C-2012 Rule 21.6 deviated 1 time. Deviation record ID -  H3_MISRAC_2012_R_21_6_DR_2 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block\
 (deviate:${DEVIATION_COUNT} "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_4")\
 (deviate:1 "MISRA C-2012 Rule 21.6" "H3_MISRAC_2012_R_21_6_DR_2")
</#if>
void _general_exception_handler(XCPT_FRAME* const pXFrame);
void _bootstrap_exception_handler(void);
<#if PRODUCT_FAMILY?contains("PIC32MZ")>
void _cache_err_exception_handler (void);
void _simple_tlb_refill_exception_handler(void);
</#if>

// Use static variables, with fixed addresses, since S/W stack can be unstable
static uint32_t exception_code;
static uint32_t exception_address;
static uint32_t cp0_status_value; // Status value from CP0 Register 12
static uintptr_t stack_pointer_value; // Stack pointer value
static uintptr_t bad_virtual_address; // Bad address for address exceptions
static uintptr_t return_address; // Return Address (ra)

/*******************************************************************************
  Function:
    void _general_exception_handler ( XCPT_FRAME* const pXFrame )

  Description:
    A general exception is any non-interrupt exception which occurs during program
    execution outside of bootstrap code.

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void __attribute__((nomips16)) _general_exception_handler (XCPT_FRAME* const pXFrame)
{
    exception_address = pXFrame->epc;
    exception_code = pXFrame->cause;   // capture exception type
    exception_code = (exception_code & 0x0000007CU) >> 2U;

    cp0_status_value   = _CP0_GET_STATUS();
    GET_EXCEP_SP(stack_pointer_value);
    bad_virtual_address = _CP0_GET_BADVADDR();
    return_address     = pXFrame->ra;

    if (exception_code == EXCEP_Overflow)
    {// Provide fallback return value for filtering primitive throwing an overflow exception.
        pXFrame->v0 = 0x7FFFU;  // set function output to maximum (saturation)
        pXFrame->v1 = 0x7FFFU;  // set intermediate results to maximum (saturation)
        pXFrame->epc = pXFrame->epc + 4U; // set return from exception to next instruction (skip)
        return;
    }

    (void)printf("**EXCEPTION:*\r\n"
           " ECode: %d, EAddr: 0x%08X, CPO Status: 0x%08X\r\n"
           " Stack Ptr: 0x%08X, Bad Addr: 0x%08X, Return Addr: 0x%08X\r\n"
           "**EXCEPTION:*\r\n",
           exception_code,exception_address,cp0_status_value,
           stack_pointer_value,bad_virtual_address,return_address);

    while(true)
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
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while(true)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}
<#if PRODUCT_FAMILY?contains("PIC32MZ")>
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
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while(true)
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
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while(true)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}
</#if>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>
#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2" "MISRA C-2012 Rule 21.6"
#pragma GCC diagnostic pop
</#if>
/*******************************************************************************
 End of File
*/
