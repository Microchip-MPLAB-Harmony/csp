/*******************************************************************************
  Reset Controller Peripheral Library, RSTC PLIB 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rstc${INSTANCE?string}.c

  Summary:
    RSTC PLIB source file

  Description:
    Interface definitions for the RSTC PLIB.
    The RSTC PLIB provides access to and control of the associated
    reset controller.

  Remarks:
    None

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
#include "plib_rstc${INSTANCE?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************
void RSTC${INSTANCE?string}_Initialize( void )
{
    // External reset length (${RSTC_EXTERNAL_RESET_LENGTH_MSECS?string} mSecs) 
    uint32_t regValue = RSTC_MR_KEY_PASSWD | RSTC_MR_ERSTL( ${RSTC_MR_EXTERNAL_RESET_LENGTH} );
    <#if RSTC_MR_EXTERNAL_RESET_ACTION == "RESET">
        <#lt>    // Perform user reset on NRST input
        <#lt>    regValue |= RSTC_MR_URSTEN_Msk;
    <#elseif RSTC_MR_EXTERNAL_RESET_ACTION == "INTERRUPT">
        <#lt>    // Interrupt on NRST input
        <#lt>    regValue |= RSTC_MR_URSTIEN_Msk;
    <#else>
        <#lt>    // Ignoring user reset input, NRST input
    </#if>
    <#if RSTC_MR_CPU_FAULT_RESET == true>
        <#lt>    // Enable CPU fault reset
        <#lt>    regValue |= RSTC_MR_CPUFEN_Msk;
    <#else>
        <#lt>    // No reset on CPU fault
    </#if>
    <#if RSTC_MR_CRYSTAL_FAULT_RESET == true>
        <#lt>    // Enable Slow Clock fault reset
        <#lt>    regValue |= RSTC_MR_SCKSW_Msk;
    <#else>
        <#lt>    // No reset on Slow Clock fault
    </#if>
    <#if RSTC_MR_ASYNCHRONOUS_RESET == true>
        <#lt>    // Reset is asynchronous to slow clock 
        <#lt>    regValue |= RSTC_MR_URSTASYNC_Msk;
    <#else>
        <#lt>    // Reset is synchronous to slow clock 
    </#if>
    <#if RSTC_MR_IMMEDIATE_GPBR_CLEAR == true>
        <#lt>    // Immediate GPBR clear on tamper detection 
        <#lt>    regValue |= RSTC_MR_ENGCLR_Msk;
    <#else>
        <#lt>    // Immediate GPBR clear on tamper detection is off 
    </#if>

    RSTC_REGS->RSTC_MR = regValue;
}

void RSTC${INSTANCE?string}_Reset( RSTC_RESET_TYPE type )
{
    // Issue reset command and wait for command processing
    RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type; 
    while( RSTC_REGS->RSTC_SR & (uint32_t)RSTC_SR_SRCMP_Msk )
    {
        ;   // busy wait
    }
}

RSTC_RESET_CAUSE RSTC${INSTANCE?string}_ResetCauseGet( void )
{
    return (RSTC_RESET_CAUSE)(RSTC_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk);
}

bool RSTC${INSTANCE?string}_NRSTPinRead( void )
{
    return (bool)(RSTC_REGS->RSTC_SR & RSTC_SR_NRSTL_Msk);
}

<#if RSTC_MR_EXTERNAL_RESET_ACTION == "INTERRUPT">
    <#lt>RSTC_OBJECT rstcObj;

    <#lt>void RSTC${INSTANCE?string}_CallbackRegister( RSTC_CALLBACK callback, uintptr_t context )
    <#lt>{
    <#lt>    rstcObj.callback = callback;
    <#lt>    rstcObj.context = context;
    <#lt>}

    <#lt>void RSTC${INSTANCE?string}_InterruptHandler( void )
    <#lt>{
    <#lt>    // Capture the status and clear interrupt.  The RSTC status always has
    <#lt>    // the last reset cause 
    <#lt>    uint32_t interruptStatus = RSTC_REGS->RSTC_SR;
    <#lt>    if( rstcObj.callback != NULL )
    <#lt>    {
    <#lt>        rstcObj.callback( rstcObj.context );
    <#lt>    }
    <#lt>}
</#if>
