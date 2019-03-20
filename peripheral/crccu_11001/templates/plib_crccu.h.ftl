/*******************************************************************************
  Digital-to-Analog Converter (${CRCCU_INSTANCE_NAME}) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${CRCCU_INSTANCE_NAME?lower_case}.h

  Summary:
    ${CRCCU_INSTANCE_NAME} PLIB Header file

  Description:
    This file defines the interface to the CRCCU peripheral library. This
    library provides access to and control of the associated peripheral
    instance.

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

#ifndef PLIB_${CRCCU_INSTANCE_NAME}_H
#define PLIB_${CRCCU_INSTANCE_NAME}_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.
*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

typedef enum
{
    /* CCITT8023 Polynom 0x04C11DB7*/
    CRCCU_POLYNOMIAL_CCITT8023,

    /* CASTAGNOLI Polynom 0x1EDC6F41 */
    CRCCU_POLYNOMIAL_CASTAGNOLI,

    /* CCITT16 Polynom 0x1021 */
    CRCCU_POLYNOMIAL_CCITT16

} CRCCU_POLYNOMIAL;

typedef enum
{
    /* BYTE Transfer*/
    CRCCU_TWIDTH_BYTE,

    /* Halfword Transfer */
    CRCCU_TWIDTH_HALFWORD,

    /* Word Transfer */
    CRCCU_TWIDTH_WORD
    
} CRCCU_TWIDTH;

/** CRCCU descriptor type */
typedef struct crccu_dscr_type {
	uint32_t ul_tr_addr;	/* TR_ADDR */
	uint32_t ul_tr_ctrl;	/* TR_CTRL */
	uint32_t ul_reserved[2];	/* Reserved register */
	uint32_t ul_tr_crc;	/* TR_CRC */
} crccu_dscr_type_t;

void ${CRCCU_INSTANCE_NAME}_Initialize (void);
bool ${CRCCU_INSTANCE_NAME}_CRCCalculate(uint32_t startAddress, uint16_t length, uint32_t * crc, bool chain);
void ${CRCCU_INSTANCE_NAME}_Setup (CRCCU_POLYNOMIAL polynomial, CRCCU_TWIDTH width);
bool ${CRCCU_INSTANCE_NAME}_CRCCalculateAndCompare (uint32_t startAddress, uint16_t length, uint32_t crc, bool chain);
#ifdef __cplusplus  // Provide C++ Compatibility
}
#endif

#endif /* PLIB_${CRCCU_INSTANCE_NAME}_H */
