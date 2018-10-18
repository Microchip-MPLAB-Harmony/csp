/*******************************************************************************
  Device Service Unit (DSU) PLIB

  Company:
    Microchip Technology Inc.

  File Name:
    plib_${DSU_INSTANCE_NAME?lower_case}.c

  Summary:
    ${DSU_INSTANCE_NAME} PLIB Implementation File

  Description:
    This file contains the implementation of the DSU Peripheral Library. This is
    generated file.

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

// *****************************************************************************
// Section: Included Files
// *****************************************************************************
// *****************************************************************************
/* This section lists the other files that are included in this file.*/

#include "plib_${DSU_INSTANCE_NAME?lower_case}.h"
#include "device.h"

// *****************************************************************************
// *****************************************************************************
// Section: ${DSU_INSTANCE_NAME} CRC Implementation
// *****************************************************************************
// *****************************************************************************

bool ${DSU_INSTANCE_NAME}_CRCCalculate (uint32_t startAddress, size_t length, uint32_t crcSeed, uint32_t * crc)
{
    bool statusValue = false;

    if( (0 != length) && (NULL != crc) )
    {
        ${DSU_INSTANCE_NAME}_REGS->DSU_ADDR = startAddress;

        ${DSU_INSTANCE_NAME}_REGS->DSU_LENGTH = (uint32_t)length;

        /* Initial CRC Value  */
        ${DSU_INSTANCE_NAME}_REGS->DSU_DATA = crcSeed;

        /* Clear Status Register */
        ${DSU_INSTANCE_NAME}_REGS->DSU_STATUSA = ${DSU_INSTANCE_NAME}_REGS->DSU_STATUSA;

        ${DSU_INSTANCE_NAME}_REGS->DSU_CTRL = DSU_CTRL_CRC_Msk;

        while(!(${DSU_INSTANCE_NAME}_REGS->DSU_STATUSA & DSU_STATUSA_DONE_Msk))
        {
            /* Wait for the DSU Operation to Complete */
        }

        if(!(${DSU_INSTANCE_NAME}_REGS->DSU_STATUSA & DSU_STATUSA_BERR_Msk))
        {
            /* Reading the resultant crc value from the DATA register */
            *crc = (uint32_t) ${DSU_INSTANCE_NAME}_REGS->DSU_DATA;

            statusValue = true;
        }
    }

    return statusValue;
}
