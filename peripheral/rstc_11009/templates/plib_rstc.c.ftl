/*******************************************************************************
  Reset Controller (RSTC) Peripheral Library(PLIB) Source file 

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rstc${INDEX?string}.c

  Summary:
    RSTC Source File

  Description:
    None

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

Microchip licenses to you the right to use, modify, copy and distribute
Software only when embedded on a Microchip microcontroller or digital signal
controller that is integrated into your product or third party product
(pursuant to the sublicense terms in the accompanying license agreement).

You should refer to the license agreement accompanying this Software for
additional information regarding your rights and obligations.

SOFTWARE AND DOCUMENTATION ARE PROVIDED AS IS  WITHOUT  WARRANTY  OF  ANY  KIND,
EITHER EXPRESS  OR  IMPLIED,  INCLUDING  WITHOUT  LIMITATION,  ANY  WARRANTY  OF
MERCHANTABILITY, TITLE, NON-INFRINGEMENT AND FITNESS FOR A  PARTICULAR  PURPOSE.
IN NO EVENT SHALL MICROCHIP OR  ITS  LICENSORS  BE  LIABLE  OR  OBLIGATED  UNDER
CONTRACT, NEGLIGENCE, STRICT LIABILITY, CONTRIBUTION,  BREACH  OF  WARRANTY,  OR
OTHER LEGAL  EQUITABLE  THEORY  ANY  DIRECT  OR  INDIRECT  DAMAGES  OR  EXPENSES
INCLUDING BUT NOT LIMITED TO ANY  INCIDENTAL,  SPECIAL,  INDIRECT,  PUNITIVE  OR
CONSEQUENTIAL DAMAGES, LOST  PROFITS  OR  LOST  DATA,  COST  OF  PROCUREMENT  OF
SUBSTITUTE  GOODS,  TECHNOLOGY,  SERVICES,  OR  ANY  CLAIMS  BY  THIRD   PARTIES
(INCLUDING BUT NOT LIMITED TO ANY DEFENSE  THEREOF),  OR  OTHER  SIMILAR  COSTS.
*******************************************************************************/

#include "plib_rstc${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: RSTC Implementation
// *****************************************************************************
// *****************************************************************************

void RSTC${INDEX?string}_Initialize (void)
{
    <#if RSTC_MR_URSTEN == "RESET">
    RSTC_REGS->RSTC_MR = (RSTC_MR_URSTEN_Msk | RSTC_MR_ERSTL(${RSTC_MR_ERSTL}) | RSTC_MR_KEY_PASSWD);
    <#else>
    RSTC_REGS->RSTC_MR = (RSTC_MR_URSTIEN_Msk | RSTC_MR_ERSTL(${RSTC_MR_ERSTL}) | RSTC_MR_KEY_PASSWD);
    </#if>
}

void RSTC${INDEX?string}_Reset (RSTC_RESET_TYPE type)
{
	/* Issue reset command 				*/
    RSTC_REGS->RSTC_CR = RSTC_CR_KEY_PASSWD | type; 
	
    /*Wait for processing reset command */
    while (RSTC_REGS->RSTC_SR& (uint32_t) RSTC_SR_SRCMP_Msk);  
}

RSTC_RESET_CAUSE RSTC${INDEX?string}_ResetCauseGet (void)
{
    return (RSTC_RESET_CAUSE) (RSTC_REGS->RSTC_SR& RSTC_SR_RSTTYP_Msk);
}

<#if RSTC_MR_URSTEN == "GPIO">
bool RSTC${INDEX?string}_NRSTPinRead (void)
{
    return  (bool) (RSTC_REGS->RSTC_SR& RSTC_SR_NRSTL_Msk);
}
</#if>

<#if RSTC_MR_URSTEN == "INTERRUPT">
RSTC_OBJECT rstcObj;

void RSTC${INDEX?string}_CallbackRegister (RSTC_CALLBACK callback, uintptr_t context)
{
    rstcObj.callback = callback;
    rstcObj.context = context;
}

void RSTC${INDEX?string}_InterruptHandler( void )
{
	// Clear the interrupt flag
	RSTC_REGS->RSTC_SR;

	// Callback user function
	if(rstcObj.callback != NULL)
	{
        rstcObj.callback(rstcObj.context);		
	}
}
</#if>