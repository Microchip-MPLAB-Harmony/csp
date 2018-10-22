/*******************************************************************************
  SHDWC PLIB Implementation

  Company:
    Microchip Technology Inc.

  File Name:
    plib_shdwc.c

  Summary:
    Shutdown Controller PLIB

  Description:
    Shutdown Controller PLIB Implementation
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
#include "device.h"
#include "plib_shdwc.h"
#include <stdint.h>

void SHDWC_Initialize(void)
{
    SHDWC_REGS->SHDW_MR =  SHDW_MR_RXLPWKEN_Msk | 
        SHDW_MR_WKUPDBC(0x0);

    SHDWC_REGS->SHDW_WUIR = 0  | SHDW_WUIR_WKUPEN2_ENABLE  | SHDW_WUIR_WKUPT2_LOW  | SHDW_WUIR_WKUPEN0_ENABLE  | SHDW_WUIR_WKUPT0_LOW ;
}

void SHDWC_Shutdown(void)
{
    /* Clear previous wake-up event before shutdown */
    SHDWC_GetWakeup();
    SHDWC_REGS->SHDW_CR = SHDW_CR_KEY_PASSWD | SHDW_CR_SHDW_Msk;
}

uint32_t SHDWC_GetWakeup(void)
{
    return SHDWC_REGS->SHDW_SR;
}

/*******************************************************************************
 End of File
*/
