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
