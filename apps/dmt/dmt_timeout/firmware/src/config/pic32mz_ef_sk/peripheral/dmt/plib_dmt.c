/*******************************************************************************
  Real Time Counter (DMT) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dmt.c

  Summary:
    DMT PLIB Implementation file

  Description:
    This file defines the interface to the deadman timer (DMT) peripheral library. 
    This library provides ability to clear the DMT counter.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
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
/* This section lists the other files that are included in this file.
*/
#include "plib_dmt.h"


// *****************************************************************************
/* Function:
   void DMT_Clear ( void )

  Summary:
    Clears DMT counter.

  Description:
    This function clears the DMT counter by writing specific numbers to DMT 
    registers in the proper order.

  Parameters:
    none

  Returns:
    void
*/
void DMT_Clear ( void )
{
    /* DMTPRECLR register */
    /*     STEP1 = 64 */
    DMTPRECLR = 16384;
    
    /* DMTCLR register */
    /*     STEP2 = 8 */
    DMTCLR = 8;
}
