/*******************************************************************************
  SSC PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_ssc.h

  Summary:
    SSC PLIB Common Header File

  Description:
    This file has prototype of all the interfaces which are common for all the
    SSC peripherals.

*******************************************************************************/

/*******************************************************************************
Copyright (c) 2018 released Microchip Technology Inc.  All rights reserved.

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

#ifndef PLIB_SSC_H
#define PLIB_SSC_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>


/* Provide C++ Compatibility */
#ifdef __cplusplus  

    extern "C" {

#endif

/****************************** SSC${SSC_INDEX?string} Interface *********************************/

#if 0
typedef enum
{
    SSC_CLOCK_PHASE_TRAILING_EDGE = 0 << SSC_CSR_NCPHA_Pos,
    SSC_CLOCK_PHASE_LEADING_EDGE = 1 << SSC_CSR_NCPHA_Pos
    
}SSC_CLOCK_PHASE;

typedef enum
{
    SSC_CLOCK_POLARITY_IDLE_LOW = 0 << SSC_CSR_CPOL_Pos,
    SSC_CLOCK_POLARITY_IDLE_HIGH = 1 << SSC_CSR_CPOL_Pos
    
}SSC_CLOCK_POLARITY;

typedef enum
{
    SSC_DATA_BITS_8 = SSC_CSR_BITS_8_BIT_Val,
    SSC_DATA_BITS_9 = SSC_CSR_BITS_9_BIT_Val,
    SSC_DATA_BITS_10 = SSC_CSR_BITS_10_BIT_Val,
    SSC_DATA_BITS_11 = SSC_CSR_BITS_11_BIT_Val,
    SSC_DATA_BITS_12 = SSC_CSR_BITS_12_BIT_Val,
    SSC_DATA_BITS_13 = SSC_CSR_BITS_13_BIT_Val,
    SSC_DATA_BITS_14 = SSC_CSR_BITS_14_BIT_Val,
    SSC_DATA_BITS_15 = SSC_CSR_BITS_15_BIT_Val,
    SSC_DATA_BITS_16 = SSC_CSR_BITS_16_BIT_Val

}SSC_DATA_BITS;
#endif

// *****************************************************************************
// *****************************************************************************
// Section: Local: **** Do Not Use ****
// *****************************************************************************
// *****************************************************************************

/* Provide C++ Compatibility */
#ifdef __cplusplus

    }
    
#endif

#endif // PLIB_SSC_H

/*******************************************************************************
 End of File
*/