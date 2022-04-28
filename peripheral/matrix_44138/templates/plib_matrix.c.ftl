/*******************************************************************************
  Matrix (AHB) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_matrix.c

  Summary:
    AHB Matrix PLIB implementation file

  Description:
    Configure AHB masters and slaves.
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
#include <device.h>
#include "plib_matrix.h"

// *****************************************************************************

void MATRIX_Initialize(void)
{
<#if CoreSeries == "SAMRH707">
    /* Set FlexRAM memory in user mode */
    MATRIX0_REGS->MATRIX_PASSR[0]= 0xFF;
    MATRIX0_REGS->MATRIX_PSR[0]= 0x00030303;
    MATRIX0_REGS->MATRIX_PASSR[1]= 0xFF;
    MATRIX0_REGS->MATRIX_PSR[1]= 0x00030303;
    MATRIX0_REGS->MATRIX_PASSR[7]= 0xFF;
    MATRIX0_REGS->MATRIX_PSR[7]= 0x00030303;

    /* Set AHB Slave in user mode */
    MATRIX0_REGS->MATRIX_PSR[6] = 0xF;
    MATRIX0_REGS->MATRIX_PASSR[6] = 0x00070707;

    /* Set HEFC TOP value and set memory in user mode */
    MATRIX0_REGS->MATRIX_PASSR[2] = 0x5;
    MATRIX0_REGS->MATRIX_PSR[2] = 0x00010101;
    MATRIX0_REGS->MATRIX_PRTSR[2] = 0x5;

    /* Enable Master Remap Control for ICM to access address 0 */
    MATRIX0_REGS->MATRIX_MRCR |= (1 << 11);
<#else>
    MATRIX0_REGS->MATRIX_PASSR[0]= 0x00000FFF;
    MATRIX0_REGS->MATRIX_PSR[0]= 0x07070707;
    MATRIX0_REGS->MATRIX_PASSR[1]= 0x00000FFF;
    MATRIX0_REGS->MATRIX_PSR[1]= 0x07070707;
    MATRIX0_REGS->MATRIX_PSR[6] = 0x07070707;
    MATRIX0_REGS->MATRIX_PASSR[6] = 0x00000FFF;
    MATRIX0_REGS->MATRIX_PASSR[7]= 0x00000FFF;
    MATRIX0_REGS->MATRIX_PSR[7]= 0x07070707;
</#if>
}

/*******************************************************************************
 End of File
*/
