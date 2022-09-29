/*******************************************************************************
  MPLAB Harmony Exceptions Source File

  File Name:
    exceptions.c

  Summary:
    This file contains a function which overrides the default _weak_ exception
    handler provided by the XC32 compiler.

  Description:
    This file redefines the default _weak_  exception handler with a more debug
    friendly one. If an unexpected exception occurs the code will stop in a
    while(1) loop.  The debugger can be halted and two variables exception_code 
    and exception_address can be examined to determine the cause and address
    where the exception occurred.
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
<#if PRODUCT_FAMILY?contains("PIC32MZ")>
<#assign DEVIATION_COUNT = 8>
<#else>
<#assign DEVIATION_COUNT = 4>
</#if>
// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
<#if HarmonyCore??>
    <#if HarmonyCore.ENABLE_DRV_COMMON == true ||
         HarmonyCore.ENABLE_SYS_COMMON == true ||
         HarmonyCore.ENABLE_APP_FILE == true >
        <#lt>#include "configuration.h"
    </#if>
</#if>
#include "device.h"
#include "definitions.h"
#include <stdio.h>

// *****************************************************************************
// *****************************************************************************
// Section: Forward declaration of the handler functions
// *****************************************************************************
// *****************************************************************************
/* MISRAC 2012 deviation block start */
/* MISRA C-2012 Rule 21.2 deviated ${DEVIATION_COUNT} times. Deviation record ID -  H3_MISRAC_2012_R_21_2_DR_4 */
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunknown-pragmas"
#pragma coverity compliance block deviate:${DEVIATION_COUNT} "MISRA C-2012 Rule 21.2" "H3_MISRAC_2012_R_21_2_DR_4"
</#if>
void _general_exception_handler(void);
void _bootstrap_exception_handler(void);
<#if PRODUCT_FAMILY?contains("PIC32MZ")>
void _cache_err_exception_handler (void);
void _simple_tlb_refill_exception_handler(void);
</#if>

// *****************************************************************************
// *****************************************************************************
// Section: Global Data Definitions
// *****************************************************************************
// *****************************************************************************

/*******************************************************************************
  Exception Reason Data

  <editor-fold defaultstate="expanded" desc="Exception Reason Data">

  Remarks:
    These global static items are used instead of local variables in the
    _general_exception_handler function because the stack may not be available
    if an exception has occured.
*/

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

/* Address of instruction that caused the exception. */
static unsigned int exception_address;

/* Code identifying the cause of the exception (CP0 Cause register). */
static uint32_t  exception_code;

// </editor-fold>

/*******************************************************************************
  Function:
    void _general_exception_handler ( void )

  Description:
    A general exception is any non-interrupt exception which occurs during program
    execution outside of bootstrap code.

  Remarks:
    Refer to the XC32 User's Guide for additional information.
 */

void __attribute__((noreturn)) _general_exception_handler ( void )
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    exception_code = ((_CP0_GET_CAUSE() & 0x0000007CU) >> 2U);
    exception_address = _CP0_GET_EPC();

    while (true)
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

void __attribute__((noreturn)) _bootstrap_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while (true)
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

void __attribute__((noreturn)) _cache_err_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while (true)
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

void __attribute__((noreturn)) _simple_tlb_refill_exception_handler(void)
{
    /* Mask off the ExcCode Field from the Cause Register
    Refer to the MIPs Software User's manual */
    exception_code = (_CP0_GET_CAUSE() & 0x0000007CU) >> 2U;
    exception_address = _CP0_GET_EPC();

    while (true)
    {
        #if defined(__DEBUG) || defined(__DEBUG_D) && defined(__XC32)
            __builtin_software_breakpoint();
        #endif
    }
}
</#if>
<#if COVERITY_SUPPRESS_DEVIATION?? && COVERITY_SUPPRESS_DEVIATION>

#pragma coverity compliance end_block "MISRA C-2012 Rule 21.2"
#pragma GCC diagnostic pop
</#if>
/*******************************************************************************
 End of File
*/
