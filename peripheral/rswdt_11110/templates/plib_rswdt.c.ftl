/*******************************************************************************
  RSWDT Peripheral Library

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rswdt.c

  Summary:
    RSWDT Source File

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

#include "plib_rswdt${rswdtIndex?string}.h"

void RSWDT${rswdtIndex?string}_Initialize( void )
{
	_RSWDT_REGS->RSWDT_MR.w = RSWDT_MR_ALLONES_Msk | RSWDT_MR_WDV(${rswdtWDV}) \
							${rswdtdebugHalt?then(' | RSWDT_MR_WDDBGHLT_Msk','')}${rswdtidleHalt?then(' | RSWDT_MR_WDIDLEHLT_Msk','')}${rswdtEnableReset?then(' | RSWDT_MR_WDRSTEN_Msk','')}${rswdtinterruptMode?then(' | RSWDT_MR_WDFIEN_Msk','')};
							
}

void RSWDT${rswdtIndex?string}_Clear(void)
{
	_RSWDT_REGS->RSWDT_CR.w = (RSWDT_CR_KEY_PASSWD|RSWDT_CR_WDRSTT_Msk);
}

<#if rswdtinterruptMode == true>
	<#lt>void RSWDT${rswdtIndex?string}_CallbackRegister( RSWDT_CALLBACK callback, uintptr_t context )
	<#lt>{
	<#lt>	rswdt.callback = callback;
	<#lt>	rswdt.context = context;
	<#lt>}
</#if>
