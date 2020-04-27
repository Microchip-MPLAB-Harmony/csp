/*******************************************************************************
  Input Capture (ICAP1) Peripheral Library (PLIB)

  Company:
    Microchip Technology Inc.

  File Name:
    plib_icap1.c

  Summary:
    ICAP1 Source File

  Description:
    None

*******************************************************************************/

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
#include "plib_icap1.h"

// *****************************************************************************

// *****************************************************************************
// Section: ICAP1 Implementation
// *****************************************************************************
// *****************************************************************************


void ICAP1_Initialize (void)
{
    /*Setup IC1CON    */
    /*ICM     = 1        */
    /*ICI     = 0        */
    /*ICTMR = 1*/
    /*C32     = 0        */
    /*FEDGE = 0        */
    /*SIDL     = false    */

    IC1CON = 0x81;



}


void ICAP1_Enable (void)
{
    IC1CONSET = _IC1CON_ON_MASK;
}


void ICAP1_Disable (void)
{
    IC1CONCLR = _IC1CON_ON_MASK;
}

uint16_t ICAP1_CaptureBufferRead (void)
{
    return (uint16_t)IC1BUF;
}




bool ICAP1_CaptureStatusGet (void)
{
    bool status = false;
    status = ((IC1CON >> ICAP_STATUS_BUFNOTEMPTY) & 0x1);
    return status;
}

bool ICAP1_ErrorStatusGet (void)
{
    bool status = false;
    status = ((IC1CON >> ICAP_STATUS_OVERFLOW) & 0x1);
    return status;
}
