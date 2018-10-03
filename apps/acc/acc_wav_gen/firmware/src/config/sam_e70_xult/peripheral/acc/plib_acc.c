/*******************************************************************************
  Analog Comparator Controller (ACC) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_acc.c

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
#include "plib_acc.h"

// *****************************************************************************
// *****************************************************************************
// Section: ACC Implementation
// *****************************************************************************
// *****************************************************************************

void ACC_Initialize (void)
{
    /*Reset ACC registers*/
	ACC_REGS->ACC_CR = ACC_CR_SWRST_Msk;
    
    /*Set Comparator Positive and Negative Input, Output Invert status to 
      Enable/Disable, Fault Generation to Enable/Disable, Set Fault source and 
      Output Edge type*/
	ACC_REGS->ACC_MR = ACC_MR_SELMINUS(0x2)| ACC_MR_SELPLUS(0x0) | ACC_MR_EDGETYP(0x2) \
							  | ACC_MR_SELFS_CE | ACC_MR_ACEN_Msk;

    /*Set Current level and Hysteresis level*/    
    ACC_REGS->ACC_ACR = ACC_ACR_ISEL_LOPW | ACC_ACR_HYST(0);       

	
    /*Wait till output mask period gets over*/
    while (ACC_REGS->ACC_ISR& (uint32_t) ACC_ISR_MASK_Msk);  
}

bool ACC_StatusGet (ACC_STATUS_SOURCE status)
{
    return (bool)(ACC_REGS->ACC_ISR& status); 
}


