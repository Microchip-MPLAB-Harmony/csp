/*******************************************************************************
  RXLP PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_rxlp.c

  Summary:
    Low power asynchronous receiver plib.

  Description:
    This implements the peripheral library for the lower power asyncronous
    receiver.  This can be used to wake up the processor from backup.
*******************************************************************************/

// DOM-IGNORE-BEGIN
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
// DOM-IGNORE-END


// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
#include "plib_rxlp.h"
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

void RXLP_Initialize(void)
{
    RXLP_REGS->RXLP_CR = RXLP_CR_RSTRX_Msk;
    RXLP_REGS->RXLP_CR = 0;

    RXLP_REGS->RXLP_MR = RXLP_MR_FILTER(0) | RXLP_MR_PAR(0x4);
    RXLP_REGS->RXLP_BRGR = RXLP_BRGR_CD(1);

    RXLP_REGS->RXLP_CMPR = RXLP_CMPR_VAL1(0) | RXLP_CMPR_VAL2(255);

    RXLP_REGS->RXLP_CR = RXLP_CR_RXEN_Msk;
}
/*******************************************************************************
 End of File
*/
