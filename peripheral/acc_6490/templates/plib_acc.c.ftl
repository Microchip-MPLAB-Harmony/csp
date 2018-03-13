/*******************************************************************************
  Analog Comparator Controller (ACC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_acc${INDEX?string}.c

  Summary:
    ACC Source File

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
#include "plib_acc${INDEX?string}.h"

<#--Implementation-->
// *****************************************************************************
// *****************************************************************************
// Section: ACC Implementation
// *****************************************************************************
// *****************************************************************************

void ACC${INDEX?string}_Initialize (void)
{
    /*Reset ACC registers*/
	_ACC_REGS->ACC_CR.w = ACC_CR_SWRST_Msk;
    
    /*Set Comparator Positive and Negative Input, Output Invert status to 
      Enable/Disable, Fault Generation to Enable/Disable, Set Fault source and 
      Output Edge type*/
	_ACC_REGS->ACC_MR.w = ACC_MR_SELMINUS(${ACC_MR_SELMINUS})| ACC_MR_SELPLUS(${ACC_MR_SELPLUS}) | ACC_MR_EDGETYP(${ACC_MR_EDGETYPE}) \
							${ACC_ACR_INV?then('| ACC_MR_INV_Msk', '')} ${ACC_ACR_FE?then('| ACC_MR_FE_Msk', '')} | ACC_MR_SELFS_${ACC_MR_SELFS} | ACC_MR_ACEN_Msk;

    /*Set Current level and Hysteresis level*/    
    _ACC_REGS->ACC_ACR.w = ACC_ACR_ISEL_${ACC_ACR_ISEL} | ACC_ACR_HYST(${ACC_ACR_HYST});       

    <#if INTERRUPT_MODE == true>
	/* Enable Interrupt 	*/
    _ACC_REGS->ACC_IER.w = ACC_IER_CE_Msk;
    </#if>
	
    /*Wait till output mask period gets over*/
    while (_ACC_REGS->ACC_ISR.w & (uint32_t) ACC_ISR_MASK_Msk);  
}

bool ACC${INDEX?string}_StatusGet (ACC_STATUS_SOURCE status)
{
    return (bool)(_ACC_REGS->ACC_ISR.w & status); 
}

<#if INTERRUPT_MODE == true>

ACC_OBJECT acc${INDEX?string}Obj;

void ACC${INDEX?string}_CallbackRegister (ACC_CALLBACK callback, uintptr_t context)
{
    acc${INDEX?string}Obj.callback = callback;
    acc${INDEX?string}Obj.context = context;
}

void ACC${INDEX?string}_InterruptHandler( void )
{
	// Clear the interrupt
    _ACC_REGS->ACC_ISR.w; 

	// Callback user function 
	if(acc${INDEX?string}Obj.callback != NULL)
	{
        acc${INDEX?string}Obj.callback(acc${INDEX?string}Obj.context);		
	}
}
</#if>

