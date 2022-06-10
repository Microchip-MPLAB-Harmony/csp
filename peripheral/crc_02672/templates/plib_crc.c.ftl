/*******************************************************************************
  Cyclic Redundancy Check (${CRC_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CRC_INSTANCE_NAME?lower_case}.c

  Summary:
    ${CRC_INSTANCE_NAME} PLIB Implementation file

  Description:
    This file defines the interface to the CRC peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

*******************************************************************************/
// DOM-IGNORE-BEGIN
/*******************************************************************************
* Copyright (C) 2021 Microchip Technology Inc. and its subsidiaries.
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

#include "plib_${CRC_INSTANCE_NAME?lower_case}.h"

static CRC_SETUP gCRCSetup;

// *****************************************************************************
/* Function:
   static uint32_t ${CRC_INSTANCE_NAME}_BitReverse( uint32_t num, uint32_t bits)

  Summary:
    Reverses the bits in the given number

  Description:
    Reverses the bits in the given number based on the size of the number.
    Example:
        number  = 10110011
        reverse = 11001101

  Parameters:
    num - Number to be reversed
    bits - size of the number (8, 16, 32)

  Returns:
    reversed number
*/
static uint32_t ${CRC_INSTANCE_NAME}_BitReverse( uint32_t num, uint32_t bits)
{
    uint32_t out = 0;
    uint32_t i;

    for( i = 0U; i < bits; i++ )
    {
        out <<= 1U;

        if(( num & 1U ) != 0U)
        {
            out |= 1U;
        }

        num >>= 1U;
    }

    return out;
}

void ${CRC_INSTANCE_NAME}_CRCSetup(CRC_SETUP CRCSetup)
{
	uint8_t temp = (gCRCSetup.polynomial_length - 1U);
    gCRCSetup.reverse_crc_input     = CRCSetup.reverse_crc_input;
    gCRCSetup.polynomial_length     = CRCSetup.polynomial_length;
    gCRCSetup.polynomial            = CRCSetup.polynomial;
    gCRCSetup.final_xor_value       = CRCSetup.final_xor_value;
    gCRCSetup.reverse_crc_output    = CRCSetup.reverse_crc_output;

    CRCCON = 0;
    CRCXOR = 0;
    CRCWDAT = 0;

    CRCCONbits.MOD = 1;

    if (gCRCSetup.reverse_crc_input == true)
    {
        CRCCONbits.LENDIAN = 1;
    }

    CRCCONbits.PLEN = temp;

    CRCCONbits.ON = 1;

    /* Store the polynomial value */
    CRCXOR = gCRCSetup.polynomial;
}

void ${CRC_INSTANCE_NAME}_CRCEnable( bool enable)
{
    if (enable == true)
    {
        CRCCONbits.ON = 1;
    }
    else
    {
        CRCCONbits.ON = 0;
    }
}

uint32_t ${CRC_INSTANCE_NAME}_CRCCalculate(void *buffer, uint32_t length, uint32_t seed)
{
    uint32_t crc = 0;
    uint8_t *buffer_8 = buffer;

    /* Suspend Any CRC Calculation */
    CRCCONbits.CRCGO = 0;

    /* Configuring Data Width to 8-Bit */
    CRCCONbits.DWIDTH = (CRC_DATA_WIDTH_BYTE - 1U);

    /* Set the Initial Seed value */
    CRCWDAT = seed;

    /* Clear the interrupt flag */
    IFS0CLR = _IFS0_CRCIF_MASK;

    /* Start CRC Calculation */
    CRCCONbits.CRCGO = 1;

    while(length > 1U)
    {
        /* Wait if FIFO is full */
        while((CRCCONbits.CRCFUL) != 0U)
        {
        }

        /* When Using Data Width to 8-bit, a byte access to the
         * CRCDAT register must be used
        */
        *((uint8_t *)&CRCDAT) = *buffer_8++;

        length--;
    }

    /* Suspend CRC Calculation and Clear interrupt flag */
    CRCCONbits.CRCGO = 0;

    IFS0CLR = _IFS0_CRCIF_MASK;

    /* Write the last Data into FIFO for completing the CRC Calculation */
    *((uint8_t *)&CRCDAT) = *buffer_8;

    /* Resume CRC Calculation */
    CRCCONbits.CRCGO = 1;

    /* Wait until CRC Calculation is completed */
    while(IFS0bits.CRCIF == 0U)
    {
    }

    /* Read the generated CRC value. */
    crc = CRCWDAT;

    /* Reverse the final crc value */
    if (gCRCSetup.reverse_crc_output == true)
    {
        crc = ${CRC_INSTANCE_NAME}_BitReverse(crc, gCRCSetup.polynomial_length);
    }

    crc ^= gCRCSetup.final_xor_value;

    return crc;
}
