/*******************************************************************************
  RXLP PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${RXLP_INSTANCE_NAME?lower_case}.c

  Summary:
    Low power asynchronous receiver plib.

  Description:
    This implements the peripheral library for the lower power asyncronous
    receiver.  This can be used to wake up the processor from backup.
*******************************************************************************/

// DOM-IGNORE-BEGIN
/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "plib_${RXLP_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: File Scope or Global Constants
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Data Types
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
// *****************************************************************************
// Section: File Scope Helper Macros
// *****************************************************************************
// *****************************************************************************

void ${RXLP_INSTANCE_NAME}_Initialize(void)
{
    ${RXLP_INSTANCE_NAME}_REGS->RXLP_CR = RXLP_CR_RSTRX_Msk;
    ${RXLP_INSTANCE_NAME}_REGS->RXLP_CR = 0;

    ${RXLP_INSTANCE_NAME}_REGS->RXLP_MR = RXLP_MR_FILTER(${FILTER?then("1","0")}) | RXLP_MR_PAR(${PARITY});
    ${RXLP_INSTANCE_NAME}_REGS->RXLP_BRGR = RXLP_BRGR_CD(${CD});

    ${RXLP_INSTANCE_NAME}_REGS->RXLP_CMPR = RXLP_CMPR_VAL1(${VAL1}) | RXLP_CMPR_VAL2(${VAL2});

    ${RXLP_INSTANCE_NAME}_REGS->RXLP_CR = RXLP_CR_RXEN_Msk;
}
/*******************************************************************************
 End of File
*/
