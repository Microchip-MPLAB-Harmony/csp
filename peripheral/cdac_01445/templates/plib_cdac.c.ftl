/*******************************************************************************
  Control Digital-to-Analog Converter (${CDAC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CDAC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${CDAC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the CDAC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#include "plib_${CDAC_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${CDAC_INSTANCE_NAME} Interface Routines
// *****************************************************************************
// *****************************************************************************

void ${CDAC_INSTANCE_NAME}_Initialize( void )
{
    /* Configure reference source */
    DAC${CDAC_INSTANCE_NUMBER}CONbits.REFSEL = ${CDAC_REFSEL};

    /* Configure output buffer enable */
    DAC${CDAC_INSTANCE_NUMBER}CONbits.DACOE = ${CDAC_DACOE};

    /* Enable ${CDAC_INSTANCE_NAME} */
    DAC${CDAC_INSTANCE_NUMBER}CONbits.ON = 1;
}

void ${CDAC_INSTANCE_NAME}_DataWrite( uint16_t data )
{
    /* Write input data */
    DAC${CDAC_INSTANCE_NUMBER}CONbits.DACDAT = data;
}