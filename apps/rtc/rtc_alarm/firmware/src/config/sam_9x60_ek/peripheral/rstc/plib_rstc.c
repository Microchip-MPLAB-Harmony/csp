/*******************************************************************************
  Reset Controller Peripheral Library, RSTC PLIB 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rstc.c

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
#include "plib_rstc.h"

// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************
void RSTC_Initialize( void )
{
    // External reset length (0.063 mSecs) 
    uint32_t regValue = RSTC_MR_KEY_PASSWD | RSTC_MR_ERSTL( 0 );
    // Interrupt on NRST input
    regValue |= RSTC_MR_URSTIEN_Msk;
    // No reset on CPU fault
    // No reset on Slow Clock fault
    // Reset is synchronous to slow clock 
    // Immediate GPBR clear on tamper detection is off 

    RSTC_REGS->RSTC_MR = regValue;
}

void RSTC_Reset( RSTC_RESET_TYPE type )
{
    // Issue reset command and wait for command processing
    RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type; 
    while( RSTC_REGS->RSTC_SR & (uint32_t)RSTC_SR_SRCMP_Msk )
    {
        ;   // busy wait
    }
}

RSTC_RESET_CAUSE RSTC_ResetCauseGet( void )
{
    return (RSTC_RESET_CAUSE)(RSTC_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk);
}

bool RSTC_NRSTPinRead( void )
{
    return (bool)(RSTC_REGS->RSTC_SR & RSTC_SR_NRSTL_Msk);
}

RSTC_OBJECT rstcObj;

void RSTC_CallbackRegister( RSTC_CALLBACK callback, uintptr_t context )
{
    rstcObj.callback = callback;
    rstcObj.context = context;
}

void RSTC_InterruptHandler( void )
{
    // Capture the status and clear interrupt.  The RSTC status always has
    // the last reset cause 
    uint32_t interruptStatus = RSTC_REGS->RSTC_SR;
    if( rstcObj.callback != NULL )
    {
        rstcObj.callback( rstcObj.context );
    }
}
