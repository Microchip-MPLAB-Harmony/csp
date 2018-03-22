/*******************************************************************************
  Device Service Unit (DSU) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_dsu.h

  Summary:
    DSU PLIB Header File

  Description:
    This file defines the interface to the DSU peripheral library.
    This library provides access to and control of the associated
    peripheral instance.
*******************************************************************************/

/*******************************************************************************
Copyright (c) 2017 released Microchip Technology Inc.  All rights reserved.

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

// DOM-IGNORE-BEGIN
#ifndef PLIB_DSUx_H
#define PLIB_DSUx_H

// *****************************************************************************
// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.*/

#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

#ifdef __cplusplus // Provide C++ Compatibility
extern "C" {
#endif

// DOM-IGNORE-END

// *****************************************************************************
/* Function:
    bool DSUx_CRCCalculate (uint32_t startAddress, size_t size,
                                 uint32_t crcSeed, uint32_t * crc);

  Summary:
    Calculates the CRC Value for the specified address range.

  Description:
    This function uses the hardware CRC computation feature of the DSU to
    calculate the CRC on a memory block. The start address and the size of the
    memory block are specified by startAddress and the size parameters. If this
    is the first block, the value of the crcSeed parameter should be 0xFFFFFFFF.
    For calculating the CRC of non-contiguous memory blocks, the CRC result from
    the CRC calculation of a previous memory block can be passed as the crcSeed
    to the CRC calculation of the next memory block.

    The calcualted CRC is returned in the crc parameter.  This should be
    inverted to match standard CRC implementations. It should be kept
    non-inverted if used as a starting point for subsequent CRC calculations.

  Precondition:
    None.

  Parameters:
    startAddress -  the starting location of the memory block on which the CRC
    calculation needs to be performed. This needs to be aligned on a 4 byte
    boundary.

    length - size of the memory block in terms of 32-bit word.

    crcSeed - Initial crcSeed value. This should be 0xFFFFFFFF for the first
    block. CRC values from the previous calculations can be passed as the CRC
    seed for next calculation while calculating CRC of separate CRC blocks.

    crc - pointer to the return parameter where the calculated CRC result is
    stored. This should be inverted to match standard CRC implementations. This
    should be kept non-inverted if used a starting point for subsequent CRC
    calculations.

  Returns:
    true - The CRC was calculated successfully.
    false - A fault occurred while calculating the CRC.

  Example:
    </code>
        // Calculate the CRC of a memory block starting 0x30000 and 1024 bytes.
        // Note the 1024 bytes is 256 32-bit words

        bool crcStatus;
        uint32_t crcResult;
        crcstatus = DSUx_CRCCalculate((uint32_t)(0x30000), 256, 0xFFFFFFFF,
                                      &crcResult);
        if(crcStatus == true)
        {
            // This is the standard CRC result.
            crcResult = ~crcResult;
        }

        // Calculate the CRC of multiple but separate blocks. Return status is
        // ignored in this example. Note how the intermediate result is not
        // inverted but the final result is.

        bool crcStatus;
        uint32_t crcResult, tempResult;

        DSUx_CRCCalculate((uint32_t)(0x30000), 256, 0xFFFFFFFF, &tempResult);
        DSUx_CRCCalculate((uint32_t)(0x31000), 256, tempResult, &crcResult);

        crcResult = ~crcResult;

    </code>

  Remarks:
    None.
*/

bool DSUx_CRCCalculate (uint32_t startAddress, size_t size, uint32_t crcSeed, uint32_t * crc);

#ifdef __cplusplus // Provide C++ Compatibility
}
#endif

#endif /* PLIB_DSU_H */
