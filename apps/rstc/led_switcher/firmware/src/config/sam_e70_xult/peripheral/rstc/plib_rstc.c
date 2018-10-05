/*******************************************************************************
  Reset Controller (RSTC) Peripheral Library(PLIB) Source file 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rstc.c

  Summary:
    RSTC Source File

  Description:
    None

*******************************************************************************/

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

#include "plib_rstc.h"

// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************

void RSTC_Initialize (void)
{
    RSTC_REGS->RSTC_MR = (RSTC_MR_URSTIEN_Msk | RSTC_MR_ERSTL(0) | RSTC_MR_KEY_PASSWD);
}

void RSTC_Reset (RSTC_RESET_TYPE type)
{
	/* Issue reset command 				*/
    RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type; 
	
    /*Wait for processing reset command */
    while (RSTC_REGS->RSTC_SR& (uint32_t) RSTC_SR_SRCMP_Msk);  
}

RSTC_RESET_CAUSE RSTC_ResetCauseGet (void)
{
    return (RSTC_RESET_CAUSE) (RSTC_REGS->RSTC_SR& RSTC_SR_RSTTYP_Msk);
}


RSTC_OBJECT rstcObj;

void RSTC_CallbackRegister (RSTC_CALLBACK callback, uintptr_t context)
{
    rstcObj.callback = callback;
    rstcObj.context = context;
}

void RSTC_InterruptHandler( void )
{
	// Clear the interrupt flag
	RSTC_REGS->RSTC_SR;

	// Callback user function
	if(rstcObj.callback != NULL)
	{
        rstcObj.callback(rstcObj.context);		
	}
}
