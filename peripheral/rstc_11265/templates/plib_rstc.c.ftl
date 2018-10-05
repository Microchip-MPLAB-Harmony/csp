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
Copyright (c) 2018 released Microchip Technology Inc. All rights reserved.
Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION, ANY WARRANTY OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE.
IN NO EVENT SHALL MICROCHIP OR ITS LICENSORS BE LIABLE OR OBLIGATED UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION, BREACH OF WARRANTY, OR
OTHER LEGAL EQUITABLE THEORY ANY DIRECT OR INDIRECT DAMAGES OR EXPENSES
INCLUDING BUT NOT LIMITED TO ANY INCIDENTAL, SPECIAL, INDIRECT, PUNITIVE OR
CONSEQUENTIAL DAMAGES, LOST PROFITS OR LOST DATA, COST OF PROCUREMENT OF
SUBSTITUTE GOODS, TECHNOLOGY, SERVICES, OR ANY CLAIMS BY THIRD PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE THEREOF), OR OTHER SIMILAR COSTS.
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
    <#if RSTC_MR_URSTEN == "RESET">
    // Enable Reset
    RSTC_REGS->RSTC_MR = (RSTC_MR_KEY_PASSWD | RSTC_MR_URSTEN_Msk);
    <#elseif RSTC_MR_URSTEN == "INTERRUPT">
    // Enable Interrupt 
    RSTC_REGS->RSTC_MR = (RSTC_MR_KEY_PASSWD | RSTC_MR_URSTIEN_Msk);
    <#else>
    // NRST input pin is ignored
    RSTC_REGS->RSTC_MR = RSTC_MR_KEY_PASSWD;
    </#if>
}

void RSTC${INSTANCE?string}_Reset( RSTC_RESET_TYPE type )
{
    /* Issue reset command */
    RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type; 
    /* Wait for command processing */
    while( RSTC_REGS->RSTC_SR & (uint32_t)RSTC_SR_SRCMP_Msk );
}

RSTC_RESET_CAUSE RSTC${INSTANCE?string}_ResetCauseGet( void )
{
    return (RSTC_RESET_CAUSE)(RSTC_REGS->RSTC_SR & RSTC_SR_RSTTYP_Msk);
}

bool RSTC${INSTANCE?string}_NRSTPinRead( void )
{
    return (bool)(RSTC_REGS->RSTC_SR & RSTC_SR_NRSTL_Msk);
}
<#if RSTC_MR_URSTEN == "INTERRUPT">

RSTC_OBJECT rstcObj;

void RSTC${INSTANCE?string}_CallbackRegister( RSTC_CALLBACK callback, uintptr_t context )
{
    rstcObj.callback = callback;
    rstcObj.context = context;
}

void RSTC${INSTANCE?string}_InterruptHandler( void )
{
    // Clear the interrupt flag
    RSTC_REGS->RSTC_SR;

    // Callback user function
    if( rstcObj.callback != NULL ) {
        rstcObj.callback( rstcObj.context );		
    }
}
</#if>
